# FASE 07: LA ADUANA

**El plan repara una vez. La aduana impide que vuelva a entrar.**

**Operaciones: `OP-A-01` LISTA y `OP-A-02` DECISION PENDIENTE.**

---

## `OP-A-01`: EL CONTROL POSICIONAL . **LISTA**

**ADJUDICADO: el control de P.2 entra a la aduana como control de entrada
permanente.**

> **EL CONTROL, en una linea: todo nodo que entre declarando MAS DE UNA fuente se
> comprueba por el material del SEGUNDO libro.**

| lo que se encuentre | que se hace |
|---|---|
| el material del segundo libro **no esta en los pasos** | **la fuente sobra** |
| **esta, y es de otro tema** | **es un injerto y se desteje** |

**POR QUE A LA ADUANA LE INTERESA MAS QUE AL PLAN.** El plan repara **67 nodos**
una vez; **la aduana impide que entre el sesenta y ocho**, y para eso le basta con
mirar **el ORDEN del campo `fuente`**, que es lo mas barato que se puede mirar.

### EL PRERREQUISITO QUE EL RECORTE DESTAPO

> **EL CAMPO `fuente` NO ESTA NORMALIZADO.**

| libro | grafias distintas | sin normalizar | canonico |
|---|---:|---:|---:|
| Hugos | **2** | 23 | **21** |
| Horowitz | **3** | 16 | **14** |

**La nomina de Hugos del auditor, los 21, SOLO CUADRA CON EL NOMBRE CANONICO.**

> **Sin lista canonica de libros, el control posicional cuenta mal.** Es un
> prerrequisito barato y es de esta fase: **una tabla de libros con sus alias de
> escritura**, igual que los nodos tienen `ids_alias`.

---

## `OP-A-02`: LA PUERTA SEMANTICA . **LISTA**

**ESPECIFICADA POR EL AUDITOR el 11 ago 2026, y cabe en una frase:**

> # LA ADUANA NO JUZGA, OBLIGA A JUZGAR.

**EL MECANISMO:**

1. **Al insertar un nodo**, corre el **indice semantico** contra **su dominio** y
   **el nucleo**.
2. Si **algun vecino supera el umbral de la cola**, **la insercion se BLOQUEA**.
3. Se desbloquea cuando **quien inserta escribe el veredicto continua-o-repite
   CITANDO EL ID del vecino**.

> **NUNCA bloquea por parecido. Solo por VEREDICTO AUSENTE.**

**POR QUE ASI Y NO CON UN FILTRO.** Un filtro que decidiera por parecido
**rechazaria nodos buenos y aceptaria malos**, porque **el parecido no es la
clase**: la clase la decide continua-o-repite, y eso lo decide quien lee. **Lo que
la aduana hace es mas barato y mas fuerte: no deja entrar nada sin que alguien
haya mirado a los vecinos y lo haya escrito.**

**POR QUE CONTRA SU DOMINIO Y EL NUCLEO, Y NO CONTRA TODO.** Es **exactamente el
reparto que el cribado midio**: la duplicacion vive **dentro del dominio y contra
el nucleo**; entre dominios distintos casi no hay. **Correr contra todo
encareceria la insercion sin subir la captura.**

**Y EL UMBRAL NO ES NUEVO: es el de la cola**, o sea **la misma vara que el
archivo ya uso 2.117 veces**.

> **EL SINTOMA QUE ESTO IMPIDE ES EL QUE EL CATALOGO YA TIENE: 400 pares en A que
> nadie vio entrar.** Cada uno habria costado **una linea de veredicto** en el
> momento de la insercion. **Hoy cuesta una fusion con reparto de perdidas.**

**LA SALIDA QUE NO VALE, escrita para que no se use**: bajar el umbral. **La
insercion se desbloquea con el veredicto escrito, no con el parecido bajado.**

**LOS CINCO CONTROLES MECANICOS QUE LA ACOMPANAN:**

| control | de donde viene |
|---|---|
| **auto-arista CON RESOLUCION** | `OP-C-04` |
| **lista blanca de claves** del nodo | `OP-C-04` |
| **control posicional del campo `fuente`** | `OP-A-01` |
| **campo `fuente` CANONICO** | **`OP-S-11`**, y es prerrequisito de los dos anteriores |
| **revision de toda nomina por el DOMINIO de sus miembros** | control mecanico del 13 ago 2026 |

> **La diferencia entre los cinco y la puerta semantica: los cinco son MECANICOS y
> no piden juicio.** La puerta semantica si lo pide, **y por eso no juzga ella:
> obliga a que alguien juzgue.**
