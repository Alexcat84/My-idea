# -*- coding: utf-8 -*-
r"""cotejo_de_ciega.py . EL FORMATO UNICO DEL COTEJO DE CIEGA, Y SU LECTOR.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como `aislador_de_ciega.py`,
`apertura_del_auditor.py`, `tallar_cabecera_reporte.py`, `serie_de_registros.py`
y `cerrar_reporte.py`: lo usan TODAS las ciegas de aqui en adelante y NO SE
CLONA. Un fichero que se clona por vuelta es un fichero que la vuelta siguiente
puede escribir de otra manera, y **de otra manera es exactamente la enfermedad
que esto viene a curar**.

DE DONDE SALE, PALABRA POR PALABRA. Es el `P.2` del ejecutor, adjudicado A FAVOR
en la `4.9` del acta 192: *"la TAREA 5 midio que el universo se queda en 6 de 43
ficheros por una razon de formato y no de fondo... mientras eso siga asi ninguna
medicion sobre la historia de ciegas va a alcanzar para concluir nada"*. **Tres
cotejos de ciega DE VERDAD (los de las vueltas 183, 184 y 190) quedan fuera de
esa medicion por FORMATO y no por FONDO.**

--- LO QUE EL FORMATO EXIGE, Y POR QUE CADA COSA ---

Cinco columnas, todas explicitas, **una fila POR CADA PUESTO COTEJADO y no solo
por las discrepancias**:

  1. `puesto`             . el numero, para poder cruzarlo con el archivo.
  2. `clase del lector`   . lo que el lector escribio a ciegas.
  3. `clase del archivo`  . lo que el archivo dice.
  4. `en dudosos`         . `si` o `no`: si el lector lo habia marcado DELANTE.
  5. `veredicto`          . `COINCIDE` o `DISCREPA`, computado de las dos clases
                            y NO tecleado.

**Y LA RAZON DE QUE LAS FILAS SEAN TODAS Y NO SOLO LAS DISCREPANCIAS ES EL
DENOMINADOR.** Dos de los seis ficheros que hoy entran en la medicion **solo
listan discrepancias**, y por eso no se sabe sobre cuantos pares se midieron. Una
tasa sin denominador no es una tasa: es un numero suelto. Con este formato el
denominador **se recupera contando las filas**, y ademas va DECLARADO en la
cabecera, **y las dos cifras tienen que calzar o el fichero es ROJO**.

--- LO QUE ESTE FORMATO NO PUEDE HACER, DICHO ANTES DE SU PRIMERA CIFRA ---

**No convierte en legible un cotejo viejo que no trae la informacion.** Un
fichero que nunca escribio la clase del lector no la tiene, y ningun lector la
puede recuperar. Lo que este formato hace es que **de aqui en adelante no vuelva
a pasar**; lo que se pueda rescatar de los viejos lo dice
`lector_de_cotejos_viejos()`, y lo que no se pueda se nombra en vez de estimarse.

**Y no dice si el lector acerto.** Dice si coincide con el archivo, que es otra
cosa: el archivo tambien se equivoca, y esta casa tiene correcciones declaradas
que lo prueban.

USO COMO INSTRUMENTO:
  from cotejo_de_ciega import escribir_cotejo, filas_del_cotejo, denominador
  escribir_cotejo(ruta, cabecera=[...], filas=[(puesto, clase_lector,
                  clase_archivo, en_dudosos)])

USO DESDE LA LINEA:
  python scripts/loop/cotejo_de_ciega.py --leer docs/loop/SALIDA_V192_T2_COTEJO.txt
  python scripts/loop/cotejo_de_ciega.py --mutacion
"""
import argparse
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MARCA_FORMATO = "FORMATO: COTEJO_DE_CIEGA v1"
CABECERA_TABLA = ("puesto | clase del lector | clase del archivo | "
                  "en dudosos del lector | veredicto")
ABRE_TABLA = "TABLA (una fila POR CADA PUESTO COTEJADO, no solo por las discrepancias):"
FIN_TABLA = "FIN DE LA TABLA."
LINEA_DENOMINADOR = "CIFRA puestos cotejados"

PAT_FILA = re.compile(
    r"^\s*(\d+)\s*\|\s*([A-Za-z?]+)\s*\|\s*([A-Za-z?]+)\s*\|\s*(si|no)\s*\|"
    r"\s*(COINCIDE|DISCREPA)\s*$")
