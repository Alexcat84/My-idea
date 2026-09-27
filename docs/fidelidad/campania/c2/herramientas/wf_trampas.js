export const meta = {
  name: 'fidelidad-campania-trampas',
  description: 'Genera 4 trampas (2 contrarias y 2 anadidas sinteticas) por lote de la campania de fidelidad; los agentes solo leen y devuelven datos',
  phases: [{ title: 'Trampas', detail: 'un generador por lote' }],
}
const W = args.W
const S = '\\\\'
const TRAMPA = { type: 'object', properties: {
  titulo: { type: 'string' }, resumen: { type: 'string' }, texto: { type: 'string' },
  tipo: { type: 'string', enum: ['CONTRARIO', 'ANADIDO'] }, libro: { type: 'string' }, fichero: { type: 'string' },
  lineas: { type: 'string' }, cita: { type: 'string' }, dato: { type: 'string' }, explicacion: { type: 'string' } },
  required: ['titulo', 'resumen', 'texto', 'tipo', 'libro', 'fichero', 'lineas', 'cita', 'explicacion'] }
const SCHEMA = { type: 'object', properties: { trampas: { type: 'array', items: TRAMPA } }, required: ['trampas'] }
if (!args.lotes || typeof args.lotes !== 'object') throw new Error('args.lotes: objeto {lote: {ficheros}} o lista de lotes con args.plan')
const PLAN = Array.isArray(args.lotes)
const ficherosDe = lote => PLAN ? `los que lista el fichero ${args.plan} (solo lectura) en su entrada "${lote}", campo "ficheros"` : args.lotes[lote].ficheros.join(' ; ')
phase('Trampas')
const nombres = PLAN ? args.lotes : Object.keys(args.lotes)
const CONC = args.conc || 6
const res = []
for (let i = 0; i < nombres.length; i += CONC) {
  const trozo = nombres.slice(i, i + CONC)
  const r = await parallel(trozo.map(lote => () => agent(
`Eres el GENERADOR DE TRAMPAS del lote ${lote} de la campania de fidelidad del catalogo de My-idea. SOLO LEES: no escribas ningun fichero, devuelve los datos. Todo en espanol, sin guiones largos (U+2014) ni medios (U+2013).

Libros del lote, SOLO LECTURA: ${ficherosDe(lote)}
Pasos reales del lote, SOLO LECTURA y solo para imitar su estilo y sus temas: ${W}${S}c2${S}claves${S}reales_${lote}.json

Escribe 2 pasos CONTRARIOS y 2 pasos ANADIDOS sinteticos, basados en pasajes REALES de esos libros (si hay varios libros, elige los que mas pasos tengan en el lote), que un lector atento deberia cazar:
- CONTRARIO: el paso aconseja lo que el libro desaconseja o contradice. Tiene que existir una cita del libro que diga lo opuesto. Sutil, como los errores reales: invertir una condicion, cambiar un umbral que el libro da, recomendar lo que el libro advierte que falla.
- ANADIDO: el paso va en la direccion del libro pero afirma un dato concreto que el libro NO respalda (cifra, plazo, herramienta o norma con nombre, responsable, frecuencia). Comprueba con Grep en todo el texto que ese dato no aparece.
Cada trampa con un titulo de nodo y un resumen breve verosimiles en el estilo de los reales, y el paso en el mismo tono y longitud que los pasos reales del lote. Reparte las 4 trampas por pasajes distintos. Comprueba que cada cita este literal en su linea.
No lances subagentes. Devuelve las 4 trampas con: titulo, resumen, texto, tipo, libro, fichero (la ruta exacta del libro), lineas (Lnnn o Lnnn-Lmmm), cita literal, dato (en ANADIDO) y explicacion.`,
  { label: 'trampas:' + lote, phase: 'Trampas', schema: SCHEMA })))
  res.push(...r)
  log(`trampas: ${res.length}/${nombres.length} lotes`)
}
return nombres.map((lote, i) => ({ lote, trampas: res[i] ? res[i].trampas : null }))
