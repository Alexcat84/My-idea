# -*- coding: utf-8 -*-
"""Pega el registro de cierre de OP-D-09 en 02_DESTEJIDOS.md, con el bloque
sellado IMPRESO y no retecleado (EJECUTOR.md regla 1)."""
import io

salida = io.open('docs/loop/SALIDA_V45_CIERRE_OPD09.txt', encoding='utf-8').read().rstrip('\n')

CAB = u"""

## `OP-D-09`: **LA PLANIFICACION DE RECOLECCION DE DATOS, DESTEJIDO SOLO** (19 ago 2026, vuelta 45)

**Va SEGUNDA y con orden libre**, porque **libera CERO congelados** y el criterio de la fase es
CONGELADOS LIBERADOS: el precedente escrito es `OP-D-05`, que **sin congelados tiene orden libre
respecto de las demas**. **DESTEJIDO SOLO**, un solo nodo, `aristas_nuevas` **VACIO**, y **el censo
no se mueve**, asi que el ciclo de Gate 0 vuelve a ser de **TRES** comandos.

**Es la unica de las 46 costuras confirmadas que NO es del nucleo** (45 nucleo y 1 `quality`), y
**la ficha ya dejo escrito el dato que vale mas que la excepcion**: tiene 16 pasos, o sea que **el
unico nodo de mundo con costura confirmada es un nodo LARGO**. **Ese dato se hereda y no se gasta
aqui**: la medicion que la ficha encarga (normalizar la tasa de costura por longitud) **no es de
esta operacion ni de esta fase**, y se deja nombrada para que no se pierda al cerrar el destejido.

### EL REPARTO: EL INDICE SON TRES PASOS Y NO CUATRO

**La ficha del gradiente decia *destejido facil, hay que quitar un indice que se colo como pasos*, y
sigue siendo facil; lo que no es es de cuatro.** La correccion la midio la vuelta 17 y esta vuelta
la ejecuta: **el paso 1 NO se poda, se REPARTE.**

| | que pasa | y por que, con la regla citada |
|---|---|---|
| **paso 1** | **SOBREVIVE VERBATIM Y DE PRIMERA**, como cabecera del metodo | **no tiene casa en el metodo de 5 a 16**: ninguno de sus doce pasos formula la pregunta. Por la **REGLA DE REPARTO** de la fase (la perdida sin bloque va **al superviviente**) se queda. Y hay motivo interno ademas del formal: **el paso 14, que sobrevive, apunta al PROBLEMA TECNICO ORIGINAL que solo el paso 1 establece**; podarlo dejaria al 14 apuntando a algo que el nodo ya no dice. **El propio `resumen_teorico` lo dice igual**: *empezar con el fin en mente, trabajando hacia atras DESDE LA PREGUNTA* |
| **paso 2** | **se va como linea**, y viaja con el **paso 9 del metodo** | *decidir QUE medir considerando como se comunicaran y analizaran los datos*: **el analisis lo hace el 9** (filtrar y analizar) **y la comunicacion la hace el 15** (presentar en informe claro con resumen ejecutivo). **No deja resto sin casa** |
| **paso 3** | **se va como linea**, y viaja con el **paso 7 del metodo** | *decidir COMO medir la poblacion o muestra (herramienta, estrategia de muestreo, tamano)*: **el 7 disena, prepara y PRUEBA metodos, formularios e instrucciones**, y **la mitad del tamano de muestra la dice ademas el 10**. **No deja resto sin casa** |
| **paso 4** | **se va como linea**, y viaja con el **paso 6 del metodo** | *recolectar los datos con MINIMO SESGO*: **el 6 selecciona y capacita recolectores IMPARCIALES**, que es donde el sesgo se ataca de raiz y no como advertencia, **con el 5 y el 8 de respaldo**. **No deja resto sin casa** |
| **pasos 5 a 16** | **NO SE TOCAN**, verbatim, contiguos y en orden | son **el metodo completo**, que es el cuerpo del nodo |

**Cada uno de los tres se comprueba EN SU CASA ANTES de quitarlo y no despues, que es lo que el
`eliminar` de la operacion exige, y la comprobacion SE VE EN EL MAPA**, que es donde se puede
auditar. **Ninguno abre paso nuevo porque ninguno deja resto.**

**LAS DOS ANCLAS INTOCABLES, VERBATIM Y EN SU SITIO RELATIVO:** el **paso 7**, ancla del **UNICO**
veredicto de este nodo en todo el cribado (el **2695**), **con su MSA dentro palabra por palabra**;
y el **paso 10**, ancla de las **DOS** candidatas paso a nodo hacia `analisis_pareto` y
`analisis_pareto_proyectos_elefante`, que **siguen sin escribirse y NO se escriben aqui**.

### EL CASO POSITIVO Y LAS GUARDAS

| | ANTES | DESPUES |
|---|---|---|
| **A1** el indice que se colo como pasos ya no esta | **CAE**: siguen los pasos **2, 3 y 4** | **PASA**: **CERO** |
| **A2** el nodo es un metodo y no un resumen mas un metodo | **CAE**: son **16** | **PASA**: **13** |
| | **0 PASAN y 2 CAEN** | **2 PASAN y 0 CAEN** |

**Y LAS NUEVE INVARIANTES EN `OK` LAS DOS VECES:** **5 = 5** vecinos (2 previos y 3 siguientes),
**16.898 = 16.898** entradas de arista, el **paso 7 con su MSA**, el **paso 10**, el **paso 14 sin
quedar colgando** (porque la pregunta del paso 1 sigue en pie), las **tres** piezas del entregable
(preguntas, muestreo y presentacion), la fuente, las **2** condiciones y **el desajuste 17 contra 16
sin rellenar**.

**Guardas del destejedor verdes:** **16 de 16 prefijos calzan**, **cero perdida con 16 origenes
cubiertos de 16**, procedencia completa, fuente sin cambio. **Simulacion previa sobre copia en
memoria antes de escribir nada.** **Gate 0 de TRES comandos** con `GATE 0: OK`, sus **VEINTE**
renglones en `[OK]` y cero rojos, **71** etiquetas, **seis** assets, las dos copias del grafo byte
iguales (md5 `0a92344492de54381d83a2c58e69ebc7`), y **el comando 4 sin correr porque el censo no se
movio** (**3.524 activos y 329 deprecados**, los mismos). **Suites:** motor **25 de 25**, web
**1.030** pasadas y 3 saltadas, `tsc` **cero lineas**.

### EL BLOQUE DE CIERRE, PEGADO ENTERO Y SIN RETECLEAR

```
"""

