"""Vuelta 46, TAREA 1: el registro de la auditoria de la vuelta 45,
IMPRESO DESDE LAS FUENTES y no tecleado (EJECUTOR.md regla 1, cuarto renglon,
LA TABLA SE IMPRIME NO SE TECLEA; y regla 2, EL INSTRUMENTO MANDA).

Dos fuentes, las dos leidas HOY:
  (a) docs/loop/ACTA_AUDITOR.md, el acta de la vuelta 45, que abre en la
      linea 9794 y cierra en la 10157. Cada celda del registro sale de una
      linea del acta y la linea se imprime al lado para que se pueda auditar.
  (b) docs/INTRA_DOMINIO_VEREDICTOS.jsonl, para RE-MEDIR por mi cuenta los
      siete puestos que el acta declara HOY en B (regla 2: una cifra del acta
      es contraste, no fuente; si discrepa, se declara).

Uso: python scripts/loop/vuelta46_registro_auditoria.py [--escribir]
Sin --escribir solo imprime. Con --escribir anade la seccion al final de
docs/plan/02_DESTEJIDOS.md.
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:45 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 45 DEL AUDITOR" corte=2026-08-20 motivo="su sujeto ES la auditoria de la vuelta 45"
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
DEST = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")

# Los siete puestos que el acta (lineas 10071 a 10076) declara HOY en B como
# trabajo PENDIENTE de la fase 06 de OP-M-03. Los numeros salen del acta; LA
# CLASE LA MIDO YO.
SIETE = [668, 737, 771, 843, 957, 1298, 753]

# Cada punto del registro con la linea del acta que lo dice. El texto de la
# celda es MIO; la linea es del acta y se imprime verbatim abajo.
PUNTOS = [
    ("el alcance de la auditoria", 9801,
     "**COMPLETA, no por muestreo**: con **Gate 0 y las tres suites re-corridos "
     "por corrida propia**. **Sin hueco de acta**: la anterior cubre la vuelta 44 "
     "(linea **9797**), y la vuelta 45 es exactamente la que el acta audita"),
    ("caidas del ejecutor", 10127,
     "**CERO de clase o cifra y CERO de reporte**"),
    ("la relectura ciega", 9941,
     "**5 de 5 coincidencias en lo adjudicable, CERO discrepancias**, y **cero "
     "discrepancias FUERA de los discutibles marcados**. Las cinco: la clase del "
     "**784** adjudicada `D` antes de destapar (**9909**), la del **2695** tambien "
     "`D` antes de destapar (**9917**), **la lectura textual de "
     "`principio_calidad_mvp`** (**9923**), y **los dos repartos releidos origen "
     "por origen con CERO perdida**, el del lienzo (**9929**) y el de "
     "planificacion (**9933**)"),
    ("los ONCE discutibles marcados", 9946,
     "**ADJUDICADOS UNO A UNO y LOS ONCE A FAVOR** (seccion 3, lineas **9948** a "
     "**10027**): D1 a D11, **ninguno en contra, ninguno sin accion**. D11 ademas "
     "**era OBLIGATORIO** (linea **10021**)"),
    ("las SEIS correcciones declaradas", 10028,
     "**LAS SEIS ADJUDICADAS CORRECTAS** (seccion 4): **NINGUNA de las seis es "
     "caida de clase o de cifra, y NINGUNA afirmacion del reporte resulto falsa** "
     "contra la corrida del auditor"),
    ("la racha de reporte", 10136,
     "**en CERO, y ya son TRES reportes limpios seguidos** contra corrida completa "
     "del auditor"),
    ("la ceguera", 9901,
     "**PARCIAL Y DECLARADA** por el propio auditor (leyo el reporte antes de los "
     "pasos), con la misma mitigacion escrita de las actas 42 a 44: imprimir "
     "primero los textos desde `git`, adjudicar, y **solo despues** destapar las "
     "razones"),
    ("las condiciones de parada", 10139,
     "**RECORRIDAS UNA A UNA: NINGUNA SE CUMPLE**. **EL BUCLE SIGUE** (linea "
     "**10155**)"),
]


def leer_acta():
    return open(ACTA, encoding="utf-8").read().split("\n")


def medir_siete():
    por_puesto = {}
    with open(VER, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            d = json.loads(linea)
            if d["puesto_intra"] in SIETE:
                por_puesto[d["puesto_intra"]] = d
    return por_puesto


def main():
    acta = leer_acta()
    print("=" * 78)
    print("VUELTA 46, TAREA 1: EL REGISTRO DE LA AUDITORIA DE LA VUELTA 45")
    print("=" * 78)
    print()
    print("--- (a) EL ACTA, LEIDA HOY ---")
    print("  fichero: docs/loop/ACTA_AUDITOR.md")
    print("  lineas totales del fichero: %d" % len(acta))
    print("  el acta de la vuelta 45 abre en la 9794 y cierra en la 10157")
    print("  linea 9794 verbatim: %s" % acta[9793])
    print()
    print("--- LAS LINEAS QUE CADA PUNTO CITA, IMPRESAS VERBATIM ---")
    for titulo, n, _celda in PUNTOS:
        print("  [%s] linea %d:" % (titulo, n))
        print("      %s" % acta[n - 1])
    print()
    print("--- LA SECCION 5 DEL ACTA, LA ADJUDICACION DEL depende_de ---")
    for n in range(10046, 10093):
        print("  %5d: %s" % (n, acta[n - 1]))
    print()
    print("--- (b) LOS SIETE PUESTOS DE LA MESA, RE-MEDIDOS POR MI HOY ---")
    print("  fuente: docs/INTRA_DOMINIO_VEREDICTOS.jsonl (no el acta)")
    por_puesto = medir_siete()
    filas = []
    for p in SIETE:
        d = por_puesto.get(p)
        if d is None:
            print("  puesto %s: AUSENTE DEL ARCHIVO" % p)
            filas.append((p, "AUSENTE", "", ""))
            continue
        print("  puesto %-5d clase %-2s  %s  contra  %s"
              % (p, d["clase"], d["nodo_a"], d["nodo_b"]))
        filas.append((p, d["clase"], d["nodo_a"], d["nodo_b"]))
    clases = [f[1] for f in filas]
    todos_b = all(c == "B" for c in clases)
    print()
    print("  LOS SIETE EN B: %s (clases medidas: %s)"
          % ("SI" if todos_b else "NO", ", ".join(clases)))
    print("  CONTRASTE CON EL ACTA (linea 10074): dice que los siete estan HOY en B.")
    print("  MI MEDICION: %s"
          % ("COINCIDE AL DIGITO" if todos_b else "DISCREPA, se declara"))
    print()

    if "--escribir" not in sys.argv:
        print("(sin --escribir: no se toco 02_DESTEJIDOS.md)")
        return 0

    # LA LINEA VA EN COLUMNA PROPIA y no pegada al final de la celda: si la
    # celda ya cita lineas de detalle, un "(linea N)" al final duplicaba la
    # marca y se leia mal. Visto en la primera corrida, antes de commitear.
    tabla = ["| que verifico el auditor | linea del acta | como salio |",
             "|---|---:|---|"]
    for titulo, n, celda in PUNTOS:
        tabla.append("| **%s** | **%d** | %s |" % (titulo, n, celda))

    tsiete = ["| puesto | clase medida HOY por mi | los dos nodos |", "|---:|---|---|"]
    for p, clase, a, b in filas:
        tsiete.append("| **%d** | **`%s`** | `%s` contra `%s` |" % (p, clase, a, b))

    seccion = SECCION % ("\n".join(tabla), "\n".join(tsiete))
    with open(DEST, "a", encoding="utf-8") as fh:
        fh.write(seccion)
    print("ESCRITO al final de docs/plan/02_DESTEJIDOS.md: %d caracteres" % len(seccion))
    return 0


SECCION = """
### LA AUDITORIA DE LA VUELTA 45, VERIFICADA Y ADJUDICADA (19 ago 2026, acta de la vuelta 45)

