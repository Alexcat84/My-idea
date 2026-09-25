import { defineConfig } from "vitest/config";
import path from "path";

export default defineConfig({
  test: {
    environment: "node",
    include: ["lib/**/*.test.ts", "app/**/*.test.ts", "lib/**/*.test.tsx", "app/**/*.test.tsx"],
    // i18n (25 sep 2026): con los catálogos en once idiomas y la suite entera en
    // paralelo, las pruebas pesadas (bcrypt, importar rutas enteras, cargar todos
    // los catálogos) pasaban de los 5 s por omisión en una máquina ocupada y el
    // guardián daba falsos rojos por tiempo. Solas tardan 2 s. El límite no
    // cambia ninguna comprobación.
    testTimeout: 30_000,
    hookTimeout: 30_000,
  },
  // i18n F2: pruebas .tsx que montan JSX (rico.tsx) con el runtime automático.
  esbuild: { jsx: "automatic" },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "."),
    },
  },
});
