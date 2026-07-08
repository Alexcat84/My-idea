# -*- coding: utf-8 -*-
"""
calculadora.py - Motor v2.1/v2.2: calculadora deterministica del Reporte de
Sostenibilidad. CERO llamadas a LLM: funciones puras sobre
numeros_proyecto (el dict {campo: {"valor":..., ...}} que
prototipo_motor.py acumula via el intérprete de turno). Cada formula trae
en su docstring el node_id del grafo del que sale (o una nota explicita
si aun no tiene nodo dedicado).

Cada funcion publica devuelve un dict con, como minimo, "insumos_usados"
(lista de campos de numeros_proyecto que SI se usaron) e
"insumos_faltantes" (campos que faltan para completar ese calculo). Si
falta algo esencial, el valor central es None y el llamador (el modo
--reporte) es responsable de explicarlo, nunca de inventarlo.

Manejo de rangos: si el usuario dio un rango para un campo (numeros_
proyecto[campo]["valor"] = {"min": x, "max": y}), el resultado tambien
sale como rango {"min":, "max":}, calculado con el emparejamiento de
intervalos correcto por operacion (suma/resta cambian que lado es el
"peor caso"), no con un min-con-min ingenuo en todos los casos.

Motor v2.2: `tipo_oferta` ('producto_fisico'|'servicio'|'digital'|'mixto'|
None) generaliza el costo unitario y los escenarios para ofertas
digitales, que no tienen horas_por_unidad/valor_hora ni un techo de
capacidad semanal en el mismo sentido que un producto fisico o un
servicio por horas. None/'producto_fisico'/'servicio' usan las formulas
originales sin cambios (retrocompatible con proyectos pre-v2.2).
"""

import math

SEMANAS_POR_MES = 4  # aproximacion deliberada (no 4.33) para numeros redondos y verificables


def _valor(numeros, campo):
    entry = (numeros or {}).get(campo)
    if not entry or entry.get("valor") is None:
        return None
    return entry["valor"]


def _es_rango(v):
    return isinstance(v, dict) and "min" in v and "max" in v


def _lado(v, lado):
    return v[lado] if _es_rango(v) else v


def _hay_rango(*vals):
    return any(_es_rango(v) for v in vals)


def _r(x, nd=2):
    return round(x, nd) if x is not None else None


def costo_unitario_total(numeros, tipo_oferta=None):
    """Costo por unidad = costo_materiales_unidad + horas_por_unidad * valor_hora.
    Fuente: nodo 'hoja_estimacion_costos' (metodo bottom-up: sumar mano de
    obra + materiales) y 'margen_bruto' (estructura costo-precio) del grafo.

    Motor v2.2, rama 'digital': una oferta digital no tiene "horas por
    unidad" de produccion (no se fabrica una unidad a la vez con trabajo
    manual) -- el costo unitario es directamente el costo variable por
    usuario/unidad declarado (costo_materiales_unidad, reusado como alias
    de "costo variable"), sin exigir horas_por_unidad/valor_hora como
    insumos faltantes (serian datos que no aplican a este tipo de oferta,
    no datos que el usuario olvido dar)."""
    materiales = _valor(numeros, "costo_materiales_unidad")
    if tipo_oferta == "digital":
        if materiales is None:
            return {"valor": None, "insumos_usados": [], "insumos_faltantes": ["costo_materiales_unidad"]}
        return {"valor": materiales, "insumos_usados": ["costo_materiales_unidad"], "insumos_faltantes": []}
    horas = _valor(numeros, "horas_por_unidad")
    valor_hora = _valor(numeros, "valor_hora")
    faltantes = [c for c, v in (
        ("costo_materiales_unidad", materiales), ("horas_por_unidad", horas), ("valor_hora", valor_hora),
    ) if v is None]
    if faltantes:
        return {"valor": None, "insumos_usados": [], "insumos_faltantes": faltantes}
    if _hay_rango(materiales, horas, valor_hora):
        lo = _lado(materiales, "min") + _lado(horas, "min") * _lado(valor_hora, "min")
        hi = _lado(materiales, "max") + _lado(horas, "max") * _lado(valor_hora, "max")
        valor = {"min": _r(lo), "max": _r(hi)}
    else:
        valor = _r(materiales + horas * valor_hora)
    return {"valor": valor, "insumos_usados": ["costo_materiales_unidad", "horas_por_unidad", "valor_hora"],
            "insumos_faltantes": []}


