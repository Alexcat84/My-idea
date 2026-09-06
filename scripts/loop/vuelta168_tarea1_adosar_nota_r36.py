# -*- coding: utf-8 -*-
r"""vuelta168_tarea1_adosar_nota_r36.py . LA NOTA FECHADA QUE SE ADOSA AL `R.36`
(TAREA 1 de la vuelta 168; adjudicacion 6.5 del acta 167, por su hallazgo 4.3).

EL CARRIL ES EL DEL BANCO 9.10 Y NO OTRO: nota fechada ADOSADA AL FINAL DE LA
ENTRADA, ninguna palabra vieja reescrita, ninguna glosa borrada. Las glosas de
la 6.1, 6.3, 6.4 y 6.9 del `R.36` describen LO ENCARGADO y no LO OCURRIDO, y
esta nota lo dice DEJANDOLAS ENTERAS DONDE ESTAN. Una correccion que tapa lo
que corrige no se puede auditar.

Y NINGUN VEREDICTO DE LA NOTA SE TECLEA (`EJECUTOR.md` 1, "LA TABLA SE CUENTA
DE SU FICHERO", y regla 2, "EL INSTRUMENTO MANDA"). Las cuatro glosas se
CONTRASTAN CONTRA GIT en esta misma vuelta, cada una con su medicion propia:

  6.1 y 6.3 dicen que el `REPORTE.md` de la vuelta 167 cubre las dos vueltas y
      cita las salidas selladas. MEDICION: se lee la PRIMERA LINEA de
      `docs/loop/REPORTE.md` en el arbol del commit del acta 167. Si esa linea
      dice "VUELTA 167", la glosa ocurrio; si dice otra vuelta, no ocurrio, y
      la nota publica que vuelta dice de verdad.
  6.4 dice que la bateria de verdad se corre en la vuelta 167. MEDICION: se
      cuentan los BYTES de `docs/loop/SALIDA_V167_BATERIA.txt` en el arbol de
      ese mismo commit. Un fichero de cero bytes no es una corrida, y eso lo
      dice el propio asunto del commit que lo trajo.
  6.9 dice "EJECUTADA EN EJECUCION, TAREA 5 de esta vuelta". MEDICION: se lee
      el ASUNTO del ultimo commit del ejecutor en el corredor de la vuelta 167
      (el anterior al acta). Si empieza por "TAREA 5: PARADA", la tarea termino
      en parada y la glosa no ocurrio.

SI ALGUNA MEDICION NO SE PUEDE HACER, EL INSTRUMENTO PARA Y NO ESCRIBE NADA:
una nota que corrige cuatro glosas sin haberlas medido seria la misma especie
que corrige.

Y SI LA MEDICION DIJERA QUE LA GLOSA SI OCURRIO, LA NOTA NO SE ESCRIBE Y SE
DECLARA: el instrumento no da por buena la adjudicacion, la comprueba. Ese es
el caso rojo de verdad y por eso el veredicto de cada glosa es una VARIABLE
COMPUTADA y no una constante literal (`EJECUTOR.md` 1, "EL CASO ROJO SE PRUEBA
POR MUTACION").

IDEMPOTENTE: si la marca de esta nota ya vive en el `R.36`, no escribe nada y
lo dice.

USO:
  python scripts/loop/vuelta168_tarea1_adosar_nota_r36.py
  python scripts/loop/vuelta168_tarea1_adosar_nota_r36.py --mutar
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")

CABECERA_R36 = "## R.36. Registro de las nueve adjudicaciones y la caida propia del acta de la vuelta 166"
MARCA = "NOTA ADOSADA, 4 sep 2026 (vuelta 168, TAREA 1, adjudicacion 6.5 del acta 167)"
PATRON_ACTA_167 = "ACTA DE LA VUELTA 167 DEL AUDITOR"


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def hash_del_acta_167():
    """EL HASH DE LA PARADA, LEIDO DE GIT Y NO TECLEADO (`EJECUTOR.md` 1, LA
    IDENTIDAD SE LEE DE GIT). Uno solo: si hay cero o mas de uno, PARA."""
    c, log = git(["log", "--format=%H%x09%s", "-400"])
    if c != 0:
        return None, "PARADA: git log fallo."
    hits = [l for l in log.splitlines() if l.split("\t", 1)[-1].startswith(PATRON_ACTA_167)]
    if len(hits) != 1:
        return None, ("PARADA: commits que empiezan por %r: %d (hace falta 1)."
                      % (PATRON_ACTA_167, len(hits)))
    h, asunto = hits[0].split("\t", 1)
    return (h, asunto), None


def medir_las_cuatro(acta):
    """LAS CUATRO GLOSAS, CONTRASTADAS CONTRA GIT. Devuelve (medidas, error).
    Cada veredicto es COMPUTADO: sale de comparar lo que la glosa afirma con lo
    que el arbol del commit del acta 167 dice."""
    m = {}

    # 6.1 y 6.3: la vuelta que el REPORTE.md de aquel arbol dice ser.
    c, rep = git(["show", "%s:docs/loop/REPORTE.md" % acta])
    if c != 0 or not rep.strip():
        return None, "PARADA: no se pudo leer docs/loop/REPORTE.md en %s." % acta[:8]
    primera = rep.splitlines()[0].strip()
    mm = re.search(r"REPORTE DE LA VUELTA (\d+)", primera)
    if not mm:
        return None, "PARADA: la primera linea del reporte no dice de que vuelta es."
    m["vuelta_del_reporte"] = int(mm.group(1))
    m["primera_linea_del_reporte"] = primera

    # 6.4: los bytes de la bateria de la 167 en aquel arbol.
    c, bat = git(["show", "%s:docs/loop/SALIDA_V167_BATERIA.txt" % acta])
    if c != 0:
        return None, ("PARADA: docs/loop/SALIDA_V167_BATERIA.txt no existe en %s."
                      % acta[:8])
    m["bytes_bateria_167"] = len(bat.encode("utf-8"))

    # 6.9: el asunto del ultimo commit del ejecutor antes del acta.
    c, padre = git(["rev-parse", "%s^" % acta])
    if c != 0:
        return None, "PARADA: no se pudo leer el padre del acta."
    c, asunto = git(["log", "-1", "--format=%s", padre.strip()])
    if c != 0 or not asunto.strip():
        return None, "PARADA: no se pudo leer el asunto del padre del acta."
    m["hash_ultima_tarea_167"] = padre.strip()
    m["asunto_ultima_tarea_167"] = asunto.strip()

    # LOS VEREDICTOS, COMPUTADOS. Ninguno es una constante literal.
    m["v_6_1_ocurrio"] = (m["vuelta_del_reporte"] == 167)
    m["v_6_3_ocurrio"] = (m["vuelta_del_reporte"] == 167)
    m["v_6_4_ocurrio"] = (m["bytes_bateria_167"] > 0)
    m["v_6_9_ocurrio"] = not m["asunto_ultima_tarea_167"].startswith("TAREA 5: PARADA")
    return m, None


def texto_de_la_nota(acta, asunto_acta, m):
    """La nota, con cada cifra puesta desde la medicion y ninguna tecleada."""
    no_ocurrieron = [c for c, k in (("6.1", "v_6_1_ocurrio"), ("6.3", "v_6_3_ocurrio"),
                                    ("6.4", "v_6_4_ocurrio"), ("6.9", "v_6_9_ocurrio"))
                     if not m[k]]
    si_ocurrieron = [c for c, k in (("6.1", "v_6_1_ocurrio"), ("6.3", "v_6_3_ocurrio"),
                                    ("6.4", "v_6_4_ocurrio"), ("6.9", "v_6_9_ocurrio"))
                     if m[k]]
    linea_si = ("**Y SE DICE CUANTAS DE LAS CUATRO SI OCURRIERON, PORQUE LA CIFRA SALE DE LA\n"
                "MEDICION Y NO DE LA ADJUDICACION: NINGUNA.**"
                if not si_ocurrieron else
                "**PERO LA MEDICION NO CONFIRMA LA ADJUDICACION ENTERA: %s SI OCURRIO SEGUN\n"
                "GIT, Y ESO SE PUBLICA EN VEZ DE CALLARSE.**" % ", ".join(si_ocurrieron))

    return (
        "\n**%s.**\n"
        "Corte de todas las cifras de esta nota: 4 sep 2026. Hash de la parada, leido de\n"
        "`git log` en esta vuelta y no tecleado: **`%s`**, *\"%s\"*.\n"
        "**NINGUNA PALABRA DE ESTA ENTRADA SE BORRA NI SE REESCRIBE, y la nota va al\n"
        "final por el carril del banco 9.10.** Lo que la nota dice es esto: **las glosas\n"
        "de la `%s` de esta misma entrada describen LO ENCARGADO y no LO\n"
        "OCURRIDO.** Estan escritas en pasado porque el commit de la TAREA 1 de la vuelta\n"
        "167 las escribio ANTES de que las tareas 2, 3 y 5 corrieran, y despues no\n"
        "corrieron como decian. **CADA UNA VA CON SU MEDICION AL LADO, corrida contra git\n"
        "en la vuelta 168 y no copiada del acta:**\n\n"
        "  - **`6.1` y `6.3` decian que el `REPORTE.md` de la vuelta 167 cubre las dos\n"
        "    vueltas y cita las salidas selladas.** MEDICION: `git show %s:docs/loop/REPORTE.md`\n"
        "    da como primera linea *\"%s\"*, o sea que aquel `REPORTE.md` era **el de la\n"
        "    vuelta %d**. La deuda de las dos vueltas la paga la TAREA 2 de la vuelta 168.\n"
        "  - **`6.4` decia que la bateria de verdad se corre en esa vuelta.** MEDICION:\n"
        "    `docs/loop/SALIDA_V167_BATERIA.txt` en el arbol de `%s` mide **%d bytes**. Un\n"
        "    fichero vacio no es una corrida, y la propia entrada ya lo decia de la 166.\n"
        "    La bateria se corre entera en la TAREA 3 de la vuelta 168.\n"
        "  - **`6.9` decia \"EJECUTADA EN EJECUCION, TAREA 5 de esta vuelta\".** MEDICION:\n"
        "    el ultimo commit del ejecutor antes del acta es `%s` y su asunto es\n"
        "    *\"%s\"*. **La TAREA 5 termino en PARADA**, y el acta 167 la adjudico a favor\n"
        "    del ejecutor en su `6.1`.\n\n"
        "**LAS QUE NO OCURRIERON, CONTADAS Y NO TECLEADAS: %d de 4 (%s).** %s\n"
        "**Y LO QUE ESTA NOTA NO HACE:** no reabre el `R.36`, no mueve ninguna clase, no\n"
        "toca ningun `estado` y no borra ni una linea. La leccion, que muerde a\n"
        "cualquiera y por eso se escribe entera: **una glosa que dice lo que una tarea VA\n"
        "a hacer no se escribe en pasado antes de que la tarea corra.**\n"
        % (MARCA, acta[:8], asunto_acta, "`, la `".join(["6.1", "6.3", "6.4", "6.9"]),
           acta[:8], m["primera_linea_del_reporte"], m["vuelta_del_reporte"],
           acta[:8], m["bytes_bateria_167"],
           m["hash_ultima_tarea_167"][:8], m["asunto_ultima_tarea_167"],
           len(no_ocurrieron), ", ".join(no_ocurrieron), linea_si))


def main():
    print("=" * 78)
    print("VUELTA 168, TAREA 1: LA NOTA ADOSADA AL R.36 (adjudicacion 6.5 del acta 167)")
    print("=" * 78)
    print("")

    par, err = hash_del_acta_167()
    if err:
        print(err)
        return 1
    acta, asunto_acta = par
    print("A) EL HASH DE LA PARADA, LEIDO DE GIT")
    print("   %s  %s" % (acta[:8], asunto_acta[:90]))
    print("")

    print("B) LAS CUATRO GLOSAS, CONTRASTADAS CONTRA GIT Y NO CONTRA EL ACTA")
    m, err = medir_las_cuatro(acta)
    if err:
        print("   " + err)
        return 1
    print("   REPORTE.md en el arbol del acta: primera linea dice VUELTA %d"
          % m["vuelta_del_reporte"])
    print("   SALIDA_V167_BATERIA.txt en ese arbol: %d bytes" % m["bytes_bateria_167"])
    print("   ultimo commit del ejecutor antes del acta: %s  %s"
          % (m["hash_ultima_tarea_167"][:8], m["asunto_ultima_tarea_167"][:70]))
    print("")
    print("C) LOS VEREDICTOS, COMPUTADOS DE LAS MEDICIONES")
    for clave, k in (("6.1", "v_6_1_ocurrio"), ("6.3", "v_6_3_ocurrio"),
                     ("6.4", "v_6_4_ocurrio"), ("6.9", "v_6_9_ocurrio")):
        print("   %-4s OCURRIO: %s" % (clave, "SI" if m[k] else "NO"))
    n_no = len([k for k in ("v_6_1_ocurrio", "v_6_3_ocurrio", "v_6_4_ocurrio",
                            "v_6_9_ocurrio") if not m[k]])
    print("   CIFRA glosas que NO ocurrieron: %d de 4" % n_no)
    if n_no == 0:
        print("   NO SE ESCRIBE NADA: la medicion dice que las cuatro ocurrieron, asi")
        print("   que la adjudicacion 6.5 no tiene sujeto. SE DECLARA y se para.")
        return 1
    print("")

    texto = io.open(SEDE, encoding="utf-8").read()
    if MARCA in texto:
        print("YA ESTABA: la nota vive en %s. No se toca." % SEDE)
        print("CIFRA notas escritas: 0")
        return 0

    print("D) LA ENTRADA R.36, LOCALIZADA Y ACOTADA ANTES DE ESCRIBIR")
    lineas = texto.split("\n")
    inicios = [i for i, l in enumerate(lineas) if l.startswith(CABECERA_R36)]
    if len(inicios) != 1:
        print("   PARADA: la cabecera del R.36 aparece %d veces." % len(inicios))
        return 1
    ini = inicios[0]
    sig = [i for i, l in enumerate(lineas) if i > ini and re.match(r"^## R\.\d+\. ", l)]
    fin = min(sig) if sig else len(lineas)
    print("   R.36 en docs/PENDIENTES.md, lineas %d a %d" % (ini + 1, fin))
    largo_antes = len(lineas)
    print("   CIFRA lineas del fichero ANTES: %d" % largo_antes)
    print("")

    nota = texto_de_la_nota(acta, asunto_acta, m)
    # LA NOTA VA AL FINAL DE LA ENTRADA, ANTES DE LA SIGUIENTE. Se inserta; el
    # texto de la entrada NO se toca en ningun punto.
    cuerpo_viejo = "\n".join(lineas[ini:fin])
    nuevas = lineas[:fin] + nota.split("\n") + lineas[fin:]
    salida = "\n".join(nuevas)
    io.open(SEDE, "w", encoding="utf-8", newline="\n").write(salida)

    print("E) ESCRITO, Y COMPROBADO QUE NADA VIEJO SE PERDIO")
    relee = io.open(SEDE, encoding="utf-8").read()
    print("   el cuerpo viejo del R.36 sigue ENTERO dentro del nuevo: %s"
          % ("SI" if cuerpo_viejo in relee else "NO"))
    if cuerpo_viejo not in relee:
        print("   PARADA: se perdio texto viejo. Esto no puede pasar.")
        return 1
    print("   la marca de la nota esta: %s" % ("SI" if MARCA in relee else "NO"))
    print("   CIFRA lineas del fichero DESPUES: %d lineas por count(NL), que calza con wc -l, y %d por len(split(NL))"
          % (relee.count("\n"), len(relee.split("\n"))))
    print("   CIFRA lineas anadidas: %d (la resta cancela el uno de mas de\n   len(split(NL)), porque largo_antes se conto igual)"
          % (len(relee.split("\n")) - largo_antes))
    print("   CIFRA lineas borradas: 0 (la escritura es una INSERCION)")
    print("   CIFRA notas escritas: 1")
    print("")
    print("VERDE: la nota queda adosada al R.36 sin borrar ni una palabra.")
    return 0


# ---------------------------------------------------------------------------
# CASO POSITIVO POR MUTACION (EJECUTOR.md 1). NINGUN VEREDICTO ES CONSTANTE: se
# llama a la MISMA funcion de veredicto con mediciones fabricadas en memoria y
# se comprueba que el veredicto SIGUE A LA MEDICION. Cero escrituras.
# ---------------------------------------------------------------------------

def _veredictos(vuelta_reporte, bytes_bateria, asunto):
    """La misma aritmetica de veredicto de `medir_las_cuatro`, aislada para
    poder darle sujetos fabricados. Si esta funcion y la de arriba se separan,
    el arnes deja de probar lo que corre, asi que se comprueba tambien que
    coinciden sobre la medicion REAL."""
    return {
        "6.1": vuelta_reporte == 167,
        "6.3": vuelta_reporte == 167,
        "6.4": bytes_bateria > 0,
        "6.9": not asunto.startswith("TAREA 5: PARADA"),
    }


def prueba_de_mutacion():
    print("=" * 78)
    print("VUELTA 168, TAREA 1: CASO POSITIVO POR MUTACION DE LA NOTA DEL R.36")
    print("=" * 78)
    print("")
    casos = []

    print("A) EL VEREDICTO SIGUE A LA MEDICION Y NO A UNA CONSTANTE")
    sujetos = [
        ("reporte de la 167, bateria con 4.000 bytes, tarea 5 normal",
         167, 4000, "TAREA 5: OP-C-01 ejecutada", 4),
        ("reporte de la 165, bateria vacia, tarea 5 en parada (EL CASO REAL)",
         165, 0, "TAREA 5: PARADA. OP-C-01 no se puede ejecutar", 0),
        ("reporte de la 167 pero bateria vacia",
         167, 0, "TAREA 5: OP-C-01 ejecutada", 3),
        ("reporte de la 166, bateria llena, tarea 5 normal",
         166, 900, "TAREA 5: algo", 2),
    ]
    for rotulo, vr, bb, asu, esperado in sujetos:
        v = _veredictos(vr, bb, asu)
        cuantas = len([k for k in v if v[k]])
        print("   %-58s -> ocurrieron %d de 4" % (rotulo[:58], cuantas))
        casos.append(("A_%d_%d_ocurren_%d" % (vr, bb, esperado), cuantas, esperado))
    print("")

    print("B) LA MEDICION REAL, LEIDA DE GIT HOY")
    par, err = hash_del_acta_167()
    if err:
        print("   " + err)
        return 1
    acta, _asunto = par
    m, err = medir_las_cuatro(acta)
    if err:
        print("   " + err)
        return 1
    print("   vuelta del reporte de aquel arbol: %d" % m["vuelta_del_reporte"])
    print("   bytes de la bateria de la 167:     %d" % m["bytes_bateria_167"])
    print("   asunto de la ultima tarea:         %s" % m["asunto_ultima_tarea_167"][:60])
    casos.append(("B_el_reporte_de_aquel_arbol_era_el_de_la_165",
                  m["vuelta_del_reporte"], 165))
    casos.append(("B_la_bateria_de_la_167_media_cero_bytes", m["bytes_bateria_167"], 0))
    casos.append(("B_la_tarea_5_empieza_por_TAREA_5_PARADA",
                  m["asunto_ultima_tarea_167"].startswith("TAREA 5: PARADA"), True))
    reales = _veredictos(m["vuelta_del_reporte"], m["bytes_bateria_167"],
                         m["asunto_ultima_tarea_167"])
    casos.append(("B_ninguna_de_las_cuatro_ocurrio",
                  len([k for k in reales if reales[k]]), 0))
    # LA FUNCION AISLADA Y LA QUE CORRE TIENEN QUE COINCIDIR SOBRE EL SUJETO REAL
    casos.append(("B_el_arnes_mide_lo_mismo_que_el_instrumento",
                  [reales["6.1"], reales["6.3"], reales["6.4"], reales["6.9"]],
                  [m["v_6_1_ocurrio"], m["v_6_3_ocurrio"], m["v_6_4_ocurrio"],
                   m["v_6_9_ocurrio"]]))
    print("")

    print("C) LA NOTA CAMBIA SI CAMBIA LA MEDICION")
    n1 = texto_de_la_nota(acta, "asunto", m)
    m2 = dict(m)
    m2["bytes_bateria_167"] = 4321
    m2["v_6_4_ocurrio"] = True
    n2 = texto_de_la_nota(acta, "asunto", m2)
    casos.append(("C_la_nota_no_es_la_misma_con_otra_medicion", n1 == n2, False))
    casos.append(("C_la_nota_real_dice_4_de_4", "TECLEADAS: 4 de 4" in n1, True))
    casos.append(("C_la_nota_mutada_dice_3_de_4", "TECLEADAS: 3 de 4" in n2, True))
    casos.append(("C_la_nota_mutada_nombra_la_que_si_ocurrio",
                  "6.4 SI OCURRIO" in n2, True))
    casos.append(("C_la_nota_real_dice_que_ninguna_ocurrio",
                  "NINGUNA.**" in n1, True))
    print("   nota real: 4 de 4 no ocurrieron | nota mutada: 3 de 4, y nombra la 6.4")
    print("")

    print("D) PASADA 1, LOS CASOS TAL CUAL")
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

    print("E) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, list):
            mutado = [not x for x in esperado]
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
    sys.stdout.reconfigure(encoding="utf-8")
    if "--mutar" in sys.argv:
        sys.exit(prueba_de_mutacion())
    sys.exit(main())
