export const meta = {
  name: 'fidelidad-campos-lectura',
  description: 'Pasada contra la fuente sobre titulo, etiqueta, resumen, entregable y condiciones: lector con trampas, verificador ciego y arbitro, solo CONTRARIOS y ANADIDOS de cifra, plazo o norma; los agentes solo leen',
  phases: [
    { title: 'Lectura', detail: 'un lector especialista por lote' },
    { title: 'Verificacion', detail: 'verificador ciego de los nodos con hallazgo mas una muestra de los limpios' },
    { title: 'Arbitraje', detail: 'un arbitro relee los desacuerdos' },
  ],
}
const W = args.W
const S = '\\\\'
if (!args.lotes || typeof args.lotes !== 'object' || Array.isArray(args.lotes)) throw new Error('args.lotes debe ser {lote: {n, trampas}}')
const VARA = `QUE BUSCAS, Y SOLO ESTO (mandato del fundador): en los campos titulo, etiqueta, resumen, entregable y condiciones de cada nodo, dos clases de error frente a su libro:
- CONTRARIO: el campo dice lo opuesto a lo que sostiene el libro, lo desaconseja o lo invierte; o cambia un umbral, una cifra, un plazo, una distancia, una secuencia o una consecuencia que el libro da (aunque el sentido general sea correcto).
- ANADIDO (de cifra, plazo o norma): el campo afirma una cifra, un porcentaje, un plazo, una frecuencia numerica, una norma, una ley, un requisito legal o regulatorio concretos que el libro NO da.
NO son hallazgos, y NO debes reportarlos: la parafrasis, la sintesis, el lenguaje de My Idea (idea, proyecto, tu), las condiciones de activacion que describen cuando aplica el concepto a quien emprende (son de My Idea, salvo que afirmen algo contrario al libro o una cifra o norma que el libro no da), los ejemplos practicos sin cifra ni norma, las herramientas, y cualquier concrecion en la direccion del libro.
REGLAS DE PRUEBA:
- CONTRARIO exige una cita literal del libro que diga lo opuesto. Antes de marcarlo, busca con Grep en TODO el libro pasajes que APOYEN el campo; si alguno lo apoya, no es CONTRARIO.
- ANADIDO exige haber buscado el dato con Grep en TODO el libro (ingles y espanol, variantes, cifras en letra y numero) sin encontrarlo. Si el libro da otro valor para ese mismo dato, es CONTRARIO.
- Localiza el pasaje del libro que trata el campo; no juzgues de memoria.
POR CADA HALLAZGO: campo (titulo, etiqueta, resumen, entregable o condiciones), indice (el numero de la condicion; 0 en los demas campos), veredicto, fragmento (el trozo EXACTO del campo que esta mal, copiado caracter a caracter), dato (que afirma y que dice el libro), lineas (L123-L130), frase_clave (literal del libro), texto_fiel (el CAMPO ENTERO reescrito: en CONTRARIO diciendo lo que dice el libro; en ANADIDO quitando el dato o poniendo el que da el libro; mismo idioma, tono y longitud, sin guiones largos ni medios; si nombra una sigla de un pais, anade "o la autoridad equivalente en tu mercado") y razon breve.`
const REGLAS = `ERES SOLO LECTOR: no escribas, crees ni borres ningun fichero en ningun sitio; devuelve todo en tu respuesta. PROHIBIDO, porque rompe la ceguera de la prueba: abrir cualquier cosa bajo ${W}${S}c2${S}claves o ${W}${S}c2${S}trampas; abrir dataset/ o docs/ de cualquier clon de My-idea; ejecutar git. Lees tu lista y el libro de cada nodo, y nada mas. No lances subagentes. Escribe en espanol y sin guiones largos (U+2014) ni medios (U+2013); una raya del libro se transcribe como --.`
const HALLAZGO = { type: 'object', properties: {
  campo: { type: 'string', enum: ['titulo', 'etiqueta', 'resumen', 'entregable', 'condiciones'] }, indice: { type: 'integer' },
  veredicto: { type: 'string', enum: ['CONTRARIO', 'ANADIDO'] }, fragmento: { type: 'string' }, dato: { type: 'string' },
  lineas: { type: 'string' }, frase_clave: { type: 'string' }, texto_fiel: { type: 'string' }, razon: { type: 'string' } },
  required: ['campo', 'indice', 'veredicto', 'fragmento', 'dato', 'lineas', 'frase_clave', 'texto_fiel', 'razon'] }
