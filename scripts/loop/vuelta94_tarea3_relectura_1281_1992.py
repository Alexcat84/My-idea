# -*- coding: utf-8 -*-
"""vuelta94_tarea3_relectura_1281_1992.py . VUELTA 94, TAREA 3: LAS DOS
RELECTURAS CONJUNTAS de la vuelta 93 (acta de la vuelta 93,
docs/loop/ACTA_AUDITOR.md secciones 5.1 y 5.2), sobre los puestos 1281 y
1992 de OP-E-07. Las dos entraron a DIRECCION_MANUAL en la vuelta 91 (nunca
pasaron por el guarda automatico, que solo corre sobre
extraer_direccion_automatica): scripts/loop/vuelta91_tarea4_direccion_ope07.py
lineas 103-129.

LA UNICA PREGUNTA QUE OP-E-07.verificacion MANDA: LA RAZON NOMBRA CUAL DE LOS
DOS NODOS ES LA MADRE, SI O NO. Se responde leyendo la razon COMPLETA de
docs/INTRA_DOMINIO_VEREDICTOS.jsonl, no el comentario de DIRECCION_MANUAL
(ese comentario es una interpretacion del ejecutor de la vuelta 91, no la
razon).

EL 1281 (get_visual -> pensamiento_visual_modelos_negocio). El unico "trae"
del segmento del hijo (desde su primera mencion) esta dentro de "ningun
habito general trae": medido abajo con un barrido propio, independiente del
de MARCA_HIJO. La razon nunca dice "paso N", "en UNA LINEA", "es un indice"
u otra formula que nombre a UN nodo como madre con contenido especifico que
el otro despliega: compara dos clases enteras ("el habito general contra su
aplicacion a un artefacto") y declara ELLA MISMA que el hijo trae contenido
(la narrativa) que "ningun habito general" tiene, lo que falla el test del
banco 9.6.2 ("el hijo cabe entero dentro de UN paso de la madre"). El unico
sosten del guarda automatico para este puesto es "es un habito"
(INVERIFICABLE, declarado en docs/PENDIENTES.md, vuelta 93), que describe
QUE ES get_visual, no que sea la madre de una linea especifica.
VEREDICTO: LA RAZON NO NOMBRA LA MADRE. SALE.

EL 1992 (metodos_pago_electronico_internacional -> seleccion_de_metodo_de_
pago via DIRECCION_MANUAL B_MADRE). Su razon dice "seleccion_de_metodo_de_
pago compara los cinco por seguridad, costo y competitividad, y cierra con
el contrato escrito y la consulta al banco": ninguna cita de paso ni de
linea. Sus dos hermanos de la misma madre y misma fuente (1991 y 1993) SI
traen la formula "dice en su paso 3, en UNA LINEA" (medido abajo, vara del
hermano). La direccion del 1992 no salio de la razon: salio del comentario
de DIRECCION_MANUAL de la vuelta 91 ("la comparacion general de los cinco
metodos es la madre, la infraestructura de uno de ellos, el hijo"), y
OP-E-07.verificacion exige leer LA RAZON, no un comentario.
VEREDICTO: LA RAZON NO NOMBRA LA MADRE. SALE.

USO:
  python scripts/loop/vuelta94_tarea3_relectura_1281_1992.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
ENTRADA = os.path.join(PLAN, "OP_E_07_DIRECCION_V93.jsonl")
SALIDA = os.path.join(PLAN, "OP_E_07_DIRECCION_V94.jsonl")

FORMULA_PASO_LINEA = re.compile(r"dice en su paso \d, en UNA LINEA", re.IGNORECASE)


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def medir_1281(razon):
    """Barrido propio del 'trae' dentro del segmento del hijo, independiente
    de MARCA_HIJO. Devuelve (total_trae_en_hijo, lista_de_contextos)."""
    idx = razon.find("pensamiento_visual_modelos_negocio")
    segmento_hijo = razon[idx:]
    apariciones = list(re.finditer(r"trae\b", segmento_hijo, re.IGNORECASE))
    contextos = [segmento_hijo[max(0, m.start() - 40):m.start() + 15] for m in apariciones]
    return len(apariciones), contextos


def medir_1992(razones):
    """Vara del hermano: 1991 y 1993 (misma madre, misma fuente) traen 'dice
    en su paso 3, en UNA LINEA'; 1992 no."""
    resultado = {}
    for p in (1991, 1992, 1993):
        m = FORMULA_PASO_LINEA.search(razones[p])
        resultado[p] = m.group(0) if m else None
    return resultado


def main():
    veredictos = {int(v["puesto_intra"]): v for v in cargar_jsonl(VEREDICTOS)}
    razon_1281 = veredictos[1281]["razon"]
    razon_1992 = veredictos[1992]["razon"]

    print("=" * 90)
    print("RELECTURA CONJUNTA, PUESTO 1281 (get_visual -> pensamiento_visual_modelos_negocio)")
    print("=" * 90)
    total, contextos = medir_1281(razon_1281)
    print("apariciones de 'trae' en el segmento del hijo: %d" % total)
    for c in contextos:
        print("  %r" % c)
    print("las %d estan dentro de 'ningun ... trae': %s" % (
        total, all("ningun" in c.lower() for c in contextos)))
    print("VEREDICTO: LA RAZON NO NOMBRA LA MADRE. SALE.")
    print()

    print("=" * 90)
    print("RELECTURA CONJUNTA, PUESTO 1992 (seleccion_de_metodo_de_pago <-> metodos_pago_electronico_internacional)")
    print("=" * 90)
    vara = medir_1992(veredictos and {k: v["razon"] for k, v in veredictos.items()})
    for p in (1991, 1992, 1993):
        print("  %d: %s" % (p, repr(vara[p]) if vara[p] else "NO trae la formula"))
    print("VEREDICTO: LA RAZON NO NOMBRA LA MADRE. SALE.")
    print()

    filas = cargar_jsonl(ENTRADA)
    print("=" * 90)
    print("FILTRADO de %s (%d filas): retira EXACTAMENTE {1281, 1992}" % (
        os.path.basename(ENTRADA), len(filas)))
    print("=" * 90)
    quedan = [f for f in filas if f["puesto"] not in (1281, 1992)]
    salieron = [f["puesto"] for f in filas if f["puesto"] in (1281, 1992)]
    print("salieron: %s" % sorted(salieron))
    if sorted(salieron) != [1281, 1992]:
        print("ROJO: no se encontraron EXACTAMENTE los dos puestos esperados en la entrada. NO SE ESCRIBE NADA.")
        return 1
    print("quedan: %d filas" % len(quedan))

    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as fh:
        for f in quedan:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")
    print("ESCRITO: %s (%d filas)" % (SALIDA, len(quedan)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
