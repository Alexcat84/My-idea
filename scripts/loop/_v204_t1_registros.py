# -*- coding: utf-8 -*-
r"""_v204_t1_registros.py . TAREA 1 DE LA VUELTA 204: `R.67` PARA EL ACTA 177 Y
`R.68` PARA EL ACTA 178, LAS DOS SIGUIENTES DE LA DEUDA.

POR EL `4.9` DEL ACTA 201: la deuda son las **177 a 180**, DOS POR VUELTA, de la
mas vieja a la mas nueva. Va PRIMERA porque `AUDITOR.md` 1.4 pone los registros
en la TAREA 1. **LA DEUDA SE REMIDE AQUI Y NO SE COPIA DEL ENCARGO**: al cierre
se recuenta cuantas actas de la 173 a la 180 siguen sin entrada propia.

CLON DECLARADO de `scripts/loop/_v203_t4_registros.py`, generado de el
programaticamente con `scripts/loop/_gen_v204_t1_registros.py`, que imprime
cuantas lineas vienen SIN TOCAR y cuantas son nuevas, contadas con `difflib` y
no a ojo.

EL COMPUTO NO SE ESCRIBE POR TERCERA VEZ Y TAMPOCO SE CLONA: se **IMPORTA** de
`scripts/loop/_v203_reparto_de_actas_viejas.py`, que es el que la 203 escribio
para sus TAREAS 1 y 4. El encargo lo manda con estas palabras: *reutiliza el
computo de la 203, importalo o clonalo con su cifra de difflib al lado, pero no
escribas un tercero*. **Aqui se toma la puerta que no fabrica fichero.**

DE QUE CONVENCION SON LAS DOS ACTAS SE COMPRUEBA Y NO SE SUPONE: la 184 es la
frontera, y este computo publica **LAS DOS LECTURAS JUNTAS** sobre cada acta,
la del lector heredado (que exige comillas inversas) y la de la vara ancha del
`4.1` del acta 202. **Si el heredado no da cero, el acta ya escribe sus claves
con comillas inversas y el lector heredado basta: se dice.**

EL NUMERO NO SE TECLEA: lo computa `serie_de_registros.siguiente_libre()`
recomputando la serie de sus DOS sedes, y el segundo se computa DESPUES de
escribirse el primero, que es la unica forma de que no se teclee.

USO:
  python scripts/loop/_v204_t1_registros.py
  python scripts/loop/_v204_t1_registros.py --escribir
  python scripts/loop/_v204_t1_registros.py --escribir --salida NOMBRE
"""
import argparse
import hashlib
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
import vuelta192_tarea1a_registrar_acta192 as R92           # noqa: E402

SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
VUELTA_QUE_ESCRIBE = 204
CORTE = "7 sep 2026"
SUJETOS = [177, 178]


