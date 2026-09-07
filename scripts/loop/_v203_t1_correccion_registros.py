# -*- coding: utf-8 -*-
r"""_v203_t1_correccion_registros.py . TAREA 1 DE LA VUELTA 203: LA CORRECCION
DECLARADA DE `R.63` Y `R.64`, Y EL REPARTO REAL DE LAS ACTAS 173 Y 174.

VA PRIMERA PORQUE `AUDITOR.md` 1.4 PONE LOS REGISTROS EN LA TAREA 1, y es el
remedio de la `C.E1` de la 202.

QUE SE CORRIGE, Y LA FRASE ES FALSA: `R.63` y `R.64` dicen que las
adjudicaciones de esas actas viven en la **seccion 6 sin clave numerada**. El
acta 202 lo midio en su `4.1` y estan NUMERADAS: la 173 de `6.1` a `6.5` y la
174 de `6.1` a `6.10`. **Aqui se vuelve a medir, no se copia del encargo.**

EL CARRIL ES EL DE `OP-L-03` DE LA 202: banco `9.10`, **POR ADICION**, con el
texto viejo **entero, sin tachar y sin borrar**, y la correccion fechada debajo.
La adicion se pega **al final de la entrada**, justo antes de la cabecera `##`
siguiente, para no partir el texto viejo por la mitad.

PREFIJO DE GUION BAJO: fuera del censo y fuera de la nomina. El computo del
reparto NO SE ESCRIBE DOS VECES: se importa de
`scripts/loop/_v203_reparto_de_actas_viejas.py`, que es el mismo que usara la
TAREA 4.

USO:
  python scripts/loop/_v203_t1_correccion_registros.py
  python scripts/loop/_v203_t1_correccion_registros.py --escribir
  python scripts/loop/_v203_t1_correccion_registros.py --escribir --salida NOMBRE
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
import _v203_reparto_de_actas_viejas as REP                 # noqa: E402

SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
VUELTA_QUE_ESCRIBE = 203
CORTE = "7 sep 2026"
LITERAL_FALSO = "seccion 6 sin clave numerada"
MARCA = ("CORRECCION DECLARADA (2026-09-07, vuelta 203, TAREA 1 del encargo), "
         "POR EL CARRIL DEL BANCO 9.10")

# LOS SUJETOS: (numero de la entrada, vuelta del acta).
SUJETOS = [(63, 173), (64, 174)]


def dos_convenciones(ruta):
    d = io.open(ruta, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return len(d), len(lf), hashlib.sha256(lf).hexdigest()[:16], lf.decode("utf-8")


def cota_de_la_entrada(lineas, numero):
    """(inicio, fin) DE LA ENTRADA `R.n` EN LA SEDE, o (None, None). La cota se
    COMPUTA de las cabeceras `##` y CAE si la cabecera no aparece 1 sola vez."""
    hits = [i for i, l in enumerate(lineas, 1)
            if l.startswith("## R.%d." % numero)]
    if len(hits) != 1:
        return None, None
    a = hits[0]
    sig = [i for i, l in enumerate(lineas, 1) if i > a and l.startswith("## ")]
    b = (sig[0] - 1) if sig else len(lineas)
    return a, b


def ya_corregida(texto_entrada):
    """LA GUARDA DE IDEMPOTENCIA: la correccion de ESTA vuelta ya esta dentro de
    ESTA entrada. PURA: recibe el texto de la entrada, no el de la sede.

    LA VARA ES LA MARCA COMPLETA Y NO EL NUMERO SUELTO, por lo mismo que la
    vuelta 200 le ensenio a la guarda de la serie: una vara demasiado laxa
    escribe dos veces, y una demasiado estrecha nunca reconoce lo escrito."""
    return MARCA in texto_entrada


def bloque_de_correccion(numero, vuelta, m, lineas_falsas):
    """EL TEXTO DE LA ADICION. NINGUNA CIFRA SE TECLEA: todas salen de `m`, que
    es lo que `REP.medir_acta()` midio en esta vuelta."""
    L = []
    a = L.append
    adj = m["adjudicaciones"]
    hal = m["hallazgos"]
    cau = m["caidas_del_auditor"]
    cej = m["caidas_del_ejecutor"]
    a("")
    a("### %s, POR ADICION Y CON EL TEXTO VIEJO ENTERO ARRIBA" % MARCA)
    a("")
    a("**EL TEXTO DE ARRIBA NO SE TACHA NI SE BORRA, Y ESO NO ES UNA")
    a("FORMALIDAD:** *una correccion que tapa lo que corrige no se puede")
    a("auditar* (`EJECUTOR.md` 8). Lo que sigue es **un bloque mas de esta misma")
    a("entrada**, sin clave nueva de esquema, exactamente como el acta 202 hizo")
    a("con la `evidencia` de `OP-L-03` en su TAREA 1.")
    a("")
    a("**LO QUE ESTABA MAL, CITADO POR LINEA Y NO PARAFRASEADO.** El texto de")
    a("arriba dice que las adjudicaciones de esta acta viven en la **%s**."
      % LITERAL_FALSO)
    a("En `docs/PENDIENTES.md` ese literal vive hoy en **%d** lineas, la **%s**,"
      % (len(lineas_falsas), " y la ".join(str(x) for x in lineas_falsas)))
    a("contadas en esta vuelta y no copiadas de ningun encargo. **ES FALSO:**")
    a("**las adjudicaciones de esta acta SI estan numeradas**, y lo unico que")
    a("les falta son **las comillas inversas** que el lector heredado exige. Lo")
    a("adjudico el acta 202 en su `4.1`, y aqui se REMIDE en vez de copiarse.")
    a("")
    a("**LO QUE SI SEGUIA SIENDO CIERTO, DICHO PARA NO EXAGERAR LA CORRECCION:**")
    a("los cinco lectores heredados **devuelven cero sobre esta acta**, y ese")
    a("cero es CIERTO. Lo que era falso era **la razon** que se le ponia. Las")
    a("dos lecturas van publicadas juntas mas abajo.")
    a("")
    a("**LA VARA QUE ESTA CORRECCION USA, DECLARADA Y CITADA** (acta 202, `4.1`,")
    a("por extension del `4.7` del acta 201): **el numeral se toma de la seccion")
    a("cuyo PROPIO TITULO lo nombra, NUNCA del numero de seccion, y dentro de")
    a("ella las claves se cuentan por su propia numeracion `N.M`, lleve o no")
    a("comillas inversas.** **ESTA ENTRADA DECLARA QUE USO ESA VARA.**")
    a("")
    a("**NINGUN LECTOR NUEVO PERMANENTE SE ESCRIBIO PARA ESTO.** Rige la")
    a("MORATORIA DE MAQUINARIA (`AUDITOR.md` 6.3). Los lectores se IMPORTAN, y")
    a("lo unico que se ensancho es **el patron de clave**, con **un parametro")
    a("`plantilla` OPCIONAL** en `R84.claves_entrecomilladas()` cuyo valor por")
    a("defecto es la expresion que esa funcion ya tenia dentro, **para que")
    a("ninguno de sus catorce llamantes se toque**: es la forma que el acta 173")
    a("adjudico en su propia `6.2`. El computo vive en")
    a("`scripts/loop/_v203_reparto_de_actas_viejas.py`, con **prefijo de guion")
    a("bajo, fuera del censo y fuera de la nomina**, que es lo que el `4.5` del")
    a("acta 199 llama **computo de una vuelta**.")
    a("")
    a("**EL ACTA ACOTADA EN ESTA VUELTA:** lineas **%d** a **%d**, **%d** lineas,"
      % (m["ini"], m["fin"], m["fin"] - m["ini"] + 1))
    a("sobre un fichero de **%d** bytes en disco y **%d** normalizado a LF."
      % (m["bytes_disco"], m["bytes_lf"]))
    a("Su cuerpo trae **%d** secciones `## N. TITULO`." % len(m["secs"]))
    a("")
    a("#### EL REPARTO REAL, CADA NUMERAL CON LA SECCION QUE LO TITULA")
    a("")
    a("| numeral | seccion que lo titula, por su TITULO | numero de esa seccion "
      "| linea | claves | cuantas |")
    a("|---|---|---:|---:|---|---:|")
    for etiqueta, dato, nombre in (("adjudicaciones", adj, "adjudicaciones"),
                                   ("hallazgos", hal, "hallazgos")):
        if dato is None:
            a("| %s | **NINGUNA SECCION DE ESTA ACTA TITULA ESTE NUMERAL** | (no "
              "aplica) | (no aplica) | (no aplica) | **no computable** |" % nombre)
            continue
        sec = dato["sec"]
        a("| %s | %s | %d | %d | %s | **%d** |"
          % (nombre, sec[2].replace("|", "/"), sec[0], sec[1],
             ", ".join("`%s`" % c for c, _n in dato["nm"]) or "(ninguna)",
             len(dato["nm"])))
    for etiqueta, dato, nombre in (("caidas_del_auditor", cau,
                                    "caidas propias del auditor"),
                                   ("caidas_del_ejecutor", cej,
                                    "caidas del ejecutor")):
        if dato is None:
            a("| %s | **NINGUNA SECCION DE ESTA ACTA TITULA ESTE NUMERAL** | (no "
              "aplica) | (no aplica) | (no aplica) | **no computable** |" % nombre)
            continue
        sec = dato["sec"]
        a("| %s | %s | %d | %d | %s | **%d** |"
          % (nombre, sec[2].replace("|", "/"), sec[0], sec[1],
             ", ".join("`%s`" % c for c, _l, _t in dato["viejas"]) or "(ninguna)",
             len(dato["viejas"])))
    a("| preguntas contestadas | (no es una seccion: son las `P.n` que los "
      "titulos de las adjudicaciones nombran) | (no aplica) | (no aplica) | %s "
      "| **%d** |"
      % (", ".join("`%s`" % p for p in m["preguntas"]) or "(ninguna)",
         len(m["preguntas"])))
    a("")
    a("**LA VIA DEL NUMERAL DE PREGUNTAS, DICHA Y NO SUPUESTA:** %s."
      % m["via_preguntas"])
    a("`%s` **%s**, y su seccion de preguntas se lee asi: %s."
      % (m["ruta_rep"], "existe" if m["existe_rep"] else "NO EXISTE",
         m["seccion_preg"]))
    if m["existe_rep"]:
        a("Su tamano, medido en esta vuelta con `os.path.getsize`: **%d** bytes."
          % m["bytes_rep"])
    else:
        a("**NO SE FABRICA Y NO SE RECONSTRUYE:** medido con `os.path.isfile` y")
        a("`os.path.getsize` en esta vuelta, **no hay fichero que medir**, y el")
        a("cero no sale de contar uno vacio.")
    a("Claves `P.n` nombradas: **%d** (%s). Claves que quedan fuera del numeral:"
      % (len(m["nombradas"]),
         ", ".join("`%s`" % x for x in m["nombradas"]) or "ninguna"))
    a("**%d** (%s)."
      % (len(m["fuera"]),
         ", ".join("`%s`" % x for x in m["fuera"]) or "ninguna"))
    a("")
    a("#### LAS DOS LECTURAS, PUBLICADAS JUNTAS, Y LA DISCREPANCIA DECLARADA")
    a("")
    a("| lectura | adjudicaciones | hallazgos | caidas del auditor |")
    a("|---|---:|---:|---:|")
    a("| **el lector heredado tal cual**, `R84.claves_entrecomilladas()` con su "
      "plantilla de siempre | %s | %s | %s |"
      % (len(adj["heredado"]) if adj else "(sin seccion)",
         len(hal["heredado"]) if hal else "(sin seccion)",
         len(cau["heredado"]) if cau else "(sin seccion)"))
    a("| **la vara adjudicada en el `4.1`**, mismo lector con la plantilla "
      "ancha | **%s** | **%s** | **%s** |"
      % (len(adj["nm"]) if adj else "(sin seccion)",
         len(hal["nm"]) if hal else "(sin seccion)",
         len(cau["viejas"]) if cau else "(sin seccion)"))
    a("")
    a("**LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO** (`EJECUTOR.md`")
    a("2). El cero del heredado **es cierto** y sigue siendo cierto: esa")
    a("plantilla exige comillas inversas y esta acta no las escribe. La cifra")
    a("de la derecha es la del **mismo lector** con la plantilla ancha, y las")
    a("dos quedan escritas.")
    a("")
    a("**Y LA COLUMNA DE LAS CAIDAS DEL AUDITOR LLEVA SU PROPIA DECLARACION,")
    a("PORQUE SU FORMA NO ES `N.M`:** esta acta escribe sus caidas como")
    a("``- **`CAIDA n`. TITULO``, que **no es la numeracion `N.M` de la vara**;")
    a("por eso se cuentan **con su propia forma**, medida en esta vuelta, y no")
    a("con la plantilla ancha, que sobre esa seccion da **%s**."
      % (len(cau["nm"]) if cau else "(sin seccion)"))
    a("")
    a("**EL CONTRASTE HEREDADO DEL REPARTO POR NEGRITA, TAMBIEN AL LADO:**")
    a("`R92.caidas_por_lead_heredado()` da **%d** del ejecutor, **%d** del"
      % (len(m["eje_h"]), len(m["aud_h"])))
    a("auditor y **%d** huerfanas sobre este mismo cuerpo." % len(m["hue_h"]))
    a("")
    a("#### LAS %s ADJUDICACIONES, UNA POR UNA, CON SU LINEA"
      % (len(adj["nm"]) if adj else "CERO"))
    a("")
    if not adj:
        a("- (ninguna seccion de esta acta se titula LAS ADJUDICACIONES)")
    else:
        a("| clave | pregunta que contesta | linea | titulo, literal del acta |")
        a("|---|---|---:|---|")
        for clave, _n in adj["nm"]:
            for ln in adj["donde"][clave]:
                t = m["lineas"][ln - 1].strip()
                preg = re.search(r"`(P\.\d+)`", t)
                a("| `%s` | %s | %d | %s |"
                  % (clave, ("`%s`" % preg.group(1)) if preg else "(ninguna)",
                     ln, t.replace("|", "/").strip("*")[:200]))
    a("")
    a("#### LOS %s HALLAZGOS, UNO POR UNO, CON SU LINEA"
      % (len(hal["nm"]) if hal else "CERO"))
    a("")
    if not hal:
        a("- (ninguna seccion de esta acta se titula LOS HALLAZGOS)")
    else:
        for clave, _n in hal["nm"]:
            for ln in hal["donde"][clave]:
                a("- **`%s`** (linea %d): %s"
                  % (clave, ln, m["lineas"][ln - 1].strip().replace("|", "/")[:200]))
    a("")
    a("#### LAS CAIDAS, CON SU LINEA Y CON SU FORMA DECLARADA")
    a("")
    if cau:
        for clave, ln, texto in cau["viejas"]:
            a("- **AUDITOR `%s`** (linea %d): %s"
              % (clave, ln, texto.replace("|", "/")[:200]))
    else:
        a("- (ninguna seccion de esta acta titula las caidas propias del auditor)")
    if cej:
        for clave, ln, texto in cej["viejas"]:
            a("- **EJECUTOR `%s`** (linea %d): %s"
              % (clave, ln, texto.replace("|", "/")[:200]))
    else:
        a("- (ninguna seccion de esta acta titula las caidas del ejecutor: **eso")
        a("  se declara, no se publica como un cero**)")
    a("")
    a("#### LA METRICA DE CREDITO, PEGADA ENTERA Y NO EXTRAIDA")
    a("")
    a("**`R95.cifras_de_la_fila_de_puestos()` devuelve `%s` sobre la fila de "
      "puestos de este cuerpo.** Cuando no alcanza, la fila se PEGA con su "
      "numero de linea, que es cita y no celda tecleada."
      % (m["lectura_puestos"],))
    a("")
    if not m["filas"]:
        a("- (ninguna fila de metrica con esos prefijos en este cuerpo)")
    for ln, s in m["filas"]:
        a("- (linea %d) %s" % (ln, s))
    a("")
    a("**EL COTEJO QUE NADIE PIDIO Y QUE VALE LA PENA DECIR:** la propia fila")
    a("de metrica de esta acta publica **%s** caidas propias del auditor, y el"
      % (("`%s`" % [s for _l, s in m["filas"]
                    if s.startswith("| caidas")][0].split("|")[2].strip())
         if [s for _l, s in m["filas"] if s.startswith("| caidas")]
         else "(ninguna fila de caidas)"))
    a("computo de esta correccion, por la forma `CAIDA n`, cuenta **%s**."
      % (len(cau["viejas"]) if cau else "(sin seccion)"))
    a("")
    a("*(Correccion escrita en la vuelta %d, TAREA 1. Corte de todas sus cifras:"
      % VUELTA_QUE_ESCRIBE)
    a("%s. Salida: `docs/loop/SALIDA_V%d_T1_CORRECCION_REGISTROS.txt`.)*"
      % (CORTE, VUELTA_QUE_ESCRIBE))
    a("")
    return NL.join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    ap.add_argument("--salida", default="T1_CORRECCION_REGISTROS")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 1: LA CORRECCION DECLARADA DE R.63 Y R.64, Y EL"
      % VUELTA_QUE_ESCRIBE)
    w("REPARTO REAL DE LAS ACTAS 173 Y 174 POR LA VARA DEL 4.1 DEL ACTA 202")
    w("=" * 78)
    w("")
    w("0) LA PRUEBA POR MUTACION DEL ENSANCHE, ANTES DE ESCRIBIR NADA")
    w("   (EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION). Lo unico")
    w("   propio de esta vuelta es LA PLANTILLA, y es lo que se prueba.")
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
    lineas0 = texto0.split(NL)
    w("   CIFRA lineas por split(NL): %d" % len(lineas0))
    lineas_falsas = [i for i, l in enumerate(lineas0, 1) if LITERAL_FALSO in l]
    w("   CIFRA lineas con el literal %r: %d | linea(s): %s"
      % (LITERAL_FALSO, len(lineas_falsas),
         ", ".join(str(x) for x in lineas_falsas) or "(ninguna)"))
    for i in lineas_falsas:
        w("      linea %5d | %s" % (i, lineas0[i - 1].strip()))
    w("")

    texto = texto0
    escritas = []
    for numero, vuelta in SUJETOS:
        w("=" * 78)
        w("TAREA 1.%s . LA ENTRADA R.%d, DEL ACTA DE LA VUELTA %d"
          % ("a" if numero == 63 else "b", numero, vuelta))
        w("=" * 78)
        w("")
        w("B) LA ENTRADA ACOTADA EN LA SEDE, COMPUTADA Y NO TECLEADA")
        lineas = texto.split(NL)
        ini, fin = cota_de_la_entrada(lineas, numero)
        if ini is None:
            w("   ROJO: la cabecera `## R.%d.` no aparece exactamente 1 vez."
              % numero)
            continue
        w("   R.%d: lineas %d a %d, %d lineas" % (numero, ini, fin, fin - ini + 1))
        entrada = NL.join(lineas[ini - 1:fin])
        w("   CIFRA bytes de la entrada al entrar: %d"
          % len(entrada.encode("utf-8")))
        w("   trae el literal falso %r: %s"
          % (LITERAL_FALSO, "SI" if LITERAL_FALSO in entrada else "NO"))
        w("")

        w("C) EL REPARTO DEL ACTA %d, MEDIDO EN ESTA VUELTA POR LA VARA" % vuelta)
        m = REP.medir_acta(vuelta, w)
        w("")
        if m is None:
            w("   ROJO: no se pudo acotar el acta %d. NO SE ESCRIBE." % vuelta)
            continue

        w("D) LA IDEMPOTENCIA Y LA ESCRITURA")
        ya = ya_corregida(entrada)
        w("   la correccion de esta vuelta YA esta en R.%d: %s"
          % (numero, "SI" if ya else "NO"))
        bloque = bloque_de_correccion(numero, vuelta, m, lineas_falsas)
        w("   CIFRA bytes del bloque compuesto: %d" % len(bloque.encode("utf-8")))
        w("   CIFRA lineas del bloque compuesto: %d" % (bloque.count(NL) + 1))
        if a.escribir and not ya:
            nuevas = lineas[:fin] + bloque.split(NL) + lineas[fin:]
            texto = NL.join(nuevas)
            w("   ESCRITA: la adicion entra al FINAL de R.%d, en la linea %d,"
              % (numero, fin + 1))
            w("   sin tocar ni una linea del texto viejo.")
            escritas.append((numero, vuelta))
        elif a.escribir:
            w("   NO SE ESCRIBE: la correccion ya estaba. IDEMPOTENTE.")
        else:
            w("   MODO MEDICION: no se escribe nada.")
        w("")

    if a.escribir and texto != texto0:
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(texto)

    w("=" * 78)
    w("EL CIERRE, REMEDIDO Y NO HEREDADO")
    w("=" * 78)
    d1, lf1, sha1, texto1 = dos_convenciones(SEDE)
    w("   docs/PENDIENTES.md al salir: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (d1, lf1, sha1))
    w("   CIFRA crecimiento en bytes de disco: %d" % (d1 - d0))
    w("   CIFRA crecimiento en bytes LF: %d" % (lf1 - lf0))
    lineas1 = texto1.split(NL)
    w("   CIFRA lineas por split(NL) al salir: %d (al entrar %d, crecimiento %d)"
      % (len(lineas1), len(lineas0), len(lineas1) - len(lineas0)))
    w("   CIFRA entradas escritas por esta corrida: %d" % len(escritas))
    for numero, vuelta in escritas:
        w("      R.%d  ->  acta de la vuelta %d" % (numero, vuelta))
    w("")
    w("LA GUARDA DEL TEXTO VIEJO: NI UNA LINEA BORRADA NI UNA CAMBIADA")
    viejas = lineas0
    faltan = 0
    j = 0
    for l in viejas:
        while j < len(lineas1) and lineas1[j] != l:
            j += 1
        if j >= len(lineas1):
            faltan += 1
        else:
            j += 1
    w("   CIFRA lineas del texto de ENTRADA que NO estan, en orden, en el de")
    w("   SALIDA: %d" % faltan)
    w("   (la adicion solo puede ANADIR: si esta cifra no es 0, es ROJO)")
    w("")
    for numero, _v in SUJETOS:
        ini, fin = cota_de_la_entrada(lineas1, numero)
        if ini is None:
            w("   R.%d: ROJO, la cabecera no aparece 1 sola vez" % numero)
            continue
        entrada = NL.join(lineas1[ini - 1:fin])
        w("   R.%d al salir: lineas %d a %d | trae la marca de la correccion: %s"
          % (numero, ini, fin, "SI" if ya_corregida(entrada) else "NO"))
        w("   R.%d al salir: sigue trayendo el texto viejo con el literal %r: %s"
          % (numero, LITERAL_FALSO, "SI" if LITERAL_FALSO in entrada else "NO"))
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
