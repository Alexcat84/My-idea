import { defineConfig } from "vitest/config";
import path from "path";

export default defineConfig({
  test: {
    environment: "node",
    include: ["lib/**/*.test.ts", "app/**/*.test.ts", "lib/**/*.test.tsx", "app/**/*.test.tsx"],
  },
  // i18n F2: pruebas .tsx que montan JSX (rico.tsx) con el runtime automático.
  esbuild: { jsx: "automatic" },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "."),
    },
  },
});
