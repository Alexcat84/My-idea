# -*- coding: utf-8 -*-
r"""vuelta199_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 199, CORRIDO ANTES
DE LA PRIMERA OPERACION.

CLON DECLARADO de `scripts/loop/vuelta197_apertura.py`, que a su vez viene de la
195 y de la 196. Lo que cambia se dice aqui y no se esconde:

1. LA VUELTA ES LA 199 Y EL ENCARGO ES OTRO. Los bloques `H` de la 197 median el
   sujeto de SU tarea 3 (el doble del auditor). Aqui miden el sujeto de LAS
   TAREAS DE ESTA VUELTA: las dos guardas apagadas, las seis llamadas que borran
   la sede, los ejemplares del banco y la vara del plan.
2. EL BLOQUE `J` ACOTA EL ACTA 198 EN ESTA VUELTA, con `grep -n` corrido aqui.
3. EL BLOQUE `F` MIDE LA NOMINA CONTRA EL CONGELADO EN 135 que manda
   `AUDITOR.md` 6.3. Ni crece ni se poda, y aqui solo se MIDE.
4. EL BLOQUE `E` SIGUE CONTANDO LA RACHA DEL INSTRUMENTO, porque de esa cifra
   depende si el tope de sub-tareas es DOS o CINCO (`AUDITOR.md` 6.2).

USO:
  python scripts/loop/vuelta199_apertura.py
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
VUELTA = 199

VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
TURNO = "docs/loop/_TURNO_DEL_AUDITOR.json"
ACTA = "docs/loop/ACTA_AUDITOR.md"

INSTRUMENTO_RACHA = "scripts/loop/vuelta192_racha_de_cierres.py"
SELLADA_RACHA = "docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt"

# LOS SUJETOS DE ESTA VUELTA, medidos y no supuestos.
MODULO_GUARDAS = "scripts/loop/apertura_del_auditor.py"
ARNES_DEL_AUDITOR = "scripts/loop/_auditor_v198_guarda_muerta.py"
SALIDA_DEL_AUDITOR = "docs/loop/SALIDA_V198_GUARDA_MUERTA.txt"
ARNES_QUE_BORRA = "scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py"
BANCO = "docs/BANCO_DE_TEXTOS.md"
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
w("         sep 2026). NO SE FABRICAN ARNESES, GUARDAS NI LECTORES NUEVOS salvo")
w("         las TAREAS 1 y 2 que el acta 198 ya adjudico. La nomina queda")
w("         CONGELADA EN 135. El trabajo es EL PLAN.")
w("         ESTA NO ES VUELTA DE BATERIA: el encargo dice con todas sus letras")
w("         que LA VUELTA DE BATERIA SE CORRE EN LA 200, para que los remedios")
w("         de las TAREAS 1 y 2 esten DENTRO cuando corra. La seccion 9 del")
w("         reporte cierra con HUECO DECLARADO Y MEDIDO.")
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

w("=== C.1 LA CADENA DE LA VUELTA 197, EL ACTA 198 Y LA DECISION, EN GIT ===")
c, logtodo = git(["log", "--format=%h%x09%s", "-40"])
filas = [l.split(chr(9), 1) for l in logtodo.splitlines() if chr(9) in l]
for etiqueta, aguja in (("acta 198", "ACTA DEL AUDITOR, VUELTA 198"),
                        ("cierre de la 197", "VUELTA 197 CERRADA"),
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
w("ES EL SUJETO DE LAS TAREAS 1 Y 2. Se mide AQUI, entero y literal, porque la")
w("TAREA 2 repara justamente el arnes que lo borra, y sin esta medida de entrada")
w("no habria contra que cotejar el 'no se movio' del cierre.")
mt = sha_de(TURNO)
if mt is None:
    w("   NO EXISTE %s al entrar." % TURNO)
else:
    w("   %s" % TURNO)
    w("      disco %d bytes | LF %d bytes | sha256 LF %s" % (mt[2], mt[3], mt[1][:16]))
    try:
        txt_turno = io.open(os.path.join(RAIZ, TURNO.replace("/", os.sep)),
                            encoding="utf-8", errors="replace").read()
        w("      CIFRA lineas del fichero del turno por split(NL): %d"
          % len(txt_turno.split(NL)))
        w("      contenido literal, cercado ENTERO:")
        for l in txt_turno.split(NL):
            w("      | " + l)
    except Exception as e:                                # noqa: BLE001
        w("      NO SE PUDO LEER: %r" % (e,))
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
        w("EL TOPE, LEIDO DE AUDITOR.md 6.2 CONTRA ESTA CIFRA: el regimen")
        w("   temporal pide DOS vueltas seguidas cerrando su propio reporte para")
        w("   devolver el tope de cinco.")
        if int(racha) >= 2:
            w("   CON RACHA %s EL REGIMEN TEMPORAL SE APAGA Y VUELVE EL TOPE DE"
              % racha)
            w("   CINCO. El encargo trae CUATRO sub-tareas, que cabe.")
        else:
            w("   CON RACHA %s EL TOPE SIGUE SIENDO DE DOS SUB-TAREAS, y el" % racha)
            w("   encargo trae CUATRO. ESO ES UNA DISCREPANCIA Y SE DECLARA EN EL")
            w("   REPORTE en vez de resolverse callando.")
    w("nuevo corte, medido antes de restaurar:")
    despues = sha_de(SELLADA_RACHA)
    if despues:
        w("   %d bytes LF | sha256 LF %s" % (despues[3], despues[1][:16]))
    git(["checkout", "--", SELLADA_RACHA])
    rest = sha_de(SELLADA_RACHA)
    if antes and rest:
        w("SELLADA ANTES:     %d bytes LF | sha256 LF %s" % (antes[3], antes[1][:16]))
        w("SELLADA RESTAURADA:%d bytes LF | sha256 LF %s" % (rest[3], rest[1][:16]))
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
w("LA CIFRA DE FUERA DE LA NOMINA VIAJA CON SU VARA, Y SE MIDEN LAS DOS")
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
mser = re.search(r"SIGUIENTE LIBRE:\s*(R\.\d+)", salida_serie)
mcol = re.search(r"CIFRA colisiones \(un numero escrito mas de una vez\):\s*(\d+)",
                 salida_serie)
mtot = re.search(r"CIFRA entradas en total:\s*(\d+)", salida_serie)
w("SIGUIENTE LIBRE de la serie: %s" % (mser.group(1) if mser else "(no impreso)"))
w("CIFRA entradas en total: %s" % (mtot.group(1) if mtot else "(no impresa)"))
w("CIFRA colisiones: %s" % (mcol.group(1) if mcol else "(no impresa)"))
w("")

w("=== H. EL SUJETO DE LA TAREA 1: LAS DOS GUARDAS APAGADAS ===")
w("SE MIDE QUE EL ARNES DEL AUDITOR Y SU SALIDA EXISTEN Y NO ESTAN VACIOS (la")
w("regla LA RUTA QUE PROMETE PRUEBA ES CIFRA, 5 sep 2026), porque el encargo dice")
w("que SE PARTE DEL ARNES QUE EL AUDITOR DEJO ESCRITO y no de uno nuevo.")
for rel in (MODULO_GUARDAS, ARNES_DEL_AUDITOR, SALIDA_DEL_AUDITOR):
    med = sha_de(rel)
    if med is None:
        w("   ROJO: NO EXISTE %s" % rel)
        continue
    w("   %s" % rel)
    w("      disco %d bytes | LF %d bytes | sha256 LF %s"
      % (med[2], med[3], med[1][:16]))
    w("      existe y no esta vacio: %s"
      % ("SI" if med[2] > 0 else "NO, CERO BYTES"))
w("LAS LINEAS DE CODIGO QUE EL ACTA 198 SENALA, LOCALIZADAS CON grep -n AQUI:")
ruta_mod = os.path.join(RAIZ, MODULO_GUARDAS.replace("/", os.sep))
lineas_mod = io.open(ruta_mod, encoding="utf-8", errors="replace").read().split(NL)
for etiqueta, patron in (
        ("_VIVO abierto puesto a True", r"_VIVO\[.abierto.\]\s*=\s*True"),
        ("_VIVO abierto puesto a False", r"_VIVO\[.abierto.\]\s*=\s*False"),
        ("la rama que mira el sello en disco solo con vuelta",
         r"if vuelta is not None:")):
    hits = [i + 1 for i, l in enumerate(lineas_mod) if re.search(patron, l)]
    w("   %-52s %d acierto(s), linea(s) %s"
      % (etiqueta, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
w("")

w("=== H.1 EL SUJETO DE LA TAREA 2: LAS SEIS LLAMADAS QUE BORRAN LA SEDE ===")
w("SE CUENTAN CON grep AQUI Y NO SE TECLEAN. El acta 198 dice SEIS; si el conteo")
w("de hoy no diera seis, MANDA EL CONTEO DE HOY y la discrepancia se declara.")
med_ab = sha_de(ARNES_QUE_BORRA)
if med_ab is None:
    w("   ROJO: NO EXISTE %s" % ARNES_QUE_BORRA)
else:
    w("   %s: %d bytes disco | %d LF" % (ARNES_QUE_BORRA, med_ab[2], med_ab[3]))
    ruta_ab = os.path.join(RAIZ, ARNES_QUE_BORRA.replace("/", os.sep))
    lineas_ab = io.open(ruta_ab, encoding="utf-8", errors="replace").read().split(NL)
    hits_ol = [i + 1 for i, l in enumerate(lineas_ab)
               if re.search(r"AP\.olvidar_todo\(\)", l)]
    w("   CIFRA llamadas a AP.olvidar_todo() contadas hoy: %d" % len(hits_ol))
    w("   lineas: %s" % ", ".join(str(h) for h in hits_ol))
    w("   CALZA CON LAS SEIS QUE EL ACTA 198 DICE: %s"
      % ("SI" if len(hits_ol) == 6 else
         "NO, y se declara: hoy salen %d" % len(hits_ol)))
    hits_rt = [i + 1 for i, l in enumerate(lineas_ab)
               if re.search(r"RUTA_DEL_TURNO", l)]
    w("   CIFRA menciones de RUTA_DEL_TURNO en el arnes AL ENTRAR: %d" % len(hits_rt))
    w("      lineas: %s" % (", ".join(str(h) for h in hits_rt) or "(ninguna)"))
w("")

w("=== H.2 EL SUJETO DE LA TAREA 3: LOS EJEMPLARES DEL BANCO ===")
w("AQUI SOLO SE MIDE QUE EL BANCO EXISTE Y CUANTAS VECES NOMBRA UN EJEMPLAR. LA")
w("LISTA SE COMPUTA EN LA TAREA 3, no aqui, y los dos que el acta 198 nombra")
w("(el 1077 del ejecutor y el 165 del auditor) se buscan para que la TAREA 3")
w("tenga contra que cotejar su computo.")
med_b = sha_de(BANCO)
if med_b is None:
    w("   ROJO: NO EXISTE %s" % BANCO)
else:
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (BANCO, med_b[2], med_b[3], med_b[1][:16]))
    ruta_b = os.path.join(RAIZ, BANCO.replace("/", os.sep))
    lineas_b = io.open(ruta_b, encoding="utf-8", errors="replace").read().split(NL)
    w("   CIFRA lineas del banco por split(NL): %d" % len(lineas_b))
    w("   CIFRA lineas con el literal EJEMPLAR: %d"
      % len([l for l in lineas_b if "EJEMPLAR" in l]))
    for aguja in ("1077", "165"):
        hits = [i + 1 for i, l in enumerate(lineas_b)
                if re.search(r"\b%s\b" % aguja, l)]
        w("   el %s aparece en %d linea(s): %s"
          % (aguja, len(hits), ", ".join(str(h) for h in hits[:12])
             or "(ninguna)"))
w("")

w("=== H.3 EL SUJETO DE LA TAREA 4: LA VARA DEL PLAN, CORRIDA AQUI ===")
w("EL ENCARGO DICE, CON ESAS PALABRAS, QUE EL PLAN SE RETOMA POR LA VARA DEL")
w("EXPEDIENTE Y NO POR EL CAMPO estado. La vara es el instrumento de abajo, y se")
w("corre AQUI, en la apertura, para que la TAREA 4 no elija su sujeto despues de")
w("mirar.")
med_v = sha_de(VARA_DEL_PLAN)
if med_v is None:
    w("   ROJO: NO EXISTE %s" % VARA_DEL_PLAN)
else:
    w("   %s: %d bytes disco | %d LF" % (VARA_DEL_PLAN, med_v[2], med_v[3]))
    w("   comando: python %s --corte HEAD" % VARA_DEL_PLAN)
    c_v, salida_v = correr([PY, VARA_DEL_PLAN, "--corte", "HEAD"])
    w("   EXITCODE: %d" % c_v)
    io.open(os.path.join(LOOP, "SALIDA_V%d_VARA_DEL_PLAN_APERTURA.txt" % VUELTA),
            "w", encoding="utf-8", newline=NL).write(salida_v)
    w("   salida sellada en docs/loop/SALIDA_V%d_VARA_DEL_PLAN_APERTURA.txt"
      % VUELTA)
    w("   %d bytes de salida" % len(salida_v.encode("utf-8")))
    for l in salida_v.split(NL):
        if re.search(r"CIFRA|OP-L-0|OP-I-01|TRABAJO REAL|LISTA", l):
            w("   | " + l.strip()[:150])
w("")

w("=== I. EL HUECO DE LA SECCION 9, MEDIDO AL ENTRAR ===")
w("NO ES VUELTA DE BATERIA: el encargo manda correrla en la 200 para que los")
w("remedios de las TAREAS 1 y 2 esten dentro. La seccion 9 cierra con HUECO")
w("DECLARADO Y MEDIDO por el carril de la TAREA 1.b de la vuelta 173.")
selladas = sorted(n for n in os.listdir(LOOP)
                  if re.match(r"^SALIDA_V\d+_BATERIA_TRAMO_\d+\.txt$", n))
w("CIFRA ficheros SALIDA_V*_BATERIA_TRAMO_N.txt en docs/loop/: %d" % len(selladas))
por_vuelta = {}
for n in selladas:
    v = re.match(r"^SALIDA_V(\d+)_", n).group(1)
    por_vuelta.setdefault(v, []).append(n)
for v in sorted(por_vuelta, key=int):
    w("   V%s: %d fichero(s)" % (v, len(por_vuelta[v])))
w("CIFRA ficheros SALIDA_V%d_BATERIA_TRAMO_N.txt al entrar: %d"
  % (VUELTA, len(por_vuelta.get(str(VUELTA), []))))
w("")

w("=== J. EL ACTA 198, ACOTADA CON grep -n EN ESTA VUELTA ===")
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
    for v in (198, 199):
        hits = [i + 1 for i, l in enumerate(lineas_acta)
                if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA %d\b" % v, l)]
        w("cabecera de la VUELTA %d: %d acierto(s), linea(s) %s"
          % (v, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
    ini = [i for i, l in enumerate(lineas_acta)
           if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA 198\b", l)]
    if len(ini) == 1:
        i0 = ini[0]
        sig = [i for i, l in enumerate(lineas_acta)
               if i > i0 and re.match(r"^#\s+ACTA\b", l)]
        i1 = sig[0] if sig else len(lineas_acta)
        w("CUERPO ACOTADO del acta 198: lineas %d a %d (1-indexadas), %d lineas"
          % (i0 + 1, i1, i1 - i0))
        w("   la de arriba es LA COTA QUE MANDA en esta vuelta.")
    else:
        w("ROJO: la cabecera del acta 198 no aparece exactamente una vez. NO SE")
        w("   ACOTA A OJO.")
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
