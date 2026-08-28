# -*- coding: utf-8 -*-
r"""vuelta100_tarea4_correccion_cierre.py . VUELTA 100, TAREA 4: LA CORRECCION
DE LA CIFRA DE CIERRE DE `OP-E-03` EN LOS SITIOS ADITIVOS (acta 99, seccion 2 y
4.4). Corre DESPUES de la TAREA 1 (instrumento) y DESPUES de la TAREA 3
(relectura conjunta de 174 y 175), para escribir la cifra UNA sola vez.

LA CIFRA SALE DE `scripts/loop/contar_cierre_efectivo.py`, corrido en esta
vuelta, no de memoria ni de la aritmetica anticipada del acta.

TOCA TRES DE LOS CUATRO SITIOS QUE EL ACTA 99 NOMBRA (linea 35602 a 35606):
`docs/plan/04_ENLACES.md`, `docs/plan/OPERACIONES.jsonl` (nota de `OP-E-03`) y
`docs/PENDIENTES.md`. EL CUARTO SITIO, `docs/loop/REPORTE.md`, NO SE TOCA
AQUI: ese fichero se SOBREESCRIBE ENTERO cada vuelta (EJECUTOR.md 7), asi que
su correccion es que el reporte de esta vuelta publique la cifra buena
directamente, no un addendum sobre el fichero viejo.

CADA SITIO SE ESCRIBE ADITIVO: el texto viejo NO SE BORRA, se ancla un
parrafo de correccion declarada detras.

MECANICA DE ROJO, y no escribe nada si salta: (i) el ancla de cada sitio no
aparece exactamente una vez; (ii) la correccion de ese sitio para esta vuelta
ya esta escrita; (iii) `contar_cierre_efectivo.py` no corre en verde; (iv) la
cifra que devuelve no es la que este script espera citar (compara contra la
cifra medida, no al reves: si difieren, ROJO y se declara la discrepancia en
vez de escribir un numero no verificado).

USO:
  python scripts/loop/vuelta100_tarea4_correccion_cierre.py --simular
  python scripts/loop/vuelta100_tarea4_correccion_cierre.py --aplicar
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

MARCA = "CORRECCION DECLARADA (vuelta 100, TAREA 4"

ANCLA_ENLACES = (
    "| direccion leida y afirmada | **95** |\n"
    "| direccion NO RESUELTA, declarada | **88** (48,1%) |\n"
    "| direcciones invertidas y afirmadas | **2** (pares 16, 114) |\n"
    "| aristas escritas o retiradas en toda la operacion | **0** |\n"
)

ANCLA_PENDIENTES = (
    "| direccion leida y afirmada | **95** |\n"
    "| direccion NO RESUELTA, declarada | **88** (48,1%) |\n"
    "| direcciones invertidas y afirmadas | **2** (pares 16, 114) |\n"
    "| aristas escritas o retiradas en toda la operacion | **0** |\n"
)

MARCA_OPERACIONES = "CORRECCION DE CIERRE (vuelta 100, TAREA 4)"


def texto_correccion(d, pct):
    return (
        "\n**%s, encargo de la vuelta 99 acta seccion 2 y 4.4.) LA TABLA DE "
        "ARRIBA NO SE BORRA: es el texto viejo, y era la cifra CRUDA (campo "
        "`direccion_leida` sin corregir).** Recontado con "
        "`scripts/loop/contar_cierre_efectivo.py` (aplica `correccion_v99` "
        "del par 147 y `correccion_v100` de los pares 174 y 175, TAREA 3 de "
        "esta vuelta): **clase A %d, B %d, C %d (par %s), D %d; direccion "
        "leida y afirmada %d, NO RESUELTA %d (%s%%); invertidas %d (pares "
        "%s).** LA CIFRA BUENA ES **%d / %d (%s%%)**."
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
    esperado = (92, 91, "49,7")
    if (d["con_dir"], len(d["sin_dir"]), pct) != esperado:
        print("ROJO: la cifra medida es %d/%d (%s%%), se esperaba %s/%s (%s%%). "
              "NO SE ESCRIBE NADA, se declara la discrepancia."
              % (d["con_dir"], len(d["sin_dir"]), pct, esperado[0], esperado[1], esperado[2]))
        return 1

    enlaces = io.open(ENLACES, encoding="utf-8").read()
    pendientes = io.open(PENDIENTES, encoding="utf-8").read()
    ops = [json.loads(l) for l in io.open(OPERACIONES, encoding="utf-8") if l.strip()]
    objetivo = [o for o in ops if o.get("id_op") == "OP-E-03"]

    if enlaces.count(ANCLA_ENLACES) != 1:
        fallos.append("el ancla de la tabla en 04_ENLACES.md aparece %d veces, se esperaba 1"
                      % enlaces.count(ANCLA_ENLACES))
    elif MARCA in enlaces:
        fallos.append("04_ENLACES.md ya trae la correccion de la vuelta 100")

    if pendientes.count(ANCLA_PENDIENTES) != 1:
        fallos.append("el ancla de la tabla en PENDIENTES.md aparece %d veces, se esperaba 1"
                      % pendientes.count(ANCLA_PENDIENTES))
    elif MARCA in pendientes:
        fallos.append("PENDIENTES.md ya trae la correccion de la vuelta 100")

    if len(objetivo) != 1:
        fallos.append("OP-E-03 aparece %d veces en OPERACIONES.jsonl, se esperaba 1" % len(objetivo))
    elif MARCA_OPERACIONES in (objetivo[0].get("nota") or ""):
        fallos.append("la nota de OP-E-03 ya trae la correccion de la vuelta 100")

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    texto = texto_correccion(d, pct)
    print("=" * 100)
    print("CORRECCION DE CIERRE, VUELTA 100 TAREA 4 (%s)" % ("SIMULACION" if a.simular else "APLICADO"))
    print("=" * 100)
    print("CIFRA BUENA: %d / %d (%s%% NO RESUELTA)" % (d["con_dir"], len(d["sin_dir"]), pct))
    print(texto)

    if a.simular:
        print("SIMULACION: no se escribio nada.")
        return 0

    io.open(ENLACES, "w", encoding="utf-8", newline="\n").write(
        enlaces.replace(ANCLA_ENLACES, ANCLA_ENLACES + texto, 1))
    io.open(PENDIENTES, "w", encoding="utf-8", newline="\n").write(
        pendientes.replace(ANCLA_PENDIENTES, ANCLA_PENDIENTES + texto, 1))

    objetivo[0]["nota"] = (objetivo[0].get("nota") or "") + (
        " %s: LA CIFRA DE CIERRE PUBLICADA EN LA VUELTA 99 (95/88, 48,1%%) "
        "ERA CRUDA, CIEGA A `correccion_v99` DEL PAR 147. Recontada con "
        "scripts/loop/contar_cierre_efectivo.py tras la relectura conjunta "
        "de la TAREA 3 de esta vuelta (pares 174 y 175, `correccion_v100`): "
        "clase A %d, B %d, C %d, D %d; direccion leida y afirmada %d, NO "
        "RESUELTA %d (%s%%); invertidas %d. LA CIFRA VIGENTE ES %d / %d "
        "(%s%%)." % (MARCA_OPERACIONES, d["clases"]["A"], d["clases"]["B"],
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
