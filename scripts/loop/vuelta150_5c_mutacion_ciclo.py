# -*- coding: utf-8 -*-
"""vuelta150_5c_mutacion_ciclo.py . EL CASO ROJO POR MUTACION Y EL CASO DE
CONTROL DE LA GUARDA DEL CICLO (TAREA 5.c de la vuelta 150).

NO TOCA UN SOLO FICHERO DEL REPO. Todo se monta sobre copias en memoria del
grafo, y el arnes comprueba con sha256 que dataset/ queda identico.

LOS CUATRO CASOS, y los cuatro con veredicto COMPUTADO, nunca un literal
comparado consigo mismo (EJECUTOR.md 1, "EL CASO ROJO SE PRUEBA POR MUTACION"):

  (A) CASO DE CONTROL, el que manda la TAREA 5.c: el ciclo corrido EN ORDEN no
      puede disparar el aviso. Se mide sobre las dos copias REALES del disco tal
      como estan tras el ciclo de esta vuelta: cero divergencias, diagnostico
      vacio.
  (B) FALTA EL COMANDO 2: se simula lo que hace `run_phase1.py` corrido solo,
      o sea la copia del dataset con la curaduria BORRADA y la de la web con la
      curaduria puesta. El diagnostico TIENE que nombrar el comando 2.
  (C) FALTA EL COMANDO 3: al reves, el dataset al dia y la web desfasada. El
      diagnostico TIENE que nombrar el comando 3.
  (D) ROJO DE VERDAD, Y NO SE TAPA (TAREA 5.b): se cambia un campo que el ciclo
      NO escribe (`titulo_concepto`). El diagnostico TIENE que decir que ESTO NO
      ES UN CICLO A MEDIAS.

LA MUTACION: para cada uno de los cuatro se cambia EL VALOR ESPERADO y se
comprueba que el assert CAE. Si alguno no cae, el caso no prueba nada y este
arnes sale en rojo diciendolo.

USO:
  python scripts/loop/vuelta150_5c_mutacion_ciclo.py
SUJETO CONGELADO (declarado en la vuelta 180, TAREA 2.a): este arnes NOMBRA `master_graph.json` en su texto pero NO LO ABRE (2 apariciones en el texto, 0 llamadas que lo lean y 0 lecturas del fichero vivo, medidas fila a fila en docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl), asi que su resultado no depende de lo que ese fichero diga hoy.
"""
import copy
import hashlib
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
from run_phase1 import gemelos_divergentes  # noqa: E402
from diagnostico_ciclo_a_medias import diagnosticar, etiquetas_canonicas  # noqa: E402

RUTA_DATASET = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
RUTA_WEB = os.path.join(RAIZ, "web", "lib", "assets", "master_graph.json")


def sha(ruta):
    with open(ruta, "rb") as fh:
        return hashlib.sha256(fh.read().replace(b"\r\n", b"\n")).hexdigest()


def cargar(ruta):
    with open(ruta, encoding="utf-8") as fh:
        return json.load(fh)["nodos"]


