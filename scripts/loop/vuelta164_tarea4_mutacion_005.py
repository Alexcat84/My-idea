# -*- coding: utf-8 -*-
r"""vuelta164_tarea4_mutacion_005.py . ARNES DE MUTACION DE LA PARTE MECANICA DE
LAS TAREAS 3 Y 4 DE LA VUELTA 164.

QUE PRUEBA, Y QUE NO. NO prueba el veredicto: la clasificacion de un paso como
"procedimiento propio" o como "orden mas complemento" es lectura del ejecutor y
por `EJECUTOR.md` regla 1 SE DECLARA QUE NO HAY CASO ROJO AUTOMATICO PARA ESO.
Prueba TODO LO QUE SI ES MECANICO y que, si se moviera, dejaria el veredicto
apoyado en una medicion falsa:

  (A) la vara leida del banco: la frase y sus CUATRO ejemplares;
  (B) los dos nodos del par en disputa, leidos del grafo;
  (C) la arista en las cuatro vistas;
  (D) el solape lexico del par que la vuelta 157 declaro COLAPSADO;
  (E) el barrido: cuantos pasos tiene cada nodo y que forma tienen;
  (F) el cruce de entregables y su calibracion contra los cuatro ejemplares;
  (G) el estado del registro DESPUES de las TAREAS 3 y 4, medido como DELTA
      contra lo que el acta 163 midio al abrir la vuelta, no como estado
      clavado (la medicina de `162_1a`).

SUJETO: el grafo, el banco y el registro de HOY, mas listas fabricadas en
memoria. CERO escrituras.

USO:  python scripts/loop/vuelta164_tarea4_mutacion_005.py
"""
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))

import vuelta163_tarea1b_relectura_101 as B      # noqa: E402
import vuelta164_tarea4_dossier_005 as T4        # noqa: E402

# LO QUE EL ACTA 163 MIDIO AL ABRIR ESTA VUELTA, escrito aqui como PUNTO DE
# PARTIDA de los deltas y no como esperado del estado de hoy. Si el estado se
# clavara, este arnes caducaria en cuanto otra vuelta moviera una clase.
REGISTRO_AL_ABRIR = {"filas": 154, "LECTURA_DIRIGIDA_C": 14, "LECTURA_DIRIGIDA_D": 108}
# LAS DOS QUE ESTA VUELTA TOCA, y lo que hace con cada una.
TOCADAS = {"LD-OPC05-101": "D", "LD-OPC05-005": "D"}
MARCA_164 = "RELECTURA CONJUNTA DE LA VUELTA 164"


