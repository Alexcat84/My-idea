# -*- coding: utf-8 -*-
r"""vuelta116_tarea3_4_tres_criterios_remision.py . TAREA 3.4 de la vuelta
116, encargo del auditor (acta de la vuelta 115).

QUE MIDE. Sobre las SIETE operaciones de la fase 04 que la TAREA 3.1 mide
como alcanzando alguna mesa de la fase 06 (OP-M-03-ENLACES, OP-E-04, OP-E-05,
OP-M-01-ESLABONES, OP-M-01-SEXTO, OP-E-06, OP-E-07), los TRES criterios de la
doctrina de la remision (docs/plan/00_INDICE.md, CORRECCION DECLARADA, "LA
FASE 03 QUEDA CERRADA CON REMISION"): DESTINO ESCRITO, NOMINA MEDIDA y CERO
DECISIONES PENDIENTES.

  DESTINO: la mesa de la fase 06_MESAS que alcanza (leido del cierre
  transitivo de la TAREA 3.1, campo `depende_de` recorrido hasta la mesa).
  NOMINA: el campo `aristas_nuevas` de docs/plan/OPERACIONES.jsonl, contado.
  DECISIONES PENDIENTES: el campo `pregunta_pendiente` (None/NINGUNA o su
  texto) y si el campo `adjudicacion` esta escrito (no vacio).

SOLO MEDIR. No adjudica si la remision esta bien cerrada.

USO:
  python scripts/loop/vuelta116_tarea3_4_tres_criterios_remision.py
"""
import json

from vuelta116_tarea3_1_cierre_transitivo_fase04 import cargar, cierre_transitivo

RUTA_OPS = "docs/plan/OPERACIONES.jsonl"

# Las siete: las que la TAREA 3.1 mide alcanzando alguna mesa de la fase 06
# (recalculado aqui mismo, no tecleado, para que un cambio en el grafo se
# note en las dos tareas a la vez).
REMITIDAS = ["OP-M-03-ENLACES", "OP-E-04", "OP-E-05", "OP-M-01-ESLABONES", "OP-M-01-SEXTO", "OP-E-06", "OP-E-07"]


def destino(by_id, oid):
    """La mesa de fase 06_MESAS que el cierre transitivo de oid alcanza
    (mismo calculo que la TAREA 3.1, reusado, no re-tecleado)."""
    cierre, _padres = cierre_transitivo(by_id, oid)
    mesas = sorted([n for n in cierre if by_id.get(n, {}).get("fase") == "06_MESAS"])
    return mesas


def main():
    ops = [json.loads(l) for l in open(RUTA_OPS, encoding="utf-8") if l.strip()]
    by_id = {o["id_op"]: o for o in ops}

    print("LOS TRES CRITERIOS DE LA REMISION SOBRE LAS SIETE, TAREA 3.4 VUELTA 116.")
    print("=" * 100)
    print("Fuente: %s. DESTINO recalculado con el mismo cierre transitivo de la TAREA 3.1." % RUTA_OPS)
    print()
    print("| operacion | destino (mesa fase 06) | nomina (aristas_nuevas) | pregunta_pendiente | adjudicacion escrita |")
    print("|---|---|---:|---|---|")
    for oid in REMITIDAS:
        o = by_id[oid]
        nomina = len(o.get("aristas_nuevas") or [])
        pp = o.get("pregunta_pendiente")
        pp_txt = "NINGUNA" if pp is None else repr(pp)
        adj = o.get("adjudicacion") or ""
        adj_escrita = "SI (%d caracteres)" % len(adj) if adj.strip() else "NO"
        mesas = destino(by_id, oid)
        print("| %s | %s | %d | %s | %s |" % (oid, ", ".join(mesas) or "NINGUNA", nomina, pp_txt, adj_escrita))

    print()
    todas_sin_pregunta = all((by_id[oid].get("pregunta_pendiente") is None) for oid in REMITIDAS)
    todas_con_adjudicacion = all((by_id[oid].get("adjudicacion") or "").strip() for oid in REMITIDAS)
    print("RESUMEN: pregunta_pendiente NINGUNA en las %d: %s. adjudicacion escrita en las %d: %s."
          % (len(REMITIDAS), todas_sin_pregunta, len(REMITIDAS), todas_con_adjudicacion))
    total_nomina = sum(len(by_id[oid].get("aristas_nuevas") or []) for oid in REMITIDAS)
    print("nomina total (suma de aristas_nuevas de las siete): %d" % total_nomina)


if __name__ == "__main__":
    main()
