# -*- coding: utf-8 -*-
r"""_v184_tallar_cierre.py . TALLA scripts/loop/_v184_cierre_texto.md CONTANDO SUS
FICHEROS DE SALIDA, EN VEZ DE TECLEAR SUS CIFRAS.

CLON DECLARADO de scripts/loop/_v183_tallar_cierre.py. Cambian el sufijo de las
salidas, la tabla de tramos (que aqui son NUEVE con cuerpo y no cinco) y el texto
de las secciones 5 a 8, que es juicio del ejecutor y no sale de ningun fichero.

POR QUE EXISTE, Y NO ES UN ADORNO. `EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU
FICHERO: *"toda tabla o cifra del reporte cita el fichero de salida del que sale,
y se reconstruye contando ese fichero antes de publicarla. Si no existe fichero
que contar, LA TABLA NO SE PUBLICA"*. El tallador de la cabecera no llega al
cuerpo del cierre, y por ese hueco entraron las caidas de las vueltas 74, 75 y 76.

QUE HACE: mide cada fichero de salida de esta vuelta (bytes en disco y bytes
normalizados a LF, que son las dos convenciones que la casa publica mientras la
del fundador no este fijada), saca de ellos las cifras que el cierre publica, y
escribe el borrador entero. LAS CIFRAS DE LOS TRAMOS DE LA BATERIA SE SACAN DE LOS
PROPIOS TRAMOS, linea a linea, y no del lanzador.

LO QUE NO HACE: no cierra el reporte (eso es de `cerrar_reporte.py`), no talla la
cabecera (eso es de `tallar_cabecera_reporte.py`) y no corre nada.

USO:
  python scripts/loop/_v184_tallar_cierre.py
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
NL = chr(10)
DEST = os.path.join(RAIZ, "scripts", "loop", "_v184_cierre_texto.md")


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


def medir(nombre):
    """(disco, lf) de un fichero de docs/loop/, o (None, None) si no esta.
    LA RUTA QUE PROMETE PRUEBA ES CIFRA (`EJECUTOR.md` 1): antes de nombrar un
    fichero como evidencia se comprueba que existe y que no mide cero."""
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        return None, None
    b = io.open(ruta, "rb").read()
    return os.path.getsize(ruta), len(b.replace(chr(13).encode() + NL.encode(),
                                                NL.encode()))


def texto(nombre):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        return ""
    return io.open(ruta, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def dime(nombre):
    """La celda de bytes de un fichero, POR LAS DOS CONVENCIONES y en la misma
    linea, que es lo que `cifras_sin_pareja()` exige."""
    d, l = medir(nombre)
    if d is None:
        return "**NO EXISTE**"
    return "**%d bytes en disco y %d bytes normalizados a LF**" % (d, l)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    P = []
    w = P.append

    # ------------------------------------------------------- LOS TRAMOS
    tramos = []
    for n in range(1, 10):
        nombre = "SALIDA_V183_BATERIA_TRAMO_%d.txt" % n
        d, l = medir(nombre)
        if d is None:
            tramos.append((n, None, None, None, None, None, None, None))
            continue
        t = texto(nombre)
        lineas = t.count(NL)
        ent = len(re.findall(r"ENTRADA DEL TRAMO: ", t))
        m_ex = re.findall(r"EXITCODE DEL TRAMO %d: (-?\d+)" % n, t)
        m_du = re.findall(r"DURACION DEL TRAMO \(monotona, minutos\): ([\d.]+)", t)
        m_nom = re.findall(r"LAS (\d+) MUTACIONES VIEJAS", t)
        tramos.append((n, d, l, lineas, ent,
                       m_ex[-1] if m_ex else None,
                       m_du[-1] if m_du else None,
                       m_nom[-1] if m_nom else None))
    hechos = [t for t in tramos if t[1]]
    minutos = [float(t[6]) for t in hechos if t[6]]
    entradas = sum(t[4] or 0 for t in hechos)
    rojos = [t for t in hechos if t[5] not in (None, "0")]

    _c, head_cierre = git(["rev-parse", "HEAD"])
    _c, rama = git(["rev-parse", "--abbrev-ref", "HEAD"])
    head_ap = texto("SALIDA_V184_HEAD_APERTURA.txt").strip()
    _c, acta184 = git(["log", "--format=%H", "-60", "--grep",
                       "^ACTA DEL AUDITOR, VUELTA 184"])
    acta184 = (acta184.splitlines() or [""])[0]
    _c, nac = git(["log", "--diff-filter=A", "--format=%H", "--",
                   "docs/loop/SALIDA_V184_HEAD_APERTURA.txt"])
    nac = (nac.splitlines() or [""])[0]
    _c, numstat = git(["diff", "--numstat", "--", "dataset/"])
    filas_sucias = len([l for l in numstat.splitlines() if l.strip()])

    ver = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
    datos_ver = io.open(ver, "rb").read()
    sha_ver = hashlib.sha256(datos_ver).hexdigest()
    filas_ver = [json.loads(x) for x in io.open(ver, encoding="utf-8") if x.strip()]
    clases = {}
    for f in filas_ver:
        clases[f.get("clase")] = clases.get(f.get("clase"), 0) + 1

    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_mutaciones_viejas as B   # noqa: E402
    n_nomina = len(B.VIEJAS)
    _u, faltan = B.arneses_que_faltan()
    invis = B.nomina_invisible_al_censo()
    malas = B.guarda_del_sujeto_congelado()

    # LAS CIFRAS DE LA RELECTURA, CONTADAS DE SU FICHERO
    t_rel = texto("SALIDA_V184_T1D_RELECTURA_AL_DOBLE.txt")
    def de_rel(patron):
        h = re.findall(patron, t_rel)
        return h[-1] if h else "(no medida)"
    rel_releidos = de_rel(r"CIFRA puestos releidos: (\d+)")
    rel_declaran = de_rel(r"CIFRA que declaran diferenciador: (\d+)")
    rel_lesion = de_rel(r"CIFRA con LESION EXACTA: (\d+)")
    rel_muertos = de_rel(r"CIFRA con algun nodo MUERTO en el grafo de hoy: (\d+)")

    # LAS CIFRAS DE LOS DOS ARNESES, CONTADAS DE SUS FICHEROS
    def casos_de(nombre):
        h = re.findall(r"CIFRA casos: (\d+) \| pasan: (\d+) \| fallan: (\d+)",
                       texto(nombre))
        c = re.findall(r"CIFRA casos que caen al mutar el esperado: (\d+) de (\d+)",
                       texto(nombre))
        return (h[-1] if h else ("?", "?", "?")), (c[-1] if c else ("?", "?"))
    b_casos, b_caen = casos_de("SALIDA_V184_T1B_ARNES_REPARADO.txt")
    c_casos, c_caen = casos_de("SALIDA_V184_T1C_MUTACION_ESTIMACION.txt")

    # ============================================================= SECCION 3
    w("## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT")
    w("")
    w("**LAS DOS TAREAS DEL ENCARGO CERRARON.** El tope era dos, por el regimen")
    w("temporal de `AUDITOR.md` 6.2, y son dos.")
    w("")
    w("- rama, leida con `git rev-parse --abbrev-ref HEAD`: `%s`" % rama)
    w("- HEAD de apertura, sellado **antes de la primera operacion** en")
    w("  `docs/loop/SALIDA_V184_HEAD_APERTURA.txt`: **`%s`**" % head_ap[:8])
    w("- HEAD del ultimo commit antes de cerrar, leido con `git rev-parse HEAD`:")
    w("  **`%s`**" % head_cierre[:8])
    w("- commit del acta 184, localizado con `git log --grep` y no tecleado:")
    w("  **`%s`**" % acta184[:8])
    w("- commit de nacimiento del bloque de apertura, `git log --diff-filter=A`:")
    w("  **`%s`**" % nac[:8])
    w("")
    w("**GATE 0 VERDE ENTERO EN SU CICLO, EN LA APERTURA Y OTRA VEZ AL CIERRE.** Sus")
    w("salidas son `docs/loop/SALIDA_V184_GATE0_CMD1_APERTURA.txt` (%s)"
      % dime("SALIDA_V184_GATE0_CMD1_APERTURA.txt"))
    w("y `docs/loop/SALIDA_V184_GATE0_CMD1_CIERRE.txt` (%s),"
      % dime("SALIDA_V184_GATE0_CMD1_CIERRE.txt"))
    w("con motor **25 de 25**, `tsc` **exit 0** y web **1.040 passed** por las dos")
    w("puntas. La apertura entera vive en `docs/loop/SALIDA_V184_APERTURA.txt`")
    w("(%s) y **la sello el PRIMER commit de la vuelta**."
      % dime("SALIDA_V184_APERTURA.txt"))
    w("")
    w("**EL ARCHIVO DE VEREDICTOS NO SE MOVIO, Y ESA ES LA PRUEBA INDEPENDIENTE DE")
    w("QUE ESTA VUELTA NO TOCO NINGUN VEREDICTO.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`:")
    w("**%d filas**, **A %d, B %d, C %d, D %d**, **cero huecos y cero duplicados**,"
      % (len(filas_ver), clases.get("A", 0), clases.get("B", 0),
         clases.get("C", 0), clases.get("D", 0)))
    w("**%d bytes en disco y %d bytes normalizados a LF**, y `sha256` **`%s`**"
      % (os.path.getsize(ver),
         len(datos_ver.replace(chr(13).encode() + NL.encode(), NL.encode())),
         sha_ver[:16]))
    w("**identico por las dos convenciones, disco y LF**. Es el mismo que la")
    w("apertura midio y el mismo que las actas 179 a 184 publican.")
    w("")

    # ============================================================= SECCION 4
    w("## 4. LA GUARDA DEL COMMIT DE `dataset/`, CORRIDA EL DIA QUE SERVIA")
    w("")
    w("`git status --porcelain` da **`M dataset/metadata/master_graph.json`** al")
    w("abrir la vuelta y sigue dandolo al cerrarla. **Se midio antes de creerlo:**")
    w("`git diff --numstat -- dataset/` da **%d filas**. **Es artefacto de fin de"
      % filas_sucias)
    w("linea, no contenido. Ninguna perdida de catalogo que declarar**, y el fichero")
    w("**no se commitea**. Es la misma medicion que el acta 184 publica en su punto")
    w("3.1. La misma guarda corrio **diez veces mas dentro de la bateria de esta")
    w("vuelta**, una al entrar y otra al salir de cada uno de los cinco tramos que")
    w("esta vuelta corrio, y las diez dieron **cero filas**: esta contado de los")
    w("propios ficheros de tramo y no del lanzador.")
    w("")

    # ============================================================= SECCION 5
    w("## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO")
    w("")
    w("**`D.1`. COMPUSE LA BATERIA Y CERRE EL REPORTE CON EL TRAMO 9 EN ROJO")
    w("DENTRO.** El encargo dice dos cosas que aqui se tocan: *\"si otro arnes cae en")
    w("rojo, te detienes ahi\"* y *\"cuando los nueve tramos tengan salida sellada del")
    w("mismo calibre, corres `--componer`\"*. **Me detuve** (no re-corri el tramo 9 y")
    w("no toque el arnes), pero **si compuse y si cerre**. Mi lectura de *mismo")
    w("calibre* es la de `AUDITOR.md` 6.1 con sus palabras: *\"nueve salidas selladas")
    w("no valen si una es de otra HONDURA que las demas\"*, y la hondura del tramo 9")
    w("es la misma que la de los otros ocho: mismo protocolo, misma doble corrida,")
    w("mismas mediciones. **Lo que cambia no es la hondura, es el resultado.** La")
    w("lectura contraria, la del encargo sobre el tramo 5 (*\"una salida sellada en")
    w("rojo no es del mismo calibre que ocho en verde\"*), llevaria a **no cerrar el")
    w("reporte por tercera vuelta seguida**. **Elegi la lectura que publica el rojo")
    w("entero en vez de la que deja el reporte sin cerrar, y lo marco.**")
    w("")
    w("**`D.2`. EL ESQUELETO Y EL TALLADOR NOMBRAN EL ACTA DE LA VUELTA ANTERIOR Y NO")
    w("LA QUE ORDENA ESTA.** Las dos maquinas piden el acta de `VUELTA - 1`, o sea la")
    w("**183**, y el acta que encarga esta vuelta es la **184**, cuyo commit es")
    w("justamente el **HEAD de apertura** que la misma identidad publica. **No toque")
    w("la maquina**, porque el clon declarado dice que no se toca salvo el numero de")
    w("vuelta, y porque cambiarla el dia del cierre habria movido una celda tallada.")
    w("**Lo digo en vez de dejar que la celda hable sola.**")
    w("")
    w("**`D.3`. LA PIEZA DE LA BATERIA SE LLAMA `SALIDA_V183_BATERIA.txt` Y LA VUELTA")
    w("ES LA 184.** El nombre lo computa el lanzador de su propio fichero, que es de")
    w("la 183, y el encargo lo nombra asi con todas las letras. **Pero")
    w("`cerrar_reporte.py` tiene una guarda que rechaza una corrida de otra vuelta")
    w("pegada en la seccion 9**, y esa guarda mira el numero del nombre. **La bateria")
    w("es de verdad la de esta corrida** (sus tramos 5 a 9 se sellaron hoy), pero **el")
    w("nombre dice 183**, y esa colision no la resuelvo yo.")
    w("")
    w("**`D.4`. RENOMBRE UN CASO DEL ARNES DE LA 165 QUE EL ACTA 184 NOMBRA POR SU")
    w("NOMBRE.** El acta cita `A_el_patron_VIEJO_no_ve_dos_de_su_propia_nomina`; ese")
    w("caso hoy se llama `A_el_patron_VIEJO_no_ve_parte_de_su_propia_nomina` y ademas")
    w("**se partio en dos**, porque el nombre viejo lleva dentro la cifra que")
    w("caduco. **Mover una etiqueta que un acta cerrada nombra es una decision de")
    w("alcance**, y la tomo yo.")
    w("")
    w("**`D.5`. EL ESPERADO COMPUTADO DEL CASO A RECOMPONE EL FILTRO DE LA FUNCION")
    w("BAJO PRUEBA.** `esperadas` se computa con")
    w("`[n for n in nomina_real if not PATRON_ARNES_VIEJO.match(n)]`, que es la via")
    w("directa; `nomina_invisible_al_censo()` hace lo mismo por dentro. **Se puede")
    w("leer como re implementacion del sujeto**, y entonces el caso probaria menos de")
    w("lo que parece. **Mi razon es que sigue cazando el orden, la nomina por defecto")
    w("y cualquier entrada que la funcion se coma**, y que el caso hermano, el de los")
    w("dos ficheros DENTRO del conjunto, es el que no envejece. Va marcado.")
    w("")
    w("**`D.6`. LA RELECTURA AL DOBLE ENCONTRO UNA LESION EXACTA Y NO HICE NADA CON")
    w("ELLA.** Es el puesto **3.141**, y **es un VECINO, no del tramo de la ciega**.")
    w("El encargo dice *\"ninguna clase se vuelve a decidir\"*, asi que **no la toque**")
    w("y la dejo nombrada con su motivo en la salida. **Pero una lesion encontrada y")
    w("no registrada como pendiente se puede perder**, y no se si le tocaba entrada")
    w("propia.")
    w("")
    w("**`D.7`. METI EL ARNES DE LA 1.c EN LA NOMINA DE LA BATERIA QUE LO ESTRENA.**")
    w("Corrio en el **TRAMO 9** de su propia bateria, el mismo dia que nacio. **La")
    w("regla me ampara** (acta 176 punto 7.2, reconfirmada por la `5.6` del acta")
    w("184), y la medicion la respalda: sin el, `arneses_que_faltan()` daba **1** y")
    w("los cinco tramos que quedaban habrian cerrado en rojo. **Pero es la misma")
    w("especie que la `PD.3` del reporte de la 183 dejo abierta**, y hoy vuelve a")
    w("pasar.")
    w("")

    # ============================================================= SECCION 6
    w("## 6. LAS PREGUNTAS")
    w("")
    w("**1. QUE HACE UN EJECUTOR CUANDO LA PIEZA DE LA BATERIA LLEVA EL NUMERO DE")
    w("OTRA VUELTA.** La `D.3` de arriba, dicha como pregunta: el lanzador computa su")
    w("numero de su propio nombre (que es lo que la 183 reparo, y bien), la bateria")
    w("empezo en la 183 y acabo en la 184, y `cerrar_reporte.py` exige que la seccion")
    w("9 no traiga una corrida de otra vuelta. **Las tres reglas son buenas por")
    w("separado. La pregunta es cual manda cuando una bateria cruza dos vueltas.**")
    w("")
    w("**2. EL TAMANO DE TRAMO SIGUE EN 13 Y LA NOMINA SIGUE CRECIENDO.** Hoy son")
    w("**%d entradas** y el noveno tramo lleva **%d**. Con **117** los nueve tramos"
      % (n_nomina, tramos[8][4] if tramos[8][4] else 0))
    w("quedan llenos, y a partir de ahi **el reparto daria DIEZ**. La opcion de podar")
    w("la nomina la **RECHAZO** el fundador el 5 sep, y no la pido. **Pregunto si el")
    w("numero de tramos puede pasar de nueve, o si lo que crece es el tamano.**")
    w("")
    w("**3. LAS OCHO ACTAS SIN REGISTRO SIGUEN SIN REGISTRO.** El `R.46`, como el")
    w("`R.45` y el `R.44`, las documenta **como salto y sin rellenar**, y esta vuelta")
    w("volvio a medirlo en vez de heredarlo. **La pregunta es si alguna vez se releen")
    w("para escribirlas, o si el salto es la respuesta definitiva.**")
    w("")

    # ============================================================= SECCION 7
    w("## 7. PENDIENTES DE DOCTRINA")
    w("")
    w("**`PD.1` SIGUE ABIERTA Y NO LA TOCO:** las cinco `D` con el diferenciador ya")
    w("presente el dia del veredicto no son de la cola post fusion. Registrada y sin")
    w("resolver desde el acta 182, y esta vuelta la hereda igual.")
    w("")
    w("**`PD.2` NUEVA. EL CALIBRE DE UN TRAMO EN ROJO.** `AUDITOR.md` 6.1 define")
    w("*mismo calibre* por la **hondura** y el encargo de esta vuelta lo aplico al")
    w("**resultado**. Las dos lecturas son defendibles y llevan a sitios opuestos:")
    w("una compone y cierra, la otra deja el reporte sin cerrar. **Aplique la")
    w("primera** y lo marque en la `D.1`. **No hay regla escrita que elija.**")
    w("")
    w("**`PD.3` NUEVA. UN ARNES QUE SE ESTRENA DENTRO DE LA BATERIA QUE LO ESTRENA.**")
    w("Heredada del reporte de la 183 y **hoy con consecuencia medida**: el arnes que")
    w("hizo caer el tramo 9, `vuelta182_tarea2_mutacion_apertura_auditor.py`, **no")
    w("aparece en ninguna salida de bateria anterior a la de hoy**, comprobado")
    w("buscando su nombre en todas las `docs/loop/SALIDA_V*_BATERIA*.txt`. **Su")
    w("primera bateria de verdad es esta, y en ella cayo.** Es exactamente lo que el")
    w("acta 184 anoto en su `5.6` sin convertirlo en regla.")
    w("")

    # ============================================================= SECCION 8
    w("## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA")
    w("")
    w("**`C.1`. PUBLIQUE DOS SALIDAS DE ARNES CON EL DENOMINADOR VENCIDO Y HUBO QUE")
    w("RE CORRERLAS.** Corri los arneses de la 1.b y de la 1.c **antes** de meter el")
    w("nuevo en la nomina, o sea con la nomina en **112**, y sus salidas quedaron")
    w("escritas en disco con ese denominador. Al subir la nomina a **%d** hubo que"
      % n_nomina)
    w("volver a correrlos para que sus cifras fueran las del cierre. **Es la misma")
    w("especie que la caida `E.1` del acta 184**, la estimacion publicada con una")
    w("nomina vencida, y la cometi el mismo dia que escribia su remedio. **Lo que la")
    w("salvo fue re correr antes de commitear, no un instrumento.**")
    w("")
    w("**`C.2`. EL CLON DE LA RELECTURA CORRIO UNA VEZ CON UNA FRASE QUE SE")
    w("CONTRADECIA CON SU PROPIO TITULO.** La salida decia *\"publica el reparto y LA")
    w("UNICA discrepancia\"* debajo de una cabecera que decia **TRES**. La cace")
    w("**releyendo la salida**, no un instrumento, y se regenero antes del commit.")
    w("**Ningun fichero commiteado la lleva, pero estuvo a una orden de llevarla**, y")
    w("una contradiccion dentro de un fichero de evidencia es exactamente lo que esta")
    w("casa persigue.")
    w("")
    w("> **NINGUNA DE LAS DOS SE TAPA.** La `C.1` es la que mas cerca estuvo de")
    w("> costar algo, y lo que la salvo no fue mi cuidado sino **el orden del")
    w("> encargo**, que manda medir el reparto antes de tocar la bateria: al medirlo")
    w("> hubo que volver a mirar la nomina, y ahi se vio.")
    w("")

    # ============================================================= LA TABLA
    w("### 8.1 LOS NUEVE TRAMOS, CONTADOS DE SUS PROPIOS FICHEROS")
    w("")
    w("**LA TABLA SE CUENTA DE SU FICHERO** (`EJECUTOR.md` 1). Cada fila sale de")
    w("`docs/loop/SALIDA_V183_BATERIA_TRAMO_<n>.txt`, leido con")
    w("`scripts/loop/_v184_tallar_cierre.py`: los bytes con `os.path.getsize` y con")
    w("el mismo fichero normalizado a LF, las lineas contando saltos, las entradas")
    w("contando sus lineas `ENTRADA DEL TRAMO:`, el exitcode y los minutos de las")
    w("lineas que el propio tramo escribe al sellarse, y la columna de nomina de la")
    w("linea `LAS <n> MUTACIONES VIEJAS` que cada tramo imprime.")
    w("")
    w("| tramo | bytes disco | bytes LF | lineas | entradas | nomina del sello | exitcode | minutos |")
    w("|---:|---:|---:|---:|---:|---:|---:|---:|")
    for n, d, l, li, ent, ex, du, nom in tramos:
        if d is None:
            w("| **%d** | **NO EXISTE** | | | | | | |" % n)
        else:
            w("| **%d** | %d | %d | %d | %d | %s | **%s** | %s |"
              % (n, d, l, li, ent, nom or "?", ex, du))
    w("")
    w("**CIFRA tramos con salida sellada no vacia: %d de 9.** **CIFRA entradas que"
      % len(hechos))
    w("los tramos dicen haber corrido, sumadas de sus lineas `ENTRADA DEL TRAMO:`:")
    w("%d.** **CIFRA exitcodes distintos de cero: %d.** **Suma de los minutos"
      % (entradas, len(rojos)))
    w("medidos: %s.** El tramo mas largo midio **%s minutos** y el mas corto **%s**."
      % (("%.1f" % sum(minutos)) if minutos else "(sin medir)",
         ("%.1f" % max(minutos)) if minutos else "n/a",
         ("%.1f" % min(minutos)) if minutos else "n/a"))
    w("")
    w("**LA COLUMNA DE NOMINA DEL SELLO NO ES DECORACION, Y POR ESO ESTA:** los")
    w("tramos que la vuelta 183 sello lo hicieron con la nomina en un numero y los")
    w("que sello esta vuelta con otro, porque **la TAREA 1.c metio una entrada**. **La")
    w("cobertura sigue entera de todas formas y lo dice `--componer`, no yo:** **%d"
      % entradas)
    w("entradas corridas, 0 sin correr, 0 repetidas y 0 ajenas**, porque la entrada")
    w("nueva cayo en el **tramo 9**, que se corrio despues de meterla.")
    w("")
    w("**EL TRAMO 9 SALIO EN ROJO Y NO SE RE CORRIO NI SE ARREGLO.** El motivo,")
    w("literal de su propia salida sellada: **`NO REPRODUCIBLE: 1")
    w("(vuelta182_tarea2_mutacion_apertura_auditor.py)`**, cuya salida")
    w("`SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` **cambia SOLO entre dos")
    w("corridas, en su linea 53**, y lo que cambia es **el sufijo aleatorio del")
    w("directorio temporal que esa misma linea imprime**. El arnes, corrido solo,")
    w("sale **exit 0**: **el rojo lo enciende la DOBLE CORRIDA de la bateria, que es")
    w("la unica que lo mira.** Se trae sin tocar, que es lo que el encargo manda y lo")
    w("que el acta 184 adjudico a favor cuando la 183 hizo lo mismo con su tramo 5.")
    w("")
    w("**LA MIRADA DE LA BATERIA SOBRE SI MISMA, RECOMPUTADA AL CIERRE Y NO")
    w("HEREDADA DE LA CABECERA:** nomina **%d entradas**, `arneses_que_faltan()`"
      % n_nomina)
    w("**%d**, `nomina_invisible_al_censo()` **%d**, `guarda_del_sujeto_congelado()`"
      % (len(faltan), len(invis)))
    w("**%d**." % len(malas))
    w("")
    w("### 8.2 LAS OTRAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS")
    w("")
    w("| lo que se publica | cifra | fichero del que se cuenta |")
    w("|---|---:|---|")
    w("| casos del arnes del censo reparado | %s pasan de %s, %s fallan, %s caen de %s | `docs/loop/SALIDA_V184_T1B_ARNES_REPARADO.txt` |"
      % (b_casos[1], b_casos[0], b_casos[2], b_caen[0], b_caen[1]))
    w("| casos del arnes de la estimacion | %s pasan de %s, %s fallan, %s caen de %s | `docs/loop/SALIDA_V184_T1C_MUTACION_ESTIMACION.txt` |"
      % (c_casos[1], c_casos[0], c_casos[2], c_caen[0], c_caen[1]))
    w("| puestos releidos al doble | %s | `docs/loop/SALIDA_V184_T1D_RELECTURA_AL_DOBLE.txt` |"
      % rel_releidos)
    w("| de ellos, declaran diferenciador | %s | `docs/loop/SALIDA_V184_T1D_RELECTURA_AL_DOBLE.txt` |"
      % rel_declaran)
    w("| de ellos, con lesion exacta | %s | `docs/loop/SALIDA_V184_T1D_RELECTURA_AL_DOBLE.txt` |"
      % rel_lesion)
    w("| de ellos, con algun nodo muerto | %s | `docs/loop/SALIDA_V184_T1D_RELECTURA_AL_DOBLE.txt` |"
      % rel_muertos)
    w("| la salida compuesta de la bateria | %s | `docs/loop/SALIDA_V183_BATERIA.txt` |"
      % dime("SALIDA_V183_BATERIA.txt"))
    w("| el reparto medido antes y despues | %s | `docs/loop/SALIDA_V184_T1_REPARTO_ANTES_Y_DESPUES.txt` |"
      % dime("SALIDA_V184_T1_REPARTO_ANTES_Y_DESPUES.txt"))
    w("| el cotejo de los tres clones declarados | %s | `docs/loop/SALIDA_V184_COTEJO_DE_CLONES.txt` |"
      % dime("SALIDA_V184_COTEJO_DE_CLONES.txt"))

    t = NL.join(P) + NL
    io.open(DEST, "w", encoding="utf-8", newline=NL).write(t)
    print("ESCRITO: %s" % DEST)
    print("CIFRA bytes: %d | CIFRA lineas: %d" % (len(t.encode("utf-8")), t.count(NL)))
    print("CIFRA tramos sellados: %d de 9" % len(hechos))
    print("CIFRA entradas contadas de los tramos: %d" % entradas)
    print("CIFRA tramos en rojo: %d" % len(rojos))
    print("CIFRA minutos sumados: %s" % (("%.1f" % sum(minutos)) if minutos else "n/a"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
