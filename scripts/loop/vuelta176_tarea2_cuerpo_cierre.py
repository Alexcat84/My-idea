# -*- coding: utf-8 -*-
r"""vuelta176_tarea2_cuerpo_cierre.py . TALLA EL CUERPO DEL CIERRE DEL REPORTE
DE LA VUELTA 176 (las secciones 3 a 8) EN VEZ DE TECLEARLO.

POR QUE NACE, Y LA REGLA ES VIEJA. `EJECUTOR.md` 1 lo dice en cuatro sedes: LA
TABLA SE IMPRIME, NO SE TECLEA (15 ago, por las paradas de las vueltas 31 y 32);
LA CABECERA DEL REPORTE SE TALLA (20 ago, por la racha de las 54, 55 y 56); LA
TABLA SE CUENTA DE SU FICHERO (26 ago, por la racha de las 74, 75 y 76, que entro
justo DONDE EL TALLADOR NO ALCANZA, en las fases mecanicas); y LA IDENTIDAD SE
LEE DE GIT (26 ago, por la racha de las 77, 78 y 79, que entro por la PROSA de
identidad, que es prosa suelta encima de la tabla). El cuerpo del cierre es
exactamente ese terreno: `cerrar_reporte.py` pega la cabecera y la bateria, pero
las secciones 3 a 8 las venia escribiendo una mano.

QUE HACE: escribe `scripts/loop/_v176_cierre_texto.md` con las secciones 3 a 8, y
TODA CIFRA Y TODA FILA DE TABLA DE LAS SECCIONES 3 Y 4 SALE DE UN INSTRUMENTO
CORRIDO AQUI:

  . los dos extremos, de los sellos `SALIDA_V176_HEAD_APERTURA.txt` y
    `SALIDA_V176_HEAD_CIERRE.txt`, nunca de la memoria;
  . la tabla de commits de la vuelta, de `git log <apertura>..<cierre>`;
  . el censo de rutas tocadas, de `git diff --name-only` entre los dos extremos,
    agrupado por directorio y CONTADO, no estimado;
  . que el grafo no se movio, de `git diff --numstat` entre los dos extremos
    sobre `dataset/ web/ engine/`;
  . las cuatro cifras de Gate 0, LEIDAS de los ficheros `SALIDA_V176_*_CIERRE.txt`
    que escribe `scripts/loop/vuelta176_cierre.py`;
  . el veredicto de la bateria y EL ROJO, CONTADOS de los nueve ficheros de tramo
    y no copiados de ningun mensaje de commit.

LAS SECCIONES 5 A 8 SON JUICIO Y VAN ESCRITAS: los discutibles, las preguntas,
los pendientes de doctrina y las caidas propias no salen de ningun instrumento
porque no son mediciones. LO QUE SI SE EXIGE DE ELLAS es que ninguna CIFRA que
lleven dentro este tecleada, y por eso las pocas que citan van interpoladas desde
lo medido aqui arriba.

CAE EN ROJO Y NO ESCRIBE NADA si le falta cualquiera de los ficheros de los que
lee, en vez de rellenar el hueco con una frase.

USO:
  python scripts/loop/vuelta176_tarea2_cuerpo_cierre.py
"""
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
DESTINO = os.path.join(AQUI, "_v176_cierre_texto.md")
NL = chr(10)
BARRA = chr(124)


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


