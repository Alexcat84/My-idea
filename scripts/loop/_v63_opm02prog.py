# -*- coding: utf-8 -*-
"""_v63_opm02prog.py . EL CONTENIDO EDITORIAL DE LA FUSION DE MESA OP-M-02-PROG.

NO ES UN INSTRUMENTO: no mide, no escribe y no decide nada por si mismo. Es EL
TEXTO del reparto pieza a pieza, con su motivo citado y LAS PERDIDAS SELLADAS EN
CAMPO PROPIO. Lo importa scripts/loop/generar_plan_de_fusion_de_mesa.py, que es
quien pone LA ARITMETICA Y LAS GUARDAS y quien sella el plan.

EL SUPERVIVIENTE NO SE ELIGE AQUI: LO ELIGIO LA FICHA. La adjudicacion de
OP-M-02-PROG esta sellada en docs/plan/OPERACIONES.jsonl desde el 12 ago 2026 y
el generador cae en ROJO si este fichero nombra otro.

CADA PERDIDA LLEVA SUS CUATRO CLAVES (especie, que, donde, enrutada_a) y su
especie es UNA DE LAS TRES ESCRITAS.
"""

FUSION = {
    "titulo": (
        "EL PROGRAMA UNICO: ocho_fases_experiencia_cliente absorbe "
        "fases_de_retencion_de_clientes. Es la SEGUNDA fusion de mesa de la campana y la "
        "segunda operacion del puesto 1 del orden adjudicado en la vuelta 47. LAS DOS "
        "PRIORIDADES VIAJAN, que es lo unico que la ficha manda preservar"
    ),
    "superviviente": "ocho_fases_experiencia_cliente",
    "absorbidos": ["fases_de_retencion_de_clientes"],
    "motivo": (
        "EL SUPERVIVIENTE LO FIJA LA FICHA SELLADA Y AQUI NO SE RE-ADJUDICA: "
        "docs/plan/OPERACIONES.jsonl escribe superviviente ocho_fases_experiencia_cliente "
        "el 12 ago 2026, POR CABLEADO SIN EMPATE, y ademas con el contenido del mismo lado: "
        "4 pasos contra 3. AQUI NO HAY CHOQUE DE NINGUNA CLASE, a diferencia de OP-M-03-I: "
        "leido con las varas por forma de los tramos, pasos 4 contra 3 apunta al "
        "superviviente y condiciones 1 contra 2 apunta al que muere, o sea CHOCAN entre si, "
        "Y EN UN CHOCAN DECIDE LA PIEZA DECLARADA (acta 53, pregunta 3), que aqui es la "
        "adjudicacion sellada y nombra al superviviente; y el cableado, que en esta ficha SI "
        "es la vara escrita, apunta al mismo sitio con el margen mas ancho de las dos "
        "operaciones de la vuelta. TRES VIAS, UN SOLO NODO. "
        "UNA DIVERGENCIA DE MEDICION SE DECLARA: la ficha midio 13 contra 3 en cableado el "
        "12 ago 2026 y HOY se mide 12 contra 3 (scripts/plan/simular_fusion.py, corrido en "
        "esta vuelta). LO QUE LA MEDICION DE HOY SOSTIENE, sin afirmar cual: CINCO de los "
        "nodos que nombran al superviviente estan HOY DEPRECADOS (fase_accomplish, "
        "fase_activate, fase_admit, fase_affirm y seis_medios_comunicacion_cliente), y el "
        "grado solo cuenta vivos. LA DIFERENCIA NO CAMBIA NADA: 12 contra 3 sigue siendo "
        "cableado sin empate."
    ),
    "pasos": {
        # 1. Mapear en que fase se encuentra actualmente cada segmento de clientes.
        "1": ["CUBIERTO", 1],
        # 2. Disenar acciones especificas de la empresa para cada una de las 8 fases
        #    (no solo para Assess y Admit).
        "2": ["CUBIERTO", 2],
        # 3. Priorizar el diseno de experiencia en las fases Affirm y Activate.
        "3": ["APPEND"],
    },
    "condiciones": {
        # 1. Cuando la empresa solo tiene procesos disenados para atraer y cerrar ventas,
        #    pero no para despues de la compra.
        "1": ["CUBIERTO", 1],
        # 2. Cuando se busca reducir la tasa de abandono temprano de clientes.
        "2": ["APPEND"],
    },
    "nota": (
        "CINCO PIEZAS REPARTIDAS: dos viajan enteras y tres ya estaban dichas. CERO "
        "INCISOS, y se dice por que en vez de callarlo: LOS CUATRO PASOS DEL SUPERVIVIENTE "
        "CIERRAN EN PUNTO, uno a uno, asi que ningun inciso se adosa limpio y la guarda de "
        "la juntura lo habria puesto en ROJO. Es exactamente el supuesto en el que la "
        "politica manda CUBIERTO con la perdida NOMBRADA, y el limite que el acta 62 le "
        "puso al D9 no muerde aqui porque no hay INCISO que ahorrarse. "
        "LA PIEZA QUE LA FICHA MANDA PRESERVAR VIAJA ENTERA: priorizar el diseno de "
        "experiencia en las fases AFFIRM y ACTIVATE, que suelen ser las mas descuidadas y "
        "donde ocurre la mayor desercion (paso 3 del que muere), es un gesto que el "
        "superviviente no hace en ningun grado: el superviviente detecta donde se atascan "
        "los clientes, pero no nombra ni prioriza esas dos fases. Va de APPEND, y con eso "
        "queda cumplida la verificacion que la ficha escribe (las dos prioridades estan en "
        "el texto del superviviente tras la fusion). "
        "LAS DOS PIEZAS QUE LA FICHA RECLASIFICA COMO QUE VIVEN DENTRO SE COMPRUEBAN Y NO "
        "SE TOCAN: detectar en que fase se atascan es el paso 3 del superviviente y el plan "
        "de avance es su paso 4, los dos leidos hoy y los dos intactos tras la fusion. "
        "LA CONDICION 2 DEL QUE MUERE VA DE APPEND PORQUE ES UN DISPARADOR DISTINTO y no un "
        "matiz (acta 55, pregunta 5): buscar REDUCIR LA TASA DE ABANDONO TEMPRANO es un "
        "objetivo de negocio, y la condicion 1 del superviviente dispara por necesitar una "
        "ESTRUCTURA SISTEMATICA para la posventa, que es otra cosa. La condicion 1 del que "
        "muere SI es el mismo disparador dicho desde el lado del sintoma (solo hay procesos "
        "para atraer y cerrar ventas, y nada para despues de la compra) y por eso va "
        "CUBIERTA y SIN perdida: lo operativo, el DESPUES DE LA VENTA, esta en el texto del "
        "superviviente con todas sus letras. "
        "UNA PERDIDA SELLADA, Y ES UNA MAS DE LAS QUE LA FICHA LISTABA: LA FICHA DICE QUE "
        "LA UNICA PERDIDA REAL DE ESTA FUSION ES PRIORIZAR AFFIRM Y ACTIVATE, y esa VIAJA, "
        "asi que por la letra de la ficha esta fusion cerraria con CERO perdidas. MEDIDO "
        "CONTRA EL TEXTO DE HOY NO ES ASI: el paso 2 del que muere lleva un parentesis, NO "
        "SOLO PARA ASSESS Y ADMIT, que no esta en ningun paso del superviviente. Se sella "
        "en vez de callarse, y la diferencia con la ficha se declara: la pasada de perdidas "
        "recomputadas de aquella ficha es del 12 ago 2026 y es ANTERIOR al contrato CAMPO "
        "PROPIO v1, que es el que obliga a sellar en campo lo que antes vivia en la prosa. "
        "VA MARCADO COMO DISCUTIBLE EN LA SECCION 6 DEL REPORTE DE ESTA VUELTA."
    ),
    "perdidas": [
        {
            "especie": "DE PARAMETRO DE PASO",
            "que": ("el parentesis NO SOLO PARA ASSESS Y ADMIT, que es la advertencia de "
                    "que el diseno no puede pararse en las dos fases previas a la venta; y "
                    "el encuadre de ACCIONES ESPECIFICAS DE LA EMPRESA frente al de "
                    "EXPERIENCIA EMOCIONAL DESEADA del paso 2 del superviviente. SE DICE LO "
                    "QUE NO SE PIERDE: el gesto de disenar para CADA UNA DE LAS OCHO FASES "
                    "esta entero en ese paso 2, y el plan de accion concreto es el paso 4 "
                    "del superviviente. NO SE ADOSA DE INCISO porque el paso 2 del "
                    "superviviente cierra en punto y la guarda de la juntura lo rechaza"),
            "donde": "paso 2 de fases_de_retencion_de_clientes",
            "enrutada_a": "la fase 04, que redacta y afina los pasos del superviviente",
        },
    ],
    "simulacion_de_hoy": (
        "scripts/plan/simular_fusion.py corrido en la vuelta 63 ANTES de tocar un nodo "
        "(docs/loop/SALIDA_V63_SIM_OPM02PROG.txt): TRES entradas se redirigen "
        "(estrategia_de_ventas, pensamiento_h2h y UNA DEL PROPIO SUPERVIVIENTE, que queda "
        "como auto arista), UNA duplicada nueva (pensamiento_h2h en nodos_siguientes) y UNA "
        "auto arista. ES IDENTICO AL DIGITO A LO QUE LA SIMULACION SELLADA DE LA FICHA "
        "DESCRIBE, con los tres nombres calzando uno a uno."
    ),
}
