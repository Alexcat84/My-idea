### TAREA 1 (BLOQUEANTE): LOS REGISTROS. `R.61` Y `R.62` ESCRITAS, Y LA CORRECCION DE CITA EN SU SEDE

**LOS DOS NUMEROS SON COMPUTADOS Y NINGUNO ESTA TECLEADO.** Comando corrido en
esta vuelta, con su salida sellada en
`docs/loop/SALIDA_V201_T1_REGISTROS.txt`:

```
python scripts/loop/_v201_t1_registrar_actas.py --escribir
```

**NINGUN LECTOR NUEVO SE ESCRIBIO, QUE ES LA MITAD DEL ENCARGO BAJO LA
MORATORIA.** Los cinco que este computo usa se IMPORTAN:
`serie_de_registros.siguiente_libre()` da el numero,
`R84.claves_entrecomilladas()` lee las `4.n`, las `5.n` y las `C.An`,
`R94.caidas_propias_entrecomilladas()` las `C.n` del ejecutor,
`R92.caidas_por_lead_heredado()` corre al lado como contraste y
`R92.titulo_de_la_entrada()` compone el titulo con sus cinco numerales. El
fichero lleva **prefijo de guion bajo** y por eso queda fuera del censo y fuera
de la nomina, que sigue **congelada en 135**.

**1.a . EL ACTA 200 ENTRA COMO `R.61`.** El cuerpo se acoto **en esta vuelta** y
no con las cifras del encargo: **lineas 70230 a 70549 de
`docs/loop/ACTA_AUDITOR.md`, 320 lineas**, sobre un fichero de **4657056 bytes en
disco y 4657056 normalizados a LF**. Numerales contados de ese cuerpo: **8
adjudicaciones** (`4.1` a `4.8`), **4 hallazgos** de la seccion 5, **2 preguntas
contestadas**, **4 caidas propias del auditor** (`C.A1` a `C.A4`) y **0 caidas
del ejecutor**. **El contraste heredado se publica al lado y la discrepancia se
declara:** `R92.caidas_por_lead_heredado()` da **1 del ejecutor y 0 del auditor**
sobre el mismo cuerpo, y las cifras que la entrada publica son las de los
lectores que leen la NEGRITA QUE ABRE cada caida.

**1.b . LA VUELTA 198 ENTRA COMO `R.62`, Y SU ENTRADA DECLARA UNA AUSENCIA.**
`docs/loop/reportes/REPORTE_V198.md` **NO EXISTE**, medido en esta vuelta con
`os.path.isfile` y `os.path.getsize` desde el propio registrador y ademas por el
bloque `H` del sello de apertura. **El cero de bytes sale de que no hay fichero,
no de medir uno.** **NO SE RECONSTRUYE Y NO SE FABRICA.** Cuerpo del acta 198
acotado hoy: **lineas 69636 a 69877, 242 lineas**; **3 adjudicaciones**, **5
hallazgos**, **3 preguntas**, **2 caidas propias del auditor** y **0 del
ejecutor**.

**Y LA CONSECUENCIA DE LA AUSENCIA SE MIDE EN VEZ DE TAPARSE:** la via del
registrador de la 200 filtra las claves `P.n` de los titulos `4.n` del acta
contra la seccion de PREGUNTAS del reporte archivado. **Sin reporte no hay
filtro**, asi que el numeral de `R.62` usa **las 3 claves `P.n` nombradas en los
titulos `4.n` del acta** (`P.2`, `P.3`, `P.1`), y la entrada **lo dice** en vez
de publicar un cero que se leeria como que el acta 198 no contesto ninguna
pregunta.

**LA GUARDA DE IDEMPOTENCIA SE VOLVIO A PROBAR POR MUTACION, Y NO POR
CORTESIA:** esta vuelta escribe **DOS entradas seguidas**, que es exactamente el
escenario en que la guarda vieja de la 200 cayo. **8 casos, 8 verdes, 0 rojos**,
la guarda vieja corriendo al lado sobre los mismos textos y **discrepando en 2**,
y **los 8 CAEN al mutar el esperado**. Contado de
`docs/loop/SALIDA_V201_T1_REGISTROS.txt`.

**LA SEGUNDA CORRIDA ES LA PRUEBA DE QUE NO DUPLICA**, sellada aparte en
`docs/loop/SALIDA_V201_T1_REGISTROS_IDEM.txt`: **0 entradas escritas** y
**crecimiento 0 bytes**.

**LA SERIE, REMEDIDA AL CERRAR CON `serie_de_registros.py` Y NO HEREDADA:** **54
entradas**, **0 colisiones**, **0 huecos**, siguiente libre **`R.63`**.
`docs/PENDIENTES.md` crece por **171 lineas anadidas y 0 borradas**, contadas con
`git diff --numstat`. **La deuda de la serie baja de 9 actas a 8**: siguen sin
entrada propia las de las vueltas **173, 174, 175, 176, 177, 178, 179 y 180**.

**1.c . LA CORRECCION DE CITA, DE UNA LINEA, EN SU SEDE.** Comando corrido en
esta vuelta, sellado en `docs/loop/SALIDA_V201_T1C_CORRECCION_DE_CITA.txt`:

```
python scripts/loop/_v201_t1c_correccion_de_cita.py --escribir
```

**LAS DOS MEDICIONES QUE LA SOSTIENEN SE HICIERON AQUI Y NO SE HEREDARON, Y SI
CUALQUIERA FALLA EL COMPUTO NO ESCRIBE NADA.** El literal `se corrige es la
guarda` sale en **0 lineas** de `docs/loop/AUDITOR.md` y en **4** de
`docs/loop/ACTA_AUDITOR.md` (**64775, 65217, 70302 y 70412**); de esas, **1 cae
dentro del cuerpo del acta 185**, acotado hoy en las **lineas 64434 a 64907**, y
**por debajo de la cabecera de su punto `6.2`**, que esta en la **linea 64753**.

**EL TEXTO VIEJO SE QUEDA ENTERO Y SIN TACHAR** (banco `9.10` mas `EJECUTOR.md`
8): el aviso se ANADE detras del parrafo de la PARADA `1`. Medido con
`git diff --numstat`: **2 lineas anadidas y 0 borradas** en
`docs/loop/reportes/REPORTE_V200.md`, que pasa de **137433 bytes en disco y LF** a
**138307 bytes en disco y LF**. **NO ES CAIDA Y NO SE COBRA:** es la forma en que
la casa lo cita desde el acta 185, y lo que el aviso corrige es **de donde sale la
regla**, no la regla.

**LO QUE ESTA TAREA NO TOCA, DICHO PORQUE EL ENCARGO LO MANDA:** **las dos
paradas que la 200 levanto no se vuelven a levantar y no se arreglan.** El acta
200 las adjudica en su `4.1` y su `4.2`, **las dos reparaciones son de codigo**, y
**la moratoria `6.3` las prohibe hoy**. Van a la auditoria integral.
