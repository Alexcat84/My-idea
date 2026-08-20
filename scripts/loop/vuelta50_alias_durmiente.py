# -*- coding: utf-8 -*-
"""vuelta50_alias_durmiente.py . MIDE UN ALIAS QUE NO SE IZO AL SUPERVIVIENTE.

POR QUE EXISTE: el acta de la vuelta 49 dejo una OBSERVACION SIN CAIDA que el
encargo de la vuelta 50 manda anotar en el registro del tramo (TAREA 1.3): el
absorbido `modelo_spin` cargaba a su vez el alias `modelo_spin_2`, y ese alias NO
se izo al superviviente al fundir. La regla 2 del EJECUTOR.md dice que una cifra
de un acta NUNCA es fuente de una cifra nueva: se cita como contraste y se vuelve
a medir. Esto la vuelve a medir.

CORRECCION DECLARADA SOBRE ESTE MISMO INSTRUMENTO, EN LA VUELTA EN QUE NACIO
(19 ago 2026, vuelta 50), y se deja escrita en vez de reescribir el fichero en
silencio, que es lo que la casa llama fallar calladito: la PRIMERA version leia
los campos `id` y `alias`. LOS CAMPOS DE LA CASA SON `node_id` y `ids_alias`
(scripts/loop/vuelta49_guarda_defectos.py lineas 51 y 57, leidas hoy). Con los
nombres equivocados el instrumento imprimio *declarado como alias por: nadie* y
*NO RESUELVE*, que POR CASUALIDAD se parece al hallazgo verdadero y por eso era
peligroso: una medicion que sale bien por el motivo equivocado no es una
medicion. Corregido antes de publicar cifra alguna.

QUE MIDE, y las cuatro cosas van por separado porque son cuatro preguntas:
  1. QUIEN LO DECLARA como alias, y si ese declarante esta deprecado.
  2. EL RESOLUTOR DE LA CASA (P.1 tal como lo implementa el instrumento de
     defectos): el mapa de alias se construye SOLO con los nodos VIVOS, asi que
     un alias que solo declara un deprecado NO RESUELVE. Esa es la vara que usan
     los conteos publicados.
  3. LA CADENA ANCHA: la misma caminata pero admitiendo tambien los `ids_alias`
     de los nodos deprecados. Es la que ensena a que nodo vivo LLEGARIA el alias
     si alguien lo siguiera a mano.
  4. QUIEN LO PISA: cuantas veces el alias aparece como extremo en
     `nodos_previos` o `nodos_siguientes` de cualquier nodo, y cuantas veces
     aparece como `nodo_a` o `nodo_b` en los veredictos.

UN ALIAS QUE NO RESUELVE POR LA VARA DE LA CASA NO ES UNA AVERIA HOY SI NADIE LO
PISA: es un PASIVO, de la especie que `OP-S-12` tiene encargada. Por eso la cifra
4 es la que manda y no la 2.

De solo lectura. No escribe nada.

Uso: python scripts/loop/vuelta50_alias_durmiente.py modelo_spin_2 [otro ...]
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
CAMPOS = ("nodos_previos", "nodos_siguientes")


def deprecado(d):
    return bool(d.get("deprecado") or d.get("deprecated"))


def cargar():
    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
        todos[d["node_id"]] = d
    # (2) EL MAPA DE LA CASA: solo los VIVOS declaran alias.
    alias_vivos = {}
    # (3) EL MAPA ANCHO: tambien los deprecados.
    alias_todos = {}
    for nid, d in todos.items():
        for x in (d.get("ids_alias") or []):
            alias_todos.setdefault(x, []).append(nid)
            if not deprecado(d):
                alias_vivos[x] = nid
    return todos, alias_vivos, alias_todos


def caminar(x, mapa, todos):
    """Camina con proteccion de ciclo. Devuelve (pasos, destino, nota)."""
    pasos = [x]
    visto = {x}
    actual = x
    while True:
        dueno = mapa.get(actual)
        if isinstance(dueno, list):
            if len(dueno) != 1:
                return pasos, None, ("dueno ambiguo: %s" % ", ".join(dueno)) if dueno else None
            dueno = dueno[0]
        if not dueno or dueno in visto:
            break
        visto.add(dueno)
        pasos.append(dueno)
        actual = dueno
    if actual not in todos:
        return pasos, None, "no llega a ningun fichero"
    if deprecado(todos[actual]):
        return pasos, actual, "termina en un DEPRECADO"
    return pasos, actual, None


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    objetivos = argv[1:] or ["modelo_spin_2"]
    todos, alias_vivos, alias_todos = cargar()
    vivos = sum(1 for d in todos.values() if not deprecado(d))
    print("=" * 78)
    print("ALIAS DURMIENTES, medidos hoy sobre %d nodos (%d vivos, %d deprecados)"
          % (len(todos), vivos, len(todos) - vivos))
    print("campos leidos: node_id / ids_alias (los de la casa)")
    print("=" * 78)

    veredictos = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]

    for x in objetivos:
        print()
        print("--- %s ---" % x)
        print("  1. QUIEN LO DECLARA")
        print("     es fichero propio (nodo con ese node_id): %s"
              % ("SI" if x in todos else "NO"))
        duenos = alias_todos.get(x, [])
        print("     declarado en ids_alias por: %s" % (", ".join(duenos) or "nadie"))
        for d in duenos:
            print("        %s  ->  deprecado: %s" % (d, "SI" if deprecado(todos[d]) else "NO"))

        print("  2. EL RESOLUTOR DE LA CASA (mapa de alias SOLO de nodos vivos, P.1)")
        pasos, destino, nota = caminar(x, alias_vivos, todos)
        print("     cadena: %s" % " -> ".join(pasos))
        if destino and not nota:
            print("     RESUELVE a vivo: %s" % destino)
        else:
            print("     NO RESUELVE%s" % (" (%s)" % nota if nota else ""))
            print("     o sea: para todo conteo publicado, este id se queda DONDE ESTA.")

        print("  3. LA CADENA ANCHA (admitiendo los ids_alias de los deprecados)")
        pasos2, destino2, nota2 = caminar(x, alias_todos, todos)
        print("     cadena: %s" % " -> ".join(pasos2))
        print("     llega a: %s%s" % (destino2 or "nada", " (%s)" % nota2 if nota2 else ""))
        if destino2 and not nota2:
            paso_dep = [p for p in pasos2[1:-1] if p in todos and deprecado(todos[p])]
            print("     pasa por deprecado(s): %s" % (", ".join(paso_dep) or "ninguno"))
            print("     el vivo lo carga como alias propio: %s"
                  % ("SI" if x in (todos[destino2].get("ids_alias") or [])
                     else "NO, y por eso solo llega por cadena a traves del deprecado"))

        print("  4. QUIEN LO PISA")
        refs_aristas = []
        for nid, d in todos.items():
            for c in CAMPOS:
                for v in d.get(c) or []:
                    if v == x:
                        refs_aristas.append("%s.%s" % (nid, c))
        print("     REFERENCIAS EN ARISTAS: %d %s"
              % (len(refs_aristas), refs_aristas or ""))
        refs_ver = [v.get("puesto") for v in veredictos
                    if v.get("nodo_a") == x or v.get("nodo_b") == x]
        print("     REFERENCIAS EN VEREDICTOS: %d %s" % (len(refs_ver), refs_ver or ""))
        print("     VEREDICTO DEL INSTRUMENTO: %s"
              % ("PASIVO DURMIENTE, nadie lo pisa hoy (especie OP-S-12)"
                 if not refs_aristas and not refs_ver
                 else "NO ES DURMIENTE: hay quien lo pisa, ver arriba"))

    print()
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
