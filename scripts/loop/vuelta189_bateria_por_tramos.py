# -*- coding: utf-8 -*-
r"""vuelta189_bateria_por_tramos.py . LA BATERIA DE MUTACIONES DE LA VUELTA 189,
POR TRAMOS RESUMIBLES, ENTERA Y SOLA.

CLON DECLARADO de scripts/loop/vuelta183_bateria_por_tramos.py. El cotejo lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte CON LO
QUE SALGA: aqui no se afirma que ningun diff salga vacio.

POR QUE EXISTE ESTE CLON, Y LA CAUSA LA MIDIO EL AUDITOR EN LA SECCION 5 DE SU
ACTA. El lanzador de la 183 YA NO REPARTE EN NUEVE TRAMOS SINO EN DIEZ, porque la
nomina paso de 121 a 125 entradas; y su --siguiente, que cuenta las salidas
selladas SALIDA_V183_BATERIA_TRAMO_n.txt de la corrida 183/184, dice hoy
"CIFRA tramos CON salida sellada no vacia: 9", "CIFRA tramos que FALTAN: 1",
"EL SIGUIENTE ES EL TRAMO 10". CORRERLO TAL CUAL HARIA UN SOLO TRAMO DE DIEZ Y
DECLARARIA LA BATERIA CORRIDA HABIENDO CORRIDO 8 ARNESES DE 125: un verde comodo
del tamano de la guarda entera. El bloque H.4 del sello de apertura de la vuelta
189 lo reprodujo entero antes de tocar nada.

LA ADJUDICACION QUE ESTE FICHERO EJECUTA, Y NO SE RE LITIGA: la bateria de esta
vuelta CORRE ENTERA SOBRE LA NOMINA DE HOY Y NO HEREDA NI UNA SALIDA SELLADA DE
LA CORRIDA 183/184. Las tres patas, las tres citadas por el auditor: AUDITOR.md
6.1 dice "la bateria entera"; "una vuelta cortada retoma en el tramo siguiente"
habla de UNA VUELTA QUE SE CORTO, y la del 183/184 CERRO; y "DEL MISMO CALIBRE"
lo cierra, porque nueve salidas de hace cinco vueltas y una de hoy no son del
mismo calibre. Y NO SE BORRA NADA: las nueve salidas de la 183 se quedan donde
estan, y el bloque H.5 del sello de apertura las midio una a una.

COMO LO CONSIGUE, Y NO ES POR TECLEAR NADA: el numero de vuelta y el nombre del
lanzador SE COMPUTAN de os.path.basename(__file__), asi que este fichero escribe
SALIDA_V189_BATERIA_TRAMO_n.txt solo, y su --siguiente cuenta desde cero. El
guarda literales_de_vuelta_clavados() corre sobre el propio fuente y NO DEJA
ARRANCAR si alguien clava un numero de vuelta en una linea que escribe o imprime.

LO QUE CAMBIA RESPECTO DEL ORIGINAL, DICHO PARA QUE EL COTEJO NO SORPRENDA: este
docstring, y las citas del reparto que decian NUEVE cuando la nomina era de 121.
LA CIFRA DE TRAMOS NO SE TECLEA EN NINGUN SITIO: sale de reparto_en_tramos()
sobre la nomina, y --plan la imprime.

USO:
  python scripts/loop/vuelta189_bateria_por_tramos.py --plan
  python scripts/loop/vuelta189_bateria_por_tramos.py --siguiente
  python scripts/loop/vuelta189_bateria_por_tramos.py --tramo 1
  python scripts/loop/vuelta189_bateria_por_tramos.py --componer
"""
import argparse
import datetime
import hashlib
import io
import os
import re
import subprocess
import sys
import tempfile
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
BATERIA = os.path.join(AQUI, "verificar_mutaciones_viejas.py")
NL = chr(10)

# ---------------------------------------------------------------------------
# EL NUMERO DE VUELTA Y EL NOMBRE DEL LANZADOR, COMPUTADOS DEL PROPIO FICHERO.
#
# CORRECCION DECLARADA (2026-09-05, continuacion de la vuelta 183, TAREA 1.b;
# caida `E.1` del acta 183, adjudicacion 5.1). LO QUE PASABA ANTES NO SE BORRA,
# SE CUENTA: este fichero es un CLON DECLARADO del de la vuelta 176 y HEREDO EL
# NUMERO DE SU PADRE en los literales que escribe. Sus salidas selladas decian
# "BATERIA DE LA VUELTA 176" y "lanzada por
# scripts/loop/vuelta176_bateria_por_tramos.py", y eso salio impreso en CUATRO
# ficheros sellados de esta misma vuelta, con TRES menciones de 176 en cada uno
# contadas con grep -c (docs/loop/SALIDA_V183B_APERTURA.txt, bloque H.2, que las
# conto ANTES de tocar este fichero). Las dos afirmaciones eran falsas: la
# bateria es la de la 183 y la lanzo el fichero de la 183.
#
# LA REPARACION NO ES TECLEAR UN 183 ENCIMA DEL 176. Un 183 tecleado se hereda
# igual que se heredo el 176: el clon siguiente volveria a mentir. El numero y
# el nombre SE COMPUTAN de os.path.basename(__file__), de modo que un clon
# llamado vuelta200_bateria_por_tramos.py diga 200 en todas sus salidas sin que
# nadie tenga que acordarse de nada. Y el numero de tramos NO se teclea tampoco:
# sale de len(tramos), o sea de la constante TAMANO que reparte la nomina.
LANZADOR = os.path.basename(os.path.abspath(__file__))
_M_VUELTA = re.match(r"^vuelta(\d+)_", LANZADOR)
if not _M_VUELTA:
    raise SystemExit("ROJO: el nombre %r no dice de que vuelta es este lanzador, "
                     "y el numero NO SE ADIVINA." % LANZADOR)
