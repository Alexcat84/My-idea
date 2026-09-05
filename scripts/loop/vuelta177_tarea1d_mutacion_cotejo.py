# -*- coding: utf-8 -*-
r"""vuelta177_tarea1d_mutacion_cotejo.py . EL CASO POSITIVO POR MUTACION DE
`scripts/loop/cotejar_clon_declarado.py`.

QUE SUJETO PRUEBA: los tres veredictos (FICHERO ENTERO, SOLO DOCSTRING, SOLO LA
MAQUINA) y la CLASIFICACION en SENTENCIAS DE CODIGO y LITERALES DE TEXTO del
instrumento que nace en la TAREA 1.d de la vuelta 177.

POR QUE NO BASTA CON CORRERLO SOBRE LOS CLONES DE VERDAD. Corrido sobre el par
que el auditor midio, el instrumento da un resultado que PARECE bien; pero un
instrumento que solo se ha visto acertar una vez no esta probado, esta estrenado.
Aqui se le fabrican clones de mentira DONDE SE SABE LA RESPUESTA DE ANTEMANO
porque la escribe esta misma prueba, y se exige que la acierte en cada uno.

LOS SIETE SUJETOS FABRICADOS, Y CADA UNO AISLA UNA COSA:

  1. IDENTICOS                . los tres veredictos IDENTICO.
  2. SOLO EL DOCSTRING CAMBIA . entero DIFIERE, docstring DIFIERE, maquina
                                IDENTICO. Es el caso normal de un clon bueno.
  3. SOLO UNA CADENA CAMBIA   . maquina DIFIERE con SENTENCIAS 0 y LITERALES
                                mas de 0. Es la distincion entera del fichero.
  4. SOLO UN COMENTARIO CAMBIA. igual que el 3: un comentario es texto.
  5. UNA LLAMADA CAMBIA       . SENTENCIAS mas de 0. Si esto no muerde, el
                                instrumento no sirve para nada.
  6. UNA CADENA DE VARIAS     . maquina DIFIERE con SENTENCIAS 0 AUNQUE EL
     LINEAS SE ALARGA           NUMERO DE LINEAS CAMBIE. ESTE ES EL CASO QUE
                                TUMBO LA PRIMERA VERSION DEL INSTRUMENTO y por
                                eso esta aqui: la version que tapaba caracter a
                                caracter clasificaba esto como SENTENCIA DE
                                CODIGO, que es justo del reves.
  7. EL NUMERO DE VUELTA      . dos ficheros que solo se diferencian en su
                                propio numero tienen que salir IDENTICOS
                                ENTEROS, porque los dos numeros se sustituyen
                                por NNN en los dos ficheros.

MAS LOS DOS ROJOS, que son conducta y no veredicto:

  8. FALTA UN FICHERO         . exit 1, y el rojo lo da `main()`, asi que este
                                caso se corre por subproceso y no por funcion.
  9. LOS DOS CARRILES QUE       . `--exigir-maquina-identica` (estricto)
     BLOQUEAN                     enrojece tambien con un cambio de solo texto;
                                  `--exigir-codigo-identico` (util) lo deja
                                  pasar y enrojece solo con una sentencia. ESTE
                                  CASO ES POR QUE EL SEGUNDO CARRIL EXISTE: la
                                  primera version del instrumento solo tenia el
                                  estricto y esta prueba lo tumbo.

CERO ESCRITURAS FUERA DE UN DIRECTORIO TEMPORAL, que se borra al terminar. Nada
de esto toca el repo.

USO:  python scripts/loop/vuelta177_tarea1d_mutacion_cotejo.py
"""
import os
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import cotejar_clon_declarado as C   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(AQUI))
NL = chr(10)
Q3 = chr(34) * 3

