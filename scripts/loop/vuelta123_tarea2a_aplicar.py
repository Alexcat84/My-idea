# -*- coding: utf-8 -*-
"""vuelta123_tarea2a_aplicar.py . Aplica la correccion 2.a del encargo de la
vuelta 123: OP-S-08.verificacion[0] dice "32 casos" y la suite tiene 27
(medido con npx vitest run, docs/loop/SALIDA_V123_TAREA2A_VITEST_ACCESOSRESUELTOS.txt).
Correccion declarada, ADITIVA, sin borrar una letra del texto viejo.
"""
import json
import io

RAIZ = "C:/Users/AlexDesk/Documents/I have an idea"
PATH = RAIZ + "/docs/plan/OPERACIONES.jsonl"

VIEJA = ("prueba propia en web/lib/engine/accesosResueltos.test.ts (32 casos, "
         "verde en SALIDA_V122_WEB_APERTURA.txt)")
CORRECCION = (
    " | CORRECCION DECLARADA (vuelta 123, TAREA 2.a): la cifra real es 27 "
    "casos, no 32. Medido con `npx vitest run lib/engine/accesosResueltos.test.ts` "
    "desde web/ (`docs/loop/SALIDA_V123_TAREA2A_VITEST_ACCESOSRESUELTOS.txt`, "
    "\"Tests  27 passed (27)\", EXIT 0); el fichero no se toco esta vuelta. LO "
    "DEMAS DEL PUNTO SIGUE CIERTO: la suite es verde y los veinte sitios estan "
    "cubiertos (acta de la vuelta 122, seccion 1.4). Solo el numero era falso."
)


def main():
    lines = io.open(PATH, encoding="utf-8").readlines()
    out = []
    tocadas = 0
    for l in lines:
        d = json.loads(l)
        if d["id_op"] == "OP-S-08":
            v0 = d["verificacion"][0]
            if VIEJA not in v0:
                raise SystemExit("ROJO: la frase vieja no aparece en OP-S-08.verificacion[0]")
            d["verificacion"][0] = v0 + CORRECCION
            tocadas += 1
        out.append(json.dumps(d, ensure_ascii=False) + "\n")
    if tocadas != 1:
        raise SystemExit("ROJO: se esperaba tocar 1 fila, se tocaron %d" % tocadas)
    io.open(PATH, "w", encoding="utf-8", newline="\n").writelines(out)
    print("OK, filas tocadas:", tocadas)


if __name__ == "__main__":
    main()