VUELTA = int(_M_VUELTA.group(1))

sys.path.insert(0, AQUI)
import guarda_commit_dataset as GUARDA   # noqa: E402
import verificar_mutaciones_viejas as B   # noqa: E402

# EL TAMANO DEL TRAMO, Y AQUI SE DICE LO QUE EL ORIGINAL YA NO PODIA DECIR. El
# original explicaba este 13 diciendo que era "el que hace que reparto_en_tramos()
# sobre la nomina de HOY devuelva NUEVE tramos". ESO ERA CIERTO CON UNA NOMINA DE
# 121 Y HOY ES FALSO: con 125 el mismo 13 da DIEZ tramos, nueve de 13 y uno de 8.
# LO QUE MANDA NO ES EL NUMERO DE TRAMOS, ES QUE LA NOMINA ENTERA SE CUBRA: la
# cifra de tramos NO SE TECLEA en ningun sitio, sale de len(tramos), y --componer
# comprueba la cobertura leyendola de las salidas y no del reparto.
TAMANO = 13
MARCA_ENTRADA = "ENTRADA DEL TRAMO: "

# LA MARCA QUE EXIME A UNA CITA HISTORICA DEL GUARDA DE ABAJO. Una linea que
# NOMBRA de donde salio una regla ("el encargo de la 176 fijo esto") NO es una
# atribucion falsa: es una cita, y borrarla seria borrar la procedencia. Se exime
# nombrandola, nunca ensanchando el patron hasta que trague.
MARCA_CITA = "CITA HISTORICA"

# LAS LINEAS QUE ESTE GUARDA MIRA: las que ESCRIBEN o IMPRIMEN texto, que son las
# unicas que pueden meter una atribucion falsa en una salida sellada.
_PREFIJOS_QUE_ESCRIBEN = ("print(", "f.write(", "cab.append(", "return \"SALIDA",
                          "return 'SALIDA")
# EL PATRON, ENSANCHADO POR LO QUE SU PROPIO ARNES LE ENCONTRO Y NO POR GUSTO.
# La primera version pedia `V` mayuscula y no admitia separador en minuscula, y
# su arnes la tumbo con dos casos que el defecto REAL de esta vuelta traia: el
# prefijo `v176_tramo` de los `mkdtemp`, que va en minuscula, y la frase
# "de la vuelta 176" con su espacio. Las dos salieron impresas en las salidas
# selladas. Se ensancha una vez, con la medicion delante, y las citas legitimas
# se eximen NOMBRANDOLAS con MARCA_CITA, que es lo que impide que ensanchar el
# patron se convierta en un cepo.
_PATRON_CLAVADO = re.compile(r"(?:vuelta|v)[ _]?(\d{3})", re.IGNORECASE)


def numero_de_vuelta_del_nombre(nombre):
    """EL NUMERO DE VUELTA QUE DICE UN NOMBRE DE FICHERO, o None si no lo dice.
    PURA. Es la mitad computable de "el numero no se teclea"."""
    m = re.match(r"^vuelta(\d+)_", os.path.basename(nombre))
    return int(m.group(1)) if m else None


def titulo_de_corrida(n, total, vuelta):
    """LA PRIMERA LINEA DE LA SALIDA SELLADA DE UN TRAMO. PURA."""
    return "CORRIDA DEL TRAMO %d DE %d, BATERIA DE LA VUELTA %d" % (n, total, vuelta)


def linea_de_lanzador(lanzador):
    """LA SEGUNDA LINEA DE LA SALIDA SELLADA DE UN TRAMO. PURA."""
    return "lanzada por scripts/loop/%s" % lanzador


def titulo_de_composicion(vuelta):
    """LA PRIMERA LINEA DE LA CABECERA DE --componer. PURA."""
    return ("LA BATERIA DE MUTACIONES DE LA VUELTA %d, CORRIDA ENTERA Y EN TRAMOS"
            % vuelta)


def linea_de_composicion(lanzador):
    """LA SEGUNDA LINEA DE LA CABECERA DE --componer. PURA."""
    return "compuesta por scripts/loop/%s --componer" % lanzador


