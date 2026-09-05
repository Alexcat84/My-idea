# -*- coding: utf-8 -*-
r"""vuelta179_tarea2_escribir_lecturas.py . LAS DIEZ LECTURAS DE `OP-L-03` SE
ESCRIBEN EN SU REGISTRO, CON SU CLASE Y SU RAZON.

TAREA 2 de la vuelta 179.

DONDE ESCRIBE, Y ES LA DISTINCION DEL PUNTO 7.8 DEL ACTA 178 QUE NO SE DIFUMINA.
Los diez pares SE MIDIERON y NINGUNO tiene puesto en la cola
(`docs/loop/SALIDA_V179_T2_LOS_DIEZ.txt`, bloque E), asi que NO SE INVENTA NINGUN
PUESTO: su clase y su razon van a `docs/plan/OP_L_03_LECTURAS.jsonl`, en el campo
`clases_de_los_pares_por_leer`, que es donde la 177 las puso y donde son
trazables. `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` NO SE TOCA, y este fichero lo
comprueba por `sha256` antes y despues.

DE DONDE SALE CADA CLASE, Y SON DOS COSAS QUE VAN JUNTAS:

  (1) LA VARA DEL BANCO, `9.6.1` y su rama contenido-manda (LA LINEA O EL
      PROCEDIMIENTO), leida sobre los `pasos_accionables` de los dos extremos.

  (2) LO QUE EL ARCHIVO YA DIJO POR UN TERCER NODO, que `banco 9.3` obliga a
      mirar antes de fijar una direccion de fusion sobre un par suelto: una
      direccion decidida sobre un par NO SOBREVIVE A SU FAMILIA. Lo mide
      `scripts/loop/vuelta179_tarea2_vecinos_del_archivo.py`
      (`docs/loop/SALIDA_V179_T2_VECINOS.txt`), y de los diez pares los DIEZ
      tienen al menos un tercero comun ya juzgado. Ninguna clase de aqui se
      decidio sin mirarlo.

LO QUE ESTE FICHERO NO HACE: no mueve ni un veredicto, no toca el marcador, no
escribe nodos y no cambia el estado de la ficha.

USO:
  python scripts/loop/vuelta179_tarea2_escribir_lecturas.py
  python scripts/loop/vuelta179_tarea2_escribir_lecturas.py --solo-mirar
"""
import argparse
import hashlib
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta166_tarea2_correccion_op_l_01 as T   # noqa: E402

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "OP_L_03_LECTURAS.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
LISTA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V179_T2_LOS_DIEZ.json")
FECHA = "2026-09-05"
VUELTA = 179

