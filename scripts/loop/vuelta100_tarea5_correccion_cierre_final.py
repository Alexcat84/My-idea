# -*- coding: utf-8 -*-
r"""vuelta100_tarea5_correccion_cierre_final.py . VUELTA 100, TAREA 5,
SEGUNDA CORRECCION DE CIERRE EN LA MISMA VUELTA: la propia TAREA 5 encontro
dos discutibles nuevos (172, 161) DESPUES de que la TAREA 4 ya hubiera
publicado 92/91 (49,7%). Publicar esa cifra sin recomputarla otra vez seria
la MISMA especie de caida que origino toda esta vuelta (acta 99, 4.4):
medir, corregir, y no recomputar el agregado.

Se ancla DETRAS del parrafo de correccion de la TAREA 4 (no lo borra), en
los tres sitios aditivos (`docs/plan/04_ENLACES.md`, `docs/PENDIENTES.md`,
`docs/plan/OPERACIONES.jsonl`). El cuarto sitio, `docs/loop/REPORTE.md`, se
sobreescribe entero por el reporte de esta vuelta (EJECUTOR.md 7): no se
toca aqui.

MECANICA DE ROJO: si `contar_cierre_efectivo.py` no da la cifra esperada, si
el ancla de la correccion de la TAREA 4 no aparece exactamente una vez en
cada sitio, o si la correccion de la TAREA 5 ya esta escrita.

USO:
  python scripts/loop/vuelta100_tarea5_correccion_cierre_final.py --simular
  python scripts/loop/vuelta100_tarea5_correccion_cierre_final.py --aplicar
"""
import argparse
import importlib.util
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ENLACES = os.path.join(RAIZ, "docs", "plan", "04_ENLACES.md")
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
PENDIENTES = os.path.join(RAIZ, "docs", "PENDIENTES.md")

CCE_RUTA = os.path.join(RAIZ, "scripts", "loop", "contar_cierre_efectivo.py")
spec = importlib.util.spec_from_file_location("contar_cierre_efectivo", CCE_RUTA)
cce = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cce)

ANCLA = "LA CIFRA BUENA ES **92 / 91 (49,7%)**."
MARCA = "CORRECCION DECLARADA (vuelta 100, TAREA 5"
MARCA_OPERACIONES = "SEGUNDA CORRECCION DE CIERRE (vuelta 100, TAREA 5)"

ESPERADO = (90, 93, "50,8")


