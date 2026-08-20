# -*- coding: utf-8 -*-
"""vuelta51_colision_fabricada_b.py . CONSTRUYE EL LOTE DE LAS CORRECCIONES `P.16`
DE LAS COLISIONES QUE EL LOTE B DE ESTA VUELTA FABRICA.

GEMELO DECLARADO de scripts/loop/vuelta51_colision_fabricada.py: mismo contrato,
mismo cierre comun, otras cabeceras. Y sucesor de
scripts/loop/vuelta50_colision_fabricada.py, del que los dos heredan el motivo:
la razon vieja tiene que quedar ENTERA dentro de la razon nueva (banco 9.10 y la
regla de la casa, una correccion que tapa lo que corrige no se puede auditar), y
se PEGA POR MAQUINA leyendola del archivo, porque transcribir a mano un parrafo
de miles de caracteres es donde nace una errata.

LA NOVEDAD DE ESTE LOTE, y por eso vale la pena que quede escrita: UNA COLISION
SE CUENTA POR PAR RESUELTO Y NO POR VEREDICTO. El par
consejo_de_calidad contra consejo_de_calidad_3 lleva TRES veredictos dentro
(2523 `A`, 2662 `A` y 2916 `D`) y es UNA sola colision: los dos `A` se voltean,
el `D` se queda. La cuenta del encargo (una colision por cada CONTINUA) calza
con esa forma de contar y no con la de contar veredictos.

EL CARRIL, adjudicado en el acta de la vuelta 49, pregunta 1: LA LECTURA `P.12`
ES LA RELECTURA CONJUNTA DEL `A` VIEJO, porque ese `A` se emitio contra un nodo
que hoy no existe solo.

GUARDA: tras construir, comprueba que la razon vieja aparece LITERAL dentro de la
nueva en TODAS. Si falta una sola, aborta sin escribir el lote.

De solo lectura sobre el archivo de veredictos: escribe el LOTE, no el archivo.
El archivo lo escribe scripts/corregir_veredicto.py, que es el carril adjudicado.

Uso: python scripts/loop/vuelta51_colision_fabricada_b.py --salida docs/loop/_lote_v51_lote_b.jsonl
"""
import argparse
import io
import json
import sys

VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"

FIN = (
    " Y LA SALIDA NO PIDE DOCTRINA NUEVA, con el carril adjudicado por el auditor en "
    "el acta de la vuelta 49, pregunta 1, y usado igual en la vuelta 50: LA LECTURA "
    "P.12 ES LA RELECTURA CONJUNTA DE ESTE A, porque este A se emitio contra un nodo "
    "que hoy no existe solo, y la lectura se hizo con los textos vivos delante y esta "
    "escrita en el registro del tramo de docs/plan/03_FUSIONES.md. P.16, QUIEN FABRICA "
    "LIMPIA, en el mismo acto y sin aplazar. El marcador queda recomputado en la misma "
    "vuelta y el barrido 9.10 corrido sobre toda tabla vigente que cite la clase, el "
    "marcador o el retrato, despues del ultimo movimiento de la vuelta.")

CAB = {}

