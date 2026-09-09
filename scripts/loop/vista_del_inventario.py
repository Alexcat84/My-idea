# -*- coding: utf-8 -*-
r"""vista_del_inventario.py . LA VISTA HUMANA DEL INVENTARIO, IMPRESA DESDE
`docs/plan/INVENTARIO.jsonl` Y NUNCA TECLEADA. NOMBRE ESTABLE, SIN NUMERO DE
VUELTA.

POR QUE NACE. La clausula idx 3 de `OP-I-01` (*el inventario se recomputa entero
con el disparador de 08_VERIFICACION*) llevaba A MEDIAS desde la vuelta 214
porque `docs/plan/10_INVENTARIO.md` declaraba en su linea 19 *LA TABLA NO SE
REGENERA AQUI, A PROPOSITO*, y 26 ficheros la nombran. La auditoria integral
del 9 sep 2026 midio que TODO lo que la vista tabula vive en el archivo (seis
tipos: dominio, racimo, acto, familia_de_ids, figura y defecto, con sus campos
forma, cobertura, estado, operaciones, fecha_corte y nota), y por decision del
fundador (PASO 1.a, item 5) la vista se FABRICA como instrumento: lo que se
puede imprimir se imprime, y la prosa escrita a mano (avisos, huecos nombrados,
reconciliaciones) NO se regenera ni se borra: queda arriba, con sus fechas.

QUE HACE, EN TRES MODOS:
  (sin bandera)   imprime el bloque por consola;
  --escribir      mete el bloque en `docs/plan/10_INVENTARIO.md` entre las marcas
                  `<!-- VISTA IMPRESA: INICIO -->` y `<!-- VISTA IMPRESA: FIN -->`
                  (si no existen, lo anexa al final; si existen, lo sustituye);
  --comprobar     el caso rojo: ROJO (exit 1) si la pagina no trae el bloque o
                  si el bloque de la pagina NO ES IDENTICO al que hoy se
                  imprimiria del archivo. Es el disparador del recomputo hecho
                  guarda: cuando el archivo cambia, la vista queda ROJA hasta
                  que alguien la vuelva a imprimir.

TODO ES PURO SOBRE UNA LISTA DE ENTRADAS: `imprimir(entradas, sha)` no toca el
disco, para que el caso rojo se pruebe por mutacion en memoria
(`vuelta221_integral_mutacion_vista_inventario.py`).

LO QUE NO HACE: no mide nada nuevo, no lee el grafo, no toca el archivo y no
reescribe ni una linea de la prosa de la pagina fuera de sus dos marcas.
"""
import argparse
import collections
import hashlib
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INVENTARIO = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
PAGINA = os.path.join(RAIZ, "docs", "plan", "10_INVENTARIO.md")
INICIO = "<!-- VISTA IMPRESA: INICIO -->"
FIN = "<!-- VISTA IMPRESA: FIN -->"
TIPOS = ("dominio", "racimo", "acto", "familia_de_ids", "figura", "defecto")


def leer(ruta=INVENTARIO):
    raw = io.open(ruta, "rb").read()
    entradas = [json.loads(l) for l in raw.decode("utf-8").splitlines() if l.strip()]
    return entradas, hashlib.sha256(raw).hexdigest()[:16]


def _celda(x, n=90):
    s = str(x if x is not None else "")
    s = s.replace("|", "/").replace("\r", " ").replace("\n", " ")
    return s if len(s) <= n else s[:n - 3] + "..."


def _estado_corto(e):
    """CERRADO o ABIERTO segun la PRIMERA de las dos palabras que aparece en el
    campo: el texto nuevo de una correccion va delante y el viejo detras
    (un estado dice "acto CERRADO (...). El texto viejo ...: acto ABIERTO", y es
    CERRADO). Lo midio el arnes de mutacion de la integral, caso B."""
    s = str(e.get("estado") or "")
    ia, ic = s.find("ABIERTO"), s.find("CERRADO")
    if ia < 0 and ic < 0:
        return _celda(s, 40)
    if ia < 0:
        return "CERRADO"
    if ic < 0:
        return "ABIERTO"
    return "CERRADO" if ic < ia else "ABIERTO"


