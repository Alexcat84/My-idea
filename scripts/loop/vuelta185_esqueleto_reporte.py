# -*- coding: utf-8 -*-
r"""vuelta185_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 185,
TALLADO AL EMPEZAR PARA QUE UNA VUELTA CORTADA DEJE REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta184_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS y el bloque de prosa del encabezado. El cotejo del
clon lo hace scripts/loop/cotejar_clon_declarado.py y su salida se pega en el
reporte con lo que salga.

POR QUE SE TALLA EN EL PASO 4 DEL ORDEN DE ESTA VUELTA Y NO AL PRINCIPIO. Si este
esqueleto corriera antes, su PASO 0 archivaria el reporte de la 184 SIN CERRAR, y
la reparacion de la TAREA 1.c llegaria tarde para el unico reporte al que le
sirve. El reporte de la 184 se cierra ANTES, en la TAREA 2.a. En ningun momento
del orden el repo se queda sin reporte en disco.

Y EL PASO 0 SE CORRE IGUAL, SALGA LO QUE SALGA. Si la TAREA 2.a dejo el reporte
de la 184 archivado, este PASO 0 no tendra nada ajeno que archivar, Y ESO SE DICE
EN SU SALIDA en vez de dejar la fila muda.

ESTA VUELTA NO ES DE BATERIA (AUDITOR.md 6.1: corre cada cinco vueltas y la
siguiente es la 189), asi que la seccion 9 de este reporte cierra CON EL HUECO
DECLARADO Y MEDIDO: nombre del fichero, bytes medidos y atribucion, las tres
juntas o no vale.

EL TOPE SIGUE EN DOS SUB-TAREAS (AUDITOR.md 6.2): la 184 no cerro su propio
reporte y la cuenta de vueltas que cierran su reporte sigue en cero.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 185 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V185_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada:
no inventa un hash.

Y SE DECLARA EL DESFASE QUE NO SE REPARA: PATRONES_ACTA sigue pidiendo el acta de
VUELTA - 1, o sea la 184, cuando el acta que ORDENA esta vuelta es la 185. Es el
`D.2` del reporte de la 184, adjudicado a favor por la `5.2` del acta 185 CON
REPARACION ENCARGADA, y esta vuelta NO la ejecuta porque su encargo trae dos
sub-tareas y ninguna es esa.

USO:
  python scripts/loop/vuelta185_esqueleto_reporte.py
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
VUELTA = 185
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
    ("1", 'LOS REGISTROS Y LAS TRES REPARACIONES DE CODIGO. BLOQUEANTE. (a) El acta 185 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus siete adjudicaciones `5.1` a `5.7` todas a favor, los CUATRO pendientes de doctrina de la seccion 6 con su estado leido del titulo (`PD.2`, `PD.3` y `PD.4` CERRADAS por cita y `PD.1` ABIERTA con sus cinco puestos leidos del acta y no copiados del encargo), la caida propia del auditor `A.1` y la caida de reporte del ejecutor `R.1`, mas su caso positivo por mutacion sobre un acta FABRICADA con el esperado mutado cayendo, y la deuda de la serie REMEDIDA y no heredada del `R.46`. (b) LA SALIDA SELLADA DEL ARNES QUE PARO LA BATERIA DEJA DE CAMBIAR SOLA: funcion PURA `sin_temporal(linea, tmp)` aplicada ANTES del recorte, sin tocar lo que el arnes prueba, con arnes propio de DOS MITADES que fallan por separado. (c) LA GUARDA DE LA BATERIA CONTINUADA, que es la adjudicacion `6.2` del acta 185: `vuelta_que_sello()` y `tramos_por_vuelta()` nuevas, `rama_de_la_seccion9()` con un cuarto parametro que por defecto se comporta EXACTAMENTE como hoy, y una rama nueva que EXIGE MAS que la vieja con CUATRO condiciones a la vez, con la evidencia computada de git y sin ninguna bandera. (d) LA ESCALADA DE `AUDITOR.md` 1.2: la columna `quien lo sello` se computa en vez de teclearse, y el cotejo de las NUEVE celdas contra las que el reporte de la 184 ya lleva es la prueba. (e) LA RELECTURA AL DOBLE del tramo de la ciega del acta 185, con el cotejo de `sha256` contra el sello `V185b` ANTES de leer un solo puesto'),
    ("2", 'EL CIERRE DE DOS REPORTES: EL DE LA 184 Y EL DE LA 185. (a) El reporte de la 184 se cierra con la guarda ya reparada por la 1.c, DESPUES de cotejar sus tres piezas por `sha256` y por bytes contra lo que la 184 midio, con el veredicto de una linea TALLADO y no tecleado, y se archiva. (b) El reporte de la 185 se abre en su esqueleto, cada tarea anexa su fila al cerrarse, la cabecera se talla y `--comparar` tiene que dar CABECERA IDENTICA AL TALLADOR, y su SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO por el carril de `cerrar_reporte.py`: nombre del fichero, bytes medidos y atribucion, las tres juntas o no vale'),
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
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y LA CUENTA SIGUE EN CERO.** El
> regimen `AUDITOR.md` 6.2 devuelve el tope a cinco cuando **dos vueltas seguidas
> cierren su propio reporte** con `scripts/loop/cerrar_reporte.py`. **La 184 no
> cerro el suyo** (`cerrar_reporte.py` exitcode 1, salida pegada entera en su
> reporte), asi que la cuenta **sigue en cero**. **Van dos tareas y no hay una
> tercera.**
>
> **EL TRABAJO DE ESTA VUELTA ES DESATASCAR EL CIERRE DEL REPORTE**, que lleva
> CUATRO vueltas sin conseguirse (181, 182, 183 y 184), y que es el mismo atasco
> por el que el fundador puso el regimen 6.2 el 5 sep.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee el
> par **2.464** ni ningun otro de la cola post fusion (encabeza el encargo de la
> **186**); no se cablea el instrumento de vigencia de las `A` rancias por `P.5`;
> **no se vuelve a decidir ninguna clase** en la relectura al doble; no se toca el
> marcador, ni un veredicto, ni `dataset/`; **no se poda la nomina de la bateria**,
> que es la opcion `c` que el fundador RECHAZO el 5 sep; y **no se repara el
> desfase del acta `VUELTA - 1`** de la `5.2`, que queda encargado y sin ejecutar
> porque el tope son dos sub-tareas.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py` y desde la 178 vuelve a correr en su sitio. **Una
> columna de apertura medida al cierre es caida que ACUMULA.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO YA NO TIENE REPORTE AJENO QUE ARCHIVAR, PORQUE
> LA TAREA 2.a LO ARCHIVO ANTES.** El orden de esta vuelta no es el de siempre y
> el motivo se dice: si el esqueleto corriera primero, su PASO 0 archivaria el
> reporte de la 184 **sin cerrar**, y la reparacion de la TAREA 1.c llegaria tarde
> para el unico reporte al que le sirve. **El PASO 0 se corre igual y su salida se
> pega con lo que salga**, diga lo que diga, en vez de dejar la fila muda.

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
