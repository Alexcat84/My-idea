# -*- coding: utf-8 -*-
r"""vuelta184_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 184, ENTERO Y
ANTES DE LA PRIMERA OPERACION.

CLON DECLARADO de scripts/loop/vuelta183b_apertura.py. Cambia el SUFIJO de las
salidas (184, computado del nombre del fichero), la lista RUTAS_DEL_ENCARGO y los
bloques H, que aqui miden lo que ESTE encargo promete y nada mas. Y LA AFIRMACION
DE CLON SE MIDE: el cotejo lo hace scripts/loop/cotejar_clon_declarado.py y su
salida se pega en el reporte con lo que salga. NO se afirma que el diff salga
vacio.

POR QUE 184 Y NO 183C. Esta vuelta NO es la continuacion de la 183: el acta 184
ya cubrio esa continuacion (ACTA_AUDITOR.md:64050) y su punto 8 manda una VUELTA
DE BATERIA NUEVA que retoma en el TRAMO 6. El reporte de la 183 se archiva en el
PASO 0 de esta vuelta y aqui se abre uno propio, el de la 184.

EL NUMERO Y EL SUFIJO NO SE TECLEAN: SALEN DE os.path.basename(__file__).

EL BLOQUE H NO TECLEA NINGUN HASH NI NINGUNA CIFRA (EJECUTOR.md 2, EL INSTRUMENTO
MANDA). El encargo da cifras (38.747 bytes y sha256 f81f1b32594221f1 del ciego del
auditor, 112 entradas de nomina, 37,0 y 48,2 minutos del --plan, 5 de 9 tramos,
tamano de tramo 13); aqui NO SE COPIA NINGUNA: se corre y se imprime lo que salga,
y la comparacion con lo que el encargo dice se hace despues, en el reporte, con
las dos al lado.

LA CIFRA DE BYTES SE PUBLICA POR LAS DOS CONVENCIONES (acta 177 punto 7.11):
disco (os.path.getsize) y git (git cat-file -s). Y la P.2 del fundador manda
BYTES EXACTOS Y NUNCA REDONDEADOS.

POR QUE SE CORRE AQUI: EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION". El encargo manda ademas commitear lo pendiente antes de tocar
nada, y un commit MUEVE HEAD: por eso este bloque corre PRIMERO.

ESTE FICHERO NO TOCA REPORTE.md, NO toca la nomina, NO corre la bateria y NO
escribe en docs/plan/: sus salidas son SALIDA_V184_*.txt.

LO QUE ESTA SESION SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano al abrir, dio UNA sola linea,
" M dataset/metadata/master_graph.json", y git diff --numstat -- dataset/ dio CERO
filas, que es la firma de fin de linea que el acta 181 punto 3.3 y el acta 184
punto 3.1 ya midieron y declararon que NO es perdida de catalogo. La prediccion se
escribe AQUI, antes de correr, y los bloques C/D/E/F de abajo la miden sin saber
lo que hay escrito.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

USO:
  python scripts/loop/vuelta184_apertura.py
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

# EL SUFIJO DE LAS SALIDAS, COMPUTADO DEL NOMBRE DEL FICHERO Y NO TECLEADO.
# vuelta183b_apertura.py -> "183B". Un clon llamado vuelta200_apertura.py
# escribiria SALIDA_V200_*.txt sin que nadie tenga que acordarse de cambiarlo.
LANZADOR = os.path.basename(os.path.abspath(__file__))
_m = re.match(r"^vuelta(\d+[a-z]?)_", LANZADOR)
if not _m:
    raise SystemExit("ROJO: el nombre %r no dice de que vuelta es. No se adivina."
                     % LANZADOR)
SUFIJO = _m.group(1).upper()
VUELTA = int(re.match(r"^(\d+)", _m.group(1)).group(1))

SUJETOS = [
    "scripts/loop/vuelta183_bateria_por_tramos.py",
    "scripts/loop/vuelta165_tarea2_mutacion_censo.py",
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/serie_de_registros.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/aislador_de_ciega.py",
    "scripts/loop/vuelta183b_tarea1f_relectura_al_doble.py",
    "scripts/loop/vuelta182_tarea3_diferenciador_movido.py",
    "scripts/loop/vuelta183b_tarea1a_registrar_acta183.py",
    "scripts/loop/cotejar_clon_declarado.py",
    "scripts/loop/archivar_reporte.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/SALIDA_V183_BATERIA_TRAMO_1.txt",
    "docs/loop/SALIDA_V183_BATERIA_TRAMO_2.txt",
    "docs/loop/SALIDA_V183_BATERIA_TRAMO_3.txt",
    "docs/loop/SALIDA_V183_BATERIA_TRAMO_4.txt",
    "docs/loop/SALIDA_V183_BATERIA_TRAMO_5.txt",
    "docs/loop/SALIDA_V183_LANZADOR_TRAMO_5.txt",
    "docs/loop/SALIDA_V183_BATERIA.txt",
    "docs/loop/_auditor_v185_ciega_blind.txt",
    "docs/loop/SELLO_APERTURA_AUDITOR_V185.json",
    "docs/loop/reportes/REPORTE_V183.md",
    "docs/PENDIENTES.md",
    "docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "scripts/loop/guarda_commit_dataset.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/anexar_tarea_al_reporte.py",
    "scripts/loop/tallar_cabecera_reporte.py",
] + SUJETOS

REGISTRO_SC = os.path.join(RAIZ, "docs", "plan", "SUJETO_CONGELADO_VEREDICTOS.jsonl")


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env, shell=shell)
    out = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    return r.returncode, out


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def bytes_de_git(ruta):
    c, o = git(["cat-file", "-s", "HEAD:" + ruta])
    o = o.strip()
    return int(o) if c == 0 and o.isdigit() else None


def sha_de(ruta):
    """SHA256 POR LAS DOS CONVENCIONES: crudo de disco y normalizado a LF."""
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (hashlib.sha256(datos).hexdigest(), hashlib.sha256(lf).hexdigest(),
            len(datos), len(lf))


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V%s_%s_APERTURA.txt" % (SUFIJO, nombre))
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("ESCRITO: %s (%d bytes)" % (os.path.basename(ruta), len(texto.encode("utf-8"))))


lineas = []
w = lineas.append
NL = chr(10)
w("SELLO DE APERTURA DE LA VUELTA %d, escrito ANTES de la primera operacion." % VUELTA)
w("Sufijo de salidas: %s (computado de %s, no tecleado)" % (SUFIJO, LANZADOR))
w("regimen: VUELTA DE BATERIA. AUDITOR.md 6.1: una vuelta cortada RETOMA EN EL")
w("         TRAMO SIGUIENTE y la bateria se declara corrida cuando los NUEVE")
w("         tramos tienen salida sellada del mismo calibre. El acta 184, punto 8,")
w("         mide 5 de 9 y manda retomar en el TRAMO 6, con el 5 re-corrido.")
w("         Esta vuelta ABRE REPORTE PROPIO y archiva el de la 183 en su PASO 0.")
w("         DOS sub-tareas, que es el tope del regimen temporal 6.2, y el acta")
w("         184 punto 8 lo remide: la 182 cerro su reporte y la 183 NO.")
w("")

w("=== A. HEAD DE APERTURA (git rev-parse HEAD) ===")
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

w("=== B.1 LA CADENA DE LA VUELTA 183, LOCALIZADA EN GIT Y NO TECLEADA ===")
w("(no se teclea ningun hash: se busca en el log el commit de cada pieza de la")
w(" 183 y se imprime lo que salga)")
c, logtodo = git(["log", "--format=%h%x09%s", "-120"])
for etiqueta, aguja in (("acta 182", "ACTA DEL AUDITOR, VUELTA 182"),
                        ("acta 183", "ACTA DEL AUDITOR, VUELTA 183"),
                        ("tramo 1", "BATERIA TRAMO 1 DE 9"),
                        ("tramo 2", "BATERIA TRAMO 2 DE 9"),
                        ("tarea 1 de la 183", "VUELTA 183, TAREA 1 CERRADA")):
    hits = [l for l in logtodo.splitlines() if aguja.upper() in l.upper()]
    w("   %-18s -> %s"
      % (etiqueta, (hits[0][:150] if hits else "NO LOCALIZADO EN LOS 120 ULTIMOS")))
w("")

w("=== C. git status --porcelain ENTERO ===")
c, st = git(["status", "--porcelain"])
for l in st.splitlines():
    w(l)
w("CIFRA lineas de status: %d" % len([l for l in st.splitlines() if l.strip()]))
w("")

w("=== D. BYTES DE CADA RUTA QUE EL ENCARGO NOMBRA, POR LAS DOS CONVENCIONES ===")
for ruta in RUTAS_DEL_ENCARGO:
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    g = bytes_de_git(ruta)
    if os.path.exists(p):
        w("%s -> disco %d bytes | git %s"
          % (ruta, os.path.getsize(p),
             ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
    else:
        w("%s -> disco NO EXISTE | git %s"
          % (ruta, ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("")

w("=== E. DIFF REAL EN BYTES DE LOS MODIFICADOS (cambio contra suciedad) ===")
c, mod = git(["ls-files", "-m"])
n_mod = 0
for ruta in [l for l in mod.splitlines() if l.strip()]:
    n_mod += 1
    c2, d = git(["diff", "--", ruta])
    w("%s -> diff de %d bytes" % (ruta, len(d.encode("utf-8"))))
    c3, dn = git(["diff", "--numstat", "--", ruta])
    w("   %s -> git diff --numstat: %d filas"
      % (ruta, len([l for l in dn.splitlines() if l.strip()])))
w("CIFRA ficheros modificados: %d" % n_mod)
c, dnd = git(["diff", "--numstat", "--", "dataset/"])
w("CIFRA filas de `git diff --numstat -- dataset/` AL ENTRAR: %d"
  % len([l for l in dnd.splitlines() if l.strip()]))
w("")

w("=== F. LO NO SEGUIDO POR GIT, FICHERO A FICHERO CON SUS BYTES ===")
c, unt = git(["status", "--porcelain", "--untracked-files=all"])
n_unt = 0
for l in unt.splitlines():
    if l.startswith("?? "):
        r = l[3:].strip().strip(chr(34))
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        tam = os.path.getsize(p) if os.path.isfile(p) else -1
        w("%s -> %s" % (r, ("%d bytes" % tam) if tam >= 0 else "(no es fichero)"))
        n_unt += 1
w("CIFRA ficheros no seguidos: %d" % n_unt)
w("")

w("=== G. git ls-tree DE HEAD SOBRE ESAS RUTAS ===")
for ruta in RUTAS_DEL_ENCARGO:
    c, t = git(["ls-tree", "HEAD", "--", ruta])
    w("%s -> %s" % (ruta, t.strip() if t.strip() else "NO ESTA EN EL ARBOL DE HEAD"))
w("")

w("=== H. EL REPORTE EN HEAD, MEDIDO SIN CREERLE AL ENCARGO ===")
w("(el encargo dice que el de la 183 sigue SIN CERRAR y SIN ARCHIVAR y que su")
w(" archivado es el PASO 0 de esta vuelta. Aqui se mide que es y en que estado")
w(" esta, sin tocarlo y antes de archivar nada)")
c, rep = git(["show", "HEAD:docs/loop/REPORTE.md"])
w("primera linea: %s" % (rep.split(NL, 1)[0].strip() if rep else "(vacio)"))
w("lineas (saltos de linea contados): %d" % rep.count(NL))
w("bytes en git: %d" % len(rep.encode("utf-8")))
MARCAS = ["SIN ESCRIBIR TODAVIA", "PENDIENTE DE TALLAR AL CIERRE",
          "ABIERTA, SIN CERRAR", "CERRADA",
          "<!-- TABLA DE TAREAS -->", "<!-- FIN TABLA DE TAREAS -->",
          "<!-- ANEXO DE TAREAS -->", "<!-- FIN ANEXO DE TAREAS -->",
          "<!-- CABECERA TALLADA -->"]
MARCAS = MARCAS + [NL + "## %d." % k for k in range(3, 10)]
for marca in MARCAS:
    w("   contiene %-40s -> %s" % (repr(marca), "SI" if marca in rep else "NO"))
RUTA_REP = os.path.join(LOOP, "REPORTE.md")
arbol = io.open(RUTA_REP, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("EL DEL ARBOL: bytes LF %d | saltos de linea %d | disco crudo %d"
  % (len(arbol.encode("utf-8")), arbol.count(NL), os.path.getsize(RUTA_REP)))
w("identico byte a byte al de HEAD: %s"
  % ("SI" if arbol == rep.replace(chr(13) + NL, NL) else "NO"))
w("FILAS DE LA TABLA DE TAREAS, CONTADAS DE SU TABLA Y NO RECORDADAS:")
dentro = False
n_filas = 0
for i, l in enumerate(arbol.split(NL), 1):
    if "<!-- TABLA DE TAREAS -->" in l:
        dentro = True
        continue
    if "<!-- FIN TABLA DE TAREAS -->" in l:
        dentro = False
        continue
    if dentro and re.search(r"TAREA\s+\d+", l) and l.strip().startswith("|"):
        n_filas += 1
        w("   LINEA %d: %s" % (i, l.strip()[:110]))
w("CIFRA filas de tarea en la tabla: %d" % n_filas)
w("")

w("=== H.1 EL REPORTE DE LA 183, SU ESTADO DE CIERRE MEDIDO ANTES DE ARCHIVARLO ===")
w("(el encargo afirma que sigue SIN CERRAR. Aqui NO se le cree: se buscan las")
w(" marcas del cierre en el texto del arbol y se publica lo que salga)")
for marca in ("EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA",
              "PENDIENTE DE TALLAR AL CIERRE", "ABIERTA, SIN CERRAR",
              "cerrar_reporte.py"):
    hits = [i for i, l in enumerate(arbol.split(NL), 1) if marca in l]
    w("   %-52s -> %d aparicion(es), lineas %s"
      % (repr(marca), len(hits), ", ".join(str(x) for x in hits[:10]) or "(ninguna)"))
w("   CIFRA rutas 'docs/loop/SALIDA_V183' citadas en el reporte: %d"
  % arbol.count("docs/loop/SALIDA_V183"))
w("")

w("=== H.2 LAS CINCO SALIDAS SELLADAS DE LA BATERIA, MEDIDAS UNA A UNA ===")
w("(el acta 184 punto 3.3 publica una tabla de cinco filas. Aqui se remiden con")
w(" las dos convenciones y su exitcode, sin copiar ni una celda del acta)")
for i in range(1, 10):
    for pre in ("SALIDA_V183_BATERIA_TRAMO_%d.txt", "SALIDA_V183_LANZADOR_TRAMO_%d.txt"):
        n = pre % i
        p = os.path.join(LOOP, n)
        if not os.path.exists(p):
            w("   %-34s NO EXISTE" % n)
            continue
        sd, sl, bd, bl = sha_de(p)
        tx = io.open(p, encoding="utf-8", errors="replace").read().replace(chr(13) + NL, NL)
        ex = [l.strip() for l in tx.split(NL) if "EXITCODE" in l.upper()]
        w("   %-34s disco %6d | LF %6d | lineas %4d | sha256 LF %s"
          % (n, bd, bl, tx.count(NL), sl[:16]))
        for l in ex[:3]:
            w("        %s" % l[:110])
w("")

w("=== H.3 EL LANZADOR DE LA BATERIA, SUS LITERALES DE VUELTA, MEDIDOS ===")
RBT = "scripts/loop/vuelta183_bateria_por_tramos.py"
BT = os.path.join(RAIZ, RBT.replace("/", os.sep))
t_bt = io.open(BT, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_bt = t_bt.split(NL)
g_bt = bytes_de_git(RBT)
w("   %s -> %d lineas | disco %d bytes | git %s"
  % (RBT, len(l_bt), os.path.getsize(BT),
     ("%d bytes" % g_bt) if g_bt is not None else "NO ESTA EN HEAD"))
w("   LAS LINEAS QUE ESCRIBEN O IMPRIMEN UN '176', LOCALIZADAS Y NO TECLEADAS:")
for i, l in enumerate(l_bt, 1):
    if "176" in l and (l.strip().startswith("print(") or l.strip().startswith("f.write(")
                       or l.strip().startswith("cab.append(") or "mkdtemp" in l):
        w("      LINEA %d: %s" % (i, l.strip()[:140]))
w("   CIFRA lineas del fichero que contienen '176': %d"
  % len([l for l in l_bt if "176" in l]))
w("   LAS DOS LINEAS DE ESTIMACION QUE LA TAREA 1.c TIENE QUE REPARAR,")
w("   LOCALIZADAS HOY Y NO TECLEADAS:")
for i, l in enumerate(l_bt, 1):
    if "ESTIMACION" in l:
        w("      LINEA %d: %s" % (i, l.strip()[:140]))
w("   CIFRA lineas del fichero que contienen 'ESTIMACION': %d"
  % len([l for l in l_bt if "ESTIMACION" in l]))
w("   CIFRA lineas que contienen 'V183' o 'vuelta183': %d"
  % len([l for l in l_bt if "V183" in l or "vuelta183" in l]))
for i, l in enumerate(l_bt, 1):
    if "V183" in l or "vuelta183" in l:
        w("      LINEA %d: %s" % (i, l.strip()[:140]))
w("")

w("=== H.3B EL ARNES QUE PARO LA BATERIA, MEDIDO ANTES DE TOCARLO ===")
w("(TAREA 1.b. LO QUE PASABA ANTES NO SE BORRA, SE CUENTA: aqui se localiza la")
w(" lista TECLEADA y se mide, sin cambiar una linea, cuantos invisibles hay hoy)")
RMC = "scripts/loop/vuelta165_tarea2_mutacion_censo.py"
MC = os.path.join(RAIZ, RMC.replace("/", os.sep))
t_mc = io.open(MC, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_mc = t_mc.split(NL)
w("   %s -> %d lineas | disco %d bytes" % (RMC, len(l_mc), os.path.getsize(MC)))
for i, l in enumerate(l_mc, 1):
    if "esperadas" in l:
        w("      LINEA %d: %s" % (i, l.strip()[:140]))
c_mc, o_mc = correr([PY, RMC])
w("   EXITCODE del arnes corrido HOY, antes de tocarlo: %d" % c_mc)
for l in o_mc.replace(chr(13), "").split(NL):
    if ("FALLA" in l or "NO CAE" in l or l.strip().startswith("CIFRA")
            or l.strip().startswith("ROJO") or l.strip().startswith("VERDE")
            or "invisibles" in l or "patron VIEJO" in l):
        w("      | " + l.rstrip()[:150])
w("")

w("=== H.4 LA SERIE DE REGISTROS Y EL ACTA 184, PARA LA TAREA 1.a ===")
w("(no se teclea ningun numero de registro: se llama a serie_de_registros.py y")
w(" se imprime lo que devuelva)")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
t_acta = io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_acta = t_acta.split(NL)
w("docs/loop/ACTA_AUDITOR.md -> %d lineas | disco %d bytes | LF %d bytes"
  % (len(l_acta), os.path.getsize(ACTA), len(t_acta.encode("utf-8"))))
CAB184 = [i for i, l in enumerate(l_acta, 1)
          if l.startswith("# ACTA DEL AUDITOR, VUELTA 184")]
w("CIFRA cabeceras del acta 184 encontradas: %d" % len(CAB184))
if CAB184:
    base = CAB184[0]
    w("   CABECERA del acta 184 en la LINEA %d" % base)
    w("   lineas del acta 184, de su cabecera al final del fichero: %d"
      % (len(l_acta) - base + 1))
    for aguja in ("## 1. ", "## 2. ", "## 3. ", "## 4. ", "## 5. ", "## 6. ",
                  "## 7. ", "## 8. ", "## 9. ", "**5.1 ", "**5.2 ", "**5.3 ",
                  "**5.4 ", "**5.5 ", "**5.6 ", "**5.7 "):
        hits = [i for i, l in enumerate(l_acta, 1)
                if l.startswith(aguja) and i >= base]
        w("   %-10s -> lineas %s"
          % (repr(aguja), ", ".join(str(x) for x in hits) or "(ninguna)"))
    w("   LA ADJUDICACION DEL PUNTO 6, QUE NO LLEVA NUMERAL 5.n Y HAY QUE CONTAR")
    w("   APARTE O EL CONTADOR LA PIERDE:")
    for i, l in enumerate(l_acta, 1):
        if i >= base and l.startswith("## 6. "):
            w("      LINEA %d: %s" % (i, l.strip()[:140]))
    w("   LAS MARCAS DE CAIDA DEL EJECUTOR EN EL ACTA 184, BUSCADAS Y NO SUPUESTAS:")
    for pat in (r"`E\.\d+`", r"\*\*E\.\d+", r"`C\.\d+`", r"NINGUNA CAIDA PROPIA"):
        hits = [i for i, l in enumerate(l_acta, 1)
                if i >= base and re.search(pat, l)]
        w("      %-24s -> %d aparicion(es), lineas %s"
          % (pat, len(hits), ", ".join(str(x) for x in hits[:12]) or "(ninguna)"))
try:
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import serie_de_registros as SER   # noqa: E402
    halladas = SER.entradas()
    w("serie_de_registros.entradas() -> %d entradas en %d sedes"
      % (len(halladas), len(SER.SEDES)))
    for s in SER.SEDES:
        w("   SEDE: %s" % os.path.relpath(s, RAIZ).replace(os.sep, "/"))
    w("CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SER.colisiones(halladas)), len(SER.huecos(halladas))))
    w("SIGUIENTE LIBRE, LLAMADO Y NO TECLEADO: R.%s"
      % SER.siguiente_libre(halladas))
    for numero, rel, linea, titulo in halladas[-4:]:
        w("   ULTIMOS: R.%s en %s:%d -> %s" % (numero, rel, linea, titulo[:100]))
except Exception as e:
    w("NO SE PUDO RECOMPUTAR LA SERIE: %r" % (e,))
w("")

w("=== H.5 EL TRAMO DE LA CIEGA DEL AUDITOR Y SU SELLO (TAREA 1.d) ===")
w("(el encargo manda cotejar el sha256 del fichero ciego contra el sello ANTES")
w(" de releer nada. AQUI NO SE COPIA EL DEL ENCARGO: se computa y se compara)")
CIEGA = os.path.join(LOOP, "_auditor_v185_ciega_blind.txt")
SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_V185.json")
if os.path.exists(SELLO):
    w("   %s -> disco %d bytes" % ("docs/loop/SELLO_APERTURA_AUDITOR_V185.json",
                                   os.path.getsize(SELLO)))
    sello = json.loads(io.open(SELLO, encoding="utf-8").read())
    w("   CLAVES DEL SELLO: %s" % ", ".join(sorted(sello.keys())))
    w("   EL SELLO ENTERO, PEGADO Y NO RESUMIDO:")
    for l in json.dumps(sello, indent=2, ensure_ascii=False).split(NL):
        w("      | " + l[:150])
else:
    w("   EL SELLO NO EXISTE. Sin el no se relee nada, y eso se dice.")
if os.path.exists(CIEGA):
    sd, sl, bd, bl = sha_de(CIEGA)
    w("   docs/loop/_auditor_v185_ciega_blind.txt -> disco %d bytes | LF %d bytes"
      % (bd, bl))
    w("   sha256 (disco): %s" % sd)
    w("   sha256 (LF)   : %s" % sl)
    t_c = io.open(CIEGA, encoding="utf-8", errors="replace").read().replace(chr(13) + NL, NL)
    l_c = t_c.split(NL)
    w("   lineas: %d" % len(l_c))
    w("   LAS DOCE PRIMERAS, PEGADAS:")
    for l in l_c[:12]:
        w("      | " + l[:150])
    puestos = sorted({int(x) for x in re.findall(r"PUESTO\s+(\d+)", t_c)})
    w("   CIFRA puestos localizados con el patron 'PUESTO <n>': %d" % len(puestos))
    w("   LOS PUESTOS: %s" % ", ".join(str(x) for x in puestos))
else:
    w("   EL FICHERO CIEGO NO EXISTE. No se relee nada, y eso se dice.")
w("")

w("=== H.6 LA BATERIA: SU REPARTO Y QUE TRAMO TOCA, CORRIDOS HOY ===")
w("EL REPARTO, CORRIDO HOY CON --plan Y NO COPIADO DEL ENCARGO:")
c_pl, o_pl = correr([PY, RBT, "--plan"])
w("   EXITCODE de --plan: %d" % c_pl)
for l in o_pl.replace(chr(13), "").split(NL):
    if l.strip():
        w("      | " + l.rstrip()[:150])
w("QUE TRAMO TOCA, CORRIDO HOY CON --siguiente:")
c_sg, o_sg = correr([PY, RBT, "--siguiente"])
w("   EXITCODE de --siguiente: %d" % c_sg)
for l in o_sg.replace(chr(13), "").split(NL):
    if l.strip():
        w("      | " + l.rstrip()[:150])
try:
    import verificar_mutaciones_viejas as VMV   # noqa: E402
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _a in VMV.VIEJAS]
    w("   CIFRA censo: %d | CIFRA nomina: %d | VARA_DEL_CENSO: %d"
      % (len(censo), len(nomina), VMV.VARA_DEL_CENSO))
    w("   TOPE_DE_MINUTOS_POR_TRAMO = %s" % VMV.TOPE_DE_MINUTOS_POR_TRAMO)
    ultima, faltan = VMV.arneses_que_faltan()
    w("   arneses_que_faltan() HOY: ultima vuelta %s, faltan %d" % (ultima, len(faltan)))
    for n in faltan:
        w("      FALTA: %s" % n)
    invis = VMV.nomina_invisible_al_censo()
    w("   nomina_invisible_al_censo(): %d" % len(invis))
    for n in invis:
        w("      INVISIBLE: %s" % n)
    malas = VMV.guarda_del_sujeto_congelado()
    w("   guarda_del_sujeto_congelado(): %d entradas sin congelar" % len(malas))
    for nombre, veredicto, vive in malas:
        w("      SUJETO SIN CONGELAR: %-46s %s" % (nombre, veredicto))
except Exception as e:
    w("   NO SE PUDO RECOMPUTAR EL CENSO: %r" % (e,))
if os.path.exists(REGISTRO_SC):
    filas_sc = [json.loads(l) for l in io.open(REGISTRO_SC, encoding="utf-8") if l.strip()]
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> %d filas, disco %d bytes"
      % (len(filas_sc), os.path.getsize(REGISTRO_SC)))
else:
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> NO EXISTE")
w("")

w("=== H.7 LAS PIEZAS QUE cerrar_reporte.py PEDIRA PARA CERRAR LA 184 ===")
for r in ["docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt",
          "scripts/loop/_v184_cierre_texto.md",
          "docs/loop/SALIDA_V183_BATERIA.txt",
          "docs/loop/SALIDA_V184_BATERIA.txt"]:
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    w("   %s -> %s" % (r, ("%d bytes" % os.path.getsize(p))
                       if os.path.exists(p) else "NO EXISTE"))
CER = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
t_cer = io.open(CER, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_cer = t_cer.split(NL)
w("   scripts/loop/cerrar_reporte.py -> %d lineas | disco %d bytes"
  % (len(l_cer), os.path.getsize(CER)))
for aguja in ("--bateria", "SALIDA_V", "def numerales_del_veredicto",
              "def caidas_propias_del_cuerpo", "def tareas_de_la_tabla",
              "def numerales_del_veredicto_que_no_calzan",
              "def frase_del_caso_del_hueco"):
    hits = [(i, l) for i, l in enumerate(l_cer, 1) if aguja in l]
    w("   %-44s -> %d aparicion(es), lineas %s"
      % (repr(aguja), len(hits), ", ".join(str(i) for i, _l in hits[:10])))
w("")

w("=== H.8 QUE REPORTES ESTAN YA ARCHIVADOS EN docs/loop/reportes/ ===")
DIRA = os.path.join(LOOP, "reportes")
arch = sorted(os.listdir(DIRA)) if os.path.isdir(DIRA) else []
for n in arch[-8:]:
    g = bytes_de_git("docs/loop/reportes/" + n)
    w("   %s -> disco %d bytes | git %s"
      % (n, os.path.getsize(os.path.join(DIRA, n)),
         ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("CIFRA reportes archivados: %d" % len(arch))
for n in ("REPORTE_V182.md", "REPORTE_V183.md", "REPORTE_V184.md"):
    w("%s archivado: %s" % (n, "SI" if n in arch else "NO"))
w("")

w("=== H.9 EL ARCHIVO DE VEREDICTOS, QUE ESTA VUELTA NO PUEDE MOVER ===")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
datos_ver = io.open(VER, "rb").read()
w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> disco %d bytes | LF %d bytes"
  % (os.path.getsize(VER), len(datos_ver.replace(chr(13).encode(), b""))))
w("   sha256 (disco): %s" % hashlib.sha256(datos_ver).hexdigest())
w("   sha256 (LF)   : %s"
  % hashlib.sha256(datos_ver.replace((chr(13) + NL).encode(), NL.encode())).hexdigest())
filas = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
w("   CIFRA filas: %d" % len(filas))
por_clase = {}
for f in filas:
    por_clase[f.get("clase")] = por_clase.get(f.get("clase"), 0) + 1
for k in sorted(por_clase, key=lambda x: (x is None, x)):
    w("   CIFRA clase %-6s: %d" % (repr(k), por_clase[k]))
puestos_v = [f.get("puesto_intra") for f in filas]
w("   MIN puesto %s | MAX puesto %s | HUECOS %d | DUPLICADOS %d"
  % (min(puestos_v), max(puestos_v),
     len(set(range(min(puestos_v), max(puestos_v) + 1)) - set(puestos_v)),
     len(puestos_v) - len(set(puestos_v))))
w("")

w("FIN DEL SELLO DE APERTURA")

texto = NL.join(lineas) + NL
io.open(os.path.join(LOOP, "SALIDA_V%s_APERTURA.txt" % SUFIJO), "w",
        encoding="utf-8", newline=NL).write(texto)
print(texto)
escribir("HEAD", head + NL)

# ------------------------------------------------- B. EL BLOQUE DE MEDICIONES
c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
escribir("GATE0_CMD1", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
escribir("CICLO_ETIQUETAS", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/sync_assets_web.py"])
escribir("CICLO_SYNC", o + "\nEXITCODE: %d\n" % c)

c, o = correr(["git", "diff", "HEAD", "--numstat", "--", "dataset/", "web/", "engine/"])
escribir("CICLO_NUMSTAT", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
escribir("CONTEO", o + "\nEXITCODE: %d\n" % c)

# EL DESFASE DEL CALIBRADO, EN SU SITIO Y NO AL CIERRE. Desde la 178, con el
# remedio de la 177 puesto y verificado, la columna de apertura medida al cierre
# pasa a ser CAIDA QUE ACUMULA. Aqui corre en la apertura, antes de la primera
# operacion, que es donde EJECUTOR.md 1 la manda.
c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + "\nEXITCODE: %d\n" % c)

c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d\n" % c)

c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + "\nEXITCODE: %d\n" % c)

print("BLOQUE DE APERTURA COMPLETO")
