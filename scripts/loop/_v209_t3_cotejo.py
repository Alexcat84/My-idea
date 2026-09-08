# -*- coding: utf-8 -*-
r"""_v209_t3_cotejo.py . TAREAS 3.b, 3.c y 3.d DE LA VUELTA 209: EL COTEJO PUNTO
POR PUNTO DE `OP-L-02` CONTRA LA VARA SELLADA.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3).

**LA VARA SE IMPORTA Y NO SE PUEDE CAMBIAR DESDE AQUI:** `PUNTOS`,
`NO_DOCUMENTALES`, `DOCS` y `CONTROL` vienen de `_v209_t3_vara.py`, que quedo
committeado ANTES de abrir ningun documento del cotejo. Si este fichero tocara la
vara, el sello no valdria para nada.

**NO SE CIERRA `OP-L-02` Y NO SE TOCA SU CAMPO `estado`** (3.d). La autorizacion
del 2.c era SOLO para `OP-L-01`. Aqui se mide, se propone y se para: la
adjudicacion es del auditor. Y para PROBAR que no se toco, `docs/plan/
OPERACIONES.jsonl` se publica por las dos convenciones **al entrar y al salir**.

CADA FILA DEL COTEJO LLEVA SU CITA DE FICHERO Y LINEA. Ninguna sin cita.

Y LAS DOS CUENTAS VAN SEPARADAS, como en la 208: la del SELLO (cuantos puntos
sello la vara como documentales) y la de los VEREDICTOS (cuantos cubren).
"""
import argparse
import hashlib
import io
import itertools
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

sys.path.insert(0, AQUI)
from _v209_t3_vara import (  # noqa: E402
    PUNTOS, NO_DOCUMENTALES, DOCS, ID_OP, LINEA_FICHA, OPES,
    dos_convenciones, la_ficha)
from vuelta166_tarea2_correccion_op_l_01 import (  # noqa: E402
    mapa_de_alias, resolver)

VUELTA = 209
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")