def margen_unitario(numeros, tipo_oferta=None):
    """Margen por unidad = precio_tentativo - costo_unitario_total; porcentaje
    = margen / precio. Fuente: nodo 'margen_bruto' (Gross Profit Margin).
    Para ofertas digitales, esto es el "margen por usuario" (Motor v2.2) --
    misma formula, el nombre cambia solo en la narracion, no en el calculo."""
    costo = costo_unitario_total(numeros, tipo_oferta=tipo_oferta)
    precio = _valor(numeros, "precio_tentativo")
    faltantes = list(costo["insumos_faltantes"])
    if precio is None:
        faltantes.append("precio_tentativo")
    if faltantes:
        return {"valor": None, "porcentaje": None, "insumos_usados": [], "insumos_faltantes": faltantes}
    costo_v = costo["valor"]
    if _hay_rango(costo_v, precio):
        # peor caso: precio bajo y costo alto; mejor caso: precio alto y costo bajo
        lo = _lado(precio, "min") - _lado(costo_v, "max")
        hi = _lado(precio, "max") - _lado(costo_v, "min")
        margen = {"min": _r(lo), "max": _r(hi)}
        p_lo = _lado(precio, "min")
        p_hi = _lado(precio, "max")
        porcentaje = {"min": _r(lo / p_lo * 100, 1) if p_lo else None,
                      "max": _r(hi / p_hi * 100, 1) if p_hi else None}
    else:
        margen = _r(precio - costo_v)
        porcentaje = _r(margen / precio * 100, 1) if precio else None
    return {"valor": margen, "porcentaje": porcentaje,
            "insumos_usados": costo["insumos_usados"] + ["precio_tentativo"], "insumos_faltantes": []}


def punto_equilibrio_unidades_mes(numeros, tipo_oferta=None):
    """Unidades/mes para cubrir costos fijos = costos_fijos_mensuales / margen_unitario.
    Formula de margen de contribucion. Fuente: nodo 'punto_equilibrio_unidades'
    (dataset v1.2 - antes de esa version, esta formula no tenia nodo propio).

    Motor v2.2: redondeado hacia ARRIBA (math.ceil), no al decimal mas
    cercano -- no se pueden vender fracciones de unidad, y quedarse corto
    en la unidad de redondeo (ej. 15 en vez de 16 cuando el calculo exacto
    da 15.38) significa no cubrir los costos fijos ese mes. Verificado
    contra el caso real que motivo este cambio: $200 fijos / $13 margen =
    15.38 -> se necesitan 16 packs, no 15.4."""
    margen = margen_unitario(numeros, tipo_oferta=tipo_oferta)
    costos_fijos = _valor(numeros, "costos_fijos_mensuales")
    faltantes = list(margen["insumos_faltantes"])
    if costos_fijos is None:
        faltantes.append("costos_fijos_mensuales")
    if faltantes:
        return {"valor": None, "insumos_usados": [], "insumos_faltantes": faltantes}
    margen_v = margen["valor"]
    if _hay_rango(margen_v, costos_fijos):
        m_lo, m_hi = _lado(margen_v, "min"), _lado(margen_v, "max")
        cf_lo, cf_hi = _lado(costos_fijos, "min"), _lado(costos_fijos, "max")
        if m_lo <= 0 or m_hi <= 0:
            return {"valor": None, "insumos_usados": [], "insumos_faltantes": [],
                    "nota": "el margen por unidad no es positivo en todo el rango; no hay punto de equilibrio posible asi"}
        valor = {"min": math.ceil(cf_lo / m_hi), "max": math.ceil(cf_hi / m_lo)}
    else:
        if margen_v <= 0:
            return {"valor": None, "insumos_usados": [], "insumos_faltantes": [],
                    "nota": "el margen por unidad no es positivo; no hay punto de equilibrio posible con estos numeros"}
        valor = math.ceil(costos_fijos / margen_v)
    return {"valor": valor, "insumos_usados": margen["insumos_usados"] + ["costos_fijos_mensuales"],
            "insumos_faltantes": []}


