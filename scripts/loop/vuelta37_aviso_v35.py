# -*- coding: utf-8 -*-
"""vuelta37_aviso_v35.py - EL AVISO DE CORTE FECHADO SOBRE LA PROPUESTA DE LA VUELTA 35.

TAREA 1 del encargo de la vuelta 37, que ejecuta la adjudicacion d6 del acta de
las vueltas 34, 35 y 36 (18 ago 2026): docs/loop/PROPUESTA_V35_RELECTURAS.json
dice en su campo estado "PROPUESTA NO VOLCADA", y eso fue verdad el 15 de agosto
y dejo de serlo el 18. El acta lo nombra por su especie: es el papel que
envejece del banco 9.10.

LA FIGURA ES LA DEL AVISO DE CORTE, NO LA DE LA CORRECCION: el sello de otra
vuelta no se reescribe (criterio del 14 ago 2026), asi que el campo estado NO SE
TOCA y las filas selladas NO SE TOCAN. Lo que se anade es un campo NUEVO y
FECHADO que apunta al volcado. Es el mismo gesto que la vuelta 36 le puso al
apartado b de RECOMPUTO_3388 sin remedirlo.

SUCESOR DECLARADO de scripts/loop/vuelta36_volcado_910.py en una sola cosa (la
lectura de la propuesta) y distinto en todo lo demas: aquel VOLCABA veredictos,
este NO TOCA docs/INTRA_DOMINIO_VEREDICTOS.jsonl ni un byte. Solo escribe el
aviso en el fichero de la propuesta.

LAS GUARDAS SE CORREN HOY, NO SE HEREDAN (EJECUTOR.md regla 2):
  1. los cinco puestos de la propuesta son EXACTAMENTE los cinco del lote
     docs/loop/_lote_v36.jsonl, y el 643 NO esta entre ellos.
  2. el 643 vive en su propio carril, docs/loop/_lote_v36_643.jsonl, el solo.
  3. los seis puestos estan HOY en clase D en el archivo de veredictos: el aviso
     afirma que se volcaron, y esa afirmacion se mide antes de escribirla.
  4. tras escribir: el campo estado queda IDENTICO caracter a caracter, y las
     filas quedan IDENTICAS caracter a caracter (comparacion del JSON serializado
     de antes contra el de despues).

Uso: python scripts/loop/vuelta37_aviso_v35.py
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROP = os.path.join(RAIZ, "docs", "loop", "PROPUESTA_V35_RELECTURAS.json")
LOTE = os.path.join(RAIZ, "docs", "loop", "_lote_v36.jsonl")
LOTE_643 = os.path.join(RAIZ, "docs", "loop", "_lote_v36_643.jsonl")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

CAMPO = "aviso_posterior"
FECHA = "18 ago 2026"

TEXTO = (
    "AVISO DE CORTE, anadido el 19 ago 2026 en la vuelta 37 por la adjudicacion "
    "d6 del acta de las vueltas 34, 35 y 36. EL CAMPO estado DE ARRIBA CONSERVA "
    "SU SELLO Y NO SE TOCA: decia la verdad el 15 de agosto y se deja tal cual, "
    "porque el sello de otra vuelta no se reescribe. LO QUE PASO DESPUES: las "
    "CINCO relecturas de esta propuesta (277, 374, 452, 1571 y 1575) SE VOLCARON "
    "EL " + FECHA + ", en la vuelta 36, por decision del fundador del 15 ago 2026 "
    "escrita en docs/loop/paradas/2026-08-15-p5-rancios-opd03-DECISION.md, y el "
    "instrumento que las volco fue scripts/loop/vuelta36_volcado_910.py con el "
    "lote docs/loop/_lote_v36.jsonl. LAS CINCO PASARON DE A A D. EL 643 NO ESTA "
    "EN ESTA PROPUESTA Y FUE POR SU PROPIO CARRIL: es la lectura dirigida LD-82, "
    "volcada el mismo dia con el lote docs/loop/_lote_v36_643.jsonl, y tambien "
    "de A a D. Este aviso no cambia ni una fila ni una razon de las selladas: "
    "solo fecha lo que el papel de arriba ya no puede decir."
)


def cargar_puestos(ruta):
    puestos = []
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            puestos.append(json.loads(linea)["puesto"])
    return puestos


def clases_de_hoy(puestos):
    # EL ARCHIVO DE VEREDICTOS NOMBRA EL PUESTO 'puesto_intra' Y LO GUARDA COMO
    # CADENA, no como entero: medido hoy sobre la primera linea del fichero. La
    # primera version de este instrumento leyo 'puesto' y la guarda 3 lo canto
    # con SEIS AUSENTES en vez de callarse y dar por bueno el volcado. Queda
    # escrito porque la casa manda fallar ruidoso (banco 9.10).
    buscados = set(str(p) for p in puestos)
    hallados = {}
    with open(VER, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            reg = json.loads(linea)
            clave = str(reg.get("puesto_intra"))
            if clave in buscados:
                hallados[int(clave)] = reg.get("clase")
    return hallados


def main():
    with open(PROP, encoding="utf-8") as fh:
        prop = json.load(fh)

    estado_antes = prop.get("estado")
    filas_antes = json.dumps(prop.get("filas"), ensure_ascii=False, sort_keys=True)

    puestos_prop = [f["puesto"] for f in prop["filas"]]
    puestos_lote = cargar_puestos(LOTE)
    puestos_643 = cargar_puestos(LOTE_643)

    print("=" * 78)
    print("GUARDAS DEL AVISO, CORRIDAS HOY")
    print("=" * 78)
    print("puestos de la propuesta      :", puestos_prop)
    print("puestos del lote _lote_v36   :", puestos_lote)
    print("puestos del carril del 643    :", puestos_643)

    if sorted(puestos_prop) != sorted(puestos_lote):
        print("ABORTA guarda 1: la propuesta y el lote no son el mismo conjunto")
        return 1
    print("guarda 1 OK: la propuesta y el lote son el MISMO conjunto de cinco")

    if 643 in puestos_prop:
        print("ABORTA guarda 2: el 643 esta dentro de la propuesta")
        return 1
    if puestos_643 != [643]:
        print("ABORTA guarda 2: el carril del 643 no trae exactamente el 643")
        return 1
    print("guarda 2 OK: el 643 NO esta en la propuesta y su carril trae solo al 643")

    todos = puestos_prop + puestos_643
    clases = clases_de_hoy(todos)
    print("clases medidas HOY en el archivo de veredictos:")
    for p in sorted(todos):
        print("   puesto %5d  clase %s" % (p, clases.get(p, "AUSENTE")))
    if any(clases.get(p) != "D" for p in todos):
        print("ABORTA guarda 3: algun puesto no esta HOY en D")
        return 1
    print("guarda 3 OK: los seis estan HOY en clase D")

    if CAMPO in prop:
        print("ABORTA: el campo %s ya existe; este instrumento no pisa avisos" % CAMPO)
        return 1

    # El aviso se escribe DESPUES de estado y ANTES de filas, para que se lea
    # pegado al sello que matiza sin desordenar las filas selladas.
    nuevo = {}
    for clave, valor in prop.items():
        nuevo[clave] = valor
        if clave == "estado":
            nuevo[CAMPO] = TEXTO

    with open(PROP, "w", encoding="utf-8") as fh:
        json.dump(nuevo, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    with open(PROP, encoding="utf-8") as fh:
        rele = json.load(fh)

    print()
    print("=" * 78)
    print("GUARDA 4, EL SELLO INTACTO, MEDIDA TRAS ESCRIBIR")
    print("=" * 78)
    estado_despues = rele.get("estado")
    filas_despues = json.dumps(rele.get("filas"), ensure_ascii=False, sort_keys=True)
    print("estado IDENTICO :", estado_despues == estado_antes)
    print("estado, literal :", estado_despues)
    print("filas IDENTICAS :", filas_despues == filas_antes)
    print("filas, caracteres antes/despues: %d / %d" % (len(filas_antes), len(filas_despues)))
    print("claves del fichero, en orden:", list(rele.keys()))
    print("campo %s presente: %s" % (CAMPO, CAMPO in rele))
    if estado_despues != estado_antes or filas_despues != filas_antes:
        print("ABORTA guarda 4: el sello se movio")
        return 1
    print("guarda 4 OK: sello y filas intactos, solo se anadio el aviso fechado")
    print()
    print("AVISO ESCRITO.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
