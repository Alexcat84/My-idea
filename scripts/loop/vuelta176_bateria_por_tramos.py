# -*- coding: utf-8 -*-
r"""vuelta176_bateria_por_tramos.py . CORRE LA BATERIA ENTERA A BOCADOS, CON LA
GUARDA DEL COMMIT DELANTE Y CON RESTAURACION AL ENTRAR DE CADA TRAMO.

DESCENDIENTE DECLARADO de `scripts/loop/vuelta175_correr_bateria.py`, del que
CONSERVA ENTERO lo que ya funcionaba y esta medido: el lanzamiento con `-u` (sin
buffer), la escritura LINEA A LINEA con `flush()`, el fichero de trabajo FUERA de
`docs/loop/` para no fabricar ruido de concurrencia, la medicion de la salida
(bytes, lineas, sha256) ANTES de nombrarla en ningun sitio, el rojo si midiera
cero bytes, el reloj de pared por los dos extremos y la propagacion tal cual del
exitcode de la bateria.

LO QUE ANADE, Y ES LO UNICO QUE ANADE: que no sea un solo bocado.

POR QUE, Y LA CAUSA ESTA MEDIDA Y NO SUPUESTA. La vuelta 175 murio DENTRO de la
bateria. Su lanzador ya habia arreglado el sintoma del fichero de cero bytes,
pero no la enfermedad: con la nomina en 87 entradas y CADA UNA CORRIDA DOS VECES
(el cotejo de reproducibilidad de la TAREA 2.f de la vuelta 141), la corrida es
UN BLOQUE INDIVISIBLE de entre 57 y 75 minutos, contado sobre las cifras del
propio archivo (0,33 minutos por entrada de media, y 0,43 en la ultima corrida
con cuerpo, la del auditor de la 171: 75 entradas en 32,5 minutos). Un bloque asi
se come la vuelta entera, y si algo lo corta se pierde TODO.

LAS CUATRO COSAS QUE LA LETRA DEL FUNDADOR DEL 5 SEP FIJA NO SE TOCAN, Y SE
DICEN UNA A UNA PARA QUE SE PUEDA COMPROBAR: la CADENCIA (la bateria corre cada
cinco vueltas) sigue igual; la SOLEDAD (vuelta propia que no lleva nada mas)
sigue igual; la INTEGRIDAD (entera, doble corrida, ninguna guarda aflojada) sigue
igual, y cada entrada sigue corriendo y sigue corriendo DOS VECES; y la NOMINA NO
SE PODA. LO QUE SE PARTE ES EL BOCADO.

LOS CINCO PASOS DE CADA TRAMO, EN ESTE ORDEN:

  1. LA GUARDA DEL COMMIT, `scripts/loop/guarda_commit_dataset.py`, corrida como
     funcion y no prometida. Si `dataset/` trae una sola fila, el tramo NO
     empieza.
  2. LA RESTAURACION AL ENTRAR. Si el paso 1 encontro suciedad, se restaura con
     `git checkout --` sobre los ficheros QUE GIT NOMBRE (nunca sobre una lista
     tecleada) y SE VUELVE A MEDIR hasta que de cero filas. UN `finally` NO
     SOBREVIVE A QUE MATEN EL PROCESO; UNA COMPROBACION AL ENTRAR, SI. Esa es la
     leccion entera de la 175 y por eso este paso va aqui y no en un `finally`.
  3. LA CORRIDA DEL TRAMO, con `--tramo N --tamano-tramo K`, sin buffer y con
     escritura linea a linea a un fichero de trabajo fuera de `docs/loop/`.
  4. EL SELLADO Y LA MEDICION. La salida del tramo se copia a
     `docs/loop/SALIDA_V176_BATERIA_TRAMO_<N>.txt` y se MIDE antes de nombrarla:
     si midiera cero bytes, ROJO y la ruta no se publica.
  5. LA COMPROBACION DE SALIDA. Se vuelve a correr la guarda del commit DESPUES
     del tramo, porque un tramo que deje `dataset/` sucio tiene que verse aqui y
     no tres pasos mas tarde.

SI UN TRAMO SALE EN ROJO, ESTE FICHERO PARA AHI Y NO SIGUE, y no lo re-corre: la
guarda que muerde es informacion, no un estorbo (letra del encargo de la 176,
TAREA 1.f).

LA COMPOSICION (`--componer`) es un acto aparte y desconfiado: no se fia de que
los tramos existan, sino que LEE de cada salida las lineas
`ENTRADA DEL TRAMO: <arnes>` que la bateria imprime, y exige que la UNION de
todas sea la nomina ENTERA, cada entrada EXACTAMENTE UNA VEZ. Si sobra o falta
una, NO compone y lo dice. Solo entonces pega los tramos en
`docs/loop/SALIDA_V176_BATERIA.txt` y lo mide.

USO:
  python scripts/loop/vuelta176_bateria_por_tramos.py --plan
  python scripts/loop/vuelta176_bateria_por_tramos.py --tramo 1
  python scripts/loop/vuelta176_bateria_por_tramos.py --componer
"""
import argparse
import datetime
import hashlib
import io
import os
import subprocess
import sys
import tempfile
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
BATERIA = os.path.join(AQUI, "verificar_mutaciones_viejas.py")
NL = chr(10)

