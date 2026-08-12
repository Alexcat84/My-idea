# FASE 04: LOS ENLACES

**La unica fase del plan que ANADE en vez de quitar.** No mueve ids, no funde, no
desteje: **pone la arista que falta.**

**Operaciones: `OP-E-01` y `OP-E-02`. LAS DOS DECISION PENDIENTE.**

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

**LA PREGUNTA de `OP-E-01`**: se leen los 624, se lee un lote y se proyecta, o **se
aplica primero la calibracion y se relee la bolsa reducida**?

---

## LOS SUELTOS DE RACIMOS, y los racimos con miembro ajeno

**`OP-E-02` junta dos cosas que se parecen y no son iguales.**

### 1. LOS SUELTOS

**Un SUELTO es un miembro que un racimo censo pero que ninguna A conecta con el
resto.** El ejemplar medido es **`comprender_alineacion_etica_ia`**, el suelto del
racimo de la supervision de la IA, cuya particion provisional es **5 mas 4 mas 1**.

> **No hay regla escrita.** Un suelto se **enlaza** al racimo, se **deja fuera** de
> la nomina, o **se espera** a que el cribado lo conecte? Es la pregunta.

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
