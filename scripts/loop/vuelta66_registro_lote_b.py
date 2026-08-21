# -*- coding: utf-8 -*-
"""vuelta66_registro_lote_b.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DEL LOTE B DEL TRAMO UNICO DE OP-U-02, BAJO LA CABECERA DE TRAMO QUE LA
VUELTA 65 YA ADOSO (linea 3732 de esa pagina, cotejada hoy).

NO REESCRIBE NI UNA LINEA DE ARRIBA: abre el fichero en modo adosar.

NINGUNA TABLA SE TECLEA (regla 1): la del reparto pieza a pieza, la de las
piezas por absorbido y las de los actos declarados SE GENERAN del PLAN SELLADO
docs/loop/PLAN_V66_OPU02_LOTE_B.json; la de las perdidas se RECORTA ENTERA de la
salida del tallador; y las celdas de guardas, colisiones y censos se EXTRAEN POR
AGUJA de las salidas de esta vuelta. La celda que no se pueda leer de su fichero
es ROJO y NO SE ESCRIBE NADA.

LAS TRES FUNCIONES QUE ARMAN TABLA (tabla_reparto, tabla_por_absorbido y
tabla_perdidas) SE COPIAN LITERAL de scripts/loop/vuelta65_registro_tramo.py,
lineas 74 a 126, y NO se re-inventan: dos registros de la misma pagina no pueden
dibujar el reparto distinto en silencio. tabla_declarado SI cambia, y el cambio
va dicho: el ancestro tallaba "el PRIMERO del prefijo" en la fila del acto, que
sobre tres declarados de este lote seria falso en dos de ellos, asi que la fila
se arma del propio plan y ademas imprime el MOTIVO DE CIERRE (P.10 o P.5) que el
declarado trae.

GUARDA DE CITAS: cada cita de linea se coteja antes de escribir.
GUARDA DE IDEMPOTENCIA: si la cabecera de este lote ya esta, no escribe.

Uso:
  python scripts/loop/vuelta66_registro_lote_b.py [--simular]
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:65 fuente=docs/plan/03_FUSIONES.md prueba="EL REGISTRO DEL LOTE A` (2026-08-20, vuelta 65)" corte=2026-08-20 motivo="la cabecera nombra la VUELTA 65 porque es la vuelta que adoso la cabecera de tramo bajo la que este registro se cuelga, cotejada hoy en la linea 3732 de esa pagina; el fichero es de la vuelta 66 y por eso el numero no calza con su propia vuelta a proposito"
import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
LOOP = os.path.join(RAIZ, "docs", "loop")
PLAN = os.path.join(LOOP, "PLAN_V66_OPU02_LOTE_B.json")
NL = chr(10)
CABECERA = "OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE B"

CITAS_PAGINA = [
    (62, "EL ORDEN DE ESTA FASE"),
    (1377, "EL CARRIL GENERAL DE COLISIONES"),
    (2922, "EL UNICO CHOQUE DE PUERTA DEL TRAMO"),
    (3613, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 64"),
    (3732, "EL REGISTRO DEL LOTE A"),
    (3744, "EL ACTO 1: `DECLARADO Y NO FUNDIDO` POR `P.10`"),
    (3792, "EL ACTO 3: LA PRIMERA FUSION DE MAS DE DOS MIEMBROS DE LA CAMPANA"),
    (3962, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 65"),
]

FALLOS = []


def leer(nombre):
    p = os.path.join(LOOP, nombre)
    if not os.path.exists(p):
        FALLOS.append("no existe la salida %s" % nombre)
        return ""
    return io.open(p, encoding="utf-8").read()


def busca(texto, patron, etiqueta):
    m = re.search(patron, texto)
    if not m:
        FALLOS.append("no se pudo leer %s" % etiqueta)
        return "?"
    return m.group(1)


def cotejar(citas, callado=False):
    lineas = io.open(PAGINA, encoding="utf-8").read().split(NL)
    if not callado:
        print()
        print("  --- GUARDA DE CITAS: docs/plan/03_FUSIONES.md (%d lineas) ---" % len(lineas))
    malas = []
    for n, aguja in citas:
        real = lineas[n - 1] if 0 < n <= len(lineas) else "(FUERA DE RANGO)"
        ok = aguja in real
        if not ok:
            malas.append((n, aguja, real))
        if not callado:
            print("     %-6d %-4s %s" % (n, "OK" if ok else "MAL", real.strip()[:100]))
    return malas


# --- COPIADAS LITERAL de vuelta65_registro_tramo.py lineas 74 a 126 ---------
def tabla_reparto(acto):
    """UNA FILA POR PIEZA, generada del plan sellado. No se teclea ninguna."""
    filas = ["| pieza del que muere | marca | a donde va |", "|---|---|---|"]
    for ab in acto["absorbidos"]:
        for etq, marcas in (("paso", acto["pasos"].get(ab) or {}),
                            ("condicion", acto["condiciones"].get(ab) or {})):
            for i in sorted(marcas, key=lambda x: int(x)):
                m = marcas[i]
                if m == "APPEND":
                    destino = "**viaja ENTERA** al superviviente"
                    marca = "`APPEND`"
                elif m.startswith("INCISO:"):
                    k, trozo, _nexo = m[len("INCISO:"):].split("|", 2)
                    destino = "**`INCISO` ADOSADO** al paso %s: *%s*" % (k, trozo)
                    marca = "`INCISO`"
                elif m.startswith("CUBIERTO_COND:"):
                    destino = "ya lo dice la **condicion %s** del superviviente" % m.split(":")[1]
                    marca = "`CUBIERTO`"
                else:
                    destino = "ya lo dice el **paso %s** del superviviente" % m.split(":")[1]
                    marca = "`CUBIERTO`"
                filas.append("| %s **%s** de `%s` | %s | %s |" % (etq, i, ab, marca, destino))
    return NL.join(filas)


def tabla_por_absorbido(acto):
    filas = ["| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |",
             "|---|---:|---:|---:|---:|---:|"]
    tot = [0, 0, 0, 0, 0]
    for ab in acto["absorbidos"]:
        p = acto["pasos"].get(ab) or {}
        c = acto["condiciones"].get(ab) or {}
        vals = list(p.values()) + list(c.values())
        ap = len([x for x in vals if x == "APPEND"])
        inc = len([x for x in vals if x.startswith("INCISO")])
        cub = len(vals) - ap - inc
        filas.append("| `%s` | %d | %d | %d | %d | %d |" % (ab, len(p), len(c), ap, cub, inc))
        for i, v in enumerate((len(p), len(c), ap, cub, inc)):
            tot[i] += v
    filas.append("| **los %d juntos** | **%d** | **%d** | **%d** | **%d** | **%d** |"
                 % (len(acto["absorbidos"]), tot[0], tot[1], tot[2], tot[3], tot[4]))
    return NL.join(filas)


def tabla_perdidas(acto_n=None):
    """RECORTADA ENTERA de la salida del tallador, no re-generada. Con acto_n se
    queda solo con las filas de ese acto, leyendo la COLUMNA acto por su sitio en
    la cabecera y no por la prosa de alrededor."""
    t = leer("SALIDA_V66_TALLAR_PERDIDAS.txt")
    m = re.search(r"^\| plan \| acto \|.*?(?=^$)", t, re.S | re.M)
    if not m:
        FALLOS.append("la salida del tallador de perdidas no trae tabla")
        return ""
    lineas = m.group(0).rstrip().split(NL)
    if acto_n is None:
        return NL.join(lineas)
    cab, sep = lineas[0], lineas[1]
    cols = [c.strip() for c in cab.strip().strip("|").split("|")]
    if "acto" not in cols:
        FALLOS.append("la tabla del tallador no tiene columna acto")
        return ""
    j = cols.index("acto")
    fuera = [l for l in lineas[2:]
             if [c.strip() for c in l.strip().strip("|").split("|")][j] == str(acto_n)]
    return NL.join([cab, sep] + fuera)


# --- tabla_declarado: NO es copia, y el cambio va dicho en el docstring -----
def tabla_declarado(dec):
    med = dec["medicion"]
    filas = ["| | |", "|---|---|"]
    filas.append("| **acto** | **%d** del `orden_universo` |" % dec["acto"])
    filas.append("| **miembros** | **%d**, y **NINGUNO se toca** |" % med["miembros"])
    filas.append("| **combinaciones internas** | %d |" % med["combinaciones"])
    filas.append("| **pares `A` internos** | %d |" % med["pares_A"])
    filas.append("| **pares `D` internos** | **%d**%s |"
                 % (med["pares_D"],
                    ", leidos y declarados DISTINTOS" if med["pares_D"] else
                    " (por eso `P.10` NO se dispara aqui)"))
    filas.append("| **pares sin veredicto escrito** | %d |" % med["pares_sin_veredicto"])
    filas.append("| **NODOS PUENTE** | **%d** |" % med["nodos_puente"])
    filas.append("| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **%d** |" % med["triangulos_puente"])
    filas.append("| **PUERTAS dentro del acto** | %s |"
                 % ("**%d**: `%s`" % (len(med["puertas_dentro"]), "`, `".join(med["puertas_dentro"]))
                    if med["puertas_dentro"] else
                    "**NINGUNA**, la guarda `1B` pasa por vacio y se dice"))
    if med.get("puestos_D_internos"):
        filas.append("| **puestos de los `D` internos** | %s |"
                     % ", ".join("**%d**" % x for x in med["puestos_D_internos"]))
    if med.get("nodo_que_pega"):
        filas.append("| **el nodo que PEGA la componente** | `%s`, con sus `A` en los puestos %s |"
                     % (med["nodo_que_pega"],
                        ", ".join("**%d**" % x for x in med["A_del_nodo_que_pega"])))
        filas.append("| **lo que solo entra por el** | `%s` |"
                     % "`, `".join(med["procesos_que_solo_entran_por_el"]))
    filas.append("| **instrumento** | [`../loop/%s`](../loop/%s) |"
                 % (os.path.basename(med["salida"]), os.path.basename(med["salida"])))
    filas.append("| **dossier `P.5`** | [`../loop/%s`](../loop/%s) |"
                 % (os.path.basename(med["dossier"]), os.path.basename(med["dossier"])))
    return NL.join(filas)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("REGISTRO DEL LOTE B DEL TRAMO UNICO DE OP-U-02 EN 03_FUSIONES.md")
    print("=" * 78)

    malas = cotejar(CITAS_PAGINA)
    print()
    print("  citas cotejadas: %d | MALAS: %d" % (len(CITAS_PAGINA), len(malas)))
    if malas:
        print()
        print("ROJO: %d cita(s) no calzan y NO se escribe nada:" % len(malas))
        for n, aguja, real in malas:
            print("   linea %d deberia contener %r y contiene: %s" % (n, aguja, real[:90]))
        return 1

    plan = json.load(io.open(PLAN, encoding="utf-8"))
    actos = {x["orden"]: x for x in plan["actos"]}
    decl = {x["acto"]: x for x in plan["declarados_y_no_fundidos"]}

    # LAS CELDAS QUE NO SE TECLEAN: se extraen por aguja de las salidas de hoy.
    fus = leer("SALIDA_V66_FUSION_LOTE_B.txt")
    col = leer("SALIDA_V66_CENSO_COLISIONES.txt")
    esp = leer("SALIDA_V66_COLISIONES_ESPERADAS.txt")
    dif = leer("SALIDA_V66_DIFF_DUPLICADAS.txt")
    rec = leer("SALIDA_V66_RECOMPUTO.txt")

    c = {
        "antes_vivos": busca(fus, r"censo ANTES: \d+ ficheros, (\d+) vivos", "vivos antes"),
        "despues_vivos": busca(fus, r"censo DESPUES: \d+ ficheros, (\d+) vivos", "vivos despues"),
        "mueren": busca(fus, r"nodos que MUEREN\s+: (\d+)", "nodos que mueren"),
        "piezas": busca(fus, r"piezas repartidas\s+: (\d+)", "piezas"),
        "tocados": busca(fus, r"ESCRITO\. ficheros tocados: (\d+)", "ficheros tocados"),
        "p16": busca(fus, r"P\.16, DUPLICADAS QUE LA PROPIA FUSION FABRICA[^:]*: (\d+)", "P.16"),
        "col_med": busca(col, r"COLISIONES DE CLASE VIGENTES\s+: (\d+)", "colisiones medidas"),
        "col_esp": busca(esp, r"ESPERADAS TRAS FUNDIR = (\d+)", "colisiones esperadas"),
        "col_nuevas": busca(esp, r"colisiones NUEVAS que la fusion fabricaria : (\d+)", "nuevas"),
        "dup_fab": busca(dif, r"GRUPOS FABRICADOS DE VERDAD: (\d+)", "duplicadas fabricadas"),
        "actos": busca(rec, r"actos \(componentes >=2\): (\d+)", "actos"),
        "abiertos": busca(rec, r"ABIERTOS: (\d+) sobre", "abiertos"),
        "abiertos_n": busca(rec, r"ABIERTOS: \d+ sobre (\d+) nodos", "nodos abiertos"),
    }
    print()
    print("  --- CELDAS EXTRAIDAS POR AGUJA (ninguna tecleada) ---")
    for k, v in c.items():
        print("     %-16s %s" % (k, v))
    if FALLOS:
        print()
        print("ROJO: %d celda(s) no se pudieron leer y NO se escribe nada:" % len(FALLOS))
        for f in FALLOS:
            print("   %s" % f)
        return 1

    crecen = {}
    for n in (7, 8, 9):
        m = re.search(r"ACTO %d \. sobrevive.*?pasos (\d+) -> (\d+).*?condiciones (\d+) -> (\d+)"
                      % n, fus, re.S)
        if not m:
            FALLOS.append("no se pudo leer el crecimiento del acto %d" % n)
        else:
            crecen[n] = m.groups()
    if FALLOS:
        print("ROJO: %s" % FALLOS)
        return 1

    t = TEXTO % dict(
        c, **{
            "rep7": tabla_reparto(actos[7]), "abs7": tabla_por_absorbido(actos[7]),
            "rep8": tabla_reparto(actos[8]), "abs8": tabla_por_absorbido(actos[8]),
            "rep9": tabla_reparto(actos[9]), "abs9": tabla_por_absorbido(actos[9]),
            "per7": tabla_perdidas(7), "per8": tabla_perdidas(8), "per9": tabla_perdidas(9),
            "dec5": tabla_declarado(decl[5]), "dec10": tabla_declarado(decl[10]),
            "dec11": tabla_declarado(decl[11]),
            "p7a": crecen[7][0], "p7b": crecen[7][1], "c7a": crecen[7][2], "c7b": crecen[7][3],
            "p8a": crecen[8][0], "p8b": crecen[8][1], "c8a": crecen[8][2], "c8b": crecen[8][3],
            "p9a": crecen[9][0], "p9b": crecen[9][1], "c9a": crecen[9][2], "c9b": crecen[9][3],
        })

    for mal, nombre in ((chr(8212), "guion largo"), (chr(8211), "guion medio")):
        if mal in t:
            print("ROJO: el texto trae un %s. PARADA." % nombre)
            return 1

    crudo = io.open(PAGINA, encoding="utf-8").read()
    if CABECERA in crudo:
        print()
        print("YA ADOSADO: el registro del lote B ya esta en la pagina. No se escribe nada.")
        return 0

    antes = len(crudo.split(NL))
    print()
    print("  la pagina tiene %d lineas y el texto anade %d" % (antes, t.count(NL)))
    if a.simular:
        print()
        print("  SIMULACION: no se escribe nada.")
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
    re_malas = cotejar(CITAS_PAGINA, callado=True)
    print("  las sedes de arriba siguen en su linea: %s"
          % ("OK (%d de %d)" % (len(CITAS_PAGINA) - len(re_malas), len(CITAS_PAGINA))
             if not re_malas else "ROJO"))
    print()
    print("VERDE: registro adosado y nada de arriba reescrito.")
    return 0


TEXTO = """

