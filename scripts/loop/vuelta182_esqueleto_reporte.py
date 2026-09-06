r"""vuelta182_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA
VUELTA 182, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS CINCO TAREAS ENCARGADAS.

CLON DECLARADO de scripts/loop/vuelta181_esqueleto_reporte.py. Lo que se toca a
mano son las CINCO filas de tarea, que son las de ESTE encargo, y los parrafos de
prosa que hablan del estado del bucle. La maquina no se toca en ninguna linea
salvo el numero de vuelta.

Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA: el cotejo lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte, que es
obligatorio desde la vuelta 178 por el docstring de aquel fichero. Este texto NO
publica ningun resultado de diff.

POR QUE ESTA VUELTA TRAE CINCO FILAS Y NO DOS. La adjudicacion 6.8 del acta 180
bajo el tope a DOS en la 181 porque era vuelta de bateria y AUDITOR.md 6.1 manda
que la vuelta de bateria no lleve nada mas; y esa misma adjudicacion escribio,
con estas palabras, "El tope vuelve a cinco en la 182". El encargo de esta vuelta
trae CINCO y dice "que es el tope. Ni una mas".

Y ESTA VUELTA NO ES DE BATERIA. La 181 era la suya y se corto antes de lanzarla.
La decision del fundador del 5 sep 2026 (PREGUNTA 4 de
docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md) manda que la bateria
corra POR TRAMOS RESUMIBLES, y la TAREA 5 de este encargo la deja preparada y
declarada para la 183. La seccion 9 del reporte cierra con su HUECO DECLARADO Y
MEDIDO, que es lo que AUDITOR.md 6.1 manda para las vueltas intermedias.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0, antes que nada.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 182 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta de la vuelta anterior por las
DOS formas del titulo y en las DOS pasadas de TALLADOR.buscar_acta; HEAD de
apertura leido de docs/loop/SALIDA_V182_HEAD_APERTURA.txt, sellado antes de la
primera operacion; commit de nacimiento del bloque de apertura por
git log --diff-filter=A. Si alguno no se puede leer o es ambiguo, el esqueleto
CAE EN ROJO y no escribe nada: no inventa un hash.

USO:
  python scripts/loop/vuelta182_esqueleto_reporte.py
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
VUELTA = 182
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
    ("1", 'LOS REGISTROS Y LA DEUDA DE LECTURA. (a) El acta 181 y sus adjudicaciones entran en la serie de registros, con el numero que devuelve `scripts/loop/serie_de_registros.py` y no tecleado. (b) LOS DOS PENDIENTES DEL ACTA 180, que llevan una vuelta esperando y estan escritos en sus puntos `6.8` y `6.6`: el remedio del `E.1` sobre `scripts/loop/cerrar_reporte.py`, que es la rama que escribe la cabecera CORRIDA ENTERA Y SOLA sobre una seccion 9 cuyo cuerpo dice que nadie la corrio, y la `P.1`, el arnes `vuelta172_tarea1c_guarda_que_mordio.py`, que cae con exit 1 fallando 1 de 6 y esta fuera del censo: primero el esperado y despues el nombre, en ese orden, que es parte de la adjudicacion. (c) LA RELECTURA AL DOBLE del tramo de la ciega que el acta 181 encarga en su `7.2` por `AUDITOR.md` 1.2, sobre los 30 puestos que su seccion 8 lista'),
    ("2", 'LA APERTURA DEL AUDITOR COMO CODIGO (decision del fundador del 5 sep 2026, PREGUNTA 3, opcion c, la mitad que quita el problema de raiz; la otra mitad, que ROMPER UN REMEDIO ESCRITO ACUMULE, ya esta escrita en `AUDITOR.md`). Fichero GEMELO del bloque de apertura del ejecutor: corre `scripts/loop/aislador_de_ciega.py` y SELLA SU SALIDA ANTES de que el turno pueda tocar `git log`, `git status` o `docs/loop/REPORTE.md`. Con CASO POR MUTACION SOBRE VARIABLE COMPUTADA, no sobre constante literal (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): si el sello se intenta DESPUES de tocar cualquiera de los tres, TIENE QUE CAER, y la prueba se corre cambiando el valor esperado para comprobar que el caso cae de verdad'),
    ("3", 'EL INSTRUMENTO DEL DIFERENCIADOR MOVIDO (decision del fundador del 5 sep 2026, PREGUNTA 1, la `b`). Cruza LA RAZON ESCRITA de cada `D` contra LOS PASOS DE HOY del otro nodo, y SOLO las `D` con la lesion exacta vuelven a la cola. CASO POSITIVO OBLIGATORIO: EL PUESTO 2.464 TIENE QUE SALIR NOMBRADO; si no sale, el instrumento no sirve y se dice. Y EL CENSO POR ESTADO DE LAS `A` en el mismo instrumento: ejecutadas contra pendientes, con LAS PENDIENTES DE TEXTO MOVIDO MARCADAS RANCIAS POR `P.5`. Las `A` NO ganan cola nueva: la ejecutada es cosa consumada y la pendiente ya la cubre `P.5`'),
    ("4", 'LAS `D` QUE EL INSTRUMENTO NOMBRE ENTRAN A LA COLA de relectura post fusion de `docs/plan/08_VERIFICACION.md`, y se releen POR TRAMOS en las vueltas siguientes. En esta vuelta SE ENTRA A LA COLA Y SE DECLARA EL TRAMO; no se releen 543 pares, que es justo lo que la decision del fundador evita al conceder la `b` y no la `c`'),
    ("5", 'LA VUELTA DE BATERIA VA EN LA 183, POR TRAMOS RESUMIBLES (decision del fundador del 5 sep 2026, PREGUNTA 4, opcion `a`, con el precedente de los nueve tramos de la vuelta 176). Aqui SOLO se deja preparada y declarada: nueve tramos, cada uno se commitea CON SU SALIDA SELLADA al terminar, una vuelta cortada RETOMA EN EL TRAMO SIGUIENTE, y la bateria se declara corrida cuando LOS NUEVE tienen salida sellada DEL MISMO CALIBRE. En esta vuelta la seccion 9 del reporte cierra con su HUECO DECLARADO Y MEDIDO, como el regimen `6.1` manda'),
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
> **ESTA VUELTA NO ES DE BATERIA, Y ESO TAMBIEN ES LETRA.** `AUDITOR.md` 6.1: la
> bateria corre CADA CINCO, en VUELTA PROPIA. **La 181 era la suya y se corto
> antes de lanzarla**, y su acta lo registra en el punto 7.5 sin contarlo como
> caida de reporte, porque el esqueleto por anexion dejo la fila diciendo ABIERTA,
> SIN CERRAR y no publico ninguna cifra de una corrida que no hubo. La decision
> del fundador del **5 sep 2026** (PREGUNTA 4 de
> `docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md`) manda que corra
> **POR TRAMOS RESUMIBLES**, y la **TAREA 5** de este encargo la deja preparada y
> declarada para la **183**. **La seccion 9 de este reporte cierra con su HUECO
> DECLARADO Y MEDIDO**, que es lo que el regimen 6.1 manda para las vueltas
> intermedias: un hueco declarado no es un hueco escondido.
>
> **EL TOPE DE ESTA VUELTA ES CINCO SUB-TAREAS, Y TAMPOCO ES UNA GANA.** La
> adjudicacion **6.8 del acta 180** bajo el tope a DOS en la 181 porque era vuelta
> de bateria, y en la misma frase escribio: *"El tope vuelve a cinco en la 182"*.
> El encargo de esta vuelta trae **CINCO** y dice *"que es el tope. Ni una mas"*.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee
> ninguno de los 543 pares que la TAREA 4 mete en la cola (eso es justo lo que la
> decision del fundador evita al conceder la `b` y no la `c`), no se toca el
> marcador, no se cambia ningun veredicto del archivo, y **las `A` no ganan cola
> nueva** por la PREGUNTA 2 de la misma decision. **Y no se corre la bateria**: se
> prepara.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno, la 179 y la 180 lo repitieron y aqui
> vuelve a correr en su sitio. **Desde la 178, una columna de apertura medida al
> cierre es caida que ACUMULA.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la
> %(ant)d escribio su reporte, lo cerro y lo archivo EN SU MISMA VUELTA; el
> fichero corre LAS DOS igualmente y publica lo que salga de cada una, porque una
> guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.

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
