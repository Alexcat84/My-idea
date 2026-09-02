# -*- coding: utf-8 -*-
"""vuelta148_1a_mutacion_embebido.py . ARNES DE LA TAREA 1.a de la vuelta 148:
EL PASO DE EMBEBIDO PREVIO DEL CANDIDATO en scripts/integrar_packs.py.

QUE SE PRUEBA Y QUE NO, DICHO DELANTE Y NO AL FINAL.

  SE PRUEBA, SIN RED Y SIN GASTAR CREDENCIAL:
    (1) que invocado SIN la clave falla RUIDOSAMENTE nombrando la variable que
        falta (VOYAGE_API_KEY) y el fichero donde vive (el .env de la raiz), y
        que NO llama a Voyage ni una vez antes de rendirse;
    (2) que con la clave puesta el mismo camino deja de fallar y pide los
        vectores (LA MUTACION: lo unico que cambia entre (1) y (2) es el VALOR
        DE UNA VARIABLE QUE EL CODIGO COMPUTA, `credencial_ausente(clave)`, no
        un literal comparado consigo mismo);
    (3) que el vector inyectado ROMPE DE VERDAD la dependencia circular que la
        vuelta 147 midio: el mismo candidato que la aduana bloquea por "NO
        TIENE VECTOR" deja de bloquearse por ese motivo cuando el paso
        a-previo le pone el suyo, y todo ocurre en memoria;
    (4) que un vector de dimension ajena y un id que ya estaba en el indice
        caen los dos, en vez de mezclarse en silencio;
    (5) que dataset/ queda IDENTICO antes y despues, medido por este arnes.

  NO SE PRUEBA AQUI, Y SE DECLARA EN VEZ DE DARLO POR BUENO: que la llamada
  REAL a Voyage devuelve un vector util para este candidato. Requiere la
  credencial VOYAGE_API_KEY, que vive en el .env de la raiz, FUERA del repo
  mientras el bucle corre (regla del fundador, seccion 4 de AUDITOR.md). El
  bucle no puede salir a la red ni gastar credencial, asi que esa mitad se
  verifica en la sesion con humano presente que corra --ejecutar, y aqui
  queda dicha como NO PROBADA.

USO:
  python scripts/loop/vuelta148_1a_mutacion_embebido.py
"""
import hashlib
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import integrar_packs as IP
import build_semantic_index_voyage as VOYAGE
import aduana_semantica as AD

PACK_DE_MUESTRA = "quality"


def huella_de_dataset():
    """sha256 del arbol dataset/ entero (ruta + bytes de cada fichero, en orden
    estable). Si el paso a-previo escribiera un solo byte ahi, esto cambia."""
    h = hashlib.sha256()
    base = os.path.join(RAIZ, "dataset")
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames.sort()
        for nombre in sorted(filenames):
            ruta = os.path.join(dirpath, nombre)
            rel = os.path.relpath(ruta, RAIZ).replace(os.sep, "/")
            h.update(rel.encode("utf-8"))
            with open(ruta, "rb") as f:
                h.update(f.read())
    return h.hexdigest()


class VoyageFalso(object):
    """Doble del modulo del indice. NO SALE A LA RED: si alguien llama a
    embeber_textos cuando no debia, lo registra y lo canta."""

    def __init__(self, clave):
        self.clave = clave
        self.llamadas = 0
        self.textos_vistos = []
        self.VOYAGE_MODEL = VOYAGE.VOYAGE_MODEL
        self.OUTPUT_DIMENSION = VOYAGE.OUTPUT_DIMENSION
        self.BATCH_SIZE = VOYAGE.BATCH_SIZE
        self.texto_nodo = VOYAGE.texto_nodo

    def credencial_ausente(self):
        # EL VEREDICTO SE COMPUTA con la funcion real sobre la clave de esta
        # instancia. No es un literal: es la misma funcion que corre en vivo.
        return VOYAGE.credencial_ausente(self.clave, os.path.join(RAIZ, ".env"))

    def embeber_textos(self, textos, input_type):
        self.llamadas += 1
        self.textos_vistos.extend(textos)
        vectores = []
        for i, t in enumerate(textos):
            semilla = hashlib.sha256(t.encode("utf-8")).digest()
            vectores.append([((semilla[j % len(semilla)] + i) % 251) / 251.0
                             for j in range(self.OUTPUT_DIMENSION)])
        return vectores, {"total_tokens": 0}


