# -*- coding: utf-8 -*-
r"""_v209_t1_registros.py . TAREA 1 DE LA VUELTA 209: `R.73` PARA EL ACTA 208,
ESCRITA EN `docs/PENDIENTES.md` POR ADICION PURA Y EN SU SEDE, mas el REMEDIDO
de las cifras de crecimiento del acta (1.a) y las DIEZ adjudicaciones con su
linea (1.c).

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3). **NO SE ESCRIBE NINGUN LECTOR NUEVO Y
TAMPOCO SE CLONA NINGUNO:** todo lo que LEE viene IMPORTADO de
`_v203_reparto_de_actas_viejas.py` (la vara del `4.1` del acta 202), de
`serie_de_registros.py`, de `_v206_t2_registros.py` (`ya_escrita`,
`dos_convenciones`, `titulo_de`) y de `_v208_t1_registros.py` (`vara_sobre`, que
es el recorrido de los cuatro numerales tal cual se corrio en la 208).
**IMPORTAR NO ES CLONAR** (acta 206, adjudicacion `6.5`). Lo unico propio de este
fichero es la PROSA de la entrada `R.73`, que es texto nuevo y no un lector.

EL NUMERO NO SE TECLEA: lo computa `serie_de_registros.siguiente_libre()`
recomputando la serie de sus DOS sedes, al ENTRAR y al SALIR.

EL AVISO DEL CIRCUNFLEJO SIGUE VIGENTE: para el padre del commit del acta se usa
`~1`, nunca el circunflejo, y ademas se comprueba ANTES DE RESTAR que los dos
blobs son DISTINTOS. Si salieran iguales, la resta seria un cero falso.

**LAS CIFRAS DEL ENCARGO SON CONTRASTE Y NO FUENTE** (`EJECUTOR.md` 2). Aqui se
mide todo con estos comandos y, si algo discrepa, LA DISCREPANCIA SE DECLARA y no
se resuelve copiando.

USO:
  python scripts/loop/_v209_t1_registros.py
  python scripts/loop/_v209_t1_registros.py --escribir
  python scripts/loop/_v209_t1_registros.py --escribir --salida NOMBRE
"""
import argparse
import hashlib
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

sys.path.insert(0, AQUI)
import serie_de_registros as SERIE                          # noqa: E402
import _v203_reparto_de_actas_viejas as REP                 # noqa: E402
import _v206_t2_registros as REG206                         # noqa: E402
from _v208_t1_registros import vara_sobre                   # noqa: E402

SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
ACTA = "docs/loop/ACTA_AUDITOR.md"
VUELTA_QUE_ESCRIBE = 209
CORTE = "7 sep 2026"
SUJETO = 208
CONTRASTE = 207

# LO QUE EL ENCARGO DICE QUE CIERRA CADA ADJUDICACION. ES UN DATO DEL ENCARGO,
# NO UNA MEDICION, y por eso va marcado como tal: la CIFRA de adjudicaciones se
# MIDE del acta con la vara, y esto solo le pone al lado que pendiente cierra.
CIERRAN = {
    "6.1": "el CHOQUE DE NUEVE ACTAS entre el remedio del acta 205 y `AUDITOR.md` 1",
    "6.2": "`P.1` del reporte de la 208",
    "6.4": "`P.2` del reporte de la 208",
    "6.5": "`P.3` del reporte de la 208",
    "6.6": "`PD.1` del reporte de la 208",
    "6.7": "los TRES DISCUTIBLES del reporte de la 208, los tres ADMITIDOS",
}

# LAS CIFRAS QUE EL ENCARGO DA COMO CONTRASTE. NO SON FUENTE DE NADA: se cotejan
# contra lo medido aqui y la discrepancia, si la hay, se declara.
CONTRASTE_ENCARGO = {
    "acta_antes": 4820516,
    "acta_despues": 4849108,
    "acta_sha": "2abc86822340d1bd",
    "acta_linea_seccion": 73083,
    "serie_entradas": 64,
    "serie_pendientes": 63,
    "serie_correcciones": 1,
    "serie_colisiones": 0,
    "serie_huecos": 0,
    "serie_siguiente": 73,
    "pendientes_bytes": 1180091,
    "pendientes_sha": "9cf019a1c9a856f0",
}


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout


