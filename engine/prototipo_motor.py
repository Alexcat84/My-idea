# -*- coding: utf-8 -*-
"""
prototipo_motor.py - Motor de ruteo (post motor-v1.0: Fase 2.6 preguntas
adaptadas por turno, Fase 2.7 escucha activa y caching incremental).

Ver examples/README.md para la prueba de cierre de motor-v1.0 (dos actos,
sin tracebacks) y las pruebas de Fase 2.6/2.7 (macetas de calcita); ver
mas abajo para el detalle de cada fase.

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
      default 0.30): si el costo acumulado alcanza el tope, las llamadas
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

# En consolas de Windows, stdout suele quedar en cp1252 (o el codepage local),
# que no puede representar caracteres como flechas (->) o comillas tipograficas
# presentes en el contenido de algunos nodos. Sin esto, print() lanza
# UnicodeEncodeError y el programa se cae a mitad de un recorrido.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

GRAPH_PATH = BASE / "dataset" / "metadata" / "master_graph.json"
QUIZ_PATH = BASE / "engine" / "cuestionario_raiz.json"
ENTRY_SEEDS_PATH = BASE / "dataset" / "metadata" / "entry_seeds.json"
PREGUNTAS_CACHE_PATH = BASE / "engine" / "preguntas_cache.json"
SESSIONS_DIR = BASE / "engine" / "sessions"

MAX_DEPTH = 15
MAX_OPCIONES = 6
MAX_SUCESORES_NIVEL2 = 4
MAX_SALTOS_SILENCIOSOS_POR_LLAMADA = 3
MAX_REPREGUNTAS_POR_PUNTO = 1

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

PRESUPUESTO_SESION_USD = float(os.environ.get("PRESUPUESTO_SESION_USD", "0.30"))
PRESUPUESTO_EXCEDIDO = False

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
    "adaptadas Y repreguntas por igual, puede venir vacia al inicio), y "
    "prioridad_declarada_actual: {\"texto\": str, \"conteo\": int} o null — "
    "lo que el usuario mismo ha repetido como su bloqueo o urgencia "
    "principal, y cuantas veces lo ha reafirmado hasta ahora.\n\n"
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
    "contenido de fondo varie; dos plantillas especialmente vigiladas por "
    "reincidentes: '¿que te preocupa/duda mas: A, o B?' y 'Entiendo que X, "
    "pero antes de Y, ¿Z?'. Si tu primer instinto de pregunta_adaptada o "
    "repregunta calza en una de esas dos plantillas Y alguna de las 3 "
    "ultimas ya la uso, cambia de plantilla por completo (no solo de "
    "palabras) — por ejemplo, en vez de '¿que te preocupa mas...?' prueba "
    "una pregunta directa de hechos ('¿ya le mostraste esto a alguien "
    "fuera de tu circulo?'), y en vez de 'Entiendo que X, pero antes de "
    "Y...' prueba reconocer y seguir sin el 'pero' (ver la regla de "
    "PRIORIDAD DECLARADA arriba). Si de verdad no hay nada nuevo que "
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
    "los sucesores inmediatos y repreguntas_disponibles=true, usa "
    "accion='repreguntar' con UNA pregunta de seguimiento especifica y "
    "breve que tampoco repita la estructura de las ultimas_preguntas_hechas.\n"
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
    "- 'camino' es la cadena LITERAL completa, sin saltos: el primer id "
    "SIEMPRE debe ser uno de los sucesores de nivel 1 dados. Si el nodo que "
    "te interesa es de nivel 2 (aparece dentro de 'sucesores' de un nodo de "
    "nivel 1), DEBES incluir primero ese nodo de nivel 1 como paso previo en "
    "'camino', y el de nivel 2 despues, en ese orden. Nunca pongas un nodo "
    "de nivel 2 sin su padre de nivel 1 inmediatamente antes en el mismo "
    "camino. Cada id debe ser un sucesor real del nodo anterior en la "
    "cadena, nunca un id repetido ni inventado.\n"
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
    "\"prioridad_declarada\": null}.\n"
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
    "\"prioridad_declarada\": null}.\n"
    "Ejemplo 3 (generar_plan porque el usuario lo pidio explicitamente, "
    "aunque con otras palabras): el usuario responde 'creo que con esto ya "
    "tengo para armar algo, dame lo que tengas'. Respuesta: {\"accion\": "
    "\"generar_plan\", \"camino\": [], \"pregunta_necesaria\": false, "
    "\"pregunta_adaptada\": null, \"repregunta\": null, \"perfil_update\": "
    "null, \"prioridad_declarada\": null}.\n"
    "Ejemplo 4 (salir sin plan): el usuario responde 'mejor lo dejamos "
    "aqui, no quiero seguir con esto ahora'. Respuesta: {\"accion\": "
    "\"salir\", \"camino\": [], \"pregunta_necesaria\": false, "
    "\"pregunta_adaptada\": null, \"repregunta\": null, \"perfil_update\": "
    "null, \"prioridad_declarada\": null}.\n"
    "Ejemplo 5 (cadena de 3 nodos silenciosos, el maximo permitido, sin "
    "preguntar nada en esta llamada): el perfil_sesion ya es muy rico "
    "(varios turnos acumulados) y responde con claridad lo que preguntan "
    "los tres primeros sucesores en cadena de este punto del grafo, pero "
    "el contexto SI alcanzaria para seguir mas alla del tercero — aun asi "
    "te detienes en el tercero por el limite de 3 saltos por llamada. "
    "Respuesta: {\"accion\": \"avanzar\", \"camino\": [\"id_n1\", "
    "\"id_n2_hijo_de_n1\", \"id_n3_hijo_de_n2\"], \"pregunta_necesaria\": "
    "false, \"pregunta_adaptada\": null, \"repregunta\": null, "
    "\"perfil_update\": null, \"prioridad_declarada\": null}. La siguiente "
    "llamada al interprete continuara desde ese tercer nodo, sin que el "
    "usuario haya notado ninguna pausa.\n"
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
    "\"conteo\": 2}}. Nota que NO dice 'pero antes de eso' ni desvia hacia "
    "validacion de pago — reconoce la prioridad y avanza sobre ella "
    "directamente.\n\n"
    "Responde SOLO un JSON: {\"accion\": \"avanzar\"|\"repreguntar\"|"
    "\"generar_plan\"|\"salir\", \"camino\": [ids en orden], "
    "\"pregunta_necesaria\": bool, \"pregunta_adaptada\": str|null, "
    "\"repregunta\": str|null, \"perfil_update\": str|null, "
    "\"prioridad_declarada\": {\"texto\": str, \"conteo\": int}|null}."
)

SYSTEM_PROFUNDIZAR = (
    "Interpretas la respuesta de un usuario a la pregunta de si quiere su "
    "plan ahora mismo (aunque le falten algunas partes) o prefiere "
    "responder unas preguntas mas para tener un plan mas completo. "
    "Responde SOLO un JSON: {\"decision\": \"generar_ya\"|\"continuar\"}."
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
    "sobre extension (mas etapas o mas parrafos por etapa).\n\n"
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
    "parezca completo."
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
                    fallback_events=None, prioridad_declarada=None):
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
    traceback visible. Usar SIEMPRE esta funcion en vez de input() directo."""
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
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


