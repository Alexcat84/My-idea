# -*- coding: utf-8 -*-
"""
test_calculadora.py - Motor v2.1: aserciones numericas exactas para
engine/calculadora.py. Sin pytest (mismo estilo que scripts/run_phase1.py):
un script plano que corre asserts y sale con codigo distinto de cero si
algo falla.

Uso: python engine/test_calculadora.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import calculadora as c


def _numeros(**campos):
    """Helper: construye un numeros_proyecto de prueba a partir de
    campo=valor (valor puede ser un numero o un dict {"min":,"max":})."""
    return {campo: {"valor": valor, "unidad": None, "texto_original": ""} for campo, valor in campos.items()}


def test_escenario_macetas():
    """El escenario mandatado: resina/materiales $8, 4 horas, valora su hora
    en $15, vendería a $85, capacidad 5/semana, sin costos fijos declarados."""
    numeros = _numeros(
        costo_materiales_unidad=8, horas_por_unidad=4, valor_hora=15,
        precio_tentativo=85, capacidad_semanal=5,
    )

    costo = c.costo_unitario_total(numeros)
    assert costo["valor"] == 68, costo
    assert costo["insumos_faltantes"] == []

    margen = c.margen_unitario(numeros)
    assert margen["valor"] == 17, margen
    assert margen["porcentaje"] == 20.0, margen

    equilibrio = c.punto_equilibrio_unidades_mes(numeros)
    assert equilibrio["valor"] is None
    assert equilibrio["insumos_faltantes"] == ["costos_fijos_mensuales"], equilibrio

    capacidad = c.techo_ingreso_capacidad(numeros)
    assert capacidad["unidades_mes"] == 20, capacidad
    assert capacidad["ingreso"] == 1700, capacidad
    assert capacidad["margen_mensual"] == 340, capacidad

    escenarios = c.escenarios_capacidad(numeros)
    assert escenarios["pesimista"] == {"unidades_mes": 10, "ingreso": 850, "margen_mensual": 170}, escenarios["pesimista"]
    assert escenarios["base"] == {"unidades_mes": 20, "ingreso": 1700, "margen_mensual": 340}, escenarios["base"]
    sd = escenarios["sobredemanda"]
    assert sd["demanda_estimada"] == 30, sd
    assert sd["unidades_producibles"] == 20, sd
    assert sd["unidades_no_atendidas"] == 10, sd
    assert sd["ingreso_perdido_estimado"] == 170, sd

    cce = c.ciclo_conversion_efectivo(numeros)
    assert cce["valor"] is None
    assert set(cce["insumos_faltantes"]) == set(c.CAMPOS_CICLO_CONVERSION_EFECTIVO)

    print("OK: test_escenario_macetas (costo=68, margen=17/20%, techo=20u/$1700/$340, "
          "equilibrio y CCE correctamente pendientes)")


def test_costo_con_rango():
    """Si el usuario da un rango ('entre $6 y $10 en materiales'), el costo,
    el margen y el porcentaje deben salir como rango, con el emparejamiento
    de intervalos correcto (no un min-con-min ingenuo en la resta)."""
    numeros = _numeros(
        costo_materiales_unidad={"min": 6, "max": 10}, horas_por_unidad=4,
        valor_hora=15, precio_tentativo=85,
    )
    costo = c.costo_unitario_total(numeros)
    assert costo["valor"] == {"min": 66, "max": 70}, costo

    margen = c.margen_unitario(numeros)
    # peor caso: costo alto (70) -> margen 85-70=15; mejor caso: costo bajo (66) -> margen 85-66=19
    assert margen["valor"] == {"min": 15, "max": 19}, margen
    assert margen["porcentaje"]["min"] == round(15 / 85 * 100, 1)
    assert margen["porcentaje"]["max"] == round(19 / 85 * 100, 1)
    print("OK: test_costo_con_rango (costo {min:66,max:70}, margen {min:15,max:19})")


def test_todo_faltante():
    """Sin ningun numero declarado, todo debe reportar insumos_faltantes
    completos y valor/resultado None - nunca inventar ni asumir un default."""
    numeros = {}
    costo = c.costo_unitario_total(numeros)
    assert costo["valor"] is None
    assert set(costo["insumos_faltantes"]) == {"costo_materiales_unidad", "horas_por_unidad", "valor_hora"}

    reporte = c.calcular_reporte(numeros)
    assert reporte["costo_unitario"]["valor"] is None
    assert reporte["margen"]["valor"] is None
    assert reporte["punto_equilibrio"]["valor"] is None
    assert reporte["capacidad"]["unidades_mes"] is None
    assert reporte["escenarios"]["base"] is None
    assert reporte["ciclo_conversion_efectivo"]["valor"] is None
    for clave, resultado in reporte.items():
        assert resultado["insumos_faltantes"], f"{clave} deberia listar insumos_faltantes sin datos: {resultado}"
    print("OK: test_todo_faltante (ningun calculo inventa datos)")


def test_margen_no_positivo_no_da_equilibrio_falso():
    """Si el margen por unidad es cero o negativo (vende mas barato de lo que
    le cuesta), el punto de equilibrio NO debe reportar un numero (dividir
    por un margen <= 0 no tiene sentido de negocio) - debe venir con nota."""
    numeros = _numeros(
        costo_materiales_unidad=50, horas_por_unidad=1, valor_hora=10,
        precio_tentativo=40,  # precio (40) < costo (60): margen negativo
        costos_fijos_mensuales=500,
    )
    equilibrio = c.punto_equilibrio_unidades_mes(numeros)
    assert equilibrio["valor"] is None
    assert "nota" in equilibrio, equilibrio
    print("OK: test_margen_no_positivo_no_da_equilibrio_falso (nunca un punto de equilibrio absurdo)")


def main():
    test_escenario_macetas()
    test_costo_con_rango()
    test_todo_faltante()
    test_margen_no_positivo_no_da_equilibrio_falso()
    print("\nTODOS LOS TESTS DE calculadora.py PASARON.")


if __name__ == "__main__":
    main()
