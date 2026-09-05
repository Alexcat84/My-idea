r"""vuelta180_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA
VUELTA 180, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS CINCO TAREAS ENCARGADAS.

CLON DECLARADO de scripts/loop/vuelta179_esqueleto_reporte.py. Lo que se toca a
mano son las CINCO filas de tarea, que son las de ESTE encargo, y los parrafos de
prosa que hablan del estado del bucle. La maquina no se toca en ninguna linea
salvo el numero de vuelta.

Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA: el cotejo lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte, que es
obligatorio desde la vuelta 178 por el docstring de aquel fichero. Este texto NO
publica ningun resultado de diff.

DE DONDE VIENE ESA CAUTELA, Y NO SE BORRA DE QUE IBA: la CAIDA DE REPORTE 1 del
acta 176 seccion 5. El esqueleto de la 176 publicaba en su docstring que el
`diff` con `NNN` sustituido "SALE VACIO"; el auditor lo corrio y salieron 58
lineas, 33 de ellas de la maquina, aunque de esas 33 las SENTENCIAS DE CODIGO
eran 1 y los LITERALES DE TEXTO 32 medidos por el instrumento. El instrumento
que lo mide, `scripts/loop/cotejar_clon_declarado.py`, NACIO EN LA TAREA 1.d DE
LA VUELTA 177 y ya trae su CUARTO veredicto, EL ARBOL DE SINTAXIS, desde la 178.
Su salida sobre ESTE fichero se pega en el reporte.

LA MAQUINA NO CAMBIA EN NADA SALVO EL NUMERO DE VUELTA: el paso 0 endurecido que
estreno la 174 se conserva entero. Esa frase SI es una afirmacion sobre la
maquina, y por eso NO se publica como comprobada aqui tampoco: la comprueba el
instrumento, no este texto.

QUE ES ESE PASO 0 ENDURECIDO, dicho otra vez para que este fichero se entienda
solo: NO PREGUNTA POR `VUELTA - 1`, PREGUNTA POR EL REPORTE QUE DE VERDAD VA A
PISAR, Y ESE NUMERO SE LEE DEL PROPIO FICHERO con la funcion pura
`vuelta_del_reporte_del_arbol()`. En esta vuelta las dos preguntas coinciden (el
arbol trae el reporte de la 179 y `VUELTA - 1` es 179), y precisamente por eso el
fichero corre LAS DOS y publica lo que salga de cada una: una guarda que solo se
mira cuando difiere no se puede auditar el dia que difiera. Y LA TAREA 4.a DE
ESTA MISMA VUELTA fabrica el caso donde NO coinciden, que es lo que faltaba.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA: `vuelta_del_reporte_del_arbol`
esta copiada de `vuelta174_esqueleto_reporte.py` en vez de importada. Importarla
crearia una dependencia nueva sobre un fichero numerado sin nada que avise si
alguien lo borra por viejo. ESO YA NO ES UN PENDIENTE: la TAREA 4.b de esta
vuelta escribe la guarda que CAE EN ROJO nombrando la fuente del clon si el
fichero del que se clono desaparece. Se clona, se declara, se guarda, y el arnes
de la funcion original (`scripts/loop/vuelta174_tarea1b_mutacion_esqueleto.py`)
sigue apuntando a su sujeto de siempre.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 180 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
`git rev-parse --abbrev-ref HEAD`; commit del acta de la vuelta anterior por las
DOS formas del titulo y en las DOS pasadas de `TALLADOR.buscar_acta`; HEAD de
apertura leido de docs/loop/SALIDA_V180_HEAD_APERTURA.txt, sellado antes de la
primera operacion; commit de nacimiento del bloque de apertura por
`git log --diff-filter=A`. Si alguno no se puede leer o es ambiguo, el esqueleto
CAE EN ROJO y no escribe nada: no inventa un hash.

USO:
  python scripts/loop/vuelta180_esqueleto_reporte.py
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paso0_archivar_anterior as PASO0   # noqa: E402
import guarda_de_la_fuente_del_clon as CLON   # noqa: E402
import tallar_cabecera_reporte as TALLADOR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = 180
# DE DONDE SE CLONO LA FUNCION PURA DE ABAJO, DECLARADO AQUI PARA QUE LA GUARDA
# DE LA 4.b PUEDA MIRARLO (vuelta 180, TAREA 4.b).
FUENTE_DEL_CLON = "scripts/loop/vuelta174_esqueleto_reporte.py"
FUNCION_CLONADA = "vuelta_del_reporte_del_arbol"
PATRONES_ACTA = [
    re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR" % (VUELTA - 1)),
    re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA %d" % (VUELTA - 1)),
]
PATRON_ACTA = "ACTA DE LA VUELTA %d DEL AUDITOR o ACTA DEL AUDITOR, VUELTA %d" % (
    VUELTA - 1, VUELTA - 1)

TAREAS = [
    ("1", 'LOS REGISTROS Y LA ETIQUETA DE FUENTE, Y ES BLOQUEANTE. (a) El acta del auditor de la vuelta 179 vive en `docs/loop/ACTA_AUDITOR.md` y NO levanta ninguna caida contra la 179: la racha de reporte vuelve a CERO, la de cifra publicada sigue en CERO y no hay correccion declarada que arrastrar. (b) LA ETIQUETA DE FUENTE, ARREGLADA, y eso LEVANTA LA PARADA DE LA 3.f DE LA 179: `clases_por_par()` LEE LA VUELTA DE LA FILA DEL REGISTRO en vez del literal `docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)` clavado, con `sha256` de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y de `docs/plan/OP_L_03_LECTURAS.jsonl` ANTES y DESPUES dentro del propio instrumento y los CUATRO publicados, con `vuelta179_tarea3_etiqueta_de_fuente.py` re-corrido y las DOS mediciones al lado (la de antes y la de despues, y la de despues en CERO falsos o se para), con `vuelta178_tarea3_anotar_triangulos.py` re-corrido y el total de triangulos y de lados sin moverse, y con su caso positivo por mutacion sobre un registro fabricado de dos vueltas distintas'),
    ("2", 'EL SUJETO CONGELADO, RESUELTO Y CABLEADO, Y ES LA QUE LIMPIA LA PISTA DE LA 181. El orden es: los trece declaran, los cuatro congelan, y SOLO ENTONCES se cablea. (a) LOS TRECE QUE NO ABREN NADA VIVO DECLARAN SU SUJETO, once `LO NOMBRA SIN ABRIRLO` y dos `ABRE UN SUJETO YA CLAVADO`, una linea por arnes con el literal que la guarda busca y NINGUNA otra linea tocada, comprobado con `git diff --numstat` sobre `scripts/loop/` publicando las lineas anadidas por fichero. (b) LOS CUATRO QUE SI ABREN, CONGELADOS DE VERDAD, cada uno con que abria, que abre ahora y la prueba de que su resultado ya no se mueve. (c) Y SOLO ENTONCES EL CABLEADO al rojo global de la bateria, con la cifra de antes y su corte pegado y la de despues, que TIENE QUE DAR 0 o no se cablea. (d) NADA SE PODA DE LA NOMINA: todo arnes que esta vuelta escriba entra en `verificar_mutaciones_viejas.py` con la cuenta entera y la resta comprobada, antes de la 181'),
    ("3", 'EL CORTE, CABLEADO DONDE TODAVIA FALTA. El hallazgo es del fundador y esta medido en la seccion 6 del acta 179: la tabla de tramos de la 2.a de la 179 esta contada de su fichero y sus cifras eran verdad, pero LE FALTA EL CORTE, y sin corte no hay manera de saber cual mira que. Se cablea el sello de `sello_de_corte()` DONDE SE GENERA LA TABLA DE TRAMOS de `backlog_l03_resuelto.py`, no en una frase del reporte, por `banco 9.21` y el punto 7.2 del acta 178. Y SE BARRE EL RESTO: la lista de toda cifra de ese instrumento y de `vuelta179_tarea2_cobertura_final.py` que pueda moverse dentro de una vuelta, diciendo cuales llevan corte y cuales no, y las que no lo lleven lo llevan al terminar. Con su caso positivo por mutacion: dos cortes distintos con la misma cifra no se confunden, y la misma cifra con dos cortes distintos tampoco'),
    ("4", 'LAS DOS PENDIENTES BARATAS QUE YA LLEVAN VUELTAS SUBIENDO, LAS DOS TEXTO QUE MIENTE SOBRE SU PROPIA MAQUINA. (a) EL DOCSTRING DE `scripts/loop/paso0_archivar_anterior.py`, que sigue hablando de LA VUELTA ANTERIOR cuando la maquina ya pregunta por EL REPORTE QUE VA A PISAR: se arregla, se publican la linea vieja y la nueva sin borrar la vieja del reporte, y SE ESCRIBE LA GUARDA QUE HACE VISIBLE LA DIFERENCIA, un caso fabricado donde las dos preguntas NO coinciden y que demuestra que la maquina responde a la buena. (b) LA GUARDA QUE FALTA EN LA DEPENDENCIA DEL `D.4` DE LA 174: el esqueleto CLONA `vuelta_del_reporte_del_arbol()` en vez de importarla y nada avisa si el fichero del que se clono desaparece; la guarda CAE EN ROJO nombrandolo, con su caso positivo por mutacion sobre una ruta fabricada que no existe'),
    ("5", 'EL BACKLOG DE `OP-L-02`, MEDIDO Y NO LEIDO, CON LA MISMA VARA RESUELTA QUE CERRO `OP-L-03`. Se corre el instrumento viejo de `OP-L-02` por dentro y sin citarlo de memoria y se publican LOS PARES QUE DA; se le pone encima el resolutor de `P.1` y se publican LOS PARES REALES, o sea los que no estan ya en el archivo tras resolver a nodo vivo; LAS DOS COLUMNAS VAN LAS DOS Y LA VIEJA NO SE BORRA (`banco 9.10`); el reparto por tramo va CON SU CORTE PEGADO por la TAREA 3 de este mismo encargo; y LOS DOS CAMINOS TIENEN QUE CALZAR en todos los actos medidos o se publica donde y se para. LO QUE NO SE HACE: no se lee ningun par, no se escribe ningun veredicto, no se toca el marcador, no se toca el estado de ninguna ficha (`EJECUTOR.md` 4, modo de cierre) y NO SE TOCAN LOS CINCO PARES DE SALES ROADMAP, que `docs/plan/LECTURAS_DIRIGIDAS.md` deja como decision revocable del fundador: se nombran y se dejan'),
]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


def vuelta_del_reporte_del_arbol(texto):
    """EL NUMERO DE VUELTA DEL REPORTE QUE SE VA A PISAR, LEIDO DE SU PROPIA
    CABECERA. Devuelve un entero, o None si la primera linea no es una cabecera
    de reporte. PURA: recibe el texto y no lee ni escribe nada.

    CLON DECLARADO de la funcion del mismo nombre de
    scripts/loop/vuelta174_esqueleto_reporte.py, byte a byte en su cuerpo. Su
    arnes de mutacion, vuelta174_tarea1b_mutacion_esqueleto.py, sigue apuntando
    al original y NO se re-apunta aqui."""
    if not texto:
        return None
    primera = texto.replace(chr(13) + chr(10), chr(10)).split(chr(10), 1)[0]
    m = re.match(r"^#\s*REPORTE DE LA VUELTA\s+(\d+)\b", primera)
    return int(m.group(1)) if m else None


if __name__ != "__main__":
    # Importable sin que corra nada.
    pass
else:
    sys.stdout.reconfigure(encoding="utf-8")

    # ---------------------------------------------- PASO 0.0, LA FUENTE DEL CLON
    # LA GUARDA QUE FALTABA DESDE LA 174 (vuelta 180, TAREA 4.b). Este fichero
    # CLONA vuelta_del_reporte_del_arbol() de vuelta174_esqueleto_reporte.py, y
    # hasta hoy NADA avisaba si ese fichero desaparecia. Va ANTES del paso 0
    # porque, si la fuente no esta, lo que hay que arreglar no es el reporte.
    ok_clon, informe_clon = CLON.exigir_fuente_del_clon(
        FUENTE_DEL_CLON, FUNCION_CLONADA)
    for l in informe_clon:
        print(l)
    print("")
    if not ok_clon:
        print("ROJO: el esqueleto NO escribe. La fuente del clon no esta en su sitio.")
        sys.exit(1)

    # ------------------------------------------------------------- PASO 0
    ruta = os.path.join(LOOP, "REPORTE.md")
    texto_a_pisar = io.open(ruta, encoding="utf-8").read() if os.path.exists(ruta) else ""
    n_arbol = vuelta_del_reporte_del_arbol(texto_a_pisar)
    print("PASO 0.a. QUE REPORTE HAY EN EL ARBOL, LEIDO DE SU PROPIA CABECERA")
    print("   docs/loop/REPORTE.md -> %d bytes" % len(texto_a_pisar.encode("utf-8")))
    print("   primera linea: %s" % texto_a_pisar.split(chr(10), 1)[0][:88])
    print("   vuelta LEIDA (no tecleada): %s" % n_arbol)
    if n_arbol is None:
        print("ROJO: el REPORTE.md del arbol no lleva cabecera de reporte. No se")
        print("      puede saber que se destruiria, y por eso no se escribe nada.")
        sys.exit(1)
    print("   coincide con VUELTA - 1 (%d): %s"
          % (VUELTA - 1, "SI" if n_arbol == VUELTA - 1 else "NO"))
    print("")

    print("PASO 0.b. LA GUARDA SOBRE LA VUELTA ANTERIOR (%d), PUBLICADA SALGA LO"
          % (VUELTA - 1))
    print("   QUE SALGA, EN MODO SOLO COMPROBACION Y SIN LANZAR EL ARCHIVADOR")
    ok_ant, informe_ant = PASO0.exigir_archivado(VUELTA - 1, ejecutar_archivador=False)
    for l in informe_ant:
        print("   " + l)
    print("   VEREDICTO SOBRE LA %d: %s" % (VUELTA - 1, "VERDE" if ok_ant else "ROJO"))
    c, toco = git(["log", "--format=%h", "-6", "--", "docs/loop/REPORTE.md"])
    print("   los seis ultimos commits que TOCAN docs/loop/REPORTE.md: %s"
          % (", ".join(toco.split()) if toco.strip() else "(ninguno)"))
    print("")

    print("PASO 0.c. LA GUARDA SOBRE EL REPORTE QUE DE VERDAD SE VA A PISAR (%d)"
          % n_arbol)
    ok, informe = PASO0.exigir_archivado(n_arbol)
    for l in informe:
        print("   " + l)
    print("")
    if not ok:
        print("ROJO: el esqueleto NO escribe. El reporte anterior no esta a salvo.")
        sys.exit(1)

    fallos = []

    c, rama = git(["rev-parse", "--abbrev-ref", "HEAD"])
    if c != 0 or not rama:
        fallos.append("no se pudo leer la rama de git")

    c, log = git(["log", "--format=%H%x09%s", "-400"])
    filas_log = [l.split("\t", 1) for l in log.splitlines() if "\t" in l]
    actas, anclado = TALLADOR.buscar_acta(filas_log, PATRONES_ACTA)
    if not anclado and actas:
        print("DECLARADO: el commit del acta %d NO empieza por su titulo; se localiza"
              % (VUELTA - 1))
        print("   por busqueda NO ANCLADA, con exactamente 1 acierto. Su asunto real,")
        print("   con el ruido y todo, es el que se publica en la identidad.")
    if len(actas) != 1:
        fallos.append("commits con %r en git log (anclado y suelto): %d (se necesita exactamente 1)"
                      % (PATRON_ACTA, len(actas)))
        acta_hash, acta_asunto = "", ""
    else:
        acta_hash, acta_asunto = actas[0]

    ruta_head = os.path.join(LOOP, "SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA)
    if not os.path.exists(ruta_head):
        fallos.append("no existe el sello %s" % os.path.basename(ruta_head))
        head_ap = ""
    else:
        head_ap = io.open(ruta_head, encoding="utf-8").read().strip()
        if len(head_ap) != 40:
            fallos.append("el sello %s no trae un hash de 40 caracteres" % os.path.basename(ruta_head))

    c, nac = git(["log", "--diff-filter=A", "--format=%H", "--",
                  "docs/loop/SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA])
    nacs = [l for l in nac.splitlines() if l.strip()]
    if len(nacs) != 1:
        fallos.append("commits que ANADEN el sello de apertura: %d (se necesita exactamente 1)" % len(nacs))
        nac_hash = ""
    else:
        nac_hash = nacs[0]

    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, "scripts/loop/tallar_cabecera_reporte.py",
                        "--fase04", "--vuelta", str(VUELTA)],
                       cwd=RAIZ, capture_output=True, env=env)
    sal_tallador = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    m = re.search(r"ROJO,\s+(\d+)\s+celdas no se pudieron leer", sal_tallador)
    if not m:
        fallos.append("el tallador no imprime la cifra de celdas ilegibles; no se teclea una")
        celdas = ""
    else:
        celdas = m.group(1)
    lado_apertura_roto = [l for l in sal_tallador.splitlines()
                          if "APERTURA" in l and l.strip().startswith(("no ", "sin "))]

    if fallos:
        print("ROJO, el esqueleto NO se escribe:")
        for f in fallos:
            print("   " + f)
        sys.exit(1)

    filas = chr(10).join(
        "| **TAREA %s** | %s | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |"
        % (n, t) for n, t in TAREAS)

    texto = """# REPORTE DE LA VUELTA %(v)d (ejecutor). FASE III, EJECUCION. Rama `%(rama)s`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta%(v)d_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA Y LA SIGUIENTE SI, Y LA CADENCIA NO SE ELIGE
