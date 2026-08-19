# -*- coding: utf-8 -*-
"""vuelta37_cerrar_opd04.py - REGISTRA EL ESTADO DE OP-D-04 EN LOS TRES SITIOS.

SUCESOR DECLARADO de scripts/loop/vuelta36_cerrar_opd03.py. LO QUE CAMBIA VA
DICHO (EJECUTOR.md regla 2): aquel cerraba una operacion (destejido hecho y sin
fusion, porque el acto dejo de existir); este NO CIERRA NADA. Deja los pasos 1 y
2 hechos, el acto leido entero, y la FUSION EN PARADA, que es un estado distinto
y se escribe como tal.

QUE ESCRIBE, y nada mas:
  1. docs/plan/LECTURAS_DIRIGIDAS.md: la respuesta a la pregunta de P.5 para
     OP-D-04, al final de la decima tanda.
  2. docs/plan/02_DESTEJIDOS.md: la seccion de estado de OP-D-04 con los tres
     motivos de la parada, cada uno con su medicion.
  3. docs/plan/OPERACIONES.jsonl: la nota de OP-D-04, con LA VIEJA ENTERA DENTRO
     y el campo estado SIN TOCAR (sigue en LISTA: ninguna pagina del plan define
     otro valor, y estrenar uno seria doctrina y no registro).

GUARDAS:
  - aborta si alguno de los tres trozos ya estuviera escrito (la vuelta se puede
    reintentar sin duplicar).
  - tras escribir OPERACIONES.jsonl: relee el fichero, comprueba que sigue
    teniendo el mismo numero de operaciones, que la nota vieja quedo LITERAL
    dentro de la nueva, y que estado, superviviente, nodos y eliminar de OP-D-04
    quedaron identicos.

Uso: python scripts/loop/vuelta37_cerrar_opd04.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
DES = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

MARCA = "LA RESPUESTA A LA PREGUNTA DE `P.5` PARA `OP-D-04`"

RESPUESTA = u"""

---

## LA RESPUESTA A LA PREGUNTA DE `P.5` PARA `OP-D-04`: **NO ES UNA FAMILIA DE SIETE. SON DOS TRIANGULOS CERRADOS, UN NODO COLGADO, Y TRES PUENTES**

**Con los VEINTIUN pares del acto leidos (8 del archivo mas estas 13), la pregunta de `P.5` tiene
respuesta medida y no estimada** (`scripts/loop/vuelta37_acto_opd04.py`, salida
`docs/loop/SALIDA_V37_OPD04_ACTO.txt`). **Reparto: 8 `A` y 13 `D`.**

| par | clase | de donde |
|---|:---:|---|
| `brainstorming_divergente` contra `brainstorming_efectivo` | **A** | puesto **823**, cribado, **releido por `P.5` el 19 ago 2026** |
| `brainstorming_divergente` contra `reglas_brainstorming` | **A** | puesto **834**, cribado, **releido por `P.5` el 19 ago 2026** |
| `brainstorming_divergente` contra `generar_multiples_opciones` | **A** | puesto **844**, cribado, **releido por `P.5` el 19 ago 2026** |
| `brainstorming_efectivo` contra `reglas_brainstorming` | **A** | puesto **234**, cribado |
| `brainstorming_efectivo` contra `construir_sobre_ideas_ajenas` | **A** | puesto **586**, cribado |
| `generar_multiples_opciones` contra `pensamiento_convergente_divergente` | **A** | puesto **943**, cribado |
| `pensamiento_convergente_divergente` contra `design_attitude_vs_decision_attitude` | **A** | puesto **885**, cribado |
| `generar_multiples_opciones` contra `design_attitude_vs_decision_attitude` | **A** | **`LD-93`** |
| `brainstorming_divergente` contra `pensamiento_convergente_divergente` | **D** | puesto **585**, cribado, **releido por `P.5` el 19 ago 2026** |
| las doce restantes | **D** | **`LD-83` a `LD-92`, `LD-94` y `LD-95`** |

**LAS OCHO `A` NO FORMAN UN CUMULO NI UNA CADENA: FORMAN DOS TRIANGULOS CERRADOS UNIDOS POR UN
HILO, CON UN NODO COLGANDO DE UN LADO.**

