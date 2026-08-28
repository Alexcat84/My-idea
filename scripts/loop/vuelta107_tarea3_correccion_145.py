# -*- coding: utf-8 -*-
"""vuelta107_tarea3_correccion_145.py . TAREA 3 de la vuelta 107, relectura
conjunta del puesto 145 (docs/loop/PROMPT_SIGUIENTE.md, TAREA 3), discutible
del acta de la vuelta 106.

DECISION: CEDO. El caso del auditor (3.1 y 3.2) gana. correccion_v106
caracterizo el paso 4 del hijo (proposito_como_motor_energia: "Evitar
sustituir el pensamiento profundo por 'mera accion fisica' como escape de la
incertidumbre") como MATERIAL AJENO a la madre (poder_a_traves_de_la_accion).
Releidos los dos nodos enteros hoy: no es ajeno. La madre hace la MISMA
advertencia dos veces, con vocabulario casi identico: su resumen ("La accion
debe ser voluntaria y comprometer a todo el organismo, no un mero movimiento
mecanico") y su paso 3 ("Asegurar que la accion sea genuina y comprometida
[...], no un gesto mecanico vacio"). El paso 4 del hijo es la MISMA cautela
contra la accion vacia/mecanica, mirada desde el angulo del pensamiento en
vez del angulo de la accion: no introduce un tema ajeno a la madre, repite
uno que la madre ya declara en dos pasos distintos del paso casado (paso 4).
Por eso NO es la especie de "metodo alternativo que compite con la linea
casada" (113, 119, 122): es una cautela consistente con el espiritu entero
del nodo madre, exactamente el patron que el acta 98 3.5 ya adjudico A CIEGAS
sobre ESTE MISMO puesto por su numero ("el hijo ejecuta la linea casada
articular/vincular/revisar y la tension vive en OTRA linea, su paso 4 contra
el paso 1 de la madre: caveat"). El acta 98 3.5 SI manda sobre este puesto:
la referencia mal citada en la razon vieja (decia "acta 97 3.3") no invalida
la doctrina, y correccion_v106 no la desmintio, solo no la aplico.

QUE HACE. Anade `correccion_v107` en el puesto_tramo 145 de
docs/plan/OP_E_03_LECTURA_TRAMO3_V98.jsonl, con `campo_corregido` igual a
`direccion_leida` y `valor_nuevo` igual al valor ORIGINAL de la fila (antes de
correccion_v106), o sea que REVIERTE el efecto de correccion_v106 sin
borrarla (EJECUTOR.md 8, "una correccion que tapa lo que corrige no se puede
auditar"). `contar_cierre_efectivo.py` aplica las correcciones en orden
ascendente de NN, asi que correccion_v107 (mas reciente) manda sobre
correccion_v106 para este campo.

USO:
  python scripts/loop/vuelta107_tarea3_correccion_145.py
"""
import json

RUTA = "docs/plan/OP_E_03_LECTURA_TRAMO3_V98.jsonl"

AGREGADO = {
    "campo_corregido": "direccion_leida",
    "valor_nuevo": "poder_a_traves_de_la_accion -> proposito_como_motor_energia",
    "cita_corregida": "banco 9.6.2 (test de reconocimiento); acta 98 3.5 (caveat fuera de la linea casada, adjudicado a ciegas sobre este mismo puesto)",
    "razon": (
        "CORRECCION DECLARADA (vuelta 107, TAREA 3, relectura conjunta con el auditor sobre "
        "el discutible 145 del acta de la vuelta 106). CEDO ante el caso del auditor: "
        "correccion_v106 no se borra, se revierte aqui con evidencia nueva. Releidos los dos "
        "nodos enteros. El resumen de la madre ('La accion debe ser voluntaria y comprometer a "
        "todo el organismo, no un mero movimiento mecanico') y su paso 3 ('Asegurar que la accion "
        "sea genuina y comprometida [...], no un gesto mecanico vacio') hacen la MISMA advertencia "
        "que el paso 4 del hijo ('Evitar sustituir el pensamiento profundo por mera accion fisica "
        "[...] como escape de la incertidumbre'), con vocabulario casi identico (mecanico / gesto "
        "vacio / mera accion). El paso 4 del hijo NO es material ajeno a la madre: es la cautela "
        "propia de la madre, mirada desde el pensamiento en vez de la accion. No compite con la "
        "linea casada (no ofrece un metodo alternativo, especie de 113/119/122): es un caveat sobre "
        "OTRA linea (paso 1 de la madre, 'actuar de inmediato'), exactamente el patron que el acta "
        "98 3.5 adjudico A CIEGAS sobre este mismo puesto por su numero, y que sigue vigente aunque "
        "su referencia estuviera mal citada (decia 'acta 97 3.3', es acta 98 3.5). SE REVIERTE: el "
        "par vuelve de NO RESUELTA a DIRECCION AFIRMADA. Clase D no cambia. Recontado con "
        "scripts/loop/contar_cierre_efectivo.py (docs/loop/SALIDA_V107_TAREA3_CIERRE_EFECTIVO.txt): "
        "clase A 3, B 2, C 1 (par 111), D 177; direccion 74/109 (59,6% NO RESUELTA); invertidas 2 "
        "(pares 16, 114). LA CIFRA VIGENTE ES 74 / 109 (59,6%). Marcado DISCUTIBLE otra vez para la "
        "relectura ciega del auditor, como pide la TAREA 3.4 del encargo."
    ),
}


def main():
    with open(RUTA, encoding="utf-8") as f:
        filas = [json.loads(l) for l in f if l.strip()]

    tocadas = 0
    for fila in filas:
        if fila.get("puesto_tramo") == 145:
            assert "correccion_v106" in fila, "145 debe traer correccion_v106 antes de revertirla"
            assert "correccion_v107" not in fila
            fila["correccion_v107"] = AGREGADO
            tocadas += 1
    assert tocadas == 1, tocadas

    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        for fila in filas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

    print("puesto 145: correccion_v107 anadida. tocadas=%d" % tocadas)


if __name__ == "__main__":
    main()