def imprimir(entradas, sha):
    L = []
    w = L.append
    por_tipo = collections.OrderedDict((t, [e for e in entradas if e.get("tipo") == t]) for t in TIPOS)
    otros = [e for e in entradas if e.get("tipo") not in TIPOS]
    actos = por_tipo["acto"]
    corte = max((str(e.get("fecha_corte") or "") for e in actos), default="")
    vigentes = [e for e in actos if str(e.get("fecha_corte") or "") == corte]
    superadas = [e for e in actos if str(e.get("fecha_corte") or "") != corte]

    w(INICIO)
    w("")
    w("## LA VISTA IMPRESA DESDE EL ARCHIVO")
    w("")
    w("**Impresa por `scripts/loop/vista_del_inventario.py` desde `docs/plan/INVENTARIO.jsonl`,")
    w("y NUNCA editada a mano: lo que este bloque dice sale del archivo, fila por fila, con la")
    w("`fecha_corte` de cada entrada. Si el archivo cambia, `--comprobar` pone este bloque en ROJO")
    w("hasta que se vuelva a imprimir. La prosa de arriba (avisos, huecos nombrados y")
    w("reconciliaciones) es de mano humana y no se regenera.**")
    w("")
    w("CIFRA entradas leidas: %d | sha256 del archivo (16 hex): `%s` | corte vigente de los actos: %s"
      % (len(entradas), sha, corte or "(sin actos)"))
    w("")
    w("### EL VOLUMEN, contado del archivo")
    w("")
    w("| tipo | entradas | de ellas |")
    w("|---|---:|---|")
    for t, es in por_tipo.items():
        extra = ""
        if t == "acto":
            extra = "%d vigentes al corte %s y %d superadas" % (len(vigentes), corte, len(superadas))
        w("| **%s** | **%d** | %s |" % (t, len(es), extra))
    w("| **TOTAL** | **%d** | %s |" % (len(entradas), ("%d de tipo fuera de los seis" % len(otros)) if otros else ""))
    w("")

    w("### POR DOMINIO")
    w("")
    w("| dominio | forma | cobertura | estado | nota | fecha_corte |")
    w("|---|---|---|---|---|---|")
    for e in sorted(por_tipo["dominio"], key=lambda x: str(x.get("nombre"))):
        w("| **%s** | %s | %s | %s | %s | %s |" % (_celda(e.get("nombre"), 40), _celda(e.get("forma"), 40),
                                                _celda(e.get("cobertura"), 60), _celda(e.get("estado"), 40),
                                                _celda(e.get("nota"), 110), e.get("fecha_corte")))
    w("")

    w("### LOS ACTOS DEL CORTE VIGENTE (%s)" % corte)
    w("")
    cerrados = [e for e in vigentes if _estado_corto(e) == "CERRADO"]
    abiertos = [e for e in vigentes if _estado_corto(e) == "ABIERTO"]
    nodos = sum(len(e.get("miembros") or []) for e in vigentes)
    w("| | cifra |")
    w("|---|---:|")
    w("| actos | **%d** |" % len(vigentes))
    w("| nodos implicados (suma de miembros) | **%d** |" % nodos)
    w("| CERRADOS | **%d** |" % len(cerrados))
    w("| ABIERTOS | **%d** |" % len(abiertos))
    w("| ni CERRADO ni ABIERTO en su estado | **%d** |" % (len(vigentes) - len(cerrados) - len(abiertos)))
    w("")
    w("**POR TAMANO:**")
    w("")
    w("| miembros | actos |")
    w("|---:|---:|")
    tam = collections.Counter(len(e.get("miembros") or []) for e in vigentes)
    for k in sorted(tam):
        w("| %d | %d |" % (k, tam[k]))
    w("")
    w("**LOS SEIS MAYORES:**")
    w("")
    w("| miembros | el acto | estado | operaciones |")
    w("|---:|---|---|---|")
    for e in sorted(vigentes, key=lambda x: (-len(x.get("miembros") or []), str(x.get("nombre"))))[:6]:
        w("| %d | `%s` | %s | %s |" % (len(e.get("miembros") or []), _celda(e.get("nombre"), 60),
                                       _estado_corto(e), ", ".join(e.get("operaciones") or [])))
    w("")

    w("### LOS RACIMOS")
    w("")
    w("| racimo | miembros | forma | cobertura | estado | fecha_corte |")
    w("|---|---:|---|---|---|---|")
    for e in por_tipo["racimo"]:
        w("| **%s** | %d | %s | %s | %s | %s |" % (_celda(e.get("nombre"), 50), len(e.get("miembros") or []),
                                                  _celda(e.get("forma"), 70), _celda(e.get("cobertura"), 50),
                                                  _celda(e.get("estado"), 90), e.get("fecha_corte")))
    w("")

    fams = por_tipo["familia_de_ids"]
    w("### LAS FAMILIAS DE IDS")
    w("")
    w("CIFRA familias: %d | CIFRA ids en ellas: %d" % (len(fams), sum(len(e.get("miembros") or []) for e in fams)))
    w("")
    w("| miembros | familias |")
    w("|---:|---:|")
    tf = collections.Counter(len(e.get("miembros") or []) for e in fams)
    for k in sorted(tf, reverse=True):
        w("| %d | %d |" % (k, tf[k]))
    w("")
    w("**LAS CUATRO MAYORES:**")
    w("")
    w("| familia | ids | estado | operaciones | fecha_corte |")
    w("|---|---|---|---|---|")
    for e in sorted(fams, key=lambda x: (-len(x.get("miembros") or []), str(x.get("nombre"))))[:4]:
        w("| `%s` | %s | %s | %s | %s |" % (_celda(e.get("nombre"), 50), ", ".join("`%s`" % m for m in (e.get("miembros") or [])),
                                            _celda(e.get("estado"), 60), ", ".join(e.get("operaciones") or []), e.get("fecha_corte")))
    w("")

    w("### LAS FIGURAS")
    w("")
    w("| figura | ejemplares (cobertura) | estado | fecha_corte |")
    w("|---|---|---|---|")
    for e in por_tipo["figura"]:
        w("| **%s** | %s | %s | %s |" % (_celda(e.get("nombre"), 60), _celda(e.get("cobertura"), 60),
                                         _celda(e.get("estado"), 60), e.get("fecha_corte")))
    w("")

    w("### LOS DEFECTOS")
    w("")
    w("| defecto | cuantos (cobertura) | estado | operaciones | fecha_corte |")
    w("|---|---|---|---|---|")
    for e in por_tipo["defecto"]:
        w("| **%s** | %s | %s | %s | %s |" % (_celda(e.get("nombre"), 60), _celda(e.get("cobertura"), 40),
                                              _celda(e.get("estado"), 70), ", ".join("`%s`" % o for o in (e.get("operaciones") or [])),
                                              e.get("fecha_corte")))
    w("")
    w(FIN)
    return "\n".join(L) + "\n"


