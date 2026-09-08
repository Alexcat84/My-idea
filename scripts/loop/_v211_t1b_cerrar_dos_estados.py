# -*- coding: utf-8 -*-
r"""_v211_t1b_cerrar_dos_estados.py . TAREA 1.b DE LA VUELTA 211: SE PONEN
`OP-L-02` Y `OP-L-03` EN `HECHA`, LAS DOS **EN EL MISMO COMPUTO**, TOCANDO
**SOLO** SU CAMPO `estado`.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3). Muere con la vuelta y no vigila nada.

**IMPORTAR NO ES CLONAR** (acta 206 `6.5`). `git`, `dos_convenciones` y `censo`
se **IMPORTAN** de `_v209_t2c_cerrar_opl01.py`, que es el fichero que la vuelta
209 corrio para `OP-L-01` y cuyo resultado el acta 209 reprodujo al digito. Aqui
no se copia ni una linea de esas tres funciones. Lo que cambia es **la lista de
fichas**, que pasa de una a dos, y el barrido del `numstat`, que el encargo pide
sobre `docs/plan/` entero y no sobre el solo fichero.

**LAS TRES GUARDAS SON LAS DEL `2.c` DE LA 209** (linea **73763** de
`docs/loop/ACTA_AUDITOR.md`: *"el pase se ejecuta con las mismas tres guardas del
`2.c` de esta vuelta, que salieron limpias"*), leidas del encargo de la 211:

  (1) LA SEDE POR LAS DOS CONVENCIONES **AL ENTRAR Y AL SALIR**, con sus dos
      `sha256`, y el valor viejo leido y publicado al lado del nuevo.
  (2) SOLO CAMBIAN ESOS DOS CAMPOS: las fichas contadas por `estado` ANTES y
      DESPUES, las dos cuentas publicadas, y `git diff --numstat` sobre
      `docs/plan/` con su CIFRA de filas.
  (3) EL CASO POSITIVO: el `jsonl` se **recarga linea a linea** y su CIFRA de
      fichas tiene que seguir siendo la misma de antes.

**LA CIRUGIA ES DE TEXTO, NO DE JSON**, por el mismo motivo que escribio la 209:
re-serializar reordenaria claves y ensuciaria el `numstat` de las demas lineas,
que es justo lo que la guarda (2) mide.

**EL CASO ROJO SE PRUEBA POR MUTACION** (`EJECUTOR.md` 1). `--mutar` corre el
mismo computo en modo medicion con **el nombre de una ficha cambiado**, y exige
que el veredicto **CAIGA**. Si sale verde con el dato mutado, la guarda no
comprueba nada y este fichero lo dice en rojo.

USO:  python scripts/loop/_v211_t1b_cerrar_dos_estados.py            (medicion)
      python scripts/loop/_v211_t1b_cerrar_dos_estados.py --mutar    (caso rojo)
      python scripts/loop/_v211_t1b_cerrar_dos_estados.py --escribir
"""
import argparse
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

from _v209_t2c_cerrar_opl01 import git, dos_convenciones, censo  # noqa: E402

OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
RUTA_REL = "docs/plan/OPERACIONES.jsonl"
SEDE_NUMSTAT = "docs/plan/"
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

