# -*- coding: utf-8 -*-
"""vuelta58_triage_heredadas.py . EL TRIAGE DE LAS ONCE CITAS HEREDADAS, CON EL
VOLTEO DE CADA PUESTO MEDIDO POR GIT Y NO SUPUESTO.

DE SOLO LECTURA. Imprime; no toca ni una pagina.

POR QUE NACE: el acta 57 del auditor (discutible D7 a favor con el atraso
ENCARGADO, y pregunta 6) manda vaciar las once citas heredadas que el barrido
de puestos volteados lista, UNA A UNA y con triage:

  - la que sea RETRATO DE UN DIA CON SU CORTE DECLARADO se ROTULA como tal,
    que es el LIMITE DECLARADO del 9.10;
  - la ENVEJECIDA se CORRIGE con tachado y nota fechada por el carril 9.10.

LA DECISION NO SE PUEDE TOMAR SIN SABER CUANDO Y POR QUE SE MOVIO CADA PUESTO,
y eso es lo que este instrumento mide: recorre las versiones de
docs/INTRA_DOMINIO_VEREDICTOS.jsonl por git, encuentra el commit EXACTO en el
que cada puesto cambio de clase, e imprime su fecha y su asunto al lado de la
clase que la pagina cita. Ninguna de las once se rotula ni se corrige por
parecido: se decide contra esta medicion.

Uso: python scripts/loop/vuelta58_triage_heredadas.py
"""
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"

# Las once, copiadas de SALIDA_V57_PUESTOS_VOLTEADOS_CIERRE.txt (fichero, linea,
# puesto, clase citada). El instrumento re-mide la clase vigente por su cuenta.
ONCE = [
    ("docs/BANCO_DE_TEXTOS.md", 2914, 2488, "A"),
    ("docs/INTRA_DOMINIO_INFORME.md", 264, 393, "A"),
    ("docs/INTRA_DOMINIO_INFORME.md", 265, 395, "A"),
    ("docs/INTRA_DOMINIO_INFORME.md", 266, 396, "A"),
    ("docs/INTRA_DOMINIO_INFORME.md", 6597, 658, "A"),
    ("docs/INTRA_DOMINIO_INFORME.md", 6597, 678, "A"),
    ("docs/INTRA_DOMINIO_INFORME.md", 9989, 1222, "A"),
    ("docs/INTRA_DOMINIO_INFORME.md", 11743, 1865, "A"),
    ("docs/plan/02_DESTEJIDOS.md", 2569, 599, "B"),
    ("docs/plan/02_DESTEJIDOS.md", 3248, 233, "B"),
    ("docs/plan/02_DESTEJIDOS.md", 3606, 784, "B"),
]


def git(*args):
    p = subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True)
    return (p.returncode, p.stdout.decode("utf-8", "replace"),
            p.stderr.decode("utf-8", "replace"))


def clases_en(commit):
    rc, out, _ = git("show", "%s:%s" % (commit, VEREDICTOS))
    if rc != 0:
        return None
    d = {}
    for ln in out.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        try:
            r = json.loads(ln)
        except ValueError:
            continue
        d[r["puesto_intra"]] = r["clase"]
    return d


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("TRIAGE DE LAS ONCE CITAS HEREDADAS. EL VOLTEO, MEDIDO POR GIT.")
    print("=" * 78)
    print()

    rc, out, _ = git("log", "--format=%H|%ad|%s", "--date=short", "--", VEREDICTOS)
    historia = [l.split("|", 2) for l in out.splitlines() if l.strip()]
    historia.reverse()  # del mas viejo al mas nuevo
    print("  versiones del archivo de veredictos en la historia: %d" % len(historia))
    print()

    cache = {}
    def clases(h):
        if h not in cache:
            cache[h] = clases_en(h)
        return cache[h]

    vigentes = clases("HEAD")
    puestos = sorted({p for _, _, p, _ in ONCE})

    # el commit del ULTIMO cambio de clase de cada puesto
    volteo = {}
    for p in puestos:
        anterior = None
        for h, fecha, asunto in historia:
            c = clases(h)
            if c is None:
                continue
            ahora = c.get(p)
            if anterior is not None and ahora != anterior:
                volteo[p] = (h[:8], fecha, asunto, anterior, ahora)
            anterior = ahora

    for ruta, linea, puesto, citada in ONCE:
        vig = vigentes.get(puesto)
        print("-" * 78)
        print("%s:%d   puesto %d" % (ruta, linea, puesto))
        print("   la pagina cita clase %s | el archivo dice HOY clase %s" % (citada, vig))
        v = volteo.get(puesto)
        if v:
            print("   ULTIMO VOLTEO MEDIDO: %s de %s a %s, commit %s"
                  % (v[1], v[3], v[4], v[0]))
            print("      asunto: %s" % v[2][:150])
        else:
            print("   ULTIMO VOLTEO MEDIDO: ninguno en la historia del archivo")
        # el corte declarado en el entorno de la cita, si lo hay
        texto = io.open(os.path.join(RAIZ, ruta), encoding="utf-8").read().splitlines()
        ini, fin = max(0, linea - 20), min(len(texto), linea + 3)
        cortes = []
        for i in range(ini, fin):
            for m in re.finditer(r"corte\s+[\d.,]+|corte\s+declarado|"
                                 r"al\s+\d{1,2}\s+\w+\s+2026|"
                                 r"\d{1,2}\s+(?:ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)\w*\s+2026",
                                 texto[i], re.IGNORECASE):
                cortes.append("linea %d: %s" % (i + 1, m.group(0)))
        print("   CORTE DECLARADO en las 20 lineas de arriba: %s"
              % ("; ".join(cortes) if cortes else "NINGUNO"))
        print()

    print("=" * 78)
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
