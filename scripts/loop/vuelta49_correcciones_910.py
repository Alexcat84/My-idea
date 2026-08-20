# -*- coding: utf-8 -*-
"""vuelta49_correcciones_910.py . APLICA LAS CORRECCIONES QUE EL BARRIDO 9.10
ADJUDICO COMO TABLAS ENVEJECIDAS, cada una con su texto viejo TACHADO y no
borrado.

EL BARRIDO LISTA, ESTE INSTRUMENTO ESCRIBE, Y LA ADJUDICACION ES DE LECTURA.
scripts/loop/vuelta49_barrido_910.py imprime 114 candidatos y declara su propio
limite: una cifra con su fecha de corte declarada aparece ahi sin estar
envejecida. La separacion entre las dos familias la hizo el ejecutor leyendo, y
va escrita en el campo motivo de cada correccion para poder discutirla una a una.

LA VARA DE SEPARACION, escrita para poder discutirla: se corrige lo que se
presenta como VIGENTE (el retrato de las A, el marcador del cierre de Fase I, y
toda tabla que diga la CLASE de uno de los seis puestos corregidos). NO se toca
lo que se presenta como el estado de un dia con su corte al lado (las filas de
apertura y cierre de vueltas pasadas, y las salidas de instrumento), porque
reescribir el estado de un dia es falsificarlo, no corregirlo.

CADA CORRECCION ES UNA SUSTITUCION LITERAL Y UNICA. Si el texto viejo no
aparece EXACTAMENTE una vez, el instrumento aborta sin escribir nada: una
sustitucion que casa dos sitios es una errata esperando.

MODOS: --simular (por defecto) y --ejecutar.

Uso: python scripts/loop/vuelta49_correcciones_910.py [--ejecutar]
"""
import argparse
import io
import sys

FECHA = "19 ago 2026 (vuelta 49)"

