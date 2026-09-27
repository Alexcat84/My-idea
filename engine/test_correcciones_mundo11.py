# -*- coding: utf-8 -*-
"""Integracion del mundo 11 (decisiones del fundador, 28 sep 2026): el aplicador de correcciones declaradas
sirve tambien para limpiar el pack ANTES de integrarlo, y gana los veredictos de esa limpieza.

Casos positivos:
  - `--nodos DIR` aplica sobre la carpeta de un pack (packs/<dominio>/nodos) y no toca dataset/nodos;
  - VOZ quita la voz de libro ("el libro", "el texto", "el autor") de cualquier campo de cara, titulo incluido;
  - RESUMEN pone el resumen nuevo (400 a 600 caracteres) y exige que el texto viejo ya viva en
    `notas_extraccion`, el campo interno nuevo: no lo duplica en `correcciones`, lo remite alli;
  - CIFRA quita una cifra de mercado declarando el fragmento que sale;
  - DOMINIO admite `primer_equipo`;
  - el nodo resultante, con `notas_extraccion`, pasa la lista blanca del esquema.
Casos negativos (rechazados sin escribir nada): un fragmento de VOZ que sigue en el texto nuevo; un RESUMEN corto o
largo; un RESUMEN sin `notas_extraccion` igual al texto viejo; un RESUMEN sin fichero y lineas en su evidencia.
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

NOTA = "UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_13.md, lineas 187 a 198. EL SEIS DEL ID ES DEL LIBRO."
NODO = {
    "node_id": "nodo_sintetico_m11",
    "fase_proyecto": "ejecucion",
    "dominio": "primer_equipo",
    "titulo_concepto": "Aplicar las tres preguntas que el libro nombra",
    "fuente": "Test",
    "resumen_teorico": NOTA,
    "notas_extraccion": NOTA,
    "pasos_accionables": ["Cuenta hasta seis, como el texto dice.", "Paga 50.000 dolares al reclutador."],
    "entregable_esperado": "Nada",
    "nodos_previos": [],
    "nodos_siguientes": [],
    "condiciones_activacion": ["Siempre"],
}
RESUMEN_NUEVO = (
    "Pedir critica sirve de poco si quien la pide rompe el silencio que sigue a la pregunta: la otra persona "
    "necesita unos segundos para decidir si es seguro decir lo incomodo. Aguantar ese silencio, contando en "
    "silencio y sin rellenarlo, le demuestra que la pregunta iba en serio y que no vas a castigar la respuesta. "
    "Si aun asi no llega nada, volver a preguntar con otras palabras o comprometerse a retomarlo mantiene abierta "
    "la puerta sin forzarla, y con el tiempo convierte la critica en un habito del equipo."
)
assert 400 <= len(RESUMEN_NUEVO) <= 600, len(RESUMEN_NUEVO)


def c(**cambios):
    base = {"id": "m11-01", "fecha": "2026-09-28", "node_id": NODO["node_id"], "decision": "prueba", "auditoria": "prueba"}
    base.update(cambios)
    return base


VOZ_PASO = c(campo="pasos_accionables", indice=0, veredicto="VOZ", texto_anterior="Cuenta hasta seis, como el texto dice.",
             texto_nuevo="Cuenta hasta seis antes de volver a hablar.",
             cita={"regla": "voz de libro (decision del fundador, 28 sep 2026)", "fragmentos": ["como el texto dice"]})
VOZ_TITULO = c(id="m11-02", campo="titulo_concepto", veredicto="VOZ",
               texto_anterior="Aplicar las tres preguntas que el libro nombra", texto_nuevo="Aplicar las tres preguntas",
               cita={"regla": "voz de libro (decision del fundador, 28 sep 2026)", "fragmentos": ["que el libro nombra"]})
RESUMEN = c(id="m11-03", campo="resumen_teorico", veredicto="RESUMEN", texto_anterior=NOTA, texto_nuevo=RESUMEN_NUEVO,
            cita={"instrumento": "redactor, verificador ciego y arbitro", "evidencia": {"fichero": "fuentes/scott_radical_candor/cap_13.md", "lineas": "187-198"}})
CIFRA = c(id="m11-04", campo="pasos_accionables", indice=1, veredicto="CIFRA",
          texto_anterior="Paga 50.000 dolares al reclutador.", texto_nuevo="Acuerda por adelantado lo que pagaras al reclutador.",
          cita={"regla": "regla de la cifra (docs/POLITICA_MARCO_PAIS.md): la cifra de mercado sale", "fragmentos": ["50.000 dolares"]})
ORTO_TITULO = c(id="m11-06", campo="titulo_concepto", veredicto="ORTOGRAFIA", texto_anterior="Aplicar las tres preguntas",
                texto_nuevo="Aplicar las tres preguntas clave", motivos=["ortografia"],
                cita={"instrumento": "prueba", "evidencia": "prueba"})
DOMINIO = c(id="m11-05", campo="dominio", veredicto="DOMINIO", texto_anterior="primer_equipo", texto_nuevo="core",
            cita={"instrumento": "prueba", "evidencia": "prueba"})


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
    pack = repo / "packs" / "primer_equipo" / "nodos"
    pack.mkdir(parents=True)
    ruta = pack / (NODO["node_id"] + ".json")
    ruta.write_text(json.dumps(NODO, ensure_ascii=False, indent=2), encoding="utf-8")
    return repo, ruta, pack


def correr(repo, pack, tanda):
    t = repo / "tanda.json"
    t.write_text(json.dumps(tanda, ensure_ascii=False), encoding="utf-8")
    import os
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run([sys.executable, str(repo / "scripts" / "fidelidad" / "aplicar_correcciones.py"), str(t), "--nodos", str(pack)],
                          capture_output=True, text=True, encoding="utf-8", env=env)


def main():
    fallos = []
    with tempfile.TemporaryDirectory() as tmp:
        repo, ruta, pack = montar(tmp)
        r = correr(repo, pack, [VOZ_PASO, VOZ_TITULO, RESUMEN, CIFRA])
        if r.returncode != 0:
            fallos.append("no aplico una tanda valida sobre el pack: " + r.stdout[-400:])
        else:
            n = json.loads(ruta.read_text(encoding="utf-8"))
            if n["pasos_accionables"][0] != VOZ_PASO["texto_nuevo"] or n["titulo_concepto"] != VOZ_TITULO["texto_nuevo"]:
                fallos.append("VOZ no cambio el paso o el titulo")
            if n["resumen_teorico"] != RESUMEN_NUEVO or n.get("notas_extraccion") != NOTA:
                fallos.append("RESUMEN no puso el resumen nuevo o perdio las notas de extraccion")
            reg = {x["id"]: x for x in n.get("correcciones", [])}
            if reg.get("m11-03", {}).get("texto_anterior_en") != "notas_extraccion" or NOTA in json.dumps(reg.get("m11-03", {}), ensure_ascii=False):
                fallos.append("RESUMEN duplico la nota en correcciones en vez de remitir a notas_extraccion")
            if n["pasos_accionables"][1] != CIFRA["texto_nuevo"]:
                fallos.append("CIFRA no cambio el paso")
            if any(Path(repo / "dataset" / "nodos").iterdir()):
                fallos.append("--nodos escribio en dataset/nodos")
            v = subprocess.run([sys.executable, str(VALIDADOR), str(pack)], capture_output=True, text=True, encoding="utf-8")
            if v.returncode != 0:
                fallos.append("el nodo con notas_extraccion no pasa la lista blanca: " + v.stdout[-300:])
    with tempfile.TemporaryDirectory() as tmp:
        repo, ruta, pack = montar(tmp)
        r = correr(repo, pack, [VOZ_TITULO, ORTO_TITULO])
        n = json.loads(ruta.read_text(encoding="utf-8"))
        if r.returncode != 0 or n["titulo_concepto"] != "Aplicar las tres preguntas clave":
            fallos.append("ORTOGRAFIA no corrige el titulo (la forja escribe sin tildes): " + r.stdout[-300:])
        elif [x.get("motivos") for x in n["correcciones"] if x["id"] == "m11-06"] != [["ortografia"]]:
            fallos.append("los motivos de una correccion no quedan declarados en el nodo")
    with tempfile.TemporaryDirectory() as tmp:
        repo, ruta, pack = montar(tmp)
        if correr(repo, pack, [DOMINIO]).returncode != 0:
            fallos.append("DOMINIO no admite primer_equipo como dominio de partida o core de llegada")
    # Las tildes no crean barandas: "tu organizacion" -> "tu organización" ya estaba (residuo_corporativo) y la
    # correccion solo le pone la tilde. Antes el aplicador comparaba la cita exacta y la daba por nueva.
    with tempfile.TemporaryDirectory() as tmp:
        repo, ruta, pack = montar(tmp)
        n = dict(NODO, entregable_esperado="Las reglas repartidas en tu organizacion segun el caso.")
        ruta.write_text(json.dumps(n, ensure_ascii=False, indent=2), encoding="utf-8")
        orto = c(id="m11-07", campo="entregable_esperado", veredicto="ORTOGRAFIA",
                 texto_anterior="Las reglas repartidas en tu organizacion segun el caso.",
                 texto_nuevo="Las reglas repartidas en tu organización según el caso.",
                 cita={"instrumento": "prueba", "evidencia": "prueba"})
        r = correr(repo, pack, [orto])
        if r.returncode != 0:
            fallos.append("una correccion de solo tildes se rechazo por una baranda que ya estaba: " + r.stdout[-300:])
    sin_nota = dict(NODO)
    sin_nota.pop("notas_extraccion")
    for nombre, mala, nodo in (
        ("un fragmento de VOZ que sigue en el texto", dict(VOZ_PASO, texto_nuevo="Cuenta hasta seis, como el texto dice, y espera."), NODO),
        ("un RESUMEN de menos de 400 caracteres", dict(RESUMEN, texto_nuevo=RESUMEN_NUEVO[:300]), NODO),
        ("un RESUMEN de mas de 600 caracteres", dict(RESUMEN, texto_nuevo=RESUMEN_NUEVO + " " + RESUMEN_NUEVO[:250]), NODO),
        ("un RESUMEN sin la nota en notas_extraccion", RESUMEN, sin_nota),
        ("un RESUMEN sin fichero y lineas", dict(RESUMEN, cita={"instrumento": "x", "evidencia": {"fichero": ""}}), NODO),
    ):
        with tempfile.TemporaryDirectory() as tmp:
            repo, ruta, pack = montar(tmp)
            ruta.write_text(json.dumps(nodo, ensure_ascii=False, indent=2), encoding="utf-8")
            antes = ruta.read_text(encoding="utf-8")
            r = correr(repo, pack, [mala])
            if r.returncode == 0:
                fallos.append("acepto " + nombre)
            if ruta.read_text(encoding="utf-8") != antes:
                fallos.append("escribio pese a rechazar (" + nombre + ")")
    if fallos:
        print("FALLA:")
        for f in fallos:
            print("  " + f)
        sys.exit(1)
    print("OK: el aplicador limpia el pack del mundo 11 por correccion declarada y rechaza lo que no se puede auditar")


if __name__ == "__main__":
    main()
