# -*- coding: utf-8 -*-
r"""vuelta200_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 200,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta199_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS, este docstring y el bloque de prosa del encabezado.
EL CODIGO DE LAS FUNCIONES VA IGUAL, byte a byte.

POR QUE DOS TAREAS, Y LA CIFRA NO SE TECLEA: la racha de cierres, contada del
instrumento en el bloque `E` del sello de apertura de ESTA vuelta, vale 1, con
la vuelta 199. `AUDITOR.md` 6.2 apaga el regimen temporal de dos sub-tareas
cuando DOS VUELTAS SEGUIDAS cierran su propio reporte con `cerrar_reporte.py`, y
con racha 1 el tope SIGUE SIENDO DOS. El encargo trae DOS. LA CIFRA SE LEE DEL
SELLO, con `racha_del_sello()`, y si el sello no la trae este esqueleto CAE EN
ROJO y no escribe nada.

Y ADEMAS ESTA ES LA VUELTA DE BATERIA POR LA CADENCIA DE `AUDITOR.md` 6.1, que
dice que NO LLEVA NADA MAS. Por eso la TAREA 2 es la bateria entera y no hay
trabajo de plan al lado: la correccion declarada de `OP-I-01` y la medicion de
`OP-L-02`, que el acta 199 ya adjudico en su `4.1` y su `4.2`, van a la 201.

EL DESFASE DE `PATRONES_ACTA` NO APARECE EN ESTA VUELTA, Y ESO SE MIDE EN VEZ DE
SUPONERSE: `PATRONES_ACTA` pide el acta de `VUELTA - 1`, o sea la 199, y el acta
que ORDENA esta vuelta ES la 199 (la 200 no existe todavia, y el bloque `H` del
sello de apertura lo cuenta: 1 acierto para la 199 y 0 para la 200). El literal
`DESFASE DECLARADO` se sigue CONTANDO de los reportes archivados, con su fecha de
corte, porque esa cifra es de inventario y envejece sola.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

USO:
  python scripts/loop/vuelta200_esqueleto_reporte.py
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
VUELTA = 200
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
    ("1", 'LOS REGISTROS. BLOQUEANTE. El acta 199 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, y su cuerpo se acota con `grep -n` EN ESTA VUELTA. Y con la entrada van LAS TRES CORRECCIONES DE CIFRA que la seccion 3 del acta 199 levanta, cada una EN SU SEDE, por el carril del banco `9.10` mas `EJECUTOR.md` 8, CON EL TEXTO VIEJO ENTERO Y SIN TACHAR: (1.a) la `C.1`, LA QUE ACUMULA, el reporte de la 199 dice UN arnes del censo fuera de la nomina con la vara 148 y al commit de cierre son DOS, y NO SE CORRIGE TECLEANDO EL DOS sino volviendo a correr `V.arneses_que_faltan(vara=148)` y pegando su salida con su corte, mas la cifra SIN VARA que el reporte dio en 61; (1.b) la `C.2`, el literal `HUECO` en `docs/plan/10_INVENTARIO.md` sale 3 y no 4, y hay que decir si se corrige la cifra o la etiqueta; (1.c) la `C.3`, ese fichero tiene 413 lineas y no 414'),
    ("2", 'LA BATERIA ENTERA, POR TRAMOS, Y CON LA TRAMPA MEDIDA DELANTE. Es la TAREA de la cadencia de `AUDITOR.md` 6.1 y la vuelta NO LLEVA NADA MAS. El lanzador es `scripts/loop/vuelta183_bateria_por_tramos.py` y NO SE CLONA. Sus dos mitades, las dos medidas por el auditor corriendolas: `--siguiente` dice que faltan el 10 y el 11 sobre NUEVE SALIDAS AJENAS de la corrida de la 183, y correr el tramo 1 PISA la sellada del 183. Por eso: LAS NUEVE SE PRESERVAN POR COPIA con sus bytes y su `sha256` medidos antes y despues; SE CORREN LOS ONCE TRAMOS, no los dos que `--siguiente` dice, porque `--plan` da ONCE hoy y el NUEVE de 6.1 se escribio con una nomina menor; CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR; una salida sellada de CERO BYTES no cuenta como hecha; y la bateria se declara corrida cuando los once tienen salida sellada del mismo calibre, y el calibre lo coteja `--componer` y no el criterio del ejecutor'),
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
    vuelta 193 se publica CON SU FECHA DE CORTE (banco 9.21)."""
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


