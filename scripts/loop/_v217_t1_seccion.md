### TAREA 1. LAS DIECISIETE CLAUSULAS DE LAS FASES 0 A 07, MEDIDAS UNA POR UNA

**LO QUE SE CORRIO, Y SU RUTA CON SUS BYTES:**
``docs/loop/SALIDA_V217_T1_DIECISIETE.txt``, **37762 bytes en disco y 37339 normalizado a LF**, exitcode 0.
Y el contraste, ``docs/loop/SALIDA_V217_T1_CONTRASTE_V150.txt``, **858 bytes en disco y 837 normalizado
a LF**, exitcode 1 y su motivo escrito abajo.

**EL INSTRUMENTO NO ES NUEVO POR DENTRO Y ESO IMPORTA CON LA MORATORIA
ENCIMA** (`AUDITOR.md` 6.3). Los lectores se **IMPORTAN** de
`scripts/loop/vuelta150_4_tabla_por_fase.py`, que es la sede donde ya viven:
`celdas_de_la_tabla`, `fichas`, `grafo`, `resolutor`, `gate0_checks` y
`guarda_salidas_congeladas`. Lo unico propio de esta vuelta es **el partido de
las celdas en clausulas y las diecisiete sondas**, que es medicion y es lo que
la moratoria protege.

**CIFRA lineas de ese fichero: 626 | CIFRA lineas ejecutadas al cargarlo: 622. La diferencia es SU ULTIMA LINEA DE ENTRADA, una llamada suelta a main() sin guarda, que se descarta para cargar sus lectores sin correr su tabla. EL FICHERO EN DISCO NO SE TOCA: la moratoria prohibe repararlo y no se repara.**

## 1.a. LAS FILAS Y SUS CLAUSULAS, SACADAS CON UN INSTRUMENTO Y NO A MANO

**LAS CUATRO CIFRAS, CADA UNA CON LA DEL ENCARGO AL LADO Y EN LA MISMA LINEA,
que es lo que la obligacion de las filas manda:**

```
CIFRA FILAS ARMADAS LEYENDO LA TABLA POR FASE: 11 | CIFRA FILAS QUE DEBERIA HABER: 11
CIFRA CLAUSULAS ARMADAS EN LA TABLA ENTERA: 30 | CIFRA QUE DEBERIA HABER: 30
CIFRA FILAS DE 0 CODIGO A 07 ADUANA ARMADAS: 8 | CIFRA QUE DEBERIA HABER: 8
CIFRA CLAUSULAS DE ESAS OCHO FILAS ARMADAS: 17 | CIFRA QUE DEBERIA HABER: 17
CIFRA descuadres contra las cifras del encargo: 0
```

**EL REPARTO POR FILA, CONTADO Y NO TECLEADO** (11 filas leidas del fichero, 11
que deberia haber):

```
  0 CODIGO               clausulas armadas  1 | que deberia haber 1
  01 FUENTES             clausulas armadas  2 | que deberia haber 2
  02 DESTEJIDOS          clausulas armadas  2 | que deberia haber 2
  03 FUSIONES            clausulas armadas  2 | que deberia haber 2
  04 ENLACES             clausulas armadas  2 | que deberia haber 2
  05 SANEO               clausulas armadas  6 | que deberia haber 6
  06 MESAS               clausulas armadas  1 | que deberia haber 1
  07 ADUANA              clausulas armadas  1 | que deberia haber 1
  08 VERIFICACION        clausulas armadas  1 | que deberia haber (fuera de las ocho: el encargo no da cifra)
  09 LECTURAS DIRIGIDAS  clausulas armadas  8 | que deberia haber (fuera de las ocho: el encargo no da cifra)
  10 INVENTARIO          clausulas armadas  4 | que deberia haber (fuera de las ocho: el encargo no da cifra)
```

**LAS DIECISIETE, VERBATIM** (17 filas leidas del fichero, 17 que deberia
haber):

