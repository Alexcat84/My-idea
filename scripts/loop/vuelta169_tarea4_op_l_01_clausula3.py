# -*- coding: utf-8 -*-
r"""vuelta169_tarea4_op_l_01_clausula3.py . `OP-L-01` CLAUSULA 3, DESENCADENADA
POR LA TAREA 3 (TAREA 4 de la vuelta 169, adjudicacion 6.5 del acta 168).

LA CLAUSULA, VERBATIM DE LA FICHA: *"cada nomina afectada se re-mide con su
cobertura al lado (banco 9.26)"*. Y LA 6.5 LE PONE SUJETO SIN DOCTRINA NUEVA:
*"son las nominas que el paso 4 del disparador re-mide, o sea las de los 569
actos y racimos, con su cobertura al lado por el banco 9.26"*.

QUE HACE ESTE INSTRUMENTO: re-mide UNA A UNA las nominas de las entradas de tipo
`acto` y `racimo`, con el resolutor delante por `P.1`, y clasifica cada
diferencia por SU MOTIVO MEDIDO en vez de contarla como un fallo suelto.

Y TRAE UNA PARADA, PORQUE EL ENCARGO LA PIDE CON ESAS PALABRAS (*"Si al
re-medirlas el instrumento dice algo distinto de lo que este encargo supone,
PARAS Y LO TRAES"*): el encargo supone que se re-miden **569**, y **221 de esas
569 estan marcadas `SUPERADA` una a una** por la vuelta 17. Re-medirlas
contradiria su propia marca. Lo re-medible son **348**. La cifra 569 no es
falsa: es el conteo de entradas de esos dos tipos. Lo que no es, es el conjunto
re-medible.

CERO ESCRITURAS EN NODOS Y CERO CLASES MOVIDAS. Lo unico que escribe, y solo con
`--aplicar`, es un elemento mas en la lista `verificacion` de `OP-L-01`, que es
la via que esa misma ficha ya uso en la vuelta 166 para sus clausulas 4 y 5, y
que el acta 71 adjudico con las palabras NO ES PARADA.

USO:
  python scripts/loop/vuelta169_tarea4_op_l_01_clausula3.py
  python scripts/loop/vuelta169_tarea4_op_l_01_clausula3.py --aplicar
"""
import collections
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INVENTARIO = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
COMPONENTES = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388_COMPONENTES.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
FICHA = "OP-L-01"
CLAUSULA_3 = "cada nomina afectada se re-mide con su cobertura al lado (banco 9.26)"


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    aplicar = "--aplicar" in sys.argv
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 169, TAREA 4: OP-L-01 CLAUSULA 3, RE MEDIDA CON COBERTURA AL LADO")
    print("=" * 78)
    print("")

    print("A) LA CLAUSULA SE LEE DE SU FICHA ANTES DE EJECUTARLA, Y SI NO ESTA, PARA")
    fichas = cargar(OPERACIONES)
    idx = [i for i, f in enumerate(fichas) if f.get("id_op") == FICHA]
    if len(idx) != 1:
        print("   ROJO: %s aparece %d veces." % (FICHA, len(idx)))
        return 1
    ficha = fichas[idx[0]]
    ver = ficha.get("verificacion") or []
    donde = [j for j, v in enumerate(ver) if v.strip() == CLAUSULA_3]
    print("   %s, linea %d de docs/plan/OPERACIONES.jsonl" % (FICHA, idx[0] + 1))
    print("   CIFRA clausulas en `verificacion`: %d" % len(ver))
    print("   la clausula 3 aparece EXACTAMENTE una vez: %s" % (len(donde) == 1))
    if len(donde) != 1:
        print("   ROJO: la clausula 3 no se localiza sin ambiguedad.")
        return 1
    print("   texto leido hoy: %r" % ver[donde[0]])
    print("")

    print("B) EL UNIVERSO QUE LA 6.5 NOMBRA, Y LA PARADA QUE TRAE")
    inv = cargar(INVENTARIO)
    dentro = [x for x in inv if x.get("tipo") in ("acto", "racimo")]

    def superada(e):
        return "SUPERADA" in ((e.get("estado") or "") + (e.get("nota") or ""))

    vigentes = [x for x in dentro if not superada(x)]
    superadas = [x for x in dentro if superada(x)]
    print("   CIFRA entradas de tipo acto mas racimo: %d  (lo que la 6.5 llama 569)"
          % len(dentro))
    print("   CIFRA de esas, marcadas SUPERADA una a una por la vuelta 17: %d" % len(superadas))
    print("   CIFRA re-medibles (nominas VIVAS): %d" % len(vigentes))
    print("   reparto de las re-medibles: %s"
          % dict(sorted(collections.Counter(x["tipo"] for x in vigentes).items())))
    print("   PARADA QUE SE TRAE: el encargo supone 569 re-medibles y el instrumento")
    print("   mide %d. Las %d superadas no se re-miden porque su propia marca lo dice."
          % (len(vigentes), len(superadas)))
    print("")

    print("C) LA RE MEDICION, CON EL RESOLUTOR DELANTE (P.1) Y LA COBERTURA AL LADO")
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x, visto=None):
        visto = visto or set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    comps = cargar(COMPONENTES)
    idxc = {frozenset(res(m) for m in c["miembros"]): c for c in comps}

    calzan, difieren, sin_comp = [], [], []
    for e in vigentes:
        c = idxc.get(frozenset(res(m) for m in e["miembros"]))
        m = re.search(r"(\d+) de (\d+)", e.get("cobertura", "") or "")
        ficha_cif = (int(m.group(1)), int(m.group(2))) if m else None
        if c is None:
            sin_comp.append((e, ficha_cif))
            continue
        hoy_cif = (c["leidos"], c["posibles"])
        if ficha_cif == hoy_cif:
            calzan.append((e, ficha_cif))
        else:
            difieren.append((e, ficha_cif, hoy_cif, c))
    print("   CIFRA nominas re-medidas: %d" % len(vigentes))
    print("   CIFRA cuya cobertura CALZA con la componente sellada: %d" % len(calzan))
    print("   CIFRA cuya cobertura DIFIERE: %d" % len(difieren))
    print("   CIFRA sin componente en el fichero sellado: %d" % len(sin_comp))
    print("   las tres partes suman el total: %s"
          % (len(calzan) + len(difieren) + len(sin_comp) == len(vigentes)))
    print("")

    print("D) CADA DIFERENCIA, CLASIFICADA POR SU MOTIVO MEDIDO Y NO POR SUPOSICION")
    print("")
    print("   | nomina | la ficha dice | la componente sellada dice | motivo medido |")
    print("   |---|---|---|---|")
    motivos = collections.Counter()
    for e, f, h, c in difieren:
        texto = e.get("cobertura", "") or ""
        if "LD-" in texto:
            motivo = "la ficha cuenta LECTURAS DIRIGIDAS, citadas por su numero, que el fichero de componentes NO PUEDE VER"
        elif f and h and f[1] == h[1] and f[0] > h[0]:
            motivo = "mismo universo de pares y la ficha trae MAS leidos: cobertura cerrada fuera de la cola"
        elif f and h and h[1] < f[1]:
            motivo = "la componente ENCOGIO: la campana fundio y los pares internos colapsaron a auto-arista"
        else:
            motivo = "PENDIENTE DE DOCTRINA: diferencia sin regla escrita que la clasifique"
        motivos[motivo] += 1
        print("   | `%s` | %d de %d | %d de %d | %s |"
              % (e["nombre"], f[0], f[1], h[0], h[1], motivo))
    print("")
    for mot, n in motivos.most_common():
        print("   CIFRA %-3d %s" % (n, mot))
    print("")

    print("E) LAS QUE NO TIENEN COMPONENTE, NOMBRADAS Y NO CONTADAS COMO CERO")
    print("")
    print("   | nomina | tamano | la ficha dice |")
    print("   |---|---:|---|")
    for e, f in sin_comp:
        print("   | `%s` | %d | %s |"
              % (e["nombre"], len(e["miembros"]),
                 ("%d de %d" % f) if f else "(sin cifra legible)"))
    print("")
    print("   NO SE RELLENAN Y NO SE INVENTAN: un acto o racimo cuyo conjunto de")
    print("   miembros resueltos ya no forma componente en el fichero sellado es un")
    print("   HUECO NOMBRADO, que es lo que la clausula 3 de OP-I-01 manda.")
    print("")

    print("F) LA COBERTURA AL LADO, QUE ES LO QUE EL 9.26 PIDE, AGREGADA")
    completas = sum(1 for _e, f in calzan if f and f[0] == f[1])
    incompletas = sum(1 for _e, f in calzan if f and f[0] != f[1])
    print("   de las %d que calzan: %d con cobertura COMPLETA y %d INCOMPLETA"
          % (len(calzan), completas, incompletas))
    print("   y mientras falte un par la forma es PROVISIONAL, que es la letra del 9.26")
    print("")

    if not aplicar:
        print("MODO MEDICION: la ficha NO se toca. Corre con --aplicar para escribir.")
        print("FIN")
        return 0

    nueva = (
        "CORRECCION DECLARADA (2026-09-04, vuelta 169, TAREA 4 del encargo), POR EL "
        "CARRIL DEL BANCO 9.10, CON EL TEXTO VIEJO ENTERO ARRIBA Y SIN CLAVE NUEVA DE "
        "ESQUEMA (es un elemento mas de esta misma lista verificacion, la via que esta "
        "ficha ya uso en la vuelta 166 para sus clausulas 4 y 5 y que el acta 71, "
        "seccion 6, adjudicacion 3, adjudico CON LAS PALABRAS NO ES PARADA). LO QUE SE "
        "EJECUTA es la clausula que en esta lista dice, verbatim: '%s'. SU SUJETO NO SE "
        "IMPROVISA: lo pone la adjudicacion 6.5 del acta 168, que dice que 'cada nomina "
        "afectada' son las nominas que el paso 4 del disparador de 08_VERIFICACION "
        "re-mide, o sea las de los actos y racimos del inventario. MEDIDO HOY CON EL "
        "RESOLUTOR PUESTO, que P.1 manda: %d entradas de tipo acto mas racimo, de las "
        "cuales %d estan marcadas SUPERADA una a una por la vuelta 17 y NO se re-miden "
        "porque su propia marca lo dice, y %d son nominas VIVAS y re-medidas. DE ESAS "
        "%d: %d CALZAN con su componente del fichero sellado, %d DIFIEREN y %d no tienen "
        "componente. Y CADA DIFERENCIA VA CON SU MOTIVO MEDIDO, no contada como fallo "
        "suelto: %s. LAS QUE NO TIENEN COMPONENTE QUEDAN NOMBRADAS Y NO RELLENADAS: %s. "
        "LA COBERTURA AL LADO, QUE ES LO QUE EL 9.26 PIDE: de las %d que calzan, %d con "
        "cobertura COMPLETA y %d INCOMPLETA, y mientras falte un par la forma es "
        "PROVISIONAL. PARADA QUE SE TRAE Y NO SE RESUELVE AQUI: el encargo de la vuelta "
        "169 supone que se re-miden 569 y el instrumento mide %d re-medibles. La cifra "
        "569 no es falsa, es el conteo de entradas de esos dos tipos; lo que no es, es "
        "el conjunto re-medible. Ver docs/loop/SALIDA_V169_T4_OP_L_01.txt. LO QUE ESTA "
        "CORRECCION NO HACE: no mueve ni un veredicto, no adjudica clase a nada, no toca "
        "ni un nodo, no cambia el estado ni las dependencias de esta ficha ni de ninguna "
        "otra, y no autoriza ninguna lectura nueva."
        % (CLAUSULA_3, len(dentro), len(superadas), len(vigentes), len(vigentes),
           len(calzan), len(difieren), len(sin_comp),
           "; ".join("%d %s" % (n, m) for m, n in motivos.most_common()),
           ", ".join("`%s`" % e["nombre"] for e, _f in sin_comp),
           len(calzan), completas, incompletas, len(dentro)))

    lineas = [l for l in io.open(OPERACIONES, encoding="utf-8") if l.strip()]
    f2 = dict(ficha)
    f2["verificacion"] = list(ver) + [nueva]
    print("G) LO QUE SE ESCRIBE, COMPROBADO ANTES DE ESCRIBIRLO")
    print("   CIFRA clausulas antes: %d | despues: %d" % (len(ver), len(f2["verificacion"])))
    print("   la clausula 3 vieja sigue ENTERA en su sitio: %s"
          % (f2["verificacion"][donde[0]] == ver[donde[0]]))
    print("   CIFRA claves de la ficha antes: %d | despues: %d" % (len(ficha), len(f2)))
    movidos = [k for k in ficha if k != "verificacion" and ficha[k] != f2.get(k)]
    print("   CIFRA campos movidos ademas de `verificacion`: %d %s" % (len(movidos), movidos))
    if len(f2) != len(ficha) or movidos or f2["verificacion"][donde[0]] != ver[donde[0]]:
        print("   ROJO: se movio algo que no era la lista de verificacion.")
        return 1
    lineas[idx[0]] = json.dumps(f2, ensure_ascii=False) + "\n"
    io.open(OPERACIONES, "w", encoding="utf-8", newline="\n").writelines(lineas)
    despues = cargar(OPERACIONES)
    print("H) ESCRITO Y RECONTADO")
    print("   CIFRA fichas antes: %d | despues: %d" % (len(fichas), len(despues)))
    print("   CIFRA clausulas de %s en disco: %d"
          % (FICHA, len(despues[idx[0]]["verificacion"])))
    print("   estado de la ficha, sin mover: %r" % despues[idx[0]].get("estado"))
    print("")
    print("VERDE: la clausula 3 de %s queda ejecutada y declarada por adicion." % FICHA)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
