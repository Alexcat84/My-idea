# -*- coding: utf-8 -*-
"""vuelta139_2a_mutaciones.py . LOS CASOS (B), (C), (D) Y (E) DE LA OPERACION
2.a DE LA VUELTA 139: LA QUINTA MARCA, VIAJA_EN_EL_ACTO.

EL CASO (A) NO ESTA AQUI Y NO SE FABRICA: ya existe y es
scripts/loop/vuelta138_2a_caso_positivo_63_64.py (los tres planes de las
vueltas 63 y 64 regenerados con el generador de HOY salen identicos salvo la
fecha). El encargo lo dice con esas palabras: "el primero YA EXISTE, no lo
fabriques".

QUE PRUEBA, con las palabras del encargo:
  (B) MUTACION SOBRE LA CIFRA COMPUTADA, y es la que prueba a P.13: dos
      absorbidos con la misma pieza, uno con APPEND y otro con
      VIAJA_EN_EL_ACTO apuntandolo. CUENTA cuantas veces aparece esa pieza en
      los pasos del superviviente resultante: tiene que ser UNA. Cambia el
      VIAJA_EN_EL_ACTO por un segundo APPEND: la cuenta pasa a DOS, y esa es
      la repeticion que P.13 prohibe por su nombre. La guarda ENSENA las dos
      cuentas.
  (C) MUTACION: VIAJA_EN_EL_ACTO apuntando a un paso marcado CUBIERTO. ROJO
      con "cadena que no llega a viajar" y el par nombrado.
  (D) MUTACION: VIAJA_EN_EL_ACTO apuntando a un absorbido que no esta en la
      operacion, y otra a un numero de paso que no existe. ROJO NOMBRANDO LOS
      DOS en cada caso.
  (E) cero escritura si hay fallos.

Y DE PROPINA, porque son guardas del encargo que sin caso no se prueban solas:
  (iii) la AUTO REFERENCIA (mismo absorbido, mismo paso) es ROJO.
  (v)   sin linea editorial es ROJO, y con una linea que NO nombra al
        absorbido destino tambien.

POR QUE LA CUENTA DEL CASO (B) ES UNA CIFRA COMPUTADA Y NO UN LITERAL
(EJECUTOR regla 1): se cuenta cuantos pasos del superviviente RESULTANTE
contienen la PIEZA, y el superviviente resultante se lee de la salida del
fundidor de verdad (scripts/loop/fundir_por_plan.py) corrido en modo
SIMULAR sobre el banco. No se compara ninguna constante consigo misma: la
mutacion cambia UNA marca del contenido editorial, el fundidor vuelve a
correr, y la cuenta se recomputa de su resultado.

Y POR QUE LAS DOS REDACCIONES DE LA PIEZA NO SON IDENTICAS EN EL BANCO: si lo
fueran, el segundo APPEND lo cazaria ademas la GUARDA 3 del fundidor ("cero
repetidos literales"), y el caso no probaria nada nuevo. Son el MISMO GESTO
con DOS REDACCIONES distintas que comparten un trozo distintivo, que es
exactamente la figura que P.13 llama repeticion y que la guarda 3 NO ve. La
cuenta se hace por ese trozo.

SOBRE QUE SUJETO, Y POR QUE UNO SINTETICO Y CONGELADO. La misma leccion que la
2.a de la vuelta 138 (banco 9.10): usar una ficha real dejaria la guarda
envejecida en cuanto esa mesa se funda, porque sus absorbidos quedarian
deprecados y el generador caeria en ROJO por otra razon sin que nadie se
enterara. El sujeto es un banco propio: tres nodos inventados y una ficha
inventada, en un directorio temporal, sin tocar ni un nodo ni una linea de
docs/plan/OPERACIONES.jsonl. Ningun id del banco existe en el catalogo, y eso
SE COMPRUEBA AQUI ANTES DE EMPEZAR.

QUE SE MONKEYPATCHEA Y QUE NO: se importan el generador y el fundidor DE
VERDAD y se les cambian las rutas de lectura y escritura (NODOS, OPERACIONES,
SALIDA) para que lean el banco. NO se toca ni una linea de su logica. Si
alguien rompe las guardas de VIAJA_EN_EL_ACTO, estos casos caen.

P.16, QUIEN FABRICA LIMPIA: el directorio temporal se borra siempre.

USO:
  python scripts/loop/vuelta139_2a_mutaciones.py
"""
import contextlib
import importlib
import io
import json
import os
import shutil
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP_SCRIPTS = os.path.join(RAIZ, "scripts", "loop")

