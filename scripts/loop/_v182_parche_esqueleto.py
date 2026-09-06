# -*- coding: utf-8 -*-
r"""_v182_parche_esqueleto.py . EL PARCHE QUE CONVIERTE EL CLON DEL ESQUELETO DE
LA 181 EN EL DE LA 182.

Se guarda con nombre, como su hermano _v182_parche_apertura.py, para que el clon
sea auditable: aqui esta el trozo exacto que cambia, y
scripts/loop/cotejar_clon_declarado.py lo mide por su cuenta.

LO QUE CAMBIA, Y ES TODO TEXTO SALVO LA LISTA DE TAREAS:
  1. El docstring, que cuenta de que va ESTA vuelta.
  2. VUELTA y la lista TAREAS, que pasa de DOS filas a CINCO.
  3. Los parrafos de prosa del encabezado del reporte, que en la 181 decian
     "ESTA ES LA VUELTA DE BATERIA" y "EL TOPE DE ESTA VUELTA ES DOS
     SUB-TAREAS". Las dos son falsas en la 182 y se sustituyen.

LA MAQUINA NO SE TOCA EN NINGUNA LINEA salvo el numero de vuelta.

USO:
  python scripts/loop/_v182_parche_esqueleto.py
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(RAIZ, "scripts", "loop", "vuelta182_esqueleto_reporte.py")
NL = chr(10)

DOC = '''r"""vuelta182_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA
VUELTA 182, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS CINCO TAREAS ENCARGADAS.

CLON DECLARADO de scripts/loop/vuelta181_esqueleto_reporte.py. Lo que se toca a
mano son las CINCO filas de tarea, que son las de ESTE encargo, y los parrafos de
prosa que hablan del estado del bucle. La maquina no se toca en ninguna linea
salvo el numero de vuelta.

Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA: el cotejo lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte, que es
obligatorio desde la vuelta 178 por el docstring de aquel fichero. Este texto NO
publica ningun resultado de diff.

POR QUE ESTA VUELTA TRAE CINCO FILAS Y NO DOS. La adjudicacion 6.8 del acta 180
bajo el tope a DOS en la 181 porque era vuelta de bateria y AUDITOR.md 6.1 manda
que la vuelta de bateria no lleve nada mas; y esa misma adjudicacion escribio,
con estas palabras, "El tope vuelve a cinco en la 182". El encargo de esta vuelta
trae CINCO y dice "que es el tope. Ni una mas".

Y ESTA VUELTA NO ES DE BATERIA. La 181 era la suya y se corto antes de lanzarla.
La decision del fundador del 5 sep 2026 (PREGUNTA 4 de
docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md) manda que la bateria
corra POR TRAMOS RESUMIBLES, y la TAREA 5 de este encargo la deja preparada y
declarada para la 183. La seccion 9 del reporte cierra con su HUECO DECLARADO Y
MEDIDO, que es lo que AUDITOR.md 6.1 manda para las vueltas intermedias.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0, antes que nada.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 182 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta de la vuelta anterior por las
DOS formas del titulo y en las DOS pasadas de TALLADOR.buscar_acta; HEAD de
apertura leido de docs/loop/SALIDA_V182_HEAD_APERTURA.txt, sellado antes de la
primera operacion; commit de nacimiento del bloque de apertura por
git log --diff-filter=A. Si alguno no se puede leer o es ambiguo, el esqueleto
CAE EN ROJO y no escribe nada: no inventa un hash.

USO:
  python scripts/loop/vuelta182_esqueleto_reporte.py
