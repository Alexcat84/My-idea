# -*- coding: utf-8 -*-
r"""_v203_cierre_mediciones.py . EL CIERRE DE LA VUELTA 203: CORRE EL CICLO
ENTERO DE GATE 0 OTRA VEZ Y REMIDE TODO AL CIERRE.

EL ESTADO AL CIERRE SE MIDE AL CIERRE (`EJECUTOR.md` 1): toda cifra que describa
el estado al cerrar se RECOMPUTA aqui, aunque la propia vuelta la haya movido.
Medir temprano y publicar tarde sin remedir es la misma especie de caida que
citar sin mirar.

PREFIJO DE GUION BAJO: computo de una vuelta, fuera del censo y de la nomina.

USO: python scripts/loop/_v203_cierre_mediciones.py
"""
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
VUELTA = 203

L = []


def w(s=""):
    L.append(s)


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env,
                       shell=shell)
    return r.returncode, (r.stdout.decode("utf-8", errors="replace")
                          + r.stderr.decode("utf-8", errors="replace"))


def dos_convenciones(rel):
    ruta = os.path.join(RAIZ, rel)
    if not os.path.isfile(ruta):
        return None
    d = io.open(ruta, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return dict(disco=len(d), lf=len(lf),
                sha_lf=hashlib.sha256(lf).hexdigest()[:16],
                texto=lf.decode("utf-8", errors="replace"))


def escribir(nombre, texto):
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s_CIERRE.txt" % (VUELTA, nombre)),
            "w", encoding="utf-8", newline=NL).write(texto)


PATRON_FILA_NUMSTAT = re.compile(r"^(\d+|-)\t(\d+|-)\t")

print("=== EL CICLO ENTERO DE GATE 0 AL CIERRE, NUNCA run_phase1.py A SECAS ===")
c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
escribir("GATE0_CMD1", o + NL + "EXITCODE: %d" % c + NL)
print("   1/8 run_phase1.py --reaplico-curaduria  EXITCODE %d" % c)
c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
escribir("CICLO_ETIQUETAS", o + NL + "EXITCODE: %d" % c + NL)
print("   2/8 etiquetas_de_cara.py --aplicar      EXITCODE %d" % c)
c, o = correr([PY, "scripts/sync_assets_web.py"])
escribir("CICLO_SYNC", o + NL + "EXITCODE: %d" % c + NL)
print("   3/8 sync_assets_web.py                  EXITCODE %d" % c)
c, o = correr(["git", "diff", "HEAD", "--numstat", "--", "dataset/", "web/",
               "engine/"])
escribir("CICLO_NUMSTAT", o + NL + "EXITCODE: %d" % c + NL)
filas_ciclo = [x for x in o.split(NL) if PATRON_FILA_NUMSTAT.match(x)]
print("   4/8 git diff HEAD --numstat             EXITCODE %d | filas %d"
      % (c, len(filas_ciclo)))
c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
escribir("CONTEO", o + NL + "EXITCODE: %d" % c + NL)
print("   5/8 vuelta83_conteo_aristas.py WORK     EXITCODE %d" % c)
c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + NL + "EXITCODE: %d" % c + NL)
print("   6/8 vuelta85_medir_desfase_calibrado    EXITCODE %d" % c)
c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + NL + "EXITCODE: %d" % c + NL)
print("   7/8 engine/run_all_tests.py             EXITCODE %d" % c)
c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True,
              cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d" % c + NL)
print("   8/8a npx tsc --noEmit                   EXITCODE %d" % c)
c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + NL + "EXITCODE: %d" % c + NL)
print("   8/8b pnpm test                          EXITCODE %d" % c)

_c, head = correr(["git", "rev-parse", "HEAD"])
io.open(os.path.join(LOOP, "SALIDA_V%d_HEAD_CIERRE.txt" % VUELTA), "w",
        encoding="utf-8", newline=NL).write(head.strip() + NL)

w("=" * 78)
w("MEDICIONES DE CIERRE DE LA VUELTA %d, RECOMPUTADAS Y NO HEREDADAS" % VUELTA)
w("=" * 78)
w("")

w("A) LA IDENTIDAD AL CIERRE, LEIDA DE GIT")
w("   HEAD de cierre, sellado en docs/loop/SALIDA_V%d_HEAD_CIERRE.txt: %s"
  % (VUELTA, head.strip()))
_c, o = correr(["git", "log", "-1", "--format=%H%x09%ad%x09%s", "--date=iso"])
w("   %s" % o.strip()[:200])
_c, rama = correr(["git", "rev-parse", "--abbrev-ref", "HEAD"])
w("   rama: %s" % rama.strip())
w("")

w("B) LA SEDE DE LOS VEREDICTOS, REMEDIDA AL CIERRE POR LAS DOS CONVENCIONES")
mv = dos_convenciones("docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl: disco %d bytes | LF %d bytes | "
  "sha256 LF %s" % (mv["disco"], mv["lf"], mv["sha_lf"]))
