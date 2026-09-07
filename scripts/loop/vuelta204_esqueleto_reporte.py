# -*- coding: utf-8 -*-
r"""vuelta204_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 204,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta203_esqueleto_reporte.py, generado de el
programaticamente con `scripts/loop/_gen_v204_esqueleto.py`. Cambia el numero de
vuelta, la lista TAREAS, este docstring y el bloque de prosa del encabezado. EL
CODIGO DE LAS FUNCIONES VA IGUAL, byte a byte, porque se copio y no se re
escribio.

POR QUE CUATRO TAREAS, Y LA CIFRA NO SE TECLEA: la racha de cierres, contada del
instrumento en el bloque `E` del sello de apertura de ESTA vuelta, vale 5, con
las vueltas 199, 200, 201, 202 y 203. `AUDITOR.md` 6.2 apaga el regimen temporal
de dos sub-tareas cuando DOS VUELTAS SEGUIDAS cierran su propio reporte con
`cerrar_reporte.py`, y con racha 5 SE APAGA y vuelve el tope de CINCO. El encargo
trae CUATRO mas la TAREA 0, que es un remedio de gobierno y no trabajo de plan.
LA CIFRA SE LEE DEL SELLO, con `racha_del_sello()`, y si el sello no la trae este
esqueleto CAE EN ROJO y no escribe nada.

Y ESTA NO ES VUELTA DE BATERIA: la 200 lo fue y cerro entera, y por la cadencia
de `AUDITOR.md` 6.1 le toca a la 205. La seccion 9 cierra con el HUECO DECLARADO
Y MEDIDO por el carril de `cerrar_reporte.py`. El trabajo de esta vuelta es EL
PLAN, que es lo que la moratoria 6.3 manda.

EL DESFASE DE `PATRONES_ACTA` NO APARECE EN ESTA VUELTA, Y ESO SE MIDE EN VEZ DE
SUPONERSE: `PATRONES_ACTA` pide el acta de `VUELTA - 1`, o sea la 203, y el acta
que ORDENA esta vuelta ES la 203. El literal `DESFASE DECLARADO` se sigue
CONTANDO de los reportes archivados, con su fecha de corte, porque esa cifra es
de inventario y envejece sola.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

USO:
  python scripts/loop/vuelta204_esqueleto_reporte.py
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
VUELTA = 204
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
    ('1', 'LOS REGISTROS. `R.67` PARA EL ACTA 177 Y `R.68` PARA EL ACTA 178, las dos siguientes de la deuda por el `4.9` del acta 201, y va PRIMERA porque `AUDITOR.md` 1.4 pone los registros en la TAREA 1. **LA DEUDA SE REMIDE AQUI Y NO SE COPIA DEL ENCARGO**: se cuenta cuantas actas de la 177 a la 180 siguen sin registro. **DE QUE CONVENCION SON SE COMPRUEBA, NO SE SUPONE**: la 184 es la frontera, y si un acta ya escribe sus claves con comillas inversas **el lector heredado basta y se dice**. **EL COMPUTO DE LA 203 SE REUTILIZA**, `scripts/loop/_v203_reparto_de_actas_viejas.py`, clonado a un `_v204_*` **con su cifra de `difflib` al lado**, y no se escribe un tercero. **CADA ACTA SE ACOTA EN ESTA VUELTA** por linea de inicio y de fin, con **el reparto entero y cada numeral con la seccion de la que sale nombrada por su TITULO**. **UN NUMERAL NO COMPUTABLE SE DECLARA EN VEZ DE PUBLICAR UN CERO**, con **las tres lecturas** cuando discrepen, porque un cero de convencion no es un cero de ausencia. **SE COTEJA CONTRA LA FILA DE METRICA DE CADA ACTA**, que la escribio el auditor de aquella vuelta y no el ejecutor. **CIERRA CON LA SERIE MEDIDA** por `scripts/loop/serie_de_registros.py` y **no con una expresion regular propia**. **GUARDA OBLIGATORIA Y CORRIDA DOS VECES**, con **crecimiento 0** la segunda'),
    ('2', 'EL TAMANO DEL AGUJERO DE `cobertura`, MEDIDO Y NO TAPADO. Adjudicado en el `4.3` del acta 203: **`OP-I-01` no se cierra** porque sus clausulas **2** y **3** no se caerian si el fallo volviera, ya que `cobertura` es texto libre. **ESTA TAREA NO CIERRA LA FICHA Y NO ESCRIBE LA VARA**: la vara es codigo permanente y va a la auditoria integral por el `4.7`. Lo que se pide es **medir de que tamano es el agujero**, para que quien escriba la vara despues sepa contra que. **CUANTAS FORMAS DISTINTAS toma hoy el campo `cobertura`** en las entradas de `docs/plan/INVENTARIO.jsonl` (**la cifra de entradas se RECUENTA**), **agrupadas por su forma**, y **cuantas quedarian fuera de cualquier vara razonable**. **LA BUSQUEDA ES POSITIVA Y NUNCA NEGATIVA** (`EJECUTOR.md` 9) y **SE DECLARA SOBRE QUE CAMPO CORRE CADA UNA**, que es la `C.2` del acta 203: la misma variante da cifras distintas sobre el campo y sobre el fichero entero, y **una vara sin declarar convierte una medicion buena en una acusacion**. **SE MIDE LO MISMO PARA LA CLAUSULA 3**, la de los huecos nombrados, que comparte el agujero. **PROPONE, NO CIERRA**, y **no toca el `estado`**'),
    ('3', 'LA DISCREPANCIA DE COMPONENTES QUE EL PROPIO INSTRUMENTO DECLARA. La 203 la reprodujo y no la persiguio, y lo dijo. **SE MIDE DE DONDE SALE LA DIFERENCIA**, con el resolutor delante, y **se declara**: cuantas componentes del sellado no estan hoy, cuantas hay hoy que no estaban, y **si la causa es el universo, la fecha o el instrumento**. **LA NOMINA SELLADA NO SE REGENERA**: `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` **se CUENTA, no se reescribe**. **EL INSTRUMENTO ESCRIBE SOBRE UNA SEDE SELLADA EN LA 169**, asi que va con **protocolo del sello**: se mide antes, se corre, se restaura con `git checkout --` y se REMIDE. **SUS DOS TAMANOS DISCREPAN POR EL CRLF** y eso es el `PD.2`: **se publica, no se resuelve**. **SI DE AQUI SALE QUE UNA CIFRA PUBLICADA ENVEJECIO**, va por el carril del banco `9.10`, **POR ADICION Y EN SU SEDE**, con el texto viejo entero y sin tachar. **SI SALE QUE HACE FALTA CODIGO, SE PARA Y SE TRAE**'),
    ('4', 'EL CENSO DE LO QUE QUEDA DEL PLAN, MEDIDO Y NO NARRADO. Las cuatro fichas reales estan medidas y **ninguna se cerro**, y la moratoria `6.3` dice que el trabajo es el plan hasta agotarlo: **ese tramo esta agotado y la pregunta que nadie ha contestado con una cifra es QUE QUEDA**. **SE CUENTAN LAS FICHAS DE `docs/plan/OPERACIONES.jsonl` POR `estado`** (la cifra se RECUENTA) **y se cruza esa cuenta con la vara del trabajo pendiente**, `scripts/loop/vuelta150_3_relectura_expediente.py --corte <HEAD de apertura>`, **que nunca es el campo `estado`** (`AUDITOR.md` 0) y **a la que se le pasa un COMMIT y no una fecha**. **LAS DOS LECTURAS SE PUBLICAN JUNTAS Y LA DISCREPANCIA SE DECLARA**: ese cruce es el punto, no la suma. **SE NOMBRAN UNA A UNA LAS CONGELADAS EN SILENCIO Y LA `HECHA` SIN NINGUNA PRUEBA**, que son las que nadie ha mirado nunca y el candidato natural al trabajo de la 205. **NINGUNA FICHA SE CIERRA Y NINGUN `estado` SE MUEVE**: lo que esta tarea produce es **el mapa de lo que queda**, para que el fundador decida el orden'),
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
> **LA TAREA 0 DEL ENCARGO ES BLOQUEANTE Y NO TIENE FILA EN LA TABLA, PORQUE NO ES
> TRABAJO SINO UNA PROHIBICION**: `docs/loop/PROMPT_SIGUIENTE.md`,
> `docs/loop/ACTA_AUDITOR.md` y `docs/loop/PARA_ALEXIS.md` **son sede del auditor**,
> y el ejecutor **no las escribe, no las reescribe, no las borra y no las
> reordena**. La 203 se escribio a si misma su encargo siguiente y con eso **borro
> la prueba de que se le mando**. **Aqui se obedece midiendo**: el bloque `C.1` del
> sello de apertura midio las tres **contra el HEAD de apertura**, y la seccion 4
> las vuelve a medir **al cierre**. **Lo que esta sesion propone para la vuelta
> siguiente vive en su propia seccion del reporte, que es su sede.** **Proponer es
> del ejecutor. Encargar es del auditor.**
>
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA.** La
> 200 lo fue y cerro entera; `AUDITOR.md` 6.1 dice que la bateria corre **cada
> cinco vueltas**, en vuelta propia, y por esa cadencia **le toca a la 205**. Aqui
> la **seccion 9 cierra igual**, con el **HUECO DECLARADO Y MEDIDO** por el carril
> de `cerrar_reporte.py`, que lleva **su nombre, sus bytes medidos y su atribucion,
> las tres juntas, o no vale**, y **distinguiendo si el cero sale de que no hay
> fichero o de medir uno vacio**. El bloque `I` del sello de apertura ya lo midio:
> **0 ficheros `SALIDA_V%(v)d_BATERIA_TRAMO_N.txt`** y
> **`docs/loop/SALIDA_V%(v)d_BATERIA.txt` NO EXISTE**, o sea que **el cero es de
> ausencia de fichero y no de fichero vacio**.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3, decision del fundador
> del 7 sep 2026), **con su linea exacta ya adjudicada dos veces, asi que aqui no
> se vuelve a discutir**: el `4.5` del acta 199 y el `4.6` del acta 203 dicen que
> la moratoria prohibe **arneses, guardas y lectores QUE SE QUEDEN VIGILANDO**, y
> que **un computo de una vuelta que muere con ella no es eso, aunque traiga una
> lectura que no existia**. Por eso todo lo que esta vuelta escribe son ficheros
> `_v204_*` **con prefijo de guion bajo, fuera del censo y fuera de la nomina**, y
> los lectores que hacen falta **se IMPORTAN o se clonan con su cifra de `difflib`
> al lado**. **La nomina queda CONGELADA EN 135**, y el bloque `F` del sello de
> apertura la midio contra ese congelado sin tocarla. **EL TRABAJO ES EL PLAN**,
> que es para lo que el bucle existe.
>
> **EL TOPE DE SUB-TAREAS ES CINCO, Y LA CIFRA QUE LO MANDA NO SE TECLEA.**
> El bloque `E` del sello de apertura de esta vuelta corrio el instrumento de la
> racha sobre el inventario ENTERO y **la racha de cierres vale %(racha)s**, con las
> vueltas **%(cuales)s**. `AUDITOR.md` 6.2 apaga el regimen temporal de dos
> sub-tareas cuando **DOS vueltas seguidas** cierran su propio reporte con
> `cerrar_reporte.py`, y con **%(racha)s** **SE APAGA**. **Este encargo trae CUATRO
> mas la TAREA 0, y cabe.** **Y ese mismo bloque corrio el instrumento de la racha
> COMPROBANDO ANTES SI ESCRIBE**, que es lo que el encargo pide expresamente: **SI
> ESCRIBE**, pisa su propia salida sellada, asi que se midio antes, se corrio, y la
> sellada se **RESTAURO con `git checkout --` y se REMIDIO IDENTICA**.
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. **El desfase de calibrado se midio
> DENTRO del bloque de apertura y ANTES de la primera operacion.** Y su bloque `F`
> publica la cifra de arneses del censo fuera de la nomina **con su vara al lado y
> las dos medidas**: con vara **%(vara)s** salen **%(conv)s** y sin vara salen
> **%(sinv)s**. **Esas son las cifras de HOY.**
>
> **LO QUE EL ACTA 203 ADJUDICO NO SE VUELVE A LEVANTAR AQUI.** Su `4.3` deja
> **`OP-I-01` SIN CERRAR**, porque sus clausulas **2** y **3** no se caerian si el
> fallo volviera (`cobertura` es texto libre) y la **4** se cae solo en la parte
> que recomputa: **aqui no se levanta y no se le toca el `estado`**. Su `4.4` deja
> contestado que el parametro opcional de `vuelta184_tarea1a_registrar_acta184.py`
> **no roza la moratoria**. Su `4.6` fija que **un computo `_v204_*` puede traer una
> lectura nueva**. Su `4.8` dice que **un reporte archivado que existe pero no
> titula seccion de preguntas se trata como el que no existe, DECLARANDOLO**. Y la
> **vara de las actas anteriores a la 184** sigue siendo la del `4.1` del acta 202:
> **el numeral se toma de la seccion cuyo PROPIO TITULO lo nombra, nunca del numero
> de seccion**, y las claves se cuentan por su numeracion `N.M`, **lleve o no
> comillas inversas**, y **la entrada declara que uso esa vara**. **`OP-L-01` y
> `OP-L-02` tampoco se cierran** (actas 202 `4.3` y `4.4`) y **sus correcciones ya
> estan escritas: no se repiten.**
>
> **LA CIFRA QUE EL ACTA 202 MIDIO EN SU `5.2` Y AQUI SE OBEDECE:** el inventario de
> salidas **se mide a si mismo y envejece dentro de la propia vuelta**. Esa media
> linea va escrita en el bloque `J` del sello de apertura: **junto al corte se
> declaran los ficheros que nacen despues de medirlo**, con sus nombres, y **el
> cierre remide la cifra en vez de heredarla** (banco `9.21`).
>
> **LAS DOS CIFRAS QUE LA 203 APRENDIO EN ROJO Y AQUI SE OBEDECEN DE ENTRADA:**
> **(a)** una pareja de bytes completa **puede ser FALSA** si se le pega a una ruta
> el tamano que tenia **en mitad de la vuelta**, asi que **detras de cada ruta va SU
> tamano al cierre** y el intermedio se dice **sin nombrar la ruta**; **(b)** el
> markdown **parte la frase donde le cabe el ancho**, asi que **cada cifra va junto
> a su pareja en el MISMO renglon**.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni **podar la nomina**, ni **mover
> un solo campo `estado`** (la vara del trabajo pendiente es
> `scripts/loop/vuelta150_3_relectura_expediente.py`, nunca el campo, por el
> recuadro de `AUDITOR.md` 0), ni **mover una clase ni un veredicto**, ni **cerrar
> ninguna ficha por cuenta del ejecutor**: lo que estas tareas producen es **lectura
> medida**, y si de ella sale que una ficha esta cumplida, **se propone con su
> evidencia y lo adjudica el auditor**. **Y siguen fuera, nombradas para que la 205
> no las redescubra:** la **operacion de codigo de la escalada** (acta 202, `4.6`,
> ratificada en el `4.9` del acta 203), **encargada y con su ejecucion SUSPENDIDA**
> hasta la primera vuelta despues de que la moratoria se levante; la **vara escrita
> para `cobertura`** (acta 203, `4.7`); la **reparacion del HEAD envejecido** de
> `vuelta170_tarea5b_veredicto_op_l_02.py`; el **cierre del turno del auditor que se
> reabre despues de declarar las clases**; que **`aislador_de_ciega.py` pueda servir
> un par cuyo nodo ya murio** (acta 203, `5.3`); los **dos arneses que el censo ve y
> la nomina congelada no tiene**; **anadir `docs/PENDIENTES.md` como quinta sede de
> cifra publicada**; y **QUE HACER CON LAS FILAS `B` DEL ARCHIVO**. **Las de codigo
> van a la auditoria integral: la moratoria las prohibe hoy.**
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
