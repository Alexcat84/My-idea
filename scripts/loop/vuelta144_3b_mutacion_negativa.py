# -*- coding: utf-8 -*-
"""vuelta144_3b_mutacion_negativa.py . LA MUTACION NEGATIVA DE LA TAREA 3.b.

QUE PRUEBA. Que las guardas PROPIAS del sellador nuevo
(`vuelta144_3b_sellar_mesa_opm04.py`) MUERDEN, y que cuando muerden NO SE
ESCRIBE NADA: ni el plan ni un nodo.

TRES CASOS, todos EN MEMORIA, todos con `--simular` puesto para que ni en el
peor caso se toque el disco, y todos con la cifra leida de la salida real y
nunca contra un literal (EJECUTOR.md regla 1):

  (A) EL EMPAREJAMIENTO CAMBIADO. Se intercambian los absorbidos de los dos
      contenidos: el superviviente de la 367 pasa a absorber el gemelo de la 328
      y al reves. LA GUARDA 5 tiene que caer nombrando los dos repartos, el del
      contenido y el que la ficha declara. Es la guarda propia de este
      instrumento y la unica que ninguna de las del generador cubre.
  (B) LA MARCA QUE APUNTA FUERA. Se le pone a un paso una marca CUBIERTO a un
      numero mayor que los pasos del superviviente. Tiene que caer la aritmetica
      del generador, IMPORTADA y no copiada, que es justo lo que se quiere
      probar: que al no relajar ninguna guarda, las del generador siguen
      mordiendo dentro del sellador nuevo.
  (C) LA CONTRAPRUEBA. Sin mutar nada, el sellador sale VERDE. Sin ella, dos
      rojos no prueban nada.

Y AL FINAL, LA CUENTA QUE MANDA: `git status --porcelain -- dataset/ docs/loop/`
tiene que salir IGUAL que al empezar. Cero escrituras.

--- EL SUJETO DEJA DE SER EL ARBOL VIVO (VUELTA 145, TAREA 2.b; acta 144,
caida 4.9 del auditor) ---

CORRECCION DECLARADA, y el texto de arriba NO SE BORRA porque sigue diciendo
exactamente lo que este arnes prueba (EJECUTOR.md 8).

EL DEFECTO, MEDIDO. Corrido sobre el arbol limpio de la apertura de la vuelta
145 este arnes daba 1 de 3: (C), la contraprueba, pedia que el sellador de
`OP-M-04` saliera VERDE, y el sellador contestaba *"ROJO, 2 fallo(s): el nodo
formalize_advisory_board YA esta deprecado, el nodo identificar_junta_asesores
YA esta deprecado"*. LA FUSION QUE ESTE ARNES SELLA YA CORRIO, en el commit
`c72ce2c0` de la vuelta 144: el mundo que (C) necesita no existe desde
entonces, y (B) caia detras porque el sellador aborta antes de llegar a la
aritmetica que (B) mide. No era un fallo de la guarda: era un arnes sin sujeto.

EL ARREGLO. El sujeto pasa a ser EL PRE-ESTADO CONGELADO, montado en un
directorio temporal por `vuelta145_2b_prestado_congelado.materializar()` a
partir de un ref de git, y las dos rutas que el sellador lee
(`dataset/nodos/` via `S.NODOS`, y `docs/plan/OPERACIONES.jsonl` via
`G.OPERACIONES`) se apuntan alli mientras dura el arnes. EL REF SE COMPUTA, NO
SE TECLEA: `ref_del_preestado()` busca el commit MAS NUEVO que deja deprecado
al absorbido y devuelve SU PADRE, o sea el arbol justo antes de la cirugia.
Medido en la vuelta 145: para los dos absorbidos da el mismo ref, `5fff85f7`,
deprecados los dos en `c72ce2c0`. Si los dos absorbidos dieran refs distintos,
ROJO PREVIO: no se elige uno.

P.16, QUIEN FABRICA LIMPIA: el temporal se retira siempre, y la cuenta de cero
escrituras sobre el arbol de verdad se mantiene igual que antes.

--- ADJUDICACION 6.7 DEL ACTA 158 (3 sep 2026): EL CHECK DE P.16 SE CINE AL
CONTENIDO Y A LA VENTANA DEL PROPIO SCRIPT ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra, y el check que este
fichero lleva NO se modifica al escribir esto: esto es la adjudicacion, no el
remedio.

LAS DOS ANCLAS QUE SE MUEVEN EN LA MISMA LINEA, y el hallazgo es del ejecutor de
la vuelta 157, que lo trajo como pregunta en vez de esquivarlo callando. El
docstring dice que se comprueba que `dataset/` y `docs/plan/` NO SE TOCAN NI UNA
VEZ, o sea CONTENIDO. El instrumento es `git status --porcelain`, que ademas de
contenido ve:
  (i)  ESTADO DE FIN DE LINEA. Este repo tiene `core.autocrlf`, asi que un
       fichero reescrito por el ciclo queda marcado como modificado aunque su
       sha256 NORMALIZADO sea identico al de HEAD. Paso de verdad en la vuelta
       157 y tumbo tres mutaciones de la bateria en ROJO con el contenido
       intacto.
  (ii) SUCIEDAD ANTERIOR AL ARRANQUE DEL SCRIPT, que no es suya. El veredicto de
       este check depende de si alguien committeo tocando `dataset/` antes, y no
       de si las mutaciones de este fichero tocaron el dataset.

EL REMEDIO ADJUDICADO: huella de CONTENIDO tomada ANTES y DESPUES de las
mutaciones DENTRO del propio script, y comparada consigo misma. Con su caso
positivo por mutacion: si una mutacion escribe de verdad en `dataset/` o en
`docs/plan/`, el check SIGUE SALIENDO ROJO.

EL ALCANCE, Y AQUI HAY UNA DISCREPANCIA DE CIFRA QUE SE DECLARA EN VEZ DE
COPIARSE: el acta 158 mide ONCE ficheros con el patron literal, siete de ellos
dentro de la bateria de las 23. El recomputo de la vuelta 159
(`scripts/loop/vuelta159_tarea1_registrar_adjudicaciones.py`, funcion
`ficheros_con_patron_p16`, salida `docs/loop/SALIDA_V159_T1_ADJUDICACIONES.txt`)
da DOCE ficheros, y los SIETE de la bateria reproducen exactamente. El duodecimo
es `scripts/loop/vuelta89_tarea4_guarda_op_c05.py`: excluirlo devuelve los once
del acta al digito. La cifra de la vuelta 159 es la del computo, y por eso el
remedio de la 6.7 queda EN PARADA, declarada en el reporte de la vuelta 159.

--- ADJUDICACION 6.1 DEL ACTA 159 (3 sep 2026): EL ALCANCE DEL CHECK DE P.16 SON
DOCE, NO ONCE, Y LA VARA ES LA LECTURA B ---

CORRECCION DECLARADA POR ADICION. Nada de lo escrito arriba se borra, y en
particular NO SE BORRA la cifra ONCE que la adjudicacion 6.7 del acta 158 dejo
escrita: se corrige delante de ella para que la correccion se pueda auditar.

LA CIFRA VIEJA Y LA NUEVA, LAS DOS ESCRITAS. El acta 158 midio ONCE ficheros de
`scripts/loop/` con el patron literal del check de P.16 y su encargo mando parar
si la cuenta no daba once. La vuelta 159 recomputo y dio DOCE, paro por mandato
literal y NO TOCO UN SOLO CHECK. EL ACTA 159 ADJUDICA QUE SON DOCE Y QUE LA
CIFRA EQUIVOCADA ERA LA DEL ACTA, o sea la del auditor: lo midio el en dos
arboles distintos, el del commit del acta 158 y HEAD, y los dos dan 4 / 12 / 14
ficheros y 3 / 7 / 7 dentro de la bateria de las 23. EL ONCE NUNCA FUE CIERTO, y
la diferencia no la introdujo ninguna vuelta.

LA VARA DE LA LECTURA ES LA B, Y SE NOMBRA PARA QUE NO VUELVA A DERIVAR: B MEDIA
es "pathspec que empieza por dataset/", que es la que el ejecutor publico como
principal y la que la 6.7 del acta 158 sostiene al describir el defecto por su
instrumento. LA LECTURA ESTRECHA DE CUATRO (dataset/ Y docs/plan/ a la vez) NO
VALE, porque el defecto no depende de que el pathspec traiga tambien docs/plan/.

EL DUODECIMO ENTRA Y TIENE NOMBRE: `vuelta89_tarea4_guarda_op_c05.py`. Es del
mismo defecto que la serie 142 a 147, solo que mas viejo, y lleva las dos anclas
que la 6.7 describe (la del fin de linea y la de la suciedad anterior al
arranque), leidas por el auditor en su fuente. NO HAY MOTIVO DE VARA PARA
EXCLUIRLO.

LO QUE ESTO OBLIGA: la 5.a y la 5.c del encargo de la vuelta 159 se ejecutan
sobre LOS DOCE, no sobre once ni sobre cuatro. La nomina no se teclea: se
recomputa, y su medicion esta pegada en `docs/loop/SALIDA_V159_T5_ALCANCE.txt`.
"""
import copy
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
sys.path.insert(0, LOOP)

