r"""vuelta184_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA
VUELTA 184, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS DOS TAREAS ENCARGADAS.

CLON DECLARADO de scripts/loop/vuelta183_esqueleto_reporte.py. Lo que se toca a
mano son las DOS filas de tarea, que son las de ESTE encargo, y los parrafos de
prosa que hablan del estado del bucle. La maquina no se toca en ninguna linea
salvo el numero de vuelta.

Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA: el cotejo lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte, que es
obligatorio desde la vuelta 178 por el docstring de aquel fichero. Este texto NO
publica ningun resultado de diff.

POR QUE ESTA VUELTA TRAE DOS FILAS Y NO CINCO. El regimen temporal de AUDITOR.md
6.2 devuelve el tope a cinco cuando DOS vueltas seguidas cierren su propio reporte
con scripts/loop/cerrar_reporte.py. El acta 184, punto 8, lo remidio en git sobre
docs/loop/reportes/: la 182 SI cerro el suyo y la 183 NO, asi que la cuenta de
"dos seguidas" VOLVIO A CERO. El tope se queda en DOS.

Y ESTA VUELTA VUELVE A SER DE BATERIA. AUDITOR.md 6.1: la bateria se declara
corrida cuando los NUEVE tramos tienen salida sellada del mismo calibre, y el acta
184 punto 8 la midio en CINCO. La vuelta retoma en el TRAMO 6, y el TRAMO 5 se
re-corre porque su rojo es lo que la TAREA 1.b repara.

Y EL PASO 0 ARCHIVA EL REPORTE DE LA 183, QUE SE QUEDO SIN CERRAR Y SIN ARCHIVAR.
Eso no es un adorno del final: es lo unico que impide que el esqueleto de hoy
destruya texto que no tiene otra sede con nombre.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0, antes que nada.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 184 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta de la vuelta anterior por las
DOS formas del titulo y en las DOS pasadas de TALLADOR.buscar_acta; HEAD de
apertura leido de docs/loop/SALIDA_V184_HEAD_APERTURA.txt, sellado antes de la
primera operacion; commit de nacimiento del bloque de apertura por
git log --diff-filter=A. Si alguno no se puede leer o es ambiguo, el esqueleto
CAE EN ROJO y no escribe nada: no inventa un hash.

USO:
  python scripts/loop/vuelta184_esqueleto_reporte.py
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
VUELTA = 184
# DE DONDE SE CLONO LA FUNCION PURA DE ABAJO, DECLARADO AQUI PARA QUE LA GUARDA
# DE LA 4.b DE LA VUELTA 180 PUEDA MIRARLO.
FUENTE_DEL_CLON = "scripts/loop/vuelta174_esqueleto_reporte.py"
FUNCION_CLONADA = "vuelta_del_reporte_del_arbol"
PATRONES_ACTA = [
    re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR" % (VUELTA - 1)),
    re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA %d" % (VUELTA - 1)),
]
PATRON_ACTA = "ACTA DE LA VUELTA %d DEL AUDITOR o ACTA DEL AUDITOR, VUELTA %d" % (
    VUELTA - 1, VUELTA - 1)

TAREAS = [
    ("1", 'LOS REGISTROS Y LAS DOS REPARACIONES DE CODIGO, BLOQUEANTE Y ANTES DE TOCAR LA BATERIA. (a) El acta 184 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus siete adjudicaciones `5.1` a `5.7`, LA ADJUDICACION DEL PUNTO 6 contada aparte porque no lleva numeral `5.n`, las cero caidas propias del auditor DECLARADAS con todas las letras y la caida `E.1` del ejecutor, mas su caso positivo por mutacion con el esperado mutado cayendo, y la deuda de la serie REMEDIDA y no heredada del `R.45`. (b) LA REPARACION DEL ARNES QUE PARO LA BATERIA, que es la adjudicacion del punto 6 del acta 184: en `scripts/loop/vuelta165_tarea2_mutacion_censo.py`, `esperadas` deja de teclearse y se computa de la nomina real, los dos ficheros que el auditor de la 165 nombro NO se borran y el caso pasa a exigir que sigan DENTRO del conjunto invisible y no que sean TODO el conjunto, la cifra sale con su corte por banco `9.21`, y todos los casos del arnes tienen que CAER al mutar su esperado. (c) LA ESTIMACION DEL `--plan` SALE CON SU CORTE PEGADO, que es la escalada de la racha de reporte: funcion PURA y arnes propio que CAE si la linea sale sin su corte o si el corte no coincide con la nomina contada en esa corrida. (d) LA RELECTURA AL DOBLE del tramo de la ciega del acta 184, con el cotejo de `sha256` contra el sello ANTES de leer un solo puesto'),
    ("2", 'LA BATERIA, DEL TRAMO 5 AL 9, Y EL CIERRE DEL REPORTE. El TRAMO 5 se re-corre primero, ya con (b) puesto, y despues los tramos 6, 7, 8 y 9 en orden; cual toca lo dice `--siguiente` y no la memoria. Cada tramo se commitea CON SU SALIDA SELLADA al terminar, antes de seguir; el reloj de cada tramo se mide al cerrarlo y se publica medido; una salida sellada que mide CERO BYTES no cuenta como hecha; `git diff --numstat -- dataset/` se mide AL ENTRAR y AL SALIR de cada tramo y las dos cifras se publican. Si otro arnes cae en rojo, el ejecutor se detiene ahi y lo trae con su salida entera, sin re-correrlo y sin arreglarlo. Cuando los nueve tramos tengan salida sellada del mismo calibre, `--componer` arma `docs/loop/SALIDA_V183_BATERIA.txt` y con esa pieza se cierra el reporte con `scripts/loop/cerrar_reporte.py`, que es lo que lleva dos vueltas sin conseguirse. El reporte, una vez cerrado, se archiva en su propia vuelta'),
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
            fallos.append("el sello %s no trae un hash de 40 caracteres"
                          % os.path.basename(ruta_head))

    c, nac = git(["log", "--diff-filter=A", "--format=%H", "--",
                  "docs/loop/SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA])
    nacs = [l for l in nac.splitlines() if l.strip()]
    if len(nacs) != 1:
        fallos.append("commits que ANADEN el sello de apertura: %d (se necesita exactamente 1)"
                      % len(nacs))
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
> **ESTA VUELTA VUELVE A SER DE BATERIA, Y RETOMA EN EL TRAMO 6.**
> `AUDITOR.md` 6.1: la bateria se declara corrida cuando **los NUEVE** tramos
> tienen salida sellada **del mismo calibre**, y el acta 184, punto 8, la midio
> en **CINCO**, con el siguiente en el **TRAMO 6**. **El TRAMO 5 se re-corre**
> porque su rojo es lo que la TAREA 1.b repara, y una salida sellada en rojo no
> es del mismo calibre que ocho en verde. **La seccion 9 de este reporte lleva la
> bateria entera dentro, no un hueco.**
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y LA CUENTA VOLVIO A CERO.** El
> regimen `AUDITOR.md` 6.2 devuelve el tope a cinco cuando **dos vueltas seguidas
> cierren su propio reporte** con `scripts/loop/cerrar_reporte.py`. El acta 184,
> punto 8, lo remidio en git sobre `docs/loop/reportes/`: **la 182 SI cerro el
> suyo** y **la 183 NO**, asi que la racha **se rompe y arranca de cero**. **Van
> dos tareas y no hay una tercera.**
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee
> ningun par de los 543 ni se toca la cola de `docs/plan/08_VERIFICACION.md` (su
> TRAMO 1 es el par **2.464** y se relee cuando haya vuelta de trabajo, no en la
> de bateria); no se cablea el instrumento de vigencia de las ocho `A` rancias por
> `P.5`; **no se vuelve a decidir ninguna clase** en la relectura al doble; no se
> toca el marcador, ni un veredicto, ni `dataset/`; y **no se poda la nomina de la
> bateria**, que es la opcion `c` que el fundador RECHAZO el 5 sep.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno, la 179 y la 180 lo repitieron y aqui
> vuelve a correr en su sitio. **Desde la 178, una columna de apertura medida al
> cierre es caida que ACUMULA.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Las dos preguntas vuelven a coincidir en el numero, pero
> **no en el estado**: el reporte de la %(ant)d **se quedo SIN CERRAR y SIN
> ARCHIVAR**, cosa que el bloque de apertura de hoy midio sin creerle al encargo
> (`docs/loop/SALIDA_V%(v)d_APERTURA.txt`, bloques H.1 y H.8). **Lo archiva el
> PASO 0 de este esqueleto, antes de escribir una sola linea encima**, y su
> salida se pega abajo con lo que salga. **Un reporte sin cerrar se archiva tal
> como quedo: taparlo con un cierre de hoy seria escribir en pasado lo que no
> paso.**

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

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

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
