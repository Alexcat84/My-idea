"""Vuelta 47, TAREA 1: las correcciones declaradas de la decision del fundador.

LA DECISION (19 ago 2026, docs/loop/paradas/2026-08-19-punto-brillante-DECISION.md,
rama a): el bloque del punto brillante SE QUEDA en puntos_brillantes_antes_del_pivote.
EL CRITERIO que la propia decision escribe y que se cita en cada correccion: cuando dos
textos sellados chocan, GANA EL QUE APLICO LA REGLA MAS RECIENTE DEL FUNDADOR, y el
perdedor se corrige. Gana la fase 01 del 14 ago 2026 (P.18 punto 3, nodo propio);
pierden los CUATRO textos del 12 ago 2026.

Este instrumento toca TRES de los cuatro (los que viven en OPERACIONES.jsonl) mas el
sello de OP-D-07. El cuarto (FRONTERAS_DECLARADAS.md linea 82) y la re-declaracion de
la frontera van en su propia pagina, en markdown.

NADA SE BORRA: el texto viejo queda TACHADO con la marca de tachado y con su fecha
delante. Una correccion que tapa lo que corrige no se puede auditar.

Uso: python scripts/loop/vuelta47_correcciones_p18.py [--escribir]
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

CRITERIO = (
    "CORRECCION DECLARADA, 19 ago 2026 (vuelta 47), DECISION DEL FUNDADOR "
    "(docs/loop/paradas/2026-08-19-punto-brillante-DECISION.md, rama a), con el "
    "criterio que la propia decision escribe: CUANDO DOS TEXTOS SELLADOS CHOCAN, GANA "
    "EL QUE APLICO LA REGLA MAS RECIENTE DEL FUNDADOR, Y EL PERDEDOR SE CORRIGE. Aqui "
    "gana la fase 01 del 14 ago 2026, que aplico P.18 punto 3 y formo NODO PROPIO; "
    "pierde este texto, sellado el 12 ago 2026."
)

VIEJO_OPD07_V2 = (
    "EL BLOQUE DEL PUNTO BRILLANTE NO SE PIERDE: viaja entero al superviviente del "
    "acto I, que es la puerta de metricas, y es ademas un lado de la FRONTERA "
    "DECLARADA del 1298. Si el destejido lo deja fuera, la frontera se queda sin uno "
    "de sus dos lados"
)

NUEVO_OPD07_V2 = (
    "~~" + VIEJO_OPD07_V2 + "~~ (texto del 12 ago 2026; NO SE BORRA). " + CRITERIO +
    " EL TEXTO QUE MANDA HOY: EL BLOQUE DEL PUNTO BRILLANTE NO SE PIERDE Y NO VIAJA. "
    "SE QUEDA ENTERO EN SU NODO PROPIO, puntos_brillantes_antes_del_pivote, creado por "
    "OP-F-04-WEI el 14 ago 2026 (commit 1eef1c6b) con la lectura declarada en "
    "docs/plan/01_FUENTES.md linea 982 (decision_pivote_perseverar, pasos 5 a 9, "
    "destino NODO PROPIO, por P.18 punto 3: ningun miembro de la familia coincidia, "
    "porque identificacion_bolsas_virales segmenta por coeficiente viral y "
    "leaky_bucket_metaphor y fases_traccion_producto miran por donde se FUGAN los "
    "clientes, y el bloque hace la pregunta contraria a la fuga). ESE NODO PROPIO ES "
    "HOY EL LADO DEL PUNTO BRILLANTE DE LA FRONTERA DECLARADA DEL 1298, y ya no lo es "
    "la puerta de metricas. MEDIDO EN LA VUELTA 47 con instrumento propio y no "
    "copiado de un acta: los 5 pasos viven byte a byte en "
    "puntos_brillantes_antes_del_pivote, 0 de 5 en pivotar_o_perseverar y 0 de 5 en "
    "decision_pivote_perseverar. LA FRONTERA NO SE QUEDA SIN LADO: CAMBIA DE SEDE, y "
    "su re-declaracion vive en docs/plan/FRONTERAS_DECLARADAS.md con correccion "
    "declarada de la misma fecha."
)

VIEJO_OPM03I_PRES = (
    "del que muere, ya destejido: EL BLOQUE DEL PUNTO BRILLANTE entero, pasos 5 a 9"
)

NUEVO_OPM03I_PRES = (
    "~~" + VIEJO_OPM03I_PRES + "~~ (texto del 12 ago 2026; NO SE BORRA). " + CRITERIO +
    " EL QUE MUERE YA NO TRAE ESE BLOQUE, Y ESTA FUSION NO LO PRESERVA PORQUE NO LO "
    "RECIBE: el bloque salio de decision_pivote_perseverar el 14 ago 2026 por "
    "OP-F-04-WEI (commit 1eef1c6b) y vive entero en su nodo propio "
    "puntos_brillantes_antes_del_pivote (docs/plan/01_FUENTES.md linea 982, P.18 punto "
    "3). MEDIDO EN LA VUELTA 47: 0 de 5 pasos en el que muere, 5 de 5 en el nodo "
    "propio. LO QUE ESTA FUSION SI TIENE QUE HACER CON EL BLOQUE, y es lo unico: NO "
    "TOCARLO Y NO PERDER SU ARISTA. decision_pivote_perseverar nombra hoy a "
    "puntos_brillantes_antes_del_pivote en nodos_siguientes y este lo nombra en "
    "nodos_previos, medido en los dos sentidos; al morir el sujeto esa arista se "
    "REDIRIGE al superviviente pivotar_o_perseverar como cualquier otra entrada del "
    "que muere, con su espejo. EL NODO PROPIO NO SE ABSORBE NI SE FUNDE: absorberlo "
    "seria deshacer P.18 punto 3, que es la regla mas reciente del fundador sobre "
    "este bloque."
)

VIEJO_OPM03I_V3 = (
    "el bloque del punto brillante esta entero y es identificable como bloque: la "
    "frontera del 1298 lo necesita nombrado"
)

NUEVO_OPM03I_V3 = (
    "~~" + VIEJO_OPM03I_V3 + "~~ (texto del 12 ago 2026; NO SE BORRA). " + CRITERIO +
    " EL BLOQUE ESTA ENTERO Y ES IDENTIFICABLE COMO BLOQUE, PERO EN SU NODO PROPIO "
    "puntos_brillantes_antes_del_pivote, QUE NO ES NINGUNO DE LOS DOS NODOS DE ESTA "
    "FUSION. LO QUE ESTA VERIFICACION COMPRUEBA HOY, y son tres cosas medibles tras "
    "la fusion: 1) los 5 pasos del bloque siguen byte a byte en "
    "puntos_brillantes_antes_del_pivote, con su fuente Traction sola; 2) la arista del "
    "sujeto muerto hacia ese nodo queda REDIRIGIDA al superviviente "
    "pivotar_o_perseverar, con su espejo, y no se pierde; 3) el nodo propio sigue VIVO "
    "y NO deprecado. Si la fusion se llevara el bloque dentro del superviviente "
    "estaria deshaciendo P.18 punto 3."
)

SELLO_OPD07 = (
    " REGISTRO DE CIERRE, 19 ago 2026 (vuelta 47). CORRECCION DECLARADA, y el texto "
    "viejo se queda entero delante: OP-D-07 QUEDA SELLADA POR LA VIA DE OP-D-05 "
    "SELLADA, citada por su nombre. LA VIA, escrita en docs/plan/02_DESTEJIDOS.md "
    "linea 1765 (encabezado OP-D-05 SELLADA: LA FUSION UNICA DE LA SELECCION DEL CEO, "
    "19 ago 2026, vuelta 40) y en su linea 1773: un destejido CONSUMIDO POR LA FASE "
    "01, medido contra el nodo de hoy y con el commit que se lo llevo nombrado, es una "
    "forma YA ESCRITA de cerrar, y OP-D-05 la uso para quedar SELLADA. AQUI PASA LO "
    "MISMO: la cirugia que OP-D-07 legisla la consumio OP-F-04-WEI el 14 ago 2026, "
    "commit 1eef1c6b, DOS DIAS DESPUES de la fecha_corte de esta operacion. LAS TRES "
    "VERIFICACIONES, AL CIERRE: la 1 CUMPLE medida (el corte cae entre el paso 4 y el "
    "5; el nodo pasa de 9 pasos a 4 con prefijo verbatim de 4); la 3 CUMPLE medida (el "
    "campo fuente queda con UNA sola obra, The Lean Startup - Eric Ries); y la 2 QUEDA "
    "SATISFECHA ENTERA por las correcciones declaradas de esta misma vuelta, que es lo "
    "que faltaba: su mitad material ya cumplia (el bloque no se perdio, 5 de 5 byte a "
    "byte) y su mitad de RUTA dejo de estar en PARADA porque el fundador la decidio el "
    "19 ago 2026, y este mismo campo verificacion ya lo dice corregido arriba. LA "
    "DIFERENCIA CON OP-D-05, dicha sin taparla: alli el bloque se disolvio en otro "
    "nodo y nada aguas abajo dependia de donde aterrizara; aqui el bloque fue a NODO "
    "PROPIO, que es MAS trazable, y lo que dependia de su sede (OP-M-03-I y "
    "FRONTERAS_DECLARADAS.md) queda corregido en el mismo acto y no despues. EL CAMPO "
    "estado NO SE TOCA: sigue LISTA, por el mismo motivo escrito en las notas de "
    "OP-F-02 y de OP-D-04, que el encargo cita: ninguna pagina del plan define otro "
    "valor para ese campo y estrenar uno seria doctrina de esquema, no registro. LA "
    "PALABRA HECHA TAMPOCO SE ESTRENA AQUI: el registro dice SELLADA, que es la forma "
    "que la propia campana ya uso en OP-D-05, y no REGISTRO DE OPERACION HECHA. CERO "
    "NODOS TOCADOS POR ESTA OPERACION, ni en la vuelta 46 ni en la 47: volver a cortar "
    "un nodo ya cortado no es ejecutar, es fabricar."
)


def sep(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


def main():
    escribir = "--escribir" in sys.argv
    raw = io.open(OPS, encoding="utf-8", newline="").read()
    lineas = raw.split("\n")

    cambios = []
    salida = []
    for l in lineas:
        if not l.strip():
            salida.append(l)
            continue
        o = json.loads(l)
        if json.dumps(o, ensure_ascii=False) != l:
            print("PARADA: la linea de %s no sobrevive al round trip" % o.get("id_op"))
            return 2
        oid = o["id_op"]
        if oid == "OP-D-07":
            v = o["verificacion"]
            if v[1] != VIEJO_OPD07_V2:
                print("PARADA: la verificacion 2 de OP-D-07 no es la esperada")
                return 2
            v[1] = NUEVO_OPD07_V2
            cambios.append(("OP-D-07", "verificacion[2]", VIEJO_OPD07_V2, v[1]))
            n = o["nota"]
            if SELLO_OPD07.strip() in n:
                print("PARADA: OP-D-07 ya lleva el sello")
                return 2
            o["nota"] = n + SELLO_OPD07
            cambios.append(("OP-D-07", "nota (sello)", "(cola de la nota del 12 ago)",
                            SELLO_OPD07))
        if oid == "OP-M-03-I":
            p = o["preservar"]
            if p[1] != VIEJO_OPM03I_PRES:
                print("PARADA: el preservar 2 de OP-M-03-I no es el esperado")
                return 2
            p[1] = NUEVO_OPM03I_PRES
            cambios.append(("OP-M-03-I", "preservar[2]", VIEJO_OPM03I_PRES, p[1]))
            v = o["verificacion"]
            if v[2] != VIEJO_OPM03I_V3:
                print("PARADA: la verificacion 3 de OP-M-03-I no es la esperada")
                return 2
            v[2] = NUEVO_OPM03I_V3
            cambios.append(("OP-M-03-I", "verificacion[3]", VIEJO_OPM03I_V3, v[2]))
        salida.append(json.dumps(o, ensure_ascii=False))

    sep("LAS CUATRO ESCRITURAS, UNA POR UNA, CON EL TEXTO VIEJO DELANTE")
    for op, campo, viejo, nuevo in cambios:
        print()
        print("  %s  %s" % (op, campo))
        print("  VIEJO: %s" % viejo[:260])
        print("  NUEVO: %s" % nuevo[:260])
        print("  (el nuevo, entero, mide %d caracteres)" % len(nuevo))

    sep("GUARDAS")
    nuevo_raw = "\n".join(salida)
    print("  lineas antes: %d   lineas despues: %d" % (len(lineas), len(salida)))
    print("  campos escritos: %d" % len(cambios))
    for mal, nombre in ((u"—", "guion largo"), (u"–", "guion medio")):
        print("  %s en el fichero entero: %d" % (nombre, nuevo_raw.count(mal)))
    antes = {json.loads(l)["id_op"]: l for l in lineas if l.strip()}
    despues = {json.loads(l)["id_op"]: l for l in salida if l.strip()}
    movidos = sorted(k for k in antes if antes[k] != despues[k])
    print("  operaciones cuya linea cambia: %d  %s" % (len(movidos), movidos))
    print("  operaciones intactas byte a byte: %d de %d"
          % (len(antes) - len(movidos), len(antes)))
    print("  el texto viejo sigue dentro del nuevo, los cuatro:")
    for etiqueta, viejo in (("OP-D-07 v2", VIEJO_OPD07_V2),
                            ("OP-M-03-I preservar", VIEJO_OPM03I_PRES),
                            ("OP-M-03-I v3", VIEJO_OPM03I_V3)):
        print("    %-22s %s" % (etiqueta, "SI" if viejo in nuevo_raw else "NO"))

    if escribir:
        io.open(OPS, "w", encoding="utf-8", newline="").write(nuevo_raw)
        print()
        print("  ESCRITO en %s" % OPS)
    else:
        print()
        print("  SIMULACION: no se escribio nada. Anade --escribir para aplicar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
