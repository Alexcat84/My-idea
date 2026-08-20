# -*- coding: utf-8 -*-
"""tallar_cabecera_reporte.py . TALLA LA TABLA DE COMPROBACIONES DE LA CABECERA
DEL REPORTE (apertura y cierre), CON CADA CELDA LEIDA DE LA SALIDA QUE LA CITA.

NOMBRE ESTABLE A PROPOSITO: no lleva numero de vuelta. La vuelta se pasa con
--vuelta y el prefijo de las salidas se arma solo (SALIDA_V<N>_...), asi que
este fichero NO se clona cada vuelta. Sucesor declarado de
scripts/loop/vuelta56_registro_tramo.py, cuya maquina se copia entera: LAS
CIFRAS SE EXTRAEN POR EXPRESION REGULAR de las salidas del dia y el tallador
CAE EN ROJO, sin escribir nada, si alguna celda no se puede leer.

POR QUE NACE (decision del fundador, 20 ago 2026, opcion b): las TRES caidas de
la racha de reporte de las vueltas 54, 55 y 56 fueron frases TECLEADAS en la
cabecera, ninguna salio de un tallador. La de la vuelta 56 es el ejemplar
exacto: la celda de las cuatro comprobaciones al CIERRE publicaba "623 igual a
623", que es la cifra de la APERTURA heredada; el instrumento del cierre dice
529. El registro del tramo ya se tallaba desde la vuelta 55; la cabecera del
reporte no, y ahi es donde caian.

LA DIFERENCIA CON EL TALLADOR DEL REGISTRO, y es la que motiva este fichero:
aquel talla UNA tabla de cierre para docs/plan/03_FUSIONES.md; este talla LAS
DOS COLUMNAS de la cabecera del reporte, apertura y cierre POR SEPARADO, cada
una con SUS CUATRO COMPROBACIONES medidas de SU PROPIA salida de recomputo. Un
lado no puede heredar del otro porque cada lado se lee de su fichero.

USO:
  python scripts/loop/tallar_cabecera_reporte.py --vuelta 56
  python scripts/loop/tallar_cabecera_reporte.py --vuelta 56 --comparar docs/loop/REPORTE.md
  python scripts/loop/tallar_cabecera_reporte.py --vuelta 56 --sin-miles

--comparar RUTA extrae la tabla de cabecera que ese fichero YA tiene y la coteja
fila a fila contra la tallada, nombrando cada celda que difiera. Es el modo con
el que se prueba que la celda mala de una vuelta vieja sale distinta del
tallador, y que una cabecera ya tallada sale identica a si misma.

FORMATO: los millares se escriben con punto (3.388), que es el estilo que la
cabecera del reporte ya usa. Con --sin-miles salen crudos como el instrumento
los imprime. Es lo unico que este tallador decide sobre la forma; el resto es
copia literal de lo medido.

SALIDA: exit 0 si talla (y si, con --comparar, no hay diferencias); exit 1 si
alguna celda no se pudo leer o si la comparacion encuentra diferencias.
"""
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")


def leer(nombre, fallos):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        fallos.append("no existe la salida %s" % nombre)
        return ""
    return io.open(ruta, encoding="utf-8").read()


def busca(texto, patron, etiqueta, fallos):
    if not texto:
        fallos.append("sin texto para %s" % etiqueta)
        return "?"
    m = re.search(patron, texto)
    if not m:
        fallos.append("no se pudo leer %s" % etiqueta)
        return "?"
    return m.group(1)


def miles(valor, con_miles):
    if not con_miles or not valor.isdigit():
        return valor
    return "{:,}".format(int(valor)).replace(",", ".")


