# -*- coding: utf-8 -*-
r"""_v178_parche_aislador.py . EL PARCHE QUE ANADE `--puestos` Y `--excluir` A
`scripts/loop/aislador_de_ciega.py` (vuelta 178, TAREA 1.d).

ES UN PARCHE, NO CODIGO VIVO, y por eso empieza por guion bajo: no lo ve el
censo de arneses y no entra en ninguna nomina. Se corre UNA VEZ y queda en el
repo para que el cambio se pueda auditar sin leer un diff a ojo.

CADA SUSTITUCION LLEVA SU `assert`: si el texto viejo no esta donde dice, el
parche PARA y no escribe nada. Un parche que aplica a medias es peor que uno que
no aplica.
"""
import io
import os

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R = os.path.join(RAIZ, "scripts", "loop", "aislador_de_ciega.py")

t = io.open(R, encoding="utf-8").read().replace(chr(13) + NL, NL)
PARES = []

PARES.append(("""  2. ELIGE LOS PARES con selectores deterministas sobre
     `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (dominio, clase, banda, rango de
     puestos, muestra con semilla). La muestra usa `random.Random(semilla)`,
     asi que la misma semilla da los mismos pares y la eleccion se puede
     reproducir.""",
"""  2. ELIGE LOS PARES con selectores deterministas sobre
     `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (dominio, clase, banda, rango de
     puestos, LISTA DE PUESTOS, LISTA DE EXCLUIDOS, muestra con semilla). La
     muestra usa `random.Random(semilla)`, asi que la misma semilla da los
     mismos pares y la eleccion se puede reproducir."""))

EXTRA = """EL CARRIL POR LISTA DE PUESTOS (vuelta 178, TAREA 1.d), Y POR QUE HACIA FALTA.
Hasta aqui este fichero elegia por dominio, clase, banda, rango o muestra, y NO
POR LISTA DE PUESTOS. Los discutibles marcados de una vuelta caen casi siempre en
PUESTOS SUELTOS Y DISPERSOS (334, 394, 404, y 878 fuera), que no son un rango ni
un dominio ni una muestra: el auditor de la vuelta 178 tuvo que escribirse
`scripts/loop/_auditor_v178_ciega.py` para poder auditar la 177, importando las
funciones de aqui en vez de copiarlas. Esa muleta SE BORRA en esta misma vuelta
(`P.16`, quien fabrica limpia) porque el lanzador ya hace su trabajo.

  `--puestos 334,394,404`  se queda SOLO con esos puestos.
  `--excluir 878`          los quita de la seleccion.

LOS DOS SON COMPONIBLES con los selectores que ya habia, y se aplican DESPUES
de ellos: `--dominio x --puestos 1,2` es "de los de x, esos dos", no "esos dos
mas los de x". El orden esta escrito aqui para que no haya que deducirlo de la
salida.

Y LOS DOS CAEN EN ROJO SI UN PUESTO PEDIDO NO EXISTE EN EL ARCHIVO, NOMBRANDOLO.
Pedir un puesto que no esta y recibir una seleccion mas corta EN SILENCIO es la
especie que este bucle castiga (banco 9, fallar ruidoso): la seleccion saldria
bien formada y con un par de menos, y nadie lo notaria. El rojo alcanza tambien a
`--excluir`, y se dice por que: el universo de los dos es el mismo archivo, asi
que nombrar ahi un puesto que no existe es la misma errata mida por donde se
mida. La comprobacion es contra EL ARCHIVO ENTERO y no contra la seleccion, para
que "no existe" y "lo filtro otro selector" no se confundan: lo segundo NO es
rojo, y la salida lo dice con su cifra.

LA GUARDA DE FUGA NO SE TOCA y sigue corriendo sobre la seleccion nueva, sea
cual sea el selector que la produjo.

"""
PARES.append(("LO QUE NO HACE, DICHO PARA QUE NADIE LEA DE MAS:",
              EXTRA + "LO QUE NO HACE, DICHO PARA QUE NADIE LEA DE MAS:"))

