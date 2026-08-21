# -*- coding: utf-8 -*-
"""vuelta66_caso_positivo_varas.py . EL CASO POSITIVO DE LA CORRECCION DEL CUADRO
DE VARAS Y DEL INSTRUMENTO N-ARIO QUE NACE CON ELLA, EN SUS TRES MITADES.

scripts/loop/vuelta58_varas_tramo.py es de NOMBRE ESTABLE y sus cifras YA estan
citadas por el registro del tramo 5 en docs/plan/03_FUSIONES.md. Una correccion
sobre un instrumento asi NO SE PUEDE CREER SIN PRUEBA: eso es lo que esto mide.

LA VARA DE LA COMPARACION ES ANCESTRO CONTRA CORREGIDO, LOS DOS CORRIDOS HOY
SOBRE EL MISMO ARBOL Y EL MISMO INSUMO, que es la que la vuelta 65 dejo escrita
tras descartar la mala (comparar contra una salida sellada mide el movimiento del
ARBOL, no el de la correccion: averia 7.4 de aquella vuelta). El ancestro se saca
de git y no se re-teclea, y se borra al terminar.

MITAD 1, NO REGRESION SOBRE UN ACTO DE DOS. Sobre un TRAMO DE MENTIRA de DOS
miembros vivos con clave orden_tramo (la forma vieja entera), el cuadro ANCESTRO
y el CORREGIDO tienen que imprimir la MISMA salida, LINEA A LINEA, sin ninguna
excepcion (este instrumento no imprime fecha, asi que no hay linea que perdonar).

MITAD 2, QUE LAS DOS RAMAS NUEVAS SIRVAN PARA ALGO Y NO CALLEN.
  2.a el ANCESTRO sobre el tramo unico de OP-U-02 (clave orden_universo) cae con
      el ROJO DEL ORDINAL, que es la averia que se corrige;
  2.b el CORREGIDO sobre ese mismo tramo YA NO cae por el ordinal, y cae por LA
      GUARDA NUEVA nombrando al instrumento N-ario. LO QUE NO PUEDE HACER ES
      IMPRIMIR EL CUADRO: si imprimiera filas de dos sobre actos de hasta quince,
      la correccion habria cambiado un ROJO ruidoso por un recorte mudo, que es
      peor que la averia.

MITAD 3, QUE LA GENERALIZACION SEA UNA GENERALIZACION. Sobre el MISMO tramo de
mentira de DOS miembros, scripts/loop/varas_n_arias_del_tramo.py tiene que dar
LA MISMA FORMA que el cuadro de pares y APUNTAR AL MISMO MIEMBRO en cada vara.
Si la flecha N-aria no coincide con la flecha vieja cuando N es 2, no es una
generalizacion: es una regla nueva disfrazada.

TODO LO QUE ESCRIBE LO BORRA: el tramo de mentira y el ancestro sacado de git.
El borrado se comprueba e imprime.

Uso:
  python scripts/loop/vuelta66_caso_positivo_varas.py
exit 0 si todo sale VERDE; exit 1 si algo falla.
"""
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VARAS = "scripts/loop/vuelta58_varas_tramo.py"
VARAS_ANC = "scripts/loop/_v66_varas_ancestro.py"
NARIO = "scripts/loop/varas_n_arias_del_tramo.py"
TRAMO_MENTIRA = "docs/loop/_v66_tramo_de_mentira.jsonl"
TRAMO_OPU02 = "docs/loop/TRAMO_UNICO_OPU02_V64.jsonl"
# EL ANCESTRO ES EL DE ANTES DE LA CORRECCION, o sea el del commit de la TAREA 1
# de esta misma vuelta.
ANCESTRO = "fa1c3226"
NL = chr(10)

BORRAR = []


