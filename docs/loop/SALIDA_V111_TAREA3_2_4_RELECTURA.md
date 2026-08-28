# TAREA 3.2 a 3.4, vuelta 111. Relectura entera, HOY, de los cinco SATELITE
que nadie habia vuelto a leer (20, 21, 38, 66, 93). Censo previo en
docs/loop/SALIDA_V111_TAREA3_1_CENSO.txt (109 NO RESUELTA, 5 con pregunta de
tres vias, los 5 SATELITE, VERDE contra la nomina del encargo).

Para los cinco, la pregunta de DIRECCION (9.6.2) y la de SATELITE/OBJETO
(estructura del paso_casado) son preguntas DISTINTAS (3.3). En los cinco, el
NO RESUELTA de hoy viene de `correccion_v105` sobre `direccion_leida`
(razon propia, banco 9.6.2, escrita en vuelta 105, INDEPENDIENTE del
veredicto SATELITE): releer SATELITE hoy no arrastra la direccion salvo que
el contra-caso encuentre algo que la propia correccion_v105 no viera, y en
ninguno de los cinco lo encuentra.

## 20 -- waterfall_vs_agile_development -> modelo_customer_development
Paso 3 de la madre: "Alinear el proceso de desarrollo de producto con el
proceso de Customer Development". Verbo "Alinear", objeto directo "el
proceso de desarrollo de producto", complemento "con el proceso de Customer
Development". El hijo (los cuatro pasos del modelo CD: Discovery,
Validation, Creation, Company-Building) vive en el complemento.
CONTRA-CASO: ¿"el proceso de desarrollo de producto" podria absorber, como
objeto directo, redefinirse segun el modelo citado en el complemento? CAE:
alinear A con B no es "reemplazar A por B" ni "ejecutar B", es coordinar
dos procesos que conservan su identidad; el hijo describe el CONTENIDO
INTERNO de B entero, sin decir nada de la coordinacion con A (que es lo que
hace el par 13, el otro hijo de la misma linea). Decidido **SATELITE**, no
se mueve.

## 21 -- build_measure_learn -> value_proposition_canvas
Paso 0 de la madre: "Generar una hipotesis clara a partir de los Canvas de
Value Proposition y Business Model". Verbo "Generar", objeto directo "una
hipotesis clara", complemento de origen "a partir de los Canvas...". El
hijo ensena a CONSTRUIR el canvas (el insumo), no a generar la hipotesis.
CONTRA-CASO: si no hay canvas no hay hipotesis, ¿es el hijo un prerrequisito
tan intimo que cuenta como objeto directo? CAE: el objeto directo es LA
HIPOTESIS; "a partir de" marca el canvas como fuente externa al acto de
generar, y el hijo no dice nada sobre el paso de insumo a conclusion (la
sintesis). Decidido **SATELITE**, no se mueve.

## 38 -- obtencion_compromiso -> enfoque_etapa_investigacion
Paso 4 de la madre: "Pon tu esfuerzo de mejora en las etapas de
investigacion y demostracion de capacidad, no en el cierre". Verbo "Pon",
objeto directo "tu esfuerzo de mejora", complemento de destino "en las
etapas...". El hijo cubre SOLO investigacion (una de las dos etapas
nombradas) y ademas argumenta en contra de invertir en la otra.
CONTRA-CASO: por el patron de dos argumentos del 97 (desarrollar uno de los
elementos coordinados es OBJETO), ¿aplica igual aqui? CAE: no es el mismo
patron; este es un complemento locativo/destino ("poner el esfuerzo EN X"),
no un verbo de dos argumentos co-iguales, y el objeto directo real ("tu
esfuerzo de mejora") no lo desarrolla el hijo en absoluto (el hijo habla de
tecnica de preguntas, no de gestion de esfuerzo). Decidido **SATELITE**, el
mas claro de los cinco, no se mueve.

## 66 -- cultura_justa_3 -> cultura_de_aprendizaje
Paso 3 de la madre: "Balancear la necesidad de accountability con la
proteccion al aprendizaje organizacional". Verbo "Balancear", objeto
directo "la necesidad de accountability", complemento "con la proteccion
al aprendizaje organizacional". El hijo desarrolla SOLO el lado del
aprendizaje, cero lineas de accountability.
CONTRA-CASO: si desarrollar B (el complemento con "con") fue OBJETO en el
97 cuando el hijo desarrollaba A, ¿aplica el mismo perdon aqui para B? CAE:
en el 97 el hijo desarrollaba A, el objeto directo MISMO; aqui el hijo
desarrolla B, el lado contrario del objeto directo, y "balancear X con Y"
pide un acto de equilibrio entre los dos, no el desarrollo aislado de
ninguno (razon ya usada por la propia correccion_v105 sobre la direccion).
Decidido **SATELITE**, no se mueve.

## 93 -- estandares_voluntarios -> definiciones_operacionales_de_calidad
Paso 3 de la madre: "Documentar el estandar con definiciones operacionales
claras y medibles". Verbo "Documentar", objeto directo "el estandar",
complemento instrumental "con definiciones operacionales...". El hijo es un
procedimiento BILATERAL cliente-proveedor, mientras el estandar del objeto
directo es de INDUSTRIA por consenso de comites.
CONTRA-CASO: ¿"documentar el estandar" consiste, en el fondo, en escribir
esas definiciones, de modo que desarrollarlas es desarrollar el objeto
directo? CAE: misma razon que ya cerro la DIRECCION (correccion_v105): el
hijo es bilateral y de escala distinta (una relacion cliente-proveedor) al
estandar de industria del objeto directo; no vive en el objeto directo ni
transparenta el acto de documentar, vive en el instrumento nombrado por el
complemento, con un alcance que ni siquiera coincide del todo con el.
Decidido **SATELITE**, no se mueve.

## TAREA 3.5, la cifra
Ninguno de los cinco se mueve: los cinco SIGUEN SATELITE tras la relectura
con contra-caso. La DIRECCION (NO RESUELTA) tampoco se mueve, porque en los
cinco esta decidida por `correccion_v105` sobre una razon de 9.6.2
independiente del veredicto SATELITE (3.3). Sin correccion_v111 que
declarar sobre estos cinco: `contar_cierre_efectivo.py` sigue en 74/109
(59,6%), sin recomputo necesario. `verificar_cobertura_bolsa_tres_vias.py`
sigue en 74/74/0 (los cinco son NO RESUELTA, fuera de esa cuenta).
