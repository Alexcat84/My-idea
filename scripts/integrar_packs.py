# -*- coding: utf-8 -*-
"""
integrar_packs.py — Fase 3.5 (bloque 4): la LÍNEA DE ENSAMBLAJE que
convierte los packs saneados (P1-HSEQ, tag hseq-sanitized-v1) en parte
del universo recorrible del motor.

PREREQUISITO HUMANO BLOQUEANTE: packs/<dominio>/metadata/bridges_aprobados.json
para CADA pack pendiente (el usuario aprueba 10-15 puentes por dominio desde
bridges_propuestos.json; regla: ningún nodo core ancla más de 2-3 puentes
por dominio). Sin esos archivos, este script se niega a correr.

v1.3.2: los packs se descubren de packs/*/nodos (data-driven, nada hardcodeado);
los ya integrados (HSEQ, fase 3.5) se detectan porque sus nodos viven en
dataset/nodos/ y se saltan — congelados.

Secuencia (plan de fase, puntos a-f):
  a. Compilar master_graph con core + packs + puentes aprobados
     (bidireccionales: alta el hijo en nodos_siguientes del padre y el
     padre en nodos_previos del hijo, en los archivos fuente).
  b. Etiquetado de familias (etiqueta del árbol de readiness) para los
     nodos de packs: engine/plan_readiness.py — mismo clasificador por
     palabras clave del core, sin costo de API.
  c. Caché de preguntas PARCIAL: engine/build_question_cache.py --patch
     con los nodos de packs + los nodos core cuyos sucesores cambiaron
     por puentes (los únicos cuyo contexto de pregunta cambió).
  d. Índice semántico Voyage COMPLETO (~2805 nodos):
     scripts/build_semantic_index_voyage.py.
  e. scripts/run_phase1.py con dominios ampliados — Gate 0 debe quedar
     VERDE (0 rotos, 1 componente, cobertura del componente principal).
  f. scripts/sync_assets_web.py + suites web (checksums de prompts y
     contrato) verdes.
Reporta costos reales de b+c+d (b es gratis; c y d llaman APIs).

HERRAMIENTA DE SESION CON CREDENCIAL (decision del fundador, 2 sep 2026,
docs/loop/paradas/2026-09-02-aduana-vector-y-a13-DECISION.md).
`integrar_packs.py --ejecutar` es una HERRAMIENTA DE SESION CON CREDENCIAL:
corre SOLO en sesiones post campaña, con humano presente y el .env
disponible. JAMAS DENTRO DEL BUCLE AUTONOMO. Gasta credencial de Voyage en
dos sitios (el paso a-previo, una llamada por candidato, y el paso d, el
indice completo) y por eso no es una herramienta que un bucle sin humano
pueda invocar. Invocada sin la clave falla RUIDOSAMENTE nombrando la
variable que falta y el fichero donde vive, y no sigue a medias.

  a-previo. EMBEBIDO DEL CANDIDATO, APARTE Y ANTES DE LA COPIA (vuelta 148).
     La vuelta 147 midio una dependencia CIRCULAR: la aduana semantica A2.6
     esta cableada en la copia del paso (a), pero el vector del candidato
     solo existe tras el paso (d), que lee un grafo que solo conoce al
     candidato tras esa misma copia. El fundador la resolvio por el CAMINO 1
     con precision de sede: el candidato se embebe APARTE, llamando a Voyage
     con el texto del PROPIO CANDIDATO, y el vector se inyecta EN MEMORIA en
     el indice que la aduana consulta. No hace falta el grafo para un vector.
     LA PUERTA NO SE MUEVE: sigue bloqueando EN la insercion, en el copy2 del
     paso (a), como la ficha OP-A-02 manda. Esto anade un paso ANTES, no
     mueve la puerta despues.

Uso:
  python scripts/integrar_packs.py --dry-run   # valida prerequisitos sin tocar nada
  python scripts/integrar_packs.py --ejecutar  # corre la línea completa
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATASET_NODOS = BASE / "dataset" / "nodos"
MASTER_GRAPH = BASE / "dataset" / "metadata" / "master_graph.json"


def descubrir_packs():
    """v1.3.2: los packs se descubren de packs/*/nodos (nada hardcodeado) y se
    separan en ya-integrados (todos sus nodos viven en dataset/nodos, p.ej. los
    HSEQ de la fase 3.5, congelados) y pendientes. Un estado parcial es un bug.
    """
    integrados, pendientes = [], []
    for carpeta in sorted(p for p in (BASE / "packs").iterdir() if (p / "nodos").is_dir()):
        nodos = sorted((carpeta / "nodos").glob("*.json"))
        if not nodos:
            continue
        en_dataset = sum(1 for n in nodos if (DATASET_NODOS / n.name).exists())
        if en_dataset == len(nodos):
            integrados.append(carpeta.name)
        elif en_dataset == 0:
            pendientes.append(carpeta.name)
        else:
            fallar(
                f"pack '{carpeta.name}' en estado PARCIAL: {en_dataset}/{len(nodos)} nodos "
                "ya están en dataset/nodos/ — integración a medias, revisar antes de seguir"
            )
    return integrados, pendientes


def fallar(msg):
    print(f"\nERROR: {msg}")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Reanudación POR PASO.
#
# La avería de origen (2026-08-07, integrando compras y entrega): el paso (a)
# copió los nodos a dataset/ y el paso (e) fallo. Al reintentar, descubrir_packs
# vio los nodos ya en dataset/, declaro los packs "ya integrados" y el script
# dijo "no hay packs pendientes, nada que hacer" — con los pasos b a f sin
# correr. Salio en verde con la mitad del trabajo sin hacer.
#
# La causa es que el estado se DEDUCIA de un efecto de un solo paso. Ahora se
# ESCRIBE, paso a paso: el archivo nace antes del primero y muere despues del
# ultimo, asi que su sola existencia significa "esto quedo a medias".
# ---------------------------------------------------------------------------
ESTADO = BASE / "dataset" / "metadata" / "_integracion_en_curso.json"

# "a_previo_embebido" NO figura aqui a proposito: su producto (los vectores de
# los candidatos) vive en memoria, no en disco, asi que no hay nada que
# "quedara hecho" entre dos corridas. Corre siempre pegado al paso (a).
PASOS = [
    "a_nodos_y_puentes", "e_gate0", "e_bis_etiquetas", "b_familias",
    "c_cache_preguntas", "d_indice_voyage", "d_bis_rumbos",
    "f_sync", "f_suite_web", "f_suite_python",
]


def pasos_pendientes(estado):
    hechos = set((estado or {}).get("hechos", []))
    return [p for p in PASOS if p not in hechos]


def decidir_accion(estado, pendientes):
    """Que hacer, en una funcion pura y testeable.

    Devuelve ('reanudar', faltan) | ('integrar', packs) | ('nada', []).
    NUNCA devuelve 'nada' habiendo trabajo a medias: ese era el bug.
    """
    if estado:
        faltan = pasos_pendientes(estado)
        if faltan:
            return "reanudar", faltan
        # Archivo huerfano: todos los pasos hechos pero nadie lo borro.
        return "nada", []
    if pendientes:
        return "integrar", pendientes
    return "nada", []


def guardar_estado(estado):
    ESTADO.parent.mkdir(parents=True, exist_ok=True)
    ESTADO.write_text(json.dumps(estado, ensure_ascii=False, indent=2), encoding="utf-8")


def cargar_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def guardar_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def validar_prerequisitos(packs):
    """El muro humano: bridges_aprobados.json en TODOS los packs pendientes."""
    faltantes = []
    puentes_por_dominio = {}
    for d in packs:
        ruta = BASE / "packs" / d / "metadata" / "bridges_aprobados.json"
        if not ruta.exists():
            faltantes.append(str(ruta.relative_to(BASE)))
            continue
        puentes = cargar_json(ruta)
        # Forma aprobada por el usuario: {"nota": ..., "aprobados": [pares]}.
        # La nota viaja en el archivo; aquí solo consumimos los pares.
        if isinstance(puentes, dict) and isinstance(puentes.get("aprobados"), list):
            puentes = puentes["aprobados"]
        if not isinstance(puentes, list) or len(puentes) == 0:
            fallar(f"{ruta.name} de '{d}' está vacío o no es una lista (ni {{nota, aprobados}})")
        puentes_por_dominio[d] = puentes
    if faltantes:
        fallar(
            "PREREQUISITO HUMANO PENDIENTE — faltan las aprobaciones de puentes:\n  - "
            + "\n  - ".join(faltantes)
            + "\nEl usuario debe aprobar 10-15 puentes por dominio desde bridges_propuestos.json "
            "(regla: ningún nodo core ancla más de 2-3 puentes por dominio) y guardar la selección "
            "en bridges_aprobados.json. Este script NO corre sin el archivo de cada pack pendiente."
        )
    # Regla de concentración: ningún nodo core ancla más de 3 puentes por dominio.
    # Formato esperado (el de bridges_propuestos.json['candidatos']):
    # {"core": <id core>, "dominio": <id del nodo del pack>, "score": ...}
    for d, puentes in puentes_por_dominio.items():
        conteo = {}
        for p in puentes:
            core = p.get("core")
            if not core:
                fallar(f"puente sin campo 'core' en '{d}': {json.dumps(p, ensure_ascii=False)[:120]}")
            conteo[core] = conteo.get(core, 0) + 1
        excedidos = {k: v for k, v in conteo.items() if v > 3}
        if excedidos:
            fallar(f"'{d}': nodos core anclando más de 3 puentes (regla del plan): {excedidos}")
        if not (5 <= len(puentes) <= 20):
            print(f"  AVISO: '{d}' tiene {len(puentes)} puentes (esperado 10-15±) — verificar que es intencional.")
    return puentes_por_dominio


def validar_anclas_de_todos_los_puentes():
    """LA LEY DEL ANCLA, sobre TODOS los puentes y no solo los pendientes.

    Un puente conecta mundo -> corazon y ancla SIEMPRE en el nucleo. La
    asercion del tejedor mataba la clase solo en los packs que estaban por
    integrarse; los 22 que ya vivian en disco no los miraba nadie. Aqui se
    revisan todos, en cada corrida, incluida la de --dry-run.
    """
    grafo_path = BASE / "dataset" / "metadata" / "master_graph.json"
    if not grafo_path.exists():
        return
    grafo = cargar_json(grafo_path)["nodos"]
    malos = []
    for ruta in sorted((BASE / "packs").glob("*/metadata/bridges_aprobados.json")):
        pack = ruta.parent.parent.name
        for x in cargar_json(ruta).get("aprobados", []):
            dom = grafo.get(x.get("core"), {}).get("dominio", "core")
            if dom != "core":
                malos.append(f"{pack}: ancla '{x.get('core')}' es de '{dom}'")
    if malos:
        detalle = "\n  ".join(malos[:10])
        fallar(f"puentes anclados FUERA del nucleo (la ley del ancla): {len(malos)}\n  {detalle}")
    print(f"  Ley del ancla: todos los puentes de todos los packs anclan en el nucleo.")


