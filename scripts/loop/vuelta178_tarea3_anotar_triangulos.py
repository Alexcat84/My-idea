# -*- coding: utf-8 -*-
r"""vuelta178_tarea3_anotar_triangulos.py . LOS TRIANGULOS `A` MAS `A` MAS `D` SE
ANOTAN CON SU REGLA. NO SE MUEVE NI UN VEREDICTO.

TAREA 3 de la vuelta 178. La `P.3` del reporte 177 queda adjudicada en el acta
177 punto 7.9 como COSA JUZGADA: no hace falta regla nueva, porque las dos que lo
deciden ya estan escritas Y RESULTAN SER COMPATIBLES.

  REGLA 1, banco 9.6.1: un nodo que es un paso de otro y NO TRAE PROCEDIMIENTO
  PROPIO, REPITE. Es la razon literal del puesto 878.

  REGLA 2, la correccion declarada del 13 ago 2026 (puestos 530 y 863): LA MADRE
  Y SU PIEZA DE ARENAS, y la vara las separa.

PARECEN CONTRARIAS Y NO LO SON. La condicion que las concilia la escribe la
propia 9.6.1: SI LA PIEZA TRAE PROCEDIMIENTO PROPIO SE SEPARA; SI ES EL PASO
DICHO OTRA VEZ, REPITE. Las arenas traen metodo propio; el anclaje no lo trae, y
el propio archivo lo mide.

LO QUE ESTE FICHERO HACE, Y LO QUE NO:

  . NO MUEVE NINGUN VEREDICTO. Cero. Lo comprueba el mismo, con el sha256 de
    `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` ANTES y DESPUES, y CAE EN ROJO si
    difieren.
  . NO ESCRIBE EN `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` ni en
    `docs/plan/OPERACIONES.jsonl` ni en `docs/plan/OP_L_03_LECTURAS.jsonl`. Su
    unica escritura es un registro PROPIO, `docs/plan/OP_L_03_TRIANGULOS.jsonl`.
  . NO TECLEA LOS TRIANGULOS: los ENCUENTRA. Enumera las ternas de nodos vivos de
    cada acto y se queda con las que tienen dos lados `A` y uno `D`. Si el numero
    que salga no es cinco, eso se publica tal cual: la cifra la da el
    instrumento corrido hoy (`EJECUTOR.md` 2).

DE DONDE SALE LA CLASE DE CADA LADO, Y SON DOS FUENTES QUE SE DECLARAN:
  (1) `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, indexado POR EL PAR RESUELTO
      (`P.1`, sin excepcion);
  (2) `docs/plan/OP_L_03_LECTURAS.jsonl`, el registro de lecturas de `OP-L-03`,
      para los lados leidos como LECTURA DIRIGIDA que por la clausula de
      `OP-L-03` NO entran en la cola. DESDE LA VUELTA 180 LA ETIQUETA DE ESA
      FUENTE DICE LA VUELTA QUE DE VERDAD ESCRIBIO LA FILA, leida de la propia
      fila, y no un literal clavado en 177: ese literal atribuia a la 177 cinco
      lecturas de la 179, medido por
      `scripts/loop/vuelta179_tarea3_etiqueta_de_fuente.py`.
  Cada lado publica de cual de las dos viene. Un lado sin clase en ninguna de las
  dos no forma triangulo y se dice.

COMO SE DECIDE QUE REGLA GOBIERNA CADA LADO, Y ES MECANICO: se lee LA RAZON
ESCRITA del propio veredicto y se buscan en ella las marcas literales de cada
regla. La 9.6.1 deja marcas como "no trae procedimiento propio" o "es el paso
cuatro contado como nodo"; la correccion del 13 ago deja "LA MADRE Y SU PIEZA" o
"la vara las separa". NO SE INTERPRETA NINGUNA RAZON A OJO: si un lado no trae
marcas de ninguna de las dos, se anota como SIN MARCA y se dice.

Y LA PRUEBA VA AL LADO, MEDIDA DEL GRAFO Y NO DE LA RAZON: los
`pasos_accionables` de cada extremo, contados. Es la corroboracion independiente
de "trae procedimiento propio", y la unica cifra de esta tarea que no sale de un
texto.

USO:
  python scripts/loop/vuelta178_tarea3_anotar_triangulos.py
  python scripts/loop/vuelta178_tarea3_anotar_triangulos.py --solo-mirar
"""
import argparse
import hashlib
import io
import json
import os
import sys
from itertools import combinations

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import vuelta166_tarea2_correccion_op_l_01 as T   # noqa: E402
import backlog_l03_resuelto as B   # noqa: E402

