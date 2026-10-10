# -*- coding: utf-8 -*-
"""'Lo que este plan aun no cubre: validar con clientes reales' solo cuando las ETAPAS de verdad no validan con
clientes (decision del fundador, 9 oct 2026), en el motor igual que en la web (web/lib/engine/coberturaClientes.test.ts).
Segunda medicion A/B: la frase fija salio en 11 de 14 planes y el arbitro la sostuvo como contrario en planes cuyas
etapas mandan hablar con clientes, entregar la primera version a los primeros usuarios o probar el precio con
compradores. Casos reales: extractos de docs/corrida_final/2026-10-08/medicion_ab2/A/. Sin API."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import prototipo_motor as pm

FRASE = pm._TEXTO_FAMILIA_FALTANTE["accion_clientes"]
ECON = pm._TEXTO_FAMILIA_FALTANTE["viabilidad_economica"]

SIN_ACCION = {
    "es_completa": False,
    "tiene_accion_clientes": False,
    "tiene_viabilidad_economica": True,
    "familias_faltantes": [FRASE],
}

# Plan ee6de956 (nucleo, app de gastos): sostenido como contrario por el arbitro.
EE6DE956 = "\n".join([
    "# Tu app de registro de gastos: descubre si alguien pagará cada mes y se quedará",
    "",
    "Tienes una app de suscripción mensual para llevar el registro de gastos personales y todavía ningún cliente ha pagado.",
    "",
    "## Etapa 1: Pon por escrito lo que das por cierto sin haberlo comprobado",
    "",
    "1. Escribe las suposiciones que sostienen tu idea.",
    "",
    "## Etapa 2: Sal a hablar con personas que podrían usarla",
    "",
    "1. Toma las suposiciones más riesgosas de la etapa 1 y conviértelas en preguntas para clientes potenciales.",
    "2. Habla con personas que llevan o intentan llevar el control de sus gastos personales.",
    "",
    "## Etapa 4: Lanza a un grupo pequeño y mide lo que hacen, no lo que dicen",
    "",
    "1. Lanza tu primera versión, funcional o simulada, a unos pocos usuarios dispuestos a probar cosas nuevas.",
])

# Plan 9909f451 (nucleo): sostenido como contrario por el arbitro.
P9909F451 = "\n".join([
    "# Plan para validar tu app de suscripción de gastos personales",
    "",
    "Todavía no has hablado con usuarios reales, así que este plan empieza por comprobar que el problema existe.",
    "",
    "## Etapa 1: Descubre cómo registra gastos la gente hoy",
    "",
    "2. Sal a hablar con personas que llevan o intentan llevar sus gastos, de forma repetida durante varias semanas, y pregúntales qué hacen hoy y qué otras soluciones usan.",
    "",
    "## Etapa 4: Prueba una versión mínima con tus primeros usuarios",
    "",
    "3. Entrégala a tus primeros usuarios, los del grupo visionario de la etapa 2, no a un público masivo.",
])

# Plan aad2749d (nucleo, macetas, ya vende): sostenido como contrario por el arbitro.
AAD2749D = "\n".join([
    "# Tu precio de 250 con costo real de 130: de comprobar el margen a decidir tu rumbo",
    "",
    "## Etapa 1: Cierra tu costo real y tu ganancia por maceta",
    "",
    "1. Suma lo que gastas en materiales por pieza.",
    "",
    "## Etapa 4: Confirma que el precio de 250 se sostiene y mide el canal de la tienda",
    "",
    "1. Escribe de antemano qué resultado te bastaría para quedarte con el precio de 250 (por ejemplo, cuántos compradores de un grupo pequeño lo aceptan).",
    "5. Mira si la feria local de agosto te sirve para probar el precio con compradores nuevos, cambiando solo eso.",
])

# Plan 85248377 (Salud y Seguridad): habla con sus EMPLEADOS, no con clientes. La frase es verdad y se queda.
P85248377 = "\n".join([
    "# Protege tu salud y la de tu taller de macetas sin frenar la producción",
    "",
    "## Etapa 3: Controla cada peligro empezando por lo más efectivo",
    "",
    "1. Para cada peligro prioritario, pregúntate en este orden: ¿puedo eliminarlo?, ¿puedo cambiar el material?",
    "",
    "## Etapa 4: Habla con tus dos empleados sobre la protección",
    "",
    "3. Pregúntales qué les incomoda del equipo de protección y qué ajuste les ayudaría a trabajar con él sin perder ritmo.",
])

# Solo la introduccion habla de clientes; ninguna etapa los toca: la frase se queda.
SOLO_INTRO = "\n".join([
    "# Ordena tu taller",
    "",
    "Tus clientes te piden más rapidez y quieres hablar con tus compradores más adelante.",
    "",
    "## Etapa 1: Ordena tus herramientas",
    "",
    "1. Pon cada herramienta en su sitio.",
])


def faltantes_con(cuerpo, evaluacion=SIN_ACCION):
    return pm._cobertura_contra_etapas(dict(evaluacion), {"familias_tratadas": [], "etapas": {}}, set(), {}, cuerpo)


for nombre, cuerpo in (("ee6de956", EE6DE956), ("9909f451", P9909F451), ("aad2749d", AAD2749D)):
    assert pm._valida_con_clientes_en_etapas(cuerpo), f"{nombre}: las etapas validan con clientes"
    assert FRASE not in faltantes_con(cuerpo)["familias_faltantes"], f"{nombre}: la frase no debe salir"

assert not pm._valida_con_clientes_en_etapas(P85248377), "85248377: los empleados no son clientes"
assert FRASE in faltantes_con(P85248377)["familias_faltantes"], "85248377: la frase se queda"

assert not pm._valida_con_clientes_en_etapas(SOLO_INTRO), "la introduccion no cuenta"
assert FRASE in faltantes_con(SOLO_INTRO)["familias_faltantes"], "solo intro: la frase se queda"

r = faltantes_con(EE6DE956, {
    "es_completa": False, "tiene_accion_clientes": False, "tiene_viabilidad_economica": False,
    "familias_faltantes": [FRASE, ECON],
})
assert r["familias_faltantes"] == [ECON], r
assert r["tiene_accion_clientes"] is True and r["es_completa"] is False, r

# Paridad con la web: cobertura por nodos de las etapas (solo ids del material entregado).
r = pm._cobertura_contra_etapas(
    dict(SIN_ACCION), {"familias_tratadas": [], "etapas": {"1": ["nodo_clientes", "nodo_inventado"]}},
    {"nodo_clientes"}, {"nodo_clientes": "accion_clientes", "nodo_inventado": "accion_clientes"}, "# Plan")
assert FRASE not in r["familias_faltantes"], r
r = pm._cobertura_contra_etapas(
    dict(SIN_ACCION), {"familias_tratadas": [], "etapas": {"1": ["nodo_inventado"]}},
    set(), {"nodo_inventado": "accion_clientes"}, "# Plan")
assert FRASE in r["familias_faltantes"], "un id que no vino en el material no cubre nada"

print("TODO OK: la frase de validar con clientes solo sale si las etapas de verdad no validan con clientes (motor).")
