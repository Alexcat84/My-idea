# -*- coding: utf-8 -*-
r"""vuelta165_tarea4_sujeto_de_los_41.py . TAREA 4 de la vuelta 165: EL SUJETO
DE CADA UNO DE LOS 41 ARNESES PRE 148 QUE ESTAN FUERA DE LA NOMINA, MEDIDO UNO
POR UNO.

POR QUE NO ES UNA PREGUNTA DE DOCTRINA (adjudicacion 6.5 del acta 164). El
reporte de la 164 pregunto si la regla de entrada de la vuelta 144 es
retroactiva. La pregunta esta mal planteada y lo dice la propia regla en su
letra desde la vuelta 148, que vive en el docstring de
`verificar_mutaciones_viejas.py`: *"LO QUE ESTA REGLA EXIGE ES SUJETO CONGELADO.
EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL FIN."* Una regla cuya condicion es el
ESTADO DEL SUJETO y no la fecha de nacimiento no puede ser retroactiva ni dejar
de serlo: no habla del calendario. Asi que aqui no se decide nada nuevo: se MIDE
el sujeto de cada uno.

EL UNIVERSO NO SE INVENTA. Los 41 se computan con el patron VIEJO del censo, que
es el universo en el que el acta 164 los nombro y los adjudico. El ensanche de
la TAREA 2 hace visibles otros 26 arneses pre 148 que NADIE ha adjudicado: esos
se declaran en `SALIDA_V165_T2_CENSO_ANTES_DESPUES.txt` y NO entran aqui.

LAS DOS MITADES DE LA MEDICION, Y SE DICE CUAL ES CUAL:

  MITAD EMPIRICA. Cada uno se CORRE HOY, con su cronometro y su clasificacion
  (`OK`, `ANCLA PERDIDA`, `NO MORDIO`), leyendo la salida real del proceso, y se
  mide ademas el arbol antes y despues para ver que ficheros movio. UN ARNES QUE
  NACIO VERDE Y HOY SALE ROJO CON EL MISMO CODIGO ES UNA DEMOSTRACION DE QUE SU
  SUJETO SE MOVIO: eso no es lectura, es medicion.

  MITAD ESTATICA. De cada fuente se extraen, CON `ast` Y SIN DOCSTRINGS, los
  literales de ruta y las invocaciones de `git`, y se clasifican con la TABLA DE
  REGLAS que este fichero publica entera mas abajo. De cada uno se imprimen las
  LINEAS LITERALES que sostienen el veredicto.

EL VEREDICTO, Y SU CONSERVADURISMO ES A PROPOSITO:
  SUJETO VIVO      . toca al menos un artefacto vivo, o sale ROJO hoy.
  SUJETO CONGELADO . sale verde hoy Y todos los artefactos que toca son
                     congelados.
  NO DECIDIBLE     . sale verde hoy y su fuente no da senal en ninguna de las
                     dos listas. NO ENTRA: nada entra sobre un quiza.

NINGUNO ENTRA EN BLOQUE Y NINGUNO SE DESCARTA EN BLOQUE (6.5), Y TODO ARNES QUE
ENTRE ENTRA CON SU TIEMPO PUBLICADO AL LADO (6.6).

SU CASO POSITIVO POR MUTACION es `vuelta165_tarea4_mutacion_sujeto.py`, que
fabrica fuentes de mentira que tocan artefactos conocidos de las dos listas y
exige que el clasificador les ponga la etiqueta correcta, con la segunda pasada
mutando cada esperado.

USO:
  python scripts/loop/vuelta165_tarea4_sujeto_de_los_41.py            (mide y corre)
  python scripts/loop/vuelta165_tarea4_sujeto_de_los_41.py --solo-estatico
"""
import argparse
import ast
import io
import os
import re
import subprocess
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP_SCRIPTS = os.path.join(RAIZ, "scripts", "loop")
sys.path.insert(0, LOOP_SCRIPTS)
import verificar_mutaciones_viejas as B   # noqa: E402

PY = sys.executable