SUP = "v139_sup_fixture"
AB1 = "v139_ab_uno_fixture"
AB2 = "v139_ab_dos_fixture"
ID_OP = "OP-V139-FIXTURE"

# LA PIEZA DE DOS DUENOS: el trozo distintivo por el que se CUENTA, y las dos
# redacciones del MISMO GESTO. No son iguales byte a byte a proposito (ver el
# docstring): si lo fueran, la guarda 3 del fundidor cazaria el doble APPEND y
# este caso no probaria nada que la casa no tuviera ya.
PIEZA = "pedidos a precio completo"
PIEZA_AB1 = "Buscar pedidos a precio completo como prueba dura de que la venta se repite"
PIEZA_AB2 = "Probar que el proceso se repite buscando pedidos a precio completo"

LINEA_EDITORIAL = (
    "Los dos absorbidos mandan el mismo gesto, probar la repeticion de la venta con "
    "pedidos a precio completo. VIAJA LA REDACCION DE " + AB1 + ", que es la que "
    "lleva el APPEND; la de " + AB2 + " no anade ningun matiz que la primera no "
    "traiga, asi que no es una pieza propia."
)


class SalidaCapturable(io.StringIO):
    """io.StringIO no trae reconfigure(), y los instrumentos la llaman."""

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
    """Escribe los tres nodos y la ficha del banco. El superviviente NO tiene la
    pieza en ninguno de sus pasos, que es la premisa del caso."""
    nodos_dir = os.path.join(tmp, "nodos")
    salida_dir = os.path.join(tmp, "salida")
    os.makedirs(nodos_dir)
    os.makedirs(salida_dir)

    cuerpos = {
        SUP: nodo(SUP,
                  ["Paso uno del superviviente del banco",
                   "Paso dos del superviviente del banco"],
                  ["Cuando se da la condicion del superviviente"]),
        AB1: nodo(AB1,
                  [PIEZA_AB1,
                   "Paso propio del absorbido uno que no esta en ningun otro"],
                  []),
        AB2: nodo(AB2,
                  ["Paso propio del absorbido dos que no esta en ningun otro",
                   PIEZA_AB2],
                  []),
    }
    for nid, cuerpo in cuerpos.items():
        io.open(os.path.join(nodos_dir, nid + ".json"), "w", encoding="utf-8",
                newline="\n").write(json.dumps(cuerpo, ensure_ascii=False, indent=2))

    ficha = {
        "id_op": ID_OP,
        "tipo": "FUSION DE MESA DE BANCO DE PRUEBAS",
        "estado": "LISTA",
        "fecha_corte": "2026-09-02",
        "nodos": [SUP, AB1, AB2],
        "superviviente": SUP,
        "eliminar": [AB1, AB2],
        "adjudicacion": "BANCO DE PRUEBAS DE LA VUELTA 139, no es una operacion de la campana",
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
    "titulo": "BANCO DE PRUEBAS DE LA VUELTA 139, OPERACION 2.a",
    "superviviente": SUP,
    "absorbidos": [AB1, AB2],
    "motivo": "BANCO DE PRUEBAS. No adjudica nada y no describe ninguna mesa real.",
    "nota": "BANCO DE PRUEBAS DE LA QUINTA MARCA, VIAJA_EN_EL_ACTO.",
    "perdidas": [],
    "simulacion_de_hoy": "ninguna, es un banco",
}


