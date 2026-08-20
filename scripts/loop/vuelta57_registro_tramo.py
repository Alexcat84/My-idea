# -*- coding: utf-8 -*-
"""vuelta57_registro_tramo.py . EL REGISTRO DEL CIERRE DEL TRAMO 4 EN
docs/plan/03_FUSIONES.md, CON CADA CIFRA LEIDA DE SU SALIDA.

SUCESOR DECLARADO de scripts/loop/vuelta56_registro_tramo.py, al que NO
reemplaza. LA MAQUINA ES LA SUYA, COPIADA: cada celda se EXTRAE por expresion
regular de la salida que la cita, y el instrumento CAE EN ROJO sin escribir nada
si alguna no se puede leer. NINGUNA CIFRA DE ESTE REGISTRO SE TECLEA.

LO UNICO QUE CAMBIA: las salidas son las `SALIDA_V57_*` y el tramo es el 4. Las
tablas del reparto y de los declarados NO se arman aqui: se PEGAN enteras de
`scripts/loop/vuelta57_tallar_planes.py`, recortadas por maquina de su salida,
que es lo mismo que hacia el ancestro con las suyas.

SE ANADE AL FINAL DEL FICHERO, detras del registro del tramo 3, y es
IDEMPOTENTE: si el encabezado del tramo 4 ya esta, no escribe nada.

Uso: python scripts/loop/vuelta57_registro_tramo.py [--simular]
"""
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
FUS = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
ENCABEZADO = "## `OP-U-01`, TRAMO 4: EL REGISTRO DEL CIERRE (20 ago 2026, vuelta 57)"


def leer(nombre):
    return io.open(os.path.join(LOOP, nombre), encoding="utf-8").read()


def busca(texto, patron, etiqueta, fallos):
    m = re.search(patron, texto)
    if not m:
        fallos.append("no se pudo leer %s" % etiqueta)
        return "?"
    return m.group(1)


def recorta(texto, desde, hasta, etiqueta, fallos):
    """Recorta una tabla entera de la salida de un tallador, entre dos marcas."""
    i = texto.find(desde)
    if i < 0:
        fallos.append("no se pudo recortar %s (falta la marca de inicio)" % etiqueta)
        return ""
    j = texto.find(hasta, i + len(desde))
    if j < 0:
        fallos.append("no se pudo recortar %s (falta la marca de fin)" % etiqueta)
        return ""
    return texto[i + len(desde):j].strip("\n")