import _v144_opm04_328 as C328  # noqa: E402
import _v144_opm04_367 as C367  # noqa: E402
import generar_plan_de_fusion_de_mesa as G  # noqa: E402
import vuelta144_3b_sellar_mesa_opm04 as S  # noqa: E402
from vuelta145_2b_prestado_congelado import (  # noqa: E402
    materializar, ref_del_preestado)

# Las rutas que el sellador lee y que el pre-estado tiene que traer consigo.
RUTAS_DEL_PREESTADO = ["docs/plan/OPERACIONES.jsonl"]



# --- REMEDIO DEL CHECK DE P.16 (vuelta 160, TAREA 3.a; adjudicacion 6.7 del
# acta 158 y 6.1 del acta 159). La huella NO MIRA A GIT: compara el disco contra
# el disco, y por eso ni el estado de fin de linea ni la suciedad anterior al
# arranque pueden moverla. Ver scripts/loop/huella_de_contenido.py ---
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import huella_de_contenido as _HC  # noqa: E402
_P16_RUTAS = ("dataset/", "docs/loop/")


def estado():
    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS, TACHADAS:
    #     ~~return subprocess.run(["git", "status", "--porcelain", "--", "dataset/", "docs/loop/"],~~
    #     ~~                      cwd=RAIZ, capture_output=True, text=True).stdout~~
    #     ~~print("CERO ESCRITURAS: git status -- dataset/ docs/loop/ identico al de la apertura "~~
    #     ~~      "del arnes: %s" % igual)~~
    # Se llama ANTES y DESPUES: la figura era correcta y el instrumento no.
    return _HC.huella(*_P16_RUTAS)


