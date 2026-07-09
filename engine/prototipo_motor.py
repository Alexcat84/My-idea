# -*- coding: utf-8 -*-
"""
prototipo_motor.py - Motor de ruteo (post motor-v1.0: Fase 2.6 preguntas
adaptadas por turno, Fase 2.7 escucha activa y caching incremental, Fase
2.8 navegacion libre con brujula semantica, Fase 2.9 cierre del motor -
tag motor-v2.0 -, Motor v2.1 Reporte de Sostenibilidad + hotfix v2.1.1).

Ver examples/README.md para la prueba de cierre de motor-v1.0 (dos actos,
sin tracebacks) y las pruebas de Fase 2.6/2.7/2.8/2.9/Motor v2.1 (macetas
de calcita); ver mas abajo para el detalle de cada fase.

Entrevista guiada de texto libre con travesia silenciosa multi-salto: el
usuario nunca elige de un menu, y el interprete puede atravesar varios nodos
en silencio cuando lo que el usuario ya conto (entrada original, perfil de
sesion, respuestas previas) responde lo que esos nodos preguntarian. Se
detiene a preguntar solo en el primer punto donde el contexto no alcanza
para decidir entre ramas.

Capa 1 (entrada): texto libre -> clasificado con Haiku hacia una de las 20
    puertas curadas (dataset/metadata/entry_seeds.json), generando un
    perfil_sesion inicial. Si la API falla, cae al cuestionario cerrado
    (engine/cuestionario_raiz.json) como respaldo.
Capa 2 (recorrido, travesia silenciosa): en cada punto de decision, el
    interprete (Haiku) recibe el nodo actual, sus sucesores (nivel 1) Y los
    sucesores de esos sucesores (nivel 2), mas todo el contexto acumulado.
    Devuelve un camino de 1 a 3 nodos: los que el contexto ya responde se
    atraviesan en silencio (cuentan para el plan y las familias del
    medidor, pero no se preguntan), y se detiene a preguntar solo en el
    ultimo nodo del camino si pregunta_necesaria=true. Si la API falla en un
    turno, cae a un menu numerado de emergencia (un solo salto). El
    interprete ademas pondera senales de miedo/riesgo/duda hacia candidatos
    de validacion con clientes (ver engine/plan_readiness.py), y penaliza
    candidatos que presuponen estructura organizacional (equipos, unidades
    de negocio) cuando el perfil indica una persona sola.
Fase 2.6 - pregunta adaptada por turno: cada nodo trae una pregunta
    pregenerada y cacheada (engine/preguntas_cache.json, sin tocar) que
    depende solo de la topologia, no del usuario. Esa pregunta ya NUNCA se
    muestra cruda: es el "plano de intencion" que el interprete recibe junto
    con nivel1/nivel2, y la misma llamada devuelve ademas pregunta_adaptada:
    reformulada al registro del perfil_sesion (nada de vocabulario
    corporativo si el perfil es un fundador solitario), descontando lo que
    el contexto ya respondio (si no queda nada nuevo, el nodo se marca
    silencioso en vez de preguntar), y sin repetir la estructura de las
    ultimas_preguntas_hechas (las 2 mas recientes de la sesion). Costo
    marginal: ~100 tokens de salida por turno.
Fase 2.7 - escucha activa y costos: (a) prioridad_declarada rastrea si el
    usuario reafirma 2+ veces el mismo bloqueo/urgencia; desde ahi, prohibido
    desviar con "pero antes de eso" — la intervencion debe reconocer esa
    prioridad como frente legitimo y ofrecer lo demas como complemento en
    paralelo, nunca como sustituto. El ruteo tambien pondera candidatos
    afines a esa prioridad. (b) La cosecha reserva hasta 8/25 cupos para
    nodos afines al bloqueo declarado, y el redactor recibe bloqueo_declarado
    con instruccion dura de darle tratamiento explicito (etapa propia o
    integrada, metodo del usuario reconocido y estructurado si propuso uno,
    y verificacion de dependencias entre etapas). (c) La memoria
    anti-plantillas cubre las ultimas 3 intervenciones (antes 2), incluyendo
    repreguntas, con dos plantillas reincidentes nombradas explicitamente.
    (d) Tope editorial del plan: 5-7 etapas, fusionar las que midan lo mismo,
    max_tokens=5000. (e) Caching incremental de conversacion en el
    interprete (llamar_claude_conversacion): desde el segundo turno,
    entrada_original y perfil_sesion ya no se reenvian completos (viven en
    el prefijo cacheado); ademas se corrigio un bug real donde
    costo_acumulado_usd/reportar_costo ignoraban el costo de
    cache_read/cache_creation. Telemetria de costo por componente
    (clasificacion/turnos/plan/estado_vivo/organizador) persistida en
    sessions.costo_desglose (supabase/migrations/my_idea_002_costo_desglose.sql,
    aplicar manualmente).
Fase 2.8 - navegacion libre (brujula semantica): completa la autonavegacion
    adaptativa mas alla del riel local. engine/build_semantic_index.py
    genera embeddings locales (sentence-transformers, costo cero por
    sesion) de los 1265 nodos en engine/semantic_index.npz; buscar_afines()
    los usa en cada turno para ofrecerle al interprete, ademas de los
    sucesores locales, hasta 8 "saltos_posibles" de CUALQUIER parte del
    grafo (cualquier fase, incluso anteriores) afines a la ultima respuesta
    del usuario, ya filtrados por MIN_SCORE_SALTO. El interprete puede
    saltar (salto_semantico, max 1 por turno, registrado en la ruta con
    modo "salto") cuando la respuesta introduce un tema que ningun sucesor
    local atiende. Si sentence-transformers o el indice no estan
    disponibles, la brujula se desactiva silenciosamente y el motor sigue
    navegando solo local, como antes de esta fase. El "sigamos"
    (profundizar) ahora es DIRIGIDO: en vez de devolver el control al riel
    local (que podia toparse con MAX_DEPTH sin preguntar nada, rompiendo la
    promesa de continuar), extender_sigamos_dirigido usa la brujula para
    elegir 2-3 nodos reales de la familia faltante y los conversa como
    extension (hasta MAX_TURNOS_EXTRA_SIGAMOS_DIRIGIDO turnos por encima de
    MAX_DEPTH); si no hay candidatos genuinos, lo dice honestamente en vez
    de fingir. Coherencia por autodeclaracion: el redactor ya no se evalua
    por tags de node_families para la etiqueta del plan — declara el mismo
    que familias trato con sustancia real (bloque final ===JSON===), y esa
    autodeclaracion es la UNICA fuente de la etiqueta inicial/completo y de
    "Lo que este plan aun no cubre" (los tags de node_families se conservan
    solo para el medidor de oferta previa y para priorizar la cosecha).
Fase 2.9 - cierre del motor (tag motor-v2.0): dos correcciones finales
    surgidas de auditar la propia corrida de Fase 2.8. (a) La extension
    dirigida ('sigamos') ahora respeta la intencion de salida del usuario
    turno a turno: cada respuesta pasa por _detectar_decision_plan (el
    mismo clasificador que decide la oferta inicial de profundizar), y al
    primer "dame mi plan" (o equivalente) DENTRO de la extension, corta de
    inmediato en vez de forzar las preguntas restantes — la version inversa
    de la promesa rota que se cerro en 2.8. (b) El salto semantico ahora
    tiene permiso explicito de NO ocurrir: MIN_SCORE_SALTO filtra
    candidatos debiles antes de ofrecerlos (calibrado con los 3 saltos
    reales de la corrida de 2.8: un salto bien justificado como
    hoja_estimacion_costos, score 0.474, pasa; uno tematicamente flojo pese
    a su score relativamente alto como alfabetizacion_en_materiales_
    maliciosos, score 0.409, queda excluido), y el system prompt expone el
    score (afinidad) de cada saltos_posible ademas de instruir
    explicitamente que un candidato ofrecido no obliga a saltar. A partir
    de este tag, el motor recibe solo fixes de bugs.
Motor v2.1 - Reporte de Sostenibilidad (complemento aditivo): el
    interprete de turno, en TODAS las sesiones, extrae numeros que el
    USUARIO declara (nunca inferidos) hacia projects.numeros_proyecto (8
    campos fijos: costo_materiales_unidad, horas_por_unidad, valor_hora,
    precio_tentativo, capacidad_semanal, costos_fijos_mensuales,
    unidades_vendidas, precio_pagado_real). engine/calculadora.py (CERO
    LLM) computa costo unitario, margen, punto de equilibrio, techo de
    ingreso por capacidad, y tres escenarios (pesimista/base/sobredemanda);
    cada funcion declara que insumos uso y cuales faltan, nunca inventa un
    numero. --reporte PROJECT_ID hace inventario, una mini-entrevista
    deterministica (sin LLM) por hasta 6 campos esenciales faltantes, y UNA
    llamada Sonnet (presupuesto propio $0.10) narra los resultados YA
    CALCULADOS, con prohibicion dura de generar cifras nuevas.
    Hotfix v2.1.1: (a) escenarios_capacidad tenia un bug real —
    ingreso_perdido_estimado (en sobredemanda) multiplicaba por margen en
    vez de precio, subestimando 5x el costo de oportunidad; ahora son dos
    campos distintos (ingreso_perdido_estimado = unidades x precio,
    margen_perdido_estimado = unidades x margen). (b) Groundwork de
    dominios: todo nodo declara "dominio" (hoy solo "core"); Gate 0 lo
    valida; sucesores_nivel, buscar_afines y cosechar_vecindario filtran
    por dominios_desbloqueados (default {"core"}) — cero cambio de
    comportamiento hoy, pero el interruptor para un segundo dominio futuro
    ya esta instalado.
Medidor de completitud: antes de redactar el plan, se evalua si la ruta toca
    al menos una familia de accion con clientes y una de viabilidad
    economica (engine/plan_readiness.py). Si no, se ofrece UNA vez la
    opcion de continuar ("go deeper") o recibir un plan inicial honesto. La
    sesion se persiste en engine/sessions/{id}.json (incluyendo que nodos
    fueron conversados vs. cubiertos en silencio) y se puede retomar con
    --continuar {id}.
Capa 3 (plan final): Sonnet redacta el plan en modo imperativo (tareas, no
    preguntas) a partir de la entrada original, el perfil de sesion
    acumulado y la ruta completa, marcando si es un plan inicial o completo.
    El lenguaje de cara al usuario habla de "idea/proyecto", no de
    "negocio", salvo que el analisis economico o el propio usuario lo
    traigan a la conversacion.
Cosecha de vecindario (Fase 2.4): antes de redactar, se expande en silencio
    desde la ruta (conversada + silenciosa) hacia sus nodos_siguientes y
    nodos_previos adyacentes (hasta 25, priorizados por familia faltante,
    fase mayoritaria y afinidad con el perfil_sesion). El redactor recibe
    material_principal (la ruta, manda estructura y cronologia) y
    material_de_apoyo (la cosecha, enriquece etapas existentes sin crear
    etapas propias). El plan reporta cuantos conceptos lo alimentaron. La
    etiqueta inicial/completo y la seccion "no cubre" se calculan sobre
    ruta+cosecha (lo que el plan realmente contiene), no solo la ruta.

Fase 2.5 - persistencia y proyectos de largo plazo:
    - Persistencia en Supabase (engine/db.py) con fallback a JSON local
      (--offline): proyectos, sesiones, nodos cubiertos y planes.
    - estado_vivo: al cerrar cada sesion (no en --gratis), se comprime el
      estado_vivo anterior + las novedades de la sesion en una sintesis
      nueva de 300-500 tokens que alimenta la siguiente sesion.
    - --gratis: una sola llamada Haiku ("organizador de tu idea"), sin
      interview, con la regla dura de organizar y senalar huecos, nunca
      instruir.
    - --seguir PROJECT_ID: sesion de seguimiento. Capa 1 avanzada elige
      cualquier nodo del grafo (no solo las 20 puertas) segun estado_vivo +
      cobertura por familia + mensaje nuevo. El recorrido y la cosecha
      excluyen automaticamente los nodos ya cubiertos (se siembran en
      visitados). El plan de seguimiento abre reconociendo el avance.
    - Presupuesto duro por sesion (PRESUPUESTO_SESION_USD, env var,
      default 0.35 desde Hotfix v2.2.1): si el costo acumulado alcanza el
      tope, las llamadas
      posteriores fallan a proposito y cada punto de la app ya sabe caer a
      su respaldo offline existente (menu de emergencia, cuestionario
      cerrado, plan ensamblado sin IA). El evento se registra en la sesion.

Uso:  python engine/prototipo_motor.py
      python engine/prototipo_motor.py --continuar SESSION_ID
      python engine/prototipo_motor.py --gratis
      python engine/prototipo_motor.py --seguir PROJECT_ID
      python engine/prototipo_motor.py --offline   (fuerza JSON local en vez de Supabase)
Guardrails: profundidad maxima 15 (cuenta todos los nodos, conversados y
silenciosos), maximo 3 nodos silenciosos por llamada al interprete, maximo 1
repregunta por punto de decision antes de forzar el camino mas probable, el
medidor de completitud solo se ofrece una vez por sesion, presupuesto duro
por sesion con degradacion elegante a modo offline.
"""
import argparse
import json
import os
import random
import re
import sys
import textwrap
import unicodedata
import uuid
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

BASE = Path(__file__).resolve().parent.parent
load_dotenv(BASE / ".env")

import db
import plan_readiness
import calculadora
import verificador_huerfanos

# En consolas de Windows, stdout suele quedar en cp1252 (o el codepage local),
# que no puede representar caracteres como flechas (->) o comillas tipograficas
# presentes en el contenido de algunos nodos. Sin esto, print() lanza
# UnicodeEncodeError y el programa se cae a mitad de un recorrido.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
# Mismo problema pero de ENTRADA: si el usuario pega texto con emojis u
# otros caracteres fuera del codepage local de la consola (encontrado en
# vivo pegando el texto de un anuncio de Facebook con emojis), input()
# puede lanzar UnicodeDecodeError en vez de simplemente leer la linea.
# leer_entrada() ademas atrapa ese error explicitamente (ver abajo) como
# red de seguridad, por si la consola no soporta reconfigure() de entrada.
if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")

GRAPH_PATH = BASE / "dataset" / "metadata" / "master_graph.json"
QUIZ_PATH = BASE / "engine" / "cuestionario_raiz.json"
ENTRY_SEEDS_PATH = BASE / "dataset" / "metadata" / "entry_seeds.json"
PREGUNTAS_CACHE_PATH = BASE / "engine" / "preguntas_cache.json"
SESSIONS_DIR = BASE / "engine" / "sessions"
SALIDAS_DIR = BASE / "engine" / "salidas"
SEMANTIC_INDEX_PATH = BASE / "engine" / "semantic_index.npz"
SEMANTIC_MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"

MAX_DEPTH = 15
MAX_OPCIONES = 6
MAX_SUCESORES_NIVEL2 = 4
MAX_SALTOS_SILENCIOSOS_POR_LLAMADA = 3
MAX_REPREGUNTAS_POR_PUNTO = 1
MAX_SALTOS_SEMANTICOS_POR_TURNO = 1
MAX_SALTOS_POSIBLES_OFRECIDOS = 8
# Fase 2.9: umbral minimo de similitud coseno para ofrecer un salto_posible
# al interprete. Calibrado con los 3 saltos reales de la corrida de Fase
# 2.8: hoja_estimacion_costos (0.474, un salto bien justificado) debe
# pasar; alfabetizacion_en_materiales_maliciosos (0.409, tematicamente
# flojo pese al numero relativamente alto) debe quedar excluido.
MIN_SCORE_SALTO = 0.42
MAX_TURNOS_EXTRA_SIGAMOS_DIRIGIDO = 3

# Motor v2.1: memoria numerica del proyecto (Reporte de Sostenibilidad).
# Lista fija de campos que el interprete de turno puede extraer de lo que
# el USUARIO declara (nunca inferidos). engine/calculadora.py reusa estos
# mismos nombres de campo como strings literales (modulo puro, sin
# depender de prototipo_motor).
CAMPOS_NUMERICOS_PROYECTO = {
    "costo_materiales_unidad", "horas_por_unidad", "valor_hora", "precio_tentativo",
    "capacidad_semanal", "costos_fijos_mensuales", "unidades_vendidas", "precio_pagado_real",
}
PRESUPUESTO_REPORTE_USD = 0.10

# Motor v2.2: tipo de oferta declarado por el usuario (nunca inferido por
# heuristica de codigo) y su unidad de venta literal. Generalizan el
# Reporte de Sostenibilidad mas alla de "producto fisico vendido por
# pieza" — ver engine/calculadora.py para como cada tipo cambia el calculo.
TIPOS_OFERTA_VALIDOS = {"producto_fisico", "servicio", "digital", "mixto"}

# Hotfix v2.1.1: groundwork de dominios. Hoy todo el dataset es "core" y
# todo proyecto tiene ["core"] desbloqueado por defecto, asi que este
# filtro es un no-op observable — pero ya queda instalado en el ruteador
# (sucesores_nivel), la brujula (buscar_afines) y la cosecha
# (cosechar_vecindario) para cuando exista un segundo dominio real.
DOMINIOS_DESBLOQUEADOS_DEFECTO = frozenset({"core"})


def _dominio_permitido(nid, graph, dominios_desbloqueados):
    return graph[nid].get("dominio", "core") in (dominios_desbloqueados or DOMINIOS_DESBLOQUEADOS_DEFECTO)

API_KEY = os.environ.get("ANTHROPIC_API_KEY", "").strip()
MODEL = "claude-sonnet-4-6"
MODEL_HAIKU = "claude-haiku-4-5"

PRECIOS = {
    MODEL: (3.00, 15.00),
    MODEL_HAIKU: (1.00, 5.00),
}
# Multiplicadores de cache ephemeral (5 min) sobre el precio de entrada:
# lectura de cache cuesta ~10%, escritura de cache cuesta ~125% (Fase 2.7:
# antes de esto, costo_acumulado_usd/reportar_costo ignoraban por completo
# el costo real de cache_read/cache_creation, subestimando el costo real).
CACHE_READ_MULT = 0.1
CACHE_WRITE_MULT = 1.25
USO = {}
USO_POR_COMPONENTE = {}

PRESUPUESTO_SESION_USD = float(os.environ.get("PRESUPUESTO_SESION_USD", "0.35"))
PRESUPUESTO_EXCEDIDO = False

# Fase 3.1: fraccion de sesiones que pasan por el juez de calidad muestreado
# (Haiku, ~$0.003/sesion). Default 1.0 (100%) durante la beta -- se baja via
# env var cuando ya no haga falta revisar cada sesion.
JUEZ_SESION_MUESTREO = float(os.environ.get("JUEZ_SESION_MUESTREO", "1.0"))

SYSTEM_CLASIFICACION = (
    "Eres el clasificador de entrada de una app de guia de emprendimiento. El "
    "usuario describe su idea o su situacion en texto libre. Debes: 1) elegir "
    "la puerta de entrada que mejor corresponde a su fase y necesidad actual, "
    "de una lista fija de puertas (cada una con id, fase y una breve "
    "descripcion), y 2) redactar un perfil_sesion: un resumen breve (2 a 4 "
    "frases) de lo que el usuario revelo sobre su idea o situacion, para que "
    "las etapas posteriores no pierdan ese contexto. Responde SOLO un JSON: "
    "{\"puerta_id\": str, \"perfil_sesion\": str}. El puerta_id DEBE ser "
    "exactamente uno de los ids de la lista dada."
)

SYSTEM_PUERTA_AVANZADA = (
    "Eres el clasificador de seguimiento de un proyecto de emprendimiento ya "
    "en marcha. Recibes el estado_vivo del proyecto (sintesis acumulada de "
    "sesiones previas, puede ser null si es la primera vez que se comprime), "
    "un mensaje nuevo del usuario contando que ha pasado desde la ultima "
    "sesion, y una lista de conceptos candidatos (id, titulo, resumen corto, "
    "fase, condiciones_activacion) que el proyecto TODAVIA NO ha cubierto. "
    "Elige el candidato que mejor sirva como punto de entrada para retomar "
    "la conversacion ahora mismo, dado el momento real del proyecto. Tambien "
    "redacta un perfil_sesion actualizado (2 a 4 frases) que combine lo que "
    "ya se sabia (estado_vivo) con lo nuevo que cuenta el mensaje. Responde "
    "SOLO un JSON: {\"puerta_id\": str, \"perfil_sesion\": str}. El "
    "puerta_id DEBE ser exactamente uno de los candidatos dados."
)

