-- my_idea_030_gestor_de_estados.sql
-- Gestor de estados por tarea (decisión del fundador, jul 2026): el usuario
-- elige el estado explícitamente, y gana soberanía de "no aplica" con motivo.
--
-- Dos cambios sobre checklist_items.estado:
--  1. RENOMBRE 'a_medias' -> 'en_proceso'. Se migra el valor interno (no solo
--     la etiqueta de cara) porque ya estamos tocando el CHECK y dejar dos
--     vocabularios (interno 'a_medias', visible "en proceso") es una trampa
--     para quien lea el código después. Barato: un UPDATE + swap del CHECK.
--  2. NUEVO estado 'no_aplica': la tarea no corre para esta idea. NO es un
--     fracaso ni un pendiente eterno: sale del denominador del avance y jamás
--     cuenta como tardía. Su porqué (opcional) vive en no_aplica_motivo.
--
-- El CHECK va como ADD CONSTRAINT nombrado (igual que 015/018): así lo parsea
-- dbContract.test.ts y así se puede relajar por nombre a futuro. La bitácora
-- del cambio (estado_anterior + motivo) la escribe la app en project_bitacora
-- (migration 018), no esta migración.

-- Swap del CHECK: primero se suelta, luego se migra el valor viejo, luego se
-- vuelve a atar con el conjunto nuevo. En este orden, ninguna fila viola el
-- constraint en ningún momento.
ALTER TABLE public.checklist_items DROP CONSTRAINT checklist_items_estado_check;

UPDATE public.checklist_items SET estado = 'en_proceso' WHERE estado = 'a_medias';

ALTER TABLE public.checklist_items
  ADD CONSTRAINT checklist_items_estado_check
    CHECK (estado IN ('pendiente', 'empezado', 'en_proceso', 'hecho', 'no_aplica'));

-- El porqué de "no aplica", en las palabras del usuario. Opcional (null = la
-- retiró sin explicar). Solo tiene sentido con estado 'no_aplica'; al volver a
-- otro estado la app lo limpia, pero el evento queda en la bitácora.
ALTER TABLE public.checklist_items ADD COLUMN no_aplica_motivo text;
