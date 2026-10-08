# Juez de fidelidad de la salida: corrida final, 8 oct 2026

Paso D de `docs/producto/CORRIDA_FINAL.md`, con las instrucciones de `docs/producto/JUEZ_FIDELIDAD.md`.

**Umbral, fijado antes de medir:** 0 contrarios, 0 invenciones y 0 procedencias en el total de salidas.

## Estado

**Tramo B (la prueba de coherencia): NO PASA.** 1 invención sostenida por el árbitro. De ahí salió la regla única
NINGUNA CAUSA INVENTADA en los cinco redactores (6dc6c832c), en producción antes del vuelo del tramo C.

**Tramo C (el vuelo completo, intento 10 + fases 3 y 4): NO PASA.** 11 hallazgos sostenidos por el árbitro en 7 de los
14 planes: 9 invenciones y 2 contrarios, 0 procedencias. Las 4 trampas, cazadas. Por la regla del fundador no se
arregla nada: se reporta con su evidencia y se espera su visto.

## Tramo B: la prueba de coherencia (13:02 a 13:31 UTC)

- Salidas: 3, todas planes del núcleo (una por persona: sola, dos_empleados, empleado_mediana).
- Trampas sin marca: 1 (un contrario plantado), semilla 20261007, escrita por el extractor antes de leer.
- Paquetes: 4 (f001 a f004), un juez ciego por paquete. Solo abre su paquete y las instrucciones.

| Paquete | Origen | Afirmaciones leídas | Hallazgos del juez |
|---|---|---:|---|
| f001 | trampa (copia de f004) | 47 | 1 invención; **no cazó la trampa** |
| f001, relectura con otro juez | trampa | 54 | el contrario plantado (cazado, con su nodo) + la misma invención |
| f002 | real (plan dc9fc04f) | 55 | ninguno |
| f003 | real (plan 620ebeb4) | 84 | ninguno |
| f004 | real (plan 7567ab55, persona dos_empleados) | 45 | 1 invención |

La trampa: «Este paso puedes saltártelo: «Decide Fundar Solo o Acompañado» no hace falta en tu caso.» (contrario al
nodo `decision_fundador_solo_vs_equipo`). El primer juez no la cazó; por el método, su paquete se releyó con otro juez,
que sí la cazó. Todas las trampas quedan cazadas.

### El hallazgo sostenido

- **Clase:** invención (una causa que ningún nodo dice y la persona no contó).
- **Salida:** plan del núcleo 7567ab55 (sesión ac962885, proyecto cbb063e9), persona dos_empleados, 13:13 UTC.
- **La frase, en su contexto:** «Tienes un taller de macetas de cemento y acabas de contratar a dos personas, pero
  terminas haciendo tú el trabajo. Eso suele pasar cuando las expectativas no están dichas con claridad **y cuando
  enseñar un puesto cuesta más que hacerlo uno mismo**. Este plan te lleva de ejecutar a dirigir, paso a paso.»
- **Lo encontraron tres jueces por separado:** el de f004, el de f001 (la copia) y el de la relectura.
- **El árbitro (SOSTENIDO):** ningún nodo dice que enseñar un puesto cueste más que hacerlo uno mismo ni lo pone como
  causa. Lo más cercano, `entrenamiento_funcional_empleados` («una de las actividades de mayor apalancamiento que un
  manager puede realizar») y `entrenamiento_gerencial` («Entrenar es parte del trabajo de quien dirige»), valoran la
  formación y no hablan de su costo. La persona contó «no sé qué decirles para que lo hagan solos [...] no les explico
  cómo quiero que lo hagan, así que al final lo termino haciendo yo»: eso sostiene la primera causa (expectativas no
  dichas, que también respalda `entrenamiento_gerencial`), no la segunda. Es plausible, pero según la rúbrica una causa
  que nadie dijo es invención.

### Cuenta del tramo B

| Clase | Hallazgos sostenidos |
|---|---:|
| contrario | 0 |
| invención | 1 |
| procedencia | 0 |

Por tipo de salida: plan del núcleo, 1 invención en 3 salidas.

Los veredictos de cada juez y del árbitro, y la clave de las trampas, quedan fuera del repo (carpeta de la sesión).

## Tramo C: el vuelo completo (22:58 a 23:39 UTC, intento 10 y fases 3 y 4)

- Salidas: 16 en 6 proyectos: 2 Claridades, 7 planes del núcleo, 7 planes de mundo.
- Trampas sin marca: 4 (una invención, dos contrarios, una procedencia), semilla 20261007. **Las 4, cazadas** al primer
  juez: f003 («La norma ISO 4417 exige guardar estos registros...»), f004 y f008 («Este paso puedes saltártelo...»),
  f005 («Es lo que recomiendan los especialistas...»).
