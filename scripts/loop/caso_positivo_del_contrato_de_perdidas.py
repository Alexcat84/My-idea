# -*- coding: utf-8 -*-
"""caso_positivo_del_contrato_de_perdidas.py . LA GUARDA QUE ESTE TRAMO ESTRENA,
PUESTA A FALLAR A PROPOSITO.

NOMBRE ESTABLE, sin numero de vuelta: la cadena de clones vuelta55, vuelta56,
vuelta57 del caso positivo no se continua aqui. Lo que este instrumento prueba
no es una vuelta: es EL CONTRATO CAMPO PROPIO v1 y la guarda que lo hace cumplir
AL SELLAR, que es lo que scripts/loop/generar_plan_del_lote.py enumera como
CAMBIO 3 en su docstring.

POR QUE HACE FALTA, y no lo cubre el caso positivo heredado: aquel prueba las
seis guardas del EJECUTOR de fusiones (miembros vivos, 1B, cobertura por olvido,
cobertura por sobrante, inciso verbatim y el censo contra una cuenta falsa), y
ninguna de las seis sabe nada de perdidas. La guarda nueva vive en el GENERADOR
y muerde ANTES, cuando el plan se sella. Una guarda que solo se declara verde no
se sabe si muerde (P.14).

LA REGLA DE TRABAJO SE MANTIENE (acta 54, pregunta 7): las mentiras se fabrican
sobre UN ACTO QUE LA VUELTA NO TOCA, para que el caso positivo no caduque. Aqui
es EL ACTO 37 DEL TRAMO 3 (seis_herramientas_comunicacion_celebracion y
seis_herramientas_comunicacion_fase_activate), uno de los tres DECLARADOS del
tramo 3, y que NO ESTA en el tramo 6: comprobado contra la nomina fijada, no
supuesto.

LAS CUATRO PRUEBAS, y la tercera es la que impide que este instrumento sea un
sello de goma que solo sabe decir rojo:

  1. ESPECIE DESCONOCIDA al sellar  -> ROJO y el plan NO se escribe.
  2. CLAVE QUE FALTA al sellar      -> ROJO y el plan NO se escribe.
  3. LA MISMA PERDIDA BIEN FORMADA  -> VERDE, se sella y el campo sale entero.
  4. EL CAMPO AUSENTE, visto por el TALLADOR sobre un plan que declara el
     contrato -> ROJO, que es la mitad del contrato que distingue LISTA VACIA
     (declaracion de cero perdidas) de CAMPO AUSENTE (el plan no lo dice).

EL MODULO DE CONTENIDO DE MENTIRA Y LOS PLANES DE MENTIRA SE ESCRIBEN EN
FICHEROS TEMPORALES Y SE BORRAN AL TERMINAR. El generador se llama SIEMPRE con
--simular en las dos primeras pruebas, y en la tercera escribe en un fichero
temporal propio: ni en el peor caso toca un nodo ni pisa un plan sellado.

DE SOLO LECTURA sobre el dataset.

Uso: python scripts/loop/caso_positivo_del_contrato_de_perdidas.py
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
AQUI = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(AQUI, "generar_plan_del_lote.py")
TALLADOR = os.path.join(AQUI, "tallar_perdidas_del_plan.py")
MOD = "_caso_positivo_contrato_perdidas"
MOD_RUTA = os.path.join(AQUI, MOD + ".py")
TMP_PLAN = os.path.join(LOOP, "_caso_positivo_contrato_sellado.json")
TMP_SIN_CAMPO = os.path.join(LOOP, "_caso_positivo_contrato_sin_campo.json")
TRAMO = os.path.join(LOOP, "TRAMO6_V61.jsonl")
TMP_NOMINA = os.path.join(LOOP, "_caso_positivo_contrato_nomina.jsonl")

VIVE = "seis_herramientas_comunicacion_celebracion"
MUERE = "seis_herramientas_comunicacion_fase_activate"


def correr(argv):
    p = subprocess.run([sys.executable] + argv, capture_output=True, cwd=RAIZ)
    return p.returncode, p.stdout.decode("utf-8", "replace") + p.stderr.decode("utf-8", "replace")


def figura():
    """LA FIGURA DEL ACTO SE MIDE, NO SE TECLEA: si el acto cambiara de tamano,
    la cobertura de aqui abajo mentiria y esto probaria otra cosa sin avisar."""
    d = {}
    for nid in (VIVE, MUERE):
        j = json.load(io.open(os.path.join(RAIZ, "dataset", "nodos", nid + ".json"),
                              encoding="utf-8"))
        d[nid] = (len(j.get("pasos_accionables") or []),
                  len(j.get("condiciones_activacion") or []),
                  bool(j.get("deprecado")))
    print("  LA FIGURA DEL ACTO, MEDIDA HOY:")
    for nid, (p, c, dep) in d.items():
        print("     %-46s pasos %d | condiciones %d | deprecado %s" % (nid, p, c, dep))
    return d


def fuera_del_tramo():
    filas = [json.loads(l) for l in io.open(TRAMO, encoding="utf-8") if l.strip()]
    miembros = set()
    for r in filas:
        miembros |= set(r["miembros"])
    dentro = [x for x in (VIVE, MUERE) if x in miembros]
    print("     la nomina fijada del tramo 6 tiene %d ids; de los dos de arriba, dentro: %s"
          % (len(miembros), dentro or "NINGUNO"))
    return not dentro


def escribir_nomina():
    """LA NOMINA DE MENTIRA, DE UNA SOLA FILA, sobre el acto 37 del tramo 3.
    NO se apunta a la nomina del tramo 6, y se dice por que, que es la leccion de
    la PRIMERA corrida de este mismo instrumento: sus once primeros actos ACABAN
    DE FUNDIRSE en esta vuelta, asi que la guarda de miembros vivos se disparaba
    ANTES que la de perdidas y el rojo no era el que se buscaba. El acto 37 del
    tramo 3 esta DECLARADO, con sus dos miembros vivos, y esta vuelta no lo toca."""
    fila = {"orden_tramo3": 37, "miembros": sorted([VIVE, MUERE]), "estado": "CERRADO"}
    io.open(TMP_NOMINA, "w", encoding="utf-8", newline=chr(10)).write(
        json.dumps(fila, ensure_ascii=False) + chr(10))


def escribir_modulo(perdidas_literal):
    """El modulo de contenido de mentira, sobre el unico acto de la nomina de
    mentira. Lo que se prueba es la guarda de PERDIDAS, y el generador tiene que
    llegar hasta ella con todo lo anterior en verde."""
    sup, ab = VIVE, MUERE
    j = json.load(io.open(os.path.join(RAIZ, "dataset", "nodos", ab + ".json"),
                          encoding="utf-8"))
    pasos = {str(i): ["CUBIERTO", 1] for i in range(1, len(j.get("pasos_accionables") or []) + 1)}
    cond = {str(i): ["CUBIERTO", 1] for i in range(1, len(j.get("condiciones_activacion") or []) + 1)}
    cuerpo = (
        "# -*- coding: utf-8 -*-\n"
        '"""CONTENIDO DE MENTIRA DEL CASO POSITIVO. Se escribe y se borra."""\n'
        "LOTE_Z = {\n"
        '    "titulo": "PLAN DE MENTIRA, CASO POSITIVO DEL CONTRATO, NO SE EJECUTA NUNCA",\n'
        '    "declarados": [],\n'
        '    "actos": [\n'
        "        {\n"
        '            "orden": 37,\n'
        '            "superviviente": %r,\n'
        '            "motivo": "caso positivo",\n'
        '            "pasos": %r,\n'
        '            "condiciones": %r,\n'
        '            "nota": "caso positivo",\n'
        '            "perdidas": %s,\n'
        "        },\n"
        "    ],\n"
        "}\n" % (sup, pasos, cond, perdidas_literal))
    io.open(MOD_RUTA, "w", encoding="utf-8", newline="\n").write(cuerpo)
    return sup, ab


def generar(destino_prefijo, simular):
    # CORRECCION DECLARADA (2026-08-20, vuelta 66, carril del banco 9.10; el texto
    # viejo va aqui verbatim y no se tacha). LA LINEA VIEJA ERA:
    #   argv = [GEN, "--lote", "Z", "--vuelta", "62", "--tramo",
    #           os.path.relpath(TMP_NOMINA, RAIZ).replace(os.sep, "/"),
    #           "--contenido", MOD, "--prefijo", destino_prefijo]
    # o sea SIN --operacion. Desde la vuelta 63 ese argumento es REQUERIDO en
    # generar_plan_del_lote.py, asi que las tres llamadas de este caso positivo
    # morian en argparse con exit 2 y este fichero LEIA ESE 2 COMO SI LA GUARDA NO
    # MORDIERA: daba "ROJO: 4 de 4 fallan" contra unas guardas que estan sanas.
    # MEDIDO EN LA VUELTA 66 al re-correrlo (docs/loop/_v66/, averia declarada en
    # el reporte): un caso positivo que acusa en falso es tan malo como uno que
    # calla, porque la proxima vez que acuse nadie le va a creer. La operacion que
    # se le pasa es OP-U-01, que es la del tramo del que sale su fixture.
    argv = [GEN, "--lote", "Z", "--vuelta", "62", "--operacion", "OP-U-01", "--tramo",
            os.path.relpath(TMP_NOMINA, RAIZ).replace(os.sep, "/"),
            "--contenido", MOD, "--prefijo", destino_prefijo]
    if simular:
        argv.append("--simular")
    return correr(argv)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("CASO POSITIVO DEL CONTRATO CAMPO PROPIO v1: LA GUARDA QUE ESTE TRAMO")
    print("ESTRENA, PUESTA A FALLAR")
    print("=" * 78)
    print()
    print("  LAS MENTIRAS VAN SOBRE UN ACTO QUE ESTA VUELTA NO TOCA (acta 54, pregunta 7):")
    print("  el acto 37 del tramo 3, DECLARADO, superviviente %s, absorbido %s" % (VIVE, MUERE))
    figura()
    limpio = fuera_del_tramo()
    print("     NINGUNO DE LOS DOS ENTRA EN EL TRAMO 6: %s" % ("SI" if limpio else "NO"))
    print()

    escribir_nomina()
    veredictos = []
    buena = ('[{"especie": "DE PARAMETRO DE PASO", "que": "una perdida de mentira", '
             '"donde": "paso 1 del absorbido", "enrutada_a": "la fase 04"}]')

    # 1. ESPECIE DESCONOCIDA AL SELLAR
    escribir_modulo('[{"especie": "DE COLOR", "que": "x", "donde": "y", "enrutada_a": "z"}]')
    code, out = generar("_caso_positivo_contrato_", True)
    ok = code == 1 and "especie de perdida desconocida" in out
    print("  1. ESPECIE DESCONOCIDA al SELLAR (guarda NUEVA de este tramo)")
    print("     exit=%d | aborta sin escribir: %s" % (code, "SI" if code == 1 else "NO"))
    for l in out.split("\n"):
        if "especie de perdida desconocida" in l or "ROJO," in l:
            print("     %s" % l.strip())
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MUERDE"))
    veredictos.append(ok)
    print()

    # 2. CLAVE QUE FALTA AL SELLAR
    escribir_modulo('[{"especie": "DE NOMBRE", "que": "x", "donde": "y"}]')
    code, out = generar("_caso_positivo_contrato_", True)
    ok = code == 1 and "le faltan las claves" in out
    print("  2. CLAVE QUE FALTA al SELLAR (falta enrutada_a)")
    print("     exit=%d | aborta sin escribir: %s" % (code, "SI" if code == 1 else "NO"))
    for l in out.split("\n"):
        if "le faltan las claves" in l or "ROJO," in l:
            print("     %s" % l.strip())
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MUERDE"))
    veredictos.append(ok)
    print()

    # 3. LA MISMA PERDIDA BIEN FORMADA: TIENE QUE PASAR
    escribir_modulo(buena)
    code, out = generar("_caso_positivo_contrato_sellado_ZZZ", False)
    sellado = os.path.join(LOOP, "_caso_positivo_contrato_sellado_ZZZZ.json")
    ok = code == 0 and "perdidas selladas, en total         : 1" in out
    print("  3. LA MISMA PERDIDA, BIEN FORMADA: LA GUARDA TIENE QUE DEJARLA PASAR")
    print("     exit=%d | sella: %s" % (code, "SI" if code == 0 else "NO"))
    for l in out.split("\n"):
        if "perdidas selladas" in l or "campo perdidas presente" in l:
            print("     %s" % l.strip())
    print("     VEREDICTO: %s" % ("LA GUARDA NO ES UN SELLO DE GOMA" if ok
                                  else "LA GUARDA TUMBA UN PLAN BUENO, ROJO"))
    veredictos.append(ok)
    print()

    # 4. EL CAMPO AUSENTE, VISTO POR EL TALLADOR
    plan = json.load(io.open(sellado, encoding="utf-8")) if os.path.exists(sellado) else None
    if plan is None:
        print("  4. NO SE PUDO LEER EL PLAN SELLADO DE LA PRUEBA 3: %s" % sellado)
        veredictos.append(False)
    else:
        del plan["actos"][0]["perdidas"]
        io.open(TMP_SIN_CAMPO, "w", encoding="utf-8", newline="\n").write(
            json.dumps(plan, ensure_ascii=False, indent=1))
        code, out = correr([TALLADOR, "--plan",
                            os.path.relpath(TMP_SIN_CAMPO, RAIZ).replace(os.sep, "/")])
        ok = code == 1 and "NO trae el campo perdidas" in out
        print("  4. CAMPO AUSENTE con el contrato declarado, visto por el TALLADOR")
        print("     exit=%d | no emite tabla: %s" % (code, "SI" if "LA TABLA" not in out else "NO"))
        for l in out.split("\n"):
            if "NO trae el campo perdidas" in l:
                print("     %s" % l.strip())
        print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MUERDE"))
        veredictos.append(ok)
    print()

    borrados = []
    for r in (MOD_RUTA, TMP_PLAN, TMP_SIN_CAMPO, TMP_NOMINA, sellado):
        if r and os.path.exists(r):
            os.remove(r)
            borrados.append(os.path.basename(r))
    pyc = os.path.join(AQUI, "__pycache__")
    if os.path.isdir(pyc):
        for f in os.listdir(pyc):
            if f.startswith(MOD):
                os.remove(os.path.join(pyc, f))
                borrados.append(f)
    print("  ficheros de mentira borrados: %s" % ", ".join(borrados))
    print()
    print("RESULTADO: %s" % ("LAS CUATRO PRUEBAS EN VERDE, LA GUARDA NUEVA MUERDE Y NO SOBREMUERDE"
                             if all(veredictos) else
                             "ROJO: %d de 4 fallan" % len([x for x in veredictos if not x])))
    return 0 if all(veredictos) else 1


if __name__ == "__main__":
    raise SystemExit(main())