w("   EL SELLO DE APERTURA DIJO 0a77b5a35a962621 POR LAS DOS. CALZA AL CIERRE: %s"
  % ("SI" if mv["sha_lf"] == "0a77b5a35a962621" else "NO, Y ESO ES ROJO"))
w("")

w("C) EL MARCADOR, RECONTADO AL CIERRE Y EN SU FORMA CANONICA")
filas = []
no_json = 0
for l in io.open(os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl"),
                 encoding="utf-8"):
    if not l.strip():
        continue
    try:
        filas.append(json.loads(l))
    except Exception:
        no_json += 1
clases = {}
for f in filas:
    clases[f.get("clase")] = clases.get(f.get("clase"), 0) + 1
puestos = sorted(f.get("puesto_intra") for f in filas
                 if f.get("puesto_intra") is not None)
huecos = [x for x in range(1, (max(puestos) if puestos else 0) + 1)
          if x not in set(puestos)]
w("   MARCADOR GLOBAL")
for k in sorted(clases):
    w("     %s %d" % (k, clases[k]))
w("   n = %d corte = %d huecos: %d dups(puesto): %d"
  % (len(filas), len(filas), len(huecos), len(puestos) - len(set(puestos))))
w("   CIFRA lineas que NO son JSON valido: %d" % no_json)
w("   LA CLAVE SE LLAMA `puesto_intra` Y NO `puesto`: es la caida que el")
w("   ejecutor de la 202 declaro en su TAREA 2, y aqui se mira donde hay algo.")
w("   ESTE CONTEO NO PASA POR EL RESOLUTOR Y SE DICE POR QUE: contar filas y")
w("   clases no toca ningun id, y P.1 manda el resolutor cuando el conteo TOCA")
w("   IDS. Ninguna clase se mueve en esta vuelta.")
w("")

w("D) LA SERIE `R.n` AL CIERRE, RECOMPUTADA")
c, salida_serie = correr([PY, "scripts/loop/serie_de_registros.py"])
io.open(os.path.join(LOOP, "SALIDA_V%d_SERIE_CIERRE.txt" % VUELTA), "w",
        encoding="utf-8", newline=NL).write(salida_serie)
for pat in (r"SIGUIENTE LIBRE[^\n]*", r"CIFRA entradas en total[^\n]*",
            r"CIFRA colisiones[^\n]*", r"CIFRA huecos[^\n]*"):
    for mm in re.finditer(pat, salida_serie):
        w("   %s" % mm.group(0).strip())
w("")

w("E) LA NOMINA Y EL CENSO AL CIERRE, CONTRA EL CONGELADO EN 135")
sys.path.insert(0, AQUI)
import verificar_mutaciones_viejas as VMV   # noqa: E402
w("   CIFRA entradas de la nomina, leidas de VMV.VIEJAS: %d" % len(VMV.VIEJAS))
w("   CALZA CON EL CONGELADO 135: %s"
  % ("SI" if len(VMV.VIEJAS) == 135 else "NO, medida %d" % len(VMV.VIEJAS)))
censo = VMV.arneses_del_directorio()
w("   CIFRA arneses que el censo reconoce en scripts/loop/: %d" % len(censo))
_u, faltan_n = VMV.arneses_que_faltan()
_u2, faltan_sin = VMV.arneses_que_faltan(vara=0)
w("   CIFRA arneses del censo FUERA de la nomina CON LA VARA %d: %d, y SIN vara: %d"
  % (VMV.VARA_DEL_CENSO, len(faltan_n), len(faltan_sin)))
for n in faltan_n:
    w("      FUERA DE LA NOMINA (con vara %d): %s" % (VMV.VARA_DEL_CENSO, n))
w("   NINGUN FICHERO DE ESTA VUELTA ENTRA AL CENSO, Y SE COMPRUEBA:")
mios = sorted(n for n in os.listdir(AQUI) if n.startswith("_v203_")
              or n.startswith("_gen_v203_") or n.startswith("vuelta203_"))
w("   CIFRA ficheros que esta vuelta anade a scripts/loop/: %d" % len(mios))
for n in mios:
    w("      %-46s en el censo: %s" % (n, "SI" if n in censo else "NO"))
w("   CIFRA de los mios que el censo VE: %d"
  % len([n for n in mios if n in censo]))
w("")

w("F) EL NUMSTAT DE LAS CUATRO SEDES, AL CERRAR")
for sede in ("dataset/", "web/", "engine/", "docs/plan/"):
    _c, o = correr(["git", "diff", "--numstat", "--", sede])
    f = [x for x in o.split(NL) if PATRON_FILA_NUMSTAT.match(x)]
    w("   CIFRA filas de numstat AL SALIR en %-12s %d" % (sede, len(f)))
    for x in f:
        w("      %s" % x.strip())
w("   LA UNICA ESCRITURA EN docs/plan/ DE ESTA VUELTA ES LA LINEA 41 DE")
w("   OPERACIONES.jsonl, y esa fila ya esta COMMITEADA, por eso el numstat")
w("   contra el arbol sale en cero.")
w("")

