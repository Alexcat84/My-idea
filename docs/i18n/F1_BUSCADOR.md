# F1: medición del buscador multilingüe

**Fecha:** 26 sep 2026. **Rama:** `i18n`. **Clave de Voyage:** cargada por el fundador para esta fase.

## Qué se midió

El grafo sigue en español: el índice semántico (`semantic_index.json`, Voyage `voyage-4-lite`) se
hizo con el texto en español de los nodos. La pregunta: una idea escrita en otro idioma, ¿recupera
los mismos nodos que su versión en español?

- **20 ideas de negocio**, la misma en los 11 idiomas (`web/scripts/i18n/ideas_medicion.json`).
- Cada una pasa por **`buscarAfines`**, la función de la app, con el grafo real y el dominio por
  defecto, y guarda los 10 primeros nodos sin umbral.
- Contra la versión en español se mide:
  - **solape:** cuántos de los 10 primeros coinciden (de 0 a 1);
  - **primero igual:** si coincide el nodo más afín;
  - **sobre el umbral:** cuántos candidatos pasan `MIN_SCORE_SALTO = 0,3`, el corte con el que la
    app decide qué saltos ofrecer en la entrevista.
- Scripts: `web/scripts/i18n/medicion_buscador.ts` (con `--remedio` para el remedio) y
  `techo_parafrasis.ts`. Datos crudos: `F1_resultados.json`, `F1_resultados_remedio.json`,
  `F1_techo_parafrasis.json`.

## Resultado por idioma

| idioma | solape | primero igual | sobre el umbral | con remedio: solape | con remedio: primero | con remedio: sobre el umbral |
|---|---|---|---|---|---|---|
| es (referencia) | 1,00 | 100 % | 7,35 | | | |
| en | 0,63 | 80 % | **2,80** | 0,77 | 75 % | 7,40 |
| pt | 0,71 | 80 % | 6,90 | 0,85 | 85 % | 7,10 |
| fr | 0,66 | 60 % | 4,40 | 0,81 | 75 % | 7,55 |
| de | 0,63 | 60 % | **2,95** | 0,79 | 80 % | 7,20 |
| it | 0,66 | 80 % | 5,20 | 0,78 | 85 % | 7,65 |
| ja | 0,57 | 45 % | 4,20 | 0,72 | 60 % | 7,35 |
| zh | 0,57 | 65 % | 4,35 | 0,71 | 65 % | 7,10 |
| ko | 0,59 | 70 % | 5,05 | 0,74 | 60 % | 7,70 |
| ar | 0,56 | 60 % | **3,25** | 0,78 | 70 % | 7,10 |
| hi | 0,61 | 65 % | **3,20** | 0,73 | 75 % | 6,75 |

**La referencia que hace falta para leer el solape:** una paráfrasis de la misma idea **en español**
(otras palabras, mismo sentido) solapa **0,54** con el original, con el primero igual en 55 % y 7,65
candidatos sobre el umbral. Es decir: el buscador es sensible a la redacción, y ni una traducción
perfecta daría 1,0.

## Lo que dicen los números

1. **El acuerdo temático entre idiomas está al nivel de una paráfrasis en español** (0,56 a 0,71
   contra 0,54). Voyage entiende la idea en los 11 idiomas: los nodos que recupera son del mismo
   tema.
2. **El problema real es el umbral.** Fuera del español las puntuaciones salen algo más bajas, y el
   corte de 0,3 deja muchos menos candidatos. En inglés, alemán, árabe e hindi quedan **2,8 a 3,25**
   de media, contra **7,35** en español. En la entrevista, eso es ofrecer menos de la mitad de los
   saltos: la exploración se empobrece justo en esos idiomas.
3. **El remedio lo arregla del todo.** Traducir la consulta al español antes de buscar devuelve los
   candidatos sobre el umbral al nivel del español en **todos** los idiomas (6,75 a 7,70) y sube el
   solape a **0,71 a 0,85**, por encima del techo de la paráfrasis (la traducción es más literal que
   una paráfrasis libre).

## Propuesta

**Adoptar el remedio en F5:** cuando el idioma del proyecto no es el español, la consulta que va al
buscador (la respuesta del usuario o el perfil de la sesión) se traduce al español antes de buscar.
El grafo no se toca: solo se traduce la consulta. Costo: una llamada corta a Claude Haiku por turno
fuera del español, con algo de latencia. Si la traducción falla, se busca con el texto original: es
la búsqueda de hoy, que funciona pero ofrece menos saltos. Esa caída queda registrada, sin silencio.

**Descartado:** bajar el umbral por idioma. Sube la cantidad, pero deja entrar candidatos de menor
afinidad, y habría que calibrar un umbral por cada idioma.

## Clave

La medición terminó. **El fundador ya puede retirar la clave:** borrar el archivo
`C:\Users\AlexDesk\Documents\my-idea-arreglos\.env` (trae, además de Voyage, las demás claves del
proyecto).