def texto(d, pct):
    return (
        "\n\n**%s, LA TAREA 5 DE LA MISMA VUELTA ENCONTRO DOS DISCUTIBLES "
        "NUEVOS (172 y 161) DESPUES DE ESTA CORRECCION.) LO DE ARRIBA NO SE "
        "BORRA: era la cifra buena SOLO con la TAREA 3 aplicada.** Recontado "
        "otra vez con `scripts/loop/contar_cierre_efectivo.py` (aplica "
        "tambien `correccion_v100` de los pares 172 y 161, TAREA 5 de esta "
        "vuelta): **clase A %d, B %d, C %d (par %s), D %d; direccion leida "
        "y afirmada %d, NO RESUELTA %d (%s%%); invertidas %d (pares %s).** "
        "LA CIFRA VIGENTE AL CIERRE DE ESTA VUELTA ES **%d / %d (%s%%)**."
        % (MARCA, d["clases"]["A"], d["clases"]["B"], d["clases"]["C"],
           ", ".join(str(x) for x in d["c"]), d["clases"]["D"],
           d["con_dir"], len(d["sin_dir"]), pct,
           len(d["invertidas"]), ", ".join(str(x) for x in d["invertidas"]),
           d["con_dir"], len(d["sin_dir"]), pct)
    )


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--simular", action="store_true")
    g.add_argument("--aplicar", action="store_true")
    a = ap.parse_args()

    fallos = []
    d, fallos_cce = cce.cifras(cce.TRAMOS_OP_E_03_POR_DEFECTO)
    if fallos_cce:
        fallos.append("contar_cierre_efectivo.py no dio verde: %s" % "; ".join(fallos_cce))
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    pct = ("%.1f" % (100.0 * len(d["sin_dir"]) / d["n"])).replace(".", ",")
    if (d["con_dir"], len(d["sin_dir"]), pct) != ESPERADO:
        print("ROJO: la cifra medida es %d/%d (%s%%), se esperaba %s/%s (%s%%). "
              "NO SE ESCRIBE NADA." % (d["con_dir"], len(d["sin_dir"]), pct,
                                        ESPERADO[0], ESPERADO[1], ESPERADO[2]))
        return 1

    enlaces = io.open(ENLACES, encoding="utf-8").read()
    pendientes = io.open(PENDIENTES, encoding="utf-8").read()
    ops = [json.loads(l) for l in io.open(OPERACIONES, encoding="utf-8") if l.strip()]
    objetivo = [o for o in ops if o.get("id_op") == "OP-E-03"]

    if enlaces.count(ANCLA) != 1:
        fallos.append("el ancla de la correccion TAREA 4 en 04_ENLACES.md aparece %d veces"
                      % enlaces.count(ANCLA))
    elif MARCA in enlaces:
        fallos.append("04_ENLACES.md ya trae la segunda correccion de la TAREA 5")

    if pendientes.count(ANCLA) != 1:
        fallos.append("el ancla de la correccion TAREA 4 en PENDIENTES.md aparece %d veces"
                      % pendientes.count(ANCLA))
    elif MARCA in pendientes:
        fallos.append("PENDIENTES.md ya trae la segunda correccion de la TAREA 5")

    if len(objetivo) != 1:
        fallos.append("OP-E-03 aparece %d veces, se esperaba 1" % len(objetivo))
    elif MARCA_OPERACIONES in (objetivo[0].get("nota") or ""):
        fallos.append("la nota de OP-E-03 ya trae la segunda correccion de la TAREA 5")

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    t = texto(d, pct)
    print("=" * 100)
    print("SEGUNDA CORRECCION DE CIERRE, VUELTA 100 TAREA 5 (%s)" % ("SIMULACION" if a.simular else "APLICADO"))
    print("=" * 100)
    print("CIFRA VIGENTE: %d / %d (%s%% NO RESUELTA)" % (d["con_dir"], len(d["sin_dir"]), pct))
    print(t)

    if a.simular:
        print("SIMULACION: no se escribio nada.")
        return 0

    io.open(ENLACES, "w", encoding="utf-8", newline="\n").write(enlaces.replace(ANCLA, ANCLA + t, 1))
    io.open(PENDIENTES, "w", encoding="utf-8", newline="\n").write(pendientes.replace(ANCLA, ANCLA + t, 1))

    objetivo[0]["nota"] = (objetivo[0].get("nota") or "") + (
        " %s: LA TAREA 5 DE ESTA MISMA VUELTA ENCONTRO DOS DISCUTIBLES NUEVOS "
        "(172, 161, `correccion_v100`), DESPUES DE LA CORRECCION DE LA TAREA 4. "
        "Recontado otra vez con scripts/loop/contar_cierre_efectivo.py: clase A "
        "%d, B %d, C %d, D %d; direccion leida y afirmada %d, NO RESUELTA %d "
        "(%s%%); invertidas %d. LA CIFRA VIGENTE AL CIERRE DE ESTA VUELTA ES %d "
        "/ %d (%s%%)." % (MARCA_OPERACIONES, d["clases"]["A"], d["clases"]["B"],
                          d["clases"]["C"], d["clases"]["D"], d["con_dir"],
                          len(d["sin_dir"]), pct, len(d["invertidas"]),
                          d["con_dir"], len(d["sin_dir"]), pct))
    with io.open(OPERACIONES, "w", encoding="utf-8", newline="\n") as f:
        for o in ops:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")

    print()
    print("APLICADO.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
