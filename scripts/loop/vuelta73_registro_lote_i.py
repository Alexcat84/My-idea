# -*- coding: utf-8 -*-
"""vuelta73_registro_lote_i.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DEL LOTE I DEL TRAMO UNICO DE OP-U-02, BAJO LA CABECERA DE TRAMO QUE LA
VUELTA 65 YA ADOSO.

NO REESCRIBE NI UNA LINEA DE ARRIBA: abre el fichero en modo adosar.

NINGUNA TABLA SE TECLEA (regla 1): la del reparto pieza a pieza y la de las
piezas por absorbido SE GENERAN del PLAN SELLADO docs/loop/PLAN_V73_OPU02_LOTE_I.json;
la de las perdidas se RECORTA ENTERA de la salida del tallador; y las celdas de
guardas, colisiones, censos y cuentas se EXTRAEN POR AGUJA de las salidas de esta
vuelta. La celda que no se pueda leer de su fichero es ROJO y NO SE ESCRIBE NADA.

LAS CUATRO FUNCIONES QUE ARMAN TABLA SE COPIAN LITERAL del registro del lote H, y
NO A MANO: las extrae scripts/loop/_v73_construir_registro_lote.py con un assert
por pieza. LA TABLA NO CRECE Y NO SE RECORTA, que es la adjudicacion 3 del acta
69, y ESTA VUELTA NO CORRIGE NINGUNA CELDA: la correccion de la vuelta 72 en la
celda de la figura del inventario ya viene aplicada en el ancestro y se copia con
el resto.

ESTE LOTE NO TIENE NINGUN ACTO DECLARADO Y NO FUNDIDO: los cuatro cierran
FUNDIDOS, asi que MOTIVO_SELLADO esta VACIO y tabla_declarado NO SE LLAMA. La
funcion se copia igual y no se borra: el proximo declarado la necesitara, y
borrarla seria ENCOGER la tabla.

LA GUARDA DE CITAS SE IMPORTA Y NO SE RE-IMPLEMENTA: este fichero importa
derivar, negativas, sustituir y cotejar_texto de
scripts/loop/vuelta73_registrar_acta72.py y les pone SUS PROPIAS agujas. Es el
carril del D14 del acta 68: importar vale DENTRO DE LA MISMA VUELTA.

GUARDA DE IDEMPOTENCIA: si la cabecera de este lote ya esta, no escribe, y se
mira ANTES de derivar nada.

Uso:
  python scripts/loop/vuelta73_registro_lote_i.py [--simular]
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
PLAN = os.path.join(LOOP, "PLAN_V73_OPU02_LOTE_I.json")
NL = chr(10)
CABECERA = "OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE I"
# LOS FUNDIDOS Y LOS DECLARADOS VAN EN LISTAS DISTINTAS. En este lote la segunda
# esta VACIA y no es un olvido: los cuatro actos cierran FUNDIDOS.
ACTOS_DEL_LOTE = (49, 50, 51, 53)
DECLARADOS_DEL_LOTE = ()

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta73_registrar_acta72 as G  # noqa: E402
from _v73_texto_lote_i import TEXTO  # noqa: E402

# LAS AGUJAS DE ESTE REGISTRO. CLAVE -> (fichero, aguja de CONTENIDO).
MIS_AGUJAS = {
    "PAG_TRAMO_CABECERA": (PAGINA, "TRAMO UNICO Y FINAL POR AGOTAMIENTO: EL REGISTRO DEL LOTE A"),
    "PAG_LOTE_G": (PAGINA, "## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE G`"),
    "PAG_LOTE_H": (PAGINA, "## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE H`"),
    "PAG_ADJ_ACTO31": (PAGINA, "### e) **ADJUDICACION 2: EL `ACTO 31`"),
    "PAG_GUARDA_1B": (PAGINA, "### c) **UN ACTO CON DOS O MAS PUERTAS CIERRA `DECLARADO Y NO FUNDIDO`"),
    "PAG_PUERTA_UNICA": (PAGINA, "**Y EL CASO DE UNA SOLA PUERTA NO ES ESTE Y SE DICE PARA QUE NO SE CONFUNDAN:**"),
    "PAG_D10_POR_PIEZA": (PAGINA, "LA FILA DEL CONTRATO ES POR PIEZA QUE SE PIERDE, NO POR SITIO DONDE VIVIA"),
    "PAG_LINEA_BASE": (PAGINA, "### c) **UNA COLISION QUE FABRICA UNA FUSION TIENE DE DUENA A QUIEN LA FABRICA"),
    "PAG_ADJ_DUENO": (PAGINA, "### g) **ADJUDICACION 2: LA FRONTERA DEL DUENO SE LEE SOBRE SU SUJETO"),
    "PAG_ADJ_PUERTAS": (PAGINA, "### h) **ADJUDICACION 4: EN LO QUE RESTA DEL TRAMO SI QUEDAN PUERTAS"),
    "PAG_ADJ_CABLEADO": (PAGINA, "### b) **CORRECCION DECLARADA, PRIMERA: LAS DOS CELDAS DE CABLEADO"),
    # las TRES sedes que la TAREA 1 de ESTA vuelta acaba de adosar
    "PAG_ACTA72": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 72, REGISTRADAS AQUI"),
    "PAG_ADJ_P4": (PAGINA, "**LA PRIMERA VA VERBATIM Y NO RESUMIDA, PORQUE ES LA QUE ESTA VUELTA EJECUTA"),
    "PAG_CORR_GLOSA": (PAGINA, "### g) **CORRECCION DECLARADA, UNICA DE ESTA VUELTA: LA GLOSA DE LA ESPECIE"),
}
MIS_ANCLAS = {}
# Numeros de 3 a 5 digitos que el texto pone en negrita y NO son citas de linea,
# declarados uno a uno con su motivo.
MIS_NUMEROS = {
    "241": "puesto A interno del acto 49, el que abre con REPITE y habla de la figura de los ids",
    "1032": "puesto A interno del acto 49, el que titula LA MISMA POLITICA CONTRA LA IA CLANDESTINA",
    "2290": "puesto A interno del acto 50, el que corona a investigacion_new_view",
    "2292": "puesto A interno del acto 50, el que corona a perspectiva_dentro_del_tunel",
    "378": "puesto A interno del acto 51, el que declara la FAMILIA DE TRES",
    "1332": "puesto A interno del acto 51, el del TERCER SUBCONJUNTO ESTRICTO",
    "2616": "puesto A interno del acto 53, el que corona a reconocimiento_al_desempeno",
    "2942": "puesto A interno del acto 53, el que deja escrita la promesa de marcado",
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
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:65 fuente=docs/plan/03_FUSIONES.md prueba="TRAMO UNICO Y FINAL POR AGOTAMIENTO: EL REGISTRO DEL LOTE A" corte=2026-08-26 motivo="el docstring nombra la VUELTA 65 porque es la vuelta que adoso la cabecera de tramo bajo la que este registro se cuelga, derivada hoy por aguja; el fichero es de la vuelta 73 y por eso el numero no calza con su propia vuelta a proposito"

# --- COPIADAS LITERAL de vuelta68_registro_lote_d.py -----------------------
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
    t = leer("SALIDA_V73_TALLAR_PERDIDAS.txt")
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

# ESTE LOTE NO TIENE NINGUN ACTO DECLARADO Y NO FUNDIDO: los CUATRO (49, 50, 51
# y 53) cierran FUNDIDOS. Por eso el mapa esta VACIO y tabla_declarado NO SE
# LLAMA. La funcion se copia igual y no se borra: el proximo declarado la
# necesitara, y borrarla seria ENCOGER la tabla, que es lo que la adjudicacion 3
# del acta 69 prohibe tanto como hacerla crecer. La guarda de main sigue
# mordiendo con el mapa vacio: si el plan trajera un declarado y este mapa no,
# seria ROJO.
MOTIVO_SELLADO = {}


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
    filas.append("| **duenos medidos hoy en el fichero del tramo** | %s |"
                 % ("**%s** en `duenos_cualquier_operacion`"
                    % "`, `".join(med["duenos_cualquier_operacion"])
                    if med.get("duenos_cualquier_operacion") else
                    "**NINGUNO**, los dos campos vacios"))
    # EL ANADIDO DE ESTA VUELTA, dicho en el docstring: la figura del inventario.
    # CORRECCION DECLARADA (vuelta 72, carril del acta 61 D2 y pregunta 2,
    # enumerada en el docstring de _v72_construir_registro_lote.py y MARCADA
    # DISCUTIBLE en el reporte). El texto viejo de esta celda esta citado
    # VERBATIM alli: llevaba tecleada dentro de la funcion la coletilla "y su
    # centro es el MISMO nodo puente que P.10 detecto", cierta para el acto 27
    # de la vuelta 69 y FALSA para un acto declarado por la guarda 1B. La frase
    # la pone ahora el contenido MEDIDO del lote. La tabla no crece ni se encoge.
    filas.append("| **figura del inventario de la que es ejemplar** | %s |"
                 % ("**%s**" % med["figura_del_inventario"]
                    if med.get("figura_del_inventario") else
                    "**NINGUNA**, medido contra `INVENTARIO.jsonl`"))
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
    print("REGISTRO DEL LOTE I DEL TRAMO UNICO DE OP-U-02 EN 03_FUSIONES.md")
    print("=" * 78)

    crudo = io.open(PAGINA, encoding="utf-8").read()
    if CABECERA in crudo:
        print()
        print("YA ADOSADO: el registro del lote I ya esta en la pagina. No se escribe nada.")
        return 0

    plan = json.load(io.open(PLAN, encoding="utf-8"))
    actos = {x["orden"]: x for x in plan["actos"]}
    declarados = {x["acto"]: x for x in plan.get("declarados_y_no_fundidos", [])}
    # LA GUARDA DEL CONTRATO DEL LOTE: lo que el plan trae y lo que este registro
    # sabe imprimir tienen que ser LO MISMO, medido, en las dos direcciones. Con
    # la lista de declarados VACIA la guarda sigue mordiendo: si el plan trajera
    # uno y este registro no lo esperase, seria ROJO.
    if sorted(actos) != sorted(ACTOS_DEL_LOTE):
        FALLOS.append("el plan trae los actos %s y este registro espera %s"
                      % (sorted(actos), sorted(ACTOS_DEL_LOTE)))
    if sorted(declarados) != sorted(DECLARADOS_DEL_LOTE):
        FALLOS.append("el plan trae los declarados %s y este registro espera %s"
                      % (sorted(declarados), sorted(DECLARADOS_DEL_LOTE)))
    if sorted(MOTIVO_SELLADO) != sorted(DECLARADOS_DEL_LOTE):
        FALLOS.append("hay motivo sellado para %s y declarados para %s"
                      % (sorted(MOTIVO_SELLADO), sorted(DECLARADOS_DEL_LOTE)))

    fus = leer("SALIDA_V73_FUSION_LOTE_I.txt")
    col = leer("SALIDA_V73_COLISIONES_CIERRE.txt")
    esp = leer("SALIDA_V73_COLISIONES_ESPERADAS.txt")
    dif = leer("SALIDA_V73_DIFF_DUPLICADAS.txt")
    rec = leer("SALIDA_V73_RECOMPUTO_CIERRE.txt")
    rea = leer("SALIDA_V73_REANCLAJE.txt")
    gate = leer("SALIDA_V73_GATE0.txt")
    tra = leer("SALIDA_V73_TRAMO_CIERRE.txt")
    pue = leer("SALIDA_V73_PUENTES_DE_LOS_QUE_QUEDAN.txt")
    ate = leer("SALIDA_V73_CUENTA_ATENUANTES.txt")
    cola = leer("SALIDA_V73_COLA_DELTA.txt")
    bor = leer("SALIDA_V73_BORDE_DEL_DUENO.txt")
    anc = leer("SALIDA_V73_ANCLA_TRAS_FUSION.txt")

    # LOS PARES D INTERNOS DE LOS QUE QUEDAN NO TIENEN LINEA DE RESUMEN EN LA
    # SALIDA DEL INSTRUMENTO, asi que se CUENTAN de su tabla y no se teclean:
    # una fila por acto, la columna D es la quinta.
    filas_pue = re.findall(r"^\s*(\d+)\s+\d+\s+\d+\s+\d+\s+(\d+)\s+\d+\s+\d+\s+\d+\s*$",
                           pue, re.M)
    con_d = len([f for f in filas_pue if int(f[1])])
    if not filas_pue:
        FALLOS.append("no se pudo leer la tabla de resumen de los puentes de los que quedan")

    c = {
        "antes_vivos": busca(fus, r"censo ANTES  : \d+ ficheros, (\d+) vivos", "vivos antes"),
        "despues_vivos": busca(fus, r"censo DESPUES: \d+ ficheros, (\d+) vivos", "vivos despues"),
        "mueren": busca(fus, r"nodos que MUEREN\s+: (\d+)", "nodos que mueren"),
        "piezas": busca(fus, r"piezas repartidas\s+: (\d+)", "piezas"),
        "enteras": busca(fus, r"piezas repartidas\s+: \d+ \((\d+) viajan enteras", "enteras"),
        "yadichas": busca(fus, r"viajan enteras, (\d+) ya estaban dichas", "ya dichas"),
        "tocados": busca(fus, r"ESCRITO\. ficheros tocados: (\d+)", "ficheros tocados"),
        "fundidos_plan": busca(fus, r"actos fundidos\s+: (\d+)", "actos fundidos del plan"),
        "declarados_plan": busca(fus, r"actos DECLARADOS y no fundidos: (\d+)", "declarados del plan"),
        "redirecciones": busca(fus, r"redirecciones sobre nodos VIVOS: (\d+)", "redirecciones"),
        "p16_fabrica": busca(fus, r"P\.16, DUPLICADAS QUE LA PROPIA FUSION FABRICA, medidas antes de limpiarlas: (\d+)",
                             "duplicadas que la fusion fabrica"),
        "auto_retiradas": busca(fus, r"AUTO-ARISTAS que la fusion habria creado y se retiran: (\d+)",
                                "auto-aristas retiradas"),
        "pasivo_antes": busca(fus, r"duplicadas tras resolver ANTES de la operacion \(pasivo historico, OP-S-12\): (\d+)",
                              "pasivo antes"),
        "pasivo_despues": busca(fus, r"duplicadas tras resolver DESPUES de la operacion\s+: (\d+)",
                                "pasivo despues"),
        "guarda_c": busca(fus, r"guarda C, los CINCO campos que esta operacion NO redacta, intactos: (\d+) de \d+",
                          "guarda C"),
        "col_base": busca(esp, r"linea base : (\d+)", "linea base"),
        "col_med": busca(col, r"COLISIONES DE CLASE VIGENTES\s+: (\d+)", "colisiones medidas"),
        "col_esp": busca(esp, r"ESPERADAS TRAS FUNDIR = (\d+)", "colisiones esperadas"),
        "col_nuevas": busca(esp, r"colisiones NUEVAS que la fusion fabricaria : (\d+)", "nuevas"),
        "col_idas": busca(esp, r"colisiones que DESAPARECERIAN\s+: (\d+)", "idas"),
        "autopares": busca(col, r"AUTO-PARES \(los dos lados al mismo vivo\): (\d+)", "auto-pares"),
        "autopares_esp": busca(esp, r"auto-pares NUEVOS \(pares internos del acto\): (\d+)",
                               "auto-pares nuevos predichos"),
        "dup_fab": busca(dif, r"GRUPOS FABRICADOS DE VERDAD: (\d+)", "duplicadas fabricadas"),
        "dup_ren": busca(dif, r"RENOMBRADOS \(aparecen con rotulo nuevo pero son el MISMO grupo\): (\d+)",
                         "renombrados"),
        "dup_antes": busca(dif, r"grupos ya RESUELTOS\s+: antes (\d+)", "grupos antes"),
        "dup_despues": busca(dif, r"grupos ya RESUELTOS\s+: antes \d+ \| despues (\d+)", "grupos despues"),
        "dup_idas": busca(dif, r"grupos que DESAPARECEN: (\d+)", "grupos que desaparecen"),
        "abiertos": busca(rec, r"ABIERTOS: (\d+) sobre", "abiertos"),
        "abiertos_n": busca(rec, r"ABIERTOS: \d+ sobre (\d+) nodos", "nodos abiertos"),
        "gate_activos": busca(gate, r"valor: (\d+) activos, \d+ deprecados", "activos del Gate 0"),
        "gate_deprecados": busca(gate, r"valor: \d+ activos, (\d+) deprecados", "deprecados del Gate 0"),
        "cola_antes": busca(cola, r"nodos en la cola ANTES  : (\d+)", "cola antes"),
        "cola_despues": busca(cola, r"nodos en la cola DESPUES: (\d+)", "cola despues"),
        "cola_entran": busca(cola, r"ENTRAN: (\d+)", "cola entran"),
        "cola_salen": busca(cola, r"SALEN : (\d+)", "cola salen"),
        "quedan_actos": busca(tra, r"QUEDAN SIN DESTINO: (\d+) actos y \d+ nodos", "actos que quedan"),
        "quedan_nodos": busca(tra, r"QUEDAN SIN DESTINO: \d+ actos y (\d+) nodos", "nodos que quedan"),
        "siguiente": busca(tra, r"el siguiente del prefijo: acto (\d+)", "siguiente"),
        "con_dueno": busca(tra, r"de los que quedan, CON DUENO medido: (\d+)", "con dueno"),
        "fundidos_medidos": busca(tra, r"actos FUNDIDOS, medido \(ningun miembro vivo, o uno solo\): (\d+)",
                                  "actos fundidos medidos"),
        "declarados_arg": busca(tra, r"DECLARADOS Y NO FUNDIDOS \(argumento\): (\d+)", "declarados"),
        "actos_mirados": busca(pue, r"actos mirados\s+: (\d+)", "actos mirados"),
        "actos_sin_puente": busca(pue, r"actos SIN ningun nodo puente\s+: (\d+)", "actos sin puente"),
        "quedan_puente": busca(pue, r"actos CON al menos un nodo puente\s+: (\d+)", "actos con puente"),
        "quedan_d": str(con_d),
        "per_total": busca(ate, r"perdidas selladas, en total\s+: (\d+)", "perdidas totales"),
        "per_paso": busca(ate, r"DE PARAMETRO DE PASO\s+: (\d+)", "perdidas de paso"),
        "per_cond": busca(ate, r"DE CONDICIONES\s+: (\d+)", "perdidas de condiciones"),
        "per_aten": busca(ate, r"filas con ATENUANTE DECLARADO\s+: (\d+)", "filas con atenuante"),
        "per_p4": busca(ate, r"de la ESPECIE DEL PENDIENTE 4\s+: (\d+)", "filas del pendiente 4"),
        "per_medido": busca(ate, r"con ATENUANTE DECLARADO Y MEDIDO\s+: (\d+)", "filas con atenuante medido"),
        "per_dos_sedes": busca(ate, r"filas con DOS SEDES en el campo donde : (\d+)", "filas de dos sedes"),
        "per_contraria": busca(ate, r"seria (\d+) y no \d+", "la aritmetica contraria"),
        "reanclaje": ("NADA QUE RE-ANCLAR" if "nada que re-anclar" in rea else "RE-ANCLAJES"),
        # EL BORDE DEL DUENO: ninguna de estas celdas se teclea. La tabla del
        # apartado g) del texto se arma entera con lo que la sonda imprimio.
        "tramo_filas": busca(tra, r"actos del tramo \(filas del fichero fijado\) : (\d+)", "filas del tramo"),
        "bor_inv_total": busca(bor, r"entradas del inventario, contadas hoy: (\d+)", "entradas del inventario"),
        "bor_miembros": busca(bor, r"miembros del lote I, contados: (\d+)", "miembros del lote"),
        "bor_tocan": busca(bor, r"entradas que TOCAN a alguno de los \d+ miembros: (\d+)", "entradas que tocan"),
        "bor_acto": busca(bor, r"de tipo acto\s+: (\d+)", "entradas de tipo acto"),
        "bor_enteras": busca(bor, r"familia_de_ids que cubren la NOMINA ENTERA de un acto del lote: (\d+)",
                             "familias de nomina entera"),
        "bor_rac_lineas": busca(bor, r"lineas de racimos barridas: (\d+)", "lineas de racimos"),
        "bor_rac_hits": busca(bor, r"miembros del lote que aparecen en alguna nomina de racimo: (\d+)",
                              "miembros en racimos"),
        "bor_ops_fichas": busca(bor, r"fichas leidas: (\d+)", "fichas de operaciones"),
        "bor_menciones": busca(bor, r"MENCIONES en total: (\d+)", "menciones en operaciones"),
        "rumbos": busca(anc, r"rumbos leidos del fichero : (\d+)", "rumbos del banco"),
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
        m = re.search(r"ACTO %d \. sobrevive.*?pasos (\d+) -> (\d+).*?condiciones (\d+) -> (\d+)"
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
    for n in DECLARADOS_DEL_LOTE:
        tablas["dec%d" % n] = tabla_declarado(declarados[n])

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
