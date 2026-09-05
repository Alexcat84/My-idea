# -*- coding: utf-8 -*-
r"""vuelta176_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA
VUELTA 176, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS DOS TAREAS ENCARGADAS.

CLON DECLARADO de scripts/loop/vuelta175_esqueleto_reporte.py, hecho con `sed`
cambiando UNICAMENTE el numero de vuelta, y COMPROBADO en vez de afirmado: el
`diff` de los dos ficheros con todo `175` y `176` sustituido por `NNN` SALE
VACIO, y esa comprobacion se corrio en la vuelta 176 antes de usar este fichero.
Lo unico que se toca a mano despues de ese `sed` son las DOS filas de tarea y
los parrafos de prosa que hablan del estado del bucle, que son distintos porque
la 175 no cerro su reporte. LA MAQUINA NO CAMBIA EN NADA: el paso 0 endurecido
que estreno la 174 se conserva entero.

QUE ES ESE PASO 0 ENDURECIDO, dicho otra vez para que este fichero se entienda
solo: NO PREGUNTA POR `VUELTA - 1`, PREGUNTA POR EL REPORTE QUE DE VERDAD VA A
PISAR, Y ESE NUMERO SE LEE DEL PROPIO FICHERO con la funcion pura
`vuelta_del_reporte_del_arbol()`. En esta vuelta las dos preguntas coinciden (el
arbol trae el reporte de la 175 y `VUELTA - 1` es 175), y precisamente por eso el
fichero corre LAS DOS y publica lo que salga de cada una: una guarda que solo se
mira cuando difiere no se puede auditar el dia que difiera.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA: `vuelta_del_reporte_del_arbol`
esta copiada de `vuelta174_esqueleto_reporte.py` en vez de importada. Importarla
crearia una dependencia nueva sobre un fichero numerado sin nada que avise si
alguien lo borra por viejo, que es justo el hallazgo (e) que el encargo de esta
vuelta anota como PENDIENTE PARA LA 176. Se clona, se declara, y el arnes de la
funcion original (`scripts/loop/vuelta174_tarea1b_mutacion_esqueleto.py`) sigue
apuntando a su sujeto de siempre y no se toca.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 176 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
`git rev-parse --abbrev-ref HEAD`; commit del acta de la vuelta anterior por las
DOS formas del titulo y en las DOS pasadas de `TALLADOR.buscar_acta`; HEAD de
apertura leido de docs/loop/SALIDA_V176_HEAD_APERTURA.txt, sellado antes de la
primera operacion; commit de nacimiento del bloque de apertura por
`git log --diff-filter=A`. Si alguno no se puede leer o es ambiguo, el esqueleto
CAE EN ROJO y no escribe nada: no inventa un hash.

USO:
  python scripts/loop/vuelta176_esqueleto_reporte.py
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
VUELTA = 176
PATRONES_ACTA = [
    re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR" % (VUELTA - 1)),
    re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA %d" % (VUELTA - 1)),
]
PATRON_ACTA = "ACTA DE LA VUELTA %d DEL AUDITOR o ACTA DEL AUDITOR, VUELTA %d" % (
    VUELTA - 1, VUELTA - 1)

TAREAS = [
    ("1", "LA BATERIA DE MUTACIONES ENTERA, SOLA Y CON SU DOBLE CORRIDA, PERO PARTIDA EN TRAMOS QUE QUEPAN EN UNA SESION, porque la causa de que la 175 se la comiera entera esta MEDIDA: 87 entradas por dos corridas cada una son un bloque indivisible de entre 57 y 75 minutos. Se parte el BOCADO y no se afloja NADA de las cuatro cosas que la letra del fundador del 5 sep fija (cadencia, soledad, integridad y la prohibicion de podar la nomina): cada entrada sigue corriendo y sigue corriendo DOS VECES. Lleva dentro su GUARDA DEL COMMIT bloqueante y su RESTAURACION AL ENTRAR de cada tramo, cada tramo SELLA Y COMMITEA su propia salida, y al final la salida unica se COMPONE y se MIDE (bytes, lineas, sha256) antes de nombrarla en ningun sitio"),
    ("2", "ABRIR Y CERRAR ESTE MISMO REPORTE EN LA MISMA VUELTA. La 174 lo hizo entero, la 175 NO LLEGO (murio dentro de la bateria y dejo sus dos filas diciendo ABIERTA, SIN CERRAR), asi que la racha que `AUDITOR.md` 6.2 pide VUELVE A EMPEZAR y esta es OTRA VEZ la primera de las dos seguidas. Esqueleto al empezar, la fila de la TAREA 1 anexada al cerrarse CADA TRAMO y no al final, cierre con `scripts/loop/cerrar_reporte.py` en esta misma vuelta, y ARCHIVADO EN LA MISMA VUELTA sin esperar a la 177")
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
> **ESTA ES OTRA VEZ UNA VUELTA DE BATERIA, Y NO ES UN CAMBIO DE CADENCIA: ES LA
> DEUDA DE LA 175, QUE NO SE PAGO** (`AUDITOR.md` 6.1, decision del fundador del 5
> sep 2026). La bateria corre CADA CINCO, en una vuelta propia QUE NO LLEVA NADA
> MAS, y la vuelta propia que le tocaba se murio antes de producir una linea. Aqui
> no hay trabajo de plan al lado, y `OP-L-03` no se toca: lleva SEIS vueltas
> aplazada y se cuenta en voz alta. **EL TOPE DE ESTA VUELTA NO ES CINCO SINO DOS**
> (`AUDITOR.md` 6.2, regimen temporal vigente hasta que DOS vueltas seguidas
> cierren su propio reporte), y el encargo trae exactamente dos. **La 174 fue la
> primera de esas dos, la 175 no cerro, y la racha VUELVE A EMPEZAR: esta es otra
> vez la primera.**
>
> **LO QUE SE PARTE ES EL BOCADO, NO LA BATERIA.** La 175 murio DENTRO de la
> corrida, y la causa esta medida y no supuesta: 87 entradas, cada una corrida DOS
> VECES, son un bloque indivisible de entre 57 y 75 minutos. Partirla en tramos
> DENTRO de esta misma vuelta no toca ninguna de las cuatro cosas que la letra del
> fundador fija (cadencia, soledad, integridad y la prohibicion de podar la
> nomina). **La nomina sigue en 87 y sigue creciendo.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la
> %(ant)d si escribio su reporte (ABIERTO Y SIN CERRAR, que es texto igual) y es el
> que hay en el arbol; el fichero corre LAS DOS igualmente y publica lo que salga
> de cada una, porque una guarda que solo se mira cuando difiere no se puede
> auditar el dia que difiera.

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
