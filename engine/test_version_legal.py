"""La version de los textos legales (decision del fundador, 7 oct 2026: consentimiento versionado como en iching-app).

Toda identidad que envia datos (la invisible tambien; correccion del fundador del mismo dia) acepta los Terminos y la
Privacidad por VERSION, y la app vuelve a pedir la aceptacion en el siguiente envio cuando la version cambia (tabla
aceptaciones_legales, migracion 050). La version tiene UNA sola fuente: docs/legal/version.json,
con el historial de versiones y la huella (sha256) de los textos de cada una. scripts/sync_legal_web.py la publica en
web/lib/legal/version.ts, que es lo unico que lee la app.

Esta guarda falla si los textos versionados cambian sin subir la version (la huella vigente deja de coincidir), si la
vigente no es la ultima del historial, si dos versiones comparten huella o si la copia web quedo atrasada. Prueba en
rojo primero: nacio antes que version.json.
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

import sync_legal_web as sl  # noqa: E402

REGISTRO = BASE / "docs" / "legal" / "version.json"


def _registro():
    return json.loads(REGISTRO.read_text(encoding="utf-8"))


def test_el_registro_de_versiones_existe_y_tiene_forma():
    reg = _registro()
    assert reg["documentos"] == ["terminos", "privacidad"], "se versionan los Terminos y la Privacidad"
    assert isinstance(reg["vigente"], str) and reg["vigente"]
    assert reg["versiones"], "el historial no puede estar vacio"
    for v in reg["versiones"]:
        assert set(v) == {"version", "huella"}, v
        assert len(v["huella"]) == 64 and all(c in "0123456789abcdef" for c in v["huella"]), v


def test_los_textos_no_cambian_sin_subir_la_version():
    reg = _registro()
    vigente = next(v for v in reg["versiones"] if v["version"] == reg["vigente"])
    assert sl.huella_legal() == vigente["huella"], (
        "Los Terminos o la Privacidad cambiaron y la version vigente sigue siendo " + reg["vigente"] + ". "
        "Sube la version: python scripts/sync_legal_web.py --nueva-version AAAA-MM-DD"
    )


def test_la_vigente_es_la_ultima_y_el_historial_no_se_repite():
    reg = _registro()
    versiones = [v["version"] for v in reg["versiones"]]
    huellas = [v["huella"] for v in reg["versiones"]]
    assert reg["vigente"] == versiones[-1], "la vigente es siempre la ultima del historial"
    assert versiones == sorted(versiones) and len(set(versiones)) == len(versiones), "versiones crecientes y unicas"
    assert len(set(huellas)) == len(huellas), "una version nueva sin cambio de texto no es una version"


def test_la_huella_muerde_si_un_texto_cambia():
    """Dos fixtures (M7): el mismo juego de textos da la misma huella; una coma de mas, otra."""
    base = {"terminos": {"es": "# T\n\nTexto.", "fr": "# T\n\nTexte."},
            "privacidad": {"es": "# P\n\nTexto.", "fr": "# P\n\nTexte."}}
    igual = json.loads(json.dumps(base))
    cambiado = json.loads(json.dumps(base))
    cambiado["privacidad"]["fr"] = "# P\n\nTexte,."
    assert sl.huella_de(base) == sl.huella_de(igual)
    assert sl.huella_de(base) != sl.huella_de(cambiado)
    # El francés cuenta igual que el español: cambiar solo un idioma también cambia la huella.
    solo_es = json.loads(json.dumps(base))
    solo_es["terminos"]["es"] = "# T\n\nOtro texto."
    assert sl.huella_de(base) != sl.huella_de(solo_es)


def test_la_huella_cubre_solo_el_espanol_y_el_frances():
    """Las otras traducciones (I18N AL DIA, 7 oct 2026) son de cortesia: en caso de discrepancia prevalece el espanol
    (y el frances en Quebec). Publicar o corregir una traduccion no cambia lo que se acepta, asi que no sube la
    version ni obliga a nadie a volver a aceptar. Su vigencia frente al espanol la guarda test_legal_huellas.py."""
    todos = sl.textos()
    assert set(todos["privacidad"]) - {"es", "fr"}, "debe haber al menos una traduccion mas que es y fr (el ingles)"
    solo_vinculantes = {doc: {i: todos[doc][i] for i in ("es", "fr")} for doc in _registro()["documentos"]}
    assert sl.huella_legal() == sl.huella_de(solo_vinculantes)


def test_la_web_lee_la_version_vigente():
    reg = _registro()
    vigente = next(v for v in reg["versiones"] if v["version"] == reg["vigente"])
    actual = (BASE / "web/lib/legal/version.ts").read_text(encoding="utf-8")
    assert actual == sl.generar_version(), "web/lib/legal/version.ts atrasado: corre python scripts/sync_legal_web.py"
    assert f'VERSION_LEGAL = "{reg["vigente"]}"' in actual
    assert f'HUELLA_LEGAL = "{vigente["huella"]}"' in actual


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