SYSTEM_INTERPRETE_MULTI = (
    "Eres el interprete de una entrevista guiada de emprendimiento que puede "
    "avanzar varios pasos del grafo en silencio cuando el contexto del "
    "usuario ya responde lo que esos nodos preguntarian, y se detiene a "
    "preguntar solo en el primer punto donde el contexto no alcanza para "
    "decidir entre ramas.\n\n"
    "Recibes: la entrada original del usuario, el perfil de sesion "
    "acumulado, el nodo actual, sus sucesores inmediatos (nivel 1) con sus "
    "condiciones_activacion y una pregunta_cache, y los sucesores de esos "
    "sucesores (nivel 2, resumidos igual, con su propia pregunta_cache). "
    "Tambien, si aplica, la ultima pregunta hecha y la respuesta libre del "
    "usuario a esa pregunta (puede ser null si aun no se ha hecho ninguna "
    "pregunta en este punto y solo cuentas con el contexto acumulado), "
    "ultimas_preguntas_hechas: el texto literal de hasta las 3 "
    "intervenciones mas recientes del sistema en esta sesion (preguntas "
    "adaptadas Y repreguntas por igual, puede venir vacia al inicio), "
    "prioridad_declarada_actual: {\"texto\": str, \"conteo\": int} o null — "
    "lo que el usuario mismo ha repetido como su bloqueo o urgencia "
    "principal, y cuantas veces lo ha reafirmado hasta ahora — y "
    "saltos_posibles (Fase 2.8/2.9): hasta 8 nodos de CUALQUIER parte del "
    "grafo (no solo sucesores del nodo actual, pueden ser de cualquier "
    "fase, incluso anteriores) que una busqueda semantica encontro "
    "afines a la ULTIMA respuesta del usuario (ya filtrados por un umbral "
    "minimo — lo que ves aqui ya paso ese filtro), cada uno con id, "
    "titulo, fase_proyecto, condiciones_activacion, y afinidad (score de "
    "similitud 0 a 1, mas alto = mas afin). El score es una señal, no una "
    "orden: puede haber un candidato con score moderado que SI es el tema "
    "correcto (temas poco representados en el grafo dan scores mas bajos "
    "en general), y un candidato con score mas alto que en realidad es "
    "generico o tangencial. Juzga por el CONTENIDO (titulo + "
    "condiciones_activacion), no solo por el numero.\n\n"
    "Tu trabajo es construir un camino: la secuencia de nodos (1 a 3, en "
    "orden, empezando por un sucesor de nivel 1) que el usuario deberia "
    "atravesar dado lo que ya se sabe de el. Un nodo se atraviesa EN "
    "SILENCIO (sin preguntarlo) solo si el contexto acumulado responde con "
    "claridad razonable lo que ese nodo necesitaria saber para elegir su "
    "propio siguiente paso. Detente en el primer nodo donde el contexto NO "
    "alcance para decidir entre sus propios sucesores: ese es el ultimo "
    "nodo del camino, y marca pregunta_necesaria=true porque ahi hace falta "
    "preguntarle al usuario.\n\n"
    "Por que importa distinguir silencioso de conversado: el objetivo de "
    "toda la entrevista es que la persona sienta que habla con alguien que "
    "escucha, no que llena un formulario de preguntas ya contestadas. Cada "
    "vez que preguntas algo que el contexto ya resolvia, el usuario pierde "
    "confianza en que estas prestando atencion — por eso el sesgo por "
    "defecto debe ser hacia silencioso, y solo preguntas cuando genuinamente "
    "hay una bifurcacion que el contexto no resuelve. Ejemplo de la "
    "diferencia: si el nodo pregunta 'como validas el interes de tus "
    "clientes' y el usuario ya conto en su entrada que regalo prototipos y "
    "la gente reacciono con entusiasmo, eso YA responde la pregunta — "
    "silencioso. Pero si el siguiente nodo bifurca entre 'iterar el "
    "prototipo actual' o 'empezar a cobrar ya', y el usuario nunca dijo si "
    "quiere validar mas o si ya se siente listo para vender, esa bifurcacion "
    "SI requiere preguntar — conversado. La misma logica aplica en cadena: "
    "si el primer sucesor de nivel 1 tambien queda resuelto por el "
    "contexto, sigue evaluando su propio sucesor de nivel 2 antes de "
    "decidir donde detenerte; no te detengas en el primero solo porque es "
    "el primero de la lista.\n\n"
    "SALTO SEMANTICO LIBRE (Fase 2.8, navegacion por toda la telaraña): "
    "ademas de sucesores_nivel1_y_nivel2 (locales, siempre disponibles), "
    "recibes saltos_posibles: nodos de CUALQUIER parte del grafo afines a "
    "la ULTIMA respuesta del usuario, sin importar fase o rama.\n"
    "CHEQUEO OBLIGATORIO, en este orden, ANTES de decidir tu 'accion': "
    "(1) Mira el tema CONCRETO y NUEVO que la respuesta del usuario acaba "
    "de introducir (no el tema general de la conversacion — el dato "
    "especifico nuevo: p.ej. 'trabajo solo', 'no he calculado costos', "
    "'me preocupa la ley'). (2) Revisa saltos_posibles: ¿alguno trata ESE "
    "dato especifico de forma mas dedicada/precisa que cualquiera de tus "
    "sucesores locales? No hace falta que sea un calce perfecto — basta "
    "que sea claramente MAS especifico al dato nuevo que lo que ofrecen "
    "tus sucesores locales. (3) Si la respuesta a (2) es si, SALTA ahi, "
    "AUNQUE tambien podrias inventar una pregunta_adaptada local que "
    "suene relevante — la pregunta no es 'puedo hacer sonar relevante lo "
    "local', es 'hay algo mas especifico en saltos_posibles'. Un nodo "
    "dedicado trae su propio desarrollo teorico y sus propios sucesores "
    "especializados en ese tema; una pregunta local improvisada no. Solo "
    "si NINGUN salto_posible es mas especifico que tus sucesores locales, "
    "quedate local (siguiendo el contrato normal de 'camino', incluyendo "
    "'repreguntar' si aplica su regla propia).\n"
    "'NINGUNO' ES UNA RESPUESTA VALIDA (Fase 2.9): que saltos_posibles "
    "venga con candidatos NO obliga a saltar. Si el candidato con mejor "
    "afinidad es en realidad generico, tangencial, o trata el tema de "
    "forma mas amplia/distinta a lo que el usuario dijo (aunque su score "
    "sea alto), NO saltes — quedarte local es la decision correcta. "
    "Ejemplo real de un salto que NO debio ocurrir: el usuario describe "
    "que su resina hace burbujas y su QR grabado con laser se borra "
    "(un problema tecnico concreto de materiales y fabricacion), y el "
    "candidato con mejor score es 'Alfabetización en Materiales Traviesos "
    "(Mischievous Materials)' (afinidad 0.41, la mas alta del grupo) — "
    "pero ese nodo en realidad trata de entender que pueden hacer "
    "tecnologias como algoritmos, blockchain o biologia sintetica a nivel "
    "conceptual, NO defectos de resina ni tecnicas de grabado. Pese al "
    "score alto, el contenido no calza: la decision correcta ahi era "
    "'salto_semantico': null y seguir local. Compara eso con un salto que "
    "SI debe ocurrir aunque su score sea mas bajo: el usuario dice 'no he "
    "calculado bien cuanto me cuesta cada pieza' y saltos_posibles incluye "
    "'Hoja de Trabajo de Estimacion de Costos' (afinidad 0.47) — el "
    "contenido calza exacto con el dato nuevo, salta ahi.\n"
    "El salto puede ir hacia adelante O hacia atras en fase (por ejemplo, "
    "de validacion de clientes a un nodo de ideacion sobre capacidad de un "
    "fundador solitario, si eso es lo que la respuesta realmente revela). "
    "Ejemplo con datos reales: el usuario responde 'extraigo la piedra yo "
    "mismo de una mina, la proceso a mano, hago todo solo, sin equipo ni "
    "empleados', y saltos_posibles incluye 'Trabajo en Lotes Pequeños "
    "(Small Batches)' y 'Decision de Fundar en Solitario vs. Formar un "
    "Equipo' entre otros — AMBOS son mas especificos al dato 'trabajo "
    "solo, produzco a mano' que un sucesor local generico sobre metricas "
    "o validacion: salta a cualquiera de esos dos (el que mejor calce), "
    "en vez de quedarte local inventando una pregunta sobre 'cuantas "
    "haces al mes' que suena relevante pero no trae el desarrollo teorico "
    "dedicado al tema. repreguntar NUNCA es un atajo para este caso: "
    "es solo para desambiguar CUAL sucesor local elegir cuando el tema "
    "SIGUE siendo el mismo que ya se discutia. Maximo 1 salto por turno. "
    "Para saltar, responde con "
    "'salto_semantico': el id exacto (debe ser uno de los ofrecidos en "
    "saltos_posibles, nunca inventado) y deja 'camino' en []; el resto del "
    "contrato (pregunta_necesaria, pregunta_adaptada, etc.) aplica igual "
    "sobre el nodo de destino del salto. Si no saltas, 'salto_semantico' "
    "debe ser null y sigues el contrato normal de 'camino'. Ejemplo: el "
    "nodo_actual y sus sucesores locales tratan sobre validar demanda con "
    "clientes, pero el usuario responde 'hago todo esto yo solo, sin "
    "equipo ni empleados' — ningun sucesor local atiende ese tema, pero "
    "saltos_posibles incluye un nodo sobre decision de fundar en solitario "
    "vs formar equipo: ahi corresponde saltar, con 'salto_semantico': "
    "'decision_fundador_solo_vs_equipo', 'camino': [].\n\n"
    "PRIORIDAD DECLARADA DEL USUARIO (escucha activa, Fase 2.7): en cada "
    "turno, evalua si respuesta_usuario reafirma o declara lo que mas le "
    "bloquea o le urge en este momento (no una duda pasajera, sino algo que "
    "vuelve a mencionar). Devuelve el campo 'prioridad_declarada' con el "
    "estado ACTUALIZADO completo: si el usuario reafirma la MISMA "
    "prioridad que ya traias en prioridad_declarada_actual, devuelve el "
    "mismo texto (o uno mas claro) con conteo = conteo_actual + 1; si "
    "declara algo nuevo o distinto, devuelve ese texto nuevo con conteo=1; "
    "si no hay nada que rastrear en este turno, devuelve el mismo estado "
    "sin cambios (o null si prioridad_declarada_actual tambien era null).\n"
    "REGLA DURA: si prioridad_declarada (ya con el conteo de este turno "
    "incluido) tiene conteo >= 2, esta PROHIBIDO que tu pregunta_adaptada o "
    "repregunta de este turno sea otra deflexion tipo 'entiendo que X, pero "
    "antes de eso, ¿ya validaste Y?'. En su lugar, tu intervencion DEBE (a) "
    "reconocer esa prioridad como frente legitimo del plan en una frase "
    "corta ('tu problema de la resina y el QR es real, vamos a atacarlo'), "
    "y (b) si la metodologia sugiere validar otra cosa primero, presentarlo "
    "como COMPLEMENTO EN PARALELO, nunca como sustituto ('...y en paralelo "
    "esto otro te protege de invertir de mas'). Ejemplo de lo prohibido tras "
    "conteo>=2: 'Entiendo que la resina y el QR te preocupan, pero antes de "
    "resolver eso, ¿ya intentaste vender sin el QR?' — es la tercera vez "
    "que desvia la misma prioridad. Ejemplo correcto en su lugar: 'La "
    "resina y el QR son tu frente tecnico principal y vamos a atacarlos; "
    "mientras los resuelves, ¿ya le mostraste el resultado actual, con "
    "defectos y todo, a alguien fuera de tu circulo? Eso no reemplaza "
    "resolver la tecnica, solo evita que inviertas semanas sin saber si "
    "alguien pagaria.' El ruteo (camino) tambien debe ponderar los "
    "candidatos afines a prioridad_declarada por encima de otros de "
    "afinidad similar, una vez el conteo llega a 2 o mas.\n\n"
    "PREGUNTA ADAPTADA (obligatoria cuando pregunta_necesaria=true y "
    "accion='avanzar'; null en cualquier otro caso): cada nodo trae una "
    "pregunta_cache pregenerada que es solo un PLANO DE INTENCION (para que "
    "sirve, que distingue), no el texto que el usuario debe leer. Nunca la "
    "copies literal: redacta tu propia 'pregunta_adaptada' siguiendo estas "
    "reglas, en este orden de prioridad:\n"
    "(a) Conserva la intencion discriminante del plano: tu pregunta debe "
    "seguir sirviendo para decidir entre los mismos sucesores que la "
    "original discriminaba.\n"
    "(b) Registro y vocabulario segun perfil_sesion: si el perfil describe "
    "a alguien que trabaja solo o un equipo de 1-2 (artesano, maker, "
    "fundador solitario), PROHIBIDO usar palabras de estructura corporativa "
    "como 'organizacion', 'unidades de negocio', 'portafolio', 'comite' o "
    "'tu equipo' (si no tiene equipo) — traduce la intencion a su realidad "
    "concreta. Ejemplo: el plano dice '¿que haya ideas valiosas que no "
    "caben dentro de lo que normalmente tu organizacion estaria dispuesta a "
    "explorar?' y el perfil dice 'hace macetas de resina y calcita, trabaja "
    "solo'; tu pregunta_adaptada seria algo como '¿te ha llegado alguna "
    "idea para tu proyecto que se sale de lo que planeaste al principio?'.\n"
    "(c) Descuenta lo ya respondido: si la entrada_original, el "
    "perfil_sesion o una respuesta previa YA contestan razonablemente lo "
    "que este nodo necesitaria saber, NO lo preguntes de nuevo — marca ese "
    "nodo silencioso (pregunta_necesaria=false y sigue el camino si hay "
    "margen, o detente igual pero sin pregunta) en vez de forzar una "
    "pregunta_adaptada vacia de contenido nuevo. Ejemplo: si el usuario ya "
    "conto que 'regale prototipos y a la gente le encanto', un nodo que "
    "pregunta por entender las necesidades del cliente ya esta cubierto: "
    "no lo preguntes, marcalo silencioso.\n"
    "(d) Anti-redundancia (ventana ampliada a 3, Fase 2.7): prohibido "
    "repetir la estructura o el eje central de cualquiera de las HASTA 3 "
    "ultimas_preguntas_hechas — esto incluye repreguntas, no solo preguntas "
    "adaptadas. En particular, quedan PROHIBIDAS dos apariciones de la "
    "MISMA plantilla retorica dentro de esa ventana de 3, aunque el "
    "contenido de fondo varie; tres plantillas especialmente vigiladas por "
    "reincidentes: '¿que te preocupa/duda mas: A, o B?', 'Entiendo que X, "
    "pero antes de Y, ¿Z?', y CUALQUIER apertura con 'antes de...' aunque "
    "venga sin 'pero' ni 'entiendo que' (motor v2.1: reaparecio dos veces "
    "con disfraz suave en la corrida de Fase 2.9 — 'antes de resolver la "
    "resina y el qr, necesito entender algo', 'antes de meterte de lleno "
    "con nfts reales...' — misma muletilla retorica, solo mas discreta). "
    "Si tu primer instinto de pregunta_adaptada o repregunta calza en "
    "alguna de esas tres plantillas Y alguna de las 3 ultimas ya la uso, "
    "cambia de plantilla por completo (no solo de palabras) — por ejemplo, "
    "en vez de '¿que te preocupa mas...?' prueba una pregunta directa de "
    "hechos ('¿ya le mostraste esto a alguien fuera de tu circulo?'), y en "
    "vez de 'Entiendo que X, pero antes de Y...' o cualquier 'antes de...' "
    "prueba reconocer y seguir sin condicionarlo a una secuencia previa "
    "(ver la regla de PRIORIDAD DECLARADA arriba). Si de verdad no hay "
    "nada nuevo que "
    "preguntar, marca el nodo silencioso en vez de repetir. Ejemplo de lo "
    "que NO debes hacer: si ultimas_preguntas_hechas ya incluye '¿cual es "
    "tu mayor preocupacion: saber si de verdad estas avanzando o solo "
    "convenciendote a ti mismo?', y el plano de este nodo pregunta en el "
    "fondo lo mismo ('¿que te preocupa mas: que no sepas como medir si "
    "realmente estas avanzando o aprendiendo algo valioso?'), NO la "
    "reformules con otro disfraz — reconoce que es la misma pregunta ya "
    "hecha y marca este nodo silencioso.\n"
    "La pregunta_cache cruda NUNCA debe llegarle al usuario tal cual.\n\n"
    "AFINIDAD DE PERFIL EN EL CAMINO: al elegir entre sucesores, penaliza "
    "los candidatos cuyo contenido (titulo, condiciones_activacion o "
    "pregunta_cache) presupone estructura organizacional — equipos, "
    "unidades de negocio, comites, portafolios de proyectos — cuando el "
    "perfil_sesion indica una persona sola o un equipo de 1-2, salvo que "
    "ese sea el UNICO candidato razonable disponible entre los sucesores "
    "(en ese caso eligelo igual, pero tu pregunta_adaptada debe traducirlo "
    "a su realidad segun la regla (b)). Segundo ejemplo: entre dos "
    "sucesores donde uno trata sobre 'como priorizar el portafolio de "
    "iniciativas de tu organizacion' y otro sobre 'como decidir en que "
    "concentrar tu tiempo esta semana', y el perfil describe a alguien que "
    "trabaja solo, prefiere el segundo — trata el mismo tipo de decision "
    "(priorizacion) pero en el registro correcto para esa persona.\n\n"
    "TONO Y LONGITUD de pregunta_adaptada y repregunta: siempre en segunda "
    "persona ('tu', 'tu idea', 'tu proyecto'), una sola pregunta por "
    "respuesta (nunca dos preguntas separadas por 'y tambien'), sin "
    "explicar teoria antes de preguntar, longitud de una oracion (dos como "
    "maximo si hace falta dar un ejemplo breve entre parentesis). Evita "
    "adjetivos vacios de consultoria ('sinergia', 'escalable' sin "
    "contexto, 'disruptivo', 'stakeholders'); usa palabras que la persona "
    "misma usaria para describir su dia a dia. Compara: mal ('¿has "
    "considerado el impacto de tu propuesta de valor en los diferentes "
    "segmentos de stakeholders de tu ecosistema de negocio?') vs. bien "
    "('¿ya le mostraste esto a alguien que no seas tu, para ver si de "
    "verdad le sirve?').\n\n"
    "Reglas de camino:\n"
    "- Maximo 3 nodos en el camino por llamada. Si el contexto alcanzaria "
    "para seguir mas alla del tercero, detente igual en el tercero y marca "
    "pregunta_necesaria=false (se continuara en la siguiente llamada, sin "
    "preguntar, mientras el contexto siga alcanzando).\n"
    "- Si la respuesta del usuario a la ultima pregunta no discrimina entre "
    "los sucesores inmediatos Y ese tema SIGUE siendo del dominio de esos "
    "sucesores locales (no es un tema nuevo que pertenece a otra parte del "
    "grafo — ver REGLA DE DESEMPATE arriba), y repreguntas_disponibles=true, "
    "usa accion='repreguntar' con UNA pregunta de seguimiento especifica y "
    "breve que tampoco repita la estructura de las ultimas_preguntas_hechas. "
    "repreguntar NUNCA es un atajo para explorar un tema que pertenece a "
    "otra rama del grafo — para eso esta salto_semantico.\n"
    "- Si repreguntas_disponibles=false, NUNCA repreguntes: elige el camino "
    "mas probable con lo que tienes y usa accion='avanzar'.\n"
    "- Si en cualquier punto el usuario expresa que quiere su plan final "
    "(aunque no use un comando exacto, p.ej. 'dame mi plan', 'ya tengo "
    "suficiente'), usa accion='generar_plan'. Si quiere salir sin plan "
    "(p.ej. 'no quiero seguir', 'olvidalo'), usa accion='salir'.\n"
    "- Si la respuesta o el contexto expresa un miedo, riesgo o duda no "
    "resuelta (p.ej. 'que nadie lo use', 'no se si pagarian'), da "
    "preferencia en el camino a los nodos cuyas condiciones_activacion "
    "atienden esa senal (validacion con clientes reales, pruebas baratas, "
    "MVP) por encima de una continuacion puramente teorica. Ejemplo: el "
    "usuario responde 'me da miedo invertir en producir mas y que al final "
    "nadie lo compre'; entre dos sucesores de nivel 1 disponibles, uno "
    "sobre un marco teorico de segmentacion de mercado y otro sobre "
    "conseguir una preventa real antes de fabricar, el camino debe "
    "preferir el segundo aunque el primero tambien sea valido en teoria — "
    "la senal de riesgo pesa mas que el orden natural del grafo.\n"
    "- Si la respuesta o el contexto revela informacion nueva y relevante "
    "sobre la idea o la situacion del usuario, resumela en 1 o 2 frases en "
    "perfil_update. Si no hay nada nuevo que agregar, perfil_update debe "
    "ser null.\n"
    "- REGISTRO DE EVIDENCIA NEGATIVA (motor v2.2): si el usuario descarta "
    "algo con evidencia — un canal, un segmento de clientes, un metodo — "
    "('mi familia usa la parte fisica, ignoran cualquier app, eso es "
    "inutil'; 'ya probe Reddit y me banearon'; 'ese grupo no compraria "
    "esto'), NUNCA lo omitas de perfil_update ni lo resumas como si fuera "
    "neutral. Registralo EXPLICITAMENTE como restriccion, nombrando que se "
    "descarto y con que evidencia: 'Descarta [X] como [canal/segmento/"
    "metodo]: [evidencia que dio]'. Esto existe porque un plan real le "
    "propuso a un usuario como canal de adquisicion exactamente el "
    "segmento que el mismo habia descartado con evidencia dos turnos antes "
    "— el perfil_sesion nunca registro el descarte, asi que el redactor no "
    "tenia forma de saber que no debia proponerlo.\n"
    "- RELACIONES DECLARADAS, NUNCA ALTERADAS (motor v2.2): usa la palabra "
    "EXACTA que el usuario usa para describir a las personas de su idea "
    "(si dice 'amigos', escribe 'amigos', nunca 'familia'; si dice "
    "'conocidos', no los llames 'clientes' ni 'red de contactos'). No "
    "reconstruyas ni generalices una relacion declarada — repetila tal "
    "cual la dijo el usuario, aunque te parezca menos formal.\n"
    "- Cuando salto_semantico es null (caso normal, sin salto), 'camino' es "
    "la cadena LITERAL completa dentro de sucesores_nivel1_y_nivel2: el "
    "primer id SIEMPRE debe ser uno de los sucesores de nivel 1 dados. Si "
    "el nodo que te interesa es de nivel 2 (aparece dentro de 'sucesores' "
    "de un nodo de nivel 1), DEBES incluir primero ese nodo de nivel 1 "
    "como paso previo en 'camino', y el de nivel 2 despues, en ese orden. "
    "Nunca pongas un nodo de nivel 2 sin su padre de nivel 1 inmediatamente "
    "antes en el mismo camino. Cada id debe ser un sucesor real del nodo "
    "anterior en la cadena, nunca un id repetido ni inventado. Cuando "
    "salto_semantico SI tiene un id (ver SALTO SEMANTICO LIBRE arriba), "
    "'camino' debe ser [] — el destino es ese id, no una cadena de "
    "sucesores locales.\n"
    "- 'repregunta' debe tener texto solo cuando accion='repreguntar'; si "
    "no, null.\n"
    "- Si recibes 'error_previo' e 'ids_validos', tu respuesta anterior fue "
    "invalida por esa razon exacta: tu 'camino' en este intento DEBE usar "
    "EXCLUSIVAMENTE ids de la lista literal 'ids_validos' (no inventes ni "
    "combines ids de fuera de esa lista).\n\n"
    "MAS SOBRE REGISTRO SEGUN PERFIL: la regla (b) no es 'nunca uses "
    "palabras formales', es 'usa el vocabulario que corresponde a la "
    "realidad del perfil'. Si el perfil describe una startup con equipo, "
    "inversionistas o varias personas en roles distintos, SI es correcto "
    "hablar de 'tu equipo', 'las areas de tu empresa' o 'tus socios' — la "
    "prohibicion aplica solo cuando esas palabras no corresponden a la "
    "realidad descrita en el perfil_sesion. Ejemplo contrastante: perfil "
    "'somos tres personas, dos programadores y una diseñadora, ya "
    "constituimos la empresa formalmente'; aqui una pregunta_adaptada como "
    "'¿como estan dividiendo las responsabilidades entre tu equipo?' es "
    "perfectamente correcta porque el equipo existe de verdad.\n\n"
    "EJEMPLOS DE RESPUESTA COMPLETA (formato de referencia, no copiar el "
    "contenido — cada sesion real tiene su propio nodo_actual y sucesores):\n"
    "Ejemplo 1 (avanzar con tramo silencioso + pregunta_adaptada al final): "
    "el usuario ya conto en su entrada_original que trabaja solo vendiendo "
    "pan artesanal y que ya probo con vecinos que compraron y repitieron. "
    "El nodo_actual es sobre validar interes inicial (ya cubierto por ese "
    "relato) y su sucesor de nivel 1 es sobre entender que problema "
    "resuelve el producto para el cliente (tambien cubierto: la gente "
    "repite compra porque le gusta el sabor). El sucesor de nivel 2 de ese "
    "nodo pregunta por el costo real de producción, algo que el usuario "
    "NUNCA menciono. Respuesta: {\"accion\": \"avanzar\", \"camino\": "
    "[\"id_del_sucesor_nivel1\", \"id_del_sucesor_nivel2\"], "
    "\"pregunta_necesaria\": true, \"pregunta_adaptada\": \"¿ya sacaste la "
    "cuenta de cuanto te cuesta en ingredientes y tiempo hacer cada "
    "tanda?\", \"repregunta\": null, \"perfil_update\": null, "
    "\"prioridad_declarada\": null, \"salto_semantico\": null}.\n"
    "Ejemplo 2 (repreguntar porque la respuesta fue ambigua): la "
    "pregunta_adaptada anterior fue '¿ya le vendiste esto a alguien fuera "
    "de tu circulo cercano?' y el usuario respondio 'creo que si le "
    "interesaria a la gente'. Eso no confirma si YA vendio o solo lo cree, "
    "y los dos sucesores de nivel 1 dependen exactamente de esa "
    "distincion (uno es sobre como convertir interes en venta real, otro "
    "es sobre como conseguir la primera venta desde cero). Respuesta: "
    "{\"accion\": \"repreguntar\", \"camino\": [], \"pregunta_necesaria\": "
    "true, \"pregunta_adaptada\": null, \"repregunta\": \"cuando dices que "
    "le interesaria a la gente, ¿alguien ya te compro o pago algo, o es "
    "todavia algo que crees que pasaria?\", \"perfil_update\": null, "
    "\"prioridad_declarada\": null, \"salto_semantico\": null}.\n"
    "Ejemplo 3 (generar_plan porque el usuario lo pidio explicitamente, "
    "aunque con otras palabras): el usuario responde 'creo que con esto ya "
    "tengo para armar algo, dame lo que tengas'. Respuesta: {\"accion\": "
    "\"generar_plan\", \"camino\": [], \"pregunta_necesaria\": false, "
    "\"pregunta_adaptada\": null, \"repregunta\": null, \"perfil_update\": "
    "null, \"prioridad_declarada\": null, \"salto_semantico\": null}.\n"
    "Ejemplo 4 (salir sin plan): el usuario responde 'mejor lo dejamos "
    "aqui, no quiero seguir con esto ahora'. Respuesta: {\"accion\": "
    "\"salir\", \"camino\": [], \"pregunta_necesaria\": false, "
    "\"pregunta_adaptada\": null, \"repregunta\": null, \"perfil_update\": "
    "null, \"prioridad_declarada\": null, \"salto_semantico\": null}.\n"
    "Ejemplo 5 (cadena de 3 nodos silenciosos, el maximo permitido, sin "
    "preguntar nada en esta llamada): el perfil_sesion ya es muy rico "
    "(varios turnos acumulados) y responde con claridad lo que preguntan "
    "los tres primeros sucesores en cadena de este punto del grafo, pero "
    "el contexto SI alcanzaria para seguir mas alla del tercero — aun asi "
    "te detienes en el tercero por el limite de 3 saltos por llamada. "
    "Respuesta: {\"accion\": \"avanzar\", \"camino\": [\"id_n1\", "
    "\"id_n2_hijo_de_n1\", \"id_n3_hijo_de_n2\"], \"pregunta_necesaria\": "
    "false, \"pregunta_adaptada\": null, \"repregunta\": null, "
    "\"perfil_update\": null, \"prioridad_declarada\": null, "
    "\"salto_semantico\": null}. La siguiente llamada al interprete "
    "continuara desde ese tercer nodo, sin que el usuario haya notado "
    "ninguna pausa.\n"
    "Ejemplo 6 (prioridad_declarada llega a conteo=2, prohibida otra "
    "deflexion): prioridad_declarada_actual={\"texto\": \"resolver la "
    "resina y el QR antes de vender en volumen\", \"conteo\": 1} y el "
    "usuario acaba de reafirmarla ('mi bloqueo real sigue siendo la "
    "tecnica, no la demanda'). Respuesta: {\"accion\": \"avanzar\", "
    "\"camino\": [\"id_nodo_experimentos_tecnicos\"], "
    "\"pregunta_necesaria\": true, \"pregunta_adaptada\": \"la resina y el "
    "QR son tu frente principal y vamos a atacarlos de una vez; para "
    "avanzar rapido ahi, ¿ya probaste cambiar una sola variable a la vez "
    "en la mezcla, o has estado cambiando varias cosas al mismo tiempo?\", "
    "\"repregunta\": null, \"perfil_update\": null, \"prioridad_declarada\": "
    "{\"texto\": \"resolver la resina y el QR antes de vender en volumen\", "
    "\"conteo\": 2}, \"salto_semantico\": null}. Nota que NO dice 'pero "
    "antes de eso' ni desvia hacia validacion de pago — reconoce la "
    "prioridad y avanza sobre ella directamente.\n"
    "Ejemplo 7 (salto semantico, Fase 2.8): nodo_actual y sus sucesores "
    "locales tratan sobre metricas de validacion de clientes, pero el "
    "usuario acaba de responder 'extraigo la piedra yo mismo de una mina, "
    "la proceso a mano, hago todo solo, sin equipo ni empleados'. Ninguno "
    "de los sucesores locales atiende ese tema (capacidad de una sola "
    "persona), pero saltos_posibles incluye "
    "'decision_fundador_solo_vs_equipo' con afinidad clara. Respuesta: "
    "{\"accion\": \"avanzar\", \"camino\": [], \"pregunta_necesaria\": "
    "true, \"pregunta_adaptada\": \"ya que haces todo tu solo, ¿has "
    "pensado en el limite de cuanto puedes producir en un mes trabajando "
    "asi, o todavia no lo has calculado?\", \"repregunta\": null, "
    "\"perfil_update\": \"Hace todo el proceso solo, sin equipo ni "
    "empleados.\", \"prioridad_declarada\": null, \"salto_semantico\": "
    "\"decision_fundador_solo_vs_equipo\"}. Nota 'camino': [] porque el "
    "destino viene de salto_semantico, no de una cadena local.\n\n"
    "MEMORIA NUMERICA DEL PROYECTO (motor v2.1): en cada turno, si "
    "respuesta_usuario (o entrada_original en el primer turno) revela un "
    "numero concreto que el USUARIO declaro sobre su proyecto (nunca uno "
    "que tu infieras, redondees o supongas), devuelve 'numeros_detectados' "
    "con los campos de esta lista fija que apliquen: "
    "costo_materiales_unidad, horas_por_unidad, valor_hora, "
    "precio_tentativo, capacidad_semanal, costos_fijos_mensuales, "
    "unidades_vendidas, precio_pagado_real. Cada campo detectado es "
    "{\"valor\": numero, o {\"min\": numero, \"max\": numero} si el "
    "usuario dio un rango, \"unidad\": str|null (ej. 'USD', 'horas', "
    "'piezas por semana'), \"texto_original\": la frase exacta donde lo "
    "dijo}. Si no se revelo ningun numero nuevo este turno, "
    "'numeros_detectados' debe ser null. Ejemplo: el usuario responde 'me "
    "cuesta como $8 en materiales y me toma unas 4 horas por pieza' -> "
    "\"numeros_detectados\": {\"costo_materiales_unidad\": {\"valor\": 8, "
    "\"unidad\": \"USD\", \"texto_original\": \"me cuesta como $8 en "
    "materiales\"}, \"horas_por_unidad\": {\"valor\": 4, \"unidad\": "
    "\"horas\", \"texto_original\": \"me toma unas 4 horas por pieza\"}}.\n\n"
    "TIPO DE OFERTA (motor v2.2): en cualquier turno donde el usuario "
    "revele que vende (o piensa vender), devuelve 'tipo_oferta_detectado' "
    "con uno de: 'producto_fisico' (algo que se fabrica o se entrega "
    "fisicamente), 'servicio' (tiempo o trabajo cobrado, no un objeto), "
    "'digital' (app, software, suscripcion, contenido — costos marginales "
    "cercanos a cero), 'mixto' (combina claramente mas de uno). Ademas "
    "devuelve 'unidad_venta_detectada': la palabra EXACTA que el usuario "
    "usa para su unidad de venta (pieza, cliente, pack, sesion, "
    "suscripcion, usuario...), tal cual la dijo, nunca una que tu "
    "inventes. Si el turno no revela nada nuevo sobre esto, ambos deben "
    "ser null. Ejemplo: 'vendo velas artesanales, cada una a $8' -> "
    "\"tipo_oferta_detectado\": \"producto_fisico\", "
    "\"unidad_venta_detectada\": \"vela\".\n\n"
    "OBSERVABILIDAD (Fase 3.1): ademas del contrato anterior, incluye "
    "'razonamiento': una frase corta (maximo ~20 palabras) explicando por "
    "que elegiste ese camino o ese salto -- no cambia tu decision, solo la "
    "documenta para que una auditoria humana o automatica pueda revisarla "
    "despues sin adivinar. Ejemplo: 'el usuario menciono costos sin "
    "calcular, saltos_posibles trae un nodo dedicado a eso'.\n\n"
    "Responde SOLO un JSON: {\"accion\": \"avanzar\"|\"repreguntar\"|"
    "\"generar_plan\"|\"salir\", \"camino\": [ids en orden], "
    "\"pregunta_necesaria\": bool, \"pregunta_adaptada\": str|null, "
    "\"repregunta\": str|null, \"perfil_update\": str|null, "
    "\"prioridad_declarada\": {\"texto\": str, \"conteo\": int}|null, "
    "\"salto_semantico\": str|null, \"numeros_detectados\": "
    "{campo: {\"valor\": num|{\"min\":num,\"max\":num}, \"unidad\": "
    "str|null, \"texto_original\": str}, ...}|null, "
    "\"tipo_oferta_detectado\": \"producto_fisico\"|\"servicio\"|"
    "\"digital\"|\"mixto\"|null, \"unidad_venta_detectada\": str|null, "
    "\"razonamiento\": str|null}."
)

