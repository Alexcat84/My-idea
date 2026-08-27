# PARA ALEXIS: EL BUCLE SE DETIENE POR RACHA DE CAIDAS DE REPORTE (27 ago 2026, vuelta 95, auditor Opus 5)

(Copia de archivo de `docs/loop/PARA_ALEXIS.md`, para que la parada quede
fechada aqui aunque el fichero vivo se sobrescriba en el futuro.)

## EL MOTIVO, EN UNA FRASE

**Tercera caida de REPORTE seguida y de la misma especie**, que es la condicion
de parada escrita en `AUDITOR.md` seccion 4: *"TRES seguidas si son PARADA: tres
de la misma especie ya no son ruido, son un patron de dictado suelto."*

**No es una parada del dato. El dato esta impecable y es importante que lo leas
primero.**

## LO PRIMERO, PORQUE ES LO QUE MAS PESA: LA VUELTA 95 ES BUEN TRABAJO

Lo medi todo yo, con mis comandos, y sale verde:

- **Grafo intacto y verificado en tres refs con sha256 en las tres**: censo
  3.853 / 3.188 vivos / 665 deprecados, aristas 9.190 / 9.169 / 18.359 / 9.813,
  auto-aristas 0. El diff de la union entera da **cero borradas y cero nuevas**.
- **Gate 0 corrido por mi: OK, y su salida es IDENTICA BYTE A BYTE a la del
  ejecutor** (4.970 bytes). `dataset/` sin mover un byte tras el ciclo de tres.
- **Motor 25/25, web 80 ficheros y 1.030 tests (3 skipped), tsc limpio.**
- **Marcador remedido por mi: A 551 / B 72 / C 5 / D 2.760, cero huecos.**
- **El sello de apertura, que fue el unico incumplimiento de la vuelta 94, esta
  esta vez en el PRIMER commit** y su padre es exactamente el hash sellado.
- **La escalada de codigo que encargue esta hecha y funciona.** El tallador
  nuevo (`scripts/loop/tallar_barrido_cifras.py`) reproduce sus 18 aciertos al
  digito cuando lo corro contra el arbol del commit donde se midio, enumeracion
  de lineas incluida. Y la fila de identidad del tallador de cabecera ya no es
  un literal: la decide `git log --diff-filter=A`, y sus dos casos obligatorios
  los corri yo y dan lo que tenian que dar.
- **El trabajo de lectura es el mas verificado de la campana.** El ejecutor leyo
  las 18 razones del grupo C y las partio en 11 que quedan y 4 que van a
  relectura conjunta. **Yo construi una vara mecanica independiente que no vio
  su codigo y me dio las dos listas identicas, sin una sola discrepancia.** Y
  mis 16 lecturas ciegas (pasos primero, razon despues) coinciden con las 16.
- **CERO caidas de clase y CERO de cifra publicada**, dos vueltas seguidas.

## LO QUE CAE, Y ES UNA COSA

`docs/loop/REPORTE.md` **linea 210**, en la lista de rutas tocadas:

> `docs/PENDIENTES.md` (cinco secciones nuevas)

**Son CUATRO.** No lo conte a ojo: talle el diff de la vuelta entera con
`scripts/loop/tallar_composicion_salida.py`
(`docs/loop/_auditor_v95_pendientes_tallado.txt`) y da **4 secciones de nivel 2
y 4 subsecciones de nivel 3**. Probe siete criterios distintos (cabeceras de
cada nivel, lineas en negrita, menciones de "VUELTA 95", hunks del diff) y
**ninguno da cinco**.

La cifra **vive solo en `REPORTE.md`** y **no mueve ningun dato**: por eso es de
REPORTE y no de cifra publicada.

## POR QUE ESO PARA EL BUCLE

Porque es la tercera seguida y las tres son la misma especie exacta: **una
cuenta de piezas de un artefacto, dictada a ojo, que el artefacto no sostiene.**

| vuelta | la frase publicada | lo que el artefacto dice |
|---:|---|---|
| 93 | "**SEIS** casos de mutacion" | el instrumento corre **CINCO** |
| 94 | "**8** aciertos, todos en `04_ENLACES.md`" | el fichero trae **14**, 11 y 3 |
| 95 | "**cinco** secciones nuevas" | el fichero trae **CUATRO** |

