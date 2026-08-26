# -*- coding: utf-8 -*-
"""_v70_construir_registro_lote.py . ARMA scripts/loop/vuelta70_registro_lote_f.py
COPIANDO POR EXTRACCION LAS CUATRO FUNCIONES DE TABLA DE
scripts/loop/vuelta69_registro_lote_e.py, EN VEZ DE RETECLEARLAS.

POR QUE. Dos registros de la misma pagina no pueden dibujar el reparto distinto
en silencio: tabla_reparto, tabla_por_absorbido, tabla_perdidas y tabla_declarado
vienen copiandose lote a lote desde la vuelta 66. Copiar a mano es retecleaar, y
retecleaar es por donde una copia diverge. Este fichero las EXTRAE con un assert
por pieza y comprueba despues que aparecen LITERALES en el destino.

LO QUE CAMBIA RESPECTO DEL ANCESTRO, Y ES SOLO ESTO:
  1. tabla_perdidas lee la salida del tallador de ESTA vuelta. El nombre del
     fichero es el UNICO cambio dentro de una funcion copiada y va con assert.
  2. tabla_declarado se copia ENTERA pero NO SE LLAMA: este lote no tiene ningun
     acto DECLARADO Y NO FUNDIDO. Se copia igual porque la adjudicacion 3 del
     acta 69 congelo esa tabla, y una tabla congelada no se recorta ni se
     ensancha: se deja como esta.
  3. MOTIVO_SELLADO queda vacio, por lo mismo: sin declarados no hay motivo que
     imprimir, y no se inventa ninguno.
  4. Las AGUJAS, los NUMEROS declarados, las CELDAS y el texto son propios.

LA GUARDA DE CITAS SE IMPORTA Y NO SE RE-IMPLEMENTA: el registro del lote importa
derivar, negativas, sustituir y cotejar_texto de
scripts/loop/vuelta70_registrar_acta69.py, que es de ESTA MISMA VUELTA. Es el
carril del D14 del acta 68: importar vale dentro de la misma vuelta, donde los
dos instrumentos nacen juntos y no pueden divergir; lo que se copia es la maquina
de una vuelta a otra.

Uso: python scripts/loop/_v70_construir_registro_lote.py
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANCESTRO = os.path.join(RAIZ, "scripts", "loop", "vuelta69_registro_lote_e.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop", "vuelta70_registro_lote_f.py")
NL = chr(10)

CABECERA = '''# -*- coding: utf-8 -*-
"""vuelta70_registro_lote_f.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DEL LOTE F DEL TRAMO UNICO DE OP-U-02, BAJO LA CABECERA DE TRAMO QUE LA
VUELTA 65 YA ADOSO.

NO REESCRIBE NI UNA LINEA DE ARRIBA: abre el fichero en modo adosar.

NINGUNA TABLA SE TECLEA (regla 1): la del reparto pieza a pieza y la de las
piezas por absorbido SE GENERAN del PLAN SELLADO docs/loop/PLAN_V70_OPU02_LOTE_F.json;
la de las perdidas se RECORTA ENTERA de la salida del tallador; y las celdas de
guardas, colisiones, censos y cuentas se EXTRAEN POR AGUJA de las salidas de esta
vuelta. La celda que no se pueda leer de su fichero es ROJO y NO SE ESCRIBE NADA.

LAS CUATRO FUNCIONES QUE ARMAN TABLA SE COPIAN LITERAL del registro del lote E, y
NO A MANO: las extrae scripts/loop/_v70_construir_registro_lote.py con un assert
por pieza. LA TABLA NO CRECE Y NO SE RECORTA, que es la adjudicacion 3 del acta
69: tabla_declarado se copia entera aunque este lote NO la use, porque no tiene
ningun acto DECLARADO Y NO FUNDIDO.

LA GUARDA DE CITAS SE IMPORTA Y NO SE RE-IMPLEMENTA: este fichero importa
derivar, negativas, sustituir y cotejar_texto de
scripts/loop/vuelta70_registrar_acta69.py y les pone SUS PROPIAS agujas. Es el
carril del D14 del acta 68: importar vale DENTRO DE LA MISMA VUELTA.

GUARDA DE IDEMPOTENCIA: si la cabecera de este lote ya esta, no escribe, y se
mira ANTES de derivar nada.

Uso:
  python scripts/loop/vuelta70_registro_lote_f.py [--simular]
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
PLAN = os.path.join(LOOP, "PLAN_V70_OPU02_LOTE_F.json")
NL = chr(10)
CABECERA = "OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE F"
ACTOS_DEL_LOTE = (32, 33, 34, 35, 36)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta70_registrar_acta69 as G  # noqa: E402
from _v70_texto_lote_f import TEXTO  # noqa: E402

