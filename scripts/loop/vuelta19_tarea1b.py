# -*- coding: utf-8 -*-
"""VUELTA 19, TAREA 1.4 segunda mitad: la adicion a la figura el forastero por cableado.

Se separa en su propio script porque se escribio DESPUES: el instrumento de cierre
(scripts/loop/vuelta19_fase2.py) destapo que el primer pase de TAREA 1 registro el
candidato condicionado en la entrada de tipo acto y NO en la nota de la figura, que
es la otra mitad de lo que el encargo pedia. Queda declarado asi en vez de metido
dentro del script anterior, para que el orden real se pueda auditar.

ESCRIBE una linea de docs/plan/INVENTARIO.jsonl y NADA MAS.
"""
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[2]
INV = RAIZ / "docs" / "plan" / "INVENTARIO.jsonl"

FORASTERO = (
    " CANDIDATO CONDICIONADO ANADIDO EL 14 ago 2026 (vuelta 19) por la adjudicacion del "
    "discutible 4 de la vuelta 18, Y NO ES UN TERCER EJEMPLAR: el campo cobertura sigue "
    "en 2 y no se toca. EL CANDIDATO ES customer_validation_sales_roadmap, el nodo que le "
    "da NOMBRE al acto customer_validation_sales_roadmap, y cumple el perfil de la figura, "
    "medido con instrumento propio en esta vuelta sobre "
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl y dataset/metadata/master_graph.json: CUATRO D "
    "contra el nucleo de cuatro, que son los puestos 872 (con hoja_de_ruta_de_ventas) y "
    "1023 (con refinar_sales_roadmap) del archivo, mas LD-66 (con estrategia_de_ventas) y "
    "LD-67 (con sales_roadmap) de docs/plan/LD_SALES_ROADMAP.md; su UNICA A es el puesto "
    "319, con sales_roadmap_vs_sales_force, que es el otro nodo de la cola y no del "
    "nucleo; y sus SEIS aristas apuntan todas fuera del acto, previos "
    "producto_minimo_viable y customer_discovery_cuatro_fases, siguientes "
    "sintesis_hipotesis_modelo_negocio, vision_estrategia_producto_pivote, tipos_de_pivote "
    "y catalogo_pivotes, NINGUNO de los seis miembro del acto. POR QUE ES CANDIDATO Y NO "
    "EJEMPLAR, y la condicion va escrita entera: SI EL ACTO SE PARTE en el nucleo de "
    "cuatro mas la cola de dos, ESTE NODO DEJA DE SER FORASTERO, porque pasa a ser la "
    "mitad de su propia familia de dos, y entonces su unica A deja de ser una anomalia y "
    "pasa a ser su familia. Los dos candidatos NO son independientes y por eso ninguno se "
    "ejecuta: los decide el recomputo de fusiones por P.5 y P.8 cuando abra este acto, no "
    "esta entrada, y hoy ninguna de las 71 operaciones LISTAS los recoge. PUNTEROS: "
    "docs/plan/LD_SALES_ROADMAP.md para la evidencia, y la entrada de tipo acto con nombre "
    "customer_validation_sales_roadmap, que trae el mismo candidato con la misma condicion."
)


def serializar(obj, modelo):
    compacto = '", "' not in modelo and '": ' not in modelo
    if compacto:
        return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return json.dumps(obj, ensure_ascii=False)


def main():
    lineas = [l for l in INV.read_text(encoding="utf-8").splitlines() if l.strip()]
    objs = [json.loads(l) for l in lineas]
    idx = [i for i, e in enumerate(objs)
           if e.get("tipo") == "figura" and e.get("nombre") == "el forastero por cableado"]
    if len(idx) != 1:
        print("ABORTA: la figura aparece %d veces" % len(idx))
        return 1
    i = idx[0]
    viejo = dict(objs[i])
    objs[i]["nota"] = viejo["nota"] + FORASTERO
    resto_v = {k: v for k, v in viejo.items() if k != "nota"}
    resto_n = {k: v for k, v in objs[i].items() if k != "nota"}
    if resto_v != resto_n or not objs[i]["nota"].startswith(viejo["nota"]):
        print("ABORTA: el cambio no es aditivo o toca otra clave")
        return 1
    print("  linea %d, figura el forastero por cableado, nota +%d caracteres" % (
        i + 1, len(FORASTERO)))

    finales = [serializar(e, lineas[j]) for j, e in enumerate(objs)]
    intactas = sum(1 for j in range(len(objs)) if finales[j] == lineas[j])
    print("  lineas byte a byte identicas: %d de %d" % (intactas, len(objs)))
    if intactas != len(objs) - 1:
        print("ABORTA: %d intactas y deberian ser %d" % (intactas, len(objs) - 1))
        return 1

    salida = "\n".join(finales) + "\n"
    INV.write_text(salida, encoding="utf-8", newline="\n")
    print("ESCRITO: %s" % INV)
    prohibidos = (chr(8212), chr(8211))  # guion largo y guion medio
    for mal in prohibidos:
        if mal in salida:
            print("AVISO: hay guion largo o medio en la salida")
            return 1
    print("cero guiones largos y cero guiones medios en el archivo entero")
    return 0


if __name__ == "__main__":
    sys.exit(main())
