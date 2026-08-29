# -*- coding: utf-8 -*-
r"""tallar_identidad_reporte.py . LA ESCALADA DE LA VUELTA 132 (TAREA 2, acta de
la vuelta 132, seccion "LO QUE COBRA LA 132"): talla el PARRAFO DE IDENTIDAD del
reporte, los tres rotulos ("HEAD sellado de apertura", "commit de nacimiento de
las salidas de apertura", "HEAD sellado de cierre"), para que NINGUNO se teclee.

POR QUE NACE. La vuelta 132 publico como "commit de nacimiento de las salidas
de apertura" el hash de la vuelta ANTERIOR (5eb04ca5), copiado por encima del
tercero, cuando las once salidas V132_*_APERTURA.txt nacieron todas en 3a5fd829
(medido con `git log --diff-filter=A --format=%h -1 --`). El agravante: el
propio `verificar_apertura_sellada.py --vuelta 132` corrido esa vuelta imprimia
en cada linea "nacido en 3a5fd829, padre 5eb04ca5" -- el instrumento tenia la
cifra buena delante y se tecleo la vieja igual. Es la caida que EJECUTOR.md 1
("LA IDENTIDAD SE LEE DE GIT") ya prohibia desde la vuelta 79, entrando por una
prosa que ese tallador no cubria: la linea de identidad vive SUELTA encima de
la tabla que `tallar_cabecera_reporte.py --fase04` si talla, y por eso se siguio
tecleando a mano.

LOS TRES ROTULOS, y de donde sale cada uno:
  - "HEAD sellado de apertura": la UNICA linea de
    docs/loop/SALIDA_V<N>_HEAD_APERTURA.txt. Se valida con `git cat-file -t`
    (tiene que ser "commit") y con `git branch --contains` (tiene que aparecer
    en la rama actual).
  - "commit de nacimiento de las salidas de apertura": `git log
    --diff-filter=A --format=%h -1 -- docs/loop/SALIDA_V<N>_<K>_APERTURA.txt`
    sobre TODOS los `SALIDA_V<N>_*_APERTURA.txt` que existan en el arbol de
    trabajo (excluyendo los que llevan `MUTACION` en el segmento intermedio,
    misma exclusion que `verificar_apertura_sellada.py:es_prueba_de_esta_guarda`,
    para que la propia prueba de esta guarda no se coma a si misma). Si no
    salen TODOS del MISMO commit, ROJO nombrando cada fichero con su commit.
  - "HEAD sellado de cierre": la UNICA linea de
    docs/loop/SALIDA_V<N>_HEAD_CIERRE.txt, validada igual que la de apertura.

LA REGLA QUE HABRIA CAZADO LA 132 SOLA: se comparan los TRES hashes entre si
(normalizados a hash completo via `git rev-parse`). Si DOS CUALESQUIERA
coinciden, el tallador NO calla y NO lo da por bueno: escribe "rotulo X y
rotulo Y coinciden en <hash>" y anade la razon MEDIDA (nunca supuesta) de por
que coinciden, leyendo `git show --stat` del commit compartido para nombrar que
otros SALIDA_V<N>_*.txt trae ese mismo commit. Una coincidencia declarada es un
dato; una coincidencia muda es la caida de la 132.

USO:
  python scripts/loop/tallar_identidad_reporte.py --vuelta 133
  python scripts/loop/tallar_identidad_reporte.py --vuelta 133 --comparar docs/loop/REPORTE.md

--comparar RUTA extrae el parrafo de identidad que ese fichero YA tiene
(busca las tres lineas por su rotulo, en cualquier orden) y coteja rotulo por
rotulo contra lo tallado; termina con "IDENTIDAD IDENTICA AL TALLADOR" (exit 0)
o con ROJO exit 1 nombrando el rotulo, el hash escrito y el hash medido. Si el
reporte no trae los tres rotulos, tambien es ROJO, nombrando el que falta.

PRUEBAS DE MUTACION (2.c, obligatorias antes de publicar la guarda, EJECUTOR.md
1 "EL CASO ROJO SE PRUEBA POR MUTACION"): sobre una COPIA del reporte, nunca
sobre el real.
  MUTACION A: pone en el rotulo "commit de nacimiento" el hash del rotulo
    "HEAD sellado de apertura" -- es EXACTAMENTE la caida de la 132 -- y
    comprueba que --comparar cae en ROJO nombrando ese rotulo.
  MUTACION B: cambia un caracter del hash del rotulo "HEAD sellado de cierre"
    y comprueba lo mismo.
Ver scripts/loop/vuelta133_tarea2c_mutaciones_identidad.py, que corre las dos
y escribe docs/loop/SALIDA_V133_2C_MUTACION_A.txt y _MUTACION_B.txt.
"""
import argparse
import io
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")

