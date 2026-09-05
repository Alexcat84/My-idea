# -*- coding: utf-8 -*-
r"""vuelta178_tarea1c_mutacion_ast.py . EL CASO POSITIVO POR MUTACION DEL CUARTO
VEREDICTO DE `cotejar_clon_declarado.py`, EL ARBOL DE SINTAXIS.

TAREA 1.c de la vuelta 178. Adjudicacion del acta 177 punto 7.7.

SUJETO CONGELADO, que es la condicion de entrada en la nomina desde la vuelta
148: TODO lo que este arnes mide son textos FABRICADOS EN MEMORIA y ficheros
fabricados en un directorio temporal que el propio arnes retira (`P.16`). Ni el
repo ni `scripts/loop/` se tocan. La funcion que se prueba, `cotejar()`, es pura
y recibe los dos textos ya leidos, que es lo que permite esto.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL (`EJECUTOR.md` 1, caida 2 de la vuelta
89): cada caso sale de correr `cotejar()` sobre un par fabricado, y la segunda
pasada MUTA EL VALOR ESPERADO y exige que CAIGA.

EL CASO QUE DECIDE TODO ESTO ES EL 1, Y VA PRIMERO A PROPOSITO: dos ficheros que
solo se diferencian en UNA COMA FINAL tienen que dar MAQUINA DIFIERE y AST
IDENTICO. Es el par que enfrento al auditor (que conto 0 sentencias a ojo) con
el instrumento (que contaba 1): los dos tenian razon, porque median cosas
distintas. Si ese caso no esta, esta sub-tarea no esta hecha.

LOS DEMAS CASOS:

  2. UNA LLAMADA DISTINTA DE VERDAD mueve el AST. Si no lo moviera, el cuarto
     veredicto seria un sello de goma que dice IDENTICO a todo.
  3. UN DOCSTRING DISTINTO mueve el AST DEL FICHERO ENTERO y NO mueve el AST SIN
     DOCSTRING. Es el motivo entero de que el veredicto vaya en dos mitades.
  4. UNA CADENA QUE SE IMPRIME distinta mueve el AST (cambia el VALOR de un
     nodo `Constant`), y ahi se ve la frontera de esta vara: mide el arbol, no
     la intencion. Se declara en vez de disimularse.
  5. LA SANGRIA Y LAS LINEAS EN BLANCO no mueven el AST.
  6. UN FICHERO QUE NO PARSEA SALE EN ROJO CON SU LINEA, y se comprueba de
     extremo a extremo corriendo el fichero como programa y mirando su `exit`.
  7. Y CUANDO LOS ARBOLES DIFIEREN SE DICE CUANTOS NODOS Y DE QUE TIPO, no un
     DIFIERE pelado.

USO:
  python scripts/loop/vuelta178_tarea1c_mutacion_ast.py
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import cotejar_clon_declarado as C   # noqa: E402

NL = chr(10)

BASE = (
    'r"""un fichero de mentira de la vuelta 100."""' + NL +
    "import os" + NL +
    NL +
    "def sumar(a, b):" + NL +
    '    print("sumando")' + NL +
    "    return a + b" + NL +
    NL +
    "sumar(1, 2)" + NL
)

# EL PAR QUE LO DECIDE TODO: la unica diferencia es una COMA FINAL en la llamada.
COMA_FINAL = BASE.replace("sumar(1, 2)", "sumar(1, 2,)")

LLAMADA_DISTINTA = BASE.replace("sumar(1, 2)", "sumar(1, 3)")
DOCSTRING_DISTINTO = BASE.replace("un fichero de mentira de la vuelta 100.",
                                  "un fichero de mentira de la vuelta 101, que cuenta otra cosa.")
CADENA_DISTINTA = BASE.replace('print("sumando")', 'print("sumo dos numeros")')
FORMATO_DISTINTO = BASE.replace("import os" + NL, "import os" + NL + NL + NL)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    p("=" * 78)
    p("CASO POSITIVO POR MUTACION DEL CUARTO VEREDICTO (vuelta 178, TAREA 1.c)")
    p("=" * 78)
    p("")

    casos = []
    NUM = (100, 101)

    p("1) EL CASO QUE LO DECIDE TODO: DOS FICHEROS QUE SOLO SE DIFERENCIAN")
    p("   EN UNA COMA FINAL")
    p("   A: ...sumar(1, 2)   B: ...sumar(1, 2,)")
    r = C.cotejar(BASE, COMA_FINAL, NUM)
    p("   SOLO LA MAQUINA        : %s" % ("IDENTICO" if r["maquina_identica"] else "DIFIERE"))
    p("   CIFRA SENTENCIAS DE CODIGO que la clasificacion vieja cuenta: %d"
      % len(r["sentencias"]))
    p("   AST DEL FICHERO ENTERO : %s"
      % ("IDENTICO" if r["ast_identico_entero"] else "DIFIERE"))
    p("   AST SIN EL DOCSTRING   : %s"
      % ("IDENTICO" if r["ast_identico_maquina"] else "DIFIERE"))
    casos.append(("1_coma_final_maquina_DIFIERE", r["maquina_identica"], False))
    casos.append(("1_coma_final_la_vieja_cuenta_UNA_sentencia", len(r["sentencias"]), 1))
    casos.append(("1_coma_final_AST_entero_IDENTICO", r["ast_identico_entero"], True))
    casos.append(("1_coma_final_AST_maquina_IDENTICO", r["ast_identico_maquina"], True))
    p("   LO QUE ESTE CASO PRUEBA: la clasificacion vieja NO SE TOCA y sigue")
    p("   diciendo 1, y el cuarto veredicto dice que el programa no cambia. Las")
    p("   dos cifras son verdaderas y ahora estan las dos en el mismo sitio.")
    p("")

    p("2) UNA LLAMADA DISTINTA DE VERDAD SI MUEVE EL AST")
    r2 = C.cotejar(BASE, LLAMADA_DISTINTA, NUM)
    p("   AST SIN EL DOCSTRING   : %s"
      % ("IDENTICO" if r2["ast_identico_maquina"] else "DIFIERE"))
    p("   CIFRA nodos: A %d | B %d" % (r2["ast_nodos_a"], r2["ast_nodos_b"]))
    casos.append(("2_llamada_distinta_AST_DIFIERE", r2["ast_identico_maquina"], False))
    p("")

    p("3) UN DOCSTRING DISTINTO MUEVE EL ENTERO Y NO MUEVE LA MAQUINA")
    r3 = C.cotejar(BASE, DOCSTRING_DISTINTO, NUM)
    p("   AST DEL FICHERO ENTERO : %s"
      % ("IDENTICO" if r3["ast_identico_entero"] else "DIFIERE"))
    p("   AST SIN EL DOCSTRING   : %s"
      % ("IDENTICO" if r3["ast_identico_maquina"] else "DIFIERE"))
    casos.append(("3_docstring_distinto_AST_entero_DIFIERE", r3["ast_identico_entero"], False))
    casos.append(("3_docstring_distinto_AST_maquina_IDENTICO", r3["ast_identico_maquina"], True))
    p("")

    p("4) UNA CADENA QUE SE IMPRIME DISTINTA SI MUEVE EL AST, Y SE DECLARA")
    p("   (es la frontera de esta vara: mide el ARBOL, o sea el valor del nodo")
    p("   Constant, no la intencion. La clasificacion por token de los tres")
    p("   veredictos viejos es la que sabe que eso es LITERAL DE TEXTO, y por eso")
    p("   los cuatro veredictos van juntos y ninguno sustituye a otro)")
    r4 = C.cotejar(BASE, CADENA_DISTINTA, NUM)
    p("   AST SIN EL DOCSTRING   : %s"
      % ("IDENTICO" if r4["ast_identico_maquina"] else "DIFIERE"))
    p("   CIFRA SENTENCIAS DE CODIGO: %d | LITERALES DE TEXTO: %d"
      % (len(r4["sentencias"]), len(r4["literales"])))
    casos.append(("4_cadena_distinta_AST_DIFIERE", r4["ast_identico_maquina"], False))
    casos.append(("4_cadena_distinta_sentencias_CERO", len(r4["sentencias"]), 0))
    p("")

    p("5) LAS LINEAS EN BLANCO NO MUEVEN EL AST")
    r5 = C.cotejar(BASE, FORMATO_DISTINTO, NUM)
    p("   SOLO LA MAQUINA        : %s"
      % ("IDENTICO" if r5["maquina_identica"] else "DIFIERE"))
    p("   AST SIN EL DOCSTRING   : %s"
      % ("IDENTICO" if r5["ast_identico_maquina"] else "DIFIERE"))
    casos.append(("5_lineas_en_blanco_AST_IDENTICO", r5["ast_identico_maquina"], True))
    p("")

    p("6) UN FICHERO QUE NO PARSEA CAE EN ROJO CON SU LINEA")
    tmp = tempfile.mkdtemp(prefix="v178_ast_")
    try:
        buena = os.path.join(tmp, "buena.py")
        rota = os.path.join(tmp, "rota.py")
        io.open(buena, "w", encoding="utf-8", newline=NL).write(BASE)
        io.open(rota, "w", encoding="utf-8", newline=NL).write(
            BASE + "def rota(:" + NL + "    pass" + NL)
        r6 = C.cotejar(BASE, io.open(rota, encoding="utf-8").read(), NUM)
        p("   CIFRA lados que no parsean: %d" % len(r6["ast_no_parsea"]))
        for lado, motivo in r6["ast_no_parsea"]:
            p("      %s: %s" % (lado, motivo))
        p("   hay cuarto veredicto: %s" % ("SI" if r6["ast_hay"] else "NO"))
        casos.append(("6_el_roto_no_parsea", len(r6["ast_no_parsea"]), 1))
        casos.append(("6_el_motivo_nombra_su_linea",
                      any("linea" in m for _l, m in r6["ast_no_parsea"]), True))
        casos.append(("6_sin_arbol_no_hay_cuarto_veredicto", r6["ast_hay"], False))

        env = dict(os.environ)
        env["PYTHONIOENCODING"] = "utf-8"
        pr = subprocess.run(
            [sys.executable, os.path.join(AQUI, "cotejar_clon_declarado.py"),
             "--a", buena, "--b", rota, "--num-a", "100", "--num-b", "101"],
            cwd=RAIZ, capture_output=True, env=env)
        sal = pr.stdout.decode("utf-8", errors="replace")
        p("   de extremo a extremo, el instrumento sale con exit %d" % pr.returncode)
        casos.append(("6_de_extremo_a_extremo_exit_1", pr.returncode, 1))
        casos.append(("6_de_extremo_a_extremo_dice_ROJO",
                      "ROJO: 1 fichero(s) no parsean" in sal, True))

        pr2 = subprocess.run(
            [sys.executable, os.path.join(AQUI, "cotejar_clon_declarado.py"),
             "--a", buena, "--b", buena, "--num-a", "100", "--num-b", "101"],
            cwd=RAIZ, capture_output=True, env=env)
        sal2 = pr2.stdout.decode("utf-8", errors="replace")
        p("   y con los dos ficheros buenos, exit %d" % pr2.returncode)
        casos.append(("6_con_los_dos_buenos_exit_0", pr2.returncode, 0))
        casos.append(("6_imprime_los_CUATRO_veredictos",
                      "LOS CUATRO VEREDICTOS" in sal2, True))
        casos.append(("6_imprime_EL_ARBOL_DE_SINTAXIS",
                      "EL ARBOL DE SINTAXIS" in sal2, True))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        p("   P.16: el temporal se retira. Existe todavia: %s" % os.path.exists(tmp))
    p("")

    p("7) CUANDO LOS ARBOLES DIFIEREN SE DICE CUANTOS NODOS Y DE QUE TIPO")
    mas_codigo = BASE + "sumar(3, 4)" + NL + "sumar(5, 6)" + NL
    r7 = C.cotejar(BASE, mas_codigo, NUM)
    p("   AST SIN EL DOCSTRING   : %s"
      % ("IDENTICO" if r7["ast_identico_maquina"] else "DIFIERE"))
    p("   CIFRA nodos: A %d | B %d" % (r7["ast_nodos_a"], r7["ast_nodos_b"]))
    p("   tipos de nodo que no empatan:")
    for tipo, na_, nb_ in r7["ast_censo_distinto"]:
        p("      %-16s A %3d | B %3d" % (tipo, na_, nb_))
    casos.append(("7_arboles_distintos_hay_censo",
                  len(r7["ast_censo_distinto"]) > 0, True))
    casos.append(("7_el_censo_nombra_Call",
                  any(t == "Call" for t, _a, _b in r7["ast_censo_distinto"]), True))
    p("")

    p("8) PASADA 1, LOS CASOS TAL CUAL")
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

    p("9) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        mutado = (not esperado) if isinstance(esperado, bool) else esperado + 1
        cae = (real != mutado)
        p("   %-46s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    p("   CIFRA casos que CAEN: %d de %d" % (caen, len(casos)))
    p("")

    if fallos or caen != len(casos):
        p("ROJO DE LA MUTACION: el cuarto veredicto no se comporta.")
        p("FIN")
        return 1
    p("VERDE DE LA MUTACION: %d casos, los %d pasan y los %d CAEN al mutarles el "
      "valor esperado. EL CASO QUE LO DECIDE TODO SALE COMO TIENE QUE SALIR: dos "
      "ficheros que solo se diferencian en UNA COMA FINAL dan MAQUINA DIFIERE con "
      "UNA sentencia contada por la clasificacion vieja, y AST IDENTICO por las "
      "dos mitades del cuarto veredicto. Y un fichero que no parsea sale en ROJO "
      "con su linea, comprobado de extremo a extremo."
      % (len(casos), len(casos), len(casos)))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
