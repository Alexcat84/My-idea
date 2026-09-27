// i18n F3: la bitácora colorea el motivo citado al final de una entrada
// ("Retiraste X: «motivo»"). Hasta F2 solo reconocía «…» tras ": ", que es la
// forma del español; cada idioma cita y pone los dos puntos a su manera.
// Lo esperado se parte a mano: [lo de antes, el separador, la cita con sus comillas].
import { describe, expect, it } from "vitest";
import { partirMotivo } from "./comillas";

describe("partirMotivo", () => {
  it("español, idéntico a lo de F2: ': «…»'", () => {
    expect(partirMotivo("Retiraste la tarea: «no aplica aquí»")).toEqual(["Retiraste la tarea", ": ", "«no aplica aquí»"]);
  });
  it("con dos puntos antes, corta en los últimos (los que abren la cita)", () => {
    expect(partirMotivo("Paso 1: hecho: «ya está»")).toEqual(["Paso 1: hecho", ": ", "«ya está»"]);
  });
  it("francés: espacio antes de los dos puntos y dentro de las comillas", () => {
    expect(partirMotivo("Tu as retiré la tâche : « pas ici »")).toEqual(["Tu as retiré la tâche", " : ", "« pas ici »"]);
  });
  it("inglés “…”, alemán „…“, japonés ：「…」, chino ：“…”", () => {
    expect(partirMotivo("You removed the task: “not here”")).toEqual(["You removed the task", ": ", "“not here”"]);
    expect(partirMotivo("Du hast die Aufgabe entfernt: „nicht hier“")).toEqual(["Du hast die Aufgabe entfernt", ": ", "„nicht hier“"]);
    expect(partirMotivo("タスクを外しました：「ここでは不要」")).toEqual(["タスクを外しました", "：", "「ここでは不要」"]);
    expect(partirMotivo("你移除了任务：“这里不需要”")).toEqual(["你移除了任务", "：", "“这里不需要”"]);
  });
  it("sin cita al final, o con comillas que no casan: nada que colorear", () => {
    expect(partirMotivo("Empezaste la tarea.")).toBeNull();
    expect(partirMotivo("Retiraste la tarea: «no aplica“")).toBeNull();
    expect(partirMotivo("Retiraste «la tarea» y siguió")).toBeNull();
  });
});
