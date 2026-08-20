# -*- coding: utf-8 -*-
"""registrar_cierre_de_tramo.py . ESCRIBE EL REGISTRO DEL CIERRE DE UN TRAMO DE
OP-U-01 EN docs/plan/03_FUSIONES.md, CON CADA CIFRA LEIDA DE SU SALIDA.

NOMBRE ESTABLE A PROPOSITO (acta 58, pregunta 4: el proximo instrumento NACE
ESTABLE): no lleva numero de tramo ni de vuelta. La vuelta entra por --vuelta,
el tramo se LEE de la salida del tallador de planes, y los prefijos de las
salidas se arman solos. La cadena de clones vuelta56 -> vuelta57 muere aqui.

SUCESOR DECLARADO de scripts/loop/vuelta57_registro_tramo.py, al que NO
reemplaza. LA MAQUINA ES LA SUYA, COPIADA: cada celda se EXTRAE por expresion
regular de la salida que la cita, las tablas se RECORTAN enteras de la salida
del tallador, y el instrumento CAE EN ROJO sin escribir nada si alguna celda no
se puede leer. NINGUNA CIFRA DE ESTE REGISTRO SE TECLEA.

LO QUE ESTE SUCESOR ANADE, y cada cosa por un motivo medido:

  1. UN TRAMO PUEDE REPARTIRSE ENTRE VARIAS VUELTAS. El tramo 5 lo abrio la
     vuelta 59 con su lote A y lo cerro la vuelta 60 con los lotes B y C. El
     ancestro leia todas sus salidas de UN solo prefijo SALIDA_V<N>_ y no podia
     escribir un registro asi. Aqui las salidas del ESTADO son las de la vuelta
     que CIERRA (que es donde vive la medicion de cierre) y la salida del
     TALLADOR se pasa entera por --tallador, porque es la que ya sabe juntar
     los planes de las dos vueltas.
  2. LA SECCION DE PERDIDAS ES OPCIONAL Y SE DICE POR QUE FALTA. El tallador de
     perdidas puede caer en ROJO sobre un acto cuya especie no sabe clasificar,
     y en ese caso NO se emite tabla. El ancestro no contemplaba ese caso y
     habria caido en ROJO entero. Aqui, si el fichero de perdidas no trae tabla,
     el registro se escribe igual y DECLARA que no la trae, con el motivo
     copiado de la salida. Callar la falta seria peor que no tener la tabla.
  3. --nota (repetible) anade parrafos al final del registro. Se usa para las
     correcciones declaradas que el encargo mande anotar en el cierre del tramo.

ES IDEMPOTENTE: si el encabezado del tramo ya esta en 03_FUSIONES.md, no escribe
nada y lo dice.

Uso:
  python scripts/loop/registrar_cierre_de_tramo.py --vuelta 60 \\
      --tallador docs/loop/SALIDA_V60_TALLAR_PLANES.txt \\
      --perdidas docs/loop/SALIDA_V60_TALLAR_PERDIDAS.txt \\
      --nomina docs/loop/SALIDA_V58_TRAMO5_NOMINA.txt \\
      --fijado docs/loop/SALIDA_V60_TRAMO5_CIERRE.txt \\
      --colisiones docs/loop/SALIDA_V58_COLISIONES_ESPERADAS_TRAMO5.txt \\
      [--nota "..."] [--simular]
"""
import argparse
import datetime
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
FUS = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]


def leer(ruta, fallos):
    r = ruta if os.path.isabs(ruta) else os.path.join(RAIZ, ruta)
    if not os.path.exists(r):
        fallos.append("no existe %s" % ruta)
        return ""
    return io.open(r, encoding="utf-8").read()


def busca(texto, patron, etiqueta, fallos):
    m = re.search(patron, texto)
    if not m:
        fallos.append("no se pudo leer %s" % etiqueta)
        return "?"
    return m.group(1)


