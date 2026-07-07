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
    en $15, vendería a $85, capacidad 5/semana, sin costos fijos declarados.

    REGLA DE PROCESO (hotfix v2.1.1, tras el bug de ingreso_perdido_estimado
    calculando con margen en vez de precio): el escenario canonico se
    calcula A MANO aqui abajo, en comentario, ANTES de escribir los
    asserts - y los asserts se escriben contra ESE calculo manual, no
    contra lo que la funcion ya devuelve. Un assert que solo repite la
    salida de la funcion no puede detectar un bug en esa misma funcion.

    Calculo manual:
      costo_unitario   = 8 (materiales) + 4h x $15/h = 8 + 60         = 68
      margen           = precio 85 - costo 68                        = 17
      margen_pct       = 17 / 85 x 100                                = 20.0
      unidades_mes     = capacidad 5/semana x 4 semanas/mes            = 20
      ingreso_mes      = 20 unidades x $85                           = 1700
      margen_mes       = 20 unidades x $17                            = 340
      pesimista (50%)  = 10 unidades -> ingreso 850, margen 170
      base (100%)      = 20 unidades -> ingreso 1700, margen 340
      sobredemanda:
        demanda_estimada (150%)    = 20 x 1.5                         = 30
        unidades_producibles       = 20 (tope real de capacidad)
        unidades_no_atendidas      = 30 - 20                          = 10
        ingreso_perdido_estimado   = 10 unidades x PRECIO $85         = 850  (facturacion que no ocurre)
        margen_perdido_estimado    = 10 unidades x MARGEN $17         = 170  (ganancia que no llega)
    """
    COSTO_UNITARIO_ESPERADO = 68
    MARGEN_ESPERADO = 17
    MARGEN_PCT_ESPERADO = 20.0
    UNIDADES_MES_ESPERADO = 20
    INGRESO_MES_ESPERADO = 1700
    MARGEN_MES_ESPERADO = 340
    PESIMISTA_ESPERADO = {"unidades_mes": 10, "ingreso": 850, "margen_mensual": 170}
    BASE_ESPERADO = {"unidades_mes": 20, "ingreso": 1700, "margen_mensual": 340}
    SOBREDEMANDA_DEMANDA_ESTIMADA_ESPERADA = 30
    SOBREDEMANDA_UNIDADES_NO_ATENDIDAS_ESPERADO = 10
    SOBREDEMANDA_INGRESO_PERDIDO_ESPERADO = 850  # unidades_no_atendidas x PRECIO, no margen
    SOBREDEMANDA_MARGEN_PERDIDO_ESPERADO = 170   # unidades_no_atendidas x MARGEN, no precio

    numeros = _numeros(
        costo_materiales_unidad=8, horas_por_unidad=4, valor_hora=15,
        precio_tentativo=85, capacidad_semanal=5,
    )

    costo = c.costo_unitario_total(numeros)
    assert costo["valor"] == COSTO_UNITARIO_ESPERADO, costo
    assert costo["insumos_faltantes"] == []

    margen = c.margen_unitario(numeros)
    assert margen["valor"] == MARGEN_ESPERADO, margen
    assert margen["porcentaje"] == MARGEN_PCT_ESPERADO, margen

    equilibrio = c.punto_equilibrio_unidades_mes(numeros)
    assert equilibrio["valor"] is None
    assert equilibrio["insumos_faltantes"] == ["costos_fijos_mensuales"], equilibrio

    capacidad = c.techo_ingreso_capacidad(numeros)
    assert capacidad["unidades_mes"] == UNIDADES_MES_ESPERADO, capacidad
    assert capacidad["ingreso"] == INGRESO_MES_ESPERADO, capacidad
    assert capacidad["margen_mensual"] == MARGEN_MES_ESPERADO, capacidad

    escenarios = c.escenarios_capacidad(numeros)
    assert escenarios["pesimista"] == PESIMISTA_ESPERADO, escenarios["pesimista"]
    assert escenarios["base"] == BASE_ESPERADO, escenarios["base"]
    sd = escenarios["sobredemanda"]
    assert sd["demanda_estimada"] == SOBREDEMANDA_DEMANDA_ESTIMADA_ESPERADA, sd
    assert sd["unidades_producibles"] == UNIDADES_MES_ESPERADO, sd
    assert sd["unidades_no_atendidas"] == SOBREDEMANDA_UNIDADES_NO_ATENDIDAS_ESPERADO, sd
    assert sd["ingreso_perdido_estimado"] == SOBREDEMANDA_INGRESO_PERDIDO_ESPERADO, sd
    assert sd["margen_perdido_estimado"] == SOBREDEMANDA_MARGEN_PERDIDO_ESPERADO, sd
    # Guardrail contra el bug exacto del hotfix: los dos campos de perdida
    # nunca deben ser iguales entre si salvo coincidencia numerica rara
    # (precio != margen en este escenario, 85 != 17), asi que si algun dia
    # vuelven a calcularse con la misma formula por error, esto lo atrapa.
    assert sd["ingreso_perdido_estimado"] != sd["margen_perdido_estimado"]

    cce = c.ciclo_conversion_efectivo(numeros)
    assert cce["valor"] is None
    assert set(cce["insumos_faltantes"]) == set(c.CAMPOS_CICLO_CONVERSION_EFECTIVO)

    print("OK: test_escenario_macetas (costo=68, margen=17/20%, techo=20u/$1700/$340, "
          "sobredemanda ingreso=850/margen=170 correctamente distinguidos, "
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
