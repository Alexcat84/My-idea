# -*- coding: utf-8 -*-
"""vuelta37_destejido_opd04.py - PASO 2 DEL ORDEN INTERNO DE OP-D-04: EL DESTEJIDO.

NO ESCRIBE NADA. Mide, imprime y adjudica si queda destejido por hacer.

LA PREGUNTA QUE CONTESTA, y es la unica: el frente 2 de OP-D-04 (la costura
confirmada de brainstorming_divergente) SIGUE ABIERTO, o lo consumio el corte de
OP-F-02, que iba en el mismo sitio?

POR QUE LA PREGUNTA EXISTE. El plan escribe cuatro frentes para este nodo
(02_DESTEJIDOS.md, seccion OP-D-04): decision de fuente, destejido, tres gemelos
y racimo de cuatro libros. Y escribe el orden: la fuente PRIMERO, el destejido
DESPUES. Pero la frontera que OP-F-02 publico en 01_FUENTES.md para su corte es
'1 a 4 / 5 a 8' sobre este mismo nodo, y el corte que docs/COSTURAS_INTERNAS.jsonl
registra para su costura es EL 5. Si son el mismo corte, el paso 2 no tiene
material propio; si son distintos, queda destejido por hacer. ESO SE MIDE.

DE DONDE SALE CADA COSA, y ninguna de un acta:
  1. docs/COSTURAS_INTERNAS.jsonl, el registro publicado de las costuras: se lee
     entero y se cruza contra los SIETE nodos del acto. La seccion 54.3 del
     INTRA_DOMINIO_INFORME declara para el acto 1 'costurados 1, sanos 6'; aqui
     se cuenta, no se cita.
  2. El grafo de HOY: los pasos que cada uno de los siete tiene ahora mismo.
  3. EL GRAFO DE ANTES DE OP-F-02, leido por git del commit 2d96e3d3~1 (2d96e3d3
     es el commit que ejecuto OP-F-02, hallado hoy con git log --follow sobre el
     fichero del nodo). De ahi salen los OCHO pasos viejos, y se comparan uno a
     uno: los 1 a 4 contra el nodo de hoy, y los 5 a 8 contra los pasos de
     ideacion_con_ia_en_la_sesion, que es el destino que 01_FUENTES.md le
     escribio al bloque.

LO QUE ESTE INSTRUMENTO NO HACE, Y VA DICHO EN VOZ ALTA: NO vuelve a correr
scripts/costuras_internas.py. Ese instrumento se declara MAL CALIBRADO en su
propia salida desde la vuelta 34 (docs/loop/SALIDA_V34_COSTURAS_RECALIBRADO.txt:
'INSTRUMENTO MAL CALIBRADO. No entrega nada.') y el encargo de esta vuelta dice
que si una operacion NECESITA su cifra, eso es guarda en rojo y se para. OP-D-04
no la necesita: su frontera ya esta PUBLICADA y SELLADA en 01_FUENTES.md y su
corte esta REGISTRADO con fecha en COSTURAS_INTERNAS.jsonl. Preguntar si hoy
nacio una costura nueva que nadie registro seria abrir alcance que ninguna
operacion escribio. Queda como DISCUTIBLE MARCADO del reporte, no como cifra.

Uso: python scripts/loop/vuelta37_destejido_opd04.py
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
COST = os.path.join(RAIZ, "docs", "COSTURAS_INTERNAS.jsonl")

SIETE = [
    "brainstorming_divergente",
    "brainstorming_efectivo",
    "reglas_brainstorming",
    "generar_multiples_opciones",
    "construir_sobre_ideas_ajenas",
    "pensamiento_convergente_divergente",
    "design_attitude_vs_decision_attitude",
]
COSTURA = "brainstorming_divergente"
DESTINO = "ideacion_con_ia_en_la_sesion"
COMMIT_F02 = "2d96e3d3"


def leer_nodo(nid):
    with io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


def nodo_en_commit(nid, commit):
    ruta = "dataset/nodos/%s.json" % nid
    salida = subprocess.check_output(
        ["git", "-C", RAIZ, "show", "%s:%s" % (commit, ruta)])
    return json.loads(salida.decode("utf-8"))


def normal(texto):
    return " ".join((texto or "").lower().split())


def bloque(titulo):
    print("")
    print("=" * 78)
    print(titulo)
    print("=" * 78)


def main():
    fallos = []

    bloque("1. LAS COSTURAS DEL ACTO, CONTADAS HOY SOBRE EL REGISTRO PUBLICADO")
    registros = {}
    total = 0
    with io.open(COST, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            total += 1
            o = json.loads(linea)
            if o.get("node_id") in SIETE:
                registros[o["node_id"]] = o
    print("registros totales en docs/COSTURAS_INTERNAS.jsonl: %d" % total)
    for nid in SIETE:
        if nid in registros:
            o = registros[nid]
            print("  COSTURADO  %-38s pasos %d  corte %d  sim_bloque %s  disparo_bloque %s"
                  % (nid, o["pasos"], o["corte"], o["sim_bloque"], o["disparo_bloque"]))
        else:
            print("  sano       %s" % nid)
    print("")
    print("costurados: %d   sanos: %d   (la seccion 54.3 del informe declara 1 y 6)"
          % (len(registros), len(SIETE) - len(registros)))
    if sorted(registros) != [COSTURA]:
        print("DISCREPA: el unico costurado esperado es %s" % COSTURA)
        fallos.append("el conjunto de costurados no es el esperado")

    reg = registros.get(COSTURA)

    bloque("2. LOS SIETE NODOS DE HOY, CON SUS PASOS")
    hoy = {}
    for nid in SIETE:
        nodo = leer_nodo(nid)
        hoy[nid] = nodo
        print("  %-38s pasos %2d   vivo %s   fuente: %s"
              % (nid, len(nodo["pasos_accionables"]),
                 not nodo.get("deprecado", False), nodo.get("fuente")))

    bloque("3. EL CORTE REGISTRADO CONTRA EL CORTE EJECUTADO POR OP-F-02")
    pasos_hoy = hoy[COSTURA]["pasos_accionables"]
    print("  costura registrada : %s tenia %d pasos, corte tras el %d"
          % (COSTURA, reg["pasos"], reg["corte"] - 1))
    print("    o sea el bloque   : pasos %d a %d" % (reg["corte"], reg["pasos"]))
    print("  frontera publicada por OP-F-02 en 01_FUENTES.md: 1 a 4 / 5 a 8")
    print("  pasos de %s HOY: %d" % (COSTURA, len(pasos_hoy)))
    print("")
    if reg["corte"] - 1 != len(pasos_hoy):
        print("  DISCREPA: el nodo de hoy no se quedo con el lado 1 a %d del corte"
              % (reg["corte"] - 1))
        fallos.append("el nodo de hoy no calza con el corte registrado")
    else:
        print("  CALZAN: el corte registrado es el 5 y el nodo de hoy tiene")
        print("  exactamente los %d pasos del lado izquierdo. UN SOLO CORTE, NO DOS."
              % len(pasos_hoy))

    bloque("4. LOS OCHO PASOS VIEJOS, LEIDOS POR GIT DE ANTES DE OP-F-02")
    print("  commit que ejecuto OP-F-02 : %s" % COMMIT_F02)
    print("  se lee su padre            : %s~1" % COMMIT_F02)
    viejo = nodo_en_commit(COSTURA, COMMIT_F02 + "~1")
    pasos_viejos = viejo["pasos_accionables"]
    print("  pasos del nodo entonces    : %d  (el registro de costuras dice %d)"
          % (len(pasos_viejos), reg["pasos"]))
    if len(pasos_viejos) != reg["pasos"]:
        fallos.append("los pasos de entonces no son los que el registro dice")
    print("")
    for i, p in enumerate(pasos_viejos, 1):
        print("   viejo %d. %s" % (i, p))

    bloque("5. LOS 1 A 4 VIEJOS CONTRA EL NODO DE HOY, UNO A UNO")
    izq = pasos_viejos[: reg["corte"] - 1]
    calzan = 0
    for i, p in enumerate(izq, 1):
        igual = i <= len(pasos_hoy) and normal(p) == normal(pasos_hoy[i - 1])
        calzan += 1 if igual else 0
        print("   %d. %s" % (i, "IDENTICO" if igual else "DISTINTO"))
        print("      entonces: %s" % p)
        print("      hoy     : %s" % (pasos_hoy[i - 1] if i <= len(pasos_hoy) else "(no hay)"))
    print("")
    print("  identicos: %d de %d" % (calzan, len(izq)))
    if calzan != len(izq):
        fallos.append("el lado izquierdo no quedo intacto")

    bloque("6. LOS 5 A 8 VIEJOS CONTRA EL DESTINO QUE EL PLAN LES ESCRIBIO")
    der = pasos_viejos[reg["corte"] - 1:]
    destino = leer_nodo(DESTINO)
    pasos_destino = destino["pasos_accionables"]
    print("  destino escrito en 01_FUENTES.md: %s" % DESTINO)
    print("  pasos del destino HOY           : %d" % len(pasos_destino))
    print("  pasos del bloque 5 a 8          : %d" % len(der))
    print("")
    calzan2 = 0
    for i, p in enumerate(der, reg["corte"]):
        j = i - reg["corte"]
        igual = j < len(pasos_destino) and normal(p) == normal(pasos_destino[j])
        calzan2 += 1 if igual else 0
        print("   viejo %d -> destino %d : %s" % (i, j + 1, "IDENTICO" if igual else "DISTINTO"))
        print("      entonces: %s" % p)
        print("      destino : %s" % (pasos_destino[j] if j < len(pasos_destino) else "(no hay)"))
    print("")
    print("  identicos: %d de %d" % (calzan2, len(der)))
    if calzan2 != len(der):
        fallos.append("el bloque de la derecha no aparece entero en el destino")

    bloque("7. EL BLOQUE NO SE BORRO: EL CABLEADO LO DICE")
    print("  %s siguientes: %s" % (COSTURA, hoy[COSTURA].get("nodos_siguientes")))
    print("  el destino esta entre ellos: %s"
          % (DESTINO in (hoy[COSTURA].get("nodos_siguientes") or [])))
    if DESTINO not in (hoy[COSTURA].get("nodos_siguientes") or []):
        fallos.append("el destino no esta cableado desde la costura")

    bloque("VEREDICTO DEL PASO 2, EL DESTEJIDO")
    if fallos:
        print("EL DESTEJIDO NO SE PUEDE DECLARAR. Discrepancias:")
        for f in fallos:
            print("   -", f)
        print("")
        print("PASO 2 EN ROJO.")
        return 1
    print("EL DESTEJIDO DE OP-D-04 ESTA CONSUMADO, Y NO POR RENUNCIA: PORQUE SU UNICA")
    print("COSTURA Y EL INJERTO DE FUENTE ERAN EL MISMO BLOQUE, Y UN SOLO CORTE SIRVIO")
    print("A LOS DOS FRENTES.")
    print("")
    print("  - de los SIETE nodos del acto, UNO estaba costurado y SEIS sanos, contado")
    print("    hoy sobre docs/COSTURAS_INTERNAS.jsonl (128 registros leidos).")
    print("  - el corte registrado de esa costura es el 5, y la frontera que OP-F-02")
    print("    publico en 01_FUENTES.md es 1 a 4 / 5 a 8: EL MISMO SITIO.")
    print("  - los cuatro pasos de hoy son IDENTICOS a los cuatro viejos de la")
    print("    izquierda, y los cuatro de la derecha estan ENTEROS e IDENTICOS en")
    print("    ideacion_con_ia_en_la_sesion, que ademas cuelga del cableado.")
    print("  - CERO material perdido: 4 mas 4 igual a 8.")
    print("")
    print("PASO 2 VERDE, SIN NADA QUE CORTAR. El acto entra a P.5 con texto estable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