ROTULO_APERTURA = "HEAD sellado de apertura"
ROTULO_NACIMIENTO = "commit de nacimiento de las salidas de apertura"
ROTULO_CIERRE = "HEAD sellado de cierre"
ROTULOS = [ROTULO_APERTURA, ROTULO_NACIMIENTO, ROTULO_CIERRE]


def _git(args, fallos, contexto):
    try:
        r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True, text=True,
                            encoding="utf-8", check=True)
        return r.stdout
    except Exception as e:
        fallos.append("no se pudo correr git %s (%s): %s" % (" ".join(args), contexto, e))
        return None


def rama_actual(fallos):
    out = _git(["rev-parse", "--abbrev-ref", "HEAD"], fallos, "rama actual")
    return out.strip() if out is not None else None


def leer_sello(nombre, fallos):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        fallos.append("%s no existe" % nombre)
        return None
    txt = io.open(ruta, encoding="utf-8").read().strip()
    if not re.match(r"^[0-9a-f]{40}$", txt):
        fallos.append("%s no trae un hash completo de 40 caracteres: %r" % (nombre, txt))
        return None
    return txt


def validar_commit_en_rama(hash_, rama, etiqueta, fallos):
    tipo = _git(["cat-file", "-t", hash_], fallos, "tipo de %s" % hash_)
    if tipo is None:
        return False
    if tipo.strip() != "commit":
        fallos.append("%s: %s no es un commit (es %s)" % (etiqueta, hash_, tipo.strip()))
        return False
    ramas = _git(["branch", "--contains", hash_], fallos, "ramas que contienen %s" % hash_)
    if ramas is None:
        return False
    nombres = [l.strip().lstrip("* ").strip() for l in ramas.splitlines() if l.strip()]
    if rama not in nombres:
        fallos.append("%s: %s no aparece en la rama actual %s (branch --contains: %s)" %
                       (etiqueta, hash_, rama, ", ".join(nombres) or "ninguna"))
        return False
    return True


def es_prueba_de_esta_guarda(nombre, vuelta):
    """Misma exclusion que verificar_apertura_sellada.py: el segmento
    intermedio del nombre no puede contener MUTACION, o la propia prueba de
    esta guarda se contaria como una salida de apertura real."""
    prefijo = "SALIDA_V%d_" % vuelta
    sufijo = "_APERTURA.txt"
    medio = nombre[len(prefijo):-len(sufijo)]
    return "MUTACION" in medio


def ficheros_apertura(vuelta):
    import glob
    patron = os.path.join(LOOP, "SALIDA_V%d_*_APERTURA.txt" % vuelta)
    candidatos = sorted(os.path.basename(p) for p in glob.glob(patron))
    return [n for n in candidatos if not es_prueba_de_esta_guarda(n, vuelta)]


def commit_de_nacimiento(nombre, rama, fallos):
    rel = "docs/loop/%s" % nombre
    out = _git(["log", rama, "--diff-filter=A", "--format=%h", "-1", "--", rel],
               fallos, "nacimiento de %s" % nombre)
    if out is None:
        return None
    h = out.strip()
    if not h:
        fallos.append("%s: ningun commit lo anade (no versionado)" % nombre)
        return None
    return h


def commit_nacimiento_de_apertura(vuelta, rama, fallos):
    nombres = ficheros_apertura(vuelta)
    if not nombres:
        fallos.append("no existe ningun SALIDA_V%d_*_APERTURA.txt en el arbol de trabajo" % vuelta)
        return None
    por_commit = {}
    for nombre in nombres:
        h = commit_de_nacimiento(nombre, rama, fallos)
        if h is None:
            continue
        por_commit.setdefault(h, []).append(nombre)
    if not por_commit:
        return None
    if len(por_commit) > 1:
        fallos.append("las salidas de apertura NO nacieron todas en el mismo commit:")
        for h, ns in sorted(por_commit.items()):
            fallos.append("  %s: %s" % (h, ", ".join(sorted(ns))))
        return None
    return list(por_commit.keys())[0]


def hash_completo(hash_corto_o_largo, fallos):
    out = _git(["rev-parse", hash_corto_o_largo], fallos, "rev-parse %s" % hash_corto_o_largo)
    return out.strip() if out is not None else None


def razon_de_coincidencia(hash_compartido, fallos):
    out = _git(["show", "--stat", "--format=%H", hash_compartido], fallos,
                "show --stat de %s" % hash_compartido)
    if out is None:
        return "no se pudo medir la razon (git show --stat fallo)"
    lineas = [l for l in out.splitlines() if "docs/loop/SALIDA_" in l or "docs/loop/SALIDA" in l]
    if lineas:
        return "el commit %s trae, entre otros, estos ficheros de salida: %s" % (
            hash_compartido[:8], "; ".join(l.strip() for l in lineas[:6]))
    return "el commit %s es el mismo objeto para los dos rotulos (git show --stat no lista SALIDA_* propios)" % hash_compartido[:8]