def sucesores_nivel(nid, graph, visitados, limite=MAX_OPCIONES):
    return [c for c in graph[nid].get("nodos_siguientes", []) if c in graph and c not in visitados][:limite]


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

    ctx_completo = {
        "entrada_original": texto_original,
        "perfil_sesion": perfil_sesion,
        "nodo_actual": resumen_nodo(actual_id, graph, preguntas_cache),
        "sucesores_nivel1_y_nivel2": nivel1,
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

    def _validar_respuesta(raw):
        data = _parsear_json(raw)
        accion = data.get("accion")
        if accion not in ("avanzar", "repreguntar", "generar_plan", "salir"):
            raise ValueError(f"accion invalida: {accion}")
        if accion == "repreguntar" and not repreguntas_disponibles:
            raise ValueError("el modelo repregunto sin repreguntas disponibles")
        if accion == "avanzar":
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
        return _validar_respuesta(raw)
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
        return _validar_respuesta(raw2)
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
        return {"accion": "avanzar", "camino": [candidato], "pregunta_necesaria": True,
                "pregunta_adaptada": pregunta_fallback, "perfil_update": None,
                "prioridad_declarada": prioridad_declarada_actual}


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


def preguntar_profundizar(familias_faltantes):
    """Ofrece UNA vez la disyuntiva plan-inicial-ya vs. seguir profundizando."""
    faltan_txt = "; ".join(familias_faltantes)
    mensaje = (
        f"Puedo darte tu plan ahora mismo. Eso si: con algunas preguntas mas "
        f"incluiria {faltan_txt}. ¿Seguimos un poco o lo quieres ya?"
    )
    respuesta = leer_entrada("\n" + mensaje + "\n> ")
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
            if vecino in graph and vecino not in ruta_set:
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


def ensamblar_plan(ruta, graph, perfil_sesion, texto_original, families, evaluacion, session_id,
                    es_seguimiento=False, estado_vivo_previo=None, prioridad_declarada=None):
    """`evaluacion` (ruta-solo) decide QUE cosechar (familia faltante como
    prioridad). La etiqueta inicial/completo y la seccion "no cubre" se
    recalculan sobre ruta+cosecha, porque eso es lo que el plan realmente
    contiene: si la cosecha trajo la familia que la ruta no toco, el plan
    ya la cubre y no puede declarar lo contrario. Devuelve un dict con el
    markdown y los metadatos de cosecha/cobertura, para persistencia.
    Fase 2.7: prioridad_declarada (el bloqueo que el usuario repitio) se
    pasa a la cosecha (reserva cupos afines) y al redactor (bloqueo_declarado
    en el payload), para que el plan le de tratamiento explicito."""
    def a_material(nid):
        n = graph[nid]
        return {
            "concepto": n["titulo_concepto"],
            "pasos": n.get("pasos_accionables", []),
            "entregable": n.get("entregable_esperado", ""),
            "es_viabilidad_economica": families.get(nid) == "viabilidad_economica",
        }

    material_principal = [a_material(nid) for nid in ruta]
    cosecha_ids = cosechar_vecindario(ruta, graph, families, evaluacion, perfil_sesion, prioridad_declarada)
    material_de_apoyo = [a_material(nid) for nid in cosecha_ids]
    evaluacion_cobertura = plan_readiness.evaluar_ruta(ruta + cosecha_ids, families)

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
            cuerpo = llamar_claude(SYSTEM_PLAN, json.dumps(payload, ensure_ascii=False), MODEL,
                                   max_tokens=5000, componente="plan")
        except Exception as e:
            print(f"  (fallo el redactor con IA, ensamblo offline: {e})")
            cuerpo = _ensamblar_offline(material_principal, perfil_sesion, texto_original)
    else:
        cuerpo = _ensamblar_offline(material_principal, perfil_sesion, texto_original)

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

        if resultado["accion"] == "salir":
            print("\nHasta pronto.")
            return {"tipo": "salio", "ruta": ruta, "modos": modos, "perfil_sesion": perfil_sesion,
                    "fallback_events": fallback_events, "prioridad_declarada": prioridad_declarada}

        if resultado["accion"] == "repreguntar":
            repreguntas_usadas += 1
            pregunta_hecha = resultado["repregunta"]
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
                    print("\nPerfecto, sigamos un poco mas.")
                    pregunta_hecha, respuesta_usuario = None, None
                    repreguntas_usadas = 0
                    continue
            break

        # accion == "avanzar": camino de 1-3 nodos, algunos silenciosos + a lo sumo uno conversado al final
        camino = resultado["camino"]
        pregunta_necesaria = resultado["pregunta_necesaria"]
        for idx, nid in enumerate(camino):
            es_ultimo = idx == len(camino) - 1
            modo = "conversado" if (es_ultimo and pregunta_necesaria) else "silencioso"
            visitados.add(nid)
            ruta.append(nid)
            modos.append(modo)
            if modo == "silencioso":
                _imprimir_nodo(len(ruta), MAX_DEPTH, graph[nid], "silencioso", con_resumen=False)
        actual_id = camino[-1]
        repreguntas_usadas = 0
        guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido,
                       project_id, db_session_id, es_seguimiento, estado_vivo_previo, fallback_events,
                       prioridad_declarada)

        if pregunta_necesaria:
            n = graph[actual_id]
            _imprimir_nodo(len(ruta), MAX_DEPTH, n, "conversado", con_resumen=True)
            pregunta_hecha = resultado.get("pregunta_adaptada") or obtener_pregunta(actual_id, n, preguntas_cache)
            respuesta_usuario = leer_entrada("\n" + pregunta_hecha + "\n> ")
            ultimas_preguntas = (ultimas_preguntas + [pregunta_hecha])[-3:]
        else:
            pregunta_hecha, respuesta_usuario = None, None

    evaluacion = plan_readiness.evaluar_ruta(ruta, families)
    print("\nEnsamblando tu plan...\n")
    resultado_plan = ensamblar_plan(ruta, graph, perfil_sesion, texto_original, families, evaluacion,
                                     session_id, es_seguimiento=es_seguimiento,
                                     estado_vivo_previo=estado_vivo_previo,
                                     prioridad_declarada=prioridad_declarada)
    plan_md = resultado_plan["markdown"]
    print(plan_md)
    fname = BASE / f"plan_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    fname.write_text(plan_md, encoding="utf-8")
    print(f"\nPlan guardado en: {fname}")
    ruta_txt = " -> ".join(f"[{m[0]}]{nid}" for nid, m in zip(ruta, modos))
    print(f"Ruta recorrida ({len(ruta)}): {ruta_txt}")

    return {
        "tipo": "plan", "ruta": ruta, "modos": modos, "perfil_sesion": perfil_sesion,
        "cosecha_ids": resultado_plan["cosecha_ids"],
        "evaluacion_cobertura": resultado_plan["evaluacion_cobertura"],
        "plan_md": plan_md, "plan_fname": fname, "fallback_events": fallback_events,
        "prioridad_declarada": prioridad_declarada,
    }