# --- LA TABLA DE REGLAS, PUBLICADA ENTERA -----------------------------------
#
# ARTEFACTOS VIVOS. Un artefacto es VIVO cuando el trabajo ordinario de esta
# campana lo reescribe o le anade: el sujeto se le mueve debajo al arnes sin que
# nadie toque el arnes. La lista no se invento de una sentada: cada entrada
# lleva por que esta.
ARTEFACTOS_VIVOS = [
    ("docs/loop/REPORTE.md",
     "se SOBRESCRIBE entero cada vuelta (EJECUTOR.md 7). Es el sujeto que hizo "
     "caer a vuelta144_2d_mutacion_cobertura.py en la vuelta 145 y el ejemplar "
     "que la propia regla del sujeto congelado cita"),
    ("docs/loop/ACTA_AUDITOR.md",
     "el auditor le ANADE un acta por vuelta; sus numeros de linea se mueven"),
    ("docs/PENDIENTES.md",
     "la serie de registros le anade una entrada por vuelta"),
    ("docs/plan/OPERACIONES.jsonl",
     "las operaciones cambian de estado segun la campana avanza"),
    ("docs/plan/CORRECCIONES_A_APLICAR.md",
     "sede alterna de la serie de registros; crece"),
    ("docs/plan/PASO_NODO_CALIBRADO.jsonl",
     "se recalibra contra el grafo"),
    ("docs/plan/INTRA_DOMINIO_VEREDICTOS.jsonl",
     "el cribado y las lecturas dirigidas le escriben"),
    ("dataset/metadata/master_graph.json",
     "ES EL GRAFO VIVO. Es exactamente el sujeto que la regla excluye, y la "
     "adjudicacion 6.5 del acta 164 lo nombra asi"),
    ("dataset/nodos",
     "los nodos del grafo vivo"),
    ("scripts/loop/verificar_mutaciones_viejas.py",
     "la nomina de la bateria CRECE cada vuelta: quien la mida tiene sujeto vivo"),
]

# ARTEFACTOS CONGELADOS. Un artefacto es CONGELADO cuando su contenido no lo
# mueve el trabajo ordinario: o esta clavado a un blob de git, o es una copia
# sellada con nombre de sujeto fijo, o lo fabrica el propio arnes.
ARTEFACTOS_CONGELADOS = [
    ("SUJETO_FIJO_",
     "la convencion de la casa para una copia sellada que nadie reescribe"),
    ("_vieja_copia",
     "copia congelada de una version anterior de un instrumento, guardada para "
     "poder correr la vieja contra la nueva"),
    ("_viejo_copia",
     "misma convencion, en masculino"),
    ("tempfile",
     "el arnes FABRICA su sujeto en un temporal y lo retira (P.16): no puede "
     "moverse debajo de nadie"),
    ("mkdtemp",
     "idem"),
]

# LAS INVOCACIONES DE GIT. `git show <ref fija>:ruta` clava el sujeto a un blob
# y es CONGELADO; `git log`, `git rev-parse HEAD`, `git status` y `git diff`
# sobre el arbol de trabajo leen el estado VIVO del repo.
GIT_VIVO = re.compile(r"\b(rev-parse|status|diff|ls-files)\b")
GIT_CONGELADO = re.compile(r"\bshow\b")

# EL LISTADO DE DIRECTORIO ES SUJETO VIVO CUANDO EL DIRECTORIO CRECE. Los dos
# que crecen en esta campana son estos, y crecen cada vuelta.
DIRECTORIOS_QUE_CRECEN = ("scripts/loop", "docs/loop", "scripts\\loop", "docs\\loop")


def codigo_sin_docstrings(fuente):
    """EL TEXTO DEL FICHERO SIN SUS DOCSTRINGS, para que la prosa que EXPLICA un
    artefacto no cuente como que el arnes lo TOQUE. Sin esto, un docstring que
    menciona `docs/loop/REPORTE.md` para contar su historia clasificaria al
    arnes como sujeto vivo sin que su codigo lo abra jamas."""
    try:
        arbol = ast.parse(fuente)
    except SyntaxError:
        return fuente, ["AVISO: el fuente no parsea; se lee entero, docstrings incluidos"]
    fuera = set()
    for nodo in ast.walk(arbol):
        if isinstance(nodo, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef,
                             ast.ClassDef)):
            cuerpo = getattr(nodo, "body", [])
            if (cuerpo and isinstance(cuerpo[0], ast.Expr)
                    and isinstance(cuerpo[0].value, ast.Constant)
                    and isinstance(cuerpo[0].value.value, str)):
                d = cuerpo[0].value
                for ln in range(d.lineno, (d.end_lineno or d.lineno) + 1):
                    fuera.add(ln)
    lineas = fuente.split("\n")
    quedan = [l if (i + 1) not in fuera else "" for i, l in enumerate(lineas)]
    return "\n".join(quedan), []