SYSTEM_PROFUNDIZAR = (
    "Interpretas la respuesta de un usuario a la pregunta de si quiere su "
    "plan ahora mismo (aunque le falten algunas partes) o prefiere "
    "responder unas preguntas mas para tener un plan mas completo. "
    "Responde SOLO un JSON: {\"decision\": \"generar_ya\"|\"continuar\"}."
)

SYSTEM_PREGUNTA_DIRIGIDA = (
    "Redactas UNA pregunta abierta para continuar una entrevista de "
    "emprendimiento, en el momento en que el usuario acepto profundizar "
    "para cubrir una familia especifica que su recorrido aun no tocaba "
    "(extension dirigida, Fase 2.8 'sigamos'). Recibes perfil_sesion (lo "
    "que se sabe de su idea), pregunta_cache (el plano de intencion del "
    "nodo elegido, pregenerado por topologia, NUNCA se muestra cruda), y "
    "ultimas_preguntas_hechas (hasta 3 textos literales, para no repetir "
    "plantilla). Reformula pregunta_cache: registro y vocabulario segun "
    "perfil_sesion (nada de 'organizacion'/'portafolio'/'tu equipo' si es "
    "un fundador solitario), segunda persona, UNA sola pregunta, sin "
    "explicar teoria antes, sin repetir la estructura de "
    "ultimas_preguntas_hechas. Responde SOLO el texto de la pregunta, sin "
    "comillas ni JSON."
)

SYSTEM_PLAN = (
    "Eres el redactor final de una app de emprendimiento. Recibes un JSON con "
    "entrada_original (el texto libre con el que la persona empezo o el "
    "mensaje nuevo de esta sesion si es un seguimiento), "
    "perfil_sesion (lo que revelo sobre su idea a lo largo del recorrido), "
    "material_principal: la ruta conversada (lista ordenada de conceptos, "
    "cada uno con titulo, pasos, entregable esperado, y "
    "es_viabilidad_economica), material_de_apoyo: conceptos vecinos del "
    "grafo (mismo formato) que NO fueron conversados con el usuario pero son "
    "relevantes a su perfil, bloqueo_declarado (str|null: lo que el usuario "
    "mismo repitio como su freno o urgencia principal durante la "
    "entrevista, ya con las palabras mas claras), y opcionalmente "
    "es_seguimiento + estado_vivo_previo si esta sesion continua un "
    "proyecto ya en marcha.\n\n"
    "Reglas obligatorias:\n"
    "1. Modo imperativo SIEMPRE. Convierte cada paso reflexivo o pregunta del "
    "material en una tarea concreta con verbo, sujeto y criterio de exito. "
    "Ejemplo: el material dice '¿has validado con clientes reales?' y tu "
    "escribes 'Entrevista a 5 personas de tu publico objetivo esta semana y "
    "anota como resuelven el problema hoy'.\n"
    "2. material_principal manda la estructura y la cronologia del plan: "
    "sus conceptos, en su orden, definen las etapas. material_de_apoyo NUNCA "
    "crea etapas propias; solo enriquece las etapas ya definidas por "
    "material_principal con acciones y consideraciones adicionales, donde el "
    "concepto de apoyo sea relevante a esa etapa. Si un concepto de apoyo no "
    "encaja con claridad en ninguna etapa existente, omitelo — no fuerces su "
    "inclusion.\n"
    "3. Cada etapa termina con una linea 'Esta semana:' seguida de UNA accion "
    "ejecutable en 7 dias, concreta y especifica al proyecto de la persona. "
    "Ejemplo: no 'Esta semana: piensa en tus costos', sino 'Esta semana: "
    "anota cuanto gastas en materiales para 3 piezas y divide entre 3 para "
    "saber tu costo real por unidad'.\n"
    "4. Si al menos un concepto (de material_principal o material_de_apoyo) "
    "tiene es_viabilidad_economica=true, agrega al final una seccion "
    "'## ¿Puede sostenerse tu idea? Los numeros en simple' que sintetice "
    "esos conceptos en palabras comunes, usando solo lo que esta en el "
    "material. Si NINGUNO lo tiene, NO agregues esa seccion ni inventes "
    "cifras.\n"
    "5. Prohibido cerrar el plan con preguntas para el usuario. El plan "
    "cierra con la primera accion concreta del lunes, no con una pregunta.\n"
    "6. Titulo breve especifico al proyecto (no generico), un parrafo de "
    "contexto que conecte entrada_original y perfil_sesion con lo que va a "
    "lograr con este plan concreto.\n"
    "7. Habla siempre de la IDEA o el PROYECTO del usuario. Usa la palabra "
    "'negocio' unicamente si el analisis economico forma parte del "
    "material recibido, o si el propio usuario ya la uso en su entrada o "
    "perfil_sesion. Ejemplo correcto: 'define el precio de tu idea' en vez "
    "de 'define el precio de tu negocio', salvo que el usuario mismo ya "
    "haya escrito 'mi negocio' en su entrada_original.\n"
    "8. Si recibes es_seguimiento=true, abre el plan con UNA linea (justo "
    "despues del titulo) que reconozca el avance del proyecto desde la "
    "ultima sesion, basada en estado_vivo_previo. Ejemplo: 'Desde la ultima "
    "vez ya validaste el interes de dos instituciones y conoces tu costo "
    "real por unidad; este plan parte de ahi.' No repitas acciones ya "
    "cubiertas antes: el material que recibes ya excluye lo cubierto en "
    "sesiones previas, asi que basta con no asumir que el usuario empieza "
    "de cero.\n"
    "9. Cobertura del bloqueo declarado (Fase 2.7): si recibes "
    "bloqueo_declarado no nulo, el plan DEBE darle tratamiento explicito y "
    "accionable — una etapa propia o integrada en una existente, con pasos "
    "concretos que lo ataquen, usando material_principal y "
    "material_de_apoyo disponibles (la cosecha ya prioriza conceptos afines "
    "a ese bloqueo). Si dentro de perfil_sesion o entrada_original el "
    "usuario ya propuso su propio metodo para atacarlo (por ejemplo, "
    "'probar variando una sola cosa a la vez'), reconocelo explicitamente "
    "por su nombre, validalo, y devuelvelo estructurado y mejorado con "
    "pasos concretos (hipotesis, una variable por intento, criterio de "
    "exito medible) — no lo menciones de pasada, dale su propio bloque de "
    "pasos. Ademas, revisa dependencias logicas entre etapas: ninguna etapa "
    "puede pedir como insumo algo que el plan no ayudo a producir en una "
    "etapa anterior (por ejemplo, si una etapa pide 'vende unidades sin "
    "defectos' o 'produce en volumen', una etapa anterior debe haber dado "
    "los pasos concretos para lograr esa calidad o cantidad; si el material "
    "no lo cubre con suficiente detalle, ajusta la etapa para pedir algo "
    "que SI es alcanzable con lo que hay disponible).\n"
    "10. Limite editorial (Fase 2.7): maximo 5 a 7 etapas en todo el plan, "
    "nunca mas de 7. Si el material sugeriria mas, FUSIONA las etapas que "
    "midan o persigan la misma funcion (por ejemplo, dos etapas que ambas "
    "miden intencion de compra o comportamiento del cliente van en una sola "
    "etapa mas densa, no en dos separadas) en vez de mantenerlas como "
    "etapas distintas. Prohibido crear una etapa cuya funcion ya cumple "
    "otra etapa del plan. Prioriza densidad (mas accion util por etapa) "
    "sobre extension (mas etapas o mas parrafos por etapa).\n"
    "11. Autodeclaracion de cobertura (Fase 2.8, coherencia por "
    "construccion): DESPUES de escribir el plan completo, declara "
    "honestamente que familias de contenido el plan REALMENTE trata. "
    "'accion_clientes' significa que al menos una etapa da pasos concretos "
    "para validar con clientes reales, conseguir una venta o preventa real, "
    "o probar pago (no basta con mencionar clientes de pasada). "
    "'viabilidad_economica' significa que el plan calcula o pide calcular "
    "costos, precios, margen o punto de equilibrio con numeros (no basta "
    "con decir 'piensa en tus costos' sin estructura). Se honesto: si el "
    "material no da para tratar una familia con sustancia real, NO la "
    "declares solo porque la mencionaste una vez. Esta autodeclaracion es "
    "la UNICA fuente para la etiqueta del plan y la seccion de lo que aun "
    "no cubre — si declaras una familia que el plan no sustenta, el "
    "usuario vera una etiqueta 'completo' que no corresponde a la "
    "realidad, exactamente el bug que esta regla existe para eliminar.\n"
    "12. Evidencia negativa y relaciones declaradas (motor v2.2): si "
    "perfil_sesion registra que el usuario descarto un canal, segmento, o "
    "metodo con evidencia (buscalo como 'Descarta [X]...' o frases "
    "equivalentes), PROHIBIDO proponer ese mismo elemento como canal, "
    "activo, o segmento en ninguna etapa del plan — ni siquiera "
    "reformulado con otras palabras. Ademas, PROHIBIDO alterar relaciones "
    "que el usuario declaro explicitamente: si dijo 'amigos', el plan dice "
    "'amigos', nunca 'familia' ni otra palabra que suene mas conveniente "
    "para la etapa que estas escribiendo. Esta regla existe porque un plan "
    "real le propuso a un usuario 'tu propia familia y su red' como canal "
    "de adquisicion, cuando el usuario habia dicho que eran amigos y que "
    "ese segmento especificamente rechazaba cualquier app — el redactor "
    "reconstruyo en vez de registrar lo que el usuario realmente dijo.\n\n"
    "Espanol comun, sin jerga sin explicar, sin autores, sin relleno "
    "motivacional. Todo debe salir del material recibido; no inventes "
    "tecnicas, cifras ni fuentes nuevas que no esten en el material.\n\n"
    "EJEMPLO COMPLETO DE TRANSFORMACION (formato de referencia; el "
    "material real de cada sesion trae mas conceptos y mas detalle que "
    "este ejemplo reducido):\n"
    "Entrada recibida: entrada_original='hago velas de soya aromaticas, "
    "las vendo a amigas pero quiero saber si esto puede ser algo mas "
    "serio'. perfil_sesion='Trabaja sola, ya vendio algunas velas a "
    "conocidas y quiere validar si hay mercado mas alla de su circulo "
    "cercano. No ha calculado costos.' material_principal=[{concepto: "
    "'Validacion con Clientes Reales', pasos: ['¿Le has preguntado a "
    "alguien fuera de tu circulo si compraria esto?', '¿Sabes cuanto "
    "pagarian?'], entregable: 'Lista de 5 personas fuera de tu circulo "
    "que probaron el producto', es_viabilidad_economica: false}, "
    "{concepto: 'Costeo Basico de Producto', pasos: ['¿Has sumado el "
    "costo de cera, mecha, fragancia y envase por vela?'], entregable: "
    "'Costo real por unidad', es_viabilidad_economica: true}]. "
    "material_de_apoyo=[{concepto: 'Canales de Venta Directa', pasos: "
    "['Considera vender en mercados locales o redes sociales antes de "
    "una tienda propia'], entregable: '', es_viabilidad_economica: "
    "false}].\n"
    "Salida esperada (fragmento, mismo orden que material_principal, con "
    "material_de_apoyo enriqueciendo la Etapa 1 porque 'canales de venta' "
    "es relevante ahi):\n"
    "'## Etapa 1: Confirma que hay demanda mas alla de tu circulo cercano"
    "\\n\\nVender a amigas te dice que el producto gusta, pero no confirma "
    "que alguien fuera de tu circulo lo compraria con dinero propio, sin "
    "el gesto de apoyarte por cercania.\\n\\n**Pasos:**\\n1. Identifica 5 "
    "personas que no te conozcan directamente (conocidos de conocidos, "
    "grupos locales, redes sociales) y ofreceles una vela a precio real, "
    "no de regalo.\\n2. Prueba venderlas primero en un mercado local o "
    "grupo de redes sociales de tu zona antes de pensar en una tienda "
    "propia — es mas rapido confirmar interes ahi que construyendo un "
    "canal nuevo desde cero.\\n3. Anota cuantas de esas 5 personas "
    "compran sin que se lo pidas dos veces.\\n\\n**Entregable:** Lista de "
    "5 personas fuera de tu circulo que probaron el producto, con cuantas "
    "pagaron.\\n\\n**Esta semana:** Publica tu vela con precio y foto en "
    "un grupo local de redes sociales y anota cuantos mensajes de interes "
    "real recibes en 7 dias.'\n"
    "Nota como el paso 2 vino de material_de_apoyo (canales de venta) "
    "insertado DENTRO de la Etapa 1 que ya definia material_principal, sin "
    "crear una etapa nueva solo para canales. La Etapa 2 (Costeo Basico) "
    "seguiria despues, y como tiene es_viabilidad_economica=true, el plan "
    "cerraria con la seccion '## ¿Puede sostenerse tu idea?' sintetizando "
    "el costeo en palabras simples, tal como pide la regla 4. Ejemplo de "
    "esa seccion final para este mismo caso: 'Sumaste que cada vela te "
    "cuesta $3 en materiales. Si la vendes a $8, tu margen por unidad es "
    "$5. Si vendes 10 velas al mes, eso son $50 de margen — suficiente "
    "para reinvertir en mas cera, pero todavia no un ingreso que reemplace "
    "otro trabajo. El numero que necesitas descubrir ahora es cuantas "
    "velas puedes vender realmente al mes fuera de tu circulo cercano.' "
    "Observa que la cifra de $3 y $8 salen directamente del material "
    "recibido (el costeo que el usuario ya calculo), nunca se inventan de "
    "la nada. Si el material no trae cifras exactas (solo dice 'no ha "
    "calculado costos'), la seccion final debe pedir ese calculo como "
    "primer paso en vez de inventar numeros de ejemplo — la honestidad "
    "sobre lo que aun no se sabe vale mas que un numero inventado que "
    "parezca completo.\n\n"
    "Cada elemento de material_principal y material_de_apoyo trae un campo "
    "'id' (Fase 3.1): es SOLO para tu autodeclaracion de procedencia al "
    "final (regla de FORMATO DE SALIDA mas abajo) -- jamas escribas un id "
    "crudo dentro del markdown visible, ahi siempre usas el titulo del "
    "concepto en prosa normal.\n\n"
    "FORMATO DE SALIDA (obligatorio): escribe el plan completo en markdown "
    "normal (como en el ejemplo). Al final, en una linea propia, escribe "
    "EXACTAMENTE el delimitador ===JSON=== y luego, en la siguiente linea, "
    "SOLO un JSON compacto de una sola linea con tu autodeclaracion de la "
    "regla 11 (Hotfix v2.2.1: la cola JSON se redujo a un solo campo para "
    "que quepa completa incluso si el plan agota casi todo max_tokens — "
    "'secciones' se elimino por ser redundante, el post-validador mecanico "
    "ya escanea los encabezados reales del markdown en vez de confiar en "
    "que el modelo los liste bien): {\"familias_tratadas\": [str, ...] "
    "(subconjunto de [\"accion_clientes\", \"viabilidad_economica\"], "
    "puede ser lista vacia), \"etapas\": {\"1\": [id, ...], \"2\": [id, ...], "
    "...} (Fase 3.1, procedencia: para cada Etapa numerada que escribiste "
    "en el markdown, la lista de 'id' -- de material_principal y/o "
    "material_de_apoyo -- cuyo contenido real usaste en esa etapa; nunca "
    "inventes un id que no viniera en el material recibido)}. No agregues "
    "nada despues de esa linea."
)

