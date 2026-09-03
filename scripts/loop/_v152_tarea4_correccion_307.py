# -*- coding: utf-8 -*-
"""VUELTA 152, TAREA 4: LA CORRECCION DECLARADA DEL 307, CON LA CIFRA VIEJA
INTACTA Y LA UNIDAD BUENA AL LADO.

EL HALLAZGO ES DEL AUDITOR (acta 151, caida 4.4): el comentario de la guarda de
OP-C-05 en scripts/run_phase1.py y la linea 27 de
docs/loop/SALIDA_V150_2C_SIETE_VERIFICACIONES.txt dicen "307 nodos vivos" donde
lo medido son 307 DESTINOS sobre 255 NODOS VIVOS. LA UNIDAD ESTABA MAL, no el
numero: 307 es correcto como cardinal de PARES nodo-destino.

RE MEDIDO EN ESTA VUELTA CON INSTRUMENTO PROPIO antes de escribir una sola
letra (EJECUTOR.md 2, EL INSTRUMENTO MANDA): 255 nodos vivos, 307 destinos.

COMO SE CORRIGE, Y POR QUE ASI. Por DECLARACION y por ADICION: en los dos
sitios la frase vieja SE QUEDA ENTERA y la buena se escribe al lado. Una
correccion que tapa lo que corrige no se puede auditar (EJECUTOR.md 8). En el
fichero de salida de la vuelta 150 NO se reescribe la linea 27: se ANADE un
bloque al final, y un assert comprueba que el fichero viejo es prefijo EXACTO
del nuevo.

POR LA DECISION DEL FUNDADOR DEL 2 SEP 2026 (PREGUNTA 2, en
docs/loop/paradas/2026-09-02-opc05-bidireccionales-DECISION.md) esta sede SI
cuenta como CIFRA PUBLICADA desde hoy, pero SIN RETROACTIVIDAD: esta se corrige
por declaracion y NO ACUMULA.

USO:
  python scripts/loop/_v152_tarea4_correccion_307.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUARDA = os.path.join(RAIZ, "scripts", "run_phase1.py")
SALIDA150 = os.path.join(RAIZ, "docs", "loop", "SALIDA_V150_2C_SIETE_VERIFICACIONES.txt")
CORR = os.path.join(RAIZ, "docs", "plan", "CORRECCIONES_A_APLICAR.md")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")


def medir():
    """LA MEDICION PROPIA, escrita aqui y no importada del codigo que corrige."""
    N = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    alias = {}
    for nid, n in N.items():
        for a in (n.get("ids_alias") or []):
            if a != nid:
                alias[a] = nid

    def r(nid):
        n = N.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid
        visto, cur, ult = {nid}, nid, (nid if n is not None else None)
        while cur in alias:
            cur = alias[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = N.get(cur)
            if c is None:
                continue
            ult = cur
            if not c.get("deprecado"):
                return cur
        return ult

    nodos, destinos = set(), 0
    for nid, n in N.items():
        if n.get("deprecado"):
            continue
        P = {r(d) for d in (n.get("nodos_previos") or []) if d in N}
        S = {r(d) for d in (n.get("nodos_siguientes") or []) if d in N}
        comunes = {x for x in (P & S) if x}
        if comunes:
            nodos.add(nid)
            destinos += len(comunes)
    return len(nodos), destinos


def anadir(ruta, bloque, etiqueta):
    viejo = io.open(ruta, encoding="utf-8").read()
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(viejo + bloque)
    nuevo = io.open(ruta, encoding="utf-8").read()
    assert nuevo.startswith(viejo), "ADICION IMPURA en %s" % etiqueta
    assert len(nuevo) > len(viejo)
    print("  [OK] %s: ADICION PURA (el viejo es prefijo EXACTO del nuevo, %d -> %d caracteres)"
          % (etiqueta, len(viejo), len(nuevo)))


def sustituir_una_vez(ruta, viejo, nuevo, etiqueta):
    t = io.open(ruta, encoding="utf-8").read()
    assert t.count(viejo) == 1, "%s: el ancla aparece %d veces" % (etiqueta, t.count(viejo))
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(t.replace(viejo, nuevo))
    print("  [OK] %s" % etiqueta)


nodos, destinos = medir()
print("MEDICION PROPIA DE ESTA VUELTA, sobre dataset/metadata/master_graph.json (WORK):")
print("  NODOS VIVOS con al menos un destino en nodos_previos Y en nodos_siguientes")
print("  a la vez, tras resolver: %d" % nodos)
print("  DESTINOS (pares nodo-destino) en esa situacion:                      %d" % destinos)
print("")
print("LA CIFRA VIEJA DECIA '%d nodos vivos'. EL NUMERO ES CORRECTO; LA UNIDAD NO:" % destinos)
print("%d es el cardinal de DESTINOS, y los NODOS son %d." % (destinos, nodos))
print("")

# ------------------------------------------------------- SEDE 1: la guarda
ANCLA = """    # se vacia en cada `campo` y nunca se cruzan las dos listas: hoy hay 307
    # nodos vivos con un destino en las dos listas y ninguno es un fallo.
