# -*- coding: utf-8 -*-
"""vuelta157_tarea2_lote1_veredictos.py . TAREA 2 DE LA VUELTA 157, EL LOTE 1.

APLICA LOS 66 VEREDICTOS DEL LOTE 1, LEIDOS UNO A UNO CONTRA LOS NODOS con el
dossier `docs/loop/SALIDA_V157_T2A_DOSSIER.txt`, bajo la PREGUNTA ESTRECHA Y
BINARIA de la adjudicacion 6.4 del acta 157:

    SE PUEDEN NOMBRAR DOS LINEAS DISTINTAS, UNA EN CADA NODO, Y DECIR QUE
    PROCEDIMIENTO DEL OTRO NODO EXPANDE CADA UNA?

LA VARA, DECLARADA CON SUS LIMITES ANTES DE APLICARLA, porque de ella cuelgan
los 66 veredictos:
  (a) UNA DIRECCION CUENTA cuando la LINEA del nodo X es una ACCION y el nodo Y
      es el COMO SE HACE esa accion. Una linea que solo MENCIONA al otro nodo
      como contexto, como precondicion o como diagnostico NO cuenta: mencionar
      no es expandir.
  (b) HACEN FALTA LAS DOS DIRECCIONES, sobre DOS LINEAS DISTINTAS. Con una sola
      direccion el par es madre e hijo y CONTINUA, que es el tercer caso del
      9.22, y la clase es D.
  (c) SI LAS DOS DIRECCIONES APUNTAN A LA MISMA LINEA, NO ES ESTA FIGURA. Es
      cita literal del 9.22 y es la comprobacion que mas casos separa en este
      lote.
  (d) SI LA RAZON DESCRIBE QUE CADA NODO EXPANDE LO SUYO, es el PUESTO 2091 del
      banco y la clase es D.
  (e) SER SANO NO PROTEGE. La 6.3 del acta 155 sostuvo `LD-OPC05-046` en C por
      el 9.6.3, o sea POR SER SANO; bajo la 6.4 sano SIN FIGURA es D, y esa
      parte de aquella adjudicacion queda revocada.
  (f) LA QUE SALGA A NO SE VOLTEA. Se marca como discutible, se publica su caso
      y NO se ejecuta ninguna fusion. NINGUNA SALIO A en este lote.

LAS GUARDAS, LAS MISMAS DE LA 156 Y NO SE AFLOJAN (encargo 2.d):
  - CADA CAMBIO DE CLASE CON CORRECCION DECLARADA y el texto viejo entero como
    PREFIJO, comprobado por assert sobre las 154 entradas y no solo sobre las
    tocadas.
  - `n` NO SE MUEVE: los veredictos del cribado se cuentan antes y despues y
    tienen que seguir en 3.388.
  - ASSERT DE FRONTERA: sha256 de todo `dataset/` y conteo de censo y aristas
    antes y despues. EL REGISTRO CAMBIA, EL GRAFO NO.
  - Gate 0 se corre al terminar el lote (fuera de este script, con el ciclo
    entero y en su orden).

LAS DOS SEDES SE ESCRIBEN JUNTAS: el registro (`clase` y `razon`) y la fila del
`.md`, que desde la TAREA 4 de esta vuelta ya acepta la celda TACHADA, asi que
la C vieja queda A LA VISTA en vez de taparse.

ES IDEMPOTENTE por marca literal.

USO:  python scripts/loop/vuelta157_tarea2_lote1_veredictos.py

--- ADJUDICACION 6.3 DEL ACTA 158 (3 sep 2026): LA PREGUNTA BINARIA DE LA 6.4 ES
UN EXISTENCIAL. SE HACE SOBRE TODOS LOS PARES DE LINEAS CANDIDATOS, NO SOBRE EL
PRIMERO QUE SE ENCUENTRE ---

CORRECCION DECLARADA POR ADICION, y NO ES DOCTRINA NUEVA: es la letra de la 6.4
del acta 157 leida entera. La 6.4 pregunta si SE PUEDEN nombrar dos lineas
distintas, y eso es un existencial: basta con que EXISTA UN PAR que cumpla.

LA CONSECUENCIA, QUE ES LO QUE AL LOTE 1 LE FALTO: hallar un par de lineas que
colapsa en la misma linea prueba que ESE PAR no es la figura, NO que no la haya.
El colapso del 9.22 descarta un par, no un nodo.

LA REGLA DE ESCRITURA QUE SE ADJUDICA, Y ES OBLIGATORIA DESDE LA PRIMERA LECTURA
DEL LOTE 2: cuando el colapso del 9.22 sea el motivo del descarte, la razon
tiene que decir TAMBIEN que NINGUN otro par de lineas sostiene la figura, y
NOMBRAR el par mas fuerte que se descarto.

EL CASO QUE LA ORIGINA, PARA QUE NO SE LEA COMO UNA REGLA SIN CUERPO
(`LD-OPC05-005`, acta 158 seccion 3.1): la razon del lote 1 descarto la figura
porque el paso 1 de `aim_of_leadership` y el paso 13 de
`causas_comunes_vs_especiales` son la misma linea, y para ESE par tenia razon.
Pero habia otro par disponible: el paso 2 de aim (investigar las causas de raiz
DEL SISTEMA) contra el paso 13 de causas, cada uno expandido por procedimientos
del otro nodo. Un existencial no se refuta con un caso.

--- ADJUDICACION 6.6 DEL ACTA 158 (3 sep 2026): EL CAMPO `cita` SE UNIFICA EN
UNA SOLA FORMA, Y GANA LA QUE NO TAPA ---

CORRECCION DECLARADA POR ADICION, y toca el campo `cita` del registro
`docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl`. Nada de lo escrito arriba se borra.

EL HECHO, MEDIDO POR EL AUDITOR COMPARANDO EL REGISTRO DE `abb2fe4e` CONTRA HEAD
(acta 158, seccion 5.1): en la vuelta 157 cambiaron 62 campos `cita`, y
cambiaron POR SOBREESCRITURA (`'LD-OPC05-001, clase C'` paso a
`'LD-OPC05-001, clase D'`, sin dejar el texto viejo). Pero las TRES que la
vuelta 156 reclasifico dicen otra cosa EN EL MISMO FICHERO
(`'LD-OPC05-002, clase C  [RECLASIFICADA A D EN LA VUELTA 156: ver la razon]'`).
DOS FORMAS PARA EL MISMO HECHO, EN EL MISMO FICHERO, EN DOS VUELTAS SEGUIDAS. Y
ademas esas tres hoy leen literalmente "clase C" en una fila cuya clase es D.

LO QUE SE ADJUDICA, POR EXTENSION DE LA 6.8 DEL ACTA 157 (la costumbre de la
casa, no tapar lo que se corrige) Y DE LA LEY DE UNA SOLA FUENTE: UNA SOLA FORMA
para las 65 filas corregidas, la que lleva la clase VIGENTE Y el rastro:

    clase D [ANTES C, RECLASIFICADA EN LA VUELTA N: ver la razon]

Con eso las 62 recuperan el rastro que la sobreescritura les quito y las 3 de la
vuelta 156 dejan de leer "clase C" en una fila que es D. Se hace POR ADICION,
con correccion declarada, y con el assert de que NINGUNA clase se mueve al
hacerlo y de que el conteo de pares del registro sale identico antes y despues.
Se ejecuta en la TAREA 4 de la vuelta 159.

NINGUNA CIFRA PUBLICADA ERA FALSA POR ESTO y el acta lo dice: la razon declara
la correccion en las 62 y ningun reporte afirmo nada sobre las citas. Lo que se
corrige es que la del 156 tapa menos y la del 157 tapa mas.

--- ADJUDICACION 6.12 DEL ACTA 158 (3 sep 2026): EL LOTE 2 VA, CON LA 6.3 PUESTA
DESDE LA PRIMERA LECTURA ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

EL LOTE 2 SON 53, de `LD-OPC05-068` a `LD-OPC05-121`, y NINGUNA trae puntero de
paso: el saco pequeno se agoto entero en el lote 1. LA NOMINA NO SE TECLEA: la
recomputa su instrumento, como se hizo con la del lote 1, y si no da 53 se para
y se dice ANTES de leer nada.

EL CRITERIO ES EL MISMO DE LA 6.4 DEL ACTA 157, con la unica correccion de la
6.3 del acta 158, que es lo que el lote 1 enseno: la pregunta es un existencial,
asi que cuando el colapso del 9.22 sea el motivo del descarte, la razon tiene
que decir TAMBIEN que ningun otro par de lineas sostiene la figura, y NOMBRAR el
par mas fuerte que se descarto.

LAS GUARDAS SON LAS MISMAS Y NO SE AFLOJAN: correccion declarada con el texto
viejo entero como prefijo, `n` no se mueve y sigue en 3.388, assert de frontera
con sha256 de `dataset/` y conteo de censo y aristas antes y despues (EL
REGISTRO CAMBIA, EL GRAFO NO), Gate 0 al terminar, y LA QUE SALGA A NO SE
VOLTEA.
"""
import hashlib
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
LD_MD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VERED = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
DATASET = os.path.join(RAIZ, "dataset")
NOMINA = os.path.join(RAIZ, "docs", "loop", "NOMINA_V157_LOTE1.json")

