# -*- coding: utf-8 -*-
r"""_v209_t2c_cerrar_opl01.py . TAREA 2.c DE LA VUELTA 209: SE CIERRA `OP-L-01`
TOCANDO **SOLO** SU CAMPO `estado`.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3).

**ES LA PRIMERA VEZ QUE EL ENCARGO AUTORIZA TOCAR UN `estado`, Y VA CON LAS TRES
GUARDAS QUE EL PROPIO ENCARGO PONE:**

  (1) EL VALOR VIEJO SE LEE Y SE PUBLICA AL LADO DEL NUEVO. No se escribe
      "queda HECHA": se escribe "pasa de LISTA a HECHA", con las dos leidas del
      fichero.
  (2) `docs/plan/OPERACIONES.jsonl` se publica POR LAS DOS CONVENCIONES, ANTES y
      DESPUES, con sus dos `sha256`.
  (3) `git diff --numstat` sobre esa sede tiene que dar **UNA linea cambiada y ni
      una mas**, y **ningun otro `id_op` se puede haber movido**. Si el numstat
      toca mas de una linea, SE PARA Y SE TRAE.

**EL VALOR NUEVO NO SE INVENTA:** se comprueba que `HECHA` ya es vocabulario del
propio fichero contando cuantas fichas lo llevan hoy. Un valor que no exista en
la sede seria doctrina nueva, y eso no lo decide el ejecutor.

**LA ESCRITURA ES CIRUGIA DE TEXTO, NO RE-SERIALIZACION.** Se sustituye el par
`"estado": "LISTA"` **dentro de su linea y solo ahi**, comprobado que aparece
exactamente una vez en esa linea. Volver a serializar el JSON reordenaria claves
o cambiaria espaciados y ensuciaria el `numstat` de las otras lineas, que es
justo lo que la guarda (3) mide.
"""
import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
RUTA_REL = "docs/plan/OPERACIONES.jsonl"
VUELTA = 209
FICHA = "OP-L-01"
LINEA = 41
VIEJO = "LISTA"
NUEVO = "HECHA"


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def dos_convenciones(ruta):
    crudo = io.open(ruta, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    return (len(crudo), len(lf),
            hashlib.sha256(crudo).hexdigest()[:16],
            hashlib.sha256(lf).hexdigest()[:16], lf.decode("utf-8"))


def censo(texto):
    """CADA `id_op` CON SU `estado`, EN ORDEN. Es la foto que la guarda (3)
    coteja entera para probar que no se movio nadie mas."""
    out = []
    for i, l in enumerate(texto.split(NL), 1):
        if not l.strip():
            continue
        d = json.loads(l)
        out.append((i, d["id_op"], d.get("estado")))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    ap.add_argument("--salida", default="T2C_CERRAR_OPL01")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append

    def cerrar(codigo):
        salida = NL.join(L) + NL
        print(salida)
        io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
                "w", encoding="utf-8", newline=NL).write(salida)
        return codigo

    w("=" * 78)
    w("VUELTA %d, TAREA 2.c: SE CIERRA %s TOCANDO SOLO SU CAMPO estado"
      % (VUELTA, FICHA))
    w("=" * 78)
    w("")

    w("GUARDA (2), PRIMERA MITAD: LA SEDE **ANTES**, POR LAS DOS CONVENCIONES")
    d0, lf0, sd0, sl0, texto0 = dos_convenciones(OPS)
    w("   %s: %d bytes en disco y %d bytes normalizado a LF" % (RUTA_REL, d0, lf0))
    w("   sha256 disco %s y sha256 LF %s" % (sd0, sl0))
    w("   contraste del encargo: 513043 por las dos y sha256 829c583eb779cab6")
    calza = (d0 == 513043 and lf0 == 513043 and sd0 == "829c583eb779cab6"
             and sl0 == "829c583eb779cab6")
    w("   CALZA: %s" % ("SI" if calza else "NO, Y LA DISCREPANCIA SE DECLARA"))
    censo0 = censo(texto0)
    w("   CIFRA fichas en el fichero: %d" % len(censo0))
    w("")

    w("GUARDA (1): EL VALOR VIEJO, LEIDO Y NO SUPUESTO")
    ls0 = texto0.split(NL)
    if LINEA > len(ls0):
        w("   ROJO: el fichero no llega a la linea %d." % LINEA)
        return cerrar(1)
    linea0 = ls0[LINEA - 1]
    d = json.loads(linea0)
    w("   linea %d, id_op leido: %s" % (LINEA, d["id_op"]))
    w("   es la ficha que el encargo nombra: %s"
      % ("SI" if d["id_op"] == FICHA else "NO, Y ESO ES ROJO"))
    if d["id_op"] != FICHA:
        return cerrar(1)
    w("   CIFRA campos de la ficha: %d" % len(d))
    w("   VALOR VIEJO del campo estado, leido del fichero: %r" % d.get("estado"))
    w("   VALOR NUEVO que se va a escribir:                %r" % NUEVO)
    if d.get("estado") != VIEJO:
        w("   ROJO: el valor viejo no es el que el encargo dice (%r)." % VIEJO)
        return cerrar(1)
    w("")

    w("EL VALOR NUEVO NO SE INVENTA: SE COMPRUEBA QUE YA ES VOCABULARIO DE LA SEDE")
    reparto = {}
    for _i, _id, e in censo0:
        reparto[e] = reparto.get(e, 0) + 1
    for k in sorted(reparto):
        w("   estado %-8r lo llevan %d fichas hoy" % (k, reparto[k]))
    w("   %r ya existe en el fichero: %s"
      % (NUEVO, "SI" if NUEVO in reparto else "NO, Y ESO SERIA DOCTRINA NUEVA"))
    if NUEVO not in reparto:
        w("   ROJO: no se estrena un valor de estado sin el fundador.")
        return cerrar(1)
    w("")

    w("LA CIRUGIA, SOBRE LA LINEA Y NO SOBRE EL JSON")
    par_viejo = '"estado": "%s"' % VIEJO
    par_nuevo = '"estado": "%s"' % NUEVO
    n_en_linea = linea0.count(par_viejo)
    w("   %r aparece %d vez(ces) EN SU LINEA (se exige 1)"
      % (par_viejo, n_en_linea))
    if n_en_linea != 1:
        w("   ROJO: no se toca lo que no se puede senalar sin ambiguedad.")
        return cerrar(1)
    linea1 = linea0.replace(par_viejo, par_nuevo, 1)
    w("   CIFRA bytes de la linea antes: %d | despues: %d | crecimiento: %d"
      % (len(linea0.encode("utf-8")), len(linea1.encode("utf-8")),
         len(linea1.encode("utf-8")) - len(linea0.encode("utf-8"))))
    d1 = json.loads(linea1)
    iguales = [k for k in d if k != "estado" and d[k] == d1.get(k)]
    w("   CIFRA campos de la ficha que NO se mueven: %d de %d"
      % (len(iguales), len(d) - 1))
    if len(iguales) != len(d) - 1:
        w("   ROJO: la cirugia movio algun campo que no era el estado.")
        return cerrar(1)
    w("   el campo estado pasa de %r a %r" % (d["estado"], d1["estado"]))
    w("")

    w("LA ESCRITURA")
    if a.escribir and d["estado"] == VIEJO:
        ls1 = list(ls0)
        ls1[LINEA - 1] = linea1
        io.open(OPS, "w", encoding="utf-8", newline=NL).write(NL.join(ls1))
        w("   ESCRITA: la linea %d y ninguna otra." % LINEA)
    elif a.escribir:
        w("   NO SE ESCRIBE: ya estaba. IDEMPOTENTE.")
    else:
        w("   MODO MEDICION: no se escribe nada.")
    w("")

    w("=" * 78)
    w("GUARDA (2), SEGUNDA MITAD: LA SEDE **DESPUES**, REMEDIDA Y NO HEREDADA")
    w("=" * 78)
    dd, lfd, sdd, sld, texto1 = dos_convenciones(OPS)
    w("   %s: %d bytes en disco y %d bytes normalizado a LF" % (RUTA_REL, dd, lfd))
    w("   sha256 disco %s y sha256 LF %s" % (sdd, sld))
    w("   CIFRA crecimiento: %d bytes en disco y %d bytes normalizado a LF"
      % (dd - d0, lfd - lf0))
    w("")

    w("GUARDA (3): UNA LINEA CAMBIADA Y NI UNA MAS, Y NINGUN OTRO id_op MOVIDO")
    c, ns = git(["diff", "--numstat", "--", RUTA_REL])
    filas = [l for l in ns.split(NL) if l.strip()]
    w("   git diff --numstat -- %s :" % RUTA_REL)
    for l in filas:
        w("      %s" % l)
    anad = borr = None
    if len(filas) == 1:
        partes = filas[0].split()
        anad, borr = int(partes[0]), int(partes[1])
    w("   CIFRA ficheros tocados: %d (se exige 1)" % len(filas))
    w("   CIFRA lineas anadidas: %s | CIFRA lineas borradas: %s" % (anad, borr))
    ok_ns = (len(filas) == 1 and anad == 1 and borr == 1)
    w("   UNA LINEA CAMBIADA Y NI UNA MAS: %s"
      % ("SI" if ok_ns else "NO, Y ESO ES PARADA: SE TRAE Y NO SE ARREGLA"))
    w("")
    censo1 = censo(texto1)
    w("   EL CENSO DE id_op Y estado, COTEJADO ENTERO CONTRA EL DE ANTES:")
    w("   CIFRA fichas antes: %d | CIFRA fichas despues: %d"
      % (len(censo0), len(censo1)))
    movidos = []
    if len(censo0) == len(censo1):
        for (i0, id0, e0), (i1, id1, e1) in zip(censo0, censo1):
            if id0 != id1 or e0 != e1:
                movidos.append((i0, id0, e0, i1, id1, e1))
    else:
        w("   ROJO: cambio el numero de fichas.")
    w("   CIFRA fichas que se movieron: %d (se espera 1, y que sea %s)"
      % (len(movidos), FICHA))
    for i0, id0, e0, i1, id1, e1 in movidos:
        w("      linea %d %s %r  ->  linea %d %s %r" % (i0, id0, e0, i1, id1, e1))
    solo_ella = (len(movidos) == 1 and movidos[0][1] == FICHA
                 and movidos[0][4] == FICHA and movidos[0][2] == VIEJO
                 and movidos[0][5] == NUEVO)
    w("   SE MOVIO SOLO %s Y SOLO SU estado: %s"
      % (FICHA, "SI" if solo_ella else "NO"))
    w("")
    w("   CIFRA otros id_op cuyo estado cambio: %d"
      % len([1 for m in movidos if m[1] != FICHA]))
    w("")
    reparto1 = {}
    for _i, _id, e in censo1:
        reparto1[e] = reparto1.get(e, 0) + 1
    w("   EL REPARTO DE estado, ANTES Y DESPUES:")
    for k in sorted(set(list(reparto) + list(reparto1))):
        w("      %-8r antes %d  despues %d" % (k, reparto.get(k, 0),
                                               reparto1.get(k, 0)))
    w("")
    veredicto = ok_ns and solo_ella
    w("VEREDICTO DE LAS TRES GUARDAS: %s"
      % ("VERDE, LAS TRES" if veredicto else "ROJO, Y SE PARA"))
    w("")
    w("FIN")
    return cerrar(0 if veredicto or not a.escribir else 1)


if __name__ == "__main__":
    raise SystemExit(main())