Y lo que la agrava: **el remedio de codigo contra esta especie se construyo en
esta misma vuelta**, el instrumento que la talla existe desde la vuelta 91, y el
encargo lo dijo en mayusculas ("TODA CIFRA QUE DESCRIBA LA COMPOSICION DE UN
FICHERO DE SALIDA SE TALLA Y SE PEGA CON SU COMANDO; ninguna se cuenta a ojo, NI
SIQUIERA LAS FACILES"). La cifra que cayo es de las faciles.

**Y te lo digo sin esconderme detras de la regla:** esta caida es la mas leve de
las tres por sus consecuencias. Es un parentesis en una lista de rutas. No mueve
un dato, no cambia un veredicto, no toca el grafo. **Es perfectamente razonable
que decidas que la regla de las tres es demasiado apretada para esta especie.**
Yo no puedo decidirlo: la regla esta escrita, las dos partes la tenian delante, y
si la dejo pasar el freno deja de existir. Por eso paro y te lo traigo.

## MIS PROPIOS ERRORES DE ESTA VUELTA, PORQUE NO SON MENOS

Tres, todos del encargo y el acta de la vuelta 94, medidos hoy por mi:

1. **Mi etiqueta del "grupo C" era falsa para nueve de sus dieciocho.** Publique
   que esas 18 razones "ni citan linea ni traen forma de indice". **Nueve de
   ellas mencionan la palabra "linea", y ocho con la formula literal "es/son UNA
   LINEA".** Mi regex casaba "EN una linea" y no "ES una linea", que es como el
   redactor escribe la mayoria de sus anclas. La conclusion que saque sigue en
   pie, la etiqueta no.
2. **Afirme una busqueda que no corri.** Mande arreglar un SyntaxWarning en
   `scripts/loop/vuelta94_tarea4_reparar_marca_hijo.py`. **Ese warning no existe
   y nunca existio**: el fichero abre con `r"""` desde su unico commit. El
   ejecutor gasto tres vias en desmentirme y tenia razon.
3. **Una omision mia mando un par a la mesa sin necesidad.** Le di al ejecutor
   la linea 32695 del acta para el 1886 y no vi que la misma tabla, dos filas
   mas arriba, **ya resolvia el 1844**. Lo adjudico en el acta: **el 1844 queda,
   y la relectura conjunta baja de cuatro a tres.**

## EL ESTADO EXACTO EN QUE QUEDA TODO

- **Rama:** `pasada-unica`. **HEAD:** `1c721c16d61a4c64db88950845ce18d451facff7`
  (mas el commit de estos documentos del bucle).
- **Fase:** III, EJECUCION, **fase 04 ENLACES**, en modo de ejecucion continua.
- **Marcador (remedido hoy):** **A 551 / B 72 / C 5 / D 2.760**, corte 3.388,
  cero huecos, cero duplicados.
- **Grafo:** 3.853 nodos, 3.188 vivos, 665 deprecados. Gate 0 **OK**. Motor
  25/25, web 80/1.030 mas 3 skipped, tsc limpio. **Nada pendiente de commitear.**
- **`docs/plan/OPERACIONES.jsonl`:** 71 operaciones, **70 LISTA y 1 HECHA**
  (`OP-E-02`).
- **`OP-E-07`** (la de la direccion): bolsa vigente **84 filas** en
  `docs/plan/OP_E_07_DIRECCION_V94.jsonl`, cifra **82 ESCRITA mas 2 YA_ESTABA**.
  Esta vuelta **no retiro ninguna arista**, que era un resultado legitimo.
- **`OP-E-03`**: abierta, con **183 filas** de bolsa en
  `docs/plan/DIFERENCIA_CONTRA_COLA.jsonl` **sin leer todavia**. El ejecutor paro
  deliberadamente ahi y lo dejo escrito, y comparto la decision.
- **Nada se ha fundido a `staging` ni a produccion.** El bucle no funde ramas.

## LO QUE NECESITO DE TI, Y SON TRES DECISIONES

1. **La de fondo: la regla de las TRES caidas de reporte.** Tres opciones, y la
   tercera es la que yo recomendaria si me lo preguntas:
   - **(a)** Confirmas la parada y el bucle se cierra aqui.
   - **(b)** Perdonas esta y la racha vuelve a cero, sin tocar la regla.
   - **(c)** **Afinas la regla:** que la caida de reporte cuente para la racha
     solo cuando la cifra este en una tabla, una cabecera o una conclusion, y no
     cuando viva en una lista de rutas o en prosa de acompanamiento. Con esa
     regla, la de esta vuelta se registra pero no acumula. **Lo digo porque el
     dato lleva dos vueltas impecable y seria una pena parar por un parentesis;
     pero es tu decision, no mia.**
2. **Los tres pares de RELECTURA CONJUNTA: 886, 890 y 947.** Son duda genuina y
   los confirmo. **El 886 es el hermano vivo del 1009 que ya salio**: mismo nodo
   hijo (`fit_problema_solucion`), misma formula literal ("trae un procedimiento
   que esas fases / esa fase no tienen"), madre casi gemela. Y la razon por la
   que la mesa no se puede evitar: **esa misma formula produjo el 1083
   (CONFIRMADO) y el 1009 (CAIDO)**, asi que ninguna vara escrita hoy los
   separa. Necesitan mesa, no otra vuelta de bucle.
3. **Si el bucle sigue, quien lo corre.** Los modelos actuales son ejecutor
   Opus 5 y auditor Opus 5. El trabajo de dato y de instrumento esta a un nivel
   alto y sostenido; lo que se repite es el dictado suelto en la prosa del
   reporte. **Si decides seguir, mi recomendacion es no cambiar modelos sino
   cambiar el reporte:** que las cifras de composicion se generen y se peguen,
   no se escriban.

## COMO RETOMAR

1. Deja tu decision sobre el punto 1 escrita en un fichero de
   `docs/loop/paradas/` (el patron es el de
   `2026-08-26-cierre-fase-03-DECISION.md`), como se hizo con la parada de la
   fase 03.
2. Si el bucle sigue, escribe el encargo de la vuelta 96 en
   `docs/loop/PROMPT_SIGUIENTE.md`, que **queda vacio a proposito**. El trabajo
   que estaba en la cola, por si sirve: **el primer tramo de lectura de
   `OP-E-03`** (40 pares de los 183, con los ids pasados por el resolutor,
   marcados LECTURA DIRIGIDA, fuera de la cola y fuera de la tasa por dominio),
   que es donde el ejecutor paro deliberadamente y bien.
3. Relanza. La rama sigue siendo `pasada-unica` y el merge a `staging` sigue
   siendo tuyo y solo tuyo.

**Todo lo de este documento esta medido en esta vuelta contra el repo, con los
ficheros `docs/loop/_auditor_v95_*` commiteados al lado. Los seis instrumentos
que escribi reproducen su propia salida, cotejado con `cmp` uno por uno.**
