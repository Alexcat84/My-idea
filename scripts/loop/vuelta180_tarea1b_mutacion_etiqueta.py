# -*- coding: utf-8 -*-
r"""vuelta180_tarea1b_mutacion_etiqueta.py . EL CASO POSITIVO POR MUTACION DE LA
ETIQUETA DE FUENTE: SI LA ETIQUETA VUELVE A QUEDARSE CLAVADA EN UN LITERAL, ESTE
CASO CAE.

TAREA 1.b de la vuelta 180. Sujeto: `clases_por_par()` y `etiqueta_del_registro()`
de `scripts/loop/vuelta178_tarea3_anotar_triangulos.py`.

SUJETO CONGELADO, y se dice como: este arnes NO ABRE NINGUN FICHERO VIVO DE LA
CAMPANA. Fabrica su propio registro de lecturas en un TEMPORAL, con dos filas
escritas por DOS VUELTAS DISTINTAS, le pasa una lista de veredictos VACIA y un
mapa de alias VACIO, y lo retira al terminar (`P.16`, quien fabrica limpia). No
lee `docs/plan/OP_L_03_LECTURAS.jsonl` ni el archivo de veredictos ni el grafo.

QUE PRUEBA, Y POR QUE ESE ES EL CASO QUE HABIA QUE FABRICAR. Hasta la vuelta 179
la etiqueta de fuente de toda clase venida del registro era el LITERAL
`docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)`, clavado cuando la 177 era la
unica vuelta que habia escrito ahi. En cuanto una segunda vuelta escribio, sus
clases salieron atribuidas a la 177: cinco lados falsos, medidos por
`scripts/loop/vuelta179_tarea3_etiqueta_de_fuente.py`. **Un registro de UNA SOLA
vuelta no puede destapar eso**, porque con una sola vuelta el literal acierta por
casualidad. Por eso el registro fabricado tiene DOS vueltas: es la unica forma de
que el caso pueda caer.

LOS DOS CASOS, Y LOS DOS CORREN:

  CASO 1, VERDE ESPERADO. Con el codigo de hoy, el lado escrito por la vuelta
  `177` sale etiquetado `(vuelta 177)` y el escrito por la `180` sale
  `(vuelta 180)`. Las DOS etiquetas son DISTINTAS.

  CASO 2, LA MUTACION, ROJO ESPERADO. Se sustituye `etiqueta_del_registro` por
  una version CLAVADA que devuelve siempre el literal de la 177, que es
  exactamente el codigo que habia antes de esta vuelta. Con esa mutacion puesta,
  las dos etiquetas salen IGUALES y el caso CAE.

Y LA MUTACION SE DESHACE SIEMPRE, en `finally`: este arnes no puede dejar el
modulo tocado para quien lo importe despues.

USO:
  python scripts/loop/vuelta180_tarea1b_mutacion_etiqueta.py
"""
import io
import json
import os
import shutil
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import vuelta178_tarea3_anotar_triangulos as S   # noqa: E402

NL = chr(10)
LITERAL_CLAVADO = "docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)"

# EL REGISTRO FABRICADO. Dos filas, dos vueltas, un par cada una.
FABRICADO = [
    {"id_op": "OP-FABRICADA", "vuelta": 177, "acto": "acto_de_la_177",
     "clases_de_los_pares_por_leer": {
         "nodo_viejo_a|nodo_viejo_b": ["A", "razon fabricada de la 177"]}},
    {"id_op": "OP-FABRICADA", "vuelta": 180, "acto": "acto_de_la_180",
     "clases_de_los_pares_por_leer": {
         "nodo_nuevo_a|nodo_nuevo_b": ["D", "razon fabricada de la 180"]}},
]


def escribir_registro(carpeta):
    """Escribe el registro fabricado y devuelve su ruta. Solo toca el temporal."""
    ruta = os.path.join(carpeta, "REGISTRO_FABRICADO.jsonl")
    with io.open(ruta, "w", encoding="utf-8", newline=NL) as f:
        for fila in FABRICADO:
            f.write(json.dumps(fila, ensure_ascii=False) + NL)
    return ruta


