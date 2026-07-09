-- ============================================================================
-- MY IDEA · Migration 012_project_nodes_salto
-- Bug real encontrado al verificar el Hotfix v2.2.1 en vivo (vuelo.ts fase 2):
-- el motor (Python, engine/prototipo_motor.py, y su espejo web
-- lib/engine/recorrido.ts) usa "salto" como un modo valido de nodo desde la
-- Fase 2.8 (saltos semanticos), pero project_nodes_tipo_check (migration
-- 001_init) nunca se actualizo para permitirlo -- cualquier sesion con un
-- salto real revienta con 23514 al ensamblar el plan (registrar_nodos /
-- registrarNodos), perdiendo la sesion completa en ese punto.
-- ============================================================================

ALTER TABLE public.project_nodes DROP CONSTRAINT project_nodes_tipo_check;
ALTER TABLE public.project_nodes ADD CONSTRAINT project_nodes_tipo_check
  CHECK (tipo IN ('conversado', 'silencioso', 'cosechado', 'salto'));
