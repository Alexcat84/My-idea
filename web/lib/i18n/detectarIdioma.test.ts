/**
 * i18n F5 (DISENO §5): el idioma de la IDEA, que manda en lo que escribe la IA
 * y en los documentos (D2). Primero el alfabeto, luego las palabras vacías del
 * alfabeto latino, y en empate (o sin señal) el idioma de la interfaz.
 *
 * Añadido del fundador (25 sep 2026): los idiomas FUERA de los once también se
 * reconocen (la IA responde en ellos; la interfaz y las plantillas sin IA caen
 * al idioma de la interfaz).
 *
 * Cada caso lleva a mano por qué sale lo que sale (AGENTS.md).
 */
import { describe, expect, it } from "vitest";
import { detectarIdioma, idiomaDePlantilla, idiomaDelProyecto, nombreIdiomaParaIA } from "./detectarIdioma";

describe("detectarIdioma: los once", () => {
  it.each([
    // Latino: las palabras vacías deciden.
    // "quiero(es) vender(-) pan(-) de(es,pt,fr) masa(-) madre(-) en(es,fr) mi(es) barrio(-)":
    // es 4 (quiero, de, en, mi), fr 2 (de, en), pt 1 (de) → es.
    ["Quiero vender pan de masa madre en mi barrio", "es"],
    // "i(en) want(en) to(en) sell(-) sourdough(-) bread(-) in(en,de,nl) my(en) neighborhood(-)":
    // en 5 (i, want, to, in, my), de 1, nl 1 → en.
    ["I want to sell sourdough bread in my neighborhood", "en"],
    // "eu(pt,ro) quero(pt) vender(-) pão(-) no(pt,es) meu(pt,ro) bairro(-)":
    // pt 4 + 1 por la "ã" = 5, ro 2 (eu, meu), es 1 (no) → pt.
    ["Eu quero vender pão no meu bairro", "pt"],
    // "je(fr) veux(fr) vendre(-) du(fr) pain(-) dans(fr) mon(fr) quartier(-)": fr 5, nadie más → fr.
    ["Je veux vendre du pain dans mon quartier", "fr"],
    // "ich(de) möchte(de) brot(-) in(de,en,nl) meinem(de) viertel(-) verkaufen(-)":
    // de 4, en 1, nl 1 → de.
    ["Ich möchte Brot in meinem Viertel verkaufen", "de"],
    // "voglio(it) vendere(-) pane(-) nel(it) mio(it) quartiere(-)": it 3, nadie más → it.
    ["Voglio vendere pane nel mio quartiere", "it"],
    // Alfabetos propios: gana el que más letras tiene.
    ["近所でパンを売りたいです", "ja"], // kana presente → japonés (aunque haya han)
    ["我想在我家附近卖面包", "zh"], // solo han, sin kana ni hangul → chino
    ["우리 동네에서 빵을 팔고 싶어요", "ko"], // hangul
    ["أريد أن أبيع الخبز في حيي", "ar"], // árabe sin letras propias del persa o el urdu
    ["मैं अपने मोहल्ले में ब्रेड बेचना चाहता हूँ", "hi"], // devanagari
  ])("%s → %s", (texto, codigo) => {
    expect(detectarIdioma(texto, "es")).toEqual({ codigo, porDefecto: false });
  });
});

describe("detectarIdioma: fuera de los once", () => {
  it.each([
    ["Я хочу продавать хлеб в своём районе", "ru"], // cirílico sin і/ї/є/ґ → ruso
    ["Я хочу продавати хліб у своєму районі", "uk"], // і, є → ucraniano
    ["Θέλω να πουλάω ψωμί στη γειτονιά μου", "el"], // griego
    ["אני רוצה למכור לחם בשכונה שלי", "he"], // hebreo
    ["ฉันอยากขายขนมปังในละแวกบ้าน", "th"], // tailandés
    ["من می‌خواهم نان پخته را در کوچه بفروشم", "fa"], // alfabeto árabe con پ y چ, letras del persa → persa
    ["আমি আমার পাড়ায় রুটি বিক্রি করতে চাই", "bn"], // bengalí
    // Latinos fuera de los once, por sus palabras vacías:
    // "ik(nl) wil(nl) brood(-) verkopen(-) in(nl,en,de) mijn(nl) buurt(-)": nl 4, en 1, de 1 → nl.
    ["Ik wil brood verkopen in mijn buurt", "nl"],
    // "chcę(pl) sprzedawać(-) chleb(-) w(pl) mojej(pl) okolicy(-)": pl 3 + 1 por la "ę" = 4 → pl.
    ["Chcę sprzedawać chleb w mojej okolicy", "pl"],
    // "mahallemde(-) ekmek(-) satmak(-) istiyorum(tr) ve(tr) bu(tr) iş(-) için(tr)":
    // tr 4 + 1 por la "ş" = 5 → tr.
    ["Mahallemde ekmek satmak istiyorum ve bu iş için", "tr"],
    // "tôi(vi) muốn(vi) bán(-) bánh(-) mì(-) ở(vi) khu(-) phố(-) của(vi) tôi(vi)":
    // vi 5 + 1 por el cuerno de "ở" = 6 → vi.
    ["Tôi muốn bán bánh mì ở khu phố của tôi", "vi"],
    // "saya(id) ingin(id) menjual(-) roti(-) di(id,it) lingkungan(-) saya(id)": id 4, it 1 (di) → id.
    ["Saya ingin menjual roti di lingkungan saya", "id"],
  ])("%s → %s", (texto, codigo) => {
    expect(detectarIdioma(texto, "es")).toEqual({ codigo, porDefecto: false });
  });
});

