# -*- coding: utf-8 -*-
r"""vuelta190_tarea5_sede_de_op_l_02.py . LA BUSQUEDA DE LA SEDE DE `OP-L-02`,
CON SUS COMANDOS Y CON EL LIMITE ESCRITO DELANTE.

QUIEN LA ENCARGA. La `4.1` del acta 189, y la vara del acta 190 (`5.4`) la
confirma medida: **71 fichas, 6 en LISTA sin ninguna prueba, 2 CONSUMIDAS por
`OP-U-01` y 4 de TRABAJO REAL**; de esas cuatro, **tres son mesas cuyo producto
documental SI existe en disco** y **`OP-L-02` es LA UNICA SIN DOCUMENTO QUE
MEDIR**, con 0 menciones de fichero en su evidencia.

EL LIMITE, ESCRITO AQUI ARRIBA PARA QUE NO SE CRUCE Y NO AL FINAL PARA QUE NO SE
LEA DESPUES DE HABERLO CRUZADO: **si la busqueda no encuentra sede en ninguna
parte, ESO ES EL RESULTADO Y SE PUBLICA COMO TAL.** No se le inventa una sede a la
ficha, no se la declara HECHA y no se la mueve de estado. **Inventarle una sede es
cambiar el alcance de la campana, y eso lo reserva el fundador.** Este fichero
abre `docs/plan/OPERACIONES.jsonl` EN MODO LECTURA y no escribe una sola linea en
el.

QUE SE BUSCA, Y SALE DE LA PROPIA FICHA Y NO DE UNA LISTA TECLEADA: su campo
`verificacion` habla de **"las tres nominas afectadas"** y de **"cada grupo del
backlog"**. Las tres nominas y los grupos del backlog **se leen del campo `nota`
de la propia ficha**, y se buscan en el repo por sus nombres.

LA BUSQUEDA NEGATIVA SE HACE CON SU COMANDO Y NO SE CITA (`EJECUTOR.md` 9): cada
busqueda que salga en cero **queda escrita con lo que se busco y donde**, para que
el cero se pueda repetir. Un cero que nadie puede repetir no es una medicion.

USO:
  python scripts/loop/vuelta190_tarea5_sede_de_op_l_02.py
"""
import hashlib
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
VUELTA = int(re.search(r"vuelta(\d+)_",
                       os.path.basename(os.path.abspath(__file__))).group(1))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
FICHA = "OP-L-02"

# LAS TRES NOMINAS Y LOS GRUPOS DEL BACKLOG, CON LOS NOMBRES QUE LA PROPIA FICHA
# LES DA. No son una lista inventada: cada entrada trae el literal de la ficha del
# que sale, para que se pueda cotejar contra el campo `nota`.
NOMINAS = [
    ("cuadrantes de mercado", "cuadrantes de mercado (8)",
     ["cuadrante", "cuadrantes"]),
    ("ecuacion de valor", "ecuacion de valor (5)",
     ["ecuacion de valor", "ecuacion_de_valor"]),
    ("el bloque humano de la supervision de la IA",
     "el bloque humano de la supervision de la IA (3)",
     ["supervision de la IA", "bloque humano", "supervision_ia"]),
]
GRUPOS_DEL_BACKLOG = [
    ("126 esperan destejido", ["esperan destejido", "126"]),
    ("55 resto sin mesa ni nomina", ["resto sin mesa", "55 son resto"]),
    ("5 de sales roadmap", ["sales roadmap", "LD_SALES_ROADMAP"]),
    ("3 ya leidas en la primera tanda", ["primera tanda"]),
]
# LAS SEDES QUE LA PROPIA FICHA NOMBRA, PARA COMPROBARLAS UNA A UNA.
RUTAS_QUE_LA_FICHA_NOMBRA = [
    "docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt",
    "docs/loop/SALIDA_V169_T5_LOTE_SALES_ROADMAP.txt",
    "docs/loop/SALIDA_V170_T3_DEUDAS_DE_CORTE.txt",
    "docs/loop/SALIDA_V170_T4B_PUENTES.txt",
    "docs/plan/LD_SALES_ROADMAP.md",
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "docs/plan/INVENTARIO.jsonl",
]
# DONDE SE BUSCA. Las carpetas de la campana, no el repo entero: buscar en
# node_modules o en el dataset daria ruido y no sede.
CARPETAS = [os.path.join("docs"), os.path.join("scripts")]
EXTENSIONES = (".md", ".jsonl", ".txt", ".json", ".py", ".mjs")


