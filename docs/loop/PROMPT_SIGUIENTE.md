Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. Cualquier guarda en rojo fuera de lo que
08_VERIFICACION.md declara permitido, o cualquier operacion cuyo texto
no alcance para ejecutarse sin decidir, te detiene a ti y convoca al
auditor.

LEE EL ACTA DE LA VUELTA 75 ANTES DE TOCAR NADA (docs/loop/ACTA_AUDITOR.md,
a partir de la linea 20976). No es tramite: esa acta encontro UNA CAIDA
FUERA DE LOS DISCUTIBLES MARCADOS y por eso esta vuelta trae relectura
al doble. Lo que sigue sale entero de ahi.

EL AVISO DE LAS RACHAS, y va delante porque cambia como trabajas:
  - CLASE O CIFRA PUBLICADA: UNA tanda (la racha limpia de cuatro se
    corto en la 75). La parada pide DOS SEGUIDAS. Si esta vuelta trae
    otra de esa especie, EL BUCLE SE DETIENE.
  - REPORTE: DOS tandas seguidas (el D9 en la 74, el gemelo del D3 en
    la 75). La parada pide TRES. Esta es la ultima que hay.
  No escribas ni una afirmacion que no puedas señalar en la salida de un
  instrumento corrido HOY. Si no la mediste, se marca "a verificar" y se
  encarga, que es lo que la regla permite.

====================================================================
TAREA 1: registros, cinco correcciones declaradas y un censo
====================================================================

