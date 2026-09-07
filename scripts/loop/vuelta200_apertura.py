# -*- coding: utf-8 -*-
r"""vuelta200_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 200, CORRIDO ANTES
DE LA PRIMERA OPERACION.

CLON DECLARADO de `scripts/loop/vuelta199_apertura.py`, que a su vez viene de la
197, la 196 y la 195. Lo que cambia se dice aqui y no se esconde:

1. LA VUELTA ES LA 200 Y ES VUELTA DE BATERIA. `AUDITOR.md` 6.1 dice que NO
   LLEVA NADA MAS. El encargo trae DOS tareas y la segunda es la bateria.
2. EL BLOQUE `H` MIDE EL SUJETO DE LA TAREA 1: el acta 199 acotada con grep -n
   aqui, el reporte de la 199 que es la SEDE de las tres correcciones de cifra,
   y `docs/plan/10_INVENTARIO.md` con sus dos conteos del literal `HUECO` (el
   sensible a mayusculas y el que no lo es) y sus lineas por los DOS caminos,
   que es justo lo que las caidas `C.2` y `C.3` del acta 199 levantan.
3. EL BLOQUE `H.1` MIDE EL SUJETO DE LA TAREA 2 ANTES DE TOCAR NADA: las NUEVE
   salidas selladas `SALIDA_V183_BATERIA_TRAMO_N.txt` que la corrida de la
   vuelta 183 dejo, con sus bytes y su `sha256`, y corre `--plan` y `--siguiente`
   del lanzador para dejar MEDIDA la trampa que el acta 199 nombra en su
   hallazgo `5.2`.
4. EL BLOQUE `F` MIDE LA NOMINA CONTRA EL CONGELADO EN 135 que manda
   `AUDITOR.md` 6.3, y mide LAS DOS CIFRAS de arneses fuera de la nomina, con
   vara 148 y sin vara. ESA MEDICION ES LA DE LA CAIDA `C.1` DEL ACTA 199, y se
   toma AQUI para que la TAREA 1.a no elija su cifra despues de mirar.
5. EL BLOQUE `E` SIGUE CONTANDO LA RACHA DEL INSTRUMENTO, porque de esa cifra
   depende si el tope de sub-tareas es DOS o CINCO (`AUDITOR.md` 6.2).

USO:
  python scripts/loop/vuelta200_apertura.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
NL = chr(10)
VUELTA = 200

VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
TURNO = "docs/loop/_TURNO_DEL_AUDITOR.json"
ACTA = "docs/loop/ACTA_AUDITOR.md"

INSTRUMENTO_RACHA = "scripts/loop/vuelta192_racha_de_cierres.py"
SELLADA_RACHA = "docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt"

# LOS SUJETOS DE ESTA VUELTA, medidos y no supuestos.
SEDE_DE_LAS_CORRECCIONES = "docs/loop/REPORTE.md"
INVENTARIO = "docs/plan/10_INVENTARIO.md"
LANZADOR_BATERIA = "scripts/loop/vuelta183_bateria_por_tramos.py"
VUELTA_DEL_LANZADOR = 183


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
w("         esta vuelta NO TIENE NINGUNA EXCEPCION: las dos de la 199 se")
w("         consumieron. La nomina queda CONGELADA EN 135.")
w("         ESTA ES VUELTA DE BATERIA. AUDITOR.md 6.1 dice que NO LLEVA NADA")
w("         MAS: la bateria entera, su doble corrida, su reloj y su salida")
w("         sellada. El encargo trae DOS tareas y la segunda es la bateria.")
w("         EL TOPE DE SUB-TAREAS LO MANDA LA CIFRA DEL BLOQUE E, contada aqui")
w("         del instrumento. El encargo trae DOS sub-tareas.")
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

w("=== C.1 LA CADENA DE LA VUELTA 199 Y SU ACTA, EN GIT ===")
c, logtodo = git(["log", "--format=%h%x09%s", "-40"])
filas = [l.split(chr(9), 1) for l in logtodo.splitlines() if chr(9) in l]
for etiqueta, aguja in (("acta 199", "ACTA DEL AUDITOR, VUELTA 199"),
                        ("cierre de la 199", "VUELTA 199 CERRADA"),
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
            w("   CINCO. El encargo trae DOS sub-tareas, que cabe.")
        else:
            w("   CON RACHA %s EL TOPE SIGUE SIENDO DE DOS SUB-TAREAS, y el"
              % racha)
            w("   encargo trae DOS, que tambien cabe.")
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
w("ESTA ES LA MEDICION DE LA CAIDA C.1 DEL ACTA 199, Y SE TOMA AQUI PARA QUE LA")
w("   TAREA 1.a NO ELIJA SU CIFRA DESPUES DE MIRAR. La cifra viaja con su vara y")
w("   se miden LAS DOS (adjudicacion 4.7 del acta 197).")
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
mser = re.search(r"SIGUIENTE LIBRE:\s*(R\.\d+)", salida_serie)
mcol = re.search(r"CIFRA colisiones \(un numero escrito mas de una vez\):\s*(\d+)",
                 salida_serie)
mtot = re.search(r"CIFRA entradas en total:\s*(\d+)", salida_serie)
w("SIGUIENTE LIBRE de la serie: %s" % (mser.group(1) if mser else "(no impreso)"))
w("CIFRA entradas en total: %s" % (mtot.group(1) if mtot else "(no impresa)"))
w("CIFRA colisiones: %s" % (mcol.group(1) if mcol else "(no impresa)"))
w("")

w("=== H. EL SUJETO DE LA TAREA 1: EL ACTA 199 Y LA SEDE DE LAS TRES ===")
w("    CORRECCIONES DE CIFRA")
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
    for v in (198, 199, 200):
        hits = [i + 1 for i, l in enumerate(lineas_acta)
                if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA %d\b" % v, l)]
        w("cabecera de la VUELTA %d: %d acierto(s), linea(s) %s"
          % (v, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
    ini = [i for i, l in enumerate(lineas_acta)
           if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA 199\b", l)]
    if len(ini) == 1:
        i0 = ini[0]
        sig = [i for i, l in enumerate(lineas_acta)
               if i > i0 and re.match(r"^#\s+ACTA\b", l)]
        i1 = sig[0] if sig else len(lineas_acta)
        w("CUERPO ACOTADO del acta 199: lineas %d a %d (1-indexadas), %d lineas"
          % (i0 + 1, i1, i1 - i0))
        w("   la de arriba es LA COTA QUE MANDA en esta vuelta. El encargo cita")
        w("   69878 a 70229. CALZA EL PRINCIPIO CON EL ENCARGO: %s"
          % ("SI" if (i0 + 1) == 69878 else "NO, y se declara"))
        w("   CALZA EL FINAL CON EL ENCARGO: %s"
          % ("SI" if i1 == 70229 else "NO, y se declara: hoy sale %d" % i1))
    else:
        w("ROJO: la cabecera del acta 199 no aparece exactamente una vez. NO SE")
        w("   ACOTA A OJO.")
w("")
w("LA SEDE DE LAS TRES CORRECCIONES, MEDIDA AL ENTRAR. Al entrar, el reporte de")
w("   la 199 todavia vive en docs/loop/REPORTE.md; el esqueleto de esta vuelta lo")
w("   ARCHIVA en docs/loop/reportes/REPORTE_V199.md antes de pisarlo, y ESA es la")
w("   sede donde las tres correcciones se escriben.")
msede = sha_de(SEDE_DE_LAS_CORRECCIONES)
if msede is None:
    w("   ROJO: NO EXISTE %s" % SEDE_DE_LAS_CORRECCIONES)
else:
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (SEDE_DE_LAS_CORRECCIONES, msede[2], msede[3], msede[1][:16]))
    ruta_sede = os.path.join(RAIZ, SEDE_DE_LAS_CORRECCIONES.replace("/", os.sep))
    t_sede = io.open(ruta_sede, encoding="utf-8", errors="replace").read()
    l_sede = t_sede.split(NL)
    w("   CIFRA lineas por split(NL): %d | CIFRA lineas por count(NL): %d"
      % (len(l_sede), t_sede.count(NL)))
    for etiqueta, aguja in (
            ("C.1, la frase del arnes fuera de la nomina", "arnes del censo"),
            ("C.1, el 61 sin vara", "sin vara salen 61"),
            ("C.2, el literal HUECO", "HUECO"),
            ("C.3, el 414", "414")):
        hits = [i + 1 for i, l in enumerate(l_sede) if aguja in l]
        w("   %-46s %d linea(s): %s"
          % (etiqueta, len(hits),
             ", ".join(str(h) for h in hits[:12]) or "(ninguna)"))
w("")
w("EL FICHERO QUE LAS CAIDAS C.2 Y C.3 MIDEN, CONTADO AQUI POR LOS DOS CAMINOS")
w("   QUE EL ACTA 199 DISTINGUE. La C.2 dice que el literal HUECO sale 3 y no 4,")
w("   y que el 4 es el conteo INSENSIBLE a mayusculas. La C.3 dice 413 lineas y")
w("   no 414, y que el 414 sale de split() sobre un fichero que acaba en salto.")
minv = sha_de(INVENTARIO)
if minv is None:
    w("   ROJO: NO EXISTE %s" % INVENTARIO)
else:
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (INVENTARIO, minv[2], minv[3], minv[1][:16]))
    ruta_inv = os.path.join(RAIZ, INVENTARIO.replace("/", os.sep))
    t_inv = io.open(ruta_inv, encoding="utf-8", errors="replace").read()
    l_inv = t_inv.split(NL)
    w("   CIFRA lineas por split(NL) (el camino del 414): %d" % len(l_inv))
    w("   CIFRA lineas por count(NL) (el camino del 413): %d" % t_inv.count(NL))
    w("   CIFRA acaba en salto de linea: %s"
      % ("SI" if t_inv.endswith(NL) else "NO"))
    sens = [i + 1 for i, l in enumerate(l_inv) if "HUECO" in l]
    insens = [i + 1 for i, l in enumerate(l_inv) if "hueco" in l.lower()]
    w("   CIFRA lineas con el literal HUECO, SENSIBLE a mayusculas: %d" % len(sens))
    w("      lineas: %s" % ", ".join(str(x) for x in sens))
    w("   CIFRA lineas con hueco, INSENSIBLE a mayusculas: %d" % len(insens))
    w("      lineas: %s" % ", ".join(str(x) for x in insens))
    w("   CIFRA apariciones del literal HUECO (no lineas, apariciones): %d"
      % t_inv.count("HUECO"))
    prov = [i + 1 for i, l in enumerate(l_inv) if "PROVISIONAL" in l]
    w("   CIFRA lineas con PROVISIONAL: %d, lineas %s"
      % (len(prov), ", ".join(str(x) for x in prov) or "(ninguna)"))
w("")

w("=== H.1 EL SUJETO DE LA TAREA 2: LAS NUEVE SELLADAS DEL 183, MEDIDAS ===")
w("    ANTES DE TOCAR NADA")
w("EL ACTA 199, HALLAZGO 5.2, DICE QUE ESTE LANZADOR LE VA A MENTIR A ESTA")
w("   VUELTA: computa su vuelta de su propio nombre de fichero, no admite")
w("   --vuelta, y escribe siempre SALIDA_V183_BATERIA_TRAMO_N.txt. Sus NUEVE")
w("   salidas selladas son DE LA CORRIDA DE LA 183 y correr el tramo 1 las PISA.")
w("   AQUI SE MIDEN ENTERAS, con bytes y sha256, ANTES de tocar nada, que es la")
w("   mitad del remedio que el encargo manda.")
mlan = sha_de(LANZADOR_BATERIA)
if mlan is None:
    w("   ROJO: NO EXISTE %s" % LANZADOR_BATERIA)
else:
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (LANZADOR_BATERIA, mlan[2], mlan[3], mlan[1][:16]))
selladas_183 = sorted(
    (n for n in os.listdir(LOOP)
     if re.match(r"^SALIDA_V%d_BATERIA_TRAMO_\d+\.txt$" % VUELTA_DEL_LANZADOR, n)),
    key=lambda n: int(re.search(r"TRAMO_(\d+)", n).group(1)))
w("   CIFRA salidas selladas SALIDA_V%d_BATERIA_TRAMO_N.txt al entrar: %d"
  % (VUELTA_DEL_LANZADOR, len(selladas_183)))
for n in selladas_183:
    mm = sha_de("docs/loop/" + n)
    w("      %-34s disco %8d bytes | LF %8d bytes | sha256 LF %s"
      % (n, mm[2], mm[3], mm[1][:16]))
    c_q, quien = git(["log", "-1", "--format=%h %s", "--", "docs/loop/" + n])
    w("         ultimo commit que lo toca: %s" % quien.strip()[:120])
w("   CIFRA salidas selladas SALIDA_V%d_BATERIA_TRAMO_N.txt al entrar: %d"
  % (VUELTA, len([n for n in os.listdir(LOOP)
                  if re.match(r"^SALIDA_V%d_BATERIA_TRAMO_\d+\.txt$" % VUELTA, n)])))
w("")
w("   EL REPARTO Y LA TRAMPA, CORRIDOS AQUI Y NO RECORDADOS:")
c_p, sal_plan = correr([PY, LANZADOR_BATERIA, "--plan"])
io.open(os.path.join(LOOP, "SALIDA_V%d_T2_PLAN_APERTURA.txt" % VUELTA), "w",
        encoding="utf-8", newline=NL).write(sal_plan)
mtr = re.search(r"CIFRA tramos:\s*(\d+)", sal_plan)
mno = re.search(r"CIFRA entradas de la nomina:\s*(\d+)", sal_plan)
w("   comando: python %s --plan  (exitcode %d)" % (LANZADOR_BATERIA, c_p))
w("   CIFRA tramos del reparto, COMPUTADA HOY: %s"
  % (mtr.group(1) if mtr else "(no impresa)"))
w("   CIFRA entradas de la nomina segun --plan: %s"
  % (mno.group(1) if mno else "(no impresa)"))
w("   AUDITOR.md 6.1 DICE NUEVE TRAMOS Y HOY SALEN %s: es el hallazgo 5.3 del"
  % (mtr.group(1) if mtr else "?"))
w("   acta 199, una cifra de la doctrina que envejecio. NO se toca AUDITOR.md,")
w("   que es del fundador.")
for l in sal_plan.split(NL):
    if "ESTIMACION" in l:
        w("   | " + l.strip())
c_s, sal_sig = correr([PY, LANZADOR_BATERIA, "--siguiente"])
io.open(os.path.join(LOOP, "SALIDA_V%d_T2_SIGUIENTE_APERTURA.txt" % VUELTA), "w",
        encoding="utf-8", newline=NL).write(sal_sig)
mhe = re.search(r"CIFRA tramos CON salida sellada no vacia:\s*(\d+)", sal_sig)
mfa = re.search(r"CIFRA tramos que FALTAN:\s*(\d+)", sal_sig)
msg = re.search(r"EL SIGUIENTE ES EL TRAMO (\d+)", sal_sig)
w("   comando: python %s --siguiente  (exitcode %d)" % (LANZADOR_BATERIA, c_s))
w("   CIFRA tramos que --siguiente da POR HECHOS: %s"
  % (mhe.group(1) if mhe else "(no impresa)"))
w("   CIFRA tramos que --siguiente dice que FALTAN: %s"
  % (mfa.group(1) if mfa else "(no impresa)"))
w("   --siguiente DICE QUE EL SIGUIENTE ES EL TRAMO %s, Y ESA ES LA MENTIRA"
  % (msg.group(1) if msg else "(no lo dice)"))
w("   MEDIDA: esos hechos son de la corrida de la vuelta %d, no de la %d."
  % (VUELTA_DEL_LANZADOR, VUELTA))
w("   ESTA VUELTA CORRE LOS %s TRAMOS, no los que --siguiente diga."
  % (mtr.group(1) if mtr else "?"))
w("")

w("=== I. EL INVENTARIO ENTERO DE SELLADAS DE BATERIA, CONTADO DE DISCO ===")
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