def capturar_fallo(fn, *a, **kw):
    """Corre algo que puede llamar a IP.fallar (que hace sys.exit(1)) y
    devuelve (salio, texto_impreso)."""
    buf = io.StringIO()
    viejo = sys.stdout
    sys.stdout = buf
    try:
        fn(*a, **kw)
        salio = False
    except SystemExit:
        salio = True
    finally:
        sys.stdout = viejo
    return salio, buf.getvalue()


def main():
    fallos = []
    huella_antes = huella_de_dataset()
    print("HUELLA DE dataset/ ANTES: %s" % huella_antes)

    packs = [PACK_DE_MUESTRA]
    ids, textos = IP.ids_y_textos_de_candidatos(packs)
    print("SUJETO: pack '%s', %d nodo(s) reales leidos de packs/%s/nodos/"
          % (PACK_DE_MUESTRA, len(ids), PACK_DE_MUESTRA))

    # LA VARIABLE COMPUTADA sobre la que se muta: la clave real del entorno.
    clave_real = VOYAGE.VOYAGE_API_KEY
    print("CLAVE REAL EN ESTA SESION: %s (len=%d)"
          % ("PRESENTE" if clave_real else "AUSENTE", len(clave_real or "")))

    # =====================================================================
    # CASO 1. SIN CREDENCIAL: FALLO RUIDOSO Y NI UNA LLAMADA A LA RED.
    # =====================================================================
    sin = VoyageFalso(clave="")
    salio, texto = capturar_fallo(IP.paso_a_previo_embeber_candidatos, packs, voyage=sin)
    print("")
    print("CASO 1 (sin credencial): salio=%s, llamadas a Voyage=%d" % (salio, sin.llamadas))
    for linea in texto.strip().splitlines():
        print("   | %s" % linea)
    if not salio:
        fallos.append("CASO 1: sin credencial NO fallo. Degradacion silenciosa.")
    if sin.llamadas != 0:
        fallos.append("CASO 1: sin credencial llamo a Voyage %d vez/veces" % sin.llamadas)
    if "VOYAGE_API_KEY" not in texto:
        fallos.append("CASO 1: el fallo no nombra la variable VOYAGE_API_KEY")
    if ".env" not in texto:
        fallos.append("CASO 1: el fallo no nombra el fichero .env donde vive la variable")
    if "HERRAMIENTA DE SESION CON CREDENCIAL" not in texto:
        fallos.append("CASO 1: el fallo no dice que es herramienta de sesion con credencial")

    # =====================================================================
    # CASO 2. LA MUTACION: LA MISMA VARIABLE, CON VALOR. EL VEREDICTO SE DA
    # LA VUELTA Y EL PASO PIDE LOS VECTORES.
    # =====================================================================
    clave_mutada = clave_real if clave_real else ("no-es-una-clave-real-" + "x" * 8)
    con = VoyageFalso(clave=clave_mutada)
    print("")
    print("CASO 2 (mutacion de la MISMA variable computada, clave con valor):")
    print("   credencial_ausente('') -> %s" % (VOYAGE.credencial_ausente("") or "")[:48])
    print("   credencial_ausente(mutada) -> %r" % VOYAGE.credencial_ausente(clave_mutada))
    vectores = IP.paso_a_previo_embeber_candidatos(packs, voyage=con)
    print("   llamadas a Voyage=%d, vectores devueltos=%d" % (con.llamadas, len(vectores)))
    if con.llamadas < 1:
        fallos.append("CASO 2: con credencial NO se pidio ni un vector")
    if sorted(vectores) != sorted(ids):
        fallos.append("CASO 2: los vectores no cubren exactamente los %d candidatos" % len(ids))
    if con.textos_vistos != textos:
        fallos.append("CASO 2: el texto embebido no es el texto del propio candidato")

    # =====================================================================
    # CASO 3. LA CIRCULARIDAD, ROTA EN MEMORIA. Candidato SINTETICO que no
    # esta en el indice ni en el grafo ni en el disco.
    # =====================================================================
    grafo = AD.cargar_grafo()
    indice = AD.cargar_indice()
    candidato = {
        "node_id": "candidato_sintetico_v148_no_existe",
        "dominio": "quality",
        "titulo_concepto": "Control estadistico del proceso",
        "resumen_teorico": "Medir la variacion de un proceso con cartas de control.",
        "condiciones_activacion": ["el proceso varia sin causa conocida"],
    }
    cid = candidato["node_id"]
    permitido_sin, bloqueos_sin, _ = AD.evaluar(candidato, grafo, indice, [])
    sin_vector = [b for b in bloqueos_sin if "NO TIENE VECTOR" in b]
    print("")
    print("CASO 3 (la circularidad):")
    print("   SIN el paso a-previo: permitido=%s, bloqueos=%d, de ellos por falta de vector=%d"
          % (permitido_sin, len(bloqueos_sin), len(sin_vector)))
    if not sin_vector:
        fallos.append("CASO 3: el candidato sin vector NO se bloqueo por falta de vector; "
                      "entonces esta prueba no esta midiendo la circularidad")

    vec_falso, _ = con.embeber_textos([VOYAGE.texto_nodo(candidato)], input_type="document")
    indice_con = IP.con_candidatos_embebidos(indice, {cid: vec_falso[0]})
    permitido_con, bloqueos_con, vecinos_con = AD.evaluar(candidato, grafo, indice_con, [])
    sin_vector2 = [b for b in bloqueos_con if "NO TIENE VECTOR" in b]
    print("   CON el paso a-previo: permitido=%s, bloqueos=%d, de ellos por falta de vector=%d, "
          "vecinos sobre el umbral=%d"
          % (permitido_con, len(bloqueos_con), len(sin_vector2), len(vecinos_con)))
    if sin_vector2:
        fallos.append("CASO 3: con el vector inyectado SIGUE bloqueando por falta de vector")
    if len(indice_con["ids"]) != len(indice["ids"]) + 1:
        fallos.append("CASO 3: el indice en memoria no crecio en exactamente un id")
    if len(indice["ids"]) != len(indice["embeddings"]):
        fallos.append("CASO 3: el indice original ya venia descuadrado")
    if cid in indice["ids"]:
        fallos.append("CASO 3: con_candidatos_embebidos MUTO el indice original en vez de copiarlo")

    if vecinos_con and permitido_con:
        fallos.append("CASO 3: hay %d vecino(s) sobre el umbral y sin veredicto, y aun asi "
                      "permitio: la puerta dejo de ser puerta" % len(vecinos_con))

    # =====================================================================
    # CASO 3b. LA PUERTA SIGUE SIENDO PUERTA, Y ESTO HAY QUE FORZARLO.
    #
    # El candidato sintetico de arriba salio con CERO vecinos sobre el umbral
    # (su vector es ruido determinista, no un embebido de verdad), asi que la
    # comprobacion "sigue bloqueando por veredicto ausente" quedo VACIA: se
    # cumplio porque no habia nada que comprobar. Un verde que vive de que
    # nadie recorre el camino es justo lo que esta campana persigue, asi que
    # aqui se recorre: se fabrica un CLON de un nodo real y se le da EL MISMO
    # VECTOR que ese nodo, con lo que el coseno es 1.0 por construccion.
    # =====================================================================
    pos = dict((n, i) for i, n in enumerate(indice["ids"]))
    gemelo = None
    for nid in indice["ids"]:
        n = grafo.get(nid)
        if n and not n.get("deprecado") and (n.get("dominio") or "core") == "core":
            gemelo = nid
            break
    if gemelo is None:
        fallos.append("CASO 3b: no se encontro ningun nodo vivo del nucleo para clonar")
    else:
        clon = {
            "node_id": "clon_sintetico_v148_de_" + gemelo,
            "dominio": "core",
            "titulo_concepto": grafo[gemelo].get("titulo_concepto") or "",
            "resumen_teorico": grafo[gemelo].get("resumen_teorico") or "",
        }
        vector_del_gemelo = indice["embeddings"][pos[gemelo]]
        indice_clon = IP.con_candidatos_embebidos(indice, {clon["node_id"]: vector_del_gemelo})
        perm_clon, bloq_clon, vec_clon = AD.evaluar(clon, grafo, indice_clon, [])
        print("")
        print("CASO 3b (la puerta sigue siendo puerta), clon de '%s':" % gemelo)
        print("   con vector inyectado: permitido=%s, vecinos sobre el umbral=%d, bloqueos=%d"
              % (perm_clon, len(vec_clon), len(bloq_clon)))
        if not vec_clon:
            fallos.append("CASO 3b: el clon con el vector IDENTICO al original no dio ni un "
                          "vecino sobre el umbral; la prueba no esta midiendo la puerta")
        if perm_clon:
            fallos.append("CASO 3b: el clon ENTRO sin veredicto escrito: la puerta dejo de "
                          "ser puerta en cuanto el candidato tiene vector")
        if bloq_clon:
            print("   la puerta BLOQUEA por veredicto ausente. Primer motivo:")
            print("      %s" % bloq_clon[0][:180])
        # Y con el veredicto escrito, el mismo clon pasa: la aduana no juzga,
        # obliga a juzgar.
        escritos = [{"nodo": clon["node_id"], "vecino": nid, "veredicto": "continua",
                     "por_que": "arnes de la vuelta 148"} for nid, _ in vec_clon]
        perm_ok, bloq_ok, _ = AD.evaluar(clon, grafo, indice_clon, escritos)
        print("   con los %d veredicto(s) escritos: permitido=%s, bloqueos=%d"
              % (len(escritos), perm_ok, len(bloq_ok)))
        if not perm_ok:
            fallos.append("CASO 3b: con TODOS los veredictos escritos el clon sigue sin pasar: "
                          "la puerta estaria bloqueando por parecido, que la ficha prohibe")

    # =====================================================================
    # CASO 4. DIMENSION AJENA E ID REPETIDO: LOS DOS CAEN.
    # =====================================================================
    salio_dim, texto_dim = capturar_fallo(
        IP.con_candidatos_embebidos, indice, {cid: [0.1, 0.2, 0.3]})
    print("")
    print("CASO 4a (dimension ajena): salio=%s" % salio_dim)
    if not salio_dim:
        fallos.append("CASO 4a: un vector de dimension ajena se mezclo sin protestar")

    repetido = indice["ids"][0]
    salio_rep, texto_rep = capturar_fallo(
        IP.con_candidatos_embebidos, indice, {repetido: vec_falso[0]})
    print("CASO 4b (id que ya estaba, '%s'): salio=%s" % (repetido, salio_rep))
    if not salio_rep:
        fallos.append("CASO 4b: un id que ya tenia vector se duplico sin protestar")

    # =====================================================================
    # CASO 5. dataset/ IDENTICO.
    # =====================================================================
    huella_despues = huella_de_dataset()
    print("")
    print("HUELLA DE dataset/ DESPUES: %s" % huella_despues)
    if huella_antes != huella_despues:
        fallos.append("CASO 5: dataset/ CAMBIO durante el arnes (%s -> %s)"
                      % (huella_antes[:16], huella_despues[:16]))
    else:
        print("dataset/ IDENTICO antes y despues: el arnes no escribio un byte.")

    print("")
    print("NO PROBADO AQUI, Y SE DECLARA: que la llamada REAL a Voyage devuelve un vector")
    print("util para el candidato. Necesita VOYAGE_API_KEY del .env de la raiz, que esta")
    print("fuera del repo mientras el bucle corre. Esa mitad se verifica en la sesion con")
    print("humano presente que corra --ejecutar; aqui no se da por buena.")

    print("")
    if fallos:
        print("ROJO, el arnes de la 1.a NO se sostiene (%d):" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("VERDE: los seis casos se comportan. Sin clave falla nombrando la variable y el")
    print("fichero SIN llamar a la red; con la MISMA variable computada puesta, pide los")
    print("vectores; el vector inyectado quita el bloqueo por falta de vector sin abrir la")
    print("puerta; dimension ajena e id repetido caen; y dataset/ queda identico.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
