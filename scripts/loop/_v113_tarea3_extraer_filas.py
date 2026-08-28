import json, io

TRAMOS = [
    "docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl",
    "docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl",
    "docs/plan/OP_E_03_LECTURA_TRAMO3_V98.jsonl",
    "docs/plan/OP_E_03_LECTURA_TRAMO4_V99.jsonl",
]
filas = []
for r in TRAMOS:
    with io.open(r, encoding="utf-8") as f:
        filas.extend(json.loads(l) for l in f if l.strip())

objetivo = [168, 170, 171, 173, 176, 178, 181, 183, 6, 8, 20, 21, 24, 25, 28, 29, 31,
            38, 40, 52, 62, 66, 80, 93, 147, 161, 172, 174, 175]
by_puesto = {f["puesto_tramo"]: f for f in filas}
out = []
for p in objetivo:
    f = by_puesto[p]
    out.append({
        "puesto": p,
        "dominio": f.get("dominio"),
        "madre": f.get("madre_de_la_bolsa"),
        "hijo": f.get("hijo_de_la_bolsa"),
        "paso_casado": f.get("paso_casado"),
        "clase": f.get("clase"),
        "direccion_leida": f.get("direccion_leida"),
        "razon": f.get("razon"),
        "correcciones": {k: v for k, v in f.items() if k.startswith("correccion_v")},
    })
with io.open("docs/loop/_v113_tarea3_filas_29.json", "w", encoding="utf-8") as g:
    json.dump(out, g, ensure_ascii=False, indent=1)
print("ok", len(out))
