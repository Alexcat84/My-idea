# -*- coding: utf-8 -*-
"""vuelta56_caso_positivo.py . EL CASO POSITIVO DE LA VUELTA 56: LAS GUARDAS
QUE ESTA VUELTA USA, PUESTAS A FALLAR A PROPOSITO.

SUCESOR DECLARADO de scripts/loop/vuelta55_caso_positivo.py, al que NO
reemplaza y que se re-corre PRIMERO como contraste (encargo 2.3).

LA REGLA DE TRABAJO SE MANTIENE, que es la del acta de la vuelta 54, pregunta
7: EL CASO POSITIVO SE FABRICA SOBRE UN ACTO QUE LA PROPIA VUELTA NO VAYA A
TOCAR, para que no caduque. Aqui las mentiras de plan se fabrican sobre EL
ACTO 20 DEL TRAMO 2 (fases_de_retencion_de_clientes y
ocho_fases_experiencia_cliente), que es uno de los CINCO DECLARADOS del tramo
2 y que el encargo de esta vuelta manda NO TOCAR (TAREA 2.5).

  SE CAMBIA DE ACTO A PROPOSITO Y SE DICE POR QUE: la vuelta 55 uso el acto 4,
  y repetir el mismo acto haria que el caso positivo probara siempre la misma
  forma de nodo. El acto 20 tiene la figura CONTRARIA a la del 4 en la unica
  cosa que la guarda de cobertura mide: aqui el que MUERE tiene MAS pasos que
  el que sobrevive (4 contra 3) y MENOS condiciones (1 contra 2).

LO QUE ESTA VUELTA ANADE, y es la respuesta al D6 de la vuelta 55: aquel
reporte declaro que su mentira de cobertura fallaba por DOS lineas rojas (la
de la guarda 2 y una "marca desconocida"), porque quitar la marca de un paso
produce las dos a la vez. Es una sola causa con dos sintomas, y estaba bien
declarada, pero una mentira que enciende dos luces no aisla la guarda que dice
probar. AQUI LA COBERTURA SE PONE A FALLAR POR SUS DOS LADOS:

  MENTIRA 2, POR OLVIDO (la peligrosa, la que pierde una pieza): el plan se
  salta el paso 3 del absorbido. Enciende las DOS lineas, como en la 55, y se
  deja tal cual para que el contraste con la vuelta anterior sea al digito.

  MENTIRA 3, POR SOBRANTE (la que AISLA la guarda 2): el plan cubre los cuatro
  pasos reales y ademas declara un paso 5 que el absorbido NO TIENE. El bucle
  del reparto solo recorre los pasos REALES, asi que ninguna marca queda
  vacia y la UNICA linea roja posible es la de la guarda 2, con "sobran
  ['5']". Una sola causa, UN solo sintoma: la guarda 2 queda probada sola.

EL PLAN FABRICADO SE ESCRIBE EN UN FICHERO TEMPORAL BAJO docs/loop/ Y SE BORRA
al terminar. El ejecutor se llama SIEMPRE en modo SIMULAR (sin --ejecutar), asi
que ni en el peor caso toca un nodo.

DE SOLO LECTURA sobre el dataset. Escribe y borra sus propios planes de mentira.

Uso: python scripts/loop/vuelta56_caso_positivo.py
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TMP_A = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v56_1b.json")
TMP_B = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v56_cobertura.json")
TMP_C = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v56_sobrante.json")
TMP_D = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v56_inciso.json")
FUNDIR = os.path.join(RAIZ, "scripts", "loop", "vuelta49_fundir_tramo.py")
CENSO = os.path.join(RAIZ, "scripts", "loop", "vuelta51_censo_colisiones.py")

VIVE = "fases_de_retencion_de_clientes"
MUERE = "ocho_fases_experiencia_cliente"


def base(titulo):
    return {
        "operacion": "OP-U-01",
        "tramo": titulo,
        "fecha": "2026-08-20",
        "vuelta": 56,
        "estado": "PLAN DE MENTIRA, CASO POSITIVO, NO SE EJECUTA NUNCA",
        "nomina": "docs/loop/RECOMPUTO_V56_APERTURA.jsonl",
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
    print("CASO POSITIVO DE LA VUELTA 56: LAS GUARDAS PUESTAS A FALLAR")
    print("=" * 78)
    print()
    print("  LAS MENTIRAS DE PLAN VAN SOBRE EL ACTO 20 DEL TRAMO 2, que esta")
    print("  DECLARADO y que esta vuelta NO TOCA (regla del acta 54, pregunta 7).")
    print("  superviviente %s, absorbido %s" % (VIVE, MUERE))
    print()
    fallos = 0

    # ---------------------------------------------------------------- 1B
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
    print("     exit=%d | aborta sin escribir: %s"
          % (rc, "SI" if "SE ABORTA SIN ESCRIBIR" in out else "NO"))
    for l in out.splitlines():
        if "guarda 1B" in l or ("[ROJO]" in l and "1B" in l):
            print("     %s" % l.strip())
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MORDIO, ROJO"))
    fallos += 0 if ok else 1
    print()

    # ------------------------------------------------------- cobertura, olvido
    # El absorbido tiene CUATRO pasos y UNA condicion. El plan SE OLVIDA DEL
    # PASO 3 y de nada mas: la guarda 1 pasa (los dos vivos) y la 1B pasa
    # (ninguno es puerta).
    plan = base("CASO POSITIVO cobertura por OLVIDO: el plan se salta un paso")
    plan["actos"] = [{
        "orden": 20,
        "miembros": [VIVE, MUERE],
        "superviviente": VIVE,
        "absorbidos": [MUERE],
        "motivo": "MENTIRA DELIBERADA",
        "pasos": {MUERE: {"1": "CUBIERTO:1", "2": "CUBIERTO:2", "4": "CUBIERTO:2"}},
        "condiciones": {MUERE: {"1": "CUBIERTO:1"}},
        "nota_del_reparto": "MENTIRA DELIBERADA: falta el paso 3",
    }]
    io.open(TMP_B, "w", encoding="utf-8", newline="\n").write(
        json.dumps(plan, ensure_ascii=False, indent=1))
    rc, out = correr([FUNDIR, "--plan", TMP_B])
    rojas = [l.strip() for l in out.splitlines() if "[ROJO]" in l]
    ok = rc != 0 and "guarda 2" in out and "ROJO" in out
    print("  2. GUARDA DE COBERTURA por OLVIDO de un paso (la direccion peligrosa)")
    print("     exit=%d | aborta sin escribir: %s"
          % (rc, "SI" if "SE ABORTA SIN ESCRIBIR" in out else "NO"))
    for l in out.splitlines():
        if "guarda 2" in l:
            print("     %s" % l.strip())
    for l in rojas:
        print("     %s" % l)
    print("     lineas rojas: %d (la 55 declaro DOS aqui, D6: una causa, dos sintomas)"
          % len(rojas))
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MORDIO, ROJO"))
    fallos += 0 if ok else 1
    print()

    # ---------------------------------------------------- cobertura, sobrante
    # LA MENTIRA QUE AISLA LA GUARDA 2 (respuesta al D6 de la vuelta 55): la
    # cobertura de los cuatro pasos reales es EXACTA, y el plan declara ademas
    # un paso 5 que el absorbido no tiene. Ninguna marca queda vacia, asi que
    # la unica linea roja posible es la de la guarda 2.
    plan = base("CASO POSITIVO cobertura por SOBRANTE: un indice que no existe")
    plan["actos"] = [{
        "orden": 20,
        "miembros": [VIVE, MUERE],
        "superviviente": VIVE,
        "absorbidos": [MUERE],
        "motivo": "MENTIRA DELIBERADA",
        "pasos": {MUERE: {"1": "CUBIERTO:1", "2": "CUBIERTO:2",
                          "3": "CUBIERTO:3", "4": "CUBIERTO:2",
                          "5": "CUBIERTO:1"}},
        "condiciones": {MUERE: {"1": "CUBIERTO:1"}},
        "nota_del_reparto": "MENTIRA DELIBERADA: el paso 5 no existe en el absorbido",
    }]
    io.open(TMP_C, "w", encoding="utf-8", newline="\n").write(
        json.dumps(plan, ensure_ascii=False, indent=1))
    rc, out = correr([FUNDIR, "--plan", TMP_C])
    rojas = [l.strip() for l in out.splitlines() if "[ROJO]" in l]
    ok = (rc != 0 and "guarda 2" in out and len(rojas) == 1
          and "sobran ['5']" in rojas[0])
    print("  3. GUARDA DE COBERTURA por SOBRANTE, la que AISLA la guarda 2")
    print("     exit=%d | aborta sin escribir: %s"
          % (rc, "SI" if "SE ABORTA SIN ESCRIBIR" in out else "NO"))
    for l in out.splitlines():
        if "guarda 2" in l:
            print("     %s" % l.strip())
    for l in rojas:
        print("     %s" % l)
    print("     lineas rojas: %d | UNA SOLA CAUSA Y UN SOLO SINTOMA: %s"
          % (len(rojas), "SI" if len(rojas) == 1 else "NO"))
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MORDIO, ROJO"))
    fallos += 0 if ok else 1
    print()

    # ---------------------------------------------------------------- inciso
    # La cobertura es EXACTA a proposito, para que la unica cosa que pueda
    # fallar sea el inciso: su primer campo es una PARAFRASIS que no existe
    # literal en el paso 2 del absorbido.
    plan = base("CASO POSITIVO inciso: el inciso NO es trozo verbatim")
    plan["actos"] = [{
        "orden": 20,
        "miembros": [VIVE, MUERE],
        "superviviente": VIVE,
        "absorbidos": [MUERE],
        "motivo": "MENTIRA DELIBERADA",
        "pasos": {MUERE: {
            "1": "CUBIERTO:1",
            "2": "INCISO:2|la experiencia emocional deseada para todos los segmentos|, o sea ",
            "3": "CUBIERTO:3", "4": "CUBIERTO:2"}},
        "condiciones": {MUERE: {"1": "CUBIERTO:1"}},
        "nota_del_reparto": "MENTIRA DELIBERADA: el inciso es parafrasis, no trozo literal",
    }]
    io.open(TMP_D, "w", encoding="utf-8", newline="\n").write(
        json.dumps(plan, ensure_ascii=False, indent=1))
    rc, out = correr([FUNDIR, "--plan", TMP_D])
    ok = rc != 0 and "NO es trozo verbatim" in out
    print("  4. GUARDA DEL INCISO VERBATIM con una parafrasis en vez de un trozo literal")
    print("     exit=%d | aborta sin escribir: %s"
          % (rc, "SI" if "SE ABORTA SIN ESCRIBIR" in out else "NO"))
    for l in out.splitlines():
        if "verbatim" in l:
            print("     %s" % l.strip())
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MORDIO, ROJO"))
    fallos += 0 if ok else 1
    print()

    # ---------------------------------------------------------------- censo
    rc, out = correr([CENSO, "--esperadas", "7",
                      "--titulo", "CASO POSITIVO: censo contra una cuenta FALSA de 7"])
    linea = [l for l in out.splitlines() if "CUENTA ESPERADA" in l]
    ok = bool(linea) and "CALZA: NO" in linea[0]
    print("  5. GUARDA DE COLISIONES contra una cuenta esperada FALSA")
    print("     %s" % (linea[0].strip() if linea else "no imprimio la comparacion"))
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MORDIO, ROJO"))
    fallos += 0 if ok else 1
    print()

    for p in (TMP_A, TMP_B, TMP_C, TMP_D):
        if os.path.exists(p):
            os.remove(p)
    print("  planes de mentira borrados: %s"
          % ", ".join(os.path.basename(p) for p in (TMP_A, TMP_B, TMP_C, TMP_D)))
    print()
    print("RESULTADO: %s" % ("LAS CINCO GUARDAS MUERDEN" if not fallos
                             else "%d GUARDA(S) NO MORDIERON" % fallos))
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
