# -*- coding: utf-8 -*-
"""vuelta124_tarea1f_caso_positivo_ventana.py . CASO POSITIVO del ENSANCHE de
verificar_cifras_del_plan.py (TAREA 1.f, encargo de la vuelta 124, remedio de
la caida 4.3 del acta de la vuelta 123: el contrato de la 123 solo veia el
par en la MISMA frase y por eso no cotejaba la correccion 2.a de su propia
vuelta, partida en dos frases).

Corre la guarda TRES veces:
  (1) Sobre una COPIA de docs/plan/OPERACIONES.jsonl DE HOY donde, dentro de
      la correccion declarada de OP-S-08, se cambia "la cifra real es 27
      casos" por "la cifra real es 99 casos", con --base 128d0e5b (el acta
      de la vuelta 122, ANTERIOR a la correccion 2.a de la 123): tiene que
      dar ROJO nombrando 99 contra 27.
  (2) Sobre el fichero REAL de hoy (sin tocar), con el mismo --base: tiene
      que dar VERDE cotejando 27 == 27 (antes del ensanche daba VERDE con
      "0 pares", porque el numero y la ruta caian en frases separadas).
  (3) El caso positivo VIEJO de la 123 (vuelta123_tarea1f_caso_positivo.py,
      --base ed916471): tiene que SEGUIR dando ROJO 32 contra 27. Si el
      ensanche rompe este caso, el ensanche esta mal (letra del encargo).

USO:
  python scripts/loop/vuelta124_tarea1f_caso_positivo_ventana.py
"""
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_PLAN = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")


def correr_guarda(base, work=None):
    args = [sys.executable, os.path.join(RAIZ, "scripts", "loop", "verificar_cifras_del_plan.py"),
            "--base", base]
    if work:
        args += ["--work", work]
    r = subprocess.run(args, cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")
    return r.returncode, r.stdout + r.stderr


def main():
    with io.open(RUTA_PLAN, encoding="utf-8") as f:
        txt = f.read()
    viejo = "la cifra real es 27 casos, no 32."
    nuevo = "la cifra real es 99 casos, no 32."
    if txt.count(viejo) != 1:
        raise SystemExit("ARNES ROTO: la frase esperada de OP-S-08 no aparece exactamente una vez (%d)" % txt.count(viejo))
    ruta_mut = os.path.join(tempfile.gettempdir(), "vuelta124_ops08_mut_99.jsonl")
    with io.open(ruta_mut, "w", encoding="utf-8") as f:
        f.write(txt.replace(viejo, nuevo))

    print("--- (1) copia mutada (99), --base 128d0e5b: esperado ROJO 99 vs 27 ---")
    ec1, out1 = correr_guarda("128d0e5b", ruta_mut)
    print(out1)
    if ec1 == 0:
        raise SystemExit("CAIDA: la copia mutada (99) dio VERDE")
    if "escribe 99, vitest da 27" not in out1:
        raise SystemExit("CAIDA: la copia mutada no nombro 99 contra 27")

    print("--- (2) fichero real, --base 128d0e5b: esperado VERDE 27 == 27 ---")
    ec2, out2 = correr_guarda("128d0e5b")
    print(out2)
    if ec2 != 0:
        raise SystemExit("CAIDA: el fichero real dio ROJO")
    if "27 == 27" not in out2:
        raise SystemExit("CAIDA: el fichero real no cotejo 27 == 27 (el ensanche no encontro el par)")

    print("--- (3) caso positivo viejo de la 123, --base ed916471: esperado ROJO 32 vs 27 ---")
    r = subprocess.run([sys.executable, os.path.join(RAIZ, "scripts", "loop",
                        "vuelta123_tarea1f_caso_positivo.py")], cwd=RAIZ,
                       capture_output=True, text=True, encoding="utf-8")
    print(r.stdout + r.stderr)
    if r.returncode != 0:
        raise SystemExit("CAIDA: el ensanche rompio el caso positivo viejo de la 123")

    print("CASO POSITIVO DEL ENSANCHE VERIFICADO: (1) ROJO 99/27, (2) VERDE 27==27, (3) el caso viejo de la 123 sigue ROJO 32/27.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