- 20 paquetes, un juez ciego por paquete; 18 hallazgos en 10 paquetes reales, cada uno arbitrado: **11 sostenidos, 7
  descartados**.

### Los hallazgos sostenidos

| Paquete | Salida | Clase | La afirmación | Por qué la sostiene el árbitro |
|---|---|---|---|---|
| f006 | plan de mundo, Calidad (265e4486) | invención | «un lote hecho con el mismo proceso suele salir más parejo» | ningún nodo compara lotes con pedidos; inclina una decisión que la persona dejó abierta |
| f006 | plan de mundo, Calidad (265e4486) | invención | «las piezas que van a la tienda de plantas [...] porque ahí un defecto te cuesta más» | nadie dio el costo de un defecto por canal; la comparación entre canales está pendiente |
| f007 | plan de mundo, Riesgos (ff010188) | invención | «para ver en pesos cuánto te cuesta un mes sin ese canal» | nadie dio la moneda; el contexto registra las cifras en USD (leve: la cuenta es correcta) |
| f009 | plan del núcleo (ee6de956) | contrario | «Lo que este plan aún no cubre: validar con clientes reales (conversaciones, una primera versión [...], una venta o preventa real)» | sus etapas 2, 4 y 5, sacadas de los nodos, mandan exactamente eso, incluido cobrar |
| f012 | plan de mundo, Seguridad Digital (f14f36e7) | invención | «El correo es la llave maestra: quien entra ahí puede recuperar tu Instagram.» | un mecanismo que ningún nodo describe; solo apareció en una pregunta de la IA que la persona no confirmó |
| f014 | plan del núcleo (aad2749d) | contrario | «anótalo al lado de tu costo de 130 para ver si coincide» (el costo de materiales) | la persona dijo que 130 incluye su hora a 50: el de materiales no puede coincidir |
| f014 | plan del núcleo (aad2749d) | invención | «calculado por separado para la tienda y para Instagram, porque no te dejan lo mismo» | nadie dio el precio que paga la tienda; el propio plan lo dice como "probablemente" |
| f016 | plan de mundo, Primer Equipo (8b7764c4) | invención | «Hoy haces tú el trabajo porque nadie sabe con precisión qué se espera de su puesto.» | **una CAUSA inventada**: la persona dio otra ("me cuesta delegar y decirles cuando algo sale mal") |
| f016 | plan de mundo, Primer Equipo (8b7764c4) | invención | «Sin eso, no puedes decirle a nadie que va tarde ni que va muy bien.» | ningún nodo pone la hoja escrita como requisito; los de opinión directa piden decirlo ya |
| f020 | plan del núcleo (c73e86f8) | invención | «Anota el nombre del cliente que más te ha recomendado [...]» | da por hecho un cliente que ya lo recomendó; se le preguntó y no contestó |
| f020 | plan del núcleo (c73e86f8) | invención | «Escríbele un mensaje de agradecimiento al cliente que más te ha recomendado [...]» | la misma suposición en otra etapa (el árbitro sugiere contarlas como un solo error de fondo) |

### Lo que se ve en los hallazgos (sin arreglar nada)

- **La regla de causas no bastó.** f016 afirma una causa de la situación de la persona que nadie dio, con la regla
  NINGUNA CAUSA INVENTADA ya en producción. La mayoría de las invenciones son del mismo tipo: hechos sobre el negocio
  de la persona (la moneda, el costo de un defecto por canal, que los canales dejan distinto, que ya hay clientes que
  recomiendan) que la IA da por sabidos.
- **El bloque «Lo que este plan aún no cubre»** (f009) contradice las etapas del propio plan. Puede ser texto que arma
  el código a partir de la cobertura de familias y no se recalcula con lo que el plan terminó cubriendo. El mismo
  bloque en f014 lo DESCARTÓ otro árbitro (lo leyó como nota de alcance): dos árbitros, dos lecturas del mismo bloque.
- **Las Claridades (2) salen limpias**; los 11 hallazgos están en 7 planes: 3 del núcleo y 4 de mundo.

### Cuenta del tramo C

| Clase | Hallazgos sostenidos |
|---|---:|
| contrario | 2 |
| invención | 9 |
| procedencia | 0 |

Por tipo de salida: plan del núcleo 5 (en 3 de 7 planes), plan de mundo 6 (en 4 de 7 planes), Claridad 0 (de 2).

Los veredictos de cada juez y de cada árbitro, y la clave de las trampas, quedan fuera del repo (carpeta de la sesión).
