# -*- coding: utf-8 -*-
r"""vuelta162_tarea2b_tabla_excepciones.py . TAREA 2.b de la vuelta 162.

Aplica sobre `scripts/loop/tallar_estado_de_fase.py` la ADJUDICACION 6.4 DEL
ACTA 161: LA VARA DE LOS DESTEJIDOS ES MAS ANCHA QUE LA FICHA DE `OP-D-02`, y el
remedio es de la vara, con TABLA DE EXCEPCIONES QUE CITA SU ADJUDICACION.

Parche de una sola pasada, con anclas literales: si un ancla no aparece
exactamente una vez, PARA sin escribir.

USO:  python scripts/loop/vuelta162_tarea2b_tabla_excepciones.py
"""
import io

RUTA = "scripts/loop/tallar_estado_de_fase.py"

ANCLA_TABLA = "def destino_de_fusion(op, nodos, fallos, resolver=None):\n"

BLOQUE_TABLA = r'''# --- ADJUDICACION 6.4 DEL ACTA 161 (3 sep 2026): LA VARA ERA MAS ANCHA QUE LA
# FICHA, Y EL REMEDIO ES DE LA VARA -----------------------------------------
#
# REGISTRO POR ADICION. Nada de lo escrito arriba se borra.
#
# EL HECHO, MEDIDO. `destino_de_fusion` toma como ABSORBIDOS **todo el campo
# `nodos` menos el superviviente**. En `OP-D-02` el campo `nodos` trae CUATRO y
# el superviviente uno, asi que la vara exige deprecacion y `ids_alias` a TRES.
# La ficha, en cambio, dice con sus palabras que solo se funde con
# `enfoque_mercado_voc` y que los otros dos hay que TENERLOS DELANTE. Resultado
# medido antes de este parche: `OP-D-02` sale `SIN CUMPLIR` con
# *"1 absorbido(s) OK de 3"*, y la fase 02 publica `sin cumplir: 8`.
#
# LO QUE LA FICHA DICE, LITERAL (campo `nota` de `OP-D-02`, correccion declarada
# de la vuelta 33): *"homework_frontend_loading y voice_of_customer_homework NO
# ENTRAN EN LA FUSION y se quedan en la nomina como lo que el punto 4 del orden
# interno siempre dijo, TENER DELANTE. El campo `nodos` NO se toca: la nomina es
# el universo del acto que hay que leer y simular junto (banco 9.24 con P.12), no
# la lista de lo que se funde"*.
#
# EL PATRON, Y NO ES INVENTADO: es el de la LISTA BLANCA DE `OP-C-05`, donde
# *"cada entrada de la lista blanca cita su lectura"*. UNA EXCEPCION SIN CITA ES
# UN AGUJERO. Aqui la cita se VERIFICA contra la ficha DEL DIA: cada entrada trae
# las FRASES LITERALES que la sostienen, y si una sola de esas frases ya no esta
# en la ficha, LA EXCEPCION NO APLICA y la operacion vuelve a medirse con la vara
# ancha, diciendolo en voz alta (banco 9, fallar ruidoso). Una excepcion que
# sobrevive a la desaparicion de su cita es un interruptor, no una excepcion.
#
# LO QUE ESTA TABLA NO HACE, Y SE DICE PARA QUE NO SE CONFUNDA: no toca el campo
# `nodos` de ninguna ficha, no deprecia nada, no llama cumplida a ninguna
# operacion cuyos absorbidos DE VERDAD esten pendientes, y no se aplica a ninguna
# operacion que no este nombrada aqui con su adjudicacion.

EXCEPCIONES_DE_ABSORBIDOS = {
    "OP-D-02": {
        "no_absorbidos": ["homework_frontend_loading", "voice_of_customer_homework"],
        "adjudicacion": "adjudicacion 6.4 del acta 161 (docs/loop/ACTA_AUDITOR.md, "
                        "seccion 6.4), sobre la correccion declarada de la vuelta 33 "
                        "en el campo `nota` de la propia ficha",
        "frases": [
            "homework_frontend_loading y voice_of_customer_homework NO ENTRAN EN LA FUSION",
            "El campo nodos NO se toca: la nomina es el universo del acto",
        ],
    },
}


def excepcion_de_absorbidos(op):
    """Los nodos que la ficha manda TENER DELANTE y no absorber, con su cita
    COMPROBADA contra el texto de la ficha de hoy.

    PURA A PROPOSITO salvo por leer el dict `op` que se le pasa: el caso positivo
    por mutacion le da fichas fabricadas en memoria.

    Devuelve (exentos, nota, avisos):
      - `exentos`: lista de ids que NO cuentan como absorbidos. VACIA si la
        excepcion no aplica, y entonces la vara mide como siempre.
      - `nota`: texto para la celda, que NOMBRA la excepcion y su adjudicacion.
        Nunca se calla: una excepcion en silencio seria peor que el rojo.
      - `avisos`: lo que no cuadra. Con avisos, `exentos` sale VACIA."""
    e = EXCEPCIONES_DE_ABSORBIDOS.get(op.get("id_op"))
    if not e:
        return [], "", []
    texto = " ".join(str(op.get(c) or "") for c in ("nota", "preservar", "verificacion"))
    avisos = []
    for frase in e["frases"]:
        if frase not in texto:
            avisos.append("la frase que sostiene la excepcion YA NO ESTA en la ficha: %r"
                          % frase)
    nomina = list(op.get("nodos") or [])
    for x in e["no_absorbidos"]:
        if x not in nomina:
            avisos.append("la excepcion nombra %s y ese id ya no esta en el campo `nodos` "
                          "de la ficha" % x)
    if avisos:
        return [], ("EXCEPCION DE ABSORBIDOS NO APLICADA (%s): %s. Se mide con la vara "
                    "ancha, como si la excepcion no existiera."
                    % (e["adjudicacion"], "; ".join(avisos))), avisos
    nota = ("EXCEPCION DE ABSORBIDOS APLICADA, %s: %s NO cuentan como absorbidos porque la "
            "ficha manda TENERLOS DELANTE, no fundirlos, y sus frases se comprobaron hoy "
            "en la propia ficha" % (e["adjudicacion"], ", ".join(e["no_absorbidos"])))
    return list(e["no_absorbidos"]), nota, []


def destino_de_fusion(op, nodos, fallos, resolver=None):
'''

