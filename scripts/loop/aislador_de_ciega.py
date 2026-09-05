# -*- coding: utf-8 -*-
r"""aislador_de_ciega.py . ELIGE Y AISLA EL SUJETO DE UNA RELECTURA CIEGA ANTES
DE QUE NADIE MIRE NADA.

NOMBRE ESTABLE A PROPOSITO, sin numero de vuelta, como
`tallar_cabecera_reporte.py`, `verificar_apertura_sellada.py` y
`archivar_reporte.py`: se usa en toda vuelta y no se clona.

POR QUE NACE (adjudicacion 6.1 del acta 169, TAREA BLOQUEANTE, y la `CAIDA 1`
de esa misma acta). DOS TURNOS DE AUDITOR SEGUIDOS QUEMARON SU SUJETO DE CIEGA:
el acta 168 leyo el destape de una sesion cortada, y el acta 169 corrio un
`grep` de verificacion sobre el mismo documento que iba a leer a ciegas. La
regla que lo cierra ya esta escrita: **EL SUJETO DE LA CIEGA SE ELIGE Y SE
AISLA ANTES DEL PRIMER COMANDO DE VERIFICACION.** Lo que faltaba es que dejara
de depender de que alguien se acuerde, y eso es este fichero.

QUE HACE, Y EN QUE ORDEN, QUE ES LO QUE IMPORTA:
  1. RECIBE UN CRITERIO ESCRITO (`--criterio`), obligatorio. Sin criterio no
     corre. El criterio se copia LITERAL a los dos ficheros, para que despues
     no se pueda discutir por que se eligieron esos pares y no otros.
  2. ELIGE LOS PARES con selectores deterministas sobre
     `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (dominio, clase, banda, rango de
     puestos, LISTA DE PUESTOS, LISTA DE EXCLUIDOS, muestra con semilla). La
     muestra usa `random.Random(semilla)`, asi que la misma semilla da los
     mismos pares y la eleccion se puede reproducir.
  3. ESCRIBE LA SALIDA CIEGA con SOLO `puesto_intra`, `nodo_a`, `nodo_b` y los
     PASOS de los dos nodos. Los campos NO se filtran quitando los prohibidos:
     se CONSTRUYEN uno a uno desde una LISTA BLANCA (`CAMPOS_CIEGOS`). La
     diferencia no es de estilo: una lista negra se queda ciega ante un campo
     nuevo, una lista blanca no.
  4. ESCRIBE EL DESTAPE (clase y razon) EN UN FICHERO APARTE, que no hace falta
     abrir hasta tener las clases escritas.
  5. ANTES DE ESCRIBIR NADA, PASA LA GUARDA DE FUGA: comprueba que ningun valor
     de `clase` ni de `razon` de los pares elegidos aparece en el texto ciego.
     Si alguno aparece, CAE EN ROJO y NO ESCRIBE NINGUNO DE LOS DOS FICHEROS.

EL CARRIL POR LISTA DE PUESTOS (vuelta 178, TAREA 1.d), Y POR QUE HACIA FALTA.
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

LO QUE NO HACE, DICHO PARA QUE NADIE LEA DE MAS: no adjudica clases, no toca
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (lo abre en modo lectura), no mueve el
marcador y no decide si una lectura es correcta. Solo reparte lo que se puede
mirar y lo que no, y deja constancia de que lo repartio antes de mirar.

SUS CASOS POSITIVOS POR MUTACION SON DOS, y ninguno sustituye al otro:
`scripts/loop/vuelta170_tarea2a_mutacion_aislador.py`, que CAE si el destape se
cuela en la salida ciega o si la lista blanca se ensancha para dejarlo pasar; y
`scripts/loop/vuelta178_tarea1d_mutacion_puestos.py`, que prueba el carril por
lista de puestos, su composicion con los selectores viejos, y EL ROJO DEL PUESTO
INEXISTENTE.

USO:
  python scripts/loop/aislador_de_ciega.py --criterio "los 8 pares de compras de la banda" \
      --dominio compras --banda --ciega docs/loop/_v170_ciega.txt \
      --destape docs/loop/_v170_destape.txt
  python scripts/loop/aislador_de_ciega.py --criterio "muestra de 10 sobre todo el archivo" \
      --muestra 10 --semilla 170 --ciega A.txt --destape B.txt
  python scripts/loop/aislador_de_ciega.py --criterio "los discutibles de la 177" \
      --puestos 334,394,404 --excluir 878 --ciega A.txt --destape B.txt

SALIDA: exit 0 si aisla; exit 1 en cualquier rojo, sin escribir nada.
"""
import argparse
import io
import json
import os
import random
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

