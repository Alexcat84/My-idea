# -*- coding: utf-8 -*-
r"""vuelta147_3e_simular_a26.py . SIMULACION PREVIA Y PRUEBA DE MUTACION DE LA
PUERTA SEMANTICA A2.6 (TAREA 3.e de la vuelta 147).

TODO SOBRE COPIA EN MEMORIA, ANTES DE CABLEAR NADA Y SIN ESCRIBIR UN BYTE EN
`dataset/`. El propio arnes comprueba `git status --porcelain -- dataset/` a los
DOS lados y compara las dos salidas.

EL SUJETO DE PRUEBA SE ELIGE POR COMPUTO Y NUNCA SE TECLEA: se busca en el
indice semantico real LA PAREJA DE NODOS VIVOS DEL MISMO DOMINIO CON EL COSENO
MAS ALTO por encima del umbral, y el NODO DE PRUEBA se fabrica CLONANDO a uno de
los dos con un `node_id` nuevo y su MISMO VECTOR. Un clon con el mismo vector
tiene coseno 1,0 contra su original, o sea que **se parece por encima del umbral
por construccion y medido, no por suposicion**.

LOS CASOS:

  (A) CASO ROJO, EL QUE MANDA, Y ES EL QUE LA FICHA PIDE LITERALMENTE (`OP-A-02`,
      verificacion 5): *"un nodo de prueba que se parezca a uno existente por
      encima del umbral NO entra sin veredicto: la prueba se cae si entra"*. El
      clon SIN veredicto tiene que salir BLOQUEADO, y el bloqueo tiene que
      NOMBRAR AL VECINO.

  (B) CASO POSITIVO. El MISMO clon CON el veredicto escrito citando el id del
      vecino tiene que ENTRAR. Sin este caso, (A) solo probaria que la puerta
      sabe decir que no, y una puerta que no deja pasar a nadie no es una
      aduana: es un muro.

  (C) LA MUTACION SOBRE VARIABLE COMPUTADA (`EJECUTOR.md` 1, "el caso rojo se
      prueba por mutacion", y NUNCA sobre un literal). Se toma el veredicto que
      hace pasar el caso (B) y se le cambia EL ID DEL VECINO por otro id VIVO
      elegido por computo: el veredicto sigue existiendo, sigue siendo valido y
      sigue citando UN id, pero **no el que hace falta**. Tiene que volver a
      BLOQUEAR. Esto prueba que la puerta exige que el veredicto CITE EL ID DEL
      VECINO y no que exista un veredicto cualquiera.

  (D) BAJAR EL UMBRAL NO ES UNA SALIDA. La ficha lo dice con todas sus letras.
      Se comprueba MECANICAMENTE que `evaluar` no acepta ningun umbral por
      parametro: se le pasa uno y tiene que reventar. Una puerta con una palanca
      para abrirla no es una puerta.

  (E) UN NODO SIN VECTOR BLOQUEA DICIENDOLO, jamas pasa en silencio (banco 9).

  (F) UN NODO QUE NO SE PARECE A NADIE ENTRA SIN VEREDICTO. Es la otra mitad de
      "nunca bloquea por parecido": si no hay vecino sobre el umbral, no hay
      nada que juzgar y la aduana no estorba. El sujeto se elige por computo:
      un vector ORTOGONAL construido a partir del propio indice.

USO:
  python scripts/loop/vuelta147_3e_simular_a26.py

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
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from aduana_semantica import (  # noqa: E402
    cargar_grafo,
    cargar_indice,
    evaluar,
    umbrales,
)


def estado_dataset():
    r = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"], cwd=RAIZ,
                       capture_output=True, text=True)
    return r.stdout


def pareja_mas_parecida(grafo, indice, umbral_sem):
    """LA PAREJA REAL DE MAYOR COSENO DENTRO DE UN MISMO DOMINIO, computada del
    indice. Devuelve (a, b, coseno)."""
    import numpy as np
    pos = dict((n, i) for i, n in enumerate(indice["ids"]))
    E = np.array(indice["embeddings"], dtype=np.float32)
    E = E / np.linalg.norm(E, axis=1, keepdims=True)
    vivos = [n for n, d in grafo.items() if not d.get("deprecado") and n in pos]
    por_dom = {}
    for n in vivos:
        por_dom.setdefault(grafo[n].get("dominio") or "core", []).append(n)
    mejor = (None, None, -1.0)
    for _dom, ids in por_dom.items():
        if len(ids) < 2:
            continue
        ids = sorted(ids)
        V = E[[pos[i] for i in ids]]
        S = V @ V.T
        np.fill_diagonal(S, -1.0)
        i, j = np.unravel_index(int(np.argmax(S)), S.shape)
        if float(S[i, j]) > mejor[2]:
            mejor = (ids[i], ids[j], float(S[i, j]))
    return mejor


def main():
    antes = estado_dataset()
    import numpy as np

    umbral_sem, umbral_tit = umbrales()
    grafo = cargar_grafo()
    indice = cargar_indice()

    a, b, cos = pareja_mas_parecida(grafo, indice, umbral_sem)
    if a is None or cos < umbral_sem:
        print("ROJO PREVIO: no hay ninguna pareja viva del mismo dominio por encima del "
              "umbral %.2f, el arnes no puede fabricar un caso que se parezca de verdad"
              % umbral_sem)
        return 2

    # EL NODO DE PRUEBA: clon de `a` con id nuevo y SU MISMO VECTOR. Coseno 1,0
    # contra `a` por construccion, medido mas abajo y no supuesto.
    nuevo_id = "nodo_de_prueba_aduana_%s" % a
    candidato = copy.deepcopy(grafo[a])
    candidato["node_id"] = nuevo_id
    candidato["id"] = nuevo_id

    g2 = dict(grafo)
    g2[nuevo_id] = candidato
    i2 = {"ids": list(indice["ids"]) + [nuevo_id],
          "embeddings": list(indice["embeddings"])
          + [indice["embeddings"][indice["ids"].index(a)]]}

    casos = []

    permitido, bloqueos, vecinos = evaluar(candidato, g2, i2, [])
    nombra = any(a in x for x in bloqueos)
    casos.append(("A el clon SIN veredicto NO entra, y el bloqueo nombra al vecino",
                  permitido is False and nombra and len(vecinos) > 0,
                  "%d vecino(s) sobre el umbral; %s" % (len(vecinos),
                                                        (bloqueos[0][:130] if bloqueos else "(sin bloqueo)"))))

    ver_bueno = [{"nodo": nuevo_id, "vecino": v[0], "veredicto": "continua",
                  "por_que": "simulacion de la vuelta 147"} for v in vecinos]
    permitido, bloqueos, _ = evaluar(candidato, g2, i2, ver_bueno)
    casos.append(("B el MISMO clon CON veredicto citando cada vecino SI entra",
                  permitido is True and not bloqueos,
                  "%d veredicto(s) escritos, cero bloqueos" % len(ver_bueno)))

    # LA MUTACION: se cambia EL ID DEL VECINO por otro id vivo elegido por
    # computo, no tecleado. El veredicto sigue existiendo y siendo valido.
    otros = sorted(n for n, d in grafo.items()
                   if not d.get("deprecado") and n not in [v[0] for v in vecinos] and n != a)
    suplantado = otros[len(otros) // 2]
    ver_mutado = copy.deepcopy(ver_bueno)
    for x in ver_mutado:
        x["vecino"] = suplantado
    permitido, bloqueos, _ = evaluar(candidato, g2, i2, ver_mutado)
    casos.append(("C veredicto que cita OTRO id (mutacion sobre variable computada): BLOQUEA",
                  permitido is False and bool(bloqueos),
                  "id suplantado por computo: %s" % suplantado))

    try:
        evaluar(candidato, g2, i2, [], umbral_semantico=0.99)
        acepta_palanca = True
    except TypeError:
        acepta_palanca = False
    casos.append(("D bajar el umbral no es una salida: evaluar() no acepta umbral por parametro",
                  acepta_palanca is False,
                  "TypeError al intentar pasarle un umbral" if not acepta_palanca
                  else "ACEPTA UNA PALANCA PARA ABRIR LA PUERTA"))

    sin_vector = copy.deepcopy(candidato)
    sin_vector["node_id"] = nuevo_id + "_sin_vector"
    sin_vector["id"] = sin_vector["node_id"]
    permitido, bloqueos, _ = evaluar(sin_vector, g2, i2, [])
    casos.append(("E un nodo SIN vector bloquea diciendolo, nunca pasa en silencio",
                  permitido is False and any("NO TIENE VECTOR" in x for x in bloqueos),
                  bloqueos[0][:130] if bloqueos else "(sin bloqueo)"))

    # UN VECTOR ORTOGONAL, CONSTRUIDO DEL PROPIO INDICE Y NO INVENTADO: se toma
    # el vector de `a`, se le resta su proyeccion sobre si mismo en una base
    # canonica desplazada, y se comprueba MIDIENDO que su coseno maximo contra
    # el vecindario queda por debajo del umbral.
    E = np.array(indice["embeddings"], dtype=np.float32)
    E = E / np.linalg.norm(E, axis=1, keepdims=True)
    media = E.mean(axis=0)
    v_orto = E[indice["ids"].index(a)] - media
    v_orto = v_orto - np.dot(v_orto, E[indice["ids"].index(a)]) * E[indice["ids"].index(a)]
    n = float(np.linalg.norm(v_orto))
    lejano_id = "nodo_de_prueba_aduana_lejano"
    lejano = {"node_id": lejano_id, "id": lejano_id,
              "dominio": grafo[a].get("dominio") or "core",
              "titulo_concepto": "Concepto sin parecido alguno para la simulacion 147"}
    g3 = dict(g2)
    g3[lejano_id] = lejano
    i3 = {"ids": list(i2["ids"]) + [lejano_id],
          "embeddings": list(i2["embeddings"]) + [(v_orto / n).tolist()]}
    permitido, bloqueos, vecinos_lejano = evaluar(lejano, g3, i3, [])
    casos.append(("F un nodo que no se parece a nadie entra SIN veredicto: nunca bloquea "
                  "por parecido",
                  permitido is True and not vecinos_lejano,
                  "%d vecinos sobre el umbral" % len(vecinos_lejano)))

    despues = estado_dataset()

    print("SIMULACION PREVIA Y MUTACION DE LA PUERTA SEMANTICA A2.6 (vuelta 147, TAREA 3.e)")
    print("")
    print("  UMBRALES IMPORTADOS DE scripts/intra_dominio.py, NO TECLEADOS:")
    print("      UMBRAL_SEMANTICO = %s | UMBRAL_TITULO = %s" % (umbral_sem, umbral_tit))
    print("  PAREJA REAL DE MAYOR COSENO EN SU DOMINIO, ELEGIDA POR COMPUTO:")
    print("      %s  con  %s   coseno %.4f" % (a, b, cos))
    print("  NODO DE PRUEBA: clon de %s con id %s y su MISMO vector" % (a, nuevo_id))
    print("")
    for rotulo, ok, detalle in casos:
        print("  %-88s %s" % (rotulo, "OK" if ok else "NO MORDIO"))
        print("      %s" % detalle)
    print("")
    print("  dataset/ ANTES  : %s" % (antes.strip() or "(sin cambios)"))
    print("  dataset/ DESPUES: %s" % (despues.strip() or "(sin cambios)"))
    print("  dataset/ IDENTICO ANTES Y DESPUES: %s" % ("SI" if antes == despues else "NO"))
    muerden = sum(1 for _, ok, _ in casos if ok)
    print("")
    print("CASOS QUE MUERDEN: %d de %d" % (muerden, len(casos)))
    print("CIFRA casos que muerden: %d casos" % muerden)
    print("CIFRA casos del arnes: %d casos" % len(casos))
    return 0 if (muerden == len(casos) and antes == despues) else 1


if __name__ == "__main__":
    raise SystemExit(main())
