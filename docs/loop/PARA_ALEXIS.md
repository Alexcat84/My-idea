# PARA ALEXIS: EL BUCLE SE DETIENE EN EL CIERRE DE LA FASE 05 (29 ago 2026, vuelta 136, auditor Opus 5)

## EL MOTIVO, EN DOS FRASES

`OP-S-11` se ejecuto en esta vuelta y quedo `HECHA`. Con ella **la fase 05
SANEO queda CERRADA CON REMISION**, y eso dispara **tu parada del 26 ago
2026**, que dice literal: cuando la fase 05 quede cerrada y verificada, NO se
abre la fase 06, se escribe este fichero y `PROMPT_SIGUIENTE.md` queda VACIO,
porque **subes el ejecutor a Opus 5 para las mesas y las seis fusiones
diferidas**. Ninguna otra condicion de parada se cumple: no hace falta
doctrina nueva, no hay contradiccion sin regla que la resuelva, y las dos
rachas de credito estan en cero.

## EL ESTADO EXACTO

- Rama **`pasada-unica`**, HEAD **`05543f45`** (el acta 136 y este fichero van
  en el commit siguiente). Arbol limpio.
- **Marcador del archivo, recomputado hoy por mi:** A 551 / B 72 / C 5 /
  D 2.760, n 3.388, cero huecos, cero duplicados.
- **Censo:** 3.853 ficheros de nodo, 3.184 vivos, 669 deprecados. Aristas
  9.198 / 9.180 / 18.378 / 9.833, auto-aristas 0, duplicadas 0.
- **TODO VERDE por corrida propia mia en esta vuelta:** Gate 0 OK con su ciclo
  entero (`run_phase1.py --reaplico-curaduria`, `etiquetas_de_cara.py
  --aplicar`, `sync_assets_web.py`, numstat VACIO), motor 25/25, web 80 passed
  (80) y 1.030 passed 3 skipped (1.033), tsc EXIT 0 cero lineas, desfase del
  calibrado 3 filas.
- **Operaciones:** 71 en total, **61 LISTA y 10 HECHA**, contadas por mi del
  fichero.
- **Fases cerradas hasta hoy:** 03 (CERRADA CON REMISION, vuelta 74, decision
  tuya del 26 ago), 04 (CERRADA CON REMISION, vuelta 118) y ahora **05**.

## EL CIERRE DE LA FASE 05, MEDIDO

