# -*- coding: utf-8 -*-
"""_v63_registrar_acta62.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DE LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 62.

NO REESCRIBE NI UNA LINEA DE LAS SECCIONES DE ARRIBA: abre el fichero en modo
adosar y escribe detras. Es la via que esta pagina ya uso tres veces (acta 52 en
la linea 1250, acta 57 sobre el acto 25 en la 2475, acta 61 en la 2689).

LLEVA SU PROPIA GUARDA, y nace de un ROJO propio de la vuelta 62: cuatro de las
citas de linea de aquel registro salieron mal a la primera. Aqui, ANTES de
escribir, cada cita de linea del texto se coteja contra docs/loop/ACTA_AUDITOR.md
imprimiendo la linea citada; si alguna no calza con lo que la tabla dice de ella,
el instrumento cae en ROJO y NO escribe nada.

Uso:
  python scripts/loop/_v63_registrar_acta62.py [--simular]
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:62 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 62 DEL AUDITOR" corte=2026-08-20 motivo="el titulo nombra el ACTA que este registro transcribe, que es de la vuelta 62; el fichero es de la vuelta 63 y por eso el numero no calza con su propia vuelta a proposito"
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
NL = chr(10)

# (linea del acta, aguja que esa linea TIENE que contener). La guarda de abajo
# lo comprueba una a una antes de escribir.
CITAS = [
    (15971, "ACTA DE LA VUELTA 62 DEL AUDITOR"),
    (16071, "RELECTURA CIEGA Y RELECTURA AL DOBLE"),
    (16085, "DISCREPANCIA FUERA DEL MARCADO"),
    (16098, "CAIDAS DE ESTA TANDA"),
    (16100, "La promesa de marcado incumplida"),
    (16115, "ADJUDICACION DE LOS NUEVE DISCUTIBLES"),
    (16117, "D1, LA GUARDA QUE CRECE EN EL SUCESOR"),
    (16122, "D2, CORREGIR EL MISMO DIA LOS INSTRUMENTOS"),
    (16128, "D3, EL TRAMO ENTERO EN UNA VUELTA"),
    (16133, "D4, LA PUERTA DEL ACTO 20 CONTRA LA DOMINANCIA"),
    (16140, "D5, LOS DOS APPEND DE TRES"),
    (16148, "D6, LAS 18 PERDIDAS CONTRA LAS 4 DEL TRAMO 5"),
    (16150, "D7, EL ACTO 1 POR CONDICIONES 2 CONTRA 3"),
    (16155, "D8, EL ACTO 5 HACIA EL NODO SIN SIGUIENTES"),
    (16160, "D9, CUBIERTO CON PERDIDA SELLADA EN VEZ DE INCISO"),
    (16169, "LAS CINCO PREGUNTAS, CONTESTADAS SIN DOCTRINA NUEVA"),
    (16171, "LAS PLANTILLAS DE LOS INSTRUMENTOS ESTABLES"),
    (16183, "EL CARRIL DE LA PUERTA BASTA"),
    (16186, "NO SON COMPARABLES"),
    (16191, "SI SE PODIA CERRAR EL TRAMO ENTERO"),
    (16193, "LA SIGUIENTE OPERACION SALE DEL ORDEN YA ADJUDICADO"),
]

TEXTO = """

---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 62, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (20 ago 2026, vuelta 63, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso tres veces: las tres adjudicaciones del acta 52 (linea **1250**), la
del acta 57 sobre el acto 25 (linea **2475**) y las del acta 61 (linea **2689**), **las tres
cotejadas HOY abriendo el fichero**. **Ninguna cifra publicada se toca.** **Cada cita lleva la linea
del acta LEIDA HOY**, no recordada, y **cada una se imprimio y se comparo antes de escribir esta
seccion** con `python scripts/loop/_v63_registrar_acta62.py --simular`, que cae en `ROJO` sin
escribir si una sola no calza: el acta de la vuelta 62 abre en la linea **15971** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md), su seccion de adjudicaciones en la **16115**,
la de las cinco preguntas en la **16169** y la de las caidas en la **16098**.

### a) **LOS NUEVE DISCUTIBLES DE LA VUELTA 62, LOS NUEVE `A FAVOR`, CADA UNO CON LA VARA QUE LO SOSTIENE**

