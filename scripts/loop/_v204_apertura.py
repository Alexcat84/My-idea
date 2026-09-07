# -*- coding: utf-8 -*-
r"""_v204_apertura.py . EL SELLO DE APERTURA DE LA VUELTA 204, ESCRITO ANTES DE
LA PRIMERA OPERACION.

PREFIJO DE GUION BAJO, Y EL ENCARGO DE ESTA VUELTA LO DICE CON SUS PALABRAS: un
fichero `_v204_*` fuera del censo y fuera de la nomina ES UN COMPUTO DE UNA
VUELTA y NO roza la moratoria de maquinaria (`AUDITOR.md` 6.3, el `4.5` del
acta 199 y el `4.6` del acta 203, que reafirma que la vara no es "si trae algo
nuevo" sino SI SE QUEDA VIGILANDO). Este fichero muere con la vuelta.

CLON DECLARADO de `scripts/loop/_v203_apertura.py`: la maquina se copia entera y
lo que cambia son los sujetos de las cuatro tareas de HOY. Se dice en vez de
disimularlo.

QUE MIDE, Y TODO SE MIDE AQUI ANTES DE TOCAR NADA (`EJECUTOR.md` 1, LA APERTURA
SE MIDE ANTES DE LA PRIMERA OPERACION):

  A    HEAD, sellado aparte para el tallador
  B    rama y remoto
  C    el estado del arbol EN LA REDACCION QUE LA GUARDA `D.1` DE
       `cerrar_reporte.py` LEE POR EXPRESION REGULAR
  C.0  el numstat de las cuatro sedes
  C.1  el numstat de LAS TRES SEDES DEL AUDITOR, que esta vuelta NO TOCA
  D    la sede de los veredictos, por las DOS convenciones
  E    la racha de cierres, corrida DEL INSTRUMENTO, comprobando ANTES si
       escribe, con su salida sellada RESTAURADA despues y REMEDIDA
  F    la nomina contra el congelado en 135, y el censo
  G    la serie `R.n`
  H    los sujetos de las CUATRO tareas, cada uno por linea
  I    el hueco de la bateria, medido, distinguiendo si el cero sale de que no
       hay fichero o de medir uno vacio
  J    el inventario de salidas, CON SU CORTE Y CON LA DECLARACION DE QUE
       ENVEJECE DENTRO DE LA PROPIA VUELTA (hallazgo `5.2` del acta 202)

Y DESPUES CORRE EL CICLO ENTERO DE GATE 0, nunca `run_phase1.py` a secas.

USO: python scripts/loop/_v204_apertura.py
"""
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
VUELTA = 204
CONGELADO_NOMINA = 135
INSTRUMENTO_RACHA = "scripts/loop/vuelta192_racha_de_cierres.py"
SELLADA_RACHA = "docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt"
ACTAS_DE_LA_DEUDA = [177, 178]
ACTAS_YA_REGISTRADAS = [173, 174, 175, 176]
SEDES_DEL_AUDITOR = ["docs/loop/PROMPT_SIGUIENTE.md",
                     "docs/loop/ACTA_AUDITOR.md",
                     "docs/loop/PARA_ALEXIS.md"]
MARCA_ESCRITURA = r"\.write\s*\(|open\s*\([^)]*[" + chr(34) + chr(39) + r"]w"

L = []


def w(s=""):
    L.append(s)


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env,
                       shell=shell)
    return r.returncode, (r.stdout.decode("utf-8", errors="replace")
                          + r.stderr.decode("utf-8", errors="replace"))


def dos_convenciones(rel):
    ruta = os.path.join(RAIZ, rel)
    if not os.path.isfile(ruta):
        return None
    d = io.open(ruta, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return dict(disco=len(d), lf=len(lf),
                sha_disco=hashlib.sha256(d).hexdigest()[:16],
                sha_lf=hashlib.sha256(lf).hexdigest()[:16],
                texto=lf.decode("utf-8", errors="replace"))


def escribir(nombre, texto):
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s_APERTURA.txt" % (VUELTA, nombre)),
            "w", encoding="utf-8", newline=NL).write(texto)


