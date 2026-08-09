# La franja bajo el umbral, cribada entera

Informe de cierre del encargo de cribado. Los 1.606 pares de
`docs/FRANJA_PARES.jsonl` quedaron leidos uno por uno, en orden de
`puesto_franja`, y registrados en `docs/FRANJA_VEREDICTOS.jsonl`. No hay
huecos: los puestos 1 a 1606 estan todos en el archivo, cada uno con su clase
y su razon.

**Los cinco ultimos (1602 a 1606) son los pares de borde** que la regla de
corte del Paso 0 habia dejado fuera. Se anexaron despues de la primera entrega,
sin renumerar nada, y con eso el agujero de borde queda cerrado. Ver el
apartado 6.3.

Ningun nodo se toco. Este documento es la entrega. **La adjudicacion del
auditor sobre las 2 A y las 6 B ya llego y esta en la seccion 9**; los racimos
quedan para despues de la muestra, y **la muestra del 5% de las D ya esta
sorteada, versionada y con dos tandas de tres leidas** (seccion 10).

---

## 1. Las cifras

| Clase | Que significa | Cuantos | % |
|---|---|---:|---:|
| A | Violacion candidata de la vara | 2 | 0,1 |
| B | Dudoso | 6 | 0,4 |
| C | Sano, pero con hallazgo lateral | 371 | 23,1 |
| D | Sano y limpio | 1.227 | 76,4 |
| | **Total** | **1.606** | **100** |

Las dos A estan en los puestos 15 y 124. Las seis B estan en los puestos 22,
28, 52, 79, 104 y 610. Despues del puesto 610 no hay una sola A ni una sola B
en 996 pares leidos, **incluidos los cinco de borde**.

**La lectura de la vara.** Por debajo del umbral la vara del gradiente
aguanta. Dos violaciones candidatas en 1.606 pares, las dos en el primer 8% de
la cola, y ninguna en los ultimos 996 pares. La franja no es un yacimiento de
violaciones del gradiente.

**Lo que la franja si encontro.** El cribado se cruzo con otra cosa, mucho mas
grande que lo que venia a buscar: el catalogo esta lleno de nodos que dicen lo
mismo dos, tres, cuatro y hasta doce veces. Eso es lo que ocupa las 371 C y es
lo que este informe organiza en la seccion 4.

---

## 2. Como clasifique

Reglas que aplique desde el primer par y sostuve hasta el ultimo. Van aqui
porque cambian como se leen los veredictos.

1. **C se marca SOLO por las ocho figuras que nombra el encargo.** La voz de
   manual y el infinitivo suelto NO disparan C: aparecen en demasiados nodos
   para ser senal.
2. **En cada razon de C digo si la figura es NUEVA o YA REGISTRADA**, para que
   la adjudicacion no tenga que ir a buscarlo. De las 371 C, 113 traen una
   figura nueva.
3. **Las herramientas con nombre propio se anotan SIN asumir que murieron.**
   Las plataformas de uso general (Google, LinkedIn, Facebook, Amazon) se
   anotan con la nota de que lo son.
4. **Los tres pares ya leidos en la cola de 346** que cayeron dentro de la
   franja van marcados como tales en su razon: franja 4 (P345), franja 5
   (P341) y franja 1029 (P173).

### Una limitacion mia, declarada

Cuando una figura ya quedaba censada completa (los racimos grandes), en varios
pares posteriores que solo tocaban a un miembro ya contado marque D en vez de
C. **El conteo de 371 C subestima cuantas veces se volvio a ver cada figura.**
Lo que NO queda corto son las figuras mismas y sus censos: esos estan
completos y son lo que importa para adjudicar.

---

## 3. Las dos violaciones candidatas, con detalle

**Franja 15.** `quality/breakthrough_desempeno_actual` contra
`plan_mejora_procesos`. El nodo del mundo da un DMAIC generico de cinco pasos
sobre el mismo material que el nodo del nucleo desarrolla en quince pasos
concretos. El de pago queda a la altura del gratis.

**Franja 124.** `environmental/eco_efectividad` contra
`economia_circular_como_modelo_de_negocio`. El nodo del mundo da tres pasos
(piloto, ciclos biologico y tecnico, materiales de upcycling) y el del nucleo
da nueve sobre la misma doctrina, cubriendo esos tres y agregando el rediseno
del modelo, el mecanismo de retorno, las cinco estrategias circulares y el
calculo de impacto. El de pago queda por debajo del gratis.

**Contexto que la adjudicacion deberia tener a la vista antes de decidir:** los
dos nodos del mundo pertenecen a racimos. `eco_efectividad` es uno de once
nodos de cradle to cradle en environmental y uno de tres que se titulan eco
efectividad. `breakthrough_desempeno_actual` convive con la familia de causas
comunes de quality. Puede que el arreglo no sea nodo por nodo sino de racimo.

> **Adjudicadas.** El auditor confirmo las dos como violaciones y les encontro
> una causa comun que yo no habia visto: **las dos son sombras de nodos
> costurados del nucleo**. La adjudicacion completa, con la verificacion de los
> cuatro nodos contra el grafo, esta en la **seccion 9**.

---

## 4. Los hallazgos laterales, agrupados por figura

Esta es la parte gruesa del informe. Las ocho figuras del encargo aparecieron
todas, pero lo que el cribado encontro no fue el par duplicado sino el
**racimo**: grupos de tres a veinte nodos que predican la misma doctrina.

### 4.1 Racimos, ordenados por tamano

| Racimo | Donde | Nodos |
|---|---|---:|
| No culpar a la persona, arreglar el sistema | health_safety | **20** |
| Causas comunes y responsabilidad del sistema | quality | **12** |
| Cradle to cradle | environmental + nucleo | **11** |
| Portafolio: revisar, podar, reasignar | **NUCLEO** | **7** |
| Customer discovery: salir a hablar con el cliente | **NUCLEO** | **7** |
| Accion correctiva | quality | **7** |
| Auditoria de calidad | quality | **6** |
| Benchmarking | quality | **5** |
| Los cinco porques | **NUCLEO** | **5** |
| Pivotar o proceder | **NUCLEO** | **5** |
| El avance y el compromiso en la venta | **NUCLEO** | **5** |
| Mapeo del flujo de valor | quality + environmental + nucleo | **5** |
| Encuadre del problema (How Might We) | **NUCLEO** | **5** |
| Ciclo de mejora PDCA / PDSA | quality | **4** |
| Clasificacion de defectos | quality | **4** |
| Analisis de causa raiz | quality | **4** |
| Las reglas del brainstorming | nucleo (3) + quality (1) | **4** |
| Fitness for purpose | quality | **3** |
| Costo de calidad | quality | **3** |
| Metas de calidad | quality | **3** |
| Consejo de calidad | quality | **3** |
| Eliminacion de causas de error | quality | **3** |
| Plan y matriz de control | quality | **3** |
| Diversidad en el diseno | environmental | **3** |
| El efectivo contra la ganancia | **NUCLEO** | **3** |
| La etapa de investigacion en la venta | **NUCLEO** | **3** |
| Estrategia de innovacion de producto | **NUCLEO** | **3** |
| Programa de catorce pasos de Crosby | quality | **3** |
| Poka yoke | quality | **3** |
| Obtencion de compromiso | **NUCLEO** | **3** |

Trece de esos racimos estan DENTRO DEL NUCLEO, es decir dentro del catalogo
que se entrega gratis.

### 4.2 El programa de Crosby, que explica media familia de quality

Este es el hallazgo que da sentido a casi todo lo que el cribado encontro en
el mundo quality.

El mundo tiene **tres** nodos que describen o presentan el programa de catorce
pasos de Crosby (`concepto_programa_catorce_pasos`,
`programa_mejora_calidad_14_pasos`, `crosby_programa_14_pasos_introduccion`).
Y ademas tiene **los pasos sueltos convertidos en nodos independientes con el
numero en el titulo**: Paso Dos, Paso 3, Paso 4, Paso 6, Paso 10, Paso 11 y
Paso 14.

**Cinco de esos pasos aparecen DUPLICADOS**, con dos nodos distintos que
llevan el mismo numero y dicen lo mismo:

| Paso | Los dos nodos |
|---|---|
| Paso 3 | `medicion_calidad` y `medicion_calidad_2` |
| Paso 6 | `accion_correctiva_4` y `accion_correctiva_sistematica` |
| Paso 10 | `establecimiento_metas` y `fijacion_de_metas` |
| Paso 11 | `eliminacion_causas_error` y `eliminacion_causas_error_2` |
| Paso 14 | `reinicio_programa_calidad` y `repeticion_programa` |

O sea: la figura del numero de paso en el titulo no era cosmetica. Es un
programa entero desmontado en piezas, con piezas duplicadas. Eso explica de un
golpe la familia de accion correctiva de siete miembros, la de eliminacion de
causas de error de tres, la del consejo de calidad de tres y la de metas de
tres.

### 4.3 Sufijo _N vivo

**Treinta nodos** con sufijo numerico vivo en el id. Ya no es una figura de
quality: hay miembros en quality, exportacion, franquicias, environmental y
health_safety.

Una variante que no estaba en la ficha: `proteccion_propiedad_intelectual_2`
vive en el mundo exportacion y `proteccion_propiedad_intelectual` vive en el
NUCLEO. El `_2` no distingue a dos hermanos del mismo mundo, choca con el id
de un nodo del catalogo gratis.

Y en varios casos conviven el id base y el de sufijo, con contenido calcado:
`sistema_responsabilidad_gerencial` con su `_2`,
`clasificacion_de_seriedad_de_defectos` con su `_2`, `eco_efectividad` con su
`_2`, `equipo_mejora_calidad` con su `_2`,
`planificacion_estrategica_despliegue` con su `_2`,
`establecer_vision_organizacional` con su `_2`, `contacto_con_el_cliente` con
su `_2`, `ciclo_de_culpa` con su `_2`, `triple_bottom_line` con su `_2`.

### 4.4 Ids casi identicos

**Diecinueve pares** de nodos cuyos ids se distinguen por una letra, un
articulo o por las mismas palabras permutadas, con contenido calcado. Empezo
como figura de quality y termino apareciendo tambien en environmental,
franquicias y **dentro del nucleo**.

Los mas claros:

- `desarrollo_caracteristicas_producto` con `desarrollar_caracteristicas_producto`
- `descubrir_necesidades_del_cliente` con `descubrir_necesidades_cliente`
- `planificacion_de_la_inspeccion` con `planificacion_inspeccion`
- `auditoria_de_producto` con `auditoria_producto`
- `analisis_causa_raiz_diagnostico` con `analisis_diagnostico_causa`
- `establecimiento_capacidad_proceso` con `establecer_capacidad_del_proceso`
- `reduccion_tiempo_ciclo` con `reduccion_de_tiempo_de_ciclo`
- `mantener_las_ganancias` con `sostener_las_ganancias`
- `desplegar_metas_organizacion` con `despliegue_metas`
- `fitness_for_use_purpose` con `fitness_for_purpose_vs_conformance`
- `relaciones_largo_plazo_con_proveedores` con `relacion_largo_plazo_proveedor_unico`
- `gestion_seguimiento_prospectos` con `cadencia_seguimiento_prospectos`
- `pdsa_shewhart_cycle` con `ciclo_shewhart_pdsa`
- `respetar_la_diversidad` con `respeto_a_la_diversidad`
- `elaboracion_fdd` con `preparar_fdd`
- **En el nucleo:** `fallo_como_aprendizaje_startup` con `fracaso_como_aprendizaje_startup`
- **En el nucleo:** `leap_of_faith_assumptions` con `leap_of_faith_questions`
- **En el nucleo:** `funnel_get_customers_optimizacion` con `optimizacion_embudo_get_customers`

**La decimonovena llego con los pares de borde, y es de otra especie**
(franja 1603): `exportacion/seleccion_canales_distribucion` contra
`seleccion_canal_distribucion` **del nucleo**. Es la **primera transdominio**
de la figura. Las dieciocho anteriores viven todas dentro de un mismo mundo o
dentro del nucleo; esta es la primera que cruza la frontera que el producto
cobra, con una sola letra de plural separando el id del mundo del id del
nucleo. El contenido del par es sano (el mundo especializa a comercio
internacional sobre la base lean del nucleo), pero la coincidencia de ids es un
riesgo de confusion que las otras dieciocho no tenian: aqui un lector puede
cruzar sin darse cuenta la linea entre lo gratis y lo pago.

> **Discrepancia de ordinal, sin resolver.** El encargo de la adjudicacion la
> llama *octava* instancia. En este registro la octava es la **franja 723**
> (`reduccion_tiempo_ciclo` con `reduccion_de_tiempo_de_ciclo`), y esta es la
> decimonovena. Escribo el ordinal que sale del archivo y dejo el otro
> anotado. No cambio ninguno de los dos por mi cuenta.

### 4.5 Costuras: nodos que cuentan lo mismo dos veces

Nodos con dos o mas bloques apilados que narran la misma doctrina. Las mas
grandes, ordenadas por tamano:

| Nodo | Donde | Pasos y bloques |
|---|---|---|
| `blueprint_de_experiencia` | nucleo | **17 pasos, 4 bloques** |
| `principio_calidad_mvp` | nucleo | **14 pasos, 3 bloques** |
| `metas_vs_proposito` | nucleo | 14 pasos, 2 bloques |
| `propuesta_gasto_capital` | nucleo | 12 pasos, 2 bloques |
| `seleccion_ceo_fundador` | nucleo | 12 pasos, 3 bloques |
| `ganar_comprension_del_cliente` | nucleo | 11 pasos, 2 bloques |
| `revisiones_regulares_desempeno_ceo` | nucleo | 10 pasos, 2 bloques |
| `customer_journey_mapping` | nucleo | 10 pasos, 2 bloques |
| `superioridad_producto_beneficios` | nucleo | 10 pasos, 2 bloques |
| `voz_del_cliente_voc` | nucleo | 10 pasos, 2 bloques |
| `criterios_seleccion_proveedores` | nucleo | 10 pasos, 2 bloques |
| `bundle_ideas` | nucleo | 9 pasos, 2 bloques |
| `five_whys_inversion_proporcional` | nucleo | 9 pasos, 2 bloques |
| `economia_circular_como_modelo_de_negocio` | nucleo | 9 pasos, paso 6 repite paso 1 |
| `sistema_inmune_producto` | nucleo | 9 pasos, 2 bloques |
| `metricas_de_adquisicion_activacion` | nucleo | 9 pasos, 2 bloques |
| `analisis_tco_roi_b2b` | nucleo | 9 pasos, 2 bloques |
| `posicionamiento_de_empresa` | nucleo | 9 pasos, 2 bloques |
| `brainstorming_divergente` | nucleo | 8 pasos, 2 bloques |
| `gestion_inventario` | nucleo | 9 pasos, 2 bloques |
| `plan_mejora_procesos` | nucleo | 15 pasos, bloques apilados |

**Todas las costuras estan en nodos del NUCLEO.** No aparecio ni una sola en
un nodo de mundo. Esa asimetria merece explicacion del auditor.

> **Queda como pregunta abierta, con hipotesis a comprobar** (adjudicacion, ver
> seccion 10): **21 de 21 en el nucleo puede ser efecto del tamano de los nodos
> del nucleo, no de su salud.** Una costura necesita sitio: hacen falta dos
> bloques apilados para que se vea, y los nodos del nucleo son sistematicamente
> mas largos que los de mundo. Si el nucleo concentra los nodos de nueve pasos
> para arriba, concentrara las costuras aunque los dos lados enfermen igual. La
> comprobacion es del barrido intra-dominio: **normalizar la tasa de costura
> por longitud del nodo** y ver si la asimetria sobrevive. Si sobrevive, es
> salud; si desaparece, era el metro.

### 4.6 Marco-pais cableado

**Veinte pares** dejaron a la vista nodos que cablean un marco regulatorio
nacional sin ninguna condicion de pais.

En los mundos: `stopfakes.gov` y `uspto.gov`, el U.S. Census Bureau, el U.S.
Commercial Service, `export.gov`, el FDD y sus veintitres secciones con plazo
de catorce dias, los registros estatales de franquicias, los requisitos de la
FTC, el Malcolm Baldrige National Quality Award, las certificaciones ASQ y del
Juran Institute, y el POA&M del marco federal en seguridad_digital.

**En el NUCLEO, dos, y son las mas duras:**

- `cumplimiento_magnuson_moss` estructura el nodo entero alrededor de una ley
  federal estadounidense, incluido el paso de consultar a un abogado que
  conozca esa ley.
- `term_sheet_disposiciones_vinculantes` cablea los costos de filing del HSR
  Act, ley antimonopolio estadounidense.

**Y aparecio marco europeo por primera vez:**
`responsabilidad_extendida_productor_2` cablea WEEE y RoHS.

**Contramodelos que el cribado encontro** y que sirven de vara de como deberia
verse un nodo bien hecho:

- `marco_legal_comercio_electronico_internacional` condiciona por pais destino
  en vez de cablear uno.
- `paris_convention_prioridad` y `patent_cooperation_treaty` usan marcos
  internacionales.
- `exclusividad_territorial_representante` manda verificar si las leyes de tu
  pais permiten el limite territorial.

**Colateral de la adjudicacion: el CUI de seguridad_digital, y lo que medí al
verificarlo.** La adjudicacion registra
`seguridad_digital/getting_started_supply_chain_risk_management` (paso 1,
*proveedores criticos con acceso a sistemas que procesan CUI*) como tercera
instancia de marco-pais en ese mundo tras los dos POA&M. **Verificado contra el
grafo: la cita existe y es marco-pais** (CUI es una designacion federal
estadounidense y arrastra NIST SP 800-171). Dos precisiones que salen de la
misma verificacion:

1. **No es nueva en este archivo.** Ya estaba registrada en el veredicto de la
   **franja 79**, dentro de la B, como *pais cableado, el nodo del mundo vuelve
   a usar CUI sin condicion de pais*. Lo que faltaba era subirla aqui, a la
   lista de la figura. Queda subida.
2. **Tercera REGISTRADA, no tercera existente.** Al ir a contarlas conte el
   mundo entero: **de los 55 nodos de seguridad_digital, 20 cablean el marco
   federal estadounidense en sus pasos** (CUI, NIST, SP 800, POA&M). Son trece
   con CUI, cuatro con NIST, cuatro con SP 800 y cuatro con POA&M, con solapes.
   **Mas de un tercio del mundo.** El cribado solo vio los que la franja le puso
   delante; el problema de ese mundo no son tres nodos sino su encuadre entero,
   y eso es material para el barrido intra-dominio, no para un parche de tres
   nodos.

### 4.7 Herramientas con nombre propio

Catorce pares las dejaron a la vista. Se anotan sin asumir que murieron.

**En nodos de mundo:** Empty Miles Service, RentaGreenBox, EcoNation, Minitab,
TrafficEstimate.com, Alexa, Google Analytics, Energy Star, la Guide to Greener
Electronics de Greenpeace, VMware.

**En nodos del NUCLEO:** Google Keyword Planner, Google Trends, oDesk, Elance,
InnoCentive, GS1, EPCglobal, Optimizely, Visual Website Optimizer, Unbounce.

Plataformas de uso general anotadas aparte: Google, LinkedIn, Facebook,
Amazon.

### 4.8 Herramientas muertas, id fosil, audiencia invertida

Tres de las ocho figuras del encargo **no produjeron ningun hallazgo nuevo** en
1.606 pares:

- **Id que no corresponde al contenido:** no encontre ninguno mas alla de los
  que ya estaban en la ficha.
- **Audiencia invertida:** no encontre ninguno nuevo.
- **Herramienta que se pueda declarar muerta:** ninguna. Todas las citadas
  quedan anotadas como vivas o sin verificar, tal como manda el encargo.

---

## 5. Lo que no cupo en las clases

Quince pares dejaron algo que no es una violacion de la vara ni una de las
ocho figuras, pero que un lector se puede encontrar. La mayoria son **choques
de doctrina entre el mundo y el nucleo**: dos nodos que mandan lo contrario
sobre el mismo acto.

Los mas fuertes:

1. **Franja 140.** El mundo manda dedicar unos minutos a preguntas personales
   antes de negociar; el nucleo manda NO gastar tiempo en aperturas personales
   en ventas grandes.
2. **Franja 303, 328 y sus repeticiones.** El mundo manda dedicarle tiempo
   semanal a escribir lo que preferirias no pensar y preparar planes B; el
   nucleo (`no_jugar_con_probabilidades`) manda rechazar la paralisis de las
   probabilidades y **evitar construir planes de contingencia**. Es el choque
   que mas veces reaparecio.
3. **Franja 618.** El mundo manda eliminar o redisenar la evaluacion
   individual anual; el nucleo manda ponerla en marcha y que nadie se quede
   sin la suya.
4. **Franja 1499, 1522 y 1565.** El mundo manda seleccionar varios canales
   complementarios; el nucleo insiste tres veces en enfocarse en UN solo canal
   durante el descubrimiento.
5. **Franja 1543.** El mundo manda devolverle el error a quien lo causo para
   que lo corrija; el nucleo prohibe senalar a la persona.
6. **Franja 732.** El mundo dice que ningun defecto es inevitable; el nucleo
   dice que el primer error se tolera siempre.

Y una figura menor pero repetida: **nodos que se apoyan en si mismos**.
`optimizacion_de_procesos` manda aplicar las mismas tecnicas que ya usaste
antes sin decir cuales (franja 1187, 1259 y 1503). Es la misma forma del nodo
que quedo como B en franja 28.

---

## 6. Correcciones mias, en limpio

Cuatro errores propios que quedan aqui declarados y ya corregidos en el archivo
(el cuarto lo encontro la muestra D, no yo):

1. **Cifras mal sumadas en dos mensajes de commit.** En el checkpoint de 500
   escribi 100 C y 393 D cuando eran 112 y 381; en el de 800 escribi 191 C y
   601 D cuando eran 188 y 604. Desde el checkpoint de 900 la cuenta se saca
   del archivo antes de redactar el mensaje. Las cifras de este informe salen
   del archivo.
2. **Un miembro de figura clasificado D por omision.** `medicion_calidad`
   (franja 247) se llama Paso 3 y lo clasifique D sin marcar la figura. Quedo
   registrado donde corresponde en franja 562 y 1525, y cuenta en la tabla del
   apartado 4.2.
3. **El agujero de borde del Paso 0: CERRADO.** Lo traje en el commit `dd0af9a`
   y estuvo abierto hasta esta entrega. La regla de corte (clave menor a
   0,7501) metio 3 pares que ya estaban leidos en la cola de 346 y dejo fuera 5
   pares genuinamente nuevos, con claves 0,7940, 0,7820, 0,7763, 0,7512 y
   0,7508.

   **Los cinco quedan anexados y leidos, con cero violaciones.** Se
   reprodujeron con la receta de este informe (regeneracion del instrumento a
   umbral semantico 0,70 en medicion aparte, resta de la cola de 346 y de la
   franja, y restauracion de las salidas del instrumento con `git checkout --`,
   sin persistir nada). La reproduccion dio **exactamente esos cinco, con las
   mismas claves y los mismos ids**, y confirmo tambien los 3 ya leidos
   (franjas 4, 5 y 1029). Entraron como puestos **1602 a 1606**, sin cambiar la
   regla y sin renumerar nada:

   | puesto | clave | par | clase |
   |---:|---:|---|:--:|
   | 1602 | 0,7940 | `quality/politica_formal_de_calidad` contra `plan_gestion_calidad` | D |
   | 1603 | 0,7820 | `exportacion/seleccion_canales_distribucion` contra `seleccion_canal_distribucion` | C |
   | 1604 | 0,7763 | `risk_management/manten_viva_tu_lista_de_riesgos` contra `matriz_probabilidad_impacto` | C |
   | 1605 | 0,7512 | `quality/evaluacion_alternativas_solucion` contra `brainstorming_divergente` | D |
   | 1606 | 0,7508 | `quality/evaluacion_desempeno_proyectos` contra `diseno_metricas_lideres_rezagados` | D |

   **Ninguna A y ninguna B entre los cinco**, que era la pregunta que el
   agujero dejaba abierta: los pares de mayor clave de la franja, los que mas
   cerca estaban del umbral, no escondian ninguna violacion. Las dos C traen
   figura: la 1603 es la primera transdominio de los ids casi identicos
   (apartado 4.4) y la 1604 es la **quinta verificacion post-cirugia no
   buscada** (apartado 9.4).

4. **Una figura del encargo aplicada a medias: los *Punto N* de Deming.** La
   figura *numero de paso en el titulo* la aplique a los *Paso N* del programa de
   Crosby y **nunca a los *Punto N* de los catorce puntos de Deming**, que son
   siete nodos de `quality` con la misma forma. Su primera aparicion en la cola
   fue la **franja 159** y la clasifique D. **La encontro la muestra D en la
   franja 822**, que queda corregida a C con el censo entero de la figura en su
   razon; el detalle esta en el apartado 10.1, verificacion 1. **Es el unico
   veredicto que la muestra ha tenido que corregir en 41 pares leidos.**

---

## 7. Lo que el auditor tiene que decidir

Este informe no propone arreglos. Lo que deja sobre la mesa. **Los puntos 1 y 7
ya tienen respuesta del auditor** y estan resueltos en las secciones 9 y 10; el
resto sigue abierto.

1. ~~**Las 2 A y las 6 B**, para adjudicar una por una.~~ **ADJUDICADAS**, ver
   seccion 9.
2. **Los treinta racimos**, para decidir si el arreglo es nodo por nodo o de
   racimo entero. Trece de ellos estan dentro del nucleo. **El auditor los deja
   como primer censo del barrido intra-dominio y los adjudica despues de la
   muestra D** (seccion 10).
3. **Los cinco pasos duplicados del programa de Crosby**, que son el caso mas
   limpio y mas facil de cerrar.
4. **Las veintiuna costuras**, todas en nodos del nucleo, con la pregunta de
   por que ninguna aparecio en un nodo de mundo. **Queda como pregunta abierta
   con hipotesis a comprobar en el barrido** (apartado 4.5 y seccion 10).
5. **Los veinte casos de marco-pais**, con los tres contramodelos que el
   propio catalogo ya tiene como vara.
6. **Los seis choques de doctrina** entre mundo y nucleo.
7. ~~**El 5% de muestra aleatoria de las D**, que el auditor sortea.~~
   **SORTEADA, VERSIONADA Y EN CURSO**: 61 pares, 41 leidos y los 41 se
   sostienen en la vara. Ver seccion 10.

---

## 8. Los veredictos completos

Lo que sigue es la lista de cada A, cada B y cada C con su razon, en orden de
`puesto_franja`. Las 1.227 D no se listan aqui; estan enteras en
`docs/FRANJA_VEREDICTOS.jsonl`, una por linea, con su razon.

### 8.1 Las A (2)

- **15** | quality/breakthrough_desempeno_actual contra plan_mejora_procesos  
  VIOLACION CANDIDATA. El mundo da un DMAIC generico de cinco pasos (define, mide, analiza, mejora, controla) y el nucleo da quince pasos concretos sobre el mismo material (as-is, limites de control, objetivos to-be, diseno del enfoque, metricas por etapa, responsable por paso). El de pago queda por debajo del gratis. Nota: el nodo del nucleo es el costurado del caso 9.