def linea_de_estimacion(que, bajo, alto, nomina, head):
    """UNA LINEA DE ESTIMACION CON SU CORTE PEGADO EN LA MISMA LINEA. PURA.

    POR QUE EXISTE (vuelta 184, TAREA 1.c; caida `E.1` del acta 184, y es la
    ESCALADA que esa acta encarga en su seccion 9 por `AUDITOR.md` 1.2).

    LO QUE PASABA ANTES NO SE BORRA, SE CUENTA: `--plan` imprimia la nomina
    ARRIBA y la estimacion ABAJO, y quien copiaba la estimacion copiaba una cifra
    sin su corte. El reporte de la 183 publico dos veces `36,6 y 47,7` minutos
    como estimacion *de hoy* cuando su propia nomina ya era de **112** y el
    `--plan` de ese dia decia `37,0 y 48,2`: la cifra publicada era la de una
    nomina de **111**, o sea la de antes de que esa misma vuelta la subiera. La
    aritmetica lo delata, 111 por 0,33 da 36,6 y 111 por 0,43 da 47,7.

    EL REMEDIO NO ES UNA ADVERTENCIA: la estimacion sale con su corte pegado, de
    modo que QUIEN COPIE LA ESTIMACION COPIE SU CORTE. Es la misma medicina que
    `sello_de_corte()` de `verificar_mutaciones_viejas.py` le puso a las cifras de
    nomina de las salidas selladas por el banco `9.21`, y aqui se escribe con el
    mismo texto para que las dos se lean igual.

    PURA a proposito: recibe QUE se estima, los dos extremos ya calculados, el
    tamano de nomina y el head, y devuelve el texto. Su arnes,
    `scripts/loop/vuelta184_tarea1c_mutacion_estimacion.py`, la tumba sin correr
    ningun proceso."""
    return ("  ESTIMACION minutos %s: entre %.1f y %.1f "
            "(corte: HEAD %s, nomina de %d entradas contada en esta corrida)"
            % (que, bajo, alto, head, nomina))


# EL PATRON QUE LEE EL CORTE DE UNA LINEA DE ESTIMACION. El head va con `.+?` y
# no con `\S+` a proposito: `corte_de_git()` devuelve `(no medible)` con un
# espacio dentro cuando git no responde, y una linea con corte de verdad no se
# puede declarar SIN corte solo porque git no contestara.
_PATRON_CORTE_ESTIMACION = re.compile(
    r"\(corte: HEAD (.+?), nomina de (\d+) entradas contada en esta corrida\)$")


def corte_de_la_estimacion(linea):
    """EL CORTE QUE LLEVA UNA LINEA DE ESTIMACION: (head, nomina), o None si la
    linea NO lleva corte. PURA.

    Es la mitad que puede caer: una linea de estimacion sin corte devuelve None y
    su arnes la declara ROJA."""
    m = _PATRON_CORTE_ESTIMACION.search(linea.rstrip())
    return (m.group(1), int(m.group(2))) if m else None


def corte_calza(linea, nomina):
    """LA LINEA LLEVA SU CORTE Y ESE CORTE DICE LA NOMINA QUE SE LE PASA. PURA.

    Las dos mitades tienen que fallar por separado: una linea SIN corte y una
    linea CON un corte que miente son dos averias distintas y las dos son rojo."""
    c = corte_de_la_estimacion(linea)
    return c is not None and c[1] == nomina


def literales_de_vuelta_clavados(texto):
    """LAS LINEAS DE UN FUENTE QUE CLAVAN UN NUMERO DE VUELTA COMO LITERAL EN
    ALGO QUE SE ESCRIBE O SE IMPRIME. PURA: recibe el texto y devuelve
    [(numero_de_linea, linea, numero_clavado)].

    ES EL GUARDA DE LA CAIDA `E.1`, Y MUERDE AL PROPIO FICHERO. Lo que dejo pasar
    la atribucion falsa no fue un descuido de teclado: fue que NADIE MIRABA. Este
    guarda corre en `main()` sobre el fuente de este mismo modulo y el lanzador NO
    ARRANCA si encuentra uno, porque una salida sellada con la vuelta equivocada
    vale menos que no tenerla: se publica como prueba de una corrida que no es la
    suya. Las citas historicas se eximen marcandolas con MARCA_CITA."""
    out = []
    for i, linea in enumerate(texto.replace(chr(13) + NL, NL).split(NL), 1):
        s = linea.strip()
        if MARCA_CITA in linea:
            continue
        if not (s.startswith(_PREFIJOS_QUE_ESCRIBEN) or "mkdtemp(" in s):
            continue
        for m in _PATRON_CLAVADO.finditer(s):
            out.append((i, s, m.group(1)))
    return out


class Desdoble(object):
    """STDOUT DESDOBLADO A UN FICHERO DE TRABAJO **FUERA DE `docs/loop/`**.

    CORRECCION DECLARADA (2026-09-05, vuelta 177, TAREA 1.e; adjudicacion 7.5
    del acta 176, `D.5`). LO QUE PASABA ANTES NO SE BORRA, SE CUENTA: este
    lanzador no escribia su propia transcripcion a ningun sitio, asi que acababa
    donde la metiera quien lo llamaba, y en la vuelta 176 quien lo llamaba la
    metio en `docs/loop/SALIDA_V176_T1_LANZADOR_TRAMO_<N>.txt`, o sea DENTRO del
    mismo directorio que la bateria esta mirando mientras corre. Se midio y NO
    fabrico ruido: los nueve tramos publicaron RUIDO DE CONCURRENCIA 0 ficheros.
    PERO ESO ES SUERTE DE BUFFER, no una garantia: la salida del lanzador se
    quedaba en el buffer hasta que el proceso terminaba, o sea despues de la
    bateria. UN CONTROL QUE FUNCIONA POR UNA PROPIEDAD QUE NADIE GARANTIZA NO ES
    UN CONTROL (banco 9, fallar ruidoso).

    LA CORRECCION ES LA MISMA PRECAUCION QUE EL FICHERO DE TRABAJO DEL TRAMO YA
    TENIA, APLICADA AL SEGUNDO FICHERO: se escribe fuera de `docs/loop/`, en el
    directorio temporal del tramo, y SE COPIA DENTRO AL FINAL, cuando la bateria
    ya no esta mirando. Asi la evidencia no se pierde y la concurrencia no
    depende de un buffer."""

    def __init__(self, destino, original):
        self.f = io.open(destino, "w", encoding="utf-8", newline=NL)
        self.original = original

    def write(self, s):
        self.original.write(s)
        self.f.write(s)
        self.f.flush()
        return len(s)

    def flush(self):
        self.original.flush()
        self.f.flush()

    def cerrar(self):
        self.f.close()


