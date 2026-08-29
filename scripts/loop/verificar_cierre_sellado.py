# -*- coding: utf-8 -*-
r"""verificar_cierre_sellado.py . LA GUARDA DEL SELLO DE CIERRE (TAREA 1.h de
la vuelta 129, acta de la vuelta 128, seccion "DOS GUARDAS QUE NO ALCANZAN,
Y SON DE LA CASA, NO TUYAS", ramal (b)).

Nombre estable, SIN numero de vuelta, gemela de
scripts/loop/verificar_apertura_sellada.py y con su mismo estilo: se invoca
con --vuelta N y no se clona cada vuelta; todo se lee de `git`, nada se
teclea ni se inventa.

POR QUE NACE. En la vuelta 128 el sello de cierre original
(`SALIDA_V128_HEAD_CIERRE.txt`) apuntaba a `9c222986`, un commit que el
propio rebase de esa vuelta saco de la rama `pasada-unica`. El ejecutor lo
detecto y regenero por su cuenta sobre el HEAD correcto, pero NINGUNA guarda
lo obligaba a hacerlo: nada impedia que un sello de cierre quedara apuntando
a un commit ausente de la rama, y la bateria de comprobaciones habria pasado
VERDE entera igual, porque ninguna de ellas mira el sello de cierre. Esta
guarda cierra ese hueco: hace por el cierre lo que
`verificar_apertura_sellada.py` ya hacia por la apertura, adaptado a lo que
un cierre tiene que probar (que el commit sellado exista, este en la rama,
pertenezca a esta vuelta y sea distinto de la apertura), no a donde nacio el
fichero.

QUE COMPRUEBA. Lee `docs/loop/SALIDA_V<vuelta>_HEAD_CIERRE.txt` del arbol de
trabajo. Cae en ROJO EXIT 1 si:
  - el fichero no existe;
  - el fichero tiene mas de una linea (o cero lineas con contenido);
  - la linea no es un hash de 40 caracteres hexadecimales;
  - el hash NO es un commit valido del repositorio (`git cat-file -t`
    distinto de "commit");
  - el commit NO esta en la rama actual (`git merge-base --is-ancestor
    <hash> HEAD` falla);
  - el commit sellado NO es descendiente del commit del acta de la vuelta
    anterior (el mismo commit de referencia que usa
    `verificar_apertura_sellada.py`, "ACTA DE LA VUELTA <vuelta-1> DEL
    AUDITOR" o "ACTA DEL AUDITOR, VUELTA <vuelta-1>"): un cierre que no
    desciende del acta anterior no pertenece a esta vuelta;
  - el hash sellado es IGUAL al de `SALIDA_V<vuelta>_HEAD_APERTURA.txt`: un
    cierre que no avanzo sobre la apertura no es un cierre.
VERDE EXIT 0 si pasa las seis.

Nunca inventa un hash ni asume una fecha: todo se lee de `git` sobre la rama
actual (`git rev-parse --abbrev-ref HEAD`), igual que la guarda de apertura.

USO:
  python scripts/loop/verificar_cierre_sellado.py --vuelta 129

DOS CASOS POSITIVOS POR MUTACION (en memoria, sin tocar ningun fichero real
del repo, cada uno corrido y pegado en su propia salida):
  (a) un hash de commit que EXISTE pero NO esta en la rama `pasada-unica`:
      se usa `74d55f9e` (commit real de la rama `main`, "Release a main: el
      cierre del frente del motor"; `git merge-base --is-ancestor 74d55f9e
      pasada-unica` da NO, exit 1, comprobado antes de escribir esta guarda);
      tiene que salir ROJO nombrando el motivo "no esta en la rama".
  (b) el hash de la apertura de la vuelta puesto como cierre: tiene que salir
      ROJO por la ultima condicion ("igual a la apertura").

CORRECCION DECLARADA (29 ago 2026, vuelta 130, TAREA 2.d, caida de
expediente de la vuelta 129, acta 129, 4.3). EL CASO (a) NO SE CORRIO CON
`74d55f9e`: el registro pegado a su lado
(`docs/loop/SALIDA_V129_1H_CIERRE_SELLADO_MUTACION.txt`) usa
`ce51aa27a4564559491890f84995884f5ae2e1f9`, un commit SINTETICO de un repo
temporal construido con `git init`, con una rama lateral divergente del
commit del acta. Ese hash cambia en cada corrida por diseno (comprobado en
la vuelta 130: la misma prueba, corrida hoy, produjo otro commit lateral
distinto, `8f5840bc...`). `74d55f9e` SI es un commit real de la rama `main`,
ajeno a `pasada-unica` (comprobado hoy: `git cat-file -t 74d55f9e` da
`commit`, `git merge-base --is-ancestor 74d55f9e pasada-unica` da exit 1),
pero NO SE USO en la corrida real: la cabecera describia una prueba que no
se corrio asi. Este parrafo lo declara sin reescribir lo de arriba; el
codigo de la guarda no se toca.
"""
import argparse
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")

RE_HASH40 = re.compile(r"^[0-9a-f]{40}$")


def _git(args, fallos, contexto):
    try:
        r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True, text=True, check=True)
        return r.stdout
    except Exception as e:
        fallos.append("no se pudo correr git %s (%s): %s" % (" ".join(args), contexto, e))
        return None


