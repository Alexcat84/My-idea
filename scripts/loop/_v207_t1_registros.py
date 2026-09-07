# -*- coding: utf-8 -*-
r"""_v207_t1_registros.py . TAREA 1 DE LA VUELTA 207: `R.71` PARA EL ACTA 206,
ESCRITA EN `docs/PENDIENTES.md` POR ADICION PURA Y EN SU SEDE.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3). **NO SE ESCRIBE NINGUN LECTOR NUEVO Y
TAMPOCO SE CLONA NINGUNO:** todo lo que lee viene IMPORTADO de
`_v203_reparto_de_actas_viejas.py` (el mismo que usaron la 203, la 204 y la 206),
de `serie_de_registros.py`, de `vuelta184_tarea1a_registrar_acta184.py` y de
`_v206_t2_registros.py`, del que se reutilizan `ya_escrita()`,
`dos_convenciones()`, `numeral()` y `titulo_de()` tal cual. IMPORTAR NO ES CLONAR
(acta 206, adjudicacion `6.5`).

EL NUMERO NO SE TECLEA: lo computa `serie_de_registros.siguiente_libre()`
recomputando la serie de sus DOS sedes.

--- LO QUE ESTA ENTRADA TIENE DE DISTINTO, Y VA MEDIDO Y NO AFIRMADO ---

`R.69` y `R.70` registraron actas VIEJAS (179 y 180), anteriores a la 184, y para
esas la vara del `4.1` del acta 202 es obligatoria. **EL ACTA 206 ES MODERNA**:
escribe sus claves con comillas inversas y con la forma `**`6.1` TITULO`. Corrido
el mismo computo IMPORTADO sobre ella, **CUATRO de los cinco numerales salen
falsos o vacios, y no por el acta sino por las marcas de titulo del lector**:

  . ADJUDICACIONES. `MARCAS["adjudicaciones"]` es `("ADJUDICACIONES", "LA
    ADJUDICACION")`, y sobre esta acta casa con la seccion **5**, titulada *"UNA
    CAIDA MIA QUE NO ES DE ESTA VUELTA: LA ADJUDICACION 5.3 DEL ACTA 205 ES
    FALSA"*, que **no es la seccion de adjudicaciones sino la correccion de una
    adjudicacion vieja**. La seccion de adjudicaciones de esta acta se titula
    **`LO QUE ADJUDICO`**, y ninguna de las dos marcas la nombra. El lector no
    declara ambiguedad porque encuentra **exactamente una** candidata, y devuelve
    **0** claves. **PUBLICAR ESE 0 SERIA PUBLICAR QUE EL ACTA 206 NO ADJUDICO
    NADA**, y el acta trae `6.1` a `6.8`.
  . CAIDAS PROPIAS DEL AUDITOR. Sus marcas son `("MIS CAIDAS PROPIAS", "MIS
    PROPIAS CAIDAS")` y esta acta titula **`MIS CAIDAS, CON SU NOMBRE`**:
    ninguna seccion casa, y el propio computo ya lo DECLARA no computable.
  . CAIDAS DEL EJECUTOR. La seccion SI se encuentra, pero sus claves son `E.1` y
    `E.2` y las tres formas que el lector mira son `4.M`, ``**`CAIDA n`.`` y el
    lead en negrita que abre con CAIDA o AMAGO. Las tres dan **0** sobre una
    seccion que el acta titula **DOS**.
  . PREGUNTAS. `REP.preguntas_del_reporte()` casa con `^##\s+\d+\.\s+PREGUNTAS\b`
    y el articulo `LAS` le rompe la coincidencia sobre `## 6. LAS PREGUNTAS`
    (acta 204 `4.4`, linea 196, y hoy sigue sin tocarse porque es codigo y rige
    la moratoria). Devuelve 0 y ademas hace decir que el reporte no titula
    ninguna seccion de preguntas, que es FALSO.

**LO QUE ESTA TAREA HACE CON ESO, Y ES LO UNICO QUE PUEDE HACER SIN TOCAR
CODIGO:** publica la lectura del lector TAL CUAL como contraste, **DECLARA el
numeral NO COMPUTABLE en vez de publicar un cero falso** (mismo precedente que la
201 en su entrada de la 198 y la 206 en `R.69` y `R.70`), y pone DEBAJO el
REPARTO MEDIDO, marcado como MEDICION y no como numeral (acta 204 `4.6`). **EL
REPARTO MEDIDO USA EL MISMO LECTOR IMPORTADO**, `R84.claves_entrecomilladas()`
con la plantilla ancha: lo unico que cambia es **a que seccion y a que prefijo de
clave se apunta**, que es un dato y no una maquina.

USO:
  python scripts/loop/_v207_t1_registros.py
  python scripts/loop/_v207_t1_registros.py --escribir
  python scripts/loop/_v207_t1_registros.py --escribir --salida NOMBRE
"""
import argparse
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

