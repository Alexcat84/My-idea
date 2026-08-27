# -*- coding: utf-8 -*-
"""vuelta88_tarea5_rebase_ope06.py . VUELTA 88, TAREA 5 (adjudicaciones 6.5 y
6.6 del acta de la vuelta 87). LA RE-BASE DE OP-E-06: MEDICION PURA, CERO
ARISTAS ESCRITAS.

POR QUE NACE. El acta de la vuelta 87 levanto la parada de OP-E-06 (seccion
4, adjudicacion 6.4), pero con una condicion: la evidencia de la ficha (12
ago 2026) envejecio, y antes de abrir la operacion hay que RE-BASARLA contra
el grafo de HOY. Este instrumento hace esa re-base, con cuatro piezas, las
cuatro citadas en la propia `verificacion` de OP-E-06 y OP-E-07:

(a) LOS 192 SE TALLAN del fichero de evidencia (docs/plan/COSECHA_RAZONES_D.
    jsonl), no se citan de la ficha: filas con `nuevo == true` cuyas
    `senales` NO son exactamente `["continua por la vara"]`.

(b) LOS CUATRO FRENTES DEL DEDUPE que la `verificacion` de OP-E-06 nombra,
    corridos sobre el grafo de HOY:
      1. contra la bolsa de PASO_NODO_CALIBRADO.jsonl (la "bolsa de 477 de
         la fase 04": el fichero es el mismo que dio 477 sin arista el 11
         ago 2026 y hoy vive con otro conteo porque OP-E-01 lo fue
         consumiendo tramo a tramo; el nombre quedo pero el fichero es el
         que manda),
      2. contra las aristas YA DECLARADAS por otras operaciones (el campo
         `aristas_nuevas` de CADA operacion en OPERACIONES.jsonl, aunque esa
         operacion no haya corrido todavia: un par que otra operacion ya se
         apropio no se vuelve a proponer aqui),
      3. contra la cola de relectura post fusion (00_INDICE.md linea 409,
         siete puestos: 707, 1096, 196, 253, 224, 591, 968, listados en
         08_VERIFICACION.md "LA LISTA"),
      4. contra los pares que YA tienen arista en el grafo de hoy,
         RESOLVIENDO POR ALIAS en las dos puntas (la letra de la
         `verificacion`: "resolviendo por alias"). Ademas, y SOLO como
         medicion de contraste (no como remocion obligatoria: esta vuelta no
         decide que hacer con un nodo deprecado, solo lo cuenta), se publica
         cuantos pares tocan un nodo DEPRECADO y cuantos tocan un id que ya
         no existe en el grafo, replicando el criterio ESTRICTO SIN ALIAS
         que el acta de la vuelta 87 declaro como su propia vara de
         contraste (docs/loop/_auditor_v87_frases_192.txt): si mi corrida
         CON alias da otro numero que esa vara SIN alias, es una diferencia
         de definicion y se declara como tal, no se resuelve copiando.

(c) LA DIRECCION SE LEE. Sobre lo que sobrevive a (b), se busca en la
    `frase` de cada fila alguna palabra de las que el acta de la vuelta 87
    declaro (CRUDA, no canon): madre, hijo, padre, desarrolla, detalla,
    "en una linea", procedimiento, cuelga, enumera, menciona, nombra. El par
    SIN ninguna de esas palabras NO ENTRA en la bolsa re-basada (punto 1 de
    la `verificacion` de OP-E-06: "si una razon no lo dice, el par NO entra
    en esta operacion"), y se cuenta y se nombra ENTERO en el fichero de
    salida (punto 3 de la `verificacion` de OP-E-07: "un descarte silencioso
    aqui seria un enlace perdido").

(d) EL RESULTADO es una bolsa re-basada con su cifra, escrita a fichero
    propio (docs/plan/OP_E_06_REBASE_V88.jsonl). La cifra vieja (192) SE
    DEJA DELANTE (no se borra) y la nueva se escribe al lado con su
    medicion. NO SE ESCRIBE NI UNA ARISTA DE OP-E-06 EN ESTA VUELTA: este
    instrumento NUNCA toca dataset/nodos ni dataset/metadata.

USO:
  python scripts/loop/vuelta88_tarea5_rebase_ope06.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
COSECHA = os.path.join(PLAN, "COSECHA_RAZONES_D.jsonl")
CALIBRADO = os.path.join(PLAN, "PASO_NODO_CALIBRADO.jsonl")
OPERACIONES = os.path.join(PLAN, "OPERACIONES.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
SALIDA = os.path.join(PLAN, "OP_E_06_REBASE_V88.jsonl")

# TAREA 5.b, frente 3: la cola de relectura post fusion (00_INDICE.md linea
# 409, siete puestos), listados en 08_VERIFICACION.md "LA LISTA".
COLA_RELECTURA_POST_FUSION = {707, 1096, 196, 253, 224, 591, 968}

# TAREA 5.c: las palabras de direccion, tal como el acta de la vuelta 87 las
# declaro (CRUDA, no canon). Si un criterio distinto hiciera falta, se
# declara aqui mismo, no en el reporte solo.
PALABRAS_DIRECCION = [
    "madre", "hijo", "padre", "desarrolla", "detalla", "en una linea",
    "en una línea", "procedimiento", "cuelga", "enumera", "menciona", "nombra",
]


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def par_no_dirigido(a, b):
    return tuple(sorted((a, b)))


def resolver_alias(grafo_nodos):
    alias_de = {}
    for nid, n in grafo_nodos.items():
        for a in (n.get("ids_alias") or []):
            if a != nid:
                alias_de[a] = nid

    def resolver(nid):
        visto = {nid}
        cur = nid
        while cur in alias_de:
            siguiente = alias_de[cur]
            if siguiente in visto:
                break
            visto.add(siguiente)
            cur = siguiente
        return cur

    return resolver


def main():
    # --- (a) TALLA DE LOS 192 Y LOS 101 ---
    filas = cargar_jsonl(COSECHA)
    nuevos = [r for r in filas if r.get("nuevo")]
    cubiertos = [r for r in filas if not r.get("nuevo")]
    solo_continua = [r for r in nuevos if r.get("senales") == ["continua por la vara"]]
    con_otra_senal = [r for r in nuevos if r.get("senales") != ["continua por la vara"]]

    print("=" * 90)
    print("TAREA 5.a: LOS 192 Y LOS 101, TALLADOS DE docs/plan/COSECHA_RAZONES_D.jsonl")
    print("=" * 90)
    print("filas totales: %d" % len(filas))
    print("nuevo=true: %d" % len(nuevos))
    print("cubiertos (nuevo=false): %d" % len(cubiertos))
    print("nuevos con senales == ['continua por la vara'] (candidatos OP-E-07): %d" % len(solo_continua))
    print("nuevos con OTRA senal (candidatos OP-E-06): %d" % len(con_otra_senal))
    print()
    reparto = {}
    for r in con_otra_senal:
        reparto[r["dominio"]] = reparto.get(r["dominio"], 0) + 1
    print("reparto por dominio de los candidatos OP-E-06:")
    for dom, n in sorted(reparto.items(), key=lambda kv: -kv[1]):
        print("  %-14s %d" % (dom, n))
    print()

    bolsa = con_otra_senal

    # --- (b) LOS CUATRO FRENTES DEL DEDUPE ---
    print("=" * 90)
    print("TAREA 5.b: LOS CUATRO FRENTES DEL DEDUPE, SOBRE EL GRAFO DE HOY")
    print("=" * 90)

    # Frente 1: bolsa PASO_NODO_CALIBRADO.jsonl (madre/hijo, no dirigido)
    calibrado = cargar_jsonl(CALIBRADO)
    pares_calibrado = {par_no_dirigido(r["madre"], r["hijo"]) for r in calibrado}
    quitados_f1 = [r for r in bolsa if par_no_dirigido(r["nodo_a"], r["nodo_b"]) in pares_calibrado]
    bolsa = [r for r in bolsa if par_no_dirigido(r["nodo_a"], r["nodo_b"]) not in pares_calibrado]
    print("FRENTE 1, contra la bolsa de PASO_NODO_CALIBRADO.jsonl (%d filas hoy): quita %d"
          % (len(calibrado), len(quitados_f1)))
    if len(quitados_f1) <= 10:
        for r in quitados_f1:
            print("  puesto %s: %s -- %s" % (r["puesto"], r["nodo_a"], r["nodo_b"]))
    print()

    # Frente 2: aristas ya declaradas por otras operaciones (campo
    # aristas_nuevas de OPERACIONES.jsonl, cualquier operacion)
    ops = cargar_jsonl(OPERACIONES)
    patron_flecha = re.compile(r"([a-z0-9_]{4,})\s*->\s*([a-z0-9_]{4,})")
    pares_declarados = set()
    for d in ops:
        for texto in (d.get("aristas_nuevas") or []):
            for m in patron_flecha.finditer(texto):
                pares_declarados.add(par_no_dirigido(m.group(1), m.group(2)))
    quitados_f2 = [r for r in bolsa if par_no_dirigido(r["nodo_a"], r["nodo_b"]) in pares_declarados]
    bolsa = [r for r in bolsa if par_no_dirigido(r["nodo_a"], r["nodo_b"]) not in pares_declarados]
    print("FRENTE 2, contra %d pares ya declarados en aristas_nuevas de otras operaciones: quita %d"
          % (len(pares_declarados), len(quitados_f2)))
    if len(quitados_f2) <= 10:
        for r in quitados_f2:
            print("  puesto %s: %s -- %s" % (r["puesto"], r["nodo_a"], r["nodo_b"]))
    print()

    # Frente 3: cola de relectura post fusion (por puesto)
    quitados_f3 = [r for r in bolsa if r["puesto"] in COLA_RELECTURA_POST_FUSION]
    bolsa = [r for r in bolsa if r["puesto"] not in COLA_RELECTURA_POST_FUSION]
    print("FRENTE 3, contra los 7 puestos de la cola de relectura post fusion: quita %d"
          % len(quitados_f3))
    if quitados_f3:
        for r in quitados_f3:
            print("  puesto %s: %s -- %s" % (r["puesto"], r["nodo_a"], r["nodo_b"]))
    print()

    # Frente 4: pares que YA tienen arista en el grafo de hoy, resolviendo
    # por alias. Ademas, medicion de contraste (deprecado / inexistente).
    grafo = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    resolver = resolver_alias(grafo)

    def existe_arista(a, b):
        ra, rb = resolver(a), resolver(b)
        na, nb = grafo.get(ra), grafo.get(rb)
        if na is None or nb is None:
            return False
        if rb in (na.get("nodos_siguientes") or []) or ra in (nb.get("nodos_previos") or []):
            return True
        if ra in (nb.get("nodos_siguientes") or []) or rb in (na.get("nodos_previos") or []):
            return True
        return False

    quitados_f4 = [r for r in bolsa if existe_arista(r["nodo_a"], r["nodo_b"])]
    bolsa = [r for r in bolsa if not existe_arista(r["nodo_a"], r["nodo_b"])]
    print("FRENTE 4, contra pares con arista YA en el grafo de hoy (resolviendo por alias): quita %d"
          % len(quitados_f4))
    if len(quitados_f4) <= 10:
        for r in quitados_f4:
            print("  puesto %s: %s -- %s" % (r["puesto"], r["nodo_a"], r["nodo_b"]))
    print()

    # Medicion de contraste, sobre los 192 originales completos (no sobre lo
    # que ya filtraron los frentes 1 a 3), para poder contrastar linea a
    # linea contra la vara del acta de la vuelta 87.
    tocan_deprecado = 0
    tocan_inexistente = 0
    ya_tienen_arista_alias = 0
    for r in con_otra_senal:
        a, b = r["nodo_a"], r["nodo_b"]
        na_existe = a in grafo
        nb_existe = b in grafo
        if not na_existe or not nb_existe:
            tocan_inexistente += 1
            continue
        if grafo[a].get("deprecado") or grafo[b].get("deprecado"):
            tocan_deprecado += 1
        if existe_arista(a, b):
            ya_tienen_arista_alias += 1
    print("MEDICION DE CONTRASTE sobre los 192 originales completos (no el remanente):")
    print("  ya tienen arista hoy (resolviendo por alias): %d" % ya_tienen_arista_alias)
    print("  tocan un nodo DEPRECADO hoy: %d" % tocan_deprecado)
    print("  tocan un id que ya no existe en el grafo: %d" % tocan_inexistente)
    print("  (vara del acta de la vuelta 87, definicion ESTRICTA SIN ALIAS: 6 / 36 / 0.")
    print("   Si estos numeros difieren de esos, es diferencia de definicion (con alias")
    print("   contra sin alias), declarada aqui y no resuelta copiando.)")
    print()

    # --- (c) LA DIRECCION SE LEE ---
    print("=" * 90)
    print("TAREA 5.c: LA DIRECCION SE LEE (palabras: %s)" % ", ".join(PALABRAS_DIRECCION))
    print("=" * 90)
    con_direccion = []
    sin_direccion = []
    for r in bolsa:
        frase = (r.get("frase") or "").lower()
        if any(p in frase for p in PALABRAS_DIRECCION):
            con_direccion.append(r)
        else:
            sin_direccion.append(r)
    print("CON alguna palabra de direccion (siguen en la bolsa): %d" % len(con_direccion))
    print("SIN ninguna palabra de direccion (SE DESCARTAN, contados y nombrados): %d" % len(sin_direccion))
    literal_ninguno = [r for r in sin_direccion if r.get("frase", "").strip() == "Ninguno enlaza al otro."]
    print("  de esos, frase literal 'Ninguno enlaza al otro.': %d" % len(literal_ninguno))
    print()
    print("LOS DESCARTADOS POR FALTA DE DIRECCION, TODOS NOMBRADOS (nunca silencioso):")
    for r in sin_direccion:
        print("  puesto %s (%s): %s -- %s | frase: %s"
              % (r["puesto"], r["dominio"], r["nodo_a"], r["nodo_b"], r["frase"]))

    bolsa_rebasada = con_direccion

    # --- (d) EL RESULTADO, A FICHERO PROPIO ---
    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as fh:
        for r in bolsa_rebasada:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    print()
    print("=" * 90)
    print("TAREA 5.d: EL RESULTADO")
    print("=" * 90)
    print("CIFRA VIEJA (12 ago 2026, ficha de OP-E-06, se deja delante, no se borra): 192")
    print("CIFRA NUEVA (28 ago 2026, vuelta 88, re-basada sobre el grafo de hoy): %d" % len(bolsa_rebasada))
    print("escrito: %s" % SALIDA)
    print()
    print("NO SE ESCRIBIO NINGUNA ARISTA DE OP-E-06 EN ESTA VUELTA. La vuelta 89 abre")
    print("la operacion con esta bolsa, no con la de la ficha del 12 ago 2026.")


if __name__ == "__main__":
    main()
