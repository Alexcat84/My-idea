# -*- coding: utf-8 -*-
"""vuelta150_1_registrar.py . TAREA 1 de la vuelta 150, POR ADICION PURA.

Escribe, en este orden y sin borrar un solo texto viejo:

  (1.a) R.29 al final de docs/plan/CORRECCIONES_A_APLICAR.md, con las
        adjudicaciones, las respuestas y las caidas del acta 149. El encargo
        nombra ESE fichero y no docs/PENDIENTES.md, donde viven R.20 a R.28; se
        obedece la letra del encargo y se deja una REMISION de una linea en
        PENDIENTES.md para que la serie no se pierda. Una remision no es una
        copia: apunta a la fuente unica.
  (1.b) CORRECCION 30 al final de docs/plan/CORRECCIONES_A_APLICAR.md, con el
        rastro del 1.056 medido HOY por instrumento propio
        (scripts/loop/vuelta150_1b_rastro_del_1056.py) y con la DISCREPANCIA
        contra el acta declarada, no copiada.
  (1.c) SOLO DESPUES de la 1.b: el campo `estado` de OP-S-12 pasa de LISTA a
        HECHA en docs/plan/OPERACIONES.jsonl. El esquema no se toca.

Comprueba al final que las 71 fichas siguen teniendo un solo esquema de 18
claves y lo imprime.

USO:
  python scripts/loop/vuelta150_1_registrar.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CORR = os.path.join(RAIZ, "docs", "plan", "CORRECCIONES_A_APLICAR.md")
PEND = os.path.join(RAIZ, "docs", "PENDIENTES.md")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

R29 = u"""
---

## R.29. Registro de correcciones y adjudicaciones declaradas de la vuelta 149 (acta del auditor, vuelta 149; escrito en la vuelta 150, TAREA 1.a)

**POR ADICION, y en `docs/plan/CORRECCIONES_A_APLICAR.md` porque el encargo de la
vuelta 150 nombra este fichero con esas palabras.** R.20 a R.28 viven en
`docs/PENDIENTES.md`; ahi queda una **remision de una linea** a esta entrada, no
una copia. Corte de todas las cifras de esta entrada: **2 sep 2026**, salvo donde
se diga otra cosa. Las adjudicaciones y las caidas del auditor se escriben IGUAL
que las del ejecutor.

