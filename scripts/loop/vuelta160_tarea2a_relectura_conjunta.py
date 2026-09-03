# -*- coding: utf-8 -*-
"""vuelta160_tarea2a_relectura_conjunta.py . TAREA 2.a DE LA VUELTA 160.

`LD-OPC05-100`, LA UNA EN DISPUTA, LEIDA CONTRA LOS NODOS Y DECIDIDA CON LA VARA
(acta 159, adjudicacion 6.3). El auditor escribio su caso en la seccion 3.2 del
acta 159 y dijo con todas sus letras que no lo decide su pluma: MI LECTURA NO ES
LA VARA, EL NODO LO ES. Lo que se publica aqui es lo que se midio contra los
nodos, con el dossier `docs/loop/SALIDA_V160_T2A_DOSSIER.txt` delante y con el
dossier de contraste `docs/loop/SALIDA_V160_T2A_CONTRASTE.txt` al lado.

AQUI VIVE LA ADJUDICACION 6.3 DEL ACTA 159, y por eso la TAREA 1 la DIFIRIO en
vez de escribirla: la 6.3 manda a relectura conjunta, o sea que su bloque tiene
que traer DENTRO el veredicto medido. Un bloque escrito en la TAREA 1, antes de
leer, habria sido una adjudicacion sin medicion.

LA VARA ES LA 6.4 DEL ACTA 157 CON LA CORRECCION DE LA 6.3 DEL ACTA 158:

    SE PUEDEN NOMBRAR DOS LINEAS DISTINTAS, UNA EN CADA NODO, Y DECIR QUE
    PROCEDIMIENTO DEL OTRO NODO EXPANDE CADA UNA?

y ESO ES UN EXISTENCIAL: un par que colapsa descarta ESE PAR, no el nodo. Por
eso la razon de esta tarea recorre el espacio de pares de la direccion en
disputa y NOMBRA LOS TRES PARES MAS FUERTES QUE DESCARTA, uno a uno.

EL RESULTADO, ADELANTADO AQUI: `LD-OPC05-100` PASA DE C A D. EL AUDITOR TIENE
RAZON Y LA CAIDA DE CLASE ES MIA, del lote 2 de la vuelta 159. NO SE PUBLICA
COMO CONCESION: se publica con un argumento que ninguna de las dos plumas habia
usado, el del campo ENTREGABLE, que se puede volver a medir en el grafo.

Y SE DICE LO QUE ESTO DISPARA, PORQUE CALLARLO SERIA PEOR: con la `005`
confirmada en la vuelta 159, esta es LA SEGUNDA TANDA SEGUIDA CON CAIDA DE CLASE
CONFIRMADA, y la regla del credito (AUDITOR.md 4, "Dos tandas seguidas: PARADA")
se dispara. Se declara en el reporte como PARADA y NO SE EJECUTA NINGUNA ACCION
DE PARADA POR MI MANO: no se escribe `PARA_ALEXIS.md`, no se vacia
`PROMPT_SIGUIENTE.md` y no se pide el merge, que son cosa del auditor y del
fundador. El resto del encargo se ejecuta entero, empezando por la TAREA 2.b,
que es justamente el remedio que la 6.4 encarga por la bajada de credito.

LAS GUARDAS SON LAS DE LA 2.d Y VIVEN EN `vuelta159_motor_veredictos.py`, QUE ES
LA FUENTE UNICA Y NO SE CLONA: frontera con sha256 de `dataset/`, censo y
aristas antes y despues, `n` en 3.388, prefijo intacto en las 154 razones,
ningun par movido y ninguna clase a `A`.

USO:  python scripts/loop/vuelta160_tarea2a_relectura_conjunta.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta159_motor_veredictos as motor  # noqa: E402

MARCA = "RELECTURA CONJUNTA DE LA VUELTA 160"


def cabeza(vieja, nueva):
    if nueva != vieja:
        return ("  [CORRECCION DECLARADA, %s (2026-09-03), Y AQUI VIVE LA "
                "ADJUDICACION 6.3 DEL ACTA 159, ANADIDA SIN BORRAR NADA DE LO "
                "ANTERIOR: LA CLASE PASA DE %s A %s. " % (MARCA, vieja, nueva))
    return ("  [%s (2026-09-03), Y AQUI VIVE LA ADJUDICACION 6.3 DEL ACTA 159, "
            "ANADIDA SIN BORRAR NADA DE LO ANTERIOR: LA CLASE SE QUEDA EN %s. "
            % (MARCA, vieja))


def nota_md(vieja, nueva, motivo):
    if nueva != vieja:
        return ("CORRECCION DECLARADA (vuelta 160, RELECTURA CONJUNTA, "
                "adjudicacion 6.3 del acta 159): la clase pasa de ~~%s~~ a %s. "
                "%s." % (vieja, nueva, motivo[:260]))
    return ("RELECTURA CONJUNTA (vuelta 160, adjudicacion 6.3 del acta 159): la "
            "clase SE SOSTIENE en %s y su caso queda escrito en la razon del "
            "registro de citas." % vieja)


V = {
    "LD-OPC05-100": ("D",
        "LA CLASE PASA DE C A D Y CORRIGE MI PROPIA LECTURA DEL LOTE 2 DE LA "
        "VUELTA 159, QUE LA SOSTUVO EN C. EL AUDITOR TIENE RAZON. Verificado "
        "contra los dos nodos con el dossier de esta vuelta delante, y contra "
        "los tres casos de contraste que la misma vara juzgo (052 y 095 en C, "
        "122 en D), recomputados hoy en "
        "docs/loop/SALIDA_V160_T2A_CONTRASTE.txt. "
        "LA LINEA 2 SE SOSTIENE Y NO ESTA EN DISCUSION: el paso 5 de "
        "proceso_ideacion_modelo_negocio (reducir a entre tres y cinco ideas y "
        "prototiparlas usando el lienzo de modelo de negocio) lo expanden los "
        "doce pasos de lienzo_modelo_negocio, que son el procedimiento entero "
        "del instrumento que esa linea nombra. UNA DIRECCION LIMPIA. "
        "LA LINEA 1 NO PASA LA VARA, Y ESE ERA TODO EL DESACUERDO. Mi razon del "
        "lote 2 decia que el paso 9 del lienzo (pausar para investigar mas "
        "informacion donde haya vacios importantes) lo expande el paso 2 de "
        "ideacion (realizar una fase de inmersion: investigar clientes, "
        "tecnologias y modelos de negocio existentes). SE MIDE Y NO SE SOSTIENE, "
        "POR TRES COSAS QUE ESTAN EN LOS NODOS. "
        "PRIMERA, LA FORMA: el paso 2 de ideacion es LA MISMA ORDEN CON TRES "
        "COMPLEMENTOS. Dice investigar y despues dice que investigar (clientes, "
        "tecnologias, modelos de negocio existentes); no trae metodo, ni "
        "instrumento con autor, ni secuencia, ni entregable propio. Contrastado "
        "con lo que ESTA MISMA VARA acepto: en la 052 el paso 8 es LAS 6 "
        "PREGUNTAS DE CHOPRA Y MEINDL, un instrumento con autor y seis "
        "dimensiones enumeradas que produce una respuesta; en la 095 los cinco "
        "pasos de process tracing son un metodo secuenciado entero (recolectar "
        "datos crudos, construir el relato del dominio, aplicar conceptos "
        "dependientes, buscar patrones entre los dos relatos, documentar). Y "
        "contrastado con lo que ESTA MISMA VARA excluyo: en la 122 el paso 6 de "
        "6S (revisa e integra practicas seguras en cada etapa de tu trabajo) es "
        "orden mas complemento de alcance, y se declaro NOMBRAR SIN "
        "PROCEDIMENTAR. El paso 2 de ideacion es de la especie de la 122, no de "
        "la de la 052 ni de la 095. "
        "SEGUNDA, EL DISPARADOR Y EL MOMENTO, Y ESTO NO LO HABIA MEDIDO NADIE: "
        "el paso 9 del lienzo es UNA PAUSA DENTRO DE LA CONSTRUCCION DEL "
        "LIENZO, disparada por vacios YA IDENTIFICADOS (su propio paso 2 dice "
        "reunirse aceptando que habra vacios en la primera version) y acotada a "
        "esos vacios. La fase de inmersion de ideacion es su paso 2 de cinco y "
        "corre ANTES de que exista ningun lienzo lleno: no la dispara ningun "
        "vacio y no toma el vacio como insumo. Un procedimiento que no recibe "
        "el vacio no puede ser el como se llena ese vacio. "
        "TERCERA, Y ES LA DECISIVA PORQUE SE LEE DE UN CAMPO Y SE PUEDE VOLVER "
        "A MEDIR: EL ENTREGABLE DE ideacion ESTA ESCRITO EN TERMINOS DEL "
        "LIENZO. Dice literalmente 'Lista corta de 3 a 5 prototipos de modelo "
        "de negocio ESBOZADOS EN EL LIENZO DE MODELO DE NEGOCIO'. El entregable "
        "del lienzo, en cambio, no menciona la ideacion: dice 'Lienzo de Modelo "
        "de Negocio completo con los 9 bloques definidos y coherentes entre si'. "
        "ideacion CONSUME el lienzo como instrumento; el lienzo no consume la "
        "ideacion. Eso es la definicion de UNA SOLA DIRECCION, MADRE E HIJO, y "
        "el par continua. "
        "BAJO LA 6.3 DEL ACTA 158 SE RECORRIO EL ESPACIO ENTERO DE LA DIRECCION "
        "EN DISPUTA ANTES DE DECIRLO, Y LOS TRES PARES MAS FUERTES QUE SE "
        "DESCARTAN VAN NOMBRADOS. "
        "PAR DESCARTADO 1, el mas fuerte: el paso 2 del lienzo (reunirse con el "
        "equipo aceptando que habra vacios en la primera version) contra el "
        "paso 1 de ideacion (ensamblar un equipo diverso en antiguedad, "
        "experiencia, area funcional y conocimiento del cliente). SE DESCARTA "
        "porque ensamblar el equipo es un ACTO PREVIO, no el como se hace la "
        "reunion: el lienzo dice 'el equipo' como algo dado y no pregunta como "
        "componerlo. Precedencia no es expansion. "
        "PAR DESCARTADO 2: el paso 3 del lienzo (escribir cada bloque en notas "
        "post-it sobre el lienzo) contra el paso 3 de ideacion (expandir "
        "generando la mayor cantidad de ideas posible por cada bloque del "
        "lienzo, sin criticar todavia y priorizando cantidad sobre calidad). SE "
        "DESCARTA porque el paso 3 del lienzo es una instruccion de NOTACION "
        "(en que soporte se escribe) y el paso 3 de ideacion es GENERACION DE "
        "IDEAS cuya salida son modelos candidatos, no un lienzo lleno: sujetos "
        "distintos, y sujeto distinto es la definicion de D. "
        "PAR DESCARTADO 3: el paso 10 del lienzo (iterar y discutir en grupo "
        "hasta lograr coherencia entre los bloques) contra los pasos 4 y 5 de "
        "ideacion (definir criterios de seleccion y reducir a tres o cinco "
        "ideas). SE DESCARTA porque la convergencia de ideacion elige ENTRE "
        "MODELOS y la del lienzo busca COHERENCIA ENTRE BLOQUES DE UN MODELO: "
        "otra unidad de analisis. "
        "Y HAY UNA INCONSISTENCIA INTERNA QUE EL AUDITOR SENALO Y QUE VERIFICO "
        "CONTRA MI PROPIO TEXTO: en la LD-OPC05-004, de esta misma serie, "
        "escribi 'UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA'. "
        "Quitada la linea 1, en la 100 queda exactamente una sola direccion. La "
        "misma vara aplicada a las dos da D en las dos. "
        "ESTA ES CAIDA DE CLASE MIA, DE LA TANDA DE LA VUELTA 159, Y LA "
        "DECLARO: con la LD-OPC05-005 ya confirmada, son DOS TANDAS SEGUIDAS y "
        "la regla del credito se dispara. Dossier en "
        "docs/loop/SALIDA_V160_T2A_DOSSIER.txt"),
}


def main():
    return motor.aplicar(
        "VUELTA 160, TAREA 2.a: LD-OPC05-100, LA UNA EN DISPUTA, RELECTURA CONJUNTA",
        V, MARCA, cabeza, nota_md, ids_esperados=list(V))


if __name__ == "__main__":
    raise SystemExit(main())
