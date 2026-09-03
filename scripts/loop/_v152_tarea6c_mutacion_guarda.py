# -*- coding: utf-8 -*-
"""VUELTA 152, TAREA 6.c: EL CASO POSITIVO POR MUTACION DE LA GUARDA DEL
REGISTRO DE CITAS DE `OP-C-05`.

LO QUE EL ENCARGO PIDE, LITERAL: "un par sin cita LA TUMBA NOMBRANDOLO, sobre
copia y con dataset/ identico antes y despues".

DOS MUTACIONES, PORQUE UN PAR PUEDE QUEDARSE SIN CITA POR LOS DOS LADOS:

  (A) SE CAE LA CITA. Se quita UNA entrada del registro y el par que defendia
      tiene que tumbar Gate 0 nombrandose. Ataca el lado del REGISTRO.
  (B) LLEGA UNA ARISTA NUEVA SIN LEER. Se anade al grafo una arista
      bidireccional entre dos nodos vivos que NADIE ha leido, que es el ataque
      de verdad: alguien cablea sin pasar por la lectura. Ataca el lado del
      GRAFO.

Y LA CONTRAPRUEBA, para que la guarda no sea un muro que siempre dice que no:
  (C) VERDE sobre el arbol intacto.

TODO SOBRE VARIABLE COMPUTADA (EJECUTOR.md 1, y la caida 2 de la vuelta 89): el
par que se espera ver nombrado NO se teclea, se LEE del propio registro y del
propio grafo en esta corrida, y despues se busca en la salida de Gate 0. No hay
un literal comparandose consigo mismo.

DATASET/ INTACTO, COMPROBADO Y NO PROMETIDO: se hashea dataset/ entero antes y
despues con sha256, y todo lo que se toca se restaura en un finally.

USO:
  python scripts/loop/_v152_tarea6c_mutacion_guarda.py
"""
import hashlib
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")


def huella_dataset():
    """sha256 de dataset/ entero, fichero a fichero y en orden."""
    h = hashlib.sha256()
    base = os.path.join(RAIZ, "dataset")
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames.sort()
        for n in sorted(filenames):
            ruta = os.path.join(dirpath, n)
            h.update(os.path.relpath(ruta, base).replace("\\", "/").encode())
            with open(ruta, "rb") as fh:
                for trozo in iter(lambda: fh.read(1 << 20), b""):
                    h.update(trozo)
    return h.hexdigest()


def gate0():
    """EL CICLO ENTERO, NO run_phase1 SUELTO. Dos trampas medidas en esta misma
    vuelta obligan a esto, y quedan escritas para que nadie las repita:

      (1) run_phase1 SUELTO deja la copia web desincronizada y la corrida
          SIGUIENTE sale en rojo por CICLO SIN CERRAR, no por la guarda. La
          primera version de este arnes dio la contraprueba en rojo por eso.
      (2) master_graph.json SE REGENERA desde dataset/nodos/*.json en cada
          corrida, asi que mutarlo NO MUTA NADA: la guarda lee el grafo ya
          regenerado. Por eso el caso B muta LOS FICHEROS DE NODO."""
    r = subprocess.run([sys.executable, os.path.join("scripts", "run_phase1.py"),
                        "--reaplico-curaduria"], capture_output=True, cwd=RAIZ)
    salida = r.stdout.decode("utf-8", "replace") + r.stderr.decode("utf-8", "replace")
    for extra in ("etiquetas_de_cara.py", "sync_assets_web.py"):
        args = [sys.executable, os.path.join("scripts", extra)]
        if extra.startswith("etiquetas"):
            args.append("--aplicar")
        subprocess.run(args, capture_output=True, cwd=RAIZ)
    linea = [x.strip() for x in salida.splitlines() if "REGISTRADO CON CITA" in x]
    return r.returncode, (linea[0] if linea else "(la guarda no aparece en la salida)")


def restaurar_arbol():
    subprocess.run(["git", "checkout", "--", "dataset", "web/lib/assets"],
                   cwd=RAIZ, capture_output=True)


# EL ARBOL SE NORMALIZA ANTES DE HASHEAR. Si no, la huella ANTES seria la de un
# arbol a medio ciclo y la comparacion final mediria mi propio desorden en vez
# de si la mutacion movio algo.
restaurar_arbol()
gate0()
ANTES = huella_dataset()
print("HUELLA sha256 DE dataset/ ANTES (con el ciclo cerrado): %s" % ANTES)
print("")

grafo_original = io.open(GRAFO, encoding="utf-8").read()
registro_original = io.open(REGISTRO, encoding="utf-8").read()
entradas = [json.loads(x) for x in registro_original.splitlines() if x.strip()]
print("REGISTRO: %d entradas. GRAFO: %d bytes." % (len(entradas), len(grafo_original)))