def lado(vuelta, sufijo, fallos):
    """Lee TODAS las cifras de un lado (APERTURA o CIERRE) de sus propias salidas."""
    p = "SALIDA_V%d_" % vuelta
    d = {}

    est = leer(p + ("APERTURA.txt" if sufijo == "APERTURA" else "CIERRE.txt"), fallos)
    d["ficheros"] = busca(est, r"ficheros\s+: (\d+)", "ficheros %s" % sufijo, fallos)
    d["vivos"] = busca(est, r"vivos\s+: (\d+)", "vivos %s" % sufijo, fallos)
    d["deprecados"] = busca(est, r"deprecados\s+: (\d+)", "deprecados %s" % sufijo, fallos)
    d["enlaces"] = busca(est, r"enlaces\s+: (\d+)", "enlaces %s" % sufijo, fallos)
    d["operaciones"] = busca(est, r"operaciones: (\d+), ids unicos", "operaciones %s" % sufijo, fallos)
    d["estados"] = busca(est, r"estados: \{'([A-Z]+)': \d+\}", "estados %s" % sufijo, fallos)
    d["rotas"] = busca(est, r"dependencias rotas: (\d+)", "dependencias rotas %s" % sufijo, fallos)
    d["inventario"] = busca(est, r"entradas: (\d+)", "inventario %s" % sufijo, fallos)

    mar = leer(p + "MARCADOR_" + sufijo + ".txt", fallos)
    d["A"] = busca(mar, r"\n  A\s+(\d+)", "A %s" % sufijo, fallos)
    d["B"] = busca(mar, r"\n  B\s+(\d+)", "B %s" % sufijo, fallos)
    d["C"] = busca(mar, r"\n  C\s+(\d+)", "C %s" % sufijo, fallos)
    d["D"] = busca(mar, r"\n  D\s+(\d+)", "D %s" % sufijo, fallos)
    # n, huecos y duplicados salen del fichero de ESTADO y no del de marcador:
    # aquel los da ya contados (huecos: 0), y el de marcador imprime la LISTA
    # de huecos (huecos: []), que no es la cifra que la cabecera publica.
    d["n"] = busca(est, r"n = (\d+)", "n %s" % sufijo, fallos)
    d["huecos"] = busca(est, r"\nhuecos: (\d+)", "huecos %s" % sufijo, fallos)
    d["duplicados"] = busca(est, r"\nduplicados: (\d+)", "duplicados %s" % sufijo, fallos)

    rec = leer(p + "RECOMPUTO_" + sufijo + ".txt", fallos)
    d["crudas"] = busca(rec, r"clase == 'A'\): (\d+)", "A crudas %s" % sufijo, fallos)
    d["colapsos"] = busca(rec, r"los dos lados\): (\d+)", "colapsos %s" % sufijo, fallos)
    d["pares"] = busca(rec, r"deduplicar\): (\d+)", "pares distintos %s" % sufijo, fallos)
    d["componentes"] = busca(rec, r"componentes totales: (\d+)", "componentes %s" % sufijo, fallos)
    d["cerrados"] = busca(rec, r"CERRADOS: (\d+) sobre", "CERRADOS %s" % sufijo, fallos)
    d["cerrados_n"] = busca(rec, r"CERRADOS: \d+ sobre (\d+) nodos", "nodos CERRADOS %s" % sufijo, fallos)
    d["abiertos"] = busca(rec, r"ABIERTOS: (\d+) sobre", "ABIERTOS %s" % sufijo, fallos)
    d["abiertos_n"] = busca(rec, r"ABIERTOS: \d+ sobre (\d+) nodos", "nodos ABIERTOS %s" % sufijo, fallos)

    # LAS CUATRO COMPROBACIONES, cada lado de SU PROPIA salida. Es la celda que
    # la vuelta 56 heredo del otro lado, y por eso se lee aqui pieza por pieza.
    d["c1_izq"] = busca(rec, r"i\. nodos en actos \((\d+)\)", "comprobacion i izquierda %s" % sufijo, fallos)
    d["c1_der"] = busca(rec, r"i\. nodos en actos \(\d+\) == suma de tamanos de las componentes \((\d+)\)",
                        "comprobacion i derecha %s" % sufijo, fallos)
    d["c2_izq"] = busca(rec, r"ii\. A vigentes resueltas del retrato \((\d+)\)",
                        "comprobacion ii izquierda %s" % sufijo, fallos)
    d["c2_der"] = busca(rec, r"ii\. A vigentes resueltas del retrato \(\d+\) == suma de aristas A internas de las componentes \((\d+)\)",
                        "comprobacion ii derecha %s" % sufijo, fallos)
    d["cuatro"] = "TODAS OK" if "LAS CUATRO: TODAS OK" in rec else "NO TODAS OK"

    d["cola"] = busca(leer(p + "COLA_" + sufijo + ".txt", fallos),
                      r"nodos en la cola: (\d+)", "cola %s" % sufijo, fallos)

    col = leer(p + "COLISIONES_" + sufijo + ".txt", fallos)
    d["colisiones"] = busca(col, r"COLISIONES DE CLASE VIGENTES\s+: (\d+)", "colisiones %s" % sufijo, fallos)
    d["autopares"] = busca(col, r"AUTO-PARES \(los dos lados al mismo vivo\): (\d+)",
                           "auto-pares %s" % sufijo, fallos)

    dup = leer(p + "DUPLICADAS_" + sufijo + ".txt", fallos)
    d["dup_grupos"] = busca(dup, r"grupos afectados \(nodo mas campo mas destino\) \| (\d+)",
                            "grupos de duplicadas %s" % sufijo, fallos)
    d["dup_nodos"] = busca(dup, r"nodos con al menos una duplicada\*\* \| \*\*(\d+)",
                           "nodos con duplicadas %s" % sufijo, fallos)
    return d


