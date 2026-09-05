# -*- coding: utf-8 -*-
r"""vuelta181_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 181, ENTERO.

CLON DECLARADO de scripts/loop/vuelta180_apertura.py. Cambia el numero de
vuelta, el prefijo de las salidas, la lista RUTAS_DEL_ENCARGO y el bloque H, que
aqui mide lo que ESTE encargo promete y nada mas.

Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA. Desde la vuelta 178 ningun
reporte escribe "CLON DECLARADO" sin pegar la salida de
scripts/loop/cotejar_clon_declarado.py (ultima linea del docstring de ese
fichero antes del USO). Este docstring NO afirma que el diff salga vacio: la
vuelta 176 cayo por eso, y el cotejo de este clon se pega en el reporte.

ESTA VUELTA SI ES DE BATERIA, Y ES LA UNICA COSA QUE LLEVA AL LADO DE LOS
REGISTROS. AUDITOR.md 6.1: la bateria corre CADA CINCO, en VUELTA PROPIA. La
cadencia esta adjudicada en el acta 176 punto 7.8 y reconfirmada en las actas
178, 179 y 180 (esta ultima en su punto 10, "LA BATERIA: LA PROXIMA ES LA 181").
Por eso el bloque H de esta apertura mide LA NOMINA COMO SUJETO DE BATERIA y no
los sujetos de cinco tareas: aqui hay DOS.

EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS Y NO ES UN DESCUIDO: es la adjudicacion
6.8 del acta 180, que resuelve la tension entre AUDITOR.md 6.1 (la vuelta de
bateria no lleva nada mas) y AUDITOR.md 6.2 (el tope vuelve a cinco) por la letra
de la parada del 5 sep 2026, donde la 6.2 se concedio "combinada con la (a)".

EL BLOQUE H NO TECLEA NINGUN HASH NI NINGUNA CIFRA. Todo se localiza y se imprime
lo que salga. Las cifras vivas de la nomina, del censo y de la guarda del sujeto
congelado NO se copian del encargo ni del acta: se recomputan corriendo los
propios instrumentos, que es la unica fuente que la casa reconoce (EJECUTOR.md 2,
EL INSTRUMENTO MANDA). El encargo da cifras (108 entradas de nomina, censo 168,
fuera 60); aqui NO SE COPIA NINGUNA: se corre y se imprime lo que salga, y la
comparacion con lo que el encargo dice se hace despues, en el reporte, con las
dos al lado.

LA CIFRA DE BYTES SE PUBLICA POR LAS DOS CONVENCIONES mientras la convencion no
este fijada (acta 177 punto 7.11, y sigue sin fijar; el acta 180 la sube por
octava vez en su 6.7): disco (os.path.getsize) y git (git cat-file -s), las dos a
la vez.

POR QUE SE CORRE AQUI: EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION". Este fichero NO toca REPORTE.md, NO toca la nomina, NO corre
la bateria y NO escribe en docs/plan/: sus salidas son SALIDA_V181_*.txt.

Y LA MEDICION DE DESFASE DEL CALIBRADO SE TOMA AQUI, EN SU SITIO: desde la 178
una columna de apertura medida al cierre es CAIDA QUE ACUMULA. Aqui corre dentro
del bloque B, antes de toda operacion.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

LO QUE ESTA VUELTA SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano al abrir la vuelta, dio CERO
lineas, y git rev-list --left-right --count HEAD...@{u} dio 0 y 0. La prediccion
se escribe AQUI, antes de correr, y los bloques C/D/E/F de abajo la miden sin
saber lo que hay escrito.

USO:
  python scripts/loop/vuelta181_apertura.py
"""
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
VUELTA = 181

