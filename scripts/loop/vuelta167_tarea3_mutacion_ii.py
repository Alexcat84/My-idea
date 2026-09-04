# -*- coding: utf-8 -*-
r"""vuelta167_tarea3_mutacion_ii.py . CASO POSITIVO POR MUTACION DEL ARREGLO DE
LA COMPROBACION ii (TAREA 3 de la vuelta 167; acta 166, adjudicacion 6.5).

LA LETRA QUE TIENE QUE CUMPLIR, Y ESTA COPIADA DEL ENCARGO: *"CON SU CASO
POSITIVO POR MUTACION, y el caso tiene que CAERSE si alguien devuelve el ultimo
gana"*. Y `EJECUTOR.md` 1, *"EL CASO ROJO SE PRUEBA POR MUTACION"*, prohibe
publicar un assert cuyo veredicto sea una constante literal: en la vuelta 89 se
publico como prueba un `veredicto_2 = "ENTRA"` comparado contra `"ENTRA"`, que no
puede salir en rojo nunca.

POR ESO AQUI NO SE COMPARAN CONSTANTES: se CORRE DOS VECES EL INSTRUMENTO REAL
sobre el archivo real, una con la fuente de hoy y otra con una copia a la que se
le ha QUITADO EL ARREGLO por cirugia de texto, y se lee el veredicto del pie de
cada corrida.

  - `scripts/plan/recomputo_3388.py` (la fuente arreglada) tiene que dar
    `ii ... OK` y `LAS CUATRO: TODAS OK`.
  - `scripts/loop/_v167_recomputo_ultimo_gana_copia.py` (la MISMA fuente con el
    ultimo gana devuelto) tiene que dar `ii ... FALLA` y
    `LAS CUATRO: AL MENOS UNA FALLA`.

Y LA CIRUGIA SE COMPRUEBA A SI MISMA: si el arreglo desapareciera de la fuente,
la copia saldria IDENTICA al original y este arnes PARA EN ROJO en vez de
aprobarse solo. Esa es justamente la propiedad que la vuelta 89 no tuvo.

CERO ESCRITURAS FUERA DE SU SITIO: la copia mutada y los jsonl de componentes se
escriben bajo `scripts/loop/` y `docs/loop/` con prefijo `_v167_`, y no se toca
ni un nodo, ni un veredicto, ni la nomina sellada de `docs/plan/`.

USO:  python scripts/loop/vuelta167_tarea3_mutacion_ii.py
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FUENTE = os.path.join(RAIZ, "scripts", "plan", "recomputo_3388.py")
COPIA = os.path.join(RAIZ, "scripts", "loop", "_v167_recomputo_ultimo_gana_copia.py")

# LA MARCA DEL ARREGLO, tal como vive hoy en la fuente. Es lo que la cirugia
# quita para devolver el ultimo gana.
ARREGLO = '''        k = frozenset((ra, rb))
        previo = leido.get(k)
        if previo is not None and previo["clase"] == "A" and r["clase"] != "A":
            continue          # LA A NO SE PIERDE: marca de la correccion de la 167
        leido[k] = r
'''
ULTIMO_GANA = '''        leido[frozenset((ra, rb))] = r
'''


def correr(script, salida):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, script, "--salida", salida],
                       cwd=RAIZ, capture_output=True, env=env)
    salida = (r.stdout.decode("utf-8", "replace") + r.stderr.decode("utf-8", "replace"))
    # LOS FINALES DE LINEA SE NORMALIZAN ANTES DE LEER EL PIE. En Windows la
    # captura trae retorno de carro y salto, y un cierre de linea de re.M no
    # casa con un retorno de carro delante: el pie se leia como None y el
    # arnes moria por TypeError en vez de decir por que.
    return salida.replace("\r\n", "\n")


def lee_ii(texto):
    """Del pie del instrumento, no de una constante. Devuelve (retrato, internas,
    veredicto_ii, veredicto_de_las_cuatro)."""
    m = re.search(r"^ii\. A vigentes resueltas del retrato \((\d+)\) == suma de "
                  r"aristas A internas de las componentes \((\d+)\): (\w+)$",
                  texto, re.M)
    c = re.search(r"^LAS CUATRO: (.+)$", texto, re.M)
    if not m or not c:
        return None, None, None, None
    return int(m.group(1)), int(m.group(2)), m.group(3), c.group(1).strip()


def lee_las_cuatro(texto):
    """Las CUATRO comprobaciones, cada una con su veredicto, leidas del pie."""
    fuera = {}
    for etq in ("i", "ii", "iii", "iv"):
        m = re.search(r"^%s\. .*?: (OK|FALLA)" % etq, texto, re.M)
        fuera[etq] = m.group(1) if m else None
    return fuera


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 167, TAREA 3: CASO POSITIVO POR MUTACION DE LA COMPROBACION ii")
    print("=" * 78)
    print("")
    casos = []

    print("A) LA CIRUGIA, Y SE COMPRUEBA A SI MISMA ANTES DE CORRER NADA")
    texto = io.open(FUENTE, encoding="utf-8").read()
    veces = texto.count(ARREGLO)
    print("   veces que la marca del arreglo aparece en la fuente: %d" % veces)
    if veces != 1:
        print("   ROJO: el arreglo no esta en la fuente exactamente una vez. Si")
        print("   alguien lo quito, este arnes NO se aprueba solo: para aqui.")
        return 1
    mutado = texto.replace(ARREGLO, ULTIMO_GANA)
    print("   la copia mutada difiere del original: %s" % (mutado != texto))
    casos.append(("A_la_cirugia_cambia_el_texto", mutado != texto, True))
    io.open(COPIA, "w", encoding="utf-8", newline="\n").write(mutado)
    print("   escrita: scripts/loop/_v167_recomputo_ultimo_gana_copia.py")
    print("")

    print("B) LAS DOS CORRIDAS, SOBRE EL ARCHIVO REAL Y CON EL INSTRUMENTO REAL")
    sal_ok = "docs/loop/_v167_t3_mut_componentes_arreglado.jsonl"
    sal_mu = "docs/loop/_v167_t3_mut_componentes_ultimo_gana.jsonl"
    t_ok = correr(FUENTE, sal_ok)
    t_mu = correr(COPIA, sal_mu)
    r_ok, a_ok, v_ok, c_ok = lee_ii(t_ok)
    r_mu, a_mu, v_mu, c_mu = lee_ii(t_mu)
    print("   FUENTE ARREGLADA : retrato %s, aristas A internas %s, ii %s, pie %r"
          % (r_ok, a_ok, v_ok, c_ok))
    print("   ULTIMO GANA      : retrato %s, aristas A internas %s, ii %s, pie %r"
          % (r_mu, a_mu, v_mu, c_mu))
    print("")

    print("C) LOS CASOS, CADA UNO CON SU VALOR LEIDO DEL PIE DE UNA CORRIDA")
    casos.append(("C_arreglada_ii_dice_OK", v_ok, "OK"))
    casos.append(("C_arreglada_las_cuatro_TODAS_OK", c_ok, "TODAS OK"))
    casos.append(("C_arreglada_las_dos_mitades_son_iguales", r_ok == a_ok, True))
    casos.append(("C_ultimo_gana_ii_dice_FALLA", v_mu, "FALLA"))
    casos.append(("C_ultimo_gana_las_cuatro_AL_MENOS_UNA_FALLA",
                  c_mu, "AL MENOS UNA FALLA"))
    casos.append(("C_ultimo_gana_las_dos_mitades_NO_son_iguales", r_mu == a_mu, False))
    casos.append(("C_el_retrato_no_se_mueve_entre_las_dos", r_ok == r_mu, True))
    casos.append(("C_lo_que_se_mueve_son_las_aristas_internas", a_ok - a_mu, 3))
    cuatro_ok = lee_las_cuatro(t_ok)
    cuatro_mu = lee_las_cuatro(t_mu)
    print("   LAS CUATRO con la fuente arreglada: %s" % cuatro_ok)
    print("   LAS CUATRO con el ultimo gana     : %s" % cuatro_mu)
    casos.append(("C_arreglada_las_cuatro_en_verde",
                  sorted(cuatro_ok.values()), ["OK"] * 4))
    casos.append(("C_ultimo_gana_solo_la_ii_cae",
                  [k for k, v in cuatro_mu.items() if v == "FALLA"], ["ii"]))
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
            mut = not esperado
        elif isinstance(esperado, int):
            mut = esperado + 1
        elif isinstance(esperado, list):
            mut = esperado + ["_mutado"]
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
        print("Y LO QUE IMPORTA, DICHO CON SU CIFRA: devolver el ultimo gana baja las")
        print("aristas A internas de %s a %s y pone la ii en FALLA." % (a_ok, a_mu))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    sys.exit(main())