def lineas_que_escriben(texto):
    return [i for i, l in enumerate(texto.split(NL), 1)
            if re.search(MARCA_ESCRITURA, l)]


w("SELLO DE APERTURA DE LA VUELTA %d, escrito ANTES de la primera operacion."
  % VUELTA)
w("regimen: MORATORIA DE MAQUINARIA (AUDITOR.md 6.3). NO SE FABRICAN ARNESES,")
w("         GUARDAS NI LECTORES NUEVOS QUE SE QUEDEN VIGILANDO. Lo que esta")
w("         vuelta escribe son ficheros _v204_* con prefijo de guion bajo,")
w("         fuera del censo y fuera de la nomina, que es lo que el 4.5 del")
w("         acta 199 y el 4.6 del acta 203 llaman COMPUTO DE UNA VUELTA. La")
w("         nomina queda CONGELADA EN %d: ni crece ni se poda."
  % CONGELADO_NOMINA)
w("         ESTA NO ES VUELTA DE BATERIA. Le toca a la 205 por la cadencia de")
w("         cinco de AUDITOR.md 6.1. La seccion 9 cierra con el HUECO")
w("         DECLARADO Y MEDIDO: nombre, bytes y atribucion, las tres juntas.")
w("         EL TRABAJO ES EL PLAN. El encargo trae CUATRO sub-tareas mas la")
w("         TAREA 0, que es un remedio de gobierno y no trabajo de plan.")
w("ESTE BLOQUE CORRE EL CICLO COMPLETO, tsc y pnpm test INCLUIDOS, y escribe el")
w("         mismo los dos literales que la guarda D.1 de cerrar_reporte.py lee.")
w("")

w("=== A. HEAD DE APERTURA (git rev-parse HEAD, leido y no tecleado) ===")
_c, head = correr(["git", "rev-parse", "HEAD"])
head = head.strip()
w(head)
_c, o = correr(["git", "log", "-1", "--format=%H%x09%ad%x09%s", "--date=iso"])
w(o.strip()[:300])
w("")

w("=== B. RAMA Y REMOTO (leidos de git, no tecleados) ===")
_c, rama = correr(["git", "rev-parse", "--abbrev-ref", "HEAD"])
w("rama: %s" % rama.strip())
_c, up = correr(["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name",
                 "@{u}"])
w("remoto de seguimiento: %s" % up.strip())
_c, ab = correr(["git", "rev-list", "--left-right", "--count", "HEAD...@{u}"])
w("adelante/atras contra el remoto (HEAD...upstream): %s" % ab.strip())
w("")

w("=== C. EL ESTADO DEL ARBOL AL ENTRAR, EN LA REDACCION QUE LA GUARDA LEE ===")
w("LOS DOS LITERALES DE ABAJO SON LOS QUE LA GUARDA D.1 DE cerrar_reporte.py")
w("busca por expresion regular. Se escriben AQUI, en el bloque de apertura, para")
w("que la apertura sellada NO haya que tocarla al cierre.")
_c, st = correr(["git", "status", "--porcelain"])
filas_st = [x for x in st.replace(chr(13) + NL, NL).split(NL) if x.strip()]
w("CIFRA lineas de status: %d" % len(filas_st))
for x in filas_st:
    w("   %s" % x.strip())
if not filas_st:
    w("   (ninguna: el arbol entra limpio)")
_c, nd = correr(["git", "diff", "--numstat", "--", "dataset/"])
filas_nd = [x for x in nd.split(NL) if x.strip()]
w("CIFRA filas de `git diff --numstat -- dataset/` AL ENTRAR: %d" % len(filas_nd))
if not filas_nd:
    w("   (ninguna: dataset/ entra limpio)")
w("")

