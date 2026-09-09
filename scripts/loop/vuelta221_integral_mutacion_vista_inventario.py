# -*- coding: utf-8 -*-
r"""vuelta221_integral_mutacion_vista_inventario.py . EL CASO ROJO POR MUTACION
DE LA VISTA IMPRESA DEL INVENTARIO (`scripts/loop/vista_del_inventario.py`),
fabricada en la AUDITORIA INTEGRAL del 9 sep 2026 (PASO 1.a, item 5, clausula
idx 3 de `OP-I-01`).

EL NUMERO 221 ES EL NUMERO DE CENSO QUE SIGUE A LA VUELTA 220, PARA QUE LA
BATERIA LO VEA; la auditoria integral NO es una vuelta del bucle.

QUE PRUEBA. Que `--comprobar` MUERDE: que la vista queda ROJA cuando el archivo
cambia por debajo, cuando alguien toca el bloque a mano, o cuando el bloque no
esta; y que sin mutar nada sale VERDE. TODAS LAS MUTACIONES SON EN MEMORIA
(la lista de entradas y el texto de la pagina son copias); CERO ESCRITURAS,
comprobado con `git status --porcelain -- docs/plan/` antes y despues.

LOS CASOS:
  (0) CONTRAPRUEBA: la pagina de hoy contra el archivo de hoy: VERDE.
  (A) EL ARCHIVO CRECE: se anade en memoria un acto vigente. El bloque fresco
      cambia (el volumen y la tabla por tamano) y `comprobar` cae.
  (B) UNA ENTRADA CAMBIA DE ESTADO: el primer acto vigente CERRADO pasa a
      ABIERTO en memoria. Cae.
  (C) LA PAGINA SE TOCA A MANO: al bloque de la pagina se le cambia una cifra
      (la primera fila del volumen). Cae.
  (D) EL BLOQUE NO ESTA: se quita de la pagina en memoria. Cae nombrando las
      marcas.
  (E) LAS CIFRAS DEL BLOQUE SON LAS DEL ARCHIVO: el volumen impreso por tipo se
      coteja contra el conteo directo de la lista; con el esperado mutado, cae.

USO:  python scripts/loop/vuelta221_integral_mutacion_vista_inventario.py
Escribe docs/loop/SALIDA_integral_MUTACION_VISTA_INVENTARIO.txt.
"""
import collections
import copy
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import vista_del_inventario as V   # noqa: E402

RAIZ = V.RAIZ
DESTINO = os.path.join(RAIZ, "docs", "loop", "SALIDA_integral_MUTACION_VISTA_INVENTARIO.txt")


def porcelain():
    r = subprocess.run(["git", "status", "--porcelain", "--", "docs/plan/"], cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", "replace")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    fallos = 0
    antes = porcelain()
    entradas, sha = V.leer()
    pagina = io.open(V.PAGINA, encoding="utf-8").read()
    w("ARNES DE MUTACION DE LA VISTA IMPRESA DEL INVENTARIO (auditoria integral, 9 sep 2026)")
    w("sujeto vivo: scripts/loop/vista_del_inventario.py")
    w("CIFRA entradas del archivo: %d | sha %s | CIFRA bytes de la pagina: %d" % (len(entradas), sha, len(pagina.encode("utf-8"))))
    w("")

    ok0, m0 = V.comprobar(pagina, entradas, sha)
    w("(0) CONTRAPRUEBA sin mutar: %s. %s" % ("VERDE" if ok0 else "ROJO", m0))
    if not ok0:
        fallos += 1

    corte = max(str(e.get("fecha_corte") or "") for e in entradas if e.get("tipo") == "acto")
    e_mut = copy.deepcopy(entradas)
    e_mut.append({"tipo": "acto", "nombre": "acto_fabricado_integral", "miembros": ["a_integral", "b_integral"],
                  "forma": "componente conexa de la relacion gemelo (banco 9.24)", "cobertura": "1 de 1 pares leidos",
                  "estado": "repite, acto CERRADO listo para fundir", "operaciones": [], "fecha_corte": corte, "nota": "mutante"})
    okA, mA = V.comprobar(pagina, e_mut, sha)
    w("(A) EL ARCHIVO CRECE EN MEMORIA (un acto vigente mas): %s -> %s. %s" % ("VERDE" if okA else "ROJO", "CAE" if not okA else "NO CAE", mA))
    if okA:
        fallos += 1

    e_mut = copy.deepcopy(entradas)
    primero = next(e for e in e_mut if e.get("tipo") == "acto" and str(e.get("fecha_corte")) == corte and "CERRADO" in str(e.get("estado")))
    primero["estado"] = "repite, acto ABIERTO"
    okB, mB = V.comprobar(pagina, e_mut, sha)
    w("(B) EL ACTO %r PASA DE CERRADO A ABIERTO EN MEMORIA: %s -> %s. %s" % (primero.get("nombre"), "VERDE" if okB else "ROJO", "CAE" if not okB else "NO CAE", mB))
    if okB:
        fallos += 1

    bloque = V.bloque_de(pagina) or ""
    m = re.search(r"\| \*\*dominio\*\* \| \*\*(\d+)\*\* \|", bloque)
    if not m:
        w("(C) SIN SUJETO: el bloque no trae la fila del volumen de dominio. NO CUENTA COMO VERDE.")
        fallos += 1
    else:
        tocado = bloque.replace(m.group(0), m.group(0).replace("**%s**" % m.group(1), "**%d**" % (int(m.group(1)) + 1)), 1)
        pag_mut = pagina.replace(bloque, tocado, 1)
        okC, mC = V.comprobar(pag_mut, entradas, sha)
        w("(C) LA PAGINA SE TOCA A MANO (dominio %s -> %d): %s -> %s. %s" % (m.group(1), int(m.group(1)) + 1, "VERDE" if okC else "ROJO", "CAE" if not okC else "NO CAE", mC))
        if okC:
            fallos += 1

    pag_sin = pagina.replace(bloque, "", 1)
    okD, mD = V.comprobar(pag_sin, entradas, sha)
    w("(D) EL BLOQUE NO ESTA: %s -> %s. %s" % ("VERDE" if okD else "ROJO", "CAE" if not okD else "NO CAE", mD))
    if okD or "no trae el bloque" not in mD:
        fallos += 1

    w("(E) LAS CIFRAS DEL VOLUMEN IMPRESO CONTRA EL CONTEO DIRECTO DE LA LISTA")
    fresco = V.imprimir(entradas, sha)
    conteo = collections.Counter(e.get("tipo") for e in entradas)
    for t in V.TIPOS:
        mm = re.search(r"\| \*\*%s\*\* \| \*\*(\d+)\*\* \|" % re.escape(t), fresco)
        impreso = int(mm.group(1)) if mm else None
        esperado = conteo.get(t, 0)
        w("      %-15s impreso %s | contado %d: %s | esperado mutado %d: %s"
          % (t, impreso, esperado, "PASA" if impreso == esperado else "FALLA", esperado + 1, "CAE" if impreso != esperado + 1 else "NO CAE"))
        if impreso != esperado or impreso == esperado + 1:
            fallos += 1

    despues = porcelain()
    w("")
    w("CERO ESCRITURAS: porcelain antes == despues: %s" % (antes == despues))
    if antes != despues:
        fallos += 1
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = "\n".join(L) + "\n"
    io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (DESTINO, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
