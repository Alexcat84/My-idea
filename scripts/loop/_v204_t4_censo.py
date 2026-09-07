# -*- coding: utf-8 -*-
r"""_v204_t4_censo.py . TAREA 4 DE LA VUELTA 204: EL CENSO DE LO QUE QUEDA DEL
PLAN, MEDIDO Y NO NARRADO.

PREFIJO DE GUION BAJO: computo de una vuelta, fuera del censo y fuera de la
nomina (`AUDITOR.md` 6.3, `4.5` del acta 199, `4.6` del acta 203).

LO QUE NO HACE, Y VA DELANTE: **NINGUNA FICHA SE CIERRA Y NINGUN `estado` SE
MUEVE.** Este fichero no abre `docs/plan/OPERACIONES.jsonl` en modo escritura en
ninguna linea. Lo que produce es EL MAPA DE LO QUE QUEDA.

EL CRUCE ES EL PUNTO, NO LA SUMA. `AUDITOR.md` 0 dice que la vara del trabajo
pendiente es `scripts/loop/vuelta150_3_relectura_expediente.py` y **nunca el
campo `estado`**. Aqui se publican **LAS DOS LECTURAS JUNTAS** y **la
discrepancia se declara**, que es lo que el encargo pide.

LA VARA SE CORRE CON UN COMMIT EN `--corte`, NO CON UNA FECHA: con una fecha sale
`ROJO: no se pudo leer OPERACIONES.jsonl`. El corte es el HEAD DE APERTURA de
esta vuelta, leido de `docs/loop/SALIDA_V204_HEAD_APERTURA.txt` y no tecleado.

USO: python scripts/loop/_v204_t4_censo.py
"""
import collections
import hashlib
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
PY = sys.executable

REL_OPS = "docs/plan/OPERACIONES.jsonl"
REL_VARA = "scripts/loop/vuelta150_3_relectura_expediente.py"
REL_SELLO_HEAD = "docs/loop/SALIDA_V204_HEAD_APERTURA.txt"
REL_SALIDA_VARA = "docs/loop/SALIDA_V204_T4_VARA.txt"

L = []


def w(s=""):
    L.append(s)