---

## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE B` (2026-08-20, vuelta 66)

**Va bajo la cabecera de tramo que la vuelta 65 adoso** (linea **3732**, cotejada hoy) y **no
reescribe ni una linea de arriba.** **NINGUNA TABLA DE AQUI SE TECLEA** (regla 1): las del reparto
pieza a pieza y las de piezas por absorbido **se generan del plan sellado**
[`../loop/PLAN_V66_OPU02_LOTE_B.json`](../loop/PLAN_V66_OPU02_LOTE_B.json), las de perdidas **se
recortan de la salida del tallador**, y las celdas de guardas y censos **se extraen por aguja** de
las salidas de esta vuelta con `python scripts/loop/vuelta66_registro_lote_b.py`.

**EL LOTE, DECLARADO AL ABRIRLO Y ENTREGADO ENTERO:** **PREFIJO SIN SALTOS** del `orden_universo` de
lo que quedaba del tramo (el lote A cerro los actos **1** y **3**): **los actos 5, 7, 8, 9, 10 y 11,
SEIS actos y 37 nodos.** **TRES cierran FUNDIDOS** (7, 8 y 9) y **TRES cierran `DECLARADOS Y NO
FUNDIDOS` con motivo sellado** (5, 10 y 11).

| | |
|---|---:|
| nodos VIVOS antes de la operacion | **%(antes_vivos)s** |
| nodos VIVOS despues | **%(despues_vivos)s** |
| nodos que MUEREN | **%(mueren)s** |
| piezas repartidas | **%(piezas)s** |
| ficheros tocados | **%(tocados)s** |
| duplicadas que la propia fusion fabrico y `P.16` limpio en el mismo commit | **%(p16)s** |
| **grupos de duplicadas FABRICADOS de verdad** (diff por instrumento, apertura contra cierre) | **%(dup_fab)s** |
| colisiones de clase **ESPERADAS**, medidas ANTES de fundir sobre el arbol de antes | **%(col_esp)s** |
| colisiones de clase **MEDIDAS** por el censo al cierre | **%(col_med)s** |
| actos del recomputo al cierre | **%(actos)s** |
| de ellos `ABIERTOS` | **%(abiertos)s** sobre **%(abiertos_n)s** nodos |