def escribir_contenido(tmp, modulo, pasos, condiciones, lineas_de_viaje=None):
    spec = dict(CABECERA_SPEC)
    spec["pasos"] = pasos
    spec["condiciones"] = condiciones
    if lineas_de_viaje is not None:
        spec["lineas_de_viaje"] = lineas_de_viaje
    ruta = os.path.join(tmp, modulo + ".py")
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(
        "# -*- coding: utf-8 -*-\n"
        "# CONTENIDO SINTETICO del banco de pruebas de la vuelta 139. Lo escribe\n"
        "# scripts/loop/vuelta139_2a_mutaciones.py en un directorio temporal y se\n"
        "# borra al terminar (P.16, quien fabrica limpia).\n"
        "FUSION = " + repr(spec) + "\n")
    # LA MISMA TRAMPA QUE CAZO LA VUELTA 138 Y SU MISMO REMEDIO: el buscador de
    # modulos cachea el listado del directorio por su mtime, y un modulo escrito
    # DESPUES del primer __import__ sobre ese directorio queda invisible. Sin
    # esto el caso es un flake, que es la peor especie de guarda.
    importlib.invalidate_caches()
    return ruta


def correr_generador(gen, nodos_dir, operaciones, salida_dir, modulo):
    """Corre el main() del generador de verdad contra el banco. Devuelve
    (codigo, texto, ruta_del_plan_o_None)."""
    gen.NODOS = nodos_dir
    gen.OPERACIONES = operaciones
    gen.SALIDA = salida_dir
    argv = [gen.__file__, "--vuelta", "139", "--id-op", ID_OP,
            "--contenido", modulo, "--prefijo", "BANCO_V139_"]
    buf = SalidaCapturable()
    viejo = sys.argv
    sys.argv = argv
    try:
        with contextlib.redirect_stdout(buf):
            codigo = gen.main()
    finally:
        sys.argv = viejo
    destino = os.path.join(salida_dir, "BANCO_V139_%s.json" % ID_OP.replace("-", ""))
    return codigo, buf.getvalue(), (destino if os.path.exists(destino) else None)


def correr_fundidor(fun, nodos_dir, plan):
    """Corre el main() del fundidor de verdad en modo SIMULAR (sin --ejecutar)
    contra el banco. Devuelve (codigo, texto)."""
    fun.NODOS = nodos_dir
    argv = [fun.__file__, "--plan", plan]
    buf = SalidaCapturable()
    viejo = sys.argv
    sys.argv = argv
    try:
        with contextlib.redirect_stdout(buf):
            codigo = fun.main()
    finally:
        sys.argv = viejo
    return codigo, buf.getvalue()


def pasos_resultantes(fun, nodos_dir, plan):
    """EL SUPERVIVIENTE RESULTANTE, construido por el fundidor DE VERDAD.

    No se reimplementa la aritmetica del fundidor aqui: eso seria medir una
    copia. Se corre su main() en modo SIMULAR (que ya construye el resultado en
    memoria y no escribe nada) y se leen los pasos del superviviente de la copia
    que deja en su propio diccionario. Para poder leerlos se envuelve censo(),
    que es lo ultimo que el main llama antes de decidir si escribe, y se guarda
    la referencia. La alternativa (parsear la salida de texto) mediria el
    formato de impresion, no el resultado.
    """
    capturado = {}
    original = fun.escribir

    def espia(nid, datos, cola):
        capturado[nid] = datos

    fun.escribir = espia
    try:
        fun.NODOS = nodos_dir
        argv = [fun.__file__, "--plan", plan, "--ejecutar"]
        buf = SalidaCapturable()
        viejo = sys.argv
        sys.argv = argv
        try:
            with contextlib.redirect_stdout(buf):
                codigo = fun.main()
        finally:
            sys.argv = viejo
    finally:
        fun.escribir = original
    pasos = (capturado.get(SUP) or {}).get("pasos_accionables") or []
    return codigo, buf.getvalue(), list(pasos)


