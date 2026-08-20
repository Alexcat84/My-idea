# -*- coding: utf-8 -*-
"""vuelta53_p16.py . ESCRIBE EL LOTE DE CORRECCIONES `P.16` DE UN LOTE DE LA
VUELTA 53, CON LA RAZON VIEJA PEGADA ENTERA Y LEIDA DEL ARCHIVO.

POR QUE EXISTE COMO INSTRUMENTO: la razon vieja NO se teclea. Se lee del propio
docs/INTRA_DOMINIO_VEREDICTOS.jsonl y se pega entera detras del preambulo de la
correccion, que es lo que la casa exige ("una correccion que tapa lo que corrige
no se puede auditar"). Si la razon vieja ya trae un preambulo de correccion, se
pega igual: nada se recorta.

DOS ESPECIES, y se escriben distinto porque el carril general de colisiones
(acta de la vuelta 52, pregunta 4, registrado en 03_FUSIONES.md por la TAREA
1.4.b de esta vuelta) las trata distinto:

  VOLTEO   . el veredicto ARRASTRADO es una A y el DIRECTO del par resuelto es
             una D. Es el UNICO caso mecanico: se voltea por maquina citando el
             directo.
  RELECTURA. hay un veredicto DEL FILO (B o C) en CUALQUIERA de los dos lados.
             Nada se voltea por maquina: se RELEE en el mismo acto con el otro
             como contraste, y LA RELECTURA decide cual de los dos se mueve. El
             texto de la relectura se escribe a mano en este fichero y va dentro
             de la razon nueva, ANTES de la vieja.

Escribe el JSONL que come scripts/corregir_veredicto.py. No corrige nada por su
cuenta.

Uso: python scripts/loop/vuelta53_p16.py <A|B|C> <ruta de salida .jsonl>
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

CARRIL = (
    "EL CARRIL ES EL GENERAL DE COLISIONES, adjudicado en el acta de la vuelta 52, pregunta 4, y "
    "registrado en docs/plan/03_FUSIONES.md por la TAREA 1.4 de esta misma vuelta para que no "
    "dependa del acta."
)

PREAMBULO = (
    "CORRECCION DECLARADA EL 20 ago 2026 (vuelta 53), Y LA COLISION QUE LA OBLIGA LA FABRICO ESTA "
    "MISMA VUELTA: SE DICE ASI EN VEZ DE PRESENTARLA COMO HALLAZGO. %(que_paso)s Las colisiones "
    "que el lote fabrica estaban PREDICHAS ANTES DE TOCAR UN NODO por "
    "scripts/loop/vuelta51_colisiones_esperadas.py sobre el archivo entero "
    "(docs/loop/SALIDA_V53_COLISIONES_ESPERADAS.txt), y el censo real tras ejecutar devolvio "
    "EXACTAMENTE ESAS, ni una mas (%(censo)s). " + CARRIL + " %(especie)s LA RAZON VIEJA VA "
    "ENTERA DEBAJO, SIN RECORTAR UNA LETRA: %(vieja)s"
)

VOLTEO = (
    "ESPECIE: VOLTEO POR MAQUINA, que es el UNICO caso mecanico del carril: el veredicto "
    "ARRASTRADO de este par resuelto es una A y el DIRECTO es la %(directo)s, que dice que los dos "
    "nodos son distintos. La clase de este puesto pasa a D CITANDO ESE DIRECTO, y ninguna lectura "
    "nueva se inventa aqui."
)

RELECTURA = (
    "ESPECIE: RELECTURA EN EL MISMO ACTO, porque hay un veredicto DEL FILO en el par resuelto y el "
    "carril prohibe voltear por maquina. Se releyo con %(contraste)s como contraste, ANTES de "
    "sellar la correccion, y LA RELECTURA DECIDE: %(relectura)s"
)

LOTES = {
    "A": {
        "censo": "docs/loop/SALIDA_V53_CENSO_COLISIONES_LOTE_A.txt, que predijo SEIS y midio SEIS, "
                 "las mismas seis",
        "que_paso": "El LOTE A de esta vuelta fundio CUATRO actos de OP-U-01 sobre la nomina del "
                    "cierre de la vuelta 52 (el lienzo de propuesta de valor, los prompts, los "
                    "warrants y la huella de carbono), con el superviviente de cada uno elegido por "
                    "CONTENIDO segun la receta ratificada y con la guarda 1B pasando POR VACIO en "
                    "los cuatro (docs/loop/PLAN_V53_OPU01_LOTE_A.json, "
                    "docs/loop/SALIDA_V53_LOTE_A_EJEC.txt).",
        "correcciones": [
            {"puesto": 475, "clase": "D", "tipo": "VOLTEO",
             "directo": "D del puesto 705"},
            {"puesto": 1175, "clase": "D", "tipo": "VOLTEO",
             "directo": "D del puesto 1144"},
            {"puesto": 559, "clase": "D", "tipo": "VOLTEO",
             "directo": "D del puesto 1448"},
            {"puesto": 1865, "clase": "D", "tipo": "VOLTEO",
             "directo": "D del puesto 1855"},
            {"puesto": 360, "clase": "D", "tipo": "RELECTURA",
             "contraste": "el veredicto DIRECTO del par resuelto, la D del puesto 250",
             "relectura":
                 "SE MUEVE ESTE C Y NO LA D, y el motivo es que LAS DOS RAZONES DICEN LO MISMO Y "
                 "SIEMPRE LO DIJERON. Este puesto cerro con NIVELES DISTINTOS, SANO; el puesto 250 "
                 "cierra con LA PARTE CONTRA EL TODO, Y EL PASO 3 DEL CANVAS APUNTA EXPLICITAMENTE "
                 "AL MAPA DE VALOR. Leido el texto de HOY, despues de la fusion, el paso 3 del "
                 "superviviente apunta al mapa de valor con MAS letra que antes y no con menos: "
                 "DIBUJAR EL CUADRADO DEL VALUE MAP A LA IZQUIERDA, DOCUMENTANDO EN EL COMO TU "
                 "PRODUCTO O SERVICIO ALIVIA PAINS Y CREA GAINS. Lo que este C congelaba NO era una "
                 "duda de clase sino UNA FIGURA, y la figura YA ESTA REGISTRADA y ademas RE-ENCUADRADA: "
                 "la seccion 5 de docs/INTRA_DOMINIO_INFORME.md la escribe entera (hoy lineas 365 a "
                 "395 y 405 a 415, verificadas en esta vuelta), dice con estas palabras que el "
                 "registro del 360 ESTABA BIEN DESCRITO Y MAL ENCUADRADO porque no habia mirado las "
                 "aristas, y la re-encuadra como CENTRO SANO CON GEMELO SIN CASA, con "
                 "value_proposition_canvas de centro enlazado a sus tres piezas y "
                 "customer_profile_value_map como el gemelo sin casa; la seccion 14 la publica "
                 "ademas en su tabla de racimos (hoy linea 503, el lienzo de propuesta de valor, "
                 "7 miembros). O sea: LA FUSION NO SE LLEVA POR DELANTE NINGUN REGISTRO PENDIENTE. "
                 "Es CONDICION DE TEXTO y no pregunta de POLITICA, y por eso el acto se pudo fundir."},
            {"puesto": 204, "clase": "D", "tipo": "RELECTURA",
             "contraste": "el veredicto ARRASTRADO del par resuelto, la D del puesto 1521",
             "relectura":
                 "SE MUEVE ESTE B Y NO LA D, y el motivo esta en el texto de HOY y no en la "
                 "aritmetica de la fusion. Este puesto cerro con DUDOSO y con una frase que era una "
                 "medicion del texto de entonces: EL SEGUNDO PROFUNDIZA PERO NO AGREGA DECISION "
                 "NUEVA. Esa frase ES FALSA HOY, y se puede comprobar sin salir del nodo: tras la "
                 "fusion warrant_pricing_venture_debt trae TRES decisiones que "
                 "venture_debt_terminos_economicos no tiene en ningun paso, EVALUAR SI CONVIENE EL "
                 "WARRANT EN LUGAR DE UN DESCUENTO SIMPLE, FIJAR EL PLAZO DE EJERCICIO ENTRE CINCO Y "
                 "DIEZ ANOS Y QUE PASA SI EL NEGOCIO SE FUSIONA, y PEDIR QUE EL PAGO QUEDE SEPARADO "
                 "PARA EVITAR EL PROBLEMA CONTABLE DEL DESCUENTO DE EMISION ORIGINAL. Y quien "
                 "escribe que esas tres son PROCEDIMIENTO y no adorno es el propio contraste: el "
                 "puesto 1521 dice que venture_debt_terminos_economicos NOMBRA LOS WARRANTS EN DOS "
                 "LINEAS y que el otro TRAE EL PROCEDIMIENTO DE ESAS DOS LINEAS, y cierra POR LA "
                 "VARA DEL BANCO 9.6.1, CONTINUA. La misma vara leida sobre el nodo de hoy da la "
                 "misma clase, asi que el B se mueve a D y la D del 1521 se queda donde esta. NO ES "
                 "LA ARITMETICA DE LA FUSION LA QUE MUEVE ESTA CLASE: es que uno de los dos nodos "
                 "CAMBIO DE TEXTO, que es el disparador escrito de la cola de relectura post fusion "
                 "de docs/plan/08_VERIFICACION.md. Es CONDICION DE TEXTO y no pregunta de POLITICA."},
        ],
    },
    "B": {
        "censo": "docs/loop/SALIDA_V53_CENSO_COLISIONES_LOTE_B.txt, que predijo CUATRO y midio "
                 "CUATRO, las mismas cuatro",
        "que_paso": "El LOTE B de esta vuelta fundio CUATRO actos de OP-U-01 sobre la nomina del "
                    "cierre de la vuelta 52 (los costos de franquicia, el abogado de franquicias, "
                    "la franquicia inadvertida y la gestion por objetivos), con el superviviente de "
                    "cada uno elegido por CONTENIDO segun la receta ratificada y con la guarda 1B "
                    "pasando POR VACIO en los cuatro (docs/loop/PLAN_V53_OPU01_LOTE_B.json, "
                    "docs/loop/SALIDA_V53_LOTE_B_EJEC.txt).",
        "correcciones": [
            {"puesto": 2075, "clase": "D", "tipo": "VOLTEO", "directo": "D del puesto 2092"},
            {"puesto": 2090, "clase": "D", "tipo": "VOLTEO", "directo": "D del puesto 2086"},
            {"puesto": 2181, "clase": "D", "tipo": "VOLTEO", "directo": "D del puesto 2073"},
            {"puesto": 2488, "clase": "D", "tipo": "VOLTEO", "directo": "D del puesto 2534"},
        ],
    },
    "C": {
        "censo": "docs/loop/SALIDA_V53_CENSO_COLISIONES_LOTE_C.txt, que predijo CUATRO y midio "
                 "CUATRO, las mismas cuatro",
        "que_paso": "El LOTE C de esta vuelta fundio CUATRO actos de OP-U-01 sobre la nomina del "
                    "cierre de la vuelta 52 (el pareto, el poka yoke, el dmaic select y la "
                    "investigacion del cliente), con el superviviente de cada uno elegido por "
                    "CONTENIDO segun la receta ratificada y con la guarda 1B pasando POR VACIO en "
                    "tres de los cuatro y con la puerta COMO SUPERVIVIENTE en el del dmaic select "
                    "(docs/loop/PLAN_V53_OPU01_LOTE_C.json, docs/loop/SALIDA_V53_LOTE_C_EJEC.txt).",
        "correcciones": [
            {"puesto": 2551, "clase": "D", "tipo": "VOLTEO", "directo": "D del puesto 3087"},
            {"puesto": 2613, "clase": "D", "tipo": "VOLTEO", "directo": "D del puesto 2931"},
            {"puesto": 2742, "clase": "D", "tipo": "VOLTEO", "directo": "D del puesto 2933"},
            {"puesto": 811, "clase": "D", "tipo": "RELECTURA",
             "contraste": "el veredicto ARRASTRADO del par resuelto, la A del puesto 1222",
             "relectura":
                 "SE MUEVEN LOS DOS, Y HAY QUE DECIR POR QUE, porque el carril dice que la "
                 "relectura decide CUAL se mueve y aqui la respuesta es LOS DOS: dejar uno en B y "
                 "el otro en D deja la colision viva, que es justo lo que P.16 existe para "
                 "impedir. LA CONDICION QUE ESTE B PUSO ERA DE CONTEO Y ESTA DESCARGADA. Este "
                 "puesto no cerro con una duda de lectura sino con esta frase: LA FAMILIA DE LOS "
                 "DATOS DEL CLIENTE DE COLEMAN YA LLEVA CUATRO NODOS VISTOS Y LOS PARES SE "
                 "CONTRADICEN ENTRE SI SEGUN CON QUIEN SE COMPARE: HAY QUE CONTARLA ANTES DE "
                 "DECIDIR. Se conto ANTES de fundir (docs/loop/SALIDA_V53_COLEMAN.txt): los cuatro "
                 "nodos que nombra siguen VIVOS, sus SEIS pares estan LEIDOS, cobertura 6 de 6 y "
                 "CERO pendientes, con el reparto 317 A, 509 D, 657 D, 687 D, 811 B y 1222 A. Con "
                 "la familia contada NO HAY CONTRADICCION: la figura es una estrella limpia con "
                 "seguimiento_informacion_cliente de centro (A con dos, puestos 317 y 1222) y "
                 "conexion_personal_emocional saliendo D contra los tres. Y LA VARA QUE DECIDE LA "
                 "CLASE LA ESCRIBE EL PROPIO CONTRASTE, el puesto 1222, con estas palabras: CUANDO "
                 "LO COMPARTIDO ES EL ACTO, ES A; CUANDO LO COMPARTIDO ES SOLO POR DONDE SE ENTRA, "
                 "ES SANO. Leidos los dos textos de hoy, lo compartido es POR DONDE SE ENTRA y no "
                 "el acto: este mismo puesto ya lo habia medido al escribir LO COMUN ES DEFINIR QUE "
                 "DATOS GUARDAR Y METERLOS EN EL CRM, dos lineas de cuatro; y lo propio de "
                 "personalizacion_investigacion_prospecto son las otras dos, LA LISTA CORTA DE "
                 "GESTOS de bajo costo y alto impacto emocional preparada de antemano, y ENSENAR "
                 "PRIMERO AL EQUIPO COMO SE SIENTE SER SORPRENDIDO, que el propio 1222 declara "
                 "PIEZAS PROPIAS SUYAS y que no estan en investigar_datos_cliente ni en el nodo que "
                 "muere. A eso se suma el momento del ciclo, EL PROSPECTO ANTES DE VENDER contra EL "
                 "CLIENTE QUE YA ESTA, que este mismo puesto escribio en su primera linea. D. Es "
                 "CONDICION DE CONTEO, descargada por medicion, y NO pregunta de POLITICA: por eso "
                 "el acto se pudo fundir."},
            {"puesto": 1222, "clase": "D", "tipo": "RELECTURA",
             "contraste": "el veredicto DIRECTO del par resuelto, la B del puesto 811",
             "relectura":
                 "SE MUEVE CON EL 811 Y EN EL MISMO ACTO, por la relectura escrita en aquel puesto. "
                 "LO QUE ADEMAS LE PASA A ESTE PUESTO EN PARTICULAR, y se dice porque no es lo "
                 "mismo que le pasa al otro: el par que este veredicto LEYO era "
                 "personalizacion_investigacion_prospecto contra seguimiento_informacion_cliente, y "
                 "seguimiento_informacion_cliente MURIO en este acto absorbido por "
                 "investigar_datos_cliente. Su medicion sigue siendo cierta para el par que leyo "
                 "(LOS DOS PRIMEROS PASOS de uno son los dos primeros del otro) y ya no describe "
                 "ningun par vivo: resuelto al dia de hoy, este puesto apunta al mismo par que el "
                 "811, que se leyo de frente y con la cobertura entera. La clase que sale de esa "
                 "relectura es D."},
        ],
    },
}


def main():
    lote = (sys.argv[1] if len(sys.argv) > 1 else "A").upper()
    salida = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
        RAIZ, "docs", "loop", "_lote_v53_lote_%s.jsonl" % lote.lower())
    sys.stdout.reconfigure(encoding="utf-8")

    if lote not in LOTES:
        print("lote desconocido")
        return 1
    cfg = LOTES[lote]

    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    idx = {r["puesto_intra"]: r for r in V}

    print("=" * 78)
    print("LAS CORRECCIONES P.16 DEL LOTE %s DE LA VUELTA 53" % lote)
    print("=" * 78)
    print()

    filas = []
    for c in cfg["correcciones"]:
        r = idx[c["puesto"]]
        if c["tipo"] == "VOLTEO":
            especie = VOLTEO % {"directo": c["directo"]}
        else:
            especie = RELECTURA % {"contraste": c["contraste"], "relectura": c["relectura"]}
        razon = PREAMBULO % {
            "que_paso": cfg["que_paso"],
            "censo": cfg["censo"],
            "especie": especie,
            "vieja": r["razon"],
        }
        filas.append({"puesto": c["puesto"], "clase": c["clase"], "razon": razon})
        print("  puesto %-6d %s -> %s | %-9s | %s contra %s"
              % (c["puesto"], r["clase"], c["clase"], c["tipo"], r["nodo_a"], r["nodo_b"]))
        print("     razon vieja pegada entera: %d caracteres" % len(r["razon"]))

    io.open(salida, "w", encoding="utf-8", newline="\n").write(
        "".join(json.dumps(f, ensure_ascii=False) + "\n" for f in filas))
    print()
    print("ESCRITO: %s (%d correcciones)" % (salida, len(filas)))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