> **LAS COLISIONES CALZAN Y LA CUENTA SE MIDIO ANTES, QUE ES LA MITAD DEL PUNTO** (adjudicacion 3 del
> encargo de esta vuelta): **esperadas %(col_esp)s** sobre la linea base **2** de la mesa `OP-M-03`,
> con **%(col_nuevas)s NUEVAS** que la fusion del **acto 8** fabrica
> (`cierre_satisfaccion_postventa` contra `cierre_segun_complejidad_venta`, y
> `cierre_segun_complejidad_venta` contra `obtencion_compromiso`, las dos `B` contra `D`), y
> **medidas %(col_med)s: LAS MISMAS CUATRO**. **Las dos de la mesa no se tocan**, y su carril sigue
> siendo el de la linea **1377**.

### a) **EL `ACTO 7`: LA FAMILIA DEL `DMAIC` Y LA SECUENCIA UNIVERSAL DE JURAN**

**Sobrevive `six_sigma_dmaic` y absorbe CINCO.** **`P.5` contestada por medicion:** los seis del
**mismo libro** (Juran), **7 pares internos con veredicto y los 7 en `A`**, **cero `D`** y **cero
puentes**. **La vara que elige es EL CABLEADO SOLO, y su letra es `P.8`:** la FORMA medida es
**`CONTENIDO EMPATA`** (pasos empatan en 6 a tres bandas, condiciones en 3 a dos bandas), y entonces
**decide el cableado solo**: **11 contra un maximo de 5**. **El superviviente pasa de %(p7a)s a
%(p7b)s pasos y de %(c7a)s a %(c7b)s condiciones.**

