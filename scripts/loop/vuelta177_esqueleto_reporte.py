# -*- coding: utf-8 -*-
r"""vuelta177_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA
VUELTA 177, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS DOS TAREAS ENCARGADAS.

CLON DECLARADO de scripts/loop/vuelta176_esqueleto_reporte.py, hecho con `sed`
cambiando UNICAMENTE el numero de vuelta. Lo que se toca a mano despues de ese
`sed` son las DOS filas de tarea y los parrafos de prosa que hablan del estado
del bucle, que son distintos porque esta vuelta no es de bateria.

Y LA AFIRMACION DE CLON NO SE PUBLICA COMO COMPROBADA EN ESTE DOCSTRING, QUE ES
JUSTO LA CAIDA QUE EL ACTA 176 SECCION 5 LEVANTO CONTRA EL FICHERO DEL QUE ESTE
DESCIENDE. Aquel decia que el `diff` con `NNN` sustituido salia vacio; el auditor
lo corrio y salieron 58 lineas, 33 de ellas de la maquina. AQUI NO SE AFIRMA
NINGUN RESULTADO DE `diff`: el cotejo lo hace el instrumento que nace en la
TAREA 1.d de esta misma vuelta, `scripts/loop/cotejar_clon_declarado.py`, que da
TRES veredictos separados (fichero entero, solo docstring, solo la maquina) y
clasifica lo que difiera en SENTENCIAS DE CODIGO y LITERALES DE TEXTO. Su salida
se pega en el reporte, y a partir de la 178 eso es obligatorio.

LA MAQUINA NO CAMBIA EN NADA: el paso 0 endurecido que estreno la 174 se conserva
entero. Esa frase SI es una afirmacion sobre la maquina, y por eso NO se publica
como comprobada aqui tampoco: la comprueba el instrumento, no este texto.

QUE ES ESE PASO 0 ENDURECIDO, dicho otra vez para que este fichero se entienda
solo: NO PREGUNTA POR `VUELTA - 1`, PREGUNTA POR EL REPORTE QUE DE VERDAD VA A
PISAR, Y ESE NUMERO SE LEE DEL PROPIO FICHERO con la funcion pura
`vuelta_del_reporte_del_arbol()`. En esta vuelta las dos preguntas coinciden (el
arbol trae el reporte de la 176 y `VUELTA - 1` es 176), y precisamente por eso el
fichero corre LAS DOS y publica lo que salga de cada una: una guarda que solo se
mira cuando difiere no se puede auditar el dia que difiera.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA: `vuelta_del_reporte_del_arbol`
esta copiada de `vuelta174_esqueleto_reporte.py` en vez de importada. Importarla
crearia una dependencia nueva sobre un fichero numerado sin nada que avise si
alguien lo borra por viejo, que es justo el hallazgo (e) que el encargo de esta
vuelta anota como PENDIENTE PARA LA 177. Se clona, se declara, y el arnes de la
funcion original (`scripts/loop/vuelta174_tarea1b_mutacion_esqueleto.py`) sigue
apuntando a su sujeto de siempre y no se toca.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 177 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
`git rev-parse --abbrev-ref HEAD`; commit del acta de la vuelta anterior por las
DOS formas del titulo y en las DOS pasadas de `TALLADOR.buscar_acta`; HEAD de
apertura leido de docs/loop/SALIDA_V177_HEAD_APERTURA.txt, sellado antes de la
primera operacion; commit de nacimiento del bloque de apertura por
`git log --diff-filter=A`. Si alguno no se puede leer o es ambiguo, el esqueleto
CAE EN ROJO y no escribe nada: no inventa un hash.

USO:
  python scripts/loop/vuelta177_esqueleto_reporte.py
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paso0_archivar_anterior as PASO0   # noqa: E402
import tallar_cabecera_reporte as TALLADOR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = 177
PATRONES_ACTA = [
    re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR" % (VUELTA - 1)),
    re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA %d" % (VUELTA - 1)),
]
PATRON_ACTA = "ACTA DE LA VUELTA %d DEL AUDITOR o ACTA DEL AUDITOR, VUELTA %d" % (
    VUELTA - 1, VUELTA - 1)

TAREAS = [
    ("1", "LOS REGISTROS Y LAS CORRECCIONES, Y ES BLOQUEANTE. Siete letras: (a) dejar constancia de la lectura del acta 176 nombrando sus adjudicaciones; (b) EL ARNES DEL ROJO, que es lo primero que se arregla, computando el esperado de la misma fuente viva en vez del `3` tecleado de la linea 175, SIN pasarlo a caso declarado, SIN re-anclarlo a sujeto congelado y SIN podar la nomina, con su caso positivo por mutacion que pruebe que el arnes SIGUE MORDIENDO; (c) la correccion declarada de la caida de reporte 1 del acta 176, el `diff` del clon que se publico como vacio y no lo es, en los DOS docstrings y sin borrar de que iban; (d) `scripts/loop/cotejar_clon_declarado.py`, el instrumento de nombre estable que hace innecesaria esa correccion a mano, con TRES veredictos separados y la clasificacion de SENTENCIAS DE CODIGO contra LITERALES DE TEXTO; (e) las dos correcciones chicas del acta, la salida del lanzador fuera de `docs/loop/` (`D.5`) y el tallador sellando su propio rechazo; (f) `D.3` y `P.3`, el tope de tramo POR MINUTOS computado del reloj medido dentro de `reparto_en_tramos()`, para que la 181 no lo decida a ojo; (g) contar en voz alta lo que NO entra en esta vuelta"),
    ("2", "`OP-L-03`, QUE LLEVA SIETE VUELTAS APLAZADA Y SE DESAPLAZA AQUI. La vara de hoy la sigue dando en LISTA sin ninguna prueba de ejecucion. Leer los ACTOS GRANDES primero, que es donde la lectura por acto cambia algo: el de SEIS miembros y los cuatro de CINCO. El criterio es `P.5` del banco del plan y se CITA, no se parafrasea: cada acto que vaya a fundirse se lee ENTERO despues de su destejido y antes de su fusion, y la decision es POR ACTO y no por pareja. Cada lectura se registra en JSONL y no se narra en prosa; ningun veredicto se mueve sin correccion declarada y recomputo; las 55 lecturas marcadas LECTURA DIRIGIDA no entran en la cola ni mueven su marcador; y el campo `estado` de la ficha NO SE TOCA aunque la operacion termine, porque la vara es `vuelta150_3_relectura_expediente.py` por decision del fundador del 4 sep 2026"),
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
            fallos.append("el sello %s no trae un hash de 40 caracteres" % os.path.basename(ruta_head))

    c, nac = git(["log", "--diff-filter=A", "--format=%H", "--",
                  "docs/loop/SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA])
    nacs = [l for l in nac.splitlines() if l.strip()]
    if len(nacs) != 1:
        fallos.append("commits que ANADEN el sello de apertura: %d (se necesita exactamente 1)" % len(nacs))
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
> **ESTA VUELTA NO ES DE BATERIA, Y LA CADENCIA NO SE ELIGE AQUI: ESTA
> ADJUDICADA.** El acta 176, punto 7.8, reancla el contador a la vuelta que de
> verdad corrio la bateria y no a la que la tenia encargada: **la 175 no fue una
> vuelta de bateria porque murio sin producir una linea**, la corrio la 176, y
> desde ella se cuentan los cinco. **La proxima vuelta de bateria es la 181, no
> la 180.** Por eso la seccion 9 de este reporte cierra con el **HUECO DECLARADO
> Y MEDIDO** por el carril de la TAREA 1.b de la 173, con su medicion, su
> atribucion y su corrida. Un hueco declarado no es un hueco escondido.
>
> **EL TOPE DE ESTA VUELTA SIGUE EN DOS** (`AUDITOR.md` 6.2, regimen temporal
> vigente hasta que DOS vueltas seguidas cierren su propio reporte con
> `cerrar_reporte.py`), y el encargo trae exactamente dos. **LA 176 ES LA PRIMERA
> DE LAS DOS SEGUIDAS**, medido y no supuesto: cerro su reporte y lo archivo en su
> misma vuelta. **Si esta cierra el suyo, el tope vuelve a CINCO por la propia
> letra de la 6.2, sin que nadie tenga que decidirlo.**
>
> **Y ESTA VUELTA SI CORRIO SU BLOQUE DE APERTURA ANTES DE SU PRIMERA
> OPERACION**, que es lo que la 176 no hizo. Su lectura (que la 6.1 sacaba el
> aparato de abrir y cerrar la vuelta) **quedo corregida en el acta 176 punto
> 7.1**: la 6.1 saca el TRABAJO DE PLAN, no el aparato; si lo sacara, sacaria
> tambien el reporte y la 6.1 y la 6.2 se contradirian. Ademas esta vuelta no es
> de bateria, asi que la duda ni se plantea.
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas coinciden, porque la
> %(ant)d escribio su reporte, lo cerro y lo archivo; el fichero corre LAS DOS
> igualmente y publica lo que salga de cada una, porque una guarda que solo se
> mira cuando difiere no se puede auditar el dia que difiera.

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
