# -*- coding: utf-8 -*-
r"""_gen_v204_t1_registros.py . GENERA scripts/loop/_v204_t1_registros.py COMO
CLON DECLARADO DE scripts/loop/_v203_t4_registros.py, COPIANDO TODO LO DEMAS
BYTE A BYTE Y MIDIENDO EL CLON CON difflib.

Fichero de computo con PREFIJO DE GUION BAJO: fuera del censo y fuera de la
nomina (`AUDITOR.md` 6.3, `4.5` del acta 199 y `4.6` del acta 203).

LO QUE NO SE CLONA, Y ESTA ES LA PIEZA QUE EL ENCARGO PIDE EXPRESAMENTE: el
COMPUTO del reparto, `scripts/loop/_v203_reparto_de_actas_viejas.py`, **NO se
clona: se IMPORTA tal cual**. El encargo dice *importalo o clonalo con su cifra
de `difflib` al lado, pero no escribas un tercero*, y **importar es la puerta
que no fabrica ningun fichero**. Por eso aqui no hay cifra de `difflib` del
reparto: no hay clon del reparto que medir.
"""
import difflib
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FUENTE = os.path.join(RAIZ, "scripts", "loop", "_v203_t4_registros.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop", "_v204_t1_registros.py")

DOCSTRING = 'r' + chr(34) * 3 + '''_v204_t1_registros.py . TAREA 1 DE LA VUELTA 204: `R.67` PARA EL ACTA 177 Y
`R.68` PARA EL ACTA 178, LAS DOS SIGUIENTES DE LA DEUDA.

POR EL `4.9` DEL ACTA 201: la deuda son las **177 a 180**, DOS POR VUELTA, de la
mas vieja a la mas nueva. Va PRIMERA porque `AUDITOR.md` 1.4 pone los registros
en la TAREA 1. **LA DEUDA SE REMIDE AQUI Y NO SE COPIA DEL ENCARGO**: al cierre
se recuenta cuantas actas de la 173 a la 180 siguen sin entrada propia.

CLON DECLARADO de `scripts/loop/_v203_t4_registros.py`, generado de el
programaticamente con `scripts/loop/_gen_v204_t1_registros.py`, que imprime
cuantas lineas vienen SIN TOCAR y cuantas son nuevas, contadas con `difflib` y
no a ojo.

EL COMPUTO NO SE ESCRIBE POR TERCERA VEZ Y TAMPOCO SE CLONA: se **IMPORTA** de
`scripts/loop/_v203_reparto_de_actas_viejas.py`, que es el que la 203 escribio
para sus TAREAS 1 y 4. El encargo lo manda con estas palabras: *reutiliza el
computo de la 203, importalo o clonalo con su cifra de difflib al lado, pero no
escribas un tercero*. **Aqui se toma la puerta que no fabrica fichero.**

DE QUE CONVENCION SON LAS DOS ACTAS SE COMPRUEBA Y NO SE SUPONE: la 184 es la
frontera, y este computo publica **LAS DOS LECTURAS JUNTAS** sobre cada acta,
la del lector heredado (que exige comillas inversas) y la de la vara ancha del
`4.1` del acta 202. **Si el heredado no da cero, el acta ya escribe sus claves
con comillas inversas y el lector heredado basta: se dice.**

EL NUMERO NO SE TECLEA: lo computa `serie_de_registros.siguiente_libre()`
recomputando la serie de sus DOS sedes, y el segundo se computa DESPUES de
escribirse el primero, que es la unica forma de que no se teclee.

USO:
  python scripts/loop/_v204_t1_registros.py
  python scripts/loop/_v204_t1_registros.py --escribir
  python scripts/loop/_v204_t1_registros.py --escribir --salida NOMBRE
''' + chr(34) * 3

