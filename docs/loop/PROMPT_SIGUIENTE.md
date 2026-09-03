Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), en REGIMEN COMPLETO, con las
guardas obligatorias por operacion.

TU VUELTA ES LA 159. El acta que te abre es la 158. Esto va en la cabecera
fija del encargo desde hoy, por la adjudicacion 6.1 del acta 158, y no es
cosmetico: las dos guardas del cierre (tallar_cabecera_reporte.py y
verificar_apertura_sellada.py) localizan la apertura buscando el acta de la
vuelta N menos 1, y el invariante de la casa es ACTA N, VUELTA N MAS 1. En
la vuelta pasada nadie te dijo el numero, tu elegiste 157 igualandolo al
acta, y las dos guardas se quedaron ciegas. Tus ficheros de esta vuelta se
llaman SALIDA_V159_*.

HASHES ADMITIDOS EN EL CORREDOR DE ESTA VUELTA: NINGUNO. No hay commit de
decision del fundador que admitir. Todo commit dentro del corredor es tuyo
y cuenta como intruso.

Y EL SELLO DE APERTURA VA EN EL PRIMER COMMIT DEL CORREDOR, NO EN EL
CIERRE. La guarda ya lo exige y esta vez podra correr. Tu caida 1 de la
157 no fue de cifra (yo re derive el valor con git rev-parse 23004b4d^ y
da abb2fe4e), fue de procedimiento, y el remedio no hay que construirlo:
basta con que la guarda no este bloqueada.

El acta que te encarga esto es ACTA_AUDITOR.md, VUELTA 158. Su veredicto:
las nueve tareas entregadas y TODO el cierre reproduce al digito con mi
propia mano (censo 3.853/3.169/684, aristas 8.780/8.740/17.520/9.914 con
solo_sig 1174 y solo_prev 1134, ciclo entero con numstat en cero filas,
Gate 0 en 26 de 26 y ademas IDENTICO al tuyo linea por linea, motor 25/25,
vitest 80 y 1.030 con 3 saltadas desde web/, tsc exit 0 sin una linea,
archivo 3.388 con A 551 B 72 C 5 D 2.760 y cero huecos y cero duplicados,
registro 154 con LECTURA_DIRIGIDA C 57 y D 65, expediente 71/36/24/12/0/7,
fase 03 16/12/4, fase 06 16/16/0, fase 08 con OP-V-01, fase 09 3/0/3, y la
bateria de las 23 VERDE en corrida sola por mi mano con RUIDO DE
CONCURRENCIA 0). Tu aditividad la medi yo: 154 lineas a 154, cero pares
perdidos y cero nuevos, 67 razones ampliadas con PREFIJO ROTO 0, 62 clases
movidas y las 62 de C a D, y CERO borrados en los seis .py. Tu correccion
de mi cifra es correcta y la registro como caida mia: eran SEIS de mis
diez casos en tu lote, no cinco.

TU PARADA NO ES PARADA Y LA ADJUDICO EN LA 6.1. Hiciste bien las tres
cosas que importaban: no parcheaste las guardas, no fabricaste los
ficheros de apertura que faltaban, y no publicaste tabla tallada sin
tallador. Lo que faltaba era un numero, y el numero lo pone el encargo.

PERO MI CIEGA TRAE UNA DISCREPANCIA FUERA DE TUS SEIS DISCUTIBLES, Y POR
ESO EL CREDITO DE LA TANDA BAJA. Lei 19 casos a ciegas (sellados en
docs/loop/_auditor_v158_mis_adjudicaciones.txt, sha1 73ad4073, calculado
antes de destapar): coincidimos en 16. Dentro de lo marcado discrepo en
dos, 027 y 122, y en los dos tu ya habias avisado. Fuera de lo marcado
discrepo en UNO, LD-OPC05-005, y ese no lo habia avisado nadie. La regla
es literal y no tiene excepcion para un fallo de metodo interesante: baja
el credito de la tanda y el tramo se relee al doble. Va encargado en la
TAREA 2 y es bloqueante.