# LA LISTA BLANCA. Lo que la salida ciega puede llevar, y nada mas. No es una
# lista de exclusiones: los campos se copian UNO A UNO desde aqui, asi que un
# campo nuevo en el archivo NO aparece solo.
CAMPOS_CIEGOS = ("puesto_intra", "nodo_a", "nodo_b")

# LOS CAMPOS DEL DESTAPE. Lo que la guarda de fuga busca en el texto ciego.
CAMPOS_DESTAPE = ("clase", "razon")


def cargar_filas(ruta=None):
    filas = []
    for l in io.open(ruta or VEREDICTOS, encoding="utf-8"):
        if l.strip():
            filas.append(json.loads(l))
    return filas


def cargar_pasos(ruta=None):
    """{id_nodo: [pasos]}. Solo los pasos: el aislador no necesita mas del
    grafo y cuanto menos cargue, menos puede filtrar."""
    g = json.load(io.open(ruta or GRAFO, encoding="utf-8"))["nodos"]
    return dict((k, list(v.get("pasos_accionables") or [])) for k, v in g.items())


def lista_de_puestos(texto):
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
    sel = list(filas)
    if dominio:
        sel = [f for f in sel if f.get("dominio") == dominio]
    if clase:
        sel = [f for f in sel if f.get("clase") == clase]
    if banda:
        sel = [f for f in sel if f.get("banda_078_080")]
    if desde is not None:
        sel = [f for f in sel if f.get("puesto_intra", 0) >= desde]
    if hasta is not None:
        sel = [f for f in sel if f.get("puesto_intra", 0) <= hasta]
    if puestos:
        pedidos = set(puestos)
        sel = [f for f in sel if f.get("puesto_intra") in pedidos]
    if excluir:
        fuera = set(excluir)
        sel = [f for f in sel if f.get("puesto_intra") not in fuera]
    sel.sort(key=lambda f: f.get("puesto_intra", 0))
    if muestra is not None and muestra < len(sel):
        sel = sorted(random.Random(semilla).sample(sel, muestra),
                     key=lambda f: f.get("puesto_intra", 0))
    return sel


def texto_ciego(filas, pasos, criterio, campos=CAMPOS_CIEGOS):
    """EL TEXTO QUE EL LECTOR VE. Se CONSTRUYE campo a campo desde `campos`,
    nunca copiando la fila y quitando lo prohibido.

    `campos` es parametro a proposito: el caso por mutacion lo ensancha para
    comprobar que la guarda de fuga MUERDE."""
    out = []
    out.append("=" * 78)
    out.append("SUJETO DE CIEGA, AISLADO ANTES DEL PRIMER COMANDO DE VERIFICACION")
    out.append("instrumento: scripts/loop/aislador_de_ciega.py")
    out.append("=" * 78)
    out.append("")
    out.append("CRITERIO ESCRITO (literal, tal como se paso):")
    out.append("   " + criterio)
    out.append("")
    out.append("CIFRA pares elegidos: %d" % len(filas))
    out.append("CAMPOS QUE ESTA SALIDA LLEVA (lista blanca): %s" % ", ".join(campos))
    out.append("")
    for f in filas:
        out.append("-" * 78)
        for c in campos:
            out.append("%s: %s" % (c, f.get(c)))
        for rol, clave in (("A", "nodo_a"), ("B", "nodo_b")):
            nid = f.get(clave)
            ps = pasos.get(nid)
            if ps is None:
                out.append("  pasos de %s (%s): EL NODO NO ESTA EN EL GRAFO" % (rol, nid))
                continue
            out.append("  pasos de %s (%s): %d" % (rol, nid, len(ps)))
            for i, p in enumerate(ps, 1):
                out.append("     paso %d: %s" % (i, p))
    out.append("-" * 78)
    out.append("FIN DE LA SALIDA CIEGA. El destape vive en OTRO fichero.")
    return "\n".join(out) + "\n"


