# -*- coding: utf-8 -*-
"""vuelta131_grupos_por_titulo.py . TAREA 3.a de la vuelta 131: revoca la
regla vieja de prefijo estricto sobre la CADENA ENTERA del campo `fuente`
(la de la vuelta 130), que se comio a Hugos (acta 130, 4.5: el recorte de
importacion corta EL TITULO A 31 CARACTERES EXACTOS y el sufijo " - Autor"
va DETRAS, asi que el prefijo sobre la cadena entera no puede cazar un
truncamiento con autor).

LA REGLA NUEVA. Cada grafia se parte en TITULO (el segmento ANTES del
primer " - ") y RESTO (lo que sigue, tipicamente el autor). Se unen dos
grafias cuando:
  (1) el titulo de una es PREFIJO ESTRICTO del titulo de la otra, Y
  (2) el titulo corto tiene 20 caracteres o mas, Y
  (3) el RESTO no las separa: son iguales, o al menos uno de los dos esta
      vacio (grafia sin autor declarado). Si los dos RESTO son distintos y
      NINGUNO esta vacio, NO se unen: son libros distintos con un titulo
      parecido, no el mismo libro truncado.
La condicion (3) no la pide la letra del encargo de forma explicita, pero
sin ella la regla fundiria libros distintos por coincidencia de titulo, que
es justo lo que el caso NEGATIVO de abajo exige que NO pase: se deja
escrita en el codigo porque el caso negativo la necesita para dar rojo.

RAMAL (xiii) (acta 130, 4.5): la regla se prueba contra el caso que la
propia operacion documenta ANTES de correr sobre el censo real.

  CASO POSITIVO: tiene que unir
    'Essentials of Supply Chain Mana - Michael H. Hugos' (titulo len=31)
  con
    'Essentials of Supply Chain Management - Michael H. Hugos'
  el caso probado de OP-S-11 (05_SANEO.md) y el que la regla vieja perdia
  (prefijo sobre la cadena entera: False. prefijo sobre el titulo: True).

  CASO NEGATIVO: fabrica un par con la MISMA relacion de prefijo de titulo
  (titulo corto >= 20 caracteres) pero RESTO distinto y no vacio, y verifica
  que NO se unen: dos libros de autor distinto no son la misma obra
  truncada.

Salida: docs/loop/SALIDA_V131_3A_GRUPOS_POR_TITULO.txt

Uso:
  python scripts/loop/vuelta131_grupos_por_titulo.py
"""
import glob
import json
import os
import sys
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V131_3A_GRUPOS_POR_TITULO.txt")


def titulo_de(grafia):
    return grafia.split(" - ", 1)[0].strip()


def resto_de(grafia):
    partes = grafia.split(" - ", 1)
    return partes[1].strip() if len(partes) > 1 else ""


def prefijo_titulo_une(a, b):
    """True si la regla de titulo (con guarda de RESTO) une a y b."""
    if a == b:
        return False
    ta, tb = titulo_de(a), titulo_de(b)
    if ta == tb:
        return False
    corto = ta if len(ta) <= len(tb) else tb
    if not (tb.startswith(ta) or ta.startswith(tb)):
        return False
    if len(corto) < 20:
        return False
    ra, rb = resto_de(a), resto_de(b)
    if ra and rb and ra != rb:
        return False
    return True


def prefijo_cadena_entera_une(a, b):
    """La regla VIEJA de la vuelta 130, sobre la cadena entera: se
    conserva como base porque el encargo de 3.c pide poder distinguir
    'cadena entera' de 'titulo' como motivo por fila."""
    return a != b and (b.startswith(a) or a.startswith(b))