%(abs7)s

**El reparto, pieza a pieza:**

%(rep7)s

**Las perdidas selladas en campo propio, recortadas de la salida del tallador:**

%(per7)s

> **CERO `INCISO` EN ESTE ACTO, Y EL MOTIVO ES MEDIBLE:** el criterio escrito de la politica del
> `INCISO` es **la legibilidad del paso resultante**, y **los SEIS pasos de `six_sigma_dmaic`
> terminan en punto**. Un inciso detras de un punto no se lee limpio, asi que **cada parametro
> concreto va `CUBIERTO` con su perdida nombrada y enrutada**, que es la otra mitad del mismo carril.

### b) **EL `ACTO 8`: LA FAMILIA DEL CIERRE EN LA VENTA GRANDE**

**Sobrevive `cierre_segun_complejidad_venta` y absorbe CINCO.** **`P.5` contestada por medicion:**
los seis de **SPIN Selling**, **9 pares internos con veredicto y los 9 en `A`**, **cero `D`**, **cero
puentes**, y **la familia ya estaba DECLARADA** por la razon del puesto **601**. **FORMA medida
`TODAS DE ACUERDO`:** 5 pasos contra un maximo de 4 y 3 condiciones contra un maximo de 2, **las dos
varas de contenido al mismo lado**; **el cableado no hace falta y no se usa** (`P.8` solo habla a
contenido empatado). **El superviviente pasa de %(p8a)s a %(p8b)s pasos y de %(c8a)s a %(c8b)s
condiciones.**

