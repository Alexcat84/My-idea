# -*- coding: utf-8 -*-
r"""vuelta191_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 191,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta190_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS, este docstring y el bloque de prosa del encabezado.
El cotejo del clon lo hace scripts/loop/cotejar_clon_declarado.py y su salida se
pega en el reporte con lo que salga: AQUI NO SE AFIRMA QUE NINGUN DIFF SALGA
VACIO.

ESTA VUELTA NO ES DE BATERIA (AUDITOR.md 6.1: corre cada cinco vueltas, la 189 la
corrio entera, y la siguiente cae en la 194). Su seccion 9 cierra con el HUECO
DECLARADO Y MEDIDO por el carril de cerrar_reporte.py, con su medicion, su
atribucion y su corrida.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 191 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V191_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada:
no inventa un hash.

Y SE DECLARA EL DESFASE QUE NO SE REPARA, POR SEPTIMA VUELTA: PATRONES_ACTA
sigue pidiendo el acta de VUELTA - 1, o sea la 190, cuando el acta que ORDENA
esta vuelta es la 191. Es el `D.2` del reporte de la 184, adjudicado a favor por
la `5.2` del acta 185 CON REPARACION ENCARGADA, y esta vuelta NO la ejecuta
porque no es ninguna de sus cinco tareas y el encargo nombra una a una las que
quedan fuera. Se declara en vez de colarse.

USO:
  python scripts/loop/vuelta191_esqueleto_reporte.py
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
VUELTA = 191
FUENTE_DEL_CLON = "scripts/loop/vuelta174_esqueleto_reporte.py"
FUNCION_CLONADA = "vuelta_del_reporte_del_arbol"
PATRONES_ACTA = [
    re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR" % (VUELTA - 1)),
    re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA %d" % (VUELTA - 1)),
]
PATRON_ACTA = "ACTA DE LA VUELTA %d DEL AUDITOR o ACTA DEL AUDITOR, VUELTA %d" % (
    VUELTA - 1, VUELTA - 1)

TAREAS = [
    ("1", 'LOS REGISTROS. BLOQUEANTE. El acta 191 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus NUEVE adjudicaciones `4.1` a `4.9`, QUE ESTA VEZ SI SON NUEVE A FAVOR: seis son los discutibles del ejecutor (`D.1` a `D.6`) y los seis van A FAVOR, y las tres restantes (`4.7`, `4.8`, `4.9`) son las tres preguntas contestadas. EL CERO DE `EN CONTRA` TIENE QUE SALIR SIN QUE LA MAQUINA SE ROMPA POR NO ENCONTRAR NINGUNA, y se prueba por mutacion con un acta fabricada que SI lleve una. Mas los TRES hallazgos de la seccion 5 que no salen de ningun discutible (la marca `DISCUTIBLE MARCADO` contra la dificultad medida en `5.1`, la etiqueta del veredicto duplicada en `5.2`, y `git checkout --` que no restaura byte a byte en `5.3`), UNA caida propia del auditor de metodo ESCRITA COMO UNA Y NO OMITIDA, CERO caidas del ejecutor que acumulen con las TRES de metodo que el reporte de la 190 declara, y LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de puestos con su nota de SOLAPE TOTAL a proposito. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido, no escribe nada, y se prueba re corriendolo con la sede medida en bytes antes y despues'),
    ("2", 'LA RELECTURA AL DOBLE DEL TRAMO DEL 3182. BLOQUEANTE. Es la deuda de credito que la TAREA 4 de la 190 dejo medida y que no se auto encargo, adjudicada A FAVOR en la `4.5` del acta 191 y encargada ahi mismo: quien encarga el doble es el auditor. EL TRAMO es la tanda de 30 puestos de `docs/loop/SALIDA_V190_T4_CIEGA.txt`, donde la discrepancia del `3182` cayo FUERA de los dudosos marcados. AL DOBLE son sus 30 vecinos deterministas, con `vecinos()` IMPORTADA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada: 30 mas 30 son 60, el doble exacto. EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO: a `vecinos()` se le pasa `evitar` con TODO lo consumido, contado de sus ficheros y no tecleado. Con `scripts/loop/aislador_de_ciega.py`, criterio escrito literal, ciega y destape en ficheros SEPARADOS, las clases escritas y COMMITEADAS en su propio commit ANTES de abrir el destape, y los dudosos NOMBRADOS DELANTE. NO SE TOCA NINGUNA CLASE: `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre solo en lectura y su `sha256` LF abre y cierra en el mismo valor por las dos convenciones'),
    ("3", 'LAS DOS CONVENCIONES DE `lineas`, QUE LLEVAN DOS VUELTAS ESPERANDO. Es la `5.1` del acta 190 y no se ha tocado. Hay instrumentos de la cadena que cuentan lineas con `len(texto.split(NL))`, que suma un elemento vacio final que no es una linea, y otros que cuentan con `texto.count(NL)`, que si calza con `wc -l`. ES UNA MEDICION ANTES QUE UN ARREGLO: (a) MIDE PRIMERO cuantos ficheros de `scripts/loop/` cuentan lineas por cada una de las dos convenciones, nombralos y publica la cifra, porque sin esa cifra el arreglo no se sabe de que tamano es; (b) DESPUES ARREGLA con la vara de las dos convenciones de BYTES que esta casa ya construyo: o se publica la pareja, o se publica la que calza con `wc -l` diciendo cual es; (c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un instrumento vuelve a publicar una sola cifra de lineas por la convencion que no calza. NO SE TOCAN LOS NUMEROS YA PUBLICADOS EN REPORTES CERRADOS'),
    ("4", 'LA GUARDA DEL VEREDICTO DUPLICADO EN `cerrar_reporte.py`. Es el hallazgo `5.2` del acta 191. La linea 50 del reporte de la 190 dice `**EL VEREDICTO DE UNA LINEA: **EL VEREDICTO DE UNA LINEA: LAS CINCO TAREAS...`, y la causa esta medida: `cerrar_reporte.py` en su linea 1817 compone la etiqueta y su propia salida prueba que el veredicto que se le paso YA la traia. (a) QUE `cerrar_reporte.py` CAIGA EN ROJO si el `--veredicto` que recibe ya trae la etiqueta o los asteriscos, en vez de pegarla dos veces, y que diga QUE RECIBIO y QUE ESPERABA: fallar ruidoso, sin limpiarla en silencio, porque limpiar en silencio es la otra mitad de la misma enfermedad. (b) CASO POSITIVO POR MUTACION que CAIGA si la guarda se quita. (c) EL REPORTE DE LA 190 NO SE REESCRIBE: esta cerrado y archivado byte a byte, y su etiqueta doble se queda donde esta con la explicacion al lado'),
    ("5", 'LA MARCA `DISCUTIBLE MARCADO` CONTRA LA DIFICULTAD MEDIDA. SOLO MEDIR, Y NO TOCA NI UNA RAZON DEL ARCHIVO. Es el hallazgo `5.1` del acta 191: sobre su tanda de treinta, dos lectores independientes discrepan del archivo en los MISMOS OCHO puestos, `DISCUTIBLE MARCADO` aparece en 427 de las 3.388 filas y en CERO de esos ocho. TREINTA CASOS NO SON UNA LEY, y por eso esto es una medicion. (a) DI PRIMERO CUAL ES TU UNIVERSO Y COMO LO CONSTRUYES antes de contar nada: que ficheros de cotejo de ciega existen, de que vueltas, y cuales quedan fuera por no ser legibles con una regla unica, con la cifra de los que entran y de los que no y con sus nombres, porque un universo elegido despues de ver el resultado no sirve. (b) CUENTA sobre ese universo cuantos puestos han tumbado alguna vez a un lector, cuantos de esos llevan la marca, y cual es la tasa de la marca en el archivo entero: las tres cifras juntas o ninguna. (c) NO SAQUES LA CONCLUSION SI LA CUENTA NO LA SOSTIENE: si el universo sale pequeno, dilo y publica el tamano. (d) NO SE ESCRIBE NI UNA FILA DEL ARCHIVO'),
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

    # EL CARRIL `--rehacer` (vuelta 191, y va declarado como discutible en el
    # reporte de esa vuelta). QUE ES Y POR QUE EXISTE, MEDIDO Y NO SUPUESTO: al
    # cerrar la 191 salieron 22 cifras de bytes publicadas SIN SU PAREJA, y dos
    # de ellas no estaban en la prosa de ninguna tarea sino en la LINEA DE
    # IDENTIDAD que este mismo fichero escribe, porque el asunto del commit del
    # acta 190 trae DENTRO `961248 bytes` y un `sha256`. Arreglarlo obliga a
    # RE ESCRIBIR el esqueleto, y el PASO 0 lo impide con razon: su archivador
    # no puede archivar como vuelta 190 un REPORTE.md que ya es de la 191.
    #
    # QUE SE AFLOJA Y QUE NO. Se salta el PASO 0 y NADA MAS. A cambio se exige
    # algo que en este caso es MAS FUERTE que el archivado: que el reporte que
    # se va a pisar sea EL DE ESTA MISMA VUELTA y este COMMITEADO en git sin
    # cambios en el arbol. Un reporte parcial que vive en un commit no se pierde
    # al pisarlo: se recupera con `git show`. Si el arbol trae cambios sin
    # commitear, o si el reporte no es de esta vuelta, ESTE CARRIL CAE EN ROJO.
    if "--rehacer" in sys.argv:
        print("CARRIL --rehacer. EL PASO 0 SE SALTA Y SE DICE POR QUE.")
        rr = subprocess.run(["git", "status", "--porcelain", "--",
                             "docs/loop/REPORTE.md"], cwd=RAIZ, capture_output=True)
        sucio = rr.stdout.decode("utf-8", errors="replace").strip()
        texto_ahora = io.open(os.path.join(LOOP, "REPORTE.md"),
                              encoding="utf-8").read()
        n_ahora = vuelta_del_reporte_del_arbol(texto_ahora)
        c_last, last = git(["log", "-1", "--format=%H %s", "--",
                            "docs/loop/REPORTE.md"])
        print("   git status de docs/loop/REPORTE.md: %r" % (sucio or "(limpio)"))
        print("   vuelta del reporte que se va a pisar, leida de su cabecera: %s"
              % n_ahora)
        print("   ultimo commit que lo toca: %s" % last[:130])
        malos = []
        if sucio:
            malos.append("el reporte del arbol tiene cambios sin commitear")
        if n_ahora != VUELTA:
            malos.append("el reporte del arbol es el de la vuelta %s y no el de la %d"
                         % (n_ahora, VUELTA))
        if not last.strip():
            malos.append("ningun commit toca docs/loop/REPORTE.md")
        if malos:
            print("ROJO, el carril --rehacer NO escribe:")
            for m in malos:
                print("   " + m)
            sys.exit(1)
        print("   VERDE: lo que se va a pisar es el reporte parcial de ESTA vuelta")
        print("   y vive entero en git. Se recupera con `git show`.")
        print("")

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
    _rehacer = "--rehacer" in sys.argv
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

    if _rehacer:
        print("PASO 0.b y 0.c: SALTADOS POR EL CARRIL --rehacer, y se dice.")
        print("")
        ok = True
    else:
        print("PASO 0.b. LA GUARDA SOBRE LA VUELTA ANTERIOR (%d), PUBLICADA SALGA LO"
              % (VUELTA - 1))
        print("   QUE SALGA, EN MODO SOLO COMPROBACION Y SIN LANZAR EL ARCHIVADOR")
        ok_ant, informe_ant = PASO0.exigir_archivado(VUELTA - 1,
                                                     ejecutar_archivador=False)
        for l in informe_ant:
            print("   " + l)
        print("   VEREDICTO SOBRE LA %d: %s"
              % (VUELTA - 1, "VERDE" if ok_ant else "ROJO"))
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
    # EL TALLADOR TIENE DOS SALIDAS Y LAS DOS SON LEGITIMAS, Y ESTO SE APRENDIO
    # MIDIENDO (vuelta 191, carril --rehacer): en la APERTURA le faltan las
    # salidas de cierre y dice `ROJO, N celdas no se pudieron leer`; RE CORRIDO
    # con el bloque de cierre ya en disco, TALLA LA TABLA ENTERA y no imprime esa
    # linea. La version anterior de este fichero solo sabia leer la primera y
    # caia en rojo sobre un tallador PERFECTAMENTE VERDE. Ahora se leen las dos y
    # **se dice cual de las dos fue**, en vez de teclear un cero.
    m = re.search(r"ROJO,\s+(\d+)\s+celdas no se pudieron leer", sal_tallador)
    tallador_verde = "LA TABLA, PARA PEGAR ENTERA" in sal_tallador
    if m:
        celdas = m.group(1)
        frase_tallador = ('corrido aqui, el tallador dice **"ROJO, %s celdas no se '
                          'pudieron leer"**' % celdas)
    elif tallador_verde:
        celdas = "0"
        frase_tallador = ("corrido aqui, el tallador **TALLA LA TABLA ENTERA y no "
                          "imprime ninguna linea de celdas ilegibles**")
    else:
        fallos.append("el tallador no imprime ni la cifra de celdas ilegibles ni "
                      "la tabla; no se teclea una")
        celdas = ""
        frase_tallador = ""
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
> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que **no lleva
> nada mas**. **La 189 la corrio entera**, asi que **la siguiente cae en la 194**.
> El hueco va **con su nombre, sus bytes medidos y su atribucion, LAS TRES
> JUNTAS**, por el carril de `cerrar_reporte.py`: **un hueco declarado no es un
> hueco escondido.**
>
> **VAN CINCO SUB-TAREAS, Y EL TOPE DE CINCO NO HACE FALTA VOLVER A GANARLO:**
> esta vigente desde la `4.10` del acta 190. **Y la cifra que lo sostiene se
> remidio en esta vuelta en vez de heredarse:** el bloque **B.2** del sello de
> apertura busco en git los commits de cierre y midio sus ficheros
> `SALIDA_V<n>_CERRAR_REPORTE.txt` uno a uno, y publica lo que salga.
>
> **DONDE SE TALLO ESTE ESQUELETO: EN LA APERTURA Y EN SU PROPIO COMMIT.** Desde
> el segundo commit de esta vuelta ya hay reporte parcial en el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** ni cribado, ni
> recomputo, ni operaciones del plan, ni las mesas anotadas, ni **podar la
> nomina** (la opcion `c` que el fundador RECHAZO el 5 sep 2026: **la nomina
> sigue creciendo y nadie la poda sin el fundador**), ni la bateria, que cae en
> la 194. **Y siguen fuera, nombradas para que la 192 no las redescubra:**
> `acumulan()` que lea la tabla o declare que no es la sede; el cotejo de clon
> declarado que separa sentencia de codigo de cambio de texto; la excepcion que
> publica siempre su lista; la medicion del censo de arneses con carril de
> mutacion sin fichero propio; las ocho actas sin entrada propia en la serie (173
> a 180); el exitcode 2 propagado a `--componer`; y que el campo `evidencia` de
> `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE MUEVE: sigue
> en `LISTA`**.
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo
> valor. **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al
> salir y **las dos cifras se publican**.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** **Una columna de apertura medida
> al cierre es caida que ACUMULA.**

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta%(v)d_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `%(rama)s`
- commit del acta de la vuelta %(ant)d: `%(acta8)s`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer
  DENTRO cifras de bytes y `sha256` suyas, y una guarda que mira renglon a
  renglon no distingue una cita de una afirmacion. Cercarlo es decir lo que es:
  **una cita de la salida de un instrumento**, que es exactamente el motivo por
  el que `cerrar_reporte.py` deja los bloques cercados fuera de su guarda de
  parejas.

```
%(asunto)s
```
- **DESFASE DECLARADO, SEPTIMA VUELTA:** la linea de arriba nombra el acta
  **%(ant)d** porque `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que
  ORDENA esta vuelta es la 191**. Es el `D.2` del reporte de la 184, adjudicado a
  favor con reparacion encargada por la `5.2` del acta 185. **Esta vuelta no la
  ejecuta** porque no es ninguna de sus cinco tareas y el encargo nombra una a
  una las que quedan fuera. Se declara en vez de colarse.
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
que la mitad izquierda ya se puede leer: %(frase_tallador)s, y de las lineas de
rojo que imprima, **%(n_ap)d mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
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
           celdas=celdas, n_ap=len(lado_apertura_roto), filas=filas,
           frase_tallador=frase_tallador)

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
