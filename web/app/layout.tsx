import type { Metadata, Viewport } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { elegir, htmlDir, htmlLang } from "@/lib/i18n/config";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";
import { SITIO } from "@/lib/i18n/mensajes/sitio";
import { idiomaDeCookies } from "@/lib/i18n/servidor";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

// Instrument Serif se fue con la portada nueva: solo la usaba el eslogan en
// itálica del hero, que la masa reemplazó. Nada más en web/ leía su variable.

// i18n F2: la descripción sale del catálogo en el idioma de la cookie; el
// título es la marca y no se traduce.
export async function generateMetadata(): Promise<Metadata> {
  return {
    title: "My Idea",
    description: elegir(SITIO, await idiomaDeCookies()).descripcion,
  };
}

export const viewport: Viewport = {
  themeColor: "#000000",
};

// Phase 3.7 (D2): sello de versión permanente. Vercel inyecta el sha del
// commit en build; en dev local no existe y el sello dice "dev". Zanja
// para siempre el "¿qué build estoy viendo?" de las sesiones del fundador.
const SELLO_VERSION = (process.env.VERCEL_GIT_COMMIT_SHA ?? "dev").slice(0, 7);

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  // i18n F2: el idioma de la interfaz sale de la cookie que escribe proxy.ts.
  const idioma = await idiomaDeCookies();
  return (
    <html lang={htmlLang(idioma)} dir={htmlDir(idioma)} className={`${inter.variable} h-full antialiased`}>
      <body className="min-h-full flex flex-col bg-bg text-ink">
        <IdiomaProvider idioma={idioma}>{children}</IdiomaProvider>
        <footer className="px-4 py-2 text-right text-[10px] text-white/25 select-all" aria-label={elegir(SITIO, idioma).etiquetaVersion}>
          v·{SELLO_VERSION}
        </footer>
      </body>
    </html>
  );
}
