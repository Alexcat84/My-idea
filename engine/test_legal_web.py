"""Paginas legales publicadas (encargo del fundador del 6 oct 2026, punto 6).

La unica fuente de los textos legales son docs/legal/*.md (espanol) y docs/legal/fr/*.md (frances). La web los recibe
generados en web/lib/legal/textos.ts por scripts/sync_legal_web.py, sin la cabecera de borrador. Esta guarda falla si
la copia web quedo atrasada, si un texto publicado conserva una marca pendiente o la cabecera de borrador, o si nombra
libros (regla D1: ningun origen llega al cliente). Prueba en rojo primero.
"""
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

import sync_legal_web as sl  # noqa: E402


def test_la_copia_web_esta_al_dia():
    actual = (BASE / "web/lib/legal/textos.ts").read_text(encoding="utf-8")
    assert actual == sl.generar(), "web/lib/legal/textos.ts atrasado: corre python scripts/sync_legal_web.py"


def test_ningun_texto_publicado_conserva_marcas_ni_cabecera():
    for doc, por_idioma in sl.textos().items():
        for idioma, texto in por_idioma.items():
            plano = texto.replace("\n", " ")
            for prohibido in ("POR VERIFICAR", "VÉRIFIER", "BORRADOR", "ÉBAUCHE", "[fecha", "[date"):
                assert prohibido not in plano, (doc, idioma, prohibido)
            assert "libro" not in plano.lower() and "livre" not in plano.lower(), (doc, idioma, "nombra libros")
            assert plano.lstrip().startswith("# "), (doc, idioma, "debe empezar por su titulo")


def test_la_cabecera_de_borrador_se_quita():
    md = "# BORRADOR PENDIENTE\n\n> nota interna\n\n# Política de privacidad de My Idea\n\nTexto."
    assert sl.publicable(md) == "# Política de privacidad de My Idea\n\nTexto."


if __name__ == "__main__":
    fallos = 0
    for nombre, f in list(globals().items()):
        if nombre.startswith("test_") and callable(f):
            try:
                f()
                print("OK  ", nombre)
            except Exception as e:  # noqa: BLE001
                fallos += 1
                print("FALLA", nombre, repr(e)[:300])
    sys.exit(1 if fallos else 0)
