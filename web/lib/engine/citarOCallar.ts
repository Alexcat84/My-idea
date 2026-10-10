/**
 * CITAR O CALLAR (decision del fundador, 9 oct 2026, REDACTOR_CON_RESPALDO.md punto 3). El redactor marca el respaldo
 * de cada frase que afirma algo del negocio o de la situacion de la persona:
 *   ⟦R7⟧            una respuesta suya (respuestas_de_la_persona del payload); ⟦R2,R5⟧ si son varias;
 *   ⟦N:node_id⟧     un tema que recibio (temas_del_recorrido o temas_vecinos);
 *   ⟦?⟧             no hay respaldo: la frase va como pregunta;
 *   ⟦R7|¿…?⟧        con su pregunta de reserva, por si la cita no vale.
 * El codigo, sin un segundo modelo:
 *  - en vivo (filtroDeMarcas): quita las marcas de cada trozo antes de la pantalla, aunque una marca llegue partida;
 *  - al guardar (validarCitas): valida cada cita (existe; las cifras de la frase estan en lo citado o en los numeros
 *    del payload; comparte al menos una palabra con contenido con lo citado), cambia lo que no vale por su pregunta de
 *    reserva o lo quita, quita de la introduccion la frase sin marca, corta en los pasos y rotulos la cola causal sin
 *    respaldo ("…, porque …") y deja el texto sin ninguna marca.
 * Limite declarado: el codigo comprueba que el respaldo exista y comparta palabras, no que respalde de verdad.
 */
export interface Respaldo {
  respuestas: Array<{ id: string; texto: string }>;
  nodos: Array<{ id: string; textos: string[] }>;
  /** Las cifras que el payload ya da por buenas (numeros_de_la_persona y calculos). */
  cifras: string[];
}

const MARCA_COMPLETA = /\s*⟦[^⟦⟧]*⟧/g;

/** En vivo: el trozo sale sin marcas. Lo que queda despues de una marca abierta (y el blanco que la precede) se retiene
 * hasta que la marca se cierra; el blanco del final se retiene por si lo sigue una marca. */
export function filtroDeMarcas(onDelta: (texto: string) => void): { onChunk: (chunk: string) => void; finalizar: () => void } {
  let pendiente = "";
  return {
    onChunk(chunk: string) {
      let t = (pendiente + chunk).replace(MARCA_COMPLETA, "");
      pendiente = "";
      const abierta = t.lastIndexOf("⟦");
      if (abierta >= 0) {
        let j = abierta;
        while (j > 0 && /\s/.test(t[j - 1])) j--;
        pendiente = t.slice(j);
        t = t.slice(0, j);
      } else {
        const blanco = t.match(/\s+$/)?.[0] ?? "";
        if (blanco) {
          pendiente = blanco;
          t = t.slice(0, t.length - blanco.length);
        }
      }
      if (t) onDelta(t);
    },
    finalizar() {
      const t = pendiente.replace(MARCA_COMPLETA, "").replace(/\s*⟦[^⟧]*$/, "");
      pendiente = "";
      if (t) onDelta(t);
    },
  };
}

const sinMarcas = (s: string) => s.normalize("NFD").replace(/\p{Mn}/gu, "").toLowerCase();
const VACIAS = new Set(["porque", "cuando", "donde", "tienes", "puedes", "hacer", "sobre", "entre", "desde", "hasta", "tambien", "todavia", "antes", "despues", "cada", "mismo", "misma", "otros", "otras", "estos", "estas", "tiene", "puede", "quieres", "quiere", "siempre"]);
const raices = (s: string) =>
  new Set(
    (sinMarcas(s).match(/\p{L}{5,}/gu) ?? []).filter((w) => !VACIAS.has(w)).map((w) => w.slice(0, 5))
  );
const cifrasDe = (s: string) => (s.match(/\d+(?:[.,]\d+)?/g) ?? []).map((n) => n.replace(",", "."));
const sinEspacios = (s: string) => !/\s/.test(s.trim());

