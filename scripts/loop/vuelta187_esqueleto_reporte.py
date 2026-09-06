# -*- coding: utf-8 -*-
r"""vuelta187_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 187,
TALLADO AL EMPEZAR PARA QUE UNA VUELTA CORTADA DEJE REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta186_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS (que aqui son CINCO y no dos) y el bloque de prosa del
encabezado. El cotejo del clon lo hace scripts/loop/cotejar_clon_declarado.py y
su salida se pega en el reporte con lo que salga.

EL TOPE VUELVE A CINCO, Y NO SE DA POR BUENO PORQUE EL ENCARGO LO DIGA. El
regimen temporal de AUDITOR.md 6.2 devolvia el tope a cinco cuando DOS vueltas
seguidas cerraran su propio reporte con cerrar_reporte.py. El bloque H.0 del
sello de apertura de esta vuelta midio las dos salidas de cierre y las dos dan
CIFRA piezas que faltan: 0. El regimen se apaga por su propio disparador de
salida y esta vuelta lleva CINCO filas.

DONDE SE TALLA ESTE ESQUELETO, DICHO CON HONESTIDAD Y NO REDONDEADO: no en la
apertura, sino DESPUES DE LA TAREA 1. La apertura si corrio primero y entera
(SALIDA_V187_APERTURA.txt), pero el esqueleto necesita que
SALIDA_V187_HEAD_APERTURA.txt este COMMITEADO para poder leer su commit de
nacimiento con git log --diff-filter=A, y ese commit es el de la TAREA 1. La
desviacion se declara aqui y en el propio reporte en vez de disimularse: lo que
EJECUTOR.md 1 protege es que una vuelta cortada deje reporte parcial y no vacio,
y desde este punto eso se cumple.

ESTA VUELTA NO ES DE BATERIA (AUDITOR.md 6.1: corre cada cinco vueltas y cerro
entera en la 184, asi que la siguiente es la 189), y su seccion 9 cierra CON EL
HUECO DECLARADO Y MEDIDO: nombre del fichero, bytes medidos y atribucion, las
tres juntas o no vale.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 187 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V187_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada:
no inventa un hash.

Y SE DECLARA EL DESFASE QUE NO SE REPARA, POR TERCERA VUELTA: PATRONES_ACTA
sigue pidiendo el acta de VUELTA - 1, o sea la 186, cuando el acta que ORDENA
esta vuelta es la 187. Es el `D.2` del reporte de la 184, adjudicado a favor por
la `5.2` del acta 185 CON REPARACION ENCARGADA, y esta vuelta NO la ejecuta
porque su encargo trae cinco tareas y ninguna es esa.

USO:
  python scripts/loop/vuelta187_esqueleto_reporte.py
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
VUELTA = 187
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
    ("1", 'LOS REGISTROS. BLOQUEANTE. El acta 187 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus SEIS adjudicaciones `5.1` a `5.6` todas a favor, los DOS numerales de la seccion 6 (`PD.1` ABIERTA con sus cinco puestos leidos del acta, y el `6.2` como CORRECCION POR DECLARACION, que es un ESTADO NUEVO: la `PD.7` del reporte de la 186 NO es un pendiente de doctrina y el numero `PD.7` queda libre), las TRES preguntas de la seccion 7 las tres CONTESTADAS, CERO caidas propias del auditor registradas COMO CERO Y NO OMITIDAS, UNA caida del ejecutor de reporte (`C.1`, la de las cuatro cifras de LF supuestas) que NO acumula y cuya ESPECIE el acta 187 corrige, y la deuda de la serie REMEDIDA en esta vuelta. Con caso positivo por mutacion sobre un acta FABRICADA, el esperado mutado cayendo, y el registrador aprendiendo el estado nuevo y haciendo PARADA ante uno que no sepa leer'),
    ("2", 'EL PLAN SE MUEVE: EL PAR 2.464 Y EL TRAMO 1 DE LA COLA POST FUSION. Se LEE el disparador escrito antes de tocar nada y se cita por numero; el par 2.464 encabeza y detras va el tramo 1 tal como el disparador lo defina, con el tamano del tramo COMPUTADO del criterio escrito y no inventado; cada par que se mueva lleva su CORRECCION DECLARADA y su RECOMPUTO por la letra de `AUDITOR.md` 1.3; el `sha256` del archivo se publica AL ABRIR y AL CERRAR, y si esta tarea mueve algo el de cierre tiene que ser distinto y la diferencia se explica par por par; y el marcador se RECOMPUTA del archivo con su comando. NO se abre la mesa del `PMF`, ni la del 603, ni la de figuras del 226'),
    ("3", 'LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 187, encargada por `AUDITOR.md` 1.2 porque las CUATRO discrepancias del auditor cayeron FUERA del discutible de clase marcado. Cotejo de `sha256` contra el sello `V188` ANTES de leer un solo puesto; 30 puestos mas 30 vecinos deterministas con `vecinos()` IMPORTADA; solape 0 contra el tramo, contra la ciega anterior y contra los 293 puestos de la exclusion, MEDIDO y no supuesto; 60 puestos releidos que es el doble exacto; NINGUNA CLASE SE VUELVE A DECIDIR. Mas los cuatro puestos 226, 603, 1612 y 2448 mirados con la misma vara, y el censo de las `B` del universo releido con sus tres comprobaciones mecanicas una a una'),
    ("4", 'LA ESCALADA: LA PAREJA DE CONVENCIONES DEJA DE BASTAR CON EXISTIR. `AUDITOR.md` 1.2, mandatorio a partir de dos. Una guarda que, para cada ruta que el reporte publique con cifra de bytes, RECOMPUTA LAS DOS CONVENCIONES DESDE EL DISCO y las coteja contra las dos publicadas, cayendo en ROJO si alguna discrepa y nombrando la ruta, la cifra publicada, la medida y cual de las dos convenciones falla. REUSA lo que `scripts/loop/vuelta186_rutas_del_reporte.py` ya sabe hacer: una sede, dos llamadores y NO un tercero. Funciones PURAS y un solo lector de disco, cableada donde `cerrar_reporte.py` juzga y SIN bandera. Con arnes obligatorio que incluye UN CASO SOBRE EL TEXTO REAL DE `git show bb3aaad3` exigiendo que HABRIA CAZADO LAS CUATRO CIFRAS DE LA `C.1`'),
    ("5", 'LA NOMINA, LA DECLARACION DEL 184 Y EL CIERRE. (a) Los CUATRO arneses de la 186 entran en la nomina MAS los que nazcan hoy, con `arneses_que_faltan()` devolviendo 0 al cerrar, el tamano de la nomina antes y despues, y cada arnes nuevo corrido DOS VECES en procesos aparte exigiendo el mismo `sha256`. NO SE PODA NADA. (b) La declaracion del defecto del reporte de la 184, que es la `P.2`: en el carril de CIERRE TARDIO la guarda de la `2.d` NO bloquea pero SE DECLARA con su motivo entero, en el carril NORMAL sigue bloqueando entera, `REPORTE_V184.md` NO se reabre, y con arnes propio. (c) La cifra inutil del bloque H.5, reparada con la cifra antes y despues. (d) El reporte de la 187 se abre, se llena por anexion y se cierra con `cerrar_reporte.py --vuelta 187` y `archivar_reporte.py --vuelta 187`, con la cabecera tallada y `--comparar` dando CABECERA IDENTICA AL TALLADOR, y su SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO'),
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
> **EL TOPE VUELVE A CINCO, Y ESTA MEDIDO EN VEZ DE DARSE POR BUENO.** El
> regimen temporal `AUDITOR.md` 6.2 devolvia el tope a cinco cuando **dos vueltas
> seguidas cerraran su propio reporte** con `scripts/loop/cerrar_reporte.py`. El
> **bloque H.0** del sello de apertura de esta vuelta midio las dos salidas de
> cierre, `docs/loop/SALIDA_V185_CERRAR_REPORTE.txt` y
> `docs/loop/SALIDA_V186_CERRAR_REPORTE.txt`, y **las dos dicen `CIFRA piezas que
> faltan: 0`**. **El regimen se apaga por su propio disparador de salida**, y esta
> vuelta lleva **CINCO tareas**.
>
> **Y CON EL TOPE EN CINCO SE ACABA LA ARITMETICA QUE APLAZABA EL PLAN.** El plan
> lleva **seis vueltas sin moverse**, y **por eso el par 2.464 y el tramo 1 de la
> cola post fusion van en la TAREA 2, delante de toda la maquinaria salvo los
> registros**. **Si esta vuelta se corta por falta de sitio, que se caiga la
> maquinaria, no el plan.**
>
> **DONDE SE TALLO ESTE ESQUELETO, DICHO SIN REDONDEAR.** No en la apertura, sino
> **despues de la TAREA 1**. La apertura si corrio primero y entera
> (`docs/loop/SALIDA_V187_APERTURA.txt`, con el ciclo de Gate 0 dentro), pero este
> esqueleto necesita que `docs/loop/SALIDA_V187_HEAD_APERTURA.txt` este
> **commiteado** para poder leer su commit de nacimiento con
> `git log --diff-filter=A`, y ese commit es el de la TAREA 1. **Se declara en vez
> de disimularse**, que es lo que el banco 9 manda: lo que `EJECUTOR.md` 1 protege
> es que una vuelta cortada deje reporte parcial y no vacio, y desde este punto
> eso se cumple.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** **no se abre la
> mesa de los tres nodos de la puerta del `PMF`** (puestos 338 y 297), ni la del
> **603**, ni la de **figuras del 226**; las tres estan anotadas en el acta 187,
> seccion 6.2, con sede en `docs/PENDIENTES.md`, y son trabajo de plan de otra
> vuelta. **No se poda la nomina de la bateria**, que es la opcion `c` que el
> fundador RECHAZO el 5 sep, y aqui se hace lo contrario, que es completarla. **No
> se reabre ni se reescribe `docs/loop/reportes/REPORTE_V184.md`**, que ya esta
> cerrado y archivado: lo que se le anade es la DECLARACION de su defecto. Y **no
> se toca `dataset/`**: el `numstat` se mide al entrar y al salir y las dos cifras
> se publican.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py` y desde la 178 vuelve a correr en su sitio. **Una
> columna de apertura medida al cierre es caida que ACUMULA.**

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