def _cargar_voyage():
    """El modulo del indice semantico, importado tarde y no arriba: importarlo
    carga el .env y lee la credencial, y quien solo corre --dry-run no tiene
    por que pasar por ahi."""
    sys.path.insert(0, str(BASE / "scripts"))
    import build_semantic_index_voyage as voyage
    return voyage


def id_de_candidato(nodo, archivo):
    """EL ID DE UN NODO DE PACK, DERIVADO EN UN SOLO SITIO. Hoy los 2.114 nodos
    de pack tienen `node_id` igual al nombre del fichero (medido en la vuelta
    148: 0 distintos), pero derivarlo de dos maneras en dos sitios es una
    coincidencia esperando a romperse en silencio el dia que uno solo difiera:
    el vector se guardaria bajo una clave y se buscaria bajo otra."""
    return nodo.get("node_id") or nodo.get("id") or archivo.stem


def ids_de_candidatos(packs):
    """Los ids de todos los nodos de los packs dados, por el mismo camino que
    usa el embebido."""
    fuera = []
    for d in packs:
        for archivo in sorted((BASE / "packs" / d / "nodos").glob("*.json")):
            fuera.append(id_de_candidato(cargar_json(archivo), archivo))
    return fuera


def ids_y_textos_de_candidatos(packs):
    """(ids, textos) de todos los nodos de los packs pendientes, EN EL MISMO
    ORDEN, leidos de su propio fichero del pack. El texto se arma con
    `texto_nodo` del modulo del indice, o sea EXACTAMENTE el mismo texto con
    el que se embebe cualquier otro nodo: si aqui se armara distinto, el
    candidato se mediria en un espacio que no es el del indice y la aduana
    comparia peras con manzanas."""
    voyage = _cargar_voyage()
    ids, textos, vacios = [], [], []
    for d in packs:
        for archivo in sorted((BASE / "packs" / d / "nodos").glob("*.json")):
            n = cargar_json(archivo)
            nid = id_de_candidato(n, archivo)
            texto = voyage.texto_nodo(n)
            if not texto:
                vacios.append(str(archivo.relative_to(BASE)))
            ids.append(nid)
            textos.append(texto)
    if vacios:
        fallar("embebido del candidato: %d nodo(s) de pack no tienen NADA que embeber "
               "(sin titulo, sin resumen y sin condiciones): %s. Un vector de texto vacio "
               "no mide nada y la aduana no puede juzgar con el"
               % (len(vacios), ", ".join(vacios[:5])))
    return ids, textos


