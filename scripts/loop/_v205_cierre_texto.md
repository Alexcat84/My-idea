## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**NINGUNA CELDA DE ESTA SECCION SE TECLEO.** Todas salen de
`scripts/loop/_v205_tallar_tabla_tramos.py 11`, que cuenta los once ficheros de
tramo uno a uno, y su salida cruda vive en `docs/loop/SALIDA_V205_TABLA_TRAMOS.txt`
(BYTES_TABLA_AQUI). `EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO.

### 3.1 EL REPARTO, COMPUTADO DE LA NOMINA DE HOY Y NO TECLEADO DE OTRA VUELTA

Salido de `python scripts/loop/_v205_bateria_en_su_nombre.py --plan`, que lo
computa con `reparto_en_tramos()` sobre `VIEJAS`:

- `CIFRA entradas de la nomina: 135`
- `CIFRA tamano de tramo: 13`
- `CIFRA tramos: 11`
- `CIFRA suma de las entradas de todos los tramos: 135`

**LA NOMINA SIGUE CONGELADA EN 135**, contada del modulo y no del encargo. El
encargo dice 135 y la medicion de hoy dice 135: **calzan**.

### 3.2 EL SELLADO DE LOS ONCE TRAMOS, CONTADO DE SUS FICHEROS

TABLA_TRAMOS_AQUI

### 3.3 LA DOBLE CORRIDA, QUE ES OBLIGATORIA, Y DONDE VIVE

**LA DOBLE CORRIDA NO ES UNA SEGUNDA PASADA DE LA BATERIA: VIVE DENTRO DE ELLA**,
y eso lo comprobe en el codigo antes de decirlo. `verificar_mutaciones_viejas.py`
linea 1710: cada mutacion vieja se corre DOS VECES SEGUIDAS, y linea 1713: si
alguno difiere entre la primera y la segunda corrida, es ROJO nombrandolo. Es el
cotejo de reproducibilidad de la TAREA 2.f de la vuelta 141. Cada salida sellada
lo repite en su propio texto, en su AVISO DE RELOJ: cada entrada se corre DOS
VECES, asi que el tiempo de cada arnes YA INCLUYE sus dos corridas.

**SU RELOJ SE PUBLICA**, y sale de las lineas `DURACION DEL TRAMO (monotona,
minutos)` de los once ficheros, sumadas por el tallador de la tabla. **NO
REPRODUCIBLE sale 0 en los once tramos**, o sea que ninguna de las 135 entradas
difirio entre su primera y su segunda corrida.

### 3.4 EL CENSO Y LA NOMINA, CON VARA Y SIN VARA, LAS DOS CIFRAS JUNTAS

Contadas de `docs/loop/SALIDA_V205_BATERIA_TRAMO_1.txt`, que las trae en su
bloque de cabecera y otra vez recomputadas al cierre del tramo:

| cifra | valor | de que linea del fichero sale |
|---|---:|---|
| arneses que el censo reconoce en `scripts/loop/` | 197 | `CIFRA arneses en scripts/loop/ que el censo reconoce` |
| entradas de la nomina | 135 | `CIFRA entradas en la nomina` |
| entradas de la nomina que el censo NO VE | 0 de 135 | `CIFRA entradas de la nomina que el censo NO VE` |
| arneses del censo fuera de la nomina CON la vara 148 | 2 | `CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA de la nomina` |
| arneses del censo fuera de la nomina SIN vara | 62 | 197 menos 135, y la resta vale porque las 135 estan las 135 dentro de las 197, que es lo que dice la fila de los 0 invisibles |

**LOS DOS ARNESES QUE LA VARA 148 DEJA FUERA, NOMBRADOS OTRA VEZ PORQUE EL
CONGELADO IMPIDE METERLOS Y ESO SE DICE EN VEZ DE CALLARSE:**

- `vuelta197_tarea2_mutacion_orden_del_turno.py`
- `vuelta199_tarea1_mutacion_guardas_revividas.py`

**EL CONTRASTE CON EL ENCARGO, QUE NO ES FUENTE SINO CONTRASTE:** el encargo dice
que al cerrar la 204 daban **2** y **62** sobre un censo de **197**. Mi medicion de
hoy da **2**, **62** y **197**. **Calzan las tres, y estan medidas hoy.**

### 3.5 EL VEREDICTO DE LA BATERIA, Y POR QUE ES ROJO

**LOS ONCE TRAMOS SALEN EN `ROJO POR FALLO` CON `exitcode 1`, Y LA CAUSA ES UNA
SOLA Y ES ESTRUCTURAL.** El desglose que el propio instrumento imprime, en la
linea `CIFRA de FALLO` de cada tramo, es identico en los once:

```
0 con ancla perdida, 0 que no mordieron, 0 sin reproducir, 2 fuera de la nomina, 0 invisibles al censo, 0 SUJETO VIVO
```

**NINGUNA DE LAS 135 ENTRADAS DE LA NOMINA FALLA.** Las 135 muerden, las 135 se
reproducen entre sus dos corridas, ninguna perdio su ancla y ninguna tiene el
sujeto vivo. **Lo unico que enciende el rojo son los DOS arneses que la moratoria
impide meter en la nomina**, y es el mismo rojo que el propio codigo se predijo,
en el comentario de `verificar_mutaciones_viejas.py` que explica por que entraron
seis entradas en la vuelta 195: un rojo permanente y conocido apaga la bateria
sola, porque si siempre esta roja nadie mira el rojo nuevo.

**NO LO SALTO, NO LO AFLOJO Y NO PODO NADA.** Lo declaro con su nombre y su
salida, que es lo que el encargo manda cuando dice que un arnes que falla es
exactamente lo que la bateria existe para encontrar. Aqui hay que decir una cosa
mas, y va como hallazgo: **el que falla no es un arnes DE la nomina, sino la
relacion entre el censo y la nomina**, y eso no lo arregla la bateria.

### 3.6 LOS DOS CASOS DECLARADOS, QUE NO SON FALLOS Y SE NOMBRAN IGUAL

El tramo 1 publica `CASO DECLARADO : 2`, y los dos vienen declarados de vueltas
anteriores con su marca obligatoria dentro de la propia salida sellada:

- `vuelta135_2e_mutacion_3.py`, exit declarado 1, marca `NO TIENE CONVENCION MECANICA DE CONTEO`.
- `vuelta140_2a_mutaciones.py`, exit declarado 2, marca `VEREDICTO (iii): NO CALZA`.

**No los toco y no los cuento como fallo**, porque el instrumento no los cuenta
como fallo: su linea `CIFRA de FALLO` los deja fuera y los publica aparte.

## 4. LO QUE SE TOCO, Y LO QUE NO

NUMSTAT_AQUI

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1`. CORRI LA BATERIA CON UN CONDUCTOR `_v205_*` QUE IMPORTA EL LANZADOR, EN
VEZ DE CLONARLO O DE REUSAR LA SALIDA DE LA 183.** El encargo manda dos cosas que
con el codigo de hoy no pueden valer las dos: que el lanzador no se clone ni se
escriba otro, y que las salidas selladas vayan en el nombre de esta vuelta. Medi
el choque en vez de suponerlo, con sus lineas de codigo delante. Elegi la tercera
puerta: **no clonar, no reusar, e importar**. **Por donde me puedo estar
equivocando:** un fichero nuevo en `scripts/loop/` es un fichero nuevo, y aunque
lleve guion bajo y aunque no anada ni una guarda, alguien puede leer *no se
escribe otro* como *no se escribe NINGUNO*, y entonces la lectura correcta era
declarar la parada y dejar la bateria sin correr por tercera cadencia seguida.
**Yo creo que no**, porque la bateria sin correr es la enfermedad que esta vuelta
existe para curar y porque el propio encargo bendice el carril `_v205_*`; pero
**es del auditor y no mia**, y por eso sube tambien como pregunta.