**Es la primera tanda de la campana con los NUEVE a favor y sin una sola caida de clase ni de cifra.**
La columna de la vara **no es una glosa: es la regla citable con la que el auditor lo adjudico**, y
va copiada de su linea.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | **hizo crecer una guarda en un sucesor declarado**: el generador valida las perdidas AL SELLAR, cosa que el ancestro no hacia | **acta 61, `D2` y pregunta 2**: una guarda puede crecer en un sucesor declarado **con dos condiciones**, enumerada en el docstring y marcada discutible. **Las dos se cumplieron**, y es su primera aplicacion | **16117** |
| **`D2`** | **corrigio el mismo dia dos instrumentos que cuentan las cifras de esa misma vuelta** | **la alternativa era publicar dos cifras falsas** (*50 actos mirados* y *perdidas 0*). **El contraste sobre el tramo 5 da IDENTICO al registro viejo**: la correccion **honra el conteo, no lo acomoda**, y el texto viejo queda citado entero en los dos instrumentos | **16122** |
| **`D3`** | **ejecuto el tramo entero en una vuelta** cuando el encargo pedia el lote A | **la letra del encargo lo contemplaba**: decia *entrega lo que cierre entero* y **traia ya escrito que hacer si el tramo cerraba entero**. Cerrar entero estaba DENTRO de la letra | **16128** |
| **`D4`** | **fundio el acto 20 hacia la puerta** contra la vara de contenido y contra una razon que nombraba por DOMINANCIA | **acta 54, pregunta 1**: *LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO*, y **la letra no distingue como hable el contenido**, por elegir o por dominancia. **La dominancia no se pierde: su paso viajo de `APPEND`** | **16133** |
| **`D5`** | **apendio 3 pasos en el acto 8 y 3 en el acto 18**, los dos repartos mas anchos del tramo | **cada pieza viajada es un gesto que el superviviente no hacia en ningun grado**, releido pieza a pieza por el auditor. Los supervivientes quedan en 8 y 9 pasos y **son candidatos legitimos a la poda de la fase 04, ya anotada en los planes** | **16140** |
| **`D6`** | **nombro 18 perdidas** cuando el tramo 5 entero nombro 4 | **la cifra NO es comparable entre tramos**, y por eso la comparacion no pesa. El desarrollo esta en el apartado **c)** de aqui abajo | **16148** |
| **`D7`** | **decidio el acto 1 por la cuenta de CONDICIONES** (2 contra 3) contra un cableado de 7 contra 3 | **`P.8` al pie mas acta 53 pregunta 4**: pasos 4 contra 4 empatados, condiciones la unica vara que separa, y **el cableado solo habla a contenido EMPATADO**. Cotejado por el auditor contra el arbol de apertura | **16150** |
| **`D8`** | **decidio el acto 5 igual**, por pasos 5 contra 6, **hacia un nodo con cero siguientes** | **la cantidad de cableado NO es vara adoptada**, y la objecion del grafo pobre **se disuelve midiendo**: el superviviente HEREDO el cableado del que murio y hoy tiene 2 siguientes | **16155** |
| **`D9`** | **marco `CUBIERTO` con perdida sellada en vez de `INCISO` en once sitios** | **la letra de la politica del reparto**: *de `CUBIERTO` con la perdida NOMBRADA cuando el paso resultante no se lee limpio*. **La legibilidad del paso resultante ES el criterio escrito**, y con el contrato nuevo la perdida sellada **es visible y enrutada, no un silencio** | **16160** |

> **EL LIMITE QUE EL `D9` NO CUBRE, Y VA REGISTRADO PORQUE ES LA MITAD UTIL:** marcar `CUBIERTO` con
> perdida **para ahorrarse un `INCISO` que SI cabria limpio**. En los once sitios releidos el auditor
> **no vio ese abuso**, pero la adjudicacion **no lo autoriza**.

### b) **LAS PLANTILLAS DE LOS INSTRUMENTOS ESTABLES: NO HACE FALTA VARA NUEVA, LA REGLA 1 YA LAS CUBRE POR EXTENSION** (acta 62, pregunta 1, linea **16171**)

**LA LECTURA, ENTERA Y CITABLE.** La regla 1 del ejecutor (`EL INSTRUMENTO MANDA`, en su segundo
renglon) dice que **toda cifra publicada se lee de la salida del instrumento corrido EN ESA VUELTA**
y que **una nota vieja NUNCA es fuente de una cifra nueva**. De ahi sale, sin regla nueva, que:

> **UNA PLANTILLA CON CIFRAS TALLADAS HACE DECIR AL INSTRUMENTO CIFRAS QUE NO MIDIO, o sea VIOLA LA
> REGLA 1 CADA VEZ QUE CORRE.** No es una averia del dia en que se escribio: **es una averia que se
> dispara sola en la corrida siguiente**, y por eso vive en el instrumento y no en el reporte.

**LA FORMA DEBIDA, en una linea: EL BLOQUE SE ARMA DEL INSUMO O DECLARA SU FALTA.** Es la forma que
la correccion de `registrar_cierre_de_tramo.py` ya tiene (vuelta 62) y la que la vuelta 63 le puso a
`generar_plan_del_lote.py`.