def dos_convenciones(ruta):
    d = io.open(ruta, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return len(d), len(lf), hashlib.sha256(lf).hexdigest()[:16], lf.decode("utf-8")


def ya_escrita(texto_sede, numero, vuelta):
    """LA GUARDA DE IDEMPOTENCIA, HEREDADA DE LA CORRECCION DE LA VUELTA 200 Y NO
    REINVENTADA. PURA: recibe el texto de la sede.

    LA CAIDA QUE LA OBLIGO, ESCRITA Y NO BORRADA: la version anterior MIRABA EL
    NUMERO Y NO EL SUJETO, y como `siguiente_libre()` avanza en cuanto la entrada
    se escribe, al re-correr el registrador escribio UNA SEGUNDA ENTRADA DEL
    MISMO ACTA. LA VARA CORRECTA ES EL SUJETO: una entrada por acta. El numero se
    sigue mirando ademas, porque una colision de numero tambien es motivo para no
    escribir."""
    por_numero = re.search(r"^##\s+R\.%d\." % numero, texto_sede, re.M) is not None
    por_sujeto = re.search(
        r"^##\s+R\.\d+\..*del acta de la vuelta %d\b" % vuelta,
        texto_sede, re.M) is not None
    return por_numero or por_sujeto


def numeral(dato, cual):
    """LA CIFRA DE UN NUMERAL, O None SI ESE NUMERAL NO ES COMPUTABLE SOBRE ESTA
    ACTA. PURA. Un None NO se convierte en cero: quien llama lo DECLARA.

    LA REGLA DE LAS CAIDAS, ESCRITA AQUI Y NO EN LA CABEZA DE NADIE, Y NACIDA DE
    UNA MEDICION DE ESTA MISMA VUELTA: la forma `CAIDA n` NO ve la forma que el
    acta 176 usa para su caida del ejecutor, que es ``**CAIDA DE REPORTE 1:``.
    Publicar el 0 de `CAIDA n` sobre una seccion que el acta TITULA `LA CAIDA DEL
    EJECUTOR, CON SU NOMBRE` seria publicar un cero falso, que es exactamente lo
    que la vuelta 201 rechazo en su entrada de la 198.

    POR ESO: el numeral de caidas es la cifra de `CAIDA n` **solo si ningun lead
    en negrita se le escapa**. Si hay leads que esa forma no ve, el numeral se
    declara NO COMPUTABLE POR UNA SOLA FORMA y la entrada publica LAS TRES
    lecturas. Eso es MEDIR y decir lo que cada forma da, no DECIDIR cual gana."""
    if dato is None:
        return None
    if cual == "nm":
        return len(dato["nm"])
    if cual == "leads":
        return len(dato["leads"])
    if cual == "viejas":
        vistas = set(ln for _c, ln, _t in dato["viejas"])
        escapados = [x for x in dato["leads"] if x[1] not in vistas]
        if escapados:
            return None
        return len(dato["viejas"])
    return None


def titulo_de(m, vuelta):
    """EL TITULO DE LA ENTRADA. NO SE USA EL HEREDADO, y el motivo va MEDIDO en
    la salida: `R92.titulo_de_la_entrada()` publica los CINCO numerales como
    cifras, y sobre estas actas DOS de los cinco NO SON COMPUTABLES porque
    ninguna seccion los titula. Un titulo que dijera 'los cero hallazgos' se
    leeria como que el acta no hallo nada, y es falso. Es el mismo precedente que
    la 201 sento en su entrada de la 198 y la 202 en las suyas."""
    adj = numeral(m.get("adjudicaciones"), "nm")
    hal = numeral(m.get("hallazgos"), "nm")
    preg = len(m["preguntas"])
    cau = numeral(m.get("caidas_del_auditor"), "viejas")
    cej = numeral(m.get("caidas_del_ejecutor"), "viejas")
    def trozo(n, sing, plur):
        if n is None:
            return "las %s NO COMPUTABLES" % plur
        if n == 1:
            return "la 1 %s" % sing
        return "las %d %s" % (n, plur)

    def trozo_m(n, sing, plur):
        if n is None:
            return "los %s NO COMPUTABLES" % plur
        if n == 1:
            return "el 1 %s" % sing
        return "los %d %s" % (n, plur)

    piezas = [trozo(adj, "adjudicacion numerada", "adjudicaciones numeradas"),
              trozo_m(hal, "hallazgo", "hallazgos"),
              trozo(preg, "pregunta contestada", "preguntas contestadas"),
              trozo(cau, "caida propia del auditor", "caidas propias del auditor"),
              trozo(cej, "caida del ejecutor", "caidas del ejecutor")]
    return ("Registro de %s del acta de la vuelta %d, computados con LA VARA DEL "
            "`4.1` DEL ACTA 202" % (", ".join(piezas), vuelta))


def armar_entrada(numero, vuelta, m, w):
    lineas = m["lineas"]
    adj = m.get("adjudicaciones")
    hal = m.get("hallazgos")
    cau = m.get("caidas_del_auditor")
    cej = m.get("caidas_del_ejecutor")
    p = []
    a = p.append
    a("## R.%d. %s" % (numero, titulo_de(m, vuelta)))
    a("")
    a("(Acta del auditor, vuelta %d; escrito en la vuelta %d, TAREA 1.)"
      % (vuelta, VUELTA_QUE_ESCRIBE))
    a("")
    a("Por adicion, como `R.21` a `R.66`. **Corte de todas las cifras de esta")
    a("entrada: %s.** El numero de esta entrada NO esta tecleado: lo computa" % CORTE)
    a("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    a("Salida: `docs/loop/SALIDA_V%d_T1_REGISTROS.txt`." % VUELTA_QUE_ESCRIBE)
    a("")
    a("**ESTA ENTRADA DECLARA QUE USO LA VARA DEL `4.1` DEL ACTA 202**, que es")
    a("obligatoria para toda acta ANTERIOR a la 184: *el numeral se toma de la")
    a("seccion cuyo PROPIO TITULO lo nombra, NUNCA del numero de seccion, y dentro")
    a("de ella las claves se cuentan por su propia numeracion `N.M`, lleve o no")
    a("comillas inversas*. **Y donde ninguna seccion titula un numeral, la entrada")
    a("DECLARA que no es computable en vez de publicar un cero**, que se leeria")
    a("como que el acta no hizo esa cosa. Es el mismo precedente que la vuelta 201")
    a("sento en su entrada de la 198.")
    a("")
    a("**NINGUN LECTOR NUEVO PERMANENTE SE ESCRIBIO PARA ESTA ENTRADA.** Rige la")
    a("MORATORIA DE MAQUINARIA (`AUDITOR.md` 6.3). Los lectores se IMPORTAN y lo")
    a("unico que se ensancho es **el patron de clave**, con un parametro")
    a("`plantilla` OPCIONAL en `R84.claves_entrecomilladas()` cuyo valor por")
    a("defecto es la expresion que ya tenia dentro, **para que ninguno de sus")
    a("catorce llamantes se toque**. El computo vive en")
    a("`scripts/loop/_v203_reparto_de_actas_viejas.py`, con prefijo de guion bajo,")
    a("**fuera del censo y fuera de la nomina**, y **es el MISMO que uso la")
    a("TAREA 1 y la TAREA 4 de la vuelta 203**, y aqui se IMPORTA tal cual:")
    a("no se escribio un tercero y tampoco se clono.")
    a("")
    a("**EL ACTA ACOTADA EN ESTA VUELTA:** lineas **%d** a **%d**, **%d** lineas,"
      % (m["ini"], m["fin"], m["fin"] - m["ini"] + 1))
    a("sobre un fichero de **%d** bytes en disco y **%d** normalizado a LF. Su"
      % (m["bytes_disco"], m["bytes_lf"]))
    a("cuerpo trae **%d** secciones `## N. TITULO`, y aqui van las que este"
      % len(m["secs"]))
    a("computo mira, cada una con **su numero y su titulo literal**:")
    a("")
    a("| numeral | seccion que lo titula, por su TITULO | numero | linea | claves | cuantas |")
    a("|---|---|---:|---:|---|---:|")
    for nombre, dato, forma in (("adjudicaciones", adj, "nm"),
                                ("hallazgos", hal, "nm"),
                                ("caidas propias del auditor", cau, "viejas"),
                                ("caidas del ejecutor", cej, "viejas")):
        if dato is None:
            a("| %s | **NINGUNA SECCION DE ESTA ACTA TITULA ESTE NUMERAL** | (no "
              "aplica) | (no aplica) | (no aplica) | **no computable** |" % nombre)
            continue
        sec = dato["sec"]
        if forma == "nm":
            claves = ", ".join("`%s`" % c for c, _n in dato["nm"]) or "(ninguna)"
            cuantas = len(dato["nm"])
        else:
            claves = ", ".join("`%s`" % c for c, _l, _t in dato["viejas"]) or "(ninguna)"
            cuantas = len(dato["viejas"])
        a("| %s | %s | %d | %d | %s | **%d** |"
          % (nombre, sec[2].replace("|", "/"), sec[0], sec[1], claves, cuantas))
    a("| preguntas contestadas | (no es una seccion: son las `P.n` que los titulos "
      "de las adjudicaciones nombran) | (no aplica) | (no aplica) | %s | **%d** |"
      % (", ".join("`%s`" % x for x in m["preguntas"]) or "(ninguna)",
         len(m["preguntas"])))
    a("")
    a("**LA VIA DEL NUMERAL DE PREGUNTAS, DICHA Y NO SUPUESTA:** %s."
      % m["via_preguntas"])
    a("`%s` **%s**, y su seccion de preguntas se lee asi: %s."
      % (m["ruta_rep"], "existe" if m["existe_rep"] else "NO EXISTE",
         m["seccion_preg"]))
    if m["existe_rep"]:
        a("Ese fichero mide **%d** bytes, medidos en esta vuelta con"
          % m["bytes_rep"])
        a("`os.path.isfile` y `os.path.getsize`.")
    else:
        a("**NO SE FABRICA Y NO SE RECONSTRUYE:** medido con `os.path.isfile` y")
        a("`os.path.getsize` en esta vuelta, **no hay fichero que medir**, y el cero")
        a("no sale de contar uno vacio. Se usa **la vara del `4.7` del acta 201**, y")
        a("**esta entrada lo declara**.")
    a("Claves `P.n` nombradas: **%d** (%s). Claves que quedan fuera del numeral:"
      % (len(m["nombradas"]),
         ", ".join("`%s`" % x for x in m["nombradas"]) or "ninguna"))
    a("**%d** (%s)."
      % (len(m["fuera"]),
         ", ".join("`%s`" % x for x in m["fuera"]) or "ninguna"))
    a("")
    a("### LAS DOS LECTURAS, PUBLICADAS JUNTAS Y CON LA DISCREPANCIA DECLARADA")
    a("")
    a("| lectura | adjudicaciones | hallazgos |")
    a("|---|---:|---:|")
    a("| **el lector heredado tal cual**, `R84.claves_entrecomilladas()` con su "
      "plantilla de siempre | %s | %s |"
      % (len(adj["heredado"]) if adj else "(sin seccion)",
         len(hal["heredado"]) if hal else "(sin seccion)"))
    a("| **la vara adjudicada en el `4.1`**, mismo lector con la plantilla ancha "
      "| **%s** | **%s** |"
      % (len(adj["nm"]) if adj else "(sin seccion)",
         len(hal["nm"]) if hal else "(sin seccion)"))
    a("")
    a("**LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO** (`EJECUTOR.md` 2).")
    a("El cero del heredado **es cierto**: esa plantilla exige comillas inversas y")
    a("esta acta no las escribe. Las dos cifras quedan escritas.")
    a("")
    a("### LAS CAIDAS, CON SUS TRES LECTURAS Y SU FORMA DECLARADA")
    a("")
    a("**LA FORMA DE CLAVE DE LAS CAIDAS DE ESTA ACTA NO ES `N.M`**, y por eso se")
    a("publican **las tres lecturas** en vez de elegir una en silencio: la de la")
    a("vara (`N.M`), la de la forma vieja (``**`CAIDA n`.``) y la de los")
    a("encabezados en negrita que abren con `CAIDA` o `AMAGO`, que es la unica que")
    a("ve la forma que el acta 176 usa (``**CAIDA DE REPORTE 1:``).")
    a("")
    a("| seccion | por la vara `N.M` | por `CAIDA n` | por lead en negrita |")
    a("|---|---:|---:|---:|")
    for nombre, dato in (("caidas propias del auditor", cau),
                         ("caidas del ejecutor", cej)):
        if dato is None:
            a("| %s | (ninguna seccion la titula) | (ninguna seccion la titula) | "
              "(ninguna seccion la titula) |" % nombre)
            continue
        a("| %s (seccion %d, linea %d) | %d | **%d** | %d |"
          % (nombre, dato["sec"][0], dato["sec"][1], len(dato["nm"]),
             len(dato["viejas"]), len(dato["leads"])))
    a("")
    for nombre, dato in (("AUDITOR", cau), ("EJECUTOR", cej)):
        if dato is None:
            a("- **%s:** ninguna seccion de esta acta titula ese numeral, **y eso"
              % nombre)
            a("  se declara, no se publica como un cero**.")
            continue
        if not dato["leads"]:
            a("- **%s:** la seccion existe y **no trae ningun encabezado de caida**"
              % nombre)
            a("  por ninguna de las tres formas.")
        for clave, ln, texto in dato["leads"]:
            a("- **%s, lead `%s`** (linea %d): %s"
              % (nombre, clave, ln, texto.replace("|", "/")[:190]))
    a("")
    a("### LAS %s ADJUDICACIONES, UNA POR UNA, CON SU LINEA"
      % (len(adj["nm"]) if adj else "CERO"))
    a("")
    if not adj:
        a("- (ninguna seccion de esta acta se titula LAS ADJUDICACIONES)")
    else:
        a("| clave | pregunta que contesta | linea | titulo, literal del acta |")
        a("|---|---|---:|---|")
        for clave, _n in adj["nm"]:
            for ln in adj["donde"][clave]:
                t = lineas[ln - 1].strip()
                preg = re.search(r"`(P\.\d+)`", t)
                a("| `%s` | %s | %d | %s |"
                  % (clave, ("`%s`" % preg.group(1)) if preg else "(ninguna)",
                     ln, t.replace("|", "/").strip("*")[:200]))
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
    fila_caidas = [s for _l, s in m["filas"] if s.startswith("| caidas")]
    a("**EL COTEJO CONTRA LA PROPIA FILA DE METRICA DEL ACTA, QUE LA ESCRIBIO EL")
    a("AUDITOR DE AQUELLA VUELTA Y NO ESTA VUELTA:** esa fila publica")
    a("%s caidas propias del auditor, y este computo, por la forma `CAIDA n`,"
      % (("`%s`" % fila_caidas[0].split("|")[2].strip()) if fila_caidas
         else "(ninguna fila de caidas)"))
    a("cuenta **%s**." % (len(cau["viejas"]) if cau else "(sin seccion)"))
    a("")
    a("**EL CONTRASTE HEREDADO DEL REPARTO POR NEGRITA, TAMBIEN AL LADO:**")
    a("`R92.caidas_por_lead_heredado()` da **%d** del ejecutor, **%d** del auditor"
      % (len(m["eje_h"]), len(m["aud_h"])))
    a("y **%d** huerfanas sobre este mismo cuerpo." % len(m["hue_h"]))
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
    w("VUELTA %d, TAREA 1: R.67 PARA EL ACTA 177 Y R.68 PARA EL ACTA 178,"
      % VUELTA_QUE_ESCRIBE)
    w("LAS DOS SIGUIENTES DE LA DEUDA DEL 4.9 DEL ACTA 201, REMEDIDA AQUI")
    w("=" * 78)
    w("")
    w("0) LA PRUEBA POR MUTACION DEL ENSANCHE, OTRA VEZ Y ANTES DE ESCRIBIR NADA.")
    w("   Es la MISMA del computo de la 203, porque es el MISMO fichero IMPORTADO:")
    w("   vuelve a correr aqui en vez de heredar su verde de otra corrida.")
    ok = REP.prueba_por_mutacion(w)
    w("   VEREDICTO DE LA PRUEBA: %s" % ("VERDE" if ok else "ROJO"))
    w("")
    if not ok:
        w("   ROJO: la prueba por mutacion no salio verde. NO SE ESCRIBE NADA.")
        print(NL.join(L))
        return 1

    d0, lf0, sha0, texto0 = dos_convenciones(SEDE)
    w("A) LA SEDE AL ENTRAR, POR LAS DOS CONVENCIONES")
    w("   docs/PENDIENTES.md: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (d0, lf0, sha0))
    w("   CIFRA lineas por split(NL): %d" % len(texto0.split(NL)))
    w("")

    escritas = []
    for etiqueta, vuelta in zip(("1.a", "1.b"), SUJETOS):
        w("=" * 78)
        w("TAREA %s . EL SUJETO ES EL ACTA DE LA VUELTA %d" % (etiqueta, vuelta))
        w("=" * 78)
        w("")
        w("B) EL NUMERO, COMPUTADO Y NO TECLEADO, RECOMPUTANDO LA SERIE AHORA")
        halladas = SERIE.entradas()
        numero = SERIE.siguiente_libre(halladas)
        w("   CIFRA entradas de la serie ANTES: %d" % len(halladas))
        w("   CIFRA colisiones ANTES: %d" % len(SERIE.colisiones(halladas)))
        w("   CIFRA huecos ANTES: %d" % len(SERIE.huecos(halladas)))
        w("   SIGUIENTE LIBRE: R.%d" % numero)
        w("")

        w("C) EL CUERPO DEL ACTA Y SUS NUMERALES, MEDIDOS EN ESTA VUELTA")
        m = REP.medir_acta(vuelta, w)
        w("")
        if m is None:
            w("   ROJO: no se pudo acotar el acta %d. NO SE ESCRIBE." % vuelta)
            continue

        w("D) EL TITULO. EL HEREDADO SE COMPUTA Y SE PUBLICA COMO CONTRASTE,")
        w("   PERO NO SE USA, Y EL MOTIVO VA MEDIDO Y NO AFIRMADO.")
        adj = numeral(m.get("adjudicaciones"), "nm")
        hal = numeral(m.get("hallazgos"), "nm")
        cau = numeral(m.get("caidas_del_auditor"), "viejas")
        cej = numeral(m.get("caidas_del_ejecutor"), "viejas")
        no_comp = [n for n, v in (("hallazgos", hal),
                                  ("caidas del auditor", cau),
                                  ("caidas del ejecutor", cej),
                                  ("adjudicaciones", adj)) if v is None]
        w("   CIFRA numerales NO COMPUTABLES sobre esta acta: %d | cuales: %s"
          % (len(no_comp), ", ".join(no_comp) or "(ninguno)"))
        crudo = R92.titulo_de_la_entrada(adj or 0, hal or 0, len(m["preguntas"]),
                                         cau or 0, cej or 0)
        w("   TITULO HEREDADO, PUBLICADO COMO CONTRASTE Y NO USADO:")
        w("      %s" % crudo)
        w("   POR QUE NO SE USA: publica los CINCO numerales como cifras, y sobre")
        w("   esta acta %d de los cinco NO SON COMPUTABLES. Un titulo que dijera"
          % len(no_comp))
        w("   'los cero hallazgos' se leeria como que el acta no hallo nada, y es")
        w("   falso. Mismo precedente que la 201 en su entrada de la 198.")
        titulo = titulo_de(m, vuelta)
        w("   TITULO ESCRITO: %s" % titulo)
        w("")

        w("E) LA SEDE Y LA IDEMPOTENCIA")
        texto_sede = io.open(SEDE, encoding="utf-8").read().replace(
            chr(13) + NL, NL)
        ya = ya_escrita(texto_sede, numero, vuelta)
        w("   la entrada del acta %d o el numero R.%d YA ESTAN: %s"
          % (vuelta, numero, "SI" if ya else "NO"))
        entrada = armar_entrada(numero, vuelta, m, w)
        w("   CIFRA bytes de la entrada compuesta: %d"
          % len(entrada.encode("utf-8")))
        w("   CIFRA lineas de la entrada compuesta: %d" % (entrada.count(NL)))
        if a.escribir and not ya:
            nuevo = texto_sede
            if not nuevo.endswith(NL):
                nuevo += NL
            nuevo += NL + entrada
            io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
            w("   ESCRITA: R.%d anadida al final de docs/PENDIENTES.md" % numero)
            escritas.append((numero, vuelta))
        elif a.escribir:
            w("   NO SE ESCRIBE: la entrada ya estaba. IDEMPOTENTE.")
        else:
            w("   MODO MEDICION: no se escribe nada.")
        w("")

    w("=" * 78)
    w("EL CIERRE, REMEDIDO Y NO HEREDADO")
    w("=" * 78)
    d1, lf1, sha1, texto1 = dos_convenciones(SEDE)
    w("   docs/PENDIENTES.md al salir: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (d1, lf1, sha1))
    w("   CIFRA crecimiento en bytes de disco: %d" % (d1 - d0))
    w("   CIFRA crecimiento en bytes LF: %d" % (lf1 - lf0))
    w("   CIFRA lineas al salir: %d (al entrar %d, crecimiento %d)"
      % (len(texto1.split(NL)), len(texto0.split(NL)),
         len(texto1.split(NL)) - len(texto0.split(NL))))
    w("   CIFRA entradas escritas por esta corrida: %d" % len(escritas))
    for numero, vuelta in escritas:
        w("      R.%d  ->  acta de la vuelta %d" % (numero, vuelta))
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
    for _n, _rel, _ln, titulo in despues:
        for mm in re.finditer(r"del acta de la vuelta (\d+)", titulo):
            con.add(int(mm.group(1)))
    sin = sorted(v for v in range(173, 181) if v not in con)
    w("LA DEUDA DEL 4.9 DEL ACTA 201, REMEDIDA AL CIERRE")
    w("   CIFRA actas de la 173 a la 180 SIN entrada propia: %d" % len(sin))
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
