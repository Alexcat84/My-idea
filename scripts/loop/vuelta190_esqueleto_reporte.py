# -*- coding: utf-8 -*-
r"""vuelta190_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 190,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta189_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS (aqui son CINCO, porque el tope temporal de dos de la
`AUDITOR.md` 6.2 caduco por la adjudicacion 4.10 del acta 190), este docstring y
el bloque de prosa del encabezado. El cotejo del clon lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte con lo
que salga: AQUI NO SE AFIRMA QUE NINGUN DIFF SALGA VACIO.

ESTA VUELTA NO ES DE BATERIA (AUDITOR.md 6.1: corre cada cinco vueltas, la 189 la
corrio entera, y la siguiente cae en la 194). Su seccion 9 cierra con el HUECO
DECLARADO Y MEDIDO por el carril de cerrar_reporte.py, con su medicion, su
atribucion y su corrida.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 190 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V190_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada:
no inventa un hash.

Y SE DECLARA EL DESFASE QUE NO SE REPARA, POR SEXTA VUELTA: PATRONES_ACTA
sigue pidiendo el acta de VUELTA - 1, o sea la 189, cuando el acta que ORDENA
esta vuelta es la 190. Es el `D.2` del reporte de la 184, adjudicado a favor por
la `5.2` del acta 185 CON REPARACION ENCARGADA, y esta vuelta NO la ejecuta
porque no es ninguna de sus cinco tareas y el encargo nombra una a una las seis
que quedan fuera. Se declara en vez de colarse.

USO:
  python scripts/loop/vuelta190_esqueleto_reporte.py
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
VUELTA = 190
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
    ("1", 'LOS REGISTROS. BLOQUEANTE. El acta 190 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus DIEZ adjudicaciones `4.1` a `4.10`, QUE NO SON DIEZ A FAVOR: seis son los discutibles del ejecutor y de esos CINCO van A FAVOR (`D.1`, `D.2`, `D.3`, `D.4`, `D.6`) y UNO EN CONTRA, el `D.5`, la guarda del sujeto congelado fuera del veredicto. La marca de EN CONTRA tiene que EXISTIR y tiene que SALIR EN LA CUENTA, probada por mutacion con un acta fabricada. Mas las TRES preguntas contestadas (`4.4` la `P.1`, `4.8` la `P.2`, `4.9` la `P.3`), los DOS hallazgos de la seccion 5 que no salen de ningun discutible (las dos convenciones de `lineas` en `5.1` y las ocho actas sin entrada propia en `5.2`), CERO caidas propias del auditor ESCRITO COMO CERO Y NO OMITIDO y TRES del ejecutor, las tres DE METODO y ninguna de racha, y LA VARA CORRIDA POR EL AUDITOR (`5.4`) con sus cifras. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido, no escribe nada, y se prueba re corriendolo con la sede medida antes y despues'),
    ("2", 'LA GUARDA DEL SUJETO CONGELADO: SEPARA LA DEUDA DEL FALLO, Y VUELVE AL VEREDICTO. Son las adjudicaciones `4.4` y `4.6` del acta 190 y las dos mitades van juntas porque una sin la otra no sirve. (a) la guarda SEPARA EN SU SALIDA las entradas `NO DECIDIBLE` que traen MOTIVO ESCRITO de las que no lo traen, y publica LAS DOS CIFRAS CON SUS NOMBRES; hoy "3 entradas sin congelar" no distingue una deuda de una decision, y esa es la `P.1` que el acta 189 dejo encargada en su `4.7`. Las tres de hoy son `vuelta186_tarea2c_mutacion_cierre_tardio.py`, `vuelta187_tarea4_mutacion_dos_convenciones.py` y `vuelta188_tarea4_mutacion_cobertura_parejas.py`, y cuantas traen motivo escrito SE MIDE. (b) LA GUARDA VUELVE AL VEREDICTO del instrumento de la nomina: el `D.5` de la 189 la saco y el acta 190 lo TUMBA, porque publicar los tres nombres arriba y cerrar en verde deja sin sintoma al que solo mire el veredicto. Con la separacion de (a) puesta, el veredicto ya puede decir ROJO POR DEUDA DECLARADA distinto de ROJO POR FALLO sin dejar de ser rojo. NO SE AFLOJA NINGUNA GUARDA, y el rojo que salga se trae con su nombre. Con simulacion previa sobre copia en memoria y caso positivo por mutacion'),
    ("3", 'LA BATERIA: QUE SU EXITCODE SEPARE, Y QUE RESTAURE SOLA LO QUE PISA. Son las adjudicaciones `4.4` y `4.9` del acta 190, y NO SE CORRE LA BATERIA en esta vuelta: se arregla su lanzador y se prueba con sus arneses. (a) EL EXITCODE SEPARA: hoy los diez tramos de la 189 salieron con exitcode 1 y en NUEVE de ellos no cayo ni un arnes, porque la fuente era siempre la guarda de nomina en deuda, y un unico `1` para un arnes caido y para una deuda declarada es degradacion silenciosa (banco 9). Que el lanzador distinga los dos casos en su salida sellada y en su codigo de salida, y que lo diga con su cifra. (b) LA BATERIA RESTAURA SOLA LAS SALIDAS SELLADAS AJENAS QUE PISA, como ya restaura `dataset/`: en la 189 piso TRES y las restauro una persona a mano, en dos vueltas distintas y a dos personas distintas. La restauracion va EN LF, y si el corte nuevo interesa se escribe AL LADO con nombre nuevo y su vuelta, nunca encima. Con simulacion previa y caso positivo por mutacion que CAIGA si una salida sellada ajena se queda pisada'),
    ("4", 'LA RELECTURA AL DOBLE DEL TRAMO DEL PUESTO 2422. ES UNA DEUDA DEL ACTA 189 Y NO SE SALTA DOS VUELTAS SEGUIDAS: la 189 la aplazo con razon por ser vuelta de bateria, y esa razon ya no vale. El acta 189 encontro la discrepancia del puesto `2422` FUERA de sus dudosos marcados, y `AUDITOR.md` 1.2 dice que eso baja el credito de la tanda y obliga a releer ese tramo AL DOBLE. Corre la relectura con `scripts/loop/aislador_de_ciega.py`, sobre los vecinos deterministas del tramo del `2422`, con el criterio escrito, la ciega y el destape en ficheros separados, y las clases escritas ANTES de abrir el destape. Publica cuantos coinciden y cuantos discrepan. NO SE TOCA NINGUNA CLASE del archivo: si de la relectura sale una correccion se declara y se trae, y no se escribe sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en esta vuelta. El `sha256` LF del archivo abre y cierra en `0a77b5a35a962621`'),
    ("5", 'LA SEDE DE `OP-L-02`: BUSCARLA, NO INVENTARLA. Es la `4.1` del acta 189 y la vara del acta 190 (`5.4`) la confirma medida: corrida con `--corte 63d0c5b4` da 71 fichas, 6 en LISTA sin ninguna prueba, 2 de ellas CONSUMIDAS por `OP-U-01` y 4 de TRABAJO REAL; de esas cuatro, tres son mesas cuyo producto documental SI existe en disco, y `OP-L-02` es LA UNICA SIN DOCUMENTO QUE MEDIR, con 0 menciones de fichero en su evidencia. Su `verificacion` habla de "las tres nominas afectadas" y de "cada grupo del backlog": BUSCA SI ESAS TRES NOMINAS TIENEN SEDE EN EL REPO, con comandos propios, y publica la busqueda entera (que se busco, donde, y que se encontro). Y EL LIMITE, ESCRITO PARA QUE NO SE CRUCE: si la busqueda no encuentra sede en ninguna parte, ESO ES EL RESULTADO Y SE PUBLICA COMO TAL. NO se le inventa una sede a la ficha, ni se declara HECHA, ni se mueve de estado: inventarle una sede es cambiar el alcance de la campana, y eso lo reserva el fundador'),
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
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que **no lleva
> nada mas**. **La 189 la corrio entera** (sus diez tramos siguen sellados en
> disco y el bloque **H.5** del sello de apertura los remidio uno a uno antes de
> tocar nada), asi que **la siguiente cae en la 194**. El hueco va **con su
> medicion, su atribucion y su corrida, por el carril de `cerrar_reporte.py`**:
> un hueco declarado no es un hueco escondido.
>
> **Y VAN CINCO SUB-TAREAS Y NO DOS.** El tope temporal de la `AUDITOR.md` 6.2
> **se cumplio y caduca**: su disparador de salida pedia **DOS vueltas seguidas
> cerrando su propio reporte** con `cerrar_reporte.py`, y **son TRES**. El bloque
> **B.2** del sello de apertura las localizo **en git y no de memoria**, por el
> asunto de su commit, y midio ademas sus tres ficheros de cierre con
> `CIFRA piezas que faltan: 0` en los tres. **Vuelve el tope de CINCO** de la
> seccion 6 de `EJECUTOR.md`.
>
> **DONDE SE TALLO ESTE ESQUELETO: EN LA APERTURA Y EN SU PROPIO COMMIT.** Desde
> el segundo commit de esta vuelta ya hay reporte parcial en el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** ni cribado, ni
> recomputo, ni operaciones del plan que no sean la **busqueda** de la TAREA 5,
> ni las mesas anotadas, ni **podar la nomina** (la opcion `c` que el fundador
> RECHAZO el 5 sep 2026: **la nomina sigue creciendo y nadie la poda sin el
> fundador**). **Y no entran las SEIS que el encargo deja nombradas a proposito
> para que la 191 no las redescubra:** las dos convenciones de `lineas`,
> `acumulan()` contra la tabla, el cotejo de clon declarado que separa, la
> excepcion que publica siempre su lista, la medicion del censo de arneses sin
> fichero, y las ocho actas sin entrada propia en la serie. **Y no se corre la
> bateria.**
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo
> valor. **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al
> salir y **las dos cifras se publican**.
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
- **DESFASE DECLARADO, SEXTA VUELTA:** la linea de arriba nombra el acta
  **%(ant)d** porque `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que
  ORDENA esta vuelta es la 190**. Es el `D.2` del reporte de la 184, adjudicado a
  favor con reparacion encargada por la `5.2` del acta 185. **Esta vuelta no la
  ejecuta** porque no es ninguna de sus cinco tareas y el encargo nombra una a
  una las seis que quedan fuera. Se declara en vez de colarse.
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
