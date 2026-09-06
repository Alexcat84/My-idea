# -*- coding: utf-8 -*-
r"""_v185_parche_esqueleto.py . EL PARCHE QUE CONVIERTE EL CLON DEL ESQUELETO DEL
REPORTE DE LA 184 EN EL DE LA 185.

Se guarda con nombre y no se tira, para que el clon sea auditable: quien quiera
saber que cambio entre vuelta184_esqueleto_reporte.py y
vuelta185_esqueleto_reporte.py tiene aqui el trozo exacto que se sustituyo, y
ademas scripts/loop/cotejar_clon_declarado.py lo mide por su cuenta. NO SE AFIRMA
QUE NINGUN DIFF SALGA VACIO: se publica lo que salga.

LO QUE CAMBIA, DECLARADO:
  1. EL DOCSTRING.
  2. `VUELTA`, de 184 a 185.
  3. `TAREAS`, que son las DOS de ESTE encargo.
  4. EL BLOQUE DE PROSA del encabezado del reporte, que cuenta que esta vuelta NO
     es de bateria, que su seccion 9 cierra con hueco declarado, y que su PASO 0
     ya no tiene reporte ajeno que archivar porque la TAREA 2.a lo archivo.

LA MAQUINA NO SE TOCA: `vuelta_del_reporte_del_arbol` sigue siendo el clon
declarado de `vuelta174_esqueleto_reporte.py`, y la guarda de la 4.b de la vuelta
180 sigue corriendo como PASO 0.0.

Y SE DECLARA LO QUE NO SE REPARA: `PATRONES_ACTA` sigue apuntando al acta de
`VUELTA - 1`, o sea la 184, cuando el acta que ORDENA esta vuelta es la 185. Es
el desfase que el reporte de la 184 marco como `D.2` y que el acta 185 adjudico a
favor CON REPARACION ENCARGADA. ESTA VUELTA NO LA EJECUTA: su encargo trae DOS
sub-tareas por el regimen 6.2 y ninguna de las dos es esta. Se declara en vez de
dejar que la celda hable sola.

USO:
  python scripts/loop/_v185_parche_esqueleto.py
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ORIGEN = os.path.join(RAIZ, "scripts", "loop", "vuelta184_esqueleto_reporte.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop", "vuelta185_esqueleto_reporte.py")
NL = chr(10)

DOCSTRING = '''# -*- coding: utf-8 -*-
r"""vuelta185_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 185,
TALLADO AL EMPEZAR PARA QUE UNA VUELTA CORTADA DEJE REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta184_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS y el bloque de prosa del encabezado. El cotejo del
clon lo hace scripts/loop/cotejar_clon_declarado.py y su salida se pega en el
reporte con lo que salga.

POR QUE SE TALLA EN EL PASO 4 DEL ORDEN DE ESTA VUELTA Y NO AL PRINCIPIO. Si este
esqueleto corriera antes, su PASO 0 archivaria el reporte de la 184 SIN CERRAR, y
la reparacion de la TAREA 1.c llegaria tarde para el unico reporte al que le
sirve. El reporte de la 184 se cierra ANTES, en la TAREA 2.a. En ningun momento
del orden el repo se queda sin reporte en disco.

Y EL PASO 0 SE CORRE IGUAL, SALGA LO QUE SALGA. Si la TAREA 2.a dejo el reporte
de la 184 archivado, este PASO 0 no tendra nada ajeno que archivar, Y ESO SE DICE
EN SU SALIDA en vez de dejar la fila muda.

ESTA VUELTA NO ES DE BATERIA (AUDITOR.md 6.1: corre cada cinco vueltas y la
siguiente es la 189), asi que la seccion 9 de este reporte cierra CON EL HUECO
DECLARADO Y MEDIDO: nombre del fichero, bytes medidos y atribucion, las tres
juntas o no vale.

EL TOPE SIGUE EN DOS SUB-TAREAS (AUDITOR.md 6.2): la 184 no cerro su propio
reporte y la cuenta de vueltas que cierran su reporte sigue en cero.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 185 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V185_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada:
no inventa un hash.

Y SE DECLARA EL DESFASE QUE NO SE REPARA: PATRONES_ACTA sigue pidiendo el acta de
VUELTA - 1, o sea la 184, cuando el acta que ORDENA esta vuelta es la 185. Es el
`D.2` del reporte de la 184, adjudicado a favor por la `5.2` del acta 185 CON
REPARACION ENCARGADA, y esta vuelta NO la ejecuta porque su encargo trae dos
sub-tareas y ninguna es esa.

USO:
  python scripts/loop/vuelta185_esqueleto_reporte.py
