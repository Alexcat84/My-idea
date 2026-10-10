/**
 * MENOS PROSA (decision del fundador, 9 oct 2026, REDACTOR_CON_RESPALDO.md punto 4). En las tres mediciones la prosa
 * narrativa del plan (la introduccion y los parrafos de las etapas) era el 18 % del texto y juntaba el 59 % de los
 * hallazgos sostenidos: causas y resultados prometidos en las bisagras. El prompt pide una introduccion corta y etapas
 * solo accionables; este codigo lo garantiza sin modelo:
 *  - la introduccion (entre el titulo y la primera seccion) se queda en su primer parrafo, con dos frases como mucho;
 *  - en cada "## Etapa N", sobreviven solo los bloques que empiezan con un rotulo ("**Pasos:**", "**Entregable:**",
 *    "**Primera acción:**"...) o con un paso de lista, y el bloque que sigue a un rotulo vacio (su contenido);
 *  - una etapa que se quedaria sin nada accionable (formato roto) se deja como vino: nunca queda vacia;
 *  - las demas secciones (la de numeros, por ejemplo) no se tocan.
 * Se aplica al generar; los planes ya guardados no cambian.
 */
const ETAPA = /^##\s+Etapa\s+\d+/i;
const ROTULO = /^\*\*[^*]+\*\*/;
const ROTULO_VACIO = /^\*\*[^*]+:\s*\*\*\s*$|^\*\*[^*]+\*\*\s*:?\s*$/;
const PASO = /^\s*(?:\d+[.)]|[-*•])\s+/;
const accionable = (l: string) => ROTULO.test(l.trim()) || PASO.test(l) || l.trim().startsWith("#");

function bloques(lineas: string[]): string[][] {
  const out: string[][] = [];
  let actual: string[] = [];
  for (const l of lineas) {
    if (l.trim() === "") {
      if (actual.length) out.push(actual);
      actual = [];
    } else actual.push(l);
  }
  if (actual.length) out.push(actual);
  return out;
}

/** Una etapa: quita los bloques narrativos. Devuelve las lineas y cuantos bloques quito, o null si no queda nada
 * accionable (la etapa se deja como vino). */
function podarEtapa(cuerpo: string[]): { lineas: string[]; quitadas: number } | null {
  const salida: string[][] = [];
  let quitadas = 0;
  let siguienteEsContenido = false;
  for (const b of bloques(cuerpo)) {
    if (siguienteEsContenido) {
      salida.push(b);
      siguienteEsContenido = false;
      continue;
    }
    const primera = b.findIndex(accionable);
    if (primera < 0) {
      quitadas++;
      continue;
    }
    if (primera > 0) quitadas++;
    const queda = b.slice(primera);
    salida.push(queda);
    siguienteEsContenido = ROTULO_VACIO.test(queda[queda.length - 1].trim());
  }
  if (!salida.some((b) => b.some((l) => PASO.test(l) || ROTULO.test(l.trim())))) return null;
  return { lineas: salida.flatMap((b, i) => (i === 0 ? b : ["", ...b])), quitadas };
}

const FRASES = /[^.!?]+[.!?]+["»”)]*\s*|[^.!?]+$/g;

export function podarProsa(cuerpo: string): { texto: string; quitadas: number; introRecortada: boolean } {
  const lineas = cuerpo.split("\n");
  // Las secciones: [encabezado, cuerpo]. La primera, antes de cualquier "## ", es el titulo y su introduccion.
  const secciones: Array<{ cabeza: string | null; cuerpo: string[] }> = [{ cabeza: null, cuerpo: [] }];
  for (const l of lineas) {
    if (/^##\s/.test(l)) secciones.push({ cabeza: l, cuerpo: [] });
    else secciones[secciones.length - 1].cuerpo.push(l);
  }
  let quitadas = 0;
  let introRecortada = false;
  const salida: string[] = [];
  for (const s of secciones) {
    if (s.cabeza === null) {
      // titulo + introduccion
      const iTitulo = s.cuerpo.findIndex((l) => /^#\s/.test(l));
      const antes = iTitulo >= 0 ? s.cuerpo.slice(0, iTitulo + 1) : [];
      const resto = iTitulo >= 0 ? s.cuerpo.slice(iTitulo + 1) : s.cuerpo;
      const bs = bloques(resto);
      salida.push(...antes);
      if (bs.length > 0) {
        const intro = bs[0].join(" ").trim();
        const frases = intro.match(FRASES)?.map((f) => f.trim()).filter(Boolean) ?? [intro];
        if (frases.length > 2 || bs.length > 1) introRecortada = true;
        quitadas += bs.length - 1;
        if (antes.length) salida.push("");
        salida.push(frases.slice(0, 2).join(" "));
      }
      salida.push("");
      continue;
    }
    salida.push(s.cabeza);
    if (ETAPA.test(s.cabeza)) {
      const podada = podarEtapa(s.cuerpo);
      if (podada) {
        quitadas += podada.quitadas;
        salida.push("", ...podada.lineas, "");
        continue;
      }
    }
    salida.push(...s.cuerpo);
  }
  const texto = salida
    .join("\n")
    .replace(/\n{3,}/g, "\n\n")
    .replace(/^\n+/, "")
    .replace(/\s+$/, "");
  return { texto, quitadas, introRecortada };
}