def nombre_transcripcion(n):
    return "SALIDA_V%d_LANZADOR_TRAMO_%d.txt" % (VUELTA, n)


def ahora_utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def nombre_tramo(n):
    return "SALIDA_V%d_BATERIA_TRAMO_%d.txt" % (VUELTA, n)


def nombre_de_la_compuesta():
    """EL NOMBRE DE LA SALIDA UNICA. Computado igual que los demas, para que la
    pieza que `cerrar_reporte.py` pide con --bateria no dependa de un literal."""
    return "SALIDA_V%d_BATERIA.txt" % VUELTA


def medir(ruta):
    """BYTES, LINEAS Y SHA256 DE UN FICHERO. Los bytes son los DEL DISCO, y el
    sha256 se computa sobre el texto normalizado a LF, que es la convencion que
    esta casa viene arrastrando sin fijar (hallazgo 4.1 del acta 174). SE DICEN
    LAS DOS: los bytes de disco y los bytes normalizados a LF, para que la cifra
    que se publique no dependa de cual mire quien la lea."""
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return {
        "bytes_disco": os.path.getsize(ruta),
        "bytes_lf": len(lf),
        "lineas": lf.count(b"\n"),
        "sha256_lf": hashlib.sha256(lf).hexdigest(),
    }


def guarda_y_restauracion(titulo):
    """PASOS 1 Y 2. Devuelve (ok, restaurados), con `restaurados` la lista de
    ficheros sobre los que hubo que hacer `git checkout --`.

    LOS FICHEROS NO SE TECLEAN NUNCA: salen de lo que `git diff --numstat`
    devuelve. Restaurar una lista tecleada seria restaurar lo que uno cree que
    se movio, no lo que se movio."""
    print("")
    print("*" * 78)
    print("%s" % titulo)
    print("*" * 78)
    filas = GUARDA.filas_sucias(RAIZ)
    print("  CIFRA filas de `git diff --numstat -- dataset/`: %d" % len(filas))
    restaurados = []
    if not filas:
        print("  LIMPIO AL ENTRAR: cero filas. No hay nada que restaurar.")
        return True, restaurados

    print("  SUCIO AL ENTRAR. Los ficheros, NOMBRADOS POR GIT y no tecleados:")
    for a, b, f in filas:
        print("      +%s -%s  %s" % (a, b, f))
    for _a, _b, f in filas:
        c, salida = GUARDA.git(["checkout", "--", f], RAIZ)
        print("  `git checkout -- %s` -> exit %d" % (f, c))
        restaurados.append(f)

    # SE VUELVE A MEDIR. Restaurar sin remedir es prometer, no comprobar.
    filas2 = GUARDA.filas_sucias(RAIZ)
    print("  CIFRA filas DESPUES de restaurar (remedido, no supuesto): %d" % len(filas2))
    for a, b, f in filas2:
        print("      QUEDA SUCIO: +%s -%s  %s" % (a, b, f))
    if filas2:
        print("  ROJO: la restauracion no dejo el arbol limpio. El tramo NO empieza.")
        return False, restaurados
    print("  RESTAURADO Y REMEDIDO: cero filas. El tramo puede empezar.")
    return True, restaurados


