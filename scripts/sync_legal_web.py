"""Publica los textos legales en la web (encargo del fundador del 6 oct 2026, punto 6).

Una sola fuente: docs/legal/*.md (espanol) y docs/legal/fr/*.md (frances). Este script escribe la copia que lee la web,
web/lib/legal/textos.ts, sin la cabecera de borrador (todo lo anterior al titulo del documento). La revision
profesional queda pendiente: cuando el profesional ajuste un texto, se edita el .md y se vuelve a correr esto.
Guarda: engine/test_legal_web.py.

La VERSION de los textos que se aceptan (decision del fundador, 7 oct 2026: consentimiento versionado) tiene una sola
fuente, docs/legal/version.json: el historial de versiones con la huella (sha256) de los Terminos y la Privacidad de
cada una, en espanol y en frances. Este script la publica en web/lib/legal/version.ts (un archivo aparte y pequeno:
el modal del cliente lo importa sin cargar los textos enteros). Si cambias un texto versionado, sube la version:

    python scripts/sync_legal_web.py --nueva-version AAAA-MM-DD

Eso anade la version con la huella de los textos de hoy y publica todo. Guarda: engine/test_version_legal.py, que
falla si los textos cambian sin subir la version.
"""
import hashlib
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DESTINO = BASE / "web" / "lib" / "legal" / "textos.ts"
DESTINO_VERSION = BASE / "web" / "lib" / "legal" / "version.ts"
REGISTRO_VERSION = BASE / "docs" / "legal" / "version.json"

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


def registro_version():
    return json.loads(REGISTRO_VERSION.read_text(encoding="utf-8"))


def huella_de(por_documento):
    """sha256 de los textos dados ({documento: {idioma: texto}}), con una serializacion canonica."""
    canon = json.dumps(por_documento, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def huella_legal():
    """La huella de los textos versionados tal como se publican hoy (los documentos del registro, es y fr)."""
    todos = textos()
    return huella_de({doc: todos[doc] for doc in registro_version()["documentos"]})


def generar_version():
    reg = registro_version()
    vigente = next(v for v in reg["versiones"] if v["version"] == reg["vigente"])
    return ("// GENERADO por scripts/sync_legal_web.py desde docs/legal/version.json. No editar a mano: para subir la\n"
            "// version corre python scripts/sync_legal_web.py --nueva-version AAAA-MM-DD (guarda:\n"
            "// engine/test_version_legal.py, que falla si los textos cambian sin subir la version).\n"
            "/** La versión vigente de los Términos y la Privacidad: la que se pide aceptar a las cuentas reales. */\n"
            f"export const VERSION_LEGAL = \"{reg['vigente']}\";\n"
            "/** sha256 de esos textos (es y fr) en la versión vigente: se guarda con cada aceptación. */\n"
            f"export const HUELLA_LEGAL = \"{vigente['huella']}\";\n")


def nueva_version(version):
    """Anade una version al registro con la huella de los textos de hoy. Falla ruidoso si no hay nada que versionar."""
    reg = registro_version()
    huella = huella_legal()
    if any(v["huella"] == huella for v in reg["versiones"]):
        sys.exit("Los textos versionados no cambiaron: no hay version nueva que subir.")
    if any(v["version"] >= version for v in reg["versiones"]):
        sys.exit(f"La version {version} no es posterior a la ultima del historial ({reg['vigente']}).")
    reg["versiones"].append({"version": version, "huella": huella})
    reg["vigente"] = version
    REGISTRO_VERSION.write_text(json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def generar():
    return ("// GENERADO por scripts/sync_legal_web.py desde docs/legal/. No editar a mano: se edita el .md y se vuelve\n"
            "// a sincronizar (guarda: engine/test_legal_web.py).\n"
            "export type DocumentoLegal = \"privacidad\" | \"terminos\" | \"cookies\";\n"
            "export const TEXTOS_LEGALES: Record<DocumentoLegal, { es: string; fr: string }> = "
            + json.dumps(textos(), ensure_ascii=False, indent=2) + ";\n")


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--nueva-version":
        nueva_version(sys.argv[2])
    elif len(sys.argv) != 1:
        sys.exit("uso: python scripts/sync_legal_web.py [--nueva-version AAAA-MM-DD]")
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(generar(), encoding="utf-8", newline="\n")
    DESTINO_VERSION.write_text(generar_version(), encoding="utf-8", newline="\n")
    print("textos legales publicados en", DESTINO.relative_to(BASE))
    print("version legal vigente", registro_version()["vigente"], "en", DESTINO_VERSION.relative_to(BASE))
