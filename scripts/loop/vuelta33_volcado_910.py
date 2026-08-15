# -*- coding: utf-8 -*-
"""vuelta33_volcado_910.py

TAREA 1.3 de la vuelta 33: construye el LOTE de correccion de los tres congelados
que la relectura de OP-D-01 (vuelta 32) dejo leidos y sin volcar, adjudicado por
el fundador el 15 ago 2026 con el banco 9.10 como mecanismo.

  494  A -> C   (banco 9.22, tercer ejemplar, con enlace mutuo declarado)
  592  B -> D   (arista que falta hacia mvp_catalogo_tecnicas)
  830  B -> D   (arista que falta hacia prueba_mvp_alta_fidelidad)

NO ESCRIBE EN EL ARCHIVO. Escribe el lote y ya: quien sustituye es
scripts/corregir_veredicto.py, que es el instrumento de la casa para esto y el
que comprueba que el total no cambie. Un script nuevo que escribiera el archivo
de veredictos seria una segunda fuente de verdad para la misma operacion.

LA RAZON VIEJA NO SE TECLEA: se COPIA del archivo, verbatim, por maquina. Ese es
el punto de la regla 8 del EJECUTOR.md (una correccion que tapa lo que corrige no
se puede auditar) y tambien el de la regla 1 (lo que existe en un instrumento no
se transcribe a mano).

Uso: python scripts/loop/vuelta33_volcado_910.py
Salida: docs/loop/_lote_v33.jsonl, y el texto entero por stdout para el registro.
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
LOTE = os.path.join(RAIZ, "docs", "loop", "_lote_v33.jsonl")

FECHA = "15 ago 2026"

CABECERA = {
    494: (
        "REESCRITA EL %s POR EL DESTEJIDO DEL EMBLEMA, y la clase pasa de A a C. "
        "CORRECCION DECLARADA. La relectura se hizo en la vuelta 32 dentro de OP-D-01 "
        "movimiento 3 y quedo leida y publicada sin volcar; el volcado lo adjudica el "
        "fundador el 15 ago 2026 con el banco 9.10 como mecanismo, y se ejecuta aqui con "
        "su barrido de tablas derivadas en el mismo acto." % FECHA
    ),
    592: (
        "REESCRITA EL %s POR EL DESTEJIDO DEL EMBLEMA, y la clase pasa de B a D. "
        "CORRECCION DECLARADA. La causa del congelamiento cayo y el volcado lo adjudica el "
        "fundador el 15 ago 2026 con el banco 9.10 como mecanismo." % FECHA
    ),
    830: (
        "REESCRITA EL %s POR EL DESTEJIDO DEL EMBLEMA, y la clase pasa de B a D. "
        "CORRECCION DECLARADA. La causa del congelamiento cayo y el volcado lo adjudica el "
        "fundador el 15 ago 2026 con el banco 9.10 como mecanismo." % FECHA
    ),
}

CUERPO = {
    494: (
        "POR QUE CAMBIA, Y EL MOTIVO ES QUE EL UNICO APOYO DE LA A DEJO DE EXISTIR. "
        "La razon vieja sostenia la A en una sola frase, los pasos 11 al 14 del primero son "
        "el nucleo del segundo dicho otra vez. MEDIDO HOY sobre el arbol: principio_calidad_mvp "
        "tiene SIETE pasos y no catorce. Su bloque 11 a 14 se lo llevo OP-F-03 y su bloque 6 a 10 "
        "se fundio con el 1 a 5 por P.19 dentro de OP-F-04-HOR, las dos en la vuelta 32. "
        "Y el informe habia escrito la condicion por adelantado, seccion 9139: si el destejido "
        "conserva la narracion de la CALIDAD, el par deja de repetir. La conserva. "
        "LA VARA DEL BANCO 9.6.1, APLICADA EN LOS DOS SENTIDOS Y SOBRE DOS LINEAS DISTINTAS, "
        "que es la comprobacion que el banco 9.22 exige para separar esta figura de la duplicacion. "
        "PRIMER SENTIDO: principio_calidad_mvp dice en su paso 3, en UNA LINEA, lanza al mercado "
        "real lo antes posible versiones simplificadas o hacky de las features complejas aceptando "
        "que fallaran, y mide la reaccion real de los clientes; y producto_minimo_viable trae el "
        "PROCEDIMIENTO entero de esa linea en sus seis pasos de hoy, bajar la hipotesis critica al "
        "problema minimo que alguien pagaria por resolver, disenar la version mas simple con el "
        "conjunto minimo desde la propia vision, no agregar funciones extra salvo la excepcion que "
        "sin ella no se puede vender, lanzar solo a los earlyvangelists y no al mercado masivo, "
        "medir la reaccion real y no la opinion, e iterar o cambiar de rumbo en ciclos cortos. "
        "SEGUNDO SENTIDO, Y SOBRE OTRA LINEA: producto_minimo_viable dice en sus pasos 2 y 3, en "
        "UNA LINEA, la version mas simple y sin funciones extra que no sean necesarias para "
        "aprender; y principio_calidad_mvp trae el PROCEDIMIENTO de esa, preguntarse si pulir "
        "contribuye directamente al aprendizaje y usar esa pregunta para resistir la presion del "
        "equipo, no asumir que el estandar de calidad de la industria ni los requerimientos "
        "heredados de un cliente anterior son lo que el mercado valora, distinguir el defecto que "
        "dificulta el aprendizaje, inaceptable, de la baja fidelidad estetica, aceptable, y usar el "
        "feedback sobre la version simple para decidir si invertir en alta calidad tradicional. "
        "SON DOS LINEAS DISTINTAS, la del lanzamiento y la de la simplicidad, una en cada nodo, y "
        "cada uno expande la del otro: NINGUNO ES LA MADRE. Por el banco 9.22 el par es SANO CON "
        "FIGURA, clase C, y el arreglo es ENLACE MUTUO, dos aristas. FUNDIRLOS SERIA EL ERROR CARO "
        "que el propio 9.22 nombra, porque borraria los dos procedimientos para dejar un nodo con "
        "dos lineas sueltas. ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS CONTRA EL GRAFO: NO HAY "
        "NINGUNA, ni principio_calidad_mvp nombra a producto_minimo_viable ni al reves. "
        "TERCER EJEMPLAR DEL 9.22 en todo el archivo, tras el 1077 y el 1240 que el propio banco "
        "nombra, Y EL PRIMERO QUE NACE CON EL ENLACE SIN PONER: los otros dos llegaron cableados. "
        "Las dos aristas quedan DECLARADAS para la fase 04 y no se ponen aqui: el campo "
        "aristas_nuevas de OP-D-01 esta vacio y los enlaces son fase 04, que va despues. "
        "FUENTES: The Lean Startup mas The Hard Thing About Hard Things contra The Lean Startup. "
        "DISCUTIBLE MARCADO, y se marca antes de saber si acierto: el informe habia escrito que "
        "este par SERIA D. Lo leo C porque la figura de los dos sentidos solo aparece cuando los "
        "dos nodos ya estan estables, y eso es DESPUES de aquella prediccion. Solo hay DOS "
        "ejemplares de esta figura en 3.388 pares: proponer el tercero es lo mas discutible de "
        "esta relectura, y quien lea las dos lineas como la misma linea dira D."
    ),
    592: (
        "POR QUE CAMBIA: LA CAUSA DEL CONGELAMIENTO CAYO, Y NO POR DECRETO. La razon vieja se "
        "abstenia por el TOQUE UNICO del banco 9.4, un nodo averiado por dentro contamina todos "
        "los pares en los que entra porque el veredicto se emite contra un texto que va a cambiar. "
        "EL TEXTO YA CAMBIO Y YA ES ESTABLE: producto_minimo_viable quedo en SEIS pasos y CINCO "
        "condiciones el 15 ago 2026 por OP-D-01 movimiento 1, medido hoy sobre el arbol, y no en "
        "veintidos pasos y diez condiciones. LA LECTURA, CONTRA LOS SEIS PASOS DE HOY Y NO CONTRA "
        "LOS VEINTIDOS DE ANTES: mvp_catalogo_tecnicas trae la ESCALERA DE COSTO, empezar por el "
        "MVP mas barato posible, hoja de datos, folleto o storyboard, subir en sofisticacion solo "
        "si lo primero promete, y usar herramientas a mano como un telefono antes de pagar "
        "produccion profesional. NINGUNO DE LOS SEIS PASOS DEL EMBLEMA NOMBRA EL COSTE, NI EL TIPO "
        "DE PROTOTIPO, NI LA HERRAMIENTA. Lo que comparten es el arranque, identificar la hipotesis "
        "critica antes de elegir, que es UNA linea. Por la vara del banco 9.6.1 esto es CONTINUA y "
        "no repeticion: el segundo trae procedimiento propio que el primero no tiene en ninguno de "
        "sus pasos. D, SANO, CON ARISTA QUE FALTA hacia mvp_catalogo_tecnicas. ARISTA, BUSCADA HOY "
        "EN LOS DOS SENTIDOS CONTRA EL GRAFO: NO HAY NINGUNA, que es lo que la razon vieja ya "
        "decia con las palabras sin arista. Libros distintos ademas, Value Proposition Design "
        "contra The Lean Startup, y eso no cambia nada porque la vara no pregunta por el autor. "
        "LA CLASE SE SOSTIENE CON LA PRACTICA MEDIDA DEL ARCHIVO Y NO CON MI GUSTO: barrido hoy el "
        "fichero entero de veredictos, los 207 cuya razon nombra ARISTA QUE FALTA son D, los 207, "
        "sin una sola excepcion en otra clase."
    ),
    830: (
        "POR QUE CAMBIA: LA CAUSA DEL CONGELAMIENTO CAYO, Y ES LA MISMA DEL 592. La razon vieja "
        "bloqueaba por el banco 9.9, la posicion del solape, diciendo que el solape tocaba todas "
        "las junturas del emblema porque era una de las ordenes que repetia CUATRO VECES. "
        "MEDIDO HOY: producto_minimo_viable tiene SEIS pasos, esa orden vive en UNO SOLO, el paso "
        "4, lanza tu primera version a tus primeros usuarios, early adopters o earlyvangelists, no "
        "al mercado masivo, y EL NODO YA NO TIENE JUNTURAS QUE TOCAR, porque su costura de fuente "
        "unica quedo colapsada el 15 ago 2026 por OP-D-01 movimiento 1. LA LECTURA, CONTRA LOS "
        "SEIS PASOS DE HOY: prueba_mvp_alta_fidelidad trae el AISLAMIENTO DE LA PRUEBA, decidir un "
        "NUMERO LIMITADO de clientes invitados a probar, incluir una llamada a la accion clara, "
        "medir cuantas visitas hacen falta antes de que alguien empiece a usarlo, medir cuantos "
        "usuarios lo recomiendan a amigos y que tan rapido empiezan, y EVITAR publicidad, prensa o "
        "demostraciones publicas durante la prueba. NINGUNO DE LOS SEIS PASOS DEL EMBLEMA DICE "
        "NADA DE ESO: el emblema manda a quien mostrar, y el otro manda como aislar la prueba y "
        "que medir en ella. Por la vara del banco 9.6.1 es CONTINUA. D, SANO, CON ARISTA QUE FALTA "
        "hacia prueba_mvp_alta_fidelidad. ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS CONTRA EL GRAFO: "
        "NO HAY NINGUNA, y esto es lo que la razon vieja NO habia mirado. "
        "LA CLASE SE SOSTIENE CON LA PRACTICA MEDIDA DEL ARCHIVO: los 207 veredictos cuya razon "
        "nombra ARISTA QUE FALTA son D, los 207, barrido hoy. "
        "DISCUTIBLE MARCADO: la lectura contraria es que mostrar solo a los earlyvangelists sigue "
        "siendo LA MISMA orden en los dos nodos y que el solape, aunque ya no toque juntura, "
        "bastaria para A. Lo leo D porque el otro nodo trae un procedimiento entero de medicion "
        "que el emblema no tiene, y la vara pesa procedimiento contra linea, no cuenta solapes."
    ),
}

NUEVA_CLASE = {494: "C", 592: "D", 830: "D"}


def main():
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    idx = {r["puesto_intra"]: r for r in V}

    lote = []
    for puesto in (494, 592, 830):
        r = idx[puesto]
        vieja = r["razon"]
        nueva = (
            CABECERA[puesto]
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
    print("EL ARCHIVO NO SE TOCA AQUI. El siguiente paso es, y con este comando exacto:")
    print("  python scripts/corregir_veredicto.py docs/loop/_lote_v33.jsonl")
    print()
    print("MARCADOR ESPERADO TRAS EL VOLCADO, escrito ANTES de correrlo para que la")
    print("comprobacion valga: n 3388, A 582, B 87, C 8, D 2711.")
    print("Si el instrumento da otra cosa, se PARA y se trae, por la letra del encargo.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
