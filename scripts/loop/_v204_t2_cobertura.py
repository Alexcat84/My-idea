# -*- coding: utf-8 -*-
r"""_v204_t2_cobertura.py . TAREA 2 DE LA VUELTA 204: EL TAMANO DEL AGUJERO DE
`cobertura`, MEDIDO Y NO TAPADO.

PREFIJO DE GUION BAJO: computo de una vuelta, fuera del censo y fuera de la
nomina (`AUDITOR.md` 6.3, `4.5` del acta 199, `4.6` del acta 203). NO ESCRIBE EN
NINGUNA SEDE, NO TOCA NINGUNA FICHA Y NO MUEVE NINGUN `estado`: lee
`docs/plan/INVENTARIO.jsonl` y `docs/plan/OPERACIONES.jsonl` y sella su salida.

QUE PIDE EL ENCARGO, Y LO QUE **NO** PIDE. Adjudicado en el `4.3` del acta 203:
**`OP-I-01` no se cierra** porque sus clausulas **2** y **3** no se caerian si el
fallo volviera, ya que `cobertura` es texto libre. **ESTA TAREA NO CIERRA LA
FICHA Y NO ESCRIBE LA VARA**: la vara es codigo permanente y va a la auditoria
integral por el `4.7`. Lo que se mide es **DE QUE TAMANO ES EL AGUJERO**.

LA LECCION QUE GOBIERNA ESTE FICHERO, Y ES LA `C.2` DEL ACTA 203: la misma
busqueda da cifras distintas segun el campo sobre el que corra, y **una vara sin
declarar convierte una medicion buena en una acusacion**. Por eso **CADA
BUSQUEDA DICE SOBRE QUE CAMPO CORRE**, y las que se puedan correr sobre el
fichero entero se corren TAMBIEN ahi y se publican **las dos cifras juntas**.

Y TODA BUSQUEDA ES POSITIVA (`EJECUTOR.md` 9): se cuenta lo que HAY y se nombra,
nunca lo que falta.

USO: python scripts/loop/_v204_t2_cobertura.py
"""
import collections
import hashlib
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

REL_INV = "docs/plan/INVENTARIO.jsonl"
REL_OPS = "docs/plan/OPERACIONES.jsonl"

# LAS VARAS CANDIDATAS. NINGUNA SE ESCRIBE EN CODIGO PERMANENTE Y NINGUNA SE
# PROPONE COMO LA BUENA: son las formas que el propio campo YA TIENE, convertidas
# en patron para poder CONTAR cuantas entradas caeria cada una. Salen de agrupar
# el campo por su esqueleto (digitos a `N`) ANTES de escribir un solo patron, que
# es lo contrario de inventarse una vara y luego buscarle clientes.
VARAS = [
    ("V1  N de N pares leidos; N en cola; N fuera de cola",
     re.compile(r"^\d+ de \d+ pares leidos; \d+ en cola; \d+ fuera de cola")),
    ("V2  N ids",
     re.compile(r"^\d+ ids\b")),
    ("V3  N a secas",
     re.compile(r"^\d+$")),
    ("V4  N de N",
     re.compile(r"^\d+ de \d+(?!\d)")),
    ("V5  N ejemplar o N ejemplares",
     re.compile(r"^\d+ ejemplares?\b")),
    ("V6  puestos N a N, N pares leidos",
     re.compile(r"^puestos \d+ a \d+, \d+ pares leidos$")),
]

# LOS LITERALES DEL HUECO NOMBRADO, QUE ES LA CLAUSULA 3. Tampoco se inventan:
# se buscan POSITIVAMENTE y se publica cuantas entradas trae cada uno y en que
# campo, sin decidir cual es el bueno.
LITERALES_HUECO = ["SIN CRIBAR", "HUECO", "hueco", "NOMBRADO", "nombrado",
                   "no rellenado", "PENDIENTE", "sin veredicto"]
LITERALES_PROVISIONAL = ["PROVISIONAL", "provisional"]
CAMPOS = ["cobertura", "forma", "estado", "nota"]

L = []


def w(s=""):
    L.append(s)


