# -*- coding: utf-8 -*-
r"""_v183_tallar_esqueleto.py . TALLA scripts/loop/vuelta183_esqueleto_reporte.py
COMO CLON DECLARADO DEL DE LA 182.

La maquina no se toca en ninguna linea salvo el numero de vuelta: lo que se
reescribe a mano son el docstring y las DOS filas de tarea, que son las de ESTE
encargo. El cotejo del clon lo hace scripts/loop/cotejar_clon_declarado.py y su
salida se pega en el reporte con lo que salga: este fichero NO publica ningun
resultado de diff.
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)
ORIG = os.path.join(RAIZ, "scripts", "loop", "vuelta182_esqueleto_reporte.py")
DEST = os.path.join(RAIZ, "scripts", "loop", "vuelta183_esqueleto_reporte.py")

t = io.open(ORIG, encoding="utf-8").read().replace(chr(13) + NL, NL)

# ------------------------------------------------------------- EL DOCSTRING
d0 = t.index('r"""')
d1 = t.index('"""', d0 + 4) + 3
DOC = 'r"""' + '''vuelta183_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA
VUELTA 183, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS DOS TAREAS ENCARGADAS.

CLON DECLARADO de scripts/loop/vuelta182_esqueleto_reporte.py. Lo que se toca a
mano son las DOS filas de tarea, que son las de ESTE encargo, y los parrafos de
prosa que hablan del estado del bucle. La maquina no se toca en ninguna linea
salvo el numero de vuelta.

Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA: el cotejo lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte, que es
obligatorio desde la vuelta 178 por el docstring de aquel fichero. Este texto NO
publica ningun resultado de diff.

POR QUE ESTA VUELTA TRAE DOS FILAS Y NO CINCO. El regimen temporal de AUDITOR.md
6.2 devuelve el tope a cinco cuando DOS vueltas seguidas cierren su propio reporte
con scripts/loop/cerrar_reporte.py. El acta 182, punto 8, midio que la 181 NO
cerro el suyo y que la 182 SI: la cuenta va por UNA. Si la 183 cierra el suyo,
seran dos seguidas y el tope vuelve a cinco en la 184.

Y ESTA VUELTA SI ES DE BATERIA. AUDITOR.md 6.1: la bateria corre CADA CINCO, en
vuelta propia, y esa vuelta no lleva trabajo de plan al lado. La 181 era la suya y
se corto antes de lanzarla. Su seccion 9 lleva LA BATERIA ENTERA dentro, no un
hueco declarado: esta vez si es su vuelta.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0, antes que nada.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 183 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta de la vuelta anterior por las
DOS formas del titulo y en las DOS pasadas de TALLADOR.buscar_acta; HEAD de
apertura leido de docs/loop/SALIDA_V183_HEAD_APERTURA.txt, sellado antes de la
primera operacion; commit de nacimiento del bloque de apertura por
git log --diff-filter=A. Si alguno no se puede leer o es ambiguo, el esqueleto
CAE EN ROJO y no escribe nada: no inventa un hash.

USO:
  python scripts/loop/vuelta183_esqueleto_reporte.py
''' + '"""'
t = t[:d0] + DOC + t[d1:]

# --------------------------------------------------------- EL NUMERO DE VUELTA
t = t.replace("VUELTA = 182", "VUELTA = 183")

# ------------------------------------------------------------- LAS DOS TAREAS
s0 = t.index("TAREAS = [")
s1 = t.index(NL + "]" + NL, s0) + len(NL + "]")
T1 = ('LOS REGISTROS Y LA ESCALADA, BLOQUEANTE Y ANTES DE LA BATERIA. '
      '(a) El acta 182 entra en la serie de registros con el numero que devuelve '
      '`scripts/loop/serie_de_registros.py` y no tecleado, con sus adjudicaciones '
      '`5.D.1` a `5.D.7` y `7.1` a `7.5`, su caida propia del auditor y las dos del '
      'ejecutor, y su caso por mutacion. '
      '(b) LA DEUDA DE OCHO REGISTROS SE DOCUMENTA COMO SALTO Y NO SE RELLENA: una '
      'sola linea de constancia en la serie, en su sitio, con la cifra contada por '
      'el instrumento. '
      '(c) LA ESCALADA DE `AUDITOR.md` 1.2, que es la operacion de codigo de esta '
      'vuelta: `scripts/loop/cerrar_reporte.py` gana una funcion PURA con arnes '
      'propio que coteja los numerales del veredicto de una linea contra lo que el '
      'cuerpo permite contar (caidas propias `C.n` de la seccion 8 y filas de la '
      'tabla de tareas), lee los numerales TAMBIEN escritos con letra, y CAE EN ROJO '
      'sin escribir nada si no calzan. Con caso positivo POR MUTACION SOBRE VARIABLE '
      'COMPUTADA. '
      '(d) EL HUECO DE LA SECCION 9 TIENE QUE DECIR SI EL FICHERO NO EXISTE O SI MIDE '
      'CERO, que hoy los confunde en un `max(tam, 0)`, sin tocar las tres piezas que '
      'el hueco ya exige. '
      '(e) LA RELECTURA AL DOBLE del tramo de la ciega: los 30 puestos de la seccion '
      '9 del acta 182 y sus 30 vecinos deterministas, mecanica y con la vara, sin '
      'volver a decidir la clase de ningun par')
