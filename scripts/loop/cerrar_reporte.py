# -*- coding: utf-8 -*-
r"""cerrar_reporte.py . EL CIERRE DEL REPORTE DEJA DE SER UN PASO A MANO.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como sus hermanos
`paso0_archivar_anterior.py`, `tallar_cabecera_reporte.py`,
`archivar_reporte.py`, `serie_de_registros.py`, `aislador_de_ciega.py` y
`anexar_tarea_al_reporte.py`: se invoca al cierre de cada vuelta y NO se clona,
para que el proximo clon no lo pierda.

POR QUE NACE (adjudicacion 6.6 del acta del auditor de la vuelta 171, y la causa
esta MEDIDA, no supuesta). Las vueltas 170 y 171 murieron las dos en el mismo
tramo: su bloque de cierre corrio entero, su tallador salio VERDE, y
`docs/loop/REPORTE.md` se quedo diciendo "SIN ESCRIBIR TODAVIA" y "PENDIENTE DE
TALLAR AL CIERRE". La causa no fue prisa: `vuelta171_cierre.py` **SOLO MIDE**,
escribe once ficheros `SALIDA_*` y **no toca `REPORTE.md` en ninguna linea**.
Cerrar el reporte era un paso a mano que venia despues, y ahi cayeron las dos.

QUE HACE, EN UN SOLO ACTO (es lo que `vuelta171_tarea1b_cerrar_reporte_170.py`
ya sabia hacer, con nombre estable y parametrizado):

  1. PEGA LA CABECERA leyendola del fichero del tallador. NINGUNA CELDA SE
     TECLEA (`EJECUTOR.md` 1, "LA CABECERA DEL REPORTE SE TALLA, NO SE TECLEA").
  2. ANEXA EL CUERPO DEL CIERRE (las secciones 3 a 8) tal como esta en su
     borrador, comprobando por sha256 que lo que anexa es byte a byte lo que el
     borrador dice.
  3. ESCRIBE LA SECCION 9 con LA SALIDA DE LA BATERIA ENTERA DENTRO.
  4. ESCRIBE EL VEREDICTO DE UNA LINEA en el sitio del "SIN ESCRIBIR TODAVIA".
  5. RELEE DEL DISCO lo que acaba de escribir.

Y CAE EN ROJO SI AL TERMINAR FALTA CUALQUIERA DE LAS CUATRO PIEZAS:

  (1) EL VEREDICTO ESCRITO      . el "SIN ESCRIBIR TODAVIA" ya no esta y hay un
                                  veredicto de una linea en su sitio.
  (2) LA CABECERA PEGADA        . todas las filas de tabla del fichero del
                                  tallador estan dentro del reporte, byte a
                                  byte, y el hueco "PENDIENTE DE TALLAR" ya no
                                  esta.
  (3) LAS SECCIONES 3 A 9       . las siete existen.
  (4) LA BATERIA DENTRO DE LA 9 . la salida de la bateria de ESTA vuelta esta
                                  dentro de la seccion 9 y no vacia, **O** un
                                  HUECO DECLARADO Y MEDIDO en su sitio.

LA PIEZA (4) ADMITE EL HUECO DECLARADO Y MEDIDO (vuelta 173, TAREA 1.b;
adjudicacion 6.2 del acta del auditor de la vuelta 172). POR QUE CAMBIA, Y NO ES
DOCTRINA NUEVA SINO UN CHOQUE ENTRE DOS REGLAS ESCRITAS: chocan la 6.6 del acta
171, que exige *"la salida de la bateria dentro de la 9"*, y la regla de la casa
que el reporte de la 171 aplico al pie de la letra, *"el hueco se declara y no se
rellena"*, que sale de `EJECUTOR.md` 1 y del carril `9.10`. Tal como estaba, este
instrumento **solo podia cerrar los reportes que no lo necesitaban** y no podia
cerrar ninguno de los tres que habian fallado, que es exactamente para lo que
nacio.

LA LETRA ES ESTRECHA A PROPOSITO, y es la del acta:

  . la (4) se satisface con LA SALIDA DE LA BATERIA DENTRO DE LA SECCION 9,
    COMO HASTA AHORA;
  . O con un HUECO DECLARADO que traiga LAS TRES COSAS JUNTAS: el NOMBRE DEL
    FICHERO, sus BYTES MEDIDOS EN LA CORRIDA, y la ATRIBUCION de quien si la
    corrio o la declaracion de que no la corrio nadie;
  . LA AUSENCIA MUDA NO LA SATISFACE: una seccion 9 que se calla no es un hueco
    declarado, es un hueco escondido;
  . UNA CORRIDA DE OTRA VUELTA PEGADA AHI TAMPOCO: ni como bateria (se mira el
    numero de vuelta del fichero que se pega) ni dentro del hueco (se mira el
    numero de vuelta de todo `SALIDA_V<N>_BATERIA` que la seccion 9 nombre).

LAS CUATRO SE COMPRUEBAN CON `piezas_que_faltan()`, que es PURA y recibe el
texto: asi su caso positivo por mutacion puede tumbarla una a una sin tocar el
repo ni escribir nada. Su arnes es
`scripts/loop/vuelta172_tarea5_mutacion_cierre.py`, cuyos 17 casos SIGUEN VERDES
y no se tocan (condicion expresa de la 6.2), y la conducta nueva se prueba en un
arnes NUEVO, `scripts/loop/vuelta173_tarea1b_mutacion_hueco.py`. Los dos
parametros nuevos de `piezas_que_faltan()` son OPCIONALES justamente para que los
17 casos viejos, que la llaman con tres argumentos, sigan llamandola igual.

LO QUE NO HACE: no talla la cabecera (eso es de `tallar_cabecera_reporte.py`), no
archiva (eso es de `archivar_reporte.py`), no corre la bateria y NO ANEXA TAREAS
(eso es de `anexar_tarea_al_reporte.py`). Recibe lo que otros produjeron y lo
monta, y si algo falta lo dice en rojo en vez de escribir un reporte a medias.

USO:
  python scripts/loop/cerrar_reporte.py --vuelta 172 \
      --cuerpo scripts/loop/_v172_cierre_texto.md \
      --tallador docs/loop/SALIDA_V172_TALLADOR_CABECERA.txt \
      --bateria docs/loop/SALIDA_V172_BATERIA.txt \
      --veredicto "LA VUELTA 172 ..."

  Y cuando la bateria de esa vuelta NO CORRIO, con la atribucion delante, que es
  lo unico que convierte una ausencia muda en un hueco declarado:

  python scripts/loop/cerrar_reporte.py --vuelta 172 ... \
      --hueco-atribucion "NADIE la corrio: ni el ejecutor ni el auditor."
"""
import argparse
import hashlib
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")

