# -*- coding: utf-8 -*-
r"""vuelta178_tarea1e_mutacion_higiene.py . EL CASO POSITIVO POR MUTACION DE LAS
DOS GUARDAS DE HIGIENE DE LA VUELTA 178.

TAREA 1.e. Las dos que el acta 177 adjudica, de una linea cada una:

  (1) `cerrar_reporte.cifras_sin_pareja()`: el reporte no publica una cifra de
      bytes ni un sha SIN SU PAREJA mientras la convencion del fundador no este
      fijada (acta 177 punto 7.11).
  (2) `verificar_mutaciones_viejas.anclaje_de()` y su guarda: LA REGLA DEL
      SUJETO CONGELADO, que existe desde la vuelta 145 y hasta hoy era una frase
      (`PD.2` del reporte 176, adjudicado en el acta 176 punto 7.9).

SUJETO CONGELADO, que es la condicion de entrada en la nomina desde la vuelta
148: TODO lo que este arnes mide son textos FABRICADOS EN MEMORIA y un
directorio TEMPORAL que el propio arnes retira (`P.16`). Ni `docs/loop/REPORTE.md`
ni `VIEJAS` ni `scripts/loop/` se leen para decidir ningun caso. Es lo que
permite que su verde sobreviva a que esta misma vuelta escriba su reporte.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL (`EJECUTOR.md` 1, caida 2 de la vuelta
89): cada caso sale de correr una de las dos funciones puras, y la segunda
pasada MUTA EL VALOR ESPERADO y exige que CAIGA.

USO:
  python scripts/loop/vuelta178_tarea1e_mutacion_higiene.py
"""
import io
import os
import shutil
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import cerrar_reporte as CR   # noqa: E402
import verificar_mutaciones_viejas as V   # noqa: E402

NL = chr(10)
CERCA = "```"

# LOS TEXTOS FABRICADOS DE LA GUARDA DE LA PAREJA. Ninguno sale de un reporte
# real: si salieran, cambiarian con el reporte y el verde no duraria una vuelta.
SOLA = "El tallador vive en `SALIDA.txt` (5.001 bytes)."
PAREJA = "El tallador vive en `SALIDA.txt` (5.021 bytes en disco y 5.001 bytes en LF)."
COINCIDEN = "El tallador: las dos convenciones, disco y normalizado a LF, dan 5.021 bytes."
SHA_SOLO = "Su sha256 es 7d683eea4700f18b y con eso queda sellado."
SHA_PAREJA = ("Su sha256 en disco es aa11bb22cc33dd44 y su sha256 en LF es "
              "7d683eea4700f18b.")
HASH_CORTO = "El commit de apertura es 77621a68 y el de cierre se talla luego."
EN_CERCA = (CERCA + NL + "salida cruda del instrumento: 5.001 bytes" + NL + CERCA)

# LOS ARNESES FABRICADOS DE LA GUARDA DEL SUJETO CONGELADO.
DOC = 'r"""un arnes de mentira que habla de docs/loop/REPORTE.md en su prosa."""'
A_CONGELADO = DOC + NL + "import tempfile" + NL + "tmp = tempfile.mkdtemp()" + NL
A_VIVO = ('r"""un arnes de mentira sin nada que declarar."""' + NL +
          "import io" + NL +
          'io.open("docs/loop/REPORTE.md")' + NL)
A_MIXTO = ('r"""un arnes de mentira que hace las dos cosas."""' + NL +
           "import io, tempfile" + NL +
           "tmp = tempfile.mkdtemp()" + NL +
           'io.open("docs/loop/REPORTE.md")' + NL)
A_MIXTO_DECLARA = ('r"""un arnes de mentira con SUJETO CONGELADO declarado."""' + NL +
                   "import io, tempfile" + NL +
                   "tmp = tempfile.mkdtemp()" + NL +
                   'io.open("docs/loop/REPORTE.md")' + NL)
