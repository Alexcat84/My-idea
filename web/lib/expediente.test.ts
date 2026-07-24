import { describe, expect, it } from "vitest";
import {
  CLAVE_EXPEDIENTE,
  claveDeCiclo,
  cicloMarkdown,
  expedienteMarkdown,
  indiceDeDocumentos,
  nombreArchivo,
  rebajarTitulos,
  titulosDeCiclos,
  type CicloExpediente,
  type DatosExpediente,
} from "./expediente";

const ciclo = (planId: string, etiqueta: string, createdAt: string, md = "# Plan\n\ncuerpo"): CicloExpediente => ({
  planId,
  etiqueta,
  createdAt,
  contenidoMd: md,
});

describe("rebajarTitulos", () => {
  it("baja cada título los niveles pedidos", () => {
    expect(rebajarTitulos("# Uno\n## Dos\ntexto", 2)).toBe("### Uno\n#### Dos\ntexto");
  });

  it("no pasa de h6 (markdown no tiene h7)", () => {
    expect(rebajarTitulos("##### Cinco\n###### Seis", 2)).toBe("###### Cinco\n###### Seis");
  });

  it("respeta los bloques de código: ahí un # es comentario, no título", () => {
    const md = ["# Título", "```bash", "# esto es un comentario", "```", "## Otro"].join("\n");
    const esperado = ["## Título", "```bash", "# esto es un comentario", "```", "### Otro"].join("\n");
    expect(rebajarTitulos(md, 1)).toBe(esperado);
  });

  it("cierra el bloque solo con su misma marca (~~~ no cierra un ```)", () => {
    const md = ["```", "~~~", "# dentro", "```", "# fuera"].join("\n");
    expect(rebajarTitulos(md, 1)).toBe(["```", "~~~", "# dentro", "```", "## fuera"].join("\n"));
  });

  it("con 0 niveles devuelve el markdown intacto", () => {
    expect(rebajarTitulos("# Uno", 0)).toBe("# Uno");
  });

  it("no toca una almohadilla que no abre título (#sin espacio)", () => {
    expect(rebajarTitulos("#etiqueta", 1)).toBe("#etiqueta");
  });
});

describe("titulosDeCiclos", () => {
  it("el primer ciclo es Tu Plan y los siguientes son seguimientos numerados", () => {
    const ts = titulosDeCiclos([
      ciclo("p1", "completo", "2026-03-01T12:00:00Z"),
      ciclo("p2", "seguimiento", "2026-03-20T12:00:00Z"),
      ciclo("p3", "seguimiento", "2026-04-10T12:00:00Z"),
    ]);
    expect(ts.map((t) => t.titulo)).toEqual(["Tu Plan", "Seguimiento 1", "Seguimiento 2"]);
  });

  it("la posición manda, no la etiqueta de base de datos", () => {
    // 'inicial' (plan corto) tambien es el primer ciclo: el usuario ve "Tu Plan".
    expect(titulosDeCiclos([ciclo("p1", "inicial", "2026-03-01T12:00:00Z")])[0].titulo).toBe("Tu Plan");
  });
});

describe("indiceDeDocumentos", () => {
  it("un documento por ciclo más el expediente completo", () => {
    const docs = indiceDeDocumentos(
      [ciclo("p1", "completo", "2026-03-01T12:00:00Z"), ciclo("p2", "seguimiento", "2026-03-20T12:00:00Z")],
      null
    );
    expect(docs.map((d) => d.clave)).toEqual([claveDeCiclo("p1"), claveDeCiclo("p2"), CLAVE_EXPEDIENTE]);
    expect(docs.at(-1)!.subtitulo).toContain("hasta hoy");
  });

  it("sin ningún plan no ofrece expediente (no hay desarrollo que contar)", () => {
    expect(indiceDeDocumentos([], null)).toEqual([]);
  });

  it("ya cerrada, el expediente se presenta como el recorrido completo", () => {
    const docs = indiceDeDocumentos([ciclo("p1", "completo", "2026-03-01T12:00:00Z")], "2026-05-01T12:00:00Z");
    expect(docs.at(-1)!.subtitulo).toContain("de la idea al cierre");
  });
});

const datos = (extra: Partial<DatosExpediente> = {}): DatosExpediente => ({
  nombre: "Kits de huerto urbano",
  entradaOriginal: "Quiero vender kits para sembrar en balcones.",
  creadaAt: "2026-03-01T12:00:00Z",
  realizadaAt: null,
  cierreMotivo: null,
  organizadorMd: "# Tu idea, ordenada\n\nlo esencial",
  ciclos: [
    ciclo("p1", "completo", "2026-03-02T12:00:00Z", "# Plan inicial\n\n## Etapa 1\npasos"),
    ciclo("p2", "seguimiento", "2026-04-02T12:00:00Z", "# Seguimiento\n\ncuerpo"),
  ],
  acciones: [
    { etapa: 1, texto: "Publica el video", estado: "hecho", completedAt: "2026-03-06T12:00:00Z", fechaBase: null },
    { etapa: 1, texto: "Habla con 5 desconocidos", estado: "pendiente", completedAt: null, fechaBase: "2026-03-13T12:00:00Z" },
    { etapa: 2, texto: "Entrega a mano", estado: "pendiente", completedAt: null, fechaBase: null },
  ],
  numerosMd: "# Tus Números\n\npunto de equilibrio",
  mundos: [{ nombre: "Riesgos Bajo Control", contenidoMd: "# Riesgos\n\ncuerpo", completadoAt: null }],
  informeMd: "# Análisis\n\n## Lo que construiste\ndatos",
  generadoAt: "2026-05-01T12:00:00Z",
  ...extra,
});