PAT_DENOM = re.compile(r"^%s:\s*(\d+)\s*$" % re.escape(LINEA_DENOMINADOR))


def veredicto_de(clase_lector, clase_archivo):
    """COINCIDE O DISCREPA, COMPUTADO Y NO TECLEADO. PURA.

    La comparacion es por la letra en mayusculas y nada mas: no se normaliza
    ninguna otra cosa, para que una clase escrita de otra manera SALGA a la vista
    en vez de resolverse en silencio."""
    return "COINCIDE" if str(clase_lector).upper() == str(clase_archivo).upper() \
        else "DISCREPA"


def filas_del_cotejo(texto):
    """LAS FILAS DE UN COTEJO EN ESTE FORMATO. PURA.

    Devuelve `[(puesto, clase_lector, clase_archivo, en_dudosos, veredicto)]`,
    vacia si el texto no trae ninguna fila legible. `en_dudosos` sale como bool."""
    salida = []
    for linea in texto.replace(chr(13) + NL, NL).split(NL):
        m = PAT_FILA.match(linea)
        if not m:
            continue
        salida.append((int(m.group(1)), m.group(2).upper(), m.group(3).upper(),
                       m.group(4) == "si", m.group(5)))
    return salida


def denominador(texto):
    """(OK, DECLARADO, CONTADO, MOTIVO). PURA. **ES LA GUARDA DEL FORMATO.**

    `declarado` es la cifra de la cabecera; `contado` es cuantas filas trae la
    tabla. **Si no calzan, o si falta alguna de las dos, `ok` es False y el
    motivo lo dice.** Un cotejo que solo lista discrepancias no puede pasar por
    aqui, y ese es exactamente el caso que su prueba de mutacion fabrica."""
    dec = None
    for linea in texto.replace(chr(13) + NL, NL).split(NL):
        m = PAT_DENOM.match(linea.strip())
        if m:
            dec = int(m.group(1))
            break
    filas = filas_del_cotejo(texto)
    if MARCA_FORMATO not in texto:
        return False, dec, len(filas), "el fichero no declara %r" % MARCA_FORMATO
    if dec is None:
        return False, None, len(filas), \
            "no trae la linea %r en su cabecera" % LINEA_DENOMINADOR
    if not filas:
        return False, dec, 0, "la tabla no trae ninguna fila legible"
    if dec != len(filas):
        return False, dec, len(filas), \
            ("el denominador declarado (%d) no calza con las filas contadas (%d)"
             % (dec, len(filas)))
    return True, dec, len(filas), "declarado y contado calzan"


def resumen(filas):
    """LAS CIFRAS DEL COTEJO, COMPUTADAS DE LAS FILAS. PURA. Devuelve un dict."""
    disc = [f for f in filas if f[4] == "DISCREPA"]
    coin = [f for f in filas if f[4] == "COINCIDE"]
    dud = [f for f in filas if f[3]]
    return {
        "total": len(filas),
        "coinciden": len(coin),
        "discrepan": len(disc),
        "dudosos": len(dud),
        "disc_dentro": [f[0] for f in disc if f[3]],
        "disc_fuera": [f[0] for f in disc if not f[3]],
        "reparto_lector": _reparto(filas, 1),
        "reparto_archivo": _reparto(filas, 2),
    }


def _reparto(filas, i):
    d = {}
    for f in filas:
        d[f[i]] = d.get(f[i], 0) + 1
    return d


