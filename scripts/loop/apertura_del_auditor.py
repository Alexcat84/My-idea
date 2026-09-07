# -*- coding: utf-8 -*-
r"""apertura_del_auditor.py . EL BLOQUE DE APERTURA DEL AUDITOR, GEMELO DEL DEL
EJECUTOR: CORRE `aislador_de_ciega.py` Y SELLA SU SALIDA ANTES DE QUE EL TURNO
PUEDA TOCAR `git log`, `git status` O `REPORTE.md`.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como `aislador_de_ciega.py`,
`tallar_cabecera_reporte.py`, `archivar_reporte.py`, `serie_de_registros.py` y
`cerrar_reporte.py`: se usa en TODA vuelta y NO SE CLONA. Un fichero que se clona
por vuelta es un fichero que la vuelta siguiente puede olvidar, y olvidarse es
justamente la enfermedad que esto viene a curar.

DE DONDE SALE, PALABRA POR PALABRA. Decision del fundador del 5 sep 2026,
PREGUNTA 3, opcion `c`, en
`docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md`: *"la apertura del
auditor pasa a CODIGO (fichero gemelo del bloque de apertura del ejecutor: corre
`aislador_de_ciega.py` y SELLA su salida antes de que el turno pueda tocar `git
log`, `git status` o `REPORTE.md`) y ademas ROMPER UN REMEDIO ESCRITO ACUMULA"*.
**Esta es la mitad que quita el problema de raiz; la otra mitad ya esta escrita en
`AUDITOR.md`.** Y en `AUDITOR.md`, seccion 1, la misma decision esta recogida:
*"con eso, aislar el sujeto deja de depender de que alguien se acuerde"*.

POR QUE HACE FALTA, Y NO ES UNA SOSPECHA: **CUATRO ACTAS SEGUIDAS** con la misma
caida propia `C.1` (178, 179, 180 y 181), y **la de la 181 es la primera en que el
remedio escrito ya existia y aun asi no se cumplio**. El acta 180 le dejo escrito
al auditor de la 181, en su linea 62490, que su PRIMER comando fuera el aislador y
que *"hasta que esos dos ficheros existan no se corre `git log`, ni `git status`,
ni se abre `REPORTE.md`"*. El acta 181 lo declara asi, en su seccion 2: *"Rompi las
tres"*.

COMO LO IMPIDE, Y ES LO UNICO QUE HACE:

  1. LLEVA UNA BITACORA DE TOQUES. Las tres cosas prohibidas **solo se pueden
     hacer llamando a las funciones de aqui** (`git_log`, `git_status`,
     `leer_reporte`), y cada una **apunta su toque antes de hacerlo**.
  2. `sellar()` **CAE EN ROJO si la bitacora ya trae alguno de los tres**, y NO
     escribe el sello. No avisa ni recomienda: no sella.
  3. El sello es un fichero con el criterio, la ruta de la ciega, la del destape,
     sus bytes y sus `sha256`. **Existe o no existe**, y quien lo lea sabe si el
     sujeto se aislo antes o despues.

LO QUE NO HACE, Y SE DICE PARA QUE NADIE LE PIDA MAS: **no puede impedir que
alguien corra `git status` en su terminal por su cuenta.** Ninguna guarda de este
repo puede. Lo que si hace es que **el sello, que es lo que el acta cita como
prueba, no se pueda escribir despues**; y el auditor que quiera saltarse esto
tiene que hacerlo **a sabiendas y sin sello**, que es exactamente la diferencia
entre un descuido y una decision.

--- LA FRASE DE ARRIBA ERA FALSA HASTA LA VUELTA 193, Y LO DIGO ANTES DE
    ARREGLARLA (hallazgo `5.1` del acta 193, levantado por el auditor CONTRA EL
    FICHERO QUE LE PROTEGE) --------------------------------------------------

**"EL SELLO NO SE PUEDA ESCRIBIR DESPUES" NO SE CUMPLIA FUERA DE UN MISMO
PROCESO, Y ESTA PROBADO, NO SUPUESTO.** `_BITACORA` y `_SELLADO` eran estado de
MODULO y morian con el proceso. El auditor sella con el CLI, o sea en un proceso
que termina; **en el proceso siguiente la bitacora nacia vacia**, y un turno que
ya habia tocado `REPORTE.md` **volvia a sellar como si nada**, con `sellar()`
SOBRESCRIBIENDO el sello y publicando `prohibidos tocados antes del sello: 0`. La
prueba entera esta en `docs/loop/_auditor_v193_cuarta_puerta_prueba.txt`, y la
corrio el auditor contra si mismo.

**Y LA CUARTA PUERTA NO LA PODIA USAR NADIE QUE SELLARA POR CLI, O SEA NADIE:**
`puede_declarar_clases()` respondia `NO: este turno no ha sellado` **aunque el
sello estuviera en disco**, y el CLI no exponia ninguna bandera para declarar
clases.

**LO QUE LA VUELTA 193 ARREGLA, Y COMO:**

  a. **LA BITACORA Y EL SELLO SOBREVIVEN AL PROCESO**, en el fichero del turno
     `docs/loop/_TURNO_DEL_AUDITOR.json`, que se carga al importar el modulo y se
     reescribe en cada toque. **Los toques apuntados en una corrida los ve la
     siguiente.**
  b. **`sellar()` CAE EN ROJO SI YA HAY SELLO EN DISCO PARA ESA VUELTA**, en vez
     de sobrescribirlo. **Un sello no se reescribe**, y hasta hoy eso solo se
     cumplia dentro de un mismo proceso.
  c. **EL CLI PUEDE DECLARAR LAS CLASES**, con `--declarar-clases RUTA`, leyendo
     el sello de disco. Sin eso la cuarta puerta era inusable.

**Y LO QUE SIGUE SIN PODERSE, DICHO EN VEZ DE PROMETIDO:**

  . **El fichero del turno se puede borrar a mano.** Quien lo borre empieza con la
    bitacora limpia. **No hay forma de impedirlo desde dentro del repo**, igual
    que no la hay de impedir un `git status` en otra terminal. Lo que si hay es
    que **borrarlo es un acto**, y el sello en disco sigue estando: la guarda `b`
    muerde igual, porque mira el DISCO y no la memoria.
  . **El fichero del turno no sabe de que vuelta es hasta que se sella.** Los
    toques anteriores al sello se apuntan sin vuelta, que es lo correcto: son del
    TURNO, y el turno empieza antes de saber su numero.
  . **Sigue sin saber si lo que se leyo era del sujeto** cuando el archivo se abre
    por fuera de estas funciones. Eso no cambia.

--- LA CUARTA PUERTA (vuelta 192, TAREA 4; hallazgo `5.2` del acta 192) --------

POR QUE NACE, Y LO LEVANTA CONTRA SI MISMO EL QUE SE COLO. Las tres puertas de
arriba FUNCIONARON en la vuelta 192: la bitacora del auditor salio vacia y su
sello es verde. **Pero el sujeto de la ciega no vive en ninguno de los tres.**
Vive en las `clase` y las `razon` de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, y por
ahi entro el auditor de la 192 **con el sello ya escrito y sin romper ninguna
guarda**: buscando la leyenda de las clases corrio una consulta sobre el archivo
que le imprimio las razones de los puestos 156 y 201, **que eran de su propia
tanda**. Los saco del cotejo y lo declaro antes de contar, **pero el remedio no
puede ser que el auditor se acuerde: esa es justo la enfermedad que este fichero
vino a curar.**

QUE PROHIBE Y QUE NO, PORQUE LA DIFERENCIA ES TODA LA GUARDA. **NO se prohibe
leer el archivo entero**, que hace falta para recomputar el marcador y el acta lo
publica en todas sus vueltas. **Se prohibe DESTAPAR EL SUJETO**, o sea leer
`clase` o `razon` DE LOS PUESTOS QUE EL SELLO YA ELIGIO, antes de que las clases
del auditor esten escritas. Por eso:

  4. `leer_veredictos()` **APUNTA SU TOQUE** y, por defecto, **devuelve las filas
     de los puestos sellados con `clase` y `razon` TAPADAS**. Quien quiera verlas
     tiene que pedirlo con `destapar_sujeto=True`, y entonces el toque que apunta
     es otro: `veredictos:destape`. **Un destape no se puede hacer sin querer.**
     `marcador()` cuenta por clase sobre el archivo ENTERO y **no destapa nada**,
     porque un agregado de miles de filas no dice la clase de ninguna.
  5. `declarar_clases_escritas()` **CAE EN ROJO** si la bitacora trae un
     `veredictos:destape` **anterior**. Es el gemelo de `sellar()`: alli el rojo
     era no poder sellar; aqui es **no poder declarar las clases escritas**, que
     es lo que un acta cita como prueba de que leyo a ciegas.

LO QUE ESTA CUARTA PUERTA NO PUEDE HACER, DICHO IGUAL QUE LAS OTRAS TRES: **no
puede impedir que alguien abra el `jsonl` por su cuenta en su terminal**, ni con
`python`, ni con `grep`, ni con un editor. Ninguna guarda de este repo puede.
**Lo que si puede es que la declaracion de clases no se pueda escribir despues**,
y que **quien se la salte lo haga a sabiendas**. Y hay una segunda cosa que no
puede y que se dice porque es mas fina: **no sabe si lo que se leyo era del
sujeto** cuando el archivo se abre por fuera de estas funciones. Solo vigila lo
que pasa por aqui, y por eso el turno que quiera poder citar su ciega tiene que
pasar por aqui.

EL ORDEN OBLIGATORIO DE UN TURNO DE AUDITOR:

    from apertura_del_auditor import sellar, git_log, git_status, leer_reporte
    sellar(criterio="...", muestra=30, semilla=182)   # PRIMERO, y solo esto
    ...                                               # ya se puede verificar
    git_status()                                      # apunta su toque

USO:
  python scripts/loop/apertura_del_auditor.py --criterio "..." --muestra 30 \
      --semilla 182 --vuelta 182
  python scripts/loop/apertura_del_auditor.py --estado
"""
import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

