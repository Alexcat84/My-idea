# -*- coding: utf-8 -*-
"""GENERADOR DE UN SOLO USO de la TAREA 4 de la vuelta 195: que `--componer`
PROPAGUE EL PEOR VEREDICTO DE LOS TRAMOS a su propio exitcode y a su linea final,
sin dejar de decir la cobertura por separado.

Se borra al cerrar la vuelta; su producto es el lanzador parcheado."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)
P = os.path.join(RAIZ, "scripts", "loop", "vuelta194_bateria_por_tramos.py")

t = io.open(P, encoding="utf-8").read()

# ------------------------------------------------------- 1. EL LECTOR NUEVO
ancla1 = '''def componer(tramos):
    """LA SALIDA UNICA, COMPUESTA DE LOS TRAMOS Y DESCONFIANDO DE ELLOS."""'''
nuevo1 = '''# --- LOS TRES VEREDICTOS Y SU ORDEN DE GRAVEDAD (vuelta 195, TAREA 4) ---------
#
# POR QUE NACE, Y LA CAUSA ESTA MEDIDA. `docs/loop/SALIDA_V194_BATERIA_COMPUESTA.txt`
# termina en *"VERDE: los 10 tramos cubren la nomina entera"* con `exitcode 0`,
# mientras los DIEZ tramos que compone traen `CLASE DEL VEREDICTO: ROJO POR FALLO`
# y `exitcode 1`. Es cierto EN LO QUE MIDE, la cobertura, y enganoso EN LO QUE
# PARECE DECIR, el estado de la bateria. Banco `9.1`: el instrumento debe caerse
# en vez de mentir. Es el hallazgo `5.3` del acta 195 y la otra mitad de la `P.3`
# del reporte de la 194, y llevaba vueltas en la lista de lo que sigue fuera como
# *"el exitcode 2 propagado a --componer"*.
#
# LOS NOMBRES Y LOS CODIGOS NO SE TECLEAN AQUI: se leen de
# `verificar_mutaciones_viejas`, que es su sede, para que no haya dos tablas que
# manana digan cosas distintas.
GRAVEDAD = {B.VERDE: 0, B.ROJO_POR_DEUDA: 1, B.ROJO_POR_FALLO: 2}
MARCA_CLASE = "CLASE DEL VEREDICTO:"


def clase_de_la_salida(ruta):
    """LA CLASE DEL VEREDICTO QUE UNA SALIDA DE TRAMO PUBLICA. Semi-pura: lo
    unico que toca es leer el fichero que se le pasa.

    Devuelve `(clase, literal)` con `clase` en `GRAVEDAD` o `None` si el fichero
    no publica ninguna. **Un `None` NO se confunde con VERDE**: quien llama lo
    trata como fallo, porque un tramo que no publica su veredicto es un tramo
    cuyo estado no se puede saber, y la duda no se resuelve a favor.

    SE LEE DE LA SALIDA Y NO SE RECALCULA, igual que la cobertura: recalcularla
    seria preguntarle al reparto por el reparto."""
    texto = io.open(ruta, encoding="utf-8", errors="replace").read()
    hallada, literal = None, ""
    for linea in texto.replace(chr(13) + NL, NL).split(NL):
        if MARCA_CLASE not in linea:
            continue
        cola = linea.split(MARCA_CLASE, 1)[1].strip()
        for nombre in sorted(GRAVEDAD, key=lambda x: -len(x)):
            if cola.startswith(nombre):
                # SE QUEDA CON LA PEOR QUE EL PROPIO FICHERO PUBLIQUE, por si
                # una salida trajera mas de una linea de veredicto.
                if hallada is None or GRAVEDAD[nombre] > GRAVEDAD[hallada]:
                    hallada, literal = nombre, linea.strip()
                break
    return hallada, literal


def peor_veredicto(clases):
    """EL PEOR VEREDICTO DE UNA LISTA DE CLASES. PURA.

    Recibe una lista de `(n, clase)` y devuelve `(clase_peor, codigo, ilegibles)`.
    `ilegibles` son los tramos cuya clase salio `None`, y **si hay alguno el peor
    es `ROJO POR FALLO`**: no se puede componer un verde sobre un tramo cuyo
    estado no se sabe.

    LA LISTA VACIA DEVUELVE VERDE, y eso es correcto aqui porque quien llama ya
    ha parado antes si no hay tramos: sin partes no se llega a esta funcion."""
    ilegibles = [n for n, c in clases if c is None]
    peor = B.VERDE
    for _n, c in clases:
        if c is not None and GRAVEDAD[c] > GRAVEDAD[peor]:
            peor = c
    if ilegibles:
        peor = B.ROJO_POR_FALLO
    return peor, B.CODIGO_DE_LA_CLASE[peor], ilegibles


def componer(tramos):
    """LA SALIDA UNICA, COMPUESTA DE LOS TRAMOS Y DESCONFIANDO DE ELLOS.

    DESDE LA VUELTA 195 PROPAGA EL PEOR VEREDICTO DE LOS TRAMOS a su exitcode y a
    su linea final. **LAS DOS COSAS SE SIGUEN DICIENDO POR SEPARADO**: la
    cobertura con su cifra y el veredicto con la suya, porque que propague el rojo
    no puede borrar que la cobertura estaba completa, que es informacion util y
    medida."""'''
assert ancla1 in t
t = t.replace(ancla1, nuevo1, 1)

# ------------------------------------------------- 2. RECOGER LA CLASE POR TRAMO
ancla2 = '''        vistas.extend(ent)
        partes.append((n, ruta, m))'''
nuevo2 = '''        clase, literal_clase = clase_de_la_salida(ruta)
        print("           veredicto del tramo, LEIDO de su salida: %s"
              % (literal_clase or "(la salida no publica CLASE DEL VEREDICTO)"))
        clases.append((n, clase))
        vistas.extend(ent)
        partes.append((n, ruta, m))'''
assert ancla2 in t
t = t.replace(ancla2, nuevo2, 1)

ancla3 = '''    partes = []
    vistas = []
    fallos = []'''
nuevo3 = '''    partes = []
    vistas = []
    fallos = []
    clases = []'''
assert ancla3 in t
t = t.replace(ancla3, nuevo3, 1)

# --------------------------------------- 3. EL BLOQUE DEL VEREDICTO PROPAGADO
ancla4 = '''    print("")
    if fallos:
        print("ROJO, %d motivo(s). LA SALIDA UNICA NO SE COMPONE Y NO SE NOMBRA" % len(fallos))'''
nuevo4 = '''    print("")
    print("  EL VEREDICTO DE LOS TRAMOS, LEIDO DE SUS SALIDAS Y NO RECALCULADO")
    peor, codigo_peor, ilegibles = peor_veredicto(clases)
    for n, c in clases:
        print("      tramo %2d -> %s" % (n, c or "SIN CLASE LEGIBLE"))
    print("  CIFRA tramos con clase ilegible: %d" % len(ilegibles))
    print("  EL PEOR VEREDICTO DE LOS TRAMOS: %s (codigo %d)" % (peor, codigo_peor))
    print("  LAS DOS COSAS SE DICEN POR SEPARADO Y NINGUNA BORRA A LA OTRA: la")
    print("  COBERTURA es lo que este modo mide, y el VEREDICTO es el estado de")
    print("  la bateria. Una cobertura entera con un tramo en rojo NO es VERDE.")

    print("")
    if fallos:
        print("ROJO, %d motivo(s). LA SALIDA UNICA NO SE COMPONE Y NO SE NOMBRA" % len(fallos))'''
assert ancla4 in t
t = t.replace(ancla4, nuevo4, 1)

# ------------------------------------------------------ 4. LA LINEA FINAL
ancla5 = '''    print("")
    print("VERDE: los %d tramos cubren la nomina entera, cada entrada EXACTAMENTE"
          % len(partes))
    print("UNA VEZ, y la salida unica existe y mide %d bytes." % m["bytes_disco"])
    return 0'''
nuevo5 = '''    print("")
    print("LA COBERTURA: los %d tramos cubren la nomina entera, cada entrada"
          % len(partes))
    print("EXACTAMENTE UNA VEZ, y la salida unica existe y mide %d bytes."
          % m["bytes_disco"])
    print("")
    if peor == B.VERDE:
        print("VERDE: la cobertura esta completa Y los %d tramos salieron en verde."
              % len(partes))
        return 0
    print("%s: LA COBERTURA ESTA COMPLETA Y AUN ASI ESTO NO ES VERDE." % peor)
    print("El peor veredicto de los %d tramos es %s, y --componer lo PROPAGA a su"
          % (len(partes), peor))
    print("propio exitcode (%d) y a esta linea. Componer no es aprobar: lo que este"
          % codigo_peor)
    print("modo mide es la COBERTURA, y la cobertura sigue completa; lo que la")
    print("salida ya no puede hacer es leerse como si la bateria estuviera bien.")
    if ilegibles:
        print("Y %d tramo(s) no publican CLASE DEL VEREDICTO: %s. Un tramo cuyo"
              % (len(ilegibles), ", ".join(str(x) for x in ilegibles)))
        print("estado no se puede saber cuenta como fallo, no como verde.")
    return codigo_peor'''
assert ancla5 in t
t = t.replace(ancla5, nuevo5, 1)

io.open(P, "w", encoding="utf-8", newline=NL).write(t)
print("PARCHEADO: scripts/loop/vuelta194_bateria_por_tramos.py (%d bytes)"
      % len(t.encode("utf-8")))
