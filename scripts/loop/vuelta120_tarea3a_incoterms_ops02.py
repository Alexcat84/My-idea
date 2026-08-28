# -*- coding: utf-8 -*-
"""vuelta120_tarea3a_incoterms_ops02.py . VUELTA 120, TAREA 3.a: escribe la
edicion "2020" en la cita de Incoterms del superviviente vivo de la nomina de
`OP-S-02`, remedida contra el grafo de hoy.

POR QUE LA NOMINA SE REMAPEA. La nomina original de `OP-S-02`
(`docs/plan/OPERACIONES.jsonl`) es del 11 ago 2026: tres nodos,
`incoterms_reglas_comerciales_internacionales`, `terminos_de_venta_incoterms`,
`seguro_de_carga_transporte`. Medido HOY contra `dataset/metadata/master_graph.json`
(campo `deprecado`), DOS de los tres estan deprecados:
  - `terminos_de_venta_incoterms` (deprecado=true) resuelve, via `ids_alias` de
    `incoterms_reglas_comerciales_internacionales`, A ESE MISMO superviviente:
    la cita de Incoterms SI viaja (el superviviente ya la lleva en su propio
    texto).
  - `seguro_de_carga_transporte` (deprecado=true) resuelve, via `ids_alias` de
    `seguro_exportacion`, A `seguro_exportacion`. La cita NO viaja completa: el
    nodo deprecado citaba "los terminos de venta (Incoterms)" en su paso 1, y
    el superviviente dice solo "terminos de venta", SIN la palabra "Incoterms".
    Anadir la version ahi seria RESTITUIR una palabra perdida en una fusion
    anterior, no anadir una version a una cita que ya existe: es una decision
    de contenido distinta, fuera del alcance literal de `OP-S-02`
    ("los tres nodos citan Incoterms con su version"). NO SE TOCA
    `seguro_exportacion` en esta vuelta: queda PENDIENTE DE DOCTRINA, trafdo a
    la mesa (ver nota de `OP-S-02` en `docs/plan/OPERACIONES.jsonl`).

LA VERSION. `docs/PENDIENTES.md`, ficha `vigencia-del-marco-internacional`,
texto fundacional: "Incoterms 2020 no es un dato local... un catalogo que lo
cite desactualizado miente con precision." Se cita "2020".

QUE ESCRIBE. Un solo campo, `resumen_teorico`, de un solo nodo vivo,
`incoterms_reglas_comerciales_internacionales` (que cubre tambien a
`terminos_de_venta_incoterms` por alias): la primera mencion de "Incoterms"
gana la version, "Los Incoterms son" -> "Los Incoterms 2020 son". CORRECCION
DECLARADA con guarda: si el texto vivo de hoy no es, byte a byte, el ANCLA
esperada, ROJO y no se escribe nada (mismo patron que
`vuelta119_tarea3_titulo_ops01.py`).

`dataset/metadata/master_graph.json` y su espejo de `web/` se recompilan
aparte, con el ciclo de tres, NUNCA por este script.

USO:
  python scripts/loop/vuelta120_tarea3a_incoterms_ops02.py --simular
  python scripts/loop/vuelta120_tarea3a_incoterms_ops02.py --mutacion-negativa
  python scripts/loop/vuelta120_tarea3a_incoterms_ops02.py
"""
import argparse
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
NID = "incoterms_reglas_comerciales_internacionales"

ANCLA_VIEJA = ("Los Incoterms son reglas estandarizadas que definen responsabilidades, "
               "costos y riesgos entre comprador y vendedor en una transacción de "
               "exportación.")
ANCLA_NUEVA = ("Los Incoterms 2020 son reglas estandarizadas que definen responsabilidades, "
               "costos y riesgos entre comprador y vendedor en una transacción de "
               "exportación.")


def leer_crudo(nid):
    with io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8", newline="") as fh:
        bruto = fh.read()
    cola = ""
    while bruto and bruto[-1] in "\r\n":
        cola = bruto[-1] + cola
        bruto = bruto[:-1]
    return json.loads(bruto), cola


def escribir(nid, datos, cola):
    with io.open(os.path.join(NODOS, nid + ".json"), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def calzar(resumen, ancla_vieja):
    """True si ANCLA_VIEJA (o la que se pase, para la mutacion negativa) esta
    literal al inicio de `resumen`."""
    return resumen.startswith(ancla_vieja)


def main():
    ap = argparse.ArgumentParser()
    modo = ap.add_mutually_exclusive_group()
    modo.add_argument("--simular", action="store_true",
                       help="solo imprime el antes/despues, no escribe")
    modo.add_argument("--mutacion-negativa", action="store_true",
                       help="caso rojo: usa un ancla deliberadamente distinta y comprueba "
                            "que el script NO escribe")
    a = ap.parse_args()

    datos, cola = leer_crudo(NID)
    resumen = datos.get("resumen_teorico", "")

    print("=" * 78)
    print("VUELTA 120, TAREA 3.a: VERSION DE INCOTERMS EN EL SUPERVIVIENTE DE OP-S-02")
    print("=" * 78)
    print("nodo: %s" % NID)

    if a.mutacion_negativa:
        ancla_falsa = ANCLA_VIEJA.replace("Incoterms", "INCOTERMS_QUE_NO_EXISTE")
        calza = calzar(resumen, ancla_falsa)
        print("MUTACION NEGATIVA: ancla deliberadamente distinta de la real.")
        print("calza (deberia ser False): %s" % calza)
        if calza:
            raise SystemExit("ROJO DE LA PRUEBA: la mutacion negativa deberia NO calzar y "
                              "calzo. La guarda no muerde.")
        print("VERDE DE LA PRUEBA: la mutacion negativa NO calza, como se espera; el caso "
              "real (mas abajo) NO se corrio con este ancla, asi que no se escribio nada.")
        return 0

    calza = calzar(resumen, ANCLA_VIEJA)
    print("resumen_teorico empieza con el ANCLA esperada: %s" % calza)
    if not calza:
        raise SystemExit("ROJO: el resumen_teorico vivo de hoy no empieza con el ANCLA "
                          "esperada. NO SE ESCRIBE nada: no se pisa un estado distinto al "
                          "medido en esta vuelta.")

    nuevo_resumen = ANCLA_NUEVA + resumen[len(ANCLA_VIEJA):]
    print()
    print("CORRECCION DECLARADA (vuelta 120, version de PENDIENTES.md ficha "
          "vigencia-del-marco-internacional, 'Incoterms 2020'):")
    print("  VIEJO -> %r" % ANCLA_VIEJA)
    print("  NUEVO -> %r" % ANCLA_NUEVA)

    if a.simular:
        print()
        print("SIMULACION: no se escribe nada (--simular).")
        return 0

    datos["resumen_teorico"] = nuevo_resumen
    escribir(NID, datos, cola)
    print()
    print("ESCRITO: dataset/nodos/%s.json, campo resumen_teorico, ningun otro campo tocado." % NID)
    print("Cubre tambien a terminos_de_venta_incoterms (deprecado, alias de este nodo): "
          "su cita de Incoterms ya resolvia aqui.")
    print("seguro_de_carga_transporte / seguro_exportacion: NO TOCADO, ver docstring "
          "(la cita no viajo completa a la fusion anterior; PENDIENTE DE DOCTRINA).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
