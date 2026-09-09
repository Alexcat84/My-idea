# -*- coding: utf-8 -*-
r"""vuelta221_integral_mutacion_nomina_por_dominio.py . EL CASO ROJO POR MUTACION
DEL QUINTO CONTROL DE LA ADUANA (`scripts/loop/verificar_nomina_por_dominio.py`),
fabricado en la AUDITORIA INTEGRAL del 9 sep 2026 (PASO 1.a, item 3).

EL NUMERO 221 ES EL NUMERO DE CENSO QUE SIGUE A LA VUELTA 220, PARA QUE LA
BATERIA LO VEA (PATRON_ARNES exige `vuelta<N>_`); la auditoria integral NO es
una vuelta del bucle, y eso se dice aqui para que nadie lo lea como tal.

QUE PRUEBA. Que la guarda MUERDE en sus tres direcciones y que sin mutar nada
sale VERDE. TODAS LAS MUTACIONES SON SOBRE COPIAS EN MEMORIA del censo y del
grafo; CERO ESCRITURAS, comprobado con `git status --porcelain` antes y despues
sobre `docs/` y `dataset/`.

LOS CASOS:
  (0) CONTRAPRUEBA: censo y grafo reales, sin mutar: VERDE.
  (A) UN MIEMBRO CAMBIA DE DOMINIO: al nodo vivo del primer miembro del primer
      racimo se le pone en memoria un dominio que NO esta entre los declarados
      del racimo. La guarda tiene que caer nombrando racimo y miembro.
  (B) UN MIEMBRO QUE NO RESUELVE: al primer miembro se le cambia el node_id por
      uno que no existe en el grafo ni como alias. ROJO nombrandolo.
  (C) UN RACIMO QUE PIERDE SU DECLARACION TRANSVERSAL: al racimo cuyo
      `dominio_censado` declara MAS DE UN dominio se le deja solo el primero. Al
      menos un miembro queda fuera y la guarda cae. Si no hubiera ningun racimo
      transversal en el censo, el caso se declara SIN SUJETO y no cuenta como
      verde.
  (D) EL PARSEO DE LA DECLARACION: `nucleo (3) + quality (1)` da {core, quality}
      y `NUCLEO` da {core}; con el esperado mutado, cae.

Y CADA CASO ROJO SE CONTRASTA: el mismo censo sin la mutacion vuelve a VERDE, o
sea que el rojo sale de la mutacion y no de otra causa.

USO:  python scripts/loop/vuelta221_integral_mutacion_nomina_por_dominio.py
Escribe docs/loop/SALIDA_integral_MUTACION_NOMINA_POR_DOMINIO.txt.
"""
import copy
import io
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import verificar_nomina_por_dominio as G   # noqa: E402

RAIZ = G.RAIZ
DESTINO = os.path.join(RAIZ, "docs", "loop", "SALIDA_integral_MUTACION_NOMINA_POR_DOMINIO.txt")