# LOS SUJETOS DE CODIGO DE LAS DOS TAREAS, nombrados aqui para que el bloque H
# no los pueda elegir despues de ver el resultado.
SUJETOS = [
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/vuelta175_correr_bateria.py",
    "scripts/loop/vuelta176_bateria_por_tramos.py",
    "scripts/loop/vuelta172_tarea1c_guarda_que_mordio.py",
    "scripts/loop/vuelta174_tarea1b_mutacion_esqueleto.py",
    "scripts/loop/sujeto_congelado_de_git.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/reportes/REPORTE_V180.md",
    "docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "scripts/loop/guarda_commit_dataset.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/anexar_tarea_al_reporte.py",
    "scripts/loop/tallar_cabecera_reporte.py",
    "scripts/loop/cotejar_clon_declarado.py",
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
w("regimen: VUELTA DE BATERIA, Y NO LLEVA NADA MAS (AUDITOR.md 6.1). DOS")
w("         sub-tareas por la adjudicacion 6.8 del acta 180, la 1 BLOQUEANTE.")
w("         El tope vuelve a cinco en la 182.")
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

w("=== B.1 LA CADENCIA DE LA BATERIA, LOCALIZADA EN GIT Y NO TECLEADA ===")
w("(AUDITOR.md 6.1: la bateria corre CADA CINCO, en vuelta propia. Aqui NO se")
w(" teclea ningun hash: se busca en el log el commit de cada acta que la")
w(" adjudica o la reconfirma, y se imprime lo que salga)")
c, logtodo = git(["log", "--format=%h%x09%s", "-120"])
for etiqueta, aguja in (("acta 176", "ACTA DEL AUDITOR, VUELTA 176"),
                        ("acta 178", "ACTA DEL AUDITOR, VUELTA 178"),
                        ("acta 179", "ACTA DEL AUDITOR, VUELTA 179"),
                        ("acta 180", "ACTA DEL AUDITOR, VUELTA 180")):
    hits = [l for l in logtodo.splitlines() if aguja.upper() in l.upper()]
    w("   %-12s -> %s"
      % (etiqueta, (hits[0][:150] if hits else "NO LOCALIZADO EN LOS 120 ULTIMOS")))
c, n_bat = git(["log", "--format=%h", "-120", "--",
                "scripts/loop/verificar_mutaciones_viejas.py"])
w("   commits que tocan verificar_mutaciones_viejas.py en los 120 ultimos: %d"
  % len([l for l in n_bat.splitlines() if l.strip()]))
w("")

w("=== C. git status --porcelain ENTERO ===")
c, st = git(["status", "--porcelain"])
for l in st.splitlines():
    w(l)
w("CIFRA lineas de status: %d" % len([l for l in st.splitlines() if l.strip()]))
w("")

w("=== D. BYTES DE CADA RUTA QUE EL ENCARGO NOMBRA, POR LAS DOS CONVENCIONES ===")
w("(disco = os.path.getsize; git = git cat-file -s HEAD:<ruta>. Acta 177 punto")
w(" 7.11 y acta 180 punto 6.7: mientras la convencion no este fijada, SE")
w(" PUBLICAN LAS DOS)")
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
          "ABIERTA, SIN CERRAR", "HUECO DECLARADO Y MEDIDO",
          "CORRIDA ENTERA Y SOLA AL CIERRE"]
MARCAS = MARCAS + [NL + "## %d." % k for k in range(3, 10)]
for marca in MARCAS:
    w("   contiene %-36s -> %s" % (repr(marca), "SI" if marca in rep else "NO"))
w("")

