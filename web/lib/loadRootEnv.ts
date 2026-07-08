/**
 * Fase 3.0: en desarrollo local, carga el .env de la RAIZ del repo (el
 * mismo que ya usa engine/prototipo_motor.py y engine/db.py) en vez de
 * mantener un web/.env.local separado con las claves duplicadas -- una
 * sola fuente de verdad para los secretos locales. Alias las variables
 * sin prefijo a su equivalente NEXT_PUBLIC_* (Next.js solo inyecta al
 * bundle del navegador las variables con ese prefijo exacto; no hay
 * forma de evitarlo, asi que este archivo hace el mapeo una sola vez).
 *
 * En Vercel esto no aplica: las variables de entorno se configuran
 * directo en Project Settings, con sus nombres NEXT_PUBLIC_* ya
 * correctos -- este loader es puramente una comodidad de desarrollo
 * local, nunca corre en produccion (no hay archivo .env que cargar ahi).
 *
 * Fase 3.0.1: la logica vive en aplicarEnv(rutaEnv), exportada para que
 * el test la ejercite contra un .env temporal de fixture en vez de exigir
 * el .env real (el verde de la suite no puede depender de secretos
 * locales). El side-effect del import queda identico al original.
 */
import { existsSync } from "node:fs";
import path from "node:path";

const ROOT_ENV_PATH = path.resolve(__dirname, "..", "..", ".env");

const ALIAS: Record<string, string> = {
  SUPABASE_URL: "NEXT_PUBLIC_SUPABASE_URL",
  SUPABASE_ANON_KEY: "NEXT_PUBLIC_SUPABASE_ANON_KEY",
};

/** Carga el .env indicado (si existe) en process.env y aplica los alias
 *  NEXT_PUBLIC_*. Devuelve true si el archivo existia y se cargo. */
export function aplicarEnv(rutaEnv: string): boolean {
  if (!existsSync(rutaEnv)) {
    return false;
  }
  process.loadEnvFile(rutaEnv);
  for (const [origen, destino] of Object.entries(ALIAS)) {
    if (!process.env[destino] && process.env[origen]) {
      process.env[destino] = process.env[origen];
    }
  }
  return true;
}

aplicarEnv(ROOT_ENV_PATH);
