export const meta = {
  name: 'etiquetas-lectura',
  description: 'Pasada de fidelidad sobre las 3.169 etiquetas de cara contra el titulo y el resumen de su nodo: lector con trampas, verificador ciego y arbitro, solo CONTRARIAS y DISTINTAS; los agentes solo leen',
  phases: [
    { title: 'Lectura', detail: 'un lector por lote' },
    { title: 'Verificacion', detail: 'verificador ciego de las etiquetas marcadas mas una muestra de las limpias' },
    { title: 'Arbitraje', detail: 'un arbitro relee los desacuerdos' },
  ],
}
const W = args.W
const S = '\\\\'
if (!args.lotes || typeof args.lotes !== 'object' || Array.isArray(args.lotes)) throw new Error('args.lotes debe ser {lote: {n, trampas}}')
const VARA = `QUE ES UNA ETIQUETA DE CARA: el nombre corto que el usuario ve en el riel para cada concepto del catalogo (imperativo en tuteo, maximo 6 palabras, sin jerga inglesa ni siglas: la casa traduce los nombres tecnicos por su funcion).

QUE BUSCAS, Y SOLO ESTO (mandato del fundador): etiquetas que dicen lo CONTRARIO o algo DISTINTO del concepto de su nodo, juzgado contra el TITULO y el RESUMEN del nodo:
- CONTRARIA: la etiqueta pide o afirma lo opuesto a lo que el nodo ensena: invierte quien hace que (el nodo dice que los inversionistas bajan la valoracion y la etiqueta pide al usuario bajarla), invierte el sentido (subir o bajar, hacer o evitar, antes o despues, presente o futuro, uno u otro), o niega lo que el concepto afirma ("sin lucro" cuando el concepto va "mas alla del lucro").
- DISTINTA: la etiqueta nombra otra accion, otro objeto u otro concepto que el nodo NO trata, de modo que quien la lea espera algo que el nodo no ensena.
NO SON HALLAZGOS, y NO debes reportarlos: una etiqueta general o vaga que cubre el concepto; una que nombra solo una parte, un paso o el proposito del nodo; la traduccion por funcion de un nombre tecnico ("Recorre el Ciclo de Aprendizaje" por construir, medir y aprender es correcta); el tuteo y el imperativo de la casa; una metafora que apunta en la direccion del concepto; una etiqueta mejorable de estilo. Solo el error de SENTIDO. En la duda, no es hallazgo.
POR CADA HALLAZGO: veredicto (CONTRARIA o DISTINTA), que_dice (lo que promete la etiqueta), que_ensena_el_nodo, cita (un fragmento LITERAL del titulo o del resumen, copiado caracter a caracter, que muestra el error), etiqueta_propuesta (fiel al titulo y al resumen, maximo 6 palabras, imperativo en tuteo, en Title Case como las demas, con sus tildes, sin jerga inglesa: canvas, pivot, equity, feedback, lead, benchmark, onboarding, pitch, lean, prompt, startup, funnel, scorecard, mvp, kpi; sin siglas) y razon breve.`
const REGLAS = `ERES SOLO LECTOR: no escribas, crees ni borres ningun fichero en ningun sitio; devuelve todo en tu respuesta. PROHIBIDO, porque rompe la ceguera de la prueba: abrir cualquier cosa bajo ${W}${S}claves, ${W}${S}reales, ${W}${S}trampas.json, ${W}${S}bases_trampa.json o cualquier otro fichero de ${W} que no sea tu lista; abrir dataset/ o docs/ de cualquier clon de My-idea; ejecutar git. Lees tu lista y nada mas. No lances subagentes. Escribe en espanol y sin guiones largos (U+2014) ni medios (U+2013).`
const HALLAZGO = { type: 'object', properties: {
  veredicto: { type: 'string', enum: ['CONTRARIA', 'DISTINTA'] }, que_dice: { type: 'string' }, que_ensena_el_nodo: { type: 'string' },
  cita: { type: 'string' }, etiqueta_propuesta: { type: 'string' }, razon: { type: 'string' } },
  required: ['veredicto', 'que_dice', 'que_ensena_el_nodo', 'cita', 'etiqueta_propuesta', 'razon'] }