CAMBIOS = [
    ("VUELTA_QUE_ESCRIBE = 203", "VUELTA_QUE_ESCRIBE = 204", 1),
    ("SUJETOS = [175, 176]", "SUJETOS = [177, 178]", 1),
    ('ap.add_argument("--salida", default="T4_REGISTROS")',
     'ap.add_argument("--salida", default="T1_REGISTROS")', 1),
    ('a("(Acta del auditor, vuelta %d; escrito en la vuelta %d, TAREA 4.)"',
     'a("(Acta del auditor, vuelta %d; escrito en la vuelta %d, TAREA 1.)"', 1),
    ('a("Por adicion, como `R.21` a `R.64`. **Corte de todas las cifras de esta")',
     'a("Por adicion, como `R.21` a `R.66`. **Corte de todas las cifras de esta")',
     1),
    ('a("Salida: `docs/loop/SALIDA_V%d_T4_REGISTROS.txt`." % VUELTA_QUE_ESCRIBE)',
     'a("Salida: `docs/loop/SALIDA_V%d_T1_REGISTROS.txt`." % VUELTA_QUE_ESCRIBE)',
     1),
    ('a("TAREA 1 de esta vuelta**: no se escribio un segundo.")',
     'a("TAREA 1 y la TAREA 4 de la vuelta 203**, y aqui se IMPORTA tal cual:")'
     + NL + '    a("no se escribio un tercero y tampoco se clono.")', 1),
    ('    w("VUELTA %d, TAREA 4: R.65 PARA EL ACTA 175 Y R.66 PARA EL ACTA 176,"',
     '    w("VUELTA %d, TAREA 1: R.67 PARA EL ACTA 177 Y R.68 PARA EL ACTA 178,"',
     1),
    ('    w("LAS DOS SIGUIENTES DE LA DEUDA DE OCHO DEL ACTA 201 4.9")',
     '    w("LAS DOS SIGUIENTES DE LA DEUDA DEL 4.9 DEL ACTA 201, REMEDIDA AQUI")',
     1),
    ('    w("   Es la MISMA del computo de la TAREA 1, porque es el MISMO fichero: se")',
     '    w("   Es la MISMA del computo de la 203, porque es el MISMO fichero IMPORTADO:")',
     1),
    ('for etiqueta, vuelta in zip(("4.a", "4.b"), SUJETOS):',
     'for etiqueta, vuelta in zip(("1.a", "1.b"), SUJETOS):', 1),
]

src = io.open(FUENTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
L = src.split(NL)
n_antes = len(L)

assert L[0].startswith("# -*- coding"), L[0][:60]
assert L[1].startswith('r' + chr(34) * 3 + '_v203_t4_registros.py'), L[1][:60]
cierres = [i for i in range(2, len(L)) if L[i] == chr(34) * 3]
assert cierres, "no se encuentra el cierre del docstring"
fin_doc = cierres[0]
doc_viejo = NL.join(L[1:fin_doc + 1])
texto = L[0] + NL + DOCSTRING + NL + NL.join(L[fin_doc + 1:])
print("1) DOCSTRING: %d lineas viejas -> %d lineas nuevas"
      % (doc_viejo.count(NL) + 1, DOCSTRING.count(NL) + 1))

print("2) LOS CAMBIOS PUNTUALES, CADA UNO CON SU CUENTA DE APARICIONES:")
for viejo, nuevo, esperadas in CAMBIOS:
    hay = texto.count(viejo)
    assert hay == esperadas, (viejo[:70], hay, esperadas)
    texto = texto.replace(viejo, nuevo)
    print("   %-3d aparicion(es)  %s" % (hay, viejo[:66]))

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
print("")
print("EL COMPUTO DEL REPARTO NO SE CLONA: SE IMPORTA. Por eso no hay cifra de")
print("   difflib para el, y la linea del import se copia sin tocar:")
for i, l in enumerate(nuevas, 1):
    if "_v203_reparto_de_actas_viejas" in l:
        print("   linea %d | %s" % (i, l.strip()))

io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
print("")
print("ESCRITO: scripts/loop/_v204_t1_registros.py (%d bytes)"
      % len(texto.encode("utf-8")))