MARCA_ABRE = "<!-- CABECERA TALLADA -->"
MARCA_CIERRA = "<!-- FIN CABECERA TALLADA -->"
VEREDICTO_VIEJO = "**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**"
HUECO_CABECERA = "PENDIENTE DE TALLAR AL CIERRE"
CAB_9 = "## 9. LA BATERIA DE MUTACIONES, CORRIDA ENTERA Y SOLA AL CIERRE"
CAB_9_HUECO = "## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO"

# LAS TRES MARCAS DEL HUECO DECLARADO. Son literales y no expresiones sueltas
# justamente para que un hueco no se pueda declarar "por parecido": o trae la
# marca, o no hay hueco declarado y la ausencia sigue siendo muda.
MARCA_HUECO = "HUECO DECLARADO Y MEDIDO"
MARCA_ATRIBUCION = "ATRIBUCION:"
PATRON_FICHERO_BATERIA = re.compile(r"SALIDA_V(\d+)_BATERIA")
PATRON_BYTES = re.compile(r"(\d[\d.]*)\s+bytes")


def sha(t):
    return hashlib.sha256(t.replace(chr(13) + NL, NL).encode("utf-8")).hexdigest()


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def rel(ruta):
    return os.path.relpath(ruta, RAIZ).replace(os.sep, "/")


