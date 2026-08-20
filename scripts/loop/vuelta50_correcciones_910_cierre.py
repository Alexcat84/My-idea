# -*- coding: utf-8 -*-
"""vuelta50_correcciones_910_cierre.py . EL SEGUNDO BARRIDO DE LA VUELTA 50, EL
DEL CIERRE, QUE ES EL QUE LA VUELTA 49 NO CORRIO.

POR QUE EXISTE, y es la regla del aviso aplicada a mi mismo: la TAREA 1.1 de esta
vuelta corrigio siete celdas con el marcador y el retrato de ESE momento
(A 573, D 2.730, colapsos 48, pares 525). DESPUES, en la TAREA 2, la fusion del
acto 1 y la limpieza `P.16` de las dos colisiones que fabrico MOVIERON otra vez el
marcador y el retrato. Dejar aquellas celdas como estaban seria repetir, dentro
de la misma vuelta, exactamente la caida que esta vuelta vino a corregir.

LA REGLA, adjudicada por el auditor (acta de la vuelta 49, seccion 5, pregunta 5,
por extension del banco `9.10`): QUIEN MUEVE UNA CLASE O FUNDE UN ACTO CORRE EL
BARRIDO ANTES DE CERRAR LA VUELTA, sobre toda tabla vigente que cite la clase, el
marcador o el retrato.

DE DONDE SALEN ESTAS CORRECCIONES: del barrido del CIERRE
(docs/loop/SALIDA_V50_BARRIDO_910_CIERRE.txt), corrido DESPUES del ultimo
movimiento de la vuelta con el sucesor scripts/loop/vuelta50_barrido_910.py y con
las cifras de la TAREA 1.1 como VIEJAS. Las cifras nuevas salen de los dos
instrumentos re-corridos al cierre y de ningun otro sitio:
  docs/loop/SALIDA_V50_MARCADOR_CIERRE.txt   (A 571, B 77, C 8, D 2.732)
  docs/loop/SALIDA_V50_RECOMPUTO_CIERRE.txt  (49 colapsos, 522 pares, ii 522=522)

UNA CELDA QUE NO SE REESCRIBE Y SE DICE POR QUE: la tabla de la TAREA 1.1 en
docs/plan/03_FUSIONES.md registra QUE corrigio aquella operacion y con que cifra.
Esa cifra fue exacta cuando se escribio. Reescribirla fabricaria una corrida que
nunca existio, que es lo que la vara de separacion prohibe. Lo que SI se corrige
es su ENCABEZADO, que decia "hoy, medido en esta vuelta" y por tanto se presentaba
como vigente, y se le adosa el aviso del segundo movimiento con las cifras del
cierre.

MODOS: --simular (por defecto) y --ejecutar. Contrato heredado: sustitucion
literal y unica; si el texto viejo no aparece EXACTAMENTE una vez, aborta.

Uso: python scripts/loop/vuelta50_correcciones_910_cierre.py [--ejecutar]
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:49 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 49 DEL AUDITOR" corte=2026-08-20 motivo="nombra a la vuelta 49 como la que no corrio este barrido, que es su motivo de existir"
import argparse
import io
import sys

FECHA = "19 ago 2026 (vuelta 50, barrido del CIERRE)"

CORRECCIONES = [

    # ---------- 1. EL RETRATO DE LAS A, filas 246, 247 y 248 ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "| A crudas en el archivo (`clase == 'A'`), corte 3.388 | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ **573**",
     "| A crudas en el archivo (`clase == 'A'`), corte 3.388 | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ ~~**573**~~ **571**",
     "Fila 246. La corrigio la TAREA 1.1 de esta misma vuelta a 573 y la TAREA 2 la volvio a mover: la fusion del acto 1 fabrico dos colisiones y la limpieza P.16 volteo los puestos 2222 y 2226 de A a D. Medido al CIERRE."),

    ("docs/plan/RECOMPUTO_3388.md",
     "(mismo nodo vivo en los dos lados) | ~~**0**~~ ~~**1**~~ ~~**41**~~ **48**",
     "(mismo nodo vivo en los dos lados) | ~~**0**~~ ~~**1**~~ ~~**41**~~ ~~**48**~~ **49**",
     "Fila 247. La fusion del acto 1 anade UN colapso mas: el puesto 2237 (drift_hacia_el_fallo_2 contra normalizacion_de_la_desviacion) resuelve hoy al mismo nodo vivo en los dos lados. Es la huella de la cirugia de esta vuelta, la misma especie que la fila ya explica."),

    ("docs/plan/RECOMPUTO_3388.md",
     "| pares distintos en el retrato tras resolver y deduplicar | ~~**583**~~ ~~**582**~~ ~~**580**~~ ~~**575**~~ ~~**574**~~ ~~**533**~~ **525**",
     "| pares distintos en el retrato tras resolver y deduplicar | ~~**583**~~ ~~**582**~~ ~~**580**~~ ~~**575**~~ ~~**574**~~ ~~**533**~~ ~~**525**~~ **522**",
     "Fila 248. Baja en tres: dos por los volteos de P.16 (2222 y 2226 dejan de ser A) y uno por el colapso a auto-arista del 2237."),

    # ---------- 2. LA COMPROBACION ii, fila 528 ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "y **RE-CORRIDO OTRA VEZ EL 19 ago 2026 (vuelta 50) CON LA PAREJA NUEVA: sigue OK con 525 y 525**, y con el las otras tres ([`../loop/SALIDA_V50_RECOMPUTO_APERTURA.txt`](../loop/SALIDA_V50_RECOMPUTO_APERTURA.txt), *LAS CUATRO: TODAS OK*).",
     "~~y **RE-CORRIDO OTRA VEZ EL 19 ago 2026 (vuelta 50) CON LA PAREJA NUEVA: sigue OK con 525 y 525**~~ y **RE-CORRIDO POR TERCERA VEZ AL CIERRE DE LA VUELTA 50, DESPUES DE FUNDIR: sigue OK con 522 y 522**, y con el las otras tres ([`../loop/SALIDA_V50_RECOMPUTO_CIERRE.txt`](../loop/SALIDA_V50_RECOMPUTO_CIERRE.txt), *LAS CUATRO: TODAS OK*). **La pareja de la apertura de la vuelta 50 se tacha por el mismo motivo que la de la 49: era cierta al medirla y la propia vuelta la movio despues.**",
     "Fila 528. El checkpoint se presenta como vigente y lo mueve toda fusion y todo volteo de A. Re-corrido AL CIERRE, que es cuando la regla del aviso manda correrlo."),

    # ---------- 3. LA TABLA POR DOMINIO, fila 1079 ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "| **total** | **3.388** | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ **573** |",
     "| **total** | **3.388** | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ ~~**573**~~ **571** |",
     "Fila 1079. Los dos volteos de P.16 son los dos de `health_safety`, y por primera vez en esta cadena el dominio que cambia NO es `core`: se dice porque la nota de la tabla venia diciendo lo contrario tres correcciones seguidas."),

    # ---------- 4. LA NOTA DE core, que esta vez no basta ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "queda en `n 1.445, A 334 (23,1 por ciento)`. Los otros nueve dominios, identicos al digito.\n"
     "LA FILA `core` DE LA TABLA DE ARRIBA SIGUE DICIENDO 344 Y NO SE REESCRIBE, por el mismo motivo\n"
     "que la segunda correccion ya escribio: es la foto del 13 ago.**",

     "queda en `n 1.445, A 334 (23,1 por ciento)`. Los otros nueve dominios, identicos al digito.\n"
     "LA FILA `core` DE LA TABLA DE ARRIBA SIGUE DICIENDO 344 Y NO SE REESCRIBE, por el mismo motivo\n"
     "que la segunda correccion ya escribio: es la foto del 13 ago.** **QUINTA CORRECCION DECLARADA\n"
     "(19 ago 2026, al CIERRE de la vuelta 50, y ROMPE EL PATRON DE LAS CUATRO ANTERIORES): el total\n"
     "es hoy `A 571, B 77, C 8, D 2.732`, y el dominio que cambia YA NO ES `core`. Los dos volteos de\n"
     "la limpieza `P.16` de esta vuelta (los puestos **2222** y **2226**, de `A` a `D`) son los dos de\n"
     "`health_safety`, que pasa de `A 45` a `A 43` sobre sus 192 pares, de 23,4 a 22,4 por ciento;\n"
     "`core` se queda quieto en `A 334`. Medido al cierre dominio por dominio\n"
     "(`../loop/SALIDA_V50_MARCADOR_CIERRE.txt`). **Las cuatro correcciones anteriores decian que el\n"
     "unico dominio que se movia era `core`; esa frase era cierta cada vez que se escribio y hoy deja\n"
     "de serlo, y se dice en vez de dejar que el lector la extienda.**",

     "La cadena de correcciones declaradas venia afirmando cuatro veces seguidas que el unico dominio que se mueve es `core`. Esta vuelta lo desmiente y la afirmacion es de las que un lector extiende sin darse cuenta."),

    # ---------- 5. EL MARCADOR DEL APENDICE 100.1 ----------
    ("docs/INTRA_DOMINIO_INFORME.md",
     "| **A** | ~~**583** (17,2 %)~~ ~~582~~ ~~581~~ ~~576~~ ~~575 (17,0 %)~~ ~~574~~ **573** (16,9 %), ver las correcciones declaradas debajo |",
     "| **A** | ~~**583** (17,2 %)~~ ~~582~~ ~~581~~ ~~576~~ ~~575 (17,0 %)~~ ~~574~~ ~~573~~ **571** (16,9 %), ver las correcciones declaradas debajo |",
     "Apendice 100.1, fila A. La TAREA 1.1 la puso en 573 y la TAREA 2 la movio a 571. El barrido del cierre la destapa, que es exactamente para lo que existe."),

    ("docs/INTRA_DOMINIO_INFORME.md",
     "~~2.726~~ ~~2.729~~ **2.730** (80,6 %) |",
     "~~2.726~~ ~~2.729~~ ~~2.730~~ **2.732** (80,6 %) |",
     "Apendice 100.1, fila D. Los dos volteos de P.16 suben D en dos."),

    ("docs/INTRA_DOMINIO_INFORME.md",
     "> (`../loop/SALIDA_V50_MARCADOR_APERTURA.txt`): **A 573, B 77, C 8, D 2.730** sobre `n`\n"
     "> **3.388**, cero huecos y cero duplicados.",

     "> (`../loop/SALIDA_V50_MARCADOR_APERTURA.txt`): **A 573, B 77, C 8, D 2.730** sobre `n`\n"
     "> **3.388**, cero huecos y cero duplicados.\n"
     "\n"
     "> **SEGUNDA CORRECCION DECLARADA DE LA VUELTA 50, Y ES LA MISMA TABLA OTRA VEZ, EL MISMO DIA,\n"
     "> A MANOS DE LA MISMA VUELTA.** La correccion de arriba se escribio con el marcador de la\n"
     "> TAREA 1.1. **Despues, en la TAREA 2, la fusion del acto 1 de `OP-U-01` fabrico dos colisiones\n"
     "> de clase y la limpieza `P.16` volteo los puestos 2222 y 2226 de `A` a `D`.** Esta vez la tabla\n"
     "> SI se barrio antes de cerrar, que es la regla que la vuelta 49 dejo adjudicada y no cumplio:\n"
     "> **quien mueve una clase o funde un acto corre el barrido `9.10` ANTES de cerrar la vuelta.**\n"
     "> **Las dos cifras intermedias del mismo dia van tachadas y no borradas**, porque cada una fue\n"
     "> exacta en su momento y taparlas volveria inauditable el orden de las operaciones. Medido al\n"
     "> cierre con `python scripts/recomputar_marcador.py 3388`\n"
     "> (`../loop/SALIDA_V50_MARCADOR_CIERRE.txt`): **A 571, B 77, C 8, D 2.732** sobre `n` **3.388**,\n"
     "> cero huecos y cero duplicados.",

     "La nota de correccion de la TAREA 1.1 cita su propia medicion fechada y por eso NO se reescribe: se le adosa la segunda, con las dos cifras del mismo dia tachadas en cadena."),

    # ---------- 6. EL ENCABEZADO DE LA TABLA DE LA TAREA 1.1 EN 03_FUSIONES ----------
    ("docs/plan/03_FUSIONES.md",
     "| la celda | decia | **hoy, medido en esta vuelta** | el instrumento |",
     "| la celda | decia | **al corregirla en la TAREA 1.1** | el instrumento |",
     "La columna se titulaba `hoy, medido en esta vuelta` y por tanto se presentaba como VIGENTE. La propia vuelta movio esas cifras despues, en la TAREA 2. La cifra de la columna NO se toca (fue exacta al escribirse y reescribirla fabricaria una corrida que nunca existio): lo que se corrige es el titulo que la presentaba como el estado de ahora."),
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
            continue
        if veces != 1:
            print("    ROJO: tiene que aparecer EXACTAMENTE UNA VEZ. No se escribe nada.")
            fallos += 1
            continue
        planes.append((fich, viejo, nuevo))
        print("    OK, lista para aplicar (%d a %d caracteres)" % (len(viejo), len(nuevo)))
        print()

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
