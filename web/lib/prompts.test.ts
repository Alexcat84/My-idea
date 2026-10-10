// Fase 3.0: prompts.ts debe re-exportar EXACTAMENTE lo que trae
// web/lib/assets/prompts.json (generado por scripts/sync_assets_web.py
// leyendo las constantes SYSTEM_* de prototipo_motor.py). Este test es la
// red de seguridad contra un futuro cambio que hardcodee un prompt en vez
// de re-exportarlo del JSON -- si alguna vez diverge, el prompt caching
// de Anthropic deja de coincidir con el prefijo de Python en silencio.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import * as prompts from "./prompts";

const promptsJsonPath = path.join(__dirname, "assets", "prompts.json");
const fuente = JSON.parse(readFileSync(promptsJsonPath, "utf-8")) as Record<string, string>;

describe("prompts.ts re-exporta byte a byte desde assets/prompts.json", () => {
  const nombres = [
    "SYSTEM_CLASIFICACION",
    "SYSTEM_PUERTA_AVANZADA",
    "SYSTEM_INTERPRETE_MULTI",
    "SYSTEM_PROFUNDIZAR",
    "SYSTEM_PREGUNTA_DIRIGIDA",
    "SYSTEM_PLAN",
    "SYSTEM_ESTADO_VIVO",
    "SYSTEM_JUEZ_SESION",
    "SYSTEM_ORGANIZADOR",
    "SYSTEM_REPORTE",
    "SYSTEM_CLASIFICAR_OFERTA",
    "SYSTEM_DIAGNOSTICO_MUNDO",
  ] as const;

  for (const nombre of nombres) {
    it(`${nombre} es identico byte a byte a la constante Python`, () => {
      expect(prompts[nombre]).toBe(fuente[nombre]);
      expect(prompts[nombre].length).toBeGreaterThan(0);
    });
  }

  // Voz de la casa: los prompts que escriben PROSA PARA EL USUARIO llevan la
  // prohibicion del guion largo en su propio SYSTEM, y este test la mantiene
  // ahi aunque alguien reescriba un prompt entero.
  //
  // Los otros cinco (CLASIFICACION, PROFUNDIZAR, ESTADO_VIVO, JUEZ_SESION,
  // CLASIFICAR_OFERTA) no la llevan a proposito: cuatro devuelven JSON interno
  // y el quinto (PROFUNDIZAR) escribe una pregunta que SI se muestra, pero los
  // cinco salen por llamarClaude, que limpia en su punto unico. La red real es
  // la limpieza de salida; la regla en el prompt solo ayuda a que llegue limpio.
  const PROSA_AL_USUARIO = [
    "SYSTEM_PUERTA_AVANZADA",
    "SYSTEM_INTERPRETE_MULTI",
    "SYSTEM_PREGUNTA_DIRIGIDA",
    "SYSTEM_PLAN",
    "SYSTEM_ORGANIZADOR",
    "SYSTEM_REPORTE",
    "SYSTEM_DIAGNOSTICO_MUNDO",
  ] as const;

  for (const nombre of PROSA_AL_USUARIO) {
    it(`${nombre} prohibe los guiones largos en su propio SYSTEM`, () => {
      expect(prompts[nombre]).toContain("PROHIBIDO usar guiones largos o medios");
    });
  }
});