BASE = NL.join([
    "# -*- coding: utf-8 -*-",
    'r' + Q3 + "fichero de mentira de la vuelta 175, para probar el cotejo." + Q3,
    "import os",
    "",
    "VUELTA = 175",
    "",
    "",
    "def saluda(a, b):",
    "    # un comentario cualquiera",
    '    print("hola %s" % a)',
    "    return os.path.join(a, b)",
    "",
    "",
    "TEXTO = " + Q3,
    "una cadena de varias lineas",
    "que dice cosas de la vuelta 175",
    "y se acaba aqui",
    Q3,
    "",
])


def escribir(dirtmp, nombre, texto):
    ruta = os.path.join(dirtmp, nombre)
    with open(ruta, "w", encoding="utf-8", newline=NL) as f:
        f.write(texto)
    return ruta


def veredicto(texto_a, texto_b, numeros=(175, 176)):
    """Los tres veredictos y la clasificacion, por la funcion PURA del sujeto."""
    return C.cotejar(texto_a, texto_b, numeros)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 177, TAREA 1.d: CASO POSITIVO POR MUTACION DEL COTEJO DE CLONES")
    print("=" * 78)
    print("")

    casos = []
    dirtmp = tempfile.mkdtemp(prefix="v177_cotejo_")
    try:
        print("A) EL SUJETO Y LOS CLONES DE MENTIRA")
        print("   sujeto: scripts/loop/cotejar_clon_declarado.py")
        print("   directorio temporal: %s" % dirtmp)
        print("   CIFRA lineas del fichero base fabricado: %d" % (BASE.count(NL) + 1))
        print("")

        print("B) CASO 1: DOS FICHEROS IDENTICOS. LOS TRES VEREDICTOS, IDENTICO")
        r = veredicto(BASE, BASE)
        print("   entero=%s docstring=%s maquina=%s"
              % (r["entero_identico"], r["docstring_identico"], r["maquina_identica"]))
        casos.append(("1_identicos_entero", r["entero_identico"], True))
        casos.append(("1_identicos_docstring", r["docstring_identico"], True))
        casos.append(("1_identicos_maquina", r["maquina_identica"], True))
        print("")

        print("C) CASO 2: SOLO CAMBIA EL DOCSTRING. LA MAQUINA TIENE QUE SALIR IGUAL")
        b = BASE.replace("fichero de mentira de la vuelta 175, para probar el cotejo.",
                         "fichero de mentira de la vuelta 176, y su docstring cuenta "
                         "otra cosa entera porque para eso esta.")
        r = veredicto(BASE, b)
        print("   entero=%s docstring=%s maquina=%s"
              % (r["entero_identico"], r["docstring_identico"], r["maquina_identica"]))
        casos.append(("2_solo_docstring_entero_difiere", r["entero_identico"], False))
        casos.append(("2_solo_docstring_docstring_difiere", r["docstring_identico"], False))
        casos.append(("2_solo_docstring_maquina_identica", r["maquina_identica"], True))
        print("")

        print("D) CASO 3: SOLO CAMBIA UNA CADENA. SENTENCIAS 0 Y LITERALES MAS DE 0")
        print("   (ESTA ES LA DISTINCION ENTERA DEL INSTRUMENTO)")
        b = BASE.replace('print("hola %s" % a)', 'print("adios, hasta luego %s" % a)')
        r = veredicto(BASE, b)
        print("   maquina=%s | sentencias=%d | literales=%d | flujo de codigo igual=%s"
              % (r["maquina_identica"], len(r["sentencias"]), len(r["literales"]),
                 r["codigo_identico"]))
        casos.append(("3_solo_cadena_maquina_difiere", r["maquina_identica"], False))
        casos.append(("3_solo_cadena_sentencias_cero", len(r["sentencias"]), 0))
        casos.append(("3_solo_cadena_literales_hay", len(r["literales"]) > 0, True))
        casos.append(("3_solo_cadena_flujo_de_codigo_igual", r["codigo_identico"], True))
        print("")

        print("E) CASO 4: SOLO CAMBIA UN COMENTARIO. UN COMENTARIO ES TEXTO")
        b = BASE.replace("# un comentario cualquiera",
                         "# otro comentario que dice una cosa distinta")
        r = veredicto(BASE, b)
        print("   maquina=%s | sentencias=%d | literales=%d"
              % (r["maquina_identica"], len(r["sentencias"]), len(r["literales"])))
        casos.append(("4_solo_comentario_sentencias_cero", len(r["sentencias"]), 0))
        casos.append(("4_solo_comentario_literales_hay", len(r["literales"]) > 0, True))
        print("")

        print("F) CASO 5: CAMBIA UNA LLAMADA DE VERDAD. TIENE QUE MORDER")
        print("   (si esto no muerde, el instrumento no sirve para nada)")
        b = BASE.replace("return os.path.join(a, b)", "return os.path.dirname(a)")
        r = veredicto(BASE, b)
        print("   maquina=%s | sentencias=%d | literales=%d | flujo de codigo igual=%s"
              % (r["maquina_identica"], len(r["sentencias"]), len(r["literales"]),
                 r["codigo_identico"]))
        casos.append(("5_llamada_distinta_maquina_difiere", r["maquina_identica"], False))
        casos.append(("5_llamada_distinta_sentencias_hay", len(r["sentencias"]) > 0, True))
        casos.append(("5_llamada_distinta_flujo_de_codigo_distinto", r["codigo_identico"], False))
        print("")

        print("G) CASO 6: UNA CADENA DE VARIAS LINEAS SE ALARGA. SENTENCIAS 0 IGUAL")
        print("   (ESTE ES EL CASO QUE TUMBO LA PRIMERA VERSION DEL INSTRUMENTO:")
        print("    tapando caracter a caracter, dos cadenas de distinto largo")
        print("    seguian difiriendo y se clasificaban como SENTENCIA DE CODIGO)")
        b = BASE.replace("y se acaba aqui",
                         "y se acaba aqui" + NL + "pero antes dice tres lineas mas"
                         + NL + "que en el otro fichero no estan" + NL
                         + "y aun asi la maquina es la misma")
        r = veredicto(BASE, b)
        print("   maquina=%s | sentencias=%d | literales=%d | flujo de codigo igual=%s"
              % (r["maquina_identica"], len(r["sentencias"]), len(r["literales"]),
                 r["codigo_identico"]))
        print("   CIFRA lineas de maquina: A %d | B %d"
              % (r["lineas_maquina_a"], r["lineas_maquina_b"]))
        casos.append(("6_cadena_mas_larga_maquina_difiere", r["maquina_identica"], False))
        casos.append(("6_cadena_mas_larga_sentencias_cero", len(r["sentencias"]), 0))
        casos.append(("6_cadena_mas_larga_flujo_de_codigo_igual", r["codigo_identico"], True))
        casos.append(("6_cadena_mas_larga_cambia_el_conteo_de_lineas",
                      r["lineas_maquina_a"] == r["lineas_maquina_b"], False))
        print("")

        print("H) CASO 7: SOLO CAMBIA EL NUMERO DE VUELTA. IDENTICOS ENTEROS")
        print("   (los DOS numeros se sustituyen por NNN en los DOS ficheros)")
        b = BASE.replace("175", "176")
        r = veredicto(BASE, b)
        print("   entero=%s docstring=%s maquina=%s"
              % (r["entero_identico"], r["docstring_identico"], r["maquina_identica"]))
        casos.append(("7_solo_el_numero_entero_identico", r["entero_identico"], True))
        print("   y SIN sustituir (numeros que no aparecen), tiene que DIFERIR:")
        r2 = veredicto(BASE, b, numeros=(900, 901))
        print("   entero=%s" % r2["entero_identico"])
        casos.append(("7_sin_sustituir_entero_difiere", r2["entero_identico"], False))
        print("")

        print("I) CASO 8: FALTA UN FICHERO. ROJO, exit 1, POR SUBPROCESO")
        ruta_a = escribir(dirtmp, "existe.py", BASE)
        ruta_no = os.path.join(dirtmp, "no_existe_ni_de_broma.py")
        cmd = [sys.executable, os.path.join(AQUI, "cotejar_clon_declarado.py"),
               "--a", ruta_a, "--num-a", "175", "--b", ruta_no, "--num-b", "176"]
        p = subprocess.run(cmd, capture_output=True, cwd=RAIZ)
        sal = p.stdout.decode("utf-8", errors="replace")
        print("   exit: %d" % p.returncode)
        print("   dice ROJO: %s" % ("ROJO" in sal))
        casos.append(("8_falta_un_fichero_exit_1", p.returncode, 1))
        casos.append(("8_falta_un_fichero_dice_rojo", "ROJO" in sal, True))
        print("   y con los dos ficheros presentes, exit 0:")
        ruta_b = escribir(dirtmp, "tambien_existe.py", BASE)
        cmd2 = [sys.executable, os.path.join(AQUI, "cotejar_clon_declarado.py"),
                "--a", ruta_a, "--num-a", "175", "--b", ruta_b, "--num-b", "176"]
        p2 = subprocess.run(cmd2, capture_output=True, cwd=RAIZ)
        print("   exit: %d" % p2.returncode)
        casos.append(("8_con_los_dos_ficheros_exit_0", p2.returncode, 0))
        print("")

        print("J) CASO 9: --exigir-maquina-identica EXTIENDE EL ROJO A LA MAQUINA")
        ruta_c = escribir(dirtmp, "maquina_distinta.py",
                          BASE.replace("return os.path.join(a, b)", "return os.path.dirname(a)"))
        ruta_d = escribir(dirtmp, "solo_texto_distinto.py",
                          BASE.replace('print("hola %s" % a)', 'print("adios %s" % a)'))
        print("   EL CARRIL ESTRICTO, --exigir-maquina-identica: enrojece con")
        print("   CUALQUIER linea de maquina distinta, INCLUIDAS las de solo texto.")
        for nombre, ruta, esperado in (("maquina distinta", ruta_c, 1),
                                       ("solo texto distinto", ruta_d, 1)):
            cmd3 = [sys.executable, os.path.join(AQUI, "cotejar_clon_declarado.py"),
                    "--a", ruta_a, "--num-a", "175", "--b", ruta, "--num-b", "176",
                    "--exigir-maquina-identica"]
            p3 = subprocess.run(cmd3, capture_output=True, cwd=RAIZ)
            print("   %-24s -> exit %d" % (nombre, p3.returncode))
            casos.append(("9_estricto_%s" % nombre.replace(" ", "_"),
                          p3.returncode, esperado))
        print("")
        print("   EL CARRIL UTIL, --exigir-codigo-identico: enrojece SOLO si difiere")
        print("   una SENTENCIA DE CODIGO, y deja pasar las de solo texto. ESTE CASO")
        print("   ES POR QUE EL SEGUNDO CARRIL EXISTE: la primera version del")
        print("   instrumento solo tenia el estricto, y esta misma prueba lo tumbo")
        print("   con un exit 1 donde tenia que dar 0.")
        for nombre, ruta, esperado in (("maquina distinta", ruta_c, 1),
                                       ("solo texto distinto", ruta_d, 0)):
            cmd4 = [sys.executable, os.path.join(AQUI, "cotejar_clon_declarado.py"),
                    "--a", ruta_a, "--num-a", "175", "--b", ruta, "--num-b", "176",
                    "--exigir-codigo-identico"]
            p4 = subprocess.run(cmd4, capture_output=True, cwd=RAIZ)
            print("   %-24s -> exit %d" % (nombre, p4.returncode))
            casos.append(("9_codigo_%s" % nombre.replace(" ", "_"),
                          p4.returncode, esperado))
        print("")

    finally:
        shutil.rmtree(dirtmp, ignore_errors=True)
        print("K) EL DIRECTORIO TEMPORAL SE BORRO: %s" % (not os.path.exists(dirtmp)))
        print("")

    print("L) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real_v, esperado in casos:
        ok = (real_v == esperado)
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real_v, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("M) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real_v, esperado in casos:
        mutado = (not esperado) if isinstance(esperado, bool) else esperado + 1
        cae = (real_v != mutado)
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