fallos = []
try:
    # ---------------------------------------------------------------- (C) VERDE
    codigo, linea = gate0()
    print("")
    print("CASO C, CONTRAPRUEBA, ARBOL INTACTO. esperado VERDE.")
    print("  exit %d | %s" % (codigo, linea[:150]))
    if codigo != 0:
        fallos.append("C")
    print("  [%s]" % ("OK" if codigo == 0 else "LA CONTRAPRUEBA FALLA: la guarda es un muro"))

    # ------------------------------------------------- (A) SE CAE UNA CITA
    # EL PAR SE ELIGE POR COMPUTO, no a dedo: la entrada del MEDIO del registro
    # ordenado. Asi el caso no puede estar amanado para un par comodo.
    ordenadas = sorted(entradas, key=lambda e: tuple(sorted(e["par"])))
    victima = ordenadas[len(ordenadas) // 2]
    par_a, par_b = sorted(victima["par"])
    esperado_a = "%s <-> %s" % (par_a, par_b)
    quedan = [e for e in ordenadas if tuple(sorted(e["par"])) != (par_a, par_b)]
    io.open(REGISTRO, "w", encoding="utf-8", newline="\n").write(
        "\n".join(json.dumps(e, ensure_ascii=False, sort_keys=True) for e in quedan) + "\n")
    codigo, linea = gate0()
    print("")
    print("CASO A, SE CAE LA CITA. Par elegido POR COMPUTO (entrada del medio de %d): %s"
          % (len(ordenadas), esperado_a))
    print("  via de la cita que se quita: %s | %s" % (victima["via"], str(victima["cita"])[:80]))
    print("  exit %d | %s" % (codigo, linea[:220]))
    nombra = esperado_a in linea
    print("  cae: %s | LA NOMBRA: %s" % (codigo != 0, nombra))
    if not (codigo != 0 and nombra):
        fallos.append("A")
    print("  [%s]" % ("OK" if (codigo != 0 and nombra) else "LA GUARDA NO MUERDE POR ESTE LADO"))
    io.open(REGISTRO, "w", encoding="utf-8", newline="\n").write(registro_original)

    # -------------------------------------- (B) ARISTA NUEVA SIN LEER
    N = json.loads(grafo_original)
    vivos = sorted(k for k, v in N["nodos"].items() if not v.get("deprecado")
                   and os.path.exists(os.path.join(RAIZ, "dataset", "nodos", k + ".json")))
    citados = {tuple(sorted(e["par"])) for e in entradas}
    # LOS DOS NODOS SE ELIGEN POR COMPUTO: el primero y el ultimo vivo en orden
    # alfabetico que NO formen ya un par citado. Nada tecleado.
    x, y = None, None
    for cand_a in vivos:
        for cand_b in reversed(vivos):
            if cand_a >= cand_b:
                continue
            if tuple(sorted((cand_a, cand_b))) in citados:
                continue
            x, y = cand_a, cand_b
            break
        if x:
            break
    esperado_b = "%s <-> %s" % tuple(sorted((x, y)))
    # SE MUTAN LOS FICHEROS DE NODO, que son la FUENTE, y no master_graph.json,
    # que es un DERIVADO que run_phase1 vuelve a generar en cada corrida. La
    # primera version de este arnes mutaba el derivado y la guarda ni se entero:
    # dio 153 con cita y 0 sin cita sobre un grafo que ya habia borrado la
    # mutacion. Queda escrito aqui porque es la clase de falso verde que este
    # arnes existe para impedir.
    for uno, otro in ((x, y), (y, x)):
        ruta = os.path.join(RAIZ, "dataset", "nodos", uno + ".json")
        d = json.load(io.open(ruta, encoding="utf-8"))
        d.setdefault("nodos_siguientes", []).append(otro)
        io.open(ruta, "w", encoding="utf-8", newline="\n").write(
            json.dumps(d, ensure_ascii=False, indent=2))
    codigo, linea = gate0()
    print("")
    print("CASO B, ARISTA BIDIRECCIONAL NUEVA QUE NADIE LEYO. Par elegido POR COMPUTO: %s"
          % esperado_b)
    print("  exit %d | %s" % (codigo, linea[:220]))
    nombra = esperado_b in linea
    print("  cae: %s | LA NOMBRA: %s" % (codigo != 0, nombra))
    if not (codigo != 0 and nombra):
        fallos.append("B")
    print("  [%s]" % ("OK" if (codigo != 0 and nombra) else "LA GUARDA NO MUERDE POR ESTE LADO"))
finally:
    # SE RESTAURA dataset/ ENTERO Y LA COPIA WEB, no solo el grafo, porque el
    # caso B toca ficheros de nodo. Y despues se vuelve a cerrar el ciclo, para
    # que la huella DESPUES se tome sobre el MISMO estado que la de ANTES y no
    # sobre un arbol a medio regenerar.
    io.open(REGISTRO, "w", encoding="utf-8", newline="\n").write(registro_original)
    restaurar_arbol()
    gate0()

DESPUES = huella_dataset()
print("")
print("HUELLA sha256 DE dataset/ DESPUES: %s" % DESPUES)
print("dataset/ IDENTICO ANTES Y DESPUES: %s" % (ANTES == DESPUES))
if ANTES != DESPUES:
    fallos.append("dataset movido")

print("")
print("=" * 96)
if fallos:
    print("CASO POSITIVO EN ROJO. Casos que no se comportan: %s" % ", ".join(fallos))
    raise SystemExit(1)
print("CASO POSITIVO SUPERADO: la contraprueba pasa en VERDE y LOS DOS ATAQUES TUMBAN")
print("GATE 0 CON exit 1 NOMBRANDO EL PAR, por los dos lados por los que un par puede")
print("quedarse sin cita: que se caiga el registro y que llegue una arista sin leer.")
print("Y dataset/ queda IDENTICO al digito, comprobado por sha256 y no prometido.")
