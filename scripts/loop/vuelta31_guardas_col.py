"""Vuelta 31: LAS GUARDAS de cierre del segundo tiempo de OP-F-04-COL.

Las que el encargo nombra y que ni la simulacion ni el caso positivo cubren:

  1. VIAJE VERBATIM: cada paso que salio de un origen vive TEXTUAL en su destino.
     El caso positivo prueba la HUELLA (un trozo); esto prueba el paso entero.
  2. CERO PERDIDA, contada sobre el arbol: los pasos de los origenes antes del
     corte tienen que ser los pasos que quedan mas los que viajaron, nodo por
     nodo, contra la version de HEAD leida con git.
  3. CERO DUPLICADAS Y CERO AUTO-ARISTAS tras resolver, sobre los nodos tocados
     (P.1: todo conteo que toque ids pasa por el resolutor antes de contar).
  4. LOS NODOS PROPIOS existen, estan vivos, tienen los doce campos y su arista
     reciproca con el donante que los creo.

No escribe nada.

Uso: python scripts/loop/vuelta31_guardas_col.py <plan.json>
"""
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
MASTER = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

CAMPOS_NODO = [
    "node_id", "fase_proyecto", "dominio", "titulo_concepto", "fuente",
    "resumen_teorico", "pasos_accionables", "entregable_esperado",
    "nodos_previos", "nodos_siguientes", "condiciones_activacion",
    "etiqueta_arbol",
]


def cargar():
    fuera = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            with open(os.path.join(NODOS, nombre), encoding="utf-8") as fh:
                d = json.load(fh)
            fuera[d["node_id"]] = d
    return fuera


def en_head(nid):
    """El nodo tal como esta en HEAD, o None si ahi no existia."""
    ruta = "dataset/nodos/%s.json" % nid
    p = subprocess.run(["git", "show", "HEAD:%s" % ruta], cwd=RAIZ,
                       capture_output=True)
    if p.returncode != 0:
        return None
    return json.loads(p.stdout.decode("utf-8"))


def alias():
    if not os.path.exists(MASTER):
        return {}
    g = json.load(open(MASTER, encoding="utf-8"))["nodos"]
    return {a: k for k, v in g.items() for a in (v.get("ids_alias") or [])}


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    plan = json.load(open(sys.argv[1], encoding="utf-8"))
    grafo = cargar()
    ALIAS = alias()

    def res(x):
        visto = set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    fallos = []
    print("GUARDAS DE CIERRE: %s" % plan["operacion"])
    print("=" * 78)

    # ---- 1. VIAJE VERBATIM ----
    print("\n--- 1. VIAJE VERBATIM: cada paso que salio vive TEXTUAL en su destino ---")
    viajados = 0
    for c in plan["cortes"]:
        dest = c["destino"]
        did = dest.get("nodo") or dest["nuevo"]["node_id"]
        d = grafo.get(did)
        if d is None:
            fallos.append("%s: el destino %s no existe" % (c["origen"], did))
            print("  [ROJO] %s no existe" % did)
            continue
        pasos = d.get("pasos_accionables") or []
        malos = [t for t in c["pasos_que_salen_texto"] if t not in pasos]
        viajados += len(c["pasos_que_salen_texto"])
        if malos:
            fallos.append("%s -> %s: %d paso(s) NO viajaron verbatim"
                          % (c["origen"], did, len(malos)))
            print("  [ROJO] %s -> %s: %s" % (c["origen"], did, [m[:50] for m in malos]))
    print("  pasos que viajaron: %d, todos verbatim: %s"
          % (viajados, "SI" if not fallos else "NO"))

    # ---- 2. CERO PERDIDA, contra HEAD ----
    print("\n--- 2. CERO PERDIDA, nodo por nodo contra la version de HEAD ---")
    porori = {}
    for c in plan["cortes"]:
        porori.setdefault(c["origen"], []).extend(c["pasos_que_salen"])
    for o in sorted(porori):
        viejo = en_head(o)
        antes = len(viejo["pasos_accionables"]) if viejo else 0
        ahora = len(grafo[o]["pasos_accionables"])
        salen = len(porori[o])
        ok = antes == ahora + salen
        if not ok:
            fallos.append("%s: %d antes, %d ahora, %d salieron" % (o, antes, ahora, salen))
        # y ademas: ningun paso que se queda cambio de texto
        quedan_viejo = [p for i, p in enumerate(viejo["pasos_accionables"], 1)
                        if i not in porori[o]] if viejo else []
        igual = quedan_viejo == grafo[o]["pasos_accionables"]
        if not igual:
            fallos.append("%s: los pasos que se quedan NO son los mismos textos" % o)
        print("  [%s] %-38s %2d antes = %2d ahora + %2d salen   texto de los que quedan: %s"
              % ("OK  " if ok and igual else "ROJO", o, antes, ahora, salen,
                 "INTACTO" if igual else "CAMBIADO"))

    # ---- 3. CERO DUPLICADAS Y CERO AUTO-ARISTAS, tras resolver ----
    #
    # CORRECCION DECLARADA DE ESTA GUARDA (14 ago 2026, vuelta 31), escrita
    # DESPUES de verla caer, que es justamente el movimiento que hay que poder
    # auditar. La primera version media el TOTAL de duplicadas tras resolver en
    # los nodos tocados y dio 9 en rojo. Antes de tocar una linea se midio la
    # MISMA cuenta sobre la version de HEAD de esos nodos
    # (docs/loop/_v31_duplicadas_antes.py, salida en
    # docs/loop/SALIDA_V31_DUPLICADAS_ANTES.txt): las NUEVE ya estaban ahi, en
    # los mismos nodos y los mismos campos, y las nueve son pares de alias que
    # resuelven al mismo destino (por ejemplo spiral_development y
    # desarrollo_en_espiral en voz_del_cliente_voc).
    #
    # Esa poblacion esta CONTADA Y ADJUDICADA por escrito: docs/plan/00_INDICE.md
    # la mide en 1.056 entradas duplicadas tras resolver en 802 nodos (el 22,8
    # por ciento del catalogo vivo), la manda a OP-S-12 con su guarda OP-C-05, y
    # su atadura 2 dice que OP-S-12 VA AL FINAL, despues de la ultima fusion,
    # porque cada fusion fabrica las suyas. Su criterio de cierre (fila 5 de la
    # tabla de condiciones) es de la fase SANEO, no de la fase 01.
    #
    # Lo que el encargo pide de ESTA operacion es que no fabrique duplicadas ni
    # auto aristas. Eso es una DIFERENCIA contra HEAD, no un total absoluto, y es
    # lo que la guarda mide a partir de aqui. El total se sigue imprimiendo con
    # su nombre para que nadie lo confunda con un cero que no existe.
    print("\n--- 3. CERO DUPLICADAS Y CERO AUTO-ARISTAS TRAS RESOLVER (P.1) ---")
    print("  se mide la DIFERENCIA contra HEAD: lo que ESTA operacion fabrica.")
    print("  el total absoluto es la poblacion de OP-S-12 (00_INDICE.md), y se imprime aparte.")
    tocados = sorted(set(porori) | {(c["destino"].get("nodo")
                                     or c["destino"]["nuevo"]["node_id"])
                                    for c in plan["cortes"]})
    dup_ahora = dup_antes = auto = 0
    for nid in tocados:
        d = grafo[nid]
        viejo = en_head(nid)
        for campo in ("nodos_previos", "nodos_siguientes"):
            v = [res(x) for x in (d.get(campo) or [])]
            sobran = len(v) - len(set(v))
            propias = sum(1 for x in v if x == res(nid))
            vv = [res(x) for x in ((viejo or {}).get(campo) or [])]
            sobran_antes = len(vv) - len(set(vv))
            dup_ahora += sobran
            dup_antes += sobran_antes
            if sobran > sobran_antes:
                fallos.append("%s.%s: esta operacion fabrico %d duplicada(s)"
                              % (nid, campo, sobran - sobran_antes))
                print("  [ROJO] %s.%s: %d antes, %d ahora" % (nid, campo, sobran_antes, sobran))
            elif sobran:
                print("  [VIEJA] %s.%s: %d duplicada(s), las mismas que en HEAD (OP-S-12)"
                      % (nid, campo, sobran))
            if propias:
                auto += propias
                fallos.append("%s.%s: %d auto arista(s)" % (nid, campo, propias))
                print("  [ROJO] %s.%s auto aristas: %d" % (nid, campo, propias))
    print("  nodos tocados: %d" % len(tocados))
    print("  duplicadas tras resolver: %d en HEAD, %d ahora, FABRICADAS POR ESTA OPERACION: %d"
          % (dup_antes, dup_ahora, dup_ahora - dup_antes))
    print("  auto aristas: %d" % auto)

    # ---- 4. LOS NODOS PROPIOS ----
    print("\n--- 4. LOS NODOS PROPIOS ---")
    nuevos = []
    for c in plan["cortes"]:
        if c["destino"]["tipo"] == "nodo_propio":
            nuevos.append((c["origen"], c["destino"]["nuevo"]["node_id"]))
    for origen, nid in nuevos:
        d = grafo.get(nid)
        if d is None:
            fallos.append("%s: no se creo" % nid)
            print("  [ROJO] %s no existe" % nid)
            continue
        faltan = [k for k in CAMPOS_NODO if k not in d]
        vivo = not d.get("deprecado") and not d.get("deprecated")
        ida = nid in (grafo[origen].get("nodos_siguientes") or [])
        vuelta = origen in (d.get("nodos_previos") or [])
        ok = not faltan and vivo and ida and vuelta
        if not ok:
            fallos.append("%s: campos %s vivo=%s ida=%s vuelta=%s"
                          % (nid, faltan, vivo, ida, vuelta))
        print("  [%s] %-42s pasos %2d  campos %2d  vivo %s  arista ida %s vuelta %s"
              % ("OK  " if ok else "ROJO", nid, len(d["pasos_accionables"]),
                 len(d), vivo, ida, vuelta))

    print("\n" + "=" * 78)
    if fallos:
        print("ROJO: %d guarda(s) caida(s)." % len(fallos))
        for f in fallos:
            print("  - %s" % f)
        return 1
    print("VERDE: las cuatro guardas pasan.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
