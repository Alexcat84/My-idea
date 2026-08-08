# HSEQ: los 13 residuales leídos, con su clase

Leídos uno a uno. **Cero API gastada.**

## Dos cosas que no esperabas, y las pongo primero

**1. Los dos nodos que sospechabas NO están en la lista.** `diseño-de-departamento-de-seguridad`
y `Auftragssystem` no aparecen entre los 13: o se fundieron en la ronda anterior, o su
re-voz ya les quitó el hallazgo. No hay nada que deprecar por estructura.

**2. Encontré un duplicado que la fusión no agrupó:**

| nodo | cuerpo |
|---|---|
| **Plan de Control de Infecciones** `infection_control_plan` | *"Conjunto de practicas y procedimientos para prevenir o minimizar el contagio de agentes infecciosos en tu lugar de traba..."* |
| **Plan de Control de Infecciones en el Lugar de Trabajo** `plan_de_control_de_infecciones` | *"Se basa en evaluar los riesgos de tu negocio para identificar tareas con exposición a agentes infecciosos, y en poner en..."* |

Es el mismo plan contado dos veces. **Recomiendo fundirlos** antes de re-vozar
ninguno: la aritmética de siempre.

## REENCUADRE — la jerarquía vive en el ejemplo (10)

Ninguno de los 13 tiene el concepto ATADO a la estructura. En varios el cuerpo ya
habla a una persona sola y lo que quedó es una palabra suelta.

| nodo | por qué |
|---|---|
| **Autoinspección del Lugar de Trabajo** `autoinspeccion_lugar_de_trabajo` | 'junto con las personas con más experiencia en tu negocio' ya habla a una persona sola; el hallazgo es marginal |
| **Educación y Capacitación en Seguridad y Salud ** `capacitacion_educacion_seguridad` | 'a ti, a tus supervisores y a cada trabajador' → 'a ti y a quien trabaje contigo' |
| **Componentes de la Cultura de Seguridad** `cultura_de_seguridad_componentes` | 'tu compromiso y el de tu equipo' → 'el tuyo y el de quien trabaje contigo' |
| **Cultura Justa (Just Culture)** `cultura_justa_organizacional` | ya dice 'las personas que trabajan contigo': el hallazgo es de una sola palabra |
| **Programa de Ergonomía Laboral** `ergonomia_laboral` | el concepto es universal y no supone jerarquía; hallazgo marginal |
| **Recopilacion y Revision de Información sobre P** `identificacion_recopilacion_informacion_peligros` | reunir información sobre peligros no supone estructura alguna |
| **Liderazgo en Seguridad y Salud** `liderazgo_gerencial_seguridad` | ya dice 'Como responsable del emprendimiento': el título conserva la palabra gerencial y el cuerpo no |
| **Protección a quien denuncia irregularidades de** `programa_proteccion_denunciantes` | ya reencuadrado en la campaña anterior ('En muchos lugares la ley...'); hallazgo residual |
| **Seguridad en Escaleras Fijas (Stairways)** `escaleras_fijas_seguridad` | DATO LOCAL: 'cuatro o más escalones', altura y resistencia son la especificación de OSHA → método más 'averigua la norma de tu país' |
| **Revisión de Aplicabilidad de Estándares OSHA** `revision_aplicabilidad_estandares_osha` | DATO LOCAL pero el CONCEPTO es universal: revisar qué normas te aplican lo hace cualquiera → 'las de tu país' |

## DEPRECAR de selección (1)

**Recursos Educativos y de Capacitación de OSHA** `recursos_educativos_osha`

> *"OSHA pone a tu disposición, sin costo, un conjunto de materiales y programas para capacitar en seguridad a tu negocio y a las personas que trabajan contigo. Encuentras publicaciones, videos, páginas d..."*

**Es un catálogo de materiales de una agencia**, exactamente la misma clase que los
tres ya deprecados: describe un servicio de un gobierno, no un concepto.
Reencuadrarlo a *"busca los materiales de tu autoridad"* prometería un catálogo
gratuito que en muchos países no existe.

## Cuentas

| clase | nodos |
|---|---:|
| fundir (el par de infecciones) | 2 → 1 |
| reencuadrar | 10 |
| deprecar | 1 |
| **total** | **13** |

**Ninguno va a la ficha Primer Equipo**: ninguno tiene el concepto atado a una
estructura de equipo. Los dos que sospechabas ya no estaban.