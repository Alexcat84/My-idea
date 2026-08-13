# REPORTE del ejecutor del bucle, vuelta 6 (checkpoint 3.000)

**Sesion ejecutora (Sonnet 5). Fecha de reloj: 13 ago 2026. Corte del cribado: puesto 3.000
de 3.388.** Rama activa: `bucle`. Hash final de esta vuelta: `544c021b`.

## Hash y rutas

- **Archivo del cribado:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en **3.000 lineas exactas**,
  puestos 1 a 3.000, **cero huecos (set 1..3000 completo) y cero duplicados** (ni de puesto ni de
  par nodo_a/nodo_b/dominio, verificado con `python scripts/recomputar_marcador.py 3000`).
- **Rutas tocadas esta vuelta:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (75 veredictos nuevos,
  2.926 a 3.000, mas dos correcciones declaradas sin alta ni baja sobre puestos ya registrados:
  2.916 de A a D, y el marcado agregado a 2.922 y a 18 pares mas del tramo 2.901-2.925),
  `docs/loop/REPORTE.md` (este archivo). `docs/plan/` NO se toco, como manda el encargo.
- **Commits de la vuelta:** `9e5dc156` (TAREA 1: correccion 2.916, relectura al doble, marcado),
  `facd7b68` (cribado 2.926-2.950), `20ec558b` (cribado 2.951-2.975), `544c021b` (cribado
  2.976-3.000, checkpoint 3.000).

## TAREA 1: registros de la relectura conjunta y la relectura al doble

### 1.1 La grieta del Consejo de Calidad (2.916): corregida a D

**El par 2.916 (`consejo_de_calidad` contra `consejo_de_calidad_3`) pasa de `~~A~~` a D.**
Verificado contra el grafo, nodos enteros y no titulos, como manda el protocolo: los dos
eslabones que el ejecutor anterior citaba como "gemelos" (2.523 y 2.662) **son contencion
asimetrica, no identidad**. El 2.523 dice textualmente que a `consejo_de_calidad_3` le quedan
"DOS LINEAS" propias tras la fusion y registra **PERDIDA NOMBRADA, motivo DESTINO** (la firma de
una absorcion, no de una identidad); el 2.662 dice que `consejo_de_calidad_3` "VA DENTRO DE"
`consejo_calidad_2`. Con un eslabon de contencion en cada cadena citada, la transitividad no
compone (regla del 2.805, extendida a su forma espejo). **La lectura directa confirma el mismo
lado**: `consejo_de_calidad_3` trae DOS pasos enteros que `consejo_de_calidad` no tiene
(coordinar la repeticion del ciclo, institucionalizar el consejo como estructura permanente) y
`consejo_de_calidad` trae TRES que `consejo_de_calidad_3` no tiene (capacitarse en el metodo,
Pareto, asignar los recursos nombrados). Conjuntos disjuntos, D. Tachado sin borrar en la razon
del jsonl; la razon vieja se conserva entera.

### 1.2 Regla adoptada: la transitividad no compone con contencion, en ninguna direccion

Adoptada tal como la dejo escrita el acta del auditor vuelta 5: **la transitividad compone
cuando los eslabones son IDENTIDADES (gemelos); no compone cuando alguno de los eslabones es
una CONTENCION, vaya en la direccion que vaya** (A contiene a g y B contiene a g no da A=B; A
cabe en H y B cabe en H tampoco). Se aplico explicitamente en el cribado nuevo en dos pares
(2.927, 2.933) donde la cadena de dos A hacia un tercer nodo compartido resulto ser contencion en
verificacion, y el par se leyo directo con la vara del paso entero, dando D en ambos casos.

### 1.3 Relectura al doble del tramo 2.901-2.925: los 25 se sostienen

Releidos los 25 pares con el barrido de familia, sin mirar la razon anterior hasta adjudicar de
nuevo. **Resultado: los 25 se sostienen, salvo el 2.916 ya corregido en la TAREA 1.1.** Cero
cambios adicionales. Marcador del tramo tras la correccion: **1 A (el 2.917, contencion del
kanban) y 24 D, 4,0 %.**

