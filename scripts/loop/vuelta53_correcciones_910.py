# -*- coding: utf-8 -*-
"""vuelta53_correcciones_910.py . LAS CELDAS QUE EL BARRIDO `9.10` DEL CIERRE DE
LA VUELTA 53 CORRIGE, TODAS CON TACHADO, CONTADOR CUADRADO Y NOTA FECHADA.

LA REGLA QUE MANDA, y son tres a la vez:
  - `9.10` del banco: quien mueve una clase barre las tablas VIGENTES antes de
    cerrar. Corrido DESPUES del ultimo movimiento de la vuelta.
  - `D7` de la vuelta 50, adjudicado: quien corrige una celda con contador
    CUADRA EL CONTADOR y ADOSA la nota fechada. Ninguna nota vieja se reescribe.
  - HERMANDAD DE LAS DOS TABLAS POR DOMINIO, escrita en las dos sedes por la
    TAREA 1.1 de esta misma vuelta: la 100.2 del INFORME y la tabla de la
    seccion `a` del RECOMPUTO se mueven JUNTAS y en el mismo acto.

LO QUE ESTA VUELTA MOVIO, y de ahi salen todas las celdas: DOCE actos fundidos
de `OP-U-01` en tres lotes y QUINCE veredictos corregidos por `P.16` (once
volteos por maquina y cuatro relecturas del filo).

CUATRO DOMINIOS SE MUEVEN Y SEIS NO, medido hoy: `core` de 329 a 325, `quality`
de 123 a 119, `environmental` de 29 a 28 y `franquicias` de 18 a 15. Quedan
identicos al digito `health_safety` 43, `exportacion` 15, `entrega` 2, `compras`
1, `risk_management` 0 y `seguridad_digital` 3.

IDEMPOTENTE: cada sustitucion comprueba primero si su resultado ya esta escrito.

Uso: python scripts/loop/vuelta53_correcciones_910.py [--simular]
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REC = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388.md")
INF = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_INFORME.md")

MEDIDO = (
    "Medido HOY con `python scripts/plan/recomputo_3388.py` y `python scripts/recomputar_marcador.py "
    "3388` DESPUES del ultimo movimiento de la vuelta 53 (`../loop/SALIDA_V53_RECOMPUTO_CIERRE.txt` "
    "y `../loop/SALIDA_V53_MARCADOR_CIERRE.txt`)"
)
MEDIDO_INF = MEDIDO.replace("../loop/", "loop/")

QUE_MOVIO = (
    "la vuelta 53 fundio DOCE actos de `OP-U-01` en tres lotes (el lienzo de propuesta de valor, "
    "los prompts, los warrants, la huella de carbono, los costos de franquicia, el abogado de "
    "franquicias, la franquicia inadvertida, la gestion por objetivos, el pareto, el poka yoke, el "
    "dmaic select y la investigacion del cliente) y corrigio QUINCE veredictos por `P.16`: ONCE "
    "volteos por maquina (475, 1175, 559, 1865, 2075, 2090, 2181, 2488, 2551, 2613 y 2742) y "
    "CUATRO relecturas del filo (360, 204, 811 y 1222)"
)

CAMBIOS = [
    # ---------------- RECOMPUTO, las tres filas del retrato ----------------
    (REC, "9.10 fila 246, A crudas",
     "~~**571**~~ ~~**566**~~ **563** **[CORREGIDA ~~SIETE~~ ~~OCHO~~ NUEVE VECES,",
     "~~**571**~~ ~~**566**~~ ~~**563**~~ **551** **[CORREGIDA ~~SIETE~~ ~~OCHO~~ ~~NUEVE~~ DIEZ VECES,"),
    (REC, "9.10 fila 246, nota adosada",
     "La nota de arriba, del mismo dia y de la TAREA 1.1, no se reescribe]** |",
     "La nota de arriba, del mismo dia y de la TAREA 1.1, no se reescribe] "
     "[DECIMA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 53, barrido "
     "`9.10` del cierre): de 563 a 551, DOCE menos, porque " + QUE_MOVIO + ". " + MEDIDO +
     ", paso 1. Las notas de las vueltas 51 y 52 no se reescriben]** |"),

    (REC, "9.10 fila 247, colapsos",
     "~~**49**~~ ~~**57**~~ **60** **[CORREGIDA ~~CUATRO~~ ~~CINCO~~ SEIS VECES,",
     "~~**49**~~ ~~**57**~~ ~~**60**~~ **72** **[CORREGIDA ~~CUATRO~~ ~~CINCO~~ ~~SEIS~~ SIETE VECES,"),
    (REC, "9.10 fila 247, nota adosada",
     "cada fusion convierte el par `A` interno del acto en un par cuyos dos ids resuelven al mismo nodo vivo. Medido HOY con `python scripts/plan/recomputo_3388.py` y `python scripts/recomputar_marcador.py 3388` DESPUES del ultimo movimiento de la vuelta 52 (`../loop/SALIDA_V52_RECOMPUTO_CIERRE.txt` y `../loop/SALIDA_V52_MARCADOR_CIERRE.txt`), paso 1]** |",
     "cada fusion convierte el par `A` interno del acto en un par cuyos dos ids resuelven al mismo nodo vivo. Medido HOY con `python scripts/plan/recomputo_3388.py` y `python scripts/recomputar_marcador.py 3388` DESPUES del ultimo movimiento de la vuelta 52 (`../loop/SALIDA_V52_RECOMPUTO_CIERRE.txt` y `../loop/SALIDA_V52_MARCADOR_CIERRE.txt`), paso 1] "
     "[SEPTIMA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 53, barrido "
     "`9.10` del cierre): de 60 a 72, DOCE colapsos mas, UNO POR CADA ACTO QUE ESTA VUELTA FUNDIO, "
     "porque cada fusion convierte el par `A` interno del acto en un par cuyos dos ids resuelven al "
     "mismo nodo vivo. " + MEDIDO + ", paso 1]** |"),

    (REC, "9.10 fila 248, pares distintos",
     "~~**522**~~ ~~**509**~~ **503** **[CORREGIDA ~~SIETE~~ ~~OCHO~~ NUEVE VECES,",
     "~~**522**~~ ~~**509**~~ ~~**503**~~ **479** **[CORREGIDA ~~SIETE~~ ~~OCHO~~ ~~NUEVE~~ DIEZ VECES,"),
    (REC, "9.10 fila 248, nota adosada",
     "que vuelve a ser la resta exacta de las dos filas de arriba (563 crudas menos 60 colapsos). " + MEDIDO.replace("vuelta 53", "vuelta 52").replace("V53", "V52"),
     "que vuelve a ser la resta exacta de las dos filas de arriba (563 crudas menos 60 colapsos). "
     + MEDIDO.replace("vuelta 53", "vuelta 52").replace("V53", "V52") +
     ", paso 1] [DECIMA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 53, "
     "barrido `9.10` del cierre): de 503 a 479, que vuelve a ser la resta exacta de las dos filas "
     "de arriba (551 crudas menos 72 colapsos). " + MEDIDO),

    # ---------------- RECOMPUTO, el checkpoint ii ----------------
    (REC, "9.10 checkpoint ii, los dos parentesis",
     "| **ii** | A vigentes resueltas del retrato (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ **503**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ **503**)",
     "| **ii** | A vigentes resueltas del retrato (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ ~~503~~ **479**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ ~~503~~ **479**)"),

    # ---------------- RECOMPUTO, la tabla por dominio ----------------
    (REC, "9.10 RECOMPUTO fila core",
     "| core | 1.445 | ~~344~~ **329** | ~~23,8 %~~ **22,8 %** **[CORREGIDA UNA VEZ,",
     "| core | 1.445 | ~~344~~ ~~329~~ **325** | ~~23,8 %~~ ~~22,8 %~~ **22,5 %** **[CORREGIDA ~~UNA VEZ~~ DOS VECES,"),
    (REC, "9.10 RECOMPUTO fila quality",
     "| quality | 844 | ~~126~~ **123** | ~~14,9 %~~ **14,6 %** **[CORREGIDA UNA VEZ,",
     "| quality | 844 | ~~126~~ ~~123~~ **119** | ~~14,9 %~~ ~~14,6 %~~ **14,1 %** **[CORREGIDA ~~UNA VEZ~~ DOS VECES,"),
    (REC, "9.10 RECOMPUTO fila environmental",
     "| environmental | 170 | 29 | 17,1 % |",
     "| environmental | 170 | ~~29~~ **28** | ~~17,1 %~~ **16,5 %** **[CORREGIDA UNA VEZ, 20 ago "
     "2026 (vuelta 53, barrido `9.10` del cierre), Y ESTA VUELTA SI LA MOVIO: el acto de la huella "
     "de carbono es de `environmental` y su volteo `P.16` (puesto 1865) baja la `A` en uno. " +
     MEDIDO + ". HERMANA de la fila de `environmental` de la 100.2 de `../INTRA_DOMINIO_INFORME.md`, "
     "corregida en este mismo acto]** |"),
    (REC, "9.10 RECOMPUTO fila franquicias",
     "| franquicias | 148 | 18 | 12,2 % |",
     "| franquicias | 148 | ~~18~~ **15** | ~~12,2 %~~ **10,1 %** **[CORREGIDA UNA VEZ, 20 ago 2026 "
     "(vuelta 53, barrido `9.10` del cierre), Y ES EL DOMINIO QUE MAS SE MUEVE DE LA VUELTA: TRES de "
     "los doce actos fundidos son de `franquicias` (los costos, el abogado y la franquicia "
     "inadvertida) y sus tres volteos `P.16` (puestos 2075, 2090 y 2181) bajan la `A` en tres. " +
     MEDIDO + ". HERMANA de la fila de `franquicias` de la 100.2 de `../INTRA_DOMINIO_INFORME.md`, "
     "corregida en este mismo acto]** |"),
    (REC, "9.10 RECOMPUTO fila total",
     "~~**571**~~ ~~**566**~~ **563** | ~~**17,2 %**~~ ~~**17,1 %**~~ ~~**17,0 %**~~ ~~**16,9 %**~~ ~~**16,7 %**~~ **16,6 %**",
     "~~**571**~~ ~~**566**~~ ~~**563**~~ **551** | ~~**17,2 %**~~ ~~**17,1 %**~~ ~~**17,0 %**~~ ~~**16,9 %**~~ ~~**16,7 %**~~ ~~**16,6 %**~~ **16,3 %**"),
    (REC, "9.10 RECOMPUTO total, nota adosada",
     "329 mas 123 mas 43 mas 2 mas 29 mas 1 mas 18 mas 0 mas 15 mas 3 son 563]** |",
     "329 mas 123 mas 43 mas 2 mas 29 mas 1 mas 18 mas 0 mas 15 mas 3 son 563] "
     "[SEGUNDA CORRECCION, 20 ago 2026 (vuelta 53, barrido `9.10` del cierre): de 563 a 551 porque "
     + QUE_MOVIO + ". CUATRO dominios se mueven y SEIS no: `core` de 329 a 325, `quality` de 123 a "
     "119, `environmental` de 29 a 28 y `franquicias` de 18 a 15; quedan identicos al digito "
     "`health_safety` 43, `exportacion` 15, `entrega` 2, `compras` 1, `risk_management` 0 y "
     "`seguridad_digital` 3. " + MEDIDO + ". LA SUMA DE LA COLUMNA VUELVE A CUADRAR CON EL TOTAL, "
     "comprobado hoy: 325 mas 119 mas 43 mas 2 mas 28 mas 1 mas 15 mas 0 mas 15 mas 3 son 551]** |"),

    # ---------------- INFORME, el apendice 100.1 ----------------
    (INF, "9.10 100.1 fila A",
     "| **A** | ~~**583** (17,2 %)~~ ~~582~~ ~~581~~ ~~576~~ ~~575 (17,0 %)~~ ~~574~~ ~~573~~ ~~571 (16,9 %)~~ ~~566 (16,7 %)~~ **563** (16,6 %), ver las correcciones declaradas debajo |",
     "| **A** | ~~**583** (17,2 %)~~ ~~582~~ ~~581~~ ~~576~~ ~~575 (17,0 %)~~ ~~574~~ ~~573~~ ~~571 (16,9 %)~~ ~~566 (16,7 %)~~ ~~563 (16,6 %)~~ **551** (16,3 %), ver las correcciones declaradas debajo |"),
    (INF, "9.10 100.1 fila B",
     "| **B** | ~~89~~ ~~87~~ ~~84~~ ~~83~~ ~~82~~ ~~81~~ ~~80~~ ~~79~~ ~~77~~ **75** |",
     "| **B** | ~~89~~ ~~87~~ ~~84~~ ~~83~~ ~~82~~ ~~81~~ ~~80~~ ~~79~~ ~~77~~ ~~75~~ **73** |"),
    (INF, "9.10 100.1 fila C",
     "| **C** | ~~7~~ ~~8~~ **7** |",
     "| **C** | ~~7~~ ~~8~~ ~~7~~ **6** |"),
    (INF, "9.10 100.1 fila D",
     "~~2.732~~ ~~2.737 (80,8 %)~~ **2.743** (81,0 %) |",
     "~~2.732~~ ~~2.737 (80,8 %)~~ ~~2.743 (81,0 %)~~ **2.758** (81,4 %) |"),

    # ---------------- INFORME, la 100.2, las cuatro filas que se mueven ----
    (INF, "9.10 100.2 fila core",
     "| core | 1.445 | ~~344~~ ~~343~~ ~~342~~ ~~337~~ ~~336~~ **329** | ~~23,8 %~~ ~~23,7 %~~ ~~23,3 %~~ **22,8 %** |",
     "| core | 1.445 | ~~344~~ ~~343~~ ~~342~~ ~~337~~ ~~336~~ ~~329~~ **325** | ~~23,8 %~~ ~~23,7 %~~ ~~23,3 %~~ ~~22,8 %~~ **22,5 %** |"),
    (INF, "9.10 100.2 fila quality",
     "| quality | 844 | ~~126~~ **123** | ~~14,9 %~~ **14,6 %** (CERRADO) |",
     "| quality | 844 | ~~126~~ ~~123~~ **119** | ~~14,9 %~~ ~~14,6 %~~ **14,1 %** (CERRADO) |"),
    (INF, "9.10 100.2 fila environmental",
     "| quality | 844 | ~~126~~ ~~123~~ **119** | ~~14,9 %~~ ~~14,6 %~~ **14,1 %** (CERRADO) |\n"
     "| environmental | 170 | 29 | 17,1 % |\n| franquicias | 148 | 18 | 12,2 % |",
     "| quality | 844 | ~~126~~ ~~123~~ **119** | ~~14,9 %~~ ~~14,6 %~~ **14,1 %** (CERRADO) |\n"
     "| environmental | 170 | ~~29~~ **28** | ~~17,1 %~~ **16,5 %** |\n"
     "| franquicias | 148 | ~~18~~ **15** | ~~12,2 %~~ **10,1 %** |"),
    (INF, "9.10 100.2 nota adosada",
     "por el motivo que la correccion de la vuelta 36 ya escribio: cada una es la foto de su propio corte.\n",
     "por el motivo que la correccion de la vuelta 36 ya escribio: cada una es la foto de su propio corte.\n"
     "\n"
     "> **QUINTA CORRECCION DECLARADA (20 ago 2026, vuelta 53, barrido `9.10` DEL CIERRE, corrido "
     "DESPUES del ultimo movimiento de la vuelta), Y ES LA PRIMERA QUE SE HACE EN EL MISMO ACTO QUE "
     "SU TABLA HERMANA.** " + QUE_MOVIO.capitalize() + ". **CUATRO FILAS SE MUEVEN Y SEIS NO**: "
     "`core` de 329 a **325**, `quality` de 123 a **119**, `environmental` de 29 a **28** y "
     "`franquicias` de 18 a **15**, que es el dominio que mas se mueve porque TRES de los doce "
     "actos fundidos son suyos. **Quedan identicos al digito** `health_safety` 43, `exportacion` "
     "15, `entrega` 2, `compras` 1, `risk_management` 0 y `seguridad_digital` 3. Todo " + MEDIDO_INF +
     ". **LA SUMA DE LA COLUMNA CUADRA CON EL MARCADOR**, comprobado hoy: 325 mas 119 mas 43 mas 2 "
     "mas 28 mas 1 mas 15 mas 0 mas 15 mas 3 son **551**, que es la `A` global de la misma corrida. "
     "**Y LA TABLA HERMANA DE `docs/plan/RECOMPUTO_3388.md` SE MOVIO EN ESTE MISMO ACTO, que es "
     "para lo que la hermandad se escribio en la TAREA 1.1 de esta vuelta.** Las cuatro "
     "correcciones de arriba no se reescriben.\n"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("LAS CORRECCIONES DEL BARRIDO 9.10 DEL CIERRE DE LA VUELTA 53")
    print("modo: %s" % ("SIMULACION, no escribe" if a.simular else "ESCRITURA"))
    print("=" * 78)
    print()

    textos = {}
    hechas = saltadas = 0
    for ruta, etiqueta, viejo, nuevo in CAMBIOS:
        if ruta not in textos:
            textos[ruta] = io.open(ruta, encoding="utf-8").read()
        t = textos[ruta]
        if nuevo in t:
            print("  YA ESTABA   %-44s (idempotente)" % etiqueta)
            saltadas += 1
            continue
        c = t.count(viejo)
        if c != 1:
            print("  ROJO        %-44s el texto viejo aparece %d veces" % (etiqueta, c))
            return 1
        textos[ruta] = t.replace(viejo, nuevo, 1)
        print("  HECHA       %-44s %s" % (etiqueta, os.path.basename(ruta)))
        hechas += 1

    if not a.simular:
        for ruta, t in textos.items():
            io.open(ruta, "w", encoding="utf-8", newline="\n").write(t)

    print()
    print("  sustituciones HECHAS: %d | ya estaban: %d" % (hechas, saltadas))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
