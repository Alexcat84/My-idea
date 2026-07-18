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


def test_digital_founder_caso_real():
    """Motor v2.2, escenario mandatado del hotfix v2.2: el proyecto real del
    fundador (app de I Ching, tipo_oferta='digital'), con los numeros YA
    CORREGIDOS a su unidad real (fijos=$200/mes de infraestructura,
    variable por pack ~$0, precio $13/pack, meta 20 packs/mes) -- en vez
    de la version contaminada donde $200 se habia leido como materiales
    por pieza.

    Calculo manual:
      costo_unitario (rama digital: solo variable, sin horas/valor_hora)
                       = 0 (variable declarado)                     = 0
      margen           = precio 13 - costo 0                        = 13
      margen_pct       = 13 / 13 x 100                               = 100.0
      punto_equilibrio = ceil(fijos 200 / margen 13)
                       = ceil(15.3846...)                            = 16  (packs/mes)
      escenarios (meta 20, adopcion 50/100/200%):
        50%  -> 10 packs -> ingreso 130,  margen_total 130
        100% -> 20 packs -> ingreso 260,  margen_total 260
        200% -> 40 packs -> ingreso 520,  margen_total 520
    """
    COSTO_UNITARIO_ESPERADO = 0
    MARGEN_ESPERADO = 13
    MARGEN_PCT_ESPERADO = 100.0
    EQUILIBRIO_ESPERADO_PACKS = 16
    ESC_50_ESPERADO = {"unidades": 10, "ingreso": 130, "margen_total": 130}
    ESC_100_ESPERADO = {"unidades": 20, "ingreso": 260, "margen_total": 260}
    ESC_200_ESPERADO = {"unidades": 40, "ingreso": 520, "margen_total": 520}

    numeros = _numeros(
        costos_fijos_mensuales=200, costo_materiales_unidad=0,
        precio_tentativo=13, unidades_vendidas=20,
    )

    costo = c.costo_unitario_total(numeros, tipo_oferta="digital")
    assert costo["valor"] == COSTO_UNITARIO_ESPERADO, costo
    assert costo["insumos_faltantes"] == [], costo  # horas/valor_hora NO deben pedirse en digital

    margen = c.margen_unitario(numeros, tipo_oferta="digital")
    assert margen["valor"] == MARGEN_ESPERADO, margen
    assert margen["porcentaje"] == MARGEN_PCT_ESPERADO, margen

    equilibrio = c.punto_equilibrio_unidades_mes(numeros, tipo_oferta="digital")
    assert equilibrio["valor"] == EQUILIBRIO_ESPERADO_PACKS, equilibrio

    escenarios = c.escenarios_adopcion(numeros, tipo_oferta="digital")
    assert escenarios["50%"] == ESC_50_ESPERADO, escenarios["50%"]
    assert escenarios["100%"] == ESC_100_ESPERADO, escenarios["100%"]
    assert escenarios["200%"] == ESC_200_ESPERADO, escenarios["200%"]

    gigo = c.detectar_inconsistencia_gigo(numeros, tipo_oferta="digital")
    assert gigo["inconsistente"] is False, gigo

    print("OK: test_digital_founder_caso_real (costo=0, margen=13/100%, "
          "equilibrio=16 packs/mes, escenarios de adopcion 50/100/200% correctos)")


def test_digital_saas_sintetico():
    """Motor v2.2, prueba mandatada (8c): caso SaaS sintetico -- fijos $200,
    costo variable por usuario $0.50, precio $5, meta 100 usuarios.

    Calculo manual:
      costo_unitario   = 0.50 (variable, rama digital)                = 0.50
      margen           = precio 5 - costo 0.50                        = 4.50
      margen_pct       = 4.50 / 5 x 100                                = 90.0
      punto_equilibrio = ceil(200 / 4.50) = ceil(44.444...)            = 45  (usuarios/mes)
      escenarios (meta 100):
        50%  -> 50 usuarios  -> ingreso 250,  margen_total 225
        100% -> 100 usuarios -> ingreso 500,  margen_total 450
        200% -> 200 usuarios -> ingreso 1000, margen_total 900
    """
    MARGEN_ESPERADO = 4.5
    MARGEN_PCT_ESPERADO = 90.0
    EQUILIBRIO_ESPERADO_USUARIOS = 45
    ESC_50_ESPERADO = {"unidades": 50, "ingreso": 250, "margen_total": 225}
    ESC_100_ESPERADO = {"unidades": 100, "ingreso": 500, "margen_total": 450}
    ESC_200_ESPERADO = {"unidades": 200, "ingreso": 1000, "margen_total": 900}

    numeros = _numeros(
        costos_fijos_mensuales=200, costo_materiales_unidad=0.50,
        precio_tentativo=5, unidades_vendidas=100,
    )

    margen = c.margen_unitario(numeros, tipo_oferta="digital")
    assert margen["valor"] == MARGEN_ESPERADO, margen
    assert margen["porcentaje"] == MARGEN_PCT_ESPERADO, margen

    equilibrio = c.punto_equilibrio_unidades_mes(numeros, tipo_oferta="digital")
    assert equilibrio["valor"] == EQUILIBRIO_ESPERADO_USUARIOS, equilibrio

    escenarios = c.escenarios_adopcion(numeros, tipo_oferta="digital")
    assert escenarios["50%"] == ESC_50_ESPERADO, escenarios["50%"]
    assert escenarios["100%"] == ESC_100_ESPERADO, escenarios["100%"]
    assert escenarios["200%"] == ESC_200_ESPERADO, escenarios["200%"]

    print("OK: test_digital_saas_sintetico (margen=4.5/90%, equilibrio=45 usuarios/mes, "
          "escenarios de adopcion correctos)")


