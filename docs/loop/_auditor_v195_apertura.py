# -*- coding: utf-8 -*-
"""APERTURA DEL AUDITOR DE LA VUELTA 195. Computa el sujeto y SELLA, en un solo
proceso y ANTES de tocar `git log`, `git status` o `REPORTE.md`.

EL SUJETO NO LO ELIJO YO HOY: lo dejo CERRADO el auditor de la 194 en
`docs/loop/PROMPT_SIGUIENTE.md`, seccion LO QUE NO ENTRA, con estas palabras:
"EL TRAMO son los 30 puestos de docs/loop/_auditor_v194_ciega_blind.txt, que son
los mismos 30 de docs/loop/SALIDA_V193_T3_CIEGA.txt; EL DOBLE son sus 30 vecinos
deterministas con vecinos() IMPORTADA de
scripts/loop/vuelta182_tarea1c_relectura_al_doble.py y no copiada, con evitar
cargado de TODO lo consumido y contado de sus ficheros."
"""
import io, json, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

from vuelta182_tarea1c_relectura_al_doble import vecinos   # IMPORTADA, no copiada
import apertura_del_auditor as AP

NL = chr(10)
PAT = re.compile(r"puesto_intra[^0-9]{0,12}(\d+)")
TRAMO_F = "docs/loop/_auditor_v194_ciega_blind.txt"
GEMELO_F = "docs/loop/SALIDA_V193_T3_CIEGA.txt"
CONSUMIDO = [
    "docs/loop/_auditor_v189b_exclusion.txt",
    "docs/loop/_auditor_v190_exclusion.txt",
    "docs/loop/_auditor_v189b_ciega_blind.txt",
    "docs/loop/_auditor_v190_ciega_blind.txt",
    "docs/loop/SALIDA_V190_T4_CIEGA.txt",
    "docs/loop/SALIDA_V191_T2_CIEGA.txt",
    "docs/loop/_auditor_v192_ciega_blind.txt",
    "docs/loop/SALIDA_V192_T2_CIEGA.txt",
    "docs/loop/_auditor_v193_ciega_blind.txt",
    "docs/loop/SALIDA_V193_T3_CIEGA.txt",
    "docs/loop/_auditor_v194_ciega_blind.txt",
]

def puestos_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    t = io.open(p, encoding="utf-8", errors="replace").read()
    return sorted(set(int(x) for x in PAT.findall(t)))

def numeros_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    t = io.open(p, encoding="utf-8", errors="replace").read()
    return sorted(set(int(x) for x in re.findall(r"\d+", t)))

L = []
w = L.append
w("=" * 78)
w("APERTURA DEL AUDITOR, VUELTA 195. SELLO PRIMERO Y SOLO ESO.")
w("=" * 78)
w("   bitacora al arrancar: %s" % (", ".join(AP.bitacora()) or "(vacia)"))
w("   prohibidos tocados hasta aqui: %d" % len(AP.toques_prohibidos()))
w("")

w("A) EL TRAMO, LEIDO DE SU FICHERO Y NO TECLEADO")
tramo = puestos_de(TRAMO_F)
gemelo = puestos_de(GEMELO_F)
w("   %s -> %d puestos" % (TRAMO_F, len(tramo)))
w("   %s -> %d puestos" % (GEMELO_F, len(gemelo)))
w("   SON EL MISMO CONJUNTO: %s" % ("SI" if set(tramo) == set(gemelo) else
                                    "NO, difieren en %d" % len(set(tramo) ^ set(gemelo))))
w("   LOS 30 DEL TRAMO: %s" % ", ".join(str(x) for x in tramo))
w("")

w("B) EL UNIVERSO CONSUMIDO, CONTADO DE SUS FICHEROS")
evitar = set()
for rel in CONSUMIDO:
    dentro = numeros_de(rel) if rel.endswith("_exclusion.txt") else puestos_de(rel)
    if dentro is None:
        w("   ROJO: falta %s" % rel)
        print(NL.join(L)); sys.exit(1)
    antes = len(evitar)
    evitar |= set(dentro)
    w("   %-52s %4d puestos (+%d nuevos)" % (rel, len(dentro), len(evitar) - antes))
w("   CIFRA universo consumido: %d" % len(evitar))
w("")

w("C) EL ARCHIVO, PARA EL TECHO. Solo se leen los puesto_intra, ni una clase.")
puestos_archivo = []
with io.open(os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl"),
             encoding="utf-8") as fh:
    for linea in fh:
        if linea.strip():
            puestos_archivo.append(json.loads(linea).get("puesto_intra"))
maximo = max(puestos_archivo)
w("   CIFRA filas del archivo: %d | puesto maximo: %d" % (len(puestos_archivo), maximo))
w("")

w("D) EL DOBLE, CON vecinos() IMPORTADA Y NO COPIADA")
dobles = vecinos(tramo, maximo, evitar=evitar)
w("   CIFRA vecinos: %d" % len(dobles))
w("   LOS VECINOS: %s" % ", ".join(str(x) for x in dobles))
w("   SOLAPE con el tramo:            %d" % len(set(dobles) & set(tramo)))
w("   SOLAPE con el universo consumido: %d" % len(set(dobles) & evitar))
w("   ES EL DOBLE: %s" % ("SI, 30 mas 30 son 60" if len(dobles) == len(tramo)
                          else "NO, son %d frente a %d" % (len(dobles), len(tramo))))
w("")

CRITERIO = (
    "RELECTURA AL DOBLE del tramo de la vuelta 193/194 (AUDITOR.md 1.2), "
    "encargada POR ESCRITO Y POR ADELANTADO por el auditor de la 194 en "
    "docs/loop/PROMPT_SIGUIENTE.md, seccion LO QUE NO ENTRA, para que el sujeto "
    "no se pueda elegir despues de mirar. EL TRAMO son los 30 puestos de "
    "docs/loop/_auditor_v194_ciega_blind.txt, identicos a los de "
    "docs/loop/SALIDA_V193_T3_CIEGA.txt. EL DOBLE que sello hoy son sus 30 "
    "vecinos deterministas, elegidos con vecinos() IMPORTADA de "
    "scripts/loop/vuelta182_tarea1c_relectura_al_doble.py y no copiada, sobre el "
    "conjunto evitar de TODO lo consumido contado de sus once ficheros, de modo "
    "que el solape con el tramo y con el universo salga POR CONSTRUCCION. EL "
    "MOTIVO ESCRITO: dos discrepancias del auditor 194 cayeron FUERA de su "
    "marcado, en los puestos 612 y 2426. LA VARA CON LA QUE LEERE: "
    "docs/BANCO_DE_TEXTOS.md 9.6.1, LA VARA DE LA RAMA CONTENIDO-MANDA, literal: "
    "\"Si lo que el hijo a\u00f1ade a lo que la madre ya dice CABE EN UNA "
    "L\u00cdNEA, REPITE. Si trae un PROCEDIMIENTO que la madre no tiene, "
    "CONTIN\u00daA.\""
)

w("E) EL SELLO")
ok, informe = AP.sellar(criterio=CRITERIO, vuelta="195",
                        puestos=",".join(str(x) for x in dobles))
for l in informe:
    w("   " + l)
w("   VEREDICTO DE LA APERTURA: %s" % ("VERDE" if ok else "ROJO"))
print(NL.join(L))
io.open(os.path.join(RAIZ, "docs", "loop", "_auditor_v195_apertura.txt"),
        "w", encoding="utf-8", newline=NL).write(NL.join(L) + NL)
sys.exit(0 if ok else 1)
