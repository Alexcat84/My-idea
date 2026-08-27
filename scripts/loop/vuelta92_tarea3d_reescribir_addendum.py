# -*- coding: utf-8 -*-
"""vuelta92_tarea3d_reescribir_addendum.py . VUELTA 92, TAREA 3(d): REESCRIBE
EL ADDENDUM DE EJECUCION DE OP-E-07 EN docs/plan/OPERACIONES.jsonl CON EL
CORTE NUEVO, SIN BORRAR EL TEXTO VIEJO (EJECUTOR.md regla 8).

Anade una frase al campo `nota` de OP-E-07 (no toca ni una palabra del texto
existente) y una entrada nueva al campo `evidencia`. Corre una sola vez;
si ya se aplico (idempotente por contenido), lo dice y no vuelve a escribir.

USO:
  python scripts/loop/vuelta92_tarea3d_reescribir_addendum.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

MARCA = "CORRECCION DECLARADA (vuelta 92"

NUEVA_FRASE_NOTA = (
    " CORRECCION DECLARADA (vuelta 92, TAREAS 2 a 4 de docs/loop/PROMPT_SIGUIENTE.md), "
    "SIN BORRAR EL TEXTO DE ARRIBA: la caida de clase de la vuelta 91 (acta de la vuelta 91, "
    "docs/loop/ACTA_AUDITOR.md, seccion 3.1, lineas 31290 a 31365; registrada tambien en "
    "docs/PENDIENTES.md) encontro que el puesto 1098 (customer_validation_sell_phase -> "
    "prueba_solucion_con_cliente) tenia una arista escrita que su propia razon PROHIBE "
    "(banco 9.6.2, docs/BANCO_DE_TEXTOS.md linea 1737 y siguientes: 'no era madre e hijo, "
    "linea compartida y procedimiento propio a cada lado', el mismo caso ya registrado en el "
    "puesto 2.195). Se construyo un guarda de dos condiciones para extraer_direccion_automatica "
    "(scripts/loop/vuelta92_tarea2_guarda_direccion.py: marca de madre positiva Y ausencia de "
    "negacion de jerarquia sin esa marca), probado contra las 88 razones de OP-E-07 (marca "
    "EXACTAMENTE el 1098) y contra las 114 de OP-E-06 (deja PASAR el 1160), y probado por "
    "mutacion. El guarda, corrido sobre OP_E_07_DIRECCION_V91.jsonl "
    "(scripts/loop/vuelta92_tarea3a_filtrar_ope07.py), saco EXACTAMENTE el 1098 y escribio "
    "docs/plan/OP_E_07_DIRECCION_V92.jsonl con 87 filas. La arista se retiro de dataset/nodos/ "
    "con scripts/loop/vuelta92_tarea3b_retirar_1098.py (las dos vistas; idempotencia probada: "
    "segunda corrida NO_ESTABA, 0 retiradas). El ciclo de tres se corrio entero: censo IGUAL "
    "(3.853 / 3.188 / 665), Gate 0 OK, motor 25/25, web 80/1030 mas 3 skipped, tsc limpio, y el "
    "diff de la union del grafo contra el cierre de la vuelta 91 "
    "(0691d2257ddbbf8b26357dbd25f5b304bc984611) dio EXACTAMENTE UNA borrada "
    "(customer_validation_sell_phase -> prueba_solucion_con_cliente) y CERO nuevas. LA CIFRA "
    "QUEDA: de los 88, UNO SALE por el banco 9.6.2 (puesto 1098, nombrado arriba), 85 ESCRITA, "
    "2 YA_ESTABA (1388 y 1946), 0 ESCALERA_ROTA. estado se queda en LISTA, mismo criterio que "
    "OP-E-01, OP-E-04 y OP-E-06: el estado de verdad es el repo y el commit, no un campo nuevo."
)

NUEVA_EVIDENCIA = (
    "docs/plan/OP_E_07_DIRECCION_V92.jsonl, 87 filas con direccion (el 1098 sale por el guarda "
    "de dos condiciones de scripts/loop/vuelta92_tarea2_guarda_direccion.py, corrido el 27 ago 2026)"
)


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [l for l in f]


def main():
    lineas = cargar_jsonl(RUTA)
    idx = None
    for i, l in enumerate(lineas):
        if l.strip() and json.loads(l).get("id_op") == "OP-E-07":
            idx = i
            break
    if idx is None:
        print("ROJO: no se encontro OP-E-07 en %s. NO SE ESCRIBE NADA." % RUTA)
        return 1

    d = json.loads(lineas[idx])
    if MARCA in d["nota"]:
        print("YA APLICADO: el addendum de la vuelta 92 ya esta en el campo nota. NO SE TOCA NADA.")
        return 0

    d["nota"] = d["nota"] + NUEVA_FRASE_NOTA
    d["evidencia"] = d["evidencia"] + [NUEVA_EVIDENCIA]

    lineas[idx] = json.dumps(d, ensure_ascii=False) + "\n"
    with io.open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.writelines(lineas)

    print("ESCRITO: %s, linea %d (OP-E-07), addendum de la vuelta 92 anadido a nota + evidencia." % (RUTA, idx + 1))
    print("EL TEXTO VIEJO NO SE TOCO: solo se anadio al final de nota, y una entrada nueva a evidencia.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
