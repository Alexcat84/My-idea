# -*- coding: utf-8 -*-
"""Construye el lote de correccion del puesto 784, CON LA RAZON VIEJA COPIADA
POR MAQUINA del archivo y no transcrita a mano (una correccion que tapa lo que
corrige no se puede auditar, EJECUTOR.md regla 8)."""
import io
import json

VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
vieja = None
for r in V:
    if r["puesto_intra"] == 784:
        vieja = r["razon"]
        assert r["clase"] == "B", r["clase"]
        break
assert vieja is not None

NUEVA = (
    u"CORRECCION DECLARADA, 19 ago 2026 (vuelta 45): DE B A D, POR EL DESTEJIDO "
    u"DE OP-D-08. Este par es el CASO POSITIVO de la operacion y es el que la "
    u"manda: su razon vieja decia NO SE JUZGA HOY y remataba con primero la "
    u"cirugia y despues el par. LA CIRUGIA ESTA HECHA y el par SE JUZGA AQUI. "
    u"LO QUE LO BLOQUEABA, MEDIDO ANTES Y DESPUES: el solape cruzaba las CUATRO "
    u"junturas del nodo largo a la vez, y hoy el nodo tiene UNA SOLA narracion, "
    u"o sea CERO junturas (guardas de la operacion, "
    u"docs/loop/SALIDA_V45_OPD08_CASO_ANTES.txt contra "
    u"SALIDA_V45_OPD08_CASO_DESPUES.txt: 0 PASAN y 4 CAEN antes, 4 PASAN y 0 "
    u"CAEN despues). lienzo_modelo_negocio paso de DIECISIETE pasos a DOCE y su "
    u"senal de bloque cayo de 65,6 a 46,0, con el corte del 13 al 8, re-medido "
    u"hoy con scripts/costuras_internas.py. "
    u"EL VEREDICTO ES D, Y LA VARA ES LA ORDINARIA (banco 9.6.1 la linea o el "
    u"procedimiento, con la direccion del 9.6.2). LOS DOS PROCEDIMIENTOS SON "
    u"DISJUNTOS, medido palabra por palabra sobre los dos textos de hoy y no "
    u"por impresion: en los DOCE pasos de lienzo_modelo_negocio no aparece ni "
    u"una vez fortaleza, debilidad, oportunidad, amenaza, SWOT, impacta ni "
    u"prioriza; y en los CINCO de swot_business_model_canvas no aparece ni una "
    u"vez identificar los segmentos, definir la propuesta, mapear, calcular, "
    u"imprimir, post-it ni publicar. Uno CONSTRUYE el lienzo y el otro lo "
    u"EVALUA. "
    u"Y SE COMPRUEBA LO QUE EL PROPIO 784 DEJO ANOTADO, que es la segunda linea "
    u"del campo verificacion de OP-D-08: el analisis cruzado (como una debilidad "
    u"de un bloque golpea a los otros, paso 4 del donante) NO ESTA en el nodo "
    u"largo, y sigue sin estar tras el destejido. Lo unico que se le parece es "
    u"el paso 10 del destejido (iterar hasta lograr COHERENCIA entre los "
    u"bloques), y no es lo mismo: la coherencia pide que los bloques no se "
    u"contradigan, y el analisis cruzado pide rastrear como una DEBILIDAD de uno "
    u"se propaga a los otros. La operacion escribio que si resultara que SI esta, "
    u"el par cambiaria de clase y habria que decirlo: NO ESTA, y por eso el par "
    u"no cambia por ese lado. "
    u"LOS ENTREGABLES NO SON INTERCAMBIABLES, leidos hoy en los dos ficheros: el "
    u"del nodo largo es un Lienzo de Modelo de Negocio completo con los 9 "
    u"bloques definidos y coherentes entre si, y el del otro es una Matriz SWOT "
    u"detallada por cada bloque con hallazgos priorizados. Uno produce el "
    u"lienzo, el otro produce una evaluacion DEL lienzo. La prueba de madre e "
    u"hijo del 9.6.2 falla en los dos sentidos: los cinco pasos del SWOT no "
    u"caben dentro de ningun paso del lienzo, y los doce del lienzo no caben "
    u"dentro de ninguno de los cinco del SWOT. LO UNICO COMPARTIDO es la "
    u"ENUMERACION de los nueve bloques, y en el donante es un PUNTERO (su paso 1 "
    u"manda TOMAR cada uno de los 9 bloques, no construirlos), no una segunda "
    u"construccion. "
    u"LA RELACION ES DE ALIMENTACION Y NO DE GEMELOS, la misma figura que el "
    u"acta de la vuelta 44 adjudico para el 233 y la 43 para el 599: uno produce "
    u"el dato que el otro consume para decidir. Y AQUI HAY UNA DIFERENCIA CON "
    u"AQUELLOS DOS QUE SE DICE PORQUE MEJORA EL CASO: LA ARISTA YA EXISTE Y ESTA "
    u"BIEN PUESTA, buscada hoy en los dos sentidos contra el grafo (regla 9): "
    u"lienzo_modelo_negocio nombra a swot_business_model_canvas en sus "
    u"nodos_siguientes y swot_business_model_canvas lo nombra en sus "
    u"nodos_previos, o sea arista dirigida CON su espejo. Este par NO deja "
    u"ninguna arista que falte para la fase 04, a diferencia del 599 y del 233. "
    u"MISMA FUENTE LOS DOS (Osterwalder, con dos grafias del mismo libro), lo que "
    u"descarta el argumento de libro y deja la decision entera en el "
    u"procedimiento. "
    u"Y SE DICE LO QUE INCOMODA EN VEZ DE ELEGIR EL DATO QUE CONVIENE: el "
    u"destejido ACERCO los dos textos en un punto, porque quito del nodo largo "
    u"tres de sus cuatro narraciones y lo dejo mas parecido a un recorrido de los "
    u"nueve bloques, que es justo la forma del paso 1 del donante. Aun asi el "
    u"veredicto es D, y por la misma frontera del 344 y del 233: recorrer los "
    u"bloques para CONSTRUIRLOS no es recorrerlos para EVALUARLOS, y ningun paso "
    u"del nodo largo pregunta nada. "
    u"LA RAZON VIEJA SE CONSERVA ENTERA Y A LA VISTA para que la correccion se "
    u"pueda auditar (copiada del archivo por maquina, no transcrita): "
    + vieja)

io.open("docs/loop/LOTE_V45_784.jsonl", "w", encoding="utf-8", newline="\n").write(
    json.dumps({"puesto": 784, "clase": "D", "razon": NUEVA}, ensure_ascii=False) + "\n")
print("LOTE ESCRITO: docs/loop/LOTE_V45_784.jsonl")
print("  puesto 784, de B a D")
print("  razon nueva: %d caracteres, de los cuales %d son la razon vieja conservada"
      % (len(NUEVA), len(vieja)))
