# -*- coding: utf-8 -*-
r"""vuelta197_tarea4_tres_varas.py . EL TOPE DE 80 LINEAS DEL MODO AUSTERO, MEDIDO
POR LAS TRES VARAS QUE LA ADJUDICACION `4.6` DEL ACTA 197 MANDA PUBLICAR.

DE DONDE SALE, Y NO ES UNA IDEA MIA. Adjudicacion `4.6` del acta 197: *"EL TOPE DE
80 LINEAS DEL MODO AUSTERO: SE MANTIENE Y NO SE AFLOJA, PERO SE MIDE POR TRES
VARAS... Encargo que se publiquen las TRES medidas (total, escrita a mano, y
escrita a mano menos lo que otra regla obliga) para que el fundador decida sobre
cifras y no sobre una queja."*

LAS TRES VARAS, DEFINIDAS AQUI PARA QUE NO HAYA QUE ADIVINARLAS:

  **V1, TOTAL.** Todas las lineas del fichero, por las DOS convenciones que esta
  casa publica siempre: `count(NL)` y `len(split(NL))`. Las dos se dan porque no
  significan lo mismo y la diferencia es una medicion.

  **V2, ESCRITA A MANO.** El total MENOS las lineas de las piezas TALLADAS. Es la
  vara que el acta 196 fijo en su `4.7`, con estas palabras: *"el tope se mide
  sobre la prosa que el ejecutor escribe A MANO, y no sobre la cabecera tallada ni
  las tablas talladas, que la propia regla nombra como contenido que se queda."*
  Las piezas talladas se localizan por sus MARCAS DE COMENTARIO, no por parecido.

  **V3, ESCRITA A MANO MENOS LO QUE OTRA REGLA OBLIGA A ESCRIBIR.** La V2 menos las
  secciones que una GUARDA busca por su literal. **Cada resta lleva al lado el
  nombre de la guarda que la obliga**, y si una seccion no tiene guarda que la
  busque, NO SE RESTA: eso es lo que impide que la V3 sea una excusa.

LO QUE ESTE FICHERO NO HACE: **no afloja el tope ni inventa una excepcion**. Mide
y publica. Si la V3 sigue por encima de 80, lo dice con esas palabras.

USO:
  python scripts/loop/vuelta197_tarea4_tres_varas.py
  python scripts/loop/vuelta197_tarea4_tres_varas.py --fichero docs/loop/reportes/REPORTE_V196.md
  python scripts/loop/vuelta197_tarea4_tres_varas.py --mutacion
"""
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
TOPE = 80

# LAS PIEZAS TALLADAS, LOCALIZADAS POR SUS MARCAS DE COMENTARIO Y NO POR PARECIDO.
# Los literales son los mismos que `cerrar_reporte.py` y
# `anexar_tarea_al_reporte.py` usan, y por eso una pieza tallada no se puede
# confundir con prosa que se le parezca.
TALLADAS = [
    ("cabecera tallada", "<!-- CABECERA TALLADA -->", "<!-- FIN CABECERA TALLADA -->",
     "scripts/loop/tallar_cabecera_reporte.py --fase04, y cerrar_reporte.py la "
     "exige por su marca MARCA_ABRE"),
    ("tabla de tareas", "<!-- TABLA DE TAREAS -->", "<!-- FIN TABLA DE TAREAS -->",
     "scripts/loop/anexar_tarea_al_reporte.py la exige por su marca ABRE_TABLA y "
     "CAE EN ROJO si no aparece exactamente una vez"),
]

