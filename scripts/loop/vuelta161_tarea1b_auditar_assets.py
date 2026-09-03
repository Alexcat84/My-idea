# -*- coding: utf-8 -*-
"""vuelta161_tarea1b_auditar_assets.py . TAREA 1.b DE LA VUELTA 161.

LOS SEIS ASSETS DE `scripts/sync_assets_web.py`, LEIDOS UNA VEZ Y COTEJADOS
CONTRA SU FUENTE, CON EL RESULTADO REGISTRADO VERDE O ROJO Y CON NOMBRE.

POR QUE EXISTE. La deuda la midio el auditor en la parada del 3 sep 2026
(`docs/loop/paradas/2026-09-03-credito-vara-movil.md`): *"El contenido de los
seis assets de `sync_assets_web` nunca se audito. Comprobamos que corre y que no
deja diferencia, pero NADIE HA MIRADO LO QUE ESCRIBE. Lleva pendiente desde el
acta 157, o sea cuatro actas."* Hasta hoy la vara era el EXIT CODE y el
`git diff` del ciclo: las dos dicen que el script corrio y que el arbol no se
movio, y NINGUNA de las dos mira lo que hay dentro de los ficheros.

UN ROJO AQUI SE DECLARA, NO SE ARREGLA DE PASO (letra del encargo).

LOS SEIS, CON LA VARA QUE LE TOCA A CADA UNO, Y LAS VARAS NO SON LA MISMA
PORQUE LAS FUENTES NO SON LA MISMA COSA:

  1..4  master_graph.json, preguntas_cache.json, node_families.json y
        entry_seeds.json son COPIAS. Su fuente es un fichero del repo y la vara
        es la que el propio `sync_assets_web.py` declara en su codigo: los bytes
        del origen con CRLF normalizado a LF. Se cotejan BYTE A BYTE. Ademas se
        parsea el JSON de los dos lados y se comparan las claves de primer nivel
        y el conteo de elementos, para que un rojo se pueda nombrar por donde
        entra y no solo como "dos hashes distintos".

  5     prompts.json NO es una copia: lo COMPONE el script leyendo doce
        constantes `SYSTEM_*` de `engine/prototipo_motor.py`. La vara es el
        valor de esas constantes, importadas AQUI y comparadas CARACTER A
        CARACTER contra el valor guardado. Se comprueban las tres cosas: que
        estan las doce, que no sobra ninguna, y que cada valor es identico.

  6     semantic_index.json NO LO PRODUCE ESTE SCRIPT y su fuente no vive en el
        repo: la escribe `scripts/build_semantic_index_voyage.py` llamando a una
        API que cuesta dinero real. ESO SE DICE EN VEZ DE FABRICARLE UNA FUENTE:
        no hay contra que cotejarlo byte a byte sin gastar fuera del repo, que
        es decision de fundador. Lo que SI se puede medir y se mide: su
        estructura, su conteo de vectores, y LA COBERTURA de sus claves contra
        los nodos vivos del grafo, que es una cotejo de contenido real contra
        una fuente que si esta en el repo.

  Y ADEMAS, PARA LOS SEIS: el `manifest.json` que el script escribe se coteja
  contra los ficheros de verdad (sha256 y bytes), porque el manifest es la vara
  que `web/lib/assets/checksums.test.ts` usa en cada build.

USO:  python scripts/loop/vuelta161_tarea1b_auditar_assets.py
"""
import hashlib
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEST = os.path.join(RAIZ, "web", "lib", "assets")

COPIAS = [
    ("master_graph.json", os.path.join("dataset", "metadata", "master_graph.json")),
    ("preguntas_cache.json", os.path.join("engine", "preguntas_cache.json")),
    ("node_families.json", os.path.join("engine", "node_families.json")),
    ("entry_seeds.json", os.path.join("dataset", "metadata", "entry_seeds.json")),
]