def tallar(vuelta):
    fallos = []
    rama = rama_actual(fallos)
    if rama is None:
        return None, fallos

    h_apertura = leer_sello("SALIDA_V%d_HEAD_APERTURA.txt" % vuelta, fallos)
    if h_apertura is not None:
        validar_commit_en_rama(h_apertura, rama, ROTULO_APERTURA, fallos)

    h_nacimiento_corto = commit_nacimiento_de_apertura(vuelta, rama, fallos)
    h_nacimiento = hash_completo(h_nacimiento_corto, fallos) if h_nacimiento_corto else None

    h_cierre = leer_sello("SALIDA_V%d_HEAD_CIERRE.txt" % vuelta, fallos)
    if h_cierre is not None:
        validar_commit_en_rama(h_cierre, rama, ROTULO_CIERRE, fallos)

    if fallos:
        return None, fallos

    valores = {
        ROTULO_APERTURA: h_apertura,
        ROTULO_NACIMIENTO: h_nacimiento,
        ROTULO_CIERRE: h_cierre,
    }

    coincidencias = []
    pares = [(ROTULO_APERTURA, ROTULO_NACIMIENTO), (ROTULO_APERTURA, ROTULO_CIERRE),
             (ROTULO_NACIMIENTO, ROTULO_CIERRE)]
    for a, b in pares:
        if valores[a] == valores[b]:
            razon = razon_de_coincidencia(valores[a], fallos)
            coincidencias.append("rotulo %s y rotulo %s coinciden en %s (%s)" % (a, b, valores[a][:8], razon))

    return {
        "valores": valores,
        "corto": {ROTULO_APERTURA: h_apertura[:8], ROTULO_NACIMIENTO: h_nacimiento_corto,
                  ROTULO_CIERRE: h_cierre[:8]},
        "coincidencias": coincidencias,
    }, fallos


def parrafo(tallado):
    v = tallado["corto"]
    lineas = [
        "%s: `%s`" % (ROTULO_APERTURA, v[ROTULO_APERTURA]),
        "%s: `%s`" % (ROTULO_NACIMIENTO, v[ROTULO_NACIMIENTO]),
        "%s: `%s`" % (ROTULO_CIERRE, v[ROTULO_CIERRE]),
    ]
    if tallado["coincidencias"]:
        for c in tallado["coincidencias"]:
            lineas.append("ATENCION: %s" % c)
    else:
        lineas.append("los tres rotulos salen con hash distinto entre si.")
    return "\n".join(lineas)


def extraer_del_reporte(ruta):
    if not os.path.exists(ruta):
        return None, "no existe %s" % ruta
    txt = io.open(ruta, encoding="utf-8").read()
    encontrados = {}
    for rotulo in ROTULOS:
        m = re.search(re.escape(rotulo) + r"[:\s]*`?([0-9a-f]{7,40})`?", txt)
        if m:
            encontrados[rotulo] = m.group(1)
    return encontrados, None


def comparar(vuelta, ruta_reporte):
    tallado, fallos = tallar(vuelta)
    if fallos:
        print("ROJO, no se pudo tallar la identidad de la vuelta %d (%d cosa(s) no cuadran):" %
              (vuelta, len(fallos)))
        for f in fallos:
            print("  %s" % f)
        return 1

    encontrados, err = extraer_del_reporte(ruta_reporte)
    if err:
        print("ROJO: %s" % err)
        return 1

    faltan = [r for r in ROTULOS if r not in encontrados]
    if faltan:
        print("ROJO: el reporte no trae el/los rotulo(s): %s" % ", ".join(faltan))
        return 1

    difs = []
    for rotulo in ROTULOS:
        escrito = encontrados[rotulo]
        medido_completo = tallado["valores"][rotulo]
        medido_corto = tallado["corto"][rotulo]
        if escrito != medido_completo and escrito != medido_corto and not medido_completo.startswith(escrito) \
                and not medido_corto.startswith(escrito):
            difs.append((rotulo, escrito, medido_corto))

    if difs:
        print("ROJO, %d rotulo(s) no cuadran:" % len(difs))
        for rotulo, escrito, medido in difs:
            print("  %s: reporte dice `%s`, medido `%s`" % (rotulo, escrito, medido))
        return 1

    print("IDENTIDAD IDENTICA AL TALLADOR (vuelta %d)" % vuelta)
    for rotulo in ROTULOS:
        print("  %s: `%s`" % (rotulo, tallado["corto"][rotulo]))
    if tallado["coincidencias"]:
        for c in tallado["coincidencias"]:
            print("  ATENCION: %s" % c)
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, required=True)
    ap.add_argument("--comparar", default=None)
    a = ap.parse_args()

    if a.comparar:
        return comparar(a.vuelta, a.comparar)

    tallado, fallos = tallar(a.vuelta)
    if fallos:
        print("ROJO, no se pudo tallar la identidad de la vuelta %d (%d cosa(s) no cuadran):" %
              (a.vuelta, len(fallos)))
        for f in fallos:
            print("  %s" % f)
        return 1
    print(parrafo(tallado))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
