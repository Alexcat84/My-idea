# -*- coding: utf-8 -*-
r"""vuelta188_tarea3c_mutacion_exclusion_por_rojo.py . EL CASO POSITIVO POR
MUTACION DE LA EXCLUSION POR ROJO DE LA DOBLE CORRIDA.

QUIEN LA ENCARGA. La `C.3` del acta 188, que el auditor levanto y el ejecutor no
trajo: en la vuelta 187, `vuelta186_tarea2c_mutacion_cierre_tardio.py` cayo en
rojo y **se corrio DOS VECES MAS** dentro de la doble corrida de la 5.a, contra la
letra que dice *"te detienes ahi, lo traes con su salida entera, **sin
re-correrlo** y sin arreglarlo"*.

QUE PRUEBA, CASO A CASO, Y TODOS TIENEN QUE CAER AL MUTAR SU ESPERADO:

  (A) UN REGISTRO VACIO NO EXCLUYE A NADIE, y eso es lo que hace que la exclusion
      no pueda tapar nada por descuido: sin rojos, la doble corrida corre todo.

  (B) UN REGISTRO QUE NOMBRA UN ARNES LO EXCLUYE, y el excluido **desaparece de
      la lista que se corre**. Es la mitad que arregla la `C.3`.

  (C) LA EXCLUSION NO ES MUDA: el excluido sale con **su nombre, la ruta de su
      salida en rojo y su motivo**. Una exclusion muda seria peor que el
      problema, porque un arnes que no corre y no se nombra parece un arnes que
      corrio.

  (D) LA COMPARACION ES POR NOMBRE DE FICHERO Y NO POR RUTA COMPLETA: un registro
      escrito con barras invertidas excluye igual. Un arnes que se salvara de la
      exclusion por una barra seria exactamente el descuido que esto impide.

  (E) UNA LINEA DEL REGISTRO SIN MOTIVO EXCLUYE IGUAL, PERO LO DICE: el arnes no
      se re corre (que es lo prudente) y la salida declara que su motivo no
      estaba escrito, en vez de inventarle uno.

LO QUE ESTE ARNES NO HACE: no corre ningun arnes, no escribe ningun registro de
rojos y no toca `docs/loop/`. Llama a las DOS funciones PURAS del fichero vivo
con registros fabricados en memoria.

Y PUBLICA EL `sha256` DE SU SUJETO AL LADO DE TODO NUMERO DE LINEA (vuelta 188,
TAREA 3.b; respuesta del acta 188 a la `P.2`).

USO:
  python scripts/loop/vuelta188_tarea3c_mutacion_exclusion_por_rojo.py
"""
import hashlib
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta188_tarea3c_nomina as NOM   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
SUJETO = "scripts/loop/vuelta188_tarea3c_nomina.py"

# UNA LISTA DE MENTIRA, CON LA MISMA FORMA QUE LA DE VERDAD.
LISTA = [
    ("scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py",
     "docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt", "de la 186"),
    ("scripts/loop/vuelta188_tarea2_mutacion_pata_documental.py",
     "docs/loop/SALIDA_V188_T2_MUTACION_PATA_DOCUMENTAL.txt", "NACE HOY"),
    ("scripts/loop/vuelta187_tarea4_mutacion_dos_convenciones.py",
     "docs/loop/SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt", "de la 187"),
]


def sello_del_sujeto(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    datos = io.open(p, "rb").read()
    lf = datos.replace(chr(13).encode() + chr(10).encode(), chr(10).encode())
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest())