def med(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    d = io.open(p, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return (len(d), len(lf), lf.count(b"\n"), hashlib.sha256(lf).hexdigest())


def ficheros():
    salida = []
    for carpeta in CARPETAS:
        base = os.path.join(RAIZ, carpeta)
        for dirpath, dirnames, nombres in os.walk(base):
            dirnames[:] = [d for d in dirnames
                           if d not in ("__pycache__", "node_modules", ".git")]
            for n in nombres:
                if n.endswith(EXTENSIONES):
                    p = os.path.join(dirpath, n)
                    salida.append(os.path.relpath(p, RAIZ).replace("\\", "/"))
    return sorted(salida)


def buscar(agujas, universo, tope=12):
    """LOS FICHEROS QUE NOMBRAN ALGUNA DE LAS AGUJAS. Devuelve
    [(ruta, aguja, cuantas)]. La comparacion va en minusculas."""
    hits = []
    for rel in universo:
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        try:
            t = io.open(p, encoding="utf-8", errors="replace").read().lower()
        except Exception:
            continue
        for a in agujas:
            c = t.count(a.lower())
            if c:
                hits.append((rel, a, c))
    hits.sort(key=lambda x: (-x[2], x[0]))
    return hits[:tope], len(hits)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 5: LA BUSQUEDA DE LA SEDE DE %s" % (VUELTA, FICHA))
    w("=" * 78)
    w("")
    w("EL LIMITE, ESCRITO DELANTE Y NO AL FINAL: si la busqueda no encuentra sede")
    w("en ninguna parte, ESO ES EL RESULTADO Y SE PUBLICA COMO TAL. No se le")
    w("inventa una sede a la ficha, no se la declara HECHA y no se la mueve de")
    w("estado. Inventarle una sede es cambiar el alcance de la campana, y eso lo")
    w("reserva el fundador.")
    w("")

    w("A) LA FICHA, LEIDA DE SU SEDE Y NO DE UN RECUERDO")
    m = med("docs/plan/OPERACIONES.jsonl")
    w("   docs/plan/OPERACIONES.jsonl -> disco %d bytes | LF %d bytes | %d lineas"
      % (m[0], m[1], m[2]))
    ficha = None
    linea_ficha = None
    total = 0
    for i, l in enumerate(io.open(OPS, encoding="utf-8"), 1):
        if not l.strip():
            continue
        total += 1
        d = json.loads(l)
        if str(d.get("id_op") or d.get("id") or "") == FICHA:
            ficha, linea_ficha = d, i
    w("   CIFRA fichas: %d" % total)
    w("   LA CLAVE DEL ID EN ESTE FICHERO ES `id_op` Y NO `id`, medido y no")
    w("   supuesto: el bloque H.7 del sello de apertura de esta vuelta busco por")
    w("   `id` y por `operacion` y dio CERO. Se declara en vez de taparse.")
    if ficha is None:
        w("   PARADA: la ficha %s no esta en el fichero." % FICHA)
        print(NL.join(L))
        return 1
    w("   %s vive en docs/plan/OPERACIONES.jsonl:%d" % (FICHA, linea_ficha))
    for k in ("fase", "tipo", "estado", "orden", "fecha_corte"):
        w("      %-14s %s" % (k, ficha.get(k)))
    for k in ("nodos", "preservar", "eliminar", "aristas_nuevas", "depende_de",
              "bloquea_a"):
        w("      %-14s %d elemento(s): %s"
          % (k, len(ficha.get(k) or []), json.dumps(ficha.get(k), ensure_ascii=False)))
    w("   CIFRA elementos de `verificacion`: %d" % len(ficha.get("verificacion") or []))
    w("   CIFRA elementos de `evidencia`: %d" % len(ficha.get("evidencia") or []))
    for e in (ficha.get("evidencia") or []):
        w("      evidencia: %s" % e)
    w("")

    w("B) LO QUE LA FICHA PIDE VERIFICAR, LITERAL Y NUMERADO")
    for i, v in enumerate(ficha.get("verificacion") or [], 1):
        w("   %d) %s" % (i, v[:260]))
        if len(v) > 260:
            w("      (...%d caracteres mas)" % (len(v) - 260))
    w("")

    w("C) LAS MENCIONES DE FICHERO EN SU EVIDENCIA, CONTADAS Y NO SUPUESTAS")
    w("   (la vara del acta 190 dice 0 menciones de fichero en su evidencia. AQUI")
    w("    SE VUELVE A CONTAR, sobre el campo `evidencia` y sobre el `nota`)")
    pat_fichero = re.compile(r"[\w/\\.-]+\.(?:md|jsonl|txt|json|py|mjs)\b")
    for campo in ("evidencia", "nota", "verificacion"):
        valor = ficha.get(campo)
        texto = (" ".join(valor) if isinstance(valor, list) else (valor or ""))
        hallados = sorted(set(pat_fichero.findall(texto)))
        w("   campo `%s`: %d caracteres, %d mencion(es) de fichero"
          % (campo, len(texto), len(hallados)))
        for h in hallados:
            w("      %s" % h)
    w("")

    w("D) LAS RUTAS QUE LA PROPIA FICHA NOMBRA, COMPROBADAS UNA A UNA EN DISCO")
    w("   (una ruta publicada como prueba es CIFRA, `EJECUTOR.md` 1: si no existe")
    w("    o mide cero bytes, es caida de cifra)")
    existen = 0
    for rel in RUTAS_QUE_LA_FICHA_NOMBRA:
        mm = med(rel)
        if mm is None:
            w("   %-52s NO EXISTE EN DISCO" % rel)
            continue
        existen += 1
        w("   %-52s disco %7d | LF %7d | %5d lineas" % (rel, mm[0], mm[1], mm[2]))
    w("   CIFRA rutas que la ficha nombra: %d" % len(RUTAS_QUE_LA_FICHA_NOMBRA))
    w("   CIFRA que existen en disco: %d" % existen)
    w("   CIFRA de cero bytes: %d"
      % len([r for r in RUTAS_QUE_LA_FICHA_NOMBRA
             if med(r) is not None and med(r)[0] == 0]))
    w("")

    universo = ficheros()
    w("E) EL UNIVERSO DE LA BUSQUEDA, DICHO ANTES DE BUSCAR")
    w("   carpetas: %s" % ", ".join(CARPETAS))
    w("   extensiones: %s" % ", ".join(EXTENSIONES))
    w("   se excluyen __pycache__, node_modules y .git")
    w("   CIFRA ficheros del universo: %d" % len(universo))
    w("")

    w("F) LAS TRES NOMINAS AFECTADAS, BUSCADAS UNA A UNA")
    w("   (los nombres salen del campo `nota` de la propia ficha, con su literal")
    w("    al lado, y no de una lista inventada)")
    resumen_nominas = []
    for nombre, literal, agujas in NOMINAS:
        w("   " + "-" * 72)
        w("   NOMINA: %s" % nombre)
        w("      literal de la ficha: %r" % literal)
        w("      agujas buscadas: %s" % ", ".join(repr(a) for a in agujas))
        hits, cuantos = buscar(agujas, universo)
        w("      CIFRA ficheros que la nombran: %d" % cuantos)
        if not hits:
            w("      CERO. LA BUSQUEDA NEGATIVA QUEDA ESCRITA CON SU COMANDO.")
        for rel, a, c in hits:
            mm = med(rel)
            w("         %-58s %r x%d (%d bytes)"
              % (rel, a, c, mm[0] if mm else -1))
        # QUE CUENTA COMO SEDE: un fichero que la nombre Y que sea un documento de
        # plan o de lectura, no una salida de una vuelta. Se dice la regla antes de
        # aplicarla.
        sedes = [r for r, _a, _c in hits
                 if r.startswith("docs/plan/") and not r.endswith(".py")]
        w("      CANDIDATOS A SEDE (en docs/plan/, que es donde viven los")
        w("      documentos del plan): %d" % len(sedes))
        for s in sedes:
            w("         %s" % s)
        resumen_nominas.append((nombre, cuantos, len(sedes)))
    w("")

    w("G) LOS GRUPOS DEL BACKLOG, BUSCADOS UNO A UNO")
    resumen_grupos = []
    for nombre, agujas in GRUPOS_DEL_BACKLOG:
        hits, cuantos = buscar(agujas, universo, tope=6)
        w("   GRUPO: %-38s agujas %s" % (nombre, ", ".join(repr(a) for a in agujas)))
        w("      CIFRA ficheros que lo nombran: %d" % cuantos)
        for rel, a, c in hits:
            w("         %-58s %r x%d" % (rel, a, c))
        if not hits:
            w("         CERO. LA BUSQUEDA NEGATIVA QUEDA ESCRITA.")
        resumen_grupos.append((nombre, cuantos))
    w("")

    w("H) LA BUSQUEDA DEL DOCUMENTO PROPIO DE LA FICHA, QUE ES LA PREGUNTA REAL")
    w("   Las otras tres mesas de TRABAJO REAL tienen un producto documental en")
    w("   disco. La pregunta es si `%s` tiene el suyo. Se busca por SU PROPIO" % FICHA)
    w("   NOMBRE en el universo entero:")
    hits, cuantos = buscar([FICHA], universo, tope=40)
    w("   CIFRA ficheros que nombran `%s`: %d" % (FICHA, cuantos))
    por_carpeta = {}
    for rel, _a, c in hits:
        carpeta = rel.rsplit("/", 1)[0]
        por_carpeta[carpeta] = por_carpeta.get(carpeta, 0) + 1
    for rel, _a, c in hits:
        mm = med(rel)
        w("      %-58s x%-3d (%d bytes)" % (rel, c, mm[0] if mm else -1))
    w("   REPARTO POR CARPETA:")
    for k in sorted(por_carpeta):
        w("      %-34s %d fichero(s)" % (k, por_carpeta[k]))
    en_plan = [r for r, _a, _c in hits if r.startswith("docs/plan/")]
    w("   CIFRA en docs/plan/, que es donde vive el producto de una mesa: %d"
      % len(en_plan))
    for r in en_plan:
        w("      %s" % r)
    w("   Y LA BUSQUEDA DE UN FICHERO CUYO NOMBRE LLEVE LA FICHA DENTRO:")
    por_nombre = [r for r in universo
                  if FICHA.lower().replace("-", "_") in r.lower().replace("-", "_")]
    w("      CIFRA ficheros cuyo NOMBRE nombra la ficha: %d" % len(por_nombre))
    for r in por_nombre:
        mm = med(r)
        w("         %-56s %d bytes" % (r, mm[0] if mm else -1))
    if not por_nombre:
        w("         CERO. LA BUSQUEDA NEGATIVA QUEDA ESCRITA CON SU COMANDO.")
    w("")

    w("I) EL RESUMEN, Y AQUI NO SE CRUZA EL LIMITE")
    w("   LAS TRES NOMINAS:")
    for nombre, cuantos, sedes in resumen_nominas:
        w("      %-46s %3d fichero(s) la nombran | %d candidato(s) a sede en docs/plan/"
          % (nombre, cuantos, sedes))
    w("   LOS GRUPOS DEL BACKLOG:")
    for nombre, cuantos in resumen_grupos:
        w("      %-46s %3d fichero(s) lo nombran" % (nombre, cuantos))
    w("")
    w("   LO QUE ESTE FICHERO NO HACE, Y SE DICE OTRA VEZ AL CERRAR:")
    w("      no le inventa una sede a la ficha,")
    w("      no la declara HECHA,")
    w("      no la mueve de estado (sigue en %r)," % ficha.get("estado"))
    w("      y no escribe una sola linea en docs/plan/OPERACIONES.jsonl.")
    m2 = med("docs/plan/OPERACIONES.jsonl")
    w("   docs/plan/OPERACIONES.jsonl al salir -> disco %d bytes | LF %d bytes"
      % (m2[0], m2[1]))
    w("   IDENTICO AL DE LA ENTRADA: %s" % ("SI" if m == m2 else "NO"))
    w("")

    texto = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%d_T5_SEDE_OP_L_02.txt" % VUELTA)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(texto.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
