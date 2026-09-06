# -*- coding: utf-8 -*-
r"""vuelta183_tarea1b_mutacion_atribucion.py . EL ARNES DE LA CAIDA `E.1`: EL
NUMERO DE VUELTA DE UNA SALIDA SELLADA SE COMPUTA, NO SE CLAVA.

QUE CAIDA REPARA, CON SU MEDICION. Acta 183, adjudicacion 5.1, caida `E.1` contra
el ejecutor, CIFRA PUBLICADA EN LA CUARTA SEDE: las cuatro salidas selladas de la
bateria de la vuelta 183 declaraban en sus primeras lineas "BATERIA DE LA VUELTA
176" y "lanzada por scripts/loop/vuelta176_bateria_por_tramos.py". Las dos son
falsas. El fichero es un CLON DECLARADO del de la 176 y HEREDO EL NUMERO DE SU
PADRE en todo lo que escribe.

LO QUE PASABA ANTES NO SE BORRA, SE CUENTA, Y ESTE ARNES LO CUENTA CADA VEZ QUE
CORRE. Su bloque K lee `docs/loop/SALIDA_V183B_APERTURA.txt`, que es el bloque de
apertura de la continuacion de la 183 y conto las menciones de `176` ANTES de que
nadie tocara el lanzador, e imprime esa cifra con el `sha256` del fichero al
lado. El dia que ese fichero se mueva, la salida lo dira sola.

POR QUE LA REPARACION NO ES TECLEAR UN 183 ENCIMA DEL 176. Un 183 tecleado se
hereda igual que se heredo el 176: el clon siguiente vuelve a mentir y nadie se
entera hasta que el auditor lee una salida sellada. El numero y el nombre del
lanzador SE COMPUTAN de `os.path.basename(__file__)`, y el numero de tramos sale
de `len(tramos)`, o sea de la constante que ya reparte la nomina.

EL CASO POSITIVO ES POR MUTACION SOBRE VARIABLE COMPUTADA, QUE ES LA CONDICION
DEL ENCARGO. El bloque G clona el fuente REAL a un fichero llamado
`vuelta777_bateria_por_tramos.py`, lo importa, y comprueba que TODO lo que ese
clon escribe dice 777: si el numero estuviera clavado, diria 183 y el caso caeria.
El bloque H hace la mutacion de verdad: coge ese mismo clon y le CLAVA el numero
como literal, y el arnes TIENE QUE CAER. Y el bloque I lo lleva hasta el final:
corre el clon con el literal clavado como PROCESO, y el lanzador TIENE QUE
NEGARSE A ARRANCAR con exitcode 1.

CADA CASO SE EVALUA SOBRE UNA VARIABLE COMPUTADA y despues se cambia el valor
esperado para comprobar que el caso CAE (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA
POR MUTACION). Un `assert` que compara una constante literal consigo misma no
puede fallar nunca y no prueba nada.

SUJETO CONGELADO, Y AQUI ES UNA HUELLA Y NO UNA FRASE. Todos los clones se
fabrican con `tempfile.mkdtemp` y se retiran; los dos ficheros del repo que este
arnes lee son `scripts/loop/vuelta183_bateria_por_tramos.py`, que es EL SUJETO
BAJO PRUEBA de un arnes de mutacion y por definicion se mueve, y
`docs/loop/SALIDA_V183B_APERTURA.txt`, que es una salida sellada y commiteada;
de los dos se imprime el `sha256` cada vez que corre.

LA SALIDA ES REPRODUCIBLE A PROPOSITO: no lleva reloj, ni rutas temporales, ni
nada que cambie entre dos corridas seguidas, porque la bateria corre cada entrada
DOS VECES y coteja que las dos salidas sean identicas.

USO:
  python scripts/loop/vuelta183_tarea1b_mutacion_atribucion.py
"""
import hashlib
import importlib.util
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