# LAS TRES COSAS QUE EL REMEDIO PROHIBE ANTES DEL SELLO. Van como constante y con
# nombre para que el arnes las pueda recorrer una a una en vez de que el caso
# rojo elija cual probar.
PROHIBIDOS_ANTES_DEL_SELLO = ("git log", "git status", "REPORTE.md")

# LA CUARTA PUERTA (vuelta 192). Va SEPARADA de las tres de arriba a proposito:
# aquellas se prohiben ANTES DEL SELLO y esta se prohibe ANTES DE LAS CLASES, que
# es un momento distinto del turno. Meterlas en la misma tupla habria roto el
# arnes de la vuelta 182, que recorre esa tupla una a una, y habria mezclado dos
# reglas que muerden en sitios distintos.
ARCHIVO_DE_VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
CAMPOS_QUE_DESTAPAN = ("clase", "razon")
TOQUE_VEREDICTOS = "veredictos"
TOQUE_DESTAPE = "veredictos:destape"
TAPADO = "(TAPADO POR LA CUARTA PUERTA)"

# LA BITACORA. Es del modulo a proposito: el estado tiene que sobrevivir entre
# llamadas dentro del mismo turno, que es lo que se esta vigilando.
#
# Y DESDE LA VUELTA 193 SOBREVIVE TAMBIEN AL PROCESO (TAREA 4.a; hallazgo 5.1 del
# acta 193). Estado de modulo solo es estado de proceso, y el auditor sella con el
# CLI: cada corrida nacia con la bitacora vacia. Ahora se persiste en el FICHERO
# DEL TURNO, se carga al importar y se reescribe en cada toque.
_BITACORA = []
_SELLADO = {"hecho": False, "ruta": None, "vuelta": None}
_CLASES = {"escritas": False, "ruta": None}

# EL CIERRE DEL TURNO (vuelta 197, TAREA 2.b; hallazgo `5.4` del acta 197).
#
# EL AGUJERO, MEDIDO Y NO NARRADO: el fichero del turno SOBREVIVIA AL TURNO. El
# auditor de la 197 llego con la bitacora del turno ANTERIOR puesta (`git log`,
# `git status`, `REPORTE.md` y dos destapes), `sellar()` cayo en rojo por esos
# toques ajenos, y tuvo que correr `--olvidar-turno` PARA PODER SELLAR. **Una
# guarda que obliga a borrar la bitacora en cada vuelta ensena a borrar la
# bitacora**, que es lo contrario de lo que la guarda quiere.
#
# EL REMEDIO, Y LO QUE NO HACE: el turno se CIERRA al declarar las clases. Cerrar
# NO es borrar: el fichero se queda, con su bitacora dentro y con un registro
# `cerrados` por vuelta, y lo unico que cambia es que **un turno nuevo lo carga
# como CERRADO y empieza limpio sin tener que borrar nada**.
#
# LO QUE NO SE AFLOJA, Y VA PRIMERO PARA QUE SE VEA:
#   . EL SELLO EN DISCO NO SE TOCA. `sello_en_disco()` y la guarda `b` de
#     `sellar()` siguen mirando el disco exactamente igual.
#   . NO SE PUEDEN DECLARAR CLASES DOS VECES. Antes lo impedia `_CLASES` cargado
#     del fichero; ahora, ademas, `_CERRADOS` guarda QUE VUELTA cerro, y
#     `puede_declarar_clases_con_sello()` cae sobre una vuelta ya cerrada. La
#     guarda no se pierde al limpiar: cambia de sitio y se hace explicita.
_CERRADOS = {}
_VIVO = {"abierto": True}

# EL FICHERO DEL TURNO. Va en una variable de modulo, y no clavado dentro de las
# funciones, PARA QUE LOS ARNESES LO PUEDAN REDIRIGIR A UN TEMPORAL: un arnes que
# escribiera en la sede de verdad ensuciaria el turno del auditor.
RUTA_DEL_TURNO = os.path.join(LOOP, "_TURNO_DEL_AUDITOR.json")


def _guardar_turno():
    """ESCRIBE EL ESTADO DEL TURNO EN SU FICHERO. No levanta: si no se puede
    escribir, el turno sigue funcionando en memoria y la guarda del disco (la
    `b`) sigue mordiendo, porque esa mira los SELLOS y no este fichero."""
    try:
        io.open(RUTA_DEL_TURNO, "w", encoding="utf-8", newline=NL).write(
            json.dumps({"bitacora": list(_BITACORA),
                        "sellado": dict(_SELLADO),
                        "clases": dict(_CLASES),
                        "cerrados": dict(_CERRADOS),
                        "vivo": dict(_VIVO)},
                       ensure_ascii=False, indent=1) + NL)
    except Exception:                                    # noqa: BLE001
        pass


def _reiniciar_memoria():
    """DEJA EL ESTADO DE MODULO COMO RECIEN IMPORTADO, SIN TOCAR NINGUN FICHERO.

    ES LA MITAD DE `olvidar_todo()` QUE NO BORRA NADA, y va separada porque las
    dos mitades tienen dueno distinto: el olvido entero es un ACTO del arnes
    (vacia la memoria Y borra el fichero), y esto es solo la memoria."""
    del _BITACORA[:]
    _SELLADO.update({"hecho": False, "ruta": None, "vuelta": None})
    _CLASES.update({"escritas": False, "ruta": None})


