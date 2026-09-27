export const meta = {
  name: 'saneamiento-J-lectura',
  description: 'Diagnostico de saneamiento, pasada de VIGENCIA y JURISDICCION: lector con trampas, verificador ciego y arbitro; solo mide, no corrige; los agentes solo leen',
  phases: [
    { title: 'Lectura', detail: 'un lector por lote' },
    { title: 'Verificacion', detail: 'verificador ciego de los nodos con pais o clase mas una muestra de los limpios' },
    { title: 'Arbitraje', detail: 'un arbitro relee los desacuerdos' },
  ],
}
const W = args.W
const S = '\\\\'
if (!args.lotes || typeof args.lotes !== 'object' || Array.isArray(args.lotes)) throw new Error('args.lotes debe ser {lote: {n, trampas}}')
const VARA = `CONTEXTO: My-idea es un catalogo de nodos de guia para emprender, en espanol, para usuarios de CUALQUIER pais. La casa tiene una POLITICA DE PAIS acordada en agosto de 2026 ("marco contra pais"):
- CLASE A, INTOCABLE: vocabulario o tratado INTERNACIONAL acordado entre paises (Incoterms, carta de credito, conocimiento de embarque, codigos arancelarios, clausula antidesviacion, PCT y Protocolo de Madrid, convenios de la ONU). Se queda, con su vigencia.
- CLASE B, REENCUADRE: el ejemplo es de un pais pero la clase existe en casi todos; el nodo lo dice y manda buscar lo del propio pais ("en EE.UU. son estas; averigua las de tu pais", "o el organismo equivalente en tu mercado").
- CLASE C, NODO-FRONTERA: una ley con alcance real que obliga a quien caiga bajo ella; el nodo la CONDICIONA de forma explicita, al frente o en sus condiciones ("si vendes a EE.UU.", "solo si tu negocio opera en Estados Unidos").
- Lo que es solo programa de un gobierno lleva condicion de pais (la politica de pais de agosto revirtio su deprecacion).
- Dos reglas: la cifra de MERCADO (un precio, una tarifa de mercado) sale del nodo; la cifra que ES LA NORMA se queda, en su nodo-frontera. Contratar, nomina y despido van como METODO, nunca como norma de un pais.

QUE MIDES EN CADA NODO (solo mides, no corriges nada):
1. clase_pais: una de estas
   - SIN_PAIS: el nodo no tiene contenido propio de ningun pais.
   - A, B o C: tiene contenido de un pais y esta tratado segun esa clase (A por ser vocabulario o tratado internacional; B porque reencuadra y manda buscar lo propio; C porque lleva la condicion explicita de pais).
   - SIN_CLASE: tiene contenido propio de un pais (una ley, un organismo, un programa, una obligacion, un tramite, una cifra legal de ese pais) escrito como si valiera para todos, sin condicion y sin reencuadre. Tambien SIN_CLASE si el tratamiento es incoherente (por ejemplo, una condicion de solo EE.UU. y a la vez "o el equivalente en tu mercado" sobre lo mismo): dilo en la nota.
2. paises: cada pais cuyo contenido propio aparece, con el fragmento literal.
3. dependencias: lo que CADUCA o puede cambiar con el tiempo, cada una con su tipo y el fragmento literal: norma (ley, reglamento, estandar con version), plazo_legal (un plazo que impone una norma), cifra_datada (una cifra con fecha o de un ano concreto, un umbral legal, una tasa vigente), institucion (un organismo o entidad concreta nombrada como recurso u obligacion), enlace (una web o URL), importe_mercado (un precio o costo de mercado). NO son dependencias: las siglas de metodos de gestion (KPI, ROI, FODA, DMAIC, PDCA, SIPOC, OKR), las normas ISO citadas como marco de metodo sin plazo ni obligacion, ni los nombres de autores o libros.
4. banderas: programa_gobierno (describe un programa de un gobierno concreto), cifra_mercado (trae un precio o costo de mercado), empleo_como_norma (trata contratar, nomina o despido como norma legal de un pais y no como metodo).
Lee el nodo entero (titulo, resumen, pasos, entregable y condiciones) y copia los fragmentos caracter a caracter.`
const REGLAS = `ERES SOLO LECTOR: no escribas, crees ni borres ningun fichero; devuelve todo en tu respuesta. PROHIBIDO, porque rompe la ceguera de la prueba: abrir cualquier fichero de ${W} que no sea tu lista; abrir dataset/, packs/ o docs/ de cualquier clon de My-idea o de la forja; ejecutar git. No lances subagentes. Escribe en espanol, sin guiones largos (U+2014) ni medios (U+2013).`
const PAIS = { type: 'object', properties: { pais: { type: 'string' }, fragmento: { type: 'string' } }, required: ['pais', 'fragmento'] }
const DEP = { type: 'object', properties: { tipo: { type: 'string', enum: ['norma', 'plazo_legal', 'cifra_datada', 'institucion', 'enlace', 'importe_mercado'] }, fragmento: { type: 'string' } }, required: ['tipo', 'fragmento'] }
const ITEM = { type: 'object', properties: {
  id: { type: 'string' }, clase_pais: { type: 'string', enum: ['SIN_PAIS', 'A', 'B', 'C', 'SIN_CLASE'] },
  paises: { type: 'array', items: PAIS }, dependencias: { type: 'array', items: DEP },
  programa_gobierno: { type: 'boolean' }, cifra_mercado: { type: 'boolean' }, empleo_como_norma: { type: 'boolean' }, nota: { type: 'string' } },
  required: ['id', 'clase_pais', 'paises', 'dependencias', 'programa_gobierno', 'cifra_mercado', 'empleo_como_norma', 'nota'] }