def correr_casos_de_prueba():
    positivo_a = "Essentials of Supply Chain Mana - Michael H. Hugos"
    positivo_b = "Essentials of Supply Chain Management - Michael H. Hugos"
    assert len(titulo_de(positivo_a)) == 31, titulo_de(positivo_a)
    ok_pos = prefijo_titulo_une(positivo_a, positivo_b)
    assert ok_pos is True, "CASO POSITIVO FALLO: la regla no une el caso Hugos"

    negativo_a = "The Complete Guide to Something Wonderful - Autor Primero"
    negativo_b = "The Complete Guide to Something Wonderful and More - Autor Segundo"
    assert titulo_de(negativo_b).startswith(titulo_de(negativo_a))
    assert len(titulo_de(negativo_a)) >= 20
    ok_neg = prefijo_titulo_une(negativo_a, negativo_b)
    assert ok_neg is False, "CASO NEGATIVO FALLO: la regla fundio dos autores distintos"

    return ok_pos, ok_neg


def cargar_censo():
    censo = Counter()
    for p in sorted(glob.glob(os.path.join(NODOS, "*.json"))):
        d = json.loads(open(p, encoding="utf-8").read())
        if d.get("deprecado"):
            continue
        fu = d.get("fuente")
        if not fu:
            continue
        primera = fu.split("|")[0].strip()
        censo[primera] += 1
    return censo


class UnionFind:
    def __init__(self, items):
        self.padre = {x: x for x in items}

    def find(self, x):
        while self.padre[x] != x:
            x = self.padre[x]
        return x

    def une(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.padre[rb] = ra


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    ok_pos, ok_neg = correr_casos_de_prueba()

    censo = cargar_censo()
    grafias = sorted(censo.keys())

    uf = UnionFind(grafias)
    for a in grafias:
        for b in grafias:
            if prefijo_cadena_entera_une(a, b):
                uf.une(a, b)
    grupos_base = len({uf.find(g) for g in grafias})

    pares_titulo_nuevos = []
    for a in grafias:
        for b in grafias:
            if prefijo_titulo_une(a, b):
                if uf.find(a) != uf.find(b):
                    pares_titulo_nuevos.append((a, b))
                uf.une(a, b)
    grupos_tras_titulo = len({uf.find(g) for g in grafias})

    grupos = {}
    for g in grafias:
        grupos.setdefault(uf.find(g), []).append(g)

    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write("CASO POSITIVO (Hugos, titulo len=31): UNE = %s\n" % ok_pos)
        fh.write("CASO NEGATIVO (autores distintos, titulo len>=20): UNE = %s (tiene que ser False)\n\n" % ok_neg)
        fh.write("GRUPOS con la regla VIEJA (prefijo sobre cadena entera, vuelta 130): %d\n" % grupos_base)
        fh.write("GRUPOS anadiendo la regla NUEVA (prefijo sobre TITULO, >=20 chars, guarda de RESTO): %d\n" % grupos_tras_titulo)
        fh.write("COLAPSOS ADICIONALES QUE GANA LA REGLA DEL TITULO: %d\n\n" % (grupos_base - grupos_tras_titulo))
        fh.write("PARES NUEVOS QUE SOLO LA REGLA DE TITULO UNE (no unidos por cadena entera):\n")
        for a, b in pares_titulo_nuevos:
            fh.write("  %s  <->  %s\n" % (a, b))
        fh.write("\nGRUPOS CON 2 O MAS MIEMBROS (canonica = grafia mas larga del grupo):\n")
        multi = {r: m for r, m in grupos.items() if len(m) > 1}
        for r in sorted(multi, key=lambda r: -sum(censo[m] for m in multi[r])):
            miembros = multi[r]
            canonica = max(miembros, key=len)
            fh.write("  CANONICA: %s\n" % canonica)
            for m in sorted(miembros, key=len):
                fh.write("    %d\t%s\n" % (censo[m], m))
        fh.write("\nTOTAL grafias: %d\n" % len(grafias))
        fh.write("TOTAL grupos (incluye singletons): %d\n" % grupos_tras_titulo)
        fh.write("TOTAL grupos con 2 o mas miembros: %d\n" % len(multi))

    print("caso positivo (Hugos) UNE: %s" % ok_pos)
    print("caso negativo (autores distintos) UNE: %s (tiene que ser False)" % ok_neg)
    print("grupos base (cadena entera, vuelta 130): %d" % grupos_base)
    print("grupos tras anadir regla de titulo: %d" % grupos_tras_titulo)
    print("colapsos adicionales: %d" % (grupos_base - grupos_tras_titulo))
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
