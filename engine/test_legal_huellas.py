"""Vigencia de las traducciones de los textos legales (encargo del fundador del 7 oct 2026, I18N AL DIA).

Los textos legales se publican en los once idiomas. El espanol es la fuente: cada traduccion (docs/legal/<idioma>/)
sale de un texto espanol concreto, y si el espanol cambia despues, la traduccion queda VIEJA aunque nadie lo note: la
persona leeria en su idioma unas condiciones que ya no son las vigentes. Por eso cada carpeta de traduccion guarda en
docs/legal/<idioma>/huellas.json la huella (sha256 del texto publicable, sin la cabecera de borrador) del fichero
espanol del que salio:

    {"COOKIES.md": "<sha256>", "PRIVACIDAD.md": "<sha256>", "TERMINOS.md": "<sha256>"}

Las claves son los nombres de los ficheros ESPANOLES de origen (tambien en fr, cuyos ficheros se llaman distinto). La
huella se escribe con python scripts/legal_huellas.py <idioma> en cuanto la traduccion esta terminada, y es tambien la
senal de "lista": scripts/sync_legal_web.py solo publica una traduccion que tiene su huella (una a medio escribir, sin
huella, queda en curso y la pagina sigue en espanol). Esta guarda falla si la huella guardada de una traduccion no
coincide con la del espanol vigente, o si hay huella de un fichero que no existe, y dice que idiomas y que ficheros
quedaron viejos. Prueba en rojo primero: nacio antes que scripts/legal_huellas.py y que las huellas.
"""
import json
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

import legal_huellas as lh  # noqa: E402
import sync_legal_web as sl  # noqa: E402


def test_ninguna_traduccion_queda_vieja():
    viejas = lh.traducciones_viejas()
    assert viejas == [], (
        "Traducciones legales sin huella o hechas sobre un espanol que ya cambio (retraducir lo que cambio y luego "
        "correr python scripts/legal_huellas.py <idioma>):\n  " + "\n  ".join(viejas)
    )


def test_el_frances_y_el_ingles_estan_completos_y_con_huella():
    for idioma in ("fr", "en"):
        huellas = json.loads((BASE / "docs" / "legal" / idioma / "huellas.json").read_text(encoding="utf-8"))
        assert sorted(huellas) == sorted(sl.ORIGENES.values()), (idioma, sorted(huellas))
        for origen in sl.ORIGENES.values():
            assert sl.ruta_traduccion(idioma, origen).exists(), (idioma, origen)


def _carpeta_de_juguete(raiz: Path):
    (raiz / "docs" / "legal" / "en").mkdir(parents=True)
    (raiz / "docs" / "legal" / "PRIVACIDAD.md").write_text(
        "# BORRADOR\n\n> nota\n\n# Politica\n\nTexto uno.\n", encoding="utf-8")
    (raiz / "docs" / "legal" / "TERMINOS.md").write_text("# Terminos\n\nTexto.\n", encoding="utf-8")
    (raiz / "docs" / "legal" / "COOKIES.md").write_text("# Cookies\n\nTexto.\n", encoding="utf-8")
    (raiz / "docs" / "legal" / "en" / "PRIVACIDAD.md").write_text("# Policy\n\nText one.\n", encoding="utf-8")


def test_la_guarda_muerde_con_huella_vieja():
    """Dos fixtures (M7): sin huella, en curso y sin publicar; con la huella de hoy, publicada y al dia; el espanol
    cambia, vieja."""
    with tempfile.TemporaryDirectory() as tmp:
        raiz = Path(tmp)
        _carpeta_de_juguete(raiz)
        assert lh.traducciones_viejas(raiz) == []
        assert lh.traducciones_en_curso(raiz) == ["en/PRIVACIDAD.md"]
        assert "en" not in sl.textos(raiz)["privacidad"], "sin huella no se publica"

        lh.escribir_huellas("en", raiz)
        assert lh.traducciones_viejas(raiz) == []
        assert lh.traducciones_en_curso(raiz) == []
        assert sl.textos(raiz)["privacidad"]["en"] == "# Policy\n\nText one."

        # Cambiar solo la cabecera de borrador no deja vieja la traduccion: la huella es del texto publicable.
        es = raiz / "docs" / "legal" / "PRIVACIDAD.md"
        es.write_text(es.read_text(encoding="utf-8").replace("> nota", "> otra nota"), encoding="utf-8")
        assert lh.traducciones_viejas(raiz) == []

        # Cambiar el texto que se publica, si.
        es.write_text(es.read_text(encoding="utf-8").replace("Texto uno.", "Texto dos."), encoding="utf-8")
        viejas = lh.traducciones_viejas(raiz)
        assert len(viejas) == 1 and "en" in viejas[0] and "PRIVACIDAD.md" in viejas[0] and "vieja" in viejas[0]


def test_una_huella_de_un_fichero_que_no_existe_es_un_error():
    with tempfile.TemporaryDirectory() as tmp:
        raiz = Path(tmp)
        _carpeta_de_juguete(raiz)
        lh.escribir_huellas("en", raiz)
        ruta = raiz / "docs" / "legal" / "en" / "huellas.json"
        huellas = json.loads(ruta.read_text(encoding="utf-8"))
        huellas["TERMINOS.md"] = huellas["PRIVACIDAD.md"]
        ruta.write_text(json.dumps(huellas), encoding="utf-8")
        viejas = lh.traducciones_viejas(raiz)
        assert len(viejas) == 1 and "TERMINOS.md" in viejas[0], viejas


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