- **124** | environmental/eco_efectividad contra economia_circular_como_modelo_de_negocio  
  VIOLACION CANDIDATA, y con figura. El nodo del mundo da tres pasos (piloto, ciclos biologicos y tecnicos, materiales de upcycling) y el del nucleo da nueve sobre la misma doctrina, cubriendo los tres del mundo y agregando el rediseno del modelo, el mecanismo de retorno, las cinco estrategias circulares y el calculo de impacto. El de pago queda por debajo del gratis. FIGURA NUEVA: costura visible en el nucleo, economia_circular_como_modelo_de_negocio tiene dos bloques apilados y el paso 6 (mapear el ciclo de vida actual) repite el paso 1 (mapear el ciclo de vida completo).

### 8.2 Las B (6)

- **22** | quality/criterios_seleccion_proyectos_calidad contra gestion_de_portafolio_gates_go_kill  
  DUDOSO. El mundo especializa a proyectos de calidad (nominaciones, consejo de calidad) pero en metodo el nucleo da mas: embudo, gates con criterios visibles, matar proyectos y balance del portafolio. Empate discutible.
- **28** | quality/optimizacion_de_procesos contra mejora_continua_relentless  
  DUDOSO. El nodo del mundo es de tres pasos y se apoya en si mismo (aplica las mismas tecnicas que ya usaste antes); el del nucleo da un metodo experimental concreto. El solape tematico es parcial, asi que no lo cierro como violacion.
- **52** | exportacion/plataformas_comercio_electronico_marketplaces contra channels_hypothesis_web_mobile  
  DUDOSO. El mundo especializa a marketplaces internacionales pero con cuatro pasos genericos; el nucleo da metodo de comparacion (un canal principal, probar con presupuesto parecido, costo por cliente e ingreso neto). Empate discutible.
- **79** | seguridad_digital/getting_started_supply_chain_risk_management contra gestion_riesgo_cadena_suministro  
  DUDOSO, y con figura. El mundo da un plan SCRM de gobierno generico y el nucleo da ocho pasos concretos (cuantificar riesgo natural por pais, riesgo operativo, mapa de rutas, simulaciones, stock de seguridad, costo de cada proteccion). La especializacion del mundo es el angulo digital, no la profundidad. FIGURA: pais cableado, el nodo del mundo vuelve a usar CUI sin condicion de pais.
- **104** | franquicias/sitio_web_captura_leads contra diseno_landing_page  
  DUDOSO. El nodo del mundo tiene tres pasos y el del nucleo cinco sobre la misma pagina de conversion. El angulo del mundo es real (la web captura contactos, NO vende, y por eso se guarda la informacion financiera para la conversacion), pero en metodo el nucleo da mas: contenido claro, refuerzo del mensaje que trajo al visitante, diseno limpio, demos de menos de un minuto y navegacion simplificada.
- **610** | franquicias/concepto_de_advances contra advances_vs_continuations  
  DUDOSO. El nodo del mundo da cuatro pasos de la misma doctrina que el nucleo, el avance como venta pequena progresiva, y lo unico propio de franquicias es el ejemplo del CIRF. El nucleo ademas aporta el diagnostico que el mundo no tiene: distinguir avance de continuacion y preguntarte que falto cuando solo lograste una continuacion. La especializacion es un ejemplo, no metodo.

### 8.3 Las C (371)

Cada razon dice si la figura es NUEVA o YA REGISTRADA.

- **2** | risk_management/manten_viva_tu_lista_de_riesgos contra plan_gestion_riesgos  
  El mundo es el registro como documento vivo y el nucleo el plan de gobierno: momentos distintos, sano. FIGURA: el nodo del mundo es uno de los cinco reencuadrados en la cirugia 1, y vuelve a salir sano.
- **3** | environmental/innovacion_abierta_externa contra open_innovation_ideacion  
  El mundo especializa la innovacion abierta a retos ambientales y añade compartir IP propia: sano. FIGURA: par calcado del nucleo, open_innovation_ideacion contra innovacion_abierta, ya registrado en la ficha.
- **7** | environmental/cierre_de_ciclos_industriales contra economia_circular_como_modelo_de_negocio  
  El mundo aporta la simbiosis industrial con empresas cercanas, que el nucleo no tiene: sano. FIGURA: costura confirmada en economia_circular_como_modelo_de_negocio, ya registrada (calibradora del instrumento).
- **11** | seguridad_digital/getting_started_risk_assessment contra risk_audit  
  Evaluar riesgos con inventario de activos contra auditar el proceso al cierre: momentos distintos, sano. FIGURA: pais cableado, el nodo del mundo usa CUI, categoria regulatoria estadounidense, sin condicion de pais.
- **12** | compras/prepara_posicion_agenda_antes_negociar contra criterios_seleccion_proveedores  
  Preparar la negociacion contra elegir al proveedor por matriz: momentos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, el paso 7 reinicia la secuencia, ya registrada como caso 3.
- **21** | quality/vacios_conocimiento_cliente contra voz_del_cliente_voc  
  El mundo aporta las necesidades latentes y no articuladas, con prototipo y piloto: sano. FIGURA: costura confirmada en voz_del_cliente_voc, doble de la observacion, ya registrada.
- **31** | quality/planificacion_economica_conjunta contra analisis_tco_roi_b2b  
  Ingenieria de valor y TCO al comprar contra TCO y ROI al vender: objetos distintos, sano. FIGURA: costura visible en el nucleo, analisis_tco_roi_b2b tiene dos bloques (vender B2B en 1 a 4, evaluar proveedores por costo ponderado en 5 a 9). Ya citado por el instrumento, sin leer.
- **38** | quality/takt_time contra produccion_scheduling_balance_objetivos  
  Takt time y flujo contra lote economico y run-out: metodos distintos, sano. FIGURA: par calcado del nucleo, produccion_scheduling_balance_objetivos contra programacion_produccion, ya registrado.
- **39** | environmental/innovacion_abierta_externa contra innovacion_abierta  
  El mismo nodo del mundo empareja con LOS DOS gemelos del nucleo (con el 3), que es justo la senal del duplicado. FIGURA: par calcado del nucleo, innovacion_abierta contra open_innovation_ideacion, ya registrado.
- **43** | franquicias/proteccion_propiedad_intelectual_franq contra proteccion_propiedad_intelectual  
  La franquicia especializa la proteccion de IP a manual, FDD y no competencia: sano. FIGURA: pais cableado, el nodo del mundo dice segun las leyes del estado y usa FDD, documento regulatorio estadounidense, sin condicion de pais.
- **49** | quality/sistema_medicion_kpi contra metas_vs_proposito  
  Un sistema de KPI contra la critica de Goodhart: angulos distintos, sano. FIGURA: costura visible en el nucleo, metas_vs_proposito tiene catorce pasos y los cinco ultimos (10 a 14) son otro tema, el objetivo declarado del cliente y el seguimiento posterior al contrato.
- **55** | quality/plan_de_control contra plan_mejora_procesos  
  Controlar el proceso contra mejorarlo: temas vecinos, sano. FIGURAS: costura ya confirmada en plan_mejora_procesos, y plan_de_control es miembro del par calcado de quality con matriz_de_control_de_proceso, ya registrado.
- **61** | franquicias/proceso_llamada_inicial_venta contra tacticas_cold_calling  
  El mundo especializa la primera llamada a la venta de franquicias sobre el cold calling generico: sano. FIGURA: proceso_llamada_inicial_venta es miembro del par calcado de franquicias con proceso_primera_llamada, ya registrado.
- **65** | environmental/consolidacion_cargas_backhaul contra milk_run_deliveries  
  Consolidacion y backhaul contra ruta milk run con EOQ: metodos distintos, sano. FIGURA: herramienta con nombre propio, el nodo del mundo cita Empty Miles Service, sin comprobar si sigue vivo.
- **66** | exportacion/proteccion_propiedad_intelectual_internacional contra proteccion_propiedad_intelectual  
  La capa internacional sobre la estrategia domestica de IP: sano. FIGURA: pais cableado, el nodo del mundo cablea stopfakes.gov y uspto.gov, ya registrado como primer miembro de la ficha de marco-pais.
- **71** | quality/estudio_lealtad_cliente contra investigar_datos_cliente  
  Estudio de lealtad contra reunir datos del cliente en el CRM: temas distintos, sano. FIGURA: herramientas con nombre propio en el nucleo, LinkedIn, Facebook y Google; son plataformas de uso general, se anotan sin asumir nada.
- **90** | compras/investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor contra criterios_seleccion_proveedores  
  Investigar con fuentes objetivas antes de contactar contra elegir por matriz ponderada: momentos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, ya registrada.
- **93** | franquicias/proceso_primera_llamada contra tacticas_cold_calling  
  El mundo especializa la primera llamada sobre el cold calling generico: sano. FIGURA: proceso_primera_llamada es miembro del par calcado de franquicias, ya registrado.
- **114** | health_safety/rendicion_cuentas_prospectiva contra curse_cinco_culpas  
  Rendir cuentas hacia adelante contra facilitar los cinco porques sin senalar culpables: sano. FIGURA NUEVA: par calcado dentro del mundo health_safety. responsabilidad_prospectiva (franja 101) y rendicion_cuentas_prospectiva (franja 114) narran lo mismo con otro titulo: cambiar la pregunta de quien fallo por que cambiar, asignar quien pone en marcha las mejoras, comprobar que funcionaron.
- **115** | quality/criterios_diseno_producto contra criterios_seleccion_proveedores  
  Criterios para elegir un diseno de producto contra criterios para elegir proveedor: objetos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, ya registrada.
- **117** | health_safety/responsabilidad_sistemica contra curse_cinco_culpas  
  Mapear la responsabilidad de todo el sistema contra facilitar los cinco porques: sano. FIGURA NUEVA, amplia la de franja 114: el calcado de health_safety es un trio, no un par. responsabilidad_sistemica comparte con rendicion_cuentas_prospectiva el cuidado de las segundas victimas y la mirada al sistema en vez de al individuo.
- **129** | quality/establecer_vision_organizacional_2 contra creacion_estrategia_cadena_suministro  
  Redactar la vision del negocio contra generar ideas de cadena de suministro: temas distintos, sano. FIGURA NUEVA, doble. Sufijo _N vivo en el mundo quality: establecer_vision_organizacional_2. Y par calcado con su hermano sin sufijo, establecer_vision_organizacional (franja 116): los dos mandan redactar una vision simple y directa, revisar que cubra clientes y personas, y compartirla. Un tercer nodo del mismo mundo, planificacion_estrategica_despliegue (franja 130), toca lo mismo pero si agrega metodo propio (el catch ball), asi que no lo cuento en el calcado.
- **141** | quality/dmaic_fase_measure contra plan_mejora_procesos  
  El mundo profundiza la fase Measure con metodo propio (Pareto, FMEA, Gage R&R, control estadistico, causa raiz) sobre el nodo del nucleo: sano. FIGURA: costura ya confirmada en plan_mejora_procesos, quince pasos con los bloques apilados.
- **143** | quality/innovacion_tipo_ii contra bundle_ideas  
  Hacerlo mas grande, mas pequeno o combinarlo, contra agrupar ideas en un solo sistema: tecnicas distintas, sano. FIGURA NUEVA: costura visible en el nucleo, bundle_ideas tiene nueve pasos en dos bloques apilados. Los pasos 1 a 5 agrupan y combinan ideas por tema; los pasos 6 a 9 vuelven a dar el mismo consejo desde la lista de objetivos, con su propia evaluacion de riesgo al final.
- **147** | environmental/seleccion_productos_servicios_verdes contra diseno_para_sostenibilidad_cradle_to_cradle  
  Comprar verde contra disenar sin basura: objetos distintos, sano. FIGURA NUEVA: herramientas con nombre propio en el nodo del mundo, RentaGreenBox y EcoNation, servicios especificos y no plataformas de uso general. Se anotan sin asumir que murieron.
- **156** | health_safety/revision_de_aprendizaje contra five_whys_inversion_proporcional  
  Renombrar la investigacion como aprendizaje contra los cinco porques con inversion proporcional: angulos distintos, sano. FIGURA NUEVA: costura visible en el nucleo, five_whys_inversion_proporcional tiene nueve pasos en dos bloques apilados. Los pasos 1 a 5 son el metodo generico con su verificacion posterior; los pasos 6 a 9 vuelven a contar el mismo metodo aplicado a un problema de ventas, con grabaciones de llamadas y rediseno del entrenamiento.
- **163** | quality/consejo_calidad_2 contra plan_gestion_calidad  
  Conformar el consejo de calidad contra el plan de gestion de calidad: objetos distintos, sano. FIGURA NUEVA, doble. Sufijo _N vivo en el mundo quality: consejo_calidad_2. Y par calcado con consejo_de_calidad_y_rol_del_director (franja 173): los dos mandan conformar el consejo con quienes deciden, dejarlo por escrito, designar responsables de los proyectos y revisar el progreso quitando obstaculos.
- **164** | quality/accion_correctiva_6 contra five_whys_inversion_proporcional  
  Accion correctiva a partir de auditorias contra los cinco porques: temas vecinos, sano. FIGURA NUEVA: sufijo _N vivo en el mundo quality, accion_correctiva_6.
- **168** | quality/equipo_mejora_calidad_2 contra plan_gestion_calidad  
  Armar el equipo de mejora de calidad contra el plan de gestion de calidad: objetos distintos, sano. FIGURA: sufijo _N vivo en el mundo quality, equipo_mejora_calidad_2. Cuarto miembro de la figura en este tramo, junto a franja 129, 163 y 164.
- **173** | quality/consejo_de_calidad_y_rol_del_director contra plan_gestion_calidad  
  Consejo de calidad y rol del director contra el plan de gestion de calidad: objetos distintos, sano. FIGURA: segundo miembro del par calcado abierto en franja 163, consejo_calidad_2 contra consejo_de_calidad_y_rol_del_director.
- **181** | quality/pocos_vitales_muchos_utiles contra gestion_portafolio_foco  
  Clasificar proyectos en vitales pocos, utiles muchos y apagado de incendios contra auditar la capacidad y matar proyectos: sano. FIGURA NUEVA: par calcado dentro del mundo quality. proyectos_vitales_pocos (franja 125) y pocos_vitales_muchos_utiles (franja 181) narran la misma doctrina de Juran: clasificar los candidatos, trabajar los dos tipos con equipos distintos y medir el impacto de los vitales en el resultado.
- **187** | quality/distincion_causas_comunes_especiales_2 contra diagnostico_sintoma_vs_causa_ventas  
  Causas comunes contra causas especiales, contra distinguir sintoma de causa en un problema de venta: temas vecinos, sano. FIGURA: sufijo _N vivo en el mundo quality, distincion_causas_comunes_especiales_2. Quinto miembro de la figura, junto a franja 129, 163, 164 y 168.
- **193** | quality/formulacion_teorias_causa contra brainstorming_divergente  
  Formular teorias de causa con afinidad, espina de pescado y FMEA contra las reglas de la divergencia: metodos distintos, sano. FIGURA NUEVA: costura visible en el nucleo, brainstorming_divergente tiene ocho pasos en dos bloques apilados. Los pasos 1 a 4 son la sesion clasica con post-its; los pasos 5 a 8 son otra narracion entera sobre usar inteligencia artificial como participante, pedirle personas, generar lotes y cruzar conceptos.
- **199** | exportacion/screening_mercados_potenciales contra evaluacion_de_atractivo_de_mercado  
  Screening de mercados de exportacion contra evaluar el atractivo de un mercado: angulos distintos, sano. FIGURA: pais cableado, el nodo del mundo manda consultar el U.S. Census Bureau y pedir ayuda al U.S. Commercial Service. Ya registrada como figura en la ficha de marco-pais.
- **201** | quality/desarrollar_caracteristicas_proceso_2 contra ciclo_construir_medir_aprender  
  Disenar el proceso que crea y entrega tu producto contra el ciclo construir medir aprender: objetos distintos, sano. FIGURA: sufijo _N vivo en el mundo quality, desarrollar_caracteristicas_proceso_2. Sexto miembro.
- **205** | quality/analisis_competitivo_calidad contra voz_del_cliente_voc  
  Comparar tu producto contra el de la competencia con pruebas de laboratorio contra observar al cliente en su entorno: objetos distintos, sano. FIGURA: costura ya confirmada en voz_del_cliente_voc, diez pasos con la observacion contada dos veces.
- **211** | quality/desarrollar_caracteristicas_producto contra requirements_documentation  
  Traducir necesidades en caracteristicas concretas contra documentar y priorizar requisitos: objetos vecinos, sano. FIGURA NUEVA: par calcado dentro del mundo quality con ids casi identicos, desarrollo_caracteristicas_producto (franja 151, seis pasos, Quality by Design) y desarrollar_caracteristicas_producto (franja 211, cuatro pasos, Features). Los ids se distinguen por una sola letra y los dos tratan de convertir necesidades en caracteristicas con metas medibles.
- **212** | quality/descubrir_necesidades_cliente contra voice_of_customer_estrategico  
  Recolectar y priorizar necesidades contra la voz del cliente a nivel estrategico: temas vecinos, sano. FIGURA NUEVA, segunda del mismo tipo que franja 211: descubrir_necesidades_del_cliente (franja 113, seis pasos) y descubrir_necesidades_cliente (franja 212, tres pasos), ids que se distinguen solo por el articulo, los dos del mundo quality y los dos sobre descubrir necesidades.
- **215** | compras/traduce_stock_muerto_numeros contra gestion_inventario  
  Traducir el stock muerto a numeros duros de espacio y costo de mantener contra la gestion de inventario completa: angulos distintos, sano. FIGURA: costura ya confirmada en gestion_inventario, nueve pasos con bloques apilados. Es el nodo del plan de cirugia 2.
- **217** | quality/desarrollar_caracteristicas_producto contra voz_del_cliente_voc  
  Traducir necesidades en caracteristicas concretas contra observar al cliente en su entorno: momentos distintos, sano. FIGURA: costura ya confirmada en voz_del_cliente_voc.
- **226** | quality/eliminacion_causas_error_4 contra regla_simplificada_tolerancia_errores  
  El canal para que quien te ayuda reporte causas de error contra la regla de dos lineas para tolerar el primer error: angulos distintos, sano. FIGURA: sufijo _N vivo en el mundo quality, eliminacion_causas_error_4. Septimo miembro.
- **231** | quality/evaluacion_encuesta_calidad_proveedor contra criterios_seleccion_proveedores  
  Evaluar al proveedor con cuestionario y visita contra elegirlo con matriz ponderada: momentos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, ya registrada.
- **233** | quality/planificacion_inspeccion contra quality_audit  
  Planificar donde y como inspeccionar contra auditar la calidad: objetos distintos, sano. FIGURA NUEVA, tercera del mismo tipo que franja 211 y 212: planificacion_de_la_inspeccion (franja 150) y planificacion_inspeccion (franja 233), ids que se distinguen solo por el articulo, los dos del mundo quality y los dos sobre planificar la inspeccion con estaciones e instrucciones.
- **237** | quality/tipos_innovacion_i_ii contra starting_points_innovacion  
  Los dos tipos de innovacion contra el punto de partida push o pull: angulos distintos, sano. FIGURA: par calcado del nucleo con el mundo, tipos_innovacion_i_ii contra innovacion_tipo_ii (franja 143 y 149), ya registrado en la cola de 346.
- **238** | health_safety/preguntar_que_no_quien contra five_whys_inversion_proporcional  
  Preguntar que paso en vez de quien fue contra los cinco porques con inversion proporcional: temas vecinos, sano. FIGURA: costura en five_whys_inversion_proporcional, ya registrada en franja 156.
- **239** | quality/establecer_metas_caracteristicas contra metas_vs_proposito  
  Fijar la meta medible de cada caracteristica del producto contra la critica de Goodhart: angulos distintos, sano. FIGURA: costura ya confirmada en metas_vs_proposito, catorce pasos con los cinco ultimos en otro tema (el objetivo declarado del cliente y el seguimiento posterior al contrato).
- **243** | quality/distincion_causas_comunes_especiales contra curse_cinco_culpas  
  No informar defectos individuales cuando el proceso esta en control contra facilitar los cinco porques sin culpables: temas vecinos, sano. FIGURA: par calcado dentro del mundo quality, distincion_causas_comunes_especiales (franja 243) con su hermano de sufijo distincion_causas_comunes_especiales_2 (franja 187). Los dos mandan verificar el control estadistico antes de investigar el defecto puntual y dirigir el esfuerzo al sistema en vez de a la persona.
- **246** | exportacion/proteccion_propiedad_intelectual_2 contra patentes_startup  
  Registrar la propiedad intelectual en cada mercado destino contra el proceso de patente provisional: momentos distintos, sano. FIGURA: sufijo _N vivo, proteccion_propiedad_intelectual_2, esta vez en el mundo exportacion y no en quality. Octavo miembro.
- **254** | quality/value_non_value_added_analysis contra plan_mejora_procesos  
  Clasificar cada paso en valor agregado o desperdicio contra el plan de mejora de procesos: metodos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **261** | environmental/modelo_lubin_esty_4_etapas contra economia_circular_como_modelo_de_negocio  
  Diagnosticar en cual de las cuatro etapas de madurez estas contra la economia circular como modelo: angulos distintos, sano. FIGURA: costura en economia_circular_como_modelo_de_negocio, ya registrada en franja 124.
- **265** | quality/distincion_causas_especiales_comunes contra five_whys_inversion_proporcional  
  Verificar el control estadistico antes de ajustar el proceso contra los cinco porques: temas vecinos, sano. FIGURA NUEVA y fuerte: el calcado de causas comunes y especiales en el mundo quality es un TRIO con ids permutados. distincion_causas_comunes_especiales (franja 243), distincion_causas_comunes_especiales_2 (franja 187) y distincion_causas_especiales_comunes (franja 265). Los tres mandan lo mismo: verificar el control estadistico antes de investigar el defecto puntual, no tratar cada caso como causa especial si el sistema es estable, y dirigir el esfuerzo al sistema. El tercero invierte el orden de las dos palabras en el id.
- **267** | environmental/identificacion_proveedores_criticos contra criterios_seleccion_proveedores  
  Priorizar proveedores criticos por impacto y riesgo ambiental contra elegirlos con matriz ponderada: angulos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, ya registrada.
- **269** | quality/desarrollar_caracteristicas_proceso_2 contra definicion_producto_proyecto  
  Disenar el proceso que crea y entrega tu producto contra definir el producto y el alcance del proyecto: momentos distintos, sano. FIGURA: sufijo _N vivo, desarrollar_caracteristicas_proceso_2, ya nombrado en franja 201.
- **273** | quality/establecimiento_capacidad_proceso contra plan_mejora_procesos  
  Probar la mejora y confirmar la capacidad del proceso contra el plan de mejora de procesos: momentos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **276** | quality/eliminacion_causas_error_4 contra five_whys_inversion_proporcional  
  El canal para que reporten causas de error contra los cinco porques: momentos distintos, sano. FIGURAS: las dos ya registradas, sufijo _N vivo en eliminacion_causas_error_4 y costura en five_whys_inversion_proporcional.
- **280** | quality/politica_de_calidad contra traspaso_ventas_cuentas  
  La politica de calidad y a quien sumas al equipo contra que lo que prometes al vender sea lo que entregas: objetos distintos, sano. FIGURA NUEVA: par calcado DENTRO DEL NUCLEO, verificado leyendo los dos nodos completos. traspaso_ventas_cuentas (franja 280) y desconexion_ventas_experiencia (franja 161) son los dos del dominio core y narran el mismo traspaso entre vender y entregar: trazar como pasa hoy la informacion, anotar lo prometido antes de cerrar, montar un paso fijo o reunion de traspaso, y revisar cada tanto si lo prometido coincide con lo entregado. El segundo agrega el incentivo de quien vende y el CRM.
- **281** | quality/definiciones_operacionales_2 contra metricas_calidad  
  Definir el metodo de prueba y el criterio de aceptacion contra definir y documentar una metrica: objetos vecinos, sano. FIGURA: sufijo _N vivo en el mundo quality, definiciones_operacionales_2. Noveno miembro.
- **291** | quality/dmaic_fase_improve contra plan_mejora_procesos  
  La fase Improve con diseno de experimentos, factoriales y RSM contra el plan de mejora de procesos: el mundo profundiza con metodo propio, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **295** | exportacion/proteccion_propiedad_intelectual_internacional contra patentes_startup  
  Registrar la propiedad intelectual en cada mercado destino contra el proceso de patente provisional: momentos distintos, sano. FIGURAS, dos. Pais cableado ya registrado: el nodo del mundo manda consultar stopfakes.gov y uspto.gov y usar el PCT y el Protocolo de Madrid. Y una NUEVA: par calcado dentro del mundo exportacion, proteccion_propiedad_intelectual_2 (franja 246) y proteccion_propiedad_intelectual_internacional (franja 295) mandan lo mismo, registrar patente y marca en cada pais objetivo antes de operar e incluir clausulas de proteccion en los acuerdos de licenciamiento.
- **304** | quality/especificacion_requisitos_proveedores contra criterios_seleccion_proveedores  
  Especificar los requisitos de calidad al proveedor contra elegirlo con matriz ponderada: momentos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, ya registrada.
- **305** | quality/establecimiento_metas contra metas_objetivos_smart_innovacion  
  Fijar metas de calidad a 30, 60 y 90 dias contra las metas SMART de innovacion: angulos distintos, sano. FIGURA: numero de paso en el titulo, establecimiento_metas se llama Paso 10. Ya registrada como clase. CORRECCION MIA sobre el registro: franja 247, medicion_calidad, se llama Paso 3 y quedo clasificado D por omision mia. Es miembro de esta misma figura y asi debe contarse en el informe.
- **307** | quality/eliminacion_causas_error contra regla_simplificada_tolerancia_errores  
  El formulario para reportar obstaculos contra la regla de dos lineas: angulos distintos, sano. FIGURAS, dos. Numero de paso en el titulo: eliminacion_causas_error se llama Paso 11. Y NUEVA: par calcado dentro del mundo quality, eliminacion_causas_error (franja 307) con eliminacion_causas_error_4 (franja 226 y 276). Los dos montan el mismo canal, un formulario simple para reportar causas de error, acuse rapido a quien avisa, asignar a quien resuelve y comunicar la decision de vuelta.
- **311** | health_safety/new_view_investigation contra five_whys_inversion_proporcional  
  La investigacion bajo la New View, separada de lo disciplinario, contra los cinco porques: temas vecinos, sano. FIGURA: costura en five_whys_inversion_proporcional, ya registrada.
- **317** | franquicias/proceso_llamada_inicial_venta contra apertura_llamada_venta_grande  
  El mundo especializa la primera llamada a la venta de franquicias sobre la apertura generica de una venta grande: sano. FIGURA: par calcado de franquicias, proceso_llamada_inicial_venta con proceso_primera_llamada, ya registrado.
- **319** | quality/contacto_con_el_cliente_2 contra documento_quien_es_quien_equipo  
  Quien tiene contacto directo con el cliente contra el documento de quien es quien del equipo: objetos distintos, sano. FIGURA: sufijo _N vivo en el mundo quality, contacto_con_el_cliente_2. Decimo miembro.
