# -*- coding: utf-8 -*-
"""vuelta54_correcciones_tarea1.py . LOS CUATRO REGISTROS ADJUDICADOS DE LA
TAREA 1 DE LA VUELTA 54, CADA UNO EN SU SEDE.

POR QUE EXISTE COMO INSTRUMENTO Y NO COMO EDICION A MANO: la regla 1 del
EJECUTOR (cuarto renglon, LA TABLA SE IMPRIME, NO SE TECLEA) nacio de las dos
paradas de credito de las vueltas 31 y 32, las dos por celdas manuales que
ningun instrumento validaba. Una sustitucion escrita aqui se puede RE-CORRER y
se puede DIFF-EAR; una celda tecleada, no.

LOS CUATRO PUNTOS:

  1.1 LA PRECISION DE LA ESTRELLA, ADOSADA AL 9.3.1 DEL BANCO. Nota NUEVA y
      fechada al final de la seccion 9.3.1 de docs/BANCO_DE_TEXTOS.md, SIN
      TACHAR NADA: cuando el GANADOR POR DERECHO de sus pares A es el CENTRO
      de una estrella cuyas puntas son D entre si, manda la receta de P.12 y
      el centro muere absorbido por el viable que el contenido elija. Piezas:
      adjudicaciones 2 y 3 del acta de la vuelta 50 y pregunta 1 del acta de
      la vuelta 53. Los tres ejemplares que la nota cita se MIDIERON EN ESTA
      VUELTA (scripts/loop/vuelta54_ejemplares_estrella.py).

  1.2 LAS DOS AMPLIACIONES DEL CARRIL GENERAL DE COLISIONES, adosadas al
      registro 1.4.b de la vuelta 53 en docs/plan/03_FUSIONES.md, cada una
      con su figura.

  1.3 EL ROTULO DEL CENSO DE DUPLICADAS DEL INSTRUMENTO DE FUNDIR
      (scripts/loop/vuelta48_fundir_tramo.py). Su censo tiene OTRA semantica
      que el instrumento publicado de OP-S-12. Se adosa la frase a los dos
      rotulos CON EL TEXTO VIEJO DELANTE. LA LOGICA NO SE TOCA.

  1.4 LA NOTA DE LOS 41 ENLACES, adosada al registro del tramo de la vuelta 53
      en docs/plan/03_FUSIONES.md, con las cifras RE-MEDIDAS EN ESTA VUELTA
      por scripts/loop/vuelta54_41_enlaces.py y no copiadas del acta.

IDEMPOTENTE: cada sustitucion comprueba primero si su resultado ya esta
escrito, y entonces no hace nada y lo dice. Re-correrlo no duplica ninguna nota.

Uso: python scripts/loop/vuelta54_correcciones_tarea1.py [--simular]
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BAN = os.path.join(RAIZ, "docs", "BANCO_DE_TEXTOS.md")
FUS = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
FUN = os.path.join(RAIZ, "scripts", "loop", "vuelta48_fundir_tramo.py")

# ==========================================================================
# 1.1 LA PRECISION DE LA ESTRELLA, al final de la seccion 9.3.1 del BANCO.
# El ancla es el cierre del VISTO SEGUNDO mas el salto a la seccion 9.3, que
# es unico en el fichero. NADA SE TACHA: la nota se ADOSA.
# ==========================================================================
ANCLA_BAN = """`accion_correctiva`.

---

### 9.3 Una dirección de fusión decidida sobre un par no sobrevive a su familia"""