def con_candidatos_embebidos(indice, vectores_por_id):
    """Copia del indice con los candidatos DENTRO, en memoria. No escribe un
    byte: `web/lib/assets/semantic_index.json` se reconstruye entero y bien en
    el paso (d), y adelantarse a escribirlo aqui dejaria un indice a medias en
    el arbol si la linea se cortara en el paso siguiente.

    Comprueba la DIMENSION una por una. Un vector de otro largo no es un error
    que se pueda arrastrar: `evaluar` monta una matriz con todo junto y numpy
    fabricaria un array de objetos en vez de fallar, o sea que el sintoma
    aparecerian metros mas abajo y disfrazado."""
    esperada = int(indice.get("dimension") or (len(indice["embeddings"][0]) if indice["embeddings"] else 0))
    ya = set(indice["ids"])
    ids = list(indice["ids"])
    embeddings = list(indice["embeddings"])
    for nid in sorted(vectores_por_id):
        v = vectores_por_id[nid]
        if len(v) != esperada:
            fallar("embebido del candidato: el vector de '%s' tiene dimension %d y el indice "
                   "usa %d. No se mezclan: la aduana mediria contra un espacio distinto"
                   % (nid, len(v), esperada))
        if nid in ya:
            fallar("embebido del candidato: '%s' YA tiene vector en el indice. Un candidato "
                   "que todavia no se ha copiado no deberia estar ahi: revisar antes de seguir"
                   % nid)
        ids.append(nid)
        embeddings.append(list(v))
    nuevo = dict(indice)
    nuevo["ids"] = ids
    nuevo["embeddings"] = embeddings
    return nuevo


