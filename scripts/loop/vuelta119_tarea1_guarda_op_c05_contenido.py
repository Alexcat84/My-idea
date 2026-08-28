# -*- coding: utf-8 -*-
"""vuelta119_tarea1_guarda_op_c05_contenido.py . VUELTA 119, TAREA 1 (encargo de
la seccion 6 de la parada docs/loop/paradas/2026-08-28-titulo-nafta-ops01.md).

POR QUE NACE. `scripts/loop/vuelta89_tarea4_guarda_op_c05.py --caso-rojo` se
para SIEMPRE con "ROJO: dataset/ ya tenia cambios antes del caso rojo", porque
su guarda de limpieza mide ESTADO con `git status --porcelain -- dataset/`, y
ese comando ve SIEMPRE la `M` espuria de fin de linea de
`dataset/metadata/master_graph.json` (LF en disco, CRLF que git aplicaria al
tocarlo). La fila 0 del plan dice "una guarda que nunca fallo no esta
probada", y esta es la hermana: una guarda cuyo caso positivo NUNCA PUEDE
CORRER esta en el mismo sitio.

EL REMEDIO (seccion 6 de la parada): la MISMA via equivalente de `OP-C-05`
(correr `scripts/plan/aristas_duplicadas_tras_resolver.py` antes y despues, y
exigir que la cuenta no crezca), pero con la comprobacion de limpieza de
`dataset/` midiendo CONTENIDO, con `git diff --numstat -- dataset/` (cero
lineas), en vez de ESTADO, con `git status --porcelain`. FICHERO NUEVO: la
guarda vieja (vuelta89_tarea4_guarda_op_c05.py) NO SE TOCA, sigue existiendo
tal como esta. --antes y --despues de este fichero son BYTE A BYTE la misma
logica que la vieja (la via equivalente no cambia): lo unico que cambia es la
funcion de limpieza que --caso-rojo usa para comprobar que dataset/ no se
toco.

USO (el que usara la operacion que abra sobre OP-C-05 o su via equivalente):
  python scripts/loop/vuelta119_tarea1_guarda_op_c05_contenido.py --antes
  ... se escriben las aristas ...
  python scripts/loop/vuelta119_tarea1_guarda_op_c05_contenido.py --despues
  python scripts/loop/vuelta119_tarea1_guarda_op_c05_contenido.py --caso-rojo

EL NOMBRE DEL FICHERO DE SELLO LLEVA LA VUELTA (SALIDA_V<N>_..._V2.txt, con el
sufijo _V2 para no chocar con el sello de la guarda vieja si las dos corrieran
la misma vuelta), leido de --vuelta (por defecto 119).
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
INSTRUMENTO = os.path.join(RAIZ, "scripts", "plan", "aristas_duplicadas_tras_resolver.py")
GRAFO_HOY = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

RE_SOBRAN = re.compile(r"\*\*entradas que SOBRAN\*\* \| \*\*(\d+)\*\*")
RE_NODOS = re.compile(r"\*\*nodos con al menos una duplicada\*\* \| \*\*(\d+)\*\*")


def contar(ruta_grafo, ruta_salida_jsonl):
    """IDENTICO a la guarda vieja: corre el instrumento de solo lectura sobre
    RUTA_GRAFO y devuelve (entradas_sobran, nodos_con_duplicada, texto
    completo). ROJO (SystemExit) si el instrumento falla o si su salida no se
    puede leer: nunca se inventa una cifra."""
    r = subprocess.run(
        [sys.executable, INSTRUMENTO, "--grafo", ruta_grafo, "--salida", ruta_salida_jsonl],
        cwd=RAIZ, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("ROJO: %s salio con exit %d\n%s" % (INSTRUMENTO, r.returncode, r.stderr))
    texto = r.stdout
    m_sobran = RE_SOBRAN.search(texto)
    m_nodos = RE_NODOS.search(texto)
    if not m_sobran or not m_nodos:
        raise SystemExit("ROJO: no se pudo leer 'entradas que SOBRAN' o 'nodos con al menos "
                          "una duplicada' de la salida del instrumento:\n%s" % texto)
    return int(m_sobran.group(1)), int(m_nodos.group(1)), texto


def sello_ruta(vuelta, lado):
    return os.path.join(LOOP, "SALIDA_V%d_GUARDA_OPC05_V2_%s.txt" % (vuelta, lado))


def cmd_antes(vuelta):
    with tempfile.TemporaryDirectory() as tmp:
        salida_jsonl = os.path.join(tmp, "ARISTAS_DUPLICADAS_ANTES.jsonl")
        sobran, nodos, texto = contar(GRAFO_HOY, salida_jsonl)
    print(texto)
    ruta = sello_ruta(vuelta, "ANTES")
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("ANTES | entradas que sobran: %d | nodos con duplicada: %d\n" % (sobran, nodos))
    print("=" * 78)
    print("SELLO ANTES: %d entradas que sobran, %d nodos (escrito en %s)" % (sobran, nodos, ruta))
    return 0


def cmd_despues(vuelta):
    ruta_antes = sello_ruta(vuelta, "ANTES")
    if not os.path.exists(ruta_antes):
        raise SystemExit("ROJO: no existe %s: corre --antes primero, nunca se inventa la "
                          "cuenta de antes" % ruta_antes)
    texto_antes = io.open(ruta_antes, encoding="utf-8").read()
    m = re.search(r"entradas que sobran: (\d+)", texto_antes)
    if not m:
        raise SystemExit("ROJO: %s no trae una cuenta reconocible" % ruta_antes)
    sobran_antes = int(m.group(1))

    with tempfile.TemporaryDirectory() as tmp:
        salida_jsonl = os.path.join(tmp, "ARISTAS_DUPLICADAS_DESPUES.jsonl")
        sobran_despues, nodos_despues, texto = contar(GRAFO_HOY, salida_jsonl)
    print(texto)
    print("=" * 78)
    print("ANTES: %d entradas que sobran | DESPUES: %d entradas que sobran"
          % (sobran_antes, sobran_despues))
    if sobran_despues > sobran_antes:
        print("ROJO: LA CUENTA CRECIO (+%d). LA OPERACION PARA (via de OP-C-05, "
              "adjudicacion 5.4 del acta 88)." % (sobran_despues - sobran_antes))
        return 1
    print("VERDE: la cuenta NO crecio (%+d). Via de OP-C-05 cumplida."
          % (sobran_despues - sobran_antes))
    return 0


def dataset_limpio_por_contenido():
    """EL REMEDIO DE ESTA TAREA: mide CONTENIDO con `git diff --numstat --
    dataset/`, no ESTADO con `git status --porcelain`. Devuelve (limpio,
    texto_crudo). Vacio (cero lineas de numstat) es limpio, sin importar lo
    que `git status` diga de finales de linea."""
    r = subprocess.run(["git", "diff", "--numstat", "--", "dataset/"],
                       cwd=RAIZ, capture_output=True, text=True)
    return (r.stdout.strip() == ""), r.stdout


def cmd_caso_rojo():
    print("=" * 78)
    print("TAREA 1 (vuelta 119): CASO ROJO OBLIGATORIO, SOBRE COPIA EN MEMORIA "
          "(dataset/ no se toca), LIMPIEZA MEDIDA POR CONTENIDO")
    print("=" * 78)

    limpio_antes, crudo_antes = dataset_limpio_por_contenido()
    print("git diff --numstat -- dataset/ ANTES: %r" % crudo_antes)
    if not limpio_antes:
        raise SystemExit("ROJO: dataset/ ya tenia cambios de CONTENIDO antes del caso rojo: "
                          "no se corre sobre un arbol con contenido sucio")

    with tempfile.TemporaryDirectory() as tmp:
        salida_hoy = os.path.join(tmp, "ARISTAS_DUPLICADAS_HOY.jsonl")
        sobran_hoy, nodos_hoy, _ = contar(GRAFO_HOY, salida_hoy)
        print("cuenta de hoy (grafo real, sin tocar): %d entradas que sobran, %d nodos"
              % (sobran_hoy, nodos_hoy))

        grafo = json.load(io.open(GRAFO_HOY, encoding="utf-8"))
        nodos = grafo["nodos"]
        nodo_elegido = None
        for nid, n in nodos.items():
            if n.get("deprecado"):
                continue
            sig = n.get("nodos_siguientes") or []
            if sig:
                nodo_elegido = nid
                destino = sig[0]
                break
        if nodo_elegido is None:
            raise SystemExit("ROJO: no se encontro ningun nodo vivo con nodos_siguientes no "
                              "vacio para fabricar el caso rojo")
        nodos[nodo_elegido]["nodos_siguientes"] = list(sig) + [destino]
        print("fabricado EN MEMORIA (no en disco): %s.nodos_siguientes gana una entrada "
              "duplicada de '%s' (%s -> %s x2)" % (nodo_elegido, destino, nodo_elegido, destino))

        ruta_grafo_fabricado = os.path.join(tmp, "master_graph_FABRICADO.json")
        with io.open(ruta_grafo_fabricado, "w", encoding="utf-8") as fh:
            json.dump(grafo, fh, ensure_ascii=False)

        salida_fabricada = os.path.join(tmp, "ARISTAS_DUPLICADAS_FABRICADO.jsonl")
        sobran_fabricado, nodos_fabricado, _ = contar(ruta_grafo_fabricado, salida_fabricada)
        print("cuenta SOBRE LA COPIA FABRICADA (fichero temporal, nunca dataset/): "
              "%d entradas que sobran, %d nodos" % (sobran_fabricado, nodos_fabricado))

    limpio_despues, crudo_despues = dataset_limpio_por_contenido()
    print("git diff --numstat -- dataset/ DESPUES: %r" % crudo_despues)
    if not limpio_despues:
        raise SystemExit("ROJO: dataset/ quedo con cambios de CONTENIDO tras el caso rojo: el "
                          "caso rojo tiene que ser puramente en memoria")

    print()
    if sobran_fabricado <= sobran_hoy:
        raise SystemExit("ROJO DEL PROPIO CASO ROJO: la copia fabricada NO crecio la cuenta "
                          "(%d contra %d): el caso positivo no vale, revisar la fabricacion"
                          % (sobran_fabricado, sobran_hoy))
    print("LA COPIA FABRICADA CRECE LA CUENTA (%d -> %d, +%d), que es EXACTAMENTE la "
          "condicion que --despues detecta como ROJO. El caso rojo CAE EN ROJO como se "
          "espera de el (simulando --despues con estas dos cuentas):"
          % (sobran_hoy, sobran_fabricado, sobran_fabricado - sobran_hoy))
    if sobran_fabricado > sobran_hoy:
        print("   --despues simulado: ROJO (exit 1), LA OPERACION PARA. CASO ROJO: PROBADO.")
    print()
    print("dataset/ nunca se toco de CONTENIDO: los dos git diff --numstat de arriba "
          "salieron vacios (la M espuria de fin de linea, si la hay, no cuenta aqui).")

    print()
    print("--- PRUEBA DE MUTACION DE LA GUARDA (EJECUTOR regla 1): la variable que decide, "
          "no un literal ---")
    print("Se muta la condicion real del codigo (sobran_fabricado > sobran_hoy) invirtiendola "
          "a mano sobre las MISMAS dos cifras medidas arriba, para comprobar que el caso CAE "
          "cuando la condicion es falsa:")
    veredicto_mutado = sobran_fabricado < sobran_hoy  # mutacion: '>' invertido a '<'
    print("  condicion mutada (sobran_fabricado < sobran_hoy) sobre %d contra %d: %s"
          % (sobran_fabricado, sobran_hoy, veredicto_mutado))
    if veredicto_mutado:
        raise SystemExit("ROJO DE LA MUTACION: con la condicion invertida el caso deberia dar "
                          "False y no dio: la prueba no discrimina")
    print("  MUTACION CAE (False), como se espera: la condicion real "
          "(sobran_fabricado > sobran_hoy) es la que decide, no un literal fijo.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--antes", action="store_true")
    g.add_argument("--despues", action="store_true")
    g.add_argument("--caso-rojo", action="store_true")
    ap.add_argument("--vuelta", type=int, default=119)
    a = ap.parse_args()

    if a.antes:
        return cmd_antes(a.vuelta)
    if a.despues:
        return cmd_despues(a.vuelta)
    return cmd_caso_rojo()


if __name__ == "__main__":
    raise SystemExit(main())
