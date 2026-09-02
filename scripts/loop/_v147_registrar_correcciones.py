# -*- coding: utf-8 -*-
"""_v147_registrar_correcciones.py . TAREAS 1.b y 1.c de la vuelta 147: anade
las CORRECCIONES 25 y 26 al final de docs/plan/CORRECCIONES_A_APLICAR.md POR
ADICION PURA. No se borra ni una letra de la 24.c ni de nada anterior."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "plan", "CORRECCIONES_A_APLICAR.md")

TEXTO = u"""
---

## CORRECCION 25. **LA CIFRA DE LAS GRAFIAS DE 31 CARACTERES, CORREGIDA, CON SUS DOS UNIDADES Y SUS DOS NOMINAS ENTERAS**

**Vuelta 147, TAREA 1.b, sobre la caida 4.1 del acta del auditor de la vuelta
146 (de CIFRA PUBLICADA, y ACUMULA).** Corte de todas las cifras de esta
correccion: **2 sep 2026**. **NO SE BORRA NI UNA LETRA DE LA 24.c**: se anade
aqui debajo, por `EJECUTOR.md` 8, porque *una correccion que tapa lo que corrige
no se puede auditar*.

**LO QUE LA 24.c PUBLICA, Y ES FALSO EN SU CIFRA:** *"hoy hay 10 grafias
distintas cuyo titulo mide exactamente 31 caracteres, y **ocho** de ellas estan
VIVAS y son CANONICAS de la tabla de `OP-S-11`"*. **Y LA PROPIA FRASE ENUMERA
SIETE NOMBRES DEBAJO DE LA PALABRA OCHO**, entre parentesis y en el mismo
renglon: `Change by Design, Revised and U`, `Co-Intelligence_ Living and Wor`,
`Juran's Quality Handbook_ The C`, `Managing the Risks of Organizat`, `The Field
Guide to Understandin`, `The Green to Gold Business Play` y `Guia de empaque
para transporte`. **La cifra se contradice con su lista sin salir del renglon.**

**LO MEDIDO POR MI HOY, Y NO COPIADO DEL ACTA** (`EJECUTOR.md` 2):
`scripts/loop/vuelta147_3a_truncacion_dos_unidades.py`, salida en
`docs/loop/SALIDA_V147_3A_TRUNCACION_DOS_UNIDADES.txt`. El instrumento **no
reimplementa nada**: importa `partir` de
`vuelta146_1c_cifras_ficha_op_a_01.py`, que es el mismo particionador con el que
la 146 hizo su censo, y `cargar_tabla` de `vuelta136_simular_ops11.py`, que
parsea `OP_S_11_MAPEO_PROPUESTO.md` tal como esta escrita.

**LAS DOS UNIDADES, ESCRITAS ANTES DE CORRER NADA.** **(A) LA SOLA LONGITUD:**
`len(titulo) == 31`, con titulo el segmento anterior al primer ` - `. Es la que
uso la 3.f de la vuelta 146. **(B) EL DETECTOR VIGENTE DE LA CAMPANA:**
`len(titulo) == 31` **CON RESTO NO VACIO**.

**LA CIFRA CORREGIDA, sobre `dataset/metadata/master_graph.json` (WORK, 3.853
nodos, 67 grafias distintas del campo `fuente` en cualquier posicion), contada
de `docs/loop/SALIDA_V147_3A_TRUNCACION_DOS_UNIDADES.txt`:**

```
CIFRA grafias de 31 por la sola longitud WORK: 10 grafias
CIFRA grafias de 31 por la sola longitud vivas y canonicas WORK: 7 grafias
CIFRA grafias de 31 por el detector vigente WORK: 9 grafias
CIFRA grafias de 31 por el detector vigente vivas y canonicas WORK: 6 grafias
```

**LAS DOS NOMINAS ENTERAS.** Por **LA SOLA LONGITUD**, las **diez**, con sus
vivos y sus deprecados, y **siete** de ellas vivas y canonicas:

```
      Change by Design, Revised and U - Tim Brown          vivos=73   depre=5    [VIVA y CANONICA]
      Co-Intelligence_ Living and Wor - Ethan Mollick      vivos=39   depre=12   [VIVA y CANONICA]
      Essentials of Supply Chain Mana - Michael H. Hugos   vivos=0    depre=1    [ni viva ni canonica]
      Guia de empaque para transporte                      vivos=1    depre=0    [VIVA y CANONICA]
      Juran's Quality Handbook_ The C - Joseph A. Defeo    vivos=459  depre=111  [VIVA y CANONICA]
      Managing the Risks of Organizat - Reason, J. T_      vivos=90   depre=22   [VIVA y CANONICA]
      The Field Guide to Understandin - Dekker, Sidney     vivos=102  depre=1    [VIVA y CANONICA]
      The Field Guide to Understandin - Dekker, Sidney;    vivos=0    depre=15   [ni viva ni canonica]
      The Green to Gold Business Play - Daniel C. Esty     vivos=209  depre=33   [VIVA y CANONICA]
      The Hard Thing About Hard Thing - Ben Horowitz       vivos=0    depre=5    [ni viva ni canonica]
```

Por **EL DETECTOR VIGENTE**, las **nueve**, y **seis** de ellas vivas y
canonicas. **La diferencia entre las dos unidades es UNA SOLA GRAFIA, nombrada
por el instrumento**:

```
  LA DIFERENCIA ENTRE LAS DOS UNIDADES, NOMBRADA UNA A UNA: 1 grafia(s)
      Guia de empaque para transporte  titulo de 31 car, RESTO VACIO
```

Los tres bloques de arriba salen de
`docs/loop/SALIDA_V147_3A_TRUNCACION_DOS_UNIDADES.txt`.

**EL SEGUNDO CAMINO, INDEPENDIENTE Y QUE NO PASA POR EL GRAFO:** la tabla
canonica leida directamente. De sus **129 filas** salen **54 canonicas
distintas**, y de esas, **siete** tienen titulo de 31 por la sola longitud y
**seis** por el detector vigente. **Los dos caminos dan lo mismo**, contado de
la misma salida:

```
CIFRA canonicas distintas de la tabla OP-S-11: 54 grafias
CIFRA canonicas de 31 por la sola longitud: 7 grafias
CIFRA canonicas de 31 por el detector vigente: 6 grafias
```

**CUAL ES LA UNIDAD QUE GOBIERNA Y POR QUE, CON LA CITA DEL DETECTOR DELANTE.**
**Gobierna (B), el detector vigente**, y no lo decide esta correccion: lo decide
el registro. Esta escrito en `docs/PENDIENTES.md`, **DECIMA entrada** (vuelta
132, corregido en la vuelta 131 sobre el discutible del acta 130 y re-medido en
la vuelta 134), y **nombra a su falso positivo por su nombre**:

> *"El detector mecanico de truncamiento vigente, corregido en la vuelta 131
> (acta 130, discutible del 130) y medido de nuevo hoy: `len(titulo) == 31` CON
> RESTO NO VACIO. La sola longitud fichaba un falso positivo, `Guia de empaque
> para transporte`, titulo completo sin autor, RESTO vacio, que no esta
> truncado: simplemente su titulo real mide 31 caracteres."*

Y esta escrito ademas **en el codigo desde la vuelta 131**:
`scripts/loop/vuelta131_residuo_para_decision.py`, funcion `es_truncada`, que
dice `len(titulo_de(g)) == 31 and bool(resto_de(g))`. **La 3.f de la vuelta 146
uso la sola longitud y metio a `Guia de empaque para transporte` en la cuenta,
diciendolo entre parentesis en la misma frase.**

**LA CIFRA QUE QUEDA, ENTONCES: por la unidad que gobierna, NUEVE grafias de
titulo de 31 y SEIS vivas y canonicas.** Por la unidad que la 146 uso, **DIEZ y
SIETE**. **La palabra OCHO no sale de ninguna de las dos.**