NOTA_ESTRELLA = """`accion_correctiva`.

#### PRECISIÓN ADJUDICADA EL 20 ago 2026 (vuelta 54, TAREA 1.1 del encargo; acta de la vuelta 53, pregunta 1): **EL GANADOR POR DERECHO QUE ES CENTRO DE UNA ESTRELLA MUERE**

**Nada de lo de arriba se tacha ni se corrige: esta precisión NO dice que el 9.3.1 estuviera
mal. Dice dónde termina lo que legisla.**

> **CUANDO EL GANADOR POR DERECHO DE SUS PARES `A` ES EL CENTRO DE UNA ESTRELLA CUYAS PUNTAS
> SON `D` ENTRE SÍ, MANDA LA RECETA DE `P.12`: EL CENTRO NO ES VIABLE Y MUERE ABSORBIDO POR
> EL VIABLE QUE EL CONTENIDO ELIJA.**

**LAS PIEZAS, y ninguna es nueva:**

| pieza | lo que aporta |
|---|---|
| **adjudicación 2 del acta de la vuelta 50** | **en la estrella el centro muere UNA vez**, absorbido por el viable que el contenido elija, y las puntas se leen por `P.12` contra ese superviviente. **No excluye a ningún centro por su historial de pares** |
| **adjudicación 3 del acta de la vuelta 50** | el motivo de fondo: la fórmula *Sobrevive X* es **el cierre de una razón de PAR**, y el racimo, no el par, decide. **Lo escribe el propio archivo en el puesto 2.237** |
| **acta de la vuelta 53, pregunta 1** | la adjudicación, por extensión citable y **sin doctrina nueva**: los tres actos NO se deshacen |

**POR QUÉ NO HAY CONTRADICCIÓN.** El 9.3.1 fija al ganador **DE SUS PARES** para poder
escribir la operación **cuando el acto se funde entero**, que es lo que hacen sus dos
ejemplares (la regla kp y la ISO sectorial). **No legisla la estrella que deja un mixto
fuera**, que es figura posterior y específica. **La frase *no hay lectura pendiente ni futura
que pueda moverlo* sigue siendo cierta de lo que habla: ninguna LECTURA lo mueve. Lo que lo
mueve no es una lectura, es la ARITMÉTICA de la receta.**

**LOS TRES EJEMPLARES MEDIDOS, los tres con el centro muerto en la vuelta 53 y registrados en
el registro del tramo de [`plan/03_FUSIONES.md`](plan/03_FUSIONES.md).** **Las clases, los
nombres y el estado de cada centro se leyeron del archivo el 20 ago 2026 (vuelta 54) con
corrida propia**, `python scripts/loop/vuelta54_ejemplares_estrella.py`
([`loop/SALIDA_V54_EJEMPLARES_ESTRELLA.txt`](loop/SALIDA_V54_EJEMPLARES_ESTRELLA.txt)), **y no
se copiaron de ningún acta ni de ningún reporte.** La columna de los pares dice la clase que
cada par tenía **al abrir la vuelta 53** (commit `d88c42bb`), que es con la que se leyó:

| acto | el centro, GANADOR POR DERECHO | sus pares `A` al abrir la 53 | qué le pasó |
|---|---|---|---|
| **el pareto** | `analisis_pareto` | **2.546 `A`** (*Sobrevive analisis_pareto*) y **2.551 `A`** (*Sobrevive analisis_pareto*). **No pierde ninguno** | **NO ES VIABLE y MUERE ABSORBIDO** por `analisis_pareto_de_proveedores`. Hoy `deprecado: true` |
| **el poka yoke** | `mistake_proofing_poka_yoke_2` | **2.613 `A`** (*Sobrevive mistake_proofing_poka_yoke_2*) y **2.737 `A`**, que no nombra superviviente. **No pierde ninguno** | **NO ES VIABLE y MUERE ABSORBIDO** por `error_proofing_servicio`. Hoy `deprecado: true` |
| **el dmaic select** | `proceso_nominacion_seleccion` | **2.627 `A`** (*Sobrevive proceso_nominacion_seleccion, el mas completo*) y **2.742 `A`**, que no nombra superviviente. **No pierde ninguno** | **NO ES VIABLE y MUERE ABSORBIDO** por `criterios_seleccion_proyectos_calidad`. Hoy `deprecado: true` |

**LO QUE ESTA PRECISIÓN NO CAMBIA, dicho para que nadie lo lea de más:** el 9.3.1 sigue
entero para lo suyo, **la prueba de contar solo los pares `A` sigue siendo la buena**, y un
ganador por derecho que **no** es centro de estrella sigue teniendo **el superviviente
fijado**. **Lo único que esta nota añade es la frontera: si el acto no se funde entero porque
hay mixto fuera, la especie del 9.3.1 no decide quién sobrevive.**

---

### 9.3 Una dirección de fusión decidida sobre un par no sobrevive a su familia"""