ANCLA_ABSORBIDOS = """    sup = op.get("superviviente")
    absorbidos = [x for x in (op.get("nodos") or []) if x != sup]
"""

NUEVO_ABSORBIDOS = """    sup = op.get("superviviente")
    # ~~absorbidos = [x for x in (op.get("nodos") or []) if x != sup]~~
    # CORRECCION DECLARADA (vuelta 162, TAREA 2.b, adjudicacion 6.4 del acta 161).
    # LA LINEA VIEJA QUEDA ARRIBA, TACHADA Y LEGIBLE, porque con ella se dieron
    # todos los veredictos de esta vara hasta hoy. LO QUE CAMBIA: los ids que una
    # EXCEPCION CITADA declara como TENER DELANTE salen del saco de absorbidos.
    # Sin entrada en la tabla, `exentos` es vacia y esto es la linea de arriba.
    exentos, nota_excepcion, _avisos = excepcion_de_absorbidos(op)
    absorbidos = [x for x in (op.get("nodos") or []) if x != sup and x not in exentos]
"""

ANCLA_RETORNO_OK = '''    if faltas:
        return False, "%d absorbido(s) OK de %d; %s" % (
            len(absorbidos) - len({f.split()[0] for f in faltas}), len(absorbidos),
            "; ".join(faltas))
    return True, "superviviente %s vivo, %d absorbido(s) deprecado(s) y en ids_alias" % (
        sup, len(absorbidos))
'''

NUEVO_RETORNO_OK = '''    cola = (". " + nota_excepcion) if nota_excepcion else ""
    if faltas:
        return False, "%d absorbido(s) OK de %d; %s%s" % (
            len(absorbidos) - len({f.split()[0] for f in faltas}), len(absorbidos),
            "; ".join(faltas), cola)
    return True, "superviviente %s vivo, %d absorbido(s) deprecado(s) y en ids_alias%s" % (
        sup, len(absorbidos), cola)
'''

PARCHES = [
    ("tabla de excepciones", ANCLA_TABLA, BLOQUE_TABLA),
    ("saco de absorbidos", ANCLA_ABSORBIDOS, NUEVO_ABSORBIDOS),
    ("razon que nombra la excepcion", ANCLA_RETORNO_OK, NUEVO_RETORNO_OK),
]


def main():
    s = io.open(RUTA, encoding="utf-8").read()
    for nombre, ancla, nuevo in PARCHES:
        n = s.count(ancla)
        if n != 1:
            raise SystemExit("ROJO: el ancla %r aparece %d veces (se esperaba 1)" % (nombre, n))
        s = s.replace(ancla, nuevo, 1)
        print("  aplicado: %s" % nombre)
    io.open(RUTA, "w", encoding="utf-8", newline="\n").write(s)
    print("VERDE: %d parches aplicados sobre %s" % (len(PARCHES), RUTA))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