### 1.4 Marcado de discutibles: densidad corregida

El tramo 2.901-2.925 llevaba solo 5 marcas en 25 pares antes de esta vuelta; el auditor senalo
que eso es marcar de menos. Esta vuelta: **el 2.922 recibe la marca que le faltaba** (cita la
transitividad 2.529/2.633 sin cambiar la clase D), **18 pares mas del tramo reciben DISCUTIBLE
MARCADO** con su filo especifico, y el 2.916 recibe marca fuerte explicita citando el contrapeso
del auditor. **Densidad final del tramo 2.901-2.925: 25 de 25 marcados.** Los tres tramos nuevos
de cribado (2.926-3.000) se marcaron **100 % desde el registro inicial**, no como correccion
posterior. **Los 100 pares de 2.901 a 3.000 llevan DISCUTIBLE MARCADO inline, 28 con la marca
fuerte.**

## TAREA 2: cribado 2.926 a 3.000 (75 pares nuevos)

### Marcador recomputado del archivo (corte 3.000, 3.000 veredictos, cero huecos, cero duplicados)

| clase | conteo | porcentaje |
|---|---:|---:|
| A | **578** | 19,3 % |
| B | 89 | 3,0 % |
| C | 7 | 0,2 % |
| D | **2.326** | 77,5 % |

Contra el checkpoint 2.900 corregido (A 572, D 2.232, tras la correccion del 2.805 en la vuelta
5): **+6 A y +94 D** en los 100 pares de 2.901 a 3.000 (incluida la correccion del 2.916, que
resta un A del conteo bruto de 7). B y C sin cambio.

### Tasa por dominio (corte 3.000)

| dominio | n | A | tasa |
|---|---:|---:|---:|
| core | 1.445 | 344 | 23,8 % |
| **quality** | **589** | **124** | **21,1 %** |
| health_safety | 192 | 45 | 23,4 % |
| entrega | 171 | 2 | 1,2 % |
| environmental | 170 | 29 | 17,1 % |
| compras | 155 | 1 | 0,6 % |
| franquicias | 148 | 18 | 12,2 % |
| exportacion | 130 | 15 | 11,5 % |

`quality` sigue bajando (24,1 % al corte 2.900 corregido, a 21,1 % al corte 3.000) porque el
cuerpo del dominio sigue entregando su piso mas bajo. Quedan **388 pares** hasta el 3.388:
quality 255 (hasta el 3.255), risk_management 106, seguridad_digital 27.

### Vara por tramo de 25 (quality, 2.901-3.000)

| tramo | n | A | tasa |
|---|---:|---:|---:|
| 2.901-2.925 | 25 | 1 | 4,0 % |
| 2.926-2.950 | 25 | 3 | 12,0 % |
| 2.951-2.975 | 25 | 2 | 8,0 % |
| **2.976-3.000** | 25 | **0** | **0,0 %** |

**El ultimo tramo entrego CERO A, un piso nuevo** (el anterior minimo registrado fue 4,0 % en
2.826-2.875 de la vuelta 4). No es caida del inventario: es la misma familia de patrones
cronicos que ya senalaba el reporte anterior (cumulos que separan cada nodo por autor y por
faceta), mas una figura nueva que aparecio con fuerza en este tramo: **el patron "ficha nombrada
literalmente dentro del paso de otro nodo"**, que se repite seis veces en el corte 2.926-3.000
(2.961, 2.963, 2.975/2.991 comparten familia, 2.980, 2.986, y el propio 2.956 de la vuelta
anterior que abrio el patron). En todos los casos, el nodo mayor NOMBRA textualmente el
contenido del nodo menor como uno de sus propios pasos, y aun asi la vara del paso entero da D
porque el nodo menor desarrolla una mecanica propia que el paso generico no cubre.