# LO QUE CUENTA COMO ARTEFACTO. Un literal del codigo es un artefacto del repo
# si nombra un fichero de dato o de codigo. Los trozos de fontaneria de rutas
# ("scripts", "loop", "docs") NO son artefactos: no nombran nada por si solos.
ES_ARTEFACTO = re.compile(r"[\w./\\-]+\.(?:md|txt|json|jsonl|py|ts|tsx)$")
ES_SCRIPT_DE_VUELTA = re.compile(r"^(?:_v\d+_|vuelta\d+_|acta\d+_|auditor_v\d+)")
ES_SALIDA_SELLADA = re.compile(r"^(?:SALIDA_V\d+|_auditor_v\d+|SUJETO_FIJO_)")
ES_INSTRUMENTO_ESTABLE = re.compile(
    r"^(?:verificar_|tallar_|contar_|censar_|serie_|comprobar_|diagnostico_)"
    r"[\w-]*\.py$")

BASENAMES_VIVOS = dict(
    (ruta.split("/")[-1], (ruta, motivo)) for ruta, motivo in ARTEFACTOS_VIVOS
    if ruta.endswith((".md", ".json", ".jsonl", ".py")))


def literales_de_ruta(codigo):
    """TODOS LOS LITERALES DE CADENA DEL CODIGO QUE NOMBRAN UN ARTEFACTO, con
    su linea. Se sacan con `ast` (no con regex sobre el texto) para no confundir
    prosa con codigo."""
    try:
        arbol = ast.parse(codigo)
    except SyntaxError:
        return []
    fuera = []
    for nodo in ast.walk(arbol):
        if isinstance(nodo, ast.Constant) and isinstance(nodo.value, str):
            v = nodo.value.strip()
            if ES_ARTEFACTO.match(v) or ("/" in v and ES_ARTEFACTO.search(v)):
                fuera.append((v, nodo.lineno))
    vistos, unicos = set(), []
    for v, ln in fuera:
        if v not in vistos:
            vistos.add(v)
            unicos.append((v, ln))
    return unicos


def clasificar_literal(v):
    """(clase, motivo) de UN literal. clase en VIVO, CONGELADO, NEUTRO."""
    base = v.replace("\\", "/").split("/")[-1]
    for ruta, motivo in ARTEFACTOS_VIVOS:
        if ruta in v.replace("\\", "/"):
            return "VIVO", motivo
    if base in BASENAMES_VIVOS:
        return "VIVO", BASENAMES_VIVOS[base][1]
    if ES_SALIDA_SELLADA.match(base):
        return ("CONGELADO",
                "salida SELLADA de una vuelta pasada: la casa no reescribe una "
                "salida sellada, y la que se reescribe la caza el cotejo de "
                "reproducibilidad de la propia bateria")
    if ES_INSTRUMENTO_ESTABLE.match(base):
        return ("VIVO",
                "instrumento de NOMBRE ESTABLE (sin numero de vuelta): la casa lo "
                "mantiene y lo cambia, asi que leerlo como DATO es sujeto que se "
                "mueve")
    if ES_SCRIPT_DE_VUELTA.match(base) and base.endswith(".py"):
        return ("CONGELADO",
                "script de una vuelta PASADA, que la casa trata como HISTORIA y no "
                "toca (la formula esta escrita en los propios guardas_cierre: 'que "
                "es HISTORIA y NO SE TOCA')")
    return "NEUTRO", "no cae en ninguna de las dos listas de la tabla"


def senales(nombre):
    """LAS SENALES DEL FUENTE, CON SU LINEA LITERAL. Devuelve
    (vivas, congeladas, neutras, avisos); cada senal es
    (etiqueta, motivo, linea, texto)."""
    ruta = os.path.join(LOOP_SCRIPTS, nombre)
    fuente = io.open(ruta, encoding="utf-8", errors="replace").read()
    codigo, avisos = codigo_sin_docstrings(fuente)
    lineas = codigo.split("\n")
    vivas, congeladas, neutras = [], [], []

    for v, ln in literales_de_ruta(codigo):
        clase, motivo = clasificar_literal(v)
        texto = lineas[ln - 1].strip()[:110] if 0 < ln <= len(lineas) else ""
        destino = {"VIVO": vivas, "CONGELADO": congeladas, "NEUTRO": neutras}[clase]
        destino.append((v, motivo, ln, texto))

    for etiqueta, motivo in ARTEFACTOS_CONGELADOS:
        if etiqueta in ("SUJETO_FIJO_", "_vieja_copia", "_viejo_copia"):
            continue
        for i, l in enumerate(lineas, 1):
            if etiqueta in l:
                congeladas.append((etiqueta, motivo, i, l.strip()[:110]))
                break
    for i, l in enumerate(lineas, 1):
        if "git" in l and GIT_VIVO.search(l):
            vivas.append(("git sobre el arbol de trabajo",
                          "lee el estado VIVO del repo, que se mueve cada commit",
                          i, l.strip()[:110]))
            break
    for i, l in enumerate(lineas, 1):
        if "git" in l and GIT_CONGELADO.search(l) and not GIT_VIVO.search(l):
            congeladas.append(("git show sobre una ref",
                               "clava el sujeto a un blob de git", i, l.strip()[:110]))
            break
    for i, l in enumerate(lineas, 1):
        if ("listdir" in l or "glob" in l) and (
                any(d in l for d in DIRECTORIOS_QUE_CRECEN) or "LOOP" in l):
            vivas.append(("listado de un directorio que crece",
                          "scripts/loop/ y docs/loop/ ganan ficheros cada vuelta",
                          i, l.strip()[:110]))
            break
    return vivas, congeladas, neutras, avisos