# LAS AGUJAS DE ESTE REGISTRO. CLAVE -> (fichero, aguja de CONTENIDO).
MIS_AGUJAS = {
    "PAG_TRAMO_CABECERA": (PAGINA, "TRAMO UNICO Y FINAL POR AGOTAMIENTO: EL REGISTRO DEL LOTE A"),
    "PAG_LOTE_C": (PAGINA, "## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE C`"),
    "PAG_LOTE_D": (PAGINA, "## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE D`"),
    "PAG_LOTE_E": (PAGINA, "## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE E`"),
    "PAG_ADJ_ACTO31": (PAGINA, "### e) **ADJUDICACION 2: EL `ACTO 31`"),
    "PAG_ADJ_SIN_PUENTES": (PAGINA, "### g) **ADJUDICACION 4: EL RESTO DEL TRAMO"),
    "PAG_ACTA69_BASE": (PAGINA, "### d) **ADJUDICACION 1: LA LINEA BASE OPERATIVA"),
    "PAG_ACTO1_P10": (PAGINA, "### a) **EL ACTO 1: `DECLARADO Y NO FUNDIDO` POR `P.10`"),
    "PAG_GUARDA_1B": (PAGINA, "### c) **UN ACTO CON DOS O MAS PUERTAS CIERRA `DECLARADO Y NO FUNDIDO`"),
    "PAG_P5_MOTIVO": (PAGINA, "### b) **UN ACTO CUYO `P.5` CONTESTA QUE NO ES UNA FAMILIA CIERRA"),
    "PAG_CUARTO_MOTIVO": (PAGINA, "### d) **EL CUARTO MOTIVO SELLADO DEL `DECLARADO Y NO FUNDIDO`"),
    "PAG_DUENO_MEDIDO": (PAGINA, "### e) **LA PREGUNTA 5, ADJUDICADA: UN ESTADO DE INVENTARIO"),
    "PAG_CUENTA_AGREGADA": (PAGINA, "> **LA REGLA QUE SALE DE ESTA CAIDA, y vale desde hoy para todo lote:**"),
    "PAG_D10_POR_PIEZA": (PAGINA, "LA FILA DEL CONTRATO ES POR PIEZA QUE SE PIERDE, NO POR SITIO DONDE VIVIA"),
    "PAG_LINEA_BASE": (PAGINA, "### c) **UNA COLISION QUE FABRICA UNA FUSION TIENE DE DUENA A QUIEN LA FABRICA"),
}
MIS_ANCLAS = {}
# Numeros de 3 a 5 digitos que el texto pone en negrita y NO son citas de linea,
# declarados uno a uno con su motivo.
MIS_NUMEROS = {
    "908": "puesto A interno del acto 32",
    "1507": "puesto A interno del acto 32, el que declara la familia de TRES",
    "403": "puesto A interno del acto 33, el que declara el superviviente",
    "1510": "puesto A interno del acto 33",
    "279": "puesto B contra el absorbido del acto 33, una de las dos mitades de la colision nueva",
    "721": "puesto D contra el superviviente del acto 33, la otra mitad de la colision nueva",
    "2233": "puesto A interno del acto 34, el que corona a dysfunctional sobre ciclo_de_culpa",
    "2272": "puesto A interno del acto 34, el que corona a ciclo_de_culpa_2 sobre ciclo_de_culpa",
    "178": "puesto A interno del acto 35",
    "880": "puesto A interno del acto 35, el que declara la pieza a salvar",
    "2562": "puesto A interno del acto 36, el que sella la linea a reponer",
    "2639": "puesto A interno del acto 36, el que trae el DISCUTIBLE MARCADO de su autor",
    "256": "el tamano del universo protegido de puertas",
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
'''

CIERRE = '''

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("REGISTRO DEL LOTE F DEL TRAMO UNICO DE OP-U-02 EN 03_FUSIONES.md")
    print("=" * 78)

    crudo = io.open(PAGINA, encoding="utf-8").read()
    if CABECERA in crudo:
        print()
        print("YA ADOSADO: el registro del lote F ya esta en la pagina. No se escribe nada.")
        return 0

    plan = json.load(io.open(PLAN, encoding="utf-8"))
    actos = {x["orden"]: x for x in plan["actos"]}
    if plan.get("declarados_y_no_fundidos"):
        FALLOS.append("el plan trae declarados y este registro no los sabe imprimir")

    fus = leer("SALIDA_V70_FUSION_LOTE_F.txt")
    col = leer("SALIDA_V70_COLISIONES_CIERRE.txt")
    esp = leer("SALIDA_V70_COLISIONES_ESPERADAS.txt")
    dif = leer("SALIDA_V70_DIFF_DUPLICADAS.txt")
    rec = leer("SALIDA_V70_RECOMPUTO_CIERRE.txt")
    rea = leer("SALIDA_V70_REANCLAJE.txt")
    gate = leer("SALIDA_V70_GATE0.txt")
    tra = leer("SALIDA_V70_TRAMO_CIERRE.txt")
    pue = leer("SALIDA_V70_PUENTES_DE_LOS_QUE_QUEDAN.txt")
    ate = leer("SALIDA_V70_CUENTA_ATENUANTES.txt")

    # LOS PARES D INTERNOS DE LOS QUE QUEDAN NO TIENEN LINEA DE RESUMEN EN LA
    # SALIDA DEL INSTRUMENTO, asi que se CUENTAN de su tabla y no se teclean:
    # una fila por acto, la columna D es la quinta.
    filas_pue = re.findall(r"^\\s*(\\d+)\\s+\\d+\\s+\\d+\\s+\\d+\\s+(\\d+)\\s+\\d+\\s+\\d+\\s+\\d+\\s*$",
                           pue, re.M)
    con_d = len([f for f in filas_pue if int(f[1])])
    if not filas_pue:
        FALLOS.append("no se pudo leer la tabla de resumen de los puentes de los que quedan")

    c = {
        "antes_vivos": busca(fus, r"censo ANTES  : \\d+ ficheros, (\\d+) vivos", "vivos antes"),
        "despues_vivos": busca(fus, r"censo DESPUES: \\d+ ficheros, (\\d+) vivos", "vivos despues"),
        "mueren": busca(fus, r"nodos que MUEREN\\s+: (\\d+)", "nodos que mueren"),
        "piezas": busca(fus, r"piezas repartidas\\s+: (\\d+)", "piezas"),
        "enteras": busca(fus, r"piezas repartidas\\s+: \\d+ \\((\\d+) viajan enteras", "enteras"),
        "yadichas": busca(fus, r"viajan enteras, (\\d+) ya estaban dichas", "ya dichas"),
        "tocados": busca(fus, r"ESCRITO\\. ficheros tocados: (\\d+)", "ficheros tocados"),
        "p16": busca(fus, r"P\\.16, DUPLICADAS QUE LA PROPIA FUSION FABRICA[^:]*: (\\d+)", "P.16"),
        "autoaristas": busca(fus, r"AUTO-ARISTAS que la fusion habria creado y se retiran: (\\d+)",
                             "auto-aristas retiradas"),
        "redirecciones": busca(fus, r"redirecciones sobre nodos VIVOS: (\\d+)", "redirecciones"),
        "pasivo_antes": busca(fus, r"ANTES de la operacion \\(pasivo historico, OP-S-12\\): (\\d+)",
                              "pasivo antes"),
        "pasivo_despues": busca(fus, r"DESPUES de la operacion\\s+: (\\d+)", "pasivo despues"),
        "campos_intactos": busca(fus, r"NO redacta, intactos: (\\d+ de \\d+)", "campos intactos"),
        "col_base": busca(esp, r"linea base : (\\d+)", "linea base"),
        "col_med": busca(col, r"COLISIONES DE CLASE VIGENTES\\s+: (\\d+)", "colisiones medidas"),
        "col_esp": busca(esp, r"ESPERADAS TRAS FUNDIR = (\\d+)", "colisiones esperadas"),
        "col_nuevas": busca(esp, r"colisiones NUEVAS que la fusion fabricaria : (\\d+)", "nuevas"),
        "col_idas": busca(esp, r"colisiones que DESAPARECERIAN\\s+: (\\d+)", "idas"),
        "col_calza": busca(col, r"CALZA: (\\w+)", "calza"),
        "autopares": busca(col, r"AUTO-PARES \\(los dos lados al mismo vivo\\): (\\d+)", "auto-pares"),
        "dup_fab": busca(dif, r"GRUPOS FABRICADOS DE VERDAD: (\\d+)", "duplicadas fabricadas"),
        "dup_ren": busca(dif, r"RENOMBRADOS \\(aparecen con rotulo nuevo pero son el MISMO grupo\\): (\\d+)",
                         "renombrados"),
        "dup_antes": busca(dif, r"grupos ya RESUELTOS\\s+: antes (\\d+)", "grupos antes"),
        "dup_despues": busca(dif, r"grupos ya RESUELTOS\\s+: antes \\d+ \\| despues (\\d+)", "grupos despues"),
        "abiertos": busca(rec, r"ABIERTOS: (\\d+) sobre", "abiertos"),
        "abiertos_n": busca(rec, r"ABIERTOS: \\d+ sobre (\\d+) nodos", "nodos abiertos"),
        "gate_activos": busca(gate, r"valor: (\\d+) activos, \\d+ deprecados", "activos del Gate 0"),
        "gate_deprecados": busca(gate, r"valor: \\d+ activos, (\\d+) deprecados", "deprecados del Gate 0"),
        "quedan_actos": busca(tra, r"QUEDAN SIN DESTINO: (\\d+) actos y \\d+ nodos", "actos que quedan"),
        "quedan_nodos": busca(tra, r"QUEDAN SIN DESTINO: \\d+ actos y (\\d+) nodos", "nodos que quedan"),
        "siguiente": busca(tra, r"el siguiente del prefijo: acto (\\d+)", "siguiente"),
        "con_dueno": busca(tra, r"de los que quedan, CON DUENO medido: (\\d+)", "con dueno"),
        "fundidos_medidos": busca(tra, r"actos FUNDIDOS, medido \\(ningun miembro vivo, o uno solo\\): (\\d+)",
                                  "actos fundidos medidos"),
        "declarados_arg": busca(tra, r"DECLARADOS Y NO FUNDIDOS \\(argumento\\): (\\d+)", "declarados"),
        "actos_mirados": busca(pue, r"actos mirados\\s+: (\\d+)", "actos mirados"),
        "actos_sin_puente": busca(pue, r"actos SIN ningun nodo puente\\s+: (\\d+)", "actos sin puente"),
        "quedan_puente": busca(pue, r"actos CON al menos un nodo puente\\s+: (\\d+)", "actos con puente"),
        "quedan_d": str(con_d),
        "per_total": busca(ate, r"perdidas selladas, en total\\s+: (\\d+)", "perdidas totales"),
        "per_paso": busca(ate, r"DE PARAMETRO DE PASO\\s+: (\\d+)", "perdidas de paso"),
        "per_cond": busca(ate, r"DE CONDICIONES\\s+: (\\d+)", "perdidas de condiciones"),
        "per_aten": busca(ate, r"filas con ATENUANTE DECLARADO\\s+: (\\d+)", "filas con atenuante"),
        "per_p4": busca(ate, r"de la ESPECIE DEL PENDIENTE 4\\s+: (\\d+)", "filas del pendiente 4"),
        "per_medido": busca(ate, r"con ATENUANTE DECLARADO Y MEDIDO\\s+: (\\d+)", "filas con atenuante medido"),
        "per_dos_sedes": busca(ate, r"filas con DOS SEDES en el campo donde : (\\d+)", "filas de dos sedes"),
        "per_contraria": busca(ate, r"seria (\\d+) y no \\d+", "la aritmetica contraria"),
        "reanclaje": ("NADA QUE RE-ANCLAR" if "nada que re-anclar" in rea else "RE-ANCLAJES"),
    }
    print()
    print("  --- CELDAS EXTRAIDAS POR AGUJA (ninguna tecleada) ---")
    for k, v in sorted(c.items()):
        print("     %-18s %s" % (k, v))
    if FALLOS:
        print()
        print("ROJO: %d celda(s) no se pudieron leer y NO se escribe nada:" % len(FALLOS))
        for f in FALLOS:
            print("   %s" % f)
        return 1

    crecimientos = {}
    for n in ACTOS_DEL_LOTE:
        m = re.search(r"ACTO %d \\. sobrevive.*?pasos (\\d+) -> (\\d+).*?condiciones (\\d+) -> (\\d+)"
                      % n, fus, re.S)
        if not m:
            print("ROJO: no se pudo leer el crecimiento del acto %d" % n)
            return 1
        crecimientos["p%da" % n], crecimientos["p%db" % n] = m.group(1), m.group(2)
        crecimientos["c%da" % n], crecimientos["c%db" % n] = m.group(3), m.group(4)

    tablas = {}
    for n in ACTOS_DEL_LOTE:
        tablas["rep%d" % n] = tabla_reparto(actos[n])
        tablas["abs%d" % n] = tabla_por_absorbido(actos[n])
        tablas["per%d" % n] = tabla_perdidas(n)

    t = TEXTO % dict(c, **dict(crecimientos, **tablas))
    if FALLOS:
        print()
        print("ROJO: %d fallo(s) al armar las tablas y NO se escribe nada:" % len(FALLOS))
        for f in FALLOS:
            print("   %s" % f)
        return 1

    # LA GUARDA DE CITAS, IMPORTADA, sobre el texto YA armado. Las celdas
    # extraidas por aguja son cifras de instrumento y entran a los numeros
    # declarados CON SU PROCEDENCIA DICHA: la red ancha existe para cazar lo
    # TECLEADO, y una celda leida de una salida no lo es.
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
'''


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    src = io.open(ANCESTRO, encoding="utf-8").read()
    print("=" * 78)
    print("CONSTRUCCION DE vuelta70_registro_lote_f.py POR EXTRACCION DEL ANCESTRO")
    print("  ancestro: %s (%d lineas)" % (os.path.basename(ANCESTRO), len(src.split(NL))))
    print("=" * 78)

    i = src.index("# --- COPIADAS LITERAL de vuelta68_registro_lote_d.py")
    f = src.index("def main():")
    tablas = src[i:f]
    for pieza in ("def tabla_reparto(", "def tabla_por_absorbido(", "def tabla_perdidas(",
                  "def tabla_declarado(", "MOTIVO_SELLADO = {"):
        assert pieza in tablas, pieza
    print("  LAS CUATRO TABLAS       : %d lineas, EXTRAIDAS (5 piezas comprobadas)"
          % tablas.count(NL))

    cambios = [
        ('    t = leer("SALIDA_V69_TALLAR_PERDIDAS.txt")',
         '    t = leer("SALIDA_V70_TALLAR_PERDIDAS.txt")'),
        ('''MOTIVO_SELLADO = {
    27: "**`P.10`**, con su triangulo MEDIDO (el carril registrado en la linea "
        "**[[PAG_ACTO1_P10]]**), **mas el ejemplar de la figura `ESTRELLA (9.23)` que una "
        "fusion entera borraria**, que es la misma forma del `acto 24` de la vuelta 68",
}''',
         '''# ESTE LOTE NO TIENE NINGUN ACTO DECLARADO Y NO FUNDIDO, asi que el mapa queda
# VACIO y tabla_declarado no se llama. Se copia igual y no se recorta: la
# adjudicacion 3 del acta 69 congelo esa tabla, y una tabla congelada tampoco se
# encoge.
MOTIVO_SELLADO = {}'''),
    ]
    for viejo, nuevo in cambios:
        assert tablas.count(viejo) == 1, viejo[:60]
        tablas = tablas.replace(viejo, nuevo)
    print("  CAMBIOS DECLARADOS      : 2 (el fichero del tallador y el mapa de motivos)")

    # EL ROTULO DEL FICHERO HIJO, EXTRAIDO DEL ANCESTRO Y NO TECLEADO AQUI, por
    # el mismo motivo que en el constructor del registrador del acta: un rotulo
    # escrito DENTRO del constructor es HUERFANO para el barrido de titulos,
    # porque el titulo que cubre es el del hijo. El barrido lo cazo hoy.
    i4 = src.index("# ROTULO titulo")
    f4 = src.index(NL, i4)
    rotulo = src[i4:f4]
    viejo_r, nuevo_r = "el fichero es de la vuelta 69", "el fichero es de la vuelta 70"
    assert rotulo.count(viejo_r) == 1
    rotulo = rotulo.replace(viejo_r, nuevo_r)
    print("  EL ROTULO DEL HIJO      : EXTRAIDO con 1 campo cambiado")

    salida = CABECERA + rotulo + NL + NL + tablas.rstrip(NL) + NL + CIERRE
    for mal, nombre in ((chr(8212), "guion largo"), (chr(8211), "guion medio")):
        assert mal not in salida, nombre
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(salida)
    print()
    print("ESCRITO %s (%d lineas)" % (os.path.basename(DESTINO), len(salida.split(NL))))

    nuevo = io.open(DESTINO, encoding="utf-8").read()
    for pieza in ("def tabla_reparto(", "def tabla_por_absorbido(", "def tabla_perdidas(",
                  "def tabla_declarado("):
        assert pieza in nuevo, pieza
    # LA PRUEBA DE QUE NO SE RETECLEO: las tres funciones que NO cambian tienen
    # que aparecer LITERALES, tal como estan en el ancestro.
    for nombre_f in ("tabla_reparto", "tabla_por_absorbido", "tabla_declarado"):
        a = src.index("def %s(" % nombre_f)
        b = src.index(NL + NL, a)
        cuerpo = src[a:b]
        ok = cuerpo in nuevo
        print("  %-22s aparece LITERAL en el destino : %s" % (nombre_f, ok))
        assert ok, nombre_f
    print()
    print("VERDE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