def correr_tramo(n, tramos):
    """LOS CINCO PASOS DE UN TRAMO. Devuelve el exitcode."""
    print("=" * 78)
    print("TRAMO %d DE %d, DE LA BATERIA DE LA VUELTA %d"
          % (n, len(tramos), VUELTA))
    print("=" * 78)
    # LA ATRIBUCION, DENTRO DE LA TRANSCRIPCION SELLADA Y NO SOLO EN LA CONSOLA.
    # El guarda de main() corre antes de que exista el desdoble, asi que su
    # veredicto se vuelve a computar aqui, donde SI queda en el fichero sellado.
    print("  lanzador (os.path.basename, no tecleado): %s" % LANZADOR)
    print("  vuelta (computada del nombre, no tecleada): %d" % VUELTA)
    print("  CIFRA literales de vuelta clavados en el fuente: %d"
          % len(literales_de_vuelta_clavados(
              io.open(os.path.abspath(__file__), encoding="utf-8").read())))
    print("  CIFRA nomina entera (leida del modulo, no tecleada): %d" % len(B.VIEJAS))
    print("  CIFRA tamano de tramo: %d" % TAMANO)
    print("  CIFRA tramos del reparto (computada): %d" % len(tramos))
    print("  CIFRA entradas de ESTE tramo: %d" % len(tramos[n - 1]))
    for s, _admite in tramos[n - 1]:
        print("      %s" % s)

    ok, restaurados = guarda_y_restauracion(
        "PASOS 1 Y 2. LA GUARDA DEL COMMIT Y LA RESTAURACION, AL ENTRAR AL TRAMO %d" % n)
    if not ok:
        print("")
        print("ROJO: el tramo %d NO EMPIEZA porque `dataset/` no quedo limpio." % n)
        return 1

    destino = os.path.join(LOOP, nombre_tramo(n))
    tmpdir = tempfile.mkdtemp(prefix="v%d_tramo%d_" % (VUELTA, n))
    trabajo = os.path.join(tmpdir, "tramo_en_curso.txt")
    cmd = [sys.executable, "-u", BATERIA, "--tramo", str(n),
           "--tamano-tramo", str(TAMANO)]
    entorno = dict(os.environ)
    entorno["PYTHONIOENCODING"] = "utf-8"

    print("")
    print("*" * 78)
    print("PASO 3. LA CORRIDA DEL TRAMO %d" % n)
    print("*" * 78)
    inicio = ahora_utc()
    t0 = time.perf_counter()
    print("  inicio (UTC): %s" % inicio)
    print("  comando: %s" % " ".join(cmd[1:]))
    print("  fichero de trabajo, FUERA de docs/loop/: %s" % trabajo)
    print("  destino final: docs/loop/%s" % nombre_tramo(n))

    with io.open(trabajo, "w", encoding="utf-8", newline=NL) as f:
        f.write(titulo_de_corrida(n, len(tramos), VUELTA) + NL)
        f.write(linea_de_lanzador(LANZADOR) + NL)
        f.write("INICIO (reloj de pared, UTC): %s" % inicio + NL)
        if restaurados:
            f.write("RESTAURACION AL ENTRAR: se hizo `git checkout --` sobre %d "
                    "fichero(s): %s" % (len(restaurados), ", ".join(restaurados)) + NL)
        else:
            f.write("RESTAURACION AL ENTRAR: no hizo falta, dataset/ estaba limpio "
                    "(cero filas de `git diff --numstat`)" + NL)
        f.write(("=" * 78) + NL)
        f.flush()
        p = subprocess.Popen(cmd, cwd=RAIZ, env=entorno, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        for linea in io.TextIOWrapper(p.stdout, encoding="utf-8", errors="replace"):
            f.write(linea.replace(chr(13) + NL, NL).rstrip(chr(13) + NL) + NL)
            f.flush()
        codigo = p.wait()
        fin = ahora_utc()
        segundos = time.perf_counter() - t0
        f.write(("=" * 78) + NL)
        f.write("EXITCODE DEL TRAMO %d: %d" % (n, codigo) + NL)
        f.write("FIN (reloj de pared, UTC): %s" % fin + NL)
        f.write("DURACION DEL TRAMO (monotona, segundos): %.1f" % segundos + NL)
        f.write("DURACION DEL TRAMO (monotona, minutos): %.1f" % (segundos / 60.0) + NL)
        f.flush()

    datos = io.open(trabajo, "rb").read()
    io.open(destino, "wb").write(datos)

    print("")
    print("*" * 78)
    print("PASO 4. EL SELLADO, MEDIDO ANTES DE NOMBRARLO EN NINGUN SITIO")
    print("        (EJECUTOR.md 1, LA RUTA QUE PROMETE PRUEBA ES CIFRA)")
    print("*" * 78)
    m = medir(destino)
    print("  docs/loop/%s" % nombre_tramo(n))
    print("  CIFRA bytes en disco: %d" % m["bytes_disco"])
    print("  CIFRA bytes normalizado a LF: %d" % m["bytes_lf"])
    print("  CIFRA lineas: %d" % m["lineas"])
    print("  CIFRA sha256 (LF): %s" % m["sha256_lf"][:16])
    print("  CIFRA exitcode del tramo: %d" % codigo)
    print("  CIFRA duracion en minutos: %.1f" % (segundos / 60.0))
    print("  inicio (UTC): %s | fin (UTC): %s" % (inicio, fin))
    if m["bytes_disco"] == 0:
        print("")
        print("ROJO: el tramo %d midio CERO BYTES. Esa ruta NO SE PUEDE PUBLICAR" % n)
        print("      como prueba de nada, y por eso no se da por buena.")
        return 1

    ok_salida, _r = guarda_y_restauracion(
        "PASO 5. LA GUARDA DEL COMMIT, OTRA VEZ, AL SALIR DEL TRAMO %d" % n)

    print("")
    if codigo != 0:
        print("EL TRAMO %d SALE EN ROJO, exitcode %d, Y AQUI SE PARA." % (n, codigo))
        print("No se re-corre: la guarda que muerde es informacion, no un estorbo")
        # CITA HISTORICA: la linea de abajo NOMBRA de donde salio la regla, no
        # atribuye esta corrida a otra vuelta. Se exime por la marca, con su
        # motivo escrito, que es como se eximen y no ensanchando el patron.
        print("(encargo de la vuelta 176, TAREA 1.f). La salida esta sellada y "   # CITA HISTORICA
              "medida.")
        return codigo
    if not ok_salida:
        print("EL TRAMO %d corrio verde PERO DEJO `dataset/` SUCIO AL SALIR y la" % n)
        print("restauracion no lo limpio. Eso es rojo del tramo.")
        return 1
    print("TRAMO %d VERDE. Su salida esta sellada, medida y se puede commitear." % n)
    return 0


def entradas_de_la_salida(ruta):
    """LAS ENTRADAS QUE UNA SALIDA DE TRAMO DICE HABER CORRIDO, leidas de sus
    lineas `ENTRADA DEL TRAMO: <arnes>`. PURA salvo por leer el fichero.

    SE LEEN DE LA SALIDA Y NO SE RECALCULAN del reparto a proposito: si se
    recalcularan, la comprobacion de cobertura estaria preguntandole al reparto
    por el reparto, y no probaria nada sobre lo que de verdad corrio."""
    texto = io.open(ruta, encoding="utf-8", errors="replace").read()
    out = []
    for linea in texto.replace(chr(13) + NL, NL).split(NL):
        if MARCA_ENTRADA in linea:
            out.append(linea.split(MARCA_ENTRADA, 1)[1].strip())
    return out


def componer(tramos):
    """LA SALIDA UNICA, COMPUESTA DE LOS TRAMOS Y DESCONFIANDO DE ELLOS."""
    print("=" * 78)
    print("LA COMPOSICION DE LOS %d TRAMOS EN UNA SOLA SALIDA" % len(tramos))
    print("=" * 78)
    nomina = [s for s, _a in B.VIEJAS]
    print("  CIFRA entradas de la nomina (leida del modulo): %d" % len(nomina))
    print("")

    partes = []
    vistas = []
    fallos = []
    for n in range(1, len(tramos) + 1):
        ruta = os.path.join(LOOP, nombre_tramo(n))
        if not os.path.exists(ruta):
            print("  TRAMO %d: docs/loop/%s NO EXISTE" % (n, nombre_tramo(n)))
            fallos.append("falta la salida del tramo %d" % n)
            continue
        m = medir(ruta)
        ent = entradas_de_la_salida(ruta)
        print("  TRAMO %d: %-38s %7d bytes disco | %7d bytes LF | %4d lineas | "
              "sha256 %s | %2d entradas"
              % (n, nombre_tramo(n), m["bytes_disco"], m["bytes_lf"], m["lineas"],
                 m["sha256_lf"][:12], len(ent)))
        if m["bytes_disco"] == 0:
            fallos.append("la salida del tramo %d mide CERO BYTES" % n)
        vistas.extend(ent)
        partes.append((n, ruta, m))

    print("")
    print("  LA COBERTURA, LEIDA DE LAS SALIDAS Y NO RECALCULADA DEL REPARTO")
    print("  CIFRA entradas que los tramos dicen haber corrido: %d" % len(vistas))
    faltan = [s for s in nomina if s not in set(vistas)]
    sobran = [s for s in vistas if s not in set(nomina)]
    repes = sorted({s for s in vistas if vistas.count(s) > 1})
    print("  CIFRA entradas de la nomina que NINGUN tramo corrio: %d" % len(faltan))
    for s in faltan:
        print("      SIN CORRER: %s" % s)
    print("  CIFRA entradas corridas que NO estan en la nomina: %d" % len(sobran))
    for s in sobran:
        print("      AJENA: %s" % s)
    print("  CIFRA entradas corridas MAS DE UNA VEZ: %d" % len(repes))
    for s in repes:
        print("      REPETIDA: %s" % s)
    if faltan:
        fallos.append("%d entrada(s) de la nomina no las corrio ningun tramo" % len(faltan))
    if sobran:
        fallos.append("%d entrada(s) corridas no estan en la nomina" % len(sobran))
    if repes:
        fallos.append("%d entrada(s) se corrieron mas de una vez" % len(repes))

    print("")
    if fallos:
        print("ROJO, %d motivo(s). LA SALIDA UNICA NO SE COMPONE Y NO SE NOMBRA" % len(fallos))
        print("NINGUNA RUTA COMO PRUEBA:")
        for f in fallos:
            print("   " + f)
        return 1

    destino = os.path.join(LOOP, nombre_de_la_compuesta())
    cab = []
    cab.append(titulo_de_composicion(VUELTA))
    cab.append(linea_de_composicion(LANZADOR))
    cab.append("")
    cab.append("LO QUE SE PARTIO ES EL BOCADO, NO LA BATERIA. Las cuatro cosas que la")
    cab.append("letra del fundador del 5 sep 2026 fija siguen enteras: la cadencia (cada")
    cab.append("cinco vueltas), la soledad (vuelta propia sin nada al lado), la")
    cab.append("integridad (cada entrada corrida, y corrida DOS VECES) y la prohibicion")
    cab.append("de podar la nomina.")
    cab.append("")
    cab.append("CIFRA entradas de la nomina: %d" % len(nomina))
    cab.append("CIFRA tramos: %d" % len(partes))
    cab.append("CIFRA entradas que los tramos dicen haber corrido: %d" % len(vistas))
    cab.append("CIFRA entradas sin correr: %d | repetidas: %d | ajenas: %d"
               % (len(faltan), len(repes), len(sobran)))
    cab.append("LA COBERTURA SE LEYO DE LAS SALIDAS, no se recalculo del reparto.")
    cab.append("")
    for n, ruta, m in partes:
        cab.append("  tramo %d -> %s: %d bytes disco, %d bytes LF, %d lineas, sha256 %s"
                   % (n, nombre_tramo(n), m["bytes_disco"], m["bytes_lf"],
                      m["lineas"], m["sha256_lf"][:16]))
    cab.append("=" * 78)

    piezas = [NL.join(cab)]
    for n, ruta, _m in partes:
        piezas.append((NL + "=" * 78 + NL +
                       "TRAMO %d DE %d. SALIDA CRUDA, SIN RECORTAR, DE docs/loop/%s"
                       % (n, len(partes), nombre_tramo(n)) + NL +
                       "=" * 78 + NL))
        piezas.append(io.open(ruta, encoding="utf-8", errors="replace").read()
                      .replace(chr(13) + NL, NL))
    texto = NL.join(piezas)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)

    m = medir(destino)
    print("LA SALIDA UNICA, MEDIDA ANTES DE NOMBRARLA EN NINGUN SITIO")
    print("   docs/loop/%s" % nombre_de_la_compuesta())
    print("   CIFRA bytes en disco: %d" % m["bytes_disco"])
    print("   CIFRA bytes normalizado a LF: %d" % m["bytes_lf"])
    print("   CIFRA lineas: %d" % m["lineas"])
    print("   CIFRA sha256 (LF): %s" % m["sha256_lf"])
    if m["bytes_disco"] == 0:
        print("")
        print("ROJO: la salida unica mide CERO BYTES y esa ruta NO SE PUBLICA.")
        return 1
    print("")
    print("VERDE: los %d tramos cubren la nomina entera, cada entrada EXACTAMENTE"
          % len(partes))
    print("UNA VEZ, y la salida unica existe y mide %d bytes." % m["bytes_disco"])
    return 0