describe("expedienteMarkdown", () => {
  it("lleva todas las secciones del viaje, en orden", () => {
    const md = expedienteMarkdown(datos());
    const orden = [
      "## Tu idea, tal como la escribiste",
      "## Tu idea, ordenada",
      "## Tu Plan",
      "## Seguimiento 1",
      "## Lo que hiciste",
      "## Tus Números",
      "## Riesgos Bajo Control",
      "## Cómo te fue",
    ];
    let cursor = -1;
    for (const seccion of orden) {
      const i = md.indexOf(seccion);
      expect(i, `falta o va desordenada la sección ${seccion}`).toBeGreaterThan(cursor);
      cursor = i;
    }
  });

  it("rebaja los títulos incrustados para que la jerarquía no quede al revés", () => {
    const md = expedienteMarkdown(datos());
    // El plan trae '# Plan inicial' y '## Etapa 1'; bajo un '## Tu Plan' pasan a h3/h4.
    expect(md).toContain("### Plan inicial");
    expect(md).toContain("#### Etapa 1");
    // Solo el título del expediente se queda en h1.
    expect(md.split("\n").filter((x) => /^# /.test(x))).toEqual(["# Kits de huerto urbano"]);
  });

  it("el registro de acciones cuenta lo hecho y fecha cada una", () => {
    const md = expedienteMarkdown(datos());
    expect(md).toContain("Completaste **1 de 3** acciones activas.");
    expect(md).toContain("- [x] Publica el video · hecho el");
    expect(md).toContain("- [ ] Habla con 5 desconocidos · previsto para el");
    expect(md).toContain("- [ ] Entrega a mano\n");
    expect(md).toContain("### Etapa 1");
    expect(md).toContain("### Etapa 2");
  });

  it("las retiradas (no_aplica) salen del denominador y van aparte con su motivo", () => {
    const md = expedienteMarkdown(
      datos({
        acciones: [
          { etapa: 1, texto: "Publica el video", estado: "hecho", completedAt: "2026-03-06T12:00:00Z", fechaBase: null },
          { etapa: 1, texto: "Habla con 5 desconocidos", estado: "pendiente", completedAt: null, fechaBase: null },
          {
            etapa: 2,
            texto: "Contrata un local",
            estado: "no_aplica",
            completedAt: null,
            fechaBase: null,
            noAplicaMotivo: "mi negocio es 100% online",
          },
        ],
      })
    );
    // El denominador cuenta 2 activas, no 3: la retirada no infla la meta.
    expect(md).toContain("Completaste **1 de 2** acciones activas.");
    // La retirada no aparece como pendiente, sino en su propia sección con motivo.
    expect(md).toContain("### Retiradas (no aplican): 1");
    expect(md).toContain("- Contrata un local — mi negocio es 100% online");
    expect(md).not.toContain("- [ ] Contrata un local");
  });

  it("una idea en marcha se declara en marcha; una cerrada, con su fecha", () => {
    expect(expedienteMarkdown(datos())).toContain("**Estado** En marcha");
    const cerrada = expedienteMarkdown(datos({ realizadaAt: "2026-05-01T12:00:00Z" }));
    expect(cerrada).toContain("**Estado** Proyecto realizado el");
  });

  it("omite en silencio lo que el usuario todavía no tiene", () => {
    const md = expedienteMarkdown(
      datos({ organizadorMd: null, numerosMd: null, mundos: [], informeMd: null, acciones: [] })
    );
    for (const ausente of ["## Tu idea, ordenada", "## Tus Números", "## Lo que hiciste", "## Cómo te fue"]) {
      expect(md).not.toContain(ausente);
    }
    expect(md).toContain("## Tu Plan");
  });

  it("el índice anuncia exactamente las secciones que trae", () => {
    const md = expedienteMarkdown(datos({ numerosMd: null }));
    const indice = md.slice(md.indexOf("## Contenido"), md.indexOf("---"));
    expect(indice).toContain("- Tu Plan");
    expect(indice).toContain("- Seguimiento 1");
    expect(indice).not.toContain("- Tus Números");
  });

  it("nunca filtra la mecánica interna (BANCO §5: es confidencial)", () => {
    const md = expedienteMarkdown(datos()).toLowerCase();
    for (const fuga of ["nodo", "grafo", "pack", "dominio", "prompt", "llm", "token"]) {
      expect(md, `el expediente filtró "${fuga}"`).not.toContain(fuga);
    }
  });

  it("sin guiones largos: es copy visible", () => {
    expect(expedienteMarkdown(datos())).not.toMatch(/[—–]/);
  });
});

describe("cicloMarkdown", () => {
  it("antepone una portadilla que identifica idea, documento y fecha", () => {
    const md = cicloMarkdown("Kits de huerto", "Seguimiento 1", ciclo("p2", "seguimiento", "2026-04-02T12:00:00Z"));
    expect(md.split("\n")[0]).toContain("Kits de huerto · Seguimiento 1 · ");
    expect(md).toContain("de 2026");
    expect(md).toContain("# Plan");
  });
});

describe("nombreArchivo", () => {
  it("junta idea y documento en un nombre seguro", () => {
    expect(nombreArchivo("Kits de huerto urbano", "Seguimiento 1")).toBe("kits-de-huerto-urbano-seguimiento-1");
  });

  it("aguanta nombres con signos y vacíos", () => {
    expect(nombreArchivo("¿Y si...? / mi idea", "Tu Plan")).toBe("y-si-mi-idea-tu-plan");
    expect(nombreArchivo("", "")).toBe("mi-idea-documento");
  });
});
