# -*- coding: utf-8 -*-
"""vuelta57_puestos_volteados.py . EL BARRIDO DE LOS PUESTOS VOLTEADOS, PARA QUE
LA ESPECIE NO DEPENDA DEL OJO.

NOMBRE CON NUMERO DE VUELTA porque nace hoy; si sobrevive a la vuelta se le
quita, como se le quito al tallador de la cabecera. Lo que NO cambia es la vara.

POR QUE NACE, y el motivo esta MEDIDO antes de escribir una linea:

  1. La CAIDA DE CIFRA PUBLICADA de la vuelta 56: el volteo del puesto 203 (de
     `C` a `D`, por la relectura del filo del acto 15) no barrio las tablas que
     citan ese puesto CON SU CLASE. El barrido `9.10` de aquella vuelta SI tiene
     una FAMILIA 2 de puestos, pero se corrio con `--puestos 305`, que es el
     valor POR DEFECTO heredado de la vuelta 50: medido hoy en la cabecera de
     `docs/loop/SALIDA_V56_BARRIDO_910_CIERRE.txt`, que imprime
     "puestos corregidos    : 305". El instrumento sabia buscar; nadie le dijo
     que buscara el 203. UNA GUARDA QUE HAY QUE ACORDARSE DE ENCENDER NO ES UNA
     GUARDA.

  2. El HALLAZGO SISTEMICO que el acta 56 declara: la lista publicada de las
     SIETE sanas con figura arrastraba al 246 y al 360 desde las vueltas 52 y
     53, cuando sus actos se fundieron y sus pares colapsaron. Nadie los tecleo
     mal: envejecieron solos, y por eso ningun barrido que dependa de que
     alguien NOMBRE el puesto los iba a cazar nunca.

DE AHI LAS DOS SECCIONES, y la segunda es la que ataca la causa:

  SECCION A, LOS VOLTEADOS DE LA VUELTA. Se DERIVAN de `git` comparando
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` contra un commit base: nadie los teclea.

  SECCION B, EL COTEJO GENERAL. Toda cita de un PUESTO CON CLASE que viva en
  `docs/` se coteja contra la clase VIGENTE del archivo, la haya movido esta
  vuelta o una de hace cuatro. Es la seccion que habria cazado al 246 y al 360
  en la vuelta 52 sin que nadie supiera que se habian movido.

COMO SE ATA UN PUESTO A UNA CLASE, con los TRES detectores escritos. Y la vara
de los tres es la misma: SOLO SE JUZGA LO QUE ESTA ATADO DE FORMA EXPLICITA. Una
letra suelta en un parrafo no ata nada, porque si atara el instrumento gritaria
sobre media pagina, y un grito asi no se puede auditar. Medido en la primera
corrida de hoy, sin esta vara salian 243 rojos y 251 ambiguos, casi todo ruido.

  DETECTOR `tabla-pc`: una tabla de markdown cuya cabecera tenga una columna que
  diga `puesto` y OTRA que diga `clase`. Cada fila ata su numero a su letra. Es
  el detector que ve la tabla de la linea 4169 del informe.

  DETECTOR `tabla-c`: una tabla con columna de `clase` y SIN columna de puesto.
  La letra de la fila ata a los puestos que la fila liste tras la palabra
  `puesto`. Es el detector que ve la fila 167 de `03_FUSIONES.md`, cuya cabecera
  es `clase | cuantas | donde va` y cuyos siete puestos viven en la tercera
  celda.

  DETECTOR `lista`: una linea que diga `puesto` o `puestos` seguido de una lista
  de numeros, Y que ademas traiga un MARCADOR EXPLICITO de clase (`clase C`,
  `clases A`, `de clase D`). Si el marcador no esta en la linea, se busca en el
  parrafo, y solo ahi. Es el detector que ve la linea 313 de `04_ENLACES.md`,
  cuyo marcador (*los pares de clase C*) vive en la linea de arriba.

LOS MILLARES CUENTAN COMO UN SOLO NUMERO. `2.117` es el puesto 2117 y no los
puestos 2 y 117, que es lo que la primera version de hoy leia.

LO TACHADO NO CUENTA. Un numero dentro de `~~...~~` esta retirado y no se juzga;
una letra de clase dentro de `~~...~~` no ata nada, que es justo la forma que
deja una correccion declarada. Asi el instrumento sale VERDE sobre un sitio ya
reparado sin que haya que borrar el texto viejo.

ROJO Y EXIT 1 si alguna cita ata un puesto a una clase que el archivo YA NO DA.
AMBIGUO (no rojo, pero se imprime entero) si el sitio ata mas de una clase: ahi
la adjudicacion es de lectura y este instrumento no la finge.

LIMITE DECLARADO, y es de la misma familia que el del barrido `9.10`: es una
busqueda LEXICA. Una pagina puede citar un veredicto sin escribir la palabra
puesto y sin tabla, y este instrumento no lo veria. Lo que SI garantiza es que
las dos formas que la casa usa de verdad, la tabla con columnas y la lista tras
la palabra puesto, quedan cubiertas por maquina y no por el ojo.

USO:
  python scripts/loop/vuelta57_puestos_volteados.py --base c0e8041a
  python scripts/loop/vuelta57_puestos_volteados.py --base HEAD~1 --solo-a
  python scripts/loop/vuelta57_puestos_volteados.py --sin-git
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"

# Las mismas dos carpetas del barrido 9.10, y por el mismo motivo escrito alli:
# docs/loop queda FUERA porque son salidas de instrumento y actas fechadas de
# vueltas pasadas, y una salida vieja se contrasta, no se maquilla.
CARPETAS = [os.path.join(RAIZ, "docs"), os.path.join(RAIZ, "docs", "plan")]

RE_TACHADO = re.compile(r"~~.*?~~", re.DOTALL)
RE_CLASE = re.compile(r"(?<![A-Za-z0-9_])([ABCD])(?![A-Za-z0-9_])")
RE_LISTA = re.compile(r"puestos?\b", re.IGNORECASE)
# el millar con punto o coma cuenta como UN numero: 2.117 es el puesto 2117
RE_NUM = re.compile(r"\b(\d{1,3}[.,]\d{3})\b|\b(\d{1,4})\b")
# EL MARCADOR EXPLICITO de clase: la palabra clase (o clases, o de clase) pegada
# a la letra, con el resaltado de markdown en medio si lo lleva.
RE_MARCADOR = re.compile(r"clases?\s*(?:de\s+)?[*`\s]*([ABCD])(?![A-Za-z0-9_])",
                         re.IGNORECASE)


def cargar_vigentes(texto):
    d = {}
    for ln in texto.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        r = json.loads(ln)
        d[r["puesto_intra"]] = r["clase"]
    return d


def git_show(hash_, ruta):
    out = subprocess.run(["git", "show", "%s:%s" % (hash_, ruta)], cwd=RAIZ,
                         capture_output=True, encoding="utf-8")
    if out.returncode != 0:
        return None
    return out.stdout


def tramos_tachados(linea):
    """Los rangos (inicio, fin) que estan dentro de un tachado en la linea."""
    return [(m.start(), m.end()) for m in RE_TACHADO.finditer(linea)]


def dentro(pos, tramos):
    return any(a <= pos < b for a, b in tramos)


def clases_de(texto):
    """Las letras de clase que una CELDA DE CLASE ata, ignorando lo tachado.
    Solo se usa sobre celdas cuya cabecera ya dijo que la columna es de clase:
    ahi una letra suelta SI ata, porque la cabecera es el marcador."""
    tach = tramos_tachados(texto)
    return sorted(set(m.group(1) for m in RE_CLASE.finditer(texto)
                      if not dentro(m.start(), tach)))


def marcadores_de(texto):
    """Las letras que un MARCADOR EXPLICITO ata, ignorando lo tachado.
    Si el marcador es PLURAL (clases D, D y A) se recogen TODAS: un sitio que
    nombra tres clases no ata ninguna, y se ira a las ambiguas en vez de a las
    rojas. Es la forma de la linea 106 del informe, medida hoy."""
    tach = tramos_tachados(texto)
    out = set()
    for m in RE_MARCADOR.finditer(texto):
        if dentro(m.start(), tach):
            continue
        out.add(m.group(1).upper())
        resto = texto[m.end():]
        while True:
            mm = re.match(r"(?:[\s*`,]|\by\b|\be\b)+([ABCD])(?![A-Za-z0-9_])", resto)
            if not mm:
                break
            out.add(mm.group(1).upper())
            resto = resto[mm.end():]
    return sorted(out)


def numeros(texto, n_max, tach=None, base=0):
    """Los numeros de puesto del texto, con el millar entero y sin lo tachado."""
    out = []
    for m in RE_NUM.finditer(texto):
        crudo = m.group(1) or m.group(2)
        v = int(crudo.replace(".", "").replace(",", ""))
        if not (1 <= v <= n_max):
            continue
        if tach is not None and dentro(base + m.start(), tach):
            continue
        out.append(v)
    return out


def tras_la_palabra(texto, n_max):
    """Los puestos que el texto lista DESPUES de la palabra puesto o puestos."""
    tach = tramos_tachados(texto)
    out = []
    for m in RE_LISTA.finditer(texto):
        resto = texto[m.end():]
        corrida = re.match(r"(?:[\s*,yYeE.:;-]|~~|\d|`)*", resto)
        if not corrida:
            continue
        out.extend(numeros(resto[:corrida.end()], n_max, tach, m.end()))
    return out


def rel(ruta):
    return os.path.relpath(ruta, RAIZ).replace("\\", "/")


def ficheros():
    vistos = set()
    for carpeta in CARPETAS:
        if not os.path.isdir(carpeta):
            continue
        for nombre in sorted(os.listdir(carpeta)):
            ruta = os.path.join(carpeta, nombre)
            if not os.path.isfile(ruta) or not nombre.endswith(".md"):
                continue
            # LAS PAGINAS DE LA FRANJA QUEDAN FUERA, y no por comodidad: numeran
            # con `puesto_franja` sobre `docs/FRANJA_VEREDICTOS.jsonl`, que es OTRA
            # numeracion. Medido hoy: el puesto 1602 es `D` en la franja
            # (politica_formal_de_calidad contra plan_gestion_calidad) y `A` en el
            # intra (calcular_peso_dimensional contra conocer_limites_peso). La
            # primera version de este instrumento las leia y daba TRES rojos que
            # eran suyos, no del catalogo.
            if nombre.upper().startswith("FRANJA"):
                continue
            if ruta in vistos:
                continue
            vistos.add(ruta)
            yield ruta


def celdas(linea):
    t = linea.strip()
    if not t.startswith("|"):
        return None
    return [p.strip() for p in t.strip("|").split("|")]


def es_separador(linea):
    c = celdas(linea)
    return bool(c) and all(x and set(x) <= set("-: ") for x in c)


def detector_tabla(lineas, n_max, citas):
    """Las dos formas de tabla: con columna de puesto y sin ella."""
    i = 0
    while i < len(lineas) - 1:
        cab = celdas(lineas[i])
        if cab and es_separador(lineas[i + 1]):
            baj = [c.lower().replace("*", "").replace("`", "") for c in cab]
            cols_c = [k for k, c in enumerate(baj) if "clase" in c]
            # UNA TABLA CON DOS COLUMNAS DE CLASE NO ATA NADA. La forma tipica es
            # `clase antes | clase ahora`, y quedarse con la primera publica como
            # vigente lo que la propia tabla declara SUPERADO. Medido hoy en la
            # linea 6310 del informe, que la primera version leia como roja.
            if len(cols_c) != 1:
                i += 1
                continue
            ic = cols_c[0]
            ip = next((k for k, c in enumerate(baj) if "puesto" in c), None)
            j = i + 2
            while j < len(lineas):
                fil = celdas(lineas[j])
                if not fil or len(fil) <= ic:
                    break
                cls = clases_de(fil[ic])
                if ip is not None and len(fil) > ip:
                    # tabla-pc: el numero vive en SU columna
                    cel_p = fil[ip]
                    nums = numeros(cel_p, n_max, tramos_tachados(cel_p))
                    det = "tabla-pc"
                else:
                    # tabla-c: la fila lista sus puestos tras la palabra
                    nums = tras_la_palabra(lineas[j], n_max)
                    det = "tabla-c"
                for p in nums:
                    citas.append(dict(puesto=p, clases=cls, linea=j + 1,
                                      detector=det, texto=lineas[j].strip()))
                j += 1
            i = j
            continue
        i += 1


def parrafo_de(lineas, k):
    """El bloque contiguo de lineas no vacias que contiene a la linea k."""
    a = k
    while a > 0 and lineas[a - 1].strip():
        a -= 1
    b = k
    while b < len(lineas) - 1 and lineas[b + 1].strip():
        b += 1
    return "\n".join(lineas[a:b + 1])


def detector_lista(lineas, n_max, citas, ya):
    """Lineas con puestos listados Y un MARCADOR EXPLICITO de clase."""
    for k, linea in enumerate(lineas):
        if not RE_LISTA.search(linea):
            continue
        nums = tras_la_palabra(linea, n_max)
        if not nums:
            continue
        cls = marcadores_de(linea)
        origen = "linea"
        if not cls:
            cls = marcadores_de(parrafo_de(lineas, k))
            origen = "parrafo"
        if not cls:
            continue
        for p in nums:
            if (k + 1, p) in ya:
                continue
            citas.append(dict(puesto=p, clases=cls, linea=k + 1,
                              detector="lista(%s)" % origen, texto=linea.strip()))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default=None,
                    help="commit contra el que se derivan los volteados de la vuelta")
    ap.add_argument("--sin-git", action="store_true",
                    help="salta la seccion A (no hay base contra la que comparar)")
    ap.add_argument("--tambien", default="",
                    help="puestos que ESTA vuelta repara aunque los volteara otra: "
                         "entran en la guarda dura igual que los derivados de git")
    ap.add_argument("--estricto", action="store_true",
                    help="hace ROJO tambien lo heredado, para el dia que la casa "
                         "decida vaciar el atraso")
    ap.add_argument("--solo-a", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    vig = cargar_vigentes(io.open(os.path.join(RAIZ, VEREDICTOS),
                                  encoding="utf-8").read())
    n_max = max(vig)

    print("=" * 78)
    print("LOS PUESTOS VOLTEADOS Y SUS CITAS. Vuelta 57.")
    print("La especie de la vuelta 56 (un volteo que no barrio sus tablas), por maquina.")
    print("=" * 78)
    print("  veredictos vigentes leidos: %d (puestos 1 a %d)" % (len(vig), n_max))
    print()

    volteados = []
    print("--- SECCION A: LOS VOLTEADOS, DERIVADOS DE GIT (nadie los teclea) ---")
    if a.sin_git or not a.base:
        print("  SALTADA por peticion (--sin-git o sin --base).")
    else:
        viejo_txt = git_show(a.base, VEREDICTOS)
        if viejo_txt is None:
            print("  ROJO: no se pudo leer %s en %s" % (VEREDICTOS, a.base))
            return 1
        viejo = cargar_vigentes(viejo_txt)
        for p in sorted(set(viejo) | set(vig)):
            vi, nu = viejo.get(p), vig.get(p)
            if vi != nu:
                volteados.append((p, vi, nu))
        print("  base: %s" % a.base)
        print("  VOLTEADOS: %d" % len(volteados))
        for p, vi, nu in volteados:
            print("    puesto %-6d %s  ->  %s" % (p, vi, nu))
        if not volteados:
            print("    ninguno.")
    bajo_guarda = set(p for p, _, _ in volteados)
    if a.tambien:
        extra = [int(x) for x in a.tambien.split(",") if x.strip()]
        bajo_guarda |= set(extra)
        print("  MAS LOS QUE ESTA VUELTA REPARA (--tambien): %s"
              % ", ".join(str(x) for x in extra))
    print("  BAJO GUARDA DURA: %s"
          % (", ".join(str(x) for x in sorted(bajo_guarda)) or "(ninguno)"))
    print()

    if a.solo_a:
        print("FIN (--solo-a)")
        return 0

    print("--- SECCION B: TODA CITA DE PUESTO CON CLASE, COTEJADA CONTRA EL ARCHIVO ---")
    print()
    rojos, ambiguos, verdes, sin_clase = [], [], 0, 0
    for ruta in ficheros():
        try:
            lineas = io.open(ruta, encoding="utf-8").read().splitlines()
        except UnicodeDecodeError:
            print("  NO SE PUDO LEER (codificacion): %s" % rel(ruta))
            continue
        citas = []
        detector_tabla(lineas, n_max, citas)
        detector_lista(lineas, n_max, citas,
                       set((c["linea"], c["puesto"]) for c in citas))
        for c in citas:
            c["fichero"] = rel(ruta)
            if not c["clases"]:
                sin_clase += 1
                continue
            if len(c["clases"]) > 1:
                ambiguos.append(c)
                continue
            atada = c["clases"][0]
            real = vig.get(c["puesto"])
            if real is None:
                continue
            if atada == real:
                verdes += 1
            else:
                c["atada"], c["real"] = atada, real
                rojos.append(c)

    print("  citas atadas y VERDES (la clase citada es la vigente): %d" % verdes)
    print("  citas con puesto pero SIN clase atada (no se juzgan)   : %d" % sin_clase)
    print("  citas AMBIGUAS (el sitio ata mas de una clase)         : %d" % len(ambiguos))
    print("  citas ENVEJECIDAS (la clase citada YA NO ES la vigente): %d" % len(rojos))
    print()
    if ambiguos:
        print("  --- LAS AMBIGUAS, enteras, para adjudicar de lectura ---")
        for c in ambiguos:
            print("    %s:%d  puesto %d  ata %s  (vigente %s)  [%s]"
                  % (c["fichero"], c["linea"], c["puesto"], "/".join(c["clases"]),
                     vig.get(c["puesto"]), c["detector"]))
            print("        %s" % c["texto"][:200])
        print()
    # LAS DOS ALTURAS, y se separan a proposito. Lo que esta BAJO GUARDA es el
    # deber que el banco 9.10 pone en el MISMO ACTO del volteo: eso es rojo y
    # detiene. Lo HEREDADO es atraso de vueltas viejas: se imprime entero y no
    # se esconde, pero no es la falta de esta vuelta, y varias de esas citas son
    # el retrato de un dia con su corte declarado, que este instrumento no sabe
    # distinguir y no finge saber.
    duros = [c for c in rojos if c["puesto"] in bajo_guarda]
    heredados = [c for c in rojos if c["puesto"] not in bajo_guarda]

    def volcar(titulo, cual):
        print("  --- %s ---" % titulo)
        for c in cual:
            marca = ""
            for p, vi, nu in volteados:
                if p == c["puesto"]:
                    marca = "  <-- VOLTEADO EN ESTA VUELTA (%s a %s)" % (vi, nu)
            print("    %s:%d  puesto %d  cita %s  pero el archivo dice %s%s  [%s]"
                  % (c["fichero"], c["linea"], c["puesto"], c["atada"], c["real"],
                     marca, c["detector"]))
            print("        %s" % c["texto"][:220])
        print()

    if heredados:
        volcar("ENVEJECIDAS HEREDADAS (%d): atraso, no falta de esta vuelta"
               % len(heredados), heredados)
    if duros:
        volcar("ENVEJECIDAS BAJO GUARDA (%d): ROJO" % len(duros), duros)

    print("=" * 78)
    print("LIMITE DECLARADO: busqueda LEXICA. Una pagina que cite un veredicto sin")
    print("la palabra puesto y sin tabla de columnas no la ve este instrumento. Y una")
    print("cifra con su fecha de corte declarada aparece aqui SIN estar envejecida:")
    print("esa diferencia es de lectura y este instrumento no la finge.")
    if duros:
        print("ROJO: %d citas de puestos BAJO GUARDA siguen envejecidas." % len(duros))
        print("El banco 9.10 pide barrerlas EN EL MISMO ACTO del volteo.")
        return 1
    if heredados and a.estricto:
        print("ROJO (--estricto): %d citas heredadas envejecidas." % len(heredados))
        return 1
    if heredados:
        print("GUARDA VERDE: cero citas envejecidas entre los puestos BAJO GUARDA.")
        print("ATRASO ABIERTO: %d citas heredadas, listadas arriba enteras."
              % len(heredados))
        return 0
    print("VERDE: ninguna cita de puesto con clase esta envejecida.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
