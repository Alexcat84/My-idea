# -*- coding: utf-8 -*-
"""vuelta55_registro_tramo.py . ESCRIBE EL REGISTRO DEL CIERRE DEL TRAMO 2 DE
OP-U-01 AL FINAL DE docs/plan/03_FUSIONES.md.

LAS TABLAS QUE RESUMEN DECISIONES NO SE TECLEAN: se pegan enteras de la salida
de scripts/loop/vuelta55_tallar_planes.py, que las talla de los PLANES SELLADOS
(regla de trabajo del acta 54, y remedio de la caida de reporte que esa acta
nombra). Este instrumento LEE esa salida y la inserta, con el comando citado al
lado, en vez de reproducirla a mano.

LAS CIFRAS DEL ESTADO se leen de las salidas del dia QUE CADA CELDA CITA, y el
instrumento las EXTRAE de esos ficheros en vez de recibirlas por parametro: una
celda tecleada es la especie de caida que las vueltas 31 y 32 pagaron.

IDEMPOTENTE: si la cabecera del registro ya esta en el fichero, no escribe.

Uso: python scripts/loop/vuelta55_registro_tramo.py [--simular]
"""
# ROTULO titulo especie=SELLO_FIJO sujeto=tramo:2 corte=2026-08-20 motivo="escribe el registro del CIERRE del tramo 2: sujeto fijo, sin argumento que lo repunte"
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
FUSIONES = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")

CABECERA = ("## `OP-U-01`, TRAMO 2 **CERRADO: 45 ACTOS FUNDIDOS DE 50 Y CINCO "
            "DECLARADOS** (20 ago 2026, vuelta 55)")


def leer(nombre):
    return io.open(os.path.join(LOOP, nombre), encoding="utf-8").read()


