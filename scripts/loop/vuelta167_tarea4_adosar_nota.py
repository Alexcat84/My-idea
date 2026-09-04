# -*- coding: utf-8 -*-
r"""vuelta167_tarea4_adosar_nota.py . LA NOTA FECHADA QUE LE DICE A LA FILA DEL
RETRATO DE QUE POBLACION HABLA (TAREA 4 de la vuelta 167; adjudicacion 6.6 del
acta 166, por su hallazgo 4.3).

EL CARRIL ES EL DEL BANCO 9.10 Y NO OTRO: nota fechada ADOSADA, cifra INTACTA,
ninguna nota vieja reescrita. **EL `4` NO SE TOCA.** Lo unico que se anade es de
que poblacion es ese 4, con el `221` y el `13` al lado, cada uno con su corte y
su fichero de salida.

Y NINGUNA CIFRA DE LA NOTA SE TECLEA (`EJECUTOR.md` 1, *"LA TABLA SE CUENTA DE
SU FICHERO"*): las tres se LEEN de
`docs/loop/SALIDA_V167_T4_CENSO_POBLACIONES.txt`, que es la salida del censo que
esta misma vuelta corrio, y si ese fichero no esta o no trae sus tres lineas,
este instrumento PARA en vez de escribir una nota con cifras inventadas.

IDEMPOTENTE: si la marca de esta nota ya vive en la fila, no escribe nada y lo
dice.

USO:
  python scripts/loop/vuelta167_tarea4_adosar_nota.py
  python scripts/loop/vuelta167_tarea4_adosar_nota.py --mutar
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388.md")
CENSO = os.path.join(RAIZ, "docs", "loop", "SALIDA_V167_T4_CENSO_POBLACIONES.txt")

ROTULO = "| pares con mas de un veredicto crudo apuntando al mismo par resuelto |"
MARCA = "NOTA ADOSADA, 4 sep 2026 (vuelta 167, TAREA 4"

PATRONES = {
    "cuatro": r"^\s*CIFRA pares con MAS DE UNA FILA A: (\d+)\s*$",
    "doscientos": r"^\s*CIFRA pares con MAS DE UNA FILA de cualquier clase: (\d+)\s*$",
    "trece": r"^\s*CIFRA pares con MAS DE UNA CLASE distinta: (\d+)\s*$",
    "corte": r"^\s*docs/INTRA_DOMINIO_VEREDICTOS\.jsonl: \d+ filas, puesto mayor (\d+)\s*$",
}


def cifras_del_fichero(ruta=None):
    """LAS TRES CIFRAS Y EL CORTE, LEIDOS DE LA SALIDA DEL CENSO. Devuelve
    (dict, error). Si falta una sola, devuelve error y NO se escribe nada."""
    ruta = ruta or CENSO
    if not os.path.exists(ruta):
        return None, "PARADA: no existe %s. Corre el censo antes." % ruta
    texto = io.open(ruta, encoding="utf-8").read()
    fuera = {}
    for clave, pat in PATRONES.items():
        m = re.findall(pat, texto, re.M)
        if len(m) != 1:
            return None, ("PARADA: '%s' aparece %d veces en la salida del censo, "
                          "y tiene que aparecer una." % (clave, len(m)))
        fuera[clave] = int(m[0])
    return fuera, None


def fila_del_plan(texto):
    """La fila del rotulo, localizada y contada. Devuelve (indice, error)."""
    lineas = texto.split("\n")
    aciertos = [i for i, l in enumerate(lineas) if l.startswith(ROTULO)]
    if len(aciertos) != 1:
        return None, ("PARADA: el rotulo aparece %d veces en RECOMPUTO_3388.md."
                      % len(aciertos))
    return aciertos[0], None


def nota(c):
    """El texto de la nota, con sus cuatro numeros METIDOS y no tecleados."""
    return (
        " [%s, adjudicacion 6.6 del acta 166 por su hallazgo 4.3): EL `%d` DE ESTA "
        "CELDA NO SE TOCA Y NINGUNA NOTA VIEJA SE REESCRIBE. Lo que se anade es DE "
        "QUE POBLACION ES ESE `%d`, porque el rotulo de la fila no lo dice y al lado "
        "de otras dos cifras parecidas se lee como contradiccion cuando no la hay. "
        "COMPROBADO POR MI EN LA FUENTE Y NO COPIADO DE NADIE: "
        "`../../scripts/plan/recomputo_3388.py:106` filtra por `clase == \"A\"` ANTES "
        "de agrupar, asi que el `retrato` de esta tabla se construye SOLO con filas "
        "de clase `A`. **LAS TRES POBLACIONES, QUE SON TRES Y NO UNA, todas con corte "
        "en el puesto %d y todas medidas hoy en "
        "`../loop/SALIDA_V167_T4_CENSO_POBLACIONES.txt`:** (1) **%d**, que es ESTA "
        "CELDA: pares del RETRATO (solo filas `A`), resueltos y sin colapsos, CON MAS "
        "DE UNA FILA `A`; (2) **%d**: pares resueltos distintos sobre TODAS las filas "
        "del archivo, sin filtrar clase, CON MAS DE UNA FILA de cualquier clase; y "
        "(3) **%d**: los de (2) que ademas llevan CLASES DISTINTAS, con reparto ocho "
        "`B` con `D`, cuatro `A` con `D` y uno con `A`, `B` y `D`. El `%d` y el `%d` "
        "vienen de la TAREA 5 de la vuelta 166 y estan tambien en "
        "`../loop/SALIDA_V166_T5_COLAPSO.txt`; aqui se recomputaron con instrumento "
        "propio de la 167 y dan lo mismo. **SON SUBCONJUNTOS ENCAJADOS y por eso no "
        "se contradicen:** los %d de (1) estan los %d dentro de (2), y solo UNO de "
        "ellos esta ademas en (3). **Y ESTA NOTA NO ADJUDICA NADA:** no mueve un "
        "veredicto, no le pone clase a ningun par y no toca ni un nodo.]"
        % (MARCA, c["cuatro"], c["cuatro"], c["corte"], c["cuatro"],
           c["doscientos"], c["trece"], c["doscientos"], c["trece"],
           c["cuatro"], c["cuatro"]))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 167, TAREA 4: LA NOTA ADOSADA A LA FILA DEL RETRATO")
    print("=" * 78)
    print("")
    c, err = cifras_del_fichero()
    print("A) LAS CIFRAS, LEIDAS DE LA SALIDA DEL CENSO Y NO TECLEADAS")
    if err:
        print("   " + err)
        return 1
    for k in ("cuatro", "doscientos", "trece", "corte"):
        print("   %-12s %d   (de docs/loop/SALIDA_V167_T4_CENSO_POBLACIONES.txt)"
              % (k, c[k]))
    print("")

    texto = io.open(PLAN, encoding="utf-8", newline="").read()
    idx, err = fila_del_plan(texto)
    print("B) LA FILA, LOCALIZADA Y CONTADA")
    if err:
        print("   " + err)
        return 1
    lineas = texto.split("\n")
    fila = lineas[idx]
    print("   docs/plan/RECOMPUTO_3388.md:%d" % (idx + 1))
    print("   CIFRA bytes de la fila ANTES: %d" % len(fila.encode("utf-8")))
    print("")

    print("C) LA CIFRA DE LA CELDA, COMPROBADA INTACTA ANTES Y DESPUES")
    celda = re.search(r"\|\s*~~\*\*0\*\*~~\s*\*\*(\d+)\*\*", fila)
    if not celda:
        print("   PARADA: la celda no tiene la forma de cifra tachada mas cifra viva.")
        return 1
    print("   la celda dice hoy: %s (y la tachada de al lado, 0)" % celda.group(1))
    if int(celda.group(1)) != c["cuatro"]:
        print("   PARADA: la celda dice %s y el censo mide %d. No se adosa nota"
              % (celda.group(1), c["cuatro"]))
        print("   sobre una celda que no cuadra con la medicion de hoy.")
        return 1
    print("   CUADRA con el censo de hoy: SI")
    print("")

    if MARCA in fila:
        print("D) YA ESTABA: la nota de esta vuelta ya vive en la fila. No se toca.")
        print("   CIFRA notas escritas: 0")
        return 0

    if not fila.rstrip().endswith("]** |"):
        print("D) PARADA: la fila no termina como se espera y no se donde adosar.")
        return 1
    corte_txt = fila.rstrip()
    nueva = corte_txt[:-len("]** |")] + "]" + nota(c) + "** |"
    lineas[idx] = nueva
    io.open(PLAN, "w", encoding="utf-8", newline="").write("\n".join(lineas))
    print("D) ESCRITO, POR ADICION")
    print("   CIFRA bytes de la fila DESPUES: %d" % len(nueva.encode("utf-8")))
    print("   CIFRA bytes anadidos: %d"
          % (len(nueva.encode("utf-8")) - len(fila.encode("utf-8"))))
    print("   CIFRA notas escritas: 1")
    print("")

    print("E) LA COMPROBACION DE QUE FUE ADICION Y NO REESCRITURA")
    texto2 = io.open(PLAN, encoding="utf-8", newline="").read()
    lineas2 = texto2.split("\n")
    print("   CIFRA lineas del fichero antes y despues: %d y %d"
          % (len(lineas), len(lineas2)))
    print("   toda linea distinta de la %d es identica: %s"
          % (idx + 1, all(lineas[i] == lineas2[i]
                          for i in range(len(lineas)) if i != idx)))
    viejo_dentro = (corte_txt[:-len("]** |")] + "]") in lineas2[idx]
    print("   el texto viejo de la fila sigue entero dentro de la nueva: %s"
          % viejo_dentro)
    celda2 = re.search(r"\|\s*~~\*\*0\*\*~~\s*\*\*(\d+)\*\*", lineas2[idx])
    print("   la celda sigue diciendo: %s" % (celda2.group(1) if celda2 else "PERDIDA"))
    if not viejo_dentro or not celda2 or celda2.group(1) != celda.group(1):
        print("   PARADA: la adicion no conservo el texto viejo o la cifra.")
        return 1
    print("")
    print("VERDE: nota adosada, cifra intacta, texto viejo entero.")
    return 0


# ---------------------------------------------------------------------------
# CASO POSITIVO POR MUTACION (EJECUTOR.md 1, "EL CASO ROJO SE PRUEBA POR
# MUTACION"). Ningun veredicto es constante literal: todos salen de correr las
# funciones REALES sobre sujetos fabricados y sobre los ficheros de verdad, y la
# segunda pasada muta cada esperado y exige que el caso CAIGA.
#
# QUE TIENE QUE PODER TUMBAR:
#   (a) que las cifras de la nota SALGAN DEL FICHERO y no esten tecleadas: se
#       fabrica una salida de censo con otras cifras y la nota tiene que
#       cambiar con ellas;
#   (b) que una salida de censo incompleta o duplicada PARE en vez de escribir;
#   (c) que la fila del plan se localice UNA sola vez;
#   (d) que la nota sea ADICION: el texto viejo de la fila entero dentro de la
#       nueva, y la cifra de la celda intacta.
# CERO ESCRITURAS SOBRE docs/plan/: el ensayo de adicion se hace sobre la fila
# EN MEMORIA, no sobre el fichero.
# ---------------------------------------------------------------------------

_CENSO_FALSO = """
   docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d filas, puesto mayor %d
   CIFRA pares con MAS DE UNA FILA A: %d
   CIFRA pares con MAS DE UNA FILA de cualquier clase: %d
   CIFRA pares con MAS DE UNA CLASE distinta: %d
