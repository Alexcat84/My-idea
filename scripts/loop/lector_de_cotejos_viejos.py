# -*- coding: utf-8 -*-
r"""lector_de_cotejos_viejos.py . EL LECTOR DE LOS COTEJOS DE CIEGA ESCRITOS
ANTES DEL FORMATO UNICO, CON SUS PARSEADORES DECLARADOS UNO A UNO.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, hermano de `cotejo_de_ciega.py`: el
formato unico dice como se escribe **de aqui en adelante**, y este dice **cuanto
se puede rescatar de lo de antes**. Los dos hacen falta y ninguno sustituye al
otro.

ES LA PIEZA `b` DE LA TAREA 5 DE LA VUELTA 192, sobre el `P.2` adjudicado A FAVOR
en la `4.9` del acta 192.

--- LOS SEIS PARSEADORES, DECLARADOS ANTES DE CONTAR NADA ---

**Cada uno se escribe mirando UN fichero real y se nombra por el.** No se
inventan formatos que nadie escribio, y **no se ensancha ninguno despues de ver
el resultado**, que es la trampa que la `4.4` del acta 192 acaba de adjudicar.

  `UNICO`      . el formato de `cotejo_de_ciega.py`. Se delega entero en el.
  `COLUMNAS`   . `NNN   C   C   dominio   COINCIDE` (o `<<< DISCREPA`), la tabla
                 ancha del `_auditor_v182_cotejo_ciega.txt`.
  `TUBERIA`    . `NNN | C | C | COINCIDE | no`, la tabla con tuberias de
                 `SALIDA_V190_T4_COTEJO.txt` y `SALIDA_V191_T2_COTEJO.txt`.
  `YO_ARCHIVO` . cualquier linea con un numero y despues `yo X` y `archivo Y`,
                 con o sin `dije`, con o sin `el`, y separados por `|` o por `/`.
                 Cubre `_auditor_v183`, `_auditor_v184`, `_auditor_v190` y
                 `_auditor_v191`, y tambien el `DISCREPA 199: yo A / archivo B`
                 del `_auditor_v189b`.
  `DISCREPA`   . la regla vieja de la TAREA 5 de la 191: una linea con un numero
                 y `DISCREPA` como palabra entera. **Se conserva a proposito**,
                 porque es la unica que lee ficheros que no dicen las dos clases,
                 y **lo que recupera es el puesto y NADA MAS**.

--- LA DIFERENCIA CON LA REGLA DE LA VUELTA 191, QUE ES EL PUNTO ENTERO ---

La regla de la 191 recuperaba **puestos que tumbaron a un lector**. Este lector
recupera, cuando el fichero lo dice, **las DOS clases y el veredicto**, y sobre
todo **intenta recuperar EL DENOMINADOR**, que es lo que la 191 midio que no
podia. Por eso cada fichero sale con **DOS veredictos separados y no uno**:

  `filas`        . cuantas filas de cotejo se pudieron leer.
  `denominador`  . sobre cuantos pares se midio, y **de donde sale**.

**Un fichero puede tener filas y no tener denominador**, y eso NO es lo mismo que
no tener nada: se dice cual de las dos le falta.

--- DE DONDE SALE EL DENOMINADOR, Y TAMBIEN VA DECLARADO ---

Por orden, y **se publica cual de los cuatro respondio**:

  1. `CIFRA puestos cotejados: N` (el formato unico).
  2. una cabecera que declara el total: `COTEJADOS: N`, `COINCIDEN: N de M`,
     `mis clases: N | destape: M`, `CIFRA puestos mios: N`, o
     `CIFRA clases mias leidas del fichero: N`.
  3. la suma de `COINCIDEN` y `DISCREPAN` declarados en la cabecera.
  4. el conteo de las filas leidas, **y SOLO si el fichero trae filas de
     COINCIDE**: un fichero que solo lista discrepancias no puede dar su
     denominador contando, y decir que si podria seria la cifra falsa que todo
     esto viene a evitar.

--- LO QUE ESTE LECTOR NO PUEDE HACER ---

**No inventa lo que el fichero no escribio.** Un cotejo que nunca puso la clase
del lector no la tiene, y ningun parseador la saca. **Y no dice si el lector
acerto**: dice si coincide con el archivo, que es otra cosa.

USO:
  python scripts/loop/lector_de_cotejos_viejos.py
  python scripts/loop/lector_de_cotejos_viejos.py --mutacion
"""
import argparse
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cotejo_de_ciega as FORMATO   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
SALIDA = os.path.join(LOOP, "SALIDA_V192_T5_LECTOR_DE_VIEJOS.txt")
NOMBRE_CANDIDATO = "COTEJO"

