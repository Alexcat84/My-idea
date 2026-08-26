# -*- coding: utf-8 -*-
"""vuelta68_registro_lote_d.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DEL LOTE D DEL TRAMO UNICO DE OP-U-02, BAJO LA CABECERA DE TRAMO QUE LA
VUELTA 65 YA ADOSO.

NO REESCRIBE NI UNA LINEA DE ARRIBA: abre el fichero en modo adosar.

NINGUNA TABLA SE TECLEA (regla 1): la del reparto pieza a pieza, la de las
piezas por absorbido y las de los actos declarados SE GENERAN del PLAN SELLADO
docs/loop/PLAN_V68_OPU02_LOTE_D.json; la de las perdidas se RECORTA ENTERA de la
salida del tallador; y las celdas de guardas, colisiones y censos se EXTRAEN POR
AGUJA de las salidas de esta vuelta. La celda que no se pueda leer de su fichero
es ROJO y NO SE ESCRIBE NADA.

LAS CUATRO FUNCIONES QUE ARMAN TABLA (tabla_reparto, tabla_por_absorbido,
tabla_perdidas y tabla_declarado) SE COPIAN LITERAL de
scripts/loop/vuelta67_registro_lote_c.py, que a su vez las copio de la vuelta 66:
dos registros de la misma pagina no pueden dibujar el reparto distinto en
silencio. tabla_declarado conserva el anadido de la vuelta 67 (imprime EL MOTIVO
SELLADO) y le suma UNA fila mas, tambien dicha aqui: imprime los DUENOS medidos
del acto cuando los tiene, porque el acto 24 de este lote trae OP-S-07 en
duenos_cualquier_operacion y esa es una razon de cierre que la prosa no deberia
ser la unica en decir. La aritmetica de las otras tres no se toca.

LA GUARDA DE CITAS ES LA ENSANCHADA DE ESTA MISMA VUELTA, Y NO SE RE-IMPLEMENTA:
este fichero IMPORTA derivar, negativas, sustituir y cotejar_texto de
scripts/loop/vuelta68_registrar_acta67.py y les pone SUS PROPIAS agujas, en vez
de copiar el codigo. Una guarda copiada en dos sitios se separa en silencio, que
es la especie que esta campana persigue. Las dos condiciones del acta 61 (D2 y
pregunta 2) estan cumplidas en el docstring de aquel fichero y el ensanche va
MARCADO DISCUTIBLE en el reporte de la vuelta 68.

GUARDA DE IDEMPOTENCIA: si la cabecera de este lote ya esta, no escribe, y se
mira ANTES de derivar nada.

Uso:
  python scripts/loop/vuelta68_registro_lote_d.py [--simular]
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:65 fuente=docs/plan/03_FUSIONES.md prueba="TRAMO UNICO Y FINAL POR AGOTAMIENTO: EL REGISTRO DEL LOTE A" corte=2026-08-26 motivo="el docstring nombra la VUELTA 65 porque es la vuelta que adoso la cabecera de tramo bajo la que este registro se cuelga, derivada hoy por aguja; el fichero es de la vuelta 68 y por eso el numero no calza con su propia vuelta a proposito"
import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
LOOP = os.path.join(RAIZ, "docs", "loop")
PLAN = os.path.join(LOOP, "PLAN_V68_OPU02_LOTE_D.json")
NL = chr(10)
CABECERA = "OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE D"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta68_registrar_acta67 as G  # noqa: E402
from _v68_texto_lote_d import TEXTO  # noqa: E402

# LAS AGUJAS DE ESTE REGISTRO. CLAVE -> (fichero, aguja de CONTENIDO). El numero
# de linea sale de buscarla; en este fichero no hay ni un numero tecleado.
MIS_AGUJAS = {
    "PAG_ORDEN_FASE": (PAGINA, "## EL ORDEN DE ESTA FASE, y el criterio que lo fija"),
    "PAG_CARRIL_COLISIONES": (PAGINA, "### EL CARRIL GENERAL DE COLISIONES, ESTRENADO EN SUS DOS FORMAS"),
    "PAG_FICHA_ENVEJECIDA": (PAGINA, "### b) **LA REGLA DE LA FICHA ENVEJECIDA**"),
    "PAG_TRAMO_CABECERA": (PAGINA, "TRAMO UNICO Y FINAL POR AGOTAMIENTO: EL REGISTRO DEL LOTE A"),
    "PAG_ACTO1_P10": (PAGINA, "### a) **EL ACTO 1: `DECLARADO Y NO FUNDIDO` POR `P.10`"),
    "PAG_GUARDA_1B": (PAGINA, "### c) **UN ACTO CON DOS O MAS PUERTAS CIERRA `DECLARADO Y NO FUNDIDO`"),
    "PAG_LOTE_B": (PAGINA, "## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE B`"),
    "PAG_ACTO11_IA": (PAGINA, "**El `acto 11`, la familia de la supervision de la IA:**"),
    "PAG_P5_MOTIVO": (PAGINA, "### b) **UN ACTO CUYO `P.5` CONTESTA QUE NO ES UNA FAMILIA CIERRA"),
    "PAG_LOTE_C": (PAGINA, "## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE C`"),
    "PAG_ACTO12_SIN_LETRA": (PAGINA, "### b) **EL `ACTO 12`: `DECLARADO Y NO FUNDIDO` POR ALGO QUE NINGUNA LETRA CUBRE"),
    "PAG_ACTA67": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 67, REGISTRADAS AQUI"),
    "PAG_CORRECCION_CITA": (PAGINA, "### b) **LA CORRECCION DECLARADA DE LA CITA, POR EL CARRIL DEL BANCO 9.10"),
    "PAG_CUARTO_MOTIVO": (PAGINA, "### d) **EL CUARTO MOTIVO SELLADO DEL `DECLARADO Y NO FUNDIDO`"),
    "PAG_TRANSITO": (PAGINA, "### e) **EL TRANSITO DEL ACTO CON FORMA `EMPATE SIN VARA`"),
    "PAG_D10_POR_PIEZA": (PAGINA, "LA FILA DEL CONTRATO ES POR PIEZA QUE SE PIERDE, NO POR SITIO DONDE VIVIA"),
}
MIS_ANCLAS = {}
# Numeros de 3 a 5 digitos que el texto pone en negrita y NO son citas de linea,
# declarados uno a uno con su motivo. Todo lo demas tiene que salir de una aguja.
MIS_NUMEROS = {
    "972": "puesto A interno del acto 19",
    "994": "puesto del D interno del acto 20",
    "177": "puesto A interno del acto 22",
    "456": "puesto A interno del acto 22, el mismo principio numerado",
    "636": "puesto de un D interno del acto 24",
    "639": "puesto de un radio de la estrella de pass/fail",
    "467": "puesto de un radio de la estrella de pass/fail",
    "511": "puesto de un radio de la estrella de pass/fail",
    "1193": "puesto del D interno del acto 23",
    "1346": "puesto del D interno del acto 24 que decidia la estrella",
    "1371": "puesto que cuenta la familia de la reserva de opciones",
    "1436": "puesto que cierra la cobertura de esa familia",
    "1517": "puesto de la absorcion que mete a la pareja en el racimo",
    "1541": "puesto que declara que la particion escrita no se mueve",
    "1582": "puesto A interno del acto 19",
    "1597": "puesto A interno del acto 19 que declara la familia de cuatro",
    "2927": "puesto de un D interno del acto 21",
    "3102": "puesto de un D interno del acto 21",
    "1797": "puesto A interno del acto 18",
    "1871": "puesto A interno del acto 18",
    "1903": "puesto A interno del acto 18",
    "730": "puesto que declara el choque encima del acto 20",
}

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


# --- COPIADAS LITERAL de vuelta67_registro_lote_c.py -----------------------
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
    """RECORTADA ENTERA de la salida del tallador, no re-generada."""
    t = leer("SALIDA_V68_TALLAR_PERDIDAS.txt")
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


MOTIVO_SELLADO = {
    20: "**`P.10`**, con su triangulo MEDIDO (acta 65, el carril registrado en la linea "
        "**[[PAG_ACTO1_P10]]**)",
    21: "**`P.10`**, con sus DOS triangulos MEDIDOS",
    23: "**`P.10`**, con su triangulo MEDIDO",
    24: "**`P.10`**, con sus DOS triangulos MEDIDOS, **mas el ejemplar de la figura `ESTRELLA "
        "(9.23)` que una fusion entera borraria**, **mas el DUENO**",
}


def tabla_declarado(dec):
    med = dec["medicion"]
    filas = ["| | |", "|---|---|"]
    filas.append("| **acto** | **%d** del `orden_universo` |" % dec["acto"])
    filas.append("| **MOTIVO SELLADO DEL CIERRE** | %s |" % MOTIVO_SELLADO[dec["acto"]])
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
    # EL ANADIDO DE ESTA VUELTA, dicho en el docstring: los duenos medidos.
    filas.append("| **duenos medidos hoy en el fichero del tramo** | %s |"
                 % ("**%s** en `duenos_cualquier_operacion`"
                    % "`, `".join(med["duenos_cualquier_operacion"])
                    if med.get("duenos_cualquier_operacion") else
                    "**NINGUNO**, los dos campos vacios"))
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
    print("REGISTRO DEL LOTE D DEL TRAMO UNICO DE OP-U-02 EN 03_FUSIONES.md")
    print("Con la guarda de citas ENSANCHADA de la vuelta 68, importada.")
    print("=" * 78)

    crudo = io.open(PAGINA, encoding="utf-8").read()
    if CABECERA in crudo:
        print()
        print("YA ADOSADO: el registro del lote D ya esta en la pagina. No se escribe nada.")
        return 0

    plan = json.load(io.open(PLAN, encoding="utf-8"))
    actos = {x["orden"]: x for x in plan["actos"]}
    decl = {x["acto"]: x for x in plan["declarados_y_no_fundidos"]}

    fus = leer("SALIDA_V68_FUSION_LOTE_D.txt")
    col = leer("SALIDA_V68_COLISIONES_CIERRE.txt")
    esp = leer("SALIDA_V68_COLISIONES_ESPERADAS.txt")
    dif = leer("SALIDA_V68_DIFF_DUPLICADAS.txt")
    rec = leer("SALIDA_V68_RECOMPUTO_CIERRE.txt")
    rea = leer("SALIDA_V68_REANCLAJE.txt")
    gate = leer("SALIDA_V68_GATE0.txt")
    tra = leer("SALIDA_V68_TRAMO_CIERRE.txt")

    c = {
        "antes_vivos": busca(fus, r"censo ANTES  : \d+ ficheros, (\d+) vivos", "vivos antes"),
        "despues_vivos": busca(fus, r"censo DESPUES: \d+ ficheros, (\d+) vivos", "vivos despues"),
        "mueren": busca(fus, r"nodos que MUEREN\s+: (\d+)", "nodos que mueren"),
        "piezas": busca(fus, r"piezas repartidas\s+: (\d+)", "piezas"),
        "enteras": busca(fus, r"piezas repartidas\s+: \d+ \((\d+) viajan enteras", "enteras"),
        "yadichas": busca(fus, r"viajan enteras, (\d+) ya estaban dichas", "ya dichas"),
        "tocados": busca(fus, r"ESCRITO\. ficheros tocados: (\d+)", "ficheros tocados"),
        "p16": busca(fus, r"P\.16, DUPLICADAS QUE LA PROPIA FUSION FABRICA[^:]*: (\d+)", "P.16"),
        "autoaristas": busca(fus, r"AUTO-ARISTAS que la fusion habria creado y se retiran: (\d+)",
                             "auto-aristas retiradas"),
        "redirecciones": busca(fus, r"redirecciones sobre nodos VIVOS: (\d+)", "redirecciones"),
        "pasivo_antes": busca(fus, r"ANTES de la operacion \(pasivo historico, OP-S-12\): (\d+)",
                              "pasivo antes"),
        "pasivo_despues": busca(fus, r"DESPUES de la operacion\s+: (\d+)", "pasivo despues"),
        "col_base": busca(esp, r"linea base : (\d+)", "linea base"),
        "col_med": busca(col, r"COLISIONES DE CLASE VIGENTES\s+: (\d+)", "colisiones medidas"),
        "col_esp": busca(esp, r"ESPERADAS TRAS FUNDIR = (\d+)", "colisiones esperadas"),
        "col_nuevas": busca(esp, r"colisiones NUEVAS que la fusion fabricaria : (\d+)", "nuevas"),
        "col_calza": busca(col, r"CALZA: (\w+)", "calza"),
        "dup_fab": busca(dif, r"GRUPOS FABRICADOS DE VERDAD: (\d+)", "duplicadas fabricadas"),
        "dup_ren": busca(dif, r"RENOMBRADOS \(aparecen con rotulo nuevo pero son el MISMO grupo\): (\d+)",
                         "renombrados"),
        "dup_antes": busca(dif, r"grupos ya RESUELTOS\s+: antes (\d+)", "grupos antes"),
        "dup_despues": busca(dif, r"grupos ya RESUELTOS\s+: antes \d+ \| despues (\d+)", "grupos despues"),
        "actos": busca(rec, r"actos \(componentes >=2\): (\d+)", "actos"),
        "abiertos": busca(rec, r"ABIERTOS: (\d+) sobre", "abiertos"),
        "abiertos_n": busca(rec, r"ABIERTOS: \d+ sobre (\d+) nodos", "nodos abiertos"),
        "gate_activos": busca(gate, r"valor: (\d+) activos, \d+ deprecados", "activos del Gate 0"),
        "gate_deprecados": busca(gate, r"valor: \d+ activos, (\d+) deprecados", "deprecados del Gate 0"),
        "quedan_actos": busca(tra, r"quedan actos\s+: (\d+)", "actos que quedan"),
        "quedan_nodos": busca(tra, r"quedan nodos\s+: (\d+)", "nodos que quedan"),
        "siguiente": busca(tra, r"el siguiente del prefijo\s+: el acto (\d+)", "siguiente"),
        "quedan_puente": busca(tra, r"con nodo puente\s+: (\d+)", "con puente"),
        "quedan_puente_cuales": busca(tra, r"con nodo puente\s+: \d+ \(actos ([^)]+)\)", "cuales con puente"),
        "declarados_espera": busca(tra, r"esperan el cierre de la fase 03: (\d+)", "declarados en espera"),
        "declarados_cuales": busca(tra, r"esperan el cierre de la fase 03: \d+ \(actos ([^)]+)\)", "cuales declarados"),
        "reanclaje": ("NADA QUE RE-ANCLAR"
                      if "nada que re-anclar" in rea else "RE-ANCLAJES"),
    }
    print()
    print("  --- CELDAS EXTRAIDAS POR AGUJA (ninguna tecleada) ---")
    for k, v in sorted(c.items()):
        print("     %-16s %s" % (k, v))
    if FALLOS:
        print()
        print("ROJO: %d celda(s) no se pudieron leer y NO se escribe nada:" % len(FALLOS))
        for f in FALLOS:
            print("   %s" % f)
        return 1

    crecimientos = {}
    for n in (19, 22):
        m = re.search(r"ACTO %d \. sobrevive.*?pasos (\d+) -> (\d+).*?condiciones (\d+) -> (\d+)"
                      % n, fus, re.S)
        if not m:
            print("ROJO: no se pudo leer el crecimiento del acto %d" % n)
            return 1
        crecimientos["p%da" % n], crecimientos["p%db" % n] = m.group(1), m.group(2)
        crecimientos["c%da" % n], crecimientos["c%db" % n] = m.group(3), m.group(4)

    t = TEXTO % dict(
        c, **dict(crecimientos, **{
            "rep19": tabla_reparto(actos[19]), "abs19": tabla_por_absorbido(actos[19]),
            "per19": tabla_perdidas(19),
            "rep22": tabla_reparto(actos[22]), "abs22": tabla_por_absorbido(actos[22]),
            "per22": tabla_perdidas(22),
            "dec20": tabla_declarado(decl[20]), "dec21": tabla_declarado(decl[21]),
            "dec23": tabla_declarado(decl[23]), "dec24": tabla_declarado(decl[24]),
        }))
    if FALLOS:
        print()
        print("ROJO: %d fallo(s) al armar las tablas y NO se escribe nada:" % len(FALLOS))
        for f in FALLOS:
            print("   %s" % f)
        return 1

    # LA GUARDA DE CITAS ENSANCHADA, IMPORTADA Y NO COPIADA: se le ponen las
    # agujas de este registro y se corre sobre el texto YA armado, o sea sobre
    # lo que de verdad se va a adosar, tablas incluidas.
    # LAS CELDAS EXTRAIDAS POR AGUJA SON CIFRAS DE INSTRUMENTO, NO TECLEADAS, y
    # por eso entran a la lista de numeros declarados con ese motivo: la red
    # ancha existe para cazar lo TECLEADO, y una celda leida de una salida no lo
    # es. Se anaden con su procedencia dicha, no en silencio.
    numeros = dict(MIS_NUMEROS)
    for k, v in list(c.items()) + list(crecimientos.items()):
        if isinstance(v, str) and v.isdigit():
            numeros[v] = "celda %s, extraida por aguja de una salida de la vuelta" % k
    G.AGUJAS, G.ANCLAS, G.NUMEROS_DECLARADOS = MIS_AGUJAS, MIS_ANCLAS, numeros
    G._CACHE.clear()
    fallos = []
    derivadas = G.derivar(fallos)
    usos = {}
    t = G.sustituir(t, derivadas, fallos, usos)
    G.cotejar_texto(t, derivadas, fallos, usos)
    for mal, nombre in ((chr(8212), "guion largo"), (chr(8211), "guion medio")):
        if mal in t:
            fallos.append("el texto trae un %s" % nombre)
    if G.RE_MARCA.search(t) or G.RE_VERBATIM.search(t):
        fallos.append("quedan marcas sin sustituir en el texto final")
    print()
    print("  agujas derivadas: %d | FALLOS: %d" % (len(derivadas), len(fallos)))
    if fallos:
        print()
        print("ROJO: %d fallo(s) y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

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
    # RE-COTEJO TRAS ADOSAR, sobre LAS LINEAS DE ARRIBA SOLAS.
    G._CACHE.clear()
    G.lineas_de(PAGINA)
    G._CACHE[PAGINA] = G._CACHE[PAGINA][:antes]
    re_fallos = []
    re_derivadas = G.derivar(re_fallos, callado=True)
    movidas = [k for k in derivadas
               if k in re_derivadas and re_derivadas[k][0] != derivadas[k][0]]
    print("  las sedes de arriba siguen en su linea: %s"
          % ("OK (%d de %d)" % (len(derivadas), len(derivadas)) if not movidas and not re_fallos
             else "ROJO: %s %s" % (movidas, re_fallos)))
    if movidas or re_fallos:
        return 1
    print()
    print("VERDE: registro adosado y nada de arriba reescrito.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
