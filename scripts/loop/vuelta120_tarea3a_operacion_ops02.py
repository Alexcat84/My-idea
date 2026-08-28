# -*- coding: utf-8 -*-
"""vuelta120_tarea3a_operacion_ops02.py . VUELTA 120, TAREA 3.a: cierra el
registro de `OP-S-02` en `docs/plan/OPERACIONES.jsonl` tras la escritura real
(`vuelta120_tarea3a_incoterms_ops02.py`), con la nomina remapeada al grafo de
hoy.

GUARDA: lee la fila de `OP-S-02` cruda, exige que el JSON de esa linea sea,
CAMPO A CAMPO, el esperado ANTES de tocarla (mismo patron de
`vuelta119_tarea3_2_3_operaciones_ops01.py`: no se pisa un estado distinto al
medido). Si algun campo no calza, ROJO y no se escribe nada. Solo esa UNA
linea de `OPERACIONES.jsonl` se toca; el resto del fichero, byte a byte.

USO:
  python scripts/loop/vuelta120_tarea3a_operacion_ops02.py --simular
  python scripts/loop/vuelta120_tarea3a_operacion_ops02.py --mutacion-negativa
  python scripts/loop/vuelta120_tarea3a_operacion_ops02.py
"""
import argparse
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
ID_OP = "OP-S-02"

VERIF_VIEJA = ["los tres nodos citan Incoterms con su version",
               "ningun nodo que solo lo apunte por arista se toca",
               "Gate 0 verde"]

VERIF_NUEVA = [
    "los tres nodos citan Incoterms con su version | CORRECCION DECLARADA "
    "(vuelta 120): la nomina de 11 ago 2026 remedida contra el grafo de hoy "
    "trae DOS de los tres deprecados (terminos_de_venta_incoterms y "
    "seguro_de_carga_transporte). terminos_de_venta_incoterms resuelve, por "
    "alias, al mismo superviviente que incoterms_reglas_comerciales_"
    "internacionales: LA VERSION SE ESCRIBIO AHI (resumen_teorico, 'Los "
    "Incoterms' a 'Los Incoterms 2020'), y cubre a los dos. "
    "seguro_de_carga_transporte resuelve a seguro_exportacion, PERO la cita "
    "de Incoterms de su paso 1 (\"los terminos de venta (Incoterms)\") NO "
    "viajo completa a la fusion anterior: el superviviente dice solo "
    "\"terminos de venta\", sin la palabra Incoterms. Anadir la version ahi "
    "restituiria una palabra perdida en una fusion anterior, que es una "
    "decision de contenido distinta al alcance literal de esta operacion "
    "(anadir version a una cita que YA existe). seguro_exportacion NO SE "
    "TOCA esta vuelta: PENDIENTE DE DOCTRINA, traido a la mesa.",
    "ningun nodo que solo lo apunte por arista se toca",
    "Gate 0 verde",
]

CAMPOS_ESPERADOS = {
    "estado": "LISTA",
    "fecha_corte": "2026-08-11",
    "verificacion": VERIF_VIEJA,
}

NOTA_AGREGADA = (" CIERRE VUELTA 120: version 'Incoterms 2020' escrita en "
                  "incoterms_reglas_comerciales_internacionales.resumen_teorico "
                  "(cubre por alias a terminos_de_venta_incoterms), Gate 0 y las "
                  "tres suites verdes despues "
                  "(scripts/loop/vuelta120_tarea3a_incoterms_ops02.py). "
                  "seguro_de_carga_transporte / seguro_exportacion queda sin "
                  "tocar: la cita no viajo completa a su fusion anterior, ver el "
                  "punto 1 de verificacion arriba.")


def leer_lineas():
    with io.open(RUTA, encoding="utf-8", newline="") as fh:
        return fh.readlines()


def hallar_fila(lineas):
    for i, linea in enumerate(lineas):
        s = linea.rstrip("\r\n")
        if not s.strip():
            continue
        d = json.loads(s)
        if d.get("id_op") == ID_OP:
            return i, d
    raise SystemExit("ROJO: no se encontro ninguna fila con id_op == %r" % ID_OP)


def calza_esperado(d, esperados):
    for campo, val in esperados.items():
        if d.get(campo) != val:
            return False, campo
    return True, None


def main():
    ap = argparse.ArgumentParser()
    modo = ap.add_mutually_exclusive_group()
    modo.add_argument("--simular", action="store_true")
    modo.add_argument("--mutacion-negativa", action="store_true")
    a = ap.parse_args()

    lineas = leer_lineas()
    idx, d = hallar_fila(lineas)

    print("=" * 78)
    print("VUELTA 120, TAREA 3.a: CIERRE DEL REGISTRO DE %s" % ID_OP)
    print("=" * 78)

    if a.mutacion_negativa:
        esperados_falsos = dict(CAMPOS_ESPERADOS)
        esperados_falsos["estado"] = "HECHA_QUE_NO_EXISTE_TODAVIA"
        ok, campo = calza_esperado(d, esperados_falsos)
        print("MUTACION NEGATIVA: esperado['estado'] cambiado a un valor que no calza.")
        print("calza (deberia ser False): %s (campo que rompe: %s)" % (ok, campo))
        if ok:
            raise SystemExit("ROJO DE LA PRUEBA: la mutacion negativa deberia NO calzar.")
        print("VERDE DE LA PRUEBA: la mutacion negativa NO calza; el caso real no se corrio "
              "con este esperado, nada se escribio.")
        return 0

    ok, campo = calza_esperado(d, CAMPOS_ESPERADOS)
    print("fila %s leida hoy calza con lo esperado: %s" % (ID_OP, ok))
    if not ok:
        raise SystemExit("ROJO: el campo %r de la fila %s de hoy no es el esperado. "
                          "NO SE ESCRIBE nada." % (campo, ID_OP))

    d["estado"] = "HECHA"
    d["fecha_corte"] = "2026-08-28"
    d["verificacion"] = VERIF_NUEVA
    d["nota"] = d["nota"] + NOTA_AGREGADA

    nueva_linea = json.dumps(d, ensure_ascii=False) + "\n"
    print()
    print("estado: LISTA -> HECHA")
    print("fecha_corte: 2026-08-11 -> 2026-08-28")
    print("verificacion[0]: correccion declarada (remapeo de nomina), texto viejo citado dentro")
    print("nota: %d caracteres agregados al final, texto viejo intacto" % len(NOTA_AGREGADA))

    if a.simular:
        print()
        print("SIMULACION: no se escribe nada (--simular).")
        return 0

    lineas[idx] = nueva_linea
    with io.open(RUTA, "w", encoding="utf-8", newline="") as fh:
        fh.writelines(lineas)
    print()
    print("ESCRITO: docs/plan/OPERACIONES.jsonl, unica fila de %s tocada." % ID_OP)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