def _persistir_resultado(project_id, db_session_id, resultado, graph, families, es_seguimiento=False):
    """Escribe en Supabase (o JSON local) el resultado de una sesion: nodos
    cubiertos, cierre de sesion (con desglose de costo por componente,
    Fase 2.7), plan, y el estado_vivo comprimido."""
    if project_id is None or db_session_id is None:
        return  # --continuar de un scratch file anterior sin project_id: nada que persistir

    ruta = resultado["ruta"]
    modos = resultado["modos"]

    if resultado["tipo"] == "salio":
        db.cerrar_sesion(project_id, db_session_id, [], costo_acumulado_usd(), PRESUPUESTO_EXCEDIDO,
                         costo_por_componente_usd())
        return

    cosecha_ids = resultado["cosecha_ids"]
    evaluacion_cobertura = resultado["evaluacion_cobertura"]

    nodos_con_tipo = list(zip(ruta, modos)) + [(nid, "cosechado") for nid in cosecha_ids]
    db.registrar_nodos(project_id, db_session_id, nodos_con_tipo)

    # estado_vivo se comprime ANTES de cerrar la sesion para que su costo
    # quede incluido en el desglose por componente que se persiste al cerrar
    proyecto = db.obtener_proyecto(project_id)
    estado_anterior = proyecto.get("estado_vivo") if proyecto else None
    conceptos_titulos = [graph[nid]["titulo_concepto"] for nid in ruta + cosecha_ids if nid in graph]
    estado_nuevo = comprimir_estado_vivo(estado_anterior, resultado["perfil_sesion"], conceptos_titulos)

    ruta_con_modos_json = [{"node_id": nid, "tipo": modo} for nid, modo in zip(ruta, modos)]
    db.cerrar_sesion(project_id, db_session_id, ruta_con_modos_json, costo_acumulado_usd(), PRESUPUESTO_EXCEDIDO,
                     costo_por_componente_usd())

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
    fname = BASE / f"plan_gratis_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    fname.write_text(markdown, encoding="utf-8")
    print(f"\nGuardado en: {fname}")

    db.guardar_plan(project_id, db_session_id, "organizador", markdown, 0, [])
    db.cerrar_sesion(project_id, db_session_id, [], costo_acumulado_usd(), PRESUPUESTO_EXCEDIDO,
                     costo_por_componente_usd())
    if isinstance(data, dict) and data.get("etapa_detectada") in db.FASES:
        db.actualizar_proyecto(project_id, fase_actual=data["etapa_detectada"])

    print(f"\nProyecto: {project_id}")
    print(f"Para continuar mas adelante: python engine/prototipo_motor.py --seguir {project_id}")
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
    if args.seguir:
        modo_seguir(args.seguir, graph, families, entry_seeds, preguntas_cache)
        return
    modo_nuevo_proyecto(graph, families, entry_seeds, preguntas_cache, args)


if __name__ == "__main__":
    main()
