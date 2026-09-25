/** La sesión en el encabezado: ui/BotonSalir.tsx y ui/Saludo.tsx. */
import type { PorIdioma } from "../config";

const es = {
  salir: "Salir",
  saludo: {
    manana: "Buenos días",
    tarde: "Buenas tardes",
    noche: "Buenas noches",
    /** El neutro del servidor, que no conoce el huso del visitante. */
    neutro: "Hola",
  },
};

const en: typeof es = {
  salir: "Log out",
  saludo: {
    manana: "Good morning",
    tarde: "Good afternoon",
    noche: "Good evening",
    neutro: "Hi",
  },
};

const fr: typeof es = {
  salir: "Se déconnecter",
  saludo: {
    manana: "Bonjour",
    tarde: "Bon après-midi",
    noche: "Bonsoir",
    neutro: "Salut",
  },
};

const pt: typeof es = {
  salir: "Sair",
  saludo: {
    manana: "Bom dia",
    tarde: "Boa tarde",
    noche: "Boa noite",
    neutro: "Olá",
  },
};

const de: typeof es = {
  salir: "Abmelden",
  saludo: {
    manana: "Guten Morgen",
    tarde: "Guten Tag",
    noche: "Guten Abend",
    neutro: "Hallo",
  },
};

const it: typeof es = {
  salir: "Esci",
  saludo: {
    manana: "Buongiorno",
    tarde: "Buon pomeriggio",
    noche: "Buonasera",
    neutro: "Ciao",
  },
};

const ja: typeof es = {
  salir: "ログアウト",
  saludo: {
    manana: "おはようございます",
    tarde: "こんにちは",
    noche: "こんばんは",
    neutro: "こんにちは",
  },
};

const zh: typeof es = {
  salir: "退出",
  saludo: {
    manana: "早上好",
    tarde: "下午好",
    noche: "晚上好",
    neutro: "你好",
  },
};

const ko: typeof es = {
  salir: "로그아웃",
  saludo: {
    manana: "좋은 아침이에요",
    tarde: "좋은 오후예요",
    noche: "좋은 저녁이에요",
    neutro: "안녕하세요",
  },
};

const ar: typeof es = {
  salir: "تسجيل الخروج",
  saludo: {
    manana: "صباح الخير",
    tarde: "مساء الخير",
    noche: "طاب مساؤكم",
    neutro: "مرحبًا",
  },
};

const hi: typeof es = {
  salir: "लॉग आउट",
  saludo: {
    manana: "सुप्रभात",
    tarde: "नमस्ते",
    noche: "शुभ संध्या",
    neutro: "नमस्ते",
  },
};

export const SESION: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
