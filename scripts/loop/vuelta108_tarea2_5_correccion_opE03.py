# -*- coding: utf-8 -*-
"""vuelta108_tarea2_5_correccion_opE03.py . TAREA 2.5 de la vuelta 108:
correccion declarada del 74/74 mal publicado en el cierre de la vuelta 107,
anadida a docs/plan/OPERACIONES.jsonl (nota de OP-E-03). El texto viejo NO SE
BORRA. La correccion de 04_ENLACES.md y de PENDIENTES.md se escribe aparte
(Edit directo, TAREA 1).

USO:
  python scripts/loop/vuelta108_tarea2_5_correccion_opE03.py
"""
import json

RUTA = "docs/plan/OPERACIONES.jsonl"

AGREGADO = (
    " CORRECCION DECLARADA (vuelta 108, TAREA 2.5, remedio de la caida 1.1 del acta de la "
    "vuelta 107, cifra publicada). LO DE ARRIBA NO SE BORRA: el '74/74' del cierre de la "
    "vuelta 107 (SALIDA_V107_TAREA5_5_CIFRA_FINAL_BOLSA.txt, sin script que lo produzca) es "
    "INCORRECTO. Contado hoy con el instrumento nuevo scripts/loop/"
    "verificar_cobertura_bolsa_tres_vias.py (cruza las RESUELTA vivas de "
    "contar_cierre_efectivo.py contra los puestos con veredicto de tres vias en los ficheros "
    "de barrido, declarados y listados en su salida): ANTES de esta vuelta eran 73/74, "
    "docs/loop/SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt, y falta el 46, apartado cada vuelta por "
    "la guarda del paso mal casado (docs/loop/SALIDA_V105_TAREA4_3_RE_BARRIDO.txt). LA TAREA 3 "
    "de esta misma vuelta corrigio la cita de la vara del puesto 46 (correccion_v108, campo "
    "'vara (cita)', sin tocar direccion_leida) y le hizo la pregunta de tres vias "
    "(docs/loop/SALIDA_V108_TAREA3_3_TRES_VIAS_46.md: OBJETO). Recontado con el mismo "
    "instrumento (docs/loop/SALIDA_V108_TAREA3_5_COBERTURA_FINAL.txt): AHORA SI 74/74. LA "
    "BOLSA QUEDA CERRADA POR OBRA DE ESTA VUELTA, no de la 107. Cifra de cierre de OP-E-03 sin "
    "cambio (correccion_v108 es 'vara (cita)', sin efecto en contar_cierre_efectivo.py): "
    "74 / 109 (59,6%)."
)


def main():
    with open(RUTA, encoding="utf-8") as f:
        filas = [json.loads(l) for l in f if l.strip()]

    tocadas = 0
    for fila in filas:
        if fila.get("id_op") == "OP-E-03":
            fila["nota"] = fila["nota"] + AGREGADO
            tocadas += 1
    assert tocadas == 1, tocadas

    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        for fila in filas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

    print("OP-E-03: nota corregida (TAREA 2.5). tocadas=%d" % tocadas)


if __name__ == "__main__":
    main()
