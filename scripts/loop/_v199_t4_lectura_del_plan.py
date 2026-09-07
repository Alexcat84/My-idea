# -*- coding: utf-8 -*-
r"""_v199_t4_lectura_del_plan.py . LA LECTURA QUE LA VARA DEL EXPEDIENTE DEJA
ESCRITA Y NO HACE, CORRIDA SOBRE LAS CUATRO FICHAS DE TRABAJO REAL.

DE DONDE SALE: TAREA 4 del encargo de la vuelta 199, *"RETOMAR EL PLAN, POR LA
VARA DEL EXPEDIENTE y no por el campo `estado`"*, en el orden `OP-L-03`,
`OP-L-01`, `OP-L-02`, `OP-I-01`.

QUE ES ESTA VUELTA DEL PLAN, DICHO SIN ADORNO. La vara
(`scripts/loop/vuelta150_3_relectura_expediente.py`) termina con una frase que
lleva vueltas escrita y que nadie habia contestado: **"Si cubre lo que la ficha
describe es LECTURA, y esta vara no la hace."** La vara sabe decir si el documento
que una ficha nombra EXISTE; **no sabe decir si dice lo que la ficha promete**.
Esto lo mide, ficha por ficha, contra el disco de HOY.

LO QUE **NO** HACE, Y VA PRIMERO PARA QUE NO SE BUSQUE: **no mueve ni un `estado`,
ni un nodo, ni un veredicto**. El campo `estado` es justamente lo que el encargo
manda NO usar como vara, y moverlo seria cerrar por decreto lo que aqui solo se
mide. Si una ficha sale cubierta, **eso es una medicion y no una adjudicacion**.

LA VARA DE CADA FICHA SALE DE SU PROPIA `evidencia` Y `verificacion`, leidas de
`docs/plan/OPERACIONES.jsonl` en esta corrida. No se teclea ninguna promesa: se
lee la que la ficha escribio y se busca en disco.

USO:
  python scripts/loop/_v199_t4_lectura_del_plan.py
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
AQUI = os.path.dirname(os.path.abspath(__file__))
NL = chr(10)
PY = sys.executable
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
SELLADA = os.path.join(LOOP, "SALIDA_V199_T4_LECTURA_DEL_PLAN.txt")

ORDEN = ("OP-L-03", "OP-L-01", "OP-L-02", "OP-I-01")


def medir(rel):
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(ruta):
        return None
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(chr(13).encode() + b"\n", b"\n")
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest()[:16])


def texto(rel):
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    return io.open(ruta, encoding="utf-8", errors="replace").read()


def fichas():
    salida = {}
    for l in io.open(OPERACIONES, encoding="utf-8"):
        l = l.strip()
        if not l:
            continue
        d = json.loads(l)
        salida[d.get("id_op")] = d
    return salida


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    veredictos = {}

    corte = subprocess.run(["git", "log", "-1", "--format=%ad", "--date=short"],
                           cwd=RAIZ, capture_output=True)
    corte = corte.stdout.decode("utf-8", errors="replace").strip()

    w("=" * 78)
    w("VUELTA 199, TAREA 4: EL PLAN, RETOMADO POR LA VARA DEL EXPEDIENTE.")
    w("LA LECTURA QUE LA VARA DEJA ESCRITA Y NO HACE.")
    w("=" * 78)
    w("")
    w("FECHA DE CORTE de todo lo de abajo, leida de git: %s" % (corte or "(no legible)"))
    w("NINGUN `estado` SE MUEVE EN ESTA CORRIDA. Se lee, se mide y se documenta.")
    w("")

    F = fichas()
    w("EL EXPEDIENTE, CONTADO HOY: %d fichas en docs/plan/OPERACIONES.jsonl"
      % len(F))
    for op in ORDEN:
        w("   %-10s presente: %s | estado: %s | corte de la ficha: %s"
          % (op, op in F, F.get(op, {}).get("estado"),
             F.get(op, {}).get("fecha_corte")))
    w("")

    # ------------------------------------------------------------- OP-L-03
    w("=" * 78)
    w("4.a  OP-L-03, LA QUE LLEVA MAS VUELTAS APLAZADA")
    w("=" * 78)
    w("LO QUE SU FICHA PROMETE, leido de su `evidencia` de hoy:")
    for e in F["OP-L-03"]["evidencia"]:
        w("   . %s" % e[:150])
    w("")
    w("EL INSTRUMENTO DE SUS PARES REALES SE VUELVE A CORRER HOY, y no se hereda")
    w("la cifra de la 179: EJECUTOR.md 2 dice que un reporte anterior NUNCA es")
    w("fuente de una cifra nueva.")
    inst = "scripts/loop/vuelta179_tarea2_cobertura_final.py"
    m = medir(inst)
    if m is None:
        w("   ROJO: NO EXISTE %s" % inst)
        veredictos["OP-L-03"] = "NO MEDIBLE: falta su instrumento"
    else:
        w("   instrumento: %s (%d bytes)" % (inst, m[0]))
        env = dict(os.environ)
        env["PYTHONIOENCODING"] = "utf-8"
        r = subprocess.run([PY, inst], cwd=RAIZ, capture_output=True, env=env)
        sal = (r.stdout.decode("utf-8", errors="replace")
               + r.stderr.decode("utf-8", errors="replace"))
        w("   exitcode: %d" % r.returncode)
        for linea in sal.split(NL):
            if re.search(r"CIFRA|CON LECTURA|SIN LECTURA|VEREDICTO|pares reales",
                         linea, re.IGNORECASE):
                w("   | " + linea.strip()[:140])
        con = re.search(r"(\d+)\s+con lectura", sal, re.IGNORECASE)
        sin = re.search(r"(\d+)\s+sin lectura", sal, re.IGNORECASE)
        w("")
        w("   LA CIFRA DE HOY, extraida de esa salida: con lectura %s | sin lectura %s"
          % (con.group(1) if con else "(no impresa)",
             sin.group(1) if sin else "(no impresa)"))
        veredictos["OP-L-03"] = ("CUBIERTA EN SU LECTURA" if (sin and sin.group(1) == "0")
                                 else "NO CONCLUYENTE: el instrumento no da la resta")
    reg = "docs/plan/OP_L_03_LECTURAS.jsonl"
    mr = medir(reg)
    if mr is None:
        w("   Y SU REGISTRO PROPIO NO EXISTE: %s" % reg)
    else:
        filas = [x for x in texto(reg).split(NL) if x.strip()]
        w("   su registro propio: %s" % reg)
        w("      %d bytes | %d filas no vacias | sha256 LF %s" % (mr[0], len(filas), mr[2]))
    w("")

    # ------------------------------------------------------------- OP-L-01
    w("=" * 78)
    w("4.b  OP-L-01, LAS ONCE LECTURAS DIRIGIDAS")
    w("=" * 78)
    w("LO QUE SU FICHA PROMETE, leido de su `evidencia` de hoy:")
    for e in F["OP-L-01"]["evidencia"]:
        w("   . %s" % e[:150])
    w("")
    t_ld = texto("docs/plan/LECTURAS_DIRIGIDAS.md")
    once = ["LD-%02d" % k for k in range(1, 12)]
    presentes = [x for x in once if re.search(r"\b%s\b" % x, t_ld)]
    w("LAS ONCE, BUSCADAS UNA A UNA EN docs/plan/LECTURAS_DIRIGIDAS.md:")
    for x in once:
        w("   %-6s %s (%d aparicion(es))"
          % (x, "ESTA" if x in presentes else "NO ESTA",
             len(re.findall(r"\b%s\b" % x, t_ld))))
    w("   CIFRA de las once que estan: %d de 11" % len(presentes))
    todas_ld = sorted(set(re.findall(r"\bLD-\d+\b", t_ld)),
                      key=lambda s: int(s.split("-")[1]))
    w("   CONTRASTE, y se publica para que el 11 no se lea como el total: el")
    w("   fichero trae %d identificadores LD distintos, del %s al %s. Las once de"
      % (len(todas_ld), todas_ld[0] if todas_ld else "(ninguno)",
         todas_ld[-1] if todas_ld else "(ninguno)"))
    w("   OP-L-01 son la PRIMERA TANDA, no el fichero entero.")
    w("")
    w("LA CLAUSULA QUE SU `verificacion` ESCRIBE Y QUE SI SE PUEDE MEDIR:")
    w('   "ninguna de las once aparece en INTRA_DOMINIO_VEREDICTOS.jsonl"')
    t_ver = texto("docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
    coladas = [x for x in once if re.search(r"\b%s\b" % x, t_ver)]
    w("   CIFRA de las once que aparecen en el archivo de veredictos: %d"
      % len(coladas))
    w("      cuales: %s" % (", ".join(coladas) or "(ninguna)"))
    w("")
    w("LOS OTROS DOS DOCUMENTOS QUE SU EVIDENCIA NOMBRA, BUSCADOS POR SU ANCLA:")
    anclas = [("docs/INTRA_DOMINIO_INFORME.md", r"(?im)^#+.*\b52\b"),
              ("docs/BANCO_DE_TEXTOS.md", r"TABLA VIVA DE LOS PUROS")]
    ok_anclas = 0
    for rel, patron in anclas:
        me = medir(rel)
        if me is None:
            w("   %-36s NO EXISTE" % rel)
            continue
        hits = re.findall(patron, texto(rel))
        w("   %-36s %d bytes | ancla %r: %d acierto(s)"
          % (rel, me[0], patron[:28], len(hits)))
        if hits:
            ok_anclas += 1
    veredictos["OP-L-01"] = (
        "CUBIERTA EN SU DOCUMENTO" if (len(presentes) == 11 and not coladas
                                       and ok_anclas == len(anclas))
        else "CUBIERTA A MEDIAS, y lo que falta va nombrado arriba")
    w("")

    # ------------------------------------------------------------- OP-L-02
    w("=" * 78)
    w("4.c  OP-L-02, LA QUE EL ENCARGO MANDA MEDIR ANTES DE DAR POR HECHO NADA")
    w("=" * 78)
    w("EL ENCARGO DICE, CON ESAS PALABRAS: MEDIR SI SU DOCUMENTO EXISTE Y")
    w("DECLARARLO. Si no existe, SE DICE; no se da por hecho ni se fabrica.")
    w("")
    w("SU `evidencia` ENTERA, leida de la ficha de hoy:")
    for e in F["OP-L-02"]["evidencia"]:
        w("   . %s" % e)
    ficheros = re.findall(r"[\w/]+\.(?:md|jsonl|json|py|txt)",
                          " ".join(F["OP-L-02"]["evidencia"]))
    w("")
    w("CIFRA ficheros que su evidencia nombra: %d" % len(ficheros))
    w("   %s" % (", ".join(ficheros) or "(NINGUNO)"))
    w("")
    w("SE DICE, Y ES EL RESULTADO DE LA 4.c: **OP-L-02 NO TIENE DOCUMENTO QUE")
    w("MEDIR.** Su evidencia entera es UNA FRASE DE PROSA con una medicion del 11")
    w("ago 2026 dentro, y no nombra ni un fichero. No hay nada que abrir, y por")
    w("eso NO SE FABRICA NINGUNO: fabricarlo seria inventar la prueba que falta.")
    w("")
    w("LO QUE SI SE PUEDE MEDIR SIN FABRICAR NADA, y se mide: su `nota` describe")
    w("una SEGUNDA TANDA de 16 lecturas por tres grupos. Se busca cada grupo en")
    w("docs/plan/LECTURAS_DIRIGIDAS.md, que es donde vivirian si vivieran.")
    grupos = [("cuadrantes de mercado", r"(?i)cuadrante"),
              ("ecuacion de valor", r"(?i)ecuaci[oó]n de valor"),
              ("supervision humana de la IA", r"(?i)supervisi[oó]n.{0,20}(humana|IA)")]
    for nombre, patron in grupos:
        hits = re.findall(patron, t_ld)
        w("   %-32s %d acierto(s) en LECTURAS_DIRIGIDAS.md" % (nombre, len(hits)))
    w("")
    w("Y LA CIFRA QUE SU PROPIA NOTA PUBLICA, PARA QUE LA PREGUNTA QUEDE ESCRITA")
    w("CON NUMEROS: dice 205 fuera de cola, 126 esperando destejido o cirugia y 79")
    w("que no esperan; de esos 79, 24 cuelgan de mesa o nomina y 55 son resto. LAS")
    w("CIFRAS SON SUYAS, del corte 2026-08-11, y NO se re miden aqui porque")
    w("re medirlas seria recomputo y esta vuelta no lo trae encargado.")
    veredictos["OP-L-02"] = "SIN DOCUMENTO QUE MEDIR, y se declara"
    w("")

    # ------------------------------------------------------------- OP-I-01
    w("=" * 78)
    w("4.d  OP-I-01, EL INVENTARIO NAVEGABLE")
    w("=" * 78)
    w("LO QUE SU FICHA PROMETE, leido de su `evidencia` de hoy:")
    for e in F["OP-I-01"]["evidencia"]:
        w("   . %s" % e[:150])
    w("")
    inv = "docs/plan/INVENTARIO.jsonl"
    mi = medir(inv)
    filas = [x for x in texto(inv).split(NL) if x.strip()]
    w("   %s: %d bytes | %d filas no vacias | sha256 LF %s"
      % (inv, mi[0], len(filas), mi[2]))
    w("   LA FICHA PROMETE 323 ENTRADAS. CONTADAS HOY: %d." % len(filas))
    w("   CALZA: %s" % ("SI" if len(filas) == 323 else
                        "NO, y la discrepancia SE DECLARA en vez de ajustarse"))
    tipos = {}
    con_corte = 0
    for x in filas:
        try:
            d = json.loads(x)
        except Exception:                                # noqa: BLE001
            tipos["(fila no legible como json)"] = tipos.get(
                "(fila no legible como json)", 0) + 1
            continue
        t = d.get("tipo") or d.get("clase") or "(sin tipo)"
        tipos[t] = tipos.get(t, 0) + 1
        if d.get("fecha_corte"):
            con_corte += 1
    w("")
    w("   EL REPARTO POR TIPO, CONTADO DEL FICHERO Y NO DE LA NOTA:")
    for t in sorted(tipos, key=lambda k: (-tipos[k], str(k))):
        w("      %-28s %d" % (str(t)[:28], tipos[t]))
    w("")
    w('   LA CLAUSULA "toda entrada lleva su fecha_corte", MEDIDA:')
    w("      CIFRA entradas con fecha_corte: %d de %d" % (con_corte, len(filas)))
    w("      CIFRA entradas SIN fecha_corte: %d" % (len(filas) - con_corte))
    vista = "docs/plan/10_INVENTARIO.md"
    mv = medir(vista)
    w("")
    if mv is None:
        w("   %s NO EXISTE" % vista)
    else:
        t_v = texto(vista)
        w("   %s: %d bytes | %d lineas" % (vista, mv[0], len(t_v.split(NL))))
        for etiqueta, patron in (("PROVISIONAL", r"PROVISIONAL"),
                                 ("HUECO", r"(?i)hueco")):
            w("      el literal %-12s aparece %d vez(ces)"
              % (etiqueta, len(re.findall(patron, t_v))))
    veredictos["OP-I-01"] = (
        "CUBIERTA EN SU DOCUMENTO" if (len(filas) == 323 and con_corte == len(filas))
        else "CUBIERTA A MEDIAS, y lo que falta va nombrado arriba")
    w("")

    # ------------------------------------------------------------- EL SALDO
    w("=" * 78)
    w("EL SALDO DE LA TAREA 4, Y NINGUNA DE ESTAS LINEAS MUEVE UN `estado`")
    w("=" * 78)
    for op in ORDEN:
        w("   %-10s %s" % (op, veredictos.get(op, "(no medido)")))
    w("")
    w("LO QUE ESTO NO DICE, Y SE DICE PARA QUE NADIE LO LEA DE MAS: que el")
    w("documento de una ficha CUBRA lo que la ficha promete NO significa que su")
    w("mesa se hiciera bien. Significa que lo que la ficha escribio que estaria,")
    w("esta, y que se puede abrir y contar. Adjudicar el `estado` es del auditor.")

    t = NL.join(L) + NL
    io.open(SELLADA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (SELLADA, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
