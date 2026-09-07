# -*- coding: utf-8 -*-
r"""vuelta197_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 197,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta196_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS (que SUBE de DOS filas a CUATRO), este docstring y el
bloque de prosa del encabezado. El codigo de las funciones va igual.

Y LA SECCION 8.1 DE LA FUENTE SE LEYO ANTES DE CLONAR, que es la disciplina que
la `C.3` del reporte de la 194 dejo escrita.

POR QUE CUATRO TAREAS Y NO DOS, Y LA CIFRA NO SE TECLEA: la racha de cierres,
contada del instrumento en el bloque `E` del sello de apertura de ESTA vuelta,
vale 2, con las vueltas 195 y 196. `AUDITOR.md` 6.2 apaga el regimen temporal de
dos sub-tareas cuando DOS VUELTAS SEGUIDAS cierran su propio reporte con
`cerrar_reporte.py`, y entonces vuelve el tope de CINCO. El encargo trae CUATRO.
LA CIFRA SE LEE DEL SELLO, con `racha_del_sello()`, y si el sello no la trae este
esqueleto CAE EN ROJO y no escribe nada.

ESTA VUELTA NO ES DE BATERIA (AUDITOR.md 6.1, decision del fundador del 5 sep
2026): la 194 la corrio entera por sus diez tramos y la proxima cae en la 199. Su
seccion 9 cierra con EL HUECO DECLARADO Y MEDIDO por el carril de la TAREA 1.b de
la vuelta 173, con su medicion, su atribucion y su corrida.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 197 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V197_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada.

EL DESFASE DE PATRONES_ACTA NO SE REPARA AQUI, Y ES DECISION DEL AUDITOR Y NO UN
OLVIDO MIO: apunta al acta de VUELTA - 1 y el acta que ORDENA esta vuelta es la
197. El encargo de la 197 no lo trae entre sus cuatro sub-tareas, y LA CIFRA DEL
ORDINAL SIGUE LLEVANDO SU FECHA DE CORTE, por banco 9.21.

USO:
  python scripts/loop/vuelta197_esqueleto_reporte.py
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
VUELTA = 197
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
    ("1", 'LOS REGISTROS. BLOQUEANTE. El acta 197 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, y el cuerpo del acta se acota contando su primera linea con `grep -n` EN ESTA VUELTA. La entrada registra, y cada cifra se cuenta del cuerpo acotado: LAS SIETE ADJUDICACIONES `4.1` a `4.7`, con las tres preguntas del reporte de la 196 contestadas POR LETRA ESCRITA y no por doctrina nueva (`4.3` la `P.1`, `4.4` la `P.2`, `4.5` la `P.3`); LOS CUATRO HALLAZGOS de la seccion 5 (`5.1` el reporte que quema la ciega del auditor por construccion, `5.2` el marcado de discutibles que no existe por debajo del puesto 2662, `5.3` los tres puestos con tres lectores independientes contra el archivo, `5.4` el fichero del turno que no se limpia al cerrar); CERO CAIDAS DEL EJECUTOR DE CIFRA PUBLICADA, con la `C.E1` de la 196 RE CLASIFICADA A MI FAVOR como caida de REPORTE en prosa de acompanamiento, que NO acumula; MIS DOS CAIDAS DE METODO; y CINCO CAIDAS PROPIAS DEL AUDITOR, `C.A1` a `C.A5`, todas de metodo y todas remediadas dentro de su vuelta, con la `C.A1` en su TERCERA acta seguida de la misma especie. Y LA METRICA DE CREDITO de la seccion 7 con sus cifras. EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se prueba re corriendolo, con la sede medida en bytes antes y despues, y CADA LECTOR NUEVO LLEVA SU MUTACION DELANTE'),
    ("2", 'EL ORDEN DEL TURNO DEL AUDITOR PASA A CODIGO. BLOQUEANTE. Sale de la adjudicacion `4.5` del acta 197, que contesta mi `P.3` por extension de `AUDITOR.md` 1.2, y esta MEDIDO: el reporte de la 196 publico la clase de archivo de 8 de los 120 puestos que el auditor de la 197 acababa de sellar. Sobre `scripts/loop/apertura_del_auditor.py`, QUE NO SE CLONA: (a) `leer_reporte()` APUNTA SU TOQUE Y CAE EN ROJO si el turno tiene sello y no ha declarado sus clases todavia, con lo que el orden obligatorio pasa a ser `sellar()` -> clasificar -> `--declarar-clases` -> `leer_reporte()`, y un turno SIN sello sigue pudiendo leer el reporte. (b) EL FICHERO DEL TURNO SE CIERRA, que es el hallazgo `5.4`: un carril que lo cierre al declarar las clases dejando constancia, de forma que un turno nuevo empiece limpio SIN TENER QUE BORRAR NADA, con el sello en disco intacto y la guarda `b` de `sellar()` mirando el disco igual que antes. (c) LA GUARDA DE CODIGO DE LA `C.A1`, que va por su TERCERA acta seguida: comprueba que la cifra del marcador que un acta publica calza con una salida de `AP.marcador()` de esa misma vuelta, y CAE EN ROJO si esa salida no existe o no calza. CADA UNA DE LAS TRES LLEVA SU CASO POSITIVO POR MUTACION DELANTE, con nombre estable y salida sellada, y el caso rojo tiene que MORDER: sin el remedio la guarda deja pasar y con el no'),
    ("3", 'LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. Es deuda suya que paga el ejecutor con el instrumento. `AUDITOR.md` 1.2: CINCO discrepancias del auditor cayeron FUERA del marcado del archivo (`655`, `719`, `976`, `1809`, `1810`), asi que el credito de su tanda baja y el tramo se relee al doble. EL TRAMO Y EL DOBLE ESTAN CERRADOS DESDE ANTES, computados y no tecleados, en `docs/loop/_auditor_v197_doble_para_la_198.txt`: SON 240 PARES, 120 del tramo y 120 del doble, y la serie medida va 30, 60, 120 y ahora 240. (a) `vecinos()` SE IMPORTA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y `puestos_de()`, `numeros_de()` y `UNIVERSO_CONSUMIDO` de `scripts/loop/vuelta196_tarea2_relectura_al_doble.py`, y NADA se copia; se RECOMPUTA el doble y se comprueba que calza con el sellado, ESQUIVANDO LA TRAMPA DE LA `C.A5` (los `_exclusion.txt` guardan enteros sueltos y se leen con `numeros_de()`). (b) LEER LOS 240 A CIEGAS con `aislador_de_ciega.py` y escribir las clases ANTES de abrir el destape. (c) LA VARA es `9.6.1` con `9.6.2`, `9.6.3` y la tabla de LOS DOS POLOS del `9.22`, y CON LOS DOS ERRORES DEL AUDITOR DELANTE: la vara es el SUELO y no el TECHO (familia con regla propia manda), y la contencion se mide SOBRE EL CONTENIDO y no sobre el contenedor. (d) NO SALTARSE LA `B` NI SOBRE EMITIRLA. (e) PUBLICAR EL COTEJO con sus cifras y los discutibles marcados ANTES de saber si acierto, MAS el reparto por puesto del literal `DISCUTIBLE MARCADO` que el hallazgo `5.2` obliga. (f) LOS PUESTOS QUE LA CIEGA NO PUEDE ALCANZAR se declaran ANTES de leer y salen del credito. (g) LOS QUEMADOS por el acta y por el reporte se declaran ANTES de leer y no entran al credito'),
    ("4", 'LAS DOS CIFRAS QUE VIAJAN SIN SU VARA. (a) LA SECCION 9 PUBLICA "0 ARNESES DEL CENSO FUERA DE LA NOMINA" SIN NOMBRAR LA VARA. No es caida (la frase nombra su fuente y esa fuente si lleva la vara, adjudicacion `4.7`), pero un `0` al lado de un censo y una nomina de tres cifras se lee como que la nomina cubre el censo entero, y no lo cubre. Esa cifra pasa a viajar SIEMPRE CON SU VARA, en el sello de apertura y en el reporte, y se miden LAS DOS: con vara y sin vara. (b) EL TOPE DE 80 LINEAS DEL MODO AUSTERO SE MIDE POR TRES VARAS Y LAS TRES SE PUBLICAN, por la adjudicacion `4.6`: total, escrita a mano (la vara que el acta 196 fijo en su `4.7`), y escrita a mano menos lo que otra regla obliga a escribir. EL TOPE NO SE AFLOJA Y LA EXCEPCION NO SE INVENTA: se publican las tres cifras para que el fundador decida sobre numeros, y si la tercera vara sigue por encima de 80 SE DICE CON ESAS PALABRAS y la pregunta queda escrita'),
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


def varas_de_la_nomina(texto):
    """LAS DOS CIFRAS DE LA TAREA 4.a, LEIDAS DEL SELLO DE APERTURA Y NO
    TECLEADAS. Devuelve (vara, con_vara, sin_vara) o (None, None, None).
    PURA: recibe el texto del sello.

    EXISTE PORQUE LA CIFRA DE FUERA DE LA NOMINA NO PUEDE VIAJAR SOLA: la
    adjudicacion 4.7 del acta 197 dice que un 0 sin su vara se lee como
    cobertura total del censo, y no lo es."""
    if not texto:
        return None, None, None
    a = re.search(r"CIFRA arneses del censo FUERA de la nomina CON LA VARA "
                  r"(\d+):\s*(\d+)", texto)
    b = re.search(r"CIFRA arneses del censo FUERA de la nomina SIN VARA "
                  r"\(vara=0\):\s*(\d+)", texto)
    if not a or not b:
        return None, None, None
    return a.group(1), a.group(2), b.group(1)


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

    # LAS DOS VARAS DE LA NOMINA, TAREA 4.a, TAMBIEN LEIDAS DEL SELLO.
    vara, con_vara, sin_vara = varas_de_la_nomina(texto_sello)
    print("LAS DOS VARAS DE LA NOMINA, LEIDAS DEL SELLO Y NO TECLEADAS:")
    print("   vara %s | fuera CON vara: %s | fuera SIN vara: %s"
          % (vara, con_vara, sin_vara))
    print("")
    if vara is None:
        fallos.append("el sello de apertura no trae las dos cifras de la nomina "
                      "con y sin vara; la TAREA 4.a depende de ellas")

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
> **EL TOPE DE CINCO SUB-TAREAS VOLVIO SOLO, Y LA CIFRA QUE LO MANDA NO SE
> TECLEA.** El bloque `E` del sello de apertura de esta vuelta corrio el
> instrumento de la racha sobre el inventario ENTERO y **la racha de cierres vale
> %(racha)s**, con las vueltas **%(cuales)s**. `AUDITOR.md` 6.2 apaga el regimen
> temporal de dos sub-tareas cuando **DOS vueltas seguidas** cierran su propio
> reporte con `cerrar_reporte.py`, **y entonces vuelve el tope de CINCO**. **Este
> encargo trae CUATRO, y cabe.**
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. **El desfase de calibrado se midio
> DENTRO del bloque de apertura y ANTES de la primera operacion.** Y trae **el
> remedio de la TAREA 4.a en su bloque `F`**: la cifra de arneses del censo fuera
> de la nomina **ya no puede viajar sin su vara**, porque se miden **las dos**, con
> vara **%(vara)s** salen **%(conv)s** y sin vara salen **%(sinv)s**.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina**, ni **la bateria entera**, que no es su
> vuelta y cae en la 199. **Y siguen fuera, nombradas para que la 198 no las
> redescubra:** el desfase de `PATRONES_ACTA`, que apunta al acta de `VUELTA - 1`
> cuando el acta que ORDENA esta vuelta es la %(v)d; la guarda de codigo del
> hallazgo `5.3` del acta 194; `acumulan()` que lea la tabla; el cotejo de clon
> declarado; las ocho actas sin entrada propia en la serie (173 a 180); el estado
> de `OP-L-02`, **que NO se mueve y sigue en `LISTA`**; **QUE HACER CON LAS FILAS
> `B` DEL ARCHIVO**; y **los puestos que dos o tres lectores independientes
> fallaron**, nombrados y medidos y **no resueltos, porque mover una clase es del
> RECOMPUTO**.
>
> **NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO:** el `sha256` LF de
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
  acta 185, **y el encargo de esta vuelta no lo trae entre sus cuatro sub-tareas**.
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

## 1. LAS CUATRO TAREAS DEL ENCARGO, Y SU ESTADO

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
           cuales=cuales_racha, vara=vara, conv=con_vara, sinv=sin_vara)

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
    print("   las dos varas de la nomina leidas del sello: %s | %s | %s"
          % (vara, con_vara, sin_vara))
    print("   reportes con el literal del desfase: %d, corte %s"
          % (len(con_literal), corte))
