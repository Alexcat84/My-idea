# -*- coding: utf-8 -*-
"""triage_ambar_titulos.py . TRIA LOS AMBAR DEL BARRIDO DE TITULOS POR EL CARRIL
DEL BANCO 9.10, Y ESCRIBE EL VEREDICTO EN EL PROPIO FICHERO.

NOMBRE ESTABLE A PROPOSITO, por la misma vara que persigue el barrido: no lleva
numero de vuelta ni de tramo. La vuelta se pasa con --vuelta y solo entra en el
titulo de la salida y en la fecha de las notas; nada de lo medido depende de ella.

POR QUE NACE (encargo de la 61, TAREA 1). El barrido dice de cada AMBAR, con
todas sus letras, que NO LO DECIDE: un numero tallado que no calza o NOMBRA UN
ANCESTRO a proposito (procedencia, y entonces no envejece) o ES UNA CITA
ENVEJECIDA, y eso lo separa el ojo. Los 35 AMBAR estuvieron en cola mientras el
tramo 5 corria. El tramo cerro, y este instrumento es donde el ojo escribe lo que
leyo, EN UNA FORMA QUE LA MAQUINA VUELVE A COTEJAR EN CADA CORRIDA.

LAS TRES SALIDAS DEL TRIAGE, y cada una con su forma:

  SELLO_FIJO   el numero nombra el sujeto FIJO del propio instrumento, que es
               justo lo que su nombre no dice (por eso salio AMBAR: la maquina no
               tenia con que cotejarlo). Se escribe un ROTULO que lo declara. El
               barrido lo coteja: el numero tallado tiene que ser el declarado, y
               el fichero NO puede recibir esa especie por argumento. Un
               instrumento repuntable NO se puede sellar con este rotulo.
  PROCEDENCIA  el numero nombra un ancestro o un sujeto ajeno a proposito (el
               acta de otra vuelta, la propuesta de otra vuelta, el instrumento
               del que se copio la aritmetica). Se escribe un ROTULO con la
               fuente y un literal de prueba, y el barrido comprueba en cada
               corrida que la fuente existe y contiene el literal.
  ENVEJECIDA   el numero se heredo de un ancestro y HOY es falso. Se corrige, con
               NOTA FECHADA y EL TEXTO VIEJO CITADO ENTERO, nunca borrado.

LO QUE ESTE INSTRUMENTO NO TOCA, dicho antes que lo que toca:
  - LA ARITMETICA DE LOS FICHEROS TRIADOS. Solo escribe lineas de comentario, y
    en el unico caso ENVEJECIDA cambia el literal del titulo y nada mas.
  - LOS ROJO DEL BARRIDO. Ni uno. En el fichero de la cita envejecida el TRAMO 3
    de la misma linea se queda tal cual, y la nota lo dice.

LAS GUARDAS, todas ANTES de escribir un solo byte:
  1. CADA ENTRADA DE LA TABLA SE COTEJA CONTRA EL BARRIDO CORRIDO HOY: si la
     mencion que dice triar no es un AMBAR VIVO de ese fichero en esta corrida,
     el instrumento CAE EN ROJO y NO ESCRIBE NADA (ni esa ni las otras).
  2. LA CUENTA CUADRA O NO SE ESCRIBE: la tabla tiene que cubrir TODOS los AMBAR
     del barrido de hoy, ni uno mas ni uno menos.
  3. LA VUELTA DE LA CITA ENVEJECIDA SE MIDE CON git, NO SE TECLEA: se lee el
     commit que ANADIO el fichero y el asunto de ese commit. Si el numero medido
     no coincide con el que el propio nombre del fichero declara, ROJO.
  4. IDEMPOTENTE: lo que ya esta escrito no se reescribe, y la segunda corrida
     dice YA ESTA.

USO:
  python scripts/loop/triage_ambar_titulos.py --vuelta 61            (simulacro)
  python scripts/loop/triage_ambar_titulos.py --vuelta 61 --escribir

SALIDA: exit 0 si el triage cuadra y (con --escribir) se escribe; exit 1 en ROJO.
"""
import argparse
import ast
import datetime
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import barrido_titulos_tallados as BARRIDO

