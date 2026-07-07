# -*- coding: utf-8 -*-
"""
db.py - Persistencia del motor (Fase 2.5)

Dos backends detras de la misma interfaz: Supabase (por defecto, si hay
credenciales) y JSON local en engine/projects_local/ (con --offline, o si
Supabase no esta configurado). El CLI no tiene login real: todas las filas
se escriben bajo DEV_USER_ID (engine/scripts/setup_dev_user.py lo crea una
sola vez). El grafo (node_id) vive en archivo, no en la base de datos.
"""
import json
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

BASE = Path(__file__).resolve().parent.parent
load_dotenv(BASE / ".env")

PROJECTS_LOCAL_DIR = BASE / "engine" / "projects_local"

SUPABASE_URL = os.environ.get("SUPABASE_URL", "").strip()
SUPABASE_SERVICE_ROLE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "").strip()
DEV_USER_ID = os.environ.get("DEV_USER_ID", "").strip()

FASES = ("ideacion", "validacion", "planificacion", "ejecucion")

_client = None
_forzar_offline = False


def forzar_offline(valor=True):
    global _forzar_offline
    _forzar_offline = valor


def disponible():
    return bool(SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY and DEV_USER_ID) and not _forzar_offline


def _cliente():
    global _client
    if _client is None:
        from supabase import create_client
        _client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
    return _client


def _ahora():
    return datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# Backend JSON local (--offline, o sin credenciales de Supabase)
# ---------------------------------------------------------------------------

def _ruta_local(project_id):
    PROJECTS_LOCAL_DIR.mkdir(parents=True, exist_ok=True)
    return PROJECTS_LOCAL_DIR / f"{project_id}.json"


def _cargar_local(project_id):
    path = _ruta_local(project_id)
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _guardar_local(project_id, data):
    _ruta_local(project_id).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _crear_proyecto_local(entrada_original):
    project_id = uuid.uuid4().hex[:8]
    data = {
        "id": project_id,
        "user_id": DEV_USER_ID or "dev-local",
        "titulo": None,
        "entrada_original": entrada_original,
        "estado_vivo": None,
        "fase_actual": "ideacion",
        "session_count": 0,
        "status": "active",
        "created_at": _ahora(),
        "updated_at": _ahora(),
        "sessions": [],
        "project_nodes": [],
        "plans": [],
        "numeros_proyecto": {},
    }
    _guardar_local(project_id, data)
    return project_id


# ---------------------------------------------------------------------------
# Interfaz publica: proyectos
# ---------------------------------------------------------------------------

def crear_proyecto(entrada_original):
    if disponible():
        resp = _cliente().table("projects").insert({
            "user_id": DEV_USER_ID,
            "entrada_original": entrada_original,
            "fase_actual": "ideacion",
        }).execute()
        return resp.data[0]["id"]
    return _crear_proyecto_local(entrada_original)


def obtener_proyecto(project_id):
    if disponible():
        resp = _cliente().table("projects").select("*").eq("id", project_id).limit(1).execute()
        return resp.data[0] if resp.data else None
    return _cargar_local(project_id)


def actualizar_proyecto(project_id, **campos):
    campos["updated_at"] = _ahora()
    if disponible():
        _cliente().table("projects").update(campos).eq("id", project_id).execute()
        return
    data = _cargar_local(project_id)
    if data is None:
        return
    data.update(campos)
    _guardar_local(project_id, data)


# ---------------------------------------------------------------------------
# Interfaz publica: sesiones
# ---------------------------------------------------------------------------

def crear_sesion(project_id, tipo, mensaje_entrada, puerta_entrada=None):
    if disponible():
        proyecto = obtener_proyecto(project_id)
        posicion = (proyecto.get("session_count", 0) if proyecto else 0) + 1
        resp = _cliente().table("sessions").insert({
            "project_id": project_id,
            "user_id": DEV_USER_ID,
            "session_position": posicion,
            "tipo": tipo,
            "mensaje_entrada": mensaje_entrada,
            "puerta_entrada": puerta_entrada,
        }).execute()
        return resp.data[0]["id"]
    data = _cargar_local(project_id)
    session_id = uuid.uuid4().hex[:8]
    data["sessions"].append({
        "id": session_id,
        "session_position": len(data["sessions"]) + 1,
        "tipo": tipo,
        "mensaje_entrada": mensaje_entrada,
        "puerta_entrada": puerta_entrada,
        "ruta": [],
        "costo_usd": 0,
        "presupuesto_excedido": False,
        "created_at": _ahora(),
        "closed_at": None,
    })
    _guardar_local(project_id, data)
    return session_id