def _cargar_turno():
    """CARGA EL ESTADO DEL TURNO DE SU FICHERO. Devuelve True si cargo algo.
    **Se llama al importar el modulo**, que es lo que hace que los toques de una
    corrida los vea la siguiente.

    ARREGLADA EN LA VUELTA 194, TAREA 2, Y LA CAUSA ESTA MEDIDA. Antes, cuando el
    fichero NO existia, esta funcion se iba dejando la memoria como estuviera. Eso
    la convertia en un MEZCLADOR y no en un cargador, y rompia lo unico para lo
    que `RUTA_DEL_TURNO` es de modulo: **un arnes que redirige la ruta a un
    temporal y vuelve a cargar seguia viendo el turno de la SEDE DE VERDAD**,
    porque el modulo ya lo habia cargado al importar y el temporal todavia no
    existia. Medido con el arnes de la 193 corrido con el turno puesto: sus
    procesos hijos entraban con `['x']` en la bitacora en vez de vacios, y sus
    casos `A`, `B` y `E` salian en rojo por una razon que no era la suya.

    LA VARA, ESCRITA ENTERA PORQUE TIENE DOS LADOS:
      . **el fichero NO existe** -> el disco dice QUE NO HAY TURNO, y la memoria
        se reinicia para decir lo mismo. Devuelve False, que sigue siendo
        "no cargue nada";
      . **el fichero existe pero NO se puede leer** -> eso NO es "no hay turno":
        es un fichero roto, y **la memoria NO se toca**, porque tirar el estado
        vivo por un JSON corrupto seria perder la prueba en silencio."""
    if not os.path.exists(RUTA_DEL_TURNO):
        _reiniciar_memoria()
        _CERRADOS.clear()
        _VIVO["abierto"] = True
        return False
    try:
        d = json.load(io.open(RUTA_DEL_TURNO, encoding="utf-8"))
    except Exception:                                    # noqa: BLE001
        return False
    # LOS CERRADOS SE CARGAN SIEMPRE: son hechos historicos del fichero y NO
    # dependen de que el turno vivo siga abierto. Son los que impiden que una
    # vuelta ya cerrada vuelva a declarar clases.
    _CERRADOS.clear()
    _CERRADOS.update(d.get("cerrados") or {})
    vivo = d.get("vivo") or {}
    _VIVO["abierto"] = bool(vivo.get("abierto", True))
    if not _VIVO["abierto"]:
        # EL TURNO ANTERIOR SE CERRO: el turno nuevo empieza LIMPIO, y el fichero
        # NO se borra. Esto es el hallazgo `5.4` del acta 197 resuelto sin ensenar
        # a nadie a borrar su propia bitacora.
        _reiniciar_memoria()
        # Y AQUI VA LA MITAD `1.a` DEL ENCARGO DE LA VUELTA 199, QUE ES EL
        # REMEDIO DEL PUNTO `C` DE LA PARADA DE LA 198. **LA MARCA DE CERRADO SE
        # CONSUME AL CARGARLA**: el fichero decia `vivo.abierto: false` PARA
        # SIEMPRE, asi que **cada proceso nuevo volvia a reiniciar la memoria y
        # tiraba lo que el anterior habia apuntado**. Con eso se apagaban DOS
        # remedios escritos: el de la 193 (que la bitacora sobreviva al proceso,
        # que es lo unico que deja a `sellar()` caer en rojo si el turno ya toco
        # `git log`) y el de la 197 (que `leer_reporte()` caiga con el sujeto
        # sellado y las clases sin escribir).
        #
        # LO QUE NO SE AFLOJA, Y VA PRIMERO: **la memoria SIGUE reiniciandose**,
        # o sea el turno nuevo SIGUE empezando limpio, que es el remedio entero
        # de la 197. Lo unico que cambia es que **el turno nuevo queda VIVO** en
        # vez de nacer muerto, y por eso lo que ESTE turno apunte a partir de
        # aqui si llega al proceso siguiente. El disco no se toca en esta linea:
        # se reescribe cuando el turno nuevo escriba algo, que es `_guardar_turno()`.
        #
        # POR QUE AQUI Y NO SOLO EN `sellar()`: la guarda de la 193 tiene que
        # morder sobre toques hechos **ANTES** del sello. Reabrir solo al sellar
        # dejaria esos toques sin acumular entre procesos, que es justo el hueco.
        # `sellar()` lo pone tambien, por si alguien carga y sella sin pasar por
        # esta rama.
        _VIVO["abierto"] = True
        return False
    del _BITACORA[:]
    _BITACORA.extend(d.get("bitacora") or [])
    _SELLADO.update(d.get("sellado") or {})
    _CLASES.update(d.get("clases") or {})
    return True


def sello_en_disco(vuelta, base=None):
    """LA RUTA DEL SELLO DE UNA VUELTA SI YA EXISTE EN DISCO, o cadena vacia.

    **ES LA GUARDA `b` DE LA TAREA 4 DE LA VUELTA 193, Y MIRA EL DISCO Y NO LA
    MEMORIA**: `_SELLADO` moria con el proceso, asi que un turno en un proceso
    nuevo reescribia el sello publicando `prohibidos antes del sello: 0`. Un
    sello no se reescribe, y ahora eso vale entre procesos y no solo dentro de
    uno."""
    ruta = os.path.join(base or LOOP, "SELLO_APERTURA_AUDITOR_V%s.json" % vuelta)
    return ruta if os.path.exists(ruta) else ""


def sello_mas_reciente_en_disco(base=None):
    """(RUTA, VUELTA) DEL SELLO DE VUELTA MAS ALTA QUE HAY EN DISCO, o ("", "").

    **ES LA MITAD `1.b` DEL ENCARGO DE LA VUELTA 199**, y nace de una caida
    medida: `puede_leer_reporte()` solo consultaba `sello_en_disco()` **si se le
    pasaba `vuelta`**, y el orden que `AUDITOR.md` escribe es `leer_reporte()` A
    SECAS. Con la memoria reiniciada y sin `vuelta`, la guarda concluia *"este
    turno NO ha sellado"* **con el sello de esa vuelta en el disco, a su lado**.
    El auditor de la 198 lo sufrio siguiendo el orden escrito.

    LA VARA ES LA VUELTA MAS ALTA, y va escrita porque es lo unico que se puede
    sostener sin adivinar: el turno vivo es siempre el del sello mas nuevo, y los
    sellos viejos ya tienen su constancia de cierre en `_CERRADOS`. Los nombres
    que no traen un numero entero detras de la `V` se ordenan por texto y siempre
    por debajo de los numericos, para que un `SELLO_APERTURA_AUDITOR_VARNES.json`
    de un arnes no se cuele como el mas reciente.

    Semi-pura: lo unico que toca disco es leer el directorio."""
    carpeta = base or LOOP
    mejor = (None, "", "")
    try:
        nombres = os.listdir(carpeta)
    except Exception:                                    # noqa: BLE001
        return "", ""
    for nombre in nombres:
        m = re.match(r"^SELLO_APERTURA_AUDITOR_V(.+)\.json$", nombre)
        if not m:
            continue
        v = m.group(1)
        n = int(v) if v.isdigit() else -1
        if mejor[0] is None or (n, v) > (mejor[0], mejor[1]):
            mejor = (n, v, os.path.join(carpeta, nombre))
    return (mejor[2], mejor[1]) if mejor[0] is not None else ("", "")


def bitacora():
    """LOS TOQUES APUNTADOS HASTA AHORA, en orden. Copia, no el original."""
    return list(_BITACORA)


def apuntar(que):
    """APUNTA UN TOQUE. Se llama ANTES de hacer la cosa, no despues: si la cosa
    revienta, el toque igual paso."""
    _BITACORA.append(que)
    _guardar_turno()
    return que


def toques_prohibidos():
    """LOS TOQUES DE LA BITACORA QUE ESTAN EN LA LISTA PROHIBIDA. PURA sobre el
    estado del modulo, y es la funcion que `sellar()` consulta."""
    return [t for t in _BITACORA if t in PROHIBIDOS_ANTES_DEL_SELLO]


def olvidar_todo():
    """VACIA LA BITACORA Y EL SELLO. **Solo para los arneses**, que necesitan
    correr varios escenarios en el mismo proceso. Un turno de auditor no la llama
    nunca, y si la llamara estaria borrando su propia prueba a mano, que es una
    decision y no un descuido."""
    del _BITACORA[:]
    _SELLADO["hecho"] = False
    _SELLADO["ruta"] = None
    _SELLADO["vuelta"] = None
    _CLASES["escritas"] = False
    _CLASES["ruta"] = None
    _CERRADOS.clear()
    _VIVO["abierto"] = True
    # Y BORRA EL FICHERO DEL TURNO, porque si no lo borrara el olvido seria a
    # medias: la memoria limpia y el disco sucio.
    try:
        if os.path.exists(RUTA_DEL_TURNO):
            os.remove(RUTA_DEL_TURNO)
    except Exception:                                    # noqa: BLE001
        pass


def git_log(*args):
    """`git log`, Y APUNTA SU TOQUE."""
    apuntar("git log")
    return _git(["log"] + list(args))


def git_status(*args):
    """`git status`, Y APUNTA SU TOQUE."""
    apuntar("git status")
    return _git(["status"] + list(args))


class ReporteFueraDeOrden(RuntimeError):
    """LO QUE `leer_reporte()` LEVANTA CUANDO EL ORDEN NO SE CUMPLE.

    ES UNA EXCEPCION Y NO UN VALOR DE VUELTA A PROPOSITO: la casa manda FALLAR
    RUIDOSO (banco 9). Un `leer_reporte()` que devolviera cadena vacia dejaria al
    turno leyendo un reporte vacio sin enterarse, y esa es la degradacion
    silenciosa que no deja sintoma."""


