"""Vuelta 28: LA MUDANZA. Saca un bloque YA REPARTIDO del miembro que lo recibio
y lo lleva a su destino nuevo, sea otro miembro o un nodo propio.

Es el recomputo que manda el acta de la vuelta 27 cuando una relectura conjunta
voltea un destino: el reparto se deshace o se muda de miembro, sin borrar el texto
de la lectura anterior. Este script NO decide: aplica un plan declarativo escrito
por lectura (P.18).

Guardas, todas antes de escribir nada:
  * SIMULACION SOBRE COPIA EN MEMORIA por defecto.
  * GUARDA DE CONTEO: el nodo de partida tiene los pasos que el plan espera.
  * GUARDA DE TEXTO: cada paso que sale calza con el prefijo escrito en el plan.
  * GUARDA DE FUENTE: la fuente de hoy del nodo de partida y la del destino son
    exactamente las esperadas.
  * GUARDA DE PROCEDENCIA: el nodo del que el bloque salio originalmente existe.
  * GUARDA DE DESTINO: un nodo propio nuevo no puede existir ya, y su titulo no
    puede estar repetido exacto en el grafo.
  * CERO PERDIDA: los pasos que viajan son VERBATIM los que salen, y la suma de
    los que se quedan mas los que viajan cubre los pasos de partida.
  * EL FINAL DE FICHERO SE PRESERVA TAL CUAL (leccion de la vuelta 26).

Uso:
    python scripts/loop/vuelta28_mudanza.py <plan.json> --simular
    python scripts/loop/vuelta28_mudanza.py <plan.json> --ejecutar
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

CAMPOS_NODO = [
    "node_id", "fase_proyecto", "dominio", "titulo_concepto", "fuente",
    "resumen_teorico", "pasos_accionables", "entregable_esperado",
    "nodos_previos", "nodos_siguientes", "condiciones_activacion",
    "etiqueta_arbol",
]


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
    print("PLAN     : %s" % plan_path)
    print("OPERACION: %s" % plan["operacion"])
    print("MOTIVO   : %s" % plan.get("motivo", ""))
    print("MODO     : %s" % modo)
    print("MUDANZAS : %d" % len(plan["mudanzas"]))
    print("=" * 78)

    fallos = []
    nuevos = []
    memoria = {}
    originales = {}

    def cargar(nid):
        if nid not in memoria:
            memoria[nid] = leer_crudo(nid)
            originales[nid] = list(memoria[nid][0].get("pasos_accionables") or [])
        return memoria[nid]

    for m in plan["mudanzas"]:
        desde = m["desde"]
        print("\n" + "-" * 78)
        print("DESDE    : %s   pasos que salen %s" % (desde, m["pasos_que_salen"]))
        print("PROCEDENC: %s" % m["procedencia"])
        if not os.path.exists(ruta(desde)):
            fallos.append("%s: no existe en el dataset" % desde)
            print("  [ROJO] no existe %s" % desde)
            continue
        d, cola = cargar(desde)
        pasos = originales[desde]
        idx = m["pasos_que_salen"]

        if len(pasos) != m["pasos_totales"]:
            fallos.append("%s: tiene %d pasos y el plan esperaba %d"
                          % (desde, len(pasos), m["pasos_totales"]))
            print("  [ROJO] pasos %d, esperados %d" % (len(pasos), m["pasos_totales"]))
            continue

        malos = []
        for pos, prefijo in zip(idx, m["prefijos"]):
            if pos < 1 or pos > len(pasos):
                malos.append((pos, "FUERA DE RANGO"))
            elif not pasos[pos - 1].startswith(prefijo):
                malos.append((pos, pasos[pos - 1][:60]))
        if malos:
            fallos.append("%s: %d paso(s) no calzan con el prefijo del plan" % (desde, len(malos)))
            print("  [ROJO] pasos que no calzan: %s" % malos)
            continue

        if d.get("fuente") != m["fuente_esperada_desde"]:
            fallos.append("%s: fuente inesperada" % desde)
            print("  [ROJO] fuente de hoy : %r" % d.get("fuente"))
            print("         fuente esperada: %r" % m["fuente_esperada_desde"])
            continue

        if not os.path.exists(ruta(m["procedencia"])):
            fallos.append("%s: la procedencia %s no existe" % (desde, m["procedencia"]))
            print("  [ROJO] no existe la procedencia %s" % m["procedencia"])
            continue

        viajan = [pasos[i - 1] for i in idx]
        quedan = [p for j, p in enumerate(pasos, 1) if j not in set(idx)]
        if len(quedan) + len(viajan) != len(pasos):
            fallos.append("%s: cero perdida no se cumple" % desde)
            print("  [ROJO] cero perdida no se cumple")
            continue
        print("  pasos totales %d, salen %d, quedan %d" % (len(pasos), len(viajan), len(quedan)))
        for i, p in zip(idx, viajan):
            print("    sale  %2d. %s" % (i, p[:100]))

        dest = m["destino"]
        if dest["tipo"] == "nodo_propio":
            nuevo = dest["nuevo"]
            nid = nuevo["node_id"]
            print("  DESTINO: NODO PROPIO %s" % nid)
            if os.path.exists(ruta(nid)) or nid in memoria:
                fallos.append("%s: el nodo propio %s YA EXISTE" % (desde, nid))
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
            if m["procedencia"] not in (cuerpo.get("nodos_previos") or []):
                fallos.append("%s: el nodo nuevo no cita su procedencia en nodos_previos" % nid)
                print("  [ROJO] nodos_previos sin la procedencia")
                continue
            cuerpo = {k: cuerpo[k] for k in CAMPOS_NODO}
            memoria[nid] = (cuerpo, "\n")
            nuevos.append(nid)
            # la arista que la creacion de un nodo obliga: procedencia -> nuevo
            pd, pcola = cargar(m["procedencia"])
            pd.setdefault("nodos_siguientes", [])
            if nid not in pd["nodos_siguientes"]:
                pd["nodos_siguientes"] = list(pd["nodos_siguientes"]) + [nid]
            memoria[m["procedencia"]] = (pd, pcola)
            print("  arista obligada : %s.nodos_siguientes += %s" % (m["procedencia"], nid))
            print("  arista reciproca: %s.nodos_previos = %s" % (nid, cuerpo["nodos_previos"]))

        elif dest["tipo"] == "miembro":
            mid = dest["nodo"]
            print("  DESTINO: MIEMBRO %s" % mid)
            if not os.path.exists(ruta(mid)):
                fallos.append("%s: el miembro destino %s no existe" % (desde, mid))
                print("  [ROJO] no existe %s" % mid)
                continue
            md, mcola = cargar(mid)
            if dest.get("fuente_esperada_destino") is not None \
                    and md.get("fuente") != dest["fuente_esperada_destino"]:
                fallos.append("%s: fuente inesperada en el destino %s" % (desde, mid))
                print("  [ROJO] fuente destino: %r" % md.get("fuente"))
                continue
            antes = len(md.get("pasos_accionables") or [])
            md["pasos_accionables"] = list(md.get("pasos_accionables") or []) + viajan
            print("  %s: pasos %d -> %d" % (mid, antes, len(md["pasos_accionables"])))
            memoria[mid] = (md, mcola)
        else:
            fallos.append("%s: tipo de destino desconocido %r" % (desde, dest["tipo"]))
            continue

        d["pasos_accionables"] = quedan
        memoria[desde] = (d, cola)

    print("\n" + "=" * 78)
    print("RESUMEN")
    print("  nodos propios nuevos    : %d %s" % (len(nuevos), nuevos))
    print("  ficheros que se tocarian: %d" % len(memoria))
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
    if nuevos:
        print("\nRECORDATORIO: cada nodo nuevo va a docs/plan/INDICE_ROJO_DECLARADO.jsonl")
        print("  python scripts/loop/vuelta28_declarar.py <OPERACION> <fecha> %s"
              % " ".join(nuevos))
    return 0


if __name__ == "__main__":
    sys.exit(main())
