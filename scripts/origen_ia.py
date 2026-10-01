"""NINGUNA REFERENCIA DE ORIGEN LLEGA A LA IA (regla del fundador, 1 oct 2026; docs/REGLAS_DE_LA_CASA.md).

No basta con ordenarle a la IA que no cite (REGLA_SIN_FUENTES): la referencia no debe llegarle nunca. Toda llamada a la
IA de la web lee el texto de los nodos de la VISTA WEB (web/lib/assets/), y esa vista la escribe un solo script,
scripts/sync_assets_web.py. Esta es la funcion unica por la que pasa todo texto de nodo en ese camino: quita los
titulos y los autores de la lista canonica (dataset/metadata/fuentes_canonicas.json) sin tocar el resto del texto ni
los nombres de metodo. La lista canonica no viaja a la web: el filtro corre aqui, antes de escribir la vista.

El dataset no cambia (el titulo_concepto es material interno y no se modifica por doctrina). Cada quita queda en el
registro interno dataset/metadata/quitas_origen_ia.json, que no se copia a la web.
Los textos de cara al cliente no dependen de este filtro: una persona citada en un campo visible sale por correccion
declarada (veredicto ATRIBUCION), y la guarda es web/lib/procedencia.test.ts. Prueba: engine/test_origen_ia.py.
"""
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CANON = BASE / "dataset/metadata/fuentes_canonicas.json"
REGISTRO = BASE / "dataset/metadata/quitas_origen_ia.json"

CAMPOS_TEXTO = ("titulo_concepto", "etiqueta_arbol", "resumen_teorico", "pasos_accionables", "entregable_esperado",
                "condiciones_activacion")

# Coincidencias con un apellido de la lista que NO son el autor (revisadas por el fundador, punto D del 1 oct 2026).
EXCEPCIONES = ("MINI Cooper",)

_NOMBRE = r"[A-ZÁÉÍÓÚÑ][\wáéíóúñ'.]*"

# Decision del fundador (1 oct 2026, punto 3): cuando quitar el apellido deja el nombre sin sentido ("Paso 6 de
# Crosby" -> "Paso 6"), se SUSTITUYE por el nombre neutro del metodo. Van antes que las quitas. Cada entrada: patron,
# nombre neutro en minuscula y en mayusculas de titulo (se elige por la mayuscula de la primera letra del original).
NEUTROS = [
    (r"[Tt]rilog[íi]a de Juran", "trilogía de la calidad", "Trilogía de la Calidad"),
    (r"[Cc]iclo (?:de )?(?:Shewhart-Deming|Deming|Shewhart)", "ciclo PDCA", "Ciclo PDCA"),
    (r"14 [Pp]untos de Deming", "14 principios de gestión de la calidad", "14 Principios de Gestión de la Calidad"),
    (r"[Pp]aso (\d+) de Crosby", r"paso \1 del programa de cero defectos", r"Paso \1 del programa de cero defectos"),
    (r"[Cc]uatro [Ee]tapas de Wallas", "cuatro etapas del proceso creativo", "Cuatro Etapas del Proceso Creativo"),
]
_NEUTROS = [(re.compile(p), m, t) for p, m, t in NEUTROS]


def cargar_canon():
    fuentes = json.loads(CANON.read_text(encoding="utf-8"))["fuentes"].values()
    return {"titulos": sorted({t for f in fuentes for t in f["titulos"]}),
            "autores": sorted({a for f in fuentes for a in f.get("autores", [])})}


