# -*- coding: utf-8 -*-
r"""vuelta183_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 183, ENTERO.

CLON DECLARADO de scripts/loop/vuelta182_apertura.py. Cambia el numero de vuelta,
el prefijo de las salidas, la lista RUTAS_DEL_ENCARGO y los bloques H, que aqui
miden lo que ESTE encargo promete y nada mas.

Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA. Desde la vuelta 178 ningun reporte
escribe "CLON DECLARADO" sin pegar la salida de
scripts/loop/cotejar_clon_declarado.py. Este docstring NO afirma que el diff salga
vacio, y NO va a salir vacio: los bloques H cambian de sentencias porque miden
otras cosas. El cotejo se pega en el reporte con lo que salga.

ESTA VUELTA SI ES DE BATERIA, Y ESO MANDA SOBRE TODO LO DEMAS. AUDITOR.md 6.1: la
bateria corre CADA CINCO, en VUELTA PROPIA, y esa vuelta no lleva trabajo de plan
al lado. La 181 era la suya y se corto antes de lanzarla. La decision del fundador
del 5 sep 2026 (PREGUNTA 4 de docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md)
la manda POR TRAMOS RESUMIBLES, y su lanzador, scripts/loop/vuelta183_bateria_por_tramos.py,
esta escrito desde la 182 y sin correr.

EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y ESTA MEDIDO. El regimen AUDITOR.md 6.2
devuelve el tope a cinco cuando DOS vueltas seguidas cierren su propio reporte con
scripts/loop/cerrar_reporte.py. El acta 182, punto 8, midio que la 181 NO cerro el
suyo y la 182 SI: la cuenta va por UNA. Aqui NO se copia esa cifra: el bloque H.4
la vuelve a medir sobre los ficheros.

EL BLOQUE H NO TECLEA NINGUN HASH NI NINGUNA CIFRA. Todo se localiza y se imprime
lo que salga (EJECUTOR.md 2, EL INSTRUMENTO MANDA). El encargo da cifras (109
entradas de nomina, tramo de 13, nueve tramos, la cabecera del acta 182 en la
linea 63250, la linea 696 de cerrar_reporte.py, el sha ea6e850d331d14f0); aqui NO
SE COPIA NINGUNA: se corre y se imprime lo que salga, y la comparacion con lo que
el encargo dice se hace despues, en el reporte, con las dos al lado.

LA CIFRA DE BYTES SE PUBLICA POR LAS DOS CONVENCIONES mientras la convencion no
este fijada (acta 177 punto 7.11): disco (os.path.getsize) y git (git cat-file -s),
las dos a la vez. Y la P.2 del fundador manda BYTES EXACTOS Y NUNCA REDONDEADOS.

POR QUE SE CORRE AQUI: EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION". Este fichero NO toca REPORTE.md, NO toca la nomina, NO corre la
bateria y NO escribe en docs/plan/: sus salidas son SALIDA_V183_*.txt.

LO QUE ESTA VUELTA SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano al abrir la vuelta, dio UNA linea,
" M dataset/metadata/master_graph.json", y git diff --numstat -- dataset/ dio CERO
filas, que es la firma de fin de linea que el acta 181 punto 3.3 ya midio y
declaro que NO es perdida de catalogo. La prediccion se escribe AQUI, antes de
correr, y los bloques C/D/E/F de abajo la miden sin saber lo que hay escrito.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

USO:
  python scripts/loop/vuelta183_apertura.py
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
VUELTA = 183

# LOS SUJETOS DE CODIGO DE LAS DOS TAREAS, nombrados aqui para que el bloque H
# no los pueda elegir despues de ver el resultado.
SUJETOS = [
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/serie_de_registros.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/vuelta183_bateria_por_tramos.py",
    "scripts/loop/aislador_de_ciega.py",
    "scripts/loop/vuelta182_tarea1c_relectura_al_doble.py",
    "scripts/loop/cotejar_clon_declarado.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/reportes/REPORTE_V182.md",
    "docs/plan/08_VERIFICACION.md",
    "docs/PENDIENTES.md",
    "docs/plan/CORRECCIONES_A_APLICAR.md",
    "docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md",
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


def nodos_por_id(grafo):
    """LOS NODOS DEL GRAFO INDEXADOS POR ID, SIN ADIVINAR LA CLAVE DE LA RAIZ.

    Prueba las formas que el fichero puede tener y devuelve la primera que da
    nodos: la clave `nodos` como diccionario id -> nodo (que es la que este
    repo usa hoy), la misma clave como lista, y `nodes` en las dos formas por
    si el fichero cambia de idioma. Si ninguna da nada, devuelve {} y quien
    llame publica el cero, que es una medicion y no un adivinanza."""
    if not isinstance(grafo, dict):
        return {}
    for clave in ("nodos", "nodes"):
        v = grafo.get(clave)
        if isinstance(v, dict) and v:
            return {k: n for k, n in v.items() if isinstance(n, dict)}
        if isinstance(v, list) and v:
            return {n.get("id"): n for n in v
                    if isinstance(n, dict) and n.get("id")}
    return {}


def clave_de_pasos(nodo):
    """EL NOMBRE DE LA CLAVE QUE pasos_del_nodo() acabo usando, para que la
    salida diga de donde saco los pasos y no haya que creerselo."""
    if not isinstance(nodo, dict):
        return "(no es dict)"
    for clave in sorted(nodo.keys()):
        nombre = clave.lower()
        if ("paso" in nombre or "step" in nombre) and isinstance(nodo[clave], list):
            return clave
    return "(ninguna)"


def pasos_del_nodo(nodo):
    """LOS PASOS DE UN NODO, BUSCADOS ENTRE SUS PROPIAS CLAVES Y NO TECLEADOS.

    CORRECCION 3 DECLARADA (vuelta 182). La version anterior probaba las claves
    `pasos` y `steps`, y este repo las llama `pasos_accionables`: la segunda
    corrida del bloque de apertura publico "cero_defectos -> 0 pasos", que es
    falso, y queda entera en docs/loop/SALIDA_V182_APERTURA_SEGUNDA_CORRIDA.txt
    sin borrar. La reparacion NO es teclear la clave buena: es recorrer las
    claves DEL PROPIO NODO y quedarse con la primera cuyo nombre contenga `paso`
    o `step` y cuyo valor sea una lista. Si no hay ninguna, devuelve [] y quien
    llame publica el cero como medicion."""
    if not isinstance(nodo, dict):
        return []
    for clave in sorted(nodo.keys()):
        nombre = clave.lower()
        if ("paso" in nombre or "step" in nombre) and isinstance(nodo[clave], list):
            return nodo[clave]
    return []


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
w("regimen: VUELTA DE BATERIA. AUDITOR.md 6.1: la bateria corre CADA")
w("         CINCO, en vuelta propia, y esa vuelta no lleva trabajo de plan")
w("         al lado. La 181 era la suya y se corto antes de lanzarla. Su")
w("         lanzador por tramos esta escrito desde la 182 y sin correr.")
w("         DOS sub-tareas, que es el tope del regimen temporal 6.2 hasta")
w("         que DOS vueltas seguidas cierren su propio reporte.")
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
                        ("acta 180", "ACTA DEL AUDITOR, VUELTA 180"),
                        ("acta 181", "ACTA DEL AUDITOR, VUELTA 181"),
                        ("acta 182", "ACTA DEL AUDITOR, VUELTA 182")):
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

w("=== H.1 EL REPORTE DEL ARBOL, QUE ES EL QUE EL ESQUELETO DE LA 183 PISARA ===")
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

w("=== H.3 LAS PIEZAS QUE cerrar_reporte.py PEDIRA PARA CERRAR LA 183 ===")
w("(al abrir NO EXISTE NINGUNA, y eso es lo correcto: las produce esta vuelta.")
w(" LA DE BATERIA SI SE VA A PRODUCIR: esta vuelta ES la de bateria y su")
w(" seccion 9 lleva la salida entera dentro, compuesta de los nueve tramos)")
for r in ["docs/loop/SALIDA_V183_TALLADOR_CABECERA.txt",
          "scripts/loop/_v183_cierre_texto.md",
          "docs/loop/SALIDA_V183_BATERIA.txt"]:
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
w("REPORTE_V182.md archivado: %s" % ("SI" if "REPORTE_V182.md" in arch else "NO"))
w("")

w("=== H.5 TAREA 1.a y 1.b: LA SERIE DE REGISTROS, EL ACTA 182 Y EL SALTO ===")
w("(no se teclea ningun numero de registro: se llama a serie_de_registros.py y")
w(" se imprime lo que devuelva. La cabecera del acta se busca en su fichero)")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
t_acta = io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_acta = t_acta.split(NL)
w("docs/loop/ACTA_AUDITOR.md -> %d lineas | disco %d bytes | LF %d bytes"
  % (len(l_acta), os.path.getsize(ACTA), len(t_acta.encode("utf-8"))))
for i, l in enumerate(l_acta, 1):
    if l.startswith("# ACTA DEL AUDITOR, VUELTA 18"):
        w("   CABECERA en la LINEA %d: %s" % (i, l.strip()[:120]))
CAB182 = [i for i, l in enumerate(l_acta, 1)
          if l.startswith("# ACTA DEL AUDITOR, VUELTA 182")]
w("CIFRA cabeceras del acta 182 encontradas: %d" % len(CAB182))
if CAB182:
    base = CAB182[0]
    w("   lineas del acta 182, de su cabecera al final del fichero: %d"
      % (len(l_acta) - base + 1))
    for aguja in ("## 1. ", "## 2. ", "## 3. ", "## 4. ", "## 5. ", "## 6. ",
                  "## 7. ", "## 8. ", "## 9. ", "## 10. ", "## 11. ",
                  "**5.D.", "**7.1 ", "**7.2 ", "**7.3 ", "**7.4 ", "**7.5 "):
        hits = [i for i, l in enumerate(l_acta, 1)
                if l.startswith(aguja) and i >= base]
        w("   %-10s -> lineas %s"
          % (repr(aguja), ", ".join(str(x) for x in hits) or "(ninguna)"))
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
    for numero, rel, linea, titulo in halladas[-6:]:
        w("   ULTIMOS: R.%s en %s:%d -> %s" % (numero, rel, linea, titulo[:100]))
except Exception as e:
    w("NO SE PUDO RECOMPUTAR LA SERIE: %r" % (e,))
w("EL SALTO DE LA 1.b, CONTADO Y NO TECLEADO: que actas tienen cabecera en el")
w("fichero del acta, para saber cuantas quedan sin entrada propia en la serie.")
cabeceras = []
for i, l in enumerate(l_acta, 1):
    if l.startswith("# ACTA DEL AUDITOR, VUELTA ") or l.startswith("# ACTA DE LA VUELTA "):
        m = re.search(r"VUELTA (\d+)", l)
        if m:
            cabeceras.append((int(m.group(1)), i))
w("   CIFRA cabeceras de acta en ACTA_AUDITOR.md: %d" % len(cabeceras))
w("   LAS ULTIMAS DOCE, POR NUMERO DE VUELTA Y LINEA:")
for n_v, li in sorted(cabeceras)[-12:]:
    w("      acta %3d -> linea %d" % (n_v, li))
w("")

w("=== H.6 TAREA 1.c: LA ESCALADA, Y LA CAIDA QUE LA TRAE, MEDIDA ===")
w("(el veredicto de una linea del reporte de la 182 contra su propia seccion 8.")
w(" NI EL VEREDICTO NI LAS CABECERAS SE TECLEAN: se leen del reporte archivado)")
R182 = os.path.join(LOOP, "reportes", "REPORTE_V182.md")
l182 = []
if not os.path.exists(R182):
    w("   docs/loop/reportes/REPORTE_V182.md -> NO EXISTE. Sin el no hay caida que")
    w("   medir, y eso se declara en vez de suponerla.")
else:
    t182 = io.open(R182, encoding="utf-8").read().replace(chr(13) + NL, NL)
    l182 = t182.split(NL)
    g182 = bytes_de_git("docs/loop/reportes/REPORTE_V182.md")
    w("   docs/loop/reportes/REPORTE_V182.md -> %d lineas | disco %d bytes | git %s"
      % (len(l182), os.path.getsize(R182),
         ("%d bytes" % g182) if g182 is not None else "NO ESTA EN HEAD"))
    for i, l in enumerate(l182, 1):
        if "EL VEREDICTO DE UNA LINEA" in l:
            w("   VEREDICTO en la LINEA %d:" % i)
            for k in range(i - 1, min(i + 6, len(l182))):
                w("      | " + l182[k].strip()[:150])
    w("   LAS CABECERAS C.n DE LA SECCION 8, CONTADAS Y NO RECORDADAS:")
    cs = [(i, l) for i, l in enumerate(l182, 1)
          if re.match(r"^\*{0,2}C\.\d+", l.strip())]
    for i, l in cs:
        w("      LINEA %d: %s" % (i, l.strip()[:130]))
    w("   CIFRA cabeceras C.n localizadas: %d" % len(cs))
    w("   CIFRA numerales distintos de C.n: %d"
      % len({re.search(r"C\.(\d+)", l).group(1) for _i, l in cs}))
    w("   LAS FILAS DE LA TABLA DE TAREAS, CONTADAS DE SU TABLA:")
    filas_t = [(i, l) for i, l in enumerate(l182, 1)
               if re.match(r"^\|\s*\*{0,2}\d+\*{0,2}\s*\|", l)]
    for i, l in filas_t:
        w("      LINEA %d: %s" % (i, l.strip()[:130]))
    w("   CIFRA filas de tabla que empiezan por un numero: %d" % len(filas_t))
    w("   LOS NUMERALES ESCRITOS CON LETRA QUE APARECEN EN EL VEREDICTO:")
    for l in [x for x in l182 if "EL VEREDICTO DE UNA LINEA" in x]:
        for pal in ("una", "dos", "tres", "cuatro", "cinco", "seis", "siete",
                    "ocho", "nueve", "diez"):
            if re.search(r"\b%s\b" % pal, l.lower()):
                w("      %s -> SI aparece" % pal)
w("EL SUJETO DE LA OPERACION, MEDIDO ANTES DE TOCARLO:")
CER = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
t_cer = io.open(CER, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_cer = t_cer.split(NL)
g_cer = bytes_de_git("scripts/loop/cerrar_reporte.py")
w("   scripts/loop/cerrar_reporte.py -> %d lineas | disco %d bytes | git %s"
  % (len(l_cer), os.path.getsize(CER),
     ("%d bytes" % g_cer) if g_cer is not None else "NO ESTA EN HEAD"))
for aguja in ("def piezas_que_faltan", "def hueco_declarado_que_falta",
              "def citas_de_arnes_que_no_calzan", "def rama_de_la_seccion9",
              "def cifras_sin_pareja", "os.path.getsize(ruta_bat)",
              "max(tam, 0)", "def main"):
    hits = [(i, l) for i, l in enumerate(l_cer, 1) if aguja in l]
    w("   %-42s -> %d aparicion(es)" % (repr(aguja), len(hits)))
    for i, l in hits:
        w("      LINEA %d: %s" % (i, l.strip()[:150]))
w("")

w("=== H.7 TAREA 1.d: EL HUECO DE LA SECCION 9, EN SU CODIGO DE HOY ===")
w("(no se copia la linea que el encargo nombra: se busca en el fichero y se")
w(" imprime con su numero, tal como esta hoy)")
for i, l in enumerate(l_cer, 1):
    if "ruta_bat" in l or "NO EXISTE" in l:
        w("   LINEA %d: %s" % (i, l.rstrip()[:160]))
w("LAS TRES PIEZAS QUE EL HUECO YA EXIGE, LOCALIZADAS EN EL CODIGO:")
for aguja in ("MARCA_HUECO", "MARCA_ATRIBUCION", "PATRON_BYTES"):
    hits = [(i, l) for i, l in enumerate(l_cer, 1) if aguja in l]
    w("   %-20s -> %d aparicion(es), lineas %s"
      % (aguja, len(hits), ", ".join(str(i) for i, _l in hits[:12])))
w("")

w("=== H.8 TAREA 1.e: EL TRAMO DE LA CIEGA DE LA 182, LEIDO DEL ACTA ===")
w("(los 30 puestos NO se teclean: se sacan de la seccion 9 del acta 182 y se")
w(" parsean. Si el acta no los trae, se dice y no se inventa ninguno)")
puestos_ciega = []
if CAB182:
    base = CAB182[0]
    ini9 = None
    fin9 = len(l_acta)
    for i in range(base, len(l_acta)):
        if l_acta[i].startswith("## 9. "):
            ini9 = i
            break
    if ini9 is None:
        w("   EL ACTA 182 NO TIENE SECCION 9. No se inventa ninguna.")
    else:
        for i in range(ini9 + 1, len(l_acta)):
            if l_acta[i].startswith("## "):
                fin9 = i
                break
        w("   SECCION 9 del acta 182: lineas %d a %d (%d lineas)"
          % (ini9 + 1, fin9, fin9 - ini9))
        for i in range(ini9, min(ini9 + 12, fin9)):
            w("      | " + l_acta[i].strip()[:150])
        for i in range(ini9, fin9):
            if "PUESTOS SON" in l_acta[i].upper():
                bloque = NL.join(l_acta[i:i + 4])
                w("   LA LINEA QUE LOS LISTA es la %d, y sus tres siguientes:" % (i + 1))
                for l in bloque.split(NL):
                    w("      | " + l.strip()[:150])
                crudo = bloque.split(":", 1)[1] if ":" in bloque else ""
                puestos_ciega = [int(x) for x in re.findall(r"\d+", crudo.replace(".", ""))]
                break
w("   CIFRA puestos parseados de esa linea: %d" % len(puestos_ciega))
w("   LOS PUESTOS, ORDENADOS: %s" % ", ".join(str(x) for x in sorted(puestos_ciega)))
w("   MIN %s | MAX %s | REPETIDOS %d"
  % (min(puestos_ciega) if puestos_ciega else "n/a",
     max(puestos_ciega) if puestos_ciega else "n/a",
     len(puestos_ciega) - len(set(puestos_ciega))))
w("LA MAQUINA DE LA 182 QUE SE IMPORTA Y NO SE COPIA:")
RREL = "scripts/loop/vuelta182_tarea1c_relectura_al_doble.py"
PREL = os.path.join(RAIZ, RREL.replace("/", os.sep))
w("   %s existe: %s | disco %s bytes"
  % (RREL, "SI" if os.path.exists(PREL) else "NO",
     os.path.getsize(PREL) if os.path.exists(PREL) else "n/a"))
if os.path.exists(PREL):
    t_rel = io.open(PREL, encoding="utf-8", errors="replace").read().replace(chr(13) + NL, NL)
    for i, l in enumerate(t_rel.split(NL), 1):
        if l.startswith("def ") or l.startswith("VARA") or l.startswith("PUESTOS"):
            w("      LINEA %d: %s" % (i, l.strip()[:130]))
w("")

w("=== H.9 TAREA 2: LA BATERIA, SU LANZADOR Y SUS TRAMOS, CONTADOS ===")
RBT = "scripts/loop/vuelta183_bateria_por_tramos.py"
BT = os.path.join(RAIZ, RBT.replace("/", os.sep))
g_bt = bytes_de_git(RBT)
w("   %s existe: %s | disco %s bytes | git %s"
  % (RBT, "SI" if os.path.exists(BT) else "NO",
     os.path.getsize(BT) if os.path.exists(BT) else "n/a",
     ("%d bytes" % g_bt) if g_bt is not None else "NO ESTA EN HEAD"))
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
w("LAS BATERIAS VIVAS EN docs/loop/, CONTADAS DE SU DIRECTORIO:")
PAT_BAT = re.compile(r"^SALIDA_V(\d+)_BATERIA.*\.txt$")
vivas = sorted(n for n in os.listdir(LOOP) if PAT_BAT.match(n))
n_cero = 0
for n in vivas:
    pth = os.path.join(LOOP, n)
    tam = os.path.getsize(pth)
    if tam == 0:
        n_cero += 1
    w("   %-50s disco %8d bytes" % (n, tam))
w("CIFRA ficheros SALIDA_V<N>_BATERIA*.txt en docs/loop/: %d" % len(vivas))
w("CIFRA de ellos que miden CERO BYTES: %d" % n_cero)
try:
    import verificar_mutaciones_viejas as VMV   # noqa: E402
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _a in VMV.VIEJAS]
    w("   CIFRA censo: %d | CIFRA nomina: %d | VARA_DEL_CENSO: %d"
      % (len(censo), len(nomina), VMV.VARA_DEL_CENSO))
    w("   FAMILIAS_DE_ARNES: %s" % ", ".join(VMV.FAMILIAS_DE_ARNES))
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
w("EL REGISTRO DEL SUJETO CONGELADO, CONTADO DE SU FICHERO:")
if os.path.exists(REGISTRO_SC):
    filas_sc = [json.loads(l) for l in io.open(REGISTRO_SC, encoding="utf-8") if l.strip()]
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> %d filas, disco %d bytes"
      % (len(filas_sc), os.path.getsize(REGISTRO_SC)))
else:
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> NO EXISTE")
w("")

w("=== H.10 EL ARCHIVO DE VEREDICTOS, QUE ESTA VUELTA NO PUEDE MOVER ===")
w("(el encargo dice que su sha256 tiene que seguir siendo el mismo al cerrar.")
w(" AQUI NO SE COPIA EL DEL ENCARGO: se computa y se imprime lo que salga)")
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
puestos = [f.get("puesto_intra") for f in filas]
w("   MIN puesto %s | MAX puesto %s | HUECOS %d | DUPLICADOS %d"
  % (min(puestos), max(puestos),
     len(set(range(min(puestos), max(puestos) + 1)) - set(puestos)),
     len(puestos) - len(set(puestos))))
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