A_SOLO_EN_DOC = (DOC + NL + "import tempfile" + NL + "tmp = tempfile.mkdtemp()" + NL)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    p("=" * 78)
    p("CASO POSITIVO POR MUTACION DE LAS DOS GUARDAS DE HIGIENE (vuelta 178, 1.e)")
    p("=" * 78)
    p("")

    casos = []

    p("A) LA GUARDA DE LA PAREJA DE CIFRAS (cerrar_reporte.cifras_sin_pareja)")
    for etiqueta, texto, esperado in (
            ("una cifra de bytes SOLA", SOLA, 1),
            ("las dos cifras de bytes", PAREJA, 0),
            ("una cifra que dice que las dos coinciden", COINCIDEN, 0),
            ("un sha SOLO", SHA_SOLO, 1),
            ("los dos sha", SHA_PAREJA, 0),
            ("un hash corto de commit, que no es un sha de contenido",
             HASH_CORTO, 0),
            ("una cifra dentro de un bloque cercado", EN_CERCA, 0)):
        salen = CR.cifras_sin_pareja(texto)
        p("   %-52s -> %d" % (etiqueta, len(salen)))
        for n, especie, muestra, linea in salen:
            p("        linea %d, %s, %r" % (n, especie, muestra))
        casos.append(("A_" + etiqueta.replace(" ", "_")[:38], len(salen), esperado))
    p("")

    p("B) LA GUARDA DEL SUJETO CONGELADO (verificar_mutaciones_viejas.anclaje_de)")
    for etiqueta, texto, declarado, esperado in (
            ("fabrica su sujeto en un temporal", A_CONGELADO, False, "CONGELADO"),
            ("abre el REPORTE.md vivo", A_VIVO, False, "SUJETO VIVO"),
            ("hace las dos cosas y no declara", A_MIXTO, False, "NO DECIDIBLE"),
            ("hace las dos y DECLARA", A_MIXTO_DECLARA, False, "CONGELADO"),
            ("esta en CASOS_DECLARADOS", A_VIVO, True, "CASO DECLARADO"),
            ("solo lo NOMBRA en el docstring", A_SOLO_EN_DOC, False, "CONGELADO")):
        v, cong, vive = V.anclaje_de(texto, declarado=declarado)
        p("   %-42s -> %-14s congela=%s vive=%s"
          % (etiqueta, v, cong[:2], vive))
        casos.append(("B_" + etiqueta.replace(" ", "_")[:38], v, esperado))
    p("")
    p("   EL CASO DEL DOCSTRING ES EL QUE IMPIDE EL FALSO ROJO: el texto de")
    p("   arriba NOMBRA docs/loop/REPORTE.md en su prosa y NO lo abre. Si la")
    p("   huella de sujeto vivo se buscara en el fichero entero, este arnes")
    p("   saldria acusado por hablar.")
    p("")

    p("C) LA GUARDA SOBRE UNA NOMINA FABRICADA Y UN DIRECTORIO FABRICADO")
    tmp = tempfile.mkdtemp(prefix="v178_higiene_")
    try:
        piezas = (("vuelta300_a_mutacion_congelada.py", A_CONGELADO),
                  ("vuelta300_b_mutacion_viva.py", A_VIVO),
                  ("vuelta300_c_mutacion_mixta.py", A_MIXTO),
                  ("vuelta300_d_mutacion_exenta.py", A_VIVO))
        for nombre, texto in piezas:
            io.open(os.path.join(tmp, nombre), "w",
                    encoding="utf-8", newline=NL).write(texto)
        nomina = [(n, False) for n, _t in piezas]
        declarados = {"vuelta300_d_mutacion_exenta.py": (1, "de mentira", "MARCA")}

        filas = V.anclaje_de_la_nomina(nomina, tmp, declarados)
        for nombre, v, _c, vv in filas:
            p("   %-38s %-14s abre: %s" % (nombre, v, ", ".join(vv) or "(nada)"))
        malas = V.guarda_del_sujeto_congelado(nomina, tmp, declarados)
        p("   CIFRA entradas que no cumplen: %d" % len(malas))
        casos.append(("C_la_guarda_caza_DOS", len(malas), 2))
        casos.append(("C_la_exenta_no_se_cuenta",
                      any(n == "vuelta300_d_mutacion_exenta.py" for n, _v, _x in malas),
                      False))
        casos.append(("C_la_congelada_no_se_cuenta",
                      any(n == "vuelta300_a_mutacion_congelada.py" for n, _v, _x in malas),
                      False))
        casos.append(("C_clasifica_las_CUATRO", len(filas), 4))

        p("   Y SI LA EXENCION SE QUITA, LA GUARDA LA CAZA (o sea que la exencion")
        p("   esta haciendo trabajo y no es decorativa):")
        malas_sin = V.guarda_del_sujeto_congelado(nomina, tmp, {})
        p("   CIFRA entradas que no cumplen sin la exencion: %d" % len(malas_sin))
        casos.append(("C_sin_la_exencion_caza_TRES", len(malas_sin), 3))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        p("   P.16: el temporal se retira. Existe todavia: %s" % os.path.exists(tmp))
    p("")

    p("D) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        p("   %-46s %s   (real=%r esperado=%r)"
          % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    p("   CIFRA casos: %d | pasan: %d | fallan: %d"
      % (len(casos), len(casos) - fallos, fallos))
    p("")

    p("E) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, str):
            mutado = esperado + " DE MENTIRA"
        else:
            mutado = esperado + 1
        cae = (real != mutado)
        p("   %-46s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    p("   CIFRA casos que CAEN: %d de %d" % (caen, len(casos)))
    p("")

    if fallos or caen != len(casos):
        p("ROJO DE LA MUTACION: alguna de las dos guardas de higiene no se comporta.")
        p("FIN")
        return 1
    p("VERDE DE LA MUTACION: %d casos, los %d pasan y los %d CAEN al mutarles el "
      "valor esperado. La guarda de la pareja caza una cifra de bytes sola y un "
      "sha solo, deja pasar las que traen su pareja o declaran que las dos "
      "convenciones coinciden, NO confunde un hash corto de commit con un sha de "
      "contenido y NO entra en los bloques cercados. La guarda del sujeto "
      "congelado separa CONGELADO, SUJETO VIVO, NO DECIDIBLE y CASO DECLARADO, y "
      "no acusa a un arnes por NOMBRAR un fichero vivo en su docstring."
      % (len(casos), len(casos), len(casos)))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
