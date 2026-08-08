# Exportación: los 30 leídos, con su clase y mi recomendación

Leídos uno a uno contra el criterio del fundador. **Cero API gastada.** La cita es
textual del cuerpo, para que puedas revocar sin abrir el grafo.

## Clase B-1 — FUSIONES INTERNAS primero (14 nodos → 5)

La clase es universal; lo que sobra es que la misma institución esté contada
varias veces. Fundir antes de reencuadrar evita pagar API por texto que se evapora.

### `recursos_apoyo_gubernamental_exportacion` absorbe 2
> Los tres listan agencias de apoyo. Uno dice CS/SBA/SBDC, otro FAS/USAID, el tercero MDC/USTDA: la misma accion, distinto directorio.

- **SOBREVIVE** Recursos de Apoyo Gubernamental para Exportadores (CS, SBA,  `recursos_apoyo_gubernamental_exportacion`
    - *"Existen múltiples agencias gubernamentales de EE.UU. que apoyan a las PyMEs exportadoras: el U.S. Commercial Service (CS) es el brazo de promoción com..."*
- Recursos de Agencias Gubernamentales para Exportadores `recursos_gubernamentales_exportacion`
    - *"Además del U.S. Commercial Service, múltiples agencias federales y estatales ofrecen apoyo a exportadores: el Foreign Agricultural Service (FAS) para ..."*
- Programas Gubernamentales de Asistencia a la Exportación `programas_asistencia_gubernamental_exportacion`
    - *"Existen múltiples agencias federales y estatales de EE.UU. (Millennium Development Corporation, USTDA, oficinas internacionales estatales) que ofrecen..."*

### `programas_ex_im_bank` absorbe 2
> Los tres son la misma institucion: el general, el de garantias y prestamos, y su Working Capital Guarantee que el general ya nombra.

- **SOBREVIVE** Programas de Financiamiento del Ex-Im Bank `programas_ex_im_bank`
    - *"El Export-Import Bank de EE.UU. ofrece seguro de crédito a la exportación, garantías de préstamo y préstamos directos para reducir riesgos comerciales..."*
- Financiamiento y Garantías del Ex-Im Bank `financiamiento_exim_bank_3`
    - *"El Export-Import Bank (Ex-Im Bank) de EE.UU. ofrece garantías de préstamo (Bank Buyer Credit Policy) y préstamos directos de mediano (1-5 años) y larg..."*
- Garantía de Capital de Trabajo (Working Capital Guarantee) `garantia_capital_trabajo`
    - *"Programa de preexportación de Ex-Im Bank que permite a los prestamistas otorgar financiamiento para que el exportador produzca o compre bienes destina..."*

### `recursos_apoyo_pymes_sba` absorbe 1
> La SBA contada dos veces: sus recursos y su financiamiento.

- **SOBREVIVE** Recursos de Apoyo de la SBA para Exportadores `recursos_apoyo_pymes_sba`
    - *"La U.S. Small Business Administration (SBA) y su red de socios (oficinas distritales, SBDCs, SCORE) ofrecen asesoría, capacitación y financiamiento pa..."*
- Programas de Financiamiento de la SBA para Exportadores `financiamiento_sba_exportacion`
    - *"La U.S. Small Business Administration (SBA) te ofrece garantías de préstamo si eres una pequeña empresa exportadora. El Export Working Capital Program..."*

### `uso_del_us_commercial_service` absorbe 1
> El mismo servicio, dos veces.

- **SOBREVIVE** Aprovechamiento del U.S. Commercial Service `uso_del_us_commercial_service`
    - *"El U.S. Commercial Service es un recurso gubernamental clave dentro del Global Entrepreneurial Ecosystem (GEE) que ayuda a pequeñas y medianas empresa..."*
- Asistencia del U.S. Commercial Service y Oficinas Locales `asistencia_us_commercial_service`
    - *"Red de especialistas comerciales internacionales que ofrecen asesoría gratuita o de bajo costo a PYMEs, incluyendo evaluación de potencial exportador,..."*

### `international_partner_search` absorbe 3
> Cuatro servicios del mismo catalogo para la misma necesidad: encontrar y verificar socios y compradores. La CLASE es 'servicios de busqueda de socios', y existe en casi todos los paises.

- **SOBREVIVE** Búsqueda Internacional de Socios (International Partner Sear `international_partner_search`
    - *"El International Partner Search del U.S. Commercial Service utiliza equipos de expertos en más de 75 países para encontrar los socios estratégicos más..."*
- Servicio Gold Key Matching `gold_key_matching_service`
    - *"El Gold Key Matching Service es una solución personalizada de búsqueda de compradores ofrecida por el U.S. Commercial Service en mercados clave de exp..."*
- Perfil de Compañía Internacional (ICP) `international_company_profile`
    - *"Un International Company Profile (ICP) es un informe de antecedentes sobre una empresa extranjera específica, preparado por oficiales comerciales del ..."*
- Programa Internacional de Compradores (IBP) `international_buyer_program`
    - *"El International Buyer Program (IBP) del Departamento de Comercio de EE.UU. apoya ferias comerciales nacionales destacadas con productos de alto poten..."*

## Clase B-2 — REENCUADRE a la clase universal (6)

El ejemplar es de EE.UU., pero **la clase existe en casi todos los países**.

| nodo | se vuelve |
|---|---|
| **Misiones Comerciales (Trade Missions)** `trade_missions` | misiones comerciales que organiza tu gobierno |
| **Consejos de Distrito de Exportación (District Export** `consejos_distrito_exportacion_dec` | redes locales de exportadores con experiencia |
| **Centro de Apoyo para Licitaciones (Advocacy Center)** `centro_asesoria_advocacy_center` | el respaldo de tu gobierno cuando compites en una licitacion extranjera |
| **Cumplimiento de Acuerdos Comerciales (TANC)** `cumplimiento_acuerdos_comerciales_tanc` | donde reclamar si un pais incumple un acuerdo comercial |
| **Seguro de Crédito a la Exportación (Export Credit In** `seguro_de_credito_a_la_exportacion` | el seguro de credito existe en casi todos los paises con agencia de credito a la exportacion (ECA) |
| **Construcción del Ecosistema Global de Emprendimiento** `ecosistema_global_emprendimiento_gee` | la red de apoyo publico y privado de tu pais |

## Clase B-3 — YA universales, solo citan fuentes de EE.UU. (6)

El concepto no tiene nada de estadounidense: los cinco métodos de pago son del
comercio internacional, y las barreras no arancelarias las pone cada país. Solo
hay que cambiar el directorio que citan.

| nodo |
|---|
| Selección del Método de Pago en Exportación `seleccion_de_metodo_de_pago` |
| Resolución de Problemas de Pago en Comercio Internacional `resolucion_problemas_de_pago` |
| Fuentes de Investigación de Mercado para Exportación `fuentes_investigacion_mercado` |
| Identificación y Gestión de Barreras Comerciales No Arancela `barreras_comerciales_no_arancelarias` |
| Investigación de Clientes Potenciales en el Extranjero `investigacion_empresa_extranjera` |
| Factores para Decisiones de Financiamiento de Exportación `decisiones_de_financiamiento_exportacion` |

## Clase C — FRONTERA CONDICIONAL (3)

Ni deprecar ciego ni universalizar falso: **alcanzan a quien toca esa cadena**,
sea o no de EE.UU. Se reencuadran con su condición honesta al frente.

| nodo | la condición |
|---|---|
| **Cumplimiento de las Export Administration Regula** `export_administration_regulations` | regulan articulos con componentes o tecnologia de EE.UU., aunque el exportador no sea estadounidense |
| **Cumplimiento de las Regulaciones Antiboicot** `antiboycott_regulations` | alcanzan a quien opera en esa cadena |
| **Cláusula Antidesviación (Destination Control Sta** `clausula_antidesviacion` | viaja en los documentos de embarque de casi todo envio que toque EE.UU. |

## DEPRECAR de selección (1)

**Programas Estatales y Locales de Financiamiento de Exportación** `programas_estatales_locales_financiamiento_exportacion`

> *"Varios estados y ciudades de EE.UU. operan programas propios de financiamiento a la exportación, incluyendo préstamos de capital de trabajo pre y post embarque, financiamiento de cuentas por..."*

**Subnacional de un país.** No hay clase universal: "los programas de tu estado"
no significa nada donde no hay estados con programa propio. Es el único de los 30
sin clase, y coincide con lo que el fundador ya había señalado.

## Cuentas

| clase | nodos | resultado |
|---|---:|---|
| B-1 fusiones internas | 14 | → 5 supervivientes, 9 absorbidos |
| B-2 reencuadre a clase | 6 | 6 re-vozados |
| B-3 ya universales | 6 | 6 re-vozados (solo el directorio) |
| C frontera condicional | 3 | 3 re-vozados con su condición |
| deprecar | 1 | 1 fuera de selección |
| **total** | **30** | **9 absorbidos, 15 re-vozados, 1 deprecado** |

Exportación quedaría en **148 activos** (de 149) tras las fusiones.