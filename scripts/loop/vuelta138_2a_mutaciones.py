# -*- coding: utf-8 -*-
"""vuelta138_2a_mutaciones.py . LAS GUARDAS (ii), (iii), (iv) Y (v) DE LA
OPERACION 2.a DE LA VUELTA 138.

QUE PRUEBA, con las palabras del encargo:
  (ii) MUTACION 1: "dos absorbidos con marcas DISTINTAS para el MISMO numero de
       paso tienen que salir DISTINTAS en el plan. Contra el codigo viejo esta
       mutacion no puede pasar; contra el nuevo, si."
  (iii) MUTACION 2: "una marca que falte para un par (absorbido, paso) cae ROJO
       NOMBRANDO EL PAR, no solo el numero."
  (iv) "EL FALLO VIEJO QUEDA EXHIBIBLE": --reparto-viejo reparte el dict plano a
       todos los absorbidos y ensena las dos marcas iguales.
  (v) "cero escritura si hay fallos".

SOBRE QUE SUJETO, Y POR QUE UNO SINTETICO Y CONGELADO. La tentacion era usar
OP-M-03-III, que es una ficha REAL con dos absorbidos. NO SE USA, y el motivo es
la leccion de la guarda envejecida de la vuelta 137 (banco 9.10): esta misma
vuelta funde OP-M-03-III, y en cuanto la funda sus dos absorbidos quedan
DEPRECADOS y el generador cae en ROJO por otra razon, con lo que estas cuatro
guardas dejarian de medir lo que dicen medir y nadie se enteraria. El sujeto es,
por tanto, un banco de pruebas propio y congelado: tres nodos inventados
(V138_SUP_FIXTURE y sus dos absorbidos) y una ficha inventada
(OP-V138-FIXTURE), escritos en un directorio temporal, sin tocar ni un nodo ni
una linea de docs/plan/OPERACIONES.jsonl. Ningun id del banco existe en el
catalogo, y eso se comprueba aqui antes de empezar.

QUE SE MONKEYPATCHEA Y QUE NO: se importa el generador de verdad y se le cambian
las TRES rutas de lectura y escritura (NODOS, OPERACIONES, SALIDA) para que lea
el banco. NO se toca ni una linea de su logica: la aritmetica, las marcas, las
guardas y el reparto son los del fichero que se esta probando. Si alguien rompe
reparto_por_par, estas guardas caen.

LA PRUEBA DE MUTACION DE CADA CASO va sobre una variable QUE EL CODIGO COMPUTA
(EJECUTOR regla 1), nunca sobre un literal:
  - el caso (ii) lee las DOS marcas DEL PLAN ESCRITO y las compara entre si; su
    mutacion es correr EL MISMO sujeto por el reparto VIEJO, donde las dos salen
    IGUALES y el caso CAE;
  - el caso (iii) lee EL TEXTO DE LA SALIDA del generador y busca en el el
    nombre del absorbido; su mutacion es devolver la marca que falta, con lo que
    el generador da VERDE y el caso CAE;
  - el caso (iv) lee el CONTADOR DE COLISIONES que exhibir_reparto computa de las
    marcas; su mutacion es correr el mismo sujeto SIN --reparto-viejo, donde el
    generador se niega y no hay colision que contar.

USO:
  python scripts/loop/vuelta138_2a_mutaciones.py
"""
import importlib
import io
import json
import os
import shutil
import sys
import tempfile
import contextlib

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP_SCRIPTS = os.path.join(RAIZ, "scripts", "loop")

SUP = "v138_sup_fixture"
AB1 = "v138_ab_uno_fixture"
AB2 = "v138_ab_dos_fixture"
ID_OP = "OP-V138-FIXTURE"


class SalidaCapturable(io.StringIO):
    """io.StringIO no trae reconfigure(), y el generador la llama."""

    def reconfigure(self, **kw):
        return None


def nodo(nid, pasos, condiciones):
    return {
        "node_id": nid,
        "titulo_concepto": "FIXTURE " + nid,
        "dominio": "core",
        "pasos_accionables": pasos,
        "condiciones_activacion": condiciones,
        "nodos_siguientes": [],
        "nodos_previos": [],
    }