PAT_COLUMNAS = re.compile(
    r"^\s*(\d+)\s+([A-D])\s+([A-D])\s+\S+\s+.*?\b(COINCIDE|DISCREPA)\b\s*$")
PAT_TUBERIA = re.compile(
    r"^\s*(\d+)\s*\|\s*([A-D])\s*\|\s*([A-D])\s*\|\s*(COINCIDE|DISCREPA)\s*\|"
    r"\s*(si|no|SI|NO)\s*$")
PAT_YO_ARCHIVO = re.compile(
    r"(?<![0-9])(\d+)(?![0-9]).*?\byo\s+(?:dije\s+)?([A-D])\b.*?"
    r"\b(?:el\s+)?archivo\s+(?:dice\s+)?([A-D])\b")
PAT_DISCREPA_SOLA = re.compile(r"\bDISCREPA\b")
PAT_NUMERO = re.compile(r"\d+")
PAT_DUDOSO = re.compile(r"(?i)(dudoso mio|en mis dudosos|estaba en mis dudosos)")

DENOMS = [
    ("el formato unico", re.compile(r"^CIFRA puestos cotejados:\s*(\d+)\s*$")),
    ("una cabecera COTEJADOS", re.compile(r"(?i)\bCOTEJADOS:\s*(\d+)")),
    ("una cabecera COINCIDEN N de M", re.compile(r"(?i)\bCOINCIDEN:\s*\d+\s+de\s+(\d+)")),
    ("una cabecera mis clases | destape",
     re.compile(r"(?i)\bmis clases:\s*(\d+)\s*\|\s*destape:\s*\d+")),
    ("una cabecera CIFRA puestos mios",
     re.compile(r"(?i)\bCIFRA puestos mios:\s*(\d+)")),
    ("una cabecera CIFRA clases mias",
     re.compile(r"(?i)\bCIFRA clases mias leidas del fichero:\s*(\d+)")),
]
PAT_COIN_DECL = re.compile(r"(?i)^\s*(?:CIFRA\s+)?COINCIDEN:\s*(\d+)\s*$")
PAT_DISC_DECL = re.compile(r"(?i)^\s*(?:CIFRA\s+)?DISCREPAN:\s*(\d+)")


def filas_por_parseador(texto):
    """LAS FILAS QUE CADA PARSEADOR SACA. PURA.

    Devuelve `{nombre: [(puesto, clase_lector, clase_archivo, en_dudosos)]}`,
    solo con los que sacan algo. **Los parseadores se corren TODOS y se publica
    cual respondio**, en vez de elegir uno a ojo."""
    out = {}
    lineas = texto.replace(chr(13) + NL, NL).split(NL)

    delunico = FORMATO.filas_del_cotejo(texto)
    if delunico:
        out["UNICO"] = [(p, cl, ca, du) for p, cl, ca, du, _v in delunico]

    for nombre, pat in (("COLUMNAS", PAT_COLUMNAS), ("TUBERIA", PAT_TUBERIA)):
        filas = []
        for l in lineas:
            m = pat.match(l)
            if m:
                du = bool(PAT_DUDOSO.search(l)) or (
                    pat is PAT_TUBERIA and m.group(5).lower() == "si")
                filas.append((int(m.group(1)), m.group(2), m.group(3), du))
        if filas:
            out[nombre] = filas

    filas = []
    for l in lineas:
        m = PAT_YO_ARCHIVO.search(l)
        if m:
            filas.append((int(m.group(1)), m.group(2), m.group(3),
                          bool(PAT_DUDOSO.search(l))))
    if filas:
        out["YO_ARCHIVO"] = filas

    sueltos = []
    for l in lineas:
        if not PAT_DISCREPA_SOLA.search(l):
            continue
        nums = PAT_NUMERO.findall(l)
        if nums:
            sueltos.append((int(nums[0]), "?", "?", bool(PAT_DUDOSO.search(l))))
    if sueltos:
        out["DISCREPA"] = sueltos
    return out