const LISTA = { type: 'object', properties: { items: { type: 'array', items: ITEM } }, required: ['items'] }
const lista = lote => `${W}${S}J${S}lotes${S}lote_${lote}.md`

function lector(lote, intento) {
  return limitado(() => agent(`Eres el LECTOR del lote ${lote} de un diagnostico de saneamiento del catalogo de My-idea (vigencia y jurisdiccion).

TU LISTA: ${lista(lote)} (un bloque por nodo). Lee CADA bloque entero, sin saltarte ninguno.
${VARA}
Devuelve TODOS los bloques (${args.lotes[lote].n}), cada uno con su id y su medida (listas vacias y banderas en false cuando no haya nada; nota vacia si no hace falta).
${REGLAS}`, { label: `lector:${lote}${intento > 1 ? ':r' + intento : ''}`, phase: 'Lectura', schema: LISTA }))
}
function verificador(lote, ids) {
  return limitado(() => agent(`Eres el VERIFICADOR CIEGO del lote ${lote} de un diagnostico de saneamiento del catalogo de My-idea (vigencia y jurisdiccion). Otro lector ya midio estos nodos; tu no sabes que encontro. Midelos desde cero.

TU LISTA: los bloques de ${lista(lote)} cuyos ids son: ${ids.join(', ')}. Solo esos, cada uno entero.
${VARA}
Devuelve todos los bloques de tu lista con su medida.
${REGLAS}`, { label: `verificador:${lote}`, phase: 'Verificacion', schema: LISTA }))
}
function arbitro(lote, casos) {
  const fmt = x => `clase ${x.clase_pais}; paises [${x.paises.map(p => p.pais).join(', ')}]; dependencias [${x.dependencias.map(d => d.tipo + ': ' + d.fragmento).join(' | ')}]; nota: ${x.nota}`
  const txt = casos.map(c => `- ${c.id}: LECTOR A: ${fmt(c.a)} / LECTOR B: ${fmt(c.b)}`).join('\n')
  return limitado(() => agent(`Eres el ARBITRO del lote ${lote} de un diagnostico de saneamiento del catalogo de My-idea (vigencia y jurisdiccion). Dos lectores independientes no coinciden. Decide releyendo el nodo, no sus razones.

LOS NODOS: sus bloques estan en ${lista(lote)} (lee solo los de estos ids). Los desacuerdos:
${txt}
${VARA}
Devuelve todos los nodos en disputa con tu medida final; en la nota di quien tenia razon y por que.
${REGLAS}`, { label: `arbitro:${lote}`, phase: 'Arbitraje', schema: LISTA }))
}

const tiposDe = x => [...new Set(x.dependencias.map(d => d.tipo))].sort().join(',')
const clave = x => `${x.clase_pais}|${x.clase_pais === 'SIN_PAIS' ? '' : [...new Set(x.paises.map(p => p.pais.toLowerCase()))].sort().join(',')}|${tiposDe(x)}`
function cazada(tipo, x) {
  if (!x) return false
  if (tipo === 'PAIS_SIN_CLASE') return x.clase_pais === 'SIN_CLASE'
  if (tipo === 'NORMA_O_PLAZO_DATADO') return x.dependencias.some(d => ['norma', 'plazo_legal', 'cifra_datada'].includes(d.tipo))
  return x.dependencias.some(d => ['enlace', 'institucion'].includes(d.tipo))
}
function recall(trampas, porId) {
  const fallos = []; let n = 0
  for (const [id, tipo] of Object.entries(trampas)) { if (cazada(tipo, porId[id])) n++; else fallos.push(`${id} (${tipo})`) }
  return { total: Object.keys(trampas).length, cazadas: n, fallos }
}
const CONC = args.conc || 5
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
      log(`${lote} lectura ${intento}: ${Object.keys(porId).length}/${n} bloques, trampas ${r.cazadas}/${r.total}`)
      if (Object.keys(porId).length >= n && r.cazadas === r.total) break
      if (intento >= 2) { log(`${lote}: tras 2 lecturas: ${r.fallos.join('; ')}`); break }
      intento++; lec = await lector(lote, intento)
    }
    return { lote, lec, historial }
  },
  async ({ lote, lec, historial }) => {
    const con = lec.items.filter(x => x.clase_pais !== 'SIN_PAIS' || x.dependencias.length).map(x => x.id)
    const limpios = lec.items.filter(x => x.clase_pais === 'SIN_PAIS' && !x.dependencias.length).map(x => x.id)
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
    const muestraCambiada = muestra.filter(id => !trampas[id] && C[id] && (C[id].clase_pais !== 'SIN_PAIS' || C[id].dependencias.length))
    log(`${lote}: ${final.length} nodos; desacuerdos ${casos.length}; limpias muestreadas ${muestra.length}, cambiadas ${muestraCambiada.length}; trampas del verificador ${recallVerif.cazadas}/${recallVerif.total}`)
    return { lote, historial, recallVerificador: recallVerif, desacuerdos: casos.length, muestreados: muestra.length, muestraCambiada, final }
  })
return resultados.filter(Boolean)
