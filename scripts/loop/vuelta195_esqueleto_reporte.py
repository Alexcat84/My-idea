# -*- coding: utf-8 -*-
r"""vuelta195_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 195,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta194_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS (que sube de TRES filas a CUATRO), este docstring y el
bloque de prosa del encabezado, porque ESTA VUELTA NO ES DE BATERIA.

Y LA SECCION 8.1 DE LA FUENTE SE LEYO ANTES DE CLONAR, que es lo que su propia
`C.3` reclamaba: un clon declarado hereda tambien los defectos declarados de su
fuente. Los dos defectos que aquella seccion nombra viven en el BLOQUE DE
APERTURA y no aqui, y estan arreglados en scripts/loop/vuelta195_apertura.py.

ESTA VUELTA NO ES DE BATERIA (AUDITOR.md 6.1, decision del fundador del 5 sep
2026): la bateria corre CADA CINCO VUELTAS en una vuelta propia QUE NO LLEVA NADA
MAS, la 194 la corrio entera por sus diez tramos y la proxima cae en la 199. Su
seccion 9 cierra con EL HUECO DECLARADO Y MEDIDO por el carril de la TAREA 1.b de
la vuelta 173, con su medicion, su atribucion y su corrida.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 195 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V195_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada.

EL DESFASE DE PATRONES_ACTA NO SE REPARA AQUI, Y ES DECISION DEL AUDITOR Y NO UN
OLVIDO MIO: apunta al acta de VUELTA - 1 y el acta que ORDENA esta vuelta es la
195. El encargo de la 195 lo pasa EXPRESAMENTE a la 196 y EN PRIMER LUGAR DE LA
COLA, con su motivo escrito: las cuatro sub-tareas de hoy atacan causas y esta es
cosmetica de cabecera. LA CIFRA DEL ORDINAL SIGUE LLEVANDO SU FECHA DE CORTE, por
banco 9.21.

USO:
  python scripts/loop/vuelta195_esqueleto_reporte.py
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
VUELTA = 195
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
    ("1", 'LOS REGISTROS. BLOQUEANTE. El acta 195 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado. La entrada registra, y cada cifra se cuenta del cuerpo acotado del acta: LAS DIEZ ADJUDICACIONES `4.1` a `4.10`, y LAS DIEZ A FAVOR (siete son los discutibles `D.1` a `D.7` del reporte de la 194 y las tres restantes son las preguntas `P.1`, `P.2` y `P.3`, dos contestadas por extension citable con la cita comprobada contra su fichero), CERO EN CONTRA y es la QUINTA acta seguida; LOS TRES HALLAZGOS DE LA SECCION 5 que no salen de ningun discutible (`5.1` la fila de credito del acta 194 que rotula mal su cifra, `5.2` el rojo de la bateria que SI es reparable, `5.3` `--componer` que publica VERDE sobre diez tramos rojos); CERO CAIDAS DEL EJECUTOR EN LA VUELTA 194, de cifra publicada y de reporte, con LA RACHA DE REPORTE VUELTA A CERO desde el 1 que dejo el acta 194, y SIN ESCALADA QUE ENCARGAR, dicho expresamente para que no se lea como olvido; UNA CAIDA PROPIA DEL AUDITOR, `C.1`, DE METODO (leer `clase` y `razon` del archivo con `json` a mano en vez de por `AP.marcador()` y `AP.leer_veredictos()`, que es la cuarta puerta y ya ofrecia las dos cosas sin coste), con el sujeto NO quemado y probado DESPUES por la propia puerta: 30 de 30 sellados vuelven TAPADOS y 0 destapes apuntados; LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de puestos (30 aislados, 30 cotejados, CERO QUEMADOS, que es la diferencia con la 194 y se debe a que los mensajes de commit del ejecutor ya no publican clases por puesto: ESO FUNCIONO); y LA FILA DE CAIDAS PROPIAS PARTIDA EN DOS, las que ACUMULAN y el total del cuerpo, que es el remedio del hallazgo `5.1` aplicado por el auditor a su propia tabla. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se prueba re corriendolo, con la sede medida en bytes antes y despues'),
    ("2", 'LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. BLOQUEANTE, Y ES DEUDA SUYA QUE PAGA EL EJECUTOR CON EL INSTRUMENTO. `AUDITOR.md` 1.2: dos discrepancias del auditor cayeron FUERA de su marcado, `654` y `719`, asi que EL CREDITO DE SU TANDA BAJA Y EL TRAMO SE RELEE AL DOBLE. El tramo y el doble estan CERRADOS DESDE ANTES, computados y no tecleados, en `docs/loop/_auditor_v195_doble_para_la_196.txt`, para que no se elijan despues de mirar. (a) `vecinos()` SE IMPORTA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y NO se copia, con `evitar` cargado de TODO lo consumido y contado de sus ficheros; el solape con el tramo y con el universo tiene que salir CERO POR CONSTRUCCION, no por suerte. (b) LEER LOS 60 A CIEGAS, tramo y doble, con `aislador_de_ciega.py`, y escribir las clases ANTES de abrir el destape. (c) LA VARA ES `docs/BANCO_DE_TEXTOS.md` `9.6.1`, citada por numero y no parafraseada, Y CON EL ERROR DEL AUDITOR PUESTO: la vara de contenido-manda es EL SUELO, NO EL TECHO, y antes de aplicarla se pregunta si el par pertenece a una familia con REGLA PROPIA ya fijada, porque entonces manda la especifica (el `719` se perdio por no preguntarlo: hay regla fijada en el puesto `595` con el `580` de precedente vivo). (d) NO SALTARSE LA `B`: el auditor emitio CERO `B` en 30 pares y el archivo tenia una, el `654`. (e) PUBLICAR EL COTEJO con sus cifras (cuantos coinciden, cuantos discrepan, y cuales caen dentro y fuera del marcado), con los discutibles marcados ANTES de saber si se acierta'),
    ("3", 'EL ROJO DE LA BATERIA, ATACADO EN SU CAUSA. Es el hallazgo `5.2` del acta 195 y la adjudicacion de la pregunta `P.2` del reporte de la 194. LO RESERVADO AL FUNDADOR ES PODAR LA NOMINA, NO HACERLA CRECER: la opcion `c` que rechazo el 5 sep 2026 era JUBILAR ARNESES VIEJOS, que es lo contrario de anadir, y el NO TOQUES LA NOMINA de los encargos anteriores se escribio para VUELTAS DE BATERIA y contra LA PODA. (a) LOS SEIS QUE EL CENSO VE Y LA NOMINA NO TIENE ENTRAN EN LA NOMINA, cada uno CON SU SUJETO CONGELADO y cotejado contra su blob de git, RECONTADOS del instrumento al empezar. (b) EL QUE NO PUEDA TENER SUJETO CONGELADO ENTRA COMO CASO DECLARADO, con su marca. (c) LAS TRES ENTRADAS SIN SUJETO CONGELADO que ya estan dentro (`vuelta186_tarea2c_mutacion_cierre_tardio.py`, `vuelta187_tarea4_mutacion_dos_convenciones.py`, `vuelta188_tarea4_mutacion_cobertura_parejas.py`, las tres ancladas a `REPORTE.md` VIVO) se resuelven POR LA MISMA REGLA: o se les congela el sujeto, o pasan a CASO DECLARADO con su marca. (d) `vuelta172_tarea5_mutacion_cierre.py` NO MUERDE desde la 189: se arregla para que caiga cuando tiene que caer, o se declara rota con su motivo medido. (e) NO SE PODA NADA: la nomina solo crece. (f) AL CERRAR, LA BATERIA SOLO SOBRE LO QUE SE TOCO, para comprobar que el rojo atacado se apago, PUBLICANDO LA CIFRA de arneses fuera de la nomina y de entradas sin sujeto congelado, y NO la bateria entera, que no es su vuelta. (g) CON SU CASO POSITIVO POR MUTACION, que pruebe lo que falla hoy: que la mirada de la nomina sobre si misma CAIGA cuando un arnes que el censo ve se queda fuera de la nomina sin ser caso declarado'),
    ("4", '`--componer` DEJA DE PUBLICAR VERDE SOBRE DIEZ ROJOS. Es el hallazgo `5.3` del acta 195 y la otra mitad de la pregunta `P.3` del reporte de la 194: `SALIDA_V194_BATERIA_COMPUESTA.txt` termina en VERDE, los 10 tramos cubren la nomina entera, con exitcode 0, mientras los diez tramos traen `CLASE DEL VEREDICTO: ROJO POR FALLO` y exitcode 1. Es cierto EN LO QUE MIDE, la cobertura, y enganoso EN LO QUE PARECE DECIR, el estado de la bateria; banco `9.1`, el instrumento debe caerse en vez de mentir. (a) `--componer` PROPAGA EL PEOR VEREDICTO DE LOS TRAMOS a su propio exitcode y a su linea final: cobertura entera y algun tramo en rojo NO es VERDE. (b) LAS DOS COSAS SE SIGUEN DICIENDO POR SEPARADO, la cobertura con su cifra y el veredicto con la suya, porque que propague el rojo no puede borrar que la cobertura estaba completa. (c) CON SU CASO POSITIVO POR MUTACION, con la salida de la 194 de sujeto congelado, que es el caso real: diez tramos rojos con cobertura 127 de 127 tienen que dar ROJO'),
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
    vuelta 193 se publica CON SU FECHA DE CORTE (banco 9.21). La caida 5.5 del
    reporte de la 192 fue exactamente una cifra de este inventario publicada sin
    corte y contradiciendo a su propia seccion 0."""
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
> **ESTA NO ES VUELTA DE BATERIA.** `AUDITOR.md` 6.1, decision del fundador del 5
> sep 2026: la bateria corre **CADA CINCO VUELTAS** en una vuelta propia **que no
> lleva nada mas**, **la 194 la corrio entera por sus diez tramos** y **la proxima
> cae en la 199**. **La seccion 9 de este reporte cierra con el HUECO DECLARADO Y
> MEDIDO** por el carril de la TAREA 1.b de la vuelta 173, con su medicion, su
> atribucion y su corrida. **Un hueco declarado no es un hueco escondido.**
>
> **VAN CUATRO SUB-TAREAS Y DOS SON BLOQUEANTES.** El tope de CINCO esta ganado y
> **la cifra se conto del instrumento en esta vuelta**, no se heredo: el bloque `E`
> del sello de apertura corrio `scripts/loop/vuelta%(ant2)d_racha_de_cierres.py`
> sobre el inventario ENTERO. `AUDITOR.md` 6.2 pedia DOS vueltas seguidas cerrando
> su propio reporte con `cerrar_reporte.py`.
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. Esas eran las dos caidas `C.1` y
> `C.2` que el reporte de la 194 se declaro en su seccion 8.1, heredadas dos
> vueltas seguidas por clonar el bloque sin leer esa seccion, que es lo que su
> propia `C.3` nombraba como causa. **Aqui se leyo la seccion 8.1 ANTES de clonar.**
> **El desfase de calibrado se midio DENTRO del bloque de apertura y ANTES de la
> primera operacion.**
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina**, ni **la bateria entera**, que no es su
> vuelta y cae en la 199. **Y siguen fuera, nombradas para que la 196 no las
> redescubra:** el desfase de `PATRONES_ACTA`, **que el encargo de la 195 pasa
> EXPRESAMENTE a la 196 y EN PRIMER LUGAR DE LA COLA**, con su motivo dicho (las
> cuatro de hoy atacan causas y esa es cosmetica de cabecera); la fila de credito
> del acta con su rotulo arreglado **en el instrumento que la talla**; la guarda de
> codigo del hallazgo `5.3` del acta 194 (mensajes de commit sin clases por puesto
> ni reparto de ciega), **que a mano YA FUNCIONA Y ESTA MEDIDO** y cuya guarda
> durable sigue pendiente; `acumulan()` que lea la tabla o que declare en su salida
> que no es la sede; el cotejo de clon declarado que separa sentencia de codigo de
> cambio de texto; la excepcion que publica siempre su lista; la medicion del censo
> de arneses con carril de mutacion sin fichero propio; las ocho actas sin entrada
> propia en la serie (173 a 180), medidas y no arregladas; que el campo `evidencia`
> de `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE MUEVE: sigue
> en `LISTA`**; y **QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO**, nombrado y medido
> y **no resuelto, porque mover una clase es del RECOMPUTO**.
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**.

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
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA, Y LLEVA SU FECHA DE CORTE.** La
  linea de arriba nombra el acta **%(ant)d** porque `PATRONES_ACTA` pide la de
  `VUELTA - 1`, y **el acta que ORDENA esta vuelta es la %(v)d**. Es el `D.2` del
  reporte de la 184, adjudicado a favor con reparacion encargada por la `5.2` del
  acta 185, **y el encargo de esta vuelta lo pasa EXPRESAMENTE a la 196 y EN
  PRIMER LUGAR DE LA COLA**, con su motivo dicho. Lo que si se puede
  contar: **%(n_lit)d reportes archivados traen el literal `DESFASE DECLARADO`**
  (%(lista_lit)s), contados por `reportes_con_el_literal()` de este mismo fichero,
  **con FECHA DE CORTE %(corte)s** (banco `9.21`, TODA CIFRA DE CRUCE LLEVA SU
  FECHA DE CORTE). **Un inventario que crece cada vuelta sin corte envejece solo.**
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
""" % dict(v=VUELTA, ant=VUELTA - 1, ant2=VUELTA - 2, pisa=n_arbol, rama=rama,
           acta8=acta_hash[:8], asunto=repr(acta_asunto), head8=head_ap[:8],
           nac8=nac_hash[:8], celdas=celdas, n_ap=len(lado_apertura_roto),
           filas=filas, n_lit=len(con_literal), lista_lit=lista_literal,
           corte=corte, frase_tallador=frase_tallador)

    io.open(ruta, "w", encoding="utf-8", newline="\n").write(texto)
    print("ESQUELETO ESCRITO: docs/loop/REPORTE.md (%d bytes, %d lineas por count(NL))"
          % (len(texto.encode("utf-8")), texto.count(chr(10))))
    print("   rama leida de git: %s" % rama)
    print("   acta %d leida de git log: %s  %s" % (VUELTA - 1, acta_hash[:8], acta_asunto[:70]))
    print("   HEAD de apertura leido del sello: %s" % head_ap[:8])
    print("   nacimiento del bloque de apertura, --diff-filter=A: %s" % nac_hash[:8])
    print("   reporte pisado, leido de su cabecera: vuelta %d" % n_arbol)
    print("   celdas ilegibles que el tallador imprime HOY: %s" % celdas)
    print("   reportes con el literal del desfase: %d, corte %s"
          % (len(con_literal), corte))
