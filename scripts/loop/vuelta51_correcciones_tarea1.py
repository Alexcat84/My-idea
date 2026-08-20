# -*- coding: utf-8 -*-
"""vuelta51_correcciones_tarea1.py . LAS TRES CORRECCIONES ADJUDICADAS DE LA
TAREA 1 DE LA VUELTA 51, cada una con su especie declarada.

POR QUE EXISTE: el acta de la vuelta 50 del auditor deja tres encargos de
correccion, y los tres son de especie distinta. La regla que los separa es la
adjudicada en la pregunta 5 de esa misma acta: si lo que envejecio es la CIFRA
de una tabla vigente de estado, se corrige la cifra con tachado por 9.10; si la
cifra fue EXACTA para su corrida y lo que envejecio es el ROTULO deictico
("hoy"), se corrige el rotulo fechandolo a su corrida y la cifra se queda.

  1.1  CIFRA EQUIVOCADA (acta 50, seccion 3.3 y pregunta 4). La fila "lecturas
       P.12 encargadas y NO hechas: 25" del registro de la vuelta 49 no
       envejecio: nacio mal. La cuenta buena al cierre de la 49 era 26. Se
       corrige LA CIFRA con tachado, fecha y motivo.
  1.2  ROTULO ENVEJECIDO (acta 50, seccion 3.1). La columna "numero en la
       vuelta 48 / hoy" de la tabla de los cinco declarados trae los numeros de
       la APERTURA de la vuelta 50 (7, 24, 26, 30, 31) y el cierre de esa misma
       vuelta los re-midio distintos (6, 23, 25, 29, 30). Las CIFRAS fueron
       exactas para su corrida: se corrige el ROTULO. Misma vara para la linea
       del "hoy el acto 156" de los imposibles, que era el numero de la
       apertura de la vuelta 50 y hoy es el 155.
  1.3  CORRECCION INCOMPLETA DE FORMA (acta 50, seccion 3.2). La celda del
       checkpoint ii de la fila 528 de RECOMPUTO_3388.md conserva "525" sin
       tachar en sus DOS parentesis mientras su propia nota vigente publica
       522 y 522. No es cifra nueva: es completar un tachado que quedo a
       medias. La vara es el tratamiento que la vuelta 50 dio a las filas 246
       y 248 de la misma pagina.

DE DONDE SALEN LAS CIFRAS QUE ESTA CORRECCION CITA, todas de instrumento y
ninguna de acta:
  ../loop/SALIDA_V50_TRAMO1_POR_MIEMBROS.txt   apertura de la vuelta 50: 7, 24, 26, 30, 31
  ../loop/SALIDA_V50_TRAMO1_CIERRE.txt         cierre de la vuelta 50   : 6, 23, 25, 29, 30
  ../loop/SALIDA_V51_TRAMO1_APERTURA.txt       apertura de la vuelta 51 : 6, 23, 25, 29, 30
  ../loop/SALIDA_V50_PUERTAS_EN_EL_LOTE.txt    imposible dos, apertura de la 50: acto 156
  ../loop/SALIDA_V51_PUERTAS_APERTURA.txt      imposible dos, apertura de la 51: acto 155
  ../loop/SALIDA_V51_RECOMPUTO_APERTURA.txt    checkpoint ii vigente: 522 igual a 522

MODOS: --simular (por defecto) y --ejecutar. Contrato heredado del instrumento
de la vuelta 50: sustitucion literal y unica; si el texto viejo no aparece
EXACTAMENTE una vez, aborta sin escribir nada.

Uso: python scripts/loop/vuelta51_correcciones_tarea1.py [--ejecutar]
"""
import argparse
import io
import sys

FECHA = "20 ago 2026 (vuelta 51, TAREA 1)"

