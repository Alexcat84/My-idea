# -*- coding: utf-8 -*-
"""vuelta144_2b_mutacion_giro.py . LA MUTACION DE LA TAREA 2.b, vuelta 144.

QUE PRUEBA. Que `vuelta143_3c_girar_arista.py` ya NO se come los fallos del
parser de la excepcion (acta 143, adjudicacion 3.3 y caida de la casa 4.4).
Hasta la 143 la guarda 5 llamaba a `T.pares_exceptuados_de(op, resolver, [])` y
TIRABA la lista: si el parseo fallaba, el conjunto salia vacio, `exceptuado`
salia False, la guarda decia OK y EL GIRO PROCEDIA A BORRAR UNA ARISTA. De los
tres instrumentos que leen la excepcion, ese era el unico que se comia sus
fallos, y es el unico que DESTRUYE.

COMO SE MUTA, SIN TOCAR EL DISCO. Dos monkeypatches y ninguna escritura:
  - `T.cargar_ops` devuelve las fichas EN MEMORIA con la formula canonica ROTA
    (se le quita la marca de cierre) en la ficha que dispara la excepcion;
  - `T.cargar_grafo` devuelve un GRAFO SIMULADO en el que el par elegido tiene
    FORMA DE GIRO (la vuelta puesta y la ida ausente).

POR QUE HACE FALTA EL GRAFO SIMULADO, y se dice en vez de esconderlo: la guarda
5 es la QUINTA. Para llegar a ella hay que pasar la 3 ("el estado de partida es
el de un giro") y la 4 ("la ficha prohibe la vuelta y nombra el par"). Todos los
pares que la excepcion del 9.22 exceptua son MUTUOS por definicion, o sea que
tienen sus DOS direcciones puestas, y con las dos puestas la guarda 3 aborta
antes ("las dos estan puestas: eso es una PODA"). Sin simular el grafo, la
mutacion caeria por la guarda equivocada y no probaria nada de la 5: se corrio
primero sin simular y se vio caer exactamente asi. Es el mismo patron que
`vuelta142_2c_mutaciones.py` estreno y que el acta 143 aprobo en su adjudicacion
3.7.

LAS TRES COMPROBACIONES:
  (A) LA MUTACION. Formula rota, `--ejecutar` puesto. El giro tiene que salir
      con codigo DISTINTO DE CERO, NOMBRAR el fallo del parser en la guarda 5 y
      dejar `git status --porcelain -- dataset/` sin mover NI UNA FILA.
  (B) EL CONTRASTE CON EL CODIGO VIEJO, medido y no supuesto. Con esa MISMA
      ficha rota, la lectura que descartaba los fallos devuelve conjunto VACIO,
      asi que `exceptuado` salia False y LA GUARDA 5 VIEJA HABRIA DICHO OK. Es
      la prueba de que el arreglo cambia el comportamiento, no solo el texto.
  (C) LA CONTRAPRUEBA. Mismo grafo simulado, formula ENTERA. La guarda 5 sigue
      abortando (el par ESTA exceptuado, que es lo correcto) pero por el motivo
      BUENO y no por fallo de parser, y tambien con cero escrituras. Sin esta,
      un giro que abortara siempre pasaria (A) sin significar nada.

EL SUJETO SE ELIGE POR COMPUTO: la primera ficha que dispare la excepcion con
pares nombrados, y el par es el primero en orden de los que esa misma ficha
exceptua, que es justo el que el giro NO debe poder borrar.

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
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import tallar_estado_de_fase as T  # noqa: E402
import vuelta143_3c_girar_arista as G  # noqa: E402



# --- REMEDIO DEL CHECK DE P.16 (vuelta 160, TAREA 3.a; adjudicacion 6.7 del
# acta 158 y 6.1 del acta 159). La huella NO MIRA A GIT: compara el disco contra
# el disco, y por eso ni el estado de fin de linea ni la suciedad anterior al
# arranque pueden moverla. Ver scripts/loop/huella_de_contenido.py ---
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import huella_de_contenido as _HC  # noqa: E402
_P16_RUTAS = ("dataset/",)


def estado_dataset():
    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LAS LINEAS VIEJAS QUEDAN
    # AQUI, TACHADAS Y LEGIBLES:
    #     ~~return subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],~~
    #     ~~                      cwd=RAIZ, capture_output=True, text=True).stdout~~
    # ESTA FUNCION SE LLAMA ANTES Y DESPUES DE CADA MUTACION, o sea que la
    # figura ya era la correcta y lo que fallaba era el instrumento. Devuelve la
    # HUELLA DE CONTENIDO y con eso el arnes deja de depender del fin de linea y
    # de la suciedad anterior al arranque, que son las dos anclas de la 6.7.
    return _HC.huella(*_P16_RUTAS)


def romper_formula(ops, idx_ficha, idx_linea):
    """Quita la marca de CIERRE de la formula canonica, en memoria."""
    copia = copy.deepcopy(ops)
    linea = copia[idx_ficha]["verificacion"][idx_linea]
    i = linea.lower().find(T.MARCA_CIERRA_EXCEPCION)
    assert i >= 0, "la ficha no trae la marca de cierre: no hay nada que romper"
    copia[idx_ficha]["verificacion"][idx_linea] = (
        linea[:i] + linea[i + len(T.MARCA_CIERRA_EXCEPCION):])
    return copia


def grafo_con_forma_de_giro(nodos, resolver, rd, rh):
    """Copia del grafo en la que la IDA rh -> rd NO esta y la VUELTA rd -> rh
    si. Es lo que la guarda 3 del giro exige para dejar seguir."""
    copia = copy.deepcopy(nodos)
    copia[rh]["nodos_siguientes"] = [x for x in (copia[rh].get("nodos_siguientes") or [])
                                     if resolver(x) != rd]
    copia[rd]["nodos_previos"] = [x for x in (copia[rd].get("nodos_previos") or [])
                                  if resolver(x) != rh]
    return copia


class Capturada(io.StringIO):
    """`sys.stdout` de mentira. El giro llama a `sys.stdout.reconfigure()` en su
    primera linea (para forzar utf-8 en la consola de Windows), asi que el
    sustituto tiene que aceptar esa llamada sin hacer nada."""

    def reconfigure(self, **kw):
        return None


def correr_giro(argv, ops_falsas, grafo_falso):
    """Corre G.main() con argv dado y con las dos cargas parcheadas. Devuelve
    (codigo, salida)."""
    real_ops = T.cargar_ops
    real_grafo = T.cargar_grafo
    real_argv = sys.argv
    real_stdout = sys.stdout
    buf = Capturada()
    try:
        T.cargar_ops = lambda ref="WORK": copy.deepcopy(ops_falsas)
        T.cargar_grafo = lambda ref="WORK": copy.deepcopy(grafo_falso)
        sys.argv = argv
        sys.stdout = buf
        try:
            codigo = G.main()
        except SystemExit as e:
            codigo = e.code if isinstance(e.code, int) else 1
    finally:
        T.cargar_ops = real_ops
        T.cargar_grafo = real_grafo
        sys.argv = real_argv
        sys.stdout = real_stdout
    return codigo, buf.getvalue()


def guardas_de(salida):
    return [ln for ln in salida.splitlines()
            if ln.startswith("guarda") or "ABORTA" in ln or ln.startswith("   OP-")
            or ln.startswith("   NO se puede") or ln.startswith("   el par")
            or ln.startswith("SIMULACION")]


def main():
    ops = T.cargar_ops("WORK")
    nodos = T.cargar_grafo("WORK")
    resolver = T.resolver_de(nodos)

    print("MUTACION DE LA TAREA 2.b | vuelta 144")
    print("Sujeto y par POR COMPUTO. Fichas y grafo EN MEMORIA: el disco no se toca.")
    print("=" * 78)

    # ---- EL SUJETO, POR COMPUTO -------------------------------------------
    # LOS FALLOS DEL PARSER SE RECOGEN Y SE DICEN (vuelta 145, TAREA 2.c; acta
    # 144, caida 4.1 del auditor). El texto viejo de este bucle pasaba una
    # LISTA LITERAL VACIA, `T.pares_exceptuados_de(op, resolver, [])`, que es
    # exactamente el defecto que ESTE MISMO INSTRUMENTO nacio para probar
    # reparado en el giro. La llamada de la comprobacion (B), mas abajo, SI
    # sigue tirandolos A PROPOSITO y lo dice en su comentario: esa es la
    # contraprueba del codigo viejo y no se toca.
    idx_ficha = None
    fallos_del_censo = []
    for i, op in enumerate(ops):
        fallos_de_esta = []
        conj, cita, nomina = T.pares_exceptuados_de(op, resolver, fallos_de_esta)
        if fallos_de_esta:
            fallos_del_censo.append((op.get("id_op"), list(fallos_de_esta)))
        if conj:
            idx_ficha, sujeto, pares_exc, nomina_exc = i, op, conj, nomina
            break
    if fallos_del_censo:
        print("FICHAS CUYA EXCEPCION NO PARSEA, NOMBRADAS EN VEZ DE SALTADAS (%d):"
              % len(fallos_del_censo))
        for id_op, fs in fallos_del_censo:
            for f in fs:
                print("     %s: %s" % (id_op, f))
        print("")
    if idx_ficha is None:
        print("OMITIDO POR FALTA DE SUJETO: ninguna ficha dispara la excepcion. ESO ES ROJO.")
        return 1

    idx_linea = None
    for j, linea in enumerate(sujeto.get("verificacion") or []):
        if any(f in (linea or "").lower() for f in T.FRASES_EXCEPCION_PAR):
            idx_linea = j
            break

    # El par se elige POR COMPUTO: el primero en orden de los que la propia
    # ficha exceptua.
    par = sorted(sorted(pares_exc, key=lambda x: sorted(x))[0])
    rd, rh = par[0], par[1]
    print("SUJETO: %s, verificacion %d" % (sujeto.get("id_op"), idx_linea))
    print("PARES QUE LA FICHA EXCEPTUA (%d): %s" % (len(nomina_exc), ", ".join(nomina_exc)))
    print("PAR QUE SE LE PASA AL GIRO: se retira %s -> %s y se escribiria %s -> %s"
          % (rd, rh, rh, rd))

    grafo = grafo_con_forma_de_giro(nodos, resolver, rd, rh)
    res_sim = T.resolver_de(grafo)
    print("GRAFO SIMULADO: la VUELTA %s -> %s puesta: %s | la IDA %s -> %s puesta: %s"
          % (rd, rh, T.arista_presente(grafo, res_sim, rd, rh)[0],
             rh, rd, T.arista_presente(grafo, res_sim, rh, rd)[0]))
    print("")

    resultados = []
    argv_base = ["vuelta143_3c_girar_arista.py",
                 "--retirar-de", rd, "--retirar-a", rh,
                 "--por-la-op", sujeto["id_op"]]

    # ---- (A) LA MUTACION ---------------------------------------------------
    antes = estado_dataset()
    ops_rotas = romper_formula(ops, idx_ficha, idx_linea)
    codigo, salida = correr_giro(argv_base + ["--ejecutar"], ops_rotas, grafo)
    despues = estado_dataset()
    escrituras = despues != antes
    nombra = "guarda 5, la lectura de la excepcion de la ficha: ROJO" in salida
    aborta = "SE ABORTA SIN ESCRIBIR NADA" in salida
    ok_a = codigo != 0 and not escrituras and nombra and aborta
    print("(A) FORMULA ROTA (sin la marca de cierre) Y GIRO CON --ejecutar:")
    print("     codigo de salida: %r (distinto de cero: %s)" % (codigo, codigo != 0))
    print("     git status -- dataset/ cambia: %s (CERO ESCRITURAS: %s)"
          % (escrituras, not escrituras))
    print("     la guarda 5 NOMBRA el fallo del parser: %s" % nombra)
    print("     la salida dice que aborta sin escribir: %s" % aborta)
    for ln in guardas_de(salida):
        print("     %s" % ln)
    print("     VEREDICTO: %s" % ("OK" if ok_a else "ROJO"))
    resultados.append(("(A) formula rota, el giro CAE y no escribe", ok_a))
    print("")

    # ---- (B) EL CONTRASTE CON EL CODIGO VIEJO ------------------------------
    op_roto = ops_rotas[idx_ficha]
    conj_viejo, _, _ = T.pares_exceptuados_de(op_roto, resolver, [])  # los fallos, tirados
    exceptuado_viejo = frozenset((rd, rh)) in conj_viejo
    fallos_hoy = []
    T.pares_exceptuados_de(op_roto, resolver, fallos_hoy)
    ok_b = (not exceptuado_viejo) and len(conj_viejo) == 0 and len(fallos_hoy) > 0
    print("(B) CONTRASTE CON EL CODIGO VIEJO, sobre la MISMA ficha rota:")
    print("     con los fallos TIRADOS (como hasta la 143): %d pares, el par exceptuado: %s"
          % (len(conj_viejo), exceptuado_viejo))
    print("     o sea que la guarda 5 VIEJA habria dicho OK y el giro habria seguido a BORRAR")
    print("     con los fallos RECOGIDOS (hoy): %d fallo(s) que abortan" % len(fallos_hoy))
    print("     VEREDICTO: %s" % ("OK" if ok_b else "ROJO"))
    resultados.append(("(B) el codigo viejo habria dicho OK", ok_b))
    print("")

    # ---- (C) LA CONTRAPRUEBA ----------------------------------------------
    antes_c = estado_dataset()
    codigo_c, salida_c = correr_giro(argv_base + ["--ejecutar"], ops, grafo)
    despues_c = estado_dataset()
    escrituras_c = despues_c != antes_c
    sin_fallo_parser = "la lectura de la excepcion de la ficha: ROJO" not in salida_c
    por_exceptuado = "SI esta en la excepcion" in salida_c
    ok_c = (not escrituras_c) and sin_fallo_parser and por_exceptuado and codigo_c != 0
    print("(C) CONTRAPRUEBA, formula ENTERA sobre el mismo grafo simulado:")
    print("     codigo de salida: %r" % codigo_c)
    print("     git status -- dataset/ cambia: %s (CERO ESCRITURAS: %s)"
          % (escrituras_c, not escrituras_c))
    print("     la guarda 5 NO cae por fallo de parser: %s" % sin_fallo_parser)
    print("     cae por el motivo BUENO (el par esta exceptuado): %s" % por_exceptuado)
    for ln in guardas_de(salida_c):
        print("     %s" % ln)
    print("     VEREDICTO: %s" % ("OK" if ok_c else "ROJO"))
    resultados.append(("(C) contraprueba, formula entera", ok_c))
    print("")

    print("=" * 78)
    buenas = sum(1 for _, ok in resultados if ok)
    for nombre, ok in resultados:
        print("  %-46s %s" % (nombre, "OK" if ok else "ROJO"))
    final = estado_dataset()
    print("")
    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LA LINEA VIEJA, TACHADA:
    #     ~~print("ESTADO FINAL DE dataset/: %d fila(s) en git status, identico al de la apertura "~~
    #     ~~      "del arnes: %s" % (len(final.splitlines()), final == antes))~~
    # La huella no devuelve filas de git status, devuelve (sha256, conteo).
    _, _p16_linea = _HC.comparar(antes, final, *_P16_RUTAS)
    print("ESTADO FINAL DE dataset/: %d fichero(s) bajo la huella, identico al de la "
          "apertura del arnes: %s" % (final[1], final == antes))
    print("   %s" % _p16_linea)
    print("")
    print("COMPROBACIONES QUE MUERDEN: %d de %d" % (buenas, len(resultados)))
    return 0 if buenas == len(resultados) and final == antes else 1


if __name__ == "__main__":
    raise SystemExit(main())
