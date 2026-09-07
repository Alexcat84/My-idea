# -*- coding: utf-8 -*-
r"""vuelta202_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 202,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta201_esqueleto_reporte.py, generado de el
programaticamente con `scripts/loop/_gen_v202_esqueleto.py`. Cambia el numero de
vuelta, la lista TAREAS, este docstring y el bloque de prosa del encabezado. EL
CODIGO DE LAS FUNCIONES VA IGUAL, byte a byte, porque se copio y no se re
escribio.

POR QUE CUATRO TAREAS, Y LA CIFRA NO SE TECLEA: la racha de cierres, contada del
instrumento en el bloque `E` del sello de apertura de ESTA vuelta, vale 3, con
las vueltas 199, 200 y 201. `AUDITOR.md` 6.2 apaga el regimen temporal de dos
sub-tareas cuando DOS VUELTAS SEGUIDAS cierran su propio reporte con
`cerrar_reporte.py`, y con racha 3 SE APAGA y vuelve el tope de CINCO. El encargo
trae CUATRO. LA CIFRA SE LEE DEL SELLO, con `racha_del_sello()`, y si el sello no
la trae este esqueleto CAE EN ROJO y no escribe nada.

Y ESTA NO ES VUELTA DE BATERIA: la 200 lo fue y cerro entera, y por la cadencia
de `AUDITOR.md` 6.1 le toca a la 205. La seccion 9 cierra con el HUECO DECLARADO
Y MEDIDO por el carril de `cerrar_reporte.py`. El trabajo de esta vuelta es EL
PLAN, que es lo que la moratoria 6.3 manda.

EL DESFASE DE `PATRONES_ACTA` NO APARECE EN ESTA VUELTA, Y ESO SE MIDE EN VEZ DE
SUPONERSE: `PATRONES_ACTA` pide el acta de `VUELTA - 1`, o sea la 201, y el acta
que ORDENA esta vuelta ES la 201 (la 202 no existe todavia, y el bloque `H.2` del
sello de apertura lo cuenta: 1 acierto para la 201 y 0 para la 202). El literal
`DESFASE DECLARADO` se sigue CONTANDO de los reportes archivados, con su fecha de
corte, porque esa cifra es de inventario y envejece sola.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

USO:
  python scripts/loop/vuelta202_esqueleto_reporte.py
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
VUELTA = 202
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
    ('1', 'LA CORRECCION DECLARADA DE LA `evidencia` DE `OP-L-03`, EN SU SEDE, adjudicada por el acta 201 en su `4.3`. **EL CARRIL ES EL DE `OP-I-01` DE LA VUELTA 201**: banco `9.10`, **POR ADICION**, como **un elemento mas de la misma lista `evidencia`**, **sin clave nueva de esquema** y **sin tocar ni tachar el texto viejo**, que es la via de la gemela `OP-L-01` en la vuelta 166 que el **acta 71, seccion 6, adjudicacion 3** adjudico con las palabras **NO ES PARADA**. Tiene que decir **TRES cosas**: que el documento que la `evidencia` nombra trae **0** veces `reparto por acto` y **0** menciones de `OP-L-03`, **medidas aqui**; que el reparto por acto vive en `docs/plan/OP_L_03_LECTURAS.jsonl` y `docs/plan/OP_L_03_TRIANGULOS.jsonl`, **nombrados los dos** y con **sus bytes exactos** (`P.2`); y **la cobertura real con su fecha de corte**, porque la evidencia promete **55 pares en 29 actos** y el fichero trae otra cifra. **GUARDA OBLIGATORIA Y CORRIDA DOS VECES**, la misma que la 201 uso para `OP-I-01`. **NINGUN campo `estado` se mueve**'),
    ('2', '`OP-L-02` CONTRA EL CRITERIO DE HECHO, ahora que su clausula 1 esta medida por el acta 201 en su `4.1`. **LO PRIMERO Y SIN CLONAR NADA**: se **importan** y se corren `scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py` y `scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py`, comprobado ANTES que **ninguno escribe ficheros**, y **ninguno se toca**. Las tres clausulas se miden contra el criterio de hecho de `docs/plan/08_VERIFICACION.md` **citado por linea**, y se citan por **linea 42 mas indice**. **LA CLAUSULA 2 TRAE UNA TRAMPA YA MEDIDA** (acta 201, `4.2`): el instrumento la da `NO CUMPLIDA` porque diffea contra `46208790`, un HEAD de la vuelta 170. **Se remide contra el HEAD de apertura de ESTA vuelta**, leido del sello, y **se publican las dos lecturas juntas** con la discrepancia declarada. **NO SE ARREGLA EL INSTRUMENTO: LA MORATORIA LO PROHIBE.** Si las tres quedan cumplidas, **SE PROPONE Y NO SE CIERRA**'),
    ('3', '`OP-L-01` CONTRA EL CRITERIO DE HECHO, Y EL HUECO DE LA VIGENCIA, adjudicada por el acta 201 en su `4.8`. Sus **cuatro pruebas de cobertura** estan cubiertas y el auditor las reprodujo las cuatro, pero **eso es PRESENCIA y no CALIDAD**. Se mide contra el criterio de hecho de `docs/plan/08_VERIFICACION.md` **citado por linea**, con su `verificacion` citada por **linea 41 mas indice**. **Y SE MIDE EL HUECO QUE LA 201 NOMBRO Y NADIE HA MEDIDO**: la **TABLA VIVA DE LOS PUROS** de `docs/BANCO_DE_TEXTOS.md` (linea **938**) declara `vigente al puesto 1157` y el marcador de hoy vale otra cosa; **las dos cifras se recuentan aqui**, y se mide **cuantas filas de esa tabla siguen en pie al corte de hoy y cuantas no**, con el **resolutor delante por `P.1`** si el conteo toca ids. **SI EL HUECO PIDE MOVER UNA CLASE, NO SE MUEVE**: mover una clase es del RECOMPUTO, se nombra y se para ahi. **PROPONE, NO CIERRA**'),
    ('4', 'LOS REGISTROS. `R.63` Y `R.64`, LAS DOS MAS VIEJAS DE LA DEUDA, adjudicada por el acta 201 en su `4.9`: la deuda son **8 actas seguidas, las 173 a 180**, y se pagan **DE LA MAS VIEJA A LA MAS NUEVA, DOS POR VUELTA**. Va **DETRAS** del trabajo de plan y nunca delante. `R.63` para el **acta 173** y `R.64` para el **acta 174**, en `docs/PENDIENTES.md`. **NINGUN LECTOR NUEVO**: los que el computo necesita **se importan**, como hizo la 201. **Cada acta se acota EN ESTA VUELTA** por linea de inicio y fin, con su reparto de adjudicaciones, hallazgos, preguntas, caidas del auditor y caidas del ejecutor. **SI EL REPORTE ARCHIVADO NO EXISTE, NO SE FABRICA**: se declara la ausencia medida con `os.path.isfile` y `os.path.getsize`, y se usa la vara que el acta 201 dejo escrita en su `4.7`. **Cierra con la serie medida**: entradas, colisiones, huecos y siguiente libre'),
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
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA.** La
> 200 lo fue y cerro entera; `AUDITOR.md` 6.1 dice que la bateria corre **cada
> cinco vueltas**, en vuelta propia, y por esa cadencia **le toca a la 205**. Aqui
> la **seccion 9 cierra igual**, con el **HUECO DECLARADO Y MEDIDO** por el carril
> de `cerrar_reporte.py`, que lleva **su nombre, sus bytes medidos y su atribucion,
> las tres juntas, o no vale**. El bloque `I` del sello de apertura ya lo midio:
> **0 ficheros `SALIDA_V%(v)d_BATERIA_TRAMO_N.txt`** y
> **`docs/loop/SALIDA_V%(v)d_BATERIA.txt` NO EXISTE**.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3, decision del fundador
> del 7 sep 2026): **no se fabrican arneses, guardas ni lectores nuevos**, y **esta
> vuelta NO TIENE NINGUNA EXCEPCION**. Lo que hace falta **se importa**, y los dos
> instrumentos de `OP-L-02` se corren **sin clonarlos y sin tocarlos**. **La nomina
> queda CONGELADA EN 135**, y el bloque `F` del sello de apertura la midio contra
> ese congelado sin tocarla. **EL TRABAJO ES EL PLAN**, que es para lo que el bucle
> existe.
>
> **EL TOPE DE SUB-TAREAS ES CINCO, Y LA CIFRA QUE LO MANDA NO SE TECLEA.**
> El bloque `E` del sello de apertura de esta vuelta corrio el instrumento de la
> racha sobre el inventario ENTERO y **la racha de cierres vale %(racha)s**, con las
> vueltas **%(cuales)s**. `AUDITOR.md` 6.2 apaga el regimen temporal de dos
> sub-tareas cuando **DOS vueltas seguidas** cierran su propio reporte con
> `cerrar_reporte.py`, y con **%(racha)s** **SE APAGA**. **Este encargo trae CUATRO,
> y cabe.**
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. **El desfase de calibrado se midio
> DENTRO del bloque de apertura y ANTES de la primera operacion.** Y su bloque `F`
> publica la cifra de arneses del censo fuera de la nomina **con su vara al lado y
> las dos medidas**: con vara **%(vara)s** salen **%(conv)s** y sin vara salen
> **%(sinv)s**. **Esas son las cifras de HOY.**
>
> **LO QUE EL ACTA 201 ADJUDICO NO SE VUELVE A LEVANTAR AQUI.** Su `4.1` disuelve
> la unica parada que la 201 levanto: `OP-L-02` **si se puede medir sin decidir**,
> porque sus seis nominas viven **por id** en la constante `NOMINAS_OP_L_02`. Su
> `4.2` declara **FALSO ROJO** el `NO CUMPLIDA` de la clausula 2, porque el
> instrumento diffea contra un HEAD sellado en la vuelta 170. Y su `4.4` fija la
> convencion: **la coordenada de una ficha JSONL es LINEA MAS INDICE**, y aqui se
> usa **publicando las dos numeraciones del indice** para que ninguna cita quede
> ambigua.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni **podar la nomina**, ni **mover
> un solo campo `estado`** (la vara del trabajo pendiente es
> `scripts/loop/vuelta150_3_relectura_expediente.py`, nunca el campo, por el
> recuadro de `AUDITOR.md` 0), ni **cerrar ninguna ficha por cuenta del ejecutor**:
> lo que estas tareas producen es **lectura medida**, y si de ella sale que una
> ficha esta cumplida, **se propone con su evidencia y lo adjudica el auditor**. **Y
> siguen fuera, nombradas para que la 203 no las redescubra:** la **reparacion del
> HEAD envejecido** de `vuelta170_tarea5b_veredicto_op_l_02.py`; el **cierre del
> turno del auditor que se reabre despues de declarar las clases**; los **dos
> arneses que el censo ve y la nomina congelada no tiene**
> (`vuelta197_tarea2_mutacion_orden_del_turno.py` y
> `vuelta199_tarea1_mutacion_guardas_revividas.py`); **las dos paradas que levanto
> la 200**; y **QUE HACER CON LAS FILAS `B` DEL ARCHIVO**. **Las tres primeras son
> de codigo y van a la auditoria integral: la moratoria las prohibe hoy.**
>
> **NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor,
> y **las dos convenciones se publican**. **Y no se toca `dataset/` a mano**: el
> `numstat` de `dataset/`, `web/`, `engine/` y `docs/plan/` se mide al entrar y al
> salir y **las dos cifras se publican**.

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
  apertura conto **1 acierto para la cabecera de la %(ant)d y 0 para la %(v)d**. El
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

## 1. LAS CUATRO TAREAS DEL ENCARGO, Y SU ESTADO

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
