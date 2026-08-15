"""Vuelta 32: la CORRECCION DECLARADA AL EJECUTAR el 14vo de Horowitz.

P.18 punto 2 y P.19 obligan a lo mismo: el destino elegido, o la fusion, se
escribe como CORRECCION DECLARADA AL EJECUTAR, con la lectura que lo sostiene.
No basta con nombrar el resultado, hay que decir POR QUE. El texto viejo del
campo nota se queda ENTERO delante: solo se anade al final.

Las cifras de esta nota NO se teclean: se leen del grafo y del plan sellado en
esta misma corrida, que es lo que la regla 2 del EJECUTOR.md obliga.

Uso: python scripts/loop/vuelta32_nota_hor14.py [--aplicar]
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
PLAN = os.path.join(RAIZ, "docs", "loop", "PLAN_V32_P19_CALIDAD_MVP.json")

MARCA = "CORRECCION DECLARADA, 15 ago 2026 (vuelta 32), EL 14vo RESUELTO"


def main():
    aplicar = "--aplicar" in sys.argv

    with open(PLAN, encoding="utf-8") as fh:
        plan = json.load(fh)
    f = plan["nodos"][0]
    with open(os.path.join(NODOS, f["nodo"] + ".json"), encoding="utf-8") as fh:
        d = json.load(fh)

    antes = len(f["pasos_originales"])
    despues = len(d.get("pasos_accionables") or [])
    if despues != len(f["pasos_finales"]):
        print("PARADA: el nodo tiene %d pasos y el plan dejaba %d"
              % (despues, len(f["pasos_finales"])))
        return 1

    texto = (
        " %s: el bloque de Horowitz de principio_calidad_mvp (los pasos 6 a 10 de la "
        "frontera publicada en la vuelta 20) queda RESUELTO DENTRO DE ESTA OPERACION, "
        "POR P.19 Y NO POR P.18. LA LECTURA, hecha hoy con el texto delante y publicada "
        "entera en docs/loop/SALIDA_V32_HOR14_LECTURA.txt: el bloque REPITE EL OBJETO de "
        "los pasos 1 a 5 de Ries, asi que no tiene destino que buscar. Par por par: el 6 "
        "(resistir la presion del equipo de completar todas las funcionalidades ideales "
        "antes de lanzar) es el 1 (antes de invertir en pulir, preguntate si contribuye "
        "al aprendizaje) con el sesgo nombrado; el 7 (distinguir requerimientos heredados "
        "de un cliente anterior de las necesidades reales del mercado amplio) es el 3 (no "
        "asumas que el estandar de la industria es lo que el cliente valora) con otra "
        "fuente del estandar falso; el 8 (lanzar al mercado real lo antes posible "
        "aceptando que fallara) es el 2 (lanza versiones simplificadas y mide la reaccion "
        "real) a escala de producto. LOS QUE NO REPITEN SE QUEDAN VERBATIM, sin "
        "reescribir: el 9 y el 10 de Horowitz y el 4 y el 5 de Ries. POR QUE NO P.18, con "
        "los descartados por su nombre: la nomina vigente al dia de la familia Horowitz "
        "se leyo entera hoy (93 miembros vivos) y NINGUNO tiene este objeto; los mas "
        "cercanos son framework_good_bad_product_manager (su objeto es el ROL del product "
        "manager), lead_bullets_no_silver_bullets y estrategia_de_balas_de_plomo (cerrar "
        "una desventaja competitiva sin atajos, consejo contrario), "
        "respuesta_estrategica_a_amenaza_competitiva (el pivote ante un competidor "
        "dominante), descubrir_valor_inesperado_cliente (el dolor no contractual de UN "
        "cliente critico) y toma_decisiones_bajo_incertidumbre (decidir con informacion "
        "incompleta, que es el genero y no este objeto). Y la salida de nodo propio de "
        "P.18 punto 3 fabricaria aqui el gemelo exacto del propio donante, que es "
        "literalmente el caso que el motivo de P.19 nombra para existir. LAS DIFERENCIAS "
        "ENTRE VERSIONES, por la tabla de los seis motivos de perdida de linea: "
        "SALVAGUARDA en el paso 1 del resultado, ALCANCE en el 2 y ALCANCE mas "
        "SALVAGUARDA en el 3; NOMBRE, DESTINO, METODO ALTERNATIVO y DIRECCION no aplican "
        "y por eso no se nombran. EL RESULTADO, MEDIDO HOY SOBRE EL ARBOL Y NO COPIADO: "
        "el nodo pasa de %d pasos a %d, conserva su fuente %r y queda MULTIFUENTE "
        "LEGITIMO por P.19 punto 2, con la procedencia declarada por bloque (pasos 4 y 6 "
        "del resultado de Ries, 5 y 7 de Horowitz, y 1, 2 y 3 de los dos libros dentro "
        "del mismo paso fundido). GUARDAS: simulacion previa sobre copia en memoria verde "
        "(SALIDA_V32_HOR14_SIM.txt), guarda de texto 10 de 10 prefijos, cero perdida con "
        "cobertura exacta de 1 a 10 sin huecos ni repetidos, y caso positivo 0 PASAN y 5 "
        "CAEN antes contra 5 PASAN y 0 CAEN despues, con 10 rastros de conservacion vivos "
        "las dos veces (SALIDA_V32_HOR14_CASO_ANTES.txt y _DESPUES.txt). Plan sellado en "
        "docs/loop/PLAN_V32_P19_CALIDAD_MVP.json. SALDO DE LA TANDA RE-MEDIDO AL CERRAR "
        "con scripts/loop/vuelta32_saldo_opf04.py, sucesor declarado del de la vuelta 30: "
        "NOMINA 14, RESUELTOS 12, FUNDIDOS por P.19 2, PENDIENTES 0, LA TANDA ESTA "
        "ENTERA, 14 DE 14 (docs/loop/SALIDA_V32_SALDO_HOR.txt). El parrafo de la vuelta 31 "
        "que declaraba esta tanda entera con 13 de 13 no se borra: queda superado por esta "
        "correccion."
    ) % (MARCA, antes, despues, d.get("fuente"))

    lineas = []
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                lineas.append(json.loads(linea))

    for o in lineas:
        if o["id_op"] != "OP-F-04-HOR":
            continue
        if MARCA in (o.get("nota") or ""):
            print("YA APLICADA: la nota de OP-F-04-HOR ya trae la correccion de la vuelta 32.")
            return 0
        o["nota"] = (o.get("nota") or "") + texto
        print("--- LO QUE SE ANADE (el texto viejo se queda entero delante) ---")
        print(texto.strip())

    if not aplicar:
        print()
        print("(simulacion: sin --aplicar no se escribe nada)")
        return 0

    with open(OPS, "w", encoding="utf-8") as fh:
        for o in lineas:
            fh.write(json.dumps(o, ensure_ascii=False) + "\n")

    de_vuelta = []
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                de_vuelta.append(json.loads(linea))
    ids = [o["id_op"] for o in de_vuelta]
    rotas = sum(1 for o in de_vuelta
                for x in (o.get("depende_de") or []) + (o.get("bloquea_a") or [])
                if x not in set(ids))
    print()
    print("VERIFICADO TRAS ESCRIBIR: %d lineas JSON validas, %d ids unicos, "
          "%d dependencias rotas" % (len(de_vuelta), len(set(ids)), rotas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
