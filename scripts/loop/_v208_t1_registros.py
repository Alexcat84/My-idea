# -*- coding: utf-8 -*-
r"""_v208_t1_registros.py . TAREA 1 DE LA VUELTA 208: `R.72` PARA EL ACTA 207,
ESCRITA EN `docs/PENDIENTES.md` POR ADICION PURA Y EN SU SEDE.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3). **NO SE ESCRIBE NINGUN LECTOR NUEVO Y
TAMPOCO SE CLONA NINGUNO:** todo lo que lee viene IMPORTADO de
`_v203_reparto_de_actas_viejas.py`, de `serie_de_registros.py`, de
`vuelta184_tarea1a_registrar_acta184.py`, de
`vuelta192_tarea1a_registrar_acta192.py` y de `_v206_t2_registros.py`, del que se
reutilizan `ya_escrita()`, `dos_convenciones()`, `numeral()` y `titulo_de()` tal
cual. IMPORTAR NO ES CLONAR (acta 206, adjudicacion `6.5`).

EL NUMERO NO SE TECLEA: lo computa `serie_de_registros.siguiente_libre()`
recomputando la serie de sus DOS sedes, al ENTRAR y al SALIR.

--- LO QUE ESTA ENTRADA TIENE DE DISTINTO, Y ES LA NOVEDAD DE LA VUELTA ---

`R.63` a `R.71` tuvieron que DECLARAR NO COMPUTABLES la mayoria de sus numerales,
porque las actas modernas dejaron de escribirse como la vara del `4.1` del acta
202 espera. **EL ACTA 207 SE ESCRIBIO A PROPOSITO PARA QUE LA VARA LA LEA** (su
adjudicacion `6.8`: *"el otro lado es como titulo yo"*), y por eso esta entrada es
la primera en mucho tiempo que puede publicar CIFRAS y no declaraciones de
ceguera.

**LA CIFRA DEL AUDITOR ES CONTRASTE Y NO FUENTE** (`EJECUTOR.md` 2). El acta
publica en su `7.1` que la vara saca **4 de 4** sobre la 207 y **1 de 4** sobre la
206. Aqui se CORRE la vara sobre LAS DOS actas, con el lector IMPORTADO y sin
tocarle una linea, y se publica lo que dé. Si discrepa, la discrepancia se declara
y NO se resuelve copiando.

USO:
  python scripts/loop/_v208_t1_registros.py
  python scripts/loop/_v208_t1_registros.py --escribir
  python scripts/loop/_v208_t1_registros.py --escribir --salida NOMBRE
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
VUELTA_QUE_ESCRIBE = 208
CORTE = "7 sep 2026"
SUJETO = 207
CONTRASTE = 206

# LAS CINCO ADJUDICACIONES QUE EL ENCARGO DICE QUE CIERRAN PENDIENTES, Y QUE
# PENDIENTE CIERRA CADA UNA. ES UN DATO DEL ENCARGO, NO UNA MEDICION, y por eso
# va marcado como tal: la cifra de adjudicaciones se MIDE del acta, y esto solo
# le pone al lado que pendiente del reporte 207 cierra cada una.
CIERRAN = {
    "6.1": "`P.2` del reporte de la 207",
    "6.3": "`P.3` del reporte de la 207",
    "6.4": "`PD.1` del reporte de la 207",
    "6.5": "el TOPE de sub-tareas, que vuelve a cinco",
    "6.8": "`P.1` del reporte de la 207",
}


def vara_sobre(vuelta, w):
    """CORRE LA VARA DEL `4.1` SOBRE UN ACTA Y DEVUELVE (m, computables). NO
    ESCRIBE NADA. `computables` es cuantos de los CUATRO numerales de seccion
    titulada dan cifra, que es la misma cuenta que el acta 207 publica en su
    `7.1` y que aqui se recorre en vez de copiarse."""
    w("   --- LA VARA SOBRE EL ACTA %d ---" % vuelta)
    m = REP.medir_acta(vuelta, w)
    if m is None:
        return None, None
    computables = 0
    detalle = []
    for etiqueta in ("adjudicaciones", "hallazgos", "caidas_del_auditor",
                     "caidas_del_ejecutor"):
        d = m.get(etiqueta)
        sec = m.get(etiqueta + "_sec")
        if d is None:
            detalle.append((etiqueta, None, None, "NINGUNA SECCION LA TITULA"))
            continue
        n = len(d["nm"])
        if n == 0:
            detalle.append((etiqueta, sec, 0,
                            "SECCION HALLADA (linea %d) PERO 0 CLAVES" % sec[1]))
            continue
        computables += 1
        detalle.append((etiqueta, sec, n,
                        ", ".join(c for c, _x in d["nm"])))
    w("   CIFRA numerales COMPUTABLES sobre el acta %d: %d de 4"
      % (vuelta, computables))
    for et, _sec, n, txt in detalle:
        w("      %-22s %s" % (et.upper().replace("_", " "),
                              ("%d -> %s" % (n, txt)) if n else txt))
    return m, (computables, detalle)


def armar_entrada(numero, m, titulo, titulo_crudo, comp207, comp206, w):
    """COMPONE EL TEXTO DE `R.72`. No lee nada del disco: recibe lo ya medido."""
    lineas = m["lineas"]
    p = []
    a = p.append
    a("## R.%d. %s" % (numero, titulo))
    a("")
    a("(Acta del auditor, vuelta %d; escrito en la vuelta %d, TAREA 1.)"
      % (SUJETO, VUELTA_QUE_ESCRIBE))
    a("")
    a("Por adicion, como `R.21` a `R.71`. **Corte de todas las cifras de esta")
    a("entrada: %s.** El numero de esta entrada NO esta tecleado: lo computa" % CORTE)
    a("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes,")
    a("corrido AL ENTRAR y AL SALIR. Salida:")
    a("`docs/loop/SALIDA_V%d_T1_REGISTROS.txt`." % VUELTA_QUE_ESCRIBE)
    a("")
    a("**ESTA ES LA PRIMERA ENTRADA EN NUEVE REGISTROS QUE PUEDE PUBLICAR LOS")
    a("CUATRO NUMERALES COMO CIFRAS EN VEZ DE DECLARARLOS NO COMPUTABLES, Y EL")
    a("MOTIVO NO ES QUE LA VARA CAMBIARA.** `R.63` a `R.71` declararon casi todos")
    a("sus numerales no computables porque las actas modernas dejaron de escribirse")
    a("como la vara del `4.1` del acta 202 espera. **El acta 207 se escribio a")
    a("proposito para que la vara la lea** (su adjudicacion `6.8`), y el lector no")
    a("se toco ni en una linea. **La moratoria de `AUDITOR.md` 6.3 queda intacta.**")
    a("")
    a("**NINGUN LECTOR NUEVO PERMANENTE SE ESCRIBIO PARA ESTA ENTRADA Y NINGUNO SE")
    a("CLONO.** El computo vive en `scripts/loop/_v%d_t1_registros.py`, con prefijo"
      % VUELTA_QUE_ESCRIBE)
    a("de guion bajo, **fuera del censo y fuera de la nomina**, y IMPORTA")
    a("`scripts/loop/_v203_reparto_de_actas_viejas.py`, `serie_de_registros.py`,")
    a("`vuelta184_tarea1a_registrar_acta184.py`,")
    a("`vuelta192_tarea1a_registrar_acta192.py` y")
    a("`scripts/loop/_v206_t2_registros.py`. **IMPORTAR NO ES CLONAR** (acta 206")
    a("`6.5`).")
    a("")
    a("**EL ACTA ACOTADA EN ESTA VUELTA:** lineas **%d** a **%d**, **%d** lineas,"
      % (m["ini"], m["fin"], m["fin"] - m["ini"] + 1))
    a("sobre un fichero de **%d** bytes en disco y **%d** normalizado a LF. Su"
      % (m["bytes_disco"], m["bytes_lf"]))
    a("cuerpo trae **%d** secciones `## N. TITULO`." % len(m["secs"]))
    a("")
    a("### LOS CUATRO NUMERALES, POR LA VARA Y SIN RETOCAR")
    a("")
    a("| numeral | seccion que la VARA elige por su TITULO | numero | linea | claves | cuantas |")
    a("|---|---|---:|---:|---|---:|")
    for etiqueta in ("adjudicaciones", "hallazgos", "caidas_del_auditor",
                     "caidas_del_ejecutor"):
        d = m.get(etiqueta)
        nombre = etiqueta.replace("_", " ")
        if d is None:
            a("| %s | **NINGUNA SECCION DE ESTA ACTA TITULA ESTE NUMERAL** | "
              "(no aplica) | (no aplica) | (no aplica) | **no computable** |"
              % nombre)
            continue
        sec = d["sec"]
        claves = ", ".join("`%s`" % c for c, _n in d["nm"]) or "(ninguna)"
        a("| %s | %s | %d | %d | %s | **%d** |"
          % (nombre, sec[2].replace("|", "/"), sec[0], sec[1], claves,
             len(d["nm"])))
    a("")
    a("**CIFRA numerales COMPUTABLES de 4 sobre el acta %d: %d.**"
      % (SUJETO, comp207[0]))
    a("")
    a("### LA MISMA VARA SOBRE EL ACTA %d, CORRIDA POR MI Y NO COPIADA" % CONTRASTE)
    a("")
    a("La `7.1` del acta 207 publica **4 de 4** sobre la 207 contra **1 de 4** sobre")
    a("la 206, y su salida es `docs/loop/SALIDA_V207_VARA_SOBRE_MI_ACTA.txt`. **Esa")
    a("cifra es CONTRASTE y no fuente** (`EJECUTOR.md` 2): aqui se vuelve a correr")
    a("la vara sobre las dos actas, con el mismo lector importado.")
    a("")
    a("| acta | numerales COMPUTABLES de 4, medidos por mi | el acta 207, como contraste | calza |")
    a("|---|---:|---:|---|")
    a("| **%d** | **%d** | 1 | %s |"
      % (CONTRASTE, comp206[0], "SI" if comp206[0] == 1 else "**NO**"))
    a("| **%d** | **%d** | 4 | %s |"
      % (SUJETO, comp207[0], "SI" if comp207[0] == 4 else "**NO**"))
    a("")
    a("### LAS %d ADJUDICACIONES DEL ACTA %d, UNA POR UNA Y CON SU LINEA"
      % (len(m["adjudicaciones"]["nm"]), SUJETO))
    a("")
    a("**LAS CINCO QUE CIERRAN PENDIENTES SE DICEN AL REGISTRARLAS**, como el")
    a("encargo pide: la `6.1` cierra la `P.2`, la `6.3` la `P.3`, la `6.4` la")
    a("`PD.1`, la `6.5` el tope de sub-tareas y la `6.8` la `P.1`. **Las tres")
    a("restantes (`6.2`, `6.6` y `6.7`) no cierran ningun pendiente numerado.**")
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
    a("### LOS %d HALLAZGOS, LAS %d CAIDAS PROPIAS DEL AUDITOR Y LA %d DEL EJECUTOR"
      % (len(m["hallazgos"]["nm"]),
         len(m["caidas_del_auditor"]["nm"]),
         len(m["caidas_del_ejecutor"]["nm"])))
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
    a("**LOS HALLAZGOS VAN EN EL ORDEN EN QUE EL ACTA LOS ESCRIBE, QUE NO ES EL")
    a("ORDEN DE SUS NUMEROS**, y eso se dice en vez de reordenarlos en silencio.")
    a("")
    a("### EL CERO FALSO QUE ESTE TITULO NO PUBLICA, DECLARADO Y MEDIDO")
    a("")
    a("`REG206.titulo_de()` cuenta las caidas con `numeral(dato, 'viejas')`, o sea")
    a("**por la forma antigua `CAIDA n`**. **El acta %d no usa esa forma**: escribe" % SUJETO)
    a("sus caidas como `9.1` a `9.4` y `4.1`, que es la forma `N.M` de la vara.")
    a("Corrido tal cual, el titulo diria **las 0 caidas propias del auditor** sobre")
    a("un acta que trae **cuatro**, y eso es publicar el cero de un instrumento como")
    a("un hecho del mundo (`EJECUTOR.md` 9).")
    a("")
    a("| caida | por `CAIDA n`, la forma antigua | por `N.M`, la forma de esta acta |")
    a("|---|---:|---:|")
    for etiqueta in ("caidas_del_auditor", "caidas_del_ejecutor"):
        dd = m[etiqueta]
        a("| %s | **%d** | **%d** |"
          % (etiqueta.replace("_", " "), len(dd["viejas"]), len(dd["nm"])))
    a("")
    a("**NINGUN LECTOR SE TOCO: SE CAMBIO EL DATO, NO LA MAQUINA.** A la misma")
    a("`titulo_de()` importada se le pasan las caidas contadas por la forma que esta")
    a("acta usa. **Y EL TITULO CRUDO QUEDA ESCRITO AQUI, ENTERO Y SIN TACHAR**, que")
    a("es la regla de la correccion declarada de la casa:")
    a("")
    a("> %s" % titulo_crudo)
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
    w("VUELTA %d, TAREA 1: R.72 PARA EL ACTA %d" % (VUELTA_QUE_ESCRIBE, SUJETO))
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

    w("C) LA VARA DEL `4.1` DEL ACTA 202, CORRIDA POR MI SOBRE LAS DOS ACTAS")
    m206, comp206 = vara_sobre(CONTRASTE, w)
    w("")
    m, comp207 = vara_sobre(SUJETO, w)
    w("")
    if m is None or m206 is None:
        w("   ROJO: no se pudo acotar alguna de las dos actas. NO SE ESCRIBE.")
        print(NL.join(L))
        return 1
    w("C.1) LO QUE EL ACTA 207 PUBLICA EN SU `7.1`, COMO CONTRASTE")
    w("   el acta dice: 4 de 4 sobre la 207 y 1 de 4 sobre la 206")
    w("   mi medicion:  %d de 4 sobre la 207 y %d de 4 sobre la 206"
      % (comp207[0], comp206[0]))
    calza = (comp207[0] == 4 and comp206[0] == 1)
    w("   CALZAN LAS DOS: %s" % ("SI" if calza else "NO, Y LA DISCREPANCIA SE "
                                 "DECLARA Y VA A LA SECCION 3.0"))
    w("")

    w("C.2) LAS OCHO ADJUDICACIONES, POR SU NUMERO Y CON SU LINEA")
    d = m["adjudicaciones"]
    w("   CIFRA adjudicaciones medidas: %d" % len(d["nm"]))
    for clave, _n in d["nm"]:
        for ln in d["donde"][clave]:
            w("      %-4s linea %5d  cierra: %-42s | %s"
              % (clave, ln, CIERRAN.get(clave, "(ninguno)"),
                 m["lineas"][ln - 1].strip()[:96]))
    faltan = [k for k in CIERRAN if k not in [c for c, _n in d["nm"]]]
    w("   CIFRA de las cinco que cierran pendientes que NO estan entre las")
    w("   medidas: %d (%s)" % (len(faltan), ", ".join(faltan) or "ninguna"))
    if faltan:
        w("   ROJO: el encargo nombra una adjudicacion que el acta no trae.")
        print(NL.join(L))
        return 1
    w("")

    w("D) EL TITULO DE LA ENTRADA, Y EL CERO FALSO QUE NO SE PUBLICA")
    w("   `REG206.titulo_de()` cuenta las caidas con `numeral(dato, 'viejas')`, o")
    w("   sea por la forma ANTIGUA `CAIDA n`. ESTA ACTA NO USA ESA FORMA: escribe")
    w("   sus caidas como `9.1` a `9.4` y `4.1`, que es la forma `N.M` de la vara.")
    w("   Corrido tal cual, el titulo saldria diciendo LAS 0 CAIDAS PROPIAS DEL")
    w("   AUDITOR sobre un acta que trae CUATRO, y eso es publicar un cero de un")
    w("   instrumento como un hecho del mundo (`EJECUTOR.md` 9).")
    titulo_crudo = REG206.titulo_de(m, SUJETO)
    w("   TITULO CRUDO, publicado como contraste y NO usado: %s" % titulo_crudo)
    w("   LAS DOS CUENTAS DE CADA CAIDA, JUNTAS Y SIN ELEGIR EN SILENCIO:")
    for etiqueta in ("caidas_del_auditor", "caidas_del_ejecutor"):
        dd = m[etiqueta]
        w("      %-22s por `CAIDA n`: %d | por `N.M` (la forma de esta acta): %d"
          % (etiqueta.replace("_", " "), len(dd["viejas"]), len(dd["nm"])))
    w("   LO QUE SE HACE, Y NO TOCA NI UNA LINEA DE NINGUN LECTOR: se le pasa a")
    w("   `titulo_de()` LA MISMA FUNCION IMPORTADA, con las caidas contadas por la")
    w("   forma que ESTA acta usa. Se cambia EL DATO, no la maquina.")
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
    entrada = armar_entrada(numero, m, titulo, titulo_crudo, comp207, comp206, w)
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
    sin = sorted(v for v in range(173, 208) if v not in con)
    w("LA DEUDA DE REGISTROS, REMEDIDA AL CIERRE Y ENSANCHADA HASTA LA 207")
    w("   CIFRA actas de la 173 a la 207 SIN entrada propia: %d" % len(sin))
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
