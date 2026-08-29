# -*- coding: utf-8 -*-
"""vuelta123_tarea1f_caso_positivo.py . CASO POSITIVO de
verificar_cifras_del_plan.py (TAREA 1.f, encargo de la vuelta 123, remedio de
la racha de cifra publicada, acta de la vuelta 122 seccion 4.1).

Corre la guarda con `--base ed916471` (el acta de la vuelta 121, el commit
ANTERIOR a que la 122 escribiera el punto 0 de `verificacion` de `OP-S-08`
con "32 casos") contra el `docs/plan/OPERACIONES.jsonl` TAL COMO ESTA HOY, es
decir ANTES de que la correccion 2.a de esta misma vuelta lo toque. Tiene que
dar ROJO nombrando `OP-S-08`, 32 contra 27, y
`web/lib/engine/accesosResueltos.test.ts`.

Se corre DOS VECES en el encargo de la 123: (a) sobre el fichero real de HOY,
antes de 2.a (ROJO esperado, este script); (b) sobre el fichero YA CORREGIDO,
otra vez con el mismo --base (tiene que dar VERDE, se corre a mano en el
encargo tras aplicar 2.a; no es este script).

USO:
  python scripts/loop/vuelta123_tarea1f_caso_positivo.py
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    r = subprocess.run([sys.executable, os.path.join(RAIZ, "scripts", "loop",
                        "verificar_cifras_del_plan.py"), "--base", "ed916471"],
                       cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")
    print(r.stdout)
    print(r.stderr, file=sys.stderr)
    esperado = "OP-S-08.verificacion: escribe 32, vitest da 27, en `web/lib/engine/accesosResueltos.test.ts`"
    if r.returncode == 0:
        raise SystemExit("CAIDA DEL CASO POSITIVO: la guarda dio VERDE contra el OPERACIONES.jsonl de antes de 2.a")
    if esperado not in r.stdout:
        raise SystemExit("CAIDA DEL CASO POSITIVO: la guarda cayo en ROJO pero no nombro el par esperado")
    print("CASO POSITIVO VERIFICADO: la guarda cae en ROJO nombrando 32 contra 27, como se esperaba.")
    sys.exit(0)


if __name__ == "__main__":
    main()
