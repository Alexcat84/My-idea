# -*- coding: utf-8 -*-
r"""vuelta180_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 180, ENTERO.

CLON DECLARADO de scripts/loop/vuelta179_apertura.py. Cambia el numero de
vuelta, el prefijo de las salidas, la lista RUTAS_DEL_ENCARGO y el bloque H, que
aqui mide lo que ESTE encargo promete y nada mas.

Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA. Desde la vuelta 178 ningun
reporte escribe "CLON DECLARADO" sin pegar la salida de
scripts/loop/cotejar_clon_declarado.py (ultima linea del docstring de ese
fichero antes del USO). Este docstring NO afirma que el diff salga vacio: la
vuelta 176 cayo por eso, y el cotejo de este clon se pega en el reporte.

ESTA VUELTA NO ES DE BATERIA Y LA SIGUIENTE SI. La cadencia esta adjudicada en
el acta 176 punto 7.8 y reconfirmada en las actas 178 punto 11 y 179 punto 11:
la proxima vuelta de bateria es la 181. Por eso la seccion 9 del reporte cerrara
con el HUECO DECLARADO Y MEDIDO, y el bloque H de esta apertura NO mide la
nomina como sujeto de bateria: mide LOS SUJETOS DE LAS CINCO TAREAS.

EL TOPE SIGUE EN CINCO SUB-TAREAS: el disparador de AUDITOR.md 6.2 se cumplio en
la 177, y la 178 y la 179 lo confirmaron entregando cinco. El bloque B.1 de abajo
LOCALIZA EN GIT los commits de cierre y de archivo de la 178 y de la 179 en vez
de teclearlos, porque EJECUTOR.md 1 dice que todo hash que el reporte publique se
lee de git en esa vuelta.

EL BLOQUE H NO TECLEA NINGUN HASH NI NINGUNA CIFRA. Todo se localiza y se imprime
lo que salga. Las cifras vivas de la nomina, del censo, de la guarda del sujeto
congelado, de los triangulos y del backlog NO se copian del encargo ni del acta:
se recomputan corriendo los propios instrumentos, que es la unica fuente que la
casa reconoce (EJECUTOR.md 2, EL INSTRUMENTO MANDA). El encargo da cifras (17 de
103, 15 etiquetados con 5 falsos, 19 triangulos y 57 lados, 6/29/8 y 34/44/10);
aqui NO SE COPIA NINGUNA: se corre y se imprime lo que salga, y la comparacion
con lo que el encargo dice se hace despues, en el reporte, con las dos al lado.

LA CIFRA DE BYTES SE PUBLICA POR LAS DOS CONVENCIONES mientras la convencion no
este fijada (acta 177 punto 7.11, y sigue sin fijar): disco (os.path.getsize) y
git (git cat-file -s), las dos a la vez.

POR QUE SE CORRE AQUI: EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION". Este fichero NO toca REPORTE.md, NO toca la nomina, NO corre
la bateria y NO escribe en docs/plan/: sus salidas son SALIDA_V180_*.txt.

Y LA MEDICION DE DESFASE DEL CALIBRADO SE TOMA AQUI, EN SU SITIO: desde la 178
una columna de apertura medida al cierre es CAIDA QUE ACUMULA. Aqui corre dentro
del bloque B, antes de toda operacion.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

LO QUE ESTA VUELTA SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano al abrir la vuelta, dio CERO
lineas. La prediccion se escribe AQUI, antes de correr, y los bloques C/D/E/F de
abajo la miden sin saber lo que hay escrito.

USO:
  python scripts/loop/vuelta180_apertura.py
"""
import hashlib
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
VUELTA = 180

# LOS SUJETOS DE CODIGO DE LAS CINCO TAREAS, nombrados aqui para que el bloque H
# no los pueda elegir despues de ver el resultado.
SUJETOS = [
    "scripts/loop/vuelta178_tarea3_anotar_triangulos.py",
    "scripts/loop/vuelta179_tarea3_etiqueta_de_fuente.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/vuelta157_tarea4b_mutacion_tachado.py",
    "scripts/loop/vuelta160_tarea7c_mutacion_guarda_cita.py",
    "scripts/loop/vuelta174_tarea1b_mutacion_esqueleto.py",
    "scripts/loop/vuelta150_2d_simular_op_c_05.py",
    "scripts/loop/backlog_l03_resuelto.py",
    "scripts/loop/backlog_l03_vuelta14.py",
    "scripts/loop/vuelta179_tarea2_cobertura_final.py",
    "scripts/loop/paso0_archivar_anterior.py",
    "scripts/loop/vuelta174_esqueleto_reporte.py",
    "scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py",
    "scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/reportes/REPORTE_V179.md",
    "docs/plan/OP_L_03_TRIANGULOS.jsonl",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/OP_L_03_LECTURAS.jsonl",
    "docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl",
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "scripts/loop/guarda_commit_dataset.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/anexar_tarea_al_reporte.py",
    "scripts/loop/tallar_cabecera_reporte.py",
    "scripts/loop/cerrar_reporte.py",
] + SUJETOS