```
   EL TALLER                                 LA ALTERNANCIA
   brainstorming_divergente ---A(844)--- generar_multiples_opciones
        |         \\                              |         \\
     A(823)      A(834)                        A(943)      A(LD-93)
        |            \\                            |            \\
   brainstorming_efectivo --A(234)-- reglas_brainstorming   |    design_attitude_vs_decision_attitude
        |                                     pensamiento_convergente_divergente --A(885)--/
     A(586)
        |
   construir_sobre_ideas_ajenas
```

**LOS DOS TRIANGULOS, con todos sus pares internos en `A`, medidos y no dibujados:**

| subconjunto cerrado | sus pares internos | que es |
|---|---|---|
| `brainstorming_divergente`, `brainstorming_efectivo`, `reglas_brainstorming` | **823, 834 y 234, las tres `A`** | **EL TALLER**: como se conduce una sesion |
| `generar_multiples_opciones`, `pensamiento_convergente_divergente`, `design_attitude_vs_decision_attitude` | **943, `LD-93` y 885, las tres `A`** | **LA ALTERNANCIA**: cuando se abre y cuando se cierra |

**Y LOS DOS SUBCONJUNTOS CERRADOS QUE QUEDAN SON DE TAMANO DOS, Y SON EXACTAMENTE LOS PUENTES:**
el par **844** (`brainstorming_divergente` con `generar_multiples_opciones`), que une los dos
triangulos, y el par **586** (`brainstorming_efectivo` con `construir_sobre_ideas_ajenas`), del
que cuelga el septimo nodo.

**POR LA REGLA `P.10` HAY TRES NODOS PUENTE, Y ES EL PRIMER PUENTE TRIPLE DEL ARCHIVO:**

| puente | sus `A` | las `D` que enfrentan a sus extremos |
|---|---|---|
| **`brainstorming_divergente`** | 823, 834 y 844 | **`LD-85`** (`brainstorming_efectivo` contra `generar_multiples_opciones`) y **`LD-88`** (`reglas_brainstorming` contra `generar_multiples_opciones`) |
| **`brainstorming_efectivo`** | 823, 234 y 586 | **`LD-83`** (`brainstorming_divergente` contra `construir_sobre_ideas_ajenas`) y **`LD-89`** (`reglas_brainstorming` contra `construir_sobre_ideas_ajenas`) |
| **`generar_multiples_opciones`** | 844, 943 y `LD-93` | **`LD-84`** (`brainstorming_divergente` contra `design_attitude_vs_decision_attitude`) y **585** (`brainstorming_divergente` contra `pensamiento_convergente_divergente`) |

> **`P.10` habia nombrado el puente DOBLE y escrito lo que significa: una componente con puente
> doble no tiene un punto debil, tiene una costura. AQUI SON TRES**, y los tres son los mismos
> nodos que la operacion llama gemelos. **La componente de siete se sostiene sobre tres nodos que,
> cada uno por su lado, unen cosas que sus vecinos leen como distintas.**

**LO QUE `P.10` PROHIBE EXPRESAMENTE, y por eso no se hace:** *fundir la componente entera porque
el cierre transitivo la junta. El cierre transitivo no lee: cuenta.* **Fundir los siete
desmentiria trece lecturas `D`.**

**LO QUE `P.10` DEJA COMO SALIDA es la tercera de sus tres**, porque las dos primeras estan
agotadas: **no queda par por leer** (21 de 21) y **no queda nodo por cambiar** (el destejido esta
consumado y los siete estan estables). Queda **fundir solo el subconjunto CERRADO y enlazar el
resto**, y aqui hay **DOS** subconjuntos cerrados de tres, no uno.

> **Y AHI ES DONDE LA OPERACION SE DETIENE, y no por falta de lectura: por falta de superviviente.**
> El detalle esta en `docs/plan/02_DESTEJIDOS.md`, en la seccion de estado de `OP-D-04`.
"""

MARCA_DES = "### `OP-D-04`, ESTADO AL 19 ago 2026 (vuelta 37)"

ESTADO = u"""

---

### `OP-D-04`, ESTADO AL 19 ago 2026 (vuelta 37): **PASOS 1 Y 2 HECHOS, ACTO LEIDO ENTERO, FUSION EN PARADA**

