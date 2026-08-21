# -*- coding: utf-8 -*-
"""vuelta65_registrar_acta64.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DE LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 64.

NO REESCRIBE NI UNA LINEA DE LAS SECCIONES DE ARRIBA: abre el fichero en modo
adosar y escribe detras. Es la via que esta pagina ya uso CINCO veces (acta 52
en la linea 1250, acta 57 sobre el acto 25 en la 2475, acta 61 en la 2689, acta
62 en la 2933 y acta 63 en la 3307).

LA GUARDA DE CITAS, heredada del registrador de la vuelta 64: ANTES de escribir,
cada cita de linea se coteja contra su fichero imprimiendo la linea citada; si
una sola no calza con la aguja que la tabla dice de ella, el instrumento cae en
ROJO y NO escribe nada. Aqui se cotejan citas de DOS ficheros, el acta y la
propia pagina de fusiones.

LA GUARDA DE IDEMPOTENCIA: si la seccion ya esta en la pagina, no se escribe
nada. Una pagina con la adjudicacion duplicada no falla, dice que si.

Uso:
  python scripts/loop/vuelta65_registrar_acta64.py [--simular]
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:64 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 64 DEL AUDITOR" corte=2026-08-20 motivo="el titulo nombra el ACTA que este registro transcribe, que es de la vuelta 64; el fichero es de la vuelta 65 y por eso el numero no calza con su propia vuelta a proposito"
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
NL = chr(10)

# (linea, aguja que esa linea TIENE que contener).
CITAS_ACTA = [
    (16655, "ACTA DE LA VUELTA 64 DEL AUDITOR"),
    (16671, "VERIFICACION POR CORRIDA PROPIA"),
    (16779, "RELECTURA CIEGA"),
    (16805, "CAIDAS DE ESTA TANDA"),
    (16808, "EJECUTOR, UNA CAIDA DE REPORTE CON NOMBRE"),
    (16819, "EJECUTOR, UNA CAIDA DE PROCEDIMIENTO AUTODECLARADA"),
    (16825, "EJECUTOR: CERO de clase y CERO de cifra publicada"),
    (16839, "ADJUDICACION DE LOS NUEVE DISCUTIBLES"),
    (16841, "D1, SELLAR EL D10 EN VEZ DE DEJARLO CUBIERTO CON SILENCIO"),
    (16851, "D2, CUBIERTO CON PERDIDA NOMBRADA EN EL PASO 1"),
    (16860, "D3, NO APILAR UN SEGUNDO INCISO EN EL PASO 5"),
    (16866, "D4, EJECUTAR DEJANDO DOS COLISIONES DE CLASE VIVAS"),
    (16876, "D5, MEDIR LA CUENTA ESPERADA DESPUES DE FUNDIR"),
    (16881, "D6, DOS INSTRUMENTOS DE NOMBRE ESTABLE ESTRENADOS"),
    (16889, "D7, NO ESTRENAR CLAVE NUEVA EN OPERACIONES.jsonl"),
    (16893, "D8, DEJAR LAS CINCO CONSUMIDAS EN ESTADO LISTA"),
    (16900, "D9, PUBLICAR LA VARA DEL INSTRUMENTO EN EL CABLEADO"),
    (16906, "LAS SIETE PREGUNTAS, CONTESTADAS SIN DOCTRINA NUEVA"),
    (16908, "EL INCISO DE CONDICIONES NO EXISTE"),
    (16914, "EL ESQUEMA DE OPERACIONES.jsonl"),
    (16916, "QUIEN RESUELVE UNA COLISION DE CLASE"),
    (16929, "LA LINEA BASE DEL CENSO PASA"),
    (16935, "LAS FUSIONES DE MESA ANTES QUE SUS MESAS"),
    (16940, "APILAR MAS DE UN INCISO SOBRE EL MISMO PASO"),
    (16947, "LA AGUJA DEL COMPROBADOR DE PROMESAS"),
    (16957, "EL SUJETO DEL CASO POSITIVO POR MEDICION"),
    (16963, "METRICA DE CREDITO ACUMULADA"),
    (16989, "Rachas: REPORTE EN UNO"),
    (16993, "CONDICIONES DE PARADA"),
]
CITAS_PAGINA = [
    (62, "EL ORDEN DE ESTA FASE"),
    (1250, "LAS TRES ADJUDICACIONES DEL ACTA DE LA VUELTA 52"),
    (1377, "EL CARRIL GENERAL DE COLISIONES"),
    (2475, "LA ADJUDICACION DEL ACTA 57 SOBRE EL **ACTO 25**"),
    (2689, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 61"),
    (2933, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 62"),
    (3307, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 63"),
    (3486, "`OP-M-03-II`: EL REGISTRO DE LA FUSION"),
]


def cotejar(ruta, citas, etq, callado=False):
    lineas = io.open(ruta, encoding="utf-8").read().split(NL)
    if not callado:
        print()
        print("  --- GUARDA DE CITAS: %s (%d lineas) ---" % (etq, len(lineas)))
    malas = []
    for n, aguja in citas:
        real = lineas[n - 1] if 0 < n <= len(lineas) else "(FUERA DE RANGO)"
        ok = aguja in real
        if not ok:
            malas.append((n, aguja, real))
        if not callado:
            print("     %-6d %-4s %s" % (n, "OK" if ok else "MAL", real.strip()[:104]))
    return malas


TEXTO = """

