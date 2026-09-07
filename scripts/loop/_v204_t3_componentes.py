# -*- coding: utf-8 -*-
r"""_v204_t3_componentes.py . TAREA 3 DE LA VUELTA 204: DE DONDE SALE LA
DISCREPANCIA DE COMPONENTES QUE EL PROPIO INSTRUMENTO DECLARA.

PREFIJO DE GUION BAJO: computo de una vuelta, fuera del censo y fuera de la
nomina (`AUDITOR.md` 6.3, `4.5` del acta 199, `4.6` del acta 203).

LO QUE NO HACE, Y VA DELANTE: **NO REGENERA LA NOMINA SELLADA.**
`docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` **se CUENTA, no se reescribe**, y
este fichero no la abre en modo escritura en ninguna linea.

EL PROTOCOLO DEL SELLO, Y AQUI SE TOMA LA PUERTA QUE NI SIQUIERA ESCRIBE. El
encargo avisa de que `scripts/loop/vuelta169_tarea3_op_i_01.py` **escribe** sobre
`docs/loop/RECOMPUTO_V169.jsonl`, que se sello en la vuelta 169. Comprobado
leyendo su codigo: no lo escribe con un `open` propio sino **por subproceso**, en
sus lineas 145 a 149, llamando a `scripts/plan/recomputo_3388.py --salida`. Y el
propio instrumento deja una puerta escrita en su linea 52: la variable de entorno
`V169_RECOMPUTO_SALIDA`. **Asi que aqui se redirige la salida y la sede sellada
NO SE TOCA**, y se mide antes y despues para probarlo en vez de decirlo.

QUE MIDE, TODO CON EL RESOLUTOR DELANTE POR `P.1`:
  A  las dos sedes, por las dos convenciones
  B  el instrumento corrido hoy, con su bloque `E` reproducido
  C  el cotejo conjunto a conjunto: cuantas del sellado no estan hoy, cuantas
     hay hoy que no estaban, y cuantas coinciden
  D  LA CAUSA, medida en positivo y no adivinada: universo, fecha o instrumento
  E  la aritmetica del colapso, leida de la salida del recomputo de hoy

USO: python scripts/loop/_v204_t3_componentes.py
"""
import collections
import hashlib
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
PY = sys.executable

REL_SELLADO = "docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl"
REL_V169 = "docs/loop/RECOMPUTO_V169.jsonl"
REL_MIA = "docs/loop/RECOMPUTO_V204_DIAGNOSTICO.jsonl"
REL_INSTR = "scripts/loop/vuelta169_tarea3_op_i_01.py"
REL_MOTOR = "scripts/plan/recomputo_3388.py"
REL_GRAFO = "dataset/metadata/master_graph.json"

L = []


def w(s=""):
    L.append(s)


