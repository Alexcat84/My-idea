export const meta = {
  name: 'saneamiento-KM-lectura',
  description: 'Diagnostico de saneamiento, pasada de COHERENCIA INTERNA (K) o MUESTRA con semilla de titulos, condiciones, fase y dominio (M): lector con trampas, verificador ciego y arbitro; solo mide; los agentes solo leen',
  phases: [
    { title: 'Lectura', detail: 'un lector por lote' },
    { title: 'Verificacion', detail: 'verificador ciego' },
    { title: 'Arbitraje', detail: 'un arbitro relee los desacuerdos' },
  ],
}
const W = args.W, P = args.pasada
const S = '\\\\'
if (P !== 'K' && P !== 'M') throw new Error('args.pasada debe ser K o M')
if (!args.lotes || typeof args.lotes !== 'object' || Array.isArray(args.lotes)) throw new Error('args.lotes debe ser {lote: {n, trampas}}')
const VARA_K = `QUE MIDES (solo mides, no corriges): la COHERENCIA INTERNA de cada nodo. Un nodo de My-idea tiene titulo, resumen, pasos, entregable y condiciones de activacion, y los cinco deben hablar del MISMO concepto y decir lo mismo.
INCOHERENTE es: un paso que hace lo contrario de lo que el resumen ensena, o un resumen que contradice lo que hacen los pasos; un entregable que los pasos no producen o que es el producto de otro concepto; un titulo que nombra un concepto distinto del que desarrollan resumen y pasos; unas condiciones que describen una situacion que el nodo no trata; dos pasos que se contradicen entre si.
NO es incoherente: pasos mas detallados que el resumen, un resumen con contexto que los pasos no repiten, un entregable general, un paso practico en la direccion del resumen, la voz de la casa. En la duda, coherente.
POR CADA CONFLICTO: campos (por ejemplo "resumen-pasos", "pasos-entregable", "titulo-resumen", "condiciones-contenido", "pasos-pasos"), descripcion breve, y los dos fragmentos literales en conflicto.`
const VARA_M = `QUE MIDES (solo mides, no corriges), en cada nodo de esta MUESTRA:
1. titulo_ok: el titulo nombra el concepto que desarrollan el resumen y los pasos.
2. condiciones_ok: las condiciones de activacion describen situaciones en las que este contenido aplica de verdad.
3. fase_ok: la fase es correcta para el contenido. Fases: ideacion (descubrir el problema o la oportunidad, explorar la idea), validacion (probarla con clientes o con el mercado), planificacion (disenar el modelo, el plan, los recursos, la estrategia), ejecucion (operar, implementar, controlar, mejorar lo que ya funciona). Un nodo de gestion operativa de un negocio en marcha es ejecucion; si la fase es discutible pero defendible, es ok.
4. dominio_ok: el dominio es el mundo al que pertenece el contenido: core (emprender en general), quality (gestion de la calidad), health_safety (seguridad y salud en el trabajo), environmental (gestion ambiental), seguridad_digital, exportacion, franquicias, risk_management (gestion de riesgos), compras (compras y proveedores), entrega (logistica y entrega). Si encaja en dos, el que tiene es ok.
Cuando algo no este ok, da la propuesta (fase o dominio correcto) y una nota breve con el motivo. En la duda, ok.`
const REGLAS = `ERES SOLO LECTOR: no escribas, crees ni borres ningun fichero; devuelve todo en tu respuesta. PROHIBIDO, porque rompe la ceguera de la prueba: abrir cualquier fichero de ${W} que no sea tu lista; abrir dataset/, packs/ o docs/ de cualquier clon de My-idea; ejecutar git. No lances subagentes. Escribe en espanol, sin guiones largos (U+2014) ni medios (U+2013).`
const CONF = { type: 'object', properties: { campos: { type: 'string' }, descripcion: { type: 'string' }, fragmento_a: { type: 'string' }, fragmento_b: { type: 'string' } }, required: ['campos', 'descripcion', 'fragmento_a', 'fragmento_b'] }
const ITEM_K = { type: 'object', properties: { id: { type: 'string' }, coherente: { type: 'boolean' }, conflictos: { type: 'array', items: CONF }, nota: { type: 'string' } }, required: ['id', 'coherente', 'conflictos', 'nota'] }
const FASES = ['ideacion', 'validacion', 'planificacion', 'ejecucion']
const ITEM_M = { type: 'object', properties: {
  id: { type: 'string' }, titulo_ok: { type: 'boolean' }, condiciones_ok: { type: 'boolean' },
  fase_ok: { type: 'boolean' }, fase_propuesta: { type: 'string' }, dominio_ok: { type: 'boolean' }, dominio_propuesto: { type: 'string' }, nota: { type: 'string' } },
  required: ['id', 'titulo_ok', 'condiciones_ok', 'fase_ok', 'fase_propuesta', 'dominio_ok', 'dominio_propuesto', 'nota'] }
