# EL RECOMPUTO DE LA FASE II, corte 3.388

> ## CORRECCION DECLARADA DEL 15 ago 2026 (vuelta 33), Y ES DE LAS QUE MUEVEN CIFRAS DE ESTE DOCUMENTO ENTERO
>
> **TRES VEREDICTOS SE VOLTEARON EL 15 ago 2026** por el banco `9.10`, con la adjudicacion del
> fundador, tras el destejido del emblema `producto_minimo_viable` (`OP-D-01` movimiento 1,
> vuelta 32): **494 de `A` a `C`**, **592 de `B` a `D`** y **830 de `B` a `D`**.
>
> **EL CORTE NO SE MUEVE: `n` sigue en 3.388.** Lo que se mueve es el reparto de clases, y con el
> **el retrato de las A de este recomputo**, porque el **494** era una `A` y su desaparicion
> **cierra una componente entera** del cierre transitivo: la de `principio_calidad_mvp` con
> `producto_minimo_viable`, de tamano 2, con una sola arista `A` interna.
>
> **EL DOCUMENTO NO SE REESCRIBE POR DENTRO Y SE DICE POR QUE:** sus cifras son el resultado de
> una corrida del 13 ago 2026 y **reescribirlas una a una fabricaria una corrida que nunca
> existio**. Lo que se hace es lo que el `9.10` pide de verdad: **se vuelve a correr el
> instrumento** y se publica el delta entero, aqui arriba, donde se lee antes que el cuerpo.
>
> **Comando, corrido en esta vuelta** (el mismo de siempre, sin tocar):
>
> ```
> python scripts/plan/recomputo_3388.py
> ```
>
> salida entera en `docs/loop/SALIDA_V33_RECOMPUTO_3388.txt`. **El instrumento reescribio ademas
> su propio fichero de detalle `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`**, que es una tabla
> derivada y por tanto entra de lleno en el `9.10`.
>
> | cifra | 13 ago 2026 (cuerpo de este documento) | 15 ago 2026 (recorrido hoy) | delta |
> |---|---:|---:|---:|
> | A crudas en el archivo | **583** | ~~**582**~~ **581** al cierre de la vuelta 34 | **menos 2** |
> | pares distintos del retrato tras resolver | **583** | **582** | **menos 1** |
> | colapsos a auto arista al resolver | 0 | **0** | sin cambio |
> | nodos con al menos una A | **854** | **852** | **menos 2** |
> | componentes de tamano 2 o mas (actos) | **335** | **334** | **menos 1** |
> | componentes CERRADAS | **280** sobre **600** nodos | **279** sobre **598** | **menos 1 y menos 2** |
> | componentes ABIERTAS | **55** sobre **254** nodos | **55** sobre **254** | **sin cambio** |
> | componentes de tamano 2 | **244** | **243** | **menos 1** |
>
> **LAS CUATRO COMPROBACIONES DEL `08_VERIFICACION.md` VUELVEN A DAR OK, las cuatro, con las
> cifras nuevas:** nodos en actos 852 igual a la suma de tamanos; A vigentes resueltas 582 igual a
> la suma de aristas A internas; todo acto cerrado con sus pares internos leidos; cero nodos
> deprecados dentro de una componente.
>
> **LO QUE ESTA CORRECCION NO TOCA, dicho para que nadie le atribuya alcance de mas:** el **592**
> y el **830** eran `B` y pasan a `D`, y **ninguna de las dos clases entra en el retrato de las
> A**, asi que **de las tres, la unica que mueve este documento es la del 494**. Las componentes
> ABIERTAS no cambian ni en numero ni en nodos: la que murio estaba CERRADA.
>
> **Y UNA CIFRA DEL CUERPO QUE ESTA CORRECCION ARRASTRA SIN RECOMPUTARLA:** el documento cita en
> varios sitios **335 actos** contra los 221 del inventario de `OP-I-01`. **Hoy son 334**, y el
> desfase del inventario **sigue siendo un pendiente de doctrina abierto**, no algo que esta
> correccion cierre.
>
> ## SEGUNDA CORRECCION DEL MISMO DIA: **LA PRIMERA FUSION DEL PLAN SE EJECUTO, Y ESTE DOCUMENTO DECIA QUE NO**
>
> **El 15 ago 2026, la misma vuelta 33, ejecuto la FUSION de `OP-D-02`:
> `voz_del_cliente_voc` absorbe a `enfoque_mercado_voc`.** Es **la primera fusion del plan de la
> pasada unica escrita contra `dataset/`**, y por eso mueve este documento por un camino distinto
> al del volteo: **no cambia ninguna clase, cambia el RESOLUTOR.**
>
> **LA FRASE DEL CUERPO QUE ENVEJECIO, y va tachada abajo en su sitio:** el paso 1 decia *ninguna
> de las 583 A colapsa* y lo sostenia en que *ninguna fusion del plan de la pasada unica se ha
> ejecutado contra `dataset/`*. **Eso era verdad el 13 ago y dejo de serlo el 15.**
>
> **AHORA COLAPSA UNA, Y EL INSTRUMENTO LA NOMBRA:** `puesto 386: enfoque_mercado_voc <->
> voz_del_cliente_voc (resuelven al mismo id)`. Al quedar el absorbido como alias del
> superviviente, **el par 386 se vuelve una auto arista y sale del retrato.**
>
> **Y EN LA MISMA VUELTA, UN SEGUNDO VOLTEO POR EL `9.10`:** con el superviviente ya estable, los
> TRES congelados que `voz_del_cliente_voc` bloqueaba se releyeron por el banco `9.4` y pasaron de
> `B` a `D`: **724**, **755** y **827**. **Ese volteo NO toca este documento**, y se dice por que:
> **`B` y `D` no entran en el retrato de las A**, que es lo unico que el recomputo mira.
>
> **Comando, corrido otra vez al cierre** (salida `docs/loop/SALIDA_V33_RECOMPUTO_3388_B.txt`),
> con el fichero de componentes reescrito de nuevo por el propio instrumento:
>
> | cifra | 13 ago | 15 ago, tras el volteo | 15 ago, tras la FUSION | delta total |
> |---|---:|---:|---:|---:|
> | A crudas en el archivo | **583** | **582** | **582** | **menos 1** |
> | colapsos a auto arista al resolver | **0** | **0** | **1** | **mas 1** |
> | pares distintos del retrato | **583** | **582** | **581** | **menos 2** |
> | nodos con al menos una A | **854** | **852** | **851** | **menos 3** |
> | componentes de tamano 2 o mas | **335** | **334** | **334** | **menos 1** |
> | componentes CERRADAS | **280** sobre **600** | **279** sobre **598** | **279** sobre **598** | **menos 1 y menos 2** |
> | componentes ABIERTAS | **55** sobre **254** | **55** sobre **254** | **55** sobre **253** | **menos 1 nodo** |
>
> **LAS CUATRO COMPROBACIONES VUELVEN A DAR OK, las cuatro**, con las cifras nuevas: nodos en
> actos **851** igual a la suma de tamanos; A vigentes resueltas **581** igual a la suma de
> aristas A internas; todo acto cerrado con sus pares internos leidos; y **cero nodos deprecados
> dentro de una componente**, que es justo la comprobacion que una fusion podria haber roto y no
> rompio.
>
> **EL MARCADOR AL CIERRE DE LA VUELTA 33**, medido tras los dos volteos: **n 3.388, A 582, B 84,
> C 8, D 2.714**. `core` pasa de `A 344, B 87, C 7, D 1.007` a **`A 343, B 82, C 8, D 1.012`**, y
> los otros nueve dominios quedan identicos al digito.

> **TERCER VOLTEO, VUELTA 34 (15 ago 2026), y este SI toca este documento**, porque una de las dos
> clases volteadas era `A`. Tras el destejido de `ab_testing_optimizacion` (`OP-D-03`, de diez
> pasos a cinco), el **1061** paso de `A` a `D` y el **738** de `B` a `D`.
>
> **Comando corrido otra vez** (`python scripts/plan/recomputo_3388.py`, salida
> `docs/loop/SALIDA_V34_RECOMPUTO_3388.txt`), con el fichero de componentes **reescrito por el
> propio instrumento**:
>
> | cifra | al cierre de la vuelta 33 | **al cierre de la vuelta 34** | delta |
> |---|---:|---:|---:|
> | A crudas en el archivo | **582** | **581** | **menos 1** |
> | pares distintos del retrato | **581** | **580** | **menos 1** |
> | nodos con al menos una A | **851** | **851** | **quieto** |
> | componentes de tamano 2 o mas | **334** | **335** | **mas 1** |
> | componentes CERRADAS | **279** sobre **598** | **281** sobre **604** | **mas 2 y mas 6** |
> | componentes ABIERTAS | **55** sobre **253** | **54** sobre **247** | **menos 1 y menos 6** |
>
> **LA CIFRA QUE HAY QUE EXPLICAR, y no se pasa por alto: los actos SUBEN de 334 a 335 quitando
> una `A`.** No es una contradiccion: **el 1061 era la arista que unia a `optimizacion_embudo_get_
> customers` (y con el a `funnel_get_customers_optimizacion`) con el resto del acto de las pruebas
> A/B**. Al caer, **una componente se PARTE EN DOS**, y las dos mitades quedan **CERRADAS**,
> porque ninguna de las dos tiene ya pares internos sin leer. **Un acto menos abierto y un acto
> mas de cuenta.**
>
> **LAS CUATRO COMPROBACIONES VUELVEN A DAR OK, las cuatro**, con las cifras nuevas: nodos en
> actos **851** igual a la suma de tamanos; A vigentes resueltas **580** igual a la suma de
> aristas A internas; todo acto cerrado con sus pares internos leidos; y **cero nodos deprecados
> dentro de una componente**.
>
> **EL MARCADOR AL CIERRE DE LA VUELTA 34:** **n 3.388, A 581, B 83, C 8, D 2.716**. `core` pasa
> de `A 343, B 82, C 8, D 1.012` a **`A 342, B 81, C 8, D 1.014`**, y **los otros nueve dominios
> quedan identicos al digito** (`docs/loop/SALIDA_V34_TASA_DOMINIO.txt`).

> ### TERCERA CORRECCION DECLARADA (18 ago 2026, vuelta 36): **`P.5` QUITA CINCO `A` DE GOLPE Y UN ACTO ENTERO DESAPARECE**
>
> **Y esta vez el disparador no es una cirugia, es una RELECTURA.** La vuelta 35 midio que **cinco
> de los seis pares `A` del acto de `OP-D-03`** se habian emitido contra texto que las cirugias de
> la fase 01 y de la propia operacion ya se habian llevado; escribio las cinco relecturas, las
> sello y **paro sin volcarlas** (regla 5 de `docs/loop/EJECUTOR.md`). El fundador las adjudico el
> 15 ago 2026 y esta vuelta las volco: **277, 374, 452, 1571 y 1575, los cinco de `A` a `D`.**
>
> **Comando corrido otra vez** (`python scripts/plan/recomputo_3388.py`, salida
> `docs/loop/SALIDA_V36_RECOMPUTO_3388.txt`), con el fichero de componentes **reescrito por el
> propio instrumento**:
>
> | cifra | al cierre de la vuelta 34 | **al cierre de la vuelta 36** | delta |
> |---|---:|---:|---:|
> | A crudas en el archivo | **581** | **576** | **menos 5** |
> | colapsos a auto arista al resolver | **1** | **1** | sin cambio |
> | pares distintos del retrato | **580** | **575** | **menos 5** |
> | nodos con al menos una A | **851** | **847** | **menos 4** |
> | componentes de tamano 2 o mas (actos) | **335** | **334** | **menos 1** |
> | componentes CERRADAS | **281** sobre **604** | **280** sobre **600** | **menos 1 y menos 4** |
> | componentes ABIERTAS | **54** sobre **247** | **54** sobre **247** | **sin cambio** |
> | CERRADAS de tamano 2 | **243** | **244** | **mas 1** |
>
> **LAS DOS CIFRAS QUE HAY QUE EXPLICAR, y ninguna se pasa por alto.**
>
> **Primera: cinco `A` menos quitan solo CUATRO nodos del cierre transitivo.** No es un descuadre:
> los seis nodos del acto pierden cinco de sus seis aristas internas, y el `643`
> (`split_testing` contra `test_ab_precio`) **sigue siendo `A`**, asi que esos dos nodos siguen
> dentro y solo salen los otros cuatro (`ab_testing_optimizacion`,
> `funnel_get_customers_optimizacion`, `optimizacion_embudo_get_customers`,
> `split_testing_experimentos_ab`).
>
> **Segunda: los actos bajan de 335 a 334 quitando cinco `A`, y la vuelta 34 los habia SUBIDO
> quitando una.** Tampoco es contradiccion, y es la misma figura vista desde el otro lado. La
> vuelta 34 corto la arista que unia dos mitades y **una componente se partio en dos**. Esta
> vuelta corta las demas: **la mitad del embudo (`funnel` contra `optimizacion_embudo`) se queda
> sin ninguna `A` y DESAPARECE del censo de actos**, mientras la mitad de las pruebas A/B
> **encoge de cuatro nodos a dos** y sigue cerrada. Un acto menos, cuatro nodos menos, y una
> componente de tamano 2 mas.
>
> **LAS CUATRO COMPROBACIONES DEL `08_VERIFICACION.md` VUELVEN A DAR OK, las cuatro**, con las
> cifras nuevas: nodos en actos **847** igual a la suma de tamanos; A vigentes resueltas **575**
> igual a la suma de aristas A internas; todo acto cerrado con sus pares internos leidos; y **cero
> nodos deprecados dentro de una componente**.
>
> **EL MARCADOR TRAS EL PRIMER VOLTEO DE LA VUELTA 36:** **n 3.388, A 576, B 83, C 8, D 2.721**.
> `core` pasa de `A 342, B 81, C 8, D 1.014` a **`A 337, B 81, C 8, D 1.019`**, y **los otros nueve
> dominios quedan identicos al digito** (`docs/loop/SALIDA_V36_TASA_DOMINIO.txt`).

> ### CUARTA CORRECCION DECLARADA (18 ago 2026, MISMA vuelta 36 unas horas despues): **EL `643`, Y CON EL EL ACTO ENTERO SE VA**
>
> **Y ESTA CORRECCION CORRIGE A LA DE ARRIBA, ESCRITA POR MI MISMO HACE UN RATO.** Se escribe
> aparte y no se funde con ella **a proposito**: son dos volteos de especie distinta y mezclarlos
> borraria la diferencia. **Los cinco de arriba se voltearon porque el texto habia cambiado bajo el
> veredicto. El `643` no: sus dos nodos no cambiaron una coma**, y su razon vieja describe el texto
> de hoy con exactitud. **Lo que cambio aqui es el criterio, y va dicho por lo que es.**
>
> **Es la lectura dirigida `LD-82`**, el ultimo par sin releer del acto de `OP-D-03`, leido por el
> mandato de `P.5` de leer el acto ENTERO antes de fundirlo, con la decision del fundador del 15
> ago 2026 detras. **`643`, `split_testing` contra `test_ab_precio`, de `A` a `D`.**
>
> **Comando corrido por TERCERA vez en el dia** (`python scripts/plan/recomputo_3388.py`, salida
> `docs/loop/SALIDA_V36_RECOMPUTO_3388_B.txt`), con el fichero de componentes **reescrito otra vez
> por el propio instrumento**:
>
> | cifra | tras el primer volteo de la vuelta 36 | **al cierre de la vuelta 36** | delta |
> |---|---:|---:|---:|
> | A crudas en el archivo | **576** | **575** | **menos 1** |
> | colapsos a auto arista al resolver | **1** | **1** | sin cambio |
> | pares distintos del retrato | **575** | **574** | **menos 1** |
> | nodos con al menos una A | **847** | **845** | **menos 2** |
> | componentes de tamano 2 o mas (actos) | **334** | **333** | **menos 1** |
> | componentes CERRADAS | **280** sobre **600** | **279** sobre **598** | **menos 1 y menos 2** |
> | componentes ABIERTAS | **54** sobre **247** | **54** sobre **247** | **sin cambio** |
> | CERRADAS de tamano 2 | **244** | **243** | **menos 1** |
>
> **EL ACTO DE `OP-D-03` HA DESAPARECIDO ENTERO DEL CENSO.** Quitar la ultima `A` de una componente
> de dos **no la encoge: la borra**, porque una componente se define por sus aristas y esa era la
> unica. Los **seis** nodos del acto estan hoy fuera del cierre transitivo: cuatro salieron con el
> primer volteo y los dos ultimos (`split_testing` y `test_ab_precio`) con este.
>
> **LAS CUATRO COMPROBACIONES DEL `08_VERIFICACION.md` VUELVEN A DAR OK, las cuatro**: nodos en
> actos **845** igual a la suma de tamanos; A vigentes resueltas **574** igual a la suma de aristas
> A internas; todo acto cerrado con sus pares internos leidos; y **cero nodos deprecados dentro de
> una componente**.
>
> **EL MARCADOR AL CIERRE DE LA VUELTA 36:** **n 3.388, A 575, B 83, C 8, D 2.722**. `core` pasa
> de `A 337, B 81, C 8, D 1.019` a **`A 336, B 81, C 8, D 1.020`**, y **los otros nueve dominios
> quedan identicos al digito** (`docs/loop/SALIDA_V36_TASA_DOMINIO_B.txt`).

**Vuelta 11 del bucle (Sonnet 5), 13 ago 2026. Disparador cumplido: el cribado intra-dominio
llego al puesto 3.388 (banco 9.21, `OP-U-02`).** Es la unica recomputacion general del plan.

**INSTRUMENTO, de solo lectura, autorizado esta vuelta:** `scripts/plan/recomputo_3388.py`. No
escribe ni un nodo, ni un veredicto, ni una operacion. Modelado sobre `scripts/plan/nominas.py`
(el `comp()` de componentes) y sobre el `res()` de `scripts/volcar_pares.py` (el resolutor de
alias, misma semantica que `resolverId` del motor).

**REGLA P.1 DEL BANCO DEL PLAN aplicada en los cuatro pasos: todo conteo que toque ids resuelve
antes de contar.** El grafo tiene hoy 3.835 nodos, 314 deprecados, 391 entradas de alias (77
huerfanas, 314 a nodo deprecado, 0 colisiones vivas, cifras de `CORRECCIONES_A_APLICAR.md`
CORRECCION 3, sin cambio).

**LO QUE ESTE DOCUMENTO NO HACE:** no cambia el estado de ninguna operacion.
`docs/plan/OPERACIONES.jsonl` no se toco esta vuelta. `OP-U-02` sigue en DECISION PENDIENTE hasta
que el auditor verifique las cuatro comprobaciones de mas abajo.

---

## PASO 1. EL RETRATO DE LAS A

**Comando:** `python scripts/plan/recomputo_3388.py` (paso 1 de su salida).

| | |
|---|---:|
| A crudas en el archivo (`clase == 'A'`), corte 3.388 | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ ~~**573**~~ **571** **[CORREGIDA SIETE VECES, el 15 y el 18 ago 2026 y el 19 ago 2026; la SEPTIMA al CIERRE de la vuelta 50, por los dos volteos de `P.16` (puestos 2222 y 2226) que la fusion del acto 1 obligo; la sexta el 19 ago 2026 en la vuelta 50, porque el volteo del puesto **305** de `A` a `D` (la limpieza `P.16` de la colision que la fusion del acto 1 fabrico, vuelta 49) MOVIO ESTA TABLA Y LA TABLA NO SE BARRIO EN AQUEL ACTO. Medido hoy con `python scripts/plan/recomputo_3388.py` (`../loop/SALIDA_V50_RECOMPUTO_APERTURA.txt`, paso 1)]** |
| de esas, colapsan a auto-arista al resolver (mismo nodo vivo en los dos lados) | ~~**0**~~ ~~**1**~~ ~~**41**~~ ~~**48**~~ **49** **[CORREGIDA CUATRO VECES, el 15 ago 2026 y el 19 ago 2026 (vueltas 49 y 50). Y NINGUNA DE LAS DOS ULTIMAS ES UN ERROR DE LECTURA: ES LA HUELLA DE LA CIRUGIA, que la propia fila ya explicaba. Cada acto que se funde convierte su par `A` en un par cuyos dos ids resuelven al mismo nodo vivo. El 41 era el corte de la TAREA 1.3 de la vuelta 49, ANTERIOR a las tres fusiones de su TAREA 2 (actos 20, 34 y la parte A del acto 1), que anadieron siete; las 48 estan impresas una a una por el instrumento en `../loop/SALIDA_V50_RECOMPUTO_APERTURA.txt`]** |
| pares distintos en el retrato tras resolver y deduplicar | ~~**583**~~ ~~**582**~~ ~~**580**~~ ~~**575**~~ ~~**574**~~ ~~**533**~~ ~~**525**~~ **522** **[CORREGIDA SIETE VECES, las dos ultimas el 19 ago 2026 (vuelta 50, una en la TAREA 1.1 y otra al CIERRE tras fundir), por el mismo motivo que las dos filas de arriba]** |
| pares con mas de un veredicto crudo apuntando al mismo par resuelto | **0** |

~~**Ninguna de las 583 A colapsa.** Los 391 alias vigentes hoy son historia previa a esta campana
(ninguna fusion del plan de la pasada unica se ha ejecutado contra `dataset/`: verificado que
`nafta_free_trade_agreements`, el ejemplar de `OP-S-01`, sigue sin `deprecado`), asi que resolver
no fusiona ningun par de las 583 A en si mismo. **El retrato de las A vigentes al cierre, corte
3.388, es de 583 pares distintos.**~~

> **CORRECCION DECLARADA (15 ago 2026, vuelta 33). EL PARRAFO DE ARRIBA ERA CIERTO EL 13 ago Y
> DEJO DE SERLO EL 15**, y no por una relectura: **porque se ejecuto la primera fusion del plan**
> (`OP-D-02`, `voz_del_cliente_voc` absorbe a `enfoque_mercado_voc`). **AHORA COLAPSA UNA**, y el
> propio instrumento la nombra al correrlo: *puesto 386: `enfoque_mercado_voc` con
> `voz_del_cliente_voc` (resuelven al mismo id)*. **El retrato pasa de 582 A crudas a 581 pares
> distintos.** La comprobacion de `nafta_free_trade_agreements` sigue siendo cierta y no se toca:
> lo que cambio no es esa, es que **ya hay una fusion ejecutada que aquel dia no habia.**

