# -*- coding: utf-8 -*-
"""vuelta65_caso_positivo_generador.py . EL CASO POSITIVO DE LA CORRECCION DEL
GENERADOR Y DEL DOSSIER, EN SUS TRES MITADES.

Los dos instrumentos son de NOMBRE ESTABLE y los dos se corrigieron en la vuelta
65 por CORRECCION DECLARADA (cambios 6 y 7 del docstring del generador, y la
nota fechada dentro del dossier). Una correccion sobre un instrumento estable que
ya sello planes NO SE PUEDE CREER SIN PRUEBA: eso es lo que esto mide.

LA VARA DE LA COMPARACION, Y POR QUE NO ES CONTRA LAS SALIDAS SELLADAS. El primer
intento de este mismo instrumento comparo contra los planes y el dossier sellados
en las vueltas 61 y 62, y dio ROJO: 808 lineas distintas y dos re-generaciones
imposibles. LA CAUSA ESTA MEDIDA Y NO SUPUESTA, y no es la correccion: los nodos
del tramo 6 de OP-U-01 SE FUNDIERON en la vuelta 62 y hoy estan deprecados y con
otro texto. Comparar contra una salida sellada mide el movimiento del ARBOL, no
el de la correccion. LA COMPARACION QUE SI AISLA LA CORRECCION es ANCESTRO CONTRA
CORREGIDO, LOS DOS CORRIDOS HOY SOBRE EL MISMO ARBOL Y EL MISMO INSUMO, y es la
que queda. El ancestro se saca de git (no se re-teclea) y se borra al terminar.

MITAD 1, NO REGRESION DEL GENERADOR. Sobre un TRAMO DE MENTIRA de DOS miembros
vivos con clave orden_tramo (la forma vieja entera), el generador ANCESTRO y el
CORREGIDO tienen que sellar el MISMO plan, campo a campo. La unica diferencia
admitida es el campo fecha, que el generador mide del reloj.

MITAD 2, NO REGRESION DEL DOSSIER. Sobre ese mismo tramo de mentira, el dossier
ANCESTRO y el CORREGIDO tienen que imprimir la MISMA salida, linea a linea.

MITAD 3, QUE LA CORRECCION SIRVA PARA ALGO. Las dos ramas nuevas se corren sobre
el tramo unico de OP-U-02 (clave orden_universo, actos de 3 a 15) y tienen que
DEJAR DE CAER EN ROJO por el ordinal, que es lo que hacian antes.

TODO LO QUE ESCRIBE LO BORRA: el tramo de mentira, su modulo de contenido, los
dos ancestros sacados de git y los dos planes re-generados. El borrado se
comprueba e imprime.

Uso:
  python scripts/loop/vuelta65_caso_positivo_generador.py
exit 0 si todo sale VERDE; exit 1 si algo falla.
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AQUI = os.path.dirname(os.path.abspath(__file__))
LOOP = os.path.join(RAIZ, "docs", "loop")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GEN = "scripts/loop/generar_plan_del_lote.py"
DOS = "scripts/loop/dossier_del_tramo.py"
GEN_ANC = "scripts/loop/_v65_generador_ancestro.py"
DOS_ANC = "scripts/loop/_v65_dossier_ancestro.py"
# EL ANCESTRO ES EL DE ANTES DE LA CORRECCION, o sea el del commit de la TAREA 1.
ANCESTRO = "ae539bb5"
TRAMO_MENTIRA = "docs/loop/_v65_tramo_de_mentira.jsonl"
CONTENIDO_MENTIRA = "_v65_fixture_lote"
TRAMO_OPU02 = "docs/loop/TRAMO_UNICO_OPU02_V64.jsonl"
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
    """DOS nodos VIVOS de verdad, elegidos por medicion y no a dedo: los dos
    primeros miembros vivos del acto 1 del tramo de OP-U-02 que tengan pasos y
    condiciones, con el superviviente elegido por tener MAS pasos."""
    filas = [json.loads(l) for l in
             io.open(os.path.join(RAIZ, TRAMO_OPU02.replace("/", os.sep)), encoding="utf-8")
             if l.strip()]
    cand = []
    for m in filas[0]["miembros"]:
        d = vivo(m)
        if d and (d.get("pasos_accionables") or []) and (d.get("condiciones_activacion") or []):
            cand.append((m, d))
        if len(cand) == 2:
            break
    if len(cand) != 2:
        return None, "no hay dos miembros vivos con pasos y condiciones para el fixture"
    cand.sort(key=lambda x: -len(x[1].get("pasos_accionables") or []))
    (sup, ds), (ab, da) = cand
    fila = {"tamano": 2, "miembros": sorted([sup, ab]),
            "miembros_vivos": 2, "figura": "PURO A", "orden_tramo9": 1,
            "tramo": "DE MENTIRA, SOLO PARA EL CASO POSITIVO DE LA VUELTA 65"}
    io.open(os.path.join(RAIZ, TRAMO_MENTIRA.replace("/", os.sep)), "w",
            encoding="utf-8", newline=NL).write(json.dumps(fila, ensure_ascii=False) + NL)
    BORRAR.append(os.path.join(RAIZ, TRAMO_MENTIRA.replace("/", os.sep)))

    # TODAS las piezas del absorbido van CUBIERTO al indice 1, que es la marca
    # mas simple y la que no depende del texto: aqui se prueba la MAQUINA, no el
    # criterio editorial.
    pasos = {str(i): ("CUBIERTO", 1) for i in range(1, len(da.get("pasos_accionables") or []) + 1)}
    conds = {str(i): ("CUBIERTO", 1) for i in range(1, len(da.get("condiciones_activacion") or []) + 1)}
    cuerpo = (
        "# -*- coding: utf-8 -*-" + NL +
        '"""Modulo de contenido DE MENTIRA del caso positivo de la vuelta 65. Se borra."""' + NL +
        "LOTE_A = {" + NL +
        "    'titulo': 'LOTE DE MENTIRA DEL CASO POSITIVO'," + NL +
        "    'actos': [{" + NL +
        "        'orden': 1," + NL +
        "        'superviviente': %r," % sup + NL +
        "        'motivo': 'MOTIVO DE MENTIRA, no adjudica nada y no se sella en ningun plan real.'," + NL +
        "        'nota': 'NOTA DE MENTIRA.'," + NL +
        "        'pasos': %r," % pasos + NL +
        "        'condiciones': %r," % conds + NL +
        "        'perdidas': []," + NL +
        "    }]," + NL +
        "    'declarados': []," + NL +
        "}" + NL)
    d = os.path.join(AQUI, CONTENIDO_MENTIRA + ".py")
    io.open(d, "w", encoding="utf-8", newline=NL).write(cuerpo)
    BORRAR.append(d)
    return (sup, ab), None


def mitad1(sup, ab):
    print()
    print("=" * 78)
    print("MITAD 1: NO REGRESION DEL GENERADOR. Ancestro contra corregido, los dos")
    print("HOY, sobre el mismo tramo de dos miembros vivos y el mismo contenido.")
    print("=" * 78)
    fallos = []
    planes = {}
    for etq, script, prefijo in (("ANCESTRO", GEN_ANC, "_V65_ANC_LOTE_"),
                                 ("CORREGIDO", GEN, "_V65_COR_LOTE_")):
        cod, salida = correr([script, "--lote", "A", "--vuelta", "65",
                              "--operacion", "OP-U-01", "--tramo", TRAMO_MENTIRA,
                              "--contenido", CONTENIDO_MENTIRA, "--prefijo", prefijo])
        destino = os.path.join(LOOP, "%sA.json" % prefijo)
        print("     %-10s exit %d | plan escrito: %s" % (etq, cod, os.path.exists(destino)))
        if cod != 0 or not os.path.exists(destino):
            fallos.append("%s: no sello plan (exit %d)" % (etq, cod))
            for l in salida.split(NL)[-10:]:
                print("        | %s" % l[:110])
            continue
        BORRAR.append(destino)
        planes[etq] = json.load(io.open(destino, encoding="utf-8"))
    if len(planes) != 2:
        return fallos
    v, n = planes["ANCESTRO"], planes["CORREGIDO"]
    difs = [k for k in sorted(set(v) | set(n)) if k != "fecha" and v.get(k) != n.get(k)]
    print()
    print("     campos de la raiz comparados : %d" % len(set(v) | set(n)))
    print("     actos                        : ancestro %d, corregido %d"
          % (len(v.get("actos", [])), len(n.get("actos", []))))
    print("     el acto sellado por los dos  : superviviente %s, absorbidos %s"
          % (n["actos"][0]["superviviente"], n["actos"][0]["absorbidos"]))
    print("     marcas de pasos, ancestro    : %s" % v["actos"][0]["pasos"])
    print("     marcas de pasos, corregido   : %s" % n["actos"][0]["pasos"])
    print("     campos DISTINTOS (sin fecha) : %d %s" % (len(difs), difs))
    if difs:
        fallos.append("el plan del ancestro y el del corregido difieren en %s" % difs)
    else:
        print("     IDENTICOS EN TODO MENOS LA FECHA: LA FORMA VIEJA NO SE MOVIO")
    return fallos


def mitad2():
    print()
    print("=" * 78)
    print("MITAD 2: NO REGRESION DEL DOSSIER. Ancestro contra corregido, los dos HOY.")
    print("=" * 78)
    fallos = []
    sal = {}
    for etq, script in (("ANCESTRO", DOS_ANC), ("CORREGIDO", DOS)):
        cod, s = correr([script, "--tramo", TRAMO_MENTIRA])
        print("     %-10s exit %d | %d lineas por count(NL), que calza con wc -l, y %d por len(split(NL))"
              % (etq, cod, s.count(NL), len(s.split(NL))))
        sal[etq] = [l.rstrip() for l in s.split(NL)]
        if cod != 0:
            fallos.append("%s: el dossier salio con exit %d" % (etq, cod))
    a, b = sal.get("CORREGIDO", []), sal.get("ANCESTRO", [])
    distintas = [i for i in range(max(len(a), len(b)))
                 if (a[i] if i < len(a) else None) != (b[i] if i < len(b) else None)]
    print("     lineas DISTINTAS: %d" % len(distintas))
    for i in distintas[:6]:
        print("        linea %d" % (i + 1))
        print("           ancestro : %s" % (b[i][:100] if i < len(b) else "(no existe)"))
        print("           corregido: %s" % (a[i][:100] if i < len(a) else "(no existe)"))
    if distintas:
        fallos.append("el dossier difiere en %d lineas sobre la forma vieja" % len(distintas))
    else:
        print("     IDENTICO AL DIGITO: LA RAMA DEL ACTO DE DOS NO SE MOVIO")
    return fallos


def mitad3():
    print()
    print("=" * 78)
    print("MITAD 3: QUE LA CORRECCION SIRVA. Las ramas nuevas sobre el tramo unico")
    print("de OP-U-02 (clave orden_universo, actos de 3 a 15).")
    print("=" * 78)
    fallos = []
    for etq, script, extra in (("DOSSIER", DOS, ["--actos", "1"]),
                               ("GENERADOR", GEN, ["--lote", "A", "--vuelta", "65",
                                                   "--operacion", "OP-U-02",
                                                   "--contenido", CONTENIDO_MENTIRA,
                                                   "--simular"])):
        print()
        print("  --- el %s, que ANTES caia en ROJO por la clave del ordinal ---" % etq.lower())
        cod, s = correr([script, "--tramo", TRAMO_OPU02] + extra)
        para = "claves de ordinal" in s
        print("     exit %d | sigue cayendo por el ordinal: %s" % (cod, para))
        if para:
            fallos.append("el %s sigue cayendo en ROJO por el ordinal" % etq.lower())
            continue
        for l in [x for x in s.split(NL) if x.strip()][:6]:
            print("     | %s" % l[:110])
        # Y LA GUARDA NUEVA DEL ACTO DE MAS DE DOS, QUE TIENE QUE MORDER.
        if etq == "GENERADOR":
            muerde = "no trae reparto por absorbido" in s
            print("     la guarda del acto de mas de dos SIN reparto MUERDE: %s" % muerde)
            if not muerde:
                fallos.append("la guarda del acto de mas de dos no mordio")
    return fallos


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("CASO POSITIVO DE LA CORRECCION DEL GENERADOR Y DEL DOSSIER (vuelta 65)")
    print("  ancestro sacado de git: %s" % ANCESTRO)
    print("=" * 78)
    fallos = []
    if not sacar_de_git(ANCESTRO, GEN, GEN_ANC) or not sacar_de_git(ANCESTRO, DOS, DOS_ANC):
        print("ROJO: no se pudieron sacar los ancestros de git %s. PARADA." % ANCESTRO)
        return 1
    print("  ancestros escritos: %s y %s" % (GEN_ANC, DOS_ANC))
    par, motivo = fabricar_fixture()
    if par is None:
        print("ROJO: %s. PARADA." % motivo)
        return 1
    print("  tramo de mentira: superviviente %s, absorbido %s (los dos VIVOS, medidos)" % par)

    fallos += mitad1(*par)
    fallos += mitad2()
    fallos += mitad3()

    for d in BORRAR:
        if os.path.exists(d):
            os.remove(d)
    quedan = [d for d in BORRAR if os.path.exists(d)]
    print()
    print("  los %d ficheros temporales BORRADOS: %s"
          % (len(BORRAR), "SI" if not quedan else "NO, quedan %s" % quedan))
    if quedan:
        fallos.append("quedaron ficheros temporales")

    print()
    print("=" * 78)
    if fallos:
        print("ROJO: %d fallo(s) y la correccion NO queda probada:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("VERDE: LA FORMA VIEJA SALE IDENTICA EN LOS DOS INSTRUMENTOS y las ramas")
    print("nuevas dejan de caer en ROJO, con la guarda del acto de mas de dos mordiendo.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