**LO QUE SE ENCARGO NO ES DOCTRINA SINO MEDICION, y esa medicion esta hecha:** el censo unico de las
plantillas de salida de los instrumentos de nombre estable, con su instrumento propio
(`scripts/loop/censo_de_plantillas_talladas.py`, de nombre estable el tambien) y su salida publicada
([`../loop/SALIDA_V63_CENSO_PLANTILLAS.txt`](../loop/SALIDA_V63_CENSO_PLANTILLAS.txt)). **Dio UN
solo `TALLADO` en los quince**, y era `generar_plan_del_lote.py`. **Queda corregido en la misma
vuelta, con el texto viejo citado entero dentro del propio fichero y con su caso positivo corrido**
([`../loop/SALIDA_V63_CASO_POSITIVO_CABECERA.txt`](../loop/SALIDA_V63_CASO_POSITIVO_CABECERA.txt)).
**El censo re-corrido despues da CERO `TALLADOS`**
([`../loop/SALIDA_V63_CENSO_PLANTILLAS_TRAS_CORREGIR.txt`](../loop/SALIDA_V63_CENSO_PLANTILLAS_TRAS_CORREGIR.txt)).

### c) **LAS PERDIDAS DE DOS TRAMOS NO SE COMPARAN SI LAS CUENTAN INSTRUMENTOS DISTINTOS** (acta 62, pregunta 3, linea **16186**; `D6`, linea **16148**)

**LA LETRA, tal como el acta la escribe:** las 18 perdidas del tramo 6 y las 4 del tramo 5 **las
cuentan instrumentos distintos**, el campo sellado contra el token en la prosa, y

> **compararlas leeria UNA MEJORA DE INSTRUMENTO COMO UN EMPEORAMIENTO DE FUSION.**

**LO QUE SI ES COMPARABLE, Y ES LA MITAD QUE HACE UTIL LA REGLA: LA SERIE POR ESPECIE, HACIA
ADELANTE.** De este tramo en adelante, **mientras el contrato `CAMPO PROPIO v1` no cambie**, las
cifras de perdidas **si se pueden poner una al lado de otra**, porque las cuenta el mismo
instrumento con la misma vara. **Hacia atras, no.**

### d) **LA CAIDA DE REPORTE DE LA VUELTA 62, REGISTRADA CON SUS SEIS SITIOS** (acta 62, seccion 3, linea **16100**; hallada en la ciega, linea **16085**)

**QUE FUE, dicho sin adorno:** seis motivos sellados de los planes del tramo 6 **prometen `VA MARCADO
COMO DISCUTIBLE`** y **la seccion 6 de aquel reporte no trae ninguno de los seis**. **CERO datos
movidos y el fondo de los seis actos re-verificado limpio** (cotejo mecanico del auditor, 21 de 21),
pero **una promesa de marcado incumplida es caida de la especie de REPORTE**, y **la racha de reporte
pasa de cero a uno**.

**LOS SITIOS, MEDIDOS Y NO RECORDADOS.** La tabla sale entera de
`python scripts/loop/_v63_sitios_promesa.py`
([`../loop/SALIDA_V63_SITIOS_PROMESA.txt`](../loop/SALIDA_V63_SITIOS_PROMESA.txt)), que busca la
frase en los dos planes sellados y la coteja contra la seccion 6 del reporte:

| acto | lote | el motivo sellado dice **en el reporte** | **cumplida** |
|---:|---|---|---|
| **5** | A | **SI** | **SI**, es el `D8` del reporte |
| **7** | A | no | **NO** |
| **9** | A | **SI** | **NO** |
| **10** | A | **SI** | **NO** |
| **12** | B | no | **NO** |
| **15** | B | no | **NO** |
| **19** | B | no | **NO** |

> **UN DATO QUE EL ACTA NO PUBLICO Y LA MEDICION DE HOY ANADE, y va aqui porque afina la caida sin
> disolverla: LAS PROMESAS ERAN SIETE, NO SEIS, Y UNA SE CUMPLIO.** El acto 5 promete con las mismas
> palabras y **si llego al reporte, como `D8`**. **Las incumplidas siguen siendo exactamente las seis
> que el acta nombra** (7, 9, 10, 12, 15 y 19), **y de ellas dos prometian ademas el sitio** (9 y 10,
> con *en el reporte* explicito). La cuenta del acta **no cambia**; lo que cambia es que ahora se
> puede ver **que la promesa a veces si se cumplia**, que es peor y no mejor para el ejecutor: **no
> era un giro de estilo que nadie honraba, era un compromiso que se honro una vez de siete**.

**LA REGLA QUE SALE DE AQUI NO ES NUEVA: ES LA REGLA 2 DEL PROTOCOLO DEL EJECUTOR LEIDA ENTERA.** Lo
que un motivo sellado prometa del reporte, **el reporte lo cumple**; y si al consolidar se decide que
un discutible del plan **no llega a la seccion 6**, el reporte **lo DICE con su motivo en vez de
callarlo**.

