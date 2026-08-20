# -*- coding: utf-8 -*-
"""vuelta50_correcciones_910.py . APLICA LAS CORRECCIONES DEL BARRIDO 9.10 DE LA
VUELTA 50, cada una con su texto viejo TACHADO y no borrado.

SUCESOR DECLARADO de scripts/loop/vuelta49_correcciones_910.py, del que hereda el
contrato entero: EL BARRIDO LISTA, ESTE INSTRUMENTO ESCRIBE, Y LA ADJUDICACION ES
DE LECTURA. Cada correccion es una sustitucion LITERAL Y UNICA; si el texto viejo
no aparece EXACTAMENTE una vez, aborta sin escribir nada.

LA VARA DE SEPARACION, la misma y se repite para poder discutirla: se corrige lo
que se presenta como VIGENTE. NO se toca lo que se presenta como el estado de un
dia con su corte al lado (las filas de apertura y cierre de vueltas pasadas, las
salidas de instrumento, y las notas de correccion que citan su propia medicion
fechada), porque reescribir el estado de un dia es falsificarlo, no corregirlo.

DE DONDE SALEN ESTAS CINCO, y no de un acta: del barrido de HOY
(docs/loop/SALIDA_V50_BARRIDO_910_A.txt, familias 1 y RETRATO) corrido con el
sucesor scripts/loop/vuelta50_barrido_910.py, que a diferencia del anterior SI
busca las cifras que se le pasan. Las cifras nuevas salen de dos instrumentos
corridos en esta vuelta y de ningun otro sitio:
  python scripts/recomputar_marcador.py 3388
  python scripts/plan/recomputo_3388.py --salida docs/loop/RECOMPUTO_V50_*.jsonl

MODOS: --simular (por defecto) y --ejecutar.
Las cifras nuevas se pasan por linea de comandos para que este instrumento sirva
tambien al barrido DEL CIERRE de la vuelta, que es lo que la regla del aviso
exige: quien mueve una clase o funde un acto barre ANTES de cerrar.

Uso: python scripts/loop/vuelta50_correcciones_910.py [--ejecutar]
"""
import argparse
import io
import sys

FECHA = "19 ago 2026 (vuelta 50)"