# (fichero, texto viejo, texto nuevo, motivo)
CORRECCIONES = [

    # ---------- 1. EL RETRATO DE LAS A ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "| A crudas en el archivo (`clase == 'A'`), corte 3.388 | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ **575** **[CORREGIDA CUATRO VECES, el 15 y el 18 ago 2026, ver las correcciones declaradas al principio del documento]** |\n"
     "| de esas, colapsan a auto-arista al resolver (mismo nodo vivo en los dos lados) | ~~**0**~~ **1** **[CORREGIDA el 15 ago 2026: la fusion de `OP-D-02` la produjo, ver la correccion declarada al principio del documento]** |\n"
     "| pares distintos en el retrato tras resolver y deduplicar | ~~**583**~~ ~~**582**~~ ~~**580**~~ ~~**575**~~ **574** **[CORREGIDA CUATRO VECES, el 15 y el 18 ago 2026, ver las correcciones declaradas al principio del documento]** |",

     "| A crudas en el archivo (`clase == 'A'`), corte 3.388 | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ **574** **[CORREGIDA CINCO VECES, el 15 y el 18 ago 2026 y el 19 ago 2026; la quinta por la relectura conjunta de las tres colisiones de clase, vuelta 49, que volteo el puesto 844 de `A` a `D`]** |\n"
     "| de esas, colapsan a auto-arista al resolver (mismo nodo vivo en los dos lados) | ~~**0**~~ ~~**1**~~ **41** **[CORREGIDA DOS VECES, el 15 ago 2026 y el 19 ago 2026. Y LA SEGUNDA NO ES UN ERROR: ES LA HUELLA DE LA CIRUGIA. Cada acto que se funde convierte su par `A` en un par cuyos dos ids resuelven al mismo nodo vivo. Las 41 son exactamente los pares `A` que las fusiones de las fases 02 y 03 ya consumieron, impresas una a una por el instrumento en `../loop/SALIDA_V49_RECOMPUTO_3388.txt`]** |\n"
     "| pares distintos en el retrato tras resolver y deduplicar | ~~**583**~~ ~~**582**~~ ~~**580**~~ ~~**575**~~ ~~**574**~~ **533** **[CORREGIDA CINCO VECES, la ultima el 19 ago 2026]** |",

     "El retrato de las A se presenta como VIGENTE (corte 3.388) y llevaba CUATRO fusiones sin barrer: decia UN colapso cuando hoy hay CUARENTA Y UNO. Es la caida de mi propio linaje que este barrido destapa, y va declarada en el reporte de la vuelta."),

    # ---------- 2. LA COMPROBACION ii ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "| **ii** | A vigentes resueltas del retrato (~~583~~ ~~582~~ **580**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ **580**) | **OK**, recomprobado el 15 ago 2026 con las cifras nuevas, DOS veces |",

     "| **ii** | A vigentes resueltas del retrato (~~583~~ ~~582~~ ~~580~~ **533**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ ~~580~~ **533**) | **OK**, recomprobado el 15 ago 2026 con las cifras nuevas, DOS veces, y **RE-CORRIDO EL 19 ago 2026 (vuelta 49): sigue OK con 533 y 533**, y con el las otras tres ([`../loop/SALIDA_V49_RECOMPUTO_3388.txt`](../loop/SALIDA_V49_RECOMPUTO_3388.txt), *LAS CUATRO: TODAS OK*) |",

     "La comprobacion se presenta como vigente y su cifra la mueve toda fusion. Re-corrida hoy por el propio instrumento."),

    # ---------- 3. EL TOTAL DE LA TABLA POR DOMINIO ----------
    ("docs/plan/RECOMPUTO_3388.md",
     "| **total** | **3.388** | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ **575** | ~~**17,2 %**~~ ~~**17,1 %**~~ **17,0 %** |",

     "| **total** | **3.388** | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ **574** | ~~**17,2 %**~~ ~~**17,1 %**~~ ~~**17,0 %**~~ **16,9 %** |",

     "Total de A presentado como vigente. El puesto 844 volteo de A a D el 19 ago 2026 y es de `core`, medido hoy con `recomputar_marcador.py 3388`."),

    # ---------- 4. EL MARCADOR DEL APENDICE DE CIERRE DE FASE I ----------
    ("docs/INTRA_DOMINIO_INFORME.md",
     "| **A** | ~~**583** (17,2 %)~~ ~~582~~ ~~581~~ ~~576~~ **575** (17,0 %), ver las correcciones declaradas debajo |\n"
     "| **B** | ~~89~~ ~~87~~ ~~84~~ **83** |\n"
     "| **C** | ~~7~~ **8** |\n"
     "| **D** | ~~**2.709** (80,0 %)~~ ~~2.711~~ ~~2.714~~ ~~2.716~~ ~~2.721~~ **2.722** |",

     "| **A** | ~~**583** (17,2 %)~~ ~~582~~ ~~581~~ ~~576~~ ~~575 (17,0 %)~~ **574** (16,9 %), ver las correcciones declaradas debajo |\n"
     "| **B** | ~~89~~ ~~87~~ ~~84~~ ~~83~~ ~~82~~ ~~81~~ ~~80~~ ~~79~~ **77** |\n"
     "| **C** | ~~7~~ **8** |\n"
     "| **D** | ~~**2.709** (80,0 %)~~ ~~2.711~~ ~~2.714~~ ~~2.716~~ ~~2.721~~ ~~2.722~~ ~~2.723~~ ~~2.724~~ ~~2.725~~ ~~2.726~~ **2.729** (80,5 %) |\n"
     "\n"
     "> **CORRECCION DECLARADA (19 ago 2026, vuelta 49), Y LA MITAD DE ELLA ES UNA CAIDA DE MI\n"
     "> PROPIO LINAJE QUE SE CUENTA EN VEZ DE ESCONDERSE.** Esta tabla venia corregida hasta el 18 ago\n"
     "> 2026 y **se quedo ahi**: las relecturas de los pares **835** (vuelta 42), **599** (vuelta 43) y\n"
     "> **233** (vuelta 44) movieron `B` y `D` y **ninguna de las tres barrio esta tabla**, que es\n"
     "> exactamente la averia que el banco `9.10` nombra. Lo que hoy la mueve son las tres de la vuelta\n"
     "> 49 (**806** y **263** de `B` a `D`, **844** de `A` a `D`); lo que la tenia parada eran las tres\n"
     "> anteriores. **Las cifras intermedias van tachadas en la cadena para que el salto no parezca de\n"
     "> un solo dia.** Medido hoy con `python scripts/recomputar_marcador.py 3388`\n"
     "> (`docs/loop/SALIDA_V49_MARCADOR.txt`): **A 574, B 77, C 8, D 2.729** sobre `n` **3.388**, cero\n"
     "> huecos y cero duplicados.",

     "El marcador del apendice se presenta como el marcador del archivo y estaba CUATRO relecturas atrasado, tres de ellas de vueltas mias. Se corrige y se declara la caida."),

    # ---------- 5. LAS DOS TABLAS QUE DAN 806 COMO B ----------
    ("docs/INTRA_DOMINIO_INFORME.md",
     "| **A** | 635 (`customer_discovery`), **849** (`customer_discovery_get_out_of_building`) |\n"
     "| **D** | 377, **854** |\n"
     "| **B** | **683, 707, 806** |",

     "| **A** | 635 (`customer_discovery`), **849** (`customer_discovery_get_out_of_building`) |\n"
     "| **D** | 377, **854**, y desde el 19 ago 2026 tambien **806** |\n"
     "| **B** | ~~**683, 707, 806**~~ **683, 707** |\n"
     "\n"
     "> **CORRECCION DECLARADA (19 ago 2026, vuelta 49).** El **806** paso de `B` a `D` en la\n"
     "> relectura conjunta de las tres colisiones de clase. **Su `B` era un `B` DE ESPERA** y la propia\n"
     "> razon lo decia: esperaba a que `voz_del_cliente_voc` se operase. **Ya esta operado**, y el par\n"
     "> resuelto sale `D`. **`customer_development_modelo` baja de TRES dudosos a DOS.**",

     "Tabla que da la clase de un puesto corregido. Es la especie exacta del banco 9.10."),

    ("docs/INTRA_DOMINIO_INFORME.md",
     "| **el nodo** | **siete pares leidos**: **A** en 635 y 849, **D** en 377 y 854, **B en 683, 707 y 806** |",

     "| **el nodo** | **siete pares leidos**: **A** en 635 y 849, **D** en 377, 854 y ~~-~~ **806**, **B** en ~~683, 707 y 806~~ **683 y 707**. **CORREGIDA el 19 ago 2026 (vuelta 49)**: el 806 paso de `B` a `D`, asi que **los dudosos sobre este nodo pasan de TRES a DOS** |",

     "Misma especie: la ficha de la mesa 3 da la clase del 806 como B."),

    # ---------- 6. LA NARRACION DEL BLOQUEO, QUE YA TERMINO ----------
    ("docs/INTRA_DOMINIO_INFORME.md",
     "> **2. LA VOZ DEL CLIENTE, CINCO nodos vistos** (puesto 806), y uno de ellos,\n"
     "> `voz_del_cliente_voc`, **es costura confirmada que bloquea dos pares**. **No se\n"
     "> puede decidir de a pares mientras el nodo grande siga sin operar.**",

     "> **2. LA VOZ DEL CLIENTE, CINCO nodos vistos** (puesto 806), y uno de ellos,\n"
     "> `voz_del_cliente_voc`, **es costura confirmada que bloquea dos pares**. **No se\n"
     "> puede decidir de a pares mientras el nodo grande siga sin operar.**\n"
     ">\n"
     "> **NOTA DE CIERRE DECLARADA (19 ago 2026, vuelta 49), y el texto de arriba NO se borra porque\n"
     "> era exacto el dia que se escribio: EL BLOQUEO TERMINO.** `voz_del_cliente_voc` **esta\n"
     "> operado** (`OP-F-04-COL`) y hoy carga a `enfoque_mercado_voc` como alias, medido en el fichero\n"
     "> del nodo. El **806** se releyo con el par ya resuelto y **paso de `B` a `D`**. **El `B` no\n"
     "> envejecio por error de lectura: se cumplio su propia condicion**, que es la mejor cosa que le\n"
     "> puede pasar a un `B` de espera.",

     "La nota decia que no se podia decidir mientras el nodo grande no se operara. Se opero. Se cierra sin borrar."),

    # ---------- 7B. LA TABLA DE CLASES DE LAS LECTURAS DIRIGIDAS DEL RACIMO ----------
    ("docs/plan/LECTURAS_DIRIGIDAS.md",
     "| `brainstorming_divergente` contra `generar_multiples_opciones` | **A** | puesto **844**, cribado, **releido por `P.5` el 19 ago 2026** |",

     "| `brainstorming_divergente` contra `generar_multiples_opciones` | ~~**A**~~ **D** | puesto **844**, cribado, **releido por `P.5` el 19 ago 2026** y **VOLTEADO DE `A` A `D` el 19 ago 2026 (vuelta 49)** por la relectura conjunta del par RESUELTO: los dos ids de este puesto estan hoy deprecados y resuelven a `reglas_brainstorming` y a `pensamiento_convergente_divergente`, y lo que cada superviviente anade al otro **ya no es LINEA sino PROCEDIMIENTO**, asi que el segundo polo del `9.22` que produjo la `A` no sobrevive al par resuelto |",

     "Tabla de clases de las lecturas dirigidas del racimo del brainstorming. Da la clase del 844 como A y hoy es D."),

    # ---------- 7. LA LISTA DE PARES A QUE SOSTIENEN EL ACTO DE SIETE ----------
    ("docs/INTRA_DOMINIO_INFORME.md",
     "| **1** | **7** | 1 | 6 | 234, 586, 823, 834, 844, 885, 943 | 2 |",

     "| **1** | **7** | 1 | 6 | 234, 586, 823, 834, ~~844~~, 885, 943 **[CORREGIDA el 19 ago 2026 (vuelta 49): el `844` dejo de ser `A` y ya no sostiene nada. Y la fila entera esta envejecida por otra causa mayor que se dice en vez de callarse: `OP-D-04` fundio ese acto, asi que de sus siete pares `A` hoy CINCO (234, 823, 834, 885 y 943) resuelven a auto-par, medido en `../loop/SALIDA_V49_RECOMPUTO_3388.txt`. La fila se conserva como el retrato del dia que se midio]** | 2 |",

     "Tabla que lista pares A por numero. El 844 ya no es A, y ademas el acto entero se fundio."),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("CORRECCIONES DEL BARRIDO 9.10 . MODO %s"
          % ("EJECUTAR" if a.ejecutar else "SIMULAR"))
    print("=" * 78)

    cache, fallos = {}, []
    for i, (f, viejo, nuevo, motivo) in enumerate(CORRECCIONES, 1):
        if f not in cache:
            cache[f] = io.open(f, encoding="utf-8", newline="").read()
        n = cache[f].count(viejo)
        print()
        print("--- CORRECCION %d . %s" % (i, f))
        print("    motivo: %s" % motivo)
        # IDEMPOTENCIA: si el texto NUEVO ya esta, esta correccion ya se aplico y
        # no se apila. Correr dos veces este instrumento no duplica una nota.
        if n == 0 and cache[f].count(nuevo) == 1:
            print("    YA APLICADA (el texto nuevo esta y el viejo no). Se salta.")
            continue
        print("    el texto viejo aparece %d vez(ces): %s"
              % (n, "OK" if n == 1 else "ROJO, tiene que ser exactamente 1"))
        if n != 1:
            fallos.append("correccion %d en %s: %d coincidencias" % (i, f, n))
            continue
        cache[f] = cache[f].replace(viejo, nuevo)
        print("    lineas viejas %d -> nuevas %d"
              % (viejo.count("\n") + 1, nuevo.count("\n") + 1))

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for x in fallos:
            print("  [ROJO] %s" % x)
        return 1

    print()
    print("RESUMEN: %d correcciones sobre %d ficheros" % (len(CORRECCIONES), len(cache)))
    if not a.ejecutar:
        print("SIMULACION: cero escrituras.")
        return 0
    for f, t in cache.items():
        io.open(f, "w", encoding="utf-8", newline="").write(t)
        print("ESCRITO: %s" % f)
    return 0


if __name__ == "__main__":
    sys.exit(main())
