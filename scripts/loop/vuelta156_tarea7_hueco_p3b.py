# -*- coding: utf-8 -*-
"""vuelta156_tarea7_hueco_p3b.py . TAREA 7 DE LA VUELTA 156.

EL HUECO DE LA P3b, CONTADO Y NOMBRADO (adjudicacion 6.6 del acta 155).

LO QUE EL ACTA CONCEDE Y LO QUE PIDE. La P3b se queda como PROXY declarado (re
correr 71 mutaciones por vuelta no cabe) y su RESPALDO es
`scripts/loop/verificar_mutaciones_viejas.py`, que corre su bateria entera cada
vuelta al cierre, la hace MORDER y comprueba que su salida sellada se repite. Lo
que falta es NOMBRAR EL HUECO: cuantas de las fichas que se apoyan en la P3b
citan un caso positivo que la bateria NO cubre.

COMO SE MIDE, Y LAS DOS NOMINAS SALEN DE SU FICHERO, NINGUNA SE TECLEA:
  - las fichas y sus citas, de `docs/plan/OPERACIONES.jsonl`, con el MISMO patron
    que `p3b_caso_positivo` usa (se importa de su modulo, no se copia);
  - la bateria, de `verificar_mutaciones_viejas.VIEJAS` (se importa igual).

LA CORRESPONDENCIA ENTRE UNA SALIDA Y UN SCRIPT DE LA BATERIA, declarada porque
es lo unico que este instrumento decide: `SALIDA_V135_2E_MUTACION_1.txt` se
corresponde con `vuelta135_2e_mutacion_1.py`, o sea que se quita el prefijo
`SALIDA_` y el sufijo `.txt`, se pasa a minusculas y se compara con el nombre del
script sin `.py`. Si el nombre normalizado de la salida coincide con el de algun
script de la bateria, esa cita ESTA CUBIERTA.

Y EL LIMITE DE ESA CORRESPONDENCIA, dicho en vez de callarse (banco 9): es por
NOMBRE. Una salida escrita por un script que la bateria SI corre pero que se
llame de otra forma saldria aqui como NO CUBIERTA, o sea que este barrido SOBRE
ESTIMA EL HUECO, nunca lo sub estima. Para el proposito de la adjudicacion (poner
cota al agujero) el lado seguro es ese.

USO:  python scripts/loop/vuelta156_tarea7_hueco_p3b.py
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import verificar_mutaciones_viejas as B  # noqa: E402

# EL PATRON DE LA P3b NO SE COPIA A MANO: SE LEE DEL FICHERO QUE LO DEFINE.
# No se puede importar el modulo (vuelta150_3_relectura_expediente.py corre su
# main() al importarse y exigiria --corte), asi que se extrae su definicion del
# codigo fuente y se compila aqui. Si aquel cambia el patron, este lo sigue solo;
# si la definicion desaparece, esto cae en ROJO en vez de seguir con una copia
# envejecida.
def _patron_de_la_p3b():
    fuente = io.open(os.path.join(RAIZ, "scripts", "loop",
                                  "vuelta150_3_relectura_expediente.py"),
                     encoding="utf-8").read()
    marca = "PATRON_CASO_POSITIVO = re.compile("
    i = fuente.index(marca)
    # la definicion acaba en la primera linea en blanco que la sigue
    j = fuente.index(chr(10) + chr(10), i)
    entorno = {"re": re}
    exec(fuente[i:j], entorno)
    return entorno["PATRON_CASO_POSITIVO"]


PATRON_CASO_POSITIVO = _patron_de_la_p3b()

OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
LOOP = os.path.join(RAIZ, "docs", "loop")


def fichas():
    return [json.loads(x) for x in io.open(OPS, encoding="utf-8") if x.strip()]


def citas_de(f):
    partes = []
    for k in ("verificacion", "evidencia"):
        v = f.get(k)
        partes += v if isinstance(v, list) else [str(v or "")]
    for k in ("nota", "adjudicacion"):
        partes.append(str(f.get(k) or ""))
    return sorted(set(PATRON_CASO_POSITIVO.findall(" ".join(partes))))


def normalizar_salida(nombre):
    n = nombre.lower()
    if n.startswith("salida_"):
        n = n[len("salida_"):]
    if n.endswith(".txt"):
        n = n[:-4]
    return n


def main():
    F = fichas()
    bateria = [s for s, _admite in B.VIEJAS]
    stems = {s[:-3].lower() for s in bateria}

    print("=" * 104)
    print("VUELTA 156, TAREA 7: EL HUECO DE LA P3b, CONTADO Y NOMBRADO")
    print("=" * 104)
    print("Fichas del expediente: %d" % len(F))
    print("Scripts de la bateria de respaldo (verificar_mutaciones_viejas.VIEJAS): %d"
          % len(bateria))
    print("")
    print("LA BATERIA, UNA A UNA (leida de VIEJAS, no tecleada):")
    for s in bateria:
        print("   %s" % s)
    print("")
    print("CIFRA scripts de la bateria: %d fichero(s)" % len(bateria))
    print("")

    con_p3b, sin_p3b = [], []
    cubiertas, huecas = [], []
    for f in sorted(F, key=lambda x: x["id_op"]):
        cit = citas_de(f)
        presentes = [c for c in cit if os.path.exists(os.path.join(LOOP, c))]
        if not presentes:
            sin_p3b.append(f["id_op"])
            continue
        con_p3b.append(f["id_op"])
        cub = [c for c in presentes if normalizar_salida(c) in stems]
        no = [c for c in presentes if normalizar_salida(c) not in stems]
        if no:
            huecas.append((f["id_op"], f.get("fase"), f.get("estado"), no, cub))
        else:
            cubiertas.append((f["id_op"], f.get("fase"), f.get("estado"), cub))

    print("=" * 104)
    print("EL HUECO, CONTADO")
    print("=" * 104)
    print("| |  |")
    print("|---|---:|")
    print("| fichas del expediente | %d |" % len(F))
    print("| fichas que CITAN un caso positivo presente en el arbol (o sea, que se apoyan en la P3b) | %d |" % len(con_p3b))
    print("| de ellas, con TODAS sus citas cubiertas por la bateria | %d |" % len(cubiertas))
    print("| de ellas, CON AL MENOS UNA CITA QUE LA BATERIA NO CUBRE | %d |" % len(huecas))
    print("| fichas que no citan ningun caso positivo presente | %d |" % len(sin_p3b))
    print("")
    print("CIFRA fichas que se apoyan en la P3b: %d operaciones" % len(con_p3b))
    print("CIFRA fichas con su caso positivo cubierto por la bateria: %d operaciones" % len(cubiertas))
    print("CIFRA fichas con al menos una cita que la bateria no cubre: %d operaciones" % len(huecas))
    print("")

    print("=" * 104)
    print("LA NOMINA DEL HUECO, UNA A UNA, CON LAS CITAS QUE NADIE RE CORRE")
    print("=" * 104)
    if not huecas:
        print("  NINGUNA. La bateria cubre todas las citas de la P3b.")
    for i, fase, estado, no, cub in huecas:
        print("")
        print("  %-16s fase %-22s estado %s" % (i, fase, estado))
        print("     citas NO cubiertas por la bateria (%d): %s" % (len(no), ", ".join(no)))
        if cub:
            print("     citas SI cubiertas (%d): %s" % (len(cub), ", ".join(cub)))

    print("")
    print("=" * 104)
    print("LAS CUBIERTAS, PARA QUE EL CONTRASTE SE VEA")
    print("=" * 104)
    if not cubiertas:
        print("  NINGUNA cita de la P3b esta cubierta por la bateria.")
    for i, fase, estado, cub in cubiertas:
        print("  %-16s fase %-22s estado %-6s citas: %s" % (i, fase, estado, ", ".join(cub)))

    print("")
    print("=" * 104)
    print("LO QUE ESTA CIFRA SIGNIFICA, DICHO SIN ADORNO")
    print("=" * 104)
    print("  La P3b da por buena una ficha porque CITA UN ARTEFACTO QUE EXISTE, no porque")
    print("  la prueba se haya vuelto a correr. Para las %d fichas cubiertas, la bateria SI"
          % len(cubiertas))
    print("  vuelve a correr esa prueba cada vuelta al cierre y la hace morder. Para las %d"
          % len(huecas))
    print("  del hueco, el artefacto existe y NADIE LO RE CORRE: la unica garantia es que el")
    print("  fichero esta ahi. ESE ES EL AGUJERO DEL PROXY, y ahora esta contado.")
    print("=" * 104)
    return 0


raise SystemExit(main())