w("G) LAS SEDES QUE ESTA VUELTA MOVIO, REMEDIDAS AL CIERRE")
for rel in ("docs/PENDIENTES.md", "docs/plan/OPERACIONES.jsonl",
            "docs/loop/REPORTE.md"):
    m = dos_convenciones(rel)
    w("   %-34s disco %d bytes | LF %d bytes | sha256 LF %s"
      % (rel, m["disco"], m["lf"], m["sha_lf"]))
w("")

w("H) EL INVENTARIO DE SALIDAS, REMEDIDO AL CIERRE EN VEZ DE HEREDARSE")
w("   ESTA ES LA CIFRA QUE EL ACTA 202 MIDIO EN SU 5.2: el inventario ENVEJECE")
w("   DENTRO DE LA PROPIA VUELTA. La de la apertura no se copia: se remide, y")
w("   se declara que ESTA remedicion tambien tiene su instante.")
inv = sorted(n for n in os.listdir(LOOP)
             if re.match(r"^SALIDA_V%d_.*\.txt$" % VUELTA, n))
w("   CIFRA ficheros SALIDA_V%d en docs/loop/ AL CIERRE: %d" % (VUELTA, len(inv)))
vacios = []
for n in inv:
    t = os.path.getsize(os.path.join(LOOP, n))
    if t == 0:
        vacios.append(n)
    w("   %-58s %d bytes" % (n, t))
w("   CIFRA de esos que miden CERO bytes: %d" % len(vacios))
w("   LA APERTURA CONTO 1 EN SU BLOQUE J, Y NOMBRO LOS QUE IBAN A NACER DESPUES.")
w("   LOS QUE NACEN DESPUES DE ESTE BLOQUE, DECLARADOS AQUI POR SU NOMBRE:")
w("      SALIDA_V%d_TALLADOR_CABECERA.txt, SALIDA_V%d_TALLADOR_COMPARAR.txt y"
  % (VUELTA, VUELTA))
w("      SALIDA_V%d_CERRAR_REPORTE.txt, que nacen del cierre del reporte."
  % VUELTA)
w("")

w("I) EL HUECO DE LA BATERIA, DECLARADO Y MEDIDO AL CIERRE")
rb = "docs/loop/SALIDA_V%d_BATERIA.txt" % VUELTA
ruta_b = os.path.join(RAIZ, rb)
tr = sorted(n for n in os.listdir(LOOP)
            if re.match(r"^SALIDA_V%d_BATERIA_TRAMO_\d+\.txt$" % VUELTA, n))
w("   nombre: %s" % rb)
w("   existe: %s" % ("SI" if os.path.isfile(ruta_b) else "NO"))
w("   bytes medidos con os.path.getsize: %s"
  % (os.path.getsize(ruta_b) if os.path.isfile(ruta_b) else
     "NINGUNO, y el cero sale de que NO HAY FICHERO, no de medir uno vacio"))
w("   CIFRA ficheros SALIDA_V%d_BATERIA_TRAMO_N.txt: %d" % (VUELTA, len(tr)))
w("   atribucion: EL EJECUTOR DE LA VUELTA %d, y el motivo es LA CADENCIA de"
  % VUELTA)
w("   AUDITOR.md 6.1: la bateria corre CADA CINCO VUELTAS, en vuelta propia; la")
w("   200 lo fue y le toca a la 205. NO es una omision de esta vuelta.")
w("")

w("J) LAS RUTAS QUE EL REPORTE PUBLICA COMO PRUEBA, COMPROBADAS UNA A UNA")
w("   (EJECUTOR.md 1, LA RUTA QUE PROMETE PRUEBA ES CIFRA: si apunta a un")
w("   fichero inexistente o de CERO BYTES es CAIDA DE CIFRA.)")
texto_rep = dos_convenciones("docs/loop/REPORTE.md")["texto"]
rutas = sorted(set(re.findall(r"`((?:docs|scripts|dataset|web|engine)/[^`\s]+)`",
                              texto_rep)))
vivas = muertas = cero = 0
for r in rutas:
    ruta = os.path.join(RAIZ, r)
    if not os.path.exists(ruta):
        muertas += 1
        w("   AUSENTE  %s" % r)
    elif os.path.isfile(ruta) and os.path.getsize(ruta) == 0:
        cero += 1
        w("   CERO     %s" % r)
    else:
        vivas += 1
w("   CIFRA rutas distintas que el reporte publica: %d" % len(rutas))
w("   CIFRA vivas: %d | CIFRA ausentes: %d | CIFRA de cero bytes: %d"
  % (vivas, muertas, cero))
w("")
w("FIN DE LAS MEDICIONES DE CIERRE")

salida = NL.join(L) + NL
print(salida)
io.open(os.path.join(LOOP, "SALIDA_V%d_CIERRE_MEDICIONES.txt" % VUELTA), "w",
        encoding="utf-8", newline=NL).write(salida)