def test_gigo_detecta_unidad_equivocada():
    """Motor v2.2, guardian GIGO: el caso real que motivo la regla -- la
    mini-entrevista original (pre-v2.2) leyo el presupuesto mensual del
    fundador ($200) como costo de materiales POR UNIDAD, y 4 meses de
    desarrollo como 4 HORAS por unidad. El campo valor_hora derivado de la
    narracion original ($387 de margen negativo, -2976.9%) es $50.

    Calculo manual (numeros contaminados, ANTES de la correccion):
      costo_unitario = materiales 200 + horas 4 x valor_hora 50
                     = 200 + 200                                     = 400
      margen         = precio 13 - costo 400                         = -387
      margen_pct     = -387 / 13 x 100                                = -2976.923...  ~ -2976.9

    -2976.9% esta muy por debajo del umbral de -100%: el guardian debe
    marcar esto como inconsistente y el llamador (modo_reporte) NUNCA debe
    narrar 'no existe punto de equilibrio posible' con estos numeros -- el
    equilibrio real, una vez corregida la unidad, es 16 packs/mes (ver
    test_digital_founder_caso_real)."""
    MARGEN_PCT_ESPERADO = round(-387 / 13 * 100, 1)  # -2976.9
    assert MARGEN_PCT_ESPERADO == -2976.9, MARGEN_PCT_ESPERADO  # confirma el calculo manual

    numeros_contaminados = _numeros(
        costo_materiales_unidad=200, horas_por_unidad=4, valor_hora=50,
        precio_tentativo=13,
    )
    margen = c.margen_unitario(numeros_contaminados)
    assert margen["porcentaje"] == MARGEN_PCT_ESPERADO, margen

    gigo = c.detectar_inconsistencia_gigo(numeros_contaminados)
    assert gigo["inconsistente"] is True, gigo
    assert gigo["motivo"] is not None and "unidad equivocada" in gigo["motivo"], gigo

    # Guardrail inverso: un escenario sano (macetas, margen 20%) NUNCA debe
    # marcarse como inconsistente -- el guardian no puede ser tan agresivo
    # que desconfie de numeros normales.
    numeros_sanos = _numeros(
        costo_materiales_unidad=8, horas_por_unidad=4, valor_hora=15, precio_tentativo=85,
    )
    gigo_sano = c.detectar_inconsistencia_gigo(numeros_sanos)
    assert gigo_sano["inconsistente"] is False, gigo_sano

    print("OK: test_gigo_detecta_unidad_equivocada (margen=-2976.9% detectado como "
          "inconsistente; escenario sano de macetas NO dispara falso positivo)")