- **323** | quality/distincion_causas_comunes_especiales_2 contra regla_simplificada_tolerancia_errores  
  Causas comunes contra especiales, contra la regla de dos lineas: niveles distintos, sano. FIGURA: sufijo _N vivo y trio calcado, los dos ya registrados en franja 187 y 265.
- **325** | quality/matriz_de_control_de_proceso contra metricas_calidad  
  La matriz de control de proceso contra definir y documentar una metrica: objetos distintos, sano. FIGURA: par calcado del mundo quality, matriz_de_control_de_proceso con plan_de_control, ya registrado.
- **327** | quality/seleccionar_diseno_general_proceso contra plan_mejora_procesos  
  Elegir el diseno general del proceso con diagrama de alto nivel y FMEA contra el plan de mejora de procesos: momentos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **331** | exportacion/evaluacion_preparacion_empresa_exportar contra tres_preguntas_carrera  
  Evaluar si tu empresa esta lista para exportar contra las tres preguntas antes de saltar a emprender: momentos distintos, sano. FIGURA: pais cableado, el nodo del mundo manda hacer la evaluacion formal en export.gov. Ya registrada como figura en la ficha de marco-pais.
- **335** | quality/auditoria_producto contra metricas_calidad  
  Auditar el producto terminado contra definir y documentar una metrica: objetos distintos, sano. FIGURA NUEVA, cuarta del mismo tipo que franja 211, 212 y 233: auditoria_de_producto (franja 152, siete pasos) y auditoria_producto (franja 335, cuatro pasos), ids que se distinguen solo por el de, los dos del mundo quality y los dos sobre auditar el producto terminado eligiendo etapa y muestra.
- **338** | quality/contacto_con_el_cliente contra documento_quien_es_quien_equipo  
  Quien tiene contacto directo con el cliente contra el documento de quien es quien: objetos distintos, sano. FIGURA NUEVA: par calcado dentro del mundo quality, contacto_con_el_cliente (franja 338) con contacto_con_el_cliente_2 (franja 319). Los dos mandan identificar a quien trata con el cliente, prepararlo para atender bien y reconocer que esa persona construye la percepcion del negocio.
- **343** | quality/equipo_interdepartamental_calidad contra five_whys_inversion_proporcional  
  Convocar a todas las areas de la cadena que genera el defecto, con datos y no acusaciones, contra los cinco porques: metodos distintos, sano. FIGURA: costura en five_whys_inversion_proporcional, ya registrada.
- **361** | health_safety/gestion_de_errores contra regla_simplificada_tolerancia_errores  
  Reducir y contener el error por diseno contra la regla de dos lineas: niveles distintos, sano. FIGURA NUEVA: par calcado dentro del mundo health_safety, principios_gestion_error (franja 277) y gestion_de_errores (franja 361). Los dos son Error Management y mandan lo mismo: disenar medidas informativas y de contencion, no apoyarse en sanciones ni exhortaciones, y distinguir los factores aleatorios de los sistematicos.
- **362** | quality/accion_correctiva_2 contra no_sacrificar_calidad_por_velocidad  
  Pasar de detectar a prevenir con analisis de tendencias contra el andon cord y la deuda tecnica: temas vecinos, sano. FIGURAS, dos. Sufijo _N vivo en el mundo quality, accion_correctiva_2, undecimo miembro. Y NUEVA: par calcado con accion_correctiva_6 (franja 164), los dos titulados Accion Correctiva y los dos con la misma doctrina, buscar la causa raiz sistemica en vez de culpar a alguien, asignar responsables y verificar que el problema no vuelva.
- **367** | quality/descubrir_necesidades_del_cliente contra ganar_comprension_del_cliente  
  El metodo fino del descubrimiento de necesidades contra ganar comprension profunda del cliente: temas vecinos, sano. FIGURA NUEVA: costura visible en el nucleo, ganar_comprension_del_cliente tiene once pasos en dos bloques apilados. Los pasos 1 a 6 son la investigacion del cliente y su flujo de trabajo; los pasos 7 a 11 son otra narracion entera sobre elegir un CRM, definir entre cinco y diez datos prioritarios y llenar la ficha. Es el mismo nodo cuyas herramientas con nombre propio quedaron anotadas en franja 71.
- **370** | quality/tipos_innovacion_i_ii contra seis_formas_innovar_perfil_cliente  
  Los dos tipos de innovacion contra las seis formas de innovar desde el perfil del cliente: metodos distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **371** | franquicias/velocidad_crecimiento_franquicia_2 contra decision_consciente_de_crecimiento  
  Encontrar tu velocidad correcta para crecer en franquicia contra el crecimiento como decision consciente: angulos distintos, sano. FIGURA: sufijo _N vivo, velocidad_crecimiento_franquicia_2, esta vez en el mundo franquicias. Duodecimo miembro.
- **387** | franquicias/velocidad_crecimiento_franquicia contra eleccion_ritmo_crecimiento  
  Comparar el tiempo de abrir una unidad propia contra abrir varias franquicias a la vez, contra elegir el ritmo de crecimiento: angulos distintos, sano. FIGURA NUEVA: par calcado dentro del mundo franquicias, velocidad_crecimiento_franquicia (franja 387) con velocidad_crecimiento_franquicia_2 (franja 371). Los dos deciden a que velocidad crecer mirando la competencia y la saturacion del territorio; el segundo agrega el limite de distancia manejable y el soporte real.
- **393** | quality/formulacion_teorias_causa contra five_whys_inversion_proporcional  
  Formular teorias de causa con afinidad, espina de pescado y FMEA contra los cinco porques: metodos distintos, sano. FIGURA: costura en five_whys_inversion_proporcional, ya registrada.
- **395** | quality/seleccion_fuente_unica_multiple contra criterios_seleccion_proveedores  
  Elegir entre fuente unica y multiples proveedores contra la matriz ponderada de seleccion: angulos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, ya registrada.
- **400** | quality/innovacion_tipo_ii contra how_might_we_hmw  
  Hacerlo mas grande, mas pequeno o combinarlo contra reformular el problema como Como podriamos: metodos distintos, sano. FIGURA NUEVA: segundo par calcado DENTRO DEL NUCLEO. how_might_we_briefs (franja 296) y how_might_we_hmw (franja 400) son los dos del nucleo y mandan lo mismo: tomar el objetivo o problema central, reformularlo con la formula Como podriamos, y verificar que la pregunta no quede ni tan amplia que sea imposible ni tan estrecha que cierre las opciones.
- **404** | franquicias/seo_para_captacion_de_franquiciados contra seo_long_tail  
  SEO para captar franquiciados contra la estrategia long tail: metodos vecinos, sano. FIGURA: herramientas con nombre propio, esta vez en el nodo del NUCLEO, seo_long_tail cita Google Keyword Planner y manda contratar freelancers en oDesk o Elance. Se anotan sin asumir que murieron.
- **406** | quality/eventos_kaizen_rie contra plan_mejora_procesos  
  El evento de mejora rapida semana a semana contra el plan de mejora de procesos: momentos distintos, sano. FIGURAS, dos. Costura ya confirmada en plan_mejora_procesos. Y NUEVA: par calcado dentro del mundo quality, kaizen_mejora_continua (franja 302) con eventos_kaizen_rie (franja 406). Los dos montan el mismo evento kaizen de dias con equipo multidisciplinario, cambios inmediatos, medicion antes y despues y control posterior.
- **413** | franquicias/analisis_competencia_franquicias contra analisis_competitivo  
  Analizar a fondo a los competidores directos de franquicia contra el analisis competitivo generico: el mundo especializa, sano. FIGURA: pais cableado, el nodo del mundo manda obtener y analizar los FDD de los competidores, documento regulatorio estadounidense, sin condicion de pais. Ya registrada como figura en la ficha de marco-pais.
- **416** | quality/distincion_causas_comunes_especiales_2 contra curse_cinco_culpas  
  Causas comunes contra especiales, contra facilitar los cinco porques sin culpables: temas vecinos, sano. FIGURA: sufijo _N vivo y trio calcado, ya registrados en franja 187 y 265.
- **418** | health_safety/principios_gestion_error contra curse_cinco_culpas  
  Los principios de gestion del error contra facilitar los cinco porques sin culpables: niveles distintos, sano. FIGURA: par calcado en health_safety, principios_gestion_error con gestion_de_errores, ya registrado en franja 361.
- **420** | quality/revision_progreso contra rendicion_de_cuentas_del_equipo  
  El proceso formal de revision de progreso contra la rendicion de cuentas de punta a punta: objetos distintos, sano. FIGURA NUEVA: par calcado dentro del mundo quality, revision_progreso (franja 420) con revision_progreso_breakthrough (franja 133 y 399). Los dos fijan puntos de revision periodicos, comparan el estado contra la meta con un formato estandar y reparten responsabilidad sobre las brechas.
- **421** | environmental/sistema_take_back contra economia_circular_como_modelo_de_negocio  
  El sistema de recuperacion take back con desensamblaje y acuerdos logisticos contra la economia circular: el mundo mas concreto, sano. FIGURA: costura en economia_circular_como_modelo_de_negocio, ya registrada en franja 124.
- **425** | environmental/eco_efectividad_2 contra economia_circular_como_modelo_de_negocio  
  Eco efectividad contra la economia circular como modelo: angulos distintos, sano. FIGURAS, dos, las dos NUEVAS. Sufijo _N vivo en el mundo environmental, eco_efectividad_2, decimotercer miembro y primero de ese mundo. Y par calcado con eco_efectividad (franja 80 y 124): los dos mandan analizar el ciclo de vida completo, cuestionar el diseno en vez de solo hacerlo mas eficiente y redisenar para que los materiales sean nutrientes biologicos o tecnicos. IMPORTANTE para la adjudicacion: eco_efectividad es el nodo de la unica violacion candidata de este tramo, franja 124.
- **426** | franquicias/analisis_competencia_franquicias contra brief_competitivo  
  Analizar a los competidores directos de franquicia contra escribir el brief competitivo y la razon de compra: angulos distintos, sano. FIGURA: pais cableado, los FDD del nodo del mundo, ya registrada y ya vista en franja 413.
- **433** | quality/tipos_innovacion_i_ii contra portafolio_innovacion_diversificado  
  Los dos tipos de innovacion contra repartir el portafolio entre incremental y disruptivo: objetos distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **434** | environmental/innovacion_abierta_externa contra open_business_models  
  Innovacion abierta y colaboracion externa contra los modelos de negocio abiertos: temas iguales pero el mundo tira a lo ambiental y el nucleo al conocimiento ocioso. Sano. FIGURAS, dos. Herramienta con nombre propio en el nodo del NUCLEO: open_business_models manda evaluar plataformas intermediarias como InnoCentive. Se anota sin asumir que murio. Y una observacion que dejo para el auditor sin marcarla como figura cerrada: open_business_models es un TERCER nodo del nucleo de la familia de innovacion abierta, junto a innovacion_abierta y open_innovation_ideacion, que ya estan registrados como par calcado desde la cola de 346.
- **440** | compras/define_punto_maximo_de_stock contra gestion_inventario  
  Calcular tu punto de reorden con uso semanal, tiempo de entrega y colchon contra la gestion de inventario completa: el mundo mas concreto, sano. FIGURA: costura ya confirmada en gestion_inventario, el nodo del plan de cirugia 2.
- **445** | health_safety/enfoque_situacional_vs_personal contra five_whys_inversion_proporcional  
  Priorizar el rediseno de la tarea sobre la medida centrada en la persona contra los cinco porques: temas vecinos, sano. FIGURA: costura en five_whys_inversion_proporcional, ya registrada.
- **446** | quality/sistema_pull_push contra programacion_produccion  
  Pasar de push a pull con kanbans contra el lote economico y el run out time: metodos distintos, sano. FIGURA: par calcado del nucleo, programacion_produccion con produccion_scheduling_balance_objetivos, ya registrado.
- **453** | quality/politica_calidad_organizacional contra plan_gestion_calidad  
  Redactar y comunicar la politica de calidad contra el plan de gestion de calidad: objetos distintos, sano. FIGURA NUEVA: par calcado dentro del mundo quality, politica_de_calidad (franja 280) con politica_calidad_organizacional (franja 453). Los dos mandan redactar la declaracion de politica, dejarla por escrito en lo que entregas a quien se suma o en el manual, comunicarla y revisar despues que se cumpla.
- **459** | quality/benchmarking_7_pasos_juran contra plan_mejora_procesos  
  Los siete pasos del benchmarking de Juran contra el plan de mejora de procesos: metodos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **460** | health_safety/falla_sistemica_vs_error_individual contra five_whys_inversion_proporcional  
  Mapear la cadena organizacional del incidente con un modelo de causalidad contra los cinco porques: marcos distintos, sano. FIGURAS, dos. Costura en five_whys_inversion_proporcional, ya registrada. Y una NUEVA que no es un par sino una FAMILIA, y por eso la dejo censada aqui completa: el mundo health_safety tiene al menos trece nodos que predican la misma doctrina, no culpar a la persona y arreglar el sistema. Son responsabilidad_prospectiva (101), rendicion_cuentas_prospectiva (114), responsabilidad_sistemica (117), revision_de_aprendizaje (156), desajuste_autoridad_responsabilidad (203), desajuste_tarea_persona (221), preguntar_que_no_quien (238), principios_gestion_error (277), new_view_investigation (311), abandonar_arreglos_rapidos (318), gestion_de_errores (361), enfoque_situacional_vs_personal (445 y 452) y falla_sistemica_vs_error_individual (460). Tres de ellos ya quedaron registrados como calcados dos a dos. La observacion para el auditor es que la figura aqui no es un par duplicado sino una doctrina repartida en trece piezas que se pisan entre si.
- **469** | quality/innovacion_tipo_ii contra asociacion_de_ideas  
  Hacerlo mas grande, mas pequeno o combinarlo contra el mecanismo de asociacion de ideas: metodos distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **470** | quality/sistema_responsabilidad_gerencial_2 contra regla_simplificada_tolerancia_errores  
  Asumir el sistema completo como tu responsabilidad contra la regla de dos lineas: niveles distintos, sano. FIGURAS, dos, las dos NUEVAS. Sufijo _N vivo en el mundo quality, sistema_responsabilidad_gerencial_2, decimocuarto miembro. Y par calcado con mejora_del_sistema_responsabilidad_gerencial (franja 191): los dos mandan mirar el sistema completo mas alla de la maquina, recoger datos de los errores y asumir tu la responsabilidad del resultado en vez de atribuirlo a quien opera.
- **473** | quality/customer_needs_spreadsheet contra voz_del_cliente_voc  
  La matriz de clientes contra necesidades contra observar al cliente en su entorno: momentos distintos, sano. FIGURA: costura ya confirmada en voz_del_cliente_voc.
- **474** | environmental/marcos_pensamiento_dfe contra how_might_we_framing  
  Elegir un marco conceptual de diseno sostenible contra reformular el problema como Como podriamos: marcos distintos, sano. FIGURA NUEVA, amplia la de franja 400: el calcado de How Might We en el NUCLEO es un TRIO, no un par. how_might_we_briefs (296), how_might_we_hmw (400) y how_might_we_framing (474). Los tres mandan redactar el problema con la formula y verificar que la pregunta no quede ni demasiado general ni demasiado estrecha.
- **477** | quality/diagnostico_antes_remedio contra five_whys_inversion_proporcional  
  El diagnostico antes que el remedio contra los cinco porques: angulos vecinos, sano. FIGURA: costura en five_whys_inversion_proporcional, ya registrada.
- **481** | quality/costo_de_calidad_3 contra metricas_calidad  
  El costo de calidad como porcentaje de ventas contra definir y documentar una metrica: objetos distintos, sano. FIGURAS, tres. Sufijo _N vivo en el mundo quality, costo_de_calidad_3, decimoquinto miembro. Numero de paso en el titulo, se llama Paso 4. Y NUEVA: par calcado con costo_de_calidad_diagnostico (franja 381), los dos mandan sumar todos los componentes del costo de calidad, usar la cifra como argumento para decidir donde invertir y seguir su tendencia en el tiempo como medida de madurez.
- **482** | quality/plan_de_control contra quality_audit  
  El plan de control contra auditar la calidad: objetos distintos, sano. FIGURA: par calcado del mundo quality, plan_de_control con matriz_de_control_de_proceso, ya registrado.
- **483** | quality/revision_diseno contra voz_del_cliente_voc  
  La revision formal de diseno contra observar al cliente en su entorno: objetos distintos, sano. FIGURA: costura ya confirmada en voz_del_cliente_voc.
- **485** | environmental/diversidad_en_diseno contra diseno_para_sostenibilidad_cradle_to_cradle  
  Respetar la diversidad cultural y ecologica en el diseno contra el mapeo cradle to cradle: angulos distintos, sano. FIGURA NUEVA: par calcado dentro del mundo environmental, respetar_la_diversidad (franja 364) con diversidad_en_diseno (franja 485). Los dos mandan investigar las condiciones locales, evitar la solucion estandarizada global y adaptar el diseno al entorno especifico.
- **486** | health_safety/responsabilizacion_del_trabajador contra curse_cinco_culpas  
  Revisar si tus politicas de seguridad culpan siempre a las personas contra facilitar los cinco porques sin culpables: temas vecinos, sano. FIGURA: responsabilizacion_del_trabajador es un miembro mas de la familia de trece nodos de health_safety censada en franja 460. Con este van catorce.
- **488** | quality/equipo_mejora_calidad_2 contra hr_calidad_gestion  
  Armar el equipo de mejora de calidad contra cuidar la calidad de todo el ciclo de vida del empleado: objetos distintos, sano. FIGURA: sufijo _N vivo, equipo_mejora_calidad_2, ya registrado en franja 168.
- **489** | quality/establecimiento_metas_de_calidad contra plan_gestion_calidad  
  Fijar metas de calidad validadas contra benchmarks contra el plan de gestion de calidad: objetos distintos, sano. FIGURA NUEVA: par calcado dentro del mundo quality, establecimiento_metas_de_calidad (franja 256 y 489) con establecer_estandares_desempeno (franja 345). Los dos mandan definir metas medibles, validar con benchmarking que ya fueron alcanzadas por otros, asegurar equidad entre roles comparables y vincularlas al scorecard.
- **494** | quality/innovacion_tipo_ii contra brainstorming_efectivo  
  Hacerlo mas grande, mas pequeno o combinarlo contra las reglas del brainstorming: metodos distintos, sano. FIGURAS, dos. Par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado. Y NUEVA: el nucleo tiene un TRIO de nodos sobre las reglas de la sesion de lluvia de ideas, reglas_brainstorming (franja 149), brainstorming_divergente (franja 193) y brainstorming_efectivo (franja 494). Los tres mandan diferir el juicio, construir sobre las ideas de otros y separar la generacion de la seleccion.
- **497** | quality/pocos_vitales_muchos_utiles contra portfolio_management  
  Clasificar proyectos en vitales pocos y utiles muchos contra gestionar el portafolio con Go Kill: angulos distintos, sano. FIGURA: par calcado proyectos_vitales_pocos con pocos_vitales_muchos_utiles, ya registrado en franja 181.
- **501** | quality/accion_correctiva_crosby contra quality_audit  
  La accion correctiva sistematica de Crosby contra los cuatro pasos de correr una auditoria: objetos vecinos, sano. FIGURA NUEVA, amplia la de franja 362: el calcado de accion correctiva en el mundo quality es un TRIO. accion_correctiva_2 (362), accion_correctiva_6 (164) y accion_correctiva_crosby (501). Los tres mandan investigar la causa raiz sin culpar a la persona, dejar el hallazgo documentado y asignar responsable del plan correctivo.
- **513** | quality/kaizen_mejora_continua contra plan_mejora_procesos  
  El evento kaizen contra el plan de mejora de procesos: momentos distintos, sano. FIGURAS: costura ya confirmada en plan_mejora_procesos, y par calcado kaizen_mejora_continua con eventos_kaizen_rie, ya registrado en franja 406.
- **517** | quality/definiciones_operacionales contra no_sacrificar_calidad_por_velocidad  
  Definiciones operacionales de calidad aceptable contra el andon cord y la deuda tecnica: objetos distintos, sano. FIGURA NUEVA: par calcado dentro del mundo quality, definiciones_operacionales (franja 517) con definiciones_operacionales_2 (franja 281). Los dos mandan acordar el criterio de aceptacion sin ambiguedad y verificar que varias personas lo apliquen igual.
- **518** | quality/innovacion_tipo_ii contra what_if_questions  
  Hacerlo mas grande, mas pequeno o combinarlo contra las preguntas Que pasaria si: metodos distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **519** | quality/revision_progreso contra plan_gestion_calidad  
  El proceso formal de revision de progreso contra el plan de gestion de calidad: objetos distintos, sano. FIGURA: par calcado revision_progreso con revision_progreso_breakthrough, ya registrado en franja 420.
- **527** | compras/ofrece_valor_no_economico contra ecuacion_de_valor  
  Ofrecer valor no economico cuando el precio se estanca contra la ecuacion de valor: lados opuestos de la mesa, sano. FIGURA NUEVA: tercer par calcado DENTRO DEL NUCLEO. ecuacion_de_valor_cliente (franja 207 y 242) y ecuacion_de_valor (franja 527) mandan lo mismo, medir que tan grande percibe el cliente su problema contra el costo total, y no pasar a la solucion hasta que la balanza se incline.
- **529** | quality/definir_mision_organizacional contra posicionamiento_de_empresa  
  Definir la mision organizacional contra escribir el posicionamiento de la empresa: objetos distintos, sano. FIGURA NUEVA: costura visible en el nucleo, posicionamiento_de_empresa tiene nueve pasos en dos bloques apilados. Los pasos 1 a 5 escriben y validan la declaracion de posicionamiento; los pasos 6 a 9 son otra narracion entera sobre redactar la historia completa de la empresa, usar cartas fundacionales como referencia y verificar que las personas clave la entiendan.
- **535** | exportacion/enfoque_paso_a_paso_investigacion_mercado contra hipotesis_de_tamano_de_mercado  
  El enfoque paso a paso para investigar mercados de exportacion contra estimar TAM y SAM: metodos distintos, sano. FIGURA: pais cableado, el nodo del mundo manda obtener las estadisticas del U.S. Census. Ya registrada.
- **536** | quality/accion_correctiva_4 contra manejo_de_quejas_entre_ejecutivos  
  Escalar el problema de calidad al siguiente nivel jerarquico contra manejar una queja entre ejecutivos: objetos distintos, sano. FIGURAS, tres. Sufijo _N vivo en quality, accion_correctiva_4, decimosexto miembro. Numero de paso en el titulo, se llama Paso 6. Y NUEVA, amplia la de franja 501: la familia de accion correctiva del mundo quality tiene CUATRO miembros, no tres: accion_correctiva_2, accion_correctiva_4, accion_correctiva_6 y accion_correctiva_crosby.
- **541** | compras/domina_lo_que_compras contra criterios_seleccion_proveedores  
  Dominar lo que compras antes de negociarlo contra la matriz ponderada de seleccion: momentos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, ya registrada.
- **542** | quality/clasificacion_de_seriedad_de_defectos_2 contra metricas_calidad  
  Clasificar la seriedad de los defectos para el proveedor contra definir y documentar una metrica: objetos distintos, sano. FIGURAS, dos, las dos NUEVAS. Sufijo _N vivo en quality, clasificacion_de_seriedad_de_defectos_2, decimoseptimo miembro. Y par calcado con clasificacion_seriedad_defectos (franja 493): los dos mandan listar los defectos posibles, asignarles nivel critico, mayor o menor, y usar esa clasificacion para enfocar la inspeccion.
- **544** | quality/entrenamiento_para_breakthrough contra entrenamiento_funcional_empleados  
  Entrenamiento por niveles de cinturon contra el entrenamiento funcional medido antes y despues: objetos distintos, sano. FIGURA NUEVA, y la traigo para que el auditor decida si cuenta: el nodo del mundo manda certificar a la gente ante ASQ y el Juran Institute. No son herramientas de software sino organismos certificadores con nombre propio, pero son la misma especie de dependencia externa cableada en un paso. Se anotan sin asumir nada.
- **546** | seguridad_digital/evaluar_controles contra quality_audit  
  Evaluar los controles implementados contra los cuatro pasos de correr una auditoria de calidad: objetos distintos, sano. FIGURA NUEVA, y es la primera que sale del mundo seguridad_digital: el nodo cablea un marco regulatorio estadounidense. Sus pasos van numerados como Tarea A-2, A-3 y A-4 de un documento externo que el lector no tiene, y el entregable se llama POA&M, Plan of Action and Milestones, terminologia del marco federal de Estados Unidos. Es marco-pais y ademas andamiaje de otro documento asomando en los pasos.
- **548** | quality/consejo_de_calidad contra plan_gestion_calidad  
  El consejo de calidad de Juran contra el plan de gestion de calidad: objetos distintos, sano. FIGURA NUEVA, amplia la de franja 163: la familia del consejo de calidad en quality tiene TRES miembros, no dos. consejo_calidad_2 (163), consejo_de_calidad_y_rol_del_director (173) y consejo_de_calidad (548). Los tres mandan reunir a quienes deciden, elegir y priorizar los proyectos, asignarles recursos y revisar el avance reconociendo logros.
- **554** | quality/roi_proyectos_calidad contra propuesta_gasto_capital  
  El ROI de un proyecto de mejora de calidad contra la guia para analizar un gasto de capital: niveles distintos, sano. FIGURA NUEVA: costura visible en el nucleo, propuesta_gasto_capital tiene doce pasos en dos bloques apilados que cuentan el mismo analisis dos veces. Los pasos 1 a 5 recopilan costos, estiman beneficios, calculan NPV, payback e IRR y redactan la propuesta; los pasos 6 a 12 vuelven a empezar con costos de hardware y software por trimestre, cuatro tipos de beneficio, flujo de caja neto trimestral, valor presente neto y presentacion a los ejecutivos.
- **556** | health_safety/ciclo_de_culpa contra curse_cinco_culpas  
  El ciclo de culpar y entrenar contra facilitar los cinco porques sin culpables: temas vecinos, sano. FIGURA: ciclo_de_culpa es un miembro mas de la familia de health_safety censada en franja 460 y ampliada en 486. Con este van quince.
- **562** | quality/medicion_calidad contra afinar_motor_crecimiento  
  Medir la calidad por area con linea base y graficos visibles contra afinar el motor de crecimiento con experimentos: objetos distintos, sano. FIGURA: numero de paso en el titulo, medicion_calidad se llama Paso 3. Esta es la correccion que anuncie en franja 305: en franja 247 la clasifique D por omision y aqui queda registrada donde corresponde.
- **564** | quality/identificar_caracteristicas_metas_proceso contra plan_mejora_procesos  
  Descomponer el proceso en caracteristicas y metas contra el plan de mejora de procesos: momentos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **566** | quality/matriz_de_control_de_proceso contra plan_gestion_calidad  
  La matriz de control de proceso contra el plan de gestion de calidad: niveles distintos, sano. FIGURA: par calcado matriz_de_control_de_proceso con plan_de_control, ya registrado.
- **567** | quality/politica_de_calidad contra cultura_de_buena_empresa  
  La politica de calidad y a quien sumas al equipo contra construir una buena empresa como fin en si mismo: angulos distintos, sano. FIGURA: par calcado politica_de_calidad con politica_calidad_organizacional, ya registrado en franja 453.
