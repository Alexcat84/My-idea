# -*- coding: utf-8 -*-
"""VUELTA 18, TAREA 1.2: adicion declarada al final del campo nota de la entrada
de tipo `defecto` "pares que una fusion reabre" de docs/plan/INVENTARIO.jsonl.

Adjudicacion del pendiente de doctrina 3 (acta vuelta 17, seccion 4): una copia
que leida sola contradice a su fuente recibe un PUNTERO a la fuente completa. La
regla escrita en la entrada NO se reescribe.

Toca UNA sola linea. Verifica antes y despues que las otras 670 quedan identicas
byte a byte.
"""
import io
import json

RUTA = "docs/plan/INVENTARIO.jsonl"

ADICION = (
    " ADICION DECLARADA 14 ago 2026 (vuelta 18), la regla de arriba NO se reescribe: "
    "leida sola, esta entrada se contradice, porque dice \"solo los B y los C\" y a "
    "continuacion lista un A, el 1096. NO es una contradiccion del plan: es que esta "
    "entrada no carga la excepcion. LA FUENTE COMPLETA ES docs/plan/08_VERIFICACION.md, "
    "seccion \"LA LISTA, barrida el 12 ago 2026 sobre las diecisiete fusiones del plan\", "
    "donde el 1096 vive con su motivo escrito: su contraparte muere y su A se volveria "
    "contradiccion con su propia D. Ante cualquier duda manda 08_VERIFICACION.md."
)

NOMBRE = "pares que una fusion reabre"


def main():
    with io.open(RUTA, encoding="utf-8") as fh:
        lineas = fh.read().split("\n")

    tocadas = []
    salida = []
    for i, linea in enumerate(lineas):
        if not linea.strip():
            salida.append(linea)
            continue
        d = json.loads(linea)
        if d.get("tipo") == "defecto" and d.get("nombre") == NOMBRE:
            if ADICION.strip() in d["nota"]:
                print("YA ESTABA PUESTA, no se toca nada")
                return
            d["nota"] = d["nota"] + ADICION
            salida.append(json.dumps(d, ensure_ascii=False))
            tocadas.append(i + 1)
        else:
            salida.append(linea)

    if len(tocadas) != 1:
        raise SystemExit("ESPERABA UNA SOLA LINEA TOCADA, salieron %s" % tocadas)

    iguales = sum(1 for a, b in zip(lineas, salida) if a == b)
    print("linea tocada   : %d" % tocadas[0])
    print("lineas totales : %d" % len([l for l in lineas if l.strip()]))
    print("identicas      : %d" % len([
        1 for a, b in zip(lineas, salida) if a == b and a.strip()
    ]))
    assert iguales == len(lineas) - 1, iguales

    with io.open(RUTA, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(salida))

    # relectura de comprobacion
    with io.open(RUTA, encoding="utf-8") as fh:
        rel = [json.loads(l) for l in fh if l.strip()]
    e = [x for x in rel if x.get("tipo") == "defecto" and x.get("nombre") == NOMBRE][0]
    print("entradas tras escribir: %d" % len(rel))
    print("claves de la entrada  : %s" % sorted(e.keys()))
    print("la nota termina en    : ...%s" % e["nota"][-70:])


if __name__ == "__main__":
    main()