1.1. REGISTRA LA CAIDA DE CLASE, con nombre y sin suavizarla. La arista
segmentos_de_clientes_problema_necesidad -> get_out_of_the_building se
escribio contra P.9 punto 1 del BANCO_DEL_PLAN ("los enlaces corren
DESPUES de las fusiones que tocan sus destinos"): get_out_of_the_building
esta en el campo eliminar de OP-M-05-EDIFICIO, que es UNA DE LAS SEIS
fusiones que tu propio reporte cito dos veces como enrutadas a la fase
06. La CLASE estaba bien leida; lo que fallo fue la ELEGIBILIDAD. La
caida esta FUERA del marcado y por eso baja el credito de la tanda
entera (AUDITOR.md seccion 1.2).

1.2. REGISTRA LA CAIDA DE REPORTE, dentro del marcado (D3). En
scripts/loop/vuelta75_op_e01_tramo1_escribir.py, PARES_DESCARTADOS dice
de planificacion_estrategica_despliegue_2 que "es gemelo de
planificacion_estrategica_despliegue, no hijo nuevo". El auditor leyo
los dos enteros: comparten la cabeza (mision, vision, metas) y divergen
en el cuerpo (catch ball y scorecards contra paridad con lo financiero,
lenguaje comun y poda de lo no alineado). Eso no es un calcado, y
publicar "es gemelo" es adjudicar una clase sin par leido. La
DISPOSICION (no enlazar) queda CONFIRMADA, con la razon corregida en
1.3.d.

1.3. LAS CINCO CORRECCIONES DECLARADAS. Todas con el texto viejo
delante y sin reescribirlo, como esta casa manda.

  a) REVIERTE LA ARISTA. Quita get_out_of_the_building de
     nodos_siguientes de segmentos_de_clientes_problema_necesidad, corre
     el ciclo de Gate 0 entero para que la reciprocidad se deshaga sola,
     y comprueba por diff de grafos que quedan VEINTICINCO aristas
     nuevas contra el commit 62d4f28e y no veintiseis. El par vuelve a
     la bolsa APARTADO, con "espera a OP-M-05-EDIFICIO" escrito al lado.
     NO la reescribas al superviviente customer_discovery_get_out_of_building:
     eso seria escribir el id de manana y P.9 punto 2 pide el id
     resuelto AL DIA DE SU ESCRITURA. NO la dejes para que la limpie
     OP-S-12: eso es exactamente lo que P.9 existe para impedir.

  b) OP-E-01, en docs/plan/OPERACIONES.jsonl y en 04_ENLACES.md: anade a
     su verificacion el FILTRO DE ELEGIBILIDAD P.9.1, con estas palabras
     o las tuyas sin perder ninguna:
       "Todo candidato de la bolsa se cruza contra los campos eliminar y
        superviviente de las operaciones NO EJECUTADAS. Si el destino o
        la madre muere en una operacion pendiente, el par NO se lee para
        escribir: se aparta con el id de esa operacion escrito al lado y
        espera su turno."
     Su verificacion copiaba P.9 sin su punto 1, y esa omision es la que
     dejo pasar la arista de 1.3.a.

  c) OP-E-05, en OPERACIONES.jsonl: su depende_de pasa de ["OP-M-01"] a
     ["OP-M-01", "OP-M-01-FUSION"]. Verificado campo a campo: sus nodos
     incluyen requisitos_gates_con_dientes, que esta en el eliminar de
     OP-M-01-FUSION; su propia verificacion dice "los ids se escriben
     resueltos tras OP-M-01-TRIO" y la nota de OP-M-01-FUSION dice
     "OP-M-01-TRIO SE DISUELVE AQUI". P.9 punto 1 manda que eso viva en
     el campo, "no en una nota". La operacion NO cambia de estado:
     sigue bloqueada, ahora con el campo diciendolo. Tu reporte declaro
     esta discrepancia y con razon no la resolvio; el auditor la
     adjudico y aqui solo se escribe.

  d) LA RAZON DEL DESCARTE de consejo_de_calidad_y_rol_del_director
     contra planificacion_estrategica_despliegue_2: sustituye "es
     gemelo" por la razon que si se sostiene, y es mejor que la vieja:
     el destino lleva sufijo numerico y la verificacion de OP-S-09
     (05_SANEO, orden 8) exige "ningun id vivo lleva sufijo numerico de
     duplicado". Por P.9 punto 1, el enlace espera a OP-S-09. Deja de
     ser un descarte sin fecha y pasa a ser un aplazamiento con
     operacion nombrada.

  e) EL UNIVERSO DEL CONTROL DE RACIMOS, en docs/PENDIENTES.md seccion
     "2. TRES RACIMOS CON MIEMBROS DE OTRO DOMINIO" y en 04_ENLACES.md
     seccion "2. LOS RACIMOS CON MIEMBRO DE OTRO DOMINIO". La frase "el
     control los encuentra todos de una vez" es FALSA y esta medida como
     falsa. Escribe la correccion: el control cubre los racimos
     censados en RACIMOS_MIEMBROS.jsonl, que el commit d4d2652f declara
     "reconstruidas de las razones de FRANJA_VEREDICTOS.jsonl", o sea los
     racimos QUE EL CRIBADO DECLARO. "El lienzo de propuesta de valor"
     es un racimo del INFORME (seccion 14, remedido a siete miembros por
     cierre transitivo) y nunca fue racimo de franja: no se perdio, es
     de otra especie. Las dos fuentes son distintas POR CONSTRUCCION.

1.4. EL CENSO QUE FALTA, y es medicion pura, no decision. El auditor
midio que de los 168 nodos distintos de los 32 racimos, 86 caen dentro
de algun componente de docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl (332
componentes, 838 nodos) y 82 caen fuera. Lo que nadie ha medido es
CUANTOS DE ESOS 168 NO TIENEN NINGUNA OPERACION QUE LOS NOMBRE. Corre el
barrido contra OPERACIONES.jsonl (campos nodos, eliminar y
superviviente, con frontera de palabra y no por substring: OP-M-03-I
esta dentro de OP-M-03-II y de OP-M-03-III, y sin frontera la cuenta
sale mal). Publica la tabla por racimo y por decision de MESA_RACIMOS.
CIFRA CONOCIDA QUE TIENE QUE REPRODUCIRSE: los tres miembros del racimo
"Programa de catorce pasos de Crosby" (concepto_programa_catorce_pasos,
programa_mejora_calidad_14_pasos, crosby_programa_14_pasos_introduccion)
NO son nombrados por ninguna operacion. Si tu barrido dice otra cosa,
declara la discrepancia en vez de resolverla copiando.
NO ENRUTES NADA. El enrutamiento se decide con la cifra delante, en la
vuelta siguiente, y no antes.