# ==========================================================================
# 1.2 LAS DOS AMPLIACIONES DEL CARRIL, adosadas al registro 1.4.b de la
# vuelta 53 en 03_FUSIONES.md. El ancla es el cierre de la figura del 243.
# ==========================================================================
ANCLA_FUS = """**El carril general dice que eso no fue una excepcion sino la regla: la LECTURA decide, no la
direccion del arrastre.**
"""

AMPLIACIONES = ANCLA_FUS + """
**LAS DOS AMPLIACIONES DEL CARRIL, ADJUDICADAS Y REGISTRADAS EL 20 ago 2026** (vuelta 54,
TAREA 1.2 del encargo; acta de la vuelta 53, preguntas 5 y 6). **Se adosan aqui, al carril que
amplian, y NO reescriben la tabla de arriba: la tabla se queda entera.**

| la forma que la tabla de arriba no cubria | que se hace | la figura |
|---|---|---|
| **CONDICION DE CONTEO O DE COBERTURA en un veredicto del filo** (el veredicto no afirma un texto: afirma una CUENTA, o pide contar antes de decidir) | **SE DESCARGA POR MEDICION ANTES DE FUNDIR**, con el instrumento y su salida CITADOS en la correccion. **Es carril de TEXTO EN SENTIDO AMPLIO**: la casilla de texto cubre TODA afirmacion verificable del veredicto, se lea en el nodo o se mida en el grafo, porque **la medicion es la lectura del grafo**. **POLITICA sigue siendo lo que pide decision de mesa, y sigue DECLARANDO el acto** | **EL `811` DE LA VUELTA 53**: su razon pedia contar la familia Coleman antes de decidir (*ya lleva cuatro nodos vistos y los pares se contradicen*). **La cuenta se corrio ANTES de fundir y dio COBERTURA 6 DE 6, CERO pares pendientes**, y contada no habia contradiccion |
| **CUANDO MOVER UN SOLO VEREDICTO DEJA LA COLISION VIVA** | **LA RELECTURA MUEVE LOS DOS**, y **lo dice en LAS DOS correcciones con la razon vieja entera**. **La vara del carril es su proposito escrito: el censo de colisiones en CERO** (`P.16` y la guarda), **no la letra del singular**. El *CUAL se mueve* de la tabla de arriba presupone que mover uno basta; cuando no basta, **la relectura, que es el mismo organo, decide QUE se mueve, uno o los dos** | **EL PAR `811` CONTRA `1222` DE LA VUELTA 53**: los dos veredictos caian sobre el MISMO par resuelto, uno `B` DIRECTO y la otra `A` arrastrada. **Dejar uno en `B` y el otro en `D` deja la colision viva**, porque `B` contra `D` sigue siendo colision de clase. **Se movieron los dos** |

**LAS DOS SON AMPLIACION Y NO EXCEPCION**, y se dice con la vara de cada una: la primera
porque **la casilla de TEXTO ya cubria toda afirmacion verificable** y lo unico que faltaba era
decirlo con esas palabras; la segunda porque **el proposito del carril es el censo en CERO**, y
un carril que dejara la colision viva no cumpliria el suyo. **NINGUNA CREA DOCTRINA NUEVA**
(acta de la vuelta 53, seccion 5, preguntas 5 y 6).
"""