ACTA = "docs/loop/ACTA_AUDITOR.md"

# LA TABLA DEL TRIAGE. Una fila por CLAVE del barrido (fichero, especie, numero),
# con el veredicto del ojo y lo que la maquina tiene que cotejar.
SELLO_FIJO = [
    ("scripts/loop/vuelta48_registro_tramo.py", "tramo", 1,
     "escribe el registro del tramo 1 de OP-U-01 y lee PLAN_V48_OPU01_TRAMO1: sujeto fijo"),
    ("scripts/loop/vuelta54_registro_tramo.py", "tramo", 2,
     "escribe el registro del tramo 2 de OP-U-01: sujeto fijo, sin argumento que lo repunte"),
    ("scripts/loop/vuelta55_registro_tramo.py", "tramo", 2,
     "escribe el registro del CIERRE del tramo 2: sujeto fijo, sin argumento que lo repunte"),
    ("scripts/loop/vuelta55_deshacer_acto23.py", "tramo", 2,
     "deshace la fusion del acto 23 del tramo 2, un acto nombrado: sujeto fijo"),
    ("scripts/loop/vuelta56_registro_tramo.py", "tramo", 3,
     "escribe el registro del cierre del tramo 3: sujeto fijo, sin argumento que lo repunte"),
    ("scripts/loop/vuelta57_registro_tramo.py", "tramo", 4,
     "escribe el registro del cierre del tramo 4: sujeto fijo, sin argumento que lo repunte"),
    ("scripts/loop/vuelta58_deshacer_acto32.py", "tramo", 4,
     "deshace la fusion del acto 32 del tramo 4, un acto nombrado: sujeto fijo"),
    ("scripts/loop/vuelta58_registro_acto32.py", "tramo", 4,
     "corrige el registro del tramo 4 por el acto 32: sujeto fijo"),
    ("scripts/loop/vuelta58_relectura_acto32.py", "tramo", 4,
     "relee el acto 32 del tramo 4 contra el grafo pre fusion: sujeto fijo"),
    ("scripts/loop/vuelta58_tallar_planes.py", "tramo", 4,
     "talla las tablas de los PLAN_V57_OPU01_LOTE_*.json, que son los del tramo 4 y estan "
     "escritos en el codigo: --vuelta solo cambia el rotulo impreso, no el plan leido"),
]

