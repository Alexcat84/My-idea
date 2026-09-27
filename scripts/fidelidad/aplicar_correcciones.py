# -*- coding: utf-8 -*-
"""Aplica una tanda de correcciones de FIDELIDAD a dataset/nodos, cada una DECLARADA en el nodo.

Mandato del fundador (campania de fidelidad total, sep 2026): nunca le diremos a un
cliente lo contrario de lo que dice su fuente. Cada cambio es una correccion
declarada: el texto viejo NO se borra, queda en el campo `correcciones` del propio
nodo, con la cita literal del libro que motiva el cambio ("una correccion que tapa
lo que corrige no se puede auditar", docs/loop/EJECUTOR.md regla 8).

Uso:
  python scripts/fidelidad/aplicar_correcciones.py <tanda.json> [--comprobar]

<tanda.json> es una lista de correcciones:
  {"id", "node_id", "campo" (pasos_accionables | condiciones_activacion | resumen_teorico |
   entregable_esperado | etiqueta_arbol), "indice" (solo en los campos lista, pasos y condiciones, desde 0), "veredicto" (CONTRARIO | ANADIDO | ATRIBUCION), "texto_anterior",
   "texto_nuevo", "cita": {"libro", "fichero", "lineas", "frase"}, "decision", "auditoria"}

El veredicto ATRIBUCION (REGLA ESTRICTA del fundador, 26 sep 2026: el cliente nunca ve un autor ni un libro citado
como fuente) quita la cita a un autor o a un libro sin cambiar el sentido. No lo motiva una frase del libro sino la
regla, asi que su "cita" es {"regla", "fragmentos"}: la regla que lo ordena y los fragmentos de atribucion que salen.

Los veredictos FASE, DOMINIO y COHERENCIA (saneamiento del dataset, TANDA 2, 26 sep 2026) los declara una pasada de
lectura contra el propio nodo, no una frase del libro: su "cita" es {"instrumento", "evidencia"}. FASE corrige
`fase_proyecto` (ideacion, validacion, planificacion o ejecucion), DOMINIO corrige `dominio` (uno de los mundos) y
COHERENCIA corrige un texto que contradice el resto del propio nodo (por ejemplo, una condicion de activacion), y
VIGENCIA uno que dejo de ser cierto con el tiempo (un enlace roto o movido, comprobado por un instrumento).

Se niega (exit 1, sin escribir nada) si el texto anterior no es EXACTAMENTE el
vigente, si el nuevo trae guiones largos o medios, si falta la cita, o si el id
de la correccion ya esta aplicado en el nodo. Con --comprobar solo valida.

Integracion del mundo 11 (decisiones del fundador, 28 sep 2026): el pack se limpia ANTES de integrarse.
  --nodos DIR   aplica sobre otra carpeta de nodos (la de un pack, packs/<dominio>/nodos) en vez de dataset/nodos.
  VOZ           quita la voz de libro ("el libro", "el texto", "el autor", las citas en ingles) de un campo de cara,
                titulo_concepto incluido, sin cambiar el sentido. Su "cita" es {"regla", "fragmentos"} como ATRIBUCION.
  CIFRA         quita una cifra de mercado (regla de la cifra de docs/POLITICA_MARCO_PAIS.md). {"regla", "fragmentos"}.
  RESUMEN       pone el resumen nuevo (400 a 600 caracteres) cuando el viejo era la nota de extraccion de la forja.
                El texto viejo YA vive en el campo interno `notas_extraccion` (el importador lo copia alli): el
                aplicador lo exige identico y en `correcciones` lo remite con `texto_anterior_en` en vez de duplicarlo.
                Su "cita" es {"instrumento", "evidencia": {"fichero", "lineas"}}.
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
NODOS = BASE / "dataset" / "nodos"
CAMPOS = {"pasos_accionables", "condiciones_activacion", "resumen_teorico", "entregable_esperado", "etiqueta_arbol",
          "fase_proyecto", "dominio", "titulo_concepto"}
# El titulo llega a la IA y a la pantalla (docs/fidelidad/CAMPOS_QUE_LLEGAN.md), pero su contenido vive con el libro:
# solo lo tocan la voz de cliente y la ortografia (la forja escribe sin tildes).
SOLO_VOZ = {"titulo_concepto": {"VOZ", "ATRIBUCION", "ORTOGRAFIA"}}
# Veredictos que declara una regla y los fragmentos que salen, no una frase del libro.
POR_REGLA = {"ATRIBUCION", "VOZ", "CIFRA"}
RESUMEN_MIN, RESUMEN_MAX = 400, 600
FASES = {"ideacion", "validacion", "planificacion", "ejecucion"}
DOMINIOS = {"core", "quality", "health_safety", "environmental", "seguridad_digital", "exportacion", "franquicias",
            "risk_management", "compras", "entrega", "primer_equipo"}
# Declarados por una pasada de lectura contra el propio nodo: su cita es {"instrumento", "evidencia"}.
POR_INSTRUMENTO = {"FASE": "fase_proyecto", "DOMINIO": "dominio", "COHERENCIA": None, "VIGENCIA": None, "ORTOGRAFIA": None}
# Los campos lista se corrigen elemento a elemento, por indice. Las condiciones de
# activacion entraron el 24 sep 2026: la pasada contra la fuente sobre los campos
# que no son pasos (docs/fidelidad/CAMPOS_QUE_LLEGAN.md) llegan a la IA. La etiqueta
# de cara (etiqueta_arbol, escalar) entro con fidelidad-t15: es lo que ve la pantalla.
LISTAS = {"pasos_accionables", "condiciones_activacion"}
PROHIBIDOS = (chr(0x2014), chr(0x2013))


def validar(c, nodo):
    fallas = []
    for k in ("id", "node_id", "campo", "veredicto", "texto_anterior", "texto_nuevo", "cita", "decision", "fecha"):
        if not c.get(k):
            fallas.append("falta %s" % k)
    if c.get("campo") not in CAMPOS:
        fallas.append("campo no admitido: %r" % c.get("campo"))
    if c.get("campo") in SOLO_VOZ and c.get("veredicto") not in SOLO_VOZ[c["campo"]]:
        fallas.append("%s solo se corrige con %s" % (c["campo"], sorted(SOLO_VOZ[c["campo"]])))
    cita = c.get("cita") or {}
    if c.get("veredicto") in POR_INSTRUMENTO:
        if not cita.get("instrumento") or not cita.get("evidencia"):
            fallas.append("un veredicto %s declara su instrumento y su evidencia" % c.get("veredicto"))
        campo = POR_INSTRUMENTO[c["veredicto"]]
        if campo and c.get("campo") != campo:
            fallas.append("el veredicto %s solo corrige %s" % (c["veredicto"], campo))
        if c.get("campo") in ("fase_proyecto", "dominio") and c.get("veredicto") not in ("FASE", "DOMINIO"):
            fallas.append("fase_proyecto y dominio solo se corrigen con los veredictos FASE y DOMINIO")
        if c.get("campo") == "fase_proyecto" and c.get("texto_nuevo") not in FASES:
            fallas.append("fase no valida: %r" % c.get("texto_nuevo"))
        if c.get("campo") == "dominio" and c.get("texto_nuevo") not in DOMINIOS:
            fallas.append("dominio no valido: %r" % c.get("texto_nuevo"))
    elif c.get("campo") in ("fase_proyecto", "dominio"):
        fallas.append("fase_proyecto y dominio solo se corrigen con los veredictos FASE y DOMINIO")
    elif c.get("veredicto") == "RESUMEN":
        ev = cita.get("evidencia") or {}
        if not cita.get("instrumento") or not isinstance(ev, dict) or not ev.get("fichero") or not ev.get("lineas"):
            fallas.append("un RESUMEN declara su instrumento y su evidencia con fichero y lineas")
        if c.get("campo") != "resumen_teorico":
            fallas.append("el veredicto RESUMEN solo corrige resumen_teorico")
        largo = len(c.get("texto_nuevo") or "")
        if not RESUMEN_MIN <= largo <= RESUMEN_MAX:
            fallas.append("el resumen nuevo tiene %d caracteres (van de %d a %d)" % (largo, RESUMEN_MIN, RESUMEN_MAX))
        if nodo is not None and nodo.get("notas_extraccion") != c.get("texto_anterior"):
            fallas.append("el texto viejo del resumen no esta guardado en notas_extraccion")
    elif c.get("veredicto") in POR_REGLA:
        if not cita.get("regla") or not cita.get("fragmentos"):
            fallas.append("una %s declara su regla y los fragmentos que salen" % c.get("veredicto"))
        for f in cita.get("fragmentos") or []:
            if f and f in c.get("texto_nuevo", ""):
                fallas.append("el fragmento de atribucion sigue en el texto nuevo: %r" % f)
    else:
        for k in ("libro", "lineas", "frase"):
            if not cita.get(k):
                fallas.append("cita sin %s" % k)
    if any(p in c.get("texto_nuevo", "") for p in PROHIBIDOS):
        fallas.append("el texto nuevo trae guion largo o medio")
    if c.get("texto_nuevo") == c.get("texto_anterior"):
        fallas.append("el texto nuevo es igual al anterior")
    if nodo is None:
        return fallas + ["el nodo no existe"]
    if any(x.get("id") == c.get("id") for x in nodo.get("correcciones", [])):
        fallas.append("la correccion %s ya esta aplicada" % c.get("id"))
    if c.get("campo") in LISTAS:
        lista = nodo.get(c["campo"], [])
        i = c.get("indice")
        if not isinstance(i, int) or not 0 <= i < len(lista):
            fallas.append("indice fuera de rango: %r" % i)
        elif lista[i] != c["texto_anterior"]:
            fallas.append("el texto anterior no es el vigente de %s[%d]" % (c["campo"], i))
    elif nodo.get(c.get("campo")) != c.get("texto_anterior"):
        fallas.append("el texto anterior no es el vigente de %s" % c.get("campo"))
    return fallas


def main(argv):
    global NODOS
    tanda = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    comprobar = "--comprobar" in argv
    if "--nodos" in argv:
        NODOS = Path(argv[argv.index("--nodos") + 1]).resolve()
    nodos, fallas = {}, []
    for c in tanda:
        ruta = NODOS / ("%s.json" % c.get("node_id"))
        if c.get("node_id") not in nodos:
            nodos[c.get("node_id")] = json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else None
        for f in validar(c, nodos[c.get("node_id")]):
            fallas.append("%s (%s): %s" % (c.get("id"), c.get("node_id"), f))
        if not fallas and nodos[c.get("node_id")] is not None:
            nodo = nodos[c["node_id"]]
            if c["campo"] in LISTAS:
                nodo[c["campo"]][c["indice"]] = c["texto_nuevo"]
            else:
                nodo[c["campo"]] = c["texto_nuevo"]
            registro = {k: c[k] for k in ("id", "fecha", "campo", "veredicto", "texto_anterior", "texto_nuevo", "cita", "decision")}
            if c["veredicto"] == "RESUMEN":
                # El texto viejo ya esta, identico, en notas_extraccion: se remite en vez de duplicarlo.
                del registro["texto_anterior"]
                registro["texto_anterior_en"] = "notas_extraccion"
            if c["campo"] in LISTAS:
                registro["indice"] = c["indice"]
            if c.get("auditoria"):
                registro["auditoria"] = c["auditoria"]
            if c.get("motivos"):
                # Un mismo texto puede corregirse por varias razones a la vez (voz, ingles, tildes): se declaran todas.
                registro["motivos"] = c["motivos"]
            nodo.setdefault("correcciones", []).append(registro)
    # LAS BARANDAS DE LA CASA (scripts/censo_duplicacion.py): una correccion no
    # puede dejar en el nodo una baranda que antes no tenia (por ejemplo, una sigla
    # como FDA u OSHA sin la formula de localizacion). Nace de la tanda fidelidad-t1,
    # que salio a produccion con una sigla sin localizar porque nadie la miraba.
    if not fallas:
        sys.path.insert(0, str(BASE / "scripts"))
        try:
            import censo_duplicacion
        except ImportError:
            censo_duplicacion = None
        if censo_duplicacion is not None:
            for nid, nodo in nodos.items():
                ruta = NODOS / ("%s.json" % nid)
                antes = censo_duplicacion.revisar_barandas(json.loads(ruta.read_text(encoding="utf-8")))
                # Se compara CUANTOS hallazgos tiene cada baranda antes y despues, no la cita exacta: una
                # correccion de solo tildes ("tu organizacion" a "tu organización") cambia la cita y no deja
                # ninguna baranda nueva (integracion del mundo 11, 28 sep 2026: la forja escribe sin tildes).
                cuenta = {}
                for b in antes:
                    cuenta[b["baranda"]] = cuenta.get(b["baranda"], 0) + 1
                despues = censo_duplicacion.revisar_barandas(nodo)
                por_baranda = {}
                for b in despues:
                    por_baranda.setdefault(b["baranda"], []).append(b)
                for baranda, hallazgos in por_baranda.items():
                    if len(hallazgos) > cuenta.get(baranda, 0):
                        fallas.append("%s: la correccion deja la baranda %s: %s" % (nid, baranda, hallazgos[-1].get("cita")))
    if fallas:
        print("TANDA RECHAZADA, no se escribio nada:")
        for f in fallas:
            print("  " + f)
        return 1
    if comprobar:
        print("TANDA VALIDA: %d correcciones en %d nodos (sin escribir)" % (len(tanda), len(nodos)))
        return 0
    for nid, nodo in nodos.items():
        (NODOS / ("%s.json" % nid)).write_text(json.dumps(nodo, ensure_ascii=False, indent=2), encoding="utf-8")
    print("TANDA APLICADA: %d correcciones en %d nodos" % (len(tanda), len(nodos)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
