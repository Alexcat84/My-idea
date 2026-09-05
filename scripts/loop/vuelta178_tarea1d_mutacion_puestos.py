# -*- coding: utf-8 -*-
r"""vuelta178_tarea1d_mutacion_puestos.py . EL CASO POSITIVO POR MUTACION DEL
CARRIL POR LISTA DE PUESTOS DE `aislador_de_ciega.py`, CON SU ROJO.

TAREA 1.d de la vuelta 178.

SUJETO CONGELADO, que es la condicion de entrada en la nomina desde la vuelta
148: TODAS las filas que este arnes usa las FABRICA el propio arnes en memoria,
y las dos salidas que escribe van a un directorio temporal que retira al acabar
(`P.16`). `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` NO SE LEE en ningun caso, ni
para elegir ni para contrastar: si lo leyera, sus cifras cambiarian con el
archivo y el verde de esta vuelta no sobreviviria a la vuelta.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL (`EJECUTOR.md` 1, caida 2 de la vuelta
89): cada caso sale de correr las funciones puras del aislador o el propio
programa, y la segunda pasada MUTA EL VALOR ESPERADO y exige que CAIGA.

QUE PRUEBA:

  1. `lista_de_puestos()` parte bien la cadena, ordena, quita repetidos y
     distingue "no se pidio" (`None`) de "se pidio vacio" (lista vacia).
  2. `--puestos` se queda SOLO con los pedidos, y en orden de puesto.
  3. `--excluir` quita los suyos, y LOS DOS SE COMPONEN entre si.
  4. LOS DOS SE COMPONEN CON LOS SELECTORES VIEJOS, y el orden es el escrito:
     primero dominio, clase, banda y rango; despues la lista.
  5. EL ROJO DEL PUESTO INEXISTENTE, que es la mitad que importa: pedir un
     puesto que el archivo no tiene NO da una seleccion mas corta, da exit 1 y
     nombra el puesto.
  6. Y UN PUESTO QUE EXISTE PERO QUE OTRO SELECTOR FILTRA NO ES ROJO, que es la
     otra mitad: si lo fuera, componer `--dominio` con `--puestos` seria
     imposible.
  7. LA GUARDA DE FUGA SIGUE CORRIENDO SOBRE LA SELECCION NUEVA. Se comprueba
     de las dos maneras: que con la lista blanca de siempre no hay fugas, y que
     si alguien ensancha la lista blanca para dejar pasar la `clase`, la guarda
     LA CAZA sobre una seleccion hecha con `--puestos`.

USO:
  python scripts/loop/vuelta178_tarea1d_mutacion_puestos.py
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import aislador_de_ciega as A   # noqa: E402

NL = chr(10)

# EL ARCHIVO FABRICADO. Cinco pares, dos dominios, clases distintas. Ninguno
# sale de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.
FILAS = [
    {"puesto_intra": 334, "nodo_a": "na_334", "nodo_b": "nb_334",
     "dominio": "ventas", "clase": "A", "razon": "razon larga del par 334",
     "banda_078_080": False},
    {"puesto_intra": 394, "nodo_a": "na_394", "nodo_b": "nb_394",
     "dominio": "ventas", "clase": "D", "razon": "razon larga del par 394",
     "banda_078_080": True},
    {"puesto_intra": 404, "nodo_a": "na_404", "nodo_b": "nb_404",
     "dominio": "compras", "clase": "A", "razon": "razon larga del par 404",
     "banda_078_080": False},
    {"puesto_intra": 878, "nodo_a": "na_878", "nodo_b": "nb_878",
     "dominio": "ventas", "clase": "A", "razon": "razon larga del par 878",
     "banda_078_080": False},
    {"puesto_intra": 1374, "nodo_a": "na_1374", "nodo_b": "nb_1374",
     "dominio": "compras", "clase": "D", "razon": "razon larga del par 1374",
     "banda_078_080": True},
]
PASOS = dict((f[k], ["paso uno de " + f[k], "paso dos de " + f[k]])
             for f in FILAS for k in ("nodo_a", "nodo_b"))


def puestos_de(sel):
    return [f["puesto_intra"] for f in sel]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    p("=" * 78)
    p("CASO POSITIVO POR MUTACION DEL CARRIL POR PUESTOS (vuelta 178, TAREA 1.d)")
    p("=" * 78)
    p("")
    p("EL ARCHIVO FABRICADO, que NO es docs/INTRA_DOMINIO_VEREDICTOS.jsonl:")
    for f in FILAS:
        p("   puesto %-5d dominio %-8s clase %s banda %s"
          % (f["puesto_intra"], f["dominio"], f["clase"], f["banda_078_080"]))
    p("   CIFRA filas fabricadas: %d" % len(FILAS))
    p("")

    casos = []

    p("1) lista_de_puestos() PARTE, ORDENA Y QUITA REPETIDOS")
    p("   '404, 334,394,334' -> %r" % (A.lista_de_puestos("404, 334,394,334"),))
    p("   None               -> %r" % (A.lista_de_puestos(None),))
    p("   ''                 -> %r" % (A.lista_de_puestos(""),))
    casos.append(("1_parte_ordena_y_deduplica",
                  A.lista_de_puestos("404, 334,394,334"), [334, 394, 404]))
    casos.append(("1_None_es_no_se_pidio", A.lista_de_puestos(None) is None, True))
    casos.append(("1_vacio_es_lista_vacia_y_no_None",
                  A.lista_de_puestos(""), []))
    p("")

    p("2) --puestos SE QUEDA SOLO CON LOS PEDIDOS")
    sel = A.elegir(FILAS, puestos=[404, 334])
    p("   puestos elegidos: %s" % puestos_de(sel))
    casos.append(("2_solo_los_pedidos_y_en_orden", puestos_de(sel), [334, 404]))
    p("")

    p("3) --excluir QUITA LOS SUYOS, Y LOS DOS SE COMPONEN")
    sel2 = A.elegir(FILAS, excluir=[878])
    sel3 = A.elegir(FILAS, puestos=[334, 394, 404, 878], excluir=[878])
    p("   solo --excluir 878          : %s" % puestos_de(sel2))
    p("   --puestos 334,394,404,878 y --excluir 878: %s" % puestos_de(sel3))
    casos.append(("3_excluir_quita_el_878", 878 in puestos_de(sel2), False))
    casos.append(("3_los_dos_se_componen", puestos_de(sel3), [334, 394, 404]))
    p("")

    p("4) SE COMPONEN CON LOS SELECTORES VIEJOS, Y EL ORDEN ES EL ESCRITO")
    sel4 = A.elegir(FILAS, dominio="ventas", puestos=[334, 404])
    p("   --dominio ventas --puestos 334,404: %s" % puestos_de(sel4))
    p("   (el 404 es de compras, asi que el dominio lo filtra ANTES: la lista se")
    p("   aplica DESPUES y no lo devuelve. Es 'de los de ventas, esos dos')")
    casos.append(("4_el_dominio_filtra_antes_que_la_lista",
                  puestos_de(sel4), [334]))
    sel5 = A.elegir(FILAS, desde=390, hasta=900, puestos=[334, 394, 878])
    p("   --desde 390 --hasta 900 --puestos 334,394,878: %s" % puestos_de(sel5))
    casos.append(("4_el_rango_tambien_filtra_antes", puestos_de(sel5), [394, 878]))
    p("")

    p("5) puestos_que_no_existen() MIRA CONTRA EL ARCHIVO ENTERO")
    p("   pedidos 334, 999, 1234 -> %r"
      % (A.puestos_que_no_existen(FILAS, [334, 999, 1234]),))
    casos.append(("5_nombra_los_que_no_existen",
                  A.puestos_que_no_existen(FILAS, [334, 999, 1234]), [999, 1234]))
    casos.append(("5_no_reclama_los_que_si_existen",
                  A.puestos_que_no_existen(FILAS, [334, 878]), []))
    p("")

    p("6) EL ROJO DE EXTREMO A EXTREMO, CORRIENDO EL PROGRAMA DE VERDAD")
    tmp = tempfile.mkdtemp(prefix="v178_puestos_")
    try:
        arch = os.path.join(tmp, "veredictos.jsonl")
        with io.open(arch, "w", encoding="utf-8", newline=NL) as fh:
            for f in FILAS:
                fh.write(json.dumps(f, ensure_ascii=False) + NL)
        grafo = os.path.join(tmp, "grafo.json")
        io.open(grafo, "w", encoding="utf-8", newline=NL).write(json.dumps(
            {"nodos": dict((k, {"pasos_accionables": v}) for k, v in PASOS.items())},
            ensure_ascii=False))

        # El aislador vivo lee sus rutas de sus constantes de modulo, asi que se
        # le apuntan a las fabricadas EN UN SUBPROCESO, con un envoltorio que
        # las sustituye antes de llamar a su `main`. El fichero vivo NO se toca.
        lanzador = os.path.join(tmp, "lanzar.py")
        io.open(lanzador, "w", encoding="utf-8", newline=NL).write(
            "import sys" + NL +
            "sys.path.insert(0, %r)" % AQUI + NL +
            "import aislador_de_ciega as A" + NL +
            "A.VEREDICTOS = %r" % arch + NL +
            "A.GRAFO = %r" % grafo + NL +
            "raise SystemExit(A.main())" + NL)

        def correr(args):
            env = dict(os.environ)
            env["PYTHONIOENCODING"] = "utf-8"
            r = subprocess.run([sys.executable, lanzador] + args,
                               cwd=RAIZ, capture_output=True, env=env)
            return r.returncode, r.stdout.decode("utf-8", errors="replace")

        ciega = os.path.join(tmp, "ciega.txt")
        destape = os.path.join(tmp, "destape.txt")
        base = ["--criterio", "los tres discutibles, sin el 878",
                "--ciega", ciega, "--destape", destape]

        c, sal = correr(base + ["--puestos", "334,394,404,878", "--excluir", "878"])
        p("   VERDE esperado: exit %d" % c)
        p("   escribe la ciega: %s" % os.path.exists(ciega))
        casos.append(("6_el_caso_bueno_exit_0", c, 0))
        casos.append(("6_el_caso_bueno_elige_TRES", "CIFRA pares elegidos: 3" in sal, True))
        casos.append(("6_el_caso_bueno_escribe_la_ciega", os.path.exists(ciega), True))
        texto_ciego = io.open(ciega, encoding="utf-8").read() if os.path.exists(ciega) else ""
        # SE MIRA `puesto_intra: 878` Y NO EL `878` A SECAS, Y SE DICE POR QUE:
        # el criterio escrito que este arnes pasa NOMBRA el 878 ("sin el 878") y
        # el criterio se copia literal a la salida ciega a proposito. Buscar el
        # numero suelto daria un falso rojo sobre el texto del propio criterio.
        casos.append(("6_la_ciega_no_lleva_la_fila_del_878",
                      "puesto_intra: 878" in texto_ciego, False))
        casos.append(("6_la_ciega_lleva_las_TRES_filas_pedidas",
                      sum(("puesto_intra: %d" % x) in texto_ciego
                          for x in (334, 394, 404)), 3))

        for r_ in (ciega, destape):
            if os.path.exists(r_):
                os.remove(r_)
        c2, sal2 = correr(base + ["--puestos", "334,9999"])
        p("   ROJO esperado, puesto 9999: exit %d" % c2)
        p("   nombra el puesto: %s" % ("NO EXISTE EN EL ARCHIVO: puesto 9999" in sal2))
        p("   no escribe nada: %s" % (not os.path.exists(ciega)))
        casos.append(("6_puesto_inexistente_exit_1", c2, 1))
        casos.append(("6_puesto_inexistente_lo_NOMBRA",
                      "NO EXISTE EN EL ARCHIVO: puesto 9999" in sal2, True))
        casos.append(("6_puesto_inexistente_NO_escribe_nada",
                      os.path.exists(ciega), False))

        c3, sal3 = correr(base + ["--excluir", "9999"])
        p("   ROJO esperado tambien en --excluir 9999: exit %d" % c3)
        casos.append(("6_excluir_inexistente_exit_1", c3, 1))

        c4, sal4 = correr(base + ["--dominio", "ventas", "--puestos", "334,404"])
        p("   NO ROJO cuando el puesto existe pero otro selector lo filtra: exit %d" % c4)
        casos.append(("6_existe_pero_filtrado_NO_es_rojo", c4, 0))
        casos.append(("6_existe_pero_filtrado_elige_UNO",
                      "CIFRA pares elegidos: 1" in sal4, True))
        p("")

        p("7) LA GUARDA DE FUGA SIGUE CORRIENDO SOBRE LA SELECCION NUEVA")
        sel_puestos = A.elegir(FILAS, puestos=[334, 394, 404])
        ciego_limpio = A.texto_ciego(sel_puestos, PASOS, "criterio de mentira")
        fugas_limpias = A.fugas(ciego_limpio, sel_puestos)
        p("   con la lista blanca de siempre, fugas: %d" % len(fugas_limpias))
        casos.append(("7_sin_ensanchar_no_hay_fugas", len(fugas_limpias), 0))
        ciego_sucio = A.texto_ciego(sel_puestos, PASOS, "criterio de mentira",
                                    campos=A.CAMPOS_CIEGOS + ("clase", "razon"))
        fugas_sucias = A.fugas(ciego_sucio, sel_puestos)
        p("   ensanchando la lista blanca a clase y razon, fugas: %d"
          % len(fugas_sucias))
        for puesto, campo in fugas_sucias:
            p("      FUGA: puesto %s, campo %s" % (puesto, campo))
        casos.append(("7_ensanchada_la_guarda_CAZA", len(fugas_sucias) > 0, True))
        casos.append(("7_caza_las_SEIS_fugas_de_los_tres_pares",
                      len(fugas_sucias), 6))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        p("   P.16: el temporal se retira. Existe todavia: %s" % os.path.exists(tmp))
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
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, list):
            mutado = esperado + [999999]
        else:
            mutado = esperado + 1
        cae = (real != mutado)
        p("   %-46s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    p("   CIFRA casos que CAEN: %d de %d" % (caen, len(casos)))
    p("")

    if fallos or caen != len(casos):
        p("ROJO DE LA MUTACION: el carril por puestos no se comporta.")
        p("FIN")
        return 1
    p("VERDE DE LA MUTACION: %d casos, los %d pasan y los %d CAEN al mutarles el "
      "valor esperado. `--puestos` y `--excluir` eligen, se componen entre si y "
      "con los selectores viejos en el orden escrito, PIDEN UN PUESTO QUE NO "
      "EXISTE Y SALEN EN ROJO NOMBRANDOLO SIN ESCRIBIR NADA, no confunden eso con "
      "un puesto filtrado por otro selector, y LA GUARDA DE FUGA SIGUE MORDIENDO "
      "sobre la seleccion nueva."
      % (len(casos), len(casos), len(casos)))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