def puede_leer_reporte(vuelta=None, base=None):
    """(SI_PUEDE, MOTIVO). PURA sobre el estado del modulo y, si se le da
    `vuelta`, sobre la existencia del sello en disco.

    DE DONDE SALE, Y NO ES UNA IDEA MIA: adjudicacion `4.5` del acta 197, que
    contesta la `P.3` del reporte de la 196 **por extension de `AUDITOR.md` 1.2**
    (*"imprime PRIMERO los pasos, adjudica tu clase, y SOLO DESPUES destapa la
    razon escrita"*). **LA TABLA DE DISCREPANCIAS DE UN REPORTE ES UN DESTAPE**, y
    esta MEDIDO: el reporte de la 196 publico la clase de archivo de 8 de los 120
    puestos que el auditor de la 197 acababa de sellar, y ademas el reparto entero
    del archivo sobre esos mismos 120. El auditor lo sufrio SIGUIENDO EL ORDEN
    ESCRITO, no saltandoselo.

    EL ORDEN OBLIGATORIO PASA A SER:
    `sellar()` -> clasificar -> `--declarar-clases` -> `leer_reporte()`.

    LO QUE **NO** SE PROHIBE, Y ES LA MITAD QUE IMPIDE QUE ESTO ESTORBE: **un
    turno SIN SELLO sigue pudiendo leer el reporte**, porque ahi no hay sujeto que
    quemar. Lo unico que se prohibe es leerlo **con el sujeto ya elegido y las
    clases sin escribir**.

    EL SELLO SE MIRA EN LOS DOS SITIOS, Y **SIEMPRE EN DISCO** (vuelta 199,
    mitad `1.b`): en la memoria del turno (`_SELLADO`, que desde la 193 sobrevive
    al proceso por el fichero del turno) y en DISCO, con `vuelta` por
    `sello_en_disco()` y SIN `vuelta` por `sello_mas_reciente_en_disco()`. Con eso
    la guarda no se puede esquivar arrancando un proceso nuevo, que es exactamente
    como se esquivaba la de `sellar()` antes de la vuelta 193.

    **CORRECCION DECLARADA, Y NO SE TAPA LO QUE CORRIGE** (`EJECUTOR.md` 8): esta
    linea decia antes *"y, si se pasa `vuelta`, tambien en DISCO"*, y ESA ERA LA
    PUERTA. `AUDITOR.md` manda llamar a `leer_reporte()` **a secas**, o sea sin
    `vuelta`, y por esa rama la guarda no miraba el disco y **dejaba pasar**. El
    auditor de la 198 lo midio contra si mismo: sello por el CLI, llamo como la
    doctrina manda, y el modulo le entrego el reporte con las tablas de
    discrepancias de su propio sujeto sin un solo rojo
    (`docs/loop/SALIDA_V198_GUARDA_MUERTA.txt`, 10 casos)."""
    hay_sello = bool(_SELLADO["hecho"])
    de_disco = ""
    vuelta_del_disco = ""
    if vuelta is not None:
        de_disco = sello_en_disco(vuelta, base)
        vuelta_del_disco = str(vuelta) if de_disco else ""
    else:
        # LA MITAD `1.b` DEL ENCARGO DE LA VUELTA 199. **SIN `vuelta` TAMBIEN SE
        # MIRA EL DISCO**, y esta rama es la que faltaba: la sede real llama a
        # `leer_reporte()` A SECAS, que es como `AUDITOR.md` lo escribe, y por
        # aqui se escapaba entera la guarda de la 197.
        de_disco, vuelta_del_disco = sello_mas_reciente_en_disco(base)
    hay_sello = hay_sello or bool(de_disco)
    if not hay_sello:
        return True, ("este turno NO ha sellado: no hay sujeto elegido, y por eso "
                      "leer el reporte no puede quemar nada")
    if _CLASES["escritas"]:
        return True, ("el sujeto esta sellado Y las clases ya estan escritas (%s): "
                      "desde aqui el reporte ya no puede quemar nada"
                      % (_CLASES["ruta"] or "sin ruta apuntada"))
    # LA CONSTANCIA DEL CIERRE VALE COMO PRUEBA DE QUE LAS CLASES SE ESCRIBIERON.
    # LO CAZO EL ARNES DE ESTA MISMA TAREA, Y NO LO SUPUSE: al cerrar el turno,
    # `_CLASES` se limpia para el turno siguiente, pero el sello sigue EN DISCO, y
    # sin esto la guarda bloqueaba PARA SIEMPRE la lectura del reporte de una
    # vuelta cuyas clases si se declararon. El registro `cerrados[vuelta]` guarda
    # la ruta de esas clases, y esa es la prueba durable.
    #
    # Y LA CLAVE SE COMPUTA, NO SE EXIGE POR PARAMETRO (vuelta 199, mitad `1.b`):
    # con `vuelta` manda `vuelta`; SIN `vuelta` manda la del sello que se acaba de
    # encontrar en disco, y si tampoco la hay, la que el turno tenga en memoria.
    # Sin esto, la rama nueva del disco bloquearia PARA SIEMPRE la lectura del
    # reporte de una vuelta cuyas clases si se declararon, que es exactamente la
    # caida que este mismo bloque vino a evitar cuando se escribio.
    clave = (str(vuelta) if vuelta is not None
             else (vuelta_del_disco or _SELLADO["vuelta"] or ""))
    if clave and clave in _CERRADOS:
        reg = _CERRADOS[clave] or {}
        if reg.get("ruta_clases"):
            return True, ("el turno de la vuelta %s se CERRO con sus clases "
                          "declaradas (%s): la constancia del cierre es la prueba, "
                          "y el reporte ya no puede quemar nada"
                          % (clave, reg.get("ruta_clases")))
    return False, ("este turno TIENE SELLO%s y NO ha declarado sus clases. La "
                   "tabla de discrepancias de un reporte ES UN DESTAPE "
                   "(adjudicacion 4.5 del acta 197, por extension de AUDITOR.md "
                   "1.2), y leerlo ahora QUEMA EL SUJETO. El orden es "
                   "sellar() -> clasificar -> --declarar-clases -> leer_reporte()."
                   % (" en disco (%s)" % os.path.relpath(de_disco, RAIZ).replace(
                       os.sep, "/") if de_disco else ""))


def leer_reporte(ruta=None, vuelta=None, base=None):
    """Abre `docs/loop/REPORTE.md`, APUNTA SU TOQUE, Y **CAE EN ROJO** si el turno
    tiene sello y todavia no ha declarado sus clases.

    EL TOQUE SE APUNTA ANTES DE DECIDIR NADA, y eso es deliberado: el modulo dice
    desde la vuelta 182 que `apuntar()` *"se llama ANTES de hacer la cosa, no
    despues: si la cosa revienta, el toque igual paso"*. Un intento de leer el
    reporte es un intento, y se registra. **Apuntar de mas solo puede hacer las
    guardas mas estrictas, nunca mas laxas**, que es el lado seguro.

    CAE LEVANTANDO `ReporteFueraDeOrden` en vez de devolviendo un valor, porque
    quien llama a esto quiere el texto y no un veredicto, y una cadena vacia
    devuelta en silencio es justo la degradacion que el banco 9 prohibe."""
    apuntar("REPORTE.md")
    ok, motivo = puede_leer_reporte(vuelta=vuelta, base=base)
    if not ok:
        raise ReporteFueraDeOrden(motivo)
    ruta = ruta or os.path.join(LOOP, "REPORTE.md")
    if not os.path.exists(ruta):
        return ""
    return io.open(ruta, encoding="utf-8", errors="replace").read()


def _git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", errors="replace")


def sha(t):
    return hashlib.sha256(t.replace(chr(13) + NL, NL).encode("utf-8")).hexdigest()


def puede_sellar():
    """(SI_PUEDE, MOTIVO). PURA sobre el estado del modulo.

    ESTA ES LA FUNCION QUE EL ARNES TUMBA, y por eso esta separada de `sellar()`:
    la decision se puede probar sin escribir un solo fichero."""
    malos = toques_prohibidos()
    if malos:
        return False, ("el turno ya toco %s antes de sellar. EL SUJETO DE LA CIEGA "
                       "YA PUDO QUEMARSE, y un sello escrito ahora no probaria "
                       "nada." % ", ".join(repr(m) for m in malos))
    if _SELLADO["hecho"]:
        return False, "este turno ya sello: un sello no se reescribe"
    return True, "la bitacora esta limpia de los tres prohibidos"


