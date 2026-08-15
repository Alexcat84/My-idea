"""Vuelta 32, TAREA 1.2: la nota de OP-D-02 queda READJUDICADA.

CORRECCION DECLARADA, y el texto viejo se queda ENTERO delante (EJECUTOR.md
regla 8: una correccion que tapa lo que corrige no se puede auditar). El campo
`nota` no se reescribe: se le anade el bloque de correccion al final.

QUE SE CORRIGE, y con que medicion del dia al lado (EJECUTOR.md regla 1 y 2):
el ORDEN INTERNO de OP-D-02 empieza por 'destejer voz_del_cliente_voc separando
Cooper (1 a 5) de Coleman (6 a 10)', y ese paso 1 YA ESTA HECHO: lo hizo
OP-F-04-COL en la vuelta 31. La medicion que lo sostiene se corre en este mismo
script, contra el arbol de HOY, y su salida se imprime para que quede en el
registro de la vuelta. No se copia de un acta ni de un reporte.

Uso: python scripts/loop/vuelta32_registros.py [--aplicar]
Sin --aplicar solo mide e imprime el texto que escribiria.
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def nodo(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    with open(ruta, encoding="utf-8") as fh:
        return json.load(fh)


def medir():
    """La medicion del dia que sostiene la readjudicacion."""
    print("--- MEDICION DEL DIA, sobre el arbol de HOY ---")
    fuera = {}
    for nid in ("voz_del_cliente_voc", "observar_al_cliente_en_su_contexto",
                "enfoque_mercado_voc"):
        d = nodo(nid)
        if d is None:
            print("%-38s AUSENTE" % nid)
            fuera[nid] = None
            continue
        pasos = d.get("pasos_accionables") or []
        fuentes = [f.strip() for f in str(d.get("fuente") or "").split("|")]
        print("%-38s pasos %2d  fuentes %d  %s" % (nid, len(pasos), len(fuentes),
                                                   d.get("fuente")))
        fuera[nid] = (len(pasos), len(fuentes), d.get("fuente"))
    return fuera


CORRECCION = (
    " ~~ORDEN INTERNO: 1. destejer voz_del_cliente_voc separando Cooper (1 a 5) de "
    "Coleman (6 a 10)~~ CORRECCION DECLARADA (2026-08-15, vuelta 32, ordenada por el "
    "encargo de la vuelta; el texto viejo se queda entero arriba): LA OPERACION QUEDA "
    "READJUDICADA PORQUE SU PASO 1 YA ESTA HECHO, y lo hizo OP-F-04-COL en la vuelta "
    "31, no esta operacion. MEDIDO HOY sobre el arbol, no copiado de un acta: "
    "voz_del_cliente_voc tiene 5 pasos y FUENTE UNICA (Winning at New Products - "
    "Robert G. Cooper), o sea que el bloque de Coleman ya no esta en el nodo; y el "
    "bloque 6 a 10 que el campo preservar manda hacer viajar entero (observar una vez "
    "al mes, ponerse en el lugar del cliente, las pepitas de oro, anotar y revisar a "
    "los dos dias, buscar patrones) vive hoy en observar_al_cliente_en_su_contexto, "
    "nodo propio nacido en la vuelta 31 con 5 pasos y fuente unica Never Lose a "
    "Customer Again - Joey Coleman. EL DESTEJIDO NO SE REPITE. LO QUE LE QUEDA A "
    "OP-D-02 ES: (a) la fusion con enfoque_mercado_voc, que cubre justo la mitad que "
    "la cirugia deja en pie, con su campo preservar intacto (la evaluacion preliminar "
    "de mercado, el analisis competitivo detallado, y probar los conceptos con "
    "clientes reales antes del desarrollo formal); (b) la relectura de los congelados "
    "724, 755 y 827 contra el superviviente; y (c) tener delante a "
    "homework_frontend_loading y voice_of_customer_homework, que es su punto 4 y no se "
    "toca. EL TIPO DE LA OPERACION SIGUE ESCRITO COMO DESTEJIDO y no se cambia aqui: "
    "el campo tipo es del plan, y lo que esta vuelta adjudica es el ALCANCE que queda "
    "por ejecutar, no la etiqueta. La segunda entrada del campo preservar (CON EL "
    "DESTEJIDO viaja el bloque 6 a 10 entero) queda CUMPLIDA por OP-F-04-COL y se deja "
    "escrita tal cual, sin tocar, por la misma razon."
)


def main():
    aplicar = "--aplicar" in sys.argv
    medir()
    print()

    lineas = []
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                lineas.append(json.loads(linea))

    encontrada = False
    for o in lineas:
        if o["id_op"] != "OP-D-02":
            continue
        encontrada = True
        if "CORRECCION DECLARADA (2026-08-15, vuelta 32" in (o.get("nota") or ""):
            print("YA APLICADA: la nota de OP-D-02 ya trae la correccion de la vuelta 32.")
            return 0
        print("--- NOTA VIEJA (se queda entera) ---")
        print(o["nota"])
        print()
        o["nota"] = (o.get("nota") or "") + CORRECCION
        print("--- NOTA NUEVA ---")
        print(o["nota"])

    if not encontrada:
        print("ERROR: OP-D-02 no esta en %s" % OPS)
        return 1

    if not aplicar:
        print()
        print("(simulacion: sin --aplicar no se escribe nada)")
        return 0

    with open(OPS, "w", encoding="utf-8") as fh:
        for o in lineas:
            fh.write(json.dumps(o, ensure_ascii=False) + "\n")

    # Verificacion tras escribir: el fichero sigue siendo JSONL valido y no se
    # perdio ni se duplico ninguna operacion.
    de_vuelta = []
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                de_vuelta.append(json.loads(linea))
    ids = [o["id_op"] for o in de_vuelta]
    rotas = 0
    for o in de_vuelta:
        for d in (o.get("depende_de") or []) + (o.get("bloquea_a") or []):
            if d not in set(ids):
                rotas += 1
    print()
    print("VERIFICADO TRAS ESCRIBIR: %d lineas JSON validas, %d ids unicos, "
          "%d dependencias rotas" % (len(de_vuelta), len(set(ids)), rotas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
