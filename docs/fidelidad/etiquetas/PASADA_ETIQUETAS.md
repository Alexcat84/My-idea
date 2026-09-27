# Pasada de fidelidad sobre las etiquetas de cara (25 sep 2026)

Decision del fundador (25 sep 2026): cada etiqueta del riel contra el titulo y el resumen de su nodo, buscando solo las que dicen lo CONTRARIO o algo DISTINTO del concepto, con verificador ciego y trampas como en la campania, corregidas por el ciclo de siempre.

## Resultado

- Etiquetas leidas: **3.169** (todos los nodos vivos del grafo; los 684 deprecados no se muestran en el riel).
- Corregidas en esta pasada: **38** (22 CONTRARIAS y 16 DISTINTAS), mas las **3** que el fundador nombro antes de la pasada (commit 6871a11e). Total en la lista de fidelidad: **41**.
- Las correcciones viven en `dataset/metadata/etiquetas_de_cara_v1_fidelidad.json`, la ultima lista de `scripts/etiquetas_de_cara.py` (manda sobre las demas), cada una con su motivo en `_motivos`. Los nodos no se tocan. Guardia: `engine/test_etiquetas_fidelidad.py`.

## Metodo

1. Los 3.169 nodos vivos se repartieron en 20 lotes (`pasada/preparar.py`, semilla fija).
2. Trampas: 4 por lote (2 CONTRARIAS y 2 DISTINTAS), 80 en total, escritas sobre nodos reales de OTRO lote para que no se delaten duplicadas. Tres de ellas son las tres etiquetas erroneas reales que nombro el fundador. Mezcladas a ciegas (`pasada/mezclar.py`); las claves en `pasada/claves/`.
3. Un lector por lote (repetido si dejaba escapar una trampa), un verificador ciego sobre todo lo marcado mas 1 de cada 6 limpias, y un arbitro en cada desacuerdo (`pasada/wf_lectura.js`). Todos los agentes en claude-opus-5-5, solo lectura.
4. La sesion releyo cada hallazgo contra su nodo y lo escribio (`pasada/aplicar.py`, que exige la cita literal del titulo o del resumen y 6 palabras como mucho). En 7 etiquetas la sesion ajusto la propuesta del lector (larga, conjugacion o tono): `pasada/ajustes_sesion.json`.

## Control de calidad

- Trampas: los lectores detectaron **79 de 80** (77 con el tipo exacto); el verificador ciego **78 de 79**. Las **3 trampas reales** (las etiquetas que nombro el fundador) se cazaron las tres.
- La trampa que se escapo (E03-092, "Elige entre Datos Propios o Existentes" donde el nodo manda combinarlos) tampoco la cazo la segunda lectura. Por eso un **verificador ciego extra** releyo E03 entero: cazo 3 de 4 trampas (la misma se le escapo), confirmo el hallazgo real de E03 y propuso uno nuevo (E03-099), que el **arbitro rechazo** por parcial y no distinta (`pasada/verificador_extra_E03.json`, `pasada/arbitro_E03-099.json`).
- 12 desacuerdos entre lector y verificador fueron al arbitro; de las 531 limpias muestreadas, 2 salieron con hallazgo tras verificar.

## Las 38 correcciones

