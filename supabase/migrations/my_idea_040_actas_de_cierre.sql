-- my_idea_040_actas_de_cierre.sql: el acta de cierre es una FOTO.
--
-- Por qué existe (AUD-09 M04, decisión del fundador del 25 sep 2026): el acta
-- ("Cerrado el X con N de M acciones", el estado de cada mundo) se recalculaba
-- en vivo. Marcar tres tareas más o correr un seguimiento después de cerrar
-- cambiaba lo que el acta decía del momento del cierre. Ahora, al cerrar, se
-- guarda una instantánea en este registro propio; volver a cerrar (tras
-- reabrir) guarda OTRA fila al lado, sin pisar la primera. La vista en vivo
-- deja de llamarse acta: se llama "estado actual".
--
-- Sirve a los dos cierres: el del proyecto (dominio 'core', ruta realizar) y
-- el de cada mundo (su dominio, ruta world/completar).
--
-- Sin UPDATE en la app: cada cierre es una fila nueva. La historia no se
-- reescribe.

CREATE TABLE public.project_actas (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id uuid NOT NULL REFERENCES public.projects(id) ON DELETE CASCADE,
  dominio text NOT NULL DEFAULT 'core',
  cerrada_at timestamptz NOT NULL,
  cierre_motivo text,
  instantanea jsonb NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);

COMMENT ON TABLE public.project_actas IS
  'Actas de cierre: la instantánea de lo que el acta muestra en el momento de cerrar (proyecto o mundo). Una fila por cierre; volver a cerrar agrega otra, nunca pisa.';

CREATE INDEX project_actas_project_dominio_idx ON public.project_actas (project_id, dominio, created_at DESC);

ALTER TABLE public.project_actas ENABLE ROW LEVEL SECURITY;

-- Espejo del patrón project_modos_own (032) / project_bitacora (018).
CREATE POLICY project_actas_own ON public.project_actas
  FOR ALL USING (EXISTS (SELECT 1 FROM public.projects p
                         WHERE p.id = project_id AND p.user_id = (SELECT auth.uid())));
