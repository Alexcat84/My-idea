"""Vuelta 144, TAREA 2.a: guarda SEMANTICA de la adicion a la verificacion 5.

Es la hermana de scripts/loop/vuelta143_3a_guarda_semantica.py, con la unica
diferencia que el caso pide: aqui la `verificacion` NO crece en numero de
lineas (la formula canonica se anade DENTRO de la linea 5, que es la que
declara la excepcion), asi que la vara de adicion pura se mide sobre EL TEXTO
DE LA LINEA y no sobre la lista.

QUE COMPRUEBA:
  - el censo de fichas no se mueve,
  - el juego de ids no se mueve,
  - cambia UNA sola ficha,
  - cambia UN solo campo, y es `verificacion`,
  - `verificacion` tiene el MISMO numero de lineas antes y despues,
  - cambia UNA sola linea de `verificacion`,
  - y el texto viejo de esa linea es PREFIJO IDENTICO del nuevo (adicion pura).

El numstat de este JSONL da 1/1 y eso es lo correcto (caida 4.7 del acta 142):
una linea por ficha, cualquier adicion la reescribe.

--- DOS REFS, NO UNO (VUELTA 145, TAREA 2.b; acta 144, caida 4.9) ---

CORRECCION DECLARADA. EL TEXTO VIEJO DE LA LINEA DE USO DECIA, VERBATIM:
"Uso: python scripts/loop/vuelta144_2a_guarda_semantica.py [ref]". No se
borra (EJECUTOR.md 8).

EL DEFECTO, MEDIDO. Esta guarda comparaba EL ARBOL DE TRABAJO contra UN SOLO
ref (`REF = sys.argv[1] ... else "HEAD"`), asi que media un cambio que solo
existe mientras ese cambio esta SIN COMMITEAR. En cuanto la TAREA 3.b de la
vuelta 144 toco la misma ficha, esta quedo en ROJO PERMANENTE, y su gemela de
la 3.b siguio verde solo por haber sido la ultima en tocarla. Medido en la
vuelta 145 sobre el arbol limpio de la apertura: LAS DOS salen ROJO con el
mismo fallo, "cambian 0 fichas, se esperaba 1", porque con el arbol limpio
WORK es HEAD y no cambia nada. (El acta 144 da la de la 3.b por verde; mi
medicion de hoy dice que sobre arbol limpio las dos estan rojas, y lo declaro
en vez de copiarlo.)

EL ARREGLO. Se aceptan DOS refs, ANTES y DESPUES, y cualquiera de los dos
puede ser el literal `WORK` para decir "el arbol de trabajo". Sin argumentos
se conserva el comportamiento viejo (HEAD contra WORK) para no romper a quien
la invoque asi.

INVOCACION CANONICA DE ESTA GUARDA, que es la que reproduce el cambio que
nacio para medir:
  python scripts/loop/vuelta144_2a_guarda_semantica.py c5a389dd^ c5a389dd

Uso: python scripts/loop/vuelta144_2a_guarda_semantica.py [ref_antes] [ref_despues]
     (un solo argumento: ese ref contra WORK. Ninguno: HEAD contra WORK.)
"""
import json
import subprocess
import sys

RUTA = "docs/plan/OPERACIONES.jsonl"
# DOS REFS (vuelta 145, TAREA 2.b): ANTES y DESPUES, cualquiera de los dos
# puede ser el literal WORK. Sin argumentos, el comportamiento viejo.
REF = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
REF_DESPUES = sys.argv[2] if len(sys.argv) > 2 else "WORK"


def texto_de(ref):
    """El JSONL en `ref`, o el del arbol de trabajo si `ref` es el literal
    WORK (vuelta 145, TAREA 2.b). Un solo camino para los dos lados, para que
    ANTES y DESPUES no se lean con maquinas distintas."""
    if ref == "WORK":
        return open(RUTA, encoding="utf-8").read()
    return subprocess.run(["git", "show", "%s:%s" % (ref, RUTA)],
                          capture_output=True, text=True, encoding="utf-8",
                          check=True).stdout


def rotulo_de(ref):
    """El hash de `ref` leido de git, o el literal WORK. Nunca tecleado."""
    if ref == "WORK":
        return "WORK (arbol de trabajo)"
    return subprocess.run(["git", "rev-parse", ref], capture_output=True, text=True,
                          encoding="utf-8").stdout.strip()


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
    antes_txt = texto_de(REF)
    despues_txt = texto_de(REF_DESPUES)
    antes, n_antes = carga(antes_txt)
    despues, n_despues = carga(despues_txt)

    fallos = []
    print("REFERENCIA ANTES  : %s" % rotulo_de(REF))
    print("REFERENCIA DESPUES: %s" % rotulo_de(REF_DESPUES))
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
        if len(vb) != len(va):
            fallos.append("en %s verificacion pasa de %d a %d lineas, se esperaba el MISMO "
                          "numero" % (k, len(va), len(vb)))
            continue
        movidas = [i for i in range(len(va)) if va[i] != vb[i]]
        print("  %s LINEAS DE verificacion QUE CAMBIAN: %s" % (k, movidas))
        if len(movidas) != 1:
            fallos.append("en %s cambian %d lineas de verificacion, se esperaba 1"
                          % (k, len(movidas)))
            continue
        i = movidas[0]
        prefijo = vb[i].startswith(va[i])
        print("  %s linea %d: %d caracteres -> %d caracteres (+%d)"
              % (k, i, len(va[i]), len(vb[i]), len(vb[i]) - len(va[i])))
        print("  %s PREFIJO IDENTICO (adicion pura dentro de la linea): %s" % (k, prefijo))
        if not prefijo:
            fallos.append("en %s el texto viejo de la linea %d NO es prefijo identico del "
                          "nuevo" % (k, i))
        print("  %s LO ANADIDO (%d caracteres): %s"
              % (k, len(vb[i]) - len(va[i]), vb[i][len(va[i]):] if prefijo else "(no aplica)"))

    print("")
    if fallos:
        print("ROJO: %d fallo(s)" % len(fallos))
        for f in fallos:
            print("  - %s" % f)
        return 1
    print("VERDE: adicion pura DENTRO de UNA linea de verificacion en UNA sola ficha, "
          "censo intacto y numero de lineas intacto")
    return 0


if __name__ == "__main__":
    sys.exit(main())