# LOS DIECISIETE DEL SUJETO CONGELADO NO SE TECLEAN: se leen del registro que la
# 179 escribio, y si el registro no esta se dice y no se inventa la lista.
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
    """Los bytes que git guarda para esa ruta en HEAD, o None si no esta.
    LA SEGUNDA CONVENCION del hallazgo 4.1 del acta 174, medida y no supuesta."""
    c, o = git(["cat-file", "-s", "HEAD:" + ruta])
    o = o.strip()
    return int(o) if c == 0 and o.isdigit() else None


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V%d_%s_APERTURA.txt" % (VUELTA, nombre))
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("ESCRITO: %s (%d bytes)" % (os.path.basename(ruta), len(texto.encode("utf-8"))))


# ---------------------------------------------------------------- A. EL SELLO
lineas = []
w = lineas.append
NL = chr(10)
w("SELLO DE APERTURA DE LA VUELTA %d, escrito ANTES de la primera operacion" % VUELTA)
w("instrumento: scripts/loop/vuelta%d_apertura.py" % VUELTA)
w("regimen: VUELTA NORMAL, NO DE BATERIA (la proxima es la 181, y es la")
w("         SIGUIENTE). CINCO sub-tareas, la 1 y la 2 BLOQUEANTES y en ese")
w("         orden. El tope de cinco de AUDITOR.md 6.2 sigue vigente, y el")
w("         bloque B.1 de abajo lo LOCALIZA EN GIT en vez de teclearlo.")
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
w("adelante/atras contra el remoto (HEAD...upstream): " + (ahead.strip() if c == 0 else "(no medible)"))
w("")

w("=== B.1 LOS CUATRO COMMITS QUE SOSTIENEN EL TOPE DE CINCO, LOCALIZADOS EN GIT ===")
w("(AUDITOR.md 6.2: el regimen de dos dura HASTA QUE DOS VUELTAS SEGUIDAS")
w(" CIERREN SU PROPIO REPORTE con cerrar_reporte.py. No se teclea ningun hash:")
w(" se busca en el log el commit de CIERRE y el de ARCHIVO de la 178 y de la 179)")
c, logtodo = git(["log", "--format=%h%x09%s", "-40"])
for etiqueta, aguja in (("178 cierre", "REPORTE DE LA 178"),
                        ("178 archivo", "REPORTE_V178.md"),
                        ("179 cierre", "REPORTE DE LA 179"),
                        ("179 archivo", "REPORTE_V179.md")):
    hits = [l for l in logtodo.splitlines() if aguja.upper() in l.upper()]
    w("   %-12s -> %s" % (etiqueta, (hits[0][:150] if hits else "NO LOCALIZADO EN LOS 40 ULTIMOS")))
c, n_cerrar = git(["log", "--format=%h", "-40", "--", "scripts/loop/cerrar_reporte.py"])
w("   commits que tocan cerrar_reporte.py en los 40 ultimos: %d"
  % len([l for l in n_cerrar.splitlines() if l.strip()]))
w("")

w("=== C. git status --porcelain ENTERO ===")
c, st = git(["status", "--porcelain"])
for l in st.splitlines():
    w(l)
w("CIFRA lineas de status: %d" % len([l for l in st.splitlines() if l.strip()]))
w("")

