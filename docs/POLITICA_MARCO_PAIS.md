# POLITICA DE PAIS: "MARCO CONTRA PAIS" (texto unico, ratificado por el fundador el 26 sep 2026)

*My-idea guia a emprendedores de CUALQUIER pais, en once idiomas. Muchos libros del catalogo son de Estados Unidos y
traen leyes, organismos, programas y cifras de ese pais. Esta politica dice que se hace con cada cosa. Hasta hoy vivia
repartida en adjudicaciones de agosto de 2026 (se citan abajo); **este documento es la letra unica, y el fundador la
ratifico el 26 sep 2026**. Donde una adjudicacion anterior diga otra cosa, manda este texto.*

---

## LAS TRES CLASES

### CLASE A. INTOCABLE: vocabulario y tratados internacionales
Lo que no es de un pais sino **acordado entre paises**: Incoterms, carta de credito, conocimiento de embarque, codigos
arancelarios, clausula antidesviacion, el PCT y el Protocolo de Madrid, los convenios de Naciones Unidas. **Se queda
tal cual**, porque es el vocabulario del comercio internacional, y lleva **ficha de vigencia**: se revisa cuando el
marco cambie de version. "Incoterms 2020 no es un dato local ni un detalle de estilo: es el vocabulario acordado entre
paises, y un catalogo que lo cite desactualizado miente con precision." Las instituciones de libro no se omiten: se
mantienen al dia.

### CLASE B. REENCUADRE a la clase universal
El ejemplo es de un pais, pero **la clase existe en casi todos**. El nodo lo dice y manda buscar lo propio: *"en
EE.UU. son estas; averigua las de tu pais"*, *"o el organismo equivalente en tu mercado"*. El metodo se conserva; el
organismo se vuelve *"averigua que organismo regula esto en tu pais"*. En la app, la tarjeta lo dice: **"Ejemplo de
Estados Unidos: busca el equivalente en tu pais."**

### CLASE C. NODO-FRONTERA con condicion explicita
Una ley con **alcance real**, que obliga a quien caiga bajo ella, sea o no de ese pais. No se borra ni se finge
universal: **gana la condicion honesta al frente**, en su primera condicion de activacion o en la primera frase del
resumen (*"si vendes productos de consumo en Estados Unidos"*, *"si levantas capital de inversionistas en Estados
Unidos"*, *"si tu empresa esta constituida en EE.UU."*). **Un nodo-frontera no lleva la formula de la clase B**: si
solo aplica en un pais, no promete un equivalente en el tuyo. En la app, la tarjeta lo dice: **"Aplica si operas o
vendes en Estados Unidos."** El modelo es la familia de Magnuson-Moss.

### LOS PROGRAMAS DE UN GOBIERNO: CLASE C (la reversion de agosto)
Un programa de un gobierno concreto (un programa de OSHA, de la SBA, de un estado) **no se depreca**: va como **clase
C** con *"si operas en EE.UU."*. La doctrina inicial de agosto ("los programas de tu estado no significan nada donde
no hay estados con programa", deprecar de seleccion) **se revirtio** en la politica de pais de agosto de 2026: los
nodos de programa o figura de un solo pais volvieron con su condicion honesta excluyente
(`packs/_core/poda/_revive_pais.json`; `docs/LECTURA_CONDICIONES_Y_DEPRECADOS.md`).

---

## LAS DOS REGLAS

### LA REGLA DE LA CIFRA
**La cifra de MERCADO sale; la cifra que ES LA NORMA se queda, dentro de su nodo-frontera**, porque alli el numero es
el hecho y la frontera ya le dice al lector cuando le aplica. Un precio, una tarifa o un costo de mercado sale con
*"pregunta el precio en tu mercado"*; un umbral legal, un plazo o una tasa que fija una ley se quedan en su clase C.

### LA REGLA DEL EMPLEO
**Contratar, la nomina y el despido van como METODO, nunca como norma de un pais.** Como seleccionar, entrevistar,
pagar o despedir es metodo y se ensena; que preguntas son ilegales, que figura laboral existe (el empleo *at-will*),
que plazos o indemnizaciones fija la ley, es norma de un pais y, si se nombra, va como clase C con su condicion o
como clase B con "averigua lo que dice la ley laboral de tu pais". *(Esta regla no estaba escrita en el repo antes
de este documento; la ratifica el fundador el 26 sep 2026.)*

---

## COMO SE REGISTRA Y COMO SE GUARDA

- **La clase no se deduce del texto: se declara.** `dataset/metadata/jurisdiccion.json` lista cada nodo con contenido
  propio de un pais, con su pais, su clase (A, B o C) y su motivo. La app lee esa lista para su aviso.
- **Guarda:** ningun nodo vivo con contenido de un pais queda sin clase (`engine/test_jurisdiccion.py`).
- **Solo se reescribe lo incoherente** (por ejemplo, un nodo-frontera que ademas promete "el equivalente en tu
  mercado"), por correccion declarada en el propio nodo.

## DE DONDE VIENE (las adjudicaciones de agosto 2026)

- `docs/PENDIENTES.md`: ficha `vigencia-del-marco-internacional` (clase A y su ficha de vigencia); "DOCTRINA DE LA
  CLASE (ago 2026)"; el patron Magnuson-Moss ("no se borra el marco nacional, se condiciona").
- `docs/GRADIENTE_VEREDICTOS.md`: PCT y Protocolo de Madrid intocables; las URL de agencias, clase "ejemplar de un pais".
- `packs/exportacion/poda/MARCO_VS_PAIS.md` y `ADJUDICACION_MARCO_VS_PAIS.md` (clases B-1, B-2, B-3 y C del comercio).
- `packs/_core/poda/REGULACION_EEUU_NUCLEO.md` (clases 2 y 3 del nucleo), `_frontera_eeuu.json`, `_reencuadre_clase.json`,
  `_cierre_ftc.json`, `_revive_pais.json`, `_residuales_clasificados.json`.
- `scripts/censo_duplicacion.py` ("LA DOCTRINA DEL IMPORTE", la regla de la cifra); `scripts/revoz_pack.py` (metodo
  mas "preguntalo en tu mercado").
- `dataset/metadata/falsos_positivos_adjudicados.json` (nodos-frontera y revividos por la politica de pais).
