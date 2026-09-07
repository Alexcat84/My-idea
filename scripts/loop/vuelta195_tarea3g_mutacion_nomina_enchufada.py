# -*- coding: utf-8 -*-
r"""vuelta195_tarea3g_mutacion_nomina_enchufada.py . CASO POSITIVO POR MUTACION
DE LA COSA QUE FALLABA HOY: **QUE LA MIRADA DE LA NOMINA SOBRE SI MISMA CAIGA
CUANDO UN ARNES QUE EL CENSO VE SE QUEDA FUERA DE LA NOMINA SIN SER CASO
DECLARADO** (TAREA 3.g de la vuelta 195).

POR QUE EXISTE ESTE FICHERO Y NO UN FLAG: la bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS.

QUE PRUEBA, Y POR QUE NO BASTABA CON LO QUE YA HABIA. `prueba_de_la_nomina()` ya
comprueba que `arneses_que_faltan()` VE a los que estan fuera. **Eso es la mitad.**
La otra mitad es que ese ver **ESTE ENCHUFADO AL VEREDICTO**, y esa mitad no
estaba probada por nada: la unica forma de saberlo era correr la bateria entera y
mirar el color, que es justo lo que la adjudicacion `4.4` del acta 190 llama
inaceptable. Aqui se prueba el cable, pieza a pieza, apagandolo y encendiendolo.

Y LA TERCERA COSA, QUE ES LA QUE EL ENCARGO SUBRAYA: **QUE SER `CASO DECLARADO`
NO SEA UNA PUERTA TRASERA PARA SALIRSE DE LA NOMINA.** `arneses_que_faltan()` NO
consulta `CASOS_DECLARADOS`, y eso hay que probarlo en vez de leerlo: un arnes
declarado que no este en la nomina TIENE que seguir saliendo como que falta.

SUJETO CONGELADO (condicion de la vuelta 148): todo ocurre sobre un directorio
FABRICADO con `mkdtemp` y nominas FABRICADAS en memoria. **Ni este fichero, ni
`scripts/loop/`, ni ningun dato de la campana se leen ni se tocan**, y `P.16`
(quien fabrica limpia) retira el temporal al salir.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: todos los reales salen de llamar a
`arneses_que_faltan()`, `hay_rojo_al_cierre()` y `clase_del_rojo()`, y la segunda
pasada MUTA el valor esperado de cada caso y exige que CAIGA.

USO:
  python scripts/loop/vuelta195_tarea3g_mutacion_nomina_enchufada.py
"""
import io
import os
import shutil
import sys
import tempfile

NL = chr(10)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as V   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
SALIDA = os.path.join(LOOP, "SALIDA_V195_T3G_MUTACION_NOMINA_ENCHUFADA.txt")