**(1) LOS NUEVE DISCUTIBLES DEL REPORTE 148, LOS NUEVE ADJUDICADOS A FAVOR, CON
RESERVA EN EL 2, EL 4 Y EL 5.**

  - **3.1, DISCUTIBLE 1, REPARAR LA GUARDA DE LA APERTURA EN VEZ DE PARAR: A
    FAVOR, SIN RESERVA.** La guarda exigia *el padre es el commit del acta*, que
    es un **proxy** del fin verdadero (*la apertura se midio antes de la primera
    operacion*), y el proxy se rompe **estructuralmente** en toda vuelta que
    reanuda tras una parada. Lo que lo salva de ser el auditado tocandose su
    propia guarda son tres cosas que el auditor verifico: el rojo corrido ANTES
    de tocarla y commiteado aparte
    (`SALIDA_V148_0D_APERTURA_SELLADA_GUARDA_VIEJA.txt`), el criterio nuevo
    cayendo con **dos** mutaciones, y el corredor aceptado **impreso entero**.
  - **3.2, DISCUTIBLE 2, LAS TRES RUTAS DEL CORREDOR LAS ELIGIO EL EJECUTOR: A
    FAVOR, CON RESERVA ANOTADA.** `PROMPT_SIGUIENTE.md`, `PARA_ALEXIS.md` y
    `docs/loop/paradas/` son los tres sitios donde la casa escribe una parada.
    **LA RESERVA:** el dia que una decision toque un cuarto sitio la guarda dara
    ROJO y habra que ensancharla; **que ensancharla sea un acto declarado y no un
    parche silencioso queda anotado**.
  - **3.3, DISCUTIBLE 3, `A1.3` CUENTA COMO ENTERO POR REMISION Y LA VARA PUBLICA
    9 DE 9: A FAVOR, Y EL AUDITOR LO PROBO POR MUTACION PROPIA.** Mando fuera el
    fichero de la decision y **la vara se cayo sola de 9 a 7 arrastrando a
    `A1.3`**, con el motivo escrito. Eso separa una remision de un interruptor:
    la remision se comprueba en la misma corrida y **cae en cascada**.
  - **3.4, DISCUTIBLE 4, `estado_de_parada` MIRA SI EL `-DECISION.md` ESTA AL
    LADO: A FAVOR, CON RESERVA SERIA Y NOMBRADA.** El fichero en disco es el
    unico sujeto que no se puede fingir con una palabra, y la vara no descansa
    solo en eso: `A2.6` ademas tiene que EXISTIR y MORDER por mutacion, 6 de 6.
    **LA RESERVA, escrita para quien venga: el fichero prueba que se decidio, no
    que se aplico.**
  - **3.5, DISCUTIBLE 5, LA EXENCION DECLARADA LA ESCRIBE EL AUDITADO: A FAVOR,
    CON RESERVA.** No es un interruptor porque **la guarda comprueba ella misma
    que lo eximido no habla del repositorio** y rechaza nombrando la ruta, el
    `SALIDA_V<N>_` o la extension. Verificado con su bateria de **seis casos**.
    **LA RESERVA: es una puerta que antes no existia**, y queda abierta con una
    condicion encargada: **cada exencion usada se imprime con su motivo en la
    salida del cierre**.
  - **3.6, DISCUTIBLE 6, LA CORRECCION DENTRO DEL MISMO STRING EN VEZ DE UNA
    CLAVE NUEVA: A FAVOR, SIN RESERVA.** Medido por el auditor: **71 fichas, un
    solo esquema, 18 claves**. Una clave 19 en una sola ficha habria roto la
    uniformidad que hace medible al catalogo entero.
  - **3.7, DISCUTIBLE 7, `OP-S-12` ELIGE QUE ENTRADA SOBREVIVE: A FAVOR, Y ES EL
    DISCUTIBLE MEJOR PLANTEADO DE LA VUELTA.** Medido y no creido: los `node_id`
    identicos, los `ids_alias` identicos, **CERO literales aparecen de la nada y
    121 desaparecen del todo**, y los **7.706** vecindarios resueltos identicos
    uno a uno. **Lo que la operacion elige no es un id: es cual de dos escrituras
    del mismo id sobrevive.**
  - **3.8, DISCUTIBLE 8, EL 1.056 QUE NO SE CUMPLE: A FAVOR, CON EL RASTRO
    COMPLETO.** Su desarrollo entero, re medido hoy con instrumento propio del
    ejecutor, va en la **CORRECCION 30** de esta misma pagina, con una
    discrepancia declarada.
  - **3.9, DISCUTIBLE 9, EL DESFASE DEL INDICE SE TRAE Y NO SE ARREGLA: A FAVOR,
    SIN RESERVA.** Arreglarlo pide `VOYAGE_API_KEY`, o sea gasto fuera del repo
    con una credencial que la casa reserva. El auditor anade que los **370** no
    vivos son **370 DEPRECADOS y CERO FANTASMAS**, y que **el blob del indice no
    se movio en toda la vuelta**.

