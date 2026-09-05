# -*- coding: utf-8 -*-
r"""vuelta162_tarea2a_mutacion_puerta.py . TAREA 2.a de la vuelta 162.

CASO POSITIVO POR MUTACION SOBRE ENCARGO Y CORREDOR FABRICADOS EN MEMORIA, para
la ADJUDICACION 6.5 DEL ACTA 161 (la puerta del corredor tras una parada).

POR QUE ASI, Y NO CON GIT. Las cuatro piezas nuevas de la guarda son PURAS A
PROPOSITO (`es_firma_de_parada`, `portadores_del_encargo`, `sin_el_portador` y
la ya existente `hashes_admitidos_por_el_encargo`): reciben el texto y el
corredor YA LEIDOS. Eso permite fabricar aqui la firma de una parada y un
corredor de mentira sin tocar el disco, sin escribir un commit y sin depender
del estado de la rama.

LA REGLA QUE ESTE FICHERO CUMPLE (EJECUTOR.md 1, 29 ago 2026): ningun assert se
publica como prueba sin haber corrido antes SU PRUEBA DE MUTACION. Aqui cada
caso es (nombre, funcion que COMPUTA el valor, valor esperado); la pasada 1 corre
los casos tal cual y TODOS tienen que pasar; la pasada 2 MUTA el valor esperado
de cada caso y ese caso TIENE que caer. Un caso que sobrevive a su mutacion no
prueba nada y sale ROJO por su nombre.

LOS DOS CASOS QUE IMPORTAN, Y SE DICEN ANTES DE CORRERLOS:
  - `puerta_solo_con_firma`: sin firma de parada, la puerta NO se abre. Es la
    mitad que la adjudicacion promete no tocar.
  - `rojo_del_ejecutor_intacto`: un commit del EJECUTOR delante de la apertura
    sigue siendo INTRUSO aunque el corredor traiga tambien al portador del
    encargo. Si este caso se pusiera verde, la puerta estaria abierta de mas.

USO:
  python scripts/loop/vuelta162_tarea2a_mutacion_puerta.py
SUJETO CONGELADO (declarado en la vuelta 180, TAREA 2.a): este arnes NOMBRA `master_graph.json` en su texto pero NO LO ABRE (1 apariciones en el texto, 0 llamadas que lo lean y 0 lecturas del fichero vivo, medidas fila a fila en docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl), asi que su resultado no depende de lo que ese fichero diga hoy.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_apertura_sellada as G   # noqa: E402

# --- LO FABRICADO, TODO EN MEMORIA ----------------------------------------

ACTA_CON_PARADA = ("", "PARA ALEXIS: hay parada y es legitima. Aqui van las tres opciones.")
ACTA_NORMAL = ("SESION EJECUTORA. TU VUELTA ES LA 999.", None)
ACTA_SIN_ENCARGO = (None, "PARA ALEXIS: texto de la parada.")
ACTA_CON_LOS_DOS_VACIOS = ("", "   \n  ")

ENCARGO_SIN_ROTULO = "SESION EJECUTORA. Decision del fundador. Cita de paso: d3482b11."
ENCARGO_CON_ROTULO_NINGUNO = (
    "SESION EJECUTORA.\n\nHASHES ADMITIDOS EN EL CORREDOR DE ESTA VUELTA: NINGUNO. No hay "
    "commit de decision que admitir.\n\nTAREA 1, lo que sea.")

# corredor fabricado: [(hash, asunto, [rutas])], del mas nuevo al mas viejo,
# que es el orden en que `git log` lo entrega.
PORTADOR = "aaaaaaaa11111111111111111111111111111111"
EJECUTOR = "bbbbbbbb22222222222222222222222222222222"
OTRO_ENCARGO = "cccccccc33333333333333333333333333333333"

FILA_PORTADOR = (PORTADOR, "Decision del fundador: se congela la vara",
                 ["docs/loop/PROMPT_SIGUIENTE.md",
                  "docs/loop/paradas/2026-09-03-DECISION.md",
                  "docs/plan/BANCO_DEL_PLAN.md"])
FILA_EJECUTOR = (EJECUTOR, "VUELTA 999, TAREA 1: escribo el grafo",
                 ["dataset/metadata/master_graph.json"])
FILA_OTRO_ENCARGO = (OTRO_ENCARGO, "Segundo encargo, que no deberia existir",
                     ["docs/loop/PROMPT_SIGUIENTE.md"])
FILA_SOLO_PARADA = ("dddddddd4444444444444444444444444444444d",
                    "Respuesta del fundador, solo papeles de parada",
                    ["docs/loop/paradas/2026-09-03-respuesta.md"])

CORREDOR_SOLO_PORTADOR = [FILA_PORTADOR]
CORREDOR_PORTADOR_Y_EJECUTOR = [FILA_EJECUTOR, FILA_PORTADOR]
CORREDOR_DOS_ENCARGOS = [FILA_OTRO_ENCARGO, FILA_PORTADOR]
CORREDOR_SIN_ENCARGO = [FILA_SOLO_PARADA]


def _intrusos(corredor, portador):
    """Lo que la guarda hace de verdad: quita al portador y despues cuenta
    intrusos. Devuelve los hashes cortos de los intrusos, ordenados."""
    resto, _fuera = G.sin_el_portador(corredor, portador)
    intrusos, _adm = G.intrusos_del_corredor(resto, ())
    return sorted(h[:8] for h, _a, _r in intrusos)


# --- LOS CASOS: (nombre, computa, esperado) --------------------------------

CASOS = [
    # LA FIRMA DE LA PARADA
    ("firma_positiva",
     lambda: G.es_firma_de_parada(*ACTA_CON_PARADA), True),
    ("firma_no_con_acta_normal",
     lambda: G.es_firma_de_parada(*ACTA_NORMAL), False),
    ("firma_no_si_el_acta_no_trae_el_encargo",
     lambda: G.es_firma_de_parada(*ACTA_SIN_ENCARGO), False),
    ("firma_no_si_PARA_ALEXIS_esta_en_blanco",
     lambda: G.es_firma_de_parada(*ACTA_CON_LOS_DOS_VACIOS), False),

    # EL PORTADOR
    ("portador_unico",
     lambda: [h[:8] for h in G.portadores_del_encargo(CORREDOR_SOLO_PORTADOR)],
     ["aaaaaaaa"]),
    ("portador_ninguno_si_nadie_escribe_el_encargo",
     lambda: G.portadores_del_encargo(CORREDOR_SIN_ENCARGO), []),
    ("dos_portadores_se_ven_los_dos_y_el_primero_es_el_mas_viejo",
     lambda: [h[:8] for h in G.portadores_del_encargo(CORREDOR_DOS_ENCARGOS)],
     ["aaaaaaaa", "cccccccc"]),

    # EL CORREDOR SIN EL PORTADOR
    ("quitar_al_portador_deja_el_resto",
     lambda: [f[0][:8] for f in
              G.sin_el_portador(CORREDOR_PORTADOR_Y_EJECUTOR, PORTADOR)[0]],
     ["bbbbbbbb"]),
    ("sin_portador_None_no_quita_nada",
     lambda: [f[0][:8] for f in
              G.sin_el_portador(CORREDOR_PORTADOR_Y_EJECUTOR, None)[0]],
     ["bbbbbbbb", "aaaaaaaa"]),

    # LA PUERTA, ENTERA
    ("puerta_abierta_deja_el_corredor_limpio",
     lambda: _intrusos(CORREDOR_SOLO_PORTADOR, PORTADOR), []),
    ("puerta_solo_con_firma",
     lambda: _intrusos(CORREDOR_SOLO_PORTADOR, None), ["aaaaaaaa"]),
    ("rojo_del_ejecutor_intacto",
     lambda: _intrusos(CORREDOR_PORTADOR_Y_EJECUTOR, PORTADOR), ["bbbbbbbb"]),

    # EL MECANISMO DEL ROTULO, QUE NO CAMBIA EN NADA
    ("rotulo_ausente_no_admite_nada",
     lambda: G.hashes_admitidos_por_el_encargo(ENCARGO_SIN_ROTULO)[1:],
     ([], False)),
    ("rotulo_con_NINGUNO_admite_cero_y_lo_dice",
     lambda: G.hashes_admitidos_por_el_encargo(ENCARGO_CON_ROTULO_NINGUNO)[1:],
     ([], True)),
]


def _mutar(valor):
    """Cambia el valor esperado a otro DISTINTO del mismo tipo. Es lo que la
    prueba de mutacion necesita: si el caso sigue pasando con el esperado
    cambiado, el caso no mide nada."""
    if isinstance(valor, bool):
        return not valor
    if isinstance(valor, list):
        return valor + ["ZZZZZZZZ"]
    if isinstance(valor, tuple):
        return tuple(list(valor) + ["ZZZZZZZZ"])
    return "ZZZZZZZZ"


def main():
    print("PASADA 1, LOS CASOS TAL CUAL: todos tienen que PASAR.")
    caidos_1 = []
    for nombre, computa, esperado in CASOS:
        obtenido = computa()
        ok = obtenido == esperado
        print("  %-52s esperado %-28r obtenido %-28r %s"
              % (nombre, esperado, obtenido, "PASA" if ok else "CAE"))
        if not ok:
            caidos_1.append(nombre)

    print("")
    print("PASADA 2, LA MUTACION: se cambia el valor esperado y cada caso TIENE que CAER.")
    sobrevivientes = []
    for nombre, computa, esperado in CASOS:
        mutado = _mutar(esperado)
        obtenido = computa()
        cae = obtenido != mutado
        print("  %-52s esperado MUTADO %-28r obtenido %-28r %s"
              % (nombre, mutado, obtenido, "CAE (bien)" if cae else "SOBREVIVE (mal)"))
        if not cae:
            sobrevivientes.append(nombre)

    print("")
    if caidos_1:
        print("ROJO: %d caso(s) no pasan tal cual: %s" % (len(caidos_1), caidos_1))
        return 1
    if sobrevivientes:
        print("ROJO: %d caso(s) sobreviven a su mutacion y por tanto no prueban nada: %s"
              % (len(sobrevivientes), sobrevivientes))
        return 1
    print("VERDE: %d casos, los %d pasan tal cual y los %d caen al mutarles el valor "
          "esperado." % (len(CASOS), len(CASOS), len(CASOS)))
    print("Y LOS DOS QUE IMPORTAN, POR SU NOMBRE: `puerta_solo_con_firma` (sin firma de "
          "parada la puerta NO se abre) y `rojo_del_ejecutor_intacto` (un commit del "
          "ejecutor delante de la apertura sigue siendo intruso aunque el portador este "
          "en el mismo corredor).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