SUJETO = os.path.join(AQUI, "vuelta183_bateria_por_tramos.py")
APERTURA = os.path.join(LOOP, "SALIDA_V183B_APERTURA.txt")

# EL NUMERO DEL CLON. No es el de ninguna vuelta real a proposito: si el fuente
# clavara un numero, el clon seguiria diciendo ese y no este, y el caso caeria.
CLON = 777

SALIDA = []


def w(linea=""):
    SALIDA.append(linea)


def caso(nombre, computado, esperado, esperado_mutado):
    """UN CASO CON SU MUTACION. `computado` sale de correr la funcion de verdad;
    `esperado` es lo que la casa afirma. Se comprueba que PASA con el esperado
    bueno y que CAE con el mutado, que es lo unico que prueba que el caso podia
    fallar."""
    pasa = computado == esperado
    cae = computado != esperado_mutado
    w("   %-56s %-5s %s"
      % (nombre, "PASA" if pasa else "FALLA", "CAE" if cae else "NO CAE"))
    if not pasa:
        w("      computado: %r" % (computado,))
        w("      esperado : %r" % (esperado,))
    return (0 if pasa else 1) + (0 if cae else 1)


def sha16(datos):
    return hashlib.sha256(datos).hexdigest()[:16]


def importar(ruta, nombre_modulo):
    """IMPORTA UN FICHERO PYTHON POR SU RUTA. El clon hace
    `sys.path.insert(0, AQUI)` con SU directorio, que es el temporal, asi que
    aqui se anade el de verdad para que sus dos imports resuelvan."""
    if AQUI not in sys.path:
        sys.path.insert(0, AQUI)
    spec = importlib.util.spec_from_file_location(nombre_modulo, ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    fallos = 0
    tmp = tempfile.mkdtemp(prefix="v183_t1b_atribucion_")
    try:
        fuente = io.open(SUJETO, encoding="utf-8").read().replace(chr(13) + NL, NL)

        w("=" * 78)
        w("ARNES DE LA CAIDA E.1: EL NUMERO DE VUELTA SE COMPUTA, NO SE CLAVA")
        w("scripts/loop/vuelta183_tarea1b_mutacion_atribucion.py")
        w("=" * 78)
        w("")

        w("A) LOS DOS FICHEROS DEL REPO QUE ESTE ARNES LEE, CON SU HUELLA")
        w("   scripts/loop/vuelta183_bateria_por_tramos.py -> %d bytes LF, sha256 %s"
          % (len(fuente.encode("utf-8")), sha16(fuente.encode("utf-8"))))
        w("   (es EL SUJETO BAJO PRUEBA: se mueve, y por eso su huella se imprime)")
        if os.path.exists(APERTURA):
            d_ap = io.open(APERTURA, "rb").read().replace(b"\r\n", b"\n")
            w("   docs/loop/SALIDA_V183B_APERTURA.txt -> %d bytes LF, sha256 %s"
              % (len(d_ap), sha16(d_ap)))
        else:
            w("   docs/loop/SALIDA_V183B_APERTURA.txt -> NO EXISTE")
        w("")

        w("B) LA FUNCION PURA QUE LEE EL NUMERO DE UN NOMBRE DE FICHERO")
        modulo = importar(SUJETO, "sujeto_bateria_real")
        f = modulo.numero_de_vuelta_del_nombre
        for nombre, esperado in (("vuelta183_bateria_por_tramos.py", 183),
                                 ("vuelta176_bateria_por_tramos.py", 176),
                                 ("vuelta777_bateria_por_tramos.py", 777),
                                 ("vuelta9_lo_que_sea.py", 9)):
            fallos += caso("numero de %-34s" % nombre, f(nombre), esperado,
                           esperado + 1)
        for nombre in ("bateria_por_tramos.py", "v183_bateria.py", ""):
            fallos += caso("un nombre sin numero de vuelta da None (%r)" % nombre,
                           f(nombre), None, 183)
        w("")

        w("C) EL MODULO REAL: SU NUMERO Y SU NOMBRE SALEN DE SU FICHERO")
        w("   LANZADOR computado: %s" % modulo.LANZADOR)
        w("   VUELTA  computada : %d" % modulo.VUELTA)
        fallos += caso("LANZADOR es el basename del propio fichero",
                       modulo.LANZADOR, os.path.basename(SUJETO),
                       "vuelta176_bateria_por_tramos.py")
        fallos += caso("VUELTA calza con el numero que dice su nombre",
                       modulo.VUELTA, f(os.path.basename(SUJETO)), 176)
        w("")

        w("D) EL GUARDA SOBRE EL FUENTE REAL: CERO LITERALES CLAVADOS")
        clavados = modulo.literales_de_vuelta_clavados(fuente)
        for i, linea, num in clavados:
            w("      LINEA %d clava %s: %s" % (i, linea[:110], num))
        fallos += caso("literales de vuelta clavados en el fuente real",
                       len(clavados), 0, 1)
        w("")

        w("E) LA MUTACION: SE CLAVA UN LITERAL Y EL GUARDA TIENE QUE MORDER")
        w("   Se inyecta una linea que escribe, con el numero clavado dentro, y")
        w("   se comprueba que el guarda la encuentra, con su numero y su sitio.")
        for numero_clavado in (183, 176, 200):
            inyectada = ('        f.write("CORRIDA DEL TRAMO 1 DE 9, BATERIA DE LA '
                         'VUELTA %d" + NL)' % numero_clavado)
            mutado = fuente + NL + inyectada + NL
            hallados = modulo.literales_de_vuelta_clavados(mutado)
            fallos += caso("clavando %d: el guarda encuentra 1" % numero_clavado,
                           len(hallados), 1, 0)
            if hallados:
                fallos += caso("clavando %d: y dice que numero es" % numero_clavado,
                               hallados[0][2], str(numero_clavado),
                               str(numero_clavado + 1))
                fallos += caso("clavando %d: y en que linea" % numero_clavado,
                               hallados[0][0], len(mutado.split(NL)) - 1,
                               1)
        w("   Y LAS OTRAS FORMAS DE CLAVARLO, QUE TAMBIEN TIENEN QUE MORDER:")
        for etiqueta, inyectada in (
                ("un print", '    print("BATERIA DE LA VUELTA 183")'),
                ("un cab.append", '    cab.append("compuesta por vuelta183_x.py")'),
                ("un mkdtemp", '    tmpdir = tempfile.mkdtemp(prefix="v183_t")'),
                ("un nombre de salida",
                 '    return "SALIDA_V183_BATERIA_TRAMO_%d.txt" % n')):
            hallados = modulo.literales_de_vuelta_clavados(fuente + NL + inyectada + NL)
            fallos += caso("%s con el numero clavado muerde" % etiqueta,
                           len(hallados), 1, 0)
        w("   Y LO QUE NO TIENE QUE MORDER, PARA QUE EL GUARDA NO SEA UN CEPO:")
        for etiqueta, inyectada in (
                ("una linea que no escribe", '    x = "vuelta183_algo.py"'),
                ("un comentario", '    # la vuelta 183 hizo esto'),
                ("el nombre ya computado",
                 '    return "SALIDA_V%d_BATERIA_TRAMO_%d.txt" % (VUELTA, n)')):
            hallados = modulo.literales_de_vuelta_clavados(fuente + NL + inyectada + NL)
            fallos += caso("%s NO muerde" % etiqueta, len(hallados), 0, 1)
        w("")

        w("F) LA EXENCION DE LA CITA HISTORICA, QUE SE NOMBRA Y NO SE ENSANCHA")
        cita = ('    print("(encargo de la vuelta 176, TAREA 1.f)")'
                '   # %s' % modulo.MARCA_CITA)
        sin_marca = '    print("(encargo de la vuelta 176, TAREA 1.f)")'
        fallos += caso("la misma linea SIN la marca muerde",
                       len(modulo.literales_de_vuelta_clavados(sin_marca)), 1, 0)
        fallos += caso("la misma linea CON la marca queda exenta",
                       len(modulo.literales_de_vuelta_clavados(cita)), 0, 1)
        w("")

        w("G) LAS CUATRO FRASES PURAS, SOBRE NUMEROS FABRICADOS")
        fallos += caso("titulo_de_corrida(3, 9, 183)",
                       modulo.titulo_de_corrida(3, 9, 183),
                       "CORRIDA DEL TRAMO 3 DE 9, BATERIA DE LA VUELTA 183",
                       "CORRIDA DEL TRAMO 3 DE 9, BATERIA DE LA VUELTA 176")
        fallos += caso("titulo_de_corrida(3, 9, 776)",
                       modulo.titulo_de_corrida(3, 9, 776),
                       "CORRIDA DEL TRAMO 3 DE 9, BATERIA DE LA VUELTA 776",
                       "CORRIDA DEL TRAMO 3 DE 9, BATERIA DE LA VUELTA 183")
        fallos += caso("linea_de_lanzador de un nombre fabricado",
                       modulo.linea_de_lanzador("vuelta776_x.py"),
                       "lanzada por scripts/loop/vuelta776_x.py",
                       "lanzada por scripts/loop/vuelta176_bateria_por_tramos.py")
        fallos += caso("titulo_de_composicion(776)",
                       modulo.titulo_de_composicion(776),
                       "LA BATERIA DE MUTACIONES DE LA VUELTA 776, CORRIDA ENTERA "
                       "Y EN TRAMOS",
                       "LA BATERIA DE MUTACIONES DE LA VUELTA 176, CORRIDA ENTERA "
                       "Y EN TRAMOS")
        fallos += caso("linea_de_composicion de un nombre fabricado",
                       modulo.linea_de_composicion("vuelta776_x.py"),
                       "compuesta por scripts/loop/vuelta776_x.py --componer",
                       "compuesta por scripts/loop/vuelta176_bateria_por_tramos.py "
                       "--componer")
        w("")

        w("H) EL CLON: EL MISMO FUENTE CON OTRO NOMBRE TIENE QUE DECIR OTRO NUMERO")
        w("   Es la prueba de que la variable esta COMPUTADA: si el numero")
        w("   estuviera clavado, el clon seguiria diciendo 183 y esto caeria.")
        ruta_clon = os.path.join(tmp, "vuelta%d_bateria_por_tramos.py" % CLON)
        io.open(ruta_clon, "w", encoding="utf-8", newline=NL).write(fuente)
        clon = importar(ruta_clon, "clon_bateria_%d" % CLON)
        w("   clon llamado: vuelta%d_bateria_por_tramos.py" % CLON)
        w("   VUELTA que el clon computa: %d" % clon.VUELTA)
        fallos += caso("el clon computa su propio numero", clon.VUELTA, CLON, 183)
        fallos += caso("el clon computa su propio nombre", clon.LANZADOR,
                       "vuelta%d_bateria_por_tramos.py" % CLON,
                       "vuelta183_bateria_por_tramos.py")
        fallos += caso("nombre_tramo del clon",
                       clon.nombre_tramo(1),
                       "SALIDA_V%d_BATERIA_TRAMO_1.txt" % CLON,
                       "SALIDA_V183_BATERIA_TRAMO_1.txt")
        fallos += caso("nombre_transcripcion del clon",
                       clon.nombre_transcripcion(2),
                       "SALIDA_V%d_LANZADOR_TRAMO_2.txt" % CLON,
                       "SALIDA_V183_LANZADOR_TRAMO_2.txt")
        fallos += caso("nombre_de_la_compuesta del clon",
                       clon.nombre_de_la_compuesta(),
                       "SALIDA_V%d_BATERIA.txt" % CLON,
                       "SALIDA_V183_BATERIA.txt")
        fallos += caso("la primera linea que el clon sellaria",
                       clon.titulo_de_corrida(1, 9, clon.VUELTA),
                       "CORRIDA DEL TRAMO 1 DE 9, BATERIA DE LA VUELTA %d" % CLON,
                       "CORRIDA DEL TRAMO 1 DE 9, BATERIA DE LA VUELTA 176")
        fallos += caso("la segunda linea que el clon sellaria",
                       clon.linea_de_lanzador(clon.LANZADOR),
                       "lanzada por scripts/loop/vuelta%d_bateria_por_tramos.py" % CLON,
                       "lanzada por scripts/loop/vuelta176_bateria_por_tramos.py")
        w("")

        w("I) LA MUTACION SOBRE LA VARIABLE COMPUTADA: SE CLAVA EL NUMERO EN EL")
        w("   CLON Y EL ARNES TIENE QUE CAER. Es el caso que el encargo pide con")
        w("   estas palabras: 'el arnes tiene que CAER si alguien vuelve a clavar")
        w("   el numero de vuelta como literal'.")
        linea_viva = "VUELTA = int(_M_VUELTA.group(1))"
        linea_muerta = "VUELTA = 183   # CLAVADO A MANO, QUE ES LA MUTACION"
        fallos += caso("la linea que computa el numero esta en el fuente",
                       fuente.count(linea_viva), 1, 0)
        fuente_clavado = fuente.replace(linea_viva, linea_muerta, 1)
        ruta_clavado = os.path.join(tmp, "vuelta%d_bateria_por_tramos.py" % (CLON + 1))
        io.open(ruta_clavado, "w", encoding="utf-8", newline=NL).write(fuente_clavado)
        clavado = importar(ruta_clavado, "clon_clavado_%d" % (CLON + 1))
        w("   clon llamado: vuelta%d_bateria_por_tramos.py" % (CLON + 1))
        w("   VUELTA que el clon con el literal clavado dice: %d" % clavado.VUELTA)
        w("   VUELTA que su NOMBRE dice: %d" % (CLON + 1))
        fallos += caso("EL ARNES CAE: el clavado NO computa su numero",
                       clavado.VUELTA == f(clavado.LANZADOR), False, True)
        fallos += caso("EL ARNES CAE: y sella con el numero de otra vuelta",
                       clavado.nombre_tramo(1),
                       "SALIDA_V183_BATERIA_TRAMO_1.txt",
                       "SALIDA_V%d_BATERIA_TRAMO_1.txt" % (CLON + 1))
        fallos += caso("EL ARNES CAE: y su primera linea sellada miente",
                       clavado.titulo_de_corrida(1, 9, clavado.VUELTA),
                       "CORRIDA DEL TRAMO 1 DE 9, BATERIA DE LA VUELTA 183",
                       "CORRIDA DEL TRAMO 1 DE 9, BATERIA DE LA VUELTA %d" % (CLON + 1))
        w("   Y EL CLON SANO, AL LADO, PARA QUE LA DIFERENCIA SE VEA:")
        fallos += caso("el clon sano SI computa su numero",
                       clon.VUELTA == f(clon.LANZADOR), True, False)
        w("")

        w("J) EL LANZADOR SE NIEGA A ARRANCAR CON UN LITERAL CLAVADO")
        w("   No basta con que una funcion pura lo vea: el proceso tiene que")
        w("   PARARSE. Se corre cada clon con --siguiente, que no escribe nada.")
        entorno = dict(os.environ)
        entorno["PYTHONPATH"] = AQUI + os.pathsep + entorno.get("PYTHONPATH", "")
        entorno["PYTHONIOENCODING"] = "utf-8"

        def correr(ruta):
            r = subprocess.run([sys.executable, ruta, "--siguiente"],
                               capture_output=True, env=entorno, cwd=RAIZ)
            return r.returncode, (r.stdout + r.stderr).decode("utf-8", errors="replace")

        cod_sano, out_sano = correr(ruta_clon)
        fallos += caso("el clon sano arranca (exitcode 0)", cod_sano, 0, 1)
        fallos += caso("y su guarda dice cero clavados",
                       "CIFRA literales de vuelta clavados en lineas que escriben: 0"
                       in out_sano, True, False)

        inyectada = ('    print("BATERIA DE LA VUELTA 183, CLAVADA A MANO")'
                     + NL + "")
        fuente_print = fuente.replace(
            "def main():", inyectada + NL + "def main():", 1)
        ruta_print = os.path.join(tmp, "vuelta%d_bateria_por_tramos.py" % (CLON + 2))
        io.open(ruta_print, "w", encoding="utf-8", newline=NL).write(fuente_print)
        cod_malo, out_malo = correr(ruta_print)
        fallos += caso("EL ARNES CAE: el clon con el literal clavado NO arranca",
                       cod_malo, 1, 0)
        fallos += caso("y lo dice en rojo y con su cuenta",
                       "ROJO: hay 1 literal(es) de vuelta clavados" in out_malo,
                       True, False)
        fallos += caso("y nombra la linea que lo clava",
                       "clava 183" in out_malo, True, False)
        w("   exitcode del clon sano: %d | exitcode del clon clavado: %d"
          % (cod_sano, cod_malo))
        w("")

        w("K) UN NOMBRE QUE NO DICE SU VUELTA NO SE ADIVINA: EL MODULO SE NIEGA")
        ruta_sin = os.path.join(tmp, "bateria_sin_numero.py")
        io.open(ruta_sin, "w", encoding="utf-8", newline=NL).write(fuente)
        try:
            importar(ruta_sin, "clon_sin_numero")
            salto = False
            mensaje = ""
        except SystemExit as e:
            salto = True
            mensaje = str(e)
        fallos += caso("importar un clon sin numero en el nombre levanta SystemExit",
                       salto, True, False)
        fallos += caso("y el mensaje dice que NO SE ADIVINA",
                       "NO SE ADIVINA" in mensaje, True, False)
        w("")

        w("L) LO QUE PASABA ANTES, CONTADO Y NO BORRADO")
        w("   La cuenta la hizo el bloque de apertura de esta continuacion ANTES")
        w("   de que nadie tocara el lanzador, y se lee de su fichero sellado.")
        if os.path.exists(APERTURA):
            t_ap = io.open(APERTURA, encoding="utf-8", errors="replace").read()
            t_ap = t_ap.replace(chr(13) + NL, NL)
            marca = "CIFRA total de lineas con '176' en las cuatro salidas selladas:"
            lineas_marca = [l.strip() for l in t_ap.split(NL) if marca in l]
            for l in lineas_marca:
                w("      | %s" % l)
            contado = (int(lineas_marca[0].rsplit(":", 1)[1])
                       if lineas_marca else -1)
            fallos += caso("la apertura conto las menciones de 176 antes de tocar",
                           contado > 0, True, False)
            por_fichero = re.findall(r"lineas con '176': (\d+)", t_ap)
            w("      por fichero: %s" % ", ".join(por_fichero))
            fallos += caso("y son cuatro ficheros los que la traen",
                           len(por_fichero), 4, 3)
            fallos += caso("y la suma de los cuatro calza con el total",
                           sum(int(x) for x in por_fichero), contado, contado + 1)
        else:
            w("      LA APERTURA NO ESTA EN DISCO. No se inventa ninguna cifra.")
            fallos += 1
        w("")

        w("=" * 78)
        w("CIFRA casos con mutacion corridos: los de arriba, uno por linea")
        w("CIFRA fallos: %d" % fallos)
        w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
        w("=" * 78)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    t = NL.join(SALIDA) + NL
    ruta = os.path.join(LOOP, "SALIDA_V183_T1B_MUTACION_ATRIBUCION.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
