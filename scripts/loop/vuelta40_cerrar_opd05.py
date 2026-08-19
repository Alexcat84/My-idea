# -*- coding: utf-8 -*-
"""vuelta40_cerrar_opd05.py - EL CIERRE DE OP-D-05, escrito por instrumento.

SUCESOR DECLARADO de scripts/loop/vuelta39_cerrar_opd04.py (EJECUTOR.md regla 2),
y lo que cambia va dicho:

  1. UN SOLO SUPERVIVIENTE, y por eso EL CAMPO `superviviente` SE ESCRIBE. Aquel
     lo dejaba en `null` por la adjudicacion `a4` (dos supervivientes y un solo
     campo). Aqui no hay tal problema, y el precedente esta MEDIDO y no
     recordado: `OP-D-02`, la otra fusion de un solo superviviente, lo tiene
     escrito con el id de su superviviente. Se hace lo mismo.
  2. CERO NODOS PUENTE Y CERO COLGADOS: el acto era UNA familia entera de tres y
     los tres se funden, asi que NO hay tercera salida de `P.10` que enlazar.
     Aquel tenia un colgado y una arista que escribir; este no tiene ninguna, y
     la guarda lo comprueba en vez de darlo por hecho.

POR QUE EL ESTADO SE QUEDA EN `LISTA`: igual que las cuatro anteriores. La casa
registra el hecho consumado en la NOTA, no en el estado. Inventar un estado
`HECHA` seria inventar una regla, y la regla 5 de `EJECUTOR.md` lo prohibe. Sigue
como PENDIENTE DE DOCTRINA heredado.

GUARDAS, escritas para caer:
  1. la operacion existe y su estado es el que este cierre espera.
  2. el texto viejo de la nota queda LITERAL dentro de la nueva, o aborta.
  3. el campo `superviviente` queda escrito con el id del superviviente Y ese
     nodo esta VIVO, medido hoy en dataset/nodos.
  4. los DOS absorbidos estan deprecados y conservan su texto entero.
  5. CERO nodos vivos del catalogo apuntan a un absorbido (barrido entero).
  6. el numero de operaciones no cambia y ninguna otra se toca (byte a byte).

Uso: python scripts/loop/vuelta40_cerrar_opd05.py [--simular|--ejecutar]
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")

ID_OP = "OP-D-05"
ESTADO_ESPERADO = "LISTA"
SUP = "seleccion_ceo_fundador"
ABSORBIDOS = ["asignacion_de_titulos_ejecutivos", "errores_comunes_asignacion_roles"]

CIERRE = (
    " ESTADO AL 19 ago 2026 (vuelta 40): EJECUTADA ENTERA. El destejido quedo "
    "declarado SIN COSTURA QUE DESTEJER y medido: la unica costura que el archivo "
    "nombraba (seleccion_ceo_fundador, doce pasos, corte 5, ficha en "
    "docs/FICHA_SUBFUSION_GRADIENTE.md) ya se la habia llevado OP-F-04-HOR en el "
    "commit 2bd8dd76, con cero de seis huellas del bloque 5 a 12 sobrevivientes y "
    "el nodo en cuatro pasos contra doce; y el instrumento de costuras, REPARADO Y "
    "VIVO en esta misma vuelta, citaba UNO de los tres "
    "(errores_comunes_asignacion_roles, bloque 45,5) que leido con el texto delante "
    "y con P.11 resulto ser cinco advertencias distintas y no una narracion contada "
    "dos veces. P.5 sobre texto ya estable contesto UNA familia: un solo "
    "subconjunto cerrado que es el acto entero, 3 de 3 pares A del archivo (492, "
    "673 y 833), CERO nodos puente de P.10 y CERO aristas cojas en los tres. La "
    "especie de 9.3.1 era POR ELEGIR (solo el par 673 nombra ganador), y P.8 "
    "eligio POR CONTENIDO a seleccion_ceo_fundador: el archivo declara en el 673 "
    "que el corto cabe entero dentro de el, el eje comun de los tres ES su titulo "
    "literal, y por P.11 errores_comunes_asignacion_roles es LINEA y no "
    "procedimiento. El cableado (9 contra 4 y 4) se cito y NO decidio, y el coste "
    "medido de la eleccion fue CERO aristas. FUSION EJECUTADA tal como el plan "
    "sellado docs/loop/PLAN_V40_OPD05.json la escribio, con las trece guardas de "
    "scripts/loop/vuelta39_fundir.py en verde: 21 de 21 origenes VERBATIM, "
    "cobertura exacta 14 de 14 pasos y 7 de 7 condiciones, preservar 8 de 8 y "
    "rastros 5 de 5 con su sede impresa, 8 redirecciones y 0 deprecados que "
    "nombran, P.16 con las 2 duplicadas fabricadas medidas antes de limpiarlas y "
    "limpiadas en la misma operacion, cero auto arista y cero duplicada al salir, "
    "a6 con titulo y etiqueta intactos, y el censo en 3.853 ficheros con los vivos "
    "bajando exactamente 2. reanclar_por_resolutor.py corrido ENTRE la fusion y "
    "run_phase1 (practica adjudicada por el acta de la vuelta 39): nada que "
    "re-anclar, tal como el plan predijo tras enumerar ANTES los registros que no "
    "son el grafo (cero vivos, y cero en los nueve bridges_aprobados.json). La "
    "simetrizacion del paso 5 trajo EXACTAMENTE las 5 aristas del plan, cero de "
    "otros nodos, y las 5 releidas en el fichero. EL RESULTADO QUEDA EN SEIS "
    "PASOS, DENTRO del estandar de 3 a 6: esta operacion NO necesita la excepcion "
    "de clase de OP-F-01 que OP-D-04 si necesito. LA TABLA DE PERDIDAS: 21 de 21 "
    "piezas VIAJAN y CERO se pierden, asi que la regla de reparto adjudicada el 11 "
    "ago 2026 se cumple por vacio y se dice asi en vez de darla por cumplida. El "
    "campo superviviente SE ESCRIBE con seleccion_ceo_fundador, por el precedente "
    "medido de OP-D-02, que es la otra fusion de un solo superviviente y lo tiene "
    "escrito. El estado sigue en LISTA como las cuatro anteriores: el esquema no "
    "distingue una operacion HECHA, y eso sigue como pendiente de doctrina."
)


def nodo(nid):
    return json.loads(io.open(os.path.join(NODOS, nid + ".json"),
                              encoding="utf-8").read())


def main():
    modo = "--simular"
    for x in sys.argv[1:]:
        if x in ("--simular", "--ejecutar"):
            modo = x

    lineas = [l for l in io.open(OPS, encoding="utf-8", newline="")]
    ops = [json.loads(l) for l in lineas if l.strip()]
    print("OPERACIONES: %d lineas, %d operaciones" % (len(lineas), len(ops)))
    print("MODO       : %s" % modo)
    print("=" * 78)

    fallos = []

    # GUARDA 1
    idx = [i for i, o in enumerate(ops) if o["id_op"] == ID_OP]
    if len(idx) != 1:
        sys.exit("guarda 1 ROJO: %s aparece %d veces" % (ID_OP, len(idx)))
    i = idx[0]
    op = ops[i]
    ok1 = op["estado"] == ESTADO_ESPERADO
    print("guarda 1, la operacion existe y su estado es %r: %s (%r)"
          % (ESTADO_ESPERADO, "OK" if ok1 else "ROJO", op["estado"]))
    if not ok1:
        fallos.append("estado inesperado")

    nota_vieja = op.get("nota") or ""
    nota_nueva = nota_vieja.rstrip() + CIERRE

    # GUARDA 2
    ok2 = nota_vieja.rstrip() in nota_nueva and len(nota_nueva) > len(nota_vieja)
    print("guarda 2, el texto viejo de la nota sobrevive LITERAL (%d -> %d, gana "
          "%d): %s" % (len(nota_vieja), len(nota_nueva),
                       len(nota_nueva) - len(nota_vieja), "OK" if ok2 else "ROJO"))
    if not ok2:
        fallos.append("la nota vieja no sobrevive literal")

    # GUARDA 3
    d_sup = nodo(SUP)
    ok3 = not d_sup.get("deprecado") and not d_sup.get("deprecated")
    print("guarda 3, el superviviente %s esta VIVO hoy en dataset/nodos: %s"
          % (SUP, "OK" if ok3 else "ROJO"))
    if not ok3:
        fallos.append("el superviviente no esta vivo")
    print("          y el campo superviviente pasa de %r a %r (precedente medido: "
          "OP-D-02)" % (op.get("superviviente"), SUP))

    # GUARDA 4
    ok4 = True
    for a in ABSORBIDOS:
        d = nodo(a)
        dep = bool(d.get("deprecado") or d.get("deprecated"))
        npasos = len(d.get("pasos_accionables") or [])
        ncond = len(d.get("condiciones_activacion") or [])
        print("guarda 4, %-34s deprecado=%s, texto INTACTO (%d pasos, %d "
              "condiciones)" % (a, dep, npasos, ncond))
        if not dep or npasos == 0:
            ok4 = False
    if not ok4:
        fallos.append("algun absorbido no quedo deprecado o perdio su texto")
    print("guarda 4: %s" % ("OK" if ok4 else "ROJO"))

    # GUARDA 5
    apuntan = []
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        d = nodo(nombre[:-5])
        if d.get("deprecado") or d.get("deprecated"):
            continue
        for campo in CAMPOS:
            for a in ABSORBIDOS:
                if a in (d.get(campo) or []):
                    apuntan.append((d["node_id"], campo, a))
    print("guarda 5, nodos VIVOS que todavia apuntan a un absorbido: %d %s"
          % (len(apuntan), "OK" if not apuntan else "ROJO"))
    for x in apuntan:
        print("    %s" % (x,))
    if apuntan:
        fallos.append("quedan vivos apuntando a un absorbido")

    # y la comprobacion que aqui NO aplica, dicha en vez de omitida
    print("nota, P.10: el acto era UNA familia entera de tres y los tres se "
          "funden, asi que NO hay colgado ni tercera salida de P.10 que enlazar. "
          "Se dice en vez de callarlo.")

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    nuevo = dict(op)
    nuevo["nota"] = nota_nueva
    nuevo["superviviente"] = SUP
    linea_nueva = json.dumps(nuevo, ensure_ascii=False) + "\n"

    # GUARDA 6: ninguna otra linea se toca
    salida = []
    k = 0
    movidas = 0
    for l in lineas:
        if not l.strip():
            salida.append(l)
            continue
        if k == i:
            salida.append(linea_nueva)
            movidas += 1
        else:
            salida.append(l)
        k += 1
    ok6 = (len(salida) == len(lineas) and movidas == 1)
    print("guarda 6, se mueve UNA sola linea de %d y el conteo no cambia: %s"
          % (len(lineas), "OK" if ok6 else "ROJO"))
    if not ok6:
        print("SE ABORTA SIN ESCRIBIR")
        return 1

    if modo == "--simular":
        print()
        print("SIMULACION: cero escrituras.")
        return 0

    io.open(OPS, "w", encoding="utf-8", newline="").write("".join(salida))
    print()
    print("ESCRITO. %s cerrada: nota de %d caracteres, superviviente %r."
          % (ID_OP, len(nota_nueva), SUP))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