PROMPTS_A_EXPORTAR = [
    "SYSTEM_CLASIFICACION",
    "SYSTEM_PUERTA_AVANZADA",
    "SYSTEM_INTERPRETE_MULTI",
    "SYSTEM_PROFUNDIZAR",
    "SYSTEM_PREGUNTA_DIRIGIDA",
    "SYSTEM_PLAN",
    "SYSTEM_ESTADO_VIVO",
    "SYSTEM_JUEZ_SESION",
    "SYSTEM_ORGANIZADOR",
    "SYSTEM_REPORTE",
    "SYSTEM_CLASIFICAR_OFERTA",
    "SYSTEM_DIAGNOSTICO_MUNDO",
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def leer_bytes(ruta):
    with open(ruta, "rb") as fh:
        return fh.read()


def claves_y_conteo(datos):
    if isinstance(datos, dict):
        return sorted(datos.keys())[:8], len(datos), "dict"
    if isinstance(datos, list):
        return [], len(datos), "list"
    return [], 0, type(datos).__name__


def main():
    print("=" * 78)
    print("VUELTA 161, TAREA 1.b: LOS SEIS ASSETS DE sync_assets_web, LEIDOS UNA VEZ")
    print("=" * 78)
    print("")
    veredictos = []

    print("A) LAS CUATRO COPIAS, COTEJADAS BYTE A BYTE CONTRA SU FUENTE")
    print("   vara: bytes del origen con CRLF normalizado a LF, que es lo que el")
    print("   propio sync_assets_web.py declara en su codigo.")
    print("")
    for nombre, rel_origen in COPIAS:
        ruta_dest = os.path.join(DEST, nombre)
        ruta_orig = os.path.join(RAIZ, rel_origen)
        if not os.path.exists(ruta_dest) or not os.path.exists(ruta_orig):
            print("   %-22s ROJO: falta un lado (destino=%s, origen=%s)"
                  % (nombre, os.path.exists(ruta_dest), os.path.exists(ruta_orig)))
            veredictos.append((nombre, False, "falta un lado"))
            continue
        b_orig = leer_bytes(ruta_orig).replace(b"\r\n", b"\n")
        b_dest = leer_bytes(ruta_dest).replace(b"\r\n", b"\n")
        igual = b_orig == b_dest
        print("   %-22s fuente %s" % (nombre, rel_origen.replace("\\", "/")))
        print("      bytes origen %d / bytes destino %d" % (len(b_orig), len(b_dest)))
        print("      sha256 origen %s" % sha(b_orig))
        print("      sha256 destino %s" % sha(b_dest))
        detalle = "identicos byte a byte"
        if not igual:
            detalle = "DIFIEREN"
            n = min(len(b_orig), len(b_dest))
            corte = next((i for i in range(n) if b_orig[i] != b_dest[i]), n)
            detalle += " (primer byte distinto en la posicion %d)" % corte
        try:
            d_orig = json.loads(b_orig.decode("utf-8"))
            d_dest = json.loads(b_dest.decode("utf-8"))
            k_o, n_o, t_o = claves_y_conteo(d_orig)
            k_d, n_d, t_d = claves_y_conteo(d_dest)
            print("      json origen  : %s de %d elementos, claves %s" % (t_o, n_o, k_o))
            print("      json destino : %s de %d elementos, claves %s" % (t_d, n_d, k_d))
            misma_forma = (t_o == t_d and n_o == n_d and k_o == k_d)
        except (ValueError, UnicodeDecodeError) as e:
            print("      json: NO SE PUDO PARSEAR (%s)" % e)
            misma_forma = False
        ok = igual and misma_forma
        print("      VEREDICTO: %s  (%s)" % ("VERDE" if ok else "ROJO", detalle))
        print("")
        veredictos.append((nombre, ok, detalle))

    print("B) prompts.json, COTEJADO CARACTER A CARACTER CONTRA LAS CONSTANTES")
    print("   fuente: engine/prototipo_motor.py (constantes SYSTEM_*)")
    ruta_prompts = os.path.join(DEST, "prompts.json")
    sys.path.insert(0, os.path.join(RAIZ, "engine"))
    try:
        import prototipo_motor as pm
        guardado = json.loads(io.open(ruta_prompts, encoding="utf-8").read())
        faltan = [n for n in PROMPTS_A_EXPORTAR if n not in guardado]
        sobran = [n for n in guardado if n not in PROMPTS_A_EXPORTAR]
        distintos = []
        for n in PROMPTS_A_EXPORTAR:
            if n in guardado and getattr(pm, n, None) != guardado[n]:
                distintos.append(n)
        print("      CIFRA prompts que el script dice exportar: %d" % len(PROMPTS_A_EXPORTAR))
        print("      CIFRA prompts guardados en prompts.json: %d" % len(guardado))
        print("      CIFRA que faltan: %d %s" % (len(faltan), faltan))
        print("      CIFRA que sobran: %d %s" % (len(sobran), sobran))
        print("      CIFRA cuyo texto NO es identico al de la constante: %d %s"
              % (len(distintos), distintos))
        for n in PROMPTS_A_EXPORTAR:
            v = guardado.get(n, "")
            print("         %-28s %6d caracteres  identico=%s"
                  % (n, len(v), getattr(pm, n, None) == v))
        ok = not faltan and not sobran and not distintos
        detalle = "los doce identicos a su constante" if ok else "hay diferencias"
    except Exception as e:  # se declara en vez de callarse
        print("      ROJO: no se pudo cotejar (%s: %s)" % (type(e).__name__, e))
        ok, detalle = False, "no se pudo cotejar"
    print("      VEREDICTO: %s  (%s)" % ("VERDE" if ok else "ROJO", detalle))
    veredictos.append(("prompts.json", ok, detalle))
    print("")

    print("C) semantic_index.json, Y SU FUENTE NO VIVE EN EL REPO")
    print("   lo escribe scripts/build_semantic_index_voyage.py llamando a una API")
    print("   que cuesta dinero real, o sea que un cotejo byte a byte contra su")
    print("   fuente seria gastar fuera del repo, que es decision de fundador.")
    print("   Se mide lo que SI se puede medir sin salir del repo:")
    ruta_si = os.path.join(DEST, "semantic_index.json")
    try:
        b_si = leer_bytes(ruta_si)
        d_si = json.loads(b_si.decode("utf-8"))
        k_si, n_si, t_si = claves_y_conteo(d_si)
        print("      bytes %d, sha256 %s" % (len(b_si), sha(b_si)))
        print("      json: %s de %d elementos, claves de primer nivel %s"
              % (t_si, n_si, k_si))
        # CAIDA MIA DE LA VUELTA 161, CAZADA LEYENDO MI PROPIA SALIDA, Y ES LA
        # MISMA ESPECIE QUE EL ACTA 158 YA TIENE REGISTRADA (docs/loop/
        # ACTA_AUDITOR.md:52977: "leyo el grafo por la clave `nodes` y las filas
        # del archivo por `puesto`, y esta casa las llama `nodos` y
        # `puesto_intra`. Salio CIFRA nodos: 6"). Mi primera version hacia
        # grafo.get("nodes", grafo) y la clave de esta casa es `nodos`, asi que
        # el fallback devolvia el diccionario entero y publicaba
        # "CIFRA nodos del grafo: 6", que son las seis claves de primer nivel.
        # Igual con el indice: sus claves de vectores viven en `ids`, no dentro
        # de `embeddings`. Linea vieja TACHADA Y LEGIBLE, no borrada:
        #     ~~nodos = grafo.get("nodes", grafo)~~
        #     ~~for clave in ("vectors", "vectores", "index", "items", "embeddings")~~
        # Y AHORA NO SE ADIVINA LA CLAVE: si no esta, se dice y se para el
        # cotejo de cobertura en vez de publicar una cifra de un fallback.
        vectores = d_si.get("embeddings") if isinstance(d_si, dict) else None
        if vectores is not None:
            print("      CIFRA entradas bajo 'embeddings': %d" % len(vectores))
        ids = None
        vivos_sin_vector = []
        if isinstance(d_si, dict) and isinstance(d_si.get("ids"), list):
            ids = set(d_si["ids"])
            print("      CIFRA entradas bajo 'ids': %d" % len(d_si["ids"]))
            print("      CIFRA ids distintos: %d" % len(ids))
        grafo = json.loads(io.open(
            os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"),
            encoding="utf-8").read())
        if "nodos" not in grafo:
            raise KeyError("el grafo no trae la clave 'nodos'; no se adivina otra")
        nodos = grafo["nodos"]
        if isinstance(nodos, dict):
            ids_grafo = set(nodos.keys())
        else:
            ids_grafo = set(n.get("id") for n in nodos)
        print("      CIFRA nodos del grafo: %d" % len(ids_grafo))
        if ids:
            dentro = len(ids & ids_grafo)
            print("      CIFRA claves del indice: %d" % len(ids))
            print("      CIFRA claves del indice que SON nodos del grafo: %d" % dentro)
            print("      CIFRA claves del indice que NO son nodos del grafo: %d"
                  % len(ids - ids_grafo))
            sin_entrada = ids_grafo - ids
            print("      CIFRA nodos del grafo SIN entrada en el indice: %d"
                  % len(sin_entrada))
            muestra = sorted(ids - ids_grafo)[:5]
            if muestra:
                print("      muestra de claves que no son nodos: %s" % muestra)
            # La cobertura sola no dice nada sin partirla por vivos y
            # deprecados: un deprecado sin vector no es una perdida.
            def _depre(nid):
                n = nodos[nid] if isinstance(nodos, dict) else {}
                return bool(n.get("deprecado") or n.get("deprecated")
                            or n.get("estado") == "deprecado")
            vivos = set(n for n in ids_grafo if not _depre(n))
            depre = ids_grafo - vivos
            print("      CIFRA nodos vivos: %d ; deprecados: %d"
                  % (len(vivos), len(depre)))
            print("      CIFRA VIVOS sin entrada en el indice: %d"
                  % len(vivos - ids))
            print("      CIFRA DEPRECADOS sin entrada en el indice: %d"
                  % len(depre - ids))
            vivos_sin_vector = sorted(vivos - ids)
            print("      LOS VIVOS SIN ENTRADA, UNO A UNO Y SIN RESUMIR:")
            for nid in vivos_sin_vector:
                print("         %s" % nid)
        else:
            print("      no se pudo derivar la nomina de claves del indice")
        # EL VEREDICTO NO SE AFLOJA PORQUE LA FUENTE NO ESTE: lo que SI se puede
        # medir es la cobertura contra el grafo, y si un nodo VIVO no tiene
        # vector, la busqueda semantica lo pierde EN SILENCIO. Eso es rojo,
        # aunque el manifest y el sha256 esten los dos verdes.
        ok = not vivos_sin_vector
        if ok:
            detalle = ("estructura y cobertura completas sobre los nodos vivos; el "
                       "cotejo byte a byte contra su fuente no se puede hacer sin "
                       "gastar fuera del repo")
        else:
            detalle = ("ROJO DE COBERTURA: %d nodos VIVOS sin vector en el indice "
                       "(nombrados arriba). Se declara y NO se arregla de paso: "
                       "rehacer el indice llama a una API que cuesta dinero real y "
                       "eso es decision de fundador" % len(vivos_sin_vector))
    except Exception as e:
        print("      ROJO: no se pudo leer o parsear (%s: %s)" % (type(e).__name__, e))
        ok, detalle = False, "no se pudo leer"
    print("      VEREDICTO: %s  (%s)" % ("VERDE" if ok else "ROJO", detalle))
    veredictos.append(("semantic_index.json", ok, detalle))
    print("")

    print("D) EL MANIFEST CONTRA LOS FICHEROS DE VERDAD")
    print("   (el manifest es la vara de web/lib/assets/checksums.test.ts)")
    ruta_man = os.path.join(DEST, "manifest.json")
    man = json.loads(io.open(ruta_man, encoding="utf-8").read())
    malos = []
    for nombre, entrada in sorted(man.items()):
        ruta = os.path.join(DEST, nombre)
        if not os.path.exists(ruta):
            print("   %-22s ROJO: el manifest lo nombra y el fichero no existe" % nombre)
            malos.append(nombre)
            continue
        b = leer_bytes(ruta)
        cuadra = (sha(b) == entrada.get("sha256") and len(b) == entrada.get("bytes"))
        print("   %-22s sha256 cuadra=%s bytes %d/%d  fuente declarada: %s"
              % (nombre, cuadra, len(b), entrada.get("bytes"), entrada.get("fuente")))
        if not cuadra:
            malos.append(nombre)
    print("   CIFRA entradas en el manifest: %d" % len(man))
    print("   CIFRA que no cuadran: %d %s" % (len(malos), malos))
    ok_man = not malos
    veredictos.append(("manifest.json", ok_man,
                       "todas las entradas cuadran" if ok_man else "hay entradas que no cuadran"))
    print("      VEREDICTO: %s" % ("VERDE" if ok_man else "ROJO"))
    print("")

    print("=" * 78)
    print("REGISTRO DEL RESULTADO, CON NOMBRE, QUE ES LO QUE EL ENCARGO PIDE")
    print("=" * 78)
    for nombre, ok, detalle in veredictos:
        print("   %-22s %-26s %s" % (nombre, "VERDE" if ok else "ROJO", detalle))
    print("")
    print("   CIFRA assets auditados: %d" % len(veredictos))
    print("   CIFRA en VERDE: %d" % len([1 for _n, ok, _d in veredictos if ok]))
    print("   CIFRA en ROJO: %d" % len([1 for _n, ok, _d in veredictos if not ok]))
    todos = all(ok for _n, ok, _d in veredictos)
    print("   VEREDICTO DE LA TAREA: %s" % ("VERDE" if todos else "ROJO, y se declara"))
    print("FIN")
    return 0 if todos else 1


if __name__ == "__main__":
    raise SystemExit(main())