def plan(tramos):
    print("=" * 78)
    print("EL REPARTO, COMPUTADO DE LA NOMINA Y NO TECLEADO")
    print("=" * 78)
    print("  CIFRA entradas de la nomina: %d" % len(B.VIEJAS))
    print("  CIFRA tamano de tramo: %d" % TAMANO)
    print("  CIFRA tramos: %d" % len(tramos))
    print("  CIFRA suma de las entradas de todos los tramos: %d"
          % sum(len(t) for t in tramos))
    print("")
    for i, t in enumerate(tramos, 1):
        print("  TRAMO %d: %d entradas" % (i, len(t)))
        for s, _a in t:
            print("      %s" % s)
    print("")
    print("  EL RELOJ, ESTIMADO CON LAS CIFRAS DEL PROPIO ARCHIVO Y DICHO COMO")
    print("  ESTIMACION Y NO COMO MEDICION: la ultima bateria con cuerpo (la del")
    print("  auditor de la 171) hizo 75 entradas en 32,5 minutos, o sea 0,43")
    print("  minutos por entrada, y la media historica es 0,33.")
    # LAS DOS LINEAS DE ESTIMACION SALEN CON SU CORTE PEGADO (vuelta 184, TAREA
    # 1.c; caida `E.1` del acta 184). La nomina y el head se computan AQUI, en la
    # misma corrida que la estimacion, para que el corte sea el de la cifra que
    # acompana y no el de otra medicion.
    nomina_hoy = len(B.VIEJAS)
    head_hoy = B.corte_de_git()
    print(linea_de_estimacion("por tramo de %d entradas" % TAMANO,
                              TAMANO * 0.33, TAMANO * 0.43, nomina_hoy, head_hoy))
    print(linea_de_estimacion("de la nomina entera",
                              nomina_hoy * 0.33, nomina_hoy * 0.43,
                              nomina_hoy, head_hoy))
    print("  LA MEDICION DE VERDAD LA DA CADA TRAMO AL CERRARSE, y es la que se")
    print("  publica. Esto es solo el reparto.")
    return 0