def texto_destape(filas, criterio, campos=CAMPOS_DESTAPE):
    out = []
    out.append("=" * 78)
    out.append("DESTAPE DEL SUJETO DE CIEGA. NO SE ABRE HASTA TENER LAS CLASES ESCRITAS.")
    out.append("instrumento: scripts/loop/aislador_de_ciega.py")
    out.append("=" * 78)
    out.append("")
    out.append("CRITERIO ESCRITO (el mismo que la salida ciega lleva):")
    out.append("   " + criterio)
    out.append("")
    out.append("CIFRA pares: %d" % len(filas))
    out.append("")
    for f in filas:
        out.append("-" * 78)
        out.append("puesto_intra: %s" % f.get("puesto_intra"))
        for c in campos:
            out.append("%s: %s" % (c, f.get(c)))
    out.append("-" * 78)
    out.append("FIN DEL DESTAPE.")
    return "\n".join(out) + "\n"


def fugas(ciego, filas, campos=CAMPOS_DESTAPE):
    """LA GUARDA. [(puesto, campo)] de todo valor de destape que se pueda leer
    en el texto ciego. Pura: no toca disco.

    Las clases son letras sueltas (`A`, `B`, `C`, `D`) y aparecerian por azar en
    cualquier prosa, asi que se buscan en la FORMA EN QUE EL DESTAPE LAS
    ESCRIBE (`clase: X`), que es como se colarian de verdad si alguien las
    metiera en la lista blanca. Las razones son texto largo y se buscan
    enteras."""
    encontradas = []
    for f in filas:
        for c in campos:
            v = f.get(c)
            if v is None or not str(v).strip():
                continue
            aguja = ("%s: %s" % (c, v)) if len(str(v)) <= 3 else str(v)
            if aguja in ciego:
                encontradas.append((f.get("puesto_intra"), c))
    return encontradas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--criterio", required=True,
                    help="el criterio ESCRITO por el que se eligen los pares")
    ap.add_argument("--ciega", required=True, help="ruta de la salida ciega")
    ap.add_argument("--destape", required=True, help="ruta del destape, APARTE")
    ap.add_argument("--dominio")
    ap.add_argument("--clase")
    ap.add_argument("--banda", action="store_true")
    ap.add_argument("--desde", type=int)
    ap.add_argument("--hasta", type=int)
    ap.add_argument("--muestra", type=int)
    ap.add_argument("--semilla", type=int, default=0)
    ap.add_argument("--puestos",
                    help="LISTA DE PUESTOS separada por comas, por ejemplo "
                         "334,394,404. Se queda SOLO con esos, y se aplica DESPUES "
                         "de los demas selectores. CAE EN ROJO si alguno no existe "
                         "en el archivo.")
    ap.add_argument("--excluir",
                    help="LISTA DE PUESTOS que se quitan de la seleccion, por "
                         "ejemplo 878. Mismo rojo que --puestos si alguno no "
                         "existe.")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("AISLADOR DE CIEGA")
    print("=" * 78)
    print("   criterio: %s" % a.criterio)

    if os.path.abspath(a.ciega) == os.path.abspath(a.destape):
        print("   ROJO: la salida ciega y el destape no pueden ser el mismo fichero.")
        return 1

    filas = cargar_filas()
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
    print("   CIFRA pares elegidos: %d" % len(sel))
    if not sel:
        print("   ROJO: el criterio no elige ningun par. No se escribe nada.")
        return 1
    print("   puestos: %s" % ", ".join(str(f.get("puesto_intra")) for f in sel))

    pasos = cargar_pasos()
    ciego = texto_ciego(sel, pasos, a.criterio)
    destape = texto_destape(sel, a.criterio)

    escapes = fugas(ciego, sel)
    print("   CIFRA fugas del destape en la salida ciega: %d" % len(escapes))
    if escapes:
        print("   ROJO, el destape se cuela en la salida ciega y NO se escribe nada:")
        for puesto, campo in escapes:
            print("      puesto %s, campo %s" % (puesto, campo))
        return 1

    io.open(a.ciega, "w", encoding="utf-8", newline="\n").write(ciego)
    io.open(a.destape, "w", encoding="utf-8", newline="\n").write(destape)
    print("")
    print("   VERDE. El sujeto queda aislado ANTES de mirar nada.")
    print("      salida ciega: %s (%d bytes)"
          % (a.ciega, len(ciego.encode("utf-8"))))
    print("      destape:      %s (%d bytes)  NO ABRIR hasta tener las clases"
          % (a.destape, len(destape.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