def techo_ingreso_capacidad(numeros):
    """Techo de ingreso mensual segun capacidad declarada:
    unidades_mes = capacidad_semanal * SEMANAS_POR_MES; ingreso = unidades_mes * precio;
    margen_mensual = unidades_mes * margen_unitario. Sin nodo dedicado (aritmetica
    directa sobre capacidad_semanal y precio_tentativo, ambos ya declarados por el usuario)."""
    capacidad = _valor(numeros, "capacidad_semanal")
    precio = _valor(numeros, "precio_tentativo")
    faltantes = [c for c, v in (("capacidad_semanal", capacidad), ("precio_tentativo", precio)) if v is None]
    if faltantes:
        return {"unidades_mes": None, "ingreso": None, "margen_mensual": None,
                "insumos_usados": [], "insumos_faltantes": faltantes}
    margen = margen_unitario(numeros)
    if _hay_rango(capacidad, precio) or _es_rango(margen["valor"]):
        cap_lo, cap_hi = _lado(capacidad, "min"), _lado(capacidad, "max")
        precio_lo, precio_hi = _lado(precio, "min"), _lado(precio, "max")
        u_lo, u_hi = _r(cap_lo * SEMANAS_POR_MES, 1), _r(cap_hi * SEMANAS_POR_MES, 1)
        unidades_mes = {"min": u_lo, "max": u_hi}
        ingreso = {"min": _r(u_lo * precio_lo), "max": _r(u_hi * precio_hi)}
        margen_mensual = None
        if margen["valor"] is not None:
            m_lo = _lado(margen["valor"], "min")
            m_hi = _lado(margen["valor"], "max")
            margen_mensual = {"min": _r(u_lo * m_lo), "max": _r(u_hi * m_hi)}
    else:
        unidades_mes = _r(capacidad * SEMANAS_POR_MES, 1)
        ingreso = _r(unidades_mes * precio)
        margen_mensual = _r(unidades_mes * margen["valor"]) if margen["valor"] is not None else None
    return {"unidades_mes": unidades_mes, "ingreso": ingreso, "margen_mensual": margen_mensual,
            "insumos_usados": ["capacidad_semanal", "precio_tentativo"] + margen["insumos_usados"],
            "insumos_faltantes": margen["insumos_faltantes"]}


def escenarios_capacidad(numeros):
    """Tres escenarios relativos a la capacidad declarada: pesimista (50% de
    la capacidad), base (100%, el techo real), y sobredemanda (150% de
    demanda estimada, mostrando cuanta venta se pierde porque la capacidad
    de produccion no alcanza). Sin nodo dedicado (deriva de techo_ingreso_capacidad)."""
    techo = techo_ingreso_capacidad(numeros)
    if techo["insumos_faltantes"] or techo["unidades_mes"] is None:
        return {"pesimista": None, "base": None, "sobredemanda": None,
                "insumos_usados": [], "insumos_faltantes": techo["insumos_faltantes"]}
    if _es_rango(techo["unidades_mes"]):
        # Con rangos, los escenarios de capacidad se simplifican al punto medio
        # para no explotar en un arbol de combinaciones dificil de leer en el reporte.
        unidades_base = _r((techo["unidades_mes"]["min"] + techo["unidades_mes"]["max"]) / 2, 1)
        precio = _r((_lado(_valor(numeros, "precio_tentativo"), "min") + _lado(_valor(numeros, "precio_tentativo"), "max")) / 2)
        margen_u = margen_unitario(numeros)["valor"]
        if _es_rango(margen_u):
            margen_u = _r((margen_u["min"] + margen_u["max"]) / 2)
    else:
        unidades_base = techo["unidades_mes"]
        precio = _valor(numeros, "precio_tentativo")
        margen_u = margen_unitario(numeros)["valor"]

    def _escenario(factor):
        unidades = _r(unidades_base * factor, 1)
        return {
            "unidades_mes": unidades,
            "ingreso": _r(unidades * precio),
            "margen_mensual": _r(unidades * margen_u) if margen_u is not None else None,
        }

    pesimista = _escenario(0.5)
    base = _escenario(1.0)
    demanda_estimada = _r(unidades_base * 1.5, 1)
    unidades_no_atendidas = _r(demanda_estimada - unidades_base, 1)
    sobredemanda = {
        "demanda_estimada": demanda_estimada,
        "unidades_producibles": unidades_base,
        "unidades_no_atendidas": unidades_no_atendidas,
        # Hotfix v2.1.1: dos campos con semantica distinta, no uno solo.
        # ingreso_perdido_estimado = ventas que no se facturan (unidades x
        # PRECIO); margen_perdido_estimado = ganancia que no llega (unidades
        # x MARGEN). Antes, "ingreso_perdido_estimado" calculaba con margen
        # por error, subestimando 5x el costo de oportunidad real (en el
        # escenario canonico: reportaba $170 cuando el ingreso no facturado
        # real es $850 - el margen perdido si es $170, pero es OTRO numero).
        "ingreso_perdido_estimado": _r(unidades_no_atendidas * precio),
        "margen_perdido_estimado": _r(unidades_no_atendidas * margen_u) if margen_u is not None else None,
    }
    return {"pesimista": pesimista, "base": base, "sobredemanda": sobredemanda,
            "insumos_usados": techo["insumos_usados"], "insumos_faltantes": []}


