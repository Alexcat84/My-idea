### TAREA 2. LA APERTURA DEL AUDITOR COMO CODIGO

**`scripts/loop/apertura_del_auditor.py`** (**11.444 bytes en disco**), con nombre
estable y sin numero de vuelta, como `aislador_de_ciega.py` y `cerrar_reporte.py`,
y **no se clona**. Decision del fundador del 5 sep 2026, PREGUNTA 3, opcion `c`,
la mitad que quita el problema de raiz; la otra mitad, que romper un remedio
escrito ACUMULE, ya estaba escrita en `AUDITOR.md`.

**COMO LO IMPIDE, Y ES LO UNICO QUE HACE.** Lleva una **bitacora de toques**: las
tres cosas prohibidas solo se hacen llamando a `git_log()`, `git_status()` y
`leer_reporte()`, y cada una **apunta su toque antes de hacerlo**. `sellar()`
**cae en rojo si la bitacora ya trae alguno de los tres, y no escribe nada**: no
avisa ni recomienda, **no sella**. La decision vive en `puede_sellar()`, separada
a proposito, para que el arnes la pueda tumbar **sin escribir un solo fichero**.

**EL CASO POR MUTACION, SOBRE VARIABLE COMPUTADA Y NO SOBRE CONSTANTE LITERAL**
(`EJECUTOR.md` 1, letra del 29 ago 2026). Instrumento
`scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py`, salida
`docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` (**5.078 bytes**).
**VERDE, 0 fallos**, con todo el material fabricado en un temporal que se borra:

- **6 escenarios** de `puede_sellar()`, los tres prohibidos uno a uno, los tres
  juntos, la bitacora limpia y un toque **no** prohibido. Los seis calzan.
- **Los tres prohibidos por su funcion de verdad**, no apuntados a mano:
  `puede_sellar()` pasa de `True` a `False` en los tres.
- **`sellar()` tras tocar: devuelve `False` y escribe CERO ficheros en el
  temporal.** No es que avise: es que no hay sello.
- **Y con la bitacora limpia SI sella**, con su ciega, su destape y su sello,
  para que se vea que no esta simplemente roto: *un guardia que no deja pasar a
  nadie no es un guardia, es una pared*.
- **LA MUTACION:** el veredicto computado tras `git_log()` es `False`; con el
  esperado `False` **PASA** y con el esperado `True` **CAE**. Y la segunda
  mutacion quita `git log` de la constante de prohibidos y el mismo escenario
  **cambia a `True`**, con la constante devuelta a su sitio despues.

`docs/loop/AUDITOR.md` gana el parrafo que nombra el fichero y **escribe el orden
obligatorio del turno como una linea de codigo y no como un recuerdo**.

> **LO QUE ESTE FICHERO NO PUEDE HACER, Y SE DICE EN VEZ DE VENDERLO DE MAS:** no
> puede impedir que alguien corra `git status` en su terminal por su cuenta.
> **Ninguna guarda de este repo puede.** Lo que si hace es que **el sello, que es
> lo que el acta cita como prueba, no se pueda escribir despues**; y con eso
> saltarse el remedio deja de ser un descuido y pasa a ser **una decision a
> sabiendas y sin sello**.
