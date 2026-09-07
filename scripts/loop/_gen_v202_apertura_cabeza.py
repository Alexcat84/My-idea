# -*- coding: utf-8 -*-
r"""vuelta202_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 202, CORRIDO ANTES
DE LA PRIMERA OPERACION.

CLON DECLARADO de `scripts/loop/vuelta201_apertura.py`, que a su vez viene de la
200, la 199, la 197, la 196 y la 195. LOS BLOQUES `A` A `G` SE COPIARON BYTE A
BYTE de aquel fichero, con el generador `_gen_v202_apertura.py` de esta misma
vuelta, y NO se re escribieron: lo unico que cambia en ellos es la constante
`VUELTA` y los dos literales que nombran la vuelta anterior. Lo que SI se
reescribe se dice aqui y no se esconde:

1. LA 202 NO ES VUELTA DE BATERIA. La 200 lo fue y cerro entera; por la cadencia
   de `AUDITOR.md` 6.1 le toca a la 205. Aqui la seccion 9 cierra con el HUECO
   DECLARADO Y MEDIDO por su carril. El sujeto de esta vuelta es EL PLAN.
2. EL BLOQUE `H` MIDE EL SUJETO DE LA TAREA 1: la ficha `OP-L-03` de
   `docs/plan/OPERACIONES.jsonl` localizada POR LINEA, sus tres elementos de
   `evidencia` con su indice, las DOS cifras que el encargo manda medir sobre
   `docs/plan/LECTURAS_DIRIGIDAS.md` (el literal `reparto por acto` y las
   menciones de `OP-L-03`), y los DOS ficheros `docs/plan/OP_L_03_*.jsonl` con
   sus bytes exactos, sus filas, sus actos distintos y sus lineas no JSON.
3. EL BLOQUE `H.1` MIDE EL SUJETO DE LAS TAREAS 2 Y 3 ANTES DE TOCAR NADA: los
   DOS instrumentos de `OP-L-02` (que NO SE TOCAN y NO SE CLONAN), medidos y
   ademas leidos para comprobar SI ESCRIBEN FICHEROS; `docs/plan/08_VERIFICACION.md`
   con el criterio de hecho localizado por linea; y la TABLA VIVA DE LOS PUROS de
   `docs/BANCO_DE_TEXTOS.md` con su literal de vigencia.
4. EL BLOQUE `H.2` MIDE EL SUJETO DE LA TAREA 4: las actas 173 y 174 ACOTADAS
   AQUI por linea de inicio y fin, y la existencia de sus reportes archivados
   medida con `os.path.isfile` y `os.path.getsize`.
5. EL BLOQUE `H.3` CORRE LA VARA DEL TRABAJO PENDIENTE, que es
   `vuelta150_3_relectura_expediente.py --corte <HEAD DE APERTURA>`, y sella su
   salida. La vara NO SE CLONA y NO SE TOCA: se invoca.
6. EL BLOQUE `F` MIDE LA NOMINA CONTRA EL CONGELADO EN 135 que manda
   `AUDITOR.md` 6.3. AQUI NO SE PODA NI SE ANADE NADA: se mide.
7. EL BLOQUE `E` SIGUE CONTANDO LA RACHA DEL INSTRUMENTO, porque de esa cifra
   depende si el tope de sub-tareas es DOS o CINCO (`AUDITOR.md` 6.2).

USO:
  python scripts/loop/vuelta202_apertura.py
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
NL = chr(10)
VUELTA = 202

VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
TURNO = "docs/loop/_TURNO_DEL_AUDITOR.json"
ACTA = "docs/loop/ACTA_AUDITOR.md"

INSTRUMENTO_RACHA = "scripts/loop/vuelta192_racha_de_cierres.py"
SELLADA_RACHA = "docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt"

# LOS SUJETOS DE ESTA VUELTA, medidos y no supuestos.
INVENTARIO_JSONL = "docs/plan/INVENTARIO.jsonl"
OPERACIONES = "docs/plan/OPERACIONES.jsonl"
FICHAS_REALES = ["OP-L-01", "OP-L-02", "OP-L-03", "OP-I-01"]
DOCUMENTOS_DE_LA_VARA = [
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "docs/INTRA_DOMINIO_INFORME.md",
    "docs/BANCO_DE_TEXTOS.md",
    "docs/plan/BANCO_DEL_PLAN.md",
]
VARA_DEL_PLAN = "scripts/loop/vuelta150_3_relectura_expediente.py"

# TAREA 1: la sede de la correccion y los dos ficheros del reparto por acto.
FICHA_T1 = "OP-L-03"
DOC_DE_LA_EVIDENCIA = "docs/plan/LECTURAS_DIRIGIDAS.md"
LITERAL_REPARTO = "reparto por acto"
FICHEROS_DEL_REPARTO = [
    "docs/plan/OP_L_03_LECTURAS.jsonl",
    "docs/plan/OP_L_03_TRIANGULOS.jsonl",
]

# TAREAS 2 y 3: los instrumentos que se IMPORTAN y no se clonan, y las sedes.
INSTRUMENTOS_OP_L_02 = [
    "scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py",
    "scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py",
]
CRITERIO_DE_HECHO = "docs/plan/08_VERIFICACION.md"
BANCO = "docs/BANCO_DE_TEXTOS.md"
LINEA_TABLA_VIVA = 938
LITERAL_VIGENCIA = "vigente al puesto"

# TAREA 4: las dos actas mas viejas de la deuda y sus reportes archivados.
# LA MARCA DE ESCRITURA EN DISCO, para comprobar ANTES de correrlos que
# los dos instrumentos de OP-L-02 SOLO MIDEN. No es una guarda nueva: es
# una expresion regular de este mismo bloque de apertura, que no vive fuera
# de el y no entra en el censo.
PATRON_ESCRITURA = re.compile(
    r"open\s*\([^)]*[" + chr(34) + chr(39) + r"](w|wb|a|ab|w\+|r\+)[" 
    + chr(34) + chr(39) + r"]|\.write\s*\(|os\.remove|shutil\.|os\.rename|os\.makedirs|json\.dump\s*\(")
ACTAS_DE_LA_DEUDA = [173, 174]
PENDIENTES = "docs/PENDIENTES.md"


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env,
                       shell=shell)
    out = (r.stdout.decode("utf-8", errors="replace")
           + r.stderr.decode("utf-8", errors="replace"))
    return r.returncode, out


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def sha_de(rel):
    """LAS DOS CONVENCIONES, MEDIDAS Y NO SUPUESTAS. Devuelve
    (sha_disco, sha_lf, bytes_disco, bytes_lf) o None si el fichero no esta."""
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(ruta):
        return None
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (hashlib.sha256(datos).hexdigest(), hashlib.sha256(lf).hexdigest(),
            len(datos), len(lf))


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V%d_%s_APERTURA.txt" % (VUELTA, nombre))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITO: %s (%d bytes)"
          % (os.path.basename(ruta), len(texto.encode("utf-8"))))


L = []
w = L.append
w("SELLO DE APERTURA DE LA VUELTA %d, escrito ANTES de la primera operacion."
  % VUELTA)
w("regimen: MORATORIA DE MAQUINARIA (AUDITOR.md 6.3, decision del fundador del 7")
w("         sep 2026). NO SE FABRICAN ARNESES, GUARDAS NI LECTORES NUEVOS, y")
w("         esta vuelta NO TIENE NINGUNA EXCEPCION. La nomina queda CONGELADA EN")
w("         135: ni crece ni se poda.")
w("         ESTA NO ES VUELTA DE BATERIA. La 200 lo fue y cerro entera; por la")
w("         cadencia de AUDITOR.md 6.1 le toca a la 205. La seccion 9 cierra con")
w("         el HUECO DECLARADO Y MEDIDO por su carril.")
w("         EL TRABAJO ES EL PLAN: las cuatro fichas reales.")
w("         EL TOPE DE SUB-TAREAS LO MANDA LA CIFRA DEL BLOQUE E, contada aqui")
w("         del instrumento. El encargo trae CUATRO sub-tareas.")
w("ESTE BLOQUE CORRE EL CICLO COMPLETO, tsc y pnpm test INCLUIDOS, y escribe el")
w("         mismo los dos literales de la guarda D.1.")
w("")
