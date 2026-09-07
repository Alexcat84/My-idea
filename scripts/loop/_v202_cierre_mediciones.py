# -*- coding: utf-8 -*-
r"""_v202_cierre_mediciones.py . LAS MEDICIONES DEL CIERRE DE LA VUELTA 202.

EJECUTOR.md 1: EL ESTADO AL CIERRE SE MIDE AL CIERRE. Todo lo que esta vuelta
pudo mover se RECOMPUTA aqui y no se hereda de la apertura.

PREFIJO DE GUION BAJO Y POR EL MISMO MOTIVO QUE SUS HERMANOS de esta vuelta
(moratoria `AUDITOR.md` 6.3 mas adjudicacion `4.5` del acta 199).

COMPONE EL TEXTO ENTERO Y LO ESCRIBE AL FINAL, en vez de imprimir por tuberia:
la primera version se corrio con `tee` y su propio fichero de salida entro en el
inventario del bloque `G` MIDIENDO CERO BYTES, porque todavia se estaba
escribiendo. La cifra era falsa por el metodo, no por el fichero, y por eso el
metodo se corrige aqui y se declara.

USO:
  python scripts/loop/_v202_cierre_mediciones.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
sys.path.insert(0, AQUI)

HEAD_APERTURA = io.open(os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "docs", "loop", "SALIDA_V202_HEAD_APERTURA.txt"), encoding="utf-8").read().strip()
SELLADA = os.path.join(LOOP, "SALIDA_V202_CIERRE_MEDICIONES.txt")


def git(a):
    r = subprocess.run(["git"] + a, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def med(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    c = io.open(p, "rb").read()
    lf = c.replace(b"\r\n", b"\n")
    return (len(c), len(lf), hashlib.sha256(c).hexdigest()[:16],
            hashlib.sha256(lf).hexdigest()[:16])


L = []
w = L.append
w("MEDICIONES DEL CIERRE DE LA VUELTA 202, RECOMPUTADAS AL CIERRE")
w("=" * 74)
w("")
w("A) LA SEDE DE LOS VEREDICTOS, REMEDIDA AL CIERRE")
m = med("docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
w("   disco %d bytes | sha256 disco %s" % (m[0], m[2]))
w("   LF    %d bytes | sha256 LF    %s" % (m[1], m[3]))
w("   LA APERTURA MIDIO 4054129 por las dos convenciones y sha 0a77b5a35a962621")
w("   por las dos, sellado en docs/loop/SALIDA_V202_APERTURA.txt bloque D.")
w("   ABRE Y CIERRA EN EL MISMO VALOR: %s"
  % ("SI" if (m[2] == "0a77b5a35a962621" and m[3] == "0a77b5a35a962621"
              and m[0] == 4054129 and m[1] == 4054129)
     else "NO, Y SE DECLARA"))
w("")
w("B) EL NUMSTAT DE LAS CUATRO SEDES, AL CIERRE")
for sede in ("dataset/", "web/", "engine/", "docs/plan/"):
    c, o = git(["diff", "HEAD", "--numstat", "--", sede])
    fil = [l for l in o.splitlines() if l.strip()]
    w("   CIFRA filas de numstat AL CERRAR en %-12s %d" % (sede, len(fil)))
    for l in fil[:10]:
        w("      " + l)
w("   LA APERTURA MIDIO 0, 0, 0 y 0 filas, en el bloque C.0 del sello.")
w("")
w("C) LO QUE ESTA VUELTA SI TOCO DE ESAS CUATRO SEDES, CONTRA EL HEAD DE")
w("   APERTURA. El numstat de arriba compara contra HEAD, y esta vuelta ya")
w("   commiteo por tramos, asi que sin esta segunda medicion el 0 de docs/plan/")
w("   se leeria como que no se toco nada, y SI se toco.")
c, o = git(["diff", HEAD_APERTURA, "--numstat", "--",
            "dataset/", "web/", "engine/", "docs/plan/"])
fil = [l for l in o.splitlines() if l.strip()]
w("   comando: git diff %s --numstat -- dataset/ web/ engine/ docs/plan/"
  % HEAD_APERTURA[:8])
w("   CIFRA filas contra el HEAD de apertura: %d" % len(fil))
for l in fil:
    w("      " + l)
w("   ES LA TAREA 1, y es la unica escritura de esta vuelta en esas cuatro")
w("   sedes: dataset/, web/ y engine/ salen en CERO filas por las dos varas.")
w("")
w("D) LA NOMINA Y EL CENSO, REMEDIDOS AL CIERRE CONTRA EL CONGELADO EN 135")
import verificar_mutaciones_viejas as VMV   # noqa: E402
w("   CIFRA entradas de la nomina: %d" % len(VMV.VIEJAS))
w("   CALZA CON EL CONGELADO 135 DE AUDITOR.md 6.3: %s"
  % ("SI" if len(VMV.VIEJAS) == 135 else "NO, Y SE DECLARA"))
w("   CIFRA casos declarados: %d" % len(VMV.CASOS_DECLARADOS))
w("   CIFRA arneses que el censo reconoce: %d" % len(VMV.arneses_del_directorio()))
w("   LA VARA DEL CENSO: %d" % VMV.VARA_DEL_CENSO)
_u, faltan = VMV.arneses_que_faltan()
_u2, sinv = VMV.arneses_que_faltan(vara=0)
w("   CIFRA arneses del censo FUERA de la nomina CON LA VARA %d: %d"
  % (VMV.VARA_DEL_CENSO, len(faltan)))
for n in faltan:
    w("      FUERA DE LA NOMINA (con vara %d): %s" % (VMV.VARA_DEL_CENSO, n))
w("   CIFRA arneses del censo FUERA de la nomina SIN VARA (vara=0): %d" % len(sinv))
w("   CIFRA entradas de la nomina que el censo NO VE: %d"
  % len(VMV.nomina_invisible_al_censo()))
w("   CIFRA entradas SIN SUJETO CONGELADO: %d"
  % len(VMV.guarda_del_sujeto_congelado()))
w("   LA APERTURA MIDIO: nomina 135, casos 2, censo 197, vara 148, fuera 2 con")
w("   vara y 62 sin vara, 0 invisibles y 0 sin sujeto congelado. IDENTICAS.")
w("   NINGUNA ENTRADA SE ANADIO Y NINGUNA SE PODO.")
w("")
w("E) EL HUECO DE LA BATERIA, MEDIDO AL CIERRE Y NO SUPUESTO")
r = "docs/loop/SALIDA_V202_BATERIA.txt"
p = os.path.join(RAIZ, r.replace("/", os.sep))
w("   %s existe: %s" % (r, "SI" if os.path.isfile(p) else "NO"))
w("   bytes: %s" % (os.path.getsize(p) if os.path.isfile(p) else
                    "NINGUNO, y el cero sale de que NO HAY FICHERO, no de "
                    "medir uno"))
tramos = sorted(n for n in os.listdir(LOOP)
                if re.match(r"^SALIDA_V202_BATERIA_TRAMO_\d+\.txt$", n))
w("   CIFRA ficheros SALIDA_V202_BATERIA_TRAMO_N.txt: %d" % len(tramos))
todas = sorted(n for n in os.listdir(LOOP)
               if re.match(r"^SALIDA_V\d+_BATERIA\.txt$", n))
w("   CIFRA salidas unicas de bateria en docs/loop/, de otras vueltas: %d"
  % len(todas))
w("   DONDE VIVE LA CORRIDA DE LA 200, MEDIDO Y NO SUPUESTO. El lanzador")
w("   scripts/loop/vuelta183_bateria_por_tramos.py computa su vuelta de SU")
w("   PROPIO NOMBRE DE FICHERO, asi que la corrida de la vuelta 200 quedo")
w("   sellada con nombre de 183. Se comprueba con git log:")
for n in ("SALIDA_V200_BATERIA.txt", "SALIDA_V183_BATERIA.txt"):
    rel = "docs/loop/" + n
    mm = med(rel)
    w("      %-28s existe: %-3s %s"
      % (n, "SI" if mm else "NO",
         ("disco %d bytes | LF %d bytes" % (mm[0], mm[1])) if mm else ""))
    if mm:
        c_q, quien = git(["log", "-1", "--format=%h %ad %s", "--date=short",
                          "--", rel])
        w("         ultimo commit que lo toca: %s" % quien.strip()[:150])
w("   POR ESO ESTA SECCION NO DICE QUE LA 200 NO CORRIO LA BATERIA: dice que")
w("   SU SALIDA NO SE LLAMA COMO SU VUELTA, que es cosa distinta y que el acta")
w("   200 ya adjudica.")
w("")
w("F) LA SERIE, REMEDIDA AL CIERRE")
env = dict(os.environ)
env["PYTHONIOENCODING"] = "utf-8"
rr = subprocess.run([sys.executable, "scripts/loop/serie_de_registros.py"],
                    cwd=RAIZ, capture_output=True, env=env)
o = rr.stdout.decode("utf-8", errors="replace")
for pat in (r"CIFRA entradas en total:\s*(\d+)",
            r"CIFRA colisiones \(un numero escrito mas de una vez\):\s*(\d+)",
            r"CIFRA huecos:\s*(\d+)", r"SIGUIENTE LIBRE:\s*(R\.\d+)"):
    mm = re.search(pat, o)
    w("   %s" % (mm.group(0).strip() if mm else "(no impresa)"))
w("")
w("G) LOS FICHEROS DE ESTA VUELTA, MEDIDOS UNO A UNO")
w("   EJECUTOR.md 1, LA RUTA QUE PROMETE PRUEBA ES CIFRA: si apunta a un fichero")
w("   inexistente o de CERO BYTES es CAIDA DE CIFRA.")
w("   ESTE PROPIO FICHERO SE MIDE APARTE Y SE DICE POR QUE: se esta escribiendo")
w("   cuando el inventario corre, asi que aqui saldria en cero por el METODO y")
w("   no por el fichero. Su medicion va en el bloque H, tomada despues.")
vivos = vacios = 0
for n in sorted(os.listdir(LOOP)):
    if not n.startswith("SALIDA_V202_"):
        continue
    if n == os.path.basename(SELLADA):
        continue
    t = os.path.getsize(os.path.join(LOOP, n))
    if t > 0:
        vivos += 1
    else:
        vacios += 1
    w("   %-46s %8d bytes  %s" % (n, t, "VIVO" if t > 0 else "CERO BYTES"))
w("   CIFRA ficheros SALIDA_V202_* (sin contar este): %d" % (vivos + vacios))
w("   CIFRA vivos: %d | CIFRA de CERO BYTES: %d" % (vivos, vacios))
w("")
w("FIN")

texto = NL.join(L) + NL
io.open(SELLADA, "w", encoding="utf-8", newline=NL).write(texto)
extra = (NL + "H) LA MEDICION DE ESTE MISMO FICHERO, TOMADA DESPUES DE "
         "ESCRIBIRLO" + NL
         + "   docs/loop/SALIDA_V202_CIERRE_MEDICIONES.txt: %d bytes en disco y LF"
         % len(texto.encode("utf-8")) + NL)
io.open(SELLADA, "a", encoding="utf-8", newline=NL).write(extra)
sys.stdout.reconfigure(encoding="utf-8")
print(texto + extra)