# LAS DIEZ LECTURAS. La clave es el par ORDENADO y unido por barra, igual que la
# 177 lo escribio. El valor es [clase, razon]. LA RAZON CITA SIEMPRE LOS DOS
# APOYOS: la vara sobre el contenido y el puesto del archivo que lo sostiene.
LECTURAS = {
 "colaboracion_cadena_suministro|diagnostico_efecto_latigo": ["A",
  "REPITE, Y ES LA MISMA FIGURA DEL PUESTO 730 CON EL GEMELO DEL HIJO. Los pasos "
  "1 y 2 de colaboracion_cadena_suministro son el acto entero de "
  "diagnostico_efecto_latigo: comparar los pedidos entrantes contra los "
  "salientes a lo largo de un periodo y graficar la divergencia entre la demanda "
  "del cliente final y las ordenes al proveedor. EL ARCHIVO YA LO DIJO POR UN "
  "TERCERO: el puesto 730 declara a efecto_bullwhip HIJO CON CASA PROPIA de esta "
  "misma madre por sus pasos 1 y 2, y el puesto 329 declara que "
  "diagnostico_efecto_latigo REPITE con efecto_bullwhip midiendo lo mismo de la "
  "misma manera. Si el hijo repite con la madre y este nodo repite con el hijo, "
  "este nodo repite con la madre. Lo que diagnostico_efecto_latigo anade por su "
  "lado, el beer game como ejercicio y la cuantificacion de costos, CABE EN LA "
  "MISMA CASA que el 329 ya midio como aditivo y no como oficio distinto."],
 "compartir_datos_cadena_suministro|diagnostico_efecto_latigo": ["D",
  "MEDIR EL LATIGO CONTRA COMPARTIR LOS DATOS QUE LO CURAN, Y ES LA MISMA "
  "FRONTERA DEL PUESTO 994 CON EL GEMELO. compartir_datos_cadena_suministro no "
  "mide nada: define que datos de demanda y desempeno se pueden compartir sin "
  "riesgo, monta el mecanismo electronico para compartirlos, avisa a los "
  "proveedores de las decisiones internas que mueven la demanda, y evalua el "
  "beneficio contra la exposicion. diagnostico_efecto_latigo no comparte nada: "
  "compara las ordenes de cada eslabon contra la demanda real, identifica la "
  "amplificacion, simula el beer game y cuantifica el costo. SON DOS OFICIOS Y "
  "EL GRAFO YA LOS CABLEA EN ORDEN: hay arista de compartir_datos a "
  "diagnostico, verificada resolviendo a nodo vivo. EL ARCHIVO YA LO DIJO POR UN "
  "TERCERO, Y ES UNA FRONTERA LIMPIA: el puesto 994 da D entre "
  "compartir_datos_cadena_suministro y efecto_bullwhip con exactamente este "
  "argumento, y el puesto 329 da A entre diagnostico_efecto_latigo y ese mismo "
  "efecto_bullwhip. Uno esta dentro de la medicion y el otro fuera."],
 "compra_por_precio_mas_bajo_como_error|relacion_largo_plazo_proveedor_unico": ["D",
  "EL ERROR CONTRA EL REMEDIO, Y EL ARCHIVO LO DICE POR DOS TERCEROS EN ESPEJO. "
  "compra_por_precio_mas_bajo_como_error es un criterio de decision en tres "
  "pasos: dejar de comprar por precio solo, calcular el costo total contando "
  "retrabajo, tiempo perdido y fallas, y mirar como funcionan juntos los "
  "materiales en el proceso y no cada ficha tecnica por separado. "
  "relacion_largo_plazo_proveedor_unico es un procedimiento de abastecimiento en "
  "cuatro: reducir proveedores hacia uno solo por articulo, formar equipos "
  "conjuntos con ingenieria y diseno, firmar contratos plurianuales con libros "
  "abiertos, y calificar por evidencia de mejora continua. Lo que cada uno anade "
  "al otro NO CABE EN UNA LINEA: es una secuencia con su propia logica, que es "
  "la vara de `banco 9.6.1` en su rama contenido-manda. EL ARCHIVO LO SOSTIENE "
  "POR DOS CAMINOS SIMETRICOS: el puesto 2424 da A entre este nodo y "
  "fin_precio_como_criterio_unico mientras el 3102 da D entre ese mismo tercero "
  "y relacion_largo_plazo_proveedor_unico; y al reves, el puesto 2421 da A entre "
  "relacion_largo_plazo_proveedor_unico y relaciones_largo_plazo_con_proveedores "
  "mientras el 2927 da D entre ese tercero y este nodo. CADA UNO TIENE SU PROPIA "
  "FAMILIA Y NO ES LA DEL OTRO."],
 "creacion_option_pool|employee_pool_esop": ["D",
  "LA NEGOCIACION DEL TAMANO CONTRA LA MECANICA DE LA RESERVA, Y ES LA FRONTERA "
  "QUE EL PUESTO 1193 YA TIENE ESCRITA CON ESAS PALABRAS. creacion_option_pool "
  "es NEGOCIACION y mira a la ronda: estimar cuantas contrataciones clave hacen "
  "falta antes de la siguiente, negociar el tamano con los inversores antes del "
  "cierre sabiendo que afecta la valoracion pre-money, y refrescar el pool en "
  "cada ronda posterior. employee_pool_esop es MECANICA y mira a la tabla de "
  "capital: negociar el tamano como porcentaje DESPUES de la inversion, definir "
  "si la reserva incluye las opciones ya entregadas o solo lo no emitido, "
  "calcular como esa dilucion afecta el precio por accion del fundador, y "
  "planear el reparto. EL ARCHIVO PONE A CADA UNO EN UN LADO DE ESA FRONTERA: el "
  "puesto 1112 da A entre creacion_option_pool y option_pool_negociacion, o sea "
  "que creacion_option_pool ES el lado NEGOCIACION; y el puesto 1193 da D entre "
  "employee_pool_esop y ese mismo option_pool_negociacion nombrando la frontera, "
  "'la mecanica de la reserva contra la negociacion de su tamano'. "
  "Y LA SENAL EN CONTRA SE DECLARA EN VEZ DE ESCONDERSE: los puestos 1436 y 1371 "
  "dan A entre pool_opciones_empleados y CADA UNO de los dos, lo que por cadena "
  "pediria A aqui. Se resuelve a favor de la frontera porque ESE TERCERO ES EL "
  "QUE ESTA A CABALLO: el 1371 dice que pool_opciones_empleados trae la "
  "verificacion de las opciones ya entregadas, que es MECANICA, y el 1436 dice "
  "que trae el presupuesto de opciones y su negociacion, que es NEGOCIACION. Un "
  "nodo que toca los dos lados no funde los dos lados entre si. VA MARCADO "
  "DISCUTIBLE."],
 "disenar_tests_pass_fail|diseno_experimentos_hipotesis": ["A",
  "REPITE, Y ES EL TERCER MIEMBRO DE UNA FAMILIA QUE EL PROPIO ARCHIVO YA "
  "DECLARO DE TRES. Los dos primeros pasos son el mismo en las mismas palabras: "
  "preguntarse que se quiere o se necesita aprender, y disenar la prueba mas "
  "simple posible que lo conteste. EL ARCHIVO LO DICE EXPRESAMENTE: el puesto "
  "511 da A entre disenar_tests_pass_fail y diseno_experimentos_pass_fail y "
  "cierra con la frase 'Con el puesto 467, la familia del diseno de experimentos "
  "llega a TRES nodos del nucleo', y el puesto 467 es precisamente A entre "
  "diseno_experimentos_hipotesis y ese mismo tercero. El tercer nodo de esa "
  "familia declarada es este par. Y LA OTRA FRONTERA NO LOS SEPARA, SINO QUE LOS "
  "PONE JUNTOS DEL MISMO LADO: los puestos 1346 y 636 dan D entre "
  "realizar_pruebas_pasa_no_pasa y CADA UNO de los dos, o sea que los dos estan "
  "en el lado DISENO y ninguno en el lado MECANICA DE EJECUCION. Lo que cada uno "
  "anade por su lado, el criterio numerico fijado de antemano en uno y la "
  "maqueta sin programar en el otro, es lo que el 467 ya midio como 'mismo "
  "experimento, uno mas instrumentado'."],
 "fase_diseno_prototipado_modelos|prototyping_possibilities": ["A",
  "LA MISMA ESCALERA DE PROTOTIPOS, Y EL ARCHIVO LA TIENE MEDIDA POR UN TERCERO "
  "CON LAS DOS PUNTAS EN A. El instrumento comun es entero: generar VARIAS "
  "direcciones alternativas y no una sola, hacerlas tangibles barato antes de "
  "comprometerse, subir la fidelidad solo en las mas prometedoras, y elegir "
  "despues de haber comparado. EL ARCHIVO YA LO DIJO POR prototipado_modelos_"
  "negocio: el puesto 641 da A contra fase_diseno_prototipado_modelos con el "
  "titulo 'DOS CASAS PARA LA MISMA FASE', y el puesto 1056 da A contra "
  "prototyping_possibilities con el titulo 'LA MISMA ESCALERA DE PROTOTIPOS' y "
  "enumerando ese instrumento comun paso por paso. Los dos extremos de este par "
  "repiten con el mismo tercero por el mismo motivo. LO QUE LOS DIFERENCIA ES EL "
  "LIENZO Y NO EL OFICIO: uno prototipa con el Business Model Canvas y el otro "
  "con bocetos de servilleta y Value Proposition Canvas, y esa eleccion de "
  "artefacto CABE EN UNA LINEA, que es la vara de `banco 9.6.1` en su rama "
  "contenido-manda."],
 "proceso_ideacion_modelo_negocio|prototyping_possibilities": ["D",
  "IDEAR CONTRA PROTOTIPAR, Y ES LA MISMA FIGURA DEL PUESTO 572 CON EL GEMELO "
  "DEL HIJO. proceso_ideacion_modelo_negocio es el acto de generar: ensamblar un "
  "equipo diverso, hacer una fase de inmersion investigando clientes y "
  "tecnologias, expandir generando la mayor cantidad de ideas por cada bloque "
  "del lienzo sin criticar, definir criterios de seleccion, y reducir a entre "
  "tres y cinco. Prototipar es su PASO 5, no su acto. EL ARCHIVO YA LO DIJO POR "
  "UN TERCERO, Y ES UNA FRONTERA LIMPIA: el puesto 572 da D entre "
  "proceso_ideacion_modelo_negocio y prototipado_modelos_negocio con el titulo "
  "'EL HIJO CON CASA PROPIA' y la razon 'prototipado_modelos_negocio desarrolla "
  "el paso 5 de proceso_ideacion_modelo_negocio'; y el puesto 1056 da A entre "
  "ese mismo tercero y prototyping_possibilities. Si el prototipado es el hijo "
  "con casa propia de la ideacion, y este nodo repite con ese hijo, entonces "
  "este nodo es el hijo y no la madre. LA VARA LO CONFIRMA SIN EL ARCHIVO: lo "
  "que prototyping_possibilities anade a lo que proceso_ideacion ya dice es una "
  "secuencia con su propia logica, bocetos, ad-libs, Value Proposition Canvas y "
  "MVP, y no una linea."],
 "analisis_trafico_competitivo|captura_conocimiento_mercado": ["A",
  "EL MISMO BARRIDO DEL TERRENO COMPETITIVO, Y EL ARCHIVO LO CIERRA POR UN "
  "TERCERO QUE ES EL GEMELO ORTOGRAFICO DE UNO DE LOS DOS. Los dos terminan en "
  "el MISMO PAR DE ARTEFACTOS y lo dicen con las mismas palabras: construir una "
  "grilla competitiva y un mapa de mercado. EL ARCHIVO YA LO DIJO DOS VECES: el "
  "puesto 941 da A entre captura_conocimiento_mercado y "
  "capturar_conocimiento_de_mercado con la razon 'EL MISMO BARRIDO DE MERCADO "
  "CON EL MISMO NOMBRE... los ids solo se diferencian en una preposicion'; y el "
  "puesto 508 da A entre analisis_trafico_competitivo y ese mismo "
  "capturar_conocimiento_de_mercado con la razon 'el mismo reconocimiento del "
  "terreno competitivo... y organizarlo'. Si b es el mismo nodo que t y a repite "
  "con t, a repite con b. Lo propio de analisis_trafico_competitivo, las "
  "herramientas de trafico web y los rankings de tiendas de aplicaciones, YA "
  "ESTA DENTRO del 508, que las nombra como parte de lo comun y no como lo "
  "propio."],
 "crowdfunding_legal_exemptions_jobs_act|cumplimiento_inversionistas_acreditados": ["A",
  "LAS MISMAS REGLAS DE VALORES SOBRE LA MISMA RONDA, Y LOS DOS REPITEN CON EL "
  "MISMO TERCERO. El nucleo comun esta entero en los dos: comprobar si quien "
  "quiere invertir califica como inversionista acreditado antes de venderle "
  "equity, elegir la excepcion de registro que permite o prohibe publicitar la "
  "ronda, y consultar con un abogado de valores antes de levantar. EL ARCHIVO YA "
  "LO DIJO POR equity_crowdfunding: el puesto 462 da A contra "
  "crowdfunding_legal_exemptions_jobs_act enumerando ese nucleo, y el puesto 916 "
  "da A contra cumplimiento_inversionistas_acreditados enumerando el mismo. Lo "
  "propio de cada uno CABE EN UNA LINEA, que es la vara de `banco 9.6.1` en su "
  "rama contenido-manda: uno anade elegir el portal autorizado si se usa el "
  "Titulo III, y el otro anade documentar la verificacion de cada inversionista."],
 "evaluacion_tecnologias_disruptivas|explotacion_tecnologias_disruptivas": ["A",
  "LA MISMA VIGILANCIA DE LA TECNOLOGIA QUE HOY RINDE MENOS, Y LOS DOS REPITEN "
  "CON EL MISMO TERCERO. Lo comun es el acto entero: detectar las tecnologias "
  "emergentes que hoy rinden menos pero traen algo distinto, estimar su "
  "probabilidad de mejora, y decidir si son amenaza o oportunidad y que hacer. "
  "EL ARCHIVO YA LO DIJO POR tecnologias_disruptivas_oportunidad: el puesto 505 "
  "da A contra evaluacion_tecnologias_disruptivas y el puesto 513 da A contra "
  "explotacion_tecnologias_disruptivas, y la razon del 513 dice de este ultimo "
  "que 'anade mirar tambien las industrias vecinas', o sea que lo trata como "
  "ADITIVO sobre el mismo acto y no como oficio distinto. Lo que "
  "explotacion_tecnologias_disruptivas trae de mas, el trabajo de campo con "
  "adoptantes tempranos y el analisis IOTA, es instrumentacion del mismo acto, "
  "que es como el 467 trato el caso paralelo en la familia del diseno de "
  "experimentos. VA MARCADO DISCUTIBLE, porque el IOTA es lo mas cerca que hay "
  "aqui de un procedimiento propio."],
}