NL = chr(10)
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
LECTURAS = os.path.join(RAIZ, "docs", "plan", "OP_L_03_LECTURAS.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
SALIDA = os.path.join(RAIZ, "docs", "plan", "OP_L_03_TRIANGULOS.jsonl")

# LAS MARCAS LITERALES DE CADA REGLA. No son parafrasis: son trozos que las
# razones del propio archivo ya escriben, y por eso se pueden buscar.
MARCAS_9_6_1 = (
    "no trae procedimiento propio",
    "contado como nodo",
    "dicho como nodo",
    "misma contencion",
    "REPITE",
)
MARCAS_13_AGO = (
    "LA MADRE Y SU PIEZA",
    "la vara las separa",
    "Madre contra pieza",
    "CORRECCION DECLARADA el 13 ago 2026",
)

NOMBRE_9_6_1 = ("banco 9.6.1: un nodo que es un paso de otro y NO TRAE "
                "PROCEDIMIENTO PROPIO, REPITE")
NOMBRE_13_AGO = ("correccion declarada del 13 ago 2026 (puestos 530 y 863): LA "
                 "MADRE Y SU PIEZA, y la vara las separa porque la pieza TRAE "
                 "procedimiento propio")


def sha(ruta):
    return hashlib.sha256(
        io.open(ruta, "rb").read().replace(chr(13).encode(), b"")).hexdigest()


def marcas_en(razon):
    """(marcas de la 9.6.1, marcas del 13 ago) encontradas en esa razon. PURA."""
    r = razon or ""
    return ([m for m in MARCAS_9_6_1 if m in r],
            [m for m in MARCAS_13_AGO if m in r])


def regla_que_gobierna(razon):
    """LA REGLA QUE GOBIERNA ESE LADO, LEIDA DE SU RAZON. PURA.

    Devuelve (nombre_de_la_regla, marcas_9_6_1, marcas_13_ago). El 13 ago manda
    cuando aparece, y se dice por que: es una CORRECCION DECLARADA sobre un par
    que antes estaba clasificado por la otra vara, asi que si sus marcas estan,
    la que gobierna hoy es la correccion."""
    m1, m2 = marcas_en(razon)
    if m2:
        return NOMBRE_13_AGO, m1, m2
    if m1:
        return NOMBRE_9_6_1, m1, m2
    return "SIN MARCA DE NINGUNA DE LAS DOS", m1, m2


def etiqueta_del_registro(vuelta):
    """LA ETIQUETA DE FUENTE DE UNA CLASE QUE VIENE DEL REGISTRO DE LECTURAS,
    CON LA VUELTA QUE DE VERDAD LA ESCRIBIO. PURA: recibe la vuelta de la fila y
    devuelve el texto de la etiqueta.

    POR QUE EXISTE, Y EL MOTIVO ESTA MEDIDO (vuelta 180, TAREA 1.b; adjudicacion
    7.7 del acta 179). Hasta la vuelta 179 esta etiqueta era un LITERAL CLAVADO,
    `docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)`, escrito cuando la 177 era la
    unica vuelta que habia escrito en ese registro. La TAREA 2 de la 179 escribio
    ocho filas mas, de la vuelta 179, y sus clases salian etiquetadas como si
    fueran de la 177: `vuelta179_tarea3_etiqueta_de_fuente.py` lo midio y dio 15
    lados etiquetados como de la 177, de los cuales 10 verdaderos y **5 falsos**.

    UN LITERAL QUE ATRIBUYE A UNA VUELTA EL TRABAJO DE OTRA ROMPE `EJECUTOR.md`
    8, toda cifra de un autor con su atribucion. Por eso la etiqueta se computa
    de la fila y no se teclea.

    Si la fila no trae `vuelta`, la etiqueta lo DICE en vez de inventar un
    numero: `(vuelta desconocida)`. Fallar ruidoso, `banco 9`."""
    return "docs/plan/OP_L_03_LECTURAS.jsonl (vuelta %s)" % (
        vuelta if vuelta is not None else "desconocida")


def clases_por_par(mapa, lecturas=None, filas=None):
    """{frozenset(par resuelto): dict con clase, fuente, puestos y razon}.

    Las dos fuentes van declaradas en cada entrada. Si un par tiene clase en las
    dos, gana la del archivo y se dice que la otra existe.

    `lecturas` y `filas` van POR PARAMETRO desde la vuelta 180 para que su caso
    positivo por mutacion pueda pasarle un registro FABRICADO en un temporal y
    unos veredictos fabricados, sin tocar ni el archivo vivo ni este fichero.
    Por defecto son el registro y el archivo de siempre."""
    reg = LECTURAS if lecturas is None else lecturas
    idx = {}
    for fila in (T.veredictos() if filas is None else filas):
        a, b = T.resolver(mapa, fila["nodo_a"]), T.resolver(mapa, fila["nodo_b"])
        if a == b:
            continue
        k = frozenset((a, b))
        e = idx.setdefault(k, {"clase": fila.get("clase"),
                               "fuente": "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
                               "puestos": [], "razon": fila.get("razon") or ""})
        e["puestos"].append(fila.get("puesto_intra"))
        if not e["razon"]:
            e["razon"] = fila.get("razon") or ""
    if os.path.exists(reg):
        for linea in io.open(reg, encoding="utf-8"):
            if not linea.strip():
                continue
            d = json.loads(linea)
            # LA VUELTA SE LEE DE LA FILA Y NO SE TECLEA (vuelta 180, TAREA 1.b).
            # Cada lado dice la vuelta que de verdad escribio esa clase.
            vuelta_de_la_fila = d.get("vuelta")
            for clave, valor in (d.get("clases_de_los_pares_por_leer") or {}).items():
                x, y = clave.split("|", 1)
                a, b = T.resolver(mapa, x), T.resolver(mapa, y)
                if a == b:
                    continue
                k = frozenset((a, b))
                if k in idx:
                    idx[k]["tambien_en_el_registro_de_lecturas"] = True
                    idx[k]["vuelta_que_lo_escribio_en_el_registro"] = vuelta_de_la_fila
                    continue
                idx[k] = {"clase": valor[0],
                          "fuente": etiqueta_del_registro(vuelta_de_la_fila),
                          "vuelta_del_registro": vuelta_de_la_fila,
                          "puestos": [], "razon": valor[1] if len(valor) > 1 else ""}
    return idx


FUENTE_ARCHIVO = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"


def lados_de_fuera_del_archivo(fila):
    """LOS LADOS DE UN TRIANGULO CUYA CLASE NO SALE DEL ARCHIVO.

    Devuelve [(lado, clase, fuente)], VACIA si los tres descansan en el archivo.
    PURA: recibe la fila ya anotada y no lee nada."""
    return [(l["lado"], l["clase"], l.get("fuente_de_la_clase"))
            for l in fila["lados"]
            if l.get("fuente_de_la_clase") != FUENTE_ARCHIVO]


def recomputable_entero_del_archivo(fila):
    """SI EL TRIANGULO SE PUEDE RECOMPUTAR ENTERO DE
    `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`. PURA.

    POR QUE IMPORTA, Y NO ES UNA CURIOSIDAD (vuelta 179, TAREA 3; adjudicado en
    el acta 178 punto 7.8 por `banco 9.10` por extension natural). Un triangulo
    que se apoya en un lado de fuera del archivo NO se puede volver a computar
    contando el archivo: si manana alguien recuenta, ese lado no esta. Publicar
    el 16 a secas dice que hay dieciseis; no dice cuantos sobreviven al
    recuento."""
    return not lados_de_fuera_del_archivo(fila)


def el_lado_de_fuera_es_el_D(fila):
    """SI ALGUNO DE LOS LADOS QUE VIENEN DE FUERA DEL ARCHIVO ES EL LADO `D`.
    PURA.

    EL `D` NO ES UN LADO CUALQUIERA: es el que hace que el triangulo sea un
    triangulo. Dos lados `A` sin un `D` entre ellos no son esta figura. Que el
    lado de fuera sea el `D` no es lo mismo que sea uno de los `A`, y por eso se
    cuenta aparte y se nombra."""
    return any(c == "D" for _l, c, _f in lados_de_fuera_del_archivo(fila))


def reparto_por_fuente(filas):
    """LA CIFRA PARTIDA POR SU FUENTE. PURA: recibe las filas y devuelve un dict.

    Es lo que el encargo de la 179 pide en vez del 16 a secas: cuantos descansan
    enteros en el archivo, cuantos se apoyan en un lado de fuera, y de esos
    cuantos tienen el `D` fuera. Y los lados contados por fuente, que es la
    cifra de la que salen las otras."""
    enteros = [f for f in filas if recomputable_entero_del_archivo(f)]
    apoyados = [f for f in filas if not recomputable_entero_del_archivo(f)]
    con_d_fuera = [f for f in apoyados if el_lado_de_fuera_es_el_D(f)]
    lados = {}
    for f in filas:
        for l in f["lados"]:
            k = l.get("fuente_de_la_clase") or "(sin fuente)"
            lados[k] = lados.get(k, 0) + 1
    return {"total": len(filas), "enteros": enteros, "apoyados": apoyados,
            "con_d_fuera": con_d_fuera, "lados_por_fuente": lados}


def triangulos_del_acto(vivos, idx):
    """LAS TERNAS CON DOS LADOS `A` Y UNO `D`. PURA: recibe los nodos vivos y el
    indice de clases. Devuelve [(terna, [(par, entrada), x3])]."""
    salida = []
    for terna in combinations(sorted(vivos), 3):
        lados = []
        for a, b in combinations(terna, 2):
            e = idx.get(frozenset((a, b)))
            if e is None:
                lados = None
                break
            lados.append(((a, b), e))
        if not lados:
            continue
        clases = sorted(e["clase"] for _p, e in lados)
        if clases == ["A", "A", "D"]:
            salida.append((terna, lados))
    return salida


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-mirar", dest="solo_mirar", action="store_true",
                    help="mide e imprime y NO escribe el registro")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    p = print

    p("=" * 78)
    p("LOS TRIANGULOS A MAS A MAS D, ANOTADOS CON SU REGLA (vuelta 178, TAREA 3)")
    p("=" * 78)
    p("")

    sha_antes = sha(VEREDICTOS)
    sha_lec_antes = sha(LECTURAS) if os.path.exists(LECTURAS) else "(no existe)"
    p("A) EL SELLO DE LOS DOS REGISTROS, ANTES DE TOCAR NADA")
    p("   (vuelta 180, TAREA 1.b: el encargo pide los CUATRO sha256, los dos de")
    p("    antes y los dos de despues, DENTRO DEL PROPIO INSTRUMENTO. Hasta la 179")
    p("    solo se sellaba el archivo de veredictos; el registro de lecturas, que")
    p("    es la otra fuente de clases, no se sellaba y esta tarea lo toca)")
    p("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
    p("      sha256 ANTES (normalizado a LF): %s" % sha_antes)
    p("      bytes en disco: %d | bytes normalizados a LF: %d"
      % (os.path.getsize(VEREDICTOS),
         len(io.open(VEREDICTOS, "rb").read().replace(chr(13).encode(), b""))))
    p("   docs/plan/OP_L_03_LECTURAS.jsonl")
    p("      sha256 ANTES (normalizado a LF): %s" % sha_lec_antes)
    if os.path.exists(LECTURAS):
        p("      bytes en disco: %d | bytes normalizados a LF: %d"
          % (os.path.getsize(LECTURAS),
             len(io.open(LECTURAS, "rb").read().replace(chr(13).encode(), b""))))
    p("")

    mapa, _n = T.mapa_de_alias()
    vivos_grafo = B.vivos_por_grafo()
    idx = clases_por_par(mapa)
    p("B) EL MATERIAL, CONTADO Y NO SUPUESTO")
    p("   CIFRA alias del resolutor: %d" % len(mapa))
    p("   CIFRA pares con clase, de las DOS fuentes: %d" % len(idx))
    de_archivo = sum(1 for e in idx.values() if e["puestos"])
    p("      de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d" % de_archivo)
    p("      del registro de lecturas de OP-L-03: %d" % (len(idx) - de_archivo))
    por_vuelta = {}
    for e in idx.values():
        if not e["puestos"]:
            k = e.get("vuelta_del_registro")
            por_vuelta[k] = por_vuelta.get(k, 0) + 1
    for k in sorted(por_vuelta, key=lambda x: (x is None, x)):
        p("         escritas por la vuelta %s: %d" % (k, por_vuelta[k]))
    p("")

    actos, _salida, _c = B.actos_del_instrumento()
    # LOS ACTOS QUE LA 177 LEYO, CONTADOS DE SU REGISTRO Y NO TECLEADOS. Sirven
    # para separar LOS CINCO que el encargo nombra del resto que aparece al
    # buscar en el backlog entero, sin excluir a nadie de la busqueda.
    leidos_177 = set()
    if os.path.exists(LECTURAS):
        for linea in io.open(LECTURAS, encoding="utf-8"):
            if linea.strip():
                leidos_177.add(json.loads(linea).get("acto"))
    p("C) LOS ACTOS DONDE SE BUSCA, Y NO SE ELIGE NINGUNO A MANO")
    p("   se miran TODOS los actos del backlog que tienen 3 o mas nodos VIVOS")
    candidatos = []
    for _tam, _pares, miembros in actos:
        vivos = sorted({T.resolver(mapa, m) for m in miembros})
        vivos = [v for v in vivos if vivos_grafo.get(v, False)]
        if len(vivos) >= 3:
            candidatos.append((miembros[0], vivos))
    p("   CIFRA actos del backlog: %d" % len(actos))
    p("   CIFRA actos con 3 o mas nodos vivos: %d" % len(candidatos))
    for nombre, vivos in candidatos:
        p("      `%s`: %d vivos" % (nombre, len(vivos)))
    p("")

    p("D) LOS TRIANGULOS ENCONTRADOS, UNO A UNO Y CON SU REGLA POR LADO")
    filas = []
    for nombre, vivos in candidatos:
        for terna, lados in triangulos_del_acto(vivos, idx):
            p("")
            p("   TRIANGULO en el acto `%s`" % nombre)
            p("      terna: %s" % ", ".join(terna))
            anotados = []
            for (x, y), e in lados:
                regla, m1, m2 = regla_que_gobierna(e["razon"])
                anotados.append({
                    "lado": [x, y],
                    "clase": e["clase"],
                    "fuente_de_la_clase": e["fuente"],
                    "puestos": [q for q in e["puestos"] if q is not None],
                    "regla_que_gobierna": regla,
                    "marcas_de_la_9_6_1_en_su_razon": m1,
                    "marcas_de_la_correccion_13_ago_en_su_razon": m2,
                    "razon_leida_del_archivo": (e["razon"] or "")[:400],
                })
                p("      lado %s + %s -> clase %s | puestos %s | fuente %s"
                  % (x, y, e["clase"],
                     ", ".join(str(q) for q in e["puestos"] if q is not None) or "(sin puesto)",
                     e["fuente"]))
                p("         GOBIERNA: %s" % regla)
                p("         marcas 9.6.1 en su razon: %s" % (", ".join(m1) or "(ninguna)"))
                p("         marcas 13 ago en su razon: %s" % (", ".join(m2) or "(ninguna)"))
            filas.append({"id_op": "OP-L-03", "vuelta": 178, "fecha": "2026-09-05",
                          "acto": nombre,
                          "acto_leido_por_la_177": nombre in leidos_177,
                          "terna": list(terna),
                          "lados": anotados,
                          "veredictos_movidos": 0})
    p("")
    de_los_tres = [f for f in filas if f["acto_leido_por_la_177"]]
    del_resto = [f for f in filas if not f["acto_leido_por_la_177"]]
    p("   CIFRA triangulos A mas A mas D encontrados EN TODO EL BACKLOG: %d"
      % len(filas))
    p("")
    p("| tramo | actos | triangulos |")
    p("|---|---|---|")
    p("| en los actos QUE LA 177 LEYO | %d | **%d** |"
      % (len({f["acto"] for f in de_los_tres}), len(de_los_tres)))
    p("| en los actos QUE LA 177 NO MIRO | %d | **%d** |"
      % (len({f["acto"] for f in del_resto}), len(del_resto)))
    p("| **todo el backlog** | %d | **%d** |"
      % (len({f["acto"] for f in filas}), len(filas)))
    p("")
    p("   LOS DE LA PRIMERA FILA SON LOS CINCO QUE EL ENCARGO NOMBRA, y la cifra")
    p("   sale del instrumento y no se ajusta a la anterior. LOS DE LA SEGUNDA SON")
    p("   LA RESPUESTA A LA LETRA (d): el patron NO es una casualidad de tres")
    p("   actos, y esto lo dice midiendo y no opinando.")
    p("")

    # ------------------------------------------------------------ VUELTA 179
    # LA CIFRA PARTIDA POR SU FUENTE (TAREA 3 de la vuelta 179; adjudicado en el
    # acta 178 punto 7.8 por `banco 9.10` por extension natural). El total a
    # secas dice cuantos hay; no dice cuantos sobreviven a un recuento del
    # archivo. NINGUNA CLASE SE MUEVE aqui: esto solo cuenta lo ya anotado.
    for f in filas:
        f["recomputable_entero_del_archivo"] = recomputable_entero_del_archivo(f)
        f["el_lado_de_fuera_es_el_D"] = el_lado_de_fuera_es_el_D(f)
        f["vuelta_que_anota_la_fuente"] = 179
    rep = reparto_por_fuente(filas)
    p("D.1) LA CIFRA PARTIDA POR SU FUENTE, QUE ES LO QUE EL TOTAL NO DICE")
    p("   (vuelta 179, TAREA 3. NINGUNA CLASE SE MUEVE: esto solo cuenta)")
    p("")
    p("| que se cuenta | cuantos |")
    p("|---|---:|")
    for k in sorted(rep["lados_por_fuente"]):
        p("| lados con clase leida de `%s` | **%d** |" % (k, rep["lados_por_fuente"][k]))
    p("| triangulos con los TRES lados con veredicto en el archivo | **%d** |"
      % len(rep["enteros"]))
    p("| triangulos con al menos un lado SIN veredicto en el archivo | **%d** |"
      % len(rep["apoyados"]))
    p("| de esos, aquellos en que el lado de fuera es el `D` | **%d** |"
      % len(rep["con_d_fuera"]))
    p("| **total de triangulos** | **%d** |" % rep["total"])
    p("")
    p("   LOS QUE TIENEN EL `D` FUERA DEL ARCHIVO, NOMBRADOS UNO A UNO. El `D` es")
    p("   el lado que hace que el triangulo sea un triangulo: dos `A` sin un `D`")
    p("   entre ellos no son esta figura.")
    if not rep["con_d_fuera"]:
        p("      (ninguno)")
    for f in rep["con_d_fuera"]:
        for lado, clase, fuente in lados_de_fuera_del_archivo(f):
            if clase != "D":
                continue
            p("      acto `%s` | terna %s" % (f["acto"], ", ".join(f["terna"])))
            p("         lado `D` de fuera: %s + %s | fuente: %s"
              % (lado[0], lado[1], fuente))
    p("   CIFRA triangulos con el `D` fuera del archivo: %d" % len(rep["con_d_fuera"]))
    p("")
    p("   LOS QUE SE APOYAN EN UN LADO DE FUERA QUE **NO** ES EL `D`:")
    otros = [f for f in rep["apoyados"] if not el_lado_de_fuera_es_el_D(f)]
    if not otros:
        p("      (ninguno)")
    for f in otros:
        p("      acto `%s` | terna %s | lados de fuera: %s"
          % (f["acto"], ", ".join(f["terna"]),
             ", ".join("%s+%s (%s)" % (l[0], l[1], c)
                       for l, c, _fu in lados_de_fuera_del_archivo(f))))
    p("   CIFRA triangulos apoyados cuyo lado de fuera NO es el `D`: %d" % len(otros))
    p("")
    p("   LA RESTA, COMPROBADA: enteros %d mas apoyados %d = %d, y el total es %d."
      % (len(rep["enteros"]), len(rep["apoyados"]),
         len(rep["enteros"]) + len(rep["apoyados"]), rep["total"]))
    p("   CALZA: %s"
      % ("SI" if len(rep["enteros"]) + len(rep["apoyados"]) == rep["total"] else "NO"))
    p("   Y de los apoyados, con el `D` fuera %d mas sin el `D` fuera %d = %d."
      % (len(rep["con_d_fuera"]), len(otros), len(rep["con_d_fuera"]) + len(otros)))
    p("   CALZA: %s"
      % ("SI" if len(rep["con_d_fuera"]) + len(otros) == len(rep["apoyados"]) else "NO"))
    p("")

    p("E) LA PRUEBA MEDIDA DEL GRAFO, QUE NO SALE DE NINGUNA RAZON")
    nodos = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    implicados = sorted({n for f in filas for n in f["terna"]})
    p("   CIFRA nodos implicados en algun triangulo: %d" % len(implicados))
    p("")
    p("| nodo | pasos_accionables |")
    p("|---|---|")
    for n in implicados:
        p("| `%s` | %d |" % (n, len(nodos.get(n, {}).get("pasos_accionables") or [])))
    for f in filas:
        for lado in f["lados"]:
            x, y = lado["lado"]
            lado["pasos_accionables"] = {
                x: len(nodos.get(x, {}).get("pasos_accionables") or []),
                y: len(nodos.get(y, {}).get("pasos_accionables") or []),
            }
    p("")

    p("F) EL REPARTO DE REGLAS, CONTADO DE LO DE ARRIBA")
    cuenta = {}
    for f in filas:
        for lado in f["lados"]:
            k = lado["regla_que_gobierna"]
            cuenta[k] = cuenta.get(k, 0) + 1
    p("| regla que gobierna el lado | lados |")
    p("|---|---|")
    for k in sorted(cuenta):
        p("| %s | **%d** |" % (k[:78], cuenta[k]))
    p("| **total de lados** | **%d** |" % sum(cuenta.values()))
    p("")

    if not a.solo_mirar:
        with io.open(SALIDA, "w", encoding="utf-8", newline=NL) as fh:
            for f in filas:
                fh.write(json.dumps(f, ensure_ascii=False) + NL)
        crudo = io.open(SALIDA, "rb").read()
        p("G) EL REGISTRO PROPIO, ESCRITO")
        p("   %s" % os.path.relpath(SALIDA, RAIZ).replace(os.sep, "/"))
        p("      filas: %d" % len(filas))
        p("      bytes en disco: %d | bytes normalizados a LF: %d"
          % (os.path.getsize(SALIDA), len(crudo.replace(chr(13).encode(), b""))))
        p("      sha256 en disco: %s" % hashlib.sha256(crudo).hexdigest())
        p("      sha256 normalizado a LF: %s"
          % hashlib.sha256(crudo.replace(chr(13).encode(), b"")).hexdigest())
        p("")

    sha_despues = sha(VEREDICTOS)
    sha_lec_despues = sha(LECTURAS) if os.path.exists(LECTURAS) else "(no existe)"
    p("H) CERO CLASES MOVIDAS, COMPROBADO Y NO PROMETIDO. LOS CUATRO sha256")
    p("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
    p("      sha256 ANTES:   %s" % sha_antes)
    p("      sha256 DESPUES: %s" % sha_despues)
    p("      IDENTICOS: %s" % ("SI" if sha_antes == sha_despues else "NO"))
    p("   docs/plan/OP_L_03_LECTURAS.jsonl")
    p("      sha256 ANTES:   %s" % sha_lec_antes)
    p("      sha256 DESPUES: %s" % sha_lec_despues)
    p("      IDENTICOS: %s" % ("SI" if sha_lec_antes == sha_lec_despues else "NO"))
    p("")
    if sha_antes != sha_despues or sha_lec_antes != sha_lec_despues:
        p("ROJO: alguna de las DOS fuentes de clases cambio durante esta tarea, y")
        p("      esta tarea tiene prohibido moverlas. Cero es cero.")
        p("FIN")
        return 1
    if not filas:
        p("ROJO: no se encontro ningun triangulo. La 177 publico cinco, asi que un")
        p("      cero aqui no es un resultado, es un instrumento que no mira.")
        p("FIN")
        return 1
    p("VERDE: %d triangulos anotados con la regla que gobierna cada uno de sus %d "
      "lados, la clase de cada lado leida de su fuente y la prueba de "
      "`pasos_accionables` medida del grafo. CERO VEREDICTOS MOVIDOS, comprobado "
      "por sha256 antes y despues." % (len(filas), sum(len(f["lados"]) for f in filas)))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
