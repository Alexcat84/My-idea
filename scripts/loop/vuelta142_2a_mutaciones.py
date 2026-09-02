# -*- coding: utf-8 -*-
r"""vuelta142_2a_mutaciones.py . LA PRUEBA DE MUTACION DE LA TAREA 2.a de la
vuelta 142 (acta de la vuelta 141, caida 4.5 del auditor: la guarda de cifras
cotejaba CERO y salia VERDE).

CUATRO CASOS, DOS POR PIEZA, y los cuatro sobre VALOR COMPUTADO, nunca sobre un
literal (EJECUTOR.md 1, "EL CASO ROJO SE PRUEBA POR MUTACION"). Ninguna
expectativa esta escrita a mano: cada caso vuelve a llamar a la guarda y compara
lo que ella devuelve.

  (i.a) MUTACION DE CIFRA. Sobre una COPIA del reporte de prueba, se cambia el
        NUMERO de una cifra en `direcciones` que SI cita su fichero
        (docs/loop/SALIDA_V142_1B_DESGLOSE_DIRECCIONES.txt, que publica su linea
        `CIFRA ...: 17 direcciones`). Tiene que salir ROJO NOMBRANDO LA LINEA.
        El numero mutado se COMPUTA (`bueno + 1`), no se teclea.
  (i.b) CONTRAPRUEBA de (i.a): la misma copia SIN mutar. Esa cifra tiene que
        salir COTEJADA y sin ningun fallo de cifra.
  (ii.a) COBERTURA CERO. Un reporte de prueba SIN ninguna cifra cotejable.
        Tiene que salir ROJO por cobertura cero, con el fallo nombrado.
  (ii.b) CONTRAPRUEBA de (ii.a): el mismo reporte con UNA cifra cotejable
        anadida. El fallo de cobertura cero tiene que DESAPARECER.

P.16, QUIEN FABRICA LIMPIA: los reportes de prueba se escriben en docs/loop/ con
un nombre que NO casa con `SALIDA_V*.txt` (para no entrar en el glob de
`ficheros_salida_existentes`) y se borran en el `finally`, pase lo que pase. El
fichero de salida que se cita SI existe de verdad y NO se toca: es el de la
TAREA 1.b de esta misma vuelta.

POR QUE LOS REPORTES DE PRUEBA VIVEN EN docs/loop/ y no en un temporal del
sistema: la guarda resuelve las citas contra `docs/loop/`, asi que un reporte
fuera de ahi no podria citar ningun instrumento real y (i) no se podria probar.

USO:
  python scripts/loop/vuelta142_2a_mutaciones.py
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_cifras_del_reporte as V

LOOP = V.LOOP
FICHERO_CITADO = "SALIDA_V142_1B_DESGLOSE_DIRECCIONES.txt"
UNIDAD = "direcciones"

# Los reportes de prueba: nombre que NO casa con SALIDA_V*.txt (P.16 y para no
# envenenar el glob de la propia guarda, que es la caida que
# verificar_apertura_sellada.py ya sufrio en la vuelta 102).
PRUEBA_A = os.path.join(LOOP, "_prueba_v142_2a_reporte.md")
PRUEBA_B = os.path.join(LOOP, "_prueba_v142_2a_cobertura.md")


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def cifra_buena_del_fichero():
    """EL VALOR ESPERADO SE COMPUTA DEL FICHERO CITADO, no se teclea: se lee su
    primera linea `CIFRA <etiqueta>: <n> direcciones`. Si el fichero dejara de
    publicarla, esto CAE con su nombre en vez de seguir con un numero viejo."""
    contenido = V.leer(os.path.join(LOOP, FICHERO_CITADO))
    candidatas = V.cifras_etiquetadas(contenido, UNIDAD)
    if not candidatas:
        raise SystemExit(
            "ROJO (arnes): %s no publica ninguna linea `CIFRA <etiqueta>: <n> %s`. "
            "Sin sujeto no hay mutacion y ESO ES ROJO, no verde." % (FICHERO_CITADO, UNIDAD))
    return candidatas[0]


def cuerpo_reporte(numero, etiqueta):
    """El reporte de prueba, con la cifra y su cita en la MISMA frase para que
    caiga en la ventana forward-only de la guarda."""
    return (
        u"# REPORTE DE PRUEBA (fabricado por vuelta142_2a_mutaciones.py)\n\n"
        u"El universo 1 da %d %s, medido en `%s` (linea CIFRA '%s').\n"
        % (numero, UNIDAD, FICHERO_CITADO, etiqueta))


def correr(ruta):
    """CORRE LA GUARDA DE VERDAD, COMO SUBPROCESO, y devuelve
    (exit, lineas_de_fallo, cotejadas, total_vistas).

    POR QUE SUBPROCESO Y NO LLAMAR A `verificar()` A SECAS, y va escrito porque
    es justo el defecto que EJECUTOR.md 1 castiga ("EL CASO ROJO SE PRUEBA POR
    MUTACION... ningun assert se publica como prueba sin haber corrido su prueba
    de mutacion"): la pieza (ii), CERO COTEJADAS DEJA DE SER VERDE, vive en el
    `main()` de la guarda, NO en `verificar()`. Un caso que llamara a
    `verificar()` y luego re-implementara aqui la regla de cobertura cero
    estaria probando SU PROPIA COPIA de la regla y saldria verde aunque la
    guarda no la tuviera. Corriendo el ejecutable se prueba el veredicto que la
    guarda publica de verdad: su EXIT y sus lineas."""
    r = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      "verificar_cifras_del_reporte.py"),
         "--reporte", ruta],
        cwd=V.RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace")
    salida = (r.stdout or "") + (r.stderr or "")
    # Los FALLOS son las lineas sangradas que van DEBAJO de la cabecera "ROJO,"
    # y hasta la linea COBERTURA. Recogerlas por sangria a secas metia tambien
    # el detalle de las COTEJADAS del camino verde, y eso hacia caer la
    # contraprueba (i.b) por un defecto de este arnes, no de la guarda.
    fallos = []
    dentro = False
    for l in salida.split("\n"):
        if l.startswith("ROJO,"):
            dentro = True
            continue
        if not dentro:
            continue
        if l.startswith("COBERTURA:") or (l and not l.startswith(" ")):
            dentro = False
            continue
        if l.strip():
            fallos.append(l.strip())
    m = re.search(r"COBERTURA:\s*(\d+) cotejadas / (\d+) exentas / (\d+) cifras", salida)
    cotejadas = int(m.group(1)) if m else -1
    total = int(m.group(3)) if m else -1
    return r.returncode, fallos, cotejadas, total, salida


def nombra_la_linea(fallos, numero, unidad):
    """Computado: hay algun fallo que nombre a la vez el numero mutado y la
    unidad. No se compara contra una frase tecleada entera."""
    patron = re.compile(r"\"%d\s+%s\"" % (numero, re.escape(unidad)))
    return [f for f in fallos if patron.search(f)]


def hay_cobertura_cero(fallos):
    return [f for f in fallos if f.startswith("COBERTURA CERO")]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    resultados = []
    try:
        etiqueta, bueno = cifra_buena_del_fichero()
        malo = bueno + 1  # COMPUTADO del valor bueno, no tecleado.
        print("=" * 78)
        print("MUTACIONES DE LA TAREA 2.a | vuelta 142")
        print("La guarda se corre COMO SUBPROCESO: se prueba su EXIT y sus lineas,")
        print("no una copia de su regla (ver el docstring de correr()).")
        print("Fichero citado: %s | linea CIFRA elegida: '%s' | valor bueno COMPUTADO: %d"
              % (FICHERO_CITADO, etiqueta, bueno))
        print("Valor mutado, COMPUTADO como bueno mas uno: %d" % malo)
        print("=" * 78)

        # ---------------- (i.b) CONTRAPRUEBA PRIMERO, sin mutar -------------
        escribir(PRUEBA_A, cuerpo_reporte(bueno, etiqueta))
        exit_b, fallos_b, cot_b, tot_b, _s = correr(PRUEBA_A)
        ok = (exit_b == 0) and cot_b == 1 and not fallos_b
        resultados.append(("i.b CONTRAPRUEBA sin mutar: EXIT 0 y la cifra buena COTEJADA", ok))
        print("")
        print("(i.b) sin mutar -> EXIT %d | cotejadas %d | vistas %d" % (exit_b, cot_b, tot_b))
        for f in fallos_b:
            print("      %s" % f)

        # ---------------- (i.a) LA MUTACION DE CIFRA ------------------------
        escribir(PRUEBA_A, cuerpo_reporte(malo, etiqueta))
        exit_a, fallos_a, cot_a, tot_a, _s = correr(PRUEBA_A)
        nombrados = nombra_la_linea(fallos_a, malo, UNIDAD)
        ok = (exit_a == 1) and bool(nombrados) and cot_a == 0
        resultados.append(("i.a MUTADA: EXIT 1 y ROJO NOMBRANDO la linea de la cifra mutada", ok))
        print("")
        print("(i.a) mutada a %d -> EXIT %d | cotejadas %d | vistas %d"
              % (malo, exit_a, cot_a, tot_a))
        for f in fallos_a:
            print("      %s" % f)

        # ---------------- (ii.a) COBERTURA CERO -----------------------------
        sin_cifras = (u"# REPORTE DE PRUEBA SIN CIFRAS COTEJABLES\n\n"
                      u"Esta pagina no publica ninguna cifra con unidad del vocabulario.\n"
                      u"Habla de la vuelta y de la rama y de nada mas.\n")
        escribir(PRUEBA_B, sin_cifras)
        exit_c, fallos_c, cot_c, tot_c, _s = correr(PRUEBA_B)
        cero = hay_cobertura_cero(fallos_c)
        ok = (exit_c == 1) and bool(cero) and cot_c == 0 and tot_c == 0
        resultados.append(("ii.a SIN cifras cotejables: EXIT 1 por COBERTURA CERO", ok))
        print("")
        print("(ii.a) sin cifras -> EXIT %d | cotejadas %d | vistas %d" % (exit_c, cot_c, tot_c))
        for f in fallos_c:
            print("      %s" % f)

        # ---------------- (ii.b) CONTRAPRUEBA de la cobertura ---------------
        escribir(PRUEBA_B, sin_cifras + u"\n" + cuerpo_reporte(bueno, etiqueta))
        exit_d, fallos_d, cot_d, tot_d, _s = correr(PRUEBA_B)
        ok = (exit_d == 0) and (not hay_cobertura_cero(fallos_d)) and cot_d == 1
        resultados.append(("ii.b CONTRAPRUEBA con UNA cifra cotejable: EXIT 0, el fallo de "
                           "cobertura cero DESAPARECE", ok))
        print("")
        print("(ii.b) con una cifra -> EXIT %d | cotejadas %d | vistas %d"
              % (exit_d, cot_d, tot_d))
        for f in fallos_d:
            print("      %s" % f)
    finally:
        # P.16: quien fabrica, limpia. Pase lo que pase.
        for p in (PRUEBA_A, PRUEBA_B):
            if os.path.exists(p):
                os.remove(p)

    print("")
    print("=" * 78)
    verdes = 0
    for nombre, ok in resultados:
        print("  %-5s %s" % ("VERDE" if ok else "ROJO", nombre))
        verdes += 1 if ok else 0
    print("CIFRA de la bateria 2.a: %d comprobaciones" % len(resultados))
    print("CIFRA verdes de la bateria 2.a: %d comprobaciones" % verdes)
    print("=" * 78)
    if verdes != len(resultados):
        print("ROJO: %d de %d casos no se comportan como la guarda promete."
              % (len(resultados) - verdes, len(resultados)))
        return 1
    print("VERDE: los %d casos se comportan." % len(resultados))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