def filas(ap, ci, con_miles):
    """Las filas de la tabla, cada una con su etiqueta, su celda de apertura y
    su celda de cierre. La etiqueta es la clave de comparacion."""
    m = lambda v: miles(v, con_miles)
    f = []
    f.append(("marcador `A` / `B` / `C` / `D`",
              "%s / %s / %s / %s" % (m(ap["A"]), m(ap["B"]), m(ap["C"]), m(ap["D"])),
              "%s / %s / %s / %s" % (m(ci["A"]), m(ci["B"]), m(ci["C"]), m(ci["D"]))))
    f.append(("`n`, huecos, duplicados",
              "%s / %s / %s" % (m(ap["n"]), ap["huecos"], ap["duplicados"]),
              "%s / %s / %s" % (m(ci["n"]), ci["huecos"], ci["duplicados"])))
    f.append(("grafo: ficheros / vivos / deprecados / enlaces",
              "%s / %s / %s / %s" % (m(ap["ficheros"]), m(ap["vivos"]), m(ap["deprecados"]), m(ap["enlaces"])),
              "%s / %s / %s / %s" % (m(ci["ficheros"]), m(ci["vivos"]), m(ci["deprecados"]), m(ci["enlaces"]))))
    f.append(("retrato: `A` crudas / colapsos / pares distintos",
              "%s / %s / %s" % (m(ap["crudas"]), m(ap["colapsos"]), m(ap["pares"])),
              "%s / %s / %s" % (m(ci["crudas"]), m(ci["colapsos"]), m(ci["pares"]))))
    f.append(("actos (componentes)", m(ap["componentes"]), m(ci["componentes"])))
    f.append(("actos `CERRADOS` / `ABIERTOS`",
              "%s / %s" % (m(ap["cerrados"]), m(ap["abiertos"])),
              "%s / %s" % (m(ci["cerrados"]), m(ci["abiertos"]))))
    f.append(("nodos en `CERRADOS` / `ABIERTOS`",
              "%s / %s" % (m(ap["cerrados_n"]), m(ap["abiertos_n"])),
              "%s / %s" % (m(ci["cerrados_n"]), m(ci["abiertos_n"]))))
    f.append(("cola de costuras", m(ap["cola"]), m(ci["cola"])))
    f.append(("colisiones de clase vigentes", m(ap["colisiones"]), m(ci["colisiones"])))
    f.append(("auto-pares (los dos lados al mismo vivo)", m(ap["autopares"]), m(ci["autopares"])))
    f.append(("duplicadas historicas: grupos / nodos",
              "%s / %s" % (m(ap["dup_grupos"]), m(ap["dup_nodos"])),
              "%s / %s" % (m(ci["dup_grupos"]), m(ci["dup_nodos"]))))
    f.append(("operaciones, estados, dependencias rotas",
              "%s, todas `%s`, %s" % (m(ap["operaciones"]), ap["estados"], ap["rotas"]),
              "%s, todas `%s`, %s" % (m(ci["operaciones"]), ci["estados"], ci["rotas"])))
    f.append(("entradas del inventario", m(ap["inventario"]), m(ci["inventario"])))
    # LA CELDA QUE LA RACHA PAGO: cada lado con SUS PROPIAS cifras.
    f.append(("las cuatro comprobaciones de `08_VERIFICACION`",
              "%s (%s igual a %s; %s igual a %s)" % (ap["cuatro"], m(ap["c1_izq"]), m(ap["c1_der"]),
                                                    m(ap["c2_izq"]), m(ap["c2_der"])),
              "%s (%s igual a %s; %s igual a %s)" % (ci["cuatro"], m(ci["c1_izq"]), m(ci["c1_der"]),
                                                    m(ci["c2_izq"]), m(ci["c2_der"]))))
    return f


