# -*- coding: utf-8 -*-
"""VUELTA 21, TAREA 1: los cinco registros de las adjudicaciones del acta de la vuelta 20.

Los cinco son ADITIVOS y de una linea o una celda: NINGUN texto viejo se borra ni
se reescribe. Las cifras que escriben salen de `scripts/loop/vuelta21_registros.py`
corrido en esta misma vuelta, no del acta ni de un reporte anterior; el acta se
cita como adjudicacion, que es lo que es.

  1. docs/plan/01_FUENTES.md, celda de `decision_de_vender_startup` en la tabla
     LOS TRES CASOS QUE NO SON UN SIMPLE APENDICE: manda el 34, el 25 era parcial
     de nacimiento. La cifra vieja y su tramo quedan enteros.
  2. docs/plan/01_FUENTES.md, subseccion de la vuelta 20: la nomina de los 13 SI
     existe y el que sobra es `principio_calidad_mvp`. La frase vieja queda entera.
  3. docs/plan/OPERACIONES.jsonl, `OP-F-04-HOR`: aviso al FINAL del campo `nota`.
     El campo `nodos` NO se toca.
  4. docs/plan/OPERACIONES.jsonl, `OP-S-11`: segundo ejemplar al FINAL del `nota`.
  5. docs/plan/RECOMPUTO_3388.md, final de la seccion TAREA (vuelta 20): dos
     lineas aditivas, la fila 7 adjudicada y la FASE II cerrada.

Idempotente: si el ancla ya no esta o el registro ya esta puesto, lo dice y no
escribe. Cero guiones largos y cero guiones medios.
"""
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[2]
FUENTES = RAIZ / "docs" / "plan" / "01_FUENTES.md"
OPS = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"
RECOMPUTO = RAIZ / "docs" / "plan" / "RECOMPUTO_3388.md"

# ---------------------------------------------------------------------------
# 1. LA CELDA DE LA FILA 7
# ---------------------------------------------------------------------------
ANCLA_CELDA = ("y el material repetido tres veces: los pasos 11 a 15, 16 a 20 y 21 a 25 "
               "vuelven sobre el precio minimo y la disposicion del equipo |")

CELDA = (ANCLA_CELDA[:-1] +
         ". **CORRECCION DECLARADA ADITIVA, 14 ago 2026 (vuelta 21): MANDA EL 34, y el 25 y su "
         "tramo se quedan enteros arriba.** Adjudicada por el acta de la vuelta 20 del auditor "
         "(seccion 4, punto 1), **que la midio con git**: el blob de "
         "`dataset/metadata/master_graph.json` es IDENTICO en `0e5e0c60` (9 ago, ultimo commit que "
         "toca el grafo), en `23f9ac32` (11 ago, el commit que CREA este archivo) y en HEAD, asi "
         "que **el nodo YA tenia 34 pasos el 11 ago: el 25 era PARCIAL DE NACIMIENTO, no un nodo "
         "que crecio**. Reproducido hoy con instrumento propio "
         "(`scripts/loop/vuelta21_registros.py`): **34** pasos en el grafo de hoy, **34** leidos "
         "del blob de `23f9ac32`, y los tres blobs con la misma firma `bb423c06`. **La frontera "
         "vigente (1 a 10 / 11 a 34) ya esta impresa en la tabla de la vuelta 20 de este archivo "
         "y se CITA, no se recuenta; el caracter del hallazgo (no es un simple apendice) queda.** |")

# ---------------------------------------------------------------------------
# 2. LA NOMINA DE LOS 13
# ---------------------------------------------------------------------------
ANCLA_NOMINA = ("salida de `scripts/loop/vuelta20_horowitz.py`; aqui va el saldo de la lectura.\n")

