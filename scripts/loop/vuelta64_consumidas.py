# -*- coding: utf-8 -*-
"""vuelta64_consumidas.py . MIDE POR CAMINO PROPIO LAS CINCO FUSIONES DE MESA
QUE EL ACTA 63 DECLARA CONSUMIDAS, Y BUSCA EN docs/plan/03_FUSIONES.md EL
REGISTRO DEL TRAMO QUE CONSUMIO CADA UNA.

SOLO LECTURA. No escribe ni un nodo ni una ficha: imprime lo medido para que la
correccion declarada de la TAREA 1.c se escriba CON LA LINEA AL LADO (regla 1).

NO REUSA el script del auditor (docs/loop/_auditor_v63_mesas.py): el camino es
propio a proposito, para que la coincidencia sea contraste y no copia (regla 2).

LA MEDICION VIVE EN medir() Y NO EN main(), y esto no es estetica: el escritor
de las correcciones (scripts/loop/vuelta64_correcciones_consumidas.py) IMPORTA
esta misma funcion en vez de reteclear la busqueda, para que el que mide y el
que escribe no puedan discrepar en silencio. Es la vara que el generador de
planes de mesa ya usa con el de lotes.

Lo que se mide:

  1. el par de cada ficha resuelto por la cadena de alias (P.1) contra el grafo
     de HOY, con el superviviente REAL (el vivo al que resuelve el par) al lado
     del superviviente que la FICHA escribe;
  2. si los dos coinciden o DIVERGEN, que es lo que MEDIOS y ADMIT tienen que
     declarar como contraste;
  3. el sitio del registro: la linea de docs/plan/03_FUSIONES.md que nombra a
     los DOS miembros, su SEDE (la cabecera de nivel 2 que manda sobre ella, la
     que trae tramo y vuelta) y sus celdas de acto, lote, sobrevive y absorbe
     LEIDAS POR EL NOMBRE DE SU COLUMNA en la cabecera de la tabla, nunca de la
     prosa de alrededor.

Uso: python scripts/loop/vuelta64_consumidas.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
REG = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")

CONSUMIDAS = ["OP-M-02-MEDIOS", "OP-M-02-ASSESS", "OP-M-02-ADMIT",
              "OP-M-02-ACTIVATE", "OP-M-02-ACCOMPLISH"]
SIN_COLUMNA = "NO HAY COLUMNA %s EN ESTA TABLA"
# La cabecera bajo la que vive el REGISTRO DE LA FUSION de un tramo.
SEDE_FUSION = chr(96) + "OP-U-01" + chr(96) + ", TRAMO"


def medir():
    """Devuelve (filas, fallos, contexto). Cada fila es un dict con lo medido."""
    nodos = {}
    for f in os.listdir(NODOS):
        if f.endswith(".json"):
            j = json.load(io.open(os.path.join(NODOS, f), encoding="utf-8"))
            nodos[j.get("node_id") or f[:-5]] = j
    alias = {}
    for nid, j in nodos.items():
        for a in (j.get("ids_alias") or []):
            alias.setdefault(a, nid)

    def vivo(n):
        j = nodos.get(n)
        return bool(j) and not (j.get("deprecado") or j.get("deprecated")
                                or j.get("estado") == "deprecado")

    def resolver(n):
        visto = set()
        while n in alias and n not in visto:
            visto.add(n)
            n = alias[n]
        return n

    fichas = {}
    for l in io.open(OPS, encoding="utf-8"):
        if l.strip():
            j = json.loads(l)
            fichas[j["id_op"]] = j

    lineas = io.open(REG, encoding="utf-8").read().split(chr(10))
    contexto = {"nodos": len(nodos), "alias": len(alias), "lineas": len(lineas)}
    filas, fallos = [], []

    for id_op in CONSUMIDAS:
        f = fichas.get(id_op)
        if f is None:
            fallos.append("%s no esta en OPERACIONES.jsonl" % id_op)
            continue
        miembros = list(f.get("nodos") or [])
        estados = []
        for m in miembros:
            if m not in nodos:
                estados.append("%s:NO EXISTE" % m)
            elif vivo(m):
                estados.append("%s:VIVO" % m)
            else:
                estados.append("%s:DEPRECADO->%s" % (m, resolver(m)))
        resueltos = sorted({resolver(m) for m in miembros if m in nodos})
        if len(resueltos) != 1:
            fallos.append("%s NO resuelve a un solo vivo: %s" % (id_op, resueltos))
            continue
        sup_real = resueltos[0]
        if not vivo(sup_real):
            fallos.append("%s resuelve a %s, que NO esta vivo" % (id_op, sup_real))
        sup_ficha = f.get("superviviente")
        muerto = [m for m in miembros if m != sup_real]

        # EL ID SE BUSCA ENTRE COMILLAS INVERSAS, NO COMO SUBCADENA SUELTA.
        # El motivo esta medido: fase_activate es subcadena de
        # fase_activate_primera_impresion y de seis_herramientas_comunicacion_
        # fase_activate, y la busqueda cruda daba por bueno un sitio (la linea
        # 2112) que no es de este par. Fallar ruidoso antes que acertar por
        # casualidad.
        def cita(m):
            return chr(96) + m + chr(96)
        crudos = []
        for i, ln in enumerate(lineas, 1):
            if all(cita(m) in ln for m in miembros):
                sede_i, sede_t = 0, "?"
                for j in range(i, 0, -1):
                    if lineas[j - 1].startswith("## "):
                        sede_i, sede_t = j, lineas[j - 1].strip()
                        break
                crudos.append((i, ln, sede_i, sede_t))
        # EL SITIO QUE VALE ES EL REGISTRO DE LA FUSION, o sea el que vive bajo
        # una cabecera de TRAMO DE OP-U-01. Los demas se DECLARAN en vez de
        # descartarse en silencio, y hay uno seguro desde la vuelta 64: la propia
        # tabla de esta seccion, que nombra los dos miembros de cada par. Un
        # instrumento que se cuenta a si mismo como fuente es la averia que este
        # filtro evita, y por eso el filtro se nombra en vez de esconderse.
        hits = [(i, ln) for i, ln, _si, st in crudos if SEDE_FUSION in st]
        otros = [(i, st) for i, _ln, _si, st in crudos if SEDE_FUSION not in st]
        if len(hits) != 1:
            fallos.append("%s: %d lineas bajo una cabecera de tramo de OP-U-01 nombran "
                          "a los dos miembros, y la correccion necesita UNA" % (id_op, len(hits)))
        sitios = []
        for i, ln in hits:
            sede_i, sede_t = 0, "?"
            for j in range(i, 0, -1):
                if lineas[j - 1].startswith("## "):
                    sede_i, sede_t = j, lineas[j - 1].strip()
                    break
            cab_i, cab_t = 0, ""
            for j in range(i, 0, -1):
                t = lineas[j - 1]
                if t.startswith("|") and ("sobrevive" in t or "que muere" in t):
                    cab_i, cab_t = j, t.strip()
                    break
            cols_cab = [c.strip().strip("`*").lower()
                        for c in cab_t.strip("|").split("|")] if cab_t else []
            cols_fila = [c.strip().strip("`*") for c in ln.strip().strip("|").split("|")]

            def celda(nombre, _cc=cols_cab, _cf=cols_fila):
                for k, c in enumerate(_cc):
                    if c == nombre and k < len(_cf):
                        return _cf[k]
                return SIN_COLUMNA % nombre.upper()

            sitios.append({
                "linea": i, "texto": ln.strip(),
                "sede_linea": sede_i, "sede": sede_t,
                "cab_linea": cab_i, "cab": cab_t,
                "acto": celda("acto") if "acto" in cols_cab else celda("#"),
                "lote": celda("lote"),
                "sobrevive": celda("sobrevive"),
                "absorbe": celda("absorbe"),
            })
        solo_muerto = [i for i, ln in enumerate(lineas, 1)
                       if all(cita(m) in ln for m in muerto)
                       and not all(cita(m) in ln for m in miembros)]
        filas.append({
            "id_op": id_op, "miembros": miembros, "estados": estados,
            "sup_real": sup_real, "sup_ficha": sup_ficha, "muerto": muerto,
            "divergen": sup_real != sup_ficha, "sitios": sitios,
            "otros_sitios": otros, "solo_muerto": solo_muerto,
        })
    return filas, fallos, contexto


def tabla_markdown(filas):
    """LA TABLA SE IMPRIME, NO SE TECLEA (regla 1). El registro de la TAREA 1.a
    pega esta salida entera en vez de reteclear las celdas."""
    nl = chr(10)
    out = ["| ficha | superviviente de la **ficha** (12 ago) | el que quedo **VIVO** | "
           "coinciden | quien la consumio | linea |",
           "|---|---|---|:---:|---|---:|"]
    for f in filas:
        s = f["sitios"][0]
        sede = s["sede"]
        tramo = sede.split("**")[0].replace("## ", "").strip().rstrip(":").rstrip(",")
        vuelta = sede.split("vuelta ")[-1].rstrip(")") if "vuelta " in sede else "?"
        lote = ("" if s["lote"].startswith("NO HAY COLUMNA") else ", lote %s" % s["lote"])
        out.append("| `%s` | `%s` | `%s` | %s | %s, vuelta %s, acto %s%s | **%d** |"
                   % (f["id_op"], f["sup_ficha"], f["sup_real"],
                      "**NO**" if f["divergen"] else "si",
                      tramo, vuelta, s["acto"], lote, s["linea"]))
    return nl.join(out)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    filas, fallos, ctx = medir()
    print("=" * 78)
    print("LAS CINCO FUSIONES DE MESA CONSUMIDAS, MEDIDAS POR CAMINO PROPIO")
    print("  grafo: %d nodos leidos de dataset/nodos | alias cargados: %d"
          % (ctx["nodos"], ctx["alias"]))
    print("  registro: docs/plan/03_FUSIONES.md, %d lineas" % ctx["lineas"])
    print("=" * 78)
    for f in filas:
        print()
        print("--- %s ---" % f["id_op"])
        print("   miembros de la ficha : %s" % ", ".join(f["estados"]))
        print("   CONSUMIDA: el par resuelve a UN solo vivo, %s" % f["sup_real"])
        print("   superviviente de la FICHA (12 ago 2026): %s" % f["sup_ficha"])
        if f["divergen"]:
            print("   DIVERGEN: la ficha decia %s y el tramo dejo vivo a %s"
                  % (f["sup_ficha"], f["sup_real"]))
        else:
            print("   COINCIDEN: el tramo ejecuto el mismo superviviente que la ficha")
        print("   lineas del registro que nombran a los DOS miembros: %d" % len(f["sitios"]))
        for s in f["sitios"]:
            print("      SEDE -> linea %d: %s" % (s["sede_linea"], s["sede"][:150]))
            print("      CABECERA DE LA TABLA -> linea %d: %s" % (s["cab_linea"], s["cab"][:150]))
            print("      acto (de su columna)     : %s" % s["acto"])
            print("      lote (de su columna)     : %s" % s["lote"])
            print("      sobrevive (de su columna): %s" % s["sobrevive"])
            print("      absorbe   (de su columna): %s" % s["absorbe"])
            print("      linea %-6d | %s" % (s["linea"], s["texto"][:130]))
        print("   OTROS sitios que nombran el par y NO son registro de fusion: %d"
              % len(f["otros_sitios"]))
        for i, st in f["otros_sitios"]:
            print("      linea %-6d bajo %s" % (i, st[:110]))
        print("   lineas que nombran solo al que murio (%s): %d %s"
              % (", ".join(f["muerto"]), len(f["solo_muerto"]), f["solo_muerto"][:12]))
    print()
    print("=" * 78)
    if fallos:
        print("ROJO, %d fallo(s):" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1
    print()
    print("--- LA TABLA, PARA PEGARLA ENTERA ---")
    print(tabla_markdown(filas))
    print()
    print("VERDE: las cinco resuelven a UN solo vivo y las cinco tienen UN registro.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
