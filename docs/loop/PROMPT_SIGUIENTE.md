# ENCARGO DE LA VUELTA 220 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

**LO QUE RIGE, Y NO SE NEGOCIA:**

- **LA 220 ES LA VUELTA DE BATERIA, Y LA BATERIA VA SOLA.** `AUDITOR.md` 6.1 dice que
  corre **cada cinco, en una VUELTA DE BATERIA propia que no lleva nada mas**. La 215
  la corrio y la cadencia pone esta aqui. **La TAREA 1 de este encargo es el registro
  que el formato fijo de `AUDITOR.md` 1.4 obliga a poner en todo encargo, y no es
  trabajo de plan al lado: no hay ninguno en esta vuelta.** Lo declaro yo para que no
  se lea como que te doy dos trabajos.
- **LA MORATORIA `AUDITOR.md` 6.3 SIGUE PUESTA.** Ningun arnes, guarda ni lector
  nuevo, y ninguno reparado. **La nomina sigue CONGELADA EN 135 y no se poda.** Todo lo
  que escribas en el arbol `scripts/loop` va con prefijo de guion bajo, `_v220_*`,
  fuera del censo y fuera de la nomina.
- **NINGUNA TAREA MUEVE EL CAMPO `estado` DE NINGUNA FICHA**, ni toca
  `docs/plan/08_VERIFICACION.md`, ni el inventario, ni `docs/plan/07_ADUANA.md`.
  Publica sus `sha256` al entrar y al salir por las dos convenciones, y tienen que
  coincidir. **Las dos celdas de la pagina 08 son sede del fundador: NO SE TOCAN.**
- **TODA CITA DE UN ACTA ANTERIOR LLEVA SU NUMERO DE ACTA Y SU LINEA, Y LA LINEA SE
  LEE DEL FICHERO** (`6.6` del acta 210, linea **74203**). **Tu reporte de la 219 lo
  cumplio 17 de 18: la unica que fallo es la del preambulo, que cita la linea 77463
  cuando el texto de las once citas vive en la 77461.** Es la caida `2.1` de mi acta.
  **Verifica cada linea contra el fichero antes de escribirla, incluidas las del
  preambulo: la que se te escapo fue justo la que anuncia esta obligacion.**
- **LOS TAMANOS EN BYTES EXACTOS**, nunca redondeados, los KB solo entre parentesis y
  detras del byte (`P.2`), **cada ruta con sus dos convenciones EN SU MISMA LINEA**. Y
  el remedio de tu propia `C.4`, **con tus palabras y no con las mias**, que por eso lo
  adjudique a favor: *la pareja de bytes no es una regla de RUTAS, es una regla de
  CIFRAS DE BYTES, vengan de una ruta o de un campo de texto de un registro.*
- **EL TOPE DE SUB-TAREAS ES CINCO** (acta 212, adjudicacion `6.8`, linea **75168**).

---

## TAREA 1. LOS REGISTROS, Y ES BLOQUEANTE

**1.a. ANOTA LAS SEIS ADJUDICACIONES DE MI ACTA 219, QUE EMPIEZA EN LA LINEA 77727 DE
`docs/loop/ACTA_AUDITOR.md`.** Registra cada una con su rotulo, su numero y **su linea
leida del fichero**:

| rotulo | adjudicacion | que se sostiene |
|---|---|---|
| TAREA 1 `D.1` | `4.1` | remedir no era recomputar. **El mismo instrumento es el mismo instrumento**, y ademas re-corri tu lector yo y sale identico |
| TAREA 1 `D.2` | `4.2` | **no lo adjudique por tu palabra: lo medi.** Selle el `sha256` de nueve ficheros, corri `_v219_t2_lecturas.py`, y **cero se movieron**. No es la especie de la `C.3` de la 218 |
| TAREA 1 `D.3` | `4.3` | la glosa es registro y no lectura tuya, y decir *"esto no lo he vuelto a medir yo"* se te cuenta a favor |
| TAREA 2 `D.1` | `4.4` | **`01 FUENTES` idx 1 se sostiene en CUBRE**, y traigo la prueba que no usaste: `P.19` punto 2 deja el nodo **MULTIFUENTE LEGITIMO**, y **sus dos ejemplares nombrados son `coeficiente_viral` y `decision_de_vender_startup`**, dos de los cinco de tu tabla |
| TAREA 2 `D.2` y `P.1` | `4.5` | **LA FRONTERA ADJUDICADA: el tercero queda FUERA DEL ALCANCE.** El punto de verificacion de `05 SANEO` idx 1 **se acota por correccion declarada** a los dos nodos que `OP-S-02` alcanza. **`05 SANEO` idx 1 SUBE A CUBRE** |
| TAREA 2 `D.3` | `4.6` | el reparto de tanda a libro es tuyo, con su guarda, y **decir el limite de tu propia guarda es lo contrario de venderla como mordiendo** |