NOMINA = ANCLA_NOMINA + """
> **CORRECCION DECLARADA ADITIVA, 14 ago 2026 (vuelta 21), y las dos frases de arriba se quedan
> ENTERAS: LA NOMINA DE LOS 13 SI ESTA ESCRITA, y SI se puede decir cual sobra.** Vive en
> [`OPERACIONES.jsonl`](OPERACIONES.jsonl), **campo `nodos` de `OP-F-04-HOR`** (fecha_corte
> 2026-08-11, adjudicacion *LEIDOS LOS 13*). **El que sobra es `principio_calidad_mvp`**: medido
> hoy con `scripts/loop/vuelta21_registros.py`, los **14** del grafo menos los **13** de la
> operacion dan exactamente ese nodo, y **ninguno de los 13 falta en el grafo**. No queda
> descubierto: barridas hoy las **71** operaciones, `principio_calidad_mvp` esta en el campo
> `nodos` de **TRES** (`OP-F-03`, el bloque de Hugos; `OP-D-01`, su destejido entero; y tambien
> `OP-D-06`, que el acta no nombra). **Lo de arriba fue una BUSQUEDA NEGATIVA CITADA**, la especie
> que la doctrina prohibe, **y se declara aqui sin borrar la frase que la contiene**. Adjudicado en
> el acta de la vuelta 20 del auditor, secciones 1 y 5.
"""

# ---------------------------------------------------------------------------
# 3 y 4. LOS DOS CAMPOS `nota` DE OPERACIONES.jsonl
# ---------------------------------------------------------------------------
NOTA_HOR = (
    " AVISO DECLARADO 14 ago 2026 (vuelta 21), y la adjudicacion de arriba se queda entera: esa "
    "prosa dice que el bloque esta AL FINAL de los pasos, y medido en la vuelta 20 uno de estos "
    "13, metas_vs_proposito, tiene el bloque de Horowitz EN MEDIO porque Coleman cierra. Remedido "
    "hoy con scripts/loop/vuelta21_registros.py por la posicion del campo fuente: Horowitz en "
    "posicion 2 de 3 y el ultimo declarado es Never Lose a Customer Again, y es el UNICO de los 13 "
    "en ese caso. LA PRESENCIA 13 DE 13 QUEDA INTACTA y el campo nodos no se toca; el reparto por "
    "nodo con su frontera leida esta en 01_FUENTES.md, seccion LA NOMINA DE LOS 14 DE HOROWITZ "
    "(tabla de la vuelta 20). Adjudicado en el acta de la vuelta 20, seccion 4, pregunta 2.")

NOTA_S11 = (
    " SEGUNDO EJEMPLAR DECLARADO 14 ago 2026 (vuelta 21), y el texto de arriba no se corrige "
    "porque no afirmaba ser exhaustivo: el nodo que declara el mismo libro dos veces con dos "
    "grafias no es UNO sino DOS en la tanda de los cuatro libros, decision_de_vender_startup y "
    "plan_mejora_procesos (The Hard Thing About Hard Things y The Hard Thing About Hard Thing), y "
    "FUERA de la tanda hay DOS de Hugos con la grafia truncada en el mismo nodo, asociaciones_clave "
    "y transicion_producto_a_experiencia (Essentials of Supply Chain Management y Essentials of "
    "Supply Chain Mana), que son de la especie truncada que esta operacion ya documenta. Medidos en "
    "las vueltas 20 y 21 del bucle (el segundo par, por el auditor en el acta de la vuelta 20, "
    "seccion 1) y los cuatro remedidos hoy sobre los 3.521 vivos con "
    "scripts/loop/vuelta21_registros.py, que no encuentra ningun otro.")

# ---------------------------------------------------------------------------
# 5. EL CIERRE EN RECOMPUTO_3388.md
# ---------------------------------------------------------------------------
CIERRE = """
> **ADJUDICADA, 14 ago 2026 (vuelta 21), y nada de lo de arriba se toca: LA FILA 7 QUEDO
> ADJUDICADA por el acta de la vuelta 20 del auditor (seccion 4, punto 1), MANDA EL 34**, y el
> conteo viejo era **PARCIAL DE NACIMIENTO** y no un nodo que crecio: el auditor lo midio con git
> (el blob del grafo es identico en `0e5e0c60`, en `23f9ac32` y en HEAD) y esta vuelta lo
> reproduce con `scripts/loop/vuelta21_registros.py` (34 pasos hoy, 34 en el blob del 11 ago, los
> tres blobs `bb423c06`). El registro aditivo esta puesto en la celda de `01_FUENTES.md`. **CON
> ESTO LA LISTA DE CIFRAS PUBLICADAS CON DOS LECTURAS QUEDA VACIA.**

> **Y LA FASE II QUEDA CERRADA por esa misma acta (seccion 8), CON LA FASE III ABIERTA en la rama
> `pasada-unica`**, creada desde `bucle` por el auditor: el trabajo de la FASE III, los reportes y
> las actas viven ahi, `bucle` queda como registro de las fases I y II, y **el merge sigue siendo
> decision de Alexis**. La medicion de la FASE II que esta seccion publica **no se recomputa aqui**:
> se cita con su corte del 14 ago 2026.
"""


