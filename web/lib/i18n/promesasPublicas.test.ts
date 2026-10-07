// Auditoría final, promesas públicas (docs/auditoria_final/informes/promesas_publicas.md),
// 7 oct 2026: M7, M8, M14, M15, B6 y B7. El texto no promete lo que la app no hace:
// el plan no trae los ciclos ni los mundos, el pack grande alcanza para un paquete
// concreto (no para "el viaje entero"), el aviso del calendario depende del programa,
// rehacer el plan es un ciclo que cuesta créditos y el PDF lo guarda tu navegador.
// Los textos esperados están escritos a mano; las cifras de precio NO se escriben en
// ningún mensaje (viven en lib/precios.ts, AGENTS.md).
import { describe, expect, it } from "vitest";
import { LOCALES } from "./config";
import { CALENDARIO } from "./mensajes/calendario";
import { CREDITOS } from "./mensajes/creditos";
import { PACKS_RECARGA } from "./mensajes/packsRecarga";
import { PLAN_DOCUMENTO } from "./mensajes/planDocumento";
import { PACKS, PRECIOS } from "../precios";

const GUIONES = /[–—]/;

describe("M7: el plan no trae los ciclos ni los mundos", () => {
  it("el texto de Tu Plan dice que los ciclos y los mundos se pagan aparte", () => {
    expect(CREDITOS.es.proyecto.planTexto).toBe(
      "Tu plan completo, de la idea a hacerla realidad, y las herramientas para ejecutarlo. Los ciclos de ajuste para rehacerlo después y los mundos se pagan aparte."
    );
    expect(CREDITOS.es.proyecto.planTexto).not.toMatch(/todo para llevarlo a cabo/);
  });
  it("en los once idiomas, sin cifras escritas a mano ni guiones largos", () => {
    for (const l of LOCALES) {
      expect(CREDITOS[l].proyecto.planTexto, l).not.toMatch(/\d/);
      expect(CREDITOS[l].proyecto.planTexto, l).not.toMatch(GUIONES);
    }
  });
});

describe("M8 y B7: las recargas dicen para qué alcanzan, sin prometer de más", () => {
  // La cuenta, a mano, contra el catálogo de precios.ts (nunca cifras en el texto):
  // Recarga = un seguimiento = el plan de un mundo.
  // Profesional = plan + 2 seguimientos + plan de un mundo + su seguimiento.
  const pack = (clave: string) => PACKS.find((p) => p.clave === clave)!;
  it("Recarga: un seguimiento o el plan de un mundo (no 'un mundo suelto')", () => {
    expect(PACKS_RECARGA.es.recarga.alcanza).toBe("un seguimiento o el plan de un mundo");
    expect(pack("recarga").creditos).toBe(PRECIOS.seguimiento);
    expect(pack("recarga").creditos).toBe(PRECIOS.mundo_activar);
  });
  it("Profesional: el paquete concreto, no 'el viaje entero de una idea'", () => {
    expect(PACKS_RECARGA.es.profesional.alcanza).toBe("tu plan, dos seguimientos y un mundo con su seguimiento");
    expect(pack("profesional").creditos).toBe(
      PRECIOS.plan_completo + 2 * PRECIOS.seguimiento + PRECIOS.mundo_activar + PRECIOS.mundo_seguimiento
    );
  });
  it("las promesas viejas no vuelven en ningún idioma", () => {
    const viejas = [
      /viaje entero/,
      /whole journey/,
      /parcours complet/,
      /jornada inteira/,
      /ganze Reise/,
      /intero viaggio/,
      /旅のすべて/,
      /完整旅程/,
      /여정 전체/,
      /من أولها إلى آخرها/,
      /पूरी यात्रा/,
      /mundo suelto/,
      /single world/,
      /seul monde/,
      /mundo avulso/,
      /einzelne Welt/,
      /singolo mondo/,
      /单独一个世界/,
      /عالم منفرد/,
      /अकेली दुनिया/,
    ];
    for (const l of LOCALES) {
      for (const clave of ["recarga", "profesional"] as const) {
        const texto = PACKS_RECARGA[l][clave].alcanza;
        for (const v of viejas) expect(texto, `${l} ${clave}`).not.toMatch(v);
        expect(texto, `${l} ${clave}`).not.toMatch(GUIONES);
      }
    }
  });
});

describe("M14: el aviso del calendario depende del programa, y se dice", () => {
  it("el español ya no asegura que el calendario avisa siempre", () => {
    const info = CALENDARIO.es.suscripcion.info;
    expect(info).not.toMatch(/Tu calendario te avisa de cada tarea el mismo día/);
    expect(info).toMatch(
      /Cada tarea lleva un aviso para su día, pero según el calendario que uses puede que tengas que activar sus notificaciones\.$/
    );
  });
  it("en los once idiomas el texto cambia de la promesa vieja", () => {
    const viejas: Record<string, string> = {
      en: "Your calendar reminds you of each task on the day it's due.",
      fr: "Ton calendrier te rappelle chaque tâche le jour même.",
      pt: "Seu calendário avisa você de cada tarefa no próprio dia.",
      de: "Dein Kalender erinnert dich am jeweiligen Tag an jede Aufgabe.",
      it: "Il tuo calendario ti ricorda ogni attività il giorno stesso.",
      ja: "各タスクの当日には、カレンダーがお知らせします。",
      zh: "每项任务到期当天，你的日历都会提醒你。",
      ko: "할 일마다 당일에 캘린더가 알려 줘요.",
      ar: "ويذكّركم تقويمكم بكل مهمة في يومها.",
      hi: "आपका कैलेंडर हर काम की याद उसी दिन दिलाएगा।",
    };
    for (const l of LOCALES) {
      if (viejas[l]) expect(CALENDARIO[l].suscripcion.info, l).not.toContain(viejas[l]);
      expect(CALENDARIO[l].suscripcion.info, l).not.toMatch(GUIONES);
    }
  });
});

describe("M15: rehacer el plan es un ciclo que cuesta créditos, no volver gratis a la entrevista", () => {
  it("el español nombra el ciclo y su costo, sin la cifra escrita", () => {
    expect(PLAN_DOCUMENTO.es.notaRecalculo).toBe(
      "¿Cambia algo en el mundo real? Pide un nuevo ciclo desde Manos a la Obra y tu plan se rehace desde donde estés. Cuesta créditos y verás el precio antes de confirmarlo."
    );
    expect(PLAN_DOCUMENTO.es.notaRecalculo).not.toMatch(/entrevista|cuando quieras/);
  });
  it("en los once idiomas: sin cifras (el componente no interpola) ni marcadores sueltos", () => {
    for (const l of LOCALES) {
      const t = PLAN_DOCUMENTO[l].notaRecalculo;
      expect(t, l).not.toMatch(/\d/);
      expect(t, l).not.toMatch(/\{\{/);
      expect(t, l).not.toMatch(GUIONES);
    }
  });
});

describe("B6: el PDF se guarda desde el navegador; el archivo es .md", () => {
  it("el español lo dice así", () => {
    expect(CREDITOS.es.incluyePlan[3]).toBe(
      "<b>Tus documentos:</b> tu plan y cada resumen, en .md para editarlos o en PDF, que guardas desde tu navegador."
    );
  });
  it("en los once idiomas nombra el .md y el PDF", () => {
    for (const l of LOCALES) {
      const t = CREDITOS[l].incluyePlan[3];
      expect(t, l).toContain(".md");
      expect(t, l).toContain("PDF");
      expect(t, l).not.toMatch(GUIONES);
    }
  });
});