---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 64, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (20 ago 2026, vuelta 65, TAREA 1.a del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **CINCO** veces: las tres adjudicaciones del acta 52 (linea **1250**),
la del acta 57 sobre el acto 25 (**2475**), las del acta 61 (**2689**), las del acta 62 (**2933**) y
las del acta 63 (**3307**), **las cinco cotejadas HOY abriendo el fichero**. **Ninguna cifra
publicada se toca.** **Cada cita lleva la linea LEIDA HOY**, no recordada, y **las treinta y siete se
imprimieron y se compararon antes de escribir esta seccion** con
`python scripts/loop/vuelta65_registrar_acta64.py --simular`, que cae en `ROJO` sin escribir si una
sola no calza: el acta de la vuelta 64 abre en la linea **16655** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md), su seccion de adjudicaciones en la **16839**,
la de las siete preguntas en la **16906**, la de las caidas de la tanda en la **16805** y la de las
rachas en la **16989**.

### a) **LOS NUEVE DISCUTIBLES, ADJUDICADOS: OCHO `A FAVOR` Y EL `D5` REGISTRADO COMO CAIDA DE PROCEDIMIENTO AUTODECLARADA**

> **LA DIVERGENCIA SE DECLARA EN VEZ DE RESOLVERSE COPIANDO (regla 1 y regla 2).** El mensaje del
> commit del acta y el encargo de esta vuelta dicen los dos **NUEVE discutibles A FAVOR**, con el
> parentesis *el `D5` registrado como caida de procedimiento autodeclarada*. **El texto del acta, que
> es la vara, no adjudica el `D5` `A FAVOR`**: la linea **16876** lo abre diciendo *caida de
> procedimiento del ejecutor, autodeclarada, registrada en la seccion 3*. **Son OCHO `A FAVOR` y UNO
> registrado como caida**, y el resumen del mensaje del commit **queda entero y sin tachar** como
> contraste. **Ninguna de las dos lecturas cambia una sola cifra ni un solo dato**: el `D5` esta
> registrado en las dos, y solo cambia el rotulo con que se le nombra.

