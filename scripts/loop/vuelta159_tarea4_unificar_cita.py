# -*- coding: utf-8 -*-
"""vuelta159_tarea4_unificar_cita.py . TAREA 4 DE LA VUELTA 159.

EL CAMPO `cita` DEL REGISTRO SE UNIFICA EN UNA SOLA FORMA, LA QUE NO TAPA
(adjudicacion 6.6 del acta 158):

    LD-OPC05-NNN, clase <VIGENTE> [ANTES <ANTERIOR>, RECLASIFICADA EN LA VUELTA
    <N>: ver la razon]

EL HECHO QUE LO OBLIGA, MEDIDO POR EL AUDITOR (acta 158, seccion 5.1): en la
vuelta 157 cambiaron 62 campos `cita` POR SOBREESCRITURA (`clase C` paso a
`clase D` sin dejar rastro), mientras que las tres de la vuelta 156 usan otra
forma (`clase C  [RECLASIFICADA A D EN LA VUELTA 156: ver la razon]`) que ademas
hoy lee literalmente "clase C" en una fila que es D. Dos formas para el mismo
hecho en el mismo fichero.

DE DONDE SALE CADA DATO, Y NINGUNO SE TECLEA:

  (a) LA HISTORIA DE CLASES SE RECONSTRUYE DE GIT, no de la prosa de las
      razones. Las razones de la vuelta 156 no usan la misma formula que las de
      la 157 y la 159 ("LA CLASE PASA DE X A Y"), asi que una vara lexica sobre
      la razon seria ciega justo en las tres filas que la 6.6 nombra. Se leen en
      cambio LOS DOCE COMMITS que tocan
      `docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl` (`git log --format=%H`), se
      parsea el blob de cada uno (`git show <commit>:<ruta>`) y se anota la
      clase de cada `LD` commit a commit. Cada cambio queda con el commit que lo
      hizo, y el NUMERO DE VUELTA sale del asunto de ese commit
      (`VUELTA (\\d+)`), no de la memoria. Es la regla de la casa: LA IDENTIDAD
      SE LEE DE GIT.
  (b) `ANTES` es la clase INMEDIATAMENTE ANTERIOR a la vigente, no la primera de
      la historia, porque eso es lo que la palabra dice. Para una fila que
      cambio dos veces (`LD-OPC05-005`, C a D en la 157 y D a C en la 159) la
      cita queda `clase C [ANTES D, RECLASIFICADA EN LA VUELTA 159: ...]`, y la
      cadena entera sigue viva en la celda tachada del `.md` y en la razon.
  (c) LA CADENA DEL `.md` SE USA COMO CONTRASTE INDEPENDIENTE, no como fuente:
      la celda acumula tachados (`~~C~~ ~~D~~ C`) y su ultimo token tiene que
      coincidir con la clase vigente de git. Si no coincide, ROJO.

POR ADICION Y CON CORRECCION DECLARADA: el campo `cita` es corto y no admite
apendices sin volverse ilegible, asi que la ADICION va en la `razon`, donde se
escribe QUE DECIA la cita antes y QUE DICE ahora. Ninguna linea vieja de la
razon se toca, y el assert de prefijo lo comprueba sobre las 154.

LOS ASSERTS QUE EXIGE LA 6.6: NINGUNA CLASE SE MUEVE al hacerlo, y el CONTEO DE
PARES del registro sale IDENTICO antes y despues.

ES IDEMPOTENTE por marca literal.

USO:  python scripts/loop/vuelta159_tarea4_unificar_cita.py
"""
import io
import json
import os
import re
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REL = "docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl"
REGISTRO = os.path.join(RAIZ, REL)
LD_MD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")

MARCA = "UNIFICACION DEL CAMPO cita (VUELTA 159, ADJUDICACION 6.6 DEL ACTA 158)"

# LA 6.6 HABLA DE LAS LECTURAS DIRIGIDAS Y SOLO DE ELLAS, Y EL ALCANCE SE
# DECLARA EN VEZ DE DARSE POR SUPUESTO. La via CRIBADO usa otro formato de cita
# ("puesto 1154, dominio quality, clase D") y los puentes de la P.10 usan un
# tercero; ninguno de los dos sufrio la sobreescritura que la 5.1 del acta 158
# midio, porque ninguna de sus clases se ha movido nunca. Se dejan INTACTOS y se
# cuenta cuantos son. La primera corrida de esta tarea reviento aqui, en un
# int() sobre "puesto 1154", y el arreglo es este filtro, declarado.
ES_LD = re.compile(r"^LD-OPC05-\d{3}$")


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def entradas(texto=None):
    t = texto if texto is not None else leer(REGISTRO)
    return [json.loads(x) for x in t.splitlines() if x.strip()]