sys.path.insert(0, AQUI)
import serie_de_registros as SERIE                          # noqa: E402
import _v203_reparto_de_actas_viejas as REP                 # noqa: E402
import _v206_t2_registros as REG206                         # noqa: E402
import vuelta184_tarea1a_registrar_acta184 as R84           # noqa: E402
import vuelta192_tarea1a_registrar_acta192 as R92           # noqa: E402

SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
VUELTA_QUE_ESCRIBE = 207
CORTE = "7 sep 2026"
SUJETO = 206

# A QUE SECCION Y A QUE PREFIJO DE CLAVE APUNTA EL REPARTO MEDIDO. SON DATOS,
# LEIDOS DEL ACTA EN ESTA VUELTA, Y CADA UNO SE COMPRUEBA CONTRA EL TITULO
# LITERAL DE SU SECCION ANTES DE USARSE: si el titulo no es ese, el computo CAE
# EN ROJO y no escribe nada, en vez de contar sobre la seccion equivocada.
PUNTERIA = [
    ("adjudicaciones", 6, "LO QUE ADJUDICO", "6."),
    ("hallazgos", 7, "HALLAZGOS QUE SUBEN", "7."),
    ("caidas propias del auditor", 9, "MIS CAIDAS, CON SU NOMBRE", "C."),
    ("caidas del ejecutor", 4, "LAS CAIDAS DEL EJECUTOR", "E."),
]


def reparto_medido(lineas, secs, w):
    """EL REPARTO MEDIDO: para cada numeral, (seccion, claves, donde), APUNTANDO
    EL LECTOR IMPORTADO A LA SECCION Y AL PREFIJO QUE ESTA ACTA USA DE VERDAD.

    Devuelve (mapa, motivos). `motivos` no vacio es ROJO: quiere decir que el
    titulo literal de una seccion NO es el que este computo creia, y entonces no
    se cuenta nada sobre ella. NO ES UN LECTOR NUEVO: es
    `R84.claves_entrecomilladas()` con otro prefijo."""
    mapa, motivos = {}, []
    por_numero = {s[0]: s for s in secs}
    for etiqueta, num, titulo_esperado, prefijo in PUNTERIA:
        sec = por_numero.get(num)
        if sec is None:
            motivos.append("la seccion %d no existe en el cuerpo del acta" % num)
            continue
        if titulo_esperado not in sec[2]:
            motivos.append("la seccion %d se titula %r y no contiene %r"
                           % (num, sec[2], titulo_esperado))
            continue
        claves = R84.claves_entrecomilladas(lineas, sec[3], sec[4], prefijo,
                                            plantilla=REP.PLANTILLA_ANCHA)
        donde = {}
        for clave, _n in claves:
            pat = re.compile(REP.PLANTILLA_ANCHA % re.escape(clave))
            donde[clave] = [i for i in range(sec[3], sec[4] + 1)
                            if pat.match(lineas[i - 1])]
        mapa[etiqueta] = dict(sec=sec, prefijo=prefijo, claves=claves, donde=donde)
        w("   %-28s seccion %-2d linea %5d prefijo %-3s -> %d (%s)"
          % (etiqueta, num, sec[1], prefijo, len(claves),
             ", ".join(c for c, _n in claves) or "ninguna"))
    return mapa, motivos


