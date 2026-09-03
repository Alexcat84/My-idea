# -*- coding: utf-8 -*-
"""vuelta89_tarea4_guarda_op_c05.py . VUELTA 89, TAREA 4 (adjudicacion 5.4 del
acta de la vuelta 88). LA VIA EQUIVALENTE DE `OP-C-05`, CABLEADA Y PROBADA.

POR QUE NACE. La `verificacion` de `OP-E-06` exige terminar "por la guarda
`OP-C-05`", pero esa guarda NO EXISTE en el codigo (ni en Gate 0 ni en los
`engine/test_gate_*.py`): la propia ficha de `OP-C-05` dice por escrito que
"esta guarda se enciende DESPUES del saneo final [`OP-S-12`]" y que el grafo
de hoy la falla y **eso no es una regresion** (adjudicacion 5.4 del acta de
la vuelta 88). Este instrumento ejecuta la VIA EQUIVALENTE que la propia
ficha autoriza: correr `scripts/plan/aristas_duplicadas_tras_resolver.py`
ANTES y DESPUES de escribir una operacion, y exigir que LA CUENTA NO CREZCA.
Si crece, la operacion para. Esto NO inventa `OP-C-05`: la ejecuta por la
via que su propia ficha deja abierta.

ESTRICTAMENTE DE SOLO LECTURA sobre `dataset/`: nunca escribe un nodo. Solo
escribe en `docs/loop/` (el sello de la cuenta de ANTES, para que DESPUES
pueda leerlo) y, en `--caso-rojo`, en un fichero temporal fuera del repo
(nunca en `dataset/`).

USO (el que usara la vuelta 90 al abrir `OP-E-06`):
  python scripts/loop/vuelta89_tarea4_guarda_op_c05.py --antes
      (corre el instrumento sobre dataset/metadata/master_graph.json de HOY,
      sella la cuenta en docs/loop/SALIDA_V<N>_GUARDA_OPC05_ANTES.txt)
  ... se escriben las aristas de OP-E-06 ...
  python scripts/loop/vuelta89_tarea4_guarda_op_c05.py --despues
      (vuelve a correr el instrumento, compara contra el sello: VERDE y
      exit 0 si la cuenta NO crecio; ROJO y exit 1, LA OPERACION PARA, si
      crecio)

TAREA 4.b, CASO ROJO OBLIGATORIO:
  python scripts/loop/vuelta89_tarea4_guarda_op_c05.py --caso-rojo
      (sobre una COPIA EN MEMORIA del grafo de hoy, mete una entrada
      duplicada tras resolver en un nodo vivo, la escribe a un fichero
      TEMPORAL fuera de dataset/, corre el instrumento sobre ese temporal, y
      comprueba que la cuenta despues es mayor que la cuenta de hoy: la
      MISMA condicion que hace caer --despues en rojo. git status
      --porcelain -- dataset/ se imprime vacio antes y despues, para dejar
      constancia de que dataset/ nunca se toco.)

EL NOMBRE DEL FICHERO DE SELLO LLEVA LA VUELTA (SALIDA_V<N>_...), leida de
--vuelta (por defecto 89): asi el sello de una vuelta no lo pisa el de la
siguiente, y `--despues` de la vuelta 90 lee el `--antes` que la vuelta 90
haya sellado, no el de esta.

--- ADJUDICACION 6.7 DEL ACTA 158 (3 sep 2026): EL CHECK DE P.16 SE CINE AL
CONTENIDO Y A LA VENTANA DEL PROPIO SCRIPT ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra, y el check que este
fichero lleva NO se modifica al escribir esto: esto es la adjudicacion, no el
remedio.

LAS DOS ANCLAS QUE SE MUEVEN EN LA MISMA LINEA, y el hallazgo es del ejecutor de
la vuelta 157, que lo trajo como pregunta en vez de esquivarlo callando. El
docstring dice que se comprueba que `dataset/` y `docs/plan/` NO SE TOCAN NI UNA
VEZ, o sea CONTENIDO. El instrumento es `git status --porcelain`, que ademas de
contenido ve:
  (i)  ESTADO DE FIN DE LINEA. Este repo tiene `core.autocrlf`, asi que un
       fichero reescrito por el ciclo queda marcado como modificado aunque su
       sha256 NORMALIZADO sea identico al de HEAD. Paso de verdad en la vuelta
       157 y tumbo tres mutaciones de la bateria en ROJO con el contenido
       intacto.
  (ii) SUCIEDAD ANTERIOR AL ARRANQUE DEL SCRIPT, que no es suya. El veredicto de
       este check depende de si alguien committeo tocando `dataset/` antes, y no
       de si las mutaciones de este fichero tocaron el dataset.

EL REMEDIO ADJUDICADO: huella de CONTENIDO tomada ANTES y DESPUES de las
mutaciones DENTRO del propio script, y comparada consigo misma. Con su caso
positivo por mutacion: si una mutacion escribe de verdad en `dataset/` o en
`docs/plan/`, el check SIGUE SALIENDO ROJO.

EL ALCANCE, Y AQUI HAY UNA DISCREPANCIA DE CIFRA QUE SE DECLARA EN VEZ DE
COPIARSE: el acta 158 mide ONCE ficheros con el patron literal, siete de ellos
dentro de la bateria de las 23. El recomputo de la vuelta 159
(`scripts/loop/vuelta159_tarea1_registrar_adjudicaciones.py`, funcion
`ficheros_con_patron_p16`, salida `docs/loop/SALIDA_V159_T1_ADJUDICACIONES.txt`)
da DOCE ficheros, y los SIETE de la bateria reproducen exactamente. El duodecimo
es `scripts/loop/vuelta89_tarea4_guarda_op_c05.py`: excluirlo devuelve los once
del acta al digito. La cifra de la vuelta 159 es la del computo, y por eso el
remedio de la 6.7 queda EN PARADA, declarada en el reporte de la vuelta 159.

--- ADJUDICACION 6.1 DEL ACTA 159 (3 sep 2026): EL ALCANCE DEL CHECK DE P.16 SON
DOCE, NO ONCE, Y LA VARA ES LA LECTURA B ---

CORRECCION DECLARADA POR ADICION. Nada de lo escrito arriba se borra, y en
particular NO SE BORRA la cifra ONCE que la adjudicacion 6.7 del acta 158 dejo
escrita: se corrige delante de ella para que la correccion se pueda auditar.

LA CIFRA VIEJA Y LA NUEVA, LAS DOS ESCRITAS. El acta 158 midio ONCE ficheros de
`scripts/loop/` con el patron literal del check de P.16 y su encargo mando parar
si la cuenta no daba once. La vuelta 159 recomputo y dio DOCE, paro por mandato
literal y NO TOCO UN SOLO CHECK. EL ACTA 159 ADJUDICA QUE SON DOCE Y QUE LA
CIFRA EQUIVOCADA ERA LA DEL ACTA, o sea la del auditor: lo midio el en dos
arboles distintos, el del commit del acta 158 y HEAD, y los dos dan 4 / 12 / 14
ficheros y 3 / 7 / 7 dentro de la bateria de las 23. EL ONCE NUNCA FUE CIERTO, y
la diferencia no la introdujo ninguna vuelta.

LA VARA DE LA LECTURA ES LA B, Y SE NOMBRA PARA QUE NO VUELVA A DERIVAR: B MEDIA
es "pathspec que empieza por dataset/", que es la que el ejecutor publico como
principal y la que la 6.7 del acta 158 sostiene al describir el defecto por su
instrumento. LA LECTURA ESTRECHA DE CUATRO (dataset/ Y docs/plan/ a la vez) NO
VALE, porque el defecto no depende de que el pathspec traiga tambien docs/plan/.

EL DUODECIMO ENTRA Y TIENE NOMBRE: `vuelta89_tarea4_guarda_op_c05.py`. Es del
mismo defecto que la serie 142 a 147, solo que mas viejo, y lleva las dos anclas
que la 6.7 describe (la del fin de linea y la de la suciedad anterior al
arranque), leidas por el auditor en su fuente. NO HAY MOTIVO DE VARA PARA
EXCLUIRLO.

LO QUE ESTO OBLIGA: la 5.a y la 5.c del encargo de la vuelta 159 se ejecutan
sobre LOS DOCE, no sobre once ni sobre cuatro. La nomina no se teclea: se
recomputa, y su medicion esta pegada en `docs/loop/SALIDA_V159_T5_ALCANCE.txt`.
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
    """Corre el instrumento de solo lectura sobre RUTA_GRAFO y devuelve
    (entradas_sobran, nodos_con_duplicada, texto_completo). ROJO (SystemExit)
    si el instrumento falla o si su salida no se puede leer: nunca se
    inventa una cifra."""
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
    return os.path.join(LOOP, "SALIDA_V%d_GUARDA_OPC05_%s.txt" % (vuelta, lado))


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


def cmd_caso_rojo():
    print("=" * 78)
    print("TAREA 4.b: CASO ROJO OBLIGATORIO, SOBRE COPIA EN MEMORIA (dataset/ no se toca)")
    print("=" * 78)

    r_antes = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                             cwd=RAIZ, capture_output=True, text=True)
    print("git status --porcelain -- dataset/ ANTES: %r" % r_antes.stdout)
    if r_antes.stdout.strip():
        raise SystemExit("ROJO: dataset/ ya tenia cambios antes del caso rojo: no se corre "
                          "sobre un arbol sucio")

    with tempfile.TemporaryDirectory() as tmp:
        # (1) LA CUENTA DE HOY, sobre el grafo real, sin tocarlo.
        salida_hoy = os.path.join(tmp, "ARISTAS_DUPLICADAS_HOY.jsonl")
        sobran_hoy, nodos_hoy, _ = contar(GRAFO_HOY, salida_hoy)
        print("cuenta de hoy (grafo real, sin tocar): %d entradas que sobran, %d nodos"
              % (sobran_hoy, nodos_hoy))

        # (2) COPIA EN MEMORIA del grafo, con una entrada duplicada tras resolver
        # metida A PROPOSITO en un nodo vivo: dos ids de la MISMA lista que
        # resuelven al MISMO destino (la clase que el instrumento cuenta).
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
        # Duplicamos el primer destino de nodos_siguientes: la MISMA entrada
        # repetida dos veces en la lista resuelve al mismo destino las dos
        # veces, que es exactamente "el id nuevo mas su alias" o su gemelo
        # literal: una entrada de mas que sobra tras resolver.
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

    r_despues = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                               cwd=RAIZ, capture_output=True, text=True)
    print("git status --porcelain -- dataset/ DESPUES: %r" % r_despues.stdout)
    if r_despues.stdout.strip():
        raise SystemExit("ROJO: dataset/ quedo con cambios tras el caso rojo: el caso rojo "
                          "tiene que ser puramente en memoria")

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
    print("dataset/ nunca se toco: los dos git status de arriba salieron vacios.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--antes", action="store_true")
    g.add_argument("--despues", action="store_true")
    g.add_argument("--caso-rojo", action="store_true")
    ap.add_argument("--vuelta", type=int, default=89)
    a = ap.parse_args()

    if a.antes:
        return cmd_antes(a.vuelta)
    if a.despues:
        return cmd_despues(a.vuelta)
    return cmd_caso_rojo()


if __name__ == "__main__":
    raise SystemExit(main())