"""
NUEVO = """    # se vacia en cada `campo` y nunca se cruzan las dos listas: hoy hay 307
    # nodos vivos con un destino en las dos listas y ninguno es un fallo.
    #
    # CORRECCION DECLARADA (2026-09-02, vuelta 152, TAREA 4; hallazgo del acta
    # 151, caida 4.4. LA FRASE DE ARRIBA NO SE BORRA: esta se anade debajo).
    # LA UNIDAD DE ESA CIFRA ESTABA MAL. El 307 es correcto, pero NO cuenta
    # nodos: cuenta DESTINOS. Re medido en la vuelta 152 con instrumento propio
    # (scripts/loop/_v152_tarea4_correccion_307.py, salida en
    # docs/loop/SALIDA_V152_T4_CORRECCION_307.txt): son 307 DESTINOS repartidos
    # sobre 255 NODOS VIVOS. Un nodo puede traer mas de un destino en las dos
    # listas a la vez, y por eso los dos cardinales no coinciden.
    #
    # Y VA CON SU REGLA AL LADO, porque esta cifra vive DENTRO del codigo de una
    # guarda de Gate 0 y hasta hoy eso no tenia casillero: por la DECISION DEL
    # FUNDADOR del 2 sep 2026 (PREGUNTA 2, en
    # docs/loop/paradas/2026-09-02-opc05-bidireccionales-DECISION.md), una cifra
    # falsa en el codigo o el docstring de una guarda de scripts/ CUENTA COMO
    # CIFRA PUBLICADA desde esa fecha, SIN RETROACTIVIDAD. Esta, por ser
    # anterior, se corrige por declaracion y NO ACUMULA.
"""
print("SEDE 1, el comentario de la guarda en scripts/run_phase1.py:")
sustituir_una_vez(GUARDA, ANCLA, NUEVO, "scripts/run_phase1.py, comentario del CASO DE BORDE")

# ------------------------------------------- SEDE 2: la salida de la vuelta 150
BLOQUE150 = """

==============================================================================
CORRECCION DECLARADA, ANADIDA POR LA VUELTA 152 (2026-09-02). NADA DE LO DE
ARRIBA SE HA REESCRITO: ESTE BLOQUE SE ANADE AL FINAL Y LA LINEA 27 SE QUEDA
LITERAL, PORQUE UNA CORRECCION QUE TAPA LO QUE CORRIGE NO SE PUEDE AUDITAR.
==============================================================================
  DONDE: VERIFICACION 3 de 7, el CASO DE BORDE, linea 27 de este fichero.
  DICE:  "307 nodo(s) vivo(s) traen un mismo destino, tras resolver, en
          nodos_previos Y en nodos_siguientes a la vez"
  Y LA UNIDAD ESTA MAL. El 307 es correcto, pero cuenta DESTINOS, no nodos.
  MEDIDO DE NUEVO EN LA VUELTA 152 CON INSTRUMENTO PROPIO
  (scripts/loop/_v152_tarea4_correccion_307.py):
      NODOS VIVOS en esa situacion .......... %d
      DESTINOS (pares nodo-destino) ......... %d
  Un mismo nodo puede traer VARIOS destinos en las dos listas a la vez, y por
  eso los dos cardinales no coinciden.
  LO QUE NO CAMBIA: el VEREDICTO de la verificacion 3 sigue siendo CONTESTADA,
  EN VERDE. La guarda saca 0 sobre este caso de borde, que es lo que la letra
  pedia; lo que estaba mal era como se nombraba el tamano del caso, no el
  comportamiento de la guarda.
  HALLAZGO: acta 151, caida 4.4. REGLA: por la decision del fundador del 2 sep
  2026 (PREGUNTA 2) esta especie cuenta como CIFRA PUBLICADA desde esa fecha,
  SIN RETROACTIVIDAD; esta se corrige por declaracion y NO ACUMULA.
