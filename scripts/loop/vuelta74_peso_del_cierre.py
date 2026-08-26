# -*- coding: utf-8 -*-
"""vuelta74_peso_del_cierre.py . ARMA EL PESO DEL CIERRE DE LA FASE 03, MEDIDO Y
NO DECIDIDO.

SOLO LECTURA, Y ESO ES LA MITAD DE SU CONTRATO. No escribe ni un nodo, ni una
ficha, ni una linea del grafo, ni sienta una mesa, ni funde, ni declara. Imprime.
La parada del 21 ago 2026 dispara cuando la fase 03 quede CERRADA Y VERIFICADA:
esta vuelta ARMA el peso y el auditor de la 74 lo pesa. MEDIR NO ES DECIDIR.

POR QUE NACE. El acta 73, en su seccion 7, nombra el cierre de la fase 03 como lo
unico que queda delante y enumera lo que falta PESAR: el destino de cada ficha de
la fase, los DECLARADOS con su subconjunto, los dos actos con dueno y la mesa
OP-M-03. Esas cuatro cosas se venian afirmando de memoria de una vuelta a otra.
La regla 1 del EJECUTOR (LA CITA LLEVA SU LINEA) y la regla 2 (EL INSTRUMENTO
MANDA) piden que se midan hoy, con su salida guardada, y eso es lo que este
fichero hace.

LOS CINCO BLOQUES, Y LO QUE CADA UNO MIDE:

  1. LAS FICHAS DE LA FASE 03, una a una. Para cada una: id, tipo, estado, sus
     nodos resueltos por P.1 contra el grafo de HOY, cuantos siguen VIVOS, si su
     nota trae una declaracion de CONSUMIDA, sus sedes en docs/plan/03_FUSIONES.md
     y sus commits en git. EL DESTINO SE DERIVA DE LO MEDIDO CON UNA REGLA
     ESCRITA Y UNICA, y la regla va impresa en la salida para que se pueda
     discutir: una ficha cuyos miembros resuelven a UN solo vivo o a ninguno ya
     no tiene fusion que hacer; una con DOS o mas la tiene entera por delante.
     Las que no traen nomina de nodos (los dos abridores de universo) se miden
     por sus REGISTROS, que es donde vive lo que hicieron.

  2. LOS DECLARADOS Y NO FUNDIDOS. La lista NO entra por argumento: se MIDE por
     dos vias que tienen que coincidir, y si no coinciden el instrumento lo dice.
     VIA A, sobre el grafo: actos del tramo fijado con DOS o mas miembros vivos y
     SIN dueno. VIA B, sobre la pagina: actos que tienen al menos una sede con la
     frase DECLARADO Y NO FUNDIDO en la region del tramo unico. Para cada uno se
     imprimen ademas la nomina, los vivos, las PUERTAS medidas contra el universo
     protegido, y el motivo sellado que su sede cita.

  3. LOS ACTOS CON DUENO. Los duenos se re-miden CAMPO A CAMPO sobre las fichas
     (nodos, preservar, eliminar), que es la vara de la adjudicacion 2 del acta
     68, y de cada dueno hallado se lee SU FASE de su propia ficha. Asi la frase
     "su destino vive fuera de la fase 03" deja de ser un recuerdo.

  4. LA MESA. Su ficha se lee ENTERA y se imprimen su fase, su estado, su
     adjudicacion y su bloquea_a. Ni se sienta ni se ejecuta.

  5. EL VEREDICTO MEDIDO. Una tabla de piezas: que le falta a la fase 03 para
     estar CERRADA segun la letra de la parada. NO decide: marca cada pieza como
     LISTA o PENDIENTE con la medicion al lado.

LAS PUERTAS NO SE RE-INVENTAN: SE IMPORTAN. El universo protegido se toma de
scripts/loop/varas_n_arias_del_tramo.py, que es instrumento de nombre estable, en
vez de copiarse aqui. Copiar es lo que protege a los registradores clonados de
vuelta en vuelta (acta 68, D14), pero AQUI el riesgo es el contrario: si este
fichero se hiciera su propia lista de puertas y el otro cambiara la suya, los dos
publicarian puertas distintas EN SILENCIO, que es justo lo que el docstring de
aquel dice querer impedir. Importar hace imposible la divergencia. VA MARCADO
COMO DISCUTIBLE en el reporte.

Uso:
  python scripts/loop/vuelta74_peso_del_cierre.py
      --tramo docs/loop/TRAMO_UNICO_OPU02_V64.jsonl
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
FASE = "03_FUSIONES"
MESA = "OP-M-03"
NL = chr(10)
BT = chr(96)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from varas_n_arias_del_tramo import protegidos  # noqa: E402

# LAS CUATRO ESPECIES DE MOTIVO SELLADO, tal como la pagina las enumera en su
# catalogo (linea de la seccion "EL CATALOGO DE MOTIVOS SELLADOS QUEDA EN
# CUATRO"). Aqui son AGUJAS DE BUSQUEDA sobre la sede, no una tabla de doctrina:
# el instrumento no decide cual aplica, solo dice cual cita la sede.
MOTIVOS = [
    ("P.10", "P.10"),
    ("P.5", "P.5"),
    ("guarda 1B", "1B"),
    ("D directo interno", "directo interno"),
    ("PENDIENTE DE DOCTRINA", "PENDIENTE DE DOCTRINA"),
]


def cargar_grafo():
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    alias = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def resolver(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x

    def vivo(x):
        d = G.get(x)
        return bool(d) and not bool(d.get("deprecado") or d.get("deprecated"))

    return G, resolver, vivo


def fichas():
    d = {}
    for l in io.open(OPS, encoding="utf-8"):
        if l.strip():
            j = json.loads(l)
            d[j["id_op"]] = j
    return d


def git(*args):
    p = subprocess.run(["git"] + list(args), capture_output=True, cwd=RAIZ)
    return p.stdout.decode("utf-8", "replace").rstrip(NL)


def sedes_de(lineas, aguja, desde=0):
    """Lineas de la pagina que nombran la aguja, con su numero de linea 1-based."""
    return [(i + 1, lineas[i]) for i in range(desde, len(lineas)) if aguja in lineas[i]]


def cabecera_que_manda(lineas, n):
    """La cabecera de nivel 2 que gobierna la linea n (1-based)."""
    for i in range(n - 1, -1, -1):
        if lineas[i].startswith("## "):
            return i + 1, lineas[i]
    return 0, ""


def bloque_1(F, resolver, vivo, lineas):
    print("=" * 78)
    print("BLOQUE 1: LAS FICHAS DE LA FASE %s, UNA A UNA, CON SU DESTINO MEDIDO" % FASE)
    print("=" * 78)
    de_fase = [o for o in F.values() if o["fase"] == FASE]
    print()
    print("  fichas de la fase %s en OPERACIONES.jsonl: %d" % (FASE, len(de_fase)))
    print("  LA REGLA DEL DESTINO, ESCRITA ANTES DE APLICARLA Y UNICA PARA LAS %d:" % len(de_fase))
    print("     a) sin nomina de nodos  -> ABRIDOR DE UNIVERSO: su destino son sus REGISTROS")
    print("     b) nomina que resuelve a UN vivo o a ninguno -> SIN FUSION PENDIENTE")
    print("        b.1 con declaracion de CONSUMIDA en su nota -> CONSUMIDA")
    print("        b.2 sin ella                                -> EJECUTADA")
    print("     c) nomina con DOS o mas vivos -> FUSION PENDIENTE, y se dice por que espera")
    print()
    resumen = []
    for o in sorted(de_fase, key=lambda x: x["id_op"]):
        oid = o["id_op"]
        ns = o.get("nodos") or []
        res = sorted(set(resolver(n) for n in ns))
        viv = sorted(x for x in res if vivo(x))
        nota = o.get("nota") or ""
        consumida = "CONSUMIDA" in nota.upper()
        regs = [(n, l) for n, l in sedes_de(lineas, BT + oid + BT)
                if l.startswith("## ")]
        commits = [x for x in git("log", "--oneline", "--all", "-F", "--grep", oid).split(NL) if x]
        if not ns:
            destino = "ABRIDOR DE UNIVERSO"
        elif len(viv) <= 1:
            destino = "CONSUMIDA" if consumida else "EJECUTADA"
        else:
            destino = "FUSION PENDIENTE"
        resumen.append((oid, o["estado"], len(ns), len(res), len(viv), destino))
        print("  --- %s ---" % oid)
        print("     tipo=%s | estado=%s | orden=%s" % (o["tipo"], o["estado"], o.get("orden")))
        print("     depende_de = %s" % (o.get("depende_de") or []))
        print("     nodos=%d  resueltos por P.1=%d  VIVOS HOY=%d  %s"
              % (len(ns), len(res), len(viv), viv))
        print("     nota con declaracion de CONSUMIDA: %s (nota de %d caracteres)"
              % ("SI" if consumida else "NO", len(nota)))
        if regs:
            for n, l in regs[:6]:
                print("     sede nivel 2 en 03_FUSIONES.md, linea %-5d %s" % (n, l.strip()[:88]))
        else:
            print("     sede nivel 2 en 03_FUSIONES.md: NINGUNA cabecera de nivel 2 la nombra")
        print("     commits que la nombran: %d %s"
              % (len(commits), [c.split()[0] for c in commits[:6]]))
        if destino == "CONSUMIDA":
            # QUIEN LA CONSUMIO, CITADO Y NO RECORDADO: las filas de la pagina que
            # nombran la ficha Y ademas nombran un TRAMO son las del registro que
            # la vuelta 64 escribio al declararlas consumidas.
            quien = [(n, l) for n, l in sedes_de(lineas, BT + oid + BT) if "TRAMO" in l.upper()]
            for n, l in quien[:3]:
                print("     quien la consumio, linea %-5d %s" % (n, l.strip()[:88]))
            if not quien:
                print("     quien la consumio: NINGUNA fila de la pagina la nombra junto a un TRAMO")
        if destino == "FUSION PENDIENTE":
            for d in (o.get("depende_de") or []):
                dep = F.get(d)
                print("     espera por %-16s fase=%-12s estado=%s"
                      % (d, dep["fase"] if dep else "SIN FICHA",
                         dep["estado"] if dep else "SIN FICHA"))
        print("     DESTINO MEDIDO: %s" % destino)
        print()
    print("  RESUMEN DE LAS %d, POR DESTINO:" % len(de_fase))
    for etq in ("ABRIDOR DE UNIVERSO", "EJECUTADA", "CONSUMIDA", "FUSION PENDIENTE"):
        cuales = [r[0] for r in resumen if r[5] == etq]
        print("     %-22s %2d  %s" % (etq, len(cuales), cuales))
    print()
    return resumen


def bloque_1b(lineas):
    """Los registros de los dos abridores: donde vive lo que hicieron."""
    print("=" * 78)
    print("BLOQUE 1.b: LOS REGISTROS DE LOS DOS ABRIDORES, QUE ES SU DESTINO")
    print("=" * 78)
    print()
    for oid in ("OP-U-01", "OP-U-02"):
        cabs = [(n, l) for n, l in sedes_de(lineas, oid) if l.startswith("## ")]
        print("  --- %s: %d cabeceras de nivel 2 en 03_FUSIONES.md ---" % (oid, len(cabs)))
        for n, l in cabs:
            print("     linea %-5d %s" % (n, l.strip()[:96]))
        print()


def region_tramo(lineas):
    """La region de la pagina donde viven los registros del tramo unico: desde la
    PRIMERA cabecera de nivel 2 que dice TRAMO UNICO hasta el final."""
    for i, l in enumerate(lineas):
        if l.startswith("## ") and "TRAMO UNICO" in l:
            return i
    return 0


def bloque_2(F, resolver, vivo, lineas, tramo, prot):
    print("=" * 78)
    print("BLOQUE 2: LOS DECLARADOS Y NO FUNDIDOS, MEDIDOS POR DOS VIAS")
    print("=" * 78)
    filas = [json.loads(l) for l in io.open(os.path.join(RAIZ, tramo.replace("/", os.sep)),
                                            encoding="utf-8") if l.strip()]
    inicio = region_tramo(lineas)
    print()
    print("  fichero fijado del tramo : %s (%d filas)" % (tramo, len(filas)))
    print("  region de los registros  : desde la linea %d (%s)"
          % (inicio + 1, lineas[inicio].strip()[:60]))
    print()

    # VIA A: sobre el grafo. Un acto esta ABIERTO si le quedan DOS o mas vivos.
    # Esa es toda la aritmetica y es la misma de tramo_al_cierre.py.
    abiertos, fundidos = [], []
    detalle = {}
    for r in filas:
        o = int(r["orden_universo"])
        M = r["miembros"]
        viv = sorted(m for m in M if vivo(m))
        duenos = r.get("duenos_cualquier_operacion") or []
        detalle[o] = (M, viv, duenos)
        (fundidos if len(viv) <= 1 else abiertos).append(o)
    print("  VIA A, SOBRE EL GRAFO DE HOY (un acto ABIERTO es el que conserva DOS o mas vivos):")
    print("     actos FUNDIDOS (un vivo o ninguno)          : %d" % len(fundidos))
    print("     actos ABIERTOS                              : %d %s"
          % (len(abiertos), sorted(abiertos)))

    # VIA B: sobre la pagina. Un acto esta DECLARADO si alguna sede suya en la
    # region del tramo lleva la frase DECLARADO Y NO FUNDIDO, en singular o en
    # plural, Y ademas nombra al acto por uno de los cuatro tokens canonicos. Los
    # tokens llevan borde de palabra a proposito: sin el, el ACTO 1 se llevaria
    # las sedes del 12, del 14 y del 17.
    re_decl = re.compile(r"DECLARADOS? Y NO FUNDIDOS?", re.I)
    via_b = {}
    for o in sorted(detalle):
        tokens = [re.compile(r"^\|\s*\*\*%d\*\*\s*\|" % o),
                  re.compile(r"\bACTOS?\s+" + BT + r"?%d" % o + BT + r"?\b", re.I),
                  re.compile(BT + r"acto %d" % o + BT, re.I),
                  re.compile(r"\sY\s+" + BT + r"%d" % o + BT)]
        golpes = [i + 1 for i in range(inicio, len(lineas))
                  if re_decl.search(lineas[i]) and any(t.search(lineas[i]) for t in tokens)]
        if golpes:
            via_b[o] = golpes
    declarados = sorted(set(via_b) & set(abiertos))
    sin_declarar = sorted(set(abiertos) - set(via_b))
    print()
    print("  VIA B, SOBRE LA PAGINA (sedes con la frase DECLARADO Y NO FUNDIDO):")
    print("     actos con al menos una sede                 : %d %s"
          % (len(via_b), sorted(via_b)))
    print()
    print("  LAS DOS VIAS, CRUZADAS:")
    print("     ABIERTOS que la pagina DECLARA              : %d %s"
          % (len(declarados), declarados))
    print("     ABIERTOS que la pagina NO declara           : %d %s"
          % (len(sin_declarar), sin_declarar))
    print("     declarados en la pagina que YA NO estan abiertos: %s"
          % sorted(set(via_b) - set(abiertos)))
    con_dueno = [o for o in sin_declarar if detalle[o][2]]
    sin_dueno = [o for o in sin_declarar if not detalle[o][2]]
    print("     de los NO declarados, CON dueno             : %d %s" % (len(con_dueno), con_dueno))
    print("     de los NO declarados, SIN dueno NI destino  : %d %s" % (len(sin_dueno), sin_dueno))
    dobles = [o for o in declarados if detalle[o][2]]
    print("     DECLARADOS que ademas tienen dueno          : %d %s" % (len(dobles), dobles))
    print()
    print("  LOS DECLARADOS, UNO A UNO, CON SUS PUERTAS Y SU MOTIVO CITADO:")
    print()
    for o in declarados:
        M, viv, duenos = detalle[o]
        puertas = sorted(m for m in viv if m in prot)
        sedes = via_b.get(o, [])
        motivos = set()
        for n in sedes:
            for etq, aguja in MOTIVOS:
                if aguja in lineas[n - 1]:
                    motivos.add(etq)
        print("     acto %-3d miembros %-2d vivos %-2d PUERTAS %d %s%s"
              % (o, len(M), len(viv), len(puertas), puertas if puertas else "",
                 "  DUENO %s" % duenos if duenos else ""))
        print("        nomina viva : %s" % ", ".join(viv))
        for n in sedes[:4]:
            print("        sede linea %-5d %s" % (n, lineas[n - 1].strip()[:84]))
        print("        motivos que la sede cita: %s"
              % (sorted(motivos) if motivos else "NINGUNO LEGIBLE EN LA SEDE"))
        print()
    return declarados, con_dueno, sin_dueno, detalle


def bloque_4b(F, resumen):
    """LO QUE BLOQUEA A LAS FICHAS DE LA FASE 03 QUE AUN TIENEN FUSION PENDIENTE.
    No basta con decir que la mesa OP-M-03 no es de la fase 03: hay que mirar TODAS
    las que estorban, porque una fase no cierra por la fase de quien la bloquea sino
    por lo que a ella misma le falta."""
    print("=" * 78)
    print("BLOQUE 4.b: QUIEN BLOQUEA A LAS FICHAS DE LA FASE %s QUE SIGUEN PENDIENTES" % FASE)
    print("=" * 78)
    print()
    pendientes = [r[0] for r in resumen if r[5] == "FUSION PENDIENTE"]
    bloqueadores = {}
    for oid in pendientes:
        for d in (F[oid].get("depende_de") or []):
            bloqueadores.setdefault(d, []).append(oid)
    print("  fichas de la fase %s con FUSION PENDIENTE: %d %s" % (FASE, len(pendientes), pendientes))
    print()
    print("  | quien bloquea | su fase | su estado | a cuantas | cuales |")
    print("  |---|---|---|---:|---|")
    for d in sorted(bloqueadores):
        g = F.get(d)
        print("  | %s | %s | %s | %d | %s |"
              % (d, g["fase"] if g else "SIN FICHA", g["estado"] if g else "SIN FICHA",
                 len(bloqueadores[d]), ", ".join(sorted(bloqueadores[d]))))
    print()
    fuera = sorted(d for d in bloqueadores if F.get(d) and F[d]["fase"] != FASE)
    dentro = sorted(d for d in bloqueadores if F.get(d) and F[d]["fase"] == FASE)
    print("  bloqueadores de FUERA de la fase %s : %d %s" % (FASE, len(fuera), fuera))
    print("  bloqueadores de DENTRO de la fase %s: %d %s" % (FASE, len(dentro), dentro))
    print()
    return pendientes, bloqueadores


def bloque_3(F, con_dueno, detalle, lineas):
    print("=" * 78)
    print("BLOQUE 3: LOS ACTOS CON DUENO, CON EL DUENO RE-MEDIDO CAMPO A CAMPO")
    print("=" * 78)
    print()
    print("  LA VARA ES LA DE LA ADJUDICACION 2 DEL ACTA 68: el dueno de un acto es")
    print("  toda ficha que nombre a alguno de sus miembros en nodos, preservar o")
    print("  eliminar. Se cruza contra LAS %d FICHAS, no contra las de una fase." % len(F))
    print()
    for o in con_dueno:
        M, viv, duenos_fichero = detalle[o]
        hallados = {}
        for oid, f in F.items():
            campos = {}
            for campo in ("nodos", "preservar", "eliminar"):
                comunes = sorted(set(f.get(campo) or []) & set(M))
                if comunes:
                    campos[campo] = comunes
            if campos:
                hallados[oid] = campos
        print("  --- acto %d: %d miembros, %d vivos ---" % (o, len(M), len(viv)))
        print("     miembros: %s" % ", ".join(M))
        print("     duenos escritos en el fichero del tramo : %s" % duenos_fichero)
        print("     duenos RE-MEDIDOS campo a campo          : %s" % sorted(hallados))
        print("     las dos vias coinciden                   : %s"
              % ("SI" if sorted(hallados) == sorted(duenos_fichero) else "NO"))
        for oid in sorted(hallados):
            f = F[oid]
            print("        %-14s fase=%-12s estado=%-7s tipo=%s"
                  % (oid, f["fase"], f["estado"], f["tipo"][:40]))
            for campo, comunes in sorted(hallados[oid].items()):
                print("           campo %-10s -> %s" % (campo, comunes))
            print("           SU FASE ES LA %s: %s" % (f["fase"],
                  "FUERA de la fase %s" % FASE if f["fase"] != FASE
                  else "DENTRO de la fase %s" % FASE))
        print()


def bloque_4(F):
    print("=" * 78)
    print("BLOQUE 4: LA MESA %s, SU FICHA LEIDA ENTERA" % MESA)
    print("=" * 78)
    print()
    f = F.get(MESA)
    if not f:
        print("  ROJO: no existe la ficha %s en OPERACIONES.jsonl" % MESA)
        return None
    print("  id_op       : %s" % f["id_op"])
    print("  FASE        : %s" % f["fase"])
    print("  tipo        : %s" % f["tipo"])
    print("  estado      : %s" % f["estado"])
    print("  orden       : %s   fecha_corte: %s" % (f.get("orden"), f.get("fecha_corte")))
    print("  nodos       : %s" % (f.get("nodos") or []))
    print("  depende_de  : %s" % (f.get("depende_de") or []))
    print("  bloquea_a   : %s" % (f.get("bloquea_a") or []))
    print("  pregunta_pendiente: %s" % f.get("pregunta_pendiente"))
    print("  adjudicacion: %d caracteres, %s"
          % (len(f.get("adjudicacion") or ""),
             "ADJUDICADA" if (f.get("adjudicacion") or "").strip() else "SIN ADJUDICAR"))
    print("  la adjudicacion, entera:")
    for trozo in re.findall(r".{1,88}(?:\s|$)", (f.get("adjudicacion") or "")):
        print("     %s" % trozo.rstrip())
    print()
    print("  verificacion (%d puntos):" % len(f.get("verificacion") or []))
    for v in (f.get("verificacion") or []):
        print("     - %s" % v[:110])
    print()
    print("  LO QUE BLOQUEA, CON LA FASE DE CADA UNO LEIDA DE SU PROPIA FICHA:")
    for d in (f.get("bloquea_a") or []):
        g = F.get(d)
        print("     %-18s fase=%-12s estado=%-7s %s"
              % (d, g["fase"] if g else "SIN FICHA", g["estado"] if g else "SIN FICHA",
                 "DE LA FASE %s" % FASE if g and g["fase"] == FASE else ""))
    print()
    print("  LA LETRA, DICHA CON LA FICHA DELANTE: el campo fase de %s dice %s."
          % (MESA, f["fase"]))
    print("  %s" % ("NO pertenece a la fase %s." % FASE if f["fase"] != FASE
                    else "SI pertenece a la fase %s." % FASE))
    print()
    return f


def bloque_4c(F, bloqueadores):
    """LAS MESAS QUE ESTORBAN, LEIDAS UNA A UNA. El encargo pregunta por OP-M-03,
    y la respuesta honesta es que no esta sola: las fichas pendientes de la fase 03
    cuelgan de CINCO mesas. Cada una se lee de su ficha y se dice si esta ADJUDICADA
    (su campo adjudicacion con texto) o no. NO SE SIENTA NINGUNA."""
    print("=" * 78)
    print("BLOQUE 4.c: LAS MESAS QUE ESTORBAN, LEIDAS UNA A UNA. NINGUNA SE SIENTA.")
    print("=" * 78)
    print()
    mesas = sorted(d for d in bloqueadores if F.get(d) and F[d]["fase"] == "06_MESAS")
    print("  mesas de la fase 06_MESAS en el arbol de bloqueo: %d %s" % (len(mesas), mesas))
    print()
    print("  | mesa | fase | estado | adjudicacion | pregunta_pendiente | bloquea_a |")
    print("  |---|---|---|---|---|---:|")
    for d in mesas:
        g = F[d]
        adj = (g.get("adjudicacion") or "").strip()
        print("  | %s | %s | %s | %s | %s | %d |"
              % (d, g["fase"], g["estado"],
                 "ADJUDICADA, %d caracteres" % len(adj) if adj else "SIN ADJUDICAR",
                 g.get("pregunta_pendiente") or "ninguna",
                 len(g.get("bloquea_a") or [])))
    print()
    todas = sorted(o["id_op"] for o in F.values() if o["fase"] == "06_MESAS")
    print("  para contraste, TODAS las fichas de la fase 06_MESAS: %d %s" % (len(todas), todas))
    sin_adj = [d for d in todas if not (F[d].get("adjudicacion") or "").strip()]
    print("  de esas, SIN adjudicacion escrita: %d %s" % (len(sin_adj), sin_adj))
    print()
    return mesas, sin_adj


def bloque_5(resumen, declarados, con_dueno, sin_dueno, mesa, F, detalle, bloqueadores):
    print("=" * 78)
    print("BLOQUE 5: EL VEREDICTO MEDIDO, PIEZA A PIEZA. NO DECIDE: MIDE.")
    print("=" * 78)
    print()
    pendientes = [r for r in resumen if r[5] == "FUSION PENDIENTE"]
    nodos_decl = sum(len(detalle[o][1]) for o in declarados)
    nodos_dueno = sum(len(detalle[o][1]) for o in con_dueno)
    filas = [
        ("fichas de la fase %s con FUSION PENDIENTE" % FASE,
         "%d de %d" % (len(pendientes), len(resumen)),
         "LISTA" if not pendientes else "PENDIENTE",
         ", ".join(r[0] for r in pendientes) or "ninguna"),
        ("actos del tramo SIN declaracion y SIN dueno",
         "%d" % len(sin_dueno),
         "LISTA" if not sin_dueno else "PENDIENTE",
         "medido en el bloque 2 por las dos vias: %s"
         % (sin_dueno if sin_dueno else "todo acto abierto o esta DECLARADO o tiene dueno")),
        ("actos DECLARADOS Y NO FUNDIDOS",
         "%d actos, %d nodos" % (len(declarados), nodos_decl),
         "PENDIENTE",
         "su subconjunto es pregunta abierta, no se resuelve aqui"),
        ("actos con DUENO fuera de la fase %s" % FASE,
         "%d actos, %d nodos" % (len(con_dueno), nodos_dueno),
         "PENDIENTE",
         "sus duenos y sus fases van medidos en el bloque 3"),
        ("la mesa %s" % MESA,
         "fase %s" % (mesa["fase"] if mesa else "?"),
         "FUERA DE LA FASE" if mesa and mesa["fase"] != FASE else "DENTRO",
         "bloquea a %d fichas, y las de la fase %s van nombradas en el bloque 4"
         % (len(mesa.get("bloquea_a") or []) if mesa else 0, FASE)),
        ("mesas y fichas que BLOQUEAN a las pendientes de la fase %s" % FASE,
         "%d bloqueadores distintos" % len(bloqueadores),
         "PENDIENTE" if bloqueadores else "LISTA",
         ", ".join(sorted(bloqueadores)) or "ninguno"),
    ]
    print("  | pieza | lo medido | estado | nota |")
    print("  |---|---|---|---|")
    for a, b, c, d in filas:
        print("  | %s | %s | %s | %s |" % (a, b, c, d))
    print()
    print("  LO QUE ESTE INSTRUMENTO NO HACE, Y SE DICE PARA QUE NADIE LO LEA DE MAS:")
    print("     no decide si la fase %s esta CERRADA Y VERIFICADA;" % FASE)
    print("     no abre la fase 04; no funde; no declara; no sienta la mesa;")
    print("     no toca un nodo. La parada la escribe el auditor, no este fichero.")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramo", default="docs/loop/TRAMO_UNICO_OPU02_V64.jsonl")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    G, resolver, vivo = cargar_grafo()
    F = fichas()
    lineas = io.open(PAGINA, encoding="utf-8").read().split(NL)
    prot = protegidos()
    print("=" * 78)
    print("EL PESO DEL CIERRE DE LA FASE %s, MEDIDO Y NO DECIDIDO (vuelta 74)" % FASE)
    print("  grafo   : %d nodos, %d vivos" % (len(G), sum(1 for x in G if vivo(x))))
    print("  fichas  : %d en OPERACIONES.jsonl" % len(F))
    print("  pagina  : docs/plan/03_FUSIONES.md, %d lineas" % len(lineas))
    print("  puertas : universo protegido de %d ids, IMPORTADO de" % len(prot))
    print("            scripts/loop/varas_n_arias_del_tramo.py y no re-inventado")
    print("  HEAD    : %s" % git("log", "-1", "--format=%h %cd", "--date=format:%Y-%m-%d %H:%M"))
    print("=" * 78)
    print()
    resumen = bloque_1(F, resolver, vivo, lineas)
    bloque_1b(lineas)
    declarados, con_dueno, sin_dueno, detalle = bloque_2(F, resolver, vivo, lineas, a.tramo, prot)
    bloque_3(F, con_dueno, detalle, lineas)
    mesa = bloque_4(F)
    _pend, bloqueadores = bloque_4b(F, resumen)
    bloque_4c(F, bloqueadores)
    bloque_5(resumen, declarados, con_dueno, sin_dueno, mesa, F, detalle, bloqueadores)
    print("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