def escenarios_adopcion(numeros, tipo_oferta=None):
    """Motor v2.2, rama 'digital': un producto digital no tiene un techo de
    capacidad semanal como un producto fisico (no se "produce" una unidad a
    la vez) -- en su lugar, los tres escenarios son niveles de ADOPCION de
    una meta declarada (unidades_vendidas, reusado aqui como "meta mensual
    realista de usuarios o ventas"): 50%, 100%, 200% de esa meta. Sin nodo
    dedicado todavia (aritmetica directa sobre unidades_vendidas y
    precio_tentativo, igual que techo_ingreso_capacidad hace con
    capacidad_semanal)."""
    meta = _valor(numeros, "unidades_vendidas")
    precio = _valor(numeros, "precio_tentativo")
    faltantes = [c for c, v in (("unidades_vendidas", meta), ("precio_tentativo", precio)) if v is None]
    if faltantes:
        return {"50%": None, "100%": None, "200%": None, "insumos_usados": [], "insumos_faltantes": faltantes}
    margen = margen_unitario(numeros, tipo_oferta=tipo_oferta)
    margen_u = margen["valor"]

    if _hay_rango(meta, precio) or _es_rango(margen_u):
        # Mismo criterio de simplificacion que escenarios_capacidad: los
        # rangos colapsan al punto medio para no explotar en un arbol de
        # combinaciones dificil de leer en el reporte.
        meta_v = _r((_lado(meta, "min") + _lado(meta, "max")) / 2, 1) if _es_rango(meta) else meta
        precio_v = _r((_lado(precio, "min") + _lado(precio, "max")) / 2) if _es_rango(precio) else precio
        margen_v = _r((_lado(margen_u, "min") + _lado(margen_u, "max")) / 2) if _es_rango(margen_u) else margen_u
    else:
        meta_v, precio_v, margen_v = meta, precio, margen_u

    def _escenario(factor):
        unidades = _r(meta_v * factor, 1)
        return {
            "unidades": unidades,
            "ingreso": _r(unidades * precio_v),
            "margen_total": _r(unidades * margen_v) if margen_v is not None else None,
        }

    return {
        "50%": _escenario(0.5), "100%": _escenario(1.0), "200%": _escenario(2.0),
        "insumos_usados": ["unidades_vendidas", "precio_tentativo"] + margen["insumos_usados"],
        "insumos_faltantes": [],
    }


UMBRAL_MARGEN_PCT_INCONSISTENTE = -100  # margen mas negativo que -100% del precio
UMBRAL_PRECIO_MINIMO_FRACCION_COSTO = 0.05  # precio < 5% del costo unitario


def detectar_inconsistencia_gigo(numeros, tipo_oferta=None):
    """Guardian GIGO (Motor v2.2): antes de narrar cualquier conclusion
    financiera, verifica que los numeros capturados no sean matematicamente
    absurdos al punto de sugerir que una cifra quedo en la unidad
    equivocada (ej. un presupuesto MENSUAL leido como costo POR UNIDAD).
    Caso real que motiva esta funcion: costo_materiales_unidad=200 (era en
    realidad presupuesto mensual), horas_por_unidad=4 (eran meses de
    desarrollo), precio_tentativo=13 (precio real del pack) -> costo total
    400, margen -387, margen_pct = -387/13*100 = -2976.9%. El reporte
    narro con confianza 'no existe punto de equilibrio posible' sobre un
    modelo cuyo equilibrio real (una vez corregida la unidad) es de solo
    16 packs/mes. Esta funcion existe para que ese calculo NUNCA se narre
    como si fuera confiable: devuelve inconsistente=True y el llamador
    (modo_reporte) debe mostrar los datos crudos con la inconsistencia
    senalada, no una conclusion financiera."""
    costo = costo_unitario_total(numeros, tipo_oferta=tipo_oferta)
    precio = _valor(numeros, "precio_tentativo")
    if costo["valor"] is None or precio is None:
        return {"inconsistente": False, "motivo": None}
    costo_v = costo["valor"]
    precio_v = precio
    if _es_rango(costo_v):
        costo_v = (costo_v["min"] + costo_v["max"]) / 2
    if _es_rango(precio_v):
        precio_v = (precio_v["min"] + precio_v["max"]) / 2
    if costo_v <= 0 or precio_v <= 0:
        return {"inconsistente": False, "motivo": None}
    margen_pct = (precio_v - costo_v) / precio_v * 100
    if margen_pct < UMBRAL_MARGEN_PCT_INCONSISTENTE:
        return {"inconsistente": True, "motivo": (
            f"con estos numeros el margen por unidad es {_r(margen_pct, 1)}%, muy por debajo "
            "de -100% -- es mas probable que alguna cifra este en la unidad equivocada (por "
            "ejemplo, un presupuesto mensual leido como costo por unidad, o un plazo en meses "
            "leido como horas) que que cada venta pierda esa cantidad de dinero"
        )}
    if precio_v < costo_v * UMBRAL_PRECIO_MINIMO_FRACCION_COSTO:
        return {"inconsistente": True, "motivo": (
            "el precio declarado es menos del 5% del costo unitario calculado -- revisa si el "
            "precio y el costo estan expresados en la misma unidad (por pieza, por mes, etc.)"
        )}
    return {"inconsistente": False, "motivo": None}


