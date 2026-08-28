# -*- coding: utf-8 -*-
r"""vuelta99_tarea4_medir_fase04.py . VUELTA 99, TAREA 4: MEDIR EL ESTADO REAL DE
LA FASE 04_ENLACES. NO CAMBIA NINGUN ESTADO: es una medicion pura sobre
docs/plan/OPERACIONES.jsonl y docs/plan/04_ENLACES.md, tal como estan HOY.

QUE MIDE, LOS TRES PUNTOS DEL ENCARGO:
  (4.1) las diez operaciones de fase 04_ENLACES: id_op, orden, estado literal,
        depende_de, y cuales de esas dependencias NO estan en HECHA.
  (4.2) el contraste entre el campo estado y la evidencia: para cada una, un
        extracto de su nota (los primeros y los ultimos 300 caracteres, sin
        editar ni resumir con juicio) y si 04_ENLACES.md trae una seccion con
        su id en el titulo.
  (4.3) la cuenta EJECUTABLE HOY (cero dependencias vivas de OTRA fase) contra
        la que espera dependencias de otras fases, y de que fases.

MECANICA DE ROJO: si fase 04_ENLACES no trae exactamente 10 operaciones, o si
algun id_op de depende_de no existe en OPERACIONES.jsonl, NO SE IMPRIME NADA.

USO:
  python scripts/loop/vuelta99_tarea4_medir_fase04.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
ENLACES = os.path.join(RAIZ, "docs", "plan", "04_ENLACES.md")
FASE = "04_ENLACES"


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    ops = cargar(OPERACIONES)
    byid = {o["id_op"]: o for o in ops}
    fase04 = [o for o in ops if o.get("fase") == FASE]

    fallos = []
    if len(fase04) != 10:
        fallos.append("fase %s trae %d operaciones, se esperaban 10" % (FASE, len(fase04)))
    for o in fase04:
        for d in (o.get("depende_de") or []):
            if d not in byid:
                fallos.append("%s depende de %r, que no existe en OPERACIONES.jsonl"
                              % (o["id_op"], d))
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE IMPRIME NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    fase04 = sorted(fase04, key=lambda o: o.get("orden", 0))
    enlaces_txt = io.open(ENLACES, encoding="utf-8").read()

    print("=" * 100)
    print("MEDICION DEL ESTADO REAL DE LA FASE 04_ENLACES (vuelta 99, TAREA 4)")
    print("NINGUN ESTADO SE TOCA. Todo lo de abajo se lee de OPERACIONES.jsonl y 04_ENLACES.md tal como estan hoy.")
    print("=" * 100)

    print("\n--- (4.1) LAS DIEZ OPERACIONES ---\n")
    for o in fase04:
        dep = o.get("depende_de") or []
        no_hecha = [(d, byid[d].get("fase"), byid[d].get("estado")) for d in dep
                    if byid[d].get("estado") != "HECHA"]
        print("%-18s orden=%-2s estado=%-6s depende_de=%s"
              % (o["id_op"], o.get("orden"), o.get("estado"), dep or "[]"))
        if no_hecha:
            print("   NO HECHA: %s"
                  % ", ".join("%s (fase %s, estado %s)" % t for t in no_hecha))
        else:
            print("   NO HECHA: (ninguna; sin dependencias o todas HECHA)")

    print("\n--- (4.2) CAMPO ESTADO CONTRA LA EVIDENCIA DE SU NOTA Y DE 04_ENLACES.md ---\n")
    for o in fase04:
        nota = o.get("nota") or ""
        tiene_seccion = bool(re.search(r"^##.*`?%s`?" % re.escape(o["id_op"]), enlaces_txt, re.M))
        print("#" * 90)
        print("%s . estado=%s . nota=%d caracteres . seccion propia en 04_ENLACES.md: %s"
              % (o["id_op"], o.get("estado"), len(nota), "SI" if tiene_seccion else "no"))
        print("  nota, primeros 220: %s" % nota[:220].replace("\n", " "))
        print("  nota, ultimos 220:  %s" % nota[-220:].replace("\n", " "))
        print()

    print("--- (4.3) LA CUENTA: EJECUTABLE HOY CONTRA ESPERA OTRA FASE ---\n")
    ejecutables, esperan, hechas = [], [], []
    for o in fase04:
        if o.get("estado") == "HECHA":
            hechas.append(o["id_op"])
            continue
        dep = o.get("depende_de") or []
        fuera_viva = [d for d in dep if byid[d].get("fase") != FASE
                     and byid[d].get("estado") != "HECHA"]
        if fuera_viva:
            fases = sorted(set(byid[d].get("fase") for d in fuera_viva))
            esperan.append((o["id_op"], fuera_viva, fases))
        else:
            dentro_viva = [d for d in dep if byid[d].get("fase") == FASE
                          and byid[d].get("estado") != "HECHA"]
            ejecutables.append((o["id_op"], dentro_viva))

    print("YA HECHA (%d): %s" % (len(hechas), ", ".join(hechas) or "ninguna"))
    print()
    print("EJECUTABLE HOY, sin dependencia viva de OTRA fase (%d):" % len(ejecutables))
    for oid, dentro in ejecutables:
        if dentro:
            print("   %s (depende dentro de la propia fase de %s, no HECHA todavia)" % (oid, dentro))
        else:
            print("   %s (sin ninguna dependencia)" % oid)
    print()
    print("ESPERA DEPENDENCIA VIVA DE OTRA FASE (%d):" % len(esperan))
    for oid, fuera_viva, fases in esperan:
        print("   %s -> %s (fase(s) %s)" % (oid, fuera_viva, ", ".join(fases)))
    print()
    print("TOTAL: %d = %d hechas + %d ejecutables + %d que esperan"
          % (len(fase04), len(hechas), len(ejecutables), len(esperan)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
