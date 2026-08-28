# -*- coding: utf-8 -*-
r"""vuelta117_tarea3_1_criterio_hecho_tres_fuentes.py . TAREA 3.1 de la
vuelta 117, encargo del auditor (acta de la vuelta 116).

QUE MIDE. El mismo criterio de HECHO de la fase 04 que
vuelta116_tarea3_3_criterio_hecho_fase04.py media SOLO sobre las 98 ESCRITA
de OP-E-01, esta vez sobre LAS TRES FUENTES que el encargo de la 117 nombra:
  (1) las 98 ESCRITA de docs/plan/OP_E_01_DECIDIDAS.jsonl
  (2) las 114 de docs/plan/OP_E_06_DIRECCION_V90.jsonl
  (3) las 84 del ULTIMO fichero de direccion de OP-E-07,
      docs/plan/OP_E_07_DIRECCION_V94.jsonl (el techo de la TAREA 3.0 de esta
      vuelta ya conto CUATRO ficheros V91-V94 y declaro V94 el ultimo).

EL RESOLVEDOR DE ALIAS DE LA CASA. Gate 0 (scripts/run_phase1.py,
step7_validate, lineas 983-1009) usa una funcion `_resolver(nid)` para su
guarda "Ningun nodo VIVO se cita a si mismo tras RESOLVER (auto-arista via
alias)": arranca en `nid`; si es un nodo vivo (existe en `nodos` y no esta
`deprecado`), lo devuelve tal cual; si no, sigue la cadena `alias_de[cur]`
(un id que aparece en el `ids_alias` de otro nodo apunta AL DUENO de ese
alias) hasta encontrar un nodo vivo, evitando ciclos con un set `visto`, y si
nunca encuentra uno vivo devuelve el ULTIMO nodo real (aunque este
deprecado). Su propio docstring dice que es "copia fiel de resolverId
(web/lib/engine/graph.ts)": el resolvedor canonico vive ahi, en TypeScript;
`_resolver` es el puerto de Gate 0 para Python, pero vive como FUNCION
ANIDADA dentro de `step7_validate` (cierra sobre variables locales `alias_de`
y `nodos_todos`), asi que NO es importable tal cual desde otro script. Este
instrumento REPLICA su misma cadena (mismo `alias_de`: alias -> dueno
directo, mismo bucle con deteccion de ciclos, mismo "si no hay vivo, el
ultimo real") en una funcion propia, `resolver(nid)`, para no depender de una
funcion privada de otro modulo.

QUE CUENTA, POR FUENTE Y EN TOTAL:
  (1) IDS VIVOS: los dos extremos resuelven DIRECTO a un id vivo (sin pasar
      por la cadena de alias).
  (2) POR ALIAS: al menos un extremo necesita la cadena de alias para llegar
      a un id vivo (subconjunto de "resuelve a vivo"); se nombra a cual.
  (3) ROTAS: al menos un extremo no resuelve a NINGUN id vivo (ni directo ni
      por alias): `resolver()` devuelve un id que sigue sin existir en
      `nodos`, o los dos ids no aparecen ni como nodo ni como alias de nadie.
  (4) PRESENTES HOY POR LAS DOS VISTAS: tras resolver los dos extremos, el
      hijo resuelto vive en `nodos_siguientes` de la madre resuelta Y la
      madre resuelta vive en `nodos_previos` del hijo resuelto.
  (5) BIDIRECCIONALES: pares (madre, hijo) de la MISMA fuente cuyo inverso
      (hijo, madre) tambien esta en esa fuente, y si coinciden con los DOS
      enlaces mutuos del banco 9.22 (LD-41, LD-43) o si hay alguno mas.

SOLO MEDIR. No adjudica si el criterio de HECHO de la fase 04 esta cumplido.

USO:
  python scripts/loop/vuelta117_tarea3_1_criterio_hecho_tres_fuentes.py
"""
import json

RUTA_GRAFO = "dataset/metadata/master_graph.json"
RUTA_DECIDIDAS = "docs/plan/OP_E_01_DECIDIDAS.jsonl"
RUTA_E06 = "docs/plan/OP_E_06_DIRECCION_V90.jsonl"
RUTA_E07 = "docs/plan/OP_E_07_DIRECCION_V94.jsonl"

ENLACES_MUTUOS_9_22 = [
    frozenset(("requisitos_gates_con_dientes", "gestion_portafolio_formal")),  # LD-41
    frozenset(("requisitos_gates_con_dientes", "gestion_portafolio_dos_niveles")),  # LD-43
]


def cargar_grafo():
    g = json.load(open(RUTA_GRAFO, encoding="utf-8"))
    return g["nodos"]


def construir_alias_de(nodos):
    """IDENTICO a scripts/run_phase1.py:983-987: alias -> dueno directo."""
    alias_de = {}
    for nid, n in nodos.items():
        for a in (n.get("ids_alias") or []):
            if a != nid:
                alias_de[a] = nid
    return alias_de


def hacer_resolver(nodos, alias_de):
    """IDENTICO a scripts/run_phase1.py:989-1009 (_resolver), replicado aqui
    porque vive como funcion anidada y no es importable. Devuelve (id_final,
    via_alias, encontrado_vivo)."""
    def resolver(nid):
        n = nodos.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid, False, True
        visto = {nid}
        cur = nid
        ultimo_real = nid if n is not None else None
        via_alias = False
        while cur in alias_de:
            cur = alias_de[cur]
            via_alias = True
            if cur in visto:
                break
            visto.add(cur)
            c = nodos.get(cur)
            if c is None:
                continue
            ultimo_real = cur
            if not c.get("deprecado"):
                return cur, True, True
        return ultimo_real, via_alias, False
    return resolver