def ld_de(e):
    return e["cita"].split(",")[0].strip()


def git(*args):
    r = subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", "replace")


def historia_de_clases():
    """Devuelve {ld: [(vuelta, commit_corto, clase_antes, clase_nueva), ...]} y
    el mapa {ld: clase_vigente_en_HEAD}, todo leido de git."""
    lineas = git("log", "--reverse", "--format=%H\t%s", "--", REL).strip().splitlines()
    commits = []
    for l in lineas:
        h, _, s = l.partition("\t")
        m = re.search(r"VUELTA (\d+)", s)
        commits.append((h.strip(), s, int(m.group(1)) if m else None))
    print("   CIFRA commits que tocan el registro (git log): %d" % len(commits))
    cambios = {}
    previo = {}
    vigente = {}
    for h, s, vuelta in commits:
        try:
            E = entradas(git("show", "%s:%s" % (h, REL)))
        except ValueError:
            continue
        actual = {ld_de(e): e["clase"] for e in E}
        for ld, cl in actual.items():
            if ld in previo and previo[ld] != cl:
                cambios.setdefault(ld, []).append((vuelta, h[:8], previo[ld], cl))
        previo = actual
        vigente = actual
    return cambios, vigente, commits


def cadena_md(texto, ld):
    """La celda de clase del `.md`, como lista de tokens sin tachar."""
    num = int(ld.split("-")[-1])
    m = re.search(
        r"\| %d \| REGISTRO DE CITAS `OP-C-05` \| [a-z0-9_]+ <-> [a-z0-9_]+ \| "
        r"([^|]*)\| %s \|" % (num, re.escape(ld)), texto)
    if not m:
        return None
    return [t.strip("~") for t in m.group(1).split()]


