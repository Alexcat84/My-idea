# -*- coding: utf-8 -*-
"""_v62_corregir_registrador.py . APLICA LAS CINCO CORRECCIONES DECLARADAS A
scripts/loop/registrar_cierre_de_tramo.py.

NO ES UN INSTRUMENTO DE MEDIDA: es el andamio que aplica los cambios con un
assert por cada uno, para que la correccion no dependa de que un dedo acierte.
Se corre UNA vez; volver a correrlo sobre el fichero ya corregido cae en rojo en
el primer assert, que es lo que se quiere.

POR QUE HACEN FALTA, medido y no supuesto: el registrador es de NOMBRE ESTABLE y
se estreno en el tramo 5, pero llevaba TRES bloques de su plantilla TALLADOS A
MANO CON LAS CIFRAS DE AQUEL TRAMO, mas DOS marcas de recorte atadas a la letra
exacta de dos talladores que esta vuelta cambio. Corrido tal cual sobre el tramo
6, el registro habria publicado "50 actos mirados, 34 vivos, 16 ya fundidos" y
"0 / 50" en un tramo de VEINTIUNO, y habria afirmado que el lote A ya estaba
fundido al tomar la apertura, que aqui es falso.
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(RAIZ, "scripts", "loop", "registrar_cierre_de_tramo.py")

NL = chr(10)
L = io.open(P, encoding="utf-8", newline="").read().split(NL)


def solo(pred, que):
    i = [k for k, l in enumerate(L) if pred(l)]
    assert len(i) == 1, ("no casa una sola vez: %s -> %s" % (que, i))
    return i[0]


# ---------------------------------------------------------------- CORRECCION 1
# El recorte de la TABLA 1 buscaba la marca ENTERA, y esa marca tallaba "LOS
# TRES LOTES" en el tallador. Al corregir alli el rotulo (el tramo 6 tiene DOS
# lotes) este recorte deja de casar y el registro cae en ROJO sin escribir.
i = solo(lambda l: l.strip().startswith("t1 = recorta("), "recorte de la tabla 1")
L[i] = NL.join([
    '    # CORRECCION DECLARADA (20 ago 2026, vuelta 62): este recorte buscaba la',
    '    # marca ENTERA de la TABLA 1, y esa marca tallaba la cuenta de lotes a mano',
    '    # en el tallador ("LOS TRES LOTES"). Al corregir alli el rotulo, porque el',
    '    # tramo 6 tiene DOS lotes, el recorte dejaba de casar y este registro caia',
    '    # en ROJO sin escribir. EL TEXTO VIEJO SE QUEDA ESCRITO Y DECIA:',
    '    #     t1 = recorta(tal, "--- TABLA 1: LOS TRES LOTES, CON SUS PIEZAS ---", ...)',
    '    # Ahora se busca por el PREFIJO de la marca, que no lleva la cuenta dentro.',
    '    t1 = recorta(tal, "--- TABLA 1:", "--- TABLA 2", "tabla 1", fallos)',
])

# ---------------------------------------------------------------- CORRECCION 2
# El bloque de perdidas solo conocia la marca y el pie del tallador VIEJO. El
# nuevo (contrato CAMPO PROPIO v1) abre y cierra su tabla con otras. Sin esto el
# registro habria publicado una FALTA DE TABLA que no existe.
i = solo(lambda l: l.strip().startswith('if per and "--- TABLA: LAS PERDIDAS'),
         "rama de la tabla de perdidas")
assert L[i + 1].strip().startswith("marca = per["), L[i + 1]
assert L[i + 2].strip().startswith("tp = recorta("), L[i + 2]
L[i:i + 3] = [
    '    # CORRECCION DECLARADA (20 ago 2026, vuelta 62): esta rama solo conocia la',
    '    # marca y el pie del tallador VIEJO de perdidas. El tallador nuevo',
    '    # (tallar_perdidas_del_plan.py, contrato CAMPO PROPIO v1) abre su tabla con',
    '    # otra marca y la cierra con otro pie, asi que sin esto el registro habria',
    '    # tomado la rama de NO EMITIO TABLA sobre una salida que SI la emite, o sea',
    '    # habria publicado una falta que no existe. EL TEXTO VIEJO SE QUEDA Y DECIA',
    '    # que la marca era "--- TABLA: LAS PERDIDAS NOMBRADAS" y el pie la linea de',
    '    # los actos con perdida. SE RECONOCEN LAS DOS, la vieja primero.',
    '    MARCAS_PERD = (("--- TABLA: LAS PERDIDAS NOMBRADAS", chr(10) + "  actos con perdida:"),',
    '                   ("--- LA TABLA ---", chr(10) + "  planes leidos"))',
    '    marca_perd = next(((m, pie) for m, pie in MARCAS_PERD if per and m in per), None)',
    '    if marca_perd:',
    '        marca = per[per.find(marca_perd[0]):].split(chr(10), 1)[0]',
    '        tp = recorta(per, marca, marca_perd[1], "tabla de perdidas", fallos)',
]

# --------------------------------------------------- CORRECCIONES 3, 4 y 5
# Los tres bloques de la plantilla que estaban tallados con las cifras del
# tramo 5. Se sustituyen por marcas, y las marcas se rellenan MIDIENDO.
i = solo(lambda l: "31 fusiones donde hay" in l, "frase de las 31 fusiones")
L[i] = "**%(fusiones_falsas)s**, y las cuatro tablas habrian mentido por omision."

i = solo(lambda l: "--prefijo PLAN_V59_OPU01_LOTE_" in l, "comando del tallador")
L[i] = "`%(comando_tallador)s`"

i = solo(lambda l: l.startswith("### EL REPARTO, TALLADO DE LOS PLANES SELLADOS DE LAS DOS VUELTAS"),
         "cabecera del reparto")
L[i] = "### EL REPARTO, TALLADO DE LOS PLANES SELLADOS%(de_las_vueltas)s"

i = solo(lambda l: l.startswith("> **LA COLUMNA DE APERTURA"), "nota de la columna de apertura")
assert L[i + 3].startswith("> es la cifra que si cubre las dos vueltas."), L[i + 3]
L[i:i + 4] = ["%(nota_apertura)s"]

i = solo(lambda l: "| actos del tramo %(tramo)s fundidos / vivos" in l, "fila del tramo")
L[i] = ("| actos del tramo %(tramo)s fundidos / vivos | 0 / %(tam)s | "
        "**%(fund)s / %(vivos_tramo)s** |")

i = solo(lambda l: l.startswith("> **EL COTEJO QUE ESTE TRAMO ESTRENA"), "bloque del cotejo")
assert L[i + 5].startswith("> ([`../loop/SALIDA_V60_COTEJO_INSUMO.txt`]"), L[i + 5]
L[i:i + 6] = ["%(bloque_cotejo)s"]

# El argumento nuevo --cotejo, repetible.
i = solo(lambda l: l.strip().startswith('p.add_argument("--nota"'), "argumento --nota")
L[i:i] = ['    p.add_argument("--cotejo", action="append", default=[],',
          '                   help="salida del cotejo del insumo contra los nodos, repetible")']

# El bloque que rellena las marcas MIDIENDO, justo antes de la fecha.
i = solo(lambda l: l.strip().startswith("hoy = datetime.date.today()"), "la fecha")
BLOQUE = [
    '    # ==================================================================',
    '    # CORRECCION DECLARADA (20 ago 2026, vuelta 62). TRES BLOQUES DE LA',
    '    # PLANTILLA DE ABAJO ESTABAN TALLADOS A MANO CON LAS CIFRAS DEL TRAMO 5, y',
    '    # en un instrumento de NOMBRE ESTABLE eso publica cifras falsas en el tramo',
    '    # siguiente sin que nadie las teclee ese dia. EL TEXTO VIEJO SE QUEDA',
    '    # ESCRITO AQUI, que es lo que hace auditable la correccion:',
    '    #',
    '    #   a) EL BLOQUE DEL COTEJO DEL INSUMO decia, literal, "50 actos mirados, 34',
    '    #      vivos, 16 ya fundidos, DESCALCES 0" y apuntaba a',
    '    #      SALIDA_V60_COTEJO_INSUMO.txt. En el tramo 6 no hay 50 actos: hay 21.',
    '    #      AHORA SE LEE DE LOS FICHEROS QUE ENTRAN POR --cotejo, y si no entra',
    '    #      ninguno el bloque DECLARA su falta en vez de inventar.',
    '    #   b) LA FILA DEL TRAMO decia "0 / 50" en la columna de apertura. AHORA EL',
    '    #      TAMANO SE MIDE, sumando los fundidos y los vivos de la salida del',
    '    #      --fijado.',
    '    #   c) LA NOTA DE LA COLUMNA DE APERTURA afirmaba que el lote A ya estaba',
    '    #      fundido al tomarla, que es cierto en un tramo repartido entre DOS',
    '    #      vueltas y FALSO en uno que abre y cierra en la misma. AHORA SE MIDE,',
    '    #      leyendo las vueltas de los planes que el tallador hallo.',
    '    #',
    '    # LAS CIFRAS DE LAS CUATRO TABLAS NO SE TOCAN EN ESTA CORRECCION.',
    '    # ==================================================================',
    '    d["tam"] = str(int(d["fund"]) + int(d["vivos_tramo"]))',
    '    if d["vivos_tramo"] != "0":',
    '        d["vivos_tramo"] = "%s, los %s DECLARADOS" % (d["vivos_tramo"], d["vivos_tramo"])',
    '',
    '    planes = re.findall(r"\\(PLAN_V(\\d+)_[^)]*\\.json\\)", tal)',
    '    vueltas_de_los_planes = sorted({int(x) for x in planes})',
    '    prefijos = sorted({re.sub(r"[A-Z]\\.json$", "", x) for x in',
    '                       re.findall(r"\\((PLAN_V\\d+_[^)]*\\.json)\\)", tal)})',
    '    d["comando_tallador"] = ("python scripts/loop/tallar_planes_del_tramo.py --vuelta %d %s"',
    '                             % (a.vuelta, " ".join("--prefijo " + x for x in prefijos)))',
    '    d["fusiones_falsas"] = (',
    '        "solo una parte de las fusiones y no las %s" % d["fund"]',
    '        if len(prefijos) > 1 else',
    '        "lo mismo que publica, porque los planes de este tramo caben en UN solo",',
    '    )',
    '    if len(prefijos) > 1:',
    '        d["fusiones_falsas"] = "solo una parte de las fusiones y no las %s" % d["fund"]',
    '    else:',
    '        d["fusiones_falsas"] = ("lo mismo que publica, porque los planes de este tramo caben"',
    '                                " en UN solo prefijo y ahi la repetibilidad no cambia nada")',
    '    d["de_las_vueltas"] = (" DE LAS %d VUELTAS" % len(vueltas_de_los_planes)',
    '                           if len(vueltas_de_los_planes) > 1 else " DE ESTA VUELTA")',
    '',
    '    if len(vueltas_de_los_planes) > 1:',
    '        d["nota_apertura"] = (chr(10).join([',
    '            "> **LA COLUMNA DE APERTURA ES LA DE LA VUELTA QUE CIERRA EL TRAMO, no la de la",',
    '            "> que lo abrio, y se dice para que nadie lea de ahi el efecto del tramo entero.**",',
    '            "> Los lotes de las vueltas anteriores (%s) ya estaban fundidos cuando se tomo. El",',
    '            "> efecto del TRAMO COMPLETO se lee de los `%s` actos fundidos de la ultima fila,",',
    '            "> que es la cifra que si cubre las %d vueltas.",',
    '        ]) % (", ".join(str(x) for x in vueltas_de_los_planes[:-1]), d["fund"],',
    '              len(vueltas_de_los_planes)))',
    '    else:',
    '        d["nota_apertura"] = (chr(10).join([',
    '            "> **EL TRAMO ABRE Y CIERRA DENTRO DE ESTA MISMA VUELTA, medido y no supuesto: los",',
    '            "> %d planes sellados que el tallador hallo son TODOS de la vuelta %d.** Por eso la",',
    '            "> columna de apertura SI precede al tramo entero: cuando se tomo no habia ni un",',
    '            "> acto de este tramo fundido, y la diferencia entre las dos columnas es el efecto",',
    '            "> del tramo completo.",',
    '        ]) % (len(planes), vueltas_de_los_planes[0]))',
    '',
    '    if a.cotejo:',
    '        piezas = []',
    '        for ruta in a.cotejo:',
    '            texto = leer(ruta, fallos)',
    '            resumen = busca(texto, r"(RESUMEN: actos mirados .*)", "resumen del cotejo", fallos)',
    '            piezas.append("> **%s**" % resumen.strip() + chr(10) +',
    '                          "> ([`../loop/%s`](../loop/%s))"',
    '                          % (os.path.basename(ruta), os.path.basename(ruta)))',
    '        d["bloque_cotejo"] = (chr(10).join([',
    '            "> **EL COTEJO DEL INSUMO, CORRIDO ANTES DE ESCRIBIR UNA LINEA DE CADA PLAN:** el",',
    '            "> insumo se midio y se FIJO al abrir el tramo y no se re-mide, pero entre aquella",',
    '            "> foto y hoy puede haberse fundido un lote del mismo tramo, y una fusion CAMBIA los",',
    '            "> pasos del superviviente. `scripts/loop/vuelta60_cotejo_insumo.py` NO re-mide:",',
    '            "> COTEJA contra los nodos de hoy y dice en que actos la foto dejo de calzar.",',
    '            ">",',
    '        ]) + chr(10) + (chr(10) + ">" + chr(10)).join(piezas))',
    '    else:',
    '        d["bloque_cotejo"] = chr(10).join([',
    '            "> **A ESTE REGISTRO NO SE LE PASO NINGUNA SALIDA DE COTEJO DEL INSUMO, y se dice",',
    '            "> en vez de callarse.** Sin ella este registro no puede afirmar que la foto fijada",',
    '            "> siguiera calzando con los nodos al escribir los planes.",',
    '        ])',
    '',
]
L[i:i] = BLOQUE

io.open(P, "w", encoding="utf-8", newline="").write(NL.join(L))
print("registrador corregido: 5 cambios aplicados con su assert")