def escribir(ruta, viejo, nuevo, rotulo):
    texto = ruta.read_text(encoding="utf-8")
    if nuevo in texto:
        print("  [YA ESTABA] %s" % rotulo)
        return False
    if texto.count(viejo) != 1:
        print("  [PARADA] %s: el ancla aparece %d veces, no una" % (rotulo, texto.count(viejo)))
        return None
    ruta.write_text(texto.replace(viejo, nuevo), encoding="utf-8")
    print("  [ESCRITO]  %s  (+%d caracteres, cero borrados)" % (rotulo, len(nuevo) - len(viejo)))
    return True


def anadir_a_nota(id_op, adicion, rotulo):
    lineas = OPS.read_text(encoding="utf-8").split("\n")
    tocadas = 0
    for i, linea in enumerate(lineas):
        if not linea.strip():
            continue
        o = json.loads(linea)
        if o["id_op"] != id_op:
            continue
        if adicion.strip() in (o.get("nota") or ""):
            print("  [YA ESTABA] %s" % rotulo)
            return False
        largo_viejo = len(o.get("nota") or "")
        o["nota"] = (o.get("nota") or "") + adicion
        lineas[i] = json.dumps(o)
        tocadas += 1
        print("  [ESCRITO]  %s  (nota de %d a %d caracteres; campo nodos intacto: %d ids)" % (
            rotulo, largo_viejo, len(o["nota"]), len(o.get("nodos") or [])))
    if tocadas != 1:
        print("  [PARADA] %s: %d lineas con ese id_op" % (rotulo, tocadas))
        return None
    OPS.write_text("\n".join(lineas), encoding="utf-8")
    return True


def anadir_al_final(ruta, adicion, rotulo, cola_esperada):
    """Aditivo puro: pega al final del archivo, tras comprobar donde acaba."""
    texto = ruta.read_text(encoding="utf-8")
    if adicion.strip() in texto:
        print("  [YA ESTABA] %s" % rotulo)
        return False
    if not texto.rstrip().endswith(cola_esperada):
        print("  [PARADA] %s: el archivo NO acaba donde el encargo dice" % rotulo)
        return None
    ruta.write_text(texto.rstrip("\n") + "\n" + adicion, encoding="utf-8")
    print("  [ESCRITO]  %s  (+%d caracteres al final, cero borrados)" % (rotulo, len(adicion)))
    return True


COLA_RECOMPUTO = "NO creo `pasada-unica` y NO corrio el Gate 0.**"


def main():
    print("VUELTA 21, TAREA 1: los cinco registros del acta de la vuelta 20")
    print()
    r = [
        escribir(FUENTES, ANCLA_CELDA, CELDA, "1. celda de la fila 7 en 01_FUENTES.md"),
        escribir(FUENTES, ANCLA_NOMINA, NOMINA, "2. la nomina de los 13 en 01_FUENTES.md"),
        anadir_a_nota("OP-F-04-HOR", NOTA_HOR, "3. nota de OP-F-04-HOR"),
        anadir_a_nota("OP-S-11", NOTA_S11, "4. nota de OP-S-11"),
        anadir_al_final(RECOMPUTO, CIERRE.lstrip("\n"), "5. el cierre en RECOMPUTO_3388.md",
                        COLA_RECOMPUTO),
    ]
    print()
    if None in r:
        print("HAY UNA PARADA: algun ancla no calzo. NADA se da por escrito.")
        return 1
    print("LOS CINCO REGISTROS, PUESTOS. Cero borrados, cero reescrituras.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
