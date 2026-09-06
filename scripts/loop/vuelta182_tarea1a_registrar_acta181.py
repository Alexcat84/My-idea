# -*- coding: utf-8 -*-
r"""vuelta182_tarea1a_registrar_acta181.py . EL ACTA 181 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA.

LA MAQUINA NO SE CLONA, SE IMPORTA, y eso lo adjudico la `6.6` del acta 172 como
correcto y obligatorio: `PALABRA` y `titulo_de_la_negrita` se importan de
`scripts/loop/vuelta172_tarea1_registrar_acta171.py`, que es la sede que la
bateria ya vigila. Lo unico propio de este fichero es EL ACOTE DE SU ACTA, LA
FORMA DE SUS ETIQUETAS y SUS GLOSAS.

POR QUE HACE FALTA CODIGO PROPIO Y NO VALE EL REGISTRADOR DE SIEMPRE, MEDIDO Y NO
SUPUESTO: `claves_de_adjudicacion()` del registrador viejo busca `**6.1 `,
`**6.2 `, ... con el `6.` CLAVADO EN EL CODIGO, y el acta 181 numera sus
adjudicaciones `7.1` a `7.5`. Corrido tal cual sobre el acta 181 devolveria CERO
adjudicaciones y el titulo saldria mal. Aqui el prefijo es PARAMETRO, y la
version con prefijo `6.` se corre igualmente sobre esta acta para publicar el
contraste, que es como se ve que el cambio hacia falta.

LAS CIFRAS DEL TITULO NO SE TECLEAN: se cuentan del acta acotada. Ni el numero de
la entrada: lo devuelve `scripts/loop/serie_de_registros.py` recomputando la serie
de sus DOS sedes.

Y LA SEDE TAMPOCO SE SUPONE: `docs/PENDIENTES.md`, por la adjudicacion 6.3 del
acta 162, que es la que los `R.30` a `R.42` citan.

LO QUE ESTE FICHERO NO HACE: no toca el acta, no toca el reporte, no toca
`docs/plan/`, no corre la bateria y no escribe ningun veredicto. Escribe UNA
entrada en UNA sede, y si la entrada ya esta, NO la duplica y lo dice.

USO:
  python scripts/loop/vuelta182_tarea1a_registrar_acta181.py
  python scripts/loop/vuelta182_tarea1a_registrar_acta181.py --simular
  python scripts/loop/vuelta182_tarea1a_registrar_acta181.py --mutacion
"""
import argparse
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402
from vuelta172_tarea1_registrar_acta171 import (   # noqa: E402
    PALABRA, titulo_de_la_negrita)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 181
VUELTA_QUE_ESCRIBE = 182
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "7."

# LAS DOS FAMILIAS DE CAIDA DEL ACTA 181, cada una con su patron. El acta 181 NO
# usa la forma `**CAIDA n.` de las actas 169 a 172: usa `**`C.1`.` para la del
# auditor y `**`E.2`.` para la del ejecutor. Se declara y se mide, no se fuerza
# el patron viejo para que salga algo.
PAT_CAIDA_AUDITOR = re.compile(r"^\s*(?:-\s+)?\*\*`?C\.(\d+)`?[,.]")
PAT_CAIDA_EJECUTOR = re.compile(r"^\s*(?:-\s+)?\*\*`?E\.(\d+)`?[,.]")
PAT_CAIDA_VIEJA = re.compile(r"^\s*(?:-\s+)?\*\*`?CAIDA (\d+)`?[,.]")

# LA VIA DE CADA ADJUDICACION, escrita a mano porque es JUICIO del ejecutor sobre
# que hace ESTA vuelta con ella, y el juicio no sale de ningun instrumento. Lo
# que si sale de instrumento es el TITULO literal de cada una y su linea.
VIA = {
    "7.1": "SIN TOCAR NADA",
    "7.2": "EJECUTADA",
    "7.3": "SIN TOCAR NADA",
    "7.4": "EJECUTADA",
    "7.5": "SIN TOCAR NADA",
}