# ==========================================================================
# 1.3 LOS DOS ROTULOS DEL CENSO DE DUPLICADAS DEL INSTRUMENTO DE FUNDIR.
# Van con el texto viejo DELANTE en comentario, que es como la casa trata una
# correccion sobre un instrumento. LA LOGICA NO SE TOCA.
# ==========================================================================
VIEJO_FUNDIR = '''    print("  duplicadas tras resolver ANTES del tramo (pasivo historico, OP-S-12): %d"
          % len(dup0))
    print("  duplicadas tras resolver DESPUES del tramo                          : %d"
          % len(dup1))
'''

NUEVO_FUNDIR = '''    # CORRECCION DE ROTULO DECLARADA, 20 ago 2026 (vuelta 54, TAREA 1.3 del
    # encargo; acta de la vuelta 53, seccion 3, punto 1). EL TEXTO VIEJO VA
    # DELANTE ENTERO, porque una correccion que tapa lo que corrige no se
    # puede auditar. Los dos rotulos decian:
    #
    #     print("  duplicadas tras resolver ANTES del tramo (pasivo historico, OP-S-12): %d"
    #           % len(dup0))
    #     print("  duplicadas tras resolver DESPUES del tramo                          : %d"
    #           % len(dup1))
    #
    # Y ESE ROTULO INVITA A LEER SU CIFRA COMO LA DE OP-S-12, QUE ES OTRA. El
    # censo de aqui y el de scripts/plan/aristas_duplicadas_tras_resolver.py
    # (el instrumento publicado de OP-S-12) NO CUENTAN LO MISMO:
    #
    #   - el de aqui resuelve alias SOLO de nodos VIVOS y EXCLUYE el destino
    #     igual al propio nodo;
    #   - el de OP-S-12 resuelve alias de TODOS los nodos y CUENTA el self.
    #
    # Por eso este midio 999 donde la cifra publicada de la vuelta 52 era
    # 1.000, con la UNICA diferencia en el grupo (conciencia_calidad,
    # nodos_siguientes, accion_correctiva_sistematica), que solo aparece
    # resolviendo un alias de un nodo DEPRECADO. Medido por el auditor en el
    # commit d88c42bb (acta de la vuelta 53, seccion 3, punto 1). NINGUNA
    # CIFRA PUBLICADA ESTABA MAL Y NINGUNA SE TOCA.
    #
    # LA LOGICA NO SE CAMBIA, y se dice: lo que este censo mide es lo que la
    # guarda necesita (las duplicadas NUEVAS que el propio tramo fabrica), y
    # para eso los alias de nodos deprecados no cuentan. Lo que cambia es el
    # ROTULO, para que su cifra no se lea como la de OP-S-12.
    print("  duplicadas tras resolver ANTES del tramo (pasivo historico, OP-S-12): %d"
          "   [CENSO PROPIO DE LA GUARDA; LA CIFRA DE OP-S-12 LA PUBLICA"
          " aristas_duplicadas_tras_resolver.py]"
          % len(dup0))
    print("  duplicadas tras resolver DESPUES del tramo                          : %d"
          "   [CENSO PROPIO DE LA GUARDA; LA CIFRA DE OP-S-12 LA PUBLICA"
          " aristas_duplicadas_tras_resolver.py]"
          % len(dup1))
'''

