# Juez de fidelidad de la salida: corrida final, 8 oct 2026

Paso D de `docs/producto/CORRIDA_FINAL.md`, con las instrucciones de `docs/producto/JUEZ_FIDELIDAD.md`.

**Umbral, fijado antes de medir:** 0 contrarios, 0 invenciones y 0 procedencias en el total de salidas.

## Estado

**Tramo B (la prueba de coherencia): NO PASA.** Un hallazgo sostenido por el árbitro: 1 invención. Por la regla
del fundador no se arregla nada: se reporta con su evidencia y se espera su visto.

El tramo C (el vuelo completo) está pendiente: el vuelo se repite cuando se resuelva el límite de arranques del día.

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
