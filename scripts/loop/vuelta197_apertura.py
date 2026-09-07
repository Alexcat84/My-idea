# -*- coding: utf-8 -*-
r"""vuelta197_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 197, CORRIDO ANTES
DE LA PRIMERA OPERACION Y CON EL DESFASE DE CALIBRADO MEDIDO AQUI DENTRO.

CLON DECLARADO de scripts/loop/vuelta196_apertura.py, Y CON LA SECCION 8.1 DE SU
FUENTE LEIDA ANTES DE CLONAR, que es la disciplina que la `C.3` del reporte de la
194 dejo escrita: un clon declarado hereda tambien los defectos declarados de su
fuente.

LO QUE CAMBIA RESPECTO DE LA FUENTE, Y CADA CAMBIO CON SU MOTIVO ESCRITO:

1. EL BLOQUE `F` MIDE LA CIFRA DE FUERA DE LA NOMINA POR LAS DOS VARAS, que es la
   TAREA 4.a del encargo de la 197 y sale de la adjudicacion `4.7` del acta 197.
   El sello de la 196 publicaba UNA cifra de arneses fuera de la nomina sin
   nombrar la vara que la produce, y `0` al lado de un censo de 195 y una nomina
   de 135 se lee como que la nomina cubre el censo entero. AQUI SE MIDEN LAS DOS:
   `vara=VARA_DEL_CENSO` (la que decide) y `vara=0` (el censo crudo), y la cifra
   NO PUEDE VIAJAR SIN SU VARA porque las dos salen impresas con el numero de la
   vara al lado.

2. EL BLOQUE `J` ACOTA EL ACTA 197 EN ESTA VUELTA, con `grep -n` corrido aqui
   sobre `docs/loop/ACTA_AUDITOR.md`, porque el encargo dice que el fichero puede
   haber crecido desde que el auditor lo midio y que manda la medicion de hoy.

3. EL BLOQUE `H` APUNTA A LOS FICHEROS DE LA 197, y ademas mide LOS DOS
   `_exclusion.txt` que el auditor declaro en su `C.A5`, porque son la trampa que
   la TAREA 3 tiene que esquivar: guardan enteros sueltos y se leen con
   `numeros_de()`, no con el patron de `puesto_intra`.

ESTA NO ES VUELTA DE BATERIA (AUDITOR.md 6.1): la 194 la corrio entera por sus
diez tramos y la proxima cae en la 199. El bloque I mide EL HUECO DE LA SECCION 9
en vez del estado de una bateria que aqui no corre.

EL TOPE DE SUB-TAREAS NO SE TECLEA: la racha de cierres se cuenta AQUI del
instrumento, y lo que salga es lo que manda. El encargo dice que el auditor la
midio en 2 con las vueltas 195 y 196, y dice ademas que mande mi medicion de hoy.

`EJECUTOR.md` 1, LA APERTURA SE MIDE ANTES DE LA PRIMERA OPERACION: el estado
TRAS la primera operacion ya es estado intermedio y se cita como tal, con el
nombre de la operacion que lo movio.

EL CICLO DE GATE 0 CORRE ENTERO Y VA CABLEADO ABAJO: `scripts/run_phase1.py`
**CON `--reaplico-curaduria`** Y DESPUES `scripts/etiquetas_de_cara.py --aplicar`.
Solo con el primero quedan 72 lineas cambiadas en
`dataset/metadata/master_graph.json`, y es el segundo quien las repone.

NINGUNA CIFRA SE TECLEA. La racha de cierres sale del instrumento corrido y
contado; el numero de la serie sale de `scripts/loop/serie_de_registros.py`; la
identidad sale de `git rev-parse` y `git log`.

USO:
  python scripts/loop/vuelta197_apertura.py
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
VUELTA = 197

# LAS SEDES QUE NO SE PUEDEN MOVER EN ESTA VUELTA.
VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
TURNO = "docs/loop/_TURNO_DEL_AUDITOR.json"
ACTA = "docs/loop/ACTA_AUDITOR.md"

# EL INSTRUMENTO DE LA RACHA, EN UNA SOLA CONSTANTE. Se ejecuta ESTA y se publica
# ESTA: no hay una segunda copia del nombre en la prosa que pueda desviarse, que
# es exactamente como nacio la caida `C.E1` del acta 196.
INSTRUMENTO_RACHA = "scripts/loop/vuelta192_racha_de_cierres.py"
SELLADA_RACHA = "docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt"

# EL SUJETO DE LA TAREA 3, cerrado por el auditor ANTES de que yo mire nada, para
# que no se pueda elegir despues de mirar. La ruta va aqui; su contenido se LEE.
DOBLE_DEL_AUDITOR = "docs/loop/_auditor_v197_doble_para_la_198.txt"
CIEGA_DEL_AUDITOR = "docs/loop/_auditor_v197_ciega_blind.txt"

# LA TRAMPA DE LA `C.A5` DEL AUDITOR, MEDIDA Y NO NARRADA: los dos ficheros de
# exclusion guardan ENTEROS SUELTOS, no `puesto_intra`, y con un solo patron el
# universo sale corto. Aqui solo se comprueba que existen y cuanto pesan.
EXCLUSIONES = [
    "docs/loop/_auditor_v182_exclusion.txt",
    "docs/loop/_auditor_v190_exclusion.txt",
]


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
w("regimen: ESTA NO ES VUELTA DE BATERIA (AUDITOR.md 6.1, decision del fundador")
w("         del 5 sep 2026). La bateria corre CADA CINCO VUELTAS en una vuelta")
w("         propia QUE NO LLEVA NADA MAS; la 194 la corrio entera por sus diez")
w("         tramos y la proxima cae en la 199. La seccion 9 del reporte cierra")
w("         con HUECO DECLARADO Y MEDIDO, no con una bateria a medias.")
w("         EL TOPE DE SUB-TAREAS LO MANDA LA CIFRA DEL BLOQUE E, contada aqui")
w("         del instrumento. El encargo trae CUATRO sub-tareas.")
w("ESTE BLOQUE CORRE EL CICLO COMPLETO, tsc y pnpm test INCLUIDOS, y escribe el")
w("         mismo los dos literales de la guarda D.1. Eso funciono en la 195 y")
w("         en la 196, y no se deshace.")
w("EL NOMBRE DEL INSTRUMENTO DE LA RACHA NO SE TECLEA EN LA PROSA: sale de la")
w("         constante que se ejecuta, y se comprueba que existe y no esta vacio")
w("         ANTES de correrlo. Es el remedio de la caida C.E1 del acta 196.")
w("LA CIFRA DE FUERA DE LA NOMINA VIAJA CON SU VARA, Y SE MIDEN LAS DOS: es la")
w("         TAREA 4.a del encargo de la 197 y sale de la adjudicacion 4.7 del")
w("         acta 197. Bloque F.")
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

w("=== C.1 LA CADENA DE LA VUELTA 196 Y EL ACTA 197, LOCALIZADAS EN GIT ===")
c, logtodo = git(["log", "--format=%h%x09%s", "-40"])
filas = [l.split("\t", 1) for l in logtodo.splitlines() if "\t" in l]
for etiqueta, aguja in (("acta 197", "ACTA DEL AUDITOR, VUELTA 197"),
                        ("cierre de la 196", "VUELTA 196 CERRADA")):
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
    w("   LAS DOS CONVENCIONES SE PUBLICAN. La LF es la que el encargo clava:")
    w("   dice que abre y cierra en el MISMO valor, sin decir cual. LO QUE MANDA")
    w("   ES LA MEDIDA DE ARRIBA, y el cierre la remide contra ella.")
w("")

w("=== D.1 EL FICHERO DEL TURNO DEL AUDITOR, MEDIDO AL ENTRAR ===")
w("SE MIDE AQUI Y NO SE TOCA, porque es el sujeto de la TAREA 2.b (hallazgo 5.4")
w("del acta 197: el fichero del turno sobrevive al turno y el auditor siguiente")
w("lo hereda sucio). Lo que esta vuelta cambia es el CODIGO que lo cierra, no")
w("este fichero a mano.")
mt = sha_de(TURNO)
if mt is None:
    w("   NO EXISTE %s al entrar." % TURNO)
else:
    w("   %s" % TURNO)
    w("      disco %d bytes | LF %d bytes | sha256 LF %s" % (mt[2], mt[3], mt[1][:16]))
    try:
        w("      contenido literal, cercado:")
        for l in io.open(os.path.join(RAIZ, TURNO.replace("/", os.sep)),
                         encoding="utf-8", errors="replace").read().split(NL)[:12]:
            w("      | " + l)
    except Exception as e:                                # noqa: BLE001
        w("      NO SE PUDO LEER: %r" % (e,))
w("")

w("=== E. LA RACHA DE CIERRES, CONTADA DEL INSTRUMENTO Y NO HEREDADA ===")
w("EL NOMBRE SALE DE LA CONSTANTE QUE SE EJECUTA, NO DE LA PROSA (remedio de la")
w("   caida C.E1 del acta 196, que era un nombre tecleado que no existia).")
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
    w("   %s, porque su sujeto es el" % SELLADA_RACHA)
    w("   inventario de cierres y ese inventario CRECIO desde que la 192 lo")
    w("   sello. Aqui se corre, se lee la cifra, y la sellada se RESTAURA con")
    w("   git checkout -- y se REMIDE antes de darla por restaurada.")
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
        w("EL ENCARGO DE LA 197 DICE QUE LA MIDA YO EN MI APERTURA Y QUE MANDE MI")
        w("   MEDICION DE HOY, no la linea que el trae. Manda el instrumento.")
        w("EL TOPE, LEIDO DE AUDITOR.md 6.2 CONTRA ESTA CIFRA: el regimen")
        w("   temporal pide DOS vueltas seguidas cerrando su propio reporte para")
        w("   devolver el tope de cinco.")
        if racha == "2":
            w("   CON RACHA 2 EL REGIMEN TEMPORAL SE APAGA Y VUELVE EL TOPE DE")
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
w("SE MIDE AQUI porque la racha se cuenta hacia atras desde la vuelta MAS ALTA y")
w("un hueco en medio la corta. Lo que hay en disco al entrar, sin tocarlo:")
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
w("   ESO ES LO QUE ESTA VUELTA TIENE QUE SELLAR, y es la linea del encargo.")
w("")

w("=== F. LA NOMINA Y EL CENSO AL ENTRAR, Y LA CIFRA CON SUS DOS VARAS ===")
w("AQUI NO SE TOCA NADA: se MIDE. La nomina NO se poda en esta vuelta.")
w("TAREA 4.a DEL ENCARGO, Y ADJUDICACION 4.7 DEL ACTA 197: la cifra de arneses")
w("   del censo que se quedan FUERA de la nomina NO PUEDE VIAJAR SIN SU VARA. Un")
w("   0 al lado de un censo de tres cifras y una nomina de tres cifras se lee")
w("   como que la nomina cubre el censo entero, y no lo cubre. SE MIDEN LAS DOS:")
w("   CON la vara (la que decide) y SIN la vara (el censo crudo).")
try:
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_mutaciones_viejas as VMV   # noqa: E402
    w("CIFRA entradas de la nomina, leidas de VMV.VIEJAS: %d" % len(VMV.VIEJAS))
    w("CIFRA casos declarados: %d" % len(VMV.CASOS_DECLARADOS))
    censo = VMV.arneses_del_directorio()
    w("CIFRA arneses que el censo reconoce en scripts/loop/: %d" % len(censo))
    w("LA VARA DEL CENSO, que es la que decide (vuelta 178, TAREA 1.b): %d"
      % VMV.VARA_DEL_CENSO)
    ultima, faltan_n = VMV.arneses_que_faltan()
    w("CIFRA ultima vuelta representada en la nomina (INFORMATIVA, ya no decide):"
      " %s" % ultima)
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
    w("   vara salen %d. La segunda es la que dice cuanto del censo la nomina NO"
      % len(faltan_sin))
    w("   cubre, y publicar solo la primera hace pasar por cobertura total lo que")
    w("   es cobertura desde la vara para arriba.")
    w("   los DIEZ primeros de los %d, para que la cifra no viaje sola:"
      % len(faltan_sin))
    for n in faltan_sin[:10]:
        w("      FUERA DE LA NOMINA (sin vara): %s" % n)
    if len(faltan_sin) > 10:
        w("      ... y %d mas, contados y no listados aqui."
          % (len(faltan_sin) - 10))
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
w("EL ENCARGO NO TECLEA NINGUN NUMERO DE SERIE Y DICE QUE LO DIGA EL")
w("   INSTRUMENTO. Manda el instrumento: lo de arriba es lo que salio HOY.")
w("")

w("=== H. EL TRAMO Y EL DOBLE DE LA TAREA 3, CERRADOS POR EL AUDITOR ===")
w("SE MIDEN, NO SE ELIGEN: el auditor los cerro antes de que yo mirara nada, y")
w("aqui solo se comprueba que sus ficheros existen y no estan vacios (la regla")
w("LA RUTA QUE PROMETE PRUEBA ES CIFRA, 5 sep 2026).")
for rel in (DOBLE_DEL_AUDITOR, CIEGA_DEL_AUDITOR):
    med = sha_de(rel)
    if med is None:
        w("   ROJO: NO EXISTE %s" % rel)
        continue
    w("   %s" % rel)
    w("      disco %d bytes | LF %d bytes | sha256 LF %s"
      % (med[2], med[3], med[1][:16]))
    w("      existe y no esta vacio: %s"
      % ("SI" if med[2] > 0 else "NO, CERO BYTES"))
w("")

w("=== H.1 LA TRAMPA DE LA C.A5, MEDIDA ANTES DE PISARLA ===")
w("El auditor declaro en su C.A5 que los dos ficheros de exclusion guardan")
w("ENTEROS SUELTOS y se leen con numeros_de(), no con el patron de puesto_intra,")
w("y que con un solo patron el universo sale 300 en vez de 681. AQUI SOLO SE")
w("MIDEN, para que la TAREA 3 no tenga que fiarse de la prosa del encargo.")
for rel in EXCLUSIONES:
    med = sha_de(rel)
    if med is None:
        w("   NO EXISTE %s (se declara en vez de suponerlo)" % rel)
        continue
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    txt = io.open(ruta, encoding="utf-8", errors="replace").read()
    sueltos = re.findall(r"\b\d+\b", txt)
    conpat = re.findall(r"puesto_intra[_\- ]?(\d+)", txt)
    w("   %s: %d bytes disco" % (rel, med[2]))
    w("      enteros sueltos que \\b\\d+\\b encuentra: %d" % len(sueltos))
    w("      aciertos del patron puesto_intra: %d" % len(conpat))
w("")

w("=== H.2 LA VARA DE LA CIEGA, LOCALIZADA EN EL BANCO Y NO PARAFRASEADA ===")
w("El encargo manda citar 9.6.1 por numero con sus precisiones 9.6.2 y 9.6.3 y")
w("la tabla de LOS DOS POLOS del 9.22. Aqui solo se comprueba QUE EXISTEN en el")
w("banco, con su linea, para que la TAREA 3 pueda citarlas sin teclear una")
w("referencia que no este.")
banco = os.path.join(RAIZ, "docs", "BANCO_DE_TEXTOS.md")
if not os.path.isfile(banco):
    w("   ROJO: no existe docs/BANCO_DE_TEXTOS.md")
else:
    lineas_banco = io.open(banco, encoding="utf-8", errors="replace").read().split(NL)
    for clave in ("9.6.1", "9.6.2", "9.6.3", "9.22"):
        hits = [i + 1 for i, l in enumerate(lineas_banco)
                if re.search(r"^#+\s*" + re.escape(clave) + r"\b", l)]
        w("   %s: %d cabecera(s) en el banco, linea(s) %s"
          % (clave, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
w("")

w("=== I. EL HUECO DE LA SECCION 9, MEDIDO AL ENTRAR ===")
w("NO ES VUELTA DE BATERIA y por eso la seccion 9 cierra con HUECO DECLARADO Y")
w("MEDIDO por el carril de la TAREA 1.b de la vuelta 173. Lo que se mide aqui es")
w("QUE SELLADAS DE BATERIA HAY EN DISCO AL ENTRAR, para que nadie pueda declarar")
w("la bateria de esta vuelta corrida sobre la corrida de otra.")
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
w("LA CADENCIA, LEIDA DE AUDITOR.md 6.1 Y NO DE MEMORIA: la 194 la corrio")
w("entera y la proxima cae en la 199. AQUI NO SE CORRE LA BATERIA ENTERA.")
w("")

w("=== J. EL ACTA 197, ACOTADA CON grep -n EN ESTA VUELTA ===")
w("EL ENCARGO DICE QUE EL FICHERO PUEDE HABER CRECIDO Y QUE MANDA LA MEDICION DE")
w("HOY. El auditor la midio empezando en la 69341 sobre 4595886 bytes; lo de")
w("abajo es lo que mide ESTE bloque, corrido antes de la primera operacion.")
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
    for v in (197, 198):
        hits = [i + 1 for i, l in enumerate(lineas_acta)
                if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA %d\b" % v, l)]
        w("cabecera de la VUELTA %d: %d acierto(s), linea(s) %s"
          % (v, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
    ini = [i for i, l in enumerate(lineas_acta)
           if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA 197\b", l)]
    if len(ini) == 1:
        i0 = ini[0]
        sig = [i for i, l in enumerate(lineas_acta)
               if i > i0 and re.match(r"^#\s+ACTA\b", l)]
        i1 = sig[0] if sig else len(lineas_acta)
        w("CUERPO ACOTADO del acta 197: lineas %d a %d (1-indexadas), %d lineas"
          % (i0 + 1, i1, i1 - i0))
        w("   la de arriba es LA COTA QUE MANDA en esta vuelta; el conteo de")
        w("   adjudicaciones, hallazgos y caidas de la TAREA 1 se cuenta de AHI.")
        w("   coincide con la 69341 que el encargo cita: %s"
          % ("SI" if i0 + 1 == 69341 else "NO, y se declara la discrepancia"))
        w("   coincide con los 4595886 bytes que el encargo cita: %s"
          % ("SI" if ma[2] == 4595886 else "NO, y se declara la discrepancia"))
    else:
        w("ROJO: la cabecera del acta 197 no aparece exactamente una vez. NO SE")
        w("   ACOTA A OJO: la TAREA 1 tiene que resolverlo antes de contar nada.")
w("")

w("FIN DEL SELLO DE APERTURA")

texto = NL.join(L) + NL
io.open(os.path.join(LOOP, "SALIDA_V%d_APERTURA.txt" % VUELTA), "w",
        encoding="utf-8", newline=NL).write(texto)
print(texto)
escribir("HEAD", head + NL)

# ------------------------------------------------- EL BLOQUE DE MEDICIONES
# NINGUNA GUARDA SE TOCA (MODO AUSTERO 4): el ciclo de Gate 0 corre ENTERO, y el
# DESFASE DEL CALIBRADO SE MIDE AQUI, EN LA APERTURA, y no al cierre.
c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
escribir("GATE0_CMD1", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
escribir("CICLO_ETIQUETAS", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/sync_assets_web.py"])
escribir("CICLO_SYNC", o + "\nEXITCODE: %d\n" % c)

c, o = correr(["git", "diff", "HEAD", "--numstat", "--", "dataset/", "web/",
               "engine/"])
escribir("CICLO_NUMSTAT", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
escribir("CONTEO", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + "\nEXITCODE: %d\n" % c)

c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True,
              cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d\n" % c)

c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + "\nEXITCODE: %d\n" % c)

print("BLOQUE DE APERTURA COMPLETO, CICLO ENTERO INCLUIDO tsc Y pnpm test")