const COLA_CAUSAL = /,?\s+(?:porque|ya que|así que|asi que|por eso|eso confirma|lo que confirma|dado que|puesto que)\b[^.!?]*/iu;
const PREFIJO = /^(\s*(?:#+\s*|\d+[.)]\s+|[-*•]\s+|\*\*[^*]+\*\*\s*)?)(.*)$/u;
const ETAPA = /^##\s+Etapa\s+\d+/i;

export function validarCitas(
  texto: string,
  r: Respaldo
): { texto: string; quitadas: number; preguntas: number; colas: number; sinMarca: number } {
  const respuestas = new Map(r.respuestas.map((x) => [x.id.toUpperCase(), x.texto]));
  const nodos = new Map(r.nodos.map((x) => [x.id, x.textos.join(" ")]));
  const cifrasPayload = new Set(r.cifras.flatMap(cifrasDe));
  let quitadas = 0;
  let preguntas = 0;
  let colas = 0;
  let sinMarca = 0;
  let zona: "intro" | "etapa" | "otra" = "intro";

  const vale = (frase: string, contenido: string): { ok: boolean; reserva: string | null } => {
    const [refsTxt, ...resto] = contenido.split("|");
    const reserva = resto.length ? resto.join("|").trim() : null;
    const refs = refsTxt.split(",").map((x) => x.trim()).filter(Boolean);
    if (refs.length === 0) return { ok: false, reserva };
    const citados: string[] = [];
    for (const ref of refs) {
      const n = ref.match(/^N:(.+)$/i);
      const t = n ? nodos.get(n[1].trim()) : respuestas.get(ref.toUpperCase());
      if (t === undefined) return { ok: false, reserva };
      citados.push(t);
    }
    const citado = citados.join(" ");
    const cifrasCitadas = new Set([...cifrasDe(citado), ...cifrasPayload]);
    if (cifrasDe(frase).some((c) => !cifrasCitadas.has(c))) return { ok: false, reserva };
    if (!sinEspacios(frase)) {
      const a = raices(frase);
      const b = raices(citado);
      if (a.size > 0 && ![...a].some((x) => b.has(x))) return { ok: false, reserva };
    }
    return { ok: true, reserva };
  };

  const salida: string[] = [];
  for (const linea of texto.split("\n")) {
    if (/^##\s/.test(linea)) zona = ETAPA.test(linea) ? "etapa" : "otra";
    if (/^#/.test(linea.trim())) {
      salida.push(linea.replace(MARCA_COMPLETA, "").replace(/[⟦⟧]/g, ""));
      continue;
    }
    if (!/[⟦⟧]/.test(linea) && zona !== "intro" && !COLA_CAUSAL.test(linea)) {
      salida.push(linea);
      continue;
    }
    const [, prefijo, cuerpo] = linea.match(PREFIJO) ?? ["", "", linea];
    const esAccion = prefijo.trim() !== "";
    // Las marcas se guardan aparte (su contenido puede llevar ? o .) y la que sigue a la puntuacion se pega a su frase.
    const marcas: string[] = [];
    const cuerpoP = cuerpo
      .replace(/⟦([^⟦⟧]*)⟧/g, (_m, c: string) => `\u0000${marcas.push(c) - 1}\u0000`)
      .replace(/([.!?]+)(\s*)((?:\u0000\d+\u0000\s*)+)/g, (_m, p: string, _s: string, ms: string) => `${ms.trim()}${p}`);
    const frases = cuerpoP.match(/[^.!?]+[.!?]+["»”)]*|[^.!?]+$/g) ?? [];
    const quedan: string[] = [];
    for (const f0 of frases) {
      const ids = [...f0.matchAll(/\u0000(\d+)\u0000/g)].map((m) => marcas[Number(m[1])]);
      let f = f0.replace(/\s*\u0000\d+\u0000/g, "").replace(/[⟦⟧]/g, "").trim();
      if (!f) continue;
      if (ids.length > 0) {
        if (ids.some((c) => c.trim() === "?")) {
          quedan.push(f);
          continue;
        }
        const juicios = ids.map((c) => vale(f, c));
        if (juicios.every((j) => j.ok)) {
          quedan.push(f);
          continue;
        }
        const reserva = juicios.find((j) => j.reserva)?.reserva;
        if (reserva) {
          preguntas++;
          quedan.push(reserva);
        } else quitadas++;
        continue;
      }
      if (zona === "intro" && !esAccion) {
        sinMarca++;
        continue;
      }
      if (COLA_CAUSAL.test(f)) {
        f = f.replace(COLA_CAUSAL, "").replace(/\s+([.!?])$/, "$1");
        colas++;
      }
      quedan.push(f);
    }
    const nuevo = quedan.join(" ").trim();
    if (!nuevo && (esAccion || cuerpo.trim())) continue;
    salida.push(prefijo + nuevo);
  }
  const limpio = salida
    .join("\n")
    .replace(/[⟦⟧]/g, "")
    .replace(/\n{3,}/g, "\n\n")
    .replace(/\s+$/, "");
  return { texto: limpio, quitadas, preguntas, colas, sinMarca };
}
