# -*- coding: utf-8 -*-
r"""contar_cierre_efectivo.py . EL REMEDIO DE LA CAIDA DE CIFRA PUBLICADA DE LA
VUELTA 99 (acta 99, seccion 4.4). Nombre estable, sin numero de vuelta, como
scripts/loop/tallar_cabecera_reporte.py.

POR QUE NACE. El cierre de OP-E-03 publicado en la vuelta 99 (95/88, 48,1%)
contaba el campo `direccion_leida` CRUDO de las 183 filas, ignorando que la
propia vuelta 99 habia declarado `correccion_v99` sobre la fila 147 (paso de
DIRECCION AFIRMADA a NO RESUELTA). La cifra efectiva es 94/89 (48,6%). La
causa raiz, medida: scripts/loop/vuelta99_tarea3_addendum_cierre_opE03.py
linea 124 cuenta `sum(1 for f in todas if f.get("direccion_leida"))`, que lee
el campo crudo y no mira ninguna `correccion_vNN`.

QUE HACE. Cuenta CLASE y DIRECCION sobre los ficheros de tramo de una
operacion de LECTURA DIRIGIDA, y para cada fila usa el valor de
`correccion_vNN` cuando ese objeto declare `campo_corregido` igual al campo
que se esta contando (`direccion_leida` o `clase`). Si una fila trae
`correccion_vNN` con `campo_corregido` que el instrumento no sabe aplicar a
NINGUNO de los dos conteos, EL INSTRUMENTO CAE EN ROJO SIN ESCRIBIR NADA: la
leccion de la caida de la vuelta 99 no es "sumaste mal", es que una
correccion declarada podia quedarse sin efecto y nada lo gritaba.

CAMPOS DE CORRECCION RECONOCIDOS:
  - "direccion_leida": el conteo de direccion usa `valor_nuevo` en vez del
    `direccion_leida` crudo de la fila (un `valor_nuevo` null cuenta como SIN
    direccion, o sea NO RESUELTA).
  - "clase": el conteo de clase usa `valor_nuevo` en vez de `clase` crudo.
  - "vara (cita)": reconocido EXPLICITAMENTE como sin efecto en estos dos
    conteos (corrige la cita de la vara, no el veredicto ni la direccion).
  Cualquier otro valor de `campo_corregido` es DESCONOCIDO y dispara el rojo
  de la guarda.

Si una fila trae mas de una `correccion_vNN`, se aplican en orden ascendente
de NN (la mas reciente manda si dos corrigen el mismo campo).

MECANICA DE ROJO, y no imprime tabla ninguna si salta: (i) algun fichero de
--tramos no existe; (ii) alguna fila no trae la marca completa de LECTURA
DIRIGIDA; (iii) los `puesto_tramo` de todos los ficheros no cubren 1..N sin
huecos ni repetidos; (iv) alguna fila trae `correccion_vNN` con
`campo_corregido` fuera del conjunto reconocido arriba.

USO:
  python scripts/loop/contar_cierre_efectivo.py --tramos F1.jsonl F2.jsonl ...
  python scripts/loop/contar_cierre_efectivo.py   (sin --tramos: usa los
      cuatro ficheros de tramo de OP-E-03 tal como existen hoy en docs/plan/)
"""
import argparse
import collections
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TRAMOS_OP_E_03_POR_DEFECTO = [
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl"),
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl"),
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO3_V98.jsonl"),
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO4_V99.jsonl"),
]

CAMPOS_RECONOCIDOS = {"direccion_leida", "clase", "vara (cita)"}
CAMPOS_QUE_CUENTAN = {"direccion_leida", "clase"}

CORREC_RE = re.compile(r"^correccion_v(\d+)$")


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def correcciones_ordenadas(fila):
    claves = [(int(m.group(1)), k) for k in fila
              for m in [CORREC_RE.match(k)] if m]
    claves.sort()
    return [fila[k] for _, k in claves]


