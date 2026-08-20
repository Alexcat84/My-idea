# -*- coding: utf-8 -*-
"""vuelta52_caso_positivo.py . EL CASO POSITIVO DE LA VUELTA 52: LAS GUARDAS QUE
ESTA VUELTA USA, PUESTAS A FALLAR A PROPOSITO.

POR QUE EXISTE, y es una guarda obligatoria del encargo (MODO DE EJECUCION
CONTINUA, guardas por operacion): una guarda que sale VERDE y nunca se ha visto
salir ROJA no prueba nada. El canon 9 del banco lo dice con otras palabras
(fallar ruidoso, no mentir calladito): si el instrumento no puede fallar, su
verde es decoracion. Esta vuelta lo sabe de primera mano: la guarda de
colisiones de la vuelta 51 salia verde mirando donde no era.

LAS TRES GUARDAS QUE SE PONEN A FALLAR, y son las tres de las que depende la
ejecucion de esta vuelta:

  1. GUARDA 1B (ningun absorbido puede ser semilla ni extremo de puente
     aprobado). Se fabrica un plan cuyo absorbido es una PUERTA conocida
     (domina_lo_que_compras, del acto 25, imposible por nomina) y se pasa al
     ejecutor en modo SIMULAR. Tiene que abortar sin escribir.

  2. GUARDA 2 (cobertura exacta de indices, cero olvidos). Se fabrica un plan
     que se OLVIDA de un paso del absorbido. Tiene que abortar sin escribir.
     Una perdida sin destino no es una perdida: es un olvido.

  3. LA GUARDA DE COLISIONES (el censo del archivo entero contra la cuenta
     esperada). Se le pide al censo que compare contra una cuenta FALSA y tiene
     que decir NO CALZA. Es la guarda que la vuelta 51 descubrio dormida.

EL PLAN FABRICADO SE ESCRIBE EN UN FICHERO TEMPORAL BAJO docs/loop/ Y SE BORRA
al terminar. El ejecutor se llama SIEMPRE en modo SIMULAR (sin --ejecutar), asi
que ni en el peor caso toca un nodo.

DE SOLO LECTURA sobre el dataset. Escribe y borra sus propios planes de mentira.

Uso: python scripts/loop/vuelta52_caso_positivo.py
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TMP_A = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v52_1b.json")
TMP_B = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v52_cobertura.json")
FUNDIR = os.path.join(RAIZ, "scripts", "loop", "vuelta49_fundir_tramo.py")
CENSO = os.path.join(RAIZ, "scripts", "loop", "vuelta51_censo_colisiones.py")


def base(titulo):
    return {
        "operacion": "OP-U-01",
        "tramo": titulo,
        "fecha": "2026-08-20",
        "vuelta": 52,
        "estado": "PLAN DE MENTIRA, CASO POSITIVO, NO SE EJECUTA NUNCA",
        "nomina": "docs/loop/RECOMPUTO_V52_APERTURA.jsonl",
        "dossier": "ninguno",
        "vara": "caso positivo",
        "declarados_y_no_fundidos": [],
    }


def correr(argv):
    p = subprocess.run([sys.executable] + argv, capture_output=True, cwd=RAIZ)
    return p.returncode, p.stdout.decode("utf-8", "replace") + p.stderr.decode("utf-8", "replace")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("CASO POSITIVO DE LA VUELTA 52: LAS GUARDAS PUESTAS A FALLAR")
    print("=" * 78)
    print()
    fallos = 0

    # ---------------------------------------------------------------- 1B
    # domina_lo_que_compras es SEMILLA DE ENTRADA y ademas extremo de puente
    # aprobado: es la puerta que hizo caer Gate 0 en la vuelta 48.
    plan = base("CASO POSITIVO 1B: el absorbido ES una puerta")
    plan["actos"] = [{
        "orden": 1,
        "miembros": ["investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor",
                     "domina_lo_que_compras"],
        "superviviente": "investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor",
        "absorbidos": ["domina_lo_que_compras"],
        "motivo": "MENTIRA DELIBERADA",
        "pasos": {},
        "condiciones": {},
        "nota_del_reparto": "MENTIRA DELIBERADA",
    }]
    io.open(TMP_A, "w", encoding="utf-8", newline="\n").write(
        json.dumps(plan, ensure_ascii=False, indent=1))
    rc, out = correr([FUNDIR, "--plan", TMP_A])
    ok = rc != 0 and "guarda 1B" in out and "ROJO" in out
    print("  1. GUARDA 1B con un absorbido que es PUERTA")
    print("     exit=%d | aborta sin escribir: %s" % (rc, "SI" if "SE ABORTA SIN ESCRIBIR" in out else "NO"))
    for l in out.splitlines():
        if "guarda 1B" in l or ("[ROJO]" in l and "1B" in l):
            print("     %s" % l.strip())
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MORDIO, ROJO"))
    fallos += 0 if ok else 1
    print()

    # ---------------------------------------------------------------- cobertura
    plan = base("CASO POSITIVO cobertura: el plan se olvida de un paso")
    plan["actos"] = [{
        "orden": 1,
        "miembros": ["criterios_equity_split", "split_igual_vs_desigual"],
        "superviviente": "criterios_equity_split",
        "absorbidos": ["split_igual_vs_desigual"],
        "motivo": "MENTIRA DELIBERADA",
        "pasos": {"split_igual_vs_desigual": {"1": "CUBIERTO:1", "2": "CUBIERTO:2", "4": "CUBIERTO:8"}},
        "condiciones": {"split_igual_vs_desigual": {"1": "CUBIERTO:2"}},
        "nota_del_reparto": "MENTIRA DELIBERADA: falta el paso 3",
    }]
    io.open(TMP_B, "w", encoding="utf-8", newline="\n").write(
        json.dumps(plan, ensure_ascii=False, indent=1))
    rc, out = correr([FUNDIR, "--plan", TMP_B])
    ok = rc != 0 and "guarda 2" in out and "ROJO" in out
    print("  2. GUARDA DE COBERTURA con un paso olvidado")
    print("     exit=%d | aborta sin escribir: %s" % (rc, "SI" if "SE ABORTA SIN ESCRIBIR" in out else "NO"))
    for l in out.splitlines():
        if "guarda 2" in l or "[ROJO]" in l:
            print("     %s" % l.strip())
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MORDIO, ROJO"))
    fallos += 0 if ok else 1
    print()

    # ---------------------------------------------------------------- censo
    rc, out = correr([CENSO, "--esperadas", "7",
                      "--titulo", "CASO POSITIVO: censo contra una cuenta FALSA de 7"])
    linea = [l for l in out.splitlines() if "CUENTA ESPERADA" in l]
    ok = bool(linea) and "CALZA: NO" in linea[0]
    print("  3. GUARDA DE COLISIONES contra una cuenta esperada FALSA")
    print("     %s" % (linea[0].strip() if linea else "no imprimio la comparacion"))
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MORDIO, ROJO"))
    fallos += 0 if ok else 1
    print()

    for p in (TMP_A, TMP_B):
        if os.path.exists(p):
            os.remove(p)
    print("  planes de mentira borrados: %s" % ", ".join(os.path.basename(p) for p in (TMP_A, TMP_B)))
    print()
    print("RESULTADO: %s" % ("LAS TRES GUARDAS MUERDEN" if not fallos
                             else "%d GUARDA(S) NO MORDIERON" % fallos))
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
