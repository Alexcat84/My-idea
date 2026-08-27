# -*- coding: utf-8 -*-
r"""vuelta98_tarea3_prueba_mutacion.py . VUELTA 98, TAREA 3: PRUEBA DE MUTACION
DE LAS GUARDAS DEL RECOMPUTO DEL PAR 42.

POR QUE ES OBLIGATORIA (EJECUTOR.md regla 1, EL CASO ROJO SE PRUEBA POR
MUTACION). El instrumento de la TAREA 3 publica cinco guardas como prueba de que
el recomputo no puede escribir sobre un estado que no es el que dice. Ninguna se
publica sin haber comprobado que CAE cuando se le cambia el valor esperado.

COMO SE MUTA SIN TOCAR EL REPO: se copian a un directorio temporal los CUATRO
ficheros del estado ANTERIOR (leidos de `git show HEAD~1:` o de la ref que se
pase con --base), se muta UNA cosa en la copia, se apuntan a esa copia las rutas
del modulo, y se corre `--medir`. El arbol de trabajo no se toca en ningun caso.

  C1  control: el estado ANTES del cambio                    espera EXIT 0
  C2  control: el arbol de trabajo de HOY, ya cambiado       espera EXIT 1 (idempotencia)
  M1  la fila 42 puesta en D en la copia                     espera EXIT 1
  M2  el par 12 del tramo 1 puesto en D                      espera EXIT 1
  M3  la frase de RESULTADO duplicada en la nota             espera EXIT 1
  M4  la fila "clase A, REPITE 3" borrada de 04_ENLACES.md   espera EXIT 1
  M5  la marca de correccion ya presente en la razon del 42  espera EXIT 1
  M6  la marca de LECTURA DIRIGIDA rota en la fila 42        espera EXIT 1
  M7  la guarda de direccion: se fuerza que el recuento de
      DESPUES difiera del de ANTES y se corre --aplicar       espera EXIT 1 y CERO escritura

LO QUE NO TIENE CASO ROJO AUTOMATICO, Y SE DECLARA EN VEZ DE FABRICARLO
(EJECUTOR.md regla 1, la letra del 29 ago 2026 nacida de la caida 2 de la vuelta
89): LA CLASE DEL PAR 42 EN SI. Que el par sea A o D es una LECTURA a mano
contra el grafo, y no hay dentro del repo una segunda fuente independiente
contra la que contrastarla. NO HAY NADA QUE MUTAR AHI, y por eso NO se fabrica
un caso rojo que se apruebe solo. Su control es la relectura ciega del auditor,
no un assert. Lo que estas mutaciones prueban es que el RECOMPUTO no escribe
sobre un estado equivocado, que es cosa distinta y menor.

USO:
  python scripts/loop/vuelta98_tarea3_prueba_mutacion.py
  python scripts/loop/vuelta98_tarea3_prueba_mutacion.py --base HEAD~1
"""
import argparse
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")

RUTAS = {
    "TRAMO2": "docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl",
    "TRAMO1": "docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl",
    "OPERACIONES": "docs/plan/OPERACIONES.jsonl",
    "ENLACES": "docs/plan/04_ENLACES.md",
}

RESULTADOS = []


def cargar_modulo():
    ruta = os.path.join(LOOP, "vuelta98_tarea3_relectura_par42.py")
    spec = importlib.util.spec_from_file_location("v98t3", ruta)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["v98t3"] = mod
    spec.loader.exec_module(mod)
    return mod