PROCEDENCIA = [
    ("scripts/loop/_v41_patch_costuras.py", "vuelta", 40, ACTA,
     "ACTA DE LA VUELTA 40 DEL AUDITOR",
     "cita el acta de la vuelta 40, seccion 5, pregunta 2, que es lo que ejecuta"),
    ("scripts/loop/_v50_contraste_contar_ld_v49.py", "vuelta", 48,
     "scripts/loop/vuelta48_contar_ld.py", "Vuelta 48, TAREA 1.4",
     "es la copia de contraste del instrumento de la vuelta 48 y conserva su cabecera a proposito"),
    ("scripts/loop/backlog_l03_vuelta14.py", "vuelta", 13, ACTA, "## VUELTA 13,",
     "nombra la via que la vuelta 13 uso para OP-U-02, de la que copia el metodo"),
    ("scripts/loop/vuelta17_marcar_221_superadas.py", "vuelta", 16, ACTA, "## VUELTA 16,",
     "ejecuta el discutible 1 del acta de la vuelta 16 y la cita con su seccion"),
    ("scripts/loop/vuelta17_nota_op_i_01.py", "vuelta", 16, ACTA, "## VUELTA 16,",
     "registra el hueco nombrado del discutible 2 del acta de la vuelta 16"),
    ("scripts/loop/vuelta19_tarea1.py", "vuelta", 18, ACTA, "## VUELTA 18,",
     "escribe los registros de las adjudicaciones del acta de la vuelta 18"),
    ("scripts/loop/vuelta21_tarea1.py", "vuelta", 20, ACTA, "## VUELTA 20,",
     "escribe los registros de las adjudicaciones del acta de la vuelta 20"),
    ("scripts/loop/vuelta37_aviso_v35.py", "vuelta", 35,
     "docs/loop/PROPUESTA_V35_RELECTURAS.json", "PROPUESTA NO VOLCADA",
     "su sujeto ES la propuesta de la vuelta 35, y el aviso de corte se le pone encima"),
    ("scripts/loop/vuelta46_registro_auditoria.py", "vuelta", 45, ACTA,
     "ACTA DE LA VUELTA 45 DEL AUDITOR", "su sujeto ES la auditoria de la vuelta 45"),
    ("scripts/loop/vuelta50_correcciones_910_cierre.py", "vuelta", 49, ACTA,
     "ACTA DE LA VUELTA 49 DEL AUDITOR",
     "nombra a la vuelta 49 como la que no corrio este barrido, que es su motivo de existir"),
    ("scripts/loop/vuelta55_deshacer_acto23.py", "vuelta", 54, ACTA,
     "ACTA DE LA VUELTA 54 DEL AUDITOR",
     "nombra la vuelta 54 como la que ejecuto la fusion que este instrumento deshace"),
    ("scripts/loop/vuelta56_tramo3_nomina.py", "vuelta", 55,
     "scripts/loop/vuelta55_tramo2_nomina.py", "RE-IDENTIFICADO POR SUS",
     "declara de que ancestro copio la aritmetica de identidad por miembros"),
    ("scripts/loop/vuelta57_correcciones_tarea1.py", "vuelta", 56, ACTA,
     "ACTA DE LA VUELTA 56 DEL AUDITOR",
     "nombra la vuelta 56 como la que dejo envejecidas las tres citas que corrige"),
    ("scripts/loop/vuelta57_tramo4_nomina.py", "vuelta", 55,
     "scripts/loop/vuelta55_tramo2_nomina.py", "RE-IDENTIFICADO POR SUS",
     "declara de que ancestro viene la aritmetica de identidad por miembros"),
    ("scripts/loop/vuelta58_deshacer_acto32.py", "vuelta", 57, ACTA,
     "ACTA DE LA VUELTA 57 DEL AUDITOR",
     "nombra la vuelta 57 como la que ejecuto la fusion que este instrumento deshace"),
]

# LA UNICA CITA ENVEJECIDA DEL TRIAGE. El ancestro imprime lo mismo con su propio
# numero y ahi SI es verdad; la copia se quedo con el numero del ancestro.
ENVEJECIDA = {
    "fichero": "scripts/loop/vuelta56_varas_tramo3.py",
    "especie": "vuelta",
    "numero": 54,
    "viejo": 'print("EL CUADRO DE VARAS DE LOS %d ACTOS DEL TRAMO 3 (vuelta 54)" % len(tramo))',
    "nuevo_patron": 'print("EL CUADRO DE VARAS DE LOS %%d ACTOS DEL TRAMO 3 (vuelta %d)" %% len(tramo))',
    "ancestro": "scripts/loop/vuelta54_varas_tramo2.py",
}


def barrido_de_hoy():
    """Del barrido corrido AHORA: los AMBAR vivos y los ya ROTULADOS, cada uno por
    (fichero, especie, numero). Los segundos son la via de la idempotencia: una
    clave que ya salio ROTULADA no es un AMBAR que falte, es una YA TRIADA."""
    vivos, rotulados = {}, {}
    for ruta_abs, rel in BARRIDO.ficheros(BARRIDO.RAICES):
        for h in BARRIDO.barrer(ruta_abs, rel):
            clave = (rel, h["especie"], h["numero"])
            if h["clase"] == "AMBAR":
                vivos.setdefault(clave, []).append(h)
            elif h["clase"] == "ROTULADO":
                rotulados.setdefault(clave, []).append(h)
    return vivos, rotulados


MARCA_CORRECCION = "# EL TEXTO VIEJO, CITADO ENTERO Y NO BORRADO:"


