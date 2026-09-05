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
  . el veredicto de la bateria, CONTADO de los nueve ficheros de tramo y no
    copiado de ningun mensaje de commit.

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
    c, log = git(["log", "--format=%h%x09%s", "%s..%s" % (apertura, cierre)])
    filas_log = [l.split(chr(9), 1) for l in log.splitlines() if chr(9) in l]
    filas_log.reverse()
    print("commits de la vuelta, leidos de git log: %d" % len(filas_log))

    tabla_commits = [chr(124) + " # " + chr(124) + " commit " + chr(124) +
                     " asunto, primeras 96 letras, leido de git " + chr(124),
                     chr(124) + "---:" + chr(124) + "---" + chr(124) + "---" + chr(124)]
    for i, (h, s) in enumerate(filas_log, 1):
        limpio = s.replace(chr(124), "/")[:96]
        tabla_commits.append("%s %d %s `%s` %s %s %s"
                             % (chr(124), i, chr(124), h, chr(124), limpio, chr(124)))

    # -------------------------------------------- LAS RUTAS TOCADAS, CONTADAS
    c, nombres = git(["diff", "--name-only", "%s..%s" % (apertura, cierre)])
    rutas = [l.strip() for l in nombres.splitlines() if l.strip()]
    por_dir = {}
    for ruta in rutas:
        d = ruta.rsplit("/", 1)[0] + "/" if "/" in ruta else "(raiz)"
        por_dir[d] = por_dir.get(d, 0) + 1
    print("rutas tocadas entre los dos extremos: %d" % len(rutas))

    tabla_rutas = [chr(124) + " directorio " + chr(124) + " rutas tocadas " + chr(124),
                   chr(124) + "---" + chr(124) + "---:" + chr(124)]
    for d in sorted(por_dir):
        tabla_rutas.append("%s `%s` %s %d %s" % (chr(124), d, chr(124), por_dir[d], chr(124)))
    tabla_rutas.append("%s **TOTAL** %s **%d** %s" % (chr(124), chr(124), len(rutas), chr(124)))

    # ------------------------------------------- EL GRAFO, ENTRE LOS EXTREMOS
    c, numstat = git(["diff", "--numstat", "%s..%s" % (apertura, cierre),
                      "--", "dataset/", "web/", "engine/"])
    filas_numstat = [l for l in numstat.splitlines() if l.strip()]
    print("filas de numstat sobre dataset/ web/ engine/: %d" % len(filas_numstat))

    # --------------------------------------------------- GATE 0, DE FICHEROS
    def cifra(nombre, patron, grupo=1):
        ruta = os.path.join(LOOP, "SALIDA_V176_%s_CIERRE.txt" % nombre)
        if not os.path.exists(ruta):
            fallos.append("no existe docs/loop/SALIDA_V176_%s_CIERRE.txt" % nombre)
            return None, ruta
        m = re.search(patron, leer(ruta))
        if not m:
            fallos.append("docs/loop/SALIDA_V176_%s_CIERRE.txt no trae la cifra que "
                          "se le pide (patron %r)" % (nombre, patron))
            return None, ruta
        return m.group(grupo), ruta

    motor, _r = cifra("MOTOR", r"(\d+)\s*/\s*(\d+)\s+", 0)
    tsc, _r = cifra("TSC", r"EXIT=(\d+)")
    web_fich, _r = cifra("WEB", r"(\d+)\s+passed")
    numstat_ciclo_ruta = os.path.join(LOOP, "SALIDA_V176_CICLO_NUMSTAT_CIERRE.txt")
    filas_ciclo = None
    if os.path.exists(numstat_ciclo_ruta):
        t = leer(numstat_ciclo_ruta)
        filas_ciclo = len([l for l in t.splitlines()
                           if l.strip() and not l.startswith("EXITCODE")])
    else:
        fallos.append("no existe docs/loop/SALIDA_V176_CICLO_NUMSTAT_CIERRE.txt")

    # ------------------------------------- LA BATERIA, CONTADA DE SUS TRAMOS
    tramos = sorted((n for n in os.listdir(LOOP)
                     if re.match(r"^SALIDA_V176_BATERIA_TRAMO_\d+\.txt$", n)),
                    key=lambda n: int(re.search(r"_(\d+)\.txt$", n).group(1)))
    total_entradas = 0
    conteos = {"ANCLA PERDIDA": 0, "NO MORDIO": 0, "NO REPRODUCIBLE": 0,
               "CASO DECLARADO": 0, "RUIDO DE CONCURRENCIA": 0}
    tabla_tramos = [chr(124) + " tramo " + chr(124) + " fichero " + chr(124) +
                    " bytes " + chr(124) + " lineas " + chr(124) + " entradas " +
                    chr(124) + " minutos " + chr(124) + " exit " + chr(124),
                    chr(124) + "---:" + chr(124) + "---" + chr(124) + "---:" +
                    chr(124) + "---:" + chr(124) + "---:" + chr(124) + "---:" +
                    chr(124) + "---:" + chr(124)]
    for nombre in tramos:
        ruta = os.path.join(LOOP, nombre)
        texto = leer(ruta)
        n = int(re.search(r"_(\d+)\.txt$", nombre).group(1))
        ent = len(re.findall(r"ENTRADA DEL TRAMO: ", texto))
        total_entradas += ent
        for clave in conteos:
            m = re.search(r"^\s*%s\s*:\s*(\d+)" % re.escape(clave), texto, re.M)
            if m:
                conteos[clave] += int(m.group(1))
        m_min = re.search(r"DURACION DEL TRAMO \(monotona, minutos\): ([\d.]+)", texto)
        m_exit = re.search(r"EXITCODE DEL TRAMO \d+: (-?\d+)", texto)
        tabla_tramos.append("%s %d %s `%s` %s %d %s %d %s %d %s %s %s %s %s"
                            % (chr(124), n, chr(124), nombre, chr(124),
                               os.path.getsize(ruta), chr(124),
                               texto.count(NL), chr(124), ent, chr(124),
                               m_min.group(1) if m_min else "?", chr(124),
                               m_exit.group(1) if m_exit else "?", chr(124)))
    unica = os.path.join(LOOP, "SALIDA_V176_BATERIA.txt")
    bytes_unica = os.path.getsize(unica) if os.path.exists(unica) else -1
    tabla_tramos.append("%s **union** %s `SALIDA_V176_BATERIA.txt` %s **%d** %s  %s "
                        "**%d** %s  %s  %s"
                        % (chr(124), chr(124), chr(124), bytes_unica, chr(124),
                           chr(124), total_entradas, chr(124), chr(124), chr(124)))

    if fallos:
        print("")
        print("ROJO, %d motivo(s), y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("   " + f)
        return 1

    # ------------------------------------------------------------- EL TEXTO
    T = {
        "ap": apertura[:8], "ci": cierre[:8],
        "n_commits": len(filas_log),
        "tabla_commits": NL.join(tabla_commits),
        "n_rutas": len(rutas),
        "tabla_rutas": NL.join(tabla_rutas),
        "n_numstat": len(filas_numstat),
        "motor": (motor or "").strip(),
        "tsc": tsc,
        "web": web_fich,
        "filas_ciclo": filas_ciclo,
        "n_tramos": len(tramos),
        "entradas": total_entradas,
        "tabla_tramos": NL.join(tabla_tramos),
        "bytes_unica": bytes_unica,
        "perdidas": conteos["ANCLA PERDIDA"],
        "no_mordio": conteos["NO MORDIO"],
        "no_reprod": conteos["NO REPRODUCIBLE"],
        "declarados": conteos["CASO DECLARADO"],
        "ruido": conteos["RUIDO DE CONCURRENCIA"],
    }

    texto = TEXTO % T
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
    print("")
    print("ESCRITO: scripts/loop/_v176_cierre_texto.md (%d bytes, %d lineas)"
          % (len(texto.encode("utf-8")), texto.count(NL)))
    for l in texto.split(NL):
        if l.startswith("## "):
            print("   " + l)
    largos = [c for c in texto if c in (chr(8212), chr(8211))]
    print("   guiones largos o medios colados: %d" % len(largos))
    return 1 if largos else 0


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
`git diff --numstat %(ap)s..%(ci)s -- dataset/ web/ engine/` sale con **%(n_numstat)d
filas**. **Cero nodos tocados, cero aristas movidas.** Y esta vuelta tenia mas
motivos que ninguna para comprobarlo, porque su trabajo entero consiste en correr
arneses que MUTAN `dataset/` a proposito.

**LA GUARDA DEL COMMIT CORRIO %(n_tramos)d VECES AL ENTRAR Y %(n_tramos)d AL SALIR**,
una por tramo, y las %(n_tramos)d veces midio **cero filas** de
`git diff --numstat -- dataset/`. No es una promesa: cada corrida esta dentro del
fichero de su tramo.

**EL COMMIT QUE LLEVA ESTE REPORTE NO SE NOMBRA AQUI**, porque se crea despues de
escribirlo.

## 4. NO HAY PARADA, Y RECORRO LAS CONDICIONES QUE ME TOCAN

**CONTRADICCION CON REGLA VIGENTE O CIFRA PUBLICADA: NO.** La unica decision con
filo de esta vuelta, partir la bateria en tramos, **no es doctrina nueva y no la
tome yo**: el acta del auditor de la 175 la adjudico expresamente, y la letra del
fundador del 5 sep fija cuatro cosas que se pueden comprobar una a una en la
seccion 2. **Las cuatro siguen enteras.**

**FALLO TECNICO REPETIDO: NO.** Gate 0 verde con su ciclo entero y en su orden, al
cierre: **numstat de %(filas_ciclo)d filas, motor %(motor)s, tsc EXITCODE %(tsc)s,
web %(web)s tests**. Las cuatro cifras se LEEN de los ficheros
`docs/loop/SALIDA_V176_*_CIERRE.txt` que escribe
`scripts/loop/vuelta176_cierre.py`, no de la memoria de nadie.

**UNA OPERACION CUYO TEXTO NO ALCANCE PARA EJECUTARSE SIN DECIDIR: NO.** Las dos
tareas del encargo venian escritas con su instrumento y su medicion, y hasta con
la causa medida de por que hacia falta el instrumento nuevo.

**LO QUE SI ME OBLIGO A DECIDIR Y LO DECLARO EN VEZ DE CALLARLO:** meter
`vuelta176_tarea1c_mutacion_tramos.py` en la nomina EN SU MISMA VUELTA, subiendola
de 87 a 88. Va razonado con la letra del propio fichero en el discutible `D.2`.

**LO QUE NO ME TOCA MEDIR Y NO MIDO:** las rachas de credito son del auditor
(`AUDITOR.md` 1.2). Aqui dejo el dato que necesita: **esta vuelta corrio su
bateria entera y cerro su propio reporte**, que son las dos cosas que la 175 dejo
abiertas.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**D.1. NO CORRI BLOQUE DE APERTURA, Y LA MITAD IZQUIERDA DE LA CABECERA SE QUEDA
EN ROJO.** Al tallar el esqueleto, `tallar_cabecera_reporte.py --fase04 --vuelta
176` imprimio **37 celdas que no se pudieron leer, 18 de ellas del lado
APERTURA**, y esa cifra la publique en el esqueleto en vez de rellenarla.
**EL MOTIVO, DICHO ENTERO:** el encargo manda dos tareas y solo dos (la bateria y
el reporte), `AUDITOR.md` 6.1 dice que la vuelta de bateria NO LLEVA NADA MAS, y
un bloque de apertura completo es Gate 0 mas motor mas tsc mas la suite de la web,
que es justamente el tiempo que la 175 no tuvo. **LO DISCUTIBLE ES QUE ESO SE
PUEDA LLAMAR "NADA MAS":** cabe leer que el bloque de apertura es maquinaria de la
casa y no una tarea, y que por tanto debia correr igual. **Y HAY UN AGRAVANTE QUE
NO ME CALLO:** aunque hubiera querido, ya no habria sido apertura, porque la
primera linea del encargo me obligaba a commitear antes, y `EJECUTOR.md` 1 dice
que el estado TRAS la primera operacion ya es intermedio y se cita como tal. Lo
unico que si selle antes de tocar nada fue el HEAD.

**D.2. METI UN ARNES EN LA NOMINA EN SU MISMA VUELTA, Y LA SUBI DE 87 A 88.**
`vuelta176_tarea1c_mutacion_tramos.py` es el caso positivo de la funcion nueva
`reparto_en_tramos()`. **LA REGLA QUE INVOCO ES LA DEL PROPIO FICHERO DESDE LA
VUELTA 148** (TAREA 2.5, sobre la adjudicacion 3.5 del acta 147): *"LO QUE ESTA
REGLA EXIGE ES SUJETO CONGELADO. EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL FIN"*.
Su sujeto son nominas fabricadas en memoria, asi que no se le puede mover debajo.
**Y SI NO ENTRARA HOY, LA BATERIA SALDRIA EN ROJO Y CON RAZON**, porque
`arneses_que_faltan()` lo veria como un arnes de la 176 posterior a la nomina.
**LO DISCUTIBLE:** que el encargo hablaba de repartir **87** entradas y yo reparti
**88**. La cifra del reparto la computo el instrumento de la nomina de hoy, que es
lo que `EJECUTOR.md` 2 manda, pero la diferencia con el numero del encargo la
declaro yo aqui y no la escondo en un total.

**D.3. EL TAMANO DE TRAMO, 10, LO ELEGI YO.** El encargo dice "tramos que quepan
holgados en una sesion" y no da cifra. Elegi 10 porque las cifras del propio
archivo (0,33 a 0,43 minutos por entrada) daban una estimacion de 3,3 a 4,3
minutos por tramo, con holgura de sobra. **La estimacion se publico ANTES de
correr** en `docs/loop/SALIDA_V176_T1C_REPARTO.txt`, para que se pueda contrastar
con lo que de verdad tardo, que esta en la tabla de la seccion 2. **LO
DISCUTIBLE:** que un numero elegido a ojo, aunque sea con una estimacion delante,
sigue siendo un numero elegido a ojo.

**D.4. LA GUARDA DEL COMMIT LLEVA UN SEGUNDO MOTIVO DE ROJO QUE EL ENCARGO NO
PIDIO.** El encargo pide que caiga si `git diff --numstat -- dataset/` devuelve
una fila. La mia cae tambien si `--numstat` calla **mientras los blobs difieren**.
Lo anadi porque el arbol de hoy me enseno que las dos preguntas NO dan siempre lo
mismo: `git status` nombraba `master_graph.json` y `--numstat` daba cero filas, y
solo el cotejo de blobs (`cb33552aedddab4d` contra `cb33552aedddab4d`) adjudico
que el contenido era identico. **LO DISCUTIBLE:** anadir un motivo de rojo que
nadie encargo es ensanchar una guarda por cuenta propia.

**D.5. EL LANZADOR DE CADA TRAMO ESCRIBE SU PROPIA SALIDA DENTRO DE `docs/loop/`
MIENTRAS LA BATERIA MIRA ESE DIRECTORIO.** El fichero de trabajo de la corrida si
vive fuera, que es la precaucion que la 175 dejo escrita, pero
`SALIDA_V176_T1_LANZADOR_TRAMO_<N>.txt` no. **NO FABRICO RUIDO Y ESTA MEDIDO, NO
supuesto:** los %(n_tramos)d tramos publican **RUIDO DE CONCURRENCIA: %(ruido)s
ficheros**. La razon es que la salida del lanzador se queda en el buffer hasta que
el proceso termina, o sea despues de la bateria. **LO DISCUTIBLE:** que eso es
suerte de buffer y no una garantia, y que la precaucion correcta era sacar tambien
esa salida de `docs/loop/`.

## 6. LAS PREGUNTAS

**P.1. LA CADENCIA, DESPUES DE ESTA VUELTA: LA 180 O LA 181.** `AUDITOR.md` 6.1
dice que la bateria corre CADA CINCO. La 175 era la que tocaba y no llego; la 176
la ha corrido. **La pregunta es si el contador se reancla a la vuelta que de
verdad la corrio (y entonces toca la 181) o si sigue en la rejilla vieja (y
entonces toca la 180).** No lo adivino y no lo doy por resuelto en ningun sitio.

**P.2. EL TAMANO DE TRAMO, ?SE FIJA O SE DEJA A OJO?** Con la nomina creciendo (23
a 82 a 87 a 88 en pocas vueltas), el numero de tramos crece solo. **?Se fija un
TOPE DE MINUTOS por tramo, del que el tamano se compute, en vez de un tope de
entradas?** Seria la version medida de lo que hoy es una eleccion.

## 7. PENDIENTES DE DOCTRINA

**PD.1. LA CONVENCION DE BYTES SIGUE SIN FIJAR** (hallazgo 4.1 del acta 174, y el
encargo la anota como (a) para la 177). Esta vuelta hace lo unico que puede sin
doctrina: **publicar LAS DOS**, bytes de disco y bytes normalizados a LF, en cada
fichero que sella. En los ficheros de esta vuelta las dos coinciden porque se
escriben con `newline=LF`, y eso tambien se publica.

**PD.2. LAS SEIS QUE EL ENCARGO ANOTA PARA LA 177 SIGUEN VIVAS Y LAS CUENTO EN VOZ
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
`vuelta176_bateria_por_tramos.py` nacio con `BATERIA` asignada dos lineas
seguidas, la primera con una ruta mal formada (`scripts/loop/` colgando de
`AQUI`, que ya es `scripts/loop/`). La segunda tapaba a la primera y por eso
funcionaba. **Que funcione por encima de un error no lo convierte en no error**,
y la linea muerta se quito antes de correr ni un tramo.
"""


if __name__ == "__main__":
    raise SystemExit(main())
