# -*- coding: utf-8 -*-
r"""_v204_t1b_ambiguedad.py . LA MEDICION QUE LA ENTRADA NO PODIA PUBLICAR:
QUE HAY DENTRO DE LAS DOS SECCIONES QUE TITULAN `ADJUDICACIONES` EN LAS ACTAS
177 Y 178, Y DE QUE CONVENCION SON.

PREFIJO DE GUION BAJO: computo de una vuelta, fuera del censo y fuera de la
nomina (`AUDITOR.md` 6.3, `4.5` del acta 199, `4.6` del acta 203). NO VIGILA A
NADIE Y NO ESCRIBE EN NINGUNA SEDE: imprime y sella su propia salida.

POR QUE EXISTE, Y ES UNA MEDICION Y NO UNA DECISION. La vara del `4.1` del acta
202 dice que **el numeral se toma de la seccion cuyo PROPIO TITULO lo nombra**.
En las dos actas de esta deuda **hay DOS secciones cuyo titulo lo nombra**, asi
que el numeral queda NO COMPUTABLE y `R.67` y `R.68` lo declaran en vez de
publicar un cero. **Elegir una de las dos seria DECIDIR, y decidir no me toca.**
Lo que SI se puede hacer, y es lo que hace este fichero, es **publicar el
reparto entero de LAS DOS**, con sus dos lecturas, para que el auditor adjudique
sobre cifras y no sobre una ausencia.

Y CONTESTA LA OTRA PREGUNTA DEL ENCARGO, *comprueba tu de que convencion son*:
si el lector heredado (el que EXIGE comillas inversas) da cero sobre la seccion,
el acta es de la convencion anterior a la 184 y el heredado NO basta; si da lo
mismo que la vara ancha, el heredado basta y se dice.

USO: python scripts/loop/_v204_t1b_ambiguedad.py
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

sys.path.insert(0, AQUI)
import _v203_reparto_de_actas_viejas as REP                 # noqa: E402

SUJETOS = [177, 178]
L = []


def w(s=""):
    L.append(s)


w("=" * 78)
w("VUELTA 204, TAREA 1.c: EL REPARTO ENTERO DE LAS DOS SECCIONES QUE TITULAN")
w("ADJUDICACIONES EN LAS ACTAS 177 Y 178, Y LA CONVENCION DE CADA UNA.")
w("=" * 78)
w("")
w("LA VARA ES LA DEL 4.1 DEL ACTA 202 Y NO SE TOCA: el numeral se toma de la")
w("seccion cuyo PROPIO TITULO lo nombra. AQUI HAY DOS, asi que el numeral es NO")
w("COMPUTABLE y R.67 y R.68 lo declaran. ESTE FICHERO NO ELIGE: PUBLICA LAS DOS.")
w("")

for vuelta in SUJETOS:
    lineas, cota, err = REP.cuerpo_del_acta(vuelta)
    w("=" * 78)
    w("ACTA %d" % vuelta)
    w("=" * 78)
    if err:
        w("   ROJO: %s" % err)
        continue
    ini, fin = cota
    w("   cuerpo acotado HOY: lineas %d a %d, %d lineas"
      % (ini, fin, fin - ini + 1))
    secs = REP.secciones(lineas, ini, fin)
    cand = REP.seccion_por_titulo(secs, REP.MARCAS["adjudicaciones"])
    w("   CIFRA secciones cuyo TITULO nombra el numeral de adjudicaciones: %d"
      % len(cand))
    for num, i, titulo, a, b in cand:
        anchas, donde = REP.claves_de(lineas, (num, i, titulo, a, b))
        heredadas, _d = REP.claves_de(lineas, (num, i, titulo, a, b),
                                      REP.PLANTILLA_VIEJA)
        w("")
        w("   SECCION %d, linea %d, lineas %d a %d" % (num, i, a, b))
        w("      titulo literal, transcrito y no parafraseado: %r" % titulo)
        w("      CIFRA claves `%d.M` POR LA VARA ANCHA: %d (%s)"
          % (num, len(anchas), ", ".join(c for c, _n in anchas) or "ninguna"))
        w("      CIFRA claves `%d.M` POR EL LECTOR HEREDADO: %d (%s)"
          % (num, len(heredadas),
             ", ".join(c for c, _n in heredadas) or "ninguna"))
        if len(anchas) == len(heredadas) and anchas:
            w("      VEREDICTO DE CONVENCION: LAS DOS LECTURAS COINCIDEN, o sea que")
            w("      esta seccion YA ESCRIBE SUS CLAVES CON COMILLAS INVERSAS y EL")
            w("      LECTOR HEREDADO BASTA.")
        elif len(heredadas) == 0 and anchas:
            w("      VEREDICTO DE CONVENCION: el heredado da CERO y la vara ancha da")
            w("      %d, o sea CONVENCION ANTERIOR A LA 184: sus claves NO llevan"
              % len(anchas))
            w("      comillas inversas y EL LECTOR HEREDADO NO BASTA.")
        else:
            w("      VEREDICTO DE CONVENCION: NI UNA COSA NI LA OTRA, y se declara")
            w("      en vez de forzarse: ancha %d, heredado %d."
              % (len(anchas), len(heredadas)))
        for clave, _n in anchas:
            for ln in donde[clave]:
                w("      | `%s` | linea %d | %s"
                  % (clave, ln, lineas[ln - 1].strip()[:150]))
        if not anchas:
            w("      (ninguna clave `%d.M` en esta seccion por ninguna de las dos"
              % num)
            w("      lecturas, y ese cero es de FORMA DE CLAVE, no de contenido:")
            w("      la seccion mide %d lineas)" % (b - a + 1))
    w("")

w("=" * 78)
w("LA SERIE, RECOMPUTADA CON EL INSTRUMENTO Y NO CON UNA EXPRESION REGULAR MIA")
w("=" * 78)
import serie_de_registros as SERIE                          # noqa: E402
halladas = SERIE.entradas()
w("   CIFRA entradas: %d" % len(halladas))
w("   CIFRA colisiones: %d" % len(SERIE.colisiones(halladas)))
w("   CIFRA huecos: %d" % len(SERIE.huecos(halladas)))
w("   SIGUIENTE LIBRE: R.%d" % SERIE.siguiente_libre(halladas))
con = set()
for _n, _rel, _ln, titulo in halladas:
    for mm in re.finditer(r"del acta de la vuelta (\d+)", titulo):
        con.add(int(mm.group(1)))
sin = sorted(v for v in range(173, 181) if v not in con)
w("   CIFRA actas de la 173 a la 180 SIN entrada propia: %d" % len(sin))
w("   cuales: %s" % (", ".join(str(x) for x in sin) or "(ninguna)"))
w("")
w("FIN")

salida = NL.join(L) + NL
sys.stdout.reconfigure(encoding="utf-8")
print(salida)
io.open(os.path.join(LOOP, "SALIDA_V204_T1C_AMBIGUEDAD.txt"), "w",
        encoding="utf-8", newline=NL).write(salida)