def preguntas_a_mano(w):
    """LAS CLAVES `P.n` DE LA SECCION DE PREGUNTAS DEL REPORTE ARCHIVADO DE LA
    206, CONTADAS A MANO PORQUE EL LECTOR HEREDADO NO VE ESA SECCION.

    COMO CUENTO, DICHO PARA QUE SE PUEDA RECONTAR SIN CORRER NADA:
      1. busco TODA seccion `## N. TITULO` cuyo TITULO nombre PREGUNTAS, SIN
         exigir que la palabra vaya pegada al numero;
      2. la acoto hasta la siguiente `## N.`;
      3. saco las claves `P.n` en LAS DOS FORMAS de esta campana, con comillas
         inversas y sin ellas.
    SI EL PATRON NO HALLA NADA se dice EL PATRON NO ENCONTRO NADA."""
    ruta = os.path.join(LOOP, "reportes", "REPORTE_V%d.md" % SUJETO)
    if not os.path.isfile(ruta):
        w("   EL PATRON NO ENCONTRO EL FICHERO en esa ruta. La cifra no se publica.")
        return None, None
    lineas = io.open(ruta, encoding="utf-8").read().replace(
        chr(13) + NL, NL).split(NL)
    cab = [(i, l) for i, l in enumerate(lineas, 1) if re.match(r"^##\s+\d+\.", l)]
    conpreg = [(i, l) for i, l in cab if "PREGUNTAS" in l.upper()]
    w("   CIFRA secciones `## N.` en el reporte archivado: %d" % len(cab))
    w("   CIFRA de ellas cuyo TITULO nombra PREGUNTAS: %d" % len(conpreg))
    for i, l in conpreg:
        w("      linea %d | %s" % (i, l.strip()))
    if len(conpreg) != 1:
        w("   EL PATRON NO ENCONTRO EXACTAMENTE UNA. La cifra no se publica.")
        return None, None
    a0 = conpreg[0][0]
    sig = [i for i, _l in cab if i > a0]
    b0 = (sig[0] - 1) if sig else len(lineas)
    claves = []
    for i in range(a0, b0 + 1):
        for mm in re.finditer(r"`(P\.\d+)`|\*\*(P\.\d+)\.", lineas[i - 1]):
            c = mm.group(1) or mm.group(2)
            if c not in claves:
                claves.append(c)
                w("      linea %d clava %s | %s" % (i, c, lineas[i - 1].strip()[:88]))
    w("   CIFRA claves `P.n` contadas a mano: %d (%s)"
      % (len(claves), ", ".join(claves) or "ninguna"))
    return claves, (conpreg[0][1].strip(), a0, b0)


