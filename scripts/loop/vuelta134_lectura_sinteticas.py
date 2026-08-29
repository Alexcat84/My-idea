# -*- coding: utf-8 -*-
"""vuelta134_lectura_sinteticas.py . TAREA 4.d de la vuelta 134.

Lee, una por una, las CINCO canonicas SINTETICAS que produce la cola
extendida a `Caps?.` (medidas en 4.b/4.c: tres de ellas SI quedan
marcadas SINTETICA por vuelta133_tabla_mapeo_propuesto.calcular() porque
son grupos de 2+ miembros sin ningun libro; las otras DOS, Cullinane y la
grafia malformada, son grupos de UN SOLO miembro y por eso calcular() no
las marca SINTETICA, aunque su forma recortada tampoco es un titulo de
libro: se leen las cinco igual, con la discrepancia declarada).

Para cada una: la canonica que produciria recortar_extendida(), y una linea
diciendo si eso es un titulo de libro legible o no. La quinta (la grafia
malformada) se mira ademas con DOS preguntas medidas y ninguna supuesta:
(1) que canonica saldria si la cola la cortase, (2) si sus acentos estan
bien en el dato o estan rotos (leido con encoding utf-8 explicito).

Salida: docs/loop/SALIDA_V134_4D_SINTETICAS.txt

USO:
  python scripts/loop/vuelta134_lectura_sinteticas.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta131_grupos_por_titulo import cargar_censo  # noqa: E402
from vuelta134_efecto_cap_abreviado import recortar_extendida  # noqa: E402

CANDIDATAS = [
    "Edwards et al., Managing Project Risks, Cap. 12; Hubbard, The Failure of Risk Management, Cap. 13; DeMarco y Lister, Waltzing with Bears",
    "DeMarco y Lister, Waltzing with Bears, Cap. 14 y 20-21 (Risk Reserve)",
    "Hubbard, The Failure of Risk Management, Cap. 3, 11 y 12 (Measuring and Improving Risk Management)",
    "Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment)",
    "Síntesis del método aplicado al emprendedor individual (riesgo de rotación, Waltzing with Bears, Cap. 13, llevado a un proyecto de una sola persona)",
]


def es_titulo_legible(canonica):
    """Heuristica DECLARADA, no oculta: una canonica que termina en coma,
    punto y coma, o que trae un parentesis sin cerrar (mas '(' que ')'), NO
    es un titulo de libro legible."""
    c = canonica.strip()
    if c.endswith((",", ";", ":")):
        return False, "termina en puntuacion de continuacion, no de titulo"
    if c.count("(") != c.count(")"):
        return False, "parentesis desbalanceado (%d '(' contra %d ')')" % (c.count("("), c.count(")"))
    return True, "titulo de libro legible"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    censo = cargar_censo()

    for i, g in enumerate(CANDIDATAS, 1):
        if g not in censo:
            print("%d. %r: NO ESTA EN EL CENSO DE HOY (discrepancia con lo esperado)" % (i, g))
            continue
        canonica = recortar_extendida(g)
        legible, motivo = es_titulo_legible(canonica)
        print("%d. grafia: %r" % (i, g))
        print("   canonica que produciria: %r" % canonica)
        print("   %s: %s" % ("LEGIBLE" if legible else "NO LEGIBLE", motivo))
        print("")

    quinta = CANDIDATAS[4]
    print("QUINTA, LAS DOS PREGUNTAS MEDIDAS (no supuestas):")
    canonica_quinta = recortar_extendida(quinta)
    print("  (1) canonica si la cola la cortase: %r" % canonica_quinta)

    raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ruta_nodo = os.path.join(raiz, "dataset", "nodos", "el_riesgo_eres_tu.json")
    with open(ruta_nodo, "rb") as f:
        crudo = f.read()
    tiene_fffd_en_bytes = b"\xef\xbf\xbd" in crudo
    import json
    decodificado = json.loads(crudo.decode("utf-8"))["fuente"]
    tiene_fffd_en_texto = "�" in decodificado
    print("  (2) acentos en el dato, medido en `%s` (bytes crudos y texto decodificado "
          "con utf-8 explicito, no por como se ve en una consola):" % ruta_nodo)
    print("      bytes crudos traen la codificacion UTF-8 de U+FFFD: %s" % tiene_fffd_en_bytes)
    print("      texto decodificado trae el codepoint U+FFFD: %s" % tiene_fffd_en_texto)
    print("      CONCLUSION: %s" %
          ("los acentos estan ROTOS en el dato" if (tiene_fffd_en_bytes or tiene_fffd_en_texto)
           else "los acentos estan BIEN en el dato; el '?' visto en consola sin "
                "reconfigurar a utf-8 era un artefacto de terminal, no del dato"))

    print("")
    print("EXITCODE: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
