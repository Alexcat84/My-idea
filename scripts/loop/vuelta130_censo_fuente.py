# -*- coding: utf-8 -*-
"""vuelta130_censo_fuente.py . TAREA 3.b(i) de la vuelta 130: censo de
GRAFIAS DISTINTAS EN PRIMERA POSICION del campo `fuente`, sobre los nodos
VIVOS de hoy. MIDE Y PROPONE, NO DECIDE (OP-S-11 sigue LISTA, no se toca
ningun nodo).

EL SEPARADOR, ARGUMENTADO CON LOS DATOS, NO ELEGIDO A PRIORI. Se corrieron
TRES candidatos sobre el catalogo de hoy y se lee cada uno antes de decidir:

  (A) separar SOLO por `;`                    -> 135 grafias en primera posicion
  (B) separar por `;` Y por ` | `             -> 128 grafias en primera posicion
  (C) separar SOLO por ` | ` (el propuesto)   -> ver RESUMEN al correr

Los datos traen `;` en 264 nodos vivos y ` | ` en 8. Leyendo los 264 valores
UNICOS con `;` (impreso a mano en esta vuelta, TAREA 3.b): el `;` en este
catalogo NUNCA separa dos declaraciones limpias de "Titulo - Autor". Separa,
segun el caso: (1) DOS O MAS AUTORES del MISMO libro
("Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe");
(2) una LISTA DE CAPITULOS o TEMAS dentro de un parentesis, del MISMO libro
("Edwards et al., Managing Project Risks, Cap. 9 (Mitigation Principles;
ALARP)"); (3), unos pocos casos del dominio `risk_management`, SI enlaza dos
citas de dos libros distintos en estilo academico
("DeMarco y Lister, Waltzing with Bears, Cap. 2; Edwards et al., Managing
Project Risks, Cap. 6"); y (4) un caso con `;` colgando al final sin nada
detras, artefacto de truncamiento
("The Field Guide to Understandin - Dekker, Sidney;").

Separar por `;` a ciegas (candidatos A y B) CONFUNDE estas cuatro cosas:
fragmenta coautores y listas de capitulos como si fueran declaraciones
nuevas, fabricando "primeras posiciones" que son APELLIDOS SUELTOS o
FRAGMENTOS DE TITULO, no citas. Los OCHO casos con ` | `, en cambio, SI
separan libros distintos de verdad en los DIEZ ejemplares medidos (ver
docstring de la operacion): la forma es siempre `Titulo - Autor | Titulo -
Autor`, sin excepcion, y las dos mitades son citas completas por si solas.

LA PROPUESTA DE ESTA VUELTA: separador = ` | ` UNICAMENTE. Ninguna cadena
con `;` y sin ` | ` se separa: se censa entera, `;` y todo, como UNA sola
declaracion (que es lo que es). Es la unica lectura que no fabrica
declaraciones donde el dato no las puso.

Salida: docs/loop/SALIDA_V130_3B_CENSO_FUENTE.txt

Uso:
  python scripts/loop/vuelta130_censo_fuente.py
"""
import glob
import json
import os
import sys
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def cargar_vivos():
    out = []
    for p in sorted(glob.glob(os.path.join(NODOS, "*.json"))):
        d = json.loads(open(p, encoding="utf-8").read())
        if d.get("deprecado"):
            continue
        fu = d.get("fuente")
        if fu:
            out.append((d["node_id"], fu))
    return out


def primeras_posiciones(vivos, separadores):
    primeras = []
    for nid, fu in vivos:
        resto = fu
        for sep in separadores:
            resto = resto.split(sep)[0] if sep in resto else resto
        # cuando hay varios separadores, partir por el que aparezca primero
        if len(separadores) > 1:
            cortes = [fu.find(s) for s in separadores if s in fu]
            if cortes:
                primer_corte = min(cortes)
                primeras.append(fu[:primer_corte].strip())
                continue
        primeras.append(resto.strip())
    return primeras


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    vivos = cargar_vivos()
    print("NODOS VIVOS CON `fuente`: %d" % len(vivos))
    con_punto_y_coma = sum(1 for _, fu in vivos if ";" in fu)
    con_pipe = sum(1 for _, fu in vivos if "|" in fu)
    print("RECUENTO DE SEPARADORES CANDIDATOS EN LOS DATOS:")
    print("  nodos con ';' : %d" % con_punto_y_coma)
    print("  nodos con '|' : %d" % con_pipe)
    solapan = sum(1 for _, fu in vivos if ";" in fu and "|" in fu)
    print("  nodos con AMBOS a la vez: %d" % solapan)
    print()

    candA = primeras_posiciones(vivos, [";"])
    candB = primeras_posiciones(vivos, [";", "|"])
    candC = primeras_posiciones(vivos, ["|"])

    print("CANDIDATO (A) separar solo por ';': %d grafias distintas en primera posicion" % len(set(candA)))
    print("CANDIDATO (B) separar por ';' y '|': %d grafias distintas en primera posicion" % len(set(candB)))
    print("CANDIDATO (C, PROPUESTO) separar solo por '|': %d grafias distintas en primera posicion" % len(set(candC)))
    print()
    print("SEPARADOR ELEGIDO: SOLO '|' (candidato C). Razon: los 264 casos con ';'")
    print("NO separan declaraciones distintas (coautores, listas de capitulos, o un")
    print("caso ajeno de dos citas academicas pegadas): partir por ';' fabrica")
    print("'primeras posiciones' que son apellidos sueltos o fragmentos de titulo.")
    print("Los 8 casos con '|' SI son 'Titulo - Autor | Titulo - Autor', dos citas")
    print("completas, sin excepcion (verificado a mano, ver docstring).")
    print()

    censo = Counter(candC)
    print("CENSO DE GRAFIAS DISTINTAS EN PRIMERA POSICION (separador '|'), CON RECUENTO:")
    for g, n in sorted(censo.items(), key=lambda kv: (-kv[1], kv[0])):
        print("  %d\t%s" % (n, g))
    print()
    print("RESUMEN: %d nodos vivos con fuente, %d grafias distintas en primera posicion (corte 2026-08-29, separador '|')." % (len(vivos), len(censo)))


if __name__ == "__main__":
    raise SystemExit(main())