**MI MEDICION NO DISCREPA DE LA DEL ACTA 146 EN NINGUNA DE LAS CUATRO CIFRAS**
(siete y seis por sus dos unidades, nueve y diez por las suyas). Lo declaro
porque `EJECUTOR.md` 2 obliga a declarar el contraste, coincida o no.

**LO QUE ESTA CORRECCION NO HACE, Y ES LA MITAD IMPORTANTE.** **No toca el
dataset, no toca la tabla, no toca una grafia y no toca
`docs/plan/OPERACIONES.jsonl`.** No mueve un nodo, no mueve una arista y no
mueve una ficha. **Y EL HALLAZGO DE FONDO DE LA 146 SIGUE EN PIE Y NO SE
RETIRA: la truncacion a 31 esta HORNEADA EN LA TABLA CANONICA**, y eso lo
demuestra el segundo camino de arriba, que ve **seis canonicas truncadas sin
mirar el grafo**. **Lo que fallaba era la cuenta y la unidad, no la idea.** Que
hacer con una tabla canonica que hornea titulos recortados **queda registrado
para quien cierre la fase 08**, y no es decision de esta vuelta.

---

## CORRECCION 26. **EL UMBRAL DE LA COLA EXISTE, TIENE NOMBRE, TIENE DOS NUMEROS Y TIENE MOTIVO ESCRITO**

**Vuelta 147, TAREA 1.c, sobre la caida 4.2 del acta del auditor de la vuelta
146 (de REPORTE, y ACUMULA).** Corte: **2 sep 2026**. **NO SE BORRA NI SE
ESCONDE LA FRASE QUE SE CORRIGE.**

**LA FRASE CORREGIDA, CITADA VERBATIM DE SU COMMIT Y NO REESCRITA.** Es la
cabecera de la PREGUNTA 2 del reporte de la vuelta 146 y su conclusion, tal como
se commitearon. El bloque va con su ref y su ruta en la propia marca, que es el
patron de la CITA CONGELADA, y el ref es **un hash y no `HEAD`**, porque un ref
movil no congela nada:

<!-- CITA CONGELADA 723b4639:docs/loop/REPORTE.md -->
```
**PREGUNTA 2. EL UMBRAL DE LA COLA NO TIENE NUMERO EN NINGUNA PARTE.** `OP-A-02` lo
cita por referencia y el barrido no halla ninguna constante que lo fije. Sin ese numero
la puerta semantica no se puede cablear. **Cual es, y de donde se lee.**
```
<!-- FIN CITA CONGELADA -->

**LO QUE HAY DE VERDAD, LEIDO POR MI DEL CODIGO Y NO DEL ACTA.**
`scripts/intra_dominio.py`:

  - **linea 60: `UMBRAL_TITULO = 80`**. Es el umbral de parecido de titulo
    (`token_sort_ratio` de rapidfuzz).
  - **linea 68: `UMBRAL_SEMANTICO = 0.78`**.

**Y TIENE MOTIVO ESCRITO EN EL PROPIO CODIGO**, en el comentario que va entre
las dos constantes: dice que el semantico se **BAJO DE 0.80 A 0.78 para el
cribado completo**, y da la medicion que lo justifica: las **DOS parejas ya
adjudicadas** que la corrida a 0,80 perdia viven en **0,7890**
(`accion_correctiva_4` con `accion_correctiva_sistematica`) y **0,7887**
(`cadencia` con `gestion_seguimiento_prospectos`); y los pares que entran por esa
rebaja van marcados con `banda_078_080` para poder contarlos aparte.

**UNA DISCREPANCIA MENOR CON EL ACTA, DECLARADA Y NO RESUELTA COPIANDO**
(`EJECUTOR.md` 2): el acta 146 dice *"con doce lineas de calibracion encima"*.
**Contadas por mi hoy sobre el fichero, el comentario de calibracion que va
encima de `UMBRAL_SEMANTICO` son SIETE lineas, de la 61 a la 67.** Las tres
lineas de comentario anteriores (56 a 58) son las de `MARCA_MANUAL` y no hablan
del umbral. **La discrepancia no cambia ningun veredicto: las dos constantes,
sus dos lineas y su motivo son exactamente los que el acta nombra.**