**EL PASO 1 DEL ORDEN INTERNO ESTA HECHO Y NO LO HIZO ESTA OPERACION: lo hizo `OP-F-02`.** Medido
hoy contra el grafo y no leido de su nota (`scripts/loop/vuelta37_fuente_primero.py`, salida
`docs/loop/SALIDA_V37_OPD04_FUENTE.txt`): sus **tres nodo propio** estan vivos con 6, 5 y 4 pasos y
los tres declarados en `INDICE_ROJO_DECLARADO.jsonl`; **Mollick no aparece ya en ninguno de los
tres origenes**; y `brainstorming_divergente` entra con **una sola fuente**, Tim Brown, que es la
fijada. `OP-F-03` tambien verificada: sus **cuatro nodo propio** vivos con 4, 9, 4 y 8 pasos. **Del
cruce medido: de los siete nodos de `OP-D-04`, UNO esta en la nomina de `OP-F-02` y CERO en la de
`OP-F-03`**, asi que esa segunda dependencia es **de orden de fase y no de nodo compartido.**

**EL PASO 2, EL DESTEJIDO, ESTA CONSUMADO, Y NO POR RENUNCIA: porque su unica costura y el injerto
de fuente eran EL MISMO BLOQUE, y un solo corte sirvio a los dos frentes**
(`scripts/loop/vuelta37_destejido_opd04.py`, salida `docs/loop/SALIDA_V37_OPD04_DESTEJIDO.txt`).

| medicion de hoy | resultado |
|---|---|
| costurados del acto sobre los 128 registros de `docs/COSTURAS_INTERNAS.jsonl` | **1 de 7**, `brainstorming_divergente`; los otros seis sanos. La seccion 54.3 del informe declara 1 y 6 |
| corte registrado de esa costura | **el 5**, bloque **5 a 8** |
| frontera que `OP-F-02` publico en `01_FUENTES.md` | **1 a 4 / 5 a 8**: **el mismo sitio** |
| pasos de `brainstorming_divergente` hoy | **4**, exactamente el lado izquierdo del corte |
| los ocho pasos viejos, leidos por `git` del padre del commit de `OP-F-02` | **8**, tal como el registro de costuras dice |
| los 1 a 4 viejos contra el nodo de hoy | **4 de 4 IDENTICOS** |
| los 5 a 8 viejos contra `ideacion_con_ia_en_la_sesion` | **4 de 4 IDENTICOS**, y el destino cuelga del cableado |
| material perdido | **CERO**: 4 mas 4 igual a 8 |

> **LO QUE NO SE HIZO Y SE DICE EN VOZ ALTA: no se volvio a correr `scripts/costuras_internas.py`.**
> Ese instrumento **se declara MAL CALIBRADO en su propia salida** desde la vuelta 34
> (`docs/loop/SALIDA_V34_COSTURAS_RECALIBRADO.txt`: *INSTRUMENTO MAL CALIBRADO. No entrega nada*).
> **`OP-D-04` no necesita su cifra**: su frontera esta **publicada** en `01_FUENTES.md` y su corte
> **registrado con fecha** en `COSTURAS_INTERNAS.jsonl`. Preguntar si hoy nacio una costura que
> nadie registro seria abrir alcance que ninguna operacion escribio. **Va como discutible marcado
> del reporte, no como cifra.**

**EL PASO 3 SE PARTE EN DOS, Y SOLO LA PRIMERA MITAD SE PUDO HACER.** `P.5` manda leer el acto
entero **antes** de la fusion, y eso esta hecho: **21 de 21 pares leidos**, cuatro de ellos
releidos hoy por rancios (585, 823, 834 y 844, **ninguno cambia de clase**) y trece leidos como
lecturas dirigidas **`LD-83` a `LD-95`**. **La respuesta a la pregunta de `P.5` esta escrita entera
en `docs/plan/LECTURAS_DIRIGIDAS.md`**: no es una familia de siete, son **dos triangulos cerrados,
un nodo colgado y TRES puentes.**

**LA FUSION NO SE EJECUTA, y son TRES motivos medidos hoy, ninguno adivinado. Cero nodos tocados.**