w("=== C.0 EL NUMSTAT DE LAS CUATRO SEDES QUE EL ENCARGO PIDE, AL ENTRAR ===")
for sede in ("dataset/", "web/", "engine/", "docs/plan/"):
    _c, o = correr(["git", "diff", "--numstat", "--", sede])
    f = [x for x in o.split(NL) if x.strip()]
    w("CIFRA filas de numstat AL ENTRAR en %-12s %d" % (sede, len(f)))
    for x in f:
        w("      %s" % x.strip())
w("")

w("=== C.1 LAS TRES SEDES DEL AUDITOR, QUE ESTA VUELTA NO ESCRIBE (TAREA 0) ===")
w("SE MIDEN AQUI PARA QUE EL CIERRE LAS PUEDA COMPARAR CONTRA ESTE MISMO HEAD.")
for sede in SEDES_DEL_AUDITOR:
    m = dos_convenciones(sede)
    if m is None:
        w("   %-34s NO EXISTE, y el cero saldria de que no hay fichero" % sede)
        continue
    w("   %-34s %d bytes disco | %d LF | sha256 LF %s"
      % (sede, m["disco"], m["lf"], m["sha_lf"]))
    _c, o = correr(["git", "diff", "--numstat", "HEAD", "--", sede])
    f = [x for x in o.split(NL) if re.match(r"^(\d+|-)\t(\d+|-)\t", x)]
    w("      CIFRA filas de numstat contra HEAD de apertura: %d" % len(f))
w("")

w("=== D. LA SEDE DE LOS VEREDICTOS, QUE NO SE PUEDE MOVER EN ESTA VUELTA ===")
rel_ver = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
mv = dos_convenciones(rel_ver)
w(rel_ver)
w("   disco %d bytes | sha256 disco %s" % (mv["disco"], mv["sha_disco"]))
w("   LF    %d bytes | sha256 LF    %s" % (mv["lf"], mv["sha_lf"]))
w("   EL ENCARGO DICE QUE AL CERRAR LA 203 VALIA 0a77b5a35a962621 POR LAS DOS.")
w("   CALZA LO MEDIDO AQUI CON LO QUE EL ENCARGO DICE: %s"
  % ("SI" if (mv["sha_disco"] == "0a77b5a35a962621"
              and mv["sha_lf"] == "0a77b5a35a962621") else
     "NO, y se declara en vez de ajustarse"))
w("")

w("=== E. LA RACHA DE CIERRES, CONTADA DEL INSTRUMENTO Y NO HEREDADA ===")
w("EL NOMBRE SALE DE LA CONSTANTE QUE SE EJECUTA, NO DE LA PROSA.")
w("instrumento: %s" % INSTRUMENTO_RACHA)
mi = dos_convenciones(INSTRUMENTO_RACHA)
w("   existe y no esta vacio: %s, %d bytes en disco | %d LF | sha256 LF %s"
  % ("SI" if mi and mi["disco"] else "NO", mi["disco"], mi["lf"], mi["sha_lf"]))
w("COMPROBACION ANTES DE CORRER, QUE EL ENCARGO PIDE EXPRESAMENTE: ESTE")
w("   INSTRUMENTO PISA SU PROPIA SALIDA SELLADA %s." % SELLADA_RACHA)
w("   Se mide ANTES, se corre, se lee la cifra, y la sellada se RESTAURA con")
w("   git checkout -- y se REMIDE. Comprobado leyendo su codigo, no supuesto:")
escrituras = lineas_que_escriben(mi["texto"])
w("   CIFRA lineas con marca de ESCRITURA en disco: %d | lineas: %s"
  % (len(escrituras), ", ".join(str(x) for x in escrituras) or "(ninguna)"))
w("   VEREDICTO DE LA COMPROBACION PREVIA: %s"
  % ("SI ESCRIBE" if escrituras else "NO ESCRIBE"))