def _apuntar_sello(ruta, vuelta):
    """MARCA EL SELLO EN EL ESTADO DEL TURNO Y LO GUARDA. Es la COLA de
    `sellar()`, la parte que corre DESPUES de que el sello ya este escrito en
    disco, y va separada por el mismo motivo que `puede_sellar()` esta separada
    de `sellar()`: **para que un arnes la pueda correr sin escribir un sello de
    verdad ni arrancar el aislador**.

    ANTES ESTABA EN LINEA DENTRO DE `sellar()`, Y ESO TENIA UN PRECIO MEDIDO: el
    arnes de la vuelta 199 tenia que COPIAR estas cuatro lineas en su proceso
    hijo, y una copia no se entera de las mutaciones que se le hacen al original.
    Su MUTACION `B` salio ROJA por eso, no por el remedio. **Un caso que prueba
    una copia de si mismo no prueba nada** (`EJECUTOR.md` 1, 29 ago 2026), y la
    salida honesta era hacer testable lo que se estaba probando, no aflojar el
    caso.

    LA LINEA DE `_VIVO` ES LA OTRA MITAD DE LA `1.a` (vuelta 199): UN TURNO QUE
    SELLA ESTA VIVO. Si el fichero venia marcado como cerrado por el turno
    ANTERIOR y nadie lo reabre, `_guardar_turno()` volveria a escribir
    `vivo.abierto: false` JUNTO CON el sello, y el proceso siguiente tiraria el
    sello recien puesto."""
    _SELLADO["hecho"] = True
    _SELLADO["ruta"] = ruta
    _SELLADO["vuelta"] = str(vuelta)
    _VIVO["abierto"] = True
    _guardar_turno()


def sellar(criterio, vuelta, muestra=None, semilla=None, puestos=None,
           excluir=None, dominio=None, clase=None, dir_salida=None):
    """CORRE EL AISLADOR Y SELLA SU SALIDA. Devuelve (ok, informe).

    CAE EN ROJO Y NO ESCRIBE NADA si `puede_sellar()` dice que no. El rojo es del
    sello entero: no se escribe el sello, y tampoco se corre el aislador, porque
    correrlo sin poder sellarlo seria producir una ciega que nadie puede citar."""
    informe = []
    w = informe.append
    base = dir_salida or LOOP

    # LA GUARDA DE DISCO (vuelta 193, TAREA 4.b). VA ANTES DE `puede_sellar()` A
    # PROPOSITO: `puede_sellar()` mira la MEMORIA, y la memoria muere con el
    # proceso. Un sello YA ESCRITO en disco es la unica prueba que sobrevive, y
    # reescribirlo borra la bitacora que lo acompanaba.
    ya = sello_en_disco(vuelta, base)
    if ya:
        w("PUEDE SELLAR: NO")
        w("   motivo: YA HAY SELLO EN DISCO para la vuelta %s, y un sello no se"
          % vuelta)
        w("   reescribe. Reescribirlo publicaria `prohibidos antes del sello: 0`")
        w("   sobre una bitacora que el proceso nuevo no vio.")
        w("   sello que ya existe: %s (%d bytes)"
          % (os.path.relpath(ya, RAIZ).replace(os.sep, "/"), os.path.getsize(ya)))
        w("   bitacora del turno hasta ahora: %s"
          % (", ".join(bitacora()) if bitacora() else "(vacia)"))
        w("ROJO: NO se corre el aislador y NO se escribe ningun sello.")
        return False, informe

    ok, motivo = puede_sellar()
    w("PUEDE SELLAR: %s" % ("SI" if ok else "NO"))
    w("   motivo: %s" % motivo)
    w("   bitacora del turno hasta ahora: %s"
      % (", ".join(bitacora()) if bitacora() else "(vacia)"))
    if not ok:
        w("ROJO: NO se corre el aislador y NO se escribe ningun sello.")
        return False, informe

    ciega = os.path.join(base, "_auditor_v%s_ciega_blind.txt" % vuelta)
    destape = os.path.join(base, "_auditor_v%s_ciega_reveal.txt" % vuelta)
    cmd = [sys.executable, os.path.join(RAIZ, "scripts", "loop",
                                        "aislador_de_ciega.py"),
           "--criterio", criterio, "--ciega", ciega, "--destape", destape]
    for bandera, valor in (("--muestra", muestra), ("--semilla", semilla),
                           ("--puestos", puestos), ("--excluir", excluir),
                           ("--dominio", dominio), ("--clase", clase)):
        if valor is not None:
            cmd += [bandera, str(valor)]
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, env=env)
    salida = (r.stdout.decode("utf-8", errors="replace")
              + r.stderr.decode("utf-8", errors="replace"))
    w("AISLADOR CORRIDO -> EXITCODE %d" % r.returncode)
    if r.returncode != 0 or not os.path.exists(ciega) or not os.path.exists(destape):
        w("ROJO: el aislador no dejo sus dos ficheros. NO se escribe sello.")
        for l in salida.split(NL)[-12:]:
            if l.strip():
                w("   | " + l.strip()[:130])
        return False, informe

    t_ciega = io.open(ciega, encoding="utf-8").read()
    t_destape = io.open(destape, encoding="utf-8").read()
    sello = {
        "vuelta": vuelta,
        "criterio": criterio,
        "ciega": os.path.relpath(ciega, RAIZ).replace(os.sep, "/"),
        "destape": os.path.relpath(destape, RAIZ).replace(os.sep, "/"),
        "bytes_ciega": os.path.getsize(ciega),
        "bytes_destape": os.path.getsize(destape),
        "sha256_ciega": sha(t_ciega),
        "sha256_destape": sha(t_destape),
        "bitacora_antes_del_sello": bitacora(),
        "prohibidos_antes_del_sello": toques_prohibidos(),
    }
    ruta = os.path.join(base, "SELLO_APERTURA_AUDITOR_V%s.json" % vuelta)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(
        json.dumps(sello, ensure_ascii=False, indent=1) + NL)
    _apuntar_sello(ruta, vuelta)
    w("SELLO ESCRITO: %s (%d bytes)"
      % (os.path.relpath(ruta, RAIZ).replace(os.sep, "/"), os.path.getsize(ruta)))
    w("   ciega   %s -> %d bytes | sha256 %s"
      % (sello["ciega"], sello["bytes_ciega"], sello["sha256_ciega"][:16]))
    w("   destape %s -> %d bytes | sha256 %s"
      % (sello["destape"], sello["bytes_destape"], sello["sha256_destape"][:16]))
    w("   prohibidos tocados antes del sello: %d"
      % len(sello["prohibidos_antes_del_sello"]))
    return True, informe


# --------------------------------------------------- LA CUARTA PUERTA (v192)
def puestos_sellados(ruta_sello=None):
    """LOS PUESTOS QUE EL SELLO DE ESTE TURNO ELIGIO. Devuelve una lista de
    enteros, VACIA si todavia no hay sello.

    NO SE TECLEAN NI SE PASAN POR ARGUMENTO: se leen del propio sello, que nombra
    la ciega, y de la ciega, que lista sus `puesto_intra`. **El sujeto de la
    cuarta puerta lo define el sello y nadie mas**, que es lo que impide elegirlo
    despues de mirar."""
    ruta = ruta_sello or _SELLADO["ruta"]
    if not ruta or not os.path.exists(ruta):
        return []
    try:
        sello = json.load(io.open(ruta, encoding="utf-8"))
    except Exception:
        return []
    rel = sello.get("ciega")
    if not rel:
        return []
    p = rel if os.path.isabs(rel) else os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.exists(p):
        return []
    texto = io.open(p, encoding="utf-8", errors="replace").read()
    return sorted(set(int(x) for x in
                      re.findall(r"puesto_intra[^0-9]{0,12}(\d+)", texto)))


def leer_veredictos(destapar_sujeto=False, ruta=None, ruta_sello=None):
    """EL ARCHIVO DE VEREDICTOS, Y APUNTA SU TOQUE. **ES LA CUARTA PUERTA.**

    Devuelve la lista de filas. Con `destapar_sujeto=False`, que es lo normal,
    **las filas de los puestos sellados salen con `clase` y `razon` TAPADAS**: se
    pueden contar, se pueden cruzar por `puesto_intra`, y no se puede ver lo que
    la ciega esconde. Con `destapar_sujeto=True` salen enteras **y se apunta un
    toque distinto**, el de destape, que es el que hace caer
    `declarar_clases_escritas()` si viene antes.

    Apunta SIEMPRE un toque, incluso tapando, porque un turno tiene derecho a
    saber cuantas veces se abrio el archivo."""
    apuntar(TOQUE_DESTAPE if destapar_sujeto else TOQUE_VEREDICTOS)
    p = ruta or os.path.join(RAIZ, ARCHIVO_DE_VEREDICTOS.replace("/", os.sep))
    filas = [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]
    if destapar_sujeto:
        return filas
    sellados = set(puestos_sellados(ruta_sello))
    if not sellados:
        return filas
    tapadas = []
    for f in filas:
        if f.get("puesto_intra") in sellados:
            f = dict(f)
            for campo in CAMPOS_QUE_DESTAPAN:
                if campo in f:
                    f[campo] = TAPADO
        tapadas.append(f)
    return tapadas


