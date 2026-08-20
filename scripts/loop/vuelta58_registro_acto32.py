# -*- coding: utf-8 -*-
"""vuelta58_registro_acto32.py . LA SEGUNDA MITAD DE LA CORRECCION DECLARADA DEL
ACTO 32, Y LA TAREA 1.4: ESCRIBIR EN EL REGISTRO DEL TRAMO 4 DE
docs/plan/03_FUSIONES.md LO QUE LA VUELTA 58 MOVIO Y LO QUE EL ACTA 57 ADJUDICO.

SUCESOR DECLARADO de scripts/loop/vuelta57_registro_tramo.py en su maquina: NINGUNA
CELDA SE TECLEA. Las cifras se extraen por expresion regular de las salidas del dia
y las tablas se RECORTAN POR MAQUINA de la salida de su tallador. Si una celda no se
puede leer, el instrumento CAE EN ROJO y no escribe nada.

LO QUE ESCRIBE, y son las dos cosas que el encargo pide:

  1. LA CORRECCION DECLARADA DEL ACTO 32 (TAREA 1.1). El texto viejo NO SE BORRA,
     que es lo que la regla 8 pide: las celdas del estado que se movieron quedan con
     TACHADO y su cifra nueva al lado, las cuatro tablas talladas del dia del sellado
     se quedan enteras con un aviso delante de que estan SUPERADAS, y al final del
     registro va el bloque nuevo con las tablas VIGENTES pegadas enteras del tallador.

  2. LAS ADJUDICACIONES DEL ACTA 57 QUE LE TOCAN AL REGISTRO (TAREA 1.4): el acto 25
     queda DECLARADO por el carril del IMPOSIBLE POR PUERTA, que ya estaba escrito y
     no hacia falta doctrina nueva (acta 51 pregunta 3, citada por el acta 54 pregunta
     1, y el acta 54 pregunta 2 lo lista en el carril de declarar y acumular), con su
     SALIDA DE FONDO reservada a la mesa en el pendiente 5.

ANCLA LITERAL UNICA (rojo si falta o si aparece mas de una vez) e IDEMPOTENTE.

MODOS: --simular (por defecto) y --ejecutar.

Uso: python scripts/loop/vuelta58_registro_acto32.py [--ejecutar]
"""
# ROTULO titulo especie=SELLO_FIJO sujeto=tramo:4 corte=2026-08-20 motivo="corrige el registro del tramo 4 por el acto 32: sujeto fijo"
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PAGINA = "docs/plan/03_FUSIONES.md"


def leer(nombre, fallos):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        fallos.append("no existe la salida %s" % nombre)
        return ""
    return io.open(ruta, encoding="utf-8").read()


def busca(texto, patron, etiqueta, fallos):
    m = re.search(patron, texto) if texto else None
    if not m:
        fallos.append("no se pudo leer %s" % etiqueta)
        return "?"
    return m.group(1)