**(2) LAS DOS PREGUNTAS DEL REPORTE 148, CONTESTADAS SIN DOCTRINA NUEVA.**

  - **3.10, PREGUNTA 1, SI LA FASE 08 PUEDE DARSE POR HECHA: NO.** El criterio
    esta en la primera linea de `docs/plan/08_VERIFICACION.md`: *"UNA FASE ESTA
    HECHA CUANDO SU VERIFICACION SE CAERIA SI EL FALLO VOLVIERA. No cuando pasa
    verde: cuando se CAERIA."* **Una verificacion que no se puede correr no se
    puede caer.** Cubierto ademas por extension citable de la seccion 4 de
    `AUDITOR.md` (*"Credenciales ausentes... que falle visible"*). **LA FASE 08
    QUEDA ABIERTA HASTA LA SESION CON CREDENCIAL.**
  - **3.11, PREGUNTA 2, SI EL REINDEXADO ENTRA EN ESA SESION: SI, Y NO ES OPINION
    DEL AUDITOR.** El reindexado **ES el punto 5 de la verificacion transversal
    de la propia fase 08**. Verificado en el codigo: `main()` de
    `scripts/build_semantic_index_voyage.py` reconstruye la lista `ids` desde
    cero con los no deprecados, asi que **una corrida completa deja el indice con
    exactamente los vivos de hoy**.

**(3) EL CIERRE DE LA FASE 07 ADUANA, ADJUDICACION 3.12 DEL ACTA 149.**
**LA FASE 07 QUEDA CERRADA.** El auditor la cierra y la firma, sobre la letra de
la decision del fundador del 2 sep 2026 (*"Con las dos, la fase 07 CIERRA"*), con
las dos aplicaciones verificadas por el en el codigo y no en la prosa (el paso
`a-previo` existe en `integrar_packs.py:317`, se llama antes de la copia en la
linea 556, la puerta sigue en el `copy2` de la linea 420 con `A2.6` en la 417),
con **la vara de codigo en 9 de 9 enteros, 0 no enteros, 0 no instalados**,
sostenida por **su propia mutacion**, y con el motivo de la remision medido: la
lectura literal **dispara en los 9** sobre los 8 nodos adjudicados. Que
`tallar_estado_de_fase.py` diga `NO COMPUTABLE` no lo impide: es la frontera de la
adjudicacion 3.9 del acta 144, que separa la vara de GRAFO de la vara de CODIGO.
**Dos unidades no comparten columna.**

**(4) LAS DOS ADJUDICACIONES DE ORDEN, 3.13 Y 3.14.**

  - **3.13, `OP-C-05` SE EJECUTA EN LA VUELTA SIGUIENTE Y ES BLOQUEANTE.** No es
    un descubrimiento discutible: es el orden escrito de `AUDITOR.md` 3, FASE III
    (*"fase 0 de codigo primero y bloqueante"*). **Sin ella, las 925 entradas que
    la vuelta 148 retiro no tienen quien las defienda.**
  - **3.14, EL `estado` DE `OP-S-12` SE MUEVE A `HECHA`, PERO DESPUES DE LA
    CORRECCION, NO ANTES.** Por el precedente de la 3.12 del acta 147: `estado`
    en `HECHA` con una cuenta abierta encima es publicar un verde sobre una
    pregunta abierta. **La cuenta abierta es la verificacion 4.**

