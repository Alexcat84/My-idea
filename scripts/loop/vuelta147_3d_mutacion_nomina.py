# -*- coding: utf-8 -*-
r"""vuelta147_3d_mutacion_nomina.py . LA PRUEBA DE MUTACION DE LA GUARDA DE LA
NOMINA DE LA ADUANA (TAREA 3.d de la vuelta 147).

QUE PRUEBA. `verificar_nomina_sellada.py` es el discutible 5 del reporte de la
146 convertido en codigo: la nomina `dataset/metadata/aduana_fuente_multiple.json`
no puede moverse sin declararse en el reporte. Una guarda que no muerde no es
una guarda (banco 9) y un caso rojo que no puede fallar no es una prueba
(`EJECUTOR.md` 1, caida 2 de la vuelta 89).

TODAS LAS MUTACIONES VAN SOBRE VARIABLE COMPUTADA Y COPIA EN MEMORIA, NUNCA
SOBRE UN LITERAL Y NUNCA SOBRE DISCO. Los tres textos que la guarda mira (la
nomina de hoy, la de `HEAD` y el reporte) son parametros inyectables suyos: aqui
se leen de verdad, se copian, se mutan LA COPIA y se le pasan. `dataset/` NO SE
TOCA, y el propio arnes lo comprueba con `git status --porcelain -- dataset/` a
los DOS lados y compara las dos salidas.

EL NODO DE LA MUTACION SE ELIGE POR COMPUTO Y NUNCA SE TECLEA: se toma una
entrada de la nomina real por su POSICION (la del medio, calculada de la
longitud de la lista), asi que el arnes sigue valiendo si la nomina cambia.

LOS CINCO CASOS:

  (A) CASO VERDE, EL DE CONTRASTE. La nomina de hoy contra la de `HEAD`, tal
      como estan, sin mutar nada: no se movio, asi que VERDE. Sin este caso, los
      rojos de abajo solo probarian que la guarda sabe decir rojo.

  (B) UNA ENTRADA QUE SE VA, SIN DECLARAR. Se quita del texto de HOY la entrada
      elegida por computo y el reporte no la nombra: ROJO NOMBRANDOLA.

  (C) UNA ENTRADA QUE ENTRA, SIN DECLARAR. Se quita esa misma entrada del texto
      de HEAD (que es lo mismo que anadirla hoy, visto desde la guarda): ROJO
      NOMBRANDOLA.

  (D) EL ATAQUE DE VERDAD, QUE ES EL QUE MOTIVA LA GUARDA: UNA LISTA DE
      DECLARACIONES QUE CAMBIA EN SILENCIO. A la entrada elegida se le anade un
      segundo libro EN EL TEXTO DE HOY, que es exactamente lo que pasaria si
      alguien re-corriera el sellador tras meter un libro nuevo a un nodo ya
      adjudicado: ROJO NOMBRANDOLA.

  (E) LA CONTRAPRUEBA, Y ES LA QUE IMPIDE QUE LA GUARDA SEA UN MURO. La MISMA
      mutacion de (D), pero con un reporte que trae la marca de declaracion Y
      nombra el `node_id`: VERDE. La guarda no prohibe re-sellar; prohibe
      re-sellar callando.

Y UN SEXTO, QUE NO ES MUTACION SINO FRONTERA:

  (F) FALLA RUIDOSO. Con la nomina de `HEAD` ilegible, la guarda tiene que salir
      ROJO diciendolo, jamas VERDE por no haber podido mirar (banco 9).

USO:
  python scripts/loop/vuelta147_3d_mutacion_nomina.py

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
"""
import copy
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from verificar_nomina_sellada import (  # noqa: E402
    MARCA_DECLARACION,
    RUTA_NOMINA,
    nomina_de_head,
    verificar,
)


def estado_dataset():
    r = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"], cwd=RAIZ,
                       capture_output=True, text=True)
    return r.stdout