- **569** | quality/accion_correctiva_5 contra five_whys_inversion_proporcional  
  Documentar cada problema y darle seguimiento hasta el cierre contra los cinco porques: metodos vecinos, sano. FIGURAS, dos. Sufijo _N vivo en quality, accion_correctiva_5, decimoctavo miembro. Y amplia la familia de franja 501 y 536: accion correctiva en el mundo quality tiene CINCO miembros. accion_correctiva_2, accion_correctiva_4, accion_correctiva_5, accion_correctiva_6 y accion_correctiva_crosby.
- **571** | quality/equipo_mejora_calidad_2 contra hr_como_control_de_calidad_gerencial  
  Armar el equipo de mejora de calidad contra usar el area de personas para corregir a tus gerentes: objetos distintos, sano. FIGURA: sufijo _N vivo, equipo_mejora_calidad_2, ya registrado.
- **574** | exportacion/screening_mercados_potenciales contra etapa_scoping  
  Screening de mercados de exportacion contra la etapa de investigacion preliminar rapida: marcos distintos, sano. FIGURA: pais cableado, el U.S. Census Bureau y el U.S. Commercial Service del nodo del mundo, ya registrada en franja 199.
- **582** | quality/analisis_flujo_proceso_servicio contra customer_journey_mapping  
  El diagrama de flujo del servicio con linea de invisibilidad contra el mapeo del viaje del cliente: metodos vecinos, sano. FIGURA NUEVA: costura visible en el nucleo, customer_journey_mapping tiene diez pasos en dos bloques apilados. Los pasos 1 a 5 mapean el viaje y priorizan mejoras por punto de contacto; los pasos 6 a 10 son otra narracion entera, con varios viajes por tema, el diagnostico de donde se pasan la responsabilidad los departamentos, la cuantificacion del mal servicio, la silla vacia del cliente en las reuniones y la consolidacion de herramientas internas.
- **583** | quality/sistema_responsabilidad_gerencial_2 contra curse_cinco_culpas  
  Asumir el sistema completo como tu responsabilidad contra facilitar los cinco porques sin culpables: marcos distintos, sano. FIGURA: par calcado sistema_responsabilidad_gerencial_2 con mejora_del_sistema_responsabilidad_gerencial, ya registrado en franja 470.
- **584** | quality/compra_por_precio_mas_bajo_como_error contra criterios_seleccion_proveedores  
  El riesgo de comprar solo por el precio mas bajo contra la matriz ponderada de seleccion: angulos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, ya registrada.
- **587** | quality/accion_correctiva_sistematica contra five_whys_inversion_proporcional  
  La accion correctiva sistematica con revision diaria, semanal y mensual contra los cinco porques: metodos vecinos, sano. FIGURAS, dos. Numero de paso en el titulo, accion_correctiva_sistematica se llama Paso 6 de Crosby. Y amplia la familia de franja 501, 536 y 569: accion correctiva en el mundo quality tiene SEIS miembros. accion_correctiva_2, accion_correctiva_4, accion_correctiva_5, accion_correctiva_6, accion_correctiva_crosby y accion_correctiva_sistematica. Los dos ultimos son ademas casi el mismo texto: los dos documentan cada problema en una ficha, lo revisan a diario, escalan lo que no se resuelve y ordenan por gravedad.
- **589** | health_safety/sesgo_retrospectivo_hindsight_2 contra reconocer_el_sesgo_narrativo  
  El sesgo de mirar hacia atras contra reconocer el sesgo narrativo: angulos vecinos, sano. FIGURA: sufijo _N vivo, sesgo_retrospectivo_hindsight_2, esta vez en el mundo health_safety. Decimonoveno miembro.
- **591** | quality/analisis_diagnostico_causa contra five_whys_inversion_proporcional  
  Analizar sintomas, formular teorias y probarlas con datos contra los cinco porques: metodos distintos, sano. FIGURA NUEVA, quinta del tipo de ids casi identicos: analisis_causa_raiz_diagnostico (franja 299) y analisis_diagnostico_causa (franja 591), los dos del mundo quality, con las mismas dos palabras permutadas en el id y la misma secuencia de sintomas, teorias, prueba con datos y confirmacion de la causa raiz.
- **598** | quality/desarrollo_caracteristicas_producto contra customer_discovery  
  Quality by Design contra salir a hablar con clientes y probar un MVP: marcos distintos, sano. FIGURA: par calcado desarrollo_caracteristicas_producto con desarrollar_caracteristicas_producto, ya registrado en franja 211.
- **601** | quality/establecer_metas_de_calidad_basadas_en_mercado contra medicion_monitoreo_desempeno  
  Fijar metas de calidad por benchmarking contra medir y monitorear el desempeno de tu propuesta de valor: objetos distintos, sano. FIGURA NUEVA, amplia la de franja 489: la familia de fijar metas de calidad en quality es un TRIO. establecimiento_metas_de_calidad (256 y 489), establecer_estandares_desempeno (345) y establecer_metas_de_calidad_basadas_en_mercado (230 y 601). Los tres mandan validar la meta con benchmarking externo, revisar el historial interno y sostener una revision periodica.
- **608** | quality/programa_auditoria_calidad contra risk_audit  
  Definir el programa de auditoria (alcance, quien audita, cumplimiento o efectividad) contra auditar la gestion de riesgos: objetos distintos, sano. FIGURA NUEVA: familia de auditoria de calidad en el mundo quality, tres nodos que se pisan. auditoria_calidad (franja 107), principios_auditoria_calidad (franja 146) y programa_auditoria_calidad (franja 608). Los tres definen contra que se audita, quien audita y con que independencia, y como se documenta el hallazgo.
- **613** | quality/responsabilidad_gerencial_causas_comunes contra five_whys_inversion_proporcional  
  Distinguir causas comunes de especiales y asumir las del sistema contra los cinco porques: marcos distintos, sano. FIGURA NUEVA, amplia las de franja 265 y 470: en el mundo quality hay un RACIMO de al menos seis nodos sobre lo mismo, que la variacion del sistema es tuya y no de quien opera. distincion_causas_comunes_especiales (243), distincion_causas_comunes_especiales_2 (187), distincion_causas_especiales_comunes (265), mejora_del_sistema_responsabilidad_gerencial (191), sistema_responsabilidad_gerencial_2 (470) y responsabilidad_gerencial_causas_comunes (613).
- **619** | exportacion/enfoque_paso_a_paso_investigacion_mercado contra tipo_de_mercado_estrategia_competitiva  
  El enfoque paso a paso para investigar mercados de exportacion contra decidir en que tipo de mercado compites: objetos distintos, sano. FIGURA: pais cableado, el U.S. Census del nodo del mundo, ya registrada.
- **620** | quality/definicion_problema_moms_2 contra five_whys_inversion_proporcional  
  Redactar el enunciado del problema con los criterios MOMS contra los cinco porques: momentos distintos, sano. FIGURA: sufijo _N vivo en quality, definicion_problema_moms_2. Vigesimo miembro.
- **623** | quality/eliminacion_causas_error_2 contra regla_simplificada_tolerancia_errores  
  El formulario para reportar causas de error, con acuse y sorteo semanal, contra la regla de dos lineas: niveles distintos, sano. FIGURAS, tres. Sufijo _N vivo en quality, eliminacion_causas_error_2, vigesimo primer miembro. Numero de paso en el titulo, se llama Paso 11. Y amplia la de franja 307: la familia ECR del mundo quality tiene TRES miembros, eliminacion_causas_error, eliminacion_causas_error_2 y eliminacion_causas_error_4, y DOS de ellos se titulan exactamente Paso 11.
- **629** | quality/clasificacion_caracteristicas_calidad contra metricas_calidad  
  Clasificar caracteristicas y defectos para priorizar la inspeccion contra definir y documentar una metrica: objetos distintos, sano. FIGURA NUEVA, amplia la de franja 542: la familia de clasificacion de defectos en quality es un TRIO. clasificacion_seriedad_defectos (493), clasificacion_de_seriedad_de_defectos_2 (542) y clasificacion_caracteristicas_calidad (629). Los tres mandan derivar la lista de caracteristicas de las especificaciones, armar la lista aparte de defectos y usar la clasificacion para enfocar la inspeccion.
- **634** | environmental/marcos_pensamiento_dfe contra encuadre_desafio_diseno  
  Elegir un marco conceptual de diseno sostenible contra encuadrar el desafio de diseno: marcos distintos, sano. FIGURA NUEVA, amplia la de franja 474: la familia del encuadre del problema en el NUCLEO llega a CUATRO nodos. how_might_we_briefs (296), how_might_we_hmw (400), how_might_we_framing (474) y encuadre_desafio_diseno (634). Los cuatro mandan formular el problema como pregunta abierta de diseno, cuidar que no quede ni demasiado amplia ni demasiado estrecha, y revisarla con lo aprendido.
- **635** | environmental/responsabilidad_extendida_productor_2 contra diseno_para_sostenibilidad_cradle_to_cradle  
  La responsabilidad extendida del productor contra el mapeo cradle to cradle: angulos vecinos, sano. FIGURAS, dos, las dos NUEVAS. Sufijo _N vivo en environmental, responsabilidad_extendida_productor_2, vigesimo segundo miembro. Y marco-pais que NO es Estados Unidos por primera vez en el cribado: el nodo cablea el cumplimiento de WEEE y RoHS, regulaciones europeas, sin condicion de region.
- **639** | environmental/respeto_a_la_diversidad contra shapeshifting_diversidad  
  Respetar la diversidad del contexto local contra cultivar la diversidad de pensamiento en tu equipo: objetos distintos, sano. FIGURA NUEVA, amplia la de franja 485: la familia de la diversidad en environmental es un TRIO, y dos de sus ids se distinguen por una sola letra. respetar_la_diversidad (364), diversidad_en_diseno (485) y respeto_a_la_diversidad (639). Es la sexta vez que aparece el patron de ids casi identicos, y la primera fuera de quality.
- **651** | exportacion/seleccion_representante_extranjero contra criterios_seleccion_proveedores  
  El checklist de nueve puntos para elegir representante en el extranjero contra la matriz ponderada de seleccion: objetos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, ya registrada.
- **654** | seguridad_digital/getting_started_security_assessment_monitoring contra risk_audit  
  Auditar los controles y montar el monitoreo continuo contra auditar la gestion de riesgos: objetos distintos, sano. FIGURA: marco-pais en seguridad_digital, segunda instancia. El nodo vuelve a mandar el POAM, Plan of Action and Milestones del marco federal de Estados Unidos, igual que evaluar_controles en franja 546. Los dos nodos comparten ademas ese paso, asi que hay solape entre ellos.
- **658** | quality/establecimiento_capacidad_proceso contra mejora_continua_relentless  
  Probar la mejora y confirmar la capacidad del proceso contra iterar cambios pequenos: momentos distintos, sano. FIGURA NUEVA, septima del tipo de ids casi identicos: establecimiento_capacidad_proceso (franja 273 y 658) y establecer_capacidad_del_proceso (franja 624), los dos del mundo quality, los dos sobre medir la capacidad del proceso mejorado contra la meta y corregir antes de operarlo.
- **663** | quality/planificacion_gobierno_organizaciones_familiares contra revisiones_regulares_desempeno_ceo  
  Gobierno y sucesion en un negocio familiar contra las revisiones escritas del desempeno del fundador: objetos distintos, sano. FIGURA NUEVA: costura visible en el nucleo, revisiones_regulares_desempeno_ceo tiene diez pasos en dos bloques apilados. Los pasos 1 a 4 montan la revision formal del desempeno del fundador; los pasos 5 a 10 son otra narracion entera, articular la historia de la empresa, auditar la velocidad de las decisiones, evaluar al equipo ejecutivo, preguntarle a la gente que tan facil le resulta trabajar y calibrar objetivos contra la oportunidad real.
- **665** | quality/trazabilidad_de_lotes contra estandar_gtin_epc  
  Numerar y rastrear lotes para poder hacer un recall contra el estandar internacional de identificacion: objetos vecinos, sano. FIGURA: herramientas con nombre propio, esta vez en el nodo del NUCLEO. estandar_gtin_epc manda registrarse en GS1 e integrarse con la red EPCglobal. Son estandares vivos y de uso amplio, se anotan sin asumir nada.
- **671** | quality/brainstorming contra pensamiento_no_guiado_vs_regulado  
  Las reglas y la mecanica de una sesion de lluvia de ideas contra alternar pensamiento no guiado y regulado: niveles distintos, sano. FIGURA NUEVA que cruza la frontera: el NUCLEO ya tenia un trio sobre las reglas del brainstorming (reglas_brainstorming, brainstorming_divergente, brainstorming_efectivo, censado en franja 494) y el mundo quality tiene ademas el suyo, brainstorming, con las mismas reglas de no criticar, buscar cantidad, registrar visible y procesar despues. Son cuatro nodos de la misma doctrina repartidos entre gratis y de pago.
- **672** | quality/desarrollar_caracteristicas_proceso_2 contra analisis_flujo_de_valor  
  Disenar el proceso que crea y entrega tu producto contra mapear el flujo de valor real: momentos distintos, sano. FIGURA: sufijo _N vivo, desarrollar_caracteristicas_proceso_2, ya registrado en franja 201.
- **674** | quality/tipos_innovacion_i_ii contra estrategia_de_innovacion_y_tecnologia  
  Los dos tipos de innovacion contra elegir las arenas estrategicas donde buscar ideas: niveles distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **679** | quality/desarrollo_caracteristicas_producto contra voz_del_cliente_voc  
  Quality by Design contra observar al cliente en su entorno: momentos distintos, sano. FIGURA: costura ya confirmada en voz_del_cliente_voc.
- **683** | quality/clasificacion_de_seriedad_de_defectos contra metricas_calidad  
  Los demeritos por unidad para comparar tendencias contra definir y documentar una metrica: objetos distintos, sano. FIGURA, amplia la de franja 629: la familia de clasificacion de defectos en quality llega a CUATRO miembros y con un detalle propio, existen a la vez el nodo base y el de sufijo. clasificacion_seriedad_defectos (493), clasificacion_de_seriedad_de_defectos (683), clasificacion_de_seriedad_de_defectos_2 (542) y clasificacion_caracteristicas_calidad (629).
- **684** | quality/medicion_calidad contra medicion_monitoreo_desempeno  
  Medir la calidad por area contra medir y monitorear el desempeno de tu propuesta de valor: objetos distintos, sano. FIGURA: numero de paso en el titulo, medicion_calidad se llama Paso 3, ya registrada en franja 562.
- **685** | quality/plan_de_control contra variance_analysis  
  El plan de control contra comparar lo planeado con lo real: objetos distintos, sano. FIGURA: par calcado plan_de_control con matriz_de_control_de_proceso, ya registrado.
- **688** | quality/doble_significado_calidad contra superioridad_producto_beneficios  
  El doble significado de la calidad contra la superioridad por beneficios: angulos vecinos, sano. FIGURA NUEVA: costura visible en el nucleo, superioridad_producto_beneficios tiene diez pasos en dos bloques apilados. Los pasos 1 a 6 separan caracteristica de beneficio y definen el producto desde la voz del cliente; los pasos 7 a 10 son otra narracion entera sobre elegir posicionamiento de precio bajo o premium y como armar el discurso de venta en cada caso, incluido que hacer con vendedores que vienen de otro posicionamiento.
- **692** | exportacion/screening_mercados_potenciales contra product_market_fit  
  Screening de mercados de exportacion contra verificar el ajuste producto mercado: objetos distintos, sano. FIGURA: pais cableado, el U.S. Census Bureau y el U.S. Commercial Service, ya registrada.
- **693** | quality/dmaic_fase_select contra plan_mejora_procesos  
  La fase Select de DMAIC con COPQ y team charter contra el plan de mejora de procesos: momentos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **694** | quality/equipo_mejora_calidad contra plan_gestion_calidad  
  Convocar representantes de cada area como agentes de cambio contra el plan de gestion de calidad: objetos distintos, sano. FIGURAS, dos, las dos NUEVAS. Numero de paso en el titulo, equipo_mejora_calidad se llama Paso Dos, y es el primero de esa figura escrito con letra y no con cifra. Y par calcado con equipo_mejora_calidad_2 (franja 168): los dos arman el mismo grupo, un representante por area clave, alguien que documente y de seguimiento, un lider y un alcance definido de lo que el grupo puede decidir.
- **695** | quality/establecer_estandares_desempeno contra diseno_metricas_lideres_rezagados  
  Fijar estandares de desempeno validados por benchmarking contra combinar senales tempranas y resultados finales: angulos distintos, sano. FIGURA: trio de metas de calidad en quality, ya censado en franja 601.
- **707** | quality/tipos_innovacion_i_ii contra resolver_problemas_grandes  
  Los dos tipos de innovacion contra buscar puntos de dolor grandes y disenar un sistema: metodos distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **714** | exportacion/screening_mercados_potenciales contra etapa_build_business_case  
  Screening de mercados de exportacion contra construir el caso de negocio: momentos distintos, sano. FIGURA: pais cableado, ya registrada.
- **716** | quality/desarrollar_caracteristicas_proceso_2 contra plan_de_lanzamiento_al_mercado  
  Disenar el proceso que crea y entrega tu producto contra el plan de lanzamiento al mercado: momentos distintos, sano. FIGURA: sufijo _N vivo, desarrollar_caracteristicas_proceso_2, ya registrado.
- **719** | quality/sistema_pull_push contra gestion_inventario  
  Pasar de push a pull con kanbans contra la gestion de inventario completa: angulos distintos, sano. FIGURA: costura ya confirmada en gestion_inventario.
- **721** | quality/fin_precio_como_criterio_unico contra traspaso_ventas_cuentas  
  Dejar de elegir proveedor solo por precio contra que lo que prometes al vender sea lo que entregas: temas distintos, sano. FIGURA: par calcado DENTRO DEL NUCLEO, traspaso_ventas_cuentas con desconexion_ventas_experiencia, ya registrado en franja 280.
- **722** | quality/proyectos_vitales_pocos contra portfolio_management  
  Clasificar proyectos en vitales pocos y utiles muchos contra gestionar el portafolio con Go Kill: angulos distintos, sano. FIGURA: par calcado proyectos_vitales_pocos con pocos_vitales_muchos_utiles, ya registrado.
- **723** | quality/reduccion_de_tiempo_de_ciclo contra reduccion_tiempo_de_mercado_velocidad  
  Reducir el tiempo de ciclo del proceso contra reducir el tiempo al mercado del producto: objetos distintos, sano. FIGURA NUEVA, octava del tipo de ids casi identicos: reduccion_tiempo_ciclo (franja 423, siete pasos concretos) y reduccion_de_tiempo_de_ciclo (franja 723, tres pasos genericos), los dos del mundo quality y los dos sobre lo mismo. Aqui ademas el segundo es mucho mas flaco que el primero.
- **729** | franquicias/posicionamiento_est contra desarrollar_posicionamiento_empresa  
  Elegir en que vas a ser el mejor y renunciar al resto contra redactar el posicionamiento de la empresa: objetos distintos, sano. FIGURA NUEVA: quinto par calcado DENTRO DEL NUCLEO. posicionamiento_de_empresa (franja 529) y desarrollar_posicionamiento_empresa (franja 729) mandan lo mismo, redactar una declaracion de posicionamiento simple y centrada en el cliente, compararla con la de los competidores y evitar superlativos que no puedes demostrar.
- **746** | quality/matriz_de_planificacion_arbol contra plan_mejora_procesos  
  El diagrama de arbol con columnas de quien y cuando contra el plan de mejora de procesos: objetos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **754** | quality/innovacion_tipo_ii contra estrategia_de_innovacion_y_tecnologia  
  Hacerlo mas grande, mas pequeno o combinarlo contra elegir las arenas estrategicas: niveles distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **759** | quality/evaluacion_desempeno_junta_directiva contra preguntas_excelencia_operacional  
  Evaluar el desempeno de la junta directiva contra las preguntas de excelencia operacional: objetos distintos, sano. FIGURA NUEVA: sexto par calcado DENTRO DEL NUCLEO. framework_excelencia_operacional (franja 158, 454 y 653) y preguntas_excelencia_operacional (franja 759) son el mismo cuestionario, como recluta, entrena y evalua a sus reportes, como decide, como diseno sus procesos centrales y como obtiene conocimiento de la organizacion.
- **761** | quality/sistema_estable_causas_comunes contra curse_cinco_culpas  
  Verificar con cartas de control si el sistema es estable antes de fijar metas contra facilitar los cinco porques: marcos distintos, sano. FIGURA, amplia la de franja 613: el racimo de quality sobre que la variacion del sistema es tuya llega a SIETE nodos con sistema_estable_causas_comunes.
- **775** | quality/planificacion_economica_conjunta contra criterios_seleccion_proveedores  
  Ingenieria de valor y costo total de propiedad con el proveedor contra la matriz ponderada de seleccion: momentos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, ya registrada.
- **784** | quality/principios_mejora_continua contra plan_mejora_procesos  
  Los principios Shingo de mejora continua contra el plan de mejora de procesos: marcos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **790** | quality/politica_no_culpar_trabajador contra regla_simplificada_tolerancia_errores  
  Analizar la distribucion de errores entre personas antes de sancionar contra la regla de dos lineas: metodos distintos, sano. FIGURA, amplia la de franja 613 y 761: el racimo de quality sobre que la variacion del sistema es tuya llega a OCHO nodos con politica_no_culpar_trabajador.
- **792** | compras/verifica_que_el_si_es_real contra traspaso_ventas_cuentas  
  Verificar que el si del proveedor es real contra que lo que prometes al vender sea lo que entregas: lados opuestos de la mesa, sano. FIGURA: par calcado DENTRO DEL NUCLEO, traspaso_ventas_cuentas con desconexion_ventas_experiencia, ya registrado.
- **794** | exportacion/optimizacion_motores_busqueda contra seo_estrategia_fat_head  
  SEO internacional por mercado destino contra la estrategia fat head: metodos distintos, sano. FIGURAS, dos. Herramientas con nombre propio en el nodo del NUCLEO: seo_estrategia_fat_head manda usar Google Keyword Planner, Google Trends y comprar anuncios SEM para validar. Y una observacion para el auditor: el nucleo tiene DOS nodos de SEO, seo_long_tail (franja 404) y seo_estrategia_fat_head (franja 794). No los cuento como calcado porque son estrategias opuestas a proposito, cola larga contra cabeza gorda, pero conviene que la ficha sepa que estan los dos.
- **795** | quality/tipos_innovacion_i_ii contra estrategia_de_innovacion_producto  
  Los dos tipos de innovacion contra la estrategia de innovacion audaz: niveles distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **800** | quality/establecer_metas_de_calidad_basadas_en_mercado contra metas_objetivos_smart_innovacion  
  Fijar metas de calidad por benchmarking contra las metas SMART de innovacion: angulos distintos, sano. FIGURA: trio de metas de calidad en quality, ya censado en franja 601.
- **801** | quality/mejora_continua_del_proceso contra plan_mejora_procesos  
  La mejora sin fin de Deming contra el plan de mejora de procesos: marcos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **803** | quality/mistake_proofing_poka_yoke_2 contra sistema_inmune_producto  
  Poka yoke en el punto donde el humano se equivoca contra el sistema inmune del producto: objetos distintos, sano. FIGURAS, dos, las dos NUEVAS. Sufijo _N vivo en quality, mistake_proofing_poka_yoke_2, vigesimo tercer miembro, y con el hace TRIO calcado junto a poka_yoke_a_prueba_de_errores (franja 198) y error_proofing_servicio (franja 314). Y costura visible en el nucleo: sistema_inmune_producto tiene nueve pasos en dos bloques, los pasos 1 a 5 son el andon cord automatizado con reversion y bloqueo de despliegues, y los pasos 6 a 9 son otra narracion sobre friccion de soporte, autoservicio y autosanacion.
- **807** | health_safety/abandonar_arreglos_rapidos contra tecnica_cinco_porques  
  Resistir el arreglo rapido tras el incidente contra la tecnica de los cinco porques: momentos distintos, sano. FIGURA NUEVA: septimo par calcado DENTRO DEL NUCLEO, y es de los mas claros. tecnica_cinco_porques (franja 807) y five_whys_inversion_proporcional (visto en decenas de pares) son el mismo metodo, preguntar por que cinco veces, no culpar a la persona y graduar la inversion de prevencion al dano. El segundo ademas arrastra su propia costura ya registrada.
- **808** | health_safety/ciclo_de_culpa_2 contra regla_simplificada_tolerancia_errores  
  Reconocer que la accion humana esta limitada por el contexto contra la regla de dos lineas: niveles distintos, sano. FIGURAS, dos, las dos NUEVAS. Sufijo _N vivo en health_safety, ciclo_de_culpa_2, vigesimo cuarto miembro. Y par calcado con ciclo_de_culpa (franja 556): los dos mandan reconocer el patron de culpar y entrenar, evitar la sancion como unica respuesta y redirigir el analisis a los factores organizacionales.
- **809** | health_safety/human_error_como_sintoma contra curse_cinco_culpas  
  El error humano como sintoma y no como causa contra facilitar los cinco porques: marcos vecinos, sano. FIGURA: human_error_como_sintoma es el miembro DIECISEIS de la familia de health_safety censada en franja 460.
- **810** | quality/dmaic_fase_define contra customer_discovery_cuatro_fases  
  La fase Define de DMAIC contra las cuatro fases del descubrimiento del cliente: marcos distintos, sano. FIGURA NUEVA: octavo par calcado DENTRO DEL NUCLEO. customer_development_process (franja 113) y customer_discovery_cuatro_fases (franja 810) narran las mismas cuatro fases, desarmar la idea en hipotesis, probar el problema con clientes, mostrar el minimo viable y evaluar si se valida.
- **813** | quality/establecer_proyecto_y_metas_diseno contra principio_calidad_mvp  
  Establecer el proyecto y sus metas de diseno contra la calidad del MVP: doctrinas distintas de cuanto pulir, sano. FIGURA NUEVA y la mas grande de este tipo: costura visible en el nucleo, principio_calidad_mvp tiene CATORCE pasos en TRES bloques apilados que cuentan la misma doctrina tres veces. Los pasos 1 a 5 distinguen defecto inaceptable de baja calidad tolerable; los pasos 6 a 10 vuelven con resistir la presion del equipo tecnico, lanzar aceptando que fallara e iterar con feedback; los pasos 11 a 14 lo cuentan otra vez como identificar lo critico, excluir lo secundario, lanzar y mejorar con el uso real.
- **816** | compras/traduce_stock_muerto_numeros contra profit_vs_cash  
  Traducir el stock muerto a numeros duros contra la diferencia entre ganar y tener el dinero: objetos distintos, sano. FIGURA NUEVA: noveno par calcado DENTRO DEL NUCLEO. diferencia_ganancia_flujo_caja (franja 320 y 734) y profit_vs_cash (franja 816) mandan lo mismo, mirar el flujo de caja aparte del estado de resultados, proyectarlo a varios meses y anticipar el momento en que crecer en ventas te deja sin efectivo.
