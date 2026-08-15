# -*- coding: utf-8 -*-
"""vuelta33_volcado_910_b.py

TAREA 2.4 de la vuelta 33: construye el LOTE de correccion de los TRES congelados
que `voz_del_cliente_voc` bloqueaba, releidos contra el superviviente ya estable
(banco 9.4, el TOQUE UNICO) y volcados por el mismo carril del 9.10 de la tarea 1.3.

  724  B -> D   voice_of_customer_estrategico   (arista que falta)
  755  B -> D   dia_en_la_vida_del_cliente      (arista que falta)
  827  B -> D   ganar_comprension_del_cliente   (sano, sin arista necesaria)

LA GUARDA DEL ENCARGO, COMPROBADA Y NO SUPUESTA: si el 724 diera `A`,
`voice_of_customer_estrategico` entraria al acto por `P.6` y habria que PARAR,
porque una fusion nueva sin operacion escrita no se improvisa. NO DA `A`, y el
motivo esta en su razon: trae un procedimiento de interrogacion y registro que el
superviviente no tiene en ninguno de sus SEIS pasos de hoy.

MISMA DISCIPLINA QUE EL PRIMER LOTE: la razon vieja se COPIA del archivo por
maquina, verbatim, y el script ABORTA si no queda literalmente dentro de la nueva.

Uso: python scripts/loop/vuelta33_volcado_910_b.py
Salida: docs/loop/_lote_v33b.jsonl. El archivo lo escribe scripts/corregir_veredicto.py.
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
LOTE = os.path.join(RAIZ, "docs", "loop", "_lote_v33b.jsonl")

FECHA = "15 ago 2026"

CABECERA = (
    "REESCRITA EL %s POR LA FUSION DE OP-D-02, y la clase pasa de B a D. CORRECCION "
    "DECLARADA. El congelamiento venia del TOQUE UNICO del banco 9.4 (un veredicto emitido "
    "contra un texto que va a cambiar no vale) y la causa CAYO: voz_del_cliente_voc quedo "
    "estable el 15 ago 2026, con SEIS pasos y fuente unica, tras absorber a enfoque_mercado_voc "
    "en la fusion de OP-D-02. El volcado va por el banco 9.10, con su barrido de tablas "
    "derivadas en el mismo acto." % FECHA
)

CUERPO = {
    724: (
        "POR QUE YA SE PUEDE JUZGAR: la razon vieja decia que el solape CRUZABA LA JUNTURA de un "
        "nodo con anatomia DOBLE DE LA OBSERVACION, diez pasos en dos mitades que hablaban las dos "
        "de observar al cliente en su contexto. ESA ANATOMIA YA NO EXISTE, medido hoy sobre el "
        "arbol: voz_del_cliente_voc tiene SEIS pasos y fuente UNICA. El bloque 6 a 10 de Coleman "
        "salio en la vuelta 31 con OP-F-04-COL y hoy vive en observar_al_cliente_en_su_contexto; "
        "lo que queda es una sola narracion, ampliada por la fusion. NO HAY JUNTURA QUE CRUZAR. "
        "LA LECTURA, CONTRA LOS SEIS PASOS DE HOY Y NO CONTRA LOS DIEZ DE ANTES. Lo compartido es "
        "el arranque: observar al cliente en su contexto real y no por encuesta, que el "
        "superviviente dice en sus pasos 1 y 2. Lo propio de voice_of_customer_estrategico es un "
        "PROCEDIMIENTO DE INTERROGACION Y REGISTRO que el superviviente no tiene en ninguno de sus "
        "seis pasos: preguntar que problemas enfrentan y QUE LOS MANTIENE DESPIERTOS POR LA NOCHE, "
        "indagar el porque detras de cada caracteristica o producto que soliciten, buscar "
        "NECESIDADES FUTURAS y planes del cliente y no solo las actuales, y documentar los ahas o "
        "descubrimientos inesperados durante la observacion. Es exactamente lo que la razon vieja "
        "habia dejado anotado como lo que habria que salvar, y hoy se puede decir que no hace "
        "falta salvarlo porque el par NO se funde. "
        "Y EL SUPERVIVIENTE CONSERVA MATERIA PROPIA QUE EL OTRO NO TOCA EN NINGUN PASO, que es la "
        "otra mitad de la prueba de reconocimiento del banco 9.6.2: la evaluacion preliminar de "
        "mercado, el analisis competitivo detallado de productos, precios y tecnologias, la prueba "
        "de concepto con clientes reales antes del desarrollo formal, y el contacto en ciclos "
        "cortos durante todo el desarrollo. MADRE voz_del_cliente_voc, cuyo paso 1 enuncia en UNA "
        "LINEA el prepararse para observar, e HIJO voice_of_customer_estrategico, que trae el "
        "protocolo entero de esa linea. CONTINUA: D, los dos sanos. "
        "ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS CONTRA EL GRAFO: NO HAY NINGUNA. D, SANO, CON "
        "ARISTA QUE FALTA, con direccion de madre a hijo. Queda declarada para la fase 04. "
        "LA GUARDA DEL ENCARGO, DICHA POR SU NOMBRE: si este par hubiera dado A, "
        "voice_of_customer_estrategico habria entrado al acto de OP-D-02 por P.6 y habria que "
        "PARAR, porque una fusion nueva sin operacion escrita no se improvisa. NO DA A, y por eso "
        "la vuelta sigue. "
        "NOTA DE ALCANCE, y es la que hace la lectura interesante: ANTES de la fusion este par "
        "estaba MUCHO mas cerca de A, porque el superviviente era solo la observacion de campo. "
        "Fue la fusion la que lo separo, al darle al superviviente el tramo de mercado. Es la "
        "razon por la que el banco 9.4 congela: el mismo par da dos clases distintas segun el dia."
    ),
    755: (
        "POR QUE YA SE PUEDE JUZGAR: identica al 724 y por la misma medicion. La razon vieja "
        "bloqueaba porque EL SOLAPE VOLVIA A CRUZAR LA JUNTURA del nodo de anatomia doble. Hoy "
        "voz_del_cliente_voc tiene SEIS pasos y fuente unica: no le queda juntura. "
        "LA LECTURA, CONTRA LOS SEIS PASOS DE HOY. Lo compartido es el arranque de campo: observar "
        "o entrevistar a los usuarios en su entorno real, que el superviviente dice en sus pasos 1, "
        "2 y 3. Lo propio de dia_en_la_vida_del_cliente son TRES COSAS que el superviviente no "
        "dice en ningun paso, y las tres forman un procedimiento con entregable propio: PROYECTAR "
        "y describir como cambiaria el dia del cliente con el producto nuevo; REPETIR el ejercicio "
        "para CADA figura de la decision, usuario final, gerente, ejecutivo y tecnologia; y "
        "PRESENTAR al equipo de desarrollo una imagen viva y especifica del antes y el despues, en "
        "narrativa o storyboard. Su entregable lo dice sin ambiguedad y es otro: documento "
        "narrativo o storyboard de antes y despues de un dia tipico de cada tipo de cliente. "
        "LA PRUEBA DE RECONOCIMIENTO DE MADRE E HIJO DEL 9.6.2 NO SE CUMPLE, y se dice en vez de "
        "forzar una madre: dia_en_la_vida_del_cliente NO cabe entero dentro de un paso del "
        "superviviente, porque sus pasos 3, 4 y 5 salen de la observacion y entran en la "
        "proyeccion y en la comunicacion al equipo. SON DOS OBJETOS DISTINTOS que comparten el "
        "arranque de campo, igual que la figura de LD-72. CONTINUA: D, los dos sanos. "
        "Libros distintos ademas, The Startup Owner's Manual contra Winning at New Products, y eso "
        "no cambia nada porque la vara no pregunta por el autor. "
        "ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS CONTRA EL GRAFO: NO HAY NINGUNA, que es lo que la "
        "razon vieja ya decia con las palabras sin arista entre ellos. D, SANO, CON ARISTA QUE "
        "FALTA: el arranque de campo compartido es real y el enlace ahorra que un lector rehaga la "
        "observacion dos veces. Queda declarada para la fase 04."
    ),
    827: (
        "POR QUE YA SE PUEDE JUZGAR, Y AQUI CAYERON LAS DOS JUNTURAS, NO UNA. La razon vieja "
        "bloqueaba por el banco 9.9 diciendo que el par tenia LOS DOS NODOS COSTURADOS y que el "
        "solape tocaba juntura por los dos lados. MEDIDO HOY, LAS DOS CIRUGIAS ESTAN HECHAS: "
        "voz_del_cliente_voc tiene SEIS pasos y fuente unica tras OP-F-04-COL y la fusion de "
        "OP-D-02; y ganar_comprension_del_cliente tiene SEIS pasos y no once, porque su bloque 7 a "
        "11, el del montaje del CRM, salio en la vuelta 31 con OP-F-04-COL hacia "
        "investigar_datos_cliente y conexion_personal_emocional. Lo que queda de el es exactamente "
        "el bloque 1 a 6 que la razon vieja llamaba la comprension del cliente. NINGUNO DE LOS DOS "
        "TIENE JUNTURA. "
        "LA LECTURA, CONTRA LOS SEIS PASOS DE CADA UNO. Lo compartido es UNA LINEA contra UNA "
        "LINEA: pasar un dia haciendo lo que hace tu cliente (su paso 4) contra observar "
        "directamente al cliente acompanandolo durante su trabajo real (paso 2 del superviviente). "
        "Lo propio de ganar_comprension_del_cliente es un procedimiento entero que el superviviente "
        "no tiene: investigar el FLUJO DE TRABAJO actual y sus interacciones con otras personas o "
        "areas, preguntar QUE OTRAS SOLUCIONES usa hoy y si el problema lo comparten mas personas, "
        "explorar QUE HARIA CAMBIAR SU COMPORTAMIENTO DE COMPRA (el precio, las caracteristicas o "
        "un nuevo estandar), identificar QUE PUBLICACIONES LEE Y A QUIEN SIGUE, y documentar con "
        "CRITERIOS CLAROS DE QUE CUENTA COMO VALIDADO. Y lo propio del superviviente que el otro no "
        "toca: la evaluacion preliminar de mercado, el analisis competitivo, la prueba de concepto "
        "y el contacto en ciclos cortos durante todo el desarrollo. Entregables distintos ademas. "
        "CONTINUA: D, los dos sanos. Libros distintos, The Startup Owner's Manual contra Winning at "
        "New Products. "
        "ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS CONTRA EL GRAFO: NO HAY NINGUNA. Y AQUI, A "
        "DIFERENCIA DEL 724 Y EL 755, NO SE DECLARA ARISTA QUE FALTA, y se dice el motivo en vez "
        "de repetir la formula: lo compartido es UNA linea en cada lado, los dos nodos ya tienen "
        "cableado propio denso (el superviviente doce siguientes, el otro cuatro previos y cuatro "
        "siguientes), y declarar un enlace por una sola linea compartida infla el grafo sin "
        "ensenarle nada al lector. DISCUTIBLE MARCADO: es el mas debil de los tres arreglos de "
        "esta tanda, y quien aplique el criterio de los otros dos dira que aqui tambien falta la "
        "arista."
    ),
}

NUEVA_CLASE = {724: "D", 755: "D", 827: "D"}


def main():
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    idx = {r["puesto_intra"]: r for r in V}

    lote = []
    for puesto in (724, 755, 827):
        r = idx[puesto]
        if r["clase"] != "B":
            print("ABORTA: el puesto %d no esta en B, esta en %s" % (puesto, r["clase"]))
            return 1
        vieja = r["razon"]
        nueva = (
            CABECERA
            + " LO QUE DECIA LA RAZON VIEJA, y se deja escrita ENTERA para que la correccion se "
            "pueda auditar (copiada del archivo por maquina, no transcrita): "
            + vieja
            + " FIN DE LA RAZON VIEJA. "
            + CUERPO[puesto]
        )
        print("=" * 78)
        print("PUESTO %d: %s -> %s   %s contra %s"
              % (puesto, r["clase"], NUEVA_CLASE[puesto], r["nodo_a"], r["nodo_b"]))
        print("  razon vieja: %d caracteres, copiada verbatim dentro de la nueva" % len(vieja))
        print("  razon nueva: %d caracteres" % len(nueva))
        assert vieja in nueva, "la razon vieja no quedo dentro de la nueva"
        lote.append({"puesto": puesto, "clase": NUEVA_CLASE[puesto], "razon": nueva})

    with io.open(LOTE, "w", encoding="utf-8", newline="\n") as fh:
        for x in lote:
            fh.write(json.dumps(x, ensure_ascii=False) + "\n")
    print("=" * 78)
    print("LOTE ESCRITO: %s  (%d entradas)" % (LOTE, len(lote)))
    print("GUARDA DEL ENCARGO: el 724 NO da A, asi que NO hay parada.")
    print("Siguiente paso, con este comando exacto:")
    print("  python scripts/corregir_veredicto.py docs/loop/_lote_v33b.jsonl")
    print()
    print("MARCADOR ESPERADO TRAS ESTE SEGUNDO VOLCADO, escrito ANTES de correrlo:")
    print("  n 3388, A 582, B 84, C 8, D 2714.")
    print("Si el instrumento da otra cosa, se PARA y se trae.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
