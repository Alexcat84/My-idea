# -*- coding: utf-8 -*-
r"""vuelta144_3b_sellar_mesa_opm04.py . SELLA EL PLAN DE UNA MESA DE **DOS
FUSIONES**, que es la figura que `OP-M-04` declara en su propio `tipo`.

POR QUE NACE UN INSTRUMENTO NUEVO, MEDIDO Y NO SUPUESTO. El sellador de la casa,
`scripts/loop/generar_plan_de_fusion_de_mesa.py`, NO PUEDE sellar esta mesa, y
lo dice su propio codigo con tres guardas que estan BIEN PUESTAS:

    if spec.get("superviviente") != sup: fallos.append(...)
    if sorted(spec.get("absorbidos") or []) != sorted(absorbidos): fallos.append(...)
    if sorted(miembros) != sorted([sup] + absorbidos): fallos.append(...)

Da por supuesto UN superviviente por ficha. `OP-M-04` tiene DOS, y su campo
`superviviente` no es un id de nodo sino la frase
"identificar_consejo_asesores (fusion 367) y formalizar_junta_asesora (fusion
328)". Corrido tal cual, el generador cae en las tres guardas y no escribe nada,
que es lo correcto: NO SE RELAJA NINGUNA. Se escribe el instrumento que la
figura pide, exactamente como la vuelta 143 escribio el del giro en vez de
relajar las guardas del retirador y del escritor.

LA MAQUINA NO SE RETECLEA NI SE COPIA: se IMPORTA del generador de la casa
(`marcar`, `reparto_por_par`, `validar_viaja_en_el_acto`, `puertas`,
`CLAVES_DE_PERDIDA`, `ESPECIES_DE_PERDIDA`, `ficha`), para que el que sella una
mesa de una fusion y el que sella una mesa de dos no puedan discrepar en
silencio. Lo unico propio de este fichero es EL REPARTO DE LA FICHA EN DOS ACTOS
y las guardas que ese reparto necesita.

LAS GUARDAS PROPIAS, todas con su salida impresa, y si UNA cae no se escribe
nada:
  (1) LA FICHA DECLARA SU FIGURA en su propio `tipo`, con la frase literal que
      `tallar_estado_de_fase.py` cita desde la TAREA 3.a de esta vuelta. Si no
      la declara, ROJO: este instrumento es SOLO para esa figura.
  (2) LOS DOS SUPERVIVIENTES SALEN DE LA FICHA, cruzando su campo
      `superviviente` con su campo `nodos`. Tienen que ser EXACTAMENTE DOS.
  (3) LOS DOS ABSORBIDOS SALEN DE `eliminar`, y `nodos` tiene que ser
      exactamente la union de supervivientes y absorbidos, sin sobras ni faltas.
  (4) CADA CONTENIDO NOMBRA UN SUPERVIVIENTE DE LA FICHA Y UN ABSORBIDO DE LA
      FICHA, y entre los dos contenidos cubren los dos y los dos, sin repetir.
  (5) EL EMPAREJAMIENTO SE COTEJA CONTRA LA FICHA Y NO SE ACEPTA DEL CONTENIDO:
      la ficha declara, en una linea de `verificacion`, con que alias queda cada
      superviviente; se parsea con la MISMA funcion que la mutacion de la 3.a
      (`vuelta144_3a_mutaciones.emparejamiento_declarado_de`, importada) y si el
      reparto del contenido no coincide con el de la ficha, ROJO nombrando los
      dos.
  (6) GUARDA 1B, la del generador: ningun absorbido es semilla de entrada ni
      extremo de puente.
  (7) LOS CUATRO MIEMBROS VIVOS Y NO DEPRECADOS hoy.
  (8) COBERTURA EXACTA por absorbido, que la pone `marcar` del generador: cada
      paso y cada condicion con marca UNICA, ni una de menos ni una de mas.
  (9) LAS PERDIDAS con sus cuatro claves y su especie dentro del contrato.

--- LA FRONTERA DE LOS DOS SELLADORES, ESCRITA (VUELTA 145, TAREA 2.e; acta
144, adjudicacion 3.2, que responde la PREGUNTA 2 del reporte de la 144) ---

NO HAY DOS CAMINOS PARA LO MISMO: HAY DOS FIGURAS.

  - `generar_plan_de_fusion_de_mesa.py` (el de la casa) sella UNA FUSION CON
    UN SUPERVIVIENTE. Su nombre no lleva vuelta ni operacion a proposito: la
    vuelta, la operacion y el contenido entran por argumento, y sirve para
    cualquier ficha de esa figura, hoy y dentro de veinte vueltas.
  - `vuelta144_3b_sellar_mesa_opm04.py` sella UNA MESA DE DOS ACTOS: DOS
    supervivientes, DOS absorbidos y un reparto que la ficha declara. Lleva la
    vuelta y la operacion en el nombre porque hoy hay UNA sola ficha con esa
    figura; el dia que haya una segunda, el instrumento se generaliza como se
    generalizo el de la casa.

QUE DECIDE CUAL SE USA: LA FIGURA QUE LA FICHA DECLARA EN SU PROPIO `tipo`,
leida con `tallar_estado_de_fase.figura_declarada_de`, nunca el gusto de quien
sella. La ficha que no declara la figura de dos actos NO entra en el sellador
de dos actos, y su guarda 1 la rechaza.

Y POR QUE NO SE RELAJO EL DE LA CASA, que seria el otro camino: sus tres
guardas de superviviente unico estan BIEN PUESTAS, y relajarlas para que
tragaran dos supervivientes las habria dejado ciegas para las fichas de UNA
fusion, que son la inmensa mayoria. Se importo su maquina entera en vez de
copiarla, asi que los dos no pueden discrepar en silencio.

DE ESCRITURA SOLO SOBRE docs/loop/PLAN_V144_OPM04.json. No toca ni un nodo.

Uso:
  python scripts/loop/vuelta144_3b_sellar_mesa_opm04.py [--simular]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
sys.path.insert(0, LOOP)

import generar_plan_de_fusion_de_mesa as G  # noqa: E402
import vuelta144_3a_mutaciones as M  # noqa: E402
import _v144_opm04_367 as C367  # noqa: E402
import _v144_opm04_328 as C328  # noqa: E402

ID_OP = "OP-M-04"
DESTINO = os.path.join(RAIZ, "docs", "loop", "PLAN_V144_OPM04.json")
VUELTA = 144


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    op = G.ficha(ID_OP)
    if op is None:
        print("ROJO: %s no esta en docs/plan/OPERACIONES.jsonl. PARADA." % ID_OP)
        return 1

    print("=" * 78)
    print("SELLADOR DEL PLAN DE LA MESA DE DOS FUSIONES %s (vuelta %d)" % (ID_OP, VUELTA))
    print("  ficha leida de: docs/plan/OPERACIONES.jsonl")
    print("  tipo: %s" % op.get("tipo"))
    print("  estado: %s | fecha de corte: %s" % (op.get("estado"), op.get("fecha_corte")))
    print("=" * 78)
    print()

    fallos = []

    # ---- (1) LA FICHA DECLARA SU FIGURA -----------------------------------
    import tallar_estado_de_fase as T
    figura = T.figura_declarada_de(op)
    print("  guarda 1, la ficha declara su figura en su `tipo`: %s"
          % ("OK (%r)" % figura if figura else "ROJO"))
    if figura is None:
        fallos.append("la ficha no declara la figura %r en su `tipo`: este sellador es SOLO "
                      "para esa figura" % T.FRASE_FIGURA_DOS_FUSIONES_UN_ENLACE)

    if op.get("estado") != "LISTA":
        fallos.append("la ficha dice estado %r y no LISTA" % op.get("estado"))

    # ---- (2) y (3) LOS DOS SUPERVIVIENTES Y LOS DOS ABSORBIDOS ------------
    sups = T._supervivientes_de(op)
    absorbidos = list(op.get("eliminar") or [])
    miembros = list(op.get("nodos") or [])
    print("  LA FICHA MANDA, y esto es lo que dice:")
    print("     nodos          : %s" % ", ".join(miembros))
    print("     superviviente  : %s" % op.get("superviviente"))
    print("     supervivientes leidos del cruce con `nodos`: %s" % ", ".join(sups))
    print("     eliminar       : %s" % ", ".join(absorbidos))
    if len(sups) != 2:
        fallos.append("la ficha nombra %d supervivientes y la figura pide DOS" % len(sups))
    if len(absorbidos) != 2:
        fallos.append("la ficha nombra %d eliminados y la figura pide DOS" % len(absorbidos))
    if sorted(miembros) != sorted(sups + absorbidos):
        fallos.append("`nodos` no es la union exacta de supervivientes y eliminados")
    print("  guarda 2 y 3, dos supervivientes, dos absorbidos y nodos = union: %s"
          % ("ROJO" if fallos else "OK"))

    # ---- (4) CADA CONTENIDO NOMBRA LO SUYO --------------------------------
    contenidos = [C367.FUSION, C328.FUSION]
    sup_c = [c.get("superviviente") for c in contenidos]
    abs_c = [x for c in contenidos for x in (c.get("absorbidos") or [])]
    if sorted(sup_c) != sorted(sups):
        fallos.append("los contenidos dicen supervivientes %r y la ficha dice %r"
                      % (sorted(sup_c), sorted(sups)))
    if sorted(abs_c) != sorted(absorbidos):
        fallos.append("los contenidos dicen absorbidos %r y la ficha dice %r"
                      % (sorted(abs_c), sorted(absorbidos)))
    if len(set(sup_c)) != len(sup_c) or len(set(abs_c)) != len(abs_c):
        fallos.append("dos contenidos nombran el mismo superviviente o el mismo absorbido")
    print("  guarda 4, los contenidos cubren los dos y los dos sin repetir: %s"
          % ("ROJO" if sorted(sup_c) != sorted(sups) or sorted(abs_c) != sorted(absorbidos)
             else "OK"))

    # ---- (5) EL EMPAREJAMIENTO SALE DE LA FICHA ---------------------------
    reparto_ficha, linea_reparto = M.emparejamiento_declarado_de(op)
    if reparto_ficha is None:
        fallos.append("la ficha no declara su reparto de absorbidos de forma legible: no se "
                      "adivina que absorbido va con que superviviente")
    else:
        reparto_contenido = {c["superviviente"]: sorted(c["absorbidos"]) for c in contenidos}
        reparto_ficha_ord = {k: sorted(v) for k, v in reparto_ficha.items()}
        if reparto_contenido != reparto_ficha_ord:
            fallos.append("el emparejamiento del contenido %r NO es el que la ficha declara %r"
                          % (reparto_contenido, reparto_ficha_ord))
        print("  guarda 5, el emparejamiento del contenido calza con el de la ficha: %s"
              % ("OK" if reparto_contenido == reparto_ficha_ord else "ROJO"))
        for s in sorted(reparto_ficha_ord):
            print("     %s absorbe %s" % (s, ", ".join(reparto_ficha_ord[s])))
        print("     leido de: %s" % (linea_reparto or "")[:100])

    # ---- (6) GUARDA 1B ----------------------------------------------------
    prot = G.puertas()
    for x in absorbidos:
        if x in prot:
            fallos.append("GUARDA 1B EN ROJO: el absorbido %s es semilla o extremo de puente" % x)
    print("  guarda 6 (1B), ningun absorbido es puerta: %s"
          % ("ROJO" if any(x in prot for x in absorbidos) else "OK"))

    # ---- (7) LOS CUATRO VIVOS --------------------------------------------
    nodos = {}
    for x in miembros:
        p = os.path.join(NODOS, x + ".json")
        if not os.path.exists(p):
            fallos.append("el nodo %s no existe en el catalogo" % x)
            continue
        nodos[x] = json.load(io.open(p, encoding="utf-8"))
        if nodos[x].get("deprecado") or nodos[x].get("deprecated"):
            fallos.append("el nodo %s YA esta deprecado" % x)
    print("  guarda 7, los %d miembros vivos y presentes: %s"
          % (len(miembros), "OK" if len(nodos) == len(miembros) else "ROJO"))

    if fallos:
        print()
        print("ROJO, %d fallo(s) y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    # ---- (8) LAS MARCAS, con la maquina del generador ---------------------
    actos = []
    for orden, spec in enumerate(contenidos, 1):
        sup = spec["superviviente"]
        abs_ = list(spec["absorbidos"])
        pasos_sup = list(nodos[sup].get("pasos_accionables") or [])
        cond_sup = list(nodos[sup].get("condiciones_activacion") or [])
        print()
        print("  ---- ACTO %d: %s absorbe %s ----" % (orden, sup, ", ".join(abs_)))
        print("     EL SUPERVIVIENTE DE HOY: %d pasos y %d condiciones"
              % (len(pasos_sup), len(cond_sup)))
        spec_p, formato_p = G.reparto_por_par(spec, "pasos", abs_, fallos)
        spec_c, formato_c = G.reparto_por_par(spec, "condiciones", abs_, fallos)
        print("     FORMATO DEL REPARTO: pasos %s | condiciones %s" % (formato_p, formato_c))
        marcas_p, marcas_c, pasos_por_ab = {}, {}, {}
        for ab in abs_:
            pa = list(nodos[ab].get("pasos_accionables") or [])
            ca = list(nodos[ab].get("condiciones_activacion") or [])
            pasos_por_ab[ab] = pa
            print("     EL ABSORBIDO %s: %d pasos y %d condiciones" % (ab, len(pa), len(ca)))
            marcas_p[ab] = G.marcar(spec_p.get(ab) or {}, pa, "paso", ab, len(pasos_sup),
                                    len(cond_sup), pasos_sup, fallos, permite_cond=True)
            marcas_c[ab] = G.marcar(spec_c.get(ab) or {}, ca, "condicion", ab, len(pasos_sup),
                                    len(cond_sup), pasos_sup, fallos, permite_cond=False)
        G.validar_viaja_en_el_acto(marcas_p, abs_, pasos_por_ab,
                                   spec.get("lineas_de_viaje") or {}, fallos)

        # ---- (9) LAS PERDIDAS ---------------------------------------------
        for p_ in (spec.get("perdidas") or []):
            faltan = [k for k in G.CLAVES_DE_PERDIDA if k not in p_]
            if faltan:
                fallos.append("a una perdida de %s le faltan las claves %s"
                              % (sup, ", ".join(faltan)))
            elif p_["especie"] not in G.ESPECIES_DE_PERDIDA:
                fallos.append("especie de perdida desconocida %r en %s. Las escritas son: %s"
                              % (p_["especie"], sup, ", ".join(G.ESPECIES_DE_PERDIDA)))
        print("     perdidas selladas: %d" % len(spec.get("perdidas") or []))

        actos.append({
            "orden": orden,
            "miembros": [sup] + abs_,
            "miembros_del_acto_entero": miembros,
            "figura": ("FUSION DE MESA, una de las DOS de %s. La ficha declara la figura "
                       "entera en su `tipo`: %r" % (ID_OP, op.get("tipo"))),
            "superviviente": sup,
            "absorbidos": abs_,
            "motivo": spec.get("motivo"),
            "pasos": marcas_p,
            "condiciones": marcas_c,
            "nota_del_reparto": spec.get("nota"),
            "perdidas": list(spec.get("perdidas") or []),
            "simulacion_de_hoy": spec.get("simulacion_de_hoy"),
            "rotulo_del_acto": spec.get("titulo"),
        })

    if fallos:
        print()
        print("ROJO, %d fallo(s) y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    plan = {
        "operacion": ID_OP,
        "rotulo": ("LA MESA DE LA JUNTA ASESORA: DOS FUSIONES MAS UN ENLACE. La 367 "
                   "(identificar_consejo_asesores absorbe identificar_junta_asesores) y la "
                   "328 (formalizar_junta_asesora absorbe formalize_advisory_board). EL "
                   "GIRO DE LA ARISTA NO VA EN ESTE PLAN: es una operacion aparte y la "
                   "hace scripts/loop/vuelta143_3c_girar_arista.py, con sus diez guardas"),
        "fecha": op.get("fecha_corte"),
        "estado": "SELLADO",
        "contrato_de_perdidas": "CAMPO PROPIO v1",
        "vuelta": VUELTA,
        "tramo": "NO ES UN TRAMO: son las DOS fusiones de la mesa %s" % ID_OP,
        "ficha_tipo": op.get("tipo"),
        "ficha_fecha_corte": op.get("fecha_corte"),
        "ficha_adjudicacion": op.get("adjudicacion"),
        "ficha_preservar": op.get("preservar"),
        "ficha_verificacion": op.get("verificacion"),
        "ficha_evidencia": op.get("evidencia"),
        "ficha_nota": op.get("nota"),
        "ficha_depende_de": op.get("depende_de"),
        "ficha_bloquea_a": op.get("bloquea_a"),
        "sellado_por": ("scripts/loop/vuelta144_3b_sellar_mesa_opm04.py, instrumento nuevo "
                        "de la vuelta 144: el generador de la casa da por supuesto UN "
                        "superviviente por ficha y esta mesa tiene DOS. NO SE RELAJO "
                        "NINGUNA GUARDA DEL GENERADOR: su maquina se IMPORTA entera "
                        "(marcar, reparto_por_par, validar_viaja_en_el_acto, puertas, "
                        "CLAVES_DE_PERDIDA, ESPECIES_DE_PERDIDA, ficha) y lo unico propio "
                        "es el reparto en dos actos y sus cinco guardas nuevas"),
        "emparejamiento_leido_de_la_ficha": linea_reparto,
        "actos": actos,
        "declarados_y_no_fundidos": [],
        "colisiones_esperadas": (
            "DOS DUPLICADAS NUEVAS, medidas en la simulacion previa del 2 sep 2026 "
            "(docs/loop/SALIDA_V144_3B_SIMULACION.txt): "
            "customer_discovery.nodos_siguientes -> formalizar_junta_asesora y "
            "verificar_product_market_fit.nodos_previos -> identificar_consejo_asesores. "
            "LAS DOS ESTAN PREDICHAS POR LA PROPIA FICHA en su `nota` y quedan para "
            "OP-S-12, que corre AL FINAL de la pasada entera por la atadura 2 del indice."),
        "vara_de_las_puertas": ("dataset/metadata/entry_seeds.json mas los entry_seeds y "
                                "bridges_aprobados de packs/, leidos al sellar"),
        "varas_impresas": ("las nueve guardas de este sellador van impresas arriba con su "
                           "veredicto, y la aritmetica de las marcas es la del generador de "
                           "la casa, importada y no copiada"),
    }

    if a.simular:
        print()
        print("SIMULACION: el plan NO se escribe. Estas son sus cifras:")
        print("  actos: %d | miembros: %d | perdidas selladas: %d"
              % (len(actos), len(miembros),
                 sum(len(x["perdidas"]) for x in actos)))
        print("FIN")
        return 0

    io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(
        json.dumps(plan, ensure_ascii=False, indent=1) + "\n")
    print()
    print("SELLADO: %s" % os.path.relpath(DESTINO, RAIZ))
    print("  actos: %d | miembros: %d | perdidas selladas: %d"
          % (len(actos), len(miembros), sum(len(x["perdidas"]) for x in actos)))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
