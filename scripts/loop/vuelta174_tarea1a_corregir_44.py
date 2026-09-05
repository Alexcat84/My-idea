# -*- coding: utf-8 -*-
r"""vuelta174_tarea1a_corregir_44.py . LA CLAUSULA DE LA 4.4, CORREGIDA POR EL
CARRIL DEL `9.10` ANTES DE QUE EL REPORTE DE LA 172 SE CIERRE Y SE ARCHIVE.

POR QUE VA AQUI Y NO DESPUES. El encargo de la vuelta 174 dice, en su ultima
linea de trabajo: *"Y EL UNICO ARREGLO DE TEXTO PENDIENTE: la clausula de la 4.4
se corrige por el carril 9.10 (se tacha con su correccion fechada debajo, NO se
borra)"*. La 4.4 del acta del auditor de la vuelta 172 (`docs/loop/ACTA_AUDITOR.md`
linea 58649, leida hoy) dice, literal: *"LA FILA DE LA TAREA 5 DICE CERRADA Y
NOMBRA COMO PRUEBA UN FICHERO QUE NO EXISTE"*. Esa fila vive dentro de
`docs/loop/REPORTE.md`, que es EXACTAMENTE el fichero que la TAREA 1.a de esta
vuelta cierra y archiva. Corregirla despues de archivar seria sellar la
afirmacion falsa en `docs/loop/reportes/REPORTE_V172.md` y corregir luego una
copia: por eso se corrige ANTES, y la eleccion va escrita para que se pueda
discutir.

QUE ES FALSO, Y SE MIDE EN VEZ DE CREERSELO. La fila da a la TAREA 5 el estado
CERRADA y nombra dos pruebas. Este instrumento MIDE LAS DOS en el disco antes de
escribir una letra, por la regla del 5 sep 2026 (`EJECUTOR.md` 1, "LA RUTA QUE
PROMETE PRUEBA ES CIFRA"): una ruta publicada como evidencia que apunta a un
fichero inexistente o de cero bytes es CAIDA DE CIFRA. Si la medicion de hoy NO
confirmase que la ruta esta vacia, este instrumento CAE EN ROJO y no escribe
nada: no se corrige por lo que dijo un acta, se corrige por lo que mide el disco.

COMO ESCRIBE, Y ES EL CARRIL `9.10` TAL COMO LO APLICO LA TAREA 2.b DE LA 172
SOBRE EL `R.40`: el texto viejo QUEDA ENTERO Y TACHADO, nunca borrado, y la
correccion va fechada debajo de la tabla. Una correccion que tapa lo que corrige
no se puede auditar (`EJECUTOR.md` 8).

LA SIMULACION VA SOBRE COPIA EN MEMORIA (`AUDITOR.md` 3, guardas obligatorias por
operacion): `corregir(texto)` es PURA, recibe el texto y devuelve
`(texto_nuevo, motivos)`. No lee ni escribe nada. Por eso su caso positivo,
`scripts/loop/vuelta174_tarea1a_mutacion_44.py`, puede tumbarla motivo a motivo
sin tocar el repo.

USO:
  python scripts/loop/vuelta174_tarea1a_corregir_44.py
  python scripts/loop/vuelta174_tarea1a_corregir_44.py --solo-comprobar
"""
import argparse
import io
import os
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")

FIN_TABLA = "<!-- FIN TABLA DE TAREAS -->"
INICIO_FILA = "| **TAREA 5** |"
CELDA_VIEJA = "| **CERRADA** |"
PRUEBA_VIEJA = "`_T5_CERRAR_REPORTE` (la corrida de esta misma vuelta)"
MARCA_CORRECCION = "CORRECCION DECLARADA (5 sep 2026, vuelta 174, TAREA 1.a"

CELDA_NUEVA = ("| ~~**CERRADA**~~ **ABIERTA, SIN CERRAR EN LA 172** "
               "(correccion declarada del 5 sep 2026, debajo de la tabla) |")