# ==========================================================================
# 1.4 LA NOTA DE LOS 41 ENLACES. Se ADOSA AL FINAL del fichero, que es donde
# termina el registro del tramo de la vuelta 53 (es la ultima seccion de la
# pagina, comprobado al escribir esto). No se ancla en una fila de tabla
# porque la ultima fila de un registro de tramo es LITERAL en los cinco
# registros que la pagina lleva y como ancla caeria en rojo.
# ==========================================================================
NOTA_41 = """
### LA NOTA DE LOS 41 ENLACES, ADOSADA AL CIERRE DE ESTA SECCION (20 ago 2026, vuelta 54, TAREA 1.4 del encargo)

**El reporte de la vuelta 53 publico que el grafo GANA 41 enlaces y escribio que la resta exacta
entre las 45 vistas y los 41 no la habia derivado y no la inventaba. El acta de la vuelta 53
(seccion 3, punto 2) la derivo commit a commit. ESTA NOTA NO COPIA ESA DERIVACION: LA VUELVE A
MEDIR**, con `python scripts/loop/vuelta54_41_enlaces.py`
([`../loop/SALIDA_V54_41_ENLACES.txt`](../loop/SALIDA_V54_41_ENLACES.txt)), corrido el 20 ago
2026 en la vuelta 54, **porque la regla 2 del `EJECUTOR` dice que un acta previa nunca es fuente
de una cifra nueva: se cita como contraste. Las dos coinciden al digito.**

| commit de la vuelta 53 | enlaces MEDIDOS | delta | vistas de la simetrizacion | instancias retiradas |
|---|---:|---:|---:|---:|
| `d88c42bb`, cierre de la vuelta 52 | **17.011** | | | |
| `49ae6eef`, TAREA 1 | **17.011** | **+0** | 0 | 0 |
| `cadc9977`, LOTE A | **17.023** | **+12** | **13** | **1** |
| `04bd56de`, LOTE B | **17.030** | **+7** | **9** | **2** |
| `90bb930c`, LOTE C | **17.052** | **+22** | **23** | **1** |
| `be5d152b`, el cierre | **17.052** | **+0** | 0 | 0 |
| **la vuelta entera** | | **+41** | **45** | **4** |

**LOS TRES LOTES CALZAN UNO A UNO** (vistas menos retiros igual al delta medido: 13 menos 1 son
12; 9 menos 2 son 7; 23 menos 1 son 22), **y eso es mas fino que la resta global**: no solo 45
menos 4 son 41, sino que **cada lote cuadra por separado**. Las vistas se leen del
`symmetrize_added` horneado en `dataset/metadata/phase1_run_log.json` de cada commit; los
enlaces, con la vara de `vuelta31_estado.py` (nodos previos mas nodos siguientes sobre los 3.853
ficheros, deprecados incluidos).

**LAS CUATRO INSTANCIAS RETIRADAS, NOMBRADAS Y VERIFICADAS UNA A UNA** (el id absorbido estaba
en el campo ANTES del lote y ya no esta DESPUES):

| lote | el campo | el id absorbido que desaparece | especie | por que se retira |
|---|---|---|---|---|
| **A** | `warrant_pricing_venture_debt.nodos_previos` | `warrants_deuda_convertible` | **AUTO-ARISTA** | el absorbido redirige AL PROPIO NODO, y una arista a si mismo no se escribe |
| **C** | `criterios_seleccion_proyectos_calidad.nodos_previos` | `proceso_nominacion_seleccion` | **AUTO-ARISTA** | igual: el absorbido redirige al propio nodo |
| **B** | `elaboracion_fdd.nodos_previos` | `contratar_abogado_especializado_franquicias` | **COLAPSO DE DUPLICADA** | el superviviente `eleccion_abogado_franquicias` **YA ESTABA en el campo**, verificado, y las dos instancias colapsan en una |
| **B** | `sistema_estable_causas_comunes.nodos_siguientes` | `critica_gestion_por_objetivos` | **COLAPSO DE DUPLICADA** | el superviviente `eliminar_metas_numericas_gerencia` **YA ESTABA en el campo**, verificado |

**45 MENOS 4 SON 41, medido commit a commit y lote a lote.** **La frase del reporte de la vuelta
53 (*`P.16` retiro por su lado duplicadas y dos auto-aristas*) queda CONFIRMADA y ahora con los
cuatro nombres.**
"""

