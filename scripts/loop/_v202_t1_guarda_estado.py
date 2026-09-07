# -*- coding: utf-8 -*-
r"""_v202_t1_guarda_estado.py . LA GUARDA DE QUE NINGUN CAMPO `estado` SE MUEVE,
MEDIDA CONTRA `HEAD` (TAREA 1 de la vuelta 202).

ES LA MISMA GUARDA QUE LA VUELTA 201 CORRIO PARA `OP-I-01` EN SU TAREA 2, y el
encargo de esta vuelta la nombra asi: *"la misma que uso la 201"*. Aquella la
corrio suelta y sello solo su salida
(`docs/loop/SALIDA_V201_T2_GUARDA_ESTADO.txt`), sin dejar el codigo; aqui se
escribe con **PREFIJO DE GUION BAJO**, fuera del censo y fuera de la nomina, por
la adjudicacion `4.5` del acta 199: un computo de UNA vuelta que no vigila a
nadie NO ES MAQUINARIA, y la moratoria (`AUDITOR.md` 6.3) no lo prohibe.

POR QUE SE ESCRIBE EN VEZ DE CORRERSE SUELTA, Y LA RAZON ES UNA REGLA DE LA CASA
Y NO UNA PREFERENCIA: `EJECUTOR.md` 1, **EL CASO ROJO SE PRUEBA POR MUTACION**,
dice que *ningun assert, guarda o caso rojo se publica como prueba sin haber
corrido antes su prueba de mutacion*. Para poder mutarla hay que poder llamarla
con datos fabricados, y para eso el veredicto tiene que vivir en una **funcion
PURA** que reciba las lineas en vez de leer el disco. Eso es `veredicto()`.

LAS CINCO COMPROBACIONES, que son las cinco que el encargo enumera:

  1. exactamente **1 sola linea** de `OPERACIONES.jsonl` difiere respecto de
     `HEAD`, y es la de la ficha que se dice;
  2. de esa ficha cambia **1 sola clave**, y es `evidencia`;
  3. los elementos viejos de `evidencia` siguen **identicos y en su orden**;
  4. el `estado` de esa ficha **entra y sale igual**;
  5. **0 de las 71 fichas** mueven su campo `estado`.

USO:
  python scripts/loop/_v202_t1_guarda_estado.py
  python scripts/loop/_v202_t1_guarda_estado.py --sufijo _IDEM
  python scripts/loop/_v202_t1_guarda_estado.py --mutacion
"""
import argparse
import io
import json
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

OPERACIONES = "docs/plan/OPERACIONES.jsonl"
ID_OP = "OP-L-03"


