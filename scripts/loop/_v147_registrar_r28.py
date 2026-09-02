# -*- coding: utf-8 -*-
"""_v147_registrar_r28.py . TAREA 1.a de la vuelta 147: anade R.28 al final de
docs/PENDIENTES.md POR ADICION PURA, sin tocar una linea de lo que ya hay."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "PENDIENTES.md")

TEXTO = u"""
## R.28. Registro de correcciones y adjudicaciones declaradas de la vuelta
146 (acta del auditor, vuelta 146; escrito en la vuelta 147, TAREA 1.a)

Por adicion, como R.21 a R.27. Las adjudicaciones y las caidas del auditor se
escriben IGUAL que las del ejecutor. Corte de todas las cifras de esta entrada:
2 sep 2026, salvo donde se diga otra cosa.

**(1) LAS DIECIOCHO ADJUDICACIONES DEL ACTA 146 (3.1 a 3.18). LOS TRECE
DISCUTIBLES A FAVOR, CINCO CON RESERVA, Y LAS TRES ULTIMAS SON LAS RESPUESTAS A
LAS TRES PREGUNTAS DEL EJECUTOR.**
  - **3.1, DISCUTIBLE 1, PUBLICAR OCHO CUANDO EL ENCARGO ANTICIPABA CUATRO: A
    FAVOR, Y EL EQUIVOCADO ERA EL AUDITOR.** `EJECUTOR.md` 2 manda que hable el
    instrumento, y el cuatro del encargo **no salia de ningun instrumento**: la
    guarda canonica sola mueve `A1.2` y `A2.4`, o sea dos casillas y no una.
    Verificado en dos direcciones por el auditor (vara vieja sobre el arbol de
    hoy: 3; vara nueva: 8). **Va a la cuenta del auditor como su caida 4.4.a.**
  - **3.2, DISCUTIBLE 2, NO MOVER `OP-A-01` A HECHA: A FAVOR, CON RAZON MEDIDA.**
    El criterio de la fase 08 es *"una fase esta HECHA cuando su verificacion se
    caeria si el fallo volviera"*, y la mitad semantica de su entrada 3 no haria
    caer nada. La medicion de la lectura literal (9 de 9) cierra la puerta de
    atras: **tampoco hay una version mecanica de esa mitad que sirva**. `estado`
    en `LISTA` es lo correcto y **publicar HECHA habria sido el verde falso**.
  - **3.3, DISCUTIBLE 3, INSTALAR LA MITAD SANA EN VEZ DE DEJARLA ENTERA SIN
    INSTALAR: A FAVOR, CON RESERVA.** Media guarda que muerde es mejor que
    ninguna, y muerde de verdad. **LA RESERVA: la vara marca `A1.3 INSTALADO Y
    MUERDE` a secas y eso lee como mas de lo que hay.** Se arregla en el
    instrumento y no en la prosa: es la TAREA 3.c de la vuelta 147.
  - **3.4, DISCUTIBLE 4, LA NOMINA COMO FICHERO NUEVO EN `dataset/metadata/`: A
    FAVOR.** Es dato y no nodo, no lo sincroniza `sync_assets_web.py` y no toca
    el grafo. Y su perdida **falla ruidoso** (banco 9).
  - **3.5, DISCUTIBLE 5, LA NOMINA CONGELA EL ESTADO SIN ADJUDICAR SU CONTENIDO:
    A FAVOR CON RESERVA SERIA.** **LA RESERVA: "re-sellarla es re-adjudicar" es
    una REGLA SIN GUARDA**, la misma especie que la caida 4.2 de la casa del
    acta 145. Convertida en codigo en la TAREA 3.d de la vuelta 147.
  - **3.6, DISCUTIBLE 6, LA VENTANA BIDIRECCIONAL DE LA GUARDA DE AUSENCIAS: A
    FAVOR.** La pregunta es binaria y no hay nada que cuadrar contra el fichero
    del vecino; `PREGUNTA:` obligatoria deja el prestamo escrito y visible.
  - **3.7, DISCUTIBLE 7, EL BLOQUE `CITA CONGELADA` COMO EXENCION NUEVA: A
    FAVOR, Y ES BUENA INGENIERIA.** La mutacion del auditor lo prueba: **no es
    un interruptor**, la guarda lee el blob del ref y cae nombrando la linea
    inventada.
  - **3.8, DISCUTIBLE 8, `--excluir` Y `--universo-prefijo`: A FAVOR CON
    RESERVA.** Los dos se imprimen en el sello. **LA RESERVA: el instrumento
    acepta el recorte sin medir lo que cuesta**; un universo de 1.481 y uno de
    15.135 valen igual ante la guarda.
  - **3.9, DISCUTIBLE 9, EL VEREDICTO POR LA PIERNA EQUIVOCADA: A FAVOR, Y ES LA
    MEJOR MARCA DE LA VUELTA.** El reporte nombro la seccion, nombro que el
    `HALLADO` salia por coincidencias de NOMBRE ajenas a la pregunta y nombro
    que lo unico que sostenia la ausencia era la pierna POR CONTENIDO en cero.
    **Ahi cayo, y por eso la caida del umbral es DENTRO de lo marcado.** **La
    extension que el discutible no vio: la pierna por contenido tambien puede
    fallar, y falla buscando nombres adivinados en vez del concepto.** Esa
    extension es la escalada de la TAREA 2 de la vuelta 147.
  - **3.10, DISCUTIBLE 10, REPARAR LA VARA SIN QUE ESTUVIERA EN EL ENCARGO: A
    FAVOR, SIN RESERVA.** Medido por el auditor: **la vara vieja sobre el arbol
    de hoy sigue diciendo 3**, o sea que la reparacion **no infla la cifra, la
    hace posible**. Y el texto viejo no se borro.
  - **3.11, DISCUTIBLE 11, CAMBIAR LA COLA DE LA VARA, QUE ERA PROSA Y NO CIFRA:
    A FAVOR.** Una linea de veredicto que no depende de lo que el instrumento
    acaba de medir es una cifra tecleada, y la doctrina de la cifra tallada la
    cubre por extension natural. **No hace falta regla nueva.**
  - **3.12, DISCUTIBLE 12, EL VOCABULARIO DE DOCE FORMULAS: A FAVOR EN LA
    ELECCION, CON RESERVA MEDIDA.** El encargo lo dejaba elegir y se declaro
    entero en el docstring. **Pero el agujero ya no es una duda: el acta lo
    midio sobre la propia pagina que lo anuncia.** La ampliacion es la TAREA 2.a
    de la vuelta 147.
  - **3.13, DISCUTIBLE 13, CORRER `run_phase1.py` SUELTO Y DECLARARLO: A FAVOR
    DE DECLARARLO.** Escribirlo en vez de esconderlo es lo que la casa pide y el
    remedio fue el correcto (cerrar el ciclo, no tocar la guarda). **Sigue
    siendo caida de procedimiento del ejecutor.** Y le paso al auditor dos veces
    en la misma vuelta: es su caida 4.4.b.
  - **3.14, RESPUESTA A LA PREGUNTA 1, LA TRUNCACION A 31.** **El hallazgo de
    fondo es REAL y vale: la truncacion esta HORNEADA EN LA TABLA CANONICA.**
    **La cifra es falsa y la unidad es la vieja.** Por la unidad del reporte son
    **SIETE**; por el detector VIGENTE de la campana (31 CON RESTO NO VACIO,
    `docs/PENDIENTES.md` DECIMA entrada) son **SEIS**. **QUE SE HACE CON ELLO:
    NADA AL DATASET.** No se toca la tabla, no se toca una grafia, no se toca
    `OPERACIONES.jsonl`. Se corrige la cifra **por adicion y sin borrar el texto
    viejo**, y la pregunta de fondo queda registrada para quien cierre la fase
    08. Cumplida en la vuelta 147 como **CORRECCION 25**.
  - **3.15, RESPUESTA A LA PREGUNTA 2, EL UMBRAL: TIENE NUMERO, Y SON DOS.**
    `scripts/intra_dominio.py` lineas 60 y 68: **`UMBRAL_TITULO = 80`** y
    **`UMBRAL_SEMANTICO = 0.78`**, este ultimo con su calibracion escrita
    encima. Es el umbral **del cribado intra**, que es lo que la ficha de
    `OP-A-02` manda usar. **La puerta semantica SI se puede cablear y el bloqueo
    que la PREGUNTA 2 declaraba no existe.** Cumplida en la vuelta 147 como
    **CORRECCION 26**.
  - **3.16, LA MITAD SEMANTICA DE LA ENTRADA 3 (pendiente de doctrina 7.1 del
    reporte 146): NO ES PARADA HOY, Y CON SU FRONTERA ESCRITA.** No hubo
    decision improvisada: se instalo la mitad mecanica, se dejo la otra sin
    instalar, se escribio en el codigo, en la vara y en el reporte, y no se
    movio `estado`. **LA FRONTERA, PARA QUE NO SE ARRASTRE EN SILENCIO: el dia
    que la fase 07 intente CERRARSE con esa mitad sin resolver, ESO SI ES PARADA
    de decision de fundador.** Hoy la fase no cierra por otra razon (`A2.6`).
  - **3.17, LA CIFRA DE `A1.3` EN LA VARA: SE PARTE EN DOS.** Un control
    instalado a medias no puede publicarse con el mismo rotulo que uno entero,
    por la misma razon de unidades de la adjudicacion 3.9 del acta 144. La vara
    tiene que decir `INSTALADO EN SU MITAD MECANICA` y el recuento tiene que
    publicar **las dos cifras**. Es la TAREA 3.c de la vuelta 147.
  - **3.18, RESPUESTA A LA PREGUNTA 3, NUEVE CONTROLES O SIETE: LAS DOS, Y LAS
    DOS EN LA SALIDA.** El nueve es la unidad DECLARADA (cada ficha declara los
    suyos y la vara no puede desobedecer a las fichas) y el siete es la unidad
    DISTINTA (`A1.1` con `A2.3`, y `A1.2` con `A2.4`, son el mismo control con
    dos nombres). **Ninguna es falsa y publicar solo una esconde la otra.** Es
    la misma doctrina de las dos unidades de arista del acta 145: **el rotulo se
    gana midiendo, no eligiendo.** Es la TAREA 3.b de la vuelta 147.

