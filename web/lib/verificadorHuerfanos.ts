/**
 * verificadorHuerfanos.ts - Fase 3.1 (caja de vidrio): port exacto de
 * engine/verificador_huerfanos.py. Automatiza la vara de auditoria
 * "ningun numero huerfano" que hasta ahora era un ritual manual. Extrae
 * todo numeral de un texto (el reporte completo, o la seccion financiera
 * del plan) y verifica que pertenezca al conjunto de numeros que de
 * verdad se le entregaron a quien narro: salidas de calculadora.ts (solo
 * aplica al reporte), numeros declarados por el usuario, y numerales
 * presentes en el texto de los nodos del material. Señal de triage para
 * revision humana, no un guardian que bloquee nada.
 */

const PATRON_NUMERO = /-?\$?\d[\d.,]*%?/g;

// Tolerancia absoluta para redondeos de narracion.
const TOLERANCIA = 0.05;

/** '$1.700' -> 1700, '-2976.9%' -> -2976.9, '17.5' -> 17.5. Heuristica de
 * tolerancia de formato (ejemplo mandatado '1.700 vs 1700'): un unico
 * punto seguido de EXACTAMENTE 3 digitos se interpreta como separador de
 * miles (estilo hispano), no como parte decimal. */
function normalizarNumero(token: string): number | null {
  let t = token.trim().replace(/\$/g, "").replace(/,/g, "");
  if (t.endsWith("%")) t = t.slice(0, -1);
  const partes = t.split(".");
  if (partes.length === 2 && partes[1].length === 3 && /^-?\d+$/.test(partes[0])) {
    t = partes[0] + partes[1];
  }
  const valor = Number(t);
  return Number.isFinite(valor) ? valor : null;
}

export interface NumeroEncontrado {
  valor: number;
  token: string;
  contexto: string;
}

export function extraerNumeros(texto: string): NumeroEncontrado[] {
  const encontrados: NumeroEncontrado[] = [];
  for (const m of (texto ?? "").matchAll(PATRON_NUMERO)) {
    const valor = normalizarNumero(m[0]);
    if (valor === null) continue;
    const inicio = Math.max(0, (m.index ?? 0) - 30);
    const fin = Math.min(texto.length, (m.index ?? 0) + m[0].length + 30);
    const contexto = texto.slice(inicio, fin).replace(/\n/g, " ").trim();
    encontrados.push({ valor, token: m[0], contexto });
  }
  return encontrados;
}

/** Recorre cualquier estructura anidada (objeto/array) y devuelve el
 * conjunto de valores numericos hoja, ignorando null/string/boolean. */
function numerosDeEstructura(obj: unknown): Set<number> {
  const numeros = new Set<number>();
  if (typeof obj === "boolean") return numeros;
  if (typeof obj === "number" && Number.isFinite(obj)) {
    numeros.add(Math.round(obj * 10000) / 10000);
  } else if (Array.isArray(obj)) {
    for (const v of obj) for (const n of numerosDeEstructura(v)) numeros.add(n);
  } else if (obj && typeof obj === "object") {
    for (const [k, v] of Object.entries(obj)) {
      // Fase 3.1: escenarios de adopcion usan claves como '50%'/'100%' --
      // un numero en una CLAVE (no solo en un valor) tambien cuenta como
      // legitimo, o narrarla ("al 50% de tu meta") se marcaria como
      // huerfano por error.
      const valorClave = normalizarNumero(k);
      if (valorClave !== null) numeros.add(Math.round(valorClave * 10000) / 10000);
      for (const n of numerosDeEstructura(v)) numeros.add(n);
    }
  }
  return numeros;
}

export function numerosDeCalculadora(resultadosCalculadora: unknown): Set<number> {
  return numerosDeEstructura(resultadosCalculadora);
}

export function numerosDeclarados(numerosProyecto: unknown): Set<number> {
  return numerosDeEstructura(numerosProyecto ?? {});
}

/** Fase 3.1: un narrador que solo describe salidas YA calculadas igual
 * hace aritmetica simple de un paso (sumas/restas) para dar contexto
 * util -- ej. 'a partir del usuario 17 ya es ganancia' cuando el
 * equilibrio calculado es 16, 'te quedan $60' cuando ingreso=260 y
 * costos_fijos=200, o 'con 20 usuarios son $260' cuando precio=13. Eso
 * no es fabricar cifras, es narrar una combinacion directa de valores
 * ya permitidos, y el verificador debe tolerarlo. Incluye tambien +-1
 * (el modismo "la unidad siguiente/anterior al equilibrio" es comun).
 * Deliberadamente NO recursivo (una sola combinacion sobre los numeros
 * YA permitidos, nunca sobre combinaciones de combinaciones): mas
 * profundidad diluye la señal real y puede generar colisiones con
 * numeros genuinamente inventados (verificado con el caso mandatado de
 * 4500). */
export function cerraduraAritmetica(numeros: Set<number>): Set<number> {
  const cerradura = new Set(numeros);
  const lista = [...numeros];
  for (const v of lista) {
    cerradura.add(Math.round((v + 1) * 10000) / 10000);
    cerradura.add(Math.round((v - 1) * 10000) / 10000);
  }
  for (let i = 0; i < lista.length; i++) {
    for (let j = i + 1; j < lista.length; j++) {
      const a = lista[i];
      const b = lista[j];
      cerradura.add(Math.round((a + b) * 10000) / 10000);
      cerradura.add(Math.round(Math.abs(a - b) * 10000) / 10000);
      cerradura.add(Math.round(a * b * 10000) / 10000);
    }
  }
  return cerradura;
}

export function numerosDeMaterial(textos: string[]): Set<number> {
  const numeros = new Set<number>();
  for (const texto of textos) {
    for (const { valor } of extraerNumeros(texto)) {
      numeros.add(Math.round(valor * 10000) / 10000);
    }
  }
  return numeros;
}

function pertenece(valor: number, permitidos: Set<number>): boolean {
  for (const p of permitidos) {
    if (Math.abs(valor - p) <= TOLERANCIA) return true;
  }
  return false;
}

export interface NumeroHuerfano {
  valor: string;
  contexto: string;
}

/** Extrae todo numeral de `texto` y registra 'numero_huerfano' (uno por
 * numero unico, via registrarEvento si se provee) para cada uno que no
 * pertenezca a numerosPermitidos. Devuelve la lista de huerfanos
 * encontrados (aunque no se pase registrarEvento). */
export function verificarNumerosHuerfanos(
  texto: string,
  numerosPermitidos: Set<number>,
  registrarEvento?: (evento: Record<string, unknown>) => void
): NumeroHuerfano[] {
  const huerfanos: NumeroHuerfano[] = [];
  const vistos = new Set<string>();
  for (const { valor, token, contexto } of extraerNumeros(texto)) {
    if (pertenece(valor, numerosPermitidos)) continue;
    const clave = `${token}|${contexto}`;
    if (vistos.has(clave)) continue;
    vistos.add(clave);
    const huerfano = { valor: token, contexto };
    huerfanos.push(huerfano);
    registrarEvento?.({ tipo: "numero_huerfano", ...huerfano });
  }
  return huerfanos;
}
