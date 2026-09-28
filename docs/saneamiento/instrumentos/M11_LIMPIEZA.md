# INSTRUMENTO M11: LIMPIEZA DEL PACK DEL MUNDO 11 ANTES DE INTEGRARLO

Decisiones del fundador del 28 sep 2026 (integracion del mundo 11, paso 3). Lo leen el REDACTOR, el VERIFICADOR
CIEGO y el ARBITRO. Nada de esto toca `dataset/`: se escribe un fichero de resultados por lote y, con lo verificado,
las tandas de correcciones declaradas (`scripts/fidelidad/aplicar_correcciones.py --nodos`).

## Lo que ve el cliente, y por eso se limpia

El texto de cada nodo llega a la IA o a la pantalla: `titulo_concepto`, `resumen_teorico`, cada elemento de
`pasos_accionables`, `entregable_esperado` y cada elemento de `condiciones_activacion`
(`docs/fidelidad/CAMPOS_QUE_LLEGAN.md`). `notas_extraccion` es INTERNO: se lee como evidencia, jamas se copia.

## 1. El resumen nuevo (veredicto RESUMEN)

El `resumen_teorico` de la forja NO es un resumen: es la nota de extraccion (unidad de origen, rutas, lineas,
razonamiento del extractor). Se escribe uno NUEVO:

- **Que dice:** que sostiene el procedimiento y por que funciona. Es la idea que hace valer los pasos, no una lista
  de los pasos ni la historia de donde salio.
- **Largo:** de 400 a 600 caracteres, contados con espacios (el aplicador rechaza fuera de ese rango). Como los del
  catalogo (mediana 447).
- **De donde sale:** SOLO de los pasos del propio nodo y de las lineas del libro que la nota cita. Los libros estan en
  `C:\Users\AlexDesk\Documents\forja-lectura\fuentes\<libro>\cap_XX.md`. Si la nota no dice fichero o lineas,
  buscalas en el libro del nodo (su carpeta va en la entrada) con frases de los pasos o de las citas en ingles.
- **Evidencia obligatoria:** `fichero` (ruta desde `fuentes/`, por ejemplo `fuentes/scott_radical_candor/cap_13.md`)
  y `lineas` ("187-198"). Si una parte del resumen sale de los pasos y no del libro, las lineas son las del pasaje
  del que salen esos pasos.
- **Prohibido:** una cifra, un plazo o una norma que no este en esas lineas; la voz de libro; el ingles; autores y
  titulos de libros; guiones largos o medios.

## 2. Los demas textos de cara (titulo, pasos, entregable, condiciones)

Se devuelve el texto nuevo de CADA elemento que tenga que cambiar, sin cambiar el sentido:

- **Voz de libro (VOZ):** fuera toda referencia al libro, al texto, al autor o la autora, al capitulo, al recuadro,
  a "el caso del texto", "lo que el libro nombra", "el texto lo dice asi", "segun cuenta", y similares, en cualquier
  forma. El contenido se afirma directamente: "las tres preguntas que el libro nombra" pasa a "estas tres preguntas"
  o se nombran.
- **Ingles (VOZ):** toda cita en ingles se REESCRIBE en espanol con palabras propias, nunca traducida literalmente;
  si la cita solo repetia lo que el paso ya dice en espanol, sale entera. Los nombres de conceptos en ingles del libro
  (Primary Aim, Benchmarks, Chief in Charge, off-site) pasan a un nombre espanol claro.