- TAREA 1, LOS REGISTROS, Y ES LO PRIMERO: deja escritas en el repo las
  doce adjudicaciones de la seccion 6 del acta 158 donde cada una vive
  (6.1 y 6.2 en el docstring de scripts/loop/verificar_apertura_sellada.py
  y en el de scripts/loop/tallar_cabecera_reporte.py, que es donde vive el
  invariante ACTA N VUELTA N MAS 1; 6.3 en
  scripts/loop/vuelta152_registro_de_citas_opc05.py, que es donde vive la
  doctrina de vias y clases, y en el instrumento de lectura del lote;
  6.4 y 6.5 en la razon de LD-OPC05-005, LD-OPC05-027 y LD-OPC05-122 del
  registro; 6.6 en el instrumento que escribe el campo cita; 6.7 en los
  once .py que llevan el patron; 6.8 en
  scripts/loop/verificar_re_sellado.py; 6.9 y 6.10 en la funcion de la
  P3b de scripts/loop/vuelta150_3_relectura_expediente.py; 6.11 en el
  instrumento de la TAREA 8 de la 157; 6.12 en el instrumento del lote),
  TODAS POR ADICION Y CON CORRECCION DECLARADA, sin borrar una linea del
  texto viejo. Y la aditividad se MIDE, no se promete: numstat de git para
  los .py y prefijo comprobado por assert para el JSONL, como en la 156 y
  la 157.

- TAREA 2, Y ES BLOQUEANTE, LA RELECTURA CONJUNTA Y EL TRAMO AL DOBLE.
  (2.a) LAS TRES EN DISPUTA, POR LA 6.4. Mi caso escrito esta en la
  seccion 3 y 3.1 del acta 158. LD-OPC05-005: tu motivo (las dos
  direcciones apuntan a la misma linea, paso 1 de aim_of_leadership y
  paso 13 de causas_comunes_vs_especiales) es CIERTO PARA ESE PAR, pero
  hay otro par disponible, y es el paso 2 de aim (investigar las causas
  de raiz DEL SISTEMA) expandido por los quince pasos de causas, contra
  el paso 13 de causas expandido por los pasos 1, 3 y 5 de aim. Verifica
  TU contra los nodos y decide con la vara, incluso contra mi, y publica
  lo que midas. LD-OPC05-027: me sale D, porque el paso 2 de SPIN repite
  la linea del paso 3 de cierre en vez de expandirla y el paso 3 aplaza
  el como a capitulos posteriores. LD-OPC05-122: me sale D, porque el
  paso 6 de 6S es seguridad ocupacional y error_proofing_servicio es
  prevencion de error en procesos de servicio, materia distinta; y esto
  revoca mi propia 6.4 del acta 157, que la sostuvo. MI LECTURA NO ES LA
  VARA, EL NODO LO ES.
  (2.b) EL TRAMO AL DOBLE, POR LA 6.5: las 41 lecturas del lote 1 que
  cayeron a D y que nadie ha vuelto a mirar. La cuenta, para que la
  contrastes: del lote de 66, 62 se movieron a D y 4 sostuvieron C; de
  esas 62 relei yo 15 hoy y mi ciega anterior leyo 6 (007, 019, 031, 043,
  055, 067), sin solape; 62 menos 21 da 41. TU INSTRUMENTO RECOMPUTA ESA
  NOMINA Y LA PUBLICA: si no da 41, paras y lo dices antes de leer nada.
  Segunda pasada independiente bajo la 6.3.
  (2.c) LA 6.3, QUE ES LA LECCION Y SE APLICA DESDE LA PRIMERA LECTURA:
  la pregunta binaria de la 6.4 es un EXISTENCIAL. Hallar un par de
  lineas que colapsa en la misma linea prueba que ESE par no es la
  figura, no que no la haya. Cuando el colapso del 9.22 sea tu motivo de
  descarte, la razon tiene que decir tambien que NINGUN otro par de
  lineas sostiene la figura, y NOMBRAR el par mas fuerte que descartaste.
  (2.d) LAS GUARDAS, LAS MISMAS Y NO SE AFLOJAN: cada cambio de clase con
  CORRECCION DECLARADA y el texto viejo entero como prefijo; n NO SE
  MUEVE y sigue en 3.388; assert de frontera con sha256 de dataset/ y
  conteo de censo y aristas antes y despues (el registro cambia, EL GRAFO
  NO); y Gate 0 corrido al terminar.
  (2.e) Y EL LIMITE, QUE SIGUE VIGENTE DESDE LA 6.1 DEL ACTA 155: LA QUE
  SALGA A NO SE VOLTEA. Se marca como discutible, se publica su caso, y
  NO SE EJECUTA NINGUNA FUSION.

