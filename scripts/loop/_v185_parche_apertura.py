# -*- coding: utf-8 -*-
r"""_v185_parche_apertura.py . EL PARCHE QUE CONVIERTE EL CLON DEL BLOQUE DE
APERTURA DE LA 184 EN EL DE LA 185.

Se guarda con nombre y no se tira, para que el clon sea auditable: quien quiera
saber que cambio entre vuelta184_apertura.py y vuelta185_apertura.py tiene aqui
el trozo exacto que se sustituyo, y ademas
scripts/loop/cotejar_clon_declarado.py lo mide por su cuenta. NO SE AFIRMA QUE
NINGUN DIFF SALGA VACIO: se publica lo que salga.

LO QUE CAMBIA, DECLARADO Y NO ESCONDIDO:
  1. EL DOCSTRING, que cuenta de que vuelta es y que promete su encargo.
  2. LAS LINEAS DEL REGIMEN del sello de apertura: la 185 NO ES VUELTA DE
     BATERIA y su seccion 9 cierra con hueco declarado.
  3. SUJETOS y RUTAS_DEL_ENCARGO, que son las de ESTE encargo.
  4. LOS BLOQUES H, que miden lo que ESTE encargo promete y nada mas. El H.9,
     el archivo de veredictos, se conserva palabra por palabra porque es la
     guarda que esta vuelta no puede mover.

USO:
  python scripts/loop/_v185_parche_apertura.py
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ORIGEN = os.path.join(RAIZ, "scripts", "loop", "vuelta184_apertura.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop", "vuelta185_apertura.py")
NL = chr(10)

DOCSTRING = '''# -*- coding: utf-8 -*-
r"""vuelta185_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 185, ENTERO Y
ANTES DE LA PRIMERA OPERACION.

CLON DECLARADO de scripts/loop/vuelta184_apertura.py. Cambia el SUFIJO de las
salidas (185, computado del nombre del fichero), la lista RUTAS_DEL_ENCARGO, las
lineas del regimen y los bloques H, que aqui miden lo que ESTE encargo promete y
nada mas. Y LA AFIRMACION DE CLON SE MIDE: el cotejo lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte con lo
que salga. NO se afirma que el diff salga vacio.

QUE ES ESTA VUELTA Y QUE NO ES. NO ES VUELTA DE BATERIA: la bateria cerro entera
en la 184 con sus nueve tramos sellados y por AUDITOR.md 6.1 corre CADA CINCO
VUELTAS, asi que la siguiente es la 189. La seccion 9 del reporte de la 185
cierra CON EL HUECO DECLARADO Y MEDIDO. El tope sigue en DOS SUB-TAREAS
(AUDITOR.md 6.2), porque la 184 no cerro su propio reporte y la cuenta sigue en
cero.

EL ORDEN DE ESTA VUELTA NO ES EL DE SIEMPRE, Y EL MOTIVO SE DICE. El reporte de
la 184 se cierra ANTES de tallar el esqueleto de la 185, con la guarda ya
reparada por la TAREA 1.c. Si el esqueleto corriera antes, su PASO 0 archivaria
el reporte de la 184 SIN CERRAR y la reparacion llegaria tarde para el unico
reporte al que le sirve. Por eso ESTE FICHERO NO ARCHIVA NADA y NO TOCA
REPORTE.md: hasta el paso 4 del encargo, el reporte del arbol sigue siendo el de
la 184.

EL SELLO DEL AUDITOR DE ESTA VUELTA NO SE DEDUCE DEL NUMERO DE VUELTA. El
auditor declaro su caida propia A.1: nombro su sello V185b cuando la casa lo
nombra V186. Las rutas exactas van en RUTAS_DEL_ENCARGO y en el bloque H.5, y el
sha256 se COMPUTA y se COMPARA, no se copia del encargo.

EL BLOQUE H NO TECLEA NINGUN HASH NI NINGUNA CIFRA (EJECUTOR.md 2, EL
INSTRUMENTO MANDA). El encargo da cifras (735 bytes del sello, 39740 y 33733 de
la ciega y el destape, 2435 del tallador de la 184, 13982 del cuerpo, 71753 de
la bateria compuesta); aqui NO SE COPIA NINGUNA: se corre y se imprime lo que
salga, y la comparacion con lo que el encargo dice se hace despues, en el
reporte, con las dos al lado.