CAB[2523] = ("D", (
    "CORRECCION DECLARADA EL 20 ago 2026 (vuelta 51), Y LA COLISION QUE LA OBLIGA LA "
    "FABRICO ESTA MISMA VUELTA: SE DICE ASI EN VEZ DE PRESENTARLA COMO HALLAZGO. LA "
    "CLASE CAMBIA: DE A A D. QUE PASO, en orden. La fusion de la PARTE A del acto 1 del "
    "lote B de OP-U-01 (la familia del CONSEJO DE CALIDAD de quality) depreco "
    "consejo_calidad y consejo_calidad_2 con alias a consejo_de_calidad. El "
    "superviviente se eligio por CONTENIDO entre los DOS UNICOS VIABLES, "
    "consejo_de_calidad y consejo_de_calidad_3: SEIS pasos contra cuatro, y el veredicto "
    "directo del par mixto (2916) cuenta TRES pasos enteros propios del elegido contra "
    "DOS del otro. Y AQUI HAY UN CHOQUE DE LETRA CONTRA ARITMETICA QUE SE REGISTRA EN "
    "VEZ DE CALLARSE: este mismo puesto cierra con Sobrevive consejo_calidad, y "
    "consejo_calidad NO ES VIABLE, porque su parte A se lleva a los cuatro miembros y no "
    "deja ningun mixto fuera, o sea que elegirlo seria fundir entero un acto que tiene "
    "una D dentro. El acta de la vuelta 50, pregunta 3, lo adjudico: MANDA LA "
    "ARITMETICA, porque P.12 es regla y la formula Sobrevive X es el cierre de una razon "
    "de PAR mientras el racimo decide. Desde la fusion, este puesto, emitido contra "
    "consejo_calidad, RESUELVE al par consejo_de_calidad contra consejo_de_calidad_3, "
    "que es exactamente el par del puesto 2916, que es D, y cae junto al 2662, que es la "
    "misma historia por el otro absorbido. TRES VEREDICTOS, UN PAR RESUELTO, DOS CLASES: "
    "colision de clase, medida con resolutor propio sobre el archivo entero "
    "(docs/loop/SALIDA_V51_CENSO_COLISIONES_LOTE_B.txt). LO QUE LA LECTURA P.12 MIDE CON "
    "LOS DOS TEXTOS VIVOS DELANTE: el A de este puesto era verdad de consejo_calidad, un "
    "nodo de SEIS pasos del que este mismo veredicto dice que consejo_de_calidad_3 le "
    "cabe dentro salvo DOS LINEAS. El nodo vivo de hoy tiene ONCE pasos y CUATRO "
    "condiciones y no es el mismo nodo: trae el motor de proyectos de Juran entero, "
    "capacitarse en el metodo, priorizar con analisis de Pareto, elegir los proyectos con "
    "problema y meta definidos y asignar capacitacion, personas, tiempo y acompanamiento, "
    "mas las politicas, la carta constitutiva, el enlace corporativo divisional y la "
    "comunicacion de responsabilidades que los dos absorbidos aportaron. Contra ESE nodo, "
    "consejo_de_calidad_3 no repite: el 2916 lo verifico contra el grafo y escribio que "
    "SON CONJUNTOS DISJUNTOS DE PASOS PROPIOS, NO GEMELOS, y lo propio del mixto es el "
    "encuadre de CROSBY, el consejo como motor del ciclo de catorce pasos que se repite "
    "y se institucionaliza como estructura permanente. P.12 lo llama CONTINUA: enlace mas "
    "poda del solape, no fusion. D. Y EL ARCHIVO YA CORTABA DENTRO DE ESTA MISMA FAMILIA "
    "POR LA MISMA LINEA antes de la fusion, y el 2916 lo cita: el puesto 2549 separo "
    "consejo_de_calidad, el motor de proyectos, de consejo_de_calidad_y_rol_del_director, "
    "la politica que le da consecuencia."))

CAB[2662] = ("D", (
    "CORRECCION DECLARADA EL 20 ago 2026 (vuelta 51), Y LA COLISION QUE LA OBLIGA LA "
    "FABRICO ESTA MISMA VUELTA: SE DICE ASI EN VEZ DE PRESENTARLA COMO HALLAZGO. LA "
    "CLASE CAMBIA: DE A A D. ES EL SEGUNDO VEREDICTO DEL MISMO PAR RESUELTO, y por eso "
    "se voltea con la misma razon que el 2523: la fusion de la PARTE A del acto 1 del "
    "lote B de OP-U-01 depreco consejo_calidad y consejo_calidad_2 con alias a "
    "consejo_de_calidad, y desde ese momento este puesto, emitido contra "
    "consejo_calidad_2, RESUELVE al par consejo_de_calidad contra consejo_de_calidad_3, "
    "que es el par del puesto 2916, que es D. UNA COLISION SE CUENTA POR PAR RESUELTO Y "
    "NO POR VEREDICTO, y este par lleva TRES dentro (2523 A, 2662 A, 2916 D): los dos A "
    "se voltean, el D se queda. AQUI TAMBIEN HAY CHOQUE DE LETRA CONTRA ARITMETICA: este "
    "puesto cierra con Sobrevive consejo_calidad_2, que NO ES VIABLE por la estructura "
    "del acto, y por la adjudicacion del acta de la vuelta 50, pregunta 3, MANDA LA "
    "ARITMETICA. LO QUE LA LECTURA P.12 MIDE CON LOS TEXTOS VIVOS DELANTE: el A de este "
    "puesto se apoyaba, con estas palabras, en que el par se resolvia POR TRANSITIVIDAD "
    "y no por lectura directa, y el propio 2916 desmonto esa cadena en su relectura "
    "conjunta: con un eslabon de CONTENCION declarado en cada cadena citada, la "
    "transitividad NO compone. El nodo vivo de hoy tiene ONCE pasos y CUATRO "
    "condiciones, y contra el consejo_de_calidad_3 aporta lo que ninguno de los once "
    "dice, coordinar la repeticion del ciclo de mejora e institucionalizar el consejo "
    "como parte de la estructura permanente. P.12 lo llama CONTINUA: enlace mas poda del "
    "solape, no fusion. D."))

