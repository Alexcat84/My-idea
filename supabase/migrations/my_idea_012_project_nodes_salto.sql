-- ============================================================================
-- MY IDEA · Migration 012_project_nodes_salto
-- Bug real encontrado al verificar el Hotfix v2.2.1 en vivo (vuelo.ts fase 2):
-- AMBOS motores usan "salto" como un modo valido de nodo desde la Fase 2.8
-- (saltos semanticos) -- Python (prototipo_motor.py:2385, modo = "salto")
-- lo escribe identico a la web (recorrido.ts) cada vez que corre sin
-- --offline contra el mismo proyecto de Supabase, no solo el puerto web.
-- project_nodes_tipo_check (migration 001_init) nunca se actualizo para
-- permitirlo -- cualquier sesion con un salto real revienta con 23514 al
-- ensamblar el plan (registrar_nodos / registrarNodos), perdiendo la
-- sesion completa en ese punto.
--
-- Nota (Hotfix v2.2.2, verificada por auditoria cruzada): tipo='salto' es
-- semanticamente un subtipo de 'conversado' -- llegada por salto semantico
-- con una pregunta hecha en el destino, no una categoria de cobertura
-- distinta. Se mantiene como valor propio (en vez de colapsarlo a
-- 'conversado') porque asi corren ambos motores hoy en produccion real;
-- separar "modo de llegada" de "cobertura" queda pendiente como decision
-- de esquema v2 si algun consumidor futuro lo necesita con datos reales
-- que lo justifiquen, no como cambio especulativo.
-- ============================================================================

ALTER TABLE public.project_nodes DROP CONSTRAINT project_nodes_tipo_check;
ALTER TABLE public.project_nodes ADD CONSTRAINT project_nodes_tipo_check
  CHECK (tipo IN ('conversado', 'silencioso', 'cosechado', 'salto'));