antes = dos_convenciones(SELLADA_RACHA)
w("SELLADA ANTES:     %d bytes LF | sha256 LF %s" % (antes["lf"], antes["sha_lf"]))
c, salida_racha = correr([PY, INSTRUMENTO_RACHA])
m = re.search(r"CIFRA vueltas CONSECUTIVAS en verde hacia atras:\s*(\d+)",
              salida_racha)
racha = int(m.group(1)) if m else None
w("CIFRA racha de cierres, contada del inventario ENTERO: %s"
  % (racha if racha is not None else "(no legible)"))
mv2 = re.search(r"las vueltas de la racha:\s*([^\n]+)", salida_racha)
if mv2:
    w("las vueltas de la racha: %s" % mv2.group(1).strip())
nuevo = dos_convenciones(SELLADA_RACHA)
w("nuevo corte, medido antes de restaurar:")
w("   %d bytes LF | sha256 LF %s" % (nuevo["lf"], nuevo["sha_lf"]))
correr(["git", "checkout", "--", SELLADA_RACHA])
rest = dos_convenciones(SELLADA_RACHA)
w("SELLADA RESTAURADA:%d bytes LF | sha256 LF %s" % (rest["lf"], rest["sha_lf"]))
w("RESTAURADA IDENTICA A LA SELLADA DE ENTRADA: %s"
  % ("SI" if rest["sha_lf"] == antes["sha_lf"] else "NO"))
w("EL ENCARGO NO ME DA LA CIFRA DE LA RACHA: MANDA CONTARLA. CONTADA DA %s."
  % racha)
w("   CON RACHA %s EL TOPE ES DE CINCO SUB-TAREAS. El encargo trae CUATRO."
  % racha)
w("")

w("=== E.1 EL INVENTARIO DE CIERRES SELLADOS, CONTADO DE DISCO ===")
sell = sorted(n for n in os.listdir(LOOP)
              if re.match(r"^SALIDA_V\d+_CERRAR_REPORTE\.txt$", n))
vv = sorted(int(re.search(r"V(\d+)_", n).group(1)) for n in sell)
w("CIFRA ficheros SALIDA_V*_CERRAR_REPORTE.txt en docs/loop/: %d" % len(sell))
w("las vueltas con sellada de cierre: %s" % ", ".join(str(x) for x in vv))
w("CIFRA sellada de cierre de la vuelta %d al entrar: %d"
  % (VUELTA, 1 if VUELTA in vv else 0))
w("")

w("=== F. LA NOMINA Y EL CENSO AL ENTRAR, CONTRA EL CONGELADO EN %d ==="
  % CONGELADO_NOMINA)
w("AQUI NO SE TOCA NADA: se MIDE. Si la cifra medida no es %d, SE DECLARA."
  % CONGELADO_NOMINA)
sys.path.insert(0, AQUI)
import verificar_mutaciones_viejas as VMV   # noqa: E402
w("CIFRA entradas de la nomina, leidas de VMV.VIEJAS: %d" % len(VMV.VIEJAS))
w("CONGELADO QUE MANDA AUDITOR.md 6.3: %d" % CONGELADO_NOMINA)
w("CALZA LA NOMINA CON EL CONGELADO: %s"
  % ("SI" if len(VMV.VIEJAS) == CONGELADO_NOMINA else
     "NO, medida %d contra congelado %d" % (len(VMV.VIEJAS), CONGELADO_NOMINA)))
censo = VMV.arneses_del_directorio()
w("CIFRA arneses que el censo reconoce en scripts/loop/: %d" % len(censo))
w("LA VARA DEL CENSO, que es la que decide: %d" % VMV.VARA_DEL_CENSO)
_u, faltan_n = VMV.arneses_que_faltan()
w("CIFRA arneses del censo FUERA de la nomina CON LA VARA %d: %d"
  % (VMV.VARA_DEL_CENSO, len(faltan_n)))
for n in faltan_n:
    w("      FUERA DE LA NOMINA (con vara %d): %s" % (VMV.VARA_DEL_CENSO, n))
