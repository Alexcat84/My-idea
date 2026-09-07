# -*- coding: utf-8 -*-
r"""vuelta196_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 196,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta195_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS (que BAJA de CUATRO filas a DOS), este docstring y el
bloque de prosa del encabezado.

Y LA SECCION 8.1 DE LA FUENTE SE LEYO ANTES DE CLONAR, que es la disciplina que
la `C.3` del reporte de la 194 dejo escrita. Las cuatro caidas `C.1` a `C.4` de
esa seccion son DE METODO y ninguna vive en este fichero, asi que por esa via no
hay remedio que aplicar aqui, y se dice en vez de callarlo.

POR QUE DOS TAREAS Y NO CINCO, Y LA CIFRA NO SE TECLEA: la racha de cierres,
contada del instrumento en el bloque `E` del sello de apertura de ESTA vuelta,
vale 1. `AUDITOR.md` 6.2 pide DOS vueltas seguidas cerrando su propio reporte
con `cerrar_reporte.py` para devolver el tope de cinco.

ESTA VUELTA NO ES DE BATERIA (AUDITOR.md 6.1, decision del fundador del 5 sep
2026): la bateria corre CADA CINCO VUELTAS en una vuelta propia QUE NO LLEVA NADA
MAS, la 194 la corrio entera por sus diez tramos y la proxima cae en la 199. Su
seccion 9 cierra con EL HUECO DECLARADO Y MEDIDO por el carril de la TAREA 1.b de
la vuelta 173, con su medicion, su atribucion y su corrida.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 196 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V196_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada.

EL DESFASE DE PATRONES_ACTA NO SE REPARA AQUI, Y ES DECISION DEL AUDITOR Y NO UN
OLVIDO MIO: apunta al acta de VUELTA - 1 y el acta que ORDENA esta vuelta es la
196. El encargo de la 196 lo deja EXPRESAMENTE FUERA, y ademas lo nombra con su
cuenta: LLEVA CUATRO ENCARGOS EN PRIMER LUGAR DE LA COLA SIN HACERSE, y pierde
contra las tres que el propio encargo pone delante. LA CIFRA DEL ORDINAL SIGUE
LLEVANDO SU FECHA DE CORTE, por banco 9.21.

USO:
  python scripts/loop/vuelta196_esqueleto_reporte.py
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
VUELTA = 196
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
    ("1", 'LOS REGISTROS. BLOQUEANTE. El acta 196 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, y el cuerpo del acta se acota contando su primera linea con `grep -n` EN ESTA VUELTA, no por la linea que el encargo cita. La entrada registra, y cada cifra se cuenta del cuerpo acotado: LAS CATORCE ADJUDICACIONES `4.1` a `4.14`, Y LAS CATORCE A FAVOR (cuatro son las discrepancias de la ciega del propio auditor resueltas a favor del archivo, tres son mis preguntas `P.1`, `P.2` y `P.3` contestadas por extension citable, y siete son mis discutibles `D.1` a `D.7`), CERO EN CONTRA y es la SEXTA acta seguida; LOS TRES HALLAZGOS DE LA SECCION 5 que no salen de ningun discutible (`5.1` el encargo que quema puestos de la ciega siguiente, `5.2` los mismos cuatro puestos fallados por dos lectores independientes, `5.3` la ciega que no puede alcanzar la clase de un puesto cuya correccion se apoya en una fusion planeada y no aplicada); UNA CAIDA MIA Y ES DE CIFRA PUBLICADA, NO DE REPORTE, la `C.E1`, con LA RACHA DE CIFRA PUBLICADA EN 1; MIS CUATRO CAIDAS DE METODO `C.1` a `C.4`, las cuatro cazadas dentro de la vuelta por guardas que yo mismo escribi y NINGUNA ACUMULA; UNA CAIDA PROPIA DEL AUDITOR, `C.A1`, DE METODO Y CON SU RACHA EN 2, con la escalada nombrada para la 197; y LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de puestos (60 aislados, 60 cotejados y DOS QUEMADOS, el `654` y el `719`) y la fila de caidas propias PARTIDA EN DOS. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se prueba re corriendolo, con la sede medida en bytes antes y despues'),
    ("2", 'LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. BLOQUEANTE, Y ES DEUDA SUYA QUE PAGA EL EJECUTOR CON EL INSTRUMENTO. `AUDITOR.md` 1.2: UNA discrepancia del auditor cayo FUERA de su marcado, el `2428`, asi que EL CREDITO DE SU TANDA BAJA Y EL TRAMO SE RELEE AL DOBLE. El tramo y el doble estan CERRADOS DESDE ANTES, computados y no tecleados, en `docs/loop/_auditor_v196_doble_para_la_197.txt`, para que no se elijan despues de mirar. SON CIENTO VEINTE PARES, y la serie medida va 30, 60 y ahora 120. (a) `vecinos()` SE IMPORTA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y NO se copia, con `evitar` cargado de TODO lo consumido y RECONTADO de sus ficheros en esta vuelta; el solape con el tramo y con el universo tiene que salir CERO POR CONSTRUCCION, no por suerte. (b) LEER LOS 120 A CIEGAS, tramo y doble, con `aislador_de_ciega.py`, y escribir las clases ANTES de abrir el destape. (c) LA VARA ES `docs/BANCO_DE_TEXTOS.md` `9.6.1`, citada por numero y no parafraseada, con sus precisiones `9.6.2` y `9.6.3`, Y CON LOS DOS ERRORES COMPARTIDOS PUESTOS DELANTE: la vara es EL SUELO Y NO EL TECHO (antes de aplicarla se pregunta si el par pertenece a una familia con REGLA PROPIA ya fijada), y LA SEMEJANZA DE LOS IDS NO DECIDE (`9.6.3` dice que el tamano del solape no decide y que se pesa el resto y en que lado). (d) NO SALTARSE LA `B` NI SOBRE EMITIRLA: el sesgo esta medido en las dos direcciones y las dos son perdida. (e) PUBLICAR EL COTEJO con sus cifras, cuantos coinciden, cuantos discrepan, y cuales caen dentro y fuera del marcado, con los discutibles marcados ANTES de saber si se acierta. (f) EL PUESTO INALCANZABLE A CIEGAS por el hallazgo `5.3` se DECLARA con su numero y su medicion y SALE DEL CREDITO, y NO se arregla'),
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
    EXISTE PARA NO TECLEAR UN ORDINAL, y su cifra ENVEJECE: por eso desde la
    vuelta 193 se publica CON SU FECHA DE CORTE (banco 9.21)."""
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


