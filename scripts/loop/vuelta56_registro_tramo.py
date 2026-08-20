# -*- coding: utf-8 -*-
"""vuelta56_registro_tramo.py . ESCRIBE EL REGISTRO DEL CIERRE DEL TRAMO 3 DE
OP-U-01 AL FINAL DE docs/plan/03_FUSIONES.md.

SUCESOR DECLARADO de scripts/loop/vuelta55_registro_tramo.py, cuya maquina se
copia entera: LAS TABLAS QUE RESUMEN DECISIONES NO SE TECLEAN (se pegan de la
salida del tallador) y LAS CIFRAS DEL ESTADO SE EXTRAEN POR EXPRESION REGULAR de
las salidas del dia que cada celda cita, en vez de recibirse por parametro. Una
celda tecleada es la especie de caida que las vueltas 31 y 32 pagaron.

IDEMPOTENTE: si la cabecera del registro ya esta en el fichero, no escribe.

Uso: python scripts/loop/vuelta56_registro_tramo.py [--simular]
"""
# ROTULO titulo especie=SELLO_FIJO sujeto=tramo:3 corte=2026-08-20 motivo="escribe el registro del cierre del tramo 3: sujeto fijo, sin argumento que lo repunte"
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
FUSIONES = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")

CABECERA = ("## `OP-U-01`, TRAMO 3 **ABIERTO Y CERRADO EN LA MISMA VUELTA: 47 ACTOS "
            "FUNDIDOS DE 50 Y TRES DECLARADOS** (20 ago 2026, vuelta 56)")


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
    print("EL REGISTRO DEL CIERRE DEL TRAMO 3, con cada cifra leida de su salida")
    print("=" * 78)
    print()

    fallos = []
    mc = leer("SALIDA_V56_MARCADOR_CIERRE.txt")
    A = busca(mc, r"\n  A (\d+)", "A de cierre", fallos)
    B = busca(mc, r"\n  B (\d+)", "B de cierre", fallos)
    C = busca(mc, r"\n  C (\d+)", "C de cierre", fallos)
    D = busca(mc, r"\n  D (\d+)", "D de cierre", fallos)
    ma = leer("SALIDA_V56_MARCADOR_APERTURA.txt")
    aA = busca(ma, r"\n  A (\d+)", "A de apertura", fallos)
    aB = busca(ma, r"\n  B (\d+)", "B de apertura", fallos)
    aC = busca(ma, r"\n  C (\d+)", "C de apertura", fallos)
    aD = busca(ma, r"\n  D (\d+)", "D de apertura", fallos)

    ec = leer("SALIDA_V56_CIERRE.txt")
    vivos = busca(ec, r"vivos\s+: (\d+)", "vivos de cierre", fallos)
    dep = busca(ec, r"deprecados\s+: (\d+)", "deprecados de cierre", fallos)
    enl = busca(ec, r"enlaces\s+: (\d+)", "enlaces de cierre", fallos)
    ea = leer("SALIDA_V56_APERTURA.txt")
    avivos = busca(ea, r"vivos\s+: (\d+)", "vivos de apertura", fallos)
    adep = busca(ea, r"deprecados\s+: (\d+)", "deprecados de apertura", fallos)
    aenl = busca(ea, r"enlaces\s+: (\d+)", "enlaces de apertura", fallos)

    rc = leer("SALIDA_V56_RECOMPUTO_CIERRE.txt")
    crudas = busca(rc, r"clase == 'A'\): (\d+)", "A crudas de cierre", fallos)
    colap = busca(rc, r"los dos lados\): (\d+)", "colapsos de cierre", fallos)
    pares = busca(rc, r"deduplicar\): (\d+)", "pares distintos de cierre", fallos)
    cerr = busca(rc, r"CERRADOS: (\d+) sobre", "CERRADOS de cierre", fallos)
    cerrn = busca(rc, r"CERRADOS: \d+ sobre (\d+) nodos", "nodos CERRADOS de cierre", fallos)
    abie = busca(rc, r"ABIERTOS: (\d+) sobre", "ABIERTOS de cierre", fallos)
    abien = busca(rc, r"ABIERTOS: \d+ sobre (\d+) nodos", "nodos ABIERTOS de cierre", fallos)
    cuatro = "TODAS OK" if "LAS CUATRO: TODAS OK" in rc else "NO TODAS OK"
    ra = leer("SALIDA_V56_RECOMPUTO_APERTURA.txt")
    acrudas = busca(ra, r"clase == 'A'\): (\d+)", "A crudas de apertura", fallos)
    acolap = busca(ra, r"los dos lados\): (\d+)", "colapsos de apertura", fallos)
    apares = busca(ra, r"deduplicar\): (\d+)", "pares distintos de apertura", fallos)
    acerr = busca(ra, r"CERRADOS: (\d+) sobre", "CERRADOS de apertura", fallos)
    acerrn = busca(ra, r"CERRADOS: \d+ sobre (\d+) nodos", "nodos CERRADOS de apertura", fallos)
    aabie = busca(ra, r"ABIERTOS: (\d+) sobre", "ABIERTOS de apertura", fallos)
    aabien = busca(ra, r"ABIERTOS: \d+ sobre (\d+) nodos", "nodos ABIERTOS de apertura", fallos)

    cola = busca(leer("SALIDA_V56_COLA_CIERRE.txt"), r"nodos en la cola: (\d+)", "cola de cierre", fallos)
    acola = busca(leer("SALIDA_V56_COLA_APERTURA.txt"), r"nodos en la cola: (\d+)", "cola de apertura", fallos)
    cen = leer("SALIDA_V56_COLISIONES_CIERRE.txt")
    coli = busca(cen, r"COLISIONES DE CLASE VIGENTES\s+: (\d+)", "colisiones de cierre", fallos)
    auto = busca(cen, r"AUTO-PARES \(los dos lados al mismo vivo\): (\d+)", "auto-pares de cierre", fallos)
    cena = leer("SALIDA_V56_COLISIONES_APERTURA.txt")
    acoli = busca(cena, r"COLISIONES DE CLASE VIGENTES\s+: (\d+)", "colisiones de apertura", fallos)
    aauto = busca(cena, r"AUTO-PARES \(los dos lados al mismo vivo\): (\d+)", "auto-pares de apertura", fallos)
    dup = leer("SALIDA_V56_DUPLICADAS_CIERRE.txt")
    dupg = busca(dup, r"grupos afectados \(nodo mas campo mas destino\) \| (\d+)", "grupos de duplicadas", fallos)
    dupn = busca(dup, r"nodos con al menos una duplicada\*\* \| \*\*(\d+)", "nodos con duplicadas", fallos)
    dupa = leer("SALIDA_V56_DUPLICADAS_APERTURA.txt")
    adupg = busca(dupa, r"grupos afectados \(nodo mas campo mas destino\) \| (\d+)", "grupos de apertura", fallos)
    adupn = busca(dupa, r"nodos con al menos una duplicada\*\* \| \*\*(\d+)", "nodos de apertura", fallos)

    tramo_c = leer("SALIDA_V56_TRAMO3_CIERRE.txt")
    tvivos = busca(tramo_c, r"VIVOS hoy\s+: (\d+)", "vivos del tramo al cierre", fallos)
    tfund = busca(tramo_c, r"FUNDIDOS\s+: (\d+)", "fundidos del tramo al cierre", fallos)

    tallado = leer("SALIDA_V56_TALLAR_PLANES.txt")
    perdidas = leer("SALIDA_V56_TALLAR_PERDIDAS.txt")

    def bloque(texto, desde, hasta):
        i = texto.index(desde)
        j = texto.index(hasta) if hasta else len(texto)
        cuerpo = texto[i + len(desde):j].strip("\n")
        return "\n".join(l for l in cuerpo.splitlines() if l.startswith("|"))

    try:
        t1 = bloque(tallado, "--- TABLA 1: LOS TRES LOTES, CON SUS PIEZAS ---", "--- TABLA 2")
        t2 = bloque(tallado, "--- TABLA 2: LA FORMA DEL VEREDICTO, CONTADA DE LOS MOTIVOS SELLADOS ---", "--- TABLA 3")
        t3 = bloque(tallado, "--- TABLA 3: ACTO A ACTO, SUPERVIVIENTE Y ABSORBIDO ---", "--- TABLA 4")
        t4 = bloque(tallado, "--- TABLA 4: LOS ACTOS DECLARADOS Y NO FUNDIDOS ---", "  actos tallados")
        t5 = bloque(perdidas, "--- TABLA: LAS PERDIDAS NOMBRADAS DE LA VUELTA 56, CON SU ESPECIE ---", "  actos con perdida")
    except ValueError as e:
        fallos.append("no se pudo recortar una tabla: %s" % e)
        t1 = t2 = t3 = t4 = t5 = ""

    if fallos:
        print("  ROJO, %d cifras no se pudieron leer y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("     %s" % f)
        return 1
    for k, v in [("A", A), ("B", B), ("C", C), ("D", D), ("vivos", vivos),
                 ("colapsos", colap), ("pares", pares), ("cola", cola),
                 ("tramo vivos", tvivos), ("tramo fundidos", tfund)]:
        print("  %-16s cierre: %s" % (k, v))
    print()

    texto = """

---

%s

**EL TRAMO 3 SE ABRE Y SE CIERRA EN LA MISMA VUELTA**: de sus **50** actos, **%s estan fundidos**
y **TRES quedan DECLARADOS**, cada uno con su especie escrita y su carril. Es el primer tramo de
`OP-U-01` que no necesita una segunda vuelta.

### LA FRONTERA DEL TRAMO: **LAS DOS LECTURAS NO CALZAN, Y LA DIVERGENCIA QUEDA EXPLICADA ENTERA**

**El abridor es `scripts/loop/vuelta56_tramo3_nomina.py`**
([`../loop/SALIDA_V56_TRAMO3_NOMINA.txt`](../loop/SALIDA_V56_TRAMO3_NOMINA.txt)), con la
**identidad POR MIEMBROS** copiada del sucesor de la vuelta 55 y el **ORDINAL** copiado del
ABRIDOR de la vuelta 54 (la posicion en el orden impreso de hoy). **Se dice de cual se copia cada
pieza porque no son la misma**: el sucesor derivaba el ordinal del puesto de la nomina de la 48
porque aquel tramo ya estaba abierto y sus ordinales ya estaban publicados; este tramo se ABRE hoy
y no tiene ordinal publicado que respetar.

| lo que el abridor comprueba | resultado al abrir la vuelta 56 |
|---|---|
| **guarda del prefijo**: los vivos de los tramos 1 y 2 ocupan los puestos 1 a N **sin huecos** | **SI**, y son **16**, medido y no tecleado (11 del tramo 1 y 5 del tramo 2) |
| **LECTURA A**: los 50 `CERRADOS` siguientes en el orden impreso de HOY | los puestos **17 a 66** |
| **LECTURA B**: los que ocupaban los puestos **101 a 150** de la nomina de la vuelta 48 | **50 actos**, los 50 vivos hoy |
| las dos lecturas, en conjunto y en orden | **NO CALZAN**: uno solo en A, uno solo en B |
| guarda de los cuatro ajenos, **camino literal** | **VERDE**, ninguno de los cuatro entra |
| guarda de los cuatro ajenos, **POR EL RESOLUTOR** | **MUERDE** donde el literal pasaba por vacio |
| guarda de solape con los tramos 1 y 2 | **VERDE**, CERO |
| figura de los 50 | **FUSION PURA los 50**, tamano 2 y `PURO A` |

> **LA DIVERGENCIA, DIAGNOSTICADA CON EL FICHERO DELANTE Y CON LA CADENA MEDIDA COMMIT A COMMIT.**
> **Solo en A**: `construir_sobre_ideas_ajenas` mas `reglas_brainstorming`, hoy en el puesto **23**,
> que **en la nomina de la 48 NO EXISTIA como `CERRADO`**: alli era la componente **62**, **ABIERTA
> y de tamano 3**, con `pensamiento_convergente_divergente` dentro. **Se partio cuando la vuelta 49
> corrigio el veredicto del puesto 844** (`brainstorming_divergente` contra
> `generar_multiples_opciones`) **de `A` a `D`**, por una de las tres colisiones de clase que el
> acta de la vuelta 48 mando releer: ese par resuelve a `pensamiento_convergente_divergente` contra
> `reglas_brainstorming` y **era la unica arista `A` que ataba al tercero a la componente**.
> **Solo en B**: `crecimiento_ingresos_verdes` mas `generacion_ingresos_verdes`, que ocupaba el
> puesto **150** de la 48 y hoy cae en el **67**, **UNO por detras del corte: DESPLAZADO al tramo
> siguiente, no perdido.**

> **EL TRAMO SE TOMA POR LA VARA VIGENTE Y NO SE ELIGE A OJO.** La cabecera del registro del tramo
> 1 de esta misma pagina dice desde la vuelta 48 que el tramo son *los CINCUENTA primeros actos
> CERRADOS de la NOMINA RE-MEDIDA AL ABRIRLO, en el orden en que el instrumento los imprime*, que
> es **la LECTURA A**. La lectura B no es una vara rival: es la comprobacion de que entre una
> apertura y la siguiente no ha pasado nada que el ejecutor no haya medido. **El abridor no elige:
> DIAGNOSTICA, y solo continua si toda divergencia cae en una de las dos formas explicadas** (un
> `CERRADO` nacido despues en el lado A, un acto desplazado detras del corte en el lado B).
> **Cualquier otra es ROJO y PARADA.**

> **Y LA GUARDA DE LOS CUATRO AJENOS SE LEE AHORA POR DOS CAMINOS** (regla 9 del `EJECUTOR.md`,
> `P.1`): el ajeno **`brainstorming_divergente`** esta **DEPRECADO** y vive hoy dentro del
> `ids_alias` de **`reglas_brainstorming`**, que es miembro del **acto 7**. **Por el camino LITERAL,
> que es el que corrian los abridores de los tramos 1 y 2, la guarda pasa POR VACIO y nadie se
> entera.** **EL ACTO SE FUNDIO IGUAL, Y LA VARA VA ESCRITA**: esta misma pagina midio esa guarda
> **SOBRE LAS COMPONENTES** el 19 ago 2026 y escribio que `ab_testing_optimizacion` y
> `brainstorming_divergente` *ya no aparecen en ninguna componente* porque sus operaciones
> corrieron y los deprecaron; **por esa vara escrita la guarda esta VERDE hoy tambien**. Y **la
> fusion NO TOCA AL AJENO por ningun lado**: el nodo que lleva su alias es **el que SOBREVIVE**, el
> que muere es `construir_sobre_ideas_ajenas`, y ni el id ni el alias ni la clase del ajeno cambian.

### LOS TRES LOTES, TALLADOS DE LOS PLANES SELLADOS

**Estas tablas NO estan tecleadas: salen enteras de
`python scripts/loop/vuelta56_tallar_planes.py`**
([`../loop/SALIDA_V56_TALLAR_PLANES.txt`](../loop/SALIDA_V56_TALLAR_PLANES.txt)), **que las cuenta
de los `PLAN_V56_*.json` sellados** y **cae en ROJO con el acto nombrado si un motivo no encaja en
ninguna forma conocida**.

%s

%s

%s

%s

### LAS PERDIDAS NOMBRADAS, CON SU ESPECIE SEPARADA Y LA FRASE SELLADA AL LADO

**Tampoco esta tecleada: sale entera de
`python scripts/loop/vuelta56_tallar_perdidas_v55.py --vuelta 56 --lotes A,B,C`**
([`../loop/SALIDA_V56_TALLAR_PERDIDAS.txt`](../loop/SALIDA_V56_TALLAR_PERDIDAS.txt)), **que lee la
especie del propio plan sin rama por defecto**. **Son ONCE: DIEZ de condiciones y UNA de un paso**,
y se cuentan separadas a proposito, porque mezclarlas fue la caida de reporte que el acta de la
vuelta 55 nombro.

%s

> **UN MATIZ DE LA COLUMNA DE LA CAUSA, declarado en vez de callado**: el tallador escribe una
> causa GENERICA para la especie de paso (*el inciso mentiria contra la unica restriccion del paso
> que protege*), que es la del acto 45 de la vuelta 55. **La del acto 39 de esta vuelta es de la
> misma familia pero no identica**: alli el inciso mentiria porque **contradiria el paso 2 del
> superviviente**, que manda suspender el juicio, y no porque el paso hable de *la unica*
> restriccion. **La razon exacta esta en la ultima columna, VERBATIM del plan sellado**, que es
> donde se lee sin tener que creerle a la etiqueta.

### LA UNICA COLISION PREVISTA DEL TRAMO, RESUELTA ANTES DE FUNDIR

**Las colisiones esperadas se midieron sobre EL ARCHIVO ENTERO y por PAR RESUELTO ANTES de tocar un
nodo** ([`../loop/SALIDA_V56_COLISIONES_ESPERADAS_TRAMO3.txt`](../loop/SALIDA_V56_COLISIONES_ESPERADAS_TRAMO3.txt)):
**100 combinaciones simuladas y UNA SOLA que fabrica colision.**

| acto | los dos puestos | que decide la relectura | consecuencia |
|---:|---|---|---|
| **15** | **203** `C` contra **813** `D` | **CONDICION DE TEXTO, y se resuelve.** El **203** es del FILO, asi que por el carril general NO se voltea por maquina: se relee en el mismo acto. **LA RELECTURA MUEVE EL 203 Y NO EL 813**, con tres razones medidas: su propia sustancia ya decia *niveles distintos, sano*; la FIGURA que lo hizo `C` (racimo de tres con `dso_dpo_gestion_capital_trabajo` de conjunto) **ya estaba medida del reves en el registro**, por el puesto **566** bajo el rotulo *hallazgo que corrige la lectura del puesto 203* y por la **seccion 14** del informe, que remidio el racimo a **CUATRO** miembros con `ciclo_de_conversion_de_efectivo` de **centro**; y la vara del banco `9.6.1` devuelve `D` en **los DOS hermanos** del racimo con la misma forma | **el 203 pasa de `C` a `D`** con correccion declarada y la razon vieja entera pegada por maquina, y **el acto SE FUNDE** |

> **Y NO ES PREGUNTA DE POLITICA, medido contra la marca operativa que esta misma vuelta registro**
> (acta de la vuelta 55, pregunta 1, adosada mas arriba en esta pagina): la razon del **203** **ni
> REMITE la decision a una instancia nombrada ni SE ABSTIENE**. Es una **RESERVA que una vara
> escrita resuelve**, o sea **MATIZ**, y el acto no queda bloqueado.

> **LA AMPLIACION DE MOVER LOS DOS NO HIZO FALTA, Y SE COMPROBO EN VEZ DE SUPONERSE:** mover UN
> solo veredicto cierra la colision, porque el 813 ya era `D`. **El censo esperado se RE-CORRIO
> despues de la correccion** y baja de UNA colision a **CERO**
> ([`../loop/SALIDA_V56_COLISIONES_ESPERADAS_TRAS_FILO.txt`](../loop/SALIDA_V56_COLISIONES_ESPERADAS_TRAS_FILO.txt)).

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

| | al abrir la vuelta 56 | **al cerrarla** |
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
| actos del tramo 3 fundidos / pendientes | 0 / 50 | **%s / %s, los tres DECLARADOS** |
| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **%s** |
| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** en los tres lotes |

> **DE DONDE SALE CADA COLUMNA. LAS DOS SON CORRIDAS PROPIAS DE ESTA VUELTA**, la de apertura
> **ANTES de la primera operacion** y la de cierre **DESPUES del ultimo movimiento**, y **ninguna
> celda esta tecleada**: las extrae `python scripts/loop/vuelta56_registro_tramo.py` de las
> salidas `_APERTURA` y `_CIERRE` hermanas que cada celda cita.

> **EL MARCADOR SE MUEVE EN `C` Y EN `D`, Y NO EN `A` NI EN `B`:** la relectura del filo del acto
> 15 corrigio el puesto **203** de `C` a `D`. **Las CUARENTA Y SIETE fusiones NO movieron el
> marcador por si solas**: son de fusion pura y ninguna fabrico colision, asi que `P.16` no tuvo
> nada que limpiar. **La `A` sigue en 551 y por eso las dos tablas por dominio hermanas tampoco se
> mueven**, medido y no supuesto.

> **EL RETRATO SE MUEVE CUARENTA Y SIETE, UNO POR ACTO, Y AQUI LA CUENTA SI ES EXACTA**, a
> diferencia de la vuelta 55: esta vuelta no deshizo ninguna fusion previa, asi que **117 mas 47
> son 164**, y **551 crudas menos 164 colapsos son 387**, que es la resta exacta.

> **Y UNA CIFRA QUE NO CUADRA A LA PRIMERA Y SE EXPLICA EN VEZ DE DEJARSE PASAR:** los auto-pares
> suben de **96** a **142**, o sea **46** y no 47. **Medido**: el censo cuenta **auto-pares
> DISTINTOS**, y el del **acto 7** cae sobre uno que YA EXISTIA, el de `reglas_brainstorming`, que
> hoy recoge **CUATRO** veredictos crudos distintos resueltos al mismo nodo. **Es el mismo acto 7
> del ajeno bajo el resolutor**, y por eso la cuenta baja en uno.
""" % (CABECERA, tfund, t1, t2, t3, t4, t5,
       aA, aB, aC, aD, A, B, C, D,
       avivos, adep, aenl, vivos, dep, enl,
       acrudas, acolap, apares, crudas, colap, pares,
       acerr, aabie, cerr, abie,
       acerrn, aabien, cerrn, abien,
       acola, cola, acoli, coli, aauto, auto,
       adupg, adupn, dupg, dupn, tfund, tvivos, cuatro)

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
