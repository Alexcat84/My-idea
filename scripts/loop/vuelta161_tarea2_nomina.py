# -*- coding: utf-8 -*-
"""vuelta161_tarea2_nomina.py . TAREA 2 DE LA VUELTA 161, LA NOMINA DEL TRAMO.

LAS CATORCE QUE HOY ESTAN EN `C`, RECOMPUTADAS DEL REGISTRO Y NO COPIADAS DEL
ENCARGO. Si no dan CATORCE, o si no calzan ELEMENTO A ELEMENTO con las catorce
que el encargo nombra, SALE ROJO Y NO SE LEE NADA.

POR QUE SE RECOMPUTA UNA NOMINA QUE EL ENCARGO YA TRAE ESCRITA: `EJECUTOR.md` 2,
"el instrumento manda". El encargo dice que las conto hoy y que las cifras de la
parada reproducen al digito; eso es un CONTRASTE, no la fuente.

Y SE COMPRUEBAN ADEMAS LAS CUATRO QUE **NO** ENTRAN, porque el encargo lo manda
con letra expresa: `094`, `100`, `101` y `118` ya estan en `D` con su correccion
declarada dentro de la cita y NO SE VUELVEN A TOCAR. Se verifica que ninguna de
las cuatro este en la nomina y que las cuatro esten en `D`.

Y LOS CUATRO EJEMPLARES DE LA VARA CONGELADA (`P.5.1`) SE COMPRUEBAN CONTRA EL
REGISTRO ANTES DE LEER NADA: `052` y `095` aceptan (tienen que estar en `C`),
`122` y `100` excluyen (tienen que estar en `D`). Si un ejemplar de la vara no
lee como la vara dice, eso es la vara contra el registro y se para.

SALIDA: `docs/loop/NOMINA_V161_TRAMO_C.json`, con la clave `tramo`, que es la
que `vuelta159_dossier.py --nomina` sabe leer.

USO:  python scripts/loop/vuelta161_tarea2_nomina.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
SALIDA = os.path.join(LOOP, "NOMINA_V161_TRAMO_C.json")

# CONTRASTE, no fuente: los catorce que el encargo de la vuelta 161 nombra.
CONTRASTE_ENCARGO = ["005", "038", "049", "052", "068", "081", "084", "087",
                     "088", "095", "098", "109", "110", "116"]

# Las cuatro que el encargo excluye con letra expresa.
NO_ENTRAN = ["094", "100", "101", "118"]

# Los cuatro ejemplares de la vara congelada P.5.1: (numero, clase que la vara dice)
EJEMPLARES = [("052", "C"), ("095", "C"), ("122", "D"), ("100", "D")]


def ld_de(e):
    return e["cita"].split(",")[0].strip()


def main():
    print("=" * 78)
    print("VUELTA 161, TAREA 2: LA NOMINA DE LAS CATORCE EN C, RECOMPUTADA")
    print("=" * 78)
    print("")
    E = [json.loads(x) for x in io.open(REGISTRO, encoding="utf-8") if x.strip()]
    ld = [e for e in E if e.get("via") == "LECTURA_DIRIGIDA"]
    print("A) EL REGISTRO DE HOY, CONTADO DE SU FICHERO")
    print("   CIFRA filas: %d" % len(E))
    print("   CIFRA de LECTURA_DIRIGIDA: %d" % len(ld))
    print("   CIFRA de CRIBADO: %d" % len([e for e in E if e.get("via") == "CRIBADO"]))
    for c in ("A", "B", "C", "D"):
        print("   CIFRA en clase %s (todo el registro): %d"
              % (c, len([e for e in E if e.get("clase") == c])))
    print("")

    nomina = sorted(ld_de(e) for e in ld if e.get("clase") == "C")
    print("B) LAS QUE HOY ESTAN EN C, RECOMPUTADAS")
    for x in nomina:
        print("   %s" % x)
    print("   CIFRA recomputada: %d" % len(nomina))
    print("")

    print("C) EL COTEJO CONTRA EL CONTRASTE DEL ENCARGO, ELEMENTO A ELEMENTO")
    contraste = sorted("LD-OPC05-%s" % n for n in CONTRASTE_ENCARGO)
    print("   CIFRA que el encargo nombra: %d" % len(contraste))
    sobran = [x for x in nomina if x not in contraste]
    faltan = [x for x in contraste if x not in nomina]
    print("   CIFRA en la recomputada y no en el encargo: %d %s" % (len(sobran), sobran))
    print("   CIFRA en el encargo y no en la recomputada: %d %s" % (len(faltan), faltan))
    if sobran or faltan:
        print("   ROJO: no calzan. NO SE LEE NADA.")
        return 1
    print("   CALZAN ELEMENTO A ELEMENTO.")
    print("")

    print("D) LAS CUATRO QUE NO ENTRAN, COMPROBADAS (letra expresa del encargo)")
    clases = {ld_de(e): e["clase"] for e in ld}
    mal = []
    for n in NO_ENTRAN:
        idn = "LD-OPC05-%s" % n
        dentro = idn in nomina
        clase = clases.get(idn)
        print("   %-16s clase HOY %s   en la nomina: %s" % (idn, clase, dentro))
        if dentro or clase != "D":
            mal.append(idn)
    if mal:
        print("   ROJO: %s" % ", ".join(mal))
        return 1
    print("   LAS CUATRO EN D Y NINGUNA EN LA NOMINA.")
    print("")

    print("E) LOS CUATRO EJEMPLARES DE LA VARA CONGELADA (P.5.1), CONTRA EL REGISTRO")
    mal = []
    for n, esperada in EJEMPLARES:
        idn = "LD-OPC05-%s" % n
        clase = clases.get(idn)
        ok = clase == esperada
        print("   %-16s la vara dice %s ; el registro dice %s   %s"
              % (idn, esperada, clase, "CALZA" if ok else "NO CALZA"))
        if not ok:
            mal.append(idn)
    if mal:
        print("   PARADA: un ejemplar de la vara no lee como la vara dice: %s"
              % ", ".join(mal))
        print("   Eso es la vara contra el registro y NO lo arregla esta vuelta.")
        return 1
    print("   LOS CUATRO CALZAN.")
    print("")

    print("F) LA GUARDA DE COHERENCIA QUE EL ENCARGO IMPONE, DECLARADA ANTES DE LEER")
    print("   DOS DE LAS CATORCE (LD-OPC05-052 y LD-OPC05-095) SON LOS EJEMPLARES DE")
    print("   ACEPTACION DE LA VARA CONGELADA. Por construccion tienen que sobrevivir")
    print("   la relectura. SI ALGUNA DE LAS DOS CAYERA, eso no es una")
    print("   reclasificacion mas: es que la lectura contradice la vara que el")
    print("   fundador acaba de congelar, y entonces SE PARA Y SE TRAE, sin tocar ni")
    print("   la clase ni la vara.")
    print("   los dos estan en la nomina: %s"
          % all(("LD-OPC05-%s" % n) in nomina for n in ("052", "095")))
    print("")

    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as fh:
        json.dump({"tramo": nomina}, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print("NOMINA SELLADA en %s" % os.path.relpath(SALIDA, RAIZ).replace("\\", "/"))
    print("CIFRA lecturas selladas: %d" % len(nomina))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
