# -*- coding: utf-8 -*-
"""cuenta_agregada_de_perdidas.py . LA CUENTA AGREGADA DE LAS PERDIDAS DE UN PLAN
SELLADO, HECHA POR MAQUINA Y CON TODA EXCLUSION DICHA.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA NI DE LOTE, por la vara del acta 58
(pregunta 4): el plan entra por --plan. Este fichero no se clona cada vuelta.

POR QUE NACE (26 ago 2026, vuelta 70). LA REGLA ES DEL ACTA 68 Y SALIO DE UNA
CAIDA: toda cuenta agregada que se publique sobre una tabla (cuantas filas
cumplen X) se deriva CONTANDO POR MAQUINA en la corrida de esa vuelta, no de
memoria del reparto; y si se excluyen filas porque otro discutible las cubre, la
frase lo DICE. La vuelta 69 la estreno con una sonda escrita dentro de la vuelta
que NO quedo en el arbol: buscada hoy con grep sobre scripts/, la cabecera CUENTA
AGREGADA DE LAS PERDIDAS no aparece en ningun instrumento, solo su salida. Una
regla cuyo instrumento no queda en el arbol depende de que la siguiente vuelta se
acuerde de re-escribirlo, que es justo lo que la regla venia a evitar.

QUE CUENTA, Y COMO. Lee el campo perdidas de cada acto del plan sellado (contrato
CAMPO PROPIO v1) y cuenta: el total, el reparto por ESPECIE, las filas que llevan
la frase sellada ATENUANTE DECLARADO, las que ademas son de la ESPECIE DEL
PENDIENTE 4, las que llevan ATENUANTE DECLARADO Y MEDIDO, y las que declaran DOS
SEDES en su campo donde. Cada cuenta se imprime CON LA NOMINA DE LAS FILAS que la
componen, para que la cifra se pueda recontar a mano contra el plan.

LAS DOS COSAS QUE MIDE Y QUE UNA LECTURA DE MEMORIA SE SALTA:
  1. LA FRASE SELLADA, NO EL MECANISMO. Una fila que DESCRIBE un atenuante en su
     prosa pero NO lleva la frase ATENUANTE DECLARADO no se cuenta, y el
     instrumento la nombra aparte bajo FILAS QUE DESCRIBEN UN ATENUANTE SIN LA
     FRASE SELLADA. Esa es la exclusion DICHA que la regla pide, y es exactamente
     el caso que la vuelta 69 tuvo con su fila 5.
  2. LA LECTURA CONTRARIA. La fila es POR PIEZA que se pierde y no por sitio
     donde vivia (acta 67, D10), asi que una fila con dos sedes cuenta UNA vez.
     El instrumento publica ademas cuanto daria la lectura contraria, para que el
     lector pueda restar en vez de tener que recontar.

CORRECCION DECLARADA (2026-08-26, vuelta 73, TAREA 1 del encargo; adjudicacion 1
del acta 72, seccion 5.1, nacida de la pregunta 2 y del D8 del reporte de la
vuelta 72). EL TEXTO VIEJO NO SE TACHA Y SE QUEDA ENTERO ARRIBA, y aqui va
citado VERBATIM para que la correccion se pueda auditar sin abrir el historial:

  "la frase sellada ATENUANTE DECLARADO, las que ademas son de la ESPECIE DEL
  PENDIENTE 4, las que llevan ATENUANTE DECLARADO Y MEDIDO"

Eso es lo que este instrumento CUENTA, y sigue siendo exacto. Lo que faltaba no
era una cuenta sino UNA DEFINICION: el nombre historico de la marca (ya lo dice
el APPEND de un hermano) nombra un VEHICULO, y quien leia la celda sin la
definicion delante podia entender que una pieza que llega por INCISO no es de
esta especie. La vuelta 72 pago ese hueco: la fila del acto 43 de su lote H
cumplia el hecho y llegaba por INCISO, y la celda salio en 0 con glosa.

LA ESPECIE DEL PENDIENTE 4 LA DEFINE EL HECHO, NO EL VEHICULO. Una fila es de
esta especie cuando LA SUSTANCIA QUE SE PIERDE LLEGA ENTERA DESDE OTRO ABSORBIDO
DEL MISMO ACTO, sea el vehiculo un APPEND o un INCISO. El motivo esta escrito en
la adjudicacion: la marca existe porque una perdida cuya sustancia llega entera
es mas barata que una perdida seca, y ese hecho no depende del vehiculo. El
nombre historico nacio cuando el APPEND era el unico vehiculo que la producia;
el INCISO nacio despues. EN ADELANTE la frase sellada ESPECIE DEL PENDIENTE 4 se
escribe en la fila cuando el HECHO se cumpla, por cualquiera de los dos.

LO QUE ESTA CORRECCION NO TOCA, Y SE DICE PARA QUE SE PUEDA MEDIR: la BUSQUEDA y
la ARITMETICA se quedan como estaban, byte a byte. FRASE_PENDIENTE4 sigue siendo
la misma cadena, la nomina sigue buscandola dentro del campo que, y la lectura
contraria sigue sumando igual. Tampoco se toca la tupla PISTAS_SIN_SELLO, que
conserva su pista "llega por el APPEND" con el nombre del vehiculo dentro: esa tupla NO define la
especie, solo delata prosa de atenuante sin sello, y estrecharla o ensancharla
seria mover la busqueda. ESTA CORRECCION ES DE GLOSA: cambia lo que el lector
entiende, no lo que la maquina cuenta.

DE SOLO LECTURA. No escribe nada.

Uso:
  python scripts/loop/cuenta_agregada_de_perdidas.py --plan docs/loop/PLAN_V70_OPU02_LOTE_F.json
"""
import argparse
import io
import json
import os
import re
import sys
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

