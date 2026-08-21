# -*- coding: utf-8 -*-
"""vuelta64_d10.py . LA RELECTURA CONJUNTA DEL D10 DEL ACTA 63, MEDIDA CONTRA
EL GRAFO DE HOY, Y SU CORRECCION DECLARADA SOBRE docs/loop/PLAN_V63_OPM02PROG.json.

EL CASO, tal como el auditor lo escribio (acta 63, seccion 4, D10): la condicion 1
de fases_de_retencion_de_clientes quedo marcada CUBIERTO:1 SIN perdida sellada, y
ese mismo dia OP-M-03-I sello DOS perdidas DE CONDICIONES por la misma especie, el
matiz del disparador que muere sin sello. El auditor NO adjudica: manda verificar
contra el grafo y decidir con la vara del acta 55, pregunta 5.

LO QUE ESTE INSTRUMENTO HACE, en este orden:
  1. IMPRIME EL TEXTO DE HOY de los dos nodos (pasos y condiciones, verbatim del
     json vivo), que es lo unico que puede sostener la decision;
  2. PONE AL LADO las DOS perdidas DE CONDICIONES que OP-M-03-I sello el mismo
     dia, leidas de su plan sellado y no de un acta, para que la comparacion de
     especie sea de textos y no de recuerdos;
  3. EXTRAE VERBATIM del plan la frase que hoy dice que esa condicion va sin
     perdida, y cae en ROJO si no la encuentra: el texto viejo se cita, no se
     resume;
  4. con --escribir, SELLA LA PERDIDA en el campo perdidas del acto y adosa la
     CORRECCION DECLARADA al final de nota_del_reparto, sin borrar ni tachar una
     sola palabra de lo que habia.

NADA DEL GRAFO SE TOCA: la fusion esta ejecutada, registrada y auditada, y la
correccion es DE REGISTRO. El nodo no se reabre.

Uso: python scripts/loop/vuelta64_d10.py [--escribir]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
PLAN = os.path.join(RAIZ, "docs", "loop", "PLAN_V63_OPM02PROG.json")
PLAN_I = os.path.join(RAIZ, "docs", "loop", "PLAN_V63_OPM03I.json")
SUP = "ocho_fases_experiencia_cliente"
MUERTO = "fases_de_retencion_de_clientes"
MARCA = "CORRECCION DECLARADA (2026-08-20, vuelta 64, TAREA 1.b del encargo"
AGUJA = "y por eso va CUBIERTA y SIN perdida"

PERDIDA = {
    "especie": "DE CONDICIONES",
    "que": ("el encuadre del sintoma: que la empresa SOLO TIENE PROCESOS DISENADOS "
            "PARA ATRAER Y CERRAR VENTAS, que es el diagnostico por el que un lector "
            "se reconoce a si mismo en el disparador; la condicion 1 del superviviente "
            "dispara por NECESITAR UNA ESTRUCTURA SISTEMATICA para gestionar la "
            "experiencia del cliente despues de la venta, que nombra la necesidad y no "
            "el hueco que la produce. SE DICE LO QUE NO SE PIERDE, y por eso la marca "
            "NO cambia: lo operativo, el DESPUES DE LA VENTA, esta en el texto del "
            "superviviente con todas sus letras, asi que la condicion sigue CUBIERTA:1 "
            "y lo que se anade es el sello de la mitad que muere"),
    "donde": "condicion 1 de fases_de_retencion_de_clientes",
    "enrutada_a": ("la fase 04, mientras el INCISO de condiciones no exista "
                   "(acta 55, pregunta 5)"),
}


def nodo(n):
    return json.load(io.open(os.path.join(NODOS, n + ".json"), encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    print("=" * 78)
    print("D10, RELECTURA CONJUNTA: LA CONDICION 1 CUBIERTA SIN PERDIDA SELLADA")
    print("  operacion: OP-M-02-PROG | plan: docs/loop/PLAN_V63_OPM02PROG.json")
    print("=" * 78)

    print()
    print("--- 1. EL TEXTO DE HOY, LEIDO DEL GRAFO VIVO ---")
    for n in (SUP, MUERTO):
        d = nodo(n)
        dep = bool(d.get("deprecado") or d.get("deprecated"))
        print()
        print("  %s  (deprecado: %s)" % (n, dep))
        for etq, campo in (("paso", "pasos_accionables"),
                           ("condicion", "condiciones_activacion")):
            for i, t in enumerate(d.get(campo) or [], 1):
                print("     %-9s %d. %s" % (etq, i, t))

    c_sup = (nodo(SUP).get("condiciones_activacion") or [])
    c_mue = (nodo(MUERTO).get("condiciones_activacion") or [])
    if len(c_sup) < 1 or len(c_mue) < 1:
        print()
        print("ROJO: falta la condicion 1 en alguno de los dos nodos. PARADA.")
        return 1
    print()
    print("--- 2. EL PAR EN DISPUTA, UNO SOBRE OTRO ---")
    print("  MUERE     (condicion 1 de %s): %s" % (MUERTO, c_mue[0]))
    print("  SOBREVIVE (condicion 1 de %s): %s" % (SUP, c_sup[0]))

    print()
    print("--- 3. LA MISMA ESPECIE, SELLADA EL MISMO DIA POR OP-M-03-I ---")
    pi = json.load(io.open(PLAN_I, encoding="utf-8"))
    hermanas = [p for acto in pi["actos"] for p in acto.get("perdidas") or []
                if p["especie"] == "DE CONDICIONES"]
    print("  perdidas DE CONDICIONES en el plan hermano: %d" % len(hermanas))
    for p in hermanas:
        print("     %s | %s" % (p["donde"], p["que"][:190]))

    # LA BUSQUEDA NEGATIVA NO SE PUEDE CITAR SI NO SE CORRE (regla 9): la
    # correccion afirma que el encuadre del sintoma NO vive en el superviviente,
    # y esa afirmacion se mide aqui sobre el json ENTERO del nodo vivo, no solo
    # sobre sus condiciones.
    print()
    print("--- 3b. LA BUSQUEDA NEGATIVA, CORRIDA Y NO CITADA ---")
    entero = json.dumps(nodo(SUP), ensure_ascii=False).lower()
    agujas = ["atraer", "cerrar venta", "cerrar la venta", "solo tiene proceso",
              "procesos dise"]
    hallados = [x for x in agujas if x in entero]
    print("  json ENTERO de %s: %d caracteres" % (SUP, len(entero)))
    for x in agujas:
        print("     %-22s %s" % (x, "PRESENTE" if x in entero else "AUSENTE"))
    print("  agujas del encuadre del sintoma halladas: %d de %d"
          % (len(hallados), len(agujas)))
    if hallados:
        print("  ROJO: el encuadre del sintoma SI vive en el superviviente (%s), "
              "asi que la perdida NO se sella. PARADA." % ", ".join(hallados))
        return 1

    plan = json.load(io.open(PLAN, encoding="utf-8"))
    acto = plan["actos"][0]
    nota = acto["nota_del_reparto"]

    print()
    print("--- 4. EL TEXTO VIEJO, EXTRAIDO VERBATIM DEL PLAN (no resumido) ---")
    if AGUJA not in nota:
        print("  ROJO: no encuentro en nota_del_reparto la frase %r. PARADA." % AGUJA)
        return 1
    i = nota.index(AGUJA)
    ini = nota.rfind(". ", 0, i) + 2
    fin = nota.find(". ", i + len(AGUJA))
    frase = nota[ini:fin + 1 if fin > 0 else len(nota)].strip()
    print("  %s" % frase)

    print()
    print("--- 5. EL ESTADO DEL CAMPO perdidas ANTES ---")
    print("  contrato: %s | perdidas selladas: %d"
          % (plan.get("contrato_de_perdidas"), len(acto.get("perdidas") or [])))
    for p in (acto.get("perdidas") or []):
        print("     %-22s %s" % (p["especie"], p["donde"]))

    print()
    print("--- 6. LA DECISION, CON SU VARA ---")
    print("  LA VARA es la del acta 55, pregunta 5, con su letra: LAS PERDIDAS DE")
    print("  CONDICIONES NO VAN DE APPEND POR DEFECTO, y LA PERDIDA NOMBRADA ES EL")
    print("  CARRIL MIENTRAS EL PENDIENTE DEL INCISO DE CONDICIONES SIGA ABIERTO.")
    print("  Esa vara reparte DOS marcas, no una: APPEND cuando el disparador es")
    print("  DISTINTO, y CUBIERTO CON LA PERDIDA NOMBRADA cuando es el MISMO")
    print("  disparador con un matiz que muere. Lo que la vara no contempla en")
    print("  ninguna de sus dos ramas es CUBIERTO CON SILENCIO.")
    print()
    print("  MEDIDO ARRIBA, y esto es lo que decide: el disparador operativo (el")
    print("  DESPUES DE LA VENTA) esta en las dos condiciones, asi que el CUBIERTO")
    print("  se sostiene y no se toca; y el encuadre del sintoma (SOLO TIENE")
    print("  PROCESOS PARA ATRAER Y CERRAR VENTAS) NO esta en ningun paso ni en")
    print("  ninguna condicion del superviviente de hoy, o sea que muere.")
    print()
    print("  SE SELLA. Es la misma especie que las dos hermanas de OP-M-03-I")
    print("  (el fenomeno sin la pendiente, el callejon sin la imagen), y tratar")
    print("  igual lo medido igual en la misma vuelta es lo que el acta 55,")
    print("  pregunta 4, llama regla de trabajo DECLARADA Y UNIFORME.")

    if MARCA in json.dumps(plan, ensure_ascii=False):
        print()
        print("YA APLICADA: la marca ya esta en el plan. No se escribe nada.")
        return 0

    correccion = (
        " " + MARCA + ", relectura conjunta del D10 del acta 63; EL TEXTO VIEJO SE "
        "QUEDA ENTERO ARRIBA Y NO SE TACHA, porque una correccion que tapa lo que "
        "corrige no se puede auditar). DONDE ESTA NOTA DICE, CON SUS PALABRAS: " +
        chr(34) + frase + chr(34) + " . LA MARCA SE SOSTIENE Y EL SILENCIO NO. "
        "LA CONDICION SIGUE CUBIERTA:1 y no se remarca: el disparador operativo, el "
        "DESPUES DE LA VENTA, esta en la condicion 1 del superviviente con todas sus "
        "letras, medido HOY sobre el json vivo con scripts/loop/vuelta64_d10.py "
        "(docs/loop/SALIDA_V64_D10.txt). LO QUE SE ANADE ES EL SELLO DE LA MITAD QUE "
        "MUERE, en el campo perdidas de este acto: el ENCUADRE DEL SINTOMA, que la "
        "empresa SOLO TIENE PROCESOS DISENADOS PARA ATRAER Y CERRAR VENTAS, no esta "
        "en ningun paso ni en ninguna condicion del superviviente de hoy, comprobado "
        "en la misma corrida por busqueda sobre su json entero. LA VARA ES LA DEL ACTA 55, PREGUNTA 5, LEIDA ENTERA: "
        "reparte DOS marcas, APPEND para el disparador DISTINTO y CUBIERTO CON LA "
        "PERDIDA NOMBRADA para el MISMO disparador con un matiz que muere, y no "
        "contempla en ninguna de sus dos ramas el CUBIERTO CON SILENCIO. Y ES LA "
        "MISMA ESPECIE QUE LAS DOS HERMANAS QUE OP-M-03-I SELLO EL MISMO DIA (el "
        "mismo fenomeno sin la pendiente, el mismo callejon sin la imagen), leidas "
        "hoy de docs/loop/PLAN_V63_OPM03I.json: tratar igual lo medido igual dentro "
        "de la misma vuelta es la regla de trabajo DECLARADA Y UNIFORME del acta 55, "
        "pregunta 4. LAS PERDIDAS DE ESTE ACTO PASAN DE UNA A DOS, y la cifra que el "
        "registro de la vuelta 63 publico queda corregida por esta nota en vez de "
        "reescrita. NADA DEL GRAFO SE TOCA: la fusion esta ejecutada y auditada y "
        "esto es registro. VA MARCADO COMO DISCUTIBLE EN LA SECCION 6 DEL REPORTE DE "
        "ESTA VUELTA."
    )
    acto["nota_del_reparto"] = nota.rstrip() + correccion
    acto["perdidas"] = list(acto.get("perdidas") or []) + [dict(PERDIDA)]

    print()
    print("--- 7. LO QUE SE ESCRIBE ---")
    print("  perdidas del acto: %d (antes %d)"
          % (len(acto["perdidas"]), len(acto["perdidas"]) - 1))
    print("  perdida nueva: %s | %s" % (PERDIDA["especie"], PERDIDA["donde"]))
    if not a.escribir:
        print("  SIMULACION: sin --escribir no se toca nada.")
        print()
        print("FIN")
        return 0

    io.open(PLAN, "w", encoding="utf-8", newline=chr(10)).write(
        json.dumps(plan, ensure_ascii=False, indent=1) + chr(10))

    print()
    print("GUARDAS TRAS ESCRIBIR")
    p2 = json.load(io.open(PLAN, encoding="utf-8"))
    a2 = p2["actos"][0]
    ok = True
    print("  el plan vuelve a parsear y sigue con %d acto(s)" % len(p2["actos"]))
    print("  contrato intacto: %s" % p2.get("contrato_de_perdidas"))
    print("  perdidas selladas: %d" % len(a2["perdidas"]))
    for p in a2["perdidas"]:
        faltan = [k for k in ("especie", "que", "donde", "enrutada_a") if k not in p]
        if faltan:
            print("  ROJO: a una perdida le faltan %s" % faltan)
            ok = False
        if p["especie"] not in ("DE PARAMETRO DE PASO", "DE CONDICIONES", "DE NOMBRE"):
            print("  ROJO: especie desconocida %r" % p["especie"])
            ok = False
    print("  las CUATRO claves y las tres especies: %s" % ("OK" if ok else "ROJO"))
    print("  el texto viejo sigue dentro: %s" % (AGUJA in a2["nota_del_reparto"]))
    print("  las marcas del acto no se han movido: pasos %s | condiciones %s"
          % (a2["pasos"], a2["condiciones"]))
    t = io.open(PLAN, encoding="utf-8").read()
    largos, medios = t.count(chr(8212)), t.count(chr(8211))
    print("  guiones largos %d, guiones medios %d" % (largos, medios))
    if not ok or AGUJA not in a2["nota_del_reparto"] or largos or medios:
        print()
        print("ROJO EN LAS GUARDAS.")
        return 1
    print()
    print("VERDE: la perdida sellada, el texto viejo entero y el grafo intacto.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