SYSTEM_ESTADO_VIVO = (
    "Comprimes el estado de un proyecto de emprendimiento en una sintesis de "
    "300 a 500 tokens que sirve como memoria para la siguiente sesion. "
    "Recibes el estado_vivo anterior (puede ser null si es la primera "
    "sesion), el perfil de sesion acumulado en la sesion que acaba de "
    "cerrar, y los titulos de los conceptos nuevos que se cubrieron. "
    "Combina todo en un solo estado_vivo nuevo: que sabemos del proyecto, "
    "que se ha validado o decidido, que sigue sin resolver. Prosa densa, "
    "sin listas, en espanol comun, sin jerga. No repitas informacion ya "
    "dicha, sintetiza. Responde SOLO el texto del estado_vivo nuevo, sin "
    "JSON, sin comillas, sin titulo."
)

SYSTEM_JUEZ_SESION = (
    "Fase 3.1 (caja de vidrio): eres un auditor barato y rapido de UNA "
    "sesion ya cerrada de una entrevista guiada de emprendimiento. NO "
    "decides nada, NO bloqueas nada -- tu veredicto es una señal de "
    "triage para que un humano revise despues las sesiones sospechosas, "
    "nunca un filtro automatico.\n\n"
    "Recibes 'turnos': una lista, en orden, de cada paso que el "
    "interprete dio -- el nodo por el que paso (titulo real del grafo), "
    "si llego ahi por sucesion normal o por un salto semantico (y de ser "
    "asi, que otros candidatos locales y saltos posibles habia con sus "
    "scores), la respuesta libre del usuario en ese punto, y el "
    "razonamiento corto que el interprete dio para su decision (puede "
    "venir null en pasos automaticos).\n\n"
    "Evalua tres cosas: (1) pertinencia_transiciones (1 a 5): ¿cada "
    "transicion entre nodos tiene sentido dado lo que el usuario acababa "
    "de decir, o hay saltos que parecen arbitrarios/forzados? 5 = todas "
    "las transiciones se justifican claramente por la respuesta previa; "
    "1 = varias transiciones no tienen relacion aparente con lo que el "
    "usuario dijo. (2) repeticion_detectada: true si el interprete "
    "pregunto (o reformulo) esencialmente lo mismo que ya le habian "
    "respondido antes en la misma sesion. (3) señales_fuera_de_material: "
    "citas literales cortas de la respuesta del usuario que mencionan un "
    "tema que NINGUN nodo visitado ni saltos_posibles ofrecidos parecia "
    "cubrir (posible hueco de contenido en el grafo, no un error del "
    "interprete) -- lista vacia si no hay ninguna.\n\n"
    "Responde SOLO un JSON: {\"pertinencia_transiciones\": 1|2|3|4|5, "
    "\"repeticion_detectada\": bool, \"señales_fuera_de_material\": "
    "[str, ...], \"comentario\": str (una sola frase, tu observacion mas "
    "util para quien revise esta sesion despues)}."
)

SYSTEM_ORGANIZADOR = (
    "Organizas la idea de un usuario en un resumen honesto, SIN instruir. "
    "Recibes texto_usuario (su idea o situacion en texto libre) y una lista "
    "de puertas curadas del grafo (fase + titulo + resumen corto) para que "
    "sepas el mapa de temas disponible. Responde SOLO un JSON: "
    "{\"idea_en_una_frase\": str, \"etapa_detectada\": "
    "\"ideacion\"|\"validacion\"|\"planificacion\"|\"ejecucion\", "
    "\"lo_que_ya_tienes_claro\": [str, ...], "
    "\"lo_que_estas_asumiendo_sin_saberlo\": [str, ...], "
    "\"areas_que_cubriria_tu_plan_completo\": [str, ...]}.\n\n"
    "REGLA DURA: organiza y senala huecos; PROHIBIDO instruir, dar pasos, "
    "recomendar acciones o usar verbos en modo imperativo en ningun campo. "
    "'areas_que_cubriria_tu_plan_completo' son solo NOMBRES de temas (3 a "
    "6), nunca acciones, nunca el 'como' hacerlo."
)

SYSTEM_REPORTE = (
    "Redactas la narracion de un Reporte de Sostenibilidad para un proyecto "
    "de emprendimiento (motor v2.2). Recibes 'resultados': salidas YA "
    "CALCULADAS por un modulo determinista (costo_unitario, margen, "
    "punto_equilibrio, capacidad, escenarios, ciclo_conversion_efectivo), "
    "cada una con su valor (o null si falta un insumo) y que campos se "
    "usaron o faltan; 'numeros_proyecto_declarados': los numeros crudos "
    "que el usuario dio, por si necesitas citarlos literalmente; y "
    "'tipo_oferta': 'producto_fisico'|'servicio'|'digital'|'mixto'|null — "
    "usa el vocabulario correcto segun este campo (para 'digital', di "
    "'margen por usuario' en vez de 'margen por pieza', 'usuarios/mes' en "
    "vez de 'unidades producidas'; para 'servicio', habla de la unidad de "
    "servicio, no de produccion fisica).\n\n"
    "REGLA DURA, LA MAS IMPORTANTE: PROHIBIDO generar, estimar, redondear "
    "distinto o inventar CUALQUIER cifra que no venga literalmente de "
    "'resultados' o 'numeros_proyecto_declarados'. Si necesitas un numero "
    "para una frase, usa EXACTAMENTE el que recibiste, sin recalcularlo tu "
    "mismo. Si un resultado tiene valor null (le falta un insumo), NO "
    "inventes un sustituto ni una cifra de ejemplo: eso se explica en la "
    "seccion de numeros faltantes, no en 'Tus números hoy'.\n\n"
    "Estructura obligatoria, con estos titulos EXACTOS y en este orden:\n"
    "## Tus números hoy\n"
    "## Qué significan\n"
    "## Escenarios\n"
    "## Los números que te faltan (y cómo conseguirlos)\n\n"
    "En '## Tus números hoy', reporta cada resultado disponible (valor no "
    "null) con su formula en palabras simples junto al numero. Ejemplo: "
    "'Tu margen: $85 − $68 = $17 por pieza; de cada venta te quedan $17.' "
    "En '## Qué significan', explica en 2-4 frases, en español simple sin "
    "jerga, que le dicen esos numeros sobre su proyecto (¿es sano el "
    "margen?, ¿el techo de ingreso alcanza lo que busca?). En "
    "'## Escenarios', si 'escenarios' tiene datos, su forma depende de "
    "tipo_oferta — nunca asumas cual es, fijate en las claves que "
    "realmente vienen en 'resultados.escenarios': (1) 'producto_fisico' o "
    "'servicio' (claves pesimista/base/sobredemanda): describe los tres "
    "con sus cifras EXACTAS. Para sobredemanda hay DOS cifras de perdida "
    "con significado DISTINTO — nunca las confundas ni uses solo una: "
    "'ingreso_perdido_estimado' es cuanto DINERO EN VENTAS no se factura "
    "(unidades no atendidas x precio), y 'margen_perdido_estimado' es "
    "cuanta GANANCIA no llega (unidades no atendidas x margen) — son "
    "numeros diferentes a proposito, explica ambos por separado con sus "
    "nombres correctos. Ejemplo: 'dejarías de facturar $850 en ventas que "
    "no puedes atender, de los cuales $170 habrían sido ganancia real "
    "para ti.' Explica tambien que 'unidades_no_atendidas' es venta que "
    "se pierde porque la capacidad de produccion no alcanza, no un "
    "fracaso de ventas. (2) 'digital' (claves 50%/100%/200%): estos son "
    "niveles de ADOPCION de la meta de usuarios/ventas que el usuario "
    "declaro, no de capacidad de produccion — describe cada nivel con su "
    "'unidades', 'ingreso' e 'margen_total' exactos, y explica que "
    "representan escenarios de cuanta gente adopta la oferta, no un techo "
    "fisico de cuanto se puede producir. En "
    "'## Los números que te faltan', para cada nombre de "
    "campo que aparezca en algun 'insumos_faltantes', tradúcelo a una "
    "frase en lenguaje natural (nunca el nombre tecnico del campo) "
    "explicando que dato es y para que serviria tenerlo.\n\n"
    "No agregues ninguna seccion, nota, disclaimer, ni pregunta al final: "
    "eso lo agrega el sistema despues de tu texto. No uses la palabra "
    "'negocio' salvo que el propio usuario ya la haya usado; habla de "
    "'tu idea' o 'tu proyecto'."
)


def cargar_grafo():
    return json.load(open(GRAPH_PATH, encoding="utf-8"))["nodos"]


def cargar_quiz():
    return json.load(open(QUIZ_PATH, encoding="utf-8"))


def cargar_entry_seeds():
    return json.load(open(ENTRY_SEEDS_PATH, encoding="utf-8"))["seeds"]


def cargar_preguntas_cache():
    if PREGUNTAS_CACHE_PATH.exists():
        return json.load(open(PREGUNTAS_CACHE_PATH, encoding="utf-8"))
    return {}


def guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido,
                    project_id=None, db_session_id=None, es_seguimiento=False, estado_vivo_previo=None,
                    fallback_events=None, prioridad_declarada=None, pregunta_hecha=None):
    """pregunta_hecha (Hotfix v2.1.2): la pregunta LITERAL que esta pendiente
    de respuesta en el momento de guardar, si la hay. Se persiste para que
    --continuar pueda re-presentarla y leer una respuesta real, en vez de
    reanudar con respuesta_usuario=None (indistinguible del arranque de una
    sesion nueva) y arriesgarse a que el interprete decida algo sin base,
    incluyendo 'salir' sin que el usuario lo haya pedido."""
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    data = {
        "ruta": ruta,
        "modos": modos,
        "perfil_sesion": perfil_sesion,
        "entrada_original": texto_original,
        "profundizar_ofrecido": profundizar_ofrecido,
        "project_id": project_id,
        "db_session_id": db_session_id,
        "es_seguimiento": es_seguimiento,
        "estado_vivo_previo": estado_vivo_previo,
        "fallback_events": fallback_events or [],
        "prioridad_declarada": prioridad_declarada,
        "pregunta_hecha": pregunta_hecha,
        "timestamp": datetime.now().isoformat(),
    }
    (SESSIONS_DIR / f"{session_id}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def cargar_sesion(session_id):
    path = SESSIONS_DIR / f"{session_id}.json"
    if not path.exists():
        print(f"ERROR: no existe la sesion {session_id} en {SESSIONS_DIR}")
        sys.exit(1)
    return json.load(open(path, encoding="utf-8"))


class SesionInterrumpida(Exception):
    """El usuario corto la sesion (EOF o Ctrl+C). El estado ya se guarda
    incrementalmente turno a turno (guardar_sesion), asi que el cierre
    elegante solo necesita evitar el traceback y decir como retomar."""
    pass


def leer_entrada(prompt=""):
    """input() que convierte EOF/Ctrl+C en un cierre elegante en vez de un
    traceback visible. Usar SIEMPRE esta funcion en vez de input() directo.
    UnicodeDecodeError (encontrado en vivo pegando texto con emojis en una
    consola de Windows con codepage local, que puede ignorar el
    reconfigure() de sys.stdin) se trata igual: el usuario retoma con
    --continuar, que ahora (hotfix v2.1.2) re-presenta la pregunta exacta
    que quedo pendiente en vez de perderla."""
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt, UnicodeDecodeError):
        raise SesionInterrumpida()


def preguntar_opcion(texto, opciones, extra=""):
    """Menu numerado de emergencia. Devuelve indice elegido, o 'P'/'Q' si extra los permite."""
    print("\n" + texto)
    for i, op in enumerate(opciones, 1):
        print(f"  {i}. {op}")
    if extra:
        print(f"  {extra}")
    while True:
        r = leer_entrada("> ").strip().upper()
        if r in ("P", "Q") and extra:
            return r
        if r.isdigit() and 1 <= int(r) <= len(opciones):
            return int(r) - 1
        print("Opcion no valida, intenta de nuevo.")


def _parsear_json(raw):
    texto = raw.strip().removeprefix("```json").removesuffix("```").strip()
    try:
        return json.loads(texto)
    except json.JSONDecodeError:
        # El modelo a veces agrega texto despues del primer objeto JSON valido
        # (p.ej. una nota o una repeticion); raw_decode toma solo el primero.
        obj, _ = json.JSONDecoder().raw_decode(texto)
        return obj


def _costo_llamada_usd(model, in_tokens, out_tokens, cache_read_tokens=0, cache_write_tokens=0):
    pin, pout = PRECIOS.get(model, (0.0, 0.0))
    return (
        in_tokens / 1_000_000 * pin
        + cache_read_tokens / 1_000_000 * pin * CACHE_READ_MULT
        + cache_write_tokens / 1_000_000 * pin * CACHE_WRITE_MULT
        + out_tokens / 1_000_000 * pout
    )


def costo_acumulado_usd():
    total = 0.0
    for model, s in USO.items():
        total += _costo_llamada_usd(model, s["in"], s["out"], s["cache_read"], s["cache_write"])
    return total


def costo_por_componente_usd():
    """Desglose de costo real por componente (Fase 2.7): clasificacion,
    turnos (entrevista, incluye repreguntas y profundizar), plan,
    estado_vivo, y organizador (solo en --gratis)."""
    return dict(USO_POR_COMPONENTE)


def llamar_claude(system, user_text, model, max_tokens=1500, componente=None):
    global PRESUPUESTO_EXCEDIDO
    if costo_acumulado_usd() >= PRESUPUESTO_SESION_USD:
        if not PRESUPUESTO_EXCEDIDO:
            PRESUPUESTO_EXCEDIDO = True
            print(f"  (presupuesto de ${PRESUPUESTO_SESION_USD:.2f} alcanzado; "
                  f"el resto de la sesion corre en modo offline)")
        raise RuntimeError("presupuesto de sesion excedido")
    import anthropic
    client = anthropic.Anthropic()
    msg = client.messages.create(
        model=model, max_tokens=max_tokens,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_text}],
    )
    _registrar_uso(model, msg, componente)
    return "".join(b.text for b in msg.content if b.type == "text")


def _registrar_uso(model, msg, componente=None):
    stats = USO.setdefault(model, {"in": 0, "out": 0, "llamadas": 0, "cache_read": 0, "cache_write": 0})
    cache_read = getattr(msg.usage, "cache_read_input_tokens", 0) or 0
    cache_write = getattr(msg.usage, "cache_creation_input_tokens", 0) or 0
    stats["in"] += msg.usage.input_tokens
    stats["out"] += msg.usage.output_tokens
    stats["cache_read"] += cache_read
    stats["cache_write"] += cache_write
    stats["llamadas"] += 1
    if componente:
        costo = _costo_llamada_usd(model, msg.usage.input_tokens, msg.usage.output_tokens, cache_read, cache_write)
        USO_POR_COMPONENTE[componente] = USO_POR_COMPONENTE.get(componente, 0.0) + costo


def llamar_claude_conversacion(system, historial_mensajes, nuevo_turno_texto, model, max_tokens=600, componente=None):
    """Como llamar_claude, pero mantiene una conversacion (historial_mensajes,
    mutada en el sitio SOLO si la llamada tiene exito) que crece turno a
    turno. El marcador de cache vive siempre en el ultimo bloque enviado: se
    quita del bloque previamente marcado (bookkeeping, seguro aunque esta
    llamada falle) y se coloca en el turno nuevo. Asi, desde la segunda
    llamada de la sesion en adelante, todo el prefijo previo (entrada
    original, perfil acumulado, turnos anteriores) se lee de cache en vez de
    repagarse completo cada vez (Fase 2.7, caching incremental de
    conversacion)."""
    global PRESUPUESTO_EXCEDIDO
    if costo_acumulado_usd() >= PRESUPUESTO_SESION_USD:
        if not PRESUPUESTO_EXCEDIDO:
            PRESUPUESTO_EXCEDIDO = True
            print(f"  (presupuesto de ${PRESUPUESTO_SESION_USD:.2f} alcanzado; "
                  f"el resto de la sesion corre en modo offline)")
        raise RuntimeError("presupuesto de sesion excedido")
    import anthropic
    client = anthropic.Anthropic()
    # El marcador anterior vive en el ultimo mensaje de rol "user" (content
    # en forma de lista); el mensaje mas reciente en la lista puede ser un
    # turno "assistant" (content como string plano), asi que se busca hacia
    # atras el primer bloque con content en lista, no simplemente [-1].
    for _msg_previo in reversed(historial_mensajes):
        _contenido_previo = _msg_previo.get("content")
        if isinstance(_contenido_previo, list) and _contenido_previo:
            _contenido_previo[-1].pop("cache_control", None)
            break
    nuevo_turno = {
        "role": "user",
        "content": [{"type": "text", "text": nuevo_turno_texto, "cache_control": {"type": "ephemeral"}}],
    }
    msg = client.messages.create(
        model=model, max_tokens=max_tokens,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=historial_mensajes + [nuevo_turno],
    )
    _registrar_uso(model, msg, componente)
    texto_respuesta = "".join(b.text for b in msg.content if b.type == "text")
    # Solo se compromete al historial real si la llamada tuvo exito: si
    # client.messages.create() lanza, no llegamos aqui y historial_mensajes
    # queda intacto (nunca con un turno de usuario sin su respuesta).
    historial_mensajes.append(nuevo_turno)
    historial_mensajes.append({"role": "assistant", "content": texto_respuesta})
    return texto_respuesta


def reportar_costo():
    print("\n" + "=" * 60)
    print("  Costo real de la sesion (tokens)")
    print("=" * 60)
    total = 0.0
    for model, s in USO.items():
        costo = _costo_llamada_usd(model, s["in"], s["out"], s["cache_read"], s["cache_write"])
        total += costo
        print(f"  {model}: {s['llamadas']} llamadas | {s['in']} in / {s['out']} out "
              f"(cache_read {s['cache_read']}, cache_write {s['cache_write']}) | ${costo:.4f}")
    if USO_POR_COMPONENTE:
        print("  Desglose por componente:")
        for comp, costo in sorted(USO_POR_COMPONENTE.items(), key=lambda kv: -kv[1]):
            print(f"    {comp}: ${costo:.4f}")
    print(f"  TOTAL: ${total:.4f}" + (" (presupuesto excedido, se degrado a offline)" if PRESUPUESTO_EXCEDIDO else ""))


def clasificar_entrada(texto, entry_seeds, graph):
    """Capa 1: texto libre -> (puerta_id, perfil_sesion). Fallback: cuestionario cerrado."""
    if API_KEY:
        puertas = [
            {
                "id": s,
                "fase": graph[s]["fase_proyecto"],
                "titulo": graph[s]["titulo_concepto"],
                "resumen": graph[s]["resumen_teorico"][:200],
            }
            for s in entry_seeds
        ]
        ctx = {"texto_usuario": texto, "puertas": puertas}
        try:
            raw = llamar_claude(SYSTEM_CLASIFICACION, json.dumps(ctx, ensure_ascii=False), MODEL_HAIKU,
                                max_tokens=400, componente="clasificacion")
            data = _parsear_json(raw)
            if data["puerta_id"] in entry_seeds:
                return data["puerta_id"], (data.get("perfil_sesion") or "").strip()
            raise ValueError(f"puerta_id fuera de las 20 puertas: {data.get('puerta_id')}")
        except Exception as e:
            print(f"  (fallo la clasificacion con IA, uso cuestionario cerrado: {e})")
    quiz = cargar_quiz()
    pf = quiz["pregunta_fase"]
    i = preguntar_opcion(pf["texto"], [o["texto"] for o in pf["opciones"]])
    fase = pf["opciones"][i]["fase"]
    pp = quiz["pregunta_puerta"][fase]
    i = preguntar_opcion(pp["texto"], [o["texto"] for o in pp["opciones"]])
    return pp["opciones"][i]["nodo"], ""


def obtener_pregunta(node_id, node, cache):
    """Pregunta abierta pregenerada para este nodo, o una generica si no esta en el cache."""
    entry = cache.get(node_id)
    if entry and entry.get("pregunta"):
        return entry["pregunta"]
    return (
        f"Pensando en \"{node['titulo_concepto']}\", cuentame en tus palabras "
        "donde estas parado ahora mismo con tu idea y que es lo que mas "
        "te preocupa o te entusiasma."
    )


def sucesores_nivel(nid, graph, visitados, limite=MAX_OPCIONES, dominios_desbloqueados=None):
    return [
        c for c in graph[nid].get("nodos_siguientes", [])
        if c in graph and c not in visitados and _dominio_permitido(c, graph, dominios_desbloqueados)
    ][:limite]


def resumen_nodo(nid, graph, preguntas_cache=None):
    n = graph[nid]
    out = {
        "id": nid,
        "titulo": n["titulo_concepto"],
        "condiciones_activacion": n.get("condiciones_activacion", [])[:2],
    }
    if preguntas_cache is not None:
        out["pregunta_cache"] = obtener_pregunta(nid, n, preguntas_cache)
    return out


# ---------------------------------------------------------------------------
# Brujula semantica (Fase 2.8): navegacion libre por TODA la telaraña, no
# solo los sucesores locales del nodo actual. Embeddings locales
# (sentence-transformers), cero costo de API por sesion. Si la libreria o
# el indice no estan disponibles, se desactiva silenciosamente (una sola
# vez, con nota impresa) y el motor sigue funcionando solo con navegacion
# local, exactamente como antes de esta fase.
# ---------------------------------------------------------------------------
_BRUJULA_MODELO = None
_BRUJULA_INDICE = None  # (ids: list[str], embeddings: np.ndarray) o (None, None) si fallo
_BRUJULA_AVISO_IMPRESO = False


def _cargar_brujula():
    global _BRUJULA_MODELO, _BRUJULA_INDICE, _BRUJULA_AVISO_IMPRESO
    if _BRUJULA_INDICE is not None:
        return _BRUJULA_INDICE[0] is not None
    try:
        import numpy as np
        data = np.load(SEMANTIC_INDEX_PATH, allow_pickle=False)
        ids = list(data["ids"])
        embeddings = data["embeddings"]
        from sentence_transformers import SentenceTransformer
        _BRUJULA_MODELO = SentenceTransformer(SEMANTIC_MODEL_NAME)
        _BRUJULA_INDICE = (ids, embeddings)
        return True
    except Exception as e:
        if not _BRUJULA_AVISO_IMPRESO:
            _BRUJULA_AVISO_IMPRESO = True
            print(f"  (brujula semantica no disponible, navegacion solo local: {e})")
        _BRUJULA_INDICE = (None, None)
        return False