class Capturada(object):
    def __init__(self):
        self.trozos = []

    def write(self, s):
        self.trozos.append(s)
        return len(s)

    def flush(self):
        pass

    def reconfigure(self, **kw):
        return None

    def valor(self):
        return "".join(self.trozos)


def correr(argv):
    real_argv, real_out = sys.argv, sys.stdout
    buf = Capturada()
    try:
        sys.argv = argv
        sys.stdout = buf
        try:
            codigo = S.main()
        except SystemExit as e:
            codigo = e.code if isinstance(e.code, int) else 1
    finally:
        sys.argv, sys.stdout = real_argv, real_out
    return codigo, buf.valor()


def miembros_de_la_mesa():
    """Los cuatro miembros, leidos de los dos contenidos y no tecleados."""
    fuera = []
    for spec in (C367.FUSION, C328.FUSION):
        fuera.append(spec["superviviente"])
        fuera.extend(spec["absorbidos"])
    return sorted(set(fuera))


def absorbidos_de_la_mesa():
    return sorted(set(list(C367.FUSION["absorbidos"]) + list(C328.FUSION["absorbidos"])))


def ref_unico_del_preestado():
    """EL REF DEL PRE-ESTADO, COMPUTADO DE LOS ABSORBIDOS Y EXIGIDO UNICO.
    Devuelve (ref, detalle). Si los absorbidos dan refs distintos, o alguno no
    da ninguno, devuelve (None, detalle) y quien llama para: no se elige uno."""
    detalle = []
    refs = set()
    for x in absorbidos_de_la_mesa():
        ref, deprecado_en, _hist = ref_del_preestado(x)
        detalle.append((x, ref, deprecado_en))
        refs.add(ref)
    if len(refs) != 1 or None in refs:
        return None, detalle
    return refs.pop(), detalle


def main():
    argv = ["vuelta144_3b_sellar_mesa_opm04.py", "--simular"]
    antes = estado()
    guardadas = (copy.deepcopy(C367.FUSION), copy.deepcopy(C328.FUSION))

    print("MUTACION NEGATIVA DE LA TAREA 3.b | vuelta 144")
    print("Todo EN MEMORIA y con --simular: ni el plan ni un nodo se tocan.")
    print("=" * 78)

    # ---- EL SUJETO CONGELADO (vuelta 145, TAREA 2.b) -----------------------
    ref, detalle = ref_unico_del_preestado()
    print("SUJETO CONGELADO: el pre-estado, con el ref COMPUTADO de los absorbidos")
    for x, r, dep in detalle:
        print("     %-32s pre-estado %s | deprecado en %s"
              % (x, (r or "NINGUNO")[:8], (dep or "NINGUNO")[:8]))
    if ref is None:
        print("")
        print("ROJO PREVIO: los absorbidos no dan un unico ref de pre-estado; "
              "no se elige uno y el arnes no mide nada")
        return 1
    rutas = RUTAS_DEL_PREESTADO + ["dataset/nodos/%s.json" % x for x in miembros_de_la_mesa()]
    print("     ref elegido: %s | %d ruta(s) materializadas" % (ref[:8], len(rutas)))
    print("")

    nodos_real, operaciones_real = S.NODOS, G.OPERACIONES
    resultados = []
    with materializar(ref, rutas) as raiz:
        S.NODOS = os.path.join(raiz, "dataset", "nodos")
        G.OPERACIONES = os.path.join(raiz, "docs", "plan", "OPERACIONES.jsonl")
        try:
            return _casos(argv, guardadas, resultados, antes)
        finally:
            S.NODOS, G.OPERACIONES = nodos_real, operaciones_real


