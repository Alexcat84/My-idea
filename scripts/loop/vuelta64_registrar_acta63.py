# -*- coding: utf-8 -*-
"""vuelta64_registrar_acta63.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DE LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 63.

NO REESCRIBE NI UNA LINEA DE LAS SECCIONES DE ARRIBA: abre el fichero en modo
adosar y escribe detras. Es la via que esta pagina ya uso CUATRO veces (acta 52
en la linea 1250, acta 57 sobre el acto 25 en la 2475, acta 61 en la 2689 y acta
62 en la 2933).

LA GUARDA DE CITAS, heredada del registrador de la vuelta 63: ANTES de escribir,
cada cita de linea se coteja contra su fichero imprimiendo la linea citada; si
una sola no calza con la aguja que la tabla dice de ella, el instrumento cae en
ROJO y NO escribe nada. Aqui se cotejan citas de DOS ficheros, el acta y la
propia pagina de fusiones.

LAS DOS TABLAS SE PEGAN, NO SE TECLEAN (regla 1): la de los desbloqueos del
puesto 2 sale de scripts/loop/vuelta64_puesto2.py y la de las cinco consumidas
de scripts/loop/vuelta64_consumidas.py, las dos IMPORTADAS, no copiadas.

Uso:
  python scripts/loop/vuelta64_registrar_acta63.py [--simular]
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
NL = chr(10)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta64_puesto2 import medir as medir_puesto2, tabla_markdown as tabla_puesto2  # noqa: E402
from vuelta64_consumidas import medir as medir_consumidas, tabla_markdown as tabla_consumidas  # noqa: E402

# (fichero, linea, aguja que esa linea TIENE que contener).
CITAS_ACTA = [
    (16274, "ACTA DE LA VUELTA 63 DEL AUDITOR"),
    (16291, "VERIFICACION POR CORRIDA PROPIA"),
    (16389, "RELECTURA CIEGA"),
    (16409, "CAIDAS DE ESTA TANDA"),
    (16416, "AUDITOR, UNA CAIDA DE ACTA CON NOMBRE"),
    (16432, "ADJUDICACION DE LOS DIEZ DISCUTIBLES"),
    (16434, "D1, EXIGIR --operacion"),
    (16440, "D2, CORREGIR EL SELLADOR DOS VUELTAS SEGUIDAS"),
    (16446, "D3, DOS INSTRUMENTOS ESTABLES ESTRENADOS"),
    (16452, "D4, EJECUTAR OP-M-03-I CON LA VARA DE LA FICHA ENVEJECIDA"),
    (16457, "D5, SEGUIR P.16 CONTRA LA LETRA DE LA FICHA Y DEL ENCARGO"),
    (16464, "D6, EJECUTAR CON LAS SIMULACIONES SELLADAS DESCUADRADAS"),
    (16471, "D7, SELLAR UNA PERDIDA QUE LA FICHA NIEGA"),
    (16477, "D8, CUBIERTO CON PERDIDA SELLADA POR EL CALIFICATIVO ACCIONABLES"),
    (16483, "D9, CAMBIAR LA VARA DEL CENSO TRAS VER SU RESULTADO"),
    (16489, "D10, LA CONDICION 1 CUBIERTA SIN PERDIDA SELLADA"),
    (16502, "LAS CINCO PREGUNTAS, CONTESTADAS SIN DOCTRINA NUEVA"),
    (16504, "FICHA SELLADA CON MEDICION ENVEJECIDA"),
    (16522, "QUIEN MANDA ENTRE EL ENCARGO Y LA DOCTRINA POSTERIOR"),
    (16525, "PUEDE UN PLAN SELLAR UNA PERDIDA QUE SU FICHA NIEGA"),
    (16529, "AFINAR LA VARA ENTRE DECLARA FALTA Y MEDIDO"),
    (16534, "VALE EL INSTRUMENTO DE TRAMOS PARA OP-U-02"),
    (16547, "CINCO FUSIONES DE MESA YA CONSUMIDAS"),
    (16583, "ADJUDICACION DEL ORDEN DEL PUESTO 2"),
]
CITAS_PAGINA = [
    (62, "EL ORDEN DE ESTA FASE"),
    (64, "Lo pidio el fundador"),
    (1250, "LAS TRES ADJUDICACIONES DEL ACTA DE LA VUELTA 52"),
    (2475, "LA ADJUDICACION DEL ACTA 57 SOBRE EL **ACTO 25**"),
    (2689, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 61"),
    (2933, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 62"),
    (3161, "`OP-M-02-PROG`: EL REGISTRO DE LA FUSION"),
    (3189, "LAS PERDIDAS, SELLADAS EN CAMPO PROPIO"),
    (3193, "DE PARAMETRO DE PASO"),
]


def cotejar(ruta, citas, etq):
    lineas = io.open(ruta, encoding="utf-8").read().split(NL)
    print()
    print("  --- GUARDA DE CITAS: %s (%d lineas) ---" % (etq, len(lineas)))
    malas = []
    for n, aguja in citas:
        real = lineas[n - 1] if 0 < n <= len(lineas) else "(FUERA DE RANGO)"
        ok = aguja in real
        if not ok:
            malas.append((n, aguja, real))
        print("     %-6d %-4s %s" % (n, "OK" if ok else "MAL", real.strip()[:104]))
    return malas


def texto(t_puesto2, t_consumidas, primera):
    return """