PARES.append(("""CASO POSITIVO POR MUTACION: `scripts/loop/vuelta170_tarea2a_mutacion_aislador.py`.
CAE si el destape se cuela en la salida ciega, o si la lista blanca se ensancha
para dejarlo pasar.""",
"""SUS CASOS POSITIVOS POR MUTACION SON DOS, y ninguno sustituye al otro:
`scripts/loop/vuelta170_tarea2a_mutacion_aislador.py`, que CAE si el destape se
cuela en la salida ciega o si la lista blanca se ensancha para dejarlo pasar; y
`scripts/loop/vuelta178_tarea1d_mutacion_puestos.py`, que prueba el carril por
lista de puestos, su composicion con los selectores viejos, y EL ROJO DEL PUESTO
INEXISTENTE."""))

PARES.append(("""      --muestra 10 --semilla 170 --ciega A.txt --destape B.txt""",
"""      --muestra 10 --semilla 170 --ciega A.txt --destape B.txt
  python scripts/loop/aislador_de_ciega.py --criterio "los discutibles de la 177" \\
      --puestos 334,394,404 --excluir 878 --ciega A.txt --destape B.txt"""))

VIEJO_E = '''def elegir(filas, dominio=None, clase=None, banda=False, desde=None, hasta=None,
           muestra=None, semilla=None):
    """LA ELECCION, DETERMINISTA Y REPRODUCIBLE. Pura: recibe las filas."""
    sel = list(filas)'''
NUEVO_E = '''def lista_de_puestos(texto):
    """`"334,394, 404"` da `[334, 394, 404]`, sin repetidos y en orden. PURA.

    Devuelve `None` si no se paso nada, que NO es lo mismo que una lista vacia:
    `None` es "no se pidio este selector", y una lista vacia seria "se pidio y
    no nombra a nadie", que este fichero trata como rojo mas abajo."""
    if texto is None:
        return None
    trozos = [x.strip() for x in str(texto).replace(";", ",").split(",")]
    return sorted({int(x) for x in trozos if x})


def puestos_que_no_existen(filas, puestos):
    """LOS PUESTOS PEDIDOS QUE EL ARCHIVO NO TIENE. PURA: recibe las filas.

    SE MIRA CONTRA EL ARCHIVO ENTERO Y NO CONTRA LA SELECCION, a proposito: un
    puesto que existe pero que otro selector filtro NO es un error, y confundir
    las dos cosas convertiria en rojo el uso normal de `--dominio` junto con
    `--puestos`. Lo que aqui es rojo es pedir un puesto QUE NO ESTA EN NINGUNA
    PARTE, que solo puede ser una errata."""
    if not puestos:
        return []
    hay = set(f.get("puesto_intra") for f in filas)
    return sorted(p for p in puestos if p not in hay)


def elegir(filas, dominio=None, clase=None, banda=False, desde=None, hasta=None,
           muestra=None, semilla=None, puestos=None, excluir=None):
    """LA ELECCION, DETERMINISTA Y REPRODUCIBLE. Pura: recibe las filas.

    `puestos` y `excluir` (vuelta 178, TAREA 1.d) son listas de enteros y se
    aplican DESPUES de los selectores viejos, que es lo que los hace
    componibles: `--dominio x --puestos 1,2` es "de los de x, esos dos"."""
    sel = list(filas)'''
PARES.append((VIEJO_E, NUEVO_E))

PARES.append(("""    if hasta is not None:
        sel = [f for f in sel if f.get("puesto_intra", 0) <= hasta]
    sel.sort(key=lambda f: f.get("puesto_intra", 0))""",
"""    if hasta is not None:
        sel = [f for f in sel if f.get("puesto_intra", 0) <= hasta]
    if puestos:
        pedidos = set(puestos)
        sel = [f for f in sel if f.get("puesto_intra") in pedidos]
    if excluir:
        fuera = set(excluir)
        sel = [f for f in sel if f.get("puesto_intra") not in fuera]
    sel.sort(key=lambda f: f.get("puesto_intra", 0))"""))

