# -*- coding: utf-8 -*-
"""Prueba comparativa Fase 2.6: repite la sesion real de las macetas de
calcita (misma entrada_original literal, capturada de
engine/sessions/0c66175b.json) contra el motor YA con preguntas adaptadas
por turno + prompt caching real. Corre en vivo (llamadas reales a la API),
persistencia forzada a JSON local para no tocar el proyecto de Supabase
real con una corrida de prueba. Guarda transcripcion completa y el
reporte de costo/cache para comparar contra los $0.1445 originales."""
import io
import json
import os
import sys
import tempfile
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import prototipo_motor as pm

pm.db.forzar_offline(True)

# Respuestas realistas, en el orden en que cubren los mismos temas que el
# perfil_sesion original de esa sesion (calcita/resina/QR/1 persona/ya
# valido con clientes/costos/paralelo resina+QR).
cola_respuestas = [
    "el problema mas urgente es que la resina de la maceta me queda con "
    "burbujas de aire, y aparte el codigo qr que grabo con laser en el "
    "fondo se borra con el tiempo, eso es fatal porque todo mi sistema de "
    "autenticacion depende de que ese qr siga legible",
    "ya regale varios prototipos a conocidos y les encanto, o sea que la "
    "gente si quiere el producto, mi bloqueo no es de demanda sino "
    "tecnico: que la resina y el qr funcionen bien",
    "extraigo la calcita rosa yo mismo de una mina, la proceso a mano en "
    "un tumbler, y hago todo solo, sin equipo ni empleados",
    "no tengo un analisis de costos completo todavia, solo se que hago "
    "todo manual: extraccion, procesamiento y vertido en resina",
    "mi mayor miedo no es que nadie lo compre, sino no poder resolver el "
    "qr y la resina antes de intentar vender en volumen",
    "la resina y el qr estan conectados: si la resina queda con defectos "
    "el qr tambien se ve mal, asi que necesito resolver los dos al mismo "
    "tiempo, no uno primero y el otro despues",
    "quiero probar variando una sola cosa a la vez en la resina para "
    "encontrar la mezcla que no haga burbujas",
    "para el qr estoy pensando en probar otra tecnica de grabado o un "
    "metodo distinto a laser que no se borre con el tiempo",
    "cobro por pieza pero no he calculado bien cuanto me cuesta en "
    "minutos y materiales hacer cada maceta",
    "me gustaria vender primero por una pagina simple mostrando fotos y "
    "el sistema de autenticacion, antes de meterme de lleno con nfts "
    "reales",
]
idx_cola = {"i": 0}
ultimas_respuestas_dadas = []


def leer_entrada_falso(prompt=""):
    print(prompt, end="")
    if "Puedo darte tu plan ahora mismo" in prompt:
        r = ("sigamos, quiero un plan completo que tambien cubra si esto "
             "se sostiene economicamente")
    elif idx_cola["i"] < len(cola_respuestas):
        r = cola_respuestas[idx_cola["i"]]
        idx_cola["i"] += 1
    else:
        r = "creo que ya cubrimos lo esencial, dame mi plan"
    ultimas_respuestas_dadas.append(r)
    print(r)
    return r


pm.leer_entrada = leer_entrada_falso

entrada_original = (
    "mi idea se compone de dos cosas, una parte fisica y la otra digital. "
    "La fisica es hacer macetas de calcita procesada, especialmente "
    "calcita rosa. Las rocas de calcita las extraigo de una mina, luego "
    "las proceso en tumblers que las convierten en semiesferas de calcita "
    "casi pulida, de tamano pequeno. Luego, en un molde vierto resina y "
    "las esferas pequenas ya procesadas. Asi creo las macetas. en la "
    "parte de abajo, le coloco un codigo QR que dirigira al dueno de la "
    "maceta a un NFT que contendra datos del material, diseno, etc. "
    "Entonces este sera el sistema de autenticacion digital por medio de "
    "NFT, que podra guardarlo en su wallet digital. este es un sistema "
    "novedoso y cualquier persona sera capaz de verificar el NFT "
    "autentico por medio del escaner del QR."
)

graph = pm.cargar_grafo()
families = pm.plan_readiness.cargar_families(graph)
entry_seeds = pm.cargar_entry_seeds()
preguntas_cache = pm.cargar_preguntas_cache()

buf = io.StringIO()
with redirect_stdout(buf):
    project_id = pm.db.crear_proyecto(entrada_original)
    db_session_id = pm.db.crear_sesion(project_id, "inicial", entrada_original)
    actual_id, perfil_sesion = pm.clasificar_entrada(entrada_original, entry_seeds, graph)
    print(f"\n(puerta de entrada elegida: {actual_id})")
    session_id = "test26" + pm.uuid.uuid4().hex[:6]
    visitados, ruta, modos = {actual_id}, [actual_id], ["conversado"]
    pm._imprimir_nodo(1, pm.MAX_DEPTH, graph[actual_id], "puerta de entrada", con_resumen=True)

    resultado = pm.ejecutar_recorrido(
        graph, families, preguntas_cache, actual_id, visitados, ruta, modos,
        perfil_sesion, entrada_original, session_id, project_id, db_session_id,
    )
    pm._persistir_resultado(project_id, db_session_id, resultado, graph, families)
    pm.reportar_costo()

transcripcion = buf.getvalue()
out_path = os.path.join(tempfile.gettempdir(), "macetas_fase26_transcript.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(transcripcion)

print(transcripcion)
print("\n\n=== GUARDADO EN:", out_path, "===")
print("=== project_id (offline):", project_id, "===")