def cuerpo_del_cotejo(cabecera, filas):
    """EL TEXTO ENTERO DEL COTEJO, EN EL FORMATO UNICO. PURA.

    `filas` son tuplas `(puesto, clase_lector, clase_archivo, en_dudosos)`: el
    veredicto **no se le pasa, se computa**, para que no se pueda teclear uno que
    contradiga a sus dos clases."""
    completas = [(p, str(cl).upper(), str(ca).upper(), bool(du),
                  veredicto_de(cl, ca)) for p, cl, ca, du in filas]
    r = resumen(completas)
    L = [MARCA_FORMATO, "=" * 78]
    L.extend(cabecera)
    L.append("")
    L.append("%s: %d" % (LINEA_DENOMINADOR, r["total"]))
    L.append("CIFRA que COINCIDEN: %d" % r["coinciden"])
    L.append("CIFRA que DISCREPAN: %d" % r["discrepan"])
    L.append("CIFRA en los dudosos del lector: %d" % r["dudosos"])
    L.append("CIFRA discrepancias DENTRO de los dudosos: %d (%s)"
             % (len(r["disc_dentro"]),
                ", ".join(str(x) for x in r["disc_dentro"]) or "ninguna"))
    L.append("CIFRA discrepancias FUERA de los dudosos: %d (%s)"
             % (len(r["disc_fuera"]),
                ", ".join(str(x) for x in r["disc_fuera"]) or "ninguna"))
    L.append("REPARTO DEL LECTOR:  %s"
             % ", ".join("%s %d" % (k, r["reparto_lector"][k])
                         for k in sorted(r["reparto_lector"])))
    L.append("REPARTO DEL ARCHIVO: %s"
             % ", ".join("%s %d" % (k, r["reparto_archivo"][k])
                         for k in sorted(r["reparto_archivo"])))
    L.append("")
    L.append(ABRE_TABLA)
    L.append(CABECERA_TABLA)
    L.append("-" * 78)
    for p, cl, ca, du, ver in completas:
        L.append("%6d | %s | %s | %s | %s"
                 % (p, cl, ca, "si" if du else "no", ver))
    L.append(FIN_TABLA)
    L.append("")
    L.append("EL DENOMINADOR ES RECUPERABLE CONTANDO LAS FILAS DE ESTA TABLA, y la")
    L.append("cifra declarada arriba tiene que calzar con ese conteo. Lo comprueba")
    L.append("`denominador()` de scripts/loop/cotejo_de_ciega.py, y si no calzan el")
    L.append("fichero es ROJO.")
    return NL.join(L) + NL


def escribir_cotejo(ruta, cabecera, filas):
    """ESCRIBE EL COTEJO Y LO RELEE PARA COMPROBAR SU PROPIO FORMATO.

    Devuelve `(ok, informe)`. **NO da por bueno lo que acaba de escribir:** lo
    relee del disco y le corre su propia guarda del denominador."""
    texto = cuerpo_del_cotejo(cabecera, filas)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    releido = io.open(ruta, encoding="utf-8").read()
    ok, dec, cont, motivo = denominador(releido)
    inf = ["ESCRITO: %s" % os.path.relpath(ruta, RAIZ).replace(os.sep, "/"),
           "   disco %d bytes | LF %d bytes"
           % (os.path.getsize(ruta),
              len(releido.replace(chr(13) + NL, NL).encode("utf-8"))),
           "   RELEIDO DEL DISCO Y PASADO POR SU PROPIA GUARDA:",
           "      denominador declarado: %s | filas contadas: %d" % (dec, cont),
           "      %s -> %s" % (motivo, "VERDE" if ok else "ROJO")]
    return ok, inf


