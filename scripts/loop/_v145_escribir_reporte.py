# -*- coding: utf-8 -*-
"""_v145_escribir_reporte.py . Arma docs/loop/REPORTE.md de la vuelta 145
PEGANDO cada tabla desde su fichero de salida, nunca tecleandola (EJECUTOR.md
1: "LA TABLA SE IMPRIME, NO SE TECLEA" y "LA TABLA SE CUENTA DE SU FICHERO").

La prosa se escribe aqui; las TABLAS y los BLOQUES se leen de docs/loop/. Si
un fichero citado no existe, ES ROJO y no se escribe el reporte a medias."""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")


def leer(nombre, desde=None, hasta=None):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        raise SystemExit("ROJO: falta docs/loop/%s, el reporte no se escribe a medias" % nombre)
    texto = io.open(ruta, encoding="utf-8").read().rstrip("\n")
    if desde is None and hasta is None:
        return texto
    lineas = texto.split("\n")
    i = 0
    if desde is not None:
        for j, l in enumerate(lineas):
            if desde in l:
                i = j
                break
        else:
            raise SystemExit("ROJO: %r no aparece en %s" % (desde, nombre))
    j = len(lineas)
    if hasta is not None:
        for k in range(i + 1, len(lineas)):
            if hasta in lineas[k]:
                j = k
                break
    return "\n".join(lineas[i:j]).rstrip("\n")


UNIDADES = ("fichero", "ficheros", "par", "pares", "grupo", "grupos", "grafia",
            "grafias", "colapso", "colapsos", "nodo", "nodos", "linea", "lineas",
            "arista", "aristas")
RE_CIFRA = None


def _trae_cifra(linea):
    """Si la linea trae un par (numero, unidad) del vocabulario cerrado de
    verificar_cifras_del_reporte.py. Se usa SOLO para decidir cada cuanto va la
    cita, nunca para cambiar una cifra."""
    global RE_CIFRA
    if RE_CIFRA is None:
        import re
        RE_CIFRA = re.compile(r"(\d[\d.,]*)\s+(%s)\b" % "|".join(UNIDADES), re.IGNORECASE)
    return bool(RE_CIFRA.search(linea))


def bloque(P, nombre, desde=None, hasta=None, cita=None):
    """Pega el contenido de docs/loop/<nombre> EN TRAMOS, y detras de cada
    tramo deja la CITA del fichero del que sale.

    POR QUE EN TRAMOS Y NO ENTERO: la ventana de cotejo de
    `verificar_cifras_del_reporte.py` es `frases[i:i+3]`, o sea la propia linea
    mas las DOS siguientes. Un bloque largo con cifras en el medio deja esas
    cifras SIN fichero que contar, que es ROJO y con razon. El tramo maximo es
    de UNA linea con cifra, de modo que la cita cae SIEMPRE dentro de la
    ventana (la linea, el cierre de la valla y la cita: tres). Ni una cifra se
    teclea: todas salen del fichero."""
    texto = leer(nombre, desde, hasta)
    linea_cita = cita or ("Contado de `%s`." % nombre)
    lineas = texto.split("\n")
    tramo = []
    con_cifra = 0

    def volcar():
        if not tramo:
            return
        P.append("```")
        P.extend(tramo)
        P.append("```")
        P.append(linea_cita)
        P.append("")
        del tramo[:]

    for l in lineas:
        tramo.append(l)
        if _trae_cifra(l):
            con_cifra += 1
        if con_cifra >= 1:
            volcar()
            con_cifra = 0
    volcar()


def tabla_de_la_cabecera():
    """Solo las filas de la tabla del tallador, tal cual."""
    texto = leer("SALIDA_V145_TALLADOR_CABECERA.txt")
    filas = [l for l in texto.split("\n") if l.startswith("|")]
    if not filas:
        raise SystemExit("ROJO: el tallador no dejo ni una fila de tabla")
    return "\n".join(filas)


def solo_lineas(P, nombre, prefijo, cita=None):
    """Pega SOLO las lineas de docs/loop/<nombre> que empiezan por `prefijo`,
    una por bloque y cada una con su cita debajo.

    POR QUE EXISTE: hay salidas cuyo detalle trae cifras que su propio fichero
    NO puede cotejar (por ejemplo, cuantos nodos usan cada grafia, que no lleva
    linea `CIFRA`). Pegar ese detalle obligaria a la guarda a contar contra la
    unica linea `CIFRA` de esa unidad y a dar ROJO con razon. Se pegan las
    lineas `CIFRA`, que SI se cotejan, y el detalle se deja en el fichero
    citado, que es donde vive entero."""
    texto = leer(nombre)
    linea_cita = cita or ("Contado de `%s`." % nombre)
    hallados = [l for l in texto.split("\n") if l.strip().startswith(prefijo)]
    if not hallados:
        raise SystemExit("ROJO: ninguna linea de %s empieza por %r" % (nombre, prefijo))
    for l in hallados:
        P.append("```")
        P.append(l.strip())
        P.append("```")
        P.append(linea_cita)
        P.append("")