def buscar_afines(texto, excluidos, k=5, min_score=0.0, con_score=False, graph=None, dominios_desbloqueados=None):
    """Top-k nodos de TODO el grafo mas afines semanticamente a `texto`
    (embeddings locales, sin llamada a la API), excluyendo `excluidos`
    (ya visitados/cubiertos). Devuelve [] si la brujula no esta disponible
    o si `texto` esta vacio.
    Fase 2.9: min_score descarta candidatos por debajo del umbral (el
    salto semantico libre lo usa via MIN_SCORE_SALTO; extender_sigamos_
    dirigido no, porque ese ya filtra por familia, un criterio de
    relevancia distinto y suficiente). con_score=True devuelve tuplas
    (id, score) en vez de solo ids, para exponerle el numero al
    interprete y que pueda juzgar afinidad debil el mismo.
    Hotfix v2.1.1: si se pasa `graph`, tambien filtra por dominio
    (dominios_desbloqueados, por defecto DOMINIOS_DESBLOQUEADOS_DEFECTO);
    si `graph` es None, no hay forma de saber el dominio de cada id y el
    filtro se omite (compatibilidad con llamadas/pruebas que no lo pasan)."""
    if not texto or not texto.strip():
        return []
    if not _cargar_brujula():
        return []
    ids, embeddings = _BRUJULA_INDICE
    query = _BRUJULA_MODELO.encode([texto], normalize_embeddings=True)[0]
    scores = embeddings @ query
    orden = scores.argsort()[::-1]
    resultados = []
    for idx in orden:
        nid = ids[idx]
        if nid in excluidos:
            continue
        if graph is not None and nid in graph and not _dominio_permitido(nid, graph, dominios_desbloqueados):
            continue
        score = float(scores[idx])
        if score < min_score:
            break  # orden descendente: nada mas adelante supera el umbral
        resultados.append((str(nid), score) if con_score else str(nid))
        if len(resultados) >= k:
            break
    return resultados


def _reparar_camino_cadena(actual_id, camino, graph, visitados):
    """Reparo 1 (cadena estricta): si un id del camino no es sucesor directo
    del anterior pero SI es sucesor de alguno de los sucesores directos de
    ese anterior (el modelo omitio el padre de nivel 1 intermedio), inserta
    ese padre automaticamente. Solo repara "hacia adelante" dentro de la
    MISMA rama que el elemento previo ya aceptado; si el modelo empezo por
    la rama equivocada, este reparo falla (ver _reparar_camino_desde_objetivo)."""
    reparado = []
    prev = actual_id
    vistos = set()
    for nid in camino:
        if nid in graph.get(prev, {}).get("nodos_siguientes", []):
            reparado.append(nid)
            vistos.add(nid)
            prev = nid
            continue
        padre = next(
            (c for c in graph.get(prev, {}).get("nodos_siguientes", [])
             if c not in visitados and c not in vistos and nid in graph.get(c, {}).get("nodos_siguientes", [])),
            None,
        )
        if padre is None:
            raise ValueError(f"{nid} no es sucesor de {prev} ni de ninguno de sus sucesores directos")
        reparado.append(padre)
        vistos.add(padre)
        reparado.append(nid)
        vistos.add(nid)
        prev = nid
    return reparado


def _reparar_camino_desde_objetivo(camino, nivel1_pool, visitados):
    """Reparo 2 (reconstruccion desde el objetivo): ignora los pasos
    intermedios que el modelo propuso (a veces atribuye un nodo de nivel 2 a
    la rama de nivel 1 equivocada, confundiendo hermanos) y reconstruye el
    camino minimo real hacia el ULTIMO id que el modelo indico, buscando su
    padre correcto en el MISMO pool de nivel1+nivel2 que se le mostro."""
    if not camino:
        raise ValueError("camino vacio")
    objetivo = camino[-1]
    if objetivo in visitados:
        raise ValueError(f"objetivo {objetivo} ya fue visitado")
    nivel1_ids = {n["id"] for n in nivel1_pool}
    if objetivo in nivel1_ids:
        return [objetivo]
    for n in nivel1_pool:
        hijos = {h["id"] for h in n.get("sucesores", [])}
        if objetivo in hijos and n["id"] not in visitados:
            return [n["id"], objetivo]
    raise ValueError(f"{objetivo} no es sucesor de nivel 1 ni de nivel 2 conocido")


def _validar_camino(actual_id, camino, graph, visitados, nivel1_pool=None):
    if not camino:
        raise ValueError("camino vacio")
    try:
        camino_reparado = _reparar_camino_cadena(actual_id, camino, graph, visitados)
        if len(camino_reparado) > MAX_SALTOS_SILENCIOSOS_POR_LLAMADA:
            raise ValueError(f"camino excede {MAX_SALTOS_SILENCIOSOS_POR_LLAMADA} nodos tras reparacion en cadena")
    except Exception:
        if nivel1_pool is None:
            raise
        camino_reparado = _reparar_camino_desde_objetivo(camino, nivel1_pool, visitados)

    prev = actual_id
    vistos_en_camino = set()
    for nid in camino_reparado:
        if nid not in graph or nid in visitados or nid in vistos_en_camino:
            raise ValueError(f"nodo invalido o repetido en camino: {nid}")
        if nid not in graph[prev].get("nodos_siguientes", []):
            raise ValueError(f"{nid} no es sucesor de {prev}")
        vistos_en_camino.add(nid)
        prev = nid
    return camino_reparado


def _elegir_por_afinidad(candidatos_ids, graph, respuesta_usuario, perfil_sesion):
    """Ultimo recurso silencioso (sin mostrar nada al usuario): elige el
    candidato de mayor afinidad de palabras clave con la ultima respuesta
    del usuario (y el perfil de sesion), en vez de un menu numerado."""
    if not candidatos_ids:
        return None
    contexto = _tokens_cosecha((respuesta_usuario or "") + " " + (perfil_sesion or ""))
    if not contexto:
        return candidatos_ids[0]

    def puntaje(nid):
        n = graph[nid]
        texto_nodo = n.get("titulo_concepto", "") + " " + " ".join(n.get("condiciones_activacion", []))
        return len(contexto & _tokens_cosecha(texto_nodo))

    return max(candidatos_ids, key=puntaje)


def interpretar_multi_salto(actual_id, graph, visitados, perfil_sesion, texto_original,
                             pregunta_hecha, respuesta_usuario, repreguntas_disponibles,
                             preguntas_cache, ultimas_preguntas=None, prioridad_declarada_actual=None,
                             historial_mensajes=None, registrar_evento=None):
    """Capa 2: decide un camino de 1-3 nodos (silenciosos + a lo sumo uno
    conversado) y, si se detiene a preguntar, la pregunta_adaptada para ese
    nodo (reformulada al registro del perfil, descontando lo ya respondido,
    sin repetir las ultimas 3 intervenciones). Ademas rastrea
    prioridad_declarada (Fase 2.7): si el usuario reafirma 2+ veces el mismo
    bloqueo, prohibe otra deflexion y exige reconocerlo como frente legitimo.
    Si el modelo devuelve algo invalido (id inexistente, camino vacio,
    pregunta_adaptada faltante), reintenta UNA vez con el error y la lista
    literal de ids validos (el reintento SIEMPRE es una llamada aislada, sin
    tocar historial_mensajes). Si vuelve a fallar, auto-selecciona en
    silencio el candidato de mayor afinidad y continua sin que el usuario
    note nada (registra el evento como 'fallback_auto' via
    `registrar_evento`, si se provee). Solo devuelve None ante un fallo de
    RED/presupuesto (ahi si corresponde el menu numerado de emergencia,
    ultimo recurso visible).

    Si se pasa historial_mensajes (lista mutable, Fase 2.7), la llamada
    principal usa llamar_claude_conversacion: desde el segundo turno de la
    sesion en adelante, entrada_original y el perfil acumulado ya no se
    reenvian completos (viven en el prefijo cacheado de turnos previos);
    solo se envia el turno nuevo. Si historial_mensajes es None, se usa el
    llamado clasico sin estado (compatibilidad con pruebas aisladas)."""
    nivel1_ids = sucesores_nivel(actual_id, graph, visitados)
    nivel1 = []
    visitados_o_nivel1 = visitados | set(nivel1_ids)
    for nid in nivel1_ids:
        nivel2_ids = sucesores_nivel(nid, graph, visitados_o_nivel1, limite=MAX_SUCESORES_NIVEL2)
        entrada_nivel1 = resumen_nodo(nid, graph, preguntas_cache)
        entrada_nivel1["sucesores"] = [resumen_nodo(n2, graph, preguntas_cache) for n2 in nivel2_ids]
        nivel1.append(entrada_nivel1)

    # Fase 2.8: brujula semantica sobre la ultima respuesta (o la entrada
    # original, si aun no hay respuesta) - candidatos de CUALQUIER parte
    # del grafo, excluyendo lo ya visitado y lo que ya ofrecen los locales.
    # Fase 2.9: filtra por MIN_SCORE_SALTO (candidatos debiles ni siquiera
    # se ofrecen) y expone el score (afinidad) para que el interprete
    # pueda juzgar los casos limite el mismo.
    texto_para_brujula = respuesta_usuario or texto_original
    excluidos_brujula = visitados | set(nivel1_ids)
    salto_candidatos = buscar_afines(texto_para_brujula, excluidos_brujula, graph=graph,
                                     k=MAX_SALTOS_POSIBLES_OFRECIDOS, min_score=MIN_SCORE_SALTO, con_score=True)
    ids_salto_ofrecidos = [nid for nid, _ in salto_candidatos]
    saltos_posibles = [
        {
            "id": nid,
            "titulo": graph[nid]["titulo_concepto"],
            "fase_proyecto": graph[nid].get("fase_proyecto"),
            "condiciones_activacion": graph[nid].get("condiciones_activacion", [])[:2],
            "afinidad": round(score, 3),
        }
        for nid, score in salto_candidatos
    ]

    ctx_completo = {
        "entrada_original": texto_original,
        "perfil_sesion": perfil_sesion,
        "nodo_actual": resumen_nodo(actual_id, graph, preguntas_cache),
        "sucesores_nivel1_y_nivel2": nivel1,
        "saltos_posibles": saltos_posibles,
        "pregunta_hecha": pregunta_hecha,
        "respuesta_usuario": respuesta_usuario,
        "repreguntas_disponibles": repreguntas_disponibles,
        "ultimas_preguntas_hechas": (ultimas_preguntas or [])[-3:],
        "prioridad_declarada_actual": prioridad_declarada_actual,
    }
    if historial_mensajes is not None and historial_mensajes:
        # turno 2+: entrada_original y perfil_sesion ya viven en el
        # historial cacheado, no hace falta repagarlos completos cada vez
        ctx_turno = {k: v for k, v in ctx_completo.items() if k not in ("entrada_original", "perfil_sesion")}
    else:
        ctx_turno = ctx_completo

    def _emitir_decision_turno(resultado, razonamiento_fallback=None):
        """Fase 3.1 (caja de vidrio): expone via registrar_evento lo que
        el interprete YA calculo para decidir (candidatos locales,
        saltos_posibles con sus scores) mas la decision final, sin tocar
        el contrato de retorno de interpretar_multi_salto (varios tests
        dependen de su forma exacta) -- el mismo canal lateral que ya usa
        'fallback_auto'."""
        if not registrar_evento or resultado is None:
            return
        registrar_evento({
            "tipo": "decision_turno",
            "nodo_actual": actual_id,
            "respuesta_usuario": respuesta_usuario,
            "candidatos_locales": [n["id"] for n in nivel1],
            "saltos_posibles": saltos_posibles,
            "decision": {
                "accion": resultado.get("accion"),
                "camino": resultado.get("camino"),
                "es_salto": resultado.get("es_salto", False),
            },
            "razonamiento": resultado.get("razonamiento") or razonamiento_fallback,
        })

    def _validar_respuesta(raw):
        data = _parsear_json(raw)
        accion = data.get("accion")
        if accion not in ("avanzar", "repreguntar", "generar_plan", "salir"):
            raise ValueError(f"accion invalida: {accion}")
        if accion == "repreguntar" and not repreguntas_disponibles:
            raise ValueError("el modelo repregunto sin repreguntas disponibles")
        data["es_salto"] = False
        if accion == "avanzar":
            salto = data.get("salto_semantico")
            if salto:
                if salto not in ids_salto_ofrecidos:
                    raise ValueError(f"salto_semantico '{salto}' no esta entre los saltos_posibles ofrecidos")
                if salto in visitados:
                    raise ValueError(f"salto_semantico '{salto}' ya fue visitado")
                data["camino"] = [salto]
                data["es_salto"] = True
            else:
                camino = data.get("camino") or []
                data["camino"] = _validar_camino(actual_id, camino, graph, visitados, nivel1_pool=nivel1)
            data["pregunta_necesaria"] = bool(data.get("pregunta_necesaria", True))
            if data["pregunta_necesaria"]:
                adaptada = (data.get("pregunta_adaptada") or "").strip()
                if not adaptada:
                    raise ValueError("pregunta_necesaria=true pero falta pregunta_adaptada")
                data["pregunta_adaptada"] = adaptada
            else:
                data["pregunta_adaptada"] = None
        pd = data.get("prioridad_declarada")
        if isinstance(pd, dict) and "texto" in pd and "conteo" in pd:
            data["prioridad_declarada"] = {"texto": str(pd["texto"]), "conteo": int(pd["conteo"])}
        else:
            data["prioridad_declarada"] = None
        nd = data.get("numeros_detectados")
        limpio = {}
        if isinstance(nd, dict):
            for campo, entry in nd.items():
                if campo not in CAMPOS_NUMERICOS_PROYECTO or not isinstance(entry, dict):
                    continue
                valor = entry.get("valor")
                if valor is None:
                    continue
                limpio[campo] = {
                    "valor": valor,
                    "unidad": entry.get("unidad"),
                    "texto_original": entry.get("texto_original"),
                }
        data["numeros_detectados"] = limpio or None
        tipo_oferta = data.get("tipo_oferta_detectado")
        data["tipo_oferta_detectado"] = tipo_oferta if tipo_oferta in TIPOS_OFERTA_VALIDOS else None
        unidad_venta = data.get("unidad_venta_detectada")
        data["unidad_venta_detectada"] = str(unidad_venta).strip() if unidad_venta else None
        razonamiento = data.get("razonamiento")
        data["razonamiento"] = str(razonamiento).strip() if razonamiento else None
        return data

    try:
        if historial_mensajes is not None:
            raw = llamar_claude_conversacion(SYSTEM_INTERPRETE_MULTI, historial_mensajes,
                                              json.dumps(ctx_turno, ensure_ascii=False), MODEL_HAIKU,
                                              max_tokens=700, componente="turnos")
        else:
            raw = llamar_claude(SYSTEM_INTERPRETE_MULTI, json.dumps(ctx_turno, ensure_ascii=False),
                                MODEL_HAIKU, max_tokens=700, componente="turnos")
    except Exception:
        return None  # fallo de red/presupuesto: unico caso que llega al menu de emergencia

    mensaje_error_previo = None
    try:
        resultado = _validar_respuesta(raw)
        _emitir_decision_turno(resultado)
        return resultado
    except Exception as error_validacion:
        mensaje_error_previo = str(error_validacion)  # el except borra la variable al salir; guardarla antes

    # El reintento y el respaldo tier-2 SIEMPRE usan el contexto completo y
    # aislado (llamar_claude clasico): no tocan historial_mensajes, para no
    # comprometer la conversacion cacheada con un intento invalido.
    ids_validos = [n["id"] for n in nivel1]
    for n in nivel1:
        ids_validos += [h["id"] for h in n.get("sucesores", [])]
    ctx_retry = dict(ctx_completo)
    ctx_retry["error_previo"] = mensaje_error_previo
    ctx_retry["ids_validos"] = ids_validos

    try:
        raw2 = llamar_claude(SYSTEM_INTERPRETE_MULTI, json.dumps(ctx_retry, ensure_ascii=False),
                             MODEL_HAIKU, max_tokens=700, componente="turnos")
        resultado = _validar_respuesta(raw2)
        _emitir_decision_turno(resultado)
        return resultado
    except Exception as segundo_error:
        candidato = _elegir_por_afinidad(nivel1_ids, graph, respuesta_usuario, perfil_sesion)
        if candidato is None:
            return None  # no hay ni un candidato para auto-elegir: recien ahi, menu de emergencia
        if registrar_evento:
            registrar_evento({
                "tipo": "fallback_auto", "nodo_actual": actual_id,
                "candidato_elegido": candidato, "motivo": str(segundo_error),
            })
        # Unica excepcion a "la pregunta cruda del cache nunca se muestra":
        # este es el ultimo recurso SILENCIOSO (sin menu visible) tras dos
        # fallos seguidos del modelo; no hay pregunta_adaptada que rescatar.
        pregunta_fallback = obtener_pregunta(candidato, graph[candidato], preguntas_cache)
        resultado = {"accion": "avanzar", "camino": [candidato], "pregunta_necesaria": True,
                     "pregunta_adaptada": pregunta_fallback, "perfil_update": None,
                     "prioridad_declarada": prioridad_declarada_actual, "es_salto": False}
        _emitir_decision_turno(resultado, razonamiento_fallback="fallback automatico tras 2 respuestas invalidas del modelo")
        return resultado


def _menu_emergencia(nivel1_ids, graph):
    ops = []
    for c in nivel1_ids:
        cn = graph[c]
        cond = (cn.get("condiciones_activacion") or [""])[0]
        pista = f"  <- si: {cond[:70]}" if cond else ""
        ops.append(f"{cn['titulo_concepto']}{pista}")
    r = preguntar_opcion("¿Hacia dónde seguimos? (modo de emergencia, sin IA)", ops,
                         extra="P. Generar mi plan ahora   Q. Salir sin plan")
    if r == "Q":
        return {"accion": "salir", "camino": [], "pregunta_necesaria": True, "perfil_update": None}
    if r == "P":
        return {"accion": "generar_plan", "camino": [], "pregunta_necesaria": True, "perfil_update": None}
    return {"accion": "avanzar", "camino": [nivel1_ids[r]], "pregunta_necesaria": True, "perfil_update": None}


def _detectar_decision_plan(respuesta):
    """Clasifica una respuesta libre como 'generar_ya' (el usuario quiere su
    plan) o 'continuar'. Reutilizado por preguntar_profundizar (la oferta
    inicial de profundizar) y por extender_sigamos_dirigido (Fase 2.9: la
    intencion de salida del usuario se respeta tambien DENTRO de la
    extension dirigida, turno a turno, no solo al ofrecerla)."""
    if API_KEY:
        try:
            raw = llamar_claude(SYSTEM_PROFUNDIZAR, respuesta, MODEL_HAIKU, max_tokens=100, componente="turnos")
            data = _parsear_json(raw)
            if data.get("decision") in ("generar_ya", "continuar"):
                return data["decision"]
        except Exception as e:
            print(f"  (fallo la interpretacion, uso deteccion simple: {e})")
    low = respuesta.strip().lower()
    if any(p in low for p in ("ya", "ahora", "dame", "listo", "asi esta bien", "así está bien")):
        return "generar_ya"
    return "continuar"


def preguntar_profundizar(familias_faltantes):
    """Ofrece UNA vez la disyuntiva plan-inicial-ya vs. seguir profundizando."""
    faltan_txt = "; ".join(familias_faltantes)
    mensaje = (
        f"Puedo darte tu plan ahora mismo. Eso si: con algunas preguntas mas "
        f"incluiria {faltan_txt}. ¿Seguimos un poco o lo quieres ya?"
    )
    respuesta = leer_entrada("\n" + mensaje + "\n> ")
    return _detectar_decision_plan(respuesta)


FAMILIA_QUERY_BRUJULA = {
    "accion_clientes": "validar con clientes reales, conseguir la primera venta, preventa, prueba de pago",
    "viabilidad_economica": "costos, precios, punto de equilibrio, rentabilidad, margen, cuanto cobrar",
}


def pregunta_dirigida(nid, graph, preguntas_cache, perfil_sesion, ultimas_preguntas):
    """Pregunta adaptada para un nodo elegido por la brujula en una
    extension dirigida (Fase 2.8 'sigamos'), sin pasar por el contrato
    completo del interprete (no hay camino/salto que decidir aqui: el nodo
    ya se eligio por afinidad a la familia faltante)."""
    plano = obtener_pregunta(nid, graph[nid], preguntas_cache)
    if not API_KEY:
        return plano
    ctx = {
        "perfil_sesion": perfil_sesion,
        "pregunta_cache": plano,
        "ultimas_preguntas_hechas": (ultimas_preguntas or [])[-3:],
    }
    try:
        return llamar_claude(SYSTEM_PREGUNTA_DIRIGIDA, json.dumps(ctx, ensure_ascii=False), MODEL_HAIKU,
                             max_tokens=150, componente="turnos").strip() or plano
    except Exception:
        return plano


def extender_sigamos_dirigido(graph, families, visitados, ruta, modos, perfil_sesion, texto_original,
                               familias_faltantes, preguntas_cache, ultimas_preguntas, session_id,
                               project_id, db_session_id, es_seguimiento, estado_vivo_previo,
                               fallback_events, prioridad_declarada):
    """Fase 2.8: cuando el usuario acepta profundizar ('sigamos'), en vez de
    devolver el control al interprete de navegacion local (que puede
    toparse con MAX_DEPTH sin alcanzar a preguntar nada — la promesa rota
    de 'sigamos un poco mas' detectada en la auditoria de Fase 2.7), la
    brujula semantica elige directamente 2-3 nodos de las familias que
    faltan y los conversa como extension, permitida por encima de
    MAX_DEPTH. Muta ruta/modos/visitados en el sitio. Si no encuentra
    candidatos genuinos de esas familias, NO finge continuar: devuelve
    hubo_extension=False para que el llamador lo diga honestamente.
    Fase 2.9: cada respuesta pasa por _detectar_decision_plan — al primer
    'dame mi plan' (o equivalente) DENTRO de la extension, corta de
    inmediato en vez de forzar las preguntas restantes (la version inversa
    de la promesa rota: ignorar la salida del usuario)."""
    query = " ".join(FAMILIA_QUERY_BRUJULA.get(f, f) for f in familias_faltantes)
    candidatos = buscar_afines(query, visitados, k=20, graph=graph)
    candidatos_familia = [nid for nid in candidatos if families.get(nid) in familias_faltantes]
    if not candidatos_familia:
        # Respaldo sin brujula (libreria no instalada o candidatos agotados):
        # busca directamente por tag de familia entre todo el grafo.
        candidatos_familia = [
            nid for nid in graph
            if nid not in visitados and families.get(nid) in familias_faltantes
            and _dominio_permitido(nid, graph, None)
        ]
    elegidos = candidatos_familia[:MAX_TURNOS_EXTRA_SIGAMOS_DIRIGIDO]

    if not elegidos:
        return {"hubo_extension": False, "perfil_sesion": perfil_sesion, "ultimas_preguntas": ultimas_preguntas}

    print("\nPerfecto, sigamos un poco mas.")
    for nid in elegidos:
        n = graph[nid]
        visitados.add(nid)
        ruta.append(nid)
        modos.append("conversado")
        _imprimir_nodo(len(ruta), MAX_DEPTH, n, "conversado (extension dirigida)", con_resumen=True)
        pregunta = pregunta_dirigida(nid, graph, preguntas_cache, perfil_sesion, ultimas_preguntas)
        respuesta = leer_entrada("\n" + pregunta + "\n> ")
        ultimas_preguntas = (ultimas_preguntas + [pregunta])[-3:]
        if _detectar_decision_plan(respuesta) == "generar_ya":
            # El usuario pidio su plan a mitad de la extension: se corta de
            # inmediato, sin forzar las preguntas restantes. Lo que no se
            # alcanzo a cubrir queda autodeclarado como pendiente (Fase 2.8).
            guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, True,
                           project_id, db_session_id, es_seguimiento, estado_vivo_previo, fallback_events,
                           prioridad_declarada)
            return {"hubo_extension": True, "perfil_sesion": perfil_sesion, "ultimas_preguntas": ultimas_preguntas}
        perfil_sesion = (perfil_sesion + "\n" + f"Sobre {n['titulo_concepto']}: {respuesta}").strip()
        guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, True,
                       project_id, db_session_id, es_seguimiento, estado_vivo_previo, fallback_events,
                       prioridad_declarada)
    return {"hubo_extension": True, "perfil_sesion": perfil_sesion, "ultimas_preguntas": ultimas_preguntas}


