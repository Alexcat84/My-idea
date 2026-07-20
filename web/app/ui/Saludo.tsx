"use client";

/**
 * Saludo — "Buenos días / Buenas tardes / Buenas noches" según la hora
 * LOCAL del visitante (por eso es cliente: el servidor no conoce su
 * huso). Sin nombre: la beta tiene invitados anónimos y no inventamos.
 */
import { useSyncExternalStore } from "react";

function saludoPorHora(h: number): string {
  if (h >= 5 && h < 12) return "Buenos días";
  if (h >= 12 && h < 19) return "Buenas tardes";
  return "Buenas noches";
}

const sinSuscripcion = () => () => {};

export function Saludo() {
  // "Hola" neutro en el servidor (no conoce el huso); el saludo real al
  // hidratar, sin setState en efecto (useSyncExternalStore distingue
  // snapshot de cliente y de servidor justo para esto).
  const texto = useSyncExternalStore(
    sinSuscripcion,
    () => saludoPorHora(new Date().getHours()),
    () => "Hola"
  );
  return <span>{texto}</span>;
}
