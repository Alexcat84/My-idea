"""Publica los textos legales en la web (encargo del fundador del 6 oct 2026, punto 6).

Una sola fuente: docs/legal/*.md (espanol) y sus traducciones en docs/legal/<idioma>/ (los once idiomas desde el 7 oct
2026, encargo I18N AL DIA; el frances conserva sus propios nombres de fichero, los demas usan los del espanol). Este
script escribe la copia que lee la web, web/lib/legal/textos.ts, sin la cabecera de borrador (todo lo anterior al
titulo del documento). La revision profesional queda pendiente: cuando el profesional ajuste un texto, se edita el .md
y se vuelve a correr esto. Guarda: engine/test_legal_web.py.

Una traduccion solo se publica cuando tiene su huella en docs/legal/<idioma>/huellas.json (la huella del texto espanol
del que salio, que escribe python scripts/legal_huellas.py <idioma>): es la senal de que esta terminada. Mientras no la
tenga, la pagina de ese idioma sigue en espanol. Si el espanol cambia despues, engine/test_legal_huellas.py la marca
como vieja hasta que se retraduzca y se vuelva a escribir su huella.

La VERSION de los textos que se aceptan (decision del fundador, 7 oct 2026: consentimiento versionado) tiene una sola
fuente, docs/legal/version.json: el historial de versiones con la huella (sha256) de los Terminos y la Privacidad de
cada una, en espanol y en frances (las versiones que prevalecen; las demas traducciones no entran en la huella y
publicarlas no sube la version). Este script la publica en web/lib/legal/version.ts (un archivo aparte y pequeno:
la linea del consentimiento lo importa sin cargar los textos enteros). Si cambias un texto versionado, sube la version:

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

# Los documentos publicados y su fichero espanol de origen (docs/legal/<origen>).
ORIGENES = {"privacidad": "PRIVACIDAD.md", "terminos": "TERMINOS.md", "cookies": "COOKIES.md"}
# Los idiomas de las traducciones, en el orden de la marca (web/lib/i18n/config.ts, LOCALES, sin el espanol).
IDIOMAS_TRADUCCION = ["en", "pt", "fr", "de", "it", "ja", "zh", "ko", "ar", "hi"]
# El frances se tradujo antes y conserva sus nombres; las demas traducciones usan los del espanol.
NOMBRES_FR = {"PRIVACIDAD.md": "CONFIDENTIALITE.md", "TERMINOS.md": "CONDITIONS.md", "COOKIES.md": "TEMOINS.md"}
# Las versiones que prevalecen en caso de discrepancia: solo ellas entran en la huella de la version legal.
IDIOMAS_VINCULANTES = ("es", "fr")


def ruta_origen(origen, base=BASE):
    return base / "docs" / "legal" / origen


def ruta_traduccion(idioma, origen, base=BASE):
    nombre = NOMBRES_FR[origen] if idioma == "fr" else origen
    return base / "docs" / "legal" / idioma / nombre


def ruta_huellas(idioma, base=BASE):
    return base / "docs" / "legal" / idioma / "huellas.json"


def huellas_guardadas(idioma, base=BASE):
    """Las huellas que guarda la carpeta de una traduccion ({origen espanol: sha256}); vacio si aun no tiene."""
    ruta = ruta_huellas(idioma, base)
    return json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else {}


def publicable(md):
    """Quita la cabecera de borrador: el documento empieza en su segundo titulo de nivel 1."""
    md = md.replace("\r\n", "\n").strip()
    partes = md.split("\n# ")
    if md.startswith("# ") and len(partes) > 1:
        return "# " + "\n# ".join(partes[1:]).strip()
    return md


def huella_texto(md):
    """sha256 del texto publicable de un .md (sin cabecera de borrador ni finales de linea de Windows)."""
    return hashlib.sha256(publicable(md).encode("utf-8")).hexdigest()


def textos(base=BASE):
    """{documento: {idioma: texto publicable}}: el espanol siempre, y cada traduccion que existe y tiene su huella."""
    salida = {}
    for doc, origen in ORIGENES.items():
        salida[doc] = {"es": publicable(ruta_origen(origen, base).read_text(encoding="utf-8"))}
        for idioma in IDIOMAS_TRADUCCION:
            ruta = ruta_traduccion(idioma, origen, base)
            if ruta.exists() and origen in huellas_guardadas(idioma, base):
                salida[doc][idioma] = publicable(ruta.read_text(encoding="utf-8"))
    return salida


def registro_version():
    return json.loads(REGISTRO_VERSION.read_text(encoding="utf-8"))


def huella_de(por_documento):
    """sha256 de los textos dados ({documento: {idioma: texto}}), con una serializacion canonica."""
    canon = json.dumps(por_documento, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def huella_legal():
    """La huella de los textos versionados tal como se publican hoy (los documentos del registro, solo es y fr)."""
    todos = textos()
    return huella_de({doc: {i: todos[doc][i] for i in IDIOMAS_VINCULANTES}
                      for doc in registro_version()["documentos"]})


def generar_version():
    reg = registro_version()
    vigente = next(v for v in reg["versiones"] if v["version"] == reg["vigente"])
    return ("// GENERADO por scripts/sync_legal_web.py desde docs/legal/version.json. No editar a mano: para subir la\n"
            "// version corre python scripts/sync_legal_web.py --nueva-version AAAA-MM-DD (guarda:\n"
            "// engine/test_version_legal.py, que falla si los textos cambian sin subir la version).\n"
            "/** La versión vigente de los Términos y la Privacidad: la que se pide aceptar en el primer envío de datos. */\n"
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
            "/** Por documento, el texto en español y en cada idioma cuya traducción está publicada (con su huella). */\n"
            "export const TEXTOS_LEGALES: Record<DocumentoLegal, { es: string; [idioma: string]: string | undefined }> = "
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