FRASE_ATENUANTE = "ATENUANTE DECLARADO"
FRASE_MEDIDO = "ATENUANTE DECLARADO Y MEDIDO"
FRASE_PENDIENTE4 = "ESPECIE DEL PENDIENTE 4"
# Palabras que delatan un atenuante DESCRITO en la prosa sin la frase sellada.
# No cuentan para la cifra: sirven para NOMBRAR la exclusion.
PISTAS_SIN_SELLO = ("llega entera por", "llega entero por", "no se pierde entero",
                    "asi que el sitio donde", "llega por el APPEND", "llega VERBATIM")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    plan = json.load(io.open(os.path.join(RAIZ, a.plan.replace("/", os.sep)), encoding="utf-8"))

    filas = []
    for acto in plan["actos"]:
        for p in acto.get("perdidas") or []:
            filas.append((acto["orden"], p))

    print("=" * 78)
    print("CUENTA AGREGADA DE LAS PERDIDAS DEL PLAN, POR MAQUINA")
    print("  plan: %s" % a.plan)
    print("  la regla es del acta 68: la cuenta se cuenta, no se recuerda, y toda")
    print("  exclusion va DICHA.")
    print("=" * 78)
    print()
    print("  perdidas selladas, en total        : %d" % len(filas))
    for esp, n in sorted(Counter(p["especie"] for _, p in filas).items()):
        print("     %-22s : %d" % (esp, n))

    def nomina(cond, titulo):
        sel = [(i, o, p) for i, (o, p) in enumerate(filas, 1) if cond(p)]
        print()
        print("  %-34s : %d" % (titulo, len(sel)))
        for i, o, p in sel:
            print("     fila %2d (acto %d)  %s" % (i, o, p["donde"]))
        return sel

    nomina(lambda p: FRASE_ATENUANTE in p["que"], "filas con ATENUANTE DECLARADO")
    nomina(lambda p: FRASE_PENDIENTE4 in p["que"], "de la ESPECIE DEL PENDIENTE 4")
    nomina(lambda p: FRASE_MEDIDO in p["que"], "con ATENUANTE DECLARADO Y MEDIDO")
    dos = nomina(lambda p: " y " in p["donde"] and re.search(r"\b(paso|condicion)\b.*\by\b.*\b(paso|condicion)\b", p["donde"]),
                 "filas con DOS SEDES en el campo donde")

    print()
    print("  LA EXCLUSION, DICHA: filas que describen un atenuante en su prosa y")
    print("  NO llevan la frase sellada (no cuentan para la cifra de arriba)")
    sin = [(i, o, p) for i, (o, p) in enumerate(filas, 1)
           if FRASE_ATENUANTE not in p["que"] and any(x in p["que"] for x in PISTAS_SIN_SELLO)]
    if not sin:
        print("     NINGUNA: toda fila que describe un atenuante lo lleva sellado.")
    for i, o, p in sin:
        print("     fila %2d (acto %d)  %s" % (i, o, p["donde"]))

    print()
    print("  LA LECTURA CONTRARIA (una fila por SITIO y no por PIEZA, que es lo que")
    print("  el D10 del acta 67 descarto): seria %d y no %d" % (len(filas) + len(dos), len(filas)))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
