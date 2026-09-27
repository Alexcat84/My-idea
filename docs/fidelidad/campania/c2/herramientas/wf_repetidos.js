export const meta = {
  name: 'fidelidad-datos-repetidos',
  description: 'Por cada correccion decidida, busca si el mismo dato se repite en otro campo del nodo y propone el segmento; solo leen',
  phases: [{ title: 'Repetidos', detail: 'revisor de nodo por grupo de correcciones' }],
}
if (!args || !args.decision || !Array.isArray(args.grupos)) throw new Error('args: {decision: ruta, grupos: [[ficha_id,...],...]}')
const SCHEMA = { type: 'object', properties: { segmentos: { type: 'array', items: { type: 'object', properties: {
  ficha_id: { type: 'string' }, campo: { type: 'string', enum: ['resumen_teorico', 'entregable_esperado', 'pasos_accionables'] },
  indice: { type: 'number' }, viejo: { type: 'string' }, nuevo: { type: 'string' }, motivo: { type: 'string' } },
  required: ['ficha_id', 'campo', 'viejo', 'nuevo', 'motivo'] } } }, required: ['segmentos'] }
phase('Repetidos')
const CONC = args.conc || 4
const res = []
for (let i = 0; i < args.grupos.length; i += CONC) {
  const trozo = args.grupos.slice(i, i + CONC)
  const r = await parallel(trozo.map((g, k) => () => agent(
`Eres REVISOR DE NODO de la campania de fidelidad de My-idea. SOLO LEES Y PROPONES: no escribas ningun fichero. Todo en espanol, sin guiones largos (U+2014) ni medios (U+2013).

En el fichero ${args.decision} (solo lectura), clave "correcciones", mira las entradas con ficha_id: ${g.join(', ')}. Cada una corrige UN paso de un nodo (texto_anterior -> texto_nuevo) por un dato que su libro contradice o no respalda (campo "dato", "veredicto" y "decision").

Para cada una, lee el nodo entero, solo lectura: C:\\Users\\AlexDesk\\Documents\\my-idea-correcciones\\dataset\\nodos\\<node_id>.json. Busca si el MISMO dato (la misma idea contraria, la misma cifra, plazo, norma, herramienta o formato) aparece tambien en resumen_teorico, entregable_esperado u OTRO paso de pasos_accionables. Si aparece, devuelve un segmento: el trozo EXACTO viejo, copiado caracter a caracter del nodo, y el trozo nuevo, con esta regla:
- si la correccion es CONTRARIO o un ANADIDO de cifra, plazo, norma o materia legal: el segmento se corrige igual que el paso (lo que dice el libro, o sin el dato);
- si es un ANADIDO practico (el texto_nuevo empieza por "Sugerencia de My Idea: "): en el resumen_teorico se quita el dato; en el entregable y en otros pasos se deja (no devuelvas segmento).
Solo segmentos que repitan ESE dato; nada mas del nodo se toca. Si una sigla de un pais aparece en el texto nuevo (FDA, OSHA, IRS...), anade "o la autoridad equivalente en tu mercado". Para un paso, da su indice desde 0. Si no hay repeticiones, devuelve la lista vacia. No lances subagentes.`,
    { label: 'repetidos:' + (i + k + 1), phase: 'Repetidos', schema: SCHEMA })))
  res.push(...r)
}
return res.filter(Boolean).flatMap(r => r.segmentos)
