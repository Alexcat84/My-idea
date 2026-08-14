# PARA ALEXIS: el bucle esta DETENIDO en la fase 01 de la FASE III. Doctrina nueva necesaria, dos casos

**Escrito por el auditor (Fable 5), vuelta 25, 14 ago 2026.** El acta completa esta en
`docs/loop/ACTA_AUDITOR.md`, vuelta 25. `docs/loop/PROMPT_SIGUIENTE.md` queda VACIO a
proposito: no hay encargo hasta tu decision.

## EL ESTADO EXACTO, todo verificado por mi con instrumento hoy

- **Rama `pasada-unica`, HEAD `6a4d7042`**, arbol limpio, empujado a `origin`.
- **LA FASE 0 ESTA CERRADA Y VERIFICADA:** `OP-C-01`, `OP-C-02`, `OP-C-03`, `OP-S-06`,
  `OP-S-07` y `OP-C-04` ejecutadas; `OP-C-05` diferida por su `depende_de` (`OP-S-12`).
  Verifique `OP-S-07` entrada por entrada contra el diff (66 retiradas exactas, 59
  ficheros, cero campos ajenos tocados, las 48 inertes intactas, 16.866 a 16.800) y
  reproduje yo mismo el caso positivo de las dos guardas de `OP-C-04`: caen con nombre
  exacto sobre el estado malo y el catalogo limpio queda en verde. La prueba del camino
  A que elegiste esta medida: `symmetrize_added` paso de 33 a CERO.
- **Gate 0 verde por el ciclo escrito, corrido entero por mi:** exit 0, `GATE 0: OK`,
  71 etiquetas sin encoger, blob `8d47ff32` byte identico a HEAD, punto fijo.
- **Suites por mi:** motor 24/24, web 1.030 pasadas y 3 saltadas en 80 ficheros,
  `tsc` limpio.
- **El marcador:** n 3.388, A 583, B 89, C 7, D 2.709, cero huecos. Sin cambios: esta
  fase no lee pares.
- **La fase 01 quedo abierta y detenida:** `OP-F-01` verifica en verde HOY pero NO esta
  hecha (su segunda linea es condicion de fin de fase); `OP-F-03` es ejecutable pero se
  difirio con prudencia; `OP-F-02` y `OP-F-04-HOR` son la parada.
- **Credito de la tanda:** una caida de REPORTE del ejecutor (dijo "2 nodos sin enlaces
  entrantes las cinco veces" y era 6 en cuatro de ellas; el fondo es benigno y esta
  medido: cuatro gemelos deprecados que perdieron su unica entrada con las 66). Fuera
  del marcado, tramo releido al doble, cero discrepancias mas. NO acumula para parada.

## EL MOTIVO DE LA PARADA: dos casos que ninguna regla escrita cubre

### Caso 1: `background_startup_vs_corporativo` esta clasificado dos veces y las dos se excluyen

- **`OP-F-01`** lo tiene en la clase LARGO LEGITIMO (adjudicacion: MANDA LA CLASE, sus
  7 miembros) y su verificacion exige *"ningun nodo de la clase queda con pasos
  alterados"*. Sus 9 pasos serian una lista legitima entera.
- **`OP-F-04-HOR`** lo tiene en la tanda de los injertos de Horowitz, LEIDO y CONFIRMADO,
  con frontera publicada dos veces en `01_FUENTES.md`: **pasos 1 a 4 de Wasserman, 5 a 9
  de Horowitz**. Por `P.3` el bloque del mismo tema SE REPARTE OBLIGATORIAMENTE: separar
  deja el nodo en 4 pasos y tumba la verificacion de `OP-F-01`.
- **La raiz:** el mismo hecho (declarar dos libros) es lo que lo mete en la clase de
  `OP-F-01` (*"rompe la exclusividad de los manuales"*) y lo que lo firma como injerto
  por `P.2`. Hay DOS lecturas adjudicadas el mismo dia en direcciones opuestas, y el
  `orden` de la fase dice quien corre primero, no que verificacion gana al cerrar.
- **Toda salida reescribe letra adjudicada** (sacarlo de una clase o de la otra, o
  partir su verificacion), y eso en esta campana se hace por CORRECCION DECLARADA con
  decision tuya, como las dos de `OP-S-07`.

**Lo que se necesita de ti (caminos posibles, elige o dicta otro):**

- **Camino A:** el nodo SALE de la clase de `OP-F-01` (queda en 6) y se desteje por
  `OP-F-04-HOR` con su frontera 1a4/5a9. La lectura del injerto es mas fuerte: esta
  confirmada contra los pasos, con frontera, mientras que su entrada en la clase se
  argumento por la fuente. Consecuencia: la clase pierde el miembro que "probaba" que el
  formato lista no es de los manuales, y esa prosa de `01_FUENTES.md` se corrige
  declarada. **Es el camino que yo recomiendo.**
- **Camino B:** el nodo SALE de la tanda de Horowitz (queda en 12) y conserva sus 9
  pasos como lista legitima. Consecuencia: contradice la lectura confirmada de la
  vuelta 20 y deja un injerto declarado sin reparto, contra P.2 y P.3.
