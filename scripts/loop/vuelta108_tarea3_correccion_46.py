# -*- coding: utf-8 -*-
"""vuelta108_tarea3_correccion_46.py . TAREA 3 de la vuelta 108, el puesto 46
(docs/loop/PROMPT_SIGUIENTE.md, TAREA 3), remedio de la caida 1.1 del acta de
la vuelta 107.

DISCREPANCIA DECLARADA CONTRA EL ENCARGO (EJECUTOR.md, "el instrumento
manda"): el encargo dice "EL 46, POR LA MISMA VIA QUE YA USASTE CON EL 147",
pero medido hoy contra docs/plan/OP_E_03_LECTURA_TRAMO3_V98.jsonl, la unica
`correccion_v99` con `campo_corregido` "vara (cita)" (la via que no toca
`direccion_leida`) esta en el PUESTO 148, no en el 147: el 147 trae
`correccion_v99` con `campo_corregido` "direccion_leida" (pasa a NO
RESUELTA), que es la otra via, la que TAREA 3.2 pide evitar ("sin tocar
direccion_leida"). El precedente real que este script sigue es el 148.

VERIFICACION CONTRA EL GRAFO DE HOY (TAREA 3.1, no copiada de la razon vieja
de la fila): dataset/metadata/master_graph.json,
`customer_discovery_get_out_of_building.pasos_accionables`:
  1. "Identifica tus hipotesis clave sobre el problema, el cliente y la solucion"
  2. "Sal a entrevistar clientes potenciales de forma repetida durante semanas o meses"
  3. "Evita las encuestas de foco tradicionales o las listas exhaustivas de funciones (features)"
  4. "Anota lo que aprendes y lo comparas con lo que pensabas al principio"
El barrido caso el paso 1. El hijo, `prueba_solucion_con_cliente`
(pasos_accionables: ampliar la lista de contactos a 10+ clientes, preguntas
de presupuesto, explorar el limite de precio, preguntar canal de
distribucion, preguntar el proceso de aprobacion de compra, anotar cada
entrevista en una ficha), es el PROCEDIMIENTO ENTERO del paso 2 (entrevistar
clientes potenciales de forma repetida, con protocolo), no del paso 1
(identificar hipotesis). CONFIRMADO: la razon vieja de la fila acertaba.

QUE HACE. Anade `correccion_v108` en el puesto_tramo 46 de
docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl, con `campo_corregido` igual a
"vara (cita)" (mismo campo que el precedente del puesto 148, valor_nuevo que
aclara que 9.6.2 cubre el test de UN paso sin decir cual), SIN TOCAR
`direccion_leida` ni `clase`. `contar_cierre_efectivo.py` reconoce ese campo
EXPRESAMENTE como sin efecto sobre los dos conteos: la cifra de cierre no se
mueve.

USO:
  python scripts/loop/vuelta108_tarea3_correccion_46.py
"""
import json

RUTA = "docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl"

AGREGADO = {
    "campo_corregido": "vara (cita)",
    "valor_anterior": "banco 9.6.1 rama contenido manda; direccion por 9.6.2; tamano del solape no decide por 9.6.3",
    "valor_nuevo": "banco 9.6.1 rama contenido manda; direccion por 9.6.2 (incluye el test de UN paso, sin decir cual); tamano del solape no decide por 9.6.3",
    "razon": (
        "CORRECCION DE CITA DECLARADA (vuelta 108, TAREA 3, remedio de la caida 1.1 del "
        "acta de la vuelta 107). El texto viejo de razon NO SE BORRA. VERIFICADO CONTRA EL "
        "GRAFO DE HOY (no copiado de la razon vieja): customer_discovery_get_out_of_building "
        "trae, en pasos_accionables, el paso 1 ('Identifica tus hipotesis clave sobre el "
        "problema, el cliente y la solucion', el que el barrido caso) y el paso 2 ('Sal a "
        "entrevistar clientes potenciales de forma repetida durante semanas o meses'). El "
        "hijo, prueba_solucion_con_cliente, es el procedimiento ENTERO del paso 2 (ampliar la "
        "lista de contactos a diez o mas clientes, preguntas de presupuesto, explorar el "
        "limite de precio, preguntar canal de distribucion y proceso de aprobacion de compra, "
        "anotar cada entrevista en una ficha), no del paso 1. La licencia de leer contra un "
        "paso distinto del que el barrido caso no la cubre el 9.6.3 (habla del TAMANO del "
        "solape, no de que linea mirar): la cubre el 9.6.2, cuyo test de reconocimiento dice "
        "'el hijo cabe entero dentro de UN paso de la madre', UN, sin decir cual. MISMA VIA "
        "QUE EL PRECEDENTE: el puesto 148 de docs/plan/OP_E_03_LECTURA_TRAMO3_V98.jsonl trae "
        "correccion_v99 con este mismo campo_corregido y el mismo texto de vara corregido, "
        "para el mismo defecto (paso citado por el barrido distinto del paso que el hijo "
        "ejecuta de verdad). DISCREPANCIA DECLARADA CONTRA EL ENCARGO (docs/loop/"
        "PROMPT_SIGUIENTE.md, TAREA 3): el encargo nombra este precedente como 'el 147', pero "
        "medido hoy el 147 trae correccion_v99 con campo_corregido 'direccion_leida' (pasa a "
        "NO RESUELTA), no 'vara (cita)'; el precedente real de la via que no toca "
        "direccion_leida es el 148. LA LECTURA NO SE TOCA: direccion_leida sigue siendo "
        "'customer_discovery_get_out_of_building -> prueba_solucion_con_cliente' y clase sigue "
        "D. Solo se corrige la cita de la vara."
    ),
}


def main():
    with open(RUTA, encoding="utf-8") as f:
        filas = [json.loads(l) for l in f if l.strip()]

    tocadas = 0
    for fila in filas:
        if fila.get("puesto_tramo") == 46:
            assert "correccion_v108" not in fila
            fila["correccion_v108"] = AGREGADO
            tocadas += 1
    assert tocadas == 1, tocadas

    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        for fila in filas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

    print("puesto 46: correccion_v108 anadida (campo 'vara (cita)'). tocadas=%d" % tocadas)


if __name__ == "__main__":
    main()
