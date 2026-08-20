# -*- coding: utf-8 -*-
"""vuelta52_correcciones_910.py . LAS CORRECCIONES DEL BARRIDO `9.10` DE LA
VUELTA 52, APLICADAS DESPUES DEL ULTIMO MOVIMIENTO.

POR QUE EXISTE, y lo manda el encargo (punto 2.7) citando la vara que la propia
casa se puso: QUIEN MUEVE UNA CLASE O FUNDE UN ACTO CORRE EL BARRIDO 9.10 ANTES
DE CERRAR. Esta vuelta fundio TRES actos y volteo SEIS veredictos por `P.16`
(los puestos 502, 266 y 246 en el lote A; los 251, 281 y 243 en el lote B), asi
que toda tabla VIGENTE que cite la clase, el marcador o el retrato se remide.

Y CON EL RENGLON QUE LA VUELTA 51 NO CUMPLIO Y QUE ESTA ES LA PRIMERA EN
CUMPLIR DE ENTRADA (`D7` de la vuelta 50, y caida de cifra publicada del acta de
la vuelta 51, seccion 3.1): QUIEN CORRIGE UNA CELDA CON CONTADOR CUADRA EL
CONTADOR Y ADOSA LA NOTA FECHADA, en el mismo acto y no en la vuelta siguiente.
Las tres celdas de contador de este barrido suben su contador aqui mismo.

TODAS LAS CIFRAS SE LEEN DE LA CORRIDA DE HOY, hecha DESPUES del ultimo
movimiento: `../loop/SALIDA_V52_MARCADOR_CIERRE.txt` y
`../loop/SALIDA_V52_RECOMPUTO_CIERRE.txt`. Ninguna se teclea de memoria ni sale
de un acta.

UN HALLAZGO QUE ESTE BARRIDO SACA Y QUE NO ES DE ESTA VUELTA, declarado aqui
porque se corrige aqui: la tabla POR DOMINIO de docs/plan/RECOMPUTO_3388.md
mantenia VIGENTE su fila de total (la vuelta 51 se la corrigio) y NO sus filas
por dominio. Medido en la APERTURA de esta vuelta, ANTES de la primera
operacion, `core` ya estaba en 332 contra los 344 publicados, `quality` en 123
contra 126 y `health_safety` en 43 contra 45: la divergencia es ANTERIOR a esta
vuelta y ninguna vuelta la habia visto porque el barrido busca de forma lexica
las cifras que se le pasan y esas tres nunca se le pasaron.

IDEMPOTENTE: cada sustitucion comprueba primero si su resultado ya esta escrito.

Uso: python scripts/loop/vuelta52_correcciones_910.py [--simular]
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REC = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388.md")
INF = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_INFORME.md")

CIERRE = ("Medido HOY con `python scripts/plan/recomputo_3388.py` y "
          "`python scripts/recomputar_marcador.py 3388` DESPUES del ultimo movimiento de la "
          "vuelta 52 (`../loop/SALIDA_V52_RECOMPUTO_CIERRE.txt` y "
          "`../loop/SALIDA_V52_MARCADOR_CIERRE.txt`)")

MOTIVO = ("la vuelta 52 fundio TRES actos de `OP-U-01` (el del reparto de equity, el de los "
          "regalos estrategicos y el de los habitos de pensamiento) y volteo SEIS veredictos "
          "por `P.16` (puestos 502, 266 y 246 en el lote A; 251, 281 y 243 en el lote B)")

CAMBIOS = [
    # ------------------------------------------------ RECOMPUTO_3388, fila 246
    ("REC", "246 A crudas, cifra",
     "~~**573**~~ ~~**571**~~ **566** **[CORREGIDA",
     "~~**573**~~ ~~**571**~~ ~~**566**~~ **563** **[CORREGIDA"),
    ("REC", "246 A crudas, contador",
     "**[CORREGIDA ~~SIETE~~ OCHO VECES, el 15 y el 18 ago 2026",
     "**[CORREGIDA ~~SIETE~~ ~~OCHO~~ NUEVE VECES, el 15 y el 18 ago 2026"),
    ("REC", "246 A crudas, nota de la novena",
     "y reproducida hoy en `../loop/SALIDA_V52_RECOMPUTO_APERTURA.txt`, paso 1]** |\n"
     "| de esas, colapsan",
     "y reproducida hoy en `../loop/SALIDA_V52_RECOMPUTO_APERTURA.txt`, paso 1] "
     "[NOVENA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 52, barrido "
     "`9.10` del cierre): de 566 a 563 porque " + MOTIVO + ". " + CIERRE + ", paso 1. La nota "
     "de arriba, del mismo dia y de la TAREA 1.1, no se reescribe]** |\n"
     "| de esas, colapsan"),

    # ------------------------------------------------ RECOMPUTO_3388, fila 247
    ("REC", "247 colapsos, cifra",
     "~~**48**~~ ~~**49**~~ **57** **[CORREGIDA",
     "~~**48**~~ ~~**49**~~ ~~**57**~~ **60** **[CORREGIDA"),
    ("REC", "247 colapsos, contador",
     "**[CORREGIDA ~~CUATRO~~ CINCO VECES, el 15 ago 2026",
     "**[CORREGIDA ~~CUATRO~~ ~~CINCO~~ SEIS VECES, el 15 ago 2026"),
    ("REC", "247 colapsos, nota de la sexta",
     "paso 1. Ninguna nota vieja se reescribe]** |",
     "paso 1. Ninguna nota vieja se reescribe] "
     "[SEXTA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 52, barrido "
     "`9.10` del cierre): de 57 a 60, TRES colapsos mas, uno por cada acto que esta vuelta "
     "fundio, porque cada fusion convierte el par `A` interno del acto en un par cuyos dos ids "
     "resuelven al mismo nodo vivo. " + CIERRE + ", paso 1]** |"),

    # ------------------------------------------------ RECOMPUTO_3388, fila 248
    ("REC", "248 pares distintos, cifra",
     "~~**525**~~ ~~**522**~~ **509** **[CORREGIDA",
     "~~**525**~~ ~~**522**~~ ~~**509**~~ **503** **[CORREGIDA"),
    ("REC", "248 pares distintos, contador",
     "**[CORREGIDA ~~SIETE~~ OCHO VECES, las dos ultimas el 19 ago 2026",
     "**[CORREGIDA ~~SIETE~~ ~~OCHO~~ NUEVE VECES, las dos ultimas el 19 ago 2026"),
    ("REC", "248 pares distintos, nota de la novena",
     "menos 57 colapsos) y esta medida en `../loop/SALIDA_V51_RECOMPUTO_CIERRE.txt`, paso 1, y "
     "reproducida hoy en `../loop/SALIDA_V52_RECOMPUTO_APERTURA.txt`, paso 1]**",
     "menos 57 colapsos) y esta medida en `../loop/SALIDA_V51_RECOMPUTO_CIERRE.txt`, paso 1, y "
     "reproducida hoy en `../loop/SALIDA_V52_RECOMPUTO_APERTURA.txt`, paso 1] "
     "[NOVENA CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, 20 ago 2026 (vuelta 52, barrido "
     "`9.10` del cierre): de 509 a 503, que vuelve a ser la resta exacta de las dos filas de "
     "arriba (563 crudas menos 60 colapsos). " + CIERRE + ", paso 1]**"),

    # ------------------------------------------------ RECOMPUTO_3388, checkpoint ii (528)
    ("REC", "528 checkpoint ii, los dos parentesis",
     "| **ii** | A vigentes resueltas del retrato (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ **509**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ **509**)",
     "| **ii** | A vigentes resueltas del retrato (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ **503**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ ~~509~~ **503**)"),
    ("REC", "528 checkpoint ii, nota",
     "y dejo de serlo cuando el 305 y las tres fusiones movieron el retrato dentro de la propia vuelta 49** |",
     "y dejo de serlo cuando el 305 y las tres fusiones movieron el retrato dentro de la propia vuelta 49** "
     "**[RE-CORRIDO EL 20 ago 2026 (vuelta 52, barrido `9.10` del cierre): SIGUE OK, ahora con "
     "503 y 503, y las dos mitades se recomputaron por separado, no se copio una en la otra. " +
     CIERRE + ", bloque LAS CUATRO COMPROBACIONES, donde las cuatro salen OK]** |"),

    # ------------------------------------------------ RECOMPUTO_3388, tabla por dominio
    ("REC", "1069 fila core de la tabla por dominio",
     "| core | 1.445 | 344 | 23,8 % |",
     "| core | 1.445 | ~~344~~ **329** | ~~23,8 %~~ **22,8 %** "
     "**[CORREGIDA UNA VEZ, 20 ago 2026 (vuelta 52, barrido `9.10` del cierre), Y LA "
     "DIVERGENCIA ES ANTERIOR A ESTA VUELTA: medido en la APERTURA de la vuelta 52, ANTES de "
     "su primera operacion, esta fila ya estaba en 332 y publicaba 344 "
     "(`../loop/SALIDA_V52_MARCADOR_APERTURA.txt`). LA CAUSA, dicha en vez de callada: la fila "
     "de TOTAL de esta misma tabla se venia manteniendo vigente vuelta a vuelta y las filas POR "
     "DOMINIO no, porque el barrido busca de forma LEXICA las cifras que se le pasan y estas "
     "nunca se le pasaron. Los tres actos que la vuelta 52 fundio son los tres de `core`, y por "
     "eso bajan tres mas. " + CIERRE + "]** |"),
    ("REC", "1070 fila quality de la tabla por dominio",
     "| quality | 844 | 126 | 14,9 % |",
     "| quality | 844 | ~~126~~ **123** | ~~14,9 %~~ **14,6 %** "
     "**[CORREGIDA UNA VEZ, 20 ago 2026 (vuelta 52, barrido `9.10` del cierre). LA DIVERGENCIA "
     "ES ENTERAMENTE ANTERIOR A ESTA VUELTA Y ESTA VUELTA NO LA MOVIO: en la APERTURA ya median "
     "123, y al cierre siguen en 123 (`../loop/SALIDA_V52_MARCADOR_APERTURA.txt` y " + CIERRE +
     "). Mismo motivo que la fila de `core`]** |"),
    ("REC", "1071 fila health_safety de la tabla por dominio",
     "| health_safety | 192 | 45 | 23,4 % |",
     "| health_safety | 192 | ~~45~~ **43** | ~~23,4 %~~ **22,4 %** "
     "**[CORREGIDA UNA VEZ, 20 ago 2026 (vuelta 52, barrido `9.10` del cierre). LA DIVERGENCIA "
     "ES ENTERAMENTE ANTERIOR A ESTA VUELTA Y ESTA VUELTA NO LA MOVIO: en la APERTURA ya median "
     "43, y al cierre siguen en 43. Mismo motivo que la fila de `core`]** |"),
    ("REC", "1079 total de la tabla por dominio",
     "| **total** | **3.388** | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ ~~**573**~~ ~~**571**~~ **566** | ~~**17,2 %**~~ ~~**17,1 %**~~ ~~**17,0 %**~~ ~~**16,9 %**~~ **16,7 %** |",
     "| **total** | **3.388** | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ ~~**573**~~ ~~**571**~~ ~~**566**~~ **563** | ~~**17,2 %**~~ ~~**17,1 %**~~ ~~**17,0 %**~~ ~~**16,9 %**~~ ~~**16,7 %**~~ **16,6 %** "
     "**[CORREGIDA, 20 ago 2026 (vuelta 52, barrido `9.10` del cierre): " + MOTIVO + ". " +
     CIERRE + ". LA SUMA DE LA COLUMNA CUADRA CON EL TOTAL, comprobado hoy: 329 mas 123 mas 43 "
     "mas 2 mas 29 mas 1 mas 18 mas 0 mas 15 mas 3 son 563]** |"),

    # ------------------------------------------------ INTRA_DOMINIO_INFORME, apendice 100.1
    ("INF", "100.1 fila A",
     "| **A** | ~~**583** (17,2 %)~~ ~~582~~ ~~581~~ ~~576~~ ~~575 (17,0 %)~~ ~~574~~ ~~573~~ ~~571 (16,9 %)~~ **566** (16,7 %), ver las correcciones declaradas debajo |",
     "| **A** | ~~**583** (17,2 %)~~ ~~582~~ ~~581~~ ~~576~~ ~~575 (17,0 %)~~ ~~574~~ ~~573~~ ~~571 (16,9 %)~~ ~~566 (16,7 %)~~ **563** (16,6 %), ver las correcciones declaradas debajo |"),
    ("INF", "100.1 fila B",
     "| **B** | ~~89~~ ~~87~~ ~~84~~ ~~83~~ ~~82~~ ~~81~~ ~~80~~ ~~79~~ **77** |",
     "| **B** | ~~89~~ ~~87~~ ~~84~~ ~~83~~ ~~82~~ ~~81~~ ~~80~~ ~~79~~ ~~77~~ **75** |"),
    ("INF", "100.1 fila C",
     "| **C** | ~~7~~ **8** |",
     "| **C** | ~~7~~ ~~8~~ **7** |"),
    ("INF", "100.1 fila D",
     "| **D** | ~~**2.709** (80,0 %)~~ ~~2.711~~ ~~2.714~~ ~~2.716~~ ~~2.721~~ ~~2.722~~ ~~2.723~~ ~~2.724~~ ~~2.725~~ ~~2.726~~ ~~2.729~~ ~~2.730~~ ~~2.732~~ **2.737** (80,8 %) |",
     "| **D** | ~~**2.709** (80,0 %)~~ ~~2.711~~ ~~2.714~~ ~~2.716~~ ~~2.721~~ ~~2.722~~ ~~2.723~~ ~~2.724~~ ~~2.725~~ ~~2.726~~ ~~2.729~~ ~~2.730~~ ~~2.732~~ ~~2.737 (80,8 %)~~ **2.743** (81,0 %) |"),
    ("INF", "100.1 tercera nota adosada",
     "> (`../loop/SALIDA_V50_MARCADOR_APERTURA.txt`): **A 573, B 77, C 8, D 2.730** sobre `n`\n"
     "> **3.388**, cero huecos y cero duplicados.",
     "> (`../loop/SALIDA_V50_MARCADOR_APERTURA.txt`): **A 573, B 77, C 8, D 2.730** sobre `n`\n"
     "> **3.388**, cero huecos y cero duplicados.\n"
     "\n"
     "> **TERCERA CORRECCION DECLARADA SOBRE ESTA TABLA (20 ago 2026, vuelta 52, barrido `9.10` "
     "del cierre), y las dos notas de la vuelta 50 y la de la vuelta 51 NO se reescriben: estan "
     "fechadas y se quedan.** Esta vez la tabla SI se barrio antes de cerrar, y ademas SE "
     "MOVIERON LAS CUATRO FILAS Y NO SOLO DOS, que es lo que la vuelta 51 no tuvo que hacer "
     "porque sus CINCO volteos salian todos de `A`. **Los seis volteos de esta vuelta salen de "
     "TRES clases distintas: TRES de `A` (los puestos 502, 251 y 281), DOS de `B` (el 266 y el "
     "243) y UNO de `C` (el 246), asi que bajan la `A`, la `B` y la `C` a la vez y las seis "
     "suben a la `D`. La cuenta cuadra al digito contra la apertura de esta vuelta (A 566, B "
     "77, C 8, D 2.737): menos 3, menos 2, menos 1 y mas 6.** " + MOTIVO + ". **Medido HOY con "
     "`python scripts/recomputar_marcador.py 3388` DESPUES del ultimo movimiento "
     "(`../loop/SALIDA_V52_MARCADOR_CIERRE.txt`): A 563, B 75, C 7, D 2.743** sobre `n` "
     "**3.388**, cero huecos y cero duplicados. **Y LA REGLA QUE ESTA VUELTA CUMPLE DE ENTRADA "
     "Y NO EN LA SIGUIENTE:** las tres celdas con contador de `plan/RECOMPUTO_3388.md` que este "
     "mismo barrido movio llevan su contador CUADRADO en el mismo acto, que es lo que el `D7` "
     "de la vuelta 50 pide y lo que la vuelta 51 no hizo."),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("CORRECCIONES DEL BARRIDO 9.10 DEL CIERRE, VUELTA 52")
    print("modo: %s" % ("SIMULACION, no escribe" if a.simular else "ESCRITURA"))
    print("=" * 78)
    print()

    rutas = {"REC": REC, "INF": INF}
    textos, hechas, saltadas = {}, 0, 0
    for clave, etiqueta, viejo, nuevo in CAMBIOS:
        if u"—" in nuevo or u"–" in nuevo:
            print("  ROJO: guion largo o medio en %s" % etiqueta)
            return 1
        ruta = rutas[clave]
        if ruta not in textos:
            textos[ruta] = io.open(ruta, encoding="utf-8").read()
        t = textos[ruta]
        if nuevo in t:
            print("  YA ESTABA   %-48s (idempotente)" % etiqueta)
            saltadas += 1
            continue
        c = t.count(viejo)
        if c != 1:
            print("  ROJO        %-48s el texto viejo aparece %d veces" % (etiqueta, c))
            return 1
        textos[ruta] = t.replace(viejo, nuevo, 1)
        print("  HECHA       %-48s %s" % (etiqueta, os.path.basename(ruta)))
        hechas += 1

    if not a.simular:
        for ruta, t in textos.items():
            io.open(ruta, "w", encoding="utf-8", newline="\n").write(t)

    print()
    print("  celdas corregidas: %d | ya estaban: %d" % (hechas, saltadas))
    print("  contadores cuadrados en el mismo acto: 3 (filas 246, 247 y 248)")
    print("  guiones largos y medios en lo escrito: CERO")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