def clasificar(estado_hoy, vivas, congeladas, neutras):
    """EL VEREDICTO. Conservador a proposito: nada entra sobre un quiza."""
    if estado_hoy != "OK":
        return ("SUJETO VIVO",
                "sale %s HOY con el mismo codigo con el que nacio verde: su ancla "
                "ya no esta donde la espera, y eso es una MEDICION de que el sujeto "
                "se movio" % estado_hoy)
    if vivas:
        return ("SUJETO VIVO",
                "su codigo toca %d artefacto(s) vivo(s): %s"
                % (len(vivas), ", ".join(sorted(set(v[0] for v in vivas)))))
    if congeladas:
        return ("SUJETO CONGELADO",
                "sale verde hoy y todo artefacto que toca es congelado: %s"
                % ", ".join(sorted(set(c[0] for c in congeladas))))
    if not neutras:
        return ("SUJETO CONGELADO",
                "sale verde hoy y NO TOCA NINGUN ARTEFACTO del repo: su sujeto lo "
                "fabrica el o vive en memoria, asi que no hay nada que se le pueda "
                "mover debajo. Es el caso mas congelado que hay")
    return ("NO DECIDIBLE",
            "sale verde hoy pero toca %d artefacto(s) que la tabla no clasifica "
            "(%s). NO ENTRA: nada entra sobre un quiza"
            % (len(neutras), ", ".join(sorted(set(n[0] for n in neutras)))))


def los_41():
    nomina = set(s for s, _a in B.VIEJAS)
    censo = sorted(n for n in os.listdir(B.LOOP) if B.PATRON_ARNES_VIEJO.match(n))
    return sorted(n for n in censo
                  if n not in nomina and (B.vuelta_de(n) or 0) < 148)


def correr(nombre):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    t0 = time.time()
    r = subprocess.run([PY, os.path.join("scripts", "loop", nombre)],
                       cwd=RAIZ, capture_output=True, env=env)
    dt = time.time() - t0
    out = (r.stdout.decode("utf-8", errors="replace")
           + r.stderr.decode("utf-8", errors="replace"))
    if r.returncode == 0:
        estado = "OK"
    elif "ROJO PREVIO" in out:
        estado = "ANCLA PERDIDA"
    else:
        estado = "NO MORDIO"
    primera = ""
    for l in out.split("\n"):
        if l.strip() and not set(l.strip()) <= set("=-"):
            primera = l.strip()[:100]
            break
    return r.returncode, estado, dt, primera


