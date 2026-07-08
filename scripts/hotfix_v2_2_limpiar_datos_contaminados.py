# -*- coding: utf-8 -*-
"""Motor v2.2, item 9 del prompt de Fable: limpieza de datos contaminados.

La mini-entrevista pre-v2.2 (molde unico "producto fisico") le pregunto al
fundador de la app de I Ching (proyecto 05868ec6-dd9b-4e5c-ab05-d81b3888e553)
"materiales por pieza" y "horas por pieza" para una oferta digital que no
tiene ninguno de los dos conceptos. El usuario, en sus propias palabras,
dijo que esos campos NO aplicaban -- pero la mini-entrevista (sin guardian
GIGO todavia) igual extrajo un numero de la respuesta:

  costo_materiales_unidad = 200  (texto real: "mi modelo no usa costo por
                                   piezas, es una app, y tengo un
                                   presupuesto de gasto mensual de unos
                                   $200 fijos" -- es presupuesto MENSUAL,
                                   no costo por pieza)
  horas_por_unidad        = 4    (texto real: "me tomas varios meses, pero
                                   no es pieza. me toma al menos 4 meses
                                   el desarrollo" -- son MESES de
                                   desarrollo, no horas por pieza)
  valor_hora               = 50   (solo tiene sentido junto a horas_por_
                                   unidad, que ya es invalido)

Dos campos SI son correctos y se conservan tal cual (el usuario los
declaro sin ambiguedad y encajan igual de bien en el molde digital):
  precio_tentativo        = 13   ("son packs los que vendo por tier... En
                                   promedio cuesta unos $13" -- precio real
                                   por pack)
  costos_fijos_mensuales  = 200  ("si $200" -- coincide con el presupuesto
                                   mensual real, ya capturado correctamente
                                   aqui)

Este script mueve los 3 campos contaminados a numeros_proyecto -> ninguno
(se eliminan de ahi) y los conserva en numeros_descartados con el motivo,
para que --reporte v2.2 los vuelva a preguntar bajo el molde digital
correcto, sin perder la trazabilidad de que existieron y por que se
invalidaron.

Requiere que la migracion my_idea_007_tipo_oferta.sql ya este aplicada
(agrega la columna numeros_descartados)."""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "engine"))
import db

PROJECT_ID = "05868ec6-dd9b-4e5c-ab05-d81b3888e553"
CAMPOS_CONTAMINADOS = {
    "costo_materiales_unidad": "presupuesto mensual ($200) capturado como costo por pieza; el modelo real es digital, sin costo por pieza",
    "horas_por_unidad": "meses de desarrollo (4) capturados como horas por pieza; no aplica a una oferta digital",
    "valor_hora": "solo tenia sentido junto a horas_por_unidad, que ya es invalido en este contexto",
}


def main():
    proyecto = db.obtener_proyecto(PROJECT_ID)
    if proyecto is None:
        print(f"ERROR: no existe el proyecto {PROJECT_ID}")
        sys.exit(1)

    numeros = dict(proyecto.get("numeros_proyecto") or {})
    descartados = dict(proyecto.get("numeros_descartados") or {})

    movidos = []
    for campo, motivo in CAMPOS_CONTAMINADOS.items():
        if campo in numeros:
            entry = dict(numeros.pop(campo))
            entry["motivo_descarte"] = motivo
            entry["descartado_en"] = datetime.now(timezone.utc).isoformat()
            descartados[campo] = entry
            movidos.append(campo)

    print(f"Campos movidos a numeros_descartados: {movidos}")
    print(f"Campos que quedan en numeros_proyecto (correctos, se conservan): {sorted(numeros.keys())}")

    db.actualizar_proyecto(PROJECT_ID, numeros_proyecto=numeros, numeros_descartados=descartados,
                            tipo_oferta="digital", unidad_venta="pack")

    verificacion = db.obtener_proyecto(PROJECT_ID)
    print("\n--- Verificacion post-limpieza ---")
    print("numeros_proyecto:", json.dumps(verificacion.get("numeros_proyecto"), indent=2, ensure_ascii=False))
    print("tipo_oferta:", verificacion.get("tipo_oferta"), "| unidad_venta:", verificacion.get("unidad_venta"))


if __name__ == "__main__":
    main()
