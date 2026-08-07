# Plan de extracción — dos mundos nuevos (Compras / Entrega)

Plan de CC antes de tocar la API, según el protocolo de la casa. La vara de
esquema es `scripts/expansion/validar_esquema.py`, nunca este documento.

---

## 1. Lo que verifiqué del herramental (no supuesto: leído)

Ya existe un pipeline probado y no hay que inventarlo: `scripts/pipeline_libros.py`,
heredero de `scripts/pipeline_dominio.py`. Trae reanudación por `_progreso.json`,
reintentos con backoff, conteo de tokens reales y costo por corrida, e inyección
del `dominio` por código (no se le confía al modelo).

**Dos de las trampas viejas ya están cerradas ahí dentro:**

- **Los bloques de pensamiento no lo rompen.** `extract_nodes_from_chunk` recorre
  `response.content` buscando `type == "text"` en vez de agarrar `content[0]`.
- **El techo de 8K ya no aplica.** `MAX_TOKENS = 16000`, y el código detecta
  `stop_reason == "max_tokens"` en vez de tragarse una respuesta cortada.

## 2. Las trampas que SIGUEN vivas (esto es lo que hay que arreglar antes de enviar)

**T1 — El reintento por corte no sube el techo.** Cuando la respuesta se corta,
`pipeline_libros.py` hace `continue` con el mismo `MAX_TOKENS`. Reintenta tres
veces el mismo chunk contra el mismo techo, se corta idéntico las tres, y el
chunk se pierde. El reintento no puede repetir la condición que causó el fallo.
→ *Arreglo:* el techo ESCALA por intento (16k → 32k → 64k) y, si aún se corta,
el lote se PARTE en dos y cada mitad se reenvía. `max_tokens` es solo un techo:
no se paga por lo que no se genera.

**T2 — El prompt de esquema es más flaco que el SOP.** `NODE_SCHEMA_PROMPT` pide
la forma correcta (sin `familia`, con `entregable_esperado`, 4 fases) pero no
pide nada de lo que hace el nodo BUENO:
- no fija las 80-150 palabras del `resumen_teorico`;
- **no prohíbe copiar pasajes** (y las fuentes son libros con copyright);
- no prohíbe los guiones largos, que la casa tiene vetados;
- no da la regla de tono (una persona sola, sin equipo ni comité);
- no pide `etiqueta_arbol`;
- pide `node_ids` en `nodos_previos/siguientes`, cuando el SOP manda **títulos**
  textuales. El precedente real le da la razón al SOP: en risk_management,
  `metadata/aristas_reparadas.json` está lleno de títulos resueltos a ids en la
  segunda pasada. Si el modelo emite ids inventados, esa reparación no tiene de
  dónde agarrarse.
→ *Arreglo:* un prompt de esquema reconciliado con el SOP, en un solo sitio.

**T3 — El inventario de ids está viejo.** `scripts/ids_existentes.txt` tiene
3.687 ids del 2026-07-14; hoy hay 3.742. Está ciego a 55 (los de
risk_management). Chequear colisiones contra una lista vieja es no chequearlas.
→ *Arreglo:* regenerarlo antes de arrancar y dejarlo como paso 0 del script.

**T4 — La brecha no se hornea sola.** Lección ya registrada: `integrar_packs.py`
**no** produce `brecha_semillas` ni `packs_entry_seeds`. Si no se hornean a mano
por pack, la brecha nunca dispara y el mundo queda mudo. No es parte de la
extracción, pero va escrito aquí para que no se olvide en la integración.

**T5 — Las fuentes no están donde el pipeline mira.** El pipeline descubre libros
en `books/<grupo>/`; las fuentes viven en `txt/Supply chain` y `txt/Procurenment`,
y no hay grupo para estos dos mundos.
→ *Arreglo:* el extractor nuevo lee las fuentes **donde viven** (`txt/`), con
un mapa explícito de qué archivo alimenta a qué mundo. No se espejan a `books/`:
duplicar 1,4 MB de texto sería crear dos copias que se separan. Decisión mía, no
gasta una pregunta.

**T6 — Nada corre en segundo plano.** Un proceso de fondo muere con la sesión.
La corrida se hace en primer plano, por tandas, con reanudación.

---

## 3. La arquitectura de envío (el corazón de lo que pediste)

### Por qué NO una sola pasada a granel

El camino a granel (trocear todo el libro y pedirle nodos a cada trozo) es el que
produjo `quality` con **896 nodos** y `health_safety` con **332**. El camino del
SOP (índice primero, aprobación, luego nodos anclados) produjo `risk_management`
con **55**, y es el que entró limpio en la v1.4 con sus puentes curados.

El costo de la API no es el problema (el corpus entero son ~239.000 palabras,
unos $5 a granel). El costo es la limpieza posterior y un mundo inflado de
conceptos repetidos.