def bloque_de(texto):
    """El bloque entre marcas de una pagina, o None si no lo trae entero."""
    i = texto.find(INICIO)
    j = texto.find(FIN)
    if i < 0 or j < 0 or j < i:
        return None
    return texto[i:j + len(FIN)] + "\n"


def con_bloque(texto, bloque):
    """La pagina con el bloque sustituido o anexado. PURA."""
    viejo = bloque_de(texto)
    if viejo is not None:
        i = texto.find(INICIO)
        return texto[:i] + bloque + texto[i + len(viejo):]
    sep = "" if texto.endswith("\n\n") else ("\n" if texto.endswith("\n") else "\n\n")
    return texto + sep + bloque


def comprobar(texto_pagina, entradas, sha):
    """(ok, motivo). PURA."""
    en_pagina = bloque_de(texto_pagina)
    if en_pagina is None:
        return False, "la pagina no trae el bloque entre %r y %r" % (INICIO, FIN)
    fresco = imprimir(entradas, sha)
    if en_pagina != fresco:
        a = en_pagina.splitlines()
        b = fresco.splitlines()
        n = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
        return False, ("el bloque de la pagina NO es identico al impreso hoy del archivo: primera "
                       "linea distinta %d de %d (pagina) contra %d (fresco)" % (n + 1, len(a), len(b)))
    return True, "el bloque de la pagina es identico al impreso hoy del archivo (%d lineas)" % len(fresco.splitlines())


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    ap.add_argument("--comprobar", action="store_true")
    a = ap.parse_args()
    entradas, sha = leer()
    if a.comprobar:
        texto = io.open(PAGINA, encoding="utf-8").read()
        ok, motivo = comprobar(texto, entradas, sha)
        print("VISTA IMPRESA DEL INVENTARIO, --comprobar: %s. %s" % ("VERDE" if ok else "ROJO", motivo))
        return 0 if ok else 1
    bloque = imprimir(entradas, sha)
    if a.escribir:
        texto = io.open(PAGINA, encoding="utf-8").read()
        nuevo = con_bloque(texto, bloque)
        io.open(PAGINA, "w", encoding="utf-8", newline="\n").write(nuevo)
        print("ESCRITO el bloque en %s (%d lineas, %d bytes de bloque)" % (PAGINA, len(bloque.splitlines()), len(bloque.encode("utf-8"))))
        return 0
    print(bloque)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
