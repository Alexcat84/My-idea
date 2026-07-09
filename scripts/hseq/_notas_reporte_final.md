# Notas acumuladas para el reporte final de hseq-sanitized-v1

(Archivo de trabajo: se consolida en el reporte del tag y luego puede
borrarse o archivarse.)

## Lecciones del corpus (para registrar en el reporte final)

1. **La similitud de título es señal poco confiable en corpus
   mono-disciplina.** El core (13 libros de disciplinas distintas) casi no
   tenía choques de título entre conceptos diferentes; estos packs (3-5
   libros de LA MISMA disciplina por dominio) chocan de nombre
   constantemente entre conceptos legítimamente distintos (ej. 5 nodos
   "Acción Correctiva" con similitud de contenido 0.005-0.104: Crosby-
   definición, Crosby-paso-6 y Juran-esporádico-vs-crónico). La revisión
   de dedup se hizo leyendo resumen_teorico/pasos_accionables, no por
   nombre — 15/132 grupos fusionados (11%), el resto eran colisiones de
   nombre entre conceptos reales.

2. **Lección de pipeline (pendiente de implementar, NO ejecutada en esta
   fase):** pipeline_dominio.py necesita, para cualquier libro futuro, un
   diseño de DOS pasadas: pasada 1 extrae todos los nodos del libro;
   pasada 2 teje aristas viendo el catálogo real de ids ya extraídos. El
   core nació con ~25% de referencias rotas por esta misma ceguera
   (generación por chunks sin estado: el modelo nombra conceptos vecinos
   plausibles en vez de referenciar nodos que vio nacer); estos dominios
   nacieron con ~8% porque el modelo mejoró, pero la cura estructural es
   la segunda pasada, no un modelo más listo.

3. **El re-match semántico (paso 3b) recuperó mucho más de lo estimado.**
   De 191 fantasmas únicos (254 referencias podadas por paso 3):
   86 recuperados automáticos (score >= 0.70), 78 recuperados por revisión
   de significado (banda 0.55-0.70: 6+16+56 por dominio), 27 podados
   definitivos (12 rechazados en revisión + 15 bajo umbral). Tasa de
   recuperación: 86% de los fantasmas — muy por encima del 25-50%
   estimado, porque el corpus mono-disciplina SÍ contenía la mayoría de
   los conceptos troncales bajo otro nombre (mismo fenómeno que hizo
   poco confiable el título en dedup, jugando esta vez a favor).
   Nota: el top-3 del embedding también falló varias veces (ej.
   'medicion_impacto_ambiental' no listó a 'metricas_impacto_ambiental');
   ~24 aprobaciones fueron overrides encontrados por búsqueda dirigida
   de títulos + lectura de contenido.

## Números por checkpoint (para la tabla del reporte)

- Censo inicial (post paso 0): 1557 nodos (314 env / 336 hs / 907 q).
- Paso 1 ASCII: 14 ids transliterados (6/2/6), 25 nodos con refs reescritas.
- Paso 2 dedup: 132 grupos candidatos, 15 aprobados, 17 nodos absorbidos.
  Conteos post-fusión: 312/332/896 = 1540.
- Paso 2b cosmético: 8 keepers renombrados a base limpia.
- Paso 3 reparación de cadenas: 26 reparadas, 254 podadas (5.14%/8.08%/7.98%
  de las refs originales — escalado al usuario por superar el umbral 3%).
- Paso 3b re-match semántico: 191 fantasmas únicos → 86 auto + 78 revisión
  + 27 poda definitiva.
- Paso 4 simetrización: 632 nodos completados (114/143/375).
- Estado post-checkpoint 4: 0 refs rotas, 0 aristas asimétricas;
  784/996/2758 refs por dominio.