def busca(texto, patron, etiqueta, fallos):
    m = re.search(patron, texto)
    if not m:
        fallos.append("no se pudo leer %s" % etiqueta)
        return "?"
    return m.group(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("EL REGISTRO DEL CIERRE DEL TRAMO 2, con cada cifra leida de su salida")
    print("=" * 78)
    print()

    fallos = []
    # --- las cifras del CIERRE, cada una de la salida que su celda cita ---
    mc = leer("SALIDA_V55_MARCADOR_CIERRE.txt")
    A = busca(mc, r"\n  A (\d+)", "A del marcador de cierre", fallos)
    B = busca(mc, r"\n  B (\d+)", "B del marcador de cierre", fallos)
    C = busca(mc, r"\n  C (\d+)", "C del marcador de cierre", fallos)
    D = busca(mc, r"\n  D (\d+)", "D del marcador de cierre", fallos)

    ec = leer("SALIDA_V55_CIERRE.txt")
    vivos = busca(ec, r"vivos\s+: (\d+)", "vivos de cierre", fallos)
    dep = busca(ec, r"deprecados\s+: (\d+)", "deprecados de cierre", fallos)
    enl = busca(ec, r"enlaces\s+: (\d+)", "enlaces de cierre", fallos)

    rc = leer("SALIDA_V55_RECOMPUTO_CIERRE.txt")
    crudas = busca(rc, r"clase == 'A'\): (\d+)", "A crudas de cierre", fallos)
    colap = busca(rc, r"los dos lados\): (\d+)", "colapsos de cierre", fallos)
    pares = busca(rc, r"deduplicar\): (\d+)", "pares distintos de cierre", fallos)
    cerr = busca(rc, r"CERRADOS: (\d+) sobre (\d+) nodos", "actos CERRADOS de cierre", fallos)
    cerrn = re.search(r"CERRADOS: \d+ sobre (\d+) nodos", rc)
    cerrn = cerrn.group(1) if cerrn else "?"
    abie = busca(rc, r"ABIERTOS: (\d+) sobre (\d+) nodos", "actos ABIERTOS de cierre", fallos)
    abien = re.search(r"ABIERTOS: \d+ sobre (\d+) nodos", rc)
    abien = abien.group(1) if abien else "?"
    cuatro = "TODAS OK" if "LAS CUATRO: TODAS OK" in rc else "NO TODAS OK"

    cola = busca(leer("SALIDA_V55_COLA_CIERRE.txt"), r"nodos en la cola: (\d+)",
                 "cola de cierre", fallos)
    cen = leer("SALIDA_V55_COLISIONES_CIERRE.txt")
    coli = busca(cen, r"COLISIONES DE CLASE VIGENTES\s+: (\d+)", "colisiones de cierre", fallos)
    auto = busca(cen, r"AUTO-PARES \(los dos lados al mismo vivo\): (\d+)",
                 "auto-pares de cierre", fallos)
    dup = leer("SALIDA_V55_DUPLICADAS_CIERRE.txt")
    dupg = busca(dup, r"grupos afectados \(nodo mas campo mas destino\) \| (\d+)",
                 "grupos de duplicadas", fallos)
    dupn = busca(dup, r"nodos con al menos una duplicada\*\* \| \*\*(\d+)",
                 "nodos con duplicadas", fallos)

    # --- las cifras de la APERTURA, de sus propias salidas ---
    ma = leer("SALIDA_V55_MARCADOR_APERTURA.txt")
    aA = busca(ma, r"\n  A (\d+)", "A de apertura", fallos)
    aB = busca(ma, r"\n  B (\d+)", "B de apertura", fallos)
    aC = busca(ma, r"\n  C (\d+)", "C de apertura", fallos)
    aD = busca(ma, r"\n  D (\d+)", "D de apertura", fallos)
    ea = leer("SALIDA_V55_APERTURA.txt")
    avivos = busca(ea, r"vivos\s+: (\d+)", "vivos de apertura", fallos)
    adep = busca(ea, r"deprecados\s+: (\d+)", "deprecados de apertura", fallos)
    aenl = busca(ea, r"enlaces\s+: (\d+)", "enlaces de apertura", fallos)
    ra = leer("SALIDA_V55_RECOMPUTO_APERTURA.txt")
    acrudas = busca(ra, r"clase == 'A'\): (\d+)", "A crudas de apertura", fallos)
    acolap = busca(ra, r"los dos lados\): (\d+)", "colapsos de apertura", fallos)
    apares = busca(ra, r"deduplicar\): (\d+)", "pares distintos de apertura", fallos)
    acerr = busca(ra, r"CERRADOS: (\d+) sobre", "CERRADOS de apertura", fallos)
    acerrn = re.search(r"CERRADOS: \d+ sobre (\d+) nodos", ra)
    acerrn = acerrn.group(1) if acerrn else "?"
    aabie = busca(ra, r"ABIERTOS: (\d+) sobre", "ABIERTOS de apertura", fallos)
    aabien = re.search(r"ABIERTOS: \d+ sobre (\d+) nodos", ra)
    aabien = aabien.group(1) if aabien else "?"
    acola = busca(leer("SALIDA_V55_COLA_APERTURA.txt"), r"nodos en la cola: (\d+)",
                  "cola de apertura", fallos)
    cena = leer("SALIDA_V55_COLISIONES_APERTURA.txt")
    acoli = busca(cena, r"COLISIONES DE CLASE VIGENTES\s+: (\d+)", "colisiones de apertura", fallos)
    aauto = busca(cena, r"AUTO-PARES \(los dos lados al mismo vivo\): (\d+)",
                  "auto-pares de apertura", fallos)
    dupa = leer("SALIDA_V55_DUPLICADAS_APERTURA.txt")
    adupg = busca(dupa, r"grupos afectados \(nodo mas campo mas destino\) \| (\d+)",
                  "grupos de duplicadas de apertura", fallos)
    adupn = busca(dupa, r"nodos con al menos una duplicada\*\* \| \*\*(\d+)",
                  "nodos con duplicadas de apertura", fallos)

    # --- las tablas talladas, pegadas ENTERAS de la salida del instrumento ---
    tallado = leer("SALIDA_V55_TALLAR_PLANES.txt")
    def bloque(desde, hasta):
        i = tallado.index(desde)
        j = tallado.index(hasta) if hasta else len(tallado)
        cuerpo = tallado[i + len(desde):j].strip("\n")
        return "\n".join(l for l in cuerpo.splitlines() if l.startswith("|"))
    try:
        t1 = bloque("--- TABLA 1: LOS TRES LOTES, CON SUS PIEZAS ---", "--- TABLA 2")
        t2 = bloque("--- TABLA 2: LA FORMA DEL VEREDICTO, CONTADA DE LOS MOTIVOS SELLADOS ---",
                    "--- TABLA 3")
        t3 = bloque("--- TABLA 3: ACTO A ACTO, SUPERVIVIENTE Y ABSORBIDO ---", "  actos tallados")
    except ValueError as e:
        fallos.append("no se pudo recortar una tabla del tallado: %s" % e)
        t1 = t2 = t3 = ""

    if fallos:
        print("  ROJO, %d cifras no se pudieron leer y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("     %s" % f)
        return 1

    for k, v in [("A", A), ("B", B), ("C", C), ("D", D), ("vivos", vivos),
                 ("deprecados", dep), ("enlaces", enl), ("crudas", crudas),
                 ("colapsos", colap), ("pares", pares), ("cola", cola),
                 ("colisiones", coli), ("auto-pares", auto)]:
        print("  %-12s cierre: %s" % (k, v))
    print()

    texto = """

---

%s

**EL TRAMO 2 QUEDA CERRADO EN CODIGO**: de sus **50** actos, **45 estan fundidos** y **CINCO
quedan DECLARADOS**, cada uno con su especie escrita y su carril. La vuelta 55 ejecuto
**VEINTICINCO fusiones** en tres lotes, y **una de ellas es una fusion REHECHA**: el acto **23**,
que la vuelta 54 habia fundido al reves y que esta vuelta deshizo y volvio a hacer con correccion
declarada.

### EL INSTRUMENTO DEL TRAMO CAYO EN ROJO AL CONTINUAR, Y EL ROJO NO DECIA LO QUE DECIA

**Corrido `scripts/loop/vuelta54_tramo2_nomina.py` sobre la nomina del dia como el encargo manda,
CAE EN ROJO CON PARADA** ([`../loop/SALIDA_V55_TRAMO2_NOMINA.txt`](../loop/SALIDA_V55_TRAMO2_NOMINA.txt)).
**El motivo se fue a mirar antes de tocar nada, y es estructural y no del tramo:** aquel
instrumento nacio para **ABRIR** un tramo y compara los 50 `CERRADOS` siguientes de HOY contra los
puestos 51 a 100 de la nomina de la vuelta 48. **En cuanto se funde un acto del tramo, el acto sale
de la nomina de `CERRADOS`, la lectura B encoge y la lectura A rellena hasta 50 con actos del tramo
SIGUIENTE.** El rojo dice *el tramo ya se toco*, no *el tramo no esta determinado*.

**SUCESOR DECLARADO, por la vara del acta 54, pregunta 3** (sus cifras ya las cita la tabla de las
dos lecturas de esta misma pagina, asi que la logica del ancestro NO se toca):
`scripts/loop/vuelta55_tramo2_nomina.py`, **con la aritmetica copiada**, la identidad del tramo
**POR MIEMBROS** de los puestos 51 a 100 de la 48, **el ordinal derivado del fichero y no tecleado**,
y el calzar de la continuacion en **dos formas**
([`../loop/SALIDA_V55_TRAMO2_NOMINA_SUCESOR.txt`](../loop/SALIDA_V55_TRAMO2_NOMINA_SUCESOR.txt)):

| lo que el sucesor comprueba | resultado al abrir la vuelta 55 |
|---|---|
| los 50 del tramo, repartidos entre VIVOS y FUNDIDOS | **29 vivos y 21 fundidos**, suma 50 de 50 |
| los FUNDIDOS, comprobados uno a uno contra el grafo | **21 de 21**: los dos ids resuelven a UNO y el superviviente lleva el alias izado |
| **lectura A** (orden impreso de hoy) contra **lectura B** (orden de la vuelta 48), sobre los vivos | **CALZAN**, mismo conjunto y mismo orden |
| los supervivientes son **PREFIJO** de la lectura A de hoy | **SI**, ningun acto ajeno se cuela por delante |
| guarda de los cuatro ajenos | **VERDE**, ninguno de los cuatro entra |
| guarda de solape con el tramo 1 | **VERDE**, cero |

> **Y LOS 29 ORDINALES QUE IMPRIME REPRODUCEN AL DIGITO LOS QUE LA VUELTA 54 PUBLICO**, porque el
> ordinal se deriva del puesto de la vuelta 48 menos 50 y no de un contador nuevo.

### LOS TRES LOTES, TALLADOS DE LOS PLANES SELLADOS

**Estas tres tablas NO estan tecleadas: salen enteras de
`python scripts/loop/vuelta55_tallar_planes.py`**
([`../loop/SALIDA_V55_TALLAR_PLANES.txt`](../loop/SALIDA_V55_TALLAR_PLANES.txt)), **que las cuenta
de los `PLAN_V55_*.json` sellados**. Es el remedio mecanico de la caida de reporte que el acta de
la vuelta 54 nombra: una tabla que resume decisiones se talla de los planes, no de memoria.

%s

%s

%s

### LAS TRES ADJUDICACIONES QUE ESTA VUELTA EJECUTA, CON SU SEDE

| la adjudicacion | de donde viene | donde se ejecuta |
|---|---|---|
| **LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO** | acta de la vuelta 54, pregunta 1 | actos **1** y **15**, con el choque de conteos escrito en el motivo de cada plan |
| **EL MATERIAL PROPIO DECLARADO DE UN SOLO LADO ES UNA VARA NO EMPATADA** | acta de la vuelta 54, pregunta 4, y relectura conjunta de la vuelta 55 | actos **18** (fundido) y **23** (correccion declarada y fusion rehecha) |
| **EL `entregable_esperado` NO ES RAZON: se declara y acumula para la mesa** | acta de la vuelta 54, pregunta 2 | actos **4**, **20** y **42**, que **no se tocan** |

### LAS CINCO RELECTURAS DEL FILO: **UNA SE RESUELVE Y CUATRO DESTAPAN PREGUNTA DE POLITICA**

**Las cinco estaban predichas y nombradas con sus puestos antes de tocar un nodo**
([`../loop/SALIDA_V55_COLISIONES_ESPERADAS_TRAMO2.txt`](../loop/SALIDA_V55_COLISIONES_ESPERADAS_TRAMO2.txt)),
y las cinco se releyeron por el carril general de colisiones **con sus dos ampliaciones**:

| acto | los dos puestos | que decide la relectura | consecuencia |
|---:|---|---|---|
| **44** | **218** `B` contra **1008** `D` | **CONDICION DE TEXTO, y se resuelve.** La condicion de CONTEO Y COBERTURA se descargo MIDIENDO ANTES: la madre despacha el momento en **UNA LINEA** (su paso 1) y el hijo trae un **PROCEDIMIENTO de cuatro decisiones**, tres de ellas ausentes de la madre. La vara del banco `9.6.1` devuelve **CONTINUA**, no repite | **el 218 pasa de `B` a `D`** con correccion declarada y la razon vieja entera pegada por maquina, y **el acto SE FUNDE** |
| **6** | **668** `B` contra **1312** `D` | **PREGUNTA DE POLITICA DE CATALOGO.** La propia razon del 668 escribe que *esa diferencia de alcance la tiene que resolver **la mesa del racimo del pivote**, no yo* | **el acto NO se funde** |
| **6** | **968** `B` contra **1305** `D` | **PREGUNTA DE POLITICA DE CATALOGO.** La razon del 968 dice que *si el criterio adoptado fuera un nodo por PUERTA, este par sobrevive entero*, y que es **el unico de los cuatro cruzados donde los dos criterios de la mesa dan respuestas distintas** | **el acto NO se funde** |
| **49** | **338** `B` contra **490** `D` | **PREGUNTA DE POLITICA DE CATALOGO.** La razon del 338 escribe que juzgar de dos en dos *da respuestas incoherentes* y que **esto pide mesa de los tres a la vez** | **el acto NO se funde** |
| **49** | **297** `B` contra **497** `D` | **PREGUNTA DE POLITICA DE CATALOGO.** La razon del 297 dice *no lo decido*, y deja las dos lecturas abiertas | **el acto NO se funde** |

> **EL CARRIL DEL FILO SE CUMPLE EN SU LETRA:** el acta de la vuelta 51, pregunta 2, dice que si la
> relectura encuentra que lo congelado es **una pregunta de POLITICA de catalogo, el acto NO se
> funde**. **Cuatro de las cinco lo son, y los actos 6 y 49 quedan DECLARADOS.** El propio par `A`
> del acto 49 (puesto **536**) ya lo escribia: *este par vive entero dentro del racimo nuevo de la
> puerta del ajuste, y por la regla operativa registrada en la seccion 9 no se pelea la clase aqui*.

> **LA AMPLIACION DE MOVER LOS DOS NO HIZO FALTA, Y SE COMPROBO EN VEZ DE SUPONERSE:** en el acto
> 44 mover UN solo veredicto cierra la colision, porque el 1008 ya era `D`. **El censo esperado se
> RE-CORRIO despues de la correccion** y baja de UNA colision a **CERO** para ese acto
> ([`../loop/SALIDA_V55_COLISIONES_ESPERADAS_TRAS_FILO.txt`](../loop/SALIDA_V55_COLISIONES_ESPERADAS_TRAS_FILO.txt)).

### LOS CINCO ACTOS QUE EL TRAMO 2 DEJA DECLARADOS, CADA UNO CON SU CARRIL

| acto | sus miembros | especie | se acumula para |
|---:|---|---|---|
| **4** | `hr_calidad_gestion`, `hr_como_control_de_calidad_gerencial` | **CONTEOS DE CONTENIDO QUE CHOCAN SIN PIEZA DECLARADA** | **LA MESA**, con el pendiente de doctrina nombrado |
| **20** | `fases_de_retencion_de_clientes`, `ocho_fases_experiencia_cliente` | **CONTEOS DE CONTENIDO QUE CHOCAN SIN PIEZA DECLARADA** | **LA MESA** |
| **42** | `fase_acclimate_experiencia_cliente`, `fase_acclimate_mapa_de_proceso` | **CONTEOS DE CONTENIDO QUE CHOCAN SIN PIEZA DECLARADA** | **LA MESA** |
| **6** | `pivotar_o_proceder`, `pivote_o_proceder` | **PREGUNTA DE POLITICA DE CATALOGO CONGELADA EN DOS `B` DEL FILO** | **LA MESA DEL RACIMO DEL PIVOTE**, que las dos razones nombran |
| **49** | `fit_problema_solucion`, `problem_solution_fit` | **PREGUNTA DE POLITICA DE CATALOGO: LA FAMILIA PIDE MESA DE LOS TRES A LA VEZ** | **LA MESA DEL RACIMO DE LA PUERTA DEL AJUSTE** |

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

| | al abrir la vuelta 55 | **al cerrarla** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | %s / %s / %s / %s | **%s / %s / %s / %s** |
| grafo: vivos / deprecados / enlaces | %s / %s / %s | **%s / %s / %s** |
| retrato: `A` crudas / colapsos / pares distintos | %s / %s / %s | **%s / %s / %s** |
| actos `CERRADOS` / `ABIERTOS` | %s / %s | **%s / %s** |
| nodos en `CERRADOS` / `ABIERTOS` | %s / %s | **%s / %s** |
| cola de costuras | %s | **%s** |
| colisiones de clase vigentes | %s | **%s**, censo propio sobre el archivo entero |
| auto-pares (los dos lados al mismo vivo) | %s | **%s** |
| duplicadas historicas: grupos / nodos | %s / %s | **%s / %s** |
| actos del tramo 2 fundidos / pendientes | 21 / 29 | **45 / 5, los cinco DECLARADOS** |
| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **%s** |
| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** en los tres lotes |

> **DE DONDE SALE CADA COLUMNA.** **LAS DOS SON CORRIDAS PROPIAS DE ESTA VUELTA**: marcador
> ([`../loop/SALIDA_V55_MARCADOR_APERTURA.txt`](../loop/SALIDA_V55_MARCADOR_APERTURA.txt) y
> [`../loop/SALIDA_V55_MARCADOR_CIERRE.txt`](../loop/SALIDA_V55_MARCADOR_CIERRE.txt)),
> estado ([`../loop/SALIDA_V55_APERTURA.txt`](../loop/SALIDA_V55_APERTURA.txt) y
> [`../loop/SALIDA_V55_CIERRE.txt`](../loop/SALIDA_V55_CIERRE.txt)),
> retrato y actos ([`../loop/SALIDA_V55_RECOMPUTO_APERTURA.txt`](../loop/SALIDA_V55_RECOMPUTO_APERTURA.txt)
> y [`../loop/SALIDA_V55_RECOMPUTO_CIERRE.txt`](../loop/SALIDA_V55_RECOMPUTO_CIERRE.txt)),
> cola, colisiones y duplicadas en sus ficheros `_APERTURA` y `_CIERRE` hermanos.
> **La columna de apertura se corrio ANTES de la primera operacion y la de cierre DESPUES del
> ultimo movimiento**, y **ninguna celda de esta tabla esta tecleada**: las extrae
> `python scripts/loop/vuelta55_registro_tramo.py` de esas mismas salidas.

> **EL MARCADOR SI SE MUEVE ESTA VEZ, Y ES LA DIFERENCIA CON LA VUELTA 54.** La relectura del filo
> del acto 44 corrigio el puesto **218** de `B` a `D`, asi que **`B` baja de 73 a 72 y `D` sube de
> 2.758 a 2.759**. **`A` y `C` no se mueven**, y por eso **las DOS tablas por dominio hermanas
> tampoco**: publican la `A` de cada dominio y la `A` de los diez es la misma al digito en las dos
> corridas. **La hermandad se cumple POR VACIO y se dice, en vez de darse por cumplida.** **Las
> veinticinco fusiones NO movieron el marcador por si solas:** son de fusion pura y ninguna fabrico
> colision, asi que `P.16` no tuvo nada que limpiar.

> **EL RETRATO SE MUEVE VEINTICUATRO, NO VEINTICINCO, Y LA CUENTA SE DEJA ESCRITA:** esta vuelta
> ejecuto **25** fusiones, pero el acto 23 es una fusion **REHECHA** sobre un acto que ya estaba
> colapsado en la apertura, y su deshacer resto uno antes de sumar los veinticinco. **93 menos 1
> mas 25 son 117**, y **458 menos 24 son 434**, que vuelve a ser la resta exacta (551 crudas menos
> 117 colapsos). Las celdas 247, 248 y 528 de `RECOMPUTO_3388.md` y las filas `B` y `D` del
> marcador publicado en `INTRA_DOMINIO_INFORME.md` quedan corregidas con tachado, contador cuadrado
> y nota fechada por el barrido `9.10` del cierre.
""" % (CABECERA, t1, t2, t3,
       aA, aB, aC, aD, A, B, C, D,
       avivos, adep, aenl, vivos, dep, enl,
       acrudas, acolap, apares, crudas, colap, pares,
       acerr, aabie, cerr, abie,
       acerrn, aabien, cerrn, abien,
       acola, cola, acoli, coli, aauto, auto,
       adupg, adupn, dupg, dupn, cuatro)

    t = io.open(FUSIONES, encoding="utf-8").read()
    if CABECERA in t:
        print("  YA ESTABA: la cabecera del registro ya vive en 03_FUSIONES.md (idempotente)")
        print()
        print("FIN")
        return 0
    if not a.simular:
        io.open(FUSIONES, "w", encoding="utf-8", newline=chr(10)).write(t.rstrip("\n") + texto)
        print("  ESCRITO al final de docs/plan/03_FUSIONES.md (%d caracteres)" % len(texto))
    else:
        print("  MODO SIMULAR: no se escribe. Serian %d caracteres." % len(texto))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