- **817** | franquicias/proceso_llamada_inicial_venta contra preparacion_preguntas_problema_precall  
  El mundo especializa la primera llamada a la venta de franquicias contra preparar las preguntas de problema: sano. FIGURA: par calcado de franquicias, proceso_llamada_inicial_venta con proceso_primera_llamada, ya registrado.
- **820** | quality/distincion_causas_especiales_comunes contra regla_simplificada_tolerancia_errores  
  Verificar el control estadistico antes de ajustar el proceso contra la regla de dos lineas: niveles distintos, sano. FIGURA: trio calcado de causas comunes y especiales, ya registrado en franja 265.
- **822** | quality/institucionalizar_capacitacion contra rediseno_procesos_negocio_cx  
  Instituir la capacitacion segun Deming contra redisenar los procesos que le dan friccion al cliente. Objetos distintos, sano. FIGURA NUEVA, destapada por la muestra D (tanda 2): numero de paso en el titulo, y no es el programa de Crosby sino LOS CATORCE PUNTOS DE DEMING. El nodo se titula Instituir la Capacitacion (Punto 6). Censo verificado contra el grafo: SIETE nodos de quality llevan el numero de punto en el titulo, los puntos 5, 6, 7, 8, 10, 13 y 14 (mejora_continua_del_sistema, institucionalizar_capacitacion, adopcion_liderazgo, eliminar_miedo, eliminar_slogans_metas, fomento_educacion_autoeducacion y plan_de_accion_transformacion). CORRECCION MIA: la figura si estaba en la lista del encargo y la aplique a los Paso N de Crosby, pero nunca a los Punto N de Deming; su primera aparicion en la cola fue la franja 159 y la clasifique D. Las demas apariciones quedan D bajo la limitacion declarada de re-vista de racimo ya contado.
- **824** | franquicias/calculo_roi_franquiciado_2 contra validacion_hipotesis_ingresos  
  Calcular el retorno que gana quien compra tu franquicia contra comprobar si tus ingresos aguantan el negocio: objetos distintos, sano. FIGURA: sufijo _N vivo en franquicias, calculo_roi_franquiciado_2. Vigesimo quinto miembro.
- **829** | quality/revision_progreso contra revision_portafolio_periodica  
  El proceso formal de revision de progreso contra la revision periodica del portafolio completo: niveles distintos, sano. FIGURAS, dos. Par calcado revision_progreso con revision_progreso_breakthrough, ya registrado en franja 420. Y una NUEVA y grande: el NUCLEO tiene un RACIMO de al menos seis nodos sobre gestionar y revisar el portafolio, con la misma doctrina de revisar todo junto cada trimestre, podar lo debil y reasignar recursos. Son gestion_portafolio_foco (125), portfolio_management (153), pruning_portafolio (465), gestion_portafolio_formal (733), gestion_portafolio_dos_niveles (780) y revision_portafolio_periodica (829).
- **836** | franquicias/multiples_compradores_influyentes contra tipos_de_clientes  
  Mapear a todos los que influyen en la decision de compra contra los tipos de cliente en el proceso de decision: temas iguales, el mundo mas breve pero con su angulo regulatorio. Sano. FIGURA: pais cableado, el nodo del mundo manda revisar el cumplimiento regulatorio en los estados con requisitos de registro de franquicias, sin condicion de pais.
- **837** | quality/brainstorming contra mash_ups  
  Las reglas y la mecanica de la sesion de ideas contra la tecnica de mash-ups: niveles distintos, sano. FIGURA: el nodo brainstorming del mundo quality junto al trio del nucleo, ya registrado en franja 671.
- **842** | compras/pide_una_revision_externa_antes_de_firmar_cualquier_contrato contra term_sheet_disposiciones_vinculantes  
  Revision externa del borrador antes de firmar contra distinguir que partes del term sheet son vinculantes: momentos distintos, sano. FIGURA NUEVA: pais cableado en un nodo del NUCLEO. term_sheet_disposiciones_vinculantes manda definir como se dividen los costos de filing del HSR Act, una ley antimonopolio estadounidense, sin condicion de pais. Hasta ahora el marco-pais habia aparecido casi siempre en nodos de mundo.
- **845** | quality/ciclo_pdca_pdsa contra plan_mejora_procesos  
  El ciclo PDCA contra el plan de mejora de procesos: niveles distintos, sano. FIGURAS, dos. Costura ya confirmada en plan_mejora_procesos. Y NUEVA: par calcado dentro del mundo quality, pdsa_shewhart_cycle (franja 783) con ciclo_pdca_pdsa (franja 845). Los dos narran el mismo ciclo de planificar, ejecutar, estudiar y actuar, y repetirlo.
- **848** | quality/accion_correctiva contra five_whys_inversion_proporcional  
  Distinguir la no conformidad esporadica de la cronica y darle a cada una su tratamiento contra los cinco porques: metodos distintos, sano. FIGURA, amplia las de franja 501, 536, 569 y 587: la familia de accion correctiva del mundo quality llega a SIETE miembros, y ahora aparece tambien el id base sin sufijo. accion_correctiva, accion_correctiva_2, accion_correctiva_4, accion_correctiva_5, accion_correctiva_6, accion_correctiva_crosby y accion_correctiva_sistematica.
- **851** | quality/medicion_calidad contra plan_mejora_procesos  
  Medir la calidad por area con linea base contra el plan de mejora de procesos: objetos distintos, sano. FIGURAS: costura ya confirmada en plan_mejora_procesos y numero de paso en el titulo, medicion_calidad se llama Paso 3.
- **852** | franquicias/manejo_objeciones_venta_franquicia contra traspaso_ventas_cuentas  
  Preparar respuestas a las objeciones tipicas contra que lo que prometes al vender sea lo que entregas: momentos distintos, sano. FIGURA: par calcado DENTRO DEL NUCLEO, traspaso_ventas_cuentas con desconexion_ventas_experiencia, ya registrado.
- **857** | health_safety/errores_como_consecuencia contra five_whys_inversion_proporcional  
  El error humano como consecuencia y no como causa contra los cinco porques: marcos vecinos, sano. FIGURA: errores_como_consecuencia es el miembro DIECISIETE de la familia de health_safety censada en franja 460. Junto con human_error_como_sintoma (franja 809) forman ademas un par casi identico entre si.
- **860** | franquicias/manejo_objeciones_venta_franquicia contra desconexion_ventas_experiencia  
  Preparar respuestas a las objeciones tipicas contra la desconexion entre vender y cumplir: momentos distintos, sano. FIGURA: par calcado DENTRO DEL NUCLEO, ya registrado.
- **867** | quality/lean_six_sigma_roadmap contra plan_mejora_procesos  
  El roadmap Lean Six Sigma contra el plan de mejora de procesos: marcos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **869** | quality/revision_diseno contra customer_development_modelo  
  La revision formal de diseno contra salir a hablar con clientes antes de construir: objetos distintos, sano. FIGURA NUEVA y grande: el NUCLEO tiene un RACIMO de al menos seis nodos sobre salir a hablar con el cliente antes de construir, con la misma doctrina. Son customer_discovery (179), customer_development_process (113), customer_discovery_phase2_problem_test (456), customer_development_vs_business_plan (570), customer_discovery_cuatro_fases (810) y customer_development_modelo (869). Dos de ellos, customer_development_process y customer_discovery_cuatro_fases, ya quedaron registrados como par calcado en franja 810; este censo los pone en contexto.
- **871** | compras/ata_el_pago_al_cumplimiento_real_del_servicio contra traspaso_ventas_cuentas  
  Atar el pago al cumplimiento real del servicio contra que lo que prometes al vender sea lo que entregas: lados opuestos de la mesa, sano. FIGURA: par calcado DENTRO DEL NUCLEO, ya registrado.
- **878** | quality/reduccion_de_tiempo_de_ciclo contra analisis_flujo_de_valor  
  Reducir el tiempo de ciclo contra mapear el flujo de valor real: niveles distintos, sano. FIGURA: par calcado reduccion_tiempo_ciclo con reduccion_de_tiempo_de_ciclo, ya registrado en franja 723.
- **883** | quality/poka_yoke_a_prueba_de_errores contra tecnica_cinco_porques  
  Poka yoke en el punto donde el humano se equivoca contra los cinco porques: momentos distintos, sano. FIGURAS: trio calcado de poka yoke en quality, ya registrado en franja 803, y par calcado del nucleo tecnica_cinco_porques con five_whys_inversion_proporcional, ya registrado en franja 807.
- **885** | quality/sostener_las_ganancias contra mejora_continua_relentless  
  Sostener la mejora con controles, entrenamiento y auditorias contra iterar cambios pequenos: momentos distintos, sano. FIGURA NUEVA, novena del tipo de ids casi identicos: mantener_las_ganancias (franja 378) y sostener_las_ganancias (franja 885), los dos del mundo quality, los dos titulados Hold the Gains en el parentesis y los dos con la misma receta, plan de control documentado, entrenamiento formal del personal nuevo y auditoria periodica de que el control sigue vivo.
- **887** | quality/fijacion_de_metas contra diseno_metricas_lideres_rezagados  
  Fijar metas de mejora por grupo con reconocimiento publico contra combinar senales tempranas y resultados finales: angulos distintos, sano. FIGURA: numero de paso en el titulo, fijacion_de_metas se llama Paso 10. Es ademas el segundo nodo del mundo quality que se llama Paso 10, junto a establecimiento_metas (franja 305), y los dos son de fijar metas.
- **893** | environmental/triple_bottom_line_2 contra modelos_negocio_mas_alla_del_lucro  
  El triple balance con foco en lo social contra los modelos de negocio mas alla del lucro: objetos distintos, sano. FIGURAS, dos, las dos NUEVAS. Sufijo _N vivo en environmental, triple_bottom_line_2, vigesimo sexto miembro. Y par calcado con triple_bottom_line (franja 798): los dos mandan definir indicadores para las tres dimensiones y meterlos juntos en el analisis, el segundo cargando mas hacia lo social.
- **902** | quality/intercambio_de_roles_para_motivacion contra tecnica_freaky_friday  
  Intercambiar puestos entre areas vecinas para mejorar comprension contra intercambiar los roles de dos lideres en conflicto: fines distintos, sano. FIGURA NUEVA: par calcado dentro del mundo quality, rotacion_de_puestos_para_mejora_calidad (franja 686) con intercambio_de_roles_para_motivacion (franja 902). Los dos montan el mismo intercambio temporal con un area vecina, lo negocian con el otro supervisor, observan el efecto en los indicadores y lo repiten si funciona.
- **907** | health_safety/new_view_human_error contra curse_cinco_culpas  
  La New View del error humano contra facilitar los cinco porques: marcos vecinos, sano. FIGURA: new_view_human_error es el miembro DIECIOCHO de la familia de health_safety censada en franja 460, y ademas es casi identico a new_view_investigation (franja 311), con el que forma par dentro de la familia.
- **909** | quality/despliegue_metas contra metas_objetivos_smart_innovacion  
  Desplegar las metas del consejo por nivel organizacional contra las metas SMART de innovacion: objetos distintos, sano. FIGURA NUEVA, decima del tipo de ids casi identicos: desplegar_metas_organizacion (franja 877) y despliegue_metas (franja 909), los dos del mundo quality, los dos sobre subdividir la meta estrategica en submetas por nivel y negociar los recursos.
- **910** | risk_management/amenaza_y_oportunidad contra matriz_probabilidad_impacto  
  Escribir la cara de amenaza y la de oportunidad de cada incertidumbre contra priorizar riesgos por probabilidad e impacto: angulos distintos, sano. FIGURA NUEVA: par calcado dentro del mundo risk_management, el primero de ese mundo en todo el cribado. caza_las_oportunidades_no_solo_amenazas (franja 188) y amenaza_y_oportunidad (franja 910) mandan lo mismo, abrir la lista de oportunidades junto a la de amenazas y elegir cual perseguir.
- **913** | quality/fitness_for_purpose_vs_conformance contra metricas_calidad  
  La aptitud de uso contra la conformidad con la especificacion, contra definir y documentar una metrica: objetos distintos, sano. FIGURA NUEVA, undecima del tipo de ids casi identicos: fitness_for_use_purpose (franja 838) y fitness_for_purpose_vs_conformance (franja 913), los dos del mundo quality y los dos sobre que la calidad se mide por el uso real y no solo por la especificacion.
- **925** | quality/criterios_baldrige_excelencia contra framework_excelencia_operacional  
  Los criterios Baldrige contra las preguntas de excelencia operacional: marcos distintos, sano. FIGURA: marco con nombre propio y de pais, el nodo del mundo estructura la autoevaluacion sobre el Malcolm Baldrige National Quality Award, un premio nacional estadounidense, sin condicion de pais. Es la misma especie que el marco-pais ya registrado.
- **937** | quality/concepto_programa_catorce_pasos contra calidad_de_ejecucion_proceso_innovacion  
  El programa de catorce pasos de Crosby contra la calidad de ejecucion del proceso de innovacion: objetos distintos, sano. FIGURA NUEVA y ES LA EXPLICACION DE OTRA: la figura del numero de paso en el titulo no es cosmetica. El mundo quality tiene un nodo que describe el programa de catorce pasos completo, concepto_programa_catorce_pasos, y ademas tiene los pasos sueltos convertidos en nodos independientes con el numero en el titulo. Hasta ahora aparecieron el Paso Dos (equipo_mejora_calidad), el Paso 3 (medicion_calidad), el Paso 4 (costo_de_calidad_3), el Paso 6 (accion_correctiva_4 y accion_correctiva_sistematica), el Paso 10 (establecimiento_metas y fijacion_de_metas) y el Paso 11 (eliminacion_causas_error y eliminacion_causas_error_2). Eso explica de un golpe por que hay tantos nodos casi iguales en quality: son el mismo programa desmontado en piezas, y varias piezas quedaron duplicadas.
- **943** | environmental/liderazgo_ceo_sostenibilidad contra seleccion_ceo_fundador  
  Que el CEO articule publicamente la vision de sostenibilidad contra decidir con intencion quien sera el CEO fundador: objetos distintos, sano. FIGURA NUEVA: costura visible en el nucleo, seleccion_ceo_fundador tiene DOCE pasos en tres bloques apilados. Los pasos 1 a 4 eligen al CEO fundador entre el equipo y documentan el acuerdo; los pasos 5 a 8 cambian de tema a evaluar tus propias brechas y buscar un CEO profesional; los pasos 9 a 12 cambian otra vez, al equipo directivo, las clausulas de la inversion y la transicion gradual.
- **945** | quality/proceso_nominacion_seleccion contra gestion_de_portafolio_gates_go_kill  
  Nominar y filtrar proyectos candidatos contra el embudo con gates y decisiones Go Kill: momentos distintos, sano. FIGURA, amplia la de franja 829: el racimo de portafolio en el NUCLEO llega a SIETE nodos con gestion_de_portafolio_gates_go_kill.
- **952** | exportacion/investigacion_mercado_primaria_secundaria_2 contra captura_conocimiento_mercado  
  Empezar por investigacion secundaria y completar con primaria contra construir conocimiento de mercado con ferias y analistas: metodos vecinos, sano. FIGURAS, dos. Sufijo _N vivo en exportacion, investigacion_mercado_primaria_secundaria_2, vigesimo septimo miembro. Y pais cableado, el nodo manda consultar los reportes del U.S. Commercial Service, ya registrada como figura.
- **959** | risk_management/mide_lo_que_de_verdad_mueve_la_aguja contra leap_of_faith_assumptions  
  Marcar los supuestos que mas mueven la aguja contra separar los hechos de los saltos de fe: angulos vecinos, sano. FIGURA NUEVA: decimo par calcado DENTRO DEL NUCLEO. extraer_priorizar_hipotesis (franja 484 y 951) y leap_of_faith_assumptions (franja 959) mandan lo mismo, listar todo lo que tiene que ser cierto, separar lo comprobado de lo supuesto y ordenar los supuestos por el riesgo que representan.
- **964** | quality/pocos_vitales_muchos_utiles contra pruning_portafolio  
  Clasificar proyectos en vitales pocos y utiles muchos contra podar el treinta por ciento mas debil: metodos vecinos, sano. FIGURAS: par calcado proyectos_vitales_pocos con pocos_vitales_muchos_utiles, ya registrado, y pruning_portafolio pertenece al racimo de portafolio del nucleo censado en franja 829.
- **966** | environmental/modelo_cradle_to_grave contra economia_circular_como_modelo_de_negocio  
  De la cuna a la tumba contra la economia circular como modelo: el mundo describe el problema y el nucleo la salida. Sano. FIGURA: costura en economia_circular_como_modelo_de_negocio, ya registrada en franja 124.
- **967** | quality/concepto_de_auditoria_de_calidad contra metricas_calidad  
  Los tipos de auditoria de calidad contra definir y documentar una metrica: objetos distintos, sano. FIGURA, amplia la de franja 608: la familia de auditoria de calidad del mundo quality llega a CUATRO nodos. auditoria_calidad (107), principios_auditoria_calidad (146), programa_auditoria_calidad (608) y concepto_de_auditoria_de_calidad (967). Los cuatro definen contra que se audita, quien audita con independencia y si el foco es cumplimiento o efectividad.
- **973** | quality/costo_de_calidad contra efecto_bullwhip  
  El costo de la calidad como marco de analisis financiero contra medir y costear el efecto latigo: objetos distintos, sano. FIGURA, amplia la de franja 481: la familia del costo de calidad en quality es un TRIO. costo_de_calidad (973), costo_de_calidad_3 (481) y costo_de_calidad_diagnostico (381). Los tres mandan sumar los componentes del costo de calidad, compararlo contra tus numeros y usarlo como argumento para decidir donde invertir.
- **977** | quality/proceso_nominacion_seleccion contra plan_mejora_procesos  
  Nominar y filtrar proyectos candidatos contra el plan de mejora de procesos: objetos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **983** | franquicias/concepto_de_advances contra obtencion_compromiso  
  El avance como venta pequena progresiva contra lograr un compromiso mas alla del cierre: sano por contenido, y con figura. FIGURA NUEVA: undecimo calcado DENTRO DEL NUCLEO, y es un TRIO con ids casi identicos. obtencion_de_compromiso (franja 127 y 960), obtencion_compromiso_venta (franja 219 y 655) y obtencion_compromiso (franja 983). Los tres mandan lo mismo, definir un objetivo de avance realista, resumir lo que el cliente reconocio, proponer el siguiente paso concreto y evitar las tecnicas de presion. Esto es ademas contexto para la B de franja 610, donde el nodo del mundo quedaba a la altura de este material.
- **986** | exportacion/tipos_sitio_web_exportacion contra channels_hypothesis_web_mobile  
  Elegir el tipo de sitio web para exportar contra elegir el canal digital: angulos distintos, sano. FIGURA: herramienta con nombre propio, el nodo del mundo manda investigar e-marketplaces citando Amazon entre otros. Es plataforma de uso general, se anota con esa nota.
- **987** | quality/definicion_calidad_fitness_for_purpose contra plan_gestion_calidad  
  Definir la calidad como aptitud para el proposito contra el plan de gestion de calidad: niveles distintos, sano. FIGURA, amplia la de franja 913: la familia de fitness for purpose en quality es un TRIO. fitness_for_use_purpose (838), fitness_for_purpose_vs_conformance (913) y definicion_calidad_fitness_for_purpose (987). Los tres mandan partir de quien es el cliente y sus necesidades explicitas e implicitas, y no confundir la calidad con la conformidad a la especificacion.
- **988** | quality/desarrollar_caracteristicas_proceso_2 contra creacion_estrategia_cadena_suministro  
  Disenar el proceso que crea y entrega tu producto contra la generacion de ideas Plan Source Make Deliver: objetos distintos, sano. FIGURA: sufijo _N vivo, desarrollar_caracteristicas_proceso_2, ya registrado.
- **989** | quality/establecimiento_metas contra diseno_metricas_lideres_rezagados  
  Fijar metas de calidad a 30, 60 y 90 dias contra combinar senales tempranas y resultados finales: objetos distintos, sano. FIGURA: numero de paso en el titulo, establecimiento_metas se llama Paso 10, ya registrada.
- **998** | franquicias/comunicacion_efectiva_con_franquiciados contra confianza_mutua_fundadores  
  Comunicacion directa y transparente con franquiciados contra construir confianza entre cofundadores: objetos distintos, sano. FIGURA NUEVA: duodecimo calcado DENTRO DEL NUCLEO, que anoto aqui aunque el par de este puesto no lo muestre entero. etapa_investigacion_ventas (franja 660) y etapa_de_investigacion (franja 1000) son el mismo nodo dos veces, priorizar la etapa de preguntar sobre la de presentar, resistir la tentacion de saltar a la demostracion y medir cuanto tiempo dedicas a investigar frente a presentar.
- **1000** | franquicias/manejo_objeciones_venta_franquicia contra etapa_de_investigacion  
  Preparar respuestas a las objeciones tipicas contra la etapa de investigacion en la venta: momentos distintos, sano. FIGURA: el calcado de la etapa de investigacion en el nucleo, anotado en franja 998.
- **1005** | quality/gestion_efectiva_benchmarking contra diseno_metricas_lideres_rezagados  
  Gestionar la iniciativa de benchmarking contra combinar senales tempranas y resultados finales: objetos distintos, sano. FIGURA NUEVA: par calcado dentro del mundo quality, rol_alta_direccion_benchmarking (franja 979) con gestion_efectiva_benchmarking (franja 1005). Los dos mandan documentar la politica de benchmarking, integrarla al plan de negocio, quitar obstaculos, dar capacitacion y reconocimiento, y hacer seguimiento SIN usar los hallazgos para sancionar.
- **1011** | quality/proyectos_vitales_pocos contra gestion_de_portafolio_gates_go_kill  
  Clasificar proyectos en vitales pocos y utiles muchos contra el embudo con gates y Go Kill: momentos distintos, sano. FIGURAS: par calcado de vitales pocos, ya registrado, y el racimo de portafolio del nucleo censado en franja 829 y ampliado en 945.
- **1016** | franquicias/cinco_categorias_costos_franquicia contra decision_intensidad_capital  
  Las cinco categorias de costo para convertir tu negocio en franquicia contra cuanto capital externo necesitas: niveles distintos, sano. FIGURA: pais cableado, el nodo del mundo presupuesta el documento de divulgacion y los registros en cada estado, marco regulatorio estadounidense, sin condicion de pais. Ya registrada como figura.
- **1018** | franquicias/medicion_resultados_marketing_franquicia contra metricas_de_adquisicion_activacion  
  Medir los resultados del marketing de franquicias contra las metricas de adquisicion y activacion: objetos vecinos, sano. FIGURAS, dos. Herramientas con nombre propio en el nodo del MUNDO: manda usar TrafficEstimate.com, Alexa y Google Analytics. Se anotan sin asumir que murieron. Y una costura NUEVA en el nodo del NUCLEO: metricas_de_adquisicion_activacion tiene nueve pasos en dos bloques, los pasos 1 a 5 arman el tablero de metricas de adquisicion y activacion, y los pasos 6 a 9 son otra narracion sobre definir la conversion de una campana, calcular clics y comparar costo de adquisicion contra valor del cliente.
- **1019** | quality/alineacion_estrategica_despliegue contra revision_portafolio_periodica  
  Alinear tus metas de calidad con tu estrategia contra la revision periodica del portafolio completo: niveles distintos, sano. FIGURA: racimo de portafolio del nucleo, ya censado en franja 829.
- **1022** | compras/punto_unico_contacto_proveedores contra traspaso_ventas_cuentas  
  Designar un unico punto de contacto con proveedores contra que lo que prometes al vender sea lo que entregas: lados opuestos de la mesa, sano. FIGURA: par calcado DENTRO DEL NUCLEO, traspaso_ventas_cuentas con desconexion_ventas_experiencia, ya registrado.
- **1025** | quality/identificar_clientes_externos_e_internos contra mapa_flujo_trabajo_cliente  
  Identificar clientes externos e internos con el diagrama de flujo contra dibujar el flujo de trabajo del cliente: objetos distintos, sano. FIGURA NUEVA: par calcado dentro del mundo quality, identificar_clientes_diseno (franja 456, 565, 575, 644, 864 y 1025 como vecino) con identificar_clientes_externos_e_internos (franja 1025). Los dos mandan mapear a todos los actores que tocan el producto y separar clientes internos de externos, incluido distinguir a quien ordena de quien usa.
- **1026** | quality/innovacion_tipo_ii contra get_visual  
  Hacerlo mas grande, mas pequeno o combinarlo contra dibujar todo lo que se te ocurra: metodos distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **1029** | environmental/cradle_to_cradle_concepto contra economia_circular_como_modelo_de_negocio  
  Decidir a que ciclo pertenece lo que haces contra la economia circular como modelo: niveles distintos, sano. FIGURA NUEVA: RACIMO de cradle to cradle repartido entre el mundo environmental y el nucleo. En environmental estan eco_efectividad (80 y 124), eco_efectividad_2 (425), nutrientes_biologicos (172), activacion_lista_positiva (312), desperdicio_es_alimento (638), materiales_ciclicos_infinitamente_reciclables (713), critica_eco_eficiencia (843), modelo_cradle_to_grave (966 y 971) y cradle_to_cradle_concepto (1029). En el nucleo esta diseno_para_sostenibilidad_cradle_to_cradle, que aparece como contraparte en casi todos ellos. Son al menos diez piezas de la misma doctrina. Es el racimo mas grande del mundo environmental y explica por que ese mundo aparece tantas veces en la franja.
- **1038** | quality/analisis_causa_raiz_defectos contra five_whys_inversion_proporcional  
  Desagregar las causas genericas de defecto y verificarlas con cada area contra los cinco porques: metodos distintos, sano. FIGURA, amplia la de franja 591: la familia de analisis de causa raiz en quality es un TRIO. analisis_causa_raiz_diagnostico (299), analisis_diagnostico_causa (591) y analisis_causa_raiz_defectos (1038).
- **1040** | quality/establecer_proyecto_mejora contra cinco_porques_master  
  Redactar la declaracion de problema y meta del proyecto contra designar un maestro de los cinco porques: objetos distintos, sano. FIGURA NUEVA: RACIMO de los cinco porques DENTRO DEL NUCLEO, cinco nodos. five_whys_inversion_proporcional (el de la costura ya registrada), tecnica_cinco_porques (807), curse_cinco_culpas, regla_simplificada_tolerancia_errores y cinco_porques_master (1040). Los cinco giran sobre el mismo metodo: preguntar por que varias veces, no culpar a la persona, graduar la prevencion al dano y sostener la disciplina en el tiempo. Es el segundo racimo grande del nucleo despues del de portafolio y el de customer discovery.
- **1048** | quality/evaluacion_gestion_riesgos contra plan_mejora_procesos  
  La lluvia de ideas de riesgos con costo y beneficio contra el plan de mejora de procesos: objetos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **1052** | quality/programa_mejora_calidad_14_pasos contra calidad_de_ejecucion_proceso_innovacion  
  El programa de mejora de calidad de catorce pasos contra la calidad de ejecucion del proceso de innovacion: objetos distintos, sano. FIGURA NUEVA que refuerza la de franja 937: el mundo quality tiene DOS nodos que describen el mismo programa de catorce pasos de Crosby, concepto_programa_catorce_pasos (937) y programa_mejora_calidad_14_pasos (1052). O sea que no solo estan los pasos sueltos duplicados: el indice del programa tambien esta duplicado.
