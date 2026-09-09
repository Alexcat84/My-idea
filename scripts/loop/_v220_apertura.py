# -*- coding: utf-8 -*-
r"""_v220_apertura.py . COMPUTO DE LA VUELTA 220, CON PREFIJO DE GUION BAJO,
FUERA DEL CENSO Y FUERA DE LA NOMINA (moratoria de AUDITOR.md 6.3).

QUE HACE: mide el estado del arbol ANTES DE LA PRIMERA OPERACION de la vuelta
(EJECUTOR.md 1, LA APERTURA SE MIDE ANTES DE LA PRIMERA OPERACION) y lo sella.

IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5, linea 72517 de
docs/loop/ACTA_AUDITOR.md, LEIDA EN ESTA VUELTA Y NO RECORDADA). Este fichero
NO copia ni una linea del computo de la 219: IMPORTA la cadena entera
(_v219_apertura, que importa _v218_apertura, que importa git/shas/RAIZ de
_v213_apertura y medir_en_disco de vuelta186_rutas_del_reporte.py) y solo le
cambia DOS cosas, EL NUMERO DE VUELTA (que se computa de mi propio nombre de
fichero y no se teclea) y LA LISTA DE SEDES que esta vuelta va a nombrar.

LA 220 SI ES VUELTA DE BATERIA (cadencia de cinco de AUDITOR.md 6.1: la 215 la
corrio y la siguiente cae aqui), asi que esta apertura SELLA ADEMAS EL ESTADO
DE LAS ONCE SALIDAS DE TRAMO QUE YA ESTABAN EN DISCO ANTES DE QUE ESTA VUELTA
CORRIERA NADA, que son las de la 215. Es la unica forma de que la cifra de
"salidas que TU escribiste en esta vuelta" del encargo 2.d se pueda medir
contra algo y no contra un recuerdo.

Y LAS SEDES QUE NO SE TOCAN VAN NOMBRADAS AQUI PARA QUE SU sha256 SE PUEDA
COTEJAR AL SALIR: docs/plan/08_VERIFICACION.md, docs/plan/07_ADUANA.md,
docs/plan/INVENTARIO.jsonl y docs/plan/OPERACIONES.jsonl.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import _v219_apertura as B  # noqa: E402

A = B.A

NL = chr(10)
YO = os.path.basename(os.path.abspath(__file__))
_M = re.match(r"^_v(\d+)_", YO)
if not _M:
    raise SystemExit("ROJO: el nombre %r no dice de que vuelta es este computo, "
                     "y el numero NO SE ADIVINA." % YO)
MI_VUELTA = int(_M.group(1))

VUELTA_DEL_ENVOLTORIO = B.MI_VUELTA
VUELTA_DE_LOS_COMANDOS = B.VUELTA_HEREDADA
A.VUELTA = MI_VUELTA

A.RUTAS = [
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/REPORTE.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/INVENTARIO.jsonl",
    "docs/plan/08_VERIFICACION.md",
    "docs/plan/07_ADUANA.md",
    "docs/plan/01_FUENTES.md",
    "docs/plan/03_FUSIONES.md",
    "docs/plan/05_SANEO.md",
    "docs/BANCO_DE_TEXTOS.md",
    "docs/plan/BANCO_DEL_PLAN.md",
    "dataset/metadata/master_graph.json",
    "scripts/loop/vuelta183_bateria_por_tramos.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
]


def sello_de_los_tramos_de_antes():
    """LAS ONCE SALIDAS DE TRAMO QUE YA ESTABAN EN DISCO ANTES DE LA PRIMERA
    OPERACION DE ESTA VUELTA, con sus bytes por las dos convenciones y el
    asunto del commit que las sello. NO se borra ninguna: se sellan para poder
    decir despues, con cifras y no con memoria, cuales reescribio la 220."""
    filas = []
    for n in range(1, 100):
        nombre = "SALIDA_V183_BATERIA_TRAMO_%d.txt" % n
        ruta = os.path.join(A.RAIZ, "docs", "loop", nombre)
        if not os.path.isfile(ruta):
            continue
        sd, sl = A.shas("docs/loop/" + nombre)
        _, asunto = A.git(["log", "-1", "--format=%s", "--",
                           "docs/loop/" + nombre])
        texto = io.open(ruta, "rb").read()
        filas.append((n, len(texto), len(texto.replace(chr(13).encode(), b"")),
                      sd, sl, asunto.strip()[:90]))
    return filas


def main():
    codigo = A.main()
    destino = os.path.join(A.RAIZ, "docs", "loop",
                           "SALIDA_V%d_APERTURA.txt" % MI_VUELTA)
    out = []
    out.append("")
    out.append("LAS SALIDAS DE TRAMO DE BATERIA QUE YA ESTABAN EN DISCO ANTES DE")
    out.append("LA PRIMERA OPERACION DE LA VUELTA %d (o sea, NO son de esta vuelta):"
               % MI_VUELTA)
    filas = sello_de_los_tramos_de_antes()
    out.append("CIFRA salidas de tramo en disco AL ENTRAR: %d" % len(filas))
    vacias = [f for f in filas if f[1] == 0]
    out.append("CIFRA de ellas que miden CERO BYTES AL ENTRAR: %d" % len(vacias))
    for n, bd, blf, sd, sl, asunto in filas:
        out.append("CIFRA SALIDA_V183_BATERIA_TRAMO_%d.txt AL ENTRAR: %d bytes en "
                   "disco y %d bytes normalizado a LF, sha256 disco %s y sha256 LF "
                   "%s | ultimo commit: %s" % (n, bd, blf, sd[:16], sl[:16], asunto))
    texto = NL.join(out) + NL
    with io.open(destino, "a", encoding="utf-8", newline=NL) as f:
        f.write(texto)
    sys.stdout.write(texto)
    return codigo


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print("EL COMPUTO IMPORTADO, NO CLONADO: %s"
          % os.path.basename(A.__file__))
    print("  a traves del envoltorio %s" % os.path.basename(B.__file__))
    print("  vuelta que ESE envoltorio computa de SU nombre: %d"
          % VUELTA_DEL_ENVOLTORIO)
    print("  vuelta que EL computo computa de SU nombre: %d"
          % VUELTA_DE_LOS_COMANDOS)
    print("  vuelta de ESTA corrida (computada de mi nombre, no tecleada): %d"
          % MI_VUELTA)
    print("  sedes que ESTA vuelta nombra: %d" % len(A.RUTAS))
    sys.exit(main())