# LA FORMA DE CADA ACTO, ESCRITA (banco 9.26 y cuarta linea de la verificacion de
# la ficha). Una por acto, no una por par.
FORMAS = {
 "colaboracion_cadena_suministro":
  "UNA MADRE CON CERO HERMANOS ENLAZADOS Y DOS HIJOS DE PASO, Y ES LA FIGURA QUE "
  "EL PUESTO 730 YA TIENE MEDIDA EN ESTE MISMO ACTO. colaboracion_cadena_"
  "suministro enumera cinco pasos: los dos primeros son medir y graficar el "
  "latigo, y los dos ultimos son acordar el intercambio de datos y montar la "
  "visibilidad compartida. Sus dos hijos de paso tienen casa propia, "
  "diagnostico_efecto_latigo por los pasos 1 y 2 y compartir_datos_cadena_"
  "suministro por los pasos 4 y 5, y LA MADRE NO ENLAZA A NINGUNO: su unica "
  "arista de salida va a optimizacion_tecnologia_cadena_suministro. Cero "
  "enlazados es el borde del mitad-o-menos de `banco 9.6.1`, asi que la silueta "
  "no dice nada y manda el contenido. Y EL CONTENIDO PARTE EL ACTO EN DOS: el "
  "hijo de la medicion REPITE con la madre y el hijo del compartir NO, que es "
  "exactamente lo que los puestos 730 y 994 ya dijeron sobre efecto_bullwhip.",
 "compra_por_precio_mas_bajo_como_error":
  "DOS FAMILIAS DE DOS QUE SE TOCAN EN UNA LINEA Y NO SE FUNDEN. El acto reune "
  "el error, compra_por_precio_mas_bajo_como_error, y el remedio, "
  "relacion_largo_plazo_proveedor_unico, que son los dos lados del Punto 4 de "
  "Deming. Cada uno tiene YA su propio gemelo declarado en el archivo y NO ES EL "
  "OTRO: fin_precio_como_criterio_unico es el gemelo del error (puesto 2424, A) "
  "y relaciones_largo_plazo_con_proveedores es el gemelo del remedio (puesto "
  "2421, A). Y LOS DOS CRUCES SALIERON D, los puestos 3102 y 2927. La figura es "
  "un par de familias vecinas, cableadas entre si por la arista que el grafo ya "
  "trae del error al remedio, y no un racimo.",
 "creacion_option_pool":
  "UNA FAMILIA DE CUATRO PARTIDA EN DOS OFICIOS, CON UN NODO A CABALLO. Los "
  "cuatro hablan de la reserva de opciones: creacion_option_pool, "
  "employee_pool_esop, option_pool_negociacion y pool_opciones_empleados. El "
  "archivo ya partio el acto en dos lados con el puesto 1193, 'la mecanica de la "
  "reserva contra la negociacion de su tamano'. creacion_option_pool esta del "
  "lado NEGOCIACION (puesto 1112, A) y employee_pool_esop del lado MECANICA. LO "
  "QUE ESTA LECTURA ANADE Y NO ESTABA ESCRITO: pool_opciones_empleados esta A "
  "CABALLO de los dos lados, porque el puesto 1371 le atribuye la mecanica y el "
  "1436 le atribuye la negociacion. Por eso la cadena de REPITE que pasa por el "
  "NO funde los dos lados, y este acto es el unico de los ocho en que el archivo "
  "se contradice consigo mismo por dos terceros distintos.",
 "disenar_tests_pass_fail":
  "UNA FAMILIA DE TRES QUE EL ARCHIVO YA DECLARO DE TRES, Y UNA FRONTERA QUE LOS "
  "DEJA A LOS TRES DEL MISMO LADO. La familia del diseno de experimentos son "
  "disenar_tests_pass_fail, diseno_experimentos_hipotesis y "
  "diseno_experimentos_pass_fail, y no lo declaro yo: lo declara la razon del "
  "puesto 511 con estas palabras, 'Con el puesto 467, la familia del diseno de "
  "experimentos llega a TRES nodos del nucleo'. Este acto cierra el triangulo "
  "que faltaba, el par entre los dos primeros. Y LA FRONTERA DEL ACTO ES OTRA "
  "COSA Y NO LOS PARTE: realizar_pruebas_pasa_no_pasa es MECANICA DE EJECUCION y "
  "sale D contra los dos, en los puestos 1346 y 636. Una familia de tres con una "
  "frontera comun enfrente.",
 "fase_diseno_prototipado_modelos":
  "UN ACTO PARTIDO EN DOS ALTURAS, Y LA MISMA PIEZA ES HIJA ARRIBA Y GEMELA "
  "ABAJO. En este acto viven proceso_ideacion_modelo_negocio, "
  "fase_diseno_prototipado_modelos y prototyping_possibilities, y el que los "
  "ordena es un cuarto que ya estaba juzgado, prototipado_modelos_negocio. LA "
  "ALTURA DE ARRIBA es idear: proceso_ideacion_modelo_negocio, cuyo paso 5 es "
  "prototipar, y por eso el puesto 572 lo separa de su hijo con casa propia. LA "
  "ALTURA DE ABAJO es prototipar: fase_diseno_prototipado_modelos y "
  "prototyping_possibilities, que repiten los dos con esa misma pieza en los "
  "puestos 641 y 1056. La figura no es un racimo de tres iguales: son DOS de "
  "abajo que se funden y UNO de arriba que no, y el archivo lo tenia ya escrito "
  "sin que nadie hubiera leido este acto entero.",
 "analisis_trafico_competitivo":
  "UN RACIMO DE TRES CON UN GEMELO ORTOGRAFICO DENTRO, Y ES LA FIGURA MAS BARATA "
  "DE LAS OCHO. captura_conocimiento_mercado y capturar_conocimiento_de_mercado "
  "son EL MISMO NODO ESCRITO DOS VECES, y no lo digo yo: lo dice la razon del "
  "puesto 941, 'los ids solo se diferencian en una preposicion'. "
  "analisis_trafico_competitivo repite con el segundo por el puesto 508, luego "
  "repite con el primero. LOS TRES SON UNO, y el acto entero se cierra con una "
  "sola lectura nueva.",
 "crowdfunding_legal_exemptions_jobs_act":
  "UN RACIMO DE TRES SOBRE LA MISMA REGLA DE VALORES, CERRADO POR EL TERCERO. "
  "crowdfunding_legal_exemptions_jobs_act, cumplimiento_inversionistas_"
  "acreditados y equity_crowdfunding mandan el mismo nucleo sobre la misma "
  "ronda: verificar la acreditacion antes de vender equity, elegir la excepcion "
  "que decide si se puede publicitar, y consultar con un abogado de valores. Los "
  "puestos 462 y 916 ya pusieron a los dos primeros en A con el tercero; este "
  "acto cierra el triangulo. Lo propio de cada uno es una linea, no un "
  "procedimiento.",
 "evaluacion_tecnologias_disruptivas":
  "UN RACIMO DE TRES CON EL PAR GEMELO POR NOMBRE DENTRO. evaluacion_ y "
  "explotacion_tecnologias_disruptivas se llaman casi igual y son el verbo "
  "antes y el verbo despues del mismo acto, y el tercero, "
  "tecnologias_disruptivas_oportunidad, ya salio A contra los dos en los puestos "
  "505 y 513. LA FIGURA TIENE UNA COSA QUE MERECE QUEDAR ESCRITA AUNQUE NO "
  "CAMBIE LA CLASE: entre evaluacion_ y explotacion_ NO HAY ARISTA, y el paso 4 "
  "de evaluacion_ es literalmente la pregunta que explotacion_ contesta, "
  "'y entonces que hago'. Es una arista que falta entre dos nodos que ademas "
  "repiten. NO SE TOCA NADA: la campana esta en modo de cierre y esto se anota, "
  "no se arregla.",
}