```
  0 CODIGO         idx 0 | cada caso positivo **se cae antes** del arreglo y pasa despues
  01 FUENTES       idx 0 | ningun nodo de la clase con pasos alterados
  01 FUENTES       idx 1 | **el material del segundo libro reubicado, no borrado**
  02 DESTEJIDOS    idx 0 | los **quince congelados** releidos
  02 DESTEJIDOS    idx 1 | **cada perdida en el bloque del que proviene**
  03 FUSIONES      idx 0 | un superviviente por acto, el resto **DEPRECADO CON ALIAS**
  03 FUSIONES      idx 1 | `resolverId` devuelve el superviviente
  04 ENLACES       idx 0 | cada arista nueva **confirmada por lectura**, no por el instrumento
  04 ENLACES       idx 1 | ninguna crea auto-arista tras resolver
  05 SANEO         idx 0 | ningun id vivo con tratado extinto
  05 SANEO         idx 1 | los tres de Incoterms con su version
  05 SANEO         idx 2 | ningun nodo cablea `export.gov`
  05 SANEO         idx 3 | ninguna de las seis herramientas muertas
  05 SANEO         idx 4 | ningun nodo con dos claves de fase
  05 SANEO         idx 5 | **ningun nodo se cita a si mismo tras resolver**
  06 MESAS         idx 0 | cada decision escrita **con su motivo y su cobertura al lado** (banco 9.26)
  07 ADUANA        idx 0 | los cuatro controles mecanicos **corriendo en Gate 0**
```

## 1.b Y 1.c. EL VEREDICTO DE CADA UNA, CON SU BUSQUEDA CORRIDA

**LA TABLA SALE DEL FICHERO Y SE CUENTA ANTES DE PUBLICARLA: 17 filas de
datos leidas, 17 que deberia haber.**

| # | fila | idx | veredicto | la clausula, VERBATIM |
|---:|---|---:|---|---|
| 1 | 0 CODIGO | 0 | CUBRE | cada caso positivo **se cae antes** del arreglo y pasa despues |
| 2 | 01 FUENTES | 0 | A MEDIAS | ningun nodo de la clase con pasos alterados |
| 3 | 01 FUENTES | 1 | A MEDIAS | **el material del segundo libro reubicado, no borrado** |
| 4 | 02 DESTEJIDOS | 0 | CUBRE | los **quince congelados** releidos |
| 5 | 02 DESTEJIDOS | 1 | A MEDIAS | **cada perdida en el bloque del que proviene** |
| 6 | 03 FUSIONES | 0 | A MEDIAS | un superviviente por acto, el resto **DEPRECADO CON ALIAS** |
| 7 | 03 FUSIONES | 1 | CUBRE | `resolverId` devuelve el superviviente |
| 8 | 04 ENLACES | 0 | CUBRE | cada arista nueva **confirmada por lectura**, no por el instrumento |
| 9 | 04 ENLACES | 1 | CUBRE | ninguna crea auto-arista tras resolver |
| 10 | 05 SANEO | 0 | CUBRE | ningun id vivo con tratado extinto |
| 11 | 05 SANEO | 1 | A MEDIAS | los tres de Incoterms con su version |
| 12 | 05 SANEO | 2 | CUBRE | ningun nodo cablea `export.gov` |
| 13 | 05 SANEO | 3 | CUBRE | ninguna de las seis herramientas muertas |
| 14 | 05 SANEO | 4 | CUBRE | ningun nodo con dos claves de fase |
| 15 | 05 SANEO | 5 | CUBRE | **ningun nodo se cita a si mismo tras resolver** |
| 16 | 06 MESAS | 0 | CUBRE | cada decision escrita **con su motivo y su cobertura al lado** (banco 9.26) |
| 17 | 07 ADUANA | 0 | CUBRE | los cuatro controles mecanicos **corriendo en Gate 0** |

**EL REPARTO, CONTADO DE ESA MISMA TABLA: 12 en CUBRE, 5 en
A MEDIAS, 0 en NO CUBRE y 0 SIN SONDA, de 17.**

**LAS QUE NO DAN CUBRE, CON SU FILA, SU INDICE Y SU CIFRA** (5 lineas
leidas del fichero):

```
01 FUENTES       idx 0 | A MEDIAS  | ningun nodo de la clase con pasos alterados
01 FUENTES       idx 1 | A MEDIAS  | **el material del segundo libro reubicado, no borrado**
02 DESTEJIDOS    idx 1 | A MEDIAS  | **cada perdida en el bloque del que proviene**
03 FUSIONES      idx 0 | A MEDIAS  | un superviviente por acto, el resto **DEPRECADO CON ALIAS**
05 SANEO         idx 1 | A MEDIAS  | los tres de Incoterms con su version
```

**LAS DOS CLAUSULAS CON CORRECCION DECLARADA SE MIDIERON POR SU LECTURA
CORREGIDA, NO A LA LETRA**, y las dos son de la fila `05 SANEO`: *"ningun nodo
cablea export.gov"* (idx 2) y *"ninguna de las seis herramientas muertas"*
(idx 3). La correccion vive en las **lineas 35 a 58** de
`docs/plan/08_VERIFICACION.md`, se leyo entera antes de medir, y su efecto esta
medido: **la de las seis herramientas, medida A LA LETRA, daria NO CUBRE por UNA
mencion viva** (`Alexa` en `inteligencia_de_anuncios_de_la_competencia`), y esa
mencion esta **FUERA de la nomina de `OP-S-04`** y el fundador ya la saco de la
campana. **Medida acotada da CERO menciones dentro de la nomina, y las dos
cifras se publican juntas.**