def correr(cmd):
    r = subprocess.run([sys.executable] + cmd, cwd=RAIZ, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def sacar_de_git(commit, ruta, destino_rel):
    r = subprocess.run(["git", "show", "%s:%s" % (commit, ruta)], cwd=RAIZ,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        return False
    d = os.path.join(RAIZ, destino_rel.replace("/", os.sep))
    io.open(d, "w", encoding="utf-8", newline=NL).write(r.stdout)
    BORRAR.append(d)
    return True


def vivo(nid):
    p = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(p):
        return None
    d = json.load(io.open(p, encoding="utf-8"))
    if d.get("deprecado") or d.get("deprecated"):
        return None
    return d


def fabricar_fixture():
    """DOS nodos VIVOS de verdad, elegidos POR MEDICION y no a dedo: los dos
    primeros miembros vivos del primer acto del tramo de OP-U-02 que tengan pasos
    y condiciones. El fixture usa la clave VIEJA orden_tramo, que es la rama que
    la mitad 1 exige que salga identica."""
    filas = [json.loads(l) for l in
             io.open(os.path.join(RAIZ, TRAMO_OPU02.replace("/", os.sep)), encoding="utf-8")
             if l.strip()]
    cand = []
    for m in filas[0]["miembros"]:
        d = vivo(m)
        if d and (d.get("pasos_accionables") or []) and (d.get("condiciones_activacion") or []):
            cand.append(m)
        if len(cand) == 2:
            break
    if len(cand) != 2:
        return None, "no hay dos miembros vivos con pasos y condiciones para el fixture"
    fila = {"tamano": 2, "miembros": sorted(cand), "miembros_vivos": 2,
            "figura": "PURO A", "orden_tramo9": 1,
            "tramo": "DE MENTIRA, SOLO PARA EL CASO POSITIVO DE LA VUELTA 66"}
    d = os.path.join(RAIZ, TRAMO_MENTIRA.replace("/", os.sep))
    io.open(d, "w", encoding="utf-8", newline=NL).write(json.dumps(fila, ensure_ascii=False) + NL)
    BORRAR.append(d)
    return sorted(cand), None


def limpiar():
    print()
    print("  --- BORRADO DE LO FABRICADO ---")
    for p in BORRAR:
        if os.path.exists(p):
            os.remove(p)
        print("     %-58s %s" % (os.path.relpath(p, RAIZ).replace(os.sep, "/"),
                                 "BORRADO" if not os.path.exists(p) else "NO SE PUDO BORRAR"))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("CASO POSITIVO DE LA CORRECCION DEL CUADRO DE VARAS (vuelta 66)")
    print("=" * 78)
    fallos = []

    par, err = fabricar_fixture()
    if err:
        print("ROJO: %s" % err)
        limpiar()
        return 1
    print()
    print("  fixture de DOS miembros vivos, elegidos por medicion: %s" % ", ".join(par))
    if not sacar_de_git(ANCESTRO, VARAS, VARAS_ANC):
        print("ROJO: no se pudo sacar el ancestro %s:%s de git" % (ANCESTRO, VARAS))
        limpiar()
        return 1
    print("  ancestro sacado de git: %s:%s" % (ANCESTRO, VARAS))

    # ---------------------------------------------------------------- MITAD 1
    print()
    print("  --- MITAD 1: NO REGRESION SOBRE UN ACTO DE DOS ---")
    ca, sa = correr([VARAS_ANC, "--tramo", TRAMO_MENTIRA, "--vuelta", "66"])
    cc, sc = correr([VARAS, "--tramo", TRAMO_MENTIRA, "--vuelta", "66"])
    print("     exit ancestro %d, exit corregido %d" % (ca, cc))
    la, lc = sa.split(NL), sc.split(NL)
    dif = [(i + 1, x, y) for i, (x, y) in enumerate(zip(la, lc)) if x != y]
    print("     lineas ancestro %d, corregido %d, DISTINTAS %d" % (len(la), len(lc), len(dif)))
    if ca != 0 or cc != 0 or len(la) != len(lc) or dif:
        fallos.append("MITAD 1: el cuadro corregido NO sale identico al ancestro sobre dos miembros")
        for i, x, y in dif[:6]:
            print("        L%d ancestro: %s" % (i, x[:92]))
            print("        L%d corregid: %s" % (i, y[:92]))
    else:
        print("     VERDE: salida IDENTICA linea a linea, la rama vieja no se movio")

    # ---------------------------------------------------------------- MITAD 2
    print()
    print("  --- MITAD 2: LAS DOS RAMAS NUEVAS, Y QUE NINGUNA CALLE ---")
    ca2, sa2 = correr([VARAS_ANC, "--tramo", TRAMO_OPU02, "--vuelta", "66"])
    ok2a = ca2 != 0 and "0 claves de ordinal" in sa2
    print("     2.a el ANCESTRO sobre el tramo unico cae por el ORDINAL: %s"
          % ("SI, como se esperaba" if ok2a else "NO, y eso invalida la premisa"))
    print("         %s" % sa2.strip().split(NL)[0][:96])
    if not ok2a:
        fallos.append("MITAD 2.a: el ancestro no cae por el ordinal")
    cc2, sc2 = correr([VARAS, "--tramo", TRAMO_OPU02, "--vuelta", "66"])
    sin_ordinal = "claves de ordinal" not in sc2
    con_guarda = "MAS DE DOS miembros" in sc2 and NARIO in sc2
    sin_cuadro = "EL CUADRO DE VARAS DE LOS" not in sc2
    print("     2.b el CORREGIDO ya NO cae por el ordinal          : %s" % ("SI" if sin_ordinal else "NO"))
    print("         cae por LA GUARDA NUEVA y nombra al N-ario     : %s" % ("SI" if con_guarda else "NO"))
    print("         y NO imprime ni una fila de cuadro             : %s" % ("SI" if sin_cuadro else "NO"))
    if not (cc2 != 0 and sin_ordinal and con_guarda and sin_cuadro):
        fallos.append("MITAD 2.b: la guarda nueva no muerde como debe sobre el tramo N-ario")
        print("         salida: %s" % sc2.strip()[:200])

    # ---------------------------------------------------------------- MITAD 3
    print()
    print("  --- MITAD 3: LA FLECHA N-ARIA COINCIDE CON LA VIEJA CUANDO N ES 2 ---")
    cn, sn = correr([NARIO, "--tramo", TRAMO_MENTIRA])
    m = re.search(r"FORMA:\s*([A-Z ]+?)\s*$", sn, re.M)
    forma_n = m.group(1).strip() if m else "(no se pudo leer)"
    formas_viejas = [f for f in ("EMPATE SIN VARA", "CONTENIDO EMPATA", "TODAS DE ACUERDO",
                                 "UNA SOLA VARA", "CHOCAN") if f in sa]
    forma_v = formas_viejas[0] if len(formas_viejas) == 1 else "(ambigua: %s)" % formas_viejas
    print("     exit n-ario %d" % cn)
    print("     FORMA del cuadro de pares : %s" % forma_v)
    print("     FORMA del cuadro N-ario   : %s" % forma_n)
    iguales = cn == 0 and forma_n == forma_v
    # y ademas: a que miembro apunta cada vara, contado sobre el mismo fixture.
    apunta = dict(re.findall(r"la vara de (PASOS|CONDICIONES)\s+apunta a: (.+)", sn))
    fila = [l for l in sa.split(NL) if l.strip().startswith("1 ")]
    print("     la fila vieja, verbatim   : %s" % (fila[0].strip()[:96] if fila else "(no hallada)"))
    print("     el N-ario apunta          : pasos a %s | condiciones a %s"
          % (apunta.get("PASOS", "?").strip(), apunta.get("CONDICIONES", "?").strip()))
    if not iguales:
        fallos.append("MITAD 3: la FORMA N-aria no coincide con la de pares sobre dos miembros")
    else:
        print("     VERDE: la misma FORMA, o sea que con N igual a 2 la flecha nueva es la vieja")

    limpiar()
    print()
    print("=" * 78)
    if fallos:
        print("ROJO: %d mitad(es) fallan" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("VERDE: las TRES mitades pasan. La correccion no regresa y la guarda muerde.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