def veredicto(head_lineas, arbol_lineas, id_op=ID_OP):
    """LAS CINCO COMPROBACIONES, EN UNA FUNCION PURA. Recibe las dos listas de
    lineas ya leidas y devuelve (ok, informe). NO TOCA EL DISCO: por eso se
    puede mutar."""
    inf = []
    w = inf.append
    ok = True
    hn = [x for x in head_lineas if x.strip()]
    an = [x for x in arbol_lineas if x.strip()]
    w("CIFRA lineas no vacias en HEAD: %d" % len(hn))
    w("CIFRA lineas no vacias en el arbol: %d" % len(an))
    if len(hn) != len(an):
        w("ROJO: el numero de fichas cambia, %d contra %d." % (len(hn), len(an)))
        ok = False
    dif = [i + 1 for i in range(min(len(hn), len(an))) if hn[i] != an[i]]
    w("CIFRA lineas que difieren: %d, cuales: %s" % (len(dif), dif))
    if len(dif) != 1:
        w("ROJO: se esperaba exactamente 1 linea distinta.")
        ok = False
    else:
        i = dif[0]
        dh, da = json.loads(hn[i - 1]), json.loads(an[i - 1])
        w("la linea %d es la ficha: %s en HEAD y %s en el arbol"
          % (i, dh.get("id_op"), da.get("id_op")))
        if dh.get("id_op") != id_op or da.get("id_op") != id_op:
            w("ROJO: la linea que cambia no es la de %s." % id_op)
            ok = False
        cam = sorted(k for k in set(list(dh) + list(da))
                     if dh.get(k) != da.get(k))
        w("CIFRA claves de esa ficha que cambian de valor: %d, cuales: %s"
          % (len(cam), cam))
        if cam != ["evidencia"]:
            w("ROJO: cambia alguna clave que no es `evidencia`.")
            ok = False
        w("estado de %s ANTES: %r | DESPUES: %r"
          % (id_op, dh.get("estado"), da.get("estado")))
        if dh.get("estado") != da.get("estado"):
            w("ROJO: el estado de la ficha se movio.")
            ok = False
        eh, ea = dh.get("evidencia", []), da.get("evidencia", [])
        w("CIFRA elementos de `evidencia` ANTES: %d | DESPUES: %d"
          % (len(eh), len(ea)))
        iguales = ea[:len(eh)] == eh
        w("los %d viejos siguen identicos y en su orden: %s" % (len(eh), iguales))
        if not iguales:
            w("ROJO: los elementos viejos no siguen identicos y en su orden.")
            ok = False
    movidas = []
    for a, b in zip(hn, an):
        da_, db_ = json.loads(a), json.loads(b)
        if da_.get("estado") != db_.get("estado"):
            movidas.append(da_.get("id_op"))
    w("CIFRA fichas de las %d cuyo campo `estado` cambia: %d, cuales: %s"
      % (len(hn), len(movidas), ", ".join(str(x) for x in movidas) or "(ninguna)"))
    if movidas:
        ok = False
    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    return ok, inf


def lineas_de_head():
    r = subprocess.run(["git", "show", "HEAD:" + OPERACIONES], cwd=RAIZ,
                       capture_output=True)
    return r.stdout.decode("utf-8").replace(chr(13) + NL, NL).split(NL)


def lineas_del_arbol():
    crudo = io.open(os.path.join(RAIZ, OPERACIONES.replace("/", os.sep)),
                    "rb").read()
    return crudo.replace(b"\r\n", b"\n").decode("utf-8").split(NL)


