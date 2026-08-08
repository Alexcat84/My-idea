# El núcleo tiene regulación estadounidense sin censar — censo POR LECTURA

**Hallazgo del auditor, confirmado.** El censo de barandas halló 10 `dato_local`
en 1.721 porque el detector busca **siglas** (OSHA, EPA, FDA, IRS, SEC). Las
leyes por su **nombre** —Magnuson-Moss, JOBS Act, Sarbanes-Oxley— pasaban de
largo.

**Método**: barrido amplio de 38 pistas para acotar el montón (31 nodos de 1.618),
y luego **lectura de los 31**. Decide lo que el nodo *describe*, jamás la cadena.
Cero API. Cero cambios: esto es una lista para adjudicar.

---

## CLASE 1 — FALSO POSITIVO: menciona EE.UU. como ejemplo, el nodo es universal

**No se tocan.** Seis nodos donde la pista es una ilustración, no una dependencia.

| nodo | la cita que lo salva |
|---|---|
| `comprender_alineacion_etica_ia` | *"dominado por perspectivas occidentales"* — habla del sesgo de los datos, no de una ley |
| `convertir_necesidad_en_demanda` | design thinking; la palabra aparece en un ejemplo |
| `diseno_de_comportamiento_sostenible` | *"El caso del Departamento de Energía de EE.UU. (Shift Focus con IDEO)"* — un caso de estudio citado |
| `evaluacion_riesgos_legales_ia` | *"la legalidad varía según el país (la UE es más restrictiva, EE.UU. …)"* — **el nodo YA localiza**, es la exención de localización |
| `vesting_dinamico` | acuerdos de equity dinámicos; la mención es incidental |
| `compensacion_service_providers` | equity como pago; *409A* aparece de paso, el concepto es universal |

Van al **registro de falsos positivos adjudicados** si se aprueban.

---

## CLASE 2 — UNIVERSAL CON EJEMPLAR DE EE.UU. → reencuadre *"averigua qué aplica en tu país"*

El concepto existe en cualquier país; lo estadounidense es el ejemplo. **Se
reencuadra dentro del nodo**, como se hizo con LEED/Energy Star.

| nodo | qué es universal | qué es el ejemplar |
|---|---|---|
| `marcas_registradas` | registrar tu marca | *"El proceso en EE.UU. incluye tres pasos… USPTO"* |
| `patentes_startup` | proteger un invento | USPTO + costos en dólares (*$2.000-$10.000*) |
| `seleccion_estructura_corporativa` | elegir la forma legal de tu negocio | *"C Corp, S Corp o LLC"* son formas estadounidenses |
| `derechos_de_registro` | que el inversor pueda vender su parte | *"la SEC en Estados Unidos"* — **ya localiza, solo falta la vuelta al lector** |
| `registration_rights_stock_consideration` | cobrar una venta en acciones | SEC |
| `preparacion_due_diligence` | tener los papeles listos antes de levantar | *"estructurada como C Corporation en Delaware"* |
| `preparacion_para_salida_a_bolsa` | salir a bolsa | Sarbanes-Oxley como carga de ejemplo |

**Recomendación**: reencuadre con `--instruccion`, conservando el ejemplar entre
paréntesis. Coste: 7 nodos.

---

## CLASE 3 — LEY CON ALCANCE REAL → nodo-frontera condicional

Son leyes que **sí obligan**, a quien caiga bajo ellas. No se borran ni se
fingen universales: ganan la condición honesta al frente.

### 3a. LA FAMILIA MAGNUSON-MOSS — **diez nodos**, la más grande del hallazgo

`cumplimiento_magnuson_moss` · `clasificacion_garantia_full_limited` ·
`regla_divulgacion_garantia` · `regla_disponibilidad_previa_venta` ·
`prohibicion_tie_in_sales` · `evitar_terminos_enganosos_garantia` ·
`publicidad_garantia_conforme` · `mecanismo_resolucion_disputas` ·
`garantias_implicitas_vs_expresas` · `contratos_de_servicio_garantia` ·
`diferenciacion_garantia_contrato_servicio`

> *"La Magnuson-Moss Warranty Act regula las garantías escritas sobre productos
> de consumo **en EE.UU.**"*
> *"La ley exige que toda garantía escrita sobre un producto de más de **$10**
> se titule explícitamente como 'Full Warranty' o 'Limited Warranty'"*
> *"La FTC exige que toda garantía escrita sobre productos de más de **$15**…"*

**Es una rama entera del núcleo escrita sobre una ley de un solo país**, con sus
umbrales en dólares cableados. Un artesano en Bogotá que lea *"titula tu garantía
como Full o Limited"* está siguiendo una instrucción que no existe donde vive.

**Condición honesta propuesta**: *"si vendes productos de consumo en Estados
Unidos"*. Y el concepto universal que hay debajo —**decir por escrito y claro qué
cubre tu garantía, qué no, cuánto dura y cómo se reclama**— merece existir en el
núcleo sin la ley. Hoy **no existe**: es un hueco de contenido nuevo.

### 3b. VALORES Y LEVANTAMIENTO DE CAPITAL — cuatro nodos

`crowdfunding_legal_exemptions_jobs_act` · `equity_crowdfunding` ·
`cumplimiento_inversionistas_acreditados` · `cumplimiento_sarbanes_oxley`

> *"Vender una participación (security) requiere registrarla ante la SEC salvo
> que aplique una exención"* · *"Las leyes de valores de **EE.UU.** restringen la
> venta de acciones… a inversionistas acreditados"*

**Condición**: *"si levantas capital de inversionistas en Estados Unidos"*.

### 3c. FISCAL — tres nodos

`eleccion_83b` · `valuacion_409a` · `original_issue_discount_oid`

> *"Una elección 83(b) es una notificación al **IRS**"* · *"La Sección 409A del
> código fiscal de **EE.UU.**"*

**Condición**: *"si tú o tu empresa tributan en Estados Unidos"*. Estos tres son
los más atados: no hay concepto universal debajo, hay un trámite ante una
agencia concreta con un plazo concreto.

---

## CLASE 4 — DEPRECAR DE SELECCIÓN

**Ninguno.** A diferencia de los programas estatales o la MBDA, aquí ningún nodo
describe *un programa o una figura* de un país sin equivalente: todos describen
**leyes** que obligan de verdad a quien cae bajo ellas, y un nodo-frontera
condicional es más honesto que borrarlos.

---

## Resumen para adjudicar

| clase | nodos | acción propuesta | ¿cuesta API? |
|---|---:|---|---|
| falso positivo | 6 | al registro, sin tocar | no |
| universal + ejemplar | 7 | reencuadre `--instruccion` | sí |
| ley con alcance real | **18** | nodo-frontera condicional | sí |
| deprecar | 0 | — | — |
| **total leído** | **31** | | |

**Y un hueco de contenido que sale de aquí**, documentado sin inventarlo: el
núcleo tiene **once nodos sobre la ley de garantías de EE.UU. y cero sobre cómo
escribir una garantía honesta** para quien vende en cualquier otro sitio. Va a
la ficha `huecos-de-contenido`.

**Ninguna de estas 31 se toca hasta tu palabra.**