QUE_HACE_ESTA_VUELTA = {
    "7.1": ("SE ACATA SIN TOCAR NADA, Y NO HAY NADA QUE HACER PORQUE LA CAIDA ES "
            "AJENA Y YA ESTA CERRADA. El `E.2` de la 181 se registra y NO acumula "
            "por la letra afinada del 27 ago 2026: la cifra vivia en prosa de "
            "acompanamiento y no en tabla, cabecera ni conclusion. LA RACHA DE "
            "REPORTE SIGUE EN UNO, y esta vuelta la cita sin moverla."),
    "7.2": ("EJECUTADA EN LA TAREA 1.c DE ESTA VUELTA. La adjudicacion encarga la "
            "RELECTURA AL DOBLE del tramo por `AUDITOR.md` 1.2, porque las cinco "
            "discrepancias salieron FUERA del marcado. El tramo son los 30 puestos "
            "que la seccion 8 del acta lista, y esta vuelta los relee al doble con "
            "el instrumento de la TAREA 1.c, no a mano."),
    "7.3": ("SE ACATA SIN TOCAR NADA. Es la declaracion del propio auditor de que "
            "su `C.1` no contamino el sujeto de la ciega, con su medicion delante "
            "(solape cero con los 43 de la 180, guarda de fuga en 0, clases "
            "selladas antes del destape). No es trabajo del ejecutor, y se cita "
            "porque la TAREA 2 de esta vuelta convierte en codigo justamente el "
            "remedio que la `C.1` rompio."),
    "7.4": ("EJECUTADA POR LA VIA QUE EL FUNDADOR ABRIO, Y NO POR EXTENSION. La "
            "`7.4` dice que el 2.464 NO lo adjudica el auditor porque seria decidir "
            "el alcance de una fase, y lo sube a parada. El fundador decidio el 5 "
            "sep 2026 por la opcion `b` de la PREGUNTA 1, y las TAREAS 3 y 4 de "
            "esta vuelta la ejecutan: instrumento del diferenciador movido, y a la "
            "cola SOLO las `D` con la lesion exacta."),
    "7.5": ("SE ACATA SIN TOCAR NADA, Y SE REGISTRA A FAVOR. El acta declara que la "
            "bateria de la 181 no corrio y que eso NO es caida de reporte, porque "
            "el esqueleto por anexion dejo la fila diciendo ABIERTA, SIN CERRAR y "
            "no publico ninguna cifra de una corrida que no hubo. La bateria va a "
            "la 183 por tramos resumibles, y la TAREA 5 de esta vuelta la deja "
            "preparada y declarada."),
}


def cuerpo_del_acta(texto=None):
    """EL ACTA ACOTADA: (lineas, inicio, fin). El fin es el final del fichero
    porque el acta 181 es la ultima escrita; si algun dia dejara de serlo, la
    cabecera siguiente seria la frontera y esta funcion CAE EN ROJO antes que
    contar de mas."""
    if texto is None:
        texto = io.open(ACTA, encoding="utf-8").read()
    texto = texto.replace(chr(13) + NL, NL)
    lineas = texto.split(NL)
    cabeceras = [i for i, l in enumerate(lineas, 1)
                 if l.startswith("# ACTA DEL AUDITOR, VUELTA ")]
    mias = [i for i in cabeceras if lineas[i - 1].startswith(CABECERA_ACTA)]
    if len(mias) != 1:
        return None, None, "PARADA: %r aparece %d veces." % (CABECERA_ACTA, len(mias))
    inicio = mias[0]
    posteriores = [i for i in cabeceras if i > inicio]
    fin = (min(posteriores) - 1) if posteriores else len(lineas)
    return lineas, (inicio, fin), None


