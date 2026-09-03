# -*- coding: utf-8 -*-
r"""vuelta164_tarea3_4_veredictos.py . TAREAS 3 y 4 de la vuelta 164.

LOS DOS VEREDICTOS DE LA RELECTURA CONJUNTA, ESCRITOS EN EL REGISTRO PARA QUE SE
PUEDAN AUDITAR. Adjudicaciones 6.4 y 6.5 del acta 163.

  - `LD-OPC05-101`: SE SOSTIENE EN `D`. El acta 163 exige que su veredicto deje
    de vivir en el asunto del commit `1fa1bac9` y se publique; lo que se publica
    aqui es la RE DERIVACION de la `D` con la frase de `P.5.1` y sus CUATRO
    EJEMPLARES delante y SIN apoyarse en la `LD-OPC05-027` ni en la
    `LD-OPC05-004`, que la razon vigente cita y que NO son ejemplares de la vara
    congelada.
  - `LD-OPC05-005`: PASA DE `C` A `D`. Es CLASE PUBLICADA QUE SE MUEVE y es
    CAIDA DE CLASE DEL EJECUTOR, de la lectura de la vuelta 159 que la devolvio
    a `C` y de la relectura de la 161 que la sostuvo. Va con correccion
    declarada, sin borrar una linea, y con recomputo.

EL MOTOR ES EL DE LA CASA Y NO SE CLONA: `vuelta159_motor_veredictos.aplicar`,
con sus guardas (frontera con `sha256` de `dataset/`, censo y aristas antes y
despues, `n` en 3.388, prefijo intacto en las 154 razones, ningun par movido,
ninguna clase a `A`, y la cita que no puede declarar una clase distinta de la
del campo).

USO:  python scripts/loop/vuelta164_tarea3_4_veredictos.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta159_motor_veredictos as motor  # noqa: E402

MARCA = "RELECTURA CONJUNTA DE LA VUELTA 164"


def cabeza(vieja, nueva):
    if nueva != vieja:
        return ("  [CORRECCION DECLARADA, %s (2026-09-03), Y AQUI VIVEN LAS "
                "ADJUDICACIONES 6.4 Y 6.5 DEL ACTA 163, ANADIDA SIN BORRAR NADA "
                "DE LO ANTERIOR: LA CLASE PASA DE %s A %s. " % (MARCA, vieja, nueva))
    return ("  [%s (2026-09-03), Y AQUI VIVEN LAS ADJUDICACIONES 6.4 Y 6.5 DEL "
            "ACTA 163, ANADIDA SIN BORRAR NADA DE LO ANTERIOR: LA CLASE SE QUEDA "
            "EN %s. " % (MARCA, vieja))


def nota_md(vieja, nueva, motivo):
    if nueva != vieja:
        return ("CORRECCION DECLARADA (vuelta 164, RELECTURA CONJUNTA, "
                "adjudicacion 6.5 del acta 163): la clase pasa de ~~%s~~ a %s. "
                "%s." % (vieja, nueva, motivo[:260]))
    return ("RELECTURA CONJUNTA (vuelta 164, adjudicacion 6.4 del acta 163): la "
            "clase SE SOSTIENE en %s y su veredicto queda RE DERIVADO de la "
            "frase de P.5.1 y sus cuatro ejemplares, sin la 027 ni la 004." % vieja)


V = {
    "LD-OPC05-101": ("D",
        "LA CLASE SE SOSTIENE EN D Y SU VEREDICTO SE PUBLICA, QUE ES LO QUE LA "
        "ADJUDICACION 6.4 DEL ACTA 163 EXIGE: hasta hoy la unica sede de esta "
        "lectura era el asunto del commit 1fa1bac9, y un veredicto que vive en "
        "un asunto de commit no se puede auditar. "
        "LA D NO SE HEREDA: SE RE DERIVA CON LA VARA CONGELADA Y SIN LAS DOS SUB "
        "VARAS QUE LA RAZON VIGENTE CITA. La correccion de la vuelta 160 tumbo "
        "la LINEA 2 con la letra de la LD-OPC05-027 (la remision no es "
        "procedimiento) y la de la LD-OPC05-004 (una orden con criterio de "
        "parada no es metodo), y NINGUNA DE LAS DOS ES EJEMPLAR DE P.5.1: "
        "medido por el dossier de la vuelta 163 en su seccion F "
        "(docs/loop/SALIDA_V163_T1B_DOSSIER_101.txt), CIFRA sub varas citadas "
        "en la razon que NO son ejemplares de P.5.1: 2. Eso NO invalida la D: "
        "obliga a re derivarla, y aqui se re deriva. "
        "LA VARA, LEIDA HOY DEL BANCO Y NO DE MEMORIA: la segunda linea de un "
        "par solo cuenta como expansion si trae PROCEDIMIENTO PROPIO, y no solo "
        "EL NOMBRE DE OTRO. Mas sus cuatro ejemplares, que son la vara tanto "
        "como la frase: 052 y 095 ACEPTAN, 122 y 100 EXCLUYEN. "
        "LA LINEA 1 NO ESTA EN DISCUSION Y ES LIMPIA: el paso 8 de "
        "search_for_business_model (usar el Business Model Canvas como "
        "herramienta de planificacion flexible) lo expanden los doce pasos de "
        "lienzo_modelo_negocio, que son el procedimiento entero del instrumento "
        "que esa linea nombra. "
        "LA PREGUNTA DEL AUDITOR, CONTESTADA CON SUS PALABRAS: los pasos 3, 4 y "
        "5 de search, SIN EL PASO 2, NO PASAN LA FRASE DE P.5.1. Y va uno a uno. "
        "PASO 3 (aplica el proceso de Customer Development para salir a probar "
        "cada hipotesis con clientes reales): NOMBRA UN CUERPO EXTERNO Y NO "
        "ENUMERA NADA DE EL. Contra el ejemplar que la vara ACEPTA: en la 052 el "
        "paso que pasa es LAS 6 PREGUNTAS DE CHOPRA Y MEINDL, y pasa porque "
        "ENUMERA sus seis dimensiones dentro de la propia linea (cantidad por "
        "lote, tiempo de respuesta, variedad, nivel de servicio, precio, tasa de "
        "innovacion). El paso 3 de search nombra Customer Development y no "
        "enumera ni uno de sus pasos. La segunda mitad de la frase de P.5.1 "
        "('y no solo el nombre de otro') cae exactamente ahi, y para decirlo NO "
        "hace falta la 027: lo dice la frase con el ejemplar 052 al lado. "
        "PASO 4 (evita montar estructuras o roles de ejecucion antes de validar "
        "el modelo): ES UNA PROHIBICION, no un procedimiento. No dice que hacer, "
        "dice que no hacer, y no produce nada. Ninguno de los cuatro ejemplares "
        "acepta una linea de esta forma. "
        "PASO 5 (itera y pivota segun la evidencia recogida hasta encontrar un "
        "modelo repetible y escalable): ORDEN MAS COMPLEMENTO MAS CRITERIO DE "
        "PARADA. Tiene el 'hasta', pero no dice QUE cambiar ni COMO. Contra el "
        "ejemplar 095, que la vara ACEPTA: sus cinco pasos de process tracing "
        "son recolectar datos crudos, construir el relato del dominio, aplicar "
        "conceptos dependientes, buscar patrones entre los dos relatos y "
        "documentar, o sea CINCO OBJETOS DISTINTOS que se encadenan y producen "
        "un entregable propio. El paso 5 de search es un solo verbo con su "
        "condicion de parada. De la especie de la 122, no de la de la 095. "
        "Y NO SE LEEN SOLO POR SEPARADO: LOS TRES JUNTOS TAMPOCO PASAN, porque "
        "de los tres solo dos producen algo (el 3 produce evidencia y el 5 la "
        "consume; el 4 no produce nada), y el nucleo productivo del 3 esta "
        "delegado entero a un cuerpo que no se enumera. Una secuencia de dos "
        "terminos con el primero delegado no es un metodo secuenciado entero. "
        "POR QUE EL PASO 2 NO SE PUEDE CONTAR AQUI, Y NO ES POR PEDIRLO EL "
        "AUDITOR: el paso 2 de search (lista explicitamente las hipotesis de tu "
        "modelo de negocio, mercado, cliente, producto, canal y precio, marcadas "
        "como no probadas) ES EL UNICO DE ESA VECINDAD QUE ENUMERA, o sea el "
        "unico con forma de 052, PERO YA ESTA DEL LADO DE LA DIRECCION LIMPIA: "
        "la propia razon de la vuelta 160 lo pone ahi con todas sus letras ('el "
        "paso 8 de search y su paso 2 los expanden los doce pasos del lienzo'). "
        "Contarlo tambien como expansion de la linea 2 lo pondria en LOS DOS "
        "LADOS, que es exactamente la figura que el 9.22 excluye y por la que la "
        "vuelta 157 tumbo la LD-OPC05-005. "
        "LO QUE LE CONCEDO AL AUDITOR, Y NO ME LO CALLO PORQUE ME CONVENGA: "
        "TIENE RAZON EN QUE EL SEGUNDO CRITERIO DE LA 100 NO SIRVE AQUI. En la "
        "100 se escribio que 'un procedimiento que no recibe el vacio no puede "
        "ser el como se llena ese vacio', y en la 101 search SI RECIBE el "
        "lienzo: su entregable es 'un lienzo de hipotesis de modelo de negocio "
        "marcado explicitamente como no probado'. O sea que ese criterio, que "
        "en la 100 fue una de las tres patas, AQUI NO TUMBA NADA. La D se "
        "sostiene SOLO por la primera pata, LA FORMA, que es la que la frase "
        "congelada mide. "
        "Y EL CRUCE DE ENTREGABLES NO SE USA, POR LA ADJUDICACION 6.3 DEL ACTA "
        "163: es corroborador y no decisor. Ademas, mecanizado sobre los cuatro "
        "ejemplares reproduce 1 de 4 (dossier de la 163, seccion E, y recomputado "
        "hoy en docs/loop/SALIDA_V164_T4_DOSSIER_005.txt): un corroborador que "
        "solo acierta una parte de su propia vara no puede sostener un veredicto, "
        "ni a favor ni en contra. "
        "LA CLASE NO SE MUEVE Y LA VARA NO SE TOCA: esta lectura no estrecha ni "
        "ensancha P.5.1, y no usa ninguna sub vara que no este en ella. Dossier "
        "en docs/loop/SALIDA_V163_T1B_DOSSIER_101.txt"),

    "LD-OPC05-005": ("D",
        "LA CLASE PASA DE C A D Y ES CAIDA DE CLASE MIA, NO DEL AUDITOR: corrige "
        "MI lectura del lote 2 de la vuelta 159, que la devolvio de D a C, y MI "
        "relectura de la vuelta 161, que la sostuvo en C. El auditor trajo el "
        "caso en la seccion 3.1 del acta 163; lo que aqui se publica es la "
        "verificacion contra los dos nodos, no su prosa, y se declara que lo "
        "decisivo NO es su pluma sino UNA RESERVA QUE MI PROPIA RELECTURA DE LA "
        "161 DEJO ESCRITA Y QUE HOY VENCE. "
        "LA VARA, LEIDA HOY DEL BANCO: la segunda linea de un par solo cuenta "
        "como expansion si trae PROCEDIMIENTO PROPIO, y no solo el nombre de "
        "otro. Mas sus cuatro ejemplares: 052 y 095 ACEPTAN, 122 y 100 EXCLUYEN. "
        "LA LINEA 1 NO ESTA EN DISCUSION Y SIGUE SIENDO MUY FUERTE: el paso 2 de "
        "aim_of_leadership (investigar las causas de raiz del sistema que afectan "
        "el desempeno general) lo expanden los QUINCE pasos de "
        "causas_comunes_vs_especiales, que son su como se hace entero, con "
        "instrumento (grafico de corrida o de control), limites calculados, "
        "reglas de senal y entregable propio. UNA DIRECCION LIMPIA. "
        "LA LINEA 2 NO PASA LA VARA, Y LA TUMBA MI PROPIA RESERVA DE LA 161. Mi "
        "relectura de esa vuelta sostuvo la C y se marco DISCUTIBLE con estas "
        "palabras, que quedan escritas arriba en esta misma razon: 'el lado que "
        "expande la linea 2 es FINO, y su paso 3 leido solo seria orden mas "
        "complemento, o sea de la especie que el ejemplar 122 excluye; SE "
        "SOSTIENE PORQUE LOS TRES PASOS LEEN COMO SECUENCIA, no porque ninguno "
        "de ellos solo procedimente'. O sea que la C descansaba ENTERA sobre que "
        "los TRES pasos (1, 3 y 5 de aim_of_leadership) forman secuencia. "
        "Y EL PRIMERO DE ESOS TRES NO PUEDE ESTAR AHI, POR LO QUE ESTA MISMA "
        "RAZON YA DECIA ANTES DE HOY: la vuelta 157 declaro, y la relectura "
        "conjunta de la 159 lo RE CONFIRMO por escrito, que el paso 1 de "
        "aim_of_leadership (identificar quien esta fuera de lo esperado) y el "
        "paso 13 de causas_comunes_vs_especiales (dar seguimiento y apoyo a "
        "quienes caen fuera de las tolerancias del grupo) SI COLAPSAN en la "
        "misma linea. Un paso que REPITE la linea no puede ser el como se hace "
        "esa linea. Medido hoy y no citado de memoria "
        "(docs/loop/SALIDA_V164_T4_DOSSIER_005.txt, seccion E): de los seis "
        "pasos de aim_of_leadership, el paso 1 es el de MAYOR solape lexico con "
        "el paso 13, y el solape medio de los otros cinco es una fraccion del "
        "suyo. La medicion no decide sola y se declara asi; lo que decide es que "
        "el colapso ya estaba establecido en el registro desde la 157. "
        "QUITADO EL PASO 1, QUEDAN EL 3 Y EL 5, Y NINGUNO DE LOS DOS TRAE "
        "PROCEDIMIENTO PROPIO. PASO 3 (disenar formas de ayuda individual o de "
        "reconocimiento segun corresponda): ORDEN MAS COMPLEMENTO MAS UNA "
        "CONDICION VAGA. No trae metodo, ni instrumento con autor, ni secuencia, "
        "ni entregable propio, que son las cuatro palabras con las que la razon "
        "de la 100 excluyo su paso 2. PASO 5 (reconocer y estudiar a quienes "
        "tienen un desempeno excepcional para replicar sus metodos): ORDEN MAS "
        "COMPLEMENTO MAS FINALIDAD. No dice COMO se estudia ni con que "
        "instrumento ni que produce; y ademas cubre UNA SOLA de las dos colas de "
        "la linea 13, la alta, cuando la linea habla de quienes caen fuera de "
        "las tolerancias en cualquier direccion. Los dos son de la especie del "
        "122 (revisa e integra practicas seguras en cada etapa de tu trabajo) y "
        "de la del 100 (investigar, y despues que investigar), no de la del 052 "
        "ni de la del 095. "
        "Y EL EXISTENCIAL DE LA 6.3 DEL ACTA 158 SE RECORRIO ENTERO ANTES DE "
        "DECIRLO: descartar UN par no descarta la figura, asi que se barrio la "
        "direccion en disputa completa, que es preguntar QUE LINEA DE "
        "causas_comunes_vs_especiales LA EXPANDE UN PROCEDIMIENTO DE "
        "aim_of_leadership. LA RESPUESTA ES NINGUNA, Y EL MOTIVO ES ESTRUCTURAL "
        "Y MEDIBLE: aim_of_leadership tiene SEIS pasos, los seis son las tres "
        "responsabilidades de su propio resumen reescritas como ordenes, ninguno "
        "enumera un instrumento con autor, ninguno trae criterio de parada, y su "
        "entregable es UN PLAN DE LIDERAZGO, o sea un documento, no un metodo "
        "aplicable a la linea de otro nodo. Los tres pares mas fuertes que se "
        "descartan van nombrados. PAR DESCARTADO 1, el mas fuerte: el paso 7 de "
        "causas (si la causa es del sistema, redisenar el proceso en lugar de "
        "sancionar al individuo) contra el paso 4 de aim (trabajar de forma "
        "continua en mejorar el sistema para todos, no solo en corregir "
        "personas). SE DESCARTA porque el paso 4 de aim es LA MISMA FRASE dicha "
        "con otras palabras, no su como se hace: otro colapso, de la especie del "
        "que la 157 ya caza. PAR DESCARTADO 2: el paso 15 de causas (analizar la "
        "distribucion de errores entre todas las personas usando limites de "
        "control) contra el paso 6 de aim (buscar reducir la variabilidad de "
        "desempeno entre personas dentro del mismo sistema). SE DESCARTA porque "
        "LA DIRECCION ESTA AL REVES: el que trae el procedimiento es causas (los "
        "limites de control) y el que ordena es aim, o sea que ese par refuerza "
        "la direccion LIMPIA y no abre la segunda. PAR DESCARTADO 3: el paso 11 "
        "de causas (dar seguimiento a la moral del equipo y la tasa de errores "
        "tras el cambio de enfoque) contra el paso 3 de aim (disenar formas de "
        "ayuda o de reconocimiento). SE DESCARTA porque los sujetos son "
        "distintos, moral y tasa de errores contra ayuda individual, y sujeto "
        "distinto es la definicion de D. "
        "QUITADA LA LINEA 2, QUEDA EXACTAMENTE UNA SOLA DIRECCION, Y LA MISMA "
        "VARA QUE ESCRIBIO 'UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR "
        "CONTINUA' en la LD-OPC05-004 y en la LD-OPC05-100 da D aqui tambien. "
        "EL CRUCE DE ENTREGABLES NO SE USA COMO DECISOR (adjudicacion 6.3 del "
        "acta 163) Y ADEMAS NO DICE NADA EN ESTE PAR: medido hoy da NINGUNO, "
        "ningun entregable nombra al otro. Se publica para que no se herede como "
        "si hubiera dicho algo. "
        "LO QUE ESTO ES Y LO QUE NO ES, DICHO SIN ADORNO: ES CAIDA DE CLASE MIA "
        "y cuenta para el credito del ejecutor. NO se declara PARADA: la racha "
        "de cifra publicada esta en CERO por la decision del fundador del 3 sep "
        "2026, medida y publicada por el propio auditor en la seccion 7 del acta "
        "163, y la regla pide DOS TANDAS SEGUIDAS. Quien cuenta la racha es el "
        "auditor y no yo; lo que hago es declararla y dejarla contable. "
        "Y UNA COSA MAS QUE NO ME CALLO PORQUE ME FAVORECE AL REVES: la ciega "
        "del auditor de la vuelta 161 dio C sobre este mismo par y COINCIDIO con "
        "la clase de entonces; la de la 163 da D. Dos ciegas de la misma pluma "
        "con letras distintas sobre el mismo par, y el propio auditor lo declaro "
        "antes que nadie. ESTA CLASE NO SE MUEVE POR ESA SEGUNDA CIEGA: se mueve "
        "porque mi reserva de la 161 vencio contra los nodos. Dossier en "
        "docs/loop/SALIDA_V164_T4_DOSSIER_005.txt"),
}


def main():
    return motor.aplicar(
        "VUELTA 164, TAREAS 3 Y 4: LOS DOS VEREDICTOS DE LA RELECTURA CONJUNTA",
        V, MARCA, cabeza, nota_md, ids_esperados=list(V))


if __name__ == "__main__":
    raise SystemExit(main())
