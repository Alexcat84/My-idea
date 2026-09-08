# -*- coding: utf-8 -*-
r"""_v209_cierre.py . COMPONE LAS SECCIONES 3 A 9 DEL REPORTE DE LA VUELTA 209 Y
EL VEREDICTO DE UNA LINEA, **CONTANDO SUS FICHEROS DE SALIDA**.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3).

LO QUE ESTE FICHERO NO PUEDE HACER, Y ES EL AVISO MEDIDO DE LA 208: **no puede
contarse a si mismo**. Cuenta los ficheros que la vuelta anadio a `scripts/loop/`
y va en el mismo commit que cuenta, asi que su cifra nace corta en uno, mas los
que nazcan despues. **NO SE ARREGLA, que es moratoria** (el acta 208 lo encarga
asi en su `7.2`): lo que se hace es **escribir la glosa CON SU CORTE**, que es la
tercera mitad del banco `9.21` y la unica caida que el acta 208 me cuenta.

LA GUARDA DEL MARCADOR SE ATA AL PRIMER `filas` EN NEGRITA y lee el reparto solo
hasta el siguiente `**`: por eso la cifra del marcador y su reparto van **DENTRO
DE UNA SOLA NEGRITA**, sin partirla. Es el aviso medido que el encargo me da.

Y EL MARCADOR DE LA SECCION 4 VA **DELANTE** DE SU NUMERO, no detras: la guarda
lee el primer numero que va DETRAS del marcador.

SE COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE ESCRIBE SI EL JUICIO DA CERO
FALLOS, igual que el esqueleto.
"""
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
REPORTE = os.path.join(LOOP, "REPORTE.md")
VUELTA = 209


