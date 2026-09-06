# -*- coding: utf-8 -*-
r"""_v182_parche_apertura_2.py . LAS DOS CORRECCIONES DECLARADAS DEL BLOQUE DE
APERTURA DE LA VUELTA 182, APLICADAS SOBRE EL FICHERO Y NO SOBRE SU SALIDA.

SE ESCRIBE CON NOMBRE Y NO SE TIRA porque las dos correcciones son mias y
EJECUTOR.md 8 manda declararlas sin borrar lo que corrigen. La PRIMERA CORRIDA
del bloque de apertura queda guardada entera en
docs/loop/SALIDA_V182_APERTURA_PRIMERA_CORRIDA.txt (33.313 bytes en disco), y
ahi se pueden leer las dos frases equivocadas tal como salieron.

CORRECCION 1, EL REGIMEN TECLEADO EN EL BLOQUE A. El clon del bloque de apertura
de la 181 arrastro tres lineas de prosa del sello que decian "VUELTA DE BATERIA,
Y NO LLEVA NADA MAS ... DOS sub-tareas ... El tope vuelve a cinco en la 182".
ESO ERA VERDAD DE LA 181 Y ES FALSO DE LA 182: esta vuelta NO es de bateria (la
bateria va a la 183 por decision del fundador del 5 sep 2026, PREGUNTA 4) y trae
CINCO sub-tareas, que es el tope que la propia 6.8 del acta 180 devolvia aqui.
Es exactamente la especie que EJECUTOR.md 1 persigue: una frase tecleada que
sobrevive a un clon porque nadie la mide. Se sustituye por texto que dice lo que
esta vuelta es.

CORRECCION 2, LA CLAVE DEL GRAFO ADIVINADA EN EL H.9. El bloque H.9 leia los
nodos con G.get("nodes", ...) y el fichero los guarda bajo "nodos", que ademas
es un DICCIONARIO indexado por id y no una lista. Resultado publicado en la
primera corrida: "CIFRA nodos del grafo: 0" y "cero_defectos -> NO ESTA EN EL
GRAFO DE HOY", las dos falsas. EJECUTOR.md 11 dice NO ADIVINES y aqui adivine
una clave; la reparacion no es escribir la clave buena a mano sino LISTAR LAS
CLAVES DE LA RAIZ y trabajar sobre la que exista, que es lo que hace el codigo
nuevo.

USO:
  python scripts/loop/_v182_parche_apertura_2.py
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(RAIZ, "scripts", "loop", "vuelta182_apertura.py")
NL = chr(10)

VIEJO_A = '''w("regimen: VUELTA DE BATERIA, Y NO LLEVA NADA MAS (AUDITOR.md 6.1). DOS")
w("         sub-tareas por la adjudicacion 6.8 del acta 180, la 1 BLOQUEANTE.")
w("         El tope vuelve a cinco en la 182.")'''

NUEVO_A = '''w("regimen: VUELTA ORDINARIA, NO DE BATERIA. La bateria corre CADA CINCO en")
w("         vuelta propia (AUDITOR.md 6.1) y la 181 era la suya y se corto")
w("         antes de lanzarla; esta vuelta la deja PREPARADA para la 183 por")
w("         tramos resumibles, y su seccion 9 cierra con HUECO DECLARADO Y")
w("         MEDIDO. CINCO sub-tareas, que es el tope que el acta 180 en su")
w("         6.8 devolvia a esta vuelta con estas palabras: El tope vuelve a")
w("         cinco en la 182.")'''

VIEJO_H9 = '''    G = json.load(io.open(GR, encoding="utf-8"))
    nodos = G.get("nodes", G if isinstance(G, list) else [])
    w("   CIFRA nodos del grafo: %d" % len(nodos))
    porid = {}
    for n in nodos:
        if isinstance(n, dict) and n.get("id"):
            porid[n["id"]] = n
    w("   LAS CLAVES DE UN NODO: %s"
      % ", ".join(sorted(nodos[0].keys())) if nodos else "(sin nodos)")
    for nid in ("cero_defectos", "zero_defects_concepto"):
        n = porid.get(nid)
        if n is None:
            w("   %s -> NO ESTA EN EL GRAFO DE HOY" % nid)
            continue
        pasos = n.get("pasos") or n.get("steps") or []
        w("   %s -> %d pasos" % (nid, len(pasos)))
        for k, ps in enumerate(pasos, 1):
            w("      paso %d: %s" % (k, str(ps)[:150]))'''

NUEVO_H9 = '''    G = json.load(io.open(GR, encoding="utf-8"))
    w("   LAS CLAVES DE LA RAIZ, LISTADAS Y NO ADIVINADAS: %s"
      % ", ".join(sorted(G.keys()) if isinstance(G, dict) else ["(no es dict)"]))
    porid = nodos_por_id(G)
    w("   CIFRA nodos del grafo, contados de la clave que existe: %d" % len(porid))
    if porid:
        una = sorted(porid)[0]
        w("   LAS CLAVES DE UN NODO (%s): %s"
          % (una, ", ".join(sorted(porid[una].keys()))))
    for nid in ("cero_defectos", "zero_defects_concepto"):
        n = porid.get(nid)
        if n is None:
            w("   %s -> NO ESTA EN EL GRAFO DE HOY" % nid)
            continue
        pasos = pasos_del_nodo(n)
        w("   %s -> %d pasos" % (nid, len(pasos)))
        for k, ps in enumerate(pasos, 1):
            w("      paso %d: %s" % (k, str(ps)[:170]))'''

# LAS DOS FUNCIONES NUEVAS, que se meten junto a las demas ayudas del fichero y
# NO dentro del bloque de impresion, para que el instrumento del diferenciador
# movido (TAREA 3) las pueda importar en vez de copiarlas.
ANCLA_FUNCION = '''def escribir(nombre, texto):'''

FUNCIONES = '''def nodos_por_id(grafo):
    """LOS NODOS DEL GRAFO INDEXADOS POR ID, SIN ADIVINAR LA CLAVE DE LA RAIZ.

    Prueba las formas que el fichero puede tener y devuelve la primera que da
    nodos: la clave `nodos` como diccionario id -> nodo (que es la que este
    repo usa hoy), la misma clave como lista, y `nodes` en las dos formas por
    si el fichero cambia de idioma. Si ninguna da nada, devuelve {} y quien
    llame publica el cero, que es una medicion y no un adivinanza."""
    if not isinstance(grafo, dict):
        return {}
    for clave in ("nodos", "nodes"):
        v = grafo.get(clave)
        if isinstance(v, dict) and v:
            return {k: n for k, n in v.items() if isinstance(n, dict)}
        if isinstance(v, list) and v:
            return {n.get("id"): n for n in v
                    if isinstance(n, dict) and n.get("id")}
    return {}


def pasos_del_nodo(nodo):
    """LOS PASOS DE UN NODO, POR LA MISMA REGLA: la clave que exista, y si no
    existe ninguna, lista vacia."""
    if not isinstance(nodo, dict):
        return []
    for clave in ("pasos", "steps"):
        v = nodo.get(clave)
        if isinstance(v, list):
            return v
    return []


'''


def main():
    t = io.open(P, encoding="utf-8").read()
    for viejo, nuevo, nombre in ((VIEJO_A, NUEVO_A, "CORRECCION 1, el regimen"),
                                 (VIEJO_H9, NUEVO_H9, "CORRECCION 2, la clave")):
        if viejo not in t:
            raise SystemExit("ROJO: no se encontro el trozo de %s" % nombre)
        t = t.replace(viejo, nuevo, 1)
        print("APLICADA: %s" % nombre)
    if ANCLA_FUNCION not in t:
        raise SystemExit("ROJO: no se encontro el ancla de las funciones")
    t = t.replace(ANCLA_FUNCION, FUNCIONES + ANCLA_FUNCION, 1)
    print("APLICADA: las dos funciones nuevas, nodos_por_id y pasos_del_nodo")
    io.open(P, "w", encoding="utf-8", newline=NL).write(t)
    print("bytes ahora: %d | lineas: %d" % (len(t.encode("utf-8")), t.count(NL)))


if __name__ == "__main__":
    main()