_u2, faltan_sin = VMV.arneses_que_faltan(vara=0)
w("CIFRA arneses del censo FUERA de la nomina SIN VARA (vara=0): %d"
  % len(faltan_sin))
w("   LAS DOS CIFRAS JUNTAS SON LA FRASE ENTERA: con vara %d salen %d, y sin"
  % (VMV.VARA_DEL_CENSO, len(faltan_n)))
w("   vara salen %d." % len(faltan_sin))
w("CIFRA entradas de la nomina que el censo NO VE: %d"
  % len(VMV.nomina_invisible_al_censo()))
w("")

w("=== G. EL NUMERO DE LA SERIE, COMPUTADO Y NO TECLEADO ===")
w("comando: python scripts/loop/serie_de_registros.py")
c, salida_serie = correr([PY, "scripts/loop/serie_de_registros.py"])
io.open(os.path.join(LOOP, "SALIDA_V%d_SERIE_APERTURA.txt" % VUELTA), "w",
        encoding="utf-8", newline=NL).write(salida_serie)
for pat in (r"SIGUIENTE LIBRE[^\n]*", r"CIFRA entradas[^\n]*",
            r"CIFRA colisiones[^\n]*", r"CIFRA huecos[^\n]*"):
    for mm in re.finditer(pat, salida_serie):
        w(mm.group(0).strip())
sl = re.search(r"SIGUIENTE LIBRE[^\n]*?R\.(\d+)", salida_serie)
w("EL ENCARGO DICE QUE AL CERRAR LA 203 EL SIGUIENTE LIBRE ERA R.67, Y MANDA")
w("   RECOMPUTARLO. CALZA LO CORRIDO CON LO QUE EL ENCARGO DICE: %s"
  % ("SI" if sl and sl.group(1) == "67" else "NO, y se declara"))
w("")

w("=== H. LOS SUJETOS DE LAS CUATRO TAREAS, MEDIDOS ANTES DE TOCAR NADA ===")
w("")
w("H.1 TAREA 1: LAS ACTAS %s Y SU HUECO EN docs/PENDIENTES.md"
  % " Y ".join(str(x) for x in ACTAS_DE_LA_DEUDA))
rel_acta = "docs/loop/ACTA_AUDITOR.md"
ma = dos_convenciones(rel_acta)
la = ma["texto"].split(NL)
w("   %s: %d bytes disco | %d LF | sha256 LF %s"
  % (rel_acta, ma["disco"], ma["lf"], ma["sha_lf"]))
