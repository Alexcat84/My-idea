# -*- coding: utf-8 -*-
r"""vuelta195_tarea4c_mutacion_componer_rojo.py . CASO POSITIVO POR MUTACION DE
QUE `--componer` PROPAGUE EL PEOR VEREDICTO DE LOS TRAMOS (TAREA 4.c de la vuelta
195), CON EL CASO REAL DE LA 194 COMO SUJETO CONGELADO.

POR QUE EXISTE ESTE FICHERO Y NO UN FLAG: la bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS.

QUE PRUEBA, Y ES EL CASO REAL Y NO UNO COMODO. La bateria de la vuelta 194 dejo
DIEZ tramos con `CLASE DEL VEREDICTO: ROJO POR FALLO` y `exitcode 1`, y su
`--componer` publico *"VERDE: los 10 tramos cubren la nomina entera"* con
`exitcode 0`. **Esas dos cosas son las dos verdaderas midiendo cosas distintas**:
la cobertura estaba completa (127 de 127) y la bateria estaba roja. Lo que estaba
mal era que la salida se leyera como si la bateria estuviera bien. Banco `9.1`:
el instrumento debe caerse en vez de mentir.

**AQUI SE EXIGE QUE DIEZ TRAMOS ROJOS CON COBERTURA ENTERA DEN ROJO**, y que el
codigo de salida que se propaga sea el de la clase peor y no un cero.

SUJETO CONGELADO (condicion de la vuelta 148), Y ES EL DE VERDAD Y NO UNO
FABRICADO: las diez salidas de la 194 se leen **por `git show` del commit que las
anadio**, cuyo hash va clavado en `COMMIT_DE_LOS_TRAMOS` mas abajo. Un blob de git
no se mueve. **No se abre ningun fichero del arbol de trabajo**, asi que da igual
lo que pase despues en `docs/loop/`.

Y LOS CASOS QUE NO SE PUEDEN SACAR DEL SUJETO REAL SE FABRICAN EN MEMORIA, con
cadenas literales de este proceso: el tramo verde, el tramo en deuda y el tramo
que no publica su clase. **La 194 no dejo ninguno de esos tres**, y una guarda que
solo se probara con el caso que ya ocurrio no sabria que hacer con el siguiente.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: todos los reales salen de llamar a
`clase_de_la_salida()` y `peor_veredicto()` del lanzador, y la segunda pasada
MUTA el valor esperado de cada caso y exige que CAIGA.

USO:
  python scripts/loop/vuelta195_tarea4c_mutacion_componer_rojo.py
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

NL = chr(10)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta194_bateria_por_tramos as L   # noqa: E402
import verificar_mutaciones_viejas as B   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
SALIDA = os.path.join(LOOP, "SALIDA_V195_T4C_MUTACION_COMPONER_ROJO.txt")

# EL SUJETO CONGELADO: el commit de la 194 que YA TIENE LAS DIEZ salidas de tramo
# en su arbol, que es el que cierra su TAREA 3. Va clavado por hash y no se busca
# en el arbol de trabajo, que es lo que lo hace inmovil.
#
# CORRECCION DECLARADA, Y NO SE BORRA DE QUE IBA: la primera version de este arnes
# apuntaba a `6a508ca5`, que es el commit que ANADIO EL TRAMO 1, y en ese arbol
# solo existia UNO de los diez. El propio caso `los_DIEZ_blobs_se_leen` lo cazo
# midiendo 1 donde tenia que medir 10, que es para lo que ese caso esta.
COMMIT_DE_LOS_TRAMOS = "56c2d085"
RUTAS_DE_LOS_TRAMOS = ["docs/loop/SALIDA_V194_BATERIA_TRAMO_%d.txt" % n
                       for n in range(1, 11)]

# LO QUE LA COMPUESTA DE LA 194 PUBLICO, LITERAL, PARA PODER EXIGIR QUE HOY YA NO
# SE PUEDA PUBLICAR ESO MISMO. Es una CITA, no una afirmacion de este arnes.
LO_QUE_PUBLICO_LA_194 = "VERDE: los 10 tramos cubren la nomina entera"


def git_show(ref):
    """EL BLOB DE UN COMMIT, LEIDO DE GIT Y NO DEL ARBOL DE TRABAJO."""
    r = subprocess.run(["git", "show", ref], cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8", errors="replace")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L_ = []
    w = L_.append
    w("=" * 78)
    w("VUELTA 195, TAREA 4.c: CASO POSITIVO POR MUTACION DE QUE --componer")
    w("PROPAGUE EL PEOR VEREDICTO, CON EL CASO REAL DE LA 194")
    w("=" * 78)
    w("")

    tmp = tempfile.mkdtemp(prefix="v195_componer_")
    casos = []
    try:
        w("A) EL SUJETO CONGELADO: LAS DIEZ SALIDAS DE LA 194, POR BLOB DE GIT")
        w("   commit clavado: %s (no se busca en el arbol)" % COMMIT_DE_LOS_TRAMOS)
        reales = []
        for i, rel in enumerate(RUTAS_DE_LOS_TRAMOS, 1):
            texto = git_show("%s:%s" % (COMMIT_DE_LOS_TRAMOS, rel))
            if texto is None:
                w("   ROJO: no se pudo leer el blob de %s" % rel)
                continue
            destino = os.path.join(tmp, os.path.basename(rel))
            io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
            reales.append((i, destino))
            w("   tramo %2d -> %s: %d bytes del blob"
              % (i, os.path.basename(rel), len(texto.encode("utf-8"))))
        casos.append(("los_DIEZ_blobs_se_leen", len(reales), 10))
        w("")

        w("B) LA CLASE DE CADA UNO, LEIDA DE SU SALIDA Y NO RECALCULADA")
        clases_reales = []
        for n, ruta in reales:
            c, literal = L.clase_de_la_salida(ruta)
            clases_reales.append((n, c))
            w("   tramo %2d -> %-16s %s" % (n, c, literal[:60]))
        casos.append(("los_DIEZ_dan_ROJO_POR_FALLO",
                      sorted({c for _n, c in clases_reales}), [B.ROJO_POR_FALLO]))
        w("")

        w("C) EL CASO QUE EL ENCARGO NOMBRA: DIEZ TRAMOS ROJOS TIENEN QUE DAR ROJO")
        peor, codigo, ilegibles = L.peor_veredicto(clases_reales)
        w("   peor veredicto: %r | codigo de salida: %d | ilegibles: %d"
          % (peor, codigo, len(ilegibles)))
        casos.append(("el_peor_de_los_diez_es_ROJO_POR_FALLO", peor,
                      B.ROJO_POR_FALLO))
        casos.append(("y_su_codigo_de_salida_NO_es_cero", codigo != 0, True))
        casos.append(("y_no_hay_ninguno_ilegible", len(ilegibles), 0))
        w("   LA CITA DE LO QUE LA 194 PUBLICO, Y ES UNA CITA Y NO UNA AFIRMACION")
        w("   DE ESTE ARNES: %r" % LO_QUE_PUBLICO_LA_194)
        w("   Con esta maquina esa linea YA NO SE PUEDE ESCRIBIR sobre estos diez,")
        w("   porque el veredicto propagado no es VERDE.")
        casos.append(("con_estos_diez_el_veredicto_ya_no_es_VERDE",
                      peor == B.VERDE, False))
        w("")

        w("D) LOS TRES CASOS QUE LA 194 NO DEJO, FABRICADOS EN MEMORIA")
        w("   Una guarda probada solo con el caso que ya ocurrio no sabe que hacer")
        w("   con el siguiente, asi que los tres se fabrican aqui.")
        fabricados = [
            ("verde", "CORRIDA DE MENTIRA" + NL
             + "      CLASE DEL VEREDICTO: VERDE | CIFRA exitcode: 0" + NL,
             B.VERDE),
            ("deuda", "CORRIDA DE MENTIRA" + NL
             + "      CLASE DEL VEREDICTO: ROJO POR DEUDA DECLARADA | CIFRA "
               "exitcode: 2" + NL,
             B.ROJO_POR_DEUDA),
            ("mudo", "CORRIDA DE MENTIRA SIN VEREDICTO NINGUNO" + NL, None),
        ]
        leidos = []
        for etiqueta, texto, esperado in fabricados:
            ruta = os.path.join(tmp, "FABRICADO_%s.txt" % etiqueta)
            io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
            c, _lit = L.clase_de_la_salida(ruta)
            leidos.append((etiqueta, c))
            w("   %-6s -> %s" % (etiqueta, c))
            casos.append(("el_fabricado_%s_se_lee_bien" % etiqueta, c, esperado))
        w("")

        w("E) LA ESCALERA DE GRAVEDAD, PROBADA EN SUS TRES PELDANOS")
        w("   VERDE solo con todos verdes; la deuda gana al verde; y el fallo gana")
        w("   a la deuda. Si el orden estuviera al reves, una bateria con un arnes")
        w("   caido se publicaria como deuda declarada, que es la degradacion que")
        w("   la 4.4 del acta 190 ya cazo una vez.")
        solo_verdes = [(1, B.VERDE), (2, B.VERDE)]
        con_deuda = [(1, B.VERDE), (2, B.ROJO_POR_DEUDA)]
        con_fallo = [(1, B.ROJO_POR_DEUDA), (2, B.ROJO_POR_FALLO)]
        for etiqueta, lista, esperado in (
                ("solo verdes", solo_verdes, B.VERDE),
                ("verde mas deuda", con_deuda, B.ROJO_POR_DEUDA),
                ("deuda mas fallo", con_fallo, B.ROJO_POR_FALLO)):
            p, cod, _i = L.peor_veredicto(lista)
            w("   %-16s -> %-26s codigo %d" % (etiqueta, p, cod))
            casos.append(("peor_de_%s" % etiqueta.replace(" ", "_"), p, esperado))
        w("")

        w("F) UN TRAMO QUE NO PUBLICA SU CLASE CUENTA COMO FALLO, NO COMO VERDE")
        w("   La duda no se resuelve a favor: un tramo cuyo estado no se puede")
        w("   saber no puede sostener un verde compuesto.")
        con_mudo = [(1, B.VERDE), (2, None)]
        p, cod, ilg = L.peor_veredicto(con_mudo)
        w("   verde mas mudo -> %s codigo %d, ilegibles %s" % (p, cod, ilg))
        casos.append(("un_tramo_mudo_pone_ROJO_POR_FALLO", p, B.ROJO_POR_FALLO))
        casos.append(("y_lo_nombra_en_la_lista_de_ilegibles", ilg, [2]))
        w("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        w("G) EL TEMPORAL SE RETIRA (P.16, quien fabrica limpia)")
        w("   sigue existiendo: %s" % ("SI" if os.path.isdir(tmp) else "NO"))
        casos.append(("el_temporal_queda_retirado", os.path.isdir(tmp), False))
        w("")

    w("H) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = real == esperado
        fallos += 0 if ok else 1
        w("   %-52s %-6s (real=%r esperado=%r)"
          % (nombre, "PASA" if ok else "FALLA", real, esperado))
    w("   CIFRA casos: %d | pasan: %d | fallan: %d"
      % (len(casos), len(casos) - fallos, fallos))
    w("")

    w("I) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, list):
            mutado = esperado + ["DE MENTIRA"]
        elif esperado is None:
            mutado = "ALGO QUE NO ES None"
        else:
            mutado = str(esperado) + " DE MENTIRA"
        cae = real != mutado
        caen += 1 if cae else 0
        w("   %-52s %-7s (esperado mutado=%r)"
          % (nombre, "CAE" if cae else "NO CAE", mutado))
    w("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    w("")

    ok = (fallos == 0 and caen == len(casos))
    w("CIFRA casos: %d | pasan: %d | fallan: %d"
      % (len(casos), len(casos) - fallos, fallos))
    if ok:
        w("VEREDICTO: VERDE")
        w("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
          % (len(casos), len(casos)))
    else:
        w("VEREDICTO: ROJO")
        w("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))

    t = NL.join(L_) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)"
          % (os.path.relpath(SALIDA, RAIZ).replace("\\", "/"),
             len(t.encode("utf-8"))))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