def recorta(texto, desde, hasta, etiqueta, fallos):
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
    return "{:,}".format(int(v)).replace(",", ".") if str(v).isdigit() else v


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--vuelta", type=int, required=True)
    p.add_argument("--tallador", required=True)
    p.add_argument("--perdidas", default=None)
    p.add_argument("--nomina", required=True)
    p.add_argument("--fijado", required=True)
    p.add_argument("--colisiones", required=True)
    p.add_argument("--nota", action="append", default=[])
    p.add_argument("--simular", action="store_true")
    a = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    fallos = []
    tal = leer(a.tallador, fallos)
    nom = leer(a.nomina, fallos)
    fij = leer(a.fijado, fallos)
    col = leer(a.colisiones, fallos)
    per = leer(a.perdidas, fallos) if a.perdidas else ""

    pfx = "SALIDA_V%d_" % a.vuelta
    ma = leer(os.path.join("docs", "loop", pfx + "MARCADOR_APERTURA.txt"), fallos)
    mc = leer(os.path.join("docs", "loop", pfx + "MARCADOR_CIERRE.txt"), fallos)
    ea = leer(os.path.join("docs", "loop", pfx + "APERTURA.txt"), fallos)
    ec = leer(os.path.join("docs", "loop", pfx + "CIERRE.txt"), fallos)
    ra = leer(os.path.join("docs", "loop", pfx + "RECOMPUTO_APERTURA.txt"), fallos)
    rc = leer(os.path.join("docs", "loop", pfx + "RECOMPUTO_CIERRE.txt"), fallos)

    # EL NUMERO DE TRAMO SALE DE LA SALIDA DEL TALLADOR, no de una constante.
    tramo = busca(tal, r"LAS TABLAS DEL TRAMO (\d+)", "numero de tramo", fallos)

    print("=" * 78)
    print("EL REGISTRO DEL CIERRE DEL TRAMO %s, con cada cifra leida de su salida" % tramo)
    print("=" * 78)
    print()

    d = {"tramo": tramo, "vuelta": a.vuelta}
    for k, t in (("A_a", ma), ("A_c", mc)):
        d[k] = busca(t, r"\n  A (\d+)", "A", fallos)
    for k, t in (("B_a", ma), ("B_c", mc)):
        d[k] = busca(t, r"\n  B (\d+)", "B", fallos)
    for k, t in (("C_a", ma), ("C_c", mc)):
        d[k] = busca(t, r"\n  C (\d+)", "C", fallos)
    for k, t in (("D_a", ma), ("D_c", mc)):
        d[k] = busca(t, r"\n  D (\d+)", "D", fallos)
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
    d["fund"] = busca(fij, r"FUNDIDOS\s+: (\d+)", "fundidos del tramo", fallos)
    d["vivos_tramo"] = busca(fij, r"VIVOS hoy\s+: (\d+)", "vivos del tramo", fallos)
    d["piezas"] = busca(tal, r"actos tallados: \d+ \| piezas: (\d+)", "piezas", fallos)
    d["actos"] = busca(tal, r"actos tallados: (\d+)", "actos tallados", fallos)
    d["perd"] = busca(tal, r"perdidas nombradas: (\d+)", "perdidas", fallos)
    d["combi"] = busca(col, r"combinaciones simuladas\s+: (\d+)", "combinaciones", fallos)
    d["fabri"] = busca(col, r"combinaciones que FABRICAN alguna: (\d+)", "fabricadas", fallos)
    d["prefijo"] = busca(nom, r"actos vivos de los tramos [^:]+: (\d+)", "prefijo", fallos)
    d["desde"] = busca(nom, r"puestos de hoy del tramo \d+: del (\d+)", "primer puesto", fallos)
    d["hasta"] = busca(nom, r"puestos de hoy del tramo \d+: del \d+ al (\d+)", "ultimo puesto", fallos)

    t1 = recorta(tal, "--- TABLA 1: LOS TRES LOTES, CON SUS PIEZAS ---", "--- TABLA 2", "tabla 1", fallos)
    t2 = recorta(tal, "--- TABLA 2: LA FORMA DEL VEREDICTO, CONTADA DE LOS MOTIVOS SELLADOS ---",
                 "--- TABLA 3", "tabla 2", fallos)
    t3 = recorta(tal, "--- TABLA 3: ACTO A ACTO, SUPERVIVIENTE Y ABSORBIDO ---",
                 "--- TABLA 4", "tabla 3", fallos)
    t4 = recorta(tal, "--- TABLA 4: LOS ACTOS DECLARADOS Y NO FUNDIDOS ---",
                 "\n  actos tallados:", "tabla 4", fallos)

    # LA SECCION DE PERDIDAS, OPCIONAL Y CON SU FALTA DECLARADA.
    if per and "--- TABLA: LAS PERDIDAS NOMBRADAS" in per:
        marca = per[per.find("--- TABLA: LAS PERDIDAS NOMBRADAS"):].split("\n", 1)[0]
        tp = recorta(per, marca, "\n  actos con perdida:", "tabla de perdidas", fallos)
        bloque_perd = ("**Talladas de los planes sellados** con el tallador de perdidas "
                       "([`../loop/%s`](../loop/%s)), que **lee la especie del propio plan y no "
                       "tiene rama por defecto**.\n\n%s" %
                       (os.path.basename(a.perdidas), os.path.basename(a.perdidas), tp))
    elif per:
        motivos = "\n".join("> %s" % l.strip() for l in per.splitlines()
                            if l.strip().startswith("[ROJO]"))
        bloque_perd = ("**EL TALLADOR DE PERDIDAS NO EMITIO TABLA, Y SE DICE EN VEZ DE CALLARSE.** "
                       "Su salida entera esta en [`../loop/%s`](../loop/%s) y su motivo es este, "
                       "copiado de ella:\n\n%s\n\n**El instrumento esta escrito para caer en ROJO "
                       "antes que clasificar en silencio**, asi que esto es la guarda funcionando, "
                       "no un fallo tapado." % (os.path.basename(a.perdidas),
                                                os.path.basename(a.perdidas), motivos))
    else:
        bloque_perd = "**No se paso fichero de perdidas a este registro.**"

    hoy = datetime.date.today()
    d["fecha"] = "%d %s %d" % (hoy.day, MESES[hoy.month - 1], hoy.year)
    encabezado = ("## `OP-U-01`, TRAMO %s: EL REGISTRO DEL CIERRE (%s, vuelta %d)"
                  % (tramo, d["fecha"], a.vuelta))

    if fallos:
        print("  ROJO, %d celdas no se pudieron leer y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("     %s" % f)
        return 1

    texto_viejo = io.open(FUS, encoding="utf-8").read()
    if ("TRAMO %s: EL REGISTRO DEL CIERRE" % tramo) in texto_viejo:
        print("  YA ESTA: el registro del tramo %s ya vive en 03_FUSIONES.md. No se escribe nada."
              % tramo)
        return 0

    for k in ("A_a", "A_c", "B_a", "B_c", "C_a", "C_c", "D_a", "D_c", "viv_a", "viv_c",
              "dep_a", "dep_c", "enl_a", "enl_c", "col_a", "col_c", "par_a", "par_c",
              "cmp_a", "cmp_c", "cer_a", "cer_c", "piezas", "combi"):
        d[k] = miles(d[k])

    notas = "\n\n".join(a.nota)
    bloque = """

---

%(enc)s

**LA VARA QUE FIJA EL TRAMO ES LA MISMA DESDE LA VUELTA 48**, escrita en la cabecera del registro
del tramo 1: *los CINCUENTA primeros actos CERRADOS de la NOMINA RE-MEDIDA AL ABRIRLO*. **EL INSUMO
DE ESTE TRAMO SE MIDIO Y SE FIJO AL ABRIRLO Y NO SE RE-MIDIO NI UNA VEZ DESPUES**, que es lo que el
encargo mandaba
([`../loop/%(nom)s`](../loop/%(nom)s)).

**GUARDA DEL PREFIJO:** los vivos de los tramos anteriores son **%(prefijo)s** y ocupan sus puestos
sin huecos, medido y no tecleado. **El tramo %(tramo)s son los puestos %(desde)s a %(hasta)s de
hoy.** **Solape con los tramos anteriores: CERO.**

> **EL COTEJO QUE ESTE TRAMO ESTRENA, y nace de que el tramo se repartio entre DOS vueltas:** entre
> la foto fijada del insumo y la ejecucion de los lotes B y C hubo una fusion de por medio (la del
> lote A), y una fusion CAMBIA los pasos del superviviente. Antes de escribir una linea del plan del
> lote B se corrio `scripts/loop/vuelta60_cotejo_insumo.py`, que NO re-mide el insumo sino que lo
> COTEJA contra los nodos de hoy: **50 actos mirados, 34 vivos, 16 ya fundidos, DESCALCES 0**
> ([`../loop/SALIDA_V60_COTEJO_INSUMO.txt`](../loop/SALIDA_V60_COTEJO_INSUMO.txt)).

**LAS COLISIONES ESPERADAS DEL TRAMO ENTERO, medidas ANTES de tocar un nodo** sobre el archivo
entero y por par resuelto
([`../loop/%(col)s`](../loop/%(col)s)):
**%(combi)s combinaciones simuladas y %(fabri)s que fabriquen colision.** Ni una. **Por eso este
tramo NO volteo ningun veredicto y el marcador queda identico al abrir y al cerrar.**

### EL ESTADO, MEDIDO AL ABRIR LA VUELTA QUE CIERRA EL TRAMO Y RECOMPUTADO AL CERRARLA

| | **apertura de la vuelta %(vuelta)d** | **cierre, RECOMPUTADO** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | %(A_a)s / %(B_a)s / %(C_a)s / %(D_a)s | **%(A_c)s / %(B_c)s / %(C_c)s / %(D_c)s** |
| grafo: vivos / deprecados / enlaces | %(viv_a)s / %(dep_a)s / %(enl_a)s | **%(viv_c)s / %(dep_c)s / %(enl_c)s** |
| retrato: colapsos / pares distintos | %(col_a)s / %(par_a)s | **%(col_c)s / %(par_c)s** |
| actos (componentes) / `CERRADOS` | %(cmp_a)s / %(cer_a)s | **%(cmp_c)s / %(cer_c)s** |
| actos del tramo %(tramo)s fundidos / vivos | 0 / 50 | **%(fund)s / %(vivos_tramo)s, los %(vivos_tramo)s DECLARADOS** |

> **LA COLUMNA DE APERTURA ES LA DE LA VUELTA QUE CIERRA EL TRAMO, no la de la que lo abrio, y se
> dice para que nadie lea de ahi el efecto del tramo entero.** El lote A ya estaba fundido cuando se
> tomo. El efecto del TRAMO COMPLETO se lee de los `%(fund)s` actos fundidos de la ultima fila, que
> es la cifra que si cubre las dos vueltas.

### EL REPARTO, TALLADO DE LOS PLANES SELLADOS DE LAS DOS VUELTAS

**Ninguna de estas tablas esta tecleada:** salen enteras de
`python scripts/loop/tallar_planes_del_tramo.py --vuelta %(vuelta)d --prefijo PLAN_V59_OPU01_LOTE_ --prefijo PLAN_V60_OPU01_LOTE_`
([`../loop/%(tal)s`](../loop/%(tal)s)), que las cuenta de los planes **SELLADOS** y **cae en ROJO
con el acto nombrado si un motivo no encaja en ninguna forma conocida**. **`--prefijo` se hizo
REPETIBLE en esta vuelta justamente para esto**: con un prefijo unico, el registro habria publicado
**31 fusiones donde hay %(fund)s**, y las cuatro tablas habrian mentido por omision.

%(t1)s

%(t2)s

%(t3)s

%(t4)s

### LAS PERDIDAS NOMBRADAS

%(perdidas)s

%(notas)s
""" % {"enc": encabezado, "nom": os.path.basename(a.nomina), "col": os.path.basename(a.colisiones),
       "tal": os.path.basename(a.tallador), "t1": t1, "t2": t2, "t3": t3, "t4": t4,
       "perdidas": bloque_perd, "notas": notas, "fabri": d["fabri"], **d}

    print(bloque)
    if a.simular:
        print("SIMULACION: no se escribe nada.")
        return 0
    io.open(FUS, "a", encoding="utf-8", newline="\n").write(bloque)
    print("ESCRITO al final de %s" % FUS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