**(5) LAS CAIDAS, CON NOMBRE.**

  - **4.1, DEL EJECUTOR, DE CLASE Y DE CIFRA PUBLICADA: NINGUNA**, dicho con la
    lista de lo que el auditor re midio delante (catorce refs, las 7.706
    comparaciones, el marcador entero, las nueve filas de cabecera caracter por
    caracter, las seis baterias, las cinco guardas del cierre, los diez ficheros
    de apertura, motor, web y tsc).
  - **4.2, DEL EJECUTOR, DE EXPEDIENTE: `OP-S-12` EJECUTADA Y SU `estado` SIN
    MOVER NI DECLARAR.** La unica de las diez de `05_SANEO` que sigue en `LISTA`
    despues de correr. **Lo que la hace caida no es no moverlo: es no decir
    nada.** Un `estado` congelado a proposito es una decision; congelado en
    silencio es un expediente que no cuenta lo que paso.
  - **4.3, DEL EJECUTOR, DE INCUMPLIMIENTO DE ENCARGO, ATENUADA POR SU PROPIA
    DECLARACION: LA FASE 08 NO SE RECORRIO ENTERA POR LA MITAD QUE SI SE PODIA.**
    De las **OCHO** filas de la tabla POR FASE, que no piden credencial, se midio
    **UNA**. La declaracion lo separa de una mentira, no de un encargo sin
    entregar.
  - **4.4, DEL EJECUTOR, DE REPORTE: NINGUNA**, y el auditor explica la que
    estuvo a punto de registrar: *"Tres corren y tres piden credencial"* sobre
    cinco puntos son **dos afirmaciones verdaderas cuyos conjuntos se solapan en
    el punto 4** sin decirlo. **Registrada como imprecision de dictado, no como
    caida.** Lo que queda encargado es la palabra: *correr* no puede significar
    *se invoco* y *quedo satisfecho* en la misma frase.
  - **4.5, DE LA CASA: EL ENCARGO DE LA VUELTA 148 SALTA DE `OP-S-12` A LA FASE
    08 SIN PASAR POR `OP-C-05`.** Lo escribio el fundador al relanzar el bucle
    (commit `68db6230`), asi que no va a la cuenta de encargo del auditor ni a la
    del ejecutor, que lo siguio al pie de la letra. **Instruccion que deja
    escrita: el modo continuo mira el `depende_de` del catalogo y no solo la
    linea del encargo.**
  - **4.6.a, DEL AUDITOR, DE PROCEDIMIENTO: corrio `run_phase1.py` suelto, fuera
    del orden del ciclo, y se saco un falso rojo** (`AssertionError: 71 nodos
    divergentes entre las dos copias`). No era un rojo: era saltarse el comando
    2. **Es la cuarta acta seguida en que un auditor cae en la misma trampa**, y
    por eso encarga la guarda en vez de limitarse a confesarla.
  - **4.6.b, DEL AUDITOR, DE CIFRA DE SU LINAJE: el CINCO del acta 147 tampoco
    reproduce sobre el sujeto que la frase nombra.** Su medicion de hoy da
    **CUATRO sobre la pagina del acta y CINCO sobre el reporte de la 146**. **La
    correccion de la 147 corrigio la cifra y erro el sujeto.** El acierto es del
    ejecutor, que la declaro en vez de copiarla, y ya esta registrada por adicion
    en la CORRECCION 27.

**(6) LA METRICA DE CREDITO: LA TANDA BAJA.** Las dos discrepancias del acta
aparecieron **FUERA de los discutibles marcados** y las dos son de expediente
(el `estado` de `OP-S-12` sin mover ni declarar, y `OP-C-05` desbloqueada y sin
nombrar). Ninguna toca una cifra ni una clase. Por `AUDITOR.md` 1.2 **se debe una
relectura al doble del tramo del expediente**, entregada en la TAREA 3 de la
vuelta 150.
"""

C30 = u"""
---

## CORRECCION 30. **LA VERIFICACION 4 DE `OP-S-12`: EL 1.056 ERA FIEL A SU CORTE Y HOY SON 925, CON EL RASTRO DE LAS TREINTA VERSIONES DELANTE**

**Vuelta 150, TAREA 1.b, sobre la adjudicacion 3.8 del acta del auditor de la
vuelta 149 (discutible 8 del reporte 148, a favor).** Corte de la medicion de
hoy: **2 sep 2026**. **POR ADICION: NO SE BORRA LA CIFRA VIEJA NI SE TOCA EL
TEXTO DE LA FICHA.**

**LA CIFRA VIEJA, CITADA VERBATIM DE `docs/plan/OPERACIONES.jsonl`, ficha
`OP-S-12`, campo `verificacion`, cuarta entrada:** *"el numero total de entradas
baja en exactamente 1.056; si baja mas, se borro algo que no era duplicado"*.