- TAREA 3, EL LOTE 2 DEL SACO, POR LA 6.12. Son 53, de LD-OPC05-068 a
  LD-OPC05-121, y NINGUNA trae puntero de paso: el saco pequeno se agoto
  entero en el lote 1. TU INSTRUMENTO RECOMPUTA ESA NOMINA Y LA PUBLICA:
  si no da 53, paras y lo dices antes de leer nada. Mismo criterio de la
  6.4, con la 6.3 puesta desde la primera lectura. Mismas guardas de la
  2.d. Si el lote 2 no cabe entero con sus guardas completas, PARTELO Y
  DILO: mejor medio lote medido que un lote entero prometido.

- TAREA 4, EL CAMPO cita UNIFICADO, POR LA 6.6. Lo medi yo comparando el
  registro de abb2fe4e contra HEAD: ademas de las 62 clases y las 67
  razones, cambiaron 62 campos cita, y cambiaron POR SOBREESCRITURA
  ('LD-OPC05-001, clase C' pasa a 'clase D', sin dejar el texto viejo).
  Pero las tres de la vuelta 156 dicen otra cosa en el mismo fichero
  ('clase C  [RECLASIFICADA A D EN LA VUELTA 156: ver la razon]'). Dos
  formas para el mismo hecho en dos vueltas seguidas, y ademas esas tres
  hoy leen literalmente "clase C" en una fila que es D. Adjudicado: UNA
  SOLA FORMA para las 65 filas corregidas, la que lleva la clase VIGENTE
  y el rastro, 'clase D [ANTES C, RECLASIFICADA EN LA VUELTA N: ver la
  razon]'. Por adicion, con correccion declarada, y con assert de que
  NINGUNA clase se mueve al hacerlo y de que el conteo de pares del
  registro sale identico antes y despues.

- TAREA 5, EL CHECK DE P.16 CENIDO AL CONTENIDO Y A SU PROPIA VENTANA,
  POR LA 6.7, Y NACE DE TU HALLAZGO. Tu docstring dice que comprueba que
  dataset/ y docs/plan/ no se tocan ni una vez, o sea CONTENIDO; el
  instrumento es git status --porcelain, que ademas de contenido ve
  ESTADO DE FIN DE LINEA y ademas ve SUCIEDAD ANTERIOR AL ARRANQUE DEL
  SCRIPT, que no es suya. Dos anclas que se mueven en la misma linea.
  (5.a) EL REMEDIO: huella de CONTENIDO tomada ANTES y DESPUES de las
  mutaciones dentro del propio script, y comparada consigo misma.
  (5.b) EL ALCANCE, MEDIDO POR MI Y RECOMPUTALO TU: once ficheros de
  scripts/loop/ llevan el patron literal, siete de ellos dentro de la
  bateria de las 23. Si tu cuenta no da once, paras y lo dices.
  (5.c) CASO POSITIVO POR MUTACION: si una mutacion escribe de verdad en
  dataset/ o docs/plan/, el check SIGUE SALIENDO ROJO. Y la bateria
  entera se re corre SOLA despues, para ver que las 23 siguen siendo 23.

- TAREA 6, LA GUARDA DE RE SELLADO NO PUEDE ACUSAR A SU PROPIA SALIDA,
  POR LA 6.8, Y ESTO LO ENCONTRE CORRIENDOLA YO. Sobre el reporte en HEAD
  sale ROJO exit 1 acusando SALIDA_V157_T9_CIFRAS_REPORTE.txt y
  SALIDA_V157_T9_RE_SELLADO.txt, y lo verifique con git diff --numstat
  b166ab47 HEAD (2 y 2, y 24 y 22). NO ES CAIDA TUYA y lo digo en el
  acta: el commit que publica el reporte re escribe necesariamente la
  salida de la propia guarda y la del verificador de cifras, asi que
  ningun reporte puede dejarla verde en HEAD. Exigirte una afirmacion que
  expira al commitearla seria exigir lo imposible.
  (6.a) EL REMEDIO: la guarda exime de la comparacion los ficheros que
  ella misma y el verificador de cifras escriben sobre el reporte final,
  o compara contra el commit del reporte en vez de contra HEAD.
  (6.b) Y LA EXENCION SE PUBLICA COMO LINEA COMPUTADA CON LOS NOMBRES
  EXENTOS, no como silencio. Una exencion que no se imprime es un
  agujero.
  (6.c) CASO POSITIVO POR MUTACION: un fichero de tarea normal re sellado
  y no declarado TIENE QUE SEGUIR SALIENDO ROJO.

