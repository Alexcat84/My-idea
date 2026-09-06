# -*- coding: utf-8 -*-
r"""vuelta186_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 186,
TALLADO AL EMPEZAR PARA QUE UNA VUELTA CORTADA DEJE REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta185_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS y el bloque de prosa del encabezado. El cotejo del
clon lo hace scripts/loop/cotejar_clon_declarado.py y su salida se pega en el
reporte con lo que salga.

POR QUE SE TALLA AQUI Y NO DESPUES DE LA TAREA 2, AL REVES QUE EN LA 185. En la
185 el esqueleto tuvo que esperar porque su PASO 0 habria archivado el reporte de
la 184 SIN CERRAR. Aqui no hay nada de eso: el reporte que hay en el arbol es el
de la 185, YA CERRADO Y YA ARCHIVADO, y el de la 184 tambien esta archivado desde
la TAREA 2.a de la 185. Asi que el esqueleto vuelve a su sitio de siempre, LA
APERTURA, que es lo que EJECUTOR.md 1 manda cuando dice que el reporte se abre al
empezar y crece por anexion.

Y EL PASO 0 SE CORRE IGUAL, SALGA LO QUE SALGA, Y SU SALIDA SE PEGA. El encargo
de la 186 lo dice con esas palabras: si no hay reporte ajeno que archivar, se
dice, en vez de dejar la fila muda.

ESTA VUELTA NO ES DE BATERIA (AUDITOR.md 6.1: corre cada cinco vueltas y la
siguiente es la 189), asi que la seccion 9 de este reporte cierra CON EL HUECO
DECLARADO Y MEDIDO: nombre del fichero, bytes medidos y atribucion, las tres
juntas o no vale.

EL TOPE SIGUE EN DOS SUB-TAREAS (AUDITOR.md 6.2), PERO LA CUENTA YA NO ESTA EN
CERO: la 185 cerro su propio reporte y es la PRIMERA de las dos seguidas. Si esta
vuelta cierra el suyo, la 187 recupera el tope de CINCO.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 186 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V186_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada:
no inventa un hash.

Y SE DECLARA EL DESFASE QUE NO SE REPARA: PATRONES_ACTA sigue pidiendo el acta de
VUELTA - 1, o sea la 185, cuando el acta que ORDENA esta vuelta es la 186. Es el
`D.2` del reporte de la 184, adjudicado a favor por la `5.2` del acta 185 CON
REPARACION ENCARGADA, y esta vuelta NO la ejecuta porque su encargo trae dos
sub-tareas y ninguna es esa.

USO:
  python scripts/loop/vuelta186_esqueleto_reporte.py
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
VUELTA = 186
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
    ("1", 'LOS REGISTROS Y LAS DOS CUENTAS QUE VENCEN. BLOQUEANTE. (a) El acta 186 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus SIETE adjudicaciones `5.1` a `5.7` todas a favor, los CUATRO pendientes de doctrina de la seccion 6 (`PD.5` y `PD.6` CERRADAS por cita, `PD.1` ABIERTA con sus cinco puestos leidos del acta, y el `6.4` como ANOTACION y no como pendiente propio), las TRES preguntas de la seccion 7 las tres CONTESTADAS, CERO caidas propias del auditor registradas COMO CERO Y NO OMITIDAS, UNA caida de reporte del ejecutor (`R.1`, la del `git status` en cero lineas) que NO acumula por vivir en prosa, y la deuda de la serie REMEDIDA en esta vuelta y no heredada del `R.47`, mas su caso positivo por mutacion sobre un acta FABRICADA con el esperado mutado cayendo. (b) LOS DOS ARNESES DE LA 185 ENTRAN EN LA NOMINA, que es la respuesta a la `P.3`: `arneses_que_faltan()` tiene que devolver 0 despues, con el tamano de la nomina antes y despues, y los dos arneses corridos DOS VECES CADA UNO EN PROCESOS APARTE exigiendo el mismo `sha256`. NO SE PODA NADA. (c) LA RELECTURA AL DOBLE del tramo de la ciega del acta 186, con el cotejo de `sha256` contra el sello `V187` ANTES de leer un solo puesto, 30 puestos mas 30 vecinos deterministas con `vecinos()` IMPORTADA, solape 0 por los dos lados MEDIDO, las cuatro discrepancias del auditor miradas con la misma vara, y la cuenta de clases `B` del universo releido'),
    ("2", 'LAS TRES REPARACIONES DE `cerrar_reporte.py`, LA ESCALADA Y EL CIERRE DE DOS REPORTES. (a) La pieza (4) deja de llevar su propia copia de `ajena != vuelta` y LLAMA a la unica sede, con parametro nuevo cuyo valor por defecto conserva EXACTAMENTE la conducta de hoy y computado en `main()` sin bandera, con arnes propio. (b) La pieza (2) busca el hueco de cabecera FUERA de los bloques cercados REUSANDO el desbloqueador que `cifras_sin_pareja()` ya tenia, separado a una sede y llamado por las dos, con arnes propio. (c) El carril de CIERRE TARDIO, computado y no pasado por bandera, donde las cifras sin pareja NO bloquean pero SE DECLARAN una a una dentro del propio reporte cerrado, con arnes propio; y DESPUES, y no antes, el reporte de la 184 se cierra y se archiva tras cotejar sus tres piezas por `sha256` y por bytes. (d) LA ESCALADA de `AUDITOR.md` 1.2: una guarda que extrae de `SALIDA_V<N>_APERTURA.txt` las dos cifras del estado del arbol y las coteja contra lo que la seccion 4 del reporte afirma, cayendo en ROJO si discrepan o si el reporte no las afirma, con arnes propio que exige que HUBIERA CAZADO LA `R.1`. (e) El reporte de la 186 se abre en su esqueleto, cada tarea anexa su fila al cerrarse, la cabecera se talla y `--comparar` tiene que dar CABECERA IDENTICA AL TALLADOR, y su SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO'),
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
> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que no lleva nada
> mas. **Cerro entera en la 184**, con sus nueve tramos sellados, asi que **la
> siguiente vuelta de bateria es la 189**. En las vueltas intermedias la seccion 9
> se cierra igual, con el **nombre del fichero, sus bytes medidos y su
> atribucion**, las tres juntas o no vale.
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, PERO LA CUENTA YA NO ESTA EN CERO.**
> El regimen `AUDITOR.md` 6.2 devuelve el tope a cinco cuando **dos vueltas
> seguidas cierren su propio reporte** con `scripts/loop/cerrar_reporte.py`. **La
> 185 cerro el suyo** y es la **PRIMERA de las dos**. **Si esta vuelta cierra el
> suyo, es la SEGUNDA y la 187 recupera el tope de CINCO.** Van dos tareas y no hay
> una tercera.
>
> **EL TRABAJO DE ESTA VUELTA ES APLICAR LAS DOS ADJUDICACIONES DEL ACTA 186 QUE
> DEJAN UN INSTRUMENTO DICIENDO DOS COSAS DEL MISMO CASO**, meter en la nomina los
> dos arneses que si no dejarian la bateria de la 189 abriendo en rojo, y cerrar el
> reporte de la 184, que lleva dos vueltas sin conseguirse.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee el
> par **2.464** ni ningun otro de la cola post fusion (**encabeza el encargo de la
> 187**, y el acta 186 explica en su seccion 12 que el tope de dos sub-tareas es
> aritmetica y no preferencia); **no se vuelve a decidir ninguna clase** en la
> relectura al doble; no se toca el marcador, ni un veredicto, ni `dataset/`; **no
> se poda la nomina de la bateria**, que es la opcion `c` que el fundador RECHAZO
> el 5 sep, y aqui se hace lo contrario, que es completarla; y **no se abre la mesa
> de los tres nodos de la puerta del `PMF`** que el acta 186 anota en su `6.4`, que
> es trabajo de plan y no de esta vuelta.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py` y desde la 178 vuelve a correr en su sitio. **Una
> columna de apertura medida al cierre es caida que ACUMULA.**
>
> **Y EL ESQUELETO VUELVE A SU SITIO DE SIEMPRE, LA APERTURA, AL REVES QUE EN LA
> 185.** Alli tuvo que esperar porque su PASO 0 habria archivado el reporte de la
> 184 sin cerrar. Aqui no hay nada de eso: el reporte del arbol es el de la 185, ya
> cerrado y ya archivado, y el de la 184 tambien esta archivado desde la TAREA 2.a
> de la 185. **El PASO 0 se corre igual y su salida se pega con lo que salga**,
> diga lo que diga, en vez de dejar la fila muda.

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