**SU CORTE Y SU UNIVERSO, LOS DOS ESCRITOS EN LA PROPIA FICHA:** `fecha_corte`
**2026-08-11**, y su `evidencia` dice *"scripts/plan/aristas_duplicadas_tras_resolver.py,
corrida del 11 ago 2026 sobre 3.521 nodos vivos"* y *"docs/plan/ARISTAS_DUPLICADAS.jsonl,
1.015 grupos"*.

**LO QUE LA OPERACION RETIRO EL 2 SEP 2026 (vuelta 148, commit `a34328b2`): 925
entradas.** No son 1.056, y **NO ES UNA CONTRADICCION**: es una cifra fiel a un
corte que se movio por debajo durante veintiuna vueltas.

**EL RASTRO, MEDIDO HOY CON INSTRUMENTO PROPIO DEL EJECUTOR** y no copiado del
acta (`EJECUTOR.md` 2). Instrumento:
`scripts/loop/vuelta150_1b_rastro_del_1056.py`; salida commiteada:
`docs/loop/SALIDA_V150_1B_RASTRO_1056.txt`.

| lo medido | cifra de hoy |
|---|---:|
| versiones de `docs/plan/ARISTAS_DUPLICADAS.jsonl` en git (`git log --follow`) | **30** |
| PRIMERA version, `af467eb1` (*"Plan: P.6, las 1.056 aristas duplicadas"*): grupos / nodos / entradas que sobran | **1.015 / 802 / 1.056** |
| version de HEAD, `d6341ebe` (vuelta 73): grupos / nodos / entradas que sobran | **898 / 711 / 935** |
| de esas 935, entradas sobre nodos **HOY DEPRECADOS** | **10** (en 10 grupos) |
| de esas 935, entradas sobre nodos **QUE YA NO EXISTEN** | **0** |
| de esas 935, entradas sobre nodos **VIVOS** | **925** |

**LAS SEIS CIFRAS REPRODUCEN AL DIGITO LAS DEL ACTA 149.** El fichero no es un
fichero quieto: **se regenera con cada fusion**, y cada fusion de `OP-U-01` y
`OP-U-02` consumio duplicadas por el camino. **La evidencia de la ficha era fiel
a su corte**, y el 925 de la pasada es el mismo numero por tres caminos
independientes: el parser del auditor, la operacion de la vuelta 148 y este
fichero escrito hace setenta y cinco vueltas.

