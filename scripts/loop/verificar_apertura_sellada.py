# -*- coding: utf-8 -*-
r"""verificar_apertura_sellada.py . LA GUARDA DE LA APERTURA (TAREA 1.2 de la
vuelta 101, acta de la vuelta 100, seccion "SEGUNDA CAIDA, DE INCUMPLIMIENTO
DE ENCARGO"). Nombre estable, SIN numero de vuelta (como
tallar_cabecera_reporte.py y contar_cierre_efectivo.py): se invoca con
--vuelta N y no se clona cada vuelta.

POR QUE NACE. EJECUTOR.md 1 dice, desde el 14 ago 2026, "LA APERTURA SE MIDE
ANTES DE LA PRIMERA OPERACION". La vuelta 99 ya habia caido en esto una vez
(acta 99). La vuelta 100 volvio a caer, y peor: SALIDA_V100_HEAD_APERTURA.txt
SI nacio en el primer commit de la vuelta (300802d1, hijo directo de
c8827ef7, el acta de la vuelta 99), pero los OCHO ficheros
SALIDA_V100_*_APERTURA.txt restantes (GATE0_CMD1, CONTEO, DESFASE_CALIBRADO,
ETIQUETAS, MOTOR, SYNC, TSC, WEB) nacieron TODOS en 592cf8bc, el ULTIMO
commit de la vuelta, junto con el reporte final. Nadie lo habia comprobado
con una guarda: el auditor tuvo que medirlo a mano con `git log
--diff-filter=A` sobre cada fichero. Esta guarda automatiza esa medicion.

QUE COMPRUEBA. La vara la da git, no se inventa (EJECUTOR.md, "LA IDENTIDAD
SE LEE DE GIT"): el COMMIT DE NACIMIENTO de cada
`docs/loop/SALIDA_V<vuelta>_*_APERTURA.txt` (el commit que lo ANADE, via
`git log --diff-filter=A`) tiene que ser el PRIMER commit de la vuelta, es
decir, el HIJO DIRECTO del commit del acta de la vuelta anterior (el commit
cuyo mensaje empieza por "ACTA DE LA VUELTA <vuelta-1> DEL AUDITOR", el mismo
patron que ya usa `tallar_cabecera_reporte.py`). Cae en ROJO si:
  - no hay ningun commit "ACTA DE LA VUELTA <vuelta-1> DEL AUDITOR" en la
    rama, o hay mas de uno (ambiguo);
  - algun `SALIDA_V<vuelta>_*_APERTURA.txt` no existe en el arbol de trabajo;
  - algun fichero de apertura no tiene EXACTAMENTE un commit que lo anada
    (cero o mas de uno: ambiguo o no versionado);
  - el PADRE del commit que anade un fichero de apertura NO es el commit del
    acta (nacio despues del primer commit, a mitad o al final de la vuelta).

Nunca inventa un hash ni asume una fecha: todo se lee de `git log` de la rama
actual (`git rev-parse --abbrev-ref HEAD`).

USO:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 101
  python scripts/loop/verificar_apertura_sellada.py --vuelta 100

PRUEBA DE MUTACION (con su salida commiteada,
docs/loop/SALIDA_V101_TAREA1_2_MUTACION_APERTURA.txt): (a) VERDE sobre la
vuelta 101 (bien sellada, con TODOS sus `*_APERTURA.txt` en el primer commit
de la vuelta); (b) ROJO sobre la vuelta 100, el caso negativo real, sin
inventar nada: nombra los ocho ficheros que nacieron en 592cf8bc en vez de en
300802d1.

--- LA GUARDA QUE SE ENVENENA SOLA (TAREA 1.3 de la vuelta 102, acta de la
vuelta 101, "PRIMERA, DE REPORTE, Y ACUMULA") ---

POR QUE NACE. `ficheros_apertura()` hacia glob de
`SALIDA_V<vuelta>_*_APERTURA.txt` sobre el arbol de trabajo, y ese patron
CASA CON SU PROPIA SALIDA: la prueba de mutacion de esta guarda escribe
`docs/loop/SALIDA_V<vuelta>_TAREA1_2_MUTACION_APERTURA.txt`, que empieza por
`SALIDA_V<vuelta>_` y termina en `_APERTURA.txt` igual que cualquier
medicion real. El dia que nace no esta commiteada (glob solo ve el arbol de
trabajo, "ningun commit lo anade"), y desde el commit siguiente nace en el
SEGUNDO commit de la vuelta, nunca en el primero: una guarda que no puede
estar VERDE ni el dia que nace ni ningun dia despues, y que se prueba a si
misma como si fuera una medicion de apertura.

LA DECISION (declarada aqui, con su motivo): `ficheros_apertura()` DESCARTA
todo `SALIDA_V<vuelta>_*_APERTURA.txt` cuyo segmento intermedio (el `*` del
patron) contenga la palabra `MUTACION`. Ninguna medicion de apertura real
(HEAD, GATE0_CMD1, ETIQUETAS, SYNC, MOTOR, WEB, TSC, CONTEO,
DESFASE_CALIBRADO, y las que se sumen despues) lleva `MUTACION` en su
nombre: es una palabra reservada para las propias salidas de prueba de esta
guarda, por convencion desde esta vuelta en adelante. NO SE USO UNA NOMINA
CERRADA de nombres de medicion porque esa lista ha crecido de verdad entre
vueltas (ETIQUETAS y SYNC no existian antes de la vuelta 100) y una nomina
fija se volveria ciega a una medicion nueva y legitima que alguien olvide
anadir a la lista; excluir por la palabra `MUTACION` no tiene ese defecto,
porque una medicion real nunca la necesita para nombrarse.

LA GUARDA NO SE VUELVE CIEGA A UN FICHERO DE APERTURA QUE LLEGUE TARDE DE
VERDAD: la exclusion es por el NOMBRE (contener `MUTACION`), no por cuando
nacio el fichero; cualquier `SALIDA_V<vuelta>_<KIND>_APERTURA.txt` real,
nazca en el primer commit o mas tarde, se sigue viendo y comprobando igual
que antes. Lo unico que deja de verse es la prueba de esta misma guarda.

PRUEBA DE MUTACION (con su salida commiteada,
docs/loop/SALIDA_V102_TAREA1_3_MUTACION_APERTURA.txt): (a) VERDE sobre la
vuelta 101 DESPUES del arreglo (con `SALIDA_V101_TAREA1_2_MUTACION_APERTURA.txt`
todavia presente en el arbol de trabajo, la guarda ya no se la come); (b)
ROJO sobre la vuelta 100, que sigue siendo el caso negativo real, sin
cambios; (c) ROJO si se mueve a mano un fichero de apertura real al SEGUNDO
commit, sobre una copia temporal de repositorio (nunca sobre el repo real):
ver scripts/loop/vuelta102_tarea1_prueba_mutacion_apertura.py, caso (c).

--- EL SELLO FIJA CONTENIDO, NO SOLO NACIMIENTO (TAREA 4, vuelta 108) ---

POR QUE NACE (acta de la vuelta 107, seccion 1.7). Esta guarda comprobaba EN
QUE COMMIT NACIO cada salida de apertura, pero nunca si su CONTENIDO DE HOY
seguia siendo el mismo con el que nacio. La vuelta 107 lo demostro sin
querer: el commit 87b4753d reescribio SALIDA_V107_TSC_APERTURA.txt (nacida
en fcb90afc con la linea "EXIT=0", hoy vacia) y la guarda siguio VERDE
porque solo miraba el commit de nacimiento, nunca el contenido de hoy.

QUE COMPRUEBA, DE MAS. Para cada `SALIDA_V<vuelta>_*_APERTURA.txt`, el
sha256 NORMALIZADO (CRLF y CR sueltos igualados a LF antes de hashear: el
repo tiene `core.autocrlf=true`, asi que el blob de git siempre trae LF
mientras el arbol de trabajo en Windows trae CRLF, y esa diferencia de
sistema operativo NO es un cambio de contenido) del blob del commit de
nacimiento (`git show <nacido_en>:docs/loop/<nombre>`) contra el sha256
NORMALIZADO del fichero de HOY en el arbol de trabajo. Si difieren, ROJO,
nombrando el fichero y los dos hashes completos: nunca se calla cual
cambio ni se resume "algo no cuadra".

Que sea legitimo corregir un artefacto (como la vuelta 107 corrigio el
`EXIT=0` espurio del tsc) no quita que tenga que VERSE: si hay que
reescribir una salida de apertura, se reescribe y esta guarda lo canta, y
el reporte lo explica. Es lo contrario de degradarse en silencio (banco
9, "fallar ruidoso").

CASO POSITIVO OBLIGATORIO (vuelta 108): `--vuelta 107` da ROJO nombrando
`SALIDA_V107_TSC_APERTURA.txt` con sus dos sha256 (docs/loop/
SALIDA_V108_TAREA4_3_CASO_VUELTA107_ROJO.txt, el caso real que lo produjo);
`--vuelta 108`, corrida al cierre de esta misma vuelta, da VERDE.
"""
import argparse
import glob
import hashlib
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")


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
    """Commit cuyo mensaje empieza por 'ACTA DE LA VUELTA <vuelta-1> DEL
    AUDITOR' O por 'ACTA DEL AUDITOR, VUELTA <vuelta-1>', igual que
    tallar_cabecera_reporte.py:commit_apertura_desde_git.

    LA SEGUNDA FORMA SE SUMA EN LA VUELTA 106 (guarda envejecida, hallada al
    sellar la apertura: verificar_apertura_sellada.py --vuelta 106 daba ROJO
    pese a que los diez SALIDA_V106_*_APERTURA.txt nacieron todos, medido a
    mano, como hijos directos de fc504151). El acta de la vuelta 105
    (fc504151) titula su commit 'ACTA DEL AUDITOR, VUELTA 105, mas el
    encargo de la 106.', que rompe por primera vez el patron literal
    'ACTA DE LA VUELTA N DEL AUDITOR' vigente sin excepcion desde la vuelta
    92 (ver git log: 92 a 104 usan la forma vieja). Las dos formas nombran
    lo mismo (el commit del acta que cierra la vuelta N-1); se aceptan las
    dos en vez de renombrar el commit ya publicado."""
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


