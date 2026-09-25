# -*- coding: utf-8 -*-
"""Campania de fidelidad: el aplicador de correcciones declara cada cambio en el nodo
y se niega a aplicar lo que no puede auditar.

Casos positivos: aplica (un paso y una condicion de activacion), conserva el texto viejo en `correcciones` con su cita, y
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
    "etiqueta_arbol": "Domina el Mundo",
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
    for util in ("censo_duplicacion.py", "etiquetas_de_cara.py"):
        if (BASE / "scripts" / util).exists():
            shutil.copy(BASE / "scripts" / util, repo / "scripts" / util)
    (repo / "dataset" / "metadata").mkdir(parents=True)
    fp = BASE / "dataset" / "metadata" / "falsos_positivos_adjudicados.json"
    if fp.exists():
        shutil.copy(fp, repo / "dataset" / "metadata" / fp.name)
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
    # POSITIVO: una condicion de activacion se corrige por indice, como un paso
    with tempfile.TemporaryDirectory() as tmp:
        repo, ruta = montar(tmp)
        r = correr(repo, [correccion(id="cond-01", campo="condiciones_activacion", indice=0,
                                     texto_anterior="Siempre", texto_nuevo="Cuando el libro lo dice")])
        nodo = json.loads(ruta.read_text(encoding="utf-8"))
        if r.returncode != 0:
            fallos.append("no aplico una correccion valida de condiciones_activacion: " + r.stdout)
        elif nodo["condiciones_activacion"][0] != "Cuando el libro lo dice" or nodo["correcciones"][0].get("indice") != 0:
            fallos.append("la condicion no cambio o no quedo declarada con su indice")
    # POSITIVO: la etiqueta de cara, campo escalar
    with tempfile.TemporaryDirectory() as tmp:
        repo, ruta = montar(tmp)
        r = correr(repo, [correccion(id="etq-01", campo="etiqueta_arbol", indice=None,
                                     texto_anterior="Domina el Mundo", texto_nuevo="Deja la Fuerza Bruta")])
        nodo = json.loads(ruta.read_text(encoding="utf-8"))
        if r.returncode != 0 or nodo.get("etiqueta_arbol") != "Deja la Fuerza Bruta":
            fallos.append("no corrigio la etiqueta de cara: " + r.stdout)
    # NEGATIVOS: cada uno rechazado y sin escribir nada
    for nombre, mala in (
        ("una condicion con indice fuera de rango",
         correccion(id="mala-03", campo="condiciones_activacion", indice=5, texto_anterior="Siempre", texto_nuevo="Otra")),
        ("texto anterior que no es el vigente", correccion(texto_anterior="Otra cosa")),
        ("texto nuevo con guion largo", correccion(texto_nuevo="Reporta " + chr(0x2014) + " en 8 horas")),
        ("cita sin frase", correccion(cita={"libro": "Test", "lineas": "L1", "frase": ""})),
        ("una sigla sin localizar (baranda dato_local_cableado)",
         correccion(id="mala-02", indice=0, texto_anterior="Paso uno", texto_nuevo="Reporta a la OSHA en 8 horas")),
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