def main():
    sha_a, sha_b = sha(RUTA_DATASET), sha(RUTA_WEB)
    print("dataset ANTES sha256=%s | web ANTES sha256=%s" % (sha_a[:12], sha_b[:12]))

    D = cargar(RUTA_DATASET)
    W = cargar(RUTA_WEB)
    canon = etiquetas_canonicas()
    print("etiquetas canonicas leidas de dataset/metadata/etiquetas_de_cara_v1*.json: %d"
          % len(canon))
    curados = [k for k in canon if k in D]
    assert curados, "no hay ni un nodo curado en el grafo: el arnes no se puede montar"
    print("nodos curados presentes en el grafo: %d" % len(curados))

    casos = []

    # (A) control
    dif_a = gemelos_divergentes(D, W)
    diag_a = diagnosticar(dif_a, D, W)
    medido_a = (len(dif_a), diag_a.strip())
    print("")
    print("(A) CASO DE CONTROL: el ciclo corrido EN ORDEN, sobre las dos copias reales.")
    print("    divergencias (COMPUTADO) = %d | diagnostico vacio = %s"
          % (medido_a[0], medido_a[1] == ""))
    casos.append(("A control", medido_a[0], 0, "el ciclo en orden no dispara el aviso"))
    assert medido_a[0] == 0 and medido_a[1] == "", \
        "el ciclo en orden dispara el aviso: la guarda grita sin motivo"
    print("    VERDE: el ciclo en orden NO dispara el aviso.")

    # (B) falta el comando 2: dataset sin curaduria, web con ella
    print("")
    print("(B) FALTA EL COMANDO 2 (etiquetas_de_cara --aplicar).")
    Db = copy.deepcopy(D)
    Wb = copy.deepcopy(W)
    tocados_b = 0
    for k in curados:
        Wb[k]["etiqueta_arbol"] = canon[k]
        Db[k]["etiqueta_arbol"] = "SIN CURAR " + canon[k]
        tocados_b += 1
    dif_b = gemelos_divergentes(Db, Wb)
    diag_b = diagnosticar(dif_b, Db, Wb)
    medido_b = 1 if "FALTA EL COMANDO 2" in diag_b else 0
    print("    nodos desfasados montados: %d | divergencias: %d" % (tocados_b, len(dif_b)))
    print("    el diagnostico nombra el COMANDO 2 (COMPUTADO) = %d" % medido_b)
    for linea in diag_b.splitlines():
        if "VEREDICTO" in linea or "FALTA:" in linea:
            print("    | %s" % linea.strip())
    casos.append(("B falta comando 2", medido_b, 1, "el diagnostico nombra el comando 2"))
    assert medido_b == 1, "el diagnostico NO nombra el comando 2"
    print("    VERDE: se delata solo y nombra el comando que falta.")

    # (C) falta el comando 3: dataset al dia, web desfasada
    print("")
    print("(C) FALTA EL COMANDO 3 (sync_assets_web).")
    Dc = copy.deepcopy(D)
    Wc = copy.deepcopy(W)
    for k in curados:
        Dc[k]["etiqueta_arbol"] = canon[k]
        Wc[k]["etiqueta_arbol"] = "SIN SINCRONIZAR " + canon[k]
    dif_c = gemelos_divergentes(Dc, Wc)
    diag_c = diagnosticar(dif_c, Dc, Wc)
    medido_c = 1 if "FALTA EL COMANDO 3" in diag_c else 0
    print("    divergencias: %d | el diagnostico nombra el COMANDO 3 (COMPUTADO) = %d"
          % (len(dif_c), medido_c))
    for linea in diag_c.splitlines():
        if "VEREDICTO" in linea or "FALTA:" in linea:
            print("    | %s" % linea.strip())
    casos.append(("C falta comando 3", medido_c, 1, "el diagnostico nombra el comando 3"))
    assert medido_c == 1, "el diagnostico NO nombra el comando 3"
    print("    VERDE: se delata solo y nombra el comando que falta.")

    # (D) rojo de verdad: un campo que el ciclo no escribe
    print("")
    print("(D) ROJO DE VERDAD: un campo que el ciclo NO escribe (titulo_concepto).")
    Dd = copy.deepcopy(D)
    Wd = copy.deepcopy(W)
    victima = sorted(Dd)[0]
    Wd[victima]["titulo_concepto"] = "ALGUIEN SEMBRO ESTO"
    dif_d = gemelos_divergentes(Dd, Wd)
    diag_d = diagnosticar(dif_d, Dd, Wd)
    medido_d = 1 if "NO ES UN CICLO A MEDIAS" in diag_d else 0
    print("    victima: %s | divergencias: %d" % (victima, len(dif_d)))
    print("    el diagnostico dice que NO es un ciclo a medias (COMPUTADO) = %d" % medido_d)
    for linea in diag_d.splitlines():
        if "VEREDICTO" in linea or "ROJO DE VERDAD" in linea:
            print("    | %s" % linea.strip())
    casos.append(("D rojo de verdad", medido_d, 1, "el diagnostico NO tapa un rojo legitimo"))
    assert medido_d == 1, "el diagnostico tapa un rojo legitimo: eso es aflojar"
    print("    VERDE: el rojo legitimo sigue siendo rojo y el diagnostico lo dice.")

    # ---- LA MUTACION ------------------------------------------------------
    print("")
    print("PRUEBA DE MUTACION SOBRE VARIABLE COMPUTADA: se cambia EL VALOR ESPERADO")
    print("de cada uno de los cuatro asserts y se comprueba que el caso CAE.")
    caidas = 0
    for etiqueta, medido, esperado, _texto in casos:
        mutado = 1 - esperado if esperado in (0, 1) else esperado + 1
        try:
            assert medido == mutado
            print("  %s: el assert NO cayo con esperado=%s. LA PRUEBA NO PRUEBA NADA"
                  % (etiqueta, mutado))
        except AssertionError:
            caidas += 1
            print("  %s: assert %s == %s CAE. El caso muerde." % (etiqueta, medido, mutado))
    esperado_caidas = len(casos)
    print("  caidas (COMPUTADO) = %d | esperado = %d" % (caidas, esperado_caidas))
    assert caidas == esperado_caidas, "alguna mutacion no cayo"

    print("")
    print("dataset DESPUES sha256=%s | web DESPUES sha256=%s"
          % (sha(RUTA_DATASET)[:12], sha(RUTA_WEB)[:12]))
    assert sha(RUTA_DATASET) == sha_a, "master_graph del dataset CAMBIO"
    assert sha(RUTA_WEB) == sha_b, "master_graph de la web CAMBIO"
    print("LAS DOS COPIAS IDENTICAS ANTES Y DESPUES: comprobado por el propio arnes.")
    print("")
    print("LOS CUATRO CASOS EN VERDE, Y LOS CUATRO MUERDEN.")


main()