def etiquetas_del_registro_fabricado(ruta):
    """{par: etiqueta de fuente} corriendo el sujeto sobre el registro fabricado.

    Mapa de alias VACIO y veredictos VACIOS: nada vivo entra aqui."""
    idx = S.clases_por_par({}, lecturas=ruta, filas=[])
    salida = {}
    for clave, entrada in idx.items():
        salida["|".join(sorted(clave))] = entrada["fuente"]
    return salida


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    carpeta = tempfile.mkdtemp(prefix="v180_t1b_")
    fallos = []
    try:
        ruta = escribir_registro(carpeta)
        p("=" * 78)
        p("CASO POSITIVO POR MUTACION DE LA ETIQUETA DE FUENTE (vuelta 180, 1.b)")
        p("=" * 78)
        p("")
        p("EL SUJETO FABRICADO, Y NO HAY NINGUN FICHERO VIVO EN ESTE ARNES")
        p("   registro fabricado: %s" % ruta)
        p("   CIFRA filas: %d" % len(FABRICADO))
        for fila in FABRICADO:
            p("      vuelta %s -> %s"
              % (fila["vuelta"], ", ".join(fila["clases_de_los_pares_por_leer"])))
        p("")

        p("CASO 1, EL CODIGO DE HOY. LAS DOS ETIQUETAS TIENEN QUE SER DISTINTAS")
        hoy = etiquetas_del_registro_fabricado(ruta)
        for k in sorted(hoy):
            p("   %-36s -> %s" % (k, hoy[k]))
        distintas = len(set(hoy.values())) == 2
        p("   CIFRA etiquetas distintas: %d (se esperan 2)" % len(set(hoy.values())))
        esperado_177 = S.etiqueta_del_registro(177)
        esperado_180 = S.etiqueta_del_registro(180)
        p("   la del lado de la 177 dice %r" % esperado_177)
        p("   la del lado de la 180 dice %r" % esperado_180)
        bien_177 = hoy.get("nodo_viejo_a|nodo_viejo_b") == esperado_177
        bien_180 = hoy.get("nodo_nuevo_a|nodo_nuevo_b") == esperado_180
        p("   el lado de la 177 lleva su etiqueta: %s" % ("SI" if bien_177 else "NO"))
        p("   el lado de la 180 lleva su etiqueta: %s" % ("SI" if bien_180 else "NO"))
        if not (distintas and bien_177 and bien_180):
            fallos.append("CASO 1: el codigo de hoy NO etiqueta cada lado con su vuelta")
        p("   VEREDICTO CASO 1: %s"
          % ("VERDE" if (distintas and bien_177 and bien_180) else "ROJO"))
        p("")

        p("CASO 2, LA MUTACION: LA ETIQUETA VUELVE A QUEDARSE CLAVADA EN UN LITERAL")
        p("   (es literalmente el codigo que habia antes de la vuelta 180)")
        original = S.etiqueta_del_registro
        try:
            S.etiqueta_del_registro = lambda _vuelta: LITERAL_CLAVADO
            mutado = etiquetas_del_registro_fabricado(ruta)
        finally:
            S.etiqueta_del_registro = original
        for k in sorted(mutado):
            p("   %-36s -> %s" % (k, mutado[k]))
        p("   CIFRA etiquetas distintas con la mutacion puesta: %d (se espera 1)"
          % len(set(mutado.values())))
        cae = len(set(mutado.values())) == 1
        p("   EL CASO CAE CON LA MUTACION PUESTA: %s" % ("SI" if cae else "NO"))
        if not cae:
            fallos.append("CASO 2: con la etiqueta clavada el caso NO cae, o sea "
                          "que este arnes no puede fallar y no prueba nada")
        p("   VEREDICTO CASO 2: %s" % ("VERDE" if cae else "ROJO"))
        p("")

        p("LA MUTACION QUEDA DESHECHA, COMPROBADO Y NO PROMETIDO")
        p("   etiqueta_del_registro(177) tras deshacer: %r"
          % S.etiqueta_del_registro(177))
        p("   etiqueta_del_registro(180) tras deshacer: %r"
          % S.etiqueta_del_registro(180))
        if S.etiqueta_del_registro(180) == LITERAL_CLAVADO:
            fallos.append("la mutacion NO se deshizo")
        p("")
    finally:
        shutil.rmtree(carpeta, ignore_errors=True)
        p("EL TEMPORAL, RETIRADO (P.16): %s -> existe: %s"
          % (carpeta, "SI" if os.path.exists(carpeta) else "NO"))
        p("")

    if fallos:
        p("ROJO: %d fallo(s)." % len(fallos))
        for f in fallos:
            p("   " + f)
        p("FIN")
        return 1
    p("VERDE: los DOS casos pasan. Con el codigo de hoy cada lado lleva la vuelta "
      "que de verdad lo escribio, y con la etiqueta clavada en un literal el caso "
      "CAE. La prueba de mutacion esta corrida, no prometida.")
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