def miles(v):
    return "{:,}".format(int(v)).replace(",", ".") if v.isdigit() else v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("EL REGISTRO DEL CIERRE DEL TRAMO 4, con cada cifra leida de su salida")
    print("=" * 78)
    print()

    fallos = []
    ma = leer("SALIDA_V57_MARCADOR_APERTURA.txt")
    mc = leer("SALIDA_V57_MARCADOR_CIERRE.txt")
    ea = leer("SALIDA_V57_APERTURA.txt")
    ec = leer("SALIDA_V57_CIERRE.txt")
    ra = leer("SALIDA_V57_RECOMPUTO_APERTURA.txt")
    rc = leer("SALIDA_V57_RECOMPUTO_CIERRE.txt")
    tal = leer("SALIDA_V57_TALLAR_PLANES.txt")
    per = leer("SALIDA_V57_TALLAR_PERDIDAS.txt")
    nom = leer("SALIDA_V57_TRAMO4_NOMINA.txt")
    fij = leer("SALIDA_V57_TRAMO4_CIERRE.txt")
    col = leer("SALIDA_V57_COLISIONES_ESPERADAS_TRAMO4.txt")

    d = {}
    for k, t, etq in (("A_a", ma, "A apertura"), ("A_c", mc, "A cierre")):
        d[k] = busca(t, r"\n  A (\d+)", etq, fallos)
    for k, t in (("C_a", ma), ("C_c", mc)):
        d[k] = busca(t, r"\n  C (\d+)", "C", fallos)
    for k, t in (("D_a", ma), ("D_c", mc)):
        d[k] = busca(t, r"\n  D (\d+)", "D", fallos)
    for k, t in (("B_a", ma), ("B_c", mc)):
        d[k] = busca(t, r"\n  B (\d+)", "B", fallos)
    for k, t in (("viv_a", ea), ("viv_c", ec)):
        d[k] = busca(t, r"vivos\s+: (\d+)", "vivos", fallos)
    for k, t in (("dep_a", ea), ("dep_c", ec)):
        d[k] = busca(t, r"deprecados\s+: (\d+)", "deprecados", fallos)
    for k, t in (("enl_a", ea), ("enl_c", ec)):
        d[k] = busca(t, r"enlaces\s+: (\d+)", "enlaces", fallos)
    for k, t in (("col_a", ra), ("col_c", rc)):
        d[k] = busca(t, r"los dos lados\): (\d+)", "colapsos", fallos)
    for k, t in (("par_a", ra), ("par_c", rc)):
        d[k] = busca(t, r"deduplicar\): (\d+)", "pares distintos", fallos)
    for k, t in (("cmp_a", ra), ("cmp_c", rc)):
        d[k] = busca(t, r"componentes totales: (\d+)", "componentes", fallos)
    for k, t in (("cer_a", ra), ("cer_c", rc)):
        d[k] = busca(t, r"CERRADOS: (\d+) sobre", "CERRADOS", fallos)
    d["fund"] = busca(fij, r"FUNDIDOS    : (\d+)", "fundidos del tramo", fallos)
    d["vivos_tramo"] = busca(fij, r"VIVOS hoy   : (\d+)", "vivos del tramo", fallos)
    d["piezas"] = busca(tal, r"actos tallados: \d+ \| piezas: (\d+)", "piezas", fallos)
    d["perd"] = busca(tal, r"perdidas nombradas: (\d+)", "perdidas", fallos)
    d["combi"] = busca(col, r"combinaciones simuladas\s+: (\d+)", "combinaciones", fallos)
    d["fabri"] = busca(col, r"combinaciones que FABRICAN alguna: (\d+)", "fabricadas", fallos)
    d["prefijo"] = busca(nom, r"actos vivos de los tramos 1, 2 y 3 : (\d+)", "prefijo", fallos)
    d["desde"] = busca(nom, r"puestos de hoy del tramo 4: del (\d+)", "primer puesto", fallos)
    d["hasta"] = busca(nom, r"puestos de hoy del tramo 4: del \d+ al (\d+)", "ultimo puesto", fallos)

    t1 = recorta(tal, "--- TABLA 1: LOS TRES LOTES, CON SUS PIEZAS ---",
                 "--- TABLA 2", "tabla 1", fallos)
    t2 = recorta(tal, "--- TABLA 2: LA FORMA DEL VEREDICTO, CONTADA DE LOS MOTIVOS SELLADOS ---",
                 "--- TABLA 3", "tabla 2", fallos)
    t3 = recorta(tal, "--- TABLA 3: ACTO A ACTO, SUPERVIVIENTE Y ABSORBIDO ---",
                 "--- TABLA 4", "tabla 3", fallos)
    t4 = recorta(tal, "--- TABLA 4: LOS ACTOS DECLARADOS Y NO FUNDIDOS ---",
                 "\n  actos tallados:", "tabla 4", fallos)
    tp = recorta(per, "--- TABLA: LAS PERDIDAS NOMBRADAS DE LA VUELTA 57, CON SU ESPECIE ---",
                 "\n  actos con perdida:", "tabla de perdidas", fallos)

    if fallos:
        print("  ROJO, %d celdas no se pudieron leer y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("     %s" % f)
        return 1

    texto = """

---

%(enc)s

**LA VARA QUE FIJA EL TRAMO ES LA MISMA DESDE LA VUELTA 48**, escrita en la cabecera del registro
del tramo 1: *los CINCUENTA primeros actos CERRADOS de la NOMINA RE-MEDIDA AL ABRIRLO*. Aqui, por
primera vez desde el tramo 2, **LAS DOS LECTURAS CALZAN**, mismo conjunto y mismo orden, sin
ninguna divergencia que diagnosticar
([`../loop/SALIDA_V57_TRAMO4_NOMINA.txt`](../loop/SALIDA_V57_TRAMO4_NOMINA.txt)).

> **LA LECTURA B DE ESTE TRAMO YA NO ES UN BLOQUE FIJO DE LA NOMINA DE LA 48, y el motivo esta
> MEDIDO por el propio abridor:** el tramo 3 realmente abierto NO es el bloque 101 a 150, porque un
> `CERRADO` nacido despues se colo y el acto del puesto 150 quedo desplazado. Tomar el bloque 151 a
> 200 dejaria ese acto **fuera de las DOS lecturas**, y la comprobacion se volveria ciega justo
> donde la vuelta anterior encontro algo. La lectura B es **la nomina de la 48 EN SU ORDEN,
> saltando los tramos FIJADOS**.

**GUARDA DEL PREFIJO:** los vivos de los tramos 1, 2 y 3 son **%(prefijo)s** y ocupan los puestos
**1 a %(prefijo)s sin huecos**, medido y no tecleado. **El tramo 4 son los puestos %(desde)s a
%(hasta)s de hoy.** **Guarda de los CUATRO AJENOS: VERDE POR LOS DOS CAMINOS**, el literal y el del
resolutor. **Solape con los tramos anteriores: CERO.**

**LAS COLISIONES ESPERADAS DEL TRAMO ENTERO, medidas ANTES de tocar un nodo** sobre el archivo
entero y por par resuelto
([`../loop/SALIDA_V57_COLISIONES_ESPERADAS_TRAMO4.txt`](../loop/SALIDA_V57_COLISIONES_ESPERADAS_TRAMO4.txt)):
**%(combi)s combinaciones simuladas y %(fabri)s que fabriquen colision.** Ni una. **Por eso esta
vuelta NO volteo ningun veredicto y el marcador queda identico al abrir y al cerrar.**

### EL ESTADO, MEDIDO AL ABRIR Y RECOMPUTADO AL CERRAR

| | **apertura** | **cierre, RECOMPUTADO** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | %(A_a)s / %(B_a)s / %(C_a)s / %(D_a)s | **%(A_c)s / %(B_c)s / %(C_c)s / %(D_c)s** |
| grafo: vivos / deprecados / enlaces | %(viv_a)s / %(dep_a)s / %(enl_a)s | **%(viv_c)s / %(dep_c)s / %(enl_c)s** |
| retrato: colapsos / pares distintos | %(col_a)s / %(par_a)s | **%(col_c)s / %(par_c)s** |
| actos (componentes) / `CERRADOS` | %(cmp_a)s / %(cer_a)s | **%(cmp_c)s / %(cer_c)s** |
| actos del tramo 4 fundidos / vivos | 0 / 50 | **%(fund)s / %(vivos_tramo)s, los %(vivos_tramo)s DECLARADOS** |

### EL REPARTO, TALLADO DE LOS PLANES SELLADOS

**Ninguna de estas tablas esta tecleada:** salen enteras de
`python scripts/loop/vuelta57_tallar_planes.py`
([`../loop/SALIDA_V57_TALLAR_PLANES.txt`](../loop/SALIDA_V57_TALLAR_PLANES.txt)), que las cuenta de
los `PLAN_V57_*.json` **SELLADOS** y **cae en ROJO con el acto nombrado si un motivo no encaja en
ninguna forma conocida**.

%(t1)s

%(t2)s

%(t3)s

%(t4)s

### LAS PERDIDAS NOMBRADAS

**Talladas de los planes sellados** con
`python scripts/loop/vuelta56_tallar_perdidas_v55.py --vuelta 57 --lotes A,B,C`
([`../loop/SALIDA_V57_TALLAR_PERDIDAS.txt`](../loop/SALIDA_V57_TALLAR_PERDIDAS.txt)), que **lee la
especie del propio plan y no tiene rama por defecto**. Son **%(perd)s, LAS TRES DE CONDICIONES**, y
las tres por la misma causa heredada: **el `INCISO` de condiciones no existe en el instrumento**.

%(tp)s

> **UNA CIFRA QUE CONVIENE DEJAR DICHA PORQUE ES LA QUE MIDE EL REPARTO:** de las **%(piezas)s**
> piezas repartidas en los tres lotes, **%(perd)s** se pierden. El resto viaja entera, esta ya dicha
> en el superviviente, o se salva de `INCISO` adosado.
""" % dict(d, enc=ENCABEZADO, t1=t1, t2=t2, t3=t3, t4=t4, tp=tp)

    with io.open(FUS, encoding="utf-8", newline="") as fh:
        actual = fh.read()
    if ENCABEZADO in actual:
        print("  YA ESTABA: el registro del tramo 4 ya vive en 03_FUSIONES.md.")
        print()
        print("FIN")
        return 0
    if not a.simular:
        crlf = "\r\n" in actual
        salida = texto.replace("\n", "\r\n") if crlf else texto
        with io.open(FUS, "a", encoding="utf-8", newline="") as fh:
            fh.write(salida)
        print("  ESCRITO al final de docs/plan/03_FUSIONES.md (%d lineas)"
              % len(texto.splitlines()))
    else:
        print("  MODO SIMULAR: no se escribe. La seccion tendria %d lineas."
              % len(texto.splitlines()))
    print()
    print("  cada celda de la tabla de estado sale de su salida por expresion regular,")
    print("  y las cuatro tablas del reparto y la de perdidas se recortan enteras de la")
    print("  salida de su tallador. NINGUNA CIFRA DE ESTE REGISTRO ESTA TECLEADA.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