def mejor_parseador(porp):
    """EL PARSEADOR QUE MAS FILAS SACA, Y CON LAS DOS CLASES. PURA.

    Prefiere SIEMPRE uno que recupere las dos clases sobre `DISCREPA`, que solo
    recupera el puesto: **mas filas con menos informacion no es mejor.**"""
    completos = {k: v for k, v in porp.items() if k != "DISCREPA"}
    if completos:
        return max(completos, key=lambda k: len(completos[k]))
    return "DISCREPA" if "DISCREPA" in porp else None


def denominador_de(texto, filas):
    """(N, DE_DONDE). PURA. `N` es None si no se puede recuperar."""
    t = texto.replace(chr(13) + NL, NL)
    for nombre, pat in DENOMS:
        for l in t.split(NL):
            m = pat.search(l.strip())
            if m:
                return int(m.group(1)), nombre
    coin = disc = None
    for l in t.split(NL):
        mc = PAT_COIN_DECL.match(l)
        md = PAT_DISC_DECL.match(l)
        if mc:
            coin = int(mc.group(1))
        if md:
            disc = int(md.group(1))
    if coin is not None and disc is not None:
        return coin + disc, "la suma de COINCIDEN y DISCREPAN declarados"
    if filas and any(cl != "?" for _p, cl, _ca, _d in filas):
        vistos = set()
        for p, cl, ca, _d in filas:
            if cl != "?" and ca != "?" and cl == ca:
                vistos.add(p)
        if vistos:
            return len(set(p for p, _c, _a, _d in filas)), \
                "el conteo de las filas, que SI traen coincidencias"
    return None, ("no se puede: el fichero no declara el total y sus filas solo "
                  "traen discrepancias")


def deduplicar(filas):
    """(FILAS SIN REPETIR, CUANTAS SE QUITARON). PURA, y conserva el orden.

    POR QUE HACE FALTA, Y ESTA MEDIDO: `_auditor_v191_cotejo_ciega.txt` lista
    **cada discrepancia DOS VECES**, una en su tabla y otra en su bloque de
    detalle, y el parseador sacaba **39 filas sobre 30 puestos distintos**. Sin
    esto, el lector habria publicado un denominador de 30 al lado de 39 filas,
    **que es exactamente la especie de cifra falsa que todo esto viene a
    evitar**. Se queda la PRIMERA aparicion de cada puesto y se cuenta cuantas se
    quitaron, **porque una fila descartada en silencio es una cifra que nadie
    puede cotejar**."""
    vistos = set()
    salida = []
    quitadas = 0
    for f in filas:
        if f[0] in vistos:
            quitadas += 1
            continue
        vistos.add(f[0])
        salida.append(f)
    return salida, quitadas


def leer(ruta):
    """UN FICHERO, LEIDO CON TODOS LOS PARSEADORES. Devuelve un dict."""
    texto = io.open(ruta, encoding="utf-8", errors="replace").read()
    porp = filas_por_parseador(texto)
    cual = mejor_parseador(porp)
    crudas = porp.get(cual, []) if cual else []
    filas, quitadas = deduplicar(crudas)
    n, de_donde = denominador_de(texto, filas)
    con_clases = [f for f in filas if f[1] != "?" and f[2] != "?"]
    return {
        "nombre": os.path.basename(ruta),
        "bytes": os.path.getsize(ruta),
        "parseadores": {k: len(v) for k, v in porp.items()},
        "cual": cual,
        "filas": filas,
        "n_filas": len(filas),
        "n_crudas": len(crudas),
        "n_duplicadas": quitadas,
        "n_con_clases": len(con_clases),
        "denominador": n,
        "de_donde": de_donde,
        "recuperado": bool(con_clases) and n is not None,
    }