def montar_banco(tmp):
    """Escribe los tres nodos y la ficha del banco. Devuelve (nodos_dir,
    operaciones, salida_dir)."""
    nodos_dir = os.path.join(tmp, "nodos")
    salida_dir = os.path.join(tmp, "salida")
    os.makedirs(nodos_dir)
    os.makedirs(salida_dir)

    cuerpos = {
        SUP: nodo(SUP,
                  ["Paso uno del superviviente del banco",
                   "Paso dos del superviviente del banco",
                   "Paso tres del superviviente del banco"],
                  ["Cuando se da la primera condicion del superviviente",
                   "Cuando se da la segunda condicion del superviviente"]),
        AB1: nodo(AB1,
                  ["Paso uno del absorbido uno",
                   "Paso dos del absorbido uno"],
                  ["Cuando se da la condicion del absorbido uno"]),
        AB2: nodo(AB2,
                  ["Paso uno del absorbido dos",
                   "Paso dos del absorbido dos"],
                  ["Cuando se da la condicion del absorbido dos"]),
    }
    for nid, cuerpo in cuerpos.items():
        io.open(os.path.join(nodos_dir, nid + ".json"), "w", encoding="utf-8",
                newline="\n").write(json.dumps(cuerpo, ensure_ascii=False, indent=1))

    ficha = {
        "id_op": ID_OP,
        "tipo": "FUSION DE MESA DE BANCO DE PRUEBAS",
        "estado": "LISTA",
        "fecha_corte": "2026-09-02",
        "nodos": [SUP, AB1, AB2],
        "superviviente": SUP,
        "eliminar": [AB1, AB2],
        "adjudicacion": "BANCO DE PRUEBAS DE LA VUELTA 138, no es una operacion de la campana",
        "preservar": [],
        "verificacion": "ninguna, es un banco",
        "evidencia": "ninguna, es un banco",
        "nota": "FICHA SINTETICA. No vive en docs/plan/OPERACIONES.jsonl.",
        "depende_de": [],
        "bloquea_a": [],
    }
    operaciones = os.path.join(tmp, "OPERACIONES_FIXTURE.jsonl")
    io.open(operaciones, "w", encoding="utf-8", newline="\n").write(
        json.dumps(ficha, ensure_ascii=False) + "\n")
    return nodos_dir, operaciones, salida_dir


CABECERA_SPEC = {
    "titulo": "BANCO DE PRUEBAS DE LA VUELTA 138, OPERACION 2.a",
    "superviviente": SUP,
    "absorbidos": [AB1, AB2],
    "motivo": "BANCO DE PRUEBAS. No adjudica nada y no describe ninguna mesa real.",
    "nota": "BANCO DE PRUEBAS DEL REPARTO POR PAR.",
    "perdidas": [],
    "simulacion_de_hoy": "ninguna, es un banco",
}


def escribir_contenido(tmp, modulo, pasos, condiciones):
    spec = dict(CABECERA_SPEC)
    spec["pasos"] = pasos
    spec["condiciones"] = condiciones
    ruta = os.path.join(tmp, modulo + ".py")
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(
        "# -*- coding: utf-8 -*-\n"
        "# CONTENIDO SINTETICO del banco de pruebas de la vuelta 138. Lo escribe\n"
        "# scripts/loop/vuelta138_2a_mutaciones.py en un directorio temporal y se\n"
        "# borra al terminar (P.16, quien fabrica limpia).\n"
        "FUSION = " + repr(spec) + "\n")
    # SIN ESTO EL CASO ES UN FLAKE, y lo fue: la segunda corrida de este mismo
    # fichero cayo con ModuleNotFoundError: _banco_v138_falta. El buscador de
    # modulos de Python cachea el listado de cada directorio de sys.path por la
    # mtime del directorio, y esa mtime tiene grano suficiente para que un
    # modulo escrito DESPUES del primer __import__ sobre el mismo directorio
    # quede invisible. invalidate_caches() tira ese cache. Se arregla en vez de
    # reintentar: una guarda que a veces no encuentra su propio sujeto no es una
    # guarda, y el fallo es intermitente, que es la peor especie.
    importlib.invalidate_caches()
    return ruta


def correr(gen, tmp, nodos_dir, operaciones, salida_dir, modulo, extra=()):
    """Corre el main() del generador de verdad contra el banco. Devuelve
    (codigo_de_salida, texto_de_la_salida, ruta_del_plan_o_None)."""
    gen.NODOS = nodos_dir
    gen.OPERACIONES = operaciones
    gen.SALIDA = salida_dir
    argv = [gen.__file__, "--vuelta", "138", "--id-op", ID_OP,
            "--contenido", modulo, "--prefijo", "BANCO_V138_"] + list(extra)
    buf = SalidaCapturable()
    viejo_argv = sys.argv
    sys.argv = argv
    try:
        with contextlib.redirect_stdout(buf):
            codigo = gen.main()
    finally:
        sys.argv = viejo_argv
    destino = os.path.join(salida_dir, "BANCO_V138_%s.json" % ID_OP.replace("-", ""))
    plan = destino if os.path.exists(destino) else None
    return codigo, buf.getvalue(), plan