T2 = ('LA BATERIA DE MUTACIONES, ENTERA Y POR TRAMOS. '
      '`scripts/loop/vuelta183_bateria_por_tramos.py`, escrito y medido en la 182 y '
      'sin correr. Cada tramo se commitea CON SU SALIDA SELLADA al terminar, antes '
      'de seguir; una vuelta cortada RETOMA EN EL TRAMO SIGUIENTE y cual toca lo dice '
      '`--siguiente`; la bateria se declara corrida cuando LOS NUEVE tienen salida '
      'sellada DEL MISMO CALIBRE; una salida sellada que mide CERO BYTES no cuenta '
      'como hecha; la doble corrida y todas las demas guardas siguen enteras, y lo '
      'unico que cambio es la cadencia. El reloj de cada tramo se mide al cerrarlo y '
      'se publica medido: la estimacion del `--plan` es estimacion y se dice como '
      'tal. Si un arnes cae en rojo, el ejecutor se detiene ahi y lo trae con su '
      'salida entera')
BLOQUE = "TAREAS = [" + NL
BLOQUE += '    ("1", %r),' % T1 + NL
BLOQUE += '    ("2", %r),' % T2 + NL
BLOQUE += "]"
t = t[:s0] + BLOQUE + t[s1:]

io.open(DEST, "w", encoding="utf-8", newline=NL).write(t)
print("ESCRITO %s" % DEST)
print("CIFRA bytes: %d | CIFRA lineas: %d" % (len(t.encode("utf-8")), t.count(NL)))

# ------------------------------------------------- LA PROSA DEL ESTADO DEL BUCLE
# LO QUE SE SUSTITUYE AQUI ES PROSA, NO MAQUINA: son los parrafos que hablan del
# regimen de ESTA vuelta, y decirlos con la letra de la anterior seria publicar
# una afirmacion de estado sin medirla (EJECUTOR.md 1).
t2 = io.open(DEST, encoding="utf-8").read().replace(chr(13) + NL, NL)

VIEJO_BAT = t2[t2.index("> **ESTA VUELTA NO ES DE BATERIA"):
               t2.index("> **LO QUE NO ENTRA EN ESTA VUELTA")]
NUEVO_BAT = '''> **ESTA VUELTA SI ES DE BATERIA, Y ESO MANDA SOBRE TODO LO DEMAS.**
> `AUDITOR.md` 6.1: la bateria corre CADA CINCO, en **VUELTA PROPIA**, y esa
> vuelta **no lleva trabajo de plan al lado**. **La 181 era la suya y se corto
> antes de lanzarla.** La decision del fundador del **5 sep 2026** (PREGUNTA 4 de
> `docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md`) la manda **por
> tramos resumibles**, y su lanzador,
> `scripts/loop/vuelta183_bateria_por_tramos.py`, esta escrito desde la 182 y sin
> correr. **La seccion 9 de este reporte lleva la bateria entera dentro, no un
> hueco: esta vez si es su vuelta.**
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y NO ES INERCIA: ESTA MEDIDO.** El
> regimen `AUDITOR.md` 6.2 devuelve el tope a cinco cuando **dos vueltas seguidas
> cierren su propio reporte** con `scripts/loop/cerrar_reporte.py`. El acta 182,
> punto 8, lo midio: **la 181 NO cerro el suyo** y **la 182 SI**, asi que la
> cuenta va por **UNA**. **Si la 183 cierra el suyo, seran dos seguidas y el tope
> vuelve a cinco en la 184.**
>
'''
t2 = t2.replace(VIEJO_BAT, NUEVO_BAT)

VIEJO_NO = t2[t2.index("> **LO QUE NO ENTRA EN ESTA VUELTA"):
              t2.index("> **Y ESTA VUELTA MIDE SU DESFASE")]
NUEVO_NO = '''> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee
> ningun par de los 543 ni se toca la cola de `docs/plan/08_VERIFICACION.md` (su
> TRAMO 1 es el par **2.464** y se relee cuando haya vuelta de trabajo, no en la
> de bateria); no se cablea el instrumento de vigencia de las ocho `A` rancias por
> `P.5`; no se toca el marcador, ni un veredicto, ni `dataset/`; y **no se poda la
> nomina de la bateria**, que es la opcion `c` que el fundador RECHAZO el 5 sep.
>
'''
t2 = t2.replace(VIEJO_NO, NUEVO_NO)

# LA %(ant)d NO ARCHIVO SU REPORTE, Y ESO SE DICE MEDIDO EN VEZ DE HEREDAR LA
# FRASE DE LA VUELTA ANTERIOR, QUE DECIA LO CONTRARIO.
VIEJO_P0 = t2[t2.index("> **Y EL PASO 0 DE ESTE ESQUELETO"):
              t2.index(NL + NL + "**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**")]
NUEVO_P0 = '''> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Las dos preguntas vuelven a coincidir en el numero, pero
> **no en el estado**: la %(ant)d **cerro su reporte con `cerrar_reporte.py` y NO
> lo archivo en su misma vuelta**, cosa que el bloque de apertura de hoy midio
> (`docs/loop/SALIDA_V%(v)d_APERTURA.txt`, bloque H.4: `REPORTE_V182.md
> archivado: NO`). **Lo archiva el PASO 0 de este esqueleto, antes de escribir
> una sola linea encima**, y su salida se pega abajo con lo que salga.'''
t2 = t2.replace(VIEJO_P0, NUEVO_P0)

t2 = t2.replace("## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO",
                "## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO")

io.open(DEST, "w", encoding="utf-8", newline=NL).write(t2)
print("PROSA SUSTITUIDA. CIFRA bytes: %d | CIFRA lineas: %d"
      % (len(t2.encode("utf-8")), t2.count(NL)))