# LAS DOS FICHAS, CON SU LINEA LEIDA DEL FICHERO Y NO CREIDA: la linea que va
# aqui es CONTRASTE, y el computo cae si el id_op de esa linea no es el que se
# nombra. (adjudicacion 6.4 del acta 209, linea 73760; adjudicacion 6.5, 73765)
FICHAS = [("OP-L-02", 42), ("OP-L-03", 43)]
VIEJO = "LISTA"
NUEVO = "HECHA"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    ap.add_argument("--mutar", action="store_true")
    ap.add_argument("--salida", default="T1B_CERRAR_DOS_ESTADOS")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    fichas = list(FICHAS)
    if a.mutar:
        fichas[1] = ("OP-L-99", FICHAS[1][1])

    L = []
    w = L.append

    def cerrar(codigo):
        """CIERRA POR CUALQUIER CAMINO, Y EN MODO MUTACION DA LA VUELTA AL
        VEREDICTO. Sin esto, un rojo TEMPRANO (que es justo el que la mutacion
        busca) saldria del computo sin publicar su propia prueba y devolviendo
        exitcode 1, o sea leyendose como fallo cuando es el exito de la guarda.
        Correccion declarada dentro de la propia vuelta 211."""
        if a.mutar:
            L.append("")
            L.append("LO QUE LA MUTACION EXIGE: que el veredicto de este computo")
            L.append("sea ROJO, o sea que este cierre traiga codigo distinto de 0.")
            L.append("CODIGO CON EL QUE EL COMPUTO IBA A CERRAR: %d" % codigo)
            L.append("VEREDICTO DE LA PRUEBA DE MUTACION: %s"
                     % ("VERDE, LA GUARDA MUERDE" if codigo != 0
                        else "ROJO, LA GUARDA NO COMPRUEBA NADA"))
            codigo = 0 if codigo != 0 else 1
        salida = NL.join(L) + NL
        print(salida)
        nombre = a.salida + ("_MUTADO" if a.mutar else "")
        io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, nombre)),
                "w", encoding="utf-8", newline=NL).write(salida)
        return codigo

    w("=" * 78)
    w("VUELTA %d, TAREA 1.b: %s Y %s PASAN A %s, LAS DOS EN EL MISMO COMPUTO"
      % (VUELTA, FICHAS[0][0], FICHAS[1][0], NUEVO))
    if a.mutar:
        w("*** CORRIDA MUTADA. El dato %r se cambio por %r a proposito."
          % (FICHAS[1][0], fichas[1][0]))
        w("*** SE EXIGE QUE EL VEREDICTO CAIGA. Un verde aqui prueba que la")
        w("*** guarda no comprueba nada.")
    w("=" * 78)
    w("")

    w("GUARDA (1), PRIMERA MITAD: LA SEDE **AL ENTRAR**, POR LAS DOS CONVENCIONES")
    d0, lf0, sd0, sl0, texto0 = dos_convenciones(OPS)
    w("   %s: %d bytes en disco y %d bytes normalizado a LF" % (RUTA_REL, d0, lf0))
    w("   sha256 disco %s y sha256 LF %s" % (sd0, sl0))
    w("   LAS DOS CONVENCIONES %s en este fichero"
      % ("COINCIDEN" if d0 == lf0 else "NO COINCIDEN"))
    censo0 = censo(texto0)
    w("   CIFRA fichas en el fichero AL ENTRAR: %d" % len(censo0))
    w("")

    w("GUARDA (1), SEGUNDA MITAD: EL VALOR VIEJO DE CADA FICHA, LEIDO Y NO SUPUESTO")
    ls0 = texto0.split(NL)
    rojo = False
    lineas_objetivo = []
    for nombre, linea in fichas:
        if linea > len(ls0):
            w("   ROJO: el fichero no llega a la linea %d." % linea)
            rojo = True
            continue
        cruda = ls0[linea - 1]
        d = json.loads(cruda)
        w("   linea %d, id_op leido del fichero: %s" % (linea, d["id_op"]))
        w("      la ficha que se nombra es %s: %s"
          % (nombre, "SI" if d["id_op"] == nombre else "NO, Y ESO ES ROJO"))
        if d["id_op"] != nombre:
            rojo = True
            continue
        w("      CIFRA campos de la ficha: %d" % len(d))
        w("      VALOR VIEJO del campo estado, leido: %r" % d.get("estado"))
        w("      VALOR NUEVO que se va a escribir:    %r" % NUEVO)
        if d.get("estado") != VIEJO:
            w("      ROJO: el valor viejo no es %r." % VIEJO)
            rojo = True
            continue
        lineas_objetivo.append((nombre, linea, cruda, d))
    w("   CIFRA fichas que pasan la guarda (1): %d de %d"
      % (len(lineas_objetivo), len(fichas)))
    w("")
    if rojo:
        w("VEREDICTO: ROJO. No se escribe nada.")
        w("")
        w("FIN")
        return cerrar(1)

    w("EL VALOR NUEVO NO SE INVENTA: YA ES VOCABULARIO DE LA SEDE")
    reparto0 = {}
    for _i, _id, e in censo0:
        reparto0[e] = reparto0.get(e, 0) + 1
    for k in sorted(reparto0):
        w("   estado %-8r lo llevan %d fichas AL ENTRAR" % (k, reparto0[k]))
    w("   %r ya existe en el fichero: %s"
      % (NUEVO, "SI" if NUEVO in reparto0 else "NO, Y ESO SERIA DOCTRINA NUEVA"))
    if NUEVO not in reparto0:
        w("   ROJO: no se estrena un valor de estado sin el fundador.")
        return cerrar(1)
    w("")

    w("LA CIRUGIA, SOBRE CADA LINEA Y NO SOBRE EL JSON")
    par_viejo = '"estado": "%s"' % VIEJO
    par_nuevo = '"estado": "%s"' % NUEVO
    nuevas = {}
    for nombre, linea, cruda, d in lineas_objetivo:
        n_en_linea = cruda.count(par_viejo)
        w("   %s, linea %d: %r aparece %d vez(ces) EN SU LINEA (se exige 1)"
          % (nombre, linea, par_viejo, n_en_linea))
        if n_en_linea != 1:
            w("      ROJO: no se toca lo que no se puede senalar sin ambiguedad.")
            return cerrar(1)
        nueva = cruda.replace(par_viejo, par_nuevo, 1)
        d1 = json.loads(nueva)
        iguales = [k for k in d if k != "estado" and d[k] == d1.get(k)]
        w("      CIFRA bytes de la linea antes: %d | despues: %d | crecimiento: %d"
          % (len(cruda.encode("utf-8")), len(nueva.encode("utf-8")),
             len(nueva.encode("utf-8")) - len(cruda.encode("utf-8"))))
        w("      CIFRA campos que NO se mueven: %d de %d"
          % (len(iguales), len(d) - 1))
        if len(iguales) != len(d) - 1:
            w("      ROJO: la cirugia movio algun campo que no era el estado.")
            return cerrar(1)
        w("      el campo estado pasa de %r a %r" % (d["estado"], d1["estado"]))
        nuevas[linea] = nueva
    w("")

    w("LA ESCRITURA, UNA SOLA VEZ Y CON LAS DOS LINEAS A LA VEZ")
    if a.escribir:
        ls1 = list(ls0)
        for linea, nueva in nuevas.items():
            ls1[linea - 1] = nueva
        io.open(OPS, "w", encoding="utf-8", newline=NL).write(NL.join(ls1))
        w("   ESCRITAS: las lineas %s y ninguna otra."
          % ", ".join(str(x) for x in sorted(nuevas)))
    else:
        w("   MODO MEDICION: no se escribe nada.")
    w("")

    w("=" * 78)
    w("GUARDA (1), AL SALIR: LA SEDE REMEDIDA Y NO HEREDADA")
    w("=" * 78)
    dd, lfd, sdd, sld, texto1 = dos_convenciones(OPS)
    w("   %s: %d bytes en disco y %d bytes normalizado a LF" % (RUTA_REL, dd, lfd))
    w("   sha256 disco %s y sha256 LF %s" % (sdd, sld))
    w("   LAS DOS CONVENCIONES %s en este fichero"
      % ("COINCIDEN" if dd == lfd else "NO COINCIDEN"))
    w("   CIFRA crecimiento: %d bytes en disco y %d bytes normalizado a LF"
      % (dd - d0, lfd - lf0))
    w("   el sha256 CAMBIO: %s (es lo que prueba que algo se escribio)"
      % ("SI" if sdd != sd0 else "NO"))
    w("")

    w("GUARDA (2): SOLO CAMBIAN ESOS DOS CAMPOS")
    c, ns = git(["diff", "--numstat", "--", SEDE_NUMSTAT])
    filas = [l for l in ns.split(NL) if l.strip()]
    w("   git diff --numstat -- %s :" % SEDE_NUMSTAT)
    for l in filas:
        w("      %s" % l)
    w("   CIFRA filas de git diff --numstat sobre %s: %d" % (SEDE_NUMSTAT, len(filas)))
    esperado = 1 if a.escribir else 0
    w("   CIFRA filas que se esperan en este modo: %d" % esperado)
    ok_ns = (len(filas) == esperado)
    if a.escribir and len(filas) == 1:
        partes = filas[0].split()
        anad, borr = int(partes[0]), int(partes[1])
        w("   CIFRA lineas anadidas: %d | CIFRA lineas borradas: %d" % (anad, borr))
        w("   DOS LINEAS CAMBIADAS Y NI UNA MAS: %s"
          % ("SI" if (anad == 2 and borr == 2) else "NO, Y ESO ES PARADA"))
        ok_ns = ok_ns and anad == 2 and borr == 2
    w("")

    censo1 = censo(texto1)
    w("   LAS DOS CUENTAS POR estado, ANTES Y DESPUES, LAS DOS PUBLICADAS:")
    reparto1 = {}
    for _i, _id, e in censo1:
        reparto1[e] = reparto1.get(e, 0) + 1
    for k in sorted(set(list(reparto0) + list(reparto1))):
        w("      %-8r  ANTES %d   DESPUES %d" % (k, reparto0.get(k, 0),
                                                 reparto1.get(k, 0)))
    w("      TOTAL     ANTES %d   DESPUES %d"
      % (sum(reparto0.values()), sum(reparto1.values())))
    w("")

    w("   EL CENSO DE id_op Y estado, COTEJADO ENTERO CONTRA EL DE ANTES:")
    movidos = []
    if len(censo0) == len(censo1):
        for (i0, id0, e0), (i1, id1, e1) in zip(censo0, censo1):
            if id0 != id1 or e0 != e1:
                movidos.append((i0, id0, e0, i1, id1, e1))
    else:
        w("      ROJO: cambio el numero de fichas.")
    nombres = [n for n, _ in fichas]
    w("   CIFRA fichas que se movieron: %d (se esperan %d en este modo)"
      % (len(movidos), len(nombres) if a.escribir else 0))
    for i0, id0, e0, i1, id1, e1 in movidos:
        w("      linea %d %s %r  ->  linea %d %s %r" % (i0, id0, e0, i1, id1, e1))
    if a.escribir:
        solo_ellas = (len(movidos) == len(nombres)
                      and sorted(m[1] for m in movidos) == sorted(nombres)
                      and all(m[2] == VIEJO and m[5] == NUEVO for m in movidos))
    else:
        solo_ellas = (len(movidos) == 0)
    w("   SE MOVIERON SOLO ESAS FICHAS Y SOLO SU estado: %s"
      % ("SI" if solo_ellas else "NO"))
    w("   CIFRA otros id_op cuyo estado cambio: %d"
      % len([1 for m in movidos if m[1] not in nombres]))
    w("")

    w("GUARDA (3), EL CASO POSITIVO: EL jsonl SE RECARGA LINEA A LINEA")
    crudo = io.open(OPS, "rb").read().replace(b"\r\n", b"\n").decode("utf-8")
    leidas = 0
    malas = 0
    for i, l in enumerate(crudo.split(NL), 1):
        if not l.strip():
            continue
        try:
            json.loads(l)
            leidas += 1
        except ValueError:
            malas += 1
            w("      ROJO: la linea %d ya no es JSON valido." % i)
    w("   CIFRA fichas releidas del disco: %d" % leidas)
    w("   CIFRA fichas AL ENTRAR (la que tiene que repetirse): %d" % len(censo0))
    w("   CIFRA lineas que no son JSON valido: %d (se exige 0)" % malas)
    ok_recarga = (leidas == len(censo0) and malas == 0)
    w("   LA LECTURA DEL FICHERO SIGUE SIENDO VALIDA: %s"
      % ("SI" if ok_recarga else "NO"))
    w("")

    veredicto = ok_ns and solo_ellas and ok_recarga
    w("VEREDICTO DE LAS TRES GUARDAS: %s"
      % ("VERDE, LAS TRES" if veredicto else "ROJO, Y SE PARA"))
    w("")
    w("FIN")
    return cerrar(0 if veredicto else 1)


if __name__ == "__main__":
    raise SystemExit(main())
