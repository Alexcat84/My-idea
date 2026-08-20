# -*- coding: utf-8 -*-
"""vuelta53_caso_positivo.py . EL CASO POSITIVO DE LA VUELTA 53: LAS GUARDAS QUE
ESTA VUELTA USA, PUESTAS A FALLAR A PROPOSITO.

SUCESOR DECLARADO de scripts/loop/vuelta52_caso_positivo.py, al que NO
reemplaza. DOS cambios, los dos con su motivo escrito:

  a) LAS NOMINAS DE MENTIRA SE ACTUALIZAN. El caso positivo de la vuelta 52
     fabricaba su plan de cobertura con criterios_equity_split absorbiendo a
     split_igual_vs_desigual, y aquella misma vuelta ejecuto esa fusion: hoy
     split_igual_vs_desigual esta DEPRECADO y el plan de mentira caeria por la
     guarda 1 (miembro ya deprecado) en vez de por la guarda 2, que es la que
     se quiere ver morder. Una mentira que falla por el motivo equivocado no
     prueba la guarda que dice probar.

  b) SE ANADE UNA CUARTA GUARDA, LA DEL INCISO VERBATIM, porque es de la que
     esta vuelta mas depende: SIETE de los doce actos llevan marcas INCISO, y
     la marca solo es honesta si su primer campo es un trozo LITERAL del paso
     del nodo que muere. Si el ejecutor pudiera escribir ahi una parafrasis, el
     instrumento estaria redactando texto nuevo dentro de un nodo publicado sin
     que nadie lo viera.

POR QUE EXISTE, y es una guarda obligatoria del encargo (MODO DE EJECUCION
CONTINUA): una guarda que sale VERDE y nunca se ha visto salir ROJA no prueba
nada. El canon 9 del banco lo dice con otras palabras (fallar ruidoso, no mentir
calladito).

EL PLAN FABRICADO SE ESCRIBE EN UN FICHERO TEMPORAL BAJO docs/loop/ Y SE BORRA
al terminar. El ejecutor se llama SIEMPRE en modo SIMULAR (sin --ejecutar), asi
que ni en el peor caso toca un nodo.

DE SOLO LECTURA sobre el dataset. Escribe y borra sus propios planes de mentira.

Uso: python scripts/loop/vuelta53_caso_positivo.py
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TMP_A = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v53_1b.json")
TMP_B = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v53_cobertura.json")
TMP_C = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v53_inciso.json")
FUNDIR = os.path.join(RAIZ, "scripts", "loop", "vuelta49_fundir_tramo.py")
CENSO = os.path.join(RAIZ, "scripts", "loop", "vuelta51_censo_colisiones.py")


def base(titulo):
    return {
        "operacion": "OP-U-01",
        "tramo": titulo,
        "fecha": "2026-08-20",
        "vuelta": 53,
        "estado": "PLAN DE MENTIRA, CASO POSITIVO, NO SE EJECUTA NUNCA",
        "nomina": "docs/loop/RECOMPUTO_V52_CIERRE.jsonl",
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
    print("CASO POSITIVO DE LA VUELTA 53: LAS CUATRO GUARDAS PUESTAS A FALLAR")
    print("=" * 78)
    print()
    fallos = 0

    # ---------------------------------------------------------------- 1B
    # domina_lo_que_compras es SEMILLA DE ENTRADA y ademas extremo de puente
    # aprobado: es la puerta que hizo caer Gate 0 en la vuelta 48. Sigue viva.
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
    # LA NOMINA DE HOY: value_proposition_canvas absorbiendo a
    # customer_profile_value_map, que es el acto 1 del lote A de esta vuelta.
    # Los dos estan VIVOS al correr esto, asi que la guarda 1 pasa y la que
    # tiene que morder es la 2. El plan se olvida del paso 3 del absorbido.
    plan = base("CASO POSITIVO cobertura: el plan se olvida de un paso")
    plan["actos"] = [{
        "orden": 1,
        "miembros": ["value_proposition_canvas", "customer_profile_value_map"],
        "superviviente": "value_proposition_canvas",
        "absorbidos": ["customer_profile_value_map"],
        "motivo": "MENTIRA DELIBERADA",
        "pasos": {"customer_profile_value_map": {"1": "CUBIERTO:2", "2": "CUBIERTO:3", "4": "APPEND"}},
        "condiciones": {"customer_profile_value_map": {"1": "CUBIERTO:1", "2": "APPEND"}},
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

    # ---------------------------------------------------------------- inciso
    # LA GUARDA NUEVA. La cobertura es EXACTA a proposito, para que la unica
    # cosa que pueda fallar sea el inciso: su primer campo es una PARAFRASIS
    # que no existe literal en el paso 1 del absorbido.
    plan = base("CASO POSITIVO inciso: el inciso NO es trozo verbatim")
    plan["actos"] = [{
        "orden": 1,
        "miembros": ["value_proposition_canvas", "customer_profile_value_map"],
        "superviviente": "value_proposition_canvas",
        "absorbidos": ["customer_profile_value_map"],
        "motivo": "MENTIRA DELIBERADA",
        "pasos": {"customer_profile_value_map": {
            "1": "INCISO:2|las tareas, dolores y alegrias del cliente|, especificando en el ",
            "2": "CUBIERTO:3", "3": "APPEND", "4": "APPEND"}},
        "condiciones": {"customer_profile_value_map": {"1": "CUBIERTO:1", "2": "APPEND"}},
        "nota_del_reparto": "MENTIRA DELIBERADA: el inciso es una parafrasis, no un trozo literal",
    }]
    io.open(TMP_C, "w", encoding="utf-8", newline="\n").write(
        json.dumps(plan, ensure_ascii=False, indent=1))
    rc, out = correr([FUNDIR, "--plan", TMP_C])
    ok = rc != 0 and "NO es trozo verbatim" in out
    print("  3. GUARDA DEL INCISO VERBATIM con una parafrasis en vez de un trozo literal")
    print("     exit=%d | aborta sin escribir: %s" % (rc, "SI" if "SE ABORTA SIN ESCRIBIR" in out else "NO"))
    for l in out.splitlines():
        if "verbatim" in l:
            print("     %s" % l.strip())
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MORDIO, ROJO"))
    fallos += 0 if ok else 1
    print()

    # ---------------------------------------------------------------- censo
    rc, out = correr([CENSO, "--esperadas", "9",
                      "--titulo", "CASO POSITIVO: censo contra una cuenta FALSA de 9"])
    linea = [l for l in out.splitlines() if "CUENTA ESPERADA" in l]
    ok = bool(linea) and "CALZA: NO" in linea[0]
    print("  4. GUARDA DE COLISIONES contra una cuenta esperada FALSA")
    print("     %s" % (linea[0].strip() if linea else "no imprimio la comparacion"))
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MORDIO, ROJO"))
    fallos += 0 if ok else 1
    print()

    for p in (TMP_A, TMP_B, TMP_C):
        if os.path.exists(p):
            os.remove(p)
    print("  planes de mentira borrados: %s"
          % ", ".join(os.path.basename(p) for p in (TMP_A, TMP_B, TMP_C)))
    print()
    print("RESULTADO: %s" % ("LAS CUATRO GUARDAS MUERDEN" if not fallos
                             else "%d GUARDA(S) NO MORDIERON" % fallos))
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