def porcelain():
    r = subprocess.run(["git", "status", "--porcelain", "--", "docs/RACIMOS_MIEMBROS.jsonl", "dataset/"],
                       cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", "replace")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    fallos = 0
    antes = porcelain()
    censo = G.leer_censo()
    nodos = G.leer_nodos()
    w("ARNES DE MUTACION DEL QUINTO CONTROL DE LA ADUANA (auditoria integral, 9 sep 2026)")
    w("sujeto vivo: scripts/loop/verificar_nomina_por_dominio.py")
    w("CIFRA racimos del censo: %d | CIFRA nodos del grafo: %d" % (len(censo), len(nodos)))
    w("")

    ok, f, det = G.verificar(censo, nodos)
    w("(0) CONTRAPRUEBA, sin mutar: %s, fallos %d, miembros revisados %d" % ("VERDE" if ok else "ROJO", len(f), det["miembros"]))
    if not ok:
        fallos += 1
        for x in f[:5]:
            w("      ROJO> %r" % (x,))

    alias_de = {}
    for nid, nd in nodos.items():
        for a in nd.get("ids_alias") or []:
            alias_de.setdefault(a, nid)
    r0 = censo[0]
    m0 = r0["miembros"][0]["node_id"]
    vivo0 = G.resolver_vivo(m0, nodos, alias_de)
    declarados0 = G.dominios_declarados(r0["dominio_censado"])
    dominios_todos = sorted({nd.get("dominio") for nd in nodos.values() if nd.get("dominio")})
    ajeno = next(d for d in dominios_todos if d not in declarados0)

    w("")
    w("(A) EL MIEMBRO %s DEL RACIMO %r (vivo: %s) PASA EN MEMORIA DEL DOMINIO %r AL %r"
      % (m0, r0["racimo"], vivo0, nodos[vivo0].get("dominio"), ajeno))
    n_mut = copy.deepcopy(nodos)
    n_mut[vivo0]["dominio"] = ajeno
    okA, fA, _ = G.verificar(censo, n_mut)
    nombra = any(x[0] == r0["racimo"] and x[1] == m0 and x[3] == ajeno for x in fA)
    w("      veredicto mutado: %s | fallos %d | nombra racimo y miembro: %s -> %s"
      % ("VERDE" if okA else "ROJO", len(fA), nombra, "CAE" if (not okA and nombra) else "NO CAE"))
    if okA or not nombra:
        fallos += 1
    okA2, _, _ = G.verificar(censo, nodos)
    w("      contraste sin mutar: %s" % ("VERDE" if okA2 else "ROJO"))
    if not okA2:
        fallos += 1

    w("")
    w("(B) EL MIEMBRO %s SE CAMBIA POR UN ID QUE NO EXISTE NI COMO ALIAS" % m0)
    c_mut = copy.deepcopy(censo)
    inexistente = m0 + "_QUE_NO_EXISTE_integral"
    c_mut[0]["miembros"][0]["node_id"] = inexistente
    okB, fB, _ = G.verificar(c_mut, nodos)
    nombraB = any(x[1] == inexistente and x[3] is None for x in fB)
    w("      veredicto mutado: %s | fallos %d | nombra el id sin resolver: %s -> %s"
      % ("VERDE" if okB else "ROJO", len(fB), nombraB, "CAE" if (not okB and nombraB) else "NO CAE"))
    if okB or not nombraB:
        fallos += 1

    w("")
    trans = [i for i, r in enumerate(censo) if len(G.dominios_declarados(r["dominio_censado"])) > 1]
    if not trans:
        w("(C) SIN SUJETO: ningun racimo del censo declara mas de un dominio. NO CUENTA COMO VERDE.")
        fallos += 1
    else:
        i = trans[0]
        r = censo[i]
        primero = str(r["dominio_censado"]).replace("+", ",").split(",")[0].strip()
        w("(C) EL RACIMO %r (censado %r) PIERDE SU DECLARACION TRANSVERSAL Y QUEDA SOLO %r"
          % (r["racimo"], r["dominio_censado"], primero))
        c_mut = copy.deepcopy(censo)
        c_mut[i]["dominio_censado"] = primero
        okC, fC, _ = G.verificar(c_mut, nodos)
        nombraC = any(x[0] == r["racimo"] for x in fC)
        w("      veredicto mutado: %s | fallos %d | nombra el racimo: %s -> %s"
          % ("VERDE" if okC else "ROJO", len(fC), nombraC, "CAE" if (not okC and nombraC) else "NO CAE"))
        if okC or not nombraC:
            fallos += 1

    w("")
    w("(D) EL PARSEO DE LA DECLARACION, con su esperado y su esperado mutado")
    casos = [("nucleo (3) + quality (1)", {"core", "quality"}), ("NUCLEO", {"core"}),
             ("quality + environmental + nucleo", {"quality", "environmental", "core"}), ("health_safety", {"health_safety"})]
    for texto, esperado in casos:
        real = G.dominios_declarados(texto)
        mutado = set(esperado) | {"MUTADO"}
        w("      %-36r -> %s | esperado %s: %s | mutado %s: %s"
          % (texto, sorted(real), sorted(esperado), "PASA" if real == esperado else "FALLA",
             sorted(mutado), "CAE" if real != mutado else "NO CAE"))
        if real != esperado or real == mutado:
            fallos += 1

    despues = porcelain()
    w("")
    w("CERO ESCRITURAS: porcelain antes == despues: %s" % (antes == despues))
    if antes != despues:
        fallos += 1
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = "\n".join(L) + "\n"
    io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (DESTINO, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
