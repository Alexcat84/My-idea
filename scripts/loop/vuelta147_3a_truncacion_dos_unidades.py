# -*- coding: utf-8 -*-
r"""vuelta147_3a_truncacion_dos_unidades.py . TAREA 3.a de la vuelta 147, la
RELECTURA AL DOBLE de la 3.f de la vuelta 146, y la medicion que alimenta la
CORRECCION 25.

POR QUE NACE. El acta de la vuelta 146, caida 4.1: el reporte de la 146 y la
CORRECCION 24.c publicaron *"ocho de ellas estan VIVAS y son CANONICAS de la
tabla de OP-S-11"* y ENUMERARON SIETE NOMBRES en la misma frase. Es CAIDA DE
CIFRA PUBLICADA porque vive en `docs/plan/CORRECCIONES_A_APLICAR.md`. Una
caida FUERA de lo marcado obliga a RELEER EL TRAMO AL DOBLE, y releer al doble
NO es repetir la misma cuenta: es medir la truncacion CON LAS DOS UNIDADES,
cada una con su nomina completa, y decir CUAL GOBIERNA con la cita del
registro delante.

LAS DOS UNIDADES, ESCRITAS ANTES DE CORRER NADA.

  (A) LA SOLA LONGITUD: `len(titulo) == 31`. Es la que uso la vuelta 146 en su
      3.f. Titulo = el segmento anterior al PRIMER " - " de la grafia.

  (B) EL DETECTOR VIGENTE DE LA CAMPANA: `len(titulo) == 31` CON RESTO NO
      VACIO. Registrado en `docs/PENDIENTES.md`, DECIMA entrada (vuelta 132,
      corregido en la vuelta 131 sobre el discutible del acta 130, y re-medido
      en la vuelta 134), y escrito ademas en el codigo desde la 131:
      `scripts/loop/vuelta131_residuo_para_decision.py:es_truncada`, que dice
      literalmente `len(titulo_de(g)) == 31 and bool(resto_de(g))`. El registro
      NOMBRA su falso positivo por su nombre: `Guia de empaque para
      transporte`, titulo completo sin autor, RESTO vacio, que no esta truncado
      y simplemente mide 31 caracteres por coincidencia.

CUAL GOBIERNA, Y NO LO DECIDE ESTE INSTRUMENTO: lo decide el registro. La (B)
esta ADJUDICADA Y REGISTRADA desde la vuelta 131 y re-medida en la 134; la (A)
es la forma cruda que aquel registro corrigio. Este script MIDE LAS DOS y
publica las dos nominas enteras, para que la cifra que gobierna no esconda a la
otra (misma doctrina de las dos unidades de arista del acta 145 y de las dos
unidades de la vara del acta 146, 3.18).

NO SE REIMPLEMENTA NADA QUE YA EXISTA (la averia de los dos `master_graph` que
el chequeo de gemelos vino a curar): `partir` se importa de
`vuelta146_1c_cifras_ficha_op_a_01.py`, que es el mismo particionador con el
que la 146 hizo su censo, y `cargar_tabla` se importa de
`vuelta136_simular_ops11.py`, que parsea `OP_S_11_MAPEO_PROPUESTO.md` tal como
esta escrita sin recalcular el union-find.

QUE PUBLICA, y todo con su linea `CIFRA <etiqueta>: <n> <unidad>` para que
`verificar_cifras_del_reporte.py` pueda cotejarlo:

  UNIVERSO 1, EL CATALOGO DE HOY (`dataset/metadata/master_graph.json`, WORK):
  las grafias distintas del campo `fuente` en CUALQUIER posicion, con sus
  nodos vivos y deprecados, filtradas por cada unidad, y de ellas cuantas son
  VIVAS (vivos > 0) y cuantas son ademas CANONICAS de la tabla de `OP-S-11`.

  UNIVERSO 2, LA TABLA CANONICA DIRECTAMENTE: las canonicas distintas de
  `docs/plan/OP_S_11_MAPEO_PROPUESTO.md`, filtradas por cada unidad. Es el
  camino independiente: no pasa por el grafo.

NO TOCA NI UNA GRAFIA, NI UN NODO, NI `OPERACIONES.jsonl`, NI LA TABLA. Solo
lee.

USO:
  python scripts/loop/vuelta147_3a_truncacion_dos_unidades.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)

from vuelta146_1c_cifras_ficha_op_a_01 import partir, SEP  # noqa: E402
from vuelta136_simular_ops11 import cargar_tabla  # noqa: E402


def es_31_sola_longitud(grafia):
    """UNIDAD (A). La forma cruda: el titulo mide 31 caracteres exactos."""
    titulo, _ = partir(grafia)
    return len(titulo) == 31


def es_31_detector_vigente(grafia):
    """UNIDAD (B). El detector REGISTRADO: 31 CON RESTO NO VACIO. Es la misma
    condicion que `vuelta131_residuo_para_decision.py:es_truncada`, escrita
    aqui con el particionador de la 146 para que las dos unidades se midan
    sobre EXACTAMENTE la misma particion y la diferencia entre ellas sea solo
    la guarda de RESTO y nunca el troceo."""
    titulo, resto = partir(grafia)
    return len(titulo) == 31 and bool(resto)


def censo_del_catalogo():
    """Grafias distintas del campo `fuente` en CUALQUIER posicion, con nodos
    vivos y deprecados que las declaran. Universo: el grafo de HOY."""
    with io.open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"),
                 encoding="utf-8") as f:
        G = json.load(f)["nodos"]
    vivos, depre = {}, {}
    for n in G.values():
        campo = n.get("fuente")
        if not campo or not isinstance(campo, str):
            continue
        for d in [x.strip() for x in campo.split(SEP) if x.strip()]:
            if n.get("deprecado"):
                depre[d] = depre.get(d, 0) + 1
            else:
                vivos[d] = vivos.get(d, 0) + 1
    todas = sorted(set(vivos) | set(depre))
    return todas, vivos, depre, len(G)


def main():
    todas, vivos, depre, n_nodos = censo_del_catalogo()
    tabla = cargar_tabla()
    canonicas = set(tabla.values())

    print("=" * 78)
    print("LA TRUNCACION A 31, MEDIDA CON LAS DOS UNIDADES. Vuelta 147, TAREA 3.a.")
    print("Relectura AL DOBLE del tramo de la 3.f de la 146 (caida 4.1 del acta 146,")
    print("de CIFRA PUBLICADA y FUERA de lo marcado).")
    print("=" * 78)
    print("")
    print("UNIVERSO 1: dataset/metadata/master_graph.json (WORK), campo `fuente`,")
    print("            TODAS las posiciones, separador ' | '.")
    print("  nodos del grafo: %d" % n_nodos)
    print("  grafias distintas del campo fuente: %d" % len(todas))
    print("")

    filas = []
    unidades = (
        ("A, LA SOLA LONGITUD (len(titulo) == 31)", es_31_sola_longitud),
        ("B, EL DETECTOR VIGENTE (31 CON RESTO NO VACIO)", es_31_detector_vigente),
    )
    for rotulo, criterio in unidades:
        sel = [g for g in todas if criterio(g)]
        vivas = [g for g in sel if vivos.get(g, 0) > 0]
        vivas_y_canon = [g for g in vivas if g in canonicas]
        filas.append((rotulo, sel, vivas, vivas_y_canon))
        print("  UNIDAD %s" % rotulo)
        print("    grafias que la cumplen: %d" % len(sel))
        for g in sel:
            marcas = []
            if vivos.get(g, 0) > 0:
                marcas.append("VIVA")
            if g in canonicas:
                marcas.append("CANONICA")
            print("      %-52s vivos=%-4d depre=%-4d [%s]"
                  % (g, vivos.get(g, 0), depre.get(g, 0),
                     " y ".join(marcas) if marcas else "ni viva ni canonica"))
        print("    de ellas VIVAS (vivos > 0): %d" % len(vivas))
        for g in vivas:
            print("      %s" % g)
        print("    de ellas VIVAS Y CANONICAS de la tabla de OP-S-11: %d" % len(vivas_y_canon))
        for g in vivas_y_canon:
            print("      %s" % g)
        print("")

    sel_a, sel_b = filas[0][1], filas[1][1]
    solo_a = [g for g in sel_a if g not in set(sel_b)]
    print("  LA DIFERENCIA ENTRE LAS DOS UNIDADES, NOMBRADA UNA A UNA: %d grafia(s)"
          % len(solo_a))
    for g in solo_a:
        t, r = partir(g)
        print("      %s  titulo de %d car, RESTO %s"
              % (g, len(t), "VACIO" if not r else r))
    print("")

    print("UNIVERSO 2: docs/plan/OP_S_11_MAPEO_PROPUESTO.md, LA TABLA CANONICA")
    print("            DIRECTAMENTE (camino independiente, no pasa por el grafo).")
    print("  filas grafia a canonica en la tabla: %d" % len(tabla))
    print("  canonicas distintas: %d" % len(canonicas))
    canon_ordenadas = sorted(canonicas)
    can_a = [g for g in canon_ordenadas if es_31_sola_longitud(g)]
    can_b = [g for g in canon_ordenadas if es_31_detector_vigente(g)]
    print("  canonicas con titulo de 31 por LA SOLA LONGITUD: %d" % len(can_a))
    for g in can_a:
        print("      %s" % g)
    print("  canonicas con titulo de 31 por EL DETECTOR VIGENTE: %d" % len(can_b))
    for g in can_b:
        print("      %s" % g)
    print("")

    print("CIFRA grafias distintas del campo fuente WORK: %d grafias" % len(todas))
    print("CIFRA grafias de 31 por la sola longitud WORK: %d grafias" % len(sel_a))
    print("CIFRA grafias de 31 por la sola longitud vivas y canonicas WORK: %d grafias"
          % len(filas[0][3]))
    print("CIFRA grafias de 31 por el detector vigente WORK: %d grafias" % len(sel_b))
    print("CIFRA grafias de 31 por el detector vigente vivas y canonicas WORK: %d grafias"
          % len(filas[1][3]))
    print("CIFRA canonicas distintas de la tabla OP-S-11: %d grafias" % len(canonicas))
    print("CIFRA canonicas de 31 por la sola longitud: %d grafias" % len(can_a))
    print("CIFRA canonicas de 31 por el detector vigente: %d grafias" % len(can_b))
    # LA DIFERENCIA ENTRE LAS DOS UNIDADES TAMBIEN ES UNA CIFRA, y sin su linea
    # `CIFRA` el reporte no la puede publicar cotejada: la guarda de cifras solo
    # sabe cotejar la unidad `grafia` contra una linea de esta forma.
    print("CIFRA grafias que separan las dos unidades: %d grafias" % len(solo_a))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