def bloque_correccion(medicion):
    """EL BLOQUE QUE VA DEBAJO DE LA TABLA. `medicion` son las lineas ya medidas
    en el disco, que este texto NO inventa. PURA."""
    return (NL +
            "> **%s, por el carril del banco `9.10`).**" % MARCA_CORRECCION + NL +
            "> **LA FILA DE LA TAREA 5 DECIA `CERRADA` Y NOMBRABA COMO PRUEBA UNA RUTA" + NL +
            "> SOBRE UN VACIO.** La fila vieja queda entera y tachada; no se borra nada." + NL +
            "> **Lo medido HOY en el disco por `scripts/loop/vuelta174_tarea1a_corregir_44.py`," + NL +
            "> con `os.path.exists` y `os.path.getsize`, no tecleado:**" + NL +
            ">" + NL +
            NL.join("> " + l for l in medicion) + NL +
            ">" + NL +
            "> **LO QUE DE VERDAD PASO, Y ES LO QUE DICE LA `4.4` DEL ACTA DEL AUDITOR DE" + NL +
            "> LA VUELTA 172** (`docs/loop/ACTA_AUDITOR.md:58649`, leida hoy): el encargo de" + NL +
            "> aquella TAREA 5 pedia TRES cosas, *\"el instrumento, su caso positivo, y que" + NL +
            "> esta vuelta se cerrara con el\"*. **Las dos primeras estan hechas y" + NL +
            "> verificadas** (el arnes de mutacion existe y su salida tambien). **La tercera" + NL +
            "> no la hizo la vuelta 172: la paga la vuelta 174**, y por eso el estado" + NL +
            "> corregido es ABIERTA, SIN CERRAR EN LA 172 y no CERRADA." + NL +
            ">" + NL +
            "> **LA REGLA QUE LO CONVIERTE EN CAIDA Y NO EN DESCUIDO** es del 5 sep 2026," + NL +
            "> `EJECUTOR.md` 1: **LA RUTA QUE PROMETE PRUEBA ES CIFRA**. Una ruta publicada" + NL +
            "> como evidencia que apunta a un fichero inexistente o de cero bytes es CAIDA" + NL +
            "> DE CIFRA en su sede. **El auditor la registro cuando esa regla todavia no" + NL +
            "> existia y la trato como rotulo de estado, sin acumular; hoy la regla existe," + NL +
            "> y quien decide si esto acumula hacia atras es el auditor, no yo.**" + NL)


