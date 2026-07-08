# -*- coding: utf-8 -*-
"""
check_migrations.py - Checklist de TODAS las migraciones de Supabase
aplicadas (my_idea).

Compara supabase/migrations/my_idea_NNN_*.sql (lo que existe en el repo)
contra el estado REAL del proyecto de Supabase (via la funcion RPC de
solo lectura introspeccion_schema(), ver
supabase/migrations/my_idea_fn_introspeccion_schema.sql -- esa funcion
vive en el mismo directorio pero deliberadamente SIN numero: es
infraestructura de este check, no una migracion de esquema mas), y
muestra:
  [OK]      la migracion ya esta aplicada
  [FALTA]   la migracion existe en el repo pero el cambio no esta en la DB
  [SIN CHK] el archivo de migracion no tiene un chequeo registrado aqui
            (agregar una entrada en MIGRACIONES la proxima vez)

Convencion de este proyecto: cada vez que se crea una migracion nueva,
se agrega TAMBIEN su entrada en MIGRACIONES (abajo) en el mismo commit --
asi este script se mantiene al dia sin depender de parsear SQL arbitrario.

Uso: python scripts/check_migrations.py
"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

BASE = Path(__file__).resolve().parent.parent
load_dotenv(BASE / ".env")

MIGRATIONS_DIR = BASE / "supabase" / "migrations"


def _tiene_columna(ctx, tabla, columna):
    return any(c["tabla"] == tabla and c["columna"] == columna for c in ctx["columnas"])


def _tiene_tabla(ctx, tabla):
    return any(c["tabla"] == tabla for c in ctx["columnas"])


def _constraint_contiene(ctx, nombre, fragmento):
    definicion = ctx["constraints"].get(nombre)
    return definicion is not None and fragmento in definicion


def _funcion_bloqueada_para_publico(ctx, nombre):
    f = ctx["funciones"].get(nombre)
    if f is None:
        return False
    return not f.get("anon_execute", True) and not f.get("authenticated_execute", True)


# Registro declarativo: un chequeo por migracion, en el mismo orden que se
# aplicaron. Actualizar esta lista cada vez que se agrega una migracion.
MIGRACIONES = [
    {
        "archivo": "my_idea_001_init.sql",
        "descripcion": "Esquema inicial: projects/sessions/project_nodes/plans/query_credits + RLS",
        "check": lambda ctx: all(
            _tiene_columna(ctx, tabla, columna)
            for tabla, columna in [
                ("projects", "id"), ("projects", "user_id"), ("projects", "fase_actual"),
                ("sessions", "id"), ("sessions", "tipo"), ("sessions", "ruta"),
                ("project_nodes", "id"),
                ("plans", "id"), ("plans", "etiqueta"),
                ("query_credits", "id"),
            ]
        ),
    },
    {
        "archivo": "my_idea_002_costo_desglose.sql",
        "descripcion": "sessions.costo_desglose (JSONB)",
        "check": lambda ctx: _tiene_columna(ctx, "sessions", "costo_desglose"),
    },
    {
        "archivo": "my_idea_003_numeros.sql",
        "descripcion": "projects.numeros_proyecto (JSONB)",
        "check": lambda ctx: _tiene_columna(ctx, "projects", "numeros_proyecto"),
    },
    {
        "archivo": "my_idea_004_reporte_tipo.sql",
        "descripcion": "sessions_tipo_check permite 'reporte'",
        "check": lambda ctx: _constraint_contiene(ctx, "sessions_tipo_check", "reporte"),
    },
    {
        "archivo": "my_idea_005_reporte_etiqueta.sql",
        "descripcion": "plans_etiqueta_check permite 'reporte_numeros'",
        "check": lambda ctx: _constraint_contiene(ctx, "plans_etiqueta_check", "reporte_numeros"),
    },
    {
        "archivo": "my_idea_006_revoke_rls_auto_enable.sql",
        "descripcion": "rls_auto_enable() sin EXECUTE para anon/authenticated",
        "check": lambda ctx: _funcion_bloqueada_para_publico(ctx, "rls_auto_enable"),
    },
    {
        "archivo": "my_idea_007_tipo_oferta.sql",
        "descripcion": "projects.tipo_oferta / unidad_venta / numeros_descartados",
        "check": lambda ctx: all(
            _tiene_columna(ctx, "projects", c) for c in ("tipo_oferta", "unidad_venta", "numeros_descartados")
        ),
    },
    {
        "archivo": "my_idea_008_beta_allowlist.sql",
        "descripcion": "tabla beta_allowlist",
        "check": lambda ctx: _tiene_tabla(ctx, "beta_allowlist"),
    },
    {
        "archivo": "my_idea_009_estado_recorrido.sql",
        "descripcion": "sessions.estado_recorrido (JSONB)",
        "check": lambda ctx: _tiene_columna(ctx, "sessions", "estado_recorrido"),
    },
    {
        "archivo": "my_idea_010_estado_reporte.sql",
        "descripcion": "projects.estado_reporte (JSONB)",
        "check": lambda ctx: _tiene_columna(ctx, "projects", "estado_reporte"),
    },
]


def _archivos_migracion_en_repo():
    # my_idea_[0-9]*.sql = solo las migraciones numeradas de la secuencia;
    # my_idea_fn_introspeccion_schema.sql vive en el mismo directorio pero
    # a proposito no tiene numero (es la funcion que este script usa, no
    # una migracion de esquema mas) y no debe listarse como "sin chequeo".
    return sorted(p.name for p in MIGRATIONS_DIR.glob("my_idea_[0-9]*.sql"))


def main():
    url = os.environ.get("SUPABASE_URL", "").strip()
    service_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "").strip()
    if not url or not service_key:
        print("ERROR: faltan SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY en .env")
        sys.exit(1)

    from supabase import create_client
    client = create_client(url, service_key)

    try:
        resp = client.rpc("introspeccion_schema").execute()
        ctx = resp.data
    except Exception as e:
        print("ERROR: no se pudo llamar a introspeccion_schema().")
        print(f"  {e}")
        print("\n  Esto casi siempre significa que la funcion de introspeccion (no es una")
        print("  migracion numerada, es infraestructura de este mismo check) todavia no")
        print("  esta aplicada. Aplicala primero en el SQL Editor de Supabase:")
        print("  supabase/migrations/my_idea_fn_introspeccion_schema.sql")
        sys.exit(1)

    archivos_repo = _archivos_migracion_en_repo()
    registradas = {m["archivo"] for m in MIGRACIONES}
    orden = {archivo: i for i, archivo in enumerate(archivos_repo)}
    MIGRACIONES.sort(key=lambda m: orden.get(m["archivo"], len(orden)))

    print("=" * 72)
    print("  Checklist de TODAS las migraciones de Supabase (my_idea)")
    print("=" * 72)
    print("  [OK   ] funcion de introspeccion disponible (my_idea_fn_introspeccion_schema.sql)")

    faltan = []
    sin_chequeo = []

    for m in MIGRACIONES:
        if m["archivo"] not in orden:
            # Registrada aqui pero el archivo ya no existe en el repo -- no debería
            # pasar en uso normal, pero se avisa en vez de fallar en silencio.
            print(f"  [???]   {m['archivo']} -- registrada aqui pero no existe en supabase/migrations/")
            continue
        try:
            aplicada = bool(m["check"](ctx))
        except Exception as e:
            print(f"  [ERROR] {m['archivo']} -- fallo el chequeo: {e}")
            faltan.append(m["archivo"])
            continue
        estado = "OK   " if aplicada else "FALTA"
        print(f"  [{estado}] {m['archivo']:<45} {m['descripcion']}")
        if not aplicada:
            faltan.append(m["archivo"])

    for archivo in archivos_repo:
        if archivo not in registradas:
            sin_chequeo.append(archivo)
            print(f"  [SIN CHK] {archivo:<43} sin chequeo registrado en este script")

    print("=" * 72)
    if not faltan and not sin_chequeo:
        print("  Todo al dia: todas las migraciones registradas estan aplicadas.")
        sys.exit(0)

    if faltan:
        print(f"  Faltan {len(faltan)} migracion(es) por aplicar (SQL Editor de Supabase):")
        for f in faltan:
            print(f"    - {f}")
    if sin_chequeo:
        print(f"  {len(sin_chequeo)} archivo(s) nuevo(s) sin chequeo registrado en scripts/check_migrations.py:")
        for f in sin_chequeo:
            print(f"    - {f}")
    sys.exit(1)


if __name__ == "__main__":
    main()
