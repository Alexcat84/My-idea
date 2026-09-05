# -*- coding: utf-8 -*-
r"""vuelta178_tarea1a_cuenta_censo.py . LA CUENTA DE LA NOMINA Y DEL CENSO,
ESCRITA ENTERA, QUE ES LO QUE LA CAZA.

TAREA 1.a de la vuelta 178. SOLO LECTURA: no toca la nomina, no toca ningun
fichero, no corre ningun arnes. Imprime.

POR QUE EXISTE, Y LA CAUSA ES UNA CAIDA MIA MEDIDA POR EL AUDITOR. El reporte de
la vuelta 177 publico en prosa que "el censo ve 153 arneses" y que "los 2 de la
177 no lo eran, la nomina va de 89 a 92". Las dos cifras estan mal, y el auditor
lo midio commit a commit: el censo ve 154, y faltaban TRES y no dos (88 en
`f3087229`, 89 en `2a33a295`, 89 en `0c3320dd`, 92 en `4bb4f459`). El fondo era
correcto y la accion fue correcta (los cuatro arneses estan en la nomina y la
nomina fue de 88 a 92 sin podar ninguna); lo que estaba mal eran los numeros.

Y LA CAIDA SE DELATABA SOLA, QUE ES EL MOTIVO ENTERO DE ESTE FICHERO: 153 menos
92 son 61, no los 62 que el mismo reporte publicaba. UNA CUENTA QUE NO CIERRA
CONSIGO MISMA SE CAZA SOLA SI ALGUIEN LA ESCRIBE ENTERA. En prosa, cada cifra
suelta parece verdadera; en una tabla con su resta al lado, la que sobra canta.
Por eso la letra del encargo pide la tabla ENTERA y no la prosa, y por eso este
instrumento la imprime con LA RESTA COMPROBADA dentro.

QUE PUBLICA, Y TODO COMPUTADO DE LAS FUNCIONES PURAS DE LA PROPIA BATERIA
(`EJECUTOR.md` 2, EL INSTRUMENTO MANDA; ninguna cifra se teclea):

  (1) cuantos arneses ve `arneses_del_directorio()`;
  (2) cuantas entradas tiene `VIEJAS`;
  (3) cuantos del censo estan FUERA de la nomina;
  (4) cuantas entradas de la nomina el censo NO VE
      (`nomina_invisible_al_censo()`);
  (5) LA RESTA COMPROBADA, con su identidad escrita y verificada.

LA IDENTIDAD QUE SE COMPRUEBA, DICHA ANTES DE MEDIRLA para que no se pueda
elegir despues: si el censo VE a todas las entradas de la nomina (o sea si (4)
es cero), entonces la nomina esta contenida en el censo y CENSO MENOS NOMINA
TIENE QUE SER EXACTAMENTE (3). Si (4) NO fuera cero, la identidad correcta es
otra y este fichero la escribe tambien: censo menos nomina mas invisibles.
LAS DOS SE PUBLICAN SIEMPRE, salga lo que salga, para que la que gobierna hoy no
tape a la otra.

CAE EN ROJO (exit 1) si la identidad no se cumple. Un censo cuya aritmetica no
cierra no es una discrepancia de gusto: es una de las dos cifras mintiendo.

LAS CIFRAS VIEJAS NO SE BORRAN, SE PONEN AL LADO (banco 9.10, correccion
declarada). Este fichero imprime las que el reporte 177 publico y las que el
acta 178 midio, junto a la medicion de HOY, y dice cual coincide con cual.

USO:
  python scripts/loop/vuelta178_tarea1a_cuenta_censo.py
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import verificar_mutaciones_viejas as V   # noqa: E402

NL = chr(10)

# LO QUE CADA SEDE PUBLICO, PARA PONERLO AL LADO Y NO PARA CREERLE. Son citas,
# no fuentes: `EJECUTOR.md` 2 dice que una nota vieja NUNCA es fuente de una
# cifra nueva, y que si discrepa de la medicion de hoy, la discrepancia se
# declara en vez de resolverse copiando.
CITAS = [
    ("reporte de la vuelta 177 (mio, prosa del cuerpo)", 153, 92, 2),
    ("acta del auditor de la vuelta 178, medido commit a commit", 154, 92, 3),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    p("=" * 78)
    p("LA CUENTA DE LA NOMINA Y DEL CENSO, ESCRITA ENTERA (vuelta 178, TAREA 1.a)")
    p("=" * 78)
    p("")

    censo = V.arneses_del_directorio()
    nomina = [s for s, _admite in V.VIEJAS]
    invisibles = V.nomina_invisible_al_censo()
    fuera = sorted(set(censo) - set(nomina))
    dentro_y_visto = sorted(set(censo) & set(nomina))

    p("A) DE DONDE SALE CADA CIFRA, NOMBRADO ANTES DE IMPRIMIRLA")
    p("   (1) arneses_del_directorio()  sobre %s"
      % os.path.relpath(V.LOOP, RAIZ).replace(os.sep, "/"))
    p("   (2) len(VIEJAS), la nomina de scripts/loop/verificar_mutaciones_viejas.py")
    p("   (3) censo menos nomina, computado aqui con conjuntos")
    p("   (4) nomina_invisible_al_censo(), la funcion pura de la propia bateria")
    p("   el universo del censo, nombrado: ficheros `vuelta<N>...<familia>...py`")
    p("   con familia en %s" % ", ".join(V.FAMILIAS_DE_ARNES))
    p("")

    p("B) LA TABLA, ENTERA Y NO EN PROSA")
    p("")
    p("| que se cuenta | instrumento | cifra |")
    p("|---|---|---|")
    p("| arneses que ve el censo | `arneses_del_directorio()` | **%d** |" % len(censo))
    p("| entradas de la nomina | `len(VIEJAS)` | **%d** |" % len(nomina))
    p("| del censo, FUERA de la nomina | conjuntos, aqui | **%d** |" % len(fuera))
    p("| de la nomina, que el censo NO VE | `nomina_invisible_al_censo()` | **%d** |"
      % len(invisibles))
    p("| del censo y de la nomina a la vez | conjuntos, aqui | **%d** |"
      % len(dentro_y_visto))
    p("")

    p("C) LA RESTA COMPROBADA, QUE ES LO QUE CAZA UNA CIFRA SUELTA")
    izq = len(censo) - len(nomina)
    der = len(fuera) - len(invisibles)
    p("   IDENTIDAD GENERAL, valida siempre:")
    p("      censo - nomina = (fuera de la nomina) - (invisibles al censo)")
    p("      %d - %d = %d   contra   %d - %d = %d"
      % (len(censo), len(nomina), izq, len(fuera), len(invisibles), der))
    p("      CALZAN: %s" % ("SI" if izq == der else "NO"))
    p("   IDENTIDAD SIMPLE, valida SOLO si los invisibles son cero:")
    p("      censo - nomina = fuera de la nomina")
    p("      %d - %d = %d   contra   %d" % (len(censo), len(nomina), izq, len(fuera)))
    p("      gobierna hoy: %s (invisibles = %d)"
      % ("SI" if not invisibles else "NO", len(invisibles)))
    p("      CALZAN: %s" % ("SI" if izq == len(fuera) else "NO"))
    p("")

    p("D) LAS CIFRAS QUE OTRAS SEDES PUBLICARON, AL LADO Y NO EN VEZ DE")
    p("   (banco 9.10: una correccion que tapa lo que corrige no se puede auditar)")
    p("")
    p("| sede | censo | nomina | faltaban | su resta | cuadra consigo misma |")
    p("|---|---|---|---|---|---|")
    for sede, c_censo, c_nomina, c_faltaban in CITAS:
        p("| %s | %d | %d | %d | %d | %s |"
          % (sede, c_censo, c_nomina, c_faltaban, c_censo - c_nomina,
             "SI" if (c_censo - c_nomina) == len(fuera) else
             "NO: su resta da %d y fuera de la nomina hay %d"
             % (c_censo - c_nomina, len(fuera))))
    p("| medicion de HOY, este instrumento | %d | %d | (lo dice la 1.b) | %d | SI |"
      % (len(censo), len(nomina), izq))
    p("")

    p("E) LOS QUE ESTAN FUERA DE LA NOMINA, UNO A UNO Y POR VUELTA")
    por_vuelta = {}
    for n in fuera:
        por_vuelta.setdefault(V.vuelta_de(n), []).append(n)
    for v in sorted(por_vuelta, key=lambda x: (x is None, x)):
        p("   vuelta %-5s %d: %s" % (v, len(por_vuelta[v]), ", ".join(por_vuelta[v])))
    p("   CIFRA vueltas distintas representadas fuera de la nomina: %d" % len(por_vuelta))
    p("")

    p("F) LAS ENTRADAS DE LA NOMINA QUE EL CENSO NO VE")
    if not invisibles:
        p("   (ninguna)")
    for n in invisibles:
        p("   INVISIBLE AL CENSO: %s" % n)
    p("")

    malas = []
    if izq != der:
        malas.append("la identidad general no se cumple: %d contra %d" % (izq, der))
    if not invisibles and izq != len(fuera):
        malas.append("los invisibles son cero y aun asi censo menos nomina (%d) no es "
                     "los que estan fuera (%d)" % (izq, len(fuera)))
    if malas:
        p("ROJO: la cuenta no cierra consigo misma, %d motivo(s):" % len(malas))
        for m in malas:
            p("   " + m)
        p("FIN")
        return 1
    p("VERDE: la cuenta cierra consigo misma. Censo %d, nomina %d, fuera de la "
      "nomina %d, invisibles al censo %d, y las dos identidades se cumplen."
      % (len(censo), len(nomina), len(fuera), len(invisibles)))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