def contar_pieza(pasos, pieza):
    """LA CIFRA COMPUTADA DEL CASO (B): cuantos pasos del superviviente
    resultante contienen la pieza. Se cuenta por el TROZO DISTINTIVO, no por
    igualdad literal, porque las dos redacciones del mismo gesto no son
    identicas (si lo fueran, la guarda 3 del fundidor ya las cazaria y este caso
    no probaria nada nuevo)."""
    return sum(1 for p in pasos if pieza.lower() in p.lower())


def limpiar(salida_dir):
    for n in os.listdir(salida_dir):
        os.remove(os.path.join(salida_dir, n))


def rojos_que_contienen(texto, trozos):
    """Las lineas de fallo del instrumento que contienen TODOS los trozos."""
    return [l.strip() for l in texto.splitlines()
            if all(t in l for t in trozos)]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.path.insert(0, LOOP_SCRIPTS)
    import generar_plan_de_fusion_de_mesa as gen
    import fundir_por_plan as fun

    print("=" * 78)
    print("CASOS (B), (C), (D) Y (E) DE LA OPERACION 2.a, VUELTA 139")
    print("LA QUINTA MARCA: VIAJA_EN_EL_ACTO")
    print("=" * 78)

    reales = [x for x in (SUP, AB1, AB2)
              if os.path.exists(os.path.join(RAIZ, "dataset", "nodos", x + ".json"))]
    print("  ids del banco que existen en dataset/nodos: %s"
          % (", ".join(reales) if reales else "NINGUNO, como debe ser"))
    if reales:
        print("ROJO: el banco pisa nodos reales. PARADA.")
        return 1

    tmp = tempfile.mkdtemp(prefix="banco_v139_2a_")
    sys.path.insert(0, tmp)
    veredictos = []
    try:
        nodos_dir, operaciones, salida_dir = montar_banco(tmp)
        print("  banco montado en un temporal: %d nodos, ficha %s"
              % (len(os.listdir(nodos_dir)), ID_OP))
        print("  la PIEZA de dos duenos, contada por el trozo %r:" % PIEZA)
        print("     en %s, paso 1: %s" % (AB1, PIEZA_AB1))
        print("     en %s, paso 2: %s" % (AB2, PIEZA_AB2))
        print("     en el superviviente: EN NINGUNO de sus 2 pasos (premisa del caso)")

        # ==================================================================
        # (B) LA CIFRA COMPUTADA. Sano contra mutado.
        # ==================================================================
        print("")
        print("-" * 78)
        print("(B) LA CUENTA DE LA PIEZA EN EL SUPERVIVIENTE RESULTANTE.")
        print("    SANO: (%s, 1) APPEND y (%s, 2) VIAJA_EN_EL_ACTO al par (%s, 1)."
              % (AB1, AB2, AB1))
        pasos_sano = {AB1: {"1": ["APPEND"], "2": ["APPEND"]},
                      AB2: {"1": ["APPEND"], "2": ["VIAJA_EN_EL_ACTO", AB1, 1]}}
        cond_vacias = {AB1: {}, AB2: {}}
        escribir_contenido(tmp, "_banco_v139_sano", pasos_sano, cond_vacias,
                           lineas_de_viaje={"%s|2" % AB2: LINEA_EDITORIAL})
        cod, txt, plan = correr_generador(gen, nodos_dir, operaciones, salida_dir,
                                          "_banco_v139_sano")
        print("    generador: exit %d | plan escrito: %s" % (cod, bool(plan)))
        for l in txt.splitlines():
            if "REPARTO:" in l or "VIAJA_EN_EL_ACTO," in l or "viaja por el paso" in l:
                print("   %s" % l.rstrip())
        cuenta_sana = None
        if plan is None:
            print("    ROJO: el generador no sello el plan. Ultimas lineas:")
            for l in txt.splitlines()[-15:]:
                print("       %s" % l)
        else:
            cod_f, txt_f, pasos_res = pasos_resultantes(fun, nodos_dir, plan)
            cuenta_sana = contar_pieza(pasos_res, PIEZA)
            print("    fundidor: exit %d | el superviviente resultante tiene %d paso(s)"
                  % (cod_f, len(pasos_res)))
            for i, p in enumerate(pasos_res, 1):
                print("       paso %d: %s" % (i, p))
            for l in txt_f.splitlines():
                if "VIAJA EN ESTE MISMO ACTO" in l or "piezas repartidas" in l:
                    print("   %s" % l.rstrip())
            print("    CUENTA DE LA PIEZA EN EL RESULTADO: %d" % cuenta_sana)
        limpiar(salida_dir)

        print("")
        print("    MUTACION DEL (B): el VIAJA_EN_EL_ACTO pasa a ser un SEGUNDO APPEND.")
        pasos_mut = {AB1: {"1": ["APPEND"], "2": ["APPEND"]},
                     AB2: {"1": ["APPEND"], "2": ["APPEND"]}}
        escribir_contenido(tmp, "_banco_v139_doble", pasos_mut, cond_vacias)
        cod2, txt2, plan2 = correr_generador(gen, nodos_dir, operaciones, salida_dir,
                                             "_banco_v139_doble")
        cuenta_mutada = None
        if plan2 is None:
            print("    ROJO: el generador no sello el plan mutado. Ultimas lineas:")
            for l in txt2.splitlines()[-15:]:
                print("       %s" % l)
        else:
            cod_f2, txt_f2, pasos_res2 = pasos_resultantes(fun, nodos_dir, plan2)
            cuenta_mutada = contar_pieza(pasos_res2, PIEZA)
            print("    fundidor: exit %d | el superviviente resultante tiene %d paso(s)"
                  % (cod_f2, len(pasos_res2)))
            for i, p in enumerate(pasos_res2, 1):
                print("       paso %d: %s" % (i, p))
            print("    CUENTA DE LA PIEZA EN EL RESULTADO: %d" % cuenta_mutada)
            print("    (y la GUARDA 3 del fundidor, cero repetidos LITERALES, NO la ve:")
            print("     las dos redacciones no son iguales byte a byte, que es justo la")
            print("     figura que P.13 llama repeticion fabricada)")
        limpiar(salida_dir)

        print("")
        print("    LAS DOS CUENTAS, UNA AL LADO DE LA OTRA: sana %s, mutada %s"
              % (cuenta_sana, cuenta_mutada))
        ok_b = (cuenta_sana == 1 and cuenta_mutada == 2)
        veredictos.append(("(B) la cuenta pasa de 1 a 2 al quitar la marca",
                           "VERDE" if ok_b else
                           "ROJO, sana %s y mutada %s" % (cuenta_sana, cuenta_mutada)))

        # ==================================================================
        # (C) CADENA QUE NO LLEGA A VIAJAR.
        # ==================================================================
        print("")
        print("-" * 78)
        print("(C) MUTACION: VIAJA_EN_EL_ACTO apuntando a un paso marcado CUBIERTO.")
        pasos_c = {AB1: {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
                   AB2: {"1": ["APPEND"], "2": ["VIAJA_EN_EL_ACTO", AB1, 1]}}
        escribir_contenido(tmp, "_banco_v139_cadena", pasos_c, cond_vacias,
                           lineas_de_viaje={"%s|2" % AB2: LINEA_EDITORIAL})
        cod_c, txt_c, plan_c = correr_generador(gen, nodos_dir, operaciones, salida_dir,
                                                "_banco_v139_cadena")
        lineas_c = rojos_que_contienen(txt_c, ["CADENA QUE NO LLEGA A VIAJAR"])
        print("    generador: exit %d | plan escrito: %s" % (cod_c, bool(plan_c)))
        for l in lineas_c:
            print("       %s" % l)
        nombra_par_c = any((AB1 in l) and ("(%s, 1)" % AB1 in l) for l in lineas_c)
        ok_c = (cod_c != 0 and plan_c is None and bool(lineas_c) and nombra_par_c)
        print("    ROJO con la letra y nombrando el par (%s, 1): %s" % (AB1, nombra_par_c))
        veredictos.append(("(C) cadena que no llega a viajar",
                           "VERDE" if ok_c else "ROJO, exit %d, lineas %d, nombra %s"
                           % (cod_c, len(lineas_c), nombra_par_c)))

        # ==================================================================
        # (D) DESTINO QUE NO EXISTE, POR LOS DOS LADOS.
        # ==================================================================
        print("")
        print("-" * 78)
        print("(D.1) MUTACION: VIAJA_EN_EL_ACTO a un absorbido que NO esta en la operacion.")
        fantasma = "v139_ab_fantasma_que_no_existe"
        pasos_d1 = {AB1: {"1": ["APPEND"], "2": ["APPEND"]},
                    AB2: {"1": ["APPEND"], "2": ["VIAJA_EN_EL_ACTO", fantasma, 1]}}
        escribir_contenido(tmp, "_banco_v139_fantasma", pasos_d1, cond_vacias,
                           lineas_de_viaje={"%s|2" % AB2: "el destino es " + fantasma})
        cod_d1, txt_d1, plan_d1 = correr_generador(gen, nodos_dir, operaciones, salida_dir,
                                                   "_banco_v139_fantasma")
        lineas_d1 = rojos_que_contienen(txt_d1, [fantasma, "NO esta en esta operacion"])
        print("    generador: exit %d | plan escrito: %s" % (cod_d1, bool(plan_d1)))
        for l in lineas_d1:
            print("       %s" % l)
        # NOMBRA LOS DOS: el absorbido fantasma y el numero de paso.
        nombra_d1 = any((fantasma in l) and ("el paso 1" in l) for l in lineas_d1)
        ok_d1 = (cod_d1 != 0 and plan_d1 is None and nombra_d1)
        print("    ROJO nombrando LOS DOS (absorbido y numero de paso): %s" % nombra_d1)
        veredictos.append(("(D.1) absorbido destino inexistente",
                           "VERDE" if ok_d1 else "ROJO, exit %d, nombra %s"
                           % (cod_d1, nombra_d1)))

        print("")
        print("(D.2) MUTACION: VIAJA_EN_EL_ACTO a un numero de paso que NO existe.")
        pasos_d2 = {AB1: {"1": ["APPEND"], "2": ["APPEND"]},
                    AB2: {"1": ["APPEND"], "2": ["VIAJA_EN_EL_ACTO", AB1, 99]}}
        escribir_contenido(tmp, "_banco_v139_paso99", pasos_d2, cond_vacias,
                           lineas_de_viaje={"%s|2" % AB2: "el destino es " + AB1})
        cod_d2, txt_d2, plan_d2 = correr_generador(gen, nodos_dir, operaciones, salida_dir,
                                                   "_banco_v139_paso99")
        lineas_d2 = rojos_que_contienen(txt_d2, ["ese paso NO existe"])
        print("    generador: exit %d | plan escrito: %s" % (cod_d2, bool(plan_d2)))
        for l in lineas_d2:
            print("       %s" % l)
        nombra_d2 = any((AB1 in l) and ("el paso 99" in l) for l in lineas_d2)
        ok_d2 = (cod_d2 != 0 and plan_d2 is None and nombra_d2)
        print("    ROJO nombrando LOS DOS (absorbido y numero de paso): %s" % nombra_d2)
        veredictos.append(("(D.2) numero de paso destino inexistente",
                           "VERDE" if ok_d2 else "ROJO, exit %d, nombra %s"
                           % (cod_d2, nombra_d2)))

        # ==================================================================
        # (iii) AUTO REFERENCIA.
        # ==================================================================
        print("")
        print("-" * 78)
        print("(iii) MUTACION: VIAJA_EN_EL_ACTO auto referente (mismo absorbido, mismo paso).")
        pasos_iii = {AB1: {"1": ["APPEND"], "2": ["APPEND"]},
                     AB2: {"1": ["APPEND"], "2": ["VIAJA_EN_EL_ACTO", AB2, 2]}}
        escribir_contenido(tmp, "_banco_v139_auto", pasos_iii, cond_vacias,
                           lineas_de_viaje={"%s|2" % AB2: "el destino es " + AB2})
        cod_iii, txt_iii, plan_iii = correr_generador(gen, nodos_dir, operaciones,
                                                      salida_dir, "_banco_v139_auto")
        lineas_iii = rojos_que_contienen(txt_iii, ["AUTO REFERENTE"])
        print("    generador: exit %d | plan escrito: %s" % (cod_iii, bool(plan_iii)))
        for l in lineas_iii:
            print("       %s" % l)
        ok_iii = (cod_iii != 0 and plan_iii is None and bool(lineas_iii))
        veredictos.append(("(iii) auto referencia",
                           "VERDE" if ok_iii else "ROJO, exit %d" % cod_iii))

        # ==================================================================
        # (v) LA LINEA EDITORIAL.
        # ==================================================================
        print("")
        print("-" * 78)
        print("(v.1) MUTACION: VIAJA_EN_EL_ACTO SIN linea editorial.")
        escribir_contenido(tmp, "_banco_v139_sinlinea", pasos_sano, cond_vacias,
                           lineas_de_viaje={})
        cod_v1, txt_v1, plan_v1 = correr_generador(gen, nodos_dir, operaciones, salida_dir,
                                                   "_banco_v139_sinlinea")
        lineas_v1 = rojos_que_contienen(txt_v1, ["SIN LINEA EDITORIAL"])
        print("    generador: exit %d | plan escrito: %s" % (cod_v1, bool(plan_v1)))
        for l in lineas_v1:
            print("       %s" % l)
        ok_v1 = (cod_v1 != 0 and plan_v1 is None and bool(lineas_v1))
        veredictos.append(("(v.1) sin linea editorial",
                           "VERDE" if ok_v1 else "ROJO, exit %d" % cod_v1))

        print("")
        print("(v.2) MUTACION: linea editorial que NO nombra al absorbido destino.")
        escribir_contenido(tmp, "_banco_v139_lineamuda", pasos_sano, cond_vacias,
                           lineas_de_viaje={"%s|2" % AB2: "Los dos dicen lo mismo."})
        cod_v2, txt_v2, plan_v2 = correr_generador(gen, nodos_dir, operaciones, salida_dir,
                                                   "_banco_v139_lineamuda")
        lineas_v2 = rojos_que_contienen(txt_v2, ["no NOMBRA al absorbido destino"])
        print("    generador: exit %d | plan escrito: %s" % (cod_v2, bool(plan_v2)))
        for l in lineas_v2:
            print("       %s" % l)
        ok_v2 = (cod_v2 != 0 and plan_v2 is None and bool(lineas_v2))
        veredictos.append(("(v.2) linea que no dice cual redaccion viaja",
                           "VERDE" if ok_v2 else "ROJO, exit %d" % cod_v2))

        # ==================================================================
        # (E) CERO ESCRITURA SI HAY FALLOS.
        # ==================================================================
        print("")
        print("-" * 78)
        quedan = sorted(os.listdir(salida_dir))
        print("(E) ficheros escritos en la salida tras los SEIS ROJOS: %s"
              % (", ".join(quedan) if quedan else "NINGUNO"))
        veredictos.append(("(E) cero escritura si hay fallos",
                           "VERDE" if not quedan else "ROJO, escribio %s" % quedan))
    finally:
        # P.16, QUIEN FABRICA LIMPIA.
        if tmp in sys.path:
            sys.path.remove(tmp)
        shutil.rmtree(tmp, ignore_errors=True)
        print("")
        print("  temporal retirado (P.16): %s" % (not os.path.exists(tmp)))

    print("")
    print("=" * 78)
    for nombre, v in veredictos:
        print("  %-48s %s" % (nombre, v))
    malos = [v for _, v in veredictos if v.startswith("ROJO")]
    if malos:
        print("ROJO: %d de %d casos no se sostienen." % (len(malos), len(veredictos)))
        print("FIN")
        return 1
    print("VERDE: los %d casos de la quinta marca se sostienen." % len(veredictos))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