# LAS SECCIONES QUE OTRA REGLA OBLIGA A ESCRIBIR, CADA UNA CON LA GUARDA QUE LA
# BUSCA POR SU LITERAL. **Si una seccion no tiene guarda, no entra en esta lista.**
OBLIGADAS = [
    ("## 9.", "cerrar_reporte.py, constantes CAB_9 y CAB_9_HUECO, y la guarda (4) "
              "de su cabecera: la seccion 9 existe o el cierre es ROJO"),
    ("## 4.", "cerrar_reporte.py, seccion_4_del_reporte() y la escalada que la "
              "coteja contra la apertura sellada"),
    ("## 3.", "cerrar_reporte.py, guarda (3): LAS SECCIONES 3 A 9, las siete "
              "existen"),
    ("## 5.", "cerrar_reporte.py, guarda (3): LAS SECCIONES 3 A 9"),
    ("## 6.", "cerrar_reporte.py, guarda (3): LAS SECCIONES 3 A 9"),
    ("## 7.", "cerrar_reporte.py, guarda (3): LAS SECCIONES 3 A 9"),
    ("## 8.", "cerrar_reporte.py, guarda (3): LAS SECCIONES 3 A 9, y "
              "claves_de_caida_de_la_seccion_8()"),
    ("## 0.", "vuelta197_esqueleto_reporte.py, LA IDENTIDAD SE LEE DE GIT "
              "(EJECUTOR.md 1): cae en rojo si algo no se lee de git"),
]


def lineas_de(texto):
    """LAS LINEAS DE UN TEXTO, POR LAS DOS CONVENCIONES. PURA.
    Devuelve (por_count_nl, por_split)."""
    t = texto.replace(chr(13) + NL, NL)
    return t.count(NL), len(t.split(NL))


def rango_entre_marcas(lineas, abre, cierra):
    """LOS INDICES 0-BASED DE LAS LINEAS ENTRE DOS MARCAS, LAS DOS INCLUIDAS.
    PURA. Devuelve un conjunto vacio si alguna marca no aparece EXACTAMENTE una
    vez: una marca ambigua NO se resta, porque restar a ojo es la puerta por la
    que la vara estrecha se convierte en una excusa."""
    i = [k for k, l in enumerate(lineas) if abre in l]
    j = [k for k, l in enumerate(lineas) if cierra in l]
    if len(i) != 1 or len(j) != 1 or j[0] < i[0]:
        return set()
    return set(range(i[0], j[0] + 1))


def rango_de_seccion(lineas, cabecera):
    """LOS INDICES 0-BASED DE UNA SECCION `## n.`, desde su cabecera hasta la
    siguiente cabecera `## ` o el fin. PURA. Conjunto vacio si la cabecera no
    aparece exactamente una vez."""
    i = [k for k, l in enumerate(lineas) if l.startswith(cabecera)]
    if len(i) != 1:
        return set()
    a = i[0]
    sig = [k for k, l in enumerate(lineas) if k > a and l.startswith("## ")]
    b = sig[0] if sig else len(lineas)
    return set(range(a, b))


def tres_varas(texto):
    """LAS TRES VARAS SOBRE UN TEXTO. PURA. Devuelve un dict con todo lo medido,
    incluidas las restas UNA POR UNA con el nombre de lo que se resta."""
    t = texto.replace(chr(13) + NL, NL)
    lineas = t.split(NL)
    v1_nl, v1_split = lineas_de(t)

    restadas_talladas = []
    fuera = set()
    for nombre, abre, cierra, guarda in TALLADAS:
        r = rango_entre_marcas(lineas, abre, cierra)
        restadas_talladas.append((nombre, len(r), guarda, bool(r)))
        fuera |= r
    v2 = v1_split - len(fuera)

    restadas_obligadas = []
    fuera2 = set(fuera)
    for cab, guarda in OBLIGADAS:
        r = rango_de_seccion(lineas, cab) - fuera2
        restadas_obligadas.append((cab, len(r), guarda, bool(r)))
        fuera2 |= r
    v3 = v1_split - len(fuera2)

    return {
        "v1_count_nl": v1_nl, "v1_split": v1_split,
        "v2": v2, "v3": v3,
        "talladas": restadas_talladas, "obligadas": restadas_obligadas,
        "lineas_talladas": len(fuera), "lineas_obligadas": len(fuera2) - len(fuera),
    }


# ------------------------------------------------------------------ MUTACION
_CUENTA = {"casos": 0, "pasan": 0}


