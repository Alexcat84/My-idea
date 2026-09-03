# -*- coding: utf-8 -*-
"""vuelta159_tarea2b_nomina_relectura.py . TAREA 2.b DE LA VUELTA 159, LA NOMINA
DEL TRAMO QUE SE RELEE AL DOBLE.

POR QUE NACE (acta 158, adjudicacion 6.5): una discrepancia FUERA de los
discutibles marcados (`LD-OPC05-005`) baja el credito de la tanda y obliga a
releer el tramo al doble. El tramo es el LOTE 1, y releerlo al doble significa
que LAS QUE CAYERON A D Y QUE NADIE HA VUELTO A MIRAR reciben una segunda pasada
independiente bajo la 6.3.

LA CIFRA NO SE TECLEA Y NO SE CREE: EL ENCARGO DICE 41 Y ESTE INSTRUMENTO LA
RECOMPUTA DE LOS FICHEROS. Si no da 41, SALE ROJO Y NO SE LEE NADA, que es lo
mismo que hizo la nomina del lote 1 en la vuelta 157.

DE DONDE SALE CADA SUMANDO, Y TODOS DE UN FICHERO DEL REPO:
  (a) EL LOTE 1, 66 ids : docs/loop/NOMINA_V157_LOTE1.json, sellado en la 157.
  (b) LAS QUE CAYERON A D: las del lote 1 cuya razon en
      docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl lleva la cabeza literal que el
      instrumento del lote escribio cuando movio la clase
      ("LOTE 1 DE LA VUELTA 157" mas "LA CLASE PASA DE C A D"). Las que
      sostuvieron C llevan otra cabeza y no cuentan.
  (c) LAS QUE EL AUDITOR YA RELEYO, de sus DOS ficheros de adjudicaciones
      selladas antes de destapar:
        docs/loop/_auditor_v158_mis_adjudicaciones.txt (la ciega de la 158)
        docs/loop/_auditor_v157_mis_adjudicaciones.txt (la ciega anterior)
      Se cruzan con (b): una relectura del auditor sobre una que sostuvo C no
      descuenta nada de este tramo, porque este tramo son las que cayeron a D.

EL RESULTADO ES (b) MENOS (c), y se sella en docs/loop/NOMINA_V159_RELECTURA.json
para que la lectura no pueda teclear su propia nomina.

USO:  python scripts/loop/vuelta159_tarea2b_nomina_relectura.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
LOTE1 = os.path.join(RAIZ, "docs", "loop", "NOMINA_V157_LOTE1.json")
CIEGA_158 = os.path.join(RAIZ, "docs", "loop", "_auditor_v158_mis_adjudicaciones.txt")
CIEGA_157 = os.path.join(RAIZ, "docs", "loop", "_auditor_v157_mis_adjudicaciones.txt")
SALIDA = os.path.join(RAIZ, "docs", "loop", "NOMINA_V159_RELECTURA.json")

CABEZA_LOTE1 = "LOTE 1 DE LA VUELTA 157"
CABEZA_A_D = "LA CLASE PASA DE C A D"

ESPERADO = 41


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def entradas():
    return [json.loads(x) for x in leer(REGISTRO).splitlines() if x.strip()]


def ld_de(e):
    return e["cita"].split(",")[0].strip()


def ids_de_ciega(ruta):
    """Los ids que el auditor sello en su fichero de adjudicaciones a ciegas.
    Se aceptan las dos formas en que los escribio: `LD-OPC05-007` (ciega de la
    157) y `027 = D` a principio de linea (ciega de la 158)."""
    texto = leer(ruta)
    ids = set(re.findall(r"LD-OPC05-(\d{3})", texto))
    ids |= set(re.findall(r"^\s{0,4}(\d{3})\s*=\s*[A-Z]", texto, re.M))
    return {"LD-OPC05-" + x for x in ids}


def main():
    print("=" * 78)
    print("VUELTA 159, TAREA 2.b: LA NOMINA DEL TRAMO QUE SE RELEE AL DOBLE")
    print("=" * 78)
    print("")

    lote1 = json.load(io.open(LOTE1, encoding="utf-8"))["lote"]
    E = {ld_de(e): e for e in entradas()}
    print("A) LOS SUMANDOS, CADA UNO DE SU FICHERO")
    print("   CIFRA ids del lote 1 (docs/loop/NOMINA_V157_LOTE1.json): %d" % len(lote1))

    cayeron = []
    sostuvieron = []
    for ld in lote1:
        e = E.get(ld)
        if e is None:
            print("   ROJO: %s esta en la nomina del lote 1 y no en el registro." % ld)
            return 1
        if CABEZA_LOTE1 in e["razon"] and CABEZA_A_D in e["razon"]:
            cayeron.append(ld)
        else:
            sostuvieron.append(ld)
    print("   CIFRA del lote 1 que CAYERON A D: %d" % len(cayeron))
    print("   CIFRA del lote 1 que SOSTUVIERON C: %d (%s)"
          % (len(sostuvieron), ", ".join(sostuvieron)))

    c158 = ids_de_ciega(CIEGA_158)
    c157 = ids_de_ciega(CIEGA_157)
    print("   CIFRA ids sellados en la ciega de la 158: %d" % len(c158))
    print("   CIFRA ids sellados en la ciega anterior (157): %d" % len(c157))

    ya_158 = sorted(set(cayeron) & c158)
    ya_157 = sorted(set(cayeron) & c157)
    ya = sorted(set(ya_158) | set(ya_157))
    print("   CIFRA de las caidas a D que la ciega de la 158 releyo: %d" % len(ya_158))
    print("      %s" % ", ".join(ya_158))
    print("   CIFRA de las caidas a D que la ciega anterior leyo: %d" % len(ya_157))
    print("      %s" % ", ".join(ya_157))
    print("   CIFRA solapadas entre las dos ciegas: %d"
          % len(set(ya_158) & set(ya_157)))
    print("   CIFRA de las caidas a D con segunda lectura YA HECHA: %d" % len(ya))
    print("")

    nomina = [x for x in cayeron if x not in set(ya)]
    print("B) EL TRAMO QUE SE RELEE, RECOMPUTADO")
    print("   %d menos %d da %d" % (len(cayeron), len(ya), len(nomina)))
    print("   CIFRA que el encargo declara: %d" % ESPERADO)
    print("")
    print("LA NOMINA ENTERA, EN ORDEN:")
    for i in range(0, len(nomina), 6):
        print("  " + "  ".join("%-16s" % x for x in nomina[i:i + 6]))
    print("")

    if len(nomina) != ESPERADO:
        print("ROJO: el computo da %d y el encargo declara %d." % (len(nomina), ESPERADO))
        print("SE PARA Y NO SE LEE NADA.")
        print("FIN")
        return 1

    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as fh:
        json.dump({"tramo": nomina,
                   "cayeron_a_d": cayeron,
                   "sostuvieron_c": sostuvieron,
                   "ya_releidas_por_el_auditor": ya},
                  fh, ensure_ascii=False, indent=1)
    print("CIFRA lecturas del tramo que se relee al doble: %d" % len(nomina))
    print("nomina sellada en docs/loop/NOMINA_V159_RELECTURA.json")
    print("")
    print("VERDE: el computo reproduce la cifra del encargo. Se puede leer.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
