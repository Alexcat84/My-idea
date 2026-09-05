# -*- coding: utf-8 -*-
r"""vuelta177_tarea1f_mutacion_tope_minutos.py . EL CASO POSITIVO POR MUTACION
DEL TOPE DE TRAMO POR MINUTOS (TAREA 1.f de la vuelta 177).

QUE SUJETO PRUEBA: las tres funciones puras que la TAREA 1.f anade a
`scripts/loop/verificar_mutaciones_viejas.py`, mas el carril nuevo de
`reparto_en_tramos()`:

    reloj_de_la_corrida(texto)   . el reloj medido, leido de la salida de una
                                   corrida anterior.
    minutos_por_entrada(reloj)   . el coste por entrada, EL MAXIMO Y NO LA MEDIA.
    tamano_por_minutos(reloj)    . el tamano de tramo COMPUTADO de ese coste.
    reparto_en_tramos(n, None, reloj=...) . el reparto sin elegir el tamano.

POR QUE (adjudicacion 7.3 del acta 176, que contesta el `D.3` y la `P.3`). El
tamano de tramo de la 176 se eligio a ojo, la estimacion publicada fue de 3,3 a
4,3 minutos por tramo, y el tramo 4 tardo 15,9. El auditor lo acepto por haberse
publicado ANTES de correr, y encargo el tope POR MINUTOS, computado del reloj
medido, para que la 181 no lo tenga que decidir a ojo.

LO QUE HAY QUE PODER TUMBAR, Y ES LO QUE ESTA PRUEBA BUSCA: que el computo sea
un adorno. Un `tamano_por_minutos` que devolviera siempre lo mismo, o que se
comiera un reloj vacio sin decirlo, o que usara la MEDIA en vez del MAXIMO,
pasaria una prueba floja y volveria a producir el tramo de 15,9. Asi que cada
caso de aqui muta UNA cosa del reloj y exige que el tamano SE MUEVA en la
direccion correcta.

EL CASO 4 ES EL QUE IMPORTA MAS: se le da un reloj DESIGUAL (un tramo carisimo
entre varios baratos, que es exactamente la forma del reloj de la 176) y se
exige que el tamano salga del CARO y no del promedio. Si esta prueba se cae, la
correccion no sirve de nada.

CERO ESCRITURAS: todo sobre relojes fabricados en memoria y sobre el texto de la
corrida de la 176 leido en modo lectura.

USO:  python scripts/loop/vuelta177_tarea1f_mutacion_tope_minutos.py
"""
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import verificar_mutaciones_viejas as B   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(AQUI))
SALIDA_176 = os.path.join(RAIZ, "docs", "loop", "SALIDA_V176_BATERIA.txt")
NL = chr(10)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 177, TAREA 1.f: EL TAMANO DE TRAMO SE COMPUTA Y NO SE ELIGE")
    print("=" * 78)
    print("")

    casos = []

    print("A) EL TOPE, LEIDO DE SU CONSTANTE Y NO TECLEADO AQUI")
    print("   TOPE_DE_MINUTOS_POR_TRAMO = %.1f" % B.TOPE_DE_MINUTOS_POR_TRAMO)
    casos.append(("A_el_tope_esta_escrito_en_el_fichero",
                  isinstance(B.TOPE_DE_MINUTOS_POR_TRAMO, float), True))
    casos.append(("A_el_tope_es_mayor_que_cero", B.TOPE_DE_MINUTOS_POR_TRAMO > 0, True))
    print("")

    print("B) EL RELOJ DE LA CORRIDA DE VERDAD, LEIDO DE SU SALIDA")
    print("   fichero: docs/loop/SALIDA_V176_BATERIA.txt")
    hay = os.path.exists(SALIDA_176)
    print("   existe: %s | bytes: %s"
          % (hay, os.path.getsize(SALIDA_176) if hay else "NO EXISTE"))
    casos.append(("B_la_salida_de_la_176_existe", hay, True))
    texto = io.open(SALIDA_176, encoding="utf-8", errors="replace").read() if hay else ""
    reloj = B.reloj_de_la_corrida(texto)
    print("   CIFRA tramos que el reloj trae: %d" % len(reloj))
    print("   el reloj: %s" % reloj)
    suma = round(sum(m for _e, m in reloj), 1)
    print("   CIFRA suma de los minutos: %.1f" % suma)
    casos.append(("B_el_reloj_trae_nueve_tramos", len(reloj), 9))
    casos.append(("B_la_suma_del_reloj_es_la_publicada", suma, 31.9))
    casos.append(("B_la_suma_de_entradas_es_la_nomina_de_la_176",
                  sum(e for e, _m in reloj), 88))
    print("")

    print("C) EL COSTE POR ENTRADA ES EL MAXIMO Y NO LA MEDIA, SOBRE ESE RELOJ")
    coste = B.minutos_por_entrada(reloj)
    media = sum(m for _e, m in reloj) / sum(e for e, _m in reloj)
    print("   coste por entrada, MAXIMO: %.4f" % coste)
    print("   coste por entrada, media (que es lo que NO se usa): %.4f" % media)
    print("   el maximo es %.1f veces la media" % (coste / media))
    casos.append(("C_el_coste_es_el_maximo", round(coste, 4), 1.59))
    casos.append(("C_el_maximo_no_es_la_media", round(coste, 4) == round(media, 4), False))
    print("")

    print("D) EL TAMANO, COMPUTADO DE ESE RELOJ")
    tam, motivo = B.tamano_por_minutos(reloj)
    print("   tamano: %d" % tam)
    print("   motivo: %s" % motivo)
    casos.append(("D_el_motivo_dice_COMPUTADO", motivo.startswith("COMPUTADO"), True))
    casos.append(("D_el_tamano_es_el_del_tope_entre_el_coste",
                  tam, max(1, int(B.TOPE_DE_MINUTOS_POR_TRAMO / coste))))
    print("   y NINGUN tramo de ese tamano se pasaria del tope, al coste medido:")
    print("      %d entradas x %.4f min = %.1f min, tope %.1f"
          % (tam, coste, tam * coste, B.TOPE_DE_MINUTOS_POR_TRAMO))
    casos.append(("D_el_tramo_computado_cabe_en_el_tope",
                  tam * coste <= B.TOPE_DE_MINUTOS_POR_TRAMO, True))
    print("   Y EL DE LA 176 NO CABIA, que es todo el motivo de esta tarea:")
    print("      10 entradas x %.4f min = %.1f min, tope %.1f"
          % (coste, 10 * coste, B.TOPE_DE_MINUTOS_POR_TRAMO))
    casos.append(("D_el_tramo_de_la_176_NO_cabia_en_el_tope",
                  10 * coste <= B.TOPE_DE_MINUTOS_POR_TRAMO, False))
    print("")

    print("E) MUTACION 1: UN RELOJ DESIGUAL. EL TAMANO SALE DEL CARO, NO DEL PROMEDIO")
    print("   (ES EL CASO QUE IMPORTA: si esto se cae, la correccion no sirve)")
    desigual = [(10, 1.0), (10, 1.0), (10, 1.0), (10, 20.0)]
    t_des, _m = B.tamano_por_minutos(desigual)
    coste_max = 20.0 / 10
    coste_med = 23.0 / 40
    print("   reloj: %s" % desigual)
    print("   coste MAXIMO %.2f | coste MEDIO %.4f" % (coste_max, coste_med))
    print("   tamano computado: %d" % t_des)
    print("   si usara la media daria: %d"
          % max(1, int(B.TOPE_DE_MINUTOS_POR_TRAMO / coste_med)))
    casos.append(("E_desigual_sale_del_caro", t_des,
                  max(1, int(B.TOPE_DE_MINUTOS_POR_TRAMO / coste_max))))
    casos.append(("E_desigual_NO_sale_del_promedio",
                  t_des == max(1, int(B.TOPE_DE_MINUTOS_POR_TRAMO / coste_med)), False))
    print("")

    print("F) MUTACION 2: SI LA CORRIDA ES MAS LENTA, EL TAMANO BAJA")
    lento = [(e, m * 4) for e, m in reloj]
    t_len, _m = B.tamano_por_minutos(lento)
    print("   con el mismo reloj x4 de lento, tamano: %d (antes %d)" % (t_len, tam))
    casos.append(("F_mas_lento_da_tramo_mas_chico", t_len < tam, True))
    print("")

    print("G) MUTACION 3: SI LA CORRIDA ES MAS RAPIDA, EL TAMANO SUBE")
    rapido = [(e, m / 4) for e, m in reloj]
    t_rap, _m = B.tamano_por_minutos(rapido)
    print("   con el mismo reloj 4 veces mas rapido, tamano: %d (antes %d)" % (t_rap, tam))
    casos.append(("G_mas_rapido_da_tramo_mas_grande", t_rap > tam, True))
    print("")

    print("H) MUTACION 4: SIN RELOJ, NO FINGE QUE COMPUTO NADA")
    t_sin, m_sin = B.tamano_por_minutos([])
    print("   tamano: %d | motivo: %s" % (t_sin, m_sin))
    casos.append(("H_sin_reloj_devuelve_el_por_defecto", t_sin, 10))
    casos.append(("H_sin_reloj_lo_dice_en_voz_alta",
                  m_sin.startswith("SIN RELOJ"), True))
    casos.append(("H_sin_reloj_NO_dice_COMPUTADO",
                  m_sin.startswith("COMPUTADO"), False))
    print("   y un texto sin marcadores da reloj vacio en vez de reventar:")
    print("      reloj_de_la_corrida('hola'): %s" % B.reloj_de_la_corrida("hola"))
    casos.append(("H_texto_sin_marcadores_da_reloj_vacio",
                  len(B.reloj_de_la_corrida("hola")), 0))
    print("")

    print("I) MUTACION 5: UN RELOJ ABSURDO NUNCA DA UN TRAMO DE CERO")
    carisimo = [(1, 10000.0)]
    t_car, _m = B.tamano_por_minutos(carisimo)
    print("   con 10000 minutos por entrada, tamano: %d" % t_car)
    casos.append(("I_nunca_devuelve_menos_de_uno", t_car, 1))
    print("   (un tramo de cero entradas dejaria la nomina sin correr, que es la")
    print("    unica cosa que la letra del fundador del 5 sep no permite tocar)")
    print("")

    print("J) EL CARRIL NUEVO DE reparto_en_tramos(), Y QUE EL VIEJO NO SE MOVIO")
    con_reloj = B.reparto_en_tramos(B.VIEJAS, None, reloj=reloj)
    con_numero = B.reparto_en_tramos(B.VIEJAS, 10)
    print("   con tamano=None y reloj: %d tramos" % len(con_reloj))
    print("   con tamano=10, como siempre: %d tramos" % len(con_numero))
    casos.append(("J_el_carril_nuevo_reparte_por_el_computado",
                  max(len(x) for x in con_reloj), tam))
    casos.append(("J_el_carril_viejo_sigue_repartiendo_de_diez",
                  max(len(x) for x in con_numero), 10))
    print("   LA UNION SIGUE SIENDO LA NOMINA ENTERA, que es lo que este reparto")
    print("   no puede romper nunca:")
    for nombre_c, tramos in (("con reloj", con_reloj), ("con numero", con_numero)):
        plano = [x for tr in tramos for x in tr]
        print("      %-12s -> %d entradas, identicas y en orden a la nomina: %s"
              % (nombre_c, len(plano), plano == list(B.VIEJAS)))
        casos.append(("J_%s_la_union_es_la_nomina" % nombre_c.replace(" ", "_"),
                      plano == list(B.VIEJAS), True))
    print("")

    print("K) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre_c, real_v, esperado in casos:
        ok = (real_v == esperado)
        print("   %-54s %s   (real=%r esperado=%r)"
              % (nombre_c, "PASA" if ok else "FALLA", real_v, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("L) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre_c, real_v, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        else:
            mutado = esperado + 1
        cae = (real_v != mutado)
        print("   %-54s %s   (esperado mutado=%r)"
              % (nombre_c, "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
