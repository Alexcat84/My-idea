# REPORTE DE LA VUELTA 175 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta175_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA ES UNA VUELTA DE BATERIA Y ESO MANDA SOBRE TODO LO DEMAS** (`AUDITOR.md`
> 6.1, decision del fundador del 5 sep 2026): la bateria corre CADA CINCO, en una
> vuelta propia QUE NO LLEVA NADA MAS. Aqui no hay trabajo de plan al lado, y
> `OP-L-03` no se toca. **EL TOPE DE ESTA VUELTA NO ES CINCO SINO DOS**
> (`AUDITOR.md` 6.2, regimen temporal vigente hasta que DOS vueltas seguidas
> cierren su propio reporte), y el encargo trae exactamente dos. **La 174 fue la
> primera de esas dos; esta es la segunda.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas coinciden, porque la 174 si
> escribio su reporte y es el que hay en el arbol; el fichero corre LAS DOS
> igualmente y publica lo que salga de cada una, porque una guarda que solo se
> mira cuando difiere no se puede auditar el dia que difiera.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta175_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 174: `1eacb3b5`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 174: LA VUELTA ABRIO Y CERRO SU PROPIO REPORTE, QUE LLEVABA CUATRO VUELTAS SIN PASAR, Y NO PUBLICO NI UNA CIFRA FALSA. LAS DOS RACHAS BAJAN A CERO Y NO HAY PARADA. EL ACTA ABRE CON EL REMEDIO BLOQUEANTE DE MI PROPIA CAIDA REPETIDA: AISLE LA CIEGA ANTES DE GATE 0, DE LA VARA, DE LOS ARNESES Y DEL RECOMPUTO, Y ESA RACHA SE ROMPE POR ORDEN Y NO POR RESULTADO. LOS SIETE DISCUTIBLES Y LAS DOS PREGUNTAS SE ADJUDICAN TODOS A FAVOR DEL EJECUTOR, CITANDO REGLA ESCRITA Y SIN DOCTRINA NUEVA: EL AUSTERO ESTA SUSPENDIDO POR SU PUNTO 5 DESDE LA 137 Y SU TOPE DE 80 NO RIGE, Y LAS CAIDAS DE RUTA DEL ACTA 172 NO ACUMULAN HACIA ATRAS POR LA LETRA SIN RETROACTIVIDAD DEL 2 SEP. CIEGA 6 DE 8, Y LAS DOS DISCREPANCIAS (424 Y 767) SON MIAS Y VAN A FAVOR DEL ARCHIVO: FALLE LA FRONTERA A CONTRA B CONTRA D POR PARECIDO DE SUPERFICIE EN LAS DOS DIRECCIONES. TRES HALLAZGOS FUERA DEL MARCADO Y NINGUNO ES CAIDA SUYA: LA CIFRA DE BYTES DE UN .txt DE docs/loop NO REPRODUCE PORQUE EL REPORTE MEZCLA GIT Y DISCO SIN DECIRLO (3257 CONTRA 3285, Y EL 2749 SELLADO HOY YA VALE 2705), LA CLAUSULA 4.4 QUEDO VIVA EN UNA SEGUNDA SEDE DEL MISMO FICHERO (REPORTE_V172.md:535), Y HAY CINCO ARNESES FUERA DE LA NOMINA Y NO UNO. GATE 0 VERDE EN SU CICLO ENTERO Y CORRIDO POR MI: numstat 0 filas, motor 25/25, tsc 0, web 82 y 1040; MARCADOR 3388 CON A 551 B 72 C 5 D 2760 Y CERO HUECOS; LAS 42 RUTAS DEL REPORTE MEDIDAS UNA A UNA Y NINGUNA CAIDA DE RUTA. LA 175 ES VUELTA DE BATERIA POR EL REGIMEN 6.1 Y LLEVA DOS SUB-TAREAS POR EL 6.2: LA BATERIA ENTERA CON SU DOBLE CORRIDA Y SU NOMINA AL DIA, Y SU PROPIO REPORTE, QUE ES LA SEGUNDA DE LAS DOS SEGUIDAS'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V175_HEAD_APERTURA.txt`: `1eacb3b5`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `032a03c7`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **174**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 175`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
21 celdas no se pudieron leer"** y de esas lineas de rojo, **2
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LA BATERIA DE MUTACIONES ENTERA, SOLA Y CON SU DOBLE CORRIDA, Y LA NOMINA AL DIA DENTRO DE ESTA MISMA TAREA (el auditor lo adjudico asi en su acta de la 174: es contrato del propio fichero, no una tercera sub-tarea). Lleva cuatro vueltas saliendo en CERO BYTES (171, 172, 173 y 174, esta ultima por regimen y no por caida). Va entera y sin aflojar ninguna guarda, y su salida se SELLA en `docs/loop/SALIDA_V175_BATERIA.txt`, MEDIDA antes de nombrarla en ningun sitio | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | ABRIR Y CERRAR ESTE MISMO REPORTE EN LA MISMA VUELTA, QUE ES LA SEGUNDA DE LAS DOS SEGUIDAS que `AUDITOR.md` 6.2 pide para levantar el regimen temporal de dos sub-tareas. Esqueleto al empezar, fila anexada al cerrarse la TAREA 1, cierre con `scripts/loop/cerrar_reporte.py`, y ARCHIVADO EN LA MISMA VUELTA sin esperar a la 176 | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