def texto_de(ref, ruta):
    r = subprocess.run(["git", "show", "%s:%s" % (ref, ruta)],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO: no se pudo leer %s:%s" % (ref, ruta))
    return r.stdout.decode("utf-8")


def correr(mod, dirtmp, modo="--medir"):
    """Apunta el modulo a las copias del directorio y corre el modo pedido."""
    for nombre, rel in RUTAS.items():
        setattr(mod, nombre, os.path.join(dirtmp, os.path.basename(rel)))
    argv = sys.argv
    salida = io.StringIO()
    stdout = sys.stdout
    try:
        sys.argv = ["x", modo]
        sys.stdout = salida
        try:
            code = mod.main()
        except SystemExit as e:
            code = e.code if isinstance(e.code, int) else 1
    finally:
        sys.argv = argv
        sys.stdout = stdout
    return code, salida.getvalue()


def preparar(ref):
    d = tempfile.mkdtemp(prefix="v98t3_")
    for rel in RUTAS.values():
        io.open(os.path.join(d, os.path.basename(rel)), "w",
                encoding="utf-8", newline="\n").write(texto_de(ref, rel))
    return d


def preparar_work():
    d = tempfile.mkdtemp(prefix="v98t3w_")
    for rel in RUTAS.values():
        shutil.copyfile(os.path.join(RAIZ, rel),
                        os.path.join(d, os.path.basename(rel)))
    return d


def leer_jsonl(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def escribir_jsonl(p, filas):
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        for x in filas:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")


def caso(nombre, descripcion, esperado, obtenido):
    ok = (esperado == obtenido)
    RESULTADOS.append((nombre, descripcion, esperado, obtenido, ok))
    print("  %-4s %-58s espera EXIT %d   obtiene EXIT %d   %s"
          % (nombre, descripcion, esperado, obtenido, "OK" if ok else "FALLA"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="HEAD",
                    help="ref del estado ANTERIOR al cambio (por defecto HEAD)")
    a = ap.parse_args()

    mod = cargar_modulo()
    print("=" * 118)
    print("PRUEBA DE MUTACION, VUELTA 98 TAREA 3 (recomputo del par 42)")
    print("=" * 118)
    print("BASE del estado anterior: %s" % a.base)
    print()

    # C1: control, el estado ANTES
    d = preparar(a.base)
    code, _ = correr(mod, d)
    caso("C1", "control: el estado ANTES del cambio", 0, code)

    # C2: control, el arbol de trabajo de HOY (ya cambiado)
    dw = preparar_work()
    code, _ = correr(mod, dw)
    caso("C2", "control: el arbol de trabajo de HOY, ya cambiado", 1, code)

    # M1: la fila 42 puesta en D
    d = preparar(a.base)
    p = os.path.join(d, "OP_E_03_LECTURA_TRAMO2_V97.jsonl")
    fs = leer_jsonl(p)
    [f for f in fs if f["puesto_tramo"] == 42][0]["clase"] = "D"
    escribir_jsonl(p, fs)
    code, _ = correr(mod, d)
    caso("M1", "mutada la fila 42 a clase D", 1, code)

    # M2: el par 12 del tramo 1 puesto en D
    d = preparar(a.base)
    p = os.path.join(d, "OP_E_03_LECTURA_TRAMO1_V96.jsonl")
    fs = leer_jsonl(p)
    [f for f in fs if f["puesto_tramo"] == 12][0]["clase"] = "D"
    escribir_jsonl(p, fs)
    code, _ = correr(mod, d)
    caso("M2", "mutado el par 12 del tramo 1 a clase D", 1, code)

    # M3: la frase de RESULTADO duplicada en la nota
    d = preparar(a.base)
    p = os.path.join(d, "OPERACIONES.jsonl")
    ops = leer_jsonl(p)
    o = [x for x in ops if x.get("id_op") == "OP-E-03"][0]
    frase = "RESULTADO: A 3, B 1, C 0, D 56. Los tres A son los pares 42, 88, 100."
    o["nota"] = o["nota"] + " " + frase
    escribir_jsonl(p, ops)
    code, _ = correr(mod, d)
    caso("M3", "duplicada la frase de RESULTADO en la nota", 1, code)

    # M4: la fila de clase A borrada de 04_ENLACES.md
    d = preparar(a.base)
    p = os.path.join(d, "04_ENLACES.md")
    t = io.open(p, encoding="utf-8").read()
    io.open(p, "w", encoding="utf-8", newline="\n").write(
        t.replace("| clase A, REPITE | **3** |", "| clase A, REPITE | **9** |", 1))
    code, _ = correr(mod, d)
    caso("M4", "borrada la fila 'clase A, REPITE 3' de 04_ENLACES.md", 1, code)

    # M5: la marca de correccion ya presente en la razon del 42
    d = preparar(a.base)
    p = os.path.join(d, "OP_E_03_LECTURA_TRAMO2_V97.jsonl")
    fs = leer_jsonl(p)
    f42 = [f for f in fs if f["puesto_tramo"] == 42][0]
    f42["razon"] = f42["razon"] + " " + mod.MARCA
    escribir_jsonl(p, fs)
    code, _ = correr(mod, d)
    caso("M5", "la marca de correccion ya presente en la razon del 42", 1, code)

    # M6: la marca de LECTURA DIRIGIDA rota en la fila 42
    d = preparar(a.base)
    p = os.path.join(d, "OP_E_03_LECTURA_TRAMO2_V97.jsonl")
    fs = leer_jsonl(p)
    [f for f in fs if f["puesto_tramo"] == 42][0]["fuera_de_la_cola"] = False
    escribir_jsonl(p, fs)
    code, _ = correr(mod, d)
    caso("M6", "rota la marca de LECTURA DIRIGIDA en la fila 42", 1, code)

    # M7: la guarda de direccion. Se fuerza que el recuento de DESPUES difiera
    # del de ANTES envolviendo cuentas(), y se corre --aplicar sobre la copia.
    d = preparar(a.base)
    original = mod.cuentas
    estado = {"n": 0}

    def cuentas_mutada(filas):
        estado["n"] += 1
        c, aa, bb, con_dir, sin_dir = original(filas)
        if estado["n"] >= 2:          # la 1.a llamada es el ANTES; a partir de la 2.a, el DESPUES
            con_dir = con_dir - 1     # se le quita una direccion afirmada
        return c, aa, bb, con_dir, sin_dir

    antes = io.open(os.path.join(d, "OP_E_03_LECTURA_TRAMO2_V97.jsonl"),
                    encoding="utf-8").read()
    mod.cuentas = cuentas_mutada
    try:
        code, _ = correr(mod, d, "--aplicar")
    finally:
        mod.cuentas = original
    despues = io.open(os.path.join(d, "OP_E_03_LECTURA_TRAMO2_V97.jsonl"),
                      encoding="utf-8").read()
    caso("M7", "mutada la guarda de direccion: el DESPUES difiere del ANTES", 1, code)
    sin_escribir = (antes == despues)
    RESULTADOS.append(("M7b", "y ademas NO escribio nada", True, sin_escribir,
                       sin_escribir))
    print("  %-4s %-58s espera %-14s obtiene %-14s %s"
          % ("M7b", "y ademas NO escribio nada", "sin escribir",
             "sin escribir" if sin_escribir else "ESCRIBIO",
             "OK" if sin_escribir else "FALLA"))

    print()
    fallan = [r for r in RESULTADOS if not r[4]]
    mut = [r for r in RESULTADOS if r[0].startswith("M")]
    con = [r for r in RESULTADOS if r[0].startswith("C")]
    print("RECUENTO, contado de los propios casos corridos:")
    print("   casos totales      %d" % len(RESULTADOS))
    print("   controles          %d, como se esperaba %d"
          % (len(con), sum(1 for r in con if r[4])))
    print("   mutaciones         %d, como se esperaba %d"
          % (len(mut), sum(1 for r in mut if r[4])))
    print("   casos que FALLAN   %d" % len(fallan))
    print()
    print("DECLARADO, y no fabricado: LA CLASE DEL PAR 42 (A contra D) es una lectura a")
    print("mano contra el grafo y NO TIENE CASO ROJO AUTOMATICO, porque no hay en el repo")
    print("una segunda fuente independiente contra la que contrastarla. Su control es la")
    print("relectura ciega del auditor. Estas mutaciones prueban el RECOMPUTO, no la clase.")
    print()
    if fallan:
        print("ROJO: %d caso(s) no se comportan como se espera." % len(fallan))
        for r in fallan:
            print("   %s %s: esperaba %r y obtuvo %r" % (r[0], r[1], r[2], r[3]))
        return 1
    print("VERDE: los %d controles pasan y las %d mutaciones tumban el instrumento."
          % (len(con), len(mut)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
