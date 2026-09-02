# -*- coding: utf-8 -*-
"""_v145_registrar_r26.py . Escribe por ADICION la entrada R.26 al final de
docs/PENDIENTES.md (vuelta 145, TAREA 1.a). Instrumento de un solo uso, con
guarda que se niega si R.26 ya esta."""
import io

TEXTO = u"""

## R.26. Registro de correcciones y adjudicaciones declaradas de la vuelta
144 (acta de la vuelta 144; escrito en la vuelta 145, TAREA 1.a)

Por adicion, como R.21 a R.25. Las adjudicaciones y las caidas del auditor se
escriben IGUAL que las del ejecutor. Corte de todas las cifras de esta entrada:
2 sep 2026 (la fecha que `git log -1 --format=%ad --date=short` devuelve en la
vuelta 145), salvo donde se diga otra cosa.

**(1) LAS NUEVE ADJUDICACIONES DEL ACTA 144 (3.1 a 3.9). OCHO A FAVOR DEL
EJECUTOR Y LA NOVENA A FAVOR EN EL CRITERIO CON LA ETIQUETA CORREGIDA.**
  - **3.1, DISCUTIBLE 1, LA ADICION A `aristas_nuevas` DE `OP-M-04`: A FAVOR, Y
    CON SU FRONTERA ESCRITA.** Adicion pura, la entrada vieja intacta y prefijo
    exacto, ninguna entrada vieja traia flecha, y la direccion escrita
    (`identificar_consejo_asesores -> formalizar_junta_asesora`) es literalmente
    la que la entrada vieja ya decia en prosa. **LA FRONTERA, QUE ES LO QUE
    IMPORTA PARA LA PROXIMA VEZ: se puede hacer legible una ficha SOLO si (a) es
    adicion pura, (b) no anade NI UN DATO que la ficha no dijera ya en su propio
    texto y (c) sin ella la guarda aborta. Si falta una de las tres, ES PARADA.**
    Cierra la PREGUNTA 1 del reporte de la 144, sin doctrina nueva.
  - **3.2, DISCUTIBLE 2, EL SELLADOR NUEVO EN VEZ DE PARAR: A FAVOR, Y LA
    PREGUNTA 2 CONTESTADA.** No hay dos caminos para lo mismo: **hay dos
    figuras.** El de la casa sella UNA fusion con UN superviviente; el nuevo
    sella UNA MESA DE DOS ACTOS. **La frontera se escribe en el docstring de los
    dos**, cumplido en la vuelta 145, TAREA 2.e, sin tocar el codigo de ninguno.
  - **3.3, DISCUTIBLES 3, 4 Y 5, LOS TRES PARSEOS DE PROSA: A FAVOR LOS TRES Y
    BIEN MARCADOS.** El emparejamiento derivado de `ids_alias` no es circular, y
    la guarda 5 cae al intercambiar los absorbidos, re-corrido por el auditor.
  - **3.4, DISCUTIBLE 6, `CUBIERTO 2` PARA EL PASO 3 DEL ABSORBIDO DEL 367: A
    FAVOR.** La marca esta bien puesta; que la marca ideal no exista se declaro.
  - **3.5, DISCUTIBLE 7, LAS DOS PERDIDAS QUE LA FICHA NO LISTA: A FAVOR.** Las
    tres selladas correctas; `preservar` como SUELO y no TECHO es la lectura
    buena. **Las DOS MARCAS DEL AUDITOR sobre el reparto van a la fase 04 CON las
    del ejecutor y no bajan credito**: `CUBIERTO:1` del paso 3 del absorbido del
    328 conserva el QUIEN y no el PARA QUE, y `CUBIERTO:3` del paso 4 del
    absorbido del 367 esta cubierto por los pasos 1, 3 Y 5 del superviviente y la
    marca solo apunta a uno.
  - **3.6, DISCUTIBLE 8, EL ROTULO DEL INCISO: A FAVOR, Y NO SE TOCA EL
    INSTRUMENTO.** Deuda del rotulo anotada, no de esa vuelta.
  - **3.7, DISCUTIBLE 9, LAS DOS UNIDADES DEL GRADO: EL CRITERIO A FAVOR, LA
    ETIQUETA SE CORRIGE.** Ver 4.7 abajo.
  - **3.8, LO QUE FALTA DE LA MESA: ADJUDICADO.** La poda del solape es fase 04.
    **El pase del 1190 fuera de congelados mide bien (da `D`, verificado por el
    auditor) PERO NO SE APLICA**: el campo `estado` sigue congelado por las actas
    139 a 144 y ese pase va en UNA sola adjudicacion del auditor con el conteo
    antes y despues. **No era la 144 y no es la 145.**
  - **3.9, LA VARA DE LAS OPERACIONES SIN HUELLA EN EL GRAFO: ADJUDICADA POR
    EXTENSION CITABLE.** Una operacion que no deja huella en el grafo **no se
    mide con una vara de grafo; se mide contra LO QUE INSTALA**, y para un
    control eso son dos cosas y solo dos: **que el control EXISTA en el codigo y
    que MUERDA por mutacion** (banco 9, *"una guarda que no muerde no es una
    guarda"*, y `EJECUTOR.md` 1, *"el caso rojo se prueba por mutacion"*). **Y LA
    FRONTERA: ese veredicto NO entra en la columna de
    `tallar_estado_de_fase.py`**, cuyo contrato dice *"destino medido contra el
    grafo"*; mezclarlo serian DOS UNIDADES EN UNA COLUMNA, la especie exacta de
    la CORRECCION 18. **La vara nueva vive APARTE y la tabla de grafo sigue
    diciendo SIN VARA ESCRITA con un puntero a ella.** Implementado en la vuelta
    145, TAREA 3.b.

**(2) DOS CAIDAS DEL EJECUTOR, UNA QUE ACUMULA Y UNA QUE NO (acta 144, 4.1 y
4.2).**
  - **4.1, DE REPORTE, Y ESTA SI ACUMULA: el censo de llamadas a
    `pares_exceptuados_de` dice SEIS y el grep del dia daba OCHO.** Las dos que
    faltaban, `vuelta144_2a_mutaciones.py` y `vuelta144_2b_mutacion_giro.py`,
    **nacieron en el MISMO commit `c5a389dd` que publica el censo**. Y no era
    solo la cuenta: **dos de sus llamadas pasaban una LISTA LITERAL VACIA en el
    bucle que elige sujeto**, o sea que tiraban los fallos igual que hacia el giro
    antes de la 2.b. Ademas **los numeros de linea de la tabla eran los de ANTES
    de las propias reparaciones** (718, 222, 240, 130 contra 801, 232, 246, 137).
    **ACUMULA por la letra afinada del 27 ago 2026: la cifra es la cuenta de filas
    de una TABLA.** Reparado en la vuelta 145, TAREA 2.c, y el censo pasa a
    imprimirlo un instrumento (`vuelta145_2c_censo_de_llamadas.py`).
  - **4.2, DE REPORTE, Y ESTA NO ACUMULA: la comprobacion que "va debajo del
    bloque" no esta debajo del bloque.** La seccion 8 del reporte de la 144 dice
    *"La comprobacion va debajo del bloque"* y debajo no hay nada: el fichero
    termina ahi. **La linea real esta en la seccion 3.5 y SI REPRODUCE**,
    verificado por el auditor, asi que la sustancia de la 4.c se entrego. **Lo que
    cae con ella es la frase** *"pegar la salida dentro del fichero que la salida
    mide ya no cambia la medida"*: la mutacion del auditor la desmiente para el
    segundo bloque, y esa es la caida 4.3.

**(3) CINCO DE LA CASA (acta 144, 4.3 a 4.7).**
  - **4.3: `quitar_bloques_cubiertos()` ANCLA EN LA PRIMERA OCURRENCIA.** Con la
    marca repetida, el recorte va de la primera apertura al primer cierre y **el
    segundo bloque se parsea**. **Re-medido por el ejecutor con instrumento
    propio y sujeto congelado por ref de git** (`vuelta145_1b_censo_de_marcas.py`
    sobre `b7f07648:docs/loop/REPORTE.md`): la marca de COBERTURA aparece **2
    veces, lineas 274/278 y 632/638**, y las otras cuatro **una sola**; la funcion
    recorta las lineas 274 a 278 y **deja fuera las 632 a 638**. Pegada la linea
    real dentro del segundo bloque, la guarda pasa de **VERDE EXIT 0 a ROJO EXIT
    1** y las unidades fuera del vocabulario suben de **29 a 34**. **CERO
    DISCREPANCIAS con el auditor en los seis numeros.** Es la 4.3 de la 143 otra
    vez: **la 2.a de la 144 reparo ese defecto con su regla (iii), el ancla unica,
    y la 2.d no la heredo.** Registrado como **CORRECCION 21**; reparado en la
    vuelta 145, TAREA 2.a.
  - **4.4, 4.5 y 4.6: TRES GUARDAS ENVEJECIDAS POR SUJETO VIVO, UNA SOLA
    ENFERMEDAD.** `vuelta144_2d_mutacion_cobertura.py` toma el `REPORTE.md` VIVO
    y le agrega sus propios delimitadores (**1 de 3**);
    `vuelta144_3b_mutacion_negativa.py` toma el grafo de hoy, o sea el mundo
    DESPUES de su propia fusion, y su contraprueba **no puede volver a estar verde
    nunca** (**1 de 3**); `vuelta144_2a_guarda_semantica.py` compara `WORK` contra
    UN solo ref y queda en **ROJO permanente**. **Medido por el ejecutor sobre el
    arbol limpio de la apertura, y con UNA DISCREPANCIA DECLARADA**: el acta da la
    gemela `vuelta144_3b_guarda_semantica.py` por *"verde solo por haber sido la
    ultima"*, y **hoy las DOS salen ROJO con el mismo fallo**, *"cambian 0 fichas,
    se esperaba 1"*, porque con el arbol limpio `WORK` es `HEAD`. **El diagnostico
    del acta no cambia; la cifra de hoy si.** Registrado como **CORRECCION 22**;
    reparado en la vuelta 145, TAREA 2.b: los cuatro curados, **VIEJAS de 13 a 19
    y VERDE**.
  - **4.7: UNIDAD MAL NOMBRADA en `SALIDA_V144_3D_ARISTAS_MOVIDAS.txt`.** El
    rotulo *"aristas RESUELTAS entre nodos VIVOS"* publica **7.343 y 7.341**, que
    es otra unidad. **Re-medido por el ejecutor con instrumento propio ya
    commiteado** (`vuelta145_2d_aristas_movidas.py`): la unidad que produce esas
    dos cifras es **la UNION de las dos vistas leidas de nodos vivos**; con **los
    dos extremos vivos** dan **7.309 y 7.307**, exactamente las del auditor, y la
    diferencia entre las dos unidades es **34** en los dos commits. **El delta
    (-2) y los conjuntos ENTRAN (5) y SALEN (7) son identicos en las dos
    unidades.** Reparado en la vuelta 145, TAREA 2.d.

**(4) DOS CAIDAS DEL AUDITOR, LAS DOS DE ENCARGO (acta 144, 4.8 y 4.9).**
  - **4.8, DE ENCARGO: la TAREA 4 de la 144 no mandaba re-correr la bateria
    DESPUES de escribir el reporte.** Por eso `vuelta144_2d_mutacion_cobertura.py`
    estaba verde cuando se corrio y roja en cuanto se escribio el reporte de esa
    misma vuelta, y nadie lo volvio a mirar. **Reparado en el encargo de la 145
    con el paso 4.d, bloqueante.**
  - **4.9, DE ENCARGO: la regla de entrada a `VIEJAS` se escribio corta.** Decia
    *"una mutacion entra en la vuelta siguiente a la que nace"* sin exigirles lo
    unico que las hace permanentes: **el sujeto congelado**. **Corregida en la
    CORRECCION 22.**

**(5) LAS DOS RACHAS, CON SU ESTADO NUEVO Y SU MOTIVO ESCRITO.**
  - **RACHA DE CIFRA PUBLICADA: SIGUE EN CERO.** El acta 144 recomputo censo y
    aristas COMMIT A COMMIT con parser propio (**3.853 / 3.169 / 684**, y **9.234
    / 9.208 / 18.442 / 9.909** en la apertura contra **9.234 / 9.211 / 18.445 /
    9.914** en el cierre), la tabla de la fase 06 **byte a byte**, las cinco que
    entran y las siete que salen, y las doce piezas del reparto una a una: **no se
    le mueve una cifra al ejecutor.**
  - **RACHA DE REPORTE: SUBE DE CERO A UNO.** El motivo escrito: **la 4.1
    ACUMULA** por la letra afinada del 27 ago 2026, porque **la cifra es la cuenta
    de filas de una TABLA**; la 4.2 no acumula porque su sustancia se entrego y lo
    que fallo fue el puntero. **UNO NO ES DOS, asi que `AUDITOR.md` 1.2 NO obliga
    a encargar la escalada en la 145**; si en la 145 aparece una segunda que
    acumule, se encarga en el mismo acto.

**NINGUN RAMAL NUEVO.** Todo se resuelve con `P.1`, `P.16`, banco 9 (fallar
ruidoso), banco 9.10 (el sujeto congelado), el hueco de orden 1 del
`00_INDICE:482`, la CORRECCION 18 (dos unidades no comparten columna),
`AUDITOR.md` 1.1 y 1.2, y `EJECUTOR.md` reglas 1, 2, 5, 8 y 9. Siguen vivos
(i) a (xxi).
"""

RUTA = "docs/PENDIENTES.md"


def main():
    t = io.open(RUTA, encoding="utf-8").read()
    if "## R.26." in t:
        print("ROJO: R.26 ya esta escrita, no se duplica")
        return 1
    io.open(RUTA, "a", encoding="utf-8", newline="\n").write(TEXTO)
    print("anadido por adicion. Lineas ahora: %d"
          % len(io.open(RUTA, encoding="utf-8").read().split("\n")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
