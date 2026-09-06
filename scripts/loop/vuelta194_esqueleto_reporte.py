# -*- coding: utf-8 -*-
r"""vuelta194_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 194,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta193_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS (que baja de cinco filas a TRES), este docstring y el
bloque de prosa del encabezado, porque ESTA VUELTA SI ES DE BATERIA.

ESTA VUELTA ES DE BATERIA (AUDITOR.md 6.1, decision del fundador del 5 sep 2026):
la bateria corre CADA CINCO VUELTAS en una vuelta propia QUE NO LLEVA NADA MAS, y
la 189 la corrio entera. Su seccion 9 NO cierra con hueco declarado: cierra con
la bateria corrida, por tramos, con su doble corrida, su reloj y su salida
sellada.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 194 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V194_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada.

EL DESFASE DE PATRONES_ACTA NO SE REPARA AQUI: apunta al acta de VUELTA - 1 y el
acta que ORDENA esta vuelta es la 194. El acta 193 lo dejo expresamente DESPUES
de la bateria de la 194, y el encargo de la 194 lo repite: la 195 es el sitio.
LA CIFRA DEL ORDINAL SIGUE LLEVANDO SU FECHA DE CORTE, por banco 9.21.

USO:
  python scripts/loop/vuelta194_esqueleto_reporte.py
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
VUELTA = 194
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
    ("1", 'LOS REGISTROS. BLOQUEANTE. El acta 194 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado. Registra LAS DIEZ ADJUDICACIONES `4.1` a `4.10`, las diez A FAVOR (siete son los discutibles `D.1` a `D.7` del reporte de la 193 y las tres restantes son las preguntas `P.1`, `P.2` y `P.3` contestadas por extension citable), CERO EN CONTRA y es la CUARTA acta seguida; LOS TRES HALLAZGOS DE LA SECCION 5 que no salen de ningun discutible (`5.1` los dos arneses de la cuarta puerta que se contradicen en la sede de verdad, `5.2` la seccion 8 que dice cuatro donde el instrumento dice cinco, `5.3` los mensajes de commit del bucle que queman la ciega del auditor antes de su primer comando); UNA CAIDA DEL EJECUTOR, DE REPORTE, QUE **SI ACUMULA** (el hallazgo `5.2`: vive solo en `REPORTE.md`, no mueve ningun dato y vive en una CONCLUSION, luego cuenta para la racha por la letra del 27 ago 2026; **RACHA DE REPORTE 1**, y no hay escalada que encargar porque se dispara a DOS); TRES CAIDAS DEL EJECUTOR DE METODO `C.1` a `C.3`, declaradas por el propio ejecutor en su seccion 8.1, que se registran y NO abren racha; DOS CAIDAS PROPIAS DEL AUDITOR, la primera grave (`C.1`, ROMPER UN REMEDIO ESCRITO, que CUENTA PARA LA PARADA por la letra del 5 sep 2026: el sello de la vuelta 194 SALIO ROJO y no existe) y la segunda de metodo (`C.2`, haber commiteado `docs/loop/_TURNO_DEL_AUDITOR.json`, que es estado de turno y no contenido de campana); y LA METRICA DE CREDITO de la seccion 7 con su fila de puestos y su nota: 30 aislados, 30 cotejados, ONCE QUEMADOS por el contexto de sesion y no por comando del auditor, y el cotejo publicado dos veces, sobre los 30 y sobre los 19 limpios. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se prueba re corriendolo, con la sede medida en bytes antes y despues'),
    ("2", 'LOS DOS ARNESES DE LA CUARTA PUERTA QUE SE CONTRADICEN. BLOQUEANTE, Y ES LA PRECONDICION DE LA BATERIA. Es el hallazgo `5.1` del acta 194, corrido y no deducido en `docs/loop/_auditor_v194_cuarta_puerta_rota.txt` con sus tres casos: `vuelta192_tarea4_mutacion_cuarta_puerta.py` llama a `AP.olvidar_todo()` OCHO veces contra el modulo REAL y nunca redirige `AP.RUTA_DEL_TURNO` a un temporal, asi que BORRA EL TURNO VIVO DEL AUDITOR en su sede de verdad y sale VERDE mientras lo hace; y el caso `H` de `vuelta193_tarea4e_mutacion_sello_entre_procesos.py` exige `os.path.exists(turno_real) == False`, o sea pide que NO haya auditor. En el orden alfabetico en que la bateria los corre, EL VERDE DEL SEGUNDO NO ES SUYO: se lo debe al primero. (a) QUE EL ARNES DE LA 192 NO TOQUE LA SEDE DE VERDAD, redirigiendo `AP.RUTA_DEL_TURNO` a un temporal antes de su primer `olvidar_todo()`. (b) QUE EL ARNES DE LA 193 DEJE DE EXIGIR QUE EL FICHERO NO EXISTA: que mida existencia, bytes y `sha256` ANTES y DESPUES y caiga si CAMBIA. (c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un arnes de la nomina modifica o borra `_TURNO_DEL_AUDITOR.json` en su sede de verdad, LANZANDO PROCESOS DE VERDAD. (d) QUE EL FICHERO DEL TURNO NO SE PUEDA VOLVER A COMMITEAR. (e) NO SE CLONA NINGUNO DE LOS DOS FICHEROS: se les anade. (f) NO SE TOCA LA NOMINA. (g) AL CERRAR, LOS DOS ARNESES EN LOS TRES ESCENARIOS DEL FICHERO DEL AUDITOR, CON LAS TRES SALIDAS PUBLICADAS; si el verde de alguno sigue dependiendo del orden, SE PARA Y SE TRAE'),
    ("3", 'LA BATERIA, ENTERA Y POR TRAMOS. `AUDITOR.md` 6.1, literal: LA BATERIA CORRE POR TRAMOS OBLIGATORIOS, CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR, UNA VUELTA CORTADA RETOMA EN EL TRAMO SIGUIENTE, y LA BATERIA SE DECLARA CORRIDA CUANDO LOS TRAMOS TIENEN SALIDA SELLADA DEL MISMO CALIBRE. (a) CLONAR EL LANZADOR COMO `scripts/loop/vuelta194_bateria_por_tramos.py`, CLON DECLARADO del de la 189, cotejado con `scripts/loop/cotejar_clon_declarado.py` y con su salida pegada. (b) EL NUMERO DE TRAMOS SE COMPUTA CON `--plan`, NO SE TECLEA NI SE HEREDA, y se publica con su FECHA DE CORTE (banco `9.21`): el NUEVE de `AUDITOR.md` 6.1 es la cuenta de la nomina del 5 sep 2026 y no un objetivo. (c) CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR. (d) LA DOBLE CORRIDA NO SE AFLOJA: cada entrada se corre DOS VECES por el cotejo de reproducibilidad de la vuelta 141. (e) AL FINAL `--componer`, que es quien coteja EL CALIBRE, y UNA SALIDA SELLADA QUE MIDE CERO BYTES NO CUENTA COMO HECHA. (f) PUBLICAR EL RELOJ de la corrida. (g) SI UN TRAMO CAE EN ROJO, NI SE ESCONDE NI SE REPITE HASTA QUE SALGA VERDE: se publica con su tramo, su entrada y su motivo. Y LA TRAMPA MEDIDA POR EL AUDITOR: las NUEVE selladas que `vuelta183_bateria_por_tramos.py --siguiente` encuentra son de las vueltas 183 y 184 y NO de esta, asi que correr ese fichero declararia la bateria corrida sobre la corrida de otra vuelta'),
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
    vuelta 193 se publica CON SU FECHA DE CORTE (banco 9.21). La caida 5.5 del
    reporte de la 192 fue exactamente una cifra de este inventario publicada sin
    corte y contradiciendo a su propia seccion 0."""
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
> **ESTA ES VUELTA DE BATERIA.** `AUDITOR.md` 6.1, decision del fundador del 5 sep
> 2026: la bateria corre **CADA CINCO VUELTAS** en una vuelta propia **que no lleva
> nada mas**, y **la 189 la corrio entera**. Por esa cadencia toca aqui. **La
> seccion 9 de este reporte NO cierra con hueco declarado: cierra con la bateria
> corrida**, por tramos, con su doble corrida, su reloj y su salida sellada.
>
> **VAN TRES SUB-TAREAS Y DOS SON BLOQUEANTES.** El tope de cinco sigue vigente y
> esta ganado, y **la cifra se conto del instrumento en esta vuelta**, no se heredo:
> el bloque `E` del sello de apertura corrio
> `scripts/loop/vuelta%(ant2)d_racha_de_cierres.py` sobre el inventario ENTERO. **Y
> la TAREA 2 no es trabajo de al lado: es la PRECONDICION de la bateria**, porque
> dos entradas de la nomina estan rotas de una forma que la bateria misma va a
> pisar, y por `AUDITOR.md` 6.1 unas salidas selladas no valen si una es de otra
> hondura que las demas.
>
> **EL DESFASE DE CALIBRADO SE MIDIO EN LA APERTURA**, dentro del bloque de
> apertura y **antes de la primera operacion**. Una columna de apertura medida al
> cierre es caida que ACUMULA, y esa fue la `C.1` que el acta 194 le puso al reporte
> de la 193.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina** (la opcion `c` que el fundador RECHAZO el
> 5 sep 2026: **la nomina sigue creciendo y nadie la poda sin el fundador**), ni
> ciegas nuevas: **es vuelta de bateria y no lleva trabajo de plan al lado**. **Y
> siguen fuera, nombradas para que la 195 no las redescubra:** la relectura al doble
> del tramo de la tanda del auditor, que es SU deuda de credito y la encarga el, y
> **va a la 195 con su tramo y su doble ya cerrados hoy**; el remedio del hallazgo
> `5.3` (los mensajes de commit del bucle **no publican clases por puesto ni el
> reparto de una ciega**, y eso empieza HOY aunque su guarda de codigo se encargue
> en la 195); el desfase de `PATRONES_ACTA`, **que el acta 193 dejo DESPUES de esta
> bateria y que la 195 recoge**; `acumulan()` que lea la tabla o declare que no es
> la sede; el cotejo de clon declarado que separa sentencia de codigo de cambio de
> texto; la excepcion que publica siempre su lista; la medicion del censo de arneses
> con carril de mutacion sin fichero propio; las ocho actas sin entrada propia en la
> serie (173 a 180); el exitcode 2 propagado a `--componer`; que el campo
> `evidencia` de `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE
> MUEVE: sigue en `LISTA`**; y **QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO**, que
> el acta 194 deja NOMBRADO y medido en su `4.8` y **no resuelto, porque mover una
> clase es del RECOMPUTO**.
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
  acta 185, **y el acta 193 lo dejo expresamente DESPUES de la bateria de la 194:
  la 195 es el sitio, y el encargo de esta vuelta lo repite**. Lo que si se puede
  contar: **%(n_lit)d reportes archivados traen el literal `DESFASE DECLARADO`**
  (%(lista_lit)s), contados por `reportes_con_el_literal()` de este mismo fichero,
  **con FECHA DE CORTE %(corte)s** (banco `9.21`, TODA CIFRA DE CRUCE LLEVA SU
  FECHA DE CORTE). **Un inventario que crece cada vuelta sin corte envejece solo.**
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

## 1. LAS TRES TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
%(filas)s
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
""" % dict(v=VUELTA, ant=VUELTA - 1, ant2=VUELTA - 2, pisa=n_arbol, rama=rama,
           acta8=acta_hash[:8], asunto=repr(acta_asunto), head8=head_ap[:8],
           nac8=nac_hash[:8], celdas=celdas, n_ap=len(lado_apertura_roto),
           filas=filas, n_lit=len(con_literal), lista_lit=lista_literal,
           corte=corte, frase_tallador=frase_tallador)

    io.open(ruta, "w", encoding="utf-8", newline="\n").write(texto)
    print("ESQUELETO ESCRITO: docs/loop/REPORTE.md (%d bytes, %d lineas por count(NL))"
          % (len(texto.encode("utf-8")), texto.count(chr(10))))
    print("   rama leida de git: %s" % rama)
    print("   acta %d leida de git log: %s  %s" % (VUELTA - 1, acta_hash[:8], acta_asunto[:70]))
    print("   HEAD de apertura leido del sello: %s" % head_ap[:8])
    print("   nacimiento del bloque de apertura, --diff-filter=A: %s" % nac_hash[:8])
    print("   reporte pisado, leido de su cabecera: vuelta %d" % n_arbol)
    print("   celdas ilegibles que el tallador imprime HOY: %s" % celdas)
    print("   reportes con el literal del desfase: %d, corte %s"
          % (len(con_literal), corte))
