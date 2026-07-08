# Sistema de Gestión de Calidad (QMS) - Índice Maestro

Este documento sirve como índice central para toda la documentación técnica, estratégica y operativa del proyecto "La Telaraña del Emprendedor". Sigue una nomenclatura codificada para asegurar la escalabilidad: cada documento tiene un código (`STR-XX`, `PLN-XX`, `AUD-XX`, `PRO-XX`, `TST-XX`), vive en su carpeta de categoría, y aparece indexado aquí con un enlace relativo.

## Categoría 01: Estrategia y Visión (STR)
Documentos relacionados con los objetivos del proyecto, orígenes de la idea, propuesta de valor y referencias fundamentales.
- **[STR-01-Vision_and_Status](01_STRATEGY/STR-01-Vision_and_Status.md):** Visión del proyecto, origen, referencias APA 7 y estado actual.

## Categoría 02: Planificación y Roadmaps (PLN)
Documentos de planificación de fases, hitos, y estructuración de la ejecución.
- **[PLN-01-Implementation_Plan](02_PLANNING/PLN-01-Implementation_Plan.md):** Plan maestro detallado de las Fases 0 a 4 (Saneamiento, Filtros, Web App, Lanzamiento). Sigue vigente: Fase 3 (porte web) es el próximo hito real.

## Categoría 03: Arquitectura Técnica (TEC)
Especificaciones de software, diagramas de base de datos, stack tecnológico y despliegue (Carpeta reservada para futuros documentos).
*(Vacio temporalmente)*

## Categoría 04: Procesos y Operaciones (PRO)
Procedimientos operativos estándar (SOPs), manuales de uso interno de scripts (como la curación del grafo) y métricas de calidad.
- **[PRO-01-Reglas_de_Proceso](../AGENTS.md):** Reglas de proceso ganadas por incidentes reales (ej. calcular a mano antes de escribir un assert numérico). Vive en la raíz del repo (`AGENTS.md`) por convención de herramientas de agentes, no en esta carpeta.
- **[PRO-02-Manual_de_Comandos_CLI](04_PROCESSES/PRO-02-Manual_de_Comandos_CLI.md):** Cómo probar cada faceta del motor por tu cuenta — sesión nueva, `--continuar`, `--seguir`, `--gratis`, `--reporte`, `--offline`, combinaciones, y mantenimiento del dataset.
- **[PRO-03-Como_Documentar_de_Aqui_en_Adelante](04_PROCESSES/PRO-03-Como_Documentar_de_Aqui_en_Adelante.md):** Instrucciones fijas de cuándo y cómo crear cada tipo de documento (`STR`/`PLN`/`AUD`/`PRO`/`TST`), flujo estándar al cerrar cualquier trabajo, y checklist rápido. Leer esto antes de agregar cualquier documento nuevo al QMS.

## Categoría 05: Pruebas y Verificación (TST)
Registro de la suite de pruebas del motor: automatizadas (regresión, costo $0) y en vivo (API real, ya ejecutadas, evidencia en `examples/`).
- **[TST-01-Registro_de_Pruebas](05_TESTING/TST-01-Registro_de_Pruebas.md):** Las 13 pruebas del motor, codificadas (T01-T14), con qué verifica cada una, cómo correrla, y el link a su evidencia.

