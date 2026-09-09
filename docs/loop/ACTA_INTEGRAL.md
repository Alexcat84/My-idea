# ACTA INTEGRAL DE CIERRE DE CAMPAÑA (9 sep 2026)

**Auditor integral, con el fundador delante.** Se escribe POR ANEXION conforme
avanza, no al final. Toda cifra sale de un instrumento corrido en esta sesion;
toda cita lleva su linea. Mapa de herencias: `docs/loop/PARA_ALEXIS.md`
(248 lineas, cierre del bucle del 9 sep 2026).

**Estado de partida, medido:** rama `pasada-unica`, HEAD `6dbfb9c0`, arbol
limpio, `origin` sin diferencia.

---

## PASO 0. HIGIENE: EL TURNO RESIDUAL DEL CORTE, CERRADO

`python scripts/loop/apertura_del_auditor.py --cerrar-turno --vuelta "220-cola"`
corrido en esta sesion. Salida literal: *vuelta registrada en cerrados: 220-cola;
el fichero del turno NO se borra; un turno NUEVO lo cargara como CERRADO y
empezara limpio SIN borrar nada*. Vueltas cerradas en el fichero tras el acto:
`206 ... 220, 220-cola`.

**Un matiz que se dice en vez de callarlo:** `--estado` sigue diciendo
`TURNO VIVO ABIERTO: SI` despues del cierre. Es el diseño declarado por el propio
instrumento (el fichero no se borra; el turno nuevo lo carga como cerrado), no un
fallo del cierre. Arbol limpio antes y despues.

---

## PASO 1. LAS DECISIONES DEL FUNDADOR, Y LO MEDIDO ANTES DE APLICARLAS

### 1.a LAS CLAUSULAS A MEDIAS: DOS LIBROS DISTINTOS, MEDIDOS

**El lector de las 17 clausulas** (`docs/loop/SALIDA_V220_T1_RECORRIDA_DEL_LECTOR.txt`,
lineas 238 a 254, filas 0 CODIGO a 07 ADUANA) deja **tres** en A MEDIAS:

| fila | fase | idx | clausula |
|---:|---|---:|---|
| 6 | `03 FUSIONES` | 0 | un superviviente por acto, el resto DEPRECADO CON ALIAS |
| 11 | `05 SANEO` | 1 | los tres de Incoterms con su version |
| 17 | `07 ADUANA` | 0 | los cuatro controles mecanicos corriendo en Gate 0 |

**Y la ficha `OP-I-01` tiene su propio libro de cuatro puntos** (leidos de
`docs/plan/OPERACIONES.jsonl`): idx 0 fecha_corte, idx 1 PROVISIONAL, idx 2
*todo hueco NOMBRADO, nunca rellenado*, idx 3 *el inventario se recomputa entero
con el disparador*. La correccion de la vuelta 214 (misma ficha, campo
`evidencia`) los re-midio: **2 en CUBRE, 2 en A MEDIAS (idx 2 y idx 3)**. El idx 3
es **la vista humana** (`docs/plan/10_INVENTARIO.md`), que en su linea 19 declara
*LA TABLA NO SE REGENERA AQUI, A PROPOSITO*. Desde la vuelta 214 la pagina 08
tiene filas 08, 09 y 10, y la fila 10 son esos cuatro puntos.

**LA CIFRA DE 03 FUSIONES idx 0, donde se midio por primera vez:** acta 217,
linea 77344: *71 actos sin fundir de 335 del corte vigente (19 nodos en las SEIS
fusiones que la remision de la fase 03 dejo enrutadas)*.

**LA CIFRA DE 07 ADUANA idx 0, medida en esta sesion y no citada:** la ficha
`OP-A-02` v4 nombra CINCO controles mecanicos. Cotejados contra las 26
comprobaciones de Gate 0 (`docs/loop/SALIDA_V220_GATE0_CMD1_CIERRE.txt`):

| control de OP-A-02 v4 | comprobacion de Gate 0 que lo corre |
|---|---|
| auto-arista con resolucion | `Ningun nodo VIVO se cita a si mismo tras RESOLVER` |
| lista blanca de claves | `Ninguna clave de nodo fuera de la lista blanca del esquema` |
| control posicional del campo fuente | `OP-A-01: todo nodo VIVO con MAS DE UNA fuente pasa la comprobacion posicional` |
| campo fuente canonico | `OP-A-01 / OP-A-02 (A2.4): el campo fuente resuelve contra la lista CANONICA` |
| **revision de nomina por dominio** | **NINGUNA por ese nombre** (la mas cercana, *la nomina adjudicada de la aduana no se movio sin declararse*, no es por dominio) |