- **Autores y titulos (ATRIBUCION, o VOZ si va con voz de libro):** fuera los autores de los libros (Kim Scott, Julie
  Zhuo, Geoff Smart, Randy Street, Andrew Grove, Michael Gerber, David Marquet) y los titulos de los libros. Los
  personajes de las anecdotas del libro no se nombran como fuente: el ejemplo se cuenta sin atribuirlo ("en un
  submarino", "un directivo"), conservando lo que ensena.
- **Cifras (CIFRA):** la cifra de MERCADO (salarios, precios, honorarios en dolares) sale, con "pregunta lo que
  cuesta en tu mercado" si hace falta; la que ES NORMA (un umbral o un plazo que fija una ley) se queda y se reporta en
  `cifras_de_norma` para su nodo-frontera (docs/POLITICA_MARCO_PAIS.md, regla de la cifra).
- **Ortografia (ORTOGRAFIA):** la forja escribe SIN tildes ("segun", "reunion", "companeros"). Todo texto nuevo va
  con su ortografia completa: tildes, enie, signos de apertura. Si un elemento solo cambia por esto, su veredicto es
  ORTOGRAFIA.
- **Condiciones (COHERENCIA):** cada condicion se lee contra el contenido del nodo; si no le corresponde, se reescribe
  desde el propio nodo. Si el nodo trata la ley de un pais, la condicion de pais va primero (clase C).
- **Voz de la casa en todo texto nuevo:** tu (nunca usted ni ustedes), frases llanas, sin guiones largos ni medios,
  puntos suspensivos con el caracter "…", sin jerga cruda (MVP, pivot, stakeholder).
- **No se inventa ni se quita contenido:** ningun paso nuevo, ninguna cifra nueva; lo unico que sale es voz de libro,
  ingles sobrante, autores, titulos y cifras de mercado.

Un mismo texto puede cambiar por varias razones: se declaran todas en `motivos` (voz_de_libro, ingles,
autor_o_titulo, cifra_de_mercado, ortografia, coherencia, voz_de_la_casa: vosotros o usted pasados a tu, que va
como VOZ), y el `veredicto` es el primero que aplique en este orden:
VOZ, ATRIBUCION, CIFRA, COHERENCIA, ORTOGRAFIA. Para VOZ, ATRIBUCION y CIFRA, `fragmentos` lista los trozos EXACTOS
del texto viejo que salen (ninguno puede quedar en el nuevo).

## 3. Pais y vigencia (se reportan, no se escriben en el nodo)

- **Jurisdiccion:** si el nodo trata una ley, un organismo, un programa o una figura de un pais, `jurisdiccion` con
  `pais` (codigo, "US"), `clase` (A, B o C segun docs/POLITICA_MARCO_PAIS.md) y `motivo`. Decidido por el fundador:
  `evitar_preguntas_ilegales_entrevista` es clase B. Regla del empleo: contratar, pagar y despedir van como metodo.
- **Vigencia:** si el nodo depende de algo que caduca (norma, plazo legal, cifra con fecha, institucion), `vigencia`
  con `tipos` (norma, plazo_legal, cifra_datada, institucion) y `fragmentos` (texto NUEVO que la motiva).

## 4. Trampas

Algunos nodos de la entrada son TRAMPAS: copias de otros nodos con algo plantado que debe salir. El redactor no sabe
cuales son; los trata como todos. El verificador tambien recibe elementos trampa: textos nuevos con un fallo plantado
que debe marcar.

## 5. Formato de salida del REDACTOR (un fichero JSON por lote)

```json
{"lote": "NN", "nodos": [
  {"node_id": "...",
   "resumen": {"texto": "...", "fichero": "fuentes/<libro>/cap_XX.md", "lineas": "A-B"},
   "cambios": [
     {"campo": "titulo_concepto", "texto_nuevo": "...", "veredicto": "VOZ", "motivos": ["voz_de_libro", "ortografia"], "fragmentos": ["que el libro nombra"]},
     {"campo": "pasos_accionables", "indice": 0, "texto_nuevo": "...", "veredicto": "ORTOGRAFIA", "motivos": ["ortografia"]}
   ],
   "jurisdiccion": null, "vigencia": null, "cifras_de_norma": []}
]}
```

Todo elemento que no aparezca en `cambios` se da por correcto tal cual (sin voz de libro, sin ingles y con su
ortografia completa). Revisa CADA elemento: la forja escribe sin tildes, asi que casi todos cambian.

## 6. VERIFICADOR CIEGO y ARBITRO

El verificador recibe, por elemento: el texto viejo, el texto nuevo y las lineas del libro (para el resumen). No ve
el razonamiento del redactor. Marca OK o FALLA con su motivo: cambio de sentido; cifra, plazo o norma que no esta en
las lineas o en el texto viejo; voz de libro, ingles, autor o titulo que quedo; falta de ortografia; resumen fuera de
400 a 600 caracteres o que no dice que sostiene el procedimiento; voz de la casa rota. En un FALLA propone el texto
corregido. El arbitro lee viejo, nuevo, la objecion y las lineas, y decide el texto final.