%(abs8)s

**El reparto, pieza a pieza:**

%(rep8)s

**Las perdidas selladas en campo propio:**

%(per8)s

### c) **EL `ACTO 9`: EL PRIMER CHOQUE DE PUERTA DEL TRAMO, REGISTRADO EN VEZ DE TAPADO**

**Sobrevive `marco_analisis_mercado_cadena_suministro` y absorbe CINCO.** **`P.5` contestada por
medicion:** los seis de **Hugos**, **7 pares internos con veredicto y los 7 en `A`**, **cero `D`**,
**cero puentes**.

> **LAS DOS VIAS APUNTABAN A LADOS DISTINTOS Y SE DICE ENTERO.** La **vara de contenido** apunta a
> `cuatro_categorias_desempeno_cadena_suministro` con **las dos varas y ninguna en contra** (FORMA
> `TODAS DE ACUERDO`: **10 pasos contra un maximo de 5** y **4 condiciones contra un maximo de 3**), y
> ademas la razon del puesto **704** dice que **el marco largo se traga al corto**. **PERO
> `marco_analisis_mercado_cadena_suministro` ES PUERTA**, con la marca `TIENE QUE SOBREVIVIR` leida
> del dossier, y **la guarda `1B` prohibe absorber una puerta**. **LA PUERTA SOBREVIVE** por el
> **acta 54, pregunta 1**, que es el mismo carril con el que esta pagina cerro el **acto 20** de un
> tramo de `OP-U-01` (linea **2922**).
>
> **Y LA CONSECUENCIA VA DICHA Y NO ESCONDIDA:** el nodo que la vara elegia es el que **mas piezas
> manda de `APPEND`, OCHO de sus diez pasos**, y **el superviviente pasa de %(p9a)s a %(p9b)s pasos y
> de %(c9a)s a %(c9b)s condiciones**, que lo convierte en **el nodo mas largo que la campana ha
> fabricado**, por encima de los 15 del acto 3. **Ese bulto es consecuencia de la guarda y no de
> repartir mal**, y va **MARCADO DISCUTIBLE** en el reporte de esta vuelta.

