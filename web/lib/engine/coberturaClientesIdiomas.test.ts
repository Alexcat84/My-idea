/**
 * La frase de "validar con clientes" en los ONCE idiomas (decision del fundador, 9 oct 2026). Detectar las etapas no
 * depende del idioma: finalizarPlan neutraliza los rotulos y toda etapa llega como "## Etapa N:". Lo que depende del
 * idioma son las palabras de la accion (hablar con, entregar a, vender) y del cliente. Por nodos ya se mira
 * (coberturaContraEtapas, c0ab3a89a) y no basto en los casos reales, porque la autodeclaracion de las etapas no siempre
 * trae los nodos de clientes; por eso hay una lista por idioma. Casos: el plan real ee6de956 (sus etapas validan con
 * clientes) y el 85248377 (habla con sus empleados), escritos en ingles y en frances como los escribiria la IA.
 */
import { describe, expect, it } from "vitest";
import { coberturaContraEtapas, validaConClientesEnEtapas } from "./planRedactor";
import { textosFamiliaFaltante } from "./constants";
import type { Locale } from "../i18n/config";

function faltantesCon(cuerpo: string, idioma: Locale): string[] {
  const frase = textosFamiliaFaltante(idioma).accion_clientes;
  return coberturaContraEtapas(
    { es_completa: false, tiene_accion_clientes: false, tiene_viabilidad_economica: true, familias_faltantes: [frase] },
    { familias_tratadas: [], etapas: {} } as never,
    new Set(),
    {},
    cuerpo,
    idioma
  ).familias_faltantes;
}

const EN_VALIDA = `# Your expense app: find out whether anyone will pay every month and stay

You have a monthly subscription app for tracking personal expenses and no customer has paid yet.

## Etapa 2: Go out and talk to people who could use it

1. Take the riskiest assumptions from stage 1 and turn them into questions for potential customers.
2. Talk with people who keep or try to keep track of their personal expenses.

## Etapa 4: Launch to a small group and measure what they do, not what they say

1. Launch your first version, working or simulated, to a few users willing to try new things.`;

const EN_EMPLEADOS = `# Protect your health and your pottery workshop without slowing production

## Etapa 3: Control each hazard starting with the most effective option

1. For each priority hazard, ask yourself in this order: can I remove it?, can I change the material?

## Etapa 4: Talk to your two employees about protection

3. Ask them what bothers them about the protective equipment and what change would help them work with it.`;

const FR_VALIDE = `# Ton appli de suivi des dépenses : découvre si quelqu'un paiera chaque mois et restera

Tu as une appli d'abonnement mensuel pour suivre les dépenses personnelles et aucun client n'a encore payé.

## Etapa 2: Va parler à des personnes qui pourraient l'utiliser

1. Prends les hypothèses les plus risquées de l'étape 1 et transforme-les en questions pour des clients potentiels.
2. Parle avec des personnes qui tiennent ou essaient de tenir leurs dépenses personnelles.

## Etapa 4: Lance auprès d'un petit groupe et mesure ce qu'ils font, pas ce qu'ils disent

1. Lance ta première version, fonctionnelle ou simulée, auprès de quelques utilisateurs prêts à essayer de nouvelles choses.`;

const FR_EMPLOYES = `# Protège ta santé et celle de ton atelier sans freiner la production

## Etapa 3: Maîtrise chaque danger en commençant par le plus efficace

1. Pour chaque danger prioritaire, demande-toi dans cet ordre : puis-je le supprimer ?, puis-je changer le matériau ?

## Etapa 4: Parle à tes deux employés de la protection

3. Demande-leur ce qui les gêne dans l'équipement de protection et quel ajustement les aiderait à travailler avec.`;

describe("la frase de validar con clientes, en otros idiomas", () => {
  it.each([
    ["inglés", EN_VALIDA, "en"],
    ["francés", FR_VALIDE, "fr"],
  ] as const)("plan en %s cuyas etapas validan con clientes: la frase NO sale", (_n, cuerpo, idioma) => {
    expect(validaConClientesEnEtapas(cuerpo, idioma)).toBe(true);
    expect(faltantesCon(cuerpo, idioma)).not.toContain(textosFamiliaFaltante(idioma).accion_clientes);
  });

  it.each([
    ["inglés", EN_EMPLEADOS, "en"],
    ["francés", FR_EMPLOYES, "fr"],
  ] as const)("plan en %s que habla con sus empleados (y se pregunta a sí mismo): la frase SE QUEDA", (_n, cuerpo, idioma) => {
    expect(validaConClientesEnEtapas(cuerpo, idioma)).toBe(false);
    expect(faltantesCon(cuerpo, idioma)).toContain(textosFamiliaFaltante(idioma).accion_clientes);
  });
});

describe("cada idioma activo tiene su lista (verbos de contacto o prueba y clientes)", () => {
  // Una frase mínima por idioma: hablar con clientes / entregar a usuarios. Sin lista, no se detecta.
  const MINIMAS: Array<[Locale, string]> = [
    ["es", "Habla con tres clientes."],
    ["en", "Interview three customers."],
    ["pt", "Converse com três clientes."],
    ["fr", "Parle avec trois clients."],
    ["de", "Sprich mit drei Kunden."],
    ["it", "Parla con tre clienti."],
    ["ja", "三人の顧客に話を聞く。"],
    ["zh", "和三位客户交谈。"],
    ["ko", "고객 세 명과 대화하세요."],
    ["ar", "تحدث مع ثلاثة عملاء."],
    ["hi", "तीन ग्राहकों से बात करें।"],
  ];
  it.each(MINIMAS)("%s", (idioma, frase) => {
    expect(validaConClientesEnEtapas(`## Etapa 1: X\n\n1. ${frase}`, idioma)).toBe(true);
    // Sin el cliente, la misma acción no valida con clientes.
    const sinCliente = frase.replace(/(clientes|customers|clients|Kunden|clienti|顧客|客户|고객|عملاء|ग्राहकों)/u, "XXX");
    expect(validaConClientesEnEtapas(`## Etapa 1: X\n\n1. ${sinCliente}`, idioma)).toBe(false);
  });
});