def es_prueba_de_esta_guarda(nombre, vuelta):
    """Descarta las propias salidas de la prueba de mutacion de esta guarda
    (ver docstring, 'LA GUARDA QUE SE ENVENENA SOLA'): el segmento intermedio
    del nombre (entre el prefijo SALIDA_V<vuelta>_ y el sufijo _APERTURA.txt)
    contiene la palabra MUTACION, que ninguna medicion real usa."""
    prefijo = "SALIDA_V%d_" % vuelta
    sufijo = "_APERTURA.txt"
    medio = nombre[len(prefijo):-len(sufijo)]
    return "MUTACION" in medio


def ficheros_apertura(vuelta):
    patron = os.path.join(LOOP, "SALIDA_V%d_*_APERTURA.txt" % vuelta)
    candidatos = sorted(os.path.basename(p) for p in glob.glob(patron))
    return [n for n in candidatos if not es_prueba_de_esta_guarda(n, vuelta)]


def commit_de_nacimiento(nombre, rama, fallos):
    rel = "docs/loop/%s" % nombre
    out = _git(["log", rama, "--diff-filter=A", "--pretty=format:%H", "--", rel],
               fallos, "nacimiento de %s" % nombre)
    if out is None:
        return None
    hallados = [h for h in out.splitlines() if h.strip()]
    if not hallados:
        fallos.append("%s: ningun commit lo anade (no versionado)" % nombre)
        return None
    if len(hallados) > 1:
        fallos.append("%s: %d commits lo anaden (%s): ambiguo" %
                      (nombre, len(hallados), ", ".join(h[:8] for h in hallados)))
        return None
    return hallados[0]


