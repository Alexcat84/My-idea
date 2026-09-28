# SEGUNDO PASE DE LA LIMPIEZA M11 (28 sep 2026): solo lo que fallo en la muestra ciega

Lee ENTERAS `C:\Users\AlexDesk\Documents\m11-trabajo\auditoria\INSTRUCCIONES.md` (la vara, los tipos, el formato de
salida y lo que NO es defecto; el leismo de persona masculina esta admitido). Este segundo pase existe porque la
muestra ciega final encontro, en 50 nodos ya auditados, 23 defectos confirmados de estos tipos (ninguna invencion ni
contrario). Busca SOBRE TODO estos tipos, y con mas cuidado en los PASOS, que es donde mas se escapan:

- `matiz`: el pasaje del libro dice can, may, might, could, often, usually, most, some, probably, likely, unlikely,
  tend to, possible... y el texto lo afirma sin matiz. Ejemplos reales de la muestra: "una perspectiva de fuera te
  ayuda" (el libro: "can help"); "los jefes casi siempre esperan demasiado" (el libro: "most managers... I'd say");
  "la objecion habitual... los jefes son reacios" (el libro: "bosses can be reluctant"); "en junio ya se ve que no
  llegara" (el libro: "unlikely to be ready"); "las tres explicaciones que se dara" (el libro: "three possible
  explanations"). Y la experiencia de una persona ("I've found", "in my experience") contada como regla.
- `calco`: "prospecto" (cliente potencial), "la vista que tienes de ti mismo" (la vision), "optimizando su interes"
  (persiguiendo), "interes estrecho", "ni mas ni menos de lo que se lo dejarias" (any more than), "escalada" (escalate),
  "condicion" por estado de salud, "tienes un bebe feo" (ugly baby), y cualquier giro ingles traducido palabra a palabra.
- `coherencia`: sujeto o posesivo que cambia de persona ("tienes un gran banquillo" cuando el banquillo es de otro),
  referente sin antecedente ("ahi", "el suboficial" ambiguo, "la gran empresa" sin presentar), una frase que dice mas de
  lo que el libro plantea como pregunta.
- `regionalismo`, `voz`, `ortografia` como en las instrucciones.

Si ves una invencion o un contrario, marcalos tambien. No inventes defectos: cita el texto exacto y la linea del libro.
Tu entrada y tu salida son las que te indiquen; el formato de salida es el de `auditoria/INSTRUCCIONES.md`.