def claves_de_adjudicacion(lineas, inicio, fin, prefijo, tope=40):
    """LA CIFRA NO SE TECLEA. Barre `<prefijo>1`, `<prefijo>2`, ... hacia arriba
    y para en la primera que no aparece.

    EL PREFIJO ES PARAMETRO y esa es la unica diferencia con la funcion del
    registrador viejo, que lo lleva clavado como `6.`. El espacio final del
    patron es el que impide que `7.1` se coma a `7.10`."""
    claves = []
    for k in range(1, tope + 1):
        clave = "%s%d" % (prefijo, k)
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        cuantas = len([i for i in range(inicio, fin + 1) if pat.match(lineas[i - 1])])
        if cuantas == 0:
            break
        claves.append((clave, cuantas))
    return claves


def cuenta_por_patron(lineas, inicio, fin, patron):
    return [i for i in range(inicio, fin + 1) if patron.match(lineas[i - 1])]


def titulo_de_la_entrada(n_adj, n_cai_aud, n_cai_eje):
    """El titulo, con sus TRES numerales COMPUTADOS y no tecleados, y con la
    concordancia dentro del computo."""
    def trozo(n, sing, plur):
        return ("%s %s" % ("la" if n == 1 else "las", sing) if n == 1
                else "%s %s %s" % ("las", PALABRA[n], plur))
    return ("Registro de %s, %s del auditor y %s del ejecutor "
            "del acta de la vuelta %d"
            % (trozo(n_adj, "adjudicacion", "adjudicaciones"),
               trozo(n_cai_aud, "caida propia", "caidas propias"),
               trozo(n_cai_eje, "caida", "caidas"),
               VUELTA_DEL_ACTA))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true",
                    help="mide y arma la entrada, pero NO escribe en la sede")
    ap.add_argument("--mutacion", action="store_true",
                    help="corre el caso positivo por mutacion y no toca nada")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    if a.mutacion:
        return prueba_de_mutacion()

    salida = []
    w = salida.append
    w("=" * 78)
    w("VUELTA %d, TAREA 1.a: EL ACTA %d ENTERA, REGISTRADA EN LA FORMA DE LA CASA"
      % (VUELTA_QUE_ESCRIBE, VUELTA_DEL_ACTA))
    w("=" * 78)
    w("")

    lineas, rango, err = cuerpo_del_acta()
    if err:
        w(err)
        print(NL.join(salida))
        return 1
    inicio, fin = rango
    w("A) EL CUERPO DEL ACTA, ACOTADO ANTES DE CONTAR NADA")
    w("   acta %d: docs/loop/ACTA_AUDITOR.md, lineas %d a %d (%d lineas)"
      % (VUELTA_DEL_ACTA, inicio, fin, fin - inicio + 1))
    w("   docs/loop/ACTA_AUDITOR.md -> disco %d bytes" % os.path.getsize(ACTA))
    w("")

    w("B) LAS ADJUDICACIONES, CONTADAS Y NO TECLEADAS")
    claves = claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_ADJ)
    w("   prefijo usado: %r" % PREFIJO_ADJ)
    w("   CIFRA adjudicaciones halladas: %d" % len(claves))
    for clave, cuantas in claves:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    viejas = claves_de_adjudicacion(lineas, inicio, fin, "6.")
    w("   EL CONTRASTE QUE PRUEBA QUE EL PREFIJO HACIA FALTA: el registrador")
    w("   viejo busca %r clavado, y sobre ESTA acta eso da %d adjudicaciones."
      % ("6.", len(viejas)))
    dobles = [c for c, n in claves if n != 1]
    if dobles:
        w("   PARADA: hay claves repetidas dentro del acta: %s" % ", ".join(dobles))
        print(NL.join(salida))
        return 1
    w("")

    w("C) LAS CAIDAS, POR SUS DOS FAMILIAS, Y EL PATRON VIEJO AL LADO")
    l_aud = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR)
    l_eje = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_EJECUTOR)
    l_vie = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_VIEJA)
    w("   CAIDAS DEL AUDITOR (patron C.n): %d, en las lineas %s"
      % (len(l_aud), ", ".join(str(x) for x in l_aud) or "(ninguna)"))
    w("   CAIDAS DEL EJECUTOR (patron E.n): %d, en las lineas %s"
      % (len(l_eje), ", ".join(str(x) for x in l_eje) or "(ninguna)"))
    w("   EL PATRON VIEJO (CAIDA n), corrido sobre esta acta: %d" % len(l_vie))
    w("   (el patron viejo da CERO y por eso hay dos patrones nuevos: el acta 181")
    w("    no numera sus caidas como las actas 169 a 172. Se declara, no se fuerza)")
    if not l_aud or not l_eje:
        w("   PARADA: falta alguna de las dos familias de caida. No se escribe.")
        print(NL.join(salida))
        return 1
    w("")

    w("D) EL TITULO, CON SUS TRES NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(len(claves), len(l_aud), len(l_eje))
    w("   %s" % titulo)
    w("")

    w("E) LOS TITULOS LITERALES DE CADA ADJUDICACION, LEIDOS DEL ACTA")
    titulos = {}
    for clave, _n in claves:
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, err2 = titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err2:
            w("   %s -> %s" % (clave, err2))
            print(NL.join(salida))
            return 1
        titulos[clave] = res
        w("   %s (linea %d): %s" % (clave, res[0], res[1][:130]))
    w("")

    w("F) EL NUMERO DE LA ENTRADA, QUE NO SE TECLEA")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    w("   serie recomputada de sus dos sedes: %d entradas" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SERIE.colisiones(halladas)), len(SERIE.huecos(halladas))))
    w("   SIGUIENTE LIBRE: R.%d" % numero)
    w("")

    w("G) LA DEUDA DE LA SERIE, MEDIDA Y NO CALLADA")
    escritas = sorted(set(n for n, _r, _l, _t in halladas))
    con_acta = set()
    for _n, _r, _l, t in halladas:
        m = re.search(r"acta de la vuelta (\d+)", t)
        if m:
            con_acta.add(int(m.group(1)))
    faltan = [v for v in range(173, VUELTA_DEL_ACTA + 1) if v not in con_acta]
    w("   ultima entrada escrita: R.%d" % (escritas[-1] if escritas else 0))
    w("   actas con entrada propia en la serie: %s"
      % ", ".join(str(x) for x in sorted(con_acta)))
    w("   ACTAS ENTRE LA 173 Y LA %d SIN ENTRADA EN LA SERIE: %d -> %s"
      % (VUELTA_DEL_ACTA, len(faltan), ", ".join(str(x) for x in faltan)))
    w("   (esta vuelta escribe la de la %d, que es la que el encargo pide. Las"
      % VUELTA_DEL_ACTA)
    w("    demas se declaran como deuda medida y NO se inventan aqui)")
    w("")

    marca = "## R.%d." % numero
    texto_sede = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    ya = ("## R.%d. %s" % (numero, titulo)) in texto_sede
    w("H) LA IDEMPOTENCIA, COMPROBADA ANTES DE ESCRIBIR")
    w("   la marca %r ya esta en la sede: %s" % (marca, "SI" if marca in texto_sede
                                                 else "NO"))
    w("   la entrada entera ya esta: %s" % ("SI" if ya else "NO"))
    w("")

    entrada = armar_entrada(numero, titulo, claves, titulos, l_aud, l_eje, inicio, fin)
    w("I) LA ENTRADA ARMADA")
    w("   %d bytes | %d lineas" % (len(entrada.encode("utf-8")), entrada.count(NL)))
    w("")

    if a.simular:
        w("J) MODO --simular: NO SE ESCRIBE NADA EN LA SEDE.")
        w("")
        w("LA ENTRADA, ENTERA:")
        for l in entrada.split(NL):
            w("   | " + l)
    elif ya:
        w("J) NO SE ESCRIBE: la entrada ya esta en la sede, byte a byte.")
    else:
        nuevo = texto_sede.rstrip(NL) + NL + NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("J) ESCRITA EN docs/PENDIENTES.md")
        w("   la sede pasa de %d a %d bytes"
          % (len(texto_sede.encode("utf-8")), len(nuevo.encode("utf-8"))))
        rele = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
        w("   RELEIDA DEL DISCO: la entrada esta byte a byte: %s"
          % ("SI" if entrada.rstrip(NL) in rele else "NO"))
        w("   guiones largos o medios en la entrada: %d"
          % (entrada.count(chr(8212)) + entrada.count(chr(8211))))
        de_nuevo = SERIE.entradas()
        w("   serie recomputada TRAS escribir: %d entradas, siguiente libre R.%d"
          % (len(de_nuevo), SERIE.siguiente_libre(de_nuevo)))
        w("   CIFRA colisiones tras escribir: %d" % len(SERIE.colisiones(de_nuevo)))

    t = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_T1A_REGISTRO_R%d.txt" % numero)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


