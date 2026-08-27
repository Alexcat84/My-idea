# -*- coding: utf-8 -*-
"""VUELTA 82, TAREA 3: la relectura conjunta del discutible 1 de la vuelta
80, descubrir_necesidades_del_cliente -> traduccion_necesidades_cliente,
verificada contra dataset/nodos/*.json ANTES de decidir (encargo de la
vuelta 82). Las dos verificaciones que el encargo pedia:

1. El hijo cabe entero en el paso 6 de la madre ("Traducir las necesidades
   priorizadas al lenguaje tecnico de la organizacion", dataset/nodos/
   descubrir_necesidades_del_cliente.json), casi palabra por palabra el
   titulo y proposito entero del hijo ("Traduccion de Necesidades del
   Cliente al Lenguaje del Proveedor"). La madre conserva materia propia en
   los otros cinco pasos (recoleccion, listar, distinguir tipos de
   necesidad, investigar usos no previstos, analizar/priorizar), ninguno
   sobre traduccion. Los entregables (senal 9.6.2 mas fiable) confirman:
   la madre entrega "lista de necesidades... priorizadas Y traducidas" (dos
   productos), el hijo entrega exactamente el segundo ("Documento de
   necesidades del cliente traducidas a especificaciones tecnicas claras y
   medibles").
2. La vara de la cadena no muerde: el unico camino previo que la vara nueva
   encontro (SALIDA_V80_TRAMO6_FILTRO_P91_GUARDA_CADENA.txt, fila 27) sube
   por descubrir_necesidades_del_cliente -> design_for_six_sigma_dfss ->
   innovacion_tipo_ii -> juran_quality_by_design ->
   identificar_clientes_externos_e_internos -> customer_needs_spreadsheet
   -> traduccion_necesidades_cliente: NO es la cadena propia de la madre en
   su propio orden (customer_needs_spreadsheet no es paso de la madre). Y
   la razon que el reporte 80 dio para NO escribir se cae al medirla:
   dataset/nodos/identificar_clientes_externos_e_internos.json trae
   nodos_siguientes = [descubrir_necesidades_del_cliente,
   customer_needs_spreadsheet] (los DOS son hijos directos del mismo
   abuelo, no una cadena madre->hijo), y customer_needs_spreadsheet NO
   esta entre los 9 nodos_siguientes de descubrir_necesidades_del_cliente.
   El camino citado como "establecido de la familia" arranca en el abuelo
   y nunca pasa por esta madre.

Con las dos verificaciones a favor y la razon en contra refutada, se
escribe: descubrir_necesidades_del_cliente -> traduccion_necesidades_cliente,
en LAS DOS VISTAS a la vez, con chequeo de escalera.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

MADRE_ID = "descubrir_necesidades_del_cliente"
HIJO_ID = "traduccion_necesidades_cliente"


def cargar(node_id):
    p = NODOS / f"{node_id}.json"
    with open(p, encoding="utf-8") as f:
        return json.load(f), p


def main():
    madre, ruta_m = cargar(MADRE_ID)
    hijo, ruta_h = cargar(HIJO_ID)

    if HIJO_ID in (madre.get("nodos_siguientes") or []):
        print(f"YA ESTABA: {MADRE_ID} -> {HIJO_ID} ya en nodos_siguientes de la madre. No se toca nada.")
        return
    if HIJO_ID in (madre.get("nodos_previos") or []):
        print(f"ESCALERA ROTA: {HIJO_ID} ya esta en nodos_previos de la madre. No se escribe.")
        return
    if MADRE_ID in (hijo.get("nodos_siguientes") or []):
        print(f"ESCALERA ROTA: {MADRE_ID} ya esta en nodos_siguientes del hijo (invertida). No se escribe.")
        return

    madre.setdefault("nodos_siguientes", [])
    madre["nodos_siguientes"].append(HIJO_ID)
    hijo.setdefault("nodos_previos", [])
    hijo["nodos_previos"].append(MADRE_ID)

    with open(ruta_m, "w", encoding="utf-8") as f:
        json.dump(madre, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(ruta_h, "w", encoding="utf-8") as f:
        json.dump(hijo, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"ARISTA ESCRITA (nodos_siguientes Y nodos_previos): {MADRE_ID} -> {HIJO_ID}")


if __name__ == "__main__":
    main()