w("   CIFRA lineas por split(NL): %d" % len(la))
cab = [(i, l) for i, l in enumerate(la, 1)
       if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA \d+\b", l)]
w("   CIFRA cabeceras de acta en el fichero: %d" % len(cab))
for v in ACTAS_YA_REGISTRADAS + ACTAS_DE_LA_DEUDA:
    hh = [i for i, l in cab
          if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA %d\b" % v, l)]
    if len(hh) == 1:
        sig = [i for i, _l in cab if i > hh[0]]
        fin = (sig[0] - 1) if sig else len(la)
        w("   acta %d: cabecera 1 vez, lineas %d a %d, %d lineas"
          % (v, hh[0], fin, fin - hh[0] + 1))
    else:
        w("   acta %d: la cabecera aparece %d veces (ROJO si no es 1)"
          % (v, len(hh)))
rel_pend = "docs/PENDIENTES.md"
mp = dos_convenciones(rel_pend)
lp = mp["texto"].split(NL)
w("   %s: %d bytes disco | %d LF | sha256 LF %s"
  % (rel_pend, mp["disco"], mp["lf"], mp["sha_lf"]))
w("   CIFRA lineas por split(NL): %d" % len(lp))
todas_r = [(i, re.match(r"^## R\.(\d+)\.", l).group(1))
           for i, l in enumerate(lp, 1) if re.match(r"^## R\.(\d+)\.", l)]
w("   CIFRA cabeceras `## R.n.` contadas de disco: %d" % len(todas_r))
if todas_r:
    w("   la ultima cabecera es R.%s en la linea %d"
      % (todas_r[-1][1], todas_r[-1][0]))
for r in (65, 66, 67, 68):
    hits = [i for i, n in todas_r if n == str(r)]
    w("   CIFRA cabeceras `## R.%d.`: %d | linea(s): %s"
      % (r, len(hits), ", ".join(str(x) for x in hits) or "(ninguna)"))
for v in ACTAS_YA_REGISTRADAS + ACTAS_DE_LA_DEUDA:
    hits = [i for i, l in enumerate(lp, 1)
            if re.match(r"^## R\.\d+\.", l)
            and re.search(r"[Aa]cta\b[^0-9]{0,12}%d\b" % v, l)]
    w("   CIFRA cabeceras `## R.n.` que nombran el acta %d: %d | linea(s): %s"
      % (v, len(hits), ", ".join(str(x) for x in hits) or "(ninguna)"))
rel_reparto = "scripts/loop/_v203_reparto_de_actas_viejas.py"
mr = dos_convenciones(rel_reparto)
w("   %s existe: %s" % (rel_reparto, "SI" if mr else "NO"))
if mr:
    w("      %d bytes disco | %d LF | sha256 LF %s | %d lineas"
      % (mr["disco"], mr["lf"], mr["sha_lf"], len(mr["texto"].split(NL))))
w("")

w("H.2 TAREA 2: EL CAMPO `cobertura` EN docs/plan/INVENTARIO.jsonl")
rel_inv = "docs/plan/INVENTARIO.jsonl"
minv = dos_convenciones(rel_inv)
w("   %s: %d bytes disco | %d LF | sha256 LF %s"
  % (rel_inv, minv["disco"], minv["lf"], minv["sha_lf"]))
filas_inv = [l for l in minv["texto"].split(NL) if l.strip()]
w("   CIFRA lineas NO VACIAS: %d" % len(filas_inv))
con_cob = 0
malas = 0
for l in filas_inv:
    try:
        d = json.loads(l)
    except Exception:
        malas += 1
        continue
    if "cobertura" in d:
        con_cob += 1
w("   CIFRA lineas que NO parsean como JSON: %d" % malas)
w("   CIFRA entradas CON la clave `cobertura`: %d" % con_cob)
w("   EL ENCARGO DICE 672 ENTRADAS Y MANDA RECONTARLAS: medidas %d."
  % len(filas_inv))
w("")

w("H.3 TAREA 3: LA DISCREPANCIA DE COMPONENTES, Y SUS DOS SEDES")
rel_comp = "docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl"
mcomp = dos_convenciones(rel_comp)
if mcomp:
    fc = [l for l in mcomp["texto"].split(NL) if l.strip()]
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (rel_comp, mcomp["disco"], mcomp["lf"], mcomp["sha_lf"]))
    w("   CIFRA lineas NO VACIAS del sellado de componentes: %d" % len(fc))
else:
    w("   %s NO EXISTE" % rel_comp)
rel_v169 = "docs/loop/RECOMPUTO_V169.jsonl"
m169 = dos_convenciones(rel_v169)
if m169:
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (rel_v169, m169["disco"], m169["lf"], m169["sha_lf"]))
    w("   EL ENCARGO DICE sha256 LF e8a10f174df3c5fa, 15369 disco y 15322 LF,")
    w("   y que la diferencia es el CRLF de git checkout (PD.2). CALZA: %s"
      % ("SI" if (m169["sha_lf"] == "e8a10f174df3c5fa"
                  and m169["disco"] == 15369 and m169["lf"] == 15322)
         else "NO, y se declara en vez de copiarse"))
else:
    w("   %s NO EXISTE" % rel_v169)