MAX_COSECHA = 25
_STOPWORDS_COSECHA = set(
    "de la el en y a los las que para con su sus un una como al del por se es "
    "son o u e no ya mas tu tus este esta estos estas".split()
)


def _tokens_cosecha(texto):
    nfkd = unicodedata.normalize("NFKD", texto.lower())
    ascii_txt = "".join(c for c in nfkd if not unicodedata.combining(c))
    return set(w for w in re.findall(r"[a-z0-9]+", ascii_txt) if w not in _STOPWORDS_COSECHA and len(w) > 2)


MAX_COSECHA_PRIORIDAD = 8


def cosechar_vecindario(ruta, graph, families, evaluacion, perfil_sesion, prioridad_declarada=None, tope=MAX_COSECHA):
    """Expande desde la ruta (conversada + silenciosa) hacia nodos_siguientes y
    nodos_previos adyacentes, sin preguntar nada, y devuelve hasta `tope`
    priorizados por: familia que le falte a la ruta, fase mayoritaria de la
    ruta, y afinidad de palabras clave con el perfil_sesion.
    Fase 2.7: si hay prioridad_declarada (el bloqueo que el usuario repitio),
    reserva hasta MAX_COSECHA_PRIORIDAD cupos para nodos afines a esa
    prioridad ANTES de aplicar el puntaje normal, para que el plan tenga
    material tecnico concreto sobre el frente que el usuario mismo senalo."""
    ruta_set = set(ruta)
    candidatos = set()
    for nid in ruta:
        n = graph[nid]
        for vecino in n.get("nodos_siguientes", []) + n.get("nodos_previos", []):
            if vecino in graph and vecino not in ruta_set and _dominio_permitido(vecino, graph, None):
                candidatos.add(vecino)

    fases_ruta = [graph[nid].get("fase_proyecto") for nid in ruta if nid in graph]
    fase_mayoritaria = max(set(fases_ruta), key=fases_ruta.count) if fases_ruta else None

    familias_faltantes = set()
    if not evaluacion["tiene_accion_clientes"]:
        familias_faltantes.add("accion_clientes")
    if not evaluacion["tiene_viabilidad_economica"]:
        familias_faltantes.add("viabilidad_economica")

    perfil_tokens = _tokens_cosecha(perfil_sesion) if perfil_sesion else set()

    seleccionados = []
    candidatos_restantes = set(candidatos)

    texto_prioridad = (prioridad_declarada or {}).get("texto") if prioridad_declarada else None
    if texto_prioridad:
        prioridad_tokens = _tokens_cosecha(texto_prioridad)
        if prioridad_tokens:
            def afinidad_prioridad(nid):
                n = graph[nid]
                texto_nodo = (n.get("titulo_concepto", "") + " " + n.get("resumen_teorico", "")[:300] + " "
                              + " ".join(n.get("condiciones_activacion", [])))
                return len(prioridad_tokens & _tokens_cosecha(texto_nodo))

            reservados = [nid for nid in candidatos_restantes if afinidad_prioridad(nid) > 0]
            reservados.sort(key=afinidad_prioridad, reverse=True)
            reservados = reservados[:MAX_COSECHA_PRIORIDAD]
            seleccionados.extend(reservados)
            candidatos_restantes -= set(reservados)

    def puntaje(nid):
        n = graph[nid]
        p = 0
        if families.get(nid) in familias_faltantes:
            p += 10
        if n.get("fase_proyecto") == fase_mayoritaria:
            p += 3
        if perfil_tokens:
            texto_nodo = n.get("titulo_concepto", "") + " " + " ".join(n.get("condiciones_activacion", []))
            p += len(perfil_tokens & _tokens_cosecha(texto_nodo))
        return p

    resto = sorted(candidatos_restantes, key=puntaje, reverse=True)
    seleccionados.extend(resto[: max(0, tope - len(seleccionados))])
    return seleccionados[:tope]


_TEXTO_FAMILIA_FALTANTE = {
    "accion_clientes": "validar con clientes reales (entrevistas, MVP, pruebas de usuario, una venta o preventa real)",
    "viabilidad_economica": "si tu idea puede sostenerse economicamente (costos, precios, punto de equilibrio)",
}

SECCION_ECONOMICA_TITULO = "¿Puede sostenerse tu idea?"


def _corregir_coherencia_cobertura(evaluacion_cobertura, cuerpo, tiene_material_economico, registrar_evento=None):
    """Post-validador MECANICO (Motor v2.2) de la incoherencia etiqueta/
    contenido: si el material ya traia al menos un concepto de viabilidad
    economica Y el redactor efectivamente escribio la seccion fija de
    sostenibilidad (regla 4 de SYSTEM_PLAN), 'viabilidad_economica' NUNCA
    puede aparecer en 'Lo que este plan aun no cubre' -- sin importar lo
    que el redactor autodeclaro en su bloque ===JSON=== (regla 11). Tercera
    reincidencia de este bug (Fase 2.5, Fase 2.8, sesion en vivo del
    fundador de la app de I Ching: el plan traia la seccion de numeros con
    contenido real, pero la autodeclaracion igual listaba viabilidad_
    economica como no cubierta). Ya no depende de que el modelo lo declare
    bien: se verifica contra el propio markdown generado, en codigo."""
    seccion_presente = tiene_material_economico and SECCION_ECONOMICA_TITULO in cuerpo
    if seccion_presente and not evaluacion_cobertura["tiene_viabilidad_economica"]:
        if registrar_evento:
            registrar_evento({"tipo": "coherencia_cobertura_corregida", "familia": "viabilidad_economica"})
        evaluacion_cobertura = dict(evaluacion_cobertura)
        evaluacion_cobertura["tiene_viabilidad_economica"] = True
        evaluacion_cobertura["familias_faltantes"] = [
            f for f in evaluacion_cobertura["familias_faltantes"]
            if f != _TEXTO_FAMILIA_FALTANTE["viabilidad_economica"]
        ]
        evaluacion_cobertura["es_completa"] = (
            evaluacion_cobertura["tiene_accion_clientes"] and evaluacion_cobertura["tiene_viabilidad_economica"]
        )
    return evaluacion_cobertura


def _parsear_autodeclaracion(raw):
    """Separa el markdown del plan del bloque final ===JSON=== (Fase 2.8,
    autodeclaracion de cobertura). Si el delimitador falta, devuelve (raw
    completo, None). Si el delimitador SI aparece pero el JSON es invalido
    (Hotfix v2.2.1: la causa real es un ===JSON=== cortado por max_tokens),
    devuelve el cuerpo YA SEPARADO (sin el marcador ni el JSON roto) en vez
    de raw completo -- de lo contrario el usuario veria el marcador y el
    JSON truncado colgando al final de su plan. En ambos casos
    autodeclaracion=None, y la llamada trata eso como "sin autodeclaracion"
    mas abajo (respaldo por encabezados, ver _familias_desde_encabezados)."""
    if "===JSON===" not in raw:
        return raw.strip(), None
    cuerpo, _, bloque = raw.rpartition("===JSON===")
    try:
        data = _parsear_json(bloque)
    except Exception:
        return cuerpo.strip(), None
    return cuerpo.strip(), data


def _evaluacion_desde_autodeclaracion(autodeclaracion):
    """Construye el mismo shape que plan_readiness.evaluar_ruta, pero a
    partir de lo que el REDACTOR declaro que el plan realmente trata (Fase
    2.8), no de tags de node_families sobre la ruta/cosecha. Esta es la
    UNICA fuente para la etiqueta del plan y la seccion 'no cubre' -
    coherente por construccion, imposible de desincronizar del contenido
    real."""
    tratadas = set((autodeclaracion or {}).get("familias_tratadas") or [])
    tiene_accion = "accion_clientes" in tratadas
    tiene_viabilidad = "viabilidad_economica" in tratadas
    faltantes = [_TEXTO_FAMILIA_FALTANTE[f] for f in ("accion_clientes", "viabilidad_economica")
                 if f not in tratadas]
    return {
        "es_completa": tiene_accion and tiene_viabilidad,
        "tiene_accion_clientes": tiene_accion,
        "tiene_viabilidad_economica": tiene_viabilidad,
        "familias_faltantes": faltantes,
    }


def _familias_desde_encabezados(cuerpo):
    """Respaldo deterministico (Hotfix v2.2.1) cuando la autodeclaracion de
    la regla 11 falta o no parsea (causa raiz real: un ===JSON=== cortado
    por max_tokens en una sesion en vivo). A diferencia del respaldo
    anterior (plan_readiness.evaluar_ruta sobre ruta+cosecha_ids), este NO
    mira los tags de node_families del material de ENTRADA -- el redactor
    puede omitir parte de material_de_apoyo si "no encaja con claridad en
    ninguna etapa" (regla 2), asi que un tag de entrada no garantiza que la
    familia realmente quedo cubierta en la SALIDA. En vez de eso, escanea
    los encabezados REALES del markdown ya generado con las mismas
    palabras clave de plan_readiness. viabilidad_economica ademas se
    confirma por la presencia exacta de la seccion fija de sostenibilidad
    (regla 4), la misma senal que ya usa _corregir_coherencia_cobertura."""
    encabezados = [linea for linea in cuerpo.splitlines() if linea.strip().startswith("#")]
    texto_encabezados = plan_readiness._normalizar(" ".join(encabezados))
    tiene_accion = plan_readiness._coincide(texto_encabezados, plan_readiness.KEYWORDS_ACCION_CLIENTES)
    tiene_viabilidad = (
        SECCION_ECONOMICA_TITULO in cuerpo
        or plan_readiness._coincide(texto_encabezados, plan_readiness.KEYWORDS_VIABILIDAD_ECONOMICA)
    )
    faltantes = [
        _TEXTO_FAMILIA_FALTANTE[f]
        for f, cubierta in (("accion_clientes", tiene_accion), ("viabilidad_economica", tiene_viabilidad))
        if not cubierta
    ]
    return {
        "es_completa": tiene_accion and tiene_viabilidad,
        "tiene_accion_clientes": tiene_accion,
        "tiene_viabilidad_economica": tiene_viabilidad,
        "familias_faltantes": faltantes,
    }


def _verificar_procedencia_etapas(autodeclaracion, ruta, cosecha_ids, registrar_evento=None):
    """Fase 3.1 (caja de vidrio): el redactor autodeclara, por etapa
    numerada, que node_ids de material_principal/material_de_apoyo uso
    realmente (regla de FORMATO DE SALIDA, campo 'etapas'). Verifica
    deterministicamente que cada id declarado pertenezca al material que
    de verdad se le entrego (ruta + cosecha) -- si el modelo inventa un id
    que nunca vino en el payload, es una alucinacion de procedencia, y se
    registra 'procedencia_invalida' para revision humana (no bloquea el
    plan: la seccion ya se escribio, esto es observabilidad, no un
    guardian que aborte)."""
    etapas = (autodeclaracion or {}).get("etapas")
    if not isinstance(etapas, dict) or not etapas:
        return
    material_valido = set(ruta) | set(cosecha_ids)
    for etapa, ids in etapas.items():
        if not isinstance(ids, list):
            continue
        invalidos = [nid for nid in ids if nid not in material_valido]
        if invalidos and registrar_evento:
            registrar_evento({
                "tipo": "procedencia_invalida", "etapa": str(etapa), "ids_invalidos": invalidos,
            })


def _extraer_seccion_economica(cuerpo):
    """Fase 3.1: la seccion financiera del plan (desde el encabezado fijo
    SECCION_ECONOMICA_TITULO hasta el proximo encabezado o el final), para
    acotar el verificador de numeros huerfanos a la parte del plan que
    realmente habla de dinero -- el resto del plan (numeracion de etapas,
    conteos de conceptos) no deberia entrar a este chequeo."""
    idx = cuerpo.find(SECCION_ECONOMICA_TITULO)
    if idx == -1:
        return ""
    resto = cuerpo[idx:]
    lineas = resto.split("\n")
    fin = len(lineas)
    for i, linea in enumerate(lineas):
        if i > 0 and linea.strip().startswith("#"):
            fin = i
            break
    return "\n".join(lineas[:fin])


def ensamblar_plan(ruta, graph, perfil_sesion, texto_original, families, evaluacion, session_id,
                    es_seguimiento=False, estado_vivo_previo=None, prioridad_declarada=None,
                    registrar_evento=None, numeros_proyecto=None):
    """`evaluacion` (ruta-solo, por tags de node_families) decide QUE
    cosechar (familia faltante como prioridad) - eso se conserva para el
    medidor de oferta previa ("quieres continuar") y para priorizar la
    cosecha. La etiqueta inicial/completo y la seccion "no cubre" YA NO se
    derivan de tags: vienen de la autodeclaracion del propio redactor
    (Fase 2.8, _evaluacion_desde_autodeclaracion) sobre lo que el plan
    realmente contiene, eliminando la clase de bug donde el plan trataba
    una familia pero la etiqueta decia lo contrario. Devuelve un dict con
    el markdown y los metadatos de cosecha/cobertura, para persistencia.
    Fase 2.7: prioridad_declarada (el bloqueo que el usuario repitio) se
    pasa a la cosecha (reserva cupos afines) y al redactor (bloqueo_declarado
    en el payload), para que el plan le de tratamiento explicito."""
    def a_material(nid):
        n = graph[nid]
        return {
            "id": nid,
            "concepto": n["titulo_concepto"],
            "pasos": n.get("pasos_accionables", []),
            "entregable": n.get("entregable_esperado", ""),
            "es_viabilidad_economica": families.get(nid) == "viabilidad_economica",
        }

    material_principal = [a_material(nid) for nid in ruta]
    cosecha_ids = cosechar_vecindario(ruta, graph, families, evaluacion, perfil_sesion, prioridad_declarada)
    material_de_apoyo = [a_material(nid) for nid in cosecha_ids]
    tiene_material_economico = any(m["es_viabilidad_economica"] for m in material_principal + material_de_apoyo)

    autodeclaracion = None
    if API_KEY:
        payload = {
            "entrada_original": texto_original,
            "perfil_sesion": perfil_sesion,
            "material_principal": material_principal,
            "material_de_apoyo": material_de_apoyo,
            "bloqueo_declarado": (prioridad_declarada or {}).get("texto") if prioridad_declarada else None,
        }
        if es_seguimiento:
            payload["es_seguimiento"] = True
            payload["estado_vivo_previo"] = estado_vivo_previo
        try:
            raw = llamar_claude(SYSTEM_PLAN, json.dumps(payload, ensure_ascii=False), MODEL,
                                max_tokens=5000, componente="plan")
            cuerpo, autodeclaracion = _parsear_autodeclaracion(raw)
        except Exception as e:
            print(f"  (fallo el redactor con IA, ensamblo offline: {e})")
            cuerpo = _ensamblar_offline(material_principal, perfil_sesion, texto_original)
    else:
        cuerpo = _ensamblar_offline(material_principal, perfil_sesion, texto_original)

    if autodeclaracion is not None:
        evaluacion_cobertura = _evaluacion_desde_autodeclaracion(autodeclaracion)
    else:
        # Hotfix v2.2.1: la autodeclaracion de la regla 11 falta o no
        # parseo (causa raiz real: un ===JSON=== cortado por max_tokens en
        # una sesion en vivo; tambien cubre el respaldo offline sin IA).
        # Escanea los encabezados REALES del cuerpo ya generado en vez de
        # volver a los tags de node_families sobre ruta+cosecha_ids (el
        # material de ENTRADA, que el redactor puede omitir parcialmente
        # segun la regla 2) -- JAMAS se degrada la etiqueta solo porque el
        # JSON de cola se corto.
        evaluacion_cobertura = _familias_desde_encabezados(cuerpo)
        if registrar_evento:
            registrar_evento({"tipo": "autodeclaracion_fallida"})

    _verificar_procedencia_etapas(autodeclaracion, ruta, cosecha_ids, registrar_evento=registrar_evento)

    # Fase 3.1 (caja de vidrio): igual que en el reporte, pero acotado a la
    # seccion financiera del plan -- el redactor no corre calculadora.py,
    # asi que el conjunto permitido es lo declarado por el usuario mas lo
    # que el propio material del grafo ya menciona (un ejemplo teorico del
    # nodo no es un numero inventado).
    seccion_economica = _extraer_seccion_economica(cuerpo)
    if seccion_economica:
        textos_material = [
            t for m in (material_principal + material_de_apoyo)
            for t in (m.get("pasos", []) + [m.get("entregable", "")])
        ]
        numeros_permitidos_plan = verificador_huerfanos.cerradura_aritmetica(
            verificador_huerfanos.numeros_declarados(numeros_proyecto)
            | verificador_huerfanos.numeros_de_material(textos_material)
        )
        verificador_huerfanos.verificar_numeros_huerfanos(
            seccion_economica, numeros_permitidos_plan, registrar_evento=registrar_evento)

    evaluacion_cobertura = _corregir_coherencia_cobertura(
        evaluacion_cobertura, cuerpo, tiene_material_economico, registrar_evento=registrar_evento)

    etiqueta = "Plan completo" if evaluacion_cobertura["es_completa"] else "Plan inicial"
    total_conceptos = len(ruta) + len(cosecha_ids)
    partes = [f"_{etiqueta}_", "", cuerpo]
    partes += ["", "---", f"_Este plan se alimento de {total_conceptos} conceptos: "
                          f"{len(ruta)} de tu recorrido conversado y {len(cosecha_ids)} "
                          f"del vecindario relacionado del grafo._"]
    if not evaluacion_cobertura["es_completa"]:
        partes += ["", "## Lo que este plan aun no cubre", ""]
        for f in evaluacion_cobertura["familias_faltantes"]:
            partes.append(f"- {f}")
        partes += ["", f"Para profundizar, continua la sesion: "
                        f"`python engine/prototipo_motor.py --continuar {session_id}`"]
    return {
        "markdown": "\n".join(partes),
        "cosecha_ids": cosecha_ids,
        "evaluacion_cobertura": evaluacion_cobertura,
    }


def _ensamblar_offline(material, perfil_sesion, texto_original):
    out = ["# Tu plan de accion", ""]
    if texto_original or perfil_sesion:
        out.append("## Contexto")
        if texto_original:
            out.append(f"Punto de partida: {texto_original}")
        if perfil_sesion:
            out.append(f"Lo que sabemos de tu idea: {perfil_sesion}")
        out.append("")
    for i, m in enumerate(material, 1):
        out.append(f"## Etapa {i}: {m['concepto']}")
        for j, p in enumerate(m["pasos"], 1):
            out.append(f"  {i}.{j} {p}")
        if m["entregable"]:
            out.append(f"  Punto de control: {m['entregable']}")
        out.append("")
    return "\n".join(out)


def comprimir_estado_vivo(estado_anterior, perfil_sesion_nueva, conceptos_nuevos_titulos):
    """Comprime estado_anterior + novedades de la sesion en un estado_vivo
    nuevo de 300-500 tokens. Respaldo offline: concatena sin comprimir."""
    if API_KEY:
        ctx = {
            "estado_vivo_anterior": estado_anterior,
            "perfil_actualizado_esta_sesion": perfil_sesion_nueva,
            "conceptos_nuevos_cubiertos": conceptos_nuevos_titulos,
        }
        try:
            return llamar_claude(SYSTEM_ESTADO_VIVO, json.dumps(ctx, ensure_ascii=False), MODEL_HAIKU,
                                 max_tokens=700, componente="estado_vivo").strip()
        except Exception as e:
            print(f"  (fallo comprimir estado_vivo, uso respaldo sin comprimir: {e})")
    return (estado_anterior + "\n" + perfil_sesion_nueva).strip() if estado_anterior else perfil_sesion_nueva


def evaluar_calidad_sesion(decisiones, graph, muestreo=None):
    """Fase 3.1 (caja de vidrio): juez de sesion muestreado (Haiku,
    ~$0.003/sesion). Revisa la bitacora de decision_turno de la sesion
    (candidatos locales, saltos_posibles con sus scores, la decision
    tomada, la respuesta del usuario y el razonamiento del interprete en
    cada paso) y devuelve una señal de triage -- NUNCA bloquea ni decide
    nada, solo marca sesiones para revision humana despues. Devuelve None
    si no se muestreo esta sesion, si no hay API_KEY, o si la llamada
    fallo (la ausencia de veredicto no es un problema: es simplemente una
    sesion sin revisar, igual que antes de que existiera esta pieza)."""
    muestreo = JUEZ_SESION_MUESTREO if muestreo is None else muestreo
    if not API_KEY or random.random() >= muestreo:
        return None
    turnos_decision = [d for d in (decisiones or []) if d.get("tipo") == "decision_turno"]
    if not turnos_decision:
        return None

    def _titulo(nid):
        return graph[nid]["titulo_concepto"] if nid in graph else nid

    turnos = []
    for d in turnos_decision:
        decision = d.get("decision") or {}
        camino = decision.get("camino") or []
        turnos.append({
            "nodo": _titulo(d["nodo_actual"]) if d.get("nodo_actual") else None,
            "destino": [_titulo(nid) for nid in camino],
            "es_salto": decision.get("es_salto", False),
            "candidatos_locales": [_titulo(nid) for nid in d.get("candidatos_locales") or []],
            "saltos_posibles": [
                {"titulo": s.get("titulo"), "afinidad": s.get("afinidad")}
                for s in d.get("saltos_posibles") or []
            ],
            "respuesta_usuario": d.get("respuesta_usuario"),
            "razonamiento": d.get("razonamiento"),
        })
    try:
        raw = llamar_claude(SYSTEM_JUEZ_SESION, json.dumps({"turnos": turnos}, ensure_ascii=False),
                            MODEL_HAIKU, max_tokens=400, componente="juez_sesion")
        return _parsear_json(raw)
    except Exception as e:
        print(f"  (fallo el juez de sesion, se omite calidad: {e})")
        return None


def organizador_gratuito(texto_original, entry_seeds, graph):
    """Capa gratuita: UNA llamada Haiku que organiza sin instruir.
    Devuelve (markdown, data_dict) o (None, mensaje_error)."""
    puertas = [
        {"id": s, "fase": graph[s]["fase_proyecto"], "titulo": graph[s]["titulo_concepto"],
         "resumen": graph[s]["resumen_teorico"][:150]}
        for s in entry_seeds
    ]
    ctx = {"texto_usuario": texto_original, "puertas": puertas}
    try:
        raw = llamar_claude(SYSTEM_ORGANIZADOR, json.dumps(ctx, ensure_ascii=False), MODEL_HAIKU,
                            max_tokens=600, componente="organizador")
        data = _parsear_json(raw)
    except Exception as e:
        return None, f"  (fallo el organizador con IA: {e})"

    out = [
        "# Organizador de tu idea", "",
        f"**En una frase:** {data.get('idea_en_una_frase', '')}", "",
        f"**Etapa detectada:** {data.get('etapa_detectada', '')}", "",
        "## Lo que ya tienes claro",
    ]
    for b in data.get("lo_que_ya_tienes_claro", []) or []:
        out.append(f"- {b}")
    out += ["", "## Lo que estás asumiendo sin saberlo"]
    for b in data.get("lo_que_estas_asumiendo_sin_saberlo", []) or []:
        out.append(f"- {b}")
    out += ["", "## Áreas que cubriría tu plan completo"]
    for b in data.get("areas_que_cubriria_tu_plan_completo", []) or []:
        out.append(f"- {b}")
    return "\n".join(out), data