**1.b. ESCRIBE EL RECUENTO NUEVO, QUE CAMBIA POR MI ADJUDICACION `4.5`.** Al cierre de
tu 219 lo dejaste en **14 CUBRE, 3 A MEDIAS, 0 NO CUBRE**, y lo reproduje yo byte a
byte con tu propio lector. **Con la `4.5` aplicada queda en 15 CUBRE, 2 A MEDIAS, 0 NO
CUBRE.** Publica **las dos cifras juntas**, la que tu lector mide hoy sin la
adjudicacion y la que la adjudicacion deja, **y di cual es cual**. **No toques
`docs/plan/08_VERIFICACION.md` para conseguirlo:** la celda es sede del fundador y la
divergencia sube nombrada, igual que la de `07 ADUANA`.

**LAS DOS QUE QUEDAN, con su cifra:** `03 FUSIONES` idx 0 (**71 actos** sin fundir por
la lectura ancha, **SEIS fusiones de 19 nodos** por la estrecha) y `07 ADUANA` idx 0
(**el quinto control sin correr**).

**1.c. ANOTA LAS SIETE COSAS QUE SUBEN NOMBRADAS A LA AUDITORIA INTEGRAL**, con su
cifra, tal como las lista la seccion 6 de mi acta. **No las resuelvas.** La **1** es mi
propia familia `C.1` en NUEVE, **y esta vez sube con TRES OPCIONES concretas para el
fundador**: registralas las tres, que es lo que la hace decidible.

---

## TAREA 2. LA BATERIA DE MUTACIONES, ENTERA Y SOLA

**2.a. CORRE LOS ONCE TRAMOS EXPLICITAMENTE, UNO POR UNO.** El lanzador es
`scripts/loop/vuelta183_bateria_por_tramos.py`, **es estable y NO SE CLONA**. Corre
`--tramo 1` hasta `--tramo 11`, **commiteando cada tramo con su salida sellada al
terminar**, que es lo que `AUDITOR.md` 6.1 manda: *"una vuelta cortada retoma en el
tramo siguiente"*.

> **AVISO MEDIDO POR MI HOY, Y ES LA CAIDA `5.1` DE MI ACTA: NO USES `--siguiente`
> COMO VARA DE LO QUE FALTA EN ESTA VUELTA.** Lo corri antes de escribir esto y
> contesta, literal: **`CIFRA tramos que FALTAN: 0`, `LOS 11 TRAMOS TIENEN SALIDA
> SELLADA`**. **Es falso para la 220 y verdadero para la 215:** las once salidas que ve
> son las de la 215, porque los tramos se sellan en nombres estables
> (`SALIDA_V183_BATERIA_TRAMO_N.txt`) y `--siguiente` **no sabe de que vuelta son las
> salidas que mira**. **Si te fias de el, esta vuelta no corre ni un tramo y el reporte
> dira que la bateria esta hecha.** Corre los once a mano y **no repares el lanzador**,
> que la moratoria `6.3` lo prohibe y no hay caida de dato que lo exija.

**2.b. LA DOBLE CORRIDA Y EL RELOJ NO SE AFLOJAN.** `AUDITOR.md` 6.1: la bateria sigue
entera y sigue sola, **cada entrada se corre DOS VECES** (cotejo de reproducibilidad,
vuelta 141), **con su reloj y su salida sellada**. Publica el reloj con su cifra.

**2.c. COMPON LA SALIDA UNICA SOLO CUANDO LOS ONCE TENGAN SALIDA SELLADA**, con
`--componer`, y **publica su nombre, sus bytes por las dos convenciones y su
atribucion, LAS TRES JUNTAS**. **Y di las dos cosas del rotulo**, que es la trampa que
lleva dos actas subiendo: el fichero compuesto se llama
`docs/loop/SALIDA_V183_BATERIA.txt`, **su primera linea dice VUELTA 183**, y **su
contenido pasa a ser el de la 220**. Cuidado con donde lo escribes: la guarda
`hueco_declarado_que_falta()` de `scripts/loop/cerrar_reporte.py` **cae en rojo si en
la seccion 9 aparece un fichero de bateria que no sea el de la vuelta que cierra**, y
tu 219 ya midio esa puerta.

**2.d. UNA SALIDA SELLADA QUE MIDE CERO BYTES NO CUENTA COMO HECHA**, y **los once
tienen que ser DEL MISMO CALIBRE**. Publica **CIFRA tramos con salida sellada no
vacia** y **CIFRA tramos que faltan**, las dos, medidas sobre las salidas que TU
escribiste en esta vuelta y no sobre las que ya estaban.

**2.e. SI UN TRAMO SALE EN ROJO, NO LO ARREGLES: PARALO Y TRAELO.** Un mutante que no
muere es una guarda que no muerde, y eso es de las que el fundador decide.

---

**Marca tus discutibles antes de saber si aciertas, y ponlos donde el reporte manda.**

**Y UNA COSA MAS, QUE ES SOBRE MI Y NO SOBRE TI:** mi acta 219 se cierra con un bloque
dirigido al auditor de la 220 con sus tres comandos de apertura y con las dos cosas que
le ahorran trabajo. **No lo borres, no lo muevas y no lo cites en tu reporte.** Esta
puesto ahi a proposito y su sitio es el final del acta.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice
una regla vigente, paras y lo traes. No adivines.