- **1054** | franquicias/cadencia_seguimiento_prospectos contra clasificacion_leads_abc  
  La cadencia de siete contactos en siete dias contra clasificar los prospectos en A, B y C: metodos distintos, sano. FIGURA NUEVA, duodecima del tipo de ids casi identicos: gestion_seguimiento_prospectos (franja 881) y cadencia_seguimiento_prospectos (franja 1054), los dos del mundo franquicias y los dos sobre el ritmo de seguimiento al prospecto, con el mismo cronograma de doce semanas acordado con el candidato.
- **1055** | quality/benchmarking_proceso contra auditoria_desempeno_new_products  
  El proceso de benchmarking de siete pasos contra auditar tus lanzamientos contra el estandar de la industria: objetos distintos, sano. FIGURA NUEVA: RACIMO de benchmarking en el mundo quality, CINCO nodos. monitoreo_continuo_benchmarking (392), benchmarking_7_pasos_juran (459), rol_alta_direccion_benchmarking (979), gestion_efectiva_benchmarking (1005) y benchmarking_proceso (1055). Los cinco definen alcance, eligen con quien compararse, normalizan datos, detectan brechas y arman el plan de mejora.
- **1058** | quality/implementacion_monitoreo_controles contra plan_mejora_procesos  
  Transferir los controles a operaciones y disolver el equipo contra el plan de mejora de procesos: momentos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **1060** | quality/moral_y_sistema_no_individuo contra five_whys_inversion_proporcional  
  Rastrear el origen real de una falla sin buscar culpables contra los cinco porques: metodos distintos, sano. FIGURA, amplia las de franja 613, 761 y 790: el racimo de quality sobre que la variacion del sistema es tuya llega a NUEVE nodos con moral_y_sistema_no_individuo.
- **1063** | quality/eliminacion_causas_error_2 contra five_whys_inversion_proporcional  
  El formulario para reportar causas de error contra los cinco porques: metodos distintos, sano. FIGURAS: sufijo _N vivo y numero de paso en el titulo, las dos ya registradas en franja 623.
- **1067** | environmental/relocalizacion_clustering_logistico contra milk_run_deliveries  
  Relocalizar y agrupar en clusters contra las entregas milk run: objetos distintos, sano. FIGURA NUEVA: par calcado DENTRO DEL NUCLEO. programacion_entregas_delivery_scheduling (franja 650 y 670) y milk_run_deliveries (franja 1067) mandan lo mismo, calcular el EOQ por ubicacion, decidir entre entrega directa y ruta consolidada, elegir la tecnica de ruteo entre matriz de ahorros y asignacion generalizada, y medir el ahorro.
- **1070** | quality/brainstorming contra get_visual  
  Las reglas y la mecanica de la sesion de ideas contra dibujar todo lo que se te ocurra: niveles distintos, sano. FIGURA: el nodo brainstorming del mundo quality junto al trio del nucleo, ya registrado en franja 671.
- **1071** | quality/validacion_sistema_medicion contra tres_as_de_metricas  
  Validar el sistema de medicion antes de confiar en los datos contra las tres cualidades de una metrica util: momentos distintos, sano. FIGURA: herramienta con nombre propio, el nodo del mundo manda usar un software estadistico y cita Minitab. Se anota sin asumir nada.
- **1079** | quality/causas_comunes_vs_especiales contra five_whys_inversion_proporcional  
  Graficar los datos en orden cronologico y aplicar reglas de senal contra los cinco porques: metodos distintos, sano. FIGURA, amplia las de franja 613, 761, 790 y 1060: el racimo de quality sobre causas comunes y responsabilidad del sistema llega a DIEZ nodos con causas_comunes_vs_especiales.
- **1082** | quality/desarrollar_caracteristicas_proceso_2 contra stage5_launch  
  Disenar el proceso que crea y entrega tu producto contra ejecutar el lanzamiento: momentos distintos, sano. FIGURA: sufijo _N vivo, desarrollar_caracteristicas_proceso_2, ya registrado.
- **1084** | quality/mapa_de_proceso_planificacion_control contra plan_mejora_procesos  
  Diagramar el proceso para ubicar los puntos de control contra el plan de mejora de procesos: momentos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **1089** | quality/innovacion_tipo_ii contra portafolio_innovacion_diversificado  
  Hacerlo mas grande, mas pequeno o combinarlo contra repartir el portafolio entre incremental y disruptivo: niveles distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **1097** | quality/juran_rcca_metodo contra tecnica_cinco_porques  
  El metodo RCCA de Juran contra la tecnica de los cinco porques: metodos vecinos, sano. FIGURAS, dos, las dos ya registradas. El racimo de los cinco porques del NUCLEO censado en franja 1040, y la familia de analisis de causa raiz del mundo quality censada en franja 1038, que con juran_rcca_metodo llega a CUATRO miembros.
- **1098** | quality/medicion_calidad_2 contra quality_audit  
  Medir la calidad por area con graficos de tendencia visibles contra los cuatro pasos de correr una auditoria: objetos distintos, sano. FIGURAS, tres, y una es fuerte. Sufijo _N vivo en quality, medicion_calidad_2, vigesimo octavo miembro. Numero de paso en el titulo, se llama Paso 3. Y NUEVA: medicion_calidad (franja 247, 562, 684 y 851) TAMBIEN se llama Paso 3. Son dos nodos distintos con el mismo numero de paso del mismo programa, y con el mismo contenido: recolectar metricas por area, clasificar los defectos y publicar graficos visibles con metas al lado. Es el cuarto paso del programa de Crosby que aparece duplicado, junto al 6, al 10 y al 11.
- **1100** | quality/sistema_estable_responsabilidad_gerencial contra rediseno_procesos_negocio_cx  
  Verificar con grafico de control que el sistema es estable contra redisenar los procesos que le dan friccion al cliente: objetos distintos, sano. FIGURA, amplia la de franja 1079: el racimo de quality sobre causas comunes y responsabilidad del sistema llega a ONCE nodos con sistema_estable_responsabilidad_gerencial.
- **1102** | quality/distincion_causas_comunes_especiales_2 contra no_sacrificar_calidad_por_velocidad  
  Causas comunes contra especiales, contra el andon cord y la deuda tecnica: marcos distintos, sano. FIGURA: sufijo _N vivo y trio calcado, ya registrados.
- **1108** | franquicias/cadencia_seguimiento_prospectos contra tacticas_cold_calling  
  La cadencia de siete contactos en siete dias contra las tacticas de llamada en frio: momentos distintos, sano. FIGURA: par calcado gestion_seguimiento_prospectos con cadencia_seguimiento_prospectos, ya registrado en franja 1054.
- **1116** | quality/benchmarking_proceso contra framework_excelencia_operacional  
  El proceso de benchmarking de siete pasos contra las preguntas de excelencia operacional: objetos distintos, sano. FIGURA: racimo de benchmarking en quality, ya censado en franja 1055.
- **1120** | franquicias/concepto_de_advances contra objetivos_de_llamada_orientados_a_avance  
  El avance como venta pequena progresiva contra definir objetivos de llamada orientados a la accion: sano por contenido, y con figura. FIGURA, amplia la de franja 983: la familia del avance y el compromiso en el NUCLEO llega a CUATRO nodos. advances_vs_continuations (610), obtencion_de_compromiso (127), obtencion_compromiso_venta (219), obtencion_compromiso (983) y objetivos_de_llamada_orientados_a_avance (1120) suman de hecho CINCO piezas de la misma doctrina de SPIN.
- **1124** | quality/reporte_auditoria contra quality_audit  
  Elaborar el reporte de auditoria contra los cuatro pasos de correr una auditoria: momentos distintos, sano. FIGURA, amplia las de franja 608 y 967: la familia de auditoria de calidad del mundo quality llega a CINCO nodos con reporte_auditoria.
- **1125** | risk_management/tu_gestion_de_riesgo_funciona contra matriz_probabilidad_impacto  
  Auditar y mejorar tu propio metodo de riesgo contra priorizar riesgos por probabilidad e impacto: objetos distintos, sano. FIGURA NUEVA: segundo par calcado dentro del mundo risk_management. como_sabes_que_tu_metodo_sirve (franja 927) y tu_gestion_de_riesgo_funciona (franja 1125) mandan lo mismo, comparar tus predicciones de riesgo pasadas con lo que ocurrio de verdad y cambiar el metodo si no atina en vez de repetirlo porque da calma.
- **1129** | quality/analisis_flujo_proceso_servicio contra plan_mejora_procesos  
  El diagrama de flujo del servicio con linea de invisibilidad contra el plan de mejora de procesos: metodos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **1131** | quality/relacion_largo_plazo_proveedor_unico contra colaboracion_cadena_suministro  
  La relacion de largo plazo con proveedor unico contra compartir datos de inventario con tu cadena: objetos distintos, sano. FIGURA NUEVA, decimotercera del tipo de ids casi identicos: relaciones_largo_plazo_con_proveedores (franja 599, 637, 995 y 1132) y relacion_largo_plazo_proveedor_unico (franja 1131), los dos del mundo quality y los dos con la misma receta de Deming, reducir proveedores por articulo hasta quedarte con uno, evaluar por evidencia de mejora y no por precio, y firmar acuerdos de largo plazo.
- **1141** | quality/brainstorming contra internal_idea_capture  
  Las reglas y la mecanica de la sesion de ideas contra el sistema interno de captura de ideas: objetos distintos, sano. FIGURA: el nodo brainstorming del mundo quality junto al trio del nucleo, ya registrado en franja 671.
- **1147** | quality/brainstorming contra bundle_ideas  
  Las reglas y la mecanica de la sesion de ideas contra agrupar las ideas en un solo sistema: momentos distintos, sano. FIGURAS: el nodo brainstorming del mundo quality y la costura de bundle_ideas, las dos ya registradas.
- **1148** | quality/equipo_mejora_calidad contra diseno_organizacional  
  Convocar representantes de cada area como agentes de cambio contra disenar el equipo por como circula la informacion: objetos distintos, sano. FIGURAS: numero de paso en el titulo, equipo_mejora_calidad se llama Paso Dos, y par calcado con equipo_mejora_calidad_2, las dos ya registradas en franja 694.
- **1149** | quality/evaluacion_desempeno_junta_directiva contra revisiones_regulares_desempeno_ceo  
  Evaluar el desempeno de la junta directiva contra las revisiones escritas del desempeno del fundador: objetos distintos, sano. FIGURA: costura en revisiones_regulares_desempeno_ceo, ya registrada en franja 663.
- **1151** | quality/establecer_proyecto_y_metas_diseno contra how_might_we_briefs  
  Establecer el proyecto y sus metas de diseno contra reformular el objetivo como Como podriamos: momentos distintos, sano. FIGURA: racimo de how_might_we en el nucleo, ya censado en franja 634.
- **1152** | quality/pocos_vitales_muchos_utiles contra gestion_de_portafolio_gates_go_kill  
  Clasificar proyectos en vitales pocos y utiles muchos contra el embudo con gates y Go Kill: momentos distintos, sano. FIGURAS: par calcado de vitales pocos y racimo de portafolio del nucleo, las dos ya registradas.
- **1153** | compras/punto_unico_contacto_proveedores contra criterios_seleccion_proveedores  
  Designar un unico punto de contacto con proveedores contra la matriz ponderada de seleccion: objetos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, ya registrada.
- **1155** | health_safety/process_tracing_methods contra pensamiento_serial_vs_espacial  
  Los metodos de rastreo de procesos para reconstruir el episodio contra elegir la herramienta de pensamiento correcta: objetos distintos, sano. FIGURA: process_tracing_methods es el miembro DIECINUEVE de la familia de health_safety censada en franja 460, y es de los que mas explicito lo dice, manda documentar las conclusiones evitando el lenguaje de deficit humano.
- **1159** | quality/innovacion_tipo_ii contra resolver_problemas_grandes  
  Hacerlo mas grande, mas pequeno o combinarlo contra buscar puntos de dolor grandes: metodos distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **1160** | quality/mistake_proofing_poka_yoke_2 contra regla_simplificada_tolerancia_errores  
  Poka yoke con sus cinco principios contra la regla de dos lineas: niveles distintos, sano. FIGURAS: sufijo _N vivo y trio calcado de poka yoke, ya registrados en franja 803.
- **1161** | environmental/formar_consejo_asesor_sostenibilidad contra formalize_advisory_board  
  Formar un consejo asesor de sostenibilidad contra formalizar el consejo asesor: el mundo especializa, sano. FIGURA NUEVA: par calcado DENTRO DEL NUCLEO. identificar_junta_asesores (franja 475) y formalize_advisory_board (franja 1161) mandan lo mismo, mapear que asesores necesitas por area, reclutar por impacto real, sumar clientes como asesores y acordar frecuencia y compensacion.
- **1163** | quality/poka_yoke_a_prueba_de_errores contra five_whys_inversion_proporcional  
  Poka yoke en el punto donde el humano se equivoca contra los cinco porques: momentos distintos, sano. FIGURAS: trio calcado de poka yoke y racimo de los cinco porques del nucleo, las dos ya registradas.
- **1164** | quality/politica_no_culpar_trabajador contra five_whys_inversion_proporcional  
  Analizar la distribucion de errores entre personas antes de sancionar contra los cinco porques: metodos distintos, sano. FIGURA: racimo de once nodos de quality sobre causas comunes y responsabilidad del sistema, ya censado en franja 1100.
- **1165** | compras/usa_el_no_del_proveedor_a_tu_favor contra obtencion_de_compromiso  
  Usar el no del proveedor a tu favor contra las cuatro acciones para obtener compromiso: lados opuestos de la mesa, sano. FIGURA: familia del avance y el compromiso en el nucleo, ya censada en franja 1120.
- **1183** | compras/escucha_activa_requisitos contra senales_de_compra_en_venta_grande  
  Escuchar activamente para captar el requisito real contra distinguir las senales de compra en ventas grandes: lados opuestos de la mesa, sano. FIGURA NUEVA: par calcado DENTRO DEL NUCLEO. senales_de_compra_reales (franja 171, 309, 545, 581 y 757) y senales_de_compra_en_venta_grande (franja 1183) mandan lo mismo, no celebrar porque el cliente menciono problemas, distinguir problema mencionado de necesidad explicita y esperar la necesidad explicita antes de dar la conversacion por buena.
- **1184** | compras/preguntas_abiertas_motivacion_proveedor contra criterios_seleccion_proveedores  
  Preguntas abiertas para descubrir la motivacion del proveedor contra la matriz ponderada de seleccion: momentos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, ya registrada.
- **1186** | quality/desarrollo_de_controles_de_proceso contra plan_mejora_procesos  
  Desarrollar los controles y transferirlos a operaciones contra el plan de mejora de procesos: momentos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **1188** | quality/proceso_nominacion_seleccion contra pruning_portafolio  
  Nominar y filtrar proyectos candidatos contra podar el treinta por ciento mas debil: momentos distintos, sano. FIGURA: racimo de portafolio del nucleo, ya censado en franja 829.
- **1190** | seguridad_digital/evaluar_controles contra risk_audit  
  Evaluar los controles implementados contra auditar la gestion de riesgos: objetos distintos, sano. FIGURA: marco-pais en seguridad_digital, el POA&M y las Tareas A-N, ya registrada en franja 546.
- **1199** | environmental/consolidacion_cargas_backhaul contra programacion_entregas_delivery_scheduling  
  Consolidar cargas y aprovechar los viajes de vuelta contra decidir entre entrega directa y milk run: metodos distintos, sano. FIGURAS: herramienta con nombre propio, el nodo del mundo cita Empty Miles Service, ya registrada en franja 65. Y el par calcado del nucleo programacion_entregas_delivery_scheduling con milk_run_deliveries, ya registrado en franja 1067.
- **1214** | quality/descubrir_necesidades_cliente contra voz_del_cliente_voc  
  Recolectar y priorizar necesidades contra observar al cliente en su entorno: metodos distintos, sano. FIGURA: costura ya confirmada en voz_del_cliente_voc.
- **1221** | environmental/eco_efectividad_re_evolucion_industrial contra diseno_para_sostenibilidad_cradle_to_cradle  
  La eco efectividad como re evolucion industrial contra el mapeo cradle to cradle: niveles distintos, sano. FIGURA, amplia la de franja 1029: el racimo de cradle to cradle en environmental llega a ONCE piezas con eco_efectividad_re_evolucion_industrial, que es ademas el TERCER nodo del mundo que se titula eco efectividad, junto a eco_efectividad (80 y 124) y eco_efectividad_2 (425).
- **1226** | quality/lenguajes_jerarquia_organizacional contra cash_is_king  
  Traducir tus metricas operativas al lenguaje del dinero contra revisar el saldo y el flujo de caja cada semana: niveles distintos, sano. FIGURA, amplia la de franja 816: la familia del efectivo contra la ganancia en el NUCLEO es un TRIO. diferencia_ganancia_flujo_caja (320), profit_vs_cash (816) y cash_is_king (1226). Los tres mandan mirar el flujo de caja aparte del estado de resultados, calcular cuanto consumes al mes y no fiarte de la utilidad en papel.
- **1234** | quality/sistema_responsabilidad_gerencial contra curse_cinco_culpas  
  Mapear los componentes del sistema y evaluar si le permitia al otro hacerlo bien contra facilitar los cinco porques: marcos distintos, sano. FIGURA, amplia la de franja 1100: el racimo de quality sobre causas comunes y responsabilidad del sistema llega a DOCE nodos con sistema_responsabilidad_gerencial, que es ademas el id base del que ya estaba registrado con sufijo, sistema_responsabilidad_gerencial_2.
- **1240** | franquicias/manejo_objeciones_venta_franquicia contra enfoque_etapa_investigacion  
  Preparar respuestas a las objeciones tipicas contra priorizar la etapa de investigacion sobre la de demostracion: momentos distintos, sano. FIGURA, amplia la de franja 998: la familia de la etapa de investigacion en el NUCLEO es un TRIO. etapa_investigacion_ventas (660), etapa_de_investigacion (1000) y enfoque_etapa_investigacion (1240). Los tres mandan lo mismo, dedicar mas tiempo a preguntar que a presentar, resistir la tentacion de saltar a la demostracion y medir la proporcion entre preguntar y presentar en tus llamadas.
- **1241** | quality/desarrollar_caracteristicas_proceso_2 contra customer_development_modelo  
  Disenar el proceso que crea y entrega tu producto contra salir a hablar con clientes antes de construir: objetos distintos, sano. FIGURAS: sufijo _N vivo en desarrollar_caracteristicas_proceso_2 y racimo de customer discovery del nucleo, las dos ya registradas.
- **1243** | quality/reporte_auditoria contra risk_audit  
  Elaborar el reporte de auditoria contra auditar la gestion de riesgos: objetos distintos, sano. FIGURA: familia de auditoria de calidad del mundo quality, ya censada en franja 1124.
- **1248** | quality/analisis_beneficio_costo contra analisis_tco_roi_b2b  
  El analisis beneficio costo contra el analisis de TCO y ROI en ventas B2B: objetos distintos, sano. FIGURA: costura visible en analisis_tco_roi_b2b, ya registrada en franja 31, nueve pasos con dos bloques, vender B2B en 1 a 4 y evaluar proveedores por costo ponderado en 5 a 9.
- **1250** | quality/matriz_de_seleccion contra criterios_seleccion_proveedores  
  La matriz de seleccion con reparto de cien puntos contra la matriz ponderada para elegir proveedor: objetos distintos, sano. FIGURA: costura visible en criterios_seleccion_proveedores, ya registrada.
- **1253** | quality/innovacion_tipo_ii contra starting_points_innovacion  
  Hacerlo mas grande, mas pequeno o combinarlo contra el punto de partida push o pull: niveles distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **1262** | exportacion/proteccion_propiedad_intelectual_2 contra proteccion_propiedad_intelectual  
  Registrar la propiedad intelectual en cada mercado destino contra dejar documentado desde el inicio de quien es la idea: momentos distintos, sano. FIGURA NUEVA y es una variante del sufijo que no habia salido: proteccion_propiedad_intelectual_2 vive en el mundo exportacion y proteccion_propiedad_intelectual vive en el NUCLEO. El sufijo _2 no distingue a dos hermanos del mismo mundo sino que choca con el id de un nodo del catalogo gratis. Los contenidos si son distintos, pero los ids se pisan.
- **1269** | quality/tipos_innovacion_i_ii contra brainstorming_divergente  
  Los dos tipos de innovacion contra las reglas de la divergencia: metodos distintos, sano. FIGURAS: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii y costura en brainstorming_divergente, las dos ya registradas.
- **1270** | quality/trilogia_de_juran contra plan_gestion_calidad  
  La trilogia de Juran contra el plan de gestion de calidad: niveles distintos, sano. FIGURA NUEVA: par calcado dentro del mundo quality, trilogia_juran_qa_qc (franja 763) con trilogia_de_juran (franja 1270). Los dos narran la misma trilogia, separar planificar de controlar y de mejorar, distinguir el pico esporadico del desperdicio cronico y darle a cada uno su tratamiento.
- **1273** | quality/analisis_causa_raiz_diagnostico contra tecnica_cinco_porques  
  El diagnostico de causa raiz con Pareto y validacion estadistica contra la tecnica de los cinco porques: metodos distintos, sano. FIGURAS: racimo de los cinco porques del nucleo y familia de analisis de causa raiz de quality, las dos ya censadas.
- **1278** | quality/analisis_vendibilidad contra analisis_tco_roi_b2b  
  Medir la disposicion a pagar por cada caracteristica contra el analisis de TCO y ROI en B2B: objetos distintos, sano. FIGURA: costura visible en analisis_tco_roi_b2b, ya registrada en franja 31.
- **1279** | quality/establecer_proyecto_y_metas_diseno contra how_might_we_brief_social  
  Establecer el proyecto y sus metas de diseno contra traducir metas globales en briefs accionables: momentos distintos, sano. FIGURA, amplia la de franja 634: la familia del encuadre del problema en el NUCLEO llega a CINCO nodos con how_might_we_brief_social. how_might_we_briefs, how_might_we_hmw, how_might_we_framing, encuadre_desafio_diseno y how_might_we_brief_social.
- **1286** | exportacion/metodos_exportacion_directa_indirecta_2 contra seleccion_canal_fisico  
  Elegir entre exportacion directa e indirecta contra elegir el canal fisico de distribucion: objetos distintos, sano. FIGURA: sufijo _N vivo en exportacion, metodos_exportacion_directa_indirecta_2. Vigesimo noveno miembro.
- **1288** | quality/competencias_ingeniero_calidad contra plan_gestion_calidad  
  Las competencias del ingeniero de calidad contra el plan de gestion de calidad: objetos distintos, sano. FIGURA: organismo certificador con nombre propio, el nodo del mundo manda certificar ante ASQ con la credencial CQE. Misma especie que la registrada en franja 544.
- **1289** | quality/equipo_mejora_calidad_2 contra plan_gestion_recursos_humanos  
  Armar el equipo de mejora de calidad contra el plan del equipo del proyecto: objetos distintos, sano. FIGURA: sufijo _N vivo y par calcado de equipo_mejora_calidad_2, ya registrados.
- **1291** | environmental/eco_efectividad_2 contra disenar_para_sanacion  
  Eco efectividad contra disenar para la sanacion: marcos vecinos, sano. FIGURAS: sufijo _N vivo en eco_efectividad_2 y racimo de cradle to cradle en environmental, las dos ya registradas.
- **1293** | quality/estructuracion_programa_auditoria contra protocolo_reuniones_gate  
  Armar las reglas de tu programa de auditoria contra las reglas de tus reuniones de decision: objetos distintos, sano. FIGURA, amplia la de franja 1124: la familia de auditoria de calidad del mundo quality llega a SEIS nodos con estructuracion_programa_auditoria. auditoria_calidad, principios_auditoria_calidad, programa_auditoria_calidad, concepto_de_auditoria_de_calidad, reporte_auditoria y estructuracion_programa_auditoria.
- **1294** | quality/planificacion_estrategica_despliegue_2 contra roadmap_proyectos_operacionales_12_meses  
  Integrar la calidad en tu plan de negocio contra el plan de doce meses de proyectos de operaciones: objetos distintos, sano. FIGURAS, dos, las dos NUEVAS. Sufijo _N vivo en quality, planificacion_estrategica_despliegue_2, trigesimo miembro. Y par calcado con planificacion_estrategica_despliegue (franja 130): los dos bajan la vision y la mision a metas anuales, meten la voz del cliente al mismo nivel que las metas financieras y alinean el reconocimiento con las metas de mejora.
- **1297** | exportacion/marco_legal_comercio_electronico_internacional contra cumplimiento_magnuson_moss  
  Las reglas legales para vender online en otros paises contra cumplir la ley Magnuson-Moss: sano, y con figura fuerte. FIGURA NUEVA: marco-pais DENTRO DEL NUCLEO, y del tipo mas duro que ha salido. cumplimiento_magnuson_moss estructura todo el nodo alrededor de una ley federal estadounidense, incluido el paso de consultar a un abogado que conozca esa ley, sin ninguna condicion de pais. El contraste con el nodo del mundo, que si condiciona por pais destino, deja la comparacion servida para el auditor.
- **1302** | quality/lenguajes_jerarquia_organizacional contra profit_vs_cash  
  Traducir tus metricas operativas al lenguaje del dinero contra la diferencia entre ganar y tener el dinero: niveles distintos, sano. FIGURA: trio del efectivo contra la ganancia en el nucleo, ya censado en franja 1226.
- **1315** | franquicias/eleccion_abogado_franquicias contra seleccion_abogado_venture  
  Elegir un abogado especializado en franquicias contra elegir uno especializado en capital de riesgo: objetos distintos, sano. FIGURA: pais cableado, el nodo del mundo pide validar experiencia en el marco regulatorio estatal, marco estadounidense, sin condicion de pais. Ya registrada como figura.
- **1319** | quality/ciclo_de_mejora_continua_helix contra design_test_repeat  
  El ciclo de cuatro pasos y la helice de mejora continua contra disenar, probar y repetir: marcos vecinos, sano. FIGURA, amplia la de franja 845: la familia del ciclo de mejora en el mundo quality es un TRIO. pdsa_shewhart_cycle (783), ciclo_pdca_pdsa (845) y ciclo_de_mejora_continua_helix (1319). Los tres narran el mismo ciclo de disenar, probar, poner en el mercado o ejecutar, estudiar el resultado y repetir.
- **1320** | quality/sistema_de_alarma_de_defectos contra sistema_inmune_producto  
  El sistema de alarmas de calidad con responsables y tiempos contra el sistema inmune del producto: niveles distintos, sano. FIGURA: costura visible en sistema_inmune_producto, ya registrada en franja 803.
- **1324** | environmental/compra_equipos_verdes contra indice_de_reparabilidad  
  Como elegir equipos tecnologicos sostenibles contra disenar el puntaje de reparabilidad de tu producto: lados opuestos, comprar contra fabricar. Sano. FIGURA: herramientas y certificaciones con nombre propio en el nodo del mundo, Energy Star y la Guide to Greener Electronics de Greenpeace. Se anotan sin asumir que siguen o no vigentes.
