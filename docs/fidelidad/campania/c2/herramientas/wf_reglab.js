export const meta = {
  name: 'fidelidad-regla-b-anadidos',
  description: 'Aplica la regla B del fundador a ANADIDOS ya fichados: clasifica LEGAL_CIFRA o PRACTICO y propone el texto final; solo leen',
  phases: [{ title: 'Regla B', detail: 'clasificacion y texto propuesto por ANADIDO' }],
}
if (!args || !args.lista || !Array.isArray(args.grupos)) throw new Error('args: {lista: ruta, grupos: [[ids], ...]}')
const SCHEMA = { type: 'object', properties: { decisiones: { type: 'array', items: { type: 'object', properties: {
  id: { type: 'string' }, tipo_anadido: { type: 'string', enum: ['LEGAL_CIFRA', 'PRACTICO', 'EXCEPCION'] },
  texto_final: { type: 'string' },
  segmentos: { type: 'array', items: { type: 'object', properties: { campo: { type: 'string' }, viejo: { type: 'string' }, nuevo: { type: 'string' } }, required: ['campo', 'viejo', 'nuevo'] } },
  motivo: { type: 'string' } }, required: ['id', 'tipo_anadido', 'texto_final', 'motivo'] } } }, required: ['decisiones'] }
phase('Regla B')
const res = await parallel(args.grupos.map((g, k) => () => agent(
`Aplicas la REGLA B del fundador de My-idea a pasos ya clasificados como INFERIDO-ANADIDO (el paso afirma algo concreto que su libro no respalda). SOLO LEES Y PROPONES: no escribas, crees ni borres ningun fichero. Todo en espanol, sin guiones largos (U+2014) ni medios (U+2013).

TU LISTA: en el fichero JSON ${args.lista} (solo lectura), los elementos con id: ${g.join(', ')}. Cada uno trae node_id, campo, indice, texto_actual, texto_fiel_propuesto, dato, libro_fichero, cita y otros_campos.

LA REGLA, literal:
- ANADIDO de cifra, plazo, norma o materia legal: se quita o se reemplaza por lo que dice el libro. -> tipo_anadido LEGAL_CIFRA; texto_final es el paso sin el dato o con el dato del libro (parte del texto_fiel_propuesto y comprueba en el libro).
- ANADIDO practico (herramienta, frecuencia, formato): se reescribe como sugerencia de My Idea, sin atribuirlo al autor. -> tipo_anadido PRACTICO; texto_final empieza exactamente por "Sugerencia de My Idea: " seguido del paso reescrito como sugerencia, en el mismo idioma y tono.
- Lo que la regla no resuelva limpio (el dato mezcla las dos cosas, o no esta claro que se quita, o quitarlo deja el paso vacio): tipo_anadido EXCEPCION, texto_final vacio, y el motivo claro.
Si un texto nombra una sigla de un pais (FDA, OSHA, IRS...), anade "o la autoridad equivalente en tu mercado".
DATOS REPETIDOS: si el mismo dato anadido aparece en otro campo del nodo (resumen_teorico, entregable_esperado; mira otros_campos y lee el nodo, solo lectura, en C:\\Users\\AlexDesk\\Documents\\my-idea-correcciones\\dataset\\nodos\\<node_id>.json), devuelve en segmentos el trozo EXACTO viejo (copiado del nodo) y el nuevo: en LEGAL_CIFRA se quita o se reemplaza igual; en PRACTICO, en el resumen_teorico se quita, y en el entregable se deja.
Puedes leer el libro de cada paso (libro_fichero) para comprobar. No lances subagentes. Devuelve una decision por id.`,
  { label: 'reglaB:' + (k + 1), phase: 'Regla B', schema: SCHEMA })))
return res.filter(Boolean).flatMap(r => r.decisiones)
