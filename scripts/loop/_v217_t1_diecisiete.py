# -*- coding: utf-8 -*-
r"""_v217_t1_diecisiete.py . LAS DIECISIETE CLAUSULAS DE LAS FASES 0 A 07 DE LA
TABLA POR FASE DE docs/plan/08_VERIFICACION.md, MEDIDAS UNA POR UNA CON SU
BUSQUEDA CORRIDA Y SU CIFRA DELANTE.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). Muere con la vuelta y no vigila nada.

QUIEN LO ENCARGA: el encargo de la vuelta 217, TAREA 1, que lo llama la ULTIMA
PUERTA DEL PLAN y lo declara BLOQUEANTE. Su motivo, con sus palabras: "declarar
la campana consumada habiendo medido trece de treinta clausulas seria la especie
exacta de verde que esta casa lleva doscientas vueltas cazando".

IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5). Los SEIS lectores de este
instrumento se IMPORTAN de scripts/loop/vuelta150_4_tabla_por_fase.py, que es la
sede donde ya viven: celdas_de_la_tabla, fichas, grafo, resolutor, gate0_checks,
salidas_del_bucle y guarda_salidas_congeladas. AQUI NO SE COPIA NI UNA LINEA DE
ESAS FUNCIONES. Lo unico propio es el PARTIDO DE LAS CELDAS EN CLAUSULAS y las
DIECISIETE SONDAS, que es lo que ese instrumento no tiene: el mide OCHO FILAS,
una por fase, y esto mide DIECISIETE CLAUSULAS, una por clausula.

Y SE DECLARA LA DISCREPANCIA EN VEZ DE RESOLVERLA COPIANDO (EJECUTOR.md 2). El
encargo dice que las ocho filas "NO LAS HA MEDIDO NADIE CON UNA SONDA CORRIDA".
Medido hoy: vuelta150_4_tabla_por_fase.py SI mide las ocho FILAS y se corrio en
las vueltas 150 a 155. Lo que nadie ha medido son las DIECISIETE CLAUSULAS por
separado, que es lo que hace este instrumento. Y ademas ese instrumento HOY CAE
EN ROJO, porque su assert exige OCHO filas y la correccion declarada de la
vuelta 214 dejo ONCE en la tabla. NO SE REPARA: la moratoria lo prohibe. Se mide,
se publica y se dice.

NO ESCRIBE EN NINGUNA FICHA, NO TOCA LA PAGINA 08, NO TOCA EL INVENTARIO Y NO
MUEVE NI UN CAMPO DE ESTADO. Lo comprueba con los dos sha256 del expediente y de
la pagina 08, al entrar y al salir.

USO:  python scripts/loop/_v217_t1_diecisiete.py --gate0 <RUTA> --corte <REF> --apertura <REF>
"""
import argparse
import copy
import hashlib
import io
import json
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)


def _cargar_v150():
    """CARGA LOS LECTORES DE vuelta150_4_tabla_por_fase.py SIN CORRER SU ENTRADA.

    NO ES UNA REPARACION Y NO TOCA EL FICHERO EN DISCO, que se queda byte a byte
    como esta: ese fichero NO lleva guarda de entrada y su ULTIMA LINEA es una
    llamada suelta a main(), asi que un import a secas lo CORRE ENTERO y hoy
    revienta en su propio assert de OCHO filas. Aqui se lee su fuente, se
    descarta esa ultima linea de entrada y se ejecuta el resto en un modulo
    propio, que es lo mismo que hace un import cuando el fichero si lleva
    guarda. Se declara porque una carga que se desvia de la convencion no se
    calla (moratoria de AUDITOR.md 6.3: NO SE REPARA NADA)."""
    import types
    ruta = os.path.join(AQUI, "vuelta150_4_tabla_por_fase.py")
    fuente = io.open(ruta, encoding="utf-8").read().replace(chr(13) + "\n", "\n")
    lineas_f = fuente.split("\n")
    quitadas = []
    while lineas_f and (not lineas_f[-1].strip()
                        or lineas_f[-1].strip() == "main()"):
        quitadas.append(lineas_f.pop())
    if "main()" not in quitadas:
        raise SystemExit("ROJO: la ultima linea de vuelta150_4_tabla_por_fase.py "
                         "ya no es la llamada suelta a main(), y este cargador "
                         "no se aplica a ciegas.")
    mod = types.ModuleType("v150_lectores")
    mod.__file__ = ruta
    exec(compile("\n".join(lineas_f), ruta, "exec"), mod.__dict__)
    return mod, len(fuente.split("\n")), len(lineas_f)


V150, _V150_LINEAS, _V150_EJECUTADAS = _cargar_v150()

NL = chr(10)
RAIZ = V150.RAIZ
VARA = V150.PAGINA
EXPEDIENTE = V150.OPS
INV = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
PAG02 = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")
E01 = os.path.join(RAIZ, "docs", "plan", "OP_E_01_DECIDIDAS.jsonl")
E06 = os.path.join(RAIZ, "docs", "plan", "OP_E_06_DIRECCION_V90.jsonl")
E07 = os.path.join(RAIZ, "docs", "plan", "OP_E_07_DIRECCION_V94.jsonl")

FILAS_0_A_07 = ["0 CODIGO", "01 FUENTES", "02 DESTEJIDOS", "03 FUSIONES",
                "04 ENLACES", "05 SANEO", "06 MESAS", "07 ADUANA"]

# LAS CIFRAS QUE EL ENCARGO ME DA PARA CONTRASTAR, NO PARA COPIAR. Si mi
# instrumento saca otra, PARO y lo traigo con las dos cifras delante.
CONTRASTE_FILAS_TOTAL = 11
CONTRASTE_CLAUSULAS_TOTAL = 30
CONTRASTE_FILAS_0_07 = 8
CONTRASTE_CLAUSULAS_0_07 = 17
CONTRASTE_REPARTO = {"0 CODIGO": 1, "01 FUENTES": 2, "02 DESTEJIDOS": 2,
                     "03 FUSIONES": 2, "04 ENLACES": 2, "05 SANEO": 6,
                     "06 MESAS": 1, "07 ADUANA": 1}

# LAS SEIS HERRAMIENTAS MUERTAS, LEIDAS DE LA PAGINA 05 Y NO TECLEADAS DE
# MEMORIA: viven en la tabla de OP-S-04 y aqui se declara cual es la marca.
SEIS_MUERTAS = ["Alexa", "Compete", "Perfect Audience", "The Deck", "oDesk",
                "Elance"]

# LOS CINCO CONTROLES MECANICOS QUE LA PAGINA 07 NOMBRA, CON LA MARCA CON LA QUE
# CADA UNO SE BUSCA EN LAS ETIQUETAS DE GATE 0. La marca es MIA y se dice que lo
# es; el control sale de la pagina. La quinta marca exige LAS DOS palabras a la
# vez, porque una marca de "dominio" a secas casaria con la comprobacion de
# dominio valido de cada nodo, que NO es una revision de nomina: seria una sonda
# mas laxa que su clausula.
CONTROLES_ADUANA = [
    ("auto-arista CON RESOLUCION (OP-C-04)", ("auto-arista via alias",)),
    ("lista blanca de claves del nodo (OP-C-04)", ("lista blanca del esquema",)),
    ("control posicional del campo fuente (OP-A-01)", ("comprobacion posicional",)),
    ("campo fuente CANONICO (OP-S-11)", ("lista CANONICA de libros",)),
    ("revision de toda nomina por el DOMINIO de sus miembros",
     ("nomina", "dominio")),
]

# LAS GUARDAS DE GATE 0 QUE CADA FICHA DE LA FASE 0 DECLARA COMO SU CASO
# POSITIVO. La marca es MIA; el texto sale del campo de obra de cada ficha.
MARCAS_GATE0_FASE0 = {
    "OP-C-04": ("auto-arista via alias", "lista blanca del esquema"),
    "OP-C-05": ("OP-C-05",),
    "OP-S-06": ("lista blanca del esquema",),
    "OP-S-07": ("auto-arista via alias",),
}

CERRADORAS_02 = ("REGISTRO DE OPERACION HECHA", "CERRADA", "SELLADA", "CIERRE")


def sha(ruta):
    b = io.open(ruta, "rb").read()
    return (hashlib.sha256(b).hexdigest()[:16],
            hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16])