def siguiente(tramos):
    """QUE TRAMO TOCA, MIRANDO QUE SALIDAS SELLADAS HAY. Es la mitad en codigo de
    "una vuelta cortada RETOMA EN EL TRAMO SIGUIENTE": el lanzador de la 176 ya
    era resumible de hecho, pero saber cual tocaba era cosa de acordarse.

    UNA SALIDA SELLADA QUE MIDE CERO BYTES NO CUENTA COMO HECHA, y eso no es
    severidad: la bateria del ejecutor salio en CERO BYTES tres vueltas seguidas
    (171, 172 y 173) y esa es media causa del regimen entero de AUDITOR.md 6.1.
    Por la letra del 5 sep 2026, una ruta que promete prueba y mide cero bytes es
    CAIDA DE CIFRA."""
    print("=" * 78)
    print("QUE TRAMO TOCA, CONTADO DE docs/loop/ Y NO RECORDADO")
    print("=" * 78)
    hechos, faltan = [], []
    for i in range(1, len(tramos) + 1):
        ruta = os.path.join(LOOP, nombre_tramo(i))
        tam = os.path.getsize(ruta) if os.path.exists(ruta) else -1
        estado = ("NO EXISTE" if tam < 0 else
                  ("CERO BYTES: NO CUENTA" if tam == 0 else "%d bytes" % tam))
        print("  TRAMO %d: %-24s %s" % (i, nombre_tramo(i), estado))
        (hechos if tam > 0 else faltan).append(i)
    print("")
    print("  CIFRA tramos del reparto: %d" % len(tramos))
    print("  CIFRA tramos CON salida sellada no vacia: %d" % len(hechos))
    print("  CIFRA tramos que FALTAN: %d" % len(faltan))
    print("  LOS QUE FALTAN: %s"
          % (", ".join(str(x) for x in faltan) or "(ninguno)"))
    if faltan:
        print("")
        print("  EL SIGUIENTE ES EL TRAMO %d." % faltan[0])
        print("  Se corre con: python scripts/loop/%s --tramo %d"
              % (LANZADOR, faltan[0]))
        print("  Y SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR, antes de seguir.")
    else:
        print("")
        print("  LOS %d TRAMOS TIENEN SALIDA SELLADA." % len(tramos))
        print("  Ahora, y solo ahora, --componer arma la salida unica.")
    print("")
    print("  LA BATERIA SE DECLARA CORRIDA CUANDO LOS %d TIENEN SALIDA SELLADA DEL"
          % len(tramos))
    print("  MISMO CALIBRE, y el calibre lo coteja --componer, no esta orden.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramo", type=int, default=None, help="corre el tramo N")
    ap.add_argument("--componer", action="store_true",
                    help="compone la salida unica de los tramos ya sellados")
    ap.add_argument("--plan", action="store_true",
                    help="imprime el reparto y no corre nada")
    ap.add_argument("--siguiente", action="store_true",
                    help="dice que tramo toca, mirando que salidas selladas hay")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    # EL GUARDA DE LA CAIDA `E.1`, CORRIDO SOBRE EL PROPIO FUENTE Y ANTES DE
    # ESCRIBIR NADA. Si alguien vuelve a clavar un numero de vuelta como literal
    # en una linea que se escribe o se imprime, ESTE LANZADOR NO ARRANCA. No es
    # severidad: una salida sellada que se atribuye otra corrida se publica luego
    # como prueba de esa otra corrida, y eso ya paso cuatro veces en esta misma
    # vuelta. Fallar ruidoso (banco 9) antes que sellar callado.
    clavados = literales_de_vuelta_clavados(
        io.open(os.path.abspath(__file__), encoding="utf-8").read())
    print("GUARDA DE LA ATRIBUCION, CORRIDA SOBRE EL PROPIO FUENTE")
    print("  lanzador (os.path.basename, no tecleado): %s" % LANZADOR)
    print("  vuelta (computada del nombre, no tecleada): %d" % VUELTA)
    print("  CIFRA literales de vuelta clavados en lineas que escriben: %d"
          % len(clavados))
    for i, linea, num in clavados:
        print("      LINEA %d clava %s: %s" % (i, num, linea[:120]))
    if clavados:
        print("")
        print("ROJO: hay %d literal(es) de vuelta clavados en lineas que escriben."
              % len(clavados))
        print("      El lanzador NO ARRANCA. El numero se computa del nombre del")
        print("      fichero; si la linea es una cita historica, se exime con la")
        print("      marca %r y no ensanchando el patron." % MARCA_CITA)
        return 1
    print("  VERDE: ninguna linea que escribe clava un numero de vuelta.")
    print("")

    tramos = B.reparto_en_tramos(B.VIEJAS, TAMANO)

    if a.siguiente:
        return siguiente(tramos)
    if a.plan:
        return plan(tramos)
    if a.componer:
        return componer(tramos)
    if a.tramo is None:
        print("ROJO: hace falta --tramo N, --componer o --plan.")
        return 1
    if not (1 <= a.tramo <= len(tramos)):
        print("ROJO: se pidio el tramo %d y el reparto solo tiene %d."
              % (a.tramo, len(tramos)))
        return 1

    # LA TRANSCRIPCION DEL PROPIO LANZADOR SE ESCRIBE FUERA DE `docs/loop/` Y SE
    # COPIA DENTRO AL FINAL (vuelta 177, TAREA 1.e; `D.5` del acta 176, punto
    # 7.5). Se instala AQUI y no dentro de `correr_tramo` para que envuelva la
    # salida ENTERA del tramo, incluida la de la guarda del commit y la de la
    # restauracion al entrar, que son las que corren antes de que exista ningun
    # directorio temporal. Ver la clase `Desdoble` para el motivo.
    tmpdir = tempfile.mkdtemp(prefix="v%d_lanzador%d_" % (VUELTA, a.tramo))
    fuera = os.path.join(tmpdir, "lanzador_en_curso.txt")
    original = sys.stdout
    doble = Desdoble(fuera, original)
    sys.stdout = doble
    try:
        print("LA TRANSCRIPCION DE ESTE LANZADOR SE ESTA ESCRIBIENDO FUERA DE")
        print("docs/loop/, y se copiara dentro AL TERMINAR: %s" % fuera)
        codigo = correr_tramo(a.tramo, tramos)
    finally:
        sys.stdout = original
        doble.cerrar()
        dentro = os.path.join(LOOP, nombre_transcripcion(a.tramo))
        datos = io.open(fuera, "rb").read()
        io.open(dentro, "wb").write(datos)
        print("TRANSCRIPCION DEL LANZADOR COPIADA A docs/loop/%s (%d bytes), "
              "ESCRITA FUERA MIENTRAS LA BATERIA CORRIA"
              % (nombre_transcripcion(a.tramo), len(datos)))
    return codigo


if __name__ == "__main__":
    raise SystemExit(main())
