# -*- coding: utf-8 -*-
"""Campania de fidelidad: el aplicador de correcciones declara cada cambio en el nodo
y se niega a aplicar lo que no puede auditar.

Casos positivos: aplica, conserva el texto viejo en `correcciones` con su cita, y
el nodo resultante pasa el validador de esquema (el campo esta legalizado).
Casos negativos: rechaza, sin escribir nada, un texto anterior que no es el vigente,
un texto nuevo con guion largo, una cita sin frase y una correccion repetida.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
APLICADOR = BASE / "scripts" / "fidelidad" / "aplicar_correcciones.py"
VALIDADOR = BASE / "scripts" / "expansion" / "validar_esquema.py"

NODO = {
    "node_id": "nodo_sintetico_fidelidad",
    "fase_proyecto": "ejecucion",
    "dominio": "core",
    "titulo_concepto": "Nodo Sintetico de Fidelidad",
    "fuente": "Test",
    "resumen_teorico": "Resumen de prueba.",
    "pasos_accionables": ["Paso uno", "Reporta de inmediato"],
    "entregable_esperado": "Nada",
    "nodos_previos": [],
    "nodos_siguientes": [],
    "condiciones_activacion": ["Siempre"],
}


def correccion(**cambios):
    c = {
        "id": "prueba-01", "fecha": "2026-09-24", "node_id": NODO["node_id"],
        "campo": "pasos_accionables", "indice": 1, "veredicto": "CONTRARIO",
        "texto_anterior": "Reporta de inmediato", "texto_nuevo": "Reporta en 8 horas",
        "cita": {"libro": "Test", "fichero": "test.txt", "lineas": "L1", "frase": "within 8 hours"},
        "decision": "prueba", "auditoria": "prueba",
    }
    c.update(cambios)
    return c


def correr(repo, tanda):
    ruta = repo / "tanda.json"
    ruta.write_text(json.dumps(tanda), encoding="utf-8")
    return subprocess.run([sys.executable, str(repo / "scripts" / "fidelidad" / "aplicar_correcciones.py"), str(ruta)],
                          capture_output=True, text=True)


def montar(tmp):
    repo = Path(tmp)
    (repo / "scripts" / "fidelidad").mkdir(parents=True)
    shutil.copy(APLICADOR, repo / "scripts" / "fidelidad" / "aplicar_correcciones.py")
    (repo / "dataset" / "nodos").mkdir(parents=True)
    ruta = repo / "dataset" / "nodos" / (NODO["node_id"] + ".json")
    ruta.write_text(json.dumps(NODO, ensure_ascii=False, indent=2), encoding="utf-8")
    return repo, ruta


def main():
    fallos = []
    # POSITIVO: aplica y declara
    with tempfile.TemporaryDirectory() as tmp:
        repo, ruta = montar(tmp)
        r = correr(repo, [correccion()])
        nodo = json.loads(ruta.read_text(encoding="utf-8"))
        if r.returncode != 0:
            fallos.append("no aplico una correccion valida: " + r.stdout)
        if nodo["pasos_accionables"][1] != "Reporta en 8 horas":
            fallos.append("el paso no cambio")
        reg = nodo.get("correcciones", [])
        if len(reg) != 1 or reg[0]["texto_anterior"] != "Reporta de inmediato" or reg[0]["cita"]["frase"] != "within 8 hours":
            fallos.append("el texto viejo o la cita no quedaron declarados en el nodo")
        v = subprocess.run([sys.executable, str(VALIDADOR), str(repo / "dataset" / "nodos")], capture_output=True, text=True)
        if v.returncode != 0:
            fallos.append("el nodo corregido no pasa el validador de esquema: " + v.stdout[-300:])
        # NEGATIVO: la misma correccion otra vez
        r2 = correr(repo, [correccion(texto_anterior="Reporta en 8 horas", texto_nuevo="Otra cosa")])
        if r2.returncode == 0:
            fallos.append("aplico dos veces el mismo id de correccion")
    # NEGATIVOS: cada uno rechazado y sin escribir nada
    for nombre, mala in (
        ("texto anterior que no es el vigente", correccion(texto_anterior="Otra cosa")),
        ("texto nuevo con guion largo", correccion(texto_nuevo="Reporta — en 8 horas")),
        ("cita sin frase", correccion(cita={"libro": "Test", "lineas": "L1", "frase": ""})),
    ):
        with tempfile.TemporaryDirectory() as tmp:
            repo, ruta = montar(tmp)
            antes = ruta.read_text(encoding="utf-8")
            r = correr(repo, [correccion(id="buena-01"), mala])
            if r.returncode == 0:
                fallos.append("acepto " + nombre)
            if ruta.read_text(encoding="utf-8") != antes:
                fallos.append("escribio el nodo pese a rechazar la tanda (" + nombre + ")")
    if fallos:
        print("FALLA:")
        for f in fallos:
            print("  " + f)
        sys.exit(1)
    print("OK: el aplicador declara cada correccion y rechaza lo que no se puede auditar")


if __name__ == "__main__":
    main()
