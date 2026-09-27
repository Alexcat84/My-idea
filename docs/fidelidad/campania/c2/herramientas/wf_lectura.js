export const meta = {
  name: 'fidelidad-campania-lectura',
  description: 'Campania de fidelidad: lector especialista por lote con trampas, verificador ciego y arbitro; los agentes solo leen y devuelven datos',
  phases: [
    { title: 'Lectura', detail: 'un lector especialista por lote clasifica cada paso' },
    { title: 'Verificacion', detail: 'verificador ciego de lo no FIEL mas una muestra de FIEL' },
    { title: 'Arbitraje', detail: 'un arbitro relee los desacuerdos' },
  ],
}
const W = args.W
const S = '\\\\'
if (!args.lotes || typeof args.lotes !== 'object' || Array.isArray(args.lotes)) throw new Error('args.lotes debe ser {lote: {n, trampas}}')
const VARA = `LA VARA DEL FUNDADOR (cuatro veredictos, literal):
- FIEL: el libro dice ese paso, literal o parafraseado, sin anadir accion, objeto ni condicion que el libro no ponga.
- OPERATIVO (INFERIDO-OPERATIVO): concreta lo que el libro dice, en su misma direccion, sin datos nuevos.
- ANADIDO (INFERIDO-ANADIDO): afirma algo concreto que el libro no respalda (una cifra, un plazo, una herramienta, un responsable, una norma, una frecuencia).
- CONTRARIO: el paso aconseja lo que el libro desaconseja o contradice, o invierte lo que el texto sostiene.
REGLAS DE PRUEBA:
- CONTRARIO exige una cita del libro que diga lo opuesto o lo desaconseje. Antes de marcarlo, busca con Grep en TODO el libro pasajes que APOYEN el paso; si alguno lo apoya, no es CONTRARIO. Que el libro no lo diga no basta: eso es INFERIDO.
- ANADIDO exige haber buscado el dato con Grep en TODO el libro (ingles y espanol, variantes, cifras en letra y numero) sin encontrarlo. Si el libro da otro valor para ese mismo dato (otro umbral, distancia, plazo), eso es CONTRARIO, no ANADIDO.
- Antes de marcar OPERATIVO, ANADIDO o CONTRARIO, localiza el pasaje del libro que trata ese paso; no juzgues de memoria.
- Un umbral, distancia, plazo o secuencia cambiados respecto al libro son CONTRARIO aunque la accion general sea correcta.
TEXTOS QUE DEBES PROPONER (el fundador decide por regla con ellos):
- CONTRARIO: texto_fiel, el paso reescrito para decir lo que dice el libro.
- ANADIDO: tipo_anadido LEGAL_CIFRA si el dato es una cifra, un plazo, una norma o materia legal; PRACTICO si es una herramienta, una frecuencia o un formato. En LEGAL_CIFRA, texto_fiel quita el dato o lo reemplaza por lo que dice el libro. En PRACTICO, texto_sugerencia reescribe el paso como sugerencia de My Idea, empezando exactamente por "Sugerencia de My Idea: ", sin atribuirlo al autor ni al libro.
- OPERATIVO: no hace falta texto; se queda como esta.
- Todo texto propuesto: en el idioma, tono y longitud del paso; sin guiones largos ni medios; si nombra una sigla de un pais (FDA, OSHA, IRS...), anade "o la autoridad equivalente en tu mercado".`
const REGLAS = `ERES SOLO LECTOR: no escribas, crees ni borres ningun fichero en ningun sitio; devuelve todo en tu respuesta. PROHIBIDO, porque rompe la ceguera de la prueba: abrir cualquier cosa bajo ${W}${S}c2${S}claves o ${W}${S}c2${S}trampas, o de ${W}${S}salidas; abrir dataset/ o docs/ de cualquier clon de My-idea; ejecutar git. Lees tu lista y el libro de cada fila, y nada mas. No lances subagentes. Escribe en espanol y sin guiones largos (U+2014) ni medios (U+2013); una raya del libro se transcribe como --.`
const ITEM = { type: 'object', properties: {
  id: { type: 'string' }, veredicto: { type: 'string', enum: ['FIEL', 'OPERATIVO', 'ANADIDO', 'CONTRARIO'] },
  lineas: { type: 'string', description: 'rango del pasaje principal del libro, formato L123-L130' },
  frase_clave: { type: 'string', description: 'frase literal del libro que decide el veredicto' },
  dato: { type: 'string', description: 'en ANADIDO o CONTRARIO: el dato del paso que el libro no respalda o contradice' },
  tipo_anadido: { type: 'string', enum: ['LEGAL_CIFRA', 'PRACTICO', ''] },
  texto_fiel: { type: 'string' }, texto_sugerencia: { type: 'string' },
  razon: { type: 'string' } }, required: ['id', 'veredicto', 'lineas', 'frase_clave', 'razon'] }
const LISTA = { type: 'object', properties: { items: { type: 'array', items: ITEM } }, required: ['items'] }

function lector(lote, intento) {
  return limitado(() => agent(`Eres el LECTOR ESPECIALISTA del lote ${lote} de la campania de fidelidad del catalogo de My-idea. Mandato del fundador: nunca le diremos a un cliente lo contrario de lo que dice su fuente.

TU LISTA: ${W}${S}c2${S}lotes${S}lote_${lote}.md (id, titulo del nodo, resumen del nodo, numero de paso, texto del paso, fichero del libro). Clasifica CADA fila, sin saltarte ninguna, contra el libro de su fila (solo lectura).
${VARA}
Para CADA paso devuelve id, veredicto, rango de lineas del pasaje principal, frase clave literal y razon breve; y en los no FIEL, el dato y los textos que pide la vara.
${REGLAS}
Devuelve la lista completa (${args.lotes[lote].n} filas).`, { label: `lector:${lote}${intento > 1 ? ':r' + intento : ''}`, phase: 'Lectura', schema: LISTA }))
}