def marcador(ruta=None):
    """EL RECUENTO POR CLASE SOBRE EL ARCHIVO ENTERO. Devuelve un dict.

    **NO DESTAPA NADA Y POR ESO NO HACE FALTA PEDIRLO:** un agregado de miles de
    filas no dice la clase de ninguna. Existe para que la cuarta puerta no
    estorbe lo que el acta SI tiene que hacer, que es recomputar el marcador
    ANTES de escribir sus clases."""
    apuntar(TOQUE_VEREDICTOS)
    p = ruta or os.path.join(RAIZ, ARCHIVO_DE_VEREDICTOS.replace("/", os.sep))
    filas = [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]
    por_clase = {}
    for f in filas:
        por_clase[f.get("clase")] = por_clase.get(f.get("clase"), 0) + 1
    return {"filas": len(filas), "por_clase": por_clase}


# --------------------------------------------------------------------------
# LA GUARDA DE LA `C.A1` (vuelta 197, TAREA 2.c).
#
# POR QUE ES DE CODIGO Y NO DE MEMORIA, Y ESTA MEDIDO: TRES ACTAS SEGUIDAS (195,
# 196 y 197) recontaron el marcador con `json` a mano en vez de por
# `AP.marcador()`. **El remedio de memoria ya se probo y fallo**: el acta 196
# declaro la caida, la remedio DENTRO de su vuelta corriendo el instrumento, y el
# acta 197 volvio a caer por la misma puerta. Un remedio que hay que recordar no
# es un remedio.
#
# LO QUE LA GUARDA EXIGE: que la cifra del marcador que un acta PUBLICA calce con
# una SALIDA SELLADA de `marcador()` **de esa misma vuelta**. Si esa salida no
# existe, es ROJO; si existe y no calza, es ROJO. **No hay tercera via**: un acta
# que publique un marcador que nadie sello por este carril no pasa.
NOMBRE_SALIDA_MARCADOR = "SALIDA_MARCADOR_AUDITOR_V%s.json"

# LA FORMA EN QUE LAS ACTAS ESCRIBEN SU FILA DEL MARCADOR, LEIDA DE LAS ACTAS 195,
# 196 y 197 y no inventada: `**3388 filas; A 551, B 72, C 5, D 2760**`.
PAT_FILAS_DEL_ACTA = re.compile(r"\*\*(\d[\d.,]*)\s+filas")
PAT_CLASE_DEL_ACTA = re.compile(r"\b([A-Z])\s+(\d[\d.,]*)\b")


def _entero(literal):
    """UN ENTERO DE UN LITERAL DE ACTA, QUE PUEDE TRAER PUNTOS DE MILLAR. PURA.
    Devuelve el entero o None. `1.306` es mil trescientos seis en esta casa, y no
    uno coma tres."""
    if literal is None:
        return None
    limpio = str(literal).replace(".", "").replace(",", "").strip()
    return int(limpio) if limpio.isdigit() else None


def sellar_marcador(vuelta, ruta=None, base=None):
    """CORRE `marcador()` Y SELLA SU SALIDA EN UN FICHERO DE ESA VUELTA.
    Devuelve (ruta_escrita, medicion).

    ES LA MITAD QUE HACE QUE LA GUARDA PUEDA MORDER: sin una salida sellada no hay
    contra que cotejar, y entonces "calza con `AP.marcador()`" seria una
    afirmacion y no una medicion."""
    m = marcador(ruta=ruta)
    destino = os.path.join(base or LOOP, NOMBRE_SALIDA_MARCADOR % vuelta)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(
        json.dumps({"vuelta": str(vuelta), "filas": m["filas"],
                    "por_clase": m["por_clase"]},
                   ensure_ascii=False, indent=1, sort_keys=True) + NL)
    return destino, m


def salida_del_marcador(vuelta, base=None):
    """LA SALIDA SELLADA DE `marcador()` DE UNA VUELTA, o None si no existe o no
    se puede leer. PURA salvo por leer el fichero."""
    ruta = os.path.join(base or LOOP, NOMBRE_SALIDA_MARCADOR % vuelta)
    if not os.path.exists(ruta):
        return None
    try:
        return json.load(io.open(ruta, encoding="utf-8"))
    except Exception:                                    # noqa: BLE001
        return None


def cifras_del_marcador_del_acta(texto):
    """LAS CIFRAS DEL MARCADOR QUE UN ACTA PUBLICA. PURA.
    Devuelve `{"filas": int, "por_clase": {...}}` o None si el texto no las trae.

    LEE LA FORMA QUE LAS ACTAS USAN, que no es la del `json` del modulo:
    `**3388 filas; A 551, B 72, C 5, D 2760**`. Un texto que no traiga la palabra
    `filas` en negrita devuelve None, **y quien llame CAE**, en vez de comparar
    contra un diccionario vacio y salir verde por no haber encontrado nada."""
    if not texto:
        return None
    m = PAT_FILAS_DEL_ACTA.search(texto)
    if not m:
        return None
    filas = _entero(m.group(1))
    if filas is None:
        return None
    # EL REPARTO SE LEE SOLO DESDE DONDE ACABA `filas`, para que un numero de
    # cualquier otra parte de la linea no entre como si fuera una clase.
    cola = texto[m.end():]
    corte = cola.find("**")
    if corte >= 0:
        cola = cola[:corte]
    por_clase = {}
    for clase, cifra in PAT_CLASE_DEL_ACTA.findall(cola):
        v = _entero(cifra)
        if v is not None and clase not in por_clase:
            por_clase[clase] = v
    return {"filas": filas, "por_clase": por_clase}


def guarda_del_marcador(texto, vuelta, base=None):
    """(OK, INFORME). LA GUARDA DE LA `C.A1`, ENTERA.

    CAE EN ROJO en los tres casos que importan, y ninguno se adivina:
      . el acta NO publica cifras de marcador legibles;
      . NO existe salida sellada de `marcador()` de esa vuelta;
      . existe y NO calza, en las filas o en el reparto por clase.

    PURA salvo por leer la salida sellada."""
    informe = []
    w = informe.append
    w("GUARDA DEL MARCADOR (C.A1), vuelta %s" % vuelta)
    del_acta = cifras_del_marcador_del_acta(texto)
    w("   cifras que el acta publica: %r" % (del_acta,))
    if del_acta is None:
        w("   ROJO: el acta no publica ninguna cifra de marcador legible. No se")
        w("   supone que no la tenga: se cae, que es lo que hace mirar.")
        return False, informe
    sellada = salida_del_marcador(vuelta, base)
    ruta = os.path.join(base or LOOP, NOMBRE_SALIDA_MARCADOR % vuelta)
    w("   salida sellada esperada: %s"
      % os.path.relpath(ruta, RAIZ).replace(os.sep, "/"))
    if sellada is None:
        w("   ROJO: NO existe salida de marcador() de esta vuelta, o no se puede")
        w("   leer. Una cifra de marcador que nadie saco por este carril es")
        w("   exactamente la C.A1, y por eso no pasa.")
        return False, informe
    w("   cifras de la salida sellada: filas %s, por_clase %r"
      % (sellada.get("filas"), sellada.get("por_clase")))
    fallos = []
    if del_acta["filas"] != sellada.get("filas"):
        fallos.append("filas: el acta dice %s y marcador() dice %s"
                      % (del_acta["filas"], sellada.get("filas")))
    sel_clases = sellada.get("por_clase") or {}
    for clase in sorted(set(list(del_acta["por_clase"]) + list(sel_clases))):
        a = del_acta["por_clase"].get(clase)
        b = sel_clases.get(clase)
        if a != b:
            fallos.append("clase %s: el acta dice %r y marcador() dice %r"
                          % (clase, a, b))
    for f in fallos:
        w("   NO CALZA -> %s" % f)
    if fallos:
        w("   ROJO: %d discrepancia(s). El acta NO puede publicar ese marcador."
          % len(fallos))
        return False, informe
    w("   VERDE: las filas y las %d clases calzan con la salida sellada."
      % len(sel_clases))
    return True, informe