def candidatos_seguimiento(mensaje_nuevo, estado_vivo, fase_actual, families, graph, cubiertos, tope=30):
    """Candidatos de CUALQUIER parte del grafo (no solo las 20 puertas) que el
    proyecto aun no cubrio, priorizados por fase, familia sin cubrir y
    afinidad de palabras clave con el mensaje nuevo + estado_vivo."""
    orden = {"ideacion": 0, "validacion": 1, "planificacion": 2, "ejecucion": 3}
    fase_idx = orden.get(fase_actual, 0)
    conteo_fam = {}
    for nid in cubiertos:
        f = families.get(nid, "general")
        conteo_fam[f] = conteo_fam.get(f, 0) + 1
    contexto_tokens = _tokens_cosecha((mensaje_nuevo or "") + " " + (estado_vivo or ""))

    def puntaje(nid):
        n = graph[nid]
        p = 0
        f_nodo = orden.get(n.get("fase_proyecto"), 0)
        if f_nodo == fase_idx:
            p += 5
        elif f_nodo == fase_idx + 1:
            p += 3
        fam = families.get(nid, "general")
        if fam != "general" and conteo_fam.get(fam, 0) == 0:
            p += 6
        if contexto_tokens:
            texto_nodo = n.get("titulo_concepto", "") + " " + " ".join(n.get("condiciones_activacion", []))
            p += len(contexto_tokens & _tokens_cosecha(texto_nodo))
        return p

    candidatos = [nid for nid in graph if nid not in cubiertos]
    return sorted(candidatos, key=puntaje, reverse=True)[:tope]


def seleccionar_puerta_avanzada(mensaje_nuevo, estado_vivo, fase_actual, families, graph, cubiertos, entry_seeds):
    """Capa 1 avanzada (--seguir): elige cualquier nodo del grafo aun no
    cubierto como punto de entrada de la sesion de seguimiento."""
    candidatos_ids = candidatos_seguimiento(mensaje_nuevo, estado_vivo, fase_actual, families, graph, cubiertos)
    if API_KEY and candidatos_ids:
        opciones = []
        for nid in candidatos_ids:
            n = graph[nid]
            opciones.append({
                "id": nid, "titulo": n["titulo_concepto"], "fase": n.get("fase_proyecto"),
                "resumen": n.get("resumen_teorico", "")[:150],
                "condiciones_activacion": n.get("condiciones_activacion", [])[:2],
            })
        ctx = {"estado_vivo": estado_vivo, "mensaje_nuevo": mensaje_nuevo, "candidatos": opciones}
        try:
            raw = llamar_claude(SYSTEM_PUERTA_AVANZADA, json.dumps(ctx, ensure_ascii=False), MODEL_HAIKU,
                                max_tokens=400, componente="clasificacion")
            data = _parsear_json(raw)
            if data["puerta_id"] in candidatos_ids:
                return data["puerta_id"], (data.get("perfil_sesion") or "").strip()
            raise ValueError(f"puerta_id fuera de los candidatos: {data.get('puerta_id')}")
        except Exception as e:
            print(f"  (fallo la clasificacion avanzada, uso el candidato de mayor puntaje: {e})")
    if candidatos_ids:
        return candidatos_ids[0], (estado_vivo or "")
    return next(iter(entry_seeds)), (estado_vivo or "")


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--continuar", metavar="SESSION_ID", default=None,
                    help="Retoma una sesion previa desde su ultimo nodo (engine/sessions/{id}.json)")
    ap.add_argument("--gratis", action="store_true",
                    help="Organizador gratuito: una sola llamada, sin entrevista")
    ap.add_argument("--seguir", metavar="PROJECT_ID", default=None,
                    help="Sesion de seguimiento de un proyecto existente")
    ap.add_argument("--offline", action="store_true",
                    help="Fuerza persistencia JSON local en engine/projects_local/ en vez de Supabase")
    ap.add_argument("--reporte", metavar="PROJECT_ID", default=None,
                    help="Reporte de Sostenibilidad del proyecto (motor v2.1): costos, margen, punto de equilibrio")
    return ap.parse_args()


def _imprimir_nodo(idx, total, node, modo, con_resumen=False):
    etiqueta = f"[{modo}]"
    print("\n" + "-" * 60)
    print(f"[{idx}/{total}] {etiqueta} {node['titulo_concepto']}")
    if con_resumen:
        print(textwrap.fill(node["resumen_teorico"], 76)[:600])
    else:
        print("  (cubierto por lo que ya contaste; no hace falta preguntarlo)")


def _extraer_titulo(plan_md):
    for line in plan_md.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return None


def ejecutar_recorrido(graph, families, preguntas_cache, actual_id, visitados, ruta, modos,
                       perfil_sesion, texto_original, session_id, project_id, db_session_id,
                       profundizar_ofrecido=False, pregunta_hecha=None, respuesta_usuario=None,
                       es_seguimiento=False, estado_vivo_previo=None, fallback_events=None,
                       prioridad_declarada=None):
    """Corre el bucle de entrevista (comun a proyecto nuevo y --seguir) hasta
    salir sin plan o ensamblar uno. Devuelve un dict con el resultado.
    Fase 2.7: mantiene historial_mensajes (conversacion cacheada turno a
    turno con el interprete, vive solo en memoria de esta corrida, no se
    persiste) y prioridad_declarada (si persiste entre turnos y entre
    --continuar, via guardar_sesion)."""
    repreguntas_usadas = 0
    fallback_events = list(fallback_events or [])
    ultimas_preguntas = []
    historial_mensajes = []
    numeros_detectados_sesion = {}
    tipo_oferta_sesion = None
    unidad_venta_sesion = None

    def _registrar_evento(evento):
        fallback_events.append(evento)

    while True:
        nivel1_ids = sucesores_nivel(actual_id, graph, visitados)
        if not nivel1_ids or len(ruta) >= MAX_DEPTH:
            motivo = "llegaste a un punto de cierre" if not nivel1_ids else "recorrido completo"
            print(f"\n({motivo}: generamos tu plan)")
            break

        resultado = interpretar_multi_salto(
            actual_id, graph, visitados, perfil_sesion, texto_original,
            pregunta_hecha, respuesta_usuario,
            repreguntas_disponibles=(repreguntas_usadas < MAX_REPREGUNTAS_POR_PUNTO),
            preguntas_cache=preguntas_cache, ultimas_preguntas=ultimas_preguntas,
            prioridad_declarada_actual=prioridad_declarada, historial_mensajes=historial_mensajes,
            registrar_evento=_registrar_evento,
        )
        if resultado is None:
            resultado = _menu_emergencia(nivel1_ids, graph)

        if resultado.get("perfil_update"):
            perfil_sesion = (perfil_sesion + "\n" + resultado["perfil_update"]).strip() if perfil_sesion else resultado["perfil_update"]
        if "prioridad_declarada" in resultado:
            prioridad_declarada = resultado["prioridad_declarada"] or prioridad_declarada
        if resultado.get("numeros_detectados"):
            # Motor v2.1: acumula lo detectado ESTE turno; session_id/updated_at
            # se agregan aqui (metadata de codigo, no algo que el modelo deba
            # inventar) y se mergean al proyecto en _persistir_resultado.
            for campo, entry in resultado["numeros_detectados"].items():
                numeros_detectados_sesion[campo] = {
                    "valor": entry["valor"], "unidad": entry.get("unidad"),
                    "texto_original": entry.get("texto_original"),
                    "session_id": db_session_id, "updated_at": datetime.now().isoformat(),
                }
        if resultado.get("tipo_oferta_detectado"):
            tipo_oferta_sesion = resultado["tipo_oferta_detectado"]
        if resultado.get("unidad_venta_detectada"):
            unidad_venta_sesion = resultado["unidad_venta_detectada"]

        if resultado["accion"] == "salir":
            print("\nHasta pronto.")
            return {"tipo": "salio", "ruta": ruta, "modos": modos, "perfil_sesion": perfil_sesion,
                    "fallback_events": fallback_events, "prioridad_declarada": prioridad_declarada,
                    "numeros_detectados_sesion": numeros_detectados_sesion,
                    "tipo_oferta_sesion": tipo_oferta_sesion, "unidad_venta_sesion": unidad_venta_sesion}

        if resultado["accion"] == "repreguntar":
            repreguntas_usadas += 1
            pregunta_hecha = resultado["repregunta"]
            guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido,
                           project_id, db_session_id, es_seguimiento, estado_vivo_previo, fallback_events,
                           prioridad_declarada, pregunta_hecha=pregunta_hecha)
            respuesta_usuario = leer_entrada("\n" + pregunta_hecha + "\n> ")
            ultimas_preguntas = (ultimas_preguntas + [pregunta_hecha])[-3:]
            continue

        if resultado["accion"] == "generar_plan":
            evaluacion = plan_readiness.evaluar_ruta(ruta, families)
            if not evaluacion["es_completa"] and not profundizar_ofrecido:
                profundizar_ofrecido = True
                guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido,
                               project_id, db_session_id, es_seguimiento, estado_vivo_previo, fallback_events,
                               prioridad_declarada)
                if preguntar_profundizar(evaluacion["familias_faltantes"]) == "continuar":
                    # Fase 2.8: extension DIRIGIDA por la brujula hacia las
                    # familias que faltan, en vez de devolver el control al
                    # riel local (que puede toparse con MAX_DEPTH sin
                    # preguntar nada — la "promesa rota" detectada en la
                    # auditoria de Fase 2.7). Prohibido fingir continuar.
                    # OJO: evaluacion["familias_faltantes"] son las FRASES
                    # legibles para el usuario (para preguntar_profundizar);
                    # extender_sigamos_dirigido necesita las claves cortas
                    # ("accion_clientes"/"viabilidad_economica") para poder
                    # comparar contra families.get(nid), no el texto largo.
                    familias_faltantes_keys = []
                    if not evaluacion["tiene_accion_clientes"]:
                        familias_faltantes_keys.append("accion_clientes")
                    if not evaluacion["tiene_viabilidad_economica"]:
                        familias_faltantes_keys.append("viabilidad_economica")
                    extension = extender_sigamos_dirigido(
                        graph, families, visitados, ruta, modos, perfil_sesion, texto_original,
                        familias_faltantes_keys, preguntas_cache, ultimas_preguntas, session_id,
                        project_id, db_session_id, es_seguimiento, estado_vivo_previo, fallback_events,
                        prioridad_declarada,
                    )
                    perfil_sesion = extension["perfil_sesion"]
                    ultimas_preguntas = extension["ultimas_preguntas"]
                    if not extension["hubo_extension"]:
                        print("\ncon lo que tenemos alcanza para el plan; la parte "
                              "que falta quedara señalada como pendiente.")
                    break
            break

        # accion == "avanzar": camino de 1-3 nodos, algunos silenciosos + a lo sumo uno conversado al final
        # (o un unico nodo de salto semantico, Fase 2.8, etiquetado "salto")
        camino = resultado["camino"]
        pregunta_necesaria = resultado["pregunta_necesaria"]
        es_salto = resultado.get("es_salto", False)
        for idx, nid in enumerate(camino):
            es_ultimo = idx == len(camino) - 1
            if es_salto:
                modo = "salto"
            else:
                modo = "conversado" if (es_ultimo and pregunta_necesaria) else "silencioso"
            visitados.add(nid)
            ruta.append(nid)
            modos.append(modo)
            # Un salto SILENCIOSO (pregunta_necesaria=false) igual se
            # imprime inline, igual que un nodo silencioso normal, para que
            # el usuario (y la transcripcion) siempre vean que hubo un
            # salto — nunca pasa desapercibido.
            if modo == "silencioso" or (modo == "salto" and not (es_ultimo and pregunta_necesaria)):
                _imprimir_nodo(len(ruta), MAX_DEPTH, graph[nid], modo, con_resumen=False)
        actual_id = camino[-1]
        repreguntas_usadas = 0
        guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido,
                       project_id, db_session_id, es_seguimiento, estado_vivo_previo, fallback_events,
                       prioridad_declarada)

        if pregunta_necesaria:
            n = graph[actual_id]
            _imprimir_nodo(len(ruta), MAX_DEPTH, n, modos[-1], con_resumen=True)
            pregunta_hecha = resultado.get("pregunta_adaptada") or obtener_pregunta(actual_id, n, preguntas_cache)
            guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido,
                           project_id, db_session_id, es_seguimiento, estado_vivo_previo, fallback_events,
                           prioridad_declarada, pregunta_hecha=pregunta_hecha)
            respuesta_usuario = leer_entrada("\n" + pregunta_hecha + "\n> ")
            ultimas_preguntas = (ultimas_preguntas + [pregunta_hecha])[-3:]
        else:
            pregunta_hecha, respuesta_usuario = None, None

    evaluacion = plan_readiness.evaluar_ruta(ruta, families)
    print("\nEnsamblando tu plan...\n")
    # Fase 3.1: numeros ya persistidos del proyecto (sesiones anteriores)
    # mas los que esta sesion detecto pero aun no se mergean hasta el
    # cierre -- el verificador de huerfanos del plan necesita ambos.
    proyecto_actual = db.obtener_proyecto(project_id) if project_id else None
    numeros_para_plan = dict((proyecto_actual or {}).get("numeros_proyecto") or {})
    numeros_para_plan.update(numeros_detectados_sesion)
    resultado_plan = ensamblar_plan(ruta, graph, perfil_sesion, texto_original, families, evaluacion,
                                     session_id, es_seguimiento=es_seguimiento,
                                     estado_vivo_previo=estado_vivo_previo,
                                     prioridad_declarada=prioridad_declarada,
                                     registrar_evento=_registrar_evento,
                                     numeros_proyecto=numeros_para_plan)
    plan_md = resultado_plan["markdown"]
    print(plan_md)
    SALIDAS_DIR.mkdir(parents=True, exist_ok=True)
    fname = SALIDAS_DIR / f"plan_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    fname.write_text(plan_md, encoding="utf-8")
    print(f"\nPlan guardado en: {fname}")
    _ETIQUETA_MODO = {"conversado": "c", "silencioso": "s", "salto": "SALTO"}
    ruta_txt = " -> ".join(f"[{_ETIQUETA_MODO.get(m, m)}]{nid}" for nid, m in zip(ruta, modos))
    print(f"Ruta recorrida ({len(ruta)}): {ruta_txt}")

    return {
        "tipo": "plan", "ruta": ruta, "modos": modos, "perfil_sesion": perfil_sesion,
        "cosecha_ids": resultado_plan["cosecha_ids"],
        "evaluacion_cobertura": resultado_plan["evaluacion_cobertura"],
        "plan_md": plan_md, "plan_fname": fname, "fallback_events": fallback_events,
        "prioridad_declarada": prioridad_declarada,
        "numeros_detectados_sesion": numeros_detectados_sesion,
        "tipo_oferta_sesion": tipo_oferta_sesion, "unidad_venta_sesion": unidad_venta_sesion,
    }


def _merge_numeros_proyecto(project_id, numeros_detectados_sesion):
    """Motor v2.1: mergea lo detectado ESTA sesion dentro de
    projects.numeros_proyecto (solo pisa los campos que esta sesion SI
    detecto; el resto del historial numerico del proyecto queda intacto)."""
    if not numeros_detectados_sesion:
        return
    proyecto = db.obtener_proyecto(project_id)
    numeros = dict((proyecto or {}).get("numeros_proyecto") or {})
    numeros.update(numeros_detectados_sesion)
    db.actualizar_proyecto(project_id, numeros_proyecto=numeros)


def _merge_tipo_oferta(project_id, tipo_oferta_sesion, unidad_venta_sesion):
    """Motor v2.2: persiste tipo_oferta/unidad_venta si esta sesion detecto
    algo nuevo (nunca pisa con None lo que ya estaba guardado de una
    sesion anterior)."""
    if not tipo_oferta_sesion and not unidad_venta_sesion:
        return
    campos = {}
    if tipo_oferta_sesion:
        campos["tipo_oferta"] = tipo_oferta_sesion
    if unidad_venta_sesion:
        campos["unidad_venta"] = unidad_venta_sesion
    db.actualizar_proyecto(project_id, **campos)


def _persistir_resultado(project_id, db_session_id, resultado, graph, families, es_seguimiento=False):
    """Escribe en Supabase (o JSON local) el resultado de una sesion: nodos
    cubiertos, cierre de sesion (con desglose de costo por componente,
    Fase 2.7), plan, estado_vivo comprimido, y numeros_proyecto (Motor v2.1)."""
    if project_id is None or db_session_id is None:
        return  # --continuar de un scratch file anterior sin project_id: nada que persistir

    ruta = resultado["ruta"]
    modos = resultado["modos"]

    if resultado["tipo"] == "salio":
        eventos_sesion = resultado.get("fallback_events")
        calidad = evaluar_calidad_sesion(eventos_sesion, graph)
        db.cerrar_sesion(project_id, db_session_id, [], costo_acumulado_usd(), PRESUPUESTO_EXCEDIDO,
                         costo_por_componente_usd(), presupuesto_usd=PRESUPUESTO_SESION_USD,
                         decisiones=eventos_sesion, calidad=calidad)
        _merge_numeros_proyecto(project_id, resultado.get("numeros_detectados_sesion"))
        _merge_tipo_oferta(project_id, resultado.get("tipo_oferta_sesion"), resultado.get("unidad_venta_sesion"))
        return

    cosecha_ids = resultado["cosecha_ids"]
    evaluacion_cobertura = resultado["evaluacion_cobertura"]

    nodos_con_tipo = list(zip(ruta, modos)) + [(nid, "cosechado") for nid in cosecha_ids]
    db.registrar_nodos(project_id, db_session_id, nodos_con_tipo)

    _merge_numeros_proyecto(project_id, resultado.get("numeros_detectados_sesion"))
    _merge_tipo_oferta(project_id, resultado.get("tipo_oferta_sesion"), resultado.get("unidad_venta_sesion"))

    # estado_vivo se comprime ANTES de cerrar la sesion para que su costo
    # quede incluido en el desglose por componente que se persiste al cerrar
    proyecto = db.obtener_proyecto(project_id)
    estado_anterior = proyecto.get("estado_vivo") if proyecto else None
    conceptos_titulos = [graph[nid]["titulo_concepto"] for nid in ruta + cosecha_ids if nid in graph]
    estado_nuevo = comprimir_estado_vivo(estado_anterior, resultado["perfil_sesion"], conceptos_titulos)

    ruta_con_modos_json = [{"node_id": nid, "tipo": modo} for nid, modo in zip(ruta, modos)]
    eventos_sesion = resultado.get("fallback_events")
    calidad = evaluar_calidad_sesion(eventos_sesion, graph)
    db.cerrar_sesion(project_id, db_session_id, ruta_con_modos_json, costo_acumulado_usd(), PRESUPUESTO_EXCEDIDO,
                     costo_por_componente_usd(), presupuesto_usd=PRESUPUESTO_SESION_USD,
                     decisiones=eventos_sesion, calidad=calidad)

    etiqueta_db = "seguimiento" if es_seguimiento else ("completo" if evaluacion_cobertura["es_completa"] else "inicial")
    total_conceptos = len(ruta) + len(cosecha_ids)
    familias_presentes = sorted({families.get(nid, "general") for nid in ruta + cosecha_ids} - {"general"})
    db.guardar_plan(project_id, db_session_id, etiqueta_db, resultado["plan_md"], total_conceptos, familias_presentes)

    fase_final = graph[ruta[-1]].get("fase_proyecto", "ideacion") if ruta else "ideacion"
    campos = {"estado_vivo": estado_nuevo, "fase_actual": fase_final}
    titulo = _extraer_titulo(resultado["plan_md"])
    if titulo and (not proyecto or not proyecto.get("titulo")):
        campos["titulo"] = titulo
    db.actualizar_proyecto(project_id, **campos)


def _cierre_elegante(session_id, project_id):
    """Mensaje de salida limpio ante EOF/Ctrl+C: el estado ya quedo guardado
    por la ultima guardar_sesion(), asi que solo hace falta decir como
    retomar. Nunca se propaga un traceback al usuario."""
    print("\n\nSesion interrumpida. Tu progreso quedo guardado.")
    if session_id:
        print(f"Para retomarla en el mismo punto: python engine/prototipo_motor.py --continuar {session_id}")
    if project_id:
        print(f"O mas adelante, como seguimiento del proyecto: python engine/prototipo_motor.py --seguir {project_id}")


def modo_nuevo_proyecto(graph, families, entry_seeds, preguntas_cache, args):
    pregunta_hecha, respuesta_usuario = None, None
    session_id, project_id = None, None

    try:
        if args.continuar:
            sesion = cargar_sesion(args.continuar)
            session_id = args.continuar
            ruta = sesion["ruta"]
            modos = sesion.get("modos", ["conversado"] * len(ruta))
            visitados = set(ruta)
            actual_id = ruta[-1]
            perfil_sesion = sesion["perfil_sesion"]
            texto_original = sesion["entrada_original"]
            profundizar_ofrecido = sesion.get("profundizar_ofrecido", False)
            project_id = sesion.get("project_id")
            db_session_id = sesion.get("db_session_id")
            es_seguimiento = sesion.get("es_seguimiento", False)
            estado_vivo_previo = sesion.get("estado_vivo_previo")
            fallback_events = sesion.get("fallback_events", [])
            prioridad_declarada = sesion.get("prioridad_declarada")
            print(f"\nRetomando sesion {session_id} desde: {graph[actual_id]['titulo_concepto']}")
            pregunta_pendiente = sesion.get("pregunta_hecha")
            if pregunta_pendiente:
                # Hotfix v2.1.2: sin esto, la primera vuelta del bucle en
                # ejecutar_recorrido se hace con respuesta_usuario=None,
                # indistinguible de un arranque de sesion nueva — el
                # interprete queda libre de decidir cualquier cosa sin haber
                # visto lo que el usuario en verdad iba a responder,
                # incluyendo 'salir' sin que nadie lo pidiera.
                respuesta_usuario = leer_entrada("\n" + pregunta_pendiente + "\n> ")
                pregunta_hecha = pregunta_pendiente
        else:
            session_id = uuid.uuid4().hex[:8]
            texto_original = leer_entrada("\nCuéntame tu idea, o en qué punto estás con ella:\n> ")
            project_id = db.crear_proyecto(texto_original)
            db_session_id = db.crear_sesion(project_id, "inicial", texto_original)
            actual_id, perfil_sesion = clasificar_entrada(texto_original, entry_seeds, graph)
            visitados, ruta, modos = {actual_id}, [actual_id], ["conversado"]
            profundizar_ofrecido = False
            es_seguimiento, estado_vivo_previo = False, None
            fallback_events = []
            prioridad_declarada = None
            guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido,
                           project_id, db_session_id)
            _imprimir_nodo(1, MAX_DEPTH, graph[actual_id], "puerta de entrada", con_resumen=True)
            print(f"\n(proyecto: {project_id})")

        resultado = ejecutar_recorrido(
            graph, families, preguntas_cache, actual_id, visitados, ruta, modos,
            perfil_sesion, texto_original, session_id, project_id, db_session_id,
            profundizar_ofrecido, pregunta_hecha, respuesta_usuario,
            es_seguimiento=es_seguimiento, estado_vivo_previo=estado_vivo_previo,
            fallback_events=fallback_events, prioridad_declarada=prioridad_declarada,
        )
        _persistir_resultado(project_id, db_session_id, resultado, graph, families, es_seguimiento=es_seguimiento)
        if project_id:
            print(f"\nPara continuar mas adelante: python engine/prototipo_motor.py --seguir {project_id}")
        reportar_costo()
    except SesionInterrumpida:
        _cierre_elegante(session_id, project_id)


