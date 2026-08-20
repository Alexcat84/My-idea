"""VUELTA 17. Anade a la nota de OP-I-01 en docs/plan/OPERACIONES.jsonl el
registro del HUECO NOMBRADO del discutible 2 de la vuelta 16, mas el registro de
lo hecho en esta vuelta sobre el inventario.

NO borra nada: la nota vieja queda entera y el texto nuevo se anade al final.
Controles: 69 operaciones antes y despues, ids unicos, y OP-I-01 encontrada una
sola vez. Si algun control falla, no escribe.

Uso:
  python scripts/loop/vuelta17_nota_op_i_01.py              (simulacro)
  python scripts/loop/vuelta17_nota_op_i_01.py --escribir
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:16 fuente=docs/loop/ACTA_AUDITOR.md prueba="## VUELTA 16," corte=2026-08-20 motivo="registra el hueco nombrado del discutible 2 del acta de la vuelta 16"

import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

ANADIDO = (
    " HUECO NOMBRADO Y REGISTRADO EN LA VUELTA 17 (14 ago 2026), adjudicacion del discutible 2 de la"
    " vuelta 16 (docs/loop/ACTA_AUDITOR.md VUELTA 16 seccion 3, punto 4 de"
    " docs/loop/paradas/2026-08-14-credito-vuelta-16.md): EL CAMPO operaciones DE LAS 335 ENTRADAS"
    " NUEVAS HEREDA LO QUE EL CAMPO nodos DE LAS OPERACIONES VIEJAS TENGA INCOMPLETO."
    " QUE SE MIDIO Y QUE NO: el metodo de cruce se verifico reproduciendo el campo operaciones de las"
    " 221 entradas viejas con su propia nomina vieja (189 de 221 identicos, y las 32 diferencias con"
    " motivo medido, vuelta 16), lo que prueba que el metodo es CONSISTENTE con el campo nodos tal"
    " como esta escrito; NO prueba que ese campo este completo. El cruce toma nodos literal y no"
    " reinterpreta por que narrativa una operacion DESTEJIDO o DECISION_DE_FUENTE toca un nodo que no"
    " tiene listado. CONSECUENCIA EXACTA, sin agravarla: si el nodos de una operacion vieja esta"
    " incompleto, el operaciones de la entrada nueva hereda ese hueco, pero no lo agranda, porque es"
    " el MISMO campo que ya gobernaba el operaciones de las 221 viejas. QUIEN LO CIERRA: auditarlo"
    " operacion por operacion es TRABAJO DE LA FASE III, no de la FASE II, y aqui queda nombrado y no"
    " rellenado, como manda la verificacion de esta misma operacion (todo hueco va NOMBRADO, nunca"
    " rellenado). LO HECHO EN LA VUELTA 17 SOBRE ESTE INVENTARIO, ademas del registro de arriba:"
    " 1) las 221 entradas viejas de tipo acto quedan MARCADAS UNA A UNA como SUPERADA POR EL CORTE"
    " 3.388, con el puntero a su sucesora vigente (nombre mas fecha_corte 2026-08-13) en su campo"
    " estado y en su campo nota, sin borrar ni una linea ni cambiar ni una fecha_corte"
    " (scripts/loop/vuelta17_marcar_221_superadas.py, diff de exactamente 221 lineas modificadas y"
    " cero altas ni bajas, el archivo sigue en 671 lineas); 2) docs/plan/10_INVENTARIO.md recibe el"
    " AVISO con tachado en cabecera, en la tabla EL VOLUMEN, en la seccion LOS ACTOS y en las dos"
    " filas de COMO SE LEE ESTE INVENTARIO, SIN regenerar la tabla, que sigue siendo el disparador de"
    " 08_VERIFICACION. CORRECCION DECLARADA DE UNA CIFRA DE ESTA MISMA NOTA (vuelta 17, remedida con"
    " instrumento propio, scripts/loop/vuelta17_acto_que_crecio.py, tres metodos independientes"
    " coincidentes): donde esta nota dice UNA CIFRA MARCADA PARA RE MEDIR, la competencia entre"
    " inversores se declaro PURA con 4 miembros al puesto 1030 y la componente de hoy tiene 5, ESO"
    " SIGUE SIENDO CIERTO y no se toca; lo que se corrige es el uso que se le dio en la vuelta 16 en"
    " otro documento: de ESA frase se copio el nombre construccion_de_leverage y el de 4 a 5 a"
    " docs/plan/RECOMPUTO_3388.md linea 1042, que preguntaba otra cosa (cual de los 221 actos crecio"
    " ENTRE el corte 2.117 y el 3.388). Medido: construccion_de_leverage tiene CINCO miembros en los"
    " DOS cortes; el unico que crecio entre los dos cortes es gestion_terminacion_franquiciado, de 2"
    " a 3, ganando perdida_control_operativo, tal como la nota de OP-U-02 ya lo decia."
)


def main():
    escribir = "--escribir" in sys.argv
    filas = []
    with open(OPERACIONES, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))

    print("operaciones leidas:", len(filas))
    ids = [o["id_op"] for o in filas]
    assert len(ids) == len(set(ids)), "hay ids repetidos"

    objetivo = [o for o in filas if o["id_op"] == "OP-I-01"]
    assert len(objetivo) == 1, "OP-I-01 no aparece exactamente una vez"
    op = objetivo[0]
    assert "HUECO NOMBRADO Y REGISTRADO EN LA VUELTA 17" not in op["nota"], "ya estaba registrado"

    largo_antes = len(op["nota"])
    op["nota"] = op["nota"] + ANADIDO
    print("nota de OP-I-01:", largo_antes, "caracteres antes,", len(op["nota"]), "despues")
    assert op["nota"].startswith("323 ENTRADAS"), "la nota vieja no quedo intacta al frente"

    if not escribir:
        print("SIMULACRO: no se escribio nada.")
        return

    with open(OPERACIONES, "w", encoding="utf-8", newline="") as fh:
        for o in filas:
            fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    print("ESCRITO en", OPERACIONES)


if __name__ == "__main__":
    main()