def destapes_antes_de_las_clases():
    """LOS TOQUES DE DESTAPE QUE LA BITACORA TRAE. PURA sobre el estado del
    modulo, y es la funcion que `puede_declarar_clases()` consulta.

    Va separada por el mismo motivo que `toques_prohibidos()`: **la decision se
    puede probar sin escribir un solo fichero.**"""
    return [t for t in _BITACORA if t == TOQUE_DESTAPE]


def puede_declarar_clases():
    """(SI_PUEDE, MOTIVO). PURA sobre el estado del modulo.

    **ESTA ES LA FUNCION QUE EL ARNES TUMBA.** Cae si el turno destapo el sujeto
    antes de escribir sus clases: unas clases escritas DESPUES de ver el archivo
    no prueban nada, que es exactamente lo mismo que dice `puede_sellar()` sobre
    el sello."""
    malos = destapes_antes_de_las_clases()
    if malos:
        return False, ("el turno destapo `clase` o `razon` de los puestos "
                       "SELLADOS %d vez(ces) ANTES de escribir sus clases. EL "
                       "SUJETO YA SE QUEMO, y unas clases escritas ahora no "
                       "probarian nada." % len(malos))
    if _CLASES["escritas"]:
        return False, "este turno ya declaro sus clases: no se declaran dos veces"
    if not _SELLADO["hecho"]:
        return False, ("este turno no ha sellado. Sin sello no hay sujeto, y sin "
                       "sujeto no hay clases que declarar")
    return True, "la bitacora esta limpia de destapes y el sello esta escrito"


def cerrados():
    """LAS VUELTAS CUYO TURNO YA SE CERRO, con lo que se registro de cada una.
    Copia, no el original."""
    return dict(_CERRADOS)


def cerrar_turno(motivo, vuelta=None, ruta_clases=None):
    """CIERRA EL TURNO DEJANDO CONSTANCIA, SIN BORRAR NADA. Devuelve
    (ok, informe).

    ES EL REMEDIO DEL HALLAZGO `5.4` DEL ACTA 197, y lo que hace es exactamente
    esto y nada mas:

      . escribe en el fichero del turno un registro `cerrados[vuelta]` con el
        motivo, la ruta de las clases y **la bitacora tal como quedo**;
      . marca el bloque vivo como CERRADO, con lo que `_cargar_turno()` de un
        proceso nuevo **reinicia la memoria y empieza limpio**;
      . **NO borra el fichero**, **NO borra el sello en disco** y **NO toca la
        memoria de este proceso**, que sigue viendo su propio turno entero hasta
        que termine.

    POR QUE NO SE LIMPIA LA MEMORIA AQUI: el proceso que declara sus clases sigue
    siendo el mismo turno y sigue necesitando su estado. Lo que tiene que empezar
    limpio es EL SIGUIENTE, y eso lo decide la carga, no el cierre."""
    informe = []
    w = informe.append
    clave = str(vuelta) if vuelta is not None else None
    if clave:
        _CERRADOS[clave] = {"motivo": motivo,
                            "ruta_clases": ruta_clases,
                            "bitacora": list(_BITACORA)}
    _VIVO["abierto"] = False
    _guardar_turno()
    w("TURNO CERRADO: %s" % motivo)
    w("   vuelta registrada en `cerrados`: %s" % (clave or "(ninguna)"))
    w("   el fichero del turno NO se borra: %s"
      % os.path.relpath(RUTA_DEL_TURNO, RAIZ).replace(os.sep, "/"))
    w("   un turno NUEVO lo cargara como CERRADO y empezara limpio SIN borrar")
    w("   nada. El sello en disco NO se toca y la guarda `b` de sellar() sigue")
    w("   mirando el disco igual que antes.")
    w("   vueltas cerradas en el fichero: %s"
      % (", ".join(sorted(_CERRADOS)) or "(ninguna)"))
    return True, informe


def puede_declarar_clases_con_sello(vuelta, base=None):
    """(SI_PUEDE, MOTIVO), LEYENDO EL SELLO DEL DISCO Y NO DE LA MEMORIA.

    **ES LA PIEZA `c` DE LA TAREA 4 DE LA VUELTA 193.** `puede_declarar_clases()`
    mira `_SELLADO`, que es estado de MODULO: el auditor sella con el CLI, en un
    proceso que termina, y en el siguiente respondia `NO: este turno no ha
    sellado` **aunque el sello estuviera en disco**. Sin esto la cuarta puerta no
    la podia usar nadie que sellara por CLI, o sea nadie.

    **LO QUE NO SE AFLOJA:** la guarda de los destapes sigue siendo la de la
    bitacora, y la bitacora ahora sobrevive al proceso. Si el turno destapo antes,
    esto CAE igual."""
    malos = destapes_antes_de_las_clases()
    if malos:
        return False, ("el turno destapo `clase` o `razon` de los puestos "
                       "SELLADOS %d vez(ces) ANTES de escribir sus clases. EL "
                       "SUJETO YA SE QUEMO." % len(malos))
    if _CLASES["escritas"]:
        return False, "este turno ya declaro sus clases: no se declaran dos veces"
    # LA GUARDA QUE EL CIERRE OBLIGA A HACER EXPLICITA (vuelta 197, TAREA 2.b).
    # Antes, "no se declaran dos veces" lo sostenia `_CLASES` cargado del fichero.
    # Al cerrar el turno esa memoria se limpia para el turno siguiente, asi que la
    # prohibicion se guarda POR VUELTA y en un sitio que el cierre no borra.
    # ES LA MISMA GUARDA, MAS EXPLICITA, NO UNA MAS FLOJA.
    if str(vuelta) in _CERRADOS:
        return False, ("el turno de la vuelta %s YA SE CERRO con sus clases "
                       "declaradas (%s). No se declaran dos veces, y esto vale "
                       "TAMBIEN entre procesos."
                       % (vuelta, _CERRADOS[str(vuelta)].get("ruta_clases")))
    ruta = sello_en_disco(vuelta, base)
    if not ruta:
        return False, ("no hay sello en disco para la vuelta %s. Sin sello no hay "
                       "sujeto, y sin sujeto no hay clases que declarar" % vuelta)
    return True, ("la bitacora esta limpia de destapes y el sello de la vuelta %s "
                  "esta en disco: %s"
                  % (vuelta, os.path.relpath(ruta, RAIZ).replace(os.sep, "/")))


def declarar_clases_con_sello(ruta_clases, vuelta, base=None):
    """MARCA LAS CLASES ESCRITAS LEYENDO EL SELLO DE DISCO. Devuelve
    (ok, informe). Gemelo de `declarar_clases_escritas()` para el carril del
    CLI, que es el que el auditor usa de verdad."""
    informe = []
    w = informe.append
    ok, motivo = puede_declarar_clases_con_sello(vuelta, base)
    w("PUEDE DECLARAR LAS CLASES (leyendo el sello de DISCO): %s"
      % ("SI" if ok else "NO"))
    w("   motivo: %s" % motivo)
    w("   bitacora del turno hasta ahora: %s"
      % (", ".join(bitacora()) if bitacora() else "(vacia)"))
    w("   destapes apuntados: %d" % len(destapes_antes_de_las_clases()))
    if not ok:
        w("ROJO: NO se marca nada. La ciega de este turno NO se puede citar.")
        return False, informe
    if not os.path.exists(ruta_clases):
        w("ROJO: %s no existe. Unas clases que no estan escritas no se declaran."
          % ruta_clases)
        return False, informe
    _CLASES["escritas"] = True
    _CLASES["ruta"] = ruta_clases
    _SELLADO["hecho"] = True
    _SELLADO["ruta"] = sello_en_disco(vuelta, base)
    _SELLADO["vuelta"] = str(vuelta)
    _guardar_turno()
    w("CLASES DECLARADAS: %s (%d bytes)"
      % (ruta_clases, os.path.getsize(ruta_clases)))
    w("   desde aqui, destapar el sujeto ya no quema nada.")
    w("   Y DESDE AQUI TAMBIEN SE PUEDE LEER `REPORTE.md`: la guarda de la "
      "TAREA 2.a")
    w("   de la vuelta 197 lo prohibia mientras las clases no estuvieran escritas.")
    _ok_c, inf_c = cerrar_turno("clases declaradas por el carril del sello de disco",
                                vuelta=vuelta, ruta_clases=ruta_clases)
    for l in inf_c:
        w("   " + l)
    return True, informe