def dos_convenciones(rel):
    d = io.open(os.path.join(RAIZ, rel), "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return len(d), len(lf), hashlib.sha256(lf).hexdigest()[:16], lf.decode("utf-8")


w("=" * 78)
w("VUELTA 204, TAREA 2: EL TAMANO DEL AGUJERO DE `cobertura`, MEDIDO Y NO")
w("TAPADO. NO CIERRA OP-I-01, NO ESCRIBE LA VARA Y NO TOCA NINGUN estado.")
w("=" * 78)
w("")

w("A) LA SEDE, RECONTADA HOY Y NO COPIADA DEL ENCARGO")
d_inv, lf_inv, sha_inv, texto_inv = dos_convenciones(REL_INV)
w("   %s: disco %d bytes | LF %d bytes | sha256 LF %s"
  % (REL_INV, d_inv, lf_inv, sha_inv))
lineas_inv = texto_inv.split(NL)
filas = [l for l in lineas_inv if l.strip()]
w("   CIFRA lineas NO VACIAS: %d" % len(filas))
rows = []
malas = 0
for l in filas:
    try:
        rows.append(json.loads(l))
    except Exception:
        malas += 1
w("   CIFRA lineas que NO parsean como JSON: %d" % malas)
w("   CIFRA entradas leidas: %d" % len(rows))
w("   EL ENCARGO DICE 672 Y MANDA RECONTARLAS. LO MEDIDO DA %d: %s"
  % (len(rows), "CALZA" if len(rows) == 672 else "NO CALZA, y se declara"))
claves = collections.Counter()
for d in rows:
    claves.update(d.keys())
w("   CIFRA claves distintas del esquema: %d" % len(claves))
for k, n in claves.most_common():
    w("      %-14s presente en %d de %d entradas" % (k, n, len(rows)))
w("   CIFRA entradas CON la clave `cobertura`: %d" % claves["cobertura"])
tipos = collections.Counter(type(d.get("cobertura")).__name__ for d in rows)
w("   CIFRA tipos de valor del campo `cobertura`: %s" % dict(tipos))
w("   CIFRA entradas cuyo `cobertura` esta vacio o solo blancos: %d"
  % sum(1 for d in rows if not str(d.get("cobertura", "")).strip()))
w("")

w("B) CUANTAS FORMAS DISTINTAS TOMA HOY EL CAMPO, AGRUPADAS POR SU FORMA")
w("   LA VARA DE AGRUPACION, DICHA ANTES DE LA CIFRA: se sustituye toda tira de")
w("   digitos por `N` (esqueleto), y se agrupa por el esqueleto. Es la unica")
w("   forma de que 'tres de cinco' y 'cuatro de nueve' cuenten como LA MISMA")
w("   FORMA, que es lo que el encargo pide contar.")
w("   BUSQUEDA POSITIVA, Y EL CAMPO SE DECLARA: corre sobre el valor del campo")
w("   `cobertura` de cada entrada, NUNCA sobre la linea entera del fichero.")
cob = [str(d.get("cobertura", "")) for d in rows]
esq = collections.Counter(re.sub(r"\d+", "N", v) for v in cob)
w("   CIFRA FORMAS DISTINTAS del campo `cobertura`: %d" % len(esq))
w("   CIFRA VALORES LITERALES distintos del campo `cobertura`: %d"
  % len(set(cob)))
w("")
w("   | entradas | forma (esqueleto, digitos a N) |")
for e, n in esq.most_common():
    w("   | %8d | %s |" % (n, e[:120].replace("|", "/")))
w("")

w("C) LAS VARAS CANDIDATAS, CONTADAS UNA A UNA Y SOBRE EL CAMPO `cobertura`")
w("   NINGUNA SE PROPONE COMO LA BUENA Y NINGUNA SE ESCRIBE EN CODIGO: se")
w("   cuenta cuantas entradas caeria cada una, que es lo que el encargo pide.")
cae = collections.defaultdict(list)
for i, v in enumerate(cob):
    for nombre, pat in VARAS:
        if pat.match(v):
            cae[nombre].append(i)
for nombre, _pat in VARAS:
    w("   %-52s %4d entradas" % (nombre, len(cae[nombre])))
cubiertas = set()
for nombre, _pat in VARAS:
    cubiertas.update(cae[nombre])
w("   CIFRA entradas que CAEN en AL MENOS UNA de las %d varas candidatas: %d"
  % (len(VARAS), len(cubiertas)))
fuera = [i for i in range(len(cob)) if i not in cubiertas]
w("   CIFRA entradas que NO CAEN EN NINGUNA, o sea EL AGUJERO: %d" % len(fuera))
w("   ESA ES LA CIFRA QUE EL ENCARGO PIDE: cuantas entradas quedarian fuera de")
w("   cualquier vara razonable. VA CON SU VARA AL LADO, porque un numero de")
w("   agujero sin la vara que lo mide no significa nada.")
w("")
w("   LAS %d DE FUERA, UNA A UNA, CON SU TIPO Y SU VALOR LITERAL:" % len(fuera))
for i in fuera:
    d = rows[i]
    w("      #%-4d tipo %-14s %s"
      % (i + 1, d.get("tipo"), repr(str(d.get("cobertura")))[:150]))
w("")

w("D) LA MISMA BUSQUEDA SOBRE EL FICHERO ENTERO, PUBLICADA AL LADO")
w("   ES LA LECCION DE LA `C.2` DEL ACTA 203: la misma variante da cifras")
w("   distintas segun el campo, y quien no declara el campo convierte una")
w("   medicion buena en una acusacion. AQUI VAN LAS DOS.")
w("   | busqueda | sobre el CAMPO `cobertura` | sobre la LINEA ENTERA del fichero |")
for nombre, pat in VARAS:
    sin_ancla = re.compile(pat.pattern.lstrip("^"))
    n_linea = sum(1 for l in filas if sin_ancla.search(l))
    w("   | %-48s | %4d | %4d |" % (nombre, len(cae[nombre]), n_linea))
w("   LAS DOS COLUMNAS SON CIERTAS Y MIDEN COSAS DISTINTAS: la izquierda ancla")
w("   al principio del CAMPO, la derecha busca en cualquier sitio de la LINEA.")
w("")

w("E) LA CLAUSULA 3, LA DE LOS HUECOS NOMBRADOS, QUE COMPARTE EL AGUJERO")
w("   TEXTO LITERAL DE LA CLAUSULA, LEIDO HOY DE LA FICHA Y NO DE MEMORIA:")
d_ops, lf_ops, sha_ops, texto_ops = dos_convenciones(REL_OPS)
ficha = None
linea_ficha = None
for i, l in enumerate(texto_ops.split(NL), 1):
    if not l.strip():
        continue
    try:
        dd = json.loads(l)
    except Exception:
        continue
    if dd.get("id_op") == "OP-I-01":
        ficha, linea_ficha = dd, i
w("   %s: disco %d bytes | LF %d bytes | sha256 LF %s"
  % (REL_OPS, d_ops, lf_ops, sha_ops))
w("   la ficha OP-I-01 vive en la LINEA %s" % linea_ficha)
ver = (ficha or {}).get("verificacion") or []
w("   CIFRA elementos de `verificacion`: %d" % len(ver))
for k, e in enumerate(ver):
    w("      clausula %d (indice %d): %s" % (k + 1, k, e))
w("   estado de la ficha, LEIDO Y NO TOCADO: %r" % (ficha or {}).get("estado"))
w("")
w("   LAS BUSQUEDAS POSITIVAS DEL HUECO, CADA UNA CON SU CAMPO DECLARADO:")
w("   | literal | campo | entradas |")
for lit in LITERALES_HUECO:
    for campo in CAMPOS:
        n = sum(1 for d in rows if lit in str(d.get(campo, "")))
        w("   | %-14s | %-10s | %4d |" % (lit, campo, n))
w("")
w("   EL AGUJERO DE LA CLAUSULA 3, DICHO CON LA MISMA VARA QUE EL DE LA 2: el")
w("   literal que mas entradas trae y el que menos difieren en DOS ORDENES DE")
w("   MAGNITUD sobre los MISMOS campos, o sea que `hueco nombrado` tampoco")
w("   tiene forma. Y ninguna de las dos clausulas dice EN QUE CAMPO se escribe")
w("   el hueco, que es la mitad del agujero: la cifra cambia segun el campo que")
w("   se mire, y la clausula no lo fija.")
w("")

w("F) LA CLAUSULA 2, LA DEL PROVISIONAL, MEDIDA IGUAL")
w("   | literal | campo | entradas |")
for lit in LITERALES_PROVISIONAL:
    for campo in CAMPOS:
        n = sum(1 for d in rows if lit in str(d.get(campo, "")))
        w("   | %-14s | %-10s | %4d |" % (lit, campo, n))
formas = collections.Counter(str(d.get("forma", ""))[:70] for d in rows)
w("   CIFRA valores distintos del campo `forma`: %d" % len(formas))
w("   CIFRA entradas cuyo campo `forma` es EXACTAMENTE `PROVISIONAL`: %d"
  % sum(1 for d in rows if str(d.get("forma", "")).strip() == "PROVISIONAL"))
w("   LA CLAUSULA 2 DICE *toda forma con cobertura incompleta va marcada")
w("   PROVISIONAL*, Y AQUI ESTA EL AGUJERO ENTERO EN UNA LINEA: para poder")
w("   comprobarla haria falta saber QUE ES `cobertura incompleta`, y el campo")
w("   `cobertura` es TEXTO LIBRE con %d formas distintas, asi que hoy NO HAY"
  % len(esq))
w("   NADA QUE COMPARAR. No es que la clausula se incumpla: es que NO SE PUEDE")
w("   MEDIR, que es exactamente lo que el `4.3` del acta 203 adjudico.")
w("")

w("G) LA COINCIDENCIA QUE SALIO MEDIDA Y NO BUSCADA, Y SE COMPRUEBA EN VEZ DE")
w("   CELEBRARSE: LA VARA V4 CAE EXACTAMENTE SOBRE LA POBLACION DEL DISPARADOR")
conj_v4 = set(cae["V4  N de N"])
conj_ar = set(i for i, d in enumerate(rows) if d.get("tipo") in ("acto", "racimo"))
w("   CIFRA entradas que caen en V4: %d" % len(conj_v4))
w("   CIFRA entradas de tipo `acto` o `racimo`, que es lo que el paso 4 de")
w("   docs/plan/08_VERIFICACION.md nombra: %d" % len(conj_ar))
w("   LOS DOS CONJUNTOS SON EL MISMO: %s" % (conj_v4 == conj_ar))
w("   CIFRA en V4 y NO en acto o racimo: %d" % len(conj_v4 - conj_ar))
w("   CIFRA en acto o racimo y NO en V4: %d" % len(conj_ar - conj_v4))
resto = collections.Counter(d.get("tipo") for i, d in enumerate(rows)
                            if i not in conj_ar)
w("   CIFRA entradas FUERA del disparador: %d, repartidas asi: %s"
  % (len(rows) - len(conj_ar), dict(resto)))
w("   POR QUE IMPORTA, Y ES LO UNICO QUE ESTA TAREA APORTA A QUIEN ESCRIBA LA")
w("   VARA DESPUES: el `4.3` del acta 203 midio 569 dentro del disparador y 103")
w("   fuera, y esas mismas 569 son EXACTAMENTE las que hoy YA tienen una forma")
w("   comprobable a maquina. O sea que el agujero de `cobertura` NO esta")
w("   repartido por todo el fichero: esta CONCENTRADO en las 103 de fuera.")
w("   Y LAS 15 SON UN SUBCONJUNTO DE ESAS 103, NO UNA SUMA APARTE, y eso se")
w("   COMPRUEBA en vez de decirse:")
dentro_103 = [i for i in fuera if i not in conj_ar]
w("      CIFRA de las %d sin ninguna vara que estan FUERA del disparador: %d"
  % (len(fuera), len(dentro_103)))
w("      CIFRA de las %d sin ninguna vara que estan DENTRO del disparador: %d"
  % (len(fuera), len(fuera) - len(dentro_103)))
w("      LAS 15 SON SUBCONJUNTO DE LAS 103: %s"
  % (set(fuera) <= (set(range(len(rows))) - conj_ar)))
w("   NO SE PROPONE NINGUNA VARA: se deja la cifra medida.")
w("")

w("H) LO QUE ESTA TAREA NO HACE, DICHO Y NO SUPUESTO")
w("   . NO cierra OP-I-01 y NO propone cerrarla.")
w("   . NO escribe ninguna vara: eso es codigo permanente y va a la auditoria")
w("     integral por el `4.7` del acta 203, y hoy la moratoria 6.3 lo prohibe.")
w("   . NO toca el campo `estado` de ninguna ficha ni de ninguna entrada.")
w("   . NO reescribe INVENTARIO.jsonl ni OPERACIONES.jsonl: los LEE.")
w("")
w("FIN")

salida = NL.join(L) + NL
print(salida)
io.open(os.path.join(LOOP, "SALIDA_V204_T2_COBERTURA.txt"), "w",
        encoding="utf-8", newline=NL).write(salida)