La columna de la vara **no es una glosa: es la regla citable con la que el auditor lo adjudico**, y
va copiada de su linea.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | **sello el `D10` en vez de dejarlo `CUBIERTO` con silencio** | `A FAVOR`, **y no estaba en discusion re-abrir nada: el encargo lo mandaba con todas sus letras**. La vara del **acta 55, pregunta 5** leida entera reparte `APPEND` o `CUBIERTO` **con perdida nombrada** y **no contempla el `CUBIERTO` con silencio**; la misma especie se sello dos veces el mismo dia en `OP-M-03-I`. *Anadir el sello de una mitad que muere no es re-abrir la fusion: es completar su registro por el carril escrito* | **16841** |
| **`D2`** | **marco `CUBIERTO` con perdida nombrada en el paso 1 pudiendo poner `INCISO`** | `A FAVOR`. **El criterio escrito de la politica es la LEGIBILIDAD del paso resultante**, y esta argumentada con el texto delante: el paso 1 del superviviente cierra en la subordinada de los inversores y el inciso quedaria colgando de `SUMALOS` y no de `SIENTATE`. La perdida va **nombrada y enrutada**, que es la mitad auditable que el `D9` del acta 62 exige. *Que lo decida el ojo del ejecutor con el criterio escrito y lo marque discutible es exactamente la forma debida* | **16851** |
| **`D3`** | **no apilo un segundo `INCISO` en el paso 5** | `A FAVOR`, **por el mismo criterio**: el paso 7 ya recibe el inciso del paso 4 y el apilado dejaria el paso diciendo otra cosa. La perdida (**los criterios de la decision**) va nombrada y enrutada, y **el paso se puede rehacer sin tocar el grafo** si la respuesta general fuera otra. **La regla general queda en la pregunta 5** y se registra en el apartado **c)** | **16860** |
| **`D4`** | **ejecuto dejando DOS colisiones de clase vivas** | `A FAVOR`, **con el desarrollo entero en la pregunta 3**. Las guardas obligatorias de `AUDITOR.md` seccion 3 estan TODAS verdes (cero duplicadas y cero auto-aristas tras resolver, **medidas por el auditor**); el censo es la guarda que el encargo anade y **su contrato es esperadas y CALZA, y CALZA**: esperadas 2, medidas 2, las mismas, **predichas por la fusion**. *Re-leer los cuatro puestos seria ejecutar la adjudicacion de la mesa `OP-M-03` fuera de su turno*, que es la improvisacion que la seccion 3 prohibe. **Publicar la celda en rojo en vez de esconderla es el canon de la casa** | **16866** |
| **`D5`** | **midio la cuenta esperada del censo DESPUES de fundir** | **NO es `A FAVOR`: es caida de procedimiento del ejecutor, autodeclarada**, y queda registrada en la seccion 3 del acta. **El manejo posterior fue el debido**: la simulacion se corrio sobre el arbol de ANTES de fundir y calza con la medida, asi que **no hay cifra mala publicada**. **El orden equivocado queda con nombre y no se repite: la cuenta esperada se mide ANTES** | **16876** |
| **`D6`** | **estreno DOS instrumentos de nombre estable y los uso el mismo dia** | `A FAVOR` **por el carril del `D3` del acta 63**, con las guardas comprobadas por el auditor: **las nueve muerden** sobre un sujeto que la vuelta no toco, **la guarda NUEVA de sujeto consumido muerde** sobre `OP-M-03-II`, el ancestro queda entero con su `ROJO` committeado como contraste, el heredado muerde las seis, y **el censo da cero tallados sobre 22**. *Un estreno que HACE CRECER una guarda y nace de una leccion medida es la especie buena de estreno* | **16881** |
| **`D7`** | **no estreno clave nueva en `OPERACIONES.jsonl`** | `A FAVOR`. **El esquema es pendiente de doctrina heredado** (acta 55) y **estrenar clave en 5 de 71 fichas seria decidirlo de tapadillo**; el campo `nota` es el carril que **ocho fichas ya usan**, y **las 18 claves quedaron intactas**, medido por el auditor | **16889** |
| **`D8`** | **dejo las cinco consumidas en estado `LISTA`** | `A FAVOR` **con el limite dicho**. La celda publica lo que el instrumento mide y **la divergencia (cinco de esas 71 no se pueden ejecutar) esta declarada** en el reporte y en las notas de las fichas; cambiar el estado seria **estrenar valor de esquema**, que es el mismo pendiente del `D7`. **La regla de la ficha envejecida** (acta 63, pregunta 1) **protege la ejecucion: lo consumado no se ejecuta, este como este su celda** | **16893** |
| **`D9`** | **publico la vara del instrumento en el cableado** | `A FAVOR`. **Son dos varas y no una discrepancia**, las dos medidas por el auditor (**10 contra 5** y **12 contra 6**, identicas a las publicadas), y **la publicada es la que la ficha uso**, que es el mismo manejo que el acta 63 declaro para los enlaces | **16900** |

### b) **EL CARRIL DE LAS DOS COLISIONES DE CLASE VIGENTES: LA MESA `OP-M-03` ES SU DUENA Y LA LINEA BASE DEL CENSO PASA A `2`**