---

## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 63, REGISTRADAS AQUI PARA QUE EL REGISTRO NO DEPENDA DEL ACTA (20 ago 2026, vuelta 64, TAREA 1 del encargo)

**Se adosan al final del documento y NO reescriben ni una linea de las secciones de arriba**, que es
la via que esta pagina ya uso **CUATRO** veces: las tres adjudicaciones del acta 52 (linea **1250**),
la del acta 57 sobre el acto 25 (**2475**), las del acta 61 (**2689**) y las del acta 62 (**2933**),
**las cuatro cotejadas HOY abriendo el fichero**. **Ninguna cifra publicada se toca.** **Cada cita
lleva la linea LEIDA HOY**, no recordada, y **las treinta y tres se imprimieron y se compararon antes
de escribir esta seccion** con `python scripts/loop/vuelta64_registrar_acta63.py --simular`, que cae
en `ROJO` sin escribir si una sola no calza: el acta de la vuelta 63 abre en la linea **16274** de
[`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md), su seccion de adjudicaciones en la **16432**,
la de las cinco preguntas en la **16502**, la del hallazgo de las consumidas en la **16547** y la
del orden del puesto 2 en la **16583**.

### a) **LOS NUEVE DISCUTIBLES ADJUDICADOS `A FAVOR`, CADA UNO CON LA VARA QUE LO SOSTIENE**

**Fueron DIEZ los marcados y NUEVE los adjudicados**: el decimo, el `D10`, quedo a **relectura
conjunta** y se resuelve en el apartado **e)** de aqui abajo. La columna de la vara **no es una
glosa: es la regla citable con la que el auditor lo adjudico**, y va copiada de su linea.

| | lo discutible, tal como el ejecutor lo marco | **la vara que lo sostiene** | linea |
|---|---|---|---:|
| **`D1`** | **exigio `--operacion` y declaro los insumos en un generador de nombre estable**, con lo que el comando viejo cae en `ROJO` | **acta 61, `D2`**, con sus dos condiciones comprobadas (docstring enumerado con nota fechada, marcado discutible). Y **que el comando viejo caiga en `ROJO` es fallar ruidoso**, canon de la casa (banco seccion 9): *un generador que sella planes no puede adivinar la operacion* | **16434** |
| **`D2`** | **corrigio el sellador dos vueltas seguidas** | **la prueba 2 del caso positivo lo mide**: la cabecera corregida da **21 y 42 IDENTICOS** a los planes ya sellados, o sea que **la correccion honra el conteo**. El riesgo de tocar el sellador es real **y la mitigacion tambien esta medida**: el censo re-corrido da cero tallados y el texto viejo queda citado entero | **16440** |
| **`D3`** | **estreno DOS instrumentos estables y los uso el mismo dia** | `fundir_por_plan.py` es **sucesor declarado POR EXTRACCION con un `assert` por cambio** (sha1 del ancestro medido por el auditor), y el caso positivo nuevo **aisla NUEVE guardas y las nueve muerden**. **La alternativa real era correr el ancestro con `OP-U-01` TALLADO en el titulo**, que es la especie que la regla 1 prohibe | **16446** |
| **`D4`** | **ejecuto `OP-M-03-I` con una ficha cuya medicion habia envejecido** | **las dos vias convergen medidas hoy**: el `CHOCAN` de las varas por forma lo decide **la pieza declarada** (acta 53, pregunta 3), que es la adjudicacion sellada, y nombra al mismo nodo. **La regla general queda escrita en el apartado b)** | **16452** |
| **`D5`** | **siguio `P.16` contra la letra de la ficha Y del encargo** | **`P.16` es posterior** (14 contra 12 de ago), **es decision del fundador**, su punto 3 hace de `OP-S-12` una verificacion de cero, y `AUDITOR.md` seccion 3 exige cero duplicadas tras resolver como guarda de la fase III. **Una linea de encargo no deroga doctrina del fundador** | **16457** |
| **`D6`** | **ejecuto con las simulaciones selladas descuadradas** | **la regla 1 leida entera**: la simulacion sellada es una nota vieja, se cita como contraste, y la de HOY se corrio y se cotejo **con las tres diferencias medidas y explicadas**, y ninguna cambia superviviente ni reparto. **Re-sellar fichas no es del ejecutor** | **16464** |
| **`D7`** | **sello una perdida que su ficha NIEGA** | el parentesis **no esta en ningun paso del superviviente de hoy**, medido sobre el json vivo, y la pasada de perdidas de la ficha es del **12 ago**, ANTERIOR al contrato `CAMPO PROPIO v1`. **La cifra de perdidas se mide contra el texto de hoy**; la afirmacion vieja se declara como contraste. **Eso no es re-abrir la ficha: es no copiarla** | **16471** |
| **`D8`** | **marco `CUBIERTO` con perdida sellada por el calificativo ACCIONABLES** | `A FAVOR` **con el limite dicho**: la perdida SELLADA es la mitad auditable y esta; el atenuante de grafo (`metricas_accionables` es nodo previo del superviviente) **es contraste medido y NO descuenta el sello**. *Una perdida con atenuante declarado es mas auditable que un silencio, no menos* | **16477** |
| **`D9`** | **cambio la vara del censo despues de ver su resultado** | `A FAVOR` **con la guarda cumplida**: la vara final es mas estrecha, **la lista `DEBIL` publica todo lo que la estrecha deja fuera**, el unico `TALLADO` de la vara nueva tambien estaba entre los once de la vieja, y **es medicion re-corrible, no doctrina**. *Lo que la salva es la publicacion de la lista `DEBIL`: sin ella seria fabricar la vara* | **16483** |

### b) **LA REGLA DE LA FICHA ENVEJECIDA**, escrita entera porque manda sobre todas las mesas que quedan

**No es doctrina nueva y el acta lo dice al adjudicarla** (linea **16504**): sale por extension
citable de **la regla 1 de `EJECUTOR.md`** (*una nota vieja NUNCA es fuente: se cita como contraste y
la discrepancia se declara*) y del **acta 53, pregunta 3** (*el `CHOCAN` lo decide la pieza
declarada*). **Su letra, tal como la vuelta 64 la aplica:**

> **Las mediciones selladas de una ficha se RE-CORREN el dia de la ejecucion.**
>
> - **Si TODAS las vias medidas hoy** (varas por forma, pieza declarada, correccion declarada si la
>   hay) **convergen en el MISMO superviviente y el MISMO reparto: SE EJECUTA**, con la divergencia
>   **declarada en el motivo** del plan.
> - **Si CUALQUIER via cambia el superviviente**, o **la pieza declarada ya no existe medida hoy**, o
>   **el objeto de la ficha ya fue consumado por otra operacion ejecutada y auditada: NO SE EJECUTA.**
>   Se trae al auditor con la medicion.
> - **Y si lo consumado es el caso, la ficha no se ejecuta ni se rehace: se declara CONSUMIDA por
>   correccion declarada** citando el registro que la consumio (carril del banco `9.10`), **porque
>   deshacer una fusion registrada y auditada seria decision de fundador.**

**Vale para las fusiones de mesa restantes con fichas del 12 ago 2026**, que son todas las que
quedan. **La vuelta 64 la aplica dos veces**: en las cinco consumidas del apartado **d)** y en
`OP-M-03-II`, cuya ejecucion re-corrio sus mediciones antes de fundir.

### c) **EL ORDEN DEL PUESTO 2 DE LA FASE 03, ADJUDICADO CON LA VARA DE LA VUELTA 47**

**Le tocaba al auditor por la decision del fundador del 19 ago 2026** (linea **64** de este mismo
documento) **y habia criterio citable**, asi que se adjudico en vez de subir a mesa. **La vara es la
general de la vuelta 47: lo que cada operacion desbloquea, escrito en el `depende_de` de las demas.**
`CONGELADOS LIBERADOS` literal **empata a las tres en cero** y por eso no separa.

**LA TABLA NO ESTA TECLEADA: sale entera de `python scripts/loop/vuelta64_puesto2.py`**
([`../loop/SALIDA_V64_PUESTO2.txt`](../loop/SALIDA_V64_PUESTO2.txt)), **que la mide de
`OPERACIONES.jsonl` en esta vuelta y no la copia del acta**:

%s

**EL PUESTO 2 QUEDA: `OP-M-02-MEDIOS`, despues `OP-M-03-II`, despues `OP-U-02`.** Y como
`OP-M-02-MEDIOS` **esta CONSUMIDA** (apartado **d**), **su resolucion es la correccion declarada y
LA PRIMERA FUSION EJECUTABLE DEL PUESTO ES `OP-M-03-II`**, que es la que esta vuelta ejecuta.
**Medido por el propio instrumento:** `%s`.

### d) **EL HALLAZGO PROPIO DEL AUDITOR: CINCO FUSIONES DE MESA YA CONSUMIDAS POR LOS TRAMOS DE `OP-U-01`, DOS CON EL SUPERVIVIENTE OPUESTO**

**El auditor lo midio con instrumento propio** (acta 63, seccion 6, linea **16547**) **y el ejecutor
lo volvio a medir por camino propio antes de escribir una sola correccion**, que es lo que el
protocolo de relectura conjunta pide. **LA TABLA SALE ENTERA de
`python scripts/loop/vuelta64_consumidas.py`**
([`../loop/SALIDA_V64_CONSUMIDAS.txt`](../loop/SALIDA_V64_CONSUMIDAS.txt)), **con los alias
resueltos por `P.1` y con las celdas de `acto`, `lote`, `sobrevive` y `absorbe` leidas POR EL NOMBRE
DE SU COLUMNA en la cabecera de cada tabla citada, nunca de la prosa de alrededor**:

%s

**LAS DOS MEDICIONES CALZAN.** La del auditor situa `OP-M-02-MEDIOS` en el tramo 3, vuelta 56, lote
B, acto 32, linea **2091**, con su perdida sellada en la **2132**; **la corrida propia da lo mismo al
digito**, y las otras cuatro quedan situadas por el mismo camino.

**LA ADJUDICACION, con las reglas ya escritas y sin estrenar ninguna:** las fusiones de los tramos
son **cosa juzgada** (planes sellados, verificadas por las actas 56 a 62); **deshacerlas seria
decision de fundador y nadie la pide**. **Las cinco fichas NO SE EJECUTAN NI SE REHACEN: se declaran
CONSUMIDAS por correccion declarada** (banco `9.10`) **en el campo `nota` de cada una**, citando el
registro del tramo que la consumio. **Y la divergencia de superviviente de `MEDIOS` y `ADMIT` se
DECLARA como contraste en vez de resolverse copiando** (regla 1): **la adjudicacion del 12 ago queda
entera y sin tachar, y lo que se declara es que NO FUE LA QUE SE EJECUTO.** **NADA DEL GRAFO SE
TOCA**: la correccion es de registro.

> **POR QUE LA CORRECCION VA EN EL CAMPO `nota` Y NO EN UNA CLAVE NUEVA, dicho para que no parezca
> descuido:** el esquema de `OPERACIONES.jsonl` es **un pendiente de doctrina heredado** (acta 55,
> seccion 5, cierre) y **estrenar clave en 5 de las 71 fichas seria decidirlo de tapadillo**. El
> campo `nota` es ademas el sitio que estas mismas fichas ya usan: `OP-F-01`, `OP-D-01`, `OP-D-03`,
> `OP-D-04`, `OP-S-06`, `OP-S-07`, `OP-C-04` y `OP-U-01` traen ahi su correccion declarada.

> **LA PREGUNTA QUE EL AUDITOR DEJO MEDIDA PERO NO CERRADA, y que se registra para que el cierre de
> la fase 03 la tenga delante:** la nomina de la vuelta 48 incluyo **cinco pares con dueno de mesa**,
> y **no hay regla escrita que mandara excluirlos de `OP-U-01`**. No es caida de nadie. Queda dicha.

### e) **`D10`, LA RELECTURA CONJUNTA: SE SELLA**

**El caso del auditor** (linea **16489**): la condicion 1 de `fases_de_retencion_de_clientes` quedo
`CUBIERTO:1` **sin perdida sellada**, y **ese mismo dia `OP-M-03-I` sello DOS perdidas `DE
CONDICIONES` por la misma especie**, el matiz del disparador que muere sin sello. **El auditor no
adjudico: mando verificar contra el grafo y decidir con la vara** del acta 55, pregunta 5.

**MEDIDO HOY sobre el json vivo** con `python scripts/loop/vuelta64_d10.py`
([`../loop/SALIDA_V64_D10.txt`](../loop/SALIDA_V64_D10.txt)):

| | el texto de HOY |
|---|---|
| **muere** (condicion 1 de `fases_de_retencion_de_clientes`) | *Cuando la empresa solo tiene procesos disenados para atraer y cerrar ventas, pero no para despues de la compra* |
| **sobrevive** (condicion 1 de `ocho_fases_experiencia_cliente`) | *Cuando el usuario necesita una estructura sistematica para gestionar la experiencia del cliente despues de la venta* |

**LA BUSQUEDA NEGATIVA SE CORRIO EN VEZ DE CITARSE** (regla 9): las **cinco** agujas del encuadre del
sintoma (*atraer*, *cerrar venta*, *cerrar la venta*, *solo tiene proceso*, *procesos dise*) salen
**AUSENTES sobre el json ENTERO del superviviente**, no solo sobre sus condiciones.

**LA DECISION: SE SELLA.** **Y el `CUBIERTO` se sostiene y no se remarca**, que es la mitad que el
auditor ya daba por buena: el disparador operativo, **el DESPUES DE LA VENTA**, esta en la condicion
1 del superviviente con todas sus letras. **Lo que se anade es el sello de la mitad que muere**, el
**encuadre del sintoma**, que es el diagnostico por el que un lector se reconoce a si mismo.

**LA VARA, leida entera** (acta 55, pregunta 5): *las perdidas de condiciones no van de `APPEND` por
defecto, y la perdida NOMBRADA es el carril mientras el pendiente del `INCISO` de condiciones siga
abierto*. **Esa vara reparte DOS marcas y no una**: `APPEND` cuando el disparador es **distinto**, y
`CUBIERTO` **con la perdida nombrada** cuando es el **mismo** disparador con un matiz que muere.
**Lo que la vara no contempla en ninguna de sus dos ramas es el `CUBIERTO` CON SILENCIO.** Y es **la
misma especie** que las dos hermanas que `OP-M-03-I` sello el mismo dia (*el mismo fenomeno sin la
pendiente*, *el mismo callejon sin la imagen*): **tratar igual lo medido igual dentro de la misma
vuelta** es la regla de trabajo **declarada y uniforme** del acta 55, pregunta 4.

> **CORRECCION DECLARADA (2026-08-20, vuelta 64, TAREA 1.b del encargo, por el carril del banco
> `9.10`; el texto viejo se queda entero y no se tacha).** **La seccion `LAS PERDIDAS, SELLADAS EN
> CAMPO PROPIO` del registro de `OP-M-02-PROG` (linea 3189) publica UNA sola fila, la `DE PARAMETRO
> DE PASO` de la linea 3193. HOY SON DOS.** La segunda es **`DE CONDICIONES`**, vive en la
> **condicion 1 de `fases_de_retencion_de_clientes`** y va **enrutada a la fase 04, mientras el
> `INCISO` de condiciones no exista**. **La fila vieja no se toca y la tabla de arriba no se
> reescribe: esta nota la corrige.** El sello esta ademas en el campo `perdidas` del plan
> ([`../loop/PLAN_V63_OPM02PROG.json`](../loop/PLAN_V63_OPM02PROG.json)), con su correccion declarada
> adosada a `nota_del_reparto` **citando verbatim la frase que decia lo contrario**, y el tallador lo
> confirma por maquina: `python scripts/loop/tallar_perdidas_del_plan.py --plan ...` da **5 perdidas
> nombradas en los dos planes de la vuelta 63** (**3 `DE CONDICIONES`, 2 `DE PARAMETRO DE PASO`**),
> donde antes daba 4 ([`../loop/SALIDA_V64_TALLAR_PERDIDAS_V63.txt`](../loop/SALIDA_V64_TALLAR_PERDIDAS_V63.txt)).

### f) **LA CAIDA DE ACTA DEL AUDITOR, REGISTRADA CON SU NOMBRE**

**No se registra solo lo del ejecutor, y por eso esta aqui** (acta 63, seccion 3, linea **16416**).
**El encargo que el acta 62 dejo escrito decia con todas sus letras que en `OP-M-02-PROG` la
duplicada que la fusion fabrica quedaba para `OP-S-12`**, repitiendo la letra de una ficha del 12 ago
que **`P.16` (decision del fundador, 14 ago) contradice**; y **el MISMO encargo pedia en otra linea
el diff de duplicadas con CERO fabricadas**. **El ejecutor resolvio bien** (es el `D5` del apartado
**a**) **y ningun dato se movio**, pero **la linea era un error del encargo**. **Las caidas de acta
del auditor pasan de 5 a 6.**

**LO QUE ESTA SECCION NO HACE, dicho para que nadie se lo atribuya: NO toca ni una cifra publicada
arriba, NO elige ningun superviviente, NO funde nada y NO deshace ninguna fusion.** Registra
adjudicaciones y corrige por declaracion.
""" % (t_puesto2, primera, t_consumidas)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 63 AL FINAL DE 03_FUSIONES.md")
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

    fp2, _ = medir_puesto2()
    fc, fallos, _ = medir_consumidas()
    if fallos:
        print()
        print("ROJO: la medicion de las consumidas trae fallos y NO se escribe nada:")
        for x in fallos:
            print("   %s" % x)
        return 1
    ejecutables = [f for f in fp2 if not f["consumida"]]
    if not ejecutables:
        print()
        print("ROJO: no queda ejecutable en el puesto 2. PARADA.")
        return 1
    primera = ejecutables[0]["id_op"]
    t = texto(tabla_puesto2(fp2), tabla_consumidas(fc), primera)

    for mal, nombre in ((chr(8212), "guion largo"), (chr(8211), "guion medio")):
        if mal in t:
            print()
            print("ROJO: el texto trae un %s. PARADA." % nombre)
            return 1

    # GUARDA DE IDEMPOTENCIA: adosar dos veces publicaria la misma seccion dos
    # veces, y una pagina con la adjudicacion duplicada no falla, dice que si.
    crudo = io.open(PAGINA, encoding="utf-8").read()
    if "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 63" in crudo:
        print()
        print("YA ADOSADA: la seccion del acta 63 ya esta en la pagina. No se escribe nada.")
        return 0

    antes = len(crudo.split(NL))
    print()
    print("  la pagina tiene %d lineas y el texto anade %d" % (antes, t.count(NL)))
    print("  la primera ejecutable del puesto 2, medida: %s" % primera)
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
    print("  las cuatro sedes de arriba siguen en su linea: %s"
          % ("OK" if not cotejar(PAGINA, CITAS_PAGINA, "re-cotejo tras adosar") else "ROJO"))
    print()
    print("VERDE: registro adosado y nada de arriba reescrito.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