CAMPOS_CICLO_CONVERSION_EFECTIVO = ("dias_inventario", "dias_cobro_clientes", "dias_pago_proveedores")


def ciclo_conversion_efectivo(numeros):
    """Cash Conversion Cycle = dias_inventario + dias_cobro_clientes - dias_pago_proveedores.
    Fuente: nodo 'ciclo_de_conversion_de_efectivo'. Los 8 campos nucleares de
    numeros_proyecto (Motor v2.1) no incluyen datos de cobro/pago todavia, asi
    que esta funcion casi siempre reportara insumos_faltantes hasta que una
    fase futura capture esos campos; existe para completar la formula del nodo
    y para no fingir un calculo que no se puede hacer con lo disponible."""
    valores = {c: _valor(numeros, c) for c in CAMPOS_CICLO_CONVERSION_EFECTIVO}
    faltantes = [c for c, v in valores.items() if v is None]
    if faltantes:
        return {"valor": None, "insumos_usados": [], "insumos_faltantes": faltantes}
    valor = valores["dias_inventario"] + valores["dias_cobro_clientes"] - valores["dias_pago_proveedores"]
    return {"valor": _r(valor, 1), "insumos_usados": list(CAMPOS_CICLO_CONVERSION_EFECTIVO), "insumos_faltantes": []}


def calcular_reporte(numeros_proyecto, tipo_oferta=None):
    """Corre todos los calculos disponibles sobre numeros_proyecto y devuelve
    un dict agregado. No lanza excepciones ante datos faltantes: cada
    sub-resultado reporta sus propios insumos_faltantes.

    Motor v2.2: tipo_oferta=None o 'producto_fisico'/'servicio' usa
    'capacidad'/'escenarios' basados en capacidad semanal (retrocompatible,
    formulas sin cambios). tipo_oferta='digital' usa 'escenarios' basados
    en adopcion de una meta declarada en su lugar (escenarios_adopcion);
    'capacidad' queda None porque el techo de produccion semanal no aplica
    a una oferta digital. El guardian GIGO (detectar_inconsistencia_gigo)
    NO vive aqui adentro a proposito: modo_reporte lo llama por separado
    antes de decidir si narra o no, para no romper el shape de este dict
    (cada valor sigue siendo un resultado con insumos_usados/insumos_
    faltantes, como esperan los llamadores existentes)."""
    resultado = {
        "costo_unitario": costo_unitario_total(numeros_proyecto, tipo_oferta=tipo_oferta),
        "margen": margen_unitario(numeros_proyecto, tipo_oferta=tipo_oferta),
        "punto_equilibrio": punto_equilibrio_unidades_mes(numeros_proyecto, tipo_oferta=tipo_oferta),
        "ciclo_conversion_efectivo": ciclo_conversion_efectivo(numeros_proyecto),
    }
    if tipo_oferta == "digital":
        resultado["capacidad"] = {"unidades_mes": None, "ingreso": None, "margen_mensual": None,
                                   "insumos_usados": [], "insumos_faltantes": []}
        resultado["escenarios"] = escenarios_adopcion(numeros_proyecto, tipo_oferta=tipo_oferta)
    else:
        resultado["capacidad"] = techo_ingreso_capacidad(numeros_proyecto)
        resultado["escenarios"] = escenarios_capacidad(numeros_proyecto)
    return resultado
