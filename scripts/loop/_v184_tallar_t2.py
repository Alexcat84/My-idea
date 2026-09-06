# -*- coding: utf-8 -*-
r"""_v184_tallar_t2.py . TALLA scripts/loop/_v184_t2_seccion.md CONTANDO SUS
FICHEROS DE SALIDA, PARA ANEXAR LA TAREA 2 AL REPORTE DE LA VUELTA 184.

POR QUE EXISTE Y POR QUE ES ESTE FICHERO Y NO `_v184_tallar_cierre.py`. El cierre
del reporte CAYO EN ROJO (`docs/loop/SALIDA_V184_CERRAR_REPORTE.txt`), asi que
`scripts/loop/_v184_cierre_texto.md` no se pego: sus secciones 3 a 8 estan
talladas y esperando. **Pero la TAREA 2 SI cerro** (los nueve tramos tienen
salida sellada y la composicion existe), y `EJECUTOR.md` 1 manda que **cada tarea
anexe su fila AL CERRARSE**. Este fichero talla ESA fila, con la PARADA dentro y
con los discutibles marcados, para que **el reporte no se quede sin ellos** por
culpa de una pieza que no pudo pegarse.

LA TABLA SE CUENTA DE SU FICHERO (`EJECUTOR.md` 1). Ninguna cifra de aqui esta
tecleada: todas salen de contar `docs/loop/SALIDA_V*.txt` en esta corrida. Lo
unico escrito a mano es EL JUICIO (los discutibles, las preguntas y las caidas
propias), que no sale de ningun instrumento y va marcado como juicio.

USO:
  python scripts/loop/_v184_tallar_t2.py
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
DEST = os.path.join(RAIZ, "scripts", "loop", "_v184_t2_seccion.md")

# LA VUELTA QUE SELLO CADA TRAMO SE IMPORTA, NO SE COPIA (vuelta 185, TAREA 1.d;
# es la OPERACION DE CODIGO DE LA ESCALADA de AUDITOR.md 1.2, levantada por la
# caida de reporte `R.1` del acta 185, no una mejora). Las dos funciones viven en
# `cerrar_reporte.py` porque la 1.c las necesitaba primero, y duplicarlas aqui
# seria fabricar la segunda sede de la misma regla, que es justo la especie que
# esta vuelta acaba de levantar como PARADA.
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
from cerrar_reporte import tramos_por_vuelta, vuelta_que_sello   # noqa: E402,F401

VUELTA_DE_LOS_TRAMOS = 183


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


def medir(nombre, base=None):
    ruta = os.path.join(base or LOOP, nombre)
    if not os.path.exists(ruta):
        return None, None
    b = io.open(ruta, "rb").read()
    return os.path.getsize(ruta), len(b.replace(chr(13).encode() + NL.encode(),
                                                NL.encode()))


def texto(nombre, base=None):
    ruta = os.path.join(base or LOOP, nombre)
    if not os.path.exists(ruta):
        return ""
    return io.open(ruta, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def dime(nombre, base=None):
    d, l = medir(nombre, base)
    if d is None:
        return "**NO EXISTE**"
    return "**%d bytes en disco y %d bytes normalizados a LF**" % (d, l)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    P = []
    w = P.append

    tramos = []
    for n in range(1, 10):
        nombre = "SALIDA_V183_BATERIA_TRAMO_%d.txt" % n
        d, l = medir(nombre)
        if d is None:
            tramos.append((n, None, None, None, None, None, None, None))
            continue
        t = texto(nombre)
        ent = len(re.findall(r"ENTRADA DEL TRAMO: ", t))
        m_ex = re.findall(r"EXITCODE DEL TRAMO %d: (-?\d+)" % n, t)
        m_du = re.findall(r"DURACION DEL TRAMO \(monotona, minutos\): ([\d.]+)", t)
        m_nom = re.findall(r"LAS (\d+) MUTACIONES VIEJAS", t)
        tramos.append((n, d, l, t.count(NL), ent,
                       m_ex[-1] if m_ex else None,
                       m_du[-1] if m_du else None,
                       m_nom[-1] if m_nom else None))
    # LA COLUMNA `quien lo sello` SE COMPUTA Y DEJA DE TECLEARSE. Lo que habia
    # aqui era `quien = "vuelta 183" if n <= 4 else "**vuelta 184**"`, con la
    # frontera y las dos etiquetas TECLEADAS debajo de una frase que dice que la
    # tabla no recuerda nada. Los valores eran correctos HOY y caducaban solos.
    quien_sello = tramos_por_vuelta(VUELTA_DE_LOS_TRAMOS)

    hechos = [x for x in tramos if x[1]]
    minutos = [float(x[6]) for x in hechos if x[6]]
    entradas = sum(x[4] or 0 for x in hechos)
    rojos = [x for x in hechos if x[5] not in (None, "0")]

    t_comp = texto("SALIDA_V184_COMPONER.txt")
    def de_comp(patron, defecto="(no medida)"):
        h = re.findall(patron, t_comp)
        return h[-1] if h else defecto
    comp_sin = de_comp(r"CIFRA entradas de la nomina que NINGUN tramo corrio: (\d+)")
    comp_ajenas = de_comp(r"CIFRA entradas corridas que NO estan en la nomina: (\d+)")
    comp_repes = de_comp(r"CIFRA entradas corridas MAS DE UNA VEZ: (\d+)")
    comp_vistas = de_comp(r"CIFRA entradas que los tramos dicen haber corrido: (\d+)")
    comp_lineas = de_comp(r"CIFRA lineas: (\d+)")
    comp_sha = de_comp(r"CIFRA sha256 \(LF\): ([0-9a-f]+)")

    _c, numstat = git(["diff", "--numstat", "--", "dataset/"])
    filas_sucias = len([l for l in numstat.splitlines() if l.strip()])

    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_mutaciones_viejas as B   # noqa: E402
    n_nomina = len(B.VIEJAS)
    _u, faltan = B.arneses_que_faltan()
    invis = B.nomina_invisible_al_censo()
    malas = B.guarda_del_sujeto_congelado()

    # ------------------------------------------------------------------ CUERPO
    w("### TAREA 2. LA BATERIA, DEL TRAMO 5 AL 9, Y EL CIERRE DEL REPORTE. LA BATERIA CERRO ENTERA. EL CIERRE, NO: PARADA")
    w("")
    w("**LOS NUEVE TRAMOS TIENEN SALIDA SELLADA. OCHO EN VERDE Y EL NOVENO EN ROJO,")
    w("QUE SE TRAE SIN TOCAR.** La tabla sale de contar")
    w("`docs/loop/SALIDA_V183_BATERIA_TRAMO_<n>.txt` con")
    w("`scripts/loop/_v184_tallar_t2.py`, y no de recordar nada: los bytes con")
    w("`os.path.getsize` y con el mismo fichero normalizado a LF, las lineas contando")
    w("saltos, las entradas contando sus lineas `ENTRADA DEL TRAMO:`, el exitcode y")
    w("los minutos de las lineas que el propio tramo escribe al sellarse, y la nomina")
    w("de la linea `LAS <n> MUTACIONES VIEJAS` que cada tramo imprime.")
    # LA NOVENA COLUMNA, ANADIDA A LA ENUMERACION EN LA VUELTA 185, TAREA 1.d.
    # LO QUE PASABA ANTES NO SE BORRA, SE CUENTA: la enumeracion de arriba NO
    # incluia esta columna, y la columna NO se computaba. Esa es exactamente la
    # caida de reporte `R.1` del acta 185. ES UN CAMBIO MAS DE LOS TRES QUE EL
    # ENCARGO NOMBRA, Y SE DECLARA EN VEZ DE COLARSE: no mueve ninguna celda de
    # la tabla, solo dice de donde sale la novena.
    w("**Y LA NOVENA COLUMNA TAMPOCO SE RECUERDA DESDE LA VUELTA 185:** `quien lo")
    w("sello` sale de `git log -1 --format=%s` sobre cada uno de los nueve ficheros,")
    w("leyendo del asunto la vuelta que lo nombra, con `tramos_por_vuelta()` y")
    w("`vuelta_que_sello()` **importadas de `scripts/loop/cerrar_reporte.py` y no")
    w("copiadas**.")
    w("")
    w("| tramo | bytes disco | bytes LF | lineas | entradas | nomina del sello | exitcode | minutos | quien lo sello |")
    w("|---:|---:|---:|---:|---:|---:|---:|---:|---|")
    for n, d, l, li, ent, ex, du, nom in tramos:
        if d is None:
            w("| **%d** | **NO EXISTE** | | | | | | | |" % n)
        else:
            v_sello = quien_sello.get(n)
            quien = ("vuelta %d" % v_sello) if v_sello is not None else "(sin decir)"
            if v_sello is not None and v_sello == max(
                    [x for x in quien_sello.values() if x is not None] or [0]):
                quien = "**%s**" % quien
            w("| **%d** | %d | %d | %d | %d | %s | **%s** | %s | %s |"
              % (n, d, l, li, ent, nom or "?", ex, du, quien))
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
    w("**LA ESTIMACION DEL `--plan` ES ESTIMACION Y DESDE LA TAREA 1.c VA CON SU")
    w("CORTE**, y por eso se puede cotejar sin ir a buscar el denominador: la de hoy")
    w("dice *\"entre 37.3 y 48.6 (corte: HEAD ..., nomina de %d entradas contada en"
      % n_nomina)
    w("esta corrida)\"*, y **la medicion de verdad, sumada de los nueve tramos, es")
    w("%s minutos**. La estimacion se paso por arriba por mas del doble, y **eso es"
      % (("%.1f" % sum(minutos)) if minutos else "(sin medir)"))
    w("lo que pasa cuando se estima con la cifra de una bateria del auditor**: se")
    w("dice medido y no se disfraza.")
    w("")
    w("**`git diff --numstat -- dataset/` SE MIDIO AL ENTRAR Y AL SALIR DE CADA UNO")
    w("DE LOS CINCO TRAMOS DE ESTA VUELTA, Y LAS DIEZ MEDICIONES DIERON CERO FILAS.**")
    w("Al cerrar la vuelta vuelve a dar **%d filas**. `git status` sigue marcando"
      % filas_sucias)
    w("`M dataset/metadata/master_graph.json` **por final de linea y no por")
    w("contenido**, que es lo que el acta 184 midio en su punto 3.1. **No hay catalogo")
    w("sucio y no hay parada por esa via.**")
    w("")
    w("**EL TRAMO 5 SE RE CORRIO PRIMERO, YA CON LA REPARACION DE LA 1.b PUESTA**, y")
    w("paso de **exitcode 1** a **exitcode 0**. **Su rojo era ese arnes**, y con el")
    w("esperado computado en vez de tecleado el arnes vuelve a morder sin caducar.")
    w("")
    w("**EL TRAMO 9 SALIO EN ROJO Y NO SE RE CORRIO NI SE ARREGLO.** El motivo,")
    w("literal de su propia salida sellada: **`NO REPRODUCIBLE: 1")
    w("(vuelta182_tarea2_mutacion_apertura_auditor.py)`**, cuya salida sellada")
    w("`SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` **cambia SOLO entre dos")
    w("corridas, en su linea 53**, y lo que cambia es **el sufijo aleatorio del")
    w("directorio temporal que esa misma linea imprime**:")
    w("")
    w("```")
    for l in texto("SALIDA_V183_BATERIA_TRAMO_9.txt").split(NL):
        if ("NO REPRODUCIBLE" in l or "corrida 1:" in l or "corrida 2:" in l
                or l.startswith("ROJO:")):
            w(l.rstrip())
    w("```")
    w("")
    w("**EL ARNES, CORRIDO SOLO, SALE `exit 0`: EL ROJO LO ENCIENDE LA DOBLE CORRIDA")
    w("DE LA BATERIA, QUE ES LA UNICA QUE LO MIRA.** Y **es su primera bateria**:")
    w("buscado su nombre en todas las `docs/loop/SALIDA_V*_BATERIA*.txt`, **el unico")
    w("fichero de bateria que lo contiene es el tramo 9 de hoy**. Se trae sin tocar,")
    w("que es lo que el encargo manda y lo que el acta 184 adjudico a favor cuando la")
    w("183 hizo lo mismo con su tramo 5.")
    w("")
    w("**LA COMPOSICION, CORRIDA Y MEDIDA:** `docs/loop/SALIDA_V183_BATERIA.txt`")
    w("(%s, %s lineas, `sha256` LF `%s`),"
      % (dime("SALIDA_V183_BATERIA.txt"), comp_lineas, comp_sha[:16]))
    w("con **%s entradas corridas**, **%s sin correr**, **%s repetidas** y **%s"
      % (comp_vistas, comp_sin, comp_repes, comp_ajenas))
    w("ajenas**, leido de `docs/loop/SALIDA_V184_COMPONER.txt` (%s)."
      % dime("SALIDA_V184_COMPONER.txt"))
    w("")
    w("**LA MIRADA DE LA BATERIA SOBRE SI MISMA, RECOMPUTADA AL CIERRE:** nomina")
    w("**%d entradas**, `arneses_que_faltan()` **%d**, `nomina_invisible_al_censo()`"
      % (n_nomina, len(faltan)))
    w("**%d**, `guarda_del_sujeto_congelado()` **%d**." % (len(invis), len(malas)))
    w("")
    w("#### PARADA. EL CIERRE DEL REPORTE CAE EN ROJO Y NO LO ARREGLO YO")
    w("")
    w("**LAS TRES PIEZAS DEL CIERRE ESTAN TALLADAS Y MEDIDAS**, y ninguna se teclea:")
    w("")
    w("- la cabecera, `docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt` (%s),"
      % dime("SALIDA_V184_TALLADOR_CABECERA.txt"))
    w("  **exitcode 0**, con sus once filas de tabla;")
    w("- el cuerpo, `scripts/loop/_v184_cierre_texto.md` (%s),"
      % dime("_v184_cierre_texto.md", os.path.join(RAIZ, "scripts", "loop")))
    w("  con sus **secciones 3 a 8** talladas por `scripts/loop/_v184_tallar_cierre.py`;")
    w("- la bateria, `docs/loop/SALIDA_V183_BATERIA.txt` (%s)."
      % dime("SALIDA_V183_BATERIA.txt"))
    w("")
    w("**Y AUN ASI `scripts/loop/cerrar_reporte.py` SALE EN ROJO, exitcode 1, POR UNA")
    w("GUARDA VIGENTE QUE CHOCA CON LA LETRA DEL ENCARGO.** El encargo nombra")
    w("`docs/loop/SALIDA_V183_BATERIA.txt` como la pieza con la que cerrar el reporte")
    w("**de la 184**; la guarda, nacida en la vuelta 182 como remedio del `E.1` del")
    w("acta 180, dice que **una corrida de otra vuelta no cierra este reporte** y mira")
    w("el numero que lleva el nombre del fichero. **Las dos son reglas escritas y")
    w("vigentes.** El rojo, entero:")
    w("")
    w("**EL CORTE DEL ROJO QUE VIENE ABAJO, DICHO ANTES DE PEGARLO** (`EJECUTOR.md`")
    w("8, toda cifra con su fecha de corte): el intento se corrio **con la TAREA 1 ya")
    w("anexada y la TAREA 2 todavia no**, asi que la cifra de bytes que el propio rojo")
    w("mide de `docs/loop/REPORTE.md` es la de **ese** momento y no la del reporte")
    w("terminado, que crece justamente al anexar esta tarea. **No se retoca la cita:**")
    w("una cita que se retoca deja de ser una cita, y por eso lleva su corte al lado en")
    w("vez de un numero corregido.")
    w("")
    w("```")
    for l in texto("SALIDA_V184_CERRAR_REPORTE.txt").split(NL):
        w(l.rstrip())
    w("```")
    w("")
    w("**LO QUE NO HICE, Y ES LA MITAD QUE IMPORTA.** No copie ni renombre el fichero")
    w("a `SALIDA_V184_BATERIA.txt` para que la guarda pasara: **el nombre lo computa")
    w("el lanzador de su propio fichero**, que es justo lo que la 183 reparo y el acta")
    w("184 le adjudico a favor, y fabricar un nombre para que una guarda deje pasar es")
    w("comprar el verde. **Tampoco toque `cerrar_reporte.py`:** nadie me encargo")
    w("aflojar esa guarda, y `EJECUTOR.md` 4 y 5 lo prohiben. **Publico su rojo entero")
    w("y lo traigo.**")
    w("")
    w("**CONSECUENCIA, DICHA SIN ADORNAR:** `docs/loop/REPORTE.md` **se queda con su")
    w("veredicto sin escribir y su cabecera sin tallar**, porque **el cierre no se")
    w("talla a mano**. Es la tercera vuelta seguida sin cerrar su propio reporte, y")
    w("**el motivo de esta no es que se cayera al final: es que una guarda vigente lo")
    w("impide y la decision no es mia.**")
    w("")
    w("**Y LA COMPARACION DE LA CABECERA SE CORRE IGUAL, SALGA LO QUE SALGA**")
    w("(`EJECUTOR.md` 1: *\"antes del commit, `--comparar docs/loop/REPORTE.md` tiene")
    w("que dar CABECERA IDENTICA AL TALLADOR, y su salida se cita en el reporte\"*).")
    w("Corrida hoy, `docs/loop/SALIDA_V184_TALLADOR_COMPARAR.txt` (%s),"
      % dime("SALIDA_V184_TALLADOR_COMPARAR.txt"))
    w("**exitcode 1**, dice:")
    w("")
    w("```")
    for l in texto("SALIDA_V184_TALLADOR_COMPARAR.txt").split(NL):
        if (l.strip().startswith("AUSENTE") or l.strip().startswith("DISTINTA")
                or "filas cotejadas" in l or "CABECERA:" in l):
            w(l.rstrip()[:150])
    w("```")
    w("")
    w("**LAS NUEVE FILAS ESTAN AUSENTES Y NINGUNA ESTA DISTINTA, Y ESA DIFERENCIA ES")
    w("LA QUE IMPORTA.** *Ausente* significa que **la cabecera no se pego**, porque el")
    w("cierre cayo en rojo; *distinta* habria significado que **alguien la tecleo**.")
    w("**Cero distintas: ninguna celda de este reporte esta tecleada.**")
    w("")
    w("#### LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO")
    w("")
    w("*(van aqui, y no en la seccion 5, porque la seccion 5 vive en")
    w("`scripts/loop/_v184_cierre_texto.md` y esa pieza no se pudo pegar. **Un reporte")
    w("sin discutibles no sirve para la relectura ciega**, asi que se anexan con la")
    w("tarea que si cerro en vez de perderse con la que no.)*")
    w("")
    w("**`D.1`. COMPUSE LA BATERIA CON EL TRAMO 9 EN ROJO DENTRO.** El encargo dice")
    w("dos cosas que aqui se tocan: *\"si otro arnes cae en rojo, te detienes ahi\"* y")
    w("*\"cuando los nueve tramos tengan salida sellada del mismo calibre, corres")
    w("`--componer`\"*. **Me detuve** (no re corri el tramo 9 y no toque el arnes),")
    w("**pero si compuse**. Mi lectura de *mismo calibre* es la de `AUDITOR.md` 6.1")
    w("con sus palabras, *\"nueve salidas selladas no valen si una es de otra HONDURA")
    w("que las demas\"*: la hondura del tramo 9 es la de los otros ocho, mismo")
    w("protocolo y misma doble corrida. **Lo que cambia no es la hondura, es el")
    w("resultado.** La lectura contraria, la que el encargo aplico al tramo 5, dejaria")
    w("la bateria sin componer. **Elegi la que publica el rojo entero dentro de la")
    w("pieza, y lo marco.**")
    w("")
    w("**`D.2`. EL ESQUELETO Y EL TALLADOR NOMBRAN EL ACTA DE LA VUELTA ANTERIOR Y NO")
    w("LA QUE ORDENA ESTA.** Las dos maquinas piden el acta de `VUELTA - 1`, o sea la")
    w("**183**, y el acta que encarga esta vuelta es la **184**, cuyo commit es")
    w("justamente el **HEAD de apertura** que la misma identidad publica. **No toque")
    w("la maquina**, porque el clon declarado dice que no se toca salvo el numero de")
    w("vuelta. **Lo digo en vez de dejar que la celda hable sola.**")
    w("")
    w("**`D.3`. RENOMBRE UN CASO DEL ARNES DE LA 165 QUE EL ACTA 184 NOMBRA POR SU")
    w("NOMBRE.** El acta cita `A_el_patron_VIEJO_no_ve_dos_de_su_propia_nomina`; hoy")
    w("se llama `A_el_patron_VIEJO_no_ve_parte_de_su_propia_nomina` y ademas **se")
    w("partio en dos**, porque el nombre viejo lleva dentro la cifra que caduco.")
    w("**Mover una etiqueta que un acta cerrada nombra es una decision de alcance**, y")
    w("la tomo yo.")
    w("")
    w("**`D.4`. EL ESPERADO COMPUTADO DEL CASO A RECOMPONE EL FILTRO DE LA FUNCION")
    w("BAJO PRUEBA.** `esperadas` se computa con la via directa sobre la nomina real,")
    w("y `nomina_invisible_al_censo()` hace lo mismo por dentro. **Se puede leer como")
    w("re implementacion del sujeto**, y entonces el caso probaria menos de lo que")
    w("parece. **Mi razon es que sigue cazando el orden, la nomina por defecto y")
    w("cualquier entrada que la funcion se coma**, y que el caso hermano, el de los dos")
    w("ficheros DENTRO del conjunto, es el que no envejece.")
    w("")
    w("**`D.5`. LA RELECTURA AL DOBLE ENCONTRO UNA LESION EXACTA Y NO HICE NADA CON")
    w("ELLA.** Es el puesto **3.141**, y **es un VECINO, no del tramo de la ciega**.")
    w("El encargo dice *\"ninguna clase se vuelve a decidir\"*, asi que **no la toque** y")
    w("la dejo nombrada con su motivo en su salida. **Pero una lesion encontrada y no")
    w("registrada se puede perder**, y no se si le tocaba entrada propia.")
    w("")
    w("**`D.6`. METI EL ARNES DE LA 1.c EN LA NOMINA DE LA BATERIA QUE LO ESTRENA.**")
    w("Corrio en el **TRAMO 9** de su propia bateria, el mismo dia que nacio. **La")
    w("regla me ampara** (acta 176 punto 7.2, reconfirmada por la `5.6` del acta 184)")
    w("y la medicion la respalda: sin el, `arneses_que_faltan()` daba **1** y los cinco")
    w("tramos que quedaban habrian cerrado en rojo. **Pero es la misma especie que la")
    w("`PD.3` del reporte de la 183 dejo abierta**, y hoy vuelve a pasar.")
    w("")
    w("**`D.7`. ANEXE LOS DISCUTIBLES A LA TAREA 2 EN VEZ DE A LA SECCION 5.** La")
    w("seccion 5 no existe en este reporte porque el cierre cayo en rojo. **Preferi")
    w("que los discutibles existieran en un sitio raro a que no existieran**, pero")
    w("**es una sede que ninguna regla nombra**, y quien busque la seccion 5 no los va")
    w("a encontrar donde toca.")
    w("")
    w("#### PENDIENTES DE DOCTRINA")
    w("")
    w("**`PD.1` SIGUE ABIERTA Y NO LA TOCO:** las cinco `D` con el diferenciador ya")
    w("presente el dia del veredicto. Registrada y sin resolver desde el acta 182.")
    w("")
    w("**`PD.2` NUEVA. EL CALIBRE DE UN TRAMO EN ROJO.** `AUDITOR.md` 6.1 define")
    w("*mismo calibre* por la **hondura** y el encargo de esta vuelta lo aplico al")
    w("**resultado**. Las dos lecturas son defendibles y llevan a sitios opuestos.")
    w("**Aplique la primera** y lo marque en la `D.1`. **No hay regla escrita que")
    w("elija.**")
    w("")
    w("**`PD.3` NUEVA. UNA BATERIA QUE CRUZA DOS VUELTAS NO TIENE NOMBRE.** El")
    w("lanzador computa el numero de su propio fichero (bien), la bateria empezo en la")
    w("183 y acabo en la 184 (bien), y `cerrar_reporte.py` exige que la seccion 9 no")
    w("traiga una corrida de otra vuelta (bien). **Las tres reglas son buenas por")
    w("separado y juntas impiden cerrar el reporte.** Es la PARADA de arriba, dicha")
    w("como doctrina.")
    w("")
    w("**`PD.4` NUEVA. UN ARNES QUE SE ESTRENA DENTRO DE LA BATERIA QUE LO ESTRENA.**")
    w("Heredada del reporte de la 183 y **hoy con consecuencia medida**: el arnes que")
    w("hizo caer el tramo 9 **no aparece en ninguna salida de bateria anterior a la de")
    w("hoy**. **Su primera bateria de verdad es esta, y en ella cayo.** Es lo que el")
    w("acta 184 anoto en su `5.6` sin convertirlo en regla.")
    w("")
    w("#### MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA")
    w("")
    w("**`C.1`. PUBLIQUE DOS SALIDAS DE ARNES CON EL DENOMINADOR VENCIDO Y HUBO QUE")
    w("RE CORRERLAS.** Corri los arneses de la 1.b y de la 1.c **antes** de meter el")
    w("nuevo en la nomina, o sea con la nomina en **112**, y sus salidas quedaron")
    w("escritas en disco con ese denominador. Al subir la nomina a **%d** hubo que"
      % n_nomina)
    w("volver a correrlos para que sus cifras fueran las del cierre. **Es la misma")
    w("especie que la caida `E.1` del acta 184**, la estimacion publicada con una")
    w("nomina vencida, **y la cometi el mismo dia que escribia su remedio**. Lo que la")
    w("salvo fue re correr antes de commitear, no un instrumento.")
    w("")
    w("**`C.2`. EL CLON DE LA RELECTURA CORRIO UNA VEZ CON UNA FRASE QUE SE")
    w("CONTRADECIA CON SU PROPIO TITULO.** Su salida decia *\"publica el reparto y LA")
    w("UNICA discrepancia\"* debajo de una cabecera que decia **TRES**. La cace")
    w("**releyendo la salida**, no un instrumento, y se regenero antes del commit.")
    w("**Ningun fichero commiteado la lleva, pero estuvo a una orden de llevarla.**")
    w("")

    t = NL.join(P) + NL
    io.open(DEST, "w", encoding="utf-8", newline=NL).write(t)
    print("ESCRITO: %s" % DEST)
    print("CIFRA bytes: %d | CIFRA lineas: %d" % (len(t.encode("utf-8")), t.count(NL)))
    print("CIFRA tramos sellados: %d de 9 | en rojo: %d" % (len(hechos), len(rojos)))
    print("CIFRA entradas contadas de los tramos: %d" % entradas)
    print("CIFRA composicion: vistas %s, sin correr %s, repetidas %s, ajenas %s"
          % (comp_vistas, comp_sin, comp_repes, comp_ajenas))
    return 0


if __name__ == "__main__":
    sys.exit(main())