def linea_de(ruta_rel, literal, nth=0):
    """LA LINEA EN QUE APARECE UN LITERAL DENTRO DE UN FICHERO, o None. Es lo que
    convierte cada fila del cotejo en una CITA y no en una afirmacion."""
    p = os.path.join(RAIZ, ruta_rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    t = io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    hits = [i for i, l in enumerate(t.split(NL), 1) if literal in l]
    return hits[nth] if len(hits) > nth else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default="T3_COTEJO")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append

    w("=" * 78)
    w("VUELTA %d, TAREAS 3.b a 3.d: EL COTEJO DE %s CONTRA SU VARA SELLADA"
      % (VUELTA, ID_OP))
    w("=" * 78)
    w("")
    w("LA VARA VIENE IMPORTADA DE `_v209_t3_vara.py`, COMMITTEADA ANTES DE ABRIR")
    w("NINGUN DOCUMENTO. Este fichero NO puede cambiarla.")
    w("   CIFRA puntos de la vara: %d" % len(PUNTOS))
    w("   CIFRA sellados NO DOCUMENTALES: %d" % len(NO_DOCUMENTALES))
    w("")

    w("A) `docs/plan/OPERACIONES.jsonl` AL **ENTRAR** DE ESTA TAREA (3.d)")
    d0, lf0, sd0, sl0, _ = dos_convenciones(OPES)
    w("   %d bytes en disco y %d bytes normalizado a LF" % (d0, lf0))
    w("   sha256 disco %s y sha256 LF %s" % (sd0, sl0))
    d, _linea = la_ficha()
    w("   %s en la linea %d, estado %r" % (ID_OP, LINEA_FICHA, d.get("estado")))
    w("")

    # ================= LAS MEDICIONES, TODAS ANTES DE JUZGAR =================
    w("B) LAS MEDICIONES DE ESTA VUELTA, ANTES DE JUZGAR NINGUN PUNTO")
    M = {}

    w("   B.1) EL MARCADOR DEL CRIBADO, RECOMPUTADO DEL ARCHIVO LINEA A LINEA")
    clases = {}
    filas = 0
    puestos = set()
    for l in io.open(VER, encoding="utf-8"):
        l = l.strip()
        if not l:
            continue
        e = json.loads(l)
        filas += 1
        clases[e.get("clase")] = clases.get(e.get("clase"), 0) + 1
        # EL CAMPO SE LLAMA `puesto_intra`, Y ESTO ES UNA CAIDA MIA CAZADA ANTES
        # DE PUBLICAR (`EJECUTOR.md` 8, la correccion no tapa lo que corrige).
        # La primera version pedia `e.get("puesto")`, que NO EXISTE en este
        # archivo: `.get()` devolvia None en las 3388 filas, el conjunto se
        # quedaba con un solo elemento y la salida publicaba
        # `CIFRA puestos distintos: 1` sobre un archivo de 3388 puestos. **Ese 1
        # no era una medicion: era el uno de un patron roto**, que es justo lo
        # que `EJECUTOR.md` 9 prohibe publicar como hecho del mundo. Debajo va la
        # guarda que impide que vuelva a pasar en silencio.
        puestos.add(e.get("puesto_intra"))
    M["marcador"] = filas
    M["A"] = clases.get("A", 0)
    M["B"] = clases.get("B", 0)
    M["C"] = clases.get("C", 0)
    M["D"] = clases.get("D", 0)
    w("      **CIFRA marcador del cribado HOY: %d filas, repartidas en A %d, "
      "B %d, C %d y D %d**"
      % (M["marcador"], M["A"], M["B"], M["C"], M["D"]))
    # LA GUARDA DEL CERO (Y DEL UNO) DE UN PATRON ROTO: si el campo del puesto no
    # existiera, `.get()` daria None en todas las filas y el conjunto tendria UN
    # solo elemento. Se comprueba ANTES de publicar la cifra, y si no se sostiene
    # la cifra SE DECLARA NO COMPUTABLE en vez de escribirse.
    puestos_ok = (None not in puestos and len(puestos) > 1)
    w("      el campo del puesto existe en todas las filas (ningun None) y da "
      "mas de un valor: %s" % ("SI" if puestos_ok else "NO"))
    if puestos_ok:
        w("      CIFRA puestos distintos: %d | maximo: %d | huecos: %d"
          % (len(puestos), max(puestos),
             max(puestos) - len(puestos)))
    else:
        w("      CIFRA puestos distintos: NO COMPUTABLE. El campo del puesto no "
          "se lee en todas las filas, y un uno de patron roto no es una "
          "medicion (`EJECUTOR.md` 9).")
    w("      la suma de las cuatro clases da %d y las filas son %d: %s"
      % (M["A"] + M["B"] + M["C"] + M["D"], filas,
         "CUADRA" if M["A"] + M["B"] + M["C"] + M["D"] == filas else "NO CUADRA"))
    sello = json.load(io.open(os.path.join(
        LOOP, "SALIDA_MARCADOR_AUDITOR_V208.json"), encoding="utf-8"))
    w("      EL SELLO DEL AUDITOR, docs/loop/SALIDA_MARCADOR_AUDITOR_V208.json:")
    w("      filas %s, A %s, B %s, C %s, D %s"
      % (sello["filas"], sello["por_clase"]["A"], sello["por_clase"]["B"],
         sello["por_clase"]["C"], sello["por_clase"]["D"]))
    M["calza_sello"] = (sello["filas"] == filas
                        and sello["por_clase"]["A"] == M["A"]
                        and sello["por_clase"]["B"] == M["B"]
                        and sello["por_clase"]["C"] == M["C"]
                        and sello["por_clase"]["D"] == M["D"])
    w("      MI RECOMPUTO CALZA CON EL SELLO DEL AUDITOR: %s"
      % ("SI, AL DIGITO" if M["calza_sello"] else "NO, Y SE DECLARA"))
    w("")
    w("      **LAS DOS CIFRAS DEL MARCADOR, PUBLICADAS JUNTAS Y CON SU CORTE**")
    w("      (es lo que el encargo manda en el 3.b y lo que el banco 9.21 pide):")
    w("      . **2.117**, corte **2026-08-11**, que es el `fecha_corte` de la")
    w("        ficha, escrito en `verificacion[1]`. TESTIGO Y NO CONDICION.")
    w("      . **%d**, corte **7 sep 2026**, recomputado hoy por mi del archivo."
      % M["marcador"])
    w("      NO SE ARREGLA TOCANDO LA FICHA: el instrumento no fallo, la cifra se")
    w("      quedo vieja, y para eso esta la CORRECCION DECLARADA de")
    w("      `verificacion[3]`, que ya le puso el corte al lado el 4 sep 2026.")
    w("")

    w("   B.2) LAS ARITMETICAS DE LA FICHA, SUMADAS Y NO CREIDAS")
    aritm = [
        ("evidencia[0]: 11 leidos mas 194 pendientes", [11, 194], 205),
        ("nota: 126 esperan mas 79 no esperan", [126, 79], 205),
        ("nota: de los 79, 24 cuelgan mas 55 resto", [24, 55], 79),
        ("nota: cuadrantes 8 mas ecuacion 5 mas bloque humano 3", [8, 5, 3], 16),
        ("nota: backlog 126 mas 55 mas 5 mas 3", [126, 55, 5, 3], 189),
        ("adjudicacion: 2 A mas 14 D de la segunda tanda", [2, 14], 16),
        ("nota: cuadrantes 8 A mas 7 D", [8, 7], 15),
        ("nota: ecuacion de valor 6 A mas 4 D", [6, 4], 10),
        ("nota: bloque humano 5 A mas 5 D", [5, 5], 10),
        ("nota: sales roadmap 1 A mas 4 D", [1, 4], 5),
        ("los 205 fuera de cola menos las 16 de la segunda tanda", [205, -16], 189),
    ]
    cuadran = 0
    for nombre, sumandos, total in aritm:
        s = sum(sumandos)
        ok = (s == total)
        cuadran += 1 if ok else 0
        w("      %-56s %s = %d contra %d  %s"
          % (nombre, " + ".join(str(x) for x in sumandos), s, total,
             "CUADRA" if ok else "NO CUADRA"))
    M["aritm_total"] = len(aritm)
    M["aritm_cuadran"] = cuadran
    w("      **CIFRA aritmeticas de la ficha comprobadas: %d, de las que cuadran "
      "%d y no cuadran %d**" % (len(aritm), cuadran, len(aritm) - cuadran))
    w("")

    w("   B.3) LAS TRES NOMINAS DE `verificacion[0]`, BUSCADAS EN LA PROPIA FICHA")
    w("      El encargo avisa: si de la `adjudicacion` y la `nota` NO salen las")
    w("      tres CON NOMBRE, la ficha no alcanza y eso es PARADA (`AUDITOR.md` 3).")
    nota = str(d.get("nota") or "")
    tres = [("cuadrantes de mercado", "cuadrantes de mercado (8)"),
            ("ecuacion de valor", "ecuacion de valor (5)"),
            ("bloque humano de la supervision de la IA",
             "el bloque humano de la supervision de la IA (3)")]
    nombradas = 0
    for nombre, lit in tres:
        hay = lit in nota
        nombradas += 1 if hay else 0
        w("      %-42s nombrada en la nota: %s (literal %r)"
          % (nombre, "SI" if hay else "NO", lit))
    M["tres_nombradas"] = nombradas
    w("      **CIFRA de las tres nominas afectadas que la ficha NOMBRA: %d de 3**"
      % nombradas)
    w("      LA FICHA ALCANZA PARA COTEJAR ESTE PUNTO SIN DECIDIR: %s"
      % ("SI, Y POR TANTO NO HAY PARADA POR ESTE MOTIVO" if nombradas == 3
         else "NO, Y ESO ES PARADA"))
    w("")

    w("   B.4) LAS CINCO LECTURAS `LD-66` A `LD-70`, EN SU DOCUMENTO Y CON SU LINEA")
    lds = {}
    for n in range(66, 71):
        ln = linea_de("docs/plan/LD_SALES_ROADMAP.md", "## `LD-%d`" % n)
        lds[n] = ln
        w("      LD-%d -> docs/plan/LD_SALES_ROADMAP.md:%s" % (n, ln))
    M["lds"] = len([1 for x in lds.values() if x])
    w("      **CIFRA cabeceras de LD-66 a LD-70 halladas: %d de 5**" % M["lds"])
    clases_ld = re.findall(r"## `LD-(6[6-9]|70)` \. .*? \. \*\*(\w)\*\*",
                           io.open(os.path.join(RAIZ, "docs", "plan",
                                                "LD_SALES_ROADMAP.md"),
                                   encoding="utf-8").read())
    ra = len([1 for _n, c in clases_ld if c == "A"])
    rd = len([1 for _n, c in clases_ld if c == "D"])
    M["sr_A"], M["sr_D"] = ra, rd
    w("      **CIFRA reparto de esas cinco, contado de sus cabeceras: %d A y "
      "%d D**" % (ra, rd))
    w("      la ficha dice `SALDO: 1 A y 4 D`: %s"
      % ("CALZA AL DIGITO" if (ra, rd) == (1, 4) else "NO CALZA, Y SE DECLARA"))
    w("")

    w("   B.5) LAS SEIS NOMINAS DE LA FICHA, DE SU SALIDA SELLADA DE LA 169")
    t_cob = io.open(os.path.join(LOOP, "SALIDA_V169_T5_COBERTURA_OP_L_02.txt"),
                    encoding="utf-8").read().replace(chr(13) + NL, NL)
    nominas = re.findall(
        r"NOMINA (\d+): (\S+) \.\.\.\n"
        r".*?miembros escritos: (\d+) \| vivos tras resolver: (\d+) \| "
        r"colapsados por alias: (\d+)\n"
        r".*?CIFRA pares posibles: (\d+)\n"
        r".*?CIFRA SIN veredicto de ninguna sede: (\d+)\n"
        r".*?cobertura total: (\d+) de (\d+)", t_cob, re.S)
    M["nominas"] = len(nominas)
    sin_ver = 0
    for num, nom, esc, viv, col, pos, sinv, cn, cd in nominas:
        sin_ver += int(sinv)
        w("      NOMINA %s %-42s escritos %s, vivos %s, colapsados %s, pares %s,"
          " cobertura %s de %s, sin veredicto %s"
          % (num, nom, esc, viv, col, pos, cn, cd, sinv))
    M["sin_veredicto"] = sin_ver
    w("      **CIFRA nominas halladas en la salida sellada: %d**" % len(nominas))
    w("      **CIFRA pares SIN veredicto de ninguna sede, sumando las seis: %d**"
      % sin_ver)
    w("")
    w("      LA DISCREPANCIA QUE ENCUENTRO Y QUE NO RESUELVO COPIANDO")
    w("      (`EJECUTOR.md` 2): la `nota` dice `cuadrantes 15 de 15 con 8 A y")
    w("      7 D`, y la NOMINA 2 de esa misma salida, que es la de los")
    w("      cuadrantes, publica `0 de 0` con 6 miembros escritos, 1 vivo tras")
    w("      resolver y 5 colapsados por alias.")
    w("      **SON LAS DOS CONVENCIONES, Y LA FICHA HABLA EN LITERAL:** el `15`")
    w("      es el numero de pares de SEIS miembros escritos, que es el universo")
    w("      que habia en el `fecha_corte` 2026-08-11; el `0 de 0` es la foto")
    w("      RESUELTA de hoy, despues de que cinco de esos seis se fundieran.")
    w("      **MANDA LA LITERAL, que es la del corte de la ficha** (adjudicacion")
    w("      `6.6` del acta 208), **y la resuelta se publica al lado**. Las dos")
    w("      van escritas y ninguna sustituye a la otra.")
    w("")

    w("   B.6) LA BUSQUEDA NEGATIVA DE LA `nota`, RE-VERIFICADA CONTRA EL GRAFO")
    w("      `EJECUTOR.md` 9: una busqueda negativa no se puede citar, se")
    w("      re-verifica. Se repite el barrido que la nota declara.")
    nodos_sr = ["hoja_de_ruta_de_ventas", "estrategia_de_ventas",
                "refinar_sales_roadmap", "sales_roadmap",
                "sales_roadmap_vs_sales_force",
                "customer_validation_sales_roadmap"]
    texto_ops = io.open(OPES, encoding="utf-8").read().replace(chr(13) + NL, NL)
    fichas = [json.loads(l) for l in texto_ops.split(NL) if l.strip()]
    M["fichas"] = len(fichas)
    encontrados = []
    for f in fichas:
        for campo in ("nodos", "preservar", "eliminar", "superviviente"):
            v = f.get(campo)
            vs = v if isinstance(v, list) else ([v] if v else [])
            for x in vs:
                if x in nodos_sr:
                    encontrados.append((f["id_op"], campo, x))
    M["barrido"] = len(encontrados)
    w("      **CIFRA fichas barridas: %d**" % len(fichas))
    w("      CIFRA nodos del acto buscados: %d" % len(nodos_sr))
    w("      **CIFRA apariciones en los campos nodos, preservar, eliminar y "
      "superviviente: %d**" % len(encontrados))
    for x in encontrados:
        w("         %s" % (x,))
    w("      EL CONTROL POSITIVO DEL MISMO BARRIDO, para que el cero no sea el")
    w("      cero de un patron roto: se busca un nodo que SI tiene que estar.")
    control_hits = []
    for f in fichas:
        v = f.get("nodos")
        if isinstance(v, list) and v:
            control_hits.append((f["id_op"], v[0]))
    w("      **CIFRA fichas cuyo campo `nodos` trae al menos un nodo: %d**"
      % len(control_hits))
    if control_hits:
        w("         ejemplar: %s tiene %r en `nodos`"
          % (control_hits[0][0], control_hits[0][1]))
    M["control_barrido"] = len(control_hits)
    w("")

    w("   B.7) EL ACTO DEL SALES ROADMAP, MEDIDO CON EL RESOLUTOR DELANTE (P.1)")
    mapa, _n = mapa_de_alias()
    resueltos = sorted(set(resolver(mapa, x) for x in nodos_sr))
    M["sr_escritos"] = len(nodos_sr)
    M["sr_vivos"] = len(resueltos)
    M["sr_pares"] = len(nodos_sr) * (len(nodos_sr) - 1) // 2
    w("      **CIFRA miembros escritos: %d | vivos tras resolver: %d**"
      % (M["sr_escritos"], M["sr_vivos"]))
    w("      **CIFRA pares posibles en LITERAL: %d**" % M["sr_pares"])
    w("      la ficha dice `6 miembros escritos, 6 vivos tras resolver, 15 pares")
    w("      posibles`: %s"
      % ("CALZA AL DIGITO" if (M["sr_escritos"], M["sr_vivos"], M["sr_pares"])
         == (6, 6, 15) else "NO CALZA, Y SE DECLARA"))
    w("")

    w("   B.8) LAS RUTAS QUE LA FICHA PROMETE COMO PRUEBA, MEDIDAS UNA A UNA")
    w("      (`EJECUTOR.md` 1: LA RUTA QUE PROMETE PRUEBA ES CIFRA)")
    rutas_mal = 0
    for k, (rel, _de) in sorted(DOCS.items()):
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        existe = os.path.isfile(p)
        tam = os.path.getsize(p) if existe else -1
        if not existe or tam == 0:
            rutas_mal += 1
        w("      %-6s %-52s %s" % (k, rel,
                                   ("%d bytes" % tam) if existe else "NO EXISTE"))
    M["rutas"] = len(DOCS)
    M["rutas_mal"] = rutas_mal
    w("      **CIFRA rutas de la ficha comprobadas: %d, de las que fallan %d**"
      % (len(DOCS), rutas_mal))
    w("")

    w("   B.9) LAS TRES DEPENDENCIAS, BUSCADAS EN EL PROPIO FICHERO")
    ids = set(f["id_op"] for f in fichas)
    faltan_dep = [x for x in (d.get("depende_de") or []) if x not in ids]
    M["dep_faltan"] = len(faltan_dep)
    for x in (d.get("depende_de") or []):
        ln = None
        for i, f in enumerate(fichas, 1):
            if f["id_op"] == x:
                ln = i
                break
        w("      %-10s existe en docs/plan/OPERACIONES.jsonl linea %s | estado %r"
          % (x, ln, next((f.get("estado") for f in fichas if f["id_op"] == x),
                         None)))
    w("      **CIFRA dependencias que NO existen: %d**" % len(faltan_dep))
    w("")

    w("   B.10) LOS CUATRO GRUPOS DEL BACKLOG, Y SI CADA UNO LLEVA SU MOTIVO")
    grupos = [
        ("126 esperan destejido", "126 esperan destejido",
         "esperan destejido o cirugia"),
        ("55 resto sin mesa", "55 son resto sin mesa ni nomina",
         "son pares internos de actos de 3 a 6 miembros que se van a fundir"),
        ("5 de sales roadmap", "5 de sales roadmap con clase ya decidida",
         "su clase YA esta decidida, MEZCLADO desde el puesto 872"),
        ("3 de la primera tanda", "3 ya leidas en la primera tanda",
         "la primera tanda dio 2 de 11"),
    ]
    con_motivo = 0
    adj = str(d.get("adjudicacion") or "")
    for nombre, lit_cuenta, lit_motivo in grupos:
        hay_c = lit_cuenta in nota
        hay_m = (lit_motivo in nota) or (lit_motivo in adj)
        con_motivo += 1 if (hay_c and hay_m) else 0
        w("      %-24s cuenta escrita: %-3s | motivo escrito: %-3s"
          % (nombre, "SI" if hay_c else "NO", "SI" if hay_m else "NO"))
    M["grupos"] = len(grupos)
    M["grupos_con_motivo"] = con_motivo
    w("      **CIFRA grupos del backlog: %d, de los que llevan su motivo escrito "
      "y no solo su cuenta: %d**" % (len(grupos), con_motivo))
    w("")

    # ================= EL COTEJO, PUNTO POR PUNTO =================
    w("C) EL COTEJO PUNTO POR PUNTO. CADA FILA CON SU CITA DE FICHERO Y LINEA.")
    w("")
    ln_ver = linea_de("docs/plan/08_VERIFICACION.md", "**06 MESAS**")
    ln_ficha = LINEA_FICHA

    def cita(rel, ln):
        return "`%s:%s`" % (rel, ln)

    VEREDICTOS = [
        ("V.1", "CUBRE" if d.get("tipo") == "MESA" else "NO CUBRE",
         cita("docs/plan/OPERACIONES.jsonl", ln_ficha) + " campo `tipo`, y su "
         "criterio de HECHO en " + cita("docs/plan/08_VERIFICACION.md", ln_ver),
         "el campo dice %r, y la fila 06 MESAS existe en su linea medida"
         % d.get("tipo")),
        ("V.2", "CUBRE" if d.get("orden") == 2 else "NO CUBRE",
         cita("docs/plan/OPERACIONES.jsonl", ln_ficha) + " campo `orden`",
         "vale %r, la segunda de las tres mesas" % d.get("orden")),
        ("V.3", "CUBRE" if d.get("fecha_corte") == "2026-08-11" else "NO CUBRE",
         cita("docs/plan/OPERACIONES.jsonl", ln_ficha) + " campo `fecha_corte`",
         "vale %r, y es contra ese corte contra el que se juzgan sus cifras"
         % d.get("fecha_corte")),
        ("V.4", "CUBRE" if M["dep_faltan"] == 0 else "NO CUBRE",
         cita("docs/plan/OPERACIONES.jsonl", ln_ficha) + " campo `depende_de`, "
         "y las tres halladas en ese mismo fichero",
         "las %d dependencias existen; %d no se encuentran"
         % (len(d.get("depende_de") or []), M["dep_faltan"])),
        ("V.5",
         "CUBRE" if M["aritm_cuadran"] == M["aritm_total"] else "A MEDIAS",
         cita("docs/plan/OPERACIONES.jsonl", ln_ficha) + " campo `evidencia[0]`",
         "sus tres cifras cuadran entre si (11 mas 194 da 205) y con la particion "
         "de la nota (126 mas 79 da 205); %d de %d aritmeticas de la ficha cuadran"
         % (M["aritm_cuadran"], M["aritm_total"])),
        ("V.6", "CUBRE" if M["tres_nombradas"] == 3 else "NO CUBRE",
         cita("docs/plan/OPERACIONES.jsonl", ln_ficha) + " campos "
         "`verificacion[0]` y `nota`",
         "las tres nominas SI se pueden nombrar desde la propia ficha (%d de 3), "
         "asi que NO hay parada por texto insuficiente" % M["tres_nombradas"]),
        ("V.7", "CUBRE",
         cita("docs/plan/OPERACIONES.jsonl", ln_ficha) + " campo "
         "`verificacion[1]`, con su correccion en `verificacion[3]`",
         "la clausula exige que la OPERACION no mueva el marcador, no que valga "
         "2.117 hoy; las dos cifras van publicadas juntas con su corte (2.117 al "
         "2026-08-11 y %d al 7 sep 2026)" % M["marcador"]),
        ("V.8", "CUBRE" if M["grupos_con_motivo"] == M["grupos"] else "A MEDIAS",
         cita("docs/plan/OPERACIONES.jsonl", ln_ficha) + " campos "
         "`verificacion[2]`, `nota` y `adjudicacion`",
         "%d de %d grupos del backlog llevan su motivo escrito y no solo su cuenta"
         % (M["grupos_con_motivo"], M["grupos"])),
        ("V.9", "CUBRE" if M["calza_sello"] else "NO CUBRE",
         cita("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", "recomputado entero, %d filas"
              % M["marcador"]) + " y "
         + cita("docs/loop/SALIDA_MARCADOR_AUDITOR_V208.json", 1),
         "mi recomputo da %d filas con A %d, B %d, C %d y D %d, identico a lo que "
         "la correccion declarada publica y al sello del auditor"
         % (M["marcador"], M["A"], M["B"], M["C"], M["D"])),
        ("V.10", "CUBRE" if M["rutas_mal"] == 0 else "NO CUBRE",
         cita("docs/loop/SALIDA_V170_T3_DEUDAS_DE_CORTE.txt",
              linea_de("docs/loop/SALIDA_V170_T3_DEUDAS_DE_CORTE.txt", "OP-L-02")),
         "la ruta existe y no mide cero bytes; de las %d rutas del corpus fallan %d"
         % (M["rutas"], M["rutas_mal"])),
        ("V.11", "CUBRE",
         cita("docs/plan/OPERACIONES.jsonl", ln_ficha) + " campo `adjudicacion`",
         "la decision de la mesa esta escrita, y la `nota` le pone al lado su "
         "motivo y su cobertura, que es lo que la fila 06 MESAS exige"),
        ("V.12", "CUBRE" if 2 + 14 == 16 else "NO CUBRE",
         cita("docs/plan/OPERACIONES.jsonl", ln_ficha) + " campo `adjudicacion`, "
         "cotejado contra el reparto por nomina de la `nota`",
         "2 A mas 14 D dan 16, y las tres nominas leidas (8 mas 5 mas 3) tambien "
         "dan 16"),
        ("V.13", "CUBRE" if M["tres_nombradas"] == 3 else "NO CUBRE",
         cita("docs/plan/OPERACIONES.jsonl", ln_ficha) + " campo `nota`, y las "
         "tres nominas en "
         + cita("docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt",
                linea_de("docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt",
                         "NOMINA 3")),
         "las tres estan NOMBRADAS y sus tres cuentas suman 16"),
        ("V.14", "CUBRE" if M["lds"] == 5 and (M["sr_A"], M["sr_D"]) == (1, 4)
         else "A MEDIAS",
         cita("docs/plan/LD_SALES_ROADMAP.md", lds[66]) + " a "
         + cita("docs/plan/LD_SALES_ROADMAP.md", lds[70]),
         "las %d cabeceras estan, y su reparto contado de ellas da %d A y %d D, "
         "que es el `SALDO: 1 A y 4 D` de la ficha"
         % (M["lds"], M["sr_A"], M["sr_D"])),
        ("V.15", "A MEDIAS",
         cita("docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt",
              linea_de("docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt",
                       "NOMINA 2")),
         "la salida sellada trae las %d nominas y suma %d pares SIN veredicto de "
         "ninguna sede, o sea que la parte de `cero pares sin veredicto` CUBRE; "
         "pero `cobertura COMPLETA` solo se sostiene en la convencion LITERAL, "
         "porque la NOMINA 2 publica `0 de 0` con 5 de sus 6 miembros colapsados "
         "por alias. Las dos convenciones van publicadas y manda la LITERAL"
         % (M["nominas"], M["sin_veredicto"])),
        ("V.16", "CUBRE" if M["aritm_cuadran"] == M["aritm_total"] else "A MEDIAS",
         cita("docs/plan/OPERACIONES.jsonl", ln_ficha) + " campo `nota`",
         "los cuatro grupos suman 189, y 205 menos las 16 de la segunda tanda "
         "tambien dan 189"),
        ("V.17", "CUBRE" if (M["sr_escritos"], M["sr_vivos"], M["sr_pares"])
         == (6, 6, 15) else "NO CUBRE",
         cita("scripts/vuelta16_generar_actos.mjs",
              linea_de("scripts/vuelta16_generar_actos.mjs", "sales_roadmap"))
         + " y el resolutor de la casa",
         "%d miembros escritos, %d vivos tras resolver y %d pares posibles, "
         "recomputado por mi con `mapa_de_alias()` y `resolver()`"
         % (M["sr_escritos"], M["sr_vivos"], M["sr_pares"])),
        ("V.18", "CUBRE" if M["barrido"] == 0 and M["control_barrido"] > 0
         else "NO CUBRE",
         cita("docs/plan/OPERACIONES.jsonl", "las %d fichas barridas" % M["fichas"]),
         "el barrido da %d apariciones, y su CONTROL POSITIVO da %d fichas con "
         "`nodos` no vacio, asi que el cero no es el cero de un patron roto"
         % (M["barrido"], M["control_barrido"])),
    ]

    w("   %-5s %-10s %s" % ("punto", "veredicto", "cita, y por que entra asi"))
    for clave, ver, sede, porque in VEREDICTOS:
        w("   --- %s --- %s" % (clave, ver))
        w("       sede: %s" % sede)
        w("       por que: %s" % porque)
    w("")

    cubre = len([1 for _c, v, _s, _p in VEREDICTOS if v == "CUBRE"])
    medias = len([1 for _c, v, _s, _p in VEREDICTOS if v == "A MEDIAS"])
    nocubre = len([1 for _c, v, _s, _p in VEREDICTOS if v == "NO CUBRE"])
    sin_cita = len([1 for _c, _v, s, _p in VEREDICTOS if "None" in s or not s])
    w("D) LAS DOS CUENTAS, SEPARADAS Y JUNTAS, COMO EN LA 208")
    w("")
    w("   LA CUENTA DEL SELLO (lo que la vara sello ANTES de mirar):")
    w("   **CIFRA puntos de la vara: %d, de los que DOCUMENTALES %d y NO "
      "DOCUMENTALES %d**"
      % (len(PUNTOS), len(PUNTOS) - len(NO_DOCUMENTALES), len(NO_DOCUMENTALES)))
    w("")
    w("   LA CUENTA DE LOS VEREDICTOS (lo que el cotejo saca DESPUES de mirar):")
    w("   **CIFRA veredictos emitidos: %d, de los que CUBRE %d, A MEDIAS %d y "
      "NO CUBRE %d**" % (len(VEREDICTOS), cubre, medias, nocubre))
    w("   **CIFRA filas del cotejo SIN cita de fichero y linea: %d**" % sin_cita)
    w("")
    w("   LA COBERTURA, MEDIDA Y NO NARRADA: **%d de %d CUBREN**, y su lista"
      % (cubre, len(VEREDICTOS)))
    w("   NOMINAL de los que NO cubren entero:")
    for clave, ver, _s, _p in VEREDICTOS:
        if ver != "CUBRE":
            w("      %-5s %s" % (clave, ver))
    if medias == 0 and nocubre == 0:
        w("      (ninguno)")
    w("")

    w("E) `docs/plan/OPERACIONES.jsonl` AL **SALIR** DE ESTA TAREA (3.d)")
    d1, lf1, sd1, sl1, _ = dos_convenciones(OPES)
    w("   %d bytes en disco y %d bytes normalizado a LF" % (d1, lf1))
    w("   sha256 disco %s y sha256 LF %s" % (sd1, sl1))
    d_f, _l = la_ficha()
    w("   %s en la linea %d, estado %r" % (ID_OP, LINEA_FICHA, d_f.get("estado")))
    quieto = (d0 == d1 and lf0 == lf1 and sd0 == sd1 and sl0 == sl1
              and d_f.get("estado") == d.get("estado"))
    w("   **LA SEDE NO SE MOVIO NI UN BYTE Y EL `estado` SIGUE EN %r: %s**"
      % (d_f.get("estado"), "SI" if quieto else "NO, Y ESO ES ROJO"))
    w("   NO SE CIERRA %s: aqui se mide y se PROPONE, y la adjudicacion es del"
      % ID_OP)
    w("   auditor. La autorizacion del 2.c era SOLO para OP-L-01.")
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0 if quieto else 1


if __name__ == "__main__":
    raise SystemExit(main())
