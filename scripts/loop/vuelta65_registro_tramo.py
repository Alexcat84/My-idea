# -*- coding: utf-8 -*-
"""vuelta65_registro_tramo.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DEL LOTE A DEL TRAMO UNICO DE OP-U-02, BAJO SU CABECERA DE TRAMO.

NO REESCRIBE NI UNA LINEA DE ARRIBA: abre el fichero en modo adosar.

NINGUNA TABLA SE TECLEA (regla 1): la del reparto, la de las piezas por
absorbido, la de las perdidas y la del acto declarado SE GENERAN del PLAN
SELLADO docs/loop/PLAN_V65_OPU02_LOTE_A.json, y las cifras de guardas se
EXTRAEN por aguja de las salidas selladas de la vuelta. La celda que no se pueda
leer de su fichero es ROJO y NO SE ESCRIBE NADA.

GUARDA DE CITAS: cada cita de linea se coteja antes de escribir.
GUARDA DE IDEMPOTENCIA: si la cabecera del tramo ya esta, no escribe.

Uso:
  python scripts/loop/vuelta65_registro_tramo.py [--simular]
"""
import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
LOOP = os.path.join(RAIZ, "docs", "loop")
PLAN = os.path.join(LOOP, "PLAN_V65_OPU02_LOTE_A.json")
NL = chr(10)
CABECERA = "OP-U-02, TRAMO UNICO Y FINAL POR AGOTAMIENTO: EL REGISTRO DEL LOTE A"

