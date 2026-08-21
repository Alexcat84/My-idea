# -*- coding: utf-8 -*-
"""vuelta65_caso_positivo_promesas.py . EL CASO POSITIVO DEL ENSANCHE DE LA AGUJA
DE scripts/loop/comprobar_promesas_de_marcado.py, EN SUS DOS MITADES.

Lo manda el acta 64, pregunta 6 (linea 16947) y lo encarga la TAREA 1.b de la
vuelta 65. Una guarda que se ensancha sin caso positivo no se puede distinguir de
una guarda que se afloja.

MITAD 1, NO REGRESION. Las DOS corridas ya selladas se re-corren con el
instrumento ENSANCHADO y tienen que seguir dando lo mismo AL DIGITO:

  - la de la vuelta 63 (SALIDA_V63_PROMESAS_CUMPLIDAS.txt): 2 promesas, 2
    CUMPLIDAS, 0 INCUMPLIDAS, contra el REPORTE DE LA VUELTA 63;
  - la de la vuelta 64 (SALIDA_V64_PROMESAS_CUMPLIDAS.txt): 2 promesas, 2
    CUMPLIDAS, 0 INCUMPLIDAS, contra el REPORTE DE LA VUELTA 64.

EL REPORTE DE CADA VUELTA SE SACA DE git, NO SE RECUERDA: docs/loop/REPORTE.md se
sobrescribe cada vuelta, asi que el de la 63 y el de la 64 se extraen de sus
commits con git show y se dejan en ficheros temporales que este instrumento BORRA
al terminar. Sin eso la mitad 1 estaria comparando contra el reporte equivocado,
que es la especie de caida que la regla 1 persigue.

MITAD 2, VISIBILIDAD. Un PLAN DE MENTIRA con una nota en PLURAL y sin una sola
aparicion de la forma singular:

  - la aguja VIEJA (solo singular) NO lo ve: 0 promesas medidas;
  - la aguja NUEVA (singular mas plural) SI lo ve: 1 promesa, y sale INCUMPLIDA
    porque la seccion 6 del reporte no nombra a ese acto inventado.

EL PLAN DE MENTIRA SE BORRA TRAS LA PRUEBA, y su borrado se comprueba e imprime.

La aguja VIEJA no se re-teclea aqui: se reconstruye del propio instrumento
quitandole la forma plural de FORMAS, asi que si manana alguien cambia la
constante, esta prueba cambia con ella.

DE SOLO LECTURA sobre todo lo committeado: los unicos ficheros que toca son los
temporales que el mismo crea y borra.

Uso:
  python scripts/loop/vuelta65_caso_positivo_promesas.py
exit 0 si las dos mitades salen VERDE; exit 1 si alguna falla.
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
INSTRUMENTO = os.path.join("scripts", "loop", "comprobar_promesas_de_marcado.py")
NL = chr(10)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comprobar_promesas_de_marcado as CPM  # noqa: E402

# (etiqueta, commit del que sale el reporte de esa vuelta, planes de la corrida,
#  salida sellada con la que se coteja)
CORRIDAS = [
    ("VUELTA 63", "3f5f33da",
     ["docs/loop/PLAN_V63_OPM03I.json", "docs/loop/PLAN_V63_OPM02PROG.json"],
     "SALIDA_V63_PROMESAS_CUMPLIDAS.txt"),
    ("VUELTA 64", "10186e4f",
     ["docs/loop/PLAN_V64_OPM03II.json", "docs/loop/PLAN_V63_OPM02PROG.json"],
     "SALIDA_V64_PROMESAS_CUMPLIDAS.txt"),
]

PLAN_MENTIRA = os.path.join(LOOP, "_v65_plan_de_mentira.json")
CUERPO_MENTIRA = {
    "operacion": "OP-DE-MENTIRA",
    "rotulo": "PLAN DE MENTIRA DEL CASO POSITIVO DE LA VUELTA 65",
    "fecha": "2026-08-20",
    "contrato_de_perdidas": "CAMPO PROPIO v1",
    "actos": [
        {
            "orden": 999,
            "miembros": ["nodo_que_no_existe_de_mentira_v65"],
            "motivo": ("ACTO DE MENTIRA PARA PROBAR LA AGUJA. Las dos piezas de "
                       "abajo VAN MARCADAS COMO DISCUTIBLES en la seccion 6 del "
                       "reporte de esta vuelta."),
            "nota_del_reparto": "",
            "perdidas": [],
        }
    ],
}


def correr(reporte, planes, etq):
    """Corre el instrumento ENSANCHADO tal como se invoca desde la linea de
    ordenes, y devuelve (codigo, salida)."""
    cmd = [sys.executable, INSTRUMENTO, "--reporte", reporte]
    for p in planes:
        cmd += ["--plan", p]
    r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    print("     comando: python %s --reporte %s %s"
          % (INSTRUMENTO.replace(os.sep, "/"), reporte,
             " ".join("--plan " + p for p in planes)))
    print("     exit %d" % r.returncode)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def cifras(txt):
    d = {}
    for clave, aguja in (("medidas", "promesas medidas     : "),
                         ("cumplidas", "promesas CUMPLIDAS   : "),
                         ("incumplidas", "promesas INCUMPLIDAS : ")):
        for l in txt.split(NL):
            if aguja in l:
                d[clave] = int(l.split(aguja)[1].strip())
    return d


def mitad1():
    print()
    print("=" * 78)
    print("MITAD 1: NO REGRESION. Las dos corridas selladas, re-corridas con la")
    print("aguja ENSANCHADA, contra el reporte de SU PROPIA vuelta sacado de git.")
    print("=" * 78)
    fallos = []
    temporales = []
    for etq, commit, planes, sellada in CORRIDAS:
        print()
        print("  --- %s ---" % etq)
        tmp_rel = "docs/loop/_v65_reporte_%s.md" % etq.split()[1]
        tmp_abs = os.path.join(RAIZ, tmp_rel.replace("/", os.sep))
        r = subprocess.run(["git", "show", "%s:docs/loop/REPORTE.md" % commit],
                           cwd=RAIZ, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        if r.returncode != 0:
            fallos.append("%s: git show %s no devuelve el reporte" % (etq, commit))
            print("     ROJO: git show %s fallo" % commit)
            continue
        io.open(tmp_abs, "w", encoding="utf-8", newline=NL).write(r.stdout)
        temporales.append(tmp_abs)
        print("     reporte sacado de git %s, cabecera: %s"
              % (commit, r.stdout.split(NL)[0][:78]))

        cod, salida = correr(tmp_rel, planes, etq)
        hoy = cifras(salida)
        viejo = cifras(io.open(os.path.join(LOOP, sellada), encoding="utf-8").read())
        print("     sellada  (%s): %s" % (sellada, viejo))
        print("     hoy, con la aguja ensanchada : %s" % hoy)
        igual = hoy == viejo and cod == 0
        print("     %s" % ("CALZA AL DIGITO y exit 0: NO HAY REGRESION"
                           if igual else "ROJO: NO CALZA"))
        if not igual:
            fallos.append("%s: sellada %s contra hoy %s (exit %d)"
                          % (etq, viejo, hoy, cod))

    for t in temporales:
        os.remove(t)
    print()
    print("  los %d reportes temporales BORRADOS: %s"
          % (len(temporales),
             "SI" if not any(os.path.exists(t) for t in temporales) else "NO"))
    return fallos


def mitad2():
    print()
    print("=" * 78)
    print("MITAD 2: VISIBILIDAD. Un plan de mentira con la nota SOLO en PLURAL.")
    print("=" * 78)
    fallos = []
    io.open(PLAN_MENTIRA, "w", encoding="utf-8", newline=NL).write(
        json.dumps(CUERPO_MENTIRA, ensure_ascii=False, indent=2))
    print()
    print("  plan de mentira escrito en docs/loop/_v65_plan_de_mentira.json")
    nota = CUERPO_MENTIRA["actos"][0]["motivo"]
    print("     el motivo dice: %s" % nota)
    print("     trae la forma SINGULAR: %s"
          % (CPM.PROMESA in nota.lower()))
    print("     trae la forma PLURAL  : %s"
          % (CPM.PROMESA_PLURAL in nota.lower()))
    if CPM.PROMESA in nota.lower():
        fallos.append("el plan de mentira trae la forma singular y la prueba no valdria")

    # LA AGUJA VIEJA, reconstruida del propio instrumento y no re-tecleada.
    reporte = io.open(os.path.join(LOOP, "REPORTE.md"), encoding="utf-8").read()
    s6 = CPM.seccion6(reporte)
    print()
    print("  seccion 6 del reporte vigente: %d caracteres" % len(s6))
    for etq, formas in (("AGUJA VIEJA (solo singular)", (CPM.PROMESA,)),
                        ("AGUJA NUEVA (singular mas plural)", CPM.FORMAS)):
        vistas = 0
        for acto in CUERPO_MENTIRA["actos"]:
            for campo in ("motivo", "nota_del_reparto"):
                bajo = (acto.get(campo) or "").lower()
                if [f for f in formas if f in bajo]:
                    vistas += 1
        print("     %-36s ve %d promesa(s)" % (etq, vistas))
        if "VIEJA" in etq and vistas != 0:
            fallos.append("la aguja vieja ve %d y deberia ver 0" % vistas)
        if "NUEVA" in etq and vistas != 1:
            fallos.append("la aguja nueva ve %d y deberia ver 1" % vistas)

    print()
    print("  Y AHORA POR EL INSTRUMENTO ENTERO, no por su constante:")
    cod, salida = correr("docs/loop/REPORTE.md",
                         ["docs/loop/_v65_plan_de_mentira.json"], "MENTIRA")
    c = cifras(salida)
    print("     %s" % c)
    ok = c.get("medidas") == 1 and c.get("incumplidas") == 1 and cod == 1
    print("     %s" % ("MUERDE: la promesa en plural PASA A VERSE y sale en ROJO "
                       "(exit 1) porque la seccion 6 no nombra ese acto inventado"
                       if ok else "ROJO: la prueba de visibilidad no muerde"))
    if not ok:
        fallos.append("visibilidad: %s con exit %d" % (c, cod))
    for l in salida.split(NL):
        if "acto 999" in l or "forma hallada" in l or "NADA de" in l:
            print("     | %s" % l.strip()[:110])

    os.remove(PLAN_MENTIRA)
    print()
    print("  el plan de mentira BORRADO: %s"
          % ("SI" if not os.path.exists(PLAN_MENTIRA) else "NO"))
    if os.path.exists(PLAN_MENTIRA):
        fallos.append("el plan de mentira no se borro")
    return fallos


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("CASO POSITIVO DEL ENSANCHE DE LA AGUJA DEL COMPROBADOR DE PROMESAS")
    print("  instrumento : %s" % INSTRUMENTO.replace(os.sep, "/"))
    print("  formas      : %s" % ", ".join(f.upper() for f in CPM.FORMAS))
    print("=" * 78)
    fallos = mitad1() + mitad2()
    print()
    print("=" * 78)
    if fallos:
        print("ROJO: %d fallo(s) y el ensanche NO queda probado:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("VERDE: LAS DOS MITADES MUERDEN. No hay regresion (2 de 2 y 2 de 2 al")
    print("digito contra las salidas selladas) y la forma plural PASA A VERSE.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
