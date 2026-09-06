# -*- coding: utf-8 -*-
"""LAS CIFRAS DEL REPORTE DE LA 194, REMEDIDAS POR EL AUDITOR DE LA 195."""
import hashlib, io, os, sys
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
NL = chr(10)
sys.stdout.reconfigure(encoding="utf-8")

def mide(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    d = io.open(p, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return dict(rel=rel, disco=len(d), lf=len(lf),
                sha_disco=hashlib.sha256(d).hexdigest(),
                sha_lf=hashlib.sha256(lf).hexdigest(),
                nl=lf.count(b"\n"), split=len(lf.split(b"\n")),
                no_vacias=len([l for l in lf.split(b"\n") if l.strip()]))

FICHEROS = ["docs/loop/REPORTE.md", "docs/loop/SALIDA_V194_BATERIA.txt",
            "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
            "docs/loop/SALIDA_V194_BATERIA_COMPUESTA.txt",
            "docs/loop/SALIDA_V194_TALLADOR_CABECERA.txt"]
print("=" * 78)
print("A) LOS FICHEROS QUE EL REPORTE PUBLICA CON CIFRA, REMEDIDOS EN BYTES EXACTOS")
print("=" * 78)
for rel in FICHEROS:
    m = mide(rel)
    if not m:
        print("   ROJO, NO EXISTE: %s" % rel); continue
    print("   %s" % rel)
    print("      disco %d bytes | LF %d bytes | count(NL) %d | split %d | no vacias %d"
          % (m["disco"], m["lf"], m["nl"], m["split"], m["no_vacias"]))
    print("      sha256 disco %s | sha256 LF %s" % (m["sha_disco"][:16], m["sha_lf"][:16]))

print("")
print("=" * 78)
print("B) LAS DIEZ SELLADAS DE LA BATERIA. NINGUNA PUEDE MEDIR CERO BYTES.")
print("=" * 78)
ceros = 0
for n in range(1, 11):
    m = mide("docs/loop/SALIDA_V194_BATERIA_TRAMO_%d.txt" % n)
    if not m:
        print("   ROJO, NO EXISTE el tramo %d" % n); ceros += 1; continue
    if m["disco"] == 0:
        ceros += 1
    print("   tramo %2d | disco %6d bytes | LF %6d | %4d lineas | sha256 LF %s"
          % (n, m["disco"], m["lf"], m["nl"], m["sha_lf"][:16]))
print("   CIFRA selladas de cero bytes o ausentes: %d" % ceros)

print("")
print("=" * 78)
print("C) LA NOMINA DE LA BATERIA, CONTADA DEL INSTRUMENTO")
print("=" * 78)
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import verificar_mutaciones_viejas as VMV
print("   CIFRA len(VMV.VIEJAS): %d" % len(VMV.VIEJAS))
print("   vuelta mas alta nombrada en la nomina: %s"
      % max(int(x) for e in VMV.VIEJAS for x in
            __import__("re").findall(r"vuelta(\d+)", str(e))))

print("")
print("=" * 78)
print("D) LA GUARDA DURABLE DEL FICHERO DEL TURNO (.gitignore)")
print("=" * 78)
gi = io.open(os.path.join(RAIZ, ".gitignore"), encoding="utf-8").read()
hit = [l for l in gi.replace(chr(13), "").split(NL) if "TURNO_DEL_AUDITOR" in l]
print("   lineas de .gitignore que lo nombran: %d -> %s" % (len(hit), hit))
