# -*- coding: utf-8 -*-
r"""_v199_t3_ejemplares_del_banco.py . LOS EJEMPLARES QUE EL BANCO NOMBRA,
COMPUTADOS DEL BANCO Y NO TECLEADOS, PARA EL CARRIL `--excluir` DE
`aislador_de_ciega.py`.

DE DONDE SALE: TAREA 3 del encargo de la vuelta 199, que es la `P.3` del reporte
de la 197 adjudicada por el auditor de la 198 **por extension de la `4.4` del acta
197**. El razonamiento, con sus palabras: *"el banco nombra sus ejemplares CON
PUESTO Y CLASE, y la doctrina que se manda citar ENTREGA LA RESPUESTA"*. Le paso al
ejecutor con el `1077` y al auditor con el `165`. **Un puesto cuya clase esta
escrita en la doctrina que la ciega obliga a citar NO ES UN PUESTO CIEGO.**

POR QUE NO ES MAQUINARIA NUEVA, Y SE DICE EN VEZ DE ESCONDERSE: la moratoria de
`AUDITOR.md` 6.3 prohibe fabricar arneses, guardas y lectores nuevos, y **la
TAREA 3 no esta entre sus dos excepciones**. Lo que la salva es que el encargo
manda que la lista se COMPUTE y no se teclee, y computar necesita codigo. Se hace
con el minimo posible: **prefijo `_` para que el censo de arneses no lo cuente**,
**NO entra en la nomina** (congelada en 135), no vigila a nadie y no se cita como
guarda. **Va MARCADO COMO DISCUTIBLE en el reporte**: si el fundador lo lee como
maquinaria, se retira y la lista se queda como fichero muerto con su fecha de
corte.

LA REGLA DE EXTRACCION, ESCRITA ENTERA PORQUE ES LO UNICO QUE SE PUEDE AUDITAR:

  . se busca un MARCADOR: `puesto`, `puestos`, `par` o `pares`;
  . detras del marcador se consume una LISTA de numeros unidos por `,`, `y` o `a`;
  . `a` entre dos numeros se lee como RANGO cerrado (el banco escribe
    *"Los puestos 2.389 a 2.412"*), y un rango de mas de `TOPE_RANGO` se declara y
    NO se expande, para que una errata no se lleve media cola;
  . los millares con punto se normalizan (`2.117` es `2117`), que es como el banco
    los escribe;
  . un numero que NO exista en el archivo se DECLARA y no entra, porque
    `--excluir` cae en rojo con un puesto inexistente y porque una cifra que no se
    puede resolver no se publica.

LO QUE LA REGLA **NO** HACE, y va escrito para que se pueda discutir: no coge
numeros sueltos sin marcador (un `9.21` de doctrina o un conteo de bytes NO es un
puesto), y no coge el numero que va DELANTE del marcador (*"tres pares"*,
*"los 240 pares"*), porque ahi el numero es un conteo y no un puesto.

EL CONTROL, Y ES LO QUE IMPIDE QUE ESTO SE APRUEBE SOLO: el acta 198 nombra DOS
ejemplares concretos, el `1077` y el `165`. **Si el computo no los encuentra, este
fichero sale ROJO y no escribe la lista.** No es un `assert` contra si mismo: los
dos numeros salen del acta y el computo sale del banco.

SALIDAS:
  docs/loop/_v199_ejemplares_del_banco_exclusion.txt   enteros sueltos, uno por
      linea, SIN cabecera: es el formato que `numeros_de()` lee y una cabecera con
      fechas o `sha256` dentro le meteria enteros que no son puestos.
  docs/loop/SALIDA_V199_T3_EJEMPLARES_DEL_BANCO.txt    la procedencia de cada
      puesto con su linea del banco, la fecha de corte y el `sha256` del banco.

USO:
  python scripts/loop/_v199_t3_ejemplares_del_banco.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
AQUI = os.path.dirname(os.path.abspath(__file__))
NL = chr(10)
BANCO = os.path.join(RAIZ, "docs", "BANCO_DE_TEXTOS.md")
EXCLUSION = os.path.join(LOOP, "_v199_ejemplares_del_banco_exclusion.txt")
SELLADA = os.path.join(LOOP, "SALIDA_V199_T3_EJEMPLARES_DEL_BANCO.txt")

# LOS DOS QUE EL ACTA 198 NOMBRA. Son el CONTROL del computo, no su fuente.
CONTROL = (1077, 165)

# UN RANGO MAS LARGO QUE ESTO SE DECLARA Y NO SE EXPANDE.
TOPE_RANGO = 60

# EL MARCADOR, Y LA ERRATA QUE EL CONTROL DEL ACTA 198 CAZO, DECLARADA SIN TAPAR
# LO QUE CORRIGE. La primera version escribia `pares?`, que en una expresion
# regular NO es *"par u pares"*: es `par` + `e` + `s` opcional, o sea **exige la
# `e`**. Con eso `puesto` y `puestos` entraban pero `par` A SECAS no, y el `165`
# del auditor, que el banco escribe como *"La nota del par 165"*, se quedaba
# fuera. **El caso de control salio ROJO y por eso se vio**: si el control no
# hubiera estado, la lista se habria publicado corta y con cara de completa.
MARCADOR = re.compile(r"\b(puestos?|par(?:es)?)\b", re.IGNORECASE)
# UN NUMERO TAL COMO EL BANCO LO ESCRIBE: con o sin millares por punto, y con o
# sin el `**` de negrita o las comillas de codigo alrededor.
NUMERO = re.compile(r"[*`]*(\d{1,3}(?:\.\d{3})+|\d+)[*`]*")
UNION = re.compile(r"^[\s,]*(?:y|e|a)?[\s,]*$", re.IGNORECASE)


def normalizar(cadena):
    """`2.117` -> 2117. PURA."""
    return int(cadena.replace(".", ""))


def numeros_tras(texto, inicio):
    """LA LISTA DE NUMEROS QUE SIGUE A UN MARCADOR, y como venian unidos.
    Devuelve una lista de (numero, union_con_el_anterior). PURA sobre el texto.

    Se consume mientras entre un numero y el siguiente SOLO haya separadores de
    lista (`,`, `y`, `e`, `a`) y espacios. En cuanto aparece cualquier otra
    palabra, la enumeracion se acaba: es lo que impide que
    *"puestos 300, 487 y 544, y los tres salieron A"* se coma la `A`, y lo que
    impide que un numero de otra frase entre por vecindad."""
    salida = []
    pos = inicio
    union = ""
    while True:
        m = NUMERO.search(texto, pos)
        if not m:
            break
        entre = texto[pos:m.start()]
        if salida and not UNION.match(entre):
            break
        if not salida and entre.strip() not in ("", ":"):
            break
        u = entre.strip(" ,").lower() if salida else ""
        salida.append((normalizar(m.group(1)), u))
        pos = m.end()
        union = u
    return salida, union


def cosechar(texto):
    """TODOS LOS PUESTOS QUE EL BANCO NOMBRA, con la linea de donde salen.
    Devuelve (dict puesto -> lista de lineas, lista de rangos declarados).
    PURA sobre el texto."""
    lineas = texto.split(NL)
    hallados, rangos = {}, []
    for i, linea in enumerate(lineas, start=1):
        # LA ENUMERACION SE MIRA SOBRE LA LINEA **Y LA SIGUIENTE**, y eso lo
        # enseño una medicion, no una precaucion: el banco escribe en su linea
        # 2327 *"Los puestos 2.389 a"* y **el `2.412` cae en la linea de abajo**.
        # Mirando linea a linea se cosechaba el `2.389` y se perdian los otros
        # 23 del rango, o sea **una lista corta con cara de completa**.
        # Unir con un espacio NO afloja nada, porque el que decide sigue siendo
        # `numeros_tras()`: entre dos numeros solo puede haber separadores de
        # lista, asi que un numero de la linea de abajo entra UNICAMENTE si la de
        # arriba quedo colgando. Un punto o cualquier palabra corta la union.
        # Y A LA LINEA DE ABAJO SE LE QUITA SU MARCA DE CITA. Tambien medido: la
        # continuacion del rango de la linea 2327 empieza por `> `, porque el
        # banco lo escribe dentro de una cita, y con el `>` delante la union
        # `a` se rompia y el rango seguia sin verse. Se quita SOLO la marca de
        # cita y los espacios: cualquier otra cosa sigue cortando la union.
        vecina = re.sub(r"^[\s>]+", "", lineas[i]) if i < len(lineas) else ""
        alcance = linea + " " + vecina
        for m in MARCADOR.finditer(linea):
            nums, _u = numeros_tras(alcance, m.end())
            anterior = None
            for numero, union in nums:
                if union == "a" and anterior is not None and numero > anterior:
                    span = numero - anterior
                    if span > TOPE_RANGO:
                        rangos.append((i, anterior, numero, span, False))
                    else:
                        rangos.append((i, anterior, numero, span, True))
                        for k in range(anterior + 1, numero):
                            hallados.setdefault(k, []).append(i)
                hallados.setdefault(numero, []).append(i)
                anterior = numero
    return hallados, rangos


def puestos_del_archivo():
    """LOS `puesto_intra` QUE EL ARCHIVO TIENE HOY, leidos del propio aislador y
    no de una copia. Devuelve un conjunto."""
    sys.path.insert(0, AQUI)
    import aislador_de_ciega as AIS   # noqa: E402
    return set(f.get("puesto_intra") for f in AIS.cargar_filas())


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L, casos, verdes = [], 0, 0
    w = L.append

    def caso(titulo, ok, detalle=""):
        nonlocal casos, verdes
        casos += 1
        if ok:
            verdes += 1
        w("   %-62s %s" % (titulo[:62], "VERDE" if ok else "ROJO"))
        if detalle:
            w("      %s" % detalle)

    datos = io.open(BANCO, "rb").read()
    texto = datos.decode("utf-8", errors="replace").replace(chr(13) + NL, NL)
    corte = subprocess.run(["git", "log", "-1", "--format=%ad", "--date=short"],
                           cwd=RAIZ, capture_output=True)
    corte = corte.stdout.decode("utf-8", errors="replace").strip()

    w("=" * 78)
    w("VUELTA 199, TAREA 3: LOS EJEMPLARES DEL BANCO, COMPUTADOS DEL BANCO.")
    w("=" * 78)
    w("")
    w("EL BANCO, MEDIDO HOY:")
    w("   docs/BANCO_DE_TEXTOS.md")
    w("   %d bytes en disco | %d bytes LF | sha256 LF %s"
      % (len(datos), len(datos.replace(chr(13).encode() + b"\n", b"\n")),
         hashlib.sha256(texto.encode("utf-8")).hexdigest()[:16]))
    w("   CIFRA lineas por split(NL): %d" % len(texto.split(NL)))
    w("   FECHA DE CORTE (banco 9.21), leida de git: %s" % (corte or "(no legible)"))
    w("")

    hallados, rangos = cosechar(texto)
    w("EL COMPUTO, CON SU REGLA DELANTE Y NO DESPUES:")
    w("   marcadores: puesto, puestos, par, pares")
    w("   uniones que continuan la lista: coma, `y`, `e`, `a`")
    w("   `a` entre dos numeros se lee como RANGO cerrado")
    w("   tope de rango que se expande: %d" % TOPE_RANGO)
    w("   CIFRA puestos distintos cosechados del banco: %d" % len(hallados))
    w("")
    w("LOS RANGOS QUE EL BANCO ESCRIBE, DECLARADOS UNO A UNO:")
    if not rangos:
        w("   (ninguno)")
    for linea, a, b, span, expandido in rangos:
        w("   linea %5d: %d a %d (%d puestos) -> %s"
          % (linea, a, b, span + 1,
             "EXPANDIDO" if expandido else "NO EXPANDIDO, pasa del tope"))
    w("")

    del_archivo = puestos_del_archivo()
    w("EL ARCHIVO, CONTADO DEL PROPIO aislador_de_ciega.py Y NO DE UNA COPIA:")
    w("   CIFRA filas del archivo: %d" % len(del_archivo))
    if del_archivo:
        w("   rango de puestos: %d a %d" % (min(del_archivo), max(del_archivo)))
    w("")

    dentro = sorted(p for p in hallados if p in del_archivo)
    fuera = sorted(p for p in hallados if p not in del_archivo)
    w("LO QUE NO EXISTE EN EL ARCHIVO SE DECLARA Y NO ENTRA:")
    w("   CIFRA numeros cosechados que NO son puestos del archivo: %d" % len(fuera))
    for p in fuera:
        w("      FUERA DEL ARCHIVO: %-6d nombrado en la(s) linea(s) %s"
          % (p, ", ".join(str(x) for x in hallados[p][:6])))
    w("")

    w("EL CONTROL DEL ACTA 198, Y ES LO QUE IMPIDE QUE ESTO SE APRUEBE SOLO:")
    for p in CONTROL:
        esta = p in hallados
        caso("el %d, que el acta 198 nombra, sale del computo" % p, esta,
             "linea(s) del banco donde se nombra: %s"
             % (", ".join(str(x) for x in hallados.get(p, [])) or "(ninguna)"))
    caso("los dos del control existen ademas en el archivo",
         all(p in del_archivo for p in CONTROL))
    w("")

    w("LA LISTA, ENTERA Y CON SU PROCEDENCIA. Cada puesto con la linea del banco")
    w("que lo nombra: LA CIFRA NO VIAJA SOLA.")
    for p in dentro:
        w("   %-6d linea(s) del banco: %s"
          % (p, ", ".join(str(x) for x in hallados[p][:8])))
    w("")
    w("CIFRA PUESTOS QUE SALEN DEL UNIVERSO DE LAS CIEGAS: %d" % len(dentro))
    if del_archivo:
        w("CIFRA universo que queda: %d de %d (%.1f por ciento fuera)"
          % (len(del_archivo) - len(dentro), len(del_archivo),
             100.0 * len(dentro) / len(del_archivo)))
    w("")

    caso("la lista no esta vacia", len(dentro) > 0)
    caso("la lista no se come mas de la mitad del archivo",
         len(dentro) * 2 < len(del_archivo),
         "%d de %d" % (len(dentro), len(del_archivo)))

    if verdes == casos:
        io.open(EXCLUSION, "w", encoding="utf-8", newline=NL).write(
            NL.join(str(p) for p in dentro) + NL)
        w("ESCRITA LA LISTA: %s" % os.path.relpath(EXCLUSION, RAIZ).replace(os.sep, "/"))
        w("   SIN CABECERA A PROPOSITO: `numeros_de()` lee enteros sueltos, y una")
        w("   cabecera con la fecha o el `sha256` dentro le meteria enteros que no")
        w("   son puestos. La procedencia vive en ESTE fichero.")
        w("   %d lineas, %d bytes"
          % (len(dentro), os.path.getsize(EXCLUSION)))
    else:
        w("NO SE ESCRIBE LA LISTA: el control no paso.")
    w("")
    w("=" * 78)
    w("CASOS: %d | VERDES: %d | ROJOS: %d" % (casos, verdes, casos - verdes))
    w("VEREDICTO: %s" % ("VERDE" if verdes == casos else "ROJO"))
    w("=" * 78)

    t = NL.join(L) + NL
    io.open(SELLADA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (SELLADA, len(t.encode("utf-8"))))
    return 0 if verdes == casos else 1


if __name__ == "__main__":
    sys.exit(main())
