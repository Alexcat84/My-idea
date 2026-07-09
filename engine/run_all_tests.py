# -*- coding: utf-8 -*-
"""Hotfix v2.2.2: corredor unico de tests del motor Python. Antes de esto,
cada test_*.py era un script suelto que se corria a mano, uno por uno --
asi es como test_reporte_tipo_oferta.py estuvo en rojo (en ambientes sin
ANTHROPIC_API_KEY) sin que nadie lo notara: no habia un solo comando que
los ejecutara todos y fallara con exit code != 0.

Cada test_*.py corre en su propio subproceso (no import directo): varios
tests hacen monkey-patching de prototipo_motor (pm.llamar_claude = ...,
pm.API_KEY = ...), y con import normal esos parches se acumularian sobre
el mismo modulo cacheado en sys.modules, contaminando el siguiente test.

Uso: python engine/run_all_tests.py"""
import subprocess
import sys
import time
from pathlib import Path

ENGINE_DIR = Path(__file__).parent


def descubrir_tests():
    return sorted(ENGINE_DIR.glob("test_*.py"))


def correr_test(ruta: Path):
    inicio = time.time()
    resultado = subprocess.run(
        [sys.executable, str(ruta)],
        cwd=str(ruta.parent),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    duracion = time.time() - inicio
    return resultado.returncode, resultado.stdout, resultado.stderr, duracion


def main():
    tests = descubrir_tests()
    if not tests:
        print("No se encontraron archivos test_*.py en engine/.")
        return 1

    print(f"Corredor unico de tests -- {len(tests)} archivo(s) encontrado(s)\n")

    fallidos = []
    for ruta in tests:
        nombre = ruta.name
        codigo, stdout, stderr, duracion = correr_test(ruta)
        if codigo == 0:
            print(f"  OK    {nombre} ({duracion:.1f}s)")
        else:
            fallidos.append((nombre, stdout, stderr, codigo))
            print(f"  FALLO {nombre} ({duracion:.1f}s) -- exit code {codigo}")

    print()
    if fallidos:
        print("=" * 70)
        print(f"  {len(fallidos)} de {len(tests)} test(s) fallaron")
        print("=" * 70)
        for nombre, stdout, stderr, codigo in fallidos:
            print(f"\n--- {nombre} (exit {codigo}) ---")
            if stdout.strip():
                print("[stdout]")
                print(stdout.strip())
            if stderr.strip():
                print("[stderr]")
                print(stderr.strip())
        return 1

    print(f"TODOS LOS TESTS PASARON ({len(tests)}/{len(tests)}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