describe("detectarIdioma: sin señal o en empate, manda la interfaz", () => {
  it("sin palabras vacías de ningún idioma: la interfaz, marcada porDefecto", () => {
    // "Uber perros" no tiene ninguna palabra vacía de ninguna lista.
    expect(detectarIdioma("Uber perros", "fr")).toEqual({ codigo: "fr", porDefecto: true });
  });
  it("texto vacío o solo cifras: la interfaz", () => {
    expect(detectarIdioma("", "de")).toEqual({ codigo: "de", porDefecto: true });
    expect(detectarIdioma("123 456 $", "ko")).toEqual({ codigo: "ko", porDefecto: true });
  });
  it("empate entre dos latinos: gana el de la interfaz si está entre los empatados", () => {
    // "de" es vacía en es, pt y fr, y "la" en es, fr e it: "pan de la casa" → es 2, fr 2, pt 1, it 1.
    // Empate es/fr: con interfaz fr, gana fr; con interfaz es, gana es.
    expect(detectarIdioma("pan de la casa", "fr")).toEqual({ codigo: "fr", porDefecto: false });
    expect(detectarIdioma("pan de la casa", "es")).toEqual({ codigo: "es", porDefecto: false });
  });
  it("empate sin la interfaz entre los empatados: la interfaz (no se adivina)", () => {
    // Con interfaz ja: es 2, fr 2 empatan y ja no está → ja, porDefecto.
    expect(detectarIdioma("pan de la casa", "ja")).toEqual({ codigo: "ja", porDefecto: true });
  });
  it("unas pocas palabras latinas dentro de un texto japonés no lo vuelven inglés", () => {
    // Kana y han: の を 作 っ て 近 所 で 売 り た い で す = 14 letras, contra M V P a p p = 6
    // latinas: gana el alfabeto japonés, y con kana presente es japonés.
    expect(detectarIdioma("MVPのappを作って近所で売りたいです", "en").codigo).toBe("ja");
  });
});

describe("idiomaDePlantilla: lo que escribe el código sin IA", () => {
  it("un idioma de los once se usa tal cual", () => {
    expect(idiomaDePlantilla("ko", "es")).toBe("ko");
  });
  it("fuera de los once cae a la interfaz (la IA sí escribe en ese idioma)", () => {
    expect(idiomaDePlantilla("ru", "en")).toBe("en");
  });
  it("sin idioma (proyecto de antes de F5) cae a la interfaz", () => {
    expect(idiomaDePlantilla(null, "pt")).toBe("pt");
  });
});

describe("idiomaDelProyecto", () => {
  it("un proyecto de antes de F5 (sin columna o NULL) es español: la app solo hablaba español", () => {
    expect(idiomaDelProyecto({})).toBe("es");
    expect(idiomaDelProyecto({ idioma: null })).toBe("es");
  });
  it("el guardado manda", () => {
    expect(idiomaDelProyecto({ idioma: "ru" })).toBe("ru");
  });
  it("un valor que no es un código se descarta", () => {
    expect(idiomaDelProyecto({ idioma: "Klingon!" })).toBe("es");
  });
});

describe("nombreIdiomaParaIA: cómo se le nombra el idioma de salida a la IA", () => {
  it("en español (el prompt está en español) y en su propia escritura", () => {
    expect(nombreIdiomaParaIA("ko")).toBe("coreano (한국어)");
    expect(nombreIdiomaParaIA("ru")).toBe("ruso (русский)");
    expect(nombreIdiomaParaIA("es")).toBe("español");
  });
  it("un código sin nombre conocido se pasa tal cual, para que la IA lo reconozca", () => {
    expect(nombreIdiomaParaIA("sw")).toBe("el idioma de código ISO «sw»");
  });
});