MARCA = "LOTE 1 DE LA VUELTA 157"

# ---------------------------------------------------------------------------
# LOS 66 VEREDICTOS. clase nueva y el motivo, que es lo que la razon va a decir.
# Los que sostienen C NOMBRAN SUS DOS LINEAS, que es lo que la 6.4 exige.
# ---------------------------------------------------------------------------
V = {
 "LD-OPC05-001": ("D", "su propia razon dice que cada uno expande un procedimiento que el otro no contiene, y eso es el PUESTO 2091 del banco. Contra los nodos: ninguna linea de accion_correctiva_sistematica la ejecuta cero_defectos, ni al reves"),
 "LD-OPC05-003": ("D", "PROCEDIMIENTO EN UN SOLO SENTIDO. El paso 1 de cronograma_proyecto (recopilar las estimaciones de duracion) si lo expande activity_duration_estimates, pero activity_duration_estimates no trae una sola linea que el cronograma expanda: madre e hijo, el par CONTINUA, tercer caso del 9.22"),
 "LD-OPC05-004": ("D", "UNA SOLA DIRECCION. El paso 4 de reempaquetado_producto (actualizar el lienzo) si lo expande el tune-up; el tune-up no trae linea que reempaquetado ejecute. Sin segunda linea no hay figura"),
 "LD-OPC05-005": ("D", "LAS DOS DIRECCIONES APUNTAN A LA MISMA LINEA (quien cae fuera de lo esperado: paso 1 de aim_of_leadership y paso 13 de causas_comunes_vs_especiales), y el 9.22 lo excluye con todas sus letras"),
 "LD-OPC05-006": ("D", "sujetos distintos, la TECNOLOGIA contra la ORGANIZACION, y ninguna linea de uno la ejecuta el otro. Sanos y distintos"),
 "LD-OPC05-007": ("D", "su propia razon dice distinto sujeto y distinta decision, que es la definicion literal de D. Contra los nodos: el POR QUE emprender contra el CUANDO, sin linea expandida en ningun sentido"),
 "LD-OPC05-008": ("D", "el paso 5 de motivaciones nombra el dilema y el dilema lo expande, pero LAS DOS DIRECCIONES APUNTAN A LA MISMA LINEA (riqueza contra control). Y la razon escrita describe que cada nodo expande lo suyo: PUESTO 2091"),
 "LD-OPC05-009": ("D", "el metodo de interpretacion contra el ritmo del proceso; ninguna linea de uno la ejecuta el otro"),
 "LD-OPC05-010": ("D", "dos clausulas distintas del mismo term sheet, cada una expandiendo lo suyo: PUESTO 2091. El waiver del paso 3 de antidilucion no es el pay-to-play"),
 "LD-OPC05-011": ("D", "dos clausulas distintas del mismo term sheet; ninguna linea de una la ejecuta la otra"),
 "LD-OPC05-012": ("D", "LAS DOS DIRECCIONES APUNTAN A LA MISMA LINEA (aprobar un Go sin recursos). Su propia razon lo dice: uno instala la practica y el otro la audita, que es cada uno lo suyo"),
 "LD-OPC05-013": ("D", "medir contra escribir, como dice su propia razon; ninguna linea de uno la ejecuta el otro"),
 "LD-OPC05-014": ("D", "UNA DIRECCION A LO SUMO, y ni siquiera nombrada en un paso: ningun paso del consejo de calidad encarga la auditoria de negocio por su nombre. Sin dos lineas, no hay figura"),
 "LD-OPC05-015": ("D", "la razon de compra contra la entrada a un mercado nuevo; cada uno expande lo suyo"),
 "LD-OPC05-016": ("D", "la diana de traccion contra el camino critico; ninguna linea de uno la ejecuta el otro"),
 "LD-OPC05-017": ("D", "UNA SOLA DIRECCION, y es la de ida. El paso 9 de pivote_estrategico (documenta cada cambio como una nueva version del lienzo) si lo expanden los ocho pasos del scorecard; pero el paso 2 del scorecard nombra los pivotes como REFERENTE y no como accion a ejecutar, y mencionar no es expandir. Sin segunda linea, madre e hijo y el par continua"),
 "LD-OPC05-018": ("D", "una direccion a lo sumo, y ademas el paso 5 del mapeo y el paso 4 de los escenarios son la misma linea (formular preguntas por bloque del Canvas)"),
 "LD-OPC05-019": ("D", "su propia razon dice que uno alimenta al otro con una cifra, y eso es UNA SOLA DIRECCION: el ROI del franquiciado no es una linea que la decision expanda de vuelta"),
 "LD-OPC05-020": ("D", "dos herramientas distintas de riesgo, la calibracion del juicio contra el analisis de sensibilidad; cada una expande lo suyo"),
 "LD-OPC05-021": ("D", "la brecha diseno contra produccion frente al COPQ y sus cuatro categorias: materias distintas, sin linea expandida en ningun sentido"),
 "LD-OPC05-022": ("D", "genero contra especie: el bloque de Canales del Canvas contra UN canal concreto. Ninguno nombra al otro en una linea que el otro ejecute"),
 "LD-OPC05-023": ("D", "armar el cap table contra convertir notas por tres metodos; cada uno expande lo suyo"),
 "LD-OPC05-024": ("D", "UNA DIRECCION (el paso 4 de mejora_continua nombra el control estadistico y causas_comunes lo expande); mejora_continua no trae linea que causas_comunes ejecute"),
 "LD-OPC05-025": ("D", "LAS DOS DIRECCIONES APUNTAN A LA MISMA LINEA (flexibilidad y escalado segun el riesgo del proyecto: paso 5 del checklist y paso 2 de los mitos)"),
 "LD-OPC05-026": ("D", "un instrumento de medida (el cuestionario de 15 afirmaciones) contra una estrategia; sin dos lineas distintas expandidas en los dos sentidos"),
 "LD-OPC05-027": ("C", "LA C SE SOSTIENE Y AQUI VAN SUS DOS LINEAS, que es lo que la 6.4 exige. LINEA 1, en metodologia_spin_selling, paso 1: diagnosticar si tu venta es pequena o grande; la expanden los pasos 1 a 3 de cierre_segun_complejidad_venta, que clasifican por valor, sofisticacion, relacion posventa, ciclo, monto y visibilidad, y ramifican. LINEA 2, en cierre_segun_complejidad_venta, paso 3: minimizar el uso de tecnicas de cierre y enfocar el esfuerzo en las etapas de indagacion (SPIN); la expanden los pasos 2 y 3 de metodologia_spin_selling. DOS LINEAS DISTINTAS Y NINGUNO ES LA MADRE"),
 "LD-OPC05-028": ("D", "UNA SOLA DIRECCION. El paso 3 de cinco_porques_master nombra una sesion de Cinco Porques y five_whys_inversion_proporcional la expande entera; five_whys no trae linea sobre designar al maestro. Madre e hijo, el par CONTINUA"),
 "LD-OPC05-029": ("D", "dos clausulas distintas del LOI, el no-shop y las condiciones de cierre; cada una expande lo suyo"),
 "LD-OPC05-030": ("D", "UNA SOLA DIRECCION. El paso 7 de community_building nombra los eventos offline y eventos_offline los expande; pero el paso 1 de eventos (piensa si buscan comunidad) es un DIAGNOSTICO, no una accion que community_building ejecute, y mencionar no es expandir"),
 "LD-OPC05-031": ("D", "SU PROPIA RAZON SE DELATA: dice que el paso 1 de compatibilidad y el paso 2 del dilema son CASI LA MISMA LINEA y que se sostiene PORQUE EL SUJETO ES DISTINTO. Sujeto distinto es la definicion de D, no de C, y las dos direcciones apuntan a la misma linea, que el 9.22 excluye"),
 "LD-OPC05-032": ("D", "pedir un compromiso de fecha contra la secuencia SPIN de preguntas; materias distintas"),
 "LD-OPC05-033": ("D", "una actitud (la concepcion hormica) contra un procedimiento de cuatro etapas; ninguna linea expandida en los dos sentidos"),
 "LD-OPC05-034": ("D", "los datos personales y emocionales contra el rediseno de los procesos internos; sin dos lineas distintas"),
 "LD-OPC05-035": ("D", "UNA DIRECCION (el paso 2 de sistema_pull_push nombra el cuello de botella y la teoria de restricciones lo expande). El pull no es la expansion de subordinar los demas procesos: es UNA forma de hacerlo, no su procedimiento"),
 "LD-OPC05-036": ("D", "gestionar el contacto directo contra redisenar los procesos internos; sin dos lineas distintas"),
 "LD-OPC05-037": ("D", "cerrar el contrato contra el informe periodico de estado: dos formularios distintos del mismo libro, cada uno con lo suyo"),
 "LD-OPC05-038": ("C", "LA C SE SOSTIENE Y AQUI VAN SUS DOS LINEAS. LINEA 1, en plan_de_control, paso 2: establecer el estandar que activara una accion, idealmente UN LIMITE DE CONTROL DE UNA CARTA DE CONTROL; la expanden los diez pasos de control_estadistico_de_procesos, que eligen la caracteristica, el tipo de carta, la linea central, los limites a mas menos tres sigma y los subgrupos racionales. LINEA 2, en control_estadistico_de_procesos, paso 9: definir INSTRUCCIONES DE INTERPRETACION Y ACCION; las expanden los diez pasos del plan_de_control, que fijan quien mide, donde se registra, QUIEN ANALIZA, QUIEN ACTUA y los pasos para volver a control. DOS LINEAS DISTINTAS Y NINGUNO ES LA MADRE"),
 "LD-OPC05-039": ("D", "ninguna de las dos direcciones es una expansion limpia: control_estadistico_metodo_medicion VALIDA un metodo, no lo define, y definiciones_operacionales fija criterios de caracteristicas de calidad, no criterios de reproducibilidad de un instrumento. Dos herramientas contiguas de Deming, cada una expandiendo lo suyo"),
 "LD-OPC05-041": ("D", "el COPQ alimenta con cifras al modelo del optimo, pero NO produce la curva en funcion del nivel de conformidad que el paso 1 del modelo necesita. Una direccion a lo sumo"),
 "LD-OPC05-042": ("D", "el COPQ mide costo y la rejilla ubica al negocio en una de cinco etapas de madurez; libros distintos (Juran y Crosby) y materias distintas"),
 "LD-OPC05-043": ("D", "el COPQ contra la trilogia de Juran: materias distintas, y ninguna linea de una la ejecuta la otra"),
 "LD-OPC05-044": ("D", "la funcion Govern contra los perfiles Current y Target del mismo marco; sin linea expandida en los dos sentidos"),
 "LD-OPC05-045": ("D", "una direccion debil (la incubacion del paso 2 de Wallas); la ruptura de habitos no trae linea que las cuatro etapas ejecuten"),
 "LD-OPC05-046": ("D", "LA C CAE Y ESTO REVOCA ESA PARTE DE LA ADJUDICACION 6.3 DEL ACTA 155, que lo sostuvo POR SER SANO (9.6.3). Bajo la 6.4 SANO SIN FIGURA ES D. Y ademas las dos direcciones apuntan a la misma linea: el sistema que recolecta, analiza y difunde informacion de incidentes, que es el paso 1 de cultura_de_aprendizaje y el paso 2 de cultura_de_seguridad_componentes"),
 "LD-OPC05-047": ("D", "LAS DOS DIRECCIONES APUNTAN AL MISMO EJE (los touchpoints y la experiencia memorable: paso 4 del journey y pasos 1 y 2 de la economia de la experiencia)"),
 "LD-OPC05-048": ("D", "una direccion a lo sumo (el paso 3 del SIPOC nombra clientes y salidas); el SIPOC no es la expansion de una linea de la hoja de necesidades"),
 "LD-OPC05-049": ("C", "LA C SE SOSTIENE Y AQUI VAN SUS DOS LINEAS. LINEA 1, en decision_pivotar_o_proceder, paso 4: toma un Business Model Canvas NUEVO y busca game changers revisando propuesta de valor, precios, canales y relaciones; la expanden los doce pasos de lienzo_modelo_negocio, que son el como se construye e itera el lienzo. LINEA 2, en lienzo_modelo_negocio, paso 12: usar el lienzo como base para PIVOTAR o validar hipotesis del negocio; la expanden los seis pasos de decision_pivotar_o_proceder, que son el como se decide formalmente pivotar o proceder. DOS LINEAS DISTINTAS Y NINGUNO ES LA MADRE"),
 "LD-OPC05-050": ("D", "la decision de pivotar contra validar el modelo financiero; sin dos lineas distintas expandidas en los dos sentidos"),
 "LD-OPC05-051": ("D", "UNA DIRECCION (el paso 3 de defensas_en_profundidad nombra las fallas latentes y el otro nodo las expande); no hay segunda linea de vuelta"),
 "LD-OPC05-052": ("D", "LAS DOS DIRECCIONES APUNTAN A LA MISMA LINEA: ajustar los cinco drivers a la estrategia elegida, que es el paso 4 de la alineacion y el paso 3 del trade off"),
 "LD-OPC05-053": ("D", "los niveles de madurez contra empezar con lo simple; libros distintos, cada uno expandiendo lo suyo"),
 "LD-OPC05-054": ("D", "la reunion de presentacion del problema contra las cuatro preguntas IPO. El paso 4 de IPO nombra OTRA reunion, la de validacion de clientes, y no esta"),
 "LD-OPC05-055": ("D", "el DFSS y su DMADV contra la rejilla de ideacion de mas grande, mas pequeno o combinado: materias distintas"),
 "LD-OPC05-056": ("D", "una direccion limpia (el paso 1 de design_test_repeat lo expanden los cinco de prototyping_possibilities); design_test_repeat es el ciclo abstracto y no la expansion de una linea del otro. Madre e hijo"),
 "LD-OPC05-057": ("D", "UNA DIRECCION (el paso 2 del entrenamiento nombra el dia ZD y el dia ZD lo expande, en tres pasos); el dia ZD no trae linea que el entrenamiento ejecute"),
 "LD-OPC05-058": ("D", "una regla de precedencia contra un glosario de terminos; sin dos lineas distintas"),
 "LD-OPC05-059": ("D", "SU PROPIA RAZON SE DELATA: dice que el puzzle expande UN ARGUMENTO EMPIRICO y el dilema UN PROCEDIMIENTO DE DECISION, que es cada nodo expandiendo lo suyo, PUESTO 2091. Y las dos direcciones apuntan a la misma linea (riqueza contra control)"),
 "LD-OPC05-060": ("D", "la privacidad de datos con opt-out contra la responsabilidad etica general del design thinking; sin linea expandida en los dos sentidos"),
 "LD-OPC05-061": ("D", "los documentos de exportacion contra los seguros de carga y de credito; cada uno expande lo suyo"),
 "LD-OPC05-062": ("D", "los documentos de exportacion contra la seleccion del metodo de transporte; cada uno expande lo suyo"),
 "LD-OPC05-063": ("D", "la ecuacion de valor es en su mayor parte un SUBCONJUNTO de la secuencia SPIN (sus pasos 2 y 3 citan las preguntas de Implicacion y de Necesidad-Beneficio del otro nodo). No hay segunda linea distinta: es madre e hijo"),
 "LD-OPC05-064": ("D", "una direccion (el paso 1 de responsabilidad_gerencial, comprometerte a aprender, lo expande el plan de capacitacion); la educacion estadistica no trae linea que el otro ejecute"),
 "LD-OPC05-065": ("D", "LAS DOS DIRECCIONES APUNTAN A LA MISMA LINEA: validar los hallazgos con el area auditada, que es el paso 1 de ejecucion_auditoria y el paso 5 de relaciones_humanas_auditoria"),
 "LD-OPC05-066": ("D", "LAS DOS DIRECCIONES APUNTAN A LA MISMA LINEA: avisar a los clientes si no puedes operar, que es el paso 3 de el_riesgo_eres_tu y el paso 4 de sigue_operando_pese_al_golpe"),
 "LD-OPC05-067": ("D", "los trece elementos del plan de exportacion contra los programas del Ex-Im Bank: materias distintas, sin linea expandida en ningun sentido"),
 "LD-OPC05-122": ("C", "LA C SE SOSTIENE Y AQUI VAN SUS DOS LINEAS, ya nombradas en la razon original y verificadas hoy contra los nodos. LINEA 1, en error_proofing_servicio, paso 4: SIMPLIFICAR EL TRABAJO para reducir la posibilidad de error humano; la expanden los seis pasos de metodologia_6s (sacar lo que no se necesita, ordenar, limpiar, estandarizar el habito, sostener la disciplina, seguridad). LINEA 2, en metodologia_6s, paso 6: SAFETY, revisa e integra practicas seguras en cada etapa; la expanden los diez pasos de error_proofing_servicio, con sus cinco principios y su validacion antes de escalar. DOS LINEAS DISTINTAS Y NINGUNO ES LA MADRE"),
}