const ITEM = { type: 'object', properties: { id: { type: 'string' }, hallazgos: { type: 'array', items: HALLAZGO } }, required: ['id', 'hallazgos'] }
const LISTA = { type: 'object', properties: { items: { type: 'array', items: ITEM } }, required: ['items'] }
const lista = lote => `${W}${S}lotes${S}lote_${lote}.md`

function lector(lote, intento) {
  return limitado(() => agent(`Eres el LECTOR ESPECIALISTA del lote ${lote} de una pasada de fidelidad sobre las etiquetas de cara del catalogo de My-idea. Mandato del fundador: la etiqueta nunca le dira al usuario lo contrario, ni otra cosa, que el concepto que hay detras.

TU LISTA: ${lista(lote)} (un bloque por nodo: id, titulo, resumen y ETIQUETA). Lee CADA bloque, sin saltarte ninguno, y juzga la ETIQUETA contra el titulo y el resumen de su bloque.
${VARA}
Devuelve TODOS los bloques (${args.lotes[lote].n}), cada uno con su id y su lista de hallazgos (vacia si no hay ninguno; como mucho un hallazgo por etiqueta).
${REGLAS}`, { label: `lector:${lote}${intento > 1 ? ':r' + intento : ''}`, phase: 'Lectura', schema: LISTA }))
}

function verificador(lote, ids) {
  return limitado(() => agent(`Eres el VERIFICADOR CIEGO del lote ${lote} de una pasada de fidelidad sobre las etiquetas de cara del catalogo de My-idea. Otro lector ya leyo estas etiquetas; tu no sabes que encontro. Juzgalas desde cero. Si hay hallazgo, tu etiqueta_propuesta es candidata a aplicarse: que sea exacta al concepto.

TU LISTA: los bloques de ${lista(lote)} cuyos ids son: ${ids.join(', ')}. Solo esos.
${VARA}
Devuelve todos los bloques de tu lista, cada uno con su lista de hallazgos (vacia si no hay ninguno; como mucho uno por etiqueta).
${REGLAS}`, { label: `verificador:${lote}`, phase: 'Verificacion', schema: LISTA }))
}

function arbitro(lote, casos) {
  const fmt = hs => hs.length ? hs.map(h => `${h.veredicto} ("${h.cita}"; ${h.razon}; propone "${h.etiqueta_propuesta}")`).join(' ; ') : 'ningun hallazgo'
  const txt = casos.map(c => `- ${c.id}: LECTOR A: ${fmt(c.a)} / LECTOR B: ${fmt(c.b)}`).join('\n')
  return limitado(() => agent(`Eres el ARBITRO del lote ${lote} de una pasada de fidelidad sobre las etiquetas de cara del catalogo de My-idea. Dos lectores independientes no coinciden. Decide releyendo el titulo y el resumen de cada bloque, no sus razones: comprueba cada cita.

LOS BLOQUES: estan en ${lista(lote)} (lee solo los de estos ids). Los desacuerdos:
${txt}
${VARA}
Devuelve todos los bloques en disputa con su lista final de hallazgos (vacia si no hay ninguno; como mucho uno por etiqueta); en la razon di quien tenia razon y por que.
${REGLAS}`, { label: `arbitro:${lote}`, phase: 'Arbitraje', schema: LISTA }))
}

const clave = hs => (hs || []).map(h => h.veredicto).sort().join('|')
function recall(trampas, porId) {
  let cazadas = 0, detectadas = 0; const fallos = []
  for (const [id, tipo] of Object.entries(trampas)) {
    const hs = porId[id] ? porId[id].hallazgos : []
    if (hs.some(h => h.veredicto === tipo)) cazadas++
    if (hs.length) detectadas++
    else fallos.push(`${id} (${tipo}, sin hallazgo)`)
  }
  return { total: Object.keys(trampas).length, cazadas, detectadas, fallos }
}

