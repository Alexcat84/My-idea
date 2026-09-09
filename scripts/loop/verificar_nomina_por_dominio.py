# -*- coding: utf-8 -*-
r"""verificar_nomina_por_dominio.py . EL QUINTO CONTROL MECANICO DE LA ADUANA
(`OP-A-02` v4, quinto de cinco; `docs/plan/07_ADUANA.md`, tabla de los cinco
controles: *revision de toda nomina por el DOMINIO de sus miembros, control
mecanico del 13 ago 2026*). NOMBRE ESTABLE, SIN NUMERO DE VUELTA, como
`verificar_nomina_sellada.py` y `verificar_fuente_canonico.py`.

POR QUE NACE AQUI Y AHORA. La pagina 07 nombra CINCO controles y Gate 0 corria
CUATRO: este era el que faltaba (acta 217, seccion 6, linea 77344, y cola de la
auditoria integral, entrada 2). La auditoria integral del 9 sep 2026 lo
FABRICA por decision del fundador (PASO 1.a, item 3), porque es un chequeo
mecanico sobre datos que ya existen y no pide decision de contenido.

LA LETRA DEL CONTROL, LEIDA DE `docs/plan/04_ENLACES.md` (lineas 1031 a 1033 y
su correccion declarada de la vuelta 76): *revisar toda nomina por el DOMINIO de
sus miembros, cruzando `RACIMOS_MIEMBROS.jsonl` contra el grafo*. El universo
es, por construccion, el censo `docs/RACIMOS_MIEMBROS.jsonl` (los racimos que
el cribado declaro); un racimo que no esta en el censo no esta en este
universo, y eso se dice en vez de fingir que se cubre.

EL CRITERIO, MECANICO Y SIN JUICIO:
  1. cada miembro del censo se resuelve por alias (P.1) hasta su nodo VIVO; un
     miembro que no resuelve a ningun nodo del grafo es ROJO;
  2. el `dominio_censado` del racimo se lee como CONJUNTO de dominios: `NUCLEO`
     es `core`, y `a + b` (con o sin cuentas entre parentesis) es la declaracion
     TRANSVERSAL explicita que la propia pagina 04 reconoce como segunda salida;
  3. un miembro cuyo nodo vivo tiene un dominio FUERA de ese conjunto es un
     racimo que PARECE de un dominio y no lo es: ROJO nombrando racimo, miembro
     y los dos dominios.

LA FRONTERA: esta guarda NO decide si un racimo debe depurarse o declararse
transversal (eso es la pagina 04 y una lectura). Solo impide que un racimo del
censo cambie de dominio EN SILENCIO, que es lo que un control mecanico puede
impedir.

PURA A PROPOSITO: `verificar(censo=None, nodos=None)` recibe el censo y los
nodos por parametro para que su caso rojo se pruebe por mutacion en memoria sin
tocar el disco (`vuelta221_integral_mutacion_nomina_por_dominio.py`).

FALLA RUIDOSO (banco 9): si el censo no se puede leer, ROJO con su motivo,
nunca un verde por no haber podido mirar.

USO SUELTO:  python scripts/loop/verificar_nomina_por_dominio.py
CABLEADA A GATE 0: scripts/run_phase1.py, step7_validate, junto a los otros
cuatro controles de la aduana.
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CENSO = os.path.join(RAIZ, "docs", "RACIMOS_MIEMBROS.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")


def leer_censo(ruta=CENSO):
    return [json.loads(l) for l in io.open(ruta, encoding="utf-8") if l.strip()]


def leer_nodos(ruta=GRAFO):
    return json.load(io.open(ruta, encoding="utf-8"))["nodos"]


def dominios_declarados(texto):
    """`NUCLEO` -> {core}; `quality + environmental + nucleo` -> {quality,
    environmental, core}; `nucleo (3) + quality (1)` -> {core, quality}."""
    partes = re.split(r"[+,]", str(texto or ""))
    out = set()
    for p in partes:
        p = re.sub(r"\(.*?\)", "", p).strip().lower()
        if not p:
            continue
        out.add("core" if p in ("nucleo", "core") else p)
    return out


def resolver_vivo(nid, nodos, alias_de):
    """Sigue ids_alias hasta un nodo vivo. Devuelve (id_vivo o None)."""
    visto = set()
    x = nid
    while True:
        if x in visto:
            return None
        visto.add(x)
        nd = nodos.get(x)
        if nd is None:
            x = alias_de.get(x)
            if x is None:
                return None
            continue
        if not nd.get("deprecado"):
            return x
        x = alias_de.get(x)
        if x is None:
            return None


def verificar(censo=None, nodos=None):
    """Devuelve (ok, fallos, detalle). `fallos` es una lista de tuplas
    (racimo, miembro, dominio_censado, dominio_real_o_None)."""
    try:
        censo = leer_censo() if censo is None else censo
        nodos = leer_nodos() if nodos is None else nodos
    except Exception as e:  # noqa: BLE001
        return False, [("(censo o grafo ilegible)", str(e), "", None)], {"racimos": 0, "miembros": 0}
    alias_de = {}
    for nid, nd in nodos.items():
        for a in nd.get("ids_alias") or []:
            alias_de.setdefault(a, nid)
    fallos = []
    miembros = 0
    for r in censo:
        declarados = dominios_declarados(r.get("dominio_censado"))
        for m in r.get("miembros") or []:
            miembros += 1
            nid = m.get("node_id") if isinstance(m, dict) else m
            vivo = resolver_vivo(nid, nodos, alias_de)
            if vivo is None:
                fallos.append((r.get("racimo"), nid, r.get("dominio_censado"), None))
                continue
            dom = nodos[vivo].get("dominio")
            if dom not in declarados:
                fallos.append((r.get("racimo"), nid, r.get("dominio_censado"), dom))
    detalle = {"racimos": len(censo), "miembros": miembros}
    return (not fallos), fallos, detalle


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ok, fallos, detalle = verificar()
    print("QUINTO CONTROL DE LA ADUANA: toda nomina del censo revisada por el DOMINIO de sus miembros")
    print("CIFRA racimos del censo: %d | CIFRA miembros revisados: %d | CIFRA fuera de su dominio: %d"
          % (detalle["racimos"], detalle["miembros"], len(fallos)))
    for f in fallos[:20]:
        print("   ROJO> racimo %r, miembro %s, censado %r, real %r" % f)
    print("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