w("=== H.1 EL REPORTE DEL ARBOL, QUE ES EL QUE EL ESQUELETO DE LA 181 PISARA ===")
RUTA_REP = os.path.join(LOOP, "REPORTE.md")
arbol = io.open(RUTA_REP, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("primera linea: %s" % arbol.split(NL, 1)[0].strip())
w("bytes en disco (normalizado a LF): %d | saltos de linea: %d"
  % (len(arbol.encode("utf-8")), arbol.count(NL)))
w("bytes en disco (crudos, os.path.getsize): %d" % os.path.getsize(RUTA_REP))
w("identico byte a byte al de HEAD: %s"
  % ("SI" if arbol == rep.replace(chr(13) + NL, NL) else "NO"))
for marca in MARCAS:
    w("   contiene %-36s -> %s" % (repr(marca), "SI" if marca in arbol else "NO"))
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

w("=== H.3 LAS PIEZAS QUE cerrar_reporte.py PEDIRA PARA CERRAR LA 181 ===")
w("(al abrir NO EXISTE NINGUNA, y eso es lo correcto: las produce esta vuelta.")
w(" LA DE BATERIA SI SE VA A PRODUCIR, y esa es la diferencia entera con la 180:")
w(" esta vuelta la corre y la seccion 9 lleva su salida dentro)")
for r in ["docs/loop/SALIDA_V181_TALLADOR_CABECERA.txt",
          "scripts/loop/_v181_cierre_texto.md",
          "docs/loop/SALIDA_V181_BATERIA.txt"]:
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
w("REPORTE_V180.md archivado: %s" % ("SI" if "REPORTE_V180.md" in arch else "NO"))
w("")

w("=== H.5 LA NOMINA Y EL CENSO, RECOMPUTADOS Y CON SU CORTE ===")
w("(el encargo dice 108 entradas de nomina, censo 168 y fuera 60, medido por el")
w(" auditor al cierre de la 180. NO SE COPIA NINGUNA: se llaman las funciones")
w(" puras del propio sujeto y se imprime lo que salga.")
w(" EL CORTE VA AL LADO por adjudicacion 7.2 del acta 178, porque el")
w(" denominador crece DENTRO de la propia vuelta)")
w("CORTE DE ESTA MEDICION: HEAD %s, APERTURA de la vuelta %d, antes de la"
  % (head[:12], VUELTA))
w("                        primera operacion de esta vuelta.")
VMV = None
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
    w("LA RESTA COMPROBADA: censo %d menos nomina %d = %d, y fuera de nomina = %d. "
      "CALZAN: %s"
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
    w("LAS CONSTANTES DE LA BATERIA, LEIDAS Y NO TECLEADAS:")
    w("   TOPE_DE_MINUTOS_POR_TRAMO = %s" % VMV.TOPE_DE_MINUTOS_POR_TRAMO)
    w("   FAMILIAS_DE_ARNES = %s" % ", ".join(VMV.FAMILIAS_DE_ARNES))
    w("   VARA_DEL_CENSO = %d" % VMV.VARA_DEL_CENSO)
    w("LA GUARDA DEL SUJETO CONGELADO, LLAMADA COMO FUNCION (no como proceso):")
    malas = VMV.guarda_del_sujeto_congelado()
    w("   CIFRA entradas cuyo SUJETO NO ESTA CONGELADO: %d" % len(malas))
    for nombre, veredicto, vive in malas:
        w("      SUJETO SIN CONGELAR: %-46s %s" % (nombre, veredicto))
    w("LAS SEIS PIEZAS DE hay_rojo_al_cierre(), MIRADAS ANTES DE CORRER NADA:")
    w("   (las tres primeras SOLO se pueden medir CORRIENDO la bateria, asi que")
    w("    aqui salen NO MEDIBLES por construccion y no por resultado. Se dicen")
    w("    igual, porque un hueco declarado no es un hueco escondido)")
    w("   perdidas            -> NO MEDIBLE EN APERTURA (exige correr los arneses)")
    w("   no mordio           -> NO MEDIBLE EN APERTURA (exige correr los arneses)")
    w("   no reproducible     -> NO MEDIBLE EN APERTURA (exige correr los arneses)")
    w("   faltan de la nomina -> %d" % len(faltan))
    w("   invisibles al censo -> %d" % len(invis))
    w("   sujeto sin congelar -> %d" % len(malas))
except Exception as e:
    w("NO SE PUDO RECOMPUTAR: %r" % (e,))
w("")

w("=== H.6 TAREA 1: LA E.1 DEL ACTA 180, MEDIDA EN EL CODIGO Y NO LEIDA ===")
w("(el acta 180 seccion 5 dice que cerrar_reporte.py tiene DOS ramas para la")
w(" seccion 9 y que la 180 entro por la equivocada. NO SE COPIA: se busca en el")
w(" fichero y se imprime la linea con su numero)")
CER = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
t_cer = io.open(CER, encoding="utf-8").read().replace(chr(13) + NL, NL)
for aguja in ("CAB_9 =", "CAB_9_HUECO =", "PATRON_FICHERO_BATERIA =",
              "def vuelta_de_fichero", "def hueco_declarado_que_falta",
              "if lineas_bat:", "hueco_declarado_que_falta(seccion9",
              "vuelta que lleva dentro el nombre del fichero"):
    hits = [(i, l) for i, l in enumerate(t_cer.split(NL), 1) if aguja in l]
    w("   %-46s -> %d aparicion(es)" % (repr(aguja), len(hits)))
    for i, l in hits:
        w("      LINEA %d: %s" % (i, l.strip()[:150]))
w("EL PATRON, APLICADO A LOS CINCO NOMBRES, CON vuelta_de_fichero() DE VERDAD:")
try:
    import cerrar_reporte as CR   # noqa: E402
    for nombre in ("docs/loop/SALIDA_V177_BATERIA.txt",
                   "docs/loop/SALIDA_V178_BATERIA.txt",
                   "docs/loop/SALIDA_V179_BATERIA.txt",
                   "docs/loop/SALIDA_V180_HUECO_BATERIA.txt",
                   "docs/loop/SALIDA_V181_BATERIA.txt"):
        p = os.path.join(RAIZ, nombre.replace("/", os.sep))
        w("   %-44s vuelta_de_fichero -> %-5s | existe: %-2s | bytes en disco: %s"
          % (nombre, CR.vuelta_de_fichero(nombre),
             "SI" if os.path.exists(p) else "NO",
             (os.path.getsize(p) if os.path.exists(p) else "n/a")))
except Exception as e:
    w("   NO SE PUDO IMPORTAR cerrar_reporte: %r" % (e,))
w("QUIEN ESCRIBE EL NOMBRE SALIDA_V180_HUECO_BATERIA, BUSCADO EN scripts/:")
n_escritores = 0
for base, _dirs, ficheros in os.walk(os.path.join(RAIZ, "scripts")):
    if "__pycache__" in base:
        continue
    for f in sorted(ficheros):
        if not f.endswith(".py"):
            continue
        try:
            tt = io.open(os.path.join(base, f), encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        if "SALIDA_V180_HUECO_BATERIA" in tt:
            n_escritores += 1
            w("      LO NOMBRA: %s"
              % os.path.relpath(os.path.join(base, f), RAIZ).replace(os.sep, "/"))
w("   CIFRA ficheros de scripts/ que nombran SALIDA_V180_HUECO_BATERIA: %d"
  % n_escritores)
w("EL ACTA 180, LOCALIZADA EN SU FICHERO Y CON SU LINEA:")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
t_acta = io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_acta = t_acta.split(NL)
w("   docs/loop/ACTA_AUDITOR.md -> %d lineas | disco %d bytes | LF %d bytes"
  % (len(l_acta), os.path.getsize(ACTA), len(t_acta.encode("utf-8"))))
for i, l in enumerate(l_acta, 1):
    if l.startswith("# ACTA DEL AUDITOR, VUELTA 180"):
        w("   CABECERA DEL ACTA 180 en la LINEA %d: %s" % (i, l.strip()[:120]))
for aguja in ("## 5. LA CAIDA DEL EJECUTOR", "## 6. LAS ADJUDICACIONES",
              "**6.1 ", "**6.2 ", "**6.3 ", "**6.4 ", "**6.5 ", "**6.6 ",
              "**6.7 ", "**6.8 ", "## 8. LA METRICA DE CREDITO",
              "## 10. LA CADENCIA Y EL TOPE", "## 11. PARADA"):
    hits = [i for i, l in enumerate(l_acta, 1) if l.startswith(aguja) and i > 62440]
    w("   %-34s -> lineas %s"
      % (repr(aguja), ", ".join(str(x) for x in hits) or "(ninguna)"))
w("")

w("=== H.7 TAREA 2: LAS BATERIAS VIEJAS Y SU RELOJ, CONTADAS DE SU DIRECTORIO ===")
w("(el grano del tope de 10 minutos se mide EN ESTA VUELTA con el reloj de ESTA")
w(" corrida. Aqui solo se deja el CONTRASTE de lo que las corridas viejas")
w(" midieron, leido de sus propios ficheros con reloj_de_la_corrida())")
PAT_BAT = re.compile(r"^SALIDA_V(\d+)_BATERIA.*\.txt$")
vivas = sorted(n for n in os.listdir(LOOP) if PAT_BAT.match(n))
n_cero = 0
for n in vivas:
    p = os.path.join(LOOP, n)
    tam = os.path.getsize(p)
    if tam == 0:
        n_cero += 1
    w("   %-50s disco %8d bytes" % (n, tam))
w("CIFRA ficheros SALIDA_V<N>_BATERIA*.txt en docs/loop/: %d" % len(vivas))
w("CIFRA de ellos que miden CERO BYTES: %d" % n_cero)
w("EL RELOJ DE LAS CORRIDAS VIEJAS, LEIDO CON reloj_de_la_corrida():")
if VMV is None:
    w("   NO SE PUDO LEER EL RELOJ: el modulo de la bateria no se importo")
else:
    for n in vivas:
        p = os.path.join(LOOP, n)
        if os.path.getsize(p) == 0:
            w("   %-50s CERO BYTES: no hay reloj que leer" % n)
            continue
        t = io.open(p, encoding="utf-8", errors="replace").read()
        rl = VMV.reloj_de_la_corrida(t)
        cost = VMV.minutos_por_entrada(rl)
        w("   %-50s tramos con reloj: %2d | minutos por entrada (MAXIMO): %s"
          % (n, len(rl), ("%.4f" % cost) if cost is not None else "(sin reloj)"))
    w("   tamano_por_minutos sobre el reloj VACIO (el por defecto declarado): %s"
      % (VMV.tamano_por_minutos([]),))
w("EL REGISTRO DEL SUJETO CONGELADO, CONTADO DE SU FICHERO Y NO TECLEADO:")
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
else:
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> NO EXISTE")
w("LA P.1, QUE NO SE TOCA AQUI (adjudicacion 6.6 del acta 180: VA A LA 182):")
P1 = os.path.join(RAIZ, "scripts", "loop", "vuelta172_tarea1c_guarda_que_mordio.py")
w("   scripts/loop/vuelta172_tarea1c_guarda_que_mordio.py existe: %s"
  % ("SI" if os.path.exists(P1) else "NO"))
if os.path.exists(P1):
    w("   -> disco %d bytes" % os.path.getsize(P1))
    if VMV is not None:
        w("   esta en el censo de arneses_del_directorio(): %s"
          % ("SI" if os.path.basename(P1) in VMV.arneses_del_directorio() else "NO"))
        w("   esta en la nomina VIEJAS: %s"
          % ("SI" if os.path.basename(P1) in [s for s, _a in VMV.VIEJAS] else "NO"))
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
