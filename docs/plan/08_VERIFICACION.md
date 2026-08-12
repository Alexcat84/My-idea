# FASE 08: LA VERIFICACION

**Operacion: `OP-V-01`. LISTA.**

---

## EL CRITERIO DE HECHO, y es uno solo

> **UNA FASE ESTA HECHA CUANDO SU VERIFICACION SE CAERIA SI EL FALLO VOLVIERA.**
>
> **No cuando pasa verde: cuando se CAERIA.**

**Es el criterio del CASO POSITIVO de la FASE 0, aplicado a todo el plan.** Y tiene
una comprobacion barata: **correr la prueba ANTES del arreglo. Si pasa, no prueba
nada.**

---

## POR FASE

| fase | que tiene que dar verde |
|---|---|
| **0 CODIGO** | cada caso positivo **se cae antes** del arreglo y pasa despues |
| **01 FUENTES** | ningun nodo de la clase con pasos alterados; **el material del segundo libro reubicado, no borrado** |
| **02 DESTEJIDOS** | los **quince congelados** releidos; **cada perdida en el bloque del que proviene** |
| **03 FUSIONES** | un superviviente por acto, el resto **DEPRECADO CON ALIAS**; `resolverId` devuelve el superviviente |
| **04 ENLACES** | cada arista nueva **confirmada por lectura**, no por el instrumento; ninguna crea auto-arista tras resolver |
| **05 SANEO** | ningun id vivo con tratado extinto; los tres de Incoterms con su version; ningun nodo cablea `export.gov`; ninguna de las seis herramientas muertas; ningun nodo con dos claves de fase; **ningun nodo se cita a si mismo tras resolver** |
| **06 MESAS** | cada decision escrita **con su motivo y su cobertura al lado** (banco 9.26) |
| **07 ADUANA** | los cuatro controles mecanicos **corriendo en Gate 0** |

---

## LA VERIFICACION TRANSVERSAL, y su orden importa

1. **Gate 0 verde**
2. **suite verde**
3. **vuelo completo**
4. **prueba de rumbos** (ya comprueba que ningun ancla este deprecada)
5. **reindexado semantico**

> **EL REINDEXADO VA AL FINAL, DESPUES DE MOVER IDS.** El indice **guarda ids** y
> es **una de las fuentes externas que `OP-S-08` identifico**. Reindexar antes deja
> el indice apuntando a la era anterior, **y el sintoma no aparece en el
> reindexado: aparece semanas despues en el recorrido de una persona.**

---

## LA COMPROBACION QUE SOLO SE PUEDE HACER AL FINAL

**Recomputar el cierre transitivo** y comprobar dos cosas:

- **los actos ejecutados desaparecieron**
- **ninguno nuevo aparecio por sorpresa**

> **Y por la regla P.1 del banco del plan: ese recomputo, como cualquier conteo que
> toque ids, PASA POR EL RESOLUTOR ANTES DE CONTAR.** Un recomputo literal sobre un
> grafo recien fusionado **contaria los absorbidos como nodos vivos.**
