# -*- coding: utf-8 -*-
"""vuelta52_correcciones_tarea1.py . LAS TRES PRIMERAS CORRECCIONES ADJUDICADAS
DE LA VUELTA 52, CADA UNA TRATADA POR SU ESPECIE.

POR QUE EXISTE COMO INSTRUMENTO Y NO COMO EDICION A MANO: la regla 1 del
EJECUTOR (cuarto renglon, LA TABLA SE IMPRIME, NO SE TECLEA) nacio de las dos
paradas de credito de las vueltas 31 y 32, las dos por celdas manuales que
ningun instrumento validaba. Una sustitucion escrita aqui se puede RE-CORRER y
se puede DIFF-EAR; una celda tecleada, no.

LAS TRES ESPECIES, y son distintas (acta de la vuelta 50, pregunta 5):

  1.1 CONTADOR QUE NO CUADRA CON SU PROPIA CADENA. Las filas 246, 247 y 248 de
      docs/plan/RECOMPUTO_3388.md llevan OCHO, CINCO y OCHO cifras tachadas y
      sus contadores dicen SIETE, CUATRO y SIETE. La OCTAVA (y la QUINTA) es la
      del CIERRE DE LA VUELTA 51, que fundio cuatro actos y volteo cinco
      veredictos por P.16 (puestos 820, 2426, 2523, 2662 y 498): el barrido
      9.10 de aquella vuelta movio las tres cifras y NO cuadro los tres
      contadores. La vara es el D7 de la vuelta 50: quien corrige una celda con
      contador CUADRA EL CONTADOR y ADOSA la nota fechada. El contador se
      corrige CON TACHADO y las notas viejas NO se reescriben.

  1.2 CIFRA QUE NACIO MAL, copiada de otra corrida. La celda "Al cerrar la
      vuelta 51 son los actos 4, 21, 23, 27 y 28" de docs/plan/03_FUSIONES.md
      cita SALIDA_V51_TRAMO1_CIERRE.txt, y esa salida imprime 3, 19, 21, 25 y
      26. Los ordinales publicados son los de la corrida TRAS EL LOTE A
      (SALIDA_V51_TRAMO1_TRAS_LOTE_A.txt, que imprime 4, 21, 23, 27 y 28). No
      envejecio: nacio mal.
      Y en el mismo registro, un ROTULO: "las 25 combinaciones de acto y
      superviviente viable se re-midieron". Las combinaciones medidas son 51;
      el 25 es la cuenta de los ACTOS MIXTOS. El parrafo siguiente de esa misma
      pagina ya dice "De 51 combinaciones".

  1.3 ROTULO ENVEJECIDO, la cifra se queda. La fila "los declarados 29, 32 y 36
      (hoy 26, 28 y 32)" del registro de la vuelta 49. El 26/28/32 es la
      numeracion de la APERTURA de aquella vuelta y sigue siendo exacta para
      esa corrida: lo que envejecio es la palabra "hoy". Se fecha el rotulo y
      las cifras NO se tocan.

IDEMPOTENTE: cada sustitucion comprueba primero si su resultado ya esta escrito,
y entonces no hace nada y lo dice. Re-correrlo no duplica ninguna nota.

Uso: python scripts/loop/vuelta52_correcciones_tarea1.py [--simular]
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REC = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388.md")
FUS = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")

NOTA_COMUN = (
    "La OCTAVA es la del CIERRE DE LA VUELTA 51, que fundio cuatro actos y volteo cinco "
    "veredictos por `P.16` (puestos 820, 2426, 2523, 2662 y 498). Aquel barrido `9.10` "
    "MOVIO LA CIFRA Y NO CUADRO EL CONTADOR, y esa es la caida de cifra publicada que el "
    "acta de la vuelta 51 nombra en su seccion 3.1. La vara es el `D7` de la vuelta 50, "
    "escrito por esta misma sesion: quien corrige una celda con contador CUADRA EL "
    "CONTADOR y ADOSA la nota fechada. Ninguna nota vieja se reescribe: estan fechadas y "
    "se quedan"
)

CAMBIOS = [
    # ---------------- 1.1, los tres contadores ----------------
    (REC, "1.1 fila 246, A crudas",
     "**[CORREGIDA SIETE VECES, el 15 y el 18 ago 2026 y el 19 ago 2026; la SEPTIMA al CIERRE",
     "**[CORREGIDA ~~SIETE~~ OCHO VECES, el 15 y el 18 ago 2026 y el 19 ago 2026; la SEPTIMA al CIERRE"),
    (REC, "1.1 fila 246, nota adosada",
     "(`../loop/SALIDA_V50_RECOMPUTO_APERTURA.txt`, paso 1)]**",
     "(`../loop/SALIDA_V50_RECOMPUTO_APERTURA.txt`, paso 1)] "
     "[CONTADOR CUADRADO Y NOTA ADOSADA, 20 ago 2026 (vuelta 52, TAREA 1.1): la cadena de esta "
     "celda lleva OCHO cifras tachadas y el contador decia SIETE. " + NOTA_COMUN +
     ". La octava cifra, de 571 a 566, esta medida en `../loop/SALIDA_V51_RECOMPUTO_CIERRE.txt`, "
     "paso 1, y reproducida hoy en `../loop/SALIDA_V52_RECOMPUTO_APERTURA.txt`, paso 1]**"),

    (REC, "1.1 fila 247, colapsos",
     "**[CORREGIDA CUATRO VECES, el 15 ago 2026 y el 19 ago 2026 (vueltas 49 y 50).",
     "**[CORREGIDA ~~CUATRO~~ CINCO VECES, el 15 ago 2026 y el 19 ago 2026 (vueltas 49 y 50)."),
    (REC, "1.1 fila 247, nota adosada",
     "las 48 estan impresas una a una por el instrumento en `../loop/SALIDA_V50_RECOMPUTO_APERTURA.txt`]**",
     "las 48 estan impresas una a una por el instrumento en `../loop/SALIDA_V50_RECOMPUTO_APERTURA.txt`] "
     "[CONTADOR CUADRADO Y NOTA ADOSADA, 20 ago 2026 (vuelta 52, TAREA 1.1): la cadena de esta "
     "celda lleva CINCO cifras tachadas y el contador decia CUATRO. La QUINTA es la del CIERRE "
     "DE LA VUELTA 51, la misma cirugia que la fila de arriba (cuatro actos fundidos y los cinco "
     "volteos `P.16` de los puestos 820, 2426, 2523, 2662 y 498), y sube el colapso de 49 a 57 "
     "porque cada acto fundido convierte sus pares `A` internos en pares cuyos dos ids resuelven "
     "al mismo nodo vivo. Aquel barrido MOVIO LA CIFRA Y NO CUADRO EL CONTADOR (acta de la vuelta "
     "51, seccion 3.1). Medido en `../loop/SALIDA_V51_RECOMPUTO_CIERRE.txt`, paso 1, y reproducido "
     "hoy en `../loop/SALIDA_V52_RECOMPUTO_APERTURA.txt`, paso 1. Ninguna nota vieja se reescribe]**"),

    (REC, "1.1 fila 248, pares distintos",
     "**[CORREGIDA SIETE VECES, las dos ultimas el 19 ago 2026 (vuelta 50,",
     "**[CORREGIDA ~~SIETE~~ OCHO VECES, las dos ultimas el 19 ago 2026 (vuelta 50,"),
    (REC, "1.1 fila 248, nota adosada",
     "por el mismo motivo que las dos filas de arriba]**",
     "por el mismo motivo que las dos filas de arriba] "
     "[CONTADOR CUADRADO Y NOTA ADOSADA, 20 ago 2026 (vuelta 52, TAREA 1.1): la cadena de esta "
     "celda lleva OCHO cifras tachadas y el contador decia SIETE. " + NOTA_COMUN +
     ". La octava cifra, de 522 a 509, es la resta exacta de las dos filas de arriba (566 crudas "
     "menos 57 colapsos) y esta medida en `../loop/SALIDA_V51_RECOMPUTO_CIERRE.txt`, paso 1, y "
     "reproducida hoy en `../loop/SALIDA_V52_RECOMPUTO_APERTURA.txt`, paso 1]**"),

    # ---------------- 1.2, los cinco ordinales y el rotulo de las 51 ----------------
    (FUS, "1.2 los cinco declarados, ordinales",
     "**Al cerrar la vuelta 51 son los actos 4, 21, 23, 27 y 28**",
     "**Al cerrar la vuelta 51 son los actos ~~4, 21, 23, 27 y 28~~ 3, 19, 21, 25 y 26**"),
    (FUS, "1.2 los cinco declarados, nota",
     "fechado a su corrida desde el principio, que es lo que el acta 50 adjudico en su pregunta 5).",
     "fechado a su corrida desde el principio, que es lo que el acta 50 adjudico en su pregunta 5).\n"
     "\n"
     "> **CORRECCION DECLARADA (20 ago 2026, vuelta 52, TAREA 1.2), y el texto viejo se queda "
     "tachado delante: LOS CINCO ORDINALES NACIERON MAL, no envejecieron.** El rotulo de la celda "
     "estaba bien fechado y la salida citada era la correcta; **las cifras venian de OTRA corrida**, "
     "la de TRAS EL LOTE A ([`../loop/SALIDA_V51_TRAMO1_TRAS_LOTE_A.txt`](../loop/SALIDA_V51_TRAMO1_TRAS_LOTE_A.txt), "
     "que imprime 4, 21, 23, 27 y 28 porque el lote B todavia no habia consumido dos actos mas). "
     "**La salida que la propia celda cita imprime 3, 19, 21, 25 y 26** "
     "([`../loop/SALIDA_V51_TRAMO1_CIERRE.txt`](../loop/SALIDA_V51_TRAMO1_CIERRE.txt), bloque "
     "*actos de FUSION PURA vivos*). Es la caida de cifra publicada que el acta de la vuelta 51 "
     "nombra en su seccion 3.2. **Al abrir la vuelta 52 los cinco siguen en 3, 19, 21, 25 y 26**, "
     "re-medidos hoy ([`../loop/SALIDA_V52_TRAMO1_APERTURA.txt`](../loop/SALIDA_V52_TRAMO1_APERTURA.txt)), "
     "y la coincidencia no es la fuente de la correccion sino su contraste: entre el cierre de la 51 "
     "y la apertura de la 52 no se fundio ningun acto."),

    (FUS, "1.2 el rotulo de las 51 combinaciones",
     "mapa de alias y re-resolver LOS 3.388 VEREDICTOS**, y las 25 combinaciones de acto y\n"
     "superviviente viable se re-midieron con la aritmetica buena",
     "mapa de alias y re-resolver LOS 3.388 VEREDICTOS**, y las ~~25~~ **51** combinaciones de acto y\n"
     "superviviente viable **de los 25 actos mixtos** se re-midieron con la aritmetica buena"),
    (FUS, "1.2 el rotulo de las 51, nota",
     "**De 51 combinaciones, CINCO no calzan con la cuenta del encargo.**",
     "**De 51 combinaciones, CINCO no calzan con la cuenta del encargo.**\n"
     "\n"
     "> **CORRECCION DE ROTULO DECLARADA (20 ago 2026, vuelta 52, TAREA 1.2; acta de la vuelta 51, "
     "seccion 3.4), y el 25 se queda tachado delante:** lo que se re-midio fueron **51 combinaciones "
     "de acto y superviviente viable**, no 25. **El 25 es la cuenta de los ACTOS MIXTOS** que habia "
     "entonces, y la frase de al lado ya publicaba el 51, asi que la pagina se contradecia consigo "
     "misma a dos lineas de distancia. La cifra buena la imprime el propio instrumento citado "
     "([`../loop/SALIDA_V51_COLISIONES_ESPERADAS.txt`](../loop/SALIDA_V51_COLISIONES_ESPERADAS.txt)). "
     "**No es una cifra mal medida: es un nombre mal puesto a una cifra bien medida**, y por eso el "
     "tratamiento es el del rotulo y no el de la cifra."),

    # ---------------- 1.3, el rotulo hoy del registro de la vuelta 49 ----------------
    (FUS, "1.3 el rotulo hoy de la vuelta 49",
     "| los declarados **29**, **32** y **36** (hoy **26**, **28** y **32**) | **siguen declarados**, ninguno se toca |",
     "| los declarados **29**, **32** y **36** (~~hoy~~ **26**, **28** y **32** AL ABRIR LA VUELTA 49) "
     "**[ROTULO FECHADO, 20 ago 2026 (vuelta 52, TAREA 1.3), CIFRAS INTACTAS: el 26/28/32 es exacto "
     "para la corrida de la APERTURA de la vuelta 49 y lo que envejecio es la palabra *hoy*. "
     "Re-medido esta vuelta con `python scripts/loop/vuelta50_tramo_por_miembros.py` contra las tres "
     "nominas selladas: al ABRIR la vuelta 49 son 26, 28 y 32 "
     "(`../loop/SALIDA_V52_TRAMO1_EN_APERTURA_V49.txt`, sobre `RECOMPUTO_V48_CIERRE.jsonl`, 254 "
     "CERRADOS); al CERRARLA ya eran 24, 26 y 30 (`../loop/SALIDA_V52_TRAMO1_EN_CIERRE_V49.txt`, "
     "sobre `RECOMPUTO_V49_CIERRE.jsonl`, 252 CERRADOS); y al ABRIR la vuelta 51 eran 23, 25 y 29 "
     "(`../loop/SALIDA_V52_TRAMO1_EN_APERTURA_V51.txt`, sobre `RECOMPUTO_V51_APERTURA.jsonl`, 251 "
     "CERRADOS). Es la misma especie que la TAREA 1.2 de la vuelta 51 corrigio en el registro de la "
     "vuelta 50, y el acta de la vuelta 51 la adjudico en su `D10`. Los tres son numeros del TRAMO "
     "(29, 32 y 36), que no bailan; lo que baila es el ordinal de la nomina del dia]** "
     "| **siguen declarados**, ninguno se toca |"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("LAS CORRECCIONES DE LA TAREA 1 DE LA VUELTA 52 (1.1, 1.2 y 1.3)")
    print("modo: %s" % ("SIMULACION, no escribe" if a.simular else "ESCRITURA"))
    print("=" * 78)
    print()

    textos = {}
    hechas = saltadas = 0
    for ruta, etiqueta, viejo, nuevo in CAMBIOS:
        if ruta not in textos:
            textos[ruta] = io.open(ruta, encoding="utf-8").read()
        t = textos[ruta]
        if nuevo in t:
            print("  YA ESTABA   %-44s (idempotente)" % etiqueta)
            saltadas += 1
            continue
        c = t.count(viejo)
        if c != 1:
            print("  ROJO        %-44s el texto viejo aparece %d veces" % (etiqueta, c))
            return 1
        textos[ruta] = t.replace(viejo, nuevo, 1)
        print("  HECHA       %-44s %s" % (etiqueta, os.path.basename(ruta)))
        hechas += 1

    if not a.simular:
        for ruta, t in textos.items():
            io.open(ruta, "w", encoding="utf-8", newline="\n").write(t)

    print()
    print("  sustituciones HECHAS: %d | ya estaban: %d" % (hechas, saltadas))
    print("  ficheros: %s" % ", ".join(sorted(os.path.basename(r) for r in textos)))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