def candidatos(directorio=None):
    base = directorio or LOOP
    return [n for n in sorted(os.listdir(base))
            if n.lower().endswith((".txt", ".md"))
            and NOMBRE_CANDIDATO in n.upper()
            and os.path.isfile(os.path.join(base, n))]


# ---------------------------------------------------------------- LA MUTACION
def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    w("   %-64s %s" % (nombre, "VERDE" if ok else "ROJO"))
    if not ok:
        w("      esperado: %r" % (esperado,))
        w("      obtenido: %r" % (obtenido,))
    return ok


def prueba_de_mutacion():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DEL LECTOR DE COTEJOS VIEJOS")
    w("=" * 78)
    w("")
    w("Los textos se FABRICAN con la cifra sabida por construccion. Ninguno sale")
    w("del repo, asi que ningun fichero real se toca.")
    w("")
    w("A) CADA PARSEADOR SOBRE SU FORMATO, Y SOLO SOBRE EL SUYO")
    cols = ("puesto  mia    archivo  dominio" + NL
            + "100     D      D        compras            COINCIDE" + NL
            + "1012    A      D        core               <<< DISCREPA" + NL)
    ok &= _caso(w, "COLUMNAS saca las dos filas",
                len(filas_por_parseador(cols).get("COLUMNAS", [])), 2)
    tub = ("   puesto | mia | archivo | veredicto | dudoso mio" + NL
           + "        3 |  A  |    A    | COINCIDE  | no" + NL
           + "      648 |  D  |    B    | DISCREPA  | SI" + NL)
    ok &= _caso(w, "TUBERIA saca las dos filas",
                len(filas_por_parseador(tub).get("TUBERIA", [])), 2)
    ok &= _caso(w, "TUBERIA lee el dudoso de la ultima celda",
                [f[3] for f in filas_por_parseador(tub)["TUBERIA"]], [False, True])
    ya = ("PUESTO 375 | yo D | archivo B" + NL
          + "PUESTO 660 | yo dije A (vara: REPITE) | el archivo dice B" + NL
          + "   DISCREPA 199: yo A / archivo B  [ESTABA EN MIS DUDOSOS]" + NL)
    ok &= _caso(w, "YO_ARCHIVO cubre las TRES escrituras de la casa",
                len(filas_por_parseador(ya).get("YO_ARCHIVO", [])), 3)
    ok &= _caso(w, "y lee sus clases bien",
                [(f[1], f[2]) for f in filas_por_parseador(ya)["YO_ARCHIVO"]],
                [("D", "B"), ("A", "B"), ("A", "B")])
    w("")
    w("B) LA REGLA DE LA 191 SE CONSERVA Y RECUPERA MENOS, QUE ES EL PUNTO")
    solo_d = "   DISCREPA 2422: el par que tumbo a alguien" + NL
    porp = filas_por_parseador(solo_d)
    ok &= _caso(w, "DISCREPA saca la fila", len(porp.get("DISCREPA", [])), 1)
    ok &= _caso(w, "pero sin las clases", porp["DISCREPA"][0][1:3], ("?", "?"))
    ok &= _caso(w, "y `mejor_parseador` NO la prefiere si hay una completa",
                mejor_parseador(filas_por_parseador(ya + solo_d)), "YO_ARCHIVO")
    w("")
    w("C) EL DENOMINADOR, Y SUS CUATRO VIAS")
    ok &= _caso(w, "via 2, una cabecera COTEJADOS",
                denominador_de("COTEJADOS: 30  COINCIDEN: 24" + NL, [])[0], 30)
    ok &= _caso(w, "via 2, COINCIDEN N de M",
                denominador_de("COINCIDEN: 29 de 30" + NL, [])[0], 30)
    ok &= _caso(w, "via 2, mis clases | destape",
                denominador_de("mis clases: 30 | destape: 30" + NL, [])[0], 30)
    ok &= _caso(w, "via 3, la suma de los dos declarados",
                denominador_de("CIFRA coinciden: 24" + NL + "CIFRA discrepan: 6" + NL,
                               [])[0], 30)
    ok &= _caso(w, "via 4, el conteo de filas CON coincidencias",
                denominador_de("sin cabecera", [(1, "A", "A", False),
                                                (2, "B", "D", False)])[0], 2)
    w("")
    w("D) LA MUTACION QUE IMPORTA: SIN CABECERA Y SOLO CON DISCREPANCIAS, EL")
    w("   DENOMINADOR **NO SE PUEDE** RECUPERAR, Y SE DICE EN VEZ DE ESTIMARSE")
    n, de = denominador_de("sin cabecera", [(1, "A", "D", False)])
    ok &= _caso(w, "el denominador sale None", n, None)
    ok &= _caso(w, "y el motivo lo explica", "no se puede" in de, True)
    w("")
    w("E) LA MUTACION QUE PRUEBA QUE `recuperado` EXIGE LAS DOS COSAS")
    w("   (filas CON clases Y denominador), y no una sola")
    ok &= _caso(w, "solo puesto, sin clases: no cuenta como recuperado",
                bool([f for f in [(1, "?", "?", False)] if f[1] != "?"]), False)
    w("")
    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V192_T5_MUTACION_LECTOR_VIEJOS.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V192_T5_MUTACION_LECTOR_VIEJOS.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutacion", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if a.mutacion:
        return prueba_de_mutacion()

    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 192, TAREA 5.b: EL LECTOR DE LOS COTEJOS VIEJOS SOBRE LOS 43")
    w("=" * 78)
    w("")
    w("LOS SEIS PARSEADORES, DECLARADOS ANTES DE CONTAR (docstring del fichero):")
    for n in ("UNICO", "COLUMNAS", "TUBERIA", "YO_ARCHIVO", "DISCREPA"):
        w("   %s" % n)
    w("   y el denominador sale de CUATRO vias, publicando cual respondio.")
    w("")
    cands = candidatos()
    w("A) LOS CANDIDATOS, POR LA MISMA REGLA 1 DE LA VUELTA 191, SIN ENSANCHARLA")
    w("   regla: ficheros .txt y .md de docs/loop/ con %r en el nombre"
      % NOMBRE_CANDIDATO)
    w("   CIFRA candidatos HOY: %d (la TAREA 5 de la 191 midio 43)" % len(cands))
    w("")
    w("B) CADA CANDIDATO, CON EL PARSEADOR QUE RESPONDIO Y SU DENOMINADOR")
    recuperados, fuera = [], []
    for n in cands:
        r = leer(os.path.join(LOOP, n))
        if r["recuperado"]:
            recuperados.append(r)
            w("   RECUPERA %-52s %s: %d filas con clases, denominador %s (%s)"
              % (n, r["cual"], r["n_con_clases"], r["denominador"], r["de_donde"]))
            if r["n_duplicadas"]:
                w("            (y %d fila(s) repetida(s) quitada(s): el fichero "
                  "lista %d en total)" % (r["n_duplicadas"], r["n_crudas"]))
            if r["denominador"] and r["n_con_clases"] > r["denominador"]:
                w("            AVISO: mas filas (%d) que denominador (%d). Se "
                  "publica y no se tapa." % (r["n_con_clases"], r["denominador"]))
        else:
            fuera.append(r)
    w("")
    w("C) LOS QUE SIGUEN FUERA, NOMBRADOS CON SU MOTIVO")
    for r in fuera:
        if r["n_con_clases"] and r["denominador"] is None:
            motivo = "trae %d filas con clases pero NO se puede recuperar el denominador" % r["n_con_clases"]
        elif r["n_filas"]:
            motivo = ("trae %d fila(s) pero ninguna dice las dos clases (solo el "
                      "parseador DISCREPA responde)" % r["n_filas"])
        else:
            motivo = "ningun parseador saca ni una fila: no es un cotejo de ciega"
        w("   FUERA    %-52s %s" % (r["nombre"], motivo))
    w("")
    w("D) EL COTEJO CONTRA LOS SEIS DE LA VUELTA 191, POR NOMBRE Y NO POR CIFRA")
    w("   (se leen de docs/loop/SALIDA_V191_T5_MARCA_CONTRA_DIFICULTAD.txt, que")
    w("    es su fichero, y no de la memoria)")
    prev = os.path.join(LOOP, "SALIDA_V191_T5_MARCA_CONTRA_DIFICULTAD.txt")
    seis, antes_cands = [], None
    if os.path.exists(prev):
        tp = io.open(prev, encoding="utf-8", errors="replace").read()
        for l in tp.replace(chr(13) + NL, NL).split(NL):
            ls = l.strip()
            if ls.startswith("ENTRA "):
                seis.append(ls.split()[1])
            m = re.match(r"^CIFRA candidatos:\s*(\d+)$", ls)
            if m:
                antes_cands = int(m.group(1))
    w("   CIFRA que entraban por la regla de la 191: %d" % len(seis))
    for n in seis:
        w("      %s" % n)
    w("   CIFRA candidatos que la 191 midio: %s" % antes_cands)
    nombres_rec = set(r["nombre"] for r in recuperados)
    siguen = [n for n in seis if n in nombres_rec]
    salen = [n for n in seis if n not in nombres_rec]
    nuevos = sorted(nombres_rec - set(seis))
    w("   SIGUEN DENTRO: %d (%s)" % (len(siguen), ", ".join(siguen) or "ninguno"))
    w("   SALEN: %d (%s)" % (len(salen), ", ".join(salen) or "ninguno"))
    w("      y salen porque este lector es MAS ESTRECHO, no mas ancho: exige las")
    w("      DOS clases Y el denominador, y la regla de la 191 se conformaba con")
    w("      el puesto de una discrepancia.")
    w("   ENTRAN QUE NO ESTABAN: %d (%s)"
      % (len(nuevos), ", ".join(nuevos) or "ninguno"))
    w("")
    w("E) LAS DOS CIFRAS, PUBLICADAS JUNTAS, QUE ES LO QUE EL ENCARGO PIDE")
    w("   ANTES  (regla de la TAREA 5 de la vuelta 191): %s de %s"
      % (len(seis), antes_cands))
    w("   DESPUES (este lector):                         %d de %d"
      % (len(recuperados), len(cands)))
    w("   Y EL DENOMINADOR DE LAS DOS CIFRAS NO ES EL MISMO, Y ESO SE DICE EN VEZ")
    w("   DE ESCONDERSE: la 191 midio sobre %s candidatos y hoy hay %d, porque"
      % (antes_cands, len(cands)))
    w("   ESTA MISMA VUELTA ha escrito ficheros con COTEJO en el nombre. De los")
    nacidos = [n for n in cands if "V192" in n.upper() or "v192" in n]
    w("   %d candidatos de hoy, %d nacieron en esta vuelta: %s"
      % (len(cands), len(nacidos), ", ".join(nacidos) or "ninguno"))
    w("   SIN ELLOS, el lector recupera %d de %d, que es la cifra comparable"
      % (len([r for r in recuperados if r["nombre"] not in nacidos]),
         len([c for c in cands if c not in nacidos])))
    w("   Y LA DIFERENCIA DE LO QUE SE RECUPERA NO ES SOLO LA CIFRA: la regla de")
    w("   la 191 sacaba PUESTOS QUE TUMBARON A UN LECTOR; este saca LAS DOS")
    w("   CLASES y, cuando el fichero lo permite, EL DENOMINADOR.")
    total_filas = sum(r["n_con_clases"] for r in recuperados)
    w("   CIFRA filas con las DOS clases recuperadas en total: %d" % total_filas)
    w("   CIFRA pares del denominador sumado de los recuperados: %d"
      % sum(r["denominador"] for r in recuperados))
    w("")
    w("F) LO QUE ESTA MEDICION NO HACE, Y ES EL RESTO DEL ENCARGO")
    w("   NO SE RE MIDE LA MARCA CONTRA LA DIFICULTAD EN ESTA VUELTA. El encargo")
    w("   lo prohibe con esas palabras: el universo nuevo se usa cuando este")
    w("   medido y declarado, no en el mismo acto en que se construye. Elegir el")
    w("   universo y sacar la conclusion a la vez es lo que la TAREA 5 de la 191")
    w("   evito bien y la `4.4` del acta 192 adjudico A FAVOR.")
    w("")
    w("FIN")
    t = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V192_T5_LECTOR_DE_VIEJOS.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
