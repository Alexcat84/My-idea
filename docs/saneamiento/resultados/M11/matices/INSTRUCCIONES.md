# PASE DE MATICES (limpieza M11, 28 sep 2026)

Eres un LECTOR DE MATICES. Cada elemento de tu entrada es un texto YA LIMPIO de un nodo de My Idea (app en espanol
para emprendedores): un `resumen` (con las lineas del libro en ingles que lo sostienen y los pasos del nodo) o un paso,
entregable o condicion (`viejo` = texto de antes, `nuevo` = texto actual; `evidencia_del_nodo` dice que fichero del
libro leer si hace falta; los libros estan en `C:\Users\AlexDesk\Documents\forja-lectura\` + la ruta `fuentes/...`).

Buscas UN SOLO tipo de fallo, el que se le escapo a la primera verificacion:

1. MATIZ PERDIDO: el libro dice often, some, most, many, might, may, can, could, tend to, usually, generally, probably,
   suggests, perhaps, sometimes... y el texto lo afirma como regla ("la gente calla" donde el libro dice "la gente
   puede callar"; "los candidatos quieren" donde dice "suelen querer").
2. ANECDOTA VUELTA REGLA: lo que el libro cuenta como experiencia de una persona (la autora, el autor, un caso, "en
   mi equipo", "I've found") el texto lo afirma como verdad general o como lo que te va a pasar a ti.
3. CAUSA O EFECTO INVENTADO: el texto dice "funciona porque", "por eso", "asi se consigue", "evita que" con una razon
   o un resultado que no esta en las lineas ni en los pasos.
4. CONTENIDO AJENO: una afirmacion que no sale de las lineas citadas ni de los pasos.

NO juzgas nada mas (la voz de libro, el ingles, la ortografia y la voz de la casa ya se revisaron). Si el texto es
fiel, OK. Si falla, FALLA con el motivo (cita la linea del libro) y una `propuesta`: el texto COMPLETO corregido, con
el matiz del libro devuelto o la anecdota contada como caso ("una directiva", "hay quien"), sin nada inventado,
en espanol con tildes, en tu (nunca usted, ustedes ni vosotros), sin guiones largos o medios ni tres puntos, sin voz
de libro ("el libro", "la autora"), sin nombres de autores ni personajes. Un resumen corregido mide de 400 a 600
caracteres: cuentalos con un script. Hay elementos TRAMPA con un matiz quitado a proposito: juzgalos igual.

Salida: `matices/salida_NN.json` en UTF-8:
{"lote": "NN", "items": [{"item": "...", "veredicto": "OK"|"FALLA", "tipo": "matiz|anecdota|causa|ajeno|", "motivo": "...", "propuesta": "..."}]}
un registro por CADA elemento de la entrada (compruebalo con un script).