## Categoría AUD: Auditorías y Cierres de Fase
Registro de auditorías de calidad del dataset y del motor, propias y externas. En este proyecto, cada "cierre de fase" documenta tanto el trabajo ejecutado como la auditoría (propia o de Fable) que lo verificó — es, de facto, el registro de "planes ejecutados" del proyecto.
- **[AUD-01-Fase1_Cierre_y_Auditoria](audits/AUD-01-Fase1_Cierre_y_Auditoria.md):** Cierre de la Fase 1 (saneamiento de enlaces, normalización ASCII, fusión semántica) y auditoría independiente de Fable. Dataset congelado en el tag `dataset-v1.0.0`.
- **[AUD-02-Fase2_Cimientos_del_Motor_y_Motor_v1.0](audits/AUD-02-Fase2_Cimientos_del_Motor_y_Motor_v1.0.md):** Kickoff de Fase 2, Fases 2.1 a 2.5 (entrevista abierta, medidor de plan listo, recorrido silencioso, cosecha de vecindario, persistencia Supabase), y cierre de Motor v1.0 (cierre elegante, auto-corrección invisible). Tag `motor-v1.0`.
- **[AUD-03-Fase2_6_a_2_9_Cierre_Motor_v2_0](audits/AUD-03-Fase2_6_a_2_9_Cierre_Motor_v2_0.md):** Fases 2.6 a 2.9 — preguntas adaptadas por turno, escucha activa, navegación libre con brújula semántica, cierre funcional del motor. Tag `motor-v2.0`.
- **[AUD-04-Motor_v2_1_y_Hotfixes](audits/AUD-04-Motor_v2_1_y_Hotfixes.md):** Motor v2.1 (Reporte de Sostenibilidad), Hotfix v2.1.1 (semántica de sobredemanda, dominios), Hotfix v2.1.2 (bugs de una sesión en vivo sin guion: `--continuar`, migraciones Supabase), y el fix de seguridad del linter de Supabase. Tag `motor-v2.1`.
- **[AUD-05-Hotfix_v2_1_3_UnicodeDecodeError](audits/AUD-05-Hotfix_v2_1_3_UnicodeDecodeError.md):** Hotfix v2.1.3 — `UnicodeDecodeError` no atrapado al pegar texto con emojis, encontrado en la primera sesión en vivo del propio usuario con su idea real. `sys.stdin` reconfigurado a UTF-8, `leer_entrada()` atrapa el error con gracia, riesgo de fondo (pegado multilínea) documentado en `PRO-02`.
- **[AUD-06-Motor_v2_2_Tipo_de_Oferta_y_Guardian_GIGO](audits/AUD-06-Motor_v2_2_Tipo_de_Oferta_y_Guardian_GIGO.md):** Motor v2.2 — tipo de oferta y unidad de venta parametrizan la mini-entrevista de `--reporte` (física/servicio/digital), guardián GIGO (nunca narra conclusiones financieras absurdas), evidencia negativa registrada como restricción en el perfil, post-validador mecánico de coherencia etiqueta/contenido. Encontrado por auditoría de Fable sobre la primera sesión real del fundador (app de I Ching): el plan proponía como canal un segmento que el usuario había descartado con evidencia, y `--reporte` narró un margen de -2976.9% cuando el equilibrio real era 16 packs/mes. Tag `motor-v2.2`.

---

## Cómo se enlaza todo esto

- Cada fase/hotfix tiene su registro narrativo corto y "vivo" en `examples/README.md` (se actualiza con cada iteración) y su registro formal y cerrado aquí, en `docs/audits/AUD-XX` (se escribe una vez, al cierre).
- Cada prueba mencionada en un AUD-XX tiene su entrada en [TST-01](05_TESTING/TST-01-Registro_de_Pruebas.md), con el archivo ejecutable real (`engine/test_*.py` o `engine/live_tests/test_*.py`).
- Los comandos para reproducir cualquier faceta del sistema por tu cuenta están en [PRO-02](04_PROCESSES/PRO-02-Manual_de_Comandos_CLI.md).
- Las migraciones de base de datos (`supabase/migrations/my_idea_00X_*.sql`) se referencian desde el AUD-XX que las originó, no tienen categoría propia todavía (candidatas a `TEC` cuando esa carpeta deje de estar vacía).
- Los planes y reportes que el motor genera para usuarios reales (no para el equipo) viven en `engine/salidas/` (gitignored) — nunca en la raíz del repo.

*Nota: Este índice se actualizará conforme se agreguen nuevos documentos formales a las categorías respectivas. Antes de agregar uno, leer [PRO-03](04_PROCESSES/PRO-03-Como_Documentar_de_Aqui_en_Adelante.md).*
