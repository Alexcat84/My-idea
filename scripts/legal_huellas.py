"""Huellas de vigencia de las traducciones legales (encargo del fundador del 7 oct 2026, I18N AL DIA).

Cada traduccion de los textos legales (docs/legal/<idioma>/) sale de un texto espanol concreto. Su carpeta guarda en
huellas.json la huella (sha256 del texto publicable, sin la cabecera de borrador) del fichero espanol del que salio:

    {
      "COOKIES.md": "<sha256>",
      "PRIVACIDAD.md": "<sha256>",
      "TERMINOS.md": "<sha256>"
    }

Las claves son los nombres de los ficheros ESPANOLES de origen (tambien en fr, cuyos ficheros se llaman distinto).

Uso:
    python scripts/legal_huellas.py <idioma>       escribe la huella de cada traduccion que existe en ese idioma, con
                                                   el espanol de HOY: correlo en cuanto la traduccion este terminada
                                                   (antes no: la huella es la senal de que esta lista y la publica).
                                                   Despues, python scripts/sync_legal_web.py para publicarla.
    python scripts/legal_huellas.py --comprobar    lista las traducciones viejas y las que siguen en curso (sin huella);
                                                   sale con codigo 1 si hay alguna vieja.

Guarda: engine/test_legal_huellas.py (falla si una huella guardada no coincide con el espanol vigente).
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sync_legal_web as sl  # noqa: E402


def huella_de_origen(origen, base=sl.BASE):
    """La huella del fichero espanol de origen tal como se publica hoy."""
    return sl.huella_texto(sl.ruta_origen(origen, base).read_text(encoding="utf-8"))


def traducciones_viejas(base=sl.BASE):
    """Cada huella guardada que ya no coincide con el espanol vigente, o que apunta a una traduccion que no existe."""
    viejas = []
    for idioma in sl.IDIOMAS_TRADUCCION:
        for origen, huella in sorted(sl.huellas_guardadas(idioma, base).items()):
            if origen not in sl.ORIGENES.values():
                viejas.append(f"{idioma}/huellas.json: {origen} no es un texto legal espanol ({sorted(sl.ORIGENES.values())})")
            elif not sl.ruta_traduccion(idioma, origen, base).exists():
                viejas.append(f"{idioma}/huellas.json: hay huella de {origen} pero no existe su traduccion "
                              f"{sl.ruta_traduccion(idioma, origen, base).name}")
            elif huella != huella_de_origen(origen, base):
                viejas.append(f"{idioma}/{sl.ruta_traduccion(idioma, origen, base).name}: vieja, salio de un {origen} "
                              "que ya cambio")
    return viejas


def traducciones_en_curso(base=sl.BASE):
    """Las traducciones que existen sin huella: aun no se publican (la pagina de ese idioma sigue en espanol)."""
    en_curso = []
    for idioma in sl.IDIOMAS_TRADUCCION:
        guardadas = sl.huellas_guardadas(idioma, base)
        for origen in sorted(sl.ORIGENES.values()):
            ruta = sl.ruta_traduccion(idioma, origen, base)
            if ruta.exists() and origen not in guardadas:
                en_curso.append(f"{idioma}/{ruta.name}")
    return en_curso


def escribir_huellas(idioma, base=sl.BASE):
    """Escribe la huella del espanol de hoy para cada traduccion que existe en `idioma`. Falla ruidoso si no hay
    ninguna o si el idioma no es de la marca."""
    if idioma not in sl.IDIOMAS_TRADUCCION:
        sys.exit(f"idioma desconocido: {idioma!r}; los de las traducciones son {', '.join(sl.IDIOMAS_TRADUCCION)}")
    huellas = {origen: huella_de_origen(origen, base) for origen in sorted(sl.ORIGENES.values())
               if sl.ruta_traduccion(idioma, origen, base).exists()}
    if not huellas:
        sys.exit(f"no hay ninguna traduccion en docs/legal/{idioma}/ (se esperan {', '.join(sorted(sl.ORIGENES.values()))})")
    sl.ruta_huellas(idioma, base).write_text(json.dumps(huellas, indent=2, sort_keys=True) + "\n", encoding="utf-8",
                                             newline="\n")
    return huellas


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--comprobar":
        viejas, en_curso = traducciones_viejas(), traducciones_en_curso()
        for v in viejas:
            print("VIEJA   ", v)
        for c in en_curso:
            print("EN CURSO", c, "(sin huella: no se publica)")
        if not viejas and not en_curso:
            print("todas las traducciones legales estan al dia con el espanol")
        sys.exit(1 if viejas else 0)
    if len(sys.argv) == 2 and not sys.argv[1].startswith("-"):
        escritas = escribir_huellas(sys.argv[1])
        print(f"huellas de docs/legal/{sys.argv[1]}/ escritas para: {', '.join(escritas)}")
        print("ahora publica con: python scripts/sync_legal_web.py")
        sys.exit(0)
    sys.exit("uso: python scripts/legal_huellas.py <idioma> | --comprobar")