def dos_convenciones(rel):
    d = io.open(os.path.join(RAIZ, rel), "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return len(d), len(lf), hashlib.sha256(lf).hexdigest()[:16], lf.decode("utf-8")


w("=" * 78)
w("VUELTA 204, TAREA 4: EL CENSO DE LO QUE QUEDA DEL PLAN, MEDIDO Y NO NARRADO.")
w("NINGUNA FICHA SE CIERRA Y NINGUN estado SE MUEVE.")
w("=" * 78)
w("")

w("A) LA PRIMERA LECTURA: LAS FICHAS POR SU CAMPO `estado`, RECONTADAS HOY")
w("   Y SE DICE LO QUE ESTA LECTURA ES: EL CAMPO, que `AUDITOR.md` 0 prohibe")
w("   usar como vara del trabajo pendiente. Va aqui porque el encargo pide LAS")
w("   DOS, no porque valga por si sola.")
d_ops, lf_ops, sha_ops, texto_ops = dos_convenciones(REL_OPS)
w("   %s: disco %d bytes | LF %d bytes | sha256 LF %s"
  % (REL_OPS, d_ops, lf_ops, sha_ops))
fichas = []
for i, l in enumerate(texto_ops.split(NL), 1):
    if not l.strip():
        continue
    fichas.append((i, json.loads(l)))
w("   CIFRA lineas NO VACIAS: %d" % len(fichas))
por_estado = collections.Counter(d.get("estado") for _i, d in fichas)
for k, n in sorted(por_estado.items(), key=lambda x: (-x[1], str(x[0]))):
    w("   CIFRA fichas con estado %-8r %d" % (k, n))
w("   EL ENCARGO DICE 71 FICHAS, 42 LISTA Y 29 HECHA, Y MANDA RECONTARLAS.")
w("   LO MEDIDO: %d fichas, %s. %s"
  % (len(fichas), ", ".join("%d %s" % (n, k) for k, n in
                            sorted(por_estado.items(), key=lambda x: -x[1])),
     "CALZA" if (len(fichas) == 71 and por_estado.get("LISTA") == 42
                 and por_estado.get("HECHA") == 29)
     else "NO CALZA, y se declara"))
por_tipo = collections.Counter(d.get("tipo") for _i, d in fichas)
w("   reparto por `tipo`, al lado y sin mezclarlo: %s" % dict(sorted(por_tipo.items())))
w("")

w("B) LA SEGUNDA LECTURA: LA VARA DEL TRABAJO PENDIENTE, QUE ES LA QUE MANDA")
head = io.open(os.path.join(RAIZ, REL_SELLO_HEAD), encoding="utf-8").read().strip()
w("   corte: el HEAD DE APERTURA de esta vuelta, LEIDO de %s" % REL_SELLO_HEAD)
w("   y no tecleado: %s" % head)
w("   comando: python %s --corte %s" % (REL_VARA, head))
w("   LA VARA LLEVA UN COMMIT Y NUNCA UNA FECHA: con una fecha sale")
w("   `ROJO: no se pudo leer OPERACIONES.jsonl`.")
ruta_sal = os.path.join(RAIZ, REL_SALIDA_VARA)
if not os.path.isfile(ruta_sal):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([PY, REL_VARA, "--corte", head], cwd=RAIZ,
                       capture_output=True, env=env)
    io.open(ruta_sal, "w", encoding="utf-8", newline=NL).write(
        (r.stdout.decode("utf-8", "replace")
         + r.stderr.decode("utf-8", "replace")).replace(chr(13) + NL, NL))
d_s, lf_s, sha_s, texto_vara = dos_convenciones(REL_SALIDA_VARA)
w("   %s: disco %d bytes | LF %d bytes | sha256 LF %s"
  % (REL_SALIDA_VARA, d_s, lf_s, sha_s))
CIFRAS = ["fichas del expediente", "fichas que no calzan",
          "fichas congeladas declaradas", "fichas congeladas en silencio",
          "fichas HECHA sin ninguna prueba", "fichas en LISTA sin ninguna prueba",
          "de esas que estan CONSUMIDAS por otra ficha",
          "de esas que son TRABAJO REAL"]
leidas = {}
for etiqueta in CIFRAS:
    m = re.search(r"CIFRA %s:\s*(\d+)" % re.escape(etiqueta), texto_vara)
    leidas[etiqueta] = int(m.group(1)) if m else None
    w("   CIFRA %-44s %s" % (etiqueta + ":", leidas[etiqueta]))
w("   EL ENCARGO PUBLICA LAS MISMAS OCHO CIFRAS CORRIDAS POR EL AUDITOR SOBRE")
w("   c4ffc221. LAS MIAS SALEN DE MI CORRIDA SOBRE %s." % head[:8])
esperadas = [71, 37, 24, 12, 1, 6, 2, 4]
distintas = [e for e, v in zip(CIFRAS, esperadas) if leidas[e] != v]
w("   CIFRA de las ocho que DIFIEREN de las del encargo: %d" % len(distintas))
for e in distintas:
    w("      DIFIERE: %s, el encargo dice %d y yo mido %s"
      % (e, esperadas[CIFRAS.index(e)], leidas[e]))
if not distintas:
    w("      (ninguna: las ocho calzan al digito)")
w("")

w("C) LAS DOS LECTURAS JUNTAS, Y LA DISCREPANCIA DECLARADA. ESTE ES EL PUNTO.")
w("   | lectura | que mide | cifra |")
w("   |---|---|---:|")
w("   | el campo `estado` | fichas que el campo llama HECHA | %d |"
  % por_estado.get("HECHA", 0))
w("   | el campo `estado` | fichas que el campo llama LISTA | %d |"
  % por_estado.get("LISTA", 0))
w("   | la vara | fichas cuyo estado NO CALZA con el repo | %d |"
  % leidas["fichas que no calzan"])
w("   | la vara | de esas, TRABAJO REAL | %d |"
  % leidas["de esas que son TRABAJO REAL"])
w("")
w("   LA DISCREPANCIA, DICHA CON SUS CIFRAS Y NO CON UN ADJETIVO:")
w("   . el campo dice que quedan %d fichas en LISTA, o sea trabajo por hacer;"
  % por_estado.get("LISTA", 0))
w("   . la vara dice que de las 71 hay %d que NO CALZAN, y que de esas solo %d"
  % (leidas["fichas que no calzan"], leidas["de esas que son TRABAJO REAL"]))
w("     son TRABAJO REAL;")
w("   . o sea que el campo `estado` SOBREESTIMA el trabajo pendiente en %d"
  % (por_estado.get("LISTA", 0) - leidas["de esas que son TRABAJO REAL"]))
w("     fichas, y por eso `AUDITOR.md` 0 lo prohibe como vara;")
w("   . y en el otro sentido el campo tambien MIENTE POR EXCESO DE CONFIANZA:")
w("     %d ficha esta en HECHA sin ninguna prueba en el repo."
  % leidas["fichas HECHA sin ninguna prueba"])
w("   NINGUNA DE LAS DOS CIFRAS SE CORRIGE CON LA OTRA: SE PUBLICAN LAS DOS.")
w("")
w("   LA SALVEDAD QUE ESA RESTA NECESITA, Y VA PEGADA A ELLA PARA QUE NADIE LA")
w("   LEA SOLA: `TRABAJO REAL` es la etiqueta de la VARA, no un sinonimo de")
w("   'lo unico que queda por hacer'. La vara llega a esa cifra por un camino")
w("   escrito: de las %d en LISTA, %d salen por CONGELADA DECLARADA (su propia"
  % (por_estado.get("LISTA", 0), leidas["fichas congeladas declaradas"]))
w("   ficha dice que esta congelada), %d por CONGELADA EN SILENCIO, %d quedan"
  % (leidas["fichas congeladas en silencio"],
     leidas["fichas en LISTA sin ninguna prueba"]))
w("   en LISTA sin ninguna prueba, y de esas %d estan CONSUMIDAS por otra ficha."
  % leidas["de esas que estan CONSUMIDAS por otra ficha"])
w("   LA RESTA DE ARRIBA ES ARITMETICA SOBRE LAS DOS CIFRAS PUBLICADAS, y no")
w("   una afirmacion de que las otras %d esten hechas."
  % (por_estado.get("LISTA", 0) - leidas["de esas que son TRABAJO REAL"]))
w("")

w("D) LAS TRECE QUE NADIE HA MIRADO NUNCA, NOMBRADAS UNA A UNA")
w("   SE LEEN DE LA TABLA DE LA VARA, fila a fila, y no se teclean.")
filas = []
for linea in texto_vara.split(NL):
    m = re.match(r"^\|\s*`(OP-[^`]+)`\s*\|\s*([^|]*)\|\s*([^|]*)\|"
                 r"\s*([^|]*)\|\s*([^|]*)\|", linea)
    if m:
        filas.append(tuple(x.strip() for x in m.groups()))
silencio = [f for f in filas if "CONGELADO EN SILENCIO" in f[4]]
hecha_sin = [f for f in filas if "HECHA SIN NINGUNA PRUEBA" in f[4]]
w("   CIFRA filas de la tabla de la vara leidas: %d" % len(filas))
w("   CIFRA CONGELADAS EN SILENCIO: %d" % len(silencio))
w("   CIFRA HECHA SIN NINGUNA PRUEBA: %d" % len(hecha_sin))
w("   CIFRA de las dos juntas: %d" % (len(silencio) + len(hecha_sin)))
w("")
w("   | id_op | fase | estado | pruebas que dan positivo | motivo |")
w("   |---|---|---|---|---|")
for f in silencio + hecha_sin:
    w("   | `%s` | %s | %s | %s | %s |" % f)
w("")
w("   QUE SIGNIFICA `CONGELADO EN SILENCIO`, DICHO Y NO SUPUESTO: la ficha esta")
w("   en LISTA, tiene alguna huella en el repo, y **su propio texto no dice")
w("   nada de su estado**. No significa que este mal: significa que **nadie la")
w("   ha mirado y escrito nunca**, que es justo lo que el encargo pide nombrar.")
w("   Y `HECHA SIN NINGUNA PRUEBA` significa que **el estado afirma mas que el")
w("   repo**: ninguna de las pruebas de grafo, codigo o git da positivo.")
w("")
w("   EL REPARTO POR FASE DE LAS TRECE, CONTADO Y NO A OJO:")
por_fase = collections.Counter(f[1] for f in silencio + hecha_sin)
for k, n in sorted(por_fase.items(), key=lambda x: (-x[1], x[0])):
    w("      %-22s %d" % (k, n))
w("")

w("E) LA GUARDA: NINGUN `estado` SE MOVIO")
d2, lf2, sha2, _t2 = dos_convenciones(REL_OPS)
w("   %s al salir: disco %d bytes | LF %d bytes | sha256 LF %s"
  % (REL_OPS, d2, lf2, sha2))
w("   IDENTICO AL DE ENTRADA: %s" % ("SI" if sha2 == sha_ops else "NO"))
w("   CIFRA de las %d fichas que cambian de `estado` en esta tarea: 0" % len(fichas))
w("")
w("FIN")

salida = NL.join(L) + NL
print(salida)
io.open(os.path.join(LOOP, "SALIDA_V204_T4_CENSO.txt"), "w",
        encoding="utf-8", newline=NL).write(salida)