def clases_del_registro():
    c = {"LECTURA_DIRIGIDA_C": 0, "LECTURA_DIRIGIDA_D": 0, "filas": 0}
    for l in io.open(os.path.join(RAIZ, "docs", "plan",
                                  "REGISTRO_DE_CITAS_OPC05.jsonl"), encoding="utf-8"):
        l = l.strip()
        if not l:
            continue
        d = json.loads(l)
        c["filas"] += 1
        if d.get("via") == "LECTURA_DIRIGIDA":
            k = "LECTURA_DIRIGIDA_%s" % d.get("clase")
            if k in c:
                c[k] += 1
    return c


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 164, TAREAS 3 Y 4: CASO POSITIVO POR MUTACION DE LO MECANICO")
    print("=" * 78)
    print("")
    casos = []

    g = B.cargar_grafo()
    _i, _f, frase, ejemplares = B.vara_de_hoy()
    filas = B.filas_del_registro()

    # --- (A) LA VARA ---
    casos.append(("A_la_vara_trae_cuatro_ejemplares", len(ejemplares), 4))
    casos.append(("A_los_cuatro_son_esos",
                  sorted(e[0] for e in ejemplares),
                  ["LD-OPC05-052", "LD-OPC05-095", "LD-OPC05-100", "LD-OPC05-122"]))
    casos.append(("A_dos_ACEPTAN_y_dos_EXCLUYEN",
                  sorted(e[1] for e in ejemplares),
                  ["ACEPTA", "ACEPTA", "EXCLUYE", "EXCLUYE"]))
    casos.append(("A_la_frase_dice_procedimiento_propio",
                  "PROCEDIMIENTO PROPIO" in frase.upper(), True))
    casos.append(("A_y_dice_no_solo_el_nombre_de_otro",
                  "NOMBRE DE OTRO" in frase.upper(), True))

    # --- (B) LOS DOS NODOS DEL PAR EN DISPUTA ---
    casos.append(("B_aim_of_leadership_tiene_SEIS_pasos",
                  len(g[T4.NODO_A]["pasos_accionables"]), 6))
    casos.append(("B_causas_comunes_tiene_QUINCE_pasos",
                  len(g[T4.NODO_B]["pasos_accionables"]), 15))
    casos.append(("B_el_paso_13_es_el_de_las_tolerancias",
                  "tolerancias" in g[T4.NODO_B]["pasos_accionables"][12], True))
    casos.append(("B_el_paso_1_de_aim_es_el_de_identificar",
                  g[T4.NODO_A]["pasos_accionables"][0].lower().startswith("identificar"),
                  True))
    casos.append(("B_el_entregable_de_aim_es_un_plan",
                  "plan de liderazgo" in g[T4.NODO_A]["entregable_esperado"].lower(),
                  True))

    # --- (C) LA ARISTA ---
    vistas = B.arista_en_las_dos_vistas(g, T4.NODO_A, T4.NODO_B)
    casos.append(("C_la_arista_esta_en_las_cuatro_vistas",
                  sum(1 for v in vistas.values() if v), 4))

    # --- (D) EL COLAPSO, MEDIDO ---
    pa = g[T4.NODO_A]["pasos_accionables"]
    p13 = g[T4.NODO_B]["pasos_accionables"][12]
    s1, comunes = T4.solape(pa[0], p13)
    otros = [T4.solape(p, p13)[0] for i, p in enumerate(pa, 1) if i != 1]
    casos.append(("D_el_colapsado_no_tiene_solape_cero", s1 > 0, True))
    casos.append(("D_ninguno_de_los_otros_lo_supera", max(otros) > s1, False))
    casos.append(("D_el_solape_medio_de_los_otros_es_menor",
                  (sum(otros) / len(otros)) < s1, True))
    casos.append(("D_la_palabra_comun_es_fuera", sorted(comunes), ["fuera"]))
    # HONESTIDAD DEL CASO: el paso 5 EMPATA con el 1, no queda por debajo. Se
    # mide y se dice, en vez de publicar "es el mayor" a secas.
    casos.append(("D_el_paso_5_EMPATA_con_el_1_y_se_dice",
                  len([s for s in otros if s == s1]), 1))
    casos.append(("D_el_solape_por_si_solo_NO_decide_y_por_eso_hay_empate",
                  s1 == max(otros), True))

    # --- (E) EL BARRIDO, LA FORMA ---
    na, ea, ta, _ma = T4.forma_de_los_pasos(g, T4.NODO_A)
    nb, eb, tb, _mb = T4.forma_de_los_pasos(g, T4.NODO_B)
    casos.append(("E_aim_tiene_UN_solo_paso_que_enumera", len(ea), 1))
    casos.append(("E_aim_no_tiene_ningun_criterio_de_parada", len(ta), 0))
    casos.append(("E_causas_tiene_DOS_pasos_que_enumeran", len(eb), 2))
    casos.append(("E_los_pasos_de_los_dos_nodos_suman", na + nb, 21))

    # --- (F) EL CRUCE DE ENTREGABLES Y SU CALIBRACION ---
    calzan = 0
    for eid, _ver, _por in ejemplares:
        fe = filas.get(eid, {})
        x, y = fe.get("nodo_a_leido"), fe.get("nodo_b_leido")
        v, _a, _b = B.cruce_de_entregables(g, x, y)
        if ("D" if v.startswith("ASIMETRICO") else "C") == fe.get("clase"):
            calzan += 1
    casos.append(("F_el_cruce_solo_reproduce_UNO_de_los_cuatro", calzan, 1))
    v005, _a5, _b5 = B.cruce_de_entregables(g, T4.NODO_A, T4.NODO_B)
    casos.append(("F_en_la_005_el_cruce_no_dice_nada",
                  v005.startswith("NINGUNO"), True))
    v101, _a1, _b1 = B.cruce_de_entregables(
        g, "lienzo_modelo_negocio", "search_for_business_model")
    casos.append(("F_en_la_101_el_cruce_si_es_asimetrico",
                  v101.startswith("ASIMETRICO"), True))
    casos.append(("F_pero_no_se_usa_de_decisor_porque_reproduce_1_de_4",
                  calzan < len(ejemplares), True))

    # --- (G) EL REGISTRO DESPUES, MEDIDO COMO DELTA Y NO COMO ESTADO ---
    hoy = clases_del_registro()
    casos.append(("G_el_numero_de_filas_NO_se_mueve",
                  hoy["filas"] - REGISTRO_AL_ABRIR["filas"], 0))
    casos.append(("G_una_sola_clase_baja_de_C",
                  REGISTRO_AL_ABRIR["LECTURA_DIRIGIDA_C"] - hoy["LECTURA_DIRIGIDA_C"], 1))
    casos.append(("G_y_esa_misma_sube_a_D",
                  hoy["LECTURA_DIRIGIDA_D"] - REGISTRO_AL_ABRIR["LECTURA_DIRIGIDA_D"], 1))
    casos.append(("G_el_saco_de_dirigidas_no_cambia_de_tamano",
                  (hoy["LECTURA_DIRIGIDA_C"] + hoy["LECTURA_DIRIGIDA_D"])
                  - (REGISTRO_AL_ABRIR["LECTURA_DIRIGIDA_C"]
                     + REGISTRO_AL_ABRIR["LECTURA_DIRIGIDA_D"]), 0))
    for ld, esperada in sorted(TOCADAS.items()):
        f = filas.get(ld, {})
        casos.append(("G_%s_queda_en_%s" % (ld.replace("-", "_"), esperada),
                      f.get("clase"), esperada))
        casos.append(("G_%s_lleva_la_marca_de_la_164" % ld.replace("-", "_"),
                      MARCA_164 in f.get("razon", ""), True))
        casos.append(("G_%s_la_cita_declara_su_clase_vigente" % ld.replace("-", "_"),
                      (re.search(r"clase ([A-D])", f.get("cita", "").split(",", 1)[1])
                       or [None, None])[1], esperada))
    # NINGUNA SE MUEVE A A, y se mide sobre el registro entero.
    casos.append(("G_ninguna_dirigida_esta_en_A",
                  sum(1 for f in filas.values()
                      if f.get("via") == "LECTURA_DIRIGIDA" and f.get("clase") == "A"), 0))

    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-56s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("")
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")
    print("   SEGUNDA PASADA: SE MUTA EL VALOR ESPERADO Y TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, list):
            mutado = esperado + ["UN_VALOR_QUE_NO_EXISTE"]
        elif esperado is None:
            mutado = "UN_VALOR_QUE_NO_HAY"
        else:
            mutado = str(esperado) + "_MUTADO"
        cae = (real != mutado)
        print("   %-56s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    print("")
    print("   CIFRA casos que CAEN al mutarles el esperado: %d de %d"
          % (caen, len(casos)))
    print("")
    if fallos == 0 and caen == len(casos):
        print("VERDE: %d casos, los %d pasan y los %d CAEN al mutarles el esperado. "
              "EL VEREDICTO NO SE PRUEBA AQUI Y SE DECLARA: no hay caso rojo "
              "automatico para la clasificacion de un paso."
              % (len(casos), len(casos), len(casos)))
        return 0
    print("ROJO: %d fallan y %d no caen al mutarlos." % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