CITAS_PAGINA = [
    (62, "EL ORDEN DE ESTA FASE"),
    (1377, "EL CARRIL GENERAL DE COLISIONES"),
    (3307, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 63"),
    (3486, "`OP-M-03-II`: EL REGISTRO DE LA FUSION"),
    (3613, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 64"),
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


def cotejar(citas):
    lineas = io.open(PAGINA, encoding="utf-8").read().split(NL)
    print()
    print("  --- GUARDA DE CITAS: docs/plan/03_FUSIONES.md (%d lineas) ---" % len(lineas))
    malas = []
    for n, aguja in citas:
        real = lineas[n - 1] if 0 < n <= len(lineas) else "(FUERA DE RANGO)"
        ok = aguja in real
        if not ok:
            malas.append((n, aguja, real))
        print("     %-6d %-4s %s" % (n, "OK" if ok else "MAL", real.strip()[:100]))
    return malas


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


def tabla_perdidas():
    """RECORTADA ENTERA de la salida del tallador, no re-generada."""
    t = leer("SALIDA_V65_TALLAR_PERDIDAS.txt")
    m = re.search(r"^\| plan \| acto \|.*?(?=^$)", t, re.S | re.M)
    if not m:
        FALLOS.append("la salida del tallador de perdidas no trae tabla")
        return ""
    return m.group(0).rstrip()


def tabla_declarado(dec):
    med = dec["medicion"]
    filas = ["| | |", "|---|---|"]
    filas.append("| **acto** | **%d** del `orden_universo`, el PRIMERO del prefijo |" % dec["acto"])
    filas.append("| **miembros** | **%d**, y **NINGUNO se toca** |" % med["miembros"])
    filas.append("| **combinaciones internas** | %d |" % med["combinaciones"])
    filas.append("| **pares `A` internos** | %d |" % med["pares_A"])
    filas.append("| **pares `D` internos** | **%d**, leidos y declarados DISTINTOS |" % med["pares_D"])
    filas.append("| **pares sin veredicto escrito** | %d |" % med["pares_sin_veredicto"])
    filas.append("| **NODOS PUENTE** | **%d** |" % med["nodos_puente"])
    filas.append("| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **%d** |" % med["triangulos_puente"])
    filas.append("| **PUERTAS dentro del acto** | **%d**: `%s` |"
                 % (len(med["puertas_dentro"]), "`, `".join(med["puertas_dentro"])))
    filas.append("| **instrumento** | [`../loop/%s`](../loop/%s) |"
                 % (os.path.basename(med["salida"]), os.path.basename(med["salida"])))
    return NL.join(filas)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("REGISTRO DEL LOTE A DEL TRAMO UNICO DE OP-U-02 EN 03_FUSIONES.md")
    print("=" * 78)

    malas = cotejar(CITAS_PAGINA)
    if malas:
        print()
        print("ROJO: %d cita(s) no calzan y NO se escribe nada." % len(malas))
        return 1

    plan = json.load(io.open(PLAN, encoding="utf-8"))
    acto = plan["actos"][0]
    dec = plan["declarados_y_no_fundidos"][0]

    ejec = leer("SALIDA_V65_LOTE_A_EJEC.txt")
    p16 = busca(ejec, r"P\.16, DUPLICADAS QUE LA PROPIA FUSION FABRICA, medidas antes de limpiarlas: (\d+)", "P.16")
    ga = busca(ejec, r"guarda A, cero AUTO-ARISTAS nuevas\s+: (OK \(\d+\)|ROJO[^\n]*)", "guarda A")
    gb = busca(ejec, r"guarda B, cero DUPLICADAS nuevas tras resolver : (OK \(\d+\)|ROJO[^\n]*)", "guarda B")
    gc = busca(ejec, r"guarda C, los CINCO campos que esta operacion NO redacta, intactos: ([^\n]+)", "guarda C")
    gd = busca(ejec, r"guarda D, los \d+ absorbidos conservan su texto INTACTO: ([^\n]+)", "guarda D")
    muertos = busca(ejec, r"nodos que MUEREN\s+: (\d+)", "nodos que mueren")
    implicados = busca(ejec, r"nodos implicados\s+: (\d+)", "nodos implicados")

    col = leer("SALIDA_V65_COLISIONES_ESPERADAS.txt")
    col_base = busca(col, r"linea base : (\d+), DECLARADA", "linea base")
    col_nuevas = busca(col, r"colisiones NUEVAS que la fusion fabricaria : (\d+)", "colisiones nuevas")
    censo = leer("SALIDA_V65_CENSO_COLISIONES_LOTE_A.txt")
    censo_calza = busca(censo, r"CUENTA ESPERADA: (\d+ \| MEDIDA: \d+ \| CALZA: \w+)", "censo de cierre")

    dif = leer("SALIDA_V65_DIFF_DUPLICADAS.txt")
    fabricadas = busca(dif, r"GRUPOS FABRICADOS DE VERDAD: (\d+)", "grupos fabricados")
    desaparecen = busca(dif, r"grupos que DESAPARECEN: (\d+)", "grupos que desaparecen")

    per = leer("SALIDA_V65_TALLAR_PERDIDAS.txt")
    n_per = busca(per, r"perdidas nombradas : (\d+)", "perdidas nombradas")
    especies = busca(per, r"por especie        : (\{[^\n]+\})", "perdidas por especie")

    if FALLOS:
        print()
        print("ROJO, %d celda(s) no se pudieron leer y NO se escribe nada:" % len(FALLOS))
        for f in FALLOS:
            print("   %s" % f)
        return 1

    t = """

---

## `%s` (2026-08-20, vuelta 65)

**Cada celda y cada tabla de este registro sale del PLAN SELLADO
[`../loop/PLAN_V65_OPU02_LOTE_A.json`](../loop/PLAN_V65_OPU02_LOTE_A.json) o de una salida de esta
vuelta, generada y pegada entera con `python scripts/loop/vuelta65_registro_tramo.py`.** **El
registro se adosa al final de la pagina y NO reescribe ni una linea de arriba.**

**EL LOTE SE DECLARO AL ABRIRLO Y ES PREFIJO SIN SALTOS** del `orden_universo` del tramo fijado en
[`../loop/TRAMO_UNICO_OPU02_V64.jsonl`](../loop/TRAMO_UNICO_OPU02_V64.jsonl): **los actos 1 y 3**,
que son **los dos primeros**. **Los dos CIERRAN ENTEROS en esta vuelta**, uno declarado y el otro
fundido.

### a) **EL ACTO 1: `DECLARADO Y NO FUNDIDO` POR `P.10`, Y ES LA PRIMERA VEZ QUE LA CAMPANA LO HACE**

`P.10` del banco del plan dice, con todas sus letras, que **un NODO PUENTE es el que tiene `A` con
dos nodos que entre si son `D`**, que **la componente que forma puede ser UNA familia o DOS pegadas
por el**, que **el cierre transitivo no lo distingue porque no lee sino que cuenta**, y que **si
aparece, LA COMPONENTE NO SE FUNDE HASTA QUE ESE TRIANGULO SE CIERRE**. **Lo que `P.10` llama *lo que
nunca es salida* es exactamente fundir la componente entera porque el cierre transitivo la junta.**

**LA MEDICION VA DELANTE DE LA DECISION**, y sale de
`python scripts/loop/vuelta65_puentes_del_tramo.py`, con los ids pasados por el resolutor (`P.1`):

%s

**LOS TRES NODOS PUENTE Y SUS SEIS TRIANGULOS, leidos de la salida:**
`errores_como_consecuencia` hace de puente en **cuatro** (contra `error_humano_vs_falla_mecanica` y
`falla_sistemica_vs_error_individual`, que son `D` en el puesto **2403**; contra
`new_view_human_error` y `riesgos_del_enfoque_en_error_humano`, `D` en el **2299**; contra
`new_view_human_error` y `seduccion_modelo_persona`, `D` en el **2331**; y contra
`riesgos_del_enfoque_en_error_humano` y `seduccion_modelo_persona`, `D` en el **2228**);
`human_error_como_sintoma` en **uno** (el **2403**); y `vieja_vision_vs_nueva_vision_seguridad` en
**uno** (`new_view_human_error` contra `new_view_vs_old_view`, `D` en el **2220**).

**LAS TRES SALIDAS DE `P.10`, RECORRIDAS UNA A UNA en vez de elegir la comoda:** *leer el par que
falta* es la unica que resuelve de verdad, **y quedan 75 combinaciones sin veredicto escrito**, que
es trabajo de cribado y no de esta operacion; *releer contra el superviviente* **no aplica**, porque
aqui no hay superviviente elegido ni nodo que vaya a cambiar; y *fundir solo el subconjunto CERRADO y
enlazar el resto* **pide que TODAS las lecturas esten hechas, y no lo estan**.

> **Y HAY UNA SEGUNDA RAZON INDEPENDIENTE, TAMBIEN MEDIDA, que sola bastaria: DOS de los quince
> miembros son PUERTA** con la marca *TIENE QUE SOBREVIVIR* (`enfoque_situacional_vs_personal` y
> `fallas_activas_condiciones_latentes`, leidas de la salida del dossier). **La GUARDA 1B dice que un
> nodo que es semilla de entrada o extremo de puente aprobado NO SE ABSORBE**, y una fusion a un solo
> superviviente tendria que absorber una de las dos.

**EL ACTO QUEDA VIVO Y ENTERO: no se toca ni un nodo, no se depreca ninguno y no se elige
superviviente.** El motivo entero esta sellado en el campo `declarados_y_no_fundidos` del plan.

### b) **EL ACTO 3: LA PRIMERA FUSION DE MAS DE DOS MIEMBROS DE LA CAMPANA**

| | |
|---|---|
| **superviviente** | `%s` |
| **absorbidos** | **%d** |
| **nodos implicados / nodos que MUEREN** | %s / %s |
| **plan sellado** | [`../loop/PLAN_V65_OPU02_LOTE_A.json`](../loop/PLAN_V65_OPU02_LOTE_A.json), contrato **`CAMPO PROPIO v1`** |
| **figura** | %s |

**LA PREGUNTA DE `P.5`, UNA FAMILIA O DOS, CONTESTADA CON MEDICION Y NO CON IMPRESION:** los **diez**
miembros salen del **mismo libro** (*Out of the Crisis*, Deming), **los 14 pares internos con
veredicto escrito son TODOS de clase `A`**, hay **CERO pares `D` internos** y **CERO nodos puente**.
**`P.10` solo detiene una componente cuando aparece un triangulo `A` mas `A` mas `D`, y aqui no hay
ninguno.**

**EL SUPERVIVIENTE LO ELIGE EL CONTENIDO, CON LAS TRES VARAS POR FORMA A SU LADO Y NINGUNA EN CONTRA**
(`TODAS DE ACUERDO`, que funde a su lado): **6 pasos contra un maximo de 5**, **3 condiciones contra
2** y **cableado 14 contra un maximo de 9**. **NI EL ROTULO SOLO NI LA CANTIDAD DECIDEN**: decide que
es el unico del acto que trae el procedimiento entero de punta a punta, del dato en orden cronologico
a la accion distinta por tipo de causa. **NINGUN MIEMBRO DE ESTE ACTO ES PUERTA**, medido al sellar.

#### EL REPARTO POR ABSORBIDO, TALLADO DEL PLAN SELLADO

%s

#### EL REPARTO, PIEZA A PIEZA, TALLADO DEL PLAN SELLADO

%s

#### LAS PERDIDAS, SELLADAS EN CAMPO PROPIO (`CAMPO PROPIO v1`)

**Son %s**, y la tabla sale entera de
`python scripts/loop/tallar_perdidas_del_plan.py --plan docs/loop/PLAN_V65_OPU02_LOTE_A.json`
([`../loop/SALIDA_V65_TALLAR_PERDIDAS.txt`](../loop/SALIDA_V65_TALLAR_PERDIDAS.txt)). **Por especie:
%s.**

%s

> **LAS TRES COSAS QUE EL REPARTO DICE EN VEZ DE CALLAR, y las tres tienen letra citable.**
> **PRIMERA, POR QUE HAY TRES `INCISO` Y NO SEIS:** el paso **4** del superviviente recibe **UN**
> inciso y **NO** recibe el segundo que pedia `trampa_del_promedio_como_estandar` con sus ejemplos de
> vision y capacitacion, **porque NO SE APILA MAS DE UN `INCISO` SOBRE EL MISMO PASO** (acta 64,
> pregunta 5, registrada en esta misma vuelta unas lineas mas arriba); esa pieza va `CUBIERTO` con la
> perdida **nombrada y enrutada**. **SEGUNDA, LAS ADVERTENCIAS NO SON PASOS** (`P.11`): *evitar
> sanciones*, *evitar conclusiones apresuradas*, *evitar tratar cada defecto como causa especial* y
> *dejar de usar el promedio como linea de corte* **califican el acto y no lo constituyen**, asi que
> van `CUBIERTO` con su perdida nombrada en vez de `APPEND`. **TERCERA, LOS SOLAPES VAN DECLARADOS**
> para la poda de la fase 04: dos piezas de comunicacion viajan enteras diciendo casi lo mismo, y las
> piezas del eje de la persona van `CUBIERTO` **con el atenuante dicho**, porque ese eje llega entero
> en el `APPEND` del paso 1 de `politica_no_culpar_trabajador`.

#### LAS GUARDAS, LEIDAS DE LA SALIDA DE LA EJECUCION

Salen de [`../loop/SALIDA_V65_LOTE_A_EJEC.txt`](../loop/SALIDA_V65_LOTE_A_EJEC.txt):

| guarda | resultado |
|---|---|
| **`P.16`, duplicadas que la propia fusion fabrica** | **%s**, limpiadas en el mismo commit |
| **guarda A**, cero auto-aristas nuevas | **%s** |
| **guarda B**, cero duplicadas nuevas tras resolver | **%s** |
| **guarda C**, los cinco campos que la operacion NO redacta, intactos | **%s** |
| **guarda D**, los absorbidos conservan su texto INTACTO | **%s** |
| **`P.16` por instrumento**, grupos FABRICADOS de verdad | **%s** (y %s grupos que DESAPARECEN) |

#### LA CUENTA ESPERADA DE COLISIONES, MEDIDA **ANTES** DE FUNDIR

**Se mide antes y no despues, y esa es la mitad del punto**: es la leccion del `D5` de la vuelta 64,
que el acta 64 registro como caida de procedimiento autodeclarada. **La linea base es `%s` y esta
DECLARADA** (acta 64, pregunta 3, registrada en esta pagina unas lineas mas arriba): **las dos
colisiones vigentes son de la mesa `OP-M-03` y NO SE TOCAN.**

**Simulacion en memoria sobre el arbol de ANTES de fundir**
([`../loop/SALIDA_V65_COLISIONES_ESPERADAS.txt`](../loop/SALIDA_V65_COLISIONES_ESPERADAS.txt)):
**colisiones NUEVAS que la fusion fabricaria: %s.** **Censo de cierre con la esperada MEDIDA:
%s** ([`../loop/SALIDA_V65_CENSO_COLISIONES_LOTE_A.txt`](../loop/SALIDA_V65_CENSO_COLISIONES_LOTE_A.txt)).

### c) **LO QUE ESTE REGISTRO NO HACE**

**NO toca ni una cifra publicada arriba, NO re-lee ni un veredicto de las dos colisiones vigentes de
la mesa `OP-M-03`, NO ejecuta ningun acto con dueno de otra operacion y NO rehace ninguna de las
cinco fichas `OP-M-02` consumidas.**
""" % (CABECERA, tabla_declarado(dec), acto["superviviente"], len(acto["absorbidos"]),
       implicados, muertos, acto["figura"], tabla_por_absorbido(acto), tabla_reparto(acto),
       n_per, especies, tabla_perdidas(), p16, ga, gb, gc, gd, fabricadas, desaparecen,
       col_base, col_nuevas, censo_calza)

    for mal, nombre in ((chr(8212), "guion largo"), (chr(8211), "guion medio")):
        if mal in t:
            print()
            print("ROJO: el texto trae un %s. PARADA." % nombre)
            return 1

    crudo = io.open(PAGINA, encoding="utf-8").read()
    if CABECERA in crudo:
        print()
        print("YA ADOSADO: la cabecera del tramo ya esta en la pagina. No se escribe nada.")
        return 0

    antes = len(crudo.split(NL))
    print()
    print("  la pagina tiene %d lineas y el texto anade %d" % (antes, t.count(NL)))
    if a.simular:
        print()
        print("  SIMULACION: no se escribe nada. Las primeras lineas:")
        for l in t.split(NL)[:10]:
            print("     %s" % l[:100])
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
    print("  las sedes de arriba siguen en su linea: %s"
          % ("OK (%d de %d)" % (len(CITAS_PAGINA), len(CITAS_PAGINA))
             if not cotejar(CITAS_PAGINA) else "ROJO"))
    print()
    print("VERDE: registro adosado y nada de arriba reescrito.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