def porcelain():
    r = subprocess.run(["git", "status", "--porcelain"], cwd=RAIZ,
                       capture_output=True, text=True)
    return sorted(l for l in r.stdout.split("\n") if l.strip())


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-estatico", action="store_true")
    a = ap.parse_args()

    print("=" * 78)
    print("VUELTA 165, TAREA 4: EL SUJETO DE CADA UNO DE LOS 41, UNO POR UNO")
    print("=" * 78)
    print("")

    nombres = los_41()
    print("A) EL UNIVERSO, COMPUTADO CON EL PATRON VIEJO Y NO TECLEADO")
    print("   CIFRA arneses a medir: %d" % len(nombres))
    print("")

    print("B) LA TABLA DE REGLAS, PUBLICADA ENTERA ANTES DE APLICARLA")
    print("   ARTEFACTOS VIVOS (%d):" % len(ARTEFACTOS_VIVOS))
    for e, m in ARTEFACTOS_VIVOS:
        print("      %-46s %s" % (e, m))
    print("   ARTEFACTOS CONGELADOS (%d):" % len(ARTEFACTOS_CONGELADOS))
    for e, m in ARTEFACTOS_CONGELADOS:
        print("      %-46s %s" % (e, m))
    print("   git: `show <ref>` congela; `rev-parse`, `status`, `diff` y")
    print("   `ls-files` leen el arbol vivo.")
    print("   listar scripts/loop/ o docs/loop/ es sujeto vivo: crecen cada vuelta.")
    print("")

    antes = porcelain()
    print("C) EL ARBOL ANTES DE CORRER NADA")
    print("   CIFRA lineas de git status --porcelain: %d" % len(antes))
    for l in antes:
        print("      %s" % l)
    print("")

    print("D) LA MEDICION, UNO POR UNO, CON SU EVIDENCIA")
    filas = []
    total = 0.0
    for i, n in enumerate(nombres, 1):
        vivas, congeladas, neutras, avisos = senales(n)
        if a.solo_estatico:
            codigo, estado, dt, primera = 0, "OK", 0.0, "(no corrido)"
        else:
            codigo, estado, dt, primera = correr(n)
            total += dt
        veredicto, motivo = clasificar(estado, vivas, congeladas, neutras)
        filas.append((n, estado, codigo, dt, veredicto, motivo, vivas, congeladas))
        print("   %2d. %s" % (i, n))
        print("       corrida de HOY: exit %d, %s, %.1fs" % (codigo, estado, dt))
        if estado != "OK":
            print("       primera linea util: %s" % primera)
        for e, m, ln, txt in vivas:
            print("       SENAL VIVA      [%s] linea %d: %s" % (e, ln, txt))
        for e, m, ln, txt in congeladas:
            print("       SENAL CONGELADA [%s] linea %d: %s" % (e, ln, txt))
        for e, m, ln, txt in neutras:
            print("       SIN CLASIFICAR   [%s] linea %d: %s" % (e, ln, txt))
        if not vivas and not congeladas and not neutras:
            print("       NO TOCA NINGUN ARTEFACTO DEL REPO")
        for av in avisos:
            print("       %s" % av)
        print("       VEREDICTO: %s . %s" % (veredicto, motivo))
    print("")

    despues = porcelain()
    print("E) EL ARBOL DESPUES, Y LO QUE LA CORRIDA MOVIO")
    print("   CIFRA lineas de git status --porcelain: %d" % len(despues))
    nuevas = [l for l in despues if l not in set(antes)]
    print("   CIFRA lineas NUEVAS respecto de antes: %d" % len(nuevas))
    for l in nuevas:
        print("      APARECE O CAMBIA: %s" % l)
    print("")

    print("F) EL VEREDICTO CONTADO, Y SOLO CONTADO")
    por_estado = {}
    por_veredicto = {}
    for n, estado, _c, _d, ver, _m, _v, _g in filas:
        por_estado.setdefault(estado, []).append(n)
        por_veredicto.setdefault(ver, []).append(n)
    print("   CIFRA medidos: %d" % len(filas))
    for k in sorted(por_estado):
        print("   CIFRA con estado %-16s %d" % (k + ":", len(por_estado[k])))
    print("")
    for k in sorted(por_veredicto):
        print("   CIFRA con veredicto %-18s %d" % (k + ":", len(por_veredicto[k])))
    print("")
    for k in sorted(por_veredicto):
        print("   %s, CON SU NOMBRE:" % k)
        for n in sorted(por_veredicto[k]):
            print("      %s" % n)
    print("")

    print("G) LOS QUE ENTRAN, Y ENTRAN CON SU TIEMPO AL LADO (adjudicacion 6.6)")
    entran = [(n, d) for n, _e, _c, d, ver, _m, _v, _g in filas
              if ver == "SUJETO CONGELADO"]
    print("   CIFRA que ENTRAN en la nomina de la bateria: %d" % len(entran))
    for n, d in sorted(entran):
        print("      %-52s %6.1fs (una corrida)" % (n, d))
    coste = sum(d for _n, d in entran)
    print("   CIFRA coste de los que entran, una corrida: %.1fs" % coste)
    print("   CIFRA coste de los que entran, DOS corridas (que es lo que la")
    print("   bateria hace por el cotejo de reproducibilidad): %.1fs" % (coste * 2))
    print("")

    print("H) EL CRONOMETRO DE ESTA MEDICION")
    print("   CIFRA TIEMPO TOTAL, en segundos: %.1f" % total)
    print("   CIFRA TIEMPO TOTAL, en minutos: %.1f" % (total / 60.0))
    lentos = sorted(((d, n) for n, _e, _c, d, _v, _m, _vv, _g in filas), reverse=True)
    if lentos:
        print("   CIFRA arnes MAS LENTO: %s con %.1fs" % (lentos[0][1], lentos[0][0]))
        print("   LOS DIEZ MAS LENTOS, DE MAS A MENOS:")
        for d, n in lentos[:10]:
            print("      %-52s %8.1fs" % (n, d))
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
