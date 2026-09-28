# Verificación ciega de aristas: instrucciones

Un catálogo de conceptos para emprendedores se recorre como un grafo: después de trabajar un concepto, la entrevista
puede pasar a uno de sus "siguientes". Hay conceptos a los que hoy no se llega desde las puertas de su mundo. Para cada
uno se proponen conceptos candidatos desde los que llegar a él. Tu trabajo es juzgar cada arista propuesta.

## Qué juzgas

Para cada caso de tu lote tienes un **destino** y varias **candidatas**. Cada arista propuesta va de una candidata al
destino. Juzga cada candidata por separado:

- `sostiene`: después de trabajar la candidata, pasar al destino es un paso natural para la misma persona.
  - Puede ser que lo continúe o lo profundice, que sea el paso siguiente del mismo tema, o que resuelva algo que la
    candidata deja abierto.
  - Un tema que solo se parece no basta.
- `debil`: la relación existe pero es floja o indirecta; se entendería, sin que sea el paso natural.
- `no_se_sostiene`: no hay un paso natural entre las dos, son temas distintos, o el orden no tiene sentido (el destino
  tendría que ir antes).

Mira el título, el resumen, las condiciones de activación, el entregable y la fase de las dos. Una arista de una fase a
otra anterior no es imposible, pero pide una razón clara.

## Qué puedes abrir

Solo estas instrucciones y tu lote: `C:/Users/AlexDesk/Documents/auditoria-final/aristas/aristas_N.json`. Nada más,
ni el repositorio ni otras carpetas.

## Lo que entregas

Un solo fichero JSON en `C:/Users/AlexDesk/Documents/auditoria-final/aristas/respuesta_N.json`, con esta forma exacta:

```json
{"lote": 1, "casos": [
  {"caso": 4, "destino": "id_del_destino", "juicios": [
    {"desde": "id_de_la_candidata", "veredicto": "sostiene", "razon": "una frase"}
  ]}
]}
```

- Un objeto por caso, con un juicio por cada candidata.
- Juzga cada una con independencia: pueden sostenerse varias, o ninguna.