LA CIFRA DE BYTES SE PUBLICA POR LAS DOS CONVENCIONES (acta 177 punto 7.11):
disco (os.path.getsize) y git (git cat-file -s). Y la P.2 del fundador manda
BYTES EXACTOS Y NUNCA REDONDEADOS.

POR QUE SE CORRE AQUI: EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION". El encargo manda ademas commitear lo pendiente antes de
tocar nada, y un commit MUEVE HEAD: por eso este bloque corre PRIMERO.

ESTE FICHERO NO TOCA REPORTE.md, NO toca la nomina, NO corre la bateria, NO
archiva ningun reporte y NO escribe en docs/plan/: sus salidas son
SALIDA_V185_*.txt.

LO QUE ESTA SESION SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano al abrir la sesion, dio CERO
lineas (arbol limpio, sin ni siquiera la M de master_graph.json que las vueltas
anteriores traian), y git diff --numstat -- dataset/ dio CERO filas. La
prediccion se escribe AQUI, antes de correr, y los bloques C/D/E/F de abajo la
miden sin saber lo que hay escrito.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

USO:
  python scripts/loop/vuelta185_apertura.py
"""
'''

REGIMEN_VIEJO = '''w("regimen: VUELTA DE BATERIA. AUDITOR.md 6.1: una vuelta cortada RETOMA EN EL")
w("         TRAMO SIGUIENTE y la bateria se declara corrida cuando los NUEVE")
w("         tramos tienen salida sellada del mismo calibre. El acta 184, punto 8,")
w("         mide 5 de 9 y manda retomar en el TRAMO 6, con el 5 re-corrido.")
w("         Esta vuelta ABRE REPORTE PROPIO y archiva el de la 183 en su PASO 0.")
w("         DOS sub-tareas, que es el tope del regimen temporal 6.2, y el acta")
w("         184 punto 8 lo remide: la 182 cerro su reporte y la 183 NO.")'''

REGIMEN_NUEVO = '''w("regimen: NO ES VUELTA DE BATERIA. AUDITOR.md 6.1: la bateria corre CADA CINCO")
w("         vueltas y cerro entera en la 184, asi que la siguiente es la 189. La")
w("         seccion 9 del reporte de la 185 cierra CON EL HUECO DECLARADO Y")
w("         MEDIDO por el carril de cerrar_reporte.py: nombre, bytes y")
w("         atribucion, las tres juntas o no vale.")
w("         DOS sub-tareas, que es el tope del regimen temporal 6.2: la 184 NO")
w("         cerro su propio reporte (exitcode 1), asi que la cuenta de vueltas")
w("         que cierran su reporte SIGUE EN CERO.")
w("         ESTE FICHERO NO ARCHIVA NADA: el reporte de la 184 se cierra en la")
w("         TAREA 2.a, ANTES del esqueleto de la 185, y por eso el PASO 0 del")
w("         esqueleto no tendra reporte ajeno que archivar.")'''

SUJETOS_VIEJO_INICIO = 'SUJETOS = ['
SUJETOS_NUEVO = '''SUJETOS = [
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py",
    "scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py",
    "scripts/loop/_v184_tallar_t2.py",
    "scripts/loop/serie_de_registros.py",
    "scripts/loop/vuelta184_tarea1a_registrar_acta184.py",
    "scripts/loop/vuelta184_tarea1d_relectura_al_doble.py",
    "scripts/loop/vuelta182_tarea1c_relectura_al_doble.py",
    "scripts/loop/cotejar_clon_declarado.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/tallar_cabecera_reporte.py",
    "scripts/loop/vuelta184_esqueleto_reporte.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/SELLO_APERTURA_AUDITOR_V185b.json",
    "docs/loop/_auditor_v185b_ciega_blind.txt",
    "docs/loop/_auditor_v185b_ciega_reveal.txt",
    "docs/loop/_auditor_v185_ciega_blind.txt",
    "docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt",
    "scripts/loop/_v184_cierre_texto.md",
    "docs/loop/SALIDA_V183_BATERIA.txt",
    "docs/loop/SALIDA_V184_CERRAR_REPORTE.txt",
    "docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt",
    "docs/loop/reportes/REPORTE_V183.md",
    "docs/PENDIENTES.md",
    "docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "scripts/loop/guarda_commit_dataset.py",
    "scripts/loop/anexar_tarea_al_reporte.py",
] + SUJETOS
'''

NUEVOS_H = r'''w("=== H. EL REPORTE EN HEAD, MEDIDO SIN CREERLE AL ENCARGO ===")
w("(el encargo dice que el de la 184 sigue SIN CERRAR y SIN ARCHIVAR, y que ESTA")
w(" vuelta lo cierra en su TAREA 2.a ANTES de tallar el esqueleto propio. Aqui se")
w(" mide que es y en que estado esta, sin tocarlo y sin archivar nada)")
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

w("=== H.1 LAS TRES PIEZAS CON LAS QUE SE CERRARA EL REPORTE DE LA 184 ===")
w("(TAREA 2.a. El encargo da tres cifras y aqui NO SE COPIA NINGUNA: se mide")
w(" cada pieza por las dos convenciones y con su sha256, y la comparacion con lo")
w(" que la 184 midio se hace despues, en el reporte, con las dos al lado)")
for r in ("docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt",
          "scripts/loop/_v184_cierre_texto.md",
          "docs/loop/SALIDA_V183_BATERIA.txt"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if not os.path.exists(p):
        w("   %s -> NO EXISTE. Sin ella no se cierra nada, y eso se dice." % r)
        continue
    sd, sl, bd, bl = sha_de(p)
    w("   %s" % r)
    w("      disco %d bytes | LF %d bytes" % (bd, bl))
    w("      sha256 (disco): %s" % sd)
    w("      sha256 (LF)   : %s" % sl)
    g = bytes_de_git(r)
    w("      git cat-file -s HEAD: %s"
      % (("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("")

w("=== H.2 LA GUARDA QUE HAY QUE REPARAR, MEDIDA ANTES DE TOCARLA (TAREA 1.c) ===")
w("(no se teclea ninguna linea: se localiza en el fichero vivo y se pega)")
CER = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
t_cer = io.open(CER, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_cer = t_cer.split(NL)
w("   scripts/loop/cerrar_reporte.py -> %d lineas | disco %d bytes"
  % (len(l_cer), os.path.getsize(CER)))
for aguja in ("def rama_de_la_seccion9", "def vuelta_de_fichero",
              "def vuelta_que_sello", "def tramos_por_vuelta",
              "PATRON_NOMBRE_DE_CORRIDA", "NO CIERRA ESTE REPORTE",
              "tramos_sellados_en_esta_vuelta"):
    hits = [(i, l) for i, l in enumerate(l_cer, 1) if aguja in l]
    w("   %-40s -> %d aparicion(es), lineas %s"
      % (repr(aguja), len(hits), ", ".join(str(i) for i, _l in hits[:10]) or "(ninguna)"))
w("   EL TEXTO DEL ROJO DE LA VUELTA AJENA, TAL COMO ESTA HOY:")
for i, l in enumerate(l_cer, 1):
    if "NO CIERRA ESTE REPORTE" in l or "el fichero de bateria que se pasa" in l:
        w("      LINEA %d: %s" % (i, l.rstrip()[:150]))
w("   EL ARNES VIEJO QUE SIGUE MANDANDO, CORRIDO HOY ANTES DE TOCAR NADA:")
RARN = "scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py"
c_ar, o_ar = correr([PY, RARN])
w("      EXITCODE: %d" % c_ar)
for l in o_ar.replace(chr(13), "").split(NL):
    if ("CIFRA" in l or "VEREDICTO" in l or "NO CALZA" in l):
        w("      | " + l.rstrip()[:150])
w("")

w("=== H.3 EL ARNES QUE PARO LA BATERIA, MEDIDO ANTES DE TOCARLO (TAREA 1.b) ===")
w("(el diagnostico esta medido dos veces, por el ejecutor de la 184 y por el")
w(" auditor de la 185. Aqui se localizan las tres lineas que el encargo nombra,")
w(" 124, 134 y 154, SIN creerle al encargo: se buscan por su contenido)")
RMU = "scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py"
MU = os.path.join(RAIZ, RMU.replace("/", os.sep))
t_mu = io.open(MU, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_mu = t_mu.split(NL)
w("   %s -> %d lineas | disco %d bytes" % (RMU, len(l_mu), os.path.getsize(MU)))
for i, l in enumerate(l_mu, 1):
    if "mkdtemp" in l or "l[:130]" in l or "def sin_temporal" in l:
        w("      LINEA %d: %s" % (i, l.rstrip()[:150]))
w("   CIFRA lineas que contienen 'mkdtemp': %d"
  % len([l for l in l_mu if "mkdtemp" in l]))
w("   CIFRA lineas que contienen 'l[:130]': %d"
  % len([l for l in l_mu if "l[:130]" in l]))
SAL_MU = os.path.join(LOOP, "SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt")
if os.path.exists(SAL_MU):
    sd, sl, bd, bl = sha_de(SAL_MU)
    w("   docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt")
    w("      disco %d bytes | LF %d bytes | sha256 LF %s" % (bd, bl, sl))
    t_sm = io.open(SAL_MU, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    l_sm = t_sm.split(NL)
    w("      lineas: %d" % len(l_sm))
    w("      LAS LINEAS 53, 54 Y 55, QUE SON LAS QUE CAMBIAN SOLAS, PEGADAS:")
    for k in (53, 54, 55):
        if k <= len(l_sm):
            w("         LINEA %d: %s" % (k, l_sm[k - 1].rstrip()[:150]))
    w("      CIFRA lineas que contienen 'v182_apertura_': %d"
      % len([l for l in l_sm if "v182_apertura_" in l]))
    w("      CIFRA lineas que contienen '<TEMPORAL>': %d"
      % len([l for l in l_sm if "<TEMPORAL>" in l]))
else:
    w("   LA SALIDA SELLADA DEL ARNES NO EXISTE.")
w("")

w("=== H.4 LA COLUMNA TECLEADA DE LA ESCALADA (TAREA 1.d) ===")
w("(la caida R.1 del acta 185 nombra la linea 128 de _v184_tallar_t2.py. Aqui se")
w(" busca por contenido y se publica la linea que salga, sea la 128 o no)")
RTT = "scripts/loop/_v184_tallar_t2.py"
TT = os.path.join(RAIZ, RTT.replace("/", os.sep))
t_tt = io.open(TT, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_tt = t_tt.split(NL)
w("   %s -> %d lineas | disco %d bytes" % (RTT, len(l_tt), os.path.getsize(TT)))
for i, l in enumerate(l_tt, 1):
    if "quien" in l:
        w("      LINEA %d: %s" % (i, l.rstrip()[:150]))
w("   LOS NUEVE TRAMOS Y EL ASUNTO DE SU ULTIMO COMMIT, LEIDOS DE GIT HOY:")
for n in range(1, 10):
    rt = "docs/loop/SALIDA_V183_BATERIA_TRAMO_%d.txt" % n
    c_l, o_l = git(["log", "-1", "--format=%h %s", "--", rt])
    w("      tramo %d -> %s" % (n, o_l.strip()[:150] or "(sin commit)"))
w("")

w("=== H.5 EL SELLO DEL AUDITOR V185b Y SU CIEGA (TAREA 1.e) ===")
w("(el encargo manda cotejar el sha256 del fichero ciego contra el sello ANTES")
w(" de releer nada. AQUI NO SE COPIA EL DEL ENCARGO: se computa y se compara.")
w(" Y el nombre del sello NO se deduce del numero de vuelta: el auditor declaro")
w(" su caida propia A.1 y el encargo da las tres rutas exactas)")
SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_V185b.json")
if os.path.exists(SELLO):
    w("   docs/loop/SELLO_APERTURA_AUDITOR_V185b.json -> disco %d bytes"
      % os.path.getsize(SELLO))
    sello = json.loads(io.open(SELLO, encoding="utf-8").read())
    w("   CLAVES DEL SELLO: %s" % ", ".join(sorted(sello.keys())))
    w("   EL SELLO ENTERO, PEGADO Y NO RESUMIDO:")
    for l in json.dumps(sello, indent=2, ensure_ascii=False).split(NL):
        w("      | " + l[:150])
else:
    w("   EL SELLO NO EXISTE. Sin el no se relee nada, y eso se dice.")
for nombre in ("_auditor_v185b_ciega_blind.txt", "_auditor_v185b_ciega_reveal.txt",
               "_auditor_v185_ciega_blind.txt"):
    p = os.path.join(LOOP, nombre)
    if not os.path.exists(p):
        w("   docs/loop/%s -> NO EXISTE" % nombre)
        continue
    sd, sl, bd, bl = sha_de(p)
    t_c = io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    puestos = sorted({int(x) for x in re.findall(r"PUESTO\s+(\d+)", t_c)})
    w("   docs/loop/%s" % nombre)
    w("      disco %d bytes | LF %d bytes | lineas %d" % (bd, bl, t_c.count(NL)))
    w("      sha256 (disco): %s" % sd)
    w("      sha256 (LF)   : %s" % sl)
    w("      CIFRA puestos con el patron 'PUESTO <n>': %d" % len(puestos))
    w("      LOS PUESTOS: %s" % ", ".join(str(x) for x in puestos))
w("   LAS SIETE DISCREPANCIAS QUE EL ACTA 185 NOMBRA, BUSCADAS EN LOS DOS")
w("   FICHEROS CIEGOS PARA SABER SI ESTAN DENTRO DEL UNIVERSO:")
SIETE = [1208, 1459, 2363, 2386, 2505, 2636, 2854]
for nombre in ("_auditor_v185b_ciega_blind.txt", "_auditor_v185_ciega_blind.txt"):
    p = os.path.join(LOOP, nombre)
    if not os.path.exists(p):
        continue
    t_c = io.open(p, encoding="utf-8", errors="replace").read()
    puestos = {int(x) for x in re.findall(r"PUESTO\s+(\d+)", t_c)}
    dentro_siete = [x for x in SIETE if x in puestos]
    w("      %s -> de los siete estan dentro: %s"
      % (nombre, ", ".join(str(x) for x in dentro_siete) or "(ninguno)"))
w("")

w("=== H.6 LA SERIE DE REGISTROS Y EL ACTA 185 (TAREA 1.a) ===")
w("(no se teclea ningun numero de registro: se llama a serie_de_registros.py y")
w(" se imprime lo que devuelva. R.47 NO se da por bueno porque lo diga el encargo)")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
t_acta = io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_acta = t_acta.split(NL)
w("docs/loop/ACTA_AUDITOR.md -> %d lineas | disco %d bytes | LF %d bytes"
  % (len(l_acta), os.path.getsize(ACTA), len(t_acta.encode("utf-8"))))
CAB185 = [i for i, l in enumerate(l_acta, 1)
          if l.startswith("# ACTA DEL AUDITOR, VUELTA 185")]
w("CIFRA cabeceras del acta 185 encontradas: %d" % len(CAB185))
if CAB185:
    base = CAB185[0]
    w("   CABECERA del acta 185 en la LINEA %d" % base)
    w("   lineas del acta 185, de su cabecera al final del fichero: %d"
      % (len(l_acta) - base + 1))
    for aguja in ("## 1. ", "## 2. ", "## 3. ", "## 4. ", "## 5. ", "## 6. ",
                  "## 7. ", "## 8. ", "## 9. ", "## 10. ", "## 11. "):
        hits = [i for i, l in enumerate(l_acta, 1)
                if l.startswith(aguja) and i >= base]
        w("   %-10s -> lineas %s"
          % (repr(aguja), ", ".join(str(x) for x in hits) or "(ninguna)"))
    w("   LOS NUMERALES DEL ACTA 185, CONTADOS CON EL PATRON DE COMILLAS")
    w("   INVERSAS QUE LA 184 ESTRENO, Y NO DE MEMORIA:")
    for pat in (r"\*\*`5\.(\d)`", r"\*\*`6\.(\d)`", r"`PD\.(\d)`",
                r"`A\.(\d)`", r"`R\.(\d)`"):
        hits = [(i, m.group(1)) for i, l in enumerate(l_acta, 1) if i >= base
                for m in [re.search(pat, l)] if m]
        vistos = sorted({v for _i, v in hits})
        w("      %-16s -> %d aparicion(es), numerales distintos %s"
          % (pat, len(hits), ", ".join(vistos) or "(ninguno)"))
    w("   LAS CABECERAS 5.n Y 6.n DEL ACTA 185, PEGADAS ENTERAS:")
    for i, l in enumerate(l_acta, 1):
        if i >= base and re.match(r"^\*\*`[56]\.\d`", l):
            w("      LINEA %d: %s" % (i, l.strip()[:140]))
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
    for numero, rel_, linea, titulo in halladas[-4:]:
        w("   ULTIMOS: R.%s en %s:%d -> %s" % (numero, rel_, linea, titulo[:100]))
except Exception as e:
    w("NO SE PUDO RECOMPUTAR LA SERIE: %r" % (e,))
w("")

w("=== H.7 LA BATERIA, QUE ESTA VUELTA NO CORRE, Y SU HUECO ===")
w("(AUDITOR.md 6.1: corre cada cinco vueltas y la siguiente es la 189. Aqui se")
w(" mide QUE HAY en disco para poder declarar el hueco con su nombre, sus bytes")
w(" y su atribucion, que son las tres piezas juntas o no vale)")
for r in ("docs/loop/SALIDA_V185_BATERIA.txt", "docs/loop/SALIDA_V184_BATERIA.txt",
          "docs/loop/SALIDA_V183_BATERIA.txt"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        sd, sl, bd, bl = sha_de(p)
        w("   %s -> disco %d bytes | LF %d bytes | sha256 LF %s" % (r, bd, bl, sl))
    else:
        w("   %s -> NO EXISTE" % r)
try:
    import verificar_mutaciones_viejas as VMV   # noqa: E402
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _a in VMV.VIEJAS]
    w("   CIFRA censo: %d | CIFRA nomina: %d | VARA_DEL_CENSO: %d"
      % (len(censo), len(nomina), VMV.VARA_DEL_CENSO))
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

w("=== H.8 QUE REPORTES ESTAN YA ARCHIVADOS EN docs/loop/reportes/ ===")
DIRA = os.path.join(LOOP, "reportes")
arch = sorted(os.listdir(DIRA)) if os.path.isdir(DIRA) else []
for n in arch[-8:]:
    g = bytes_de_git("docs/loop/reportes/" + n)
    w("   %s -> disco %d bytes | git %s"
      % (n, os.path.getsize(os.path.join(DIRA, n)),
         ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("CIFRA reportes archivados: %d" % len(arch))
for n in ("REPORTE_V183.md", "REPORTE_V184.md", "REPORTE_V185.md"):
    w("%s archivado: %s" % (n, "SI" if n in arch else "NO"))
w("")

'''


def main():
    src = io.open(ORIGEN, encoding="utf-8").read().replace(chr(13) + NL, NL)
    # 1. EL DOCSTRING
    fin_doc = src.index('"""', src.index('r"""') + 4) + 3 + 1
    cuerpo = src[fin_doc:]
    # 2. LAS LINEAS DEL REGIMEN
    if REGIMEN_VIEJO not in cuerpo:
        raise SystemExit("ROJO: no encuentro las lineas del regimen en el origen")
    cuerpo = cuerpo.replace(REGIMEN_VIEJO, REGIMEN_NUEVO)
    # 3. SUJETOS Y RUTAS_DEL_ENCARGO, DE UN TAJO
    i0 = cuerpo.index(SUJETOS_VIEJO_INICIO)
    i1 = cuerpo.index("REGISTRO_SC = os.path.join(")
    cuerpo = cuerpo[:i0] + SUJETOS_NUEVO + NL + cuerpo[i1:]
    # 4. LOS BLOQUES H, DEL H. AL H.8 INCLUSIVE
    j0 = cuerpo.index('w("=== H. EL REPORTE EN HEAD')
    j1 = cuerpo.index('w("=== H.9 EL ARCHIVO DE VEREDICTOS')
    cuerpo = cuerpo[:j0] + NUEVOS_H + cuerpo[j1:]
    texto = DOCSTRING + cuerpo
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITO: %s" % DESTINO)
    print("CIFRA bytes: %d | CIFRA lineas: %d"
          % (len(texto.encode("utf-8")), texto.count(NL)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