1.5. CITA, sin reescribirlas, las dos adjudicaciones del auditor que ya
cierran pendientes de doctrina y que por tanto NO vuelves a preguntar:
  - PENDIENTE 1 (universo de "racimo con miembro ajeno"): adjudicado con
    el remedio ya escrito. "Mapeo del flujo de valor" YA esta resuelto
    por la segunda salida (su dominio_censado es literalmente "quality +
    environmental + nucleo", que ES la declaracion transversal
    explicita). desarrollo_value_proposition_usp va por la primera
    salida (la nomina se depura), porque el informe seccion 33.2 ya lo
    leyo: "CAE, y ni siquiera es del dominio... CERO SOLAPE", y el 33.3
    lo llama "defecto de NOMINA, no de lectura".
  - PENDIENTE 2 (MESA_RACIMOS dentro de los 221 actos): confusion de
    categoria, contestada citando MESA_RACIMOS.md seccion 6: "CERRADA
    como insumo del plan de la pasada unica... lo que sigue no es
    decidir, es planificar la ejecucion con estas cuatro como marco". La
    mesa no es un acto: es el marco. Y ya esta cableada: la DECISION 4
    tiene operacion propia, OP-S-09, cuya evidencia la cita por su
    nombre; la 1 la cita OP-M-02; la 2 y la 3 las cita OP-D-04.

1.6. CITA, tambien sin reescribirla, la adjudicacion de las dos cifras
de enlaces: 17.671 es "entradas de nodos_siguientes mas entradas de
nodos_previos" y 9.495 es "union dirigida unica". El auditor midio el
17.671 en el commit de apertura 62d4f28e y da clavado. Las dos se
publican de aqui en adelante CON SU DEFINICION AL LADO, y ninguna
sustituye a la otra.

====================================================================
TAREA 2: la relectura al doble, el cierre de OP-E-02, y solo
         despues el tramo 2
====================================================================

2.1. LA RELECTURA AL DOBLE DEL TRAMO 1, y es la primera cosa que se
hace. La manda AUDITOR.md seccion 1.2 porque la caida aparecio fuera del
marcado. NO es repetir la misma lectura: es correr la vara que el D4
confeso NO haber corrido.
  a) Para las VEINTICINCO aristas que quedan tras la reversion de 1.3.a,
     corre la regla 9.6.1 COMPLETA (la mayoria de la madre) par a par,
     no solo la 9.6.2 de contenido. Publica por par si la 9.6.1
     confirma, si la deja igual, o si voltea la direccion.
  b) Aplica ademas a las veinticinco el filtro P.9.1 de 1.3.b, ya con el
     instrumento escrito. El auditor lo corrio y le dio UNA sola roja
     (la revertida); si tu corrida da otra cosa, declara la
     discrepancia.
  c) DATO DEL AUDITOR QUE NO TIENES QUE VOLVER A MEDIR salvo que quieras
     contrastarlo: el chequeo de escalera (si el hijo ya apuntaba a la
     madre) dio CERO de 26. Ninguna cierra ciclo de dos.
  d) Cualquier arista que la 9.6.1 voltee o tumbe se corrige con
     correccion declarada y recomputo, como cualquier otra.

