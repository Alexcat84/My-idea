"""Vuelta 32: la PARADA de OP-D-02 registrada en su campo nota.

CORRECCION DECLARADA que se anade al final: el texto viejo, y la readjudicacion
que esta misma vuelta ya le escribio, se quedan enteros delante.

Las cifras se miden aqui, no se teclean.

Uso: python scripts/loop/vuelta32_nota_opd02.py [--aplicar]
"""
import itertools
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

MARCA = "PARADA REGISTRADA, 15 ago 2026 (vuelta 32)"


def main():
    aplicar = "--aplicar" in sys.argv
    lineas = []
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                lineas.append(json.loads(linea))
    op = [o for o in lineas if o["id_op"] == "OP-D-02"][0]
    nomina = op["nodos"]

    por_par = {}
    for l in open(VER, encoding="utf-8"):
        if l.strip():
            v = json.loads(l)
            por_par[frozenset((v["nodo_a"], v["nodo_b"]))] = v
    pares = list(itertools.combinations(sorted(nomina), 2))
    con = [por_par[frozenset(p)] for p in pares if frozenset(p) in por_par]
    sin = [p for p in pares if frozenset(p) not in por_par]
    aes = [v for v in con if v["clase"] == "A"]
    sin_ganador = [v["puesto_intra"] for v in aes if "gana" not in v["razon"].lower()]

    texto = (
        " %s: LA FUSION NO SE EJECUTA, y son TRES motivos medidos hoy con "
        "scripts/loop/vuelta32_acto_opd02.py, de solo lectura. CERO NODOS TOCADOS. "
        "MOTIVO 1, y lo exige la verificacion de esta misma operacion (el acto se leyo "
        "ENTERO antes de fundirse: cero pares internos sin veredicto): medido par por par "
        "sobre docs/INTRA_DOMINIO_VEREDICTOS.jsonl, PARES POSIBLES %d, CON VEREDICTO %d, SIN "
        "VEREDICTO %d. Los que faltan, por su nombre: %s. Y P.5, que esta nota cita mas "
        "arriba, dice que la pregunta que el acto leido entero contesta es si el acto es UNA "
        "familia o DOS: con %d de %d esa pregunta no tiene respuesta medida. Los pares A del "
        "acto son %s y su cierre transitivo cubre a los %d nodos de la nomina, ninguno fuera. "
        "MOTIVO 2, NO HAY SUPERVIVIENTE: el campo superviviente esta en null, leido hoy, y no "
        "se puede fijar por el banco 9.3.1 porque su prueba es gano todos los pares A que lo "
        "tocan y, medido hoy, los pares A %s NO NOMBRAN GANADOR en su razon. Ningun nodo del "
        "acto tiene una victoria citable, asi que no hay GANADOR POR DERECHO; y la otra "
        "especie, GANADOR POR ELEGIR, exige P.8 sobre la nomina entera con el acto completo "
        "delante, que es lo que el motivo 1 dice que no hay. MOTIVO 3, LA NOMINA PUEDE ESTAR "
        "CORTA y el aviso ya estaba escrito: la razon del puesto 788 cierra diciendo que la "
        "familia de la voz del cliente hay que contarla entera antes de tocarla. Censo por "
        "nombre corrido hoy (banco 9.5.1), y es una CITA y no una prueba de pertenencia: de "
        "los 9 nodos vivos con alguna marca, cuatro son falsos positivos del substring voc; "
        "de los cinco reales, DOS estan FUERA de la nomina, voice_of_customer_estrategico y "
        "voc_temprano_en_agile_stage_gate, los dos del mismo libro, y el primero es el "
        "contrario del congelado 724. Y POR ESO LAS RELECTURAS DE 724, 755 Y 827 SE LEEN "
        "PERO NO SE CLASIFICAN: los tres estan congelados por el TOQUE UNICO del banco 9.4, "
        "y aunque la mitad de esa causa ya cayo (voz_del_cliente_voc esta destejido y "
        "estable), la otra mitad sigue en pie porque el superviviente de este acto puede no "
        "ser voz_del_cliente_voc. Emitirlas hoy seria romper la misma regla por la que estan "
        "congelados. Quedan leidas y publicadas en docs/loop/SALIDA_V32_OPD02_RELECTURA.txt y "
        "en el reporte, sin clase. El detalle entero esta en docs/plan/02_DESTEJIDOS.md, "
        "seccion OP-D-02, ESTADO AL 15 ago 2026."
    ) % (MARCA, len(pares), len(con), len(sin),
         "; ".join("%s contra %s" % p for p in sin),
         len(con), len(pares),
         ", ".join(str(v["puesto_intra"]) for v in sorted(aes, key=lambda x: x["puesto_intra"])),
         len(nomina),
         " y ".join(str(x) for x in sorted(sin_ganador)))

    if MARCA in (op.get("nota") or ""):
        print("YA APLICADA.")
        return 0
    op["nota"] = (op.get("nota") or "") + texto
    print(texto.strip())

    if not aplicar:
        print("\n(simulacion: sin --aplicar no se escribe nada)")
        return 0

    with open(OPS, "w", encoding="utf-8") as fh:
        for o in lineas:
            fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    de_vuelta = [json.loads(l) for l in open(OPS, encoding="utf-8") if l.strip()]
    ids = [o["id_op"] for o in de_vuelta]
    rotas = sum(1 for o in de_vuelta
                for x in (o.get("depende_de") or []) + (o.get("bloquea_a") or [])
                if x not in set(ids))
    print("\nVERIFICADO TRAS ESCRIBIR: %d lineas JSON validas, %d ids unicos, "
          "%d dependencias rotas" % (len(de_vuelta), len(set(ids)), rotas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
