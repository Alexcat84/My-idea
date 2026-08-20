# -*- coding: utf-8 -*-
"""vuelta51_correcciones_910.py . EL BARRIDO 9.10 DEL CIERRE DE LA VUELTA 51,
CORRIDO DESPUES DEL ULTIMO MOVIMIENTO.

LA REGLA QUE LO OBLIGA, adjudicada por el auditor (acta de la vuelta 49, seccion
5, pregunta 5, por extension del banco 9.10) y repetida en el aviso del encargo
de esta vuelta: QUIEN MUEVE UNA CLASE O FUNDE UN ACTO CORRE EL BARRIDO ANTES DE
CERRAR LA VUELTA, sobre toda tabla vigente que cite la clase, el marcador o el
retrato.

QUE MOVIO ESTA VUELTA: cuatro actos fundidos (siete nodos absorbidos) y CINCO
veredictos volteados de `A` a `D` por `P.16` (puestos 820, 2426, 2523, 2662 y
498). El marcador paso de `A 571, B 77, C 8, D 2.732` a `A 566, B 77, C 8,
D 2.737` y el retrato de `571 / 49 / 522` a `566 / 57 / 509`.

DE DONDE SALEN LAS CIFRAS NUEVAS, todas de instrumento corrido AL CIERRE y de
ningun acta ni reporte:
  docs/loop/SALIDA_V51_MARCADOR_CIERRE.txt   (A 566, B 77, C 8, D 2.737)
  docs/loop/SALIDA_V51_RECOMPUTO_CIERRE.txt  (566 crudas, 57 colapsos, 509 pares,
                                              checkpoint ii 509 igual a 509)
  docs/loop/SALIDA_V51_BARRIDO_910_CIERRE.txt (los candidatos, buscando el
                                              marcador viejo DE HOY y el retrato
                                              viejo DE HOY)

LO QUE ESTE INSTRUMENTO NO CORRIGE Y SE DICE EN VEZ DE CALLARSE: el barrido saco
DOS FAMILIAS MAS de candidatos que NO se tocan aqui porque piden adjudicacion y
no medicion, y las dos van al reporte con su cifra medida:
  1. el apendice 95.1 de docs/INTRA_DOMINIO_INFORME.md, MARCADOR (corte 2.900).
     Publica A 571, B 89, C 7, D 2.233. Medido hoy con
     `python scripts/recomputar_marcador.py 2900`: A 554, B 77, C 8, D 2.261.
     La duda no es la cifra: es si esa tabla es una FOTO FECHADA de la vuelta 4
     (y entonces la cadena de tachados que vueltas posteriores le fueron
     aplicando a la `A` y a la `D` sobraba) o una TABLA VIGENTE al corte 2.900
     (y entonces lleva tiempo derivando, porque se ha mantenido restando de la
     cifra anterior en vez de re-midiendo, y por eso la `B` y la `C` se quedaron
     en las de la vuelta 4).
  2. las dos tablas EL MARCADOR ... AL CERRAR LA VUELTA de
     docs/plan/RECOMPUTO_3388.md (lineas 1790 y 1837), que publican
     `575 / 83 / 8 / 2.722` bajo un encabezado que dice *medido hoy*. Misma
     duda y misma especie que el rotulo que la TAREA 1.2 de esta vuelta corrigio.

MODOS: --simular (por defecto) y --ejecutar. Contrato heredado: sustitucion
literal y unica; si el texto viejo no aparece EXACTAMENTE una vez, aborta.

Uso: python scripts/loop/vuelta51_correcciones_910.py [--ejecutar]
"""
import argparse
import io
import sys

FECHA = "20 ago 2026 (vuelta 51, barrido del CIERRE)"

MOTIVO = ("La vuelta 51 fundio CUATRO actos y volteo CINCO veredictos de A a D por P.16 "
          "(puestos 820, 2426, 2523, 2662 y 498). Medido al CIERRE, despues del ultimo "
          "movimiento.")