def casos_de_mutacion(head_lineas, arbol_lineas):
    """LOS CASOS ROJOS, FABRICADOS MUTANDO EL ARBOL Y NUNCA EL REPO. Devuelve
    una lista de (nombre, head, arbol) que TIENEN QUE dar ROJO."""
    hn = [x for x in head_lineas if x.strip()]
    an = [x for x in arbol_lineas if x.strip()]
    casos = []

    # A) DOS LINEAS DIFIEREN en vez de una: se toca una segunda ficha.
    m = list(an)
    otra = 0 if json.loads(an[0]).get("id_op") != ID_OP else 1
    d = json.loads(m[otra])
    d["nota"] = str(d.get("nota") or "") + " MUTACION"
    m[otra] = json.dumps(d, ensure_ascii=False)
    casos.append(("A) dos lineas difieren en vez de una", hn, m))

    # B) CAMBIA UNA CLAVE QUE NO ES `evidencia` en la ficha del sujeto.
    m = list(an)
    i = [k for k, x in enumerate(an) if json.loads(x).get("id_op") == ID_OP][0]
    d = json.loads(m[i])
    d["orden"] = (d.get("orden") or 0) + 1
    m[i] = json.dumps(d, ensure_ascii=False)
    casos.append(("B) cambia una clave que no es `evidencia`", hn, m))

    # C) EL `estado` DE LA FICHA SE MUEVE.
    m = list(an)
    d = json.loads(m[i])
    d["estado"] = "HECHA"
    m[i] = json.dumps(d, ensure_ascii=False)
    casos.append(("C) el estado de la ficha del sujeto se mueve", hn, m))

    # D) EL `estado` DE OTRA FICHA SE MUEVE.
    m = list(an)
    d = json.loads(m[otra])
    d["estado"] = "HECHA"
    m[otra] = json.dumps(d, ensure_ascii=False)
    casos.append(("D) el estado de OTRA ficha se mueve", hn, m))

    # E) UN ELEMENTO VIEJO DE `evidencia` SE REESCRIBE en vez de anadirse.
    m = list(an)
    d = json.loads(m[i])
    ev = list(d.get("evidencia", []))
    if ev:
        ev[0] = "REESCRITO"
        d["evidencia"] = ev
        m[i] = json.dumps(d, ensure_ascii=False)
    casos.append(("E) un elemento viejo de `evidencia` se reescribe", hn, m))

    # F) NINGUNA LINEA DIFIERE: la correccion no se escribio.
    casos.append(("F) ninguna linea difiere", hn, list(hn)))

    return casos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sufijo", default="")
    ap.add_argument("--mutacion", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    head, arbol = lineas_de_head(), lineas_del_arbol()

    if a.mutacion:
        L = []
        w = L.append
        w("PRUEBA DE MUTACION DE LA GUARDA DE LA VUELTA 202, TAREA 1")
        w("=" * 70)
        w("EJECUTOR.md 1: EL CASO ROJO SE PRUEBA POR MUTACION. Ninguna guarda se")
        w("publica como prueba sin haber corrido antes su prueba de mutacion.")
        w("EL REPO NO SE TOCA: los casos se fabrican MUTANDO LAS LINEAS EN")
        w("MEMORIA y llamando a la funcion PURA veredicto().")
        w("")
        ok_real, inf_real = veredicto(head, arbol)
        w("CASO DE CONTROL (el arbol de verdad): %s"
          % ("VERDE" if ok_real else "ROJO"))
        for l in inf_real:
            w("   " + l)
        w("")
        casos = casos_de_mutacion(head, arbol)
        caen = 0
        for nombre, h, m in casos:
            ok, inf = veredicto(h, m)
            w("%-50s %s" % (nombre, "CAE EN ROJO" if not ok else "NO CAE"))
            for l in inf:
                if l.startswith("ROJO") or l.startswith("VEREDICTO"):
                    w("      " + l)
            if not ok:
                caen += 1
        w("")
        # LAS DOS FORMAS CANONICAS QUE `cerrar_reporte.py` SABE COTEJAR
        # (`cifra_propia_del_arnes`). Se escriben para que la prosa del reporte
        # que cite este fichero SE PUEDA CONTAR CONTRA EL en vez de quedar
        # SIN COTEJO, que es lo que la escalada de AUDITOR.md 1.2 vino a evitar.
        w("CIFRA casos: %d | pasan: %d" % (len(casos), caen))
        w("CIFRA casos que CAEN: %d de %d" % (caen, len(casos)))
        w("CIFRA casos de mutacion: %d | CIFRA que CAEN EN ROJO: %d"
          % (len(casos), caen))
        w("CIFRA casos de control que quedan VERDES: %d de 1" % (1 if ok_real else 0))
        w("VEREDICTO DE LA MUTACION: %s"
          % ("VERDE, la guarda muerde" if (caen == len(casos) and ok_real)
             else "ROJO, la guarda NO muerde en algun caso"))
        salida = NL.join(L) + NL
        print(salida)
        io.open(os.path.join(LOOP, "SALIDA_V202_T1_MUTACION_GUARDA.txt"), "w",
                encoding="utf-8", newline=NL).write(salida)
        return 0 if caen == len(casos) and ok_real else 1

    ok, inf = veredicto(head, arbol)
    L = ["GUARDA DE LA VUELTA 202, TAREA 1: NINGUN `estado` SE MUEVE",
         "=" * 70,
         "corrida: %s" % ("SEGUNDA" if a.sufijo else "PRIMERA"),
         "medida contra HEAD con git show HEAD:%s" % OPERACIONES] + inf
    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V202_T1_GUARDA_ESTADO%s.txt" % a.sufijo),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
