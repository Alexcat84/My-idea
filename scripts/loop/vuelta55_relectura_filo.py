# -*- coding: utf-8 -*-
"""vuelta55_relectura_filo.py . CONSTRUYE EL LOTE DE LA RELECTURA DEL FILO DE LA
VUELTA 55, POR EL CARRIL GENERAL DE COLISIONES DE docs/plan/03_FUSIONES.md.

MISMA MAQUINA que scripts/loop/vuelta49_relectura_colisiones.py, con su misma
guarda: la razon vieja se LEE DEL ARCHIVO y se pega POR MAQUINA dentro de la
nueva, y si no queda literal dentro, aborta sin escribir el lote. Transcribir a
mano un parrafo de miles de caracteres es exactamente donde nace una errata, y
una correccion que tapa lo que corrige no se puede auditar (banco 9.10).

LO QUE ESTE INSTRUMENTO NO HACE: no decide. La cabecera es la lectura del
ejecutor de la vuelta 55 y se lee y se discute como tal.

De solo lectura sobre el archivo de veredictos: escribe el LOTE, no el archivo.
El archivo lo escribe scripts/corregir_veredicto.py, que es el carril adjudicado.

Uso: python scripts/loop/vuelta55_relectura_filo.py --salida docs/loop/_lote_v55_filo.jsonl
"""
import argparse
import io
import json
import sys

VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"

CAB = {}

CAB[218] = ("D", """CORRECCION DECLARADA EL 20 ago 2026 (vuelta 55), POR RELECTURA DEL FILO EN EL MISMO ACTO, encargada por el encargo 2.3 y corrida por el carril general de colisiones de docs/plan/03_FUSIONES.md con sus dos ampliaciones de la vuelta 54. LA CLASE CAMBIA: DE B A D. POR QUE ESTE PAR ENTRA A RELECTURA: el acto 44 del tramo 2 de OP-U-01 funde formalizacion_acuerdo_equity dentro de reparto_inicial_equity, y al resolver, el par de ESTE puesto (reparto_inicial_equity contra timing_equity_split, clase B) y el del puesto 1008 (formalizacion_acuerdo_equity contra timing_equity_split, clase D) pasan a ser EL MISMO PAR RESUELTO con DOS CLASES. La colision estaba PREDICHA y NOMBRADA antes de tocar un nodo, con sus dos puestos impresos, en docs/loop/SALIDA_V55_COLISIONES_ESPERADAS_TRAMO2.txt. El veredicto arrastrado es del FILO, una B, asi que por el acta de la vuelta 51 (pregunta 2) NO se voltea por maquina: se RELEE el par resuelto con el veredicto directo como contraste. LA CONDICION QUE ESTA RELECTURA TIENE QUE DESCARGAR ES DE CONTEO Y COBERTURA, que la ampliacion registrada en la vuelta 54 declara carril de TEXTO en sentido amplio y manda descargar MIDIENDO ANTES de fundir, y eso es lo que se hizo. LA MEDICION, contra los ficheros de hoy: reparto_inicial_equity tiene CUATRO pasos y de ellos UNO SOLO habla del momento, el paso 1, Espera a que la estrategia de tu negocio y quienes forman tu equipo se estabilicen antes de cerrar el reparto final. Es UNA LINEA. timing_equity_split tiene CUATRO pasos y LOS CUATRO son el momento, y son un PROCEDIMIENTO: hablar con los socios sobre si conviene dividir de inmediato o esperar a tener mas informacion sobre las contribuciones reales; si se decide esperar, fijar un momento claro, por ejemplo antes de levantar la primera ronda; pesar el riesgo de perder a un cofundador valioso si no se le ofrece equity pronto; y evitar dejar la negociacion para cuando ya exista una valoracion externa, porque eso eleva la tension. TRES de esos cuatro pasos no estan en la madre en ninguna forma. LA VARA DEL BANCO 9.6.1, LA LINEA O EL PROCEDIMIENTO, DEVUELVE CONTINUA Y NO REPITE: contra una linea de la madre, el hijo trae un procedimiento de cuatro decisiones. D. Y LA PROPIA RAZON VIEJA YA LO ESCRIBIA con estas palabras, El segundo profundiza el cuando del primero, que es la definicion misma de CONTINUA; lo que le faltaba a aquella lectura no era el dato sino la vara, y por eso quedo marcada DUDOSO en vez de resuelta. DATO DEL GRAFO, medido hoy resolviendo a nodo vivo y citado como dato y no como argumento (banco 9.5.0): HAY ARISTA EN LOS DOS SENTIDOS, reparto_inicial_equity tiene a timing_equity_split en sus siguientes y timing_equity_split lo tiene en sus previos. La arista no acusa cuando falta ni exculpa cuando esta, pero aqui refuerza la lectura de jerarquia sana en vez de duplicacion. ESTA CORRECCION RESUELVE LA COLISION CON UN SOLO MOVIMIENTO Y SE DICE: el puesto 1008 ya es D y NO se toca, asi que tras esta correccion el par resuelto queda con UNA sola clase, D, y el censo vuelve a cero. La ampliacion de la vuelta 54 que manda MOVER LOS DOS cuando mover uno deja la colision viva NO se aplica aqui, porque mover uno la cierra, y se declara que se comprobo en vez de darse por supuesto. COHERENCIA CON EL TRAMO 1, verificada hoy en docs/plan/03_FUSIONES.md: el carril del filo de la vuelta 52 ya leyo DOS pares de esta misma familia del reparto de equity, criterios_equity_split contra reparto_inicial_equity (puesto 266) y criterios_equity_split contra timing_equity_split (puesto 246), y los DOS salieron CONDICION DE TEXTO y se resolvieron. Este es el tercero y sale igual: CONDICION DE TEXTO, NO pregunta de politica de catalogo, asi que el acto SI se funde.""")