def lineas(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(
        chr(13) + NL, NL).split(NL)


def jsonl(ruta):
    return [json.loads(l) for l in lineas(ruta) if l.strip()]


def texto_de(nd):
    """TODO EL TEXTO DE UN NODO EN UNA SOLA CADENA. PURA."""
    return " ".join([str(nd.get("titulo_concepto") or ""),
                     str(nd.get("resumen_teorico") or ""),
                     " ".join(nd.get("pasos_accionables") or []),
                     str(nd.get("entregable_esperado") or ""),
                     " ".join(nd.get("condiciones_activacion") or [])])


# ---------------------------------------------------------------------------
# (a) LAS FILAS Y SUS CLAUSULAS, SACADAS CON UN INSTRUMENTO Y NO A MANO
# ---------------------------------------------------------------------------

def partir_en_clausulas(celda):
    """LA CELDA PARTIDA EN CLAUSULAS POR SU PROPIO PUNTO Y COMA. PURA.

    El punto y coma es el separador que la propia pagina usa: la fila 05 SANEO
    escribe sus seis clausulas asi y la 09 sus ocho. No se inventa nada."""
    return [c.strip() for c in celda.split(";") if c.strip()]


# ---------------------------------------------------------------------------
# LOS DATOS. TODAS LAS SONDAS SON PURAS SOBRE ESTE DICT, PARA QUE EL MUTANTE SE
# PUEDA FABRICAR EN MEMORIA Y NO EN NINGUNA FICHA.
# ---------------------------------------------------------------------------

def corpus_de_pruebas():
    """LOS FICHEROS DE PRUEBA DEL REPO, CON SU TEXTO. Se recorre web, engine y
    scripts, y se toma todo .test.ts y todo test_*.py."""
    fuera = []
    for r in ("web", "engine", "scripts"):
        base_r = os.path.join(RAIZ, r)
        if not os.path.isdir(base_r):
            continue
        for base, dirs, ficheros in os.walk(base_r):
            dirs[:] = [d for d in dirs
                       if d not in ("node_modules", ".next", "__pycache__")]
            for f in ficheros:
                if not (f.endswith(".test.ts")
                        or (f.startswith("test_") and f.endswith(".py"))):
                    continue
                p = os.path.join(base, f)
                try:
                    t = io.open(p, encoding="utf-8", errors="replace").read()
                except Exception:
                    continue
                fuera.append((os.path.relpath(p, RAIZ).replace(os.sep, "/"), t))
    return fuera


def _git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def salidas_rojas_por_op(corte, ids):
    """LAS SALIDAS DEL ARBOL DEL CORTE QUE NOMBRAN UN id_op Y TRAEN MARCA DE
    ROJO, BUSCADAS CON git grep SOBRE ESE ARBOL Y NO CON UN LECTOR NUEVO.

    POR QUE NO SE USA salidas_del_bucle DE LA SEDE, Y SE DICE EN VEZ DE
    CALLARLO: esa funcion hace UN git show POR FICHERO, y el arbol del corte
    trae 7820 ficheros de salida; son 7820 subprocesos para una busqueda que
    git grep resuelve en dos. EL DETECTOR ES EL MISMO, letra por letra: la
    marca de rojo son FALLO entre corchetes, EXITCODE: 1, EXIT=1, la palabra
    CAE con punto, o ROJO."""
    glob = "docs/loop/SALIDA_*.txt"
    _c, todos = _git(["ls-tree", "-r", "--name-only", corte, "--", "docs/loop"])
    catalogo = [x for x in todos.splitlines()
                if x.startswith("docs/loop/SALIDA_") and x.endswith(".txt")]
    _c, rojo = _git(["grep", "-l", "-E",
                     r"\[FALLO\]|EXITCODE: 1|EXIT=1| CAE\.|ROJO", corte,
                     "--", glob])
    rojas = {x.split(":", 1)[1] for x in rojo.splitlines() if ":" in x}
    por_op = {}
    for i in ids:
        _c, s = _git(["grep", "-l", "-E",
                      re.escape(i) + r"([^A-Za-z0-9_-]|$)", corte, "--", glob])
        nombra = {x.split(":", 1)[1] for x in s.splitlines() if ":" in x}
        por_op[i] = sorted(nombra & rojas)
    return catalogo, rojas, por_op


def cargar(ruta_gate0, corte, apertura):
    N = V150.grafo("WORK")
    base = subprocess.run(["git", "merge-base", "pasada-unica", "main"],
                          capture_output=True, cwd=RAIZ).stdout.decode().strip()
    Nb = V150.grafo(base)
    F = V150.fichas()
    ops = {}
    for n, l in enumerate(lineas(EXPEDIENTE), start=1):
        if l.strip():
            d = json.loads(l)
            ops[d["id_op"]] = (n, d)
    ver = jsonl(VEREDICTOS)
    pruebas = corpus_de_pruebas()
    ls02 = lineas(PAG02)
    # LOS COMMITS QUE TOCARON CADA NODO DE LA CLASE DESDE EL GRAFO PREVIO, para
    # que la atribucion sea una medicion y no una suposicion.
    clase = ops["OP-F-01"][1].get("nodos") or []
    commits_clase = {}
    for nid in clase:
        r = subprocess.run(["git", "log", "--format=%h|%s", "%s..HEAD" % base,
                            "--", "dataset/nodos/%s.json" % nid],
                           capture_output=True, cwd=RAIZ)
        commits_clase[nid] = [x for x in
                              r.stdout.decode("utf-8", "replace").splitlines()
                              if x.strip()]
    fase0_ids = [x["id_op"] for x in F if x["fase"] == "00_CODIGO"]
    catalogo, rojas, por_op = salidas_rojas_por_op(corte, fase0_ids)
    e01 = [f for f in jsonl(E01) if f.get("decision") == "ESCRITA"]
    origen_existe = {}
    for f in e01:
        fo = f.get("fichero_origen")
        if fo:
            origen_existe[fo] = os.path.isfile(
                os.path.join(RAIZ, "docs", "loop", fo))
    return {
        "N": N,
        "Nb": Nb,
        "base": base,
        "F": F,
        "ops": ops,
        "inv": jsonl(INV),
        "ver": ver,
        "n_ver": len(ver),
        "gate0": V150.gate0_checks(ruta_gate0),
        "pruebas": pruebas,
        "ls02": ls02,
        "commits_clase": commits_clase,
        "e01": e01,
        "e06": jsonl(E06),
        "e07": jsonl(E07),
        "origen_existe": origen_existe,
        "catalogo_salidas": catalogo,
        "rojas": rojas,
        "rojas_por_op": por_op,
        "apertura": apertura,
    }


def _copia(D):
    """UNA COPIA SOBRE LA QUE EL MUTANTE PUEDE MORDER SIN TOCAR NADA REAL, Y
    SIN CLONAR LOS OCHO MEGAS DEL GRAFO PREVIO NI EL CATALOGO DE SALIDAS. Se
    copia en profundidad LO QUE LOS MUTANTES MUEVEN (el grafo de hoy, las
    fichas, el inventario y el expediente) y en superficie lo demas, que
    ninguno modifica en su sitio: lo reasigna entero."""
    E = dict(D)
    E["N"] = copy.deepcopy(D["N"])
    E["F"] = copy.deepcopy(D["F"])
    E["inv"] = copy.deepcopy(D["inv"])
    E["ops"] = copy.deepcopy(D["ops"])
    E["ver"] = list(D["ver"])
    E["e01"] = list(D["e01"])
    E["e06"] = list(D["e06"])
    E["e07"] = list(D["e07"])
    E["gate0"] = list(D["gate0"])
    E["pruebas"] = list(D["pruebas"])
    E["ls02"] = list(D["ls02"])
    E["rojas_por_op"] = dict(D["rojas_por_op"])
    return E


def _res(D):
    return V150.resolutor(D["N"])


def _nomina(D, *ids):
    fuera = []
    for i in ids:
        fuera.extend(D["ops"][i][1].get("nodos") or [])
    return fuera


# ---------------------------------------------------------------------------
# LAS DIECISIETE SONDAS. CADA UNA ES PURA SOBRE D Y DEVUELVE
# (veredicto, [lineas de cifra]).
# ---------------------------------------------------------------------------

def s_caso_positivo(D):
    c = []
    fase0 = [x for x in D["F"] if x["fase"] == "00_CODIGO"]
    c.append("EL SUJETO NO SE TECLEA: son las fichas cuyo campo de fase dice "
             "00_CODIGO, leidas del expediente en esta corrida.")
    c.append("CIFRA fichas de la fase 00_CODIGO: %d" % len(fase0))
    c.append("LA CLAUSULA TIENE DOS MITADES Y LAS DOS SE MIDEN: (1) que el caso "
             "positivo EXISTA Y CORRA HOY, y (2) que SE CAYERA ANTES del "
             "arreglo, que es un hecho historico y solo lo prueba una salida "
             "ROJA guardada en el arbol del corte.")
    c.append("MITAD 1, POR DOS PIERNAS DECLARADAS: (A) un bloque de prueba del "
             "corpus que nombre el id_op; (B) una etiqueta de Gate 0 que case "
             "con la marca que la propia ficha declara para su guarda.")
    con1 = 0
    for x in fase0:
        i = x["id_op"]
        ficheros = [(p, len(re.findall(r"\bit\(|\bdef test_", t)))
                     for p, t in D["pruebas"]
                     if re.search(re.escape(i) + r"(?![A-Za-z0-9_-])", t)]
        marcas = MARCAS_GATE0_FASE0.get(i, ())
        etiquetas = [(e, t) for e, t in D["gate0"]
                     if any(m in t for m in marcas)] if marcas else []
        if ficheros:
            con1 += 1
            c.append("  %-10s PIERNA A: %d fichero(s) de prueba lo nombran -> %s"
                     % (i, len(ficheros),
                        ", ".join("%s (%d bloques)" % (p, n)
                                  for p, n in ficheros[:2])))
        elif etiquetas:
            con1 += 1
            c.append("  %-10s PIERNA B: %d etiqueta(s) de Gate 0 corriendo hoy, "
                     "estado %s -> %s"
                     % (i, len(etiquetas),
                        ",".join(e for e, _ in etiquetas),
                        " | ".join(t[:62] for _, t in etiquetas)))
        else:
            c.append("  %-10s SIN CASO POSITIVO QUE CORRA HOY, ni por prueba ni "
                     "por etiqueta de Gate 0" % i)
    c.append("CIFRA de la MITAD 1, casos positivos que corren hoy: %d de %d"
             % (con1, len(fase0)))
    c.append("MITAD 2, LA HISTORICA: se busca con git grep SOBRE EL ARBOL DEL "
             "CORTE (nunca sobre el arbol de trabajo, que incluiria el papeleo "
             "de esta misma vuelta) una salida que nombre el id_op y traiga "
             "marca de rojo.")
    c.append("CIFRA ficheros de salida en el arbol del corte: %d"
             % len(D["catalogo_salidas"]))
    c.append("CIFRA de esos que traen alguna marca de rojo: %d" % len(D["rojas"]))
    con_rojo = {i: [os.path.basename(x) for x in v]
                for i, v in D["rojas_por_op"].items() if v}
    usadas = {x for v in D["rojas_por_op"].values() for x in v}
    propias, intrusas = V150.guarda_salidas_congeladas(usadas, D["apertura"])
    c.append("GUARDA DE SALIDAS (importada, no clonada): salidas anadidas por "
             "esta vuelta %d | usadas como prueba %d | INTRUSAS %d"
             % (len(propias), len(usadas), len(intrusas)))
    for x in intrusas:
        c.append("   INTRUSA> %s" % x)
    portadoras = {}
    for g in D["F"]:
        for d in (g.get("depende_de") or []):
            portadoras.setdefault(d, []).append(g["id_op"])
    con2 = 0
    for x in fase0:
        i = x["id_op"]
        propia = con_rojo.get(i, [])
        via = [g for g in portadoras.get(i, []) if con_rojo.get(g)]
        if propia:
            con2 += 1
            c.append("  %-10s ROJO GUARDADO, %d salida(s) -> %s"
                     % (i, len(propia), ", ".join(sorted(propia)[:2])))
        elif via:
            con2 += 1
            c.append("  %-10s ROJO POR PORTADORA declarada: %s"
                     % (i, ", ".join(via)))
        else:
            c.append("  %-10s SIN salida roja guardada, ni propia ni por "
                     "portadora (la busqueda da CERO y ese cero es el "
                     "resultado)" % i)
    c.append("CIFRA de la MITAD 2, casos positivos con rojo historico guardado: "
             "%d de %d" % (con2, len(fase0)))
    if intrusas:
        return "NO CUBRE", c
    if con1 == len(fase0) and con2 == len(fase0):
        return "CUBRE", c
    if con1 or con2:
        return "A MEDIAS", c
    return "NO CUBRE", c


def s_pasos_no_alterados(D):
    c = []
    clase = D["ops"]["OP-F-01"][1].get("nodos") or []
    c.append("EL SUJETO ES LA CLASE Y NO LA FASE ENTERA: la clausula dice "
             "'ningun nodo DE LA CLASE', y la clase es LARGO LEGITIMO, cuyo "
             "censo es el campo de nodos de OP-F-01 (linea %d del expediente), "
             "leido hoy y no tecleado." % D["ops"]["OP-F-01"][0])
    c.append("CIFRA miembros de la clase: %d | CIFRA que la ficha declara tras "
             "su correccion del 14 ago 2026: 6" % len(clase))
    c.append("LA VARA DEL 'ANTES' ES EL GRAFO PREVIO A LA CAMPANA, %s, y se "
             "compara por DOS varas distintas que no se mezclan: el NUMERO de "
             "pasos y el TEXTO de los pasos." % D["base"][:8])
    n_dist, t_dist = [], []
    for nid in clase:
        a = (D["Nb"].get(nid) or {}).get("pasos_accionables") or []
        b = (D["N"].get(nid) or {}).get("pasos_accionables") or []
        if len(a) != len(b):
            n_dist.append((nid, len(a), len(b)))
        if a != b:
            t_dist.append(nid)
        c.append("  %-46s pasos antes %2d | pasos hoy %2d | texto identico: %s"
                 % (nid[:46], len(a), len(b), "SI" if a == b else "NO"))
    c.append("CIFRA miembros con el NUMERO de pasos alterado: %d" % len(n_dist))
    c.append("CIFRA miembros con el TEXTO de algun paso distinto: %d"
             % len(t_dist))
    if not n_dist and not t_dist:
        c.append("   (las dos busquedas dan CERO, y ese cero es el resultado)")
    c.append("LA ATRIBUCION SE MIDE, NO SE SUPONE: de cada miembro con texto "
             "distinto se leen los commits que lo tocaron desde el grafo previo "
             "y se cuenta cuantos NOMBRAN una operacion de la fase 01.")
    tot_c, con_f01 = 0, 0
    for nid in t_dist:
        cs = D["commits_clase"].get(nid, [])
        tot_c += len(cs)
        for x in cs:
            if re.search(r"OP-F-\d", x):
                con_f01 += 1
        c.append("  %-46s commits que lo tocaron: %d" % (nid[:46], len(cs)))
        for x in cs[:3]:
            c.append("     commit> %s" % x[:110])
    c.append("CIFRA commits que tocaron a los de texto distinto: %d | CIFRA de "
             "esos que NOMBRAN una operacion de la fase 01: %d"
             % (tot_c, con_f01))
    if n_dist:
        return "NO CUBRE", c
    if t_dist:
        return "A MEDIAS", c
    return "CUBRE", c


def s_segundo_libro(D):
    c = []
    fichas01 = ["OP-F-02", "OP-F-03", "OP-F-04-COL", "OP-F-04-HOR",
                "OP-F-04-WEI", "OP-F-04-RAC"]
    menciones = []
    for i in fichas01:
        for nid in (D["ops"][i][1].get("nodos") or []):
            menciones.append((i, nid))
    c.append("EL SUJETO SON LAS FICHAS DE LA FASE 01 QUE CARGAN MATERIAL DE UN "
             "SEGUNDO LIBRO, y sus nominas se leen del expediente, no se "
             "teclean: %s." % ", ".join(fichas01))
    c.append("CIFRA menciones de nodo en esas nominas: %d | CIFRA ids "
             "distintos: %d" % (len(menciones), len({x[1] for x in menciones})))
    c.append("CIFRA que el recorte posicional de OP-A-01 publica al 11 ago "
             "2026, citada como contraste y no como fuente: 67 nodos con mas de "
             "un libro y 70 declaraciones en segunda posicion.")
    alias_de = {}
    for nid, nd in D["N"].items():
        for a in nd.get("ids_alias") or []:
            alias_de.setdefault(a, nid)
    borrados, multiples = [], []
    for i, nid in menciones:
        nd = D["N"].get(nid)
        if nd is None and nid not in alias_de:
            borrados.append((i, nid))
            continue
        if nd is None:
            continue
        fu = nd.get("fuente")
        decl = [x.strip() for x in str(fu).split(" | ") if x.strip()] \
            if isinstance(fu, str) else []
        if len(decl) > 1:
            multiples.append((i, nid, len(decl)))
    c.append("MITAD 'NO BORRADO': un nodo cuenta como NO borrado si sigue "
             "existiendo en el grafo, o si su id vive como alias de otro, que es "
             "material mudado y no material perdido.")
    c.append("CIFRA menciones BORRADAS sin rastro: %d" % len(borrados))
    for x in borrados[:5]:
        c.append("   BORRADA> %s" % str(x))
    if not borrados:
        c.append("   (la busqueda de las borradas da CERO, y ese cero es el "
                 "resultado: se corrio y se publica)")
    c.append("MITAD 'REUBICADO': una mencion esta reubicada cuando su nodo ya NO "
             "declara mas de una fuente. La que sigue declarando dos o mas "
             "todavia carga el material del segundo libro.")
    c.append("CIFRA menciones que TODAVIA declaran mas de una fuente: %d"
             % len(multiples))
    for x in multiples:
        c.append("   AUN CON DOS O MAS FUENTES> %s / %s, %d fuentes"
                 % (x[0], x[1], x[2]))
    if borrados:
        return "NO CUBRE", c
    if multiples:
        return "A MEDIAS", c
    return "CUBRE", c


def s_quince_congelados(D):
    c = []
    det = re.compile(r"^(NO SE JUZGA|NO PUEDO JUZGAR|CONGELAD)", re.I)
    cong = [v for v in D["ver"] if det.match(str(v.get("razon") or "").strip())]
    c.append("EL DETECTOR NO ES MIO: es el de "
             "scripts/loop/vuelta45_verificar_opd01_opd02.py, y su regla es que "
             "la razon ABRA con NO SE JUZGA, NO PUEDO JUZGAR o CONGELAD.")
    c.append("CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl contadas hoy: "
             "%d" % D["n_ver"])
    c.append("CIFRA congelados que quedan HOY en el archivo entero: %d | CIFRA "
             "que la clausula nombra: 15" % len(cong))
    fase02 = {n for x in D["F"] if x["fase"] == "02_DESTEJIDOS"
              for n in (x.get("nodos") or [])}
    c.append("CIFRA nodos en las nominas de la fase 02, leidos del expediente: "
             "%d" % len(fase02))
    de_la_fase = 0
    for v in cong:
        suyo = v.get("nodo_a") in fase02 or v.get("nodo_b") in fase02
        de_la_fase += 1 if suyo else 0
        c.append("   CONGELADO> puesto %s, clase %s, %s contra %s | de la "
                 "nomina de la fase 02: %s"
                 % (v.get("puesto_intra"), v.get("clase"), v.get("nodo_a"),
                    v.get("nodo_b"), "SI" if suyo else "NO"))
    if not cong:
        c.append("   (la busqueda da CERO congelados, y ese cero es el "
                 "resultado)")
    c.append("CIFRA congelados que SI son de la nomina de la fase 02: %d "
             "(se exigen 0)" % de_la_fase)
    c.append("LA CIFRA QUINCE ES LA DE SU CORTE Y NO LA DE HOY, y se dice en vez "
             "de callarlo: la clausula la escribio cuando quedaban quince.")
    return ("CUBRE" if de_la_fase == 0 else "NO CUBRE"), c


def s_perdida_en_su_bloque(D):
    c = []
    fase02 = [x for x in D["F"] if x["fase"] == "02_DESTEJIDOS"]
    c.append("EL SUJETO SON LAS FICHAS DE LA FASE 02, leidas del expediente por "
             "su campo de fase y no tecleadas.")
    c.append("CIFRA fichas de la fase 02: %d" % len(fase02))
    c.append("LA CLAUSULA TIENE DOS MITADES: (1) que la REGLA DE REPARTO este "
             "escrita en la ficha que declara la perdida, y (2) que la "
             "operacion tenga REGISTRO DE CIERRE en su pagina.")
    c.append("EL DETECTOR DE LA MITAD 1 SE PUBLICA CON SUS DOS ANCHURAS Y EL "
             "VEREDICTO SALE DE LA ESTRECHA: la ESTRECHA busca la frase de la "
             "regla, 'bloque del que proviene' o 'regla de reparto'; la ANCHA "
             "busca que la ficha NOMBRE UN BLOQUE al declarar su perdida. Una "
             "ficha puede cumplir la clausula con otras palabras, y por eso la "
             "ancha se cuenta; pero contar la ancha como veredicto seria una "
             "sonda mas laxa que su clausula.")
    con_perdida, con_regla, con_registro, con_ancha = 0, 0, 0, 0
    for x in fase02:
        entero = json.dumps(x, ensure_ascii=False)
        perdida = bool(x.get("preservar"))
        regla = bool(re.search(r"bloque del que proviene|regla de reparto",
                               entero, re.I))
        ancha = bool(re.search(r"bloque", " ".join(x.get("preservar") or []),
                               re.I))
        anclas = [n + 1 for n, l in enumerate(D["ls02"])
                  if x["id_op"] in l
                  and any(k in l for k in CERRADORAS_02)]
        con_perdida += 1 if perdida else 0
        con_regla += 1 if regla else 0
        con_ancha += 1 if ancha else 0
        con_registro += 1 if anclas else 0
        c.append("  %-10s perdidas declaradas %d | regla ESTRECHA: %-2s | regla "
                 "ANCHA (nombra un bloque): %-2s | lineas de registro de cierre "
                 "en la pagina 02: %d %s"
                 % (x["id_op"], len(x.get("preservar") or []),
                    "SI" if regla else "NO", "SI" if ancha else "NO",
                    len(anclas),
                    ("(primera: %d)" % anclas[0]) if anclas else "(ninguna)"))
    c.append("CIFRA fichas con perdida declarada: %d de %d"
             % (con_perdida, len(fase02)))
    c.append("CIFRA fichas con la regla ESTRECHA escrita: %d de %d"
             % (con_regla, len(fase02)))
    c.append("CIFRA fichas que NOMBRAN UN BLOQUE al declarar su perdida (regla "
             "ANCHA): %d de %d" % (con_ancha, len(fase02)))
    c.append("CIFRA fichas con registro de cierre en docs/plan/02_DESTEJIDOS.md: "
             "%d de %d" % (con_registro, len(fase02)))
    c.append("CIFRA que la propia pagina 02 publica tras su correccion del 19 "
             "ago 2026, citada como contraste: 9 de 9.")
    if con_registro == len(fase02) and con_regla == len(fase02):
        return "CUBRE", c
    if con_registro or con_regla:
        return "A MEDIAS", c
    return "NO CUBRE", c


def _actos_vigentes(D):
    """LOS ACTOS DEL CORTE VIGENTE. El corte no se teclea: se toma el MAYOR de
    los que el inventario trae para el tipo acto. PURA."""
    actos = [e for e in D["inv"] if e.get("tipo") == "acto"]
    if not actos:
        return [], None
    corte = max(str(e.get("fecha_corte") or "") for e in actos)
    return [e for e in actos if str(e.get("fecha_corte") or "") == corte], corte


def s_un_superviviente(D):
    c = []
    actos, corte = _actos_vigentes(D)
    c.append("EL SUJETO SON LOS ACTOS DEL CORTE VIGENTE del inventario, y el "
             "corte no se teclea: se toma el MAYOR de los que el propio fichero "
             "trae.")
    c.append("CIFRA corte vigente leido: %s" % corte)
    c.append("CIFRA actos de ese corte: %d | CIFRA actos de todos los cortes: %d"
             % (len(actos), len([e for e in D["inv"] if e.get("tipo") == "acto"])))
    res = _res(D)
    uno, varios, cero = 0, 0, 0
    con_alias, sin_alias, ej = 0, 0, []
    for a in actos:
        ms = a.get("miembros") or []
        vivos = [m for m in ms
                 if m in D["N"] and not D["N"][m].get("deprecado")]
        if len(vivos) == 1:
            uno += 1
            s = vivos[0]
            al = set(D["N"][s].get("ids_alias") or [])
            for m in ms:
                if m == s:
                    continue
                if m in al:
                    con_alias += 1
                else:
                    sin_alias += 1
                    if len(ej) < 5:
                        ej.append((a.get("nombre"), s, m))
        elif not vivos:
            cero += 1
        else:
            varios += 1
    c.append("CIFRA actos con UN SOLO superviviente vivo: %d" % uno)
    c.append("CIFRA actos con VARIOS miembros vivos, o sea sin fundir todavia: "
             "%d" % varios)
    c.append("CIFRA actos con CERO miembros vivos: %d" % cero)
    c.append("CIFRA miembros absorbidos de los actos ya fundidos: %d, de ellos "
             "CON alias en el superviviente %d y SIN alias %d"
             % (con_alias + sin_alias, con_alias, sin_alias))
    for x in ej:
        c.append("   SIN ALIAS> acto %s, superviviente %s, absorbido %s" % x)
    if not sin_alias:
        c.append("   (la busqueda de absorbidos sin alias da CERO, y ese cero "
                 "es el resultado)")
    if sin_alias:
        return "NO CUBRE", c
    if varios or cero:
        return "A MEDIAS", c
    return "CUBRE", c


def s_resolver_da_superviviente(D):
    c = []
    actos, corte = _actos_vigentes(D)
    res = _res(D)
    c.append("EL RESOLUTOR NO ES MIO: se IMPORTA de "
             "scripts/loop/vuelta150_4_tabla_por_fase.py, que a su vez replica "
             "la cadena de _resolver de Gate 0, copia fiel de resolverId.")
    c.append("EL SUJETO SON LOS ABSORBIDOS DE LOS ACTOS QUE YA TIENEN UN SOLO "
             "SUPERVIVIENTE: donde no hay superviviente todavia no hay nada que "
             "resolver, y eso se dice en vez de contarlo como fallo.")
    c.append("CIFRA corte vigente leido: %s | CIFRA actos de ese corte: %d"
             % (corte, len(actos)))
    prob, bien, mal, ej = 0, 0, 0, []
    fuera = 0
    for a in actos:
        ms = a.get("miembros") or []
        vivos = [m for m in ms
                 if m in D["N"] and not D["N"][m].get("deprecado")]
        if len(vivos) != 1:
            fuera += 1
            continue
        s = vivos[0]
        for m in ms:
            if m == s:
                continue
            prob += 1
            if res(m) == s:
                bien += 1
            else:
                mal += 1
                if len(ej) < 5:
                    ej.append((a.get("nombre"), m, res(m), s))
    c.append("CIFRA actos FUERA de esta vara por no tener superviviente unico: "
             "%d" % fuera)
    c.append("CIFRA absorbidos probados por el resolutor: %d" % prob)
    c.append("CIFRA que resuelven AL superviviente: %d | CIFRA que NO: %d"
             % (bien, mal))
    for x in ej:
        c.append("   NO RESUELVE> acto %s, absorbido %s da %s y no %s" % x)
    if not mal:
        c.append("   (la busqueda de los que no resuelven da CERO, y ese cero "
                 "es el resultado)")
    if not prob:
        return "NO CUBRE", c
    return ("CUBRE" if mal == 0 else "NO CUBRE"), c


def _aristas_nuevas(D):
    fuera = []
    for f in D["e01"]:
        fuera.append(("OP-E-01", f["madre"], f["hijo"],
                      f.get("fichero_origen"), None))
    for f in D["e06"]:
        fuera.append(("OP-E-06", f["madre"], f["hijo"], None, f.get("puesto")))
    for f in D["e07"]:
        fuera.append(("OP-E-07", f["madre"], f["hijo"], None, f.get("puesto")))
    return fuera


def s_arista_confirmada_por_lectura(D):
    c = []
    aristas = _aristas_nuevas(D)
    c.append("EL SUJETO SON LAS TRES FUENTES DE ARISTA NUEVA QUE LA PROPIA "
             "PAGINA 04 NOMBRA EN SU CIERRE: las ESCRITA de OP-E-01, la "
             "direccion V90 de OP-E-06 y la direccion V94 de OP-E-07.")
    c.append("CIFRA aristas nuevas armadas leyendo las tres fuentes: %d | CIFRA "
             "que el cierre de la pagina 04 publica: 296" % len(aristas))
    c.append("CIFRA por fuente: OP-E-01 %d, OP-E-06 %d, OP-E-07 %d"
             % (len(D["e01"]), len(D["e06"]), len(D["e07"])))
    c.append("QUE CUENTA COMO CONFIRMADA POR LECTURA, y se declara antes de "
             "medir: la fila cita el FICHERO DE LECTURA del que salio, y ese "
             "fichero existe en disco; o la fila cita el PUESTO de un veredicto "
             "del archivo, y ese puesto existe.")
    puestos = {v.get("puesto_intra") for v in D["ver"]}
    con, sin, ej = 0, 0, []
    for fuente, m, h, fo, puesto in aristas:
        ok = False
        if fo is not None:
            ok = bool(D["origen_existe"].get(fo))
        elif puesto is not None:
            ok = puesto in puestos
        if ok:
            con += 1
        else:
            sin += 1
            if len(ej) < 5:
                ej.append((fuente, m, h, fo, puesto))
    c.append("CIFRA ficheros de lectura distintos citados por OP-E-01: %d, de "
             "ellos EXISTEN en disco %d"
             % (len(D["origen_existe"]),
                sum(1 for v in D["origen_existe"].values() if v)))
    c.append("CIFRA puestos distintos del archivo: %d" % len(puestos))
    c.append("CIFRA aristas nuevas CONFIRMADAS por lectura: %d | CIFRA SIN "
             "confirmar: %d" % (con, sin))
    for x in ej:
        c.append("   SIN CONFIRMAR> %s" % str(x))
    if not sin:
        c.append("   (la busqueda de las no confirmadas da CERO, y ese cero es "
                 "el resultado)")
    if not aristas:
        return "NO CUBRE", c
    return ("CUBRE" if sin == 0 else ("A MEDIAS" if con else "NO CUBRE")), c


def s_sin_autoarista(D):
    c = []
    aristas = _aristas_nuevas(D)
    res = _res(D)
    c.append("LA CLAUSULA DICE 'TRAS RESOLVER', asi que la comparacion literal "
             "no vale: los dos extremos se pasan por el resolutor y se comparan "
             "despues, que es la leccion escrita de OP-S-07.")
    c.append("CIFRA aristas nuevas medidas: %d" % len(aristas))
    auto, ej = 0, []
    for fuente, m, h, _fo, _p in aristas:
        rm, rh = res(m), res(h)
        if rm is not None and rm == rh:
            auto += 1
            if len(ej) < 5:
                ej.append((fuente, m, h, rm))
    c.append("CIFRA aristas nuevas que crean AUTO-ARISTA tras resolver: %d"
             % auto)
    for x in ej:
        c.append("   AUTO-ARISTA> %s: %s a %s, los dos resuelven a %s" % x)
    if not auto:
        c.append("   (la busqueda da CERO, y ese cero es el resultado: se "
                 "corrio y se publica con su comando delante)")
    et = [(e, t) for e, t in D["gate0"] if "auto-arista via alias" in t]
    c.append("Y LA GUARDA HERMANA DE GATE 0, CITADA COMO CONTRASTE Y NO COMO "
             "FUENTE: %s" % (" | ".join("[%s] %s" % (e, t[:80]) for e, t in et)
                             or "ninguna etiqueta"))
    if not aristas:
        return "NO CUBRE", c
    return ("CUBRE" if auto == 0 else "NO CUBRE"), c


def s_tratado_extinto(D):
    c = []
    c.append("LECTURA CORREGIDA, Y LA CORRECCION NO ES MIA: la celda de la fila "
             "05 se lee ACOTADA A LAS NOMINAS DE SUS OPERACIONES (correccion "
             "declarada de la vuelta 122, lineas 35 a 58 de "
             "docs/plan/08_VERIFICACION.md), citando el punto 2 de la decision "
             "del fundador del 28 ago 2026, que saco el barrido global de NAFTA "
             "de la campana y dejo VIVA esta fila gemela.")
    nom = _nomina(D, "OP-S-01")
    c.append("CIFRA nodos de la nomina de OP-S-01, leidos del expediente: %d"
             % len(nom))
    res = _res(D)
    vivos_con = []
    for nid in nom:
        nd = D["N"].get(nid)
        if nd is None:
            c.append("  %-46s NO EXISTE en el grafo (ausencia, no cero)" % nid[:46])
            continue
        vivo = not nd.get("deprecado")
        tiene = ("nafta" in nid.lower()
                 or "nafta" in str(nd.get("titulo_concepto") or "").lower())
        if vivo and tiene:
            vivos_con.append(nid)
        c.append("  %-46s vivo: %-2s | nombra el tratado extinto en id o "
                 "titulo: %-2s | resuelve a %s"
                 % (nid[:46], "SI" if vivo else "NO", "SI" if tiene else "NO",
                    res(nid)))
    c.append("CIFRA ids VIVOS de la nomina que nombran el tratado extinto: %d"
             % len(vivos_con))
    glob = [k for k, v in D["N"].items()
            if not v.get("deprecado")
            and ("nafta" in k.lower()
                 or "nafta" in str(v.get("titulo_concepto") or "").lower())]
    c.append("Y LA LECTURA GLOBAL, PUBLICADA AUNQUE NO SEA EL SUJETO: CIFRA "
             "nodos VIVOS de TODO el catalogo que lo nombran en id o titulo: %d"
             % len(glob))
    if not glob:
        c.append("   (las dos busquedas dan CERO, y ese cero es el resultado)")
    return ("CUBRE" if not vivos_con else "NO CUBRE"), c


def s_incoterms(D):
    c = []
    nom = _nomina(D, "OP-S-02")
    res = _res(D)
    c.append("EL SUJETO SON LOS TRES DE LA NOMINA DE OP-S-02, leidos del "
             "expediente (linea %d) y no tecleados." % D["ops"]["OP-S-02"][0])
    c.append("CIFRA nodos de la nomina: %d | CIFRA que la clausula escribe: 3"
             % len(nom))
    c.append("LECTURA CORREGIDA, Y LA CORRECCION ES DE LA VUELTA 120 Y VIVE EN "
             "LA PROPIA FICHA: DOS de los tres estan deprecados, y la version "
             "se mide EN SU SUPERVIVIENTE, no en el id muerto.")
    lit, cor = 0, 0
    for nid in nom:
        nd = D["N"].get(nid)
        if nd is None:
            c.append("  %-46s NO EXISTE (ausencia, no cero)" % nid[:46])
            continue
        t = texto_de(nd)
        con_ver = bool(re.search(r"Incoterms\s*(19|20)\d\d", t, re.I))
        lit += 1 if (not nd.get("deprecado") and con_ver) else 0
        s = res(nid)
        ts = texto_de(D["N"][s]) if s in D["N"] else ""
        cita_s = "incoterms" in ts.lower()
        ver_s = bool(re.search(r"Incoterms\s*(19|20)\d\d", ts, re.I))
        cor += 1 if ver_s else 0
        c.append("  %-40s vivo: %-2s | version en el propio nodo: %-2s | "
                 "superviviente %s | ese cita Incoterms: %-2s | con version: %s"
                 % (nid[:40], "NO" if nd.get("deprecado") else "SI",
                    "SI" if con_ver else "NO", s,
                    "SI" if cita_s else "NO", "SI" if ver_s else "NO"))
    c.append("CIFRA por la LECTURA LITERAL (el propio nodo, vivo y con version): "
             "%d de %d" % (lit, len(nom)))
    c.append("CIFRA por la LECTURA CORREGIDA (su superviviente trae la version): "
             "%d de %d" % (cor, len(nom)))
    c.append("EL QUE NO CUBRE POR NINGUNA DE LAS DOS ES EL TERCERO, y su motivo "
             "esta escrito y adjudicado: la cita de Incoterms no viajo completa "
             "a una fusion anterior, y el residuo quedo anotado en "
             "docs/PENDIENTES.md por el acta 120, sin ejecutarse.")
    if cor == len(nom):
        return "CUBRE", c
    if cor:
        return "A MEDIAS", c
    return "NO CUBRE", c


def s_export_gov(D):
    c = []
    c.append("CLAUSULA CON CORRECCION DECLARADA, Y SE MIDE POR SU LECTURA "
             "CORREGIDA: la correccion de la vuelta 122 dice literalmente que "
             "esta clausula esta CUMPLIDA, por OP-S-03. Se remide igual, hoy y "
             "con la busqueda corrida, porque una correccion citada no es una "
             "medicion.")
    nom = _nomina(D, "OP-S-03")
    c.append("CIFRA nodos de la nomina de OP-S-03: %d" % len(nom))
    en_nom = [nid for nid in nom
              if nid in D["N"] and "export.gov" in texto_de(D["N"][nid]).lower()]
    glob = [k for k, v in D["N"].items()
            if "export.gov" in texto_de(v).lower()]
    c.append("CIFRA nodos de la NOMINA que cablean export.gov: %d" % len(en_nom))
    c.append("CIFRA nodos de TODO el catalogo, vivos y deprecados, que lo "
             "cablean: %d" % len(glob))
    for x in glob[:5]:
        c.append("   CABLEA> %s" % x)
    if not glob:
        c.append("   (las dos busquedas dan CERO, y ese cero es el resultado: "
                 "se corrieron y se publican)")
    return ("CUBRE" if not en_nom and not glob else
            ("A MEDIAS" if not en_nom else "NO CUBRE")), c


def s_seis_herramientas(D):
    c = []
    c.append("CLAUSULA CON CORRECCION DECLARADA, Y ES LA QUE LA CORRECCION DE "
             "LA VUELTA 122 ACOTA: medida A LA LETRA da NO CUBRE por un residuo "
             "que el fundador ya saco de la campana. Se mide ACOTADA A LA "
             "NOMINA de OP-S-04, y el residuo global se publica al lado en vez "
             "de callarse.")
    nom = _nomina(D, "OP-S-04")
    c.append("CIFRA nodos de la nomina de OP-S-04, leidos del expediente (linea "
             "%d): %d" % (D["ops"]["OP-S-04"][0], len(nom)))
    c.append("CIFRA herramientas muertas que la clausula nombra: %d"
             % len(SEIS_MUERTAS))
    en_nom_tot, glob_tot = 0, 0
    for h in SEIS_MUERTAS:
        pat = re.compile(r"\b" + re.escape(h) + r"\b")
        en_nom = [nid for nid in nom
                  if nid in D["N"] and pat.search(texto_de(D["N"][nid]))]
        glob = [k for k, v in D["N"].items()
                if not v.get("deprecado") and pat.search(texto_de(v))]
        en_nom_tot += len(en_nom)
        glob_tot += len(glob)
        c.append("  %-18s en la NOMINA: %d | en nodos VIVOS de todo el "
                 "catalogo: %d %s"
                 % (h, len(en_nom), len(glob), glob[:2] if glob else ""))
    c.append("CIFRA menciones vivas DENTRO de la nomina: %d (se exigen 0 por la "
             "lectura corregida)" % en_nom_tot)
    c.append("CIFRA menciones vivas FUERA de la nomina, o sea el residuo global: "
             "%d. La correccion lo nombra por su nodo y lo manda a "
             "docs/PENDIENTES.md como trabajo post campana." % glob_tot)
    if not en_nom_tot and not glob_tot:
        c.append("   (las dos busquedas dan CERO, y ese cero es el resultado)")
    return ("CUBRE" if en_nom_tot == 0 else "NO CUBRE"), c


def s_dos_claves_de_fase(D):
    c = []
    claves = set()
    for v in D["N"].values():
        claves |= set(v.keys())
    fase_k = sorted(k for k in claves
                    if "fase" in k.lower() or "phase" in k.lower()
                    or "proekto" in k.lower() or "project" in k.lower())
    c.append("LAS CLAVES NO SE TECLEAN: se computa la union de todas las claves "
             "del grafo y se filtran las que tienen pinta de fase.")
    c.append("CIFRA claves distintas en todo el grafo: %d" % len(claves))
    c.append("CIFRA claves con pinta de fase: %d -> %s"
             % (len(fase_k), fase_k))
    dos = [k for k, v in D["N"].items()
           if sum(1 for kk in v if kk in fase_k) > 1]
    c.append("CIFRA nodos con MAS DE UNA clave de fase: %d" % len(dos))
    for x in dos[:5]:
        c.append("   CON DOS> %s -> %s"
                 % (x, [kk for kk in D["N"][x] if kk in fase_k]))
    if not dos:
        c.append("   (la busqueda da CERO, y ese cero es el resultado: los dos "
                 "campos sucios que OP-S-06 nombra, fase_proekto cirilica y "
                 "fase_project, no viven hoy en el grafo compilado)")
    et = [(e, t) for e, t in D["gate0"] if "lista blanca del esquema" in t]
    c.append("Y LA GUARDA HERMANA DE GATE 0, CITADA COMO CONTRASTE: %s"
             % (" | ".join("[%s] %s" % (e, t[:80]) for e, t in et)
                or "ninguna etiqueta"))
    return ("CUBRE" if not dos else "NO CUBRE"), c


def s_autocita_tras_resolver(D):
    c = []
    res = _res(D)
    c.append("LA CLAUSULA DICE 'TRAS RESOLVER' Y POR ESO NO VALE COMPARAR "
             "LITERAL: un chequeo literal da CERO sobre un grafo con "
             "veintisiete, porque ninguna de las 33 era directa. Es la leccion "
             "escrita de OP-S-07 y de OP-C-04.")
    vivos = [k for k, v in D["N"].items() if not v.get("deprecado")]
    c.append("CIFRA nodos del grafo: %d | CIFRA VIVOS: %d"
             % (len(D["N"]), len(vivos)))
    auto = []
    for k in vivos:
        v = D["N"][k]
        for campo in ("nodos_previos", "nodos_siguientes"):
            for x in v.get(campo) or []:
                if res(x) == k:
                    auto.append((k, campo, x))
    c.append("CIFRA auto-aristas TRAS RESOLVER sobre nodos vivos: %d" % len(auto))
    for x in auto[:5]:
        c.append("   AUTO-CITA> %s en %s cita %s" % x)
    if not auto:
        c.append("   (la busqueda da CERO, y ese cero es el resultado)")
    et = [(e, t) for e, t in D["gate0"] if "auto-arista via alias" in t]
    c.append("Y LA GUARDA DE GATE 0, CITADA COMO CONTRASTE Y NO COMO FUENTE: %s"
             % (" | ".join("[%s] %s" % (e, t[:90]) for e, t in et)
                or "ninguna etiqueta"))
    return ("CUBRE" if not auto else "NO CUBRE"), c


def s_decision_con_motivo_y_cobertura(D):
    c = []
    mesas = [x for x in D["F"] if x["fase"] == "06_MESAS"]
    c.append("EL SUJETO SON LAS FICHAS DE LA FASE 06, leidas por su campo de "
             "fase y no tecleadas.")
    c.append("CIFRA fichas de la fase 06: %d" % len(mesas))
    c.append("QUE CUENTA COMO QUE, Y SE DECLARA ANTES DE MEDIR: la DECISION es "
             "el campo de adjudicacion de la ficha; el MOTIVO es su campo de "
             "nota; y LA COBERTURA AL LADO no se busca en la ficha sino donde "
             "el banco 9.26 la pone, en las nominas del inventario que nombran "
             "esa mesa. Contar un 'N de M' cualquiera dentro de la ficha seria "
             "una sonda mas laxa que su clausula, porque la frase '5 de 5 mesas "
             "completas' aparece en las cinco y no habla de ninguna nomina.")
    con_dec, con_mot = 0, 0
    tot_nom, tot_cob = 0, 0
    for x in mesas:
        dec = bool(str(x.get("adjudicacion") or "").strip())
        mot = bool(str(x.get("nota") or "").strip())
        con_dec += 1 if dec else 0
        con_mot += 1 if mot else 0
        ent = [e for e in D["inv"] if x["id_op"] in (e.get("operaciones") or [])]
        cob = [e for e in ent if str(e.get("cobertura") or "").strip()]
        tot_nom += len(ent)
        tot_cob += len(cob)
        c.append("  %-10s decision escrita: %-2s | motivo escrito: %-2s | "
                 "nominas del inventario que la nombran: %2d | de esas CON "
                 "cobertura al lado: %2d"
                 % (x["id_op"], "SI" if dec else "NO", "SI" if mot else "NO",
                    len(ent), len(cob)))
        for e in ent[:2]:
            c.append("     NOMINA> %s %s | cobertura: %s"
                     % (e.get("tipo"), str(e.get("nombre"))[:40],
                        str(e.get("cobertura"))[:46]))
    c.append("CIFRA mesas con decision escrita: %d de %d" % (con_dec, len(mesas)))
    c.append("CIFRA mesas con motivo escrito: %d de %d" % (con_mot, len(mesas)))
    c.append("CIFRA nominas del inventario de las cinco mesas: %d | CIFRA de "
             "esas CON cobertura al lado: %d | SIN cobertura: %d"
             % (tot_nom, tot_cob, tot_nom - tot_cob))
    if tot_nom == tot_cob and con_dec == len(mesas) and con_mot == len(mesas):
        return "CUBRE", c
    if tot_cob or con_dec:
        return "A MEDIAS", c
    return "NO CUBRE", c


def s_cuatro_controles(D):
    c = []
    c.append("LA CLAUSULA PIDE CUATRO Y LA PAGINA 07 NOMBRA CINCO, y eso se dice "
             "delante en vez de resolverlo callando: la tabla LOS CINCO "
             "CONTROLES MECANICOS QUE LA ACOMPANAN de docs/plan/07_ADUANA.md "
             "trae cinco filas, y la verificacion de OP-A-02 escribe 'los CINCO "
             "controles mecanicos corriendo'. El quinto nacio el 13 ago 2026, "
             "despues de que se escribiera esta celda.")
    c.append("CIFRA etiquetas de Gate 0 leidas de la corrida de esta vuelta: %d"
             % len(D["gate0"]))
    corriendo, verdes = 0, 0
    for nombre, marcas in CONTROLES_ADUANA:
        hits = [(e, t) for e, t in D["gate0"]
                if all(m.lower() in t.lower() for m in marcas)]
        if hits:
            corriendo += 1
            if all(e == "OK" for e, _ in hits):
                verdes += 1
        c.append("  %-54s marca %-28s | etiquetas %d | %s"
                 % (nombre[:54], " y ".join(marcas), len(hits),
                    (" | ".join("[%s] %s" % (e, t[:58]) for e, t in hits[:2]))
                    or "NINGUNA: la busqueda da CERO y ese cero es el resultado"))
    c.append("CIFRA controles de la pagina 07 que CORREN hoy en Gate 0: %d de "
             "%d | CIFRA de esos en verde: %d"
             % (corriendo, len(CONTROLES_ADUANA), verdes))
    c.append("CIFRA que la clausula pide: 4")
    if corriendo >= 4 and verdes == corriendo:
        return "CUBRE", c
    if corriendo:
        return "A MEDIAS", c
    return "NO CUBRE", c


SONDAS = {
    ("0 CODIGO", 0): s_caso_positivo,
    ("01 FUENTES", 0): s_pasos_no_alterados,
    ("01 FUENTES", 1): s_segundo_libro,
    ("02 DESTEJIDOS", 0): s_quince_congelados,
    ("02 DESTEJIDOS", 1): s_perdida_en_su_bloque,
    ("03 FUSIONES", 0): s_un_superviviente,
    ("03 FUSIONES", 1): s_resolver_da_superviviente,
    ("04 ENLACES", 0): s_arista_confirmada_por_lectura,
    ("04 ENLACES", 1): s_sin_autoarista,
    ("05 SANEO", 0): s_tratado_extinto,
    ("05 SANEO", 1): s_incoterms,
    ("05 SANEO", 2): s_export_gov,
    ("05 SANEO", 3): s_seis_herramientas,
    ("05 SANEO", 4): s_dos_claves_de_fase,
    ("05 SANEO", 5): s_autocita_tras_resolver,
    ("06 MESAS", 0): s_decision_con_motivo_y_cobertura,
    ("07 ADUANA", 0): s_cuatro_controles,
}


# ---------------------------------------------------------------------------
# LOS MUTANTES. SE FABRICAN EN MEMORIA SOBRE UNA COPIA PROFUNDA Y NO TOCAN
# NINGUNA FICHA, NINGUN NODO Y NINGUNA PAGINA.
# ---------------------------------------------------------------------------

def _r_caso_positivo(D):
    D["pruebas"] = []
    D["gate0"] = []
    D["rojas_por_op"] = {}
    return D


def _r_pasos(D):
    clase = D["ops"]["OP-F-01"][1].get("nodos") or []
    if clase:
        D["N"][clase[0]]["pasos_accionables"] = ["un solo paso podado"]
    return D


def _r_segundo_libro(D):
    nid = (D["ops"]["OP-F-03"][1].get("nodos") or [None])[0]
    if nid:
        D["N"].pop(nid, None)
        for _k, v in D["N"].items():
            if nid in (v.get("ids_alias") or []):
                v["ids_alias"] = [a for a in v["ids_alias"] if a != nid]
    return D


def _r_congelados(D):
    fase02 = [x for x in D["F"] if x["fase"] == "02_DESTEJIDOS"]
    nodos = [n for x in fase02 for n in (x.get("nodos") or [])]
    if len(nodos) >= 2:
        D["ver"] = D["ver"] + [{
            "puesto_intra": 999999, "clase": "A", "nodo_a": nodos[0],
            "nodo_b": nodos[1],
            "razon": "NO SE JUZGA HOY: fabricado en memoria para el mutante"}]
        D["n_ver"] = D["n_ver"] + 1
    return D


def _r_perdida(D):
    D["ls02"] = ["(pagina vaciada en memoria para el mutante)"]
    for x in D["F"]:
        if x["fase"] == "02_DESTEJIDOS":
            x["preservar"] = []
            x["nota"] = ""
            x["adjudicacion"] = ""
            x["verificacion"] = []
    return D


def _r_un_superviviente(D):
    actos, _ = _actos_vigentes(D)
    for a in actos:
        ms = a.get("miembros") or []
        vivos = [m for m in ms
                 if m in D["N"] and not D["N"][m].get("deprecado")]
        if len(vivos) == 1 and len(ms) > 1:
            s = vivos[0]
            D["N"][s]["ids_alias"] = []
            return D
    return D


def _r_resolver(D):
    actos, _ = _actos_vigentes(D)
    for a in actos:
        ms = a.get("miembros") or []
        vivos = [m for m in ms
                 if m in D["N"] and not D["N"][m].get("deprecado")]
        if len(vivos) == 1 and len(ms) > 1:
            s = vivos[0]
            otro = [m for m in ms if m != s][0]
            D["N"][s]["ids_alias"] = [a2 for a2 in (D["N"][s].get("ids_alias") or [])
                                      if a2 != otro]
            if otro in D["N"]:
                D["N"][otro]["deprecado"] = True
            return D
    return D


def _r_confirmada(D):
    if D["e06"]:
        D["e06"] = copy.deepcopy(D["e06"])
        D["e06"][0]["puesto"] = -12345
    return D


def _r_autoarista_nueva(D):
    if D["e07"]:
        D["e07"] = copy.deepcopy(D["e07"])
        D["e07"][0]["hijo"] = D["e07"][0]["madre"]
    return D


def _r_tratado(D):
    nom = _nomina(D, "OP-S-01")
    for nid in nom:
        if nid in D["N"] and D["N"][nid].get("deprecado"):
            D["N"][nid]["deprecado"] = False
            return D
    return D


def _r_incoterms(D):
    nom = _nomina(D, "OP-S-02")
    res = V150.resolutor(D["N"])
    for nid in nom:
        s = res(nid)
        if s in D["N"]:
            D["N"][s]["resumen_teorico"] = "sin version escrita"
            D["N"][s]["titulo_concepto"] = "sin version"
            D["N"][s]["pasos_accionables"] = []
            D["N"][s]["entregable_esperado"] = ""
            D["N"][s]["condiciones_activacion"] = []
    return D


def _r_export(D):
    nid = (_nomina(D, "OP-S-03") or [None])[0]
    if nid and nid in D["N"]:
        D["N"][nid]["resumen_teorico"] = "vuelve a cablear export.gov"
    return D


def _r_herramientas(D):
    nid = (_nomina(D, "OP-S-04") or [None])[0]
    if nid and nid in D["N"]:
        D["N"][nid]["resumen_teorico"] = "usar Alexa y Compete para medir"
    return D


def _r_claves(D):
    k = next(iter(D["N"]))
    D["N"][k]["fase_proekto"] = "ejecucion"
    return D


def _r_autocita(D):
    for k, v in D["N"].items():
        if not v.get("deprecado"):
            v["nodos_previos"] = list(v.get("nodos_previos") or []) + [k]
            return D
    return D


def _r_mesas(D):
    for e in D["inv"]:
        if any(o.startswith("OP-M-") for o in (e.get("operaciones") or [])):
            e["cobertura"] = ""
            return D
    return D


def _r_controles(D):
    D["gate0"] = [(e, t) for e, t in D["gate0"]
                  if "comprobacion posicional" not in t
                  and "lista CANONICA de libros" not in t]
    return D


MUTANTES_ROTOS = {
    ("0 CODIGO", 0): ("desaparecen las pruebas, las etiquetas y las salidas",
                      _r_caso_positivo),
    ("01 FUENTES", 0): ("un miembro de la clase queda con un solo paso", _r_pasos),
    ("01 FUENTES", 1): ("un nodo de la nomina se borra sin dejar alias",
                        _r_segundo_libro),
    ("02 DESTEJIDOS", 0): ("aparece un congelado de la nomina de la fase 02",
                           _r_congelados),
    ("02 DESTEJIDOS", 1): ("la pagina 02 se queda sin registros y las fichas sin "
                           "regla", _r_perdida),
    ("03 FUSIONES", 0): ("un superviviente pierde sus alias", _r_un_superviviente),
    ("03 FUSIONES", 1): ("un absorbido deja de resolver a su superviviente",
                         _r_resolver),
    ("04 ENLACES", 0): ("una arista nueva cita un puesto que no existe",
                        _r_confirmada),
    ("04 ENLACES", 1): ("una arista nueva se cierra sobre si misma",
                        _r_autoarista_nueva),
    ("05 SANEO", 0): ("el id con el tratado extinto vuelve a estar vivo",
                      _r_tratado),
    ("05 SANEO", 1): ("los supervivientes pierden la version", _r_incoterms),
    ("05 SANEO", 2): ("un nodo de la nomina vuelve a cablear el dominio muerto",
                      _r_export),
    ("05 SANEO", 3): ("un nodo de la nomina vuelve a nombrar dos muertas",
                      _r_herramientas),
    ("05 SANEO", 4): ("un nodo recibe una segunda clave de fase", _r_claves),
    ("05 SANEO", 5): ("un nodo vivo se cita a si mismo", _r_autocita),
    ("06 MESAS", 0): ("una nomina de mesa se queda sin cobertura", _r_mesas),
    ("07 ADUANA", 0): ("dos controles dejan de correr en Gate 0", _r_controles),
}


def _s_pasos(D):
    clase = D["ops"]["OP-F-01"][1].get("nodos") or []
    for nid in clase:
        if nid in D["Nb"] and nid in D["N"]:
            D["N"][nid]["pasos_accionables"] = list(
                D["Nb"][nid].get("pasos_accionables") or [])
    return D


def _s_segundo_libro(D):
    for i in ("OP-F-02", "OP-F-03", "OP-F-04-COL", "OP-F-04-HOR",
              "OP-F-04-WEI", "OP-F-04-RAC"):
        for nid in (D["ops"][i][1].get("nodos") or []):
            nd = D["N"].get(nid)
            if nd is None:
                continue
            fu = str(nd.get("fuente") or "")
            if " | " in fu:
                nd["fuente"] = fu.split(" | ")[0]
    return D


def _s_un_superviviente(D):
    """EL MUNDO EN QUE LA FASE 03 YA ESTA CORRIDA: el inventario se queda con
    los actos que YA tienen un solo superviviente vivo. No se toca el grafo, y
    se dice por que: deprecar a mano los miembros de un acto mueve tambien a
    OTROS actos que comparten ese nodo, y el mutante mediria entonces un
    desorden fabricado por el en vez de un mundo sano."""
    actos, _ = _actos_vigentes(D)
    fundidos = []
    for a in actos:
        vivos = [m for m in (a.get("miembros") or [])
                 if m in D["N"] and not D["N"][m].get("deprecado")]
        if len(vivos) == 1:
            fundidos.append(a)
    otros = [e for e in D["inv"] if e.get("tipo") != "acto"]
    D["inv"] = otros + fundidos
    return D


def _s_incoterms(D):
    nom = _nomina(D, "OP-S-02")
    res = V150.resolutor(D["N"])
    for nid in nom:
        s = res(nid)
        if s in D["N"]:
            D["N"][s]["resumen_teorico"] = (
                str(D["N"][s].get("resumen_teorico") or "")
                + " Los Incoterms 2020 fijan el reparto.")
    return D


MUTANTES_SANOS = {
    ("01 FUENTES", 0): ("los seis vuelven al texto del grafo previo", _s_pasos),
    ("01 FUENTES", 1): ("las nominas dejan de declarar un segundo libro",
                        _s_segundo_libro),
    ("03 FUSIONES", 0): ("los actos sin fundir quedan con un superviviente y sus "
                         "alias", _s_un_superviviente),
    ("05 SANEO", 1): ("los tres supervivientes traen la version", _s_incoterms),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate0", required=True)
    ap.add_argument("--corte", required=True)
    ap.add_argument("--apertura", required=True)
    args = ap.parse_args()

    sha_exp_0 = sha(EXPEDIENTE)
    sha_vara_0 = sha(VARA)
    print("=" * 78)
    print("VUELTA 217, TAREA 1. LAS DIECISIETE CLAUSULAS DE LAS FASES 0 A 07")
    print("=" * 78)
    print("SHA256 DE docs/plan/OPERACIONES.jsonl AL ENTRAR: %s disco y %s LF"
          % sha_exp_0)
    print("SHA256 DE docs/plan/08_VERIFICACION.md AL ENTRAR: %s disco y %s LF"
          % sha_vara_0)
    print("")
    fallos = 0

    print("=" * 78)
    print("1.a. LAS FILAS Y SUS CLAUSULAS, SACADAS CON UN INSTRUMENTO")
    print("=" * 78)
    print("EL LECTOR SE IMPORTA, NO SE CLONA: celdas_de_la_tabla de "
          "scripts/loop/vuelta150_4_tabla_por_fase.py.")
    print("CIFRA lineas de ese fichero: %d | CIFRA lineas ejecutadas al "
          "cargarlo: %d. La diferencia es SU ULTIMA LINEA DE ENTRADA, una "
          "llamada suelta a main() sin guarda, que se descarta para cargar sus "
          "lectores sin correr su tabla. EL FICHERO EN DISCO NO SE TOCA: la "
          "moratoria prohibe repararlo y no se repara."
          % (_V150_LINEAS, _V150_EJECUTADAS))
    filas = V150.celdas_de_la_tabla()
    clausulas_por_fila = [(f, partir_en_clausulas(c)) for f, c in filas]
    total_cl = sum(len(cl) for _f, cl in clausulas_por_fila)
    print("CIFRA FILAS ARMADAS LEYENDO LA TABLA POR FASE: %d | CIFRA FILAS QUE "
          "DEBERIA HABER: %d" % (len(filas), CONTRASTE_FILAS_TOTAL))
    print("CIFRA CLAUSULAS ARMADAS EN LA TABLA ENTERA: %d | CIFRA QUE DEBERIA "
          "HABER: %d" % (total_cl, CONTRASTE_CLAUSULAS_TOTAL))
    print("EL PARTIDOR ES EL PUNTO Y COMA DE LA PROPIA PAGINA, no una regla mia.")
    print("")
    print("EL REPARTO POR FILA, CONTADO Y NO TECLEADO:")
    for f, cl in clausulas_por_fila:
        esperado = CONTRASTE_REPARTO.get(f)
        print("  %-22s clausulas armadas %2d | que deberia haber %s"
              % (f, len(cl), esperado if esperado is not None else "(fuera de "
                 "las ocho: el encargo no da cifra)"))
    de_0_a_07 = [(f, cl) for f, cl in clausulas_por_fila if f in FILAS_0_A_07]
    total_0_07 = sum(len(cl) for _f, cl in de_0_a_07)
    print("")
    print("CIFRA FILAS DE 0 CODIGO A 07 ADUANA ARMADAS: %d | CIFRA QUE DEBERIA "
          "HABER: %d" % (len(de_0_a_07), CONTRASTE_FILAS_0_07))
    print("CIFRA CLAUSULAS DE ESAS OCHO FILAS ARMADAS: %d | CIFRA QUE DEBERIA "
          "HABER: %d" % (total_0_07, CONTRASTE_CLAUSULAS_0_07))
    descuadres = []
    if len(filas) != CONTRASTE_FILAS_TOTAL:
        descuadres.append("filas de la tabla entera")
    if total_cl != CONTRASTE_CLAUSULAS_TOTAL:
        descuadres.append("clausulas de la tabla entera")
    if len(de_0_a_07) != CONTRASTE_FILAS_0_07:
        descuadres.append("filas de 0 a 07")
    if total_0_07 != CONTRASTE_CLAUSULAS_0_07:
        descuadres.append("clausulas de 0 a 07")
    for f, cl in de_0_a_07:
        if CONTRASTE_REPARTO.get(f) != len(cl):
            descuadres.append("reparto de la fila %s" % f)
    print("CIFRA descuadres contra las cifras del encargo: %d" % len(descuadres))
    for d in descuadres:
        print("   DESCUADRE> %s" % d)
    if descuadres:
        print("ROJO Y PARADA: mi instrumento saca otro numero que el encargo. "
              "Las dos cifras quedan escritas arriba y no se resuelve copiando.")
        return 1
    print("LAS DOS CIFRAS CALZAN EN LOS CUATRO CONTEOS Y EN LAS OCHO FILAS.")
    print("")
    print("LAS DIECISIETE, VERBATIM, CON SU FILA Y SU INDICE:")
    orden = []
    for f, cl in de_0_a_07:
        for k, texto in enumerate(cl):
            orden.append((f, k, texto))
            print("  %-16s idx %d | %s" % (f, k, texto))
    print("")

    D = cargar(args.gate0, args.corte, args.apertura)

    print("=" * 78)
    print("1.b Y 1.c. LAS DIECISIETE, MEDIDAS UNA POR UNA, CON SU BUSQUEDA")
    print("=" * 78)
    resultados = []
    for n, (f, k, texto) in enumerate(orden, start=1):
        sonda = SONDAS.get((f, k))
        print("")
        print("-" * 78)
        print("CLAUSULA %2d de %d | fila %s | indice %d" % (n, len(orden), f, k))
        print("   VERBATIM: %s" % texto)
        print("-" * 78)
        if sonda is None:
            print("ROJO: no hay sonda para esta clausula.")
            fallos += 1
            resultados.append((f, k, texto, "SIN SONDA"))
            continue
        veredicto, cifras = sonda(_copia(D))
        for l in cifras:
            print("   " + l)
        print("   VEREDICTO MEDIDO HOY: **%s**" % veredicto)
        resultados.append((f, k, texto, veredicto))
    print("")

    print("=" * 78)
    print("1.d. EL CASO ROJO NO SE PROMETE, SE PRUEBA POR MUTACION")
    print("=" * 78)
    print("EL MUTANTE SE FABRICA EN MEMORIA SOBRE UNA COPIA PROFUNDA Y NO SE "
          "ESCRIBE EN NINGUNA FICHA, NINGUN NODO NI NINGUNA PAGINA.")
    print("")
    caen = 0
    for n, (f, k, _t) in enumerate(orden, start=1):
        nombre, romper = MUTANTES_ROTOS[(f, k)]
        Dm = romper(_copia(D))
        v, _ = SONDAS[(f, k)](Dm)
        cae = (v != "CUBRE")
        caen += 1 if cae else 0
        print("MUTANTE ROTO %2d | %-16s idx %d | %-50s | veredicto %-9s | CAE: %s"
              % (n, f, k, nombre[:50], v, "SI" if cae else "NO"))
    print("")
    print("CIFRA mutantes rotos: %d | CIFRA que CAEN (o sea que NO dicen CUBRE): "
          "%d" % (len(orden), caen))
    if caen != len(orden):
        print("ROJO: alguna sonda dice CUBRE sobre datos rotos.")
        fallos += 1
    print("")
    print("Y EL REVERSO, PORQUE UNA SONDA QUE NUNCA PUEDE DECIR CUBRE TAMPOCO "
          "MIDE: las que hoy NO dan CUBRE llevan ademas un mutante SANO, y "
          "tienen que SUBIR.")
    suben = 0
    for clave, (nombre, sanar) in MUTANTES_SANOS.items():
        Dm = sanar(_copia(D))
        v, _ = SONDAS[clave](Dm)
        sube = (v == "CUBRE")
        suben += 1 if sube else 0
        print("MUTANTE SANO    | %-16s idx %d | %-50s | veredicto %-9s | SUBE: %s"
              % (clave[0], clave[1], nombre[:50], v, "SI" if sube else "NO"))
    print("CIFRA mutantes sanos: %d | CIFRA que SUBEN a CUBRE: %d"
          % (len(MUTANTES_SANOS), suben))
    if suben != len(MUTANTES_SANOS):
        print("ROJO: alguna sonda no puede decir CUBRE ni con datos sanos.")
        fallos += 1
    no_cubren = [r for r in resultados if r[3] != "CUBRE"]
    print("CIFRA clausulas que hoy NO dan CUBRE: %d | CIFRA de esas con mutante "
          "sano probado: %d" % (len(no_cubren), len(MUTANTES_SANOS)))
    if len(no_cubren) != len(MUTANTES_SANOS):
        print("AVISO: no todas las que no dan CUBRE tienen mutante sano, y se "
              "dice en vez de callarlo.")
    print("")

    print("=" * 78)
    print("EL REPARTO, CONTADO DE LO DE ARRIBA Y NO TECLEADO")
    print("=" * 78)
    for v in ("CUBRE", "A MEDIAS", "NO CUBRE", "SIN SONDA"):
        n = sum(1 for r in resultados if r[3] == v)
        print("CIFRA clausulas en %-10s: %d de %d" % (v, n, len(resultados)))
    print("")
    print("LA TABLA DE LAS DIECISIETE, FILA A FILA:")
    print("| # | fila | idx | veredicto | la clausula, VERBATIM |")
    print("|---:|---|---:|---|---|")
    for n, (f, k, t, v) in enumerate(resultados, start=1):
        print("| %d | %s | %d | %s | %s |" % (n, f, k, v, t))
    print("CIFRA FILAS DE ESTA TABLA: %d | CIFRA QUE DEBERIA HABER: %d"
          % (len(resultados), CONTRASTE_CLAUSULAS_0_07))
    print("")
    print("LAS QUE NO DAN CUBRE, CON SU FILA, SU INDICE Y SU CIFRA:")
    if not no_cubren:
        print("   NINGUNA: las diecisiete dan CUBRE.")
    for f, k, t, v in no_cubren:
        print("   %-16s idx %d | %-9s | %s" % (f, k, v, t[:96]))
    print("")

    print("=" * 78)
    print("1.e. NO SE ESCRIBIO NADA: LOS DOS SHA, AL ENTRAR Y AL SALIR")
    print("=" * 78)
    sha_exp_1 = sha(EXPEDIENTE)
    sha_vara_1 = sha(VARA)
    print("SHA256 DE docs/plan/OPERACIONES.jsonl AL SALIR: %s disco y %s LF"
          % sha_exp_1)
    print("SHA256 DE docs/plan/08_VERIFICACION.md AL SALIR: %s disco y %s LF"
          % sha_vara_1)
    igual = (sha_exp_0 == sha_exp_1 and sha_vara_0 == sha_vara_1)
    print("LOS CUATRO SHA COINCIDEN CON LOS DE LA ENTRADA: %s"
          % ("SI" if igual else "NO"))
    if not igual:
        print("ROJO: algo se escribio y no debia.")
        fallos += 1
    print("")
    print("CIFRA comprobaciones de este instrumento que fallan: %d" % fallos)
    print("VERDE: la medicion queda corrida." if not fallos
          else "ROJO: la medicion tiene fallos declarados arriba.")
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
