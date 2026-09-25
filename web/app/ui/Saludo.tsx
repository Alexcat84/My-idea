"use client";

/**
 * Saludo — "Buenos días / Buenas tardes / Buenas noches" según la hora
 * LOCAL del visitante (por eso es cliente: el servidor no conoce su
 * huso). Sin nombre: la beta tiene invitados anónimos y no inventamos.
 */
import { useSyncExternalStore } from "react";
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { SESION } from "@/lib/i18n/mensajes/sesion";

type TextosSaludo = (typeof SESION)["es"]["saludo"];

function saludoPorHora(h: number, t: TextosSaludo): string {
  if (h >= 5 && h < 12) return t.manana;
  if (h >= 12 && h < 19) return t.tarde;
  return t.noche;
}

const sinSuscripcion = () => () => {};

export function Saludo() {
  const t = elegir(SESION, useIdioma()).saludo;
  // "Hola" neutro en el servidor (no conoce el huso); el saludo real al
  // hidratar, sin setState en efecto (useSyncExternalStore distingue
  // snapshot de cliente y de servidor justo para esto).
  const texto = useSyncExternalStore(
    sinSuscripcion,
    () => saludoPorHora(new Date().getHours(), t),
    () => t.neutro
  );
  return <span>{texto}</span>;
}
