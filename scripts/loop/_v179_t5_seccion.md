### TAREA 5. LO QUE NO ENTRA Y NO SE PIERDE, CONTADO EN VOZ ALTA

**Ninguna de las cinco se toca**, y las cinco se nombran **con su medicion**, que
es lo que `EJECUTOR.md` 1 exige desde el 5 sep 2026: **una ruta publicada como
prueba es una cifra publicada**, y si apunta a un fichero inexistente o de cero
bytes es caida de cifra. Nombrar cinco pendientes sin comprobar sus sedes es
prometer cinco pruebas sin mirar ninguna.

**LA TABLA SALE DE `docs/loop/SALIDA_V179_T5_NO_ENTRA.txt`** y se pega entera:

| que no entra | sede | existe | bytes en disco | bytes en LF | lineas que la traen |
|---|---|---|---:|---:|---:|
| 1. LA SEGUNDA SEDE DE LA CLAUSULA 4.4 | `docs/loop/reportes/REPORTE_V172.md` | SI | 48851 | 48851 | 2 |
| 2. EL DOCSTRING DEL PASO 0 | `scripts/loop/paso0_archivar_anterior.py` | SI | 7112 | 7112 | 1 |
| 3. LA GUARDA QUE FALTA EN LA DEPENDENCIA DEL `D.4` DE LA 174 | `scripts/loop/vuelta179_esqueleto_reporte.py` | SI | 19911 | 19911 | 2 |
| 4. EL GRANO DEL TOPE DE 10 MINUTOS | `scripts/loop/verificar_mutaciones_viejas.py` | SI | 111914 | 111914 | 1 |
| 5. LA CONVENCION DE BYTES | `docs/loop/AUDITOR.md` | SI | 22612 | 22612 | 1 |

**Las cinco sedes existen, ninguna mide cero bytes y las cinco agujas aparecen.**

**Y EL INSTRUMENTO SALIO EN ROJO EN SU PRIMERA CORRIDA, QUE ES LO QUE SE LE
PIDE.** La aguja de la **2** estaba escrita en mayusculas y el docstring lo dice
en minusculas, `"la vuelta anterior"`, en su linea 25. **Cayo nombrando la aguja
que fallaba**, se corrigio la aguja (no el fichero, que no se toca) y volvio a
correr. Una guarda que no puede salir en rojo no prueba nada.

**LO QUE CADA UNA ES, EN UNA LINEA:**

1. **La segunda sede de la clausula 4.4** vive en `REPORTE_V172.md:535`, y sigue
   ahi, con dos lineas del fichero que la nombran.
2. **El docstring de `paso0_archivar_anterior.py`** sigue hablando de **la vuelta
   anterior** cuando la maquina ya pregunta por **el reporte que va a pisar**. La
   maquina esta bien; el texto que la describe, no. **Esta vuelta lo volvio a
   usar** y las dos preguntas volvieron a coincidir, asi que la divergencia sigue
   sin poderse ver en corrida.
3. **La guarda que falta en la dependencia del `D.4` de la 174**: el esqueleto
   **clona** `vuelta_del_reporte_del_arbol()` en vez de importarla, y **nada avisa
   si el fichero del que se clono desaparece**. El de esta vuelta lo declara en su
   docstring, con dos lineas que lo dicen, y sigue sin instrumento.
4. **El grano del tope de 10 minutos** se mide **EN LA 181**, con el reloj de esa
   corrida, y **no se re-elige a ojo antes**. Esta vuelta no es de bateria y
   medirlo aqui seria medirlo sobre una corrida que no existe.
5. **La convencion de bytes** es del fundador y **lleva seis actas subiendo**, y esa cifra es del encargo de esta vuelta y no
   la recomputo yo.
   **Sube como pendiente, no como problema:** el remedio provisional, publicar
   siempre las dos, ya es instrumento dentro de `cerrar_reporte.py` desde la 178,
   y esta vuelta volvio a salir a coste cero. **Toda cifra de bytes de este
   reporte va por las dos convenciones**, incluidas las cinco filas de arriba.