# (fichero, texto viejo, texto nuevo, motivo)
CORRECCIONES = [

    # ---------- 1. EL RETRATO DE LAS A: LAS TRES FILAS 246, 247 y 248 ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "| A crudas en el archivo (`clase == 'A'`), corte 3.388 | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ **574** **[CORREGIDA CINCO VECES, el 15 y el 18 ago 2026 y el 19 ago 2026; la quinta por la relectura conjunta de las tres colisiones de clase, vuelta 49, que volteo el puesto 844 de `A` a `D`]** |\n"
     "| de esas, colapsan a auto-arista al resolver (mismo nodo vivo en los dos lados) | ~~**0**~~ ~~**1**~~ **41** **[CORREGIDA DOS VECES, el 15 ago 2026 y el 19 ago 2026. Y LA SEGUNDA NO ES UN ERROR: ES LA HUELLA DE LA CIRUGIA. Cada acto que se funde convierte su par `A` en un par cuyos dos ids resuelven al mismo nodo vivo. Las 41 son exactamente los pares `A` que las fusiones de las fases 02 y 03 ya consumieron, impresas una a una por el instrumento en `../loop/SALIDA_V49_RECOMPUTO_3388.txt`]** |\n"
     "| pares distintos en el retrato tras resolver y deduplicar | ~~**583**~~ ~~**582**~~ ~~**580**~~ ~~**575**~~ ~~**574**~~ **533** **[CORREGIDA CINCO VECES, la ultima el 19 ago 2026]** |",

     "| A crudas en el archivo (`clase == 'A'`), corte 3.388 | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ **573** **[CORREGIDA SEIS VECES, el 15 y el 18 ago 2026 y el 19 ago 2026; la sexta el 19 ago 2026 en la vuelta 50, porque el volteo del puesto **305** de `A` a `D` (la limpieza `P.16` de la colision que la fusion del acto 1 fabrico, vuelta 49) MOVIO ESTA TABLA Y LA TABLA NO SE BARRIO EN AQUEL ACTO. Medido hoy con `python scripts/plan/recomputo_3388.py` (`../loop/SALIDA_V50_RECOMPUTO_APERTURA.txt`, paso 1)]** |\n"
     "| de esas, colapsan a auto-arista al resolver (mismo nodo vivo en los dos lados) | ~~**0**~~ ~~**1**~~ ~~**41**~~ **48** **[CORREGIDA TRES VECES, el 15 ago 2026 y el 19 ago 2026 (vueltas 49 y 50). Y NINGUNA DE LAS DOS ULTIMAS ES UN ERROR DE LECTURA: ES LA HUELLA DE LA CIRUGIA, que la propia fila ya explicaba. Cada acto que se funde convierte su par `A` en un par cuyos dos ids resuelven al mismo nodo vivo. El 41 era el corte de la TAREA 1.3 de la vuelta 49, ANTERIOR a las tres fusiones de su TAREA 2 (actos 20, 34 y la parte A del acto 1), que anadieron siete; las 48 estan impresas una a una por el instrumento en `../loop/SALIDA_V50_RECOMPUTO_APERTURA.txt`]** |\n"
     "| pares distintos en el retrato tras resolver y deduplicar | ~~**583**~~ ~~**582**~~ ~~**580**~~ ~~**575**~~ ~~**574**~~ ~~**533**~~ **525** **[CORREGIDA SEIS VECES, la ultima el 19 ago 2026 (vuelta 50), por el mismo motivo que las dos filas de arriba]** |",

     "LAS TRES FILAS DEL RETRATO SE PRESENTAN COMO VIGENTES (corte 3.388) y quedaron atras tras el volteo del 305 y las tres fusiones de la vuelta 49. Es la caida de cifra publicada que el acta 49 seccion 3 nombra, y se corrige con la medicion de HOY, no con la del acta."),

    # ---------- 2. LA COMPROBACION ii (fila 528) ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "| **ii** | A vigentes resueltas del retrato (~~583~~ ~~582~~ ~~580~~ **533**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ ~~580~~ **533**) | **OK**, recomprobado el 15 ago 2026 con las cifras nuevas, DOS veces, y **RE-CORRIDO EL 19 ago 2026 (vuelta 49): sigue OK con 533 y 533**, y con el las otras tres ([`../loop/SALIDA_V49_RECOMPUTO_3388.txt`](../loop/SALIDA_V49_RECOMPUTO_3388.txt), *LAS CUATRO: TODAS OK*) |",

     "| **ii** | A vigentes resueltas del retrato (~~583~~ ~~582~~ ~~580~~ ~~533~~ **525**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ ~~580~~ ~~533~~ **525**) | **OK**, recomprobado el 15 ago 2026 con las cifras nuevas, DOS veces, ~~y **RE-CORRIDO EL 19 ago 2026 (vuelta 49): sigue OK con 533 y 533**~~ y **RE-CORRIDO OTRA VEZ EL 19 ago 2026 (vuelta 50) CON LA PAREJA NUEVA: sigue OK con 525 y 525**, y con el las otras tres ([`../loop/SALIDA_V50_RECOMPUTO_APERTURA.txt`](../loop/SALIDA_V50_RECOMPUTO_APERTURA.txt), *LAS CUATRO: TODAS OK*). **La pareja de la vuelta 49 se tacha y no se borra: era cierta con el retrato de aquel corte y dejo de serlo cuando el 305 y las tres fusiones movieron el retrato dentro de la propia vuelta 49** |",

     "La comprobacion se presenta como vigente y su cifra la mueve toda fusion y todo volteo de A. Re-corrida hoy por el propio instrumento con la pareja nueva."),

    # ---------- 3. EL TOTAL DE LA TABLA POR DOMINIO (fila 1079) ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "| **total** | **3.388** | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ **574** | ~~**17,2 %**~~ ~~**17,1 %**~~ ~~**17,0 %**~~ **16,9 %** |",

     "| **total** | **3.388** | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ **573** | ~~**17,2 %**~~ ~~**17,1 %**~~ ~~**17,0 %**~~ **16,9 %** |",

     "Total de A presentado como vigente. El puesto 305 volteo de A a D el 19 ago 2026 (vuelta 49) y es de `core`, medido hoy con `recomputar_marcador.py 3388` (`../loop/SALIDA_V50_MARCADOR_APERTURA.txt`). LA TASA NO SE MUEVE Y SE DICE POR QUE: 573 sobre 3.388 sigue redondeando a 16,9 por ciento, asi que la celda de la tasa queda como esta y no se le anade un tachado que fingiria un cambio que no hubo."),

    # ---------- 4. LA CUARTA CORRECCION DECLARADA DE LA FILA core ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "digito.** **La tasa de quality\n"
     "cayo de 24,3 % (corte 2.900, acta vuelta 4) a 14,9 % (corte 3.388)**",

     "digito.** **CUARTA CORRECCION DECLARADA (19 ago 2026, vuelta 50): el total es hoy `A 573,\n"
     "B 77, C 8, D 2.730` sobre los mismos 3.388 pares, y el UNICO dominio que cambia vuelve a ser\n"
     "`core`, porque los CUATRO volteos de la vuelta 49 (806, 844, 263 y 305) son los cuatro de\n"
     "`core`. Medido hoy dominio por dominio (`../loop/SALIDA_V50_MARCADOR_APERTURA.txt`): `core`\n"
     "queda en `n 1.445, A 334 (23,1 por ciento)`. Los otros nueve dominios, identicos al digito.\n"
     "LA FILA `core` DE LA TABLA DE ARRIBA SIGUE DICIENDO 344 Y NO SE REESCRIBE, por el mismo motivo\n"
     "que la segunda correccion ya escribio: es la foto del 13 ago.** **La tasa de quality\n"
     "cayo de 24,3 % (corte 2.900, acta vuelta 4) a 14,9 % (corte 3.388)**",

     "La cadena de correcciones declaradas de esta tabla se quedo en la tercera (18 ago). El dominio `core` vigente hoy es 334 y no 336, y sin esta cuarta entrada la unica cifra de `core` legible como reciente seria la del 18 ago."),

    # ---------- 5. EL MARCADOR DEL APENDICE 100.1 DE CIERRE DE FASE I ----------
    ("docs/INTRA_DOMINIO_INFORME.md",
     "| **A** | ~~**583** (17,2 %)~~ ~~582~~ ~~581~~ ~~576~~ ~~575 (17,0 %)~~ **574** (16,9 %), ver las correcciones declaradas debajo |\n"
     "| **B** | ~~89~~ ~~87~~ ~~84~~ ~~83~~ ~~82~~ ~~81~~ ~~80~~ ~~79~~ **77** |\n"
     "| **C** | ~~7~~ **8** |\n"
     "| **D** | ~~**2.709** (80,0 %)~~ ~~2.711~~ ~~2.714~~ ~~2.716~~ ~~2.721~~ ~~2.722~~ ~~2.723~~ ~~2.724~~ ~~2.725~~ ~~2.726~~ **2.729** (80,5 %) |",

     "| **A** | ~~**583** (17,2 %)~~ ~~582~~ ~~581~~ ~~576~~ ~~575 (17,0 %)~~ ~~574~~ **573** (16,9 %), ver las correcciones declaradas debajo |\n"
     "| **B** | ~~89~~ ~~87~~ ~~84~~ ~~83~~ ~~82~~ ~~81~~ ~~80~~ ~~79~~ **77** |\n"
     "| **C** | ~~7~~ **8** |\n"
     "| **D** | ~~**2.709** (80,0 %)~~ ~~2.711~~ ~~2.714~~ ~~2.716~~ ~~2.721~~ ~~2.722~~ ~~2.723~~ ~~2.724~~ ~~2.725~~ ~~2.726~~ ~~2.729~~ **2.730** (80,6 %) |\n"
     "\n"
     "> **CORRECCION DECLARADA (19 ago 2026, vuelta 50). LA TABLA VOLVIO A QUEDARSE ATRAS, Y ESTA\n"
     "> VEZ DENTRO DE LA MISMA VUELTA QUE LA ACABABA DE CORREGIR.** La correccion de la vuelta 49\n"
     "> que esta justo debajo se escribio con el marcador de su TAREA 1.3 (`A 574, D 2.729`) y\n"
     "> **despues, en su propia TAREA 2, el puesto 305 volteo de `A` a `D`** por la limpieza `P.16`\n"
     "> de la colision que la fusion del acto 1 fabrico. **Nadie volvio a barrer esta tabla al\n"
     "> cerrar aquella vuelta**, y esa es la caida de cifra publicada que el acta de la vuelta 49\n"
     "> nombra en su seccion 3. La leccion queda escrita donde se cometio: **quien mueve una clase o\n"
     "> funde un acto corre el barrido `9.10` ANTES de cerrar la vuelta**, no solo en el acto del\n"
     "> volteo. Medido hoy con `python scripts/recomputar_marcador.py 3388`\n"
     "> (`../loop/SALIDA_V50_MARCADOR_APERTURA.txt`): **A 573, B 77, C 8, D 2.730** sobre `n`\n"
     "> **3.388**, cero huecos y cero duplicados.",

     "El marcador del apendice se presenta como el marcador vigente del archivo y quedo UNA relectura atras: el volteo del 305 de la propia vuelta 49. Se corrige con la medicion de hoy y se declara la caida donde se cometio."),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    args = ap.parse_args()

    print("=" * 78)
    print("CORRECCIONES DEL BARRIDO 9.10, %s" % FECHA)
    print("modo: %s" % ("EJECUTAR" if args.ejecutar else "SIMULAR"))
    print("=" * 78)
    print()

    # PRIMERO SE COMPRUEBAN TODAS, DESPUES SE ESCRIBE NINGUNA O TODAS.
    planes = []
    fallos = 0
    for n, (fich, viejo, nuevo, motivo) in enumerate(CORRECCIONES, 1):
        texto = io.open(fich, encoding="utf-8").read()
        veces = texto.count(viejo)
        print("--- CORRECCION %d: %s" % (n, fich))
        print("    motivo: %s" % motivo)
        print("    apariciones del texto viejo: %d" % veces)
        if veces != 1:
            print("    ROJO: tiene que aparecer EXACTAMENTE UNA VEZ. No se escribe nada.")
            fallos += 1
            continue
        if nuevo in texto:
            print("    YA APLICADA (idempotencia): el texto nuevo ya esta dentro.")
            continue
        planes.append((fich, viejo, nuevo))
        print("    OK, lista para aplicar (%d a %d caracteres)"
              % (len(viejo), len(nuevo)))
        print()

    if fallos:
        print()
        print("ABORTA: %d correccion(es) en rojo." % fallos)
        return 1

    if not args.ejecutar:
        print()
        print("SIMULACION: %d correccion(es) listas. Nada escrito." % len(planes))
        return 0

    # Se agrupan por fichero para escribir cada uno una sola vez.
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
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
