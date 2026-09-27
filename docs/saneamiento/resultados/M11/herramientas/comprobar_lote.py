# -*- coding: utf-8 -*-
"""Comprobacion mecanica de un lote del REDACTOR M11 antes de entregarlo (no juzga el sentido: eso es del verificador).

    python comprobar_lote.py redactor/lote_NN.json

Sale con 1 y lista los problemas si: falta un nodo de la entrada; el resumen no tiene 400 a 600 caracteres o le falta
fichero o lineas; un indice no existe; un fragmento declarado sigue en el texto nuevo; un texto nuevo trae guion
largo o medio, tres puntos, voz de libro, marcas de auditoria o una palabra comun sin tilde; o un elemento que NO
cambia conserva voz de libro, ingles o faltas de tilde.
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
VOZ = re.compile(
    r"(?<![\w])(?:(?:el|del|al|este|ese|propio|mismo) libro(?! de texto| abierto)|(?:el|del|al|la|de la|los|las) autor(?:a|es|as)?"
    r"|(?:seg[uú]n|como dice|lo que dice) el texto|el texto (?:lo |la |las |los |le |les |no )?(?:dice|pone|nombra|enumera|escribe|cuenta|llama"
    r"|describe|avisa|hace|propone|atribuye|define|recoge|da|trae|manda|pide|admite|advierte|recomienda|sugiere|abre|cierra|usa|deja|insiste|lista|habla)"
    r"|(?:del|propio) texto(?! (?:de|legal|lineal|completo|largo|plano))|(?:el|del|este|ese|mismo|propio) cap[ií]tulo|la obra|recuadro)(?![\w])",
    re.I)
MARCAS = re.compile(r"fuentes/[a-z_]+|\bcap_\d+|[a-z0-9_]\.md\b|UNIDAD DE ORIGEN|\bD\.\d{1,3}\b|\bl[ií]neas? \d+", re.I)
AUTORES = re.compile(r"\b(?:Kim Scott|Scott|Julie Zhuo|Zhuo|Geoff Smart|Randy Street|Grove|Gerber|Marquet|Radical Candor|High Output|E-Myth|Turn the Ship|Making of a Manager|ghSMART)\b")
INGLES = re.compile(r"\b(?:the|and|you|we|of|to|with|your|this|that|is|are|what|when|how)\b(?:\s+\w+){0,3}\s+\b(?:the|to|a|and|of|you|your|it|is|in)\b", re.I)
# palabras comunes que la forja escribe sin tilde (muestra, no exhaustiva)
# (solo palabras que SIN tilde no existen en espanol: nada de verbos como critica, practica, publico o ultimo)
SIN_TILDE = re.compile(r"(?<![\w])(?:segun|reunion|tambien|despues|asi|ademas|todavia|decision|informacion|comunicacion|organizacion"
                       r"|evaluacion|conversacion|situacion|accion|direccion|relacion|solucion|dia|dias|facil|dificil|rapido|metodo|metodos"
                       r"|tecnica|tecnicas|proximo|companero|companeros|anos|senal|senales|codigo|codigos|numeros|paginas|despues)(?![\w])", re.I)
PROHIBIDOS = ("—", "–", "...")


def textos_viejos(n):
    out = {("titulo_concepto", None): n["titulo_concepto"], ("entregable_esperado", None): n["entregable_esperado"]}
    for i, t in enumerate(n["pasos_accionables"]):
        out[("pasos_accionables", i)] = t
    for i, t in enumerate(n["condiciones_activacion"]):
        out[("condiciones_activacion", i)] = t
    return out


def main(ruta):
    salida = json.loads(Path(ruta).read_text(encoding="utf-8"))
    lote = salida["lote"]
    entrada = json.loads((AQUI / "entrada" / ("lote_%s.json" % lote)).read_text(encoding="utf-8"))
    por_id = {n["node_id"]: n for n in salida["nodos"]}
    problemas = []
    for n in entrada["nodos"]:
        nid = n["node_id"]
        s = por_id.get(nid)
        if not s:
            problemas.append("%s: falta en la salida" % nid)
            continue
        r = s.get("resumen") or {}
        t = r.get("texto") or ""
        if not 400 <= len(t) <= 600:
            problemas.append("%s: el resumen tiene %d caracteres" % (nid, len(t)))
        if not r.get("fichero") or not r.get("lineas"):
            problemas.append("%s: el resumen no declara fichero y lineas" % nid)
        viejos = textos_viejos(n)
        nuevos = {("resumen_teorico", None): t}
        for c in s.get("cambios") or []:
            k = (c.get("campo"), c.get("indice"))
            if k not in viejos:
                problemas.append("%s: el cambio %s no existe en el nodo" % (nid, k))
                continue
            nuevos[k] = c.get("texto_nuevo") or ""
            for f in c.get("fragmentos") or []:
                if f and f in nuevos[k]:
                    problemas.append("%s %s: el fragmento %r sigue en el texto nuevo" % (nid, k, f))
        for k, v in viejos.items():
            nuevos.setdefault(k, v)  # lo que no cambia se da por bueno: se mira igual
        for k, v in nuevos.items():
            for rx, que in ((VOZ, "voz de libro"), (MARCAS, "marca de auditoria"), (AUTORES, "autor o titulo"), (INGLES, "ingles"), (SIN_TILDE, "palabra sin tilde")):
                m = rx.search(v)
                if m:
                    problemas.append("%s %s: %s %r" % (nid, k, que, m.group(0)))
            if any(p in v for p in PROHIBIDOS):
                problemas.append("%s %s: guion largo, medio o tres puntos" % (nid, k))
    if problemas:
        print("LOTE %s CON %d PROBLEMAS:" % (lote, len(problemas)))
        for p in problemas:
            print("  " + p)
        return 1
    print("LOTE %s OK: %d nodos, comprobacion mecanica sin problemas" % (lote, len(entrada["nodos"])))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