def paso_a_previo_embeber_candidatos(packs, voyage=None):
    """PASO a-previo: UNA LLAMADA A VOYAGE POR CANDIDATO, antes de la copia.

    Devuelve {node_id: vector}. `voyage` se puede inyectar para que el arnes de
    prueba corra este paso SIN salir a la red y SIN gastar credencial.

    EL FALLO RUIDOSO. Sin credencial no se embebe, sin vector la aduana bloquea
    y sin aduana no hay insercion: no hay ningun "seguir a medias" que tenga
    sentido. Asi que se comprueba ANTES de leer un solo fichero y se falla
    nombrando la variable y el fichero donde vive."""
    voyage = voyage or _cargar_voyage()
    print("\n=== a-previo. Embebido del candidato APARTE (antes de la copia) ===")

    motivo = voyage.credencial_ausente()
    if motivo:
        fallar("EMBEBIDO DEL CANDIDATO (paso a-previo): %s\n  "
               "integrar_packs.py --ejecutar es una HERRAMIENTA DE SESION CON CREDENCIAL: "
               "corre solo en sesiones post campaña, con humano presente y el .env puesto, "
               "y JAMAS dentro del bucle autonomo." % motivo)

    ids, textos = ids_y_textos_de_candidatos(packs)
    if not ids:
        fallar("embebido del candidato: los packs pendientes no traen ningun nodo")
    print("  %d candidato(s) a embeber con %s (dim=%d), en lotes de %d."
          % (len(ids), voyage.VOYAGE_MODEL, voyage.OUTPUT_DIMENSION, voyage.BATCH_SIZE))

    vectores, tokens = [], 0
    for i in range(0, len(textos), voyage.BATCH_SIZE):
        lote = textos[i:i + voyage.BATCH_SIZE]
        vs, usage = voyage.embeber_textos(lote, input_type="document")
        if len(vs) != len(lote):
            fallar("embebido del candidato: se pidieron %d vectores y volvieron %d. El orden "
                   "de Voyage es el de entrada, y sin esa correspondencia los vectores se "
                   "asignarian al nodo equivocado" % (len(lote), len(vs)))
        vectores.extend(vs)
        tokens += (usage or {}).get("total_tokens", 0)
    print("  %d vector(es) obtenidos (~%d tokens). NO se escribe el indice aqui: el paso (d) "
          "lo reconstruye entero." % (len(vectores), tokens))
    return dict(zip(ids, vectores))