def rama_actual(fallos):
    out = _git(["rev-parse", "--abbrev-ref", "HEAD"], fallos, "rama actual")
    return out.strip() if out is not None else None


def commit_acta(vuelta, rama, fallos):
    """Mismo criterio que verificar_apertura_sellada.py: el commit cuyo
    mensaje empieza por 'ACTA DE LA VUELTA <vuelta-1> DEL AUDITOR' o por
    'ACTA DEL AUDITOR, VUELTA <vuelta-1>'."""
    out = _git(["log", rama, "--pretty=format:%H\x01%s"], fallos, "git log de la rama")
    if out is None:
        return None
    patrones = [
        re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR\b" % (vuelta - 1)),
        re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA %d\b" % (vuelta - 1)),
    ]
    hallados = []
    for linea in out.splitlines():
        if "\x01" not in linea:
            continue
        h, s = linea.split("\x01", 1)
        if any(p.match(s) for p in patrones):
            hallados.append(h)
    if not hallados:
        fallos.append("git log de la rama %s no trae ningun commit 'ACTA DE LA VUELTA %d "
                      "DEL AUDITOR': no se puede fijar el commit de referencia" % (rama, vuelta - 1))
        return None
    if len(hallados) > 1:
        fallos.append("git log de la rama %s trae %d commits 'ACTA DE LA VUELTA %d DEL "
                      "AUDITOR' (%s): ambiguo" % (rama, len(hallados), vuelta - 1,
                                                    ", ".join(h[:8] for h in hallados)))
        return None
    return hallados[0]


def leer_sello(nombre, fallos):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        fallos.append("%s no existe en el arbol de trabajo" % nombre)
        return None
    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()
    lineas = [l for l in contenido.splitlines() if l.strip() != ""]
    if len(lineas) != 1:
        fallos.append("%s tiene %d linea(s) con contenido, se esperaba exactamente 1" %
                      (nombre, len(lineas)))
        return None
    hash_ = lineas[0].strip()
    if not RE_HASH40.match(hash_):
        fallos.append("%s: '%s' no es un hash de 40 caracteres hexadecimales" % (nombre, hash_))
        return None
    return hash_


def es_commit(hash_, fallos):
    try:
        r = subprocess.run(["git", "cat-file", "-t", hash_], cwd=RAIZ,
                           capture_output=True, text=True)
    except Exception as e:
        fallos.append("no se pudo correr git cat-file -t %s: %s" % (hash_, e))
        return False
    tipo = r.stdout.strip()
    if r.returncode != 0 or tipo != "commit":
        fallos.append("%s no es un commit valido del repositorio (git cat-file -t da '%s', "
                      "exit %d)" % (hash_, tipo or "(vacio)", r.returncode))
        return False
    return True


def esta_en_rama(hash_, rama, fallos, etiqueta="el hash sellado"):
    r = subprocess.run(["git", "merge-base", "--is-ancestor", hash_, rama], cwd=RAIZ,
                       capture_output=True, text=True)
    if r.returncode != 0:
        fallos.append("%s (%s) no esta en la rama %s (git merge-base --is-ancestor da exit %d)" %
                      (etiqueta, hash_, rama, r.returncode))
        return False
    return True


def es_descendiente_del_acta(hash_, acta, fallos):
    r = subprocess.run(["git", "merge-base", "--is-ancestor", acta, hash_], cwd=RAIZ,
                       capture_output=True, text=True)
    if r.returncode != 0:
        fallos.append("el commit sellado %s no es descendiente del commit del acta anterior %s: "
                      "no pertenece a esta vuelta" % (hash_, acta[:8]))
        return False
    return True


def verificar(vuelta):
    fallos = []
    rama = rama_actual(fallos)
    if rama is None:
        return fallos, None

    acta = commit_acta(vuelta, rama, fallos)
    nombre_cierre = "SALIDA_V%d_HEAD_CIERRE.txt" % vuelta
    nombre_apertura = "SALIDA_V%d_HEAD_APERTURA.txt" % vuelta

    hash_cierre = leer_sello(nombre_cierre, fallos)
    if hash_cierre is None:
        return fallos, None

    if not es_commit(hash_cierre, fallos):
        return fallos, hash_cierre

    if not esta_en_rama(hash_cierre, rama, fallos, etiqueta="el commit de cierre"):
        return fallos, hash_cierre

    if acta is not None:
        es_descendiente_del_acta(hash_cierre, acta, fallos)

    hash_apertura = leer_sello(nombre_apertura, fallos)
    if hash_apertura is not None and hash_apertura == hash_cierre:
        fallos.append("%s es IGUAL a %s (%s): un cierre que no avanzo sobre la apertura no es "
                      "un cierre" % (nombre_cierre, nombre_apertura, hash_cierre))

    return fallos, hash_cierre


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, required=True)
    a = ap.parse_args()

    fallos, hash_cierre = verificar(a.vuelta)
    if fallos:
        print("ROJO, cierre de la vuelta %d NO sellado (%d cosa(s) no cuadran):" %
              (a.vuelta, len(fallos)))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("VERDE: SALIDA_V%d_HEAD_CIERRE.txt sella %s, un commit valido, en la rama, "
          "descendiente del acta anterior y distinto de la apertura." %
          (a.vuelta, hash_cierre))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