def corregir(texto, medicion):
    """LA CORRECCION, SOBRE COPIA EN MEMORIA. Devuelve `(texto_nuevo, motivos)`;
    `motivos` VACIA si salio bien, y entonces `texto_nuevo` es el corregido. Si
    hay un solo motivo, `texto_nuevo` es el texto ORIGINAL sin tocar: este
    instrumento no escribe reportes a medias.

    PURA a proposito: ni lee ni escribe. Su caso positivo por mutacion vive en
    `scripts/loop/vuelta174_tarea1a_mutacion_44.py` y la tumba motivo a motivo."""
    motivos = []

    if MARCA_CORRECCION in texto:
        motivos.append("la correccion YA ESTA escrita en este texto: este "
                       "instrumento no la escribe dos veces")
    if texto.count(FIN_TABLA) != 1:
        motivos.append("la marca %r aparece %d veces y tiene que aparecer UNA"
                       % (FIN_TABLA, texto.count(FIN_TABLA)))
    filas = [l for l in texto.split(NL) if l.startswith(INICIO_FILA)]
    if len(filas) != 1:
        motivos.append("la fila %r aparece %d veces y tiene que aparecer UNA"
                       % (INICIO_FILA, len(filas)))
    if not medicion:
        motivos.append("no se paso ninguna medicion: una correccion sin la "
                       "medicion que la sostiene no se escribe")
    if motivos:
        return texto, motivos

    fila = filas[0]
    if fila.count(CELDA_VIEJA) != 1:
        motivos.append("la fila de la TAREA 5 no trae la celda %r exactamente "
                       "una vez (trae %d)" % (CELDA_VIEJA, fila.count(CELDA_VIEJA)))
    if fila.count(PRUEBA_VIEJA) != 1:
        motivos.append("la fila de la TAREA 5 no trae la prueba falsa %r "
                       "exactamente una vez (trae %d)"
                       % (PRUEBA_VIEJA, fila.count(PRUEBA_VIEJA)))
    if motivos:
        return texto, motivos

    fila_nueva = fila.replace(CELDA_VIEJA, CELDA_NUEVA)
    fila_nueva = fila_nueva.replace(PRUEBA_VIEJA, "~~" + PRUEBA_VIEJA + "~~")
    nuevo = texto.replace(fila, fila_nueva)

    i = nuevo.index(FIN_TABLA) + len(FIN_TABLA)
    nuevo = nuevo[:i] + NL + bloque_correccion(medicion) + nuevo[i:]

    # LAS COMPROBACIONES SOBRE LO YA CONSTRUIDO, DENTRO DE LA MISMA FUNCION PURA,
    # para que la mutacion pueda tumbarlas sin escribir en disco.
    if "~~**CERRADA**~~" not in nuevo:
        motivos.append("el CERRADA viejo no quedo tachado")
    if PRUEBA_VIEJA not in nuevo:
        motivos.append("la prueba vieja se perdio, y el 9.10 dice que NO se borra")
    if "~~" + PRUEBA_VIEJA + "~~" not in nuevo:
        motivos.append("la prueba vieja no quedo tachada")
    if MARCA_CORRECCION not in nuevo:
        motivos.append("el bloque de correccion no quedo escrito")
    if nuevo.index(MARCA_CORRECCION) < nuevo.index(FIN_TABLA):
        motivos.append("el bloque de correccion no quedo DEBAJO de la tabla")
    if chr(8212) in nuevo or chr(8211) in nuevo:
        motivos.append("se colaron guiones largos o medios")
    if motivos:
        return texto, motivos
    return nuevo, []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-comprobar", action="store_true")
    a = ap.parse_args()

    print("=" * 78)
    print("VUELTA 174, TAREA 1.a: LA CLAUSULA DE LA 4.4, CORREGIDA POR EL `9.10`")
    print("=" * 78)
    print("")

    print("A) EL SUJETO, ACOTADO ANTES DE TOCARLO")
    texto = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    print("   docs/loop/REPORTE.md -> %d bytes, %d saltos de linea"
          % (len(texto.encode("utf-8")), texto.count(NL)))
    print("   primera linea: %s" % texto.split(NL, 1)[0][:88])
    for i, l in enumerate(texto.split(NL), 1):
        if l.startswith(INICIO_FILA):
            print("   la fila de la TAREA 5 esta en REPORTE.md:%d (%d bytes)"
                  % (i, len(l.encode("utf-8"))))
    print("")

    print("B) LAS DOS RUTAS QUE LA FILA NOMBRA, MEDIDAS EN EL DISCO DE HOY")
    print("   (LA RUTA QUE PROMETE PRUEBA ES CIFRA, EJECUTOR.md 1, 5 sep 2026)")
    medicion = []
    vacia = 0
    for r in ["docs/loop/SALIDA_V172_T5_MUTACION_CIERRE.txt",
              "docs/loop/SALIDA_V172_T5_CERRAR_REPORTE.txt"]:
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        if not os.path.exists(p):
            est = "**NO EXISTE**"
            vacia += 1
        elif os.path.getsize(p) == 0:
            est = "**EXISTE PERO 0 BYTES**"
            vacia += 1
        else:
            est = "**%d bytes**" % os.path.getsize(p)
        medicion.append("- `%s` -> %s" % (r, est))
        print("   %-52s %s" % (r, est.replace("*", "")))
    print("   CIFRA rutas de la fila que apuntan a un vacio: %d" % vacia)
    if vacia != 1:
        print("")
        print("ROJO: la fila nombra 2 rutas y hoy %d apuntan a un vacio. La 4.4 dice"
              % vacia)
        print("      que es UNA (la corrida que no existe). No se escribe nada.")
        return 1
    print("")

    print("C) LA SIMULACION, SOBRE COPIA EN MEMORIA Y SIN TOCAR EL DISCO")
    nuevo, motivos = corregir(texto, medicion)
    print("   corregir() devuelve %d motivo(s)" % len(motivos))
    for m in motivos:
        print("      " + m)
    if motivos:
        print("")
        print("ROJO: la simulacion no sale limpia y NO se escribe nada.")
        return 1
    print("   texto simulado: %d bytes (%+d contra el original)"
          % (len(nuevo.encode("utf-8")),
             len(nuevo.encode("utf-8")) - len(texto.encode("utf-8"))))
    print("   lineas: %d -> %d (adicion pura: %s)"
          % (texto.count(NL), nuevo.count(NL),
             "SI" if nuevo.count(NL) >= texto.count(NL) else "NO"))
    print("")

    if a.solo_comprobar:
        print("SOLO COMPROBAR: la simulacion sale limpia y NO se escribe nada.")
        return 0

    print("D) SE ESCRIBE")
    io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(nuevo)
    print("   ESCRITO: docs/loop/REPORTE.md (%d bytes)" % len(nuevo.encode("utf-8")))
    print("")

    print("E) LA RELECTURA DEL DISCO, QUE ES LA QUE VALE")
    de_nuevo = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    fila = [l for l in de_nuevo.split(NL) if l.startswith(INICIO_FILA)]
    fila = fila[0] if fila else ""
    pruebas = [
        ("el CERRADA viejo sigue ENTERO en la fila", "**CERRADA**" in fila),
        ("y ahora esta TACHADO", "~~**CERRADA**~~" in fila),
        ("el estado corregido esta escrito al lado",
         "**ABIERTA, SIN CERRAR EN LA 172**" in fila),
        ("la prueba falsa sigue ENTERA", PRUEBA_VIEJA in fila),
        ("y ahora esta TACHADA", "~~" + PRUEBA_VIEJA + "~~" in fila),
        ("la prueba que SI existe sigue sin tachar",
         "`SALIDA_V172_T5_MUTACION_CIERRE.txt`," in fila),
        ("el bloque de correccion esta escrito", MARCA_CORRECCION in de_nuevo),
        ("y esta DEBAJO de la tabla",
         MARCA_CORRECCION in de_nuevo and FIN_TABLA in de_nuevo
         and de_nuevo.index(MARCA_CORRECCION) > de_nuevo.index(FIN_TABLA)),
        ("la medicion de hoy esta dentro del bloque",
         "SALIDA_V172_T5_CERRAR_REPORTE.txt` -> **NO EXISTE**" in de_nuevo),
        ("las otras cuatro filas de tareas siguen intactas",
         all(de_nuevo.count("| **TAREA %d** |" % k) == 1 for k in (1, 2, 3, 4))),
        ("ninguna otra fila quedo tachada", de_nuevo.count("~~**CERRADA**~~") == 1),
        ("el reporte sigue SIN CERRAR (el hueco y el veredicto viejo siguen)",
         "PENDIENTE DE TALLAR AL CIERRE" in de_nuevo
         and "SIN ESCRIBIR TODAVIA" in de_nuevo),
        ("cero guiones largos y cero guiones medios",
         chr(8212) not in de_nuevo and chr(8211) not in de_nuevo),
    ]
    fallan = 0
    for etiqueta, ok in pruebas:
        print("   %-58s %s" % (etiqueta, "SI" if ok else "NO"))
        if not ok:
            fallan += 1
    print("   CIFRA comprobaciones: %d | fallan: %d" % (len(pruebas), fallan))
    print("")
    if fallan:
        print("ROJO: %d comprobacion(es) de la relectura fallan." % fallan)
        return 1
    print("VERDE: la clausula de la 4.4 queda corregida por el carril del `9.10`,")
    print("       con el texto viejo entero y tachado y la correccion fechada debajo.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