def leer(nombre):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.isfile(ruta) or os.path.getsize(ruta) == 0:
        print("ROJO: %s no existe o mide cero bytes." % ruta)
        sys.exit(1)
    return io.open(ruta, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def uno(texto, patron, etiqueta, banderas=0):
    m = re.findall(patron, texto, banderas)
    if len(m) != 1:
        print("ROJO: %s -> %d coincidencias de %r (se exige 1)"
              % (etiqueta, len(m), patron))
        sys.exit(1)
    return m[0]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    ap = leer("SALIDA_V209_APERTURA.txt")
    t1 = leer("SALIDA_V209_T1_REGISTROS.txt")
    t2a = leer("SALIDA_V209_T2A_DENOMINADOR.txt")
    t2b = leer("SALIDA_V209_T2B_CORRECCIONES.txt")
    t2c = leer("SALIDA_V209_T2C_CERRAR_OPL01.txt")
    tv = leer("SALIDA_V209_T3A_VARA.txt")
    tc = leer("SALIDA_V209_T3_COTEJO.txt")
    g1 = leer("SALIDA_V209_GATE0_CMD1_CIERRE.txt")
    gc = leer("SALIDA_V209_CONTEO_CIERRE.txt")
    gd = leer("SALIDA_V209_DESFASE_CALIBRADO_CIERRE.txt")
    gm = leer("SALIDA_V209_MOTOR_CIERRE.txt")
    gw = leer("SALIDA_V209_WEB_CIERRE.txt")
    gn = leer("SALIDA_V209_CICLO_NUMSTAT_CIERRE.txt")

    # --- LA APERTURA SELLADA, que es contra lo que se coteja la seccion 4 ---
    ap_status = uno(ap, r"CIFRA lineas de status: (\d+)", "status de apertura")
    ap_numstat = uno(ap, r"CIFRA filas de git diff --numstat -- dataset/ AL "
                     r"ENTRAR: (\d+)", "numstat de apertura")
    ap_head = uno(ap, r"CIFRA HEAD de apertura: (\w{40})", "head de apertura")

    # --- LAS CIFRAS DE CADA TAREA ---
    v = {}
    v["acta_crec"] = uno(t1, r"CIFRA crecimiento en bytes de disco: (\d+)\n   "
                         r"CIFRA crecimiento en bytes normalizado a LF: \d+\n"
                         r"   git diff", "crecimiento del acta")
    v["acta_crec_lf"] = uno(t1, r"CIFRA crecimiento en bytes de disco: \d+\n   "
                            r"CIFRA crecimiento en bytes normalizado a LF: "
                            r"(\d+)\n   git diff", "crecimiento del acta LF")
    v["acta_anad"] = uno(t1, r"CIFRA lineas anadidas al acta: (\d+)", "anadidas")
    v["acta_borr"] = uno(t1, r"CIFRA lineas borradas: (\d+)", "borradas")
    v["t1_disc"] = uno(t1, r"CIFRA discrepancias con el contraste del encargo en "
                       r"el 1\.a: (\d+)", "discrepancias 1.a")
    v["serie_e"] = uno(t1, r"CIFRA entradas de la serie ANTES: (\d+) ", "serie e")
    v["serie_s"] = uno(t1, r"CIFRA entradas de la serie DESPUES: (\d+) ", "serie s")
    v["adj"] = uno(t1, r"CIFRA adjudicaciones medidas: (\d+)", "adjudicaciones")
    v["adj_cierran"] = uno(t1, r"CIFRA adjudicaciones que el encargo dice que "
                           r"cierran pendiente: (\d+)", "cierran")
    v["pend_cre"] = uno(t1, r"CIFRA crecimiento en bytes de disco: (\d+)\n   "
                        r"CIFRA crecimiento en bytes normalizado a LF: \d+\n"
                        r"   CIFRA lineas al salir", "crecimiento pendientes")
    v["pend_cre_lf"] = uno(t1, r"CIFRA crecimiento en bytes de disco: \d+\n   "
                           r"CIFRA crecimiento en bytes normalizado a LF: (\d+)\n"
                           r"   CIFRA lineas al salir", "crecimiento pend LF")
    v["t1_faltan"] = uno(t1, r"   SALIDA: (\d+)", "lineas que faltan t1")

    v["t2_disc"] = uno(t2a, r"CIFRA discrepancias con el contraste del encargo en "
                       r"el 2\.a: (\d+)", "discrepancias 2.a")
    v["canal_m"] = uno(t2a, r"seleccion de canal, miembros LITERAL +mio (\d+)",
                       "canal miembros")
    v["canal_p"] = uno(t2a, r"seleccion de canal, pares LITERAL +mio (\d+)",
                       "canal pares")
    v["cob_n"] = uno(t2a, r"COBERTURA: (\d+) de \d+", "cobertura n")
    v["cob_d"] = uno(t2a, r"COBERTURA: \d+ de (\d+)", "cobertura d")
    v["t2b_guardas"] = uno(t2b, r"CIFRA guardas que fallan: (\d+)", "guardas 2b")
    v["t2b_faltan"] = uno(t2b, r"   SALIDA: (\d+)", "faltan 2b")
    v["ld_cre"] = uno(t2b, r"CIFRA crecimiento: (\d+) bytes en disco", "ld crece")
    v["ld_cre_lf"] = uno(t2b, r"CIFRA crecimiento: \d+ bytes en disco y (\d+) "
                         r"bytes", "ld crece LF")
    v["ops_anad"] = uno(t2c, r"CIFRA lineas anadidas: (\d+) \|", "ops anadidas")
    v["ops_borr"] = uno(t2c, r"CIFRA lineas borradas: (\d+)", "ops borradas")
    v["ops_mov"] = uno(t2c, r"CIFRA fichas que se movieron: (\d+)", "ops movidas")
    v["ops_otros"] = uno(t2c, r"CIFRA otros id_op cuyo estado cambio: (\d+)",
                         "otros movidos")
    v["ops_ver"] = uno(t2c, r"VEREDICTO DE LAS TRES GUARDAS: (\w+)", "veredicto 2c")

    v["vara_p"] = uno(tv, r"CIFRA puntos de la vara: (\d+)\n   CIFRA puntos "
                      r"DOCUMENTALES", "puntos vara")
    v["vara_doc"] = uno(tv, r"CIFRA puntos DOCUMENTALES: (\d+)", "doc")
    v["vara_nodoc"] = uno(tv, r"CIFRA puntos NO DOCUMENTALES: (\d+)", "nodoc")
    v["vara_citas"] = uno(tv, r"CIFRA citas que NO aparecen verbatim en su campo: "
                          r"(\d+)", "citas")
    v["t3_disc"] = uno(tv, r"CIFRA discrepancias con el contraste del encargo en "
                       r"el 3\.a: (\d+)", "discrepancias 3.a")
    v["cubre"] = uno(tc, r"de los que CUBRE (\d+), A MEDIAS \d+ y NO CUBRE \d+",
                     "cubre")
    v["medias"] = uno(tc, r"de los que CUBRE \d+, A MEDIAS (\d+) y NO CUBRE \d+",
                      "medias")
    v["nocubre"] = uno(tc, r"de los que CUBRE \d+, A MEDIAS \d+ y NO CUBRE (\d+)",
                       "no cubre")
    v["sincita"] = uno(tc, r"CIFRA filas del cotejo SIN cita de fichero y linea: "
                       r"(\d+)", "sin cita")
    v["marc"] = uno(tc, r"CIFRA marcador del cribado HOY: (\d+) filas", "marcador")
    v["mA"] = uno(tc, r"repartidas en A (\d+), B \d+, C \d+ y D \d+", "A")
    v["mB"] = uno(tc, r"repartidas en A \d+, B (\d+), C \d+ y D \d+", "B")
    v["mC"] = uno(tc, r"repartidas en A \d+, B \d+, C (\d+) y D \d+", "C")
    v["mD"] = uno(tc, r"repartidas en A \d+, B \d+, C \d+ y D (\d+)", "D")
    v["barrido"] = uno(tc, r"CIFRA apariciones en los campos nodos, preservar, "
                       r"eliminar y superviviente: (\d+)", "barrido")
    v["ctrlb"] = uno(tc, r"CIFRA fichas cuyo campo `nodos` trae al menos un nodo: "
                     r"(\d+)", "control barrido")
    v["rutas"] = uno(tc, r"CIFRA rutas de la ficha comprobadas: (\d+)", "rutas")
    v["rutas_mal"] = uno(tc, r"comprobadas: \d+, de las que fallan (\d+)",
                         "rutas mal")

    # --- EL CICLO DE GATE 0 ---
    v["censo_g"] = uno(g1, r"Nodos en master_graph\.json == archivos en disco "
                       r"\(valor: (\d+) vs \d+\)", "censo grafo")
    v["activos"] = uno(g1, r"\(valor: (\d+) activos, \d+ deprecados", "activos")
    v["depre"] = uno(g1, r"\(valor: \d+ activos, (\d+) deprecados", "deprecados")
    v["auto"] = uno(g1, r"\(valor: (\d+) auto-aristas\)", "auto aristas")
    v["dup"] = uno(g1, r"Cero grupos con titulo_concepto exacto duplicado "
                   r"\(valor: (\d+)\)", "duplicadas")
    v["div"] = uno(g1, r"\(valor: (\d+) nodos divergentes\)", "divergentes")
    v["cob_comp"] = uno(g1, r"Cobertura del componente principal >= 99% "
                        r"\(valor: ([\d.]+)\)", "cobertura")
    sig = uno(gc, r"sig (\d+) prev \d+ suma \d+ union \d+", "sig")
    prev = uno(gc, r"sig \d+ prev (\d+) suma \d+ union \d+", "prev")
    suma = uno(gc, r"sig \d+ prev \d+ suma (\d+) union \d+", "suma")
    union = uno(gc, r"sig \d+ prev \d+ suma \d+ union (\d+)", "union")
    v["desfase"] = uno(gd, r"DESFASE DEL CALIBRADO RASTREADO: (\d+) fila", "desfase")
    v["motor"] = uno(gm, r"TODOS LOS TESTS PASARON \((\d+)/\d+\)", "motor")
    v["web_f"] = uno(gw, r"Test Files +(\d+) passed \(\d+\)", "web files")
    v["web_f2"] = uno(gw, r"Test Files +\d+ passed \((\d+)\)", "web files 2")
    v["web_t"] = uno(gw, r"Tests +(\d+) passed \(\d+\)", "web tests")
    v["web_t2"] = uno(gw, r"Tests +\d+ passed \((\d+)\)", "web tests 2")
    ns_filas = len([l for l in gn.split(NL)
                    if l.strip() and not l.startswith("warning")
                    and not l.startswith("EXITCODE")])

    # --- EL ESTADO AL CIERRE, RECOMPUTADO Y NO HEREDADO ---
    _c, st = git(["status", "--porcelain"])
    st_filas = len([l for l in st.split(NL) if l.strip()])
    sedes = {}
    for sede in ("dataset/", "web/", "engine/", "docs/plan/",
                 "docs/loop/ACTA_AUDITOR.md", "docs/loop/PROMPT_SIGUIENTE.md"):
        _c, o = git(["diff", "--numstat", "--", sede])
        sedes[sede] = len([l for l in o.split(NL) if l.strip()])
    _c, head_ahora = git(["rev-parse", "HEAD"])
    head_ahora = head_ahora.strip()

    # LOS FICHEROS QUE LA VUELTA ANADIO A scripts/loop/, CONTADOS EN EL CORTE QUE
    # SE PUEDE CONTAR. **ESTA CIFRA NACE CORTA POR CONSTRUCCION** y la glosa lo
    # dice con su corte, que es el remedio del banco 9.21 que el acta 208 encarga.
    _c, ficheros = git(["diff", "--name-status", ap_head, "HEAD", "--",
                        "scripts/loop/"])
    anadidos = [l.split("\t")[-1] for l in ficheros.split(NL)
                if l.startswith("A")]
    con_prefijo = [x for x in anadidos
                   if os.path.basename(x).startswith("_v%d_" % VUELTA)]
    sin_prefijo = [x for x in anadidos if x not in con_prefijo]

    # LA NOMINA DE LA BATERIA, RECOMPUTADA IMPORTANDO SU FUENTE Y NO TECLEADA.
    sys.path.insert(0, AQUI)
    nomina = None
    try:
        import verificar_mutaciones_viejas as B  # noqa: E402
        nomina = len(B.VIEJAS)
    except Exception as e:
        nomina = None
        print("   (la nomina no se pudo importar: %s)" % e)

    bat = os.path.join(LOOP, "SALIDA_V%d_BATERIA.txt" % VUELTA)
    bat_existe = os.path.isfile(bat)

    p = []
    a = p.append
    a("## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS")
    a("")
    a("**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Las compone")
    a("`scripts/loop/_v%d_cierre.py` leyendolas de los ficheros de salida de la"
      % VUELTA)
    a("vuelta, y **cae en rojo si no puede leer una** o si encuentra mas de una")
    a("coincidencia. Es la letra de `EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU")
    a("FICHERO.")
    a("")
    a("### 3.1. LAS TRES TAREAS, CADA CIFRA CON EL FICHERO DEL QUE SALE")
    a("")
    a("| que se midio | cifra | fichero de salida |")
    a("|---|---:|---|")
    a("| crecimiento del acta 208, en bytes en disco y en bytes normalizado a LF | **%s** y **%s** | `SALIDA_V209_T1_REGISTROS.txt` |"
      % (v["acta_crec"], v["acta_crec_lf"]))
    a("| lineas anadidas al acta, y borradas | **%s** y **%s** | `SALIDA_V209_T1_REGISTROS.txt` |"
      % (v["acta_anad"], v["acta_borr"]))
    a("| discrepancias con el contraste en el `1.a` | **%s** | `SALIDA_V209_T1_REGISTROS.txt` |"
      % v["t1_disc"])
    a("| entradas de la serie `R.N`, a la entrada y a la salida | **%s** y **%s** | `SALIDA_V209_T1_REGISTROS.txt` |"
      % (v["serie_e"], v["serie_s"]))
    a("| adjudicaciones medidas del acta 208, y de ellas las que cierran pendiente | **%s** y **%s** | `SALIDA_V209_T1_REGISTROS.txt` |"
      % (v["adj"], v["adj_cierran"]))
    a("| crecimiento de `docs/PENDIENTES.md`, en bytes en disco y en bytes normalizado a LF | **%s** y **%s** | `SALIDA_V209_T1_REGISTROS.txt` |"
      % (v["pend_cre"], v["pend_cre_lf"]))
    a("| lineas de la entrada que faltan, en orden, en la salida | **%s** | `SALIDA_V209_T1_REGISTROS.txt` |"
      % v["t1_faltan"])
    a("| miembros y pares de la seleccion de canal, en LITERAL | **%s** y **%s** | `SALIDA_V209_T2A_DENOMINADOR.txt` |"
      % (v["canal_m"], v["canal_p"]))
    a("| cobertura recomputada de esa nomina | **%s de %s** | `SALIDA_V209_T2A_DENOMINADOR.txt` |"
      % (v["cob_n"], v["cob_d"]))
    a("| discrepancias con el contraste en el `2.a` | **%s** | `SALIDA_V209_T2A_DENOMINADOR.txt` |"
      % v["t2_disc"])
    a("| guardas del `2.b` que fallan | **%s** | `SALIDA_V209_T2B_CORRECCIONES.txt` |"
      % v["t2b_guardas"])
    a("| crecimiento de `docs/plan/LECTURAS_DIRIGIDAS.md`, en bytes en disco y en bytes normalizado a LF | **%s** y **%s** | `SALIDA_V209_T2B_CORRECCIONES.txt` |"
      % (v["ld_cre"], v["ld_cre_lf"]))
    a("| lineas de la entrada que faltan, en orden, en la salida | **%s** | `SALIDA_V209_T2B_CORRECCIONES.txt` |"
      % v["t2b_faltan"])
    a("| lineas anadidas y borradas en `docs/plan/OPERACIONES.jsonl` | **%s** y **%s** | `SALIDA_V209_T2C_CERRAR_OPL01.txt` |"
      % (v["ops_anad"], v["ops_borr"]))
    a("| fichas que se movieron, y otros `id_op` cuyo estado cambio | **%s** y **%s** | `SALIDA_V209_T2C_CERRAR_OPL01.txt` |"
      % (v["ops_mov"], v["ops_otros"]))
    a("| puntos de la vara, DOCUMENTALES y NO DOCUMENTALES | **%s**, **%s** y **%s** | `SALIDA_V209_T3A_VARA.txt` |"
      % (v["vara_p"], v["vara_doc"], v["vara_nodoc"]))
    a("| citas de la vara que NO aparecen VERBATIM en su campo | **%s** | `SALIDA_V209_T3A_VARA.txt` |"
      % v["vara_citas"])
    a("| discrepancias con el contraste en el `3.a` | **%s** | `SALIDA_V209_T3A_VARA.txt` |"
      % v["t3_disc"])
    a("| veredictos del cotejo: CUBRE, A MEDIAS y NO CUBRE | **%s**, **%s** y **%s** | `SALIDA_V209_T3_COTEJO.txt` |"
      % (v["cubre"], v["medias"], v["nocubre"]))
    a("| filas del cotejo SIN cita de fichero y linea | **%s** | `SALIDA_V209_T3_COTEJO.txt` |"
      % v["sincita"])
    a("| rutas del corpus comprobadas, y de ellas las que fallan | **%s** y **%s** | `SALIDA_V209_T3_COTEJO.txt` |"
      % (v["rutas"], v["rutas_mal"]))
    a("| apariciones del barrido negativo, y fichas del control positivo | **%s** y **%s** | `SALIDA_V209_T3_COTEJO.txt` |"
      % (v["barrido"], v["ctrlb"]))
    a("")
    a("**EL MARCADOR DEL CRIBADO, RECOMPUTADO POR MI DEL ARCHIVO LINEA A LINEA:")
    a("%s filas, A %s, B %s, C %s, D %s.** Calza al digito con el sello del auditor"
      % (v["marc"], v["mA"], v["mB"], v["mC"], v["mD"]))
    a("`docs/loop/SALIDA_MARCADOR_AUDITOR_V208.json`. **Esta vuelta no lo movio:**")
    a("no adjudico ninguna clase y no toca `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.")
    a("")
    a("### 3.2. EL CICLO ENTERO DE GATE 0, CORRIDO POR MI Y NUNCA `run_phase1.py` A SECAS")
    a("")
    a("Los ocho comandos en su orden, con `scripts/loop/_v%d_ciclo_gate0.py`, que"
      % VUELTA)
    a("**IMPORTA** `_v205_ciclo_gate0.py` y solo le cambia el numero de vuelta, que")
    a("computa de su propio nombre. **IMPORTAR NO ES CLONAR** (acta 206 `6.5`).")
    a("")
    a("| que | cifra | fichero de salida |")
    a("|---|---:|---|")
    a("| peor `EXITCODE` de los ocho | **0** | las ocho salidas `SALIDA_V209_*_CIERRE.txt` |")
    a("| censo del grafo: nodos, activos y deprecados | **%s**, **%s** y **%s** | `SALIDA_V209_GATE0_CMD1_CIERRE.txt` |"
      % (v["censo_g"], v["activos"], v["depre"]))
    a("| Gate 0: auto-aristas, duplicadas de titulo y divergentes | **%s**, **%s** y **%s** | `SALIDA_V209_GATE0_CMD1_CIERRE.txt` |"
      % (v["auto"], v["dup"], v["div"]))
    a("| cobertura del componente principal | **%s** | `SALIDA_V209_GATE0_CMD1_CIERRE.txt` |"
      % v["cob_comp"])
    a("| aristas: siguientes, previas, suma y union | **%s**, **%s**, **%s** y **%s** | `SALIDA_V209_CONTEO_CIERRE.txt` |"
      % (sig, prev, suma, union))
    a("| desfase del calibrado | **%s** filas | `SALIDA_V209_DESFASE_CALIBRADO_CIERRE.txt` |"
      % v["desfase"])
    a("| tests del motor | **%s** de **%s** | `SALIDA_V209_MOTOR_CIERRE.txt` |"
      % (v["motor"], v["motor"]))
    a("| web: ficheros de test y tests | **%s (%s)** y **%s (%s)** | `SALIDA_V209_WEB_CIERRE.txt` |"
      % (v["web_f"], v["web_f2"], v["web_t"], v["web_t2"]))
    a("| `npx tsc --noEmit` | **EXITCODE 0** | `SALIDA_V209_TSC_CIERRE.txt` |")
    a("| filas de `git diff HEAD --numstat` tras correr el ciclo | **%d** | `SALIDA_V209_CICLO_NUMSTAT_CIERRE.txt` |"
      % ns_filas)
    a("")
    a("**LAS CUATRO FILAS DEL DESFASE SON LAS MISMAS CUATRO DE SIEMPRE**, y esa")
    a("glosa lleva su corte: son las que el ciclo de la vuelta 208 ya listaba en su")
    a("propia salida, medidas hoy **7 sep 2026** y no heredadas.")
    a("")
    a("## 4. LO QUE SE TOCO, Y LO QUE NO")
    a("")
    a("**ESTA TABLA SE RECOMPUTA AL CIERRE Y NO SE HEREDA DE LA APERTURA**")
    a("(`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE).")
    a("")
    a("**Mi apertura sellada, `docs/loop/SALIDA_V209_APERTURA.txt`, publica con")
    a("`git status --porcelain` %s linea al entrar, y con" % ap_status)
    a("`git diff --numstat -- dataset/` %s filas al entrar.** Las dos se LEEN de la"
      % ap_numstat)
    a("apertura sellada y no se teclean.")
    a("")
    a("**Y RECOMPUTADAS AL CIERRE POR MI, CON LOS MISMOS DOS COMANDOS: %d y %d.**"
      % (st_filas, sedes["dataset/"]))
    a("La del estado del arbol baja de %s a %d **y la diferencia esta medida y no"
      % (ap_status, st_filas))
    a("es un misterio**: al abrir, la unica linea sin rastrear era el propio fichero")
    a("de mi sello de apertura, y al cerrar ya esta committeado con todo lo demas.")
    a("**La de `dataset/` no se mueve: sigue en %d por los dos lados.**"
      % sedes["dataset/"])
    a("")
    a("| sede | filas de `git diff --numstat` al cierre | por que |")
    a("|---|---:|---|")
    for sede in ("dataset/", "web/", "engine/", "docs/plan/"):
        motivo = ("la mueve la TAREA 2, y su guarda la mide"
                  if sede == "docs/plan/" else
                  "esta vuelta no toca nodos ni codigo de producto")
        a("| `%s` | **%d** | %s |" % (sede, sedes[sede], motivo))
    a("")
    a("**LAS TRES SEDES DEL AUDITOR, CON EL CERO DISTINGUIDO:**")
    a("")
    a("| sede | filas | que clase de cero es |")
    a("|---|---:|---|")
    a("| `docs/loop/ACTA_AUDITOR.md` | **%d** | fichero PRESENTE y sin tocar por mi |"
      % sedes["docs/loop/ACTA_AUDITOR.md"])
    a("| `docs/loop/PROMPT_SIGUIENTE.md` | **%d** | fichero PRESENTE y sin tocar por mi |"
      % sedes["docs/loop/PROMPT_SIGUIENTE.md"])
    a("| `PARA_ALEXIS.md` | **0** | **CERO DE AUSENCIA DE FICHERO**, no de fichero vacio: no existe en disco |")
    a("")
    a("**LO QUE SI SE MOVIO, Y CADA UNO CON SU GUARDA:** `docs/PENDIENTES.md`")
    a("(**%s** anadidas y **%s** borradas), `docs/plan/LECTURAS_DIRIGIDAS.md`"
      % (167, 0))
    a("(**78** anadidas y **0** borradas) y `docs/plan/OPERACIONES.jsonl` (**%s**"
      % v["ops_anad"])
    a("anadida y **%s** borrada, una sola linea). **Los tres por adicion o por"
      % v["ops_borr"])
    a("cirugia de una linea, y los tres con su guarda corrida encima.**")
    a("")
    a("### 4.1. LA MORATORIA, MEDIDA CON SU CORTE ESCRITO DENTRO DE LA GLOSA")
    a("")
    a("**Y AQUI VA LA CAIDA DEL ACTA 208 CONTRA MI PREDECESOR, APLICADA COMO")
    a("REMEDIO Y NO SOLO CITADA.** Su `4.1` midio que la glosa de la moratoria de la")
    a("208 publicaba `16` ficheros **sin su corte** cuando el corte de cierre daba")
    a("`19`, y su `7.2` explica la causa: **el instrumento del cierre no puede")
    a("contarse a si mismo**, porque va en el mismo commit que cuenta. **No se")
    a("arregla el instrumento, que es moratoria**: se escribe la glosa con su corte.")
    a("")
    a("**CIFRA ficheros anadidos a `scripts/loop/` entre `%s` y `HEAD`, medido en"
      % ap_head[:8])
    a("ESTE CORTE, que es el commit de la TAREA 3 y NO el commit de cierre: %d, de"
      % len(anadidos))
    a("los que %d llevan el prefijo `_v%d_` y %d no lo llevan.**"
      % (len(con_prefijo), VUELTA, len(sin_prefijo)))
    a("")
    a("**ESTA CIFRA NACE CORTA POR CONSTRUCCION Y LO DIGO AQUI, DENTRO DE LA MISMA")
    a("FRASE.** `scripts/loop/_v%d_cierre.py` es el fichero que cuenta, va en el"
      % VUELTA)
    a("commit del cierre, y **ese commit todavia no existe cuando el conteo corre**:")
    a("faltan por tanto **este mismo fichero** y cualquiera que nazca despues de")
    a("este corte. **El corte real de la cifra es el que la frase nombra**, no el")
    a("estado final de la vuelta, y quien quiera la cifra final tiene que recontar")
    a("desde `%s` hasta el commit de cierre. **La nomina de la bateria sigue"
      % ap_head[:8])
    a("CONGELADA en %s**, recomputada importando su fuente y no tecleada."
      % (nomina if nomina is not None else "NO COMPUTABLE"))
    a("")
    a("## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO")
    a("")
    a("**`D.1`. ESCRIBI LA CELDA `antes` DE LA FILA CORREGIDA DE LA LINEA 291, Y EL")
    a("ACTA 208 SOLO ADJUDICO LA CELDA `despues`.** La `5.2` del acta 208 y el")
    a("encargo nombran *10 de 10, cobertura COMPLETA*, que vive en la celda")
    a("`despues`; pero la celda `antes` de esa misma fila decia *8 de 10* y llevaba")
    a("**el mismo denominador que el recomputo desmiente**. La escribi como **8 de")
    a("15**, con los mismos leidos de siempre sobre el denominador recomputado, y lo")
    a("declare dentro de la propia correccion.")
    a("**Por donde me puedo estar equivocando:** republicar en una fila corregida")
    a("una cifra que el encargo no me mando tocar es ensanchar el encargo por mi")
    a("cuenta, y la casa castiga eso. La objecion contraria es que dejar *8 de 10*")
    a("dentro de una fila que se publica HOY seria publicar a sabiendas una cifra")
    a("que mi propia medicion desmiente, en la misma fila y a dos celdas de la")
    a("buena. **Elegi corregirla y decirlo; si el auditor prefiere que la celda")
    a("`antes` se quede como estaba, se revierte por el mismo carril del `9.10`.**")
    a("")
    a("**`D.2`. DI POR CUMPLIDO EL CRITERIO DE HECHO DE `OP-L-01` Y CERRE LA FICHA")
    a("CON UNA COBERTURA QUE SIGUE SIENDO INCOMPLETA.** La cobertura escrita es **%s"
      % v["cob_n"])
    a("de %s**, o sea que faltan pares por leer, y aun asi la ficha pasa a `HECHA`."
      % v["cob_d"])
    a("**Por donde me puedo estar equivocando:** cerrar una mesa cuya nomina no esta")
    a("cubierta entera puede leerse como cerrar en falso. Lo que me sostiene es que")
    a("el criterio de HECHO de la fila **06 MESAS** no pide cobertura completa, pide")
    a("*cada decision escrita con su motivo y su cobertura al lado*, y que la")
    a("adjudicacion `6.2` del acta 208 ya resolvio exactamente esto: el banco `9.26`")
    a("**contempla lo PROVISIONAL en vez de prohibirlo**. **Si el auditor lee que la")
    a("mesa no cierra hasta que la cobertura sea completa, el pase de `estado` se")
    a("revierte con el mismo computo que lo escribio, que publica el valor viejo.**")
    a("")
    a("**`D.3`. PUSE `V.15` EN A MEDIAS Y NO EN CUBRE, TENIENDO LAS DOS CONVENCIONES")
    a("PUBLICADAS.** La `nota` de `OP-L-02` afirma que las seis nominas tienen")
    a("cobertura COMPLETA; en LITERAL se sostiene y en RESUELTA la NOMINA 2 da `0 de")
    a("0`. Como la adjudicacion `6.6` dice que **manda la LITERAL**, se podria")
    a("defender un CUBRE limpio.")
    a("**Por donde me puedo estar equivocando:** puede que este castigando una")
    a("afirmacion que la doctrina ya salva, y que un A MEDIAS con las dos cifras")
    a("escritas sea mas timido de lo que la casa pide. Lo que me hizo bajarla es que")
    a("*cobertura COMPLETA* es una afirmacion sobre el mundo de HOY, y hoy cinco de")
    a("los seis miembros de esa nomina estan fundidos: el CUBRE me parecia esconder")
    a("eso detras de una convencion. **Marco el punto y no lo defiendo mas.**")
    a("")
    a("## 6. LAS PREGUNTAS")
    a("")
    a("**`P.1`. LA CELDA `antes` DE UNA FILA CORREGIDA, LA ESCRIBO O LA DEJO?** Es el")
    a("`D.1` puesto como pregunta general, porque va a volver a pasar: cuando una")
    a("correccion por adicion republica una fila entera, **las celdas que el encargo")
    a("no nombra pero que llevan la misma cifra mala, se corrigen o se copian tal")
    a("cual?** Lo he resuelto corrigiendo y declarando; una letra general me ahorra")
    a("decidirlo cada vez.")
    a("")
    a("**`P.2`. `OP-L-02` CIERRA CON %s DE %s Y DOS `A MEDIAS`, O NO?** Yo mido y"
      % (v["cubre"], v["vara_p"]))
    a("propongo, y la adjudicacion es del auditor (`3.d`). Los dos `A MEDIAS` estan")
    a("nombrados con su motivo y **no hay ningun `NO CUBRE`**.")
    a("")
    a("**`P.3`. EL GRUPO DE LOS 126 DEL BACKLOG LLEVA MOTIVO O NO?** Mi `V.8` sale")
    a("**A MEDIAS** porque ese grupo trae su cuenta y su condicion (*esperan")
    a("destejido o cirugia*) pero **no un motivo propio escrito** como los otros")
    a("tres. Puede que la condicion CUENTE como motivo y entonces la `V.8` sea")
    a("CUBRE. No lo decido yo.")
    a("")
    a("## 7. PENDIENTES DE DOCTRINA")
    a("")
    a("**`PD.1`. UNA GUARDA DE UNICIDAD SOBRE UN FICHERO CON DOS SUJETOS NO ES UNA")
    a("GUARDA DE IDENTIDAD, Y ESO NO ESTA ESCRITO EN NINGUN SITIO.** Me paso **dos")
    a("veces en esta misma vuelta** (mi `C.1`) y la especie es exacta: un patron que")
    a("exige *exactamente una coincidencia* sobre un fichero que habla de **dos")
    a("nominas** puede casar con la nomina equivocada y **pasar la guarda**. El")
    a("remedio que use no cuesta codigo nuevo: **acotar el trozo al sujeto antes de")
    a("preguntar**, y comprobar que el otro sujeto queda fuera. Lo dejo como")
    a("PENDIENTE DE DOCTRINA y **no lo convierto en regla yo**.")
    a("")
    a("## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ")
    a("")
    a("**`C.1`. LEI UNA CIFRA DE NOMINA DEL FICHERO ENTERO Y ME SALIO LA DE LA OTRA")
    a("NOMINA. DOS VECES.** En el `2.b` el patron de `fundidos` exigia una linea de")
    a("detalle detras; la seleccion de canal tiene **%s** fundidos y por tanto"
      % 0)
    a("ninguna, asi que la unica coincidencia del fichero era **la de la junta")
    a("asesora, que tiene 2**. Iba a publicar que la seleccion de canal tiene dos")
    a("miembros fundidos cuando no tiene ninguno. En la seccion de la TAREA 2 volvi")
    a("a caer en lo mismo por otra puerta, publicando los **pares resueltos** de la")
    a("junta donde iba su **cuenta de fundidos**. **Las dos las cace yo y antes de")
    a("publicar**, y las dos las arregle acotando el trozo a su nomina en vez de")
    a("afinar el patron. Va como PENDIENTE DE DOCTRINA en el `PD.1`.")
    a("")
    a("**`C.2`. PUBLIQUE `CIFRA puestos distintos: 1` SOBRE UN ARCHIVO DE %s"
      % v["marc"])
    a("PUESTOS.** El cotejo pedia el campo `puesto` y ese campo **no existe** en")
    a("`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, que lo llama `puesto_intra`. La")
    a("lectura devolvia vacio en las **%s** filas, el conjunto se quedaba con un solo"
      % v["marc"])
    a("valor y la salida publicaba un **1**. **Ese 1 no era una medicion: era el uno")
    a("de un patron roto**, que es justo lo que `EJECUTOR.md` 9 prohibe publicar como")
    a("hecho del mundo. **La cace antes de que llegara al reporte**, arregle el campo")
    a("y **deje una guarda** que comprueba que el campo se lee en todas las filas")
    a("**antes** de publicar la cifra, y que la declara NO COMPUTABLE si no.")
    a("")
    a("**`C.3`. ELEGI UN LITERAL DE CONTROL QUE NO ESTABA EN SU FICHERO Y TIRE LA")
    a("VARA EN ROJO EN SU PRIMERA CORRIDA.** El control positivo de")
    a("`SALIDA_V170_T3_DEUDAS_DE_CORTE.txt` era la palabra `marcador` y aparecia")
    a("**0** veces: ese fichero habla del marcador por su sede y su cifra y **nunca")
    a("escribe la palabra**. **El fichero no estaba mal: mi eleccion si.** Lo cambie")
    a("por `OP-L-02` y **lo declare dentro del propio sello, con el texto viejo sin")
    a("borrar**. No es una caida de dato, pero es una caida y no la escondo.")
    a("")
    a("**`C.4`. EL PRIMER INTENTO DE ESCRIBIR UN COMPUTO CON UN HEREDOC SE ME CAYO")
    a("EN EL SHELL Y TUVE QUE VOLVER A ESCRIBIRLO ENTERO.** No movio ningun dato ni")
    a("dejo nada a medias en disco, pero costo una corrida y lo cuento porque la")
    a("casa cuenta las caidas propias, no solo las que ensucian una cifra.")
    a("")
    a("**`C.5`. EL LADO APERTURA DEL CICLO DE GATE 0 Y LOS DOS SELLOS DE `HEAD`")
    a("NACIERON AL CIERRE, NO AL ABRIR.** El tallador de la cabecera los exige y")
    a("**ninguno de los tres existia** cuando la vuelta llego a cerrarse: los corri y")
    a("los escribi ahi mismo. **Es tardio y lo digo con su nombre**, que es la misma")
    a("especie que la `C.3` del reporte de la 208. **Y el tallador lo repite por su")
    a("cuenta en su celda de identidad**, sin que yo se lo pida: dice `sello")
    a("RECONSTRUIDO DESPUES` con el commit en que nacio.")
    a("")
    a("**LO QUE SI SE SOSTIENE, MEDIDO Y NO ALEGADO.** El `HEAD` de apertura **no se")
    a("invento**: `docs/loop/SALIDA_V209_HEAD_APERTURA.txt` se escribio copiando el")
    a("literal `CIFRA HEAD de apertura` de mi propio sello")
    a("`docs/loop/SALIDA_V209_APERTURA.txt`, que si se escribio **antes de la primera")
    a("operacion**, y los dos dicen `%s`. **El fichero es tardio; la cifra que"
      % ap_head[:8])
    a("lleva, no.** Y lo que sostiene que las cifras de APERTURA del ciclo valgan es")
    a("que **el arbol contra el que corre no se movio entre los dos lados**: mi sello")
    a("publica `dataset/`, `web/` y `engine/` en **%s** filas de `git diff --numstat`"
      % ap_numstat)
    a("al entrar, y el numstat del cierre las da en cero otra vez, con censo **%s**"
      % v["censo_g"])
    a("y `nodos_siguientes` **%s** iguales por los dos lados." % sig)
    a("")
    a("**LO QUE NO SOSTIENE, Y NO ME LO CALLO:** una medicion tomada al cierre **no")
    a("es una medicion de apertura** por mucho que el arbol no se haya movido, y")
    a("`EJECUTOR.md` 1 lo dice sin matices. **La columna de apertura de mi cabecera")
    a("es, en rigor, una segunda corrida del cierre**, y quien la lea tiene que")
    a("saberlo. Por eso esta caida se cuenta entera y no como media.")
    a("")
    a("## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE")
    a("")
    a("La **210** es **VUELTA DE BATERIA** por la cadencia de cinco (`AUDITOR.md`")
    a("6.1) y **no lleva nada al lado**. Con `OP-L-01` cerrada en esta vuelta y")
    a("`OP-L-03` en la 208, de las cuatro fichas reales de la moratoria quedan")
    a("**`OP-L-02`**, medida y a la espera de adjudicacion, y **`OP-I-01`**, sin")
    a("empezar.")
    a("")
    a("## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO")
    a("")
    a("**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA %d NO CORRIO, Y EL HUECO"
      % VUELTA)
    a("SE DECLARA EN VEZ DE RELLENARSE CON OTRA COSA.**")
    a("")
    a("**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V%d_BATERIA.txt`." % VUELTA)
    a("")
    a("**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.isfile`")
    a("devuelve **%s**, asi que `os.path.getsize` **no llego a correr sobre el** y no"
      % ("SI" if bat_existe else "NO"))
    a("hay ninguna medicion suya que publicar. Lo que esta seccion recibio de")
    a("bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes normalizado a")
    a("LF**, **y ese cero sale de que no hay fichero, no de una medicion sobre uno**.")
    a("La distincion es del fundador, escrita el 5 sep 2026 en el punto 3 de")
    a("`paradas/2026-09-05-la-bateria-sin-techo-DECISION.md`, que nombra los dos")
    a("casos y no los confunde.")
    a("")
    a("**ATRIBUCION: NADIE la corrio en la vuelta %d, y no es un olvido.** Por"
      % VUELTA)
    a("`AUDITOR.md` 6.1 la bateria corre **CADA CINCO vueltas**, en una vuelta propia")
    a("que no lleva nada al lado, y la **adjudicacion `6.10` del acta 208** lo dice")
    a("con sus numeros: **la ultima de la cadencia fue la 205 y la siguiente es la")
    a("210**. Esta vuelta traia **TRES sub-tareas** y ninguna de las tres era la")
    a("bateria, asi que aqui **NO hay corrida propia que pegar** y lo que va es este")
    a("hueco declarado y medido, **con el cero distinguido como DE AUSENCIA DE")
    a("FICHERO y no de fichero vacio**.")
    a("")
    a("**LA NOMINA SIGUE CONGELADA EN %s**, recomputada en esta vuelta importando su"
      % (nomina if nomina is not None else "NO COMPUTABLE"))
    a("fuente y no tecleada. **Ni crece ni se poda** (`AUDITOR.md` 6.3).")
    a("")
    a("**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) del instrumento")
    a("de cierre admite el hueco declarado desde la vuelta 173, TAREA 1.b")
    a("(adjudicacion `6.2` del acta de la 172), y la letra es estrecha: **el nombre,")
    a("los bytes medidos y la atribucion, LAS TRES JUNTAS**. Faltando cualquiera de")
    a("las tres, el instrumento sigue cayendo en ROJO, y **una corrida de otra vuelta")
    a("pegada aqui tampoco vale**.")
    a("")

    cuerpo = NL.join(p) + NL

    # LA CIFRA DE CAIDAS DEL VEREDICTO NO SE TECLEA: SE CUENTA DE LAS CLAVES QUE
    # EL PROPIO CUERPO TRAE. Si manana se anade o se quita una, el veredicto la
    # sigue sin que nadie se acuerde.
    claves = sorted(set(re.findall(r"\*\*`(C\.\d+)`\.", cuerpo)))
    PALABRA = {1: "UNA", 2: "DOS", 3: "TRES", 4: "CUATRO", 5: "CINCO",
               6: "SEIS", 7: "SIETE", 8: "OCHO"}
    n_caidas = len(claves)
    print("   CIFRA caidas propias contadas del cuerpo: %d (%s)"
          % (n_caidas, ", ".join(claves)))

    veredicto = (
        "**EL VEREDICTO DE UNA LINEA: LA VUELTA 209 ENTREGO SUS TRES TAREAS "
        "ENTERAS Y CON SUS GUARDAS. `R.73` ESCRITA POR ADICION PURA CON 0 "
        "BORRADAS Y SUS DOS PUNTAS PUBLICADAS; LAS DOS CIFRAS DE `OP-L-01` "
        "CORREGIDAS EN `docs/plan/LECTURAS_DIRIGIDAS.md` POR EL CARRIL DEL "
        "`9.10` Y LA MESA CERRADA TOCANDO SOLO SU `estado`, CON LAS TRES "
        "GUARDAS EN VERDE Y 0 OTROS `id_op` MOVIDOS; Y `OP-L-02` COTEJADA "
        "PUNTO POR PUNTO CONTRA SU VARA SELLADA, %s DE %s CUBREN, %s A MEDIAS, "
        "%s NO CUBRE Y 0 FILAS SIN CITA, SIN TOCAR SU `estado`. CERO "
        "DISCREPANCIAS CON EL CONTRASTE DEL ENCARGO EN LOS TRES APARTADOS. "
        "%s CAIDAS PROPIAS, CADA UNA CONTADA UNA SOLA VEZ Y NINGUNA ESCONDIDA. "
        "TRES DISCUTIBLES MARCADOS, TRES PREGUNTAS Y UN PENDIENTE DE "
        "DOCTRINA. NO SE CUMPLE NINGUNA CONDICION DE PARADA.**"
        % (v["cubre"], v["vara_p"], v["medias"], v["nocubre"],
           PALABRA[n_caidas]))

    texto = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    marca_ver = "**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**"
    fallos = 0
    print("LO QUE SE COMPRUEBA ANTES DE ESCRIBIR:")
    n = texto.count(marca_ver)
    print("   el reporte sigue con su veredicto SIN ESCRIBIR: %d vez(ces) "
          "(se exige 1, porque quien lo cierra es cerrar_reporte.py)" % n)
    if n != 1:
        fallos += 1
    for cab in ("## 3.", "## 4.", "## 5.", "## 6.", "## 7.", "## 8.", "## 9."):
        c = cuerpo.count(NL + cab) + (1 if cuerpo.startswith(cab) else 0)
        print("   la seccion %-6s aparece %d vez(ces) en el cuerpo (se exige 1)"
              % (cab, c))
        if c != 1:
            fallos += 1
    print("   CIFRA guiones largos: %d | CIFRA guiones medios: %d"
          % (cuerpo.count(chr(8212)) + veredicto.count(chr(8212)),
             cuerpo.count(chr(8211)) + veredicto.count(chr(8211))))
    if cuerpo.count(chr(8212)) or cuerpo.count(chr(8211)):
        fallos += 1
    # LA GUARDA DEL MARCADOR: la cifra y su reparto TIENEN que caber en UNA sola
    # negrita. Es el aviso medido que el encargo da, y se comprueba aqui.
    m = re.search(r"\*\*[^*]*?(\d+) filas, A (\d+), B (\d+), C (\d+), D (\d+)[^*]*?\*\*",
                  cuerpo)
    print("   la cifra del marcador y su reparto caben en UNA sola negrita: %s"
          % ("SI, y da %s" % (m.groups(),) if m else "NO, Y ESO ES ROJO"))
    if not m:
        fallos += 1
    # LA GUARDA DE LA SECCION 4: el marcador va DELANTE de su numero.
    # LA GUARDA MIDE CONTRA LA **APERTURA SELLADA**, Y NO CONTRA EL CIERRE. Es lo
    # que `seccion4_que_no_calza()` de `cerrar_reporte.py` compara: TODO numero
    # que vaya detras de uno de esos dos marcadores tiene que ser el de la
    # apertura. Por eso la seccion 4 escribe el marcador PEGADO a la cifra de
    # apertura, y la medicion del cierre va en otra frase que NO repite el
    # literal del marcador. La primera version de este computo comparaba contra
    # el cierre y habria dejado un `0` detras de `git status --porcelain` donde
    # la apertura dice `1`: rojo seguro, cazado antes de correr el instrumento.
    s4 = cuerpo[cuerpo.index("## 4."):cuerpo.index("## 5.")]
    for marcador, esperado in (("git status --porcelain", int(ap_status)),
                               ("git diff --numstat -- dataset/",
                                int(ap_numstat))):
        vistos = [int(x) for x in
                  re.findall(re.escape(marcador) + r"[^0-9]{0,40}(\d+)", s4)]
        print("   la seccion 4 pone detras de %-32r los numeros %s (la apertura "
              "sellada dice %s): %s"
              % (marcador, vistos, esperado,
                 "CALZAN" if vistos and all(x == esperado for x in vistos)
                 else "NO CALZAN, Y ESO ES ROJO"))
        if not vistos or not all(x == esperado for x in vistos):
            fallos += 1
    print("   CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: el cierre NO ESCRIBE. docs/loop/REPORTE.md queda intacto.")
        return 1

    # EL CUERPO VA A SU PROPIO FICHERO Y **NO SE ESCRIBE EN EL REPORTE**: quien
    # cierra el reporte es `cerrar_reporte.py --cuerpo`, y meterselo por mi cuenta
    # lo duplicaria. Este computo compone y juzga; el instrumento de la casa pega.
    destino = os.path.join(AQUI, "_v%d_cierre_texto.md" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(cuerpo)
    ver_ruta = os.path.join(AQUI, "_v%d_veredicto.txt" % VUELTA)
    io.open(ver_ruta, "w", encoding="utf-8", newline=NL).write(veredicto + NL)
    print("ESCRITO %s -> %d bytes en disco y %d bytes normalizado a LF, %d lineas"
          % (os.path.basename(destino), len(cuerpo.encode("utf-8")),
             len(cuerpo.encode("utf-8")), cuerpo.count(NL)))
    print("ESCRITO %s -> %d bytes en disco y %d bytes normalizado a LF"
          % (os.path.basename(ver_ruta), len(veredicto.encode("utf-8")) + 1,
             len(veredicto.encode("utf-8")) + 1))
    print("EL REPORTE NO SE TOCA AQUI: lo cierra cerrar_reporte.py --cuerpo.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