### Las dos etapas

**Etapa 1 — el índice (barata, sin nodos).**
Se trocea cada fuente (5.000 palabras, 500 de solape) y a cada trozo se le pide
SOLO una lista de conceptos: título, una línea de qué aporta, el ancla de sección,
y la fase propuesta. La salida por trozo es pequeña, así que no hay riesgo de
corte y el gasto es mínimo. Después consolido localmente (fusiono repetidos por
título) en **un índice temático por mundo, de 40-80 conceptos**.

Ese índice te lo entrego a ti. Tú cortas, fusionas y añades. **Ningún nodo nace
antes de tu visto.**

**Etapa 2 — los nodos (anclados al índice aprobado).**
Por cada concepto APROBADO se envía el concepto + el fragmento real de la fuente
donde vive. El modelo no puede inventar un nodo que no aprobaste, y ningún nodo
nace de memoria: nace del texto (regla 8 del SOP).

- **Tandas de 8 conceptos**, agrupadas por fase narrativa, para que el modelo vea
  a los hermanos y los `nodos_previos/siguientes` apunten a algo que existe.
- **Techo de 32.000 tokens**, con la escalera de T1 encima.
- **Reanudable por concepto**, no por trozo: si se corta, no se vuelve a pagar lo
  ya hecho.

### Las barandas locales (lo que se revisa sin preguntarle al modelo)

Entre tanda y tanda, y sin gastar un token:

1. `validar_esquema.py` sobre la carpeta (exit 0 o se para la corrida).
2. Colisión de `node_id` contra el inventario **recién regenerado**.
3. **Guarda de copyright**: se rechaza cualquier `resumen_teorico` que comparta
   una tirada de 12 palabras literales con el fragmento fuente. Es la diferencia
   entre destilar y copiar, y es comprobable sin criterio.
4. `resumen_teorico` entre 80 y 150 palabras.
5. Cero guiones largos (— –) en cualquier campo.
6. `etiqueta_arbol` de 6 palabras y 40 caracteres como máximo.

Lo que falle se aparta a un archivo de rechazos con su motivo. **No se degrada
en silencio**: si una tanda entera falla, la corrida se para y te lo digo.

---

## 4. Dudas ADJUDICADAS por el fundador (2026-08-07)

- **D1 — Voss: entra ACOTADO a proveedores.** El acote se aplica en la etapa 1:
  el índice solo admite conceptos anclables a una compra real (un proveedor, un
  precio, un plazo, un contrato de suministro). La negociación general (rehenes,
  salarios, ventas a clientes) se descarta antes de que nazca un solo nodo.
- **D2 — El inventario de Muller va a COMPRAS**, no a entrega.
- **D3 — Dos mundos: `compras` y `entrega`.**
- **D4 — 50-70 nodos por mundo** (recomendación aceptada por defecto).

El enunciado original de las dudas queda abajo, como registro.

---

## 4-bis. Las dudas, tal como se plantearon

**D1 — Voss.** `Rompe la barrera del no` son 87.000 palabras: el **36% de todo el
corpus** y casi la mitad de la carpeta de compras. Es un libro de negociación
(rehenes, ventas, salarios), no de compras. Si entra entero, inunda el mundo de
conceptos que no son de comprar.
*Mi recomendación:* entra **acotado a la negociación con proveedores** (el índice
solo admite conceptos que se puedan anclar a una compra real), o queda fuera de
esta ola y se decide después como potenciador propio.

**D2 — El inventario de Muller.** `MULLER_INVENTARIO_EXTRACTO_MINERIA.md` está en
la carpeta de compras, pero el inventario es la bisagra entre comprar y entregar.
¿A cuál de los dos mundos pertenece? *Mi recomendación:* al de **entrega**, donde
el usuario ya está moviendo cosas.

**D3 — Uno o dos mundos, y cómo se llaman.** Yo leo dos: **comprar/abastecerse**
y **entregar** (empaque, courier, última milla, fulfilment). Necesito el nombre
visible de cada uno y su slug de dominio, que es lo que se inyecta por código y
ya no se cambia sin migración.

**D4 — El tamaño de cada mundo.** risk_management tiene 55 nodos; exportacion,
158. *Mi recomendación:* apuntar a **50-70 por mundo**, que es lo que el índice
de 40-80 conceptos produce, y dejar crecer después.

---

## 5. Lo que arranco sin esperarte

Nada de esto depende de tus respuestas, así que va mientras decides:

1. Regenerar `scripts/ids_existentes.txt` (T3).
2. El extractor con las dos etapas y los envíos endurecidos (T1, T2).
3. Las barandas locales y sus pruebas, con la guarda de copyright.

Tus respuestas solo rellenan la tabla de grupos: qué fuente alimenta a qué mundo
y cómo se llama cada uno.
