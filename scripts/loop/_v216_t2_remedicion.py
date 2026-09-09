# -*- coding: utf-8 -*-
r"""_v216_t2_remedicion.py . LA RE-MEDICION QUE EL FUNDADOR ORDENO EL 9 SEP 2026:
LAS CINCO FICHAS SIN EJECUTAR, MEDIDAS CONTRA LAS CATORCE FILAS DE DERIVACION.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). Muere con la vuelta y no vigila nada.

QUIEN LO ORDENA, POR SU RUTA Y NO DE MEMORIA:
docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md, DECISION 2, verbatim:
"las cinco fichas SIN EJECUTAR se re-miden contra esas filas (OP-V-01 con su
prueba por cita de la corrida K ya escrita)".

QUE HACE, Y ES LO QUE LA 214 DEJO A MEDIAS:
  (a) SACA LAS CATORCE FILAS con un instrumento, de la tabla de derivacion de
      docs/plan/08_VERIFICACION.md, y COTEJA cada clausula, VERBATIM, contra
      el indice y la linea de docs/plan/OPERACIONES.jsonl que la fila declara.
      Si el numero de filas no es CATORCE, PARA.
  (b) CORRE UNA SONDA POR CADA UNA DE LAS CATORCE, hoy, y publica CUBRE,
      A MEDIAS o NO CUBRE con la busqueda corrida y su cifra delante,
      INCLUIDAS LAS QUE DAN CERO. La 214 dejo SEIS de las catorce sin sonda,
      declaradas documentales; aqui las catorce llevan sonda corrida.
  (c) OP-V-01 VA POR CITA DE LA CORRIDA K, que es lo que la DECISION 2 manda:
      se BUSCA, no se inventa, y si no apareciera se publicaria la busqueda
      que la busco.

LAS CORRECCIONES DECLARADAS NO SON CLAUSULAS DE LA VARA Y NO ENTRAN (registro
R.72 del acta 208), pero SI SE LEEN: la propia tabla dice, columna a columna,
que correccion corrige que clausula, y una clausula corregida se mide POR SU
LECTURA CORREGIDA. Leer la correccion no es medirla.

NO ESCRIBE EN NINGUNA FICHA Y NO MUEVE NI UN CAMPO DE ESTADO. Lo comprueba con
los dos sha256 del expediente, al entrar y al salir.

IMPORTAR NO ES CLONAR (acta 206, 6.5): es_relleno, es_vacio y
es_del_vocabulario se IMPORTAN de _v215_t4_dos_puntos.py, que es donde nacieron
con su correccion declarada dentro.

USO:  python scripts/loop/_v216_t2_remedicion.py
"""
import copy
import hashlib
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v215_t4_dos_puntos import (  # noqa: E402
    es_relleno, es_vacio, es_del_vocabulario)

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VARA = os.path.join(RAIZ, "docs", "plan", "08_VERIFICACION.md")
EXPEDIENTE = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
INV = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
CORRIDA_K = os.path.join(RAIZ, "docs", "loop",
                         "SALIDA_SESION_CREDENCIAL_VUELO_K.txt")
VISTA_HUMANA = "10_INVENTARIO.md"
COMMIT_OP_V_01 = "e966d896"

FILA = re.compile(
    r"^\| \*\*(.+?)\*\* \| `(OP-[A-Z]-\d+)` \| (\d+) \| (\d+) \| (.+?) \| (.+?) \|$")
CABECERA_LD = re.compile(r"^#+ `(LD-\d+)` \. `([^`]+)` contra `([^`]+)`")
COBERTURA = re.compile(
    r"(\d+) de (\d+) pares leidos; (\d+) en cola; (\d+) fuera de cola")
NOMINA_SEGUNDA = re.compile(r"^## (.+?): \d+ de \d+, y cae\s*$")

# LAS CINCO PARTES DE LA CLAUSULA TRANSVERSAL DE OP-V-01, PARTIDAS POR SU
# PROPIA COMA, Y LA MARCA CON LA QUE CADA UNA SE BUSCA. La marca es mia y se
# dice que lo es; la parte sale de la clausula. Cada marca puede traer VARIAS
# formas, porque las dos sedes escriben la misma cifra de dos maneras.
#
# CORRECCION DECLARADA DE ESTA MISMA VUELTA, Y NO TAPA LO QUE CORRIGE: la marca
# del vuelo completo era el literal "16" a secas, que es MAS LAXA QUE SU
# CLAUSULA porque casa con cualquier linea que lleve ese numero por cualquier
# motivo. Se estrecha a las dos formas en que las dos sedes escriben la cifra
# del vuelo, y la version laxa queda escrita aqui y no se borra.
MARCAS_TRANSVERSAL = (
    ("Gate 0 verde", ("GATE 0 VERDE",)),
    ("suite verde", ("motor 25/25",)),
    ("vuelo completo", ("16 de 16", "16/16")),
    ("prueba de rumbos", ("PRUEBA DE RUMBOS",)),
    ("reindexado semantico DESPUES de mover ids", ("d70adc1d",)),
)


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def sha(ruta):
    b = io.open(ruta, "rb").read()
    return hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16]


