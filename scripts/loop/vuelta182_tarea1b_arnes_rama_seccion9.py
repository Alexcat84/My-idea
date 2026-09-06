# -*- coding: utf-8 -*-
r"""vuelta182_tarea1b_arnes_rama_seccion9.py . EL ARNES DE `rama_de_la_seccion9()`,
LA FUNCION QUE NACE CON EL REMEDIO DEL `E.1` DEL ACTA 180.

QUE PRUEBA, Y EL PRIMER CASO ES EL DE LA CAIDA REAL: el escenario exacto de la
vuelta 180, con el fichero `docs/loop/SALIDA_V180_HUECO_BATERIA.txt` (que existia
y traia 21 lineas) pasado a un cierre de la vuelta 180. **Con la logica vieja eso
entraba por la rama de CORRIDA ENTERA Y SOLA; con la nueva tiene que salir HUECO
o ROJO.** Si algun dia vuelve a salir CORRIDA, este arnes cae y el `E.1` esta de
vuelta.

LA LOGICA VIEJA SE REIMPLEMENTA AQUI, DECLARADA COMO COPIA HISTORICA Y NO COMO
CODIGO VIVO (`rama_vieja()`), porque un remedio que no puede ensenar el mal que
cura no se puede auditar. No se importa de ningun sitio: el fichero vivo ya no la
tiene.

Y EL CASO ROJO SE PRUEBA POR MUTACION (`EJECUTOR.md` 1, letra del 29 ago 2026).
Ninguna comparacion de aqui es entre dos constantes literales: la rama SE COMPUTA
llamando a la funcion de verdad, y al final se muta el valor esperado de un caso
y se comprueba que ese caso CAE. Si no cayera, no probaria nada.

USO:
  python scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

# LA COPIA HISTORICA. Es el codigo que `main()` tenia ANTES del remedio, escrito
# aqui para poder ensenar la caida. NO ES CODIGO VIVO y no se importa de ningun
# lado: `cerrar_reporte.py` ya no lo tiene.
PATRON_VIEJO = re.compile(r"SALIDA_V(\d+)_BATERIA")


def rama_vieja(lineas_bateria, nombre_bateria, vuelta):
    """LA LOGICA DE ANTES DEL REMEDIO, TAL CUAL ERA. La guarda de vuelta ajena
    pedia `ajena is not None`, asi que un None se saltaba en silencio, y la rama
    se elegia SOLO por si el fichero traia lineas."""
    m = PATRON_VIEJO.search(nombre_bateria or "")
    ajena = int(m.group(1)) if m else None
    if ajena is not None and ajena != vuelta:
        return "ROJO", "vuelta ajena"
    return ("CORRIDA" if lineas_bateria else "HUECO"), "por si trae lineas"


# LOS CASOS. Cada uno es (nombre, lineas, fichero, vuelta, rama esperada NUEVA).
# El esperado es lo unico escrito a mano; la rama sale de llamar a la funcion.
CASOS = [
    ("EL CASO REAL DE LA 180: fichero con lineas y con HUECO en el nombre",
     21, "docs/loop/SALIDA_V180_HUECO_BATERIA.txt", 180, "HUECO"),
    ("EL MISMO FICHERO PASADO A OTRA VUELTA: es corrida ajena",
     21, "docs/loop/SALIDA_V180_HUECO_BATERIA.txt", 182, "ROJO"),
    ("HUECO DE VERDAD: fichero de ESTA vuelta y sin lineas",
     0, "docs/loop/SALIDA_V182_HUECO_BATERIA.txt", 182, "HUECO"),
    ("BATERIA DE VERDAD: fichero de ESTA vuelta y con lineas",
     900, "docs/loop/SALIDA_V182_BATERIA.txt", 182, "CORRIDA"),
    ("CORRIDA AJENA CLASICA: la de la 176 pasada a la 182",
     900, "docs/loop/SALIDA_V176_BATERIA.txt", 182, "ROJO"),
    ("FICHERO ANONIMO: el nombre no dice de que vuelta es",
     900, "docs/loop/SALIDA_DE_LA_BATERIA.txt", 182, "ROJO"),
    ("FICHERO ANONIMO Y VACIO: sigue siendo ROJO, no HUECO",
     0, "docs/loop/bateria.txt", 182, "ROJO"),
    ("SIN VUELTA: no se puede juzgar nada",
     900, "docs/loop/SALIDA_V182_BATERIA.txt", None, "ROJO"),
    ("TRAMO DE LA 183: el nombre por tramos sigue diciendo su vuelta",
     900, "docs/loop/SALIDA_V183_BATERIA_TRAMO_1.txt", 183, "CORRIDA"),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    salida = []
    w = salida.append
    w("ARNES DE rama_de_la_seccion9(), REMEDIO DEL E.1 DEL ACTA 180")
    w("sujeto vivo: scripts/loop/cerrar_reporte.py")
    w("")

    if not hasattr(CR, "rama_de_la_seccion9"):
        w("ROJO: cerrar_reporte.py NO tiene rama_de_la_seccion9(). El remedio no")
        w("      esta puesto, y este arnes no puede probar nada.")
        print(NL.join(salida))
        return 1

    w("A) EL PATRON, ANTES Y DESPUES, SOBRE LOS MISMOS NOMBRES")
    for nombre in ("docs/loop/SALIDA_V180_HUECO_BATERIA.txt",
                   "docs/loop/SALIDA_V181_BATERIA.txt",
                   "docs/loop/SALIDA_V183_BATERIA_TRAMO_1.txt",
                   "docs/loop/SALIDA_DE_LA_BATERIA.txt"):
        m = PATRON_VIEJO.search(nombre)
        w("   %-48s viejo -> %-5s | vivo -> %s"
          % (nombre, m.group(1) if m else "None", CR.vuelta_de_fichero(nombre)))
    w("")

    w("B) LOS CASOS, CON LAS DOS LOGICAS AL LADO")
    fallos = 0
    n_cambia = 0
    for nombre, n_lineas, fichero, vuelta, esperada in CASOS:
        lineas = ["x"] * n_lineas
        vieja, _mv = rama_vieja(lineas, fichero, vuelta)
        nueva, motivo = CR.rama_de_la_seccion9(lineas, fichero, vuelta)
        ok = nueva == esperada
        if not ok:
            fallos += 1
        if vieja != nueva:
            n_cambia += 1
        w("   %s" % nombre)
        w("      lineas %-4d fichero %-46s vuelta %s" % (n_lineas, fichero, vuelta))
        w("      VIEJA -> %-8s | VIVA -> %-8s | esperada %-8s | %s"
          % (vieja, nueva, esperada, "CALZA" if ok else "NO CALZA"))
        w("      motivo de la viva: %s" % motivo[:130])
    w("")
    w("   CIFRA casos: %d" % len(CASOS))
    w("   CIFRA que CALZAN: %d" % (len(CASOS) - fallos))
    w("   CIFRA que NO CALZAN: %d" % fallos)
    w("   CIFRA casos en que la logica vieja y la viva DIFIEREN: %d" % n_cambia)
    w("")

    w("C) EL CASO DE LA CAIDA REAL, SOLO, PORQUE ES EL QUE IMPORTA")
    lineas = ["x"] * 21
    vieja, _m = rama_vieja(lineas, "docs/loop/SALIDA_V180_HUECO_BATERIA.txt", 180)
    viva, motivo = CR.rama_de_la_seccion9(
        lineas, "docs/loop/SALIDA_V180_HUECO_BATERIA.txt", 180)
    w("   la 180 paso un fichero de 21 lineas llamado SALIDA_V180_HUECO_BATERIA")
    w("   LA LOGICA VIEJA lo mandaba a: %s" % vieja)
    w("   LA LOGICA VIVA lo manda a:    %s" % viva)
    w("   motivo: %s" % motivo)
    w("   LA CABECERA QUE SALDRIA CON CADA UNA:")
    w("      vieja -> %s" % (CR.CAB_9 if vieja == "CORRIDA" else CR.CAB_9_HUECO))
    w("      viva  -> %s" % (CR.CAB_9 if viva == "CORRIDA" else CR.CAB_9_HUECO))
    w("   Y LA GUARDA hueco_declarado_que_falta() CORRE: %s"
      % ("NO, porque la rama de CORRIDA no la llama" if viva == "CORRIDA"
         else "SI, porque la rama de HUECO es la que la llama"))
    w("")
    w("   LA HISTORIA DE ESTE CASO, DECLARADA PORQUE ES LA PRUEBA DE QUE EL ARNES")
    w("   SIRVE PARA ALGO. Este fichero se escribio ANTES de aplicar el remedio y")
    w("   la primera pasada del remedio llevaba solo tres piezas: el patron")
    w("   ensanchado, el None que deja de ser silencio y la funcion pura. Con esas")
    w("   tres, este arnes salio VERDE en sus nueve casos Y ESTA MISMA SECCION C")
    w("   publicaba que el caso real de la 180 SEGUIA saliendo CORRIDA, porque el")
    w("   fichero SI era de la vuelta 180 y SI traia lineas. Esa salida esta entera")
    w("   y sin tocar en docs/loop/SALIDA_V182_T1B_ARNES_REMEDIO_INCOMPLETO.txt.")
    w("   DE AHI SALIO LA PIEZA (d): una corrida no es cualquier fichero con")
    w("   lineas, tiene que LLAMARSE como se llama una corrida. Un remedio que su")
    w("   propio arnes destapa a medias es el arnes haciendo su trabajo.")
    w("")

    w("D) LA MUTACION DEL VALOR ESPERADO, QUE ES LO QUE PRUEBA QUE ESTO CAE")
    lineas = ["x"] * 21
    medida, _m2 = CR.rama_de_la_seccion9(
        lineas, "docs/loop/SALIDA_V180_HUECO_BATERIA.txt", 182)
    w("   caso mutado: el fichero de la 180 pasado a un cierre de la 182")
    w("   la rama COMPUTADA (no escrita) es: %s" % medida)
    for esperado in ("ROJO", "CORRIDA"):
        w("   con el esperado %-8s -> %s"
          % (esperado, "PASA" if medida == esperado else "CAE"))
    cae = medida != "CORRIDA"
    w("   EL CASO CAE AL MUTAR EL ESPERADO A CORRIDA: %s" % ("SI" if cae else "NO"))
    if not cae:
        fallos += 1
    w("")
    w("   LA SEGUNDA MUTACION: SE LE QUITA LA IDENTIDAD AL NOMBRE.")
    sin_id, _m3 = CR.rama_de_la_seccion9(lineas, "docs/loop/bateria_182.txt", 182)
    w("   con el nombre sin SALIDA_V<N>_ la rama computada es: %s" % sin_id)
    w("   TENIA QUE SER ROJO: %s" % ("SI" if sin_id == "ROJO" else "NO"))
    if sin_id != "ROJO":
        fallos += 1
    w("")
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))

    t = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