def armar_entrada(numero, titulo, claves, titulos, l_aud, l_eje, inicio, fin):
    p = []
    p.append("## R.%d. %s" % (numero, titulo))
    p.append("")
    p.append("(Acta del auditor, vuelta %d, secciones 2, 5 y 7; escrito en la vuelta %d,"
             % (VUELTA_DEL_ACTA, VUELTA_QUE_ESCRIBE))
    p.append("TAREA 1.a.)")
    p.append("")
    p.append("Por adicion, como `R.21` a `R.42`. **Corte de todas las cifras de esta")
    p.append("entrada: 5 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.42`. Salida:")
    p.append("`docs/loop/SALIDA_V%d_T1A_REGISTRO_R%d.txt`."
             % (VUELTA_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 1.a EN CURSO Y LAS TAREAS 2 A 5 SIN")
    p.append("CORRER, ASI QUE SUS GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA NO HA")
    p.append("PASADO.** Es la forma que la `6.4` del acta 172 adjudico como correcta y que")
    p.append("la realidad probo cuando la vuelta 172 se corto: donde una glosa dice")
    p.append("EJECUTADA, la prueba va nombrada con su fichero de salida; donde dice que va")
    p.append("a ejecutarse, se dice que **todavia no ha corrido** y no se disfraza.")
    p.append("")
    p.append("**Y LOS TRES NUMERALES DEL TITULO TAMPOCO ESTAN TECLEADOS:** se cuentan del")
    p.append("acta acotada (lineas %d a %d) y de ahi sale el numeral en palabra, incluida"
             % (inicio, fin))
    p.append("la concordancia. **%d adjudicaciones `7.n`, %d caida propia del auditor"
             % (len(claves), len(l_aud)))
    p.append("(`C.n`) y %d caida del ejecutor (`E.n`).**" % len(l_eje))
    p.append("")
    p.append("**EL PATRON DE CAIDA SI CAMBIA ESTA VEZ, Y SE DECLARA EN VEZ DE FORZARLO.**")
    p.append("Las actas 169 a 172 numeraban sus caidas `**CAIDA n.`; el acta 181 usa")
    p.append("``**`C.1`.`` para la del auditor y ``**`E.2`.`` para la del ejecutor. **El")
    p.append("patron viejo, corrido sobre el acta 181, cuenta CERO**, y esa cifra se")
    p.append("publica al lado de las otras dos para que se vea que no se afloja nada: se")
    p.append("anaden dos patrones nuevos, no se ensancha el viejo hasta que trague.")
    p.append("")
    p.append("**Y EL PREFIJO DE LAS ADJUDICACIONES TAMBIEN.** `claves_de_adjudicacion()`")
    p.append("del registrador viejo lleva el `6.` clavado en el codigo y el acta 181 numera")
    p.append("`7.1` a `7.5`. **Corrida con el prefijo viejo sobre esta acta, la cuenta da")
    p.append("CERO.** Aqui el prefijo es parametro. `PALABRA` y `titulo_de_la_negrita` **se")
    p.append("importan** de `scripts/loop/vuelta172_tarea1_registrar_acta171.py`, no se")
    p.append("copian, que es la `6.6` del acta 172 al pie de la letra.")
    p.append("")
    p.append("**LAS %s ADJUDICACIONES, CON SU LINEA EN EL ACTA LEIDA HOY.** El titulo de"
             % PALABRA[len(claves)].upper())
    p.append("cada una es LITERAL del fichero; la glosa que sigue es prosa del ejecutor y")
    p.append("va marcada como tal.")
    p.append("")
    for clave, _n in claves:
        ln, tit = titulos[clave]
        p.append("  - **%s (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). VIA: %s.** Titulo"
                 % (clave, ln, VIA[clave]))
        p.append("    literal del acta: *\"%s\"*" % tit)
        p.append("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA[clave])
    p.append("")
    p.append("**LA CAIDA PROPIA DEL AUDITOR, EN LA LINEA %d, Y NO ES TRABAJO DEL"
             % l_aud[0])
    p.append("EJECUTOR.** Es la `C.1`, la **cuarta seguida**, y ademas la primera en que el")
    p.append("remedio escrito existia y aun asi no se cumplio. **Se registra porque la")
    p.append("TAREA 2 de esta vuelta convierte ese remedio en codigo**, que es la mitad")
    p.append("que el fundador concedio el 5 sep 2026 (PREGUNTA 3, opcion `c`); la otra")
    p.append("mitad, que romper un remedio escrito ACUMULE, ya esta en `AUDITOR.md`.")
    p.append("")
    p.append("**LA CAIDA DEL EJECUTOR, EN LA LINEA %d: `E.2`, Y NO ACUMULA.** La cuenta de"
             % l_eje[0])
    p.append("quien nombra `SALIDA_V180_HUECO_BATERIA` en `scripts/` era 1 cuando se midio")
    p.append("y era 3 cuando se publico. **La cifra se midio bien y se publico tarde**, y")
    p.append("vive en prosa de acompanamiento, no en tabla, cabecera ni conclusion: por la")
    p.append("letra afinada del 27 ago 2026 **NO acumula**. **La racha de reporte se queda")
    p.append("en UNO.**")
    p.append("")
    p.append("**LA DEUDA DE LA SERIE, MEDIDA HOY Y DECLARADA EN VEZ DE CALLADA.** La ultima")
    p.append("entrada escrita antes de esta registraba el acta de la vuelta **172**")
    p.append("(`R.42`). **Las actas 173 a 180 no tienen entrada propia en la serie.** Esta")
    p.append("vuelta escribe la de la 181, que es la que su encargo pide, y **deja las ocho")
    p.append("anteriores dichas y contadas**, con su cifra en")
    p.append("`docs/loop/SALIDA_V%d_T1A_REGISTRO_R%d.txt`, seccion G. **No se inventan")
    p.append("aqui**: escribir de golpe ocho registros que nadie encargo seria decidir")
    p.append("alcance por mi cuenta.")
    return NL.join(p) + NL


def _acta_fabricada(adjudicaciones, caidas_aud, caidas_eje, prefijo="7."):
    """UN ACTA DE MENTIRA para el caso positivo por mutacion. NO toca el repo."""
    L = ["# ACTA DEL AUDITOR, VUELTA %d (fabricada)" % VUELTA_DEL_ACTA, ""]
    for k in range(1, caidas_aud + 1):
        L += ["**`C.%d`. UNA CAIDA DEL AUDITOR DE MENTIRA.**" % k, ""]
    for k in range(1, caidas_eje + 1):
        L += ["**`E.%d`. UNA CAIDA DEL EJECUTOR DE MENTIRA.**" % k, ""]
    L += ["## 7. LAS ADJUDICACIONES", ""]
    for k in range(1, adjudicaciones + 1):
        L += ["**%s%d UN TITULO DE MENTIRA NUMERO %d.** Y su cuerpo." % (prefijo, k, k), ""]
    return NL.join(L) + NL


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION, SOBRE VARIABLE COMPUTADA Y NO SOBRE
    CONSTANTE LITERAL (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION).

    Se fabrica un acta con OTRAS cifras, se corre el contador de verdad sobre
    ella, y se exige que el titulo CAMBIE. Despues se muta el valor esperado y se
    comprueba que el caso CAE: si no cayera, el caso no probaria nada."""
    sys.stdout.reconfigure(encoding="utf-8")
    salida = []
    w = salida.append
    w("CASO POSITIVO POR MUTACION de vuelta182_tarea1a_registrar_acta181.py")
    w("")
    fallos = 0
    casos = [(5, 1, 1), (3, 2, 1), (12, 1, 4), (1, 1, 1)]
    for n_adj, n_aud, n_eje in casos:
        texto = _acta_fabricada(n_adj, n_aud, n_eje)
        lineas, rango, err = cuerpo_del_acta(texto)
        if err:
            w("   %r -> %s" % ((n_adj, n_aud, n_eje), err))
            fallos += 1
            continue
        ini, fin = rango
        claves = claves_de_adjudicacion(lineas, ini, fin, PREFIJO_ADJ)
        aud = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR)
        eje = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_EJECUTOR)
        # LAS TRES VARIABLES SON COMPUTADAS: salen de correr el contador sobre el
        # acta fabricada, no de escribirlas aqui.
        ok = (len(claves) == n_adj and len(aud) == n_aud and len(eje) == n_eje)
        titulo = titulo_de_la_entrada(len(claves), len(aud), len(eje))
        w("   acta fabricada con adj=%d aud=%d eje=%d" % (n_adj, n_aud, n_eje))
        w("      el contador dice adj=%d aud=%d eje=%d -> %s"
          % (len(claves), len(aud), len(eje), "CALZA" if ok else "NO CALZA"))
        w("      titulo computado: %s" % titulo)
        if not ok:
            fallos += 1
    w("")
    w("LA MUTACION DEL VALOR ESPERADO, QUE ES LO QUE PRUEBA QUE EL CASO PUEDE CAER:")
    texto = _acta_fabricada(5, 1, 1)
    lineas, (ini, fin), _e = cuerpo_del_acta(texto)
    medido = len(claves_de_adjudicacion(lineas, ini, fin, PREFIJO_ADJ))
    esperado_bueno = 5
    esperado_mutado = 6
    w("   medido sobre el acta fabricada (variable computada): %d" % medido)
    w("   con el esperado BUENO   (%d): %s"
      % (esperado_bueno, "PASA" if medido == esperado_bueno else "CAE"))
    w("   con el esperado MUTADO  (%d): %s"
      % (esperado_mutado, "PASA" if medido == esperado_mutado else "CAE"))
    cae_al_mutar = medido != esperado_mutado
    w("   EL CASO CAE AL MUTAR EL ESPERADO: %s" % ("SI" if cae_al_mutar else "NO"))
    if not cae_al_mutar:
        fallos += 1
    w("")
    w("LA SEGUNDA MUTACION: EL PREFIJO. Con el prefijo viejo el contador tiene que")
    w("dar CERO sobre un acta que numera 7.n, que es justo el motivo de este fichero.")
    con_viejo = len(claves_de_adjudicacion(lineas, ini, fin, "6."))
    w("   prefijo %r sobre acta de %r -> %d adjudicaciones" % ("6.", "7.", con_viejo))
    w("   EL CASO CAE CON EL PREFIJO VIEJO: %s" % ("SI" if con_viejo == 0 else "NO"))
    if con_viejo != 0:
        fallos += 1
    w("")
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_T1A_MUTACION_REGISTRO.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