**El quinto control es la revision de nomina por dominio.** Y la fila 07 de la
pagina 08 (linea 30) dice CUATRO donde la ficha dice CINCO: es la divergencia que
la cola de siete lleva como entrada 2.

**PENDIENTE DE PREGUNTA AL FUNDADOR (se para aqui, por su orden):** su letra
nombra `05 SANEO idx 1` y `OP-I-01 idx 3` como dos de *las tres*; el lector de las
17 tiene otras dos ademas (`03 FUSIONES idx 0`, `07 ADUANA idx 0`) y `OP-I-01`
tiene ademas su idx 2. Son **cinco** items a medias en dos libros, no tres. Se
pide alcance antes de escribir nada en el plan.

### 1.b LA BATERIA: LA NOMINA Y LOS NUEVE ARNESES, MEDIDOS

`scripts/loop/verificar_mutaciones_viejas.py` trae **154** entradas literales
`vuelta*.py` en su texto (contadas con regex en esta sesion); la nomina corrida
en la 220 fue de **135** exactamente una vez, 270 corridas. Los **siete que no
muerden**, con su tramo, leidos de `docs/loop/SALIDA_V220_T2_BATERIA.txt` lineas
112 a 120:

| tramo | arnes | lineas |
|---:|---|---:|
| 3 | `vuelta160_tarea6b_mutacion_puerta.py` | 303 |
| 5 | `vuelta165_tarea6_mutacion_op_l_01.py` | 174 |
| 5 | `vuelta166_tarea2_mutacion_correccion.py` | 267 |
| 5 | `vuelta168_tarea1_mutacion_nota.py` | 24 |
| 6 | `vuelta168_tarea2_mutacion_reconstructor.py` | 24 |
| 6 | `vuelta171_mutacion_busqueda_acta.py` | 172 |
| 9 | `vuelta185_tarea1c_mutacion_bateria_continuada.py` | 264 |

Los **dos fuera de la nomina** (lineas 122 a 125 de la misma salida):
`vuelta197_tarea2_mutacion_orden_del_turno.py` (423 lineas) y
`vuelta199_tarea1_mutacion_guardas_revividas.py` (442 lineas). Su medicion uno a
uno se anexa en cuanto corran.

### 1.b (continuacion) LOS NUEVE, CORRIDOS UNO A UNO, Y LO QUE SE HIZO CON CADA UNO

**Los dos fuera de la nomina, corridos tal cual en esta sesion:**

| arnes | exitcode | veredicto impreso |
|---|---:|---|
| `vuelta197_tarea2_mutacion_orden_del_turno.py` | 0 | VEREDICTO: VERDE |
| `vuelta199_tarea1_mutacion_guardas_revividas.py` | 0 | VEREDICTO DEL ARNES: VERDE |

Legitimos los dos (cada uno prueba una pieza viva de `apertura_del_auditor.py`
y trae su mutacion), **ENTRAN en la nomina**: `VIEJAS` pasa de 135 a 137,
`arneses_que_faltan()` devuelve vacio e `nomina_invisible_al_censo()` devuelve
vacio, medidos importando el fichero tras el parche.

**Los siete que no muerden, corridos uno a uno ANTES de tocar nada** (los siete
exitcode 1) **y diagnosticados leyendo su codigo y git, no su rotulo.** El rojo
de un arnes de mutacion puede ser dos cosas opuestas: la guarda que no muerde
(el mutante no cae) o el sujeto que se movio (el arnes ya no puede probar lo que
probaba). **Los siete eran sujeto movido**, en tres especies:

| arnes | lo que imprimia | causa medida | reparacion |
|---|---|---|---|
| `vuelta160_tarea6b_mutacion_puerta.py` | `no se hallo el acta 159 en la rama` | busca el asunto en `git log -n 500`; el acta 159 (`13cf21be`) esta a **641** commits de HEAD | se lee la rama entera |
| `vuelta168_tarea1_mutacion_nota.py` | `commits que empiezan por 'ACTA DE LA VUELTA 167': 0` | ventana `-400` en `vuelta168_tarea1_adosar_nota_r36.py`; el acta 167 (`e3152a9c`) esta a **541** | se lee la rama entera |
| `vuelta168_tarea2_mutacion_reconstructor.py` | `... 'ACTA DE LA VUELTA 165': 0` | ventana `-400` en `vuelta168_tarea2_reconstruir_166_167.py`; el acta 165 (`00cfe6e0`) esta a **556** | se lee la rama entera |
| `vuelta171_mutacion_busqueda_acta.py` | `F_y_es_el_commit_d7b18370 FALLA (real='')` | ventana `-400`; `d7b18370` esta a **513** | se lee la rama entera |
| `vuelta165_tarea6_mutacion_op_l_01.py` | `C_tiene_seis_clausulas FALLA (real=7)`, `C_tres... (real=4)`, `C_sigue_en_LISTA (real='HECHA')` | la ficha paso a 7 clausulas y 4 declaradas en la vuelta 203 (`169a2ff6`) y a HECHA en la 209 (`1a3d6d54`), trazado con `git log` sobre `OPERACIONES.jsonl` | tercer re anclaje, con el motivo escrito y los dos anteriores intactos; el caso sigue siendo igualdad exacta |
| `vuelta166_tarea2_mutacion_correccion.py` | `F_mover_el_estado_tumba_el_invariante_4 FALLA (real=True)` | la mutacion escribia `HECHA` sobre una ficha que ya esta en HECHA: no era mutacion | el estado se mueve siempre a un valor distinto del que tiene hoy |
| `vuelta185_tarea1c_mutacion_bateria_continuada.py` | bloque F: los once tramos dan `vuelta 220`, reparto 4 y 5 `NO` | `tramos_por_vuelta(183)` lee el ultimo commit de cada fichero en HEAD y la 220 los volvio a sellar todos | `cerrar_reporte.tramos_por_vuelta` gana `ref=None` (con `None`, conducta identica); el arnes clava el commit del tramo 9 de la 184 leido de git por su asunto (`3500db9d`, exactamente uno) y lee el reparto EN ese commit |

Los cuatro primeros son **una sola caida en cuatro cuerpos**: una ventana
contada sobre git que la propia rama dejo atras. Y las profundidades dicen
cuando empezo a fallar cada uno: el de la 171 al pasar de 400 commits desde
`d7b18370`, mucho antes de la 220.

**Las siete reparaciones, corridas una a una despues del parche:**

| arnes | exitcode | segunda pasada (el esperado mutado cae) |
|---|---:|---|
| `vuelta160_tarea6b_mutacion_puerta.py` | 0 | VERDE: los 4 se comportan |
| `vuelta165_tarea6_mutacion_op_l_01.py` | 0 | 16 pasan, 16 caen al mutar |
| `vuelta166_tarea2_mutacion_correccion.py` | 0 | 20 pasan, 20 caen al mutar |
| `vuelta168_tarea1_mutacion_nota.py` | 0 | 14 pasan, 14 caen al mutar |
| `vuelta168_tarea2_mutacion_reconstructor.py` | 0 | 17 pasan, 17 caen al mutar |
| `vuelta171_mutacion_busqueda_acta.py` | 0 | 16 pasan, 16 caen al mutar |
| `vuelta185_tarea1c_mutacion_bateria_continuada.py` | 0 | reparto 4 y 5 sobre nueve SI; mutados (5 y 4) CAE, (nueve por la 183) CAE; CIFRA fallos: 0 |

**Ninguno se retira.** Los siete se repararon barato y con su mutacion probada
por la segunda pasada de cada arnes. Una caida propia de esta sesion, declarada:
el primer parche de `cerrar_reporte.py` dejo un parentesis sin cerrar
(`SyntaxError` en la linea 389 al importar); se cerro y el arnes 185 se volvio a
correr desde cero. El fichero sellado
`docs/loop/SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt` queda con la corrida
reparada (el arnes escribe en esa ruta fija); los sellos de 197 y 199 se
restauraron a HEAD porque sus arneses ya la habian escrito igual en su vuelta.

**Doctrina escrita:** `docs/loop/AUDITOR.md` 6.3 lleva la congelacion en 135
tachada con su correccion declarada (9 sep 2026), y nace **6.4 REGIMEN POST
BUCLE DE LA BATERIA** (nomina abierta que llena el censo, cuando corre, las dos
especies del rojo, reparar barato o retirar con motivo, ninguna ventana contada
sobre git, la salida sellada con el nombre de la sesion). La entrada de la
nomina en `verificar_mutaciones_viejas.py` dice lo mismo en su sitio.

**La bateria entera con la nomina de 137** se corre en el PASO 2.b con su
sello `_integral_`; aqui solo se midieron los nueve uno a uno.

### 1.d LA COLA DE SIETE, LEIDA DEL ACTA 219

Seccion 6, lineas 78024 a 78066, las siete con su numero. Se resuelven o se
remiten con ficha en el apartado correspondiente de esta acta; ninguna queda sin
linea.
