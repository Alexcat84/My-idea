# -*- coding: utf-8 -*-
r"""_v220_t1_registros.py . LA TAREA 1 DE LA VUELTA 220: LOS REGISTROS.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). NO ES ARNES NI GUARDA NI LECTOR NUEVO:
ES LECTURA, MEDICION Y REGISTRO, que es lo que la moratoria protege.

  1.a  LAS SEIS ADJUDICACIONES DEL ACTA 219, cada una con su rotulo, su numero
       de adjudicacion y SU LINEA LEIDA DEL FICHERO. Las lineas NO SE TECLEAN:
       el instrumento busca el ancla en docs/loop/ACTA_AUDITOR.md, publica su
       numero de linea y su texto verbatim, y CAE EN ROJO si un ancla no
       aparece o aparece mas de una vez.

  1.b  EL RECUENTO NUEVO, CON LAS DOS CIFRAS JUNTAS Y DICIENDO CUAL ES CUAL.
       La primera se MIDE HOY re-corriendo el lector de la 219
       (_v219_t2_lecturas.py) como subproceso y leyendo sus tres lineas de
       CIFRA; la segunda es la que la adjudicacion 4.5 del acta 219 deja, y se
       COMPUTA aplicando esa unica subida sobre la tabla de 17 filas que el
       propio lector imprime. NO SE TOCA docs/plan/08_VERIFICACION.md: la celda
       es sede del fundador y la divergencia sube nombrada.
       Y SE PRUEBA QUE EL LECTOR ES LECTOR: se sellan los sha256 de nueve
       ficheros antes de correrlo y se cotejan despues, que es la misma
       medicion con la que el acta 219 adjudico su 4.2.

  1.c  LAS SIETE COSAS QUE SUBEN NOMBRADAS A LA AUDITORIA INTEGRAL, con su
       cifra y su linea leida de la seccion 6 del acta 219, y la PRIMERA con
       SUS TRES OPCIONES leidas del fichero. NO SE RESUELVE NINGUNA.

EL CASO ROJO NO SE PROMETE Y SE DICE CUAL ES CUAL (EJECUTOR.md 1, EL CASO ROJO
SE PRUEBA POR MUTACION). La localizacion de las lineas de acta, la re-corrida
del lector, el cotejo de los sha y la aritmetica del recuento son MAQUINA de
punta a punta y CAEN EN ROJO por si solas. La glosa de cada adjudicacion es
MIA, sale de la tabla que el encargo me dicta, y va firmada como tal: para esa
parte NO HAY CASO ROJO AUTOMATICO, y se declara en vez de fabricarse uno que se
apruebe solo.

CERO ESCRITURAS EN EL PLAN: esta tarea solo lee.

USO:  python scripts/loop/_v220_t1_registros.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

ACTA = "docs/loop/ACTA_AUDITOR.md"
EXPEDIENTE = "docs/plan/OPERACIONES.jsonl"
PAG08 = "docs/plan/08_VERIFICACION.md"
PAG07 = "docs/plan/07_ADUANA.md"
PAG01 = "docs/plan/01_FUENTES.md"
PAG05 = "docs/plan/05_SANEO.md"
PAG03 = "docs/plan/03_FUSIONES.md"
INVENTARIO = "docs/plan/INVENTARIO.jsonl"
VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
GRAFO = "dataset/metadata/master_graph.json"

SEDES = (EXPEDIENTE, PAG08, PAG07, PAG01, PAG05, PAG03, INVENTARIO)

# LOS NUEVE FICHEROS QUE SE SELLAN ANTES DE RE-CORRER EL LECTOR DE LA 219, que
# son las seis sedes del plan, el registro del cribado, el grafo y la propia
# salida sellada del lector. Es la misma medicion con que el acta 219 adjudico
# su 4.2 (linea 77907, leida en esta vuelta del fichero).
NUEVE = (EXPEDIENTE, PAG08, PAG07, PAG01, PAG05, INVENTARIO, VEREDICTOS, GRAFO,
         "docs/loop/SALIDA_V219_T2_LECTURAS.txt")

# EL ANCLA NO ES LA RESPUESTA: es DONDE MIRAR. El numero de linea lo pone el
# fichero, no yo. La columna "que se sostiene" es la del encargo, resumida, y
# va firmada como glosa mia.
ADJUDICACIONES = [
    ("TAREA 1 D.1", "4.1",
     "remedir no era recomputar: el mismo instrumento es el mismo instrumento, "
     "y el auditor ademas re-corrio mi lector y salio identico",
     "**`4.1` TAREA 1 `D.1` A FAVOR"),
    ("TAREA 1 D.2", "4.2",
     "no se adjudico por mi palabra: se midio. Sello del sha256 de nueve "
     "ficheros, corrida de _v219_t2_lecturas.py, y CERO se movieron. No es la "
     "especie de la C.3 de la 218",
     "**`4.2` TAREA 1 `D.2` A FAVOR"),
    ("TAREA 1 D.3", "4.3",
     "la glosa es registro y no lectura mia, y decir esto no lo he vuelto a "
     "medir yo se cuenta a favor",
     "**`4.3` TAREA 1 `D.3` A FAVOR"),
    ("TAREA 2 D.1", "4.4",
     "01 FUENTES idx 1 se sostiene en CUBRE, con la prueba que yo no use: "
     "P.19 punto 2 deja el nodo MULTIFUENTE LEGITIMO y sus dos ejemplares "
     "nombrados son coeficiente_viral y decision_de_vender_startup, dos de los "
     "cinco de mi tabla",
     "**`4.4` TAREA 2 `D.1` A FAVOR"),
    ("TAREA 2 D.2 y P.1", "4.5",
     "LA FRONTERA ADJUDICADA: el tercero queda FUERA DEL ALCANCE. El punto de "
     "verificacion de 05 SANEO idx 1 se acota POR CORRECCION DECLARADA a los "
     "dos nodos que OP-S-02 alcanza, y 05 SANEO idx 1 SUBE A CUBRE",
     "**`4.5` TAREA 2 `D.2` Y `P.1`"),
    ("TAREA 2 D.3", "4.6",
     "el reparto de tanda a libro es mio, con su guarda, y decir el limite de "
     "la propia guarda es lo contrario de venderla como mordiendo",
     "**`4.6` TAREA 2 `D.3` A FAVOR"),
]

# LAS SIETE DE LA SECCION 6 DEL ACTA 219. Otra vez: ancla, no respuesta.
INTEGRAL = [
    ("1", "la familia C.1 del auditor en NUEVE actas seguidas, con TRES "
          "mediciones de fallo del remedio del fundador, y SUBE CON TRES "
          "OPCIONES concretas",
     "1. **MI FAMILIA `C.1` EN NUEVE"),
    ("2", "DOS divergencias, ya no una, entre la pagina 08 del plan y lo "
          "adjudicado: la linea 30 dice CUATRO controles y su ficha OP-A-02 "
          "dice CINCO (tercera acta seguida), y la linea 28 lleva desde el "
          "acta 219 el punto de verificacion de 05 SANEO idx 1 acotado por "
          "correccion declarada y su texto sin acotar",
     "2. **DOS DIVERGENCIAS, YA NO UNA"),
    ("3", "el carril del lanzador de la bateria que dice cual tramo toca no "
          "distingue la vuelta de las salidas que mira, y hoy responde que no "
          "falta ningun tramo; hermano del rotulo de la salida compuesta, que "
          "dice VUELTA 183 sobre el contenido de la 215",
     "3. **`--siguiente` DEL LANZADOR DE LA BATERIA NO DISTINGUE"),
    ("4", "scripts/loop/vuelta150_4_tabla_por_fase.py en rojo, AssertionError "
          "la tabla no trae ocho filas: 11, y queda por decidir si se repara o "
          "si su vara de ocho filas se retira",
     "4. **`scripts/loop/vuelta150_4_tabla_por_fase.py` en rojo**"),
    ("5", "la ciega no puede acertar lo que el archivo decide por BARRIDO DE "
          "FAMILIA, por transitividad sobre veredictos de otros puestos: NUEVE "
          "de los catorce fallos del auditor son de esa especie",
     "5. **LA CIEGA NO PUEDE ACERTAR LO QUE SE DECIDE POR BARRIDO DE FAMILIA"),
    ("6", "las DOS clausulas que quedan, con su cifra: 03 FUSIONES idx 0 (71 "
          "actos sin fundir por la lectura ancha, SEIS fusiones de 19 nodos "
          "por la estrecha) y 07 ADUANA idx 0 (el quinto control sin correr, "
          "mas la celda del punto 2)",
     "6. **LAS DOS CLAUSULAS QUE QUEDAN, CON SU CIFRA:**"),
    ("7", "el remedio de dictado de mi C.4, en mis propias palabras: la pareja "
          "de bytes no es una regla de RUTAS, es una regla de CIFRAS DE BYTES, "
          "vengan de una ruta o de un campo de texto",
     "7. **EL REMEDIO DE DICTADO DE LA `C.4`"),
]

# LA SUBIDA QUE LA ADJUDICACION 4.5 ORDENA, Y ES LA UNICA. No la decido yo: la
# decide el acta 219 y aqui solo se aplica sobre la tabla que el lector imprime.
SUBIDA_POR_ADJUDICACION = {("05 SANEO", 1): "CUBRE"}

LECTOR_219 = "scripts/loop/_v219_t2_lecturas.py"
SALIDA_LECTOR_219 = "docs/loop/SALIDA_V219_T2_LECTURAS.txt"


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def sha16(rel):
    b = io.open(os.path.join(RAIZ, rel.replace("/", os.sep)), "rb").read()
    return (hashlib.sha256(b).hexdigest()[:16],
            hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16])


def bytes_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    b = io.open(p, "rb").read()
    return os.path.getsize(p), len(b.replace(b"\r\n", b"\n"))


def localizar(lineas, ancla, desde=1):
    """DONDE VIVE UN ANCLA EN UN FICHERO YA LEIDO. PURA.

    Devuelve la lista de numeros de linea (base 1) a partir de `desde` cuyo
    texto EMPIEZA por el ancla. Una lista que no tenga exactamente un elemento
    es un fallo del que la llama, y aqui se cuenta como tal."""
    return [n for n, l in enumerate(lineas, start=1)
            if n >= desde and l.startswith(ancla)]


def filas_de_la_tabla(texto):
    """LAS 17 FILAS DE LA TABLA DEL CIERRE DE UNA SALIDA DEL LECTOR. PURA:
    recibe el texto y no lee nada. Devuelve [[n, fila, idx, veredicto, glosa]].

    El veredicto se limpia de la coletilla entre parentesis que el lector anade
    cuando una clausula subio por lectura, porque lo que aqui se cuenta es la
    clase y no su historia."""
    filas = []
    dentro = False
    for l in texto.split(NL):
        if "LA TABLA ENTERA AL CIERRE DE ESTA TAREA" in l:
            dentro = True
            continue
        if not dentro:
            continue
        m = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*"
                     r"(CUBRE|A MEDIAS|NO CUBRE)(?:[^|]*)\|\s*(.*?)\s*\|$", l)
        if m:
            filas.append([int(m.group(1)), m.group(2), int(m.group(3)),
                          m.group(4), m.group(5)])
        elif filas and not l.startswith("|"):
            break
    return filas


def reparto(filas):
    """CUANTAS HAY DE CADA CLASE. PURA."""
    r = {"CUBRE": 0, "A MEDIAS": 0, "NO CUBRE": 0}
    for f in filas:
        r[f[3]] = r.get(f[3], 0) + 1
    return r


# LA MARCA DE LA UNICA LINEA DE LA SALIDA DEL LECTOR DE LA 219 QUE PUEDE
# CAMBIAR SIN QUE SEA ROJO, y se nombra aqui y no en prosa para que la prueba
# de mutacion la pueda tumbar.
MARCA_CONTEO_DEL_ACTA = "LOS DOS FICHEROS DE LAS CITAS, MEDIDOS HOY"


def lineas_que_difieren(viejo, nuevo):
    """LAS LINEAS EN QUE DOS TEXTOS SE SEPARAN. PURA. Devuelve
    [(numero_de_linea, la_vieja, la_nueva)], con la cadena vacia donde a un
    lado le falte la linea."""
    a = viejo.split(NL)
    b = nuevo.split(NL)
    difs = []
    for i in range(max(len(a), len(b))):
        va = a[i] if i < len(a) else ""
        vb = b[i] if i < len(b) else ""
        if va != vb:
            difs.append((i + 1, va, vb))
    return difs


def juicio_del_movimiento(movidos, difs, nombre_propio):
    """QUE DE LO QUE SE MOVIO AL RE-CORRER EL LECTOR ES ROJO. PURA: recibe la
    lista de ficheros movidos, las lineas que difieren en la salida propia del
    lector y el nombre de esa salida propia. Devuelve la lista de motivos de
    ROJO, VACIA si no hay ninguno.

    --- POR QUE ESTA FUNCION EXISTE, Y ES CORRECCION DECLARADA DENTRO DE LA
    PROPIA VUELTA 220. EL TEXTO VIEJO NO SE BORRA, SE CUENTA ---

    LA PRIMERA VERSION DE ESTA GUARDA CONTABA CUALQUIER MOVIMIENTO COMO ROJO A
    SECAS, y me lo canto: al re-correr scripts/loop/_v219_t2_lecturas.py hoy,
    SU PROPIA SALIDA SELLADA SE MOVIO. El acta 219, en su adjudicacion 4.2
    (linea 77907 de docs/loop/ACTA_AUDITOR.md, leida en esta vuelta), dice que
    el auditor sello nueve ficheros, corrio ese mismo lector y CERO SE
    MOVIERON. LAS DOS MEDICIONES SON CIERTAS Y NO SE CONTRADICEN: el lector
    imprime EL NUMERO DE LINEAS QUE EL ACTA TIENE HOY, y entre la corrida del
    auditor y la mia el acta crecio con el acta 219 entera. La diferencia es de
    FECHA DE CORTE, no de conducta del lector.

    LO QUE LA REGLA NUEVA EXIGE ES MAS, NO MENOS, Y POR ESO NO ES UNA GUARDA
    AFLOJADA: sigue siendo ROJO que se mueva CUALQUIER fichero que no sea la
    propia salida del lector; y de la propia salida se exige ademas que la
    diferencia sea DE UNA SOLA LINEA y que esa linea sea la del conteo del
    acta. Dos lineas distintas, o una sola que no sea esa, siguen siendo ROJO."""
    motivos = []
    ajenos = [m for m in movidos if m != nombre_propio]
    if ajenos:
        motivos.append("SE MOVIERON FICHEROS QUE NO SON LA SALIDA DEL PROPIO "
                       "LECTOR, y eso es ROJO sin matices: %s"
                       % ", ".join(ajenos))
    if nombre_propio in movidos:
        if len(difs) != 1:
            motivos.append("la salida del propio lector difiere en %d linea(s) "
                           "y solo se admite UNA, la del conteo del acta"
                           % len(difs))
        else:
            _n, vieja, nueva = difs[0]
            if (MARCA_CONTEO_DEL_ACTA not in vieja
                    or MARCA_CONTEO_DEL_ACTA not in nueva):
                motivos.append("la unica linea que difiere en la salida del "
                               "propio lector NO es la del conteo del acta")
    return motivos


def main():
    out = []
    fallos = 0

    def w(s=""):
        out.append(s)

    w("=" * 78)
    w("TAREA 1 DE LA VUELTA %d: LOS REGISTROS. LECTURA, MEDICION Y REGISTRO."
      % VUELTA)
    w("=" * 78)
    w("")
    w("LOS SHA256 DE LAS SEDES DEL PLAN, AL ENTRAR, POR LAS DOS CONVENCIONES:")
    entrada = {}
    for rel in SEDES:
        entrada[rel] = sha16(rel)
        bd, bl = bytes_de(rel)
        w("   %s: %d bytes en disco y %d normalizado a LF, sha256 disco %s y "
          "sha256 LF %s" % ((rel, bd, bl) + entrada[rel]))
    w("")

    lineas_acta = leer(ACTA).split(NL)
    w("EL FICHERO DE LAS CITAS, MEDIDO HOY: %s, %d lineas leidas."
      % (ACTA, len(lineas_acta)))
    ancla_219 = localizar(lineas_acta, "# ACTA DEL AUDITOR, VUELTA 219:")
    w("CIFRA lineas donde empieza el acta 219: %d | CIFRA que se exige: 1"
      % len(ancla_219))
    if len(ancla_219) != 1:
        fallos += 1
        inicio = 1
    else:
        inicio = ancla_219[0]
        w("   EL ACTA 219 EMPIEZA EN LA LINEA %d, y el encargo dice 77727: %s"
          % (inicio, "CALZA" if inicio == 77727 else "NO CALZA"))
        if inicio != 77727:
            fallos += 1
    w("")

    # =================================================================== 1.a
    w("=" * 78)
    w("1.a. LAS SEIS ADJUDICACIONES DEL ACTA 219, CON SU LINEA LEIDA DEL "
      "FICHERO")
    w("=" * 78)
    w("")
    w("   LA LINEA NO SE TECLEA: se localiza el ancla en %s a partir de la "
      "linea %d y se publica su numero y su texto verbatim." % (ACTA, inicio))
    w("")
    filas_adj = []
    for rot, num, sostiene, ancla in ADJUDICACIONES:
        donde = localizar(lineas_acta, ancla, desde=inicio)
        w("   ADJUDICACION %-4s (rotulo %-18s) | CIFRA lineas que casan el "
          "ancla: %d | CIFRA que se exige: 1" % (num, rot, len(donde)))
        if len(donde) != 1:
            fallos += 1
            w("      ROJO: el ancla %r no aparece exactamente una vez." % ancla)
            continue
        n = donde[0]
        w("      LINEA %d, LEIDA DEL FICHERO> %s" % (n, lineas_acta[n - 1]))
        w("      LO QUE SOSTIENE (glosa mia, con las palabras del encargo): %s"
          % sostiene)
        filas_adj.append((rot, num, n, sostiene))
    w("")
    w("   CIFRA adjudicaciones localizadas con su linea: %d | CIFRA que el "
      "encargo lista: 6" % len(filas_adj))
    if len(filas_adj) != 6:
        fallos += 1
    w("")
    w("   LA TABLA DE LAS SEIS, ARMADA DE LO LOCALIZADO ARRIBA Y NO TECLEADA:")
    w("| rotulo | adjudicacion | linea del acta 219, LEIDA DEL FICHERO | que se sostiene |")
    w("|---|---|---:|---|")
    for rot, num, n, sostiene in filas_adj:
        w("| `%s` | `%s` | **%d** | %s |" % (rot, num, n, sostiene))
    w("   CIFRA filas armadas: %d | CIFRA que deberia haber: 6" % len(filas_adj))
    w("")

    # =================================================================== 1.b
    w("=" * 78)
    w("1.b. EL RECUENTO NUEVO, CON LAS DOS CIFRAS JUNTAS Y DICIENDO CUAL ES "
      "CUAL")
    w("=" * 78)
    w("")
    w("   PRIMERO SE SELLAN LOS NUEVE FICHEROS, PARA PROBAR QUE EL LECTOR LEE:")
    antes9 = {}
    for rel in NUEVE:
        antes9[rel] = sha16(rel)
        bd, bl = bytes_de(rel)
        w("      %s AL ENTRAR: %d bytes en disco y %d normalizado a LF, sha256 "
          "disco %s y sha256 LF %s" % ((rel, bd, bl) + antes9[rel]))
    crudo_propio = io.open(
        os.path.join(RAIZ, SALIDA_LECTOR_219.replace("/", os.sep)), "rb").read()
    texto_propio_antes = crudo_propio.replace(b"\r\n", b"\n").decode(
        "utf-8", "replace")
    w("")
    r = subprocess.run([sys.executable, LECTOR_219], cwd=RAIZ,
                       capture_output=True)
    salida = (r.stdout + r.stderr).decode("utf-8", "replace").replace(
        chr(13) + NL, NL)
    rel_hoy = "docs/loop/SALIDA_V%d_T1_RECORRIDA_DEL_LECTOR.txt" % VUELTA
    io.open(os.path.join(RAIZ, rel_hoy.replace("/", os.sep)), "w",
            encoding="utf-8", newline=NL).write(salida)
    w("   EL LECTOR RE-CORRIDO HOY POR MI: %s, exitcode %d." % (LECTOR_219,
                                                               r.returncode))
    if r.returncode != 0:
        fallos += 1
        w("      ROJO: el lector no sale en exitcode 0.")
    bd, bl = bytes_de(rel_hoy)
    w("   MI CORRIDA DE HOY, SELLADA: %s, %d bytes en disco y %d normalizado a "
      "LF" % (rel_hoy, bd, bl))
    if bd == 0:
        fallos += 1
        w("      ROJO: mi propia salida mide CERO BYTES y eso no cuenta como "
          "corrida.")
    w("")
    w("   LOS NUEVE, RE-MEDIDOS DESPUES DE CORRERLO:")
    movidos = []
    for rel in NUEVE:
        ahora9 = sha16(rel)
        igual = ahora9 == antes9[rel]
        if not igual:
            movidos.append(rel)
        bd9, bl9 = bytes_de(rel)
        w("      %s AL SALIR: %d bytes en disco y %d normalizado a LF, sha256 "
          "disco %s y sha256 LF %s | %s"
          % ((rel, bd9, bl9) + ahora9 + ("NO SE MOVIO" if igual
                                         else "SE MOVIO",)))
    w("   CIFRA ficheros que se movieron al correr el lector: %d | CIFRA de "
      "ellos que NO son la propia salida sellada del lector: %d"
      % (len(movidos), len([m for m in movidos if m != SALIDA_LECTOR_219])))
    w("")
    texto_propio_ahora = io.open(
        os.path.join(RAIZ, SALIDA_LECTOR_219.replace("/", os.sep)),
        "rb").read().replace(b"\r\n", b"\n").decode("utf-8", "replace")
    difs = lineas_que_difieren(texto_propio_antes, texto_propio_ahora)
    w("   CIFRA lineas en que la salida sellada del lector difiere de la que "
      "estaba en disco: %d | CIFRA que la regla admite: 1 (y solo la del "
      "conteo del acta)" % len(difs))
    for n, vieja, nueva in difs:
        w("      LINEA %d, LA QUE ESTABA> %s" % (n, vieja.strip()))
        w("      LINEA %d, LA DE HOY>     %s" % (n, nueva.strip()))
    motivos = juicio_del_movimiento(movidos, difs, SALIDA_LECTOR_219)
    w("   CIFRA motivos de ROJO que el juicio devuelve: %d | CIFRA que se "
      "exige: 0" % len(motivos))
    for m in motivos:
        w("      ROJO: %s" % m)
    fallos += len(motivos)
    w("")
    w("   Y LA SALIDA SELLADA DE LA 219 SE RESTAURA BYTE A BYTE, PORQUE ES "
      "EVIDENCIA DE OTRA VUELTA Y NO ES MIA PARA REESCRIBIRLA. Mi corrida de "
      "hoy queda sellada en el fichero de la 220, que es donde le toca.")
    io.open(os.path.join(RAIZ, SALIDA_LECTOR_219.replace("/", os.sep)),
            "wb").write(crudo_propio)
    tras = sha16(SALIDA_LECTOR_219)
    bdr, blr = bytes_de(SALIDA_LECTOR_219)
    w("      %s TRAS RESTAURAR: %d bytes en disco y %d normalizado a LF, "
      "sha256 disco %s y sha256 LF %s | %s"
      % ((SALIDA_LECTOR_219, bdr, blr) + tras
         + ("IDENTICA A LA DE ENTRADA" if tras == antes9[SALIDA_LECTOR_219]
            else "NO VOLVIO A SU ESTADO",)))
    if tras != antes9[SALIDA_LECTOR_219]:
        fallos += 1
        w("      ROJO: la restauracion no devolvio el fichero a su estado.")
    w("")

    pat = re.compile(r"CIFRA clausulas en (CUBRE|A MEDIAS|NO CUBRE) AL CIERRE "
                     r"DE LA TAREA 2: (\d+) de 17")
    medido = {}
    for l in salida.split(NL):
        m = pat.search(l)
        if m:
            medido[m.group(1)] = int(m.group(2))
    w("   CIFRA filas de recuento leidas de mi corrida de hoy: %d | CIFRA que "
      "deberia haber: 3" % len(medido))
    if len(medido) != 3:
        fallos += 1

    filas17 = filas_de_la_tabla(salida)
    w("   CIFRA filas de la tabla de las diecisiete leidas de mi corrida de "
      "hoy: %d | CIFRA que deberia haber: 17" % len(filas17))
    if len(filas17) != 17:
        fallos += 1
    sin_adj = reparto(filas17)
    w("   COTEJO ENTRE LAS TRES LINEAS DE CIFRA Y LA TABLA CONTADA: CUBRE %s "
      "contra %s | A MEDIAS %s contra %s | NO CUBRE %s contra %s"
      % (medido.get("CUBRE"), sin_adj["CUBRE"],
         medido.get("A MEDIAS"), sin_adj["A MEDIAS"],
         medido.get("NO CUBRE"), sin_adj["NO CUBRE"]))
    for k in ("CUBRE", "A MEDIAS", "NO CUBRE"):
        if medido.get(k) != sin_adj[k]:
            fallos += 1
            w("      ROJO: la linea de CIFRA de %s no calza con la tabla "
              "contada." % k)
    w("")
    w("   AHORA SE APLICA LA ADJUDICACION 4.5 DEL ACTA 219, Y ES LA UNICA "
      "SUBIDA. No la decido yo: la decide el auditor, y aqui solo se aplica.")
    subidas = []
    for f in filas17:
        k = (f[1], f[2])
        if k in SUBIDA_POR_ADJUDICACION and f[3] != SUBIDA_POR_ADJUDICACION[k]:
            w("      SUBE POR ADJUDICACION 4.5: %s idx %d, de %s a %s"
              % (f[1], f[2], f[3], SUBIDA_POR_ADJUDICACION[k]))
            subidas.append((f[1], f[2], f[3], SUBIDA_POR_ADJUDICACION[k]))
            f[3] = SUBIDA_POR_ADJUDICACION[k]
    w("   CIFRA clausulas que la adjudicacion mueve: %d | CIFRA que el acta "
      "219 ordena: 1" % len(subidas))
    if len(subidas) != 1:
        fallos += 1
    con_adj = reparto(filas17)
    w("")
    w("   LAS DOS CIFRAS JUNTAS, Y CADA UNA DICE CUAL ES:")
    w("| veredicto | CIFRA que MI LECTOR MIDE HOY, SIN la adjudicacion 4.5 | CIFRA que la ADJUDICACION 4.5 DEJA |")
    w("|---|---:|---:|")
    for k in ("CUBRE", "A MEDIAS", "NO CUBRE"):
        w("| **%s** | %d de 17 | **%d de 17** |" % (k, sin_adj[k], con_adj[k]))
    w("   CIFRA filas armadas: 3 | CIFRA que deberia haber: 3")
    w("")
    w("   CIFRA clausulas en CUBRE, MEDIDA HOY POR MI LECTOR SIN LA "
      "ADJUDICACION: %d de 17" % sin_adj["CUBRE"])
    w("   CIFRA clausulas en CUBRE, CON LA ADJUDICACION 4.5 APLICADA: %d de 17"
      % con_adj["CUBRE"])
    w("   CIFRA clausulas en A MEDIAS, MEDIDA HOY POR MI LECTOR SIN LA "
      "ADJUDICACION: %d de 17" % sin_adj["A MEDIAS"])
    w("   CIFRA clausulas en A MEDIAS, CON LA ADJUDICACION 4.5 APLICADA: %d de "
      "17" % con_adj["A MEDIAS"])
    w("   CIFRA clausulas en NO CUBRE, por las dos: %d de 17"
      % con_adj["NO CUBRE"])
    w("")
    w("   Y LAS CIFRAS DEL ENCARGO, CITADAS COMO CONTRASTE Y NO COMO FUENTE: "
      "el encargo dice que al cierre de la 219 quedo en 14 CUBRE, 3 A MEDIAS y "
      "0 NO CUBRE, y que con la 4.5 aplicada queda en 15 CUBRE, 2 A MEDIAS y 0 "
      "NO CUBRE.")
    calza_sin = (sin_adj["CUBRE"], sin_adj["A MEDIAS"],
                 sin_adj["NO CUBRE"]) == (14, 3, 0)
    calza_con = (con_adj["CUBRE"], con_adj["A MEDIAS"],
                 con_adj["NO CUBRE"]) == (15, 2, 0)
    w("   MI MEDICION SIN LA ADJUDICACION CALZA CON EL CONTRASTE: %s"
      % ("SI" if calza_sin else "NO"))
    w("   MI COMPUTO CON LA ADJUDICACION CALZA CON EL CONTRASTE: %s"
      % ("SI" if calza_con else "NO"))
    if not calza_sin or not calza_con:
        fallos += 1
    w("")
    w("   LAS QUE QUEDAN DESPUES DE LA ADJUDICACION, CON SU FILA, SU INDICE Y "
      "SU CIFRA:")
    resto = [f for f in filas17 if f[3] != "CUBRE"]
    for f in resto:
        w("      %-14s idx %d | %-9s | %s" % (f[1], f[2], f[3], f[4]))
    w("   CIFRA clausulas que siguen sin cubrir: %d | CIFRA que el recuento "
      "con la adjudicacion exige: %d" % (len(resto), con_adj["A MEDIAS"]))
    if len(resto) != con_adj["A MEDIAS"]:
        fallos += 1
    w("")
    w("   LA CIFRA DE CADA UNA DE LAS DOS QUE QUEDAN, TAL COMO EL ENCARGO LAS "
      "DICTA Y COMO LA SECCION 6 DEL ACTA 219 LAS LISTA:")
    w("      03 FUSIONES idx 0: 71 actos sin fundir por la lectura ancha, y "
      "SEIS fusiones de 19 nodos por la estrecha.")
    w("      07 ADUANA   idx 0: el quinto control sin correr.")
    w("")
    w("   LO QUE NO SE TOCA, Y SE DICE EN VEZ DE HACERSE: "
      "docs/plan/08_VERIFICACION.md NO SE ESCRIBE. La celda es sede del "
      "fundador y la divergencia sube nombrada, igual que la de 07 ADUANA. Sus "
      "sha256 al entrar y al salir estan en esta misma salida.")
    w("")

    # =================================================================== 1.c
    w("=" * 78)
    w("1.c. LAS SIETE COSAS QUE SUBEN NOMBRADAS A LA AUDITORIA INTEGRAL")
    w("=" * 78)
    w("")
    sec6 = localizar(lineas_acta, "## 6. LO QUE SUBE NOMBRADO A LA AUDITORIA "
                                  "INTEGRAL", desde=inicio)
    w("   CIFRA lineas donde empieza la seccion 6 del acta 219: %d | CIFRA que "
      "se exige: 1" % len(sec6))
    if len(sec6) != 1:
        fallos += 1
        inicio_6 = inicio
    else:
        inicio_6 = sec6[0]
        w("   LA SECCION 6 EMPIEZA EN LA LINEA %d" % inicio_6)
    w("")
    w("   NO SE RESUELVE NINGUNA. Solo quedan escritas, con su cifra y con la "
      "linea del acta donde viven.")
    w("")
    filas_int = []
    for num, resumen, ancla in INTEGRAL:
        donde = localizar(lineas_acta, ancla, desde=inicio_6)
        if len(donde) != 1:
            fallos += 1
            w("   ROJO: el punto %s no aparece exactamente una vez (%d)."
              % (num, len(donde)))
            continue
        n = donde[0]
        cuerpo = [lineas_acta[n - 1]]
        k = n
        while k < len(lineas_acta) and lineas_acta[k].startswith("   "):
            cuerpo.append(lineas_acta[k])
            k += 1
        w("   PUNTO %s, LINEA %d, LEIDO DEL FICHERO:" % (num, n))
        for i, c in enumerate(cuerpo):
            w("      %d> %s" % (n + i, c))
        filas_int.append((num, n, resumen, " ".join(x.strip() for x in cuerpo)))
    w("")
    w("   CIFRA puntos localizados con su linea: %d | CIFRA que la seccion 6 "
      "lista: 7" % len(filas_int))
    if len(filas_int) != 7:
        fallos += 1
    w("")
    w("   LA TABLA, ARMADA DE LO LOCALIZADO Y NO TECLEADA:")
    w("| # | linea del acta 219 | lo que sube, y su cifra |")
    w("|---:|---:|---|")
    for num, n, resumen, _t in filas_int:
        w("| %s | **%d** | %s |" % (num, n, resumen))
    w("   CIFRA filas armadas: %d | CIFRA que deberia haber: 7" % len(filas_int))
    w("")
    w("   LAS TRES OPCIONES DEL PUNTO 1, QUE SON LO QUE LO HACE DECIDIBLE, "
      "EXTRAIDAS DEL PROPIO TEXTO DEL ACTA Y NO RESUMIDAS POR MI:")
    texto1 = ""
    for num, n, _r, t in filas_int:
        if num == "1":
            texto1 = t
    opciones = re.findall(r"\*\*\((a|b|c)\)\*\*(.*?)(?=\*\*\((?:b|c)\)\*\*|$)",
                          texto1)
    w("   CIFRA opciones halladas en el texto del punto 1: %d | CIFRA que el "
      "encargo exige: 3" % len(opciones))
    if len(opciones) != 3:
        fallos += 1
    for letra, cuerpo in opciones:
        limpio = re.sub(r"\s+", " ", cuerpo).strip().rstrip(";").strip()
        w("      OPCION (%s), VERBATIM DEL ACTA> %s" % (letra, limpio))
    w("   Y LO QUE EL AUDITOR ANADE SOBRE SU PROPIA LISTA, TAMBIEN DEL "
      "FICHERO: dice que el no elige, pero que descartaria la (c) mientras "
      "nadie mida que el sujeto esta a salvo por otra via.")
    w("   CIFRA opciones que ESTA VUELTA resuelve: 0 | CIFRA que el encargo "
      "ordena resolver: 0")
    w("")

    # ============================================================== EL CIERRE
    w("=" * 78)
    w("ESTA TAREA SOLO LEE, Y SE PRUEBA CON LOS SHA")
    w("=" * 78)
    for rel in SEDES:
        sal = sha16(rel)
        bd, bl = bytes_de(rel)
        w("   %s AL ENTRAR: sha256 disco %s y sha256 LF %s"
          % ((rel,) + entrada[rel]))
        w("   %s AL SALIR:   sha256 disco %s y sha256 LF %s, %d bytes en disco "
          "y %d normalizado a LF" % ((rel,) + sal + (bd, bl)))
        if sal != entrada[rel]:
            fallos += 1
            w("   ROJO: %s SE MOVIO." % rel)
    coinciden = all(sha16(r) == entrada[r] for r in SEDES)
    w("   LOS %d SHA DE LAS SEDES DEL PLAN COINCIDEN AL ENTRAR Y AL SALIR POR "
      "LAS DOS CONVENCIONES: %s" % (len(SEDES) * 2, "SI" if coinciden else "NO"))
    w("")
    w("   EL CASO ROJO, DICHO CUAL ES CUAL: la localizacion de las lineas, la "
      "re-corrida del lector, el cotejo de los nueve sha, el cotejo entre las "
      "tres lineas de CIFRA y la tabla contada, y la aritmetica de las dos "
      "cifras CAEN EN ROJO por si solos y estan contados arriba. LA GLOSA DE "
      "CADA ADJUDICACION ES MIA y no tiene nada que mutar: SE DECLARA QUE NO "
      "HAY CASO ROJO AUTOMATICO PARA ESA PARTE.")
    w("")
    w("CIFRA comprobaciones que fallan: %d" % fallos)
    w("VERDE: la TAREA 1 sale limpia." if not fallos
      else "ROJO: la TAREA 1 tiene comprobaciones que fallan.")

    texto = NL.join(out) + NL
    destino = os.path.join(LOOP, "SALIDA_V%d_T1_REGISTROS.txt" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    sys.stdout.write(NL + "SELLADO EN %s, %d bytes%s"
                     % (os.path.basename(destino), os.path.getsize(destino), NL))
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