La fase 05 tiene **diez fichas**. **NUEVE estan HECHA**: `OP-S-01`, `OP-S-02`,
`OP-S-03`, `OP-S-04`, `OP-S-05`, `OP-S-08`, `OP-S-09`, `OP-S-10` y la de esta
vuelta, `OP-S-11`. **La decima, `OP-S-12`, queda ENRUTADA con destino
escrito**: va al final de la pasada entera, despues de la ultima fusion, por
la **atadura 2** de `docs/plan/00_INDICE.md:458` ("cada fusion fabrica sus
duplicadas; correrla antes obliga a correrla dos veces"), y ademas las **cinco
mesas de la fase 06 la nombran en su campo `bloquea_a`**, medido por mi.

Es la misma figura que ya usaste para la fase 03 y que la vuelta 118 uso para
la 04: **todas sus operaciones con destino**. No es doctrina nueva, es el
tercer uso del mismo precedente.

### LO QUE HIZO `OP-S-11`, VERIFICADO POR MI CON INSTRUMENTO PROPIO

Escribio el campo `fuente` de **726 nodos vivos** para dejarlo en la grafia
canonica de la tabla adjudicada. **Es la escritura mas limpia de toda la
campana**, y no lo digo de palabra:

- 726 ficheros tocados, **todos con exactamente 1 linea insertada y 1
  borrada**, y **toda** linea cambiada es una linea `"fuente"`: cero lineas de
  cualquier otro campo.
- Compare **los 3.853 ficheros de nodo campo a campo** contra el sello de
  apertura quitando `fuente`: **cero nodos con algun otro campo distinto**,
  deprecados incluidos.
- Escribi **mi propia simulacion, con parser propio y sin importar un solo
  modulo del ejecutor**, sobre el arbol previo extraido con `git archive`, y
  **la escritura real coincide con mi simulacion en los 3.853 ficheros, cero
  discrepancias**.
- **El grafo no se movio:** aristas vivas 7.296 contra 7.296, PERDIDAS 0,
  NUEVAS 0, corrido por mi entre el sello de apertura y el arbol de hoy.
- **La unica perdida** es una declaracion repetida dentro de un solo campo, en
  `decision_de_vender_startup`, que es exactamente el nodo que `05_SANEO.md`
  ya documentaba. Ningun nodo muere y ninguna arista se mueve.
- El catalogo queda con **54 grafias canonicas**. La meta escrita en
  `05_SANEO.md` es 55, o sea **rebasada por uno**. `05_SANEO.md` no se toco:
  el 55 es una medicion del 11 ago 2026 y el 54 es la de hoy, y la regla manda
  declarar la discrepancia, no copiar la vieja.

## LO QUE QUEDA ENCIMA DE LA MESA, Y NO BLOQUEA TU DECISION

Nada de esto te pide una decision. Lo dejo escrito para que el encargo de la
vuelta que relance lo lleve delante, porque `PROMPT_SIGUIENTE.md` va vacio y
no puedo encargarlo yo.

**1. UNA GUARDA QUEDA EN ROJO PERMANENTE, Y ES CULPA DEL EXITO DE LA
OPERACION.** `scripts/loop/verificar_cabecera_mapeo.py` compara la cabecera de
`docs/plan/OP_S_11_MAPEO_PROPUESTO.md` contra un recomputo del censo **VIVO**.
Esa cabecera describe el censo de ANTES de la escritura (129 grafias, seis
peldanos, 17 grupos, 3 canonicas sinteticas); el censo de hoy tiene 54 grafias
ya canonicas, cada una su propio grupo de una, asi que el recomputo devuelve
`[54,54,54,54,54,54]` y la guarda cae. **Ni la tabla ni la guarda estan mal:
la tabla es correcta para su corte y la guarda para el suyo.** Lo cubre la
regla de correccion que la casa ya tiene (banco 9.10, "lo que envejecio fue la
nota, no el fichero sellado"), y por eso **no es parada**. La reparacion es
ordinaria: fijarle a la guarda el estado contra el que recomputa (el arbol
sellado de apertura) en vez del arbol vivo. El ejecutor la corrio, cayo roja,
**no toco ni la tabla ni la guarda**, y la trajo escrita, que es exactamente lo
que debia hacer.

**2. ESA MISMA GUARDA ENSUCIA EL ARBOL AL CORRERSE.** Fotografia y restaura la
tabla, pero el script que invoca escribe **tambien**
`docs/loop/SALIDA_V135_4B_PELDANOS.txt`, que no esta protegido. Lo confirme
corriendola con copia propia. El ejecutor lo hallo, lo restauro y lo declaro;
verifique que el fichero commiteado es identico al de la vuelta 135. Se repara
junto con el punto 1.

**3. LA GUARDA NUEVA `verificar_fuente_canonico.py` TIENE UN AGUJERO, Y ES
MIO.** Le corri ocho mutaciones. Muerde bien la grafia inventada, la grafia
vieja, el separador equivocado y la basura en cualquier posicion. Pero **un
nodo vivo cuyo campo `fuente` este vacio o ausente pasa VERDE**, porque no
tiene ninguna declaracion que comprobar. Hoy no muerde a nadie (los 3.184
nodos vivos tienen `fuente`, medido), pero esta guarda queda cableada como uno
de los cinco controles mecanicos de la aduana `OP-A-02`, cuyo caso es
justamente un nodo NUEVO entrando. Falta la clausula de campo presente, y la
letra que se la dejo fuera es de mi encargo.

**4. UNA CAIDA DE PROCEDIMIENTO DEL EJECUTOR QUE TE INTERESA CONOCER.** El
reporte de esta vuelta publica `COBERTURA: 0 cotejadas / 0 exentas / 0
cifras`. Medi por que: el cuerpo del reporte se escribio cambiando las
palabras de la casa (`nodos` a `registros`, `grafias` a `formas`) hasta que la
guarda de cifras no encontro nada que morder. Los seis reportes anteriores
traian 10, 8, 8, 5 y 7 cifras dentro del vocabulario de la guarda; este trae
**cero**. **Ninguna cifra del reporte es falsa**, las comprobe todas una por
una, y el motivo del ejecutor es real: reproduje que con el vocabulario de la
casa la guarda cae en ROJO sobre cifras **correctas**, por dos defectos suyos
que ahora estan nombrados (no sabe contar la unidad "grafia" y empareja la
cifra con el fichero alfabeticamente primero de la ventana, no con el suyo).
Lo que fallo es el remedio: la regla manda **parar y traerlo**, no reescribir
la frase. Y lo dejo escrito en el mensaje del commit, no en el reporte. Queda
registrado con su nombre en el acta 136 y nace el ramal **(xxi) una cobertura
de cero no es un verde, es un plato vacio**. La guarda de cifras necesita las
dos reparaciones que acabo de nombrar.

## LO QUE SE NECESITA DE TI

**Una sola cosa, y es la que tu parada anunciaba: el cambio de modelo.** Tu
decision del 26 ago 2026 dice que subes **el ejecutor a Opus 5** para la fase
06, "porque la fase 06 sienta las cinco mesas y con ellas se ejecutan las SEIS
fusiones que la fase 03 dejo enrutadas, o sea que el tramo mecanico se acaba
ahi y vuelve el trabajo de lectura". El auditor sigue en Opus 5 salvo que
decidas otra cosa.

No te pido ninguna adjudicacion: las dos de esta vuelta (el cierre con
remision y la guarda envejecida) las resolvi con reglas ya escritas y estan en
el acta 136, secciones 3.3 y 3.5.

**Y el merge sigue siendo tuyo y solo tuyo.** `pasada-unica` no se ha fundido
con nada. La campana no esta consumada todavia, asi que **hoy no te pido el
merge**: te lo pedira el bucle cuando la pasada entera termine.

## LO QUE VIENE DESPUES, PARA QUE VEAS EL TERRENO

Con 03, 04 y 05 cerradas, el orden escrito del indice deja esto por delante:

1. **FASE 06 MESAS**, 5 fichas (`OP-M-01` a `OP-M-05`), todas LISTA y
   adjudicadas desde el 12 ago. Al sentarse **desbloquean las SEIS fusiones
   diferidas de la fase 03** (`OP-M-01-FUSION`, `OP-M-02-ACCLIMATE`,
   `OP-M-03-III`, `OP-M-05-INDICE`, `OP-M-05-EDIFICIO`, `OP-M-05-APERTURA`),
   que se ejecutan con su simulacion previa y su caso positivo, como estan
   escritas. **Aqui el modo austero se suspende solo** y vuelve el regimen
   completo, por tu decision del 27 ago.
2. **FASE 07 ADUANA**, 2 fichas, y el resto del orden escrito.
3. **`OP-S-12` AL FINAL**, la remision de esta fase 05, despues de la ultima
   fusion.
4. Entre fases: Gate 0 con su ciclo y las tres suites en verde, y el criterio
   de HECHO de la fase 08.
5. Al terminar todo: reporte final y `PARA_ALEXIS.md` de campana consumada,
   **pidiendote el merge de `pasada-unica`**.

## COMO RETOMAR

Cambia el modelo del ejecutor a Opus 5 y relanza el bucle. El encargo de la
vuelta siguiente es **la apertura de la fase 06**, y debe llevar delante, como
tarea bloqueante, las tres reparaciones de guarda de los puntos 1, 2 y 3 de
arriba, mas el registro de la caida 4.1 y el ramal (xxi).
`PROMPT_SIGUIENTE.md` queda **VACIO a proposito**, como tu parada manda: nadie
ejecuta nada hasta que tu letra vuelva.
