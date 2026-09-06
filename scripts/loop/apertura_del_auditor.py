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
                        "clases": dict(_CLASES)},
                       ensure_ascii=False, indent=1) + NL)
    except Exception:                                    # noqa: BLE001
        pass


def _cargar_turno():
    """CARGA EL ESTADO DEL TURNO DE SU FICHERO, si existe. Devuelve True si
    cargo algo. **Se llama al importar el modulo**, que es lo que hace que los
    toques de una corrida los vea la siguiente."""
    if not os.path.exists(RUTA_DEL_TURNO):
        return False
    try:
        d = json.load(io.open(RUTA_DEL_TURNO, encoding="utf-8"))
    except Exception:                                    # noqa: BLE001
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


def leer_reporte(ruta=None):
    """Abre `docs/loop/REPORTE.md`, Y APUNTA SU TOQUE."""
    apuntar("REPORTE.md")
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
    _SELLADO["hecho"] = True
    _SELLADO["ruta"] = ruta
    _SELLADO["vuelta"] = str(vuelta)
    _guardar_turno()
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
