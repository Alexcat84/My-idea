# -*- coding: utf-8 -*-
"""vuelta37_build_lote_p5.py - CONSTRUYE EL LOTE DE LAS CUATRO RELECTURAS DE P.5 SOBRE OP-D-04.

SUCESOR DECLARADO de scripts/loop/_build_lote.py y del par de la vuelta 36
(vuelta36_volcado_910.py leia el lote de un fichero ya sellado por la vuelta 35).
LO QUE CAMBIA VA DICHO (regla 2): aqui NO hay propuesta sellada de una vuelta
anterior, porque la medicion de P.5 y la relectura ocurren en la MISMA vuelta.
Asi que la garantia de que la razon vieja va literal no puede venir de un sello:
viene de que ESTE script COPIA LA RAZON VIEJA DEL ARCHIVO POR MAQUINA y la
incrusta dentro de la nueva. Ni una letra de la razon vieja se teclea.

LAS CUATRO RELECTURAS, y ninguna cambia de clase:
  823  A -> A   brainstorming_divergente contra brainstorming_efectivo
  834  A -> A   brainstorming_divergente contra reglas_brainstorming
  844  A -> A   brainstorming_divergente contra generar_multiples_opciones
  585  D -> D   brainstorming_divergente contra pensamiento_convergente_divergente

POR QUE SE RELEEN SI NO CAMBIAN DE CLASE. P.5 no manda cambiar veredictos: manda
LEER el acto entero despues del destejido y antes de la fusion, y su alcance
adjudicado el 15 ago 2026 es el acto en operacion. Los cuatro se emitieron contra
un brainstorming_divergente de OCHO pasos que hoy tiene CUATRO, medido por las
dos varas (fecha y texto) en scripts/loop/vuelta37_p5_opd04.py. Una razon que
describe un nodo que ya no existe es papel que envejece (banco 9.10) aunque su
clase siga siendo la buena: se corrige con la vieja entera debajo.

GUARDAS, escritas para caer:
  1. los cuatro puestos existen en el archivo y estan en la clase que se espera.
  2. los seis nodos del acto que estos cuatro pares tocan tienen HOY los pasos que
     las razones nuevas afirman.
  3. la razon vieja del archivo de hoy queda LITERAL dentro de la nueva.
  4. el marcador NO se mueve: como ninguna relectura cambia de clase, A, B, C y D
     deben quedar exactamente donde estaban. Se imprime antes y despues.

Uso: python scripts/loop/vuelta37_build_lote_p5.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
LOTE = os.path.join(RAIZ, "docs", "loop", "_lote_v37_p5.jsonl")

PASOS_ESPERADOS = {
    "brainstorming_divergente": 4,
    "brainstorming_efectivo": 4,
    "reglas_brainstorming": 5,
    "generar_multiples_opciones": 3,
    "pensamiento_convergente_divergente": 4,
}

CABECERA = (
    "RELEIDA EL 19 ago 2026 POR P.5 DENTRO DE OP-D-04, Y LA CLASE NO CAMBIA: SIGUE {clase}. "
    "CORRECCION DECLARADA, con el texto viejo entero debajo. P.5 manda que cada acto se lea "
    "ENTERO DESPUES de su destejido y ANTES de su fusion, y su alcance quedo adjudicado el 15 "
    "ago 2026 por decision del fundador: solo dentro del acto en operacion, nunca fuera. Este "
    "par se emitio ANTES del destejido, y medido hoy con las dos varas del instrumento "
    "scripts/loop/vuelta37_p5_opd04.py (fecha de lectura contra fecha de cambio del fichero, y "
    "comparacion del texto de los pasos en el commit de la lectura contra el de hoy) resulta que "
    "brainstorming_divergente se leyo con OCHO pasos y hoy tiene CUATRO, porque OP-F-02 se llevo "
    "su bloque 5 a 8, el injerto de Mollick, entero a ideacion_con_ia_en_la_sesion. "
)

CUERPOS = {
    823: (
        "LO QUE LA RELECTURA MIDE, PASO POR PASO SOBRE LOS FICHEROS DE HOY, Y ES POR ESO QUE LA "
        "CLASE AGUANTA: la razon vieja localizo el solape ella misma, con estas palabras, EL "
        "SOLAPE DE ESTE PAR NO CRUZA LA JUNTURA, CAE COMPLETO EN LOS PASOS 1 A 4, EL TALLER DE "
        "TIM BROWN. Medido hoy, eso era exacto y sigue siendolo: el nucleo compartido que la "
        "razon vieja lista vive entero en los cuatro pasos que quedaron. Fijar y hacer visibles "
        "las reglas de diferir el juicio y construir sobre las ideas de otros es el paso 2 de "
        "brainstorming_divergente y son los pasos 1 y 2 de brainstorming_efectivo; generar sin "
        "filtrar prematuramente es el paso 3 del primero y vive en el diferir el juicio del "
        "paso 1 del segundo; separar la divergencia de la seleccion es el paso 4 del segundo y "
        "esta en el resumen y en el entregable del primero. LO PROPIO DE brainstorming_efectivo "
        "que la razon vieja nombraba SIGUE INTACTO: formar grupos donde la gente se conozca y "
        "tenga confianza, que es su paso 3. "
        "Y AQUI ESTA LO QUE SI ENVEJECIO, Y ES LA MITAD DE UNA FRASE: la razon vieja decia que "
        "LO PROPIO DE brainstorming_divergente SON EL REGISTRO VISUAL EN POST-ITS Y EL BLOQUE DE "
        "IA ENTERO. El registro visual sigue siendo su paso 4. EL BLOQUE DE IA YA NO ESTA EN EL "
        "NODO: se fue entero a ideacion_con_ia_en_la_sesion, medido por git contra el padre del "
        "commit de OP-F-02 y comprobado paso a paso, los cuatro identicos. LO PROPIO DE "
        "brainstorming_divergente, LEIDO HOY, ES OTRO Y ES MAS CHICO: la sala dedicada sin "
        "distracciones de su paso 1, el empujon de generar el mayor numero posible sin filtrar "
        "de su paso 3, y el registro visual de su paso 4. TRES gestos de taller, ninguno de "
        "ellos en el otro nodo. "
        "LA NOTA DE COSTURA DE LA RAZON VIEJA TAMBIEN ENVEJECIO Y SE CORRIGE: decia que "
        "brainstorming_divergente es COSTURA CONFIRMADA, OCHO PASOS CON LA JUNTURA EN EL PASO 5. "
        "Ya no: el destejido de OP-D-04 esta consumado, porque su unica costura y el injerto de "
        "fuente eran el mismo bloque y un solo corte sirvio a los dos frentes "
        "(scripts/loop/vuelta37_destejido_opd04.py). El nodo tiene cuatro pasos y ninguna "
        "juntura. "
        "LA CLASE NO SE PELEA Y SE DICE POR QUE, citando la regla y no inventandola: los dos "
        "nodos siguen siendo miembros del racimo censado Las reglas del brainstorming, "
        "verificado hoy en docs/RACIMOS_MIEMBROS.jsonl, que tiene CUATRO miembros vivos, "
        "reglas_brainstorming, brainstorming_divergente y brainstorming_efectivo de core mas "
        "brainstorming de quality. La REGLA FAMILIA DECLARADA, generalizada el 11 ago 2026 a "
        "todo racimo declarado, dice que un par cuyos DOS nodos pertenecen a un racimo ya "
        "declarado lleva razon familia declarada y NO pelea la clase, y que lo que si se anota "
        "es cualquier cosa NUEVA. Lo nuevo de esta relectura es lo de arriba: el bloque de IA "
        "salio y la costura se destejio. A SE SOSTIENE. "
        "ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS CONTRA EL GRAFO COMPILADO Y RESUELTA POR ALIAS: "
        "NO HAY NINGUNA, y no se declara, porque una A manda fusion y no enlace. "
        "DISCUTIBLE MARCADO: la A de este par no la sostiene la vara del contenido sino la regla "
        "FAMILIA DECLARADA, y quien quiera pelearla dira que tras la cirugia brainstorming_"
        "divergente conserva TRES gestos propios de cuatro pasos, que es mas de lo que tenia "
        "cuando la razon vieja lo llamo repeticion. Lo que lo impide es que la regla escrita "
        "manda no pelear la clase de un par de racimo declarado; la decision vive en la mesa del "
        "racimo, no aqui."
    ),
    834: (
        "LO QUE LA RELECTURA MIDE, Y ESTE ES EL CASO MAS LIMPIO DE LOS CUATRO: la razon vieja no "
        "cito ni una sola vez material del bloque que se fue. Su nucleo compartido, medido hoy "
        "sobre los dos ficheros, esta entero y en pie: fijar y hacer cumplir las reglas de "
        "diferir el juicio y de ir por cantidad es el paso 2 de brainstorming_divergente y el "
        "paso 2 de reglas_brainstorming; generar sin filtrar es el paso 3 del primero; capturar "
        "las ideas en post-its para poder moverlas es el paso 4 del primero y el paso 4 del "
        "segundo. Y LO PROPIO DE reglas_brainstorming QUE LA RAZON VIEJA LLAMO LO MAS CARO DE "
        "PERDER SIGUE ENTERO, las tres piezas: definir un enunciado claro del problema centrado "
        "en la necesidad del cliente es su paso 1, la INMERSION previa con visita de campo o "
        "entrevistas es su paso 3, y el calentamiento del Silly Cow es su paso 5. "
        "LO QUE SI ENVEJECIO ES SU ULTIMA FRASE, y es una nota de orden, no de contenido: decia "
        "que POR EL BANCO 9.9 EL PAR SE JUZGA HOY PESE A QUE brainstorming_divergente ES COSTURA "
        "CONFIRMADA, EL SOLAPE CAE ENTERO EN SUS PASOS 1 A 4 Y LA JUNTURA ESTA EN EL 5. Esa "
        "salvedad ya no hace falta: la juntura no existe, el destejido esta consumado y el nodo "
        "tiene cuatro pasos. La frase se conserva entera debajo porque es la prueba de que el "
        "lector de entonces ya habia colocado el solape en el lado que iba a sobrevivir, y "
        "acerto. "
        "LA CLASE NO SE PELEA POR LA MISMA REGLA QUE EN EL 823: los dos son miembros del racimo "
        "censado Las reglas del brainstorming, verificado hoy en docs/RACIMOS_MIEMBROS.jsonl. "
        "REGLA FAMILIA DECLARADA. A SE SOSTIENE, y esta vez sin ni una linea de la razon vieja "
        "que haya dejado de ser cierta sobre el contenido. "
        "ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS Y RESUELTA POR ALIAS: NO HAY NINGUNA, y no se "
        "declara, porque una A manda fusion. Libros distintos, Change by Design contra Business "
        "Model Generation, medido hoy en el campo fuente de los dos."
    ),
    844: (
        "LO QUE LA RELECTURA MIDE, Y ES EL PAR QUE MEJOR SE DEFENDIO SOLO: la razon vieja escribio "
        "su propia guarda contra esta cirugia, con estas palabras, ES LA TERCERA VEZ QUE ESTE "
        "NODO ENTRA A UN PAR Y LAS TRES VECES EL SOLAPE CAYO EN SUS PASOS 1 A 4, CON LA JUNTURA "
        "EN EL 5, O SEA EN EL BLOQUE DE TIM BROWN QUE LA CIRUGIA DEJA EN PIE. Medido hoy sobre "
        "los ficheros: acerto en todo. El nucleo compartido sigue entero, generar deliberadamente "
        "muchas alternativas antes de elegir es el paso 1 de generar_multiples_opciones y el paso "
        "3 de brainstorming_divergente, y construir sobre las ideas de los demas es el paso 2 del "
        "segundo y la polinizacion cruzada del paso 3 del primero. LO PROPIO DE generar_multiples_"
        "opciones sigue siendo UNO, el plazo claro para la fase de divergencia, su paso 2. Y LOS "
        "TRES QUE LA RAZON VIEJA LISTABA COMO PROPIOS DE brainstorming_divergente SIGUEN LOS "
        "TRES: la sala dedicada sin distracciones, las reglas explicitas de diferir el juicio y "
        "cantidad sobre calidad, y el registro visual en post-its. CERO de lo citado se movio. "
        "LA VARA SE VUELVE A CORRER HOY Y NO SE HEREDA. La prueba de reconocimiento de madre e "
        "hijo del banco 9.6.2 NO se cumple, y se dice en vez de forzarla: generar_multiples_"
        "opciones no cabe entero dentro de UN paso de brainstorming_divergente, porque su paso 1 "
        "cae en el paso 3 del otro y su paso 3 cae en el paso 2, o sea que lo cruza. Asi que se "
        "aplica el banco 9.22 en los dos sentidos: lo que generar_multiples_opciones anade es el "
        "plazo, UNA LINEA; lo que brainstorming_divergente anade son la sala, la regla y el "
        "post-it, y por la regla practica del informe 67.6 los tres son LINEA, acciones unicas y "
        "criterios sueltos, no procedimientos que obliguen a varias decisiones dentro de si ni "
        "que se repitan en el tiempo. LINEA EN LOS DOS SENTIDOS es el segundo polo del 9.22: "
        "REPITEN, clase A, y el arreglo es FUSION con las lineas repuestas en el superviviente. "
        "A SE SOSTIENE, ahora citando el 9.22 y no solo el 9.6.1. "
        "LO UNICO QUE SE CORRIGE ES LA NOTA DE COSTURA: la juntura del paso 5 ya no existe, el "
        "destejido de OP-D-04 esta consumado y el nodo tiene cuatro pasos. "
        "ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS Y RESUELTA POR ALIAS: NO HAY NINGUNA, y no se "
        "declara, porque una A manda fusion y no enlace. Los dos son del mismo libro, Change by "
        "Design, medido hoy."
    ),
    585: (
        "LO QUE LA RELECTURA MIDE, Y LA CLASE NO SE MUEVE PORQUE EL ARGUMENTO NO COLGABA DEL "
        "BLOQUE QUE SE FUE: la razon vieja abre diciendo LA SESION CONTRA LA DISCIPLINA MENTAL, Y "
        "SON NIVELES DISTINTOS, y ese corte se sostiene entero con los cuatro pasos de hoy. "
        "brainstorming_divergente sigue siendo el protocolo de la sesion: reunir al equipo sin "
        "distracciones, fijar las reglas de cantidad sobre calidad y diferir el juicio, generar "
        "sin filtrar, y registrar en post-its. pensamiento_convergente_divergente sigue sin dar "
        "protocolo de sesion: dedicar tiempo explicito a generar antes de buscar la solucion, la "
        "metafora del embudo que abre y estrecha, alternar a conciencia entre generacion y "
        "eliminacion, y aceptar que matar a los hijos favoritos es parte del oficio. Los cuatro "
        "pasos del segundo estan hoy identicos a los del commit de la lectura, medido por git. "
        "LO QUE SI ENVEJECIO ES LA DESCRIPCION, Y ES LA MITAD DE UNA ENUMERACION: la razon vieja "
        "describia brainstorming_divergente incluyendo Y DESPUES EL BLOQUE DE IA COMO PARTICIPANTE "
        "MAS, CON PERSONAS O ESTILOS DISTINTOS, EL LOTE GRANDE CON FILTRADO HUMANO EXPERTO Y EL "
        "CRUCE DE CONCEPTOS YA GENERADOS. NINGUNA DE ESAS CUATRO ESTA HOY EN EL NODO: las cuatro "
        "se fueron enteras a ideacion_con_ia_en_la_sesion con OP-F-02, comprobadas paso a paso e "
        "identicas. La descripcion se corrige y el veredicto no, porque aquel bloque no era lo "
        "que separaba a los dos nodos: lo que los separa es el nivel, y el nivel no cambio. "
        "LAS TRES OBSERVACIONES LATERALES DE LA RAZON VIEJA, VERIFICADAS UNA POR UNA HOY. Primera, "
        "el LIMITE DE LA REGLA FAMILIA DECLARADA: sigue siendo cierto, solo brainstorming_"
        "divergente esta en la nomina del racimo Las reglas del brainstorming y "
        "pensamiento_convergente_divergente no, verificado en docs/RACIMOS_MIEMBROS.jsonl, asi "
        "que la regla no aplica y el par se pelea normal. Segunda, que "
        "pensamiento_convergente_divergente ENLAZA A brainstorming_efectivo y es vecino del "
        "racimo sin ser miembro: sigue siendo cierto, y esta vuelta lo leyo, es la LD-86. "
        "Tercera, el defecto de campo de la fuente: sigue en pie, uno dice Change by Design, "
        "Revised and U y el otro Change by Design, la misma obra en dos grafias dentro del par. "
        "SIN ARISTA entre ellos, buscada hoy en los dos sentidos y resuelta por alias. D SE "
        "SOSTIENE, los dos sanos."
    ),
}


def leer_archivo():
    return [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]


def marcador(V):
    m = {}
    for v in V:
        m[v["clase"]] = m.get(v["clase"], 0) + 1
    return m


def pasos(nid):
    d = json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))
    return len(d.get("pasos_accionables") or [])


def main():
    V = leer_archivo()
    por_puesto = dict((int(v["puesto_intra"]), v) for v in V)

    print("=" * 78)
    print("GUARDAS DEL LOTE, CORRIDAS HOY")
    print("=" * 78)
    print("marcador ANTES: n %d  %s" % (len(V), marcador(V)))

    print("")
    print("guarda 2, los pasos de hoy:")
    for nid in sorted(PASOS_ESPERADOS):
        real = pasos(nid)
        ok = real == PASOS_ESPERADOS[nid]
        print("  %-38s hoy %d, la razon nueva dice %d  %s"
              % (nid, real, PASOS_ESPERADOS[nid], "OK" if ok else "DISCREPA"))
        if not ok:
            print("ABORTA guarda 2")
            return 1

    filas = []
    print("")
    print("guarda 1 y 3, puesto por puesto:")
    for puesto in sorted(CUERPOS):
        v = por_puesto.get(puesto)
        if v is None:
            print("ABORTA guarda 1: el puesto %d no esta en el archivo" % puesto)
            return 1
        clase = v["clase"]
        vieja = v["razon"]
        nueva = (CABECERA.format(clase=clase)
                 + CUERPOS[puesto]
                 + " LO QUE DECIA LA RAZON VIEJA, y se deja escrita ENTERA para que la"
                   " correccion se pueda auditar (copiada del archivo por maquina, no"
                   " transcrita): " + vieja + " FIN DE LA RAZON VIEJA.")
        if vieja not in nueva:
            print("ABORTA guarda 3: la razon vieja del %d no queda literal dentro" % puesto)
            return 1
        filas.append({"puesto": puesto, "clase": clase, "razon": nueva})
        print("  %-5d clase %s -> %s   razon vieja %d caracteres, nueva %d, vieja LITERAL dentro: si"
              % (puesto, clase, clase, len(vieja), len(nueva)))

    with io.open(LOTE, "w", encoding="utf-8") as fh:
        for f in filas:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")

    print("")
    print("guarda 4, el marcador esperado TRAS el volcado, escrito ANTES de volcar:")
    print("  ninguna de las cuatro cambia de clase, asi que el marcador debe quedar")
    print("  EXACTAMENTE igual: %s" % marcador(V))
    print("")
    print("LOTE ESCRITO en %s con %d filas." % (os.path.relpath(LOTE, RAIZ), len(filas)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
