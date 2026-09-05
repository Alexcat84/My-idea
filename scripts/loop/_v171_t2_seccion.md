### TAREA 2 (BLOQUEANTE PARA LA 3). EL BORRADOR QUE ENVENENO UN INSTRUMENTO

**LOS CINCO SALIERON, Y NO SIRVIO DE NADA: LAS DOS VARAS NO CONVERGEN. PARO Y LO
TRAIGO, QUE ES LO QUE EL ENCARGO MANDA CON ESAS PALABRAS.** Instrumentos
`scripts/loop/vuelta171_tarea2_sacar_borradores.py` (**exit 1**, y sale en 1 a
proposito: su guarda es la que cae) y
`scripts/loop/vuelta171_tarea2_atribuir_universo.py` (**exit 0**).

**EL MOVIMIENTO SI SE HIZO, ENTERO Y SIN PERDER NADA:** `git mv` de los cinco
`docs/loop/_v170_t*_seccion.md` a `scripts/loop/`, **5 de 5 con sha256 identico
en el destino y 0 de 5 quedando en `docs/loop/`**, comprobado fichero a fichero
(`docs/loop/SALIDA_V171_T2_SACAR_BORRADORES.txt`, bloque E). **Nada se borro y
nada se edito.**

**LAS TRES LECTURAS QUE EL ENCARGO PIDE, MAS UNA CUARTA QUE HIZO FALTA**, todas
del contador `scripts/loop/vuelta48_contar_ld.py` corrido por mi en esta vuelta,
las de corte viejo sobre WORKTREE LIMPIO y no sobre el arbol de hoy:

| lectura | hechas | mayor de las hechas | mayor del universo | huecos | sin seccion |
|---|---:|---:|---:|---:|---:|
| `222ca6a7`, worktree limpio | 82 | **LD-138** | **LD-138** | 54 | 2 |
| `0caca89f` (HEAD de apertura), worktree limpio | 82 | LD-138 | **LD-154** | 64 | 8 |
| HEAD, ANTES de mover | 82 | LD-138 | **LD-154** | 64 | 8 |
| HEAD, DESPUES de mover | 82 | **LD-138** | **LD-154** | 64 | 8 |

**TU CIFRA DE 54 ERA CIERTA Y LA REPRODUJE EXACTA**, y tambien reproduje exacta
la de 64 con sus 8. **Pero mover los cinco no movio ni una cifra**, y eso es lo
que hay que explicar.

**LA CAUSA, MEDIDA Y NO SUPUESTA** (`docs/loop/SALIDA_V171_T2_ATRIBUCION.txt`,
bloque B, y `docs/loop/SALIDA_V171_T2_LAS_DOS_FUENTES.txt`). **Los ocho numeros
son los mismos ocho; lo que cambio por completo es DE DONDE SALEN.** En
`0caca89f` los seis de mas venian TODOS de `docs/loop/_v170_t4_seccion.md`, que
es lo que el acta 170 midio. Hoy, con ese fichero ya fuera de `docs/`, los mismos
seis vienen de **dos ficheros que en `0caca89f` no los nombraban, y los dos los
ha escrito ESTA VUELTA**:

| fuente de hoy | que numeros trae | de donde sale |
|---|---|---|
| `docs/loop/reportes/REPORTE_V170.md` | `LD-12`, `LD-27`, `LD-100`, `LD-137`, `LD-139`, `LD-154` | **NO EXISTIA en `0caca89f`**; lo crea la TAREA 1.d de esta vuelta (`git log --diff-filter=A` lo ancla en `dd34047a`) |
| `docs/PENDIENTES.md` | `LD-12`, `LD-27`, `LD-139`, `LD-154` | **cero apariciones en `0caca89f`, una hoy**, y esta en UNA sola linea, `docs/PENDIENTES.md:12296`, que es la glosa de la adjudicacion `6.1` dentro del `R.40` que escribio la TAREA 1.a de esta vuelta |

**Y LA PRIMERA DE LAS DOS TIENE UNA PRUEBA QUE NO ADMITE DISCUSION:** el sha256
(LF) de `docs/loop/reportes/REPORTE_V170.md` es
`0b85f30e9c78e2b4d59e19deb9aa30d61d3724800bd54e7309246fb405bd1e16`, **y el
sha256 de `docs/loop/REPORTE.md` en `ca55afd8` es exactamente el mismo**. O sea
que el contador esta contando, como si fuera un encargo, **un fichero que es
BYTE A BYTE el mismo que el contador ya excluye por NARRATIVO DEL BUCLE**.

**LO QUE ESTO ES, DICHO SIN ADORNO: LA VUELTA 170 ENVENENO EL CONTADOR CON UN
BORRADOR, Y ESTA VUELTA LO HA ENVENENADO CON DOS COSAS SUYAS AL SACAR EL
BORRADOR.** Y la segunda es peor que la primera por una razon que hay que decir:
el borrador de la 170 era un fichero suelto que alguien podia mover. **El
archivado nace de un automatismo que esta misma vuelta acaba de enchufar** (la
TAREA 5.a), asi que **a partir de ahora cada vuelta deja un
`docs/loop/reportes/REPORTE_V<N>.md` bajo `docs/` sin que nadie tenga que
acordarse**. Es exactamente la especie ancha que el acta 170 subio al fundador en
su seccion 7.3: *"cualquier fichero nuevo bajo `docs/` puede mover la lectura de
un instrumento que barra `docs/`"*.

**NO ACUSO DE MAS:** los otros dos reportes archivados no nombran ningun `LD` sin
seccion (`REPORTE_V168.md` no nombra ninguno; `REPORTE_V169.md` nombra `LD-66` a
`LD-70`, que **si** tienen seccion propia y por eso no entran en la cuenta).

**LA GUARDA, Y CAE:** el mayor de las HECHAS da `LD-138` y el mayor del UNIVERSO
da `LD-154`. **No convergen. LA TAREA 3 NO SE CORRE**, y no por prudencia: si se
corriera, *"el siguiente libre es el mayor mas uno"* sobre este universo daria
**`LD-155`** y no `LD-139`, que es justo la cifra falsa que la guarda existe para
impedir.

**Y NO ARREGLO NINGUNA DE LAS DOS FUENTES, Y DIGO POR QUE.** Para la primera hay
un remedio de una linea (excluir `docs/loop/reportes/REPORTE_V<N>.md` con la
misma vara y por el mismo motivo que los tres narrativos del bucle) y creo que
cabe entero dentro de la adjudicacion `6.3`, que dice que la exclusion **ya
esta** en el instrumento y solo hay que leerla *"sin hacerse el tonto con el
nombre del fichero"*. **Pero el acta 170 reservo al fundador la guarda general
sobre ficheros nuevos bajo `docs/`**, y tocar la lista de exclusiones del
contador es tocar esa guarda. Para la segunda no hay remedio de instrumento
ninguno: `docs/PENDIENTES.md` **si** es un sitio donde cabe un encargo, por el
criterio escrito del propio contador, asi que excluirlo seria doctrina nueva y
ademas mala. **Las dos suben en `PD.1` y en `P.1`, con mi propuesta escrita y
sin ejecutarla.**
