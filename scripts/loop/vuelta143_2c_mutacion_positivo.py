# -*- coding: utf-8 -*-
r"""vuelta143_2c_mutacion_positivo.py . LA PRUEBA DE MUTACION DE LA TAREA 2.c de
la vuelta 143 (acta de la vuelta 142, adjudicacion 3.1 y caida 4.5 de la casa).

LO QUE EL ENCARGO PIDE, LITERAL: "mueve una de las dos divergentes al saco de
cumplidas en memoria y comprueba que la expectativa vuelve a fallar
nombrandola."

TODO EN MEMORIA Y SOBRE EL SUJETO CONGELADO (el commit 62d4f28e, con sus cuatro
blobs cotejados por sha256 por el propio instrumento). Ni el disco ni el
instrumento real se tocan: se importa su funcion `evaluar()` y se le pasan las
filas y la cifra mutadas.

UNA COSA QUE SE DECLARA, PORQUE SE MIDIO Y NO SE ADIVINO: la comprobacion (A) de
la expectativa nueva (la union de los tres sacos igual al catalogo menos las
remitidas) ES CIEGA A ESTA MUTACION, y tenia que serlo: mover una divergente al
saco de cumplidas la saca de un sumando y la mete en otro, y LA UNION NO SE
MUEVE. Por eso la expectativa nueva no es solo (A). La que muerde es la (B),
"ninguna divergente sale cumplida", con el saco de divergentes computado de la
FICHA y del GRAFO y no de la razon de la vara. Este arnes lo prueba de las dos
maneras: comprueba que la (A) sigue verde con la mutacion puesta (o sea que la
mutacion es real y aun asi (A) no la ve) y que el veredicto entero CAE por la
(B) nombrando la operacion.

CUATRO CASOS, todos sobre cifra computada y nunca contra un literal:

  (a) CONTRAPRUEBA SIN MUTAR: el caso positivo CALZA (codigo 0).
  (b) MUTACION: se elige POR COMPUTO la primera divergente, se le pone
      cumplido=True en su fila y se la saca del saco de divergentes de la
      cifra, exactamente como haria una vara que la llamara cumplida. El
      veredicto tiene que CAER (codigo distinto de 0).
  (c) LA CAIDA NOMBRA LA OPERACION MUTADA en el texto del fallo.
  (d) LA UNION SIGUE SIENDO LA MISMA con la mutacion puesta, que es la medicion
      que sostiene lo declarado arriba sobre la ceguera de la (A).

USO:
  python scripts/loop/vuelta143_2c_mutacion_positivo.py

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

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import tallar_estado_de_fase as T
import vuelta141_2e_caso_positivo_fase03 as C


class Captura(object):
    """Recoge lo que evaluar() imprime, para poder cotejar el texto del fallo."""

    def __init__(self):
        self.buf = io.StringIO()
        self.viejo = None

    def __enter__(self):
        self.viejo = sys.stdout
        sys.stdout = self.buf
        return self

    def __exit__(self, *a):
        sys.stdout = self.viejo
        return False

    @property
    def texto(self):
        return self.buf.getvalue()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    resultados = []

    # --- REMEDIO DEL CHECK DE P.16 (vuelta 160, TAREA 3.a; adjudicacion 6.7 del
    # acta 158 y 6.1 del acta 159). La huella NO MIRA A GIT: compara el disco contra
    # el disco, y por eso ni el estado de fin de linea ni la suciedad anterior al
    # arranque pueden moverla. Ver scripts/loop/huella_de_contenido.py ---
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import huella_de_contenido as _HC  # noqa: E402
    _P16_RUTAS = ("dataset/", "docs/plan/")
    _p16_antes = _HC.huella(*_P16_RUTAS)

    print("=" * 78)
    print("MUTACION DE LA TAREA 2.c | vuelta 143")
    print("Sujeto congelado: %s | fase %s" % (C.COMMIT_CONGELADO, C.FASE))
    print("Todo EN MEMORIA. La divergente que se mueve se ELIGE POR COMPUTO.")
    print("=" * 78)

    ops = T.cargar_ops(C.COMMIT_CONGELADO)
    nodos = T.cargar_grafo(C.COMMIT_CONGELADO)
    lista, cifra, _fallos = T.medir(C.FASE, ops, nodos, ref=C.COMMIT_CONGELADO)
    remitidas = sorted(x for x in T.leer_remisiones(C.FASE_DESTINO_DE_LA_REMISION,
                                                    C.COMMIT_CONGELADO)
                       if x in {f["id_op"] for f in lista})

    # ---------------- (a) CONTRAPRUEBA SIN MUTAR ---------------------------
    with Captura() as cap0:
        calza0, codigo0 = C.evaluar(lista, cifra, ops, nodos, remitidas)
    ok = (calza0 is True) and (codigo0 == 0)
    resultados.append(("a CONTRAPRUEBA sin mutar: el caso positivo CALZA (codigo 0)", ok))
    print("")
    print("(a) sin mutar -> calza=%s codigo=%s" % (calza0, codigo0))
    print("    divergentes que la vara publica: %s" % ", ".join(cifra["nombres_divergentes"]))

    # ---------------- LA MUTACION: una divergente pasa a cumplida ----------
    divergentes = list(cifra["nombres_divergentes"])
    if not divergentes:
        print("")
        print("OMITIDO POR FALTA DE SUJETO: el corte congelado no trae ninguna divergente, "
              "asi que no hay nada que mover. ESO ES ROJO, no verde.")
        return 1
    sujeto = sorted(divergentes)[0]
    lista_m = copy.deepcopy(lista)
    cifra_m = copy.deepcopy(cifra)
    for f in lista_m:
        if f["id_op"] == sujeto:
            f["cumplido"] = True
            f["razon"] = "MUTACION DE LA VUELTA 143: la vara la llama cumplida"
    cifra_m["nombres_divergentes"] = [x for x in cifra_m["nombres_divergentes"] if x != sujeto]
    cifra_m["divergentes"] = len(cifra_m["nombres_divergentes"])
    cifra_m["nombres_sin_cumplir"] = [x for x in cifra_m["nombres_sin_cumplir"] if x != sujeto]
    cifra_m["sin_cumplir"] = len(cifra_m["nombres_sin_cumplir"])
    cifra_m["cumplido"] = cifra_m["cumplido"] + 1

    with Captura() as cap1:
        calza1, codigo1 = C.evaluar(lista_m, cifra_m, ops, nodos, remitidas)
    texto1 = cap1.texto

    # ---------------- (b) EL VEREDICTO CAE ---------------------------------
    ok = (calza1 is False) and (codigo1 != 0)
    resultados.append(("b movida %s al saco de cumplidas, la expectativa CAE" % sujeto, ok))
    print("")
    print("(b) mutada %s -> calza=%s codigo=%s" % (sujeto, calza1, codigo1))

    # ---------------- (c) LA CAIDA LA NOMBRA -------------------------------
    lineas_fallo = [ln.strip() for ln in texto1.splitlines()
                    if ln.startswith("   (") and sujeto in ln]
    ok = bool(lineas_fallo) and any("(B)" in ln for ln in lineas_fallo)
    resultados.append(("c la caida NOMBRA a %s y lo hace por la comprobacion (B)" % sujeto, ok))
    print("")
    print("(c) lineas de fallo que la nombran:")
    for ln in lineas_fallo:
        print("    %s" % ln)

    # ---------------- (d) LA UNION NO SE MUEVE -----------------------------
    def union_de(l, c):
        return ({f["id_op"] for f in l if f["cumplido"] is True}
                | set(c["nombres_divergentes"]) | set(c["nombres_sin_vara"]))
    u0, u1 = union_de(lista, cifra), union_de(lista_m, cifra_m)
    ok = (u0 == u1) and ("(A)" not in " ".join(lineas_fallo))
    resultados.append(("d la UNION de los tres sacos NO se mueve con la mutacion, o sea que "
                       "la comprobacion (A) sola es ciega a esto y la que muerde es la (B)", ok))
    print("")
    print("(d) union sin mutar %d nombres | union mutada %d nombres | iguales: %s"
          % (len(u0), len(u1), u0 == u1))

    # ---------------- P.16 --------------------------------------------------
    sucio = subprocess.run(["git", "status", "--porcelain", "--", "dataset/", "docs/plan/"],
                           cwd=T.RAIZ, capture_output=True, text=True).stdout.strip()
    # CORRECCION DECLARADA (vuelta 160, TAREA 3.a). LA LINEA VIEJA QUEDA AQUI,
    # TACHADA Y LEGIBLE:
    #     ~~resultados.append(("P.16 dataset/ y docs/plan/ SIN TOCAR tras la mutacion", sucio == ""))~~
    #     ~~print("git status --porcelain -- dataset/ docs/plan/ : %r" % sucio)~~
    # EL VEREDICTO PASA A LA HUELLA DE CONTENIDO. git status queda como INFORME.
    _p16_despues = _HC.huella(*_P16_RUTAS)
    _p16_ok, _p16_linea = _HC.comparar(_p16_antes, _p16_despues, *_P16_RUTAS)
    resultados.append(("P.16 dataset/ y docs/plan/ SIN TOCAR tras la mutacion", _p16_ok))
    print("")
    print(_p16_linea)
    print("git status --porcelain -- dataset/ docs/plan/ (INFORME, no vara) : %r" % sucio)

    print("")
    print("=" * 78)
    verdes = 0
    for nombre, ok in resultados:
        print("  %-5s %s" % ("VERDE" if ok else "ROJO", nombre))
        verdes += 1 if ok else 0
    print("CIFRA de la bateria 2.c: %d comprobaciones" % len(resultados))
    print("CIFRA verdes de la bateria 2.c: %d comprobaciones" % verdes)
    print("=" * 78)
    if verdes != len(resultados):
        print("ROJO: %d de %d casos no se comportan." % (len(resultados) - verdes, len(resultados)))
        return 1
    print("VERDE: los %d casos se comportan." % len(resultados))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