# ==========================================================================
# 1.3.b EL MISMO ROTULO EN EL INSTRUMENTO QUE DE VERDAD SE CORRE, Y ES
# ALCANCE MIO SOBRE EL ENCARGO: SE DECLARA EN VEZ DE HACERSE CALLADO.
#
# El encargo nombra "scripts/loop/vuelta48_fundir_tramo.py, los dos print de
# duplicadas tras resolver, hoy lineas 418 a 421", y la referencia es EXACTA:
# medido hoy con git, ese print vivia en la linea 418 del fichero del commit
# anterior. Pero el instrumento que EJECUTA los tramos desde la vuelta 49 es
# su SUCESOR DECLARADO, scripts/loop/vuelta49_fundir_tramo.py (el que anade el
# destino INCISO), y lleva LOS MISMOS DOS ROTULOS, palabra por palabra, en sus
# lineas 478 a 481. La vuelta 53 corrio ESE, comprobado en su salida: solo el
# de la 49 imprime "INCISOS ADOSADOS", y las tres salidas de sus lotes lo
# imprimen.
#
# Reparar solo el ancestro dejaria el sintoma vivo justo en el instrumento que
# publica la cifra en cada tramo. Se adosa la MISMA frase, con el MISMO texto
# viejo delante, y va MARCADO COMO DISCUTIBLE en el reporte, porque anadir un
# fichero que el encargo no nombra es alcance mio y no suyo.
# ==========================================================================
FUN49 = os.path.join(RAIZ, "scripts", "loop", "vuelta49_fundir_tramo.py")

NUEVO_FUNDIR_49 = NUEVO_FUNDIR.replace("(vuelta 54, TAREA 1.3 del",
                                       "(vuelta 54, TAREA 1.3.b del")

CAMBIOS = [
    (BAN, "1.1 la precision de la estrella, al final del 9.3.1", ANCLA_BAN, NOTA_ESTRELLA),
    (FUS, "1.2 las dos ampliaciones del carril", ANCLA_FUS, AMPLIACIONES),
    (FUN, "1.3 los dos rotulos del censo de duplicadas", VIEJO_FUNDIR, NUEVO_FUNDIR),
    (FUN49, "1.3.b los mismos dos rotulos en el sucesor", VIEJO_FUNDIR, NUEVO_FUNDIR_49),
]

COLA = [
    (FUS, "1.4 la nota de los 41 enlaces", NOTA_41),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("LOS CUATRO REGISTROS DE LA TAREA 1 DE LA VUELTA 54")
    print("modo: %s" % ("SIMULACION, no escribe" if a.simular else "ESCRITURA"))
    print("=" * 78)
    print()

    textos = {}
    hechas = saltadas = 0
    for ruta, etiqueta, viejo, nuevo in CAMBIOS:
        if ruta not in textos:
            textos[ruta] = io.open(ruta, encoding="utf-8").read()
        t = textos[ruta]
        if nuevo in t:
            print("  YA ESTABA   %-52s (idempotente)" % etiqueta)
            saltadas += 1
            continue
        c = t.count(viejo)
        if c != 1:
            print("  ROJO        %-52s el texto viejo aparece %d veces" % (etiqueta, c))
            return 1
        textos[ruta] = t.replace(viejo, nuevo, 1)
        print("  HECHA       %-52s %s" % (etiqueta, os.path.basename(ruta)))
        hechas += 1

    for ruta, etiqueta, bloque in COLA:
        if ruta not in textos:
            textos[ruta] = io.open(ruta, encoding="utf-8").read()
        t = textos[ruta]
        if bloque in t:
            print("  YA ESTABA   %-52s (idempotente)" % etiqueta)
            saltadas += 1
            continue
        textos[ruta] = t.rstrip(chr(10)) + chr(10) + bloque
        print("  ADOSADA     %-52s %s (al final)" % (etiqueta, os.path.basename(ruta)))
        hechas += 1

    if not a.simular:
        for ruta, t in textos.items():
            io.open(ruta, "w", encoding="utf-8", newline=chr(10)).write(t)

    print()
    print("  sustituciones HECHAS: %d | ya estaban: %d" % (hechas, saltadas))
    print("  ficheros: %s" % ", ".join(sorted(os.path.basename(r) for r in textos)))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