def test_palancas_inversas():
    """Palancas inversas del canon 14 (Tus Numeros). Espejo exacto de
    describe("palancas inversas") en web/lib/calculadora.test.ts.

    Calculo manual (regla de proceso: a mano ANTES del assert):

    Caso PERDIDA (velas de soya): costo total $42, precio $38.
      costo_unitario = 30 (materiales) + 2h x $6/h = 30 + 12             = 42
      margen         = 38 - 42                                           = -4  (-10.5%)
      precio_para_margen_objetivo(0.25) = 42 / (1 - 0.25) = 42 / 0.75    = 56.0
      margen_con_precio(56)             = 56 - 42 = 14 ; 14/56 x 100     = 25.0%
      costo_maximo_para_margen_objetivo(0.25) = 38 x 0.75               = 28.5
      margen_con_costo(28.5)            = 38 - 28.5 = 9.5 ; 9.5/38 x 100 = 25.0%
      unidades_para_ganancia_objetivo(0): margen -4 <= 0 -> None + nota

    Caso SANO (kits de huerto): costo $180, precio $350, fijos $1.200.
      costo_unitario = 100 + 4h x $20/h = 100 + 80                       = 180
      margen         = 350 - 180                                         = 170  (48.6%)
      unidades_para_ganancia_objetivo(0)    = ceil(1200/170) = ceil(7.06) = 8
      unidades_para_ganancia_objetivo(2880) = ceil(4080/170) = ceil(24)  = 24
      precio_para_margen_objetivo(0.55)  = 180 / 0.45                    = 400.0
      costo_maximo_para_margen_objetivo(0.55) = 350 x 0.45               = 157.5
    """
    velas = _numeros(costo_materiales_unidad=30, horas_por_unidad=2, valor_hora=6,
                     precio_tentativo=38, costos_fijos_mensuales=200)
    m_base = c.margen_unitario(velas)
    assert m_base["valor"] == -4 and m_base["porcentaje"] == -10.5, m_base
    assert c.precio_para_margen_objetivo(velas, 0.25)["valor"] == 56, c.precio_para_margen_objetivo(velas, 0.25)
    m56 = c.margen_con_precio(velas, 56)
    assert m56["valor"] == 14 and m56["porcentaje"] == 25.0, m56
    assert c.costo_maximo_para_margen_objetivo(velas, 0.25)["valor"] == 28.5, c.costo_maximo_para_margen_objetivo(velas, 0.25)
    m28 = c.margen_con_costo(velas, 28.5)
    assert m28["valor"] == 9.5 and m28["porcentaje"] == 25.0, m28
    u_perdida = c.unidades_para_ganancia_objetivo(velas, 0)
    assert u_perdida["valor"] is None and "no es positivo" in u_perdida["nota"], u_perdida

    kits = _numeros(costo_materiales_unidad=100, horas_por_unidad=4, valor_hora=20,
                    precio_tentativo=350, costos_fijos_mensuales=1200)
    assert c.margen_unitario(kits)["valor"] == 170, c.margen_unitario(kits)
    assert c.unidades_para_ganancia_objetivo(kits, 0)["valor"] == 8, c.unidades_para_ganancia_objetivo(kits, 0)
    assert c.unidades_para_ganancia_objetivo(kits, 2880)["valor"] == 24, c.unidades_para_ganancia_objetivo(kits, 2880)
    assert c.precio_para_margen_objetivo(kits, 0.55)["valor"] == 400, c.precio_para_margen_objetivo(kits, 0.55)
    assert c.costo_maximo_para_margen_objetivo(kits, 0.55)["valor"] == 157.5, c.costo_maximo_para_margen_objetivo(kits, 0.55)

    # RANGO: costo {min 42, max 52} con objetivo 25% (factor 0.75) ->
    #   precio {min 42/0.75 = 56, max 52/0.75 = 69.33}
    con_rango = _numeros(costo_materiales_unidad={"min": 30, "max": 40}, horas_por_unidad=2,
                         valor_hora=6, precio_tentativo=38)
    assert c.precio_para_margen_objetivo(con_rango, 0.25)["valor"] == {"min": 56, "max": 69.33}, \
        c.precio_para_margen_objetivo(con_rango, 0.25)

    # Objetivo >= 100% no da precio valido; sin costo no inventa margen.
    r_inalcanzable = c.precio_para_margen_objetivo(kits, 1)
    assert r_inalcanzable["valor"] is None and "infinito" in r_inalcanzable["nota"], r_inalcanzable
    sin_costo = _numeros(precio_tentativo=38)
    m_sin = c.margen_con_precio(sin_costo, 56)
    assert m_sin["valor"] is None and "costo_materiales_unidad" in m_sin["insumos_faltantes"], m_sin

    print("OK: test_palancas_inversas (perdida velas y sano kits del canon 14; "
          "precio/costo/margen/volumen inversos con paridad TS)")


def main():
    test_escenario_macetas()
    test_costo_con_rango()
    test_todo_faltante()
    test_margen_no_positivo_no_da_equilibrio_falso()
    test_digital_founder_caso_real()
    test_digital_saas_sintetico()
    test_gigo_detecta_unidad_equivocada()
    test_palancas_inversas()
    print("\nTODOS LOS TESTS DE calculadora.py PASARON.")


if __name__ == "__main__":
    main()