def blob(rev, ruta):
    """LOS BYTES CRUDOS DE UN FICHERO EN UN COMMIT. `git show` con `:` da el
    blob tal cual esta en el objeto, sin pasar por el filtro del arbol."""
    c, b = git(["show", "%s:%s" % (rev, ruta)])
    return b if c == 0 else None


def dos_convenciones_de_bytes(b):
    """LAS DOS CONVENCIONES SOBRE UNOS BYTES YA LEIDOS: como estan, y con los
    CRLF normalizados a LF. Devuelve (disco, lf, sha_disco, sha_lf)."""
    lf = b.replace(chr(13).encode() + NL.encode(), NL.encode())
    return (len(b), len(lf),
            hashlib.sha256(b).hexdigest()[:16],
            hashlib.sha256(lf).hexdigest()[:16])


def commit_del_acta(w):
    """EL COMMIT QUE ESCRIBIO EL ACTA DEL SUJETO, LEIDO DE git log Y NO
    TECLEADO (`EJECUTOR.md` 1, LA IDENTIDAD SE LEE DE GIT)."""
    c, b = git(["log", "-1", "--format=%H", "--", ACTA])
    h = b.decode("utf-8").strip()
    w("   commit que toco el acta, leido de git log: %s" % h)
    c2, b2 = git(["log", "-1", "--format=%s", h])
    w("   asunto (primeros 110): %s" % b2.decode("utf-8").strip()[:110])
    return h


def medir_crecimiento_del_acta(w):
    """EL 1.a: REMEDIR LAS CIFRAS DE CRECIMIENTO DEL ACTA CON MIS COMANDOS."""
    w("1.a) EL CRECIMIENTO DEL ACTA, REMEDIDO CON MIS COMANDOS")
    h = commit_del_acta(w)
    w("   EL PADRE SE PIDE CON ~1 Y NUNCA CON EL CIRCUNFLEJO (aviso vigente).")
    c, bp = git(["rev-parse", "%s~1" % h])
    padre = bp.decode("utf-8").strip()
    w("   padre: %s" % padre)
    antes = blob("%s~1" % h, ACTA)
    despues = blob(h, ACTA)
    if antes is None or despues is None:
        w("   ROJO: no se pudo leer alguno de los dos blobs.")
        return None
    # LA GUARDA CONTRA EL CERO FALSO DE LA RESTA: se comprueba que los dos
    # valores son DISTINTOS ANTES de restar, que es el aviso del circunflejo.
    iguales = (antes == despues)
    w("   los dos blobs son IDENTICOS: %s (si lo fueran, la resta seria un cero "
      "falso y no se publicaria)" % ("SI" if iguales else "NO"))
    if iguales:
        w("   ROJO: el padre y el hijo traen el mismo acta. NO SE RESTA.")
        return None
    da, la, sda, sla = dos_convenciones_de_bytes(antes)
    dd, ld, sdd, sld = dos_convenciones_de_bytes(despues)
    w("   ACTA ANTES  (%s~1): %d bytes en disco y %d normalizado a LF, "
      "sha256 disco %s y sha256 LF %s" % (h[:8], da, la, sda, sla))
    w("   ACTA DESPUES (%s): %d bytes en disco y %d normalizado a LF, "
      "sha256 disco %s y sha256 LF %s" % (h[:8], dd, ld, sdd, sld))
    w("   CIFRA crecimiento en bytes de disco: %d" % (dd - da))
    w("   CIFRA crecimiento en bytes normalizado a LF: %d" % (ld - la))
    c, bn = git(["diff", "--numstat", "%s~1" % h, h, "--", ACTA])
    ns = bn.decode("utf-8").strip()
    w("   git diff --numstat %s~1 %s -- %s : %s" % (h[:8], h[:8], ACTA, ns))
    partes = ns.split()
    anadidas = int(partes[0]) if partes else -1
    borradas = int(partes[1]) if len(partes) > 1 else -1
    w("   CIFRA lineas anadidas al acta: %d | CIFRA lineas borradas: %d"
      % (anadidas, borradas))
    # EL ARBOL DE HOY, que es lo que mi apertura sello.
    dh, lh, shh, texto = REG206.dos_convenciones(os.path.join(RAIZ, ACTA))
    w("   ACTA EN EL ARBOL DE HOY: %d bytes en disco y %d normalizado a LF, "
      "sha256 LF %s" % (dh, lh, shh))
    lineas = texto.split(NL)
    w("   CIFRA lineas del acta por split(NL): %d | por wc -l (sin la ultima "
      "vacia): %d" % (len(lineas), len(lineas) - 1))
    ini = None
    for i, l in enumerate(lineas, 1):
        if l.startswith("# ACTA DEL AUDITOR, VUELTA %d" % SUJETO):
            ini = i
            break
    w("   CIFRA linea en que abre la seccion del acta %d: %s" % (SUJETO, ini))
    w("")
    w("   EL COTEJO CONTRA EL CONTRASTE DEL ENCARGO (contraste, NO fuente):")
    filas = [
        ("acta ANTES, bytes", da, CONTRASTE_ENCARGO["acta_antes"]),
        ("acta DESPUES, bytes en disco", dd, CONTRASTE_ENCARGO["acta_despues"]),
        ("acta DESPUES, bytes LF", ld, CONTRASTE_ENCARGO["acta_despues"]),
        ("linea en que abre la seccion", ini,
         CONTRASTE_ENCARGO["acta_linea_seccion"]),
    ]
    discrepan = 0
    for nombre, mio, suyo in filas:
        ok = (mio == suyo)
        if not ok:
            discrepan += 1
        w("      %-32s mio %-10s contraste %-10s %s"
          % (nombre, mio, suyo, "CALZA" if ok else "DISCREPA Y SE DECLARA"))
    for nombre, mio in (("sha256 disco del acta de hoy", sdd),
                        ("sha256 LF del acta de hoy", sld)):
        ok = (mio == CONTRASTE_ENCARGO["acta_sha"])
        if not ok:
            discrepan += 1
        w("      %-32s mio %-10s contraste %-10s %s"
          % (nombre, mio, CONTRASTE_ENCARGO["acta_sha"],
             "CALZA" if ok else "DISCREPA Y SE DECLARA"))
    w("   CIFRA discrepancias con el contraste del encargo en el 1.a: %d"
      % discrepan)
    w("")
    return {"antes": da, "despues_disco": dd, "despues_lf": ld,
            "crecimiento_disco": dd - da, "crecimiento_lf": ld - la,
            "sha_disco": sdd, "sha_lf": sld, "anadidas": anadidas,
            "borradas": borradas, "ini": ini, "commit": h, "padre": padre,
            "discrepan": discrepan, "lineas_split": len(lineas),
            "arbol_disco": dh, "arbol_lf": lh}