rel_i169 = "scripts/loop/vuelta169_tarea3_op_i_01.py"
mi169 = dos_convenciones(rel_i169)
if mi169:
    esc169 = lineas_que_escriben(mi169["texto"])
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (rel_i169, mi169["disco"], mi169["lf"], mi169["sha_lf"]))
    w("   CIFRA lineas con marca de ESCRITURA: %d | lineas: %s"
      % (len(esc169), ", ".join(str(x) for x in esc169) or "(ninguna)"))
    w("   VEREDICTO DE LA COMPROBACION PREVIA: %s"
      % ("SI ESCRIBE" if esc169 else "NO ESCRIBE"))
else:
    w("   %s NO EXISTE" % rel_i169)
w("")

w("H.4 TAREA 4: LAS FICHAS DE docs/plan/OPERACIONES.jsonl, CONTADAS AL ENTRAR")
rel_ops = "docs/plan/OPERACIONES.jsonl"
mo = dos_convenciones(rel_ops)
w("   %s: %d bytes disco | %d LF | sha256 LF %s"
  % (rel_ops, mo["disco"], mo["lf"], mo["sha_lf"]))
filas_ops = [(i, l) for i, l in enumerate(mo["texto"].split(NL), 1) if l.strip()]
w("   CIFRA lineas NO VACIAS de OPERACIONES.jsonl: %d" % len(filas_ops))
por_estado = {}
for i, l in filas_ops:
    try:
        d = json.loads(l)
    except Exception:
        por_estado.setdefault("(no parsea)", []).append(i)
        continue
    por_estado.setdefault(d.get("estado"), []).append(i)
for k in sorted(por_estado, key=str):
    w("   CIFRA fichas con estado %-12r %d" % (k, len(por_estado[k])))
w("   EL ENCARGO DICE 71 FICHAS, 42 LISTA Y 29 HECHA, Y MANDA RECONTARLAS.")
rel_vara = "scripts/loop/vuelta150_3_relectura_expediente.py"
mvara = dos_convenciones(rel_vara)
w("   %s existe: %s" % (rel_vara, "SI" if mvara else "NO"))
if mvara:
    escv = lineas_que_escriben(mvara["texto"])
    w("      %d bytes disco | %d LF | sha256 LF %s"
      % (mvara["disco"], mvara["lf"], mvara["sha_lf"]))
    w("      CIFRA lineas con marca de ESCRITURA: %d | lineas: %s"
      % (len(escv), ", ".join(str(x) for x in escv) or "(ninguna)"))
    w("      VEREDICTO DE LA COMPROBACION PREVIA: %s"
      % ("SI ESCRIBE" if escv else "NO ESCRIBE"))
w("")

w("=== I. EL HUECO DE LA BATERIA, MEDIDO Y NO AFIRMADO ===")
tr = sorted(n for n in os.listdir(LOOP)
            if re.match(r"^SALIDA_V%d_BATERIA_TRAMO_\d+\.txt$" % VUELTA, n))
w("CIFRA ficheros SALIDA_V%d_BATERIA_TRAMO_N.txt al entrar: %d"
  % (VUELTA, len(tr)))
rb = os.path.join(LOOP, "SALIDA_V%d_BATERIA.txt" % VUELTA)
existe_b = os.path.isfile(rb)
w("CIFRA docs/loop/SALIDA_V%d_BATERIA.txt existe al entrar: %s"
  % (VUELTA, "SI" if existe_b else "NO"))
w("   bytes: %s"
  % (os.path.getsize(rb) if existe_b else
     "NINGUNO, y el cero sale de que NO HAY FICHERO, no de medir uno vacio"))
w("")

w("=== J. EL INVENTARIO DE SALIDAS DE ESTA VUELTA, CON SU CORTE ===")
w("LA MEDIA LINEA QUE EL ACTA 202 PIDE EN SU HALLAZGO 5.2, Y VA ESCRITA ANTES")
w("   DE MEDIR: ESTE INVENTARIO SE MIDE A SI MISMO Y ENVEJECE DENTRO DE LA")
w("   PROPIA VUELTA. Todo fichero SALIDA_V%d que nazca DESPUES de este bloque"
  % VUELTA)
