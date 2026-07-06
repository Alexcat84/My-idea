# -*- coding: utf-8 -*-
"""
setup_dev_user.py - Crea (o encuentra) el usuario fijo de desarrollo (Fase 2.5)

El CLI no tiene login real: opera como un unico usuario de desarrollo cuyo
id se referencia en cada fila (user_id). Este script es idempotente: si el
usuario dev@my-idea.local ya existe, solo imprime su id.

Uso: python scripts/setup_dev_user.py
"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

BASE = Path(__file__).resolve().parent.parent
load_dotenv(BASE / ".env")

DEV_EMAIL = "dev@my-idea.local"
DEV_PASSWORD = "dev-local-only-not-a-real-account-0001"


def main():
    url = os.environ.get("SUPABASE_URL", "").strip()
    service_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "").strip()
    if not url or not service_key:
        print("ERROR: faltan SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY en .env")
        sys.exit(1)

    from supabase import create_client
    client = create_client(url, service_key)

    page = client.auth.admin.list_users()
    for u in page:
        if u.email == DEV_EMAIL:
            print(f"Ya existe. DEV_USER_ID={u.id}")
            return

    resp = client.auth.admin.create_user({
        "email": DEV_EMAIL,
        "password": DEV_PASSWORD,
        "email_confirm": True,
    })
    print(f"Creado. DEV_USER_ID={resp.user.id}")


if __name__ == "__main__":
    main()
