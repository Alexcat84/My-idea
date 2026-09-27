export const meta = {
  name: 'saneamiento-R-lectura',
  description: 'Diagnostico de saneamiento, pasada de ARISTAS RANCIAS tras las correcciones de fidelidad: lector con trampas, verificador ciego y arbitro; solo mide; los agentes solo leen',
  phases: [
    { title: 'Lectura', detail: 'un lector por lote' },
    { title: 'Verificacion', detail: 'verificador ciego' },
    { title: 'Arbitraje', detail: 'un arbitro relee los desacuerdos' },
  ],
}
const W = args.W, P = 'R'
const S = '\\\\'
if (!args.lotes || typeof args.lotes !== 'object' || Array.isArray(args.lotes)) throw new Error('args.lotes debe ser {lote: {n, trampas}}')
const VARA = `QUE MIDES (solo mides, no corriges): si cada ARISTA sigue en pie. En My-idea una arista une dos nodos del catalogo en un recorrido: el vecino que va DESPUES es un paso natural a continuacion de este nodo (lo usa, lo continua o lo profundiza); el que va ANTES lo prepara. La campania de fidelidad corrigio el texto de estos nodos; mides si sus aristas siguen teniendo sentido con el texto de HOY.
Por cada arista, su estado:
- VIGENTE: la relacion se sostiene con el texto de hoy de los dos nodos (aunque sea amplia o tematica).
- RANCIA_POR_CORRECCION: la relacion se apoyaba en lo que la correccion quito o cambio, y con el texto de hoy ya no se sostiene.
- RANCIA_DE_ANTES: la relacion no se sostiene, y no por la correccion: los dos nodos no tienen que ver, o el orden (antes o despues) esta invertido.
- DUDOSA: no puedes decidir con lo que ves.
Da un motivo breve en cada una que no sea VIGENTE. En la duda entre vigente y rancia, VIGENTE.`
const REGLAS = `ERES SOLO LECTOR: no escribas, crees ni borres ningun fichero; devuelve todo en tu respuesta. PROHIBIDO, porque rompe la ceguera de la prueba: abrir cualquier fichero de ${W} que no sea tu lista; abrir dataset/, packs/ o docs/ de cualquier clon de My-idea; ejecutar git. No lances subagentes. Escribe en espanol, sin guiones largos (U+2014) ni medios (U+2013).`
const ITEM_R = { type: 'object', properties: { id: { type: 'string' }, estado: { type: 'string', enum: ['VIGENTE', 'RANCIA_POR_CORRECCION', 'RANCIA_DE_ANTES', 'DUDOSA'] }, motivo: { type: 'string' } }, required: ['id', 'estado', 'motivo'] }
const CONF = { type: 'object', properties: { campos: { type: 'string' }, descripcion: { type: 'string' }, fragmento_a: { type: 'string' }, fragmento_b: { type: 'string' } }, required: ['campos', 'descripcion', 'fragmento_a', 'fragmento_b'] }
const ITEM_K = { type: 'object', properties: { id: { type: 'string' }, coherente: { type: 'boolean' }, conflictos: { type: 'array', items: CONF }, nota: { type: 'string' } }, required: ['id', 'coherente', 'conflictos', 'nota'] }
const FASES = ['ideacion', 'validacion', 'planificacion', 'ejecucion']
const ITEM_M = { type: 'object', properties: {
  id: { type: 'string' }, titulo_ok: { type: 'boolean' }, condiciones_ok: { type: 'boolean' },
  fase_ok: { type: 'boolean' }, fase_propuesta: { type: 'string' }, dominio_ok: { type: 'boolean' }, dominio_propuesto: { type: 'string' }, nota: { type: 'string' } },
  required: ['id', 'titulo_ok', 'condiciones_ok', 'fase_ok', 'fase_propuesta', 'dominio_ok', 'dominio_propuesto', 'nota'] }
const LISTA = { type: 'object', properties: { items: { type: 'array', items: ITEM_R } }, required: ['items'] }
const QUE = 'aristas rancias tras las correcciones'
const lista = lote => `${W}${S}${P}${S}lotes${S}lote_${lote}.md`
const marcado = x => x.estado !== 'VIGENTE'
const clave = x => x.estado
function cazada(tipo, x) { return !!x && x.estado !== 'VIGENTE' }
function recall(trampas, porId) {
  const fallos = []; let n = 0
  for (const [id, tipo] of Object.entries(trampas)) { if (cazada(tipo, porId[id])) n++; else fallos.push(`${id} (${tipo})`) }
  return { total: Object.keys(trampas).length, cazadas: n, fallos }
}
function lector(lote, intento) {
  return limitado(() => agent(`Eres el LECTOR del lote ${lote} de un diagnostico de saneamiento del catalogo de My-idea (${QUE}).

TU LISTA: ${lista(lote)} (un bloque por nodo corregido, con sus aristas). Lee CADA bloque entero y juzga CADA arista, sin saltarte ninguna.
${VARA}
Devuelve TODAS las aristas (${args.lotes[lote].n}), cada una con su id (el de la arista, por ejemplo R01-01-02) y su estado.
${REGLAS}`, { label: `lector${P}:${lote}${intento > 1 ? ':r' + intento : ''}`, phase: 'Lectura', schema: LISTA }))
}
function verificador(lote, ids) {
  return limitado(() => agent(`Eres el VERIFICADOR CIEGO del lote ${lote} de un diagnostico de saneamiento del catalogo de My-idea (${QUE}). Otro lector ya midio estos nodos; tu no sabes que encontro. Midelos desde cero.

TU LISTA: las aristas de ${lista(lote)} cuyos ids son: ${ids.join(', ')}. Solo esas; lee el bloque entero de su nodo para cada una.
${VARA}
Devuelve todas las aristas de tu lista con su estado.
${REGLAS}`, { label: `verificador${P}:${lote}`, phase: 'Verificacion', schema: LISTA }))
}
function arbitro(lote, casos) {
  const txt = casos.map(c => `- ${c.id}: LECTOR A: ${JSON.stringify(c.a)} / LECTOR B: ${JSON.stringify(c.b)}`).join('\n')
  return limitado(() => agent(`Eres el ARBITRO del lote ${lote} de un diagnostico de saneamiento del catalogo de My-idea (${QUE}). Dos lectores independientes no coinciden. Decide releyendo el nodo, no sus razones.

LAS ARISTAS: estan en ${lista(lote)} (lee los bloques de sus nodos). Los desacuerdos:
${txt}
${VARA}
Devuelve todas las aristas en disputa con tu estado final; en el motivo di quien tenia razon y por que.
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
    const muestra = limpios.filter((_, i) => i % 6 === 0)
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