CABEZA_D = ("  [CORRECCION DECLARADA, %s (2026-09-03), ANADIDA SIN BORRAR NADA DE "
            "LO ANTERIOR: LA CLASE PASA DE C A D. Leido contra los dos nodos bajo la "
            "pregunta binaria de la adjudicacion 6.4 del acta 157 (se pueden nombrar DOS "
            "LINEAS DISTINTAS, una en cada nodo, y decir que procedimiento del otro nodo "
            "expande cada una). NO SE PUEDE, y el motivo es este: " % MARCA)
CABEZA_C = ("  [LECTURA DEL %s (2026-09-03), ANADIDA SIN BORRAR NADA DE LO ANTERIOR: "
            "LA CLASE SE QUEDA EN C. " % MARCA)
COLA = (". Dossier de la lectura en docs/loop/SALIDA_V157_T2A_DOSSIER.txt y veredicto "
        "en docs/loop/SALIDA_V157_T2_LOTE1.txt.]")


def leer(r):
    return io.open(r, encoding="utf-8").read()


def entradas():
    return [json.loads(x) for x in leer(REGISTRO).splitlines() if x.strip()]


def guardar(E):
    with io.open(REGISTRO, "w", encoding="utf-8", newline="\n") as fh:
        for e in E:
            fh.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")