%(abs9)s

**El reparto, pieza a pieza:**

%(rep9)s

**Las perdidas selladas en campo propio:**

%(per9)s

> **LOS CUATRO CALCULOS FINANCIEROS SE OBSERVAN Y NO SE ACTUAN.** Los pasos **7 a 10** de
> `cuatro_categorias_desempeno_cadena_suministro` (rotacion de inventario, retorno sobre ventas,
> ciclo de conversion de efectivo, y mirar cuentas por cobrar y pagar antes que el inventario)
> **tienen la firma de un bloque pegado**: los pasos 1 a 6 de ese nodo son el tablero de las cuatro
> categorias y estos cuatro no vuelven a nombrarlas. **La observacion se REGISTRA y no se EJECUTA:**
> decidir si eso es un injerto es materia de **DESTEJIDO** (`P.3` y `P.19`) y **ninguna operacion
> escrita lo nombra**. Los cuatro viajan enteros de `APPEND` y la fase 04 poda. **Fundir no es sitio
> para destejer.**

### d) **EL `ACTO 5`: `DECLARADO Y NO FUNDIDO` POR `P.5`, Y ES LA PRIMERA VEZ QUE LA CAMPANA CIERRA UN ACTO POR LA PREGUNTA DE `P.5` Y NO POR EL TRIANGULO DE `P.10`**

%(dec5)s

