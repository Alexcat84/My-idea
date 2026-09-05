# -*- coding: utf-8 -*-
r"""vuelta179_tarea3_etiqueta_de_fuente.py . CUANTOS LADOS LLEVAN UNA ETIQUETA
DE FUENTE QUE YA NO ES VERDAD, CONTADO Y NO SUPUESTO.

TAREA 3 de la vuelta 179. SOLO LECTURA: no escribe nada.

QUE PASA, Y LO DESTAPO ESTA MISMA VUELTA. `clases_por_par()` de
`scripts/loop/vuelta178_tarea3_anotar_triangulos.py` etiqueta con el LITERAL
`"docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)"` toda clase que venga de ese
registro, porque cuando se escribio la vuelta 177 era la unica que habia escrito
ahi. LA TAREA 2 DE ESTA MISMA VUELTA escribio ocho filas mas, de la vuelta 179, y
sus clases salen etiquetadas como si fueran de la 177.

NO SE ARREGLA AQUI, Y SE DICE POR QUE. El encargo de la vuelta 179 dice con estas
palabras: *"El campo `fuente_de_la_clase` por lado NO se toca: ya esta bien y es
lo que permitio levantar esto"*. `EJECUTOR.md` 5 dice que cuando algo contradice
una regla vigente se escribe como PARADA en el reporte y NO lo arregla el
ejecutor. Esto contradice `EJECUTOR.md` 8, *"toda cifra de un autor con su
atribucion"*. Asi que se MIDE, se publica y se para.

USO:
  python scripts/loop/vuelta179_tarea3_etiqueta_de_fuente.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "OP_L_03_LECTURAS.jsonl")
TRIANGULOS = os.path.join(RAIZ, "docs", "plan", "OP_L_03_TRIANGULOS.jsonl")
ETIQUETA = "docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("LA ETIQUETA DE FUENTE QUE YA NO ES VERDAD (vuelta 179, TAREA 3)")
    print("=" * 78)
    print("")

    print("A) QUE VUELTA ESCRIBIO CADA CLASE, CONTADO DEL REGISTRO")
    de_quien = {}
    for linea in io.open(REGISTRO, encoding="utf-8"):
        if not linea.strip():
            continue
        d = json.loads(linea)
        for k in (d.get("clases_de_los_pares_por_leer") or {}):
            de_quien[k] = d.get("vuelta")
    por_vuelta = {}
    for k, v in de_quien.items():
        por_vuelta[v] = por_vuelta.get(v, 0) + 1
    for v in sorted(por_vuelta, key=lambda x: (x is None, x)):
        print("   CIFRA pares con clase escrita por la vuelta %s: %d" % (v, por_vuelta[v]))
    print("   CIFRA pares con clase en el registro, en total: %d" % len(de_quien))
    print("")

    print("B) QUE DICE LA ETIQUETA DE CADA LADO, CONTADO DEL REGISTRO DE TRIANGULOS")
    filas = [json.loads(l) for l in io.open(TRIANGULOS, encoding="utf-8") if l.strip()]
    cuenta = {}
    del_registro = 0
    for f in filas:
        for l in f["lados"]:
            fu = l.get("fuente_de_la_clase") or "(sin fuente)"
            cuenta[fu] = cuenta.get(fu, 0) + 1
            if fu == ETIQUETA:
                del_registro += 1
    print("   CIFRA filas de docs/plan/OP_L_03_TRIANGULOS.jsonl: %d" % len(filas))
    for k in sorted(cuenta):
        print("   %-62s %d lados" % (k[:62], cuenta[k]))
    print("")

    print("C) CUANTOS DE ESOS LADOS SON DE VERDAD DE LA 177 Y CUANTOS NO")
    bien, mal, sin_saber = 0, 0, 0
    culpables = []
    for f in filas:
        for l in f["lados"]:
            if l.get("fuente_de_la_clase") != ETIQUETA:
                continue
            x, y = l["lado"]
            clave = None
            for cand in ("%s|%s" % (x, y), "%s|%s" % (y, x)):
                if cand in de_quien:
                    clave = cand
                    break
            if clave is None:
                sin_saber += 1
                continue
            if de_quien[clave] == 177:
                bien += 1
            else:
                mal += 1
                culpables.append((f["acto"], x, y, de_quien[clave]))
    print("   CIFRA lados etiquetados como de la vuelta 177: %d" % del_registro)
    print("   CIFRA de esos que SI son de la vuelta 177: %d" % bien)
    print("   CIFRA de esos que NO lo son: %d" % mal)
    print("   CIFRA de esos cuyo par no se encontro en el registro: %d" % sin_saber)
    print("   LA RESTA: %d mas %d mas %d = %d, y los etiquetados son %d. CALZA: %s"
          % (bien, mal, sin_saber, bien + mal + sin_saber, del_registro,
             "SI" if bien + mal + sin_saber == del_registro else "NO"))
    print("")
    print("   LOS MAL ETIQUETADOS, UNO A UNO:")
    for acto, x, y, v in culpables:
        print("      acto `%s` | %s + %s | lo escribio la vuelta %s y la etiqueta dice 177"
              % (acto, x, y, v))
    if not culpables:
        print("      (ninguno)")
    print("")

    print("D) EL VEREDICTO, Y ES UNA PARADA Y NO UN ARREGLO")
    if mal:
        print("   HAY %d LADO(S) CON LA ATRIBUCION EQUIVOCADA." % mal)
        print("   NO SE ARREGLA AQUI: el encargo de esta vuelta dice que")
        print("   `fuente_de_la_clase` NO SE TOCA, y `EJECUTOR.md` 5 manda escribirlo")
        print("   como PARADA en el reporte en vez de arreglarlo por cuenta propia.")
        print("   LO QUE CONTRADICE: `EJECUTOR.md` 8, toda cifra de un autor con su")
        print("   atribucion.")
        print("FIN")
        return 0
    print("   NINGUN LADO ESTA MAL ETIQUETADO HOY.")
    print("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