// Auditoria de prompts, decision del fundador del 7 oct 2026 (docs/auditoria_final/informes/auditoria_prompts.md,
// secciones B, C y F): las instrucciones que empujaban a inventar se reescriben, y esta guarda fija el texto nuevo
// para que ninguna reescritura futura lo pierda. Los SYSTEM_* del motor se leen de prompts.json (la copia byte a byte
// de engine/prototipo_motor.py); SYSTEM_ENLACE_PROTECCION nace en prompts.ts.
describe("auditoria de prompts (7 oct 2026): ninguna instruccion empuja a inventar", () => {
  it("B2: la seccion de numeros del plan solo lleva los que nombran los conceptos de viabilidad", () => {
    expect(prompts.SYSTEM_PLAN).toContain("Un item por cada numero que nombran los conceptos con es_viabilidad_economica");
    // 9 oct 2026 (REDACTOR_CON_RESPALDO punto 1): lo que recibe la IA se llama "temas", no "material".
    expect(prompts.SYSTEM_PLAN).toContain("no añadas metricas que los temas no nombren");
    expect(prompts.SYSTEM_PLAN).not.toContain("cada numero que la persona debe calcular o conseguir");
  });

  it("B4: el cierre del plan prohibe inventar leyes, normas, tramites, plazos, precios, porcentajes, tasas de exito, resultados y nombres de herramientas o empresas", () => {
    const cierre = prompts.SYSTEM_PLAN.match(/Tampoco inventes [^.]*\./)?.[0] ?? "";
    for (const t of ["leyes", "normas", "tramites", "plazos", "precios", "porcentajes de referencia", "tasas de exito",
      "resultados prometidos", "nombres de herramientas o empresas", "que no esten en los temas o en lo que dijo la persona"])
      expect(cierre, t).toContain(t);
    expect(prompts.SYSTEM_PLAN.indexOf("Todo debe salir de los temas recibidos")).toBeLessThan(prompts.SYSTEM_PLAN.indexOf("Tampoco inventes"));
  });

  it("B5: el perfil se anota con las palabras de la persona, sin deducir", () => {
    expect(prompts.SYSTEM_INTERPRETE_MULTI).toContain("con lo que la persona dijo, en sus palabras; no deduzcas causas, cifras ni logros");
    expect(prompts.SYSTEM_INTERPRETE_MULTI).not.toContain("resumela");
  });

  it("B7: los caminos salen solo de los candidatos y de lo que conto la persona, con un ejemplo neutro", () => {
    expect(prompts.SYSTEM_CAMINOS).not.toContain("Eres el estratega");
    expect(prompts.SYSTEM_CAMINOS).not.toContain("que harias distinto");
    expect(prompts.SYSTEM_CAMINOS).toContain("que trabajarias distinto usando solo lo que dicen los candidatos y lo que conto la persona");
    expect(prompts.SYSTEM_CAMINOS).toContain("sin canales, modelos de venta, cifras ni plazos nuevos");
    expect(prompts.SYSTEM_CAMINOS).toContain("(ejemplo: 'Probar primero con quienes ya te compran')");
    expect(prompts.SYSTEM_CAMINOS).not.toContain("Vender por encargo sin local");
    expect(prompts.SYSTEM_CAMINOS).toContain("Sin cifras que no esten en lo que recibiste");
  });

  it("B8 y B9: el enlazador solo pone deteccion y severidad con base en el texto; si no, vacio y null", () => {
    const p = prompts.SYSTEM_ENLACE_PROTECCION.replace(/\s+/g, " ");
    expect(p).toContain("solo si el texto de la respuesta la nombra o se lee en ella sin suponer nada; si no, cadena vacía");
    expect(p).toContain("solo si el plan o la persona dan base para ella; si no la dan, null");
  });

  it("B10: las areas del organizador son temas de la lista de puertas y lo que asume son preguntas abiertas", () => {
    expect(prompts.SYSTEM_ORGANIZADOR).toContain("son solo NOMBRES de temas de la lista de puertas");
    expect(prompts.SYSTEM_ORGANIZADOR).toContain("'lo_que_estas_asumiendo_sin_saberlo' son preguntas abiertas, nunca afirmaciones de mercado, normas o cifras");
  });

  it("C1: el ejemplo de la regla 15 no manda a un registro oficial que puede no existir", () => {
    expect(prompts.SYSTEM_PLAN).not.toContain("registro oficial");
    expect(prompts.SYSTEM_PLAN).toContain("busca cuantos auditores certificados hay en tu zona; ese numero te dira si hay espacio");
  });

  it("C2: el avance de un seguimiento sale solo de lo que dice estado_vivo_previo", () => {
    expect(prompts.SYSTEM_PLAN).toContain("Usa solo avances que estado_vivo_previo diga con esas palabras");
  });

  it("C3: el ejemplo del costo por unidad no fija una cantidad de piezas", () => {
    expect(prompts.SYSTEM_PLAN).not.toContain("3 piezas");
    expect(prompts.SYSTEM_PLAN).toContain("para una tanda y divide entre las piezas que salieron");
  });

  it("C5: lo adyacente que se ofrece al confesar el dominio viene de los nodos que recibe", () => {
    expect(prompts.SYSTEM_INTERPRETE_MULTI).toContain("lo adyacente que trae alguno de los nodos que recibes");
    expect(prompts.SYSTEM_INTERPRETE_MULTI).not.toContain("lo adyacente que SI cubres");
  });

  it("C6, en parte: el ejemplo de $850/$170 va marcado como cifras ficticias de forma; la ayuda de como conseguir los datos se queda", () => {
    expect(prompts.SYSTEM_REPORTE).toMatch(/cifras ficticias[^']*'dejarías de facturar \$850/);
    expect(prompts.SYSTEM_REPORTE).toContain("## Los números que te faltan (y cómo conseguirlos)");
  });
});