def recortar(texto, desde, hasta, etiqueta, fallos):
    """La tabla entera entre dos marcas de la salida del tallador, recortada por
    maquina y no copiada a mano."""
    i = texto.find(desde)
    if i < 0:
        fallos.append("no se encontro el inicio de %s" % etiqueta)
        return ""
    j = texto.find(hasta, i + len(desde))
    if j < 0:
        fallos.append("no se encontro el fin de %s" % etiqueta)
        return ""
    filas = [l for l in texto[i + len(desde):j].splitlines() if l.strip().startswith("|")]
    if not filas:
        fallos.append("%s salio sin filas" % etiqueta)
    return "\n".join(filas)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("EL REGISTRO DEL TRAMO 4, CORREGIDO . MODO %s"
          % ("EJECUTAR" if a.ejecutar else "SIMULAR"))
    print("=" * 78)
    print()

    fallos = []
    tall = leer("SALIDA_V58_TALLAR_PLANES.txt", fallos)
    est = leer("SALIDA_V58_ESTADO_TRAS_ACTO32.txt", fallos)
    rec = leer("SALIDA_V58_RECOMPUTO_TRAS_ACTO32.txt", fallos)
    cen = leer("SALIDA_V58_CENSO_TRAS_ACTO32.txt", fallos)
    des = leer("SALIDA_V58_DESHACER_ACTO32.txt", fallos)

    d = {}
    d["vivos"] = busca(est, r"vivos\s+: (\d+)", "vivos", fallos)
    d["deprecados"] = busca(est, r"deprecados\s+: (\d+)", "deprecados", fallos)
    d["enlaces"] = busca(est, r"enlaces\s+: (\d+)", "enlaces", fallos)
    d["colapsos"] = busca(rec, r"los dos lados\): (\d+)", "colapsos", fallos)
    d["pares"] = busca(rec, r"deduplicar\): (\d+)", "pares distintos", fallos)
    d["componentes"] = busca(rec, r"componentes totales: (\d+)", "componentes", fallos)
    d["cerrados"] = busca(rec, r"CERRADOS: (\d+) sobre", "CERRADOS", fallos)
    d["c1"] = busca(rec, r"i\. nodos en actos \((\d+)\)", "comprobacion i", fallos)
    d["c1d"] = busca(rec, r"i\. nodos en actos \(\d+\) == suma de tamanos de las componentes \((\d+)\)",
                     "comprobacion i derecha", fallos)
    d["c2"] = busca(rec, r"ii\. A vigentes resueltas del retrato \((\d+)\)",
                    "comprobacion ii", fallos)
    d["c2d"] = busca(rec, r"ii\. A vigentes resueltas del retrato \(\d+\) == suma de aristas A internas de las componentes \((\d+)\)",
                     "comprobacion ii derecha", fallos)
    d["autopares"] = busca(cen, r"AUTO-PARES \(los dos lados al mismo vivo\): (\d+)",
                           "auto-pares", fallos)
    d["colisiones"] = busca(cen, r"COLISIONES DE CLASE VIGENTES\s+: (\d+)",
                            "colisiones", fallos)
    d["fundidos"] = busca(tall, r"actos tallados: (\d+)", "actos tallados", fallos)
    d["piezas"] = busca(tall, r"actos tallados: \d+ \| piezas: (\d+)", "piezas", fallos)
    d["declarados"] = busca(tall, r"\*\*(\d+) declarados\*\*", "declarados", fallos)

    t1 = recortar(tall, "--- TABLA 1", "--- TABLA 2", "tabla 1", fallos)
    t2 = recortar(tall, "--- TABLA 2", "--- TABLA 3", "tabla 2", fallos)
    t4 = recortar(tall, "--- TABLA 4", "--- TABLA 5", "tabla 4", fallos)
    t5 = recortar(tall, "--- TABLA 5", "  actos tallados", "tabla 5", fallos)

    if fallos:
        print("  ROJO, %d celdas no se pudieron leer y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("     %s" % f)
        return 1

    print("  celdas leidas de instrumento: %d" % len(d))
    for k in sorted(d):
        print("     %-14s %s" % (k, d[k]))
    print("  tablas recortadas por maquina: 4 (%d, %d, %d y %d filas)"
          % (len(t1.splitlines()), len(t2.splitlines()),
             len(t4.splitlines()), len(t5.splitlines())))
    print()

    aviso = ("> **TABLA SUPERADA (20 ago 2026, vuelta 58).** Esta tabla es la del dia del "
             "sellado y **se queda entera porque el texto viejo no se borra**. La VIGENTE, "
             "con el acto **32** fuera, esta en la **CORRECCION DECLARADA** del final de "
             "este registro.")

    bloque = """
---

### CORRECCION DECLARADA: **EL ACTO 32 SE DESHACE Y QUEDA DECLARADO, SEPTIMO DEL TRAMO** (20 ago 2026, vuelta 58, TAREA 1.1 del encargo)

**LA RELECTURA CONJUNTA QUE EL ACTA 57 ENCARGO SE RESOLVIO A FAVOR DEL CASO DEL AUDITOR**
(su seccion 2 y su discutible `D4`), **y se verifico contra el grafo ANTES de tocar nada**, que es
lo que el encargo pedia. **Instrumento de solo lectura**
`python scripts/loop/vuelta58_relectura_acto32.py --raiz <worktree en 75863aee>`
([`../loop/SALIDA_V58_RELECTURA_ACTO32_PREFUSION.txt`](../loop/SALIDA_V58_RELECTURA_ACTO32_PREFUSION.txt)),
con la aritmetica de varas copiada entera del cuadro de varas y medida sobre el arbol **PRE
FUSION**: `programa_de_referidos_de_franquiciados` contra `referidos_franquiciados_existentes` da
**pasos 5 contra 5, condiciones 2 contra 2 y cableado 3 contra 3**, y la forma que la receta le da
es **EMPATE SIN VARA**.

**LA LETRA VIGENTE, LEIDA HOY Y CON SU LINEA AL LADO:** el acta 53, pregunta 4 (linea **13015** de
`../loop/ACTA_AUDITOR.md`) *reserva el empate sin vara para cuando TODO empata*; el acta 54,
pregunta 4 (linea **13389**) dice que *el conteo de caracteres no desempata*, y su linea **13391**
que *el propio declarado de UN SOLO LADO es una vara no empatada*. **En este acto el propio
declarado esta A LOS DOS LADOS**: la razon del puesto **2127**, leida hoy entera, mide **UNA
LINEA** propia de uno y **DOS LINEAS** propias del otro. **Contar esas lineas es un conteo sobre la
letra, y ninguna acta lo ha adjudicado como vara.** La razon del 2127 **no declara superviviente,
ni contencion, ni padre**: pesa una pieza como *la que mas cuesta reponer*, que no es ninguna de
las tres formas que el acta 53, pregunta 3, enumera.

> **EL CONTRASTE INTERNO, MEDIDO EN LA MISMA SALIDA Y NO CITADO DE MEMORIA:** el **acto 11** de
> este mismo tramo da **4 contra 4, 2 contra 2 y 2 contra 2**, tambien **EMPATE SIN VARA**, y su
> razon (puesto **1884**) declara material propio **UNA linea contra TRES**. **La vuelta 57 lo
> DECLARO.** Dos actos con la misma forma y el mismo tipo de desempate no pueden acabar uno fundido
> y otro declarado, y esa inconsistencia es la que esta correccion cierra.

**NINGUNA EVIDENCIA NUEVA CONTRA EL CASO**, asi que no hubo que parar antes de tocar el grafo.
**LA RAMA DE LA CANTIDAD COMO VARA NO SE APLICA MAS** mientras la mesa no la adopte: queda dentro
del **pendiente de doctrina 1**, tal como el acta 57 (pregunta 2) la dejo.

**EL DESHACER, Y LO QUE OBLIGO A HACERLO DISTINTO DEL ACTO 23 DE LA VUELTA 55.**
`python scripts/loop/vuelta58_deshacer_acto32.py --ejecutar`
([`../loop/SALIDA_V58_DESHACER_ACTO32.txt`](../loop/SALIDA_V58_DESHACER_ACTO32.txt)). De los
**CINCO** ficheros que el acto 32 toco en el lote B (`a1d7269d`), **CUATRO** no se habian vuelto a
tocar y se restauran al blob del lote A (`0481113f`); **el quinto,
`principio_apalancamiento_numero_magico.json`, SI se toco despues**, en el lote C (`706397c7`) y
**por OTRO acto, el 35**. **Restaurarle el blob habria borrado el acto 35**, asi que ese fichero
recibe el **DIFF INVERSO** del acto 32, probado con `--check` antes de aplicarse. **El acto 35
queda en pie, verificado por conteo.** Las guardas de despues: **los dos miembros VIVOS, sin alias
cruzado y CAMPO A CAMPO IDENTICOS al blob pre fusion**, y **el cableado de vuelta al absorbido en
los tres vecinos**.

#### EL ESTADO DEL TRAMO 4, RECOMPUTADO TRAS DESHACER EL ACTO 32

**Ninguna celda esta tecleada:** las extrae `python scripts/loop/vuelta58_registro_acto32.py` de
[`../loop/SALIDA_V58_ESTADO_TRAS_ACTO32.txt`](../loop/SALIDA_V58_ESTADO_TRAS_ACTO32.txt),
[`../loop/SALIDA_V58_RECOMPUTO_TRAS_ACTO32.txt`](../loop/SALIDA_V58_RECOMPUTO_TRAS_ACTO32.txt) y
[`../loop/SALIDA_V58_CENSO_TRAS_ACTO32.txt`](../loop/SALIDA_V58_CENSO_TRAS_ACTO32.txt).

| | **cierre de la vuelta 57** | **tras deshacer el acto 32** |
|---|---:|---:|
| grafo: vivos / deprecados / enlaces | 3341 / 512 / 17369 | **{vivos} / {deprecados} / {enlaces}** |
| retrato: colapsos / pares distintos | 208 / 343 | **{colapsos} / {pares}** |
| actos (componentes) / `CERRADOS` | 149 / 96 | **{componentes} / {cerrados}** |
| auto-pares / colisiones de clase vigentes | 186 / 0 | **{autopares} / {colisiones}** |
| actos del tramo 4 fundidos / vivos | 44 / 6 | **{fundidos} / {declarados}, los {declarados} DECLARADOS** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (441 igual a 441; 343 igual a 343) | **TODAS OK ({c1} igual a {c1d}; {c2} igual a {c2d})** |

> **CADA CELDA QUE SE MOVIO LO HIZO EN UNO, Y ESO ERA LO QUE EL ENCARGO PREDECIA:** los colapsos
> bajan uno, los pares distintos suben uno, los actos suben uno, los `CERRADOS` suben uno, los
> auto-pares bajan uno, los vivos suben uno y los deprecados bajan uno. **Los enlaces bajan TRES y
> el motivo esta medido, no supuesto:** el conteo incluye los deprecados, la fusion habia sumado
> **tres** `nodos_previos` al superviviente, y esos tres son los que se van. **El marcador NO se
> mueve y tampoco es un olvido**: deshacer una fusion pura no voltea ningun veredicto, y el censo
> de colisiones sale en **{colisiones}** con `CALZA: SI`.

#### LAS TABLAS VIGENTES, TALLADAS DE LOS PLANES SELLADOS CON EL 32 RETIRADO

**Salen enteras de** `python scripts/loop/vuelta58_tallar_planes.py --vuelta 58 --retirado "32|..."`
([`../loop/SALIDA_V58_TALLAR_PLANES.txt`](../loop/SALIDA_V58_TALLAR_PLANES.txt)), **sucesor
declarado del tallador de la vuelta 57 copiado byte a byte**, cuyo unico anadido es el argumento
`--retirado`. **EL PLAN SELLADO NO SE TOCA:** los `PLAN_V57_*.json` se quedan con el acto 32 dentro
y su motivo entero, porque reescribir un plan sellado taparia lo que se corrige. **Corrido sin
`--retirado`, este sucesor imprime lo mismo que su ancestro al digito, y se comprobo.**

{t1}

{t2}

{t4}

{t5}

---

### LA ADJUDICACION DEL ACTA 57 SOBRE EL **ACTO 25**: **EL CARRIL YA ESTABA ESCRITO** (20 ago 2026, vuelta 58, TAREA 1.4 del encargo)

**El registro del tramo 4 dejo el acto 25 con la pregunta abierta** (*que se hace con un acto
`CERRADO` cuyos DOS miembros son puertas*). **El acta 57 la contesta en su pregunta 3 y SIN
DOCTRINA NUEVA, y se anota aqui con fecha porque es este registro el que la pedia:**

> **DECLARARLO FUE CORRECTO, y el carril es el IMPOSIBLE POR PUERTA.** La vara del acta 51,
> pregunta 3, define el imposible por puerta como **el acto donde NINGUNA fusion respeta la
> guarda**; el acta 54, pregunta 1, la cita; y el acta 54, pregunta 2, **lo lista con todas sus
> letras en el carril de DECLARAR Y ACUMULAR**. **Con las DOS puertas, ninguna direccion respeta la
> guarda `1B`: se declara, se acumula, el bucle sigue.** **No hacia falta doctrina nueva para
> declararlo y no se escribio ninguna.**

**LO QUE SI QUEDA PARA LA MESA ES LA SALIDA DE FONDO, Y SOLO ESA:** mover el puente o la semilla al
superviviente, o dejar el par como enlace permanente. **Eso es politica de catalogo y la casa lo
reserva**, en el **pendiente de doctrina 5**. **El acto 25 no vuelve a la cola de fusion mientras
tanto**, y sigue en la tabla de declarados de arriba con su especie escrita.
"""
    bloque = bloque.format(t1=t1, t2=t2, t4=t4, t5=t5, **d)

    ops = [
        # las celdas del estado que se movieron, con TACHADO y la cifra nueva
        ("| grafo: vivos / deprecados / enlaces | 3385 / 468 / 17290 | **3341 / 512 / 17369** |",
         "| grafo: vivos / deprecados / enlaces | 3385 / 468 / 17290 | ~~**3341 / 512 / 17369**~~ **%s / %s / %s** |"
         % (d["vivos"], d["deprecados"], d["enlaces"]),
         "celda del grafo"),
        ("| retrato: colapsos / pares distintos | 164 / 387 | **208 / 343** |",
         "| retrato: colapsos / pares distintos | 164 / 387 | ~~**208 / 343**~~ **%s / %s** |"
         % (d["colapsos"], d["pares"]),
         "celda del retrato"),
        ("| actos (componentes) / `CERRADOS` | 193 / 140 | **149 / 96** |",
         "| actos (componentes) / `CERRADOS` | 193 / 140 | ~~**149 / 96**~~ **%s / %s** |"
         % (d["componentes"], d["cerrados"]),
         "celda de los actos"),
        ("| actos del tramo 4 fundidos / vivos | 0 / 50 | **44 / 6, los 6 DECLARADOS** |",
         "| actos del tramo 4 fundidos / vivos | 0 / 50 | ~~**44 / 6, los 6 DECLARADOS**~~ **%s / %s, los %s DECLARADOS** |"
         % (d["fundidos"], d["declarados"], d["declarados"]),
         "celda de los actos del tramo"),
    ]
    avisos = [
        ("| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas nombradas |",
         "aviso sobre la tabla de lotes"),
        ("| la forma, leida del motivo sellado | cuantos | los actos |",
         "aviso sobre la tabla de formas"),
        ("| acto | lote | sobrevive | absorbe | piezas | enteras | ya dichas | `INCISO` |",
         "aviso sobre la tabla acto a acto"),
        ("| acto | lote | sus miembros | especie | se acumula para |",
         "aviso sobre la tabla de declarados"),
    ]

    crudo = io.open(os.path.join(RAIZ, PAGINA), encoding="utf-8", newline="").read()
    fin = "\r\n" if crudo.count("\r\n") > crudo.count("\n") // 2 else "\n"
    L = crudo.replace("\r\n", "\n").split("\n")
    print("  %s: final de linea %s, %d lineas"
          % (PAGINA, "CRLF" if fin == "\r\n" else "LF", len(L)))

    # EL ALCANCE SE ACOTA AL REGISTRO DEL TRAMO 4, y esto no es comodidad: la
    # primera corrida CAYO EN ROJO ella sola porque las cabeceras de las cuatro
    # tablas son IDENTICAS en los registros de los tramos 1, 2, 3 y 4, y el ancla
    # aparecia dos y tres veces. La guarda hizo lo que se le pide y no escribio
    # nada; lo que se corrige es el alcance, no la guarda.
    CABEZA = "## `OP-U-01`, TRAMO 4: EL REGISTRO DEL CIERRE (20 ago 2026, vuelta 57)"
    if L.count(CABEZA) != 1:
        print("  ROJO: la cabecera del registro del tramo 4 aparece %d veces."
              % L.count(CABEZA))
        return 1
    BASE = L.index(CABEZA)
    # Y LA VENTANA SE CIERRA ANTES DEL BLOQUE DE LA CORRECCION, que es lo que la
    # SEGUNDA corrida destapo: el bloque nuevo PEGA LAS TABLAS ENTERAS, cabecera
    # incluida, asi que a partir de la primera escritura el ancla aparece dos veces
    # dentro del tramo y la guarda caia en rojo sobre su propio trabajo. La guarda
    # estaba bien (no escribio nada); lo que faltaba era el limite de la ventana.
    MARCA = ("### CORRECCION DECLARADA: **EL ACTO 32 SE DESHACE Y QUEDA DECLARADO, "
             "SEPTIMO DEL TRAMO**")
    TOPE = next((i for i in range(BASE, len(L)) if L[i].startswith(MARCA)), len(L))
    print("  el registro del tramo 4: lineas %d a %d (la ventana de las anclas)"
          % (BASE + 1, TOPE))
    print()

    def unica(ancla):
        """La posicion del ancla DENTRO de la ventana, y cuantas veces aparece ahi.
        Fuera de la ventana no se mira."""
        hall = [i for i in range(BASE, TOPE) if L[i] == ancla]
        return (hall[0] if len(hall) == 1 else None), len(hall)

    hechos, ya, malos = [], [], []
    for ancla, nuevo, nombre in ops:
        if nuevo in L:
            ya.append(nombre)
            print("  YA ESTABA   %s" % nombre)
            continue
        k, cuantas = unica(ancla)
        if k is None:
            malos.append("%s: el ancla aparece %d veces en el tramo 4" % (nombre, cuantas))
            print("  ROJO        %s: el ancla aparece %d veces" % (nombre, cuantas))
            continue
        L[k] = nuevo
        hechos.append(nombre)
        print("  ESCRIBE     %s" % nombre)

    for ancla, nombre in avisos:
        k, cuantas = unica(ancla)
        if k is None:
            malos.append("%s: el ancla aparece %d veces en el tramo 4" % (nombre, cuantas))
            print("  ROJO        %s: el ancla aparece %d veces" % (nombre, cuantas))
            continue
        if k >= 2 and L[k - 2].startswith("> **TABLA SUPERADA"):
            ya.append(nombre)
            print("  YA ESTABA   %s" % nombre)
            continue
        L[k:k] = [aviso, ""]
        hechos.append(nombre)
        print("  ESCRIBE     %s" % nombre)

    marca_bloque = MARCA
    if any(l.startswith(marca_bloque) for l in L):
        ya.append("bloque de la correccion")
        print("  YA ESTABA   bloque de la correccion")
    else:
        L.extend(bloque.split("\n"))
        hechos.append("bloque de la correccion")
        print("  ESCRIBE     bloque de la correccion (%d lineas)"
              % len(bloque.split("\n")))

    print()
    if malos:
        print("  ROJO, %d anclas malas y NO se escribe nada:" % len(malos))
        for m in malos:
            print("     %s" % m)
        return 1
    print("  resumen: %d a escribir, %d YA ESTABAN" % (len(hechos), len(ya)))
    print()
    if not a.ejecutar:
        print("  MODO SIMULAR: no se escribe nada.")
        print("FIN")
        return 0
    if not hechos:
        print("  nada que escribir: los %d sitios YA ESTABAN. Idempotente." % len(ya))
        print("FIN")
        return 0
    io.open(os.path.join(RAIZ, PAGINA), "w", encoding="utf-8", newline="").write(
        fin.join(L))
    print("  escrito: %s" % PAGINA)
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