**No es doctrina nueva y el acta lo dice al adjudicarla** (linea **16916**): es **extension del carril
general de colisiones**, que el acta 52 pregunta 4 adjudico y que **esta misma pagina registro en la
linea 1377** en sus dos especies (**volteo por maquina** y **relectura en el mismo acto**). **La
especie `B` contra `D` ya tiene precedente resuelto por RELECTURA EN EL MISMO ACTO**, el puesto 204.

**Lo que el acta 64 fija, y su letra:**

> **El acto al que pertenecen los puestos es material adjudicado de la mesa `OP-M-03`**: el **668**
> esta LITERAL entre sus siete dudosos y su expediente del 12 ago ya lo posiciona como *puerta contra
> acto con enlace*, el **1312** esta entre sus tres sanos, y el par de la reunion es la misma familia
> del pivote cuya serie la mesa gobierna.
>
> **La relectura en el mismo acto EXISTE como carril; su ejecutor es la operacion que es DUENA del
> acto, y su turno lo fija el `00_INDICE`.** Hasta ese turno **las dos colisiones quedan REGISTRADAS,
> VIGENTES y PUBLICADAS EN ROJO**, con **la mesa `OP-M-03` como duena nombrada**, y **NO SE TOCAN**.
>
> **LA LINEA BASE DEL CENSO DE COLISIONES PASA DE `0` A `2`, DECLARADA** (linea **16929**): **toda
> operacion siguiente corre el censo con esperadas MEDIDAS sobre esa base**, y **un delta no predicho
> por la operacion sigue siendo PARADA de guarda**.
>
> **Que la deuda crezca con `OP-M-03-III` (de 2 a 3, medido) no cambia el carril**: cambia la cuenta
> esperada de esa fusion, **que debera predecirlo en su plan**.

**Y LA CUENTA ESPERADA SE MIDE ANTES DE FUNDIR, sobre el arbol de antes**, que es la leccion del
`D5` del apartado **a)** escrita como procedimiento y no como reproche.

### c) **NO SE APILA MAS DE UN `INCISO` SOBRE EL MISMO PASO**

**Por defecto NO** (acta 64, pregunta 5, linea **16940**), **y tampoco es doctrina nueva**: sale por
**extension del criterio escrito** de la politica del `INCISO`, que es **la legibilidad del paso
resultante**, y *un segundo inciso sin coordinar la rompe*.

> **Si un caso concreto leyera limpio con dos, se ejecuta MARCADO DISCUTIBLE y el auditor lo
> adjudica**, que es el mismo camino del `D2` y el `D3`. **La perdida del paso que no lo recibe queda
> ENRUTADA y re-hacible** si el fundador un dia escribe otra letra.

### d) **LA CAIDA DE REPORTE DEL EJECUTOR, CON SU NOMBRE, Y LA RACHA EN UNO**

**Se registra aqui porque el registro no depende del acta, y porque una caida que solo vive en un
acta se olvida.** **La caida es la `7.1` del reporte de la vuelta 64** (acta, linea **16808**): el
mensaje del commit `6e1784c0` publico **tres celdas del barrido que salieron de la corrida ANTERIOR y
no de la de ese momento**. **El ejecutor la autodeclaro y el auditor la verifico EXACTA en sus dos
mitades**: el mensaje dice 417 ficheros, `ROJO` 32 y cuatro scripts sin hallazgo; **la corrida
committeada EN ESE MISMO COMMIT** dice 415 ficheros, `ROJO` 33 y `AMBAR` 2.

**Es caida de REPORTE**, no de clase ni de cifra: **vive en un mensaje de commit y no movio ningun
dato**. Se registra, **dispara la relectura al doble del tramo** (hecha) y **NO acumula para la
parada**. **LA RACHA DE REPORTE PASA DE CERO A UNO** (linea **16989**), y **tres tandas seguidas de
la misma especie serian patron y parada**. **CLASE O CIFRA sigue EN CERO**, novena tanda limpia
(linea **16825**).

### e) **LAS RESPUESTAS DE LAS PREGUNTAS 4 Y 7, REGISTRADAS Y NO ENCARGADAS**

**Se registran porque son adjudicaciones vivas que mandan sobre lo que viene, aunque no encarguen
trabajo a nadie.**

