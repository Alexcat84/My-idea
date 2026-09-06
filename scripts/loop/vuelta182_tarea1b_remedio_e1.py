# -*- coding: utf-8 -*-
r"""vuelta182_tarea1b_remedio_e1.py . EL REMEDIO DEL `E.1` DEL ACTA 180, APLICADO
SOBRE `scripts/loop/cerrar_reporte.py` Y NO NARRADO.

QUE PASO, MEDIDO POR EL AUDITOR Y RE-MEDIDO AQUI (acta 180 seccion 5, cabecera en
`docs/loop/ACTA_AUDITOR.md:62449`). El reporte de la vuelta 180 salio con la
cabecera **"## 9. LA BATERIA DE MUTACIONES, CORRIDA ENTERA Y SOLA AL CIERRE"**
sobre una seccion cuyo propio cuerpo decia que NADIE LA CORRIO. Tres causas, y
las tres son de codigo:

  1. `PATRON_FICHERO_BATERIA` buscaba `SALIDA_V(\d+)_BATERIA` y el fichero que se
     paso se llamaba `SALIDA_V180_HUECO_BATERIA.txt`. **La `H` de HUECO se metia
     entre la vuelta y la palabra BATERIA**, asi que `vuelta_de_fichero()`
     devolvia `None`.
  2. Con `None`, la guarda de VUELTA AJENA no compara nada y se salta: su
     condicion es `ajena is not None and ajena != V`.
  3. Y la rama de la seccion 9 se elegia SOLO por `if lineas_bat:`, o sea POR SI
     EL FICHERO TRAE LINEAS, sin preguntar de que vuelta es. El fichero tecleado
     traia 21 lineas, luego entro por la rama de CORRIDA ENTERA, y
     `hueco_declarado_que_falta()`, que **solo se llama en la rama `else`**,
     nunca corrio sobre el hueco de la 180.

EL REMEDIO, Y SON TRES COSAS PORQUE LAS CAUSAS ERAN TRES:

  (a) EL PATRON SE ENSANCHA A LO QUE DE VERDAD HAY: `SALIDA_V<N>_<lo que sea>_
      BATERIA`. Con eso `SALIDA_V180_HUECO_BATERIA` deja de dar `None` y pasa a
      dar 180, que es la verdad.
  (b) `None` DEJA DE SER SILENCIO Y PASA A SER ROJO. Un fichero de bateria cuyo
      nombre no dice de que vuelta es NO cierra ningun reporte. Es `banco 9`,
      fallar ruidoso: la degradacion silenciosa no deja sintoma.
  (c) LA DECISION DE RAMA SALE DE `main()` Y SE HACE FUNCION PURA,
      `rama_de_la_seccion9()`. Mientras vivio dentro de `main()` no habia forma
      de probarla sin escribir un reporte entero, y por eso nadie la probo. Ahora
      su arnes la tumba caso por caso sin tocar el repo.

  (d) Y UNA CORRIDA NO ES CUALQUIER FICHERO CON LINEAS: TIENE QUE LLAMARSE COMO
      SE LLAMA UNA CORRIDA. `SALIDA_V<N>_BATERIA...` es una corrida;
      `SALIDA_V<N>_HUECO_BATERIA` NO lo es, por mucho que traiga lineas, y va a
      la rama del HUECO, que es la que llama a `hueco_declarado_que_falta()`.

LA (d) NO ESTABA EN LA PRIMERA PASADA DE ESTE REMEDIO Y LA CAZO SU PROPIO ARNES,
Y ESO SE DECLARA EN VEZ DE TAPARSE. Con solo la (a), la (b) y la (c) puestas,
`scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py` salio VERDE en sus nueve
casos pero su seccion C publicaba, con todas las letras, que EL CASO REAL DE LA
180 SEGUIA SALIENDO `CORRIDA`: el fichero SI era de la vuelta 180 y SI traia
lineas, asi que el ensanche del patron le daba identidad correcta y la rama
seguia mintiendo. Esa salida queda entera y sin tocar en
`docs/loop/SALIDA_V182_T1B_ARNES_REMEDIO_INCOMPLETO.txt` (5.293 bytes) y la del
parche a medias en `docs/loop/SALIDA_V182_T1B_REMEDIO_E1_PRIMERA_PASADA.txt`
(867 bytes). **Un remedio que su propio arnes destapa a medias es el arnes
haciendo su trabajo**, y por eso el arnes se escribio ANTES de aplicar nada.

LO QUE EL REMEDIO NO HACE, Y SE DICE: no afloja ninguna guarda. La rama de
CORRIDA ENTERA se vuelve MAS estrecha, no menos: antes bastaba con traer lineas,
ahora hay que traer lineas Y ser de esta vuelta.

USO:
  python scripts/loop/vuelta182_tarea1b_remedio_e1.py --simular
  python scripts/loop/vuelta182_tarea1b_remedio_e1.py
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CER = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

VIEJO_PATRON = '''PATRON_FICHERO_BATERIA = re.compile(r"SALIDA_V(\\d+)_BATERIA")'''
NUEVO_PATRON = '''# EL PATRON, ENSANCHADO EN LA VUELTA 182 POR EL REMEDIO DEL `E.1` DEL ACTA 180.
# ANTES ERA r"SALIDA_V(\\d+)_BATERIA" Y ESA ERA LA PRIMERA DE LAS TRES CAUSAS: el
# fichero que la vuelta 180 paso se llamaba `SALIDA_V180_HUECO_BATERIA.txt`, con
# la palabra HUECO metida entre la vuelta y la palabra BATERIA, asi que el patron
# NO casaba y `vuelta_de_fichero()` devolvia None. El trozo `[A-Z0-9_]*` admite
# cualquier cosa en medio SIN admitir minusculas ni otro fichero: sigue exigiendo
# `SALIDA_V<numero>_` delante y `BATERIA` detras.
PATRON_FICHERO_BATERIA = re.compile(r"SALIDA_V(\\d+)_[A-Z0-9_]*BATERIA")

# EL NOMBRE DE UNA CORRIDA, QUE NO ES LO MISMO QUE UN NOMBRE QUE LLEVE UNA VUELTA
# DENTRO. Nace en la vuelta 182 con la pieza (d) del remedio del `E.1`:
# `SALIDA_V180_BATERIA.txt` y `SALIDA_V176_BATERIA_TRAMO_3.txt` SI son nombres de
# corrida; `SALIDA_V180_HUECO_BATERIA.txt` NO lo es, y ese fue justamente el
# fichero con el que la vuelta 180 publico una cabecera falsa sobre un cuerpo que
# decia lo contrario.
PATRON_NOMBRE_DE_CORRIDA = re.compile(r"^SALIDA_V\\d+_BATERIA[A-Z0-9_]*\\.txt$")'''

ANCLA_FUNCION = '''def hueco_declarado_que_falta(seccion9, vuelta):'''

FUNCION_NUEVA = '''def rama_de_la_seccion9(lineas_bateria, nombre_bateria, vuelta):
    """QUE RAMA LE TOCA A LA SECCION 9, Y POR QUE. Devuelve (rama, motivo) con
    rama en `CORRIDA`, `HUECO` o `ROJO`.

    NACE EN LA VUELTA 182 COMO REMEDIO DEL `E.1` DEL ACTA 180, y nace FUERA de
    `main()` a proposito. Mientras esta decision vivio dentro de `main()` no se
    podia probar sin escribir un reporte entero, y por eso nadie la probo: el
    reporte de la 180 salio diciendo CORRIDA ENTERA Y SOLA sobre una seccion cuyo
    cuerpo decia que nadie la corrio.

    LAS TRES REGLAS, EN ORDEN, Y LA PRIMERA ES LA QUE FALTABA:

      1. SI EL NOMBRE NO DICE DE QUE VUELTA ES, ES ROJO. Antes esto era silencio:
         `vuelta_de_fichero()` devolvia None y la guarda de vuelta ajena se
         saltaba porque su condicion pedia `ajena is not None`. Un fichero de
         bateria anonimo NO cierra un reporte (`banco 9`, fallar ruidoso).
      2. SI EL NOMBRE DICE OTRA VUELTA, ES ROJO. Esta ya existia y se conserva
         palabra por palabra: una corrida de otra vuelta no cierra este reporte.
      3. SI EL NOMBRE NO ES EL DE UNA CORRIDA, ES `HUECO` AUNQUE TRAIGA LINEAS.
         `SALIDA_V<N>_BATERIA...` es el nombre de una corrida;
         `SALIDA_V<N>_HUECO_BATERIA` no lo es. ESTA ES LA REGLA QUE LE FALTABA A
         LA 180: su fichero era de la vuelta 180 y traia 21 lineas, asi que ni la
         identidad ni el conteo lo paraban, y la cabecera salio diciendo CORRIDA
         ENTERA Y SOLA sobre un cuerpo que decia lo contrario.
      4. SOLO ENTONCES SE MIRA SI TRAE LINEAS. Con lineas, `CORRIDA`; sin lineas,
         `HUECO`, que es la rama donde vive `hueco_declarado_que_falta()`.

    LA RAMA DE CORRIDA SE VUELVE MAS ESTRECHA, NO MAS ANCHA: antes bastaba con
    traer lineas, ahora hay que traer lineas Y ser de esta vuelta.

    PURA: no lee ni escribe nada, para que su arnes la pueda tumbar caso por caso
    sin tocar el repo."""
    if vuelta is None:
        return "ROJO", ("no se dijo de que vuelta es este reporte, y sin eso no se "
                        "puede juzgar ninguna bateria")
    ajena = vuelta_de_fichero(nombre_bateria)
    if ajena is None:
        return "ROJO", ("el fichero de bateria %r no dice de que vuelta es. Un "
                        "fichero anonimo NO cierra un reporte: se llama "
                        "SALIDA_V<N>_BATERIA o no vale" % (nombre_bateria,))
    if ajena != vuelta:
        return "ROJO", ("el fichero de bateria que se pasa es el de la vuelta %d y "
                        "se esta cerrando la %d. UNA CORRIDA DE OTRA VUELTA NO "
                        "CIERRA ESTE REPORTE." % (ajena, vuelta))
    if not PATRON_NOMBRE_DE_CORRIDA.match(os.path.basename(nombre_bateria)):
        return "HUECO", ("el fichero %r es de la vuelta %d pero NO se llama como "
                         "una corrida: una corrida se llama SALIDA_V<N>_BATERIA y "
                         "esto no lo es, asi que no puede declararse corrida por "
                         "mucho que traiga lineas"
                         % (os.path.basename(nombre_bateria), vuelta))
    if lineas_bateria:
        return "CORRIDA", ("la bateria de la vuelta %d trae %d linea(s) no vacias"
                           % (vuelta, len(lineas_bateria)))
    return "HUECO", ("la bateria de la vuelta %d no corrio: su fichero no existe o "
                     "esta vacio" % vuelta)


'''

VIEJO_MAIN = '''    ajena = vuelta_de_fichero(a.bateria)
    print("   vuelta que lleva dentro el nombre del fichero: %s" % ajena)
    if ajena is not None and ajena != V:
        rojos.append("el fichero de bateria que se pasa es el de la vuelta %d y se "
                     "esta cerrando la %d. UNA CORRIDA DE OTRA VUELTA NO CIERRA "
                     "ESTE REPORTE." % (ajena, V))
    atribucion = a.hueco_atribucion.strip()
    if not lineas_bat:'''

NUEVO_MAIN = '''    ajena = vuelta_de_fichero(a.bateria)
    print("   vuelta que lleva dentro el nombre del fichero: %s" % ajena)
    # LA DECISION DE RAMA YA NO SE TOMA AQUI: la toma rama_de_la_seccion9(), que
    # es pura y tiene arnes propio. REMEDIO DEL `E.1` DEL ACTA 180, vuelta 182.
    rama, motivo_rama = rama_de_la_seccion9(lineas_bat, a.bateria, V)
    print("   RAMA DE LA SECCION 9, decidida por rama_de_la_seccion9(): %s" % rama)
    print("      motivo: %s" % motivo_rama)
    if rama == "ROJO":
        rojos.append(motivo_rama)
    atribucion = a.hueco_atribucion.strip()
    if rama == "HUECO":'''

VIEJO_RAMA = '''    if lineas_bat:
        seccion9 = (
            CAB_9 + NL + NL +'''
NUEVO_RAMA = '''    if rama == "CORRIDA":
        seccion9 = (
            CAB_9 + NL + NL +'''


def aplicar(texto):
    """PURA: recibe el texto de cerrar_reporte.py y devuelve (texto_nuevo,
    informe). Asi el arnes puede correr el parche sobre una copia."""
    informe = []
    for viejo, nuevo, nombre in (
            (VIEJO_PATRON, NUEVO_PATRON, "(a) el patron ensanchado"),
            (ANCLA_FUNCION, FUNCION_NUEVA + ANCLA_FUNCION,
             "(c) la funcion pura rama_de_la_seccion9"),
            (VIEJO_MAIN, NUEVO_MAIN, "(b) None deja de ser silencio, en main()"),
            (VIEJO_RAMA, NUEVO_RAMA, "(c) main() usa la rama decidida")):
        if viejo not in texto:
            informe.append("NO SE ENCUENTRA EL TROZO DE %s" % nombre)
            return None, informe
        texto = texto.replace(viejo, nuevo, 1)
        informe.append("APLICADO: %s" % nombre)
    return texto, informe


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    salida = []
    w = salida.append
    w("VUELTA 182, TAREA 1.b: EL REMEDIO DEL E.1 DEL ACTA 180")
    w("sujeto: scripts/loop/cerrar_reporte.py")
    t = io.open(CER, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("   ANTES: %d lineas | disco %d bytes | LF %d bytes"
      % (len(t.split(NL)), os.path.getsize(CER), len(t.encode("utf-8"))))
    w("")

    w("EL ESTADO DE ANTES, MEDIDO Y NO RECORDADO:")
    import re as _re
    pat_viejo = _re.compile(r"SALIDA_V(\d+)_BATERIA")
    for nombre in ("docs/loop/SALIDA_V180_HUECO_BATERIA.txt",
                   "docs/loop/SALIDA_V181_BATERIA.txt",
                   "docs/loop/SALIDA_V182_HUECO_BATERIA.txt"):
        m = pat_viejo.search(nombre)
        w("   patron VIEJO sobre %-44s -> %s"
          % (nombre, m.group(1) if m else "None"))
    w("   (el primero da None y ESA es la causa 1 del E.1)")
    w("")

    nuevo, informe = aplicar(t)
    for l in informe:
        w("   " + l)
    if nuevo is None:
        w("ROJO: el remedio NO se aplica.")
        print(NL.join(salida))
        return 1
    w("")
    w("   DESPUES: %d lineas | LF %d bytes"
      % (len(nuevo.split(NL)), len(nuevo.encode("utf-8"))))
    w("   CRECE EN: %d bytes" % (len(nuevo.encode("utf-8")) - len(t.encode("utf-8"))))
    w("")

    if a.simular:
        w("MODO --simular: NO SE ESCRIBE cerrar_reporte.py.")
    else:
        io.open(CER, "w", encoding="utf-8", newline=NL).write(nuevo)
        rele = io.open(CER, encoding="utf-8").read().replace(chr(13) + NL, NL)
        w("ESCRITO scripts/loop/cerrar_reporte.py")
        w("   RELEIDO DEL DISCO, identico a lo que se quiso escribir: %s"
          % ("SI" if rele == nuevo else "NO"))
        w("   disco %d bytes" % os.path.getsize(CER))
        import ast
        try:
            ast.parse(rele)
            w("   SINTAXIS: OK")
        except SyntaxError as e:
            w("   SINTAXIS: ROJA -> %r" % (e,))
            print(NL.join(salida))
            return 1

    t2 = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_T1B_REMEDIO_E1.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t2)
    print(t2)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t2.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
