# -*- coding: utf-8 -*-
r"""_gen_v204_cierre.py . GENERA scripts/loop/_v204_cierre_mediciones.py COMO
CLON DECLARADO DE scripts/loop/_v203_cierre_mediciones.py, CON SU CIFRA DE
difflib AL LADO.

Cambia la constante de vuelta, los prefijos de los ficheros propios, las dos
glosas que eran de la 203 y NADA MAS, y anade UN BLOQUE NUEVO: el `K`, que es el
`numstat` de las TRES SEDES DEL AUDITOR contra el HEAD de apertura, que es lo que
la TAREA 0 del encargo obliga a publicar en la seccion 4.
"""
import difflib
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FUENTE = os.path.join(RAIZ, "scripts", "loop", "_v203_cierre_mediciones.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop", "_v204_cierre_mediciones.py")

CAMBIOS = [
    ("VUELTA = 203", "VUELTA = 204", 1),
    ('r"""_v203_cierre_mediciones.py . EL CIERRE DE LA VUELTA 203: CORRE EL CICLO',
     'r"""_v204_cierre_mediciones.py . EL CIERRE DE LA VUELTA 204: CORRE EL CICLO',
     1),
    ('mios = sorted(n for n in os.listdir(AQUI) if n.startswith("_v203_")'
     + NL + '              or n.startswith("_gen_v203_") or n.startswith("vuelta203_"))',
     'mios = sorted(n for n in os.listdir(AQUI) if n.startswith("_v204_")'
     + NL + '              or n.startswith("_gen_v204_") or n.startswith("vuelta204_"))',
     1),
    ('w("   LA UNICA ESCRITURA EN docs/plan/ DE ESTA VUELTA ES LA LINEA 41 DE")'
     + NL + 'w("   OPERACIONES.jsonl, y esa fila ya esta COMMITEADA, por eso el numstat")'
     + NL + 'w("   contra el arbol sale en cero.")',
     'w("   ESTA VUELTA NO ESCRIBIO NI UNA LINEA EN docs/plan/, Y POR ESO EL CERO")'
     + NL + 'w("   NO ES DE ARBOL LIMPIO DESPUES DE COMMITEAR SINO DE NO HABER TOCADO")'
     + NL + 'w("   NADA: las TAREAS 2, 3 y 4 LEEN esas sedes y ninguna las abre en modo")'
     + NL + 'w("   escritura. La unica sede movida de la campana es docs/PENDIENTES.md.")',
     1),
    ('for rel in ("docs/PENDIENTES.md", "docs/plan/OPERACIONES.jsonl",'
     + NL + '            "docs/loop/REPORTE.md"):',
     'for rel in ("docs/PENDIENTES.md", "docs/plan/OPERACIONES.jsonl",'
     + NL + '            "docs/plan/INVENTARIO.jsonl",'
     + NL + '            "docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl",'
     + NL + '            "docs/loop/RECOMPUTO_V169.jsonl",'
     + NL + '            "docs/loop/REPORTE.md"):',
     1),
]

BLOQUE_K = '''w("K) LA TAREA 0: LAS TRES SEDES DEL AUDITOR, CONTRA EL HEAD DE APERTURA")
w("   ES LA PIEZA QUE EL ENCARGO OBLIGA A PUBLICAR EN LA SECCION 4, Y LAS TRES")
w("   TIENEN QUE DAR 0. El HEAD de apertura se LEE del sello y no se teclea.")
_h = io.open(os.path.join(LOOP, "SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA),
             encoding="utf-8").read().strip()
w("   HEAD de apertura, leido de SALIDA_V%d_HEAD_APERTURA.txt: %s" % (VUELTA, _h))
for _sede in ("docs/loop/PROMPT_SIGUIENTE.md", "docs/loop/ACTA_AUDITOR.md",
              "docs/loop/PARA_ALEXIS.md"):
    _c, _o = correr(["git", "diff", "--numstat", _h, "--", _sede])
    _f = [x for x in _o.split(NL) if PATRON_FILA_NUMSTAT.match(x)]
    _existe = os.path.isfile(os.path.join(RAIZ, _sede))
    w("   CIFRA filas de numstat de %-34s %d" % (_sede, len(_f)))
    for x in _f:
        w("      %s" % x.strip())
    if not _existe:
        w("      Y EL CERO SE DISTINGUE: este fichero NO EXISTE en el arbol ni en")
        w("      git ls-files, asi que su 0 es DE AUSENCIA DE FICHERO y no de")
        w("      fichero sin tocar. AUDITOR.md 4 lo describe como el fichero que el")
        w("      auditor escribe CUANDO HAY PARADA, y no ha habido ninguna.")
    else:
        _m = dos_convenciones(_sede)
        w("      existe, y mide %d bytes en disco y %d normalizado a LF"
          % (_m["disco"], _m["lf"]))
w("")

'''

src = io.open(FUENTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
L = src.split(NL)
n_antes = len(L)
texto = src

print("LOS CAMBIOS PUNTUALES, CADA UNO CON SU CUENTA DE APARICIONES:")
for viejo, nuevo, esperadas in CAMBIOS:
    hay = texto.count(viejo)
    assert hay == esperadas, (viejo[:70], hay, esperadas)
    texto = texto.replace(viejo, nuevo)
    print("   %d aparicion(es)  %s" % (hay, viejo.split(NL)[0][:66]))

ancla = 'w("FIN DE LAS MEDICIONES DE CIERRE")'
assert texto.count(ancla) == 1
texto = texto.replace(ancla, BLOQUE_K + ancla)
print("   BLOQUE K anadido delante de %r" % ancla[:40])

nuevas = texto.split(NL)
sm = difflib.SequenceMatcher(None, L, nuevas, autojunk=False)
iguales = sum(b.size for b in sm.get_matching_blocks())
print("")
print("EL CLON, MEDIDO Y NO AFIRMADO (difflib.SequenceMatcher):")
print("   CIFRA lineas de la fuente %s: %d" % (os.path.basename(FUENTE), n_antes))
print("   CIFRA lineas del destino %s: %d"
      % (os.path.basename(DESTINO), len(nuevas)))
print("   CIFRA lineas que vienen SIN TOCAR de la fuente: %d" % iguales)
print("   CIFRA lineas nuevas o cambiadas en el destino: %d"
      % (len(nuevas) - iguales))

io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
print("")
print("ESCRITO: scripts/loop/_v204_cierre_mediciones.py (%d bytes)"
      % len(texto.encode("utf-8")))