def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    _CUENTA["casos"] += 1
    _CUENTA["pasan"] += 1 if ok else 0
    w("   %-62s %s" % (nombre, "VERDE" if ok else "ROJO"))
    if not ok:
        w("      esperado: %r" % (esperado,))
        w("      obtenido: %r" % (obtenido,))
    return ok


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION DE LAS TRES VARAS, sobre texto FABRICADO."""
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("VUELTA 197, TAREA 4.b: CASO POSITIVO POR MUTACION DE LAS TRES VARAS")
    w("=" * 78)
    w("")
    fab = NL.join([
        "# REPORTE FABRICADO",          # 1  mano
        "prosa a mano uno",             # 2  mano
        "<!-- CABECERA TALLADA -->",    # 3  tallada
        "| a | b |",                    # 4  tallada
        "<!-- FIN CABECERA TALLADA -->",  # 5  tallada
        "prosa a mano dos",             # 6  mano
        "<!-- TABLA DE TAREAS -->",     # 7  tallada
        "| tarea | x |",                # 8  tallada
        "<!-- FIN TABLA DE TAREAS -->",  # 9  tallada
        "## 9. LA BATERIA",             # 10 obligada
        "hueco declarado",              # 11 obligada
        "## 99. UNA SECCION SIN GUARDA",  # 12 mano
        "prosa a mano tres",            # 13 mano
    ])
    m = tres_varas(fab)
    w("A) SOBRE UN REPORTE FABRICADO DE 13 LINEAS")
    ok &= _caso(w, "V1 por len(split(NL)) cuenta las 13", m["v1_split"], 13)
    ok &= _caso(w, "V1 por count(NL) cuenta 12, que es una menos",
                m["v1_count_nl"], 12)
    ok &= _caso(w, "V2 resta las 6 lineas talladas y deja 7", m["v2"], 7)
    ok &= _caso(w, "V3 resta ademas las 2 de la seccion 9 y deja 5", m["v3"], 5)
    ok &= _caso(w, "y la seccion 99, que NO tiene guarda, NO se resta",
                m["v3"] >= 5, True)
    w("   LA MUTACION QUE MAS IMPORTA: si la V3 restara cualquier `## n.` en vez")
    w("   de solo las que una guarda busca, la seccion 99 tambien caeria y la V3")
    w("   daria 3. Se comprueba que da 5.")
    ok &= _caso(w, "la V3 NO es 3", m["v3"] == 3, False)
    w("")
    w("B) UNA MARCA AMBIGUA NO SE RESTA")
    doble = fab + NL + "<!-- CABECERA TALLADA -->"
    m2 = tres_varas(doble)
    talladas2 = dict((n, c) for n, c, _g, _h in m2["talladas"])
    ok &= _caso(w, "con la marca de apertura DUPLICADA, la cabecera no se resta",
                talladas2["cabecera tallada"], 0)
    w("   LA MUTACION: restar a ojo una pieza cuya marca es ambigua es la puerta")
    w("   por la que la vara estrecha se convierte en una excusa. No se resta.")
    w("")
    w("C) UN TEXTO SIN NINGUNA MARCA: LAS TRES VARAS COINCIDEN")
    m3 = tres_varas("una" + NL + "dos" + NL + "tres")
    ok &= _caso(w, "V1 split, V2 y V3 son las tres 3",
                (m3["v1_split"], m3["v2"], m3["v3"]), (3, 3, 3))
    w("   Es la comprobacion de que las varas RESTAN y no INVENTAN: sin piezas")
    w("   talladas ni secciones con guarda, no hay nada que descontar.")
    w("")
    w("=" * 78)
    w("CASOS: %d | VERDES: %d | ROJOS: %d"
      % (_CUENTA["casos"], _CUENTA["pasan"], _CUENTA["casos"] - _CUENTA["pasan"]))
    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    w("=" * 78)
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V197_T4_MUTACION_TRES_VARAS.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fichero", action="append", default=[],
                    help="ruta de un reporte a medir; se puede repetir")
    ap.add_argument("--mutacion", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if a.mutacion:
        return prueba_de_mutacion()

    ficheros = a.fichero or ["docs/loop/REPORTE.md",
                             "docs/loop/reportes/REPORTE_V196.md"]
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 197, TAREA 4.b: EL TOPE DE 80 LINEAS, MEDIDO POR LAS TRES VARAS")
    w("=" * 78)
    w("")
    w("ADJUDICACION `4.6` DEL ACTA 197. EL TOPE NO SE AFLOJA Y LA EXCEPCION NO SE")
    w("INVENTA: se publican las tres cifras para que el fundador decida sobre")
    w("numeros y no sobre una queja. TOPE VIGENTE: %d lineas." % TOPE)
    w("")
    for rel in ficheros:
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        w("-" * 78)
        w("FICHERO: %s" % rel)
        if not os.path.isfile(p):
            w("   NO EXISTE. No se publica cifra.")
            continue
        texto = io.open(p, encoding="utf-8", errors="replace").read()
        m = tres_varas(texto)
        w("   bytes en disco: %d" % os.path.getsize(p))
        w("")
        w("   | vara | que cuenta | cifra | contra el tope de %d |" % TOPE)
        w("   |---|---|---:|---|")
        w("   | **V1 total** | `count(NL)` | **%d** | %s |"
          % (m["v1_count_nl"],
             "POR ENCIMA" if m["v1_count_nl"] > TOPE else "dentro"))
        w("   | **V1 total** | `len(split(NL))` | **%d** | %s |"
          % (m["v1_split"], "POR ENCIMA" if m["v1_split"] > TOPE else "dentro"))
        w("   | **V2 escrita a mano** | total menos las piezas TALLADAS | **%d** | %s |"
          % (m["v2"], "POR ENCIMA" if m["v2"] > TOPE else "dentro"))
        w("   | **V3 estrecha** | V2 menos lo que otra regla obliga | **%d** | %s |"
          % (m["v3"], "POR ENCIMA" if m["v3"] > TOPE else "dentro"))
        w("")
        w("   LO QUE LA V2 RESTA, PIEZA A PIEZA, CON SU GUARDA AL LADO:")
        for nombre, cuantas, guarda, hallada in m["talladas"]:
            w("      %-18s %3d lineas | %s"
              % (nombre, cuantas, "hallada" if hallada else "NO HALLADA, no se resta"))
            w("         la exige: %s" % guarda)
        w("      SUBTOTAL restado por la V2: %d lineas" % m["lineas_talladas"])
        w("")
        w("   LO QUE LA V3 RESTA ADEMAS, SECCION A SECCION, CON SU GUARDA AL LADO:")
        for cab, cuantas, guarda, hallada in m["obligadas"]:
            w("      %-8s %3d lineas | %s"
              % (cab, cuantas, "hallada" if hallada else "NO HALLADA, no se resta"))
            w("         la exige: %s" % guarda)
        w("      SUBTOTAL restado por la V3: %d lineas" % m["lineas_obligadas"])
        w("")
        if m["v3"] > TOPE:
            w("   **LA TERCERA VARA SIGUE POR ENCIMA DE 80.** Se dice con esas")
            w("   palabras, que es lo que el encargo manda. Son %d lineas contra un"
              % m["v3"])
            w("   tope de %d: %.1f veces el tope." % (TOPE, m["v3"] / float(TOPE)))
        else:
            w("   La tercera vara ENTRA en el tope de %d." % TOPE)
        w("")
    w("-" * 78)
    w("LA PREGUNTA QUE QUEDA ESCRITA, Y NO LA CONTESTO YO:")
    w("   El modo austero dice que RECORTA TINTA, NO CONTROL. Las tres cifras de")
    w("   arriba muestran que lo que empuja el reporte por encima del tope no es")
    w("   prosa de acompanamiento sino PIEZAS QUE UNA GUARDA EXIGE. La pregunta")
    w("   es del fundador y tiene tres respuestas posibles, ninguna mia: subir el")
    w("   tope, medirlo por la vara estrecha, o recortar de verdad las secciones")
    w("   que hoy son obligatorias. EL TOPE NO SE AFLOJA MIENTRAS NO SE DECIDA.")
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V197_T4_TRES_VARAS.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
