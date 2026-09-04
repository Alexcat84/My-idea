# -*- coding: utf-8 -*-
r"""vuelta166_tarea5b_frontera_ld07.py . TAREA 5 de la vuelta 166, segunda
escritura: LA FRONTERA QUE `LD-07` DEJO ESCRITA Y QUE HOY YA NO SEPARA NADA.

QUE ANOTA. `LD-07` cierra con una frontera: *"la reunion de conclusion y la
encuesta no son lo mismo"*. **Los dos nodos que esa frase separa son HOY el
mismo nodo**, porque `encuesta_satisfaccion_postproyecto` resuelve a
`reunion_conclusion_proyecto`. La anotacion se escribe DONDE `LD-07` VIVE, POR
ADICION Y CON SU FECHA, que es la letra del encargo.

NO SE BORRA NI UNA LETRA de `LD-07`, y la frase de la frontera se CITA entera:
era cierta el dia que se escribio y sigue siendo la lectura de aquel dia. Lo
que cambio no es la lectura: es el grafo debajo de ella.

Y NO SE ADJUDICA NADA. La `D` de `LD-07` no se mueve, la `A DE BLOQUE` de
`LD-06` tampoco, y no se declara cual de las dos manda. La adjudicacion 5.14 lo
dice con esas palabras: la clase la decide una lectura, no un colapso.

EL RESOLUTOR SE IMPORTA de la TAREA 2 y la coincidencia se MIDE aqui: si los dos
ids NO resolvieran al mismo nodo, este instrumento PARA en vez de anotar una
fusion que no existe.

IDEMPOTENTE: si el bloque ya esta, no escribe.

USO:
  python scripts/loop/vuelta166_tarea5b_frontera_ld07.py            (mide, NO escribe)
  python scripts/loop/vuelta166_tarea5b_frontera_ld07.py --aplicar  (mide y escribe)
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta166_tarea2_correccion_op_l_01 as T2   # noqa: E402

RAIZ = T2.RAIZ
DOC = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")

CABECERA_LD07 = "### `LD-07` . `project_close_out` contra `encuesta_satisfaccion_postproyecto`"
FRONTERA = ("> **CONTINUA.** Y deja una frontera util entre los dos nodos de "
            "Coleman: **la")
MARCA = "> **LA FRONTERA DE ARRIBA YA NO SEPARA DOS NODOS (4 sep 2026, vuelta 166"

A = "reunion_conclusion_proyecto"
B = "encuesta_satisfaccion_postproyecto"


def main(aplicar):
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 166, TAREA 5b: LA FRONTERA DE LD-07, ANOTADA POR ADICION")
    print("=" * 78)
    print("")

    mapa, _n = T2.mapa_de_alias()
    ra, rb = T2.resolver(mapa, A), T2.resolver(mapa, B)
    print("A) LA COINCIDENCIA SE MIDE, NO SE HEREDA DEL ACTA")
    print("   %s resuelve a %s" % (A, ra))
    print("   %s resuelve a %s" % (B, rb))
    print("   los dos nodos que la frontera separa son HOY el mismo: %s" % (ra == rb))
    if ra != rb:
        print("   PARADA: no resuelven al mismo nodo. No se anota una fusion que")
        print("   la medicion de hoy no ve.")
        return 1
    print("")

    texto = io.open(DOC, encoding="utf-8").read()
    lineas = texto.split("\n")
    print("B) LA IDEMPOTENCIA, ANTES QUE NADA")
    if MARCA in texto:
        print("   YA ESTABA: la anotacion vive en el documento.")
        print("   CIFRA bloques escritos: 0")
        return 0
    print("   la marca no esta: se puede seguir.")
    print("")

    print("C) DONDE VIVE LD-07 Y DONDE VIVE SU FRONTERA")
    cab = [i for i, l in enumerate(lineas, 1) if l.startswith(CABECERA_LD07)]
    print("   CIFRA veces que la cabecera de LD-07 aparece: %d" % len(cab))
    if len(cab) != 1:
        print("   PARADA: la cabecera no es unica.")
        return 1
    n_cab = cab[0]
    fr = [i for i, l in enumerate(lineas, 1) if l.startswith(FRONTERA)]
    print("   CIFRA veces que la frase de la frontera aparece: %d" % len(fr))
    if len(fr) != 1:
        print("   PARADA: la frontera no es unica.")
        return 1
    n_fr = fr[0]
    print("   docs/plan/LECTURAS_DIRIGIDAS.md:%d  cabecera de LD-07" % n_cab)
    print("   docs/plan/LECTURAS_DIRIGIDAS.md:%d  primera linea de la frontera" % n_fr)
    fin = n_fr
    while fin < len(lineas) and lineas[fin].startswith(">"):
        fin += 1
    cita = " ".join(l.lstrip("> ").strip() for l in lineas[n_fr - 1:fin])
    print("   la frontera, entera y citada del fichero:")
    print("      %s" % cita)
    print("   se inserta DESPUES de la linea %d, dentro de LD-07 y antes de LD-08"
          % fin)
    print("")
    bloque = [
        "",
        "%s, TAREA 5;" % MARCA,
        "> adjudicacion 5.14 del acta 165 y su hallazgo 4.2). POR ADICION Y SIN BORRAR",
        "> NI UNA LETRA DE ARRIBA:** la frontera se escribio el 11 ago 2026 y era cierta",
        "> aquel dia. **Hoy los dos nodos que separa son EL MISMO NODO:** medido en esta",
        "> vuelta con el resolutor que `P.1` obliga, `%s` resuelve a" % B,
        "> `%s`, asi que `LD-06` y `LD-07` apuntan hoy al mismo par" % A,
        "> resuelto y las once lecturas dirigidas son **NUEVE pares distintos**.",
        ">",
        "> **QUE SE PIERDE Y QUE NO.** No se pierde la lectura: los dos textos que se",
        "> leyeron aquel dia siguen siendo los que se leyeron. **Lo que se pierde es la",
        "> frontera**, porque ya no hay dos nodos entre los que trazarla. Y no es una",
        "> contradiccion entre `LD-06` y `LD-07`: las dos leyeron el **BLOQUE INJERTADO**",
        "> de `project_close_out` contra dos nodos que entonces eran dos, y la `A` de",
        "> `LD-06` no es entre los nodos sino entre el bloque y el otro nodo entero, tal",
        "> como esa misma ficha lo dice.",
        ">",
        "> **LO QUE ESTA ANOTACION NO HACE:** no mueve la `D` de `LD-07`, no mueve la",
        "> `A DE BLOQUE` de `LD-06`, no declara cual de las dos manda y no toca ni un",
        "> nodo. **La clase la decide una lectura, no un colapso.** Medido en",
        "> `../loop/SALIDA_V166_T5_COLAPSO.txt`.",
    ]
    nuevas = lineas[:fin] + bloque + lineas[fin:]
    nuevo = "\n".join(nuevas)
    print("D) LAS GUARDAS, SOBRE EL TEXTO NUEVO SIN ESCRIBIRLO")
    guardas = [
        ("1_ninguna_linea_vieja_desaparece", all(l in nuevas for l in lineas), True),
        ("2_el_documento_solo_crece", len(nuevo) > len(texto), True),
        ("3_la_frontera_vieja_sigue_entera",
         all(lineas[i] in nuevas for i in range(n_fr - 1, fin)), True),
        ("4_la_anotacion_cae_dentro_de_LD_07",
         nuevo.index(MARCA) > nuevo.index(CABECERA_LD07), True),
        ("5_y_antes_de_LD_08",
         nuevo.index(MARCA) < nuevo.index("### `LD-08`"), True),
        ("6_cero_guiones_largos_y_medios",
         "\n".join(bloque).count("\u2014") + "\n".join(bloque).count("\u2013"), 0),
        ("7_no_se_mueve_ninguna_clase",
         nuevo.count("### `LD-07` . `project_close_out` contra "
                     "`encuesta_satisfaccion_postproyecto` . **D**"), 1),
    ]
    malos = 0
    for nombre, real, esp in guardas:
        ok = real == esp
        print("   %-42s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esp))
        if not ok:
            malos += 1
    if malos:
        print("   PARADA: la simulacion falla. NO SE ESCRIBE NADA.")
        return 1
    print("")
    print("E) EL BLOQUE ENTERO, PARA QUE NADA ENTRE SIN LEERSE")
    for l in bloque:
        print("   %s" % l)
    print("")
    if not aplicar:
        print("F) NO SE ESCRIBE (falta --aplicar)")
        return 0
    with io.open(DOC, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(nuevo)
    print("F) ESCRITO")
    t2 = io.open(DOC, encoding="utf-8").read()
    print("   CIFRA lineas antes: %d | despues: %d"
          % (len(lineas), len(t2.split("\n"))))
    print("   la anotacion esta: %s" % (MARCA in t2))
    print("   la frontera vieja sigue: %s" % (lineas[n_fr - 1] in t2))
    print("   la cabecera de LD-07 sigue con su D: %s"
          % (t2.count(CABECERA_LD07 + " . **D**") == 1))
    print("   FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main("--aplicar" in sys.argv))