## 1.d. EL CASO ROJO NO SE PROMETE, SE PRUEBA POR MUTACION

**17 mutantes rotos leidos del fichero, 17 que deberia haber, y CAEN
17 de 17.** Ninguno toca una ficha, un nodo ni una pagina: se fabrican en
memoria sobre una copia.

```
MUTANTE ROTO  1 | 0 CODIGO         idx 0 | desaparecen las pruebas, las etiquetas y las salid | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO  2 | 01 FUENTES       idx 0 | un miembro de la clase queda con un solo paso      | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO  3 | 01 FUENTES       idx 1 | un nodo de la nomina se borra sin dejar alias      | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO  4 | 02 DESTEJIDOS    idx 0 | aparece un congelado de la nomina de la fase 02    | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO  5 | 02 DESTEJIDOS    idx 1 | la pagina 02 se queda sin registros y las fichas s | veredicto A MEDIAS  | CAE: SI
MUTANTE ROTO  6 | 03 FUSIONES      idx 0 | un superviviente pierde sus alias                  | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO  7 | 03 FUSIONES      idx 1 | un absorbido deja de resolver a su superviviente   | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO  8 | 04 ENLACES       idx 0 | una arista nueva cita un puesto que no existe      | veredicto A MEDIAS  | CAE: SI
MUTANTE ROTO  9 | 04 ENLACES       idx 1 | una arista nueva se cierra sobre si misma          | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 10 | 05 SANEO         idx 0 | el id con el tratado extinto vuelve a estar vivo   | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 11 | 05 SANEO         idx 1 | los supervivientes pierden la version              | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 12 | 05 SANEO         idx 2 | un nodo de la nomina vuelve a cablear el dominio m | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 13 | 05 SANEO         idx 3 | un nodo de la nomina vuelve a nombrar dos muertas  | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 14 | 05 SANEO         idx 4 | un nodo recibe una segunda clave de fase           | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 15 | 05 SANEO         idx 5 | un nodo vivo se cita a si mismo                    | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 16 | 06 MESAS         idx 0 | una nomina de mesa se queda sin cobertura          | veredicto A MEDIAS  | CAE: SI
MUTANTE ROTO 17 | 07 ADUANA        idx 0 | dos controles dejan de correr en Gate 0            | veredicto A MEDIAS  | CAE: SI
```

**Y EL REVERSO, PORQUE UNA SONDA QUE NUNCA PUEDE DECIR CUBRE TAMPOCO MIDE:
4 mutantes SANOS, y SUBEN 4.**

```
MUTANTE SANO    | 01 FUENTES       idx 0 | los seis vuelven al texto del grafo previo         | veredicto CUBRE     | SUBE: SI
MUTANTE SANO    | 01 FUENTES       idx 1 | las nominas dejan de declarar un segundo libro     | veredicto CUBRE     | SUBE: SI
MUTANTE SANO    | 03 FUSIONES      idx 0 | los actos sin fundir quedan con un superviviente y | veredicto CUBRE     | SUBE: SI
MUTANTE SANO    | 05 SANEO         idx 1 | los tres supervivientes traen la version           | veredicto CUBRE     | SUBE: SI
```

## 1.e. NO SE ESCRIBIO NADA, Y SE PRUEBA CON LOS CUATRO SHA

```
SHA256 DE docs/plan/OPERACIONES.jsonl AL ENTRAR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/OPERACIONES.jsonl AL SALIR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/08_VERIFICACION.md AL ENTRAR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
SHA256 DE docs/plan/08_VERIFICACION.md AL SALIR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
LOS CUATRO SHA COINCIDEN CON LOS DE LA ENTRADA: SI
```

**Ni un campo de estado, ni la pagina 08, ni el inventario, ni el expediente.**

## 1.f. LA DISCREPANCIA CONTRA MI PROPIO ENCARGO, DECLARADA Y NO RESUELTA COPIANDO

**MI ENCARGO DICE, VERBATIM: "LAS OCHO FILAS DE 0 CODIGO A 07 ADUANA, CON SUS
DIECISIETE CLAUSULAS, NO LAS HA MEDIDO NADIE CON UNA SONDA CORRIDA". MEDIDO HOY:
ESO ES CIERTO DE LAS DIECISIETE CLAUSULAS Y NO LO ES DE LAS OCHO FILAS.**