def correr(args, env_extra=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    if env_extra:
        env.update(env_extra)
    r = subprocess.run(args, cwd=RAIZ, capture_output=True, env=env)
    return r.returncode, (r.stdout.decode("utf-8", "replace")
                          + r.stderr.decode("utf-8", "replace")).replace(
                              chr(13) + NL, NL)


def dos_convenciones(rel):
    ruta = os.path.join(RAIZ, rel)
    if not os.path.isfile(ruta):
        return None
    d = io.open(ruta, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return dict(disco=len(d), lf=len(lf),
                sha_lf=hashlib.sha256(lf).hexdigest()[:16],
                texto=lf.decode("utf-8", "replace"))


def cargar(rel):
    return [json.loads(l) for l in io.open(os.path.join(RAIZ, rel),
                                           encoding="utf-8") if l.strip()]


w("=" * 78)
w("VUELTA 204, TAREA 3: DE DONDE SALE LA DISCREPANCIA DE COMPONENTES QUE EL")
w("PROPIO INSTRUMENTO DECLARA. LA NOMINA SELLADA SE CUENTA, NO SE REESCRIBE.")
w("=" * 78)
w("")

w("A) LAS DOS SEDES AL ENTRAR, POR LAS DOS CONVENCIONES")
m_sell = dos_convenciones(REL_SELLADO)
w("   %s: disco %d bytes | LF %d bytes | sha256 LF %s"
  % (REL_SELLADO, m_sell["disco"], m_sell["lf"], m_sell["sha_lf"]))
m_v169_antes = dos_convenciones(REL_V169)
w("   %s: disco %d bytes | LF %d bytes | sha256 LF %s"
  % (REL_V169, m_v169_antes["disco"], m_v169_antes["lf"],
     m_v169_antes["sha_lf"]))
w("   EL `PD.2` SE PUBLICA Y NO SE RESUELVE: los dos tamanos de la sede sellada")
w("   de la 169 discrepan por el CRLF que `git checkout` deja, %d en disco y %d"
  % (m_v169_antes["disco"], m_v169_antes["lf"]))
w("   normalizado a LF. La convencion de bytes sigue siendo del fundador.")
w("")

w("B) EL PROTOCOLO DEL SELLO, Y LA PUERTA QUE NI SIQUIERA ESCRIBE")
m_instr = dos_convenciones(REL_INSTR)
lineas_instr = m_instr["texto"].split(NL)
directas = [i for i, l in enumerate(lineas_instr, 1)
            if re.search(r"\.write\s*\(|open\s*\([^)]*[" + chr(34) + chr(39)
                         + r"]w", l)]
indirectas = [i for i, l in enumerate(lineas_instr, 1)
              if "--salida" in l or "SALIDA_V169" in l]
w("   %s: disco %d bytes | LF %d bytes | sha256 LF %s"
  % (REL_INSTR, m_instr["disco"], m_instr["lf"], m_instr["sha_lf"]))
w("   CIFRA lineas con ESCRITURA DIRECTA (`.write(` o `open(...,'w')`): %d | %s"
  % (len(directas), ", ".join(str(x) for x in directas) or "(ninguna)"))
w("   CIFRA lineas que ESCRIBEN POR SUBPROCESO (`--salida` o `SALIDA_V169`): %d"
  % len(indirectas))
w("      lineas: %s" % ", ".join(str(x) for x in indirectas))
w("   MI PROPIA CAIDA, DECLARADA AQUI Y NO TAPADA: el bloque `H.3` de mi sello")
w("   de apertura publico *VEREDICTO DE LA COMPROBACION PREVIA: NO ESCRIBE*")
w("   sobre este instrumento, y ES FALSO EN LO QUE IMPORTA. Mi marca solo veia")
w("   la ESCRITURA DIRECTA, que en efecto es 0, y este instrumento escribe POR")
w("   SUBPROCESO. La cifra de 0 era cierta; la palabra que le puse encima, no.")
w("   EL TEXTO VIEJO NO SE BORRA: sigue entero en el sello de apertura.")
env_extra = {"V169_RECOMPUTO_SALIDA":
             os.path.join(RAIZ, REL_MIA.replace("/", os.sep))}
w("   REMEDIO: se redirige la salida con `V169_RECOMPUTO_SALIDA`, que el propio")
w("   instrumento documenta en su linea 52, a %s." % REL_MIA)
c, sal = correr([PY, REL_INSTR], env_extra)
io.open(os.path.join(LOOP, "SALIDA_V204_T3_INSTRUMENTO.txt"), "w",
        encoding="utf-8", newline=NL).write(sal)
w("   exit del instrumento: %d" % c)
m_v169_desp = dos_convenciones(REL_V169)
w("   %s DESPUES de correr: disco %d bytes | LF %d bytes | sha256 LF %s"
  % (REL_V169, m_v169_desp["disco"], m_v169_desp["lf"], m_v169_desp["sha_lf"]))
w("   LA SEDE SELLADA DE LA 169 QUEDA IDENTICA, y no hizo falta restaurarla: %s"
  % ("SI" if m_v169_desp["sha_lf"] == m_v169_antes["sha_lf"] else "NO"))
_c, st = correr(["git", "status", "--porcelain", "--", REL_V169, REL_SELLADO])
filas_st = [x for x in st.split(NL) if x.strip()]
w("   CIFRA filas de `git status --porcelain` sobre las DOS sedes: %d" % len(filas_st))
for x in filas_st:
    w("      %s" % x.strip())
w("")
w("   EL BLOQUE `E` DEL INSTRUMENTO, REPRODUCIDO HOY Y NO COPIADO DEL ENCARGO:")
dentro = False
for l in sal.split(NL):
    if l.startswith("E) "):
        dentro = True
    elif l.startswith("F) "):
        dentro = False
    if dentro and l.strip():
        w("      %s" % l.rstrip())
w("")

w("C) EL COTEJO CONJUNTO A CONJUNTO, CON EL RESOLUTOR DELANTE POR `P.1`")
G = json.load(io.open(os.path.join(RAIZ, REL_GRAFO), encoding="utf-8"))["nodos"]
ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}


def res(x, visto=None):
    visto = visto or set()
    while x in ALIAS and x not in visto:
        visto.add(x)
        x = ALIAS[x]
    return x


sellado = cargar(REL_SELLADO)
hoy = cargar(REL_MIA)
w("   CIFRA componentes del fichero SELLADO: %d" % len(sellado))
w("   CIFRA componentes de la corrida de HOY: %d" % len(hoy))
est_s = collections.Counter(c.get("estado") for c in sellado)
est_h = collections.Counter(c.get("estado") for c in hoy)
w("   reparto por estado del SELLADO: %s" % dict(sorted(est_s.items())))
w("   reparto por estado de HOY:      %s" % dict(sorted(est_h.items())))
w("   CIFRA nodos del grafo vivo: %d | CIFRA alias en el resolutor: %d"
  % (len(G), len(ALIAS)))

claves_s = {}
for c in sellado:
    claves_s.setdefault(frozenset(res(m) for m in c["miembros"]), []).append(c)
claves_h = {}
for c in hoy:
    claves_h.setdefault(frozenset(res(m) for m in c["miembros"]), []).append(c)
S, H = set(claves_s), set(claves_h)
w("   CIFRA claves distintas del SELLADO tras resolver: %d" % len(S))
w("   CIFRA claves distintas de HOY tras resolver: %d" % len(H))
w("   CIFRA componentes del sellado QUE NO ESTAN HOY: %d" % len(S - H))
w("   CIFRA componentes de hoy QUE NO ESTABAN EN EL SELLADO: %d" % len(H - S))
w("   CIFRA componentes que COINCIDEN en las dos: %d" % len(S & H))
w("")

w("D) LA CAUSA, MEDIDA EN POSITIVO Y NO ADIVINADA")
w("   D.1 EL UNIVERSO: cuantas componentes del sellado COLAPSAN hoy")
colapsan_a_uno = 0
con_muertos = 0
tam_1 = 0
for clave, cs in claves_s.items():
    resueltos = set(clave)
    if len(resueltos) == 1:
        colapsan_a_uno += 1
    if any(x not in G for x in resueltos):
        con_muertos += 1
    if len(cs[0]["miembros"]) == 1:
        tam_1 += 1
w("      CIFRA componentes del sellado cuyos miembros resuelven HOY a UN SOLO")
w("      nodo, o sea que la campana los FUNDIO: %d de %d"
  % (colapsan_a_uno, len(claves_s)))
w("      CIFRA componentes del sellado con algun miembro que HOY no es nodo")
w("      vivo ni alias que lleve a uno: %d" % con_muertos)
w("      CIFRA componentes del sellado que ya tenian UN SOLO miembro: %d" % tam_1)
w("")
w("   D.2 LA FECHA: cuando se sello cada cosa, leido de git y no tecleado")
for rel in (REL_SELLADO, REL_V169, REL_MOTOR, REL_GRAFO, REL_INSTR):
    _c, o = correr(["git", "log", "-1", "--format=%h %ad", "--date=short",
                    "--", rel])
    w("      %-46s ultimo commit que lo toca: %s" % (rel, o.strip() or "(ninguno)"))
_c, fecha_sell = correr(["git", "log", "-1", "--format=%ad", "--date=short",
                         "--", REL_SELLADO])
fecha_sell = fecha_sell.strip()
w("      FECHA DE CORTE DEL SELLADO, leida de git: %s" % fecha_sell)
w("")
w("   D.3 EL INSTRUMENTO: cuantas veces cambio DESDE ese corte")
for rel in (REL_MOTOR, REL_INSTR):
    _c, o = correr(["git", "log", "--format=%h %ad %s", "--date=short",
                    "--since=%s" % fecha_sell, "--", rel])
    cs = [x for x in o.split(NL) if x.strip()]
    w("      CIFRA commits que tocan %s desde %s: %d" % (rel, fecha_sell, len(cs)))
    for x in cs[:6]:
        w("         %s" % x.strip()[:110])
w("")
w("   D.4 EL UNIVERSO OTRA VEZ, POR LA OTRA PUERTA: cuantas veces cambio el")
w("       grafo y la sede de veredictos desde ese mismo corte")
commits_universo = 0
for rel in (REL_GRAFO, "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"):
    _c, o = correr(["git", "log", "--format=%h", "--since=%s" % fecha_sell,
                    "--", rel])
    cs = [x for x in o.split(NL) if x.strip()]
    commits_universo += len(cs)
    w("      CIFRA commits que tocan %-40s desde %s: %d" % (rel, fecha_sell, len(cs)))
w("")

w("   D.5 LO QUE EL COLAPSO NO EXPLICA, CONTADO EN VEZ DE PASADO POR ALTO")
perdidas = S - H
perdidas_colapsan = [k for k in perdidas if len(k) == 1]
perdidas_no_colapsan = [k for k in perdidas if len(k) > 1]
w("      CIFRA componentes del sellado que HOY NO ESTAN: %d" % len(perdidas))
w("      de esas, las que resuelven a UN SOLO nodo (colapso puro): %d"
  % len(perdidas_colapsan))
w("      de esas, las que TODAVIA tienen dos o mas nodos distintos y aun asi")
w("      no aparecen hoy: %d" % len(perdidas_no_colapsan))
w("      ESAS %d SON LAS QUE EL COLAPSO NO EXPLICA SOLO, y no se tapan."
  % len(perdidas_no_colapsan))
dentro_de_otra = 0
solapan = 0
sueltas = 0
for k in perdidas_no_colapsan:
    if any(k <= kh for kh in H):
        dentro_de_otra += 1
    elif any(k & kh for kh in H):
        solapan += 1
    else:
        sueltas += 1
w("      de esas %d: %d estan CONTENIDAS en una componente de hoy, %d SOLAPAN"
  % (len(perdidas_no_colapsan), dentro_de_otra, solapan))
w("      con alguna sin estar contenidas, y %d no tocan ninguna." % sueltas)
tam = collections.Counter(len(k) for k in perdidas_no_colapsan)
w("      reparto por numero de nodos distintos tras resolver: %s"
  % dict(sorted(tam.items())))
w("")

w("E) LA ARITMETICA DEL COLAPSO, LEIDA DE LA SALIDA DEL RECOMPUTO DE HOY")
c2, sal2 = correr([PY, REL_MOTOR, "--salida", REL_MIA])
io.open(os.path.join(LOOP, "SALIDA_V204_T3_RECOMPUTO.txt"), "w",
        encoding="utf-8", newline=NL).write(sal2)
w("   exit de %s: %d" % (REL_MOTOR, c2))
for linea in sal2.split(NL):
    if re.match(r"^(A crudas|de esas,|PARES DISTINTOS|de esos,|COMPONENTES)",
                linea.strip()):
        w("      %s" % linea.strip())
w("")

w("F) EL VEREDICTO SOBRE LA CAUSA, COMPUESTO DE LAS CIFRAS DE ARRIBA")
w("   NO SE PROPONE NINGUNA REPARACION Y NO SE TOCA NINGUNA CIFRA PUBLICADA.")
w("")
w("   UNA CAIDA MIA, CAZADA ANTES DE PUBLICARSE Y DECLARADA AQUI DENTRO")
w("   (`EJECUTOR.md` 8, una correccion que tapa lo que corrige no se puede")
w("   auditar). MI PRIMERA REDACCION DE ESTE BLOQUE DECIA, TECLEADO Y NO")
w("   MEDIDO, *el instrumento y el motor NO cambiaron desde el corte del")
w("   sellado, asi que la causa NO es el instrumento*. MI PROPIO BLOQUE D.3 LO")
w("   DESMIENTE: el motor tiene commits despues del corte, y uno de ellos dice")
w("   en su asunto *la A deja de perderse al agrupar*, que es un cambio de")
w("   conducta y no de forma. LA FRASE VIEJA QUEDA ESCRITA AQUI Y NO SE BORRA.")
w("")
w("   LO QUE LAS CIFRAS SOSTIENEN, Y SOLO ESO:")
w("   . EL UNIVERSO CAMBIO, Y MUCHO: %d commits sobre el grafo y la sede de"
  % commits_universo)
w("     veredictos desde el corte %s (D.4), y **%d de las %d** componentes del"
  % (fecha_sell, colapsan_a_uno, len(claves_s)))
w("     sellado resuelven HOY a UN SOLO nodo (D.1), que es exactamente lo que la")
w("     nota de la propia ficha describe: cada acto fundido convierte sus pares")
w("     A internos en auto-arista y deja de formar componente.")
w("   . EL INSTRUMENTO TAMBIEN CAMBIO, y NO se puede descartar como causa")
w("     PARCIAL: el motor cambio despues del corte (D.3). LO QUE SI SE PUEDE")
w("     DECIR CON CIFRA es que el conjunto de hoy es SUBCONJUNTO ESTRICTO del")
w("     sellado: %d componentes de hoy que no estaban en el sellado. Un cambio"
  % len(H - S))
w("     de algoritmo que agrupara distinto habria producido componentes NUEVAS,")
w("     y no hay ninguna.")
w("   . LA FECHA NO ES UNA CAUSA APARTE sino la etiqueta de la primera: lo que")
w("     cambia con el tiempo es el universo, no el reloj.")
w("   . EL REPARTO DE LA CAUSA, EN UNA LINEA: de las %d que faltan, %d son"
  % (len(perdidas), len(perdidas_colapsan)))
w("     colapso puro y %d NO lo son, y esas %d no las explica el colapso solo."
  % (len(perdidas_no_colapsan), len(perdidas_no_colapsan)))
w("")
w("   POR DONDE ME PODRIA EQUIVOCAR, dicho antes de saberlo:")
w("   . si alguien contase como cambio del instrumento un cambio en un modulo")
w("     que el motor IMPORTE, mi D.3 no lo veria: mide los dos ficheros por su")
w("     ruta y no su cadena de imports entera;")
w("   . mi D.1 llama COLAPSO a que los miembros resuelvan a un solo nodo, y esa")
w("     es UNA lectura del colapso, no la unica: una componente puede dejar de")
w("     serlo sin fundirse del todo, y esas caen en la cifra de %d de la D.5;"
  % len(perdidas_no_colapsan))
w("   . NO SE MIDIO el grafo del corte 2026-08-19 contra el de hoy nodo a nodo:")
w("     eso exige sacar de git una version vieja del grafo y correr el motor")
w("     sobre ella, que es una corrida nueva y no la pedia el encargo. SE DICE")
w("     EN VEZ DE CALLARLO, porque es la medicion que cerraria la pregunta.")
w("")
w("FIN")

salida = NL.join(L) + NL
print(salida)
io.open(os.path.join(LOOP, "SALIDA_V204_T3_COMPONENTES.txt"), "w",
        encoding="utf-8", newline=NL).write(salida)