- **1327** | quality/mistake_proofing_poka_yoke_2 contra five_whys_inversion_proporcional  
  Poka yoke con sus cinco principios contra los cinco porques: momentos distintos, sano. FIGURAS: trio calcado de poka yoke y racimo de los cinco porques del nucleo, las dos ya registradas.
- **1342** | quality/crosby_programa_14_pasos_introduccion contra rediseno_procesos_negocio_cx  
  La introduccion al programa de catorce pasos contra redisenar los procesos que le dan friccion al cliente: objetos distintos, sano. FIGURA, amplia las de franja 937 y 1052: el mundo quality tiene TRES nodos que describen o presentan el mismo programa de catorce pasos de Crosby. concepto_programa_catorce_pasos, programa_mejora_calidad_14_pasos y crosby_programa_14_pasos_introduccion.
- **1345** | quality/establecer_vision_organizacional_2 contra metas_objetivos_smart_innovacion  
  Redactar la vision del negocio contra las metas SMART de innovacion: objetos distintos, sano. FIGURA: sufijo _N vivo y par calcado de establecer_vision_organizacional_2, ya registrados en franja 129.
- **1349** | quality/decide_phase_roadmap contra pivotar_o_proceder  
  La fase Decide del roadmap de transformacion contra decidir si pivotas o sigues: objetos distintos, sano. FIGURA NUEVA: RACIMO de pivotar o proceder DENTRO DEL NUCLEO, cuatro nodos. actualizar_modelo_de_negocio_pivot_o_proceed (918), reunion_pivotar_o_perseverar (1039), decision_pivotar_o_proceder (1329) y pivotar_o_proceder (1349). Los cuatro mandan lo mismo, sentarte con tu equipo o inversor, revisar evidencia real y no opiniones, clasificar el entusiasmo del cliente, actualizar el lienzo y decidir formalmente si cambias de rumbo o sigues.
- **1354** | quality/ciclo_shewhart_pdsa contra plan_mejora_procesos  
  El ciclo de Shewhart paso a paso contra el plan de mejora de procesos: niveles distintos, sano. FIGURAS, dos. Costura ya confirmada en plan_mejora_procesos. Y amplia la de franja 1319: la familia del ciclo de mejora en el mundo quality llega a CUATRO nodos con ciclo_shewhart_pdsa, junto a pdsa_shewhart_cycle, ciclo_pdca_pdsa y ciclo_de_mejora_continua_helix. Dos de ellos tienen ademas ids casi identicos, pdsa_shewhart_cycle y ciclo_shewhart_pdsa, con las mismas palabras permutadas.
- **1365** | quality/roi_proyectos_calidad contra analisis_tco_roi_b2b  
  El ROI de un proyecto de mejora de calidad contra el analisis de TCO y ROI en B2B: objetos distintos, sano. FIGURA: costura visible en analisis_tco_roi_b2b, ya registrada.
- **1368** | quality/innovacion_tipo_ii contra construir_sobre_ideas_ajenas  
  Hacerlo mas grande, mas pequeno o combinarlo contra construir sobre las ideas de otros: niveles distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **1375** | health_safety/bad_apple_theory contra curse_cinco_culpas  
  La teoria de la manzana podrida contra facilitar los cinco porques sin culpables: marcos vecinos, sano. FIGURA: bad_apple_theory es el miembro VEINTE de la familia de health_safety censada en franja 460, y es el que nombra la doctrina contraria con su propio titulo.
- **1383** | risk_management/guarda_lo_que_aprendiste_de_cada_golpe contra fracaso_como_aprendizaje_startup  
  Guardar la leccion de cada susto contra tratar el fracaso como aprendizaje: angulos distintos, sano. FIGURA NUEVA, decimocuarta del tipo de ids casi identicos y la primera de ese tipo DENTRO DEL NUCLEO: fallo_como_aprendizaje_startup (visto en decenas de pares) y fracaso_como_aprendizaje_startup (franja 1383). Los dos son del nucleo, los dos mandan lo mismo, aceptar el fallo como parte de la busqueda, reorientarse rapido con los hechos nuevos y no penalizar al equipo por una hipotesis fallida. Los ids se distinguen por una sola palabra, fallo contra fracaso.
- **1388** | quality/falacia_problemas_diferentes contra superioridad_producto_beneficios  
  La falacia de creer que tu negocio es distinto contra la superioridad por beneficios: objetos distintos, sano. FIGURA: costura visible en superioridad_producto_beneficios, ya registrada en franja 688.
- **1412** | quality/establecer_proyecto_y_metas_diseno contra plan_mejora_procesos  
  Establecer el proyecto y sus metas de diseno contra el plan de mejora de procesos: objetos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **1421** | quality/mapeo_flujo_valor contra mapa_flujo_trabajo_cliente  
  Mapear el flujo de valor de la concepcion a la comercializacion contra dibujar el flujo de trabajo del cliente: objetos distintos, sano. FIGURA NUEVA: RACIMO de mapeo del flujo de valor repartido entre mundos y nucleo, CINCO nodos. En quality, lean_manufacturing (376), ocho_desperdicios_lean (806) y mapeo_flujo_valor (1421). En environmental, value_stream_mapping_ambiental (767). Y en el nucleo, analisis_flujo_de_valor, que es la contraparte de casi todos ellos. Los cinco mandan mapear el estado actual, clasificar cada actividad en valor agregado o no, y redisenar eliminando lo que no aporta.
- **1423** | quality/revision_diseno contra dia_en_la_vida_del_cliente  
  La revision formal de diseno contra un dia en la vida del cliente: objetos distintos, sano. FIGURA NUEVA: par calcado DENTRO DEL NUCLEO. mapa_flujo_trabajo_cliente (franja 441 y 1421) y dia_en_la_vida_del_cliente (franja 1423) mandan lo mismo, observar al cliente en su entorno, documentar como resuelve el problema hoy sin tu producto, dibujar el antes y el despues y repetirlo por cada tipo de persona que decide.
- **1427** | franquicias/tasa_captura_leads contra optimizacion_embudo_get_customers  
  Optimizar la tasa de captura del formulario contra optimizar el embudo de conseguir clientes: niveles distintos, sano. FIGURAS, dos, las dos NUEVAS. Herramientas con nombre propio en el nodo del NUCLEO: optimizacion_embudo_get_customers manda usar Optimizely, Visual Website Optimizer o Unbounce. Y par calcado DENTRO DEL NUCLEO con ids casi identicos, decimoquinto de ese tipo: funnel_get_customers_optimizacion (franja 611) y optimizacion_embudo_get_customers (franja 1427). Los dos mandan lo mismo, definir la metrica del embudo, correr pruebas A/B, comparar valor del cliente contra costo de adquisicion antes de escalar y concentrarse en el canal validado.
- **1437** | quality/desarrollar_caracteristicas_proceso_2 contra plan_mejora_procesos  
  Disenar el proceso que crea y entrega tu producto contra el plan de mejora de procesos: momentos distintos, sano. FIGURAS: sufijo _N vivo en desarrollar_caracteristicas_proceso_2 y costura en plan_mejora_procesos, las dos ya registradas.
- **1440** | quality/responsabilidad_gerencial_causas_comunes contra regla_simplificada_tolerancia_errores  
  Distinguir causas comunes de especiales y asumir las del sistema contra la regla de dos lineas: niveles distintos, sano. FIGURA: racimo de doce nodos de quality sobre causas comunes y responsabilidad del sistema, ya censado en franja 1234.
- **1442** | quality/tipos_innovacion_i_ii contra definicion_tipos_nuevo_producto  
  Los dos tipos de innovacion contra la taxonomia de seis tipos de nuevo producto: objetos distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **1449** | risk_management/cual_es_tu_mayor_riesgo contra leap_of_faith_questions  
  Escribir cual crees que es tu mayor riesgo y como lo sabes contra las preguntas de salto de fe: angulos vecinos, sano. FIGURA NUEVA, decimosexta del tipo de ids casi identicos y la segunda DENTRO DEL NUCLEO: leap_of_faith_assumptions (franja 959) y leap_of_faith_questions (franja 1449). Los dos mandan hacer explicitas las suposiciones criticas del modelo, priorizar cual representa el mayor riesgo y disenar un experimento para validarla.
- **1458** | quality/accion_correctiva_2 contra five_whys_inversion_proporcional  
  Pasar de detectar a prevenir con analisis de tendencias contra los cinco porques: metodos vecinos, sano. FIGURAS: sufijo _N vivo y familia de siete miembros de accion correctiva en quality, las dos ya registradas.
- **1459** | quality/analisis_vendibilidad contra superioridad_producto_beneficios  
  Medir la disposicion a pagar por cada caracteristica contra la superioridad por beneficios: momentos distintos, sano. FIGURA: costura visible en superioridad_producto_beneficios, ya registrada.
- **1468** | quality/innovacion_tipo_ii contra seis_formas_innovar_perfil_cliente  
  Hacerlo mas grande, mas pequeno o combinarlo contra las seis formas de innovar desde el perfil del cliente: metodos distintos, sano. FIGURA: par calcado tipos_innovacion_i_ii con innovacion_tipo_ii, ya registrado.
- **1471** | compras/investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor contra customer_discovery_get_out_of_building  
  Investigar con fuentes objetivas antes de contactar al proveedor contra salir a hablar con clientes de verdad: lados opuestos de la mesa, sano. FIGURA, amplia la de franja 869: el racimo de customer discovery en el NUCLEO llega a SIETE nodos con customer_discovery_get_out_of_building.
- **1476** | quality/establecimiento_metas_de_calidad contra metas_objetivos_smart_innovacion  
  Fijar metas de calidad validadas contra benchmarks contra las metas SMART de innovacion: angulos distintos, sano. FIGURA: trio de metas de calidad en quality, ya censado en franja 601.
- **1477** | quality/evaluacion_alternativas_solucion contra bundle_ideas  
  Evaluar alternativas de solucion con matriz de seleccion contra agrupar las ideas en un solo sistema: momentos distintos, sano. FIGURA: costura visible en bundle_ideas, ya registrada en franja 143.
- **1480** | quality/revision_progreso_breakthrough contra plan_mejora_procesos  
  Revisar el avance de los proyectos de mejora cada trimestre contra el plan de mejora de procesos: objetos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **1481** | quality/rol_alta_direccion_benchmarking contra pivotar_o_perseverar  
  Tu compromiso al liderar un benchmarking contra decidir si pivotas o perseveras: objetos distintos, sano. FIGURA, amplia la de franja 1349: el racimo de pivotar o proceder en el NUCLEO llega a CINCO nodos con pivotar_o_perseverar.
- **1489** | quality/reinicio_programa_calidad contra rediseno_tras_fracaso_proyecto  
  Formar un equipo nuevo y repetir el programa contra no repetir el mismo enfoque tras un fracaso: objetos distintos, sano. FIGURA NUEVA, y es el quinto paso duplicado del programa de Crosby: reinicio_programa_calidad se llama Paso 14 y repeticion_programa (franja 1494) TAMBIEN se llama Paso 14. Los dos mandan lo mismo, formar un equipo nuevo cada doce a dieciocho meses, conmemorar el aniversario y reiniciar el ciclo completo. Con este van cinco pasos del programa duplicados: el 3, el 6, el 10, el 11 y el 14.
- **1494** | quality/repeticion_programa contra diseno_para_el_ciclo_completo  
  Hacerlo de nuevo cada doce a dieciocho meses contra disenar para el ciclo completo del proyecto: objetos distintos, sano. FIGURA: el par de nodos que se llaman los dos Paso 14, anotado en franja 1489.
- **1513** | franquicias/elaboracion_fdd contra regla_divulgacion_garantia  
  Elaborar el documento de divulgacion de la franquicia contra reunir los terminos de la garantia en un solo documento: objetos distintos, sano. FIGURA: pais cableado, el nodo del mundo estructura todo alrededor del FDD estadounidense, con sus veintitres secciones y su plazo de catorce dias. Ya registrada como figura y es de las instancias mas duras del mundo franquicias.
- **1517** | quality/establecer_vision_organizacional_2 contra estrategia_de_innovacion_de_producto  
  Redactar la vision del negocio contra la estrategia de innovacion de producto: objetos distintos, sano. FIGURAS, dos. Sufijo _N vivo y par calcado de establecer_vision_organizacional_2, ya registrados. Y una NUEVA, decimoseptima del tipo de ids casi identicos y la tercera DENTRO DEL NUCLEO: estrategia_de_innovacion_y_tecnologia (franja 237 y 754), estrategia_innovacion_producto (franja 795) y estrategia_de_innovacion_de_producto (franja 1517) son TRES nodos del nucleo con ids casi iguales y la misma doctrina, definir metas de innovacion, elegir arenas estrategicas, repartir el presupuesto por tipo de proyecto y comprometerse con una vision de largo plazo.
- **1525** | quality/medicion_calidad contra checkpoints_validacion  
  Medir la calidad por area con linea base contra los checkpoints que validan cada hipotesis: objetos distintos, sano. FIGURA: numero de paso en el titulo, medicion_calidad se llama Paso 3, ya registrada.
- **1539** | exportacion/evaluacion_preparacion_empresa_exportar contra evaluacion_ventana_mercado  
  Evaluar si tu empresa esta lista para exportar contra evaluar la ventana de oportunidad del mercado: objetos distintos, sano. FIGURA: pais cableado, el nodo del mundo manda hacer la evaluacion formal en export.gov. Ya registrada.
- **1547** | quality/analisis_flujo_proceso_servicio contra blueprint_de_experiencia  
  El diagrama de flujo del servicio con linea de invisibilidad contra el mapa de experiencia del cliente: metodos vecinos, sano. FIGURA NUEVA y es la costura mas larga del cribado: blueprint_de_experiencia tiene DIECISIETE pasos en al menos CUATRO bloques apilados. Los pasos 1 a 4 mapean la experiencia y sus momentos emocionales; los pasos 5 a 8 son otra narracion sobre el proceso de postventa y los momentos de ansiedad; los pasos 9 a 13 son otra mas sobre el ritual de celebracion cuando el prospecto se vuelve cliente; y los pasos 14 a 17 son otra sobre listar puntos de contacto, redisenar el traspaso entre vender y dar soporte y asignar responsable a cada punto. Supera a principio_calidad_mvp, que tenia catorce pasos en tres bloques.
- **1552** | quality/pdsa_shewhart_cycle contra tecnica_cinco_porques  
  El ciclo PDSA contra la tecnica de los cinco porques: metodos distintos, sano. FIGURAS: familia del ciclo de mejora en quality y racimo de los cinco porques del nucleo, las dos ya censadas.
- **1557** | franquicias/preparar_fdd contra conditions_precedent_financing  
  Preparar el documento de divulgacion de la franquicia contra las condiciones previas del financiamiento: objetos distintos, sano. FIGURAS, dos. Pais cableado, el nodo del mundo cablea los veintitres items requeridos por la FTC y el plazo de catorce dias, marco estadounidense. Y NUEVA, decimoctava del tipo de ids casi identicos: elaboracion_fdd (franja 1513) y preparar_fdd (franja 1557), los dos del mundo franquicias, los dos sobre redactar el mismo documento con las mismas veintitres secciones y el mismo plazo.
- **1563** | quality/sipoc contra plan_mejora_procesos  
  El mapa SIPOC contra el plan de mejora de procesos: herramientas distintas, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **1568** | franquicias/programa_cumplimiento_legal contra evitar_terminos_enganosos_garantia  
  Un sistema para reducir el riesgo de demandas al vender franquicias contra evitar terminos enganosos en la garantia: objetos distintos, sano. FIGURA: pais cableado, el nodo del mundo manda capacitar cada ano en la ley de franquicias y hacer compras de prueba para verificar el cumplimiento, sin condicion de pais. Ya registrada.
- **1574** | quality/control_mantener_ganancias contra plan_gestion_calidad  
  El plan de control para mantener las ganancias contra el plan de gestion de calidad: niveles distintos, sano. FIGURA: es un miembro mas de la familia de plan de control y matriz de control del mundo quality, ya registrada como par calcado en la cola de 346. Con control_mantener_ganancias esa familia llega a TRES, junto a plan_de_control y matriz_de_control_de_proceso.
- **1577** | quality/dmaic_fase_define contra plan_mejora_procesos  
  La fase Define de DMAIC contra el plan de mejora de procesos: momentos distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **1584** | environmental/monetizacion_npv_caso_negocio contra propuesta_gasto_capital  
  Monetizar los factores clave y calcular el NPV contra la guia para analizar un gasto de capital: niveles distintos, sano. FIGURA: costura visible en propuesta_gasto_capital, doce pasos en dos bloques que cuentan el mismo analisis dos veces, ya registrada en franja 554.
- **1591** | health_safety/sesgo_retrospectivo_hindsight_2 contra reconocer_sesgo_de_apofenia  
  El sesgo de mirar hacia atras contra reconocer la apofenia y el sesgo de patrones: angulos vecinos, sano. FIGURA: sufijo _N vivo en health_safety, sesgo_retrospectivo_hindsight_2, ya registrado en franja 589.
- **1592** | quality/enfoque_proyecto_por_proyecto contra plan_mejora_procesos  
  Breakthrough proyecto por proyecto contra el plan de mejora de procesos: niveles distintos, sano. FIGURA: costura ya confirmada en plan_mejora_procesos.
- **1594** | quality/establecer_vision_organizacional contra estrategia_de_innovacion_de_producto  
  Vision, mision y estrategias contra la estrategia de innovacion de producto y tecnologia: niveles distintos, sano. FIGURA: trio de estrategia de innovacion con ids casi identicos en el NUCLEO, ya registrado en franja 1517.
- **1595** | quality/optimizacion_caracteristicas_diseno contra actualizar_modelo_de_negocio_pivot_o_proceed  
  Optimizar las caracteristicas con revisiones formales de diseno contra decidir si pivotas o sigues: objetos distintos, sano. FIGURA: racimo de pivotar o proceder en el nucleo, ya censado en franja 1349 y ampliado en 1481.
- **1603** | exportacion/seleccion_canales_distribucion contra seleccion_canal_distribucion  
  El mundo especializa la eleccion de canal al comercio internacional sobre la base lean del nucleo: sano. FIGURA NUEVA, decimonovena del tipo de ids casi identicos, y la PRIMERA TRANSDOMINIO de esa figura: seleccion_canales_distribucion en exportacion contra seleccion_canal_distribucion en el nucleo, separados por una sola letra de plural. Verificado: las dieciocho anteriores viven todas dentro de un mismo mundo o dentro del nucleo, ninguna cruza la frontera. DISCREPANCIA DE ORDINAL: el encargo la llama OCTAVA; en este registro la octava es la franja 723. Anotada en la seccion de adjudicacion del informe, sin resolver. Par de borde.
- **1604** | risk_management/manten_viva_tu_lista_de_riesgos contra matriz_probabilidad_impacto  
  Mantener vivo el registro de riesgos contra priorizar por probabilidad e impacto: momentos propios, sano. FIGURA: QUINTA verificacion post-cirugia no buscada. manten_viva_tu_lista_de_riesgos es uno de los cinco peldanos que reescribio la cirugia 1 (08988ad, verificado en el commit) y vuelve a la cola por su cuenta, como los cuatro de la tabla de la ficha. Par de borde.

### 8.4 Lo que no cupo en las clases (15 notas dentro de pares D o C)

- **140** | compras/muestra_puntos_en_comun_antes_de_negociar contra apertura_llamada_venta_grande  
  El mundo manda dedicar unos minutos a preguntas personales antes de negociar y el nucleo manda NO gastar tiempo en aperturas personales en ventas grandes. NOTA para el informe: no es problema de la vara, son situaciones distintas (comprar cara a cara contra abrir una venta grande), pero es un choque de consejo que el lector puede encontrarse si ve los dos en el mismo plan.
- **303** | risk_management/deja_de_ignorar_el_riesgo contra no_jugar_con_probabilidades  
  Darte permiso de pensar en negativo contra rechazar la paralisis de las probabilidades. NOTA para el informe, segundo choque de consejo del mismo tipo que franja 140: el mundo manda dedicarle tiempo semanal a lo que preferirias no pensar y el nucleo manda evitar planes de contingencia que desvien el foco de encontrar la solucion. Son doctrinas opuestas sobre el mismo acto, no un problema de la vara.
- **407** | quality/inventory_analysis_lean contra ratios_eficiencia_inventario  
  Identificar y clasificar cada punto de inventario del flujo de valor contra calcular los ratios de dias y rotacion. Metodos distintos. NOTA: el nodo del nucleo ratios_eficiencia_inventario tiene ocho pasos y el paso 5 (calcular la rotacion actual) repite el paso 2. Lo anoto aqui como costura probable, no la marco como figura porque el bloque 5 a 8 si agrega objetos nuevos (retorno sobre ventas y ciclo de conversion de efectivo).
- **557** | quality/establecer_proyecto_y_metas_diseno contra brief_de_diseno  
  Establecer el proyecto y sus metas de diseno con metricas SMART contra el brief de diseno que deliberadamente no sobre especifica. NOTA menor: los dos hablan del mismo documento inicial pero con doctrinas opuestas sobre cuanto precisar, el mundo pide metricas SMART y el nucleo advierte de no dictar la solucion. No es problema de la vara.
- **618** | quality/evaluacion_de_desempeno_merito contra gestion_desempeno_feedback  
  Eliminar la calificacion por meritos segun Deming contra montar revisiones de desempeno formales y periodicas. NOTA para el informe, tercer choque de consejo del tipo de franja 140 y 303: el mundo manda eliminar o redisenar la evaluacion individual anual y el nucleo manda ponerla en marcha y que nadie se quede sin la suya. Doctrinas opuestas sobre el mismo acto.
- **647** | quality/calificacion_productos_procesos contra mejora_continua_relentless  
  Calificar el cambio antes de implementarlo contra iterar cambios pequenos sin esperar la revision anual. NOTA menor: son doctrinas de ritmo opuesto sobre el mismo acto, probar antes de soltar contra soltar rapido y medir. Menos marcado que los choques de franja 140, 303 y 618.
- **732** | quality/programa_cero_defectos contra regla_simplificada_tolerancia_errores  
  El programa de cero defectos como prevencion contra la regla de tolerar el primer error. NOTA menor: son doctrinas de tolerancia opuestas sobre el mismo acto, el mundo dice que ningun defecto es inevitable y el nucleo dice que el primer error se tolera siempre.
- **753** | quality/cultura_integridad_objetividad_resolucion_problemas contra curse_cinco_culpas  
  Discutir los problemas sin buscar culpables contra facilitar los cinco porques sin culpables. Marcos vecinos. NOTA: cultura_integridad_objetividad_resolucion_problemas es la misma doctrina de no culpar a la persona que en health_safety ocupa quince nodos, pero vive en quality. La doctrina cruza mundos.
- **1144** | compras/ten_un_checklist_de_clausulas_de_contrato contra elementos_contrato_legal  
  El checklist de clausulas que todo contrato necesita contra los elementos que hacen valido un contrato. Angulos vecinos, complementarios. NOTA: el nodo del nucleo manda consultar las leyes estatales y locales de contratos, que es marco-pais suave dentro del nucleo.
- **1187** | quality/optimizacion_de_procesos contra rediseno_procesos_negocio_cx  
  Ajustar a fondo el proceso y cada una de sus partes contra redisenar los procesos que le dan friccion al cliente. Objetos distintos. NOTA: el nodo del mundo se apoya en si mismo, manda aplicar las mismas tecnicas que ya usaste antes sin decir cuales, igual que el nodo de franja 28 que quedo como B.
- **1386** | quality/breakthrough_desempeno_actual contra five_whys_inversion_proporcional  
  El ciclo DMAIC de ruptura del desempeno contra los cinco porques. Marcos distintos. NOTA: breakthrough_desempeno_actual es el nodo del mundo de la unica A de la primera parte de la franja, puesto 15, donde quedaba a la altura del gratis frente a plan_mejora_procesos. Aqui, contra los cinco porques, la comparacion no repite el problema.
- **1391** | exportacion/paris_convention_prioridad contra patentes_startup  
  Usar el derecho de prioridad del Convenio de Paris contra el proceso de patente provisional. Marcos distintos. NOTA: aqui el nodo del mundo si usa un marco internacional en vez de cablear un pais, que es lo contrario de la figura de marco-pais.
- **1499** | exportacion/seleccion_canales_exportacion contra seleccion_canal_distribucion  
  Elegir los canales de venta internacional contra elegir el canal de distribucion. Angulos vecinos, y aqui chocan: el mundo manda seleccionar varios canales complementarios y el nucleo manda enfocarse en UNO solo durante el descubrimiento. NOTA para el informe, es otro choque de consejo del tipo de franja 140.
- **1543** | quality/rework_por_el_causante contra curse_cinco_culpas  
  Corregir tu mismo el error que causaste contra facilitar los cinco porques sin culpables. NOTA: aqui el mundo y el nucleo tiran en direcciones distintas, el mundo devuelve el error a quien lo causo y el nucleo prohibe senalar a la persona. No es problema de la vara, pero es un choque de doctrina visible.
- **1589** | exportacion/exclusividad_territorial_representante contra clausula_no_shop_adquisicion  
  Definir la exclusividad territorial de tu representante contra la clausula de no-shop en la venta de tu empresa. Objetos distintos. NOTA: el nodo del mundo si manda verificar si las leyes de tu pais permiten ese limite territorial, que es el contraste sano del marco-pais.

---

Cribado completo: 1.606 de 1.606, con los cinco pares de borde anexados.
Ningun nodo se toco.

---

## 9. La adjudicacion del auditor

El auditor leyo las 2 A y las 6 B y las adjudico. Lo que sigue es su veredicto,
con la verificacion que hice contra el grafo antes de escribirlo.

### 9.1 Las dos A: VIOLACIONES CONFIRMADAS

Las dos quedan confirmadas como violaciones de la vara. **Y el auditor les
encontro una causa comun que yo no habia visto: las dos son sombras de los dos
nodos costurados del nucleo.**

| franja | nodo del mundo | pasos | nodo del nucleo | pasos | el nucleo esta costurado |
|---:|---|---:|---|---:|---|
| **15** | `quality/breakthrough_desempeno_actual` | 5 | `plan_mejora_procesos` | 15 | si, tres bloques apilados |
| **124** | `environmental/eco_efectividad` | 3 | `economia_circular_como_modelo_de_negocio` | 9 | si, dos bloques apilados |

**Verificado contra el grafo, nodo por nodo:**

- `breakthrough_desempeno_actual` (quality, 5 pasos) es el DMAIC de manual:
  define, mide, analiza causas raiz, implementa mejoras, establece controles.
- `plan_mejora_procesos` (nucleo, 15 pasos) **no son quince decisiones**. El
  tercer bloque (pasos 11 a 15) vuelve a contar el segundo casi paso por paso:
  el paso 11 (*define el resultado final que el proceso debe producir*) es el
  paso 8 (*definir el output esperado del proceso antes de disenar los pasos*);
  el paso 13 (*establece metricas para cada etapa*) es el paso 9 (*establecer
  metricas de exito en cada etapa*); el paso 14 (*asigna responsabilidad clara
  a una organizacion o individuo por cada paso*) es el paso 10 (*asignar
  responsabilidad clara por cada paso*). Es la costura que el lote 10 ya le
  habia confirmado.