2.2. CIERRA OP-E-02. Ya puede cerrar: no pide fundador, no pide doctrina
nueva y no escribe ni una arista. Cierra con DECLARACION, que es lo que
su propia ficha pide ("o la nomina se depura, o el racimo se declara
transversal de forma explicita"). Escribe en su registro:
  - el suelto comprender_alineacion_etica_ia va a mesa (racimo sin
    centro, tercer supuesto de la regla del 11 ago 2026), sin arista;
  - los 171 miembros de los 32 racimos siguen vivos, cero fundidos desde
    el censo, cero racimos con miembro ajeno tras normalizar NUCLEO
    contra core (re-corrido por el auditor con salida identica);
  - los tres ejemplares resueltos como dice 1.5, cada uno por su salida
    del remedio.
Con eso la ficha tiene destino y la operacion queda HECHA por el
criterio de la fase.

2.3. SOLO ENTONCES, EL TRAMO 2 DE OP-E-01.
  a) RECALIBRA la bolsa antes de leer. No reuses la salida de la vuelta
     75: el grafo se movio en esta misma vuelta con la reversion de
     1.3.a. Es EL INSTRUMENTO MANDA, y en esta operacion ya mordio una
     vez.
  b) Pasa la bolsa fresca por el filtro P.9.1 ANTES de leer nada, y
     publica cuantos candidatos aparta y por que operacion. Esa cifra es
     nueva y no la tiene nadie.
  c) Lee la cabeza de la bolsa ya filtrada, en el orden del archivo y
     sin sorteo (el paso 3 esta decidido: leer entera). Tramo de 30
     pares como el anterior, salvo que el filtro deje menos.
  d) Vara 9.6.1 y 9.6.2 del banco, las dos, par a par. La 9.6.1 deja de
     ser opcional en esta operacion desde esta vuelta.
  e) Entre fichas, el CICLO DE GATE 0 ENTERO (el cuarto comando solo si
     la operacion toca el censo, que en esta fase no ocurre) y LAS TRES
     SUITES en verde. Cero auto-aristas tras resolver y cero duplicadas:
     si alguna aparece, es PARADA de guarda.

2.4. EL D2 VA A RELECTURA CONJUNTA, y es la unica discrepancia de clase
de la ciega. El auditor discrepa de tu descarte de
mejora_calidad_crosby paso 2 -> concepto_programa_catorce_pasos. Su caso,
con su evidencia, esta en el acta seccion 2 (D2): el paso 2 de la madre
nombra el programa en una linea, el hijo es ese programa del mismo libro
y sus cuatro pasos son el procedimiento de adoptarlo; y sobre todo, la
fusion que la arista tendria que deshacer NO ESTA EN EL PLAN (ninguna
operacion nombra a ninguno de los tres miembros del racimo, y el nodo no
lleva sufijo numerico, asi que tampoco cae en OP-S-09). VERIFICALO
CONTRA EL GRAFO Y CONTRA OPERACIONES.jsonl POR TU CUENTA y DECIDE CON LA
VARA. Si le das la razon, escribes la arista con correccion declarada.
Si se la quitas, escribes por que con la cifra delante. Las dos salidas
son legitimas; lo que no lo es es dejarla sin resolver otra vuelta.

2.5. SIGUE EN MODO CONTINUO por el orden escrito hasta que una guarda
salga en rojo fuera de lo permitido, una ficha no alcance para
ejecutarse sin decidir, o se cumpla una condicion de parada. Recuerda lo
que ya esta medido y no hace falta volver a descubrir: OP-M-03-ENLACES,
OP-E-04, OP-E-05, OP-M-01-ESLABONES y OP-M-01-SEXTO estan las CINCO
bloqueadas por las fusiones de la fase 06 (la de OP-E-05 ahora con su
campo corregido en 1.3.c). OP-E-03 espera a que OP-E-01 termine. OP-E-06
y OP-E-07 no tienen bloqueo de dependencia pero esperan su turno.

NO ejecutes las seis fusiones enrutadas a la fase 06: su destino esta
escrito y su momento es cuando sus mesas se sienten. NO reabras los
nueve del subconjunto: son cosa juzgada por decision del fundador. NO
abras la fase 05 hasta cerrar la 04, y ten presente que la fase 05 tiene
PARADA ESCRITA al cerrarse (AUDITOR.md seccion 4): la fase 06 no se abre
en este tramo.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