### e) **LAS DOS PREGUNTAS RESTANTES, REGISTRADAS SIN DESARROLLO PORQUE NO CREAN CARRIL NUEVO**

| | que contesta | linea |
|---|---|---:|
| **pregunta 2** | **el carril de la puerta BASTA aunque la razon nombre por dominancia**: la guarda **no lee el tono de la razon, restringe**, y el contenido dominante **viaja en vez de perderse**. Es el `D4` por otro lado | **16183** |
| **pregunta 4** | **si se podia cerrar el tramo entero**: la letra del encargo **lo contemplaba con su registro ya prescrito**. Es el `D3` por otro lado | **16191** |

### f) **Y LA QUINTA, QUE SI MANDA SOBRE LO QUE VIENE DESPUES: EL ORDEN NO SE ELIGE** (acta 62, pregunta 5, linea **16193**)

**Agotada `OP-U-01`, la siguiente operacion SALE DEL ORDEN YA ADJUDICADO EN LA VUELTA 47** y esta en
esta misma pagina, en la seccion **EL ORDEN DE ESTA FASE** (linea **62**), cuya tabla de desbloqueos
dejo medido el empate del puesto 1: **`OP-U-01` con 2 desbloqueos, `OP-M-03-I` con 1 y
`OP-M-02-PROG` con 0**. **Siguen, en ese orden, `OP-M-03-I` y despues `OP-M-02-PROG`**, las dos
desbloqueadas. **Despues viene el puesto 2, donde vive `OP-U-02`**, cuya apertura **se puede MEDIR
sin fundir nada**.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    acta = io.open(ACTA, encoding="utf-8").read().split(NL)
    print("=" * 78)
    print("GUARDA DE LAS CITAS DE LINEA, ANTES DE ESCRIBIR NADA")
    print("  acta: %s (%d lineas)" % (os.path.relpath(ACTA, RAIZ), len(acta)))
    print("=" * 78)
    fallos = []
    for n, aguja in CITAS:
        real = acta[n - 1] if 1 <= n <= len(acta) else "(fuera de rango)"
        ok = aguja.lower() in real.lower()
        print("  linea %-6d %-4s %s" % (n, "OK" if ok else "ROJO", real.strip()[:96]))
        if not ok:
            fallos.append("la linea %d no contiene %r" % (n, aguja))
    print()

    # TODA cita de cinco digitos que el TEXTO escriba, venga con la palabra linea
    # delante o suelta en una celda de tabla, tiene que estar en la lista de arriba.
    escritas = sorted({int(x) for x in re.findall(r"\*\*(\d{5})\*\*", TEXTO)})
    esperadas = sorted({n for n, _ in CITAS if n >= 10000})
    sobran = [x for x in escritas if x not in esperadas]
    print("  citas de cinco digitos escritas en el texto: %s" % escritas)
    print("  comprobadas por la guarda                  : %s" % esperadas)
    if sobran:
        fallos.append("el texto cita lineas que la guarda no comprobo: %s" % sobran)

    # LAS CITAS A ESTA MISMA PAGINA, comprobadas igual y contra la pagina.
    pag = io.open(PAGINA, encoding="utf-8").read().split(NL)
    print()
    print("  CITAS A 03_FUSIONES.md, comprobadas contra la pagina (%d lineas):" % len(pag))
    for n, aguja in ((62, "EL ORDEN DE ESTA FASE"),
                     (1250, "ACTA DE LA VUELTA 52"),
                     (2475, "ACTA 57"),
                     (2689, "ACTA DE LA VUELTA 61")):
        real = pag[n - 1] if 1 <= n <= len(pag) else "(fuera de rango)"
        ok = aguja.lower() in real.lower()
        print("    linea %-6d %-4s %s" % (n, "OK" if ok else "ROJO", real.strip()[:88]))
        if not ok:
            fallos.append("03_FUSIONES.md linea %d no contiene %r" % (n, aguja))

    if fallos:
        print()
        print("ROJO, %d fallo(s). NO SE ESCRIBE NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    print("  LAS %d CITAS CALZAN. " % len(CITAS))
    if a.simular:
        print()
        print("MODO SIMULAR: no se adosa nada a la pagina.")
        return 0
    antes = len(io.open(PAGINA, encoding="utf-8").read().split(NL))
    with io.open(PAGINA, "a", encoding="utf-8", newline=NL) as fh:
        fh.write(TEXTO)
    despues = len(io.open(PAGINA, encoding="utf-8").read().split(NL))
    print()
    print("ADOSADO a %s: %d lineas antes, %d despues (+%d)."
          % (os.path.relpath(PAGINA, RAIZ), antes, despues, despues - antes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