RE_FILA = re.compile(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")


def limpiar(celda):
    """Quita el resaltado de la celda para comparar contenido y no maquillaje."""
    return re.sub(r"\s+", " ", celda.replace("**", "")).strip()


def tabla_del_fichero(ruta):
    """Extrae las filas de la primera tabla de cabecera que el fichero tenga."""
    texto = io.open(ruta, encoding="utf-8").read()
    filas_halladas = {}
    for linea in texto.splitlines():
        if not linea.strip().startswith("|"):
            continue
        m = RE_FILA.match(linea.strip())
        if not m:
            continue
        etiqueta = limpiar(m.group(1))
        if not etiqueta or set(etiqueta) <= set("-: "):
            continue
        if etiqueta not in filas_halladas:
            filas_halladas[etiqueta] = (limpiar(m.group(2)), limpiar(m.group(3)))
    return filas_halladas


def main():
    ap_arg = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    ap_arg.add_argument("--vuelta", type=int, required=True)
    ap_arg.add_argument("--sin-miles", action="store_true")
    ap_arg.add_argument("--comparar", default=None,
                        help="fichero cuya tabla de cabecera se coteja contra la tallada")
    a = ap_arg.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    con_miles = not a.sin_miles

    print("=" * 78)
    print("LA CABECERA DEL REPORTE, TALLADA. Vuelta %d." % a.vuelta)
    print("Cada celda sale de la salida que la cita; ninguna esta tecleada.")
    print("=" * 78)
    print()

    fallos = []
    apertura = lado(a.vuelta, "APERTURA", fallos)
    cierre = lado(a.vuelta, "CIERRE", fallos)

    if fallos:
        print("  ROJO, %d celdas no se pudieron leer y NO se talla nada:" % len(fallos))
        for f in fallos:
            print("     %s" % f)
        return 1

    f = filas(apertura, cierre, con_miles)

    print("--- LA TABLA, PARA PEGAR ENTERA EN LA CABECERA DEL REPORTE ---")
    print()
    print("| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |")
    print("|---|---:|---:|")
    for etiqueta, celda_ap, celda_ci in f:
        print("| %s | %s | **%s** |" % (etiqueta, celda_ap, celda_ci))
    print()

    print("--- LAS CUATRO COMPROBACIONES, CADA LADO DE SU PROPIA SALIDA ---")
    print()
    print("  APERTURA (SALIDA_V%d_RECOMPUTO_APERTURA.txt):" % a.vuelta)
    print("    i.  nodos en actos %s == componentes %s" % (apertura["c1_izq"], apertura["c1_der"]))
    print("    ii. A vigentes %s == aristas A internas %s" % (apertura["c2_izq"], apertura["c2_der"]))
    print("    veredicto: %s" % apertura["cuatro"])
    print("  CIERRE   (SALIDA_V%d_RECOMPUTO_CIERRE.txt):" % a.vuelta)
    print("    i.  nodos en actos %s == componentes %s" % (cierre["c1_izq"], cierre["c1_der"]))
    print("    ii. A vigentes %s == aristas A internas %s" % (cierre["c2_izq"], cierre["c2_der"]))
    print("    veredicto: %s" % cierre["cuatro"])
    if apertura["c1_izq"] == cierre["c1_izq"] and apertura["c2_izq"] == cierre["c2_izq"]:
        print("  AVISO: los dos lados dan la MISMA cifra. Puede ser cierto (vuelta que no")
        print("  movio el retrato), pero es la forma que la caida de la vuelta 56 tenia.")
    print()

    if not a.comparar:
        print("FIN")
        return 0

    print("--- COMPARACION CONTRA %s ---" % a.comparar)
    print()
    ruta = a.comparar if os.path.isabs(a.comparar) else os.path.join(RAIZ, a.comparar)
    if not os.path.exists(ruta):
        print("  ROJO: no existe %s" % ruta)
        return 1
    existentes = tabla_del_fichero(ruta)
    diferencias = 0
    ausentes = 0
    for etiqueta, celda_ap, celda_ci in f:
        clave = limpiar(etiqueta)
        if clave not in existentes:
            print("  AUSENTE  | %s | la fila no esta en el fichero" % etiqueta)
            ausentes += 1
            continue
        vieja_ap, vieja_ci = existentes[clave]
        for nombre, vieja, tallada in (("apertura", vieja_ap, limpiar(celda_ap)),
                                       ("cierre", vieja_ci, limpiar(celda_ci))):
            if vieja != tallada:
                diferencias += 1
                print("  DISTINTA | %s | %s" % (etiqueta, nombre))
                print("             fichero : %s" % vieja)
                print("             tallador: %s" % tallada)
    print()
    print("  filas cotejadas: %d | DISTINTAS: %d | ausentes: %d"
          % (len(f), diferencias, ausentes))
    if diferencias or ausentes:
        print("  CABECERA: NO CALZA CON EL TALLADOR")
        return 1
    print("  CABECERA: IDENTICA AL TALLADOR")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
