# -*- coding: utf-8 -*-
"""vuelta90_tarea4_direccion_ope06.py . VUELTA 90, TAREA 4, PRIMERA MITAD: LA
DIRECCION DE CADA PAR DE LA BOLSA V90, LEIDA DE SU PROPIA RAZON.

POR QUE HACE FALTA. docs/plan/OP_E_06_REBASE_V90.jsonl (117 filas) trae
`nodo_a` y `nodo_b` EN EL ORDEN DEL VEREDICTO ORIGINAL (docs/INTRA_DOMINIO_
VEREDICTOS.jsonl: `barrido_razones_d.py` los copia tal cual del par que se
comparo en el cribado), que NO dice quien es la madre y quien el hijo. La
propia `verificacion` de `OP-E-06` lo exige por escrito: "LA DIRECCION DE
CADA ARISTA SALE DE SU PROPIA RAZON, no se decide de nuevo". Este instrumento
es esa lectura, hecha sobre el campo `razon` COMPLETO de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (no sobre el `frase` de la cosecha, que
esta truncado a 200 caracteres y en varias filas corta justo el nombre del
nodo que hace falta leer, TAREA 3.a de esta misma vuelta).

LA REGLA DE LECTURA, la misma que las adjudicaciones 4.1 y 2.1 del acta 89 ya
aplicaron sobre el 530: el nodo que la razon describe DESPACHANDO,
DICIENDO, NOMBRANDO, ENUMERANDO, ORDENANDO, DEFINIENDO, PREGUNTANDO o
NEGOCIANDO algo "EN UNA LINEA" (o "EN DOS LINEAS") es LA MADRE; el otro, el
que la razon describe con "trae el procedimiento (de esa linea)", "trae
completo", "desarrolla el paso/su paso" o "RECORRE EL CAMINO", es EL HIJO. La
arista se escribe MADRE -> HIJO (nodos_siguientes de la madre, nodos_previos
del hijo), que es la misma escalera que toda esta fase usa.

CLASIFICACION AUTOMATICA, Y DONDE NO ALCANZA. Sobre las 117 filas, la
deteccion por expresion regular (buscar el verbo de "una linea" pegado al
nombre de un id, y "trae el procedimiento" pegado al del otro) resuelve 108
sin ambiguedad. SEIS quedan en `DIRECCION_MANUAL` porque el patron de la
razon no cae en la forma exacta que la regex espera (dos aristas con la
madre en segunda mencion, un "el paso 2 DE LA MADRE" que nombra el rol en
vez del id, y una madre nombrada sin el verbo pegado a su primera mencion):
cada una lleva su cita literal de la razon completa en el comentario, para
que se pueda auditar sin volver a abrir el fichero.

LOS TRES EXCLUIDOS, y por que NO son de esta operacion: 2082, 2084 y 2112
tienen su razon citando LITERALMENTE "banco 9.22" con la formula "CONTINUA
en los dos sentidos": es la doctrina del ENLACE MUTUO (docs/plan/
04_ENLACES.md, seccion "LAS CINCO C"), NO la escalera de madre a hijo que
`OP-E-06` exige ("UNA SOLA DIRECCION por arista"). Forzar una sola direccion
sobre un par que su propia razon declara mutuo seria leer solo la mitad de
la evidencia. QUEDAN FUERA de la bolsa V90 escrita esta vuelta, y van a
`PENDIENTES` como candidatos de una operacion de ENLACE MUTUO (dos aristas),
no de `OP-E-06`.

CIFRA ESPERADA: 117 (bolsa V90) = 114 (con direccion, a escribir) + 3
(excluidos por banco 9.22). Verificado en tiempo de ejecucion: ROJO si no
cuadra, o si alguna fila queda sin clasificar.

SALIDA: docs/plan/OP_E_06_DIRECCION_V90.jsonl (114 filas: puesto, madre,
hijo). NO ESCRIBE NINGUNA ARISTA EN dataset/: eso es la segunda mitad de la
TAREA 4 (scripts/loop/vuelta90_tarea4_escribir_ope06.py).

USO:
  python scripts/loop/vuelta90_tarea4_direccion_ope06.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
BOLSA = os.path.join(PLAN, "OP_E_06_REBASE_V90.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
SALIDA = os.path.join(PLAN, "OP_E_06_DIRECCION_V90.jsonl")

MARCA_MADRE = re.compile(r"\b(dice|despacha|nombra|enumera|ordena|define|pregunta|negocia|mapea|cuenta)\b", re.IGNORECASE)
MARCA_LINEA = re.compile(r"\bEN\s+(UNA|DOS)\s+LINEA", re.IGNORECASE)
MARCA_HIJO = re.compile(
    r"trae\s+el\s+procedimiento|trae\s+su\s+propio\s+procedimiento|trae\s+completo|"
    r"RECORRE\s+EL\s+CAMINO|desarrolla\s+el\s+paso|desarrolla\s+su\s+paso|desarrollado",
    re.IGNORECASE)

# LOS TRES EXCLUIDOS: su razon cita "banco 9.22" con "CONTINUA en los dos
# sentidos" (enlace mutuo), no la escalera de una sola direccion que OP-E-06
# exige. Verificado en tiempo de ejecucion contra la razon real (mas abajo),
# no solo declarado aqui.
EXCLUIDOS_MUTUO_922 = {2082, 2084, 2112}

# LOS SEIS QUE LA REGEX NO RESUELVE, leidos a mano sobre la razon COMPLETA
# (cada cita es textual, del propio campo `razon` de INTRA_DOMINIO_VEREDICTOS.jsonl):
DIRECCION_MANUAL = {
    530: "A_MADRE",   # "...que la madre despacha en una linea" (la madre = estrategia_de_innovacion_de_producto,
                       # nodo_a; nodo_b "trae el PROCEDIMIENTO de seleccion de arenas")
    552: "B_MADRE",   # "JUZGADO POR EL TEXTO: el paso 2 DE LA MADRE es una linea...": la madre es
                       # preparacion_materiales_fundraising (nodo_b); executive_summary_inversion (nodo_a)
                       # "es el paso 2... desarrollado"
    1261: "A_MADRE",  # "customer_development_modelo dice en su paso 2, en UNA LINEA..."; "voz_del_cliente_voc
                       # trae el procedimiento de esa linea Y LE ANADE LA DIMENSION QUE FALTA"
    1787: "A_MADRE",  # "commuting_teletrabajo_sostenible dice en su paso 3, en UNA LINEA..."; "teletrabajo_
                       # sostenible trae el procedimiento de esa linea"
    2015: "B_MADRE",  # "nafta_free_trade_agreements RECORRE EL CAMINO...; y dice en UNA LINEA completar el
                       # certificado..."; "certificacion_origen_producto trae el procedimiento de esa linea"
    2023: "B_MADRE",  # "certificado_de_origen_tratados_libre_comercio RECORRE EL CAMINO...; y dice en UNA
                       # LINEA preparar y firmar el certificado..."; "certificacion_origen_producto trae el
                       # procedimiento de esa linea"
}


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def clasificar(nodo_a, nodo_b, razon):
    def segmento(nid):
        i = razon.find(nid)
        return razon[i:i + 240] if i != -1 else ""

    seg_a, seg_b = segmento(nodo_a), segmento(nodo_b)
    a_madre = bool(MARCA_MADRE.search(seg_a[:120])) and bool(MARCA_LINEA.search(seg_a))
    b_madre = bool(MARCA_MADRE.search(seg_b[:120])) and bool(MARCA_LINEA.search(seg_b))
    a_hijo = bool(MARCA_HIJO.search(seg_a[:120]))
    b_hijo = bool(MARCA_HIJO.search(seg_b[:120]))
    if a_madre and not b_madre:
        return "A_MADRE"
    if b_madre and not a_madre:
        return "B_MADRE"
    if a_hijo and not b_hijo:
        return "B_MADRE"
    if b_hijo and not a_hijo:
        return "A_MADRE"
    return None


def main():
    bolsa = cargar_jsonl(BOLSA)
    veredictos = {r["puesto_intra"]: r for r in cargar_jsonl(VEREDICTOS)}

    print("=" * 90)
    print("VUELTA 90, TAREA 4 (primera mitad): LA DIRECCION DE LOS %d PARES DE LA BOLSA V90" % len(bolsa))
    print("=" * 90)

    pares = []
    excluidos = []
    sin_clasificar = []

    for f in bolsa:
        p, a, b = f["puesto"], f["nodo_a"], f["nodo_b"]
        if p not in veredictos:
            sin_clasificar.append((p, a, b, "no esta en %s" % VEREDICTOS))
            continue
        razon = veredictos[p]["razon"]

        if p in EXCLUIDOS_MUTUO_922:
            if "9.22" not in razon:
                sin_clasificar.append((p, a, b, "declarado EXCLUIDO por banco 9.22 pero su razon "
                                                 "de HOY no cita '9.22': revisar la exclusion"))
                continue
            excluidos.append((p, a, b))
            continue

        veredicto = DIRECCION_MANUAL.get(p) or clasificar(a, b, razon)
        if veredicto is None:
            sin_clasificar.append((p, a, b, "la clasificacion automatica no pudo leer la direccion"))
            continue
        if "9.22" in razon:
            sin_clasificar.append((p, a, b, "su razon de HOY cita '9.22' y NO esta en "
                                             "EXCLUIDOS_MUTUO_922: revisar si es un cuarto enlace mutuo"))
            continue

        madre, hijo = (a, b) if veredicto == "A_MADRE" else (b, a)
        pares.append({"puesto": p, "madre": madre, "hijo": hijo})

    if sin_clasificar:
        print("ROJO: %d fila(s) sin clasificar. NO SE ESCRIBE NADA:" % len(sin_clasificar))
        for p, a, b, motivo in sin_clasificar:
            print("   puesto %s (%s -> %s): %s" % (p, a, b, motivo))
        return 1

    print("PARES CON DIRECCION LEIDA: %d" % len(pares))
    print("EXCLUIDOS POR ENLACE MUTUO (banco 9.22, van a PENDIENTES): %d" % len(excluidos))
    for p, a, b in excluidos:
        print("   puesto %s: %s <-> %s" % (p, a, b))
    print()

    if len(pares) + len(excluidos) != len(bolsa):
        print("ROJO: %d + %d != %d (la cuenta no cuadra contra la bolsa V90). NO SE ESCRIBE NADA."
              % (len(pares), len(excluidos), len(bolsa)))
        return 1
    if len(pares) != 114:
        print("ROJO: %d pares con direccion, se esperaban 114. NO SE ESCRIBE NADA." % len(pares))
        return 1

    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as fh:
        for pe in pares:
            fh.write(json.dumps(pe, ensure_ascii=False) + "\n")

    print("VERIFICADO: 114 + 3 == 117.")
    print("escrito: %s" % SALIDA)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
