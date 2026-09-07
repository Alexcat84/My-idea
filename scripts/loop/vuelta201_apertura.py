# -*- coding: utf-8 -*-
r"""vuelta201_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 201, CORRIDO ANTES
DE LA PRIMERA OPERACION.

CLON DECLARADO de `scripts/loop/vuelta200_apertura.py`, que a su vez viene de la
199, la 197, la 196 y la 195. Lo que cambia se dice aqui y no se esconde:

1. LA 201 NO ES VUELTA DE BATERIA. La 200 lo fue y cerro entera; por la cadencia
   de `AUDITOR.md` 6.1 la bateria vuelve CADA CINCO VUELTAS. Aqui la seccion 9
   cierra con el HUECO DECLARADO Y MEDIDO por su carril. Por eso este bloque NO
   trae el `H.1` de las selladas del 183 ni corre el lanzador: el sujeto de esta
   vuelta es EL PLAN.
2. EL BLOQUE `H` MIDE EL SUJETO DE LA TAREA 1: el acta 200 acotada AQUI, la
   ausencia de `docs/loop/reportes/REPORTE_V198.md` medida con `os.path.exists`,
   y la seccion 8 del reporte que se va a archivar como `REPORTE_V200.md`, que
   es la sede de la correccion de cita de la 1.c. Y mide las palabras de la cita
   sobre los DOS ficheros, que es lo que el encargo dice haber hecho: si esas
   palabras estan en `AUDITOR.md` o solo en el acta 185.
3. EL BLOQUE `H.1` MIDE EL SUJETO DE LAS TAREAS 2, 3 Y 4 ANTES DE TOCAR NADA:
   `docs/plan/INVENTARIO.jsonl` recontado hoy con su reparto por tipo, las
   CUATRO FICHAS REALES de `docs/plan/OPERACIONES.jsonl` con su linea, y los
   CUATRO DOCUMENTOS que la vara nombra, con sus bytes en disco y LF (`P.2`).
4. EL BLOQUE `H.2` CORRE LA VARA DEL TRABAJO PENDIENTE, que es
   `vuelta150_3_relectura_expediente.py --corte <HEAD DE APERTURA>`, y sella su
   salida. La vara NO SE CLONA y NO SE TOCA: se invoca.
5. EL BLOQUE `F` MIDE LA NOMINA CONTRA EL CONGELADO EN 135 que manda
   `AUDITOR.md` 6.3, y mide LAS DOS CIFRAS de arneses fuera de la nomina, con
   vara y sin vara. AQUI NO SE PODA NI SE ANADE NADA: se mide.
6. EL BLOQUE `E` SIGUE CONTANDO LA RACHA DEL INSTRUMENTO, porque de esa cifra
   depende si el tope de sub-tareas es DOS o CINCO (`AUDITOR.md` 6.2).

USO:
  python scripts/loop/vuelta201_apertura.py
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
NL = chr(10)
VUELTA = 201

VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
TURNO = "docs/loop/_TURNO_DEL_AUDITOR.json"
ACTA = "docs/loop/ACTA_AUDITOR.md"

INSTRUMENTO_RACHA = "scripts/loop/vuelta192_racha_de_cierres.py"
SELLADA_RACHA = "docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt"

# LOS SUJETOS DE ESTA VUELTA, medidos y no supuestos.
SEDE_DE_LA_CITA = "docs/loop/REPORTE.md"
REPORTE_AUSENTE = "docs/loop/reportes/REPORTE_V198.md"
INVENTARIO_JSONL = "docs/plan/INVENTARIO.jsonl"
OPERACIONES = "docs/plan/OPERACIONES.jsonl"
FICHAS_REALES = ["OP-L-01", "OP-L-02", "OP-L-03", "OP-I-01"]
DOCUMENTOS_DE_LA_VARA = [
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "docs/INTRA_DOMINIO_INFORME.md",
    "docs/BANCO_DE_TEXTOS.md",
    "docs/plan/BANCO_DEL_PLAN.md",
]
VARA_DEL_PLAN = "scripts/loop/vuelta150_3_relectura_expediente.py"


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env,
                       shell=shell)
    out = (r.stdout.decode("utf-8", errors="replace")
           + r.stderr.decode("utf-8", errors="replace"))
    return r.returncode, out


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def sha_de(rel):
    """LAS DOS CONVENCIONES, MEDIDAS Y NO SUPUESTAS. Devuelve
    (sha_disco, sha_lf, bytes_disco, bytes_lf) o None si el fichero no esta."""
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(ruta):
        return None
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (hashlib.sha256(datos).hexdigest(), hashlib.sha256(lf).hexdigest(),
            len(datos), len(lf))


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V%d_%s_APERTURA.txt" % (VUELTA, nombre))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITO: %s (%d bytes)"
          % (os.path.basename(ruta), len(texto.encode("utf-8"))))


L = []
w = L.append
w("SELLO DE APERTURA DE LA VUELTA %d, escrito ANTES de la primera operacion."
  % VUELTA)
w("regimen: MORATORIA DE MAQUINARIA (AUDITOR.md 6.3, decision del fundador del 7")
w("         sep 2026). NO SE FABRICAN ARNESES, GUARDAS NI LECTORES NUEVOS, y")
w("         esta vuelta NO TIENE NINGUNA EXCEPCION. La nomina queda CONGELADA EN")
w("         135: ni crece ni se poda.")
w("         ESTA NO ES VUELTA DE BATERIA. La 200 lo fue y cerro entera; por la")
w("         cadencia de AUDITOR.md 6.1 la bateria vuelve CADA CINCO VUELTAS. La")
w("         seccion 9 cierra con el HUECO DECLARADO Y MEDIDO por su carril.")
w("         EL TRABAJO ES EL PLAN: las cuatro fichas reales.")
w("         EL TOPE DE SUB-TAREAS LO MANDA LA CIFRA DEL BLOQUE E, contada aqui")
w("         del instrumento. El encargo trae CUATRO sub-tareas.")
w("ESTE BLOQUE CORRE EL CICLO COMPLETO, tsc y pnpm test INCLUIDOS, y escribe el")
w("         mismo los dos literales de la guarda D.1.")
w("")

w("=== A. HEAD DE APERTURA (git rev-parse HEAD, leido y no tecleado) ===")
c, head = git(["rev-parse", "HEAD"])
head = head.strip()
w(head)
c, asunto = git(["log", "-1", "--format=%H%x09%ad%x09%s", "--date=iso"])
w(asunto.strip()[:400])
w("")

w("=== B. RAMA Y REMOTO (leidos de git, no tecleados) ===")
c, rama = git(["rev-parse", "--abbrev-ref", "HEAD"])
w("rama: " + rama.strip())
c, up = git(["rev-parse", "--abbrev-ref", "@{u}"])
w("remoto de seguimiento: " + (up.strip() if c == 0 else "(ninguno)"))
c, ahead = git(["rev-list", "--left-right", "--count", "HEAD...@{u}"])
w("adelante/atras contra el remoto (HEAD...upstream): "
  + (ahead.strip() if c == 0 else "(no medible)"))
w("")

w("=== C. EL ESTADO DEL ARBOL AL ENTRAR, EN LA REDACCION QUE LA GUARDA LEE ===")
w("LOS DOS LITERALES DE ABAJO SON LOS QUE LA GUARDA D.1 DE cerrar_reporte.py")
w("busca por expresion regular. Se escriben AQUI, en el bloque de apertura, para")
w("que la apertura sellada NO haya que tocarla al cierre.")
c, est = git(["status", "--porcelain"])
sucios = [l for l in est.splitlines() if l.strip()]
w("CIFRA lineas de status: %d" % len(sucios))
for l in sucios[:20]:
    w("   " + l)
if not sucios:
    w("   (ninguna: el arbol entra limpio)")
c, numstat = git(["diff", "--numstat", "--", "dataset/"])
lineas_ns = [l for l in numstat.splitlines() if l.strip()]
w("CIFRA filas de `git diff --numstat -- dataset/` AL ENTRAR: %d" % len(lineas_ns))
for l in lineas_ns[:20]:
    w("   " + l)
if not lineas_ns:
    w("   (ninguna: dataset/ entra limpio)")
w("")

w("=== C.0 EL NUMSTAT DE LAS CUATRO SEDES QUE EL ENCARGO PIDE, AL ENTRAR ===")
for sede in ("dataset/", "web/", "engine/", "docs/plan/"):
    c, ns = git(["diff", "HEAD", "--numstat", "--", sede])
    fil = [l for l in ns.splitlines() if l.strip()]
    w("CIFRA filas de numstat AL ENTRAR en %-12s %d" % (sede, len(fil)))
    for l in fil[:10]:
        w("      " + l)
w("")

w("=== C.1 LA CADENA DE LA VUELTA 200 Y SU ACTA, EN GIT ===")
c, logtodo = git(["log", "--format=%h%x09%s", "-40"])
filas = [l.split(chr(9), 1) for l in logtodo.splitlines() if chr(9) in l]
for etiqueta, aguja in (("acta 200", "ACTA DEL AUDITOR, VUELTA 200"),
                        ("cierre de la 200", "VUELTA 200 CERRADA"),
                        ("decision del fundador", "Decision del fundador")):
    hits = [(h, s) for h, s in filas if s.startswith(aguja)]
    w("%-32s %d acierto(s): %s"
      % (etiqueta, len(hits), ", ".join(h for h, _s in hits) or "(ninguno)"))
w("")

w("=== D. LA SEDE DE LOS VEREDICTOS, QUE NO SE PUEDE MOVER EN ESTA VUELTA ===")
m = sha_de(VEREDICTOS)
if m is None:
    w("ROJO: no existe %s" % VEREDICTOS)
else:
    w("%s" % VEREDICTOS)
    w("   disco %d bytes | sha256 disco %s" % (m[2], m[0][:16]))
    w("   LF    %d bytes | sha256 LF    %s" % (m[3], m[1][:16]))
    w("   LAS DOS CONVENCIONES SE PUBLICAN, y el cierre las remide contra estas.")
w("")

w("=== D.1 EL FICHERO DEL TURNO DEL AUDITOR, MEDIDO AL ENTRAR ===")
mt = sha_de(TURNO)
if mt is None:
    w("   NO EXISTE %s al entrar." % TURNO)
else:
    w("   %s" % TURNO)
    w("      disco %d bytes | LF %d bytes | sha256 LF %s"
      % (mt[2], mt[3], mt[1][:16]))
w("")

w("=== E. LA RACHA DE CIERRES, CONTADA DEL INSTRUMENTO Y NO HEREDADA ===")
w("EL NOMBRE SALE DE LA CONSTANTE QUE SE EJECUTA, NO DE LA PROSA.")
racha = None
med_inst = sha_de(INSTRUMENTO_RACHA)
if med_inst is None or med_inst[2] == 0:
    w("ROJO: el instrumento %s NO EXISTE o mide CERO BYTES. NO SE PUBLICA CIFRA."
      % INSTRUMENTO_RACHA)
else:
    w("instrumento: %s" % INSTRUMENTO_RACHA)
    w("   existe y no esta vacio: SI, %d bytes en disco | %d LF | sha256 LF %s"
      % (med_inst[2], med_inst[3], med_inst[1][:16]))
    w("comando: python %s" % INSTRUMENTO_RACHA)
    w("NOTA MEDIDA Y DECLARADA: este instrumento PISA su propia salida sellada")
    w("   %s. Aqui se corre, se lee la cifra, y la" % SELLADA_RACHA)
    w("   sellada se RESTAURA con git checkout -- y se REMIDE.")
    antes = sha_de(SELLADA_RACHA)
    c, salida_racha = correr([PY, INSTRUMENTO_RACHA])
    mrac = re.search(r"CIFRA vueltas CONSECUTIVAS en verde hacia atras:\s*(\d+)",
                     salida_racha)
    mlas = re.search(r"las vueltas de la racha:\s*(.+)", salida_racha)
    racha = mrac.group(1) if mrac else None
    if racha is None:
        w("ROJO: el instrumento no imprime la cifra de la racha. NO SE TECLEA una.")
    else:
        w("CIFRA racha de cierres, contada del inventario ENTERO: %s" % racha)
        w("las vueltas de la racha: %s"
          % (mlas.group(1).strip() if mlas else "(no impresa)"))
        if int(racha) >= 2:
            w("   CON RACHA %s EL REGIMEN TEMPORAL SE APAGA Y VUELVE EL TOPE DE"
              % racha)
            w("   CINCO. El encargo trae CUATRO sub-tareas, que cabe.")
        else:
            w("   CON RACHA %s EL TOPE SIGUE SIENDO DE DOS SUB-TAREAS, y el"
              % racha)
            w("   encargo trae CUATRO, QUE NO CABE, y eso se declara en vez de")
            w("   ajustarse.")
    w("nuevo corte, medido antes de restaurar:")
    despues = sha_de(SELLADA_RACHA)
    if despues:
        w("   %d bytes LF | sha256 LF %s" % (despues[3], despues[1][:16]))
    git(["checkout", "--", SELLADA_RACHA])
    rest = sha_de(SELLADA_RACHA)
    if antes and rest:
        w("SELLADA ANTES:     %d bytes LF | sha256 LF %s"
          % (antes[3], antes[1][:16]))
        w("SELLADA RESTAURADA:%d bytes LF | sha256 LF %s"
          % (rest[3], rest[1][:16]))
        w("RESTAURADA IDENTICA A LA SELLADA DE ENTRADA: %s"
          % ("SI" if antes[1] == rest[1] else "NO"))
w("")

w("=== E.1 EL INVENTARIO DE CIERRES SELLADOS, CONTADO DE DISCO ===")
cierres = sorted(n for n in os.listdir(LOOP)
                 if re.match(r"^SALIDA_V\d+_CERRAR_REPORTE\.txt$", n))
w("CIFRA ficheros SALIDA_V*_CERRAR_REPORTE.txt en docs/loop/: %d" % len(cierres))
nums = sorted(int(re.match(r"^SALIDA_V(\d+)_", n).group(1)) for n in cierres)
w("las vueltas con sellada de cierre: %s" % ", ".join(str(n) for n in nums))
if nums:
    faltan_c = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
    w("CIFRA vueltas del rango %d a %d SIN sellada: %d"
      % (min(nums), max(nums), len(faltan_c)))
    w("   cuales: %s" % (", ".join(str(n) for n in faltan_c) or "(ninguna)"))
w("CIFRA sellada de cierre de la vuelta %d al entrar: %d"
  % (VUELTA, 1 if VUELTA in nums else 0))
w("")

w("=== F. LA NOMINA Y EL CENSO AL ENTRAR, CONTRA EL CONGELADO EN 135 ===")
w("AQUI NO SE TOCA NADA: se MIDE. AUDITOR.md 6.3 congela la nomina en 135: NI")
w("   CRECE NI SE PODA. Si la cifra medida no es 135, SE DECLARA la discrepancia")
w("   en vez de ajustarla.")
w("LA CIFRA DE FUERA DE LA NOMINA VIAJA CON SU VARA Y SE MIDEN LAS DOS")
w("   (adjudicacion 4.7 del acta 197).")
try:
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_mutaciones_viejas as VMV   # noqa: E402
    w("CIFRA entradas de la nomina, leidas de VMV.VIEJAS: %d" % len(VMV.VIEJAS))
    w("CONGELADO QUE MANDA AUDITOR.md 6.3: 135")
    w("CALZA LA NOMINA CON EL CONGELADO: %s"
      % ("SI" if len(VMV.VIEJAS) == 135 else
         "NO, y se declara: medida %d contra congelado 135" % len(VMV.VIEJAS)))
    w("CIFRA casos declarados: %d" % len(VMV.CASOS_DECLARADOS))
    censo = VMV.arneses_del_directorio()
    w("CIFRA arneses que el censo reconoce en scripts/loop/: %d" % len(censo))
    w("LA VARA DEL CENSO, que es la que decide (vuelta 178, TAREA 1.b): %d"
      % VMV.VARA_DEL_CENSO)
    ultima, faltan_n = VMV.arneses_que_faltan()
    w("CIFRA ultima vuelta representada en la nomina (INFORMATIVA): %s" % ultima)
    w("CIFRA arneses del censo FUERA de la nomina CON LA VARA %d: %d"
      % (VMV.VARA_DEL_CENSO, len(faltan_n)))
    for n in faltan_n:
        w("      FUERA DE LA NOMINA (con vara %d): %s" % (VMV.VARA_DEL_CENSO, n))
    if not faltan_n:
        w("      (ninguno)")
    _u2, faltan_sin = VMV.arneses_que_faltan(vara=0)
    w("CIFRA arneses del censo FUERA de la nomina SIN VARA (vara=0): %d"
      % len(faltan_sin))
    w("   LAS DOS CIFRAS JUNTAS SON LA FRASE ENTERA: con vara %d salen %d, sin"
      % (VMV.VARA_DEL_CENSO, len(faltan_n)))
    w("   vara salen %d." % len(faltan_sin))
    invisibles = VMV.nomina_invisible_al_censo()
    w("CIFRA entradas de la nomina que el censo NO VE: %d" % len(invisibles))
    for n in invisibles:
        w("      INVISIBLE AL CENSO: %s" % n)
    informe = VMV.guarda_del_sujeto_congelado()
    w("CIFRA entradas SIN SUJETO CONGELADO, leidas de")
    w("   guarda_del_sujeto_congelado(): %d" % len(informe))
    for fila in informe:
        w("      SIN SUJETO CONGELADO: %s" % (fila,))
except Exception as e:                                   # noqa: BLE001
    w("NO SE PUDO LEER LA NOMINA: %r" % (e,))
w("")

w("=== G. EL NUMERO DE LA SERIE, COMPUTADO Y NO TECLEADO ===")
w("comando: python scripts/loop/serie_de_registros.py")
c, salida_serie = correr([PY, "scripts/loop/serie_de_registros.py"])
io.open(os.path.join(LOOP, "SALIDA_V%d_SERIE_APERTURA.txt" % VUELTA), "w",
        encoding="utf-8", newline=NL).write(salida_serie)
mser = re.search(r"SIGUIENTE LIBRE:\s*(R\.\d+)", salida_serie)
mcol = re.search(r"CIFRA colisiones \(un numero escrito mas de una vez\):\s*(\d+)",
                 salida_serie)
mtot = re.search(r"CIFRA entradas en total:\s*(\d+)", salida_serie)
w("SIGUIENTE LIBRE de la serie: %s" % (mser.group(1) if mser else "(no impreso)"))
w("CIFRA entradas en total: %s" % (mtot.group(1) if mtot else "(no impresa)"))
w("CIFRA colisiones: %s" % (mcol.group(1) if mcol else "(no impresa)"))
w("EL ENCARGO DICE QUE HOY EL SIGUIENTE LIBRE ES R.61 Y MANDA VOLVER A CORRERLO.")
w("   CALZA LO CORRIDO CON LO QUE EL ENCARGO DICE: %s"
  % ("SI" if (mser and mser.group(1) == "R.61") else "NO, y se declara"))
w("")

w("=== H. EL SUJETO DE LA TAREA 1: EL ACTA 200, LA AUSENCIA DE LA 198 Y LA ===")
w("    SEDE DE LA CORRECCION DE CITA")
ma = sha_de(ACTA)
if ma is None:
    w("ROJO: no existe %s" % ACTA)
else:
    w("%s: %d bytes disco | %d bytes LF | sha256 LF %s"
      % (ACTA, ma[2], ma[3], ma[1][:16]))
    ruta_acta = os.path.join(RAIZ, ACTA.replace("/", os.sep))
    lineas_acta = io.open(ruta_acta, encoding="utf-8",
                          errors="replace").read().split(NL)
    w("CIFRA lineas del acta por split(NL): %d" % len(lineas_acta))
    for v in (198, 199, 200, 201):
        hits = [i + 1 for i, l in enumerate(lineas_acta)
                if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA %d\b" % v, l)]
        w("cabecera de la VUELTA %d: %d acierto(s), linea(s) %s"
          % (v, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
    ini = [i for i, l in enumerate(lineas_acta)
           if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA 200\b", l)]
    if len(ini) == 1:
        i0 = ini[0]
        sig = [i for i, l in enumerate(lineas_acta)
               if i > i0 and re.match(r"^#\s+ACTA\b", l)]
        i1 = sig[0] if sig else len(lineas_acta)
        w("CUERPO ACOTADO del acta 200: lineas %d a %d (1-indexadas), %d lineas"
          % (i0 + 1, i1, i1 - i0))
        w("   la de arriba es LA COTA QUE MANDA en esta vuelta, computada aqui")
        w("   sobre el fichero y no tecleada del encargo.")
        for etiqueta, aguja in (("4.1", r"^#{2,4}\s*4\.1\b"),
                                ("4.2", r"^#{2,4}\s*4\.2\b"),
                                ("4.7", r"^#{2,4}\s*4\.7\b")):
            hh = [j + 1 for j in range(i0, i1)
                  if re.match(aguja, lineas_acta[j])]
            w("   adjudicacion %s del acta 200: %d acierto(s), linea(s) %s"
              % (etiqueta, len(hh),
                 ", ".join(str(x) for x in hh) or "(ninguna)"))
    else:
        w("ROJO: la cabecera del acta 200 no aparece exactamente una vez. NO SE")
        w("   ACOTA A OJO.")
w("")
w("LA AUSENCIA DE LA 198, MEDIDA CON os.path.exists Y NO RECORDADA (TAREA 1.b):")
ruta_198 = os.path.join(RAIZ, REPORTE_AUSENTE.replace("/", os.sep))
w("   %s existe: %s" % (REPORTE_AUSENTE, "SI" if os.path.isfile(ruta_198) else "NO"))
m198 = sha_de(REPORTE_AUSENTE)
w("   bytes medidos: %s"
  % ("%d disco | %d LF" % (m198[2], m198[3]) if m198 else
     "NINGUNO, y el cero sale de que NO HAY FICHERO, no de medir uno"))
dir_rep = os.path.join(LOOP, "reportes")
archivados = sorted(n for n in os.listdir(dir_rep)
                    if re.match(r"^REPORTE_V\d+\.md$", n))
nums_rep = sorted(int(re.match(r"^REPORTE_V(\d+)\.md$", n).group(1))
                  for n in archivados)
w("   CIFRA reportes archivados en docs/loop/reportes/: %d" % len(archivados))
w("   rango %d a %d" % (min(nums_rep), max(nums_rep)))
faltan_rep = [n for n in range(min(nums_rep), max(nums_rep) + 1)
              if n not in nums_rep]
w("   CIFRA vueltas del rango SIN reporte archivado: %d" % len(faltan_rep))
w("      cuales: %s" % (", ".join(str(n) for n in faltan_rep) or "(ninguna)"))
w("")
w("LA SEDE DE LA CORRECCION DE CITA (TAREA 1.c), MEDIDA AL ENTRAR. Al entrar, el")
w("   reporte de la 200 todavia vive en docs/loop/REPORTE.md; el esqueleto de")
w("   esta vuelta lo ARCHIVA en docs/loop/reportes/REPORTE_V200.md antes de")
w("   pisarlo, y ESA es la sede donde la correccion de cita se escribe.")
msede = sha_de(SEDE_DE_LA_CITA)
if msede is None:
    w("   ROJO: NO EXISTE %s" % SEDE_DE_LA_CITA)
else:
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (SEDE_DE_LA_CITA, msede[2], msede[3], msede[1][:16]))
    ruta_sede = os.path.join(RAIZ, SEDE_DE_LA_CITA.replace("/", os.sep))
    t_sede = io.open(ruta_sede, encoding="utf-8", errors="replace").read()
    l_sede = t_sede.split(NL)
    w("   CIFRA lineas por split(NL): %d | CIFRA lineas por count(NL): %d"
      % (len(l_sede), t_sede.count(NL)))
    hs8 = [i + 1 for i, l in enumerate(l_sede) if re.match(r"^##\s*8\b", l)]
    w("   cabecera de la seccion 8: %d acierto(s), linea(s) %s"
      % (len(hs8), ", ".join(str(x) for x in hs8) or "(ninguna)"))
    for etiqueta, aguja in (
            ("la palabra PARADA", "PARADA"),
            ("la mencion de AUDITOR.md 0", "AUDITOR.md` 0"),
            ("la frase 'se corrige es la guarda'", "se corrige es la guarda"),
            ("la mencion del acta 185", "acta 185")):
        hits = [i + 1 for i, l in enumerate(l_sede) if aguja in l]
        w("   %-42s %d linea(s): %s"
          % (etiqueta, len(hits),
             ", ".join(str(h) for h in hits[:14]) or "(ninguna)"))
w("")
w("LA CITA DE LA 1.c, MEDIDA SOBRE LOS DOS FICHEROS Y NO SUPUESTA. El encargo")
w("   dice que las palabras 'cuando una guarda contradice una decision escrita")
w("   del fundador, la que se corrige es la guarda' NO estan en AUDITOR.md y SI")
w("   en el acta 185 punto 6.2. AQUI SE COMPRUEBA, no se cree.")
for fichero in (ACTA, "docs/loop/AUDITOR.md"):
    ruta_f = os.path.join(RAIZ, fichero.replace("/", os.sep))
    if not os.path.isfile(ruta_f):
        w("   %s: NO EXISTE" % fichero)
        continue
    lf = io.open(ruta_f, encoding="utf-8", errors="replace").read().split(NL)
    for aguja in ("se corrige es la guarda", "contradice una decision escrita",
                  "contradice una decision"):
        hits = [i + 1 for i, l in enumerate(lf) if aguja in l]
        w("   %-24s | %-34s %d linea(s): %s"
          % (os.path.basename(fichero), aguja, len(hits),
             ", ".join(str(h) for h in hits[:10]) or "(ninguna)"))
ruta_acta2 = os.path.join(RAIZ, ACTA.replace("/", os.sep))
la = io.open(ruta_acta2, encoding="utf-8", errors="replace").read().split(NL)
i185 = [i for i, l in enumerate(la)
        if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA 185\b", l)]
w("   cabecera del acta 185: %d acierto(s), linea(s) %s"
  % (len(i185), ", ".join(str(x + 1) for x in i185) or "(ninguna)"))
if len(i185) == 1:
    j0 = i185[0]
    sg = [i for i, l in enumerate(la) if i > j0 and re.match(r"^#\s+ACTA\b", l)]
    j1 = sg[0] if sg else len(la)
    hh = [j + 1 for j in range(j0, j1) if re.match(r"^#{2,4}\s*6\.2\b", la[j])]
    w("   punto 6.2 DENTRO del acta 185 (lineas %d a %d): %d acierto(s), %s"
      % (j0 + 1, j1, len(hh), ", ".join(str(x) for x in hh) or "(ninguna)"))
w("")

w("=== H.1 EL SUJETO DE LAS TAREAS 2, 3 Y 4: EL INVENTARIO, LAS CUATRO ===")
w("    FICHAS REALES Y LOS CUATRO DOCUMENTOS, MEDIDOS ANTES DE TOCAR NADA")
minv = sha_de(INVENTARIO_JSONL)
if minv is None:
    w("   ROJO: NO EXISTE %s" % INVENTARIO_JSONL)
else:
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (INVENTARIO_JSONL, minv[2], minv[3], minv[1][:16]))
    ruta_inv = os.path.join(RAIZ, INVENTARIO_JSONL.replace("/", os.sep))
    t_inv = io.open(ruta_inv, encoding="utf-8", errors="replace").read()
    l_inv = [l for l in t_inv.split(NL) if l.strip()]
    w("   CIFRA lineas NO VACIAS (las entradas): %d" % len(l_inv))
    w("   CIFRA lineas por split(NL): %d | por count(NL): %d"
      % (len(t_inv.split(NL)), t_inv.count(NL)))
    w("   CIFRA acaba en salto de linea: %s"
      % ("SI" if t_inv.endswith(NL) else "NO"))
    malas = 0
    por_tipo = {}
    claves = {}
    for l in l_inv:
        try:
            d = json.loads(l)
        except Exception:                                # noqa: BLE001
            malas += 1
            continue
        for k in d:
            claves[k] = claves.get(k, 0) + 1
        t = d.get("tipo", "(sin campo tipo)")
        por_tipo[t] = por_tipo.get(t, 0) + 1
    w("   CIFRA lineas que NO son JSON valido: %d" % malas)
    w("   EL REPARTO POR TIPO, RECONTADO HOY Y NO HEREDADO:")
    for t in sorted(por_tipo, key=lambda x: (-por_tipo[x], str(x))):
        w("      %-40s %d" % (t, por_tipo[t]))
    w("   SUMA DEL REPARTO: %d" % sum(por_tipo.values()))
    w("   CIFRA claves distintas en las entradas: %d" % len(claves))
    w("      %s" % ", ".join("%s=%d" % (k, claves[k]) for k in sorted(claves)))
w("")
w("   LAS CUATRO FICHAS REALES, LOCALIZADAS POR LINEA EN %s:" % OPERACIONES)
mops = sha_de(OPERACIONES)
if mops is None:
    w("   ROJO: NO EXISTE %s" % OPERACIONES)
else:
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (OPERACIONES, mops[2], mops[3], mops[1][:16]))
    ruta_ops = os.path.join(RAIZ, OPERACIONES.replace("/", os.sep))
    lin_ops = io.open(ruta_ops, encoding="utf-8",
                      errors="replace").read().split(NL)
    w("   CIFRA lineas NO VACIAS de OPERACIONES.jsonl: %d"
      % len([l for l in lin_ops if l.strip()]))
    for idop in FICHAS_REALES:
        aguja = chr(34) + "id_op" + chr(34) + ": " + chr(34) + idop + chr(34)
        hits = [i + 1 for i, l in enumerate(lin_ops)
                if l.strip() and aguja in l]
        w("      %-9s %d linea(s): %s"
          % (idop, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
        if len(hits) == 1:
            d = json.loads(lin_ops[hits[0] - 1])
            ver = d.get("verificacion", [])
            ev = d.get("evidencia", [])
            w("         estado=%r  tipo=%r  fase=%r"
              % (d.get("estado"), d.get("tipo"), d.get("fase")))
            w("         CIFRA elementos de `verificacion`: %d" % len(ver))
            w("         CIFRA elementos de `evidencia`: %d" % len(ev))
            w("         CIFRA elementos de `evidencia` con mencion de fichero: "
              "%d"
              % len([x for x in ev
                     if re.search(r"[A-Za-z0-9_/.-]+\.(md|jsonl|py|json|txt)",
                                  str(x))]))
w("")
w("   LOS CUATRO DOCUMENTOS QUE LA VARA NOMBRA, EN BYTES EXACTOS (P.2):")
for doc in DOCUMENTOS_DE_LA_VARA:
    md = sha_de(doc)
    if md is None:
        w("      %-38s NO EXISTE EN DISCO" % doc)
        continue
    ruta_d = os.path.join(RAIZ, doc.replace("/", os.sep))
    td = io.open(ruta_d, encoding="utf-8", errors="replace").read()
    w("      %-38s disco %8d bytes | LF %8d bytes | sha256 LF %s | %d lineas "
      "por count(NL)" % (doc, md[2], md[3], md[1][:16], td.count(NL)))
w("")

w("=== H.2 LA VARA DEL TRABAJO PENDIENTE, CORRIDA AQUI CON EL HEAD DE ===")
w("    APERTURA COMO CORTE. LA VARA NO SE CLONA Y NO SE TOCA: SE INVOCA.")
mv = sha_de(VARA_DEL_PLAN)
if mv is None or mv[2] == 0:
    w("   ROJO: la vara %s NO EXISTE o mide CERO BYTES." % VARA_DEL_PLAN)
else:
    w("   vara: %s" % VARA_DEL_PLAN)
    w("      %d bytes disco | %d LF | sha256 LF %s" % (mv[2], mv[3], mv[1][:16]))
    w("   comando: python %s --corte %s" % (VARA_DEL_PLAN, head[:8]))
    c_v, sal_vara = correr([PY, VARA_DEL_PLAN, "--corte", head])
    io.open(os.path.join(LOOP, "SALIDA_V%d_VARA_DEL_PLAN.txt" % VUELTA), "w",
            encoding="utf-8", newline=NL).write(sal_vara)
    w("   exitcode: %d" % c_v)
    w("   sellada en docs/loop/SALIDA_V%d_VARA_DEL_PLAN.txt (%d bytes)"
      % (VUELTA, len(sal_vara.encode("utf-8"))))
    for l in sal_vara.split(NL):
        if l.strip().startswith("CIFRA"):
            w("   | " + l.strip()[:150])
w("")

w("=== I. EL INVENTARIO DE SELLADAS DE BATERIA, CONTADO DE DISCO ===")
w("ESTA VUELTA NO CORRE LA BATERIA (cadencia de AUDITOR.md 6.1). Se cuenta lo")
w("   que hay para que el HUECO de la seccion 9 se declare CON MEDICION.")
selladas = sorted(n for n in os.listdir(LOOP)
                  if re.match(r"^SALIDA_V\d+_BATERIA_TRAMO_\d+\.txt$", n))
w("CIFRA ficheros SALIDA_V*_BATERIA_TRAMO_N.txt en docs/loop/: %d" % len(selladas))
por_vuelta = {}
for n in selladas:
    v = re.match(r"^SALIDA_V(\d+)_", n).group(1)
    por_vuelta.setdefault(v, []).append(n)
for v in sorted(por_vuelta, key=int):
    w("   V%s: %d fichero(s)" % (v, len(por_vuelta[v])))
compuestas = sorted(n for n in os.listdir(LOOP)
                    if re.match(r"^SALIDA_V\d+_BATERIA\.txt$", n))
w("CIFRA salidas unicas SALIDA_V*_BATERIA.txt en docs/loop/: %d" % len(compuestas))
for n in compuestas:
    mm = sha_de("docs/loop/" + n)
    w("   %-28s disco %8d bytes | LF %8d bytes" % (n, mm[2], mm[3]))
w("CIFRA ficheros SALIDA_V%d_BATERIA_TRAMO_N.txt al entrar: %d"
  % (VUELTA, len([n for n in os.listdir(LOOP)
                  if re.match(r"^SALIDA_V%d_BATERIA_TRAMO_\d+\.txt$" % VUELTA, n)])))
w("CIFRA docs/loop/SALIDA_V%d_BATERIA.txt existe al entrar: %s"
  % (VUELTA, "SI" if os.path.isfile(
      os.path.join(LOOP, "SALIDA_V%d_BATERIA.txt" % VUELTA)) else "NO"))
w("")

w("FIN DEL SELLO DE APERTURA")

texto = NL.join(L) + NL
io.open(os.path.join(LOOP, "SALIDA_V%d_APERTURA.txt" % VUELTA), "w",
        encoding="utf-8", newline=NL).write(texto)
print(texto)
escribir("HEAD", head + NL)

# ------------------------------------------------- EL BLOQUE DE MEDICIONES
c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
escribir("GATE0_CMD1", o + NL + "EXITCODE: %d" % c + NL)

c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
escribir("CICLO_ETIQUETAS", o + NL + "EXITCODE: %d" % c + NL)

c, o = correr([PY, "scripts/sync_assets_web.py"])
escribir("CICLO_SYNC", o + NL + "EXITCODE: %d" % c + NL)

c, o = correr(["git", "diff", "HEAD", "--numstat", "--", "dataset/", "web/",
               "engine/"])
escribir("CICLO_NUMSTAT", o + NL + "EXITCODE: %d" % c + NL)

c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
escribir("CONTEO", o + NL + "EXITCODE: %d" % c + NL)

c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + NL + "EXITCODE: %d" % c + NL)

c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + NL + "EXITCODE: %d" % c + NL)

c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True,
              cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d" % c + NL)

c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + NL + "EXITCODE: %d" % c + NL)

print("BLOQUE DE APERTURA COMPLETO, CICLO ENTERO INCLUIDO tsc Y pnpm test")