- **Camino C:** doctrina general nueva de tu pluma sobre que verificacion manda cuando
  un nodo vive en dos operaciones (alcanza tambien a los tres cruces declarados de
  `OP-F-03` con `OP-D-01` y `OP-D-06`, y a cualquier futuro).

### Caso 2: `OP-F-02` no nombra el destino de la reunion

El bloque de IA de los tres nodos de Mollick (`future_scenarios_planning`, `gut_check`,
`brainstorming_divergente`) *"viaja ENTERO al racimo de supervision de la IA, que hoy
tiene DIEZ miembros"*. Pero `aristas_nuevas` esta vacio, `superviviente` es null, la
nomina de diez es PROVISIONAL por su propia nota, y **ningun miembro esta nombrado como
receptor, ni hay regla que diga si el bloque se funde en un miembro o forma nodo propio
dentro del racimo**. `P.3` resuelve hasta el nivel de familia, no de miembro. Elegir
destino seria decision de contenido de mi pluma o de la del ejecutor, y esa pluma no es
nuestra.

**Ademas les falta la frontera del bloque en cada uno de los tres** (la tanda de los 43
publica fronteras pero excluye a Mollick por definicion). **Esa mitad SI la deje
adjudicada por extension:** se lee cada nodo contra sus `pasos_accionables` y se escribe
la frontera en `01_FUENTES.md` antes de cortar, con el mismo metodo de la tabla de los
14 de Horowitz. Se ejecutara en la reanudacion; no desbloquea la operacion sin el
destino.

**Lo que se necesita de ti:** nombrar el destino (un miembro concreto del racimo, o
nodo propio dentro del racimo, o la regla general que lo decida, por ejemplo: *el bloque
va al miembro cuyo objeto coincida, decidido por lectura, y si ninguno coincide forma
nodo propio*). Con eso `OP-F-02` queda ejecutable.

## LO QUE YA QUEDO ADJUDICADO Y NO NECESITA DE TI (se registra al reanudar)

1. **El ciclo de Gate 0 gana un tercer comando condicional:** cuando una operacion
   cambia el grafo, tras reaplicar curaduria corre `sync_assets_web.py` (es el remedio
   escrito del propio validador), con la vara de las dos copias byte identicas a HEAD.
   El registro en `08_VERIFICACION.md` es TAREA 1 del proximo encargo.
2. **El blob de la linea base de `08_VERIFICACION.md` es registro historico, no vara:**
   se le anade una vez su calificador de corte; la vara operativa sigue siendo *byte
   identico al HEAD del momento* y la cifra vigilada es el conteo de 71 etiquetas.
3. **`SALIDA_V24_OPC04_ANTES_DEL_ARREGLO.txt` se conserva tal cual:** su nombre ya es
   la marca.

## PREGUNTAS QUE VIAJAN CON ESTA PARADA (decision tuya, no urgen para reanudar)

- **Tres implementaciones del resolutor** (TypeScript del motor, guarda de Gate 0,
  instrumento del ejecutor). Mi recomendacion: una sola fuente en Python para los
  scripts (la guarda importable) y un test de paridad contra el TypeScript; es codigo
  que ninguna operacion ordena, por eso no se toco.
- **El chequeo de gemelos del Gate no puede ver la divergencia que la operacion recien
  creo** (compara el snapshot de antes del paso 6); hoy la caza la suite del motor. Si
  quieres esa guarda dentro del Gate, es codigo nuevo.
- **Estado *ejecutada* para las operaciones del plan** (seis ya corrieron y las 71 dicen
  LISTA). Mi recomendacion: sin estado nuevo en caliente; evidencia por commit al
  cierre de cada fase.

## COMO RETOMAR

1. Decide el caso 1 (camino A, B, C u otro) y el caso 2 (el destino o su regla).
2. Escribe las CORRECCIONES DECLARADAS en las notas de las operaciones afectadas en
   `docs/plan/OPERACIONES.jsonl` (o dictalas y que la primera vuelta las escriba como
   TAREA 1, que es el patron de las dos de `OP-S-07`).
3. Relanza el bucle. El encargo de la primera vuelta sera: TAREA 1 los registros (las
   dos adjudicaciones pendientes de arriba mas tus correcciones), TAREA 2 la fase 01 por
   su orden (`OP-F-01`, `OP-F-02` con frontera leida y destino nuevo, `OP-F-03`,
   `OP-F-04-HOR`), con el modo continuo de `AUDITOR.md` seccion 3 tal como esta escrito.

Nada de lo reservado se toco: cero merges, `dataset/` byte identico a HEAD tras cada
corrida, los veredictos intactos, el `.env` fuera del repo.

DECISION DEL FUNDADOR (14 ago 2026): caso 1 por el camino A con la regla P.17; caso 2 por
regla de destino por lectura. Las tres preguntas: backlog post-campaña las dos de codigo;
sin estado ejecutada. La fase 01 arranca.
