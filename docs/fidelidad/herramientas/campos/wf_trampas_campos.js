export const meta = {
  name: 'fidelidad-campos-trampas',
  description: 'Genera 4 nodos trampa por lote para la pasada sobre resumen, entregable, condiciones, titulo y etiqueta; los agentes solo leen y devuelven datos',
  phases: [{ title: 'Trampas', detail: 'un generador por lote' }],
}
const W = args.W
const S = '\\\\'
const TRAMPA = { type: 'object', properties: {
  titulo: { type: 'string' }, etiqueta: { type: 'string' }, resumen: { type: 'string' }, entregable: { type: 'string' },
  condiciones: { type: 'array', items: { type: 'string' } },
  tipo: { type: 'string', enum: ['CONTRARIO', 'ANADIDO'] }, campo: { type: 'string', enum: ['resumen', 'entregable', 'condiciones'] },
  libro: { type: 'string' }, fichero: { type: 'string' }, lineas: { type: 'string' }, cita: { type: 'string' }, dato: { type: 'string' }, explicacion: { type: 'string' } },
  required: ['titulo', 'etiqueta', 'resumen', 'entregable', 'condiciones', 'tipo', 'campo', 'libro', 'fichero', 'lineas', 'cita', 'dato', 'explicacion'] }
const SCHEMA = { type: 'object', properties: { trampas: { type: 'array', items: TRAMPA } }, required: ['trampas'] }
const nombres = args.lotes
const CONC = args.conc || 5
phase('Trampas')
const res = []
for (let i = 0; i < nombres.length; i += CONC) {
  const trozo = nombres.slice(i, i + CONC)
  const r = await parallel(trozo.map(lote => () => agent(
`Eres el GENERADOR DE TRAMPAS del lote ${lote} de una pasada de fidelidad del catalogo de My-idea sobre los campos de cada nodo que no son pasos: titulo, etiqueta de cara, resumen, entregable y condiciones de activacion. SOLO LEES: no escribas ningun fichero, devuelve los datos. Todo en espanol, sin guiones largos (U+2014) ni medios (U+2013).

Libros del lote, SOLO LECTURA: los que lista el fichero ${args.plan} en su entrada "${lote}", campo "ficheros".
Nodos reales del lote, SOLO LECTURA y solo para imitar su estilo, longitud y temas: ${W}${S}c2${S}claves${S}reales_${lote}.json

Escribe 4 NODOS sinteticos completos (titulo, etiqueta corta, resumen, entregable y 1 a 3 condiciones de activacion), verosimiles y en el estilo de los reales, basados en pasajes REALES de esos libros. Cada nodo lleva UN solo error sembrado en UNO de sus campos (resumen, entregable o condiciones); el resto del nodo es fiel. 2 nodos con un error CONTRARIO y 2 con un ANADIDO de cifra, plazo o norma:
- CONTRARIO: el campo dice lo opuesto al libro o cambia un umbral, un plazo, una secuencia o una consecuencia que el libro da. Tiene que existir una cita del libro que diga lo contrario. Sutil, como los errores reales.
- ANADIDO de cifra, plazo o norma: el campo afirma una cifra, un plazo, una norma o un requisito legal concreto que el libro NO da. Comprueba con Grep en todo el libro que ese dato no aparece.
Reparte los errores entre campos distintos (no los 4 en el resumen). Comprueba que cada cita este literal en su linea.
No lances subagentes. Devuelve los 4 nodos con: titulo, etiqueta, resumen, entregable, condiciones, tipo, campo (donde esta el error), libro, fichero (ruta exacta del libro), lineas, cita literal, dato (el fragmento erroneo tal como aparece en el campo) y explicacion.`,
  { label: 'trampas:' + lote, phase: 'Trampas', schema: SCHEMA })))
  res.push(...r)
  log(`trampas: ${res.length}/${nombres.length} lotes`)
}
return nombres.map((lote, i) => ({ lote, trampas: res[i] ? res[i].trampas : null }))