w("   NO esta contado aqui. Por el banco 9.21 el corte se declara: LA CIFRA DE")
w("   ABAJO ES LA DE ESTE INSTANTE, y el cierre la REMIDE en vez de heredarla.")
inv = sorted(n for n in os.listdir(LOOP)
             if re.match(r"^SALIDA_V%d_.*\.txt$" % VUELTA, n))
w("CIFRA ficheros SALIDA_V%d de docs/loop/ EN ESTE INSTANTE: %d"
  % (VUELTA, len(inv)))
for n in inv:
    w("   %-58s %d bytes" % (n, os.path.getsize(os.path.join(LOOP, n))))
w("LOS QUE ESTE MISMO BLOQUE VA A HACER NACER DESPUES DE CONTAR, NOMBRADOS AQUI")
w("   PARA QUE EL DESFASE NO SORPRENDA A NADIE: HEAD_APERTURA, GATE0_CMD1_,")
w("   CICLO_ETIQUETAS_, CICLO_SYNC_, CICLO_NUMSTAT_, CONTEO_, DESFASE_")
w("   CALIBRADO_, MOTOR_, TSC_ y WEB_APERTURA. SERIE_APERTURA ya nacio arriba,")
w("   dentro del bloque G, y por eso SI puede estar en la lista.")
w("")
w("FIN DEL SELLO DE APERTURA")

io.open(os.path.join(LOOP, "SALIDA_V%d_APERTURA.txt" % VUELTA), "w",
        encoding="utf-8", newline=NL).write(NL.join(L) + NL)
print(NL.join(L))

escribir("HEAD", head + NL)

print(NL + "=== EL CICLO ENTERO DE GATE 0, NUNCA run_phase1.py A SECAS ===")
c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
escribir("GATE0_CMD1", o + NL + "EXITCODE: %d" % c + NL)
print("   1/8 run_phase1.py --reaplico-curaduria  EXITCODE %d" % c)
c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
escribir("CICLO_ETIQUETAS", o + NL + "EXITCODE: %d" % c + NL)
print("   2/8 etiquetas_de_cara.py --aplicar      EXITCODE %d" % c)
c, o = correr([PY, "scripts/sync_assets_web.py"])
escribir("CICLO_SYNC", o + NL + "EXITCODE: %d" % c + NL)
print("   3/8 sync_assets_web.py                  EXITCODE %d" % c)
c, o = correr(["git", "diff", "HEAD", "--numstat", "--", "dataset/", "web/",
               "engine/"])
escribir("CICLO_NUMSTAT", o + NL + "EXITCODE: %d" % c + NL)
PATRON_FILA_NUMSTAT = re.compile(r"^(\d+|-)\t(\d+|-)\t")
filas_ciclo = [x for x in o.split(NL) if PATRON_FILA_NUMSTAT.match(x)]
print("   4/8 git diff HEAD --numstat             EXITCODE %d | filas %d"
      % (c, len(filas_ciclo)))
c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
escribir("CONTEO", o + NL + "EXITCODE: %d" % c + NL)
print("   5/8 vuelta83_conteo_aristas.py WORK     EXITCODE %d" % c)
c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + NL + "EXITCODE: %d" % c + NL)
print("   6/8 vuelta85_medir_desfase_calibrado    EXITCODE %d" % c)
c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + NL + "EXITCODE: %d" % c + NL)
print("   7/8 engine/run_all_tests.py             EXITCODE %d" % c)
c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True,
              cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d" % c + NL)
print("   8/8a npx tsc --noEmit                   EXITCODE %d" % c)
c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + NL + "EXITCODE: %d" % c + NL)
print("   8/8b pnpm test                          EXITCODE %d" % c)
print("CICLO DE APERTURA COMPLETO.")