def paso_a_integrar_nodos_y_puentes(packs, puentes_por_dominio, vectores_candidatos=None):
    """Copia los nodos de packs al dataset y teje los puentes bidireccionales."""
    print("\n=== a. Integrando nodos de packs + puentes aprobados ===")

    # LA PUERTA SEMANTICA A2.6 DE OP-A-02, CABLEADA AQUI (vuelta 147, TAREA
    # 3.e). Este es el punto de insercion que la 3.e de la vuelta 146 dejo
    # nombrado: el shutil.copy2 que copia cada nodo a dataset/nodos/. La frase
    # que lo gobierna, citada de la ficha: LA ADUANA NO JUZGA, OBLIGA A JUZGAR.
    # Al insertar un nodo se corre el indice contra SU DOMINIO y el NUCLEO, y si
    # algun vecino supera el umbral de la cola LA INSERCION SE BLOQUEA hasta que
    # quien inserta escriba el veredicto continua-o-repite CITANDO EL ID DEL
    # VECINO. Nunca bloquea por parecido: solo por VEREDICTO AUSENTE.
    #
    # NO SE REIMPLEMENTA NADA: el criterio entero, con su frontera, sus dos
    # umbrales IMPORTADOS de scripts/intra_dominio.py y el vecindario, vive en
    # scripts/loop/aduana_semantica.py. Dos versiones de la misma comprobacion
    # serian la averia de los dos master_graph que el chequeo de gemelos vino a
    # curar.
    #
    # LO QUE ESTA PUERTA CUESTA, DICHO AQUI Y NO ESCONDIDO: un candidato SIN
    # VECTOR en el indice semantico no se puede medir, y la puerta lo bloquea
    # diciendolo en vez de dejarlo pasar sin mirar (banco 9). En la secuencia de
    # HOY el indice se construye en el paso (d), DESPUES de esta copia, asi que
    # un pack pendiente de verdad chocaria contra eso. QUEDA TRAIDO COMO PARADA
    # en el reporte de la vuelta 147 y NO SE DECIDE AQUI: reordenar la linea o
    # embeber el candidato antes de insertarlo es una decision que el texto de
    # la ficha no cubre.
    if packs:
        sys.path.insert(0, str(BASE / "scripts" / "loop"))
        from aduana_semantica import (cargar_grafo, cargar_indice, cargar_veredictos,
                                      evaluar)
        grafo_aduana = cargar_grafo()
        indice_aduana = cargar_indice()
        veredictos_aduana = cargar_veredictos()
        # EL VECTOR DEL CANDIDATO, PUESTO EN MEMORIA (vuelta 148). Viene del
        # paso a-previo, que ya llamo a Voyage con el texto del propio
        # candidato. Sin esto la aduana bloquearia a TODO candidato por "no
        # tiene vector", que es la dependencia circular que la 147 midio.
        # Se exige que esten TODOS: un candidato sin vector aqui seria un
        # bloqueo silencioso disfrazado de bloqueo legitimo.
        tengo = vectores_candidatos or {}
        faltan = [nid for nid in ids_de_candidatos(packs) if nid not in tengo]
        if faltan:
            fallar("la aduana iba a medir sin los vectores del paso a-previo: faltan %d "
                   "(%s). Correr la linea entera, no el paso (a) suelto"
                   % (len(faltan), ", ".join(faltan[:5])))
        indice_aduana = con_candidatos_embebidos(indice_aduana, vectores_candidatos)
    copiados = 0
    for d in packs:
        origen = BASE / "packs" / d / "nodos"
        for archivo in sorted(origen.glob("*.json")):
            destino = DATASET_NODOS / archivo.name
            if destino.exists():
                fallar(f"colisión de node_id entre core y '{d}': {archivo.name} ya existe en dataset/nodos/")
            candidato = cargar_json(archivo)
            permitido, bloqueos, _vecinos = evaluar(
                candidato, grafo_aduana, indice_aduana, veredictos_aduana)
            if not permitido:
                detalle = "\n  ".join(bloqueos[:5])
                fallar(f"ADUANA SEMANTICA (OP-A-02, A2.6): la insercion de "
                       f"{archivo.name} queda BLOQUEADA, {len(bloqueos)} motivo(s)\n  "
                       f"{detalle}")
            shutil.copy2(archivo, destino)
            copiados += 1
    print(f"  {copiados} nodos de packs copiados a dataset/nodos/.")

    tejidos = 0
    tocados_core = set()
    for d, puentes in puentes_por_dominio.items():
        for p in puentes:
            core_id = p.get("core")
            pack_id = p.get("dominio")  # así llama bridges_propuestos al nodo del pack
            if not pack_id:
                fallar(f"puente sin campo 'dominio' (nodo del pack) en '{d}': {json.dumps(p, ensure_ascii=False)[:120]}")
            ruta_core = DATASET_NODOS / f"{core_id}.json"
            ruta_pack = DATASET_NODOS / f"{pack_id}.json"
            if not ruta_core.exists() or not ruta_pack.exists():
                fallar(f"puente {core_id} -> {pack_id}: alguno de los dos no existe en dataset/nodos/")
            nodo_core = cargar_json(ruta_core)
            nodo_pack = cargar_json(ruta_pack)

            # EL ANCLA MAL ROTULADA MUERE AQUÍ, en la fábrica.
            #
            # Un puente es "del core hacia un mundo", y el campo se llama `core`
            # por eso. Pero el proponedor de puentes busca sobre el master graph
            # entero, donde los packs YA integrados también viven: nada le
            # impedía anclar un puente de entrega en un nodo de quality y
            # llamarlo "core". La cirugía de Calidad pagó esa lección con dos
            # especímenes: al deprecar nodos de quality se rompieron un puente
            # de entrega y otro de risk_management, y no se vieron hasta que el
            # Gate 0 aprendió a mirarlos.
            #
            # El Gate los caza DESPUÉS, con el daño hecho y a mano. Aquí se
            # cazan ANTES, cuando todavía es un dato en un archivo: el dominio
            # REAL del ancla tiene que ser 'core', y el del otro extremo tiene
            # que ser el pack que el puente declara.
            dom_core = nodo_core.get("dominio", "core")
            if dom_core != "core":
                fallar(
                    f"puente de '{d}' anclado en '{core_id}', que NO es del core "
                    f"sino de '{dom_core}'. Un puente sale del core; si el ancla "
                    f"pertenece a otro pack, el puente ata dos mundos entre sí y "
                    f"nadie lo sabe hasta que uno de los dos cambie."
                )
            dom_pack = nodo_pack.get("dominio")
            if dom_pack != d:
                fallar(
                    f"puente de '{d}' cuyo extremo '{pack_id}' pertenece a "
                    f"'{dom_pack}', no a '{d}'."
                )

            if pack_id not in nodo_core.get("nodos_siguientes", []):
                nodo_core.setdefault("nodos_siguientes", []).append(pack_id)
            if core_id not in nodo_pack.get("nodos_previos", []):
                nodo_pack.setdefault("nodos_previos", []).append(core_id)
            guardar_json(ruta_core, nodo_core)
            guardar_json(ruta_pack, nodo_pack)
            tejidos += 1
            tocados_core.add(core_id)
    print(f"  {tejidos} puentes tejidos (bidireccionales) sobre {len(tocados_core)} nodos core.")
    return tocados_core


