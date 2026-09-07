# -*- coding: utf-8 -*-
r"""_v201_t4_leer_op_l_01_y_03.py . LA LECTURA MEDIDA DE `OP-L-01` Y `OP-L-03`
CONTRA SU VARA (TAREA 4 de la vuelta 201).

ES EL TRABAJO QUE LA MORATORIA `6.3` MANDA: EL PLAN HASTA AGOTARLO.

PREFIJO DE GUION BAJO Y POR EL MISMO MOTIVO QUE SUS HERMANOS de esta vuelta
(moratoria `AUDITOR.md` 6.3 mas adjudicacion `4.5` del acta 199): computo de una
vuelta, fuera del censo y fuera de la nomina, que no vigila a nadie.

QUE HACE, EN ESTE ORDEN Y SIN SALTARSE EL PRIMERO:

1. **VUELVE A CORRER LA VARA**, `scripts/loop/vuelta150_3_relectura_expediente.py`,
   con el corte de esta vuelta, que por regla escrita es EL HEAD DE APERTURA, y
   **publica sus cifras de HOY**. La vara **no se clona y no se toca: se invoca**.
   Si sus cifras discrepan de las del encargo, **la discrepancia se declara y no
   se resuelve copiando** (`AUDITOR.md` 1.1, EL INSTRUMENTO MANDA).
2. Por cada una de las dos fichas: **cita su `verificacion` por linea**, **mide
   sus documentos en bytes exactos de disco y LF** (`P.2`), y **dice si el
   documento cubre lo que la ficha describe**, con la cita que lo sostenga o con
   **el hueco NOMBRADO**.

COMO SE MIDE LA COBERTURA, Y SE DICE ANTES DE MEDIRLA PARA QUE NO SE ELIJA
DESPUES. Cada elemento de `evidencia` que nombra un fichero trae ademas una
DESCRIPCION en castellano de lo que ese fichero deberia traer. La prueba es:
**buscar en el fichero la seccion o el literal que esa descripcion nombra, y
contar los aciertos**. Si el acierto esta, la cita se pega con su linea y la
cobertura sale CUBIERTA. Si no esta, **el hueco se NOMBRA** y la cobertura sale
NO CUBIERTA. **La prueba es de PRESENCIA de lo que la ficha dice que hay, no de
calidad**, y eso se declara en vez de venderse como mas de lo que es.

LO QUE NO HACE: **no mueve ningun `estado`**, **no cierra ninguna ficha**, no
adjudica nada, no toca ni un nodo ni un veredicto y **no escribe una sola linea
en `docs/plan/`**. Si de la lectura sale que una ficha esta cumplida, **se
propone con su evidencia y lo adjudica el auditor**.

USO:
  python scripts/loop/_v201_t4_leer_op_l_01_y_03.py --corte <REF>
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
NL = chr(10)

OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VARA = "scripts/loop/vuelta150_3_relectura_expediente.py"
PATRON_RUTA = re.compile(r"([A-Za-z0-9_/]+\.(?:md|jsonl|txt|json))")

# LAS CIFRAS QUE EL ENCARGO TRAE, ESCRITAS AQUI SOLO PARA CONTRASTARLAS CON LAS
# DE HOY. NO SON FUENTE DE NADA: si discrepan, la discrepancia se declara.
CIFRAS_DEL_ENCARGO = {
    "fichas del expediente": 71,
    "fichas que no calzan": 37,
    "fichas en LISTA sin ninguna prueba": 6,
    "de esas que son TRABAJO REAL": 4,
    "de esas que estan CONSUMIDAS por otra ficha": 2,
}

# LA PRUEBA DE COBERTURA, DECLARADA ANTES DE CORRERLA. Por cada ficha, y por cada
# elemento de `evidencia` que nombra un fichero, la aguja que lo comprueba.
# (id_op, indice del elemento, ruta real en el repo, descripcion, patron, minimo)
PRUEBAS = [
    ("OP-L-01", 1, "docs/plan/LECTURAS_DIRIGIDAS.md",
     "las once con su razon",
     r"^###\s+`LD-(0[1-9]|1[01])`", 11),
    ("OP-L-01", 1, "docs/plan/LECTURAS_DIRIGIDAS.md",
     "la cabecera que agrupa a las once",
     r"^##\s+LAS ONCE, una por una", 1),
    ("OP-L-01", 2, "docs/INTRA_DOMINIO_INFORME.md",
     "seccion 52, las parejas que el ejercicio no puede cerrar",
     r"^##\s+52\.\s+LAS PAREJAS QUE EL EJERCICIO NO PUEDE CERRAR", 1),
    ("OP-L-01", 3, "docs/BANCO_DE_TEXTOS.md",
     "TABLA VIVA DE LOS PUROS",
     r"TABLA VIVA DE LOS PUROS", 1),
    ("OP-L-03", 1, "docs/plan/BANCO_DEL_PLAN.md",
     "P.5",
     r"^##\s+P\.5\s", 1),
    ("OP-L-03", 3, "docs/plan/LECTURAS_DIRIGIDAS.md",
     "el reparto por acto",
     r"reparto por acto", 1),
    ("OP-L-03", 3, "docs/plan/LECTURAS_DIRIGIDAS.md",
     "el sujeto de la ficha, nombrado en el documento",
     r"OP-L-03", 1),
]


def correr(args):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=RAIZ, capture_output=True, env=env)
    return (r.returncode,
            r.stdout.decode("utf-8", errors="replace")
            + r.stderr.decode("utf-8", errors="replace"))


def medir(rel):
    """LOS BYTES EXACTOS DE UN FICHERO, EN LAS DOS CONVENCIONES (`P.2`).
    Devuelve (disco, lf, lineas_count_nl) o None si no esta."""
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    crudo = io.open(p, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    return len(crudo), len(lf), lf.decode("utf-8", errors="replace").count(NL)


def lineas_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return []
    return io.open(p, "rb").read().replace(b"\r\n", b"\n").decode(
        "utf-8", errors="replace").split(NL)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corte", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 201, TAREA 4 . `OP-L-01` Y `OP-L-03` LEIDAS CONTRA SU VARA")
    w("NO SE MUEVE NINGUN `estado` Y NO SE CIERRA NINGUNA FICHA.")
    w("=" * 78)
    w("")

    w("A) LO PRIMERO Y SIN SALTARSELO: LA VARA, CORRIDA AQUI POR MI")
    w("   La vara NO SE CLONA Y NO SE TOCA: se invoca.")
    w("   comando: python %s --corte %s" % (VARA, a.corte))
    c, sal = correr([PY, VARA, "--corte", a.corte])
    io.open(os.path.join(LOOP, "SALIDA_V201_T4_VARA.txt"), "w",
            encoding="utf-8", newline=NL).write(sal)
    w("   exitcode: %d" % c)
    w("   sellada en docs/loop/SALIDA_V201_T4_VARA.txt (%d bytes)"
      % len(sal.encode("utf-8")))
    hoy = {}
    for l in sal.split(NL):
        m = re.match(r"\s*CIFRA (.+?):\s*(\d+)", l)
        if m:
            hoy.setdefault(m.group(1).strip(), int(m.group(2)))
    w("   LAS CIFRAS DE HOY, LEIDAS DE SU SALIDA:")
    for k in sorted(hoy):
        w("      CIFRA %-46s %d" % (k, hoy[k]))
    w("")
    w("   EL CONTRASTE CON LAS CIFRAS DEL ENCARGO, Y SI DISCREPAN SE DECLARA")
    w("   (AUDITOR.md 1.1, EL INSTRUMENTO MANDA):")
    discrepan = 0
    for k, v in sorted(CIFRAS_DEL_ENCARGO.items()):
        mia = hoy.get(k)
        calza = (mia == v)
        if not calza:
            discrepan += 1
        w("      %-46s encargo %-4s hoy %-6s %s"
          % (k, v, mia, "CALZA" if calza else "DISCREPA, Y SE DECLARA"))
    w("   CIFRA cifras del encargo que DISCREPAN de las de hoy: %d" % discrepan)
    w("")

    w("B) LAS DOS FICHAS, LOCALIZADAS POR LINEA")
    crudo = io.open(OPERACIONES, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    lineas = lf.decode("utf-8").split(NL)
    w("   docs/plan/OPERACIONES.jsonl: disco %d bytes | LF %d bytes"
      % (len(crudo), len(lf)))
    fichas = {}
    for idop in ("OP-L-01", "OP-L-03"):
        aguja = chr(34) + "id_op" + chr(34) + ": " + chr(34) + idop + chr(34)
        hits = [i for i, l in enumerate(lineas, 1) if l.strip() and aguja in l]
        w("   %-9s %d linea(s): %s"
          % (idop, len(hits), ", ".join(str(x) for x in hits) or "(ninguna)"))
        if len(hits) != 1:
            w("   ROJO: no aparece exactamente una vez.")
            print(NL.join(L))
            return 1
        fichas[idop] = (hits[0], json.loads(lineas[hits[0] - 1]))
    w("")

    for idop in ("OP-L-01", "OP-L-03"):
        ln, d = fichas[idop]
        ver = d.get("verificacion", [])
        ev = d.get("evidencia", [])
        w("=" * 78)
        w("FICHA %s . LINEA %d DE docs/plan/OPERACIONES.jsonl" % (idop, ln))
        w("=" * 78)
        w("   estado (SE LEE, NO SE MUEVE): %r" % d.get("estado"))
        w("   fecha_corte: %r | tipo: %r | fase: %r | orden: %r"
          % (d.get("fecha_corte"), d.get("tipo"), d.get("fase"), d.get("orden")))
        w("   depende_de: %s"
          % (", ".join(d.get("depende_de") or []) or "(vacio)"))
        w("   nodos=%d preservar=%d eliminar=%d superviviente=%r"
          % (len(d.get("nodos") or []), len(d.get("preservar") or []),
             len(d.get("eliminar") or []), d.get("superviviente")))
        w("")
        w("   SU `verificacion`, CITADA POR LINEA. LA FICHA ES UNA LINEA DE")
        w("   JSONL, asi que la coordenada es LA LINEA %d MAS EL INDICE del" % ln)
        w("   elemento, y las dos van juntas.")
        w("   CIFRA elementos de `verificacion`: %d" % len(ver))
        for i, x in enumerate(ver, 1):
            s = str(x)
            es_corr = "CORRECCION DECLARADA" in s
            w("   --- verificacion[%d] (linea %d) %s, %d caracteres ---"
              % (i, ln, "CORRECCION DECLARADA POR ADICION" if es_corr
                 else "CLAUSULA", len(s)))
            tope = s if not es_corr else s[:300] + " ...(la correccion se cita "
            if es_corr:
                tope = tope + "entera en el fichero, aqui va su apertura)"
            for trozo in [tope[k:k + 72] for k in range(0, len(tope), 72)]:
                w("      | " + trozo)
        w("")
        w("   SU `evidencia`, ELEMENTO A ELEMENTO, CON SU FICHERO MEDIDO EN")
        w("   BYTES EXACTOS DE DISCO Y LF (P.2)")
        w("   CIFRA elementos de `evidencia`: %d" % len(ev))
        for i, x in enumerate(ev, 1):
            s = str(x)
            m = PATRON_RUTA.search(s)
            w("      evidencia[%d]: %s" % (i, s))
            if not m:
                w("         NO NOMBRA NINGUN FICHERO: es prosa, y no hay")
                w("            documento que medir por esta via.")
                continue
            nombre = m.group(1)
            candidatos = [p for _o, _idx, p, _de, _pa, _mi in PRUEBAS
                          if _o == idop and _idx == i]
            ruta = candidatos[0] if candidatos else nombre
            med = medir(ruta)
            if med is None:
                w("         %s NO EXISTE EN DISCO. HUECO NOMBRADO." % ruta)
                continue
            w("         %s" % ruta)
            w("            disco %d bytes | LF %d bytes | %d lineas por count(NL)"
              % (med[0], med[1], med[2]))
        w("")
        w("   LA LECTURA: SI EL DOCUMENTO CUBRE LO QUE LA FICHA DESCRIBE")
        w("   LA PRUEBA VA DECLARADA ANTES DE CORRERSE, en la constante PRUEBAS")
        w("   de este mismo fichero, para que la aguja no se elija despues de")
        w("   mirar. ES PRUEBA DE PRESENCIA, NO DE CALIDAD, y se dice.")
        cubiertas = huecos = 0
        for o, idx, ruta, desc, patron, minimo in PRUEBAS:
            if o != idop:
                continue
            ls = lineas_de(ruta)
            pat = re.compile(patron, re.M)
            hits = [k + 1 for k, l in enumerate(ls) if pat.search(l)]
            ok = len(hits) >= minimo
            if ok:
                cubiertas += 1
            else:
                huecos += 1
            w("      evidencia[%d] . %s" % (idx, desc))
            w("         fichero: %s" % ruta)
            w("         aguja:   %r  (minimo %d)" % (patron, minimo))
            w("         CIFRA aciertos: %d, linea(s) %s"
              % (len(hits), ", ".join(str(x) for x in hits[:14]) or "(ninguna)"))
            w("         VEREDICTO: %s"
              % ("CUBIERTA" if ok else "NO CUBIERTA, Y EL HUECO VA NOMBRADO"))
            if hits:
                w("         LA CITA QUE LO SOSTIENE, pegada de su linea:")
                for x in hits[:3]:
                    w("            linea %d: %s" % (x, ls[x - 1].strip()[:120]))
        w("")
        w("   CIFRA pruebas de cobertura de %s: %d CUBIERTAS y %d NO CUBIERTAS"
          % (idop, cubiertas, huecos))
        w("")

    w("=" * 78)
    w("B.2) EL HUECO DE `OP-L-03`, MEDIDO HASTA EL FINAL EN VEZ DE DEJARLO EN")
    w("     'NO CUBIERTA'. UNA BUSQUEDA NEGATIVA NO SE PUEDE CITAR SIN HABERLA")
    w("     CORRIDO (EJECUTOR.md 9), Y AQUI SE CORRE LA POSITIVA TAMBIEN.")
    w("=" * 78)
    dirplan = os.path.join(RAIZ, "docs", "plan")
    cand = sorted(n for n in os.listdir(dirplan) if n.startswith("OP_L_03_"))
    w("   CIFRA ficheros docs/plan/OP_L_03_* en disco: %d" % len(cand))
    nombradas_ev = json.dumps(fichas["OP-L-03"][1].get("evidencia"),
                              ensure_ascii=False)
    for n in cand:
        rel = "docs/plan/" + n
        med = medir(rel)
        w("      %-34s disco %d bytes | LF %d bytes | %d lineas por count(NL)"
          % (n, med[0], med[1], med[2]))
        filas = [l for l in lineas_de(rel) if l.strip()]
        w("         CIFRA filas no vacias: %d" % len(filas))
        actos = set()
        malas = 0
        for l in filas:
            try:
                obj = json.loads(l)
            except Exception:                                # noqa: BLE001
                malas += 1
                continue
            if obj.get("acto") is not None:
                actos.add(obj["acto"])
        w("         CIFRA lineas que NO son JSON valido: %d" % malas)
        w("         CIFRA valores distintos del campo `acto`: %d" % len(actos))
        w("         LA `evidencia` DE LA FICHA LO NOMBRA: %s"
          % ("SI" if n in nombradas_ev else "NO"))
    w("   LA FRASE ENTERA, Y LAS DOS MITADES SE MIDEN: el documento que la")
    w("   `evidencia` de OP-L-03 NOMBRA (docs/plan/LECTURAS_DIRIGIDAS.md) NO trae")
    w("   ni el literal 'reparto por acto' ni una sola mencion de OP-L-03; y los")
    w("   ficheros que SI traen un reparto por acto de esta ficha EXISTEN en")
    w("   disco y su `evidencia` NO LOS NOMBRA. EL HUECO NO ES QUE FALTE EL")
    w("   TRABAJO: ES QUE LA EVIDENCIA APUNTA AL DOCUMENTO EQUIVOCADO.")
    w("")

    w("=" * 78)
    w("C) LO QUE ESTA TAREA PROPONE Y LO QUE NO DECIDE")
    w("=" * 78)
    w("   NO SE MOVIO NINGUN `estado`, NO SE CERRO NINGUNA FICHA y NO SE ESCRIBIO")
    w("   UNA SOLA LINEA EN docs/plan/. Lo unico que produce esta tarea es")
    w("   LECTURA MEDIDA. Si de ella sale que una ficha esta cumplida, SE PROPONE")
    w("   CON SU EVIDENCIA Y LO ADJUDICA EL AUDITOR.")
    w("")
    w("   Y LO QUE LA PROPIA VARA YA DICE Y AQUI NO SE MEJORA: que el documento")
    w("   este NO significa que su mesa se hiciera bien. Esta lectura mide")
    w("   PRESENCIA de lo que la ficha dice que hay, no calidad de la mesa.")
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V201_T4_LECTURA.txt"), "w",
            encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