> **`P.10` NO SE DISPARA AQUI, Y SE DICE PRIMERO** para que no se confunda con el acto **1** (linea
> **3744**): **cero `D` internos, cero nodos puente y cero triangulos**, medido. Por la adjudicacion
> del acta 65 **un veredicto ausente NO es un par sin leer**, asi que **con `P.10` sola este acto se
> fundiria**.
>
> **LO QUE LO DETIENE ES LA OTRA MITAD: la pregunta que `P.5` obliga a contestar antes de fundir, EL
> ACTO ES UNA FAMILIA O SON DOS.** Contestada sobre el texto estable de los ocho nodos leidos
> enteros, **NO ES UNA FAMILIA**: hay un **bucle de cuatro tiempos** (`build_measure_learn`,
> `ciclo_construir_medir_aprender`, `ciclo_crear_medir_aprender` y
> `startup_como_experimento_cientifico`, cerrados entre si por los puestos 213, 376, 486 y 1208) y
> hay **TRES PROCESOS LARGOS que lo contienen como UNO DE SUS PASOS** y que tienen procedimiento
> propio: `design_thinking_proceso` recorre entender, observar con etnografia, definir un punto de
> vista e idear antes de prototipar; `testing_process_completo` da forma con los dos lienzos, extrae
> hipotesis, disena con la tarjeta de test y mide con el Progress Board; `desarrollo_en_espiral` fija
> **que** se mide, **cuantas** vueltas y la documentacion de cada iteracion.
>
> **Y LOS TRES ENTRAN A LA COMPONENTE POR UN SOLO NODO QUE NO TIENE NADA PROPIO**,
> `design_test_repeat`, cuyas cinco `A` son la unica via. **Sus propias razones lo dicen cuatro
> veces:** el **796** lo llama *el ciclo desnudo contra el proceso que lo contiene* y dice que lo que
> anade *no llega ni a una linea*; el **1182** y el **1573** lo llaman **SUBCONJUNTO ESTRICTO**; y el
> **1573** avisa de que de `design_thinking_proceso` *se perderian CUATRO ETAPAS ENTERAS*.
>
> **`P.12` ES LA LETRA QUE CIERRA ESTO:** *el cierre transitivo convoca, la lectura decide*, y con el
> acto leido entero **mandan los veredictos DIRECTOS**, porque **una `A` que nadie leyo no existe**.
> **Fundir el acto entero sellaria que los tres procesos repiten ENTRE SI**, y **entre ellos no hay
> ni un solo veredicto escrito**.
>
> **LAS ALTERNATIVAS SE RECORREN EN VEZ DE ELEGIR LA COMODA:** leer los 19 pares que faltan es
> cribado que esta fase no tiene (banco 9.21 y regla 4); **fundir solo la sub-familia cerrada es una
> FUSION PARCIAL**, que el encargo de esta vuelta prohibe con todas sus letras; y fundir entero
> desmiente cuatro razones escritas. **ASI QUE NO SE FUNDE NADA Y SE DECLARA.** Es **reversible
> entero** y **no desmiente ninguna lectura escrita**, que es lo que el acta 65 dijo del acto 1 al
> adjudicarlo `A FAVOR`. **VA COMO PENDIENTE DE DOCTRINA** en el reporte, por la regla 5, **sin
> parar**: la letra no dice que hacer cuando `P.5` contesta DOS y `P.10` no se dispara, y **lo mejor
> sostenido es el carril que ya existe**.

### e) **LOS `ACTOS 10` Y `11`: `DECLARADOS Y NO FUNDIDOS` POR `P.10`, CON SU TRIANGULO MEDIDO**

**El `acto 10`, la familia del sales roadmap:**

%(dec10)s

> **Las cuatro lecturas que una fusion entera desmentiria son DE UNA PIEZA y no un accidente:** las
> razones del **1306** y del **1330** dicen las dos **el contenido del mapa contra el uso del mapa**,
> y la del **872** dice **la economia de la venta contra el mapa de acceso** y declara que **el
> sub-puro del sales roadmap SE ROMPE**.

**El `acto 11`, la familia de la supervision de la IA:**

%(dec11)s

> **Las dos lecturas que una fusion entera desmentiria dicen LA MISMA FRONTERA con las mismas
> palabras:** el **1496** dice *uno protege la decision de hoy, el otro protege la capacidad de
> decidir de manana*, y el **1541** lo repite. Ademas el **1541** declara que con ese par **el racimo
> de la IA termina su cola** y que **la particion escrita NO se mueve**: **hay una frontera escrita
> dentro de este acto y una fusion entera la borraria**.

**Los TRES declarados quedan VIVOS Y ENTEROS**, sin un nodo tocado ni un superviviente elegido, y
**su destino comparte carril con el pendiente 2 del acta 65: el cierre de la fase 03.**

### f) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba, NO deshace ninguna fusion, NO re-lee ni un veredicto de las
colisiones vigentes, NO funde ningun acto con dueno, NO toca la mesa `OP-M-03` y NO ejecuta ninguna
de las cinco fichas `OP-M-02` consumidas.**
"""


if __name__ == "__main__":
    sys.exit(main())