sys.path.insert(0, AQUI)
import guarda_commit_dataset as GUARDA   # noqa: E402
import verificar_mutaciones_viejas as B   # noqa: E402

TAMANO = 10
MARCA_ENTRADA = "ENTRADA DEL TRAMO: "


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
    return "SALIDA_V176_LANZADOR_TRAMO_%d.txt" % n


def ahora_utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def nombre_tramo(n):
    return "SALIDA_V176_BATERIA_TRAMO_%d.txt" % n


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
    print("TRAMO %d DE %d, DE LA BATERIA DE LA VUELTA 176" % (n, len(tramos)))
    print("=" * 78)
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
    tmpdir = tempfile.mkdtemp(prefix="v176_tramo%d_" % n)
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
        f.write("CORRIDA DEL TRAMO %d DE %d, BATERIA DE LA VUELTA 176" % (n, len(tramos)) + NL)
        f.write("lanzada por scripts/loop/vuelta176_bateria_por_tramos.py" + NL)
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
        print("(encargo de la 176, TAREA 1.f). La salida esta sellada y medida.")
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

    destino = os.path.join(LOOP, "SALIDA_V176_BATERIA.txt")
    cab = []
    cab.append("LA BATERIA DE MUTACIONES DE LA VUELTA 176, CORRIDA ENTERA Y EN TRAMOS")
    cab.append("compuesta por scripts/loop/vuelta176_bateria_por_tramos.py --componer")
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
    print("   docs/loop/SALIDA_V176_BATERIA.txt")
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
    print("  ESTIMACION minutos por tramo de %d entradas: entre %.1f y %.1f"
          % (TAMANO, TAMANO * 0.33, TAMANO * 0.43))
    print("  ESTIMACION minutos de la nomina entera: entre %.1f y %.1f"
          % (len(B.VIEJAS) * 0.33, len(B.VIEJAS) * 0.43))
    print("  LA MEDICION DE VERDAD LA DA CADA TRAMO AL CERRARSE, y es la que se")
    print("  publica. Esto es solo el reparto.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramo", type=int, default=None, help="corre el tramo N")
    ap.add_argument("--componer", action="store_true",
                    help="compone la salida unica de los tramos ya sellados")
    ap.add_argument("--plan", action="store_true",
                    help="imprime el reparto y no corre nada")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    tramos = B.reparto_en_tramos(B.VIEJAS, TAMANO)

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
    tmpdir = tempfile.mkdtemp(prefix="v176_lanzador%d_" % a.tramo)
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