def main():
    print("=" * 78)
    print("VUELTA 159, TAREA 4: EL CAMPO cita UNIFICADO EN UNA SOLA FORMA")
    print("=" * 78)
    print("")

    print("A) LA HISTORIA DE CLASES, RECONSTRUIDA DE GIT Y NO DE LA PROSA")
    cambios, vigente_git, commits = historia_de_clases()
    for h, s, v in commits:
        print("      %s  vuelta %-4s %s" % (h[:8], v if v else "?", s[:82]))
    print("   CIFRA filas con AL MENOS UN cambio de clase en la historia: %d"
          % len(cambios))
    por_vuelta = {}
    for ld, ch in cambios.items():
        for v, _, _, _ in ch:
            por_vuelta[v] = por_vuelta.get(v, 0) + 1
    print("   CIFRA cambios de clase por vuelta: %s"
          % json.dumps(por_vuelta, sort_keys=True))
    print("")

    E = entradas()
    antes_razon = {ld_de(e): e["razon"] for e in E}
    antes_clase = {ld_de(e): e["clase"] for e in E}
    antes_cita = {ld_de(e): e["cita"] for e in E}
    texto_md = leer(LD_MD)

    print("B) EL CONTRASTE INDEPENDIENTE CONTRA LA CELDA TACHADA DEL .md")
    desacuerdos = []
    con_fila = 0
    fuera = [ld_de(e) for e in E if not ES_LD.match(ld_de(e))]
    print("   CIFRA filas que NO son lecturas dirigidas y quedan intactas: %d"
          % len(fuera))
    for e in E:
        ld = ld_de(e)
        if not ES_LD.match(ld):
            continue
        cad = cadena_md(texto_md, ld)
        if cad is None:
            continue
        con_fila += 1
        if cad[-1] != e["clase"]:
            desacuerdos.append((ld, cad, e["clase"]))
    print("   CIFRA filas del registro con fila en el .md: %d" % con_fila)
    print("   CIFRA filas donde el ultimo token del .md NO es la clase vigente: %d"
          % len(desacuerdos))
    for d in desacuerdos:
        print("      ROJO %s: cadena %s, clase %s" % d)
    if desacuerdos:
        print("SE PARA: el .md y el registro no cuentan la misma historia.")
        print("FIN")
        return 1
    print("   LAS DOS SEDES CUENTAN LA MISMA HISTORIA.")
    print("")

    print("C) LAS CITAS, REESCRITAS A LA FORMA UNICA")
    tocadas, ya, sin_cambio = 0, 0, 0
    for e in E:
        ld = ld_de(e)
        if not ES_LD.match(ld):
            continue
        vig = e["clase"]
        ch = cambios.get(ld)
        if ch:
            vuelta, _, ant, _ = ch[-1]
            nueva = ("%s, clase %s [ANTES %s, RECLASIFICADA EN LA VUELTA %s: "
                     "ver la razon]" % (ld, vig, ant, vuelta))
        else:
            nueva = "%s, clase %s" % (ld, vig)
        if e["cita"] == nueva:
            sin_cambio += 1
            continue
        if MARCA in e["razon"]:
            ya += 1
            continue
        e["razon"] = e["razon"] + (
            "  [%s, ANADIDA SIN BORRAR NADA DE LO ANTERIOR: el campo `cita` de "
            "esta fila decia %r y desde hoy dice %r. La clase NO se mueve: lo "
            "que cambia es que la cita deja de tapar su propia correccion. La "
            "historia de clases de la que sale este texto se reconstruyo de los "
            "commits del registro, no de esta prosa, y esta pegada en "
            "docs/loop/SALIDA_V159_T4_CITAS.txt.]" % (MARCA, e["cita"], nueva))
        e["cita"] = nueva
        tocadas += 1
        if tocadas <= 6 or ch:
            print("   %-16s [%s] -> [%s]" % (ld, antes_cita[ld], nueva))
    print("")
    print("   CIFRA citas reescritas en esta corrida: %d" % tocadas)
    print("   CIFRA citas que ya estaban en la forma unica: %d" % sin_cambio)
    print("   CIFRA citas que ya llevaban la marca de esta tarea: %d" % ya)
    print("")

    with io.open(REGISTRO, "w", encoding="utf-8", newline="\n") as fh:
        for e in E:
            fh.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")

    print("D) LOS ASSERTS QUE LA 6.6 EXIGE, MEDIDOS Y NO PROMETIDOS")
    D = entradas()
    assert len(D) == len(E) == 154, "el numero de lineas del registro se movio"
    print("   D.1 LINEAS: %d antes y %d despues" % (len(E), len(D)))

    movidas = [ld_de(d) for d in D if d["clase"] != antes_clase[ld_de(d)]]
    print("   D.2 CIFRA clases movidas por esta tarea: %d" % len(movidas))
    assert not movidas, "NINGUNA clase se mueve al unificar la cita"
    print("       NINGUNA. La cita cambia, la clase no.")

    pares_antes = {tuple(sorted(e["par"])) for e in E}
    pares_desp = {tuple(sorted(d["par"])) for d in D}
    print("   D.3 CIFRA pares antes: %d, CIFRA pares despues: %d"
          % (len(pares_antes), len(pares_desp)))
    assert pares_antes == pares_desp, "el conteo de pares del registro se movio"
    print("       IDENTICO.")

    rotos = [ld_de(d) for d in D if not d["razon"].startswith(antes_razon[ld_de(d)])]
    print("   D.4 CIFRA razones cuyo texto viejo YA NO ES PREFIJO: %d" % len(rotos))
    assert not rotos, "PREFIJO ROTO en: %s" % ", ".join(rotos)
    print("       PREFIJO INTACTO en las %d." % len(D))

    formas = {}
    for d in D:
        if not ES_LD.match(ld_de(d)):
            continue
        formas["con rastro" if "[ANTES " in d["cita"] else "sin rastro"] = \
            formas.get("con rastro" if "[ANTES " in d["cita"] else "sin rastro", 0) + 1
    print("   D.5 CIFRA citas por forma: %s" % json.dumps(formas, sort_keys=True))
    viejas = [ld_de(d) for d in D if "RECLASIFICADA A " in d["cita"]]
    print("   D.6 CIFRA citas que siguen en la forma vieja de la vuelta 156: %d"
          % len(viejas))
    assert not viejas, "queda una cita en la forma vieja: %s" % ", ".join(viejas)
    print("       NINGUNA. UNA SOLA FORMA.")
    print("")

    r = git("diff", "--numstat", "--", "docs/plan/")
    print("   D.7 numstat de docs/plan/:")
    for l in r.strip().splitlines():
        print("       %s" % l)
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
