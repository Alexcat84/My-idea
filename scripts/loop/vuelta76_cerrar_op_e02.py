"""VUELTA 76, TAREA 2.2: cierra OP-E-02 con DECLARACION, adjudicado por el
auditor en el acta de la vuelta 75 seccion 4.1 ("OP-E-02 PUEDE CERRAR. No pide
fundador, no pide doctrina nueva y no escribe ni una arista: cierra con
declaracion, que es lo que su propia ficha pide").

No se toca ni la adjudicacion ni la nota vieja: se ANADE el registro de
cierre al final de la nota, con la fecha de esta vuelta, y el estado pasa de
LISTA a HECHA porque la operacion ya esta resuelta por el criterio de la
fase (MODO DE CIERRE: cero reparaciones de nodos, esto es lectura y
declaracion, ninguna arista se escribe).
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
RUTA = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"

REGISTRO_CIERRE = (
    " CIERRE POR DECLARACION (26 ago 2026, vuelta 76, adjudicado por el "
    "auditor, acta de la vuelta 75 seccion 4.1). Medido HOY, corrida propia "
    "de scripts/loop/vuelta75_op_e02_racimos.py: de los 32 racimos censados "
    "en docs/RACIMOS_MIEMBROS.jsonl, los 171 miembros siguen VIVOS (0 "
    "muertos/fundidos desde el censo) y 0 racimos tienen miembro ajeno tras "
    "normalizar NUCLEO contra core. EL SUELTO comprender_alineacion_etica_ia "
    "va a MESA sin arista: su racimo esta partido en dos bloques y no tiene "
    "centro, tercer supuesto de la regla del 11 ago 2026. LOS TRES "
    "EJEMPLARES DE RACIMO CON MIEMBRO AJENO, cada uno por su salida del "
    "remedio (o la nomina se depura, o el racimo se declara transversal): "
    "value_stream_mapping_ambiental y analisis_flujo_de_valor YA RESUELTOS "
    "por la segunda salida (su racimo Mapeo del flujo de valor tiene "
    "dominio_censado literal quality + environmental + nucleo, que ES la "
    "declaracion transversal explicita); desarrollo_value_proposition_usp "
    "por la primera salida, la nomina se depura (informe seccion 33.2: CAE, "
    "y ni siquiera es del dominio, CERO SOLAPE; 33.3 lo llama defecto de "
    "NOMINA, no de lectura). Con eso la ficha tiene destino en sus tres "
    "piezas y la operacion queda HECHA por el criterio de la fase: no "
    "escribio ni una arista, es lectura y declaracion."
)


def main():
    lineas = RUTA.read_text(encoding="utf-8").splitlines()
    tocada = False
    for i, linea in enumerate(lineas):
        if not linea.strip():
            continue
        op = json.loads(linea)
        if op["id_op"] == "OP-E-02":
            if REGISTRO_CIERRE not in op["nota"]:
                op["nota"] = op["nota"] + REGISTRO_CIERRE
                op["estado"] = "HECHA"
                op["fecha_corte"] = "2026-08-26"
                lineas[i] = json.dumps(op, ensure_ascii=False)
                tocada = True
    RUTA.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print("OP-E-02 cerrada con declaracion" if tocada else "NADA QUE TOCAR (ya cerrada)")


if __name__ == "__main__":
    main()
