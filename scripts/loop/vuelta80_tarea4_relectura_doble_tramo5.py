# -*- coding: utf-8 -*-
"""VUELTA 80, TAREA 4: relectura AL DOBLE del tramo 5 de OP-E-01 (12 aristas
escritas en la vuelta 79), por el credito rebajado (AUDITOR.md seccion 1.2):
la caida de reporte de la vuelta 79 cayo FUERA de los discutibles marcados,
asi que el tramo se relee al doble.

DOS BARRIDOS, LOS DOS CON FICHERO DE SALIDA Y LA TABLA CONTADA DE SU FICHERO:

1. Cruza las 12 aristas escritas contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl,
   emparejando SIN DIRECCION (el cribado lee PARES, no aristas dirigidas).

2. Cruza las 12 contra la bolsa filtrada de la vuelta 79
   (docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V79.jsonl, snapshot de 167 filas
   ANTES de que el tramo 5 escribiera), buscando el MISMO PAR en la
   DIRECCION CONTRARIA (la vara de la guarda del par no dirigido, TAREA 4 de
   la vuelta 79).

Nota: dos de las 12 (producto_mercado_fit_motores -> afinar_motor_crecimiento
y terminologia_clave_breakthrough -> analisis_sintomas) ya se revirtieron en
la TAREA 3 de esta misma vuelta por relectura conjunta de un discutible
marcado. Esta relectura al doble es una vara de CREDITO distinta (aparece
FUERA del marcado) y se corre sobre las 12 tal como se escribieron en la
vuelta 79, igual que la vuelta 79 releyo las 24 del tramo 4 sin excluir la
que ya iba a revision conjunta.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]

PARES_TRAMO5 = [
    ("uso_inadecuado_computadoras", "causas_comunes_vs_especiales"),
    ("producto_mercado_fit_motores", "afinar_motor_crecimiento"),
    ("planificacion_inicial_calidad", "identificar_caracteristicas_metas_proceso"),
    ("establecimiento_capacidad_proceso", "pruebas_destructivas"),
    ("certificacion_de_proveedores", "indice_cpk"),
    ("mitigacion_efecto_latigo", "precios_todos_los_dias_bajos"),
    ("herramientas_analisis_causa_raiz", "estratificacion_datos"),
    ("identificacion_evaluacion_peligros", "investigacion_incidentes"),
    ("establecimiento_capacidad_proceso", "control_estadistico_de_procesos"),
    ("testear_circulo_cuadrado_rectangulo", "validar_modelo_negocio_hechos"),
    ("terminologia_clave_breakthrough", "analisis_sintomas"),
    ("mapa_de_canal_de_ventas", "validar_canal_distribucion"),
]

assert len(PARES_TRAMO5) == 12, "el tramo 5 escribio 12, contadas: %d" % len(PARES_TRAMO5)


def cargar_veredictos():
    ruta = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"
    por_par = {}
    with open(ruta, encoding="utf-8") as f:
        for i, linea in enumerate(f, start=1):
            d = json.loads(linea)
            a, b = d.get("nodo_a"), d.get("nodo_b")
            clave = frozenset((a, b))
            por_par.setdefault(clave, []).append((i, d))
    return por_par


def cargar_bolsa_v79():
    ruta = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO_FILTRADO_V79.jsonl"
    filas = []
    with open(ruta, encoding="utf-8") as f:
        for i, linea in enumerate(f, start=1):
            d = json.loads(linea)
            d["_fila"] = i
            filas.append(d)
    return filas


def main():
    veredictos = cargar_veredictos()
    bolsa = cargar_bolsa_v79()

    print("=" * 78)
    print("BARRIDO 1: LAS 12 ARISTAS DEL TRAMO 5 CONTRA INTRA_DOMINIO_VEREDICTOS.jsonl (SIN DIRECCION)")
    print("=" * 78)
    leidos = 0
    clase_a = 0
    a_revertir = []
    for madre, hijo in PARES_TRAMO5:
        clave = frozenset((madre, hijo))
        entradas = veredictos.get(clave, [])
        if not entradas:
            print("  %s -> %s | SIN VEREDICTO" % (madre, hijo))
            continue
        leidos += 1
        for puesto, d in entradas:
            clase = d.get("clase")
            print("  %s -> %s | puesto %d | clase %s" % (madre, hijo, puesto, clase))
            if clase == "A":
                clase_a += 1
                a_revertir.append((madre, hijo, puesto))
    print()
    print("RESUMEN BARRIDO 1: pares %d | LEIDOS por el cribado %d | clase A %d | A REVERTIR %d"
          % (len(PARES_TRAMO5), leidos, clase_a, len(a_revertir)))
    print()

    print("=" * 78)
    print("BARRIDO 2: LAS 12 CONTRA LA BOLSA FILTRADA DE LA VUELTA 79 (167 FILAS), BUSCANDO LA RECIPROCA")
    print("=" * 78)
    con_reciproca = []
    for madre, hijo in PARES_TRAMO5:
        reciprocas = [f for f in bolsa if f["madre"] == hijo and f["hijo"] == madre]
        if reciprocas:
            for r in reciprocas:
                print("  %s -> %s | RECIPROCA en fila %d (paso %s), arista=%s"
                      % (madre, hijo, r["_fila"], r["paso"], r["arista"]))
            con_reciproca.append((madre, hijo))
    print()
    print("RESUMEN BARRIDO 2: de las 12, con reciproca propuesta en la bolsa filtrada: %d"
          % len(con_reciproca))
    for madre, hijo in con_reciproca:
        print("  -> %s -> %s" % (madre, hijo))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