**COMPROBACION CRUZADA con la evidencia vieja:** las A con `puesto_intra <= 2117`, resueltas y
deduplicadas, dan **401** pares, contra las **400 A vigentes al puesto 2117** citadas como
evidencia de `OP-U-01`. ~~**Diferencia de una unidad, no investigada: fuera del alcance de este
recomputo** (la evidencia vieja no publica su comando ni su lista, asi que no hay con que
diferenciar). Se deja escrita como pregunta abierta, no como discrepancia que pare la vuelta:
ninguna cifra publicada con corte se contradice, la vieja no trae instrumento reproducible con el
que comparar par por par.~~

**CORRECCION DECLARADA (vuelta 12, auditor Opus 5, verificada por el ejecutor con instrumento
propio antes de escribirse): la diferencia de una unidad ESTA RESUELTA, PAR POR PAR, Y NO ES UNA
CONTRADICCION.** El repositorio guarda el archivo al corte exacto (`git show
c16a24f5:docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, 11 ago 2026, 2.117 lineas). Comparado clase a clase
contra el archivo de hoy en ese mismo tramo (2.117 primeras lineas): **cambia UNA sola clase, el
puesto 2.078** (`elaboracion_fdd` contra `preparar_fdd`, dominio `franquicias`), **D el 11 ago 2026
y A hoy por correccion posterior declarada**. El archivo viejo tiene exactamente **400 A**. **No
hay descuadre: hay una correccion declarada, y cada cifra es correcta en su corte** (banco 9.21,
"toda cifra de cruce lleva su fecha de corte"). Verificado por el ejecutor con un script propio de
comparacion linea a linea contra el blob del commit `c16a24f5`: un solo cambio de clase en las
2.117 lineas, exactamente el 2.078, exactamente D a A.

---

## PASO 2. EL BARRIDO DE CONFIRMADAS CONTRA LAS A

~~**NO CORRIDO.**

**LA BUSQUEDA, tal como pide el encargo, empezando por los dos ficheros senalados:**

- `docs/plan/01_FUENTES.md`, linea 53 (tabla de la aritmetica de los 18) y linea 62 (la nota que
  distingue los dos numeros de Hugos): **la cifra 11 aparece dos veces, siempre como CONTEO**
  ("11 son costuras confirmadas con pegado de Hugos"), nunca como nomina.
- `docs/plan/CORRECCIONES_A_APLICAR.md`, lineas 169-174 (CORRECCION 4): **misma cifra, mismo
  tratamiento**, conteo sin lista.
- Busqueda ampliada sobre `docs/` completo (`grep -rn "costuras confirmadas"`,
  `"confirmadas de rebote"`): `docs/COSTURAS_INTERNAS_RESUMEN.md` secciones 6 y 7 y
  `docs/FICHA_SUBFUSION_GRADIENTE.md` (marcador de la clase, `~3400-3430`) **repiten el total de
  46 costuras confirmadas (45 nucleo + 1 `quality`) sin nomina**. `docs/GRADIENTE_VEREDICTOS.md`
  tiene una familia con nombre parecido, **"costuras confirmadas DE REBOTE"** (6 casos, esos si
  nombrados: `ratios_eficiencia_inventario`, `plan_mejora_procesos`, `economia_circular`,
  `propuesta_gasto_capital`, y dos mas), **pero es OTRO UNIVERSO**: verificaciones post-cirugia de
  la cola del gradiente semantico, no la nomina de las 46 confirmadas del cierre de costuras
  internas que este paso 2 necesita.

**RESULTADO: la nomina de las 11 (ni la de las 46) no esta escrita como lista en ningun sitio del
repositorio.** Por la instruccion del encargo, **el paso 2 NO SE CORRE**: no se inventa ni se
reconstruye de memoria. Queda declarado como pendiente para quien tenga a mano la nomina original
del cierre de costuras (probablemente en una sesion de trabajo que no dejo el listado en disco).~~

**CORRECCION DECLARADA (vuelta 12, adjudicacion del auditor: el paso 2 se puede correr sin
inventar nomina, por la VIA ACOTADA). El paso pasa de NO CORRIDO A CORRIDO.**

**LO QUE FALTABA NO ERA LA NOMINA DE LAS 46: era el archivo de salida del propio instrumento.**
`docs/COSTURAS_INTERNAS.jsonl` existe, 128 filas con `node_id`, `dominio`, `pasos`, `corte`,
`disparo_bloque` y `disparo_pareja` (verificado: 128 filas, campos exactos). No trae el veredicto,
asi que la nomina de las confirmadas no esta ahi como dato directo; pero el paso 2 no necesita la
nomina entera, solo necesita saber que citas caen dentro del retrato de las A.

**1. Cruce de las 128 citas (resueltas por alias, P.1) contra los 854 nodos con al menos una A del
paso 1 y 3.** Comando: recorrer `docs/COSTURAS_INTERNAS.jsonl`, resolver cada `node_id` por alias,
y comparar contra el conjunto de nodos del paso 3. **Verificado por el ejecutor: la interseccion es
de TREINTA Y SEIS nodos**, exacto contra la cifra del auditor. Las 128 citas resuelven a 128 nodos
distintos (cero colisiones por alias en este universo), y de esos, 36 tienen al menos una A vigente
al corte 3.388.

**2. Para esos treinta y seis, y solo esos, el veredicto YA ESCRITO**, buscado en
`docs/FICHA_SUBFUSION_GRADIENTE.md`. **Los treinta y seis, sin excepcion, aparecen en la tabla
reconciliada de esa ficha** (lineas 3651 a 3780, "Las 128, con su fila y su veredicto", la misma que
declara "cada una de las 128 citas leidas vive en exactamente una fila"): **36 de 36 tienen
veredicto escrito, cero SIN VEREDICTO ESCRITO.** Ningun nodo se leyo de nuevo ni se adivino desde el
texto: los 36 veredictos son copia literal de esa tabla, citados linea por linea.

| clase | cuantos | nodos, con su linea en FICHA_SUBFUSION_GRADIENTE.md |
|---|---:|---|
| **CONFIRMADA** | **15** | `ab_testing_optimizacion` (3660), `blueprint_de_experiencia` (3671), `brainstorming_divergente` (3766), `customer_journey_mapping` (3693), `future_scenarios_planning` (3676), `key_partners_hypothesis` (3663), `optimizacion_embudo_get_customers` (3775), `plan_de_adquisicion_acquire` (3697), `principio_calidad_mvp` (3686), `producto_minimo_viable` (3653), `producto_unico_superior` (3773), `propuesta_gasto_capital` (3776), `seleccion_ceo_fundador` (3743), `split_testing_experimentos_ab` (3664), `voz_del_cliente_voc` (3672) |
| **FALSA** | **21** | `captura_conocimiento_mercado` (3769), `control_estadistico_de_procesos` (3717), `criterios_equity_split` (3700), `design_for_six_sigma_dfss` (3710), `dso_dpo_gestion_capital_trabajo` (3777), `evaluacion_riesgo_calidad_organizacional` (3723), `eventos_offline_como_canal_traccion` (3764), `export_administration_regulations` (3716), `ferias_comerciales_franquicia` (3740), `founder_ceo_succession_process` (3665), `funcion_protect_politica_seguridad` (3724), `getting_started_maintenance` (3720), `metricas_accionables` (3741), `mix_ubicaciones_corporativas_franquicia` (3666), `modelo_spin_preguntas` (3747), `portfolio_management` (3767), `regalos_estrategicos_sorpresa` (3756), `tipos_innovacion_i_ii` (3779), `verificar_modelo_ingresos` (3692), `vesting_acciones_fundadores` (3759), `viaje_diagnostico_remedial` (3722) |
| **SIN VEREDICTO ESCRITO** | **0** | (ninguno) |

**3. Los que salen CONFIRMADA son las CURAS ACOPLADAS** (destejido y fusion en el mismo acto, banco
9.4). **La ficha ya tiene la serie escrita** (SANO POR DENTRO, GEMELO POR FUERA, con sus ejemplares
CUARTO a DUODECIMO mas el DECIMOTERCERO Y CUARTO, lineas 2899 a 3184) **y ninguno de los 15 es
nuevo: los 15 ya estan escritos, se citan, no se reescriben:**

- **Diez tienen ejemplar numerado propio** en la serie: `optimizacion_embudo_get_customers`
  (CUARTO, linea 2940), `producto_unico_superior` (QUINTO, linea 2973),
  `propuesta_gasto_capital` (SEXTO, linea 2990), `key_partners_hypothesis` (SEPTIMO, linea 3008),
  `split_testing_experimentos_ab` (OCTAVO, linea 3029), `voz_del_cliente_voc` (NOVENO, linea 3051),
  `ab_testing_optimizacion` (UNDECIMO, linea 3091), `seleccion_ceo_fundador` (DUODECIMO, linea
  3111), `producto_minimo_viable` y `principio_calidad_mvp` (DECIMOTERCERO Y CUARTO, LA CURA
  ACOPLADA MAYOR, linea 3118).
- **Dos son el precedente citado dentro de esa misma serie**: `blueprint_de_experiencia` y
  `customer_journey_mapping` (puesto 341, "precedente exacto" nombrado en la linea 3128, con su
  propia seccion en la ficha, lineas 846 a 1260).
- **Tres estan en la tabla "TRES que el goteo no habia encontrado"** del recuento completo del 13
  ago 2026 (linea 3154 a 3163): `brainstorming_divergente` (tres gemelos, 823/834/844),
  `future_scenarios_planning` (`escenarios_futuros`, 711) y `plan_de_adquisicion_acquire`
  (`plan_acquire_activate`, 344).

**VERIFICACION CRUZADA, no pedida por el encargo pero barata y decisiva: los 15 CONFIRMADA ya
tienen operacion propia en `docs/plan/OPERACIONES.jsonl`.** Cada uno de los 15 aparece en la nomina
de `nodos` de alguna `OP-D-01` a `OP-D-06`: `OP-D-01` (producto_minimo_viable,
principio_calidad_mvp), `OP-D-02` (voz_del_cliente_voc), `OP-D-03` (ab_testing_optimizacion,
optimizacion_embudo_get_customers, split_testing_experimentos_ab), `OP-D-04`
(brainstorming_divergente), `OP-D-05` (seleccion_ceo_fundador), `OP-D-06` (todos los demas:
blueprint_de_experiencia, customer_journey_mapping, future_scenarios_planning,
key_partners_hypothesis, plan_de_adquisicion_acquire, producto_unico_superior,
propuesta_gasto_capital, mas los dos que repite con `OP-D-01`). **Cero de los 15 quedan sin dueno.**
El paso 2, corrido por la via acotada, no encuentra ninguna cura acoplada nueva que el plan no
tuviera ya contemplada: confirma que `OP-D-01` a `OP-D-06` son exhaustivas sobre el universo de los
36.

---

## PASO 3. EL CIERRE TRANSITIVO

**Calculado sobre el retrato del paso 1 (las 583 A resueltas), no sobre el archivo crudo.**

| | |
|---|---:|
| nodos con al menos una A (tras resolver) | ~~**854**~~ **852** **[CORREGIDA 15 ago 2026, ver la correccion declarada al principio del documento]** |
| componentes totales (tamano >= 2) | ~~**335**~~ **334** **[CORREGIDA 15 ago 2026, ver la correccion declarada al principio del documento]** |
| distribucion de tamanos | 2: 244 &#124; 3: 56 &#124; 4: 16 &#124; 5: 7 &#124; 6: 5 &#124; 7: 2 &#124; 8: 1 &#124; 9: 1 &#124; 10: 1 &#124; 13: 1 &#124; 15: 1 |

**Las componentes grandes nombradas por `OP-U-01`/`OP-U-02` al corte 2.117 siguen presentes hoy,
mismo tamano, identificadas por el nodo que la nota de esas operaciones cita** (verificado por
coincidencia de nombre y tamano, no por un registro historico de membresia completa que no
existe):

| tamano | nombre citado en la nota vieja | miembro que la identifica | sigue del mismo tamano hoy |
|---:|---|---|---|
| 13 | "puertas y portafolio" | `gestion_de_portafolio_gates_go_kill` | **si, 13** |
| 9 | "customer discovery" | `customer_discovery` | **si, 9** |
| 8 | "build, measure, learn" | `build_measure_learn` | **si, 8** |
| 7 | "customer validation" | `customer_validation` | **si, 7** |
| 7 | "el brainstorming" | `brainstorming_divergente` | **si, 7** |

**Ninguna de las cinco crecio ni se cerro entre el 2.117 y el 3.388.** Las dos que `OP-U-02`
declaraba con dueno en otra fase tambien se confirman presentes con su nomina completa: la de
`OP-D-03` (`ab_testing_optimizacion`, `funnel_get_customers_optimizacion`,
`optimizacion_embudo_get_customers`, `split_testing`, `split_testing_experimentos_ab`,
`test_ab_precio`, tamano 6) y la de `OP-D-04` (`brainstorming_divergente` y sus seis companeros,
tamano 7, la misma de la fila de arriba).

**La componente nueva mas grande, tamano 15, es enteramente del dominio `health_safety`**
(`cultura_de_seguridad_interpretivista_funcionalista`, `errores_como_consecuencia`,
`new_view_vs_old_view`... la familia entera de vieja-vision-contra-nueva-vision del error humano):
no existia al corte 2.117 porque el cribado de `health_safety` no habia cerrado todavia (cierra en
la seccion 80 del informe, con puesto posterior a 2.117). **La segunda componente nueva mas
grande, tamano 10, es enteramente de `quality`** (`causas_comunes_vs_especiales` y su familia de
nueve companeros): tampoco existia al corte 2.117, porque `quality` no habia abierto su cribado
(seccion 81, tambien posterior).

---

## PASO 4. LAS NOMINAS Y LOS ACTOS, con cobertura al lado

**Cada componente re-medida con banco 9.26 (cobertura al lado) y reclasificada CERRADO/ABIERTO con
el mismo criterio de `OP-U-01`: CERRADO cuando TODOS los pares posibles entre miembros estan
leidos (`fuera_de_cola == 0` y `en_cola_sin_leer == 0`); ABIERTO en cualquier otro caso.**

**AVISO METODOLOGICO QUE CAMBIA EL CALCULO RESPECTO AL 2.117: la cola intra-dominio esta AGOTADA
(verificado, `docs/INTRA_DOMINIO_PARES.jsonl` y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` tienen
EXACTAMENTE los mismos 3.388 pares, cero diferencia en ningun sentido).** Eso significa que la
segunda condicion del criterio de `OP-U-01` ("ningun miembro tiene un par pendiente en la cola sin
leer") **es hoy trivialmente cierta para todo el mundo**: no queda ni un par de la cola sin leer.
Lo unico que puede dejar abierto un acto hoy es la primera condicion: que existan pares POSIBLES
entre miembros del acto que **nunca entraron a la cola** (el universo de `OP-L-02`, "fuera de
cola"). El script lo mide exactamente asi: `fuera_de_cola` es la cuenta de esos pares.

### El marcador nuevo

| | corte 2.117 (`OP-U-01`/`OP-U-02`) | corte 3.388 (esta vuelta) | diferencia |
|---|---:|---:|---:|
| actos totales (tamano >= 2) | 221 | **335** | **+114** |
| **CERRADOS** | 173 | **280** | **+107** |
| nodos en actos CERRADOS | 371 | **600** | **+229** |
| **ABIERTOS** | 48 | **55** | **+7** |
| nodos en actos ABIERTOS | 205 | **254** | **+49** |
| nodos en actos, total | 576 | **854** | **+278** |

**CERRADOS por tamano (corte 3.388):** 2: 244, 3: 32, 4: 4. Contra el 2.117 (149 de dos, 23 de
tres, 1 de cuatro, el de SPIN): **crecieron los tres niveles**, y el de cuatro paso de 1 a 4 (SPIN
sigue siendo uno de ellos, verificado por nombre: `framework_spin_selling`,
`metodologia_spin_selling`, `modelo_spin`, `modelo_spin_preguntas`, presente en la lista de
tamano 4).

**ABIERTOS por tamano (corte 3.388):** 3: 24, 4: 12, 5: 7, 6: 5, 7: 2, 8: 1, 9: 1, 10: 1, 13: 1,
15: 1. Los de tamano >= 5 suman **19** (7+5+2+1+1+1+1+1), contra los **16** nombrados al 2.117
(1 de 13, 1 de 9, 1 de 8, 2 de 7, 4 de 6, 7 de 5). **La diferencia de +3 se explica entera:** la
fila de seis crecio de CUATRO a CINCO (+1), y aparecen las dos componentes enteramente nuevas
identificadas en el paso 3, tamano 10 (+1) y tamano 15 (+1). 4+1+1+1 no cuadra con la aritmetica
simple porque el quinto miembro de la fila de seis TAMBIEN es nuevo (arista mas vieja posterior al
2.117): 16 (viejos) + 1 (crecio la fila de 6) + 1 (el de 10) + 1 (el de 15) = 19.

### Cuantos actos son continuacion de antes del 2.117 y cuantos son enteramente nuevos

**MEDIDO POR PROXY DE EDAD DE ARISTA (la fecha, `puesto_intra`, de la A mas antigua que conecta
cada par dentro de la componente), NO POR UN MAPEO 1 A 1 CONTRA LA MEMBRESIA DE LOS 48 ANTIGUOS:
esa membresia completa nunca se escribio como lista en ningun documento del plan (solo tamanos y
un puñado de nombres, citados arriba), asi que un mapeo exacto no se puede hacer sin inventar.**
Este proxy es lo maximo que se puede medir sin adivinar:

| | actos | de ellos, ABIERTOS | de ellos, CERRADOS |
|---|---:|---:|---:|
| **TODO ANTERIOR AL 2.117** (todas sus aristas A tienen puesto <= 2.117) | 221 | 42 | 179 |
| **MIXTO** (al menos una arista <= 2.117 y al menos una > 2.117) | 1 | 1 | 0 |
| **TODO POSTERIOR AL 2.117** (todas sus aristas A tienen puesto > 2.117) | 113 | 12 | 101 |

**Lectura, con la cautela de que es un proxy:** de los 55 actos abiertos de hoy, **43 (42 + el
mixto) tienen alguna arista anterior al 2.117**, o sea que son continuacion de algo que ya existia
en alguna forma (abierto o cerrado) al corte viejo; **12 son enteramente nuevos**, formados por
completo dentro del cribado que corrio despues del 2.117. **Ninguno de los cinco actos grandes
nombrados en la tabla del paso 3 aparece entre los enteramente nuevos** (los cinco tienen su A mas
vieja anterior al 2.117, verificado). ~~**Con esa cautela declarada: no se puede decir con certeza
cuantos de los 48 antiguos cerraron**, porque un acto abierto viejo pudo haberse partido o fundido
con otro por una A nueva y el proxy de edad no distingue eso de una simple continuacion. Lo que
si se puede decir, medido: ninguno de los CINCO actos grandes identificables por nombre paso de
abierto a cerrado, y 113 actos son enteramente producto del cribado que corrio entre el 2.117 y
el 3.388 (los 1.271 pares que faltaban), de los cuales 101 nacieron ya cerrados (en su
mayoria pares de dos de `quality`, que aporta 25 de las 28 fusiones mutuas del catalogo) y 12
nacieron abiertos (entre ellos las dos componentes nuevas mas grandes, tamano 15 en
`health_safety` y tamano 10 en `quality`).~~

**CORRECCION DECLARADA (vuelta 12, auditor Opus 5, VERIFICADA POR EL EJECUTOR CON INSTRUMENTO
PROPIO, no solo transcrita): el mapeo de los 48 antiguos SI se puede hacer 1 a 1, sin proxy.** La
condicion que lo permite: **la cola `docs/INTRA_DOMINIO_PARES.jsonl` esta completa en 3.388 pares
desde el 9 ago 2026** (`c442345a`, "la cola completa, 3388 pares ordenados") **y no se ha tocado
desde entonces** (`git diff --stat c442345a -- docs/INTRA_DOMINIO_PARES.jsonl` vacio), asi que la
cola contra la que se midio `OP-U-01` el 11 ago 2026 es la misma de hoy. **Metodo:** se vuelve a
correr la medicion de `OP-U-01` sobre el mismo archivo, truncado al corte viejo (2.117 lineas) y
**excluyendo la correccion posterior del 2.078** (forzado a D, su clase el 11 ago), con el
CRITERIO ORIGINAL DE DOS CONDICIONES escrito en la nota de `OP-U-01`/`OP-U-02`: (1) todos los pares
posibles entre miembros ya leidos, y (2) **ningun miembro tiene un par pendiente en la cola sin
leer, CONTRA CUALQUIER NODO, no solo contra otro miembro del acto**. Con la condicion (2) medida en
su forma completa (no solo pares internos al acto, que es la simplificacion valida SOLO cuando la
cola esta agotada, como al corte 3.388), **el ejecutor reproduce la cifra publicada EXACTA**: 221
componentes sobre 576 nodos, **173 cerrados sobre 371** (149 de dos, 23 de tres, uno de cuatro),
**48 abiertos sobre 205**, motivos **42 por par interno mas 6 por miembro pendiente**. Con esa
membresia:

| los 48 actos abiertos del 2.117 | cuantos | verificado |
|---|---:|---|
| **CERRARON** (mismos miembros, hoy CERRADO) | **5** | si |
| siguen abiertos, identicos, sin crecer | **42** | si |
| siguen abiertos y CRECIERON | **1** | si (`gestion_terminacion_franquiciado` con `terminacion_franquiciado_causas`, de 2 a 3) |

Y por el otro lado: **114 actos de hoy no contienen ni un nodo que estuviera en un acto del 2.117**;
**102 de esos nacieron cerrados y 12 nacieron abiertos**. Las cuentas cierran: 173 + 5 + 102 =
**280**; 42 + 1 + 12 = **55**. **El proxy de edad de arista de arriba (221/1/113, con 101 nacidos
cerrados y 12 abiertos) difiere en exactamente una unidad, y la unidad es el mismo 2.078**: su
arista es anterior al 2.117, asi que el proxy lo llama continuacion, pero en el corte viejo ese
par era D y su acto no existia. Las dos mediciones son coherentes entre si una vez nombrada la
causa. **Ninguno de los cinco actos grandes identificables por nombre cerro ni cambio de
tamano**, confirmado con las dos vias.

---

## LAS CUATRO COMPROBACIONES

**Comando:** el mismo, seccion final de su salida.

| # | comprobacion | resultado |
|---:|---|---|
| **i** | nodos en actos (~~854~~ **852**) == suma de tamanos de las componentes (~~854~~ **852**) | **OK**, recomprobado el 15 ago 2026 |
| **ii** | A vigentes resueltas del retrato (~~583~~ ~~582~~ ~~580~~ ~~533~~ **525**) == suma de aristas A internas de las componentes (~~583~~ ~~582~~ ~~580~~ ~~533~~ **525**) | **OK**, recomprobado el 15 ago 2026 con las cifras nuevas, DOS veces, ~~y **RE-CORRIDO EL 19 ago 2026 (vuelta 49): sigue OK con 533 y 533**~~ ~~y **RE-CORRIDO OTRA VEZ EL 19 ago 2026 (vuelta 50) CON LA PAREJA NUEVA: sigue OK con 525 y 525**~~ y **RE-CORRIDO POR TERCERA VEZ AL CIERRE DE LA VUELTA 50, DESPUES DE FUNDIR: sigue OK con 522 y 522**, y con el las otras tres ([`../loop/SALIDA_V50_RECOMPUTO_CIERRE.txt`](../loop/SALIDA_V50_RECOMPUTO_CIERRE.txt), *LAS CUATRO: TODAS OK*). **La pareja de la apertura de la vuelta 50 se tacha por el mismo motivo que la de la 49: era cierta al medirla y la propia vuelta la movio despues.** **La pareja de la vuelta 49 se tacha y no se borra: era cierta con el retrato de aquel corte y dejo de serlo cuando el 305 y las tres fusiones movieron el retrato dentro de la propia vuelta 49** |
| **iii** | todo acto CERRADO tiene sus pares internos leidos y ningun miembro con par pendiente | **OK**, verificado sobre los 280 |
| **iv** | ningun nodo deprecado aparece dentro de una componente | **OK**, 0 encontrados |

**LAS CUATRO CUADRAN.** El recomputo esta bien hecho por su propio criterio: no hay auto-aristas
fantasma, no hay deprecados colados dentro de una componente (que habria significado que el
resolutor no resolvio), y las dos sumas de control (nodos y aristas) cierran exactas.

---

## POR QUE LA DIFERENCIA DE `OP-E-03` (387 FILAS) NO BAJO, CERRADO

**Pregunta abierta de la TAREA 3 de la vuelta 11** (`docs/loop/REPORTE.md` de esa vuelta, que se
sobreescribe por vuelta, y `docs/plan/08_VERIFICACION.md`): el encargo de esa vuelta esperaba que
la diferencia del barrido calibrado contra la cola BAJARA una vez que `risk_management`,
`seguridad_digital` y `quality` cerraran su cribado, porque el ensayo en vacio del 11 ago 2026
(387 de 477) se corrio cuando esos tres dominios (`quality` sobre todo) todavia no tenian cola.
**No bajo: sigue en 387 de 477, byte por byte identico.**

**CORRECCION DECLARADA (vuelta 12, auditor Opus 5, adjudicacion 2.c de su acta): la expectativa de
baja fue un error del auditor, no del ejecutor, y la razon decisiva se lee directo en el script.**
`scripts/plan/diferencia_contra_cola.py` compara cada candidato del barrido contra la **UNION** de
`docs/INTRA_DOMINIO_PARES.jsonl` (la cola PLANIFICADA) **mas** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
(los pares ya leidos), y **la primera esta completa en 3.388 pares desde el 9 ago 2026** (`c442345a`,
verificado sin diferencia contra el estado de hoy). **La cola planificada no crece cuando un
dominio se criba: crece el archivo LEIDO, que ya estaba dentro de la union desde antes.** Por eso
el 387 no podia moverse pasara lo que pasara con `quality`, `risk_management` o `seguridad_digital`:
esos tres dominios ya aportaban sus pares a la union por el lado de `INTRA_DOMINIO_PARES.jsonl`
desde el 9 ago, antes incluso del ensayo en vacio del 11 ago que produjo el 387. **El ejecutor de
la vuelta 11 hizo bien en publicar la cifra sin forzar la baja**; su explicacion de entonces
(heuristicas de generacion de candidatos distintas, solape estructuralmente chico) es cierta pero
no era la razon decisiva. Queda escrita aqui la razon decisiva, para que ningun encargo futuro
vuelva a pedir una baja imposible.

---

## LO QUE ESTE RECOMPUTO NO DECIDE

~~**Ninguna operacion cambia de estado con este documento.** `OP-U-02` queda con la evidencia de
arriba, a la espera de que el auditor verifique las cuatro comprobaciones y autorice el paso a
LISTA en el encargo siguiente. `OP-U-01`, `OP-L-02`, las cinco mesas y las seis `OP-D-*` siguen con
sus cifras del corte 2.117 hasta esa misma autorizacion (banco del plan P.12: el cierre transitivo
CONVOCA, no decide; una componente medida no es una fusion aprobada).~~

**CORRECCION DECLARADA (vuelta 12): la autorizacion ya se dio.** El auditor (Opus 5, acta vuelta
11, adjudicacion 4.1) verifico las cuatro comprobaciones con instrumento propio, con la prueba
extra de identidad conjunto a conjunto de las 335 componentes, y autorizo el paso. **Esta misma
vuelta, `docs/plan/OPERACIONES.jsonl` SI se edita** (TAREA 2.A del encargo): `OP-U-02` pasa a
LISTA con `fecha_corte` 2026-08-13, y `OP-U-01`, `OP-L-02`, las cinco mesas y las seis `OP-D-*`
reescriben sus cifras con el corte 3.388 al lado del corte 2.117 (banco 9.21, la vieja no se
borra). El recomputo en si (este documento) sigue siendo lectura pura: la escritura vive en
`OPERACIONES.jsonl`, no aqui.

**El fichero de detalle, con las 335 componentes fila por fila (miembros, cobertura, clases
internas, estado, edad), vive en** `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`, **solo lectura,
salida directa del script.**

---

## TAREA 1 (vuelta 13): dos verificaciones y su cierre

### 1. La nomina de las 46 SI existe (correccion declarada)

**CORRECCION DECLARADA (vuelta 13, sin borrar el texto viejo).** El `docs/loop/REPORTE.md` de la vuelta 12 (commit `77ffde4c`, seccion LO QUE NO SE MIDIO) escribio dos frases que quedan citadas aqui, tachadas, para que la correccion se pueda auditar:

> tachado: "La nomina completa de las 46 confirmadas (no solo las 36 con A) sigue sin estar escrita como lista en ningun sitio."
> tachado: "las 10 restantes de las 46 (las que no tienen A vigente, si las hay) no se buscaron"

**Las dos frases son falsas y las dos se corrigen aqui, verificadas con instrumento propio antes de escribirse.**

**La nomina SI esta escrita.** Vive en `docs/FICHA_SUBFUSION_GRADIENTE.md`, tabla "Las 128, con su fila y su veredicto" (lineas 3651 a 3780). Comando: parseo de las 128 filas de esa tabla. **Resultado, verificado: 128 filas, 128 ids distintos, 46 confirmadas y 82 falsas** (contra la fila de totales que la propia ficha ya publicaba en la linea 3640: 46 / 82 / 128, exacta).

**La aritmetica correcta: de las 46 confirmadas, QUINCE tienen A vigente al corte 3.388 y TREINTA Y UNA no.** Comando: cada uno de los 46 ids resuelto por alias (P.1) y comparado contra el conjunto de 854 nodos con A del paso 1 del recomputo (script nuevo esta vuelta, `scripts/loop/barrido_vuelta13.py`). **Las QUINCE con A vigente son exactamente las 15 CONFIRMADA ya citadas en el paso 2 de este documento** (la misma lista, verificada dos veces por dos vias: por interseccion contra las 128 citas en el paso 2 original, y ahora por interseccion directa contra las 46 confirmadas), las mismas que ya tienen dueno en `OP-D-01` a `OP-D-06`.

**El 10 de la vuelta pasada salia de restar 46 menos 36 (la interseccion de las 128 citas contra las 854 con A, no el numero de confirmadas dentro de ella). El numero correcto de confirmadas SIN A vigente es 31, no 10.** Las 31 se listan completas en la TAREA 2.B de mas abajo.

### 2. `OP-S-10`, la unica operacion del plan que se mueve entre los dos cortes

**Remedido, tal como pide el encargo, antes de escribirlo.** Comando: `python scripts/loop/barrido_vuelta13.py` (script nuevo esta vuelta, modelado sobre `scripts/plan/recomputo_3388.py`; corte viejo por `git show c16a24f5:docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, el metodo que quedo escrito en el paso 1 de este documento; corte nuevo por el archivo de hoy).

| | corte 2.117 | corte 3.388 |
|---|---:|---:|
| pares internos leidos de la nomina de 31 | 7 | 17 |
| de esos, clase A | 1 | 2 |
| actos que tocan la nomina | 3 | 6 |
| nodos de la nomina dentro de un acto | 4 | 8 |

**Exacto contra la medicion del auditor, las cuatro cifras.** Detalle de los seis actos al corte 3.388: `cinco_categorias_costos_franquicia` / `costos_preparacion_franquicia` / `estimacion_inversion_inicial_franquiciador` (3); `contratar_abogado_especializado_franquicias` / `contratar_abogado_franquicias` / `eleccion_abogado_franquicias` (3); `elaboracion_fdd` / `preparar_fdd` (2); `comprender_definicion_legal_franquicia` / `marco_name_system_fee` (2); `deteccion_franquicia_inadvertida` / `estructuras_combinadas_franquicia` / `prevenir_franquicias_inadvertidas` (3); `confidencialidad_manual_operaciones` / `desarrollar_manual_operaciones` (2).

**Verificado contra el universo entero: de las 43 operaciones del plan con nomina de dos nodos o mas (`OP-D-07` tiene una sola y no entra en la comparacion), `OP-S-10` es LA UNICA que cambia entre los dos cortes.** Las otras 42 (incluidas `OP-L-02`, las cinco mesas con sus 22 hijas y las seis `OP-D-01` a `OP-D-06`, ya verificadas en la vuelta pasada) se remidieron esta vuelta como control cruzado y dieron CERO cambios.

**`OPERACIONES.jsonl` se edita: `OP-S-10` reescribe su nota con las dos cifras, el corte viejo al lado del nuevo (banco 9.21), y la nota de orden entre fases: `OP-S-10` es SANEO (fase 05) y el saneo corre DESPUES de las FUSIONES (fase 03, `00_INDICE.md`, seccion EL ORDEN). El precedente citable es `OP-F-03`, que ya escribio la misma precaucion para sus tres cruces ("en los tres manda el orden fuente primero").**

**DISCUTIBLE MARCADO:** la frase del encargo "seis de sus treinta y un nodos habran sido absorbidos cuando le llegue el turno" NO se pudo reproducir con instrumento propio. Verificado: cero de los 31 nodos de la nomina aparecen en el campo `nodos` de ninguna operacion FUSION o DESTEJIDO ya LISTA (comando: interseccion de conjuntos contra las 69 operaciones). Hoy no hay ninguna fusion YA DECIDIDA que absorba a alguno de los 31: los seis actos de la tabla de arriba no tienen operacion propia ni superviviente elegido en ningun documento del plan. Lo unico medible es que 8 de los 31 caen dentro de un acto que algun dia se fundira, y de esos SOLO el par `elaboracion_fdd` / `preparar_fdd` es INTERNO a la propia nomina de `OP-S-10` (fusionar ese par absorbe con certeza a uno de los dos). Cuantos de los otros seis nodos terminan absorbidos depende de que nodo se elija superviviente en cada uno de los otros cinco actos, eleccion que no esta escrita en ningun sitio. Se trae la cifra de seis tal como la dio el encargo, sin reescribirla ni descartarla: la verifica el auditor con lo que tenga a mano.

---

## TAREA 2.A (vuelta 13): el barrido se completa sobre las 69

**Universo: las operaciones que quedaron fuera del barrido de la vuelta pasada** (`OP-F-01` a `OP-F-04-RAC`, las doce `OP-S-*`, `OP-D-07`, `OP-E-01`, `OP-E-02`, `OP-E-04`, `OP-E-05`, las cinco `OP-C-*`, las dos `OP-A-*`, `OP-V-01`, `OP-I-01`, `OP-L-01`, `OP-L-03`; 35 operaciones). Comando: `python scripts/loop/barrido_vuelta13.py` para las 17 con nomina de dos nodos o mas; lectura directa de `adjudicacion` y `nota` en `docs/plan/OPERACIONES.jsonl` para las 18 sin nomina comparable.

### Las operaciones CON nomina de dos nodos o mas (17, mas `OP-D-07` con una sola)

| operacion | nomina | 2.117: leidos (A) / actos sobre nodos | 3.388: leidos (A) / actos sobre nodos | cambia |
|---|---:|---|---|:--:|
| `OP-F-01` | 7 | 0 (0) / 0 sobre 0 | 0 (0) / 0 sobre 0 | no |
| `OP-F-02` | 3 | 0 (0) / 2 sobre 2 | 0 (0) / 2 sobre 2 | no |
| `OP-F-03` | 21 | 1 (0) / 3 sobre 3 | 1 (0) / 3 sobre 3 | no |
| `OP-F-04-COL` | 15 | 2 (1) / 3 sobre 4 | 2 (1) / 3 sobre 4 | no |
| `OP-F-04-HOR` | 13 | 1 (0) / 1 sobre 1 | 1 (0) / 1 sobre 1 | no |
| `OP-F-04-WEI` | 13 | 1 (1) / 7 sobre 8 | 1 (1) / 7 sobre 8 | no |
| `OP-F-04-RAC` | 4 | 0 (0) / 3 sobre 3 | 0 (0) / 3 sobre 3 | no |
| `OP-S-01` | 2 | 1 (1) / 1 sobre 2 | 1 (1) / 1 sobre 2 | no |
| `OP-S-02` | 3 | 2 (1) / 2 sobre 3 | 2 (1) / 2 sobre 3 | no |
| `OP-S-03` | 3 | 0 (0) / 0 sobre 0 | 0 (0) / 0 sobre 0 | no |
| `OP-S-04` | 5 | 1 (1) / 1 sobre 2 | 1 (1) / 1 sobre 2 | no |
| `OP-S-06` | 6 | 0 (0) / 2 sobre 2 | 0 (0) / 2 sobre 2 | no |
| `OP-S-07` | 27 | 1 (0) / 9 sobre 9 | 1 (0) / 9 sobre 9 | no |
| `OP-S-10` | 31 | 7 (1) / 3 sobre 4 | 17 (2) / 6 sobre 8 | SI, ver TAREA 1.2 |
| `OP-E-04` | 9 | 8 (6) / 1 sobre 9 | 8 (6) / 1 sobre 9 | no |
| `OP-E-05` | 3 | 1 (0) / 1 sobre 3 | 1 (0) / 1 sobre 3 | no |
| `OP-D-07` | 1 | sin pares posibles (nomina de un solo nodo) | sin pares posibles | no |

**CERO cambios salvo `OP-S-10`.** Verificado con el mismo instrumento sobre las 43 operaciones del plan entero con nomina de dos o mas (incluidas las 26 ya verificadas la vuelta pasada), la unica que cambia sigue siendo `OP-S-10`.

### Las operaciones SIN nomina comparable (18)

**Regla aplicada:** para cada una, razonamiento de por que su cifra publicada no depende del corte del cribado intra-dominio, salvo dos EXCEPCIONES encontradas y declaradas como tales (no forzadas a la regla).

| operacion | cifra publicada | por que (no) depende del corte |
|---|---|---|
| `OP-S-05` | censo de herramientas: 6 muertas, 7 vivas, 1 no verificable, 14 verificadas | medida contra el estado de internet y el texto de los nodos, no contra INTRA_DOMINIO_VEREDICTOS.jsonl ni la cola. No depende del corte. |
| `OP-S-08` | 42 accesos directos en produccion: 22 internos, 20 externos | medida sobre el codigo fuente (grep sobre web/lib y web/app), ajena al archivo de veredictos. No depende del corte. |
| `OP-S-09` | 53 familias de ids, 125 nodos vivos | medida sobre los ids VIVOS del grafo por patron (sufijo, particulas, orden de palabras), no sobre veredictos A/D. El grafo no cambia porque se lean mas pares. No depende del corte. |
| `OP-S-11` | normalizacion del campo `fuente` (grafias repetidas del mismo libro) | medida sobre metadatos del grafo (campo `fuente`), no sobre veredictos. No depende del corte. |
| `OP-S-12` | 1.056 entradas duplicadas tras resolver, en 802 nodos (core 461, quality 306, health_safety...) | medida sobre `nodos_previos`/`nodos_siguientes` del grafo (estructura de aristas), no sobre el archivo de veredictos del cribado. No depende del corte. |
| `OP-E-01` | bolsa de candidatos de enlaces: de 742 brutos a 624, calibrada a 477 | universo de generacion DISTINTO (paso del nodo contra titulo del hijo candidato), no INTRA_DOMINIO. La calibracion del verbo ya corrio y esta fija. No depende del corte del cribado intra-dominio. |
| `OP-E-02` | regla de decision para sueltos (enlaza / funde / mesa), sin cifra propia | es una tabla de reglas, no una cuenta. El ejemplar medido (comprender_alineacion_etica_ia) es un caso ya resuelto. No depende del corte. |
| `OP-C-01` | sitios de codigo listados con su numero de linea | ubicaciones de codigo, ajenas al archivo de veredictos intra-dominio. No dependen de ningun corte del cribado. |
| `OP-C-02` | sitios de codigo listados con su numero de linea | igual que OP-C-01: ubicaciones de codigo, sin relacion con el cribado. |
| `OP-C-03` | sitios de codigo listados con su numero de linea | igual que OP-C-01. |
| `OP-C-04` | guarda de auto-arista con resolucion en Gate 0 | cambio de codigo, sin cifra ligada al cribado. |
| `OP-C-05` | lista blanca de aristas bidireccionales (2 enlaces mutuos mas 2 citas LD) | lista fija por evidencia de lectura ya escrita (LD-41 y otra), no por el estado del cribado. No depende del corte. |
| `OP-A-01` | regla de orden posicional del campo `fuente` (P.2) | regla sobre el orden del campo `fuente`, sin cifra ligada al cribado intra-dominio. |
| `OP-A-02` | doctrina ("la aduana no juzga, obliga a juzgar") | doctrina pura, sin cifra. |
| `OP-V-01` | doctrina ("el criterio de HECHO") | doctrina pura, sin cifra. |
| `OP-L-01` | 11 lecturas dirigidas EJECUTADAS el 11 ago 2026, saldo 2 A y 9 D | hechos pasados ya escritos con su veredicto: no son una cuenta derivada del estado actual del archivo de veredictos, son eventos fijos. No dependen del corte. |

**DOS EXCEPCIONES, declaradas y no forzadas a la regla de arriba:**

**`OP-I-01` SI depende del corte, y su cifra publicada esta desactualizada.** Su nota (11 ago 2026) dice: "CUATRO DOMINIOS no han entrado al cribado intra (quality 792, health_safety 283, risk_management 55 y seguridad_digital 55)". **Verificado contra el archivo de hoy: los cuatro SI tienen pares leidos al corte 3.388.** Comando: contar `dominio` en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, corte 2.117 (`git show c16a24f5:docs/INTRA_DOMINIO_VEREDICTOS.jsonl`) contra corte 3.388.

| dominio | pares leidos al 2.117 | pares leidos al 3.388 |
|---|---:|---:|
| quality | 0 | 844 |
| health_safety | 0 | 192 |
| risk_management | 0 | 106 |
| seguridad_digital | 0 | 27 |

**NO se recomputa aqui el inventario entero** (323 entradas de `10_INVENTARIO.md` e `INVENTARIO.jsonl`, incluida la propia cifra de "221 actos" que el mismo `OP-I-01` cita, tambien desactualizada contra los 335 de hoy): esta fuera del alcance de esta TAREA, que es sobre `OPERACIONES.jsonl`, no sobre el inventario navegable. **Se deja como DISCUTIBLE MARCADO y PENDIENTE DE DOCTRINA: el auditor decide si `OP-I-01` se reabre para un recomputo del inventario completo o si esta correccion basta como nota.**

**`OP-L-03` no se pudo verificar en ningun sentido, y se declara asi en vez de forzarse.** Su cifra ("55 pares por leer, repartidos en 29 actos": uno de seis con 6 pares, cuatro de cinco con 15, nueve de cuatro con 19, quince de tres con uno cada uno) describe un backlog de PARES INTERNOS SIN LEER dentro de actos que estaban abiertos alrededor del 12 ago 2026. **El cribado avanzo de 2.117 a 3.388 pares entre ese momento y hoy, y el paso 4 de este documento ya midio que CINCO actos que estaban abiertos cerraron en ese tramo.** Si alguno de esos 55 pares queda dentro de un acto que ya cerro, el backlog de `OP-L-03` esta hoy sobreestimado, y no hay en el repositorio una lista estructurada de los 55 pares (solo prosa en la `nota`, sin `nodos` ni ids linea por linea) con la que recomputar sin inventar. **Se marca DISCUTIBLE y PENDIENTE DE DOCTRINA: la nomina de los 55 pares, si existe en algun sitio no encontrado, o el recomputo entero si no existe.**

---

### `OP-U-02`: "el recomputo no abre 48 fusiones: abre 44", recomputada con los dos criterios

**Criterio del propio plan** (los abiertos que ya tienen dueno en otra fase, mesa o destejido, no se cuentan como fusiones que el recomputo abra), aplicado sobre los 55 abiertos al corte 3.388 (antes 48 al 2.117, sin borrar esa cifra). Comando: cruce de `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` (55 filas ABIERTO) contra el campo `nodos` (resuelto por alias) de toda operacion `OP-M-*` u `OP-D-*` salvo `OP-U-01`/`OP-U-02`.

| tamano del acto | identificado por | dueno (mesa o destejido) |
|---:|---|---|
| 13 | `gestion_de_portafolio_gates_go_kill` (portafolio) | `OP-M-01` y sus hijas |
| 9 | `customer_discovery` | `OP-M-05-INDICE` / `OP-M-05-EDIFICIO` |
| 7 | `customer_validation` | `OP-M-05-APERTURA` |
| 7 | `brainstorming_divergente` | `OP-D-04` |
| 6 | `ab_testing_optimizacion` | `OP-D-03` |
| 4 | `formalizar_junta_asesora` (junta asesora) | `OP-M-04` |
| 4 | `enfoque_mercado_voc` (voz del cliente) | `OP-D-02` |
| 3 | `pivote_estrategico` (pivote) | `OP-M-03-III` / `OP-M-03-ENLACES` |

**OCHO actos ya tienen dueno en mesa o destejido. AL CORTE 3.388, CRITERIO DEL PROPIO PLAN: el recomputo no abre 55, abre 47** (55 menos los ocho).

**AVISO DE TRAMPA, criterio ANCHO y distinto** (que alguna nomina de CUALQUIER operacion, no solo mesa o destejido, toque algun miembro del acto). Comando: mismo cruce, contra el campo `nodos` de TODAS las operaciones (`OP-F-*`, `OP-S-*`, `OP-E-*` incluidas). **Verificado, exacto contra la medicion del auditor: 11 de los 55 tocan alguna nomina y 44 no tocan ninguna.**

**Que este segundo numero tambien de 44 sea coincidencia queda declarado: son dos cuentas distintas, sobre dos universos de tamano distinto (48 actos contra 55 actos) y con dos criterios distintos (dueno en mesa o destejido, contra toca cualquier nomina).** Entre los 44 que no tocan ninguna nomina bajo el criterio ancho estan las dos componentes enteramente nuevas (tamano 15 de `health_safety`, tamano 10 de `quality`) y **el de ocho del ciclo crear medir aprender (`build_measure_learn`), que a diferencia de los otros cuatro grandes citados en el paso 3 de este documento NUNCA tuvo dueno en ninguna operacion del plan, ni con el criterio ancho ni con el del propio plan.**

**`OPERACIONES.jsonl` se edita: `OP-U-02` agrega esta correccion a su nota, sin borrar la cifra vieja del 2.117 (44).**

### Comprobacion de integridad, TAREA 2.A

Comando: `python -c "import json; ops=[json.loads(l) for l in open('docs/plan/OPERACIONES.jsonl',encoding='utf-8') if l.strip()]; ..."` (conteo de lineas, ids unicos, y resolucion de `depende_de`/`bloquea_a` contra el conjunto de ids).

| comprobacion | antes | despues |
|---|---:|---:|
| operaciones (lineas) | 69 | 69 |
| ids unicos | 69 | 69 |
| ids duplicados | 0 | 0 |
| `depende_de` rotos (apuntan a un id que no existe) | 0 | 0 |
| `bloquea_a` rotos | 0 | 0 |

**Lineas exactas cambiadas (`git diff --stat docs/plan/OPERACIONES.jsonl`): 2 de 69** (`OP-S-10` y `OP-U-02`, una linea cada una porque el archivo es JSONL de una operacion por linea). Ninguna otra linea se toco. `dataset/` no se toco ni un byte.

---

## TAREA 2.B (vuelta 13): el paso 2, releido al doble, sobre las 46

**Efecto de la regla del credito (acta vuelta 12, seccion 4): el paso 2 del recomputo se corre sobre las 46 confirmadas enteras, no solo sobre las 36 con A.**

### 1. La nomina de las 46, citada linea a linea (cero se reescriben)

| cita | bloque | linea en FICHA_SUBFUSION_GRADIENTE.md |
|---|---:|---:|
| `producto_minimo_viable` | 80,2 | 3653 |
| `coeficiente_viral` | 74,7 | 3654 |
| `decision_de_vender_startup` | 69,3 | 3655 |
| `viral_loop_marketing` | 65,9 | 3656 |
| `transicion_producto_a_experiencia` | 60,1 | 3657 |
| `lienzo_modelo_negocio` | 59,2 | 3658 |
| `plan_mejora_procesos` | 56,7 | 3659 |
| `ab_testing_optimizacion` | 52,6 | 3660 |
| `planificacion_recoleccion_datos` | 52,3 | 3661 |
| `key_partners_hypothesis` | 51,7 | 3663 |
| `split_testing_experimentos_ab` | 51,5 | 3664 |
| `project_close_out` | 50,3 | 3670 |
| `blueprint_de_experiencia` | 50,3 | 3671 |
| `voz_del_cliente_voc` | 50,2 | 3672 |
| `cultura_de_experiencia` | 50,2 | 3673 |
| `future_scenarios_planning` | 50,1 | 3676 |
| `empoderamiento_de_participantes` | 50,1 | 3677 |
| `schedule_management_plan` | 49,8 | 3680 |
| `economia_circular_como_modelo_de_negocio` | 49,7 | 3682 |
| `metas_vs_proposito` | 49,7 | 3683 |
| `enfoque_motor_unico_crecimiento` | 49,5 | 3685 |
| `principio_calidad_mvp` | 49,2 | 3686 |
| `actualizacion_posiciones_existentes` | 49,0 | 3688 |
| `analisis_tco_roi_b2b` | 48,9 | 3690 |
| `customer_journey_mapping` | 48,6 | 3693 |
| `organizacion_adaptativa` | 48,5 | 3695 |
| `plan_de_adquisicion_acquire` | 48,3 | 3697 |
| `ratios_eficiencia_inventario` | 48,3 | 3701 |
| `modelo_hibrido_agile_stage_gate` | 48,1 | 3703 |
| `ganar_comprension_del_cliente` | 48,0 | 3708 |
| `mapa_de_canal_de_ventas` | 47,4 | 3715 |
| `seleccion_ceo_fundador` | 46,8 | 3743 |
| `cliente_disena_producto` | 46,6 | 3745 |
| `asociaciones_clave` | 46,5 | 3746 |
| `reduccion_tamano_de_lote_batch_size` | 46,0 | 3748 |
| `sistema_inmune_producto` | 45,9 | 3750 |
| `sales_funnel_get_keep_grow` | 45,9 | 3751 |
| `estrategia_de_innovacion_producto` | 45,7 | 3753 |
| `posicionamiento_de_empresa` | 45,6 | 3757 |
| `gut_check` | 45,2 | 3762 |
| `gestion_libro_abierto_obm` | 45,1 | 3763 |
| `brainstorming_divergente` | 44,8 | 3766 |
| `producto_unico_superior` | 44,2 | 3773 |
| `revisiones_regulares_desempeno_ceo` | 44,2 | 3774 |
| `optimizacion_embudo_get_customers` | 44,1 | 3775 |
| `propuesta_gasto_capital` | 44,1 | 3776 |

### 2. Partida en dos: las 15 con A vigente y las 31 sin ella

**Las QUINCE con A vigente al corte 3.388, ya cerradas la vuelta pasada, con dueno en `OP-D-01` a `OP-D-06`:**

`ab_testing_optimizacion`, `blueprint_de_experiencia`, `brainstorming_divergente`, `customer_journey_mapping`, `future_scenarios_planning`, `key_partners_hypothesis`, `optimizacion_embudo_get_customers`, `plan_de_adquisicion_acquire`, `principio_calidad_mvp`, `producto_minimo_viable`, `producto_unico_superior`, `propuesta_gasto_capital`, `seleccion_ceo_fundador`, `split_testing_experimentos_ab`, `voz_del_cliente_voc`

**Las TREINTA Y UNA sin A vigente:**

`actualizacion_posiciones_existentes`, `analisis_tco_roi_b2b`, `asociaciones_clave`, `cliente_disena_producto`, `coeficiente_viral`, `cultura_de_experiencia`, `decision_de_vender_startup`, `economia_circular_como_modelo_de_negocio`, `empoderamiento_de_participantes`, `enfoque_motor_unico_crecimiento`, `estrategia_de_innovacion_producto`, `ganar_comprension_del_cliente`, `gestion_libro_abierto_obm`, `gut_check`, `lienzo_modelo_negocio`, `mapa_de_canal_de_ventas`, `metas_vs_proposito`, `modelo_hibrido_agile_stage_gate`, `organizacion_adaptativa`, `plan_mejora_procesos`, `planificacion_recoleccion_datos`, `posicionamiento_de_empresa`, `project_close_out`, `ratios_eficiencia_inventario`, `reduccion_tamano_de_lote_batch_size`, `revisiones_regulares_desempeno_ceo`, `sales_funnel_get_keep_grow`, `schedule_management_plan`, `sistema_inmune_producto`, `transicion_producto_a_experiencia`, `viral_loop_marketing`

### 3. Para cada una de las 31, dos preguntas: aparece en la nomina de alguna operacion, y cual

| nodo | aparece en la nomina de | tipo de esa operacion |
|---|---|---|
| `actualizacion_posiciones_existentes` | `OP-F-04-HOR` | DECISION_DE_FUENTE (no fusion) |
| `analisis_tco_roi_b2b` | `OP-F-03` | DECISION_DE_FUENTE (no fusion) |
| `asociaciones_clave` | `OP-F-03` | DECISION_DE_FUENTE (no fusion) |
| `cliente_disena_producto` | `OP-F-04-COL` | DECISION_DE_FUENTE (no fusion) |
| `coeficiente_viral` | `OP-F-04-WEI` | DECISION_DE_FUENTE (no fusion) |
| `cultura_de_experiencia` | `OP-F-04-COL` | DECISION_DE_FUENTE (no fusion) |
| `decision_de_vender_startup` | `OP-F-04-HOR` | DECISION_DE_FUENTE (no fusion) |
| `economia_circular_como_modelo_de_negocio` | `OP-F-03` | DECISION_DE_FUENTE (no fusion) |
| `empoderamiento_de_participantes` | `OP-F-03` | DECISION_DE_FUENTE (no fusion) |
| `enfoque_motor_unico_crecimiento` | `OP-F-04-WEI` | DECISION_DE_FUENTE (no fusion) |
| `estrategia_de_innovacion_producto` | `OP-F-04-HOR` | DECISION_DE_FUENTE (no fusion) |
| `ganar_comprension_del_cliente` | `OP-F-04-COL` | DECISION_DE_FUENTE (no fusion) |
| `gestion_libro_abierto_obm` | `OP-F-03` | DECISION_DE_FUENTE (no fusion) |
| `gut_check` | `OP-F-02` | DECISION_DE_FUENTE (no fusion) |
| `mapa_de_canal_de_ventas` | `OP-F-03` | DECISION_DE_FUENTE (no fusion) |
| `metas_vs_proposito` | `OP-F-04-COL`, `OP-F-04-HOR` | DECISION_DE_FUENTE (no fusion) |
| `modelo_hibrido_agile_stage_gate` | `OP-F-03` | DECISION_DE_FUENTE (no fusion) |
| `organizacion_adaptativa` | `OP-F-04-HOR` | DECISION_DE_FUENTE (no fusion) |
| `plan_mejora_procesos` | `OP-F-04-HOR` | DECISION_DE_FUENTE (no fusion) |
| `posicionamiento_de_empresa` | `OP-F-04-HOR` | DECISION_DE_FUENTE (no fusion) |
| `project_close_out` | `OP-F-04-COL` | DECISION_DE_FUENTE (no fusion) |
| `ratios_eficiencia_inventario` | `OP-F-03` | DECISION_DE_FUENTE (no fusion) |
| `reduccion_tamano_de_lote_batch_size` | `OP-F-03` | DECISION_DE_FUENTE (no fusion) |
| `revisiones_regulares_desempeno_ceo` | `OP-F-04-HOR` | DECISION_DE_FUENTE (no fusion) |
| `sales_funnel_get_keep_grow` | `OP-F-04-WEI` | DECISION_DE_FUENTE (no fusion) |
| `schedule_management_plan` | `OP-F-03` | DECISION_DE_FUENTE (no fusion) |
| `sistema_inmune_producto` | `OP-F-04-COL` | DECISION_DE_FUENTE (no fusion) |
| `transicion_producto_a_experiencia` | `OP-F-03` | DECISION_DE_FUENTE (no fusion) |
| `viral_loop_marketing` | `OP-F-04-COL`, `OP-F-04-WEI` | DECISION_DE_FUENTE (no fusion) |
| `lienzo_modelo_negocio` | NINGUNA | (sin dueno) |
| `planificacion_recoleccion_datos` | NINGUNA | (sin dueno) |

**Fraccion: de las 31, VEINTINUEVE aparecen en la nomina de alguna operacion (todas `OP-F-*`, decisiones de fuente, NO fusiones) y DOS no aparecen en ninguna.**

**Precision necesaria para no confundir los dos sentidos de "dueno":** las 29 tienen dueno de FUENTE (una operacion que fija su atribucion bibliografica), no dueno de FUSION. Ninguna de las 31 tiene un par con A vigente (por eso estan en esta lista), asi que ninguna tiene gemelo con quien fundirse hoy, tenga o no una `OP-F-*` que le fije la fuente.

### 4. Las 31 son costuras confirmadas SIN gemelo vigente

**Las 31 son costuras confirmadas SIN gemelo vigente, o sea destejidos que NO son curas acopladas** (no hay fusion en el mismo acto que las acompane).

**Lista declarada de las DOS que ademas no tienen dueno en ninguna operacion del plan** (ni de fuente ni de fusion): `lienzo_modelo_negocio` y `planificacion_recoleccion_datos`. ~~**NO se crean operaciones nuevas para ellas ni para las otras 29: lo adjudica el auditor con esta lista delante.**~~

> **REVERTIDO POR DECISION DEL FUNDADOR, 14 ago 2026 (vuelta 17). LAS DOS RECIBEN DUENO.** El texto
> tachado no se borra: era la adjudicacion vigente del auditor (`docs/loop/ACTA_AUDITOR.md` VUELTA 13
> seccion 5 punto 5) y sigue siendo cierta de su fecha.
>
> | nodo | operacion nueva | forma |
> |---|---|---|
> | `lienzo_modelo_negocio` | **`OP-D-08`** | DESTEJIDO SOLO, orden 8 de `02_DESTEJIDOS` |
> | `planificacion_recoleccion_datos` | **`OP-D-09`** | DESTEJIDO SOLO, orden 9 de `02_DESTEJIDOS` |
>
> **EL PLAN PASA DE 69 A 71 OPERACIONES.** Las 69 viejas no se tocan: las dos se anaden al final de
> `docs/plan/OPERACIONES.jsonl`, con el mismo esquema de dieciocho campos, ids unicos y cero
> dependencias rotas (verificado tras escribir).
>
> **LO QUE SIGUE EN PIE DEL TEXTO TACHADO: las otras 29 NO reciben operacion nueva.** La decision del
> fundador nombra dos, y solo dos. Las 29 conservan su dueno de FUENTE en una `OP-F-*`, que es lo que
> esta misma seccion ya precisaba.
>
> **REMEDIDO EN LA VUELTA 17, no copiado de esta seccion** (`scripts/loop/vuelta17_dos_costuras.py`,
> de solo lectura sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `docs/COSTURAS_INTERNAS.jsonl` y
> `docs/plan/OPERACIONES.jsonl`): las dos siguen con **CERO A vigentes** y **CERO nominas de
> operacion** en el momento de escribirles la suya. `lienzo_modelo_negocio` tiene **siete** pares en
> el cribado (543 D, 784 B, 998 D, 999 D, 1123 D, 1136 D, 1434 D) y `planificacion_recoleccion_datos`
> tiene **uno** (2695 D).
>
> **UNA PRECISION QUE SOLO SE PUEDE HACER AHORA Y NO AL CORTE 2.117, y cambia el peso de la
> evidencia:** `planificacion_recoleccion_datos` es de `quality`, que **al corte 2.117 estaba SIN
> CRIBAR con cero pares juzgados**. Su "sin gemelo" de entonces no era una medicion, era un hueco de
> cribado. **Al corte 3.388, `quality` tiene 844 pares juzgados con 126 A** (medido en esta vuelta),
> asi que **hoy su cero A vigentes SI es una medicion.**

### 5. Ningun nodo se releyo para decidir si tiene costura

**Ningun nodo de las 31 (ni de las 15) se leyo de nuevo.** Los 46 veredictos CONFIRMADA/FALSA son copia literal de `docs/FICHA_SUBFUSION_GRADIENTE.md`; lo unico medido esta vuelta es la interseccion contra el conjunto de nodos con A vigente y contra las nominas de operaciones, ambas por id resuelto, sin abrir el texto de ningun nodo.

---

## TAREA (vuelta 14): tres correcciones adjudicadas por `docs/loop/PARA_ALEXIS.md` (opcion B, 13 ago 2026)

**Las tres vienen adjudicadas por el fundador via el auditor, seccion 5 punto 4 de la parada archivada
(`docs/loop/paradas/2026-08-13-credito-vuelta-13.md`) y por `docs/loop/ACTA_AUDITOR.md` seccion 4. No
son medicion nueva de doctrina: son cierre de lo que la vuelta 13 dejo abierto.**

### 1. La fila del bonus de `OP-L-02`, corregida con tachado

**El `docs/loop/REPORTE.md` de la vuelta 13 publico esta fila, y es la que causo la caida de credito
de esa vuelta (ACTA_AUDITOR.md seccion 4):**

> ~~bloque humano de la supervision de la IA | 10 (particion provisional 5+4+1) | 45 pares posibles |
> 10 leidos (cobertura MEZCLADO, no completa)~~ **FILA FALSA, mezclaba dos universos.**

**La fila corregida, verificada contra `docs/plan/LECTURAS_DIRIGIDAS.md` lineas 439 y 465 y contra la
nota de `OP-L-02` en `OPERACIONES.jsonl` ("bloque humano de la IA 10 de 10 con 7 A y 3 D"):**

**El bloque humano de la supervision de la IA tiene CINCO nodos y DIEZ pares posibles (no diez nodos
y cuarenta y cinco pares, que es el racimo entero de la supervision de la IA, otro universo). Los diez
estan leidos: cobertura COMPLETA, ~~7 en A y 3 en D~~.**

**REPARTO DE CLASES CORREGIDO EN LA VUELTA 16 (caida MIA del auditor, no del ejecutor de esta tanda; ver
`docs/loop/ACTA_AUDITOR.md` VUELTA 15 seccion 3): el "7 A y 3 D" se copio de la nota vieja de `OP-L-02`
comparando texto en vez de recomputar los diez pares. Remedido contra `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
con instrumento propio: de los siete en cola, `166` `human_in_the_loop_ia`-`principio_humano_en_el_loop`
A, `293` `mitigar_falling_asleep_wheel`-`riesgo_sobredependencia_ia` A, `692`
`alineacion_etica_ia_negocio`-`principio_humano_en_el_loop` A, `792`
`alineacion_etica_ia_negocio`-`human_in_the_loop_ia` A, `1.041`
`human_in_the_loop_ia`-`mitigar_falling_asleep_wheel` A, `1.496`
`human_in_the_loop_ia`-`riesgo_sobredependencia_ia` D, `1.541`
`mitigar_falling_asleep_wheel`-`principio_humano_en_el_loop` D (5 A, 2 D); mas las tres dirigidas, las
tres D. **EL REPARTO REAL ES 10 DE 10, CINCO A Y CINCO D, no siete y tres.** El conteo de diez pares
sigue siendo correcto: solo el reparto de clases cambia. No mueve la forma (sigue MEZCLADO) ni el 18 de
45 del racimo entero.**

~~El racimo entero (diez nodos, cuarenta y cinco pares) sigue con cobertura 10 de 45: los diez pares
leidos son justo los internos al bloque humano; los 35 restantes cruzan contra el bloque del mapa y
siguen sin leerse, tal como ya declaraba `OP-F-02`. Eso si es correcto en el reporte de la vuelta 13
y no se toca.~~ **FALSO, corregido en la vuelta 15.** Esta frase la escribio el auditor en el acta de
la vuelta 13 y se declaro "cierta"; el ejecutor de la vuelta 14 la copio aqui sin recomputarla, contra
el propio banco 9.10 (toda tabla que cita un veredicto se recomputa del archivo). El auditor declaro su
propia caida en `docs/loop/ACTA_AUDITOR.md` VUELTA 14 seccion 4 y encargo remedirla con instrumento
propio, sin copiar su cifra.

**REMEDIDO EN LA VUELTA 15, con instrumento propio (python sobre el jsonl, corrido fuera del texto del
acta), sobre la nomina de DIEZ de `docs/INTRA_DOMINIO_INFORME.md` secciones 11.bis.1 y 11.bis.3**
(bloque humano 5: `principio_humano_en_el_loop`, `human_in_the_loop_ia`, `alineacion_etica_ia_negocio`,
`mitigar_falling_asleep_wheel`, `riesgo_sobredependencia_ia`; bloque del mapa 4:
`comprension_capacidades_limitaciones_ia`, `jagged_frontier_ia`, `invitar_ia_a_todo`,
`principio_invitar_ia_siempre`; suelto 1: `comprender_alineacion_etica_ia`):

| medida | cifra |
|---|---:|
| pares posibles (C(10,2)) | 45 |
| pares de la nomina que estan en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **15**: puestos 166, 177, 293, 456, 692, 792, 993, 1.041, 1.211, 1.239, 1.339, 1.451, 1.496, 1.517, 1.541 (8 A, 7 D) |
| lecturas dirigidas del bloque humano fuera de cola | **3**: `alineacion_etica_ia_negocio` contra `mitigar_falling_asleep_wheel` (D), `alineacion_etica_ia_negocio` contra `riesgo_sobredependencia_ia` (D), `principio_humano_en_el_loop` contra `riesgo_sobredependencia_ia` (D); `docs/plan/LECTURAS_DIRIGIDAS.md` lineas 437 a 468, verificadas por busqueda directa: los tres pares no aparecen en `INTRA_DOMINIO_VEREDICTOS.jsonl` |
| **COBERTURA REAL DEL RACIMO AL 3.388** | **18 de 45** (8 A, 10 D) |
| **sin leer** | **27**, no 35 |

**Tres cosas falsas en la frase vieja:** la cobertura no es 10 de 45; los diez pares del bloque humano
no son los unicos leidos del racimo (el bloque del mapa aporta 177, 1.211, 1.239, 1.339, 1.451, 1.517,
y el suelto aporta 993); y los 35 restantes no "siguen sin leerse", porque ocho de ellos (los seis
cruzados entre bloques mas los dos de `comprender_alineacion_etica_ia`) ya estan leidos, cuatro de ellos
(1.211, 1.239, 1.339, 1.451) siendo justo los que probaron que el racimo se parte. La cuarta cosa: la
nota de `OP-F-02` no declara 10 de 45, declara **14 de 45 al puesto 1.517** (correcto para su corte de
entonces, sin el 1.541 y sin las tres lecturas dirigidas). **No es doctrina nueva: es la regla de la
FASE II (ninguna cifra publicada queda sin recomputar con su corte nuevo), mas banco 9.10, 9.21 y 9.26
(la forma se escribe con su cobertura al lado).**

### 2. El backlog de `OP-L-03`, recomputado al corte 3.388

**Medido con `scripts/loop/backlog_l03_vuelta14.py` (instrumento nuevo, solo lectura), por la via del
archivo de componentes `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`, la misma que se uso para
`OP-U-02` en la vuelta 13.**

**Metodo, calcado del que el propio `OP-L-03` ya tenia escrito:**
1. Universo: actos ABIERTOS de tamano 3 a 6 en el archivo de componentes al corte 3.388: **48 actos,
   107 pares fuera de cola.**
2. Se excluyen los actos que tocan alguna de las SEIS nominas que `OP-L-02` ya cerro por LECTURA
   DIRIGIDA (cuadrantes de mercado, ecuacion de valor, bloque humano de la supervision de la IA, sales
   roadmap, seleccion de canal, junta asesora): esas lecturas no viven en
   `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, asi que el archivo de componentes las sigue marcando
   ABIERTAS, y sin excluirlas a mano se cuentan dos veces entre `OP-L-02` y `OP-L-03`. Quedan **42
   actos, 83 pares.**
3. Del resto, se excluyen los que ESPERAN destejido o cirugia (banco: "cirugia" es sinonimo de
   DESTEJIDO, `00_INDICE.md` linea 326, "las siete cirugias hechas" son los siete `OP-D-*`): **DOS
   actos, 10 pares**, los dos con nomina dentro de una `OP-D-*` todavia sin ejecutar (`OP-D-03`, seis
   nodos del cierre de ventas A/B, 7 pares; `OP-D-02`, cuatro nodos de la voz del cliente, 3 pares).

**BACKLOG DE `OP-L-03` AL CORTE 3.388: CUARENTA actos, SETENTA Y TRES pares** (contra los VEINTINUEVE
actos y CINCUENTA Y CINCO pares del corte 2.117, banco 9.21 no borra el corte viejo). Reparto por
tamano de acto: **dos de SEIS con 14 pares; cuatro de CINCO con 15 pares; diez de CUATRO con 20 pares;
veinticuatro de TRES con 24 pares.** Lista de los 40 actos, nodo por nodo, en la salida de
`scripts/loop/backlog_l03_vuelta14.py` (no se repite aqui completa por espacio; el instrumento es
reproducible y de solo lectura).

**LA SUBIDA ES ESPERABLE, NO UN ERROR:** el backlog crecio de 29 a 40 actos porque el cribado paso de
2.117 a 3.388 y trajo pares nuevos en `quality`, `health_safety`, `risk_management` y
`seguridad_digital`, cuatro dominios que al corte viejo no habian entrado (ver punto 3 abajo). Los
actos nuevos del backlog son de esos dominios.

**DISCUTIBLE MARCADO:** de los 40 actos del backlog, CUATRO tocan ademas la nomina de una operacion NO
destejido (`OP-S-07` CAMPO_SUCIO dos veces, `OP-M-03-III` FUSION DE MESA mas `OP-M-03-ENLACES` ENLACE
una vez, `OP-S-04` HERRAMIENTA mas `OP-F-04-WEI` DECISION_DE_FUENTE una vez). La regla escrita de
`OP-L-02` solo excluye lo que "espera destejido o cirugia", no "cualquier operacion", asi que estos
cuatro se dejan DENTRO del backlog por lectura literal de la regla. Si el auditor lee "tiene dueno" mas
ancho (como el criterio ancho que `OP-U-02` uso para otra pregunta), la cuenta bajaria a 36 actos.
~~No se decide aqui: se trae la pregunta.~~

**ADJUDICADO EN LA VUELTA 15 (`docs/loop/ACTA_AUDITOR.md` VUELTA 14, seccion 2 y seccion 6 punto 1):
EL BACKLOG DE `OP-L-03` QUEDA EN CUARENTA ACTOS Y SETENTA Y TRES PARES, por lectura literal y no por
preferencia.** El auditor aplico el mismo metodo, sin cambiarlo, sobre **las componentes reconstruidas
del corte 2.117** (corriendo `scripts/plan/recomputo_3388.py` con `--veredictos` apuntando al blob
`git show c16a24f5:docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, 2.117 lineas, 400 A):

| paso | corte 2.117 reconstruido |
|---|---|
| ABIERTOS de tamano 3 a 6 | 37 actos, 89 pares |
| menos las seis nominas de `OP-L-02` | 31 actos, 65 pares |
| menos los que esperan destejido | **29 actos, 55 pares** |
| reparto por tamano | uno de 6 con 6; cuatro de 5 con 15; nueve de 4 con 19; quince de 3 con 15 |

**El 29 y el 55 son EXACTAMENTE la cifra publicada de `OP-L-03` (corte 2.117), con el reparto identico
al que la nota ya tenia escrito, y en ese corte LOS MISMOS CUATRO ACTOS EN DISPUTA (`OP-S-07`,
`OP-M-03-III`/`OP-M-03-ENLACES`, `OP-S-04`/`OP-F-04-WEI`) YA VIVIAN DENTRO de aquel 55.** El criterio
ancho aplicado al mismo corte viejo habria dado **25 actos y 51 pares**, que contradice la cifra
publicada del banco. **El metodo literal, sin cambios, es el metodo que produjo la cifra vieja: se
sostiene.** Sin doctrina nueva: banco 9.21 (la cifra vieja no se borra) mas la evidencia del propio
corte reconstruido. La nota de `OP-L-03` en `docs/plan/OPERACIONES.jsonl` queda puesta al dia con esta
adjudicacion, sin borrar el discutible.

### 3. El inventario de `OP-I-01`: 221 actos eran, hoy son 335

**Verificado contra `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`: 335 lineas, o sea 335 componentes de
tamano 2 o mas al corte 3.388** (280 CERRADOS, 55 ABIERTOS, comprobacion de integridad del propio
`recomputo_3388.py` en verde). **Contra los 221 actos que la nota de `OP-I-01` declaraba al corte
2.117.**

**Alcance de esta correccion: SOLO la cifra de actos.** El resto del inventario de 323 entradas (53
familias de ids, 14 defectos, 13 racimos, 12 figuras, 10 dominios, y el total de 323) no se recomputo:
el encargo de esta vuelta pedia solo la cifra de actos, y el propio `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`
no mide familias, defectos, racimos, figuras ni dominios. **Queda declarado, no medido, como
~~PENDIENTE DE DOCTRINA para un encargo propio~~ ENCARGO PROPIO DE RECOMPUTO** (etiqueta corregida en
la vuelta 15, `docs/loop/ACTA_AUDITOR.md` VUELTA 14 seccion 5 y seccion 6 punto 4: el acta de la vuelta
13, adjudicacion 6.4, ya dice literalmente que `OP-I-01` **no es pendiente de doctrina**, es un encargo
propio de recomputo de inventario; no mueve ninguna cifra ni ninguna clase, es correccion de etiqueta,
no de medicion) (ya lo declaraba el discutible 2 del reporte de la
vuelta 13): con 335 actos en vez de 221, el total de entradas del inventario tambien cambia (de 323 a
al menos 437), pero esa suma no se escribe aqui porque los otros cinco sumandos siguen sin
recomputarse.

---

## TAREA (vuelta 15): el recomputo del inventario de `OP-I-01` al corte 3.388

**Regla que gobierna esta seccion, la de la FASE II: ninguna cifra publicada queda sin recomputar con
su corte nuevo.** Toda cifra de cobertura o de conteo que aparece abajo se remidio contra el archivo en
ESTA vuelta, con instrumento propio (python sobre `docs/plan/INVENTARIO.jsonl`,
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` y
`docs/plan/LECTURAS_DIRIGIDAS.md`), no copiada de ningun acta ni de ningun encargo.

### 1. El archivo vivo, medido primero, y esta desfasado por DOS vias a la vez

**`docs/plan/INVENTARIO.jsonl` tiene HOY 336 entradas, contadas por el campo `tipo`:**

| tipo | cifra medida hoy | cifra que declara la nota vieja de `OP-I-01` |
|---|---:|---:|
| dominio | 10 | 10 |
| acto | 221 | 221 |
| racimo | 13 | 13 |
| familia_de_ids | 53 | 53 |
| figura | **20** | 12 |
| defecto | **19** | 14 |
| **total** | **336** | **323** |

**La nota de `OP-I-01` esta desfasada por dos vias independientes:** por el corte (los 221 actos son del
corte 2.117, hoy son 335 componentes, TAREA vuelta 14 ya corregida) y por el propio archivo (figura y
defecto crecieron de 12 a 20 y de 14 a 19 entre el 11 ago 2026 y hoy, por trabajo de plan que no toco el
cribado). **Las dos vias hay que decirlas**, y las cifras de figura y defecto de arriba (20 y 19) son la
cuenta real del archivo hoy, no la de la nota.

### 2. Los seis sumandos, cada uno con su instrumento y su dependencia del corte declarada

#### a. Dominios: los diez, con pares leidos y tasa de A al 3.388

**Instrumento: conteo directo de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` por campo `dominio`, las 3.388
lineas.**

| dominio | pares leidos | A | tasa de A |
|---|---:|---:|---:|
| core | 1.445 | 344 | 23,8 % |
| quality | 844 | 126 | 14,9 % |
| health_safety | 192 | 45 | 23,4 % |
| entrega | 171 | 2 | 1,2 % |
| environmental | 170 | 29 | 17,1 % |
| compras | 155 | 1 | 0,6 % |
| franquicias | 148 | 18 | 12,2 % |
| risk_management | 106 | 0 | 0,0 % |
| exportacion | 130 | 15 | 11,5 % |
| seguridad_digital | 27 | 3 | 11,1 % |
| **total** | **3.388** | ~~**583**~~ ~~**582**~~ ~~**581**~~ ~~**576**~~ ~~**575**~~ ~~**574**~~ ~~**573**~~ **571** | ~~**17,2 %**~~ ~~**17,1 %**~~ ~~**17,0 %**~~ **16,9 %** |

~~**Los diez dominios y el total (3.388 pares, 583 A) coinciden con el marcador recomputado de la vuelta
14** (`A 583, B 89, C 7, D 2.709`), verificado de nuevo aqui por suma de columna.~~ **CORRECCION
DECLARADA (15 ago 2026): la coincidencia era cierta el 13 ago y las dos cifras se movieron juntas.
Hoy el total es `A 582, B 87, C 8, D 2.711` sobre los mismos 3.388 pares, y el UNICO dominio que
cambia es `core`, porque los tres volteados son los tres de `core`. Medido hoy dominio por dominio
(`docs/loop/SALIDA_V33_TASA_DOMINIO.txt`): `core` pasa de `n 1445, A 344, B 87, C 7, D 1007` a
`n 1445, A 343 (23,7 por ciento), B 85, C 8, D 1009`. Los otros nueve dominios, identicos al
digito.** **SEGUNDA CORRECCION DECLARADA (18 ago 2026, vuelta 36): el total es hoy
`A 576, B 83, C 8, D 2.721` sobre los mismos 3.388 pares, y el UNICO dominio que cambia vuelve a
ser `core`, porque los CINCO pares que `P.5` volteo (277, 374, 452, 1571 y 1575) son los cinco de
`core`. Medido hoy dominio por dominio (`docs/loop/SALIDA_V36_TASA_DOMINIO.txt`): `core` queda en
`n 1445, A 337 (23,3 por ciento), B 81, C 8, D 1019`. Los otros nueve dominios, identicos al
digito. LA FILA `core` DE LA TABLA DE ARRIBA SIGUE DICIENDO 344 Y NO SE REESCRIBE: es la foto del
13 ago, y reescribirla fabricaria una corrida que nunca existio.** **TERCERA CORRECCION DECLARADA
(18 ago 2026, misma vuelta 36 unas horas despues): tras el `643` el total es `A 575, B 83, C 8,
D 2.722` y `core` queda en `n 1445, A 336 (23,3 por ciento), B 81, C 8, D 1020`
(`docs/loop/SALIDA_V36_TASA_DOMINIO_B.txt`). Los otros nueve dominios, otra vez identicos al
digito.** **CUARTA CORRECCION DECLARADA (19 ago 2026, vuelta 50): el total es hoy `A 573,
B 77, C 8, D 2.730` sobre los mismos 3.388 pares, y el UNICO dominio que cambia vuelve a ser
`core`, porque los CUATRO volteos de la vuelta 49 (806, 844, 263 y 305) son los cuatro de
`core`. Medido hoy dominio por dominio (`../loop/SALIDA_V50_MARCADOR_APERTURA.txt`): `core`
queda en `n 1.445, A 334 (23,1 por ciento)`. Los otros nueve dominios, identicos al digito.
LA FILA `core` DE LA TABLA DE ARRIBA SIGUE DICIENDO 344 Y NO SE REESCRIBE, por el mismo motivo
que la segunda correccion ya escribio: es la foto del 13 ago.** **QUINTA CORRECCION DECLARADA
(19 ago 2026, al CIERRE de la vuelta 50, y ROMPE EL PATRON DE LAS CUATRO ANTERIORES): el total
es hoy `A 571, B 77, C 8, D 2.732`, y el dominio que cambia YA NO ES `core`. Los dos volteos de
la limpieza `P.16` de esta vuelta (los puestos **2222** y **2226**, de `A` a `D`) son los dos de
`health_safety`, que pasa de `A 45` a `A 43` sobre sus 192 pares, de 23,4 a 22,4 por ciento;
`core` se queda quieto en `A 334`. Medido al cierre dominio por dominio
(`../loop/SALIDA_V50_MARCADOR_CIERRE.txt`). **Las cuatro correcciones anteriores decian que el
unico dominio que se movia era `core`; esa frase era cierta cada vez que se escribio y hoy deja
de serlo, y se dice en vez de dejar que el lector la extienda.** **La tasa de quality
cayo de 24,3 % (corte 2.900, acta vuelta 4) a 14,9 % (corte 3.388)** porque los 355 pares que entraron
despues del corte 2.900 en ese dominio son mayoritariamente D: es la figura 9.27 (la cola del dominio se
agota por dentro) actuando sobre el propio quality.

#### b. Actos: 335, con su reparto CERRADOS y ABIERTOS

> **AVISO DE CORTE (18 ago 2026, vuelta 36): las cifras de este apartado son las de la vuelta 14 y
> se citan con su corte, no se remiden aqui. EL DATO VIGENTE ESTA ARRIBA**, en la tercera
> correccion declarada del principio del documento: **333 actos, 279 CERRADOS sobre 598 nodos y 54
> ABIERTOS sobre 247**, con el instrumento re corrido en
> `docs/loop/SALIDA_V36_RECOMPUTO_3388_B.txt`.

**Ya medido en la vuelta 14 con `scripts/plan/recomputo_3388.py` sobre
`docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`: 335 componentes, 280 CERRADOS (sobre 600 nodos: 244 de
dos, 32 de tres, 4 de cuatro) y 55 ABIERTOS (sobre 254 nodos).** Se cita aqui con su corte, no se
remide: es el mismo instrumento y el mismo archivo que la TAREA 1 de esta vuelta ya volvio a verificar
(seccion 2, punto 4 de la vuelta 14 y ACTA_AUDITOR.md VUELTA 14 seccion 1 punto 4).

#### c. Racimos: los trece, cada uno con su nomina y su cobertura remedida (banco 9.26)

**Instrumento: para cada racimo, se generaron los pares posibles (C(n,2)) sobre su nomina vigente y se
cruzaron contra `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`; donde la cobertura declarada no calzaba solo con
la cola, se busco la lectura dirigida en `docs/plan/LECTURAS_DIRIGIDAS.md` o en el expediente de la mesa
correspondiente, y se verifico que esos pares NO estan en la cola (para no contarlos dos veces).**

**Empieza por la supervision de la IA, ya remedida en la TAREA 1 de esta vuelta: 18 de 45 (15 en cola mas
3 lecturas dirigidas del bloque humano fuera de cola), no 10 de 45.**

| racimo | nomina | pares posibles | cobertura remedida al 3.388 | fuente de lo que esta fuera de cola |
|---|---:|---:|---|---|
| el efectivo contra la ganancia | 3 | 3 | 3 de 3 (todo en cola) | ninguna, cobertura completa |
| la ecuacion de valor | 5 | 10 | 10 de 10 (6 A, 4 D): 5 en cola mas 5 lecturas dirigidas | `LECTURAS_DIRIGIDAS.md` linea 408 |
| el sales roadmap | 6 | 15 | 10 de 15 (todo en cola) | ninguna encontrada, cobertura incompleta |
| la competencia entre inversores | 5 | 10 | 7 de 10 (todo en cola) | ninguna encontrada, cobertura incompleta |
| la junta asesora | 4 | 6 | 6 de 6 (4 A, 2 D): 5 en cola mas `LD-01` | `LECTURAS_DIRIGIDAS.md` linea 76 |
| los cuadrantes de mercado | 6 | 15 | 15 de 15 (8 A, 7 D): 7 en cola mas 8 lecturas dirigidas | `LECTURAS_DIRIGIDAS.md` linea 372 |
| build, measure, learn | 8 | 28 | 9 de 28 (todo en cola) | ninguna encontrada, cobertura incompleta |
| el compromiso contado tres veces | 3 | 3 | 3 de 3 (todo en cola) | ninguna, cobertura completa |
| la seleccion de canal | 5 | 10 | 10 de 10 (9 A, 1 D): 8 en cola mas `LD-02` y `LD-03` | `LECTURAS_DIRIGIDAS.md` lineas 95 y 112 |
| **la supervision de la IA** | 10 | 45 | **18 de 45** (8 A, 10 D): 15 en cola mas 3 lecturas dirigidas | TAREA 1 de esta vuelta |
| la mesa unida de puertas y portafolio | 17 | 136 | ~~49 de 136: 23 en cola mas 26 de `LD_MESA_UNIDA.md`~~ **54 de 136 (23 A, 2 B, 2 C, 27 D): 23 en cola mas 31 dirigidas unicas, corregido vuelta 16** | `EXPEDIENTE_MESA_UNIDA.md` linea 291, corregido en TAREA vuelta 16 punto 1 |
| el racimo del pivote | 7 | 21 | 13 de 21 (todo en cola) | ninguna encontrada, cobertura incompleta |
| la serie de Coleman | 28 | 378 | 45 de 378: 41 en cola mas `LD-28` a `LD-31` (4 D) | `EXPEDIENTE_MESA_COLEMAN.md` linea 41 y nota de `INVENTARIO.jsonl` |

~~**RESULTADO: DOCE de los trece racimos VERIFICAN IDENTICOS a la cifra que ya tenia `INVENTARIO.jsonl`,
puesto por puesto y clase por clase, sin que ningun pareto nuevo entrara a sus nominas entre el corte en
que se midieron y el 3.388.** El unico que cambio es **la supervision de la IA**, corregido en la TAREA 1
de esta misma vuelta (10 de 45 falso, 18 de 45 real). El numero de racimos con nombre sigue en **TRECE**:
no aparecio ninguno nuevo ni se fusiono ninguno.~~

**FALSO, CORREGIDO EN LA VUELTA 16 (caida de cifra publicada, ver `docs/loop/ACTA_AUDITOR.md` VUELTA 15
seccion 2 y TAREA vuelta 16 punto 1).** El instrumento de esta tabla cruzaba la nomina contra la cola
mas solo UNO de los cuatro registros `LD_*.md` (`LD_MESA_UNIDA.md`); no sumaba `LD_CADENA.md` ni
`LD_ACTO_DE_SEIS.md`, que traen cinco lecturas mas internas a la mesa unida (`LD-58`, `LD-60`, `LD-61`,
`LD-63`, `LD-64`, ejecutadas el mismo 12 ago 2026). Con el instrumento corregido, **TRECE de trece
racimos verifican identicos a como estaban ANTES de esta vuelta 16**, pero **la mesa unida no era 49 de
136: es 54 de 136** (23 en cola mas 31 dirigidas unicas, 23 A, 2 B, 2 C, 27 D). El numero de racimos con
nombre sigue en **TRECE**: no aparecio ninguno nuevo ni se fusiono ninguno.

#### d. Familias de ids, figuras y defectos: cuales dependen del corte y cuales no

**Familias de ids (53): SU CONTEO NO DEPENDE DEL CORTE DEL CRIBADO.** Cada familia es un cluster de ids
del catalogo que comparten raiz (sufijo, particula u orden), medible directo de los ids en
`master_graph.json` sin abrir ni un veredicto: verificado en esta vuelta que las 53 declaradas siguen
siendo 53 en el archivo (seccion 1). **Lo que SI depende del corte es si cada familia CONTINUA o REPITE
(su fusion), y CORRIJO AQUI MISMO, con tachado, una primera version de esta seccion que daba por
sentado, sin comprobarlo: ~~"ese estado ya esta cubierto por el recomputo de actos del punto (b)"~~.**
Lo comprobe con instrumento propio (interseccion de miembros de cada familia contra los `miembros` de
las 335 componentes de `RECOMPUTO_3388_COMPONENTES.jsonl`) y **NO es cierto para la mayoria**:

| cobertura contra componentes | familias |
|---|---:|
| un solo componente contiene a la familia entera | **23** |
| algun miembro esta en algun componente, pero ninguno los contiene enteros | **14** |
| ningun miembro de la familia aparece en ningun componente | **16** |
| **total** | **53** |

**Para las 23, el estado SI esta cubierto por (b)** (la familia es, literal, el mismo objeto que un
componente). **Para las 30 restantes (14 partidas entre componentes, 16 sin componente alguno), el
estado de fusion NO esta cubierto por (b) y queda SIN REMEDIR esta vuelta**: las 16 sin overlap son,
con este instrumento, ids que no tienen ninguna arista A registrada hoy hacia ningun otro nodo (ni
propio ni ajeno a su familia), y las 14 partidas tienen a sus miembros repartidos en componentes
distintos, lo que sugiere que la familia no es una sola pieza sino dos o mas. **Verificar cual de las
dos lecturas es la correcta, familia por familia, es trabajo de la misma naturaleza que el punto 4 de
abajo (leer y clasificar, no contar) y no se gasta ese alcance aqui: se trae como discutible.** El
conteo de 53 (estructural, seccion 1) no cambia por este hallazgo.

**Defectos (19): NO DEPENDEN DEL CORTE DEL CRIBADO.** Son defectos de estructura del catalogo (alias
huerfanos, campos sucios, injertos de fuente, grafias no canonicas, etc.), contados sobre el grafo y
sobre las operaciones de saneamiento (`OP-S-*`) ya ejecutadas; ninguno de los 19 se mide leyendo pares.
**Se declara: NO se remiden, por no depender del corte.** El conteo de 19 (contra los 14 de la nota
vieja) es la unica correccion que les toca, y es de archivo desactualizado, no de cribado (seccion 1).

**Figuras (20): SI DEPENDEN DEL CORTE DEL CRIBADO, y NO se remiden esta vuelta.** Las figuras de lectura
(SUBCONJUNTO ESTRICTO, ESTRELLA, banco 9.22, 9.23, 9.27, P.2, P.4, etc.) cuentan "ejemplares": pares
concretos cuya razon de veredicto encaja en el patron. Doce de las veinte tienen `fecha_corte` 2026-08-11
(el corte viejo, 2.117) y el cribado sumo 1.271 pares desde entonces (183 de ellos A). **Probe un
instrumento mecanico** (grep del nombre de cada figura sobre el campo `razon` de las 3.388 lineas) **y lo
DESCARTO como cifra publicable**: da conteos que NO calzan con los "ejemplares" declarados en ningun
sentido fiable (por ejemplo ESTRELLA da 17 menciones de la palabra contra 9 ejemplares declarados, y
TRIANGULO ABIERTO da 0 contra 2 declarados), porque el patron no se decide por si el texto NOMBRA la
figura sino por si el PAR CALZA con su forma, que es juicio sobre el contenido del par, no conteo de
palabra. **Remedir las veinte con fidelidad exige releer y clasificar contra cada patron los pares nuevos
desde su corte, trabajo de la misma escala que la regeneracion de actos del punto 4 de abajo: no se
gasta ese alcance sin que se encargue.** Se trae como PENDIENTE DE MEDICION, no como cifra: el conteo de
20 figuras-tipo (contra las 12 de la nota vieja) SI se corrige en la seccion 1 porque es conteo de filas
del archivo, no de ejemplares.

### 3. EL TOTAL NUEVO, con las dos cifras viejas al lado y sin fusion oculta

| total | cifras | corte |
|---|---:|---|
| la nota vieja de `OP-I-01` | 323 (221 actos, 53 familias, 14 defectos, 13 racimos, 12 figuras, 10 dominios) | 2026-08-11, puesto 2.117 |
| el archivo medido hoy, tal cual esta escrito | 336 (221 actos, 53 familias, 19 defectos, 13 racimos, 20 figuras, 10 dominios) | 2026-08-13, sin corregir la cifra de actos |
| **EL TOTAL NUEVO, recomputado al corte 3.388** | **450** (**335** actos, 53 familias, 19 defectos, 13 racimos, 20 figuras, 10 dominios) | **2026-08-13, corte 3.388** |

**El total nuevo (450) sustituye SOLO la cifra de actos (221 a 335) sobre el archivo medido hoy (336);
los otros cinco sumandos no cambian de conteo porque no dependen del corte del cribado (seccion 2.d).**
**Parte que NO se midio dentro de este total: los "ejemplares" internos de las veinte figuras** (su
conteo-de-filas si esta en el 450, pero cuantos ejemplares tiene cada una no se remidio, seccion 2.d).
**El total de 450 no incluye entradas nuevas escritas al archivo: las 335 lineas de tipo acto NO se
regeneraron (punto 4).**

### 4. DISCUTIBLE MARCADO: el PLAN de regenerar las 221 entradas de tipo `acto`, sin ejecutar

**No se regeneran esta vuelta, por instruccion expresa del encargo. El plan, para que el auditor lo
adjudique:**

- **Que campos llevaria cada una de las 335 entradas nuevas**, calcados de la unica entrada de tipo
  `acto` que hoy existe (`nombre`, `miembros`, `forma`, `cobertura`, `estado`, `operaciones`,
  `fecha_corte`, `nota`). **Dos campos no salen directo de la fuente y hay que derivarlos**: `nombre`
  (hoy es el id del primer miembro; `RECOMPUTO_3388_COMPONENTES.jsonl` no trae nombre, solo `miembros`) y
  `operaciones` (hoy es una busqueda cruzada contra las nominas de las 69 operaciones de
  `OPERACIONES.jsonl`, no un campo del archivo de componentes).
- **De que instrumento sale cada campo**: `miembros`, `tamano`/`posibles`/`leidos`/`en_cola_sin_leer`/
  `fuera_de_cola`/`clases_internas`/`estado` vienen literales de
  `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`; `cobertura` se arma con esos cinco numeros en el formato
  de texto que ya usan las 221 entradas viejas; `operaciones` exige el cruce nuevo contra
  `OPERACIONES.jsonl` descrito arriba; `nota` no tiene fuente mecanica y quedaria vacia o generica si no
  se escribe a mano.
- **Cuantas lineas se escriben y se borran**: se BORRAN 221 lineas de tipo `acto` y se ESCRIBEN 335,
  **neto +114 lineas** en `docs/plan/INVENTARIO.jsonl`; `docs/plan/10_INVENTARIO.md` (la vista humana)
  tambien cambiaria su tabla de actos si la trae completa (no se verifico si la trae hoy, fuera de
  alcance de este plan).
- **Que citas de otros documentos se romperian**: ninguna cita textual por nombre de acto especifico se
  encontro en la busqueda de esta vuelta (`grep` de "221 actos"; ocho archivos citan la CIFRA, ninguno
  cita un `nombre` de acto individual de la lista vieja como si fuera a seguir existiendo). **El riesgo
  no es de citas rotas: es de que la nota `nota` de las 221 entradas viejas (texto escrito a mano en
  algunos casos) se pierda si se sobrescribe sin copiarla.**
- **Cuanto cuesta**: generar los 335 registros con los cinco campos mecanicos es un script corto (minutos);
  el cruce `operaciones` contra 69 nominas es mecanico tambien pero mas lento (recorrer 335 por 69); el
  campo `nota` no tiene atajo mecanico honesto y, si se quiere con el mismo nivel de detalle que las 221
  viejas, es trabajo de lectura y redaccion por acto, la misma escala que escribir 335 fichas cortas.

**No se decide aqui: se trae la pregunta, igual que el discutible de `OP-L-03` en la vuelta 14.**

---

## TAREA (vuelta 16): registro de las cinco adjudicaciones y regeneracion de las 335 entradas de tipo `acto`

**Las cinco adjudicaciones de `docs/loop/ACTA_AUDITOR.md` VUELTA 15 seccion 6, registradas cada una donde
corresponde, con su cita:**

1. **La cobertura de la mesa unida se corrige a 54 de 136** (adjudicacion 6.1). Ejecutado en TAREA vuelta
   16 punto 1: tachado sin borrar el 49 en `docs/plan/INVENTARIO.jsonl`, `docs/plan/10_INVENTARIO.md`,
   `docs/plan/OPERACIONES.jsonl` (nota de `OP-M-01`), `docs/plan/EXPEDIENTE_MESA_UNIDA.md`,
   `docs/plan/LD_MESA_UNIDA.md`, `docs/plan/LECTURAS_DIRIGIDAS.md` y en la tabla de los trece racimos de
   esta misma seccion (linea 847 de esta version).
2. **El bloque humano de la IA se corrige a 5 A y 5 D** (adjudicacion 6.2). Ejecutado en TAREA vuelta 16
   punto 1: tachado sin borrar en `docs/plan/LECTURAS_DIRIGIDAS.md` (lineas 440 y 465), en la nota de
   `OP-L-02` de `docs/plan/OPERACIONES.jsonl`, y en la seccion de esta misma pagina que copiaba el "7 A y
   3 D" (lineas 638 a 642).
3. **La regeneracion de las entradas de tipo `acto` se aprueba con cinco condiciones** (adjudicacion 6.3).
   Ejecutada de punta a punta abajo, seccion siguiente.
4. **El estado de fusion de las 53 familias se publica en tres cubetas con nombre** (adjudicacion 6.4).
   Publicado en la seccion de mas abajo, "LAS TRES CUBETAS DE LAS 53 FAMILIAS".
5. **Los ejemplares de las veinte figuras quedan como el ultimo bloque grande de la FASE II** (adjudicacion
   6.5). **REGISTRADO AQUI FORMALMENTE**: junto al lote de cinco del sales roadmap, la cola de relectura
   post fusion, el criterio del forastero y las lecturas de acto entero de P.5, **la FASE II no cierra sin
   los ejemplares de las veinte figuras remedidos, o sin que el fundador los difiera por escrito.** Nada
   nuevo se mide aqui sobre las figuras: siguen PENDIENTES DE MEDICION (seccion TAREA vuelta 15, punto
   2.d), el grep queda descartado como instrumento (discutible 3 adjudicado), y remedirlas exige releer y
   clasificar cada patron contra los pares nuevos desde su corte.

### 1. Condicion (a): la busqueda de los 221 nombres viejos por el repo, con script

**Instrumento: `scripts/vuelta16_buscar_actos.mjs` y `scripts/vuelta16_buscar_actos2.mjs`, ambos de solo
lectura, corridos sobre `git ls-files` (7.468 archivos rastreados, menos `INVENTARIO.jsonl`).**

**Primer barrido, sobre TODO el repo:** los 221 nombres aparecen citados **los 221 de 221**, porque cada
`nombre` de acto ES literalmente el id de un nodo real del catalogo, y por eso aparece de forma trivial en
`dataset/`, `packs/`, `engine/`, `web/` (el nodo existe ahi, no el acto) y en los archivos mecanicos del
cribado (`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `docs/FRANJA_*`, `docs/GRADIENTE_*`, que listan el nodo
como miembro de un par, no como acto). **Ese barrido no distingue nada: da 221 de 221 pase lo que pase, asi
que no es la pregunta util.**

**Segundo barrido, acotado a la CAPA NARRATIVA de planeacion** (`docs/plan/*.md`, `docs/loop/*.md`,
`docs/BANCO_DE_TEXTOS.md`, y `docs/plan/OPERACIONES.jsonl`; fuera del barrido `INVENTARIO.jsonl`,
`RECOMPUTO_3388_COMPONENTES.jsonl` y los cuatro jsonl mecanicos de pares/razones que solo listan miembros),
que es donde tendria sentido citar un acto como objeto que sigue existiendo: **81 de 221 nombres aparecen**,
casi todos dentro de `OPERACIONES.jsonl` (como miembro de la nomina `nodos` de una operacion) y de los
expedientes de mesa (`EXPEDIENTE_MESA_*.md`, `LD_*.md`). **Ninguna de las 81 citas es una cita AL ACTO
COMO OBJETO DE INVENTARIO por su nombre compuesto**: todas citan al NODO individual dentro de una nomina
mas amplia (una operacion, una mesa, un racimo), que es justo lo que las cinco condiciones de la
adjudicacion 6.3 protegen sin necesidad de tocar ninguna de esas citas, porque **ningun nodo se borra, se
renombra ni cambia de id.** Lista completa de los 81, con sitio y conteo, en
`scripts/_actos_citas_narrativa.json`. **Si alguna cita asumiera que el acto viejo especifico (con esa
composicion y ese id de acto) sigue existiendo tal cual, no se toca sin decirlo**, pero no se encontro
ninguna con esa forma: las citas son siempre al nodo, nunca al acto-registro.

### 2. Condiciones (b) a (f): el metodo, y un hallazgo que cambia el alcance de (b) y (c)

**Instrumento: `scripts/vuelta16_generar_actos.mjs`, de solo lectura sobre
`docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` (335 componentes al corte 3.388) y sobre las 221 entradas
viejas de `INVENTARIO.jsonl`.**

**Mapeo de sucesion, medido antes de escribir nada:** para cada uno de los 221 actos viejos se busco el
componente de `RECOMPUTO_3388_COMPONENTES.jsonl` cuyo `miembros` CONTIENE enteros a los miembros del acto
viejo (superset). **Resultado: los 221 de 221 tienen exactamente UN sucesor, y ninguno tiene mas de uno.**
Dicho de otro modo: **la componente conexa nunca se parte entre el corte 2.117 y el 3.388** (esperable,
porque las aristas A solo se agregan, nunca se retiran, asi que un componente solo puede crecer o quedarse
igual). **De los 221, 220 son identicos en tamano y 1 crecio** (~~`construccion_de_leverage`, la
"competencia entre inversores", de 4 a 5 miembros, ya documentado en la ficha del racimo~~
**`gestion_terminacion_franquiciado`, de 2 a 3 miembros, ganando `perdida_control_operativo`**).

> **CORRECCION DECLARADA, vuelta 17, 14 ago 2026. LA CAIDA ES DEL EJECUTOR, no del auditor ni del
> archivo.** El conteo "220 identicos y 1 crecio" siempre estuvo bien; **el NOMBRE se copio de una nota
> vieja de otro objeto y de otra epoca en vez de leerse de la salida del instrumento que acababa de
> correr.** Es la misma especie de fallo que la caida de la vuelta 15 (banco 9.10 y regla 1 de
> `docs/loop/EJECUTOR.md`, adoptada por esta caida): el instrumento corriendo y la afirmacion saliendo
> de otro sitio.
>
> **LA FUENTE CORRECTA YA ESTABA ESCRITA EN EL PROPIO PLAN, y no se leyo:** la nota de `OP-U-02` en
> `docs/plan/OPERACIONES.jsonl` dice, con esas palabras, *"CUARENTA Y DOS siguen abiertos identicos y
> UNO crecio (`gestion_terminacion_franquiciado` con `terminacion_franquiciado_causas`, de 2 a 3)"*.
>
> **REMEDIDO EN LA VUELTA 17 CON INSTRUMENTO PROPIO, no copiando la cifra del acta del auditor:**
> `scripts/loop/vuelta17_acto_que_crecio.py`, de solo lectura, con **tres metodos independientes que
> tienen que coincidir o se declara la discrepancia**: (A) superset de los 221 viejos contra
> `RECOMPUTO_3388_COMPONENTES.jsonl`; (B) superset contra las 335 entradas nuevas de tipo `acto` del
> propio `INVENTARIO.jsonl`, que es el mismo hecho por otra ruta de datos; (C) sin superset, por
> pertenencia nodo a componente al corte 3.388, preguntando el tamano de hoy de la componente que
> contiene al primer miembro de cada acto viejo. **Los tres dan 220 identicos, 1 que crecio, cero sin
> sucesor y cero con mas de un sucesor, y los tres nombran a `gestion_terminacion_franquiciado`, de 2
> a 3, ganando `perdida_control_operativo`.** Control previo del metodo C: los 335 componentes cubren
> 854 nodos distintos con **cero** nodos en dos componentes a la vez.
>
> **Y el contraste con el nombre caido, medido y no supuesto: `construccion_de_leverage` tiene CINCO
> miembros en los dos cortes y no tuvo cuatro en ninguno de los dos.** La cifra "de 4 a 5" no describe
> a ningun objeto de este archivo en ninguno de los dos cortes.
>
> **HALLAZGO DE PASO, que no se pidio y se declara porque toca una formula viva:** la nota vieja de
> `gestion_terminacion_franquiciado` decia literalmente *"tamano 2. Sin pares pendientes: no puede
> crecer"*, **y crecio.** La formula mecanica no miente sobre lo que mide (los pares INTERNOS del
> acto, que en efecto no quedaban pendientes) pero su frase **"no puede crecer" promete mas de lo que
> mide**: una componente tambien crece cuando un nodo de FUERA entra por una arista A nueva, que es
> exactamente lo que paso aqui. **Esa misma frase se sigue escribiendo hoy en las 335 entradas
> nuevas.** Va como PENDIENTE DE DOCTRINA al reporte de esta vuelta; no se toca ninguna nota, porque
> reescribir la formula de 335 entradas no es una correccion, es una regeneracion.

**Esto cambia el alcance de la condicion (c): NINGUNA de las 221 entradas viejas queda "sin componente
sucesor".** La condicion (c) esta escrita para el caso que no aparecio: se declara medido, no se fuerza.
**Y esto tambien acota la condicion (b):** de las 221 notas viejas, **220 son la MISMA formula mecanica**
("tamano N. Sin pares pendientes: no puede crecer." o "tamano N. Puede crecer: X en cola y Y fuera de
cola."), medido por conteo de valores distintos (22 notas unicas sobre 221 filas, y de esas 22 solo
UNA no sigue la formula). **La UNICA nota escrita a mano de las 221 es la de `formalizar_junta_asesora`**
(la junta asesora, la decision de fusion en dos con enlace, `OP-M-04`), y es esa la que viaja.

**Condicion (a) de las cinco, NADA SE BORRA: se cumple por construccion.** Las 221 lineas viejas de
`INVENTARIO.jsonl` **no se tocan, no se editan, no se borran**: siguen exactamente como estaban, con su
`fecha_corte` de 2026-08-11 intacta. **Se ANADEN 335 lineas nuevas**, una por componente del corte 3.388,
en vez de sobrescribir las 221: es la lectura mas literal de "nada se borra" y de "no se borra ni una linea
del archivo" (condicion c), y es MAS estricta que el plan original de la vuelta 15, que proponia BORRAR las
221 y escribir 335 (discutible 4 de esa vuelta, "se BORRAN 221 lineas... y se ESCRIBEN 335"). **La
condicion (a) de la adjudicacion deroga esa parte del plan viejo: no se borra ninguna.**

**Condicion (d), la convencion de `nombre`: verificada antes de usarla, no supuesta.** Sobre las 221
viejas, `nombre` es SIEMPRE el primer elemento de `miembros`, y `miembros` esta SIEMPRE ordenado
alfabeticamente (221 de 221 en los dos chequeos). `RECOMPUTO_3388_COMPONENTES.jsonl` tambien trae sus 335
`miembros` ordenados alfabeticamente (335 de 335). **La convencion es la misma y se aplica igual: `nombre`
= primer id alfabetico de `miembros`.** No hizo falta inventar ninguna.

**Condicion (e), `nota` no se inventa:** las 335 entradas nuevas llevan la MISMA formula mecanica de
cobertura que usaban las 220 viejas normales (calculada de `leidos`/`posibles`/`en_cola_sin_leer`/
`fuera_de_cola`), mas una linea de procedencia ("REGENERADO EN LA VUELTA 16..."). **Las 114 sin antecesor
en los 221** llevan ademas la linea "Sin antecesor... Nota no inventada: hueco nombrado, no rellenado." **La
unica que lleva prosa mas alla de la formula es la sucesora de `formalizar_junta_asesora`, que carga la
nota vieja completa, sin tocarla, con su corte viejo (2026-08-11) al lado.**

**Condicion (f), campos mecanicos:** `miembros`, `forma`, `cobertura` y `estado` salen literales de
`RECOMPUTO_3388_COMPONENTES.jsonl` (`tamano`, `posibles`, `leidos`, `en_cola_sin_leer`, `fuera_de_cola`,
`estado` CERRADO/ABIERTO), en el mismo formato de texto que usaban las 221 viejas (verificado char a char
contra dos ejemplos, uno CERRADO y uno ABIERTO). **`operaciones` es el cruce contra las 69 nominas de
`OPERACIONES.jsonl`, y el metodo se VERIFICO antes de aplicarse**, reproduciendo el campo `operaciones` de
los 221 viejos con su propia nomina vieja: **189 de 221 identicos**, y las 32 diferencias tienen motivo
medido, no error: 5 son actos que CERRARON entre el 2.117 y el 3.388 (los mismos cinco que nombra la nota
de `OP-U-01`, confirmado uno a uno), y el resto son operaciones-hijas creadas DESPUES de que la entrada
vieja se escribiera (`OP-M-02-*`, `OP-M-03-*`, `OP-M-01-ESLABONES`, `OP-E-04`, `OP-E-05`, etc.), que
nunca se pudieron reflejar en un campo que no se toca desde el 11 ago 2026 (banco 9.21, la cifra vieja no
se actualiza sola). **El metodo: `operaciones` de un componente es la union de a) todo `id_op` cuyo
`nodos` (de las 44 de 69 operaciones que lo traen poblado) comparte AL MENOS UN miembro con el componente;
b) `OP-U-01` si el componente esta CERRADO o `OP-U-02` si esta ABIERTO (las dos son universales por su
propia adjudicacion, verificado que las 221 viejas las llevan sin excepcion segun su estado de entonces);
c) `OP-L-03` si el componente esta en el backlog de 40 actos y 73 pares ya adjudicado en la vuelta 14
(recalculado aqui con el mismo metodo de `scripts/loop/backlog_l03_vuelta14.py`, y da EXACTAMENTE 40
actos y 73 pares, identico al adjudicado).**

**LO QUE NO SE REPRODUJO, declarado y no escondido:** el cruce de (a) no intenta reconstruir por que
narrativa una operacion `DESTEJIDO` o `DECISION_DE_FUENTE` especifica toca un nodo mas alla de su campo
`nodos`; se tomo el campo `nodos` tal cual esta escrito en `OPERACIONES.jsonl`, sin reinterpretarlo. Si ese
campo esta incompleto en alguna operacion vieja, el cruce hereda esa incompletud, pero no la agrava: es el
mismo campo que ya gobernaba el `operaciones` de las 221 entradas viejas.

### 3. Ejecutado: 335 entradas nuevas ANADIDAS a `docs/plan/INVENTARIO.jsonl`

**Las 335 lineas de tipo `acto` estan escritas al final del archivo** (despues de las 336 que ya habia),
con `fecha_corte` 2026-08-13 (el corte 3.388, no la fecha de hoy). **221 son sucesoras de una entrada
vieja (con su nota mecanica recalculada, y la de `formalizar_junta_asesora` con su nota vieja transplantada);
114 son componentes nuevas que no existian como acto en el corte 2.117.**

**MEDIDO EL ARCHIVO OTRA VEZ por campo `tipo`, tras la escritura:**

| tipo | antes de esta vuelta | **despues** |
|---|---:|---:|
| dominio | 10 | 10 |
| acto | 221 | **556** (221 viejos intactos mas 335 nuevos) |
| racimo | 13 | 13 |
| familia_de_ids | 53 | 53 |
| figura | 20 | 20 |
| defecto | 19 | 19 |
| **TOTAL** | **336** | **671** |

**EL TOTAL REAL NO ES 450, y el motivo NO es la condicion (c) (cero entradas superadas sin sucesor,
seccion 2 de arriba): es la condicion (a).** El 450 de la vuelta 15 se proyecto asumiendo REEMPLAZO (borrar
221, escribir 335: 335+53+19+13+20+10=450). **La adjudicacion 6.3 aprobo la regeneracion con la condicion
"nada se borra", que prohibe ese reemplazo**: el archivo no sustituye, ANADE. El total real, con los 336
viejos y los 335 nuevos ambos vivos, es **671** (556 actos, 53 familias, 19 defectos, 13 racimos, 20
figuras, 10 dominios). **Ninguna cifra vieja se borra: el 323, el 336 y el 450 siguen escritos arriba, y
el 671 se suma al lado, no los reemplaza.** No se cuadra el numero a la fuerza, tal como pide el punto (g)
del encargo.

**DISCUTIBLE MARCADO: `docs/plan/10_INVENTARIO.md` (la vista humana) NO se toco.** Su propia regla dice
"se recomputa entero con el disparador de `08_VERIFICACION`", y esa vista trae hoy la tabla de actos al
corte 2.117 (221, con reparto por tamano). Con 556 actos vivos en el archivo fuente, esa vista queda
desactualizada por partida doble (corte y cifra), pero regenerarla entera es un trabajo de la escala de
`08_VERIFICACION`, no de esta TAREA. **Se trae como pregunta, no se toca sin decirlo.**

### 4. LAS TRES CUBETAS DE LAS 53 FAMILIAS, publicadas con nombre (adjudicacion 6.4)

**Sin leer ni un par, por interseccion de miembros contra los 335 componentes de
`RECOMPUTO_3388_COMPONENTES.jsonl` (el archivo original de 335, no las 335 lineas nuevas de acto que son
la misma informacion en otro formato):**

| cubeta | cuantas | familias |
|---|---:|---|
| **CONTENIDAS** (un solo componente contiene a la familia entera) | **23** | `defensas_en_profundidad`, `dia_cero_defectos`, `distincion_causas_comunes_especiales`, `ciclo_de_culpa`, `conciencia_calidad`, `confusion_de_modos_automatizacion`, `contacto_con_el_cliente`, `control_estadistico_de_procesos`, `critica_eco_eficiencia`, `definicion_problema_moms`, `descubrir_necesidades_cliente`, `design_for_six_sigma_dmadv`, `diversidad_vs_homogeneidad_equipo`, `drift_hacia_el_fallo`, `equipo_mejora_calidad`, `estilo_gerencial_ballet_vs_hockey`, `estructura_de_gates`, `evitar_greenwashing`, `medicion_calidad`, `obtencion_compromiso`, `secuencia_universal_breakthrough`, `sesgo_retrospectivo_hindsight`, `six_sigma_dmaic` |
| **PARTIDAS** (miembros repartidos en componentes distintos, ninguno los contiene enteros) | **14** | `accion_correctiva`, `consejo_calidad`, `definiciones_operacionales`, `cultura_justa`, `eliminacion_causas_error`, `estrategia_de_innovacion_de_producto`, `control_estadistico_del_proceso`, `customer_development_modelo`, `eco_efectividad`, `plan_de_gestion_de_riesgos`, `proteccion_propiedad_intelectual`, `regla_todo_o_nada_inspeccion`, `responsabilidad_extendida_productor`, `storytelling_como_herramienta_de_diseno` |
| **SIN ARISTA A** (ningun miembro aparece en ningun componente al corte 3.388) | **16** | `make_certain_programa`, `auditoria_de_producto`, `capacidad_de_proceso`, `clasificacion_de_seriedad_de_defectos`, `ciclo_ventas_calidad_franquicia`, `costo_de_calidad`, `desarrollar_caracteristicas_proceso`, `dialogo_con_stakeholders`, `establecer_vision_organizacional`, `planificacion_de_la_inspeccion`, `planificacion_estrategica_despliegue`, `reduccion_de_tiempo_de_ciclo`, `sistema_responsabilidad_gerencial`, `triple_bottom_line`, `validacion_sistema_medicion`, `velocidad_crecimiento_franquicia` |
| **total** | **53** | |

**ESTO ES EL ESTADO, no la falta de estado (adjudicacion 6.4).** Lo que queda abierto, si alguna de las 14
PARTIDAS es de verdad dos familias distintas, **es materia de mesa, no de recomputo**: se deja escrito
como tal, no como medicion pendiente.

### 5. La nota de `OP-I-01`, puesta al dia

**Actualizada en `docs/plan/OPERACIONES.jsonl`** con: la correccion de etiqueta del punto 2.d (TAREA vuelta
16 punto 3 de este mismo documento), y el nuevo total real de 671 con su motivo (regeneracion aditiva, no
reemplazo), citando esta seccion.

---

**DISCUTIBLES DE ESTA TAREA, marcados para la relectura ciega:**

1. **La lectura de "nada se borra" como ADITIVA (335 lineas nuevas conviviendo con las 221 viejas) en vez
   de IN-PLACE (actualizar las 221 en su sitio, preservando el valor viejo por tachado, como se hace en el
   resto de este documento).** Las dos lecturas cumplen "no se borra texto"; la elegida es la mas literal
   ("no se borra ni una linea del archivo", condicion c) y la mas auditable (diff de solo altas), pero
   duplica informacion (556 actos describen 335 componentes reales) y deja la vista humana desactualizada.
   Si el auditor prefiere la lectura in-place, se revierte el append y se reescribe como actualizacion de
   las 221 lineas existentes.
2. **El campo `operaciones` de las 335 nuevas no reproduce las operaciones DESTEJIDO/FUENTE que no tienen
   el nodo relevante en su campo `nodos`** (si alguna lo tiene incompleto). Se declara, no se investigo
   operacion por operacion si su `nodos` esta completo.
3. **`10_INVENTARIO.md` no se toco.** Queda desactualizado por partida doble frente al archivo fuente.

---

## TAREA (vuelta 17): las cuatro correcciones, las dos costuras con dueno, y la FASE II medida bloque por bloque

**Corte de todas las cifras de esta seccion: 14 ago 2026, sobre el cribado CERRADO en 3.388 de 3.388.**
**MODO DE CIERRE: cero reparaciones de nodos, cero operaciones ejecutadas, cero pares nuevos leidos.**
`dataset/` intacto y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` intacto en sus 3.388 lineas.

Los puntos 1 a 4 del encargo estan ejecutados arriba, cada uno en su sitio y con su tachado: la caida
del acto que crecio (seccion "TAREA vuelta 16", punto 2), las 221 lineas marcadas como superadas
(`docs/plan/INVENTARIO.jsonl`), el aviso de la vista humana (`docs/plan/10_INVENTARIO.md`) y el hueco
nombrado del campo `operaciones` (nota de `OP-I-01`). Las dos costuras con dueno estan en la seccion
TAREA 2.B punto 4, con su tachado. **Lo que sigue es el punto 5: seguir la FASE II por donde estaba.**

### 1. Que se midio, con que instrumento, y que NO se cerro

**Instrumento: `scripts/loop/vuelta17_fase2_pendiente.py`, de solo lectura**, sobre
`docs/plan/INVENTARIO.jsonl`, `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `docs/plan/OPERACIONES.jsonl` (las
71) y `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`.

**LA FASE II NO CIERRA EN ESTA VUELTA, y se dice antes de dar ninguna cifra.** De los cinco bloques que
le faltaban, **dos quedan VERIFICADOS ENTEROS, uno queda NOMBRADO, uno queda CUANTIFICADO EXACTO y el
grande queda MEDIDO EN TAMANO pero sin cerrar**, porque cerrarlo es trabajo de lectura y el `grep` quedo
descartado como instrumento en la vuelta 15.

| bloque | antes de esta vuelta | despues |
|---|---|---|
| la cola de relectura post fusion | siete pares declarados, sin verificar contra el corte 3.388 | **VERIFICADA ENTERA, 7 de 7** |
| el criterio del forastero | dos ejemplares declarados "con todas sus lecturas hechas" | **VERIFICADOS LOS DOS** |
| el lote de cinco del sales roadmap | "cinco pares", sin nomina en ningun sitio | **LOS CINCO NOMBRADOS** |
| las lecturas de acto entero de P.5 | una condicion escrita, sin cifra | **CUANTIFICADA: 280 hechos, 55 pendientes, 329 pares** |
| los ejemplares de las veinte figuras | PENDIENTES DE MEDICION | **medido el tamano, NO cerrado** |

### 2. La cola de relectura post fusion: VERIFICADA ENTERA, 7 de 7

**La nomina existe y no habia que buscarla en prosa:** esta en `docs/plan/08_VERIFICACION.md` (tabla
"LA LISTA, barrida el 12 ago 2026 sobre las diecisiete fusiones del plan") y repetida en la entrada de
tipo `defecto` "pares que una fusion reabre" de `docs/plan/INVENTARIO.jsonl`. Los siete puestos son
**707, 1096, 196, 253, 224, 591 y 968**, y **una cae, el 751**.

**REMEDIDO CONTRA EL ARCHIVO Y CONTRA EL PLAN DE 71 OPERACIONES, no copiado de la tabla:**

| puesto | clase hoy | su disparador, comprobado en `OPERACIONES.jsonl` | verifica |
|---:|:--:|---|:--:|
| **707** | **B** | `customer_discovery_overview` esta en el `eliminar` de `OP-M-05-INDICE`: MUERE | si |
| **1096** | **A** | su contraparte `filosofia_customer_validation` esta en el `eliminar` de `OP-M-05-APERTURA`: MUERE | si |
| **196** | **B** | `fase_acclimate_mapa_de_proceso` esta en el `eliminar` de `OP-M-02-ACCLIMATE`: MUERE | si |
| **253** | **B** | `fase_acclimate_experiencia_cliente` esta en la nomina de `OP-M-02-ACCLIMATE` y NO en su `eliminar`: sobrevive y CAMBIA DE TEXTO | si |
| **224** | **B** | `fase_assess_ciclo_cliente`, mismo patron en `OP-M-02-ASSESS` | si |
| **591** | **B** | `pivote_estrategico`, mismo patron en `OP-M-03-III` | si |
| **968** | **B** | `pivote_o_proceder`, mismo patron en `OP-M-03-II` | si |

**Y LA QUE CAE TAMBIEN SE VERIFICA, porque una baja declarada tambien se comprueba:** el puesto **751**
(`customer_validation_sell_phase` contra `verificar_product_market_fit`, B) sale de la lista porque su
nodo ya no muere. **Medido: NINGUNA de las 71 operaciones tiene `customer_validation_sell_phase` en su
campo `eliminar`.** La baja es correcta.

**UNA DIFERENCIA ENTRE DOS SITIOS QUE DICEN LO MISMO, declarada y NO arreglada aqui.** La entrada de
tipo `defecto` escribe la regla del disparador asi: *"Solo los B y los C: un D dice que los dos son
sanos... un A ya esta resuelto"*, **y a continuacion lista un A, el 1096.** Leida sola, esa entrada se
contradice. **NO es una contradiccion del plan: es que la entrada no carga la excepcion, que si esta
escrita en `08_VERIFICACION.md` con su motivo** (*"su contraparte muere y su A se volveria contradiccion
con su propia D"*) y en `00_INDICE.md` con las mismas palabras. **Los dos documentos juntos son
consistentes; la entrada sola no.** Se trae como pregunta al reporte y no se toca: la fuente de la
nomina es `08_VERIFICACION.md`, y esa esta completa.

### 3. El criterio del forastero: los DOS ejemplares verificados

**La figura declara "dos ejemplares, y los dos casos con todas sus lecturas hechas".** Remedido:

| ejemplar | lo que dice la figura | lo medido en la vuelta 17 |
|---|---|---|
| `tacticas_cierre_ventas` | *"seis lecturas, una sola contra miembros del cierre y sale D, y su unica A es con un nodo que no es del cierre"* | **SEIS pares en el cribado: 1 A y 5 D.** Su unica A es el puesto **221**, contra `compromiso_linea_tiempo_cliente` |
| `incentivos_no_monetarios_advocacy` | *"CUATRO lecturas contra la serie y LAS CUATRO D"* | **CERO pares en el cribado** |

**Ese CERO es la clase de busqueda negativa que no se puede citar sin re-verificarla (regla 8 del
ejecutor), asi que se re-verifico: NO es un hueco.** Sus lecturas **no son del cribado, son DIRIGIDAS**,
y viven en `docs/plan/LD_ADOPT_ADVOCATE.md`: **`LD-28`, `LD-30` y `LD-31`, las tres D**, mas su cruce.
**Un instrumento que solo mire `INTRA_DOMINIO_VEREDICTOS.jsonl` lo daria por no leido, y estaria mal.**
Queda escrito para que no se vuelva a levantar como hallazgo falso.

### 4. El lote de cinco del sales roadmap: LOS CINCO, NOMBRADOS por primera vez

**El plan los contaba** (`00_INDICE.md`: "cinco pares"; `LECTURAS_DIRIGIDAS.md`, el backlog documentado)
**pero no los nombraba en ningun sitio.** Calculados aqui de la nomina de seis nodos del racimo (15
pares posibles) menos los 10 con veredicto:

| el par que falta |
|---|
| `customer_validation_sales_roadmap` contra `estrategia_de_ventas` |
| `customer_validation_sales_roadmap` contra `sales_roadmap` |
| `estrategia_de_ventas` contra `hoja_de_ruta_de_ventas` |
| `estrategia_de_ventas` contra `refinar_sales_roadmap` |
| `estrategia_de_ventas` contra `sales_roadmap_vs_sales_force` |

**Los diez que si estan, con su clase, remedidos: 6 A y 4 D** (192 A, 200 A, 255 A, 319 A, 872 D, 918 A,
966 A, 1023 D, 1306 D, 1330 D). **Calza exacto con la tabla de los trece racimos de la vuelta 16.**

> **LO QUE LA NOMINA ENSENA Y EL CONTEO ESCONDIA, y no se pidio: los cinco que faltan no estan
> repartidos por el racimo. CUATRO DE LOS CINCO CUELGAN DEL MISMO NODO, `estrategia_de_ventas`**, que
> tiene **uno solo de sus cinco pares leido** (el 966, A contra `sales_roadmap`).
>
> **Esto NO desmiente el motivo escrito para no leerlos** (*"su clase ya esta decidida: MEZCLADO desde
> el 872. Leerlos cierra cobertura, no cambia forma"*), **y hay que decir por que no lo desmiente:** es
> cierto que leerlos no puede mover la clase del racimo. **Pero la pregunta de P.5 no es la clase del
> racimo: es si el acto es UNA familia o DOS**, y esa pregunta, en este acto, se contesta entera
> leyendo los cuatro pares de un solo nodo. **Son dos preguntas distintas sobre los mismos cinco pares,
> y el plan solo tenia escrita la respuesta a una.** Se trae como pregunta, no se decide.

### 5. Las lecturas de acto entero de P.5: cuantificadas, y con una consecuencia que no estaba escrita

**P.5 dice que cada acto que vaya a fundirse se lee ENTERO antes de fundirse.** Hasta hoy era una
condicion sin cifra. Medida sobre las 335 componentes del corte 3.388:

| | |
|---|---:|
| componentes con **TODOS** sus pares leidos, o sea **P.5 ya es un HECHO** | **280** |
| componentes con pares sin leer, o sea **P.5 sigue siendo una CONDICION** | **55** |
| **pares que faltan por leer en total** | **329** |
| de esos 329, los que estan **EN COLA** sin leer | **0** |
| de esos 329, los que estan **FUERA DE COLA** | **329** |

**Los 55 son exactamente los 55 actos ABIERTOS** y los 280 exactamente los 280 CERRADOS: las dos
particiones coinciden componente por componente, no es casualidad de conteo.

> **LA CONSECUENCIA, que es lo que esta cuenta aporta y no estaba escrita en ninguna parte: LOS 329
> PARES QUE LE FALTAN A P.5 ESTAN TODOS FUERA DE COLA. CERO en cola.** Con el cribado **cerrado en
> 3.388 de 3.388**, eso significa que **ni uno solo va a llegar por su cuenta**: la cola no los va a
> traer, porque la cola se acabo. **Cada uno de los 329 es una lectura dirigida o no es nada.**
>
> **Y por eso el sales roadmap y P.5 no son dos bloques, son el mismo bloque visto de dos lados:** el
> acto `customer_validation_sales_roadmap` es uno de los 55, con **10 de 15 leidos y los 5 que faltan
> fuera de cola**. Los cinco pares nombrados arriba **son su deuda de P.5**.

**Los diez actos mas grandes con deuda de P.5, para que el tamano del trabajo se vea:**

| tamano | acto | leidos de posibles | fuera de cola |
|---:|---|---:|---:|
| 15 | `cultura_de_seguridad_interpretivista_funcionalista` | 30 de 105 | 75 |
| 13 | `decision_factory_mentality` | 20 de 78 | 58 |
| 10 | `causas_comunes_vs_especiales` | 14 de 45 | 31 |
| 9 | `customer_development_modelo` | 16 de 36 | 20 |
| 8 | `build_measure_learn` | 9 de 28 | 19 |
| 7 | `customer_validation` | 15 de 21 | 6 |
| 7 | `brainstorming_divergente` | 8 de 21 | 13 |
| 6 | `customer_validation_sales_roadmap` | 10 de 15 | 5 |
| 6 | `clasificacion_mercados_cadena_suministro` | 7 de 15 | 8 |
| 6 | `cierre_segun_complejidad_venta` | 9 de 15 | 6 |

### 6. Los ejemplares de las veinte figuras: medido el TAMANO, no cerrado

**Es el bloque grande y sigue abierto.** Lo que esta vuelta aporta no es su contenido: es **su forma
exacta**, para que deje de ser "veinte figuras pendientes" y pase a ser una nomina.

**Criterio del instrumento, escrito para que se pueda discutir:** una figura NOMBRA sus ejemplares si su
propio campo `nota` trae al menos un id de nodo, un puesto citado o un id de lectura dirigida.

| | cuantas |
|---|---:|
| figuras que **NOMBRAN** al menos un ejemplar en su nota | **7** |
| figuras que **NO NOMBRAN** ninguno | **13** |
| **total** | **20** |

**EL REPARTO NO ES ALEATORIO Y ESO ES EL HALLAZGO: parte casi exacto por fecha de corte.** Las **doce
del 11 ago 2026 NO nombran ninguno**; de las **ocho del 12 ago 2026, SIETE nombran y UNA no** (`cobrar
una A sin fundir`). **Las doce viejas se escribieron como doctrina de una linea y las nuevas como ficha
con casos, y por eso el `grep` de la vuelta 15 daba cero en doce de veinte: no es que los ejemplares no
existan, es que no estan en la entrada.**

**LAS TRECE SIN NOMBRAR, con lo que cada una declara:** `SUBCONJUNTO ESTRICTO` (23 ejemplares),
`LA VARA EN LOS DOS SENTIDOS (9.22)` (3 de un polo y 2 del otro), `ESTRELLA (9.23)` (9),
`TRIANGULO ABIERTO` (2), `EL ESQUELETO COMPARTIDO` (3), `LAS DOS ADUANAS` (5), `LA BIFURCACION` (2),
`LOS DOS PARES QUE NO SE CRUZAN` (1), `LA FIRMA POSICIONAL DEL INJERTO (P.2)` (67 candidatos, 43
confirmados), `LA A DE BLOQUE (P.4)` (1 ejemplar y 1 contraejemplo),
`LA COLA DEL DOMINIO SE AGOTA POR DENTRO (9.27)` (3 dominios), `EL PASO DE OFICIO` (medio dominio
`exportacion`, sin cifra) y `cobrar una A sin fundir` (1).

**CUANTOS EJEMPLARES SIN NOMBRAR SON, con las DOS cuentas y sus dos definiciones, porque la ingenua
enganaria:**

| cuenta | definicion | resultado |
|---|---|---:|
| **ingenua** | primer numero que aparezca en el campo `cobertura` de cada una de las 13 | **119** |
| **corregida** | igual, pero `LA VARA` cuenta 5 (3 mas 2, que si son ejemplares) y `LA FIRMA` cuenta 43 (los confirmados) y no 67 (los candidatos, que no son ejemplares) | **98** |

> **LA INGENUA NO SE PUBLICA COMO SI FUERA LA BUENA, y se dice por que: en dos de las trece el primer
> numero del campo `cobertura` NO es un conteo de ejemplares.** En `LA VARA EN LOS DOS SENTIDOS` el
> primer numero es **2 polos**, y en `LA FIRMA POSICIONAL DEL INJERTO` es **67 nodos candidatos**.
> **Las dos cuentas se dejan escritas con su definicion al lado en vez de elegir una**, porque la
> diferencia entre 119 y 98 es entera de definicion y no de medicion. **`EL PASO DE OFICIO` no aporta a
> ninguna de las dos: su cobertura no trae numero.**

**LO QUE ESTO NO ES: no es la medicion que la FASE II espera.** La FASE II pide **los ejemplares**, no
**cuantos faltan por nombrar**. **Lo que cierra el bloque sigue siendo trabajo de lectura**, figura por
figura, y sigue **PENDIENTE DE MEDICION** exactamente como lo dejo la adjudicacion 6.5 de la vuelta 15.
**Lo unico que cambia es que ahora se sabe cuanto es y donde esta: trece entradas, y entre 98 y 119
ejemplares segun como se cuenten los dos casos de definicion.**

---

## TAREA (vuelta 19): los cinco registros, la novena estrella, y la FASE II medida bloque por bloque al cierre

**Corte de todas las cifras de esta seccion: 14 ago 2026, sobre el cribado CERRADO en 3.388 de 3.388.**
**MODO DE CIERRE: cero reparaciones de nodos, cero operaciones ejecutadas, cero pares nuevos encolados.**
`dataset/` intacto y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` intacto en sus 3.388 lineas.

**Instrumentos de esta vuelta, los cuatro de solo lectura:** `scripts/loop/vuelta19_medir.py`,
`scripts/loop/vuelta19_figuras.py` y `scripts/loop/vuelta19_fase2.py`, sobre
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `dataset/metadata/master_graph.json`,
`docs/plan/INVENTARIO.jsonl` y `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`. **Ninguna cifra de esta
seccion sale de una nota vieja: todas salen de una corrida de hoy.**

### 1. LOS CINCO BLOQUES DE LA FASE II, con lo que cada uno tenia y lo que tiene hoy

| bloque | tras la vuelta 17 | **tras la vuelta 19** |
|---|---|---|
| la cola de relectura post fusion | VERIFICADA ENTERA, 7 de 7 | **sigue verificada**: los siete puestos citados en la entrada `defecto` remedidos hoy, seis en B, el 1096 en A, mas el 751 que cae |
| el criterio del forastero | VERIFICADOS LOS DOS | **los dos siguen, mas UN CANDIDATO CONDICIONADO** registrado y no contado: `customer_validation_sales_roadmap` |
| el lote de cinco del sales roadmap | LOS CINCO NOMBRADOS | **LEIDOS Y CERRADO**: `LD-66` a `LD-70`, el acto pasa a 15 de 15 y a CERRADO |
| las lecturas de acto entero de P.5 | CUANTIFICADA: 280 hechos, 55 pendientes, 329 pares | **REMEDIDA: 281 hechos, 54 pendientes, 324 pares** |
| los ejemplares de las veinte figuras | medido el tamano, NO cerrado | **LAS VEINTE NOMBRADAS**: ver el punto 2 |

### 2. EL BLOQUE GRANDE: las veinte figuras, nombradas

**Medido con `scripts/loop/vuelta19_fase2.py`, y con las DOS cuentas al lado porque miden cosas
distintas:**

| cuenta | definicion | resultado |
|---|---|---:|
| **de FORMA**, la de la vuelta 17 | la nota trae un id de nodo, un puesto citado o un `LD-nn` | **20 de 20** |
| **de TANDA**, la sustantiva | la nota trae la marca explicita `EJEMPLARES NOMBRADOS EL` o `SEDES NOMBRADAS EL` de una tanda de nombramiento | **13 de 20** |

> **Las dos cuentas se publican juntas y ninguna sola, porque el acta de la vuelta 18 ya adjudico que
> la de forma tiene falsos positivos** (su adjudicacion 9, con `EL PASO DE OFICIO` como ejemplar).
> **Las SIETE que no traen marca de tanda no estan sin nombrar: nacieron nombradas.** Son las ocho del
> corte 2026-08-12 menos `cobrar una A sin fundir`, que si recibio tanda en la vuelta 18: `frontera de
> disposicion`, `el nombre que esconde`, `nodo puente`, `la camarilla cerrada por lectura`, `la perdida
> que cambia de dueno`, `el superviviente es de la nomina, no del nodo` y `el forastero por cableado`.
> **Sus notas ya citan nodos y puestos desde el dia que se escribieron**, y esta vuelta lo comprobo
> entrada por entrada.

**LAS TRES QUE FALTABAN, cerradas en esta vuelta y con su discrepancia declarada al lado:**

| figura | lo que se nombro | la discrepancia declarada, con la cifra vieja intacta |
|---|---|---|
| **`SUBCONJUNTO ESTRICTO`** | **los 23 puestos**, verificados uno por uno contra el archivo, **cero fallos y los 23 en A** | el 23 cuenta **etiquetas**: el **511** esta declarado en prosa y su razon no la trae. Instancias declaradas: **24** |
| **`LA FIRMA POSICIONAL DEL INJERTO (P.2)`** | **las dos sedes**, con la tabla de los 67 **reproducida celda por celda**, mas **diez ejemplares citables por nodo** | la tanda de los cuatro libros mide **44 nodos distintos** y el doc publica **43**; la diferencia entera es Horowitz, **14 en una sede y 13 en la otra** |
| **`EL PASO DE OFICIO`** | **los TRES declarados por su nombre en la razon del propio archivo**: 2045, 2054 y 2070, los tres D | la cota de 6 nodos se midio con la cadena `us commercial service` **sin puntos**; con la cadena corregida son **26 nodos de 141 y 40 pares de 130** |

### 3. LA NOVENA ESTRELLA: no faltaba, no se habia buscado donde estaba

**El encargo mandaba leer el par periferico como `LD-71`. El par YA ESTABA LEIDO**, y esta medido en
esta vuelta: es **`LD-04`**, de la primera tanda de dirigidas del **11 ago 2026**,
`evaluacion_tecnologias_disruptivas` contra `explotacion_tecnologias_disruptivas`, **clase D**, y ese
mismo `LD-04` ya declaraba por escrito ***"es una ESTRELLA del banco 9.23, con centro y dos
periferios"***.

| la cuenta de 9.23 | estado, medido hoy |
|---|---|
| pares con el centro `tecnologias_disruptivas_oportunidad`, todos A | **SI**: 505 y 513, los dos A, y son los dos unicos del archivo que lo tocan |
| al menos un par entre perifericos, leido y sano | **SI**: `LD-04`, D, desde el 11 ago 2026 |

> **Las estrellas verificadas pasan de OCHO a NUEVE y el campo `cobertura`, que dice 9, queda
> CONFIRMADO en vez de discrepante.** La relectura independiente esta en
> [`LD_ESTRELLA_DISRUPTIVAS.md`](LD_ESTRELLA_DISRUPTIVAS.md), con su limite de ceguera declarado. **No
> se acuno `LD-71`**: un segundo numero para un par ya adjudicado seria una segunda fuente de verdad
> para un solo veredicto.

### 4. TRES SEDES QUE HOY CUENTAN EL MISMO ACTO Y NO DICEN LO MISMO, declarado y NO arreglado

**El registro de TAREA 1.4 movio una de las tres y el encargo solo nombraba esa. Las otras dos quedan
como estaban, y la divergencia se escribe en vez de taparse:**

| sede | que dice hoy del acto del sales roadmap | que dice de la deuda total de P.5 |
|---|---|---:|
| `docs/plan/INVENTARIO.jsonl`, entrada de tipo `acto` | **15 de 15, CERRADO** | **324** |
| `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` | 10 de 15, ABIERTO, 5 fuera de cola | **329** |
| `docs/plan/INVENTARIO.jsonl`, entrada de tipo `racimo` "el sales roadmap" | 10 de 15, MEZCLADO | no la cuenta |

> **La diferencia entre 324 y 329 son EXACTAMENTE los cinco pares de `LD-66` a `LD-70`, y no hay
> ninguna otra.** Las dos cifras son correctas para lo que cada una mide: el archivo de componentes es
> una foto del cierre transitivo al corte 3.388 y **no recoge lecturas dirigidas por diseno**; la
> entrada de `acto` si las recoge. **Quien cite 329 tiene que decir de que sede sale.** La entrada de
> `racimo` es el caso distinto: mide la misma nomina y no tiene motivo para diferir. **Se trae como
> pregunta al reporte y no se toca, porque el encargo scopeaba la entrada de tipo `acto`.**

### 5. EL MARCADOR Y LO RESERVADO, al cerrar la vuelta

| | medido hoy |
|---|---:|
| lineas de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **3.388**, intacto |
| **A / B / C / D** | ~~**583 / 89 / 7 / 2.709**~~ ~~**582 / 87 / 8 / 2.711**~~ ~~**581 / 83 / 8 / 2.716**~~ ~~**576 / 83 / 8 / 2.721**~~ **575 / 83 / 8 / 2.722** **[CORREGIDA VARIAS VECES, el 15 y el 18 ago 2026, ver las correcciones declaradas al principio del documento]** |
| entradas de `docs/plan/INVENTARIO.jsonl` | **671**, y ninguna nace ni muere en esta vuelta |
| entradas tocadas | **9**: cinco en TAREA 1, una mas en su segunda mitad, y tres en TAREA 2.B |
| **ACLARACION DE ROTULO, 14 ago 2026 (vuelta 20), y la fila de arriba no se toca** | el **9** de esa fila son **EDICIONES**, y caen sobre **8 entradas DISTINTAS**: `EL PASO DE OFICIO` recibio **dos**, una en TAREA 1 y otra en TAREA 2.B. Rotulo, no cifra: la descomposicion escrita al lado (cinco mas una mas tres) es exacta, y el reporte de la vuelta 19 ya lo decia bien (*ocho lineas y nueve ediciones*) |
| actos vigentes **CERRADOS / ABIERTOS** | **281 / 54** |
| **la FASE II** | **las veinte figuras quedan NOMBRADAS. Quien declare el bloque cerrado es el auditor, no esta seccion** |

---

## TAREA (vuelta 20): los cinco registros de cierre, y la FASE II medida bloque por bloque

**Corte de todas las cifras de esta seccion: 14 ago 2026, sobre el cribado CERRADO en 3.388 de 3.388.**
**MODO DE CIERRE: cero reparaciones de nodos, cero operaciones ejecutadas, cero pares nuevos leidos.**
`dataset/` intacto, `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` intacto en sus 3.388 lineas, y
`RECOMPUTO_3388_COMPONENTES.jsonl` intacto en sus 335 componentes.

**Instrumentos de esta vuelta, los dos de solo lectura:** `scripts/loop/vuelta20_medir.py` y
`scripts/loop/vuelta20_horowitz.py`, sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`,
`dataset/metadata/master_graph.json`, `docs/plan/INVENTARIO.jsonl`,
`docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` y el arbol entero de `docs/`. **Ninguna cifra de esta
seccion sale de una nota, de un acta ni de un reporte anterior: todas salen de una corrida de hoy.**

### A. LOS CINCO BLOQUES DE LA FASE II, remedidos DESPUES de los registros

| bloque | tras la vuelta 19 | **tras los registros de la vuelta 20** |
|---|---|---|
| la cola de relectura post fusion | sigue verificada, 7 de 7 | **SIGUE VERIFICADA, 7 de 7 y remedida hoy**: la nota cita ocho puestos, y quitado el **751** que CAE por `LD-59` quedan los **siete** de la cola, que es lo que su campo `cobertura` dice. Seis en **B** (196, 224, 253, 591, 707, 968) y el **1096 en A**, con su excepcion escrita en `08_VERIFICACION.md`. El 751 esta hoy en **B** y fuera de la cola |
| el criterio del forastero | los dos, mas un candidato condicionado | **IGUAL, y remedido**: `tacticas_cierre_ventas` con **6 lecturas, 1 A y 5 D**; `incentivos_no_monetarios_advocacy` con **0 pares** en el archivo, que es lo que su nota declara; el candidato condicionado (`customer_validation_sales_roadmap`) sigue registrado y **sin contar** |
| el lote de cinco del sales roadmap | leidos y acto CERRADO | **CERRADO EN LAS DOS SEDES VIVAS**: los **15** pares posibles de la nomina son **10** en el archivo de veredictos mas **5** en dirigidas, y las cinco (`LD-66` a `LD-70`) estan localizadas hoy en `LD_SALES_ROADMAP.md`. La entrada de `racimo` **pasa a 15 de 15 y a cobertura COMPLETA** en esta vuelta; **la FORMA sigue MEZCLADO y no se toca** |
| las lecturas de acto entero de P.5 | 281 hechos, 54 pendientes, 324 pares | **IGUAL, remedido hoy**: **556 actos** (221 superadas, **335 vigentes**), vigentes **281 CERRADOS y 54 ABIERTOS**, deuda **324** por el campo `cobertura` (**0 en cola, 324 fuera de cola**) |
| los ejemplares de las veinte figuras | las veinte nombradas, 20 de forma y 13 de tanda | **IGUAL, y las dos cuentas se siguen publicando juntas**: **20 de 20** de forma y **13 de 20** con marca de tanda. Las **siete** sin marca son las que nacieron nombradas, y el acta de la vuelta 19 verifico cinco de ellas contra archivo, grafo y dirigidas |

**LA COTA DE `EL PASO DE OFICIO`, regenerada en TAREA 1.3 y remedida aqui con las DOS cadenas:**

| cota | criterio | nodos | con la linea en su **paso 1** | pares |
|---|---|---:|---:|---:|
| **VIGENTE**, cadena corregida | las pistas de la vuelta 18 con `us commercial service` reemplazada por `commercial service` | **26 de 141 vivos** | **7** | **40 de 130** |
| contraste, cadena de la vuelta 18 | las pistas tal como estaban, con `us commercial service` sin puntos | **6 de 141 vivos** | **2** | **10 de 130** |

> **Las dos se remidieron HOY y las dos reproducen. Ninguna se borra.** El dominio `exportacion`
> tiene **158 nodos en el grafo, 17 con la clave `deprecado` y 141 VIVOS**, y **130 pares leidos**.

**EL MARCADOR, EL INVENTARIO Y LO RESERVADO, al cerrar la vuelta:**

| | medido hoy |
|---|---:|
| lineas de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **3.388**, intacto |
| **A / B / C / D** | ~~**583 / 89 / 7 / 2.709**~~ ~~**582 / 87 / 8 / 2.711**~~ ~~**581 / 83 / 8 / 2.716**~~ ~~**576 / 83 / 8 / 2.721**~~ **575 / 83 / 8 / 2.722** (17,0 / 2,4 / 0,2 / 80,3 por ciento) **[CORREGIDA VARIAS VECES, el 15 y el 18 ago 2026, ver las correcciones declaradas al principio del documento]** |
| puestos | **1 a 3.388, cero huecos y cero duplicados** |
| entradas de `docs/plan/INVENTARIO.jsonl` | **671**, y ninguna nace ni muere en esta vuelta |
| tipos del inventario | acto **556**, familia_de_ids **53**, figura **20**, defecto **19**, racimo **13**, dominio **10** |
| **entradas DISTINTAS tocadas en esta vuelta** | **3**, y el rotulo va dicho entero para no repetir el de la vuelta 19: **4 pasadas de escritura** sobre esas 3 (`LA FIRMA POSICIONAL DEL INJERTO (P.2)` recibio **dos**) y **6 campos** en total (el `racimo` cambia `cobertura`, `estado` y `nota`; `EL PASO DE OFICIO` cambia `nota`; `LA FIRMA POSICIONAL` cambia `nota` dos veces) |
| actos vigentes **CERRADOS / ABIERTOS** | **281 / 54** |
| nodos en `dataset/metadata/master_graph.json` | **3.835**, de ellos **3.521 vivos**; **cero tocados** |
| componentes en `RECOMPUTO_3388_COMPONENTES.jsonl` | **335**, intacto |
| operaciones en `OPERACIONES.jsonl` | **71**, **cero ejecutadas** |

### B. LAS CIFRAS PUBLICADAS CON DOS LECTURAS: la lista NO queda vacia, queda con UNA

**Barridas las siete que esta vuelta tenia delante, seis quedan cerradas y una queda viva.**

| # | la cifra | sede A | sede B | estado hoy |
|---:|---|---|---|---|
| 1 | el acto del sales roadmap | entrada de `acto`: **15 de 15, CERRADO** | entrada de `racimo`: decia **10 de 15, INCOMPLETA** | **CERRADA en esta vuelta** (TAREA 1.2): el racimo pasa a **15 de 15** y a **cobertura COMPLETA**, aditivo y con el texto viejo entero |
| 2 | la deuda de P.5 | inventario: **324** | `COMPONENTES.jsonl`: **329** | **ADJUDICADA en la vuelta 19 y no reabierta**: las dos son correctas para lo que miden, la diferencia son exactamente los cinco de `LD-66` a `LD-70`, y **quien cite 329 dice la sede** |
| 3 | la cota de `EL PASO DE OFICIO` | **6** nodos, 2 en paso 1, 10 pares | **26** nodos, 7 en paso 1, 40 pares | **CERRADA en esta vuelta** (TAREA 1.3): la corregida es la **VIGENTE**, la vieja queda de **contraste**, cada una con su criterio al lado |
| 4 | la tanda de los cuatro libros | `01_FUENTES.md`: **43** nodos, Horowitz **13** | `10_INVENTARIO.md`, `RECORTE_POSICIONAL.md` y el grafo: **14** | **CERRADA en esta vuelta** (TAREA 1.4): **44 nodos distintos**, correccion declarada con la cifra vieja entera, la nomina de los 14 impresa y su forma verificada uno por uno |
| 5 | el rotulo de la TAREA (vuelta 19) | *entradas tocadas: **9*** | entradas distintas: **8** | **CERRADA en esta vuelta** (TAREA 1.5): el 9 son **EDICIONES** sobre 8 entradas. Rotulo, no cifra |
| 6 | el numero del par de la novena estrella | `LD-04`, del 11 ago 2026 | el encargo 19 mandaba acunar `LD-71` | **CERRADA en esta vuelta** (TAREA 1.1): `LD-04` es el numero, con puntero a su relectura; **`LD-71` no existe en ninguna sede de dirigidas** salvo como el numero que se decidio no acunar |
| **7** | **los pasos de `decision_de_vender_startup`** | `01_FUENTES.md`, tabla de LOS TRES CASOS: **25 pasos** | el grafo, `FICHA_SUBFUSION_GRADIENTE.md`, `COSTURAS_INTERNAS_RESUMEN.md` y la nota de `LA FIRMA POSICIONAL`: **34 pasos** | **VIVA Y SIN ADJUDICAR. NO se arregla en esta vuelta** |

> **POR QUE LA 7 NO SE ARREGLA, y se trae en vez de taparse.** La levanto la medicion de TAREA 1.4 y
> **el encargo de esta vuelta no la scopeaba**. Censadas **todas** las sedes de `docs/` con
> instrumento, el reparto es de **tres sedes mas el grafo contra una**, y los otros dos apartados de
> la misma tabla calzan exactos (`viral_loop_marketing` **30**, `coeficiente_viral` **16**), asi que
> el que diverge es uno solo. **Pero el 25 no es una cifra suelta:** va cosido a un tramo escrito
> (*los pasos 11 a 15, 16 a 20 y 21 a 25*) que habria que rehacer entero, y eso es **reescribir un
> hallazgo, no anotar una correccion aditiva**. No hay regla vigente que mande esa reescritura sin
> saber si el nodo crecio despues del 11 ago o si el conteo viejo era parcial. **Queda declarada al
> lado de la vieja, sin tocar la vieja, y su adjudicacion es del auditor.**

### C. EL VEREDICTO, dicho como MEDICION y no como cierre

> **LOS CINCO BLOQUES: ninguno queda abierto.** Los cinco se remidieron hoy con instrumento, los
> cinco reproducen, y el unico que se movio en esta vuelta (el del sales roadmap) se movio **para
> cerrar la divergencia entre sus dos sedes vivas**, no para abrir nada.

> **LA LISTA DE B: NO queda vacia. Queda con UNA**, la fila 7, nombrada con sus dos sedes y sin
> arreglar. **Por eso esta seccion NO declara la FASE II lista para verificacion de cierre**: la
> condicion que el encargo escribio pedia las dos cosas a la vez, y solo se cumple una. **Se dice lo
> que se midio y no se redondea hacia el cierre.**

> **LO QUE SI SE PUEDE DECIR, medido:** la FASE II queda **con sus cinco bloques cerrados y con UN
> cabo suelto nombrado**, y ese cabo es una cifra de `01_FUENTES.md` sobre los pasos de un nodo,
> **no un pendiente del cribado ni del recomputo**. Si el auditor adjudica la fila 7 en la vuelta
> 21, no queda nada. **El cierre y la apertura de la FASE III son suyos: esta vuelta NO abrio la
> FASE III, NO creo `pasada-unica` y NO corrio el Gate 0.**
> **ADJUDICADA, 14 ago 2026 (vuelta 21), y nada de lo de arriba se toca: LA FILA 7 QUEDO
> ADJUDICADA por el acta de la vuelta 20 del auditor (seccion 4, punto 1), MANDA EL 34**, y el
> conteo viejo era **PARCIAL DE NACIMIENTO** y no un nodo que crecio: el auditor lo midio con git
> (el blob del grafo es identico en `0e5e0c60`, en `23f9ac32` y en HEAD) y esta vuelta lo
> reproduce con `scripts/loop/vuelta21_registros.py` (34 pasos hoy, 34 en el blob del 11 ago, los
> tres blobs `bb423c06`). El registro aditivo esta puesto en la celda de `01_FUENTES.md`. **CON
> ESTO LA LISTA DE CIFRAS PUBLICADAS CON DOS LECTURAS QUEDA VACIA.**

> **Y LA FASE II QUEDA CERRADA por esa misma acta (seccion 8), CON LA FASE III ABIERTA en la rama
> `pasada-unica`**, creada desde `bucle` por el auditor: el trabajo de la FASE III, los reportes y
> las actas viven ahi, `bucle` queda como registro de las fases I y II, y **el merge sigue siendo
> decision de Alexis**. La medicion de la FASE II que esta seccion publica **no se recomputa aqui**:
> se cita con su corte del 14 ago 2026.
