"""Vuelta 46: EL CIERRE DE LA FASE 02, MEDIDO Y NO SUPUESTO.

El encargo manda: las nueve operaciones de la fase con su registro, el criterio
de HECHO de 08_VERIFICACION contra cada una, Gate 0 y suites en verde, y el
estado del archivo (congelados restantes). Y remata: SI ALGO NO CIERRA, SE
DECLARA CON LA MEDICION DELANTE EN VEZ DE DECLARARLO CERRADO.

Este instrumento NO opina: cuenta. Todo sale de:
  docs/plan/OPERACIONES.jsonl          (las nueve operaciones, enteras)
  docs/plan/02_DESTEJIDOS.md           (el registro escrito de cada una)
  docs/plan/08_VERIFICACION.md         (el criterio de HECHO de la fase)
  docs/INTRA_DOMINIO_VEREDICTOS.jsonl  (los congelados que quedan)
  dataset/nodos/*.json                 (los nodos sujetos)

La marca de congelado es la MISMA del verificador de la vuelta 45
(scripts/loop/vuelta45_verificar_opd01_opd02.py, linea 53): la razon ABRE con
NO SE JUZGA, NO PUEDO JUZGAR o CONGELAD. No se estrena detector.

Uso: python scripts/loop/vuelta46_cierre_fase02.py
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
DEST = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")
VERIF = os.path.join(RAIZ, "docs", "plan", "08_VERIFICACION.md")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

MARCA = re.compile(r"^(NO SE JUZGA|NO PUEDO JUZGAR|CONGELAD)", re.I)

# El registro de cada operacion se busca en 02_DESTEJIDOS.md por su patron
# escrito: un encabezado que nombra la operacion, y la frase del cierre.
# CORRECCION DECLARADA DEL INSTRUMENTO (vuelta 46, vista antes de publicar
# nada): buscar SOLO la frase "REGISTRO DE OPERACION HECHA" daba 5 de 9 y eso
# NO era una ausencia de registro, era el detector. Esa frase se acuno en la
# vuelta 30 (OP-D-06 en adelante); OP-D-03, OP-D-04 y OP-D-05 cerraron ANTES,
# con la forma vieja, que es un encabezado "OP-D-0X CERRADA" o "SELLADA".
# Se miden LAS DOS FORMAS y se publican por separado, sin fundir una en otra.
PATRON_REGISTRO = "REGISTRO DE OPERACION HECHA"
PATRON_CERRADA = re.compile(r"^#+\s+.*OP-D-\d\d.*\s(CERRADA|SELLADA)", re.I)


def sep(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


def main():
    ops = {}
    for linea in io.open(OPS, encoding="utf-8"):
        linea = linea.strip()
        if linea:
            d = json.loads(linea)
            ops[d["id_op"]] = d

    f02 = sorted([d for d in ops.values() if d["fase"] == "02_DESTEJIDOS"],
                 key=lambda d: d["id_op"])

    texto = io.open(DEST, encoding="utf-8").read()
    lineas = texto.split("\n")

    sep("1. LAS OPERACIONES DE LA FASE 02, CONTADAS DEL FICHERO")
    print("  operaciones con fase == 02_DESTEJIDOS: %d" % len(f02))
    print()
    print("  %-10s %-6s %-8s %-6s %-6s %-8s" %
          ("op", "orden", "estado", "nodos", "verif", "arist_nue"))
    for d in f02:
        print("  %-10s %-6s %-8s %-6d %-6d %-8d" %
              (d["id_op"], d.get("orden"), d.get("estado"),
               len(d.get("nodos") or []), len(d.get("verificacion") or []),
               len(d.get("aristas_nuevas") or [])))

    sep("2. EL REGISTRO ESCRITO DE CADA UNA, BUSCADO EN 02_DESTEJIDOS.md")
    print("  patron buscado: un encabezado que nombre la operacion, y la frase")
    print("  '%s' en el cuerpo que le sigue." % PATRON_REGISTRO)
    print()
    # Localizar los encabezados que nombran cada operacion.
    marcas = []
    for i, l in enumerate(lineas):
        if l.startswith("#"):
            marcas.append((i, l))
    registros = {}
    for d in f02:
        oid = d["id_op"]
        # ultimo encabezado de nivel 2 que nombre la operacion
        cabeceras = [(i, l) for i, l in marcas
                     if l.startswith("## ") and oid in l]
        if not cabeceras:
            registros[oid] = (None, False, 0, "")
            continue
        ini = cabeceras[-1][0]
        siguientes = [i for i, l in marcas if l.startswith("## ") and i > ini]
        fin = siguientes[0] if siguientes else len(lineas)
        cuerpo_l = lineas[ini:fin]
        cuerpo = "\n".join(cuerpo_l)
        cerrada = [l for l in cuerpo_l if PATRON_CERRADA.match(l) and oid in l]
        registros[oid] = (ini + 1, PATRON_REGISTRO in cuerpo, fin - ini,
                          cerrada[0].strip() if cerrada else "")
    print("  %-10s %-11s %-10s %-8s %s" %
          ("op", "linea del", "frase de", "lineas", "encabezado CERRADA o SELLADA"))
    print("  %-10s %-11s %-10s %-8s %s" %
          ("", "encabezado", "la v30", "seccion", "(la forma anterior a la v30)"))
    for d in f02:
        oid = d["id_op"]
        ln, tiene, largo, cerr = registros[oid]
        print("  %-10s %-11s %-10s %-8s %s" %
              (oid, ln if ln else "SIN SECCION", "SI" if tiene else "NO",
               largo, cerr[:64] if cerr else "(ninguno)"))
    con_frase = [o for o in registros if registros[o][1]]
    con_cerrada = [o for o in registros if registros[o][3]]
    con_alguno = [o for o in registros if registros[o][1] or registros[o][3]]
    print()
    print("  con la frase REGISTRO DE OPERACION HECHA (forma de la v30) : %d de %d"
          % (len(con_frase), len(f02)))
    print("  con encabezado CERRADA o SELLADA (forma anterior)          : %d de %d"
          % (len(con_cerrada), len(f02)))
    print("  CON REGISTRO DE CIERRE EN ALGUNA DE LAS DOS FORMAS         : %d de %d"
          % (len(con_alguno), len(f02)))
    sin_ninguno = [d["id_op"] for d in f02
                   if not (registros[d["id_op"]][1] or registros[d["id_op"]][3])]
    print("  SIN NINGUN REGISTRO DE CIERRE: %s"
          % (", ".join(sin_ninguno) if sin_ninguno else "ninguna"))
    print()
    print("  LIMITE DECLARADO DEL LOCALIZADOR: OP-D-01 y OP-D-02 comparten UNA")
    print("  SOLA seccion (la de la vuelta 45, que las verifica juntas), asi que")
    print("  las dos apuntan a la misma linea. No son dos secciones contadas una.")

    sep("3. EL CRITERIO DE HECHO DE LA FASE 02, COPIADO DE 08_VERIFICACION.md")
    tv = io.open(VERIF, encoding="utf-8").read().split("\n")
    for i, l in enumerate(tv, 1):
        if "02 DESTEJIDOS" in l:
            print("  linea %d: %s" % (i, l.strip()))
    for i, l in enumerate(tv, 1):
        if "UNA FASE ESTA HECHA" in l:
            print("  linea %d: %s" % (i, l.strip()))

    sep("4. LOS CONGELADOS QUE QUEDAN HOY EN EL ARCHIVO")
    print("  marca: la razon ABRE con NO SE JUZGA, NO PUEDO JUZGAR o CONGELAD")
    print("  (el mismo detector de scripts/loop/vuelta45_verificar_opd01_opd02.py)")
    print()
    vers = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    congelados = [v for v in vers if MARCA.match((v.get("razon") or "").strip())]
    print("  veredictos en el archivo: %d" % len(vers))
    print("  CONGELADOS HOY          : %d" % len(congelados))
    for v in congelados:
        print("    puesto %-6d clase %-2s  %s  contra  %s"
              % (v["puesto_intra"], v["clase"], v["nodo_a"], v["nodo_b"]))
        print("      razon (primeras 220): %s" % (v["razon"] or "")[:220])

    sep("5. LOS NODOS SUJETOS DE LA FASE, Y SI SIGUEN VIVOS")
    sujetos = []
    for d in f02:
        for n in (d.get("nodos") or []):
            sujetos.append((d["id_op"], n))
    print("  parejas operacion/nodo declaradas: %d" % len(sujetos))
    vivos, muertos, ausentes = 0, 0, []
    for oid, nid in sujetos:
        ruta = os.path.join(NODOS, nid + ".json")
        if not os.path.exists(ruta):
            ausentes.append((oid, nid))
            continue
        d = json.loads(io.open(ruta, encoding="utf-8").read())
        # el campo real es "deprecado", presente en 329 ficheros y SIEMPRE True,
        # medido hoy sobre dataset/nodos. No hay campo "estado" en el nodo.
        if d.get("deprecado") is True:
            muertos += 1
        else:
            vivos += 1
    print("  nodos sujetos que existen como fichero: %d" % (len(sujetos) - len(ausentes)))
    print("  vivos %d  deprecados %d  ausentes %d" % (vivos, muertos, len(ausentes)))
    for oid, nid in ausentes:
        print("    AUSENTE: %s (declarado por %s)" % (nid, oid))

    sep("6. LO QUE ESTE INSTRUMENTO NO DECIDE")
    print("  No decide si la fase esta CERRADA. Cuenta lo que hay y lo publica.")
    print("  La adjudicacion de si OP-D-07 cuenta como HECHA cuando su cirugia la")
    print("  ejecuto OTRA fase va al reporte como DISCUTIBLE MARCADO, no aqui.")
    print("  nodos tocados por ESTA corrida: 0 (instrumento de solo lectura)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