def lineas(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(
        chr(13) + NL, NL).split(NL)


def jsonl(ruta):
    return [json.loads(l) for l in lineas(ruta) if l.strip()]


# ---------------------------------------------------------------------------
# (a) LAS CATORCE FILAS, LEIDAS CON UN INSTRUMENTO
# ---------------------------------------------------------------------------

def filas_de_derivacion(ls):
    """LAS FILAS DE LA TABLA DE DERIVACION, CON SU LINEA ABSOLUTA. PURA."""
    fuera = []
    for i, l in enumerate(ls):
        m = FILA.match(l)
        if m:
            fuera.append({
                "linea_vara": i + 1,
                "fase": m.group(1),
                "ficha": m.group(2),
                "indice": int(m.group(3)),
                "linea_exp": int(m.group(4)),
                "clausula": m.group(5).strip(),
                "corregida_por": m.group(6).strip(),
            })
    return fuera


# ---------------------------------------------------------------------------
# LOS DATOS QUE LAS SONDAS MIDEN. TODAS LAS SONDAS SON PURAS SOBRE ESTE DICT,
# PARA QUE EL MUTANTE SE PUEDA FABRICAR EN MEMORIA Y NO EN NINGUNA FICHA.
# ---------------------------------------------------------------------------

def cargar():
    inv = jsonl(INV)
    ver = jsonl(VEREDICTOS)
    ops = {}
    for n, l in enumerate(lineas(EXPEDIENTE), start=1):
        if l.strip():
            d = json.loads(l)
            ops[d["id_op"]] = (n, d)
    ld_ls = lineas(LD)
    ld_pares, las_once = [], []
    dentro_once = False
    for l in ld_ls:
        if l.startswith("## LAS ONCE, una por una"):
            dentro_once = True
        elif dentro_once and l.startswith("## "):
            dentro_once = False
        m = CABECERA_LD.match(l)
        if m:
            par = (m.group(1), m.group(2), m.group(3))
            ld_pares.append(par)
            if dentro_once:
                las_once.append(par)
    nombran, escriben = [], []
    for base, _, ficheros in os.walk(os.path.join(RAIZ, "scripts")):
        for f in ficheros:
            if not f.endswith(".py"):
                continue
            p = os.path.join(base, f)
            try:
                t = io.open(p, encoding="utf-8").read()
            except Exception:
                continue
            if VISTA_HUMANA not in t:
                continue
            rel = os.path.relpath(p, RAIZ).replace(os.sep, "/")
            nombran.append(rel)
            ts = t.replace(chr(13) + NL, NL).split(NL)
            for i, l in enumerate(ts):
                if VISTA_HUMANA not in l:
                    continue
                ventana = NL.join(ts[i:i + 4])
                if re.search(r'open\([^)]*"w|open\([^)]*\'w|\.write\(', ventana):
                    escriben.append(rel)
                    break
    ck_existe = os.path.isfile(CORRIDA_K)
    return {
        "inv": inv,
        "n_ver": len(ver),
        "ver_por_par": {frozenset((v["nodo_a"], v["nodo_b"])): v for v in ver},
        "puestos": sorted(v["puesto_intra"] for v in ver),
        "ops": ops,
        "ld_ls": ld_ls,
        "ld_pares": ld_pares,
        "las_once": las_once,
        "ck_existe": ck_existe,
        "ck_bytes": os.path.getsize(CORRIDA_K) if ck_existe else 0,
        "ck_bytes_lf": (len(io.open(CORRIDA_K, "rb").read()
                            .replace(b"\r\n", b"\n")) if ck_existe else 0),
        "ck_ls": lineas(CORRIDA_K) if ck_existe else [],
        "commit_ls": git(["show", "-s", "--format=%B", COMMIT_OP_V_01])[1]
                     .replace(chr(13) + NL, NL).split(NL),
        "py_nombran": sorted(set(nombran)),
        "py_escriben": sorted(set(escriben)),
    }


def escrituras_declaradas(D, ficha):
    """CUANTAS ESCRITURAS DECLARA LA FICHA EN SUS CUATRO CAMPOS DE OBRA. Es la
    vara que la correccion declarada de OP-L-01 (indice 4) fija para la
    clausula del marcador: 2.117 es TESTIGO y no condicion, y lo que la
    clausula pide es que ESTA operacion no lo mueva. PURA."""
    d = D["ops"][ficha][1]
    return sum(len(d.get(k) or [])
               for k in ("nodos", "preservar", "eliminar", "aristas_nuevas"))


# ---------------------------------------------------------------------------
# LAS CATORCE SONDAS. CADA UNA ES PURA SOBRE D Y DEVUELVE
# (veredicto, [lineas de cifra]).
# ---------------------------------------------------------------------------

def s_transversal(D):
    c = []
    c.append("CIFRA la corrida K existe en disco: %s"
             % ("SI" if D["ck_existe"] else "NO (ausencia, no cero)"))
    c.append("CIFRA bytes exactos de la corrida K: %d bytes en disco y %d "
             "bytes normalizado a LF" % (D["ck_bytes"], D["ck_bytes_lf"]))
    c.append("RUTA de la corrida K: docs/loop/SALIDA_SESION_CREDENCIAL_VUELO_K.txt")
    c.append("CIFRA lineas de la corrida K: %d" % len(D["ck_ls"]))
    c.append("CIFRA lineas del cuerpo del commit %s, que es el que movio el "
             "estado: %d" % (COMMIT_OP_V_01, len(D["commit_ls"])))
    sostenidas = 0
    for parte, marcas in MARCAS_TRANSVERSAL:
        en_ck = [i + 1 for i, l in enumerate(D["ck_ls"])
                 if any(m in l for m in marcas)]
        en_cm = [i + 1 for i, l in enumerate(D["commit_ls"])
                 if any(m in l for m in marcas)]
        hay = bool(en_ck or en_cm)
        sostenidas += 1 if hay else 0
        c.append("PARTE %-42s marca %-22s | corrida K linea(s) %s | commit "
                 "linea(s) %s | SOSTENIDA: %s"
                 % (parte[:42], " o ".join(marcas), (en_ck[:3] or "ninguna"),
                    (en_cm[:3] or "ninguna"), "SI" if hay else "NO"))
        if en_ck:
            c.append("   CITA corrida K %d: %s"
                     % (en_ck[0], D["ck_ls"][en_ck[0] - 1].strip()[:130]))
        if en_cm:
            c.append("   CITA commit %d: %s"
                     % (en_cm[0], D["commit_ls"][en_cm[0] - 1].strip()[:130]))
    c.append("CIFRA partes de la clausula: %d | CIFRA sostenidas por cita: %d"
             % (len(MARCAS_TRANSVERSAL), sostenidas))
    if not D["ck_existe"]:
        return "NO CUBRE", c
    if sostenidas == len(MARCAS_TRANSVERSAL):
        return "CUBRE", c
    if sostenidas:
        return "A MEDIAS", c
    return "NO CUBRE", c


def _apariciones(D, universo):
    """LAS LECTURAS DIRIGIDAS DE UN UNIVERSO QUE TIENEN FILA EN EL ARCHIVO, Y
    CON LA PREGUNTA QUE DE VERDAD IMPORTA AL LADO: si esa fila ES una RELECTURA
    declarada de un puesto que YA existia, o si la lectura dirigida CREO puesto
    nuevo. PURA."""
    fuera = []
    for n, a, b in universo:
        fila = D["ver_por_par"].get(frozenset((a, b)))
        if fila is None:
            continue
        razon = str(fila.get("razon") or "")
        fuera.append((n, a, b, fila.get("puesto_intra"), n in razon))
    return fuera


def s_once_no_aparecen(D):
    c = []
    caen_once = _apariciones(D, D["las_once"])
    caen_todas = _apariciones(D, D["ld_pares"])
    nuevas = [x for x in caen_todas if not x[4]]
    c.append("EL SUJETO DE LA CLAUSULA SON LAS ONCE, Y NO SE TECLEAN: se leen "
             "de las cabeceras que viven bajo la seccion LAS ONCE, una por "
             "una, de docs/plan/LECTURAS_DIRIGIDAS.md, que es la tanda de esta "
             "ficha.")
    c.append("CIFRA cabeceras LD leidas bajo esa seccion: %d | CIFRA que la "
             "clausula dice: 11" % len(D["las_once"]))
    c.append("CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d" % D["n_ver"])
    c.append("CIFRA pares distintos del archivo: %d" % len(D["ver_por_par"]))
    c.append("LA COMPARACION ES LITERAL Y POR EL PAR, NUNCA POR NOMBRE SUELTO: "
             "se pregunta si el PAR de la lectura dirigida es par de alguna "
             "fila del archivo.")
    c.append("CIFRA de LAS ONCE que APARECEN en el archivo: %d" % len(caen_once))
    for n, a, b, puesto, rel in caen_once:
        c.append("   APARECE> %s (%s contra %s) en el puesto %s" % (n, a, b, puesto))
    if not caen_once:
        c.append("   (la busqueda da CERO, y ese cero es el resultado: se "
                 "corrio y se publica con su comando delante)")
    c.append("Y LA LECTURA ANCHA, PUBLICADA AUNQUE NO SEA EL SUJETO DE LA "
             "CLAUSULA, porque el instrumento de la vuelta 203 mide ese otro "
             "universo: toda cabecera LD que haya HOY en la pagina.")
    c.append("CIFRA cabeceras LD en toda la pagina, contadas hoy: %d"
             % len(D["ld_pares"]))
    c.append("CIFRA de esas que tienen fila en el archivo: %d" % len(caen_todas))
    for n, a, b, puesto, rel in caen_todas:
        c.append("   CON FILA> %s (%s contra %s) en el puesto %s | su fila la "
                 "NOMBRA como relectura: %s" % (n, a, b, puesto,
                                                "SI" if rel else "NO"))
    c.append("CIFRA de esas filas que NO son relectura declarada de un puesto "
             "ya existente: %d" % len(nuevas))
    c.append("LA CIFRA ONCE DE LA CLAUSULA ES LA DE SU CORTE Y NO LA DE HOY: la "
             "pagina siguio creciendo, y eso se dice en vez de callarlo.")
    if not D["las_once"]:
        return "NO CUBRE", c
    return ("CUBRE" if not caen_once else "NO CUBRE"), c


def _marcador(D, ficha, c):
    esc = escrituras_declaradas(D, ficha)
    c.append("CIFRA marcador del cribado contado hoy, linea a linea de "
             "docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d" % D["n_ver"])
    c.append("CIFRA que la clausula escribe: 2117 (2.117)")
    c.append("LECTURA LITERAL: los dos numeros NO calzan, y se dice antes que "
             "nada en vez de resolverse copiando.")
    c.append("LECTURA CORREGIDA, QUE ES LA QUE LA PROPIA FICHA FIJO POR "
             "CORRECCION DECLARADA: 2.117 es el valor del marcador en la "
             "fecha_corte de la ficha, TESTIGO Y NO CONDICION, y lo que la "
             "clausula pide es que ESTA operacion no lo mueva.")
    c.append("CIFRA escrituras declaradas de %s en nodos, preservar, eliminar "
             "y aristas_nuevas: %d" % (ficha, esc))
    c.append("   (con CERO escrituras declaradas la operacion no puede mover "
             "el marcador ni queriendo)")
    return esc


def s_marcador_l01(D):
    c = []
    esc = _marcador(D, "OP-L-01", c)
    return ("CUBRE" if esc == 0 else "NO CUBRE"), c


def s_marcador_l02(D):
    c = []
    esc = _marcador(D, "OP-L-02", c)
    return ("CUBRE" if esc == 0 else "NO CUBRE"), c


def s_nominas_con_cobertura(D):
    c = []
    universo = [e for e in D["inv"] if e.get("tipo") in ("acto", "racimo")]
    sin = [e for e in universo if not str(e.get("cobertura") or "").strip()]
    c.append("EL SUJETO NO SE IMPROVISA: 'cada nomina afectada' son las "
             "nominas de los actos y racimos del inventario, por la "
             "adjudicacion 6.5 del acta 168 citada en la correccion declarada "
             "de esta misma ficha.")
    c.append("CIFRA entradas de docs/plan/INVENTARIO.jsonl: %d" % len(D["inv"]))
    c.append("CIFRA nominas de tipo acto mas racimo: %d" % len(universo))
    c.append("CIFRA de esas SIN cobertura escrita al lado: %d" % len(sin))
    for e in sin[:5]:
        c.append("   SIN COBERTURA> %s" % str(e.get("nombre"))[:70])
    if not sin:
        c.append("   (la busqueda de las que faltan da CERO, y ese cero es el "
                 "resultado)")
    return ("CUBRE" if not sin else "NO CUBRE"), c


def _articulo_fuera(nombre):
    """QUITA SOLO EL ARTICULO DE CABEZA, NUNCA LOS DE DENTRO. PURA.

    CORRECCION DECLARADA DE ESTA MISMA VUELTA, Y NO TAPA LO QUE CORRIGE. La
    primera corrida de esta sonda hacia replace('la ', '') sobre el nombre
    ENTERO, y por eso `la supervision de la IA` se convertia en
    `supervision de ia` y salia NO HALLADA en el inventario. La cifra que
    publicaba, 2 de 3 nominas halladas, era falsa POR MI SONDA y no por el
    dato. La primera version queda escrita aqui arriba y no se borra."""
    bajo = nombre.strip().lower()
    for art in ("los ", "las ", "la ", "el ", "un ", "una "):
        if bajo.startswith(art):
            return bajo[len(art):]
    return bajo


def s_tres_nominas(D):
    c = []
    nombres = []
    dentro = False
    for l in D["ld_ls"]:
        if l.startswith("# SEGUNDA TANDA"):
            dentro = True
            continue
        if dentro and l.startswith("# ") and not l.startswith("## "):
            break
        if not dentro:
            continue
        m = NOMINA_SEGUNDA.match(l)
        if m:
            nombres.append(m.group(1).split(",")[0].strip())
    c.append("LAS TRES NOMINAS NO SE TECLEAN: se leen de las cabeceras de la "
             "SEGUNDA TANDA de docs/plan/LECTURAS_DIRIGIDAS.md, que es la "
             "tanda de esta ficha.")
    c.append("CIFRA nominas leidas de esas cabeceras: %d | CIFRA que la "
             "clausula dice: 3" % len(nombres))
    for n in nombres:
        c.append("   NOMINA LEIDA> %s" % n)
    c.append("LA COBERTURA SE MIDE DE SUS CIFRAS Y NO DE LA PALABRA "
             "PROVISIONAL: una entrada puede traer esa palabra dentro de una "
             "frase que dice justo lo contrario, y contarla por subcadena "
             "seria una sonda mas laxa que su clausula.")
    completas, halladas = 0, 0
    for n in nombres:
        clave = _articulo_fuera(n)
        cand = [e for e in D["inv"]
                if clave in _articulo_fuera(str(e.get("nombre", "")))]
        if not cand:
            c.append("NOMINA %-28s NO HALLADA en el inventario (ausencia, no "
                     "cero)" % n[:28])
            continue
        halladas += 1
        e = cand[0]
        cob = str(e.get("cobertura") or "")
        forma = str(e.get("forma") or "")
        entero = json.dumps(e, ensure_ascii=False)
        m2 = re.search(r"(\d+) de (\d+)", cob)
        leidos, tot = (int(m2.group(1)), int(m2.group(2))) if m2 else (None, None)
        completa_entrada = (leidos is not None and leidos >= tot)
        m3 = re.search(r"(\d+) leidos y (\d+) SIN veredicto", entero)
        completa_nomina = (int(m3.group(2)) == 0) if m3 else None
        reescrita = bool(forma.strip()) and ("forma vieja de este campo" in entero)
        c.append("NOMINA %-28s | entrada %-30s"
                 % (n[:28], str(e.get("nombre"))[:30]))
        c.append("   LECTURA (i), LA DE LA ENTRADA ENTERA: cobertura %s | "
                 "CIERRA: %s" % (cob[:80], "SI" if completa_entrada else "NO"))
        if m3:
            c.append("   LECTURA (ii), LA DE LA NOMINA, DECLARADA POR LA PROPIA "
                     "ENTRADA: %s | CIERRA: %s"
                     % (m3.group(0), "SI" if completa_nomina else "NO"))
        else:
            c.append("   LECTURA (ii): la entrada NO declara una nomina aparte, "
                     "asi que la (i) es la unica y no hay dos universos.")
        c.append("   FORMA REESCRITA (la entrada guarda su forma vieja al "
                 "lado): %s" % ("SI" if reescrita else "NO"))
        cierra = completa_nomina if m3 else completa_entrada
        if cierra and reescrita:
            completas += 1
        c.append("   ESTA NOMINA CIERRA SU COBERTURA Y REESCRIBE SU FORMA: %s"
                 % ("SI" if (cierra and reescrita) else "NO"))
    c.append("CIFRA nominas halladas en el inventario: %d de %d"
             % (halladas, len(nombres)))
    c.append("CIFRA nominas con cobertura cerrada y forma reescrita: %d de %d"
             % (completas, len(nombres)))
    if not nombres:
        return "NO CUBRE", c
    if completas == len(nombres):
        return "CUBRE", c
    if completas:
        return "A MEDIAS", c
    return "NO CUBRE", c


def s_backlog_con_motivo(D):
    c = []
    dentro = False
    filas = []
    for l in D["ld_ls"]:
        if l.startswith("## EL BACKLOG DOCUMENTADO"):
            dentro = True
            continue
        if dentro and l.startswith("#"):
            break
        if not dentro or not l.startswith("|"):
            continue
        celdas = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(celdas) != 3:
            continue
        if set(celdas[0]) <= set("-: ") or celdas[0].lower() == "grupo":
            continue
        filas.append(celdas)
    sin = [f for f in filas if not f[2].strip()]
    c.append("LA SEDE ES LA SECCION DE LA PAGINA QUE LA PROPIA CLAUSULA "
             "NOMBRA: EL BACKLOG DOCUMENTADO, con su motivo.")
    c.append("CIFRA grupos del backlog leidos de esa tabla: %d" % len(filas))
    for f in filas:
        c.append("   GRUPO> %-46s | pares %-6s | motivo escrito: %s"
                 % (f[0][:46], f[1][:6], "SI" if f[2].strip() else "NO"))
    c.append("CIFRA grupos SIN motivo escrito: %d" % len(sin))
    if not sin:
        c.append("   (la busqueda de los que faltan da CERO, y ese cero es el "
                 "resultado)")
    if not filas:
        return "NO CUBRE", c
    return ("CUBRE" if not sin else "NO CUBRE"), c


def s_par_interno_sin_veredicto(D):
    c = []
    universo = [e for e in D["inv"] if e.get("tipo") in ("acto", "racimo")]
    con_patron, en_cola = [], []
    for e in universo:
        m = COBERTURA.search(str(e.get("cobertura") or ""))
        if not m:
            continue
        con_patron.append(e)
        if int(m.group(3)) > 0:
            en_cola.append((e.get("nombre"), m.group(0)))
    c.append("LA VARA LA FIJA LA CORRECCION DECLARADA DE ESTA MISMA FICHA: un "
             "par SIN LEER es el que esta EN COLA Y SIN VEREDICTO, y el "
             "recomputo lo cuenta APARTE de fuera_de_cola. Un par que nunca "
             "entro a la cola no es lectura pendiente: es propuesta que la "
             "semejanza nunca hizo.")
    c.append("CIFRA nominas de tipo acto mas racimo: %d" % len(universo))
    c.append("CIFRA de esas con cobertura contada en el formato del recomputo: "
             "%d" % len(con_patron))
    c.append("CIFRA nominas con pares EN COLA y sin leer: %d" % len(en_cola))
    for n, t in en_cola[:5]:
        c.append("   EN COLA> %s | %s" % (str(n)[:60], t))
    if not en_cola:
        c.append("   (la busqueda da CERO, y ese cero es el resultado)")
    if not con_patron:
        return "NO CUBRE", c
    return ("CUBRE" if not en_cola else "NO CUBRE"), c


def s_lecturas_dirigidas_fuera(D):
    c = []
    caen = _apariciones(D, D["ld_pares"])
    nuevas = [x for x in caen if not x[4]]
    esc = escrituras_declaradas(D, "OP-L-03")
    puestos = D["puestos"]
    huecos = (max(puestos) - len(set(puestos))) if puestos else -1
    c.append("LA CLAUSULA TIENE DOS MITADES Y LAS DOS SE MIDEN, cada una con "
             "su busqueda corrida.")
    c.append("MITAD 1, NO ENTRAN EN LA COLA. CIFRA cabeceras LD hoy: %d | "
             "CIFRA de esas con fila en el archivo: %d"
             % (len(D["ld_pares"]), len(caen)))
    for n, a, b, puesto, rel in caen:
        c.append("   CON FILA> %s (%s contra %s) en el puesto %s | su fila la "
                 "NOMBRA como relectura de un puesto ya existente: %s"
                 % (n, a, b, puesto, "SI" if rel else "NO"))
    c.append("CIFRA lecturas dirigidas que CREARON puesto nuevo en la cola, "
             "que es lo que la clausula prohibe: %d" % len(nuevas))
    if not nuevas:
        c.append("   (la busqueda da CERO, y ese cero es el resultado: la que "
                 "tiene fila la tiene por RELECTURA de un puesto que el "
                 "cribado ya habia abierto, y su propia razon la nombra)")
    c.append("MITAD 2, NO MUEVEN SU MARCADOR. CIFRA marcador contado hoy: %d | "
             "CIFRA puestos distintos: %d | CIFRA puesto maximo: %s | CIFRA "
             "huecos: %d" % (D["n_ver"], len(set(puestos)),
                             max(puestos) if puestos else "n/d", huecos))
    c.append("CIFRA escrituras declaradas de OP-L-03 en nodos, preservar, "
             "eliminar y aristas_nuevas: %d" % esc)
    c.append("LA CIFRA 55 DE LA CLAUSULA ES LA DE SU CORTE (11 ago 2026) Y NO "
             "LA DE HOY, y se dice en vez de callarlo.")
    return ("CUBRE" if (not nuevas and esc == 0 and huecos == 0) else "NO CUBRE"), c


def s_actos_con_forma_y_cobertura(D):
    c = []
    universo = [e for e in D["inv"]
                if "OP-L-03" in (e.get("operaciones") or [])]
    sin = [e for e in universo
           if not str(e.get("forma") or "").strip()
           or not str(e.get("cobertura") or "").strip()]
    c.append("EL SUJETO SE MIDE Y NO SE SUPONE: son las entradas del "
             "inventario que nombran OP-L-03 en su campo de operaciones.")
    c.append("CIFRA entradas que nombran OP-L-03: %d" % len(universo))
    c.append("CIFRA de esas SIN forma escrita o SIN cobertura al lado: %d"
             % len(sin))
    for e in sin[:5]:
        c.append("   SIN FORMA O SIN COBERTURA> %s" % str(e.get("nombre"))[:70])
    if not sin:
        c.append("   (la busqueda de las que faltan da CERO, y ese cero es el "
                 "resultado)")
    if not universo:
        return "NO CUBRE", c
    return ("CUBRE" if not sin else "NO CUBRE"), c


def s_fecha_corte(D):
    c = []
    sin = [e for e in D["inv"] if not str(e.get("fecha_corte") or "").strip()]
    c.append("CIFRA entradas de docs/plan/INVENTARIO.jsonl: %d" % len(D["inv"]))
    c.append("CIFRA entradas SIN fecha_corte: %d" % len(sin))
    for e in sin[:5]:
        c.append("   SIN FECHA> %s" % str(e.get("nombre"))[:70])
    if not sin:
        c.append("   (la busqueda de las que faltan da CERO, y ese cero es el "
                 "resultado)")
    return ("CUBRE" if not sin else "NO CUBRE"), c


def s_provisional(D):
    c = []
    incompletas, sin_marca = [], []
    for e in D["inv"]:
        m = COBERTURA.search(str(e.get("cobertura") or ""))
        if not m:
            continue
        if int(m.group(1)) >= int(m.group(2)):
            continue
        incompletas.append(e)
        if "PROVISIONAL" not in json.dumps(e, ensure_ascii=False).upper():
            sin_marca.append(e)
    c.append("LA COBERTURA INCOMPLETA SE MIDE DEL PROPIO CAMPO Y NO SE OPINA: "
             "es la que dice X de Y pares leidos con X menor que Y.")
    c.append("CIFRA entradas con cobertura contada en ese formato: %d"
             % sum(1 for e in D["inv"]
                   if COBERTURA.search(str(e.get("cobertura") or ""))))
    c.append("CIFRA entradas con cobertura INCOMPLETA: %d" % len(incompletas))
    c.append("CIFRA de esas SIN marca PROVISIONAL: %d" % len(sin_marca))
    for e in sin_marca[:5]:
        c.append("   SIN PROVISIONAL> %s" % str(e.get("nombre"))[:70])
    if not sin_marca:
        c.append("   (la busqueda de las que faltan da CERO, y ese cero es el "
                 "resultado)")
    if not incompletas:
        return "NO CUBRE", c
    return ("CUBRE" if not sin_marca else "NO CUBRE"), c


def s_hueco_nombrado(D):
    c = []
    campos = 0
    rellenos, vacios, descartados = [], [], []
    for i, e in enumerate(D["inv"], start=1):
        for campo, valor in e.items():
            if not isinstance(valor, str):
                continue
            campos += 1
            if es_vacio(valor):
                vacios.append((i, campo))
            elif es_relleno(valor):
                if es_del_vocabulario(D["inv"], campo, valor):
                    descartados.append((i, campo, valor))
                else:
                    rellenos.append((i, campo, valor))
    c.append("EL VOCABULARIO DE RELLENO Y SU REGLA DE DESCARTE SE IMPORTAN DE "
             "_v215_t4_dos_puntos.py, donde nacieron con su correccion "
             "declarada dentro. El campo se compara ENTERO, nunca por "
             "subcadena.")
    c.append("CIFRA entradas examinadas: %d" % len(D["inv"]))
    c.append("CIFRA campos de texto examinados: %d" % campos)
    c.append("CIFRA campos SOSPECHOSOS descartados porque el campo los usa "
             "como estado: %d" % len(descartados))
    c.append("CIFRA campos RELLENADOS de verdad: %d" % len(rellenos))
    c.append("CIFRA campos VACIOS, que no estan nombrados ni rellenados: %d"
             % len(vacios))
    if not rellenos and not vacios:
        c.append("   (las dos busquedas dan CERO, y ese cero es el resultado)")
    return ("CUBRE" if not rellenos and not vacios else "NO CUBRE"), c


def s_disparador(D):
    c = []
    c.append("LA BUSQUEDA, CON SU COMANDO ESCRITO ANTES DE SU RESULTADO: se "
             "recorre TODO el arbol de scripts y por cada fichero .py se "
             "pregunta si NOMBRA la vista humana y si ADEMAS la ESCRIBE, con "
             "una apertura en modo escritura o una llamada de escritura en la "
             "misma linea o en las tres siguientes.")
    c.append("CIFRA ficheros .py que NOMBRAN la vista humana: %d"
             % len(D["py_nombran"]))
    c.append("CIFRA ficheros .py que la ESCRIBEN: %d" % len(D["py_escriben"]))
    for f in D["py_escriben"][:5]:
        c.append("   ESCRIBE> %s" % f)
    if not D["py_escriben"]:
        c.append("   (ninguno: la busqueda da CERO, y ese cero es el "
                 "resultado. La sede que regeneraria la vista humana NO EXISTE "
                 "en el repo)")
    c.append("LA MITAD QUE SI: el fichero fuente esta recomputado, con %d "
             "entradas al corte del marcador de hoy." % len(D["inv"]))
    c.append("LA MITAD QUE FALTA: regenerar la vista humana, y no tiene "
             "instrumento que la haga.")
    if D["py_escriben"]:
        return "CUBRE", c
    return "A MEDIAS", c


SONDAS = {
    ("OP-V-01", 8): s_transversal,
    ("OP-L-01", 0): s_once_no_aparecen,
    ("OP-L-01", 1): s_marcador_l01,
    ("OP-L-01", 2): s_nominas_con_cobertura,
    ("OP-L-02", 0): s_tres_nominas,
    ("OP-L-02", 1): s_marcador_l02,
    ("OP-L-02", 2): s_backlog_con_motivo,
    ("OP-L-03", 0): s_par_interno_sin_veredicto,
    ("OP-L-03", 1): s_lecturas_dirigidas_fuera,
    ("OP-L-03", 2): s_actos_con_forma_y_cobertura,
    ("OP-I-01", 0): s_fecha_corte,
    ("OP-I-01", 1): s_provisional,
    ("OP-I-01", 2): s_hueco_nombrado,
    ("OP-I-01", 3): s_disparador,
}


# ---------------------------------------------------------------------------
# (d) LOS MUTANTES. SE FABRICAN EN MEMORIA Y NO TOCAN NINGUNA FICHA.
# ---------------------------------------------------------------------------

def _rompe_transversal(D):
    D["ck_existe"] = False
    D["ck_ls"] = []
    D["ck_bytes"] = 0
    D["commit_ls"] = []
    return D


def _rompe_ld_en_archivo(D):
    """UNA DE LAS ONCE ENTRA A LA COLA CON PUESTO PROPIO Y SIN SER RELECTURA.
    La fila se fabrica EN MEMORIA y no se escribe en ningun fichero."""
    if D["las_once"]:
        n, a, b = D["las_once"][0]
        D["ver_por_par"][frozenset((a, b))] = {
            "puesto_intra": max(D["puestos"]) + 1, "nodo_a": a, "nodo_b": b,
            "clase": "D", "razon": "fabricada en memoria para el mutante"}
        D["puestos"] = D["puestos"] + [max(D["puestos"]) + 1]
        D["n_ver"] = D["n_ver"] + 1
    return D


def _rompe_marcador(ficha):
    def f(D):
        D["ops"][ficha][1]["nodos"] = ["un_nodo_que_no_existe"]
        return D
    return f


def _rompe_cobertura(D):
    for e in D["inv"]:
        if e.get("tipo") in ("acto", "racimo"):
            e["cobertura"] = ""
            break
    return D


def _rompe_tres_nominas(D):
    """LAS TRES NOMINAS DEJAN SU COBERTURA ABIERTA Y PIERDEN SU FORMA VIEJA."""
    for e in D["inv"]:
        n = str(e.get("nombre", "")).lower()
        if ("cuadrante" in n or "ecuacion de valor" in n
                or "supervision de la ia" in n):
            e["cobertura"] = "1 de 99 pares leidos; 0 en cola; 98 fuera de cola"
            e["forma"] = ""
            e["nota"] = "1 leidos y 9 SIN veredicto"
    return D


def _rompe_backlog(D):
    fuera, dentro = [], False
    for l in D["ld_ls"]:
        if l.startswith("## EL BACKLOG DOCUMENTADO"):
            dentro = True
        elif dentro and l.startswith("#"):
            dentro = False
        if dentro and l.startswith("| **esperan"):
            celdas = l.strip().strip("|").split("|")
            l = "|" + celdas[0] + "|" + celdas[1] + "|   |"
        fuera.append(l)
    D["ld_ls"] = fuera
    return D


def _rompe_en_cola(D):
    for e in D["inv"]:
        if COBERTURA.search(str(e.get("cobertura") or "")):
            e["cobertura"] = "1 de 3 pares leidos; 2 en cola; 0 fuera de cola"
            break
    return D


def _rompe_forma_l03(D):
    for e in D["inv"]:
        if "OP-L-03" in (e.get("operaciones") or []):
            e["forma"] = ""
            break
    return D


def _rompe_fecha(D):
    D["inv"][0]["fecha_corte"] = ""
    return D


def _rompe_provisional(D):
    for e in D["inv"]:
        m = COBERTURA.search(str(e.get("cobertura") or ""))
        if m and int(m.group(1)) < int(m.group(2)):
            for k, v in list(e.items()):
                if isinstance(v, str) and "PROVISIONAL" in v.upper():
                    e[k] = v.upper().replace("PROVISIONAL", "SIN MARCA")
            break
    return D


def _rompe_hueco(D):
    D["inv"][0]["forma"] = "TBD"
    return D


def _sana_disparador(D):
    D["py_escriben"] = ["scripts/inventado_que_no_existe.py"]
    return D


def _rompe_disparador(D):
    D["py_escriben"] = []
    return D


MUTANTES_ROTOS = {
    ("OP-V-01", 8): ("la corrida K desaparece y el commit se queda mudo",
                     _rompe_transversal),
    ("OP-L-01", 0): ("una lectura dirigida SI aparece en el archivo",
                     _rompe_ld_en_archivo),
    ("OP-L-01", 1): ("la ficha declara una escritura de nodo",
                     _rompe_marcador("OP-L-01")),
    ("OP-L-01", 2): ("una nomina se queda sin cobertura al lado",
                     _rompe_cobertura),
    ("OP-L-02", 0): ("las dos nominas que hoy calzan dejan de calzar",
                     _rompe_tres_nominas),
    ("OP-L-02", 1): ("la ficha declara una escritura de nodo",
                     _rompe_marcador("OP-L-02")),
    ("OP-L-02", 2): ("un grupo del backlog se queda sin motivo",
                     _rompe_backlog),
    ("OP-L-03", 0): ("una nomina se queda con pares EN COLA sin leer",
                     _rompe_en_cola),
    ("OP-L-03", 1): ("una lectura dirigida SI aparece en el archivo",
                     _rompe_ld_en_archivo),
    ("OP-L-03", 2): ("un acto de OP-L-03 se queda sin forma",
                     _rompe_forma_l03),
    ("OP-I-01", 0): ("una entrada se queda sin fecha_corte", _rompe_fecha),
    ("OP-I-01", 1): ("una incompleta pierde su marca PROVISIONAL",
                     _rompe_provisional),
    ("OP-I-01", 2): ("un campo se rellena con una palabra del vocabulario",
                     _rompe_hueco),
    ("OP-I-01", 3): ("no hay instrumento que escriba la vista humana",
                     _rompe_disparador),
}

# LOS MUTANTES SANOS SOLO SE FABRICAN PARA LAS SONDAS QUE HOY NO DAN CUBRE.
# Sin ellos, una sonda que siempre dice NO CUBRE seria una constante, y una
# constante no es una medicion (EJECUTOR.md 1, el caso rojo se prueba por
# mutacion, y su reverso: un caso que no puede salir bien no prueba nada).
MUTANTES_SANOS = {
    ("OP-I-01", 3): ("aparece un instrumento que escribe la vista humana",
                     _sana_disparador),
}


def main():
    sha_antes = sha(EXPEDIENTE)
    print("=" * 78)
    print("VUELTA 216, TAREA 2. LA RE-MEDICION QUE EL FUNDADOR ORDENO")
    print("=" * 78)
    print("SHA256 LF DE docs/plan/OPERACIONES.jsonl AL ENTRAR: %s" % sha_antes)
    print("")
    fallos = 0

    print("=" * 78)
    print("2.a. LAS CATORCE FILAS, SACADAS CON UN INSTRUMENTO Y NO A MANO")
    print("=" * 78)
    ls_vara = lineas(VARA)
    filas = filas_de_derivacion(ls_vara)
    print("CIFRA lineas de docs/plan/08_VERIFICACION.md: %d" % len(ls_vara))
    print("CIFRA FILAS ARMADAS LEYENDO ESA TABLA: %d | CIFRA FILAS QUE DEBERIA "
          "HABER: 14" % len(filas))
    if len(filas) != 14:
        print("ROJO Y PARADA: el instrumento no saca CATORCE filas.")
        return 1
    D = cargar()
    print("")
    print("EL COTEJO DE CADA FILA CONTRA SU SEDE, VERBATIM Y POR SU INDICE:")
    descuadres = 0
    for k, f in enumerate(filas, start=1):
        ficha = D["ops"].get(f["ficha"])
        if ficha is None:
            print("FILA %2d | %s | LA FICHA NO EXISTE EN EL EXPEDIENTE" % (k, f["ficha"]))
            descuadres += 1
            continue
        n_exp, d = ficha
        cl = (d.get("verificacion") or [])
        real = cl[f["indice"]] if f["indice"] < len(cl) else None
        calza_linea = (n_exp == f["linea_exp"])
        calza_texto = (real == f["clausula"])
        print("FILA %2d | %-8s | indice %d | linea %d (leida %d: %s) | "
              "VERBATIM CALZA: %s"
              % (k, f["ficha"], f["indice"], f["linea_exp"], n_exp,
                 "SI" if calza_linea else "NO",
                 "SI" if calza_texto else "NO"))
        print("        clausula: %s" % f["clausula"][:150])
        print("        corregida por: %s" % f["corregida_por"])
        if not calza_linea or not calza_texto:
            descuadres += 1
            if real is not None:
                print("        EN EL EXPEDIENTE DICE: %s" % real[:150])
    print("")
    print("CIFRA filas que NO calzan con su sede: %d (se exigen 0)" % descuadres)
    if descuadres:
        fallos += 1
    corr = sum(1 for f in filas if f["corregida_por"] != "no")
    print("CIFRA filas que la tabla declara CORREGIDAS por una correccion "
          "declarada: %d | CIFRA sin correccion: %d" % (corr, len(filas) - corr))
    print("LAS CORRECCIONES DECLARADAS NO SON CLAUSULAS DE LA VARA Y NO ENTRAN "
          "COMO FILAS (registro R.72 del acta 208). SI SE LEEN, porque la "
          "propia tabla dice cual corrige cual, y una clausula corregida se "
          "mide POR SU LECTURA CORREGIDA.")
    print("")

    print("=" * 78)
    print("2.b Y 2.c. LAS CATORCE, MEDIDAS UNA POR UNA, CON SU BUSQUEDA CORRIDA")
    print("=" * 78)
    resultados = []
    for k, f in enumerate(filas, start=1):
        clave = (f["ficha"], f["indice"])
        sonda = SONDAS.get(clave)
        print("")
        print("-" * 78)
        print("CLAUSULA %2d de 14 | ficha %s | indice %d | linea %d de "
              "docs/plan/OPERACIONES.jsonl"
              % (k, f["ficha"], f["indice"], f["linea_exp"]))
        print("   VERBATIM: %s" % f["clausula"])
        print("-" * 78)
        if sonda is None:
            print("ROJO: no hay sonda para esta clausula.")
            fallos += 1
            resultados.append((f, "SIN SONDA"))
            continue
        veredicto, cifras = sonda(D)
        for l in cifras:
            print("   " + l)
        print("   VEREDICTO MEDIDO HOY: **%s**" % veredicto)
        resultados.append((f, veredicto))
    print("")

    print("=" * 78)
    print("2.d. EL CASO ROJO NO SE PROMETE, SE PRUEBA POR MUTACION")
    print("=" * 78)
    print("EL MUTANTE SE FABRICA EN MEMORIA SOBRE UNA COPIA PROFUNDA DE LOS "
          "DATOS Y NO SE ESCRIBE EN NINGUNA FICHA.")
    print("")
    caen = 0
    for k, f in enumerate(filas, start=1):
        clave = (f["ficha"], f["indice"])
        nombre, romper = MUTANTES_ROTOS[clave]
        Dm = romper(copy.deepcopy(D))
        v, _ = SONDAS[clave](Dm)
        cae = (v != "CUBRE")
        caen += 1 if cae else 0
        print("MUTANTE ROTO %2d | %-8s idx %d | %-52s | veredicto %-9s | "
              "CAE: %s" % (k, f["ficha"], f["indice"], nombre[:52], v,
                           "SI" if cae else "NO"))
    print("")
    print("CIFRA mutantes rotos: %d | CIFRA que CAEN (o sea que NO dicen "
          "CUBRE): %d" % (len(filas), caen))
    if caen != len(filas):
        print("ROJO: alguna sonda dice CUBRE sobre datos rotos.")
        fallos += 1
    print("")
    print("Y EL REVERSO, PORQUE UNA SONDA QUE NUNCA PUEDE DECIR CUBRE TAMPOCO "
          "MIDE: las que hoy NO dan CUBRE se prueban tambien con un mutante "
          "SANO, y tienen que SUBIR.")
    suben = 0
    for clave, (nombre, sanar) in MUTANTES_SANOS.items():
        Dm = sanar(copy.deepcopy(D))
        v, _ = SONDAS[clave](Dm)
        sube = (v == "CUBRE")
        suben += 1 if sube else 0
        print("MUTANTE SANO    | %-8s idx %d | %-52s | veredicto %-9s | "
              "SUBE: %s" % (clave[0], clave[1], nombre[:52], v,
                            "SI" if sube else "NO"))
    print("CIFRA mutantes sanos: %d | CIFRA que SUBEN a CUBRE: %d"
          % (len(MUTANTES_SANOS), suben))
    if suben != len(MUTANTES_SANOS):
        print("ROJO: alguna sonda no puede decir CUBRE ni con datos sanos.")
        fallos += 1
    no_cubren = [c for _, c in resultados if c != "CUBRE"]
    print("CIFRA clausulas que hoy NO dan CUBRE: %d | CIFRA de esas con "
          "mutante sano probado: %d" % (len(no_cubren), len(MUTANTES_SANOS)))
    if len(no_cubren) != len(MUTANTES_SANOS):
        print("AVISO: no todas las que no dan CUBRE tienen mutante sano, y se "
              "dice en vez de callarlo.")
    print("")

    print("=" * 78)
    print("EL REPARTO, CONTADO DE LO DE ARRIBA Y NO TECLEADO")
    print("=" * 78)
    print("| clausula | ficha | indice | linea del expediente | veredicto |")
    print("|---:|---|---:|---:|---|")
    for k, (f, v) in enumerate(resultados, start=1):
        print("| %d | %s | %d | %d | %s |"
              % (k, f["ficha"], f["indice"], f["linea_exp"], v))
    for etiqueta in ("CUBRE", "A MEDIAS", "NO CUBRE", "SIN SONDA"):
        n = sum(1 for _, v in resultados if v == etiqueta)
        print("CIFRA clausulas en %s: %d" % (etiqueta, n))
    print("CIFRA clausulas medidas: %d | CIFRA que deberia haber: 14"
          % len(resultados))
    if len(resultados) != 14:
        fallos += 1
    print("")

    print("=" * 78)
    print("LA GUARDA: QUE ESTA TAREA NO MOVIO NI UN CAMPO DE ESTADO")
    print("=" * 78)
    sha_despues = sha(EXPEDIENTE)
    print("SHA256 LF DE docs/plan/OPERACIONES.jsonl AL SALIR: %s" % sha_despues)
    print("CIFRA los dos sha256 CALZAN: %s (se exige SI)"
          % ("SI" if sha_antes == sha_despues else "NO"))
    if sha_antes != sha_despues:
        fallos += 1
    for rel in ("docs/plan/OPERACIONES.jsonl", "docs/plan/INVENTARIO.jsonl",
                "docs/plan/08_VERIFICACION.md",
                "docs/plan/LECTURAS_DIRIGIDAS.md"):
        _, ns = git(["diff", "--numstat", "--", rel])
        n = len([x for x in ns.split(NL) if x.strip()])
        print("CIFRA filas de git diff --numstat sobre %s: %d (se exigen 0)"
              % (rel, n))
        if n:
            fallos += 1
    print("")
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    print("VERDE: la re-medicion queda corrida." if not fallos
          else "ROJO: la re-medicion tiene comprobaciones que fallan.")
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