def sha_dataset():
    """sha256 de TODO dataset/, fichero a fichero y en orden. Si esta tarea
    tocara una sola coma del grafo, este numero cambia."""
    h = hashlib.sha256()
    for base, _dirs, files in sorted(os.walk(DATASET)):
        for n in sorted(files):
            ruta = os.path.join(base, n)
            h.update(os.path.relpath(ruta, RAIZ).replace("\\", "/").encode("utf-8"))
            with io.open(ruta, "rb") as f:
                h.update(f.read().replace(b"\r\n", b"\n"))
    return h.hexdigest()


def censo_y_aristas():
    N = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    vivos = sum(1 for n in N.values() if not n.get("deprecado"))
    sig = sum(len(n.get("nodos_siguientes") or []) for n in N.values())
    prev = sum(len(n.get("nodos_previos") or []) for n in N.values())
    return len(N), vivos, len(N) - vivos, sig, prev


def n_veredictos():
    return sum(1 for x in io.open(VERED, encoding="utf-8") if x.strip())


def tocar_md(texto, ld, clase_vieja, clase_nueva, nota):
    """Tacha la celda de clase y anade la correccion al final de la columna de
    motivo. El texto viejo de la columna NO se borra: la nota va detras."""
    num = int(ld.split("-")[-1])
    pat = re.compile(
        r"(\| %d \| REGISTRO DE CITAS `OP-C-05` \| [a-z0-9_]+ <-> [a-z0-9_]+ \| )"
        r"%s( \| %s \| )([^\n|]*)(\|)" % (num, re.escape(clase_vieja), re.escape(ld)))
    m = pat.search(texto)
    if not m:
        return texto, False
    if clase_nueva != clase_vieja:
        celda = "~~%s~~ %s" % (clase_vieja, clase_nueva)
    else:
        celda = clase_vieja
    nuevo = "%s%s%s%s %s |" % (m.group(1), celda, m.group(2), m.group(3).rstrip(), nota)
    return texto[:m.start()] + nuevo + texto[m.end():], True