**MOTIVO 1: NO HAY SUPERVIVIENTE, ni escrito ni deducible, y esta vez el hueco es mayor que en
`OP-D-02`.** El campo `superviviente` de `OP-D-04` esta en **`null`**, leido hoy en el fichero. Y
la especie de `9.3.1`, **con su correccion del 18 ago 2026 que manda hacer la prueba SOLO sobre los
pares `A`**, sale **POR ELEGIR** por el peor de los caminos: **de los OCHO pares `A` del acto,
CERO nombran ganador en su razon.** No es que un nodo gane unos y pierda otros: **es que no hay ni
una victoria citable de la que tirar.** Y dos de esas ocho, el **823** y el **834**, dicen
literalmente que **no se pelea la clase porque la decision ya esta tomada en otro sitio**, que es
la mesa del racimo. **`P.8` desempata a contenido empatado; aqui el contenido no ha hablado
todavia.**

**MOTIVO 2: TRES NODOS PUENTE, Y `P.10` PROHIBE FUNDIR LA COMPONENTE ENTERA.** El campo `preservar`
de la operacion habla de **el superviviente del acto**, en singular, y la medicion dice que el acto
**no puede volverse un solo nodo sin desmentir trece lecturas `D`**. La salida que `P.10` deja
(fundir solo el subconjunto cerrado y enlazar el resto) **da DOS triangulos, no uno**, y por lo
tanto **dos supervivientes y no uno**: eso **cambia la forma final de la operacion**, y la forma
final no la escribe ninguna pagina. La seccion **54.6** del informe lo dejo dicho el 11 ago 2026 y
sigue siendo cierto: *no dice si los siete nodos del brainstorming deben quedar en uno, en dos o en
cuatro; dice cuantos hay que tener delante para poder decidirlo*. **Hoy ya estan todos delante. La
decision sigue sin tomarse.**

**MOTIVO 3: EL PRIMER TRIANGULO ES UN RACIMO MIXTO AL QUE LE FALTA UN MIEMBRO, Y ESE MIEMBRO ESTA
FUERA DEL ACTO Y FUERA DEL DOMINIO.** Medido hoy en `docs/RACIMOS_MIEMBROS.jsonl`: el racimo **Las
reglas del brainstorming** tiene **CUATRO** miembros, `reglas_brainstorming`,
`brainstorming_divergente`, `brainstorming_efectivo` **y `brainstorming`, que es de `quality`**.
**Los tres primeros son exactamente el triangulo cerrado; el cuarto no esta en el acto.** Y
`docs/MESA_RACIMOS.md` escribe que este racimo es uno de los **tres mixtos** de los trece del
nucleo, con esta advertencia: *podar el lado del nucleo de un racimo mixto cambia el gradiente del
mundo que lo acompana*. **Fundir los tres aqui decidiria la forma del racimo sin su cuarto miembro
y sin su mesa.** Y `P.5` no da puerta para leerlo: su alcance adjudicado es **el acto en operacion,
nunca fuera**. **Medido tambien hoy: ninguna operacion de la fase 06 nombra a estos nodos**, asi
que esa mesa **no esta escrita como operacion**.

> **LO QUE SI QUEDA HECHO Y NO HAY QUE REPETIR:** la fuente verificada, el destejido consumado, el
> acto **leido entero por primera vez** con sus trece lecturas dirigidas nuevas, las cuatro
> relecturas de `P.5` volcadas con su correccion declarada, y **el mapa del acto medido**: dos
> triangulos, tres puentes y un nodo colgado. **Lo unico que falta para ejecutar es una decision
> sobre la forma final y sobre quien sobrevive en cada triangulo.**

