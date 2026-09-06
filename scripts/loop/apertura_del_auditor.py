# -*- coding: utf-8 -*-
r"""apertura_del_auditor.py . EL BLOQUE DE APERTURA DEL AUDITOR, GEMELO DEL DEL
EJECUTOR: CORRE `aislador_de_ciega.py` Y SELLA SU SALIDA ANTES DE QUE EL TURNO
PUEDA TOCAR `git log`, `git status` O `REPORTE.md`.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como `aislador_de_ciega.py`,
`tallar_cabecera_reporte.py`, `archivar_reporte.py`, `serie_de_registros.py` y
`cerrar_reporte.py`: se usa en TODA vuelta y NO SE CLONA. Un fichero que se clona
por vuelta es un fichero que la vuelta siguiente puede olvidar, y olvidarse es
justamente la enfermedad que esto viene a curar.

DE DONDE SALE, PALABRA POR PALABRA. Decision del fundador del 5 sep 2026,
PREGUNTA 3, opcion `c`, en
`docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md`: *"la apertura del
auditor pasa a CODIGO (fichero gemelo del bloque de apertura del ejecutor: corre
`aislador_de_ciega.py` y SELLA su salida antes de que el turno pueda tocar `git
log`, `git status` o `REPORTE.md`) y ademas ROMPER UN REMEDIO ESCRITO ACUMULA"*.
**Esta es la mitad que quita el problema de raiz; la otra mitad ya esta escrita en
`AUDITOR.md`.** Y en `AUDITOR.md`, seccion 1, la misma decision esta recogida:
*"con eso, aislar el sujeto deja de depender de que alguien se acuerde"*.

POR QUE HACE FALTA, Y NO ES UNA SOSPECHA: **CUATRO ACTAS SEGUIDAS** con la misma
caida propia `C.1` (178, 179, 180 y 181), y **la de la 181 es la primera en que el
remedio escrito ya existia y aun asi no se cumplio**. El acta 180 le dejo escrito
al auditor de la 181, en su linea 62490, que su PRIMER comando fuera el aislador y
que *"hasta que esos dos ficheros existan no se corre `git log`, ni `git status`,
ni se abre `REPORTE.md`"*. El acta 181 lo declara asi, en su seccion 2: *"Rompi las
tres"*.

COMO LO IMPIDE, Y ES LO UNICO QUE HACE:

  1. LLEVA UNA BITACORA DE TOQUES. Las tres cosas prohibidas **solo se pueden
     hacer llamando a las funciones de aqui** (`git_log`, `git_status`,
     `leer_reporte`), y cada una **apunta su toque antes de hacerlo**.
  2. `sellar()` **CAE EN ROJO si la bitacora ya trae alguno de los tres**, y NO
     escribe el sello. No avisa ni recomienda: no sella.
  3. El sello es un fichero con el criterio, la ruta de la ciega, la del destape,
     sus bytes y sus `sha256`. **Existe o no existe**, y quien lo lea sabe si el
     sujeto se aislo antes o despues.

LO QUE NO HACE, Y SE DICE PARA QUE NADIE LE PIDA MAS: **no puede impedir que
alguien corra `git status` en su terminal por su cuenta.** Ninguna guarda de este
repo puede. Lo que si hace es que **el sello, que es lo que el acta cita como
prueba, no se pueda escribir despues**; y el auditor que quiera saltarse esto
tiene que hacerlo **a sabiendas y sin sello**, que es exactamente la diferencia
entre un descuido y una decision.

EL ORDEN OBLIGATORIO DE UN TURNO DE AUDITOR:

    from apertura_del_auditor import sellar, git_log, git_status, leer_reporte
    sellar(criterio="...", muestra=30, semilla=182)   # PRIMERO, y solo esto
    ...                                               # ya se puede verificar
    git_status()                                      # apunta su toque

USO:
  python scripts/loop/apertura_del_auditor.py --criterio "..." --muestra 30 \
      --semilla 182 --vuelta 182
  python scripts/loop/apertura_del_auditor.py --estado
"""
import argparse
import hashlib
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

