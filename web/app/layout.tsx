import type { Metadata, Viewport } from "next";
import { Instrument_Serif, Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

// Solo la landing la usa (eslogan en itálica); el diseño del fundador
// la pide como 'Instrument Serif' y Landing.tsx la lee por la variable.
const instrument = Instrument_Serif({
  variable: "--font-serif",
  weight: "400",
  style: ["normal", "italic"],
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "My Idea",
  description: "El espacio donde tus ideas se trabajan.",
};

export const viewport: Viewport = {
  themeColor: "#000000",
};

// Phase 3.7 (D2): sello de versión permanente. Vercel inyecta el sha del
// commit en build; en dev local no existe y el sello dice "dev". Zanja
// para siempre el "¿qué build estoy viendo?" de las sesiones del fundador.
const SELLO_VERSION = (process.env.VERCEL_GIT_COMMIT_SHA ?? "dev").slice(0, 7);

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es" className={`${inter.variable} ${instrument.variable} h-full antialiased`}>
      <body className="min-h-full flex flex-col bg-bg text-ink">
        {children}
        <footer className="px-4 py-2 text-right text-[10px] text-white/25 select-all" aria-label="versión">
          v·{SELLO_VERSION}
        </footer>
      </body>
    </html>
  );
}
