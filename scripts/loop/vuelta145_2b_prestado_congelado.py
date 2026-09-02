# -*- coding: utf-8 -*-
r"""vuelta145_2b_prestado_congelado.py . EL PRE-ESTADO CONGELADO, VUELTA 145,
TAREA 2.b.

POR QUE NACE (acta 144, caida 4.9 del auditor, "EL SUJETO VIVO"). Un arnes de
mutacion cuyo sujeto es EL ARBOL DE TRABAJO deja de medir en cuanto el arbol se
mueve, y la vuelta que lo escribe es la ultima que lo ve verde.
`vuelta144_3b_mutacion_negativa.py` es el ejemplar duro: su contraprueba (C)
pide que el sellador de `OP-M-04` salga VERDE, y ya no puede, porque LA FUSION
QUE SELLA YA CORRIO y sus dos absorbidos estan deprecados. No es que este mal
corrida: NO PUEDE VOLVER A ESTAR VERDE NUNCA.

QUE HACE. Materializa en un directorio TEMPORAL el estado de unos ficheros TAL
COMO ESTABAN en un commit dado, para que un arnes pueda apuntar alli sus rutas
en vez de al arbol vivo. Es el mismo patron que
`SUJETO_FIJO_V135_2E_REPORTE_134.md` (banco 9.10), con una sola diferencia
declarada: EL SUJETO NO SE COPIA AL REPOSITORIO, SE LEE DE GIT. Congelar por
ref en vez de por fichero se elige porque los sujetos de este caso son nodos
del catalogo y `docs/plan/OPERACIONES.jsonl`, y una copia commiteada de un nodo
seria un SEGUNDO nodo con el mismo id: exactamente la clase de duplicado que la
campana persigue. Git ya es el congelador, y el commit citado es el ancla.

EL COMMIT DEL PRE-ESTADO SE COMPUTA, NO SE TECLEA (EJECUTOR.md 1, "LA IDENTIDAD
SE LEE DE GIT"): `commit_antes_de_deprecar()` recorre `git log` del fichero de
un nodo, de lo nuevo a lo viejo, y devuelve el PRIMER commit cuyo blob NO trae
el nodo deprecado. Si no hay ninguno, devuelve None y quien llama para.

P.16, QUIEN FABRICA LIMPIA: `materializar()` es un gestor de contexto y retira
siempre el directorio temporal, salga por donde salga.

USO (como libreria):
  from vuelta145_2b_prestado_congelado import commit_antes_de_deprecar, materializar
"""
import contextlib
import io
import json
import os
import shutil
import subprocess
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout


def blob(ref, ruta_rel):
    """El contenido de `ruta_rel` tal como quedo en `ref`, o None."""
    return _git(["show", "%s:%s" % (ref, ruta_rel)])


def commit_antes_de_deprecar(node_id):
    """EL COMMIT DEL PRE-ESTADO, COMPUTADO. Recorre los commits que tocan
    `dataset/nodos/<node_id>.json`, de lo nuevo a lo viejo, y devuelve el
    PRIMERO cuyo blob NO trae el nodo deprecado, junto con la lista entera de
    commits mirados para que la eleccion sea auditable. (None, mirados) si
    ninguno lo tiene vivo."""
    rel = "dataset/nodos/%s.json" % node_id
    out = _git(["log", "--format=%H", "--", rel])
    if out is None:
        return None, []
    mirados = []
    for h in out.decode("utf-8").split():
        datos = blob(h, rel)
        if datos is None:
            mirados.append((h, "sin blob"))
            continue
        try:
            n = json.loads(datos.decode("utf-8"))
        except ValueError:
            mirados.append((h, "no parsea"))
            continue
        vivo = not (n.get("deprecado") or n.get("deprecated"))
        mirados.append((h, "vivo" if vivo else "deprecado"))
        if vivo:
            return h, mirados
    return None, mirados


def ref_del_preestado(node_id):
    """EL REF DEL PRE-ESTADO ENTERO, COMPUTADO, y es lo que un arnes quiere de
    verdad: no el commit viejo en que ese nodo se toco por ultima vez estando
    vivo (`commit_antes_de_deprecar`, que puede ser de hace veinte vueltas y
    traeria consigo un `OPERACIONES.jsonl` igual de viejo), sino EL ARBOL
    JUSTO ANTES DE LA CIRUGIA: el PADRE del commit que deprecio el nodo.

    Devuelve (ref_padre, hash_del_que_deprecio, mirados). El commit que
    deprecio es el MAS NUEVO que toca el fichero del nodo dejandolo deprecado
    y cuyo predecesor en el log lo tenia vivo; si no lo hay, (None, None,
    mirados)."""
    rel = "dataset/nodos/%s.json" % node_id
    out = _git(["log", "--format=%H", "--", rel])
    if out is None:
        return None, None, []
    historial = []
    for h in out.decode("utf-8").split():
        datos = blob(h, rel)
        estado = "sin blob"
        if datos is not None:
            try:
                n = json.loads(datos.decode("utf-8"))
                estado = "deprecado" if (n.get("deprecado") or n.get("deprecated")) else "vivo"
            except ValueError:
                estado = "no parsea"
        historial.append((h, estado))
    for i, (h, estado) in enumerate(historial):
        siguiente = historial[i + 1][1] if i + 1 < len(historial) else None
        if estado == "deprecado" and siguiente == "vivo":
            padre = _git(["rev-parse", "%s^" % h])
            if padre is None:
                return None, h, historial
            return padre.decode("utf-8").strip(), h, historial
    return None, None, historial


@contextlib.contextmanager
def materializar(ref, rutas_rel):
    """Escribe en un directorio temporal el contenido que `rutas_rel` tenia en
    `ref`, conservando la estructura de carpetas, y cede la raiz temporal.
    Levanta IOError si alguna ruta no existe en ese commit: nunca deja un
    sujeto a medias sin decirlo (banco 9, fallar ruidoso)."""
    raiz = tempfile.mkdtemp(prefix="_v145_prestado_")
    try:
        for rel in rutas_rel:
            datos = blob(ref, rel)
            if datos is None:
                raise IOError("no existe %s en %s: el pre-estado no se puede montar"
                              % (rel, ref))
            destino = os.path.join(raiz, rel.replace("/", os.sep))
            carpeta = os.path.dirname(destino)
            if not os.path.isdir(carpeta):
                os.makedirs(carpeta)
            with io.open(destino, "wb") as f:
                f.write(datos)
        yield raiz
    finally:
        shutil.rmtree(raiz, ignore_errors=True)