# LAS TRES COSAS QUE EL REMEDIO PROHIBE ANTES DEL SELLO. Van como constante y con
# nombre para que el arnes las pueda recorrer una a una en vez de que el caso
# rojo elija cual probar.
PROHIBIDOS_ANTES_DEL_SELLO = ("git log", "git status", "REPORTE.md")

# LA BITACORA. Es del modulo a proposito: el estado tiene que sobrevivir entre
# llamadas dentro del mismo turno, que es lo que se esta vigilando.
_BITACORA = []
_SELLADO = {"hecho": False, "ruta": None}


def bitacora():
    """LOS TOQUES APUNTADOS HASTA AHORA, en orden. Copia, no el original."""
    return list(_BITACORA)


def apuntar(que):
    """APUNTA UN TOQUE. Se llama ANTES de hacer la cosa, no despues: si la cosa
    revienta, el toque igual paso."""
    _BITACORA.append(que)
    return que


def toques_prohibidos():
    """LOS TOQUES DE LA BITACORA QUE ESTAN EN LA LISTA PROHIBIDA. PURA sobre el
    estado del modulo, y es la funcion que `sellar()` consulta."""
    return [t for t in _BITACORA if t in PROHIBIDOS_ANTES_DEL_SELLO]


def olvidar_todo():
    """VACIA LA BITACORA Y EL SELLO. **Solo para los arneses**, que necesitan
    correr varios escenarios en el mismo proceso. Un turno de auditor no la llama
    nunca, y si la llamara estaria borrando su propia prueba a mano, que es una
    decision y no un descuido."""
    del _BITACORA[:]
    _SELLADO["hecho"] = False
    _SELLADO["ruta"] = None


def git_log(*args):
    """`git log`, Y APUNTA SU TOQUE."""
    apuntar("git log")
    return _git(["log"] + list(args))


def git_status(*args):
    """`git status`, Y APUNTA SU TOQUE."""
    apuntar("git status")
    return _git(["status"] + list(args))


def leer_reporte(ruta=None):
    """Abre `docs/loop/REPORTE.md`, Y APUNTA SU TOQUE."""
    apuntar("REPORTE.md")
    ruta = ruta or os.path.join(LOOP, "REPORTE.md")
    if not os.path.exists(ruta):
        return ""
    return io.open(ruta, encoding="utf-8", errors="replace").read()


def _git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", errors="replace")


def sha(t):
    return hashlib.sha256(t.replace(chr(13) + NL, NL).encode("utf-8")).hexdigest()


def puede_sellar():
    """(SI_PUEDE, MOTIVO). PURA sobre el estado del modulo.

    ESTA ES LA FUNCION QUE EL ARNES TUMBA, y por eso esta separada de `sellar()`:
    la decision se puede probar sin escribir un solo fichero."""
    malos = toques_prohibidos()
    if malos:
        return False, ("el turno ya toco %s antes de sellar. EL SUJETO DE LA CIEGA "
                       "YA PUDO QUEMARSE, y un sello escrito ahora no probaria "
                       "nada." % ", ".join(repr(m) for m in malos))
    if _SELLADO["hecho"]:
        return False, "este turno ya sello: un sello no se reescribe"
    return True, "la bitacora esta limpia de los tres prohibidos"


