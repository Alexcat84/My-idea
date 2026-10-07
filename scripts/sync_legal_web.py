"""Publica los textos legales en la web (encargo del fundador del 6 oct 2026, punto 6).

Una sola fuente: docs/legal/*.md (espanol) y docs/legal/fr/*.md (frances). Este script escribe la copia que lee la web,
web/lib/legal/textos.ts, sin la cabecera de borrador (todo lo anterior al titulo del documento). La revision
profesional queda pendiente: cuando el profesional ajuste un texto, se edita el .md y se vuelve a correr esto.
Guarda: engine/test_legal_web.py.
"""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DESTINO = BASE / "web" / "lib" / "legal" / "textos.ts"

FUENTES = {
    "privacidad": {"es": "docs/legal/PRIVACIDAD.md", "fr": "docs/legal/fr/CONFIDENTIALITE.md"},
    "terminos": {"es": "docs/legal/TERMINOS.md", "fr": "docs/legal/fr/CONDITIONS.md"},
    "cookies": {"es": "docs/legal/COOKIES.md", "fr": "docs/legal/fr/TEMOINS.md"},
}


def publicable(md):
    """Quita la cabecera de borrador: el documento empieza en su segundo titulo de nivel 1."""
    md = md.replace("\r\n", "\n").strip()
    partes = md.split("\n# ")
    if md.startswith("# ") and len(partes) > 1:
        return "# " + "\n# ".join(partes[1:]).strip()
    return md


def textos():
    return {doc: {idioma: publicable((BASE / ruta).read_text(encoding="utf-8")) for idioma, ruta in rutas.items()}
            for doc, rutas in FUENTES.items()}


def generar():
    return ("// GENERADO por scripts/sync_legal_web.py desde docs/legal/. No editar a mano: se edita el .md y se vuelve\n"
            "// a sincronizar (guarda: engine/test_legal_web.py).\n"
            "export type DocumentoLegal = \"privacidad\" | \"terminos\" | \"cookies\";\n"
            "export const TEXTOS_LEGALES: Record<DocumentoLegal, { es: string; fr: string }> = "
            + json.dumps(textos(), ensure_ascii=False, indent=2) + ";\n")


if __name__ == "__main__":
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(generar(), encoding="utf-8", newline="\n")
    print("textos legales publicados en", DESTINO.relative_to(BASE))