function verificador(lote, ids) {
  return limitado(() => agent(`Eres el VERIFICADOR CIEGO del lote ${lote} de la campania de fidelidad del catalogo de My-idea. Otro lector ya clasifico estos pasos; tu no sabes como. Clasificalos desde cero, releyendo el libro. En los CONTRARIOS, tu texto_fiel es el que se aplicara: que sea exacto al libro.

TU LISTA: las filas de ${W}${S}c2${S}lotes${S}lote_${lote}.md cuyos ids son: ${ids.join(', ')}. Solo esas.
${VARA}
${REGLAS}
Devuelve todos los pasos de tu lista con sus campos.`, { label: `verificador:${lote}`, phase: 'Verificacion', schema: LISTA }))
}

function arbitro(lote, casos) {
  const txt = casos.map(c => `- ${c.id}: LECTOR A dice ${c.a.veredicto} (${c.a.lineas}: "${c.a.frase_clave}"; ${c.a.razon}) / LECTOR B dice ${c.b.veredicto} (${c.b.lineas}: "${c.b.frase_clave}"; ${c.b.razon})`).join('\n')
  return limitado(() => agent(`Eres el ARBITRO del lote ${lote} de la campania de fidelidad del catalogo de My-idea. Dos lectores independientes no coinciden. Decide releyendo el LIBRO, no sus razones: comprueba cada cita y busca en todo el libro lo que ninguno vio.

LOS PASOS: sus filas estan en ${W}${S}c2${S}lotes${S}lote_${lote}.md (lee solo esas). Los desacuerdos:
${txt}
${VARA}
${REGLAS}
Devuelve todos los pasos en disputa con su veredicto final, lineas, frase clave, razon (di quien tenia razon y por que) y los textos que pide la vara.`, { label: `arbitro:${lote}`, phase: 'Arbitraje', schema: LISTA }))
}

function recall(trampas, porId) {
  let cazadas = 0, detectadas = 0; const fallos = []
  for (const [id, tipo] of Object.entries(trampas)) {
    const v = porId[id] ? porId[id].veredicto : 'FIEL'
    if (v === tipo) cazadas++
    if (v === 'ANADIDO' || v === 'CONTRARIO') detectadas++
    else fallos.push(`${id} (${tipo}, leido ${v})`)
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
      historial.push({ intento, pasos: Object.keys(porId).length, esperados: n, recall: r })
      log(`${lote} lectura ${intento}: ${Object.keys(porId).length}/${n} pasos, trampas ${r.detectadas}/${r.total}`)
      if (Object.keys(porId).length >= n && r.detectadas === r.total) break
      if (intento >= 2) { log(`${lote}: tras 2 lecturas sigue incompleto o con trampas sin cazar: ${r.fallos.join('; ')}`); break }
      intento++; lec = await lector(lote, intento)
    }
    return { lote, lec, historial }
  },
  async ({ lote, lec, historial }) => {
    const noFiel = lec.items.filter(x => x.veredicto !== 'FIEL').map(x => x.id)
    const fiel = lec.items.filter(x => x.veredicto === 'FIEL').map(x => x.id)
    const muestraFiel = fiel.filter((_, i) => i % 6 === 0)
    const ver = await verificador(lote, [...noFiel, ...muestraFiel].sort())
    return { lote, lec, historial, ver, muestraFiel }
  },
  async ({ lote, lec, historial, ver, muestraFiel }) => {
    const trampas = args.lotes[lote].trampas
    const A = Object.fromEntries(lec.items.map(x => [x.id, x]))
    const B = Object.fromEntries(((ver && ver.items) || []).map(x => [x.id, x]))
    const recallVerif = recall(Object.fromEntries(Object.entries(trampas).filter(([id]) => B[id])), B)
    const casos = Object.keys(B).filter(id => !trampas[id] && A[id] && A[id].veredicto !== B[id].veredicto).map(id => ({ id, a: A[id], b: B[id] }))
    const arb = casos.length ? await arbitro(lote, casos) : { items: [] }
    const C = Object.fromEntries(((arb && arb.items) || []).map(x => [x.id, x]))
    const final = []
    for (const id of Object.keys(A)) {
      if (trampas[id]) continue
      if (C[id]) final.push({ ...C[id], decidido_por: 'arbitro', lector: A[id].veredicto, verificador: B[id].veredicto })
      else if (B[id]) final.push({ ...B[id], decidido_por: 'lector y verificador de acuerdo', lector: A[id].veredicto, verificador: B[id].veredicto })
      else final.push({ ...A[id], decidido_por: 'lector (FIEL no muestreado)', lector: A[id].veredicto })
    }
    const cuenta = {}
    for (const x of final) cuenta[x.veredicto] = (cuenta[x.veredicto] || 0) + 1
    const fielMuestra = muestraFiel.filter(id => !trampas[id])
    const fielCambiados = fielMuestra.filter(id => { const f = final.find(x => x.id === id); return f && f.veredicto !== 'FIEL' })
    log(`${lote}: ${JSON.stringify(cuenta)}; desacuerdos ${casos.length}; FIEL muestreados ${fielMuestra.length}, cambiados ${fielCambiados.length}; trampas del verificador ${recallVerif.detectadas}/${recallVerif.total}`)
    return { lote, historial, recallVerificador: recallVerif, desacuerdos: casos.length, fielMuestreados: fielMuestra.length, fielCambiados, cuenta, final }
  })
return resultados.filter(Boolean)
