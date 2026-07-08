/**
 * parseJson.ts - Fase 3.0: port de _parsear_json en prototipo_motor.py.
 * Claude a veces envuelve su JSON en ```json ... ``` o agrega texto/una
 * nota despues del primer objeto valido -- se toma solo el primero.
 */
export function parsearJson<T = unknown>(raw: string): T {
  const texto = raw
    .trim()
    .replace(/^```json/, "")
    .replace(/```$/, "")
    .trim();
  try {
    return JSON.parse(texto) as T;
  } catch {
    // Extrae solo el primer objeto/array JSON valido del inicio del texto,
    // igual que json.JSONDecoder().raw_decode en Python.
    let profundidad = 0;
    let enString = false;
    let escape = false;
    for (let i = 0; i < texto.length; i++) {
      const c = texto[i];
      if (escape) {
        escape = false;
        continue;
      }
      if (c === "\\") {
        escape = true;
        continue;
      }
      if (c === '"') {
        enString = !enString;
        continue;
      }
      if (enString) continue;
      if (c === "{" || c === "[") profundidad++;
      else if (c === "}" || c === "]") {
        profundidad--;
        if (profundidad === 0) {
          return JSON.parse(texto.slice(0, i + 1)) as T;
        }
      }
    }
    throw new SyntaxError(`no se pudo extraer JSON valido de: ${texto.slice(0, 200)}`);
  }
}