def marca_del_plan(ruta, absorbido, numero):
    d = json.load(io.open(ruta, encoding="utf-8"))
    return d["actos"][0]["pasos"].get(absorbido, {}).get(numero)


def limpiar(salida_dir):
    for n in os.listdir(salida_dir):
        os.remove(os.path.join(salida_dir, n))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.path.insert(0, LOOP_SCRIPTS)
    import generar_plan_de_fusion_de_mesa as gen

    print("=" * 78)
    print("GUARDAS (ii), (iii), (iv) Y (v) DE LA OPERACION 2.a, VUELTA 138")
    print("=" * 78)

    # NINGUN ID DEL BANCO EXISTE EN EL CATALOGO: se mide antes de empezar.
    reales = [x for x in (SUP, AB1, AB2)
              if os.path.exists(os.path.join(RAIZ, "dataset", "nodos", x + ".json"))]
    print("  ids del banco que existen en dataset/nodos: %s"
          % (", ".join(reales) if reales else "NINGUNO, como debe ser"))
    if reales:
        print("ROJO: el banco pisa nodos reales. PARADA.")
        return 1

    tmp = tempfile.mkdtemp(prefix="banco_v138_2a_")
    sys.path.insert(0, tmp)
    veredictos = []
    try:
        nodos_dir, operaciones, salida_dir = montar_banco(tmp)

        # ------------------------------------------------------------------
        # (ii) MUTACION 1: marcas DISTINTAS para el MISMO numero de paso.
        # ------------------------------------------------------------------
        print("")
        print("-" * 78)
        print("(ii) MUTACION 1: dos absorbidos, marcas DISTINTAS para el paso 1.")
        pasos_par = {AB1: {"1": ["APPEND"], "2": ["CUBIERTO", 1]},
                     AB2: {"1": ["CUBIERTO", 2], "2": ["APPEND"]}}
        cond_par = {AB1: {"1": ["APPEND"]}, AB2: {"1": ["CUBIERTO", 1]}}
        escribir_contenido(tmp, "_banco_v138_par", pasos_par, cond_par)
        cod, txt, plan = correr(gen, tmp, nodos_dir, operaciones, salida_dir, "_banco_v138_par")
        print("  exit del generador: %d | plan escrito: %s" % (cod, bool(plan)))
        for l in txt.splitlines():
            if "FORMATO DEL REPARTO" in l:
                print(" %s" % l)
        if plan is None:
            print("  ROJO: no se escribio el plan. Salida:")
            for l in txt.splitlines()[-15:]:
                print("     %s" % l)
            veredictos.append(("(ii) marcas distintas", "ROJO, sin plan"))
        else:
            m1 = marca_del_plan(plan, AB1, "1")
            m2 = marca_del_plan(plan, AB2, "1")
            print("  marca del par (%s, 1) en el plan: %r" % (AB1, m1))
            print("  marca del par (%s, 1) en el plan: %r" % (AB2, m2))
            distintas = (m1 != m2)
            print("  distintas: %s" % distintas)
            veredictos.append(("(ii) marcas distintas",
                               "VERDE" if distintas else "ROJO, salieron iguales"))
        limpiar(salida_dir)

        # LA MUTACION DEL CASO (ii): el MISMO sujeto por el reparto VIEJO.
        print("")
        print("  MUTACION DEL CASO (ii): el mismo sujeto por el REPARTO VIEJO.")
        pasos_plano = {"1": ["APPEND"], "2": ["CUBIERTO", 1]}
        cond_plano = {"1": ["APPEND"]}
        escribir_contenido(tmp, "_banco_v138_plano", pasos_plano, cond_plano)
        cod_v, txt_v, _ = correr(gen, tmp, nodos_dir, operaciones, salida_dir,
                                 "_banco_v138_plano", extra=["--reparto-viejo"])
        colisiones = None
        for l in txt_v.splitlines():
            if l.strip().startswith("COLISIONES DEL REPARTO VIEJO:"):
                colisiones = int(l.strip().split(":")[1])
        print("  colisiones contadas por el generador: %s" % colisiones)
        cae = bool(colisiones)
        print("  el caso (ii) CAE contra el reparto viejo: %s" % cae)
        veredictos.append(("(ii) su mutacion, reparto viejo",
                           "VERDE, cae" if cae else "ROJO, no cae"))
        limpiar(salida_dir)

        # ------------------------------------------------------------------
        # (iii) MUTACION 2: falta la marca de un par (absorbido, paso).
        # ------------------------------------------------------------------
        print("")
        print("-" * 78)
        print("(iii) MUTACION 2: falta la marca del par (%s, 1)." % AB2)
        pasos_falta = {AB1: {"1": ["APPEND"], "2": ["CUBIERTO", 1]},
                       AB2: {"2": ["APPEND"]}}
        escribir_contenido(tmp, "_banco_v138_falta", pasos_falta, cond_par)
        cod_f, txt_f, plan_f = correr(gen, tmp, nodos_dir, operaciones, salida_dir,
                                      "_banco_v138_falta")
        lineas_del_par = [l.strip() for l in txt_f.splitlines() if "FALTA EL PAR" in l]
        print("  exit del generador: %d" % cod_f)
        for l in lineas_del_par:
            print("     %s" % l)
        nombra_el_par = any((AB2 in l) and ("(%s, 1)" % AB2 in l) for l in lineas_del_par)
        print("  el ROJO nombra el par (%s, 1): %s" % (AB2, nombra_el_par))
        rojo = (cod_f != 0)
        veredictos.append(("(iii) ROJO nombrando el par",
                           "VERDE" if (rojo and nombra_el_par) else
                           "ROJO, exit %d, nombra %s" % (cod_f, nombra_el_par)))

        # ------------------------------------------------------------------
        # (v) CERO ESCRITURA SI HAY FALLOS.
        # ------------------------------------------------------------------
        quedan = sorted(os.listdir(salida_dir))
        print("  (v) ficheros escritos en la salida tras el ROJO: %s"
              % (", ".join(quedan) if quedan else "NINGUNO"))
        veredictos.append(("(v) cero escritura si hay fallos",
                           "VERDE" if not quedan else "ROJO, escribio %s" % quedan))

        # LA MUTACION DEL CASO (iii): se devuelve la marca que faltaba.
        print("")
        print("  MUTACION DEL CASO (iii): se devuelve la marca del par (%s, 1)." % AB2)
        cod_d, txt_d, plan_d = correr(gen, tmp, nodos_dir, operaciones, salida_dir,
                                      "_banco_v138_par")
        hay_falta = any("FALTA EL PAR" in l for l in txt_d.splitlines())
        print("  exit del generador: %d | queda algun FALTA EL PAR: %s" % (cod_d, hay_falta))
        cae3 = (cod_d == 0 and not hay_falta)
        print("  el caso (iii) CAE al devolver la marca: %s" % cae3)
        veredictos.append(("(iii) su mutacion, marca devuelta",
                           "VERDE, cae" if cae3 else "ROJO, no cae"))
        limpiar(salida_dir)

        # ------------------------------------------------------------------
        # (iv) EL FALLO VIEJO, EXHIBIDO.
        # ------------------------------------------------------------------
        print("")
        print("-" * 78)
        print("(iv) EL FALLO VIEJO, EXHIBIDO con --reparto-viejo:")
        for l in txt_v.splitlines():
            if "COLISION" in l or "EXHIBICION" in l or l.strip().startswith("paso ") \
                    or l.strip().startswith("condicion "):
                print("  %s" % l.rstrip())
        veredictos.append(("(iv) el fallo viejo exhibible",
                           "VERDE, %d colision(es)" % colisiones if colisiones
                           else "ROJO, cero colisiones"))

        # LA MUTACION DEL CASO (iv): el MISMO spec plano SIN la bandera.
        print("")
        print("  MUTACION DEL CASO (iv): el mismo spec plano SIN --reparto-viejo.")
        cod_n, txt_n, plan_n = correr(gen, tmp, nodos_dir, operaciones, salida_dir,
                                      "_banco_v138_plano")
        lineas_rojo = [l.strip() for l in txt_n.splitlines() if "FORMATO VIEJO" in l]
        print("  exit del generador: %d | plan escrito: %s" % (cod_n, bool(plan_n)))
        for l in lineas_rojo:
            print("     %s" % l[:200])
        nombra_los_dos = any((AB1 in l and AB2 in l) for l in lineas_rojo)
        print("  el ROJO nombra los DOS absorbidos: %s" % nombra_los_dos)
        veredictos.append(("(iv) su mutacion, sin la bandera",
                           "VERDE, cae" if (cod_n != 0 and nombra_los_dos and not plan_n)
                           else "ROJO, no cae"))
        limpiar(salida_dir)
    finally:
        # P.16, QUIEN FABRICA LIMPIA.
        shutil.rmtree(tmp, ignore_errors=True)
        print("")
        print("  P.16: el banco temporal se retira. Existe todavia: %s" % os.path.exists(tmp))

    print("")
    print("=" * 78)
    for k, v in veredictos:
        print("  %-34s %s" % (k, v))
    malos = [k for k, v in veredictos if v.startswith("ROJO")]
    if malos:
        print("ROJO: %d de %d guardas no pasan: %s" % (len(malos), len(veredictos),
                                                       ", ".join(malos)))
        print("FIN")
        return 1
    print("VERDE: las %d guardas pasan." % len(veredictos))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
