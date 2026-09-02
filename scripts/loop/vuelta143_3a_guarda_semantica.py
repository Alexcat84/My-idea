"""Vuelta 143, TAREA 3.a: guarda SEMANTICA del commit de la 3.a de la 142.

El numstat de un JSONL de una linea por ficha no puede dar CERO BORRADAS
(caida 4.7 del acta 142): cualquier adicion dentro de una ficha reescribe su
linea y da 1/1. La guarda buena es semantica y es esta:

  - el censo de fichas no se mueve,
  - cambia UNA sola ficha,
  - cambia UN solo campo, y es `verificacion`,
  - `verificacion` crece de N a N+1 lineas,
  - las N viejas son PREFIJO IDENTICO de las N+1 nuevas (adicion pura).

Corre contra el arbol de trabajo comparado con una referencia de git.
Uso: python scripts/loop/vuelta143_3a_guarda_semantica.py [ref]
"""
import json
import subprocess
import sys

RUTA = "docs/plan/OPERACIONES.jsonl"
REF = sys.argv[1] if len(sys.argv) > 1 else "HEAD"


def carga(texto):
    fichas = {}
    n = 0
    for linea in texto.splitlines():
        linea = linea.strip()
        if not linea:
            continue
        obj = json.loads(linea)
        n += 1
        fichas[obj["id_op"]] = obj
    return fichas, n


def main():
    antes_txt = subprocess.run(
        ["git", "show", "%s:%s" % (REF, RUTA)],
        capture_output=True, text=True, encoding="utf-8", check=True).stdout
    despues_txt = open(RUTA, encoding="utf-8").read()
    antes, n_antes = carga(antes_txt)
    despues, n_despues = carga(despues_txt)

    fallos = []
    print("REFERENCIA: %s" % subprocess.run(
        ["git", "rev-parse", REF], capture_output=True, text=True,
        encoding="utf-8").stdout.strip())
    print("FICHAS ANTES: %d | FICHAS DESPUES: %d" % (n_antes, n_despues))
    if n_antes != n_despues:
        fallos.append("el censo de fichas se movio")
    solo_antes = sorted(set(antes) - set(despues))
    solo_despues = sorted(set(despues) - set(antes))
    print("IDS SOLO ANTES: %s | IDS SOLO DESPUES: %s" % (solo_antes, solo_despues))
    if solo_antes or solo_despues:
        fallos.append("el juego de ids se movio")

    cambian = sorted(k for k in antes if k in despues and antes[k] != despues[k])
    print("FICHAS QUE CAMBIAN: %s" % cambian)
    if len(cambian) != 1:
        fallos.append("cambian %d fichas, se esperaba 1" % len(cambian))

    for k in cambian:
        campos = sorted(c for c in set(antes[k]) | set(despues[k])
                        if antes[k].get(c) != despues[k].get(c))
        print("  %s CAMPOS QUE CAMBIAN: %s" % (k, campos))
        if campos != ["verificacion"]:
            fallos.append("en %s cambian campos %s, se esperaba solo verificacion" % (k, campos))
            continue
        va = antes[k]["verificacion"]
        vb = despues[k]["verificacion"]
        print("  %s verificacion: %d lineas -> %d lineas" % (k, len(va), len(vb)))
        if len(vb) != len(va) + 1:
            fallos.append("en %s verificacion pasa de %d a %d, se esperaba +1" % (k, len(va), len(vb)))
        prefijo = vb[:len(va)] == va
        print("  %s PREFIJO IDENTICO (adicion pura): %s" % (k, prefijo))
        if not prefijo:
            fallos.append("en %s las lineas viejas NO son prefijo identico de las nuevas" % k)
        for i, linea in enumerate(vb[len(va):]):
            print("  %s LINEA NUEVA %d (%d caracteres): %s" % (k, len(va) + i + 1, len(linea), linea[:120]))

    print("")
    if fallos:
        print("ROJO: %d fallo(s)" % len(fallos))
        for f in fallos:
            print("  - %s" % f)
        return 1
    print("VERDE: adicion pura de UNA linea de verificacion en UNA sola ficha, censo intacto")
    return 0


if __name__ == "__main__":
    sys.exit(main())
