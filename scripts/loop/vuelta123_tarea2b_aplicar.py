# -*- coding: utf-8 -*-
"""vuelta123_tarea2b_aplicar.py . Aplica la correccion 2.b del encargo de la
vuelta 123: la nota de OP-S-09 dice "familia por familia (29)" dos parrafos
despues de declarar que estructura_de_gates/estructura_gates "desaparece
entera" (toque unico de la vuelta 78). Las dos no pueden ser ciertas: restando
esa familia quedan 28 familias, 67 nodos, 39 pares (18 de dos, 9 de tres, 1 de
cuatro), medido con scripts/loop/vuelta77_op_s09_nomina.py sobre el grafo de
hoy (docs/loop/SALIDA_V123_TAREA2B_NOMINA_29.txt). Correccion declarada,
ADITIVA, al final de la nota, sin borrar una letra.
"""
import json
import io

RAIZ = "C:/Users/AlexDesk/Documents/I have an idea"
PATH = RAIZ + "/docs/plan/OPERACIONES.jsonl"

CORRECCION = (
    " CORRECCION DECLARADA (vuelta 123, TAREA 2.b, remedido por el ejecutor): "
    "esta misma nota dice \"familia por familia (29)\" dos parrafos DESPUES de "
    "declarar que estructura_de_gates y estructura_gates \"desaparece entera\" "
    "por el toque unico de la vuelta 78 (banco 9.4): las dos frases no pueden "
    "ser ciertas a la vez. Remedido con `scripts/loop/vuelta77_op_s09_nomina.py` "
    "sobre el grafo de HOY, restando esa familia (`docs/loop/"
    "SALIDA_V123_TAREA2B_NOMINA_29.txt`, 29 familias/69 nodos en crudo, la fila "
    "`[PARTICULAS] ['estructura_de_gates', 'estructura_gates']` es la que se "
    "resta): quedan 28 familias, 67 nodos, 39 pares par a par (consecutivos "
    "dentro de cada familia: 18 familias de dos con 1 par cada una, 9 de tres "
    "con 2 pares cada una, 1 de cuatro con 3 pares, 18+18+3=39). El digito 29 "
    "esta bien medido (es el censo del script, citado tres lineas antes); lo "
    "que fallaba era aplicarlo al conjunto del que la propia nota ya resta un "
    "miembro. LA LECTURA DE LA TAREA 3.a DE ESTA VUELTA CUBRE LAS 28, NO LAS 29."
)


def main():
    lines = io.open(PATH, encoding="utf-8").readlines()
    out = []
    tocadas = 0
    for l in lines:
        d = json.loads(l)
        if d["id_op"] == "OP-S-09":
            nota = d["nota"]
            if "familia por familia (29)" not in nota:
                raise SystemExit("ROJO: frase vieja no encontrada en OP-S-09.nota")
            d["nota"] = nota + CORRECCION
            tocadas += 1
        out.append(json.dumps(d, ensure_ascii=False) + "\n")
    if tocadas != 1:
        raise SystemExit("ROJO: se esperaba tocar 1 fila, se tocaron %d" % tocadas)
    io.open(PATH, "w", encoding="utf-8", newline="\n").writelines(out)
    print("OK, filas tocadas:", tocadas)


if __name__ == "__main__":
    main()