def patrones(canon):
    """Los autores se buscan con mayuscula y como palabra entera: 'reason to buy' o 'brown-bag' no son apellidos.
    Los titulos, sin distinguir mayusculas y con sus comillas."""
    aut = "(?:" + "|".join(re.escape(a) for a in sorted(canon["autores"], key=len, reverse=True)) + r")(?![\w-])"
    grupo = r"(?:%s\s*[-–]\s*)*%s(?:\s*[-–]\s*%s)*" % (_NOMBRE, aut, _NOMBRE)
    tit = "|".join(re.escape(t) for t in sorted(canon["titulos"], key=len, reverse=True))
    return [
        # un titulo de libro, con sus comillas si las lleva
        re.compile(r"\s*[\"'«“‘]?(?:%s)[\"'»”’]?" % tit, re.I),
        # un parentesis que solo trae nombres: "(Juran)", "(Shewhart-Deming)", "(Lubin-Esty)"
        re.compile(r"\s*\(%s(?:\s*(?:,|y)\s*%s)*\)" % (grupo, grupo)),
        # el autor al final de un parentesis con mas texto: "(Red de Profesionales, Crosby)"
        re.compile(r"\s*,\s*%s(?=\))" % grupo),
        # "de Juran", "de Deming", "del Crosby"
        re.compile(r"\s+del?\s+%s" % grupo),
        # el autor como adjetivo o suelto: "Modelo Juran de Calidad"
        re.compile(r"\s*(?<![\w-])%s" % grupo),
    ]


def quitar_origen(texto, pats):
    """Devuelve (texto_limpio, quitas). Una quita es el trozo exacto que salio, o "original -> nombre neutro"."""
    if not texto:
        return texto, []
    guardados = {}
    for i, e in enumerate(EXCEPCIONES):
        if e in texto:
            marca = "\x00%d\x00" % i
            guardados[marca] = e
            texto = texto.replace(e, marca)
    quitas = []
    for p, minus, titulo in _NEUTROS:
        def _neutro(m, minus=minus, titulo=titulo):
            nuevo = m.expand(titulo if next(c for c in m.group(0) if c.isalpha()).isupper() else minus)
            quitas.append("%s -> %s" % (m.group(0), nuevo))
            return nuevo
        texto = p.sub(_neutro, texto)
    for p in pats:
        def _quita(m):
            quitas.append(m.group(0))
            return ""
        texto = p.sub(_quita, texto)
    if quitas:
        texto = re.sub(r"\(\s*\)", "", texto)
        texto = re.sub(r"\s+([,.;:)])", r"\1", texto)
        texto = re.sub(r"\(\s+", "(", texto)
        texto = re.sub(r"[ \t]{2,}", " ", texto).strip()
    for marca, e in guardados.items():
        texto = texto.replace(marca, e)
    return texto, quitas


def limpiar_nodo(nodo, pats, registro):
    for campo in CAMPOS_TEXTO:
        v = nodo.get(campo)
        if isinstance(v, str):
            nuevo, quitas = quitar_origen(v, pats)
            if quitas:
                nodo[campo] = nuevo
                registro.extend({"node_id": nodo["node_id"], "campo": campo, "indice": None, "quitado": q}
                                for q in quitas)
        elif isinstance(v, list):
            for i, s in enumerate(v):
                if not isinstance(s, str):
                    continue
                nuevo, quitas = quitar_origen(s, pats)
                if quitas:
                    v[i] = nuevo
                    registro.extend({"node_id": nodo["node_id"], "campo": campo, "indice": i, "quitado": q}
                                    for q in quitas)
    return nodo


def limpiar_textos(datos, pats, registro, donde):
    """Cualquier otro asset con texto que llega a la IA (las preguntas en cache): recorre sus cadenas."""
    if isinstance(datos, dict):
        return {k: limpiar_textos(v, pats, registro, donde + [k]) for k, v in datos.items()}
    if isinstance(datos, list):
        return [limpiar_textos(v, pats, registro, donde + [i]) for i, v in enumerate(datos)]
    if isinstance(datos, str):
        nuevo, quitas = quitar_origen(datos, pats)
        registro.extend({"asset": donde[0], "ruta": donde[1:], "quitado": q} for q in quitas)
        return nuevo
    return datos


def escribir_registro(registro):
    REGISTRO.write_text(json.dumps({
        "_nota": "Registro interno de las quitas del filtro de origen hacia la IA (scripts/origen_ia.py). No se copia "
                 "a la web. Se regenera en cada sync_assets_web.py.",
        "quitas": registro}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