def corregida_ya(fichero):
    """La cita envejecida ya esta corregida en el fichero?

    NO se pregunta si el texto viejo desaparecio, y el motivo es la propia
    doctrina: el texto viejo se CITA y no se borra, asi que sigue ahi dentro de la
    nota. La pregunta buena es si la NOTA de la correccion ya esta escrita."""
    if fichero != ENVEJECIDA["fichero"]:
        return False
    ruta = os.path.join(RAIZ, fichero.replace("/", os.sep))
    if not os.path.exists(ruta):
        return False
    return MARCA_CORRECCION in io.open(ruta, encoding="utf-8").read()


def vuelta_medida_por_git(fichero, fallos):
    """El numero de vuelta del commit que ANADIO el fichero, medido con git."""
    try:
        salida = subprocess.check_output(
            ["git", "log", "--diff-filter=A", "--format=%h|%s", "--", fichero],
            cwd=RAIZ, stderr=subprocess.STDOUT).decode("utf-8", "replace").strip()
    except (OSError, subprocess.CalledProcessError) as e:
        fallos.append("git no pudo medir el commit de alta de %s (%s)" % (fichero, e))
        return None, None, None
    lineas = [l for l in salida.splitlines() if l.strip()]
    if not lineas:
        fallos.append("git no encuentra el commit que anadio %s" % fichero)
        return None, None, None
    commit, _, asunto = lineas[-1].partition("|")
    m = re.search(r"(?i)\bvuelta\s+(\d+)", asunto)
    if not m:
        fallos.append("el asunto del commit de alta de %s no nombra vuelta: %r" % (fichero, asunto))
        return None, asunto, commit
    return int(m.group(1)), asunto, commit


def linea_tras_docstring(ruta_abs, fallos):
    """La linea SIGUIENTE al cierre del docstring del modulo. Ahi van los rotulos:
    FUERA del docstring, para no meterse dentro del titulo que el barrido lee."""
    fuente = io.open(ruta_abs, encoding="utf-8").read()
    arbol = ast.parse(fuente)
    if not (arbol.body and isinstance(arbol.body[0], ast.Expr)
            and isinstance(arbol.body[0].value, ast.Constant)
            and isinstance(arbol.body[0].value.value, str)):
        fallos.append("%s no abre con docstring de modulo" % ruta_abs)
        return None
    return arbol.body[0].end_lineno


def rotulo_sello(especie, numero, corte, motivo):
    return ('# ROTULO titulo especie=SELLO_FIJO sujeto=%s:%d corte=%s motivo="%s"'
            % (especie, numero, corte, motivo))


def rotulo_procedencia(especie, numero, fuente, prueba, corte, motivo):
    return ('# ROTULO titulo especie=PROCEDENCIA cita=%s:%d fuente=%s prueba="%s" '
            'corte=%s motivo="%s"' % (especie, numero, fuente, prueba, corte, motivo))