def _normalizar_finales_de_linea(datos):
    """CRLF/LF no es cambio de CONTENIDO (TAREA 4, vuelta 108): este repo
    tiene core.autocrlf=true, asi que el arbol de trabajo en Windows trae
    CRLF mientras que el blob de git (lo que `git show <commit>:ruta`
    devuelve) siempre trae LF. Comparar los bytes crudos daria ROJO en
    TODO fichero de mas de una linea, sin que nadie lo haya tocado de
    verdad. Se normaliza CRLF y CR sueltos a LF en los dos lados antes de
    hashear, para que la guarda mida CONTENIDO y no la convencion de fin de
    linea del sistema operativo."""
    return datos.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def sha256_normalizado(datos):
    return hashlib.sha256(_normalizar_finales_de_linea(datos)).hexdigest()


def blob_de_nacimiento(nombre, nacido_en, fallos):
    """El contenido del fichero TAL COMO QUEDO en el commit que lo anadio
    (TAREA 4.1, vuelta 108): `git show <nacido_en>:docs/loop/<nombre>`."""
    rel = "docs/loop/%s" % nombre
    try:
        r = subprocess.run(["git", "show", "%s:%s" % (nacido_en, rel)], cwd=RAIZ,
                           capture_output=True, check=True)
        return r.stdout
    except Exception as e:
        fallos.append("no se pudo leer el blob de nacimiento de %s en %s: %s"
                      % (nombre, nacido_en[:8], e))
        return None


