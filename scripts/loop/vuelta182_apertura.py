# -*- coding: utf-8 -*-
r"""vuelta182_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 182, ENTERO.

CLON DECLARADO de scripts/loop/vuelta181_apertura.py. Cambia el numero de vuelta,
el prefijo de las salidas, la lista RUTAS_DEL_ENCARGO y el bloque H, que aqui mide
lo que ESTE encargo promete y nada mas. El bloque H de la 181 medi'a la nomina como
sujeto de bateria; esta vuelta NO es de bateria, asi que mide otra cosa.

Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA. Desde la vuelta 178 ningun reporte
escribe "CLON DECLARADO" sin pegar la salida de
scripts/loop/cotejar_clon_declarado.py. Este docstring NO afirma que el diff salga
vacio, y de hecho NO va a salir vacio: el bloque H cambia de sentencias porque mide
otras cosas. El cotejo se pega en el reporte con lo que salga.

ESTA VUELTA NO ES DE BATERIA. AUDITOR.md 6.1: la bateria corre CADA CINCO, en
VUELTA PROPIA. La 181 era la suya y se corto antes de lanzarla. El encargo de la
182 manda que la bateria vaya a la 183 POR TRAMOS RESUMIBLES (decision del fundador
del 5 sep 2026, PREGUNTA 4), asi que aqui la seccion 9 del reporte cierra con su
HUECO DECLARADO Y MEDIDO, como el regimen 6.1 manda para las vueltas intermedias.

EL TOPE DE ESTA VUELTA ES CINCO SUB-TAREAS Y ESO TAMBIEN ES LETRA, NO GANAS. La
adjudicacion 6.8 del acta 180 bajo el tope a DOS en la 181 porque era vuelta de
bateria y la 6.1 manda que no lleve nada mas; dicho eso, escribio "El tope vuelve a
cinco en la 182". El encargo de esta vuelta trae CINCO y dice "que es el tope".

EL BLOQUE H NO TECLEA NINGUN HASH NI NINGUNA CIFRA. Todo se localiza y se imprime
lo que salga (EJECUTOR.md 2, EL INSTRUMENTO MANDA). El encargo da cifras (543 D,
329 A, el puesto 2.464, los commits de20c078 y 02384c6a); aqui NO SE COPIA NINGUNA:
se corre y se imprime lo que salga, y la comparacion con lo que el encargo dice se
hace despues, en el reporte, con las dos al lado.

LA CIFRA DE BYTES SE PUBLICA POR LAS DOS CONVENCIONES mientras la convencion no
este fijada (acta 177 punto 7.11, acta 180 punto 6.7 por octava vez): disco
(os.path.getsize) y git (git cat-file -s), las dos a la vez. Y la P.2 del fundador,
del 5 sep 2026, manda BYTES EXACTOS Y NUNCA REDONDEADOS, con los KB solo entre
parentesis: aqui no se imprime ningun KB.

POR QUE SE CORRE AQUI: EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION". Este fichero NO toca REPORTE.md, NO toca la nomina, NO corre la
bateria y NO escribe en docs/plan/: sus salidas son SALIDA_V182_*.txt.

Y LA MEDICION DE DESFASE DEL CALIBRADO SE TOMA AQUI, EN SU SITIO: desde la 178 una
columna de apertura medida al cierre es CAIDA QUE ACUMULA.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

LO QUE ESTA VUELTA SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano al abrir la vuelta, dio UNA linea,
" M dataset/metadata/master_graph.json", y git diff --numstat -- dataset/ dio CERO
filas, que es la firma de fin de linea que el acta 181 punto 3.3 ya midio y
declaro que NO es perdida de catalogo. La prediccion se escribe AQUI, antes de
correr, y los bloques C/D/E/F de abajo la miden sin saber lo que hay escrito.

USO:
  python scripts/loop/vuelta182_apertura.py
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
VUELTA = 182

# LOS SUJETOS DE CODIGO DE LAS DOS TAREAS, nombrados aqui para que el bloque H
# no los pueda elegir despues de ver el resultado.
SUJETOS = [
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/vuelta172_tarea1c_guarda_que_mordio.py",
    "scripts/loop/aislador_de_ciega.py",
    "scripts/loop/serie_de_registros.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/vuelta176_bateria_por_tramos.py",
    "scripts/loop/verificar_apertura_sellada.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/reportes/REPORTE_V181.md",
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
w("regimen: VUELTA ORDINARIA, NO DE BATERIA. La bateria corre CADA CINCO en")
w("         vuelta propia (AUDITOR.md 6.1) y la 181 era la suya y se corto")
w("         antes de lanzarla; esta vuelta la deja PREPARADA para la 183 por")
w("         tramos resumibles, y su seccion 9 cierra con HUECO DECLARADO Y")
w("         MEDIDO. CINCO sub-tareas, que es el tope que el acta 180 en su")
w("         6.8 devolvia a esta vuelta con estas palabras: El tope vuelve a")
w("         cinco en la 182.")
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

w("=== H.5 TAREA 1.a: LA SERIE DE REGISTROS Y EL ACTA 181, LOCALIZADAS ===")
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
CAB181 = [i for i, l in enumerate(l_acta, 1)
          if l.startswith("# ACTA DEL AUDITOR, VUELTA 181")]
w("CIFRA cabeceras del acta 181 encontradas: %d" % len(CAB181))
if CAB181:
    base = CAB181[0]
    w("   lineas del acta 181, de su cabecera al final del fichero: %d"
      % (len(l_acta) - base + 1))
    for aguja in ("## 1. ", "## 2. ", "## 3. ", "## 4. ", "## 5. ", "## 6. ",
                  "## 7. ", "## 8. ", "## 9. ", "## 10. ", "## 11. ",
                  "**7.1 ", "**7.2 ", "**7.3 ", "**7.4 ", "**7.5 "):
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
w("")

w("=== H.6 TAREA 1.b: LOS DOS PENDIENTES DEL ACTA 180, MEDIDOS EN EL CODIGO ===")
w("(el E.1 sobre cerrar_reporte.py y la P.1 del censo. NO SE COPIA NADA DEL ACTA:")
w(" se busca en el fichero y se imprime la linea con su numero)")
CER = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
t_cer = io.open(CER, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_cer = t_cer.split(NL)
w("scripts/loop/cerrar_reporte.py -> %d lineas | disco %d bytes | LF %d bytes"
  % (len(l_cer), os.path.getsize(CER), len(t_cer.encode("utf-8"))))
for aguja in ("CAB_9 =", "CAB_9_HUECO =", "PATRON_FICHERO_BATERIA =",
              "def vuelta_de_fichero", "def hueco_declarado_que_falta",
              "if lineas_bat:", "hueco_declarado_que_falta(seccion9",
              "vuelta que lleva dentro el nombre del fichero"):
    hits = [(i, l) for i, l in enumerate(l_cer, 1) if aguja in l]
    w("   %-46s -> %d aparicion(es)" % (repr(aguja), len(hits)))
    for i, l in hits:
        w("      LINEA %d: %s" % (i, l.strip()[:150]))
w("EL PATRON APLICADO, CON vuelta_de_fichero() DE VERDAD Y NO PARAFRASEADA:")
try:
    import cerrar_reporte as CR   # noqa: E402
    for nombre in ("docs/loop/SALIDA_V177_BATERIA.txt",
                   "docs/loop/SALIDA_V180_HUECO_BATERIA.txt",
                   "docs/loop/SALIDA_V181_BATERIA.txt",
                   "docs/loop/SALIDA_V182_HUECO_BATERIA.txt",
                   "docs/loop/SALIDA_V183_BATERIA.txt"):
        pth = os.path.join(RAIZ, nombre.replace("/", os.sep))
        w("   %-46s vuelta_de_fichero -> %-5s | existe: %-2s | disco: %s"
          % (nombre, CR.vuelta_de_fichero(nombre),
             "SI" if os.path.exists(pth) else "NO",
             (os.path.getsize(pth) if os.path.exists(pth) else "n/a")))
except Exception as e:
    w("   NO SE PUDO IMPORTAR cerrar_reporte: %r" % (e,))
w("LA P.1, EL ARNES EN ROJO, MEDIDO Y NO RECORDADO:")
RP1 = "scripts/loop/vuelta172_tarea1c_guarda_que_mordio.py"
P1 = os.path.join(RAIZ, RP1.replace("/", os.sep))
w("   %s existe: %s" % (RP1, "SI" if os.path.exists(P1) else "NO"))
if os.path.exists(P1):
    g1 = bytes_de_git(RP1)
    w("   -> disco %d bytes | git %s"
      % (os.path.getsize(P1), ("%d bytes" % g1) if g1 is not None else "NO ESTA EN HEAD"))
    c_p1, o_p1 = correr([PY, RP1])
    w("   CORRIDO HOY -> EXITCODE %d, %d bytes de salida"
      % (c_p1, len(o_p1.encode("utf-8"))))
    for l in o_p1.replace(chr(13), "").split(NL):
        if l.strip():
            w("      | " + l.strip()[:140])
    c_nac, o_nac = git(["log", "--diff-filter=A", "--format=%h%x09%ad%x09%s",
                        "--date=short", "--", RP1])
    w("   COMMIT DE NACIMIENTO (git log --diff-filter=A): %s"
      % (o_nac.strip()[:160] or "(no localizado)"))
VMV = None
try:
    import verificar_mutaciones_viejas as VMV   # noqa: E402
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _a in VMV.VIEJAS]
    w("   esta en el censo arneses_del_directorio(): %s"
      % ("SI" if os.path.basename(P1) in censo else "NO"))
    w("   esta en la nomina VIEJAS: %s"
      % ("SI" if os.path.basename(P1) in nomina else "NO"))
    w("   CIFRA censo: %d | CIFRA nomina: %d | VARA_DEL_CENSO: %d"
      % (len(censo), len(nomina), VMV.VARA_DEL_CENSO))
    w("   FAMILIAS_DE_ARNES: %s" % ", ".join(VMV.FAMILIAS_DE_ARNES))
except Exception as e:
    w("   NO SE PUDO RECOMPUTAR EL CENSO: %r" % (e,))
w("")

w("=== H.7 TAREA 1.c: EL TRAMO DE LA CIEGA DE LA 181, LEIDO DEL ACTA ===")
w("(los 30 puestos NO se teclean: se sacan de la linea del acta que los lista y")
w(" se parsean. Si el acta no los trae, se dice y no se inventa ninguno)")
puestos_ciega = []
if CAB181:
    base = CAB181[0]
    for i in range(base, len(l_acta)):
        if "LOS 30 PUESTOS SON" in l_acta[i]:
            bloque = NL.join(l_acta[i:i + 4])
            w("   LINEA %d del acta, y sus tres siguientes:" % (i + 1))
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
w("")

w("=== H.8 TAREA 2: EL AISLADOR Y LA APERTURA DEL AUDITOR, ANTES DE ESCRIBIRLA ===")
for r in ("scripts/loop/aislador_de_ciega.py",
          "scripts/loop/verificar_apertura_sellada.py",
          "scripts/loop/apertura_del_auditor.py",
          "scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py"):
    pth = os.path.join(RAIZ, r.replace("/", os.sep))
    g = bytes_de_git(r)
    w("   %-58s -> disco %s | git %s"
      % (r, ("%d bytes" % os.path.getsize(pth)) if os.path.exists(pth) else "NO EXISTE",
         ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("   (los dos ultimos NO EXISTEN al abrir, y eso es lo correcto: los escribe")
w("    esta vuelta. Si existieran al abrir, seria que la vuelta ya se corrio)")
AIS = os.path.join(RAIZ, "scripts", "loop", "aislador_de_ciega.py")
t_ais = io.open(AIS, encoding="utf-8", errors="replace").read().replace(chr(13) + NL, NL)
w("   aislador_de_ciega.py -> %d lineas" % len(t_ais.split(NL)))
for aguja in ("def guarda_de_fuga", "def elegir_pares", "def escribir_ciega",
              "--criterio", "--puestos", "--semilla", "CAMPOS_CIEGOS"):
    hits = [i for i, l in enumerate(t_ais.split(NL), 1) if aguja in l]
    w("   %-22s -> lineas %s"
      % (repr(aguja), ", ".join(str(x) for x in hits[:6]) or "(ninguna)"))
w("   LAS TRES COSAS QUE EL REMEDIO PROHIBE ANTES DEL SELLO, nombradas aqui para")
w("   que el gemelo no las pueda elegir despues: git log, git status, REPORTE.md")
w("")

w("=== H.9 TAREA 3: EL ARCHIVO DE VEREDICTOS Y EL 2.464, RECONTADOS ===")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
filas = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
w("docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> %d filas | disco %d bytes"
  % (len(filas), os.path.getsize(VER)))
por_clase = {}
for f in filas:
    por_clase[f.get("clase")] = por_clase.get(f.get("clase"), 0) + 1
for k in sorted(por_clase, key=lambda x: (x is None, x)):
    w("   CIFRA clase %-6s: %d" % (repr(k), por_clase[k]))
w("   SUMA de las clases: %d | filas: %d | CALZAN: %s"
  % (sum(por_clase.values()), len(filas),
     "SI" if sum(por_clase.values()) == len(filas) else "NO"))
puestos = [f.get("puesto_intra") for f in filas]
w("   MIN puesto %s | MAX puesto %s | HUECOS %d | DUPLICADOS %d"
  % (min(puestos), max(puestos),
     len(set(range(min(puestos), max(puestos) + 1)) - set(puestos)),
     len(puestos) - len(set(puestos))))
EL_2464 = [f for f in filas if f.get("puesto_intra") == 2464]
w("   EL PUESTO 2464, LOCALIZADO Y NO RECORDADO: %d fila(s)" % len(EL_2464))
for f in EL_2464:
    w("      nodo_a: %s" % f.get("nodo_a"))
    w("      nodo_b: %s" % f.get("nodo_b"))
    w("      clase : %s | dominio: %s" % (f.get("clase"), f.get("dominio")))
    w("      razon : %s" % str(f.get("razon"))[:400])
w("   LOS CAMPOS DE UNA FILA, LISTADOS PARA QUE EL INSTRUMENTO NO INVENTE NINGUNO:")
w("      %s" % ", ".join(sorted(filas[0].keys())))
w("EL GRAFO DE HOY, ABIERTO PARA VER SI EL DIFERENCIADOR SIGUE AHI:")
GR = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
w("   dataset/metadata/master_graph.json -> disco %d bytes" % os.path.getsize(GR))
try:
    G = json.load(io.open(GR, encoding="utf-8"))
    w("   LAS CLAVES DE LA RAIZ, LISTADAS Y NO ADIVINADAS: %s"
      % ", ".join(sorted(G.keys()) if isinstance(G, dict) else ["(no es dict)"]))
    porid = nodos_por_id(G)
    w("   CIFRA nodos del grafo, contados de la clave que existe: %d" % len(porid))
    if porid:
        una = sorted(porid)[0]
        w("   LAS CLAVES DE UN NODO (%s): %s"
          % (una, ", ".join(sorted(porid[una].keys()))))
    for nid in ("cero_defectos", "zero_defects_concepto"):
        n = porid.get(nid)
        if n is None:
            w("   %s -> NO ESTA EN EL GRAFO DE HOY" % nid)
            continue
        pasos = pasos_del_nodo(n)
        w("   %s -> %d pasos (clave usada: %s)"
          % (nid, len(pasos), clave_de_pasos(n)))
        for k, ps in enumerate(pasos, 1):
            w("      paso %d: %s" % (k, str(ps)[:170]))
except Exception as e:
    w("   NO SE PUDO ABRIR EL GRAFO: %r" % (e,))
w("")

w("=== H.10 TAREA 5: LAS BATERIAS Y SUS TRAMOS, CONTADAS DE SU DIRECTORIO ===")
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
w("EL LANZADOR POR TRAMOS DE LA 176, QUE ES EL PRECEDENTE QUE LA DECISION CITA:")
RBT = "scripts/loop/vuelta176_bateria_por_tramos.py"
BT = os.path.join(RAIZ, RBT.replace("/", os.sep))
w("   %s existe: %s | disco %s bytes"
  % (RBT, "SI" if os.path.exists(BT) else "NO",
     os.path.getsize(BT) if os.path.exists(BT) else "n/a"))
if os.path.exists(BT):
    t_bt = io.open(BT, encoding="utf-8", errors="replace").read().replace(chr(13) + NL, NL)
    for i, l in enumerate(t_bt.split(NL), 1):
        if "TRAMOS" in l and "=" in l and not l.strip().startswith("#"):
            w("      LINEA %d: %s" % (i, l.strip()[:150]))
w("EL RELOJ DE LAS CORRIDAS VIEJAS, LEIDO CON reloj_de_la_corrida():")
if VMV is None:
    w("   NO SE PUDO LEER EL RELOJ: el modulo de la bateria no se importo")
else:
    for n in vivas:
        pth = os.path.join(LOOP, n)
        if os.path.getsize(pth) == 0:
            w("   %-50s CERO BYTES: no hay reloj que leer" % n)
            continue
        tt = io.open(pth, encoding="utf-8", errors="replace").read()
        rl = VMV.reloj_de_la_corrida(tt)
        cost = VMV.minutos_por_entrada(rl)
        w("   %-50s tramos con reloj: %2d | minutos por entrada (MAXIMO): %s"
          % (n, len(rl), ("%.4f" % cost) if cost is not None else "(sin reloj)"))
    w("   TOPE_DE_MINUTOS_POR_TRAMO = %s" % VMV.TOPE_DE_MINUTOS_POR_TRAMO)
    ultima, faltan = VMV.arneses_que_faltan()
    w("   arneses_que_faltan() HOY: ultima vuelta %s, faltan %d" % (ultima, len(faltan)))
    for n in faltan:
        w("      FALTA: %s" % n)
    invis = VMV.nomina_invisible_al_censo()
    w("   nomina_invisible_al_censo(): %d" % len(invis))
    malas = VMV.guarda_del_sujeto_congelado()
    w("   guarda_del_sujeto_congelado(): %d entradas sin congelar" % len(malas))
    for nombre, veredicto, vive in malas:
        w("      SUJETO SIN CONGELAR: %-46s %s" % (nombre, veredicto))
w("EL REGISTRO DEL SUJETO CONGELADO, CONTADO DE SU FICHERO:")
if os.path.exists(REGISTRO_SC):
    filas_sc = [json.loads(l) for l in io.open(REGISTRO_SC, encoding="utf-8") if l.strip()]
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> %d filas, disco %d bytes"
      % (len(filas_sc), os.path.getsize(REGISTRO_SC)))
else:
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> NO EXISTE")
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
