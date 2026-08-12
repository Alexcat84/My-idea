# FASE 04: LOS ENLACES

**La unica fase del plan que ANADE en vez de quitar.** No mueve ids, no funde, no
desteje: **pone la arista que falta.**

**Operaciones: `OP-E-01` y `OP-E-02`. LAS DOS LISTAS**, adjudicadas el 11 ago 2026.

---

## LA BOLSA DEL PASO CONTRA NODO

**Medida el 13 ago 2026 con una muestra pineada de 24** (pin en
`docs/PIN_SORTEO_PASO_NODO.txt`).

| | |
|---|---:|
| candidatos **sin arista** | **624** |
| leidos en la muestra | 24 |
| **JERARQUIA SANA** (arista que falta) | **19** |
| **MADRE QUE REPITE** (poda) | **0** |
| falso positivo | 5 |

> **CERO PODAS EN VEINTICUATRO LECTURAS.** La bolsa **no es una mezcla de dos
> clases de arreglo: es UNA, y es la barata.** No hay que triar entre enlazar y
> podar: hay que **enlazar**.

**PROYECCION, declarada como proyeccion**: **489** jerarquias sanas, con intervalo
de Wilson al 95% **entre 376 y 586**.

---

## LA CALIBRACION YA ESCRITA, para cuando el instrumento vuelva a correr

**No se aplica a la lista ya emitida**, que se lee como esta.

> **En CUATRO de los cinco falsos positivos, el paso y el hijo comparten el
> SUSTANTIVO y cambian el VERBO**: leer contra disenar, monitorear contra lograr,
> listar contra definir, comprar contra certificar.
>
> **El instrumento mide vocabulario y no accion.**

**La correccion**: extraer el verbo principal del paso y el del titulo del hijo, y
**penalizar cuando los verbos son de familias distintas**. **No se toca el umbral:
se anade una senal.**

## `OP-E-01`, EL ORDEN ADJUDICADO: TRES PASOS Y NO SE SALTAN

| paso | que se hace |
|---:|---|
| **1** | **LA CALIBRACION DEL VERBO** sobre el barrido paso-contra-nodo |
| **2** | **MUESTRA PINEADA NUEVA** sobre la bolsa reducida, para medir la **tasa residual** |
| **3** | **SOLO ENTONCES** se decide leer entera o proyectar |

**PASO 2, Y EL SORTEO VA DECLARADO:**

> **La muestra nueva se sortea sobre la bolsa REDUCIDA, con la semilla escrita y
> guardada ANTES de mirar los candidatos**, como se hizo con el pin de la muestra
> vieja. **Tamano minimo 24, el mismo de la vieja, para que las dos tasas sean
> comparables.**
>
> **Sin el pin escrito antes, la tasa no vale: se puede elegir la muestra que la
> confirme.**

**LA CIFRA DE PARTIDA, para comparar contra ella**: 19 jerarquias sanas de 24,
**cero podas**, 5 falsos positivos, proyeccion de 376 a 586 sobre 624.

> **POR QUE ESTE ORDEN Y NO OTRO.** Leer los 624 antes de calibrar es **leer cinco
> de cada veinticuatro sabiendo que son falsos**. Y calibrar sin volver a
> muestrear **deja la tasa vieja aplicada a una bolsa que ya no es la misma.**

---

## LOS SUELTOS DE RACIMOS, y los racimos con miembro ajeno

**`OP-E-02` junta dos cosas que se parecen y no son iguales.**

### 1. LOS SUELTOS

**Un SUELTO es un miembro que un racimo censo pero que ninguna A conecta con el
resto.** El ejemplar medido es **`comprender_alineacion_etica_ia`**, el suelto del
racimo de la supervision de la IA, cuya particion provisional es **5 mas 4 mas 1**.

**LA REGLA, adjudicada el 11 ago 2026, y son tres casos:**

| situacion | que se hace |
|---|---|
| el racimo **tiene centro** y el par del suelto con el centro **ya salio SANO** | **se ENLAZA** |
| el suelto **tiene par A** | **no es enlace: es FUSION**, y va a la fase 03 |
| el racimo **NO tiene centro** | **no se inventa: va a su MESA** |

> **EL EJEMPLAR MEDIDO CAE EN EL TERCER SUPUESTO.**
> `comprender_alineacion_etica_ia` es el suelto de un racimo **partido en dos
> bloques**, o sea **sin centro**: va a mesa y no se enlaza.

> **Por que la regla tiene que nombrar el caso sin centro: es justo donde la
> tentacion es inventar uno.** Un racimo partido en dos no tiene centro por
> definicion, y **colgar el suelto de cualquiera de los dos bloques seria adjudicar
> la particion de contrabando.**

### 2. LOS RACIMOS CON MIEMBRO DE OTRO DOMINIO

**Tres ya hallados, y son la muestra, no el censo:**

| racimo | el miembro | su dominio real |
|---|---|---|
| el lienzo de propuesta de valor (`core`) | `desarrollo_value_proposition_usp` | **franquicias** |
| mapeo del flujo de valor (`quality`) | `value_stream_mapping_ambiental` | **environmental** |
| mapeo del flujo de valor (`quality`) | `analisis_flujo_de_valor` | **core** |

> **La regla para estos SI esta escrita**: o **la nomina se depura**, o **el racimo
> se declara TRANSVERSAL de forma explicita**. **Lo que no puede quedar es un
> racimo que PARECE de un dominio y no lo es.**

**Y el control mecanico que los encuentra a todos de una vez ya esta adoptado**:
revisar **toda** nomina por el DOMINIO de sus miembros, cruzando
`RACIMOS_MIEMBROS.jsonl` contra el grafo.

---

## LAS SIETE C TAMBIEN SON DE ESTA FASE

**Los pares de clase C, sanos con figura, se arreglan con DOS ARISTAS**, no con
una fusion. Puestos **201, 203, 215, 246, 360, 1077 y 1240**.

> **Es el ENLACE MUTUO del banco 9.22**: cada nodo expande una linea distinta del
> otro, ninguno es la madre, **y fundirlos borraria los dos procedimientos.**

---

## POR QUE ESTA FASE SE PUEDE ADELANTAR, y su unica atadura

**No mueve ids**, asi que no depende de la FASE 0 para ejecutarse.

> **Pero SI depende de `OP-C-04` para verificarse.** Una arista nueva mal puesta
> **puede crear una auto-arista via alias**, que es justo lo que la guarda literal
> no ve. **Sin la guarda que resuelve, esta fase puede meter en silencio lo que
> `OP-S-07` acaba de sacar.**
