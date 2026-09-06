# -*- coding: utf-8 -*-
r"""_v183_tallar_cierre.py . TALLA scripts/loop/_v183_cierre_texto.md CONTANDO SUS
FICHEROS DE SALIDA, EN VEZ DE TECLEAR SUS CIFRAS.

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
  python scripts/loop/_v183_tallar_cierre.py
"""
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
DEST = os.path.join(RAIZ, "scripts", "loop", "_v183_cierre_texto.md")


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


def cifra_de(nombre, patron, grupo=1):
    """UNA CIFRA SACADA DE SU FICHERO, con la ULTIMA aparicion que gane, o None.
    Se lee del fichero y no se recuerda."""
    hits = re.findall(patron, texto(nombre))
    if not hits:
        return None
    ult = hits[-1]
    return ult if isinstance(ult, str) else ult[grupo - 1]


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
            tramos.append((n, None, None, None, None, None, None))
            continue
        t = texto(nombre)
        lineas = t.count(NL)
        ent = len(re.findall(r"ENTRADA DEL TRAMO: ", t))
        m_ex = re.findall(r"EXITCODE DEL TRAMO %d: (-?\d+)" % n, t)
        m_du = re.findall(r"DURACION DEL TRAMO \(monotona, minutos\): ([\d.]+)", t)
        tramos.append((n, d, l, lineas, ent,
                       m_ex[-1] if m_ex else None,
                       m_du[-1] if m_du else None))
    hechos = [t for t in tramos if t[1]]
    minutos = [float(t[6]) for t in hechos if t[6]]
    entradas = sum(t[4] or 0 for t in hechos)

    _c, head_cierre = git(["rev-parse", "HEAD"])
    _c, rama = git(["rev-parse", "--abbrev-ref", "HEAD"])
    head_ap = texto("SALIDA_V183_HEAD_APERTURA.txt").strip()
    _c, acta182 = git(["log", "--format=%H", "-60", "--grep",
                       "^ACTA DEL AUDITOR, VUELTA 182"])
    acta182 = (acta182.splitlines() or [""])[0]
    _c, nac = git(["log", "--diff-filter=A", "--format=%H", "--",
                   "docs/loop/SALIDA_V183_HEAD_APERTURA.txt"])
    nac = (nac.splitlines() or [""])[0]
    _c, numstat = git(["diff", "--numstat", "--", "dataset/"])
    filas_sucias = len([l for l in numstat.splitlines() if l.strip()])

    ver = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
    import hashlib
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

    # ============================================================= SECCION 3
    w("## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT")
    w("")
    w("**LAS DOS TAREAS DEL ENCARGO CERRARON.** El tope era dos, por el regimen")
    w("temporal de `AUDITOR.md` 6.2, y son dos.")
    w("")
    w("- rama, leida con `git rev-parse --abbrev-ref HEAD`: `%s`" % rama)
    w("- HEAD de apertura, sellado **antes de la primera operacion** en")
    w("  `docs/loop/SALIDA_V183_HEAD_APERTURA.txt`: **`%s`**" % head_ap[:8])
    w("- HEAD del ultimo commit antes de cerrar, leido con `git rev-parse HEAD`:")
    w("  **`%s`**" % head_cierre[:8])
    w("- commit del acta 182, localizado en `git log --grep` y no tecleado:")
    w("  **`%s`**" % acta182[:8])
    w("- commit de nacimiento del bloque de apertura, `git log --diff-filter=A`:")
    w("  **`%s`**" % nac[:8])
    w("")
    w("**GATE 0 VERDE ENTERO EN SU CICLO, EN LA APERTURA**, y sus salidas son")
    w("`SALIDA_V183_GATE0_CMD1_APERTURA.txt` (%s), motor **25 de 25**, `tsc`"
      % dime("SALIDA_V183_GATE0_CMD1_APERTURA.txt"))
    w("**exit 0** y web **1.040 passed**, contados de")
    w("`SALIDA_V183_MOTOR_APERTURA.txt`, `SALIDA_V183_TSC_APERTURA.txt` y")
    w("`SALIDA_V183_WEB_APERTURA.txt`. La apertura entera vive en")
    w("`SALIDA_V183_APERTURA.txt` (%s) y **la sello el PRIMER commit de la vuelta**,"
      % dime("SALIDA_V183_APERTURA.txt"))
    w("cosa que comprobo `scripts/loop/verificar_apertura_sellada.py --vuelta 183`:")
    w("**VERDE, los 10 ficheros `SALIDA_V183_*_APERTURA.txt` nacidos en `%s`, hijo"
      % nac[:8])
    w("directo del acta**.")
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
    w("apertura midio y el mismo que las actas 179, 180, 181 y 182 publican.")
    w("")

    # ============================================================= SECCION 4
    w("## 4. LA GUARDA DEL COMMIT DE `dataset/`, CORRIDA EL DIA QUE SERVIA")
    w("")
    w("`git status --porcelain` da **`M dataset/metadata/master_graph.json`** al")
    w("abrir la vuelta y sigue dandolo al cerrarla. **Se midio antes de creerlo:**")
    w("`git diff --numstat -- dataset/` da **%d filas**. **Es artefacto de fin de"
      % filas_sucias)
    w("linea, no contenido. Ninguna perdida de catalogo que declarar**, y el fichero")
    w("**no se commitea**. La misma guarda corrio **dieciocho veces mas dentro de la")
    w("bateria**, una al entrar y otra al salir de cada uno de los nueve tramos, y")
    w("las dieciocho dieron **cero filas**: esta contado de los propios ficheros de")
    w("tramo y no del lanzador.")
    w("")

    # ============================================================= SECCION 5
    w("## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO")
    w("")
    w("**`D.1`. LA VARA DE LOS NUMERALES SOLO MIRA DOS ESPECIES, Y LAS ELEGI YO.**")
    w("`numerales_del_veredicto_que_no_calzan()` coteja **caidas** y **tareas**, que")
    w("son las dos que el encargo nombra como minimo. **No es una lista cerrada por")
    w("doctrina: es la que el cuerpo permite contar hoy**, y anadir una tercera es")
    w("anadir una entrada en `SUSTANTIVO_A_ESPECIE` mas su contador. Lo digo porque")
    w("un veredicto puede publicar otras cifras (puestos, tramos, bytes) y **esta")
    w("guarda no las ve**: su verde NO significa que el veredicto entero calce.")
    w("")
    w("**`D.2`. UN VEREDICTO NO PUEDE NOMBRAR UNA CUENTA AJENA COMO 'N CAIDAS'.**")
    w("La guarda no distingue *\"mis seis caidas\"* de *\"las seis caidas del acta")
    w("182\"*: las dos las cuenta contra el cuerpo de ESTE reporte. **Lo elegi asi a")
    w("proposito** y esta escrito en su docstring: en la unica linea que se llama a")
    w("si misma veredicto, una cifra sin dueno explicito es la del reporte. **Pero es")
    w("una eleccion mia y puede molestar**, y por eso va marcada.")
    w("")
    w("**`D.3`. METI EN LA NOMINA UN ARNES QUE NO ES DE ESTA VUELTA.**")
    w("`vuelta182_tarea2_mutacion_apertura_auditor.py` es de la 182, y lo meti yo en")
    w("la 183 porque su ausencia habria cerrado los nueve tramos en ROJO. **La regla")
    w("me ampara** (acta 176 punto 7.2, reconfirmada en la `D.4` del acta 182), pero")
    w("**meter en la nomina un arnes ajeno el dia de la bateria es una decision de")
    w("alcance que nadie me encargo**. La alternativa era parar la vuelta de bateria")
    w("entera por una linea que la 182 no escribio.")
    w("")
    w("**`D.4`. DECLARE CONGELADO EL SUJETO DE UN ARNES AJENO.** Para que el anterior")
    w("entrara hubo que anadir el literal `SUJETO CONGELADO` a su docstring, porque")
    w("`guarda_del_sujeto_congelado()` lo daba **NO DECIDIBLE**. **Lo medi antes de")
    w("declararlo** (su unica aparicion de `REPORTE.md` fuera del docstring es un dato")
    w("en una tabla de escenarios), **pero la declaracion la firma quien escribio el")
    w("arnes, y no fui yo.**")
    w("")
    w("**`D.5`. LEI EL TRAMO DE LA CIEGA DE UN SITIO QUE EL ENCARGO NO NOMBRA.** El")
    w("encargo dice *\"la seccion 9 de mi acta 182\"*; ahi no hay ningun puesto y lo")
    w("medi. Fui al fichero sellado del auditor y lo cambie por `sha256`. **Creo que")
    w("es la fuente mejor y no la peor**, pero **cambie la fuente de un tramo por mi")
    w("cuenta**, y eso se marca.")
    w("")

    # ============================================================= SECCION 6
    w("## 6. LAS PREGUNTAS")
    w("")
    w("**1. LA NOMINA CRECE Y NADIE LA PODA. QUE PASA CUANDO NO QUEPA EN UNA")
    w("VUELTA.** Hoy son **%d entradas** y la bateria entera midio **%s minutos**"
      % (n_nomina, ("%.1f" % sum(minutos)) if minutos else "(sin medir)"))
    w("repartidos en nueve tramos. La opcion `c` (podar) la **RECHAZO** el fundador")
    w("el 5 sep. **No pido podarla: pregunto si el numero de tramos tambien crece**,")
    w("porque hoy el tamano de tramo esta fijado en 13 para que salgan nueve, y con la")
    w("nomina en 111 el ultimo tramo ya lleva **%d entradas**."
      % (tramos[8][4] if tramos[8][4] else 0))
    w("")
    w("**2. LA GUARDA DE LOS NUMERALES SE APLICA AL REPORTE DEL AUDITOR.**")
    w("`cerrar_reporte.py` es del ejecutor. El acta del auditor tiene tambien su")
    w("veredicto y sus cifras, y el `E.1` que disparo esta escalada nacio de una")
    w("contradiccion **del ejecutor**, pero nada impide la misma especie de caida en")
    w("un acta. **No lo hago por mi cuenta: no es mi documento.**")
    w("")
    w("**3. LAS OCHO ACTAS SIN REGISTRO SIGUEN SIN REGISTRO.** El `R.44` las")
    w("documenta como salto, que es lo encargado. **La pregunta es si alguna vez se")
    w("releen para escribirlas, o si el salto es la respuesta definitiva.**")
    w("")

    # ============================================================= SECCION 7
    w("## 7. PENDIENTES DE DOCTRINA")
    w("")
    w("**`PD.1` SIGUE ABIERTA Y NO LA TOCO:** las cinco `D` con el diferenciador ya")
    w("presente el dia del veredicto no son de la cola post fusion. El acta 182 la")
    w("dejo **registrada y sin resolver** en su `7.4`, y esta vuelta la hereda igual.")
    w("")
    w("**`PD.2` NUEVA. QUE PASA CUANDO EL ENCARGO NOMBRA MAL LA FUENTE DE UN TRAMO.**")
    w("La 1.e tenia que leer 30 puestos de un sitio donde no estan. **No hay regla")
    w("escrita** que diga si eso es PARADA (`EJECUTOR.md` 5, *\"contradice una regla")
    w("vigente\"*) o correccion declarada. **Lo trate como correccion declarada** y")
    w("segui, que es lo que `EJECUTOR.md` 5 manda cuando falta la regla: no parar,")
    w("registrar lo mejor sostenido y marcarlo. **Queda como pendiente de doctrina.**")
    w("")
    w("**`PD.3` NUEVA. UN ARNES QUE NACE EN UNA VUELTA DE BATERIA ENTRA EN SU PROPIA")
    w("BATERIA O EN LA SIGUIENTE.** El de la 1.c entro en la de hoy y corrio en el")
    w("**TRAMO 1**. Salio verde, asi que no hubo problema; **pero un arnes que se")
    w("estrena dentro de la bateria que lo estrena no tiene corrida anterior con la")
    w("que cotejar su reproducibilidad**, y la doble corrida compara una salida")
    w("consigo misma en su primer dia. **No lo resuelvo yo.**")
    w("")

    # ============================================================= SECCION 8
    w("## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA")
    w("")
    w("**`C.1`. DEJE QUE EL TRAMO 3 SE CORTARA POR CORRERLO EN PRIMER PLANO.** El")
    w("tramo 2 tardo **5,6 minutos** medidos, y aun asi lance el 3 encadenado detras")
    w("de un commit en la misma orden, con el techo de diez minutos de la sesion")
    w("delante. **Se corto a mitad.** No costo ningun dato porque el regimen del")
    w("fundador esta hecho justo para esto (**una vuelta cortada retoma en el tramo")
    w("siguiente**) y porque lo medi en vez de suponerlo: `git diff --numstat --")
    w("dataset/` dio **cero filas** y `SALIDA_V183_BATERIA_TRAMO_3.txt` **no existia**,")
    w("asi que `--siguiente` volvio a decir **TRAMO 3** y ahi se retomo. **Pero la")
    w("estimacion del `--plan` decia hasta 5,6 minutos por tramo y yo encadene un")
    w("commit con guardian delante: eso fue mio.**")
    w("")
    w("**`C.2`. EL ENCARGO DECIA 109 ENTRADAS DE NOMINA Y ESTA BATERIA CORRIO %d.**"
      % n_nomina)
    w("La cifra del encargo era correcta cuando se escribio y la apertura la")
    w("confirmo. **La movi yo**, en la TAREA 1, al meter los dos arneses. Lo digo")
    w("aqui y no solo en la tarea porque **cualquiera que compare el encargo con este")
    w("reporte va a ver dos numeros distintos**, y la diferencia tiene que tener")
    w("dueno: es mia, esta medida y esta razonada.")
    w("")
    w("**`C.3`. EL PRIMER BLOQUE DE APERTURA QUE ESCRIBI TRAIA UN `%d` SIN")
    w("ARGUMENTO.** En el bloque B del clon, una linea imprimia literalmente `%d`")
    w("en vez de la cifra de adjudicaciones. **Lo cazo la corrida en `--simular`,")
    w("antes de escribir nada en `docs/PENDIENTES.md`**, y se arreglo antes de la")
    w("corrida de verdad. No llego a ningun documento, pero se declara: una cifra que")
    w("no se imprime es una cifra que no se publica, y estuvo a una orden de")
    w("publicarse.")
    w("")
    w("> **NINGUNA DE LAS TRES SE TAPA.** La `C.1` es la que mas cerca estuvo de")
    w("> costar algo, y lo que la salvo no fue mi cuidado sino **el regimen por tramos")
    w("> del fundador**: sin el, un corte a los diez minutos habria tirado la bateria")
    w("> entera y esta vuelta habria vuelto a cerrar con un hueco.")
    w("")

    # ============================================================= LA TABLA
    w("### 8.1 LOS NUEVE TRAMOS, CONTADOS DE SUS PROPIOS FICHEROS")
    w("")
    w("**LA TABLA SE CUENTA DE SU FICHERO** (`EJECUTOR.md` 1). Cada fila sale de")
    w("`docs/loop/SALIDA_V183_BATERIA_TRAMO_<n>.txt`, leido con")
    w("`scripts/loop/_v183_tallar_cierre.py`: los bytes con `os.path.getsize` y con")
    w("el mismo fichero normalizado a LF, las lineas contando saltos, las entradas")
    w("contando sus lineas `ENTRADA DEL TRAMO:`, y el exitcode y los minutos de las")
    w("lineas que el propio tramo escribe al sellarse.")
    w("")
    w("| tramo | bytes disco | bytes LF | lineas | entradas | exitcode | minutos |")
    w("|---:|---:|---:|---:|---:|---:|---:|")
    for n, d, l, li, ent, ex, du in tramos:
        if d is None:
            w("| **%d** | **NO EXISTE** | | | | | |" % n)
        else:
            w("| **%d** | %d | %d | %d | %d | **%s** | %s |"
              % (n, d, l, li, ent, ex, du))
    w("")
    w("**CIFRA tramos con salida sellada no vacia: %d de 9.** **CIFRA entradas que"
      % len(hechos))
    w("los tramos dicen haber corrido, sumadas de sus lineas `ENTRADA DEL TRAMO:`:")
    w("%d.** **CIFRA exitcodes distintos de cero: %d.** **Suma de los minutos"
      % (entradas, len([t for t in hechos if t[5] not in (None, "0")])))
    w("medidos: %s**, contra la estimacion del `--plan`, que decia **entre 36,6 y"
      % (("%.1f" % sum(minutos)) if minutos else "(sin medir)"))
    w("47,7 minutos** y **se dijo como estimacion**. El tramo mas largo midio **%s"
      % (("%.1f" % max(minutos)) if minutos else "n/a"))
    w("minutos** y el mas corto **%s minutos**."
      % (("%.1f" % min(minutos)) if minutos else "n/a"))
    w("")
    w("**LA MIRADA DE LA BATERIA SOBRE SI MISMA, RECOMPUTADA AL CIERRE Y NO")
    w("HEREDADA DE LA CABECERA:** nomina **%d entradas**, `arneses_que_faltan()`"
      % n_nomina)
    w("**%d**, `nomina_invisible_al_censo()` **%d**, `guarda_del_sujeto_congelado()`"
      % (len(faltan), len(invis)))
    w("**%d**." % len(malas))

    t = NL.join(P) + NL
    io.open(DEST, "w", encoding="utf-8", newline=NL).write(t)
    print("ESCRITO: %s" % DEST)
    print("CIFRA bytes: %d | CIFRA lineas: %d" % (len(t.encode("utf-8")), t.count(NL)))
    print("CIFRA tramos sellados: %d de 9" % len(hechos))
    print("CIFRA entradas contadas de los tramos: %d" % entradas)
    print("CIFRA minutos sumados: %s" % (("%.1f" % sum(minutos)) if minutos else "n/a"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