def vuelta_de_fichero(nombre):
    """El numero de vuelta que lleva dentro un `SALIDA_V<N>_BATERIA...`, o None
    si el nombre no dice de que vuelta es. PURA."""
    if not nombre:
        return None
    m = PATRON_FICHERO_BATERIA.search(nombre)
    return int(m.group(1)) if m else None


def hueco_declarado_que_falta(seccion9, vuelta):
    """LO QUE LE FALTA A UN HUECO PARA ESTAR DECLARADO Y MEDIDO. Devuelve la
    lista de motivos, VACIA si el hueco esta completo.

    LAS TRES COSAS TIENEN QUE VENIR JUNTAS (adjudicacion 6.2 del acta 172): el
    NOMBRE DEL FICHERO, sus BYTES MEDIDOS y la ATRIBUCION. Traer dos de tres no
    es un hueco declarado a medias: es un hueco que no cuenta.

    PURA a proposito, como su hermana `piezas_que_faltan()`: recibe el texto de
    la seccion 9 y el numero de vuelta, y no lee ni escribe nada. Asi su caso
    positivo por mutacion la puede tumbar motivo a motivo sin tocar el repo."""
    if vuelta is None:
        return ["no se dijo de que vuelta es este reporte, y sin eso un hueco no "
                "se puede juzgar"]
    if MARCA_HUECO not in seccion9:
        return ["LA AUSENCIA ES MUDA: la seccion 9 no declara ningun hueco (no "
                "trae la marca %r)" % MARCA_HUECO]
    motivos = []

    nombrados = sorted(set(int(n) for n in PATRON_FICHERO_BATERIA.findall(seccion9)))
    if not nombrados:
        motivos.append("el hueco no nombra el fichero de la bateria")
    elif vuelta not in nombrados:
        motivos.append("el hueco no nombra la bateria de la vuelta %d" % vuelta)
    ajenas = [n for n in nombrados if n != vuelta]
    if ajenas:
        motivos.append("la seccion 9 trae la bateria de la vuelta %s, que es UNA "
                       "CORRIDA DE OTRA VUELTA"
                       % ", ".join(str(n) for n in ajenas))

    if not PATRON_BYTES.search(seccion9):
        motivos.append("el hueco no trae sus bytes medidos")

    atribucion = ""
    if MARCA_ATRIBUCION in seccion9:
        atribucion = seccion9.split(MARCA_ATRIBUCION, 1)[1].split(NL, 1)[0].strip()
    if not atribucion:
        motivos.append("el hueco no trae atribucion de quien si la corrio ni "
                       "declaracion de que no la corrio nadie")
    return motivos