def cerrar_sesion(project_id, session_id, ruta_con_modos, costo_usd, presupuesto_excedido, costo_desglose=None):
    """ruta_con_modos: [{"node_id": str, "tipo": "conversado"|"silencioso"}].
    costo_desglose (Fase 2.7): {"clasificacion": float, "turnos": float,
    "plan": float, "estado_vivo": float, ...} - costo real por componente,
    ademas del total, para monitorear que componente crece con el tiempo.
    Requiere la columna sessions.costo_desglose (jsonb); ver
    supabase/migrations/my_idea_002_costo_desglose.sql. Si la columna aun
    no existe en el proyecto de Supabase, este update fallaria; en ese caso
    se reintenta sin costo_desglose para no romper el cierre de sesion."""
    if disponible():
        campos = {
            "ruta": ruta_con_modos,
            "costo_usd": costo_usd,
            "presupuesto_excedido": presupuesto_excedido,
            "closed_at": _ahora(),
        }
        if costo_desglose:
            campos["costo_desglose"] = costo_desglose
        try:
            _cliente().table("sessions").update(campos).eq("id", session_id).execute()
        except Exception:
            campos.pop("costo_desglose", None)
            _cliente().table("sessions").update(campos).eq("id", session_id).execute()
        proyecto = obtener_proyecto(project_id)
        nuevo_conteo = (proyecto.get("session_count", 0) if proyecto else 0) + 1
        actualizar_proyecto(project_id, session_count=nuevo_conteo)
        return
    data = _cargar_local(project_id)
    for s in data["sessions"]:
        if s["id"] == session_id:
            s["ruta"] = ruta_con_modos
            s["costo_usd"] = costo_usd
            s["presupuesto_excedido"] = presupuesto_excedido
            s["costo_desglose"] = costo_desglose or {}
            s["closed_at"] = _ahora()
    data["session_count"] = data.get("session_count", 0) + 1
    data["updated_at"] = _ahora()
    _guardar_local(project_id, data)


# ---------------------------------------------------------------------------
# Interfaz publica: nodos cubiertos por proyecto
# ---------------------------------------------------------------------------

def registrar_nodos(project_id, session_id, nodos_con_tipo):
    """nodos_con_tipo: [(node_id, tipo)], tipo en conversado|silencioso|cosechado.
    Ignora duplicados (un nodo cuenta una sola vez por proyecto)."""
    ya_cubiertos = nodos_cubiertos(project_id)
    nuevos = [(nid, tipo) for nid, tipo in nodos_con_tipo if nid not in ya_cubiertos]
    if not nuevos:
        return
    if disponible():
        filas = [{"project_id": project_id, "session_id": session_id, "node_id": nid, "tipo": tipo}
                  for nid, tipo in nuevos]
        _cliente().table("project_nodes").insert(filas).execute()
        return
    data = _cargar_local(project_id)
    for nid, tipo in nuevos:
        data["project_nodes"].append({"session_id": session_id, "node_id": nid, "tipo": tipo})
    _guardar_local(project_id, data)


def nodos_cubiertos(project_id):
    if disponible():
        resp = _cliente().table("project_nodes").select("node_id").eq("project_id", project_id).execute()
        return {row["node_id"] for row in resp.data}
    data = _cargar_local(project_id)
    if data is None:
        return set()
    return {row["node_id"] for row in data.get("project_nodes", [])}


def conteo_familias_cubiertas(project_id, families):
    cubiertos = nodos_cubiertos(project_id)
    conteo = {}
    for nid in cubiertos:
        fam = families.get(nid, "general")
        conteo[fam] = conteo.get(fam, 0) + 1
    return conteo


# ---------------------------------------------------------------------------
# Interfaz publica: planes
# ---------------------------------------------------------------------------

def guardar_plan(project_id, session_id, etiqueta, contenido_md, conceptos_usados, familias_cubiertas):
    if disponible():
        _cliente().table("plans").insert({
            "session_id": session_id,
            "user_id": DEV_USER_ID,
            "etiqueta": etiqueta,
            "contenido_md": contenido_md,
            "conceptos_usados": conceptos_usados,
            "familias_cubiertas": familias_cubiertas,
        }).execute()
        return
    data = _cargar_local(project_id)
    data["plans"].append({
        "session_id": session_id,
        "etiqueta": etiqueta,
        "contenido_md": contenido_md,
        "conceptos_usados": conceptos_usados,
        "familias_cubiertas": familias_cubiertas,
        "created_at": _ahora(),
    })
    _guardar_local(project_id, data)
