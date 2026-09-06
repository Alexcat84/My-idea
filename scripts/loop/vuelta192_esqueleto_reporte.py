# -*- coding: utf-8 -*-
r"""vuelta192_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 192,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta191_esqueleto_reporte.py. Cambia el numero
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
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 192 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V192_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada:
no inventa un hash.

Y EL DESFASE QUE NO SE REPARA SE DECLARA SIN TECLEAR SU ORDINAL. PATRONES_ACTA
sigue pidiendo el acta de VUELTA - 1, o sea la 191, cuando el acta que ORDENA
esta vuelta es la 192. El reporte de la 191 se llama a si mismo la SEPTIMA vuelta
del desfase; aqui NO se escribe "octava" a mano: se CUENTA cuantos reportes
archivados traen el literal `DESFASE DECLARADO` y se publican LAS DOS cifras, la
del texto de la 191 y la del conteo de hoy, con la discrepancia dicha en vez de
resuelta. La reparacion toca `tallar_cabecera_reporte.py`, que cuatro entradas de
la nomina nombran, y el acta 192 la deja FUERA de esta vuelta y DESPUES de la
bateria de la 194 en su `4.7`.

USO:
  python scripts/loop/vuelta192_esqueleto_reporte.py
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
VUELTA = 192
FUENTE_DEL_CLON = "scripts/loop/vuelta174_esqueleto_reporte.py"
FUNCION_CLONADA = "vuelta_del_reporte_del_arbol"
PATRONES_ACTA = [
    re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR" % (VUELTA - 1)),
    re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA %d" % (VUELTA - 1)),
]
PATRON_ACTA = "ACTA DE LA VUELTA %d DEL AUDITOR o ACTA DEL AUDITOR, VUELTA %d" % (
    VUELTA - 1, VUELTA - 1)
LITERAL_DESFASE = "DESFASE DECLARADO"

TAREAS = [
    ("1", 'LOS REGISTROS. BLOQUEANTE. El acta 192 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado. Con sus DIEZ adjudicaciones `4.1` a `4.10`, y las diez A FAVOR: siete son los discutibles del ejecutor (`D.1` a `D.7`, cuya numeracion en el reporte de la 191 va con el `D.7` escrito ANTES del `D.6`) y las tres restantes son las preguntas y los pendientes de doctrina contestados. OTRA VEZ CERO EN CONTRA, y si el arnes de la 191 ya cubre ese cero, SE DICE CON SU FICHERO en vez de re fabricarlo. Mas los TRES hallazgos de la seccion 5 que no salen de ningun discutible (los dos arneses `SUJETO VIVO` en `5.1`, la cuarta puerta del sello en `5.2`, y el segundo dato independiente sobre la marca contra la dificultad en `5.3`), DOS caidas propias del auditor escritas COMO DOS y ninguna omitida (la `C.1` es DE CIFRA PUBLICADA y va corregida por DECLARACION; la `C.2` es de metodo), CERO caidas del ejecutor que acumulen con las SEIS de metodo que el reporte de la 191 declara, y LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de puestos con su nota: 30 aislados y 28 cotejados, SOLAPE TOTAL a proposito. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido no escribe nada, y se prueba re corriendolo con la sede medida en bytes antes y despues'),
    ("2", 'LA RELECTURA AL DOBLE DEL TRAMO DE LA 191. BLOQUEANTE. La encarga el AUDITOR, que es donde `AUDITOR.md` 1.2 la pone, y esta vez CON MOTIVO DOBLE: el puesto `2832` cayo FUERA de los dudosos marcados de DOS lectores independientes en DOS tandas seguidas, la del ejecutor en la 191 y la del auditor en la 192. EL TRAMO son los 30 puestos de `docs/loop/SALIDA_V191_T2_CIEGA.txt`, que el bloque `H.3` del sello de apertura midio como el MISMO conjunto que `docs/loop/_auditor_v192_ciega_blind.txt`. AL DOBLE son sus 30 vecinos deterministas, con `vecinos()` IMPORTADA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada: 30 mas 30 son 60, el doble exacto. EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO: a `vecinos()` se le pasa `evitar` con TODO lo consumido, contado de sus SEIS ficheros y no tecleado. Con `scripts/loop/aislador_de_ciega.py`, criterio escrito literal, ciega y destape en ficheros SEPARADOS, las clases escritas y COMMITEADAS en su propio commit ANTES de abrir el destape, y los dudosos NOMBRADOS DELANTE. Y SI EL TRAMO VUELVE A TUMBAR A LOS DOS LECTORES EN LOS MISMOS PUESTOS, SE DICE CON SUS NUMEROS. NO SE TOCA NINGUNA CLASE: `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre solo en lectura y su `sha256` LF abre y cierra en el mismo valor por las dos convenciones'),
    ("3", 'LOS DOS ARNESES `SUJETO VIVO` DE LA 191, ANTES DE QUE ENTREN EN LA NOMINA. BLOQUEANTE, Y LO ES POR LA BATERIA DE LA 194. Es el hallazgo `5.1` del acta 192, corrido con la guarda de la casa y medido en `docs/loop/_auditor_v192_sujeto_vivo.txt`. (a) CORRER LA GUARDA `guarda_del_sujeto_congelado_separada()` y publicar sus TRES listas sobre los doce arneses de la 191, con sus nombres: si la medicion no da 2 y 6, la del ejecutor manda y la del auditor se declara equivocada, que para eso se publica el comando. (b) ARREGLAR LOS DOS `SUJETO VIVO` para que su sujeto quede CONGELADO, o DECLARAR EL CASO por el carril de los `CASO DECLARADO` que la casa ya tiene: la `4.4` del acta 191 adjudico que `SUJETO VIVO` es FALLO y no deuda, asi que dejarlos como estan no es opcion. (c) LOS SEIS `sin_motivo` NO SON FALLO PERO SI SON DEUDA: nombrarlos y decir, por cada uno, si su sujeto esta vivo de verdad o si solo le falta escribir el motivo, sin arreglarlos a ciegas. (d) NO SE TOCA LA NOMINA: no se poda, no se adelanta y no se le meten entradas nuevas, que la opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue rechazada. (e) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un arnes con sujeto vivo vuelve a colarse hacia la nomina sin declararse'),
    ("4", 'LA CUARTA PUERTA DEL SELLO DE LA APERTURA DEL AUDITOR. Es el hallazgo `5.2` del acta 192, levantado por el auditor CONTRA SI MISMO. `scripts/loop/apertura_del_auditor.py` impide tocar `git log`, `git status` y `REPORTE.md` antes del sello, y eso FUNCIONO; pero EL SUJETO DE LA CIEGA NO VIVE EN NINGUNO DE LOS TRES: vive en las razones y las clases de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, y por ahi se colo el auditor de la 192 con el sello ya escrito y sin romper ninguna guarda (los puestos 156 y 201 de su propia tanda). (a) AL SELLO SE LE ANADE LA CUARTA PUERTA: una funcion del propio fichero para leer el archivo que APUNTE SU TOQUE, y una comprobacion que CAIGA EN ROJO si el turno leyo `clase` o `razon` DE LOS PUESTOS SELLADOS antes de que las clases del auditor esten escritas. No se prohibe leer el archivo entero, que hace falta para el marcador: se prohibe destapar el sujeto. (b) DECIR EN EL PROPIO FICHERO LO QUE ESTA GUARDA NO PUEDE HACER, como su docstring ya hace con las otras tres. (c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si la cuarta puerta se quita. (d) NO SE CLONA EL FICHERO: `apertura_del_auditor.py` tiene nombre estable y sin numero de vuelta, y se le anade, no se le hace una version 2'),
    ("5", 'EL FORMATO UNICO DEL COTEJO DE CIEGA. Es el `P.2` del ejecutor, adjudicado A FAVOR en la `4.9` del acta 192. La TAREA 5 de la 191 midio que el universo se queda en 6 ficheros de 43, y tres cotejos de ciega DE VERDAD (los del 183, 184 y 190) quedan fuera POR FORMATO y no por fondo. ES UN FORMATO ANTES QUE UNA RE MEDICION: (a) ESCRIBIR EL FORMATO UNICO del cotejo de ciega, con nombre estable y sin numero de vuelta, que lleve como minimo y explicitos el puesto, la clase del lector, la clase del archivo, si el puesto estaba en los dudosos del lector, y el COINCIDE o DISCREPA, y que deje el DENOMINADOR RECUPERABLE, porque dos de los seis ficheros de hoy solo listan discrepancias. (b) UN LECTOR QUE LEA LOS FORMATOS VIEJOS y publique CUANTOS de los 43 pasa a recuperar, con sus nombres, y cuantos siguen fuera y por que, con la cifra de antes y la de despues LAS DOS JUNTAS. (c) NO SE RE MIDE LA MARCA CONTRA LA DIFICULTAD EN ESTA VUELTA: el universo nuevo se usa cuando este medido y declarado, no en el mismo acto en que se construye. (d) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un cotejo del formato nuevo no permite recuperar el denominador'),
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


def reportes_con_el_literal(directorio=None, literal=None):
    """LOS REPORTES ARCHIVADOS QUE TRAEN EL LITERAL DEL DESFASE. Devuelve una
    lista de (nombre, apariciones), ordenada por nombre.

    Semi-pura: lo unico que toca disco es leer el directorio. `directorio` y
    `literal` van por parametro para que se pueda correr sobre uno fabricado.
    EXISTE PARA NO TECLEAR UN ORDINAL: el reporte de la 191 se llama a si mismo
    la SEPTIMA vuelta del desfase, y esa palabra no sale de ningun instrumento.
    Aqui se cuenta lo que si se puede contar, y las dos cifras se publican."""
    base = directorio or os.path.join(LOOP, "reportes")
    lit = literal or LITERAL_DESFASE
    salida = []
    if not os.path.isdir(base):
        return salida
    for nombre in sorted(os.listdir(base)):
        if not nombre.lower().endswith(".md"):
            continue
        t = io.open(os.path.join(base, nombre), encoding="utf-8",
                    errors="replace").read()
        if lit in t:
            salida.append((nombre, t.count(lit)))
    return salida


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

    # EL ORDINAL DEL DESFASE NO SE TECLEA: SE CUENTA LO QUE SE PUEDE CONTAR.
    con_literal = reportes_con_el_literal()
    print("EL DESFASE, CONTADO EN VEZ DE TECLEADO:")
    for nombre, veces in con_literal:
        print("   %-28s trae %r %d vez(ces)" % (nombre, LITERAL_DESFASE, veces))
    print("   CIFRA reportes archivados con el literal: %d" % len(con_literal))
    print("")

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
    # linea. Se leen las dos y **se dice cual de las dos fue**, en vez de teclear
    # un cero.
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

    lista_literal = ", ".join("`%s`" % n for n, _v in con_literal) or "(ninguno)"

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
> **VAN CINCO SUB-TAREAS Y DOS SON BLOQUEANTES. El tope de cinco no hace falta
> volver a ganarlo:** esta vigente desde la `4.10` del acta 190. **Y la cifra que
> lo sostiene se REMIDIO en esta vuelta en vez de heredarse**, tal como el encargo
> manda: el bloque **B.2** del sello de apertura busco en git los commits de
> cierre y midio sus ficheros `SALIDA_V<n>_CERRAR_REPORTE.txt` uno a uno, **y
> cuando vi que mi ventana estaba tecleada escribi un instrumento que cuenta del
> inventario ENTERO**, `scripts/loop/vuelta%(v)d_racha_de_cierres.py`. Las cifras
> que andan dando vueltas se publican JUNTAS en la seccion 0.
>
> **DONDE SE TALLO ESTE ESQUELETO: EN LA APERTURA Y EN SU PROPIO COMMIT.** Desde
> el segundo commit de esta vuelta ya hay reporte parcial en el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** ni cribado, ni
> recomputo, ni operaciones del plan, ni las mesas anotadas, ni **podar la
> nomina** (la opcion `c` que el fundador RECHAZO el 5 sep 2026: **la nomina
> sigue creciendo y nadie la poda sin el fundador**), ni la bateria, que cae en
> la 194. **Y siguen fuera, nombradas para que la 193 no las redescubra:** el
> desfase de `PATRONES_ACTA`, **que se encarga DESPUES de la 194** porque toca
> `tallar_cabecera_reporte.py` y cuatro entradas de la nomina lo nombran;
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
  **una cita de la salida de un instrumento**.

```
%(asunto)s
```
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA.** La linea de arriba nombra el
  acta **%(ant)d** porque `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que
  ORDENA esta vuelta es la %(v)d**. Es el `D.2` del reporte de la 184, adjudicado
  a favor con reparacion encargada por la `5.2` del acta 185, **y la `4.7` del
  acta 192 lo deja expresamente DESPUES de la bateria de la 194**. El reporte de
  la 191 se llama a si mismo **la SEPTIMA vuelta** del desfase; **esa palabra no
  sale de ningun instrumento, asi que aqui no se copia ni se le suma uno a ojo**:
  lo que si se puede contar es que **%(n_lit)d reportes archivados traen el
  literal `DESFASE DECLARADO`** (%(lista_lit)s), contados por
  `reportes_con_el_literal()` de este mismo fichero. **LAS DOS CIFRAS SE PUBLICAN
  Y LA DISCREPANCIA SE DECLARA EN VEZ DE RESOLVERSE COPIANDO.**
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
           n_lit=len(con_literal), lista_lit=lista_literal,
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
    print("   reportes archivados con el literal del desfase: %d" % len(con_literal))
    print("   filas de tarea abiertas: %d" % len(TAREAS))