const ITEM = { type: 'object', properties: { id: { type: 'string' }, hallazgos: { type: 'array', items: HALLAZGO } }, required: ['id', 'hallazgos'] }
const LISTA = { type: 'object', properties: { items: { type: 'array', items: ITEM } }, required: ['items'] }

function lector(lote, intento) {
  return limitado(() => agent(`Eres el LECTOR ESPECIALISTA del lote ${lote} de una pasada de fidelidad del catalogo de My-idea. Mandato del fundador: nunca le diremos a un cliente lo contrario de lo que dice su fuente.

TU LISTA: ${W}${S}c2${S}lotes${S}lote_${lote}.md (un bloque por nodo: id, fichero del libro, titulo, etiqueta, resumen, entregable y condiciones). Lee CADA nodo, sin saltarte ninguno, contra el libro de su bloque (solo lectura).
${VARA}
Devuelve TODOS los nodos (${args.lotes[lote].n}), cada uno con su id y su lista de hallazgos (vacia si no hay ninguno).
${REGLAS}`, { label: `lector:${lote}${intento > 1 ? ':r' + intento : ''}`, phase: 'Lectura', schema: LISTA }))
}

function verificador(lote, ids) {
  return limitado(() => agent(`Eres el VERIFICADOR CIEGO del lote ${lote} de una pasada de fidelidad del catalogo de My-idea. Otro lector ya leyo estos nodos; tu no sabes que encontro. Leelos desde cero contra el libro. En los CONTRARIOS, tu texto_fiel es el que se aplicara: que sea exacto al libro.

TU LISTA: los bloques de ${W}${S}c2${S}lotes${S}lote_${lote}.md cuyos ids son: ${ids.join(', ')}. Solo esos.
${VARA}
Devuelve todos los nodos de tu lista, cada uno con su lista de hallazgos (vacia si no hay ninguno).
${REGLAS}`, { label: `verificador:${lote}`, phase: 'Verificacion', schema: LISTA }))
}

function arbitro(lote, casos) {
  const fmt = hs => hs.length ? hs.map(h => `${h.veredicto} en ${h.campo}[${h.indice}] ("${h.fragmento}"; ${h.lineas}: "${h.frase_clave}"; ${h.razon})`).join(' ; ') : 'ningun hallazgo'
  const txt = casos.map(c => `- ${c.id}: LECTOR A: ${fmt(c.a)} / LECTOR B: ${fmt(c.b)}`).join('\n')
  return limitado(() => agent(`Eres el ARBITRO del lote ${lote} de una pasada de fidelidad del catalogo de My-idea. Dos lectores independientes no coinciden. Decide releyendo el LIBRO, no sus razones: comprueba cada cita y busca en todo el libro lo que ninguno vio.

LOS NODOS: sus bloques estan en ${W}${S}c2${S}lotes${S}lote_${lote}.md (lee solo esos). Los desacuerdos:
${txt}
${VARA}
Devuelve todos los nodos en disputa con su lista final de hallazgos (vacia si no hay ninguno); en la razon de cada hallazgo di quien tenia razon y por que.
${REGLAS}`, { label: `arbitro:${lote}`, phase: 'Arbitraje', schema: LISTA }))
}

const clave = hs => (hs || []).map(h => `${h.campo}:${h.campo === 'condiciones' ? h.indice : 0}:${h.veredicto}`).sort().join('|')
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
      historial.push({ intento, nodos: Object.keys(porId).length, esperados: n, recall: r })
      log(`${lote} lectura ${intento}: ${Object.keys(porId).length}/${n} nodos, trampas ${r.detectadas}/${r.total}`)
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
      else if (B[id]) final.push({ id, hallazgos: B[id], decidido_por: 'lector y verificador de acuerdo' })
      else final.push({ id, hallazgos: A[id], decidido_por: 'lector (limpio no muestreado)' })
    }
    const conHallazgo = final.filter(x => x.hallazgos.length).length
    const muestraCambiada = muestra.filter(id => !trampas[id]).filter(id => { const f = final.find(x => x.id === id); return f && f.hallazgos.length })
    log(`${lote}: ${final.length} nodos, ${conHallazgo} con hallazgo; desacuerdos ${casos.length}; limpios muestreados ${muestra.length}, con hallazgo tras verificar ${muestraCambiada.length}; trampas del verificador ${recallVerif.detectadas}/${recallVerif.total}`)
    return { lote, historial, recallVerificador: recallVerif, desacuerdos: casos.length, muestreados: muestra.length, muestraCambiada, final }
  })
return resultados.filter(Boolean)
