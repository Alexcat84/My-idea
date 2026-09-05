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
                                  dentro de la seccion 9, y no vacia.

LAS CUATRO SE COMPRUEBAN CON `piezas_que_faltan()`, que es PURA y recibe el
texto: asi su caso positivo por mutacion puede tumbarla una a una sin tocar el
repo ni escribir nada. Su arnes es
`scripts/loop/vuelta172_tarea5_mutacion_cierre.py`.

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


def sha(t):
    return hashlib.sha256(t.replace(chr(13) + NL, NL).encode("utf-8")).hexdigest()


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def rel(ruta):
    return os.path.relpath(ruta, RAIZ).replace(os.sep, "/")


def piezas_que_faltan(texto, filas_tallador, lineas_bateria):
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

    # (4) LA BATERIA DENTRO DE LA SECCION 9
    if (NL + "## 9.") not in texto:
        faltan.append("(4) no hay seccion 9 donde meter la bateria")
    elif not lineas_bateria:
        faltan.append("(4) la salida de la bateria esta vacia")
    else:
        seccion9 = texto[texto.index(NL + "## 9."):]
        fuera = [l for l in lineas_bateria if l.rstrip() not in seccion9]
        if fuera:
            faltan.append("(4) %d linea(s) de la bateria no estan dentro de la "
                          "seccion 9" % len(fuera))
    return faltan


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, required=True)
    ap.add_argument("--cuerpo", required=True)
    ap.add_argument("--tallador", required=True)
    ap.add_argument("--bateria", required=True)
    ap.add_argument("--veredicto", required=True)
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
    if not lineas_bat:
        rojos.append("la salida de la bateria de la vuelta %d esta vacia o no existe. "
                     "ESTE INSTRUMENTO NO CIERRA UN REPORTE SIN SU BATERIA." % V)
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

    seccion9 = (
        CAB_9 + NL + NL +
        "**CORRIDA ENTERA Y SOLA, Y SU SALIDA VA AQUI COMPLETA Y SIN RECORTAR.**" + NL +
        "Fichero: `%s` (**%d bytes, %d lineas no vacias**, contadas" % (a.bateria, tam,
                                                                       len(lineas_bat)) + NL +
        "por `scripts/loop/cerrar_reporte.py`). **Este instrumento CAE EN ROJO si esta" + NL +
        "seccion se queda sin ella**, que es la cuarta de sus cuatro piezas." + NL + NL +
        "```" + NL + bateria.rstrip(NL) + NL + "```" + NL)

    texto = texto.rstrip(NL) + NL + NL + cuerpo.rstrip(NL) + NL + NL + seccion9
    io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(texto)
    print("   ESCRITO: %s (%d bytes, %d saltos de linea)"
          % (rel(REPORTE), len(texto.encode("utf-8")), texto.count(NL)))
    print("")

    print("D) SE RELEE DEL DISCO Y SE MIRAN LAS CUATRO PIEZAS")
    de_nuevo = leer(REPORTE)
    faltan = piezas_que_faltan(de_nuevo, filas, lineas_bat)
    for etiqueta in ("(1) veredicto escrito", "(2) cabecera pegada",
                     "(3) secciones 3 a 9", "(4) bateria dentro de la 9"):
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