PIE = u"""```

### LA RELECTURA DEL 2695, Y EL RIESGO QUE LA OPERACION ANUNCIO

**La operacion escribio su propio aviso y hay que contestarlo de frente:** *quien lea el diseno del
metodo como el paso 7 del plan subsumido dira `A` por contencion; tras quitar el indice el plan
queda MAS parecido a un metodo y menos a un resumen, o sea que **el riesgo de contencion SUBE**. Si
tras el destejido el 2695 se vuelve `A`, **eso es un resultado de la operacion y se escribe**, no un
fallo de la cirugia.*

**RELEIDO HOY CON LOS DOS TEXTOS DELANTE: SIGUE DANDO `D`, y la vara es medida y no de gusto.**

| la prueba | lo medido |
|---|---|
| **la prueba de madre e hijo del `9.6.2`** | pide que **el hijo quepa ENTERO dentro de UN paso de la madre**. **NO CABE**: sus cinco pasos se derraman sobre **TRES** pasos distintos del plan (el **2**, el **4** y el **5**) |
| **material propio del hijo** | su **paso 3** (*determinar que informacion adicional necesitas para poder RASTREAR o analizar mas adelante*) **no tiene casa en ninguno de los trece pasos del plan**. El hijo **anade**, no solo profundiza |
| **los entregables** | el plan entrega **un plan documentado** con preguntas, muestreo y presentacion; el otro entrega **formularios y procedimientos probados y validados, LISTOS PARA USAR**. **No son intercambiables** |
| **el alcance** | el plan va **de formular la pregunta hasta generalizar las conclusiones a otros problemas** (13 pasos); el hijo cubre **solo el tramo de disenar y validar** |

> **Y SE DICE LO QUE LA MEDICION CONTRADICE DEL AVISO, en vez de darle la razon por cortesia: EL
> RIESGO DE CONTENCION NO SUBIO, BAJO.** El aviso suponia que quitar el indice acercaria los dos
> textos. **Medido: el paso del indice que MAS se solapaba con el objeto del hijo era el 3** (*decidir
> COMO medir: herramienta, estrategia de muestreo, tamano*), **y ese es justamente uno de los tres que
> se fueron**. Quitarlo **elimino una de las dos superficies de solape**, no la agrando. **El aviso
> era razonable a priori y la medicion apunta al otro lado; se publican los dos.** **VA COMO
> DISCUTIBLE MARCADO.**

**ARISTA QUE FALTA, declarada para la fase 04:** buscada hoy **en los dos sentidos** contra el grafo
(regla 9), **no existe ninguna de las dos**. La razon del propio 2695 declara una **jerarquia** (el
diseno del metodo **profundiza** un paso del plan), y la regla escrita de la cola de relectura dice
que **una `D` con jerarquia SE ENLAZA**. **Se suma a las del 599 y el 233.** **El par 784 de `OP-D-08`
no entra en esa lista porque su arista ya existia.**

> **UNA CITA QUE QUEDA RANCIA EN UN DETALLE, DECLARADA Y NO REESCRITA**, con el precedente del acto
> 711 de `OP-D-06`, que hizo exactamente esto con una razon suya: la razon del **2695** nombra su
> ancla como **el paso 7** del plan, y **tras el destejido ese mismo texto es el paso 4**. **El texto
> del ancla es identico palabra por palabra** (*disenar, preparar y probar metodos, formularios e
> instrucciones de recolucion, incluir MSA*); **lo que se movio es el numero, no la linea**. **No se
> reescribe la razon**: una cita rancia declarada se puede auditar, una cita corregida por dentro no.

**El veredicto NO cambia de clase, asi que NO se toca `INTRA_DOMINIO_VEREDICTOS.jsonl`** y **el
marcador no se mueve por esta operacion**: se queda en **A 575, B 79, C 8, D 2.726** sobre **n
3.388**, el estado que dejo la relectura del 784 en `OP-D-08`.

### LA SENAL DE COSTURA, Y AQUI NO CAE

**Re-corrido `scripts/costuras_internas.py` tras el acto:** el nodo pasa de **16 pasos con bloque
56,7 y corte tras el 14** a **13 pasos con bloque 56,7 y corte tras el 11**. **LA SENAL NO SE MOVIO
NI UNA DECIMA**, y se publica asi en vez de buscarle una lectura amable: **a diferencia del lienzo de
`OP-D-08`, que cayo de 65,6 a 46,0, aqui el destejido no toco lo que el instrumento mide.** Tiene
sentido y no lo arregla: **lo que se quito era el INDICE, y el bloque que la senal detecta esta
DENTRO del metodo**, que es justo lo que esta operacion tenia prohibido tocar. **La senal queda
REGISTRADA COMO CITA y no como veredicto**, por el limite declarado del propio instrumento, **y se
deja escrita como lo que es: una costura que este destejido NO cura y que ninguna operacion abierta
reclama.** **VA COMO DISCUTIBLE MARCADO.**

> **Y UNA CIFRA DE LA PROPIA OPERACION QUE NO CALZA, declarada en vez de copiada (regla 2):** su
> campo `evidencia` dice **senal de bloque 52,3** y **corte mecanico en el 11**. **Medido por mi en la
> apertura, con 16 pasos: bloque 56,7 y corte tras el 14.** El corte **11** que la operacion cita es
> **el que el nodo tiene HOY, con 13 pasos**, no el que tenia con 16. **Las dos cifras escritas son de
> otro corte** (vuelta 17) y **se citan como contraste, no como fuente.** La guarda que si se
> comprueba, **CERO MOVIMIENTO de grafo**, calza al digito.

### LO QUE `OP-D-09` DEJA ABIERTO Y NO SE LLEVA CONSIGO

| que queda | donde va |
|---|---|
| **El desajuste 17 contra 16** del `resumen_teorico` | **NO SE RELLENA. Hueco nombrado**: decidirlo **exige la fuente, que esta fuera del repo**. Queda como guarda `B9` para que nadie lo cierre por descuido |
| **La arista que falta del 2695** | **fase 04**, con las del **599** y el **233** |
| **Las dos candidatas paso a nodo del paso 10** (hacia `analisis_pareto` y `analisis_pareto_proyectos_elefante`) | **fase 04**: siguen **sin escribirse** y esta operacion **no las escribe**, porque su `aristas_nuevas` esta **VACIO** |
| **La costura que la senal sigue citando** (bloque 56,7 dentro del metodo) | **anotada, sin dueno**. **Ninguna operacion abierta la reclama**, y este destejido tenia prohibido tocar el metodo |
| **La medicion de la tasa de costura por longitud** que la ficha encarga | **no es de esta fase**. Se deja nombrada |

### EL REGISTRO DE OPERACION HECHA

**Los SIETE puntos de la `verificacion` estan cumplidos y medidos**, asi que el registro se escribe
**en la nota**, con el campo `estado` **quieto en `LISTA`**. **Misma marca de discutible que
`OP-D-08`**: el encargo pide *registro de cierre* y no dice literalmente *registro de OPERACION
HECHA*; se escribe por la misma vara (*si y solo si todo lo material cumple*) y **el texto viejo
queda entero delante por si el auditor lo quita**.
"""

with io.open('docs/plan/02_DESTEJIDOS.md', 'a', encoding='utf-8', newline='') as fh:
    fh.write(CAB + salida + u"\n" + PIE)
print("OK, seccion de cierre de OP-D-09 pegada")
