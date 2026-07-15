/**
 * detectorAcentos.ts - Fase 3.9 (D11): detector heuristico de espanol SIN
 * acentos en la salida del redactor. El SYSTEM_PLAN se escribe sin tildes por
 * byte-safety del prompt caching, y el modelo tiende a imitar ese estilo: el
 * plan real del fundador salio "restriccion critica", "clausula", "logica"
 * mientras las preguntas de la entrevista si tenian acentos. Señal de triage
 * (glass box), no bloquea. Deliberadamente CONSERVADOR: solo clases de palabra
 * que en espanol correcto SIEMPRE llevan tilde, evitando las ambiguas
 * (mas/mas, esta/esta, si/si, el/el, tu/tu) que tienen forma valida sin tilde.
 */

// Terminaciones -cion/-sion: en su forma correcta llevan tilde en la o
// (informacion -> informacion, decision -> decision). La version sin tilde
// que este patron caza es siempre incorrecta; la acentuada no matchea porque
// la o con tilde no es [a-z].
const TERMINACION = /\b[a-z]{3,}(?:cion|sion)\b/gi;

// Palabras de alta frecuencia en un plan que SIEMPRE se acentuan y no tienen
// homografo valido sin tilde en este contexto.
const PALABRAS_ACENTUADAS = [
  "analisis", "clausula", "logica", "numero", "numeros", "metodo", "metodos",
  "economico", "economica", "economicos", "economicas", "estandar", "dias",
  "aqui", "asi", "tambien", "segun", "rapido", "rapida", "basico", "basica",
  "pagina", "paginas", "proximo", "proxima", "ultimo", "ultima", "facil",
  "dificil", "credito", "creditos", "podria", "deberia", "tendria", "haria",
];
const LISTA = new RegExp(`\\b(?:${PALABRAS_ACENTUADAS.join("|")})\\b`, "gi");

/** Devuelve los tokens sin acento sospechosos (unicos, minusculas). Vacio =
 * la salida parece correctamente acentuada. */
export function detectarFaltaDeAcentos(texto: string): string[] {
  const sospechosos = new Set<string>();
  for (const m of (texto ?? "").matchAll(TERMINACION)) sospechosos.add(m[0].toLowerCase());
  for (const m of (texto ?? "").matchAll(LISTA)) sospechosos.add(m[0].toLowerCase());
  return [...sospechosos];
}
