# -*- coding: utf-8 -*-
r"""vuelta178_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA
VUELTA 178, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS CINCO TAREAS ENCARGADAS.

CLON DECLARADO de scripts/loop/vuelta177_esqueleto_reporte.py, hecho con `sed`
cambiando UNICAMENTE el numero de vuelta. Lo que se toca a mano despues de ese
`sed` son las CINCO filas de tarea (la 177 traia dos) y los parrafos de prosa que
hablan del estado del bucle, que son distintos porque el tope volvio a cinco.

Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA: el cotejo lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte, que es
obligatorio desde esta vuelta por el docstring de aquel fichero. Este texto NO
publica ningun resultado de diff.

DE DONDE VIENE ESA CAUTELA, Y NO SE BORRA DE QUE IBA: la CAIDA DE REPORTE 1 del
acta 176 seccion 5. El esqueleto de la 176 publicaba en su docstring que el
`diff` con `NNN` sustituido "SALE VACIO"; el auditor lo corrio y salieron 58
lineas, 33 de ellas de la maquina, aunque de esas 33 las SENTENCIAS DE CODIGO
eran 1 y los LITERALES DE TEXTO 32 medidos por el instrumento. El instrumento
que lo mide, `scripts/loop/cotejar_clon_declarado.py`, NACIO EN LA TAREA 1.d DE
LA VUELTA 177 y en esta vuelta se le anade su CUARTO veredicto, EL ARBOL DE
SINTAXIS. Su salida sobre ESTE fichero se pega en el reporte.

LA MAQUINA NO CAMBIA EN NADA: el paso 0 endurecido que estreno la 174 se conserva
entero. Esa frase SI es una afirmacion sobre la maquina, y por eso NO se publica
como comprobada aqui tampoco: la comprueba el instrumento, no este texto.

QUE ES ESE PASO 0 ENDURECIDO, dicho otra vez para que este fichero se entienda
solo: NO PREGUNTA POR `VUELTA - 1`, PREGUNTA POR EL REPORTE QUE DE VERDAD VA A
PISAR, Y ESE NUMERO SE LEE DEL PROPIO FICHERO con la funcion pura
`vuelta_del_reporte_del_arbol()`. En esta vuelta las dos preguntas coinciden (el
arbol trae el reporte de la 177 y `VUELTA - 1` es 177), y precisamente por eso el
fichero corre LAS DOS y publica lo que salga de cada una: una guarda que solo se
mira cuando difiere no se puede auditar el dia que difiera.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA: `vuelta_del_reporte_del_arbol`
esta copiada de `vuelta174_esqueleto_reporte.py` en vez de importada. Importarla
crearia una dependencia nueva sobre un fichero numerado sin nada que avise si
alguien lo borra por viejo, que es el hallazgo (e) que el encargo de la 177
anotaba como pendiente y que sigue sin instrumento. Se clona, se declara, y el arnes de la
funcion original (`scripts/loop/vuelta174_tarea1b_mutacion_esqueleto.py`) sigue
apuntando a su sujeto de siempre y no se toca.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 178 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
`git rev-parse --abbrev-ref HEAD`; commit del acta de la vuelta anterior por las
DOS formas del titulo y en las DOS pasadas de `TALLADOR.buscar_acta`; HEAD de
apertura leido de docs/loop/SALIDA_V178_HEAD_APERTURA.txt, sellado antes de la
primera operacion; commit de nacimiento del bloque de apertura por
`git log --diff-filter=A`. Si alguno no se puede leer o es ambiguo, el esqueleto
CAE EN ROJO y no escribe nada: no inventa un hash.

USO:
  python scripts/loop/vuelta178_esqueleto_reporte.py
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paso0_archivar_anterior as PASO0   # noqa: E402
import tallar_cabecera_reporte as TALLADOR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = 178
PATRONES_ACTA = [
    re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR" % (VUELTA - 1)),
    re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA %d" % (VUELTA - 1)),
]
PATRON_ACTA = "ACTA DE LA VUELTA %d DEL AUDITOR o ACTA DEL AUDITOR, VUELTA %d" % (
    VUELTA - 1, VUELTA - 1)

TAREAS = [
    ("1", "LOS REGISTROS Y LAS CORRECCIONES, Y ES BLOQUEANTE. Cinco letras: (a) LA RELECTURA AL DOBLE DEL TRAMO DE LA CAIDA de conteo del acta 177, la cuenta de la nomina y del censo, publicada ENTERA en tabla y con la resta comprobada, porque una cuenta que no cierra consigo misma se caza sola si alguien la escribe entera; (b) `arneses_que_faltan()` SE ARREGLA en la funcion y no en la llamada, con la vara del censo EXPLICITA y con su motivo, sin podar la nomina, y con el caso positivo por mutacion que hoy CAE con la funcion vieja: dos arneses de la MISMA vuelta que la ultima de la nomina, uno dentro y otro fuera, y la funcion tiene que VER al de fuera; (c) EL CUARTO VEREDICTO de `cotejar_clon_declarado.py`, EL ARBOL DE SINTAXIS, sin tocar la clasificacion vieja, en rojo si un fichero no parsea, y con el caso que lo decide todo: dos ficheros que solo difieren en una coma final dan maquina DIFIERE y AST IDENTICO; (d) EL `--puestos` Y EL `--excluir` DEL AISLADOR DE CIEGA, componibles con los selectores que ya tiene, en rojo si un puesto pedido no existe, con la guarda de fuga intacta, y borrando despues la muleta `_auditor_v178_ciega.py` por `P.16`; (e) LAS DOS DE HIGIENE: que `cerrar_reporte.py` CAIGA EN ROJO si el reporte publica una cifra de bytes o un sha sin su pareja, y LA GUARDA DEL SUJETO CONGELADO, que lleva desde la vuelta 145 siendo una frase y no un instrumento"),
    ("2", "`OP-L-03`: SE RE-MIDE EL BACKLOG ENTERO ANTES DE LEER UN ACTO MAS. No se toca `backlog_l03_vuelta14.py`, que sostiene una cifra adjudicada en la vuelta 15; se escribe el filtro DELANTE, en `scripts/loop/backlog_l03_resuelto.py`, de nombre estable y sin numero de vuelta, que corre el instrumento viejo y le pasa el resolutor de `P.1` por encima publicando LAS DOS COLUMNAS AL LADO. Por acto y en total: miembros escritos, vivos por el resolutor, vivos por el campo `deprecado` del grafo, SI LOS DOS CAMINOS CALZAN, pares que el instrumento da, pares reales y pares disueltos. CAE EN ROJO si los dos caminos no calzan en algun acto, nombrandolo. Con su caso positivo por mutacion sobre un mapa de alias FABRICADO. Y publica la cifra que la 177 no pudo publicar: cuanto sobra en los 34 actos que no miro. EL ESTADO DE LA FICHA NO SE TOCA"),
    ("3", "LOS CINCO TRIANGULOS `A` MAS `A` MAS `D`: SE ANOTAN CON SU REGLA, NO SE MUEVEN. La `P.3` de la 177 queda adjudicada como COSA JUZGADA en el acta 177 punto 7.9: las dos reglas que lo deciden ya estan escritas y RESULTAN COMPATIBLES. La `9.6.1` del banco dice que un nodo que es un paso de otro y NO TRAE PROCEDIMIENTO PROPIO, REPITE; la correccion declarada del 13 ago 2026 sobre los puestos 530 y 863 dice que la madre y su pieza de arenas se separan. La condicion que las concilia es la que la propia `9.6.1` escribe: SI LA PIEZA TRAE PROCEDIMIENTO PROPIO SE SEPARA, SI ES EL PASO DICHO OTRA VEZ, REPITE. Por cada uno de los cinco se anota EN EL JSONL cual de las dos reglas gobierna cada lado y CON QUE PRUEBA. CERO VEREDICTOS MOVIDOS"),
    ("4", "LA CEGUERA DE LA VARA, QUE LLEVA DOS VUELTAS CONTADA. `vuelta150_3_relectura_expediente.py` imprime SEIS fichas en LISTA sin prueba y dos de las seis estan CONSUMIDAS por otras, asi que el trabajo real son CUATRO. La vara es del fundador y su veredicto NO SE TOCA: lo que se anade es una COLUMNA, no una exclusion. Que siga imprimiendo las seis y que diga de cada una si esta CONSUMIDA por otra ficha y por cual. La cuenta final publica LAS DOS, nunca solo el cuatro. Con su caso positivo por mutacion sobre un expediente fabricado"),
    ("5", "LO QUE NO ENTRA Y NO SE PIERDE, CONTADO EN VOZ ALTA COMO SIEMPRE: la segunda sede de la clausula 4.4 en `REPORTE_V172.md:535`; el docstring de `paso0_archivar_anterior.py`; la guarda que falta en la dependencia del `D.4` de la 174; y la medicion del grano del tope de 10 minutos, que se mide EN LA 181 con el reloj de esa corrida y no se re-elige a ojo antes. Ninguna de las cuatro se toca aqui, y las cuatro se nombran para que no se caigan"),
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
> **ESTA VUELTA NO ES DE BATERIA, Y LA CADENCIA NO SE ELIGE AQUI: ESTA
> ADJUDICADA Y RECONFIRMADA.** El acta 176, punto 7.8, reanclo el contador a la
> vuelta que de verdad corrio la bateria y no a la que la tenia encargada, y el
> encargo de esta vuelta lo repite con todas las letras: **la proxima vuelta de
> bateria es la 181**, y la 178, la 179 y la 180 cierran su seccion 9 con el
> **HUECO DECLARADO Y MEDIDO**, con su nombre, sus bytes medidos y su atribucion,
> las tres juntas. Un hueco declarado no es un hueco escondido.
>
> **EL TOPE VUELVE A CINCO, Y NO LO DECIDE NADIE: LO DISPARO LA VUELTA
> ANTERIOR.** `AUDITOR.md` 6.2 dice que el regimen temporal de dos sub-tareas
> dura **hasta que DOS vueltas seguidas cierren su propio reporte** con
> `cerrar_reporte.py`. **La 176 y la 177 lo hicieron, cada una en su misma
> vuelta, y las dos archivaron ademas su reporte sin esperar a la siguiente.**
> El tope vuelve a CINCO por la propia letra de la 6.2, sin que nadie tenga que
> decidirlo, y este encargo trae cinco. **El regimen temporal queda CUMPLIDO Y
> CITABLE, no borrado**, y los cuatro commits que lo cumplen se localizan EN GIT
> en el bloque B.1 de `scripts/loop/vuelta178_apertura.py`, no se teclean.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, QUE ES LA CAIDA
> PROPIA QUE LA 177 SE ANOTO.** El remedio quedo cableado en
> `vuelta177_apertura.py` y aqui se estrena de verdad: el medidor corre dentro
> del bloque de apertura, antes de la primera operacion. **Desde esta vuelta, una
> columna de apertura medida al cierre es caida que ACUMULA**, y eso lo dice el
> encargo, no este reporte.
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas coinciden, porque la
> %(ant)d escribio su reporte, lo cerro y lo archivo; el fichero corre LAS DOS
> igualmente y publica lo que salga de cada una, porque una guarda que solo se
> mira cuando difiere no se puede auditar el dia que difiera.

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