const CONC = args.conc || 6
let activos = 0
const cola = []
async function limitado(fn) {
  if (activos >= CONC) await new Promise(r => cola.push(r))
  activos++
  try { return await fn() } finally { activos--; const sig = cola.shift(); if (sig) sig() }
}
const LOTES = Object.keys(args.lotes)
const resultados = await pipeline(LOTES,
  async (lote) => {
    const n = args.lotes[lote].n, trampas = args.lotes[lote].trampas
    let lec = await lector(lote, 1), intento = 1
    const historial = []
    for (;;) {
      if (!lec) throw new Error('lector sin resultado en ' + lote)
      const porId = Object.fromEntries(lec.items.map(x => [x.id, x]))
      const r = recall(trampas, porId)
      historial.push({ intento, bloques: Object.keys(porId).length, esperados: n, recall: r })
      log(`${lote} lectura ${intento}: ${Object.keys(porId).length}/${n} bloques, trampas ${r.detectadas}/${r.total}`)
      if (Object.keys(porId).length >= n && r.detectadas === r.total) break
      if (intento >= 2) { log(`${lote}: tras 2 lecturas sigue incompleto o con trampas sin cazar: ${r.fallos.join('; ')}`); break }
      intento++; lec = await lector(lote, intento)
    }
    return { lote, lec, historial }
  },
  async ({ lote, lec, historial }) => {
    const con = lec.items.filter(x => x.hallazgos.length).map(x => x.id)
    const limpios = lec.items.filter(x => !x.hallazgos.length).map(x => x.id)
    const muestra = limpios.filter((_, i) => i % 6 === 0)
    const ver = await verificador(lote, [...con, ...muestra].sort())
    return { lote, lec, historial, ver, muestra }
  },
  async ({ lote, lec, historial, ver, muestra }) => {
    const trampas = args.lotes[lote].trampas
    const A = Object.fromEntries(lec.items.map(x => [x.id, x.hallazgos]))
    const B = Object.fromEntries(((ver && ver.items) || []).map(x => [x.id, x.hallazgos]))
    const recallVerif = recall(Object.fromEntries(Object.entries(trampas).filter(([id]) => B[id])), Object.fromEntries(Object.entries(B).map(([k, v]) => [k, { hallazgos: v }])))
    const casos = Object.keys(B).filter(id => !trampas[id] && A[id] && clave(A[id]) !== clave(B[id])).map(id => ({ id, a: A[id], b: B[id] }))
    const arb = casos.length ? await arbitro(lote, casos) : { items: [] }
    const C = Object.fromEntries(((arb && arb.items) || []).map(x => [x.id, x.hallazgos]))
    const final = []
    for (const id of Object.keys(A)) {
      if (trampas[id]) continue
      if (C[id]) final.push({ id, hallazgos: C[id], decidido_por: 'arbitro', lector: A[id], verificador: B[id] })
      else if (B[id]) final.push({ id, hallazgos: B[id], decidido_por: 'lector y verificador de acuerdo', lector: A[id] })
      else final.push({ id, hallazgos: A[id], decidido_por: 'lector (limpio no muestreado)' })
    }
    const conHallazgo = final.filter(x => x.hallazgos.length).length
    const muestraCambiada = muestra.filter(id => !trampas[id]).filter(id => { const f = final.find(x => x.id === id); return f && f.hallazgos.length })
    log(`${lote}: ${final.length} etiquetas, ${conHallazgo} con hallazgo; desacuerdos ${casos.length}; limpias muestreadas ${muestra.length}, con hallazgo tras verificar ${muestraCambiada.length}; trampas del verificador ${recallVerif.detectadas}/${recallVerif.total}`)
    return { lote, historial, recallVerificador: recallVerif, desacuerdos: casos.length, muestreados: muestra.length, muestraCambiada, final }
  })
return resultados.filter(Boolean)