def leer_pares(ruta):
    filas = [json.loads(l) for l in open(ruta, encoding="utf-8") if l.strip()]
    return [(f["madre"], f["hijo"]) for f in filas]


def medir_fuente(nombre, pares, nodos, resolver):
    print("--- FUENTE: %s (%d pares) ---" % (nombre, len(pares)))
    ids_vivos = 0
    por_alias = []
    rotas = []
    presentes = []
    ausentes = []
    for m, h in pares:
        rm, alias_m, vivo_m = resolver(m)
        rh, alias_h, vivo_h = resolver(h)
        if not vivo_m or not vivo_h:
            rotas.append((m, h, rm, vivo_m, rh, vivo_h))
            continue
        if alias_m or alias_h:
            por_alias.append((m, rm if alias_m else "=", h, rh if alias_h else "="))
        else:
            ids_vivos += 1
        # PRESENCIA HOY POR LAS DOS VISTAS, sobre los ids RESUELTOS.
        n_madre = nodos.get(rm) or {}
        n_hijo = nodos.get(rh) or {}
        sig = rh in (n_madre.get("nodos_siguientes") or [])
        prev = rm in (n_hijo.get("nodos_previos") or [])
        if sig and prev:
            presentes.append((m, h, rm, rh))
        else:
            ausentes.append((m, h, rm, rh, sig, prev))

    print("ids vivos DIRECTO (los dos extremos, sin cadena de alias): %d" % ids_vivos)
    print("resueltos POR ALIAS (al menos un extremo): %d" % len(por_alias))
    for x in por_alias:
        print("   ALIAS: %s (->%s) -- %s (->%s)" % x)
    print("ROTAS (al menos un extremo sin id vivo, ni directo ni por alias): %d" % len(rotas))
    for x in rotas:
        print("   ROTO: %s (resuelve %s, vivo=%s) -> %s (resuelve %s, vivo=%s)" % x)
    print("PRESENTES hoy en el grafo por las DOS vistas: %d de %d (con extremos vivos)"
          % (len(presentes), len(presentes) + len(ausentes)))
    print("AUSENTES (con extremos vivos, pero la arista resuelta no esta completa hoy): %d"
          % len(ausentes))
    for x in ausentes:
        print("   AUSENTE: %s -> %s (resuelto %s -> %s) sig=%s prev=%s" % x)

    set_pares = set(pares)
    bidireccionales = set()
    for m, h in pares:
        if (h, m) in set_pares:
            bidireccionales.add(frozenset((m, h)))
    print("pares con las DOS direcciones escritas EN ESTA FUENTE: %d" % len(bidireccionales))
    for par in bidireccionales:
        m, h = tuple(par)
        es_9_22 = par in ENLACES_MUTUOS_9_22
        print("   %s <-> %s -- %s" % (m, h, "ES uno de los dos enlaces mutuos del 9.22" if es_9_22 else "NO es de los dos del 9.22, ALGUNA MAS"))
    print()
    return {
        "total": len(pares), "ids_vivos": ids_vivos, "por_alias": len(por_alias),
        "rotas": len(rotas), "presentes": len(presentes), "ausentes": len(ausentes),
        "bidireccionales": len(bidireccionales),
    }


def main():
    nodos = cargar_grafo()
    alias_de = construir_alias_de(nodos)
    resolver = hacer_resolver(nodos, alias_de)

    print("CRITERIO DE HECHO DE LA FASE 04 SOBRE TRES FUENTES, TAREA 3.1 VUELTA 117.")
    print("Resolvedor: replica de _resolver() en scripts/run_phase1.py:989-1009")
    print("(copia fiel declarada de resolverId, web/lib/engine/graph.ts); NO importable")
    print("tal cual por ser funcion anidada, replicada aqui con la misma cadena de alias_de.")
    print("=" * 100)
    print()

    fuentes = [
        ("OP-E-01 ESCRITA (%s)" % RUTA_DECIDIDAS,
         [(f["madre"], f["hijo"]) for f in
          (json.loads(l) for l in open(RUTA_DECIDIDAS, encoding="utf-8") if l.strip())
          if f["decision"] == "ESCRITA"]),
        ("OP-E-06 direccion (%s)" % RUTA_E06, leer_pares(RUTA_E06)),
        ("OP-E-07 direccion, ULTIMO (%s)" % RUTA_E07, leer_pares(RUTA_E07)),
    ]

    resumenes = {}
    todos_los_pares = []
    for nombre, pares in fuentes:
        resumenes[nombre] = medir_fuente(nombre, pares, nodos, resolver)
        todos_los_pares.extend(pares)

    print("--- TOTAL (%d pares, suma de las tres fuentes, sin deduplicar) ---" % len(todos_los_pares))
    for campo in ("total", "ids_vivos", "por_alias", "rotas", "presentes", "ausentes", "bidireccionales"):
        print("%s: %d" % (campo, sum(r[campo] for r in resumenes.values())))


if __name__ == "__main__":
    main()