| nodo | antes | despues | veredicto | quien decidio |
|---|---|---|---|---|
| `aprobacion_alta_direccion` | Involucra a la Alta Dirección | Involúcrate Tú Mismo en el Cambio | CONTRARIA | lector y verificador de acuerdo |
| `antidilucion_provisiones` | Protege tu Porcentaje de Dueño | Entiende la Protección Antidilución del Inversionista | CONTRARIA | lector y verificador de acuerdo |
| `capital_social_founder` | Construye tu Red Social | Construye tu Red Antes de Fundar | DISTINTA | lector y verificador de acuerdo |
| `protective_provisions` | Define tus Cláusulas de Veto | Conoce el Veto de tus Inversionistas | CONTRARIA | lector y verificador de acuerdo |
| `cumplimiento_vs_violacion` | Reencuadra la Violación como Aprendizaje | Reencuadra la Violación como Norma Local | DISTINTA | lector y verificador de acuerdo |
| `costo_de_oportunidad` | Piensa lo que Dejas Ganar | Calcula lo que Dejas de Ganar | CONTRARIA | arbitro |
| `acceptance_control` | Controla la Aceptación, No Muestrees | Adapta tu Muestreo de Aceptación Continuamente | CONTRARIA | lector y verificador de acuerdo |
| `six_sigma_dmaic` | Mejora en Cinco Pasos | Resuelve Problemas Crónicos por Fases | DISTINTA | lector y verificador de acuerdo |
| `mitigacion_riesgos_ambientales` | Reduce tu Responsabilidad Extendida | Mitiga Riesgos Ambientales de tu Cadena | CONTRARIA | lector y verificador de acuerdo |
| `rol_de_mandos_medios_y_supervisores` | Empodera a tus Mandos Medios | Lidera la Calidad sin Mandar | CONTRARIA | arbitro |
| `tablero_control_scorecard` | Informa a tu Alta Dirección | Arma tu Tablero de Calidad | DISTINTA | lector y verificador de acuerdo |
| `diseno_mas_alla_del_individuo` | Piensa en Grupos No Individuos | Diseña Más Allá del Individuo | CONTRARIA | arbitro |
| `clausula_personas_clave_banker` | Protege tu Persona Clave Contratada | Exige Cláusula de Banquero Clave | DISTINTA | lector y verificador de acuerdo |
| `autoacusacion_antes_mala_noticia` | Anticipa la queja antes de darla | Acúsate Antes de Dar Malas Noticias | CONTRARIA | lector y verificador de acuerdo |
| `evaluacion_vp_ventas` | Evalúa a tu Futuro Vendedor | Evalúa a tu Director de Ventas | DISTINTA | lector y verificador de acuerdo |
| `founders_activities_clause` | Exige Dedicación Total a Fundadores | Evalúa la Cláusula de Dedicación Exclusiva | CONTRARIA | lector y verificador de acuerdo |
| `sintesis_hipotesis_modelo_negocio` | Valida tus Hipótesis en Conjunto | Revisa tus Hipótesis en Conjunto | DISTINTA | lector y verificador de acuerdo |
| `patent_cooperation_treaty` | Patenta tu Invento Globalmente | Presenta una Solicitud Internacional de Patente | CONTRARIA | lector y verificador de acuerdo |
| `ecuacion_de_valor_cliente` | Equilibra Esfuerzo y Valor Percibido | Aumenta el Valor Antes del Costo | CONTRARIA | lector y verificador de acuerdo |
| `transicion_post_sucesion` | Gestiona tu Salida como Fundador | Maneja tu Rol Tras la Sucesión | CONTRARIA | lector y verificador de acuerdo |
| `relacion_doble_reporte_dotted_line` | Combina Reporte Funcional y Técnico | Combina Reporte Técnico y Operativo | DISTINTA | lector y verificador de acuerdo |
| `derecho_rechazo_trabajo_peligroso` | Puedes Rechazar Trabajo Peligroso | Respeta el Rechazo al Trabajo Peligroso | CONTRARIA | lector y verificador de acuerdo |
| `rol_lider_equipo_calidad` | Elige tu Líder de Equipo | Define el Rol del Líder | DISTINTA | lector y verificador de acuerdo |
| `right_of_first_refusal_pro_rata` | Protege tu Derecho Pro Rata | Conoce el Derecho Preferente del Inversionista | CONTRARIA | lector y verificador de acuerdo |
| `decision_segunda_unidad_operativa` | Decide Abrir una Segunda Unidad | Decide si Abrir una Segunda Unidad | CONTRARIA | arbitro |
| `cumplimiento_acuerdos_comerciales_tanc` | Vigila el Cumplimiento Comercial | Pide Ayuda ante Barreras Comerciales | CONTRARIA | lector y verificador de acuerdo |
| `rol_green_belt_six_sigma` | Forma a tus Colaboradores Clave | Colabora y Lidera Proyectos de Mejora | DISTINTA | lector y verificador de acuerdo |
| `cultura_de_buena_empresa` | Construye una Gran Empresa | Construye una Buena Empresa | DISTINTA | lector y verificador de acuerdo |
| `precision_exactitud_sensores` | Calibra Precisión y Exactitud | Distingue Precisión de Exactitud | CONTRARIA | arbitro |
| `programa_make_certain_3` | Certifica tu Trabajo Administrativo | Prevén Errores en el Trabajo Administrativo | DISTINTA | arbitro |
| `lenguajes_jerarquia_organizacional` | Habla el Idioma de tu Equipo | Traduce tu Operación a Dinero | DISTINTA | lector y verificador de acuerdo |
| `diseno_para_ia_centrada_en_humano` | Humaniza tu Diseño con IA | Diseña una IA Más Humana | CONTRARIA | lector y verificador de acuerdo |
| `escenarios_de_evolucion_de_la_ia` | Anticipa Hasta Dónde Llegará la IA | Prepara Varios Escenarios de la IA | CONTRARIA | lector y verificador de acuerdo |
| `seminario_de_exito_para_gerencia` | Muestra Éxitos ante la Gerencia | Comparte Testimonios con Quienes Dudan | DISTINTA | lector y verificador de acuerdo |
| `economia_circular_de_la_imaginacion` | Regenera también tus Ideas | Diseña para Regenerar la Imaginación | DISTINTA | lector y verificador de acuerdo |
| `consejo_de_calidad_2` | Autogestiona tu Consejo de Calidad | Crea un Consejo de Calidad Autónomo | CONTRARIA | lector y verificador de acuerdo |
| `acuerdo_de_co_venta_y_votacion` | Protege tu Venta de Acciones | Pacta Venta Conjunta y Voto Coordinado | CONTRARIA | lector y verificador de acuerdo |
| `stage5_launch` | Instala y Opera tu Equipo | Lanza tu Producto al Mercado Completo | DISTINTA | lector y verificador de acuerdo |

El motivo y la cita de cada una estan en `CORRECCIONES_PASADA_ETIQUETAS.json` y en `_motivos` de la lista.