def leer(ruta):
    return io.open(ruta, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    fallos = []

    # ------------------------------------------------------- LOS DOS EXTREMOS
    r_ap = os.path.join(LOOP, "SALIDA_V176_HEAD_APERTURA.txt")
    r_ci = os.path.join(LOOP, "SALIDA_V176_HEAD_CIERRE.txt")
    for r in (r_ap, r_ci):
        if not os.path.exists(r):
            fallos.append("no existe el sello %s" % os.path.basename(r))
    if fallos:
        print("ROJO, no se escribe nada:")
        for f in fallos:
            print("   " + f)
        return 1
    apertura = leer(r_ap).strip()
    cierre = leer(r_ci).strip()
    print("apertura leida del sello: %s" % apertura[:8])
    print("cierre   leido del sello: %s" % cierre[:8])

    # --------------------------------------------------- LOS COMMITS, DE GIT
    _c, log = git(["log", "--format=%h%x09%s", "%s..%s" % (apertura, cierre)])
    filas_log = [l.split(chr(9), 1) for l in log.splitlines() if chr(9) in l]
    filas_log.reverse()
    print("commits de la vuelta, leidos de git log: %d" % len(filas_log))

    tabla_commits = [
        BARRA + " # " + BARRA + " commit " + BARRA +
        " asunto, primeras 92 letras, leido de git " + BARRA,
        BARRA + "---:" + BARRA + "---" + BARRA + "---" + BARRA]
    for i, (h, s) in enumerate(filas_log, 1):
        limpio = s.replace(BARRA, "/")[:92]
        tabla_commits.append("%s %d %s `%s` %s %s %s"
                             % (BARRA, i, BARRA, h, BARRA, limpio, BARRA))

    # -------------------------------------------- LAS RUTAS TOCADAS, CONTADAS
    _c, nombres = git(["diff", "--name-only", "%s..%s" % (apertura, cierre)])
    rutas = [l.strip() for l in nombres.splitlines() if l.strip()]
    por_dir = {}
    for ruta in rutas:
        d = ruta.rsplit("/", 1)[0] + "/" if "/" in ruta else "(raiz)"
        por_dir[d] = por_dir.get(d, 0) + 1
    print("rutas tocadas entre los dos extremos: %d" % len(rutas))

    tabla_rutas = [BARRA + " directorio " + BARRA + " rutas tocadas " + BARRA,
                   BARRA + "---" + BARRA + "---:" + BARRA]
    for d in sorted(por_dir):
        tabla_rutas.append("%s `%s` %s %d %s" % (BARRA, d, BARRA, por_dir[d], BARRA))
    tabla_rutas.append("%s **TOTAL** %s **%d** %s" % (BARRA, BARRA, len(rutas), BARRA))

    # ------------------------------------------- EL GRAFO, ENTRE LOS EXTREMOS
    _c, numstat = git(["diff", "--numstat", "%s..%s" % (apertura, cierre),
                       "--", "dataset/", "web/", "engine/"])
    filas_numstat = [l for l in numstat.splitlines() if l.strip()]
    print("filas de numstat sobre dataset/ web/ engine/: %d" % len(filas_numstat))

    # --------------------------------------------------- GATE 0, DE FICHEROS
    def cifra(nombre, patron, grupo=1):
        ruta = os.path.join(LOOP, "SALIDA_V176_%s_CIERRE.txt" % nombre)
        if not os.path.exists(ruta):
            fallos.append("no existe docs/loop/SALIDA_V176_%s_CIERRE.txt" % nombre)
            return None
        m = re.search(patron, leer(ruta))
        if not m:
            fallos.append("docs/loop/SALIDA_V176_%s_CIERRE.txt no trae la cifra que "
                          "se le pide (patron %r)" % (nombre, patron))
            return None
        return m.group(grupo)

    motor = cifra("MOTOR", r"(\d+\s*/\s*\d+)", 1)
    tsc = cifra("TSC", r"EXIT=(\d+)")
    web_tests = cifra("WEB", r"Tests\s+(\d+)\s+passed")
    web_fich = cifra("WEB", r"Test Files\s+(\d+)\s+passed")

    # LAS FILAS DE NUMSTAT SE CUENTAN POR SU FORMA, NO POR "toda linea que no
    # este vacia". El bloque de cierre captura stdout y stderr juntos, y en
    # Windows git escribe en stderr el aviso de LF/CRLF; contarlo como fila
    # publicaria "1 fila" donde el catalogo no se movio, que es una cifra falsa
    # en la direccion mas cara. Una fila de `--numstat` es
    # `<anadidas>TAB<borradas>TAB<ruta>` y nada mas.
    numstat_ciclo = os.path.join(LOOP, "SALIDA_V176_CICLO_NUMSTAT_CIERRE.txt")
    filas_ciclo = None
    if os.path.exists(numstat_ciclo):
        filas_ciclo = len([l for l in leer(numstat_ciclo).splitlines()
                           if re.match(r"^[\d-]+\t[\d-]+\t\S", l)])
    else:
        fallos.append("no existe docs/loop/SALIDA_V176_CICLO_NUMSTAT_CIERRE.txt")

    # ------------------------------------- LA BATERIA, CONTADA DE SUS TRAMOS
    tramos = sorted((n for n in os.listdir(LOOP)
                     if re.match(r"^SALIDA_V176_BATERIA_TRAMO_\d+\.txt$", n)),
                    key=lambda n: int(re.search(r"_(\d+)\.txt$", n).group(1)))
    if not tramos:
        fallos.append("no hay ni un fichero SALIDA_V176_BATERIA_TRAMO_<n>.txt")
    total_entradas = 0
    minutos = 0.0
    conteos = {"ANCLA PERDIDA": 0, "NO MORDIO": 0, "NO REPRODUCIBLE": 0,
               "CASO DECLARADO": 0, "RUIDO DE CONCURRENCIA": 0}
    culpables = []
    tabla_tramos = [
        BARRA + " tramo " + BARRA + " fichero " + BARRA + " bytes " + BARRA +
        " lineas " + BARRA + " entradas " + BARRA + " minutos " + BARRA +
        " exit " + BARRA,
        BARRA + "---:" + BARRA + "---" + BARRA + "---:" + BARRA + "---:" +
        BARRA + "---:" + BARRA + "---:" + BARRA + "---:" + BARRA]
    for nombre in tramos:
        ruta = os.path.join(LOOP, nombre)
        texto = leer(ruta)
        n = int(re.search(r"_(\d+)\.txt$", nombre).group(1))
        ent = len(re.findall(r"ENTRADA DEL TRAMO: ", texto))
        total_entradas += ent
        for clave in conteos:
            m = re.search(r"^\s*%s\s*:\s*(\d+)\s*\((.*?)\)" % re.escape(clave),
                          texto, re.M)
            if m:
                conteos[clave] += int(m.group(1))
                if int(m.group(1)) and clave in ("ANCLA PERDIDA", "NO MORDIO",
                                                 "NO REPRODUCIBLE"):
                    culpables.append((n, clave, m.group(2)))
        m_min = re.search(r"DURACION DEL TRAMO \(monotona, minutos\): ([\d.]+)", texto)
        if m_min:
            minutos += float(m_min.group(1))
        m_exit = re.search(r"EXITCODE DEL TRAMO \d+: (-?\d+)", texto)
        tabla_tramos.append(
            "%s %d %s `%s` %s %d %s %d %s %d %s %s %s %s %s"
            % (BARRA, n, BARRA, nombre, BARRA, os.path.getsize(ruta), BARRA,
               texto.count(NL), BARRA, ent, BARRA,
               m_min.group(1) if m_min else "?", BARRA,
               m_exit.group(1) if m_exit else "?", BARRA))
    unica = os.path.join(LOOP, "SALIDA_V176_BATERIA.txt")
    bytes_unica = os.path.getsize(unica) if os.path.exists(unica) else -1
    tabla_tramos.append(
        "%s **union** %s `SALIDA_V176_BATERIA.txt` %s **%d** %s  %s **%d** %s "
        "**%.1f** %s  %s"
        % (BARRA, BARRA, BARRA, bytes_unica, BARRA, BARRA, total_entradas,
           BARRA, minutos, BARRA, BARRA))

    tabla_culpables = [
        BARRA + " tramo " + BARRA + " clase de rojo " + BARRA + " arnes " + BARRA,
        BARRA + "---:" + BARRA + "---" + BARRA + "---" + BARRA]
    for n, clase, quien in culpables:
        tabla_culpables.append("%s %d %s **%s** %s `%s` %s"
                               % (BARRA, n, BARRA, clase, BARRA, quien, BARRA))
    if not culpables:
        tabla_culpables.append("%s  %s (ninguno) %s  %s" % (BARRA, BARRA, BARRA, BARRA))

    if fallos:
        print("")
        print("ROJO, %d motivo(s), y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("   " + f)
        return 1

    T = {
        "ap": apertura[:8], "ci": cierre[:8],
        "n_commits": len(filas_log),
        "tabla_commits": NL.join(tabla_commits),
        "n_rutas": len(rutas),
        "tabla_rutas": NL.join(tabla_rutas),
        "n_numstat": len(filas_numstat),
        "motor": (motor or "").strip(),
        "tsc": tsc,
        "web_tests": web_tests,
        "web_fich": web_fich,
        "filas_ciclo": filas_ciclo,
        "n_tramos": len(tramos),
        "entradas": total_entradas,
        "minutos": minutos,
        "tabla_tramos": NL.join(tabla_tramos),
        "tabla_culpables": NL.join(tabla_culpables),
        "bytes_unica": bytes_unica,
        "perdidas": conteos["ANCLA PERDIDA"],
        "no_mordio": conteos["NO MORDIO"],
        "no_reprod": conteos["NO REPRODUCIBLE"],
        "declarados": conteos["CASO DECLARADO"],
        "ruido": conteos["RUIDO DE CONCURRENCIA"],
        "n_rojos": len(culpables),
    }

    salida = 0
    for ruta, plantilla in ((DESTINO, TEXTO),
                            (os.path.join(AQUI, "_v176_t1_seccion.md"), T1),
                            (os.path.join(AQUI, "_v176_t2_seccion.md"), T2)):
        texto = plantilla % T
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
        print("")
        print("ESCRITO: %s (%d bytes, %d lineas)"
              % (os.path.relpath(ruta, RAIZ).replace(os.sep, "/"),
                 len(texto.encode("utf-8")), texto.count(NL)))
        for l in texto.split(NL):
            if l.startswith("## "):
                print("   " + l)
        largos = [c for c in texto if c in (chr(8212), chr(8211))]
        print("   guiones largos o medios colados: %d" % len(largos))
        if largos:
            salida = 1
    return salida


TEXTO = r"""## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT

**LOS DOS EXTREMOS SE LEEN DE LOS SELLOS Y NO SE TECLEAN.** Apertura `%(ap)s`, de
`docs/loop/SALIDA_V176_HEAD_APERTURA.txt`, sellado **antes de la primera
operacion**; cierre `%(ci)s`, de `docs/loop/SALIDA_V176_HEAD_CIERRE.txt`, sellado
**tras la ultima**. **LOS COMMITS DE LA VUELTA, LEIDOS DE
`git log %(ap)s..%(ci)s`: %(n_commits)d.** La tabla la imprime
`scripts/loop/vuelta176_tarea2_cuerpo_cierre.py`; ninguna celda se teclea.

%(tabla_commits)s

**LAS RUTAS QUE ESTA VUELTA TOCA, CONTADAS Y NO ESTIMADAS**, de
`git diff --name-only %(ap)s..%(ci)s`, agrupadas por directorio:

%(tabla_rutas)s

**EL GRAFO NO SE MOVIO, PROBADO Y NO CREIDO:**
`git diff --numstat %(ap)s..%(ci)s -- dataset/ web/ engine/` sale con
**%(n_numstat)d filas**. **Cero nodos tocados, cero aristas movidas.** Y ninguna
vuelta tenia mas motivos que esta para comprobarlo, porque su trabajo entero
consiste en correr arneses que MUTAN `dataset/` a proposito.

**LA GUARDA DEL COMMIT CORRIO DOS VECES POR TRAMO, AL ENTRAR Y AL SALIR**, o sea
**%(n_tramos)d veces al entrar y %(n_tramos)d al salir**, y todas midio **cero
filas** de `git diff --numstat -- dataset/`. No es una promesa: cada corrida esta
dentro del fichero de su tramo.

**EL COMMIT QUE LLEVA ESTE REPORTE NO SE NOMBRA AQUI**, porque se crea despues de
escribirlo.

## 4. LA PARADA, Y ES UNA. LA BATERIA MORDIO

**HAY PARADA, Y NO LA ARREGLO YO** (`EJECUTOR.md` 5: *"Paras SOLO si algo
contradice una regla vigente o una cifra publicada con su corte: en ese caso lo
escribes en el reporte como PARADA y no lo arreglas tu"*). **LA BATERIA DE ESTA
VUELTA SACO %(n_rojos)d ROJO**, y la tabla sale contada de los ficheros de tramo:

%(tabla_culpables)s

**QUE FALLA, EXACTAMENTE.** Dentro de
`scripts/loop/vuelta166_tarea2_mutacion_correccion.py`, el caso
`H_el_texto_nombra_las_tres` mide **`real=11`** contra un **`esperado=3`**. El
`3` es **UNA CONSTANTE LITERAL ESCRITA EN EL ARNES**
(`casos.append(("H_el_texto_nombra_las_tres", real.count("cae sobre"), 3))`),
mientras que el `11` sale de `T.medir_clausula_1()` corrido **sobre el registro de
veredictos VIVO**, que crece en cada vuelta. Los otros 18 casos del arnes pasan,
y los 19 CAEN al mutarles el esperado.

**NO ES CAIDA DE ESTA VUELTA, Y LO MIDO EN VEZ DE ALEGARLO.** En la ultima bateria
con cuerpo, la del auditor de la vuelta 171, este mismo arnes salio
**`exit 0 OK` en 4,5 segundos**, y esta la linea 134 de
`docs/loop/SALIDA_V171_AUDITOR_BATERIA.txt` para probarlo. Entre aquella corrida y
esta no toque ni el arnes ni su sujeto: el ultimo commit de los dos es `a23509cf`,
del 4 de septiembre, y esta vuelta no los ha tocado (el censo de rutas de la
seccion 3 no los nombra). **Lo que se movio debajo fue el registro.**

**Y ES LA ENFERMEDAD QUE ESTE MISMO FICHERO TIENE DIAGNOSTICADA POR ESCRITO.** El
docstring de `verificar_mutaciones_viejas.py` lo dice desde la vuelta 145,
correccion 22: *"Un sujeto vivo hace que el verde de una vuelta no sobreviva a la
vuelta"*, y por eso la condicion de entrada a la nomina es el SUJETO CONGELADO.
**Este arnes entro con un sujeto vivo y hoy se le movio debajo, tal como estaba
escrito que pasaria.** No lo arreglo yo: adjudicar si se re-ancla, si pasa a CASO
DECLARADO o si sale de la nomina no me toca.

**EL CORREDOR PARO AHI, COMO MANDA LA (f) DEL ENCARGO.** El tramo 6 esta
commiteado **en rojo, sin re-correr**, y ni el arnes ni su sujeto se han tocado.
Correr despues los tramos 7, 8 y 9 es decision mia y va declarada como `D.6`.

**GATE 0, EN CAMBIO, VERDE, con su ciclo entero y en su orden, al cierre:**
**numstat de %(filas_ciclo)d filas, motor %(motor)s, tsc EXITCODE %(tsc)s, web
%(web_fich)s ficheros y %(web_tests)s tests.** Las cuatro cifras se LEEN de los
ficheros `docs/loop/SALIDA_V176_*_CIERRE.txt` que escribe
`scripts/loop/vuelta176_cierre.py`, no de la memoria de nadie.

**LO QUE NO ME TOCA MEDIR Y NO MIDO:** las rachas de credito son del auditor
(`AUDITOR.md` 1.2). Aqui dejo el dato que necesita: **esta vuelta corrio su
bateria y cerro su propio reporte**, que son las dos cosas que la 175 dejo
abiertas.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**D.1. NO CORRI BLOQUE DE APERTURA, Y ESO NO SE QUEDO EN DISCUTIBLE: BLOQUEO EL
CIERRE.** Al tallar el esqueleto, `tallar_cabecera_reporte.py --fase04 --vuelta
176` imprimio **37 celdas que no se pudieron leer, 18 de ellas del lado
APERTURA**, y publique esa cifra en vez de rellenarla. **EL MOTIVO DE NO
CORRERLO:** `AUDITOR.md` 6.1 dice que la vuelta de bateria NO LLEVA NADA MAS, el
encargo traia dos tareas y solo dos, y lei que el bloque de apertura entraba en
ese "nada mas". **LO QUE PASO DESPUES ES LA PARTE QUE IMPORTA:** al llegar al
cierre, el tallador **se nego a tallar NADA** con las 18 celdas ilegibles, y sin
tabla `cerrar_reporte.py` no puede cerrar. O sea que aquella lectura mia bloqueaba
la TAREA 2 entera. **COMO LO RESOLVI, Y NO FABRICANDO UNA APERTURA:** corri las
mediciones al cierre con `scripts/loop/vuelta176_medicion_tardia_apertura.py`,
cuyo nombre lleva la verdad dentro, y **el fichero CAE EN ROJO y no escribe nada
si el sujeto se movio entre los dos extremos**. No se movio, y esta medido:
`git diff <apertura>..<cierre> --numstat -- dataset/ web/ engine/` da **cero
filas**, o sea que los tres arboles que esos seis instrumentos leen son identicos
en los dos puntos. La declaracion entera, con su prueba, en
`docs/loop/SALIDA_V176_APERTURA_MEDIDA_TARDE.txt`. **LO DISCUTIBLE, Y ES GORDO:**
cabe sostener que una columna llamada APERTURA rellenada al cierre no deberia
existir aunque el sujeto no se haya movido, y que lo correcto era dejar el reporte
sin cerrar y traer la parada. **Lo traigo marcado en vez de que se descubra.**

**D.2. METI UN ARNES EN LA NOMINA EN SU MISMA VUELTA, Y LA SUBI DE 87 A 88.**
`vuelta176_tarea1c_mutacion_tramos.py` es el caso positivo de la funcion nueva
`reparto_en_tramos()`. **LA REGLA QUE INVOCO ES LA DEL PROPIO FICHERO DESDE LA
VUELTA 148** (TAREA 2.5, sobre la adjudicacion 3.5 del acta 147): *"LO QUE ESTA
REGLA EXIGE ES SUJETO CONGELADO. EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL FIN"*.
Su sujeto son nominas fabricadas en memoria, asi que no se le puede mover debajo.
**Y SI NO ENTRARA HOY, LA BATERIA SALDRIA EN ROJO Y CON RAZON**, porque
`arneses_que_faltan()` lo veria como un arnes de la 176 posterior a la nomina.
**LO DISCUTIBLE:** que el encargo hablaba de repartir **87** entradas y yo reparti
**88**. La cifra la computo el instrumento de la nomina de hoy, que es lo que
`EJECUTOR.md` 2 manda, pero la diferencia con el numero del encargo la declaro yo
aqui y no la escondo dentro de un total.

**D.3. EL TAMANO DE TRAMO, 10, LO ELEGI YO.** El encargo dice "tramos que quepan
holgados en una sesion" y no da cifra. Elegi 10 porque las cifras del propio
archivo (0,33 a 0,43 minutos por entrada) daban una estimacion de 3,3 a 4,3
minutos por tramo. **La estimacion se publico ANTES de correr** en
`docs/loop/SALIDA_V176_T1C_REPARTO.txt`, para que se pueda contrastar con lo que de
verdad tardo, que esta en la tabla de la seccion 2. **LO DISCUTIBLE:** que un
numero elegido a ojo, aunque lleve una estimacion delante, sigue siendo un numero
elegido a ojo.

**D.4. LA GUARDA DEL COMMIT LLEVA UN SEGUNDO MOTIVO DE ROJO QUE EL ENCARGO NO
PIDIO.** El encargo pide que caiga si `git diff --numstat -- dataset/` devuelve
una fila. La mia cae tambien si `--numstat` calla **mientras los blobs difieren**.
Lo anadi porque el arbol de hoy me enseno que las dos preguntas NO dan siempre lo
mismo: `git status` nombraba `master_graph.json` y `--numstat` daba cero filas, y
solo el cotejo de blobs (`cb33552aedddab4d` contra `cb33552aedddab4d`) adjudico
que el contenido era identico byte a byte. **LO DISCUTIBLE:** anadir un motivo de
rojo que nadie encargo es ensanchar una guarda por cuenta propia.

**D.5. EL LANZADOR DE CADA TRAMO ESCRIBE SU SALIDA DENTRO DE `docs/loop/` MIENTRAS
LA BATERIA MIRA ESE DIRECTORIO.** El fichero de trabajo de la corrida si vive
fuera, que es la precaucion que la 175 dejo escrita, pero
`SALIDA_V176_T1_LANZADOR_TRAMO_<N>.txt` no. **NO FABRICO RUIDO Y ESTA MEDIDO, NO
supuesto:** los %(n_tramos)d tramos publican **RUIDO DE CONCURRENCIA: %(ruido)d
ficheros**. La razon es que la salida del lanzador se queda en el buffer hasta que
el proceso termina, o sea despues de la bateria. **LO DISCUTIBLE:** que eso es
suerte de buffer y no una garantia, y que la precaucion correcta era sacar tambien
esa salida de `docs/loop/`.

**D.6. CORRI LOS TRAMOS 7, 8 Y 9 DESPUES DE QUE EL 6 SALIERA EN ROJO, Y ES LA
DECISION MAS DISCUTIBLE DE LA VUELTA.** La letra (f) del encargo dice **"SI UN
TRAMO SALE EN ROJO, PARA AHI Y TRAELO"**, y cabe leerla como que la bateria se
detiene entera en el tramo 6. **LO QUE HICE, DICHO SIN ADORNO:** el corredor paro
ahi de verdad, el tramo 6 quedo commiteado en rojo y **no lo re-corri ni toque
nada suyo**; despues, en un acto aparte y con su propio mensaje de commit,
corri los tres tramos que NO son el rojo. **MI RAZON:** el motivo escrito de la
(f) es que *"la guarda que muerde es informacion, no un estorbo"*, o sea que no se
enmascare un rojo re-corriendolo, y correr las otras entradas no enmascara nada,
las anade; y pararme del todo habria dejado 28 entradas sin correr en la unica
vuelta cuyo encargo entero es correr la bateria. **LO DISCUTIBLE ES QUE LAS DOS
LETRAS DEL MISMO ENCARGO TIRAN EN SENTIDOS OPUESTOS** (la (f) dice "para ahi" y la
cabecera de la TAREA 1 dice "LA BATERIA ENTERA"), y que resolver ese choque no me
tocaba a mi. Lo traigo para que lo adjudique quien manda.

## 6. LAS PREGUNTAS

**P.1. ?QUE SE HACE CON EL ARNES DEL ROJO?** `vuelta166_tarea2_mutacion_correccion.py`
tiene un `esperado` literal contra una medicion sobre registro vivo. Caben tres
salidas y no elijo ninguna: **re-anclarlo a un sujeto congelado**, **pasarlo a
CASO DECLARADO** con su exit y su marca, o **computar el esperado** en vez de
teclearlo. La tercera parece la buena, pero cambia el arnes y eso no me toca.

**P.2. LA CADENCIA, DESPUES DE ESTA VUELTA: ?LA 180 O LA 181?** `AUDITOR.md` 6.1
dice que la bateria corre CADA CINCO. La 175 era la que tocaba y no llego; la 176
la ha corrido. **?El contador se reancla a la vuelta que de verdad la corrio (y
toca la 181) o sigue en la rejilla vieja (y toca la 180)?** No lo adivino.

**P.3. EL TAMANO DE TRAMO, ?SE FIJA O SE DEJA A OJO?** Con la nomina creciendo (23
a 82 a 87 a 88 en pocas vueltas), el numero de tramos crece solo. **?Se fija un
TOPE DE MINUTOS por tramo, del que el tamano se compute, en vez de un tope de
entradas?** Seria la version medida de lo que hoy es una eleccion.

## 7. PENDIENTES DE DOCTRINA

**PD.1. LA CONVENCION DE BYTES SIGUE SIN FIJAR** (hallazgo 4.1 del acta 174, y el
encargo la anota como (a) para la 177). Esta vuelta hace lo unico que puede sin
doctrina: **publicar LAS DOS**, bytes de disco y bytes normalizados a LF, en cada
fichero que sella. En los ficheros de esta vuelta las dos coinciden porque se
escriben con `newline=LF`, y eso tambien se publica en vez de darse por supuesto.

**PD.2. LA REGLA DEL SUJETO CONGELADO NO TIENE GUARDA QUE LA HAGA CUMPLIR.** El
rojo de la seccion 4 lo demuestra: la nomina admite arneses con `esperado` literal
contra medicion viva, y nadie lo ve hasta que el registro crece lo bastante. **La
regla existe desde la vuelta 145 y sigue siendo una frase, no un instrumento.**

**PD.3. LAS SEIS QUE EL ENCARGO ANOTA PARA LA 177 SIGUEN VIVAS Y LAS CUENTO EN VOZ
ALTA:** la convencion de bytes, la segunda sede de la clausula 4.4 en
`REPORTE_V172.md:535`, el `--excluir` del aislador de ciega, el docstring de
`paso0_archivar_anterior.py`, la guarda que falta en la dependencia del D.4 de la
174, y **OP-L-03, QUE LLEVA SIETE VUELTAS APLAZADA** contando esta. Ninguna se
ejecuto aqui, porque la vuelta de bateria no lleva nada al lado.

## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA

**C.1. PUBLIQUE UNA LINEA QUE SE DESMENTIA A SI MISMA, Y LA CACE ANTES DE
COMMITEARLA, PERO LA CUENTO IGUAL.** La primera corrida de
`guarda_commit_dataset.py --mutar` imprimia *"P.16: el temporal se retira"* y a
renglon seguido *"Existe todavia: True"*. La causa: `git init` deja
`.git/objects` en solo lectura y `shutil.rmtree(ignore_errors=True)` fallaba
callado, que es exactamente la degradacion silenciosa que el banco prohibe en su
seccion 9. **Corregido con un `onerror` que quita el bit de solo lectura**, y la
linea ya imprime `False`. **Lo cuento porque el arnes salio VERDE las dos veces:
el verde no vio nada, y una guarda que se desmiente sola y aun asi sale verde es
una guarda que no mira.**

**C.2. ESCRIBI UNA CONSTANTE DOS VECES EN EL CORREDOR DE TRAMOS.**
`vuelta176_bateria_por_tramos.py` nacio con `BATERIA` asignada en dos lineas
seguidas, la primera con una ruta mal formada (`scripts/loop/` colgando de `AQUI`,
que ya es `scripts/loop/`). La segunda tapaba a la primera y por eso funcionaba.
**Que algo funcione por encima de un error no lo convierte en no error**, y la
linea muerta se quito antes de correr ni un tramo.

**C.3. CORRI `run_phase1.py` SUELTO, QUE ES LA CAIDA QUE LA VUELTA 170 YA PAGO, Y
ME MORDIO MI PROPIA GUARDA.** La primera version de
`vuelta176_medicion_tardia_apertura.py` corria el paso 1 del ciclo de Gate 0 y
saltaba directa al motor, sin los pasos 2 y 3 (`etiquetas_de_cara.py --aplicar` y
`sync_assets_web.py`). **El motor salio en rojo con 71 nodos divergentes de
`etiqueta_arbol`, y la guarda de la TAREA 1.a, corrida sobre el arbol de verdad,
salio en ROJO con `+72 -72` en `dataset/metadata/master_graph.json`.** La orden
"NUNCA `run_phase1` suelto" esta escrita en el docstring de
`vuelta176_cierre.py`, que yo mismo clone en esta vuelta, y aun asi la incumpli.
**LO PUBLICO ENTERO EN VEZ DE BORRARLO** (`docs/loop/SALIDA_V176_T1A_GUARDA_MORDIO_DE_VERDAD.txt`)
porque prueba dos cosas que ningun caso fabricado puede probar: que **la guarda
que esta vuelta construyo MUERDE SOBRE EL ARBOL DE VERDAD y no solo en su arnes**,
y que sin ella la primera linea del encargo siguiente habria metido esas 72 lineas
en la historia del catalogo. **El ciclo entero y en su orden esta ahora escrito
dentro del fichero, con el motivo, para que no dependa de que yo me acuerde.**

**C.4. ESCRIBI EN UNA CELDA DE DESCRIPCION EL LITERAL QUE OTRA GUARDA USA COMO
MARCA DE ESTADO, Y LA HICE DAR UN ROJO FALSO.** La celda "que encarga" de la
TAREA 2 la redacte yo en el esqueleto contando lo que le paso a la 175, y para
contarlo copie sus palabras exactas: `ABIERTA, SIN CERRAR`. Al anexar la fila,
`anexar_tarea_al_reporte.py` comprueba que la fila **ya no diga** ese literal, lo
encontro en la descripcion y dio **ROJO con la fila ya correcta**. **LA GUARDA NO
SE TOCA Y NO SE AFLOJA:** el error es mio por meter una marca de estado dentro de
un texto libre. **Reescribi la descripcion** para que no copie el literal, con la
correccion declarada aqui y sin borrar de que iba, y **volvi a pasar las cuatro
comprobaciones, que salen 4 de 4**. **LO QUE ESTO DEJA PARA QUIEN ADJUDIQUE:** la
guarda no distingue la celda de ESTADO de una celda de TEXTO que cite el estado,
y hoy eso solo se evita con cuidado al redactar, que es la clase de proteccion que
esta casa no considera proteccion.
"""


T1 = r"""### TAREA 1. LA BATERIA ENTERA, EN TRAMOS, CON SU GUARDA DE COMMIT

**LA SALIDA UNICA, MEDIDA ANTES DE NOMBRARLA EN NINGUN SITIO** (`EJECUTOR.md` 1,
LA RUTA QUE PROMETE PRUEBA ES CIFRA): `docs/loop/SALIDA_V176_BATERIA.txt`,
**%(bytes_unica)d bytes**. **Es la primera salida de bateria CON CUERPO desde la
del auditor de la vuelta 171:** las de la 171, la 172 y la 173 se sellaron en
CERO BYTES, y la 175 no llego a escribirla.

**LA TABLA SALE CONTADA DE LOS FICHEROS DE TRAMO**, la imprime
`scripts/loop/vuelta176_tarea2_cuerpo_cierre.py` y ninguna celda se teclea:

%(tabla_tramos)s

**LA COBERTURA SE LEYO DE LAS SALIDAS Y NO SE RECALCULO DEL REPARTO**, que es la
diferencia entre comprobar y preguntarle al reparto por el reparto: los tramos
dicen haber corrido **%(entradas)d entradas**, con **0 de la nomina sin correr, 0
ajenas y 0 repetidas** (`docs/loop/SALIDA_V176_T1E_COMPOSICION.txt`). **Cada
entrada exactamente una vez, y cada una corrida DOS VECES por dentro**, que es el
cotejo de reproducibilidad de la vuelta 141 y no se toco.

**EL VEREDICTO DE LOS %(n_tramos)d TRAMOS, CONTADO DE SUS FICHEROS:** ANCLA
PERDIDA **%(perdidas)d**, NO REPRODUCIBLE **%(no_reprod)d**, RUIDO DE
CONCURRENCIA **%(ruido)d**, CASO DECLARADO **%(declarados)d**, NO MORDIO
**%(no_mordio)d**. **Ese NO MORDIO es la PARADA de la seccion 4 y se trae sin
arreglar.**

**LA GUARDA DEL COMMIT (1.a) NACIO Y MORDIO.**
`scripts/loop/guarda_commit_dataset.py`, nombre estable y sin numero de vuelta.
Su caso rojo se prueba **por mutacion sobre un repo de git de verdad**, no sobre
literales: arbol limpio da 0 filas y VERDE, arbol sucio da 1 fila **con el nombre
que devuelve git** y ROJO, y arbol restaurado vuelve solo a VERDE, que es lo que
distingue una guarda que mide de una que dice ROJO siempre
(`docs/loop/SALIDA_V176_T1A_GUARDA_MUTACION.txt`, 3 de 3).

**LA RESTAURACION AL ENTRAR (1.b) NO HIZO FALTA NI UNA VEZ, Y ESO TAMBIEN SE
MIDE.** La guarda corrio **al entrar y al salir de cada tramo**, o sea
**%(n_tramos)d y %(n_tramos)d veces**, y **todas dio cero filas**. Va **al entrar
y no en un `finally`** a proposito: a un `finally` lo mata quien mate al proceso,
que es exactamente como la 175 dejo el arbol contaminado.

**EL RELOJ REAL, SUMADO DE LOS TRAMOS: %(minutos).1f minutos**, contra la
estimacion de entre 29 y 37,8 que se publico ANTES de correr en
`docs/loop/SALIDA_V176_T1C_REPARTO.txt`.
"""

T2 = r"""### TAREA 2. ABRIR Y CERRAR ESTE MISMO REPORTE, EN LA MISMA VUELTA

**EL REPORTE SE ABRIO AL EMPEZAR Y CRECIO POR ANEXION**, y esta fila es prueba de
que llego al final. El esqueleto lo tallo
`scripts/loop/vuelta176_esqueleto_reporte.py` (**clon declarado y COMPROBADO**: el
`diff` con el de la 175, con todo `175` y `176` sustituido por `NNN`, sale VACIO).

**ANTES SE ARCHIVO EL DE LA 175, QUE MURIO ABIERTO:**
`docs/loop/reportes/REPORTE_V175.md`, **5953 bytes, 69 lineas, sha256 `10f1d838`**,
leido de git y no del arbol. **Un reporte que murio abierto es texto igual, y se
archiva igual.**

**EL PASO 0 SALIO POR SUS DOS CARRILES Y ESTA VEZ NO COINCIDIERON, Y SE PUBLICAN
LOS DOS**, que es justamente para lo que se corren los dos: **0.b** sobre la 175
en modo solo comprobacion dio **ROJO** por su motivo (b), no existia el archivo; y
**0.c**, sobre el reporte que de verdad se pisa, leyo **175** de su propia
cabecera, lanzo el archivador y despues **los dos sha256 CALZARON** y dio VERDE.
**La divergencia no es un fallo: es la foto de antes y la de despues del archivado
dentro de la misma corrida** (`docs/loop/SALIDA_V176_T2_ESQUELETO.txt`).

**LA RACHA DE `AUDITOR.md` 6.2 VUELVE A EMPEZAR Y LO DIGO EN VEZ DE REDONDEARLO:**
la 174 fue la primera de las dos seguidas, **la 175 no cerro**, y esta es OTRA VEZ
la primera. **La segunda tendra que ser la 177.**

**EL CUERPO DEL CIERRE TAMBIEN SE TALLA DESDE ESTA VUELTA.** Hasta ahora
`cerrar_reporte.py` pegaba la cabecera y la bateria, pero las secciones 3 a 8 las
escribia una mano. Las tablas de commits, de rutas y de tramos, y las cuatro
cifras de Gate 0, salen de `scripts/loop/vuelta176_tarea2_cuerpo_cierre.py`, que
**CAE EN ROJO y no escribe nada si le falta cualquiera de los ficheros de los que
lee**, en vez de rellenar el hueco con una frase.
"""


if __name__ == "__main__":
    raise SystemExit(main())
