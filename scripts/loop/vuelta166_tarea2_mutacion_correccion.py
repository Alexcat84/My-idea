# -*- coding: utf-8 -*-
r"""vuelta166_tarea2_mutacion_correccion.py . CASO POSITIVO POR MUTACION DE LA
CORRECCION DECLARADA DE `OP-L-01` (TAREA 2 de la vuelta 166), CON NOMBRE DE
ARNES para que la bateria lo vea (`verificar_mutaciones_viejas.py` invoca cada
arnes SIN ARGUMENTOS).

QUE PRUEBA, Y POR QUE ES ESTO. Lo unico que esta TAREA promete es que la
correccion entra POR ADICION: sin borrar una letra, sin clave nueva de esquema,
sin tocar el resto de la ficha y sin tocar las otras 70 lineas. Esa promesa vive
entera en `invariantes()`. Asi que lo que hay que poder tumbar es exactamente
eso: se fabrican fichas MUTADAS que violan cada invariante de una en una y se
exige que el invariante correspondiente CAIGA. Un guardian que aprueba una
mutacion que deberia rechazar no es un guardian.

CERO ESCRITURAS: todo se hace en memoria sobre copias de las lineas leidas.

USO:  python scripts/loop/vuelta166_tarea2_mutacion_correccion.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta166_tarea2_correccion_op_l_01 as T   # noqa: E402


def _con(lineas, n, d):
    """Devuelve (linea_nueva, lineas_nuevas) para la ficha d en la linea n."""
    l = json.dumps(d, ensure_ascii=False)
    ls = list(lineas)
    ls[n - 1] = l
    return l, ls


def _veredictos(inv):
    return {nombre: ok for nombre, ok, _det in inv}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 166, TAREA 2: CASO POSITIVO POR MUTACION DE LOS CINCO INVARIANTES")
    print("=" * 78)
    print("")

    lineas = T.lineas_del_fichero()
    n, d, linea_vieja = T.ficha(lineas)
    print("A) EL SUJETO, LEIDO DEL FICHERO DE VERDAD Y NO FABRICADO")
    print("   docs/plan/OPERACIONES.jsonl:%d, ficha %s" % (n, d["id_op"]))
    print("   CIFRA lineas del fichero: %d" % len([x for x in lineas if x.strip()]))
    print("   CIFRA clausulas de verificacion hoy: %d" % len(d["verificacion"]))
    print("")

    casos = []

    print("B) EL CASO SANO: LA ADICION LIMPIA TIENE QUE PASAR LOS CINCO")
    sano = json.loads(linea_vieja)
    sano["verificacion"] = list(sano["verificacion"]) + ["CORRECCION UNO", "CORRECCION DOS"]
    ln, lns = _con(lineas, n, sano)
    v = _veredictos(T.invariantes(linea_vieja, ln, lineas, lns, n))
    for k in sorted(v):
        print("   %-52s %s" % (k, "PASA" if v[k] else "FALLA"))
    casos.append(("B_la_adicion_limpia_pasa_los_cinco", sum(v.values()), 5))
    print("")

    print("C) MUTACION 1: SE BORRA UNA LETRA DE LA CLAUSULA VIEJA")
    m = json.loads(linea_vieja)
    vieja0 = m["verificacion"][0]
    m["verificacion"] = [vieja0[:-1]] + list(m["verificacion"][1:]) + ["A", "B"]
    ln, lns = _con(lineas, n, m)
    v = _veredictos(T.invariantes(linea_vieja, ln, lineas, lns, n))
    print("   se le quita el ultimo caracter a la clausula 1")
    print("   invariante 1 (byte a byte): %s" % ("PASA" if v["1_las_clausulas_viejas_siguen_byte_a_byte_y_en_su_orden"] else "CAE"))
    casos.append(("C_borrar_una_letra_tumba_el_invariante_1",
                  v["1_las_clausulas_viejas_siguen_byte_a_byte_y_en_su_orden"], False))

    print("C bis: SE BORRA UNA CLAUSULA ENTERA Y SE SUSTITUYE")
    m = json.loads(linea_vieja)
    m["verificacion"] = [m["verificacion"][0], m["verificacion"][2], "A", "B", "C"]
    ln, lns = _con(lineas, n, m)
    v = _veredictos(T.invariantes(linea_vieja, ln, lineas, lns, n))
    casos.append(("Cbis_borrar_la_clausula_2_tumba_el_invariante_1",
                  v["1_las_clausulas_viejas_siguen_byte_a_byte_y_en_su_orden"], False))

    print("C ter: SE REORDENAN LAS VIEJAS SIN BORRAR NINGUNA")
    m = json.loads(linea_vieja)
    m["verificacion"] = [m["verificacion"][1], m["verificacion"][0],
                         m["verificacion"][2], "A", "B"]
    ln, lns = _con(lineas, n, m)
    v = _veredictos(T.invariantes(linea_vieja, ln, lineas, lns, n))
    print("   ninguna se borra, pero cambian de orden")
    casos.append(("Cter_reordenar_las_viejas_tumba_el_invariante_1",
                  v["1_las_clausulas_viejas_siguen_byte_a_byte_y_en_su_orden"], False))
    print("")

    print("D) MUTACION 2: SE CREA UNA CLAVE NUEVA DE ESQUEMA")
    m = json.loads(linea_vieja)
    m["verificacion"] = list(m["verificacion"]) + ["A", "B"]
    m["correccion_declarada"] = "una clave que el esquema no tiene"
    ln, lns = _con(lineas, n, m)
    v = _veredictos(T.invariantes(linea_vieja, ln, lineas, lns, n))
    print("   se anade la clave 'correccion_declarada'")
    casos.append(("D_clave_nueva_tumba_el_invariante_2",
                  v["2_el_esquema_no_gana_ni_pierde_una_clave"], False))
    print("D bis: SE QUITA UNA CLAVE DEL ESQUEMA")
    m = json.loads(linea_vieja)
    m["verificacion"] = list(m["verificacion"]) + ["A", "B"]
    del m["pregunta_pendiente"]
    ln, lns = _con(lineas, n, m)
    v = _veredictos(T.invariantes(linea_vieja, ln, lineas, lns, n))
    casos.append(("Dbis_quitar_una_clave_tumba_el_invariante_2",
                  v["2_el_esquema_no_gana_ni_pierde_una_clave"], False))
    print("")
    print("E) MUTACION 3: LA LISTA CRECE EN OTRA COSA QUE DOS")
    for cuantas in (0, 1, 3):
        m = json.loads(linea_vieja)
        m["verificacion"] = list(m["verificacion"]) + ["X"] * cuantas
        ln, lns = _con(lineas, n, m)
        v = _veredictos(T.invariantes(linea_vieja, ln, lineas, lns, n))
        print("   crece en %d -> invariante 3: %s"
              % (cuantas, "PASA" if v["3_verificacion_crece_en_exactamente_dos"] else "CAE"))
        casos.append(("E_crecer_en_%d_tumba_el_invariante_3" % cuantas,
                      v["3_verificacion_crece_en_exactamente_dos"], False))
    print("")

    print("F) MUTACION 4: SE TOCA EL RESTO DE LA FICHA (Y EL ESTADO ES EL CASO GORDO)")
    m = json.loads(linea_vieja)
    m["verificacion"] = list(m["verificacion"]) + ["A", "B"]
    m["estado"] = "HECHA"
    ln, lns = _con(lineas, n, m)
    v = _veredictos(T.invariantes(linea_vieja, ln, lineas, lns, n))
    print("   se cambia estado de LISTA a HECHA de tapadillo dentro de la correccion")
    casos.append(("F_mover_el_estado_tumba_el_invariante_4",
                  v["4_el_resto_de_la_ficha_no_se_toca_ni_en_estado"], False))
    m = json.loads(linea_vieja)
    m["verificacion"] = list(m["verificacion"]) + ["A", "B"]
    m["depende_de"] = ["OP-D-01"]
    ln, lns = _con(lineas, n, m)
    v = _veredictos(T.invariantes(linea_vieja, ln, lineas, lns, n))
    print("   se le inventa una dependencia")
    casos.append(("Fbis_inventar_dependencia_tumba_el_invariante_4",
                  v["4_el_resto_de_la_ficha_no_se_toca_ni_en_estado"], False))
    print("")

    print("G) MUTACION 5: SE TOCA OTRA LINEA DEL FICHERO")
    m = json.loads(linea_vieja)
    m["verificacion"] = list(m["verificacion"]) + ["A", "B"]
    ln, lns = _con(lineas, n, m)
    otra = 1 if n != 1 else 2
    d_otra = json.loads(lns[otra - 1])
    d_otra["estado"] = "HECHA" if d_otra["estado"] != "HECHA" else "LISTA"
    lns[otra - 1] = json.dumps(d_otra, ensure_ascii=False)
    v = _veredictos(T.invariantes(linea_vieja, ln, lineas, lns, n))
    print("   se le cambia el estado a la ficha de la linea %d" % otra)
    casos.append(("G_tocar_otra_linea_tumba_el_invariante_5",
                  v["5_las_otras_lineas_del_fichero_no_se_tocan"], False))
    m = json.loads(linea_vieja)
    m["verificacion"] = list(m["verificacion"]) + ["A", "B"]
    ln, lns = _con(lineas, n, m)
    lns.append(json.dumps({"id_op": "OP-FALSA"}, ensure_ascii=False))
    v = _veredictos(T.invariantes(linea_vieja, ln, lineas, lns, n))
    print("   se le cuela una ficha nueva al final del fichero")
    casos.append(("Gbis_colar_una_ficha_nueva_tumba_el_invariante_5",
                  v["5_las_otras_lineas_del_fichero_no_se_tocan"], False))
    print("")

    print("H) EL TEXTO DE LAS DOS CORRECCIONES SIGUE A LA MEDICION Y NO A UNA CONSTANTE")
    mapa, _nn = T.mapa_de_alias()
    once = T.las_once()
    V = T.veredictos()
    n_lit, n_res, n_pl, n_pr, hall = T.medir_clausula_1(mapa, once, V)
    real = T.texto_correccion_1(hall, n_lit, n_res, n_pl, n_pr, len(mapa), len(V))
    falso = T.texto_correccion_1(hall[:1], n_lit, 1, n_pl, n_pr, len(mapa), len(V))
    print("   CIFRA hallazgos medidos hoy: %d" % len(hall))
    casos.append(("H_el_texto_nombra_las_tres", real.count("cae sobre"), 3))
    casos.append(("H_con_un_hallazgo_solo_nombra_una", falso.count("cae sobre"), 1))
    casos.append(("H_los_dos_textos_no_son_iguales", real == falso, False))
    casos.append(("H_el_texto_lleva_los_cinco_puestos",
                  sum(1 for p in ("712", "976", "1190", "1325", "1281") if p in real), 5))
    c2a = T.texto_correccion_2(len(V), d["adjudicacion"], 0)
    c2b = T.texto_correccion_2(2117, d["adjudicacion"], 0)
    casos.append(("H_la_correccion_2_lleva_el_marcador_de_hoy", str(len(V)) in c2a, True))
    casos.append(("H_y_cambia_si_el_marcador_cambia", c2a == c2b, False))
    print("")

    print("I) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real_v, esperado in casos:
        ok = (real_v == esperado)
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real_v, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("J) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real_v, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        else:
            mutado = str(esperado) + "_mutado"
        cae = (real_v != mutado)
        print("   %-52s %s   (esperado mutado=%r)"
              % (nombre, "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    print("K) Y SE COMPRUEBA QUE ESTA PRUEBA NO ESCRIBIO NADA")
    lineas2 = T.lineas_del_fichero()
    print("   el fichero es identico byte a byte al de antes de la prueba: %s"
          % (lineas == lineas2))
    if lineas != lineas2:
        print("   ROJO: la prueba de mutacion escribio. Eso es peor que no tenerla.")
        return 1
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