def insertar(lineas, indice, bloque):
    """Mete el bloque ANTES de la linea de indice (0 based)."""
    return lineas[:indice] + bloque + lineas[indice:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, required=True)
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    corte = datetime.date.today().isoformat()
    fallos = []

    print("=" * 100)
    print("TRIAGE DE LOS AMBAR DEL BARRIDO DE TITULOS, POR EL CARRIL DEL BANCO 9.10 (vuelta %d)"
          % a.vuelta)
    print("  modo : %s" % ("ESCRIBIR" if a.escribir else "SIMULAR"))
    print("  corte: %s (fecha del sistema, la misma que va en cada rotulo)" % corte)
    print("=" * 100)
    print()

    # ---- GUARDAS 1 y 2: la tabla contra el barrido de HOY ----
    vivos, rotulados = barrido_de_hoy()
    total_vivos = sum(len(v) for v in vivos.values())
    total_rot = sum(len(v) for v in rotulados.values())
    print("--- EL BARRIDO CORRIDO AHORA MISMO, QUE ES LA VARA ---")
    print("  menciones AMBAR vivas   : %d en %d claves (fichero, especie, numero)"
          % (total_vivos, len(vivos)))
    print("  menciones YA ROTULADAS  : %d en %d claves (triadas en una corrida anterior)"
          % (total_rot, len(rotulados)))

    tabla = [(f, e, n, "SELLO_FIJO") for f, e, n, _ in SELLO_FIJO]
    tabla += [(f, e, n, "PROCEDENCIA") for f, e, n, _, _, _ in PROCEDENCIA]
    tabla.append((ENVEJECIDA["fichero"], ENVEJECIDA["especie"], ENVEJECIDA["numero"], "ENVEJECIDA"))

    claves_tabla = {(f, e, n) for f, e, n, _ in tabla}
    if len(claves_tabla) != len(tabla):
        fallos.append("la tabla repite una clave (fichero, especie, numero)")
    cubiertas, ya_triadas = 0, 0
    for f, e, n, veredicto in tabla:
        if (f, e, n) in vivos:
            cubiertas += len(vivos[(f, e, n)])
        elif (f, e, n) in rotulados:
            ya_triadas += len(rotulados[(f, e, n)])
        elif veredicto == "ENVEJECIDA" and corregida_ya(f):
            ya_triadas += 1
        else:
            fallos.append("la tabla tria %s %s %d en %s y HOY no es ni un AMBAR vivo ni una "
                          "mencion ya rotulada alli" % (veredicto, e, n, f))
    for clave in sorted(vivos):
        if clave not in claves_tabla:
            fallos.append("el barrido de hoy trae un AMBAR que la tabla NO tria: %s %s %d"
                          % (clave[0], clave[1], clave[2]))
    print("  menciones cubiertas por la tabla: %d AMBAR vivas mas %d ya triadas"
          % (cubiertas, ya_triadas))
    print("  claves de la tabla: %d SELLO_FIJO, %d PROCEDENCIA, 1 ENVEJECIDA"
          % (len(SELLO_FIJO), len(PROCEDENCIA)))
    print()

    # ---- GUARDA 3: la vuelta de la cita envejecida, MEDIDA con git ----
    print("--- LA CITA ENVEJECIDA, CON SU VUELTA MEDIDA Y NO TECLEADA ---")
    medida, asunto, commit = vuelta_medida_por_git(ENVEJECIDA["fichero"], fallos)
    m = re.search(r"(?i)vuelta(\d+)", os.path.basename(ENVEJECIDA["fichero"]))
    declarada = int(m.group(1)) if m else None
    print("  fichero            : %s" % ENVEJECIDA["fichero"])
    print("  commit que lo anade: %s" % commit)
    print("  asunto del commit  : %s" % asunto)
    print("  vuelta MEDIDA por git                  : %s" % medida)
    print("  vuelta que el NOMBRE del fichero declara: %s" % declarada)
    if medida is None or declarada is None:
        fallos.append("no se pudo medir la vuelta de %s por los dos relojes" % ENVEJECIDA["fichero"])
    elif medida != declarada:
        fallos.append("los dos relojes no coinciden (git dice %d, el nombre dice %d): "
                      "no se fecha a ojo" % (medida, declarada))
    else:
        print("  LOS DOS RELOJES COINCIDEN en %d: la correccion escribe ese numero y no otro" % medida)
    print()

    if fallos:
        print("--- ROJO: %d, Y NO SE ESCRIBE NADA ---" % len(fallos))
        for f in fallos:
            print("    %s" % f)
        print("FIN")
        return 1

    # ---- LOS ROTULOS ----
    plan = {}
    for fichero, especie, numero, motivo in SELLO_FIJO:
        plan.setdefault(fichero, []).append(rotulo_sello(especie, numero, corte, motivo))
    for fichero, especie, numero, fuente, prueba, motivo in PROCEDENCIA:
        plan.setdefault(fichero, []).append(
            rotulo_procedencia(especie, numero, fuente, prueba, corte, motivo))

    print("--- LOS ROTULOS, uno por clave (fichero, especie, numero) ---")
    escritos, ya_estaban = 0, 0
    for fichero in sorted(plan):
        ruta_abs = os.path.join(RAIZ, fichero.replace("/", os.sep))
        texto = io.open(ruta_abs, encoding="utf-8").read()
        nuevos = [r for r in plan[fichero] if r not in texto]
        ya_estaban += len(plan[fichero]) - len(nuevos)
        if not nuevos:
            print("    %-52s YA ESTA" % fichero)
            continue
        destino = linea_tras_docstring(ruta_abs, fallos)
        if destino is None:
            continue
        print("    %-52s +%d rotulo(s) tras el docstring (linea %d)"
              % (fichero, len(nuevos), destino))
        for r in nuevos:
            print("        %s" % r)
        escritos += len(nuevos)
        if a.escribir:
            lineas = insertar(texto.splitlines(), destino, nuevos)
            io.open(ruta_abs, "w", encoding="utf-8", newline=chr(10)).write(
                chr(10).join(lineas) + chr(10))
    print()

    # ---- LA CORRECCION DE LA CITA ENVEJECIDA ----
    print("--- LA CORRECCION DECLARADA, con el texto viejo CITADO y no borrado ---")
    ruta_abs = os.path.join(RAIZ, ENVEJECIDA["fichero"].replace("/", os.sep))
    texto = io.open(ruta_abs, encoding="utf-8").read()
    nuevo = ENVEJECIDA["nuevo_patron"] % medida
    if MARCA_CORRECCION in texto:
        print("    YA ESTA: la nota de la correccion ya esta escrita y la linea dice ya "
              "(vuelta %d). No se reescribe." % medida)
    elif ENVEJECIDA["viejo"] not in texto:
        fallos.append("el texto viejo de la cita envejecida no aparece literal en %s"
                      % ENVEJECIDA["fichero"])
    else:
        nota = [
            "    # CORRECCION DECLARADA (%s, vuelta %d, TAREA 1, carril del banco 9.10)."
            % (corte, a.vuelta),
            "    %s" % MARCA_CORRECCION,
            "    #   %s" % ENVEJECIDA["viejo"],
            "    # Por que era CITA ENVEJECIDA y no procedencia: el (vuelta 54) venia del ancestro",
            "    # %s, donde SI es verdad, y este fichero" % ENVEJECIDA["ancestro"],
            "    # nacio en la vuelta %d, MEDIDA con git log --diff-filter=A" % medida,
            "    # (commit %s, asunto %r)." % (commit, asunto),
            "    # EL TRAMO 3 DE ESTA MISMA LINEA NO SE TOCA: es un ROJO del barrido y esta vuelta",
            "    # no paga ROJO. Se corrige la cita envejecida y nada mas.",
        ]
        lineas = texto.splitlines()
        indice = next(i for i, l in enumerate(lineas) if ENVEJECIDA["viejo"] in l)
        print("    linea %d de %s" % (indice + 1, ENVEJECIDA["fichero"]))
        print("        VIEJO: %s" % ENVEJECIDA["viejo"])
        print("        NUEVO: %s" % nuevo)
        for l in nota:
            print("        %s" % l.strip())
        if a.escribir:
            lineas[indice] = lineas[indice].replace(ENVEJECIDA["viejo"], nuevo)
            lineas = insertar(lineas, indice, nota)
            io.open(ruta_abs, "w", encoding="utf-8", newline=chr(10)).write(
                chr(10).join(lineas) + chr(10))
        escritos += 1
    print()

    if fallos:
        print("--- ROJO: %d ---" % len(fallos))
        for f in fallos:
            print("    %s" % f)
        print("FIN")
        return 1

    print("RESUMEN: %d menciones AMBAR vivas triadas y %d ya triadas antes (%d claves "
          "SELLO_FIJO, %d PROCEDENCIA, 1 ENVEJECIDA) | escrituras nuevas %d, ya estaban %d | modo %s"
          % (cubiertas, ya_triadas, len(SELLO_FIJO), len(PROCEDENCIA), escritos, ya_estaban,
             "ESCRIBIR" if a.escribir else "SIMULAR"))
    if not a.escribir and escritos:
        print("SIMULACRO: no se escribio ni un byte. Con --escribir se escribe.")
    if a.escribir and not escritos:
        print("YA ESTA: no habia nada nuevo que escribir.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
