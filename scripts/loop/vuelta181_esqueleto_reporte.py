r"""vuelta181_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA
VUELTA 181, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS DOS TAREAS ENCARGADAS.

CLON DECLARADO de scripts/loop/vuelta180_esqueleto_reporte.py. Lo que se toca a
mano son las DOS filas de tarea, que son las de ESTE encargo, y los parrafos de
prosa que hablan del estado del bucle. La maquina no se toca en ninguna linea
salvo el numero de vuelta.

Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA: el cotejo lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte, que es
obligatorio desde la vuelta 178 por el docstring de aquel fichero. Este texto NO
publica ningun resultado de diff.

DE DONDE VIENE ESA CAUTELA, Y NO SE BORRA DE QUE IBA: la CAIDA DE REPORTE 1 del
acta 176 seccion 5. El esqueleto de la 176 publicaba en su docstring que el
`diff` con `NNN` sustituido "SALE VACIO"; el auditor lo corrio y salieron 58
lineas, 33 de ellas de la maquina, aunque de esas 33 las SENTENCIAS DE CODIGO
eran 1 y los LITERALES DE TEXTO 32 medidos por el instrumento.

POR QUE ESTA VUELTA TRAE DOS FILAS Y NO CINCO, Y NO ES UN DESCUIDO: la
adjudicacion 6.8 del acta del auditor de la vuelta 180. `AUDITOR.md` 6.1 dice que
la vuelta de bateria NO LLEVA NADA MAS y `AUDITOR.md` 6.2 devuelve el tope a
cinco; las dos salen de la MISMA parada del 5 sep 2026 y la 6.2 se concedio
"combinada con la (a)", o sea subordinada a ella. Manda la 6.1. El tope vuelve a
cinco en la 182.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
`vuelta_del_reporte_del_arbol` esta copiada de
`vuelta174_esqueleto_reporte.py` en vez de importada, y la guarda que CAE EN ROJO
si esa fuente desaparece la escribio la TAREA 4.b de la vuelta 180: corre aqui
como PASO 0.0, antes que nada.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 181 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
`git rev-parse --abbrev-ref HEAD`; commit del acta de la vuelta anterior por las
DOS formas del titulo y en las DOS pasadas de `TALLADOR.buscar_acta`; HEAD de
apertura leido de docs/loop/SALIDA_V181_HEAD_APERTURA.txt, sellado antes de la
primera operacion; commit de nacimiento del bloque de apertura por
`git log --diff-filter=A`. Si alguno no se puede leer o es ambiguo, el esqueleto
CAE EN ROJO y no escribe nada: no inventa un hash.

USO:
  python scripts/loop/vuelta181_esqueleto_reporte.py
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
VUELTA = 181
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
    ("1", 'LOS REGISTROS, Y LO QUE SE HEREDA DEL ACTA 180, Y ES BLOQUEANTE. (a) El acta del auditor de la vuelta 180 vive en `docs/loop/ACTA_AUDITOR.md` con su cabecera en la linea `62449`, y levanta UNA caida de reporte contra la 180, la `E.1`, que vive en la cabecera de su seccion 9 y por tanto ACUMULA: la racha de reporte pasa de CERO a UNO. NO hay ninguna caida de cifra publicada (racha 0) y NO hay ninguna correccion declarada que arrastrar. Los CINCO discutibles de la 180 quedan adjudicados a favor del ejecutor los cinco (puntos 6.1 a 6.5), y el `D.1` corrige ademas el propio encargo del auditor, que lo registra como caida suya. La caida propia del auditor, la tercera seguida, esta en la seccion 2 del acta con el remedio que ata al auditor de la 181: no es trabajo del ejecutor y se cita para que quede en el carril de lectura. (b) Y se anota lo que NO se hace aqui y cuando se hace: la `P.1` (`vuelta172_tarea1c_guarda_que_mordio.py`, en rojo y fuera del censo) queda adjudicada en el `6.6` y el remedio del `E.1` en el `6.8`, LAS DOS EN LA 182'),
    ("2", 'LA BATERIA DE MUTACIONES, ENTERA, SOLA, Y CON SU RELOJ, Y ES LA UNICA TAREA DE TRABAJO DE ESTA VUELTA. (a) `scripts/loop/verificar_mutaciones_viejas.py` SIN `--tramo`, sobre la nomina entera, cada entrada corrida DOS VECES (el cotejo de reproducibilidad de la vuelta 141, que no se afloja), con la salida en `docs/loop/SALIDA_V181_BATERIA.txt` con ese nombre exacto y publicada COMPLETA Y SIN RECORTAR en la seccion 9; y con la guarda nueva de una linea que nace de la `E.1`: el valor de `vuelta que lleva dentro el nombre del fichero` que imprime `cerrar_reporte.py` TIENE QUE DECIR 181, y si dice `None` u otro numero SE PARA. (b) EL RELOJ, medido en esta corrida y no elegido a ojo: tiempo total, tiempo por entrada con su maximo, su minimo y su mediana, el nombre del arnes mas lento, y si el tope de 10 minutos se toco o no CON LA CIFRA AL LADO. Se mide, se publica y no se cambia nada. (c) EL VEREDICTO DE LAS SEIS PIEZAS de `hay_rojo_al_cierre()` una a una, cada una con su cifra, y no solo el color final. (d) LA DOBLE CORRIDA COTEJADA Y PUBLICADA COMO TAL, nombrando a quien no reproduzca. (e) NADA SE PODA DE LA NOMINA (`AUDITOR.md` 6.1), y si la bateria destapa un arnes roto NO se borra ni se saca: se deja en rojo, se nombra y se trae'),
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
> **ESTA ES LA VUELTA DE BATERIA, Y NO LLEVA NADA MAS.** `AUDITOR.md` 6.1: la
> bateria corre CADA CINCO, en VUELTA PROPIA. La cadencia se adjudico en el acta
> 176 punto 7.8, se reconfirmo en las actas 178 y 179, y el acta 180 la clava por
> cuarta vez en su punto 10 con estas palabras: *"LA BATERIA: LA PROXIMA ES LA
> 181, Y ES LA VUELTA QUE VIENE"*. **La 180 fue la ULTIMA que declaro el hueco.
> Aqui se corre.**
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y NO ES UN DESCUIDO: ES LA
> ADJUDICACION 6.8 DEL ACTA 180.** `AUDITOR.md` 6.2 devolvio el tope a cinco, pero
> la 6.1 y la 6.2 salen de la MISMA parada del 5 sep 2026 y la 6.2 se concedio
> *"combinada con la (a)"*, o sea subordinada a ella. **La vuelta de bateria no
> lleva trabajo de plan al lado.** El tope vuelve a cinco en la 182.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se lee ningun
> par, no se escribe ningun veredicto, no se toca el marcador, no se toca el estado
> de ninguna ficha, no se toca `docs/plan/`, no se arregla la `P.1` y no se toca
> `cerrar_reporte.py`. **Las dos ultimas van a la 182 y estan escritas en los
> puntos 6.6 y 6.8 del acta 180.**
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