def fecha_de_corte_del_arbol():
    """LA FECHA DE CORTE DE LAS CIFRAS DE ESTE ESQUELETO, LEIDA DE GIT Y NO
    TECLEADA (banco 9.21). Devuelve la fecha ISO del HEAD, que es el estado del
    arbol que se acaba de contar. Si git no responde devuelve None, y entonces
    LA CIFRA NO SE PUBLICA CON UN CORTE INVENTADO: se dice que no hay corte."""
    c, o = git(["log", "-1", "--format=%ad", "--date=short"])
    o = o.strip()
    return o if c == 0 and re.match(r"^\d{4}-\d{2}-\d{2}$", o) else None


def racha_del_sello(texto):
    """LA RACHA DE CIERRES, LEIDA DEL SELLO DE APERTURA DE ESTA VUELTA Y NO
    TECLEADA. Devuelve (racha, cuales) o (None, None) si el sello no la trae.
    PURA: recibe el texto del sello.

    EXISTE PORQUE EL TOPE DE SUB-TAREAS DEPENDE DE ESA CIFRA (AUDITOR.md 6.2) y
    la cabecera de este reporte la publica. Una cifra que gobierna el tamano del
    encargo no se puede teclear."""
    if not texto:
        return None, None
    m = re.search(r"CIFRA racha de cierres, contada del inventario ENTERO:\s*(\d+)",
                  texto)
    q = re.search(r"las vueltas de la racha:\s*(.+)", texto)
    return (m.group(1) if m else None), (q.group(1).strip() if q else None)


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
        print("   por busqueda NO ANCLADA, con exactamente 1 acierto.")
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

    # LA RACHA NO SE TECLEA: SE LEE DEL SELLO DE APERTURA DE ESTA VUELTA, que la
    # conto del instrumento ANTES de la primera operacion.
    ruta_sello = os.path.join(LOOP, "SALIDA_V%d_APERTURA.txt" % VUELTA)
    texto_sello = (io.open(ruta_sello, encoding="utf-8", errors="replace").read()
                   if os.path.exists(ruta_sello) else "")
    racha, cuales_racha = racha_del_sello(texto_sello)
    print("LA RACHA DE CIERRES, LEIDA DEL SELLO DE APERTURA Y NO TECLEADA:")
    print("   fichero: docs/loop/SALIDA_V%d_APERTURA.txt (%d bytes)"
          % (VUELTA, len(texto_sello.encode("utf-8"))))
    print("   CIFRA racha: %s | las vueltas: %s" % (racha, cuales_racha))
    print("")
    if racha is None:
        fallos.append("el sello de apertura no trae la cifra de la racha; el tope "
                      "de sub-tareas depende de ella y no se teclea")

    # EL ORDINAL DEL DESFASE NO SE TECLEA: SE CUENTA LO QUE SE PUEDE CONTAR, Y
    # DESDE LA VUELTA 193 LA CIFRA VA CON SU FECHA DE CORTE (banco 9.21).
    con_literal = reportes_con_el_literal()
    corte = fecha_de_corte_del_arbol()
    print("EL DESFASE, CONTADO EN VEZ DE TECLEADO:")
    for nombre, veces in con_literal:
        print("   %-28s trae %r %d vez(ces)" % (nombre, LITERAL_DESFASE, veces))
    print("   CIFRA reportes archivados con el literal: %d" % len(con_literal))
    print("   FECHA DE CORTE de esa cifra: %s" % (corte or "(no legible de git)"))
    print("")
    if corte is None:
        fallos.append("no se pudo leer la fecha de corte de git; una cifra de "
                      "inventario sin corte no se publica (banco 9.21)")

    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, "scripts/loop/tallar_cabecera_reporte.py",
                        "--fase04", "--vuelta", str(VUELTA)],
                       cwd=RAIZ, capture_output=True, env=env)
    sal_tallador = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
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
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA NO ES VUELTA DE BATERIA.** `AUDITOR.md` 6.1, decision del fundador del 5
> sep 2026: la bateria corre **CADA CINCO VUELTAS** en una vuelta propia **que no
> lleva nada mas**, **la 194 la corrio entera por sus diez tramos** y **la proxima
> cae en la 199**. **La seccion 9 de este reporte cierra con el HUECO DECLARADO Y
> MEDIDO** por el carril de la TAREA 1.b de la vuelta 173, con su medicion, su
> atribucion y su corrida. **Un hueco declarado no es un hueco escondido.**
>
> **VAN DOS SUB-TAREAS Y LAS DOS SON BLOQUEANTES, Y LA CIFRA QUE LO MANDA NO SE
> TECLEA.** El bloque `E` del sello de apertura de esta vuelta corrio el
> instrumento de la racha sobre el inventario ENTERO y **la racha de cierres vale
> %(racha)s**, con las vueltas **%(cuales)s**. `AUDITOR.md` 6.2 pide **DOS vueltas
> seguidas** cerrando su propio reporte con `cerrar_reporte.py` para devolver el
> tope de cinco, **y con 1 el tope es de DOS**. **Lo que esta en mi mano y esta
> vuelta hace: sellar `docs/loop/SALIDA_V%(v)d_CERRAR_REPORTE.txt`**, con lo que la
> racha llega a 2 y el tope de cinco vuelve solo en la 197.
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. Eso funciono en la 195 y **no se
> deshace**. **El desfase de calibrado se midio DENTRO del bloque de apertura y
> ANTES de la primera operacion.** Y el bloque `E` trae **el remedio de la caida
> `C.E1`** que el acta 196 me registra: **el nombre del instrumento de la racha ya
> no se teclea en la prosa**, sale de la constante que se ejecuta, y **se comprueba
> que existe y no mide cero bytes ANTES de correrlo**.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina**, ni **la bateria entera**, que no es su
> vuelta y cae en la 199. **Y siguen fuera, nombradas en el orden del encargo para
> que la 197 no las redescubra:** que `cerrar_reporte.py` escriba su propia salida
> sellada; **el tope de 80 lineas del modo austero**, adjudicado en la `4.7` del
> acta 196 **en contra mia**, con el encargo de **medir este reporte por las dos
> varas y publicar las dos cifras**; la guarda de la `P.2` con su calibrado antes
> que sus dientes; **el desfase de `PATRONES_ACTA`, que lleva CUATRO encargos en
> primer lugar de la cola sin hacerse**; la fila de credito del acta con su rotulo
> impuesto por el instrumento; la guarda de codigo del hallazgo `5.3` del acta 194;
> `acumulan()` que lea la tabla; el cotejo de clon declarado; la excepcion que
> publica siempre su lista; el censo de arneses con carril de mutacion sin fichero
> propio; las ocho actas sin entrada propia en la serie (173 a 180); que el campo
> `evidencia` de `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE
> MUEVE: sigue en `LISTA`**; y **QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO**, y
> ahora tambien **LOS CUATRO PUESTOS QUE DOS LECTORES INDEPENDIENTES FALLARON**
> (`976`, `2428`, `2662`, `3173`), nombrados y medidos y **no resueltos, porque
> mover una clase es del RECOMPUTO**.
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta%(v)d_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `%(rama)s`
- commit del acta de la vuelta %(ant)d: `%(acta8)s`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
%(asunto)s
```
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA, Y LLEVA SU FECHA DE CORTE.** La
  linea de arriba nombra el acta **%(ant)d** porque `PATRONES_ACTA` pide la de
  `VUELTA - 1`, y **el acta que ORDENA esta vuelta es la %(v)d**. Es el `D.2` del
  reporte de la 184, adjudicado a favor con reparacion encargada por la `5.2` del
  acta 185, **y el encargo de esta vuelta lo deja EXPRESAMENTE FUERA y ademas lo
  nombra con su cuenta: CUATRO encargos en primer lugar de la cola sin hacerse**.
  Lo que si se puede contar: **%(n_lit)d reportes archivados traen el literal
  `DESFASE DECLARADO`** (%(lista_lit)s), contados por `reportes_con_el_literal()`
  de este mismo fichero, **con FECHA DE CORTE %(corte)s** (banco `9.21`, TODA
  CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Un inventario que crece cada vuelta
  sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V%(v)d_HEAD_APERTURA.txt`: `%(head8)s`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `%(nac8)s`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **%(pisa)d**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta %(v)d`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: %(frase_tallador)s, y de las lineas de
rojo que imprima, **%(n_ap)d mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
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
""" % dict(v=VUELTA, ant=VUELTA - 1, pisa=n_arbol, rama=rama,
           acta8=acta_hash[:8], asunto=repr(acta_asunto), head8=head_ap[:8],
           nac8=nac_hash[:8], celdas=celdas, n_ap=len(lado_apertura_roto),
           filas=filas, n_lit=len(con_literal), lista_lit=lista_literal,
           corte=corte, frase_tallador=frase_tallador, racha=racha,
           cuales=cuales_racha)

    io.open(ruta, "w", encoding="utf-8", newline="\n").write(texto)
    print("ESQUELETO ESCRITO: docs/loop/REPORTE.md (%d bytes, %d lineas por count(NL))"
          % (len(texto.encode("utf-8")), texto.count(chr(10))))
    print("   rama leida de git: %s" % rama)
    print("   acta %d leida de git log: %s  %s" % (VUELTA - 1, acta_hash[:8], acta_asunto[:70]))
    print("   HEAD de apertura leido del sello: %s" % head_ap[:8])
    print("   nacimiento del bloque de apertura, --diff-filter=A: %s" % nac_hash[:8])
    print("   reporte pisado, leido de su cabecera: vuelta %d" % n_arbol)
    print("   celdas ilegibles que el tallador imprime HOY: %s" % celdas)
    print("   racha de cierres leida del sello: %s" % racha)
    print("   reportes con el literal del desfase: %d, corte %s"
          % (len(con_literal), corte))