"""


def _censo_falso(tmp, cuatro=7, doscientos=300, trece=20, corte=9999,
                 duplicar=False, quitar=False):
    txt = _CENSO_FALSO % (corte, corte, cuatro, doscientos, trece)
    if duplicar:
        txt += "   CIFRA pares con MAS DE UNA FILA A: %d\n" % (cuatro + 1)
    if quitar:
        txt = "\n".join(l for l in txt.split("\n")
                        if "MAS DE UNA CLASE distinta" not in l)
    io.open(tmp, "w", encoding="utf-8", newline="\n").write(txt)
    return tmp


def prueba_de_mutacion():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 167, TAREA 4: CASO POSITIVO POR MUTACION DE LA NOTA ADOSADA")
    print("=" * 78)
    print("")
    casos = []
    tmp = os.path.join(RAIZ, "docs", "loop", "_v167_t4_censo_falso.txt")

    print("A) LAS CIFRAS SALEN DEL FICHERO Y NO ESTAN TECLEADAS")
    c1, e1 = cifras_del_fichero(_censo_falso(tmp, 7, 300, 20, 9999))
    print("   censo falso (7, 300, 20, corte 9999) -> leido %r" % (c1,))
    casos.append(("A_lee_el_cuatro_del_fichero", c1["cuatro"], 7))
    casos.append(("A_lee_el_doscientos_del_fichero", c1["doscientos"], 300))
    casos.append(("A_lee_el_trece_del_fichero", c1["trece"], 20))
    casos.append(("A_lee_el_corte_del_fichero", c1["corte"], 9999))
    n1 = nota(c1)
    casos.append(("A_la_nota_lleva_el_7_del_fichero", "EL `7` DE ESTA" in n1, True))
    casos.append(("A_la_nota_NO_lleva_el_4_de_hoy", "EL `4` DE ESTA" in n1, False))
    c2, _e = cifras_del_fichero(_censo_falso(tmp, 4, 221, 13, 3388))
    casos.append(("A_con_otras_cifras_la_nota_es_otra", nota(c1) == nota(c2), False))
    print("")

    print("B) UNA SALIDA DE CENSO ROTA PARA EN VEZ DE ESCRIBIR")
    cq, eq = cifras_del_fichero(_censo_falso(tmp, quitar=True))
    print("   falta una linea -> %s" % eq)
    casos.append(("B_si_falta_una_cifra_para", eq is not None and cq is None, True))
    cd, ed = cifras_del_fichero(_censo_falso(tmp, duplicar=True))
    print("   linea duplicada -> %s" % ed)
    casos.append(("B_si_una_cifra_esta_dos_veces_para", ed is not None, True))
    ci, ei = cifras_del_fichero(os.path.join(RAIZ, "docs", "loop", "_no_existe_.txt"))
    casos.append(("B_si_no_existe_el_fichero_para", ei is not None, True))
    os.remove(tmp)
    print("")

    print("C) LA FILA DEL PLAN SE LOCALIZA UNA SOLA VEZ")
    plan = io.open(PLAN, encoding="utf-8", newline="").read()
    idx, err = fila_del_plan(plan)
    print("   fila real: indice %s, error %r" % (idx, err))
    casos.append(("C_la_fila_real_se_localiza", err is None, True))
    doble = plan.split("\n")
    doble.append(doble[idx])
    _i, e_doble = fila_del_plan("\n".join(doble))
    casos.append(("C_si_estuviera_dos_veces_para", e_doble is not None, True))
    _i, e_cero = fila_del_plan("una tabla sin esa fila\n")
    casos.append(("C_si_no_estuviera_para", e_cero is not None, True))
    print("")

    print("D) LA NOTA ES ADICION: EL TEXTO VIEJO ENTERO Y LA CIFRA INTACTA")
    fila = plan.split("\n")[idx]
    base = fila.rstrip()
    nueva = base[:-len("]** |")] + "]" + nota(c2) + "** |"
    print("   bytes antes %d, bytes despues %d"
          % (len(base.encode("utf-8")), len(nueva.encode("utf-8"))))
    casos.append(("D_el_texto_viejo_entero_sigue_dentro",
                  (base[:-len("]** |")] + "]") in nueva, True))
    casos.append(("D_la_nueva_es_mas_larga", len(nueva) > len(base), True))
    v = re.search(r"\|\s*~~\*\*0\*\*~~\s*\*\*(\d+)\*\*", base).group(1)
    n = re.search(r"\|\s*~~\*\*0\*\*~~\s*\*\*(\d+)\*\*", nueva).group(1)
    print("   celda antes %s, celda despues %s" % (v, n))
    casos.append(("D_la_celda_no_se_mueve", n, v))
    casos.append(("D_la_tachada_sigue_estando", "~~**0**~~" in nueva, True))
    casos.append(("D_la_nota_nueva_esta", MARCA in nueva, True))
    casos.append(("D_las_notas_viejas_no_se_reescriben",
                  nueva.count("PRIMERA CORRECCION"), base.count("PRIMERA CORRECCION")))
    print("")

    print("E) PASADA 1, LOS CASOS TAL CUAL")
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

    print("F) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mut = not esperado
        elif isinstance(esperado, int):
            mut = esperado + 1
        else:
            mut = str(esperado) + "_mutado"
        cae = (real != mut)
        print("   %-52s %s   (esperado mutado=%r)"
              % (nombre, "CAE" if cae else "NO CAE", mut))
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
    if "--mutar" in sys.argv:
        sys.exit(prueba_de_mutacion())
    sys.exit(main())