### Las seis A del tramo nuevo (2.926-3.000), por su mecanismo

| puesto | mecanismo |
|---:|---|
| **2.931** | identidad de gemelos: `error_proofing_servicio` = `poka_yoke_a_prueba_de_errores`, via `mistake_proofing_poka_yoke_2`, verificado que los dos eslabones citados son identidad y no contencion |
| **2.935** | identidad ya doctrina: `breakthrough_desempeno_actual` = `secuencia_universal_para_el_breakthrough`, ambos ya identicos a `six_sigma_dmaic` por eslabones de identidad |
| **2.942** | gemelos del Paso 12 de Crosby: `reconocimiento` = `reconocimiento_crosby`, mismo esqueleto, mismo patron ya visto en el 2.616 |
| **2.952** | **NUEVA fusion mutua**: `cultura_integridad_objetividad_resolucion_problemas` contra `manejo_problemas`, resumenes casi verbatim del mismo pasaje Crosby, cada uno con su linea propia (oportunidad de mejora contra protocolo de escalamiento). Mueve el contador de mutuas a **DIECINUEVE** |
| **2.962** | identidad: `seis_sigma_servicios` = `six_sigma_dmaic_2`, DMAIC aplicado literalmente a servicios, los cinco pasos calzan uno a uno |
| (2.917, del tramo relecturado) | A por contencion: `kanban_pull_system` cabe entero en `sistema_pull_push`, confirmado por el entregable de este ultimo, que nombra "kanbans implementados" |

Ninguna de las seis abre figura nueva salvo la fusion mutua del 2.952 (contador a diecinueve); el
resto son transitividades de identidad hacia cumulos ya contados o gemelos de familias ya vistas.

### Familias del 9.3 al dia, con su especie de ganador (corte 3.000)

| familia | novedad de este corte | especie |
|---|---|---|
| la **capacidad** | extiende con 2.984, 2.996, **ambas D pese a sim_tit muy alto (68,0 y 64,9)** | **SIN ACTO, sigue cerrada** |
| la **distincion comun/especial** | sin miembros nuevos; tres pares del tramo (2.977, 2.985, 2.990) vuelven a confirmar la frontera D contra el cumulo de responsabilidad gerencial | **POR DERECHO**, sin cambio |
| la **responsabilidad gerencial** | tres D mas contra la distincion (2.977, 2.985, 2.990) y una D mas propia (2.994 contra `aceptacion_de_fallas_como_inevitables`) | **POR ELEGIR provisional, sigue abierto** (pregunta 3, sin adjudicar) |
| el **breakthrough / DMAIC** | dos identidades nuevas (2.935, 2.962), ambas transitividad hacia el hub ya contado | **POR ELEGIR**, sin cambio de cumulo |
| **fusion mutua** | **UN caso nuevo**, el 2.952 | contador **DIECINUEVE** (anterior: 2.891) |
| el **Consejo de Calidad** | la grieta del 2.916 se cierra a D; el hub `consejo_calidad` sigue absorbiendo `consejo_de_calidad_3` via 2.523 y 2.662 (contencion, no via el 2.916) | **grieta cerrada**, pregunta 2 resuelta en su origen |
| **ficha nombrada dentro del paso de otro nodo** | figura reconocida esta vuelta, seis casos en 2.901-3.000 (2.956, 2.961, 2.963, 2.980, 2.986, mas 2.975/2.991 de la familia del Paso 14) | siempre D, ficha contra mapa |
| **senal del idioma (quinta cara)** | sin aparicion nueva; cinco denominaciones al corte 3.000 | sin cambio |

## LA LECCION DEL METODO, y va al acta del auditor

**El filo dominante de este checkpoint no fue el mismo que en el 2.900.** Alli la mayoria de las
D caian por transitividad de cumulo o contencion clasica (un nodo cabe en otro). Aqui aparecio
con fuerza una figura distinta: **el nodo mayor NOMBRA LITERALMENTE el contenido del nodo menor
como uno de sus propios pasos**, y aun asi no funde, porque el nodo menor desarrolla una mecanica
propia (tecnica, formula, checklist) que el paso generico del mayor no despliega. Ejemplos
citables para la ciega:

- **2.961** (`estrategias_estimacion_costos` contra `metodologia_medicion_copq`): el paso 3 de
  `metodologia_medicion_copq` dice literalmente "elegir la estrategia de estimacion de costos mas
  adecuada (recursos totales o costo unitario)", el titulo entero del otro nodo. D de todos
  modos: la ficha trae la formula completa (que fuentes de datos usar, que incluir en el
  calculo) que el paso generico no tiene.
- **2.963** (`key_process_product_characteristics` contra `planificacion_inicial_calidad`): el
  paso 2 de `planificacion_inicial_calidad` dice "identificar caracteristicas clave del producto
  y del proceso (KPCs)", nombrando el otro nodo entero. D: KPC trae la traza completa desde QFD y
  AMFE hasta el registro en planos que el paso generico no desarrolla.
- **2.980** y **2.986** (`formulacion_teorias_causa` contra `diagrama_causa_efecto` y contra
  `analisis_diagnostico_causa`): el paso 3 de `formulacion_teorias_causa` dice "construir un
  diagrama de causa-efecto (espina de pescado)", y el paso 2 de `analisis_diagnostico_causa` dice
  "formular teorias... usando brainstorming y diagramas causa-efecto". Los tres nodos se citan
  entre si por nombre y ninguno funde con otro: cada uno desarrolla su propia mecanica (el
  Ishikawa completo con angulo de 70 grados y verificacion de cadenas causales; la afinidad y el
  FMEA; el Pareto previo y la validacion estadistica final).

**El segundo filo, mas viejo pero repetido:** los dos cumulos separados de la doctrina de "no
culpar al trabajador" (la distincion estadistica POR DERECHO contra la postura gerencial de
`sistema_responsabilidad_gerencial`) siguen sin fundirse pese a compartir vocabulario Deming casi
identico; el tramo trajo tres confirmaciones mas de esa frontera (2.977, 2.985, 2.990), todas D,
consistentes con 2.677, 2.766, 2.800, 2.850, 2.881, 2.906.

## LA GRIETA DEL 2.916, resuelta

Cerrada en la TAREA 1 con correccion declarada. Ver seccion 1.1 arriba. La regla que queda
escrita para el resto del cribado: **antes de invocar transitividad de cumulo, verificar que
CADA eslabon citado sea identidad y no contencion, en las dos direcciones.**

## DISCUTIBLES MARCADOS para la relectura ciega (marcados ANTES de saber si acierto)

**Los 100 pares de 2.901 a 3.000 llevan DISCUTIBLE MARCADO inline en el jsonl; el marcado que
cuenta para el credito es el del archivo.** 28 llevan la marca fuerte. Las seis A del tramo
nuevo (2.931, 2.935, 2.942, 2.952, 2.962) mas el 2.917 relecturado son el riesgo primario, junto
con el 2.916 ya corregido.

**Los discutibles mas fuertes, con su filo, para la ciega:**