def declarar_clases_escritas(ruta_clases):
    """MARCA QUE LAS CLASES DEL AUDITOR ESTAN ESCRITAS. Devuelve (ok, informe).

    **CAE EN ROJO Y NO MARCA NADA** si `puede_declarar_clases()` dice que no. Es
    el gemelo exacto de `sellar()`: alli el rojo era no poder sellar; aqui es no
    poder declarar, **y a partir de aqui destapar el sujeto ya no quema nada**,
    porque las clases ya estan escritas."""
    informe = []
    w = informe.append
    ok, motivo = puede_declarar_clases()
    w("PUEDE DECLARAR LAS CLASES: %s" % ("SI" if ok else "NO"))
    w("   motivo: %s" % motivo)
    w("   bitacora del turno hasta ahora: %s"
      % (", ".join(bitacora()) if bitacora() else "(vacia)"))
    w("   destapes apuntados: %d" % len(destapes_antes_de_las_clases()))
    if not ok:
        w("ROJO: NO se marca nada. La ciega de este turno NO se puede citar.")
        return False, informe
    if not os.path.exists(ruta_clases):
        w("ROJO: %s no existe. Unas clases que no estan escritas no se declaran."
          % ruta_clases)
        return False, informe
    _CLASES["escritas"] = True
    _CLASES["ruta"] = ruta_clases
    _guardar_turno()
    w("CLASES DECLARADAS: %s (%d bytes)"
      % (ruta_clases, os.path.getsize(ruta_clases)))
    w("   desde aqui, destapar el sujeto ya no quema nada.")
    _ok_c, inf_c = cerrar_turno("clases declaradas por el carril de memoria",
                                vuelta=_SELLADO.get("vuelta"),
                                ruta_clases=ruta_clases)
    for l in inf_c:
        w("   " + l)
    return True, informe


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--criterio")
    ap.add_argument("--vuelta")
    ap.add_argument("--muestra", type=int)
    ap.add_argument("--semilla", type=int)
    ap.add_argument("--puestos")
    ap.add_argument("--excluir")
    ap.add_argument("--dominio")
    ap.add_argument("--clase")
    ap.add_argument("--estado", action="store_true",
                    help="imprime la bitacora y si se puede sellar, y no hace mas")
    ap.add_argument("--declarar-clases", dest="declarar_clases",
                    help="RUTA del fichero de clases del auditor. Lee el sello "
                         "de DISCO y marca las clases escritas (vuelta 193, "
                         "TAREA 4.c). Necesita --vuelta")
    ap.add_argument("--olvidar-turno", action="store_true",
                    help="borra el fichero del turno. Es un ACTO y se dice: "
                         "quien lo corra empieza con la bitacora limpia")
    ap.add_argument("--cerrar-turno", dest="cerrar_turno", action="store_true",
                    help="CIERRA el turno dejando constancia y SIN borrar nada "
                         "(vuelta 197, TAREA 2.b). Necesita --vuelta")
    ap.add_argument("--sellar-marcador", dest="sellar_marcador",
                    action="store_true",
                    help="corre marcador() y SELLA su salida en "
                         "SALIDA_MARCADOR_AUDITOR_V<vuelta>.json. Necesita "
                         "--vuelta")
    ap.add_argument("--guarda-marcador", dest="guarda_marcador",
                    help="RUTA de un fichero de texto (el acta o su seccion). "
                         "Comprueba que el marcador que publica calza con la "
                         "salida sellada de esa vuelta. Necesita --vuelta")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("APERTURA DEL AUDITOR. Gemelo del bloque de apertura del ejecutor.")
    print("=" * 78)
    print("   LOS TRES PROHIBIDOS ANTES DEL SELLO: %s"
          % ", ".join(repr(p) for p in PROHIBIDOS_ANTES_DEL_SELLO))
    print("   Y LA CUARTA PUERTA, ANTES DE LAS CLASES: %s, campos %s"
          % (ARCHIVO_DE_VEREDICTOS,
             ", ".join(repr(c) for c in CAMPOS_QUE_DESTAPAN)))
    print("   FICHERO DEL TURNO: %s (%s)"
          % (os.path.relpath(RUTA_DEL_TURNO, RAIZ).replace(os.sep, "/"),
             "existe, %d bytes" % os.path.getsize(RUTA_DEL_TURNO)
             if os.path.exists(RUTA_DEL_TURNO) else "no existe todavia"))
    if a.olvidar_turno:
        olvidar_todo()
        print("   FICHERO DEL TURNO BORRADO. La bitacora empieza limpia, Y ESO ES")
        print("   UN ACTO: el sello que hubiera en disco NO se borra, y la guarda")
        print("   de `sellar()` sigue mordiendo porque mira el disco.")
        return 0
    if a.cerrar_turno:
        if not a.vuelta:
            print("   ROJO: --cerrar-turno necesita --vuelta para saber que")
            print("   vuelta queda registrada como cerrada.")
            return 1
        _ok, informe = cerrar_turno("cerrado a mano por el CLI", vuelta=a.vuelta)
        for l in informe:
            print("   " + l)
        return 0
    if a.sellar_marcador:
        if not a.vuelta:
            print("   ROJO: --sellar-marcador necesita --vuelta.")
            return 1
        destino, m = sellar_marcador(a.vuelta)
        print("   SALIDA DE marcador() SELLADA: %s (%d bytes)"
              % (os.path.relpath(destino, RAIZ).replace(os.sep, "/"),
                 os.path.getsize(destino)))
        print("   filas %d | por_clase %r" % (m["filas"], m["por_clase"]))
        print("   ESTA es la salida contra la que --guarda-marcador cotejara lo")
        print("   que el acta publique. Sin ella, la guarda CAE EN ROJO.")
        return 0
    if a.guarda_marcador:
        if not a.vuelta:
            print("   ROJO: --guarda-marcador necesita --vuelta.")
            return 1
        if not os.path.exists(a.guarda_marcador):
            print("   ROJO: %s no existe." % a.guarda_marcador)
            return 1
        texto = io.open(a.guarda_marcador, encoding="utf-8",
                        errors="replace").read()
        ok, informe = guarda_del_marcador(texto, a.vuelta)
        for l in informe:
            print("   " + l)
        print("   VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
        return 0 if ok else 1
    if a.declarar_clases:
        if not a.vuelta:
            print("   ROJO: --declarar-clases necesita --vuelta para saber que")
            print("   sello leer del disco.")
            return 1
        ok, informe = declarar_clases_con_sello(a.declarar_clases, a.vuelta)
        for l in informe:
            print("   " + l)
        print("   VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
        return 0 if ok else 1
    if a.estado:
        ok, motivo = puede_sellar()
        print("   bitacora: %s" % (", ".join(bitacora()) or "(vacia)"))
        print("   PUEDE SELLAR: %s (%s)" % ("SI" if ok else "NO", motivo))
        ok2, motivo2 = puede_declarar_clases()
        print("   LA CUARTA PUERTA: %s" % ARCHIVO_DE_VEREDICTOS)
        print("      campos que destapan: %s"
              % ", ".join(repr(c) for c in CAMPOS_QUE_DESTAPAN))
        print("      destapes apuntados: %d" % len(destapes_antes_de_las_clases()))
        print("   PUEDE DECLARAR LAS CLASES: %s (%s)"
              % ("SI" if ok2 else "NO", motivo2))
        ok3, motivo3 = puede_leer_reporte(vuelta=a.vuelta)
        print("   PUEDE LEER REPORTE.md: %s (%s)"
              % ("SI" if ok3 else "NO", motivo3))
        print("   TURNO VIVO ABIERTO: %s" % ("SI" if _VIVO["abierto"] else "NO"))
        print("   VUELTAS YA CERRADAS en el fichero del turno: %s"
              % (", ".join(sorted(_CERRADOS)) or "(ninguna)"))
        return 0
    if not a.criterio or not a.vuelta:
        print("   ROJO: --criterio y --vuelta son obligatorios. Sin criterio "
              "escrito no se elige ningun sujeto.")
        return 1
    ok, informe = sellar(a.criterio, a.vuelta, muestra=a.muestra,
                         semilla=a.semilla, puestos=a.puestos, excluir=a.excluir,
                         dominio=a.dominio, clase=a.clase)
    for l in informe:
        print("   " + l)
    print("   VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    return 0 if ok else 1


# LA CARGA AL IMPORTAR (vuelta 193, TAREA 4.a). VA AQUI, AL FINAL Y FUERA DE
# `main()`, PORQUE TIENE QUE CORRER TAMBIEN CUANDO EL MODULO SE IMPORTA: el turno
# del auditor pasa por `import apertura_del_auditor`, no solo por el CLI. Si el
# fichero no existe, no hace nada y el turno empieza limpio.
_CARGADO_DEL_DISCO = _cargar_turno()


if __name__ == "__main__":
    sys.exit(main())
