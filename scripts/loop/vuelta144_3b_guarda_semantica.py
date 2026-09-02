"""Vuelta 144, TAREA 3.b: guarda SEMANTICA de la adicion a `aristas_nuevas`.

Hermana de scripts/loop/vuelta143_3a_guarda_semantica.py y de
scripts/loop/vuelta144_2a_guarda_semantica.py. Aqui el campo que crece es
`aristas_nuevas` y crece EN NUMERO DE ENTRADAS, asi que la vara de adicion pura
se mide sobre la LISTA, como en la de la 143.

QUE COMPRUEBA:
  - el censo de fichas no se mueve,
  - el juego de ids no se mueve,
  - cambia UNA sola ficha,
  - cambia UN solo campo, y es `aristas_nuevas`,
  - `aristas_nuevas` crece de N a N+1 entradas,
  - las N viejas son PREFIJO IDENTICO de las N+1 nuevas (adicion pura),
  - y NINGUNA entrada vieja trae flecha, que es lo que la adicion viene a
    remediar: si alguna la trajera, la adicion no haria falta.

El numstat de este JSONL da 1/1 y eso es lo correcto (caida 4.7 del acta 142).

Uso: python scripts/loop/vuelta144_3b_guarda_semantica.py [ref]
"""
import json
import subprocess
import sys

RUTA = "docs/plan/OPERACIONES.jsonl"
CAMPO = "aristas_nuevas"
REF = sys.argv[1] if len(sys.argv) > 1 else "HEAD"


def carga(texto):
    fichas, n = {}, 0
    for linea in texto.splitlines():
        linea = linea.strip()
        if not linea:
            continue
        obj = json.loads(linea)
        n += 1
        fichas[obj["id_op"]] = obj
    return fichas, n


def main():
    antes_txt = subprocess.run(["git", "show", "%s:%s" % (REF, RUTA)],
                               capture_output=True, text=True, encoding="utf-8",
                               check=True).stdout
    despues_txt = open(RUTA, encoding="utf-8").read()
    antes, n_antes = carga(antes_txt)
    despues, n_despues = carga(despues_txt)

    fallos = []
    print("REFERENCIA: %s" % subprocess.run(["git", "rev-parse", REF], capture_output=True,
                                            text=True, encoding="utf-8").stdout.strip())
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
        if campos != [CAMPO]:
            fallos.append("en %s cambian campos %s, se esperaba solo %s" % (k, campos, CAMPO))
            continue
        va = antes[k][CAMPO]
        vb = despues[k][CAMPO]
        print("  %s %s: %d entrada(s) -> %d entrada(s)" % (k, CAMPO, len(va), len(vb)))
        if len(vb) != len(va) + 1:
            fallos.append("en %s %s pasa de %d a %d, se esperaba +1" % (k, CAMPO, len(va), len(vb)))
        prefijo = vb[:len(va)] == va
        print("  %s PREFIJO IDENTICO (adicion pura): %s" % (k, prefijo))
        if not prefijo:
            fallos.append("en %s las entradas viejas NO son prefijo identico de las nuevas" % k)
        con_flecha_antes = [i for i, x in enumerate(va) if "->" in x]
        print("  %s ENTRADAS VIEJAS CON FLECHA: %s (tiene que ser vacia: si ya hubiera una, "
              "la adicion no haria falta)" % (k, con_flecha_antes))
        if con_flecha_antes:
            fallos.append("en %s ya habia %d entrada(s) con flecha antes de la adicion"
                          % (k, len(con_flecha_antes)))
        for i, entrada in enumerate(vb[len(va):]):
            print("  %s ENTRADA NUEVA %d (%d caracteres): %s"
                  % (k, len(va) + i + 1, len(entrada), entrada[:160]))

    print("")
    if fallos:
        print("ROJO: %d fallo(s)" % len(fallos))
        for f in fallos:
            print("  - %s" % f)
        return 1
    print("VERDE: adicion pura de UNA entrada de %s en UNA sola ficha, censo intacto" % CAMPO)
    return 0


if __name__ == "__main__":
    sys.exit(main())
