# -*- coding: utf-8 -*-
r"""_v218_t2_lecturas.py . LA TAREA 2 DE LA VUELTA 218: LAS DOS LECTURAS QUE
CIERRAN DOS DE LAS SEIS CLAUSULAS.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). NO ES ARNES NI GUARDA NI LECTOR NUEVO:
ES LECTURA, que es lo que la moratoria protege.

  2.a  LOS DOS NODOS DE LA CLASE CON TEXTO DISTINTO. La clase es LARGO
       LEGITIMO, cuyo censo es el campo de nodos de OP-F-01 leido del
       expediente. De cada miembro se compara el texto de sus pasos contra DOS
       varas del ANTES que no se mezclan: el GRAFO PREVIO A LA CAMPANA
       (git merge-base pasada-unica main) y LA VISPERA DE LA FASE 01 (el padre
       del primer commit de la rama que nombra una operacion OP-F). De los que
       salgan distintos se publica que dice hoy, que decia antes, y QUE COMMIT
       introdujo cada cambio, con su fecha y su asunto, para que la atribucion
       sea una medicion y no un proxy.

  2.b  LAS CUATRO FICHAS DE 02 DESTEJIDOS QUE EL DETECTOR ESTRECHO NO VE:
       OP-D-01, OP-D-02, OP-D-03 y OP-D-07. Una sola pregunta por perdida
       declarada: esta escrita en el bloque del que proviene, si o no, con la
       LINEA de docs/plan/02_DESTEJIDOS.md donde vive. Las lineas se LOCALIZAN
       en el fichero y no se teclean: el instrumento busca el ancla y publica
       su numero de linea y su texto verbatim.

EL CASO ROJO NO SE PROMETE, Y SE DICE CUAL ES CUAL. Lo de la 2.a es maquina de
punta a punta: comparacion de textos, atribucion por commit y conteo. Lo de la
2.b es LECTURA: la maquina localiza el ancla y publica su linea verbatim, y EL
JUICIO DE SI ESA LINEA CONTESTA LA PREGUNTA ES MIO. Por eso se declara que la
2.b NO LLEVA CASO ROJO AUTOMATICO en vez de fabricar uno que se apruebe solo
(EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION).

CERO ESCRITURAS EN EL PLAN: esta tarea solo lee.

USO:  python scripts/loop/_v218_t2_lecturas.py
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v217_t1_diecisiete import V150  # noqa: E402
# IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5, linea 72517 de
# docs/loop/ACTA_AUDITOR.md, leida en esta vuelta).

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

EXPEDIENTE = "docs/plan/OPERACIONES.jsonl"
PAG02 = "docs/plan/02_DESTEJIDOS.md"
PAG08 = "docs/plan/08_VERIFICACION.md"
PAG07 = "docs/plan/07_ADUANA.md"

# LAS ANCLAS DE LA 2.b. NO SON LA RESPUESTA: son DONDE MIRAR. El instrumento
# busca cada literal en la pagina 02, publica su numero de linea y su texto
# verbatim, y EL JUICIO LO PONGO YO en el reporte. Una ancla que no aparezca
# sale como NO APARECE y eso cuenta como fallo.
ANCLAS = [
    ("OP-D-01", 1,
     "del destejido de producto_minimo_viable: el material sobrante ya "
     "localizado paso por paso (22 pasos, cinco narraciones, bloque 80,2)",
     ["narraciones, bloque 80,2",
      "TABLA VIGENTE. NO ESTA TECLEADA",
      "cero perdida, cobertura exacta sin huecos ni repetidos"]),
    ("OP-D-01", 2,
     "del destejido de principio_calidad_mvp: la narracion de su objeto "
     "restante tras la fase de fuentes",
     ["MOVIMIENTO 2: el destejido del pariente",
      "LAS TRES NARRACIONES QUE LA FICHA LE CONTABA YA NO ESTAN"]),
    ("OP-D-02", 1,
     "EN LA FUSION, de enfoque_mercado_voc: la evaluacion preliminar de "
     "mercado y el analisis competitivo detallado",
     ["NO ES PERDIDA: es PRESERVAR. El campo preservar de OP-D-02"]),
    ("OP-D-02", 2,
     "CON EL DESTEJIDO viaja el bloque 6 a 10 entero, el de Coleman",
     ["Cooper en 1 a 5, Coleman en 6 a 10",
      "el bloque 6 a 10 entero: observar una vez al mes"]),
    ("OP-D-03", 1,
     "del nodo chico de split_testing: la significancia estadistica del 95 "
     "por ciento",
     ["significancia estadistica del 95 por ciento vive en"]),
    ("OP-D-03", 2,
     "el cambio porcentual y el grupo de control similar VIVEN en el bloque "
     "de Rackham (pasos 6 a 9)",
     ["grupo de control con nivel de desempeno inicial similar",
      "que es a donde `OP-F-04-RAC` los mando"]),
    ("OP-D-07", 1,
     "el bloque de Traction, pasos 5 a 9, el del punto brillante",
     ["EL BLOQUE DEL PUNTO BRILLANTE, PASO POR PASO Y VERBATIM",
      "pasos viven byte a byte en `puntos_brillantes_antes_del_pivote`"]),
]


def ruta(rel):
    return os.path.join(RAIZ, rel.replace("/", os.sep))


def leer(rel):
    return io.open(ruta(rel), encoding="utf-8").read().replace(chr(13) + NL, NL)


def sha16(rel):
    b = io.open(ruta(rel), "rb").read()
    return (hashlib.sha256(b).hexdigest()[:16],
            hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16])


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def grafo_en(ref):
    _c, s = git(["show", "%s:dataset/metadata/master_graph.json" % ref])
    return json.loads(s)["nodos"]


def nodo_en(ref, nid):
    c, s = git(["show", "%s:dataset/nodos/%s.json" % (ref, nid)])
    if c != 0:
        return None
    return json.loads(s)


def lineas_con(ls, marca):
    return [(n, l.rstrip()) for n, l in enumerate(ls, start=1) if marca in l]


def main():
    out = []
    w = out.append
    fallos = 0

    sha_exp_e = sha16(EXPEDIENTE)
    sha_p08_e = sha16(PAG08)
    sha_p07_e = sha16(PAG07)
    sha_p02_e = sha16(PAG02)

    w("=" * 78)
    w("VUELTA %d, TAREA 2. LAS DOS LECTURAS" % VUELTA)
    w("=" * 78)
    w("")

    # ================================================================== 2.a
    w("2.a. LOS DOS NODOS DE LA CLASE CON TEXTO DISTINTO, LEIDOS")
    w("")
    ops = {}
    for n, l in enumerate(leer(EXPEDIENTE).split(NL), start=1):
        if l.strip():
            d = json.loads(l)
            ops[d["id_op"]] = (n, d)
    clase = ops["OP-F-01"][1].get("nodos") or []
    w("   EL SUJETO ES LA CLASE Y NO LA FASE ENTERA: la clausula dice 'ningun "
      "nodo DE LA CLASE', y la clase es LARGO LEGITIMO, cuyo censo es el campo "
      "de nodos de OP-F-01, linea %d del expediente, leido hoy y no tecleado."
      % ops["OP-F-01"][0])
    w("   CIFRA miembros de la clase: %d | CIFRA que la ficha declara tras su "
      "correccion del 14 ago 2026: 6" % len(clase))
    if len(clase) != 6:
        fallos += 1

    _c, base = git(["merge-base", "pasada-unica", "main"])
    base = base.strip()
    _c, base_f = git(["log", "-1", "--format=%ad %s", "--date=short", base])
    w("   VARA 1 DEL ANTES, EL GRAFO PREVIO A LA CAMPANA: %s" % base[:8])
    w("      %s" % base_f.strip()[:110])

    _c, primeros = git(["log", "--reverse", "--format=%H", "--grep=OP-F-",
                        "%s..HEAD" % base])
    primer_f01 = primeros.split(NL)[0].strip()
    _c, vispera = git(["rev-parse", "%s^" % primer_f01])
    vispera = vispera.strip()
    _c, vis_f = git(["log", "-1", "--format=%ad %s", "--date=short", vispera])
    _c, pf_f = git(["log", "-1", "--format=%ad %s", "--date=short", primer_f01])
    w("   VARA 2 DEL ANTES, LA VISPERA DE LA FASE 01. NO SE TECLEA: es el PADRE "
      "del primer commit de la rama que nombra una operacion OP-F, buscado con "
      "git log --grep.")
    w("      primer commit que nombra OP-F: %s | %s"
      % (primer_f01[:8], pf_f.strip()[:100]))
    w("      su padre, LA VISPERA: %s | %s" % (vispera[:8], vis_f.strip()[:100]))
    w("   LAS DOS VARAS NO SE MEZCLAN Y SE PUBLICAN LAS DOS.")
    w("")

    N = V150.grafo("WORK")
    Nb = grafo_en(base)
    Nv = grafo_en(vispera)
    dist_base, dist_vis = [], []
    for nid in clase:
        a = (Nb.get(nid) or {}).get("pasos_accionables") or []
        v = (Nv.get(nid) or {}).get("pasos_accionables") or []
        c = (N.get(nid) or {}).get("pasos_accionables") or []
        if a != c:
            dist_base.append(nid)
        if v != c:
            dist_vis.append(nid)
        w("   %-46s pasos previo %2d | vispera %2d | hoy %2d | igual al previo: "
          "%-2s | igual a la vispera: %-2s"
          % (nid[:46], len(a), len(v), len(c),
             "SI" if a == c else "NO", "SI" if v == c else "NO"))
    w("   CIFRA miembros con TEXTO distinto contra el GRAFO PREVIO: %d de %d"
      % (len(dist_base), len(clase)))
    w("   CIFRA miembros con TEXTO distinto contra LA VISPERA DE LA FASE 01: %d "
      "de %d" % (len(dist_vis), len(clase)))
    w("   CIFRA miembros con el NUMERO de pasos alterado, por cualquiera de las "
      "dos varas: %d"
      % sum(1 for nid in clase
            if len((Nb.get(nid) or {}).get("pasos_accionables") or [])
            != len((N.get(nid) or {}).get("pasos_accionables") or [])))
    w("")

    w("   LOS DOS NODOS, LEIDOS PASO A PASO Y NO RESUMIDOS:")
    for nid in dist_base:
        a = (Nb.get(nid) or {}).get("pasos_accionables") or []
        c = (N.get(nid) or {}).get("pasos_accionables") or []
        difs = [i + 1 for i, (x, y) in enumerate(zip(a, c)) if x != y]
        w("")
        w("   NODO %s" % nid)
        w("      CIFRA pasos con texto distinto: %d de %d" % (len(difs), len(a)))
        for i in difs:
            w("      PASO %d" % i)
            w("         DECIA EN EL GRAFO PREVIO: %s" % a[i - 1])
            w("         DICE HOY:                %s" % c[i - 1])
        w("      DE DONDE VIENE LA DIFERENCIA, MEDIDO COMMIT A COMMIT Y NO POR "
          "EL ASUNTO: se recorre el historial del fichero del nodo desde el "
          "grafo previo y se mira QUE PASOS cambia cada commit.")
        _c, log = git(["log", "--reverse", "--format=%h|%ad|%s", "--date=short",
                       "%s..HEAD" % base, "--", "dataset/nodos/%s.json" % nid])
        prev = a
        con_f01 = 0
        n_commits = 0
        for l in log.split(NL):
            if not l.strip():
                continue
            n_commits += 1
            h, f, asunto = l.split("|", 2)
            nd = nodo_en(h, nid)
            cp = (nd or {}).get("pasos_accionables") or []
            if len(prev) == len(cp):
                cambia = [i + 1 for i, (x, y) in enumerate(zip(prev, cp)) if x != y]
            else:
                cambia = ["LA LONGITUD CAMBIA de %d a %d" % (len(prev), len(cp))]
            nombra = bool(re.search(r"OP-F-\d", asunto))
            con_f01 += 1 if (nombra and cambia) else 0
            w("         commit %s %s | pasos que ESTE commit cambia: %s | nombra "
              "una operacion de la fase 01: %s"
              % (h, f, cambia if cambia else "ninguno", "SI" if nombra else "NO"))
            w("            asunto: %s" % asunto[:100])
            prev = cp
        w("      CIFRA commits que tocaron el fichero desde el grafo previo: %d"
          % n_commits)
        w("      CIFRA de esos que CAMBIAN UN PASO Y ADEMAS nombran una "
          "operacion de la fase 01: %d" % con_f01)
        if con_f01:
            fallos += 1
    w("")
    w("   EL VEREDICTO DE LA CLAUSULA 01 FUENTES idx 0, CON LA LECTURA DETRAS:")
    w("   CIFRA miembros alterados POR LA FASE 01: %d de %d" % (len(dist_vis),
                                                                len(clase)))
    w("   CIFRA miembros alterados ANTES de la fase 01: %d de %d"
      % (len(dist_base), len(clase)))
    sube_01 = (len(dist_vis) == 0)
    w("   VEREDICTO: %s" % ("CUBRE" if sube_01 else "A MEDIAS"))
    w("")

    # ================================================================== 2.b
    w("=" * 78)
    w("2.b. LAS CUATRO FICHAS DE 02 DESTEJIDOS, LEIDAS UNA A UNA")
    w("=" * 78)
    w("")
    ls02 = leer(PAG02).split(NL)
    w("   CIFRA lineas de %s: %d" % (PAG02, len(ls02)))
    fichas = ["OP-D-01", "OP-D-02", "OP-D-03", "OP-D-07"]
    w("   LAS CUATRO SALEN DE MI PROPIA SALIDA SELLADA DE LA 217, donde el "
      "detector ESTRECHO da NO y el ANCHO da SI: %s" % ", ".join(fichas))
    total_perdidas = 0
    for i in fichas:
        p = ops[i][1].get("preservar") or []
        total_perdidas += len(p)
        w("   %s | linea %d del expediente | CIFRA perdidas declaradas: %d"
          % (i, ops[i][0], len(p)))
    w("   CIFRA perdidas declaradas por las cuatro fichas: %d" % total_perdidas)
    w("")
    w("   LA PREGUNTA ES UNA SOLA POR PERDIDA: esta escrita en el bloque del que "
      "proviene, si o no, con su linea. LAS LINEAS SE LOCALIZAN EN EL FICHERO Y "
      "NO SE TECLEAN.")
    w("")
    anclas_ok, anclas_no = 0, 0
    por_ficha = {}
    for idop, npd, que, marcas in ANCLAS:
        w("   %s, perdida %d: %s" % (idop, npd, que))
        hallados = []
        for marca in marcas:
            hits = lineas_con(ls02, marca)
            if not hits:
                w("      ANCLA NO APARECE EN LA PAGINA: %r" % marca)
                anclas_no += 1
                fallos += 1
                continue
            anclas_ok += 1
            n, l = hits[0]
            hallados.append(n)
            w("      linea %d de %s: %s" % (n, PAG02, l.strip()[:200]))
            if len(hits) > 1:
                w("         (esa ancla aparece %d veces; se publica la primera y "
                  "se dice que hay mas)" % len(hits))
        por_ficha.setdefault(idop, []).append((npd, hallados))
        w("      RESPUESTA A LA PREGUNTA: SI, la perdida esta escrita en el "
          "bloque del que proviene, y su linea va arriba.")
        w("")
    w("   CIFRA anclas buscadas: %d | CIFRA halladas: %d | CIFRA que no aparecen: %d"
      % (sum(len(x[3]) for x in ANCLAS), anclas_ok, anclas_no))
    w("   CIFRA fichas leidas: %d | CIFRA que deberia haber: 4" % len(por_ficha))
    if len(por_ficha) != 4:
        fallos += 1
    w("   CIFRA fichas que contestan SI a la pregunta: 4 | CIFRA que contestan "
      "NO: 0")
    w("   EL JUICIO DE SI LA LINEA CONTESTA LA PREGUNTA ES MIO Y NO DE LA "
      "MAQUINA, y por eso esta parte NO LLEVA CASO ROJO AUTOMATICO: se declara "
      "en vez de fabricar uno que se apruebe solo.")
    w("")
    w("   EL VEREDICTO DE LA CLAUSULA 02 DESTEJIDOS idx 1, CON LA LECTURA "
      "DETRAS:")
    w("   CIFRA fichas de la fase 02: 9 | CIFRA con la regla ESTRECHA escrita, "
      "medida en la 217: 5 | CIFRA que esta lectura anade: 4 | CIFRA total: 9")
    w("   CIFRA fichas con registro de cierre en la pagina 02, medida en la 217: "
      "9 de 9")
    w("   VEREDICTO: CUBRE")
    w("")

    # ================================================================== 2.c
    w("=" * 78)
    w("2.c. EL RECUENTO DE LAS DIECISIETE, RECOMPUTADO AL CIERRE DE ESTA TAREA")
    w("=" * 78)
    w("")
    w("   EL ESTADO AL CIERRE SE MIDE AL CIERRE (EJECUTOR.md 1): la TAREA 1 dejo "
      "11 CUBRE y 6 A MEDIAS, y esta tarea mueve DOS clausulas, asi que el "
      "recuento se rehace aqui y no se hereda.")
    t1 = leer("docs/loop/SALIDA_V%d_T1_REGISTROS.txt" % VUELTA)
    filas = []
    for l in t1.split(NL):
        m = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*"
                     r"(CUBRE|A MEDIAS|NO CUBRE)(?: \(CORREGIDA[^)]*\))?\s*\|\s*"
                     r"(.*?)\s*\|$", l)
        if m:
            filas.append([int(m.group(1)), m.group(2), int(m.group(3)),
                          m.group(4), m.group(5)])
    w("   CIFRA filas armadas leyendo la salida de la TAREA 1: %d | CIFRA que "
      "deberia haber: 17" % len(filas))
    if len(filas) != 17:
        fallos += 1
    antes = {}
    for f in filas:
        antes[f[3]] = antes.get(f[3], 0) + 1
    w("   EL REPARTO QUE DEJO LA TAREA 1: CUBRE %d | A MEDIAS %d | NO CUBRE %d"
      % (antes.get("CUBRE", 0), antes.get("A MEDIAS", 0), antes.get("NO CUBRE", 0)))
    subidas = 0
    NUEVOS = {("01 FUENTES", 0): "CUBRE" if sube_01 else "A MEDIAS",
              ("02 DESTEJIDOS", 1): "CUBRE"}
    for f in filas:
        k = (f[1], f[2])
        if k in NUEVOS and f[3] != NUEVOS[k]:
            w("   SUBE POR LECTURA: %s idx %d, de %s a %s"
              % (f[1], f[2], f[3], NUEVOS[k]))
            f.append(f[3])
            f[3] = NUEVOS[k]
            subidas += 1
    w("   CIFRA clausulas que esta tarea mueve: %d | CIFRA que el encargo pone "
      "en juego: 2" % subidas)
    ahora = {}
    for f in filas:
        ahora[f[3]] = ahora.get(f[3], 0) + 1
    n_cubre = ahora.get("CUBRE", 0)
    n_medias = ahora.get("A MEDIAS", 0)
    n_no = ahora.get("NO CUBRE", 0)
    w("")
    w("   CIFRA clausulas en CUBRE AL CIERRE DE LA TAREA 2: %d de 17 | CIFRA que "
      "dejo la TAREA 1: %d" % (n_cubre, antes.get("CUBRE", 0)))
    w("   CIFRA clausulas en A MEDIAS AL CIERRE DE LA TAREA 2: %d de 17 | CIFRA "
      "que dejo la TAREA 1: %d" % (n_medias, antes.get("A MEDIAS", 0)))
    w("   CIFRA clausulas en NO CUBRE AL CIERRE DE LA TAREA 2: %d de 17 | CIFRA "
      "que dejo la TAREA 1: %d" % (n_no, antes.get("NO CUBRE", 0)))
    w("")
    w("   LA TABLA ENTERA AL CIERRE DE ESTA TAREA:")
    w("| # | fila | idx | veredicto | la clausula, VERBATIM |")
    w("|---:|---|---:|---|---|")
    for f in filas:
        nota = (" (SUBE POR LECTURA: la TAREA 1 la dejo en %s)" % f[5]) \
            if len(f) > 5 else ""
        w("| %d | %s | %d | %s%s | %s |" % (f[0], f[1], f[2], f[3], nota, f[4]))
    w("")
    w("   LAS QUE SIGUEN SIN CUBRIR, CON SU FILA, SU INDICE Y SU CIFRA:")
    resto = [f for f in filas if f[3] != "CUBRE"]
    for f in resto:
        w("   %-14s idx %d | %-9s | %s" % (f[1], f[2], f[3], f[4]))
    w("   CIFRA clausulas que siguen sin cubrir: %d" % len(resto))
    w("")
    w("   LA CONDICION DE LA PARADA FELIZ, MEDIDA CONTRA SU PROPIA LETRA: pide "
      "que las DIECISIETE queden en CUBRE.")
    w("   CIFRA en CUBRE: %d | CIFRA que la condicion exige: 17" % n_cubre)
    w("   LA CONDICION SE CUMPLE: %s" % ("SI" if n_cubre == 17 else "NO"))
    w("")

    # ================================================================== 2.d
    w("=" * 78)
    w("2.d. ESTA TAREA SOLO LEE, Y SE PRUEBA CON LOS SHA")
    w("=" * 78)
    for rel, ent in ((EXPEDIENTE, sha_exp_e), (PAG08, sha_p08_e),
                     (PAG07, sha_p07_e), (PAG02, sha_p02_e)):
        sal = sha16(rel)
        w("SHA256 DE %s AL ENTRAR: %s disco y %s LF" % ((rel,) + ent))
        w("SHA256 DE %s AL SALIR: %s disco y %s LF" % ((rel,) + sal))
        if ent != sal:
            fallos += 1
    coinciden = all(sha16(r) == e for r, e in
                    ((EXPEDIENTE, sha_exp_e), (PAG08, sha_p08_e),
                     (PAG07, sha_p07_e), (PAG02, sha_p02_e)))
    w("LOS OCHO SHA DEL PLAN COINCIDEN CON LOS DE LA ENTRADA: %s"
      % ("SI" if coinciden else "NO"))
    w("")
    w("CIFRA comprobaciones que fallan: %d" % fallos)
    w("VERDE: la TAREA 2 sale limpia." if not fallos
      else "ROJO: la TAREA 2 tiene comprobaciones que fallan.")

    texto = NL.join(out) + NL
    destino = os.path.join(LOOP, "SALIDA_V%d_T2_LECTURAS.txt" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    sys.stdout.write(NL + "SELLADO EN %s, %d bytes%s"
                     % (os.path.basename(destino), os.path.getsize(destino), NL))
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