def correr(cmd, descripcion):
    print(f"\n=== {descripcion} ===\n  $ {' '.join(cmd)}")
    # Windows: pnpm es pnpm.cmd — subprocess sin shell no lo resuelve solo.
    ejecutable = shutil.which(cmd[0])
    if ejecutable:
        cmd = [ejecutable] + cmd[1:]
    r = subprocess.run(cmd, cwd=BASE)
    if r.returncode != 0:
        fallar(f"'{descripcion}' terminó con código {r.returncode} — línea de ensamblaje DETENIDA (revisar antes de reintentar)")


def main():
    ap = argparse.ArgumentParser()
    modo = ap.add_mutually_exclusive_group(required=True)
    modo.add_argument("--dry-run", action="store_true", help="valida prerequisitos sin tocar nada")
    modo.add_argument("--ejecutar", action="store_true", help="corre la línea de ensamblaje completa")
    args = ap.parse_args()

    validar_anclas_de_todos_los_puentes()
    integrados, pendientes = descubrir_packs()
    estado = json.loads(ESTADO.read_text(encoding="utf-8")) if ESTADO.exists() else None
    accion, detalle = decidir_accion(estado, pendientes)

    if integrados:
        print(f"Packs ya integrados (congelados, no se tocan): {', '.join(integrados)}")

    if accion == "nada":
        if estado:
            print(f"Todos los pasos estaban hechos; borrando {ESTADO.name} huerfano.")
            ESTADO.unlink(missing_ok=True)
        print("No hay packs pendientes de integrar. Nada que hacer.")
        return

    if accion == "reanudar":
        pendientes = estado["packs"]
        print(f"\nINTEGRACION A MEDIAS de {', '.join(pendientes)}: "
              f"{len(estado['hechos'])} pasos hechos, faltan {len(detalle)}.")
        for p in detalle:
            print(f"   pendiente: {p}")
        if args.dry_run:
            print("\n--dry-run: nada tocado. Para reanudar: python scripts/integrar_packs.py --ejecutar")
            return
        print("Se REANUDA desde el primer paso pendiente.\n")
    else:
        print(f"Packs pendientes: {', '.join(pendientes)}")

    puentes = validar_prerequisitos(pendientes)
    total_pack_nodes = sum(len(list((BASE / "packs" / d / "nodos").glob("*.json"))) for d in pendientes)
    print(f"Prerequisitos OK: puentes aprobados en {len(pendientes)} packs; {total_pack_nodes} nodos listos.")

    if args.dry_run:
        print("\n--dry-run: nada tocado. Para ejecutar: python scripts/integrar_packs.py --ejecutar")
        return

    if estado is None:
        estado = {"packs": pendientes, "hechos": [], "tocados_core": []}
        guardar_estado(estado)

    def paso(nombre, fn):
        """Corre el paso si falta; lo marca solo DESPUES de que salga bien."""
        if nombre in estado["hechos"]:
            print(f"\n=== [ya hecho, se salta] {nombre} ===")
            return
        fn()
        estado["hechos"].append(nombre)
        guardar_estado(estado)

    # a-previo. EL EMBEBIDO DEL CANDIDATO, ANTES DE LA COPIA. No se marca como
    # paso hecho en el fichero de estado A PROPOSITO: los vectores viven en
    # memoria y no en disco, asi que una reanudacion que se saltara este paso
    # llegaria al paso (a) sin ellos. Es barato de rehacer (una llamada por
    # candidato) y caro de suponer.
    vectores_candidatos = {}

    def _a():
        vectores_candidatos.update(paso_a_previo_embeber_candidatos(pendientes))
        estado["tocados_core"] = sorted(
            paso_a_integrar_nodos_y_puentes(pendientes, puentes, vectores_candidatos))
    paso("a_nodos_y_puentes", _a)

    # e-parte-1. recompilar master_graph + Gate 0 (los nodos ya están en dataset/)
    # --reaplico-curaduria: run_phase1 avisa a gritos y FALLA cuando la
    # recompilación revierte las etiquetas de cara. Aquí ese aviso sobra,
    # porque el paso siguiente (e-bis) las reaplica; sin la bandera pararía la
    # línea justo antes de arreglarlo.
    paso("e_gate0", lambda: correr(
        [sys.executable, "scripts/run_phase1.py", "--reaplico-curaduria"],
        "e. run_phase1: recompilación + Gate 0 (debe quedar VERDE)"))

    # e-parte-1b. RE-APLICAR las etiquetas de cara. Cazado el 2026-08-07
    # integrando compras y entrega: la curaduría de etiquetas parchea las dos
    # COPIAS del grafo, no los archivos de nodo, así que run_phase1 la revierte
    # cada vez que recompila el master desde dataset/nodos/. Sin este paso, una
    # integración devuelve a 71 nodos del core su jerga original ("Canvas",
    # "Pivotar", "SPIN") sin que nada se queje: el grafo queda válido y el
    # usuario ve palabras que el fundador saco de la casa hace una fase.
    #
    # ESTE PASO ES LA UNICA FUENTE DE CURADURIA DE ETIQUETAS. La capa
    # re-aplicable solo es legitima mientras sea unica: si alguien cura una
    # etiqueta en otro sitio (a mano en un nodo, en un script aparte, en el
    # espejo de la web), la proxima recompilacion revive el bug con otro
    # disfraz y ademas nadie sabra cual de las dos curadurias manda. Lo que
    # haya que curar se escribe en dataset/metadata/etiquetas_de_cara_v1*.json
    # y entra por aqui, o no entra.
    paso("e_bis_etiquetas", lambda: correr(
        [sys.executable, "scripts/etiquetas_de_cara.py", "--aplicar"],
        "e-bis. Re-aplicar las etiquetas de cara (run_phase1 las revierte)"))

    # b. familias (sin costo) — DESPUÉS de run_phase1: plan_readiness lee
    # master_graph.json, que recién queda recompilado con el grafo ampliado.
    paso("b_familias", lambda: correr(
        [sys.executable, "engine/plan_readiness.py"],
        "b. Etiquetas de familia (readiness) para el grafo ampliado"))

    # c. caché de preguntas PARCIAL: nodos de packs + cores tocados por puentes.
    # La lista va en un archivo (--patch-file): 1500+ ids exceden el límite de
    # línea de comandos de Windows.
    def _c():
        pack_ids = [p.stem for d in pendientes for p in (BASE / "packs" / d / "nodos").glob("*.json")]
        tocados_core = estado.get("tocados_core", [])
        a_parchear = pack_ids + sorted(tocados_core)
        print(f"\n  caché parcial: {len(pack_ids)} nodos de packs + {len(tocados_core)} cores con sucesores nuevos")
        patch_file = BASE / "engine" / "_patch_pendientes.txt"
        patch_file.write_text("\n".join(a_parchear) + "\n", encoding="utf-8")
        correr(
            [sys.executable, "engine/build_question_cache.py", "--patch-file", str(patch_file)],
            "c. Caché de preguntas parcial (packs + cores tocados)",
        )
        patch_file.unlink(missing_ok=True)
    paso("c_cache_preguntas", _c)

    # d. índice Voyage completo
    paso("d_indice_voyage", lambda: correr(
        [sys.executable, "scripts/build_semantic_index_voyage.py"],
        "d. Índice semántico Voyage completo"))

    # d-bis. LA PRUEBA DE RUMBOS, obligatoria tras CADA reindex.
    # Gate 0 dice que el grafo esta sano; las suites, que el codigo cumple; el
    # vuelo, que el viaje corre. Ninguno dice si la BRUJULA APUNTA BIEN. Un
    # reindex cambia el espacio semantico entero, y una deriva de punteria no
    # rompe nada: manda a la persona equivocada al mundo equivocado, en silencio.
    # Aqui se CANTA contra la linea base committeada.
    paso("d_bis_rumbos", lambda: correr(
        [sys.executable, "scripts/rumbos/prueba_rumbos.py"],
        "d-bis. Prueba de rumbos (la brujula apunta donde debe)"))

    # f. sync de assets a la web + suites
    paso("f_sync", lambda: correr(
        [sys.executable, "scripts/sync_assets_web.py"], "f. Sync de assets a web/lib/assets"))
    # 'run test' (script del package.json), no 'vitest run' bare: pnpm bajo
    # subprocess de Windows mal-parsea el binario suelto ("web" not found).
    paso("f_suite_web", lambda: correr(
        ["pnpm", "-C", "web", "run", "test"],
        "f. Suite web (checksums + contrato) — debe quedar verde"))
    paso("f_suite_python", lambda: correr(
        [sys.executable, "engine/run_all_tests.py"], "f. Suite python — debe quedar verde"))

    # Solo aqui, con TODOS los pasos hechos, desaparece la marca de "a medias".
    ESTADO.unlink(missing_ok=True)

    print(
        "\nLÍNEA DE ENSAMBLAJE COMPLETA. Revisar los costos reales que reportaron "
        "build_question_cache (c) y build_semantic_index_voyage (d) arriba (b es gratis, "
        "clasificador por palabras clave) e incluirlos en el reporte de fase. "
        "Recordar: commit de dataset/ + packs/ + web/lib/assets en el MISMO commit."
    )


if __name__ == "__main__":
    main()
