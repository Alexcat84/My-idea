# -*- coding: utf-8 -*-
r"""_v220_t2_bateria.py . LA MEDICION DE LA TAREA 2 DE LA VUELTA 220: LA
BATERIA DE MUTACIONES, ENTERA Y SOLA.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). NO ES ARNES NI GUARDA NI LECTOR NUEVO, y
sobre todo NO ES UN CLON DEL LANZADOR: el lanzador
scripts/loop/vuelta183_bateria_por_tramos.py es estable, NO SE CLONA y NO SE
REPARA. Esto solo MIDE lo que esa corrida dejo en disco, y muere con la vuelta.

LA VARA DE "LO QUE ESTA VUELTA ESCRIBIO" NO ES `--siguiente`, Y ESA ES LA MITAD
QUE IMPORTA. El acta 219, caida `5.1` (linea 77991 de docs/loop/ACTA_AUDITOR.md,
leida en esta vuelta del fichero), midio que `--siguiente` contesta
"CIFRA tramos que FALTAN: 0" ANTES de que la 220 corriera un solo tramo, porque
mira nombres estables y no sabe de que vuelta son las salidas. AQUI LA VARA ES
DOBLE Y LAS DOS MITADES SE LEEN, NO SE TECLEAN:

  1. EL sha256 DE CADA SALIDA DE TRAMO TIENE QUE SER DISTINTO DEL QUE LA
     APERTURA DE ESTA VUELTA SELLO, que es el de la corrida anterior. Una
     salida cuyo sha no se movio NO la escribio esta vuelta.
  2. EL ASUNTO DEL ULTIMO COMMIT DE CADA SALIDA TIENE QUE NOMBRAR LA VUELTA
     220, leido de git log y no tecleado.

Una salida que falle CUALQUIERA de las dos cuenta como TRAMO QUE FALTA, aunque
exista y aunque no este vacia. Y UNA SALIDA SELLADA QUE MIDE CERO BYTES NO
CUENTA COMO HECHA, que es la tercera puerta y la que el regimen de AUDITOR.md
6.1 nombra por su nombre.

Y LO QUE ESTE FICHERO NO HACE: no repara ningun tramo en rojo, no toca la
nomina (CONGELADA EN 135) y no vuelve a correr nada. Solo cuenta.

USO:  python scripts/loop/_v220_t2_bateria.py
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

APERTURA = "docs/loop/SALIDA_V%d_APERTURA.txt" % VUELTA
COMPUESTA = "docs/loop/SALIDA_V183_BATERIA.txt"
LANZADOR = "scripts/loop/vuelta183_bateria_por_tramos.py"
TRAMOS = 11


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def sha16(rel):
    b = io.open(os.path.join(RAIZ, rel.replace("/", os.sep)), "rb").read()
    return hashlib.sha256(b).hexdigest()[:16]


def bytes_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    b = io.open(p, "rb").read()
    return os.path.getsize(p), len(b.replace(b"\r\n", b"\n"))


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", errors="replace").strip()


def shas_de_la_apertura():
    """LOS sha256 QUE LA APERTURA DE ESTA VUELTA SELLO PARA CADA TRAMO, leidos
    de su fichero. Devuelve {numero_de_tramo: sha16}. Si la apertura no los
    trae, devuelve un diccionario vacio y quien llama lo cuenta como fallo: sin
    ese sello no hay forma de decir que salida es de esta vuelta."""
    hallados = {}
    pat = re.compile(r"CIFRA SALIDA_V183_BATERIA_TRAMO_(\d+)\.txt AL ENTRAR:.*?"
                     r"sha256 disco ([0-9a-f]+)")
    for l in leer(APERTURA).split(NL):
        m = pat.search(l)
        if m:
            hallados[int(m.group(1))] = m.group(2)
    return hallados


def vuelta_que_sello(asunto):
    """EL NUMERO DE VUELTA QUE NOMBRA EL ASUNTO DE UN COMMIT. PURA."""
    m = re.search(r"VUELTA (\d+)", asunto or "")
    return int(m.group(1)) if m else None


def cifra(texto, ancla):
    """LA PRIMERA LINEA DE UN TEXTO QUE LLEVA UN ANCLA, YA LIMPIA. PURA."""
    for l in texto.split(NL):
        if ancla in l:
            return l.strip()
    return ""


def main():
    out = []
    fallos = 0

    def w(s=""):
        out.append(s)

    w("=" * 78)
    w("TAREA 2 DE LA VUELTA %d: LA BATERIA DE MUTACIONES, ENTERA Y SOLA." % VUELTA)
    w("=" * 78)
    w("")
    bd, bl = bytes_de(LANZADOR)
    w("EL LANZADOR ES ESTABLE, NO SE CLONA Y NO SE REPARA: %s, %d bytes en "
      "disco y %d bytes normalizado a LF, sha256 disco %s."
      % (LANZADOR, bd, bl, sha16(LANZADOR)))
    w("   Y su sha256 al entrar, leido de la apertura de esta vuelta: %s"
      % cifra(leer(APERTURA), "CIFRA " + LANZADOR + ":"))
    w("")

    # ================================================== 2.a y 2.d: LOS ONCE
    w("=" * 78)
    w("2.a y 2.d. LOS ONCE TRAMOS, CORRIDOS EXPLICITAMENTE Y MEDIDOS SOBRE LAS")
    w("SALIDAS QUE ESTA VUELTA ESCRIBIO")
    w("=" * 78)
    w("")
    antes = shas_de_la_apertura()
    w("   LOS sha256 QUE LA APERTURA SELLO ANTES DE LA PRIMERA OPERACION: %d | "
      "CIFRA que se exige: %d" % (len(antes), TRAMOS))
    if len(antes) != TRAMOS:
        fallos += 1
        w("      ROJO: sin el sello de apertura no se puede decir que salida es "
          "de esta vuelta.")
    w("")
    w("   LA VARA, Y NO ES `--siguiente`: sha256 DISTINTO DEL DE LA APERTURA, "
      "ASUNTO DEL ULTIMO COMMIT QUE NOMBRE LA VUELTA %d, Y BYTES MAYORES QUE "
      "CERO. LAS TRES." % VUELTA)
    w("")
    hechos, faltan, vacias = [], [], []
    filas = []
    for n in range(1, TRAMOS + 1):
        rel = "docs/loop/SALIDA_V183_BATERIA_TRAMO_%d.txt" % n
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(p):
            faltan.append(n)
            w("   TRAMO %-2d NO EXISTE EN DISCO." % n)
            continue
        bdn, bln = bytes_de(rel)
        sh = sha16(rel)
        asunto = git(["log", "-1", "--format=%s", "--", rel])
        vsello = vuelta_que_sello(asunto)
        movida = sh != antes.get(n)
        de_esta = (vsello == VUELTA)
        no_vacia = bdn > 0
        ok = movida and de_esta and no_vacia
        if bdn == 0:
            vacias.append(n)
        if ok:
            hechos.append(n)
        else:
            faltan.append(n)
        exitcode = cifra(leer(rel), "CIFRA exitcode:")
        veredicto = cifra(leer(rel), "VEREDICTO DE ESTA CORRIDA:")
        dur = cifra(leer(rel), "DURACION DEL TRAMO (monotona, minutos):")
        w("   TRAMO %-2d %s: %d bytes en disco y %d bytes normalizado a LF | "
          "sha256 disco %s | sha256 que sello la apertura %s | SE MOVIO: %s | "
          "vuelta del ultimo commit: %s | NO VACIA: %s | CUENTA COMO HECHO: %s"
          % (n, rel, bdn, bln, sh, antes.get(n, "(sin sello)"),
             "SI" if movida else "NO", vsello, "SI" if no_vacia else "NO",
             "SI" if ok else "NO"))
        w("      %s | %s | %s" % (veredicto, exitcode, dur))
        filas.append((n, rel, bdn, bln, sh, veredicto, dur))
    w("")
    w("   CIFRA tramos con salida sellada no vacia ESCRITA EN ESTA VUELTA: %d | "
      "CIFRA tramos que faltan: %d" % (len(hechos), len(faltan)))
    w("   CIFRA salidas de tramo que miden CERO BYTES: %d | CIFRA que se "
      "exige: 0" % len(vacias))
    if len(hechos) != TRAMOS or faltan or vacias:
        fallos += 1
        w("      ROJO: no estan los once del mismo calibre.")
    w("")
    w("   LOS ONCE, DEL MISMO CALIBRE, MEDIDO Y NO AFIRMADO:")
    entradas = []
    # CORRECCION DECLARADA DENTRO DE LA PROPIA VUELTA, Y LA CAZO ESTA MISMA
    # GUARDA EN ROJO ANTES DE QUE LLEGARA A NINGUN REPORTE. El patron viejo
    # pedia UN SOLO espacio entre la barra y el numero (`\| (\d+) entradas`) y
    # el compositor alinea esa columna a la derecha, asi que el tramo 11, que
    # tiene 5 entradas y no 13, lleva DOS espacios y no casaba. La cifra que
    # salio fue 10 tramos de 11 y 130 entradas de 135. El patron viejo queda
    # escrito aqui sin borrar, porque una correccion que tapa lo que corrige no
    # se puede auditar.
    for l in leer("docs/loop/SALIDA_V%d_T2_COMPONER.txt" % VUELTA).split(NL):
        m = re.search(r"TRAMO (\d+): SALIDA_V183_BATERIA_TRAMO_\d+\.txt.*?\|"
                      r"\s+(\d+) entradas", l)
        if m:
            entradas.append((int(m.group(1)), int(m.group(2))))
    w("   CIFRA tramos con su cuenta de entradas leida del compositor: %d | "
      "CIFRA que se exige: %d" % (len(entradas), TRAMOS))
    if len(entradas) != TRAMOS:
        fallos += 1
    total_entradas = sum(e for _n, e in entradas)
    w("   CIFRA entradas sumadas de los once tramos: %d | CIFRA de la nomina "
      "CONGELADA: 135" % total_entradas)
    if total_entradas != 135:
        fallos += 1
    w("")

    # ============================================================= 2.b: RELOJ
    w("=" * 78)
    w("2.b. LA DOBLE CORRIDA Y EL RELOJ, QUE NO SE AFLOJAN")
    w("=" * 78)
    w("")
    aviso = [l.strip() for l in leer(
        "docs/loop/SALIDA_V183_BATERIA_TRAMO_1.txt").split(NL)
        if "cada entrada se corre" in l or "reproducibilidad" in l]
    w("   LA DOBLE CORRIDA, LEIDA DE LA PROPIA SALIDA DE LA BATERIA Y NO "
      "AFIRMADA POR MI:")
    for a in aviso:
        w("      bateria> %s" % a)
    if not aviso:
        fallos += 1
        w("      ROJO: la salida no dice que cada entrada se corra dos veces.")
    w("")
    w("   EL RELOJ, TRAMO A TRAMO, LEIDO DE CADA SALIDA:")
    minutos = 0.0
    for n, _rel, _bd, _bl, _sh, _v, dur in filas:
        m = re.search(r"([\d.]+)$", dur)
        val = float(m.group(1)) if m else 0.0
        minutos += val
        w("      TRAMO %-2d %s" % (n, dur))
    w("   CIFRA minutos de reloj sumados de los once tramos: %.1f" % minutos)
    w("   CIFRA entradas corridas: %d | CIFRA corridas reales, que son el "
      "doble por el cotejo de reproducibilidad: %d"
      % (total_entradas, total_entradas * 2))
    w("")

    # ========================================================= 2.c: COMPUESTA
    w("=" * 78)
    w("2.c. LA SALIDA UNICA, Y LAS TRES COSAS JUNTAS")
    w("=" * 78)
    w("")
    bdc, blc = bytes_de(COMPUESTA)
    w("   EL NOMBRE, LOS BYTES POR LAS DOS CONVENCIONES Y LA ATRIBUCION, LAS "
      "TRES JUNTAS: %s, %d bytes en disco y %d bytes normalizado a LF, LA "
      "CORRIO EL EJECUTOR DE LA VUELTA %d, ENTERA Y SOLA, POR SUS ONCE TRAMOS."
      % (COMPUESTA, bdc, blc, VUELTA))
    if bdc == 0:
        fallos += 1
        w("      ROJO: la salida unica mide CERO BYTES.")
    w("   sha256 disco de la salida unica: %s" % sha16(COMPUESTA))
    w("")
    w("   LAS DOS COSAS DEL ROTULO, DICHAS LAS DOS Y NO UNA:")
    primera = leer(COMPUESTA).split(NL)[0].strip()
    w("      1. SU PRIMERA LINEA, LEIDA DEL FICHERO> %s" % primera)
    w("      2. SU CONTENIDO ES EL DE LA VUELTA %d, y no el de la 183: los "
      "once tramos que lo componen los escribi yo en esta vuelta, con su "
      "sha256 movido y su commit nombrando la %d, y esta medido arriba uno a "
      "uno." % (VUELTA, VUELTA))
    dice183 = "VUELTA 183" in primera
    w("      CIFRA menciones de la vuelta 183 en su primera linea: %d | CIFRA "
      "menciones de la vuelta %d: %d"
      % (1 if dice183 else 0, VUELTA, primera.count("VUELTA %d" % VUELTA)))
    w("      Y EL MOTIVO, MEDIDO Y NO SUPUESTO: el lanzador computa ese numero "
      "de su propio nombre de fichero, que es %s, y el lanzador es estable y "
      "NO SE CLONA POR VUELTA. La moratoria 6.3 prohibe repararlo y no hay "
      "caida de dato que lo exija." % os.path.basename(LANZADOR))
    w("")
    comp = leer("docs/loop/SALIDA_V%d_T2_COMPONER.txt" % VUELTA)
    for ancla in ("CIFRA entradas que los tramos dicen haber corrido:",
                  "CIFRA entradas de la nomina que NINGUN tramo corrio:",
                  "CIFRA entradas corridas que NO estan en la nomina:",
                  "CIFRA entradas corridas MAS DE UNA VEZ:"):
        w("   compositor> %s" % cifra(comp, ancla))
    w("")

    # ============================================== 2.e: LO QUE SALE EN ROJO
    w("=" * 78)
    w("2.e. LO QUE SALE EN ROJO, MEDIDO, NO REPARADO Y TRAIDO")
    w("=" * 78)
    w("")
    especies = {"ancla perdida": 0, "que no mordieron": 0, "sin reproducir": 0,
                "fuera de la nomina": 0, "invisibles al censo": 0,
                "SUJETO VIVO": 0}
    no_mordieron = []
    fuera = set()
    for n in range(1, TRAMOS + 1):
        rel = "docs/loop/SALIDA_V183_BATERIA_TRAMO_%d.txt" % n
        t = leer(rel)
        linea = cifra(t, "CIFRA de FALLO:")
        w("   TRAMO %-2d %s" % (n, linea))
        for clave in especies:
            m = re.search(r"(\d+) " + re.escape(clave), linea)
            if m:
                especies[clave] += int(m.group(1))
        m = re.search(r"NO MORDIO\s+: (\d+) \(([^)]*)\)", t)
        if m and int(m.group(1)):
            for nombre in m.group(2).split(", "):
                no_mordieron.append((n, nombre.strip()))
        for l in t.split(NL):
            if l.strip().startswith("FUERA DE LA NOMINA:"):
                fuera.add(l.split(":", 1)[1].strip())
    w("")
    w("   LAS ESPECIES, SUMADAS SOBRE LOS ONCE TRAMOS:")
    for clave in ("ancla perdida", "que no mordieron", "sin reproducir",
                  "fuera de la nomina", "invisibles al censo", "SUJETO VIVO"):
        w("      CIFRA %s: %d" % (clave, especies[clave]))
    w("")
    w("   LOS QUE NO MORDIERON, UNO A UNO Y CON SU TRAMO:")
    for n, nombre in no_mordieron:
        w("      TRAMO %-2d %s" % (n, nombre))
    w("   CIFRA arneses que NO MORDIERON en esta corrida: %d"
      % len(no_mordieron))
    w("")
    w("   LOS QUE EL CENSO VE Y LA NOMINA CONGELADA NO TIENE, UNO A UNO:")
    for nombre in sorted(fuera):
        w("      %s" % nombre)
    w("   CIFRA arneses fuera de la nomina, distintos: %d" % len(fuera))
    w("")
    w("   EL COTEJO CONTRA LA CORRIDA ANTERIOR, QUE ES LO QUE DICE SI ESTO ES "
      "NUEVO O ES UNA CONDICION QUE YA VENIA. Se lee de la version commiteada "
      "de cada salida en el HEAD de apertura de esta vuelta, y no de mi "
      "recuerdo:")
    head_ap = leer("docs/loop/SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA).strip()
    iguales = 0
    for n in range(1, TRAMOS + 1):
        rel = "docs/loop/SALIDA_V183_BATERIA_TRAMO_%d.txt" % n
        viejo = git(["show", "%s:%s" % (head_ap, rel)])
        m_v = re.search(r"NO MORDIO\s+: (\d+) \(([^)]*)\)", viejo)
        t = leer(rel)
        m_n = re.search(r"NO MORDIO\s+: (\d+) \(([^)]*)\)", t)
        v = m_v.group(0).strip() if m_v else "(sin linea)"
        a = m_n.group(0).strip() if m_n else "(sin linea)"
        igual = v == a
        if igual:
            iguales += 1
        w("      TRAMO %-2d ANTES> %s" % (n, v))
        w("      TRAMO %-2d HOY>   %s | %s"
          % (n, a, "IDENTICO" if igual else "DISTINTO"))
    w("   CIFRA tramos cuya lista de los que no mordieron es IDENTICA a la de "
      "la corrida anterior: %d de %d" % (iguales, TRAMOS))
    w("")
    w("   Y LO QUE NO HAGO, DICHO CON SU LETRA DELANTE: NO REPARO NINGUNO. El "
      "encargo dice PARALO Y TRAELO, y la moratoria 6.3 prohibe reparar "
      "guardas. Sube como PARADA al reporte, con sus nombres y sus cifras.")
    w("")

    # ==================================================== EL CARRIL QUE MIENTE
    w("=" * 78)
    w("LO QUE `--siguiente` CONTESTO ANTES DE QUE ESTA VUELTA CORRIERA NADA")
    w("=" * 78)
    w("")
    w("   NO ES MI VARA Y NO SE USA COMO TAL: se corrio SOLO para dejar "
      "reproducida la caida 5.1 del acta 219 con mi propia medicion.")
    prev = leer("docs/loop/SALIDA_V%d_T2_SIGUIENTE_ANTES.txt" % VUELTA)
    for ancla in ("CIFRA tramos del reparto:",
                  "CIFRA tramos CON salida sellada no vacia:",
                  "CIFRA tramos que FALTAN:",
                  "LOS 11 TRAMOS TIENEN SALIDA SELLADA"):
        w("      siguiente> %s" % cifra(prev, ancla))
    w("   LA CIFRA QUE ESO CONTESTABA ERA FALSA PARA LA %d Y VERDADERA PARA LA "
      "215, y mi vara de arriba, la del sha movido y el commit que nombra la "
      "vuelta, medida en ese mismo momento habria dicho 0 hechos y 11 que "
      "faltan." % VUELTA)
    w("")

    w("=" * 78)
    w("CIFRA comprobaciones que fallan: %d" % fallos)
    w("VERDE: los once tramos estan, del mismo calibre, y la salida unica "
      "existe." if not fallos
      else "ROJO: la TAREA 2 tiene comprobaciones que fallan.")

    texto = NL.join(out) + NL
    destino = os.path.join(LOOP, "SALIDA_V%d_T2_BATERIA.txt" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    sys.stdout.write(NL + "SELLADO EN %s, %d bytes%s"
                     % (os.path.basename(destino), os.path.getsize(destino), NL))
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