**LA VERIFICACION 4 NO ESTA CONTRADICHA: ESTA VENCIDA.** Su guarda real (*"si
baja MAS, se borro algo que no era duplicado"*) **se respeta**: bajo exactamente
lo que habia sobre vivos, ni una entrada mas.

**UNA DISCREPANCIA CONTRA EL ACTA, DECLARADA Y NO COPIADA (`EJECUTOR.md` 2).**
El acta 149, adjudicacion 3.8, dice: *"La bajada de 1.056 a 935 es **monotona** a
lo largo de las treinta versiones"*. **MI MEDICION DE HOY DICE QUE NO ES
MONOTONA, por un solo escalon y de una sola unidad:** la version `706397c7`
(vuelta 57, 20 ago 2026 11:49) da **995** entradas que sobran y la siguiente,
`3ffc2091` (vuelta 58, 20 ago 2026 13:16), da **996**. Comprobado que la segunda
es descendiente de la primera (`git merge-base --is-ancestor 706397c7 3ffc2091`
sale en verde), o sea que el orden es el cronologico y no un artefacto del
listado. **Las otras veintiocho transiciones bajan o se quedan igual.** Sube en
una porque una fusion puede crear una duplicada nueva antes de consumir otras;
**la direccion general del acta es correcta y la palabra "monotona" no lo es**.
**La cifra que sostiene la adjudicacion 3.8 (1.056 al inicio, 935 en HEAD, 925
sobre vivos) NO depende de esa palabra y queda intacta.**

**LO QUE ESTA CORRECCION NO HACE.** No borra ni reescribe la cuarta
`verificacion` de `OP-S-12`, que se queda literal. No toca el esquema: las **71
fichas siguen teniendo UN solo esquema de 18 claves**, comprobado despues de
escribir. Y no mueve por si sola el `estado`: el `estado` se mueve **detras** de
esta correccion, que es el orden que manda la adjudicacion 3.14 del acta 149.
"""

REMISION = u"""
**REMISION (vuelta 150, TAREA 1.a): `R.29`, el registro del acta de la vuelta
149, NO esta en esta pagina.** El encargo de la vuelta 150 lo manda a
`docs/plan/CORRECCIONES_A_APLICAR.md` con esas palabras, y ahi vive, al final del
fichero. **Esto es una remision, no una copia:** la fuente unica de `R.29` es esa
pagina. Nada de `R.20` a `R.28` se toca.
"""


def anadir(ruta, texto):
    s = io.open(ruta, encoding="utf-8").read()
    largo_antes = len(s)
    if not s.endswith("\n"):
        s += "\n"
    s += texto
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(s)
    print("  %s: %d -> %d caracteres (POR ADICION)"
          % (os.path.relpath(ruta, RAIZ).replace("\\", "/"), largo_antes, len(s)))
    return largo_antes


def main():
    print("1.a) R.29 al final de CORRECCIONES_A_APLICAR.md, y la remision en PENDIENTES.md")
    antes_corr = anadir(CORR, R29)
    anadir(PEND, REMISION)

    print("")
    print("1.b) CORRECCION 30 al final de CORRECCIONES_A_APLICAR.md, DETRAS de R.29")
    anadir(CORR, C30)

    print("")
    print("1.c) SOLO AHORA: el estado de OP-S-12, de LISTA a HECHA")
    lineas = io.open(OPS, encoding="utf-8").read().splitlines()
    fichas = [json.loads(x) for x in lineas if x.strip()]
    print("  fichas leidas: %d" % len(fichas))
    esquemas = {tuple(sorted(f.keys())) for f in fichas}
    print("  esquemas distintos ANTES: %d | claves: %d"
          % (len(esquemas), len(list(esquemas)[0])))
    tocadas = 0
    salida = []
    for f in fichas:
        if f["id_op"] == "OP-S-12":
            print("  OP-S-12 estado ANTES: %s" % f["estado"])
            assert f["estado"] == "LISTA", "el estado no es LISTA: no lo toco"
            f["estado"] = "HECHA"
            tocadas += 1
            print("  OP-S-12 estado DESPUES: %s" % f["estado"])
        salida.append(json.dumps(f, ensure_ascii=False))
    assert tocadas == 1, "se toco mas de una ficha"
    io.open(OPS, "w", encoding="utf-8", newline="\n").write("\n".join(salida) + "\n")

    fichas2 = [json.loads(x) for x in io.open(OPS, encoding="utf-8").read().splitlines() if x.strip()]
    esquemas2 = {tuple(sorted(f.keys())) for f in fichas2}
    print("  fichas DESPUES: %d | esquemas distintos: %d | claves: %d"
          % (len(fichas2), len(esquemas2), len(list(esquemas2)[0])))
    assert len(fichas2) == len(fichas), "cambio el numero de fichas"
    assert esquemas2 == esquemas, "cambio el esquema"
    hechas = sum(1 for f in fichas2 if f["fase"] == "05_SANEO" and f["estado"] == "HECHA")
    total = sum(1 for f in fichas2 if f["fase"] == "05_SANEO")
    print("  05_SANEO: %d de %d en HECHA" % (hechas, total))
    print("")
    print("EL TEXTO VIEJO NO SE BORRO EN NINGUN SITIO: las tres escrituras son adiciones,")
    print("y la de OPERACIONES.jsonl solo cambia el valor de un campo, no su texto.")
    print("longitud de CORRECCIONES_A_APLICAR.md al empezar: %d" % antes_corr)


main()