PARES.append(("""    ap.add_argument("--muestra", type=int)
    ap.add_argument("--semilla", type=int, default=0)""",
'''    ap.add_argument("--muestra", type=int)
    ap.add_argument("--semilla", type=int, default=0)
    ap.add_argument("--puestos",
                    help="LISTA DE PUESTOS separada por comas, por ejemplo "
                         "334,394,404. Se queda SOLO con esos, y se aplica DESPUES "
                         "de los demas selectores. CAE EN ROJO si alguno no existe "
                         "en el archivo.")
    ap.add_argument("--excluir",
                    help="LISTA DE PUESTOS que se quitan de la seleccion, por "
                         "ejemplo 878. Mismo rojo que --puestos si alguno no "
                         "existe.")'''))

VIEJO_S = '''    filas = cargar_filas()
    print("   CIFRA filas del archivo: %d" % len(filas))
    sel = elegir(filas, dominio=a.dominio, clase=a.clase, banda=a.banda,
                 desde=a.desde, hasta=a.hasta, muestra=a.muestra,
                 semilla=a.semilla)
    print("   CIFRA pares elegidos: %d" % len(sel))'''
NUEVO_S = '''    filas = cargar_filas()
    print("   CIFRA filas del archivo: %d" % len(filas))

    # EL ROJO DEL PUESTO INEXISTENTE, ANTES DE ELEGIR NADA (vuelta 178, TAREA
    # 1.d). Va delante de la seleccion a proposito: si un puesto pedido no
    # existe, lo que sale no es "una seleccion mas corta", es una peticion mal
    # escrita, y este fichero no escribe nada con ella.
    try:
        pedidos = lista_de_puestos(a.puestos)
        excluidos = lista_de_puestos(a.excluir)
    except ValueError as e:
        print("   ROJO: --puestos o --excluir no son una lista de enteros: %s" % e)
        return 1
    for etiqueta, lista in (("--puestos", pedidos), ("--excluir", excluidos)):
        if lista is None:
            continue
        if not lista:
            print("   ROJO: %s se paso vacio. Un selector que no nombra a nadie no "
                  "es un selector." % etiqueta)
            return 1
        print("   %s: %s" % (etiqueta, ", ".join(str(x) for x in lista)))
        ausentes = puestos_que_no_existen(filas, lista)
        if ausentes:
            print("   ROJO: %d puesto(s) de %s NO EXISTEN en el archivo, y NO se "
                  "escribe nada. Pedir un puesto que no esta y recibir una seleccion "
                  "mas corta en silencio es la especie que este bucle castiga:"
                  % (len(ausentes), etiqueta))
            for x in ausentes:
                print("      NO EXISTE EN EL ARCHIVO: puesto %d" % x)
            return 1
        print("      los %d existen en el archivo" % len(lista))

    sel = elegir(filas, dominio=a.dominio, clase=a.clase, banda=a.banda,
                 desde=a.desde, hasta=a.hasta, muestra=a.muestra,
                 semilla=a.semilla, puestos=pedidos, excluir=excluidos)
    print("   CIFRA pares elegidos: %d" % len(sel))'''
PARES.append((VIEJO_S, NUEVO_S))

for viejo, nuevo in PARES:
    assert viejo in t, "NO ESTA: " + viejo[:70]
    t = t.replace(viejo, nuevo, 1)

io.open(R, "w", encoding="utf-8", newline=NL).write(t)
print("PARCHES APLICADOS: %d" % len(PARES))
print("aislador_de_ciega.py -> %d bytes, %d saltos de linea"
      % (len(t.encode("utf-8")), t.count(NL)))