""" % (nodos, destinos)
print("SEDE 2, docs/loop/SALIDA_V150_2C_SIETE_VERIFICACIONES.txt:")
anadir(SALIDA150, BLOQUE150, "SALIDA_V150_2C_SIETE_VERIFICACIONES.txt")

# ------------------------------------------------------- EL REGISTRO, CORR 32
BLOQUE_CORR = """

---

## CORRECCION 32. **LOS "307 NODOS VIVOS" DEL CASO DE BORDE DE `OP-C-05` SON 307 DESTINOS SOBRE 255 NODOS VIVOS**

**Fecha: 2026-09-02. Vuelta 152, TAREA 4. Hallazgo del acta 151, caida 4.4.**

**LA CIFRA VIEJA, INTACTA Y CITADA.** El comentario del CASO DE BORDE de la
guarda de `OP-C-05` en `scripts/run_phase1.py` dice *"hoy hay 307 nodos vivos
con un destino en las dos listas y ninguno es un fallo"*, y la linea 27 de
`docs/loop/SALIDA_V150_2C_SIETE_VERIFICACIONES.txt` dice *"307 nodo(s) vivo(s)
traen un mismo destino, tras resolver, en `nodos_previos` Y en
`nodos_siguientes` a la vez"*. **Las dos frases se quedan donde estan.**

**LA UNIDAD BUENA, AL LADO Y RE MEDIDA EN ESTA VUELTA.** El **307 es correcto**,
pero **no cuenta nodos: cuenta destinos**. Medido con instrumento propio escrito
en esta vuelta (`scripts/loop/_v152_tarea4_correccion_307.py`, salida en
`docs/loop/SALIDA_V152_T4_CORRECCION_307.txt`):

| cifra | valor |
|---|---|
| **NODOS VIVOS** con al menos un destino en `nodos_previos` Y en `nodos_siguientes` tras resolver | **%d** |
| **DESTINOS** (pares nodo-destino) en esa situacion | **%d** |

Un mismo nodo puede traer **varios** destinos en las dos listas a la vez, y por
eso los dos cardinales no coinciden.

**LO QUE ESTA CORRECCION NO TOCA.** El **veredicto** de la verificacion 3 de
`OP-C-05` sigue siendo **CONTESTADA, EN VERDE**: la guarda saca **0** sobre este
caso de borde, que es exactamente lo que su letra pide. Lo que estaba mal era
**como se nombraba el tamano del caso**, no el comportamiento de la guarda. Y no
se reescribe la linea 27 del fichero de la vuelta 150: se **anade** un bloque al
final, con un `assert` que comprueba que el fichero viejo es **prefijo exacto**
del nuevo.

**LA REGLA CON LA QUE ENTRA, ESCRITA POR EL FUNDADOR.** Por la **decision del 2
sep 2026, PREGUNTA 2**
(`docs/loop/paradas/2026-09-02-opc05-bidireccionales-DECISION.md`), una cifra
falsa en el **codigo o el docstring de una guarda de `scripts/`** cuenta como
**CIFRA PUBLICADA desde esa fecha, sin retroactividad**. **Esta es anterior: se
corrige por declaracion y NO ACUMULA.**
""" % (nodos, destinos)
print("REGISTRO, docs/plan/CORRECCIONES_A_APLICAR.md:")
anadir(CORR, BLOQUE_CORR, "CORRECCIONES_A_APLICAR.md, CORRECCION 32")

print("")
print("LAS TRES SEDES ESCRITAS. Comprobacion de que la guarda sigue compilando:")
import py_compile
py_compile.compile(GUARDA, doraise=True)
print("  [OK] compila: scripts/run_phase1.py")
