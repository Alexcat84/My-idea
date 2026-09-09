# -*- coding: utf-8 -*-
r"""_v216_t3_dos_varas.py . LA TAREA 3 DE LA VUELTA 216: LA CONSECUENCIA,
MEDIDA, Y LAS DOS VARAS PUBLICADAS LADO A LADO SIN MAQUILLAR QUE MIDEN COSAS
DISTINTAS.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

QUE HACE:
  (3.a) reparte las CATORCE clausulas por ficha, contandolas de la salida
        sellada de la TAREA 2, y dice cuantas filas armo y cuantas deberia
        haber.
  (3.b) lee la corrida de la vara del expediente que esta vuelta hizo con el
        hash de SU apertura, y publica MIS cifras. Las del auditor van al lado
        COMO CONTRASTE, leidas de su acta por su linea, para cotejar y NO para
        copiar.
  (3.c) publica LAS DOS VARAS LADO A LADO, ficha por ficha. NO son la misma
        vara y no se maquilla que lo sean: la del expediente mide P1, P2 y P3,
        y la de las catorce filas mide clausulas. Una ficha puede salir en
        HECHA SIN NINGUNA PRUEBA y tener todas sus clausulas en CUBRE, y eso NO
        es una contradiccion.
  (3.d) escribe la condicion de la parada feliz ANTES de su resultado y dice si
        se cumple. NO DECLARA NADA CONSUMADO: eso es del auditor.

NO TOCA NI UN CAMPO DE ESTADO Y NO ESCRIBE EN NINGUNA FICHA. Lo comprueba.

USO:  python scripts/loop/_v216_t3_dos_varas.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
T2 = "docs/loop/SALIDA_V%d_T2_REMEDICION.txt" % VUELTA
VARA = "docs/loop/SALIDA_V%d_T3_EXPEDIENTE.txt" % VUELTA
ACTA = "docs/loop/ACTA_AUDITOR.md"
EXPEDIENTE = "docs/plan/OPERACIONES.jsonl"

LAS_CINCO = ("OP-V-01", "OP-L-01", "OP-L-02", "OP-L-03", "OP-I-01")

# LAS CIFRAS DEL AUDITOR, CADA UNA CON EL TROZO DE TEXTO QUE LA ANCLA DENTRO DE
# SU ACTA. El texto es suyo y se busca literal; la etiqueta de la izquierda es
# mia. NINGUNA CIFRA SUYA SE TECLEA: se saca de la linea que el anclaje halla.
CONTRASTES = (
    ("fichas que no calzan", r"Expediente \*\*(\d+) de 71 que no calzan\*\*"),
    ("fichas en HECHA sin ninguna prueba", r"\*\*(\d+) en HECHA sin ninguna prueba\*\*"),
)

# LO QUE EL ENCARGO ME DA COMO CIFRA DEL AUDITOR PARA COTEJAR. Es texto de mi
# encargo y se dice que lo es: se coteja contra lo que YO mido, y si no calza,
# publico la mia y declaro la diferencia.
DEL_ENCARGO = (
    ("no calzan", 40),
    ("congeladas declaradas", 24),
    ("congeladas en silencio", 12),
    ("en LISTA sin prueba", 3),
    ("en HECHA sin prueba", 4),
)

MIAS = (
    ("no calzan", "CIFRA fichas que no calzan: "),
    ("congeladas declaradas", "CIFRA fichas congeladas declaradas: "),
    ("congeladas en silencio", "CIFRA fichas congeladas en silencio: "),
    ("en LISTA sin prueba", "CIFRA fichas en LISTA sin ninguna prueba: "),
    ("en HECHA sin prueba", "CIFRA fichas HECHA sin ninguna prueba: "),
)


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def cifra(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(-?\d+)", l.split(etiqueta, 1)[1])
            if m:
                return int(m.group(1))
    return None


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def sha(rel):
    b = io.open(os.path.join(RAIZ, rel.replace("/", os.sep)), "rb").read()
    return hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16]


def main():
    sha_antes = sha(EXPEDIENTE)
    fallos = 0
    t2 = leer(T2)
    vara = leer(VARA)
    acta = leer(ACTA).split(NL)

    print("=" * 78)
    print("VUELTA %d, TAREA 3. LA CONSECUENCIA, MEDIDA Y SIN TOCAR UN ESTADO"
          % VUELTA)
    print("=" * 78)
    print("SHA256 LF DE docs/plan/OPERACIONES.jsonl AL ENTRAR: %s" % sha_antes)
    print("")

    print("=" * 78)
    print("3.a. LAS CATORCE CLAUSULAS, REPARTIDAS POR FICHA")
    print("=" * 78)
    filas = []
    for l in t2.split(NL):
        m = re.match(r"^\| (\d+) \| (OP-[A-Z]-\d+) \| (\d+) \| (\d+) \| (.+?) \|$", l)
        if m:
            filas.append(m.groups())
    print("CIFRA FILAS ARMADAS LEYENDO %s: %d | CIFRA FILAS QUE DEBERIA HABER: "
          "14" % (T2, len(filas)))
    if len(filas) != 14:
        print("ROJO: el reparto no sale de catorce filas.")
        return 1
    por_ficha = {}
    for n, ficha, idx, linea, ver in filas:
        d = por_ficha.setdefault(ficha, {"linea": linea, "total": 0,
                                         "cubre": 0, "otras": []})
        d["total"] += 1
        if ver == "CUBRE":
            d["cubre"] += 1
        else:
            d["otras"].append("indice %s en %s" % (idx, ver))
    print("")
    print("| ficha | linea del expediente | clausulas suyas | en CUBRE | NO en CUBRE | cuales |")
    print("|---|---:|---:|---:|---:|---|")
    armadas_ficha = 0
    for f in LAS_CINCO:
        d = por_ficha.get(f)
        if d is None:
            print("| `%s` | (NO APARECE) | | | | |" % f)
            fallos += 1
            continue
        armadas_ficha += 1
        print("| `%s` | %s | **%d** | **%d** | %d | %s |"
              % (f, d["linea"], d["total"], d["cubre"],
                 d["total"] - d["cubre"], ", ".join(d["otras"]) or "ninguna"))
    print("")
    print("CIFRA FILAS DE FICHA ARMADAS: %d | CIFRA QUE DEBERIA HABER: 5"
          % armadas_ficha)
    if armadas_ficha != 5:
        fallos += 1
    suma = sum(d["total"] for d in por_ficha.values())
    print("LA SUMA SE COMPRUEBA CONTRA SI MISMA: %d clausulas repartidas, y las "
          "filas de la TAREA 2 son %d." % (suma, len(filas)))
    if suma != len(filas):
        fallos += 1
    print("")

    print("=" * 78)
    print("3.b. LA VARA DEL EXPEDIENTE, CORRIDA CON EL HASH DE MI APERTURA")
    print("=" * 78)
    _, head = git(["rev-parse", "HEAD"])
    ap = leer("docs/loop/SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA).strip()
    print("CIFRA hash de MI apertura, leido del sello y no tecleado: %s" % ap)
    print("CIFRA HEAD de ahora mismo, leido de git: %s" % head.strip())
    print("EL COMANDO: scripts/loop/vuelta150_3_relectura_expediente.py --corte "
          "%s" % ap)
    print("LA SALIDA: %s" % VARA)
    corte_en_salida = ("--corte %s" % ap) in vara or ap[:12] in vara
    print("CIFRA la salida cita ese mismo corte: %s (se exige SI)"
          % ("SI" if corte_en_salida else "NO"))
    if not corte_en_salida:
        fallos += 1
    print("")
    print("| cifra | LA MIA, medida hoy | la del encargo, del auditor | calzan |")
    print("|---|---:|---:|---|")
    discrepancias = []
    del_encargo = dict(DEL_ENCARGO)
    for etiqueta, marca in MIAS:
        mia = cifra(vara, marca)
        suya = del_encargo[etiqueta]
        calza = (mia == suya)
        if not calza:
            discrepancias.append((etiqueta, mia, suya))
        print("| %s | **%s** | %s | %s |"
              % (etiqueta, mia, suya, "SI" if calza else "NO"))
    print("")
    print("CIFRA celdas que NO calzan con la cifra del encargo: %d"
          % len(discrepancias))
    for etiqueta, mia, suya in discrepancias:
        print("   DISCREPANCIA DECLARADA> %s: la MIA %s, la suya %s. PUBLICO LA "
              "MIA Y NO COPIO LA SUYA (EJECUTOR.md 2)." % (etiqueta, mia, suya))
    if not discrepancias:
        print("   (cero discrepancias: las cinco cifras calzan una a una, y lo "
              "digo con las dos columnas delante en vez de con una sola)")
    print("")
    print("Y LA CIFRA DEL AUDITOR TAMBIEN SE LEE DE SU ACTA, CON SU LINEA, "
          "PORQUE UNA CIFRA CITADA DE UN ENCARGO NO ES UNA CIFRA LEIDA:")
    for etiqueta, patron in CONTRASTES:
        hallada = None
        for i, l in enumerate(acta, start=1):
            m = re.search(patron, l)
            if m:
                hallada = (i, m.group(1), l.strip())
        if hallada is None:
            print("   ANCLAJE %s: NO APARECE en el acta (ausencia, no cero)"
                  % etiqueta)
            fallos += 1
            continue
        print("   ANCLAJE %-38s | linea %d | cifra suya %s"
              % (etiqueta, hallada[0], hallada[1]))
        print("      CITA: %s" % hallada[2][:150])
    print("")
    print("LAS CUATRO FICHAS EN HECHA SIN NINGUNA PRUEBA, NOMBRADAS Y CONTADAS "
          "DE MI PROPIA SALIDA:")
    nombradas = []
    for l in vara.split(NL):
        m = re.match(r"^\| `(OP-[A-Z0-9-]+)` \| (\S+) \| HECHA \| (\S+) \| "
                     r"HECHA SIN NINGUNA PRUEBA", l)
        if m:
            nombradas.append(m.groups())
            print("   HECHA SIN PRUEBA> %s (fase %s, pruebas positivas: %s)"
                  % m.groups())
    print("CIFRA fichas nombradas: %d | CIFRA que mi propia salida cuenta: %s"
          % (len(nombradas), cifra(vara, "CIFRA fichas HECHA sin ninguna prueba: ")))
    if len(nombradas) != cifra(vara, "CIFRA fichas HECHA sin ninguna prueba: "):
        fallos += 1
    print("")

    print("=" * 78)
    print("3.c. LAS DOS VARAS, LADO A LADO, Y NO SE MAQUILLA QUE SEAN LA MISMA")
    print("=" * 78)
    print("LA VARA DEL EXPEDIENTE MIDE P1, P2 Y P3: grafo, codigo vivo y huella")
    print("en git. LA VARA DE LAS CATORCE FILAS MIDE CLAUSULAS DE VERIFICACION.")
    print("SON DOS VARAS DISTINTAS MIDIENDO COSAS DISTINTAS, Y UNA FICHA PUEDE")
    print("SALIR EN HECHA SIN NINGUNA PRUEBA CON TODAS SUS CLAUSULAS EN CUBRE.")
    print("ESO NO ES UNA CONTRADICCION. Cambiar la vara seria fabricar")
    print("maquinaria, y la moratoria de AUDITOR.md 6.3 lo prohibe.")
    print("")
    # LA TABLA DE LAS QUE NO CALZAN SE ACOTA POR SU PROPIA CABECERA.
    #
    # CORRECCION DECLARADA DE ESTA MISMA VUELTA, Y NO TAPA LO QUE CORRIGE: la
    # primera version leia CUALQUIER fila con forma de tabla de toda la salida,
    # y por eso cogia para `OP-I-01` la fila de la tabla de DESBLOQUEADAS, cuya
    # tercera celda es el TIPO y no el estado. Publicaba `estado MESA` cuando
    # la ficha esta en LISTA. La cifra era falsa POR MI COMPOSITOR y no por el
    # instrumento, y la primera version queda escrita aqui y no se borra.
    ls_vara = vara.split(NL)
    i0 = next((i for i, l in enumerate(ls_vara)
               if l.startswith("TABLA DE LAS QUE NO CALZAN")), None)
    i1 = next((i for i in range(i0 + 2, len(ls_vara))
               if ls_vara[i].startswith("=" * 20)), len(ls_vara)) if i0 is not None else 0
    estado_de = {}
    for l in ls_vara[i0:i1] if i0 is not None else []:
        m = re.match(r"^\| `(OP-[A-Z0-9-]+)` \| (\S+) \| (\S+) \| (\S+) \| (.+?) \|$", l)
        if m and m.group(1) in LAS_CINCO:
            estado_de.setdefault(m.group(1), (m.group(3), m.group(4), m.group(5)))
    j0 = next((i for i, l in enumerate(ls_vara)
               if l.startswith("| id_op | fase | tipo | depende_de medido | consumida por |")),
              None)
    lista_sin_prueba = {}
    if j0 is not None:
        for l in ls_vara[j0:]:
            m = re.match(r"^\| `(OP-[A-Z0-9-]+)` \| (\S+) \| (.+?) \| (.+?) \| (.+?) \|$", l)
            if m and m.group(1) in LAS_CINCO:
                lista_sin_prueba[m.group(1)] = m.group(5)
            if l.strip().startswith("CONTADO:"):
                break
    print("CIFRA filas leidas de la tabla de las que NO CALZAN, acotada por su "
          "propia cabecera: %d" % len(estado_de))
    print("CIFRA filas leidas de la tabla de las que estan en LISTA SIN NINGUNA "
          "PRUEBA: %d" % len(lista_sin_prueba))
    faltan = [f for f, _, _ in
              [(x[0], x[1], x[2]) for x in nombradas] if f not in estado_de]
    print("CIFRA de las CUATRO en HECHA sin prueba que NO aparecen en lo leido: "
          "%d (se exigen 0)" % len(faltan))
    if faltan:
        print("   FALTAN> %s" % faltan)
        fallos += 1
    print("")
    print("| ficha | VARA 1, la del expediente (P1 P2 P3) | VARA 2, las catorce clausulas |")
    print("|---|---|---|")
    filas_dos = 0
    for f in LAS_CINCO:
        d = por_ficha.get(f, {"total": 0, "cubre": 0})
        e = estado_de.get(f)
        if e is not None:
            v1 = "estado `%s`, pruebas positivas %s, %s" % (e[0], e[1], e[2])
        elif f in lista_sin_prueba:
            v1 = ("estado `LISTA` SIN NINGUNA PRUEBA, o sea que su estado CALZA "
                  "con el repo: consumida por otra ficha: %s" % lista_sin_prueba[f])
        else:
            v1 = "NO SALE en la tabla de las que no calzan: para esta vara CALZA"
        v2 = "%d de %d clausulas en CUBRE" % (d["cubre"], d["total"])
        print("| `%s` | %s | %s |" % (f, v1, v2))
        filas_dos += 1
    print("")
    print("CIFRA FILAS ARMADAS EN LA TABLA DE LAS DOS VARAS: %d | CIFRA QUE "
          "DEBERIA HABER: 5" % filas_dos)
    if filas_dos != 5:
        fallos += 1
    print("")

    print("=" * 78)
    print("3.d. LA CONDICION DE LA PARADA FELIZ, ESCRITA ANTES DE SU RESULTADO")
    print("=" * 78)
    print("LA CONDICION, VERBATIM DE MI ENCARGO: 'si las CATORCE clausulas")
    print("quedan en CUBRE con su busqueda corrida y su cifra delante, y si el")
    print("cierre integral sale limpio, entonces la campana esta consumada EN LO")
    print("QUE EL BUCLE PUEDE CONSUMAR'.")
    print("")
    cubren = sum(1 for _, _, _, _, v in filas if v == "CUBRE")
    print("CIFRA clausulas en CUBRE: %d | CIFRA que la condicion exige: 14"
          % cubren)
    print("CIFRA clausulas que NO estan en CUBRE: %d" % (14 - cubren))
    for n, ficha, idx, linea, ver in filas:
        if ver != "CUBRE":
            print("   NO CUBRE LA CONDICION> clausula %s, ficha %s, indice %s, "
                  "linea %s del expediente, veredicto %s"
                  % (n, ficha, idx, linea, ver))
    cumple = (cubren == 14)
    print("")
    print("LA PRIMERA MITAD DE LA CONDICION SE CUMPLE: %s"
          % ("SI" if cumple else "NO"))
    print("Y POR ESO NO PROPONGO LA PARADA FELIZ: la condicion la escribi antes"
          if not cumple else
          "LA SEGUNDA MITAD, EL CIERRE INTEGRAL, LA MIDE LA TAREA 4.")
    if not cumple:
        print("de saber el resultado, y una parada feliz escrita sobre una")
        print("condicion que no se cumple es exactamente la especie de verde")
        print("que esta casa lleva doscientas vueltas cazando.")
    print("")
    print("LO QUE ESTA TAREA NO HACE, Y LO DIGO PARA QUE NO SE BUSQUE: NO")
    print("declara la campana consumada, NO escribe docs/loop/PARA_ALEXIS.md y")
    print("NO pide ningun merge. Quien declara es EL AUDITOR, por la 4.2 del")
    print("acta 203, linea 71543, ratificada por el fundador el 9 sep 2026. Y")
    print("EL BUCLE NO FUNDE RAMAS.")
    print("")

    print("=" * 78)
    print("LA GUARDA: QUE ESTA TAREA NO MOVIO NI UN CAMPO DE ESTADO")
    print("=" * 78)
    sha_despues = sha(EXPEDIENTE)
    print("SHA256 LF DE docs/plan/OPERACIONES.jsonl AL SALIR: %s" % sha_despues)
    print("CIFRA los dos sha256 CALZAN: %s (se exige SI)"
          % ("SI" if sha_antes == sha_despues else "NO"))
    if sha_antes != sha_despues:
        fallos += 1
    _, ns = git(["diff", "--numstat", "--", EXPEDIENTE])
    n = len([x for x in ns.split(NL) if x.strip()])
    print("CIFRA filas de git diff --numstat sobre el expediente: %d (se exigen "
          "0)" % n)
    if n:
        fallos += 1
    print("")
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    print("VERDE: la TAREA 3 queda medida." if not fallos
          else "ROJO: la TAREA 3 tiene comprobaciones que fallan.")
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
