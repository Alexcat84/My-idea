/**
 * El nombre y la promesa de cada mundo, por idioma (i18n F3; glosario en
 * DISENO §6). La fuente del español es web/lib/assets/packs_catalog.json: este
 * `es` es su COPIA y lib/catalogoMundos.test.ts falla si se separan. Las claves
 * son la `clave` de cada pack (el dominio): no se traducen.
 */
import type { PorIdioma } from "../config";

const es = {
  quality: { nombre: "Calidad y Confianza", promesa: "Que tu cliente confíe, vuelva y te recomiende." },
  health_safety: { nombre: "Seguridad y Personas", promesa: "Protege a tu gente y a tu negocio de su peor día." },
  environmental: { nombre: "Ambiente y Futuro", promesa: "Convierte lo sostenible en ventaja que se nota y se cobra." },
  seguridad_digital: { nombre: "Seguridad Digital", promesa: "Blinda tus datos, tus cuentas y la confianza de tus clientes." },
  exportacion: { nombre: "Vender al Mundo", promesa: "Lleva tu producto a clientes de otros países, con método." },
  franquicias: { nombre: "Multiplica tu Negocio", promesa: "Convierte tu negocio probado en muchos que funcionan igual." },
  risk_management: { nombre: "Riesgos Bajo Control", promesa: "Ve venir lo que puede fallar, y decide antes de que decida por ti." },
  compras: { nombre: "Tu Compra Correcta", promesa: "Compra lo que toca, al que toca, al precio que toca." },
  entrega: { nombre: "Del Taller a sus Manos", promesa: "Que llegue entero, a tiempo y sin sorpresas de costo." },
};

const en: typeof es = {
  quality: { nombre: "Quality & Trust", promesa: "Get your customers to trust you, come back and recommend you." },
  health_safety: { nombre: "Safety & People", promesa: "Protect your people and your business from their worst day." },
  environmental: { nombre: "Environment & Future", promesa: "Turn sustainability into an edge people notice and pay for." },
  seguridad_digital: { nombre: "Digital Security", promesa: "Lock down your data, your accounts and your customers' trust." },
  exportacion: { nombre: "Sell to the World", promesa: "Take your product to customers in other countries, with a method." },
  franquicias: { nombre: "Multiply Your Business", promesa: "Turn your proven business into many that work the same way." },
  risk_management: { nombre: "Risks Under Control", promesa: "See what could go wrong before it happens, and decide before it decides for you." },
  compras: { nombre: "The Right Purchase", promesa: "Buy the right thing, from the right supplier, at the right price." },
  entrega: { nombre: "From Workshop to Customer", promesa: "Make sure it arrives intact, on time and with no cost surprises." },
};

export const MUNDOS_I18N: PorIdioma<typeof es> = { es, en };
