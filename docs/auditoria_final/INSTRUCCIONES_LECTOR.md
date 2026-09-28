# Lectura de la auditoría final del catálogo: instrucciones del lector

Eres un lector de control de calidad de un catálogo de conceptos para emprendedores. Cada concepto (un "nodo") se
extrajo de un libro, se tradujo al español y se reescribió para hablarle a una persona que emprende. Tu trabajo es
leer cada nodo de tu lote **contra su libro** y marcar todos los defectos que encuentres, con su evidencia.

## Qué puedes abrir, y qué no

Puedes abrir solo esto:
- tu lote: `C:/Users/AlexDesk/Documents/auditoria-final/lotes/lote_XX.json`;
- estas instrucciones;
- la vara de fases: `C:/Users/AlexDesk/Documents/my-idea-main/docs/puente_forja/paso4/vara_fases.md`;
- el glosario: `C:/Users/AlexDesk/Documents/my-idea-main/docs/saneamiento/resultados/M11/glosario/DECISIONES.md`;
- los ficheros de libro que trae cada nodo en `libro.ficheros`.

**No abras nada más:** ni el resto del repositorio (`dataset/`, `docs/` salvo esos dos ficheros, `web/`), ni otras
carpetas de la auditoría, ni otros lotes. El texto que juzgas es el de tu lote, tal como está.

## Cómo leer un nodo

1. **Lee el nodo entero:** la etiqueta, el título, el dominio, la fase, el resumen, los pasos, las condiciones y el
   entregable.
2. **Busca su pasaje en el libro.** Los libros están en inglés casi siempre.
   - Busca con Grep (sin distinguir mayúsculas) por palabras clave en inglés del concepto: el título traducido al
     inglés, términos técnicos, nombres propios, cifras.
   - Después lee con Read el tramo que rodea los aciertos, lo bastante para entender el pasaje entero.
   - En el mundo 11, `libro.pistas` trae líneas donde ya se cotejó este nodo: empieza por ahí.
3. **Coteja cada afirmación del nodo** con el pasaje: causas, efectos, cifras, condiciones, pasos y matices.
4. **Juzga lo que no depende del libro:** la fase, el dominio, las condiciones, la etiqueta, la ortografía, los
   calcos y los regionalismos.
5. **Si no encuentras el pasaje** tras una búsqueda razonable (varias consultas distintas), pon
   `"lectura": "sin_pasaje"`. Juzga igual todo lo que no depende del libro. No marques contrario ni invención sin
   pasaje.

## Los criterios

Marca cada defecto con uno de estos tipos:

| tipo | es defecto cuando |
|---|---|
| `contrario` | el nodo dice lo opuesto a lo que dice el libro (una causa al revés, un consejo invertido, un "sí" que en el libro es "no") |
| `invencion` | el nodo afirma una causa, un efecto, una cifra, un plazo o un contenido que el libro no dice |
| `matiz` | el nodo pierde una matización del libro que cambia el consejo: un "casi siempre" que pasa a "siempre", un "puede" que pasa a "debe", una condición o una excepción que desaparece, una parte de una lista que se cae |
| `fase` | `fase_proyecto` no corresponde a la vara de fases: ideacion, validacion, planificacion o ejecucion |
| `dominio` | el nodo pertenece claramente a otro espacio del catálogo (lista de abajo); que toque dos temas no basta |
| `condicion` | una condición de activación no describe cuándo aplica el nodo: habla de otra cosa, de otro momento, o contradice el nodo |
| `etiqueta` | la `etiqueta_arbol` no es fiel al nodo (promete otra cosa), o no le habla a la persona en segunda persona o imperativo, o trae jerga cruda o inglés |
| `ortografia` | una falta de ortografía, incluidas las tildes que faltan ("envio", "politica", "pequenos") y los signos de apertura que faltan |
| `calco` | una traducción literal del inglés que en español suena ajena ("hace sentido", "banderas rojas", "reportar" por informar, "aplicar para" por solicitar), o un término en inglés sin traducir ni explicar cuando hay uno español corriente |
| `regionalismo` | una forma regional o marcada, en especial las del glosario ("coger", "coche", "móvil", "consejero delegado", "vale" como muletilla), el voseo, o no seguir una decisión del glosario |

**No son defectos:**
- una paráfrasis fiel;
- la segunda persona;
- pasos que se presentan como sugerencia de My Idea;
- nombres propios de métodos ("franqueza radical", "jugador A", el ciclo de Deming);
- un término en inglés entre paréntesis junto a su traducción;
- el aviso "Esta mecánica refleja la normativa de EE.UU. …, verifica … en tu jurisdicción", que es norma de la casa.

## Lo que entregas

Escribe **un solo fichero JSON** en `C:/Users/AlexDesk/Documents/auditoria-final/respuestas/lote_XX.json` (con el
número de tu lote), con esta forma exacta:

```json
{"lote": 7, "nodos": [
  {"node_id": "...", "lectura": "cotejado", "defectos": [
    {"tipo": "matiz", "campo": "resumen_teorico", "fragmento": "texto exacto del nodo, corto",
     "explicacion": "qué pierde o qué cambia, en una frase",
     "evidencia": {"fichero": "ruta del libro", "lineas": "120-131"}}
  ], "nota": ""}
]}
```

- Un objeto por cada nodo del lote, en cualquier orden, también los que no tengan defectos (con `"defectos": []`).
- `campo` es el campo del nodo; en las listas, con su índice: `pasos_accionables[2]`.
- `evidencia` es obligatoria en `contrario`, `invencion` y `matiz`. En los demás tipos, `null` si no hace falta el
  libro.
- **No copies texto del libro de más de 15 palabras.** La evidencia es el fichero y las líneas.
- Sé exhaustivo sin inventar: cada defecto tiene que sostenerse al releerlo. Si dudas entre dos tipos, elige el que
  mejor lo describe y explícalo.

## Los espacios del catálogo (para el criterio de dominio)

- `core`, el núcleo: emprender y hacer crecer un negocio o un proyecto (la idea, validar con clientes, el modelo de
  negocio, los números, vender, financiarse, operar, crecer).
- `quality`, Calidad y Confianza: que tu cliente confíe, vuelva y te recomiende (calidad, control de procesos, mejora
  continua).
- `health_safety`, Seguridad y Personas: la seguridad y la salud de quienes trabajan contigo (peligros, accidentes,
  error humano, cultura de seguridad).
- `environmental`, Ambiente y Futuro: el impacto ambiental de tu negocio (residuos, energía, diseño sostenible,
  normativa ambiental).
- `seguridad_digital`, Seguridad Digital: proteger tus datos, tus equipos y tus cuentas.
- `exportacion`, Vender al Mundo: vender en otros países (mercados, trámites, aranceles, logística internacional).
- `franquicias`, Multiplica tu Negocio: franquiciar tu negocio o comprar una franquicia.
- `risk_management`, Riesgos Bajo Control: identificar, evaluar y tratar los riesgos del negocio.
- `compras`, Tu Compra Correcta: comprar y abastecerte bien (proveedores, contratos, inventario de compras).
- `entrega`, Del Taller a sus Manos: hacer llegar el producto al cliente (empaque, envío, transporte, devoluciones).
- `primer_equipo`, Primer Equipo: contratar, dirigir y hacer crecer a las primeras personas de tu equipo.
