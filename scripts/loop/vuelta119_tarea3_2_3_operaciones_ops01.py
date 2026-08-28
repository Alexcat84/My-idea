# -*- coding: utf-8 -*-
"""vuelta119_tarea3_2_3_operaciones_ops01.py . VUELTA 119, TAREAS 3.2 y 3.3:
edita la fila de `OP-S-01` en `docs/plan/OPERACIONES.jsonl`, POR CORRECCION
DECLARADA (texto viejo intacto, la correccion se anade encima):

  3.2 El punto 4 de `verificacion` ("ningun nodo VIVO lleva NAFTA en su id ni
      en su titulo") SE ACOTA a la nomina de esta operacion (los dos nodos de
      la fusion), citando que el barrido global de NAFTA vive anotado en
      `PENDIENTES.md`, ficha `vigencia-del-marco-internacional` (decision del
      fundador, 28 ago 2026, punto 2). El punto NO se reescribe: se le
      concatena el acotamiento.

  3.3 `estado` pasa de `LISTA` a `HECHA` (misma figura que `OP-E-02`, cierre
      por declaracion: el acto material ya esta hecho, lo que falta es
      lectura y declaracion, no escritura de aristas) y `nota` gana un
      parrafo de CIERRE CON REMISION: el acto material de la fusion lo
      consumio la fase 03 en la vuelta 57 (commit `a1d7269d`, 20 ago 2026),
      y el punto 4 queda remitido a `PENDIENTES.md` por la decision del
      fundador.

Reescribe SOLO la fila de `OP-S-01`: lee el fichero linea por linea, localiza
la unica linea cuyo `id_op` es `OP-S-01`, la reemplaza, y escribe las demas
lineas byte a byte identicas (nunca se reformatea el fichero entero).

Uso: python scripts/loop/vuelta119_tarea3_2_3_operaciones_ops01.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

PUNTO4_VIEJO = "ningun nodo VIVO lleva NAFTA en su id ni en su titulo"
ACOTAMIENTO = (
    " | CORRECCION DECLARADA (28 ago 2026, decision del fundador en "
    "docs/loop/paradas/2026-08-28-titulo-nafta-ops01-DECISION.md, punto 2): "
    "este punto se ACOTA A LA NOMINA DE ESTA OPERACION (los dos nodos de la "
    "fusion, nafta_free_trade_agreements y "
    "certificado_de_origen_tratados_libre_comercio), no al barrido global de "
    "NAFTA sobre el resto del catalogo. Ese barrido (los otros cuatro nodos "
    "vivos que nombran NAFTA) vive anotado en PENDIENTES.md, ficha "
    "vigencia-del-marco-internacional, como trabajo post campaña."
)

NOTA_AGREGADA = (
    " CIERRE CON REMISION (28 ago 2026, decision del fundador, punto 3 de "
    "docs/loop/paradas/2026-08-28-titulo-nafta-ops01-DECISION.md): el acto "
    "material de esta fusion (deprecar nafta_free_trade_agreements con alias "
    "hacia el superviviente) lo consumio la fase 03 en la vuelta 57 (commit "
    "a1d7269d, 20 ago 2026, LOTE B DEL TRAMO 4). Con el titulo del "
    "superviviente corregido en la TAREA 3.1 de la vuelta 119 (titulo_concepto "
    "pasa a 'Certificado de Origen y Tratados de Libre Comercio (T-MEC/USMCA, "
    "Rules of Origin, RVC)', Gate 0 y las tres suites verdes despues, ciclo de "
    "tres corrido) y el punto 4 acotado y remitido a PENDIENTES.md, "
    "OP-S-01 SE DECLARA CUMPLIDA CON REMISION."
)


def main():
    with io.open(RUTA, encoding="utf-8", newline="") as fh:
        lineas = fh.readlines()

    encontrada = 0
    nuevas = []
    for linea in lineas:
        cruda = linea.rstrip("\r\n")
        cola = linea[len(cruda):]
        if not cruda.strip():
            nuevas.append(linea)
            continue
        obj = json.loads(cruda)
        if obj.get("id_op") != "OP-S-01":
            nuevas.append(linea)
            continue
        encontrada += 1

        verif = list(obj["verificacion"])
        idx = verif.index(PUNTO4_VIEJO)
        print("verificacion[%d] VIEJO: %r" % (idx, verif[idx]))
        verif[idx] = verif[idx] + ACOTAMIENTO
        obj["verificacion"] = verif

        estado_viejo = obj["estado"]
        obj["estado"] = "HECHA"
        fecha_vieja = obj["fecha_corte"]
        obj["fecha_corte"] = "2026-08-28"

        nota_vieja = obj["nota"]
        obj["nota"] = nota_vieja + NOTA_AGREGADA

        print("estado VIEJO -> NUEVO: %r -> %r" % (estado_viejo, obj["estado"]))
        print("fecha_corte VIEJA -> NUEVA: %r -> %r" % (fecha_vieja, obj["fecha_corte"]))
        print("verificacion[%d] NUEVO: %r" % (idx, verif[idx]))
        print("nota: %d caracteres viejos + %d caracteres agregados = %d"
              % (len(nota_vieja), len(NOTA_AGREGADA), len(obj["nota"])))

        nuevas.append(json.dumps(obj, ensure_ascii=False) + cola)

    if encontrada != 1:
        raise SystemExit("ROJO: se esperaba UNA fila OP-S-01 y se encontraron %d" % encontrada)

    with io.open(RUTA, "w", encoding="utf-8", newline="") as fh:
        fh.writelines(nuevas)

    print()
    print("ESCRITO: docs/plan/OPERACIONES.jsonl, SOLO la fila OP-S-01 reemplazada, "
          "el resto de las 70 lineas byte a byte identicas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
