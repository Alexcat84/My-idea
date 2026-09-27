import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  // Portada (ui/portada): en las muestras de la masa hubo un fallo por dos
  // cosas con el mismo nombre. Aqui ninguna declaracion puede repetir ni
  // tapar otra, ni usarse antes de existir. (Los shaders tienen su propia
  // guarda: masa/glsl.test.ts.)
  {
    files: ["app/ui/portada/**/*.{ts,tsx}"],
    rules: {
      "no-var": "error",
      "no-redeclare": "off",
      "@typescript-eslint/no-redeclare": "error",
      "no-shadow": "off",
      "@typescript-eslint/no-shadow": ["error", { hoist: "all", builtinGlobals: false }],
      "no-use-before-define": "off",
      "@typescript-eslint/no-use-before-define": ["error", { functions: false }],
      "@typescript-eslint/no-unused-vars": ["error", { argsIgnorePattern: "^_" }],
    },
  },
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
  ]),
]);

export default eslintConfig;
