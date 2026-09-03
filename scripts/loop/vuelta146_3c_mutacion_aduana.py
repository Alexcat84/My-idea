# -*- coding: utf-8 -*-
r"""vuelta146_3c_mutacion_aduana.py . LOS CASOS ROJOS DE LOS TRES CONTROLES DE
`OP-A-01` CABLEADOS A GATE 0 (TAREAS 3.b y 3.c de la vuelta 146).

QUE PRUEBA, Y SOBRE QUE. Que los tres `checks` que la vuelta 146 anade a
`step7_validate` de `scripts/run_phase1.py` MUERDEN. Una guarda que no muerde no
es una guarda (banco 9), y un caso rojo que no puede fallar no es una prueba
(`EJECUTOR.md` 1, caida 2 de la vuelta 89).

TODAS LAS MUTACIONES SON SOBRE UNA VARIABLE QUE EL CODIGO COMPUTA, NUNCA SOBRE
UN LITERAL, Y SOBRE COPIA EN MEMORIA: se parchea `run_phase1.load_json` para
que UN fichero de nodo devuelva un diccionario alterado, y el parche se
restaura siempre. CERO ESCRITURAS EN `dataset/`, comprobado por el propio arnes
con `git status --porcelain -- dataset/` ANTES y DESPUES, cuya igualdad forma
parte del veredicto.

LOS SUJETOS SE ELIGEN POR COMPUTO, no se teclean: el nodo que se muta sale de
leer el grafo en esta corrida (el primero de la nomina de fuente multiple, y
para el caso del nodo nuevo, el primer nodo vivo de una sola fuente).

LOS CUATRO CASOS:

  (A) CONTROL POSICIONAL, NODO NUEVO SIN ADJUDICAR. A un nodo vivo de UNA sola
      fuente se le anade en memoria un SEGUNDO libro (uno canonico de la tabla,
      elegido por computo, para que el caso pruebe el control posicional y no de
      rebote el canonico). El check posicional tiene que pasar de OK a FALLO
      nombrandolo.

  (B) CONTROL POSICIONAL, SEGUNDO LIBRO ANADIDO EN SILENCIO A UNO YA ADJUDICADO.
      A un nodo que YA esta en la nomina se le anade una tercera declaracion. El
      check tiene que caer, porque la lista se coteja ENTERA Y EN ORDEN. Sin este
      caso, el control solo probaria que sabe ver un id que no esta en la lista.

  (C) CAMPO FUENTE CANONICO (el control A2.4, TAREA 3.c). A un nodo vivo se le
      pone una grafia FUERA DE LA TABLA, computada como la canonica del nodo con
      un sufijo que ninguna canonica tiene. Gate 0 tiene que caer nombrandolo.

  (D) EL SEGUNDO LIBRO SIN NI UN PASO. A un nodo de la nomina se le vacian los
      `pasos_accionables` en memoria. El tercer check tiene que caer nombrandolo.

Y LA CONTRAPRUEBA, QUE VA EN TODOS: sin mutar nada, los tres checks salen OK.
Sin ella, un rojo podria estar saliendo por cualquier otra causa.

USO:
  python scripts/loop/vuelta146_3c_mutacion_aduana.py

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
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import run_phase1 as R  # noqa: E402
from vuelta136_simular_ops11 import cargar_tabla  # noqa: E402

ROTULO_POSICIONAL = "OP-A-01: todo nodo VIVO con MAS DE UNA fuente pasa la comprobacion posicional"
ROTULO_CANONICO = "OP-A-01 / OP-A-02 (A2.4): el campo `fuente` resuelve contra la lista CANONICA de libros"
ROTULO_PASOS = "OP-A-01: ningun nodo declara un SEGUNDO libro sin tener ni un paso donde pueda aparecer"

_load_json_real = R.load_json


def estado_dataset():
    r = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                       cwd=RAIZ, capture_output=True, text=True)
    return r.stdout


def correr_checks(mutaciones=None):
    """Corre step7_validate con `run_phase1.load_json` parcheado. `mutaciones`
    es {stem_del_fichero: funcion(datos)->datos}. Devuelve {rotulo: (ok, detalle)}.

    NO recompila el grafo: lee el master_graph.json ya compilado del arbol. Los
    tres checks de OP-A-01 leen los ficheros de nodo directamente (por eso
    parchear load_json basta) y `verificar_fuente_canonico` tambien."""
    mutaciones = mutaciones or {}

    def load_json_parcheado(path):
        datos = _load_json_real(path)
        stem = os.path.splitext(os.path.basename(str(path)))[0]
        fn = mutaciones.get(stem)
        return fn(copy.deepcopy(datos)) if fn else datos

    R.load_json = load_json_parcheado
    # verificar_fuente_canonico lee con su propio io.open, asi que se le
    # parchea su cargador por el mismo camino: se sustituye la funcion que
    # produce (id, fuente) por una que aplica las mismas mutaciones.
    import verificar_fuente_canonico as V
    cargar_real = V.cargar_nodos_vivos

    def cargar_parcheado(overrides=None):
        filas = cargar_real(overrides)
        if not mutaciones:
            return filas
        salida = []
        for nid, fuente in filas:
            fn = mutaciones.get(nid)
            if fn:
                fuente = fn({"fuente": fuente}).get("fuente")
            salida.append((nid, fuente))
        return salida

    V.cargar_nodos_vivos = cargar_parcheado
    try:
        master = _load_json_real(R.MASTER_GRAPH_PATH)
        checks, _ = R.step7_validate(master, [], None)
    finally:
        R.load_json = _load_json_real
        V.cargar_nodos_vivos = cargar_real
    return {rot: (bool(ok), det) for rot, ok, det in checks}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    antes = estado_dataset()

    # SUJETOS ELEGIDOS POR COMPUTO
    nomina = json.loads(io.open(
        os.path.join(RAIZ, "dataset", "metadata", "aduana_fuente_multiple.json"),
        encoding="utf-8").read())["adjudicados"]
    adjudicado = nomina[0]["node_id"]
    canonicas = sorted(set(cargar_tabla().values()))
    libro_extra = canonicas[0]

    base = correr_checks()
    contraprueba = all(base[r][0] for r in (ROTULO_POSICIONAL, ROTULO_CANONICO, ROTULO_PASOS))

    # el primer nodo vivo de UNA sola fuente, computado
    import verificar_fuente_canonico as V
    suelto = None
    for nid, fuente in V.cargar_nodos_vivos():
        if isinstance(fuente, str) and " | " not in fuente and nid not in {x["node_id"] for x in nomina}:
            suelto, fuente_suelto = nid, fuente
            break

    casos = []

    def anadir_libro(datos, libro=libro_extra):
        datos["fuente"] = "%s | %s" % (datos.get("fuente"), libro)
        return datos

    cA = correr_checks({suelto: anadir_libro})
    okA = (not cA[ROTULO_POSICIONAL][0]) and (suelto in str(cA[ROTULO_POSICIONAL][1]))
    casos.append(("A nodo nuevo con dos libros sin adjudicar", okA, suelto,
                  cA[ROTULO_POSICIONAL]))

    cB = correr_checks({adjudicado: anadir_libro})
    okB = (not cB[ROTULO_POSICIONAL][0]) and (adjudicado in str(cB[ROTULO_POSICIONAL][1]))
    casos.append(("B tercer libro anadido en silencio a uno ya adjudicado", okB, adjudicado,
                  cB[ROTULO_POSICIONAL]))

    def grafia_fuera_de_tabla(datos):
        datos["fuente"] = "%s, EDICION QUE NINGUNA CANONICA TIENE" % datos.get("fuente")
        return datos

    cC = correr_checks({suelto: grafia_fuera_de_tabla})
    okC = (not cC[ROTULO_CANONICO][0]) and (suelto in str(cC[ROTULO_CANONICO][1]))
    casos.append(("C grafia fuera de la tabla canonica (control A2.4)", okC, suelto,
                  cC[ROTULO_CANONICO]))

    def vaciar_pasos(datos):
        datos["pasos_accionables"] = []
        return datos

    cD = correr_checks({adjudicado: vaciar_pasos})
    okD = (not cD[ROTULO_PASOS][0]) and (adjudicado in str(cD[ROTULO_PASOS][1]))
    casos.append(("D segundo libro sin ni un paso", okD, adjudicado, cD[ROTULO_PASOS]))

    despues = estado_dataset()
    dataset_intacto = (antes == despues)

    print("MUTACIONES DE LOS TRES CONTROLES DE OP-A-01 EN GATE 0 | vuelta 146, 3.b y 3.c")
    print("=" * 78)
    print("SUJETOS ELEGIDOS POR COMPUTO: adjudicado %r | suelto %r | libro extra %r"
          % (adjudicado, suelto, libro_extra))
    print("")
    print("CONTRAPRUEBA, SIN MUTAR NADA: los tres checks salen OK: %s" % contraprueba)
    for r in (ROTULO_POSICIONAL, ROTULO_CANONICO, ROTULO_PASOS):
        print("   [%s] %s (valor: %s)" % ("OK" if base[r][0] else "FALLO", r, base[r][1]))
    print("")
    for rot, ok, sujeto, (ok_check, detalle) in casos:
        print("%s" % rot)
        print("   sujeto %r | el check pasa a FALLO: %s | lo nombra: %s"
              % (sujeto, not ok_check, sujeto in str(detalle)))
        print("   valor del check: %s" % str(detalle)[:220])
        print("   VEREDICTO: %s" % ("OK" if ok else "ROJO"))
        print("")
    print("dataset/ IDENTICO antes y despues (cero escrituras): %s" % dataset_intacto)
    print("=" * 78)
    buenas = sum(1 for _, ok, _, _ in casos if ok)
    print("CASOS QUE MUERDEN: %d de %d" % (buenas, len(casos)))
    todo = (buenas == len(casos)) and contraprueba and dataset_intacto
    print("VEREDICTO GLOBAL: %s" % ("VERDE" if todo else "ROJO"))
    return 0 if todo else 1


if __name__ == "__main__":
    raise SystemExit(main())
