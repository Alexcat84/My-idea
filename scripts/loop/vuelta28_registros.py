"""Vuelta 28, TAREA 1: los registros.

Hornea la entrada de la familia HUGOS-SISTEMAS en docs/plan/INVENTARIO.jsonl
(tipo familia_de_ids), adjudicacion 7 del acta de la vuelta 27.

NADA se copia de un acta ni de un reporte: la nomina se MIDE contra el grafo en
esta corrida (EJECUTOR.md regla 2), y si un id no esta vivo o su fuente no es la
esperada, el script PARA y no escribe.

Uso:
    python scripts/loop/vuelta28_registros.py --simular
    python scripts/loop/vuelta28_registros.py --ejecutar
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
INV = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")

# Los nueve de la nomina, tal como el encargo los nombra: los ocho de la salida
# de sistemas mas tecnologia_como_medio_no_fin.
NOMINA = [
    "arquitectura_flexible_soa",
    "complejidad_acorde_capacidad_organizacional",
    "definicion_objetivos_proyecto_sistema",
    "diseno_conceptual_sistema",
    "ejecucion_incremental_transicion_tecnologica",
    "guias_diseno_sistemas_estrategicos",
    "rediseno_tras_fracaso_proyecto",
    "requisitos_sistema_retroalimentacion",
    "tecnologia_como_medio_no_fin",
]
FUENTE_ESPERADA = "Essentials of Supply Chain Management - Michael H. Hugos"


def leer_nodo(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    with open(ruta, encoding="utf-8") as fh:
        return json.load(fh)


def vivo(d):
    return not d.get("deprecado") and not d.get("deprecated")


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("--simular", "--ejecutar"):
        print(__doc__)
        return 2
    ejecutar = sys.argv[1] == "--ejecutar"

    print("=" * 78)
    print("NOMINA DE HUGOS-SISTEMAS, MEDIDA CONTRA EL GRAFO EN ESTA CORRIDA")
    print("=" * 78)
    fallos = 0
    for nid in NOMINA:
        d = leer_nodo(nid)
        if d is None:
            print("  AUSENTE DEL GRAFO: %s" % nid)
            fallos += 1
            continue
        f = (d.get("fuente") or "").strip()
        ok_vivo = vivo(d)
        ok_fuente = f == FUENTE_ESPERADA
        if not ok_vivo or not ok_fuente:
            fallos += 1
        print("  %-46s vivo=%-5s pasos=%2d fuente_unica_hugos=%s"
              % (nid, ok_vivo, len(d.get("pasos_accionables") or []), ok_fuente))
        if not ok_fuente:
            print("      fuente medida: %r" % f)

    # Contraste: la familia Hugos entera al dia de hoy.
    vivos_hugos = 0
    unica_hugos = 0
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        with open(os.path.join(NODOS, nombre), encoding="utf-8") as fh:
            d = json.load(fh)
        if "hugos" in (d.get("fuente") or "").lower() and vivo(d):
            vivos_hugos += 1
            if len(str(d.get("fuente")).split("|")) == 1:
                unica_hugos += 1
    print()
    print("  contraste medido hoy: %d nodos vivos declaran a Hugos, %d con fuente UNICA"
          % (vivos_hugos, unica_hugos))
    print("  la nomina de HUGOS-SISTEMAS es %d de esos %d" % (len(NOMINA), unica_hugos))

    if fallos:
        print()
        print("PARA: %d fallo(s) de nomina. No se escribe nada." % fallos)
        return 1

    ya = 0
    with open(INV, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip() and json.loads(linea).get("nombre") == "HUGOS-SISTEMAS":
                ya += 1
    if ya:
        print()
        print("PARA: la entrada HUGOS-SISTEMAS ya existe en el inventario (%d)." % ya)
        return 1

    entrada = {
        "tipo": "familia_de_ids",
        "nombre": "HUGOS-SISTEMAS",
        "miembros": NOMINA,
        "forma": (
            "familia de destino nombrada por el fundador, no familia de ids gemelos: "
            "nodos VIVOS de fuente UNICA Hugos cuyo objeto es la parte de SISTEMAS del "
            "libro (como se disena, se justifica y se construye un sistema), no el flujo "
            "de cadena de suministro"
        ),
        "cobertura": "9 ids, los 9 medidos vivos y con fuente unica Hugos en esta corrida",
        "estado": "VIVA: es el destino escrito de los siete de la tercera clase de OP-F-03",
        "operaciones": ["OP-F-03"],
        "fecha_corte": "2026-08-14",
        "nota": (
            "HORNEADA por la adjudicacion 7 del acta de la vuelta 27 del auditor "
            "(docs/loop/ACTA_AUDITOR.md, seccion 4, punto 7), que la concede POR EXTENSION "
            "CITADA. La familia la nombra el fundador en su correccion del 14 ago 2026, "
            "escrita en el campo nota de OP-F-03 de docs/plan/OPERACIONES.jsonl con estas "
            "palabras: 'su bloque va a la familia HUGOS-SISTEMAS'. El destino DENTRO de la "
            "familia lo decide P.18 (docs/plan/BANCO_DEL_PLAN.md), que nombra a esta familia "
            "en su alcance del mismo dia. "
            "LA LECTURA QUE LOS JUNTA, medida hoy sobre titulo, entregable y resumen de los "
            "nueve: los nueve son el mismo capitulo de Hugos, el de COMO SE CONSTRUYE UN "
            "SISTEMA. Cuatro dicen el ciclo entero de diseno (diseno_conceptual_sistema "
            "esboza, guias_diseno_sistemas_estrategicos compara disenos con siete criterios, "
            "definicion_objetivos_proyecto_sistema parte el diseno en componentes cohesivos, "
            "complejidad_acorde_capacidad_organizacional mide el alcance contra la capacidad "
            "real). Tres dicen COMO SE EJECUTA (ejecucion_incremental_transicion_tecnologica "
            "por pasos incrementales, rediseno_tras_fracaso_proyecto cambia el enfoque tras "
            "fallar, arquitectura_flexible_soa reutiliza lo que ya existe antes de construir). "
            "Dos dicen PARA QUE (tecnologia_como_medio_no_fin exige conectar cada inversion "
            "con una mejora de servicio o de costo, requisitos_sistema_retroalimentacion pone "
            "las tres condiciones del sistema que se autoajusta). Es el material que la "
            "vuelta 26 llamo tercera clase: piensa en grande, empieza pequeno, entrega rapido, "
            "hitos de 30, 60 y 90 dias, time boxes, reutilizar lo existente, y justificar la "
            "inversion contando beneficios directos, incrementales, de evitacion e intangibles. "
            "NOTA DE ALCANCE, dicha para que nadie la lea de mas: los nueve son la nomina "
            "LEIDA de la familia, no un barrido exhaustivo del capitulo sobre los 107 nodos "
            "de fuente unica Hugos medidos hoy. Es la nomina contra la que se ejecuto el "
            "reparto de OP-F-03, y si la familia crece, P.18 manda releerla al dia de la "
            "operacion que la use."
        ),
    }
    linea = json.dumps(entrada, ensure_ascii=False)
    print()
    print("ENTRADA A HORNEAR:")
    print(linea)

    if not ejecutar:
        print()
        print("SIMULACION: no se escribio nada.")
        return 0

    with open(INV, "r", encoding="utf-8", newline="") as fh:
        crudo = fh.read()
    cola = "" if crudo.endswith("\n") else "\n"
    with open(INV, "a", encoding="utf-8", newline="") as fh:
        fh.write(cola + linea + "\n")
    print()
    print("ESCRITO en docs/plan/INVENTARIO.jsonl")
    return 0


if __name__ == "__main__":
    sys.exit(main())
