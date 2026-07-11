"use client";

/**
 * Saludo — "Buenos días / Buenas tardes / Buenas noches" según la hora
 * LOCAL del visitante (por eso es cliente: el servidor no conoce su
 * huso). Sin nombre: la beta tiene invitados anónimos y no inventamos.
 */
import { useEffect, useState } from "react";

function saludoPorHora(h: number): string {
  if (h >= 5 && h < 12) return "Buenos días";
  if (h >= 12 && h < 19) return "Buenas tardes";
  return "Buenas noches";
}

export function Saludo() {
  // Render inicial neutro para no romper la hidratación (SSR no sabe la hora local).
  const [texto, setTexto] = useState("Hola");
  useEffect(() => {
    setTexto(saludoPorHora(new Date().getHours()));
  }, []);
  return <span>{texto}</span>;
}