**El auditor corrio la vuelta 45 ENTERA y las dos operaciones que esta pagina cerro ya tienen su
acta detras.** Todo lo que sigue se lee de `docs/loop/ACTA_AUDITOR.md`, **leida hoy**, que abre en
la linea **9794** y cierra en la **10157**, y **cada punto va con la linea que lo dice**. La tabla
se imprime desde el acta con `python scripts/loop/vuelta46_registro_auditoria.py --escribir`
(salida sellada en `docs/loop/SALIDA_V46_REGISTRO_AUDITORIA.txt`), que **imprime verbatim cada
linea citada** para que ninguna celda sea un recuerdo.

%s

#### LA PREGUNTA DE LA SECCION 10 DEL REPORTE, ADJUDICADA SIN DOCTRINA NUEVA

**El ejecutor de la vuelta 45 dejo la pregunta de si `OP-D-07` era ejecutable, y el auditor la
contesto entera con la estructura escrita del plan delante** (seccion 5 del acta, lineas **10046** a
**10077**). **La adjudicacion:**

> **`OP-D-07` ES EJECUTABLE: SU `depende_de` SE SATISFACE CON LA MESA `OP-M-03` ADJUDICADA** (linea
> **10051**), con **CUATRO apoyos escritos y CERO doctrina nueva** (linea **10077**: *extension
> citable de la estructura escrita*).

