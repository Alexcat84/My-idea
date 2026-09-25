/** La fila "Potencia tu idea" (app/ui/PotenciaTuIdea.tsx, canon 07-B / 08). Las
 * cifras salen de precios.ts: aquí solo va la frase con su {{n}}. */
import type { PorIdioma } from "../config";

const es = {
  titulo: "Potencia tu idea",
  creditos: "{{n}} créditos",
  incluido: "Incluido",
  tusNumeros: "Tus Números",
  tusNumerosPromesa: "Tus cifras reales convertidas en margen, punto de equilibrio y escenarios.",
  tusNumerosNota: "Incluido con tu plan · una vez por idea",
  completado: "Completado",
  activo: "Activo",
  activoConProgreso: "Activo · <progreso>{{hechos}}/{{total}}</progreso>",
  planBasico: "Plan básico",
  listoParaTuPlan: "Listo para tu plan",
  seAbreConTuPlan: "Se abre con tu plan",
  abriendo: "Abriendo…",
  sinPublicar: "sin publicar",
  errorAbrir: "No pudimos abrirlo; intenta de nuevo.",
  basicoEspera: "Tu plan básico te espera · el completo: {{n}} créditos, solo si la IA lo entrega",
  diagnosticoEspera: "Tu diagnóstico te espera · su plan: {{n}} créditos",
  empiezaDiagnostico: "Empieza con un diagnóstico gratis",
};

const en: typeof es = {
  titulo: "Power up your idea",
  creditos: "{{n}} credits",
  incluido: "Included",
  tusNumeros: "Your Numbers",
  tusNumerosPromesa: "Your real figures turned into margin, break-even point, and scenarios.",
  tusNumerosNota: "Included with your plan · once per idea",
  completado: "Completed",
  activo: "Active",
  activoConProgreso: "Active · <progreso>{{hechos}}/{{total}}</progreso>",
  planBasico: "Basic plan",
  listoParaTuPlan: "Ready for your plan",
  seAbreConTuPlan: "Opens with your plan",
  abriendo: "Opening…",
  sinPublicar: "unpublished",
  errorAbrir: "We couldn't open it; try again.",
  basicoEspera: "Your basic plan is waiting · the full one: {{n}} credits, only if the AI delivers it",
  diagnosticoEspera: "Your diagnosis is waiting · its plan: {{n}} credits",
  empiezaDiagnostico: "Start with a free diagnosis",
};

export const POTENCIA_TU_IDEA: PorIdioma<typeof es> = { es, en };
