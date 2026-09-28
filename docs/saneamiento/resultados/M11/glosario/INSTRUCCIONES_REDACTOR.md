# REDACTOR DEL PASE DE GLOSARIO (limpieza M11, 28 sep 2026)

Lee ENTERO `glosario/DECISIONES.md`: es la ley de este pase. Tu entrada (`glosario/entrada_X.json`) trae textos YA
LIMPIOS del pack del mundo 11 que contienen algun termino de la tabla (campo `terminos` dice cual se detecto, por
patron: puede ser un falso positivo).

Por cada texto decide:
- si el termino detectado NO es el caso de la tabla (por ejemplo "lista" = enumeracion; "sola" referida a una cosa; un
  femenino que es de una ANECDOTA en tercera persona, "una directiva... ella"; "el Pozo" ya explicado en el nodo),
  no lo cambias;
- si SI es el caso, escribes el texto nuevo con el cambio MINIMO que pide la tabla, sin tocar nada mas, sin cambiar el
  sentido, en espanol con tildes, en tu (nunca usted, ustedes ni vosotros), sin guiones largos o medios ni tres puntos.
  Prohibido introducir "se espera", "se recomienda", "se debe", "se traduce", "su equipo" o "el equipo de".
  Un `resumen_teorico` sigue midiendo de 400 a 600 caracteres (cuentalos con un script).
- "El Pozo": mira el nodo entero (lo tienes en `C:\Users\AlexDesk\Documents\m11-trabajo\copia\primer_equipo\nodos\<node_id>.json`);
  si ningun campo explica que es, en su PRIMER uso del nodo pon "el Pozo (el bache de desanimo)" con tildes ("desánimo").

Salida `glosario/propuestas_X.json` en UTF-8:
{"grupo": "X", "cambios": [{"node_id": "...", "campo": "...", "indice": null|N, "texto_anterior": "<exacto>",
  "texto_nuevo": "...", "veredicto": "VOZ", "motivos": ["voz_de_la_casa"|"ingles"|"coherencia"],
  "fragmentos": ["<trozos EXACTOS del texto anterior que salen y no quedan en el nuevo>"], "termino": "..."}],
 "sin_cambio": [{"node_id": "...", "campo": "...", "indice": null|N, "por_que": "..."}]}
Cada elemento de la entrada va en `cambios` o en `sin_cambio` (compruebalo con un script). `texto_anterior` es el texto
de la entrada, exacto. Si en un mismo texto hay dos terminos, un solo cambio con los dos.
