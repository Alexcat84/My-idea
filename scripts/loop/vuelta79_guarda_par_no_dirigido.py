# -*- coding: utf-8 -*-
"""VUELTA 79, TAREA 4: LA GUARDA DEL PAR NO DIRIGIDO.

Adjudicada por cita, SIN DOCTRINA NUEVA (acta de la vuelta 78, seccion 4 y
seccion 5 punto 6; banco 9.6.2 "LA VARA TIENE DIRECCION"; AUDITOR.md seccion 3,
el criterio del forastero: la fuente propone, la lectura confirma).

EL HALLAZGO QUE LA MOTIVA (acta 78, seccion 4): la bolsa filtrada de la vuelta
78 (191 filas) traia el mismo par DOS VECES, una en cada direccion
(necesidades_reales_vs_declaradas -> descubrir_necesidades_del_cliente en la
fila 1, y la reciproca en la fila 46). El campo `arista` del calibrador NO
TIENE DIRECCION: al escribir la fila 1, la fila 46 quedo marcada resuelta sin
que nadie la mirara. Es la misma especie de fallo que el banco 9.6.2 nombra
para la vara aplicada al reves: "se aplico al reves tres veces y ninguna de
las tres se detecto al escribirla". Aqui el instrumento SI puso las dos
direcciones sobre la mesa; lo que faltaba era mirarlas juntas antes de leer
cualquiera de las dos.

LA GUARDA (sin doctrina nueva, solo obliga a mirar lo que el instrumento ya
decia):
  1. Antes de leer, la bolsa filtrada se agrupa por PAR NO DIRIGIDO
     (frozenset({madre, hijo})).
  2. Cuando el mismo par aparece en las dos direcciones, las DOS FILAS se
     leen JUNTAS y la direccion se decide con 9.6.2 explicitamente: las dos
     opciones se escriben en la razon, y la descartada se nombra.
  3. La fila hermana NO se cuenta como candidato aparte en la cifra de bolsa
     restante: las dos cuentan como UN candidato (una decision).
"""
from collections import defaultdict


def agrupar_por_par_no_dirigido(filas):
    """Agrupa FILAS (cada una con 'madre' e 'hijo') por par no dirigido.

    Devuelve (parejas, sueltas):
      - parejas: lista de listas de 2+ filas que comparten el mismo par no
        dirigido con AL MENOS dos direcciones distintas presentes (el caso
        que la guarda existe para atrapar).
      - sueltas: filas cuyo par no dirigido aparece en una sola direccion
        (el caso normal, que la guarda no debe romper).
    """
    por_clave = defaultdict(list)
    for fila in filas:
        clave = frozenset((fila["madre"], fila["hijo"]))
        por_clave[clave].append(fila)

    parejas, sueltas = [], []
    for clave, grupo in por_clave.items():
        direcciones = set((f["madre"], f["hijo"]) for f in grupo)
        if len(direcciones) >= 2:
            parejas.append(grupo)
        else:
            sueltas.extend(grupo)
    return parejas, sueltas


def candidatos_para_contar(filas):
    """Cuantos CANDIDATOS distintos quedan tras la guarda: cada pareja de
    direcciones cuenta como UNO (una decision), no como dos filas."""
    parejas, sueltas = agrupar_por_par_no_dirigido(filas)
    return len(parejas) + len(sueltas)


def _caso_positivo():
    """CASO POSITIVO OBLIGATORIO, con datos SINTETICOS que no tocan el grafo
    real: un par propuesto en las dos direcciones se agrupa y se publica
    junto; un candidato normal en una sola direccion no se rompe."""
    filas = [
        {"madre": "alfa", "hijo": "beta", "paso": 1, "_id": "F1"},
        {"madre": "beta", "hijo": "alfa", "paso": 3, "_id": "F2"},
        {"madre": "gamma", "hijo": "delta", "paso": 2, "_id": "F3"},
        {"madre": "epsilon", "hijo": "zeta", "paso": 1, "_id": "F4"},
        {"madre": "zeta", "hijo": "eta", "paso": 4, "_id": "F5"},
    ]
    parejas, sueltas = agrupar_por_par_no_dirigido(filas)

    print("=" * 78)
    print("CASO POSITIVO SINTETICO: LA GUARDA DEL PAR NO DIRIGIDO")
    print("=" * 78)
    print()
    print("Filas de entrada: %d" % len(filas))
    print()
    print("PAREJAS detectadas (mismo par, dos direcciones): %d" % len(parejas))
    for grupo in parejas:
        ids = [f["_id"] for f in grupo]
        print("  -> %s: %s" % (ids, [(f["madre"], "->", f["hijo"]) for f in grupo]))
    print()
    print("SUELTAS (una sola direccion, no tocadas por la guarda): %d" % len(sueltas))
    for f in sueltas:
        print("  -> %s: %s -> %s" % (f["_id"], f["madre"], f["hijo"]))
    print()

    ok = True
    # 1. alfa/beta (F1, F2) se agrupan como UNA pareja.
    if len(parejas) != 1 or sorted(f["_id"] for f in parejas[0]) != ["F1", "F2"]:
        print("FALLO: F1/F2 (alfa<->beta) no se agruparon como pareja")
        ok = False
    # 2. gamma->delta (F3) queda suelta: una sola direccion, un solo candidato.
    if not any(f["_id"] == "F3" for f in sueltas):
        print("FALLO: F3 (gamma->delta), candidato normal, no quedo suelta")
        ok = False
    # 3. epsilon->zeta (F4) y zeta->eta (F5) COMPARTEN el nodo zeta pero NO
    #    son el mismo par no dirigido (zeta participa dos veces, con
    #    companeros distintos): las dos deben quedar sueltas, sin falsos
    #    positivos por compartir un solo extremo.
    if not (any(f["_id"] == "F4" for f in sueltas) and any(f["_id"] == "F5" for f in sueltas)):
        print("FALLO: F4/F5 comparten un nodo (zeta) pero NO son el mismo par; no debian agruparse")
        ok = False
    # 4. El total de CANDIDATOS tras la guarda es 1 (pareja) + 3 (sueltas) = 4,
    #    no 5: la fila hermana no se cuenta aparte.
    total = candidatos_para_contar(filas)
    if total != 4:
        print("FALLO: candidatos_para_contar dio %d, se esperaba 4 (1 pareja + 3 sueltas)" % total)
        ok = False

    print("RESULTADO DEL CASO POSITIVO: %s" % ("OK, LA GUARDA FUNCIONA" if ok else "FALLO"))
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if _caso_positivo() else 1)