def sellar(criterio, vuelta, muestra=None, semilla=None, puestos=None,
           excluir=None, dominio=None, clase=None, dir_salida=None):
    """CORRE EL AISLADOR Y SELLA SU SALIDA. Devuelve (ok, informe).

    CAE EN ROJO Y NO ESCRIBE NADA si `puede_sellar()` dice que no. El rojo es del
    sello entero: no se escribe el sello, y tampoco se corre el aislador, porque
    correrlo sin poder sellarlo seria producir una ciega que nadie puede citar."""
    informe = []
    w = informe.append
    ok, motivo = puede_sellar()
    w("PUEDE SELLAR: %s" % ("SI" if ok else "NO"))
    w("   motivo: %s" % motivo)
    w("   bitacora del turno hasta ahora: %s"
      % (", ".join(bitacora()) if bitacora() else "(vacia)"))
    if not ok:
        w("ROJO: NO se corre el aislador y NO se escribe ningun sello.")
        return False, informe

    base = dir_salida or LOOP
    ciega = os.path.join(base, "_auditor_v%s_ciega_blind.txt" % vuelta)
    destape = os.path.join(base, "_auditor_v%s_ciega_reveal.txt" % vuelta)
    cmd = [sys.executable, os.path.join(RAIZ, "scripts", "loop",
                                        "aislador_de_ciega.py"),
           "--criterio", criterio, "--ciega", ciega, "--destape", destape]
    for bandera, valor in (("--muestra", muestra), ("--semilla", semilla),
                           ("--puestos", puestos), ("--excluir", excluir),
                           ("--dominio", dominio), ("--clase", clase)):
        if valor is not None:
            cmd += [bandera, str(valor)]
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, env=env)
    salida = (r.stdout.decode("utf-8", errors="replace")
              + r.stderr.decode("utf-8", errors="replace"))
    w("AISLADOR CORRIDO -> EXITCODE %d" % r.returncode)
    if r.returncode != 0 or not os.path.exists(ciega) or not os.path.exists(destape):
        w("ROJO: el aislador no dejo sus dos ficheros. NO se escribe sello.")
        for l in salida.split(NL)[-12:]:
            if l.strip():
                w("   | " + l.strip()[:130])
        return False, informe

    t_ciega = io.open(ciega, encoding="utf-8").read()
    t_destape = io.open(destape, encoding="utf-8").read()
    sello = {
        "vuelta": vuelta,
        "criterio": criterio,
        "ciega": os.path.relpath(ciega, RAIZ).replace(os.sep, "/"),
        "destape": os.path.relpath(destape, RAIZ).replace(os.sep, "/"),
        "bytes_ciega": os.path.getsize(ciega),
        "bytes_destape": os.path.getsize(destape),
        "sha256_ciega": sha(t_ciega),
        "sha256_destape": sha(t_destape),
        "bitacora_antes_del_sello": bitacora(),
        "prohibidos_antes_del_sello": toques_prohibidos(),
    }
    ruta = os.path.join(base, "SELLO_APERTURA_AUDITOR_V%s.json" % vuelta)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(
        json.dumps(sello, ensure_ascii=False, indent=1) + NL)
    _SELLADO["hecho"] = True
    _SELLADO["ruta"] = ruta
    w("SELLO ESCRITO: %s (%d bytes)"
      % (os.path.relpath(ruta, RAIZ).replace(os.sep, "/"), os.path.getsize(ruta)))
    w("   ciega   %s -> %d bytes | sha256 %s"
      % (sello["ciega"], sello["bytes_ciega"], sello["sha256_ciega"][:16]))
    w("   destape %s -> %d bytes | sha256 %s"
      % (sello["destape"], sello["bytes_destape"], sello["sha256_destape"][:16]))
    w("   prohibidos tocados antes del sello: %d"
      % len(sello["prohibidos_antes_del_sello"]))
    return True, informe


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--criterio")
    ap.add_argument("--vuelta")
    ap.add_argument("--muestra", type=int)
    ap.add_argument("--semilla", type=int)
    ap.add_argument("--puestos")
    ap.add_argument("--excluir")
    ap.add_argument("--dominio")
    ap.add_argument("--clase")
    ap.add_argument("--estado", action="store_true",
                    help="imprime la bitacora y si se puede sellar, y no hace mas")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("APERTURA DEL AUDITOR. Gemelo del bloque de apertura del ejecutor.")
    print("=" * 78)
    print("   LOS TRES PROHIBIDOS ANTES DEL SELLO: %s"
          % ", ".join(repr(p) for p in PROHIBIDOS_ANTES_DEL_SELLO))
    if a.estado:
        ok, motivo = puede_sellar()
        print("   bitacora: %s" % (", ".join(bitacora()) or "(vacia)"))
        print("   PUEDE SELLAR: %s (%s)" % ("SI" if ok else "NO", motivo))
        return 0
    if not a.criterio or not a.vuelta:
        print("   ROJO: --criterio y --vuelta son obligatorios. Sin criterio "
              "escrito no se elige ningun sujeto.")
        return 1
    ok, informe = sellar(a.criterio, a.vuelta, muestra=a.muestra,
                         semilla=a.semilla, puestos=a.puestos, excluir=a.excluir,
                         dominio=a.dominio, clase=a.clase)
    for l in informe:
        print("   " + l)
    print("   VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