- `eco_efectividad` (environmental, 3 pasos): piloto, ciclos biologico y
  tecnico, materiales de upcycling.
- `economia_circular_como_modelo_de_negocio` (nucleo, 9 pasos) **son cinco
  decisiones contadas dos veces**. El segundo bloque (6 a 9) repite el primero:
  el paso 6 (*mapear el ciclo de vida actual*) es el paso 1 (*mapear el ciclo
  de vida completo*); el paso 8 (*disenar un mecanismo de retorno o
  remanufactura*) es el paso 3 (*redisenar el modelo para incluir recuperacion,
  reuso o regeneracion*); el paso 9 (*calcular el impacto en sostenibilidad y
  en costos*) es el paso 5 (*medir el impacto economico y ambiental*).

> **La lectura del auditor, en una linea: las violaciones de la franja no son
> enfermedad nueva. Son la acrecion del gratis tapando al pago.**
>
> El nodo del nucleo no gana la comparacion porque sepa mas. La gana porque
> **abulta**: cuenta la misma doctrina dos o tres veces y llega a la mesa con
> quince pasos contra cinco, o nueve contra tres. La vara del gradiente estaba
> midiendo una costura y llamandola profundidad.

### 9.2 La cura acoplada, para la pasada unica

El auditor dicta **una sola cura, de dos manos, para las dos A**, y las dos
manos se hacen en la misma pasada:

1. **Destejer el costurado del nucleo.** Quitar el bloque repetido reduce la
   sombra sin quitarle nada al lector: `plan_mejora_procesos` pierde una
   narracion, no una decision, y `economia_circular_como_modelo_de_negocio`
   pasa de nueve pasos a las cinco decisiones que de verdad tiene.
2. **Profundizar el nodo del mundo con su propio libro**, que es **el patron de
   la cirugia 1**: no se copia del nucleo ni se le recorta al nucleo, se le da
   al nodo de pago la voz y el metodo de su propia fuente.

**Las dos manos juntas o ninguna.** Destejer solo el nucleo deja el par igual
de plano por el otro lado; profundizar solo el mundo deja la costura viva. Y la
cirugia 1 ya demostro, cuatro veces sin buscarlo, que cuando las dos se hacen
el par vuelve a la cola por su cuenta y pasa.

### 9.3 Las seis B: OK las seis

Ninguna de las seis es violacion. El veredicto del auditor, una por una:

| franja | par | veredicto |
|---:|---|---|
| **22** | `quality/criterios_seleccion_proyectos_calidad` contra `gestion_de_portafolio_gates_go_kill` | **OK.** Especializacion real: la matriz de nominaciones es del mundo. |
| **28** | `quality/optimizacion_de_procesos` contra `mejora_continua_relentless` | **OK apretado.** El nodo del mundo es flaco y autorreferente: **candidato a engorde, no caso de vara.** |
| **52** | `exportacion/plataformas_comercio_electronico_marketplaces` contra `channels_hypothesis_web_mobile` | **OK.** Especializacion a marketplaces. |
| **79** | `seguridad_digital/getting_started_supply_chain_risk_management` contra `gestion_riesgo_cadena_suministro` | **OK.** Objetos distintos: gobierno cyber contra riesgo fisico de la cadena. |
| **104** | `franquicias/sitio_web_captura_leads` contra `diseno_landing_page` | **OK.** Tema propio, y la doctrina opuesta es legitima: captura de leads contra landing de autoservicio. |
| **610** | `franquicias/concepto_de_advances` contra `advances_vs_continuations` | **OK.** Especializacion con el CIRF. |

**La unica accion que sale de las seis** es la del 28, y no es de vara: el nodo
del mundo entra a la lista de engorde, no a la de violaciones.

### 9.4 Colateral de la adjudicacion

Dos cosas que la adjudicacion dejo registradas y que verifique antes de
escribir:

1. **El CUI del marco NIST en
   `seguridad_digital/getting_started_supply_chain_risk_management`.**
   Verificado en el paso 1 del nodo. Tercera instancia **registrada** de
   marco-pais en ese mundo tras los dos POA&M. Al contarla mediante el grafo
   salio ademas que **20 de los 55 nodos de ese mundo cablean el marco federal
   estadounidense**: el detalle esta en el apartado 4.6.
2. **La quinta verificacion post-cirugia no buscada** (franja 1604, uno de los
   pares de borde). `manten_viva_tu_lista_de_riesgos` es **uno de los cinco
   peldanos que reescribio la cirugia 1** (verificado en el commit `08988ad`,
   que toca ese archivo) y volvio a la cola por su cuenta, contra
   `matriz_probabilidad_impacto`, y **paso**: momento propio, sano. Es la quinta
   de la tabla de la ficha, que tenia cuatro. Y llego sola, otra vez: salio del
   agujero de borde, no de ninguna busqueda.

---

## 10. La muestra D, los racimos y lo que queda abierto

### 10.1 La muestra de validacion del cribado

**El auditor lee 61 pares D, el 5%, sorteados con semilla `81febf5c`, en
tandas.** Es la validacion final del cribado: si la muestra no encuentra en las
D nada que debiera haber sido A, B o C, la clasificacion de las 1.228 D queda en
pie.

El 5% se calcula sobre las **1.228 D** del archivo cerrado (1.228 por 0,05 son
61,4, que redondea a 61).

#### El procedimiento del sorteo, fijado y reproducible

El encargo anterior fijaba la semilla pero no el procedimiento, y sin
procedimiento una semilla no reproduce nada. **El auditor lo fijo, y queda
escrito aqui para que cualquiera pueda repetir el sorteo y obtener la misma
lista:**

```python
import json, random
V = [json.loads(l) for l in open('docs/FRANJA_VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]
D = sorted(v['puesto_franja'] for v in V if v['clase'] == 'D')   # 1228 puestos
muestra = sorted(random.Random("81febf5c").sample(D, 61))        # sin reemplazo
```

Poblacion: los puestos de clase D de `docs/FRANJA_VEREDICTOS.jsonl` **en orden
ascendente**, que son 1.228. Generador: `random.Random("81febf5c")` de Python.
Extraccion: `sample` de 61, **sin reemplazo**. Resultado ordenado ascendente.

> **REPRODUCIDO Y VERIFICADO.** Corri el procedimiento contra el archivo y la
> lista sale **identica a la dictada por el auditor, los 61 puestos, en el mismo
> orden**. Cero diferencias en los dos sentidos.

> **PIN OBLIGATORIO, y hay que leerlo antes de intentar reproducir el sorteo.**
> La poblacion del sorteo son las **1.228 D que habia en el archivo cuando se
> sorteo**, es decir el archivo tal como quedo en el commit **`e4af8c35`**. La
> propia muestra ya reclasifico un veredicto (**F822**, de D a C, ver la tanda
> 2), asi que **la poblacion viva ya no es la misma**: hoy son 1.227 D y el
> mismo procedimiento sobre esa poblacion **da otra lista** (comprobado: solo 34
> de los 61 puestos coincidirian).
>
> **Reproducir el sorteo se hace contra el pin, no contra el archivo vivo:**
>
> ```
> git show e4af8c35:docs/FRANJA_VEREDICTOS.jsonl
> ```
>
> **Y esto no es un defecto del sorteo: es lo que pasa cuando una muestra
> funciona.** Si la validacion encuentra algo, cambia el archivo que valida. La
> lista versionada de arriba es la que manda; el procedimiento sirve para
> auditarla contra el pin.

#### La lista completa, versionada

Los 61 puestos sorteados, con su par y su tanda. **Esta es la lista de
referencia**: si una relectura futura no coincide con ella, la que manda es la
que sale del procedimiento de arriba corrido sobre el archivo.

| puesto | tanda | par |
|---:|:--:|---|
| **18** | **1** | `compras/preguntas_abiertas_motivacion_proveedor` contra `gestion_procurement_consumo` |
| **40** | **1** | `health_safety/revision_de_aprendizaje` contra `curse_cinco_culpas` |
| **72** | **1** | `entrega/elegir_modo_transporte_volumen_distancia` contra `programacion_entregas_delivery_scheduling` |
| **85** | **1** | `quality/sistema_gestion_calidad` contra `metricas_calidad` |
| **103** | **1** | `quality/inhibidores_del_breakthrough` contra `coraje_para_pivotar` |
| **130** | **1** | `quality/planificacion_estrategica_despliegue` contra `creacion_estrategia_cadena_suministro` |
| **135** | **1** | `compras/preguntas_abiertas_motivacion_proveedor` contra `investigacion_como_habilidad_clave` |
| **258** | **1** | `quality/matriz_de_planificacion_arbol` contra `plan_gestion_recursos_humanos` |
| **268** | **1** | `franquicias/contratar_vendedor_franquicia` contra `contratar_cerrador_de_ventas` |
| **303** | **1** | `risk_management/deja_de_ignorar_el_riesgo` contra `no_jugar_con_probabilidades` |
| **363** | **1** | `entrega/mapear_servicio_antes_durante_despues` contra `encuesta_satisfaccion_postproyecto` |
| **378** | **1** | `quality/mantener_las_ganancias` contra `mejora_continua_relentless` |
| **392** | **1** | `quality/monitoreo_continuo_benchmarking` contra `mantener_puntaje_innovacion` |
| **449** | **1** | `quality/empoderamiento_personal_frontline` contra `documento_quien_es_quien_equipo` |
| **462** | **1** | `quality/innovacion_tipo_ii` contra `pensamiento_convergente_divergente` |
| **508** | **1** | `environmental/optimizacion_tecnologia_cadena_suministro` contra `cuatro_categorias_desempeno_cadena_suministro` |
| **580** | **1** | `quality/gestion_participativa_qc_circle_supervisores` contra `entrenamiento_gerencial` |
| **597** | **1** | `compras/preparate_para_marcharte_del_trato` contra `necesidad_vs_deseo_en_ma` |
| **602** | **1** | `risk_management/las_formas_en_que_los_proyectos_mueren` contra `definicion_producto_proyecto` |
| **603** | **1** | `compras/negocia_por_intereses_no_posiciones` contra `prevencion_objeciones_vs_manejo` |
| **621** | 2 | `quality/planificacion_cadena_suministro` contra `plan_gestion_adquisiciones` |
| **622** | 2 | `franquicias/ingenieria_inversa_metas` contra `metrics_that_matter_framework` |
| **631** | 2 | `quality/mejora_del_sistema_responsabilidad_gerencial` contra `no_sacrificar_calidad_por_velocidad` |
| **657** | 2 | `quality/cuestionario_autoevaluacion_gerencial_calidad` contra `framework_excelencia_operacional` |
| **673** | 2 | `quality/sistema_pull_push` contra `pull_no_push` |
| **686** | 2 | `quality/rotacion_de_puestos_para_mejora_calidad` contra `hr_calidad_gestion` |
| **715** | 2 | `franquicias/alternativa_operaciones_propias` contra `decision_autofinanciamiento_vs_inversion` |
| **730** | 2 | `quality/equipo_conjunto_de_mejora_con_proveedores` contra `plataforma_colaboracion_tiempo_real` |
| **756** | 2 | `risk_management/nombra_tus_suposiciones_fragiles` contra `definicion_producto_proyecto` |
| **796** | 2 | `entrega/medir_satisfaccion_real_del_cliente` contra `metricas_servicio_cliente_bts_bto` |
| **799** | 2 | `environmental/value_stream_mapping_ambiental` contra `modelo_simulacion_cadena_suministro_circular` |
| **804** | 2 | `compras/muestra_puntos_en_comun_antes_de_negociar` contra `preguntas_situacion` |
| **819** | 2 | `environmental/alineacion_engagement_estrategia_general` contra `cultura_de_buena_empresa` |
| **822** | 2 | `quality/institucionalizar_capacitacion` contra `rediseno_procesos_negocio_cx` |
| **853** | 2 | `quality/ausencia_valor_verdadero` contra `metricas_calidad` |
| **947** | 2 | `quality/desarrollo_expertos_capaces` contra `entrenamiento_funcional_empleados` |
| **957** | 2 | `quality/establecer_proyecto_y_metas_diseno` contra `definicion_objetivos_proyecto_sistema` |
| **961** | 2 | `quality/aceptacion_de_fallas_como_inevitables` contra `regla_simplificada_tolerancia_errores` |
| **1085** | 2 | `risk_management/el_riesgo_eres_tu` contra `transicion_post_sucesion` |
| **1096** | 2 | `franquicias/mito_control_calidad_corporativo` contra `decision_intensidad_capital` |
| **1128** | 2 | `exportacion/negociacion_acuerdo_representante_extranjero` contra `negociacion_contratos_proveedores` |
| **1130** | 2 | `quality/establecer_estandares_desempeno` contra `checklist_sistema_stage_gate_primera_clase` |
| **1135** | 2 | `quality/vacios_conocimiento_cliente` contra `enfoque_mercado_voc` |
| **1143** | 2 | `quality/roi_proyectos_calidad` contra `ranking_proyectos_por_npv` |
| **1170** | 2 | `quality/prepare_phase_roadmap` contra `fase_diseno_prototipado_modelos` |
| **1179** | 2 | `quality/vacios_conocimiento_cliente` contra `categorias_entusiasmo_cliente` |
| **1207** | 2 | `quality/diseno_servicio_calidad` contra `encuesta_satisfaccion_postproyecto` |
| **1217** | 2 | `risk_management/reporta_el_riesgo_sin_maquillaje` contra `cultura_transparencia_organizacional` |
| **1301** | 2 | `quality/evaluacion_desempeno_proyectos` contra `mantener_puntaje_innovacion` |
| **1312** | 2 | `compras/prepara_posicion_agenda_antes_negociar` contra `obtencion_de_compromiso` |
| **1362** | 2 | `quality/calculo_roi_calidad` contra `costo_de_oportunidad` |
| **1376** | 2 | `quality/desarrollar_caracteristicas_proceso` contra `determine_what_to_prototype` |
| **1379** | 2 | `risk_management/correr_hacia_el_riesgo` contra `fallo_como_aprendizaje_startup` |
| **1384** | 2 | `environmental/pilotos_estrategia_sostenibilidad` contra `fase_mobilizar_modelo_negocio` |
| **1399** | 2 | `risk_management/escepticismo_sano_ante_el_riesgo` contra `matriz_probabilidad_impacto` |
| **1426** | 2 | `environmental/pilotos_estrategia_sostenibilidad` contra `romper_vision_en_experimentos` |
| **1436** | 2 | `quality/auditorias_gerenciales_periodicas` contra `cultura_feedback_alta_frecuencia` |
| **1467** | 2 | `exportacion/promocion_sitio_web` contra `test_socios_de_trafico` |
| **1519** | 2 | `quality/reduccion_inventario_calidad` contra `gestion_riesgo_cadena_suministro` |
| **1529** | 2 | `franquicias/manejo_objeciones_venta_franquicia` contra `desarrollo_presentacion_problema` |
| **1565** | 2 | `entrega/decidir_vender_solo_online_o_tambien_tienda_fisica` contra `channels_hypothesis_physical` |

#### Marcador de la muestra

| | |
|---|---:|
| **pares D leidos por el auditor** | **41** de **61** |
| de esos, se sostienen como **D limpios de vara** | **41** |
| **violaciones encontradas** | **0** |
| **dudosos mal archivados** | **0** |
| **veredictos corregidos por figura** | **1** (F822, de D a C) |

**Cifras recomputadas del archivo, no del dictado.** Las 41 leidas son la tanda 1
(20 puestos, del 18 al 603) mas la tanda 2 (21 puestos, del 621 al 1128). Quedan
**20 por leer**, del 1130 al 1565.

#### TANDA 1 (puestos 18 a 603): VEINTE DE VEINTE

**Los veinte primeros de la muestra se sostienen.** El auditor los leyo contra
el grafo, uno por uno. **Cero violaciones de la vara y cero dudosos mal
archivados**: los veinte estaban bien clasificados como D.

**Lo que eso dice del cribado, con la cautela que corresponde:** veinte de
veinte es un tramo limpio, no una prueba cerrada. Con 20 de 61 leidos, lo que
esta validado es el primer tercio de la muestra. **Las dos tandas que faltan son
las que deciden.**

#### El matiz de F303: HUECO DEL ENCARGO, no error del cribado

Un solo par de la tanda dejo materia, y **el auditor lo adjudica como hueco del
encargo, no como fallo de la clasificacion**.

**Franja 303**: `risk_management/deja_de_ignorar_el_riesgo` contra
`no_jugar_con_probabilidades`. **El par porta una FRONTERA DE DOCTRINA**, y las
dos caras estan verificadas contra el grafo:

| | el mundo dice | el nucleo dice |
|---|---|---|
| **nodo** | `deja_de_ignorar_el_riesgo` (risk_management) | `no_jugar_con_probabilidades` (nucleo) |
| **fuente** | DeMarco y Lister, *Waltzing with Bears*, cap. 1 y 2 | Ben Horowitz, *The Hard Thing About Hard Things* |
| **doctrina** | *dedica quince minutos a proposito a escribir lo que preferirias no pensar*, y **date permiso de pensar en negativo un rato cada semana** | *rechaza la paralisis de las probabilidades*, **evita construir planes de contingencia que desvien el enfoque de encontrar la salida** |

**Por que el veredicto D era correcto.** El encargo listaba ocho figuras que
disparaban clase C, y **frontera de doctrina no estaba entre ellas**. Con las
instrucciones dadas, un par sano en gradiente cuyo unico hallazgo es un choque
de doctrina se clasifica D, que es exactamente lo que se hizo, **y la nota del
choque quedo escrita en la razon del veredicto** desde el primer momento, junto
con el parentesco con la franja 140.

> **El cribado no perdio la figura: la vio, la anoto y no tenia casilla donde
> ponerla.** El hueco es de la lista de figuras, no de la lectura.

**La figura entra a la ficha** como FRONTERA CANDIDATA junto a las cuatro
formuladas, con sus dos nodos y la nota de parentesco con
`risk_management/correr_hacia_el_riesgo`, que sale del mismo capitulo del mismo
libro que el nodo del mundo.


#### TANDA 2 (puestos 621 a 1128): VEINTIUNO DE VEINTIUNO limpios de vara

**Los veintiun pares de la tanda 2 se sostienen en la pregunta de la vara.** El
auditor los leyo contra el grafo. **Cero violaciones y cero dudosos escondidos**,
igual que la tanda 1.

**La muestra acumula 41 de 41 sin una sola violacion.** Con 41 de 61 leidos, dos
tercios de la validacion estan hechos y el cribado se sostiene en lo que vino a
comprobarse: **la clasificacion de las D como sanas de gradiente no ha fallado ni
una vez.**

**Pero la tanda dejo dos cosas que la tanda 1 no dejo**, y las dos se verificaron
contra el grafo antes de escribirlas. La primera obligo a corregir un veredicto;
la segunda desarmo una candidatura.

#### VERIFICACION 1 (F822): la figura estaba en la lista y se me escapo

**Resultado: es el primer C-como-D de la muestra. El veredicto queda corregido.**

`quality/institucionalizar_capacitacion` se titula **Instituir la Capacitacion
(Punto 6)**. Numero de paso en el titulo **estaba entre las ocho figuras que
disparaban C** en el encargo, asi que no cabe archivarlo bajo ninguna limitacion
declarada.

**Comprobado contra el informe, como pedia el encargo:** el racimo de los catorce
puntos de Deming **NO esta entre los treinta racimos censados** del apartado 4.1.
El que si esta es **el programa de catorce pasos de CROSBY**, que es otro
programa, de otro autor, con otra numeracion. **No son el mismo hallazgo.**

**Censo de la figura, verificado contra el grafo. Son SIETE nodos, todos de
`quality`, y todos llevan el numero de punto de Deming en el titulo:**

| punto | nodo | titulo |
|---:|---|---|
| **5** | `mejora_continua_del_sistema` | Mejora continua y permanente del sistema de produccion y servicio (Punto 5) |
| **6** | `institucionalizar_capacitacion` | Instituir la Capacitacion (Punto 6) |
| **7** | `adopcion_liderazgo` | Adoptar e Instituir el Liderazgo (Punto 7) |
| **8** | `eliminar_miedo` | Eliminar el Miedo (Punto 8) |
| **10** | `eliminar_slogans_metas` | Eliminar Slogans, Exhortaciones y Metas Numericas (Punto 10) |
| **13** | `fomento_educacion_autoeducacion` | Fomentar la Educacion y Autoeducacion (Punto 13) |
| **14** | `plan_de_accion_transformacion` | Plan de Accion para la Transformacion (Punto 14) |

> **Siete de los catorce puntos entraron al catalogo como nodos sueltos con el
> numero puesto**, exactamente la misma forma que ya se habia censado para los
> pasos de Crosby. **Es la misma figura, de otro programa.**

**La correccion, escrita sin adorno.** La figura estaba en la lista del encargo y
**la apliqué a los *Paso N* de Crosby pero nunca a los *Punto N* de Deming**. Su
primera aparicion en la cola no fue la 822: fue **la franja 159**
(`mejora_continua_del_sistema`), y la clasifiqué D. La 822 es donde la muestra la
cazo.

**Lo que cambia y lo que no:**

- **F822 pasa de D a C**, con la figura y el censo en su razon. Es el unico
  veredicto corregido por la muestra hasta ahora.
- **Las demas apariciones quedan D**, y no por dejadez: caen bajo la limitacion
  declarada en el apartado 2 (cuando una figura queda censada completa, los pares
  posteriores que solo tocan a un miembro ya contado se marcan D). El censo esta
  arriba, entero, que es lo que la adjudicacion necesita.
- **Las cifras de clase cambian**: 371 C y 1.227 D. Recomputadas del archivo.

#### VERIFICACION 2 (F947): el paralelo se sostiene a medias y la candidatura cae

**Resultado: la D se sostiene. NO es par calcado, y el dato que sostenia la
candidatura no esta en el texto.**

`quality/desarrollo_expertos_capaces` (Juran) contra
`core/entrenamiento_funcional_empleados` (Horowitz), leidos paso a paso:

| | quality (Juran) | nucleo (Horowitz) |
|---:|---|---|
| **1** | usar los resultados de la evaluacion de competencias como linea base | identificar las competencias clave de cada rol critico |
| **2** | disenar un curriculo de capacitacion por rol y nivel jerarquico | crear documentos o programas de entrenamiento especificos (*Good PM / Bad PM*) |
| **3** | **establecer un programa de certificacion interno** (Green Belt, Black Belt, Lean Expert) | **hacer obligatorio el entrenamiento antes de aprobar nuevas contrataciones** |
| **4** | medir el impacto de la capacitacion en el desempeno de los proyectos de mejora | medir la productividad de los nuevos empleados antes y despues |

**Lo que si se confirma:** el paralelo es real **en tres de los cuatro pasos**.
Los dos nodos montan el mismo esqueleto (linea base de competencias, programa por
rol, medicion despues), y eso es mas parecido de lo que decia mi razon original
(*metodos distintos*).

**Lo que lo desarma, y es el paso 3.** Ahi las dos doctrinas se separan de
verdad: **quality monta una estructura de certificacion interna** y **el nucleo
pone el entrenamiento como compuerta de contratacion**. No es el mismo consejo
dicho dos veces: son dos palancas distintas sobre el mismo material.

> **Y la premisa de la candidatura no esta en el catalogo, comprobado.** El
> encargo la apoyaba en que los dos lados usan **el mismo ejemplo, Green Belt**.
> **`entrenamiento_funcional_empleados` no dice Green Belt en ningun sitio**: ni
> en sus pasos, ni en su resumen, ni en su entregable. Su ejemplo es **Good PM /
> Bad PM**, de Horowitz.
>
> **Barrido del catalogo entero para no dejarlo en una sola lectura: Green Belt y
> Black Belt aparecen en DOCE nodos, y los doce son de `quality`. Ninguno del
> nucleo.** El vocabulario de los cinturones no cruza al catalogo gratis.

**Por eso la D queda**, con la verificacion escrita en su razon. **No la subo a B
tampoco**: los dos nodos tienen cuatro pasos, ninguno es mas hondo que el otro, y
la especializacion de quality es real (competencias, cinturones, proyectos de
mejora). No hay empate que adjudicar.

#### Hallazgo lateral de la verificacion 2: el racimo de los cinturones

El barrido de Green Belt y Black Belt destapo material que el cribado no habia
visto, porque **son nodos de `quality` contra `quality` y la franja solo miraba
mundo contra nucleo**. Se anota como **racimo CANDIDATO**, fuera del censo de
treinta, que esta cerrado:

- **El rol del Black Belt, tres veces**: `rol_black_belt`,
  `rol_black_belt_six_sigma` y `rol_facilitador_black_belt`.
- **La estructura de roles entera, dos veces**: `roles_six_sigma` y
  `estructura_competencias_six_sigma_lean`, las dos listando Green, Black, Master
  y Lean.
- **La certificacion y el entrenamiento de los cinturones, tres veces**:
  `certificacion_belts_six_sigma`, `entrenamiento_para_breakthrough` y
  `desarrollo_expertos_capaces`, que es el nodo que abrio esta verificacion.
- Y `rol_green_belt_six_sigma` para el Green Belt.

> **Nueve nodos de `quality` sobre la estructura de cinturones de Six Sigma.**
> Seria de los racimos mas grandes de los treinta censados si perteneciera a ese
> censo. **No se censa aqui**: el censo de treinta esta cerrado y este es
> material del barrido intra-dominio. **Queda anotado con su medicion para que el
> barrido lo encuentre hecho.**

### 10.2 Los treinta racimos: primer censo, adjudicacion despues

**Los treinta racimos del apartado 4.1 quedan como PRIMER CENSO del barrido
intra-dominio**, no como una lista de arreglos pendientes. Se adjudican
**despues** de la muestra D.

Tiene sentido en ese orden: el cribado los encontro de rebote, mirando pares de
mundo contra nucleo, y por eso el censo es el que cabe por esa ventana. El
barrido intra-dominio es la herramienta que los mira de frente, y adjudicar
treinta racimos con el censo parcial seria decidir con la mitad del mapa.

### 10.3 La asimetria de las costuras: pregunta abierta, con hipotesis

**21 costuras de 21 estan en nodos del nucleo. Ninguna en un nodo de mundo.**
Queda anotada como pregunta abierta, con una hipotesis concreta a comprobar en
el barrido:

> **Puede ser efecto del tamano de los nodos del nucleo, no de su salud.**

Una costura necesita sitio para verse: hacen falta dos bloques apilados, y los
nodos del nucleo son sistematicamente mas largos que los de mundo. Si el nucleo
concentra los nodos de nueve pasos para arriba, va a concentrar las costuras
aunque los dos lados enfermen exactamente igual.

**La comprobacion es barata y es del barrido: normalizar la tasa de costura por
longitud del nodo.** Si al comparar nodos de la misma longitud la asimetria
sobrevive, es salud del nucleo. Si desaparece, era el metro.

---

**Estado del encargo:** cribado cerrado (1.606 de 1.606), agujero de borde
cerrado, A y B adjudicadas, **muestra D sorteada y en curso (41 de 61, cuarenta y
uno de cuarenta y uno se sostienen en la vara, con un veredicto corregido por
figura)**, racimos esperando al barrido.
