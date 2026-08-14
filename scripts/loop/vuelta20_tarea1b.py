# -*- coding: utf-8 -*-
"""VUELTA 20, TAREA 1.4, segunda mitad: la TERCERA SEDE de la nomina de los 14.

ESCRIBE en docs/plan/INVENTARIO.jsonl y NADA MAS. UNA entrada tocada, UN campo,
adicion al final:

  figura LA FIRMA POSICIONAL DEL INJERTO (P.2) -> nota

MOTIVO. Al buscar la nomina en TODAS las sedes del plan (y no solo en las dos
que el encargo nombraba) aparecio docs/plan/RECORTE_POSICIONAL.md, del MISMO
11 ago 2026 que el saldo de 01_FUENTES.md, con el grupo de Horowitz en 14 Y SU
NOMINA ESCRITA. Cotejada hoy nodo por nodo con scripts/loop/vuelta20_horowitz.py
contra dataset/metadata/master_graph.json, es IDENTICA a la medida hoy, igual que
las de Coleman (15) y Hugos (21) que ese mismo doc nombra, y sus agregados
reproducen exactos (3.521 vivos, 67 con mas de un libro, 70 declaraciones en
segunda o posterior posicion).

Es la correccion de un descuido de esta misma vuelta: la primera redaccion decia
que del grupo solo habia conteos, y eso era una busqueda negativa citada sin
haber mirado todas las sedes. Lo que sigue sin estar escrito en ninguna parte es
la nomina de los TRECE.
"""
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[2]
INV = RAIZ / "docs" / "plan" / "INVENTARIO.jsonl"

TERCERA_SEDE = (
    " LA TERCERA SEDE, hallada y cotejada el 14 ago 2026 (vuelta 20), adicion al final y "
    "nada borrado: docs/plan/RECORTE_POSICIONAL.md, DEL MISMO 11 ago 2026 que el saldo de "
    "01_FUENTES.md, ya publicaba en su seccion LOS TRES QUE MAS APORTAN el grupo de "
    "Horowitz con 14 candidatos Y SU NOMINA ESCRITA. Cotejada hoy nodo por nodo con "
    "scripts/loop/vuelta20_horowitz.py contra dataset/metadata/master_graph.json, LA NOMINA "
    "DE ESE DOC Y LA MEDIDA HOY SON IDENTICAS, y lo mismo pasa con las otras dos que ese doc "
    "nombra, Coleman 15 y Hugos 21, identicas las dos; sus agregados tambien reproducen "
    "exactos, 3.521 nodos vivos, 67 con mas de un libro y 70 declaraciones en segunda o "
    "posterior posicion. CONSECUENCIA PARA LA DISCREPANCIA: el 13 de 01_FUENTES.md ya estaba "
    "contradicho EL MISMO DIA por otro documento del plan, y el 14 tiene TRES sedes "
    "(RECORTE_POSICIONAL.md, 10_INVENTARIO.md y el grafo) contra UNA. Y CORRIGE UN DESCUIDO "
    "DE ESTA MISMA VUELTA, declarado en vez de tapado: la primera redaccion de la nota de "
    "arriba y de 01_FUENTES.md decia que del grupo SOLO HABIA CONTEOS, que era una busqueda "
    "negativa citada sin mirar todas las sedes; lo que sigue sin estar escrito en ninguna "
    "parte es la nomina de los TRECE, y por eso sigue sin poderse decir cual sobra.")


def serializar(obj, modelo):
    compacto = '", "' not in modelo and '": ' not in modelo
    if compacto:
        return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return json.dumps(obj, ensure_ascii=False)


def main():
    lineas = [l for l in INV.read_text(encoding="utf-8").splitlines() if l.strip()]
    objs = [json.loads(l) for l in lineas]
    print("entradas leidas: %d" % len(objs))

    idx = [i for i, e in enumerate(objs)
           if e.get("tipo") == "figura"
           and e.get("nombre") == "LA FIRMA POSICIONAL DEL INJERTO (P.2)"]
    if len(idx) != 1:
        print("ABORTA: la figura aparece %d veces" % len(idx))
        return 1
    i = idx[0]
    viejo = dict(objs[i])
    objs[i]["nota"] = viejo["nota"] + TERCERA_SEDE
    if not objs[i]["nota"].startswith(viejo["nota"]):
        print("ABORTA: la adicion no es aditiva")
        return 1
    if {k: v for k, v in viejo.items() if k != "nota"} != {
            k: v for k, v in objs[i].items() if k != "nota"}:
        print("ABORTA: cambio otra clave")
        return 1
    print("  linea %d, nota +%d caracteres" % (i + 1, len(TERCERA_SEDE)))

    finales = [serializar(e, lineas[k]) for k, e in enumerate(objs)]
    intactas = sum(1 for k in range(len(objs)) if finales[k] == lineas[k])
    print("  lineas byte a byte identicas: %d de %d" % (intactas, len(objs)))
    if intactas != len(objs) - 1:
        print("ABORTA: %d intactas y deberian ser %d" % (intactas, len(objs) - 1))
        return 1

    salida = "\n".join(finales) + "\n"
    INV.write_text(salida, encoding="utf-8", newline="\n")
    print("ESCRITO: %s" % INV)
    for mal in (chr(8212), chr(8211)):
        if mal in salida:
            print("AVISO: hay guion largo o medio en la salida")
            return 1
    print("cero guiones largos y cero guiones medios en el archivo entero")
    return 0


if __name__ == "__main__":
    sys.exit(main())
