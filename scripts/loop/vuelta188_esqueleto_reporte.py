# -*- coding: utf-8 -*-
r"""vuelta188_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 188,
TALLADO EN LA APERTURA PARA QUE UNA VUELTA CORTADA DEJE REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta187_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS, este docstring y el bloque de prosa del encabezado.
El cotejo del clon lo hace scripts/loop/cotejar_clon_declarado.py y su salida se
pega en el reporte con lo que salga: AQUI NO SE AFIRMA QUE NINGUN DIFF SALGA
VACIO.

Y AQUI SE EJECUTA EL REMEDIO DE LA `C.1` DE LA VUELTA 187 (acta 188, seccion 8;
encargo de la 188, TAREA 5.c). La 187 tallo su esqueleto DESPUES de la TAREA 1 y
lo declaro, con una causa que el acta corrige: es cierto que el esqueleto
necesita que SALIDA_V<N>_HEAD_APERTURA.txt este COMMITEADO para leer su commit de
nacimiento con git log --diff-filter=A, y NO es cierto que eso obligue a esperar
a la TAREA 1. La vuelta 186 lo hizo en TRES commits (793ad9a1 apertura ->
88bd3216 esqueleto en su propio commit -> 456f0847 tarea 1). ESTA VUELTA HACE LO
MISMO: apertura y su commit, esqueleto y SU PROPIO COMMIT, y despues las tareas.
El remedio cuesta un commit y estaba en uso hace dos vueltas.

ESTA VUELTA NO ES DE BATERIA (AUDITOR.md 6.1: corre cada cinco vueltas y cerro
entera en la 184, asi que la siguiente es la 189), y su seccion 9 cierra CON EL
HUECO DECLARADO Y MEDIDO: nombre del fichero, bytes medidos y atribucion, las
tres juntas o no vale. Y ESTA VUELTA NO ESCRIBE DOS SECCIONES 9, que es la `C.4`
del acta 188: la unica seccion 9 es la que talla cerrar_reporte.py.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 188 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V188_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada:
no inventa un hash.

Y SE DECLARA EL DESFASE QUE NO SE REPARA, POR CUARTA VUELTA: PATRONES_ACTA
sigue pidiendo el acta de VUELTA - 1, o sea la 187, cuando el acta que ORDENA
esta vuelta es la 188. Es el `D.2` del reporte de la 184, adjudicado a favor por
la `5.2` del acta 185 CON REPARACION ENCARGADA, y esta vuelta NO la ejecuta
porque su encargo trae cinco tareas y ninguna es esa.

USO:
  python scripts/loop/vuelta188_esqueleto_reporte.py
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
VUELTA = 188
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
    ("1", 'LOS REGISTROS. BLOQUEANTE. El acta 188 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus SEIS adjudicaciones `5.1` a `5.6` todas a favor, los TRES numerales de la seccion 6 (`PD.1` ABIERTA con sus cinco puestos leidos del acta, `PD.8` ABIERTA, y el `6.3` como ANOTACION), las TRES preguntas de la seccion 7 las tres CONTESTADAS, CERO caidas propias del auditor registradas COMO CERO Y NO OMITIDAS, y CUATRO caidas del ejecutor todas DE METODO y NINGUNA DE RACHA: `C.1` y `C.2` declaradas por el ejecutor y `C.3` y `C.4` levantadas por el auditor, LAS CUATRO ATRIBUIDAS AL EJECUTOR porque la atribucion la hace la cabecera de la seccion y no quien las encontro. Mas la deuda de la serie REMEDIDA en esta vuelta. Con caso positivo por mutacion sobre un acta FABRICADA y el esperado mutado cayendo, y con la PARADA conservada entera: un estado que el registrador no sepa leer sigue siendo PARADA'),
    ("2", 'EL PLAN: LAS CUATRO FICHAS QUE LA VARA NOMBRA, RESUELTAS CONTRA SU EVIDENCIA. `scripts/loop/vuelta150_3_relectura_expediente.py --corte <HEAD de apertura>` corrida con corte propio y no copiada del acta; las cuatro fichas `OP-L-01`, `OP-L-02`, `OP-L-03` y `OP-I-01` LEIDAS ENTERAS Y CITADAS de `docs/plan/OPERACIONES.jsonl`; el producto de cada una MEDIDO contra la `evidencia` que la propia ficha nombra, con bytes por las dos convenciones y la cuenta prometida contra la cuenta que hay; LA VARA GANA SU PATA DOCUMENTAL EN CODIGO para las fichas de tipo `MESA`, con la cifra vieja publicada entera y al lado; el estado de cada una declarado en una de las tres formas (su producto la cubre, esta pero no la cubre, o no hay evidencia y es PARADA); y el desfase de sus cortes medido y publicado. NO se toca el campo `estado`, NO se reescriben las fichas y NINGUN VEREDICTO SE MUEVE'),
    ("3", 'EL CASO E: EL INVENTARIO DE EXENCIONES EN VEZ DE UNA CUENTA TECLEADA. BLOQUEANTE PORQUE LA BATERIA ES LA 189. El caso E de `scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py` deja de contar un texto y pasa a COMPUTAR EL INVENTARIO de guardas eximidas en el carril tardio CON SUS NOMBRES, leido del fuente, y a cotejarlo contra una LISTA AUTORIZADA Y ESCRITA que hoy tiene DOS entradas con su vuelta y su decision al lado. Cae en rojo en TRES casos y los tres se prueban: una exencion fuera de la lista, una de la lista que desaparece, y una eximida que NO exige su declaracion. Los otros diecisiete casos no se tocan. Mas (b) el `sha256` del sujeto al lado de todo numero de linea que un arnes publique, y (c) la doble corrida de la nomina EXCLUYENDO explicitamente cualquier arnes que ya haya salido en rojo en esa misma vuelta, DICIENDOLO en su salida'),
    ("4", 'LA ESCALADA: LA GUARDA QUE VE LA MITAD, Y LA SECCION QUE SE DUPLICA. `AUDITOR.md` 1.2, mandatorio con la racha de reporte en dos. (a) `parejas_publicadas()` ensancha sus formas para cubrir las TRES que hoy se le escapan, leidas de reportes reales; LA REGLA DE LA AMBIGUEDAD NO SE TOCA; y la guarda PUBLICA SU COBERTURA, cuantas parejas ve contra cuantas rutas con cifra de bytes hay y cuantas quedan sin atribuir POR AMBIGUAS nombradas una a una. (b) `piezas_que_faltan()` exige que las secciones sean UNICAS Y ESTEN EN ORDEN, no solo que existan, que es la `C.4`. Con arnes obligatorio que incluye un caso por cada forma nueva con su mutacion cayendo, un caso de ambiguedad que exija NO atribuir, un caso sobre el texto real de `git show 9a06b7c8` exigiendo SEIS parejas vistas y SEIS que calzan, y un caso sobre ese mismo texto que ACUSE las dos secciones 9 nombrando sus dos lineas'),
    ("5", 'LA RELECTURA AL DOBLE, LOS DOS REMEDIOS PEQUENOS Y EL CIERRE. (a) La relectura al doble del tramo de la ciega del acta 188, encargada por `AUDITOR.md` 1.2 porque la discrepancia del auditor (el puesto 1202) cayo FUERA del discutible de clase marcado: cotejo de `sha256` contra el sello `V189` ANTES de leer un solo puesto, 30 puestos mas 30 vecinos deterministas con `vecinos()` IMPORTADA y no copiada, 60 releidos que es el doble exacto, NINGUNA CLASE SE VUELVE A DECIDIR; mas el remedio del `D.2`, que es un conjunto `evitar` OPCIONAL para `vecinos()` que deja su conducta de hoy intacta sin el, y los TRES solapes del UNIVERSO publicados; mas el puesto 1202 mirado con la misma vara; mas la cuenta de cuantos de los 60 llevan en su razon evidencia DE FAMILIA y no del par. (b) `docs/loop/DISCUTIBLES_DE_CLASE_V188.txt` con los puestos de los discutibles DE CLASE y nada mas. (c) El esqueleto tallado en la apertura y en su propio commit, que es la `C.1`. (d) El reporte se abre, se llena por anexion y se cierra con `cerrar_reporte.py --vuelta 188` y `archivar_reporte.py --vuelta 188`, con UNA SOLA SECCION 9'),
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
> siguiente vuelta de bateria es la 189, o sea la que viene**. En las vueltas
> intermedias la seccion 9 se cierra igual, con el **nombre del fichero, sus
> bytes medidos y su atribucion**, las tres juntas o no vale.
>
> **Y ESTA VUELTA ESCRIBE UNA SOLA SECCION 9**, que es la `C.4` del acta 188: el
> reporte de la 187 llevaba **dos**, en las lineas 870 y 920, con la `## 10.` en
> medio. Lo que esta vuelta tenga que decir de la bateria va **en la que talla
> `scripts/loop/cerrar_reporte.py`**, no en una segunda escrita a mano.
>
> **EL TOPE SIGUE EN CINCO, Y ESTA MEDIDO EN VEZ DE DARSE POR BUENO.** El regimen
> temporal `AUDITOR.md` 6.2 quedo cumplido y apagado en la 187. El **bloque H.0**
> del sello de apertura de esta vuelta midio **las tres** salidas de cierre,
> `docs/loop/SALIDA_V185_CERRAR_REPORTE.txt`,
> `docs/loop/SALIDA_V186_CERRAR_REPORTE.txt` y
> `docs/loop/SALIDA_V187_CERRAR_REPORTE.txt`, y **las tres dicen `CIFRA piezas que
> faltan: 0`**. Esta vuelta lleva **CINCO tareas**.
>
> **DONDE SE TALLO ESTE ESQUELETO, Y ESTA VEZ LA RESPUESTA ES EN LA APERTURA.**
> Es el remedio de la `C.1` de la 187, escrito en la TAREA 5.c del encargo: la
> vuelta 187 lo tallo **despues de la TAREA 1**, y el acta 188 le corrigio la
> causa midiendola contra la vuelta 186, que hizo lo mismo **en tres commits**
> (`793ad9a1` apertura, `88bd3216` **esqueleto en su propio commit**, `456f0847`
> tarea 1). **Aqui va igual: apertura y su commit, esqueleto y SU PROPIO COMMIT,
> y despues las tareas.** Desde el segundo commit de esta vuelta ya hay reporte
> parcial en el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** **no se abren
> las mesas anotadas** (la del `PMF` con los puestos 338, 297 y ahora 670, la del
> **603** y la de figuras del **226**), que el `6.3` del acta 188 deja como
> ANOTACION y no encarga; **no se poda la nomina de la bateria**, que es la opcion
> `c` que el fundador RECHAZO el 5 sep; **no se anade ningun campo a
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**, que es la `PD.8` y es del fundador;
> **no se toca el campo `estado` de `docs/plan/OPERACIONES.jsonl`**, declarado
> HISTORICO el 4 sep 2026; **no se reabre `docs/loop/reportes/REPORTE_V184.md`**;
> y **no se mueve ningun veredicto**: el `sha256` LF del archivo abre y tiene que
> cerrar en el mismo valor. Y **no se toca `dataset/`**: el `numstat` se mide al
> entrar y al salir y las dos cifras se publican.
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
