export const meta = {
  name: 'saneamiento-F-fase',
  description: 'Saneamiento TANDA 2, punto 8 (fundador, 26 sep 2026): la FASE de los 853 nodos vivos marcados validacion o ideacion, con la vara calibrada de la pasada M; lector con trampas, verificador ciego y arbitro; los agentes solo leen',
  phases: [{ title: 'Lectura' }, { title: 'Verificacion' }, { title: 'Arbitraje' }],
}
const W = args.W
const S = '\\\\'
const VARA = `QUE MIDES (solo mides, no corriges): la FASE de cada nodo del catalogo de My-idea. Cada bloque trae la fase que tiene hoy.
Fases: ideacion (descubrir el problema o la oportunidad, explorar la idea), validacion (probarla con clientes o con el mercado), planificacion (disenar el modelo, el plan, los recursos, la estrategia), ejecucion (operar, implementar, controlar, mejorar lo que ya funciona). Un nodo de gestion operativa de un negocio en marcha es ejecucion; si la fase es discutible pero defendible, es ok.
fase_ok: la fase que trae es correcta para el contenido (titulo, resumen, pasos, entregable, condiciones). Cuando no lo sea, fase_propuesta es la fase correcta (una de las cuatro) y la nota dice el motivo en una frase. Si es ok, fase_propuesta es la misma que trae. En la duda, ok.`
const REGLAS = `ERES SOLO LECTOR: no escribas, crees ni borres ningun fichero; devuelve todo en tu respuesta. PROHIBIDO, porque rompe la ceguera de la prueba: abrir cualquier fichero de ${W} que no sea tu lista; abrir dataset/, packs/ o docs/ de cualquier clon de My-idea; ejecutar git. No lances subagentes. Escribe en espanol, sin guiones largos (U+2014) ni medios (U+2013).`
const FASES = ['ideacion', 'validacion', 'planificacion', 'ejecucion']
const ITEM = { type: 'object', properties: { id: { type: 'string' }, fase_ok: { type: 'boolean' }, fase_propuesta: { type: 'string', enum: FASES }, nota: { type: 'string' } }, required: ['id', 'fase_ok', 'fase_propuesta', 'nota'] }
const LISTA = { type: 'object', properties: { items: { type: 'array', items: ITEM } }, required: ['items'] }
const lista = l => `${W}${S}F${S}lotes${S}lote_${l}.md`
const clave = x => x.fase_ok ? 'ok' : x.fase_propuesta
const cazada = (t, x) => !!x && (t === 'FASE_MAL' ? !x.fase_ok : x.fase_ok)
function recall(tr, porId) { let n = 0; const f = []; for (const [id, t] of Object.entries(tr)) { if (cazada(t, porId[id])) n++; else f.push(`${id} (${t})`) } return { total: Object.keys(tr).length, cazadas: n, fallos: f } }
const CONC = 6; let activos = 0; const cola = []
async function limitado(fn) { if (activos >= CONC) await new Promise(r => cola.push(r)); activos++; try { return await fn() } finally { activos--; const s = cola.shift(); if (s) s() } }
const res = await pipeline(Object.keys(args.lotes),
  async l => {
    const pedir = r => limitado(() => agent(`Eres el LECTOR${r ? ' (segunda lectura, despacio)' : ''} del lote ${l} de la pasada de fase del saneamiento del catalogo de My-idea.\nTU LISTA: ${lista(l)} (un bloque por nodo). Lee CADA bloque entero, sin saltarte ninguno.\n${VARA}\nDevuelve TODOS los bloques (${args.lotes[l].n}), cada uno con su id y su medida.\n${REGLAS}`, { label: `lector:${l}${r ? ':r2' : ''}`, phase: 'Lectura', schema: LISTA }))
    let lec = await pedir(false)
    let r = recall(args.lotes[l].trampas, Object.fromEntries(lec.items.map(x => [x.id, x])))
    if (r.cazadas < r.total || lec.items.length < args.lotes[l].n) { log(`${l}: trampas ${r.cazadas}/${r.total}, ${lec.items.length}/${args.lotes[l].n}; relectura`); lec = await pedir(true); r = recall(args.lotes[l].trampas, Object.fromEntries(lec.items.map(x => [x.id, x]))) }
    log(`${l}: ${lec.items.length}/${args.lotes[l].n}, trampas ${r.cazadas}/${r.total}, marcados ${lec.items.filter(x => !x.fase_ok).length}`)
    return { l, lec, r }
  },
  async ({ l, lec, r }) => {
    const ids = lec.items.filter((x, i) => !x.fase_ok || i % 4 === 0).map(x => x.id)
    const ver = await limitado(() => agent(`Eres el VERIFICADOR CIEGO del lote ${l} de la pasada de fase del saneamiento del catalogo de My-idea. Otro lector ya midio estos nodos; tu no sabes que encontro. Midelos desde cero.\nTU LISTA: los bloques de ${lista(l)} cuyos ids son: ${ids.join(', ')}. Solo esos, cada uno entero.\n${VARA}\nDevuelve todos los bloques de tu lista con su medida.\n${REGLAS}`, { label: `verificador:${l}`, phase: 'Verificacion', schema: LISTA }))
    return { l, lec, r, ver }
  },
  async ({ l, lec, r, ver }) => {
    const tr = args.lotes[l].trampas
    const A = Object.fromEntries(lec.items.map(x => [x.id, x])), B = Object.fromEntries(((ver && ver.items) || []).map(x => [x.id, x]))
    const casos = Object.keys(B).filter(id => !tr[id] && A[id] && clave(A[id]) !== clave(B[id]))
    const txt = casos.map(id => `- ${id}: LECTOR A: ${JSON.stringify(A[id])} / LECTOR B: ${JSON.stringify(B[id])}`).join('\n')
    const arb = casos.length ? await limitado(() => agent(`Eres el ARBITRO del lote ${l} de la pasada de fase del saneamiento del catalogo de My-idea. Dos lectores independientes no coinciden. Decide releyendo el nodo, no sus razones.\nLOS NODOS: sus bloques estan en ${lista(l)} (lee solo los de estos ids). Los desacuerdos:\n${txt}\n${VARA}\nDevuelve todos los nodos en disputa con tu medida final; en la nota di quien tenia razon y por que.\n${REGLAS}`, { label: `arbitro:${l}`, phase: 'Arbitraje', schema: LISTA })) : { items: [] }
    const C = Object.fromEntries(((arb && arb.items) || []).map(x => [x.id, x]))
    const final = Object.keys(A).filter(id => !tr[id]).map(id => ({ ...(C[id] || B[id] || A[id]), decidido_por: C[id] ? 'arbitro' : B[id] ? 'lector y verificador de acuerdo' : 'lector (limpio, sin muestra del verificador)' }))
    const rv = recall(Object.fromEntries(Object.entries(tr).filter(([id]) => B[id])), B)
    log(`${l}: fase mal ${final.filter(x => !x.fase_ok).length}; desacuerdos ${casos.length}; trampas del verificador ${rv.cazadas}/${rv.total}`)
    return { lote: l, recall: r, recallVerificador: rv, desacuerdos: casos.length, final }
  })
return res.filter(Boolean)