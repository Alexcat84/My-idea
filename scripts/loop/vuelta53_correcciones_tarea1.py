# -*- coding: utf-8 -*-
"""vuelta53_correcciones_tarea1.py . LAS CORRECCIONES Y REGISTROS ADJUDICADOS
DE LA TAREA 1 DE LA VUELTA 53, CADA UNO TRATADO POR SU ESPECIE.

POR QUE EXISTE COMO INSTRUMENTO Y NO COMO EDICION A MANO: la regla 1 del
EJECUTOR (cuarto renglon, LA TABLA SE IMPRIME, NO SE TECLEA) nacio de las dos
paradas de credito de las vueltas 31 y 32, las dos por celdas manuales que
ningun instrumento validaba. Una sustitucion escrita aqui se puede RE-CORRER y
se puede DIFF-EAR; una celda tecleada, no.

LAS CUATRO ESPECIES DE ESTA VUELTA:

  1.1 TABLA VIGENTE MANTENIDA A MEDIAS. La 100.2 de docs/INTRA_DOMINIO_INFORME.md
      (TASA POR DOMINIO, corte 3.388) es TABLA VIGENTE hermana de la 100.1 (acta
      de la vuelta 52, seccion 3.1) y tres de sus diez filas quedaron atras:
      core publica 336 y midio por ultima vez en la era de la vuelta 36, quality
      publica 126 y health_safety 45, las dos sin tocar desde sus volteos. Se
      corrigen LAS TRES con tachado y nota fechada, con las cifras de la corrida
      del dia, y la nota DECLARA LA HERMANDAD con la tabla por dominio de
      docs/plan/RECOMPUTO_3388.md: quien corrija una, corrige la otra en el
      mismo acto. LA HERMANDAD SE ESCRIBE EN LAS DOS SEDES y no solo en una,
      porque una hermandad escrita en un solo lado no la ve quien entra por el
      otro.

  1.2 FOTO FECHADA QUE NO PUBLICA LA CIFRA DE SU CORRIDA. Las dos tablas de los
      registros de las vueltas 19 y 20 en docs/plan/RECOMPUTO_3388.md dejaban
      visible el 575/83/8/2.722, que no es de ninguna corrida: es el ultimo
      eslabon de un MANTENIMIENTO POR RESTA que se le aplico a una foto como si
      fuera tabla vigente. La cifra de su corrida es 583/89/7/2.709, verificada
      por git DOS veces (el instrumento de la vuelta 52 y el conteo propio del
      auditor) y RE-VERIFICADA HOY con scripts/loop/vuelta53_marcador_por_git.py
      sobre los once commits del cierre de la 19 al de la 21. Queda VISIBLE el
      583 y TACHADAS las cuatro cifras del mantenimiento muerto. Nada se borra.
      Los porcentajes de la tabla de la vuelta 20 son los del 575 y siguen a su
      cifra: se tachan con ella y se publican los del 583, leidos de la salida
      del instrumento y no tecleados.

  1.3 ROTULO QUE REPITE EL SINTOMA EN VEZ DE DECIR LA VARA. En
      scripts/loop/vuelta48_puertas_en_el_lote.py el caso c del docstring y el
      parentesis del resumen dicen "mas de una puerta" mientras el propio
      listado imprime "puertas (1)" debajo. La vara implementada esta BIEN
      (candidato limpio); la letra del sintoma nace del encargo 1.5 de la vuelta
      52 y su autor la declara suya (acta 52, seccion 3.2). Se corrigen los dos
      rotulos con el texto viejo delante.

  1.4 REGISTROS DE ADJUDICACIONES, para que el registro no dependa del acta.
      Tres carriles adjudicados en el acta de la vuelta 52 se escriben en el
      registro del tramo de docs/plan/03_FUSIONES.md: el acto de la sucesion del
      CEO declarado POR EMPATE SIN VARA, el carril GENERAL de colisiones, y el
      criterio del mixto contenido.

IDEMPOTENTE: cada sustitucion comprueba primero si su resultado ya esta escrito,
y entonces no hace nada y lo dice. Re-correrlo no duplica ninguna nota.

Uso: python scripts/loop/vuelta53_correcciones_tarea1.py [--simular]
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REC = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388.md")
FUS = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
INF = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_INFORME.md")
PUE = os.path.join(RAIZ, "scripts", "loop", "vuelta48_puertas_en_el_lote.py")

# --------------------------------------------------------------------------
# LA NOTA DE LA HERMANDAD, escrita una sola vez y pegada en las DOS sedes.
# --------------------------------------------------------------------------
HERMANDAD = (
    "**LAS DOS TABLAS POR DOMINIO SON HERMANAS Y SE MUEVEN JUNTAS, y esto queda escrito en "
    "las DOS sedes para que no dependa de ningun acta:** la **100.2** de "
    "`docs/INTRA_DOMINIO_INFORME.md` y la **tabla por dominio de la seccion `a`** de "
    "`docs/plan/RECOMPUTO_3388.md` miden LO MISMO (los diez dominios al corte 3.388, que es el "
    "catalogo entero y no una fecha) y las dos se presentan como el estado VIGENTE del archivo. "
    "**QUIEN CORRIJA UNA, CORRIGE LA OTRA EN EL MISMO ACTO.**"
)

CAMBIOS = [
    # ================= 1.1, las tres filas de la 100.2 =================
    # LAS TRES FILAS VAN EN UNA SOLA SUSTITUCION, en bloque, y no una a una.
    # EL MOTIVO, medido y no supuesto: la fila de health_safety de la 100.2 es
    # LITERALMENTE IDENTICA a la de la 99.2 (checkpoint corte 3.300, linea
    # 16158), que es una FOTO FECHADA y NO se toca. Una sustitucion suelta
    # sobre esa cadena aparece DOS veces y el instrumento cae en rojo, que es
    # lo que tiene que hacer. El bloque de las tres filas seguidas es unico.
    (INF, "1.1 las tres filas de la 100.2, en bloque",
     "| core | 1.445 | ~~344~~ ~~343~~ ~~342~~ ~~337~~ **336** | ~~23,8 %~~ ~~23,7 %~~ **23,3 %** |\n"
     "| health_safety | 192 | 45 | 23,4 % |\n"
     "| quality | 844 | 126 | 14,9 % (CERRADO) |",
     "| core | 1.445 | ~~344~~ ~~343~~ ~~342~~ ~~337~~ ~~336~~ **329** | ~~23,8 %~~ ~~23,7 %~~ ~~23,3 %~~ **22,8 %** |\n"
     "| health_safety | 192 | ~~45~~ **43** | ~~23,4 %~~ **22,4 %** |\n"
     "| quality | 844 | ~~126~~ **123** | ~~14,9 %~~ **14,6 %** (CERRADO) |"),
    (INF, "1.1 nota adosada al final de la 100.2",
     "> se presenta como el estado VIGENTE del archivo**, y esas son las dos de la seccion 100.\n"
     "\n"
     "### 100.3",
     "> se presenta como el estado VIGENTE del archivo**, y esas son las dos de la seccion 100.\n"
     "\n"
     "> **CUARTA CORRECCION DECLARADA (20 ago 2026, vuelta 53, TAREA 1.1 del encargo, que la manda "
     "citando la adjudicacion del acta de la vuelta 52, seccion 3.1). ESTA VEZ SE MUEVEN TRES "
     "FILAS Y NO UNA, Y LA DIVERGENCIA ES ANTERIOR A ESTA VUELTA.** El auditor la levanto midiendo: "
     "esta tabla se venia manteniendo A MEDIAS como vigente. **La fila de `core` tenia cadena de "
     "tachados** (344, 343, 342, 337) con **336** visible y **su ultimo mantenimiento es de la era "
     "de la vuelta 36**; **`quality` publicaba 126 y `health_safety` 45**, las dos **sin tocar "
     "desde sus volteos**. **NINGUNA VUELTA LA HABIA VISTO, y el motivo se dice en vez de "
     "callarse: el barrido `9.10` busca de forma LEXICA las cifras que se le pasan, y 336, 126 y "
     "45 nunca se le pasaron.** Es la misma especie que el `D7` de la vuelta 52 corrigio en la "
     "tabla hermana del `RECOMPUTO`, pero en esta casa.\n"
     ">\n"
     "> **LAS TRES CIFRAS NUEVAS SON DE LA CORRIDA DEL DIA**, no de un acta ni de un reporte: "
     "`python scripts/recomputar_marcador.py 3388` "
     "([`loop/SALIDA_V53_MARCADOR_APERTURA.txt`](loop/SALIDA_V53_MARCADOR_APERTURA.txt), bloque "
     "*TASA POR DOMINIO*), corrida el 20 ago 2026 ANTES de la primera operacion de la vuelta 53. "
     "Mide **`core` 329 (22,8 %)**, **`quality` 123 (14,6 %)** y **`health_safety` 43 (22,4 %)**. "
     "**LOS OTROS SIETE DOMINIOS DE LA TABLA MIDEN EXACTOS HOY Y NO SE TOCAN**, comprobado en la "
     "misma salida: `entrega` 2, `environmental` 29, `franquicias` 18, `exportacion` 15, `compras` "
     "1, `risk_management` 0 y `seguridad_digital` 3. **LA SUMA DE LA COLUMNA CUADRA CON EL "
     "MARCADOR**, comprobado hoy: 329 mas 123 mas 43 mas 2 mas 29 mas 1 mas 18 mas 0 mas 15 mas 3 "
     "son **563**, que es la `A` global de la misma corrida. **La columna `n` no se mueve** y su "
     "suma sigue siendo 3.388: lo que cambio es el reparto, no el censo.\n"
     ">\n"
     "> " + HERMANDAD + " La tabla hermana se corrigio el 20 ago 2026 en la vuelta 52 y hoy mide "
     "lo mismo que esta al digito; **desde hoy las dos llevan escrita la hermandad**, que es lo "
     "que el encargo manda para que un barrido futuro no vuelva a mover una sola.\n"
     ">\n"
     "> **NADA SE BORRA Y NINGUNA NOTA VIEJA SE REESCRIBE:** las tres correcciones de arriba "
     "(vueltas 33, 34 y 36) siguen enteras con su fecha, y las TRECE filas de checkpoints "
     "anteriores que citan `core` con `A 344` **siguen sin tocarse**, por el motivo que la "
     "correccion de la vuelta 36 ya escribio: cada una es la foto de su propio corte.\n"
     "\n"
     "### 100.3"),

    # ================= 1.1, la hermandad en la sede del RECOMPUTO =================
    (REC, "1.1 hermandad adosada a la tabla del RECOMPUTO",
     "~~**Los diez dominios y el total (3.388 pares, 583 A) coinciden con el marcador recomputado de la vuelta\n"
     "14**",
     "> **HERMANDAD DECLARADA (20 ago 2026, vuelta 53, TAREA 1.1 del encargo; adjudicacion del acta de la "
     "vuelta 52, seccion 3.1).** " + HERMANDAD + " **La 100.2 quedo atras en TRES filas** (`core` 336, "
     "`quality` 126, `health_safety` 45) **porque esta hermandad no estaba escrita en ninguna de las dos "
     "sedes**, y por eso la vuelta 52 movio esta tabla sola. **Las tres filas de la 100.2 se corrigieron el "
     "20 ago 2026 (vuelta 53) a 329, 123 y 43**, que es lo que mide esta tabla, y las dos publican hoy la "
     "misma corrida: `python scripts/recomputar_marcador.py 3388` "
     "([`../loop/SALIDA_V53_MARCADOR_APERTURA.txt`](../loop/SALIDA_V53_MARCADOR_APERTURA.txt)), corrida "
     "ANTES de la primera operacion de la vuelta 53.\n"
     "\n"
     "~~**Los diez dominios y el total (3.388 pares, 583 A) coinciden con el marcador recomputado de la vuelta\n"
     "14**"),

    # ================= 1.2, el 583 visible en las dos fotos =================
    (REC, "1.2 foto de la vuelta 19, el 583 visible",
     "| **A / B / C / D** | ~~**583 / 89 / 7 / 2.709**~~ ~~**582 / 87 / 8 / 2.711**~~ ~~**581 / 83 / 8 / 2.716**~~ ~~**576 / 83 / 8 / 2.721**~~ **575 / 83 / 8 / 2.722** **[CORREGIDA VARIAS VECES, el 15 y el 18 ago 2026, ver las correcciones declaradas al principio del documento]** |",
     "| **A / B / C / D** | **583 / 89 / 7 / 2.709** ~~**582 / 87 / 8 / 2.711**~~ ~~**581 / 83 / 8 / 2.716**~~ ~~**576 / 83 / 8 / 2.721**~~ ~~**575 / 83 / 8 / 2.722**~~ **[CORREGIDA VARIAS VECES, el 15 y el 18 ago 2026, ver las correcciones declaradas al principio del documento]** **[EL 583 RESTITUIDO A LA VISTA Y EL MANTENIMIENTO MUERTO TACHADO, 20 ago 2026 (vuelta 53, TAREA 1.2 del encargo; adjudicacion del acta de la vuelta 52, pregunta 7). UNA FOTO FECHADA PUBLICA LA CIFRA DE SU CORRIDA, y la de esta es `A 583, B 89, C 7, D 2.709`, RE-VERIFICADA POR GIT HOY sobre los ONCE commits que van del cierre de la vuelta 19 al de la 21 (`python scripts/loop/vuelta53_marcador_por_git.py`, [`../loop/SALIDA_V53_MARCADOR_POR_GIT.txt`](../loop/SALIDA_V53_MARCADOR_POR_GIT.txt): los once miden lo mismo al digito). LAS CUATRO CIFRAS TACHADAS (582, 581, 576 y 575) NO ERAN CORRECCIONES: ERAN MANTENIMIENTO DE FOTO POR RESTA, restados de la cifra anterior en vez de re-medidos, y por eso la `B` y la `C` se congelaron mientras la `A` y la `D` bajaban. El 575 que quedaba visible no es de ninguna corrida. NADA SE BORRA: la cadena entera se queda como registro de lo que paso. LA CADENA TERMINA AQUI: esta celda no publica el marcador vigente, que vive en las filas del paso 1 y de la tabla por dominio de este documento y en el apendice 100.1 de `../INTRA_DOMINIO_INFORME.md`]** |"),

    (REC, "1.2 foto de la vuelta 20, el 583 visible y sus porcentajes",
     "| **A / B / C / D** | ~~**583 / 89 / 7 / 2.709**~~ ~~**582 / 87 / 8 / 2.711**~~ ~~**581 / 83 / 8 / 2.716**~~ ~~**576 / 83 / 8 / 2.721**~~ **575 / 83 / 8 / 2.722** (17,0 / 2,4 / 0,2 / 80,3 por ciento) **[CORREGIDA VARIAS VECES, el 15 y el 18 ago 2026, ver las correcciones declaradas al principio del documento]** |",
     "| **A / B / C / D** | **583 / 89 / 7 / 2.709** (**17,2 / 2,6 / 0,2 / 80,0** por ciento) ~~**582 / 87 / 8 / 2.711**~~ ~~**581 / 83 / 8 / 2.716**~~ ~~**576 / 83 / 8 / 2.721**~~ ~~**575 / 83 / 8 / 2.722** (17,0 / 2,4 / 0,2 / 80,3 por ciento)~~ **[CORREGIDA VARIAS VECES, el 15 y el 18 ago 2026, ver las correcciones declaradas al principio del documento]** **[EL 583 RESTITUIDO A LA VISTA Y EL MANTENIMIENTO MUERTO TACHADO, 20 ago 2026 (vuelta 53, TAREA 1.2 del encargo; adjudicacion del acta de la vuelta 52, pregunta 7). UNA FOTO FECHADA PUBLICA LA CIFRA DE SU CORRIDA, y la de esta es `A 583, B 89, C 7, D 2.709`, RE-VERIFICADA POR GIT HOY sobre los ONCE commits que van del cierre de la vuelta 19 al de la 21 (`python scripts/loop/vuelta53_marcador_por_git.py`, [`../loop/SALIDA_V53_MARCADOR_POR_GIT.txt`](../loop/SALIDA_V53_MARCADOR_POR_GIT.txt): los once miden lo mismo al digito). LOS CUATRO PORCENTAJES VIEJOS ERAN LOS DEL 575 Y SE TACHAN CON EL; LOS CUATRO NUEVOS SON LOS DEL 583 Y SE LEEN DE LA MISMA SALIDA, no se teclean: el instrumento de hoy anade las columnas de porcentaje con el redondeo de `scripts/recomputar_marcador.py` y lo declara en su cabecera. LAS CUATRO CIFRAS TACHADAS (582, 581, 576 y 575) NO ERAN CORRECCIONES: ERAN MANTENIMIENTO DE FOTO POR RESTA, restados de la cifra anterior en vez de re-medidos. NADA SE BORRA. LA CADENA TERMINA AQUI: esta celda no publica el marcador vigente]** |"),

    # ================= 1.4, los tres registros de adjudicaciones =================
    (FUS, "1.4.a nota adosada a la fila del acto de la sucesion",
     "| `founder_ceo_succession_process`, `identificacion_necesidad_sucesion_ceo`, `sucesion_iniciada_por_fundador` | **EL CONTENIDO NO ALCANZA A ELEGIR Y LA RECETA NO TIENE CARRIL PARA LO QUE LA LECTURA ENCUENTRA** | SE DECLARA POR DOS MOTIVOS Y LOS DOS SE ESCRIBEN, porque cada uno por separado ya bastaria | LA MESA y el PARA_ALEXIS del cierre |",
     "| `founder_ceo_succession_process`, `identificacion_necesidad_sucesion_ceo`, `sucesion_iniciada_por_fundador` | **EL CONTENIDO NO ALCANZA A ELEGIR Y LA RECETA NO TIENE CARRIL PARA LO QUE LA LECTURA ENCUENTRA** **[ESPECIE ADJUDICADA Y REGISTRADA, 20 ago 2026 (vuelta 53, TAREA 1.4.a): el acto queda DECLARADO POR EMPATE SIN VARA, que es el carril del encargo 2.4 de la vuelta 52; el `ENTRA` que la lectura ademas destapo es real y REFUERZA la declaracion, pero NO hace falta para sostenerla. Ver el registro entero mas abajo]** | SE DECLARA POR DOS MOTIVOS Y LOS DOS SE ESCRIBEN, porque cada uno por separado ya bastaria | LA MESA y el PARA_ALEXIS del cierre |"),

]

# --------------------------------------------------------------------------
# 1.4, EL BLOQUE DE LOS TRES REGISTROS, que se ADOSA AL FINAL del fichero y no
# se ancla en una fila de tabla. EL MOTIVO, medido: la ultima fila de la
# seccion de la vuelta 52 ("duplicadas tras resolver NUEVAS...") es LITERAL en
# los CUATRO registros de tramo que la pagina lleva, asi que como ancla cae en
# rojo, que es lo que tiene que hacer. La seccion de la vuelta 52 es hoy la
# ultima de la pagina, y ahi es donde va el bloque.
# --------------------------------------------------------------------------
COLA = [
    (FUS, "1.4 el bloque de los tres registros",
     "\n"
     "### LAS TRES ADJUDICACIONES DEL ACTA DE LA VUELTA 52, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (20 ago 2026, vuelta 53, TAREA 1.4 del encargo)\n"
     "\n"
     "**Las tres se adjudicaron DESPUES de que esta seccion quedara escrita**, y por eso se adosan al\n"
     "final de ella en vez de reescribirla. **Ninguna cifra de arriba se toca.**\n"
     "\n"
     "**a) EL ACTO DE LA SUCESION DEL CEO QUEDA DECLARADO POR EMPATE SIN VARA** (acta de la vuelta\n"
     "52, `D2` y pregunta 2; el carril es el del encargo 2.4 de aquella vuelta, cumplido al pie).\n"
     "**El contenido NO ELIGE y hay una vara para cada lado**: las condiciones apuntan a\n"
     "`identificacion_necesidad_sucesion_ceo` (2 contra 1) y el **PADRE DECLARADO** del puesto 612\n"
     "apunta a `sucesion_iniciada_por_fundador`. **El cableado EMPATA 3 contra 3.** Cuando el\n"
     "contenido no elige y el cableado tampoco, **el acto se DECLARA como empate sin vara y se\n"
     "acumula para la mesa con los demas declarados**, y eso basta por si solo. **EL `ENTRA` QUE LA\n"
     "LECTURA DESTAPO ES REAL Y VA DICHO, pero no es lo que sostiene la declaracion**: los dos\n"
     "veredictos `A` del acto (puestos **256** y **354**) declaran a los dos viables contenidos\n"
     "ENTEROS en el centro que moriria. **Y la frontera de parada queda trazada** (acta 52, pregunta\n"
     "2): si algun dia un acto NO se puede ni fundir ni declarar sin resolver un `ENTRA`, ese dia es\n"
     "PARADA por doctrina nueva. **Hoy ninguno lo necesita.**\n"
     "\n"
     "**b) EL CARRIL GENERAL DE COLISIONES DE CLASE, ADJUDICADO Y REGISTRADO** (acta de la vuelta 52,\n"
     "pregunta 4). **Piezas: acta 51 pregunta 2b, [`08_VERIFICACION.md`](08_VERIFICACION.md), `P.12`\n"
     "y `P.16`.**\n"
     "\n"
     "| la forma del par resuelto | que se hace |\n"
     "|---|---|\n"
     "| **`A` ARRASTRADO contra un DIRECTO `D`** | **VOLTEO POR MAQUINA**, citando el directo y pegando la razon vieja entera. Es la figura de la vuelta 51 y **es el UNICO caso mecanico** |\n"
     "| **un veredicto DEL FILO (`B` o `C`) en CUALQUIERA de los dos lados**, arrastrado O directo | **NADA se voltea por maquina.** El disparador de `08_VERIFICACION` ya mete el par en la cola (nodo muerto o texto cambiado): **se RELEE EN EL MISMO ACTO** con el otro veredicto como contraste, **LA RELECTURA DECIDE CUAL DE LOS DOS SE MUEVE**, y la correccion CITA esa relectura con la razon vieja entera |\n"
     "| la relectura destapa **POLITICA DE CATALOGO** | **el acto NO se funde: se DECLARA** y se acumula para la mesa |\n"
     "\n"
     "**LA FIGURA DEL CARRIL ES EL `243` DE LA VUELTA 52**, y por eso se nombra: alli el arrastrado\n"
     "era una `D` (el 563) y el directo una `B` (el 243), que es al reves de los dos carriles que\n"
     "habia escritos, **y la relectura movio el `B` DIRECTO porque sostuvo la `D` por su cuenta**.\n"
     "**El carril general dice que eso no fue una excepcion sino la regla: la LECTURA decide, no la\n"
     "direccion del arrastre.**\n"
     "\n"
     "**c) EL CRITERIO DEL MIXTO QUE QUEDA CONTENIDO TRAS LA FUSION, ADJUDICADO Y REGISTRADO** (acta\n"
     "de la vuelta 52, pregunta 1). **EL VEREDICTO DIRECTO MANDA.**\n"
     "\n"
     "| el par mixto directo | que se hace |\n"
     "|---|---|\n"
     "| **`D`** | **MANTIENE `CONTINUA`.** La aritmetica del solape que una fusion fabrica NO tumba una lectura real del archivo. **El unico carril para moverlo es una relectura declarada**: el par entra a la cola de relectura post fusion de `08_VERIFICACION` cuando el superviviente cambia de texto, y **si ESA relectura encuentra que el mixto quedo sin nada propio, lo mueve POR LECTURA con correccion declarada, nunca por aritmetica** |\n"
     "| **`B`** | **SE LEE ANTES DE FUNDIR** (acta 51, pregunta 5), y esa lectura decide su carril: si es CONDICION DE TEXTO se resuelve y el acto se funde; si es PREGUNTA DE POLITICA el acto se DECLARA |\n"
     "\n"
     "**EL CRITERIO ASIMETRICO QUEDA RATIFICADO CON ESA FORMA**, y se dice porque la vuelta 52 lo\n"
     "aplico a los dos lados en la misma tanda y lo trajo marcado: **ni el acto de los regalos (`D`,\n"
     "`CONTINUA`) ni el de la sucesion (`B`, declarado) estaban mal.**\n"),
]

# --------------------------------------------------------------------------
# 1.3, LOS DOS ROTULOS DEL INSTRUMENTO DE LAS PUERTAS.
# Van aparte porque son codigo y no prosa: el texto viejo se conserva DELANTE
# (en el docstring y en un comentario), que es como la casa trata una
# correccion sobre un instrumento.
# --------------------------------------------------------------------------
VIEJO_DOCSTRING = """FALTABA EL TERCER CASO, y es el que se anade:

  c) MAS DE UNA PUERTA, CON ALGUNA OBLIGADA A MORIR POR LA ESTRUCTURA DEL ACTO.
     No es que todos los miembros sean puerta (caso b): es que NINGUNA eleccion
     de superviviente que la receta `P.12` permita deja vivas a todas las
     puertas del acto. El acto no se funde y queda DECLARADO IMPOSIBLE POR
     PUERTA."""

NUEVO_DOCSTRING = """FALTABA EL TERCER CASO, y es el que se anade:

  c) ALGUNA PUERTA OBLIGADA A MORIR POR LA ESTRUCTURA DEL ACTO, CUALQUIERA SEA
     SU CUENTA.
     No es que todos los miembros sean puerta (caso b): es que NINGUNA eleccion
     de superviviente que la receta `P.12` permita deja vivas a todas las
     puertas del acto. El acto no se funde y queda DECLARADO IMPOSIBLE POR
     PUERTA.

     CORRECCION DE ROTULO DECLARADA, 20 ago 2026 (vuelta 53, TAREA 1.3 del
     encargo; adjudicacion del acta de la vuelta 52, pregunta 5 y seccion 3.2).
     EL TEXTO VIEJO VA DELANTE ENTERO, porque una correccion que tapa lo que
     corrige no se puede auditar. Este caso decia:

         c) MAS DE UNA PUERTA, CON ALGUNA OBLIGADA A MORIR POR LA ESTRUCTURA
            DEL ACTO.

     Y ESE ROTULO REPETIA EL SINTOMA EN VEZ DE DECIR LA VARA. La vara
     implementada abajo (un candidato es LIMPIO si ninguno de sus absorbidos es
     puerta; el acto es SALVABLE si tiene al menos un candidato limpio) NO
     CUENTA PUERTAS, y esta bien asi: la vuelta 52 encontro un tercer acto
     imposible por estructura con UNA SOLA puerta (calcular_peso_dimensional_
     antes_cotizar y hermanos), cuya unica puerta es el CENTRO de la estrella y
     por eso no puede sobrevivir. El listado imprimia "puertas (1)" justo
     debajo del rotulo que decia "mas de una". LA LETRA DEL SINTOMA NACE DEL
     ENCARGO 1.5 DE LA VUELTA 52, y su autor la declara suya en el acta 52,
     seccion 3.2: el ejecutor heredo esa letra, no la fabrico. La vara buena es
     la del acta 51, pregunta 3: un acto es IMPOSIBLE POR PUERTA cuando NINGUNA
     fusion posible respeta la guarda 1B."""

VIEJO_RESUMEN = """    print("    IMPOSIBLES POR ESTRUCTURA (mas de una puerta, alguna obligada a morir): %d"
          % len(imp_estructura))"""

NUEVO_RESUMEN = """    # CORRECCION DE ROTULO DECLARADA, 20 ago 2026 (vuelta 53, TAREA 1.3 del
    # encargo). EL TEXTO VIEJO VA DELANTE ENTERO: este parentesis decia
    # "(mas de una puerta, alguna obligada a morir)", que es el SINTOMA y no
    # la vara, y el listado de abajo imprime "puertas (1)" en uno de los tres.
    # El motivo entero esta en el caso c del docstring.
    print("    IMPOSIBLES POR ESTRUCTURA (alguna puerta obligada a morir por la"
          " estructura del acto, cualquiera sea su cuenta): %d"
          % len(imp_estructura))"""

CAMBIOS_CODIGO = [
    (PUE, "1.3 rotulo del caso c en el docstring", VIEJO_DOCSTRING, NUEVO_DOCSTRING),
    (PUE, "1.3 rotulo del parentesis del resumen", VIEJO_RESUMEN, NUEVO_RESUMEN),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("LAS CORRECCIONES Y REGISTROS DE LA TAREA 1 DE LA VUELTA 53")
    print("modo: %s" % ("SIMULACION, no escribe" if a.simular else "ESCRITURA"))
    print("=" * 78)
    print()

    textos = {}
    hechas = saltadas = 0
    for ruta, etiqueta, viejo, nuevo in CAMBIOS + CAMBIOS_CODIGO:
        if ruta not in textos:
            textos[ruta] = io.open(ruta, encoding="utf-8").read()
        t = textos[ruta]
        if nuevo in t:
            print("  YA ESTABA   %-52s (idempotente)" % etiqueta)
            saltadas += 1
            continue
        c = t.count(viejo)
        if c != 1:
            print("  ROJO        %-52s el texto viejo aparece %d veces" % (etiqueta, c))
            return 1
        textos[ruta] = t.replace(viejo, nuevo, 1)
        print("  HECHA       %-52s %s" % (etiqueta, os.path.basename(ruta)))
        hechas += 1

    # LA COLA: bloques que se ADOSAN AL FINAL del fichero, sin ancla.
    for ruta, etiqueta, bloque in COLA:
        if ruta not in textos:
            textos[ruta] = io.open(ruta, encoding="utf-8").read()
        t = textos[ruta]
        if bloque in t:
            print("  YA ESTABA   %-52s (idempotente)" % etiqueta)
            saltadas += 1
            continue
        textos[ruta] = t.rstrip("\n") + "\n" + bloque
        print("  ADOSADA     %-52s %s (al final)" % (etiqueta, os.path.basename(ruta)))
        hechas += 1

    if not a.simular:
        for ruta, t in textos.items():
            io.open(ruta, "w", encoding="utf-8", newline="\n").write(t)

    print()
    print("  sustituciones HECHAS: %d | ya estaban: %d" % (hechas, saltadas))
    print("  ficheros: %s" % ", ".join(sorted(os.path.basename(r) for r in textos)))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