def main():
    print("=" * 78)
    print("VUELTA 157, TAREA 2: EL LOTE 1 DEL SACO, 66 LECTURAS")
    print("=" * 78)
    print("")

    ids = json.load(io.open(NOMINA, encoding="utf-8"))["lote"]
    assert sorted(ids) == sorted(V), "la nomina sellada y los veredictos no calzan"
    print("CIFRA lecturas de la nomina sellada: %d" % len(ids))
    print("CIFRA veredictos escritos en este instrumento: %d" % len(V))
    print("")

    print("A) LA FRONTERA, ANTES DE TOCAR NADA")
    sha_antes = sha_dataset()
    censo_antes = censo_y_aristas()
    n_antes = n_veredictos()
    print("   sha256 de dataset/ ANTES : %s" % sha_antes)
    print("   censo ANTES              : %d nodos, %d vivos, %d deprecados" % censo_antes[:3])
    print("   aristas ANTES            : %d siguientes, %d previos" % censo_antes[3:])
    print("   CIFRA n, veredictos del cribado ANTES: %d" % n_antes)
    print("")

    E = entradas()
    antes_razon = {e["cita"].split(",")[0]: e["razon"] for e in E}
    antes_clase = {e["cita"].split(",")[0]: e["clase"] for e in E}
    texto_md = leer(LD_MD)

    print("B) LOS 66 VEREDICTOS, UNO A UNO")
    a_d, se_queda_c, ya, sin_fila = 0, 0, 0, []
    for e in E:
        ld = e["cita"].split(",")[0]
        if ld not in V:
            continue
        nueva, motivo = V[ld]
        vieja = e["clase"]
        if MARCA in e["razon"]:
            ya += 1
            print("   %-16s %s -> %s   YA ESTABA" % (ld, vieja, nueva))
            continue
        cabeza = CABEZA_D if nueva != vieja else CABEZA_C
        e["razon"] = e["razon"] + cabeza + motivo + COLA
        e["clase"] = nueva
        e["cita"] = re.sub(r"clase [A-Z]+$", "clase %s" % nueva, e["cita"])
        texto_md, ok = tocar_md(
            texto_md, ld, vieja, nueva,
            "CORRECCION DECLARADA (vuelta 157, LOTE 1): la clase pasa de ~~%s~~ a %s. %s."
            % (vieja, nueva, motivo[:220]) if nueva != vieja else
            "LECTURA DEL LOTE 1 (vuelta 157): la C SE SOSTIENE y sus dos lineas quedan nombradas en la razon del registro de citas.")
        if not ok:
            sin_fila.append(ld)
        if nueva != vieja:
            a_d += 1
        else:
            se_queda_c += 1
        print("   %-16s %s -> %s   %s" % (ld, vieja, nueva, motivo[:78]))
    print("")

    if sin_fila:
        print("ROJO: no se encontro la fila del .md de: %s" % ", ".join(sin_fila))
        print("FIN")
        return 1

    guardar(E)
    with io.open(LD_MD, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto_md)

    print("C) LAS GUARDAS, MEDIDAS Y NO PROMETIDAS")
    D = entradas()
    assert len(D) == len(E) == 154, "el numero de lineas del registro se movio"
    for d in D:
        ld = d["cita"].split(",")[0]
        assert d["razon"].startswith(antes_razon[ld]), (
            "%s: el texto viejo de `razon` YA NO ES PREFIJO del nuevo" % ld)
    print("   C.1 PREFIJO: las %d razones del registro conservan su texto viejo ENTERO" % len(D))
    pares_antes = {tuple(sorted(e["par"])) for e in E}
    pares_desp = {tuple(sorted(d["par"])) for d in D}
    assert pares_antes == pares_desp, "esta tarea NO mueve ningun par"
    print("   C.2 PARES: %d pares, los mismos antes y despues" % len(pares_desp))
    movidas = [d["cita"].split(",")[0] for d in D
               if d["clase"] != antes_clase[d["cita"].split(",")[0]]]
    print("   C.3 CLASES MOVIDAS: %d, y todas de C a D" % len(movidas))
    assert all(antes_clase[x] == "C" for x in movidas), "se movio una clase que no era C"
    assert all(d["clase"] == "D" for d in D if d["cita"].split(",")[0] in movidas)

    sha_desp = sha_dataset()
    censo_desp = censo_y_aristas()
    n_desp = n_veredictos()
    print("   C.4 FRONTERA, sha256 de dataset/ DESPUES: %s" % sha_desp)
    print("       censo DESPUES  : %d nodos, %d vivos, %d deprecados" % censo_desp[:3])
    print("       aristas DESPUES: %d siguientes, %d previos" % censo_desp[3:])
    assert sha_antes == sha_desp, "EL GRAFO SE MOVIO: la frontera esta rota"
    assert censo_antes == censo_desp, "el censo o las aristas se movieron"
    print("       EL REGISTRO CAMBIA, EL GRAFO NO: sha256 IDENTICO y censo IDENTICO")
    print("   C.5 CIFRA n, veredictos del cribado DESPUES: %d" % n_desp)
    assert n_antes == n_desp == 3388, "n se movio: tenia que quedarse en 3.388"
    print("       n NO SE MUEVE y sigue en 3.388")
    print("")

    r = subprocess.run(["git", "diff", "--numstat", "--", "docs/plan/"],
                       cwd=RAIZ, capture_output=True)
    print("   numstat de docs/plan/:")
    for l in r.stdout.decode("utf-8", "replace").strip().splitlines():
        print("      %s" % l)
    print("")

    clases = {}
    for d in D:
        if d.get("via") == "LECTURA_DIRIGIDA":
            clases[d["clase"]] = clases.get(d["clase"], 0) + 1
    print("D) EL SACO, RECONTADO SOBRE EL REGISTRO YA ESCRITO")
    print("   CIFRA lecturas dirigidas por clase: %s" % json.dumps(clases, sort_keys=True))
    print("   CIFRA reclasificadas de C a D en este lote: %d" % a_d)
    print("   CIFRA que sostienen C en este lote: %d" % se_queda_c)
    print("   CIFRA que ya estaban escritas: %d" % ya)
    print("")
    print("NINGUNA SALIO A. No hay candidato a fusion, no se toca una arista y n no se")
    print("mueve. El limite de la 6.1 sigue vigente y no se cruzo.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
