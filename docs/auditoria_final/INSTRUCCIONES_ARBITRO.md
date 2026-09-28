# Arbitraje de la auditoría final: instrucciones del árbitro

Un lector ciego leyó un lote de conceptos (nodos) contra sus libros y marcó defectos. Tú eres el árbitro: relees cada
defecto marcado contra el nodo y contra el libro, y decides si se sostiene. Solo cuenta lo que tú confirmes.

## Qué puedes abrir

Solo esto:
- tu paquete: `C:/Users/AlexDesk/Documents/auditoria-final/arbitraje/arbitraje_XX.json`;
- estas instrucciones;
- las instrucciones del lector, para las definiciones de cada tipo:
  `C:/Users/AlexDesk/Documents/auditoria-final/INSTRUCCIONES_LECTOR.md`;
- la vara de fases: `C:/Users/AlexDesk/Documents/my-idea-main/docs/puente_forja/paso4/vara_fases.md`;
- el glosario: `C:/Users/AlexDesk/Documents/my-idea-main/docs/saneamiento/resultados/M11/glosario/DECISIONES.md`;
- los ficheros de libro de cada nodo.

Nada más: ni el resto del repositorio, ni otras carpetas, ni las respuestas de los lectores.

## Cómo arbitrar

Para cada defecto:
1. **Localízalo.** Busca el fragmento en el campo indicado del nodo, tal como está en tu paquete.
2. **Relee el libro** cuando el tipo lo pide (`contrario`, `invencion`, `matiz`). Ve a la evidencia que dio el lector y
   busca tú mismo si el libro dice otra cosa en otro sitio.
3. **Decide:**
   - `confirmado`: el defecto existe y es de ese tipo.
   - `reclasificado`: el defecto existe pero es de otro tipo. Pon el tipo correcto en `tipo_final`.
   - `rechazado`: no es un defecto. Por ejemplo, el libro sí lo dice, es una paráfrasis fiel, es uso corriente en
     español, o es un término técnico aceptado.
4. **Sé exigente en las dos direcciones.**
   - **Invención:** un paso práctico que hace operativo lo que el libro enseña, sin afirmar un hecho nuevo, no es
     invención. Una cifra, una causa o un efecto que el libro no da, sí lo es.
   - **Calco:** un término en inglés junto a su traducción no es calco. Un anglicismo que el español corriente ya usa
     ("marketing", "software", "email") tampoco lo es, salvo que el glosario lo decida de otro modo.
   - **Ortografía:** las tildes que faltan cuentan siempre.

## Lo que entregas

Un solo fichero JSON en `C:/Users/AlexDesk/Documents/auditoria-final/arbitraje/fallo_XX.json`, con esta forma exacta:

```json
{"lote": 7, "fallos": [
  {"node_id": "...", "n": 0, "veredicto": "confirmado", "tipo_final": "matiz", "razon": "una frase",
   "evidencia": {"fichero": "...", "lineas": "..."}}
]}
```

- Un fallo por cada defecto del paquete. `n` es el número del defecto dentro de su nodo, tal como viene en el paquete.
- `tipo_final` es el tipo del defecto si lo confirmas o lo reclasificas, y `null` si lo rechazas.
- No copies texto del libro de más de 15 palabras.