CORRECCIONES = [

    # ---------- 1.1 LA CIFRA EQUIVOCADA DEL REGISTRO DE LA VUELTA 49 ----------
    ("docs/plan/03_FUSIONES.md",
     "| lecturas `P.12` **encargadas y NO hechas** | **25** |",

     # UNA SOLA LINEA A PROPOSITO: es una celda de tabla markdown, y partirla en
     # varias lineas rompe la fila. Es la misma forma que tienen las celdas
     # corregidas de RECOMPUTO_3388.md (filas 246, 247 y 248). La primera
     # version de este instrumento la partio en diez lineas y rompio la tabla;
     # se corrigio dentro de la misma vuelta y queda dicho aqui.
     "| lecturas `P.12` **encargadas y NO hechas** | ~~**25**~~ **26** **[CORREGIDA UNA VEZ, el 20 ago 2026 (vuelta 51, TAREA 1.1). NO ES UNA CIFRA QUE ENVEJECIO: NACIO MAL. La cuenta buena al cierre de la vuelta 49 era 26, medida por miembros sobre la nomina de aquel estado (`../loop/SALIDA_V50_TRAMO1_POR_MIEMBROS.txt`, corrida al abrir la vuelta 50 sobre el hash `b8d1083a`, que es el cierre de la 49) y re-derivada por el auditor en el acta de la vuelta 50, seccion 3.3, que es su relectura conjunta: 25 mixtos al cierre de la vuelta 50 mas el acto 1 que esa vuelta resolvio. LA FILA HERMANA del registro de la vuelta 50, que dice 25 al cierre, esta bien medida y NO se toca. El 25 de aqui convivia en esta misma pagina con el 26 de la medicion de la forma, dos parrafos mas arriba]** |",

     "Fila del registro de la vuelta 49. Cifra publicada equivocada DE AQUELLA vuelta, adjudicada en el acta 50 (seccion 3.3 y pregunta 4). Se corrige con tachado, fecha y motivo, y con la salida que la mide citada."),

    # ---------- 1.2a EL ROTULO DE LA COLUMNA DE LOS CINCO DECLARADOS ----------
    ("docs/plan/03_FUSIONES.md",
     "| los miembros | por que sigue declarado | numero en la vuelta 48 / **hoy** |",

     "| los miembros | por que sigue declarado | numero en la vuelta 48 / ~~**hoy**~~ **AL ABRIR LA VUELTA 50** |",

     "Tabla de los cinco declarados del registro de la vuelta 50. El rotulo `hoy` era deictico y envejecio dentro de la propia vuelta. Las CIFRAS de la columna NO se tocan: fueron exactas para la corrida que la celda cita."),

    # ---------- 1.2b LA NOTA DEL ROTULO Y EL "hoy el acto 156" ----------
    ("docs/plan/03_FUSIONES.md",
     "**Los dos IMPOSIBLES por puerta re-medidos hoy sobre la nomina de hoy son el `domina_lo_que_compras`\n"
     "y `licenciamiento_tecnologico` contra `proteccion_propiedad_intelectual_internacional`** (hoy el\n"
     "acto **156**), **y el segundo cae FUERA del tramo 1**, que es exactamente lo que decia el registro\n"
     "de la vuelta 48 con la numeracion de aquel dia.",

     "> **CORRECCION DECLARADA DE ROTULO (20 ago 2026, vuelta 51, TAREA 1.2), adjudicada en el acta de\n"
     "> la vuelta 50, seccion 3.1, con la figura del discutible D6 de la propia vuelta 50.** La columna\n"
     "> de arriba se titulaba **`hoy`** y traia los numeros de la corrida de APERTURA de la vuelta 50\n"
     "> (**7, 24, 26, 30, 31**,\n"
     "> [`../loop/SALIDA_V50_TRAMO1_POR_MIEMBROS.txt`](../loop/SALIDA_V50_TRAMO1_POR_MIEMBROS.txt)).\n"
     "> **El cierre de esa MISMA vuelta los re-midio distintos: 6, 23, 25, 29 y 30**\n"
     "> ([`../loop/SALIDA_V50_TRAMO1_CIERRE.txt`](../loop/SALIDA_V50_TRAMO1_CIERRE.txt)), porque la\n"
     "> fusion del acto 1 borro un acto de la nomina y corrio todos los numeros de detras. **Las cifras\n"
     "> NO se reescriben: fueron exactas para la corrida que la celda cita, y reescribirlas fabricaria\n"
     "> una corrida que nunca existio.** Lo que se corrige es el ROTULO, fechado a su corrida. **Los\n"
     "> mismos cinco actos re-medidos al abrir la vuelta 51 siguen en 6, 23, 25, 29 y 30**\n"
     "> ([`../loop/SALIDA_V51_TRAMO1_APERTURA.txt`](../loop/SALIDA_V51_TRAMO1_APERTURA.txt)). **Y la\n"
     "> propia tabla ya avisaba de que el numero no se usa: la llave son los miembros.**\n"
     "\n"
     "**Los dos IMPOSIBLES por puerta re-medidos sobre la nomina de la APERTURA DE LA VUELTA 50 son el\n"
     "`domina_lo_que_compras` y `licenciamiento_tecnologico` contra\n"
     "`proteccion_propiedad_intelectual_internacional`** (~~hoy el acto **156**~~ **el acto 156 en\n"
     "aquella corrida**, [`../loop/SALIDA_V50_PUERTAS_EN_EL_LOTE.txt`](../loop/SALIDA_V50_PUERTAS_EN_EL_LOTE.txt);\n"
     "**al abrir la vuelta 51 es el acto 155**,\n"
     "[`../loop/SALIDA_V51_PUERTAS_APERTURA.txt`](../loop/SALIDA_V51_PUERTAS_APERTURA.txt)), **y el\n"
     "segundo cae FUERA del tramo 1**, que es exactamente lo que decia el registro de la vuelta 48 con\n"
     "la numeracion de aquel dia. **Rotulo corregido con la misma vara el 20 ago 2026 (vuelta 51,\n"
     "TAREA 1.2): el ordinal era el de la apertura de la vuelta 50 y se presentaba como el de hoy. Los\n"
     "DOS imposibles siguen siendo los mismos DOS por miembros, que es la llave que no baila.**",

     "La linea del `hoy el acto 156` de los imposibles es la misma especie que el rotulo de la columna: el ordinal era el de la apertura de la vuelta 50 y hoy es el 155. Se fecha a su corrida y se anade la medicion de hoy al lado, sin tocar la cifra vieja."),

    # ---------- 1.3 EL PARENTESIS DE LA FILA 528 ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "A vigentes resueltas del retrato (~~583~~ ~~582~~ ~~580~~ ~~533~~ **525**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ ~~580~~ ~~533~~ **525**)",

     "A vigentes resueltas del retrato (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ **522**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ ~~580~~ ~~533~~ ~~525~~ **522**)",

     "Fila 528, checkpoint ii. La celda mostraba 525 SIN tachar en sus dos parentesis mientras su propia nota vigente, fechada al cierre de la vuelta 50, publica 522 y 522. Correccion INCOMPLETA DE FORMA, adjudicada en el acta 50 seccion 3.2, y no cifra nueva: la pareja 522 igual a 522 se re-corrio al abrir la vuelta 51 y sigue OK. La cadena de notas NO se toca."),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("LAS TRES CORRECCIONES ADJUDICADAS DE LA TAREA 1, %s" % FECHA)
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
