# -*- coding: utf-8 -*-
r"""vuelta202_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 202, CORRIDO ANTES
DE LA PRIMERA OPERACION.

CLON DECLARADO de `scripts/loop/vuelta201_apertura.py`, que a su vez viene de la
200, la 199, la 197, la 196 y la 195. LOS BLOQUES `A` A `G` SE COPIARON BYTE A
BYTE de aquel fichero, con el generador `_gen_v202_apertura.py` de esta misma
vuelta, y NO se re escribieron: lo unico que cambia en ellos es la constante
`VUELTA` y los dos literales que nombran la vuelta anterior. Lo que SI se
reescribe se dice aqui y no se esconde:

1. LA 202 NO ES VUELTA DE BATERIA. La 200 lo fue y cerro entera; por la cadencia
   de `AUDITOR.md` 6.1 le toca a la 205. Aqui la seccion 9 cierra con el HUECO
   DECLARADO Y MEDIDO por su carril. El sujeto de esta vuelta es EL PLAN.
2. EL BLOQUE `H` MIDE EL SUJETO DE LA TAREA 1: la ficha `OP-L-03` de
   `docs/plan/OPERACIONES.jsonl` localizada POR LINEA, sus tres elementos de
   `evidencia` con su indice, las DOS cifras que el encargo manda medir sobre
   `docs/plan/LECTURAS_DIRIGIDAS.md` (el literal `reparto por acto` y las
   menciones de `OP-L-03`), y los DOS ficheros `docs/plan/OP_L_03_*.jsonl` con
   sus bytes exactos, sus filas, sus actos distintos y sus lineas no JSON.
3. EL BLOQUE `H.1` MIDE EL SUJETO DE LAS TAREAS 2 Y 3 ANTES DE TOCAR NADA: los
   DOS instrumentos de `OP-L-02` (que NO SE TOCAN y NO SE CLONAN), medidos y
   ademas leidos para comprobar SI ESCRIBEN FICHEROS; `docs/plan/08_VERIFICACION.md`
   con el criterio de hecho localizado por linea; y la TABLA VIVA DE LOS PUROS de
   `docs/BANCO_DE_TEXTOS.md` con su literal de vigencia.
4. EL BLOQUE `H.2` MIDE EL SUJETO DE LA TAREA 4: las actas 173 y 174 ACOTADAS
   AQUI por linea de inicio y fin, y la existencia de sus reportes archivados
   medida con `os.path.isfile` y `os.path.getsize`.
5. EL BLOQUE `H.3` CORRE LA VARA DEL TRABAJO PENDIENTE, que es
   `vuelta150_3_relectura_expediente.py --corte <HEAD DE APERTURA>`, y sella su
   salida. La vara NO SE CLONA y NO SE TOCA: se invoca.
6. EL BLOQUE `F` MIDE LA NOMINA CONTRA EL CONGELADO EN 135 que manda
   `AUDITOR.md` 6.3. AQUI NO SE PODA NI SE ANADE NADA: se mide.
7. EL BLOQUE `E` SIGUE CONTANDO LA RACHA DEL INSTRUMENTO, porque de esa cifra
   depende si el tope de sub-tareas es DOS o CINCO (`AUDITOR.md` 6.2).

USO:
  python scripts/loop/vuelta202_apertura.py
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
VUELTA = 202

VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
TURNO = "docs/loop/_TURNO_DEL_AUDITOR.json"
ACTA = "docs/loop/ACTA_AUDITOR.md"

INSTRUMENTO_RACHA = "scripts/loop/vuelta192_racha_de_cierres.py"
SELLADA_RACHA = "docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt"

# LOS SUJETOS DE ESTA VUELTA, medidos y no supuestos.
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

# TAREA 1: la sede de la correccion y los dos ficheros del reparto por acto.
FICHA_T1 = "OP-L-03"
DOC_DE_LA_EVIDENCIA = "docs/plan/LECTURAS_DIRIGIDAS.md"
LITERAL_REPARTO = "reparto por acto"
FICHEROS_DEL_REPARTO = [
    "docs/plan/OP_L_03_LECTURAS.jsonl",
    "docs/plan/OP_L_03_TRIANGULOS.jsonl",
]

# TAREAS 2 y 3: los instrumentos que se IMPORTAN y no se clonan, y las sedes.
INSTRUMENTOS_OP_L_02 = [
    "scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py",
    "scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py",
]
CRITERIO_DE_HECHO = "docs/plan/08_VERIFICACION.md"
BANCO = "docs/BANCO_DE_TEXTOS.md"
LINEA_TABLA_VIVA = 938
LITERAL_VIGENCIA = "vigente al puesto"

# TAREA 4: las dos actas mas viejas de la deuda y sus reportes archivados.
# LA MARCA DE ESCRITURA EN DISCO, para comprobar ANTES de correrlos que
# los dos instrumentos de OP-L-02 SOLO MIDEN. No es una guarda nueva: es
# una expresion regular de este mismo bloque de apertura, que no vive fuera
# de el y no entra en el censo.
PATRON_ESCRITURA = re.compile(
    r"open\s*\([^)]*[" + chr(34) + chr(39) + r"](w|wb|a|ab|w\+|r\+)["
    + chr(34) + chr(39) + r"]|\.write\s*\(|os\.remove|shutil\.|os\.rename|os\.makedirs|json\.dump\s*\(")
ACTAS_DE_LA_DEUDA = [173, 174]
PENDIENTES = "docs/PENDIENTES.md"


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
w("         cadencia de AUDITOR.md 6.1 le toca a la 205. La seccion 9 cierra con")
w("         el HUECO DECLARADO Y MEDIDO por su carril.")
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

w("=== C.1 LA CADENA DE LA VUELTA 201 Y SU ACTA, EN GIT ===")
c, logtodo = git(["log", "--format=%h%x09%s", "-40"])
filas = [l.split(chr(9), 1) for l in logtodo.splitlines() if chr(9) in l]
for etiqueta, aguja in (("acta 201", "ACTA DEL AUDITOR, VUELTA 201"),
                        ("cierre de la 201", "VUELTA 201 CERRADA"),
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
w("EL ENCARGO DICE QUE HOY EL SIGUIENTE LIBRE ES R.63 Y MANDA VOLVER A CORRERLO.")
w("   CALZA LO CORRIDO CON LO QUE EL ENCARGO DICE: %s"
  % ("SI" if (mser and mser.group(1) == "R.63") else "NO, y se declara"))
w("")

w("=== H. EL SUJETO DE LA TAREA 1: LA FICHA OP-L-03, SU EVIDENCIA Y LOS DOS ===")
w("    FICHEROS DEL REPARTO POR ACTO, MEDIDOS ANTES DE TOCAR NADA")
w("LA COORDENADA DE UNA FICHA JSONL ES LINEA MAS INDICE (acta 201, 4.4). AQUI SE")
w("   PUBLICAN LAS DOS NUMERACIONES DEL INDICE, la de base 0 de Python y la de")
w("   base 1 que el encargo usa, para que ninguna cita quede ambigua.")
mops = sha_de(OPERACIONES)
lin_ops = []
if mops is None:
    w("   ROJO: NO EXISTE %s" % OPERACIONES)
else:
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (OPERACIONES, mops[2], mops[3], mops[1][:16]))
    ruta_ops = os.path.join(RAIZ, OPERACIONES.replace("/", os.sep))
    lin_ops = io.open(ruta_ops, encoding="utf-8", errors="replace").read().split(NL)
    w("   CIFRA lineas NO VACIAS de OPERACIONES.jsonl: %d"
      % len([l for l in lin_ops if l.strip()]))
    aguja = chr(34) + "id_op" + chr(34) + ": " + chr(34) + FICHA_T1 + chr(34)
    hits = [i + 1 for i, l in enumerate(lin_ops) if l.strip() and aguja in l]
    w("   CIFRA lineas donde vive %s: %d | linea(s): %s"
      % (FICHA_T1, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
    if len(hits) == 1:
        d = json.loads(lin_ops[hits[0] - 1])
        w("   la ficha %s vive en la LINEA %d" % (FICHA_T1, hits[0]))
        w("   estado=%r  tipo=%r  fase=%r  fecha_corte=%r"
          % (d.get("estado"), d.get("tipo"), d.get("fase"), d.get("fecha_corte")))
        w("   CIFRA claves de la ficha: %d" % len(d))
        w("      %s" % ", ".join(sorted(d)))
        ev = d.get("evidencia", [])
        w("   CIFRA elementos de `evidencia`: %d" % len(ev))
        for i, e in enumerate(ev):
            w("      evidencia indice %d (elemento %d): %s" % (i, i + 1, repr(e)))
        ver = d.get("verificacion", [])
        w("   CIFRA elementos de `verificacion`: %d" % len(ver))
        for i, e in enumerate(ver):
            w("      verificacion indice %d (elemento %d), %d caracteres: %s"
              % (i, i + 1, len(str(e)), repr(e)[:200]))
        w("   CIFRA elementos de `evidencia` que NOMBRAN un fichero: %d"
          % len([x for x in ev
                 if re.search(r"[A-Za-z0-9_/.-]+\.(md|jsonl|py|json|txt)", str(x))]))
        w("   CIFRA elementos de `evidencia` que traen el literal %r: %d"
          % (LITERAL_REPARTO,
             len([x for x in ev if LITERAL_REPARTO in str(x)])))
    else:
        w("   ROJO: la ficha %s no aparece exactamente una vez. NO SE ACOTA A OJO."
          % FICHA_T1)
w("")
w("LAS DOS CIFRAS QUE EL ENCARGO MANDA MEDIR SOBRE EL DOCUMENTO QUE LA EVIDENCIA")
w("   NOMBRA. NO SE COPIAN DEL ENCARGO: SE CUENTAN AQUI.")
mdoc = sha_de(DOC_DE_LA_EVIDENCIA)
if mdoc is None:
    w("   ROJO: NO EXISTE %s" % DOC_DE_LA_EVIDENCIA)
else:
    ruta_doc = os.path.join(RAIZ, DOC_DE_LA_EVIDENCIA.replace("/", os.sep))
    t_doc = io.open(ruta_doc, encoding="utf-8", errors="replace").read()
    l_doc = t_doc.split(NL)
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (DOC_DE_LA_EVIDENCIA, mdoc[2], mdoc[3], mdoc[1][:16]))
    w("   CIFRA lineas por split(NL): %d | por count(NL): %d"
      % (len(l_doc), t_doc.count(NL)))
    w("   CIFRA apariciones del literal %r: %d"
      % (LITERAL_REPARTO, t_doc.count(LITERAL_REPARTO)))
    w("   CIFRA lineas que traen el literal %r: %d"
      % (LITERAL_REPARTO,
         len([l for l in l_doc if LITERAL_REPARTO in l])))
    w("   CIFRA apariciones de %r: %d" % (FICHA_T1, t_doc.count(FICHA_T1)))
    w("   CIFRA lineas que mencionan %r: %d"
      % (FICHA_T1, len([l for l in l_doc if FICHA_T1 in l])))
    w("   LA BUSQUEDA POSITIVA, PORQUE UNA BUSQUEDA NEGATIVA NO SE PUEDE CITAR")
    w("      (EJECUTOR.md 9). Variantes buscadas y su cuenta:")
    for var in ("reparto por acto", "reparto por", "por acto", "OP-L-03",
                "OP_L_03", "OP L 03"):
        w("      %-20s %d aparicion(es)" % (var, t_doc.count(var)))
w("")
w("LOS DOS FICHEROS QUE SI TRAEN EL REPARTO POR ACTO, MEDIDOS EN BYTES EXACTOS")
w("   (P.2: bytes exactos, nunca redondeados, KB solo entre parentesis y detras")
w("   del byte). SE MIDE TAMBIEN SU CONTENIDO: filas, actos distintos y lineas")
w("   que no son JSON.")
for fr in FICHEROS_DEL_REPARTO:
    mfr = sha_de(fr)
    if mfr is None:
        w("   %-38s NO EXISTE EN DISCO" % fr)
        continue
    ruta_fr = os.path.join(RAIZ, fr.replace("/", os.sep))
    t_fr = io.open(ruta_fr, encoding="utf-8", errors="replace").read()
    filas_fr = [l for l in t_fr.split(NL) if l.strip()]
    actos = []
    malas_fr = 0
    for l in filas_fr:
        try:
            dd = json.loads(l)
        except Exception:                                # noqa: BLE001
            malas_fr += 1
            continue
        if "acto" in dd:
            actos.append(dd["acto"])
    w("   %s" % fr)
    w("      disco %d bytes (%.1f KB) | LF %d bytes | sha256 LF %s"
      % (mfr[2], mfr[2] / 1024.0, mfr[3], mfr[1][:16]))
    w("      CIFRA filas no vacias: %d" % len(filas_fr))
    w("      CIFRA lineas que NO son JSON valido: %d" % malas_fr)
    w("      CIFRA filas con campo `acto`: %d" % len(actos))
    w("      CIFRA actos DISTINTOS: %d" % len(set(actos)))
    w("      los actos distintos, ordenados: %s"
      % ", ".join(sorted(set(actos))))
w("")
w("LA CIFRA QUE LA EVIDENCIA PROMETE, LEIDA DE LA PROPIA FICHA Y NO TECLEADA:")
if lin_ops:
    aguja = chr(34) + "id_op" + chr(34) + ": " + chr(34) + FICHA_T1 + chr(34)
    hh = [i + 1 for i, l in enumerate(lin_ops) if l.strip() and aguja in l]
    if len(hh) == 1:
        d = json.loads(lin_ops[hh[0] - 1])
        for i, e in enumerate(d.get("evidencia", [])):
            mm = re.search(r"(\d+)\s+pares?\s+en\s+(\d+)\s+actos?", str(e))
            if mm:
                w("   evidencia indice %d (elemento %d) promete %s pares en %s actos"
                  % (i, i + 1, mm.group(1), mm.group(2)))
                w("      su literal entero: %s" % repr(e))
w("")

w("=== H.1 EL SUJETO DE LAS TAREAS 2 Y 3: LOS DOS INSTRUMENTOS DE OP-L-02, ===")
w("    EL CRITERIO DE HECHO Y LA TABLA VIVA DE LOS PUROS")
w("LOS DOS INSTRUMENTOS SE IMPORTAN Y NO SE CLONAN (encargo de esta vuelta). AQUI")
w("   SE MIDEN Y SE LEEN PARA COMPROBAR SI ESCRIBEN FICHEROS, que es lo que el")
w("   encargo manda comprobar ANTES de correrlos.")
for ins in INSTRUMENTOS_OP_L_02:
    mi = sha_de(ins)
    if mi is None or mi[2] == 0:
        w("   ROJO: %s NO EXISTE o mide CERO BYTES." % ins)
        continue
    ruta_i = os.path.join(RAIZ, ins.replace("/", os.sep))
    t_i = io.open(ruta_i, encoding="utf-8", errors="replace").read()
    l_i = t_i.split(NL)
    aciertos = [(j + 1, l.strip()) for j, l in enumerate(l_i)
                if PATRON_ESCRITURA.search(l)]
    w("   %s" % ins)
    w("      disco %d bytes | LF %d bytes | sha256 LF %s"
      % (mi[2], mi[3], mi[1][:16]))
    w("      CIFRA lineas por count(NL): %d" % t_i.count(NL))
    w("      CIFRA lineas con marca de ESCRITURA en disco: %d" % len(aciertos))
    for j, l in aciertos[:12]:
        w("         linea %d: %s" % (j, l[:110]))
    if not aciertos:
        w("         (ninguna: el instrumento SOLO MIDE, no escribe ficheros)")
    w("      CIFRA apariciones del literal 46208790 (el HEAD sellado en la 170): %d"
      % t_i.count("46208790"))
    for j, l in enumerate(l_i):
        if "46208790" in l:
            w("         linea %d: %s" % (j + 1, l.strip()[:120]))
w("")
w("EL CRITERIO DE HECHO, LOCALIZADO POR LINEA Y NO CITADO DE MEMORIA:")
mcri = sha_de(CRITERIO_DE_HECHO)
if mcri is None:
    w("   ROJO: NO EXISTE %s" % CRITERIO_DE_HECHO)
else:
    ruta_c = os.path.join(RAIZ, CRITERIO_DE_HECHO.replace("/", os.sep))
    t_c = io.open(ruta_c, encoding="utf-8", errors="replace").read()
    l_c = t_c.split(NL)
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (CRITERIO_DE_HECHO, mcri[2], mcri[3], mcri[1][:16]))
    w("   CIFRA lineas por count(NL): %d" % t_c.count(NL))
    for aguja in ("CRITERIO DE HECHO", "criterio de hecho", "OP-L-01",
                  "OP-L-02", "OP-L-03"):
        hits = [j + 1 for j, l in enumerate(l_c) if aguja in l]
        w("   %-20s %d linea(s): %s"
          % (aguja, len(hits),
             ", ".join(str(x) for x in hits[:16]) or "(ninguna)"))
w("")
w("LA TABLA VIVA DE LOS PUROS Y SU LITERAL DE VIGENCIA, MEDIDOS AL ENTRAR:")
mban = sha_de(BANCO)
if mban is None:
    w("   ROJO: NO EXISTE %s" % BANCO)
else:
    ruta_b = os.path.join(RAIZ, BANCO.replace("/", os.sep))
    t_b = io.open(ruta_b, encoding="utf-8", errors="replace").read()
    l_b = t_b.split(NL)
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (BANCO, mban[2], mban[3], mban[1][:16]))
    w("   CIFRA lineas por split(NL): %d | por count(NL): %d"
      % (len(l_b), t_b.count(NL)))
    w("   EL ENCARGO NOMBRA LA LINEA %d. Su contenido, leido y no supuesto:"
      % LINEA_TABLA_VIVA)
    if len(l_b) >= LINEA_TABLA_VIVA:
        w("      linea %d: %s" % (LINEA_TABLA_VIVA, l_b[LINEA_TABLA_VIVA - 1][:200]))
    else:
        w("      ROJO: el fichero tiene menos de %d lineas" % LINEA_TABLA_VIVA)
    hits = [j + 1 for j, l in enumerate(l_b) if LITERAL_VIGENCIA in l]
    w("   CIFRA lineas con el literal %r: %d | linea(s): %s"
      % (LITERAL_VIGENCIA, len(hits),
         ", ".join(str(x) for x in hits[:16]) or "(ninguna)"))
    for x in hits[:8]:
        w("      linea %d: %s" % (x, l_b[x - 1].strip()[:180]))
    hits2 = [j + 1 for j, l in enumerate(l_b) if "TABLA VIVA" in l]
    w("   CIFRA lineas con el literal TABLA VIVA: %d | linea(s): %s"
      % (len(hits2), ", ".join(str(x) for x in hits2[:16]) or "(ninguna)"))
w("")

w("=== H.2 EL SUJETO DE LA TAREA 4: LAS ACTAS 173 Y 174, ACOTADAS AQUI, Y ===")
w("    SUS REPORTES ARCHIVADOS, MEDIDOS CON os.path.isfile Y os.path.getsize")
ma = sha_de(ACTA)
if ma is None:
    w("   ROJO: no existe %s" % ACTA)
else:
    w("   %s: %d bytes disco | %d bytes LF | sha256 LF %s"
      % (ACTA, ma[2], ma[3], ma[1][:16]))
    ruta_acta = os.path.join(RAIZ, ACTA.replace("/", os.sep))
    lineas_acta = io.open(ruta_acta, encoding="utf-8",
                          errors="replace").read().split(NL)
    w("   CIFRA lineas del acta por split(NL): %d" % len(lineas_acta))
    for v in ACTAS_DE_LA_DEUDA + [201, 202]:
        hits = [i + 1 for i, l in enumerate(lineas_acta)
                if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA %d\b" % v, l)
                or re.match(r"^#\s*ACTA DE LA VUELTA %d DEL AUDITOR\b" % v, l)]
        w("   cabecera de la VUELTA %d: %d acierto(s), linea(s) %s"
          % (v, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
    for v in ACTAS_DE_LA_DEUDA:
        ini = [i for i, l in enumerate(lineas_acta)
               if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA %d\b" % v, l)
               or re.match(r"^#\s*ACTA DE LA VUELTA %d DEL AUDITOR\b" % v, l)]
        if len(ini) != 1:
            w("   ROJO: la cabecera del acta %d no aparece exactamente una vez." % v)
            continue
        i0 = ini[0]
        sig = [i for i in range(i0 + 1, len(lineas_acta))
               if re.match(r"^#\s+ACTA\b", lineas_acta[i])]
        i1 = sig[0] if sig else len(lineas_acta)
        w("   CUERPO ACOTADO del acta %d: lineas %d a %d (1-indexadas), %d lineas"
          % (v, i0 + 1, i1, i1 - i0))
        cuerpo = lineas_acta[i0:i1]
        secc = {}
        for j, l in enumerate(cuerpo):
            mm = re.match(r"^#{2,4}\s*(\d+)(?:\.(\d+))?\b", l)
            if mm:
                secc.setdefault(mm.group(1), []).append(i0 + j + 1)
        for k in sorted(secc, key=lambda x: int(x)):
            w("      seccion %s: %d cabecera(s) en linea(s) %s"
              % (k, len(secc[k]), ", ".join(str(x) for x in secc[k][:20])))
        claves_p = sorted(set(re.findall(r"P\.(\d+)", NL.join(cuerpo))), key=int)
        w("      CIFRA claves P.n distintas nombradas en el cuerpo: %d (%s)"
          % (len(claves_p), ", ".join("P." + x for x in claves_p) or "(ninguna)"))
w("")
w("LOS REPORTES ARCHIVADOS DE LA DEUDA, MEDIDOS Y NO RECORDADOS:")
dir_rep = os.path.join(LOOP, "reportes")
for v in ACTAS_DE_LA_DEUDA:
    rel_rep = "docs/loop/reportes/REPORTE_V%d.md" % v
    ruta_rep = os.path.join(RAIZ, rel_rep.replace("/", os.sep))
    existe = os.path.isfile(ruta_rep)
    w("   %-40s os.path.isfile: %s | os.path.getsize: %s"
      % (rel_rep, "SI" if existe else "NO",
         (str(os.path.getsize(ruta_rep)) + " bytes") if existe
         else "NO MEDIBLE, no hay fichero"))
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
faltan_168_199 = [n for n in range(168, 200) if n not in nums_rep]
w("   CIFRA vueltas del rango 168 a 199 SIN reporte archivado: %d"
  % len(faltan_168_199))
w("      cuales: %s" % (", ".join(str(n) for n in faltan_168_199) or "(ninguna)"))
mpen = sha_de(PENDIENTES)
if mpen is None:
    w("   ROJO: NO EXISTE %s" % PENDIENTES)
else:
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (PENDIENTES, mpen[2], mpen[3], mpen[1][:16]))
w("")

w("=== H.3 EL INVENTARIO Y LAS CUATRO FICHAS REALES, MEDIDOS ANTES DE TOCAR ===")
w("    NADA, Y LA VARA DEL TRABAJO PENDIENTE CORRIDA CON EL HEAD DE APERTURA")
minv = sha_de(INVENTARIO_JSONL)
if minv is None:
    w("   ROJO: NO EXISTE %s" % INVENTARIO_JSONL)
else:
    ruta_inv = os.path.join(RAIZ, INVENTARIO_JSONL.replace("/", os.sep))
    t_inv = io.open(ruta_inv, encoding="utf-8", errors="replace").read()
    l_inv = [l for l in t_inv.split(NL) if l.strip()]
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (INVENTARIO_JSONL, minv[2], minv[3], minv[1][:16]))
    w("   CIFRA lineas NO VACIAS (las entradas): %d" % len(l_inv))
w("   LAS CUATRO FICHAS REALES, LOCALIZADAS POR LINEA EN %s:" % OPERACIONES)
if lin_ops:
    for idop in FICHAS_REALES:
        aguja = chr(34) + "id_op" + chr(34) + ": " + chr(34) + idop + chr(34)
        hits = [i + 1 for i, l in enumerate(lin_ops) if l.strip() and aguja in l]
        w("      %-9s %d linea(s): %s"
          % (idop, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
        if len(hits) == 1:
            d = json.loads(lin_ops[hits[0] - 1])
            w("         estado=%r  tipo=%r  fase=%r"
              % (d.get("estado"), d.get("tipo"), d.get("fase")))
            w("         CIFRA elementos de `verificacion`: %d"
              % len(d.get("verificacion", [])))
            w("         CIFRA elementos de `evidencia`: %d"
              % len(d.get("evidencia", [])))
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
w("   LA VARA DEL TRABAJO PENDIENTE, CORRIDA AQUI CON EL HEAD DE APERTURA COMO")
w("   CORTE. LA VARA NO SE CLONA Y NO SE TOCA: SE INVOCA.")
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
