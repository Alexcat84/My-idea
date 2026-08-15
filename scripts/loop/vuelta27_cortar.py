"""Vuelta 27, fase 01: EL CORTE. Separa el bloque injertado de un nodo y lo
lleva a su destino, segun un PLAN declarativo que este script no decide.

El plan lo escribe el ejecutor por lectura (P.18) y vive en docs/loop/PLAN_V27_*.json.
Este script solo aplica lo escrito, con guardas:

  * SIMULACION SOBRE COPIA EN MEMORIA por defecto: no escribe nada.
  * GUARDA DE TEXTO: cada paso que sale se comprueba contra el prefijo escrito en
    el plan. Si el nodo cambio bajo los pies, PARA y no toca nada.
  * GUARDA DE FUENTE: la fuente de hoy tiene que ser exactamente la esperada.
  * GUARDA DE DESTINO: un nodo propio nuevo no puede existir ya, y su titulo no
    puede estar repetido exacto en el grafo.
  * CERO PERDIDA: la union de los pasos que se quedan y los que viajan tiene que
    cubrir todos los pasos de origen, salvo que el plan declare un destejido con
    su mapa explicito.
  * EL FINAL DE FICHERO SE PRESERVA TAL CUAL (leccion de la vuelta 26).

Uso:
    python scripts/loop/vuelta27_cortar.py <plan.json> --simular
    python scripts/loop/vuelta27_cortar.py <plan.json> --ejecutar
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def leer_crudo(nid):
    with open(ruta(nid), encoding="utf-8", newline="") as fh:
        crudo = fh.read()
    return json.loads(crudo), ("\n" if crudo.endswith("\n") else "")


def escribir(nid, datos, cola):
    with open(ruta(nid), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def titulos_del_grafo():
    fuera = {}
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        with open(os.path.join(NODOS, nombre), encoding="utf-8") as fh:
            d = json.load(fh)
        fuera.setdefault((d.get("titulo_concepto") or "").strip(), []).append(d["node_id"])
    return fuera


CAMPOS_NODO = [
    "node_id", "fase_proyecto", "dominio", "titulo_concepto", "fuente",
    "resumen_teorico", "pasos_accionables", "entregable_esperado",
    "nodos_previos", "nodos_siguientes", "condiciones_activacion",
    "etiqueta_arbol",
]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    plan_path = sys.argv[1]
    modo = sys.argv[2] if len(sys.argv) > 2 else "--simular"
    if modo not in ("--simular", "--ejecutar"):
        print(__doc__)
        return 2

    plan = json.load(open(plan_path, encoding="utf-8"))
    titulos = titulos_del_grafo()
    print("PLAN   : %s" % plan_path)
    print("OPERACION: %s" % plan["operacion"])
    print("MODO   : %s" % modo)
    print("CORTES : %d" % len(plan["cortes"]))
    print("=" * 78)

    fallos = []
    escrituras = []   # (nid, datos, cola)
    nuevos = []

    # el estado en memoria: un nodo puede recibir de dos cortes distintos
    memoria = {}
    # UN NODO PUEDE TENER DOS BLOQUES CON DESTINOS DISTINTOS (asociaciones_clave,
    # transicion_producto_a_experiencia). Los indices de TODOS sus cortes se leen
    # contra los pasos ORIGINALES, no contra el nodo ya recortado por el corte
    # anterior: si no, el segundo corte se lleva el paso equivocado y la guarda de
    # texto no lo veria porque los prefijos tambien se habrian corrido.
    originales = {}
    fuentes_originales = {}
    removidos = {}

    def cargar(nid):
        if nid not in memoria:
            memoria[nid] = leer_crudo(nid)
            originales[nid] = list(memoria[nid][0].get("pasos_accionables") or [])
            fuentes_originales[nid] = memoria[nid][0].get("fuente")
        return memoria[nid]

    for c in plan["cortes"]:
        origen = c["origen"]
        print("\n" + "-" * 78)
        print("ORIGEN : %s   frontera %s" % (origen, c.get("frontera", "?")))
        if not os.path.exists(ruta(origen)):
            fallos.append("%s: no existe en el dataset" % origen)
            print("  [ROJO] no existe")
            continue
        d, cola = cargar(origen)
        pasos = originales[origen]
        idx = c["pasos_que_salen"]

        # GUARDA DE CONTEO
        if c.get("pasos_totales") is not None and len(pasos) != c["pasos_totales"]:
            fallos.append("%s: tiene %d pasos y el plan esperaba %d"
                          % (origen, len(pasos), c["pasos_totales"]))
            print("  [ROJO] pasos %d, esperados %d" % (len(pasos), c["pasos_totales"]))
            continue

        # GUARDA DE TEXTO
        malos = []
        for pos, prefijo in zip(idx, c["prefijos"]):
            if pos < 1 or pos > len(pasos):
                malos.append((pos, "FUERA DE RANGO"))
            elif not pasos[pos - 1].startswith(prefijo):
                malos.append((pos, pasos[pos - 1][:60]))
        if malos:
            fallos.append("%s: %d paso(s) no calzan con el prefijo del plan" % (origen, len(malos)))
            print("  [ROJO] pasos que no calzan: %s" % malos)
            continue

        # GUARDA DE FUENTE
        if fuentes_originales[origen] != c["fuente_esperada"]:
            fallos.append("%s: fuente inesperada" % origen)
            print("  [ROJO] fuente de hoy : %r" % fuentes_originales[origen])
            print("         fuente esperada: %r" % c["fuente_esperada"])
            continue

        salen = [pasos[i - 1] for i in idx]
        ya = removidos.setdefault(origen, set())
        if ya & set(idx):
            fallos.append("%s: dos cortes se disputan los pasos %s" % (origen, sorted(ya & set(idx))))
            print("  [ROJO] pasos disputados: %s" % sorted(ya & set(idx)))
            continue
        quedan = [p for j, p in enumerate(pasos, 1) if j not in (ya | set(idx))]
        print("  pasos totales %d, salen %d, quedan %d" % (len(pasos), len(salen), len(quedan)))
        print("  fuente: %r  ->  %r" % (d.get("fuente"), c["fuente_queda"]))
        for i, p in zip(idx, salen):
            print("    sale  %2d. %s" % (i, p[:100]))

        dest = c["destino"]

        # los pasos que viajan: verbatim, o los del destejido declarado
        if dest.get("pasos_destejidos"):
            viajan = dest["pasos_destejidos"]
            mapa = dest.get("mapa_destejido") or {}
            print("  DESTEJIDO DECLARADO: %d pasos de origen -> %d pasos de destino"
                  % (len(salen), len(viajan)))
            cubiertos = set()
            for k, v in mapa.items():
                cubiertos |= set(v)
            faltan = [i for i in idx if i not in cubiertos]
            if faltan:
                fallos.append("%s: el mapa del destejido deja fuera los pasos %s" % (origen, faltan))
                print("  [ROJO] el mapa deja fuera: %s" % faltan)
                continue
            for k, v in mapa.items():
                print("    destino %s <- origen %s" % (k, v))
        else:
            viajan = salen

        if dest["tipo"] == "nodo_propio":
            nuevo = dest["nuevo"]
            nid = nuevo["node_id"]
            print("  DESTINO: NODO PROPIO %s" % nid)
            if os.path.exists(ruta(nid)) or nid in memoria:
                fallos.append("%s: el nodo propio %s YA EXISTE" % (origen, nid))
                print("  [ROJO] ya existe %s" % nid)
                continue
            titulo = (nuevo.get("titulo_concepto") or "").strip()
            if titulo in titulos:
                fallos.append("%s: titulo repetido exacto con %s" % (nid, titulos[titulo]))
                print("  [ROJO] titulo repetido: %s" % titulos[titulo])
                continue
            titulos.setdefault(titulo, []).append(nid)
            cuerpo = dict(nuevo)
            cuerpo["pasos_accionables"] = viajan
            faltantes = [k for k in CAMPOS_NODO if k not in cuerpo]
            if faltantes:
                fallos.append("%s: al nodo nuevo le faltan campos %s" % (nid, faltantes))
                print("  [ROJO] faltan campos: %s" % faltantes)
                continue
            cuerpo = {k: cuerpo[k] for k in CAMPOS_NODO}
            memoria[nid] = (cuerpo, "\n")
            nuevos.append(nid)
            # la arista que la creacion de un nodo obliga: origen -> nuevo
            d.setdefault("nodos_siguientes", [])
            if nid not in d["nodos_siguientes"]:
                d["nodos_siguientes"] = list(d["nodos_siguientes"]) + [nid]
            print("  arista obligada: %s.nodos_siguientes += %s" % (origen, nid))
            print("  arista reciproca: %s.nodos_previos = %s" % (nid, cuerpo["nodos_previos"]))

        elif dest["tipo"] == "miembro":
            mid = dest["nodo"]
            print("  DESTINO: MIEMBRO %s" % mid)
            # AMPLIACION DECLARADA (14 ago 2026, vuelta 29): el destino vale si
            # existe en disco O si este MISMO plan acaba de crearlo como nodo
            # propio en un corte anterior. Sin esto, la adjudicacion 3 del acta
            # de la vuelta 27 (DOS BLOQUES QUE CAEN EN EL MISMO NODO PROPIO SE
            # FUNDEN EN UNO, nunca dos gemelos) no se puede ejecutar: el segundo
            # corte chocaba con la guarda de "ya existe" del nodo propio, y la
            # unica salida habria sido fabricar el par que la campana existe
            # para deshacer. No ablanda ninguna guarda: si mid no esta ni en
            # disco ni en memoria, sigue siendo rojo.
            if not os.path.exists(ruta(mid)) and mid not in memoria:
                fallos.append("%s: el miembro destino %s no existe" % (origen, mid))
                print("  [ROJO] no existe %s" % mid)
                continue
            if mid in nuevos:
                print("  (destino creado por este mismo plan, corte anterior)")
            m, mcola = cargar(mid)
            if dest.get("fuente_esperada_destino") is not None \
                    and m.get("fuente") != dest["fuente_esperada_destino"]:
                fallos.append("%s: fuente inesperada en el destino %s" % (origen, mid))
                print("  [ROJO] fuente destino: %r" % m.get("fuente"))
                continue
            antes = len(m.get("pasos_accionables") or [])
            m["pasos_accionables"] = list(m.get("pasos_accionables") or []) + viajan
            print("  %s: pasos %d -> %d" % (mid, antes, len(m["pasos_accionables"])))
            memoria[mid] = (m, mcola)
        else:
            fallos.append("%s: tipo de destino desconocido %r" % (origen, dest["tipo"]))
            continue

        ya |= set(idx)
        d["pasos_accionables"] = quedan
        d["fuente"] = c["fuente_queda"]
        memoria[origen] = (d, cola)
        escrituras.append(origen)

    print("\n" + "=" * 78)
    print("RESUMEN")
    print("  cortes aplicados en memoria: %d" % len(escrituras))
    print("  nodos propios nuevos       : %d %s" % (len(nuevos), nuevos))
    print("  ficheros que se tocarian   : %d" % len(memoria))
    if fallos:
        print("\nPARADA: %d guarda(s) en rojo. NO se escribe nada." % len(fallos))
        for f in fallos:
            print("  - %s" % f)
        return 1

    if modo == "--simular":
        print("\nSIMULACION: cero escrituras.")
        return 0

    for nid, (datos, cola) in memoria.items():
        escribir(nid, datos, cola)
    print("\nESCRITO: %d fichero(s) en dataset/nodos/." % len(memoria))
    for nid in sorted(memoria):
        print("  - %s%s" % (nid, "  [NUEVO]" if nid in nuevos else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