const VARA = P === 'K' ? VARA_K : VARA_M
const LISTA = { type: 'object', properties: { items: { type: 'array', items: P === 'K' ? ITEM_K : ITEM_M } }, required: ['items'] }
const QUE = P === 'K' ? 'la coherencia interna' : 'titulos, condiciones, fase y dominio de una muestra'
const lista = lote => `${W}${S}${P}${S}lotes${S}lote_${lote}.md`
const marcado = x => P === 'K' ? !x.coherente : !(x.titulo_ok && x.condiciones_ok && x.fase_ok && x.dominio_ok)
const clave = x => P === 'K' ? `${x.coherente}|${[...new Set(x.conflictos.map(c => c.campos))].sort().join(',')}`
  : `${x.titulo_ok}|${x.condiciones_ok}|${x.fase_ok}|${x.dominio_ok}`
function cazada(tipo, x) {
  if (!x) return false
  if (P === 'K') return !x.coherente
  if (tipo === 'FASE_O_DOMINIO_MAL') return !x.fase_ok || !x.dominio_ok
  return !x.titulo_ok || !x.condiciones_ok
}
function recall(trampas, porId) {
  const fallos = []; let n = 0
  for (const [id, tipo] of Object.entries(trampas)) { if (cazada(tipo, porId[id])) n++; else fallos.push(`${id} (${tipo})`) }
  return { total: Object.keys(trampas).length, cazadas: n, fallos }
}
function lector(lote, intento) {
  return limitado(() => agent(`Eres el LECTOR del lote ${lote} de un diagnostico de saneamiento del catalogo de My-idea (${QUE}).

TU LISTA: ${lista(lote)} (un bloque por nodo). Lee CADA bloque entero, sin saltarte ninguno.
${VARA}
Devuelve TODOS los bloques (${args.lotes[lote].n}), cada uno con su id y su medida.
${REGLAS}`, { label: `lector${P}:${lote}${intento > 1 ? ':r' + intento : ''}`, phase: 'Lectura', schema: LISTA }))
}
function verificador(lote, ids) {
  return limitado(() => agent(`Eres el VERIFICADOR CIEGO del lote ${lote} de un diagnostico de saneamiento del catalogo de My-idea (${QUE}). Otro lector ya midio estos nodos; tu no sabes que encontro. Midelos desde cero.

TU LISTA: los bloques de ${lista(lote)} cuyos ids son: ${ids.join(', ')}. Solo esos, cada uno entero.
${VARA}
Devuelve todos los bloques de tu lista con su medida.
${REGLAS}`, { label: `verificador${P}:${lote}`, phase: 'Verificacion', schema: LISTA }))
}
function arbitro(lote, casos) {
  const txt = casos.map(c => `- ${c.id}: LECTOR A: ${JSON.stringify(c.a)} / LECTOR B: ${JSON.stringify(c.b)}`).join('\n')
  return limitado(() => agent(`Eres el ARBITRO del lote ${lote} de un diagnostico de saneamiento del catalogo de My-idea (${QUE}). Dos lectores independientes no coinciden. Decide releyendo el nodo, no sus razones.

LOS NODOS: sus bloques estan en ${lista(lote)} (lee solo los de estos ids). Los desacuerdos:
${txt}
${VARA}
Devuelve todos los nodos en disputa con tu medida final; en la nota di quien tenia razon y por que.
${REGLAS}`, { label: `arbitro${P}:${lote}`, phase: 'Arbitraje', schema: LISTA }))
}
const CONC = args.conc || 5
let activos = 0
const cola = []
async function limitado(fn) {
  if (activos >= CONC) await new Promise(r => cola.push(r))
  activos++
  try { return await fn() } finally { activos--; const sig = cola.shift(); if (sig) sig() }
}
const resultados = await pipeline(Object.keys(args.lotes),
  async (lote) => {
    const n = args.lotes[lote].n, trampas = args.lotes[lote].trampas
    let lec = await lector(lote, 1), intento = 1
    const historial = []
    for (;;) {
      if (!lec) throw new Error('lector sin resultado en ' + lote)
      const porId = Object.fromEntries(lec.items.map(x => [x.id, x]))
      const r = recall(trampas, porId)
      historial.push({ intento, bloques: Object.keys(porId).length, esperados: n, recall: r })
      log(`${lote} lectura ${intento}: ${Object.keys(porId).length}/${n}, trampas ${r.cazadas}/${r.total}`)
      if (Object.keys(porId).length >= n && r.cazadas === r.total) break
      if (intento >= 2) { log(`${lote}: tras 2 lecturas: ${r.fallos.join('; ')}`); break }
      intento++; lec = await lector(lote, intento)
    }
    return { lote, lec, historial }
  },
  async ({ lote, lec, historial }) => {
    const con = lec.items.filter(marcado).map(x => x.id)
    const limpios = lec.items.filter(x => !marcado(x)).map(x => x.id)
    const muestra = P === 'M' ? limpios : limpios.filter((_, i) => i % 6 === 0)
    const ver = await verificador(lote, [...con, ...muestra].sort())
    return { lote, lec, historial, ver, muestra }
  },
  async ({ lote, lec, historial, ver, muestra }) => {
    const trampas = args.lotes[lote].trampas
    const A = Object.fromEntries(lec.items.map(x => [x.id, x]))
    const B = Object.fromEntries(((ver && ver.items) || []).map(x => [x.id, x]))
    const recallVerif = recall(Object.fromEntries(Object.entries(trampas).filter(([id]) => B[id])), B)
    const casos = Object.keys(B).filter(id => !trampas[id] && A[id] && clave(A[id]) !== clave(B[id])).map(id => ({ id, a: A[id], b: B[id] }))
    const arb = casos.length ? await arbitro(lote, casos) : { items: [] }
    const C = Object.fromEntries(((arb && arb.items) || []).map(x => [x.id, x]))
    const final = []
    for (const id of Object.keys(A)) {
      if (trampas[id]) continue
      if (C[id]) final.push({ ...C[id], decidido_por: 'arbitro' })
      else if (B[id]) final.push({ ...B[id], decidido_por: 'lector y verificador de acuerdo' })
      else final.push({ ...A[id], decidido_por: 'lector (limpio no muestreado)' })
    }
    const muestraCambiada = muestra.filter(id => !trampas[id] && C[id] && marcado(C[id]))
    log(`${lote}: ${final.length} nodos, ${final.filter(marcado).length} marcados; desacuerdos ${casos.length}; limpios muestreados ${muestra.length}, cambiados ${muestraCambiada.length}; trampas del verificador ${recallVerif.cazadas}/${recallVerif.total}`)
    return { lote, historial, recallVerificador: recallVerif, desacuerdos: casos.length, muestreados: muestra.length, muestraCambiada, final }
  })
return resultados.filter(Boolean)