| puesto | clase | por donde puede caer |
|---:|---|---|
| **2.916** | D (corregido) | quien lea las cuatro fusiones previas como gemelos por identidad en vez de contencion asimetrica dira A; el propio contrapeso esta escrito en la razon |
| **2.917** | A | quien lea kanban como instrumento aparte del sistema pull, sin ir al entregable de `sistema_pull_push` que nombra "kanbans implementados", dira D |
| **2.931** | A | quien pese "servicio" como cara distinta del poka-yoke general de manufactura dira D |
| **2.935** | A | sim_tit 46,3; quien lea el vocabulario distinto (los dos viajes contra las cinco letras del DMAIC) como estructura distinta dira D |
| **2.942** | A | quien lea "adaptar el reconocimiento a tu forma de trabajar" como un paso entero propio dira D |
| **2.952** | A | la unica fusion mutua nueva del checkpoint; quien pese la oportunidad de mejora y el protocolo de escalamiento como pasos enteros propios por la vara del paso entero dira D, y entonces el contador NO sube a diecinueve |
| **2.962** | A | quien lea el ejemplo de servicios (ciclo de emision de credito) como cara distinta del DMAIC generico dira D |
| **2.904, 2.910, 2.956, 2.961, 2.963, 2.980, 2.986** | D | el patron "ficha nombrada dentro del paso del otro nodo"; quien lea la mencion literal como el mismo acto repetido dira A en cualquiera de los siete |
| **2.927, 2.933** | D | los dos pares con cadena de dos A hacia un tercer nodo compartido, verificados como contencion y no identidad; quien componga la cadena sin verificar dira A |
| **2.965** | D | `six_sigma_dmaic` es identidad ya doctrina de la pata de mejora de la Trilogia; quien confunda la pata con el paraguas de tres procesos dira A |
| **2.983, 2.984, 2.996** | D | sim_tit muy alto (52,6; 68,0; 64,9), los tres con un paso entero asimetrico especifico (plan de reaccion; prueba de mejoras; unidad de estudio persona/maquina); quien pese el titulo compartido sin leer ese paso dira A |
| **2.978** | D | la logica de decision esporadico/cronico es identica en los dos nodos; solo la tiene mas desarrollada uno de los dos con tres tecnicas propias; el mas parejo de los discutibles del checkpoint |

**Patron del checkpoint:** A por contencion verificada, identidad de gemelos o fusion mutua
nueva, contra D por ficha-nombrada-dentro-del-paso, dos-cumulos-separados-de-siempre, y
paso-entero-asimetrico con sim_tit alto. La vara del paso entero y la regla de la contencion del
2.805/2.916 tiran de las dos direcciones.

## PENDIENTES DE DOCTRINA y PREGUNTAS (regla 9: lo que no puedo medir, lo traigo)

- **NO hubo PENDIENTE DE DOCTRINA nueva en el cribado.** Los 75 pares nuevos y los 25
  relecturados se clasificaron con reglas escritas (vara del paso entero, ficha contra mapa,
  contencion verificada, identidad de gemelos, fusion mutua, capacidad SIN ACTO, la regla nueva
  de la transitividad del 2.805/2.916). Ninguno pidio una regla que no exista.
- **PREGUNTA 1 (heredada, la fecha/orden canonico): no aplica esta vuelta**, sin novedad.
- **PREGUNTA 2, la cobertura del Consejo de Calidad: LA DOY POR RESUELTA EN SU ORIGEN**, no
  cerrada por mi (eso es adjudicacion del auditor). La grieta que la mantenia abierta (el 2.916)
  esta corregida; el hub sigue absorbiendo a `consejo_de_calidad_3` por los eslabones de
  contencion 2.523 y 2.662, que no se tocaron. Traido, no dictado.
- **PREGUNTA 3, el sub-cumulo de la responsabilidad gerencial: SIGUE ABIERTA** (heredada). Tres
  D mas de la misma frontera (2.977, 2.985, 2.990) mas una D propia (2.994) refuerzan que el
  cumulo esta POR ELEGIR provisional y separado del cumulo de la distincion. La cola dira.
  Anotado, no dictado.
- **PREGUNTA 4, nueva: la figura "ficha nombrada dentro del paso de otro nodo".** Aparecio seis
  veces en este corte (2.956, 2.961, 2.963, 2.980, 2.986, y la familia del 2.975/2.991). En los
  seis casos la vara del paso entero dio D porque el nodo menor desarrolla mecanica propia. La
  traigo como figura reconocida, no como regla nueva: la vara existente (paso entero, ficha
  contra mapa) ya la cubre, pero merece nombrarse porque puede repetirse en la cola. No pide
  doctrina nueva.
