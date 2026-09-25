-- my_idea_046_idioma_del_proyecto.sql — i18n F5 (DISENO §3.3 y §5; decisiones
-- del fundador D2 y del 25 sep 2026).
--
-- 1. projects.idioma: el idioma en que está ESCRITA la idea, detectado de su
--    texto original al crearla (lib/i18n/detectarIdioma.ts). Manda en lo que
--    escribe la IA y en los documentos de ese proyecto; la interfaz sigue la
--    preferencia del usuario (cookie). Código ISO 639-1, y puede estar FUERA de
--    los once (la IA responde en él; lo que escribe el código sin IA cae al
--    idioma de la interfaz). NULL = idea de antes de F5, que es español (la app
--    solo hablaba español): no hace falta rellenar las filas viejas.
--
-- 2. conteo_idiomas: el CONTEO ANÓNIMO de los idiomas en que se escriben las
--    ideas, para decidir qué idiomas vienen después (añadido del fundador, 25
--    sep 2026). Sin user_id, sin project_id y sin fecha fina: solo el mes, el
--    idioma de la idea, el de la interfaz y cuántas ideas. Una fila así no se
--    puede cruzar con ninguna persona ni con ninguna idea.
--
-- Solo service_role toca el conteo (RLS sin políticas + REVOKE), por la
-- función contar_idioma_de_idea, que suma uno de forma atómica.

ALTER TABLE public.projects ADD COLUMN IF NOT EXISTS idioma text;
ALTER TABLE public.projects DROP CONSTRAINT IF EXISTS projects_idioma_check;
ALTER TABLE public.projects
  ADD CONSTRAINT projects_idioma_check CHECK (idioma IS NULL OR idioma ~ '^[a-z]{2,3}$');

COMMENT ON COLUMN public.projects.idioma IS
  '046: idioma de la idea (ISO 639-1), detectado al crearla. NULL = anterior a F5, es decir español.';

CREATE TABLE IF NOT EXISTS public.conteo_idiomas (
  mes             date    NOT NULL,
  idioma_idea     text    NOT NULL,
  idioma_interfaz text    NOT NULL,
  ideas           integer NOT NULL DEFAULT 0,
  CONSTRAINT conteo_idiomas_pkey PRIMARY KEY (mes, idioma_idea, idioma_interfaz),
  CONSTRAINT conteo_idiomas_idea_check CHECK (idioma_idea ~ '^[a-z]{2,3}$'),
  CONSTRAINT conteo_idiomas_interfaz_check CHECK (idioma_interfaz ~ '^[a-z]{2,3}$'),
  CONSTRAINT conteo_idiomas_ideas_check CHECK (ideas >= 0)
);

ALTER TABLE public.conteo_idiomas ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON public.conteo_idiomas FROM anon, authenticated;

COMMENT ON TABLE public.conteo_idiomas IS
  '046: conteo anónimo de ideas por mes, idioma de la idea e idioma de la interfaz. Sin vínculo con personas ni ideas.';

-- Suma una idea al mes en curso. Un código inválido no cuenta (y no falla:
-- el conteo nunca debe tumbar la creación de una idea).
CREATE OR REPLACE FUNCTION public.contar_idioma_de_idea(
  p_idioma_idea     text,
  p_idioma_interfaz text
) RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
  IF p_idioma_idea IS NULL OR p_idioma_idea !~ '^[a-z]{2,3}$'
     OR p_idioma_interfaz IS NULL OR p_idioma_interfaz !~ '^[a-z]{2,3}$' THEN
    RETURN;
  END IF;
  INSERT INTO public.conteo_idiomas (mes, idioma_idea, idioma_interfaz, ideas)
  VALUES (date_trunc('month', now())::date, p_idioma_idea, p_idioma_interfaz, 1)
  ON CONFLICT (mes, idioma_idea, idioma_interfaz)
  DO UPDATE SET ideas = public.conteo_idiomas.ideas + 1;
END;
$$;

REVOKE EXECUTE ON FUNCTION public.contar_idioma_de_idea(text, text) FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION public.contar_idioma_de_idea(text, text) TO service_role;