"""
'''

TAREAS_NUEVAS = '''TAREAS = [
    ("1", 'LOS REGISTROS Y LAS TRES REPARACIONES DE CODIGO. BLOQUEANTE. (a) El acta 185 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus siete adjudicaciones `5.1` a `5.7` todas a favor, los CUATRO pendientes de doctrina de la seccion 6 con su estado leido del titulo (`PD.2`, `PD.3` y `PD.4` CERRADAS por cita y `PD.1` ABIERTA con sus cinco puestos leidos del acta y no copiados del encargo), la caida propia del auditor `A.1` y la caida de reporte del ejecutor `R.1`, mas su caso positivo por mutacion sobre un acta FABRICADA con el esperado mutado cayendo, y la deuda de la serie REMEDIDA y no heredada del `R.46`. (b) LA SALIDA SELLADA DEL ARNES QUE PARO LA BATERIA DEJA DE CAMBIAR SOLA: funcion PURA `sin_temporal(linea, tmp)` aplicada ANTES del recorte, sin tocar lo que el arnes prueba, con arnes propio de DOS MITADES que fallan por separado. (c) LA GUARDA DE LA BATERIA CONTINUADA, que es la adjudicacion `6.2` del acta 185: `vuelta_que_sello()` y `tramos_por_vuelta()` nuevas, `rama_de_la_seccion9()` con un cuarto parametro que por defecto se comporta EXACTAMENTE como hoy, y una rama nueva que EXIGE MAS que la vieja con CUATRO condiciones a la vez, con la evidencia computada de git y sin ninguna bandera. (d) LA ESCALADA DE `AUDITOR.md` 1.2: la columna `quien lo sello` se computa en vez de teclearse, y el cotejo de las NUEVE celdas contra las que el reporte de la 184 ya lleva es la prueba. (e) LA RELECTURA AL DOBLE del tramo de la ciega del acta 185, con el cotejo de `sha256` contra el sello `V185b` ANTES de leer un solo puesto'),
    ("2", 'EL CIERRE DE DOS REPORTES: EL DE LA 184 Y EL DE LA 185. (a) El reporte de la 184 se cierra con la guarda ya reparada por la 1.c, DESPUES de cotejar sus tres piezas por `sha256` y por bytes contra lo que la 184 midio, con el veredicto de una linea TALLADO y no tecleado, y se archiva. (b) El reporte de la 185 se abre en su esqueleto, cada tarea anexa su fila al cerrarse, la cabecera se talla y `--comparar` tiene que dar CABECERA IDENTICA AL TALLADOR, y su SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO por el carril de `cerrar_reporte.py`: nombre del fichero, bytes medidos y atribucion, las tres juntas o no vale'),
]
'''

PROSA_NUEVA = '''> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que no lleva nada
> mas. **Cerro entera en la 184**, con sus nueve tramos sellados, asi que **la
> siguiente vuelta de bateria es la 189**. En las vueltas intermedias la seccion 9
> se cierra igual, con el **nombre del fichero, sus bytes medidos y su
> atribucion**, las tres juntas o no vale.
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y LA CUENTA SIGUE EN CERO.** El
> regimen `AUDITOR.md` 6.2 devuelve el tope a cinco cuando **dos vueltas seguidas
> cierren su propio reporte** con `scripts/loop/cerrar_reporte.py`. **La 184 no
> cerro el suyo** (`cerrar_reporte.py` exitcode 1, salida pegada entera en su
> reporte), asi que la cuenta **sigue en cero**. **Van dos tareas y no hay una
> tercera.**
>
> **EL TRABAJO DE ESTA VUELTA ES DESATASCAR EL CIERRE DEL REPORTE**, que lleva
> CUATRO vueltas sin conseguirse (181, 182, 183 y 184), y que es el mismo atasco
> por el que el fundador puso el regimen 6.2 el 5 sep.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee el
> par **2.464** ni ningun otro de la cola post fusion (encabeza el encargo de la
> **186**); no se cablea el instrumento de vigencia de las `A` rancias por `P.5`;
> **no se vuelve a decidir ninguna clase** en la relectura al doble; no se toca el
> marcador, ni un veredicto, ni `dataset/`; **no se poda la nomina de la bateria**,
> que es la opcion `c` que el fundador RECHAZO el 5 sep; y **no se repara el
> desfase del acta `VUELTA - 1`** de la `5.2`, que queda encargado y sin ejecutar
> porque el tope son dos sub-tareas.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py` y desde la 178 vuelve a correr en su sitio. **Una
> columna de apertura medida al cierre es caida que ACUMULA.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO YA NO TIENE REPORTE AJENO QUE ARCHIVAR, PORQUE
> LA TAREA 2.a LO ARCHIVO ANTES.** El orden de esta vuelta no es el de siempre y
> el motivo se dice: si el esqueleto corriera primero, su PASO 0 archivaria el
> reporte de la 184 **sin cerrar**, y la reparacion de la TAREA 1.c llegaria tarde
> para el unico reporte al que le sirve. **El PASO 0 se corre igual y su salida se
> pega con lo que salga**, diga lo que diga, en vez de dejar la fila muda.'''


def main():
    src = io.open(ORIGEN, encoding="utf-8").read().replace(chr(13) + NL, NL)
    fin_doc = src.index('"""', src.index('r"""') + 4) + 3 + 1
    cuerpo = src[fin_doc:]

    # 2. EL NUMERO DE VUELTA
    if "VUELTA = 184" not in cuerpo:
        raise SystemExit("ROJO: no encuentro 'VUELTA = 184' en el origen.")
    cuerpo = cuerpo.replace("VUELTA = 184", "VUELTA = 185", 1)

    # 3. LAS TAREAS
    i0 = cuerpo.index("TAREAS = [")
    i1 = cuerpo.index("def git(args):")
    cuerpo = cuerpo[:i0] + TAREAS_NUEVAS + NL + NL + cuerpo[i1:]

    # 4. EL BLOQUE DE PROSA
    j0 = cuerpo.index("> **ESTA VUELTA VUELVE A SER DE BATERIA")
    j1 = cuerpo.index("**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**")
    cuerpo = cuerpo[:j0] + PROSA_NUEVA + NL + NL + cuerpo[j1:]

    texto = DOCSTRING + cuerpo
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITO: %s" % DESTINO)
    print("CIFRA bytes: %d | CIFRA lineas: %d"
          % (len(texto.encode("utf-8")), texto.count(NL)))
    print("CIFRA apariciones de 'VUELTA = 185': %d" % texto.count("VUELTA = 185"))
    print("CIFRA apariciones de 'VUELTA = 184': %d" % texto.count("VUELTA = 184"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
