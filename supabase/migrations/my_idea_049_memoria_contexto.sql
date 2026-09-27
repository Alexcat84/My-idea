-- my_idea_049_memoria_contexto.sql -- la MEMORIA DE CONTEXTO del proyecto (decision del fundador, 28 sep 2026,
-- docs/REGLAS_DE_LA_CASA.md, principio 1: el contexto completo del usuario viaja siempre y se guarda en la base).
--
-- projects.memoria guarda, en JSON:
--   * la FICHA DE CONTEXTO estructurada de la persona (papel, si tiene jefe, equipo, sector, etapa, prioridad
--     declarada y frases textuales), que el interprete actualiza en cada turno;
--   * el HILO: cada pregunta y cada respuesta de todas las sesiones del proyecto, en orden, solo añadiendo.
-- La forma la define web/lib/engine/memoria.ts. '{}' se lee como memoria vacia (proyectos anteriores a la 049).
--
-- Sin politicas nuevas: la columna vive en projects y hereda su RLS (cada quien ve y escribe solo sus proyectos).
-- El bloque 049 de my_idea_check_migraciones.sql la confirma ANTES (MISSING) y DESPUES (OK).

ALTER TABLE public.projects
  ADD COLUMN IF NOT EXISTS memoria jsonb NOT NULL DEFAULT '{}'::jsonb;