def armar_entrada(numero, m, medido, preg_mano, preg_sec, w):
    """COMPONE EL TEXTO DE `R.71`. No lee nada: recibe lo ya medido."""
    lineas = m["lineas"]
    adj_v = m.get("adjudicaciones")      # lo que la VARA saco (seccion 5)
    hal_v = m.get("hallazgos")
    cau_v = m.get("caidas_del_auditor")
    cej_v = m.get("caidas_del_ejecutor")
    p = []
    a = p.append
    a("## R.%d. %s" % (numero, REG206.titulo_de(m, SUJETO)))
    a("")
    a("(Acta del auditor, vuelta %d; escrito en la vuelta %d, TAREA 1.)"
      % (SUJETO, VUELTA_QUE_ESCRIBE))
    a("")
    a("Por adicion, como `R.21` a `R.70`. **Corte de todas las cifras de esta")
    a("entrada: %s.** El numero de esta entrada NO esta tecleado: lo computa" % CORTE)
    a("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    a("Salida: `docs/loop/SALIDA_V%d_T1_REGISTROS.txt`." % VUELTA_QUE_ESCRIBE)
    a("")
    a("**ESTA ENTRADA DECLARA QUE CORRIO LA VARA DEL `4.1` DEL ACTA 202 Y QUE SOBRE")
    a("ESTA ACTA LA VARA NO ALCANZA, Y LO DICE EN VEZ DE PUBLICAR SUS CEROS.** La")
    a("vara es *el numeral se toma de la seccion cuyo PROPIO TITULO lo nombra,")
    a("NUNCA del numero de seccion*, y es **obligatoria para toda acta ANTERIOR a")
    a("la 184**. El acta 206 es POSTERIOR y escribe sus claves con comillas")
    a("inversas, pero **los titulos de sus secciones no son los que las marcas del")
    a("lector buscan**, y por eso cuatro de los cinco numerales salen vacios o")
    a("apuntando a otra seccion. **CADA UNO SE DECLARA CON SU MOTIVO MEDIDO**, y")
    a("**el reparto medido va DEBAJO, marcado como MEDICION y no como numeral**")
    a("(acta 204 `4.6`).")
    a("")
    a("**NINGUN LECTOR NUEVO PERMANENTE SE ESCRIBIO PARA ESTA ENTRADA Y NINGUNO SE")
    a("CLONO.** Rige la MORATORIA DE MAQUINARIA (`AUDITOR.md` 6.3). El computo vive")
    a("en `scripts/loop/_v%d_t1_registros.py`, con prefijo de guion bajo, **fuera"
      % VUELTA_QUE_ESCRIBE)
    a("del censo y fuera de la nomina**, y IMPORTA")
    a("`scripts/loop/_v203_reparto_de_actas_viejas.py` (el mismo de la 203, la 204")
    a("y la 206), `serie_de_registros.py`, `vuelta184_tarea1a_registrar_acta184.py`")
    a("y `scripts/loop/_v206_t2_registros.py`. **IMPORTAR NO ES CLONAR** (acta 206")
    a("`6.5`). Lo unico que este computo cambia es **a que seccion y a que prefijo")
    a("de clave se apunta el lector**, que es un dato y no una maquina.")
    a("")
    a("**EL ACTA ACOTADA EN ESTA VUELTA:** lineas **%d** a **%d**, **%d** lineas,"
      % (m["ini"], m["fin"], m["fin"] - m["ini"] + 1))
    a("sobre un fichero de **%d** bytes en disco y **%d** normalizado a LF. Su"
      % (m["bytes_disco"], m["bytes_lf"]))
    a("cuerpo trae **%d** secciones `## N. TITULO`." % len(m["secs"]))
    a("")
    a("| numeral | seccion que la VARA elige por su TITULO | numero | linea | claves | cuantas |")
    a("|---|---|---:|---:|---|---:|")
    for nombre, dato, motivo in (
            ("adjudicaciones", adj_v,
             "LA VARA ELIGE UNA SECCION QUE NO ES LA DE ADJUDICACIONES"),
            ("hallazgos", hal_v, ""),
            ("caidas propias del auditor", cau_v,
             "NINGUNA SECCION DE ESTA ACTA TITULA ESTE NUMERAL"),
            ("caidas del ejecutor", cej_v,
             "LA SECCION SI SE ENCUENTRA, PERO NINGUNA DE LAS TRES FORMAS VE SUS CLAVES")):
        if dato is None:
            a("| %s | **%s** | (no aplica) | (no aplica) | (no aplica) | **no "
              "computable** |" % (nombre, motivo))
            continue
        sec = dato["sec"]
        claves = ", ".join("`%s`" % c for c, _n in dato["nm"]) or "(ninguna)"
        cuantas = len(dato["nm"])
        if nombre == "hallazgos":
            a("| %s | %s | %d | %d | %s | **%d** |"
              % (nombre, sec[2].replace("|", "/"), sec[0], sec[1], claves, cuantas))
        else:
            a("| %s | %s | %d | %d | %s | **no computable**, %s |"
              % (nombre, sec[2].replace("|", "/"), sec[0], sec[1], claves, motivo))
    a("| preguntas contestadas | (no es una seccion: son las `P.n` que los titulos "
      "de las adjudicaciones nombran, y la seccion de adjudicaciones que la vara "
      "elige no es la de esta acta) | (no aplica) | (no aplica) | (ninguna) | "
      "**no computable** |")
    a("")
    a("**LA VIA DEL NUMERAL DE PREGUNTAS, DICHA Y NO SUPUESTA:** %s."
      % m["via_preguntas"])
    a("`%s` **%s**, y mide **%s** bytes con `os.path.getsize`. **Su seccion de"
      % (m["ruta_rep"], "existe" if m["existe_rep"] else "NO EXISTE",
         m["bytes_rep"]))
    a("preguntas SI existe y el lector heredado NO LA VE**: `%s`."
      % m["seccion_preg"])
    a("")
    a("### EL REPARTO MEDIDO, QUE NO ES EL NUMERAL")
    a("")
    a("**ESTO ES UNA MEDICION Y NO UN NUMERAL** (acta 204 `4.6`). El numeral de")
    a("arriba se queda como esta; esto va debajo y no lo sustituye. **Se cuenta con")
    a("EL MISMO LECTOR IMPORTADO**, `R84.claves_entrecomilladas()` con la plantilla")
    a("ancha, apuntado a la seccion y al prefijo de clave que ESTA acta usa, y")
    a("**cada seccion se comprueba por su titulo literal antes de contar sobre")
    a("ella**.")
    a("")
    a("| numeral | seccion, por su titulo literal | numero | linea | prefijo de clave | claves | cuantas |")
    a("|---|---|---:|---:|---|---|---:|")
    for etiqueta, _num, _tit, _pref in PUNTERIA:
        d = medido.get(etiqueta)
        if d is None:
            a("| %s | (el titulo no calzo y no se conto nada sobre ella) | | | | | |"
              % etiqueta)
            continue
        sec = d["sec"]
        a("| %s | %s | %d | %d | `%s` | %s | **%d** |"
          % (etiqueta, sec[2].replace("|", "/"), sec[0], sec[1], d["prefijo"],
             ", ".join("`%s`" % c for c, _n in d["claves"]) or "(ninguna)",
             len(d["claves"])))
    a("")
    a("**LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO** (`EJECUTOR.md` 2).")
    a("Las dos lecturas quedan escritas: la de la vara arriba y la medida aqui.")
    a("**NINGUN CERO DE UN INSTRUMENTO SE PUBLICA COMO UN HECHO DEL MUNDO**")
    a("(`EJECUTOR.md` 9).")
    a("")
    a("### LAS %d ADJUDICACIONES DEL ACTA 206, UNA POR UNA, CON SU LINEA"
      % len(medido["adjudicaciones"]["claves"]))
    a("")
    a("**EL ENCARGO DE LA VUELTA %d DICE SEIS Y MI MEDICION DICE %d, Y LA"
      % (VUELTA_QUE_ESCRIBE, len(medido["adjudicaciones"]["claves"])))
    a("DISCREPANCIA SE DECLARA EN VEZ DE RESOLVERSE COPIANDO** (`EJECUTOR.md` 2).")
    a("El encargo enumera `6.2` a `6.7` en su punto 1.c y nombra la `6.8` aparte en")
    a("su TAREA 2; la `6.1` no la enumera. **Contadas del acta con el lector")
    a("importado, son %d: de la `6.1` a la `6.8`, todas en la seccion 6.**"
      % len(medido["adjudicaciones"]["claves"]))
    a("")
    a("| clave | pregunta o pendiente que su TITULO nombra | linea | titulo, literal del acta |")
    a("|---|---|---:|---|")
    d = medido["adjudicaciones"]
    for clave, _n in d["claves"]:
        for ln in d["donde"][clave]:
            t = lineas[ln - 1].strip()
            nombradas = re.findall(r"`(P\.\d+|PD\.\d+)`", t)
            a("| `%s` | %s | %d | %s |"
              % (clave,
                 ", ".join("`%s`" % x for x in nombradas) or "(ninguna)",
                 ln, t.replace("|", "/").strip("*")[:200]))
    a("")
    a("### LOS %d HALLAZGOS, LAS %d CAIDAS PROPIAS DEL AUDITOR Y LAS %d DEL EJECUTOR"
      % (len(medido["hallazgos"]["claves"]),
         len(medido["caidas propias del auditor"]["claves"]),
         len(medido["caidas del ejecutor"]["claves"])))
    a("")
    a("| clave | numeral | linea | titulo, literal del acta |")
    a("|---|---|---:|---|")
    for etiqueta in ("hallazgos", "caidas propias del auditor",
                     "caidas del ejecutor"):
        d = medido[etiqueta]
        for clave, _n in d["claves"]:
            for ln in d["donde"][clave]:
                t = lineas[ln - 1].strip()
                a("| `%s` | %s | %d | %s |"
                  % (clave, etiqueta, ln,
                     t.replace("|", "/").strip("*")[:200]))
    a("")
    a("### EL REPARTO MEDIDO DE LAS PREGUNTAS, QUE TAMPOCO ES EL NUMERAL")
    a("")
    if preg_mano is None:
        a("- **EL PATRON NO ENCONTRO LA SECCION**, y eso no dice que no exista.")
    else:
        _t, _a0, _b0 = preg_sec
        a("**COMO SE CONTO, DICHO PARA QUE SE PUEDA RECONTAR SIN CORRER NADA:** en")
        a("`%s` la seccion de preguntas se titula" % m["ruta_rep"])
        a("**%s**, en la linea **%d**, y va hasta la **%d**."
          % (_t.replace("#", "").strip(), _a0, _b0))
        a("")
        a("| lectura | claves `P.n` | cuantas |")
        a("|---|---|---:|")
        a("| **contada a mano en la vuelta %d**, sobre la seccion de preguntas del "
          "reporte archivado | %s | **%d** |"
          % (VUELTA_QUE_ESCRIBE,
             ", ".join("`%s`" % x for x in preg_mano) or "(ninguna)",
             len(preg_mano)))
        a("| **nombradas en los TITULOS de las adjudicaciones** de la seccion 6, "
          "que es la via del `4.7` del acta 201 | %s | **%d** |"
          % (", ".join("`%s`" % x for x in m["nombradas_medidas"]) or "(ninguna)",
             len(m["nombradas_medidas"])))
        a("| **nombradas en el CUERPO de la seccion 6**, contando `P.n` y `PD.n` "
          "| %s | **%d** |"
          % (", ".join("`%s`" % x for x in m["cuerpo_6"]) or "(ninguna)",
             len(m["cuerpo_6"])))
        a("| el lector heredado, `REP.preguntas_del_reporte()`, publicado como "
          "contraste | el patron no encontro nada | 0 |")
        a("")
        a("**LAS TRES PREGUNTAS DEL REPORTE DE LA 206 QUEDAN CONTESTADAS EN EL ACTA,")
        a("Y ESO SE MIDE:** `P.1` en el cuerpo de la `6.1`, `P.2` en el de la `6.2`")
        a("y `P.3` en el TITULO de la `6.3`. **Por la via del `4.7` solo la `P.3`")
        a("cuenta**, porque es la unica que un titulo nombra. **Las dos cifras")
        a("quedan escritas y no se elige una en silencio.**")
    a("")
    a("### LAS TRES QUE CIERRAN PENDIENTES QUE VENIAN ARRASTRANDOSE")
    a("")
    a("- **`6.3` cierra la `P.3`** del reporte de la 206, y **con medicion**:")
    a("  `archivar_reporte.py` acepta `--commit`, pero `cerrar_reporte.py` **no")
    a("  tiene ningun argumento de ruta**, asi que el cierre tardio solo puede")
    a("  hacerse sobre `docs/loop/REPORTE.md`. **La `C.2` de aquel reporte NO")
    a("  cuenta como caida del ejecutor.**")
    a("- **`6.4` cierra la `PD.1`**: una columna de apertura reconstruida vale **si")
    a("  y solo si la propia celda publica que es reconstruccion, con su commit y")
    a("  su prueba al lado**.")
    a("- **`6.5` cierra la `PD.2`**: **importar no es clonar**, como letra general")
    a("  y no solo para un envoltorio.")
    a("")
    a("### LA METRICA DE CREDITO, PEGADA ENTERA Y NO EXTRAIDA")
    a("")
    a("**`R95.cifras_de_la_fila_de_puestos()` devuelve `%s` sobre la fila de "
      "puestos de este cuerpo.** Cuando no alcanza, la fila se PEGA con su numero "
      "de linea, que es cita y no celda tecleada." % (m["lectura_puestos"],))
    a("")
    if not m["filas"]:
        a("- (ninguna fila de metrica con esos prefijos en este cuerpo)")
    for ln, s in m["filas"]:
        a("- (linea %d) %s" % (ln, s))
    a("")
    a("**EL CONTRASTE HEREDADO DEL REPARTO POR NEGRITA, TAMBIEN AL LADO:**")
    a("`R92.caidas_por_lead_heredado()` da **%d** del ejecutor, **%d** del auditor"
      % (len(m["eje_h"]), len(m["aud_h"])))
    a("y **%d** huerfanas sobre este mismo cuerpo. **Esa cifra de %d del ejecutor"
      % (len(m["hue_h"]), len(m["eje_h"])))
    a("NO son seis caidas del ejecutor:** corre sobre el CUERPO ENTERO y reparte")
    a("por la negrita que atribuye, no por la seccion. **Se publica como contraste")
    a("y no como numeral.**")
    a("")
    return NL.join(p) + NL


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    ap.add_argument("--salida", default="T1_REGISTROS")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 1: R.71 PARA EL ACTA %d" % (VUELTA_QUE_ESCRIBE, SUJETO))
    w("=" * 78)
    w("")
    w("0) LA PRUEBA POR MUTACION DEL ENSANCHE, ANTES DE ESCRIBIR NADA.")
    w("   Es la MISMA del computo de la 203, porque es el MISMO fichero IMPORTADO:")
    w("   vuelve a correr aqui en vez de heredar su verde de otra corrida.")
    ok = REP.prueba_por_mutacion(w)
    w("   VEREDICTO DE LA PRUEBA: %s" % ("VERDE" if ok else "ROJO"))
    w("")
    if not ok:
        w("   ROJO: la prueba por mutacion no salio verde. NO SE ESCRIBE NADA.")
        print(NL.join(L))
        return 1

    d0, lf0, sha0, texto0 = REG206.dos_convenciones(SEDE)
    w("A) LA SEDE AL ENTRAR, POR LAS DOS CONVENCIONES")
    w("   docs/PENDIENTES.md: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (d0, lf0, sha0))
    w("   CIFRA lineas por split(NL): %d" % len(texto0.split(NL)))
    w("")

    w("B) EL NUMERO, COMPUTADO Y NO TECLEADO, RECOMPUTANDO LA SERIE AHORA")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    w("   CIFRA entradas de la serie ANTES: %d" % len(halladas))
    w("   CIFRA colisiones ANTES: %d" % len(SERIE.colisiones(halladas)))
    w("   CIFRA huecos ANTES: %d" % len(SERIE.huecos(halladas)))
    w("   SIGUIENTE LIBRE: R.%d" % numero)
    w("")

    w("C) EL CUERPO DEL ACTA Y SUS NUMERALES POR LA VARA, TAL CUAL Y SIN RETOCAR")
    m = REP.medir_acta(SUJETO, w)
    w("")
    if m is None:
        w("   ROJO: no se pudo acotar el acta %d. NO SE ESCRIBE." % SUJETO)
        print(NL.join(L))
        return 1

    w("C.1) EL REPARTO MEDIDO, CON EL MISMO LECTOR APUNTADO A LA SECCION Y AL")
    w("     PREFIJO DE CLAVE QUE ESTA ACTA USA DE VERDAD")
    medido, motivos = reparto_medido(m["lineas"], m["secs"], w)
    w("   CIFRA motivos de rojo del reparto medido: %d" % len(motivos))
    for mo in motivos:
        w("      " + mo)
    if motivos:
        w("   ROJO: un titulo literal no calzo. NO SE ESCRIBE NADA.")
        print(NL.join(L))
        return 1
    w("")

    w("C.2) LOS CUATRO NUMERALES QUE LA VARA NO PUEDE DAR, DECLARADOS UNO A UNO")
    w("     EN VEZ DE PUBLICAR SUS CEROS")
    adj_sec = m.get("adjudicaciones_sec")
    w("   ADJUDICACIONES: la vara elige la seccion %s, titulada %r, que NO es la"
      % (adj_sec[0] if adj_sec else "(ninguna)",
         adj_sec[2] if adj_sec else ""))
    w("   seccion de adjudicaciones de esta acta. Sus claves por la vara: %d."
      % (len(m["adjudicaciones"]["nm"]) if m.get("adjudicaciones") else 0))
    w("   -> NO COMPUTABLE. Publicar ese 0 diria que el acta 206 no adjudico nada.")
    w("   CAIDAS PROPIAS DEL AUDITOR: ninguna seccion titula el numeral.")
    w("   -> NO COMPUTABLE, y el propio computo importado ya lo declaraba.")
    cej = m.get("caidas_del_ejecutor")
    if cej:
        w("   CAIDAS DEL EJECUTOR: seccion %d encontrada, titulada %r."
          % (cej["sec"][0], cej["sec"][2]))
        w("   claves por la vara `%d.M`: %d | por `CAIDA n`: %d | por lead: %d"
          % (cej["sec"][0], len(cej["nm"]), len(cej["viejas"]), len(cej["leads"])))
        w("   -> NO COMPUTABLE por ninguna de las tres formas, sobre una seccion")
        w("      cuyo propio titulo dice DOS.")
    w("   PREGUNTAS: el lector heredado dice %r" % m["seccion_preg"])
    w("   -> NO COMPUTABLE por esa via.")
    w("")

    w("C.3) LAS PREGUNTAS, CONTADAS A MANO SOBRE EL REPORTE ARCHIVADO DE LA 206")
    preg_mano, preg_sec = preguntas_a_mano(w)
    w("")

    w("C.4) LAS `P.n` Y `PD.n` QUE LA SECCION 6 NOMBRA, MEDIDAS")
    d6 = medido["adjudicaciones"]
    nombradas = []
    for clave, _n in d6["claves"]:
        for ln in d6["donde"][clave]:
            for mm in re.finditer(r"`(P\.\d+)`", m["lineas"][ln - 1]):
                if mm.group(1) not in nombradas:
                    nombradas.append(mm.group(1))
    cuerpo_6 = []
    for i in range(d6["sec"][3], d6["sec"][4] + 1):
        for mm in re.finditer(r"`(P\.\d+|PD\.\d+)`", m["lineas"][i - 1]):
            if mm.group(1) not in cuerpo_6:
                cuerpo_6.append(mm.group(1))
    w("   CIFRA `P.n` nombradas en los TITULOS de las adjudicaciones: %d (%s)"
      % (len(nombradas), ", ".join(nombradas) or "ninguna"))
    w("   CIFRA `P.n` y `PD.n` en el CUERPO de la seccion 6: %d (%s)"
      % (len(cuerpo_6), ", ".join(cuerpo_6) or "ninguna"))
    m["nombradas_medidas"] = nombradas
    m["cuerpo_6"] = cuerpo_6
    w("")

    w("D) EL TITULO. LOS NUMERALES NO COMPUTABLES SE FUERZAN A `None` PARA QUE EL")
    w("   TITULO NO PUBLIQUE UN CERO FALSO, Y LA LECTURA CRUDA QUEDA ARRIBA ENTERA")
    w("   lo que la vara dio, ANTES de forzar: adjudicaciones %s | caidas del "
      "ejecutor %s"
      % (len(m["adjudicaciones"]["nm"]) if m.get("adjudicaciones") else None,
         len(cej["viejas"]) if cej else None))
    m["adjudicaciones"] = None
    m["caidas_del_ejecutor"] = None
    m["preguntas_numeral"] = None
    titulo = REG206.titulo_de(m, SUJETO)
    w("   TITULO ESCRITO: %s" % titulo)
    w("")

    w("E) LA SEDE Y LA IDEMPOTENCIA")
    texto_sede = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    ya = REG206.ya_escrita(texto_sede, numero, SUJETO)
    w("   la entrada del acta %d o el numero R.%d YA ESTAN: %s"
      % (SUJETO, numero, "SI" if ya else "NO"))
    entrada = armar_entrada(numero, m, medido, preg_mano, preg_sec, w)
    w("   CIFRA bytes de la entrada compuesta: %d" % len(entrada.encode("utf-8")))
    w("   CIFRA lineas de la entrada compuesta: %d" % entrada.count(NL))
    escritas = []
    if a.escribir and not ya:
        nuevo = texto_sede
        if not nuevo.endswith(NL):
            nuevo += NL
        nuevo += NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("   ESCRITA: R.%d anadida al final de docs/PENDIENTES.md" % numero)
        escritas.append((numero, SUJETO))
    elif a.escribir:
        w("   NO SE ESCRIBE: la entrada ya estaba. IDEMPOTENTE.")
    else:
        w("   MODO MEDICION: no se escribe nada.")
    w("")

    w("=" * 78)
    w("EL CIERRE, REMEDIDO Y NO HEREDADO")
    w("=" * 78)
    d1, lf1, sha1, texto1 = REG206.dos_convenciones(SEDE)
    w("   docs/PENDIENTES.md al salir: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (d1, lf1, sha1))
    w("   CIFRA crecimiento en bytes de disco: %d" % (d1 - d0))
    w("   CIFRA crecimiento en bytes LF: %d" % (lf1 - lf0))
    w("   CIFRA lineas al salir: %d (al entrar %d, crecimiento %d)"
      % (len(texto1.split(NL)), len(texto0.split(NL)),
         len(texto1.split(NL)) - len(texto0.split(NL))))
    w("   CIFRA entradas escritas por esta corrida: %d" % len(escritas))
    for num, vue in escritas:
        w("      R.%d  ->  acta de la vuelta %d" % (num, vue))
    w("")
    w("LA GUARDA DEL TEXTO VIEJO: NI UNA LINEA BORRADA NI UNA CAMBIADA")
    viejas = texto0.split(NL)
    nuevas = texto1.split(NL)
    faltan = 0
    j = 0
    for l in viejas:
        while j < len(nuevas) and nuevas[j] != l:
            j += 1
        if j >= len(nuevas):
            faltan += 1
        else:
            j += 1
    w("   CIFRA lineas del texto de ENTRADA que NO estan, en orden, en el de")
    w("   SALIDA: %d" % faltan)
    w("   (la adicion solo puede ANADIR: si esta cifra no es 0, es ROJO)")
    w("")
    despues = SERIE.entradas()
    w("LA SERIE AL CIERRE, RECOMPUTADA Y NO HEREDADA")
    w("   CIFRA entradas de la serie DESPUES: %d" % len(despues))
    w("   CIFRA colisiones DESPUES: %d" % len(SERIE.colisiones(despues)))
    w("   CIFRA huecos DESPUES: %d" % len(SERIE.huecos(despues)))
    w("   SIGUIENTE LIBRE DESPUES: R.%d" % SERIE.siguiente_libre(despues))
    w("")
    con = set()
    for _n, _rel, _ln, titulo_e in despues:
        for mm in re.finditer(r"del acta de la vuelta (\d+)", titulo_e):
            con.add(int(mm.group(1)))
    sin = sorted(v for v in range(173, 207) if v not in con)
    w("LA DEUDA DE REGISTROS, REMEDIDA AL CIERRE Y ENSANCHADA HASTA LA 206")
    w("   CIFRA actas de la 173 a la 206 SIN entrada propia: %d" % len(sin))
    w("   cuales: %s" % (", ".join(str(x) for x in sin) or "(ninguna)"))
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt"
                         % (VUELTA_QUE_ESCRIBE, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