def sha(ruta):
    return hashlib.sha256(io.open(ruta, "rb").read().replace(chr(13).encode(), b"")).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-mirar", dest="solo_mirar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    p = print

    p("=" * 78)
    p("LAS DIEZ LECTURAS DE OP-L-03, ESCRITAS EN SU REGISTRO (179, TAREA 2)")
    p("=" * 78)
    p("")

    sha_antes = sha(VEREDICTOS)
    p("A) EL ARCHIVO DE VEREDICTOS, SELLADO ANTES DE TOCAR NADA")
    p("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
    p("   sha256 ANTES: %s" % sha_antes)
    p("   CIFRA bytes en disco: %d" % os.path.getsize(VEREDICTOS))
    p("")

    pares = json.load(io.open(LISTA, encoding="utf-8"))
    p("B) LAS DIEZ LECTURAS SE COTEJAN CONTRA LA LISTA DEL INSTRUMENTO")
    p("   (ni una clase se escribe para un par que el instrumento no dio)")
    claves_instrumento = set("|".join(sorted((f["a"], f["b"]))) for f in pares)
    claves_mias = set(LECTURAS)
    sobran = sorted(claves_mias - claves_instrumento)
    faltan = sorted(claves_instrumento - claves_mias)
    p("   CIFRA pares que el instrumento da: %d" % len(claves_instrumento))
    p("   CIFRA lecturas escritas aqui: %d" % len(claves_mias))
    p("   CIFRA lecturas que NO estan en la lista del instrumento: %d" % len(sobran))
    for k in sobran:
        p("      SOBRA: %s" % k)
    p("   CIFRA pares del instrumento SIN lectura: %d" % len(faltan))
    for k in faltan:
        p("      FALTA: %s" % k)
    if sobran or faltan:
        p("")
        p("ROJO: la lista de lecturas y la del instrumento no calzan. No se escribe nada.")
        return 1
    p("")

    p("C) EL REPARTO DE CLASES, CONTADO DE LAS LECTURAS")
    reparto = {}
    for k, (clase, _r) in LECTURAS.items():
        reparto[clase] = reparto.get(clase, 0) + 1
    p("| clase | pares |")
    p("|---|---:|")
    for c in sorted(reparto):
        p("| %s | **%d** |" % (c, reparto[c]))
    p("| **total** | **%d** |" % sum(reparto.values()))
    p("   LA RESTA: %s = %d, y los pares son %d. CALZA: %s"
      % (" mas ".join(str(reparto[c]) for c in sorted(reparto)),
         sum(reparto.values()), len(LECTURAS),
         "SI" if sum(reparto.values()) == len(LECTURAS) else "NO"))
    p("")

    p("D) LAS FILAS QUE SE ESCRIBEN, UNA POR ACTO")
    por_acto = {}
    for f in pares:
        por_acto.setdefault(f["acto"], []).append(f)
    sin_forma = [n for n in por_acto if n not in FORMAS]
    if sin_forma:
        p("   ROJO: hay actos sin forma escrita: %s" % ", ".join(sin_forma))
        return 1
    mapa, _n = T.mapa_de_alias()
    grafo = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    filas = []
    for nombre in sorted(por_acto):
        de_este = por_acto[nombre]
        clases = {}
        for f in de_este:
            k = "|".join(sorted((f["a"], f["b"])))
            clases[k] = LECTURAS[k]
        rep = {}
        for _k, (c, _r) in clases.items():
            rep[c] = rep.get(c, 0) + 1
        fila = {
            "id_op": "OP-L-03", "vuelta": VUELTA, "fecha": FECHA, "acto": nombre,
            "leido": True,
            "miembros": sorted({n for f in de_este for n in (f["a"], f["b"])}),
            "cifra_pares_reales_del_acto": len(de_este),
            "cifra_pares_leidos": len(clases),
            "cifra_pares_sin_lectura": len(de_este) - len(clases),
            "clases_de_los_pares_por_leer": clases,
            "reparto_de_clases": rep,
            "ninguno_tiene_puesto_en_la_cola": True,
            "donde_va_el_veredicto":
                "docs/plan/OP_L_03_LECTURAS.jsonl, campo clases_de_los_pares_por_leer. "
                "Ninguno de estos pares tiene puesto en docs/INTRA_DOMINIO_VEREDICTOS.jsonl "
                "y NO SE INVENTA NINGUNO (punto 7.8 del acta del auditor de la vuelta 178).",
            "veredictos_movidos": 0,
            "no_mueve_veredictos":
                "NINGUN VEREDICTO SE MUEVE Y NINGUNO SE ANADE. El marcador del archivo "
                "queda igual y se comprueba por sha256 antes y despues en "
                "docs/loop/SALIDA_V179_T2_ESCRIBIR.txt.",
            "forma": FORMAS[nombre],
            "apoyo_del_archivo_por_un_tercero":
                "Medido por scripts/loop/vuelta179_tarea2_vecinos_del_archivo.py "
                "(docs/loop/SALIDA_V179_T2_VECINOS.txt), que es lo que banco 9.3 obliga "
                "a mirar antes de fijar una direccion de fusion sobre un par suelto.",
            "cobertura": {
                "pares_leidos_en_esta_vuelta": len(clases),
                "pares_reales_del_acto": len(de_este),
                "pares_del_acto_sin_cubrir": len(de_este) - len(clases),
                "nota": "banco 9.26: la forma se re-mide CON SU COBERTURA AL LADO.",
            },
        }
        filas.append(fila)
        p("")
        p("   acto `%s`" % nombre)
        p("      miembros: %s" % ", ".join(fila["miembros"]))
        p("      pares reales del acto: %d | leidos aqui: %d | sin cubrir: %d"
          % (len(de_este), len(clases), len(de_este) - len(clases)))
        for k in sorted(clases):
            p("      %-4s %s" % (clases[k][0], k))
        p("      reparto: %s" % json.dumps(rep, ensure_ascii=False))
    p("")
    p("   CIFRA filas que se escriben: %d" % len(filas))
    p("   CIFRA pares cubiertos por esas filas: %d"
      % sum(f["cifra_pares_leidos"] for f in filas))
    p("")

    if a.solo_mirar:
        p("   --solo-mirar: NO se escribe nada.")
        return 0

    antes_reg = os.path.getsize(REGISTRO)
    n_antes = len([l for l in io.open(REGISTRO, encoding="utf-8") if l.strip()])
    with io.open(REGISTRO, "a", encoding="utf-8", newline=NL) as fh:
        for f in filas:
            fh.write(json.dumps(f, ensure_ascii=False) + NL)
    n_despues = len([l for l in io.open(REGISTRO, encoding="utf-8") if l.strip()])
    p("E) EL REGISTRO DE OP-L-03, ESCRITO POR ANEXION Y SIN PISAR NADA")
    p("   docs/plan/OP_L_03_LECTURAS.jsonl")
    p("   CIFRA filas ANTES: %d | DESPUES: %d | anadidas: %d"
      % (n_antes, n_despues, n_despues - n_antes))
    p("   CIFRA bytes ANTES: %d | DESPUES: %d" % (antes_reg, os.path.getsize(REGISTRO)))
    p("   las filas de la 177 siguen enteras: %s"
      % ("SI" if n_despues - n_antes == len(filas) else "NO"))
    p("")

    sha_despues = sha(VEREDICTOS)
    p("F) CERO VEREDICTOS MOVIDOS, COMPROBADO Y NO PROMETIDO")
    p("   sha256 ANTES:   %s" % sha_antes)
    p("   sha256 DESPUES: %s" % sha_despues)
    p("   IDENTICOS: %s" % ("SI" if sha_antes == sha_despues else "NO"))
    if sha_antes != sha_despues:
        p("ROJO: el archivo de veredictos se movio.")
        return 1
    p("")

    p("G) EL MARCADOR, RECOMPUTADO DEL ARCHIVO (banco 9.10)")
    cuenta = {}
    for linea in io.open(VEREDICTOS, encoding="utf-8"):
        if linea.strip():
            c = json.loads(linea).get("clase")
            cuenta[c] = cuenta.get(c, 0) + 1
    p("| clase | puestos |")
    p("|---|---:|")
    for c in sorted(cuenta):
        p("| %s | **%d** |" % (c, cuenta[c]))
    p("| **total** | **%d** |" % sum(cuenta.values()))
    p("   EL MARCADOR NO SE TOCA porque ninguno de los diez tiene puesto, y se")
    p("   recomputa igualmente para poder decir que no se movio.")
    p("")
    p("VERDE: las %d lecturas quedan escritas en %d filas de acto, cero veredictos"
      % (len(LECTURAS), len(filas)))
    p("movidos y cero puestos inventados.")
    p("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