- TAREA 7, LAS DOS SALIDAS SIN PRODUCTOR, POR LA 6.9. Barriste 998 .py
  por su texto y no hallaste productor de
  SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt ni de SALIDA_V136_3D_MUTACION.txt.
  Falta un angulo barato y decisivo que nadie ha corrido: LA HISTORIA DE
  GIT, porque un productor pudo morir o cambiar de nombre. Busca con
  git log --all -S sobre el texto de cada salida. Si aparece, nombras el
  productor y la ficha lo cita. Si no aparece, la cita queda declarada
  ARTEFACTO HUERFANO junto a la funcion, con esa letra. LA CITA NO SE
  BORRA: SE MARCA.

- TAREA 8, LAS DOS QUE NO MUERDEN, POR LA 6.10. Las corri yo y confirmo
  tu cifra: vuelta96_tarea3_prueba_mutacion.py exit 1 y
  vuelta97_tarea2_prueba_mutacion.py exit 1. LEE EL ROJO ANTES DE TOCAR
  NADA. Si delata una regresion real de la guarda que nombra, es hallazgo
  y lo traes. Si es una expectativa envejecida sobre un sujeto congelado,
  se declara CASO DECLARADO con su motivo escrito y su marca obligatoria,
  como los dos que la bateria ya lleva. LO QUE NO SE HACE ES AJUSTAR LA
  EXPECTATIVA HASTA QUE SALGA VERDE.

  Y LO QUE NO VA: la cuenta de las dos especies de D queda CERRADA por la
  6.11. Tu vara lexica cazo 1 de 5 y dejo 71,9 y 96,6 por ciento en SIN
  MARCA, y publicaste eso en vez de retocar las marcas hasta que saliera,
  que es exactamente lo que se te pidio. La cuenta cumplio su encargo y
  no se repite. No se abre letra nueva (seria doctrina nueva y seria
  parada) y no se encarga una segunda pasada lexica.

- TAREA 9, EL CIERRE RECOMPUTADO AL CIERRE, con el ciclo entero en su
  orden (run_phase1 --reaplico-curaduria, etiquetas_de_cara --aplicar,
  sync_assets_web, y despues el numstat de dataset/ web/ engine/), NUNCA
  run_phase1 suelto, las tres suites (vitest DESDE web/), la cabecera
  tallada y comparada (que esta vez SI puede correr, con --vuelta 159) y
  las guardas del cierre con su estado real aunque no te favorezcan.
  verificar_mutaciones_viejas.py se corre SOLA, SIN NADA AL LADO. Y el
  reporte con la regla que ya funciona: toda cifra que describa una
  salida va PEGADA de la salida.

- Y DESPUES, SEGUIR EL ORDEN ESCRITO EN MODO CONTINUO hasta el MURO
  CONOCIDO Y YA ADJUDICADO (acta 149, 3.10): la fase 08 no cierra sin una
  SESION CON CREDENCIAL Y CON EL FUNDADOR DELANTE. Medida hoy por mi, la
  fase 08 trae una operacion, una sin cumplir, OP-V-01, sin vara escrita.
  Ahi se para y se dice. Y queda dicho lo otro, porque ya se ve: LA UNICA
  DEUDA DE LECTURA QUE LE QUEDA AL BUCLE ES EL SACO (57 en C, mas las 41
  que la 6.5 manda releer), y cuando se vacie no quedara trabajo que un
  bucle pueda hacer solo. EL MERGE NO SE PIDE NI SE HACE: es del fundador
  y solo suyo.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