def _casos(argv, guardadas, resultados, antes):
    try:
        # ---- (C) LA CONTRAPRUEBA, primero -----------------------------------
        cod_c, sal_c = correr(argv)
        ok_c = cod_c == 0 and "SIMULACION: el plan NO se escribe" in sal_c
        print("(C) CONTRAPRUEBA, sin mutar nada: codigo %r" % cod_c)
        print("     VEREDICTO: %s" % ("OK" if ok_c else "ROJO"))
        resultados.append(("(C) contraprueba, el sellador sale VERDE", ok_c))
        print("")

        # ---- (A) EL EMPAREJAMIENTO CAMBIADO ---------------------------------
        a367, a328 = C367.FUSION["absorbidos"], C328.FUSION["absorbidos"]
        C367.FUSION["absorbidos"] = list(a328)
        C367.FUSION["pasos"] = {a328[0]: {}}
        C367.FUSION["condiciones"] = {a328[0]: {}}
        C328.FUSION["absorbidos"] = list(a367)
        C328.FUSION["pasos"] = {a367[0]: {}}
        C328.FUSION["condiciones"] = {a367[0]: {}}
        cod_a, sal_a = correr(argv)
        cae_guarda5 = "guarda 5, el emparejamiento del contenido calza con el de la ficha: ROJO" in sal_a
        nombra = "NO es el que la ficha declara" in sal_a
        no_escribe = "NO se escribe nada" in sal_a
        ok_a = cod_a != 0 and cae_guarda5 and nombra and no_escribe
        print("(A) EMPAREJAMIENTO CAMBIADO (los dos absorbidos intercambiados):")
        print("     codigo %r | la guarda 5 cae: %s | nombra los dos repartos: %s | no "
              "escribe nada: %s" % (cod_a, cae_guarda5, nombra, no_escribe))
        for ln in sal_a.splitlines():
            if "guarda 5" in ln or "NO es el que la ficha declara" in ln:
                print("     %s" % ln.strip()[:180])
        print("     VEREDICTO: %s" % ("OK" if ok_a else "ROJO"))
        resultados.append(("(A) emparejamiento cambiado, cae la guarda 5", ok_a))
        print("")

        # ---- (B) LA MARCA QUE APUNTA FUERA ----------------------------------
        C367.FUSION.update(copy.deepcopy(guardadas[0]))
        C328.FUSION.update(copy.deepcopy(guardadas[1]))
        ab = C367.FUSION["absorbidos"][0]
        fuera = 99
        C367.FUSION["pasos"] = copy.deepcopy(C367.FUSION["pasos"])
        C367.FUSION["pasos"][ab]["1"] = ["CUBIERTO", fuera]
        cod_b, sal_b = correr(argv)
        cae_aritmetica = "CUBIERTO:%d y el superviviente tiene" % fuera in sal_b
        no_escribe_b = "NO se escribe nada" in sal_b
        ok_b = cod_b != 0 and cae_aritmetica and no_escribe_b
        print("(B) MARCA CUBIERTO:%d, fuera del rango del superviviente:" % fuera)
        print("     codigo %r | cae la aritmetica IMPORTADA del generador: %s | no escribe "
              "nada: %s" % (cod_b, cae_aritmetica, no_escribe_b))
        for ln in sal_b.splitlines():
            if "CUBIERTO:%d" % fuera in ln:
                print("     %s" % ln.strip()[:180])
        print("     VEREDICTO: %s" % ("OK" if ok_b else "ROJO"))
        resultados.append(("(B) marca fuera de rango, cae la aritmetica", ok_b))
        print("")
    finally:
        C367.FUSION.clear()
        C367.FUSION.update(guardadas[0])
        C328.FUSION.clear()
        C328.FUSION.update(guardadas[1])

    despues = estado()
    igual = despues == antes
    print("=" * 78)
    buenas = sum(1 for _, ok in resultados if ok)
    for nombre, ok in resultados:
        print("  %-48s %s" % (nombre, "OK" if ok else "ROJO"))
    print("")
    print("CERO ESCRITURAS: huella de CONTENIDO de dataset/ y docs/loop/ identica a la "
          "de la apertura del arnes: %s" % igual)
    print("   %s" % _HC.comparar(antes, despues, *_P16_RUTAS)[1])
    print("")
    print("COMPROBACIONES QUE MUERDEN: %d de %d" % (buenas, len(resultados)))
    return 0 if buenas == len(resultados) and igual else 1


if __name__ == "__main__":
    raise SystemExit(main())
