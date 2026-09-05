# -*- coding: utf-8 -*-
r"""vuelta170_tarea2a_mutacion_aislador.py . CASO POSITIVO POR MUTACION DEL
AISLADOR DE LA CIEGA (TAREA 2.a de la vuelta 170), CON NOMBRE DE ARNES para que
la bateria lo vea (invoca cada arnes SIN ARGUMENTOS).

QUE PRUEBA, Y POR QUE ES ESTO Y NO OTRA COSA. Lo que `aislador_de_ciega.py`
promete es UNA sola cosa que importa: QUE EL DESTAPE NO SE PUEDA LEER EN LA
SALIDA CIEGA. Todo lo demas (los selectores, el criterio, los dos ficheros) es
andamiaje de esa promesa. Asi que el caso central es exactamente el que el acta
169 pide en su `6.1`: **QUE EL CASO CAIGA SI EL DESTAPE SE CUELA EN LA SALIDA
CIEGA**.

Y SE PRUEBA ENSANCHANDO LA LISTA BLANCA, que es el unico camino real por el que
se colaria: `texto_ciego` construye la salida campo a campo desde `CAMPOS_CIEGOS`,
asi que si alguien mete `clase` o `razon` ahi dentro, la fuga aparece. El
parametro `campos` existe en la firma PARA ESTO: para poder mutar la lista sin
tocar el fichero real ni el disco.

CERO ESCRITURAS Y CERO FICHEROS: las filas y el mapa de pasos se fabrican EN
MEMORIA. Nada toca `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` ni el grafo. P.16, el
que fabrica limpia: no hay nada que limpiar porque no se crea nada.

SUJETO CONGELADO (condicion de entrada a la bateria desde la vuelta 148, TAREA
2.5, adjudicacion 3.5 del acta 147): los sujetos son literales de este proceso,
no ficheros vivos. No hay nada que se le pueda mover debajo.

USO:  python scripts/loop/vuelta170_tarea2a_mutacion_aislador.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aislador_de_ciega as A   # noqa: E402

CRITERIO = "criterio de mentira de la prueba de mutacion"

FILAS = [
    {"puesto_intra": 11, "dominio": "compras", "nodo_a": "nodo_uno",
     "nodo_b": "nodo_dos", "banda_078_080": True, "clase": "A",
     "razon": "razon fabricada del primer par, larga a proposito para que se pueda buscar entera"},
    {"puesto_intra": 22, "dominio": "compras", "nodo_a": "nodo_tres",
     "nodo_b": "nodo_cuatro", "banda_078_080": False, "clase": "D",
     "razon": "razon fabricada del segundo par, tambien larga y distinta de la primera"},
    {"puesto_intra": 33, "dominio": "calidad", "nodo_a": "nodo_cinco",
     "nodo_b": "nodo_seis", "banda_078_080": True, "clase": "B",
     "razon": "razon fabricada del tercer par, de otro dominio para poder filtrar"},
]

PASOS = {
    "nodo_uno": ["primer paso del uno", "segundo paso del uno"],
    "nodo_dos": ["unico paso del dos"],
    "nodo_tres": ["primer paso del tres"],
    "nodo_cuatro": [],
    "nodo_cinco": ["paso del cinco"],
    "nodo_seis": ["paso del seis"],
}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 170, TAREA 2.a: CASO POSITIVO POR MUTACION DEL AISLADOR DE CIEGA")
    print("=" * 78)
    print("")
    casos = []

    print("A) LA SALIDA CIEGA LLEVA LO QUE TIENE QUE LLEVAR")
    ciego = A.texto_ciego(FILAS, PASOS, CRITERIO)
    print("   CIFRA bytes del texto ciego: %d" % len(ciego.encode("utf-8")))
    casos.append(("A_lleva_el_puesto_de_cada_par",
                  sum(1 for f in FILAS if "puesto_intra: %d" % f["puesto_intra"] in ciego), 3))
    casos.append(("A_lleva_los_dos_nodos_de_cada_par",
                  sum(1 for f in FILAS
                      for k in ("nodo_a", "nodo_b") if "%s: %s" % (k, f[k]) in ciego), 6))
    casos.append(("A_lleva_los_pasos_de_los_nodos",
                  sum(1 for p in ("primer paso del uno", "unico paso del dos",
                                  "primer paso del tres", "paso del cinco",
                                  "paso del seis") if p in ciego), 5))
    casos.append(("A_dice_cuando_un_nodo_no_tiene_pasos",
                  "pasos de B (nodo_cuatro): 0" in ciego, True))
    casos.append(("A_lleva_el_criterio_escrito", CRITERIO in ciego, True))
    print("")

    print("B) Y NO LLEVA EL DESTAPE: NINGUNA RAZON, NINGUNA CLASE")
    escapes = A.fugas(ciego, FILAS)
    print("   CIFRA fugas con la lista blanca de verdad: %d" % len(escapes))
    casos.append(("B_con_la_lista_blanca_de_verdad_no_hay_fugas", len(escapes), 0))
    casos.append(("B_ninguna_razon_esta_en_el_texto_ciego",
                  sum(1 for f in FILAS if f["razon"] in ciego), 0))
    casos.append(("B_ni_la_forma_en_que_el_destape_escribe_la_clase",
                  sum(1 for f in FILAS if "clase: %s" % f["clase"] in ciego), 0))
    print("")

    print("C) EL CASO QUE EL ACTA PIDE: SI EL DESTAPE SE CUELA, ESTO CAE")
    print("   se ENSANCHA la lista blanca con 'razon' y se vuelve a construir")
    ciego_roto = A.texto_ciego(FILAS, PASOS, CRITERIO,
                               campos=A.CAMPOS_CIEGOS + ("razon",))
    escapes_roto = A.fugas(ciego_roto, FILAS)
    print("   CIFRA fugas con la lista blanca ensanchada: %d" % len(escapes_roto))
    for puesto, campo in escapes_roto:
        print("      puesto %s, campo %s" % (puesto, campo))
    casos.append(("C_la_guarda_MUERDE_las_tres_razones", len(escapes_roto), 3))
    casos.append(("C_y_todas_las_fugas_son_de_razon",
                  sorted(set(c for _p, c in escapes_roto)), ["razon"]))
    print("   se ENSANCHA con 'clase' en vez de 'razon'")
    ciego_clase = A.texto_ciego(FILAS, PASOS, CRITERIO,
                                campos=A.CAMPOS_CIEGOS + ("clase",))
    escapes_clase = A.fugas(ciego_clase, FILAS)
    print("   CIFRA fugas: %d" % len(escapes_clase))
    casos.append(("C_la_guarda_MUERDE_las_tres_clases", len(escapes_clase), 3))
    casos.append(("C_y_todas_las_fugas_son_de_clase",
                  sorted(set(c for _p, c in escapes_clase)), ["clase"]))
    print("   se ENSANCHA con LOS DOS a la vez")
    ciego_ambos = A.texto_ciego(FILAS, PASOS, CRITERIO,
                                campos=A.CAMPOS_CIEGOS + ("clase", "razon"))
    casos.append(("C_con_los_dos_la_guarda_muerde_seis",
                  len(A.fugas(ciego_ambos, FILAS)), 6))
    print("")

    print("D) EL DESTAPE VIVE APARTE Y SI LLEVA LO QUE LE TOCA")
    destape = A.texto_destape(FILAS, CRITERIO)
    casos.append(("D_el_destape_lleva_las_tres_razones",
                  sum(1 for f in FILAS if f["razon"] in destape), 3))
    casos.append(("D_y_las_tres_clases",
                  sum(1 for f in FILAS if "clase: %s" % f["clase"] in destape), 3))
    casos.append(("D_y_el_mismo_criterio_para_poder_casarlos",
                  CRITERIO in destape, True))
    casos.append(("D_el_ciego_y_el_destape_no_son_el_mismo_texto",
                  ciego == destape, False))
    print("   CIFRA bytes del destape: %d" % len(destape.encode("utf-8")))
    print("")

    print("E) LA ELECCION ES DETERMINISTA Y REPRODUCIBLE")
    casos.append(("E_el_filtro_de_dominio_deja_dos",
                  len(A.elegir(FILAS, dominio="compras")), 2))
    casos.append(("E_el_filtro_de_clase_deja_uno",
                  len(A.elegir(FILAS, clase="A")), 1))
    casos.append(("E_el_filtro_de_banda_deja_dos",
                  len(A.elegir(FILAS, banda=True)), 2))
    casos.append(("E_el_rango_de_puestos_deja_uno",
                  len(A.elegir(FILAS, desde=20, hasta=30)), 1))
    m1 = [f["puesto_intra"] for f in A.elegir(FILAS, muestra=2, semilla=170)]
    m2 = [f["puesto_intra"] for f in A.elegir(FILAS, muestra=2, semilla=170)]
    print("   misma semilla, dos corridas: %s y %s" % (m1, m2))
    casos.append(("E_la_misma_semilla_da_la_misma_muestra", m1 == m2, True))
    casos.append(("E_la_muestra_sale_ordenada_por_puesto", m1 == sorted(m1), True))
    casos.append(("E_sin_filtros_estan_los_tres", len(A.elegir(FILAS)), 3))
    print("")

    print("F) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("G) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, list):
            mutado = esperado + ["_mutado"]
        else:
            mutado = str(esperado) + "_mutado"
        cae = (real != mutado)
        print("   %-52s %s   (esperado mutado=%r)"
              % (nombre, "CAE" if cae else "NO CAE", mutado))
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
