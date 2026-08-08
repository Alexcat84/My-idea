# Fase 1 — lo que traigo antes de disparar un solo peso de API

**Séptimo paro.** El censo de las tres barandas sobre los siete packs dio 56
nodos. Los leí todos antes de decidir nada, y de la lectura salen **cuatro cosas
que no decido solo**.

Cero API gastada hasta aquí. El censo, la válvula y la lectura son locales.

---

## 1. LA BARANDA ESTÁ CAZANDO LA VOZ CORRECTA — 13 de los 56

El patrón de `residuo_corporativo` incluye:

```python
r"\btu equipo\b|\bsu equipo\b|\bel equipo de\b",
```

`\btu equipo\b` era **correcto en la era de la extracción**: un nodo recién
sacado del libro que decía *"tu equipo"* estaba arrastrando una empresa con
organigrama. Pero la re-voz de este mismo ciclo reescribió los nodos para
hablarle a una persona que **sí tiene dos o tres personas trabajando con ella**,
y *"tu equipo"* es justamente la voz que quedó.

**13 nodos tienen `tu equipo` como ÚNICO hallazgo, y los 13 están ya en segunda
persona con CERO tercera persona corporativa:**

| pack | nodo | 2.ª persona | 3.ª corporativa |
|---|---|---:|---:|
| environmental | `valor_intangible_sostenibilidad` | 8 | 0 |
| quality | `conciencia_calidad` | 2 | 0 |
| quality | `politica_de_calidad` | 9 | 0 |
| quality | `sistema_estable_responsabilidad_gerencial` | 4 | 0 |
| health_safety | `autoinspeccion_lugar_de_trabajo` | 7 | 0 |
| health_safety | `capacitacion_educacion_seguridad` | 7 | 0 |
| health_safety | `cultura_justa_organizacional` | 4 | 0 |
| health_safety | `ergonomia_laboral` | 5 | 0 |
| health_safety | `identificacion_recopilacion_informacion_peligros` | 9 | 0 |
| health_safety | `liderazgo_gerencial_seguridad` | 8 | 0 |
| health_safety | `programa_proteccion_denunciantes` | 5 | 0 |
| health_safety | `revision_aplicabilidad_estandares_osha` | 13 | 0 |
| franquicias | `definir_meta_a_5_anos_antes_de_franquiciar` | 23 | 0 |

**Ocho de los nueve de HSEQ son nodos que yo mismo re-vocé en el ciclo anterior.**
La baranda está señalando su propio trabajo terminado.

Es la misma clase que la guardia de acentos que rechazó 39 de 40 nodos buenos:

> **Una baranda que caza lo correcto no es estricta: está rota.**

Y es peor que inofensivo: re-vozarlos cuesta dinero y **arriesga degradar trece
nodos que ya están bien**, porque el modelo tiene que cambiar algo para
justificar su turno.

**Mi recomendación**: sacar `\btu equipo\b` del patrón y dejar `\bsu equipo\b` y
`\bel equipo de\b`, que sí delatan tercera persona. Los 13 salen del lote sin
tocarse. **No lo aplico hasta tu palabra**: es la vara del censo entero y
cambiarla por mi cuenta sería mover la regla a mitad de la medición.

Si la palabra es «déjala como está», los 13 entran al lote y se re-vozan.

---

## 2. TRES FUSIONES QUE EL ÍNDICE ANTERIOR NO VIO — la válvula las deja pasar

Aparecieron leyendo, no buscándolas. Las tres pasé por la válvula de pasos
accionables, que es la última palabra:

| par | solape de pasos | veredicto |
|---|---:|---|
| `evaluar_huella_carbono` **vs** `medir_huella_carbono_corporativa` | **19%** | fusión |
| `vision_alineacion_sostenibilidad` **vs** `vision_clara_sostenibilidad` | **16%** | fusión |
| `autoevaluacion_gerencial_exportacion` **vs** `evaluacion_preparacion_empresa_exportar` | **13%** | fusión |

Los tres pares son de packs **cuya fusión ya corrió en el ciclo del censo**. El
índice los propuso por parecido de título y estos se le escaparon: *"Evaluar la
Huella de Carbono de la Empresa"* y *"Medir la Huella de Carbono Corporativa"*
son el mismo nodo con dos verbos distintos.

**Y una CUARTA que la válvula frenó**, y la traigo como duda, no como fusión:

- `entrenamiento_supervisores` **vs** `entrenamiento_supervisores_calidad` —
  **6%**. Uno es *una conversación previa para que cada quien pueda explicar el
  programa*; el otro son *seis horas de instrucción estructurada por etapas*.
  Títulos casi idénticos, acciones distintas. El título mentía, los pasos no.

**Mi recomendación**: fundir los tres, conservar el cuarto. No ejecuto nada sin
tu palabra.

---

## 3. LOS CONCEPTOS QUE SOLO EXISTEN CON SU MARCO — la lista pedida

Ninguno se decide solo. Los ordeno por qué tan atado está el concepto a su marco:

### (a) ATADO A UNA INSTITUCIÓN DE UN SOLO PAÍS — el caso más claro