CAB[498] = ("D", (
    "CORRECCION DECLARADA EL 20 ago 2026 (vuelta 51), Y LA COLISION QUE LA OBLIGA LA "
    "FABRICO ESTA MISMA VUELTA: SE DICE ASI EN VEZ DE PRESENTARLA COMO HALLAZGO. LA "
    "CLASE CAMBIA: DE A A D. QUE PASO, en orden. La fusion de la PARTE A del acto 2 del "
    "lote B de OP-U-01 (la familia de la RELACION PREVIA ENTRE COFUNDADORES, del libro "
    "de Wasserman) depreco riesgo_cofundadores_relacion_previa, el CENTRO de la "
    "estrella, con alias a cofundar_con_amigos_familia_riesgos, que es el superviviente "
    "elegido por CONTENIDO: CINCO pasos contra cuatro y resumen de 576 caracteres contra "
    "491. Desde ese momento este puesto, emitido contra "
    "riesgo_cofundadores_relacion_previa, RESUELVE al par "
    "cofundar_con_amigos_familia_riesgos contra seleccion_relaciones_cofundadores, que "
    "es exactamente el par del puesto 1058, que es D. DOS VEREDICTOS, UN PAR RESUELTO, "
    "DOS CLASES: colision de clase, medida con resolutor propio sobre el archivo entero "
    "(docs/loop/SALIDA_V51_CENSO_COLISIONES_LOTE_B.txt). LO QUE LA LECTURA P.12 MIDE CON "
    "LOS DOS TEXTOS VIVOS DELANTE: el A de este puesto era verdad de "
    "riesgo_cofundadores_relacion_previa, un nodo de CUATRO pasos que MAPEA y CLASIFICA "
    "la relacion previa y no manda ninguna medida. El nodo vivo de hoy tiene SIETE pasos "
    "y TRES condiciones y trae el procedimiento de blindaje entero: discutir antes de "
    "fundar el reparto de equity, los roles y que pasa si el negocio falla; PROBAR LA "
    "RELACION DE TRABAJO EN UN PROYECTO PEQUENO antes de comprometerse; cortafuegos "
    "formales entre lo personal y lo profesional; estructuras de autoridad claras aunque "
    "incomoden; revisar si ya se trabajo de verdad con esa persona antes; y el criterio "
    "de que sumar a alguien con quien ya trabajaste reduce el riesgo mas que sumar a un "
    "amigo o familiar sin ese antecedente. Contra ESE nodo, "
    "seleccion_relaciones_cofundadores no repite, y el veredicto directo del par lo "
    "escribe con la vara del banco 9.6.1 nombrada: el mixto MAPEA EL TERRENO y dice EN "
    "UNA LINEA lo que el superviviente trae como PROCEDIMIENTO ENTERO. P.12 lo llama "
    "CONTINUA: enlace mas poda del solape, no fusion. D. Y lo propio del mixto que la "
    "fusion no se lleva queda nombrado en el registro del tramo: el mapa de los TRES "
    "CIRCULOS, cercanos, indirectos y desconocidos, y el proceso de evaluacion de "
    "habilidades y compatibilidad para el circulo externo."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por = {r["puesto_intra"]: r for r in V}

    FORMULA = ("LO QUE DECIA LA RAZON VIEJA, y se deja escrita ENTERA para que la "
               "correccion se pueda auditar (copiada del archivo por maquina, no "
               "transcrita): ")

    filas, fallos = [], 0
    for n in sorted(CAB):
        clase, cabecera = CAB[n]
        if n not in por:
            print("ROJO: el puesto %d no esta registrado." % n)
            fallos += 1
            continue
        vieja = por[n]["razon"]
        nueva = cabecera + FIN + " " + FORMULA + vieja + " FIN DE LA RAZON VIEJA."
        if vieja not in nueva:
            print("ROJO: la razon vieja del %d no quedo literal dentro de la nueva." % n)
            fallos += 1
            continue
        if u"—" in nueva or u"–" in nueva:
            print("ROJO: guion largo o medio en la razon nueva del %d." % n)
            fallos += 1
            continue
        print("puesto %d | %s -> %s | %s contra %s | razon %d a %d caracteres"
              % (n, por[n]["clase"], clase, por[n]["nodo_a"], por[n]["nodo_b"],
                 len(vieja), len(nueva)))
        filas.append({"puesto": n, "clase": clase, "razon": nueva})

    if fallos:
        print()
        print("ABORTA: %d en rojo. El lote NO se escribe." % fallos)
        return 1

    with io.open(a.salida, "w", encoding="utf-8", newline="\n") as f:
        for x in filas:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    print()
    print("LOTE ESCRITO: %s (%d filas)" % (a.salida, len(filas)))
    print("La guarda paso en las %d: la razon vieja vive LITERAL dentro de la nueva."
          % len(filas))
    print("guiones largos y medios en las razones nuevas: CERO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