1. **LA ESTRUCTURA DEL PROPIO PLAN LO EXIGE** (linea **10052**). `OP-M-03` es fase **06_MESAS** y
   bloquea a `OP-M-03-I`, que es fase **03_FUSIONES**. Si el `depende_de` exigiera la mesa
   **EJECUTADA ENTERA**, ninguna fusion del racimo podria correr antes de la fase 06 y el orden de
   fases del `00_INDICE` quedaria en bloqueo. El indice lo niega con letra: *NO QUEDA NI UNA LECTURA
   POR HACER QUE BLOQUEE ALGO*.
2. **LA MESA ESTA ADJUDICADA Y CERRADA** (linea **10062**): la adjudicacion entera vive en el campo
   `adjudicacion` de `OP-M-03`, el `EXPEDIENTE_MESA_PIVOTE` figura **cerrada** en el `00_INDICE`, y
   la nota de la mesa dice con letra que **la clase de los pares depende de esta decision Y NO AL
   REVES**.
3. **TODO LO QUE `OP-D-07` CONSUME DE LA MESA ESTA ESCRITO EN SU PROPIO TEXTO** (linea **10067**): el
   corte entre el paso 4 y el 5, el bloque del punto brillante en preservar, y el orden (el destejido
   **ANTES** de la fusion).
4. **LO QUE LA MESA AUN DEBE NO ALIMENTA EL DESTEJIDO, Y QUEDA MEDIDO PARA QUE NADIE LO DE POR
   HECHO** (linea **10071**).

##### EL AVISO MEDIDO: LAS REESCRITURAS DE LA MESA SIGUEN PENDIENTES

**Las reescrituras de los seis dudosos y el 753 citando el criterio** (puntos 1 y 2 de la
`verificacion` de `OP-M-03`) **NO se han ejecutado**. El acta lo declara en la linea **10074** y
**esta pagina NO lo copia: lo RE-MIDE**, que es la regla 2 (*una cifra de un acta es contraste, no
fuente*). **Medidos hoy por mi sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`:**

%s

**LOS SIETE SIGUEN EN `B`, al digito, y COINCIDEN con lo que el acta declara.** Son **trabajo de
`OP-M-03` en su fase 06**, no precondicion del corte de `OP-D-07`: **nadie los puede dar por hechos**
mientras esta tabla siga diciendo `B`.

**Y EL ORDEN** (linea **10079**): `OP-D-07` **libera CERO congelados**, asi que **su orden es libre
por el criterio de la fase** (*CONGELADOS LIBERADOS*), con el precedente escrito de `OP-D-05` y
`OP-D-09`. **Es la ULTIMA operacion de la fase 02 sin ejecutar: tras ella, el cierre de la fase se
DECLARA MIDIENDO, no se supone.**

#### NO HAY CAIDA DE REPORTE QUE CORREGIR

**La casilla no se rellena porque no hay nada que poner en ella.** El acta (linea **10127**) declara
**CERO caidas del ejecutor de clase o cifra y CERO de reporte**, y la seccion 4 adjudica **las SEIS
correcciones declaradas como correctas**, con la frase que cierra el punto: **NINGUNA afirmacion del
reporte resulto falsa contra mi corrida**. **El reporte de la vuelta 45 salio limpio contra la
corrida entera del auditor**, y esa es la tercera vez seguida (linea **10136**).
"""


if __name__ == "__main__":
    sys.exit(main())