# LA SEPARACION VACIA, que es lo que `guarda_del_sujeto_congelado_separada()`
# devuelve cuando no hay ninguna deuda. Va aqui como constante FABRICADA para que
# `clase_del_rojo()` se pueda llamar sin tocar el repo.
SEPARADA_LIMPIA = {"sujeto_vivo": [], "con_motivo": [], "sin_motivo": []}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 195, TAREA 3.g: CASO POSITIVO POR MUTACION DE QUE LA MIRADA DE LA")
    w("NOMINA SOBRE SI MISMA ESTE ENCHUFADA AL VEREDICTO")
    w("=" * 78)
    w("")

    tmp = tempfile.mkdtemp(prefix="v195_nomina_")
    casos = []
    try:
        # ------------------------------------------------ EL SUJETO FABRICADO
        nombres = ("vuelta200_tarea1_mutacion_dentro.py",
                   "vuelta201_tarea2_mutacion_fuera.py",
                   "vuelta202_tarea3_mutacion_declarada_y_fuera.py",
                   "vuelta203_tarea4_un_script_cualquiera.py")
        for n in nombres:
            io.open(os.path.join(tmp, n), "w", encoding="utf-8").write(
                "# de mentira" + NL)
        w("A) EL DIRECTORIO FABRICADO, QUE NO ES scripts/loop/")
        # EL NOMBRE DEL TEMPORAL NO SE IMPRIME, Y LA CAUSA ESTA MEDIDA: la
        # primera version de este arnes escribia `os.path.basename(tmp)` en su
        # salida sellada, y `mkdtemp` pone un sufijo distinto en cada corrida.
        # El cotejo de reproducibilidad de la vuelta 141 lo cazo en la corrida
        # acotada de la TAREA 3.f: dos corridas seguidas daban salidas
        # DISTINTAS y el arnes salio NO REPRODUCIBLE. Una salida sellada que
        # cambia sola no se puede cotejar con nada.
        w("   temporal: uno de `mkdtemp` con prefijo `v195_nomina_`. SU NOMBRE")
        w("   NO SE IMPRIME a proposito: lleva un sufijo distinto en cada")
        w("   corrida y haria esta salida IRREPRODUCIBLE.")
        w("   ficheros: %s" % ", ".join(sorted(os.listdir(tmp))))
        censo = V.arneses_del_directorio(tmp)
        w("   CIFRA arneses que el censo reconoce: %d (%s)"
          % (len(censo), ", ".join(censo)))
        w("   el cuarto NO es un arnes de mutacion y el censo NO lo cuenta.")
        casos.append(("el_censo_ve_los_TRES_arneses_y_no_el_cuarto", len(censo), 3))

        w("")
        w("B) LA NOMINA FABRICADA DEJA DOS FUERA, Y UNO DE ELLOS ES CASO DECLARADO")
        nomina = [("vuelta200_tarea1_mutacion_dentro.py", False)]
        declarados = {"vuelta202_tarea3_mutacion_declarada_y_fuera.py":
                      (2, "motivo de mentira", "MARCA DE MENTIRA")}
        w("   nomina:     %s" % ", ".join(n for n, _a in nomina))
        w("   declarados: %s" % ", ".join(sorted(declarados)))
        _u, faltan = V.arneses_que_faltan(nomina, tmp, vara=0)
        w("   CIFRA que faltan: %d (%s)" % (len(faltan), ", ".join(faltan)))
        casos.append(("ve_a_los_DOS_que_estan_fuera", faltan,
                      ["vuelta201_tarea2_mutacion_fuera.py",
                       "vuelta202_tarea3_mutacion_declarada_y_fuera.py"]))
        w("   Y LA QUE IMPORTA: SER CASO DECLARADO NO SACA A NADIE DE LA NOMINA.")
        w("   `arneses_que_faltan()` NO consulta CASOS_DECLARADOS, y por eso el")
        w("   declarado sigue saliendo. Una exencion de exitcode no es una")
        w("   exencion de estar en la nomina, y eso se prueba en vez de leerse.")
        casos.append(("el_declarado_sigue_faltando",
                      "vuelta202_tarea3_mutacion_declarada_y_fuera.py" in faltan,
                      True))

        w("")
        w("C) EL CABLE: CON ESA LISTA, EL VEREDICTO TIENE QUE SER ROJO")
        w("   Esto es lo que no estaba probado por nada, y es la mitad que")
        w("   importa: que VER a los que faltan MUEVA el veredicto. La unica")
        w("   forma de saberlo era correr la bateria entera y mirar el color.")
        rojo = V.hay_rojo_al_cierre([], [], [], faltan, [], [])
        clase = V.clase_del_rojo([], [], [], faltan, [], SEPARADA_LIMPIA)
        codigo = V.CODIGO_DE_LA_CLASE[clase]
        w("   hay_rojo_al_cierre(faltan=%d) -> %s" % (len(faltan), rojo))
        w("   clase_del_rojo(...)           -> %r (codigo %d)" % (clase, codigo))
        casos.append(("con_faltan_hay_rojo", rojo, True))
        casos.append(("y_la_clase_es_ROJO_POR_FALLO", clase, V.ROJO_POR_FALLO))
        casos.append(("y_su_codigo_de_salida_NO_es_cero", codigo != 0, True))
        w("   Y NO ES `ROJO POR DEUDA`: un hueco de censo es FALLO, no deuda, y")
        w("   la precedencia esta escrita en `clase_del_rojo()`.")
        casos.append(("y_NO_es_ROJO_POR_DEUDA", clase == V.ROJO_POR_DEUDA, False))

        w("")
        w("D) SE APAGA LA PIEZA Y EL ROJO TIENE QUE APAGARSE CON ELLA")
        w("   Si el rojo siguiera encendido con la lista vacia, este cable no")
        w("   probaria nada: estaria encendido por otra cosa.")
        rojo_sin = V.hay_rojo_al_cierre([], [], [], [], [], [])
        clase_sin = V.clase_del_rojo([], [], [], [], [], SEPARADA_LIMPIA)
        w("   hay_rojo_al_cierre(faltan=0) -> %s" % rojo_sin)
        w("   clase_del_rojo(...)          -> %r (codigo %d)"
          % (clase_sin, V.CODIGO_DE_LA_CLASE[clase_sin]))
        casos.append(("sin_faltan_no_hay_rojo", rojo_sin, False))
        casos.append(("y_la_clase_vuelve_a_VERDE", clase_sin, V.VERDE))
        casos.append(("y_su_codigo_es_cero", V.CODIGO_DE_LA_CLASE[clase_sin], 0))

        w("")
        w("E) SI LOS DOS ENTRAN EN LA NOMINA, DEJA DE FALTAR NADIE Y EL ROJO SE VA")
        w("   Es el escenario de esta misma vuelta: la TAREA 3.a metio SEIS en la")
        w("   nomina de verdad. Aqui se prueba la CONDUCTA sobre el fabricado.")
        completa = nomina + [("vuelta201_tarea2_mutacion_fuera.py", False),
                             ("vuelta202_tarea3_mutacion_declarada_y_fuera.py",
                              False)]
        _u2, faltan2 = V.arneses_que_faltan(completa, tmp, vara=0)
        w("   CIFRA que faltan tras meterlos: %d" % len(faltan2))
        casos.append(("metidos_en_la_nomina_ya_no_faltan", len(faltan2), 0))
        casos.append(("y_entonces_no_hay_rojo_por_esta_pieza",
                      V.hay_rojo_al_cierre([], [], [], faltan2, [], []), False))

        w("")
        w("F) Y LA VARA SIGUE PROTEGIENDO A LOS ANTERIORES, QUE NO SE AFLOJA")
        w("   Con la vara en 202, el de la 201 queda por debajo y no se reclama.")
        _u3, faltan3 = V.arneses_que_faltan(nomina, tmp, vara=202)
        w("   con la vara en 202, faltan: %d (%s)"
          % (len(faltan3), ", ".join(faltan3) or "ninguno"))
        casos.append(("la_vara_protege_al_anterior",
                      "vuelta201_tarea2_mutacion_fuera.py" in faltan3, False))
        casos.append(("y_el_de_la_202_si_se_reclama",
                      "vuelta202_tarea3_mutacion_declarada_y_fuera.py" in faltan3,
                      True))
        w("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        w("G) EL TEMPORAL SE RETIRA (P.16, quien fabrica limpia)")
        w("   sigue existiendo: %s" % ("SI" if os.path.isdir(tmp) else "NO"))
        casos.append(("el_temporal_queda_retirado", os.path.isdir(tmp), False))
        w("")

    w("H) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = real == esperado
        fallos += 0 if ok else 1
        w("   %-56s %-6s (real=%r esperado=%r)"
          % (nombre, "PASA" if ok else "FALLA", real, esperado))
    w("   CIFRA casos: %d | pasan: %d | fallan: %d"
      % (len(casos), len(casos) - fallos, fallos))
    w("")

    w("I) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    w("   Un caso que no cae al mutar su esperado no esta comprobando nada, que")
    w("   es la letra de EJECUTOR.md 1: EL CASO ROJO SE PRUEBA POR MUTACION.")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, list):
            mutado = esperado + ["vuelta999_tarea9_mutacion_de_mentira.py"]
        else:
            mutado = str(esperado) + " DE MENTIRA"
        cae = real != mutado
        caen += 1 if cae else 0
        w("   %-56s %-7s (esperado mutado=%r)"
          % (nombre, "CAE" if cae else "NO CAE", mutado))
    w("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    w("")

    ok = (fallos == 0 and caen == len(casos))
    w("CIFRA casos: %d | pasan: %d | fallan: %d"
      % (len(casos), len(casos) - fallos, fallos))
    if ok:
        w("VEREDICTO: VERDE")
        w("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
          % (len(casos), len(casos)))
    else:
        w("VEREDICTO: ROJO")
        w("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))

    t = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)"
          % (os.path.relpath(SALIDA, RAIZ).replace("\\", "/"),
             len(t.encode("utf-8"))))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