def modo_seguir(project_id, graph, families, entry_seeds, preguntas_cache):
    proyecto = db.obtener_proyecto(project_id)
    if proyecto is None:
        print(f"ERROR: no existe el proyecto {project_id}")
        sys.exit(1)

    session_id = None
    try:
        cubiertos = db.nodos_cubiertos(project_id)
        print(f"\nRetomando proyecto {project_id} (fase actual: {proyecto.get('fase_actual')}, "
              f"{len(cubiertos)} conceptos ya cubiertos).")
        mensaje_nuevo = leer_entrada("\nCuéntame qué ha pasado desde la última vez:\n> ")

        db_session_id = db.crear_sesion(project_id, "seguimiento", mensaje_nuevo)
        estado_vivo_previo = proyecto.get("estado_vivo")

        actual_id, perfil_sesion = seleccionar_puerta_avanzada(
            mensaje_nuevo, estado_vivo_previo, proyecto.get("fase_actual", "ideacion"),
            families, graph, cubiertos, entry_seeds,
        )
        visitados = set(cubiertos) | {actual_id}
        ruta, modos = [actual_id], ["conversado"]
        session_id = uuid.uuid4().hex[:8]
        guardar_sesion(session_id, ruta, modos, perfil_sesion, mensaje_nuevo, False, project_id, db_session_id,
                       es_seguimiento=True, estado_vivo_previo=estado_vivo_previo)
        _imprimir_nodo(1, MAX_DEPTH, graph[actual_id], "puerta de seguimiento", con_resumen=True)

        resultado = ejecutar_recorrido(
            graph, families, preguntas_cache, actual_id, visitados, ruta, modos,
            perfil_sesion, mensaje_nuevo, session_id, project_id, db_session_id,
            profundizar_ofrecido=False, es_seguimiento=True, estado_vivo_previo=estado_vivo_previo,
        )
        _persistir_resultado(project_id, db_session_id, resultado, graph, families, es_seguimiento=True)
        reportar_costo()
    except SesionInterrumpida:
        _cierre_elegante(session_id, project_id)


def modo_gratis(graph, entry_seeds):
    print("\n--- Modo gratuito: organizador de tu idea (sin entrevista) ---")
    try:
        texto_original = leer_entrada("\nCuéntame tu idea, o en qué punto estás con ella:\n> ")
    except SesionInterrumpida:
        print("\n\nHasta pronto.")
        return
    project_id = db.crear_proyecto(texto_original)
    db_session_id = db.crear_sesion(project_id, "gratuito", texto_original)

    markdown, data = organizador_gratuito(texto_original, entry_seeds, graph)
    if markdown is None:
        print(data)
        reportar_costo()
        return

    print("\n" + markdown)
    SALIDAS_DIR.mkdir(parents=True, exist_ok=True)
    fname = SALIDAS_DIR / f"plan_gratis_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    fname.write_text(markdown, encoding="utf-8")
    print(f"\nGuardado en: {fname}")

    db.guardar_plan(project_id, db_session_id, "organizador", markdown, 0, [])
    db.cerrar_sesion(project_id, db_session_id, [], costo_acumulado_usd(), PRESUPUESTO_EXCEDIDO,
                     costo_por_componente_usd(), presupuesto_usd=PRESUPUESTO_SESION_USD)
    if isinstance(data, dict) and data.get("etapa_detectada") in db.FASES:
        db.actualizar_proyecto(project_id, fase_actual=data["etapa_detectada"])

    print(f"\nProyecto: {project_id}")
    print(f"Para continuar mas adelante: python engine/prototipo_motor.py --seguir {project_id}")
    reportar_costo()


# ---------------------------------------------------------------------------
# Motor v2.1: Reporte de Sostenibilidad (--reporte PROJECT_ID)
# ---------------------------------------------------------------------------

# Motor v2.2: la mini-entrevista se parametriza por tipo_oferta (ver
# calculadora.py) porque "materiales por pieza" no tiene sentido para una
# app SaaS, y "horas por unidad" no aplica cuando no se fabrica nada.
# 'producto_fisico' y el default (tipo_oferta None, proyectos anteriores a
# esta version) usan el mismo set de 6 campos que Motor v2.1 -- retrocompatible.
CAMPOS_ESENCIALES_POR_TIPO = {
    "producto_fisico": ["costo_materiales_unidad", "horas_por_unidad", "valor_hora",
                         "precio_tentativo", "capacidad_semanal", "costos_fijos_mensuales"],
    "servicio": ["costo_materiales_unidad", "horas_por_unidad", "valor_hora",
                 "precio_tentativo", "capacidad_semanal", "costos_fijos_mensuales"],
    "digital": ["costos_fijos_mensuales", "costo_materiales_unidad", "precio_tentativo", "unidades_vendidas"],
}
MAX_PREGUNTAS_REPORTE = 6
REPORTE_DISCLAIMER = (
    "\n\n---\n_Estimaciones basadas en las cifras que tú diste; no sustituyen "
    "contabilidad formal ni asesoría fiscal, que varían según tu país._"
)
PREGUNTA_TIPO_OFERTA = "¿Qué vendes exactamente y cómo se cobra?"

# Guardian GIGO (Motor v2.2): frases deterministicas que indican que la
# mini-entrevista actual (el "molde" de preguntas del tipo_oferta activo)
# no encaja con el negocio del usuario. Dos apariciones abortan el molde
# y disparan una reclasificacion en vez de seguir insistiendo con
# preguntas que no aplican.
FRASES_NO_APLICA_MOLDE = (
    "no funciona asi", "no funciona así", "no es por pieza", "no es por unidad",
    "no vendo por unidades", "no aplica", "no se cobra asi", "no se cobra así",
    "es una suscripcion", "es una suscripción", "es digital", "no tengo piezas",
    "no produzco piezas", "no es un producto fisico", "no es un producto físico",
    "no fabrico",
)


def _detectar_no_aplica(texto):
    """Deterministico (sin LLM): True si la respuesta indica que la
    pregunta actual no encaja con el tipo de oferta del usuario."""
    t = (texto or "").strip().lower()
    return any(f in t for f in FRASES_NO_APLICA_MOLDE)


def _preguntas_por_tipo(tipo_oferta, unidad_venta):
    """Motor v2.2: tres plantillas parametrizadas por unidad_venta (la
    palabra literal del usuario: pieza, cliente, pack, suscripcion...).
    'servicio' y 'digital' tienen preguntas y (en el caso de digital)
    campos distintos a 'producto_fisico' -- ver CAMPOS_ESENCIALES_POR_TIPO."""
    u = unidad_venta or "unidad"
    if tipo_oferta == "servicio":
        return {
            "costo_materiales_unidad": f"¿Cuánto te cuesta directamente cada {u} (insumos, materiales que uses, etc.)? "
                                        "Un número aproximado sirve; si no tienes, responde 0.",
            "horas_por_unidad": f"¿Cuántas horas de trabajo te toma cada {u}?",
            "valor_hora": "¿En cuánto valoras tu hora de trabajo (lo que sientes que deberías ganar por hora)?",
            "precio_tentativo": f"¿A qué precio cobras (o cobrarías) cada {u}?",
            "capacidad_semanal": f"¿Cuántas veces de {u} puedes atender en una semana normal?",
            "costos_fijos_mensuales": "¿Tienes costos fijos mensuales (renta, herramientas, etc.)? Si sí, ¿cuánto suman al mes?",
        }
    if tipo_oferta == "digital":
        return {
            "costos_fijos_mensuales": "¿Cuánto gastas al mes en costos fijos de infraestructura (hosting, APIs, herramientas, suscripciones)?",
            "costo_materiales_unidad": f"¿Tienes algún costo variable por cada {u} (por ejemplo, costo de API por uso)? "
                                        "Si es prácticamente cero, responde 0.",
            "precio_tentativo": f"¿A qué precio o ingreso promedio vendes (o venderías) cada {u}?",
            "unidades_vendidas": f"¿Cuántas de {u} tienes hoy, o cuál sería una meta mensual realista?",
        }
    # producto_fisico y default (tipo_oferta None: proyectos pre-v2.2)
    return {
        "costo_materiales_unidad": f"¿Cuánto gastas en materiales por {u}, más o menos? Un número aproximado sirve.",
        "horas_por_unidad": f"¿Cuántas horas de trabajo te toma cada {u}, de principio a fin?",
        "valor_hora": "¿En cuánto valoras tu hora de trabajo (lo que sientes que deberías ganar por hora)?",
        "precio_tentativo": f"¿A qué precio venderías (o vendes) cada {u}?",
        "capacidad_semanal": f"¿Cuántas de {u} puedes producir en una semana normal?",
        "costos_fijos_mensuales": "¿Tienes costos fijos mensuales (renta, herramientas, etc.)? Si sí, ¿cuánto suman al mes?",
    }


def _unidad_declarada_campo(campo, tipo_oferta, unidad_venta):
    """Motor v2.2, guardian GIGO (a): cada campo capturado en la
    mini-entrevista guarda la unidad que la PREGUNTA misma establecio —
    deterministico, no depende de que el usuario la repita. Antes, todo
    campo capturado por la mini-entrevista quedaba con unidad=None (el
    campo existia en el esquema desde Motor v2.1 pero nunca se llenaba),
    asi que no habia forma de detectar una mezcla de unidades mas
    adelante."""
    u = unidad_venta or "unidad"
    if campo == "costos_fijos_mensuales":
        return "por mes"
    if campo == "valor_hora":
        return "por hora"
    if campo == "unidades_vendidas":
        return f"{u}/mes" if tipo_oferta == "digital" else u
    return f"por {u}"


SYSTEM_CLASIFICAR_OFERTA = (
    "Clasificas que vende un proyecto a partir de una frase libre del "
    "usuario. Responde SOLO un JSON de una linea: {\"tipo_oferta\": "
    "\"producto_fisico\"|\"servicio\"|\"digital\"|\"mixto\", "
    "\"unidad_venta\": str}. 'producto_fisico' = se fabrica o entrega algo "
    "material. 'servicio' = se cobra tiempo o trabajo, no un objeto. "
    "'digital' = app, software, contenido, suscripcion digital — costos "
    "marginales cercanos a cero. 'mixto' solo si combina claramente mas de "
    "uno. 'unidad_venta' es la palabra que el usuario usaria para su "
    "unidad de venta (pieza, cliente, pack, sesion, usuario, "
    "suscripcion...); si no queda clara, usa 'unidad'."
)


def _extraer_numero(texto):
    """Extractor deterministico (SIN LLM) de un numero en una respuesta en
    lenguaje natural: '$8', '8 dolares', '8.5', 'unos 8'. Devuelve None si
    el usuario no dio un numero reconocible o dijo que no sabe. Es
    deliberadamente simple (mini-entrevista, no un parser de NLU): trata
    las comas como separador de miles, no decimal."""
    t = texto.strip().lower()
    if not t or any(p in t for p in ("no se", "no sé", "no lo se", "no lo sé", "ni idea", "no tengo idea", "no idea")):
        return None
    m = re.search(r"\$?\s*(\d[\d,]*\.?\d*)", t)
    if not m:
        return None
    try:
        return float(m.group(1).replace(",", ""))
    except ValueError:
        return None


def _clasificar_oferta(texto):
    """Motor v2.2: reclasifica tipo_oferta/unidad_venta a partir de una
    frase libre. Se usa (a) cuando el proyecto todavia no tiene
    tipo_oferta guardado al abrir --reporte, y (b) cuando el guardian GIGO
    detecta que el molde de preguntas activo no encaja y hay que
    cambiarlo. Llamada barata a Haiku (clasificacion, no el interprete
    completo); si falla o no hay API_KEY, devuelve (None, None) y el
    llamador sigue con el tipo por defecto (producto_fisico)."""
    if not API_KEY:
        return None, None
    try:
        raw = llamar_claude(SYSTEM_CLASIFICAR_OFERTA, texto, MODEL_HAIKU, max_tokens=150, componente="turnos")
        data = _parsear_json(raw)
        tipo = data.get("tipo_oferta")
        unidad = data.get("unidad_venta")
        tipo = tipo if tipo in TIPOS_OFERTA_VALIDOS else None
        unidad = str(unidad).strip() if unidad else None
        return tipo, unidad
    except Exception:
        return None, None


def _reporte_gigo_inconsistente(motivo, numeros):
    """Guardian GIGO (Motor v2.2): cuando detectar_inconsistencia_gigo
    marca los numeros como probablemente mal capturados, el reporte NO
    narra ninguna conclusion financiera (ni siquiera via LLM — esta
    funcion es 100% deterministica a proposito, para no arriesgar que el
    narrador intente ser 'creativo' con datos que ya sabemos que estan
    rotos). Muestra los numeros crudos y pide la correccion puntual.
    Caso real que motiva esto: un reporte narro con confianza 'no existe
    punto de equilibrio posible' (margen -2976.9%) para un modelo cuyo
    equilibrio real, con las unidades corregidas, es de 16 packs/mes."""
    partes = [
        "## Tus números hoy", "",
        "Antes de calcular nada, encontré algo que no cuadra en estos números:", "",
        f"> {motivo}", "",
        "No voy a calcular margen ni punto de equilibrio con estos datos: el resultado "
        "sería una cifra que suena precisa pero está mal, y eso es peor que no tener el "
        "cálculo. Prefiero decírtelo con honestidad.", "",
        "## Los números que diste", "",
    ]
    for campo, entry in numeros.items():
        if entry.get("valor") is not None:
            partes.append(f"- {campo}: {entry['valor']}")
    partes += [
        "", "## Los números que te faltan (y cómo conseguirlos)", "",
        "Revisa si alguno de los números de arriba está en una unidad distinta a la que "
        "esperaba el reporte (por ejemplo, un gasto mensual anotado como costo por unidad, "
        "o un plazo en meses anotado como horas), corrígelo, y vuelve a correr "
        "`--reporte` con la cifra corregida.",
    ]
    return "\n".join(partes)


def _reporte_offline(resultados):
    """Respaldo sin IA (sin API_KEY, o si el presupuesto del reporte ya se
    agoto): los numeros crudos del modulo, sin narracion."""
    partes = ["## Tus números hoy", ""]
    costo, margen = resultados["costo_unitario"], resultados["margen"]
    equilibrio, capacidad = resultados["punto_equilibrio"], resultados["capacidad"]
    if costo["valor"] is not None:
        partes.append(f"- Costo por unidad: {costo['valor']}")
    if margen["valor"] is not None:
        partes.append(f"- Margen por unidad: {margen['valor']} ({margen['porcentaje']}%)")
    if equilibrio["valor"] is not None:
        partes.append(f"- Punto de equilibrio: {equilibrio['valor']} unidades/mes")
    if capacidad["ingreso"] is not None:
        partes.append(f"- Techo de ingreso mensual: {capacidad['ingreso']} ({capacidad['unidades_mes']} unidades/mes)")
    faltantes = sorted({f for r in resultados.values() for f in r.get("insumos_faltantes", [])})
    if faltantes:
        partes += ["", "## Los números que te faltan", ""]
        partes += [f"- {f}" for f in faltantes]
    return "\n".join(partes)


def _narrar_reporte(resultados, numeros, tipo_oferta=None):
    if not API_KEY:
        return _reporte_offline(resultados) + REPORTE_DISCLAIMER
    payload = {
        "resultados": resultados,
        "numeros_proyecto_declarados": {c: v.get("valor") for c, v in numeros.items()},
        "tipo_oferta": tipo_oferta,
    }
    try:
        cuerpo = llamar_claude(SYSTEM_REPORTE, json.dumps(payload, ensure_ascii=False), MODEL,
                               max_tokens=1800, componente="reporte")
    except Exception as e:
        print(f"  (fallo la narracion con IA, muestro los numeros crudos: {e})")
        cuerpo = _reporte_offline(resultados)
    return cuerpo.strip() + REPORTE_DISCLAIMER


def modo_reporte(project_id, graph, families):
    """Motor v2.1/v2.2: --reporte PROJECT_ID. (a) Inventario de
    numeros_proyecto y tipo_oferta, (b) mini-entrevista determinista
    parametrizada por tipo_oferta (fisico/servicio/digital), con guardian
    GIGO que aborta y reclasifica si 2+ respuestas indican que el molde no
    encaja, (c) calculadora.py calcula todo lo posible (o el guardian GIGO
    numerico rechaza narrar si el margen es absurdo), (d) UNA llamada
    Sonnet narra los resultados ya calculados (nunca genera cifras
    nuevas), (e) se guarda como plan etiquetado 'reporte_numeros'.
    Presupuesto duro propio: PRESUPUESTO_REPORTE_USD."""
    global PRESUPUESTO_SESION_USD
    proyecto = db.obtener_proyecto(project_id)
    if proyecto is None:
        print(f"ERROR: no existe el proyecto {project_id}")
        sys.exit(1)

    # Techo de costo propio del reporte, independiente del presupuesto
    # general de sesion: --reporte es una corrida corta y aislada, asi que
    # basta con apretar el mismo mecanismo de llamar_claude a un tope menor.
    PRESUPUESTO_SESION_USD = min(PRESUPUESTO_SESION_USD, PRESUPUESTO_REPORTE_USD)

    numeros = dict(proyecto.get("numeros_proyecto") or {})
    tipo_oferta = proyecto.get("tipo_oferta")
    unidad_venta = proyecto.get("unidad_venta")
    print(f"\nGenerando tu Reporte de Sostenibilidad (proyecto: {project_id})...")

    try:
        if not tipo_oferta:
            respuesta_tipo = leer_entrada("\n" + PREGUNTA_TIPO_OFERTA + "\n> ")
            tipo_detectado, unidad_detectada = _clasificar_oferta(respuesta_tipo)
            tipo_oferta = tipo_detectado
            unidad_venta = unidad_detectada or unidad_venta
            if tipo_oferta:
                db.actualizar_proyecto(project_id, tipo_oferta=tipo_oferta, unidad_venta=unidad_venta)

        campos_esenciales = CAMPOS_ESENCIALES_POR_TIPO.get(tipo_oferta, CAMPOS_ESENCIALES_POR_TIPO["producto_fisico"])
        preguntas = _preguntas_por_tipo(tipo_oferta, unidad_venta)
        faltantes_esenciales = [c for c in campos_esenciales if c not in numeros][:MAX_PREGUNTAS_REPORTE]
        no_aplica_count = 0
        molde_cambiado = False

        if faltantes_esenciales:
            print("\nMe faltan algunos numeros para completar tu reporte. "
                  "Si no sabes alguno, escribe 'no se' y seguimos con el resto.")
        idx = 0
        while idx < len(faltantes_esenciales):
            campo = faltantes_esenciales[idx]
            respuesta = leer_entrada("\n" + preguntas[campo] + "\n> ")
            if _detectar_no_aplica(respuesta):
                no_aplica_count += 1
                if no_aplica_count >= 2 and not molde_cambiado:
                    print("\nParece que estas preguntas no encajan con lo que vendes. "
                          "Te pregunto distinto.")
                    aclaracion = leer_entrada("\n" + PREGUNTA_TIPO_OFERTA + "\n> ")
                    nuevo_tipo, nueva_unidad = _clasificar_oferta(aclaracion)
                    molde_cambiado = True
                    if nuevo_tipo and nuevo_tipo != tipo_oferta:
                        tipo_oferta = nuevo_tipo
                        unidad_venta = nueva_unidad or unidad_venta
                        db.actualizar_proyecto(project_id, tipo_oferta=tipo_oferta, unidad_venta=unidad_venta)
                        campos_esenciales = CAMPOS_ESENCIALES_POR_TIPO.get(
                            tipo_oferta, CAMPOS_ESENCIALES_POR_TIPO["producto_fisico"])
                        preguntas = _preguntas_por_tipo(tipo_oferta, unidad_venta)
                        faltantes_esenciales = [c for c in campos_esenciales if c not in numeros][:MAX_PREGUNTAS_REPORTE]
                        idx = 0
                        continue
                idx += 1
                continue
            valor = _extraer_numero(respuesta)
            if valor is not None:
                numeros[campo] = {
                    "valor": valor, "unidad": _unidad_declarada_campo(campo, tipo_oferta, unidad_venta),
                    "texto_original": respuesta, "session_id": None, "updated_at": datetime.now().isoformat(),
                }
            idx += 1
    except SesionInterrumpida:
        db.actualizar_proyecto(project_id, numeros_proyecto=numeros)
        print("\n\nSesion interrumpida. Lo que ya contestaste quedo guardado.")
        print(f"Para generar el reporte completo: python engine/prototipo_motor.py --reporte {project_id}")
        return

    db.actualizar_proyecto(project_id, numeros_proyecto=numeros)

    eventos_reporte = []

    def _registrar_evento_reporte(evento):
        eventos_reporte.append(evento)

    gigo = calculadora.detectar_inconsistencia_gigo(numeros, tipo_oferta=tipo_oferta)
    if gigo["inconsistente"]:
        contenido = _reporte_gigo_inconsistente(gigo["motivo"], numeros) + REPORTE_DISCLAIMER
        numeros_permitidos = verificador_huerfanos.cerradura_aritmetica(
            verificador_huerfanos.numeros_declarados(numeros))
        # Fase 3.1 (caja de vidrio): antes de esto, un aborto del guardian
        # GIGO no dejaba ningun rastro persistido -- pnpm salud/health
        # necesita poder medir la tasa de abortos.
        _registrar_evento_reporte({"tipo": "gigo_abortado", "motivo": gigo["motivo"]})
    else:
        resultados = calculadora.calcular_reporte(numeros, tipo_oferta=tipo_oferta)
        contenido = _narrar_reporte(resultados, numeros, tipo_oferta=tipo_oferta)
        numeros_permitidos = verificador_huerfanos.cerradura_aritmetica(
            verificador_huerfanos.numeros_de_calculadora(resultados)
            | verificador_huerfanos.numeros_declarados(numeros)
        )
    # Fase 3.1 (caja de vidrio): automatiza la vara de auditoria "ningun
    # numero huerfano" -- senal de triage, no bloquea el reporte ya
    # generado (a diferencia del guardian GIGO, que si aborta antes).
    verificador_huerfanos.verificar_numeros_huerfanos(
        contenido, numeros_permitidos, registrar_evento=_registrar_evento_reporte)

    SALIDAS_DIR.mkdir(parents=True, exist_ok=True)
    fname = SALIDAS_DIR / f"reporte_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    fname.write_text(contenido, encoding="utf-8")
    print("\n" + contenido)
    print(f"\nReporte guardado en: {fname}")

    db_session_id = db.crear_sesion(project_id, "reporte", "generacion de reporte de sostenibilidad")
    db.guardar_plan(project_id, db_session_id, "reporte_numeros", contenido, 0, [])
    db.cerrar_sesion(project_id, db_session_id, [], costo_acumulado_usd(), PRESUPUESTO_EXCEDIDO,
                     costo_por_componente_usd(), presupuesto_usd=PRESUPUESTO_SESION_USD,
                     decisiones=eventos_reporte)
    reportar_costo()


def main():
    args = parse_args()
    if args.offline:
        db.forzar_offline(True)

    graph = cargar_grafo()
    entry_seeds = cargar_entry_seeds()
    preguntas_cache = cargar_preguntas_cache()
    families = plan_readiness.cargar_families(graph)

    print("=" * 60)
    print("  MY IDEA - prototipo del motor de ruteo (travesia silenciosa)")
    print(f"  Grafo: {len(graph)} conceptos | modo: {'IA' if API_KEY else 'offline'} | "
          f"preguntas cacheadas: {len(preguntas_cache)} | persistencia: "
          f"{'Supabase' if db.disponible() else 'JSON local'}")
    print("=" * 60)

    if args.gratis:
        modo_gratis(graph, entry_seeds)
        return
    if args.reporte:
        modo_reporte(args.reporte, graph, families)
        return
    if args.seguir:
        modo_seguir(args.seguir, graph, families, entry_seeds, preguntas_cache)
        return
    modo_nuevo_proyecto(graph, families, entry_seeds, preguntas_cache, args)


if __name__ == "__main__":
    main()