CORRECCIONES = [

    # ---------- RECOMPUTO_3388, fila 246: A crudas ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "| A crudas en el archivo (`clase == 'A'`), corte 3.388 | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ ~~**573**~~ **571**",
     "| A crudas en el archivo (`clase == 'A'`), corte 3.388 | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ ~~**573**~~ ~~**571**~~ **566**",
     "Fila 246. " + MOTIVO),

    # ---------- fila 247: colapsos a auto-arista ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "(mismo nodo vivo en los dos lados) | ~~**0**~~ ~~**1**~~ ~~**41**~~ ~~**48**~~ **49**",
     "(mismo nodo vivo en los dos lados) | ~~**0**~~ ~~**1**~~ ~~**41**~~ ~~**48**~~ ~~**49**~~ **57**",
     "Fila 247. Sube OCHO: los siete pares internos de los cuatro actos fundidos que ahora resuelven al mismo nodo vivo en los dos lados, mas el que arrastra el segundo absorbido de los actos de tres. Es la huella de la cirugia, la misma especie que la fila ya explica."),

    # ---------- fila 248: pares distintos ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "| pares distintos en el retrato tras resolver y deduplicar | ~~**583**~~ ~~**582**~~ ~~**580**~~ ~~**575**~~ ~~**574**~~ ~~**533**~~ ~~**525**~~ **522**",
     "| pares distintos en el retrato tras resolver y deduplicar | ~~**583**~~ ~~**582**~~ ~~**580**~~ ~~**575**~~ ~~**574**~~ ~~**533**~~ ~~**525**~~ ~~**522**~~ **509**",
     "Fila 248. Baja TRECE: cinco por los volteos de P.16 (los cinco dejan de ser A) y ocho por los colapsos a auto-arista de las cuatro fusiones."),

    # ---------- fila 528: el checkpoint ii ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "A vigentes resueltas del retrato (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ **522**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ **522**)",
     "A vigentes resueltas del retrato (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ **509**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ ~~522~~ **509**)",
     "Fila 528, la pareja del checkpoint ii. La TAREA 1.3 de esta misma vuelta completo el tachado del 525 que habia quedado a medias, y la TAREA 2 movio la pareja otra vez. Re-corrido al cierre: sigue OK con 509 y 509."),

    ("docs/plan/RECOMPUTO_3388.md",
     "y **RE-CORRIDO POR TERCERA VEZ AL CIERRE DE LA VUELTA 50, DESPUES DE FUNDIR: sigue OK con 522 y 522**",
     "~~y **RE-CORRIDO POR TERCERA VEZ AL CIERRE DE LA VUELTA 50, DESPUES DE FUNDIR: sigue OK con 522 y 522**~~ y **RE-CORRIDO POR CUARTA VEZ AL CIERRE DE LA VUELTA 51, DESPUES DE FUNDIR CUATRO ACTOS Y VOLTEAR CINCO VEREDICTOS: sigue OK con 509 y 509** (`../loop/SALIDA_V51_RECOMPUTO_CIERRE.txt`, *LAS CUATRO: TODAS OK*)",
     "Fila 528, la cadena de notas. La pareja de la vuelta 50 se tacha por el mismo motivo que las anteriores: era cierta al medirla y otra vuelta la movio despues."),

    # ---------- fila 1079: el total de la tabla por dominio ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "| **total** | **3.388** | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ ~~**573**~~ **571** | ~~**17,2 %**~~ ~~**17,1 %**~~ ~~**17,0 %**~~ **16,9 %** |",
     "| **total** | **3.388** | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ ~~**573**~~ ~~**571**~~ **566** | ~~**17,2 %**~~ ~~**17,1 %**~~ ~~**17,0 %**~~ ~~**16,9 %**~~ **16,7 %** |",
     "Fila 1079. " + MOTIVO + " Y LOS DOMINIOS QUE SE MUEVEN SON DOS Y NINGUNO ES core POR SI SOLO: quality baja de A 126 a A 123 (14,9 a 14,6 por ciento) por los tres volteos de la accion correctiva y del consejo de calidad, y core baja de A 334 a A 332 (23,1 a 23,0) por los dos del scorecard y de los cofundadores."),

    # ---------- INFORME 100.1, fila A ----------
    ("docs/INTRA_DOMINIO_INFORME.md",
     "| **A** | ~~**583** (17,2 %)~~ ~~582~~ ~~581~~ ~~576~~ ~~575 (17,0 %)~~ ~~574~~ ~~573~~ **571** (16,9 %), ver las correcciones declaradas debajo |",
     "| **A** | ~~**583** (17,2 %)~~ ~~582~~ ~~581~~ ~~576~~ ~~575 (17,0 %)~~ ~~574~~ ~~573~~ ~~571 (16,9 %)~~ **566** (16,7 %), ver las correcciones declaradas debajo |",
     "Apendice 100.1, fila A. " + MOTIVO),

    # ---------- INFORME 100.1, fila D ----------
    ("docs/INTRA_DOMINIO_INFORME.md",
     "~~2.729~~ ~~2.730~~ **2.732** (80,6 %) |",
     "~~2.729~~ ~~2.730~~ ~~2.732~~ **2.737** (80,8 %) |",
     "Apendice 100.1, fila D. Los cinco volteos de P.16 suben D en cinco."),

    # ---------- INFORME 100.1, la nota ----------
    ("docs/INTRA_DOMINIO_INFORME.md",
     "> cierre con `python scripts/recomputar_marcador.py 3388`\n"
     "> (`../loop/SALIDA_V50_MARCADOR_CIERRE.txt`): **A 571, B 77, C 8, D 2.732** sobre `n` **3.388**,\n"
     "> cero huecos y cero duplicados.",

     "> cierre con `python scripts/recomputar_marcador.py 3388`\n"
     "> (`../loop/SALIDA_V50_MARCADOR_CIERRE.txt`): **A 571, B 77, C 8, D 2.732** sobre `n` **3.388**,\n"
     "> cero huecos y cero duplicados.\n"
     "\n"
     "> **CORRECCION DECLARADA DE LA VUELTA 51 (20 ago 2026), Y ESTA VEZ LA TABLA NO SE QUEDO ATRAS:\n"
     "> EL BARRIDO SE CORRIO AL CIERRE, DESPUES DEL ULTIMO MOVIMIENTO, QUE ES LO QUE LA REGLA PIDE.**\n"
     "> La vuelta 51 fundio **CUATRO** actos del tramo 1 de `OP-U-01` (la accion correctiva y el\n"
     "> scorecard en el lote A, el consejo de calidad y la relacion previa entre cofundadores en el\n"
     "> lote B) y volteo **CINCO** veredictos de `A` a `D` por la limpieza `P.16` de las colisiones\n"
     "> que esas mismas fusiones fabricaron: los puestos **820**, **2426**, **2523**, **2662** y\n"
     "> **498**. **Las cifras intermedias van tachadas y no borradas**, porque cada una fue exacta en\n"
     "> su momento. Medido al cierre con `python scripts/recomputar_marcador.py 3388`\n"
     "> (`../loop/SALIDA_V51_MARCADOR_CIERRE.txt`): **A 566, B 77, C 8, D 2.737** sobre `n` **3.388**,\n"
     "> cero huecos y cero duplicados. **Y LOS DOMINIOS QUE SE MUEVEN SON DOS: `quality` de `A 126` a\n"
     "> `A 123` y `core` de `A 334` a `A 332`.**",

     "Apendice 100.1, la nota. La correccion de la vuelta 50 cita su propia medicion fechada y por eso NO se reescribe: se le adosa la de la vuelta 51."),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("CORRECCIONES DEL BARRIDO 9.10, %s" % FECHA)
    print("modo: %s" % ("EJECUTAR" if args.ejecutar else "SIMULAR"))
    print("=" * 78)
    print()

    planes, fallos = [], 0
    for n, (fich, viejo, nuevo, motivo) in enumerate(CORRECCIONES, 1):
        texto = io.open(fich, encoding="utf-8").read()
        veces = texto.count(viejo)
        print("--- CORRECCION %d: %s" % (n, fich))
        print("    motivo: %s" % motivo)
        print("    apariciones del texto viejo: %d" % veces)
        if nuevo in texto:
            print("    YA APLICADA (idempotencia).")
            print()
            continue
        if veces != 1:
            print("    ROJO: tiene que aparecer EXACTAMENTE UNA VEZ. No se escribe nada.")
            fallos += 1
            print()
            continue
        planes.append((fich, viejo, nuevo))
        print("    OK, lista para aplicar (%d a %d caracteres)" % (len(viejo), len(nuevo)))
        print()

    sucios = [n for n, (_, _, nuevo, _) in enumerate(CORRECCIONES, 1)
              if u"—" in nuevo or u"–" in nuevo]
    if sucios:
        print("ROJO: guion largo o medio en los textos nuevos %s" % sucios)
        fallos += 1
    else:
        print("guiones largos y medios en los textos nuevos: CERO")

    if fallos:
        print()
        print("ABORTA: %d correccion(es) en rojo." % fallos)
        return 1
    if not args.ejecutar:
        print()
        print("SIMULACION: %d correccion(es) listas. Nada escrito." % len(planes))
        return 0

    porfich = {}
    for fich, viejo, nuevo in planes:
        porfich.setdefault(fich, []).append((viejo, nuevo))
    for fich, pares in porfich.items():
        texto = io.open(fich, encoding="utf-8").read()
        for viejo, nuevo in pares:
            if texto.count(viejo) != 1:
                print("ABORTA en escritura: %s ya no casa una sola vez." % fich)
                return 1
            texto = texto.replace(viejo, nuevo)
        io.open(fich, "w", encoding="utf-8", newline="").write(texto)
        print("ESCRITO: %s (%d correcciones)" % (fich, len(pares)))
    print()
    print("APLICADAS: %d" % len(planes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