VIEJA_ABRE = (" LO QUE DECIA LA RAZON VIEJA, y se deja escrita ENTERA para que la "
              "correccion se pueda auditar (copiada del archivo por maquina, no "
              "transcrita): ")
VIEJA_CIERRA = " FIN DE LA RAZON VIEJA."


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    idx = {r["puesto_intra"]: r for r in V}

    lote, fallos = [], []
    print("=" * 78)
    print("LOTE DE LA RELECTURA DEL FILO DE LA VUELTA 55")
    print("la razon vieja se pega POR MAQUINA, no se transcribe")
    print("=" * 78)
    for p in sorted(CAB):
        if p not in idx:
            fallos.append("el puesto %d no esta registrado" % p)
            continue
        vieja = idx[p]["razon"]
        clase_nueva, cab = CAB[p]
        nueva = cab.strip() + VIEJA_ABRE + vieja + VIEJA_CIERRA
        if vieja not in nueva:
            fallos.append("la razon vieja del %d NO quedo dentro de la nueva" % p)
        lote.append({"puesto": p, "clase": clase_nueva, "razon": nueva})
        print("  puesto %-5d %s -> %s | %-36s contra %s"
              % (p, idx[p]["clase"], clase_nueva, idx[p]["nodo_a"], idx[p]["nodo_b"]))
        print("      razon vieja %6d caracteres | razon nueva %6d | vieja DENTRO: %s"
              % (len(vieja), len(nueva), vieja in nueva))

    cambian = sum(1 for x in lote if idx[x["puesto"]]["clase"] != x["clase"])
    print()
    print("cambian de clase: %d de %d" % (cambian, len(lote)))
    if fallos:
        print()
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1
    io.open(a.salida, "w", encoding="utf-8", newline="\n").write(
        "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in lote))
    print("lote escrito: %s (%d lineas)" % (a.salida, len(lote)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