**POR QUE ES EL UMBRAL DE LA COLA.** La ficha de `OP-A-02` dice que *"el umbral
de la cola es el mismo del cribado intra"*, y `scripts/intra_dominio.py` **ES**
el cribado intra. **La consecuencia que importa: la puerta semantica `A2.6` SI se
puede cablear, y el bloqueo que la PREGUNTA 2 declaraba no existe.**

**POR QUE MI BARRIDO NO LO HALLO, ESCRITO SIN ADORNO, PORQUE ES EL CORAZON DE LA
ESCALADA DE LA VUELTA 147.** El barrido de la 3.e de la 146
(`docs/loop/SALIDA_V146_3E_BARRIDO_UMBRAL.txt`) tenia **las cinco piezas del
sello completas** y **`scripts/intra_dominio.py` estaba DENTRO de su universo**
(1.482 ficheros de `scripts/`, `engine/` y `web/`). Fallo por sus dos piernas:

  - **LA PIERNA POR NOMBRE era `umbral|cola`**, y el fichero **se llama
    `intra_dominio.py`**, o sea por su operacion y no por su constante. Es la
    misma forma en que la caida de la 145 no hallo
    `OP_S_11_MAPEO_PROPUESTO.md`.
  - **LA PIERNA POR CONTENIDO eran TRES NOMBRES DE CONSTANTE ADIVINADOS**,
    `UMBRAL_DE_LA_COLA`, `UMBRAL_COLA` y `umbral_de_la_cola`, **ninguno de los
    cuales existe en ninguna parte del repositorio**. **La constante real se
    llama `UMBRAL_SEMANTICO`.**

**ESO ES LO QUE LA TAREA 2 DE LA VUELTA 147 VIENE A IMPEDIR**, y no con prosa:
`barrer_ausencia.py` publica desde hoy **la SEXTA PIEZA del sello, la VITALIDAD
DE LOS PATRONES DE CONTENIDO** (cuantas de las alternativas del patron aparecen
en el universo), y `verificar_ausencias_del_reporte.py` **rechaza un barrido
cuyas alternativas de contenido esten TODAS muertas**. **Corrida sobre el sello
del umbral de la 146 congelado en su commit, la guarda sale ROJO nombrando las
tres cadenas muertas**, y sobre el mismo barrido **rehecho por el CONCEPTO**
(`umbral|similitud`) sale VERDE y **halla `scripts/intra_dominio.py`**. Las dos
salidas estan en `docs/loop/SALIDA_V147_2C_MUTACION_VITALIDAD.txt` y
`docs/loop/SALIDA_V147_2D_BARRIDO_UMBRAL_REHECHO.txt`.

**LO QUE ESTA CORRECCION NO HACE:** no toca `docs/plan/OPERACIONES.jsonl`, no
toca la ficha de `OP-A-02` y no toca una sola grafia del campo `fuente`.
"""


def main():
    with io.open(RUTA, encoding="utf-8") as f:
        antes = f.read()
    if "## CORRECCION 25." in antes:
        raise SystemExit("ROJO PREVIO: la CORRECCION 25 ya esta escrita, no se duplica")
    with io.open(RUTA, "a", encoding="utf-8", newline="\n") as f:
        f.write(TEXTO)
    with io.open(RUTA, encoding="utf-8") as f:
        despues = f.read()
    assert despues.startswith(antes), "ROJO: la escritura NO fue por adicion pura"
    print("CORRECCIONES 25 y 26 anadidas por ADICION PURA. El fichero viejo es prefijo "
          "exacto del nuevo.")
    print("CIFRA lineas antes: %d lineas" % len(antes.splitlines()))
    print("CIFRA lineas despues: %d lineas" % len(despues.splitlines()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