**EL MARCADOR NO SE MOVIO, y esa es la prueba de que no se toco nada:** las cuatro relecturas no
cambian de clase y las trece lecturas dirigidas estan fuera de cola. **`n 3.388, A 575, B 83, C 8,
D 2.722`**, identico a la apertura de la vuelta.
"""

NOTA_NUEVA = (
    "CORRECCION DECLARADA, 19 ago 2026 (vuelta 37), y nada de lo de arriba se borra: "
    "LOS PASOS 1 Y 2 DEL ORDEN INTERNO ESTAN HECHOS Y EL ACTO ESTA LEIDO ENTERO; EL PASO 3, "
    "LA FUSION, QUEDA EN PARADA. "
    "PASO 1, LA FUENTE: hecho, y NO lo hizo esta operacion sino OP-F-02. Medido hoy contra el "
    "grafo y no leido de su nota (scripts/loop/vuelta37_fuente_primero.py): los tres nodo propio "
    "de OP-F-02 vivos con 6, 5 y 4 pasos y los tres en el indice rojo; Mollick fuera de los tres "
    "origenes; brainstorming_divergente con UNA sola fuente, Tim Brown. OP-F-03 tambien "
    "verificada, sus cuatro nodo propio vivos con 4, 9, 4 y 8 pasos. CRUCE MEDIDO: de los siete "
    "nodos de OP-D-04, UNO esta en la nomina de OP-F-02 y CERO en la de OP-F-03, asi que esa "
    "segunda dependencia es de orden de fase y no de nodo compartido. "
    "PASO 2, EL DESTEJIDO: CONSUMADO, y no por renuncia. La unica costura del acto y el injerto de "
    "fuente eran EL MISMO BLOQUE y un solo corte sirvio a los dos frentes "
    "(scripts/loop/vuelta37_destejido_opd04.py). De los siete nodos, UNO costurado y SEIS sanos "
    "sobre los 128 registros de COSTURAS_INTERNAS.jsonl; el corte registrado es el 5 y la frontera "
    "publicada por OP-F-02 es 1 a 4 / 5 a 8, el mismo sitio; los ocho pasos viejos leidos por git "
    "del padre del commit de OP-F-02 se reparten 4 y 4 IDENTICOS, cuatro en el nodo de hoy y "
    "cuatro en ideacion_con_ia_en_la_sesion, con cero material perdido. NO se volvio a correr "
    "scripts/costuras_internas.py, que se declara MAL CALIBRADO en su propia salida desde la "
    "vuelta 34: esta operacion no necesita su cifra porque su frontera esta publicada y su corte "
    "registrado con fecha. "
    "P.5, EL ACTO LEIDO ENTERO: hecho por primera vez. Pares internos posibles 21, con veredicto en "
    "el archivo 8, sin registro 13. Las trece se leyeron como lecturas dirigidas LD-83 a LD-95 "
    "(doce D y una A, la LD-93), las trece verificadas fuera de cola sobre las 3.388 filas de "
    "INTRA_DOMINIO_PARES.jsonl, asi que n no se movio. Y CUATRO pares del archivo estaban RANCIOS "
    "por las dos varas (585, 823, 834 y 844, todos por brainstorming_divergente de 8 a 4 pasos): "
    "releidos y volcados el 19 ago 2026, y NINGUNO CAMBIA DE CLASE, porque las tres razones de los "
    "gemelos habian localizado ellas mismas el solape en los pasos 1 a 4 citando el banco 9.9, o "
    "sea en el lado que la cirugia iba a dejar en pie, y acertaron las tres. "
    "LA RESPUESTA DE P.5: NO ES UNA FAMILIA DE SIETE. Son DOS TRIANGULOS CERRADOS "
    "(brainstorming_divergente con brainstorming_efectivo y reglas_brainstorming, por 823, 834 y "
    "234; y generar_multiples_opciones con pensamiento_convergente_divergente y "
    "design_attitude_vs_decision_attitude, por 943, LD-93 y 885), un NODO COLGADO "
    "(construir_sobre_ideas_ajenas, por el 586) y TRES NODOS PUENTE de P.10, que es el primer "
    "puente TRIPLE del archivo: brainstorming_divergente, brainstorming_efectivo y "
    "generar_multiples_opciones. Reparto de los 21 pares: 8 A y 13 D. "
    "PARADA DE LA FUSION, TRES MOTIVOS MEDIDOS. UNO: no hay superviviente ni escrito ni deducible; "
    "el campo sigue en null y la especie de 9.3.1, con su correccion del 18 ago 2026 que hace la "
    "prueba SOLO sobre los pares A, sale POR ELEGIR por el peor camino, porque de los OCHO pares A "
    "CERO nombran ganador, y dos de ellos (823 y 834) dicen literalmente que la clase no se pelea "
    "porque la decision vive en la mesa del racimo. DOS: tres nodos puente, y P.10 prohibe "
    "expresamente fundir la componente entera porque el cierre transitivo la junta; su tercera "
    "salida da DOS triangulos y por tanto DOS supervivientes, y la forma final de la operacion no "
    "la escribe ninguna pagina (la seccion 54.6 del informe dice desde el 11 ago 2026 que no "
    "adjudica si los siete quedan en uno, en dos o en cuatro). TRES: el primer triangulo es el "
    "racimo MIXTO Las reglas del brainstorming al que le falta su cuarto miembro, brainstorming, "
    "que es de quality y esta fuera del acto; MESA_RACIMOS.md advierte que podar el lado del "
    "nucleo de un racimo mixto cambia el gradiente del mundo que lo acompana, P.5 no da puerta "
    "para leerlo (su alcance es el acto en operacion, nunca fuera) y ninguna operacion de la fase "
    "06 nombra a estos nodos, asi que esa mesa no esta escrita. "
    "CERO NODOS TOCADOS y el marcador quieto en n 3.388, A 575, B 83, C 8, D 2.722. EL CAMPO "
    "estado SE QUEDA EN LISTA y no se toca, por el mismo motivo escrito en la nota de OP-F-02: "
    "ninguna pagina del plan define otro valor y estrenar uno seria doctrina, no registro."
)


def main():
    # 1. la respuesta de P.5
    s = io.open(LD, encoding="utf-8").read()
    if MARCA in s:
        print("YA ESTABA la respuesta de P.5 en LECTURAS_DIRIGIDAS.md: no se pisa")
        return 1
    io.open(LD, "w", encoding="utf-8", newline="\n").write(s.rstrip("\n") + "\n" + RESPUESTA)
    print("1. ESCRITA la respuesta de P.5 en docs/plan/LECTURAS_DIRIGIDAS.md")

    # 2. el estado en 02_DESTEJIDOS
    s = io.open(DES, encoding="utf-8").read()
    if MARCA_DES in s:
        print("YA ESTABA el estado en 02_DESTEJIDOS.md: no se pisa")
        return 1
    io.open(DES, "w", encoding="utf-8", newline="\n").write(s.rstrip("\n") + "\n" + ESTADO)
    print("2. ESCRITO el estado de OP-D-04 en docs/plan/02_DESTEJIDOS.md")

    # 3. la nota de la operacion
    filas = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    antes_n = len(filas)
    objetivo = None
    for o in filas:
        if o.get("id_op") == "OP-D-04":
            objetivo = o
    if objetivo is None:
        print("ABORTA: OP-D-04 no esta en OPERACIONES.jsonl")
        return 1
    vieja = objetivo["nota"]
    if "CORRECCION DECLARADA, 19 ago 2026" in vieja:
        print("YA ESTABA la nota: no se pisa")
        return 1
    guardado = {
        "estado": objetivo["estado"],
        "superviviente": objetivo["superviviente"],
        "nodos": list(objetivo["nodos"]),
        "eliminar": list(objetivo["eliminar"]),
    }
    objetivo["nota"] = vieja + " " + NOTA_NUEVA
    io.open(OPS, "w", encoding="utf-8", newline="\n").write(
        "".join(json.dumps(o, ensure_ascii=False) + "\n" for o in filas))

    rele = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    d = dict((o["id_op"], o) for o in rele)
    o4 = d["OP-D-04"]
    print("3. ESCRITA la nota de OP-D-04 en docs/plan/OPERACIONES.jsonl")
    print("")
    print("GUARDAS TRAS ESCRIBIR:")
    print("   operaciones antes/despues     : %d / %d" % (antes_n, len(rele)))
    print("   nota vieja LITERAL dentro     : %s (vieja %d car., nueva %d)"
          % (vieja in o4["nota"], len(vieja), len(o4["nota"])))
    print("   estado sin tocar              : %r == %r  -> %s"
          % (o4["estado"], guardado["estado"], o4["estado"] == guardado["estado"]))
    print("   superviviente sin tocar       : %r == %r  -> %s"
          % (o4["superviviente"], guardado["superviviente"],
             o4["superviviente"] == guardado["superviviente"]))
    print("   nodos sin tocar               : %s" % (o4["nodos"] == guardado["nodos"]))
    print("   eliminar sin tocar            : %s" % (o4["eliminar"] == guardado["eliminar"]))
    ok = (antes_n == len(rele) and vieja in o4["nota"]
          and o4["estado"] == guardado["estado"]
          and o4["superviviente"] == guardado["superviviente"]
          and o4["nodos"] == guardado["nodos"]
          and o4["eliminar"] == guardado["eliminar"])
    print("")
    print("TODAS LAS GUARDAS: %s" % ("OK" if ok else "EN ROJO"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
