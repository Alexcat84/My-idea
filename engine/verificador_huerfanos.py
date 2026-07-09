# -*- coding: utf-8 -*-
"""Fase 3.1 (caja de vidrio): automatiza la vara de auditoria "ningun
numero huerfano" que hasta ahora era un ritual manual. Extrae todo
numeral de un texto (el reporte completo, o la seccion financiera del
plan) y verifica que pertenezca al conjunto de numeros que de verdad se
le entregaron a quien narro: salidas de calculadora.py (solo aplica al
reporte -- el redactor del plan nunca corre la calculadora), numeros
declarados por el usuario (numeros_proyecto), y numerales presentes en
el texto de los nodos del material (pasos_accionables/entregable_esperado
de ruta+cosecha). Cualquier numero fuera de ese conjunto se marca
'numero_huerfano' -- señal de triage para revision humana (Fase 3.1),
NO un guardian que bloquee nada (a diferencia del GIGO numerico, que si
aborta la narracion)."""
import re

_PATRON_NUMERO = re.compile(r'-?\$?\d[\d.,]*%?')

# Tolerancia absoluta para redondeos de narracion (ej. el modelo dice
# "16.0" cuando el valor exacto es 16, o trunca un decimal al narrar).
TOLERANCIA = 0.05


def _normalizar_numero(token):
    """'$1.700' -> 1700.0, '-2976.9%' -> -2976.9, '17.5' -> 17.5.
    Heuristica de tolerancia de formato (Fase 3.1, ejemplo mandatado
    '1.700 vs 1700'): un unico punto seguido de EXACTAMENTE 3 digitos se
    interpreta como separador de miles (estilo hispano), no como parte
    decimal -- distingue de casos genuinamente decimales como '0.35' (2
    digitos) o '17.5' (1 digito)."""
    t = token.strip().replace("$", "").replace(",", "")
    if t.endswith("%"):
        t = t[:-1]
    partes = t.split(".")
    if len(partes) == 2 and len(partes[1]) == 3 and partes[0].lstrip("-").isdigit():
        t = partes[0] + partes[1]
    try:
        return float(t)
    except ValueError:
        return None


def extraer_numeros(texto):
    """Devuelve [(valor_normalizado, token_original, contexto), ...] para
    cada numeral valido encontrado en el texto, con ~30 caracteres de
    contexto a cada lado (para que el flag sea legible, no solo un
    numero suelto)."""
    encontrados = []
    for m in _PATRON_NUMERO.finditer(texto or ""):
        valor = _normalizar_numero(m.group())
        if valor is None:
            continue
        inicio, fin = max(0, m.start() - 30), min(len(texto), m.end() + 30)
        contexto = texto[inicio:fin].replace("\n", " ").strip()
        encontrados.append((valor, m.group(), contexto))
    return encontrados


def _numeros_de_estructura(obj):
    """Recorre cualquier dict/list anidado (las salidas de calculadora.py,
    o numeros_proyecto) y devuelve el conjunto de valores numericos hoja,
    ignorando None/str/bool (bool antes que (int,float): en Python
    isinstance(True, int) es True)."""
    numeros = set()
    if isinstance(obj, bool):
        return numeros
    if isinstance(obj, (int, float)):
        numeros.add(round(float(obj), 4))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            # Fase 3.1: escenarios_adopcion usa claves como '50%'/'100%' --
            # un numero en una CLAVE (no solo en un valor) tambien cuenta
            # como legitimo, o el narrador que la menciona ("al 50% de tu
            # meta") se marcaria como huerfano por error.
            valor_clave = _normalizar_numero(str(k))
            if valor_clave is not None:
                numeros.add(round(valor_clave, 4))
            numeros |= _numeros_de_estructura(v)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            numeros |= _numeros_de_estructura(v)
    return numeros


def cerradura_aritmetica(numeros):
    """Fase 3.1: un narrador que solo describe salidas YA calculadas
    igual hace aritmetica simple de un paso (sumas/restas/multiplicacion)
    para dar contexto util -- ej. 'a partir del usuario 17 ya es
    ganancia' cuando el equilibrio calculado es 16, 'te quedan $60'
    cuando ingreso=260 y costos_fijos=200, o 'con 20 usuarios son $260'
    cuando precio=13. Eso no es fabricar cifras, es narrar una
    combinacion directa de valores ya permitidos, y el verificador debe
    tolerarlo. Incluye tambien +-1 (el modismo 'la unidad siguiente/
    anterior al equilibrio' es comun). Deliberadamente NO recursivo (una
    sola combinacion sobre los numeros YA permitidos, nunca sobre
    combinaciones de combinaciones): mas profundidad diluye la señal
    real y puede generar colisiones con numeros genuinamente inventados
    (verificado con el caso mandatado de 4500)."""
    numeros = set(numeros)
    cerradura = set(numeros)
    lista = list(numeros)
    for v in lista:
        cerradura.add(round(v + 1, 4))
        cerradura.add(round(v - 1, 4))
    for i, a in enumerate(lista):
        for b in lista[i + 1:]:
            cerradura.add(round(a + b, 4))
            cerradura.add(round(abs(a - b), 4))
            cerradura.add(round(a * b, 4))
    return cerradura


def numeros_de_calculadora(resultados_calculadora):
    """Todo numero que calculadora.calcular_reporte() produjo, en
    cualquier sub-resultado (costo, margen, punto_equilibrio, capacidad,
    escenarios, ciclo_conversion_efectivo)."""
    return _numeros_de_estructura(resultados_calculadora)


def numeros_declarados(numeros_proyecto):
    """Todo numero que el usuario declaro (numeros_proyecto), incluyendo
    rangos {min, max}."""
    return _numeros_de_estructura(numeros_proyecto or {})


def numeros_de_material(textos):
    """Todo numero mencionado en el texto de los nodos del material
    (pasos_accionables, entregable_esperado de ruta+cosecha) -- si el
    grafo mismo menciona un numero (ej. un ejemplo teorico), citarlo en
    el plan no es un numero huerfano."""
    numeros = set()
    for texto in textos:
        for valor, _, _ in extraer_numeros(texto):
            numeros.add(round(valor, 4))
    return numeros


def _pertenece(valor, permitidos):
    return any(abs(valor - p) <= TOLERANCIA for p in permitidos)


def verificar_numeros_huerfanos(texto, numeros_permitidos, registrar_evento=None):
    """Extrae todo numeral de `texto` y registra 'numero_huerfano' (uno
    por numero unico, via registrar_evento si se provee) para cada uno
    que no pertenezca a numeros_permitidos. Devuelve la lista de
    huerfanos encontrados (aunque no se pase registrar_evento, para que
    quien llame -- incluyendo los tests -- pueda inspeccionarla)."""
    huerfanos = []
    vistos = set()
    for valor, token, contexto in extraer_numeros(texto):
        if _pertenece(valor, numeros_permitidos):
            continue
        clave = (token, contexto)
        if clave in vistos:
            continue
        vistos.add(clave)
        huerfano = {"valor": token, "contexto": contexto}
        huerfanos.append(huerfano)
        if registrar_evento:
            registrar_evento({"tipo": "numero_huerfano", **huerfano})
    return huerfanos