w("=== D. BYTES DE CADA RUTA QUE EL ENCARGO NOMBRA, POR LAS DOS CONVENCIONES ===")
w("(disco = os.path.getsize; git = git cat-file -s HEAD:<ruta>. Acta 177 punto")
w(" 7.11: mientras la convencion no este fijada, SE PUBLICAN LAS DOS)")
for ruta in RUTAS_DEL_ENCARGO:
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    g = bytes_de_git(ruta)
    if os.path.exists(p):
        w("%s -> disco %d bytes | git %s"
          % (ruta, os.path.getsize(p), ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
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
    w("   %s -> git diff --numstat: %d filas" % (ruta, len([l for l in dn.splitlines() if l.strip()])))
w("CIFRA ficheros modificados: %d" % n_mod)
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
c, rep = git(["show", "HEAD:docs/loop/REPORTE.md"])
w("primera linea: %s" % (rep.split(NL, 1)[0].strip() if rep else "(vacio)"))
w("lineas (saltos de linea contados): %d" % rep.count(NL))
w("bytes en git: %d" % len(rep.encode("utf-8")))
MARCAS = ["SIN ESCRIBIR TODAVIA", "PENDIENTE DE TALLAR AL CIERRE",
          "ABIERTA, SIN CERRAR", "HUECO DECLARADO Y MEDIDO"]
MARCAS = MARCAS + [NL + "## %d." % k for k in range(3, 10)]
for marca in MARCAS:
    w("   contiene %-34s -> %s" % (repr(marca), "SI" if marca in rep else "NO"))
w("")

w("=== H.1 EL REPORTE DEL ARBOL, QUE ES EL QUE EL ESQUELETO DE LA 180 PISARA ===")
RUTA_REP = os.path.join(LOOP, "REPORTE.md")
arbol = io.open(RUTA_REP, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("primera linea: %s" % arbol.split(NL, 1)[0].strip())
w("bytes en disco (normalizado a LF): %d | saltos de linea: %d"
  % (len(arbol.encode("utf-8")), arbol.count(NL)))
w("bytes en disco (crudos, os.path.getsize): %d" % os.path.getsize(RUTA_REP))
w("identico byte a byte al de HEAD: %s"
  % ("SI" if arbol == rep.replace(chr(13) + NL, NL) else "NO"))
for marca in MARCAS:
    w("   contiene %-34s -> %s" % (repr(marca), "SI" if marca in arbol else "NO"))
w("")

w("=== H.2 EL COMMIT QUE DE VERDAD TOCA REPORTE.md POR ULTIMA VEZ ===")
w("(no se teclea ningun hash: se localiza con git log y se imprime lo que salga)")
c, cual = git(["log", "--format=%h%x09%s", "-8"])
w("los ocho ultimos commits:")
for l in cual.splitlines():
    w("   " + l[:150])
c, ult = git(["log", "-1", "--format=%h", "--", "docs/loop/REPORTE.md"])
w("ultimo commit que TOCA docs/loop/REPORTE.md: %s" % ult.strip())
c, asu = git(["log", "-1", "--format=%s", ult.strip()])
w("   su asunto: %s" % asu.strip()[:150])
w("")

w("=== H.3 LAS PIEZAS QUE cerrar_reporte.py PEDIRA PARA CERRAR LA 180 ===")
w("(al abrir NO EXISTE NINGUNA, y eso es lo correcto: las produce esta vuelta.")
w(" La de bateria NO SE VA A PRODUCIR: esta vuelta no es de bateria y la seccion")
w(" 9 cierra con el HUECO DECLARADO Y MEDIDO. La 181 la corre)")
for r in ["docs/loop/SALIDA_V180_TALLADOR_CABECERA.txt",
          "scripts/loop/_v180_cierre_texto.md",
          "docs/loop/SALIDA_V180_BATERIA.txt"]:
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        w("%s -> %d bytes" % (r, os.path.getsize(p)))
    else:
        w("%s -> NO EXISTE" % r)
w("")

w("=== H.4 QUE REPORTES ESTAN YA ARCHIVADOS EN docs/loop/reportes/ ===")
DIRA = os.path.join(LOOP, "reportes")
arch = sorted(os.listdir(DIRA)) if os.path.isdir(DIRA) else []
for n in arch:
    g = bytes_de_git("docs/loop/reportes/" + n)
    w("   %s -> disco %d bytes | git %s"
      % (n, os.path.getsize(os.path.join(DIRA, n)),
         ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("CIFRA reportes archivados: %d" % len(arch))
w("REPORTE_V179.md archivado: %s" % ("SI" if "REPORTE_V179.md" in arch else "NO"))
w("")

w("=== H.5 LA NOMINA Y EL CENSO, RECOMPUTADOS Y CON SU CORTE ===")
w("(el encargo NO da cifra de nomina ni de censo para esta vuelta, y aunque la")
w(" diera no se copiaria: se llaman las funciones puras del propio sujeto.")
w(" EL CORTE VA AL LADO por adjudicacion 7.2 del acta 178, porque el")
w(" denominador crece DENTRO de la propia vuelta)")
w("CORTE DE ESTA MEDICION: HEAD %s, APERTURA de la vuelta %d, antes de la" % (head[:12], VUELTA))
w("                        primera operacion de esta vuelta.")
try:
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_mutaciones_viejas as VMV   # noqa: E402
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _a in VMV.VIEJAS]
    invis = VMV.nomina_invisible_al_censo()
    fuera = sorted(set(censo) - set(nomina))
    w("CIFRA arneses que ve arneses_del_directorio(): %d" % len(censo))
    w("CIFRA entradas de VIEJAS (la nomina): %d" % len(nomina))
    w("CIFRA entradas de la nomina que el censo NO ve: %d" % len(invis))
    w("CIFRA del censo que estan FUERA de la nomina: %d" % len(fuera))
    for n in fuera:
        w("     FUERA: %s" % n)
    w("LA RESTA COMPROBADA: censo %d menos nomina %d = %d, y fuera de nomina = %d. CALZAN: %s"
      % (len(censo), len(nomina), len(censo) - len(nomina), len(fuera),
         "SI" if (len(censo) - len(nomina)) == len(fuera) else "NO"))
    ultima, faltan = VMV.arneses_que_faltan()
    w("arneses_que_faltan() HOY: ultima vuelta de la nomina %s, y dice que faltan %d"
      % (ultima, len(faltan)))
    for n in faltan:
        w("      FALTA: %s" % n)
    w("EL SELLO DE CORTE, LLAMADO Y NO PARAFRASEADO:")
    w("   sello_de_corte(len(VIEJAS), corte_de_git()) -> %s"
      % VMV.sello_de_corte(len(nomina), VMV.corte_de_git()))
except Exception as e:
    w("NO SE PUDO RECOMPUTAR: %r" % (e,))
w("")

w("=== H.6 TAREA 1: LA ETIQUETA DE FUENTE, MEDIDA ANTES DE ARREGLARLA ===")
w("(el encargo dice 15 etiquetados como de la 177, 10 verdaderos y 5 falsos.")
w(" NINGUNO SE COPIA: se corre el instrumento de la 179 y se imprime lo que salga)")
c, o = correr([PY, "scripts/loop/vuelta179_tarea3_etiqueta_de_fuente.py"])
w("comando: python scripts/loop/vuelta179_tarea3_etiqueta_de_fuente.py -> exit %d" % c)
for l in o.split(NL):
    if l.strip() and ("CIFRA" in l or "LA RESTA" in l or "acto `" in l):
        w("   " + l.rstrip()[:180])
w("EL SELLO DE LOS TRES REGISTROS QUE LA TAREA 1 PROMETE NO MOVER:")
for r in ("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", "docs/plan/OP_L_03_LECTURAS.jsonl",
          "docs/plan/OP_L_03_TRIANGULOS.jsonl"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        t = io.open(p, "rb").read()
        w("   %-42s sha256 disco %s" % (r, hashlib.sha256(t).hexdigest()))
        w("   %-42s sha256 LF    %s | disco %d bytes | LF %d bytes"
          % ("", hashlib.sha256(t.replace(chr(13).encode(), b"")).hexdigest(),
             os.path.getsize(p), len(t.replace(chr(13).encode(), b""))))
    else:
        w("   %-42s NO EXISTE" % r)
w("EL LITERAL CLAVADO, BUSCADO EN EL SUJETO Y CONTADO:")
SUJ_T3 = os.path.join(RAIZ, "scripts", "loop", "vuelta178_tarea3_anotar_triangulos.py")
t_t3 = io.open(SUJ_T3, encoding="utf-8").read().replace(chr(13) + NL, NL)
LITERAL = "docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)"
w("   CIFRA apariciones de %r en el sujeto: %d" % (LITERAL, t_t3.count(LITERAL)))
for i, l in enumerate(t_t3.split(NL), 1):
    if LITERAL in l:
        w("      LINEA %d: %s" % (i, l.strip()[:160]))
w("")

w("=== H.7 TAREA 2: LA GUARDA DEL SUJETO CONGELADO, CORRIDA ANTES DE TOCAR NADA ===")
w("(el encargo dice 17 de 103 al corte c348de45f70f, medido por el fundador. NO SE")
w(" COPIA: se corre la guarda y se cuenta su propia salida)")
c, o = correr([PY, "scripts/loop/verificar_mutaciones_viejas.py", "--sujeto-congelado"])
w("comando: verificar_mutaciones_viejas.py --sujeto-congelado -> exit %d" % c)
w("   CIFRA lineas no vacias de la salida: %d" % len([l for l in o.split(NL) if l.strip()]))
for etiqueta in ("SUJETO VIVO", "NO DECIDIBLE", "CASO DECLARADO", "CONGELADO"):
    w("   CIFRA lineas que dicen %-18s: %d"
      % (repr(etiqueta), len([l for l in o.split(NL) if etiqueta in l])))
for l in o.split(NL):
    if l.strip() and ("CIFRA" in l or "ROJO" in l or "VERDE" in l):
        w("   " + l.rstrip()[:180])
w("EL REGISTRO DE LOS DIECISIETE, CONTADO DE SU FICHERO Y NO TECLEADO:")
if os.path.exists(REGISTRO_SC):
    filas_sc = [json.loads(l) for l in io.open(REGISTRO_SC, encoding="utf-8") if l.strip()]
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> %d filas, disco %d bytes"
      % (len(filas_sc), os.path.getsize(REGISTRO_SC)))
    por_lectura = {}
    for f in filas_sc:
        k = f.get("veredicto_de_la_lectura")
        por_lectura[k] = por_lectura.get(k, 0) + 1
    for k in sorted(por_lectura, key=lambda x: (x is None, x)):
        w("   CIFRA con veredicto_de_la_lectura %-28s: %d" % (repr(k), por_lectura[k]))
    w("   LOS QUE ABREN FICHERO VIVO, NOMBRADOS UNO A UNO:")
    for f in filas_sc:
        if f.get("veredicto_de_la_lectura") == "ABRE FICHERO VIVO":
            w("      %-46s abre %s"
              % (f["arnes"], ", ".join(f.get("ficheros_vivos_atribuidos") or [])))
    w("   LOS QUE SOLO LO NOMBRAN O YA LO TIENEN CLAVADO:")
    for f in filas_sc:
        if f.get("veredicto_de_la_lectura") != "ABRE FICHERO VIVO":
            w("      %-46s %-26s guarda dice %s"
              % (f["arnes"], f.get("veredicto_de_la_lectura"),
                 f.get("veredicto_de_la_guarda")))
    ya = 0
    for f in filas_sc:
        pa = os.path.join(RAIZ, "scripts", "loop", f["arnes"])
        if os.path.exists(pa) and "SUJETO CONGELADO" in io.open(
                pa, encoding="utf-8", errors="replace").read():
            ya += 1
    w("   CIFRA filas cuyo arnes YA declara el literal de la guarda en su texto: %d" % ya)
else:
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> NO EXISTE")
w("EL CABLEADO AL ROJO GLOBAL, BUSCADO Y NO SUPUESTO:")
CER_VMV = os.path.join(RAIZ, "scripts", "loop", "verificar_mutaciones_viejas.py")
t_vmv = io.open(CER_VMV, encoding="utf-8").read().replace(chr(13) + NL, NL)
for aguja in ("guarda_del_sujeto_congelado", "informe_del_sujeto_congelado",
              "sujeto_congelado", "def main"):
    w("   CIFRA apariciones de %-34s: %d" % (repr(aguja), t_vmv.count(aguja)))
w("")

w("=== H.8 TAREA 3: EL CORTE, Y DONDE FALTA. LA TABLA DE TRAMOS MEDIDA HOY ===")
w("(el encargo dice que la 2.a de la 179 publico 6/29/8 y 34/44/10 y que hoy da")
w(" 14/39/18 y 26/34/0. NINGUNA SE COPIA: se corre y se pega lo que salga)")
c, o = correr([PY, "scripts/loop/backlog_l03_resuelto.py"])
w("comando: python scripts/loop/backlog_l03_resuelto.py -> exit %d" % c)
dentro_f = False
for l in o.split(NL):
    if l.strip().startswith("F) LO QUE SOBRA"):
        dentro_f = True
    if dentro_f and l.strip():
        w("   " + l.rstrip()[:180])
    if dentro_f and l.strip().startswith("| **todos**"):
        dentro_f = False
for l in o.split(NL):
    if l.strip() and ("VERDE" in l or "ROJO" in l):
        w("   " + l.rstrip()[:180])
w("EL SELLO DE CORTE, BUSCADO EN LOS DOS SUJETOS DE LA TAREA 3:")
for r in ("scripts/loop/backlog_l03_resuelto.py",
          "scripts/loop/vuelta179_tarea2_cobertura_final.py"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        t = io.open(p, encoding="utf-8").read().replace(chr(13) + NL, NL)
        w("   %-52s sello_de_corte: %d | corte_de_git: %d | 'corte': %d"
          % (r, t.count("sello_de_corte"), t.count("corte_de_git"), t.count("corte")))
    else:
        w("   %-52s NO EXISTE" % r)
w("")

w("=== H.9 TAREA 4: LAS DOS PENDIENTES BARATAS, MEDIDAS ANTES DE TOCARLAS ===")
P0 = os.path.join(RAIZ, "scripts", "loop", "paso0_archivar_anterior.py")
t_p0 = io.open(P0, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("scripts/loop/paso0_archivar_anterior.py -> %d lineas, disco %d bytes | LF %d bytes"
  % (t_p0.count(NL), os.path.getsize(P0), len(t_p0.encode("utf-8"))))
w("   LAS LINEAS QUE DICEN 'ANTERIOR', UNA A UNA:")
for i, l in enumerate(t_p0.split(NL), 1):
    if "anterior" in l.lower():
        w("      LINEA %d: %s" % (i, l.strip()[:170]))
w("   CIFRA apariciones de 'vuelta anterior' en el fichero: %d"
  % t_p0.lower().count("vuelta anterior"))
w("   CIFRA apariciones de 'que va a pisar' en el fichero: %d"
  % t_p0.lower().count("que va a pisar"))
ESQ174 = os.path.join(RAIZ, "scripts", "loop", "vuelta174_esqueleto_reporte.py")
w("scripts/loop/vuelta174_esqueleto_reporte.py existe: %s"
  % ("SI" if os.path.exists(ESQ174) else "NO"))
if os.path.exists(ESQ174):
    t_e = io.open(ESQ174, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("   -> %d lineas, disco %d bytes | LF %d bytes"
      % (t_e.count(NL), os.path.getsize(ESQ174), len(t_e.encode("utf-8"))))
    w("   CIFRA apariciones de 'def vuelta_del_reporte_del_arbol': %d"
      % t_e.count("def vuelta_del_reporte_del_arbol"))
ESQ179 = os.path.join(RAIZ, "scripts", "loop", "vuelta179_esqueleto_reporte.py")
if os.path.exists(ESQ179):
    t_e9 = io.open(ESQ179, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("scripts/loop/vuelta179_esqueleto_reporte.py -> CIFRA 'CLON DECLARADO': %d"
      % t_e9.count("CLON DECLARADO"))
    w("   CIFRA apariciones de 'vuelta174_esqueleto_reporte': %d"
      % t_e9.count("vuelta174_esqueleto_reporte"))
w("")

w("=== H.10 TAREA 5: OP-L-02, SUS INSTRUMENTOS Y SU FICHA, MEDIDOS Y NO LEIDOS ===")
w("(no se lee NINGUN par en esta apertura ni en esa tarea: solo se mide)")
for r in ("scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py",
          "scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py",
          "scripts/loop/vuelta150_3_relectura_expediente.py"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        t = io.open(p, encoding="utf-8").read().replace(chr(13) + NL, NL)
        w("   %-56s %d lineas | disco %d bytes | LF %d bytes"
          % (r, t.count(NL), os.path.getsize(p), len(t.encode("utf-8"))))
    else:
        w("   %-56s NO EXISTE" % r)
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
if os.path.exists(OPS):
    fops = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    w("   docs/plan/OPERACIONES.jsonl -> %d filas" % len(fops))
    for f in fops:
        if f.get("id_op") in ("OP-L-01", "OP-L-02", "OP-L-03", "OP-I-01"):
            w("      %-10s estado %s" % (f.get("id_op"), repr(f.get("estado"))))
    w("      (EL ESTADO NO ES LA VARA. La vara es la salida de")
    w("       scripts/loop/vuelta150_3_relectura_expediente.py --corte <HEAD>)")
LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
if os.path.exists(LD):
    t_ld = io.open(LD, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("   docs/plan/LECTURAS_DIRIGIDAS.md -> %d lineas | disco %d bytes | LF %d bytes"
      % (t_ld.count(NL), os.path.getsize(LD), len(t_ld.encode("utf-8"))))
    w("   CIFRA apariciones de 'SALES ROADMAP' (sin distinguir mayusculas): %d"
      % t_ld.upper().count("SALES ROADMAP"))
    w("   CIFRA apariciones de 'sales_roadmap': %d" % t_ld.count("sales_roadmap"))
w("")

w("FIN DEL SELLO DE APERTURA")

texto = NL.join(lineas) + NL
io.open(os.path.join(LOOP, "SALIDA_V%d_APERTURA.txt" % VUELTA), "w",
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