**`asistencia_agencias_minoritarias_mbda`** (exportación)
*"La MBDA es la única agencia federal dedicada al crecimiento de empresas
propiedad de minorías… más de 40 centros de negocios… eventos coordinados por
MBDA y el Departamento de Comercio."*

Es **exactamente la clase** que ya deprecaste de selección en este ciclo: los
programas estatales de financiamiento, NIOSH, SBREFA, los programas de OSHA. Una
agencia federal estadounidense para minorías estadounidenses no tiene equivalente
universal, y prometerlo sería deshonesto dos veces.

> *"Los programas de tu estado no significan nada donde no hay estados con
> programa."*

**Mi recomendación: DEPRECAR DE SELECCIÓN**, sin borrar.

### (b) MARCO INTERNACIONAL DE VERDAD — se quedan y se mantienen al día

**`familia_normas_iso_9000`** (quality) — ISO 9000 es del Comité Técnico 176 de
ISO, internacional, aplicable a cualquier tamaño y sector. Es una
**institución-de-libro**: no se omite, se mantiene al día. Va a la ficha
`vigencia-del-marco-internacional`.

**`certificacion_leed_energy_star`** (environmental) — aquí hay **dos cosas
mezcladas**: LEED (del USGBC, de origen estadounidense pero con consejos y
proyectos certificados en decenas de países) y **Energy Star con su Portfolio
Manager, que es de la EPA y solo estadounidense**. El nodo los trata como uno.
**Traigo la pregunta**: ¿se parte en dos (LEED se queda con nota de vigencia,
Energy Star se retira), o se reencuadra como *"busca el sello de eficiencia que
reconozcan en tu mercado"*? No lo decido.

### (c) MENCIÓN DE EJEMPLO, NO DEPENDENCIA — reencuadrables

**`quality_by_design`** — el concepto es de Juran, universal. La FDA aparece solo
como *"ha sido adoptado incluso por la FDA"*: un ejemplo de adopción, no un
requisito. Se reencuadra quitando o generalizando la mención.

**`adaptaciones_sectoriales_iso`** — **ya está reencuadrado**: dice *"las cGMP
que exige la FDA en Estados Unidos, **o el organismo equivalente en tu mercado**"*.
La baranda salta por la sigla, no por el encuadre. Es la ley que ya adjudicaste:
**detectar por mención en vez de por lo que el nodo describe**. Recomiendo
dejarlo intacto.

**`quimica_verde`** — los 12 principios de Anastas y Warner son universales.
REACH (europeo) y TSCA (estadounidense) aparecen como *"anticípate a regulaciones
futuras"*. Reencuadrable.

**`sistema_puntuacion_baldrige`** (quality) — Baldrige es un premio nacional
estadounidense, pero el nodo **ya reencuadró sus dimensiones** (*"para cada
proceso de tu negocio, califica el Enfoque, el Despliegue…"*). Lo único atado es
la escala de 0 a 1000 puntos. Reencuadrable quitando la escala.

---

## 4. LO QUE QUEDA PARA RE-VOZ, SI SE ADJUDICA COMO PROPONGO

| pack | del censo | menos falsos positivos | menos fusión/deprecación | a re-voz |
|---|---:|---:|---:|---:|
| environmental | 23 | −1 | −2 (fusión) −1 (LEED, pendiente) | **19** |
| quality | 10 | −3 | −1 (`adaptaciones_sectoriales_iso`) | **6** |
| health_safety | 9 | −8 | — | **1** |
| franquicias | 9 | −1 | — | **8** |
| exportacion | 4 | — | −1 (fusión) −1 (MBDA) | **2** |
| seguridad_digital | 1 | — | — | **1** |
| risk_management | 0 | — | — | **0** |
| **total** | **56** | **−13** | **−6** | **37** |

**Los dos packs nunca medidos salen casi limpios**: `seguridad_digital` 1 de 55,
`risk_management` **0 de 55**. Sus dos hallazgos eran falsos positivos que
verifiqué leyendo:

- `evalua_la_gravedad_sin_autoengano` dice *"para el emprendedor solo, **sin un
  jefe ni un comité** que lo contrapese"* — nombra el comité para decir que no lo
  hay.
- `la_matriz_de_colores_te_engana` es el nodo *"Por Qué la Matriz de Riesgo No
  Funciona"*, que argumenta **contra** las matrices. Ya estaba fichado al margen.

Es el mejor argumento a favor del SOP: los dos packs construidos con la vara
actual salen con **1 hallazgo real en 110 nodos**, contra los 6,6% del catálogo.

---

## Lo que necesito para seguir

1. `\btu equipo\b`: ¿sale del patrón o se queda?
2. Las tres fusiones: ¿se ejecutan?
3. MBDA: ¿deprecación de selección?
4. LEED/Energy Star: ¿se parte, se reencuadra o se deja?
5. `adaptaciones_sectoriales_iso`: ¿intacto, como recomiendo?

Con eso disparo el lote de re-voz de una sola vez, con su anotación en el libro
mayor.
