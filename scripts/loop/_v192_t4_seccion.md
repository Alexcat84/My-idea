### TAREA 4. LA CUARTA PUERTA DEL SELLO DE LA APERTURA DEL AUDITOR. **CERRADA.** El fichero no se clona: se le anade, y su arnes de la nomina sigue reproduciendo byte a byte.

**(a) LA CUARTA PUERTA, ANADIDA A `scripts/loop/apertura_del_auditor.py`.** **Lo
que el fichero crecio va cercado abajo**, citado de la salida del parche, porque
la primera de las dos cifras es de ANTES y una cifra de bytes suelta al lado de
una ruta se lee como una afirmacion sobre esa ruta HOY:

```
   apertura_del_auditor.py pasa de 14724 a 21223 bytes en disco
   COMPILA
```

Lo que se le anade son **cinco funciones y cuatro constantes**, y ni una linea de
las tres puertas viejas se toca:

- `puestos_sellados()`. **El sujeto lo define el sello y nadie mas:** lee el
  sello del turno, de ahi la ruta de la ciega, y de la ciega sus
  `puesto_intra`. **No se teclean ni se pasan por argumento**, que es lo que
  impide elegir el sujeto despues de mirar.
- `leer_veredictos()`. **APUNTA SU TOQUE**, y por defecto devuelve las filas de
  los puestos sellados **con `clase` y `razon` TAPADAS**. Quien quiera verlas
  tiene que pedir `destapar_sujeto=True`, y entonces el toque que apunta es
  **otro**: el de destape. **Un destape no se puede hacer sin querer.**
- `marcador()`. Cuenta por clase sobre el archivo **entero** y **no destapa
  nada**, porque un agregado de miles de filas no dice la clase de ninguna.
  Existe para que la cuarta puerta **no estorbe lo que el acta si tiene que
  hacer**: recomputar el marcador antes de escribir sus clases.
- `puede_declarar_clases()`, PURA sobre el estado del modulo, **que es la que el
  arnes tumba**.
- `declarar_clases_escritas()`. **CAE EN ROJO y no marca nada** si hubo un
  destape antes. Es el gemelo exacto de `sellar()`: alli el rojo era no poder
  sellar; **aqui es no poder declarar las clases escritas**, que es lo que un
  acta cita como prueba de que leyo a ciegas.

**LA LINEA QUE SEPARA LO PROHIBIDO DE LO PERMITIDO ES TODA LA GUARDA, Y VA
ESCRITA:** no se prohibe leer el archivo entero, que hace falta para el marcador;
**se prohibe DESTAPAR EL SUJETO**, o sea leer `clase` o `razon` **de los puestos
que el sello ya eligio**, antes de que las clases esten escritas.

**Y LA CUARTA PUERTA VA EN SU PROPIA CONSTANTE Y NO DENTRO DE
`PROHIBIDOS_ANTES_DEL_SELLO`, POR UNA RAZON MEDIDA:** aquellas se prohiben
**antes del sello** y esta se prohibe **antes de las clases**, que es otro momento
del turno; y ademas el arnes de la vuelta 182 **recorre esa tupla una a una**, asi
que meterla dentro lo habria roto. Se comprobo re corriendolo, y esta abajo.

**(b) LO QUE ESTA GUARDA NO PUEDE HACER, ESCRITO EN EL PROPIO FICHERO** como su
docstring ya hacia con las otras tres, **y ademas PROBADO en el bloque `G` del
arnes y no solo escrito**: **no puede impedir que alguien abra el `jsonl` por su
cuenta en su terminal**, ni con `python`, ni con `grep`, ni con un editor. El
arnes lo lee a mano y comprueba que **la bitacora sigue vacia y las clases se
pueden declarar igual**. Lo que si puede es que **la declaracion no se pueda
escribir despues** y que **quien se la salte lo haga a sabiendas**. Y una segunda
cosa que no puede, dicha porque es mas fina: **no sabe si lo que se leyo era del
sujeto cuando el archivo se abre por fuera de estas funciones**.

**(c) EL CASO POSITIVO POR MUTACION: VERDE, CON 30 CASOS Y CERO ROJOS**
(`docs/loop/SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt`, **disco 4282 bytes | LF
4282 bytes**). **SUJETO CONGELADO:** fabrica su propio archivo, su propia ciega y
su propio sello en un directorio temporal y los retira. **La mutacion que importa
es la `E`:** se sustituye `leer_veredictos()` por **la version sin el apunte de
destape, que es exactamente el codigo de antes de esta vuelta**, y se comprueba
que entonces

- el sujeto **se ve igual**,
- **no queda apuntado ningun destape**, y
- **`declarar_clases_escritas()` sale VERDE**.

**Ese es el agujero, y es el que esta puerta tapa: el sujeto se quema exactamente
igual y el sello sigue saliendo verde.** Hay una segunda mutacion (`F`): con
`CAMPOS_QUE_DESTAPAN` vacio, el tapado deja de tapar. Y las dos restauran lo que
tocaron y lo comprueban.

**(d) NO SE CLONA EL FICHERO.** `apertura_del_auditor.py` conserva su nombre
estable y sin numero de vuelta: **se le anade, no se le hace una version 2**. El
parche lo aplico `scripts/loop/_v192_parche_cuarta_puerta.py`, que es **idempotente
y CAE sin escribir nada si alguna de sus cuatro anclas no aparece**.

**LA COMPROBACION QUE ESTA TAREA SE DEBIA A SI MISMA, Y ES LA MISMA ENFERMEDAD DE
LA TAREA 3:** `vuelta182_tarea2_mutacion_apertura_auditor.py` **esta en la
nomina** y su sujeto es justo el fichero que acabo de tocar. Si su salida sellada
dejara de reproducir, **yo mismo habria roto la bateria de la 194 arreglando la
puerta que existe para no romperla**. Medido antes y despues, con el fichero ya
parcheado:

```
ANTES (identico a HEAD): disco 4982 bytes | LF 4982 bytes | sha256 LF ce85fd0cc659774c
exitcode del re corrido: 0
DESPUES:                 disco 4982 bytes | LF 4982 bytes | sha256 LF ce85fd0cc659774c
REPRODUCE BYTE A BYTE: True
```

Y `git status --porcelain` sobre esa ruta sale **vacio**, o sea identica a `HEAD`.
**Una sola entrada de la nomina nombra este fichero, y esa entrada sigue en
verde.**

**LO QUE ESTA TAREA NO HACE, DICHO PARA QUE NO SE BUSQUE:** no re escribe el acta
192 ni ninguna de sus cifras; los puestos 156 y 201 que el auditor quemo **siguen
declarados donde el los declaro**, y esta puerta no los recupera. **Lo que hace es
que la proxima vez no dependa de que alguien se acuerde**, que es lo que el propio
auditor pidio al levantarlo contra si mismo.
