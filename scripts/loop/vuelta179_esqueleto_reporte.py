# -*- coding: utf-8 -*-
r"""vuelta179_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA
VUELTA 179, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS CINCO TAREAS ENCARGADAS.

CLON DECLARADO de scripts/loop/vuelta178_esqueleto_reporte.py. Lo que se toca a
mano son las CINCO filas de tarea, que son las de ESTE encargo, y los parrafos de
prosa que hablan del estado del bucle. La maquina no se toca en ninguna linea.

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
LA VUELTA 177 y y ya trae su CUARTO veredicto, EL ARBOL DE SINTAXIS,
desde la 178. Su salida sobre ESTE fichero se pega en el reporte.

LA MAQUINA NO CAMBIA EN NADA: el paso 0 endurecido que estreno la 174 se conserva
entero. Esa frase SI es una afirmacion sobre la maquina, y por eso NO se publica
como comprobada aqui tampoco: la comprueba el instrumento, no este texto.

QUE ES ESE PASO 0 ENDURECIDO, dicho otra vez para que este fichero se entienda
solo: NO PREGUNTA POR `VUELTA - 1`, PREGUNTA POR EL REPORTE QUE DE VERDAD VA A
PISAR, Y ESE NUMERO SE LEE DEL PROPIO FICHERO con la funcion pura
`vuelta_del_reporte_del_arbol()`. En esta vuelta las dos preguntas coinciden (el
arbol trae el reporte de la 178 y `VUELTA - 1` es 178), y precisamente por eso el
fichero corre LAS DOS y publica lo que salga de cada una: una guarda que solo se
mira cuando difiere no se puede auditar el dia que difiera.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA: `vuelta_del_reporte_del_arbol`
esta copiada de `vuelta174_esqueleto_reporte.py` en vez de importada. Importarla
crearia una dependencia nueva sobre un fichero numerado sin nada que avise si
alguien lo borra por viejo, que es el punto 3 de la TAREA 5 de ESTE encargo,
anotado como pendiente y que sigue sin instrumento. Se clona, se declara, y el arnes de la
funcion original (`scripts/loop/vuelta174_tarea1b_mutacion_esqueleto.py`) sigue
apuntando a su sujeto de siempre y no se toca.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 179 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
`git rev-parse --abbrev-ref HEAD`; commit del acta de la vuelta anterior por las
DOS formas del titulo y en las DOS pasadas de `TALLADOR.buscar_acta`; HEAD de
apertura leido de docs/loop/SALIDA_V179_HEAD_APERTURA.txt, sellado antes de la
primera operacion; commit de nacimiento del bloque de apertura por
`git log --diff-filter=A`. Si alguno no se puede leer o es ambiguo, el esqueleto
CAE EN ROJO y no escribe nada: no inventa un hash.

USO:
  python scripts/loop/vuelta179_esqueleto_reporte.py
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
VUELTA = 179
PATRONES_ACTA = [
    re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR" % (VUELTA - 1)),
    re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA %d" % (VUELTA - 1)),
]
PATRON_ACTA = "ACTA DE LA VUELTA %d DEL AUDITOR o ACTA DEL AUDITOR, VUELTA %d" % (
    VUELTA - 1, VUELTA - 1)

TAREAS = [
    ("1", "LOS REGISTROS, LAS CORRECCIONES Y LA OPERACION DE CODIGO DE LA ESCALADA, Y ES BLOQUEANTE. Cuatro letras: (a) LA CORRECCION DECLARADA DE LA CAIDA DE LA 178, que publico en su 1.e `16 casos` donde su propio fichero `docs/loop/SALIDA_V178_T1E_MUTACION.txt` dice 18, con las TRES cifras al lado (la publicada, la del fichero y la de la re-corrida de hoy) y SIN retocar el reporte archivado, que dice lo que se publico; (b) LA OPERACION DE CODIGO DE LA ESCALADA, que es la pieza que manda: la guarda de LA PROSA QUE CITA UN FICHERO, dentro de `cerrar_reporte.py` y como funcion PURA junto a sus hermanas, que caza toda frase que publique una cifra de casos de un arnes Y nombre un `SALIDA_V*.txt` en la misma linea, lee la cifra propia de ese fichero y CAE EN ROJO nombrando la linea, la cifra publicada y la del fichero, con los bloques cercados fuera y con el fichero inexistente o de cero bytes tambien en ROJO; con su caso positivo por mutacion y CORRIDA SOBRE `REPORTE_V178.md` publicando lo que salga; (c) LOS DOS ARNESES DESTAPADOS ENTRAN EN LA NOMINA de `verificar_mutaciones_viejas.py`, mas todo arnes que esta vuelta escriba, con la cuenta entera y la resta comprobada, ANTES de la 181 para que el rojo que la 178 anuncio no llegue a existir; (d) EL CORTE DEL DENOMINADOR CABLEADO DONDE SE GENERA LA CIFRA y no en una frase, porque la 178 publico 15 de 92 siendo verdad y al cerrar eran 15 de 98"),
    ("2", "`OP-L-03`: SE LEEN LOS DIEZ PARES REALES DE LOS ACTOS SIN LEER. El backlog ya esta re-medido y `backlog_l03_resuelto.py` sale VERDE con los dos caminos calzando en los 40 actos: de los 73 pares que el instrumento da quedan 18 reales, 8 los leyo la 177 y quedan 10 en los 34 actos que nadie ha mirado. Los diez se leen con la vara del banco, par por par, y cada uno con su veredicto y su razon en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` SOLO SI EL PAR TIENE PUESTO EN LA COLA; si no lo tiene NO SE INVENTA UN PUESTO y su clase y su razon van al registro de `OP-L-03` en el campo `clases_de_los_pares_por_leer`, que es donde la 177 las puso y donde son trazables. El marcador no se toca si no hay puesto, y si lo hay se recomputa del archivo con sus cuatro clases. Cada acto cierra con su forma escrita: la figura, su cobertura y lo que queda. Y la cifra va al lado, siempre las dos: pares del instrumento y pares reales"),
    ("3", "LOS DIECISEIS TRIANGULOS SE PUBLICAN PARTIDOS POR SU FUENTE, y NINGUNA CLASE SE MUEVE. `vuelta178_tarea3_anotar_triangulos.py` publica la cifra PARTIDA y no solo el 16: cuantos descansan enteros en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y cuantos se apoyan en un lado de fuera, y NOMBRA aquellos en que el lado de fuera es el `D`, que es el lado que hace que el triangulo sea un triangulo. `docs/plan/OP_L_03_TRIANGULOS.jsonl` gana un campo por fila que diga si el triangulo es recomputable entero del archivo, y el campo `fuente_de_la_clase` por lado NO se toca. CERO VEREDICTOS MOVIDOS, comprobado por `sha256` antes y despues. Con su caso positivo por mutacion sobre un registro fabricado, donde un triangulo con sus tres lados en el archivo y otro con el `D` fuera caen en casillas distintas"),
    ("4", "LAS QUINCE DEL SUJETO CONGELADO SE JUZGAN, UNA A UNA, Y NO SE CABLEA NADA TODAVIA. Primero se juzgan, despues se cablea, y no al reves. Por cada una de las quince, un veredicto escrito con su prueba: o el arnes de verdad ABRE un fichero vivo de la campana y hay que congelarle el sujeto, o LO NOMBRA SIN ABRIRLO y basta con que lo declare, o es un CASO DECLARADO legitimo y se anota por que. Registro propio y no prosa: `docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl`, una fila por arnes, con el nombre, el veredicto, el fichero que abre y la evidencia (la linea del codigo). NO se arregla ningun arnes en esta vuelta y NO se cablea la guarda al rojo global de la bateria: el cableado se decide con los quince veredictos delante. NADA se borra de la nomina"),
    ("5", "LO QUE NO ENTRA Y NO SE PIERDE, CONTADO EN VOZ ALTA. Ninguna de estas cinco se toca aqui, y las cinco se nombran CON SU MEDICION (existe, bytes en disco y normalizados a LF) para que no se caigan: la segunda sede de la clausula 4.4 en `REPORTE_V172.md:535`; el docstring de `paso0_archivar_anterior.py`, que sigue hablando de LA VUELTA ANTERIOR cuando la maquina pregunta por EL REPORTE QUE VA A PISAR; la guarda que falta en la dependencia del `D.4` de la 174, donde el esqueleto clona en vez de importar y nada avisa si el fichero del que se clono desaparece; el grano del tope de 10 minutos, que se mide EN LA 181 con el reloj de esa corrida y no se re-elige a ojo antes; y la convencion de bytes, que es del fundador, lleva seis actas subiendo y sube como PENDIENTE y no como problema, porque el remedio provisional de publicar siempre las dos ya es instrumento"),
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
> ADJUDICADA Y RECONFIRMADA DOS VECES.** El acta 176, punto 7.8, reanclo el
> contador a la vuelta que de verdad corrio la bateria y no a la que la tenia
> encargada; **el acta 178, punto 11, lo reconfirmo**; y el encargo de esta vuelta
> lo repite con todas las letras: **la proxima vuelta de bateria es la 181**, y la
> 179 y la 180 cierran su seccion 9 con el **HUECO DECLARADO Y MEDIDO**, con su
> nombre, sus bytes medidos y su atribucion, las tres juntas. Un hueco declarado
> no es un hueco escondido.
>
> **EL TOPE SIGUE EN CINCO, Y NO LO DECIDE NADIE: LO DISPARO LA 177 Y LA 178 LO
> CONFIRMO ENTREGANDO CINCO.** `AUDITOR.md` 6.2 dice que el regimen temporal de
> dos sub-tareas dura **hasta que DOS vueltas seguidas cierren su propio reporte**
> con `cerrar_reporte.py`, y eso se cumplio. **El regimen temporal queda CUMPLIDO
> Y CITABLE, no borrado**, y los cuatro commits que lo sostienen se localizan EN
> GIT en el bloque B.1 de `scripts/loop/vuelta179_apertura.py`, no se teclean.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno y aqui se repite: el medidor corre
> dentro del bloque de apertura. **Desde la 178, una columna de apertura medida al
> cierre es caida que ACUMULA**, y eso lo dice el encargo, no este reporte.
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la
> %(ant)d escribio su reporte, lo cerro y lo archivo EN SU MISMA VUELTA; el
> fichero corre LAS DOS igualmente y publica lo que salga de cada una, porque una
> guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.

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