def piezas_que_faltan(texto, filas_tallador, lineas_bateria,
                      vuelta=None, nombre_bateria=None):
    """LAS CUATRO PIEZAS, COMPROBADAS SOBRE EL TEXTO YA ESCRITO. Devuelve la
    lista de las que FALTAN, vacia si estan las cuatro.

    PURA A PROPOSITO: recibe el texto del reporte, las filas de la cabecera
    tallada y las lineas no vacias de la salida de la bateria, para que su caso
    positivo por mutacion pueda tumbarla una a una **sin tocar el repo y sin
    escribir nada**. Si esto viviera dentro del cuerpo de una funcion que
    escribe, no habria nada que un arnes pudiera llamar, y una guarda que no se
    puede llamar no se puede probar."""
    faltan = []

    # (1) EL VEREDICTO ESCRITO
    if (VEREDICTO_VIEJO in texto
            or "**EL VEREDICTO DE UNA LINEA:" not in texto):
        faltan.append("(1) el veredicto de una linea no esta escrito")

    # (2) LA CABECERA PEGADA
    if HUECO_CABECERA in texto:
        faltan.append("(2) el hueco de la cabecera sigue sin rellenar")
    elif not filas_tallador:
        faltan.append("(2) el fichero del tallador no trae ninguna fila de tabla")
    else:
        fuera = [f for f in filas_tallador if f.rstrip() not in texto]
        if fuera:
            faltan.append("(2) %d fila(s) de la cabecera tallada no estan pegadas"
                          % len(fuera))

    # (3) LAS SECCIONES 3 A 9
    ausentes = [k for k in range(3, 10) if (NL + "## %d." % k) not in texto]
    if ausentes:
        faltan.append("(3) faltan las secciones %s"
                      % ", ".join(str(k) for k in ausentes))

    # (4) LA BATERIA DENTRO DE LA SECCION 9, O EL HUECO DECLARADO Y MEDIDO
    if (NL + "## 9.") not in texto:
        faltan.append("(4) no hay seccion 9 donde meter la bateria")
    else:
        seccion9 = texto[texto.index(NL + "## 9."):]
        if lineas_bateria:
            fuera = [l for l in lineas_bateria if l.rstrip() not in seccion9]
            if fuera:
                faltan.append("(4) %d linea(s) de la bateria no estan dentro de la "
                              "seccion 9" % len(fuera))
            else:
                ajena = vuelta_de_fichero(nombre_bateria)
                if vuelta is not None and ajena is not None and ajena != vuelta:
                    faltan.append("(4) la salida pegada en la seccion 9 es la de la "
                                  "vuelta %d y no la de la %d: UNA CORRIDA DE OTRA "
                                  "VUELTA NO SATISFACE ESTA PIEZA" % (ajena, vuelta))
        else:
            motivos = hueco_declarado_que_falta(seccion9, vuelta)
            if motivos:
                faltan.append("(4) la bateria no esta y el hueco no vale: %s"
                              % "; ".join(motivos))
    return faltan


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, required=True)
    ap.add_argument("--cuerpo", required=True)
    ap.add_argument("--tallador", required=True)
    ap.add_argument("--bateria", required=True)
    ap.add_argument("--veredicto", required=True)
    ap.add_argument("--hueco-atribucion", dest="hueco_atribucion", default="",
                    help="LA ATRIBUCION DEL HUECO. Solo se usa cuando la salida "
                         "de la bateria de ESTA vuelta esta vacia o no existe. "
                         "Sin ella, una bateria vacia sigue siendo ROJO: la "
                         "ausencia muda no cierra ningun reporte.")
    a = ap.parse_args()
    V = a.vuelta

    print("=" * 78)
    print("SE CIERRA EL REPORTE DE LA VUELTA %d, EN UN SOLO ACTO" % V)
    print("=" * 78)
    print("")
    rojos = []

    print("A) EL SUJETO, COMPROBADO ANTES DE TOCARLO")
    texto = leer(REPORTE)
    primera = texto.split(NL, 1)[0]
    print("   %s primera linea: %s" % (rel(REPORTE), primera[:88]))
    m = re.match(r"^#\s*REPORTE DE LA VUELTA\s+(\d+)\b", primera)
    if not m or int(m.group(1)) != V:
        rojos.append("el REPORTE.md del arbol no es el de la vuelta %d" % V)
    print("   CIFRA bytes: %d | saltos de linea: %d"
          % (len(texto.encode("utf-8")), texto.count(NL)))
    for marca, esperado in ((VEREDICTO_VIEJO, True), (HUECO_CABECERA, True),
                            (NL + "## 3.", False), (NL + "## 9.", False)):
        hay = marca in texto
        print("   contiene %-36r -> %s (se esperaba %s)"
              % (marca[:34], "SI" if hay else "NO", "SI" if esperado else "NO"))
        if hay != esperado:
            rojos.append("el sujeto no esta en el estado de un reporte SIN CERRAR: %r"
                         % marca[:36])
    print("")

    print("B) LAS TRES PIEZAS QUE VIENEN DE FUERA, MEDIDAS ANTES DE PEGARLAS")
    tallador = leer(os.path.join(RAIZ, a.tallador.replace("/", os.sep)))
    filas = [l.rstrip() for l in tallador.split(NL) if l.strip().startswith("|")]
    print("   %-52s %7d bytes, %d filas de tabla"
          % (a.tallador, len(tallador.encode("utf-8")), len(filas)))
    if len(filas) < 8:
        rojos.append("el fichero del tallador trae %d filas de tabla, muy pocas" % len(filas))

    cuerpo = leer(os.path.join(RAIZ, a.cuerpo.replace("/", os.sep)))
    print("   %-52s %7d bytes, sha256 %s"
          % (a.cuerpo, len(cuerpo.encode("utf-8")), sha(cuerpo)[:16]))
    secciones = [l for l in cuerpo.split(NL) if l.startswith("## ")]
    for l in secciones:
        print("      %s" % l[:92])
    if not cuerpo.startswith("## 3."):
        rojos.append("el borrador del cierre no empieza por la seccion 3")

    ruta_bat = os.path.join(RAIZ, a.bateria.replace("/", os.sep))
    existe = os.path.exists(ruta_bat)
    tam = os.path.getsize(ruta_bat) if existe else -1
    print("   %-52s %s" % (a.bateria, ("%d bytes" % tam) if existe else "NO EXISTE"))
    bateria = leer(ruta_bat) if existe and tam > 0 else ""
    lineas_bat = [l for l in bateria.split(NL) if l.strip()]
    print("   CIFRA lineas no vacias de la bateria: %d" % len(lineas_bat))
    ajena = vuelta_de_fichero(a.bateria)
    print("   vuelta que lleva dentro el nombre del fichero: %s" % ajena)
    if ajena is not None and ajena != V:
        rojos.append("el fichero de bateria que se pasa es el de la vuelta %d y se "
                     "esta cerrando la %d. UNA CORRIDA DE OTRA VUELTA NO CIERRA "
                     "ESTE REPORTE." % (ajena, V))
    atribucion = a.hueco_atribucion.strip()
    if not lineas_bat:
        print("   LA BATERIA DE ESTA VUELTA NO CORRIO. Se mira la atribucion:")
        print("   --hueco-atribucion: %s"
              % (repr(atribucion) if atribucion else "(vacia)"))
        if not atribucion:
            rojos.append("la salida de la bateria de la vuelta %d esta vacia o no "
                         "existe y NO SE DECLARO NINGUNA ATRIBUCION. La ausencia "
                         "muda no cierra un reporte: o va la bateria, o va un "
                         "HUECO DECLARADO Y MEDIDO con --hueco-atribucion." % V)
    print("")

    if rojos:
        print("ROJO, %d motivo(s), y NO se escribe nada:" % len(rojos))
        for r in rojos:
            print("   " + r)
        return 1

    print("C) SE ESCRIBE")
    bloque_cabecera = (
        MARCA_ABRE + NL +
        "**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio" + NL +
        "de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta %d`, y su salida" % V + NL +
        "cruda vive en `%s` (%d bytes, %d filas de tabla," % (a.tallador,
                                                             len(tallador.encode("utf-8")),
                                                             len(filas)) + NL +
        "contadas por `scripts/loop/cerrar_reporte.py`). **LA CELDA QUE NO SALGA DE UN" + NL +
        "INSTRUMENTO NO SE ESCRIBE.**" + NL + NL +
        NL.join(filas) + NL + NL +
        MARCA_CIERRA + NL)
    i0 = texto.index(MARCA_ABRE)
    i1 = texto.index(MARCA_CIERRA) + len(MARCA_CIERRA) + 1
    texto = texto[:i0] + bloque_cabecera + texto[i1:]
    print("   cabecera: %d bytes de hueco -> %d bytes de tabla pegada"
          % (i1 - i0, len(bloque_cabecera.encode("utf-8"))))

    veredicto = "**EL VEREDICTO DE UNA LINEA: %s**" % a.veredicto.strip()
    i = texto.index(VEREDICTO_VIEJO)
    j = texto.index(NL + NL, i)
    texto = texto[:i] + veredicto + texto[j + 1:]
    print("   veredicto escrito: %d bytes" % len(veredicto.encode("utf-8")))

    if lineas_bat:
        seccion9 = (
            CAB_9 + NL + NL +
            "**CORRIDA ENTERA Y SOLA, Y SU SALIDA VA AQUI COMPLETA Y SIN RECORTAR.**" + NL +
            "Fichero: `%s` (**%d bytes, %d lineas no vacias**, contadas" % (a.bateria, tam,
                                                                           len(lineas_bat)) + NL +
            "por `scripts/loop/cerrar_reporte.py`). **Este instrumento CAE EN ROJO si esta" + NL +
            "seccion se queda sin ella**, que es la cuarta de sus cuatro piezas." + NL + NL +
            "```" + NL + bateria.rstrip(NL) + NL + "```" + NL)
    else:
        # EL HUECO SE DECLARA Y NO SE RELLENA. Las tres cosas van juntas, y las
        # dos primeras SE MIDEN AQUI con os.path.getsize: ninguna se teclea.
        seccion9 = (
            CAB_9_HUECO + NL + NL +
            "**%s. LA BATERIA DE LA VUELTA %d NO CORRIO, Y EL HUECO SE DECLARA EN VEZ"
            % (MARCA_HUECO, V) + NL +
            "DE RELLENARSE CON OTRA COSA.**" + NL + NL +
            "**EL NOMBRE DEL FICHERO:** `%s`." % a.bateria + NL +
            "**SUS BYTES, MEDIDOS EN ESTA CORRIDA** con `os.path.getsize` por" + NL +
            "`scripts/loop/cerrar_reporte.py`, no tecleados: **%d bytes**." % max(tam, 0) + NL + NL +
            "%s %s" % (MARCA_ATRIBUCION, atribucion) + NL + NL +
            "**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este" + NL +
            "instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b" + NL +
            "(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es" + NL +
            "estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**." + NL +
            "Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y" + NL +
            "**una corrida de otra vuelta pegada aqui tampoco vale**." + NL)

    texto = texto.rstrip(NL) + NL + NL + cuerpo.rstrip(NL) + NL + NL + seccion9
    io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(texto)
    print("   ESCRITO: %s (%d bytes, %d saltos de linea)"
          % (rel(REPORTE), len(texto.encode("utf-8")), texto.count(NL)))
    print("")

    print("D) SE RELEE DEL DISCO Y SE MIRAN LAS CUATRO PIEZAS")
    de_nuevo = leer(REPORTE)
    faltan = piezas_que_faltan(de_nuevo, filas, lineas_bat,
                               vuelta=V, nombre_bateria=a.bateria)
    for etiqueta in ("(1) veredicto escrito", "(2) cabecera pegada",
                     "(3) secciones 3 a 9",
                     "(4) bateria dentro de la 9 o hueco declarado"):
        codigo = etiqueta[:3]
        mal = [f for f in faltan if f.startswith(codigo)]
        print("   %-34s %s" % (etiqueta, "SI" if not mal else "NO: " + mal[0]))
    print("   CIFRA piezas que faltan: %d" % len(faltan))
    extra = 0
    for etiqueta, cond in (
            ("el cuerpo del cierre esta byte a byte", cuerpo.rstrip(NL) in de_nuevo),
            ("cero guiones largos y cero guiones medios",
             chr(8212) not in de_nuevo and chr(8211) not in de_nuevo)):
        print("   %-34s %s" % (etiqueta, "SI" if cond else "NO"))
        if not cond:
            extra += 1
    print("")
    if faltan or extra:
        print("ROJO: al reporte de la vuelta %d le faltan %d de sus cuatro piezas."
              % (V, len(faltan)))
        for f in faltan:
            print("   " + f)
        return 1
    print("VERDE: el reporte de la vuelta %d queda cerrado, con sus cuatro piezas." % V)
    print("   LA SEGUNDA COMPROBACION (leer de git lo que se acaba de commitear)")
    print("   NO la hace este fichero: va DESPUES del commit, con git show.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