# ---------------------------------------------------------------- LA MUTACION
def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    w("   %-64s %s" % (nombre, "VERDE" if ok else "ROJO"))
    if not ok:
        w("      esperado: %r" % (esperado,))
        w("      obtenido: %r" % (obtenido,))
    return ok


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION: **CAE SI UN COTEJO NO PERMITE RECUPERAR EL
    DENOMINADOR.** No toca el repo: fabrica los textos."""
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DEL FORMATO UNICO DEL COTEJO DE CIEGA")
    w("=" * 78)
    w("")
    w("LO QUE SE PRUEBA: que `denominador()` CAE cuando el cotejo no permite")
    w("recuperar sobre cuantos pares se midio. Los textos se FABRICAN aqui, con")
    w("la cifra sabida por construccion, y el valor esperado NO es una constante")
    w("igual a la obtenida.")
    w("")

    bueno = cuerpo_del_cotejo(["cabecera de prueba"],
                              [(1, "A", "A", False), (2, "B", "D", True),
                               (3, "D", "D", False)])
    w("A) UN COTEJO BIEN FORMADO, CON TRES FILAS")
    ok &= _caso(w, "denominador() sale VERDE", denominador(bueno)[0], True)
    ok &= _caso(w, "declarado y contado son los dos 3", denominador(bueno)[1:3], (3, 3))
    ok &= _caso(w, "filas_del_cotejo() recupera las tres", len(filas_del_cotejo(bueno)), 3)
    ok &= _caso(w, "el veredicto se computa y no se teclea",
                [f[4] for f in filas_del_cotejo(bueno)],
                ["COINCIDE", "DISCREPA", "COINCIDE"])
    w("")

    w("B) LA MUTACION QUE EL ENCARGO PIDE: UN COTEJO QUE SOLO LISTA LAS")
    w("   DISCREPANCIAS. Es la forma de dos de los seis ficheros que hoy entran")
    w("   en la medicion, y por eso su denominador no se sabe.")
    solo_disc = NL.join([l for l in bueno.split(NL)
                         if "COINCIDE" not in l or l.startswith("CIFRA que")])
    ok &= _caso(w, "denominador() CAE sobre el cotejo mutilado",
                denominador(solo_disc)[0], False)
    ok &= _caso(w, "y dice que declarado (3) y contado (1) no calzan",
                denominador(solo_disc)[1:3], (3, 1))
    w("")

    w("C) LA MUTACION SIN LA LINEA DEL DENOMINADOR EN LA CABECERA")
    sin_dec = NL.join([l for l in bueno.split(NL)
                       if not l.startswith(LINEA_DENOMINADOR + ":")])
    ok &= _caso(w, "denominador() CAE sin la linea declarada",
                denominador(sin_dec)[0], False)
    ok &= _caso(w, "y el motivo nombra la linea que falta",
                LINEA_DENOMINADOR in denominador(sin_dec)[3], True)
    w("")

    w("D) LA MUTACION SIN LA MARCA DE FORMATO")
    sin_marca = bueno.replace(MARCA_FORMATO, "un cotejo cualquiera")
    ok &= _caso(w, "denominador() CAE sin la marca de formato",
                denominador(sin_marca)[0], False)
    w("")

    w("E) LA MUTACION CON LA TABLA VACIA")
    vacio = cuerpo_del_cotejo(["cabecera de prueba"], [])
    ok &= _caso(w, "denominador() CAE con cero filas", denominador(vacio)[0], False)
    w("")

    w("F) LA MUTACION QUE FALSEA EL DENOMINADOR DECLARADO")
    falseado = bueno.replace("%s: 3" % LINEA_DENOMINADOR,
                             "%s: 30" % LINEA_DENOMINADOR)
    ok &= _caso(w, "denominador() CAE si la cabecera miente",
                denominador(falseado)[0], False)
    ok &= _caso(w, "y publica las dos cifras, 30 declarada y 3 contada",
                denominador(falseado)[1:3], (30, 3))
    w("")

    w("G) `veredicto_de` NO NORMALIZA MAS QUE LA CAJA, PARA QUE UNA CLASE RARA")
    w("   SALGA A LA VISTA EN VEZ DE RESOLVERSE EN SILENCIO")
    ok &= _caso(w, "'a' contra 'A' COINCIDE", veredicto_de("a", "A"), "COINCIDE")
    ok &= _caso(w, "'A' contra 'D' DISCREPA", veredicto_de("A", "D"), "DISCREPA")
    ok &= _caso(w, "'AB' contra 'A' DISCREPA", veredicto_de("AB", "A"), "DISCREPA")
    w("")

    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(RAIZ, "docs", "loop",
                        "SALIDA_V192_T5_MUTACION_FORMATO_COTEJO.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V192_T5_MUTACION_FORMATO_COTEJO.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--leer", help="lee un cotejo y le corre la guarda del denominador")
    ap.add_argument("--mutacion", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if a.mutacion:
        return prueba_de_mutacion()
    if not a.leer:
        print("ROJO: hace falta --leer RUTA o --mutacion.")
        return 1
    texto = io.open(a.leer, encoding="utf-8", errors="replace").read()
    ok, dec, cont, motivo = denominador(texto)
    print("%s" % a.leer)
    print("   declarado: %s | contado: %d" % (dec, cont))
    print("   %s" % motivo)
    if ok:
        r = resumen(filas_del_cotejo(texto))
        for k in ("total", "coinciden", "discrepan", "dudosos"):
            print("   %-12s %d" % (k, r[k]))
        print("   discrepancias DENTRO de los dudosos: %s"
              % (", ".join(str(x) for x in r["disc_dentro"]) or "ninguna"))
        print("   discrepancias FUERA de los dudosos: %s"
              % (", ".join(str(x) for x in r["disc_fuera"]) or "ninguna"))
    print("   VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