"""'''

TAREAS = '''TAREAS = [
    ("1", 'LOS REGISTROS Y LA DEUDA DE LECTURA. (a) El acta 181 y sus adjudicaciones entran en la serie de registros, con el numero que devuelve `scripts/loop/serie_de_registros.py` y no tecleado. (b) LOS DOS PENDIENTES DEL ACTA 180, que llevan una vuelta esperando y estan escritos en sus puntos `6.8` y `6.6`: el remedio del `E.1` sobre `scripts/loop/cerrar_reporte.py`, que es la rama que escribe la cabecera CORRIDA ENTERA Y SOLA sobre una seccion 9 cuyo cuerpo dice que nadie la corrio, y la `P.1`, el arnes `vuelta172_tarea1c_guarda_que_mordio.py`, que cae con exit 1 fallando 1 de 6 y esta fuera del censo: primero el esperado y despues el nombre, en ese orden, que es parte de la adjudicacion. (c) LA RELECTURA AL DOBLE del tramo de la ciega que el acta 181 encarga en su `7.2` por `AUDITOR.md` 1.2, sobre los 30 puestos que su seccion 8 lista'),
    ("2", 'LA APERTURA DEL AUDITOR COMO CODIGO (decision del fundador del 5 sep 2026, PREGUNTA 3, opcion c, la mitad que quita el problema de raiz; la otra mitad, que ROMPER UN REMEDIO ESCRITO ACUMULE, ya esta escrita en `AUDITOR.md`). Fichero GEMELO del bloque de apertura del ejecutor: corre `scripts/loop/aislador_de_ciega.py` y SELLA SU SALIDA ANTES de que el turno pueda tocar `git log`, `git status` o `docs/loop/REPORTE.md`. Con CASO POR MUTACION SOBRE VARIABLE COMPUTADA, no sobre constante literal (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): si el sello se intenta DESPUES de tocar cualquiera de los tres, TIENE QUE CAER, y la prueba se corre cambiando el valor esperado para comprobar que el caso cae de verdad'),
    ("3", 'EL INSTRUMENTO DEL DIFERENCIADOR MOVIDO (decision del fundador del 5 sep 2026, PREGUNTA 1, la `b`). Cruza LA RAZON ESCRITA de cada `D` contra LOS PASOS DE HOY del otro nodo, y SOLO las `D` con la lesion exacta vuelven a la cola. CASO POSITIVO OBLIGATORIO: EL PUESTO 2.464 TIENE QUE SALIR NOMBRADO; si no sale, el instrumento no sirve y se dice. Y EL CENSO POR ESTADO DE LAS `A` en el mismo instrumento: ejecutadas contra pendientes, con LAS PENDIENTES DE TEXTO MOVIDO MARCADAS RANCIAS POR `P.5`. Las `A` NO ganan cola nueva: la ejecutada es cosa consumada y la pendiente ya la cubre `P.5`'),
    ("4", 'LAS `D` QUE EL INSTRUMENTO NOMBRE ENTRAN A LA COLA de relectura post fusion de `docs/plan/08_VERIFICACION.md`, y se releen POR TRAMOS en las vueltas siguientes. En esta vuelta SE ENTRA A LA COLA Y SE DECLARA EL TRAMO; no se releen 543 pares, que es justo lo que la decision del fundador evita al conceder la `b` y no la `c`'),
    ("5", 'LA VUELTA DE BATERIA VA EN LA 183, POR TRAMOS RESUMIBLES (decision del fundador del 5 sep 2026, PREGUNTA 4, opcion `a`, con el precedente de los nueve tramos de la vuelta 176). Aqui SOLO se deja preparada y declarada: nueve tramos, cada uno se commitea CON SU SALIDA SELLADA al terminar, una vuelta cortada RETOMA EN EL TRAMO SIGUIENTE, y la bateria se declara corrida cuando LOS NUEVE tienen salida sellada DEL MISMO CALIBRE. En esta vuelta la seccion 9 del reporte cierra con su HUECO DECLARADO Y MEDIDO, como el regimen `6.1` manda'),
]'''

PROSA_VIEJA = '''> **ESTA ES LA VUELTA DE BATERIA, Y NO LLEVA NADA MAS.** `AUDITOR.md` 6.1: la
> bateria corre CADA CINCO, en VUELTA PROPIA. La cadencia se adjudico en el acta
> 176 punto 7.8, se reconfirmo en las actas 178 y 179, y el acta 180 la clava por
> cuarta vez en su punto 10 con estas palabras: *"LA BATERIA: LA PROXIMA ES LA
> 181, Y ES LA VUELTA QUE VIENE"*. **La 180 fue la ULTIMA que declaro el hueco.
> Aqui se corre.**
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y NO ES UN DESCUIDO: ES LA
> ADJUDICACION 6.8 DEL ACTA 180.** `AUDITOR.md` 6.2 devolvio el tope a cinco, pero
> la 6.1 y la 6.2 salen de la MISMA parada del 5 sep 2026 y la 6.2 se concedio
> *"combinada con la (a)"*, o sea subordinada a ella. **La vuelta de bateria no
> lleva trabajo de plan al lado.** El tope vuelve a cinco en la 182.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se lee ningun
> par, no se escribe ningun veredicto, no se toca el marcador, no se toca el estado
> de ninguna ficha, no se toca `docs/plan/`, no se arregla la `P.1` y no se toca
> `cerrar_reporte.py`. **Las dos ultimas van a la 182 y estan escritas en los
> puntos 6.6 y 6.8 del acta 180.**'''

PROSA_NUEVA = '''> **ESTA VUELTA NO ES DE BATERIA, Y ESO TAMBIEN ES LETRA.** `AUDITOR.md` 6.1: la
> bateria corre CADA CINCO, en VUELTA PROPIA. **La 181 era la suya y se corto
> antes de lanzarla**, y su acta lo registra en el punto 7.5 sin contarlo como
> caida de reporte, porque el esqueleto por anexion dejo la fila diciendo ABIERTA,
> SIN CERRAR y no publico ninguna cifra de una corrida que no hubo. La decision
> del fundador del **5 sep 2026** (PREGUNTA 4 de
> `docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md`) manda que corra
> **POR TRAMOS RESUMIBLES**, y la **TAREA 5** de este encargo la deja preparada y
> declarada para la **183**. **La seccion 9 de este reporte cierra con su HUECO
> DECLARADO Y MEDIDO**, que es lo que el regimen 6.1 manda para las vueltas
> intermedias: un hueco declarado no es un hueco escondido.
>
> **EL TOPE DE ESTA VUELTA ES CINCO SUB-TAREAS, Y TAMPOCO ES UNA GANA.** La
> adjudicacion **6.8 del acta 180** bajo el tope a DOS en la 181 porque era vuelta
> de bateria, y en la misma frase escribio: *"El tope vuelve a cinco en la 182"*.
> El encargo de esta vuelta trae **CINCO** y dice *"que es el tope. Ni una mas"*.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee
> ninguno de los 543 pares que la TAREA 4 mete en la cola (eso es justo lo que la
> decision del fundador evita al conceder la `b` y no la `c`), no se toca el
> marcador, no se cambia ningun veredicto del archivo, y **las `A` no ganan cola
> nueva** por la PREGUNTA 2 de la misma decision. **Y no se corre la bateria**: se
> prepara.'''


def main():
    t = io.open(P, encoding="utf-8").read().replace(chr(13) + NL, NL)
    i = t.index('r"""')
    j = t.index('"""', i + 4) + 3
    t = t[:i] + DOC + t[j:]
    t = t.replace("VUELTA = 181", "VUELTA = 182", 1)
    ini = t.index("TAREAS = [")
    fin = t.index("]", t.index('("2", '))
    while t[fin - 1] != NL:
        fin = t.index("]", fin + 1)
    t = t[:ini] + TAREAS + t[fin + 1:]
    if PROSA_VIEJA not in t:
        raise SystemExit("ROJO: no se encontro la prosa vieja del encabezado")
    t = t.replace(PROSA_VIEJA, PROSA_NUEVA, 1)
    t = t.replace("## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO",
                  "## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO", 1)
    io.open(P, "w", encoding="utf-8", newline=NL).write(t)
    print("PARCHE DEL ESQUELETO APLICADO sobre %s" % P)
    print("bytes ahora: %d | lineas: %d" % (len(t.encode("utf-8")), t.count(NL)))


if __name__ == "__main__":
    main()