def racha_del_sello(texto):
    """LA RACHA DE CIERRES, LEIDA DEL SELLO DE APERTURA DE ESTA VUELTA Y NO
    TECLEADA. Devuelve (racha, cuales) o (None, None) si el sello no la trae.
    PURA: recibe el texto del sello.

    EXISTE PORQUE EL TOPE DE SUB-TAREAS DEPENDE DE ESA CIFRA (AUDITOR.md 6.2) y
    la cabecera de este reporte la publica. Una cifra que gobierna el tamano del
    encargo no se puede teclear."""
    if not texto:
        return None, None
    m = re.search(r"CIFRA racha de cierres, contada del inventario ENTERO:\s*(\d+)",
                  texto)
    q = re.search(r"las vueltas de la racha:\s*(.+)", texto)
    return (m.group(1) if m else None), (q.group(1).strip() if q else None)


def varas_de_la_nomina(texto):
    """LAS DOS CIFRAS DE LA TAREA 4.a, LEIDAS DEL SELLO DE APERTURA Y NO
    TECLEADAS. Devuelve (vara, con_vara, sin_vara) o (None, None, None).
    PURA: recibe el texto del sello.

    EXISTE PORQUE LA CIFRA DE FUERA DE LA NOMINA NO PUEDE VIAJAR SOLA: la
    adjudicacion 4.7 del acta 197 dice que un 0 sin su vara se lee como
    cobertura total del censo, y no lo es."""
    if not texto:
        return None, None, None
    a = re.search(r"CIFRA arneses del censo FUERA de la nomina CON LA VARA "
                  r"(\d+):\s*(\d+)", texto)
    b = re.search(r"CIFRA arneses del censo FUERA de la nomina SIN VARA "
                  r"\(vara=0\):\s*(\d+)", texto)
    if not a or not b:
        return None, None, None
    return a.group(1), a.group(2), b.group(1)


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

    # LA RACHA NO SE TECLEA: SE LEE DEL SELLO DE APERTURA DE ESTA VUELTA, que la
    # conto del instrumento ANTES de la primera operacion.
    ruta_sello = os.path.join(LOOP, "SALIDA_V%d_APERTURA.txt" % VUELTA)
    texto_sello = (io.open(ruta_sello, encoding="utf-8", errors="replace").read()
                   if os.path.exists(ruta_sello) else "")
    racha, cuales_racha = racha_del_sello(texto_sello)
    print("LA RACHA DE CIERRES, LEIDA DEL SELLO DE APERTURA Y NO TECLEADA:")
    print("   fichero: docs/loop/SALIDA_V%d_APERTURA.txt (%d bytes)"
          % (VUELTA, len(texto_sello.encode("utf-8"))))
    print("   CIFRA racha: %s | las vueltas: %s" % (racha, cuales_racha))
    print("")
    if racha is None:
        fallos.append("el sello de apertura no trae la cifra de la racha; el tope "
                      "de sub-tareas depende de ella y no se teclea")

    # LAS DOS VARAS DE LA NOMINA, TAREA 4.a, TAMBIEN LEIDAS DEL SELLO.
    vara, con_vara, sin_vara = varas_de_la_nomina(texto_sello)
    print("LAS DOS VARAS DE LA NOMINA, LEIDAS DEL SELLO Y NO TECLEADAS:")
    print("   vara %s | fuera CON vara: %s | fuera SIN vara: %s"
          % (vara, con_vara, sin_vara))
    print("")
    if vara is None:
        fallos.append("el sello de apertura no trae las dos cifras de la nomina "
                      "con y sin vara; la TAREA 4.a depende de ellas")

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
> **ESTA ES LA VUELTA DE BATERIA, Y NO LLEVA NADA MAS.** `AUDITOR.md` 6.1 lo dice
> con estas palabras: la bateria corre **cada cinco vueltas**, en una **vuelta
> propia** con **su doble corrida, su reloj y su salida sellada**, y **nada de
> trabajo de plan al lado**. Por eso este encargo trae **DOS** tareas y la segunda
> es la bateria; y por eso **la correccion declarada de `OP-I-01` y la medicion de
> `OP-L-02`, que el acta 199 ya adjudico en su `4.1` y su `4.2`, VAN A LA 201** y
> no se pierden.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3, decision del fundador
> del 7 sep 2026): **no se fabrican arneses, guardas ni lectores nuevos**, y **esta
> vuelta NO TIENE NINGUNA EXCEPCION**, porque las dos de la 199 se consumieron.
> **La nomina queda CONGELADA EN 135**, y el bloque `F` del sello de apertura la
> midio contra ese congelado.
>
> **EL TOPE SIGUE SIENDO DE DOS SUB-TAREAS, Y LA CIFRA QUE LO MANDA NO SE
> TECLEA.** El bloque `E` del sello de apertura de esta vuelta corrio el
> instrumento de la racha sobre el inventario ENTERO y **la racha de cierres vale
> %(racha)s**, con las vueltas **%(cuales)s**. `AUDITOR.md` 6.2 apaga el regimen
> temporal de dos sub-tareas cuando **DOS vueltas seguidas** cierran su propio
> reporte con `cerrar_reporte.py`, y con **%(racha)s** no se apaga. **Este encargo
> trae DOS, y cabe.**
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. **El desfase de calibrado se midio
> DENTRO del bloque de apertura y ANTES de la primera operacion.** Y su bloque `F`
> **es la medicion de la caida `C.1` del acta 199, tomada antes de mirar nada**: la
> cifra de arneses del censo fuera de la nomina **viaja con su vara y se miden las
> dos**, con vara **%(vara)s** salen **%(conv)s** y sin vara salen **%(sinv)s**.
> **Esas son las cifras de HOY, y la TAREA 1.a las publica con sus nombres.**
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni **podar la nomina** (la poda se
> decide en la auditoria integral, no aqui), ni **el trabajo de plan**, que la
> cadencia de 6.1 manda dejar fuera de una vuelta de bateria. **Y siguen fuera,
> nombradas para que la 201 no las redescubra:** la guarda de codigo del hallazgo
> `5.3` del acta 194; `acumulan()` que lea la tabla; el cotejo de clon declarado;
> las actas sin entrada propia en la serie; **QUE HACER CON LAS FILAS `B` DEL
> ARCHIVO**, que el hallazgo `5.1` del acta 199 vuelve a poner encima de la mesa; y
> **los puestos que dos o tres lectores independientes fallaron**, nombrados y
> medidos y **no resueltos, porque mover una clase es del RECOMPUTO**.
>
> **NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**. **La bateria lo mide ella sola once veces mas**,
> al entrar y al salir de cada tramo, con `guarda_y_restauracion()`.

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
- **EL DESFASE DE `PATRONES_ACTA` NO APARECE EN ESTA VUELTA, Y SE MIDE EN VEZ DE
  SUPONERSE.** `PATRONES_ACTA` pide el acta de `VUELTA - 1`, o sea la **%(ant)d**,
  y **el acta que ORDENA esta vuelta ES la %(ant)d**: el bloque `H` del sello de
  apertura conto **1 acierto para la cabecera de la 199 y 0 para la 200**. El
  `D.2` del reporte de la 184 sigue vivo como especie, y aqui **no muerde**. Lo
  que si se sigue contando, porque es cifra de inventario y envejece sola: **%(n_lit)d reportes archivados traen el literal
  `DESFASE DECLARADO`** (%(lista_lit)s), contados por `reportes_con_el_literal()`
  de este mismo fichero, **con FECHA DE CORTE %(corte)s** (banco `9.21`, TODA
  CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Un inventario que crece cada vuelta
  sin corte envejece solo.**
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
""" % dict(v=VUELTA, ant=VUELTA - 1, pisa=n_arbol, rama=rama,
           acta8=acta_hash[:8], asunto=repr(acta_asunto), head8=head_ap[:8],
           nac8=nac_hash[:8], celdas=celdas, n_ap=len(lado_apertura_roto),
           filas=filas, n_lit=len(con_literal), lista_lit=lista_literal,
           corte=corte, frase_tallador=frase_tallador, racha=racha,
           cuales=cuales_racha, vara=vara, conv=con_vara, sinv=sin_vara)

    io.open(ruta, "w", encoding="utf-8", newline="\n").write(texto)
    print("ESQUELETO ESCRITO: docs/loop/REPORTE.md (%d bytes, %d lineas por count(NL))"
          % (len(texto.encode("utf-8")), texto.count(chr(10))))
    print("   rama leida de git: %s" % rama)
    print("   acta %d leida de git log: %s  %s" % (VUELTA - 1, acta_hash[:8], acta_asunto[:70]))
    print("   HEAD de apertura leido del sello: %s" % head_ap[:8])
    print("   nacimiento del bloque de apertura, --diff-filter=A: %s" % nac_hash[:8])
    print("   reporte pisado, leido de su cabecera: vuelta %d" % n_arbol)
    print("   celdas ilegibles que el tallador imprime HOY: %s" % celdas)
    print("   racha de cierres leida del sello: %s" % racha)
    print("   las dos varas de la nomina leidas del sello: %s | %s | %s"
          % (vara, con_vara, sin_vara))
    print("   reportes con el literal del desfase: %d, corte %s"
          % (len(con_literal), corte))