**(2) DOS CAIDAS DEL EJECUTOR, Y LAS DOS ACUMULAN (acta 146, 4.1 y 4.2).**
  - **4.1, DE CIFRA PUBLICADA, Y ACUMULA. EL "OCHO" DE LAS GRAFIAS DE 31, QUE
    CONTRADICE SU PROPIA ENUMERACION.** La CORRECCION 24.c y la 3.f del reporte
    de la 146 publican *"ocho de ellas estan VIVAS y son CANONICAS de la tabla
    de `OP-S-11`"* y **enumeran SIETE nombres en la misma frase**. Medido por el
    auditor por tres caminos independientes: **SIETE** por esa misma unidad y
    **SEIS** por el detector vigente. **EL MOTIVO POR EL QUE ES DE CIFRA
    PUBLICADA Y NO DE REPORTE, ESCRITO: VIVE EN
    `docs/plan/CORRECCIONES_A_APLICAR.md`**, o sea en `docs/plan/`, y por la
    letra de la seccion 4 eso la hace cifra publicada. **RACHA DE CIFRA
    PUBLICADA: DE CERO A UNO.** **Y CAE FUERA DE LOS TRECE DISCUTIBLES**:
    ninguno cubre el censo de la truncacion. Por la regla del credito de la
    seccion 1.2, **BAJA EL CREDITO DE TODA LA TANDA y ese tramo se relee al
    doble**, cumplido en la vuelta 147, TAREA 3.a. **LO QUE NO ES: no mueve un
    nodo, no mueve una arista, no mueve una ficha.**
  - **4.2, DE REPORTE, Y ACUMULA. *"EL UMBRAL DE LA COLA NO TIENE NUMERO EN
    NINGUNA PARTE"*.** Vive en la **cabecera de la PREGUNTA 2** del reporte de
    la 146 y en su conclusion (*"Sin ese numero la puerta semantica no se puede
    cablear"*), asi que por la letra afinada del 27 ago 2026 **ACUMULA**. Es **la
    misma especie que la caida 4.1 del acta 145**: una busqueda negativa
    publicada como hecho y usada para bloquear trabajo. **Y CAE DENTRO del
    discutible 9**, que nombra la 3.e y nombra que la ausencia descansaba entera
    en la pierna por contenido: **por la regla del marcado, NO baja el credito de
    la tanda.** Registrada como **CORRECCION 26**.

**(3) DOS DE LA CASA, LAS DOS DE GUARDA QUE NO ALCANZA (acta 146, 4.3).**
  - **4.3.a: EL VOCABULARIO DE DOCE FORMULAS TIENE UN AGUJERO MEDIDO.** El acta
    lo midio sobre la pagina que lo anuncia y publico seis escapes, cinco de
    ellos sin barrido en su ventana. **No es caida del ejecutor: el encargo le
    dejo elegir el vocabulario.** Tapada en la vuelta 147, TAREA 2.a.
  - **4.3.b: UN BARRIDO PUEDE TRAER EL SELLO COMPLETO Y UNA PIERNA POR CONTENIDO
    DE NOMBRES ADIVINADOS**, y entonces el sello certifica el metodo exacto que
    la CORRECCION 23 prohibe, un nivel mas abajo. **Tampoco es caida del
    ejecutor: el sello no pedia nada sobre los patrones.** Tapada en la vuelta
    147, TAREA 2.b, con la SEXTA PIEZA del sello.

**(4) DOS CAIDAS DEL AUDITOR (acta 146, 4.4).**
  - **4.4.a, DE ENCARGO: ANTICIPO UNA CIFRA Y MANDO PUBLICARLA.** El encargo
    escribio *"tu vara tiene que pasar de TRES a CUATRO instalados y mordiendo, y
    ESA es la cifra que publicas"*, y **el cuatro no salia de ningun
    instrumento**; ni siquiera cuadraba con su propia 3.c, que sola mueve dos
    casillas. Es la misma especie que sus caidas 4.3 y 4.4 del acta 145.
  - **4.4.b, DE PROCEDIMIENTO: CORRIO `run_phase1.py` FUERA DEL ORDEN DEL CICLO
    DOS VECES**, y se saco dos falsos rojos (71 divergentes, y despues un numstat
    de 72/72), **exactamente la trampa que el mismo habia avisado por escrito** y
    que el ejecutor habia declarado en su 5.1. Cerro el ciclo en su orden, volvio
    a OK, y lo escribio en vez de callarlo.

**(5) LAS DOS RACHAS, CON SU ESTADO NUEVO Y SU MOTIVO ESCRITO.**
  - **RACHA DE CLASE O CIFRA PUBLICADA DEL EJECUTOR: DE CERO A UNO.** El motivo:
    **la 4.1 vive en `docs/plan/CORRECCIONES_A_APLICAR.md`**, y por la letra de
    la seccion 4 del acta eso la hace cifra publicada y no de reporte. **La regla
    de parada de esta racha es DOS TANDAS SEGUIDAS, asi que una no es parada, y
    una segunda si lo seria.**
  - **RACHA DE REPORTE: DE DOS A TRES.** El motivo: **la 4.2 ACUMULA porque vive
    en una cabecera y en una conclusion**.
  - **POR QUE ESO NO ES PARADA TODAVIA, DICHO CON LA LETRA DE LA REGLA DELANTE.**
    La regla de parada **no dice "tres acumuladas": dice TRES SEGUIDAS DE LA
    MISMA ESPECIE**. La de la 144 era **la cuenta de filas de una tabla**; la de
    la 145 y la de la 146 son las dos **una busqueda negativa publicada como
    hecho**. **Van DOS de la misma especie corriendo, y la tercera de esa especie
    seria PARADA AUTOMATICA.** **Y una segunda caida de cifra publicada tambien
    lo seria.** No es una amenaza: es la aritmetica, escrita por delante para
    poder evitarla.
  - **Y DOS ES DOS, ASI QUE POR `AUDITOR.md` 1.2 LA ESCALADA VUELVE A DISPARARSE
    Y ES LA TAREA 2 DE LA VUELTA 147.** La escalada de la 146
    (`verificar_ausencias_del_reporte.py` mas `barrer_ausencia.py`) **esta
    construida y muerde**, probado por mutaciones del auditor; **lo que pasa es
    que no alcanza**, y se sabe porque **la caida de la 146 le paso por
    delante**. La de la 147 la extiende: **ampliacion declarada del vocabulario y
    SEXTA PIEZA del sello, la vitalidad de la pierna por contenido.**

**NINGUN RAMAL NUEVO.** Todo se resuelve con `EJECUTOR.md` 1, 2, 8 y 9, banco 9
(fallar ruidoso), banco 9.10 (el sujeto congelado), la CORRECCION 18 (dos
unidades no comparten columna), la CORRECCION 22 (el sujeto vivo), la CORRECCION
23 (la busqueda negativa) y `AUDITOR.md` 1.2 y 3. Siguen vivos (i) a (xxi).
"""


def main():
    with io.open(RUTA, encoding="utf-8") as f:
        antes = f.read()
    if "## R.28." in antes:
        raise SystemExit("ROJO PREVIO: R.28 ya esta escrito, no se duplica")
    with io.open(RUTA, "a", encoding="utf-8", newline="\n") as f:
        f.write(TEXTO)
    with io.open(RUTA, encoding="utf-8") as f:
        despues = f.read()
    assert despues.startswith(antes), "ROJO: la escritura NO fue por adicion pura"
    print("R.28 anadido por ADICION PURA. El fichero viejo es prefijo exacto del nuevo.")
    print("CIFRA lineas antes: %d lineas" % len(antes.splitlines()))
    print("CIFRA lineas despues: %d lineas" % len(despues.splitlines()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