def valor_efectivo(fila, campo, fallos_fila):
    valor = fila.get(campo)
    for c in correcciones_ordenadas(fila):
        cc = c.get("campo_corregido")
        if cc == campo:
            valor = c.get("valor_nuevo")
        elif cc not in CAMPOS_RECONOCIDOS:
            fallos_fila.append(
                "puesto_tramo %s trae correccion con campo_corregido %r, "
                "DESCONOCIDO (ni direccion_leida, ni clase, ni 'vara (cita)')"
                % (fila.get("puesto_tramo"), cc))
    return valor


def cifras(rutas):
    fallos = []
    todas = []
    rangos = []
    for ruta in rutas:
        if not os.path.exists(ruta):
            fallos.append("no existe %s" % os.path.relpath(ruta, RAIZ))
            continue
        filas = cargar(ruta)
        for f in filas:
            if (f.get("marca") != "LECTURA DIRIGIDA" or not f.get("fuera_de_la_cola")
                    or f.get("mueve_el_marcador_del_cribado") is not False
                    or not f.get("fuera_de_la_tasa_por_dominio")):
                fallos.append("%s puesto_tramo %s no trae la marca completa de "
                              "LECTURA DIRIGIDA" % (os.path.basename(ruta), f.get("puesto_tramo")))
            # guarda de campo_corregido desconocido: recorre TODAS las
            # correcciones de la fila, aunque no toquen ni clase ni direccion
            for c in correcciones_ordenadas(f):
                cc = c.get("campo_corregido")
                if cc not in CAMPOS_RECONOCIDOS:
                    fallos.append(
                        "%s puesto_tramo %s trae correccion con campo_corregido "
                        "%r, DESCONOCIDO" % (os.path.basename(ruta), f.get("puesto_tramo"), cc))
        todas.extend(filas)
        rangos.append((os.path.basename(ruta), len(filas)))

    if fallos:
        return None, fallos

    puestos = sorted(f["puesto_tramo"] for f in todas)
    n = len(todas)
    if puestos != list(range(1, n + 1)):
        faltan = sorted(set(range(1, n + 1)) - set(puestos))
        repetidos = [p for p, c in collections.Counter(puestos).items() if c > 1]
        fallos.append("los puesto_tramo no cubren 1 a %d sin huecos ni repetidos: "
                      "faltan %s, repetidos %s" % (n, faltan, repetidos))
        return None, fallos

    d = {"n": n, "rangos": rangos}
    ignorar = []
    clases = collections.Counter()
    con_dir = 0
    sin_dir = []
    invertidas = []
    for f in todas:
        clase_ef = valor_efectivo(f, "clase", ignorar)
        clases[clase_ef] += 1
        dir_ef = valor_efectivo(f, "direccion_leida", ignorar)
        if dir_ef:
            con_dir += 1
            if dir_ef.split("->")[0].strip() == f.get("hijo_de_la_bolsa"):
                invertidas.append(f["puesto_tramo"])
        else:
            sin_dir.append(f["puesto_tramo"])

    d["clases"] = clases
    d["c"] = sorted(f["puesto_tramo"] for f in todas if valor_efectivo(f, "clase", []) == "C")
    d["con_dir"] = con_dir
    d["sin_dir"] = sorted(sin_dir)
    d["invertidas"] = sorted(invertidas)
    return d, fallos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramos", nargs="+", default=None)
    a = ap.parse_args()
    rutas = a.tramos if a.tramos else TRAMOS_OP_E_03_POR_DEFECTO

    d, fallos = cifras(rutas)
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("=" * 100)
    print("CIERRE EFECTIVO (correcciones declaradas APLICADAS)")
    print("=" * 100)
    for nombre, filas in d["rangos"]:
        print("%s n=%d" % (nombre, filas))
    pct = 100.0 * len(d["sin_dir"]) / d["n"]
    print("n=%d  clase A %d, B %d, C %d (par %s), D %d"
          % (d["n"], d["clases"]["A"], d["clases"]["B"], d["clases"]["C"],
             ", ".join(str(x) for x in d["c"]), d["clases"]["D"]))
    print("direccion: %d / %d  (%s%% NO RESUELTA)"
          % (d["con_dir"], len(d["sin_dir"]), ("%.1f" % pct).replace(".", ",")))
    print("invertidas: %d (pares %s)"
          % (len(d["invertidas"]), ", ".join(str(x) for x in d["invertidas"])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