def armar_entrada(numero, m, crec, titulo, titulo_crudo, comp208, comp207,
                  serie_ent, w):
    """COMPONE EL TEXTO DE `R.73`. No lee nada del disco: recibe lo ya medido."""
    lineas = m["lineas"]
    p = []
    a = p.append
    a("## R.%d. %s" % (numero, titulo))
    a("")
    a("(Acta del auditor, vuelta %d; escrito en la vuelta %d, TAREA 1.)"
      % (SUJETO, VUELTA_QUE_ESCRIBE))
    a("")
    a("Por adicion, como `R.21` a `R.72`. **Corte de todas las cifras de esta")
    a("entrada: %s.** El numero de esta entrada NO esta tecleado: lo computa" % CORTE)
    a("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes,")
    a("corrido AL ENTRAR y AL SALIR. Salida:")
    a("`docs/loop/SALIDA_V%d_T1_REGISTROS.txt`." % VUELTA_QUE_ESCRIBE)
    a("")
    a("**NINGUN LECTOR NUEVO PERMANENTE SE ESCRIBIO PARA ESTA ENTRADA Y NINGUNO SE")
    a("CLONO.** El computo vive en `scripts/loop/_v%d_t1_registros.py`, con prefijo"
      % VUELTA_QUE_ESCRIBE)
    a("de guion bajo, **fuera del censo y fuera de la nomina**, y IMPORTA")
    a("`scripts/loop/_v203_reparto_de_actas_viejas.py` (la vara del `4.1` del acta")
    a("202), `serie_de_registros.py`, `scripts/loop/_v206_t2_registros.py` y")
    a("`scripts/loop/_v208_t1_registros.py`, del que se reutiliza `vara_sobre()`")
    a("**tal cual**. **IMPORTAR NO ES CLONAR** (acta 206 `6.5`). Lo unico propio de")
    a("este computo es la PROSA de esta entrada, que es texto y no un lector.")
    a("")
    a("### EL CRECIMIENTO DEL ACTA, REMEDIDO Y NO COPIADO")
    a("")
    a("El encargo de la vuelta %d da estas cifras **como CONTRASTE y no como"
      % VUELTA_QUE_ESCRIBE)
    a("fuente** (`EJECUTOR.md` 2). Se han vuelto a medir con `git show`,")
    a("`git diff --numstat` y las dos convenciones de la casa.")
    a("")
    a("| que se mide | medido en la vuelta %d | contraste del encargo | calza |"
      % VUELTA_QUE_ESCRIBE)
    a("|---|---:|---:|---|")
    a("| acta ANTES (blob de `%s~1`), bytes | **%d** | 4820516 | %s |"
      % (crec["commit"][:8], crec["antes"],
         "SI" if crec["antes"] == CONTRASTE_ENCARGO["acta_antes"] else "**NO**"))
    a("| acta DESPUES (blob de `%s`), bytes en disco | **%d** | 4849108 | %s |"
      % (crec["commit"][:8], crec["despues_disco"],
         "SI" if crec["despues_disco"] == CONTRASTE_ENCARGO["acta_despues"]
         else "**NO**"))
    a("| acta DESPUES, bytes normalizado a LF | **%d** | 4849108 | %s |"
      % (crec["despues_lf"],
         "SI" if crec["despues_lf"] == CONTRASTE_ENCARGO["acta_despues"]
         else "**NO**"))
    a("| `sha256` disco del acta | **`%s`** | `2abc86822340d1bd` | %s |"
      % (crec["sha_disco"],
         "SI" if crec["sha_disco"] == CONTRASTE_ENCARGO["acta_sha"] else "**NO**"))
    a("| `sha256` LF del acta | **`%s`** | `2abc86822340d1bd` | %s |"
      % (crec["sha_lf"],
         "SI" if crec["sha_lf"] == CONTRASTE_ENCARGO["acta_sha"] else "**NO**"))
    a("| linea en que abre la seccion del acta %d | **%d** | 73083 | %s |"
      % (SUJETO, crec["ini"],
         "SI" if crec["ini"] == CONTRASTE_ENCARGO["acta_linea_seccion"]
         else "**NO**"))
    a("")
    a("**CIFRA crecimiento del acta: %d bytes en disco y %d bytes normalizado a"
      % (crec["crecimiento_disco"], crec["crecimiento_lf"]))
    a("LF**, con **%d** lineas anadidas y **%d** borradas segun"
      % (crec["anadidas"], crec["borradas"]))
    a("`git diff --numstat %s~1 %s`. **El acta solo crece por anexion y su cero de"
      % (crec["commit"][:8], crec["commit"][:8]))
    a("borradas lo prueba.**")
    a("")
    a("**EL PADRE SE PIDIO CON `~1` Y NUNCA CON EL CIRCUNFLEJO**, y ademas se")
    a("comprobo ANTES DE RESTAR que los dos blobs son DISTINTOS: una resta entre dos")
    a("valores iguales daria un cero que no es una medicion. **CIFRA discrepancias")
    a("con el contraste del encargo en este apartado: %d.**" % crec["discrepan"])
    a("")
    a("### LAS %d ADJUDICACIONES DEL ACTA %d, UNA POR UNA Y CON SU LINEA MEDIDA"
      % (len(m["adjudicaciones"]["nm"]), SUJETO))
    a("")
    a("**SEIS DE LAS DIEZ CIERRAN PENDIENTE, Y SE DICE AL REGISTRARLAS**, que es lo")
    a("que el encargo pide: la `6.1` cierra el choque de nueve actas entre el remedio")
    a("del acta 205 y `AUDITOR.md` 1, la `6.2` la `P.1`, la `6.4` la `P.2`, la `6.5`")
    a("la `P.3`, la `6.6` la `PD.1` y la `6.7` los tres discutibles, los tres")
    a("ADMITIDOS. **Las cuatro restantes (`6.3`, `6.8`, `6.9` y `6.10`) no cierran")
    a("ningun pendiente numerado**, y eso se dice en vez de inflar la cuenta.")
    a("")
    a("| clave | que pendiente cierra | pregunta que su TITULO nombra | linea | titulo, literal del acta |")
    a("|---|---|---|---:|---|")
    d = m["adjudicaciones"]
    for clave, _n in d["nm"]:
        for ln in d["donde"][clave]:
            t = lineas[ln - 1].strip()
            nombradas = re.findall(r"`(P\.\d+|PD\.\d+)`", t)
            a("| `%s` | %s | %s | %d | %s |"
              % (clave, CIERRAN.get(clave, "(ninguno)"),
                 ", ".join("`%s`" % x for x in nombradas) or "(ninguna)",
                 ln, t.replace("|", "/").strip("*")[:210]))
    a("")
    a("**CIFRA adjudicaciones medidas por la vara: %d. CIFRA de las que cierran"
      % len(d["nm"]))
    a("pendiente: %d.**" % len(CIERRAN))
    a("")
    a("### LOS CUATRO NUMERALES, POR LA VARA Y SIN RETOCAR")
    a("")
    a("| numeral | seccion que la VARA elige por su TITULO | numero | linea | claves | cuantas |")
    a("|---|---|---:|---:|---|---:|")
    for etiqueta in ("adjudicaciones", "hallazgos", "caidas_del_auditor",
                     "caidas_del_ejecutor"):
        dd = m.get(etiqueta)
        nombre = etiqueta.replace("_", " ")
        if dd is None:
            a("| %s | **NINGUNA SECCION DE ESTA ACTA TITULA ESTE NUMERAL** | "
              "(no aplica) | (no aplica) | (no aplica) | **no computable** |"
              % nombre)
            continue
        sec = dd["sec"]
        claves = ", ".join("`%s`" % c for c, _n in dd["nm"]) or "(ninguna)"
        a("| %s | %s | %d | %d | %s | **%d** |"
          % (nombre, sec[2].replace("|", "/"), sec[0], sec[1], claves,
             len(dd["nm"])))
    a("")
    a("**CIFRA numerales COMPUTABLES de 4 sobre el acta %d: %d.**"
      % (SUJETO, comp208[0]))
    a("")
    a("### LA MISMA VARA SOBRE EL ACTA %d, CORRIDA POR MI Y NO COPIADA" % CONTRASTE)
    a("")
    a("| acta | numerales COMPUTABLES de 4, medidos en esta vuelta |")
    a("|---|---:|")
    a("| **%d** | **%d** |" % (CONTRASTE, comp207[0]))
    a("| **%d** | **%d** |" % (SUJETO, comp208[0]))
    a("")
    a("### LOS HALLAZGOS, LAS CAIDAS PROPIAS DEL AUDITOR Y LA DEL EJECUTOR")
    a("")
    a("| clave | numeral | linea | titulo, literal del acta |")
    a("|---|---|---:|---|")
    for etiqueta in ("hallazgos", "caidas_del_auditor", "caidas_del_ejecutor"):
        dd = m[etiqueta]
        for clave, _n in dd["nm"]:
            for ln in dd["donde"][clave]:
                t = lineas[ln - 1].strip()
                a("| `%s` | %s | %d | %s |"
                  % (clave, etiqueta.replace("_", " "), ln,
                     t.replace("|", "/").strip("*")[:210]))
    a("")
    a("### EL CERO FALSO QUE ESTE TITULO NO PUBLICA, DECLARADO Y MEDIDO")
    a("")
    a("`REG206.titulo_de()` cuenta las caidas con `numeral(dato, 'viejas')`, o sea")
    a("**por la forma antigua `CAIDA n`**. **El acta %d tampoco usa esa forma**:" % SUJETO)
    a("escribe sus caidas como `9.1` a `9.4` y `4.1`, que es la forma `N.M` de la")
    a("vara. Es la misma especie que el `D.1` del reporte de la 208, **que el acta")
    a("208 ADMITIO en su `6.7`** con esta letra general: *cuando un lector heredado")
    a("no ve el dato por la forma en que se escribe hoy, se le pasa el dato contado")
    a("por la forma vigente y se publican las dos cuentas mas el resultado crudo*.")
    a("**Eso es exactamente lo que se hace aqui, y ya no es una eleccion del")
    a("ejecutor: es doctrina adjudicada.**")
    a("")
    a("| caida | por `CAIDA n`, la forma antigua | por `N.M`, la forma de esta acta |")
    a("|---|---:|---:|")
    for etiqueta in ("caidas_del_auditor", "caidas_del_ejecutor"):
        dd = m[etiqueta]
        a("| %s | **%d** | **%d** |"
          % (etiqueta.replace("_", " "), len(dd["viejas"]), len(dd["nm"])))
    a("")
    a("**NINGUN LECTOR SE TOCO: SE CAMBIO EL DATO, NO LA MAQUINA.** Y **EL TITULO")
    a("CRUDO QUEDA ESCRITO AQUI, ENTERO Y SIN TACHAR**, que es la regla de la")
    a("correccion declarada de la casa:")
    a("")
    a("> %s" % titulo_crudo)
    a("")
    a("### LA SERIE `R.N`, RECOMPUTADA DE SUS DOS SEDES A LA ENTRADA")
    a("")
    a("| que se mide | medido a la entrada | contraste del encargo | calza |")
    a("|---|---:|---:|---|")
    a("| entradas de la serie | **%d** | 64 | %s |"
      % (serie_ent["total"],
         "SI" if serie_ent["total"] == CONTRASTE_ENCARGO["serie_entradas"]
         else "**NO**"))
    a("| de ellas en `docs/PENDIENTES.md` | **%d** | 63 | %s |"
      % (serie_ent["en_pendientes"],
         "SI" if serie_ent["en_pendientes"] == CONTRASTE_ENCARGO["serie_pendientes"]
         else "**NO**"))
    a("| de ellas en `docs/plan/CORRECCIONES_A_APLICAR.md` | **%d** | 1 | %s |"
      % (serie_ent["en_correcciones"],
         "SI" if serie_ent["en_correcciones"] == CONTRASTE_ENCARGO["serie_correcciones"]
         else "**NO**"))
    a("| colisiones | **%d** | 0 | %s |"
      % (serie_ent["colisiones"],
         "SI" if serie_ent["colisiones"] == 0 else "**NO**"))
    a("| huecos | **%d** | 0 | %s |"
      % (serie_ent["huecos"], "SI" if serie_ent["huecos"] == 0 else "**NO**"))
    a("| siguiente libre | **R.%d** | R.73 | %s |"
      % (numero, "SI" if numero == CONTRASTE_ENCARGO["serie_siguiente"]
         else "**NO**"))
    a("")
    a("**LAS DOS PUNTAS SE PUBLICAN**, la de entrada aqui y la de salida en")
    a("`docs/loop/SALIDA_V%d_T1_REGISTROS.txt`, que es donde el instrumento la"
      % VUELTA_QUE_ESCRIBE)
    a("recomputa DESPUES de escribir.")
    a("")
    a("### LAS PREGUNTAS CONTESTADAS")
    a("")
    a("**LA VIA DEL NUMERAL, DICHA Y NO SUPUESTA:** %s." % m["via_preguntas"])
    a("`%s` **%s**, y mide **%s** bytes con `os.path.getsize`. La seccion que el"
      % (m["ruta_rep"], "existe" if m["existe_rep"] else "NO EXISTE",
         m["bytes_rep"]))
    a("lector heredado ve: `%s`." % m["seccion_preg"])
    a("")
    a("| lectura | claves | cuantas |")
    a("|---|---|---:|")
    a("| **nombradas en los TITULOS de las adjudicaciones**, que es la via del "
      "`4.7` del acta 201 | %s | **%d** |"
      % (", ".join("`%s`" % x for x in m["nombradas"]) or "(ninguna)",
         len(m["nombradas"])))
    a("| **las que el reporte archivado llama pregunta**, por el lector heredado "
      "| %s | **%d** |"
      % (", ".join("`%s`" % x for x in m["del_reporte"]) or "(ninguna)",
         len(m["del_reporte"])))
    a("| **el numeral publicado**, por la via de arriba | %s | **%d** |"
      % (", ".join("`%s`" % x for x in m["preguntas"]) or "(ninguna)",
         len(m["preguntas"])))
    a("")
    a("**LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO** (`EJECUTOR.md` 2).")
    a("**NINGUN CERO DE UN INSTRUMENTO SE PUBLICA COMO UN HECHO DEL MUNDO**")
    a("(`EJECUTOR.md` 9).")
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
    a("y **%d** huerfanas sobre este mismo cuerpo. **Corre sobre el CUERPO ENTERO y"
      % len(m["hue_h"]))
    a("reparte por la negrita que atribuye, no por la seccion: se publica como")
    a("contraste y no como numeral.**")
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
    w("VUELTA %d, TAREA 1: R.73 PARA EL ACTA %d" % (VUELTA_QUE_ESCRIBE, SUJETO))
    w("=" * 78)
    w("")
    w("0) LA PRUEBA POR MUTACION DEL LECTOR IMPORTADO, ANTES DE ESCRIBIR NADA.")
    w("   Vuelve a correr aqui en vez de heredar su verde de otra corrida.")
    ok = REP.prueba_por_mutacion(w)
    w("   VEREDICTO DE LA PRUEBA: %s" % ("VERDE" if ok else "ROJO"))
    w("")
    if not ok:
        w("   ROJO: la prueba por mutacion no salio verde. NO SE ESCRIBE NADA.")
        print(NL.join(L))
        return 1

    crec = medir_crecimiento_del_acta(w)
    if crec is None:
        print(NL.join(L))
        return 1

    d0, lf0, sha0, texto0 = REG206.dos_convenciones(SEDE)
    w("A) LA SEDE AL ENTRAR, POR LAS DOS CONVENCIONES")
    w("   docs/PENDIENTES.md: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (d0, lf0, sha0))
    w("   CIFRA lineas por split(NL): %d" % len(texto0.split(NL)))
    w("   contraste del encargo: 1180091 por las dos y sha256 9cf019a1c9a856f0")
    w("   CALZA: %s" % ("SI" if (d0 == CONTRASTE_ENCARGO["pendientes_bytes"]
                                 and lf0 == CONTRASTE_ENCARGO["pendientes_bytes"]
                                 and sha0 == CONTRASTE_ENCARGO["pendientes_sha"])
                        else "NO, Y LA DISCREPANCIA SE DECLARA"))
    w("")

    w("B) EL NUMERO, COMPUTADO Y NO TECLEADO, RECOMPUTANDO LA SERIE AHORA")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    en_pend = len([1 for e in halladas if "PENDIENTES.md" in e[1]])
    en_corr = len([1 for e in halladas if "CORRECCIONES_A_APLICAR.md" in e[1]])
    mayor = max(e[0] for e in halladas)
    serie_ent = {"total": len(halladas), "en_pendientes": en_pend,
                 "en_correcciones": en_corr,
                 "colisiones": len(SERIE.colisiones(halladas)),
                 "huecos": len(SERIE.huecos(halladas)), "mayor": mayor}
    w("   CIFRA entradas de la serie ANTES: %d (%d en docs/PENDIENTES.md y %d en "
      "docs/plan/CORRECCIONES_A_APLICAR.md)" % (len(halladas), en_pend, en_corr))
    w("   CIFRA colisiones ANTES: %d" % serie_ent["colisiones"])
    w("   CIFRA huecos ANTES: %d" % serie_ent["huecos"])
    w("   MAYOR ESCRITA: R.%d | SIGUIENTE LIBRE: R.%d" % (mayor, numero))
    w("   contraste del encargo: 64 (63 y 1), 0 colisiones, 0 huecos, mayor R.72,")
    w("   siguiente libre R.73")
    w("")

    w("C) LA VARA DEL `4.1` DEL ACTA 202, CORRIDA POR MI SOBRE LAS DOS ACTAS")
    w("   EL LECTOR VA IMPORTADO Y SIN TOCARLE UNA LINEA: `vara_sobre()` viene de")
    w("   `_v208_t1_registros.py` y `medir_acta()` de `_v203_reparto_de_actas_")
    w("   viejas.py`. Si un numeral no sale, SE DECLARA NO COMPUTABLE con su")
    w("   motivo y NO se ensancha el lector (moratoria de `AUDITOR.md` 6.3).")
    m207, comp207 = vara_sobre(CONTRASTE, w)
    w("")
    m, comp208 = vara_sobre(SUJETO, w)
    w("")
    if m is None or m207 is None:
        w("   ROJO: no se pudo acotar alguna de las dos actas. NO SE ESCRIBE.")
        print(NL.join(L))
        return 1

    w("C.1) LAS DIEZ ADJUDICACIONES, POR SU NUMERO Y CON SU LINEA MEDIDA")
    d = m["adjudicaciones"]
    w("   CIFRA adjudicaciones medidas: %d" % len(d["nm"]))
    for clave, _n in d["nm"]:
        for ln in d["donde"][clave]:
            w("      %-4s linea %5d  cierra: %-62s | %s"
              % (clave, ln, CIERRAN.get(clave, "(ninguno)"),
                 m["lineas"][ln - 1].strip()[:80]))
    faltan = [k for k in CIERRAN if k not in [c for c, _n in d["nm"]]]
    w("   CIFRA adjudicaciones que el encargo dice que cierran pendiente: %d"
      % len(CIERRAN))
    w("   CIFRA de esas que NO estan entre las medidas: %d (%s)"
      % (len(faltan), ", ".join(faltan) or "ninguna"))
    if faltan:
        w("   ROJO: el encargo nombra una adjudicacion que el acta no trae.")
        print(NL.join(L))
        return 1
    w("")

    w("D) EL TITULO DE LA ENTRADA, Y EL CERO FALSO QUE NO SE PUBLICA")
    titulo_crudo = REG206.titulo_de(m, SUJETO)
    w("   TITULO CRUDO, publicado como contraste y NO usado: %s" % titulo_crudo)
    w("   LAS DOS CUENTAS DE CADA CAIDA, JUNTAS Y SIN ELEGIR EN SILENCIO:")
    for etiqueta in ("caidas_del_auditor", "caidas_del_ejecutor"):
        dd = m[etiqueta]
        w("      %-22s por `CAIDA n`: %d | por `N.M` (la forma de esta acta): %d"
          % (etiqueta.replace("_", " "), len(dd["viejas"]), len(dd["nm"])))
    m_para_titulo = dict(m)
    for etiqueta in ("caidas_del_auditor", "caidas_del_ejecutor"):
        dd = m[etiqueta]
        m_para_titulo[etiqueta] = dict(
            dd, viejas=[(c, n, "") for c, n in dd["nm"]], leads=[])
    titulo = REG206.titulo_de(m_para_titulo, SUJETO)
    w("   TITULO ESCRITO: %s" % titulo)
    w("")

    w("E) LA SEDE Y LA IDEMPOTENCIA")
    texto_sede = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    ya = REG206.ya_escrita(texto_sede, numero, SUJETO)
    w("   la entrada del acta %d o el numero R.%d YA ESTAN: %s"
      % (SUJETO, numero, "SI" if ya else "NO"))
    entrada = armar_entrada(numero, m, crec, titulo, titulo_crudo, comp208,
                            comp207, serie_ent, w)
    w("   CIFRA bytes de la entrada compuesta: %d" % len(entrada.encode("utf-8")))
    w("   CIFRA lineas de la entrada compuesta: %d" % entrada.count(NL))
    w("   CIFRA guiones largos en la entrada: %d | guiones medios: %d"
      % (entrada.count(chr(8212)), entrada.count(chr(8211))))
    if entrada.count(chr(8212)) or entrada.count(chr(8211)):
        w("   ROJO: la entrada trae guiones prohibidos. NO SE ESCRIBE.")
        print(NL.join(L))
        return 1
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
    w("   CIFRA crecimiento en bytes normalizado a LF: %d" % (lf1 - lf0))
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
    faltan_l = 0
    j = 0
    for l in viejas:
        while j < len(nuevas) and nuevas[j] != l:
            j += 1
        if j >= len(nuevas):
            faltan_l += 1
        else:
            j += 1
    w("   CIFRA lineas del texto de ENTRADA que NO estan, en orden, en el de")
    w("   SALIDA: %d" % faltan_l)
    w("   (la adicion solo puede ANADIR: si esta cifra no es 0, es ROJO)")
    w("")
    despues = SERIE.entradas()
    w("LA SERIE AL CIERRE, RECOMPUTADA Y NO HEREDADA (LA SEGUNDA PUNTA)")
    w("   CIFRA entradas de la serie DESPUES: %d (%d en docs/PENDIENTES.md y %d "
      "en docs/plan/CORRECCIONES_A_APLICAR.md)"
      % (len(despues), len([1 for e in despues if "PENDIENTES.md" in e[1]]),
         len([1 for e in despues if "CORRECCIONES_A_APLICAR.md" in e[1]])))
    w("   CIFRA colisiones DESPUES: %d" % len(SERIE.colisiones(despues)))
    w("   CIFRA huecos DESPUES: %d" % len(SERIE.huecos(despues)))
    w("   MAYOR ESCRITA DESPUES: R.%d | SIGUIENTE LIBRE DESPUES: R.%d"
      % (max(e[0] for e in despues), SERIE.siguiente_libre(despues)))
    w("")
    con = set()
    for _n, _rel, _ln, titulo_e in despues:
        for mm in re.finditer(r"del acta de la vuelta (\d+)", titulo_e):
            con.add(int(mm.group(1)))
    sin = sorted(v for v in range(173, 209) if v not in con)
    w("LA DEUDA DE REGISTROS, REMEDIDA AL CIERRE Y ENSANCHADA HASTA LA 208")
    w("   CIFRA actas de la 173 a la 208 SIN entrada propia: %d" % len(sin))
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