`scripts/loop/vuelta150_4_tabla_por_fase.py` **mide las ocho filas**, una por
fase, con su veredicto de tres palabras, y se corrio en las vueltas 150 a 155.
Lo que nadie habia medido, y es lo que esta tarea mide, son **las diecisiete
clausulas por separado**. Las dos cosas se publican y la discrepancia no se
resuelve copiando (`EJECUTOR.md` 2).

**Y HAY UNA SEGUNDA MITAD, MEDIDA CON SU CORRIDA: ESE INSTRUMENTO HOY CAE EN
ROJO.** Corrido en esta vuelta contra mi propio corte, sale con **exitcode 1**:

```
FILAS DE LA TABLA POR FASE, LEIDAS DE docs/plan/08_VERIFICACION.md: 11
AssertionError: la tabla no trae ocho filas: 11
```

**La causa esta medida y no supuesta:** su `assert` exige OCHO filas y la
correccion declarada de la vuelta 214 dejo **ONCE** en la tabla POR FASE, al
anadir las de las fases 08, 09 y 10. **NO LO REPARO Y ESO ES DELIBERADO: la
moratoria de `AUDITOR.md` 6.3 prohibe reparar arneses, y el propio encargo dice
que las dos tareas de esta vuelta son medicion y verificacion.** Se mide, se
publica y se dice. **Y por lo mismo, para cargar sus lectores sin correr su
tabla se descarta SU ULTIMA LINEA DE ENTRADA al ejecutarlo en memoria: el
fichero en disco no se toca ni en un byte.**

## 1.g. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Son lectura mia y por eso van aparte** (`EJECUTOR.md` 7). **Cinco.**

| # | sobre que | que decidi y cual es la duda |
|---|---|---|
| **D.a** | `01 FUENTES` idx 0, la vara del ANTES | Publico **A MEDIAS** y no CUBRE. Los seis miembros de la clase conservan su NUMERO de pasos contra el grafo previo, que es lo que la clase protege; pero DOS tienen texto distinto, y aunque los commits que los tocaron no nombran ninguna operacion de la fase 01, el asunto de un commit es un proxy y no una lectura. Si el auditor lee que la clausula protege el numero y no la letra, esta clausula es CUBRE. |
| **D.b** | `01 FUENTES` idx 1, que es 'reubicado' | Publico **A MEDIAS**. La mitad 'no borrado' esta medida y da CERO borradas de 70 menciones. Para la mitad 'reubicado' elegi como vara que el nodo YA NO declare mas de una fuente, y quedan 7 menciones que todavia declaran dos o mas. Si el auditor lee que reubicar es solo mover el bloque y no reducir el campo, la vara es otra. |
| **D.c** | `02 DESTEJIDOS` idx 1, la anchura del detector | Publico **A MEDIAS** con la regla ESTRECHA, que busca la frase de la regla de reparto, y publico al lado la ANCHA, que busca que la ficha nombre un bloque. Las dos cifras estan en la tabla. Si el auditor lee que nombrar el bloque con otras palabras cumple la clausula, esta es CUBRE por la cifra ancha. |
| **D.d** | `03 FUSIONES` idx 0, el universo de la clausula | Publico **A MEDIAS** midiendo TODOS los actos del corte vigente. La mitad del alias cubre entera y sin excepcion; lo que no cubre es que 71 actos siguen con varios miembros vivos, o sea SIN FUNDIR. Si el auditor lee que la clausula solo habla de los actos YA fundidos, como hace el arnes de la vuelta 150 al medir solo las fichas con superviviente escrito, esta clausula es CUBRE. |
| **D.e** | `07 ADUANA` idx 0, cuatro contra cinco | Publico **CUBRE** porque la clausula pide CUATRO y hay CUATRO corriendo y en verde. Pero la pagina 07 y la verificacion de `OP-A-02` nombran CINCO, y el quinto, la revision de toda nomina por el DOMINIO de sus miembros, NO corre. Si el auditor lee que la celda quedo vieja y que la cifra viva es cinco, esta clausula es A MEDIAS. |

**LO QUE NO PROPONGO, Y DIGO POR QUE.** El encargo escribe la condicion de la
parada feliz antes de saber el resultado: *"si las DIECISIETE quedan en CUBRE
con su busqueda corrida y su cifra delante"*. **No quedan: 5 de 17 dan
A MEDIAS**, y estan nombradas arriba con su fila, su indice y su cifra. **Por
tanto NO propongo declarar la campana consumada.** Lo que si digo, porque es lo
que la medicion sostiene: **ninguna de las diecisiete da NO CUBRE**, y las cinco
que no cubren lo hacen por trabajo pendiente medido y nombrado, no por un fallo
del catalogo.
