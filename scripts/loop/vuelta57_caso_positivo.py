# -*- coding: utf-8 -*-
"""vuelta57_caso_positivo.py . EL CASO POSITIVO DE LA VUELTA 57: LAS GUARDAS QUE
ESTA VUELTA USA, PUESTAS A FALLAR A PROPOSITO.

SUCESOR DECLARADO de scripts/loop/vuelta56_caso_positivo.py, al que NO reemplaza
y que se re-corre PRIMERO como contraste.

LA REGLA DE TRABAJO SE MANTIENE, que es la del acta de la vuelta 54, pregunta 7:
EL CASO POSITIVO SE FABRICA SOBRE UN ACTO QUE LA PROPIA VUELTA NO VAYA A TOCAR,
para que no caduque. Aqui las mentiras de plan se fabrican sobre EL ACTO 37 DEL
TRAMO 3 (`seis_herramientas_comunicacion_celebracion` y
`seis_herramientas_comunicacion_fase_activate`), que es uno de los TRES
DECLARADOS del tramo 3 y que esta vuelta no toca: el tramo 4 no lo contiene, y
la guarda de solape del abridor lo comprueba.

  SE CAMBIA DE ACTO A PROPOSITO Y SE DICE POR QUE: la vuelta 55 uso el acto 4 y
  la 56 el acto 20, los dos con figura ASIMETRICA (uno tiene mas pasos que el
  otro). El acto 37 es SIMETRICO AL DIGITO: 5 pasos contra 5 y 1 condicion
  contra 1. Es una figura que el caso positivo no habia probado nunca, y es la
  peor para la guarda de cobertura, porque un plan que se equivoque de miembro
  cubre igual de bien los dos lados.

LO QUE ESTA VUELTA ANADE, y es su unica novedad: LA GUARDA 1 SE PONE A FALLAR
POR PRIMERA VEZ. Las vueltas 55 y 56 la declaraban VERDE en todos los actos,
pero nunca la habian puesto a mentir, y una guarda que solo se declara verde no
se sabe si muerde. La mentira es la que de verdad hace dano en esta operacion:
un plan que manda absorber un nodo QUE YA ESTA DEPRECADO. Se fabrica con un
deprecado real del catalogo (`6s_lugar_trabajo`, medido hoy entre los 468 que el
grafo declara), no con un id inventado, para que la linea roja sea la de "YA
esta deprecado" y no la de "no existe en el catalogo": son dos ramas distintas
de la misma guarda y solo una prueba lo que se quiere probar.

LAS OTRAS CINCO SE MANTIENEN PALABRA POR PALABRA (1B la puerta, cobertura por
OLVIDO, cobertura por SOBRANTE, INCISO verbatim y el censo contra una cuenta
falsa), para que el contraste con la vuelta 56 sea al digito.

EL PLAN FABRICADO SE ESCRIBE EN UN FICHERO TEMPORAL BAJO docs/loop/ Y SE BORRA
al terminar. El ejecutor se llama SIEMPRE en modo SIMULAR (sin --ejecutar), asi
que ni en el peor caso toca un nodo.

DE SOLO LECTURA sobre el dataset. Escribe y borra sus propios planes de mentira.

Uso: python scripts/loop/vuelta57_caso_positivo.py
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TMP_0 = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v57_vivos.json")
TMP_A = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v57_1b.json")
TMP_B = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v57_cobertura.json")
TMP_C = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v57_sobrante.json")
TMP_D = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_v57_inciso.json")
FUNDIR = os.path.join(RAIZ, "scripts", "loop", "vuelta49_fundir_tramo.py")
CENSO = os.path.join(RAIZ, "scripts", "loop", "vuelta51_censo_colisiones.py")

VIVE = "seis_herramientas_comunicacion_celebracion"
MUERE = "seis_herramientas_comunicacion_fase_activate"
DEPRECADO = "6s_lugar_trabajo"

# La cobertura EXACTA del absorbido: cinco pasos y una condicion, medidos del
# fichero del nodo y no tecleados de memoria.
COBERTURA_OK = {"1": "CUBIERTO:1", "2": "CUBIERTO:2", "3": "CUBIERTO:3",
                "4": "CUBIERTO:4", "5": "CUBIERTO:5"}
COND_OK = {"1": "CUBIERTO:1"}


def base(titulo):
    return {
        "operacion": "OP-U-01",
        "tramo": titulo,
        "fecha": "2026-08-20",
        "vuelta": 57,
        "estado": "PLAN DE MENTIRA, CASO POSITIVO, NO SE EJECUTA NUNCA",
        "nomina": "docs/loop/RECOMPUTO_V57_APERTURA.jsonl",
        "dossier": "ninguno",
        "vara": "caso positivo",
        "declarados_y_no_fundidos": [],
    }


def correr(argv):
    p = subprocess.run([sys.executable] + argv, capture_output=True, cwd=RAIZ)
    return p.returncode, p.stdout.decode("utf-8", "replace") + p.stderr.decode("utf-8", "replace")


def escribir(ruta, plan):
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(
        json.dumps(plan, ensure_ascii=False, indent=1))


def comprobar_forma():
    """LA FIGURA DEL ACTO SE MIDE, NO SE TECLEA: si el acto dejara de ser
    simetrico o cambiara de tamano, la cobertura exacta de aqui arriba mentiria
    y el caso positivo probaria otra cosa sin avisar."""
    d = {}
    for nid in (VIVE, MUERE):
        p = os.path.join(RAIZ, "dataset", "nodos", nid + ".json")
        j = json.load(io.open(p, encoding="utf-8"))
        d[nid] = (len(j.get("pasos_accionables") or []),
                  len(j.get("condiciones_activacion") or []),
                  bool(j.get("deprecado")))
    print("  LA FIGURA DEL ACTO, MEDIDA HOY:")
    for nid, (p, c, dep) in d.items():
        print("     %-46s pasos %d | condiciones %d | deprecado %s" % (nid, p, c, dep))
    simetrico = d[VIVE][:2] == d[MUERE][:2]
    print("     SIMETRICO AL DIGITO: %s" % ("SI" if simetrico else "NO"))
    calza = (d[MUERE][0] == len(COBERTURA_OK) and d[MUERE][1] == len(COND_OK))
    print("     la cobertura exacta escrita en este instrumento calza con el nodo: %s"
          % ("SI" if calza else "NO"))
    if not calza:
        print("     ROJO: el absorbido cambio de forma. El caso positivo NO se corre.")
    return calza


def veredicto(titulo, rc, out, ok, filtros, extra=None):
    rojas = [l.strip() for l in out.splitlines() if "[ROJO]" in l]
    print("  %s" % titulo)
    print("     exit=%d | aborta sin escribir: %s"
          % (rc, "SI" if "SE ABORTA SIN ESCRIBIR" in out else "NO"))
    for l in out.splitlines():
        if any(f in l for f in filtros):
            print("     %s" % l.strip())
    for l in rojas:
        print("     %s" % l)
    if extra:
        print("     %s" % extra(rojas))
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MORDIO, ROJO"))
    print()
    return 0 if ok else 1


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("CASO POSITIVO DE LA VUELTA 57: LAS GUARDAS PUESTAS A FALLAR")
    print("=" * 78)
    print()
    print("  LAS MENTIRAS DE PLAN VAN SOBRE EL ACTO 37 DEL TRAMO 3, que esta")
    print("  DECLARADO y que esta vuelta NO TOCA (regla del acta 54, pregunta 7).")
    print("  superviviente %s, absorbido %s" % (VIVE, MUERE))
    print()
    if not comprobar_forma():
        return 1
    print()
    fallos = 0

    # ------------------------------------------------- guarda 1, LA NUEVA
    # LA MENTIRA QUE DE VERDAD HACE DANO: absorber un nodo YA DEPRECADO. El
    # deprecado es REAL (medido entre los 468 del grafo), no inventado, para que
    # la linea roja sea la de "YA esta deprecado" y no la de "no existe".
    plan = base("CASO POSITIVO guarda 1: el absorbido YA esta deprecado")
    plan["actos"] = [{
        "orden": 1,
        "miembros": [VIVE, DEPRECADO],
        "superviviente": VIVE,
        "absorbidos": [DEPRECADO],
        "motivo": "MENTIRA DELIBERADA",
        "pasos": {}, "condiciones": {},
        "nota_del_reparto": "MENTIRA DELIBERADA: el absorbido esta deprecado desde antes",
    }]
    escribir(TMP_0, plan)
    rc, out = correr([FUNDIR, "--plan", TMP_0])
    ok = rc != 0 and "YA esta deprecado" in out
    fallos += veredicto(
        "0. GUARDA 1 con un absorbido YA DEPRECADO (NUEVA en esta vuelta)",
        rc, out, ok, ("guarda 1,",),
        lambda rojas: "la rama probada es la de YA DEPRECADO, no la de id inexistente: %s"
                      % ("SI" if "YA esta deprecado" in out else "NO"))

    # ---------------------------------------------------------------- 1B
    plan = base("CASO POSITIVO 1B: el absorbido ES una puerta")
    plan["actos"] = [{
        "orden": 1,
        "miembros": ["investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor",
                     "domina_lo_que_compras"],
        "superviviente": "investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor",
        "absorbidos": ["domina_lo_que_compras"],
        "motivo": "MENTIRA DELIBERADA",
        "pasos": {}, "condiciones": {},
        "nota_del_reparto": "MENTIRA DELIBERADA",
    }]
    escribir(TMP_A, plan)
    rc, out = correr([FUNDIR, "--plan", TMP_A])
    ok = rc != 0 and "guarda 1B" in out and "ROJO" in out
    fallos += veredicto("1. GUARDA 1B con un absorbido que es PUERTA",
                        rc, out, ok, ("guarda 1B",))

    # ------------------------------------------------------- cobertura, olvido
    plan = base("CASO POSITIVO cobertura por OLVIDO: el plan se salta un paso")
    marcas = dict(COBERTURA_OK)
    marcas.pop("3")
    plan["actos"] = [{
        "orden": 37,
        "miembros": [VIVE, MUERE],
        "superviviente": VIVE,
        "absorbidos": [MUERE],
        "motivo": "MENTIRA DELIBERADA",
        "pasos": {MUERE: marcas},
        "condiciones": {MUERE: dict(COND_OK)},
        "nota_del_reparto": "MENTIRA DELIBERADA: falta el paso 3",
    }]
    escribir(TMP_B, plan)
    rc, out = correr([FUNDIR, "--plan", TMP_B])
    ok = rc != 0 and "guarda 2" in out and "ROJO" in out
    fallos += veredicto(
        "2. GUARDA DE COBERTURA por OLVIDO de un paso (la direccion peligrosa)",
        rc, out, ok, ("guarda 2",),
        lambda rojas: "lineas rojas: %d (la 55 declaro DOS aqui, D6: una causa, dos sintomas)"
                      % len(rojas))

    # ---------------------------------------------------- cobertura, sobrante
    plan = base("CASO POSITIVO cobertura por SOBRANTE: un indice que no existe")
    marcas = dict(COBERTURA_OK)
    marcas["6"] = "CUBIERTO:1"
    plan["actos"] = [{
        "orden": 37,
        "miembros": [VIVE, MUERE],
        "superviviente": VIVE,
        "absorbidos": [MUERE],
        "motivo": "MENTIRA DELIBERADA",
        "pasos": {MUERE: marcas},
        "condiciones": {MUERE: dict(COND_OK)},
        "nota_del_reparto": "MENTIRA DELIBERADA: el paso 6 no existe en el absorbido",
    }]
    escribir(TMP_C, plan)
    rc, out = correr([FUNDIR, "--plan", TMP_C])
    rojas = [l.strip() for l in out.splitlines() if "[ROJO]" in l]
    ok = (rc != 0 and "guarda 2" in out and len(rojas) == 1
          and "sobran ['6']" in rojas[0])
    fallos += veredicto(
        "3. GUARDA DE COBERTURA por SOBRANTE, la que AISLA la guarda 2",
        rc, out, ok, ("guarda 2",),
        lambda r: "lineas rojas: %d | UNA SOLA CAUSA Y UN SOLO SINTOMA: %s"
                  % (len(r), "SI" if len(r) == 1 else "NO"))

    # ---------------------------------------------------------------- inciso
    plan = base("CASO POSITIVO inciso: el inciso NO es trozo verbatim")
    marcas = dict(COBERTURA_OK)
    marcas["2"] = ("INCISO:2|eligiendo los canales que mejor encajen con tu manera "
                   "de vender|, o sea ")
    plan["actos"] = [{
        "orden": 37,
        "miembros": [VIVE, MUERE],
        "superviviente": VIVE,
        "absorbidos": [MUERE],
        "motivo": "MENTIRA DELIBERADA",
        "pasos": {MUERE: marcas},
        "condiciones": {MUERE: dict(COND_OK)},
        "nota_del_reparto": "MENTIRA DELIBERADA: el inciso es parafrasis, no trozo literal",
    }]
    escribir(TMP_D, plan)
    rc, out = correr([FUNDIR, "--plan", TMP_D])
    ok = rc != 0 and "NO es trozo verbatim" in out
    fallos += veredicto(
        "4. GUARDA DEL INCISO VERBATIM con una parafrasis en vez de un trozo literal",
        rc, out, ok, ("verbatim",))

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

    for p in (TMP_0, TMP_A, TMP_B, TMP_C, TMP_D):
        if os.path.exists(p):
            os.remove(p)
    print("  planes de mentira borrados: %s"
          % ", ".join(os.path.basename(p) for p in (TMP_0, TMP_A, TMP_B, TMP_C, TMP_D)))
    print()
    print("RESULTADO: %s" % ("LAS SEIS GUARDAS MUERDEN" if not fallos
                             else "%d GUARDA(S) NO MORDIERON" % fallos))
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