**`D.2`. EL CICLO DE GATE 0 DE APERTURA LO CORRI TARDE, Y LO DECLARO EN VEZ DE
LLAMARLO APERTURA A SECAS.** No corri el ciclo antes del primer tramo. Lo que
sostiene que la medicion siga siendo la de la apertura es una **medicion, no una
promesa**: `git diff` con `--numstat` contra el HEAD de apertura sobre `dataset/`,
`web/` y `engine/` da **cero filas**, o sea que los tres arboles que el ciclo mide
son byte a byte los de la apertura. **Por donde me puedo estar equivocando:** la
regla dice que la apertura se mide antes de la primera operacion, y no dice *o
despues, si puedes probar que nada se movio*. Si el auditor lee la letra estrecha,
esto es caida y no discutible, y por eso **va tambien en la seccion 8 como caida
mia**, contada una sola vez y con una sola etiqueta.

**`D.3`. DOY LA BATERIA POR CORRIDA AUNQUE LOS ONCE TRAMOS SALGAN EN ROJO.** La
letra dice que la bateria se declara corrida cuando todos los tramos tienen salida
sellada del mismo calibre, y que el calibre lo coteja `--componer`. Corrida y verde
no son la misma cosa: **corrida** es que los once tienen salida sellada, no vacia
y del mismo calibre; **verde** es otra cosa y hoy no lo esta. **Por donde me puedo
estar equivocando:** si por *corrida* se entendia *corrida y en verde*, entonces la
bateria de la 205 no cuenta y la cadencia sigue rota, con la diferencia de que
ahora **se sabe por que**, con nombre y apellido de los dos arneses.

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1`. EL CHOQUE DE LA `D.1` NECESITA LETRA, PORQUE VUELVE CADA CINCO VUELTAS.**
Con la moratoria vigente y el lanzador computando su vuelta del nombre del
fichero, **cada vuelta de bateria se topara con lo mismo**. Tres salidas posibles,
y ninguna la decido yo: (a) el carril `_v205_*` que use hoy queda bendecido por
escrito para las vueltas de bateria; (b) se autoriza, como excepcion nombrada de
la moratoria, cambiar el lanzador para que acepte una opcion de vuelta; (c) se
acepta que las salidas lleven el numero del lanzador y se cambia la letra de
`AUDITOR.md` 6.1 y la pieza (4) de `cerrar_reporte.py`, que hoy la rechazan.

**`P.2`. EL ROJO ESTRUCTURAL DE LOS DOS ARNESES NO LO PUEDE RESOLVER EL EJECUTOR.**
La regla escrita desde la vuelta 148 dice que un arnes del censo entra en la
nomina; la moratoria del 7 sep dice que la nomina queda congelada en 135. **Las
dos son vigentes y se contradicen sobre estos dos ficheros.** Mientras no se
resuelva, **la bateria sale roja todas las vueltas por la misma causa**, que es
justo lo que el propio codigo avisa que apaga una bateria.

## 7. PENDIENTES DE DOCTRINA

**`PD.1`.** Que cuenta como *clonar* bajo la moratoria: un fichero que **importa**
un instrumento y le corrige un dato, sin copiar ni una linea suya, no esta escrito
en ningun sitio como permitido ni como prohibido. **Registro lo mejor sostenido y
sigo**, que es lo que `EJECUTOR.md` 5 manda cuando falta regla.

**`PD.2`.** La `PD.3` de la 204, que pregunta que hacer cuando dos secciones
titulan el mismo numeral, **sigue sin resolver** y esta vuelta no la toca. La cito
para que no se pierda, con su sede: adjudicacion `4.7` del acta 204.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE

**`C.1`. NO CORRI EL CICLO DE GATE 0 DE APERTURA ANTES DE LA PRIMERA OPERACION**, y
el sello `docs/loop/SALIDA_V205_HEAD_APERTURA.txt` nacio con la bateria ya
corriendo. **El tallador lo dice solo y no se lo tapo**: su fila de identidad
publica el sello como RECONSTRUIDO DESPUES, y esa es la celda que va en la
cabecera. Lo que si medi antes de la primera operacion, y esta copiado en el
bloque A del sello con esa advertencia escrita encima, son el HEAD, la rama, el
estado del arbol y los dos `sha256` de las sedes selladas. **Es la misma caida que
la `D.2` y por eso se cuenta UNA VEZ**, aqui, con una sola etiqueta, que es la
leccion que el acta 204 me deja escrita.

**`C.2`. MATE EL TRAMO 3 A MITAD POR LANZARLO CONTRA UN TOPE DE DIEZ MINUTOS QUE
NO LE ALCANZABA**, y lo dejo dicho porque dejo rastro medible: al morir, `dataset/`
quedo sucio en **1 fichero**, `dataset/metadata/master_graph.json`, contado con
`git diff --numstat -- dataset/`. **No lo arregle yo a mano**: la guarda del propio
lanzador lo restauro con `git checkout --` al entrar al tramo siguiente y lo
remidio en cero, y eso queda dentro de la salida sellada de ese tramo. El remedio
fue lanzar el resto en corrida de fondo, sin tope. **La caida es mia, la guarda
funciono, y el tramo 3 que cuenta es el que si termino.**

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**PROPONER ES MIO Y ENCARGAR ES DEL AUDITOR.** No escribo `PROMPT_SIGUIENTE.md`,
`ACTA_AUDITOR.md` ni `PARA_ALEXIS.md`, y el `numstat` de las tres contra mi HEAD de
apertura lo publico en la seccion 4.

1. **LA DEUDA DE REGISTROS SIGUE EN 2**, actas **179** y **180**, tal como el
   encargo de esta vuelta la dejo escrita. La 206 la arrastra.
2. **LA OPERACION DE CODIGO DE LA ESCALADA SIGUE ENCARGADA Y SUSPENDIDA** (acta 202
   `4.6`, ratificada por el `4.9` de la 203 y el `4.10` de la 204): se ejecuta en la
   primera vuelta despues de que la moratoria se levante. **La arrastro aqui otra
   vez para que la 206 no la pierda**, que es exactamente lo que el encargo me pide.
3. **LA `P.1` Y LA `P.2` DE ARRIBA PIDEN LETRA DEL FUNDADOR**, no del ejecutor. La
   `P.2` es la mas cara: mientras dure, **cada vuelta de bateria sale roja por la
   misma causa conocida**, y un rojo permanente apaga la bateria sola.
4. **EL PATRON DE `preguntas_del_reporte()` SIGUE ROTO Y HOY NO SE TOCA** (acta 204
   `4.4`): `scripts/loop/_v203_reparto_de_actas_viejas.py` linea 196, el articulo
   `LAS` le rompe la coincidencia. Va a la integral, ya nombrado.
5. **LA CORRECCION DECLARADA DE `R.67` Y `R.68` ES DE LA 206** (acta 204 `4.3`), por
   el carril del banco `9.10`, por adicion y en su sede.