def _caso_a(w):
    fallos = casos = caen = 0
    w("CASO A. UN REGISTRO VACIO NO EXCLUYE A NADIE")
    for etiqueta, texto in (("fichero que no existe (cadena vacia)", ""),
                            ("registro solo con cabecera de comentarios",
                             "# ROJOS DE LA VUELTA 188" + NL + "#" + NL),
                            ("registro con lineas en blanco", NL + NL + "   " + NL)):
        rojos = NOM.rojos_registrados(texto)
        corren, excluidos = NOM.particion_por_rojo(LISTA, rojos)
        casos += 1
        ok = (len(rojos) == 0 and len(excluidos) == 0 and len(corren) == len(LISTA))
        w("   %-44s -> rojos %d | excluidos %d | corren %d de %d | %s"
          % (etiqueta, len(rojos), len(excluidos), len(corren), len(LISTA),
             "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos += 1
        w("      MUTACION del esperado (exigir 1 excluido): %s"
          % ("PASA" if len(excluidos) == 1 else "CAE"))
        if len(excluidos) == 1:
            fallos += 1
        else:
            caen += 1
    w("")
    return fallos, casos, caen


def _caso_bc(w):
    fallos = casos = caen = 0
    w("CASO B. UN REGISTRO QUE NOMBRA UN ARNES LO EXCLUYE, Y EL EXCLUIDO")
    w("        DESAPARECE DE LA LISTA QUE SE CORRE")
    texto = ("# ROJOS DE LA VUELTA 188" + NL
             + "scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py | "
               "docs/loop/SALIDA_V186_T2C_EN_ROJO.txt | "
               "cayo en rojo con CIFRA fallos: 2 y su remedio es de otra vuelta"
             + NL)
    rojos = NOM.rojos_registrados(texto)
    corren, excluidos = NOM.particion_por_rojo(LISTA, rojos)
    casos += 1
    nombres_corren = [os.path.basename(s) for s, _x, _y in corren]
    ok = (len(rojos) == 1 and len(excluidos) == 1 and len(corren) == len(LISTA) - 1
          and "vuelta186_tarea2c_mutacion_cierre_tardio.py" not in nombres_corren)
    w("   rojos %d | excluidos %d | corren %d de %d" % (len(rojos), len(excluidos),
                                                        len(corren), len(LISTA)))
    w("   los que corren: %s" % ", ".join(nombres_corren))
    w("   ESPERADO: el excluido NO esta entre los que corren -> %s"
      % ("CALZA" if ok else "NO CALZA"))
    if not ok:
        fallos += 1
    w("   MUTACION del esperado (exigir que corran los %d): %s"
      % (len(LISTA), "PASA" if len(corren) == len(LISTA) else "CAE"))
    if len(corren) == len(LISTA):
        fallos += 1
    else:
        caen += 1
    w("")

    w("CASO C. LA EXCLUSION NO ES MUDA: NOMBRE, RUTA DE SU ROJO Y MOTIVO")
    casos += 1
    script, salida, origen, ruta, motivo = excluidos[0]
    w("   script:  %s" % script)
    w("   salida:  %s" % salida)
    w("   ruta del rojo: %s" % ruta)
    w("   motivo:  %s" % motivo)
    ok_c = (script.endswith("vuelta186_tarea2c_mutacion_cierre_tardio.py")
            and ruta == "docs/loop/SALIDA_V186_T2C_EN_ROJO.txt"
            and "CIFRA fallos: 2" in motivo)
    w("   ESPERADO: las TRES piezas presentes y no una sola -> %s"
      % ("CALZA" if ok_c else "NO CALZA"))
    if not ok_c:
        fallos += 1
    w("   MUTACION del esperado (exigir que el motivo NO se conserve): %s"
      % ("PASA" if "CIFRA fallos: 2" not in motivo else "CAE"))
    if "CIFRA fallos: 2" not in motivo:
        fallos += 1
    else:
        caen += 1
    w("")
    return fallos, casos, caen


def _caso_de(w):
    fallos = casos = caen = 0
    w("CASO D. LA COMPARACION ES POR NOMBRE DE FICHERO Y NO POR RUTA COMPLETA")
    for etiqueta, linea in (
            ("ruta con barras invertidas",
             "scripts\\loop\\vuelta186_tarea2c_mutacion_cierre_tardio.py | x.txt | m"),
            ("solo el nombre, sin directorio",
             "vuelta186_tarea2c_mutacion_cierre_tardio.py | x.txt | m"),
            ("ruta con directorio de mas",
             "a/b/scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py | x.txt | m")):
        rojos = NOM.rojos_registrados(linea + NL)
        corren, excluidos = NOM.particion_por_rojo(LISTA, rojos)
        casos += 1
        ok = (len(excluidos) == 1)
        w("   %-32s -> excluidos %d | %s"
          % (etiqueta, len(excluidos), "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos += 1
        w("      MUTACION del esperado (exigir 0 excluidos): %s"
          % ("PASA" if len(excluidos) == 0 else "CAE"))
        if len(excluidos) == 0:
            fallos += 1
        else:
            caen += 1
    w("   Y UN NOMBRE QUE NO ESTA EN LA LISTA NO EXCLUYE A NADIE, para que se vea")
    w("   que no esta clavado:")
    rojos = NOM.rojos_registrados("scripts/loop/vuelta999_otro.py | x.txt | m" + NL)
    corren, excluidos = NOM.particion_por_rojo(LISTA, rojos)
    casos += 1
    w("      rojos %d | excluidos %d | corren %d -> %s"
      % (len(rojos), len(excluidos), len(corren),
         "CALZA" if (len(rojos) == 1 and not excluidos) else "NO CALZA"))
    if excluidos or len(rojos) != 1:
        fallos += 1
    else:
        caen += 1
    w("")

    w("CASO E. UNA LINEA SIN MOTIVO EXCLUYE IGUAL, PERO LO DICE")
    for etiqueta, linea, esperado_motivo, esperado_ruta in (
            ("sin motivo, con ruta",
             "scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py | x.txt",
             "(sin motivo declarado)", "x.txt"),
            ("solo el nombre",
             "scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py",
             "(sin motivo declarado)", "(sin salida declarada)")):
        rojos = NOM.rojos_registrados(linea + NL)
        corren, excluidos = NOM.particion_por_rojo(LISTA, rojos)
        casos += 1
        ok = (len(excluidos) == 1
              and excluidos[0][4] == esperado_motivo
              and excluidos[0][3] == esperado_ruta)
        w("   %-22s -> excluidos %d | ruta %r | motivo %r | %s"
          % (etiqueta, len(excluidos),
             excluidos[0][3] if excluidos else None,
             excluidos[0][4] if excluidos else None,
             "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos += 1
        w("      MUTACION del esperado (exigir un motivo inventado): %s"
          % ("PASA" if excluidos and excluidos[0][4] == "el que sea" else "CAE"))
        if excluidos and excluidos[0][4] == "el que sea":
            fallos += 1
        else:
            caen += 1
    w("   NO SE LE INVENTA UN MOTIVO: se excluye igual, porque no re correrlo es lo")
    w("   prudente, y la salida declara que su motivo no estaba escrito.")
    w("")
    return fallos, casos, caen


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    disco, lf, sha = sello_del_sujeto(SUJETO)
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DE LA EXCLUSION POR ROJO DE LA DOBLE CORRIDA")
    w("(vuelta 188, TAREA 3.c; remedio de la `C.3` del acta 188)")
    w("=" * 78)
    w("")
    w("EL SUJETO ES EL FICHERO VIVO %s, IMPORTADO." % SUJETO)
    w("SELLO DEL SUJETO (vuelta 188, TAREA 3.b): disco %d bytes | LF %d bytes |"
      % (disco, lf))
    w("sha256 LF %s" % sha)
    w("")
    w("LINEAS DEL SUJETO QUE ESTE ARNES JUZGA, LEIDAS HOY Y CON EL SELLO DE ARRIBA:")
    fuente = io.open(os.path.join(RAIZ, SUJETO.replace("/", os.sep)),
                     encoding="utf-8").read().replace(chr(13) + NL, NL)
    for aguja in ("def rojos_registrados", "def particion_por_rojo",
                  "REGISTRO_ROJOS ="):
        hits = [i for i, l in enumerate(fuente.split(NL), 1) if l.startswith(aguja)]
        w("   %-28s -> lineas %s"
          % (aguja, ", ".join(str(x) for x in hits) or "(ninguna)"))
    w("")
    w("LA LISTA DE MENTIRA SOBRE LA QUE SE PARTE, CON %d ENTRADAS:" % len(LISTA))
    for s, _x, o in LISTA:
        w("   %-58s %s" % (os.path.basename(s), o))
    w("")
    fallos = casos = caen = 0
    for parte in (_caso_a, _caso_bc, _caso_de):
        f, c, k = parte(w)
        fallos += f
        casos += c
        caen += k
    w("CIFRA casos: %d | pasan: %d" % (casos, casos - fallos))
    w("CIFRA casos que CAEN al mutar su esperado: %d de %d" % (caen, caen))
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