> AQUI: ESTA ADJUDICADA Y RECONFIRMADA TRES VECES.** El acta 176, punto 7.8,
> reanclo el contador a la vuelta que de verdad corrio la bateria y no a la que la
> tenia encargada; **el acta 178, punto 11, y el acta 179, punto 11, lo
> reconfirmaron**; y el encargo de esta vuelta lo repite con todas las letras:
> **la proxima vuelta de bateria es la 181**. Esta es **LA ULTIMA VUELTA QUE
> DECLARA EL HUECO**: la seccion 9 cierra con el **HUECO DECLARADO Y MEDIDO** y
> sus TRES piezas juntas, el nombre del fichero, sus bytes por las dos
> convenciones y la atribucion. Un hueco declarado no es un hueco escondido, y
> **la 181 lo corre**.
>
> **EL TOPE SIGUE EN CINCO, Y NO LO DECIDE NADIE: LO DISPARO LA 177 Y LA 178 Y LA
> 179 LO CONFIRMARON ENTREGANDO CINCO.** `AUDITOR.md` 6.2 dice que el regimen
> temporal de dos sub-tareas dura **hasta que DOS vueltas seguidas cierren su
> propio reporte** con `cerrar_reporte.py`, y eso se cumplio. **El regimen
> temporal queda CUMPLIDO Y CITABLE, no borrado**, y los cuatro commits que lo
> sostienen se localizan EN GIT en el bloque B.1 de
> `scripts/loop/vuelta180_apertura.py`, no se teclean.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno, la 179 lo repitio y aqui vuelve a
> correr en su sitio. **Desde la 178, una columna de apertura medida al cierre es
> caida que ACUMULA**, y eso lo dice el encargo, no este reporte.
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la
> %(ant)d escribio su reporte, lo cerro y lo archivo EN SU MISMA VUELTA; el
> fichero corre LAS DOS igualmente y publica lo que salga de cada una, porque una
> guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.
> **Y LA TAREA 4.a DE ESTA VUELTA FABRICA EL DIA EN QUE DIFIEREN**, que es lo que
> a esta guarda le faltaba desde la 174: hasta hoy nadie la habia visto responder
> a la pregunta buena cuando las dos preguntas dan cosas distintas.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta%(v)d_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `%(rama)s`
- commit del acta de la vuelta %(ant)d: `%(acta8)s`, asunto real leido de git log:
  %(asunto)s
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V%(v)d_HEAD_APERTURA.txt`: `%(head8)s`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `%(nac8)s`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **%(pisa)d**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta %(v)d`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
%(celdas)s celdas no se pudieron leer"** y de esas lineas de rojo, **%(n_ap)d
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
%(filas)s
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
""" % dict(v=VUELTA, ant=VUELTA - 1, pisa=n_arbol, rama=rama, acta8=acta_hash[:8],
           asunto=repr(acta_asunto), head8=head_ap[:8], nac8=nac_hash[:8],
           celdas=celdas, n_ap=len(lado_apertura_roto), filas=filas)

    io.open(ruta, "w", encoding="utf-8", newline="\n").write(texto)
    print("ESQUELETO ESCRITO: docs/loop/REPORTE.md (%d bytes, %d lineas)"
          % (len(texto.encode("utf-8")), texto.count(chr(10))))
    print("   rama leida de git: %s" % rama)
    print("   acta %d leida de git log: %s  %s" % (VUELTA - 1, acta_hash[:8], acta_asunto[:70]))
    print("   HEAD de apertura leido del sello: %s" % head_ap[:8])
    print("   nacimiento del bloque de apertura, --diff-filter=A: %s" % nac_hash[:8])
    print("   reporte pisado, leido de su cabecera: vuelta %d" % n_arbol)
    print("   celdas ilegibles que el tallador imprime HOY: %s" % celdas)
    print("   de ellas, del lado APERTURA: %d" % len(lado_apertura_roto))
    print("   filas de tarea abiertas: %d" % len(TAREAS))
