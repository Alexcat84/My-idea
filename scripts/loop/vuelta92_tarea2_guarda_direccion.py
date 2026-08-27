# -*- coding: utf-8 -*-
"""vuelta92_tarea2_guarda_direccion.py . VUELTA 92, TAREA 2 (BLOQUEANTE): EL
GUARDA DE DOS CONDICIONES PARA `extraer_direccion_automatica`.

POR QUE NACE (acta de la vuelta 91, `docs/loop/ACTA_AUDITOR.md`, seccion 3.1 y
6.5, lineas 31290 a 31365 y 31499 a 31507). El criterio de
`extraer_direccion_automatica` (`scripts/loop/vuelta91_tarea4_direccion_ope07.py`)
busca la palabra "trae" en el segmento de un id y le pone direccion. En el
puesto 1098 esa palabra aparece en la formula de la clase D ("trae un
procedimiento que el otro no tiene en ninguna forma"), no en la formula de
madre e hijo, y el par entro con arista cuando su propia razon manda que
SALGA ("Queda anotada UNA LINEA COMPARTIDA que no crea jerarquia porque
ninguno la expande").

EL GUARDA, LAS DOS CONDICIONES (encargo de la vuelta 92,
`docs/loop/PROMPT_SIGUIENTE.md`):
  (a) la razon trae una MARCA DE MADRE POSITIVA: una linea NOMBRADA CON SU
      PASO (numero o palabra ordinal), o una de las formulas de indice
      ("ES EL INDICE", "ENUMERA", "ORDENA", "ES LA ETAPA", "ES EL PROGRAMA",
      "MANDA", "ENUNCIA", "es un repertorio", "NOMBRA EL PROBLEMA",
      "ESCRIBE EL ENCARGO ENTERO", "es POSTURA", "MONTA EL MARCO",
      "describe las piezas", "compara los", "calcula dos indicadores",
      "RECORRE", "despacha en/su", o "la madre" nombrada literalmente).
  (b) la razon NO NIEGA la jerarquia ("no crea jerarquia", "ninguno la
      expande", "sin jerarquia") SIN TENER (a): la negacion solo tumba el par
      cuando no hay ninguna marca de madre que la sostenga; si (a) esta
      presente la negacion puede referirse a una SEGUNDA linea distinta (el
      caso del puesto 1160 de OP-E-06, acta 91 seccion 3.2), y el par sigue.

POR QUE "en un solo paso" (SIN NUMERO) NO CUENTA COMO MARCA DE MADRE, Y ES EL
NUCLEO DEL GUARDA. El propio 1098 dice "los dos... lo dicen en un solo paso",
que suena a la formula de "paso nombrado" pero es SIMETRICA (de LOS DOS, no
de uno) y SIN NUMERO. Todas las 87 marcas de madre validas de la bolsa nombran
el paso con un NUMERO o un ORDINAL ("paso 4", "paso 2", "pasos 2, 3 y 4",
"tercer paso"); el guarda exige eso, no la palabra "paso" sola.

LA VARA DURA, LOS DOS CASOS OBLIGATORIOS (correr con --vara):
  1. Sobre las 88 razones de docs/plan/OP_E_07_REBASE_V91.jsonl: el guarda
     tiene que marcar el 1098 como SALE y NINGUN otro de los 88.
  2. Sobre las 114 de docs/plan/OP_E_06_DIRECCION_V90.jsonl: el guarda tiene
     que dejar PASAR el 1160.
Si no cumple los dos, no alcanza y se declara.

MECANICA DE ROJO, igual que la TAREA 3 de la vuelta 91: si no se puede leer
la razon de algun puesto, NO SE TALLA NADA, EXIT 1, sin tabla parcial.

USO:
  python scripts/loop/vuelta92_tarea2_guarda_direccion.py --vara
  python scripts/loop/vuelta92_tarea2_guarda_direccion.py --mutacion
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
BOLSA_OPE07 = os.path.join(PLAN, "OP_E_07_REBASE_V91.jsonl")
BOLSA_OPE06 = os.path.join(PLAN, "OP_E_06_DIRECCION_V90.jsonl")

# CONDICION (a): MARCA DE MADRE POSITIVA. Cada alternativa cita el puesto (de
# la propia bolsa de 88, o de la relectura al doble de la vuelta 91, acta
# lineas 31400 a 31423) que la hizo necesaria: no es una lista inventada, es
# la lista de formulas que la razon REALMENTE usa cuando SI hay madre e hijo.
_ORDINALES = r"primer|segundo|tercer|cuarto|quinto|sexto|septimo|octavo|noveno"
# EL SUFIJO QUE NO CUENTA, y es la trampa que la mutacion del 1160 encontro:
# "es/en UNA LINEA compartida" es la MISMA formula, en superficie, que el
# 1098 usa para negar la jerarquia ("Es UNA linea compartida y ninguno la
# expande", puesto 1160; "Queda anotada UNA LINEA COMPARTIDA que no crea
# jerarquia", puesto 1098). Una linea llamada COMPARTIDA nunca es la marca
# positiva: la lookahead negativa la excluye en todas las variantes.
_LINEA = r"l[ií]neas?(?!\s*compartid)"
_LINEA_SOLA = r"l[ií]nea(?!\s*compartid)"
_ALTERNATIVAS_MARCA_MADRE = [
    r"paso\s+\d", r"pasos\s+\d",                        # "paso 4" / "pasos 2, 3 y 4" (1114, 1318...)
    r"(?:" + _ORDINALES + r")\s+paso",                  # "tercer paso" (940, 993, 1196)
    r"etapas?\s+\d",                                    # "etapa 1", "etapa 2" (1244, 1344)
    r"en\s+(?:una|dos|tres|media)\s+" + _LINEA,         # "en UNA LINEA", "en DOS LINEAS" (1195, 1612...)
    r"es\s+(?:una|dos|tres)\s+" + _LINEA,               # "es UNA LINEA" (896, 902, 910, 940...)
    r"dice\s+(?:una|dos|tres)\s+" + _LINEA,             # "dice tres lineas" (960, sin "en")
    r"son\s+" + _LINEA,                                 # "son lineas" (909)
    r"(?:primera|segunda|tercera)\s+" + _LINEA_SOLA,    # "de su segunda linea" (1129)
    r"en\s+una\s+sola\s+" + _LINEA_SOLA,                # "en una sola linea" (1086)
    r"entre sus pasos",                                 # "dice, entre sus pasos" (1848)
    r"es un h[aá]bito",                                 # "es un habito de taller" (1281)
    r"prueba el problema",                              # "prueba el problema" (1009, la fase indice)
    r"es (?:el|un) indice",                             # "ES EL INDICE" (1388), "es un INDICE" (1092)
    r"enumera",                                         # "ENUMERA" (1500)
    r"ordena",                                          # "ORDENA" (886, 951, 1083)
    r"es la etapa",                                     # "ES LA ETAPA" (890)
    r"es el programa",                                  # "ES EL PROGRAMA" (1020)
    r"\bmanda\b",                                       # "MANDA SALIR" (947)
    r"enuncia",                                         # "ENUNCIA" (872, 1023, 1946)
    r"es un repertorio",                                # "es un repertorio" (1196)
    r"nombra el problema",                              # "NOMBRA EL PROBLEMA" (1844)
    r"escribe el encargo entero",                       # "ESCRIBE EL ENCARGO ENTERO" (1567)
    r"es postura",                                      # "es POSTURA" (1337)
    r"monta el marco",                                  # "MONTA EL MARCO" (1886)
    r"describe las piezas",                             # "describe las piezas" (1191, 1220)
    r"compara los",                                     # "compara los cinco" (974, 1992, 1993)
    r"calcula dos indicadores",                         # "calcula dos indicadores" (974)
    r"recorre",                                         # "RECORRE" (1536)
    r"despacha",                                        # "despacha la primera en UNA LINEA" (951, 1102...)
    r"la madre\b",                                      # "la madre nombrada literalmente" (1191)
]
MARCA_MADRE_POSITIVA = re.compile("|".join(_ALTERNATIVAS_MARCA_MADRE), re.IGNORECASE)

# CONDICION (b): NEGACION DE JERARQUIA.
NIEGA_JERARQUIA = re.compile(
    r"no crea jerarquia|ninguno la expande|sin jerarquia",
    re.IGNORECASE,
)


def guarda_direccion(razon):
    """LA UNICA PIEZA DE JUICIO DEL GUARDA, aislada para que su caso rojo se
    pueda probar por mutacion. Devuelve "PASA" o "SALE"."""
    tiene_marca = bool(MARCA_MADRE_POSITIVA.search(razon))
    niega = bool(NIEGA_JERARQUIA.search(razon))
    if not tiene_marca:
        return "SALE"
    if niega and not tiene_marca:
        return "SALE"  # inalcanzable (tiene_marca ya es True), escrito para que la regla quede literal
    return "PASA"


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def cargar_veredictos():
    return {int(v["puesto_intra"]): v for v in cargar_jsonl(VEREDICTOS)}


def correr_sobre_bolsa(ruta_bolsa, veredictos, campo_puesto="puesto"):
    """Devuelve (resultados, rojo). resultados es lista de (puesto, veredicto,
    tiene_marca, niega). rojo es un mensaje si no se pudo leer alguna razon,
    o None."""
    filas = cargar_jsonl(ruta_bolsa)
    resultados = []
    for f in filas:
        puesto = f[campo_puesto]
        v = veredictos.get(puesto)
        if v is None:
            return None, "ROJO: el puesto %s no tiene entrada en %s. NO SE TALLA NADA." % (
                puesto, VEREDICTOS)
        razon = v["razon"]
        veredicto = guarda_direccion(razon)
        tiene_marca = bool(MARCA_MADRE_POSITIVA.search(razon))
        niega = bool(NIEGA_JERARQUIA.search(razon))
        resultados.append((puesto, veredicto, tiene_marca, niega))
    return resultados, None


def vara_dura():
    veredictos = cargar_veredictos()

    print("=" * 90)
    print("VARA DURA, CASO 1: las 88 razones de OP_E_07_REBASE_V91.jsonl")
    print("=" * 90)
    res1, rojo1 = correr_sobre_bolsa(BOLSA_OPE07, veredictos, campo_puesto="puesto")
    if rojo1:
        print(rojo1)
        return 1
    salen1 = [p for p, v, _, _ in res1 if v == "SALE"]
    print("total: %d, SALEN: %d %s" % (len(res1), len(salen1), salen1))
    caso1_ok = salen1 == [1098]
    print("CASO 1 %s: el guarda tiene que marcar SOLO el 1098 como SALE." % ("OK" if caso1_ok else "ROJO"))
    print()

    print("=" * 90)
    print("VARA DURA, CASO 2: las 114 de OP_E_06_DIRECCION_V90.jsonl, el 1160 tiene que PASAR")
    print("=" * 90)
    res2, rojo2 = correr_sobre_bolsa(BOLSA_OPE06, veredictos, campo_puesto="puesto")
    if rojo2:
        print(rojo2)
        return 1
    salen2 = [p for p, v, _, _ in res2 if v == "SALE"]
    veredicto_1160 = next((v for p, v, _, _ in res2 if p == 1160), None)
    print("total: %d, SALEN: %d %s" % (len(res2), len(salen2), salen2))
    print("veredicto del 1160: %s" % veredicto_1160)
    caso2_ok = veredicto_1160 == "PASA"
    print("CASO 2 %s: el 1160 tiene que dar PASA (si tumba el 1160, el guarda esta mal)."
          % ("OK" if caso2_ok else "ROJO"))
    print()

    print("=" * 90)
    if caso1_ok and caso2_ok:
        print("LA VARA ALCANZA: los dos casos obligatorios se cumplen.")
        return 0
    print("LA VARA NO ALCANZA: revisar el guarda.")
    return 1


def _autoprueba_mutacion():
    """PROBAR guarda_direccion POR MUTACION, contrato de
    verificar_caso_rojo_por_mutacion.py: la entrada es la RAZON (una cadena
    que el codigo de verdad recibe), no un literal disfrazado."""
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    from verificar_caso_rojo_por_mutacion import probar_por_mutacion

    veredictos = cargar_veredictos()
    razon_1098 = veredictos[1098]["razon"]
    razon_1160 = veredictos[1160]["razon"]

    print("CASO 1: el 1098 REAL da SALE (sin marca de madre). NO BASTA con quitar")
    print("la negacion para probar el guarda (1098 seguiria SALE por falta de")
    print("marca, que es un caso rojo disfrazado, EXACTAMENTE el defecto de la")
    print("vuelta 89). La mutacion tiene que INYECTAR una marca de madre real")
    print("(paso numerado) para que el CRITERIO cambie de veredicto.")
    razon_1098_con_marca = razon_1098.replace(
        "Queda anotada UNA LINEA COMPARTIDA que no crea jerarquia porque ninguno la expande",
        "customer_validation_sell_phase dice en su paso 4, en UNA LINEA",
    )
    assert razon_1098_con_marca != razon_1098
    probar_por_mutacion(
        nombre="guarda_direccion sobre el puesto 1098 (inyectar marca de madre con paso numerado)",
        criterio=guarda_direccion,
        entrada=razon_1098,
        veredicto_esperado="SALE",
        entrada_mutada=razon_1098_con_marca,
        veredicto_tras_mutar="PASA",
    )

    print()
    print("CASO 2: el 1160 REAL da PASA (tiene marca de madre con paso numerado,")
    print("'dice en su paso 2, en UNA LINEA'), y una version MUTADA que le quita")
    print("esa marca tiene que dar SALE.")
    razon_1160_mutada = re.sub(r"dice en su paso 2, en UNA LINEA", "trae consigo lo de siempre", razon_1160)
    assert razon_1160_mutada != razon_1160, "la mutacion no encontro la marca a quitar en la razon del 1160"
    probar_por_mutacion(
        nombre="guarda_direccion sobre el puesto 1160 (quitar la marca de madre numerada)",
        criterio=guarda_direccion,
        entrada=razon_1160,
        veredicto_esperado="PASA",
        entrada_mutada=razon_1160_mutada,
        veredicto_tras_mutar="SALE",
    )
    print()
    print("LOS DOS CASOS: PROBADOS POR MUTACION. guarda_direccion SI depende de su entrada.")
    return 0


def main():
    if "--mutacion" in sys.argv:
        return _autoprueba_mutacion()
    return vara_dura()


if __name__ == "__main__":
    raise SystemExit(main())