| pregunta | la respuesta del acta 64, copiada de su linea | linea |
|---|---|---:|
| **4. las fusiones de mesa ANTES que sus mesas** | **el orden es el escrito** (`00_INDICE` y campo `orden`) **y no se cambia por acta**; **el costo** (las colisiones que fabrica ejecutar las hijas antes que la madre) **queda medido y registrado**, y **la pregunta se guarda para el CIERRE DE LA FASE 03**, como la de los cinco pares con dueno del acta 63 | **16935** |
| **7. el sujeto del caso positivo elegido por medicion** | **la guarda nueva ya cae en `ROJO` si el sujeto esta consumido**, que es lo que la vuelta 64 demostro; elegirlo por medicion es **mejora del mismo instrumento por el mismo carril de sucesores, SIN URGENCIA MEDIDA**. **Queda ANOTADO, no encargado** | **16957** |

**Y las otras cinco quedan donde el acta las dejo y aqui se dice para que no parezca omision:** la
**1** (el `INCISO` de condiciones no existe) sigue en su carril escrito del acta 55 pregunta 5, con
**el costo medido y registrado** (linea **16908**); la **2** (el esquema de `OPERACIONES.jsonl`)
sigue pendiente y **el carril de la nota lo cubre** (**16914**); la **3** y la **5** se registran
enteras en los apartados **b)** y **c)** de aqui arriba; y la **6** (la aguja del comprobador de
promesas) **iba encargada** (**16947**) **y es la TAREA 1.b de la vuelta 65**, que la ensancha por
correccion declarada con caso positivo en dos mitades.

### f) **LO QUE ESTA SECCION NO HACE, dicho para que nadie se lo atribuya**

**NO toca ni una cifra publicada arriba, NO elige ningun superviviente, NO funde nada, NO deshace
ninguna fusion y NO re-lee ni un veredicto de las dos colisiones vigentes.** Registra adjudicaciones.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 64 AL FINAL DE 03_FUSIONES.md")
    print("=" * 78)

    malas = cotejar(ACTA, CITAS_ACTA, "docs/loop/ACTA_AUDITOR.md")
    malas += cotejar(PAGINA, CITAS_PAGINA, "docs/plan/03_FUSIONES.md")
    print()
    print("  citas cotejadas: %d | MALAS: %d"
          % (len(CITAS_ACTA) + len(CITAS_PAGINA), len(malas)))
    if malas:
        print()
        print("ROJO: %d cita(s) no calzan y NO se escribe nada:" % len(malas))
        for n, aguja, real in malas:
            print("   linea %d deberia contener %r y contiene: %s" % (n, aguja, real[:90]))
        return 1

    t = TEXTO
    for mal, nombre in ((chr(8212), "guion largo"), (chr(8211), "guion medio")):
        if mal in t:
            print()
            print("ROJO: el texto trae un %s. PARADA." % nombre)
            return 1

    crudo = io.open(PAGINA, encoding="utf-8").read()
    if "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 64" in crudo:
        print()
        print("YA ADOSADA: la seccion del acta 64 ya esta en la pagina. No se escribe nada.")
        return 0

    antes = len(crudo.split(NL))
    print()
    print("  la pagina tiene %d lineas y el texto anade %d" % (antes, t.count(NL)))
    if a.simular:
        print()
        print("  SIMULACION: no se escribe nada. El texto empieza asi:")
        for l in t.split(NL)[:8]:
            print("     %s" % l[:100])
        print()
        print("FIN")
        return 0

    with io.open(PAGINA, "a", encoding="utf-8", newline=NL) as fh:
        fh.write(t)
    despues = len(io.open(PAGINA, encoding="utf-8").read().split(NL))
    print()
    print("GUARDAS TRAS ESCRIBIR")
    print("  lineas antes %d, despues %d (delta %d)" % (antes, despues, despues - antes))
    txt = io.open(PAGINA, encoding="utf-8").read()
    print("  guiones largos %d, guiones medios %d"
          % (txt.count(chr(8212)), txt.count(chr(8211))))
    re_malas = cotejar(PAGINA, CITAS_PAGINA, "re-cotejo tras adosar", callado=True)
    print("  las sedes de arriba siguen en su linea: %s"
          % ("OK (%d de %d)" % (len(CITAS_PAGINA) - len(re_malas), len(CITAS_PAGINA))
             if not re_malas else "ROJO"))
    print()
    print("VERDE: registro adosado y nada de arriba reescrito.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
