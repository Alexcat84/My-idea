# -*- coding: utf-8 -*-
r"""vuelta193_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 193,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta192_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS, este docstring, el bloque de prosa del encabezado y
LA FECHA DE CORTE DE LA CIFRA DEL ORDINAL DEL DESFASE, que es lo que el acta 193
encarga arreglar en su lista de lo que sigue fuera.

ESTA VUELTA NO ES DE BATERIA (AUDITOR.md 6.1) PERO ES LA ULTIMA ANTES: la 189 la
corrio entera y la siguiente cae en la 194. Su seccion 9 cierra con el HUECO
DECLARADO Y MEDIDO por el carril de cerrar_reporte.py, con su nombre, sus bytes
medidos y su atribucion, LAS TRES JUNTAS.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 193 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V193_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada.

EL DESFASE DE PATRONES_ACTA NO SE REPARA AQUI, y el acta 193 lo deja expresamente
DESPUES de la bateria de la 194 porque toca tallar_cabecera_reporte.py, que
CUATRO entradas de la nomina nombran. LO QUE SI SE ARREGLA EN ESTA VUELTA ES QUE
LA CIFRA DEL ORDINAL LLEVE SU FECHA DE CORTE, por banco 9.21 (TODA CIFRA DE CRUCE
LLEVA SU FECHA DE CORTE): la caida 5.5 del reporte de la 192 fue publicar 3 donde
su propia seccion 0 decia 4, y una cifra de inventario sin corte envejece sola.

USO:
  python scripts/loop/vuelta193_esqueleto_reporte.py
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
VUELTA = 193
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
    ("1", 'LOS REGISTROS. BLOQUEANTE. El acta 193 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado. Registra LAS DIEZ ADJUDICACIONES `4.1` a `4.10`, las diez A FAVOR (siete son los discutibles `D.1` a `D.7` del reporte de la 192 y las tres restantes son las preguntas `P.1`, `P.2` y `P.3` contestadas), OTRA VEZ CERO EN CONTRA; LOS CUATRO HALLAZGOS DE LA SECCION 5 que no salen de ningun discutible (`5.1` la cuarta puerta que no se puede usar desde el CLI, `5.2` el cotejo que convierte `"no"` en `si`, `5.3` el arnes que imprime su `mkdtemp` en la salida sellada, `5.4` el reporte que se contradice en la cuenta del `DESFASE DECLARADO`); UNA CAIDA DEL EJECUTOR, DE REPORTE, QUE NO ACUMULA (la seccion 5.5 publica 3 donde hay 4 y donde su propia seccion 0 dice 4: se registra con su nombre, dispara la relectura al doble y NO acumula por la letra del 27 ago 2026, RACHA DE REPORTE 0); UNA CAIDA PROPIA DEL AUDITOR, DE METODO (`C.1`, correr `run_phase1.py` sin `--reaplico-curaduria` y ensuciar `dataset/`); y LA METRICA DE CREDITO de la seccion 7 con la fila de puestos y su nota: 30 aislados y 30 cotejados, CERO quemados, SOLAPE TOTAL a proposito, o sea control y no cobertura nueva. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se prueba re corriendolo, con la sede medida en bytes antes y despues'),
    ("2", 'LOS TRES ARNESES QUE NO REPRODUCEN, ANTES DE LA BATERIA DE LA 194. BLOQUEANTE Y LA MAS URGENTE DE LA VUELTA. Es la adjudicacion `4.10` y el hallazgo `5.3` del acta 193, medido en `docs/loop/_auditor_v193_reproducibilidad.txt`: los tres REPRODUCEN entre dos corridas de hoy y NINGUNO contra su sellada. (a) LOS DOS PRIMEROS (`vuelta191_tarea3_mutacion_lineas.py` y `vuelta191_tarea6_mutacion_bloque_tallado.py`): CONGELAR SU SUJETO o DECLARAR EL CASO por el carril de los `CASO DECLARADO`, porque la `4.4` del acta 191 dice que `SUJETO VIVO` es FALLO y no deuda y la `4.10` cierra la salida que quedaba: una salida que no reproduce NO ES DEL MISMO CALIBRE, tenga o no tenga motivo escrito. (b) EL TERCERO (`guarda_de_entrada_a_la_nomina.py`): que su salida sellada NO lleve el nombre del directorio temporal; el directorio se sigue fabricando y se sigue retirando (`P.16`). (c) ARREGLAR LA GUARDA QUE NO LO VIO: `tempfile` y `mkdtemp` cuentan como huellas de CONGELADO y por eso da CONGELADO a un arnes cuya salida cambia en cada corrida; UNA HUELLA DE TEXTO NO PRUEBA REPRODUCCION. (d) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un arnes cuya salida no reproduce vuelve a salir CONGELADO. (e) NO SE TOCA LA NOMINA: la opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue rechazada. (f) AL CERRAR, CORRER LOS TRES DOS VECES Y PUBLICAR SUS BYTES Y SUS `sha256`; si alguno sigue sin reproducir, SE PARA Y SE TRAE'),
    ("3", 'LA VARA DE LAS CIEGAS PASA A SER LA DEL BANCO, Y EL DOBLE SE LEE CON ELLA. Es la adjudicacion `4.9` del acta 193, que contesta la `P.3` a favor. No es doctrina nueva: la vara ya esta escrita en `docs/BANCO_DE_TEXTOS.md` `9.6.1`, LA VARA DE LA RAMA CONTENIDO-MANDA: LA LINEA O EL PROCEDIMIENTO, propuesta y adoptada el 12 ago 2026. (a) ESCRIBIR EL CRITERIO DE LA CIEGA CITANDO `9.6.1` POR NUMERO, con la frase de la vara copiada LITERAL y no parafraseada (`9.5.0`), y que sea el criterio que se le pasa a `aislador_de_ciega.py` de aqui en adelante. (b) LA RELECTURA AL DOBLE DEL TRAMO DE LA 192, que es la deuda de credito de la tanda del auditor y la encarga el auditor, que es donde `AUDITOR.md` 1.2 la pone, CON MOTIVO TRIPLE: dos discrepancias cayeron fuera del marcado del auditor, las dos cayeron tambien fuera del marcado del ejecutor, y son el mismo par para los dos lectores. (c) EL TRAMO son los 30 puestos de `docs/loop/SALIDA_V192_T2_CIEGA.txt`, que son los mismos 30 de la ciega del auditor `docs/loop/_auditor_v193_ciega_blind.txt`. (d) AL DOBLE son sus 30 vecinos deterministas, con `vecinos()` IMPORTADA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada, con `evitar` cargado con TODO lo consumido, CONTADO DE SUS FICHEROS Y NO DEL ENCARGO, y con el solape contra el tramo y contra el universo en 0 y 0 POR CONSTRUCCION. (e) criterio escrito literal, ciega y destape en ficheros SEPARADOS, clases escritas y COMMITEADAS en su propio commit ANTES de abrir el destape, y dudosos NOMBRADOS DELANTE. (f) PUBLICAR LO QUE LA VARA NUEVA CAMBIA: cuantos dudosos y cuantas discrepancias habrian salido distinto con `9.6.1`, y si no cambia nada, DECIRLO. NO SE TOCA NINGUNA CLASE: `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre solo en lectura y su `sha256` LF abre y cierra en `0a77b5a35a962621` por las dos convenciones'),
    ("4", 'LA CUARTA PUERTA QUE SOBREVIVA AL PROCESO. Es el hallazgo `5.1` del acta 193, levantado por el auditor CONTRA EL FICHERO QUE LE PROTEGE Y QUE EL EJECUTOR ESCRIBIO PARA EL EN LA 192, y medido en `docs/loop/_auditor_v193_cuarta_puerta_prueba.txt`: `_BITACORA` y `_SELLADO` son estado de MODULO y mueren con el proceso, el auditor sella con el CLI, y en el proceso siguiente `puede_declarar_clases()` responde `NO: este turno no ha sellado` aunque el sello este en disco. Y LA MITAD MAS SERIA ES SOBRE LAS TRES PUERTAS VIEJAS: el docstring afirma que el sello no se pueda escribir despues, y un turno que toca `REPORTE.md` y arranca otro proceso vuelve a sellar con bitacora vacia porque `sellar()` SOBRESCRIBE. (a) QUE LA BITACORA Y EL SELLO SOBREVIVAN AL PROCESO, en un fichero del turno. (b) QUE `sellar()` CAIGA EN ROJO SI YA HAY SELLO EN DISCO PARA ESA VUELTA, en vez de sobrescribirlo. (c) QUE EL CLI PUEDA DECLARAR LAS CLASES, con su bandera, leyendo el sello de disco. (d) Y SI ALGO NO SE PUEDE, DECIRLO EN EL DOCSTRING en vez de afirmar lo contrario, que esa frase vive en sede de cifra publicada desde el 2 sep 2026. (e) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un sello se puede reescribir despues de tocar uno de los tres prohibidos en otro proceso. (f) NO SE CLONA EL FICHERO: `apertura_del_auditor.py` tiene nombre estable y se le anade. (g) RE CORRER SU ARNES DE LA NOMINA CON EL PARCHE PUESTO Y COMPROBAR QUE REPRODUCE BYTE A BYTE; hoy da 4282 bytes y `sha256` `4779fcd04bc5b2da`'),
    ("5", 'EL COTEJO QUE NO CONVIERTA `"no"` EN `si`. Es el hallazgo `5.2` del acta 193. `cuerpo_del_cotejo()` de `scripts/loop/cotejo_de_ciega.py` hace `bool(du)`, y `bool("no")` es `True`; el docstring especifica esa columna como `en dudosos` . `si` o `no`, que es justo la forma que revienta, y el instrumento publico al auditor `discrepancias FUERA de los dudosos: 0 (ninguna)` TENIENDO DOS. LA CIFRA PUBLICADA DEL EJECUTOR NO ESTA AFECTADA: `vuelta192_tarea2b_cotejo.py` linea 145 pasa `p in dudosos`, un booleano de verdad. IMPORTA MAS QUE UNA ERRATA porque la columna `en dudosos` es la unica del fichero de la que cuelga una regla de parada: `AUDITOR.md` 1.2 baja el credito y encarga el doble POR LO QUE CAE FUERA. (a) QUE `en_dudosos` SE NORMALICE O CAIGA, y no se resuelva en silencio, con la misma vara que el caso `G` de la mutacion ya le aplica a `veredicto_de`. (b) QUE LA GUARDA DE `escribir_cotejo()` MIRE ALGO MAS QUE EL DENOMINADOR, o que diga en su salida que no es la sede de esta comprobacion. (c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un `en_dudosos` no booleano se convierte en `si` sin avisar. (d) RE ESCRIBIR EL COTEJO DEL AUDITOR CON EL INSTRUMENTO ARREGLADO y comprobar que da lo que el publica a mano: 30 cotejados, 25 coinciden, 5 discrepan, 3 dentro y 2 fuera. (e) `cotejo_de_ciega.py` NACIO EN LA 192 Y ENTRA EN LA NOMINA POR LA REGLA DEL PROPIO FICHERO: tocarlo ahora es ANTES de que entre, y eso es a favor y no en contra'),
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
    # DESDE ESTA VUELTA LA CIFRA VA CON SU FECHA DE CORTE (banco 9.21).
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
> **NO ES VUELTA DE BATERIA, PERO ES LA ULTIMA ANTES.** `AUDITOR.md` 6.1: la
> bateria corre CADA CINCO VUELTAS, **la 189 la corrio entera**, y **la siguiente
> cae en la 194**. La seccion 9 cierra con el **HUECO DECLARADO Y MEDIDO** por el
> carril de `cerrar_reporte.py`, **con su nombre, sus bytes medidos y su
> atribucion, LAS TRES JUNTAS**. Y por eso **las dos bloqueantes son las que le
> llegan rotas a esa corrida**.
>
> **VAN CINCO SUB-TAREAS Y DOS SON BLOQUEANTES.** El tope de cinco esta ganado con
> holgura y **la cifra se conto del instrumento en esta vuelta**, no se heredo: el
> bloque `E` del sello de apertura corrio
> `scripts/loop/vuelta%(ant)d_racha_de_cierres.py` sobre el inventario ENTERO.
>
> **EL DESFASE DE CALIBRADO SE MIDIO EN LA APERTURA**, dentro del bloque de
> apertura y **antes de la primera operacion**. Una columna de apertura medida al
> cierre es caida que ACUMULA.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina** (la opcion `c` que el fundador RECHAZO el
> 5 sep 2026: **la nomina sigue creciendo y nadie la poda sin el fundador**), ni la
> bateria, que cae en la 194. **Y siguen fuera, nombradas para que la 194 no las
> redescubra:** el desfase de `PATRONES_ACTA`, **que se encarga DESPUES de la 194**
> porque toca `tallar_cabecera_reporte.py` y cuatro entradas de la nomina lo
> nombran; `acumulan()` que lea la tabla o declare que no es la sede; el cotejo de
> clon declarado que separa sentencia de codigo de cambio de texto; la excepcion
> que publica siempre su lista; la medicion del censo de arneses con carril de
> mutacion sin fichero propio; las ocho actas sin entrada propia en la serie (173 a
> 180); el exitcode 2 propagado a `--componer`; y que el campo `evidencia` de
> `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE MUEVE: sigue en
> `LISTA`**.
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
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA, Y DESDE ESTA VUELTA LLEVA SU
  FECHA DE CORTE.** La linea de arriba nombra el acta **%(ant)d** porque
  `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que ORDENA esta vuelta es la
  %(v)d**. Es el `D.2` del reporte de la 184, adjudicado a favor con reparacion
  encargada por la `5.2` del acta 185, **y el acta 193 lo deja expresamente DESPUES
  de la bateria de la 194**. Lo que si se puede contar: **%(n_lit)d reportes
  archivados traen el literal `DESFASE DECLARADO`** (%(lista_lit)s), contados por
  `reportes_con_el_literal()` de este mismo fichero, **con FECHA DE CORTE
  %(corte)s** (banco `9.21`, TODA CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Esa
  fecha es la reparacion que el acta 193 encarga sobre la caida `5.5` del reporte
  de la 192**, que publico una cifra de este mismo inventario contradiciendo a su
  propia seccion 0: **un inventario que crece cada vuelta sin corte envejece solo.**
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
           celdas=celdas, n_ap=len(lado_apertura_roto), filas=filas,
           n_lit=len(con_literal), lista_lit=lista_literal, corte=corte,
           frase_tallador=frase_tallador)

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