def main():
    antes = estado_dataset()

    texto_hoy = io.open(RUTA_NOMINA, encoding="utf-8").read()
    texto_head = nomina_de_head()
    if texto_head is None:
        print("ROJO PREVIO: no se pudo leer la nomina de HEAD, el arnes no puede probar nada")
        return 2

    d_hoy = json.loads(texto_hoy)
    d_head = json.loads(texto_head)
    filas = d_head.get("adjudicados", [])
    if len(filas) < 2:
        print("ROJO PREVIO: la nomina de HEAD trae %d entradas, hacen falta al menos 2"
              % len(filas))
        return 2

    # EL SUJETO SE ELIGE POR COMPUTO: la entrada del medio de la lista real.
    indice = len(filas) // 2
    elegido = filas[indice]["node_id"]

    def texto(d):
        return json.dumps(d, ensure_ascii=False, indent=2)

    sin_elegido_hoy = copy.deepcopy(d_hoy)
    sin_elegido_hoy["adjudicados"] = [x for x in sin_elegido_hoy["adjudicados"]
                                      if x["node_id"] != elegido]
    sin_elegido_head = copy.deepcopy(d_head)
    sin_elegido_head["adjudicados"] = [x for x in sin_elegido_head["adjudicados"]
                                       if x["node_id"] != elegido]
    con_libro_de_mas = copy.deepcopy(d_hoy)
    for x in con_libro_de_mas["adjudicados"]:
        if x["node_id"] == elegido:
            # El libro que se cuela sale de OTRA fila de la propia nomina, no de
            # un literal tecleado: computado, como manda EJECUTOR.md 1.
            otra = filas[(indice + 1) % len(filas)]["fuente"][0]
            x["fuente"] = list(x["fuente"]) + [otra]
    reporte_mudo = "Un reporte que no dice nada de la nomina."
    reporte_declarado = ("Un reporte que declara el %s y nombra a %s."
                         % (MARCA_DECLARACION, elegido))

    casos = []

    ok, fallos, det = verificar(texto_hoy, texto_head, reporte_mudo)
    casos.append(("A caso verde de contraste: la nomina no se movio", ok is True,
                  "entran %d, salen %d, cambian %d"
                  % (len(det.get("entran", [])), len(det.get("salen", [])),
                     len(det.get("cambian", [])))))

    ok, fallos, _ = verificar(texto(sin_elegido_hoy), texto_head, reporte_mudo)
    casos.append(("B una entrada que SALE sin declarar", ok is False
                  and any(elegido in f for f in fallos),
                  fallos[0][:150] if fallos else "(sin fallo)"))

    ok, fallos, _ = verificar(texto_hoy, texto(sin_elegido_head), reporte_mudo)
    casos.append(("C una entrada que ENTRA sin declarar", ok is False
                  and any(elegido in f for f in fallos),
                  fallos[0][:150] if fallos else "(sin fallo)"))

    ok, fallos, _ = verificar(texto(con_libro_de_mas), texto_head, reporte_mudo)
    casos.append(("D el ataque de verdad: un SEGUNDO LIBRO que se cuela en silencio",
                  ok is False and any(elegido in f for f in fallos),
                  fallos[0][:150] if fallos else "(sin fallo)"))

    ok, fallos, _ = verificar(texto(con_libro_de_mas), texto_head, reporte_declarado)
    casos.append(("E contraprueba: la MISMA mutacion, declarada en el reporte", ok is True,
                  "la guarda no prohibe re-sellar, prohibe re-sellar callando"))

    ok, fallos, _ = verificar(texto_hoy, "esto no es JSON", reporte_mudo)
    casos.append(("F falla ruidoso: la nomina de HEAD ilegible es ROJO, nunca verde",
                  ok is False and bool(fallos),
                  fallos[0][:150] if fallos else "(sin fallo)"))

    despues = estado_dataset()

    print("PRUEBA DE MUTACION DE LA GUARDA DE LA NOMINA (vuelta 147, TAREA 3.d)")
    print("")
    print("  NODO ELEGIDO POR COMPUTO (posicion %d de %d en la nomina de HEAD): %s"
          % (indice, len(filas), elegido))
    print("")
    for rotulo, ok_, detalle in casos:
        print("  %-70s %s" % (rotulo, "OK" if ok_ else "NO MORDIO"))
        print("      %s" % detalle)
    print("")
    print("  dataset/ ANTES  : %s" % (antes.strip() or "(sin cambios)"))
    print("  dataset/ DESPUES: %s" % (despues.strip() or "(sin cambios)"))
    print("  dataset/ IDENTICO ANTES Y DESPUES: %s" % ("SI" if antes == despues else "NO"))
    muerden = sum(1 for _, ok_, _ in casos if ok_)
    print("")
    print("CASOS QUE MUERDEN: %d de %d" % (muerden, len(casos)))
    print("CIFRA casos que muerden: %d casos" % muerden)
    print("CIFRA casos del arnes: %d casos" % len(casos))
    return 0 if (muerden == len(casos) and antes == despues) else 1


if __name__ == "__main__":
    raise SystemExit(main())
