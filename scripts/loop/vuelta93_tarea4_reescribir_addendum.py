# -*- coding: utf-8 -*-
"""vuelta93_tarea4_reescribir_addendum.py . VUELTA 93, TAREA 4: REESCRIBE EL
CAMPO `nota` DE `OP-E-07` EN `docs/plan/OPERACIONES.jsonl`, ANADIENDO (SIN
BORRAR NADA DE LO QUE YA ESTABA) LA CORRECCION DE ESTA VUELTA: EL PUESTO 1009
SALE POR EL GUARDA REPARADO.

Identico en mecanica a `scripts/loop/vuelta92_tarea3d_reescribir_addendum.py`:
lee la linea de OP-E-07, concatena texto nuevo al final de `nota` (nunca
reemplaza ni una palabra de lo que ya habia) y reescribe SOLO esa linea del
fichero jsonl, preservando el resto byte a byte.

USO:
  python scripts/loop/vuelta93_tarea4_reescribir_addendum.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

TEXTO_NUEVO = (
    " CORRECCION DECLARADA (vuelta 93, TAREAS 2 a 4 de docs/loop/PROMPT_SIGUIENTE.md), "
    "SIN BORRAR EL TEXTO DE ARRIBA: el acta de la vuelta 92 (docs/loop/ACTA_AUDITOR.md, "
    "seccion 4, lineas 31977 a 32106) discrepo de su propia adjudicacion de la vuelta 91 "
    "sobre el puesto 1009 (customer_discovery_phase2_problem_test -> fit_problema_solucion) "
    "y la mando a relectura conjunta. La relectura (scripts/loop/vuelta93_tarea2_relectura_"
    "1009.py, docs/loop/SALIDA_V93_TAREA2_RELECTURA_1009.txt) concluyo que la razon del 1009 "
    "TAMPOCO nombra cual nodo es la madre: usa la formula de la clase D (\"trae un "
    "procedimiento que ESA FASE no tiene\", igual en forma a la del 1098, no \"la madre\" como "
    "el puesto 1083 que SI se confirmo), no nombra ninguna linea con su paso, y ella misma "
    "declara que \"el bloque de traccion queda fuera\" del solape, lo que hace fallar el test "
    "del banco 9.6.2 (BANCO_DE_TEXTOS.md lineas 1771 a 1774: el hijo cabe entero dentro de UN "
    "paso de la madre). Por OP-E-07.verificacion (\"si la razon tampoco lo dice, el par sale "
    "de la cosecha\"), EL PAR SALE, exactamente el mismo tratamiento que el 1098 en la vuelta "
    "92. El guarda de dos condiciones se reparo en las DOS direcciones "
    "(scripts/loop/vuelta93_tarea3_guarda_direccion.py): se anadieron las formulas que un "
    "TERCER CONJUNTO de 81 razones (los pares de COSECHA_RAZONES_D.jsonl con senales "
    "\"formula de la vara\" o \"procedimiento de esa linea\", menos los 202 puestos de las dos "
    "bolsas oficiales) probo que faltaban (\"termina/cierra/empieza CON o EN UNA LINEA\", "
    "puestos 995, 1007, 1024; \"el paso nombra, el hijo ejecuta\", puesto 995), y se retiro la "
    "alternativa \"prueba el problema\" (anadida en la vuelta 92 citando solo el puesto 1009), "
    "que era el UNICO sosten de que el 1009, el 1411 y el 1557 pasaran el guarda sin merecerlo: "
    "su formula es la de la clase D, no la de madre e hijo. El guarda reparado se probo contra "
    "TRES casos obligatorios (scripts/loop/vuelta93_tarea3_guarda_direccion.py --vara, EXIT 0): "
    "sobre las 88 de OP_E_07_REBASE_V91.jsonl saca EXACTAMENTE {1009, 1098}; sobre las 114 de "
    "OP_E_06_DIRECCION_V90.jsonl deja pasar el 1160 y no saca ningun otro (0 SALEN, OP-E-06 no "
    "se reabre); sobre el tercer conjunto de 81 (reconstruido por codigo propio, no copiado de "
    "ningun acta) los tres falsos SALE conocidos (995, 1007, 1024) PASAN y ningun otro sale. "
    "Probado por mutacion (docs/loop/SALIDA_V93_TAREA3_MUTACION.txt, EXIT 0, seis casos). El "
    "guarda ademas quedo CABLEADO POR DEFECTO dentro de extraer_direccion_automatica "
    "(scripts/loop/vuelta91_tarea4_direccion_ope07.py, TAREA 3.e): una llamada futura a esa "
    "funcion ya no puede saltarse el guarda sin querer (docs/loop/"
    "SALIDA_V93_TAREA3E_VERIFICACION_CABLEADO.txt). El guarda, corrido sobre "
    "OP_E_07_DIRECCION_V92.jsonl (scripts/loop/vuelta93_tarea3a_filtrar_1009.py), saco "
    "EXACTAMENTE el 1009 y escribio docs/plan/OP_E_07_DIRECCION_V93.jsonl con 86 filas. La "
    "arista se retiro de dataset/nodos/ con scripts/loop/vuelta93_tarea3b_retirar_1009.py (las "
    "dos vistas; idempotencia probada: segunda corrida NO_ESTABA, 0 retiradas, hash identico "
    "antes y despues). El ciclo de tres se corrio entero: censo IGUAL (3.853 / 3.188 / 665), "
    "Gate 0 OK, motor 25/25, web 80/1030 mas 3 skipped, tsc limpio, y el diff de la union del "
    "grafo contra el cierre de la vuelta 92 (85a250bee2495f4a23d89a4cf51338a5bcd8397e) dio "
    "EXACTAMENTE UNA borrada (customer_discovery_phase2_problem_test -> fit_problema_solucion) "
    "y CERO nuevas (docs/loop/SALIDA_V93_DIFF_UNION.txt). La via de OP-C-05 dio 935 entradas "
    "que sobran ANTES y 935 DESPUES: VERDE, la cuenta no crecio "
    "(docs/loop/SALIDA_V93_GUARDA_OPC05_DESPUES.txt). LA CIFRA QUEDA: de los 87 con direccion "
    "que dejo la vuelta 92, UNO SALE por el banco 9.6.2 (puesto 1009, nombrado arriba), 86 con "
    "direccion, 84 ESCRITA, 2 YA_ESTABA (1388 y 1946), 0 ESCALERA_ROTA. estado se queda en "
    "LISTA, mismo criterio que OP-E-01, OP-E-04 y OP-E-06: el estado de verdad es el repo y el "
    "commit, no un campo nuevo."
)


def main():
    lineas = io.open(OPERACIONES, encoding="utf-8").read().splitlines(keepends=True)
    idx_encontrado = None
    for i, linea in enumerate(lineas):
        if not linea.strip():
            continue
        d = json.loads(linea)
        if d.get("id_op") == "OP-E-07":
            idx_encontrado = i
            break

    if idx_encontrado is None:
        print("ROJO: no se encontro OP-E-07 en %s. NO SE ESCRIBE NADA." % OPERACIONES)
        return 1

    linea_original = lineas[idx_encontrado]
    d = json.loads(linea_original)
    nota_vieja = d.get("nota", "")
    if TEXTO_NUEVO.strip() in nota_vieja:
        print("YA APLICADO: la nota de OP-E-07 ya trae el texto de la vuelta 93. NO SE TOCA NADA.")
        return 0

    d["nota"] = nota_vieja + TEXTO_NUEVO
    nueva_linea = json.dumps(d, ensure_ascii=False) + "\n"
    lineas[idx_encontrado] = nueva_linea

    with io.open(OPERACIONES, "w", encoding="utf-8", newline="") as fh:
        fh.writelines(lineas)

    print("ESCRITO: %s, linea %d (OP-E-07), nota anadida sin borrar nada, %d caracteres nuevos"
          % (OPERACIONES, idx_encontrado + 1, len(TEXTO_NUEVO)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