def contenido_igual_al_nacer(nombre, nacido_en, fallos):
    """TAREA 4 de la vuelta 108 (encargo del auditor, acta de la vuelta 107,
    seccion 1.7: "LA GUARDA DEL SELLO QUE NO ALCANZA"). El sello de
    verificar_apertura_sellada.py comprobaba EN QUE COMMIT NACIO cada salida
    de apertura, pero nunca si su CONTENIDO DE HOY seguia siendo el mismo con
    el que nacio. La vuelta 107 lo demostro sin querer: el commit 87b4753d
    reescribio SALIDA_V107_TSC_APERTURA.txt (nacida en fcb90afc con la linea
    "EXIT=0", hoy vacia) y la guarda siguio VERDE.

    Compara el sha256 NORMALIZADO (ver _normalizar_finales_de_linea) del blob
    del commit de nacimiento contra el sha256 NORMALIZADO del fichero de HOY
    en el arbol de trabajo. Devuelve (iguales, hash_nacimiento, hash_hoy);
    (None, None, None) si el fichero de hoy no existe o el blob no se pudo
    leer (fallo ya registrado en `fallos` por el llamador)."""
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        fallos.append("%s no existe en el arbol de trabajo (no se puede comparar contenido)" % nombre)
        return None, None, None
    blob = blob_de_nacimiento(nombre, nacido_en, fallos)
    if blob is None:
        return None, None, None
    with open(ruta, "rb") as f:
        hoy = f.read()
    h_nac = sha256_normalizado(blob)
    h_hoy = sha256_normalizado(hoy)
    return h_nac == h_hoy, h_nac, h_hoy


def verificar(vuelta):
    fallos = []
    rama = rama_actual(fallos)
    if rama is None:
        return fallos, []
    acta = commit_acta(vuelta, rama, fallos)
    if acta is None:
        return fallos, []

    nombres = ficheros_apertura(vuelta)
    if not nombres:
        fallos.append("no existe ningun docs/loop/SALIDA_V%d_*_APERTURA.txt en el arbol de trabajo" % vuelta)
        return fallos, []

    detalle = []
    for nombre in nombres:
        nacido_en = commit_de_nacimiento(nombre, rama, fallos)
        if nacido_en is None:
            continue
        padre_out = _git(["rev-parse", "%s^" % nacido_en], fallos, "padre de %s" % nacido_en)
        padre = padre_out.strip() if padre_out is not None else None
        if padre is None:
            continue
        if padre != acta:
            fallos.append("%s nacio en %s, cuyo padre es %s (no el commit del acta %s): "
                          "no se sello antes de la 1.a operacion" %
                          (nombre, nacido_en[:8], padre[:8], acta[:8]))

        # TAREA 4 (vuelta 108): el sello fija CONTENIDO, no solo nacimiento.
        iguales, h_nac, h_hoy = contenido_igual_al_nacer(nombre, nacido_en, fallos)
        if iguales is False:
            fallos.append("%s CAMBIO DE CONTENIDO despues de nacer en %s: sha256 de nacimiento "
                          "%s, sha256 de hoy %s" % (nombre, nacido_en[:8], h_nac, h_hoy))

        detalle.append((nombre, nacido_en[:8], padre[:8] if padre else "?", padre == acta))
    return fallos, detalle


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, required=True)
    a = ap.parse_args()

    fallos, detalle = verificar(a.vuelta)
    if fallos:
        print("ROJO, apertura de la vuelta %d NO sellada antes de la 1.a operacion "
              "(%d cosa(s) no cuadran):" % (a.vuelta, len(fallos)))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("VERDE: los %d ficheros SALIDA_V%d_*_APERTURA.txt nacieron todos en el "
          "primer commit de la vuelta (hijo directo del acta):" % (len(detalle), a.vuelta))
    for nombre, nacido_en, padre, ok in detalle:
        print("   %s -- nacido en %s, padre %s" % (nombre, nacido_en, padre))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
