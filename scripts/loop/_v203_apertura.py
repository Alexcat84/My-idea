# -*- coding: utf-8 -*-
r"""_v203_apertura.py . EL SELLO DE APERTURA DE LA VUELTA 203, ESCRITO ANTES DE
LA PRIMERA OPERACION.

PREFIJO DE GUION BAJO, Y EL ENCARGO DE ESTA VUELTA LO DICE CON SUS PALABRAS: un
fichero `_v203_*` fuera del censo y fuera de la nomina ES UN COMPUTO DE UNA
VUELTA y NO roza la moratoria de maquinaria (`AUDITOR.md` 6.3, y el `4.5` del
acta 199). Este fichero muere con la vuelta y no vigila a nadie.

QUE MIDE, Y TODO SE MIDE AQUI ANTES DE TOCAR NADA (`EJECUTOR.md` 1, LA APERTURA
SE MIDE ANTES DE LA PRIMERA OPERACION):

  A    HEAD, sellado aparte para el tallador
  B    rama y remoto
  C    el estado del arbol EN LA REDACCION QUE LA GUARDA `D.1` DE
       `cerrar_reporte.py` LEE POR EXPRESION REGULAR
  C.0  el numstat de las cuatro sedes
  D    la sede de los veredictos, por las DOS convenciones
  E    la racha de cierres, corrida DEL INSTRUMENTO, con su salida sellada
       RESTAURADA despues, porque ese instrumento PISA su propia salida y esa es
       la caida `C.2` del auditor de la 202
  F    la nomina contra el congelado en 135, y el censo
  G    la serie `R.n`
  H    los sujetos de las CUATRO tareas, cada uno por linea
  I    el hueco de la bateria, medido
  J    el inventario de salidas, CON SU CORTE Y CON LA DECLARACION DE QUE
       ENVEJECE DENTRO DE LA PROPIA VUELTA (hallazgo `5.2` del acta 202)

Y DESPUES CORRE EL CICLO ENTERO DE GATE 0, nunca `run_phase1.py` a secas.

USO: python scripts/loop/_v203_apertura.py
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
VUELTA = 203
CONGELADO_NOMINA = 135
INSTRUMENTO_RACHA = "scripts/loop/vuelta192_racha_de_cierres.py"
SELLADA_RACHA = "docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt"
ACTAS_DE_LA_DEUDA = [175, 176]
ACTAS_DE_LA_CORRECCION = [173, 174]

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


w("SELLO DE APERTURA DE LA VUELTA %d, escrito ANTES de la primera operacion."
  % VUELTA)
w("regimen: MORATORIA DE MAQUINARIA (AUDITOR.md 6.3). NO SE FABRICAN ARNESES,")
w("         GUARDAS NI LECTORES NUEVOS QUE SE QUEDEN VIGILANDO. Lo que esta")
w("         vuelta escribe son ficheros _v203_* con prefijo de guion bajo,")
w("         fuera del censo y fuera de la nomina, que es lo que el 4.5 del")
w("         acta 199 llama COMPUTO DE UNA VUELTA. La nomina queda CONGELADA")
w("         EN %d: ni crece ni se poda." % CONGELADO_NOMINA)
w("         ESTA NO ES VUELTA DE BATERIA. Corrio entera en la 200 y por la")
w("         cadencia de cinco de AUDITOR.md 6.1 le toca a la 205. La seccion 9")
w("         cierra con el HUECO DECLARADO Y MEDIDO: nombre, bytes y atribucion.")
w("         EL TRABAJO ES EL PLAN. El encargo trae CUATRO sub-tareas.")
w("ESTE BLOQUE CORRE EL CICLO COMPLETO, tsc y pnpm test INCLUIDOS, y escribe el")
w("         mismo los dos literales que la guarda D.1 de cerrar_reporte.py lee.")
w("")

w("=== A. HEAD DE APERTURA (git rev-parse HEAD, leido y no tecleado) ===")
_c, head = correr(["git", "rev-parse", "HEAD"])
head = head.strip()
w(head)
_c, o = correr(["git", "log", "-1", "--format=%H%x09%ad%x09%s", "--date=iso"])
w(o.strip())
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

w("=== D. LA SEDE DE LOS VEREDICTOS, QUE NO SE PUEDE MOVER EN ESTA VUELTA ===")
rel_ver = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
mv = dos_convenciones(rel_ver)
w(rel_ver)
w("   disco %d bytes | sha256 disco %s" % (mv["disco"], mv["sha_disco"]))
w("   LF    %d bytes | sha256 LF    %s" % (mv["lf"], mv["sha_lf"]))
w("   EL ENCARGO DICE QUE HOY VALE 0a77b5a35a962621 POR LAS DOS CONVENCIONES.")
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
w("LA COMPROBACION QUE EL AUDITOR DE LA 202 SE SALTO Y ES SU CAIDA C.2: ESTE")
w("   INSTRUMENTO PISA SU PROPIA SALIDA SELLADA %s." % SELLADA_RACHA)
w("   Se mide ANTES, se corre, se lee la cifra, y la sellada se RESTAURA con")
w("   git checkout -- y se REMIDE. Comprobado leyendo su codigo, no supuesto:")
escrituras = [i for i, l in enumerate(mi["texto"].split(NL), 1)
              if re.search(r"\.write\s*\(|open\s*\([^)]*[" + chr(34) + chr(39)
                           + r"]w", l)]
w("   CIFRA lineas con marca de ESCRITURA en disco: %d | lineas: %s"
  % (len(escrituras), ", ".join(str(x) for x in escrituras) or "(ninguna)"))
antes = dos_convenciones(SELLADA_RACHA)
w("SELLADA ANTES:     %d bytes LF | sha256 LF %s" % (antes["lf"], antes["sha_lf"]))
c, salida_racha = correr([PY, INSTRUMENTO_RACHA])
# UNA CAIDA MIA, CAZADA ANTES DE PUBLICARSE Y DECLARADA AQUI DENTRO
# (`EJECUTOR.md` 8, una correccion que tapa lo que corrige no se puede
# auditar). MI PRIMER PATRON ERA `racha[^\n]*?:\s*(\d+)` y publicaba 199,
# porque el primer renglon que trae la palabra `racha` seguida de dos puntos
# y un numero es `las vueltas de la racha: 199, 200, 201, 202`, o sea LA
# LISTA y no LA CIFRA. El 199 no era una medicion: era el sintoma de leer el
# renglon de al lado. LA CIFRA SE LEE DE SU PROPIA ETIQUETA, que es la que
# el bloque C del instrumento imprime.
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
w("EL ENCARGO DICE QUE LA RACHA VALE 4 (vueltas 199, 200, 201 y 202).")
w("   CALZA LO CORRIDO CON LO QUE EL ENCARGO DICE: %s"
  % ("SI" if racha == 4 else "NO, y se declara en vez de copiarse"))
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
w("EL ENCARGO DICE QUE HOY EL SIGUIENTE LIBRE ES R.65 Y MANDA VOLVER A CORRERLO.")
w("   CALZA LO CORRIDO CON LO QUE EL ENCARGO DICE: %s"
  % ("SI" if sl and sl.group(1) == "65" else "NO, y se declara"))
w("")

w("=== H. LOS SUJETOS DE LAS CUATRO TAREAS, MEDIDOS ANTES DE TOCAR NADA ===")
w("")
w("H.1 TAREA 1: LAS ENTRADAS R.63 Y R.64 DE docs/PENDIENTES.md Y SU FRASE FALSA")
rel_pend = "docs/PENDIENTES.md"
mp = dos_convenciones(rel_pend)
w("   %s: %d bytes disco | %d LF | sha256 LF %s"
  % (rel_pend, mp["disco"], mp["lf"], mp["sha_lf"]))
lp = mp["texto"].split(NL)
w("   CIFRA lineas por split(NL): %d" % len(lp))
for r in (63, 64):
    hits = [i for i, l in enumerate(lp, 1) if l.startswith("## R.%d." % r)]
    w("   CIFRA cabeceras `## R.%d.`: %d | linea(s): %s"
      % (r, len(hits), ", ".join(str(x) for x in hits) or "(ninguna)"))
LITERAL_FALSO = "seccion 6 sin clave numerada"
hits_f = [i for i, l in enumerate(lp, 1) if LITERAL_FALSO in l]
w("   CIFRA lineas con el literal %r: %d | linea(s): %s"
  % (LITERAL_FALSO, len(hits_f), ", ".join(str(x) for x in hits_f) or "(ninguna)"))
w("   EL ENCARGO DICE QUE VIVEN EN LAS LINEAS 15813 Y 15902, Y MANDA MEDIRLAS.")
w("   CALZA LO MEDIDO CON LO QUE EL ENCARGO DICE: %s"
  % ("SI" if hits_f == [15813, 15902] else "NO, y se declara"))
for i in hits_f:
    w("      linea %5d | %s" % (i, lp[i - 1].strip()))
w("")

w("H.2 TAREA 2: LA FICHA OP-L-01, SU `verificacion` Y EL UNIVERSO DE las_once()")
rel_ops = "docs/plan/OPERACIONES.jsonl"
mo = dos_convenciones(rel_ops)
w("   %s: %d bytes disco | %d LF | sha256 LF %s"
  % (rel_ops, mo["disco"], mo["lf"], mo["sha_lf"]))
filas = [(i, l) for i, l in enumerate(mo["texto"].split(NL), 1) if l.strip()]
w("   CIFRA lineas NO VACIAS de OPERACIONES.jsonl: %d" % len(filas))
fichas = {}
for i, l in filas:
    try:
        d = json.loads(l)
    except Exception:
        continue
    fichas.setdefault(d.get("id_op"), []).append((i, d))
for op in ("OP-L-01", "OP-I-01"):
    lns = fichas.get(op, [])
    w("   CIFRA lineas donde vive %s: %d | linea(s): %s"
      % (op, len(lns), ", ".join(str(i) for i, _d in lns) or "(ninguna)"))
    for i, d in lns:
        w("      la ficha %s vive en la LINEA %d" % (op, i))
        w("      estado=%r  tipo=%r  fase=%r  fecha_corte=%r"
          % (d.get("estado"), d.get("tipo"), d.get("fase"), d.get("fecha_corte")))
        w("      CIFRA claves de la ficha: %d" % len(d))
        w("         %s" % ", ".join(sorted(d)))
        for campo in ("evidencia", "verificacion"):
            v = d.get(campo) or []
            w("      CIFRA elementos de `%s`: %d" % (campo, len(v)))
            for k, e in enumerate(v):
                w("         %s indice %d (elemento %d), %d caracteres: %s"
                  % (campo, k, k + 1, len(e), repr(e)[:160]))
w("")
rel_ld = "docs/plan/LECTURAS_DIRIGIDAS.md"
mld = dos_convenciones(rel_ld)
w("   %s: %d bytes disco | %d LF | sha256 LF %s"
  % (rel_ld, mld["disco"], mld["lf"], mld["sha_lf"]))
lld = mld["texto"].split(NL)
w("   CIFRA lineas por split(NL): %d" % len(lld))
w("")

w("H.3 EL CRITERIO DE HECHO, LOCALIZADO POR LINEA Y NO CITADO DE MEMORIA")
rel_cri = "docs/plan/08_VERIFICACION.md"
mc = dos_convenciones(rel_cri)
lc = mc["texto"].split(NL)
w("   %s: %d bytes disco | %d LF | sha256 LF %s"
  % (rel_cri, mc["disco"], mc["lf"], mc["sha_lf"]))
w("   CIFRA lineas por split(NL): %d" % len(lc))
for lit in ("CRITERIO DE HECHO", "criterio de hecho", "OP-I-01", "OP-L-01"):
    hh = [i for i, l in enumerate(lc, 1) if lit in l]
    w("   %-20s %d linea(s): %s"
      % (lit, len(hh), ", ".join(str(x) for x in hh) or "(ninguna)"))
w("")

w("H.4 TAREA 4: LAS DOS ACTAS DE LA DEUDA Y SUS REPORTES ARCHIVADOS")
rel_acta = "docs/loop/ACTA_AUDITOR.md"
ma = dos_convenciones(rel_acta)
la = ma["texto"].split(NL)
w("   %s: %d bytes disco | %d LF | sha256 LF %s"
  % (rel_acta, ma["disco"], ma["lf"], ma["sha_lf"]))
w("   CIFRA lineas por split(NL): %d" % len(la))
cab = [(i, l) for i, l in enumerate(la, 1)
       if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA \d+\b", l)]
w("   CIFRA cabeceras de acta en el fichero: %d" % len(cab))
for v in ACTAS_DE_LA_CORRECCION + ACTAS_DE_LA_DEUDA:
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
    rrel = "docs/loop/reportes/REPORTE_V%d.md" % v
    rruta = os.path.join(RAIZ, rrel)
    ex = os.path.isfile(rruta)
    w("   %s existe: %s | bytes con os.path.getsize: %s"
      % (rrel, "SI" if ex else "NO",
         os.path.getsize(rruta) if ex else
         "NINGUNO, y el cero sale de que NO HAY FICHERO, no de medir uno"))
w("")

w("=== I. EL HUECO DE LA BATERIA, MEDIDO Y NO AFIRMADO ===")
tr = sorted(n for n in os.listdir(LOOP)
            if re.match(r"^SALIDA_V%d_BATERIA_TRAMO_\d+\.txt$" % VUELTA, n))
w("CIFRA ficheros SALIDA_V%d_BATERIA_TRAMO_N.txt al entrar: %d"
  % (VUELTA, len(tr)))
rb = os.path.join(LOOP, "SALIDA_V%d_BATERIA.txt" % VUELTA)
w("CIFRA docs/loop/SALIDA_V%d_BATERIA.txt existe al entrar: %s"
  % (VUELTA, "SI" if os.path.isfile(rb) else "NO"))
w("")

w("=== J. EL INVENTARIO DE SALIDAS DE ESTA VUELTA, CON SU CORTE ===")
w("LA MEDIA LINEA QUE EL ACTA 202 PIDE EN SU HALLAZGO 5.2, Y VA ESCRITA ANTES")
w("   DE MEDIR: ESTE INVENTARIO SE MIDE A SI MISMO Y ENVEJECE DENTRO DE LA")
w("   PROPIA VUELTA. Todo fichero SALIDA_V%d que nazca DESPUES de este bloque"
  % VUELTA)
w("   NO esta contado aqui, y esa es la razon por la que la 202 publico 37 y al")
w("   cierre habia 41. Por el banco 9.21 el corte se declara: LA CIFRA DE ABAJO")
w("   ES LA DE ESTE INSTANTE, y el cierre la REMIDE en vez de heredarla.")
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
# LA SEGUNDA CAIDA MIA, CAZADA ANTES DE PUBLICARSE Y DECLARADA AQUI DENTRO.
# Mi primera cuenta era `len([x for x in o.split(NL) if x.strip()])` y
# publicaba 1 fila con `dataset/`, `web/` y `engine/` LIMPIOS: lo que contaba
# era el renglon de aviso de git *"warning: in the working copy of
# dataset/metadata/master_graph.json, LF will be replaced by CRLF"*, que va
# por stderr y `correr()` junta con stdout. UNA FILA DE NUMSTAT TIENE FORMA:
# dos cifras (o dos guiones, que es como git marca lo binario) y una ruta,
# separadas por tabulador. Se cuenta por LA FORMA y no por "no esta vacia".
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
