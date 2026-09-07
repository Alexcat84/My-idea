# -*- coding: utf-8 -*-
r"""_v207_t2_vara.py . LA VARA DE LA MESA `OP-L-01`, SACADA DE SU PROPIA FICHA Y
SELLADA ANTES DE ABRIR NINGUNO DE LOS TRES DOCUMENTOS (encargo 207, punto 2.a:
*"Esa lista es tu vara, y la escribes ANTES de abrir ningun documento, por el
mismo motivo por el que la ciega se sella antes de verificar: una vara escrita
despues de mirar se acomoda a lo que se vio"*).

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (encargo 2.e, moratoria de `AUDITOR.md` 6.3). **NO ES UN LECTOR DE
PROPOSITO GENERAL:** lee UNA linea de `docs/plan/OPERACIONES.jsonl` con `json` y
comprueba literales.

LO QUE HACE, Y ES LO UNICO QUE HACE: publica **la lista numerada de lo que la
ficha dice que esta mesa produce**, y **cada punto va con la CITA LITERAL del
campo y del elemento de la ficha del que sale**. NINGUNA CITA SE TECLEA A CIEGAS:
este computo **COMPRUEBA que cada cita aparece verbatim** dentro del elemento que
dice, y **CAE EN ROJO sin escribir nada** si alguna no aparece. Una vara cuyas
citas no se comprueban no es una vara.

POR QUE LA CITA ES `campo[indice]` Y NO UN NUMERO DE LINEA: la ficha entera vive
en **UNA sola linea** de `docs/plan/OPERACIONES.jsonl`, la **41**. Decir *"linea
41"* once veces no localiza nada. La sede fina de cada punto es el campo y su
posicion dentro de la lista, y eso es lo que se publica, con la linea del fichero
al lado.

**ESTE COMPUTO NO ABRE NI MIDE `LECTURAS_DIRIGIDAS.md`, NI
`INTRA_DOMINIO_INFORME.md`, NI `BANCO_DE_TEXTOS.md`.** Esos se abren en el cotejo,
que es otro fichero y otro commit.

**NO TOCA EL CAMPO `estado`** (`AUDITOR.md` 0): lo lee para publicarlo como dato
de la ficha y no lo mueve, no lo levanta y no lo usa para decidir nada.
"""
import hashlib
import io
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
NL = chr(10)
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
FICHA = "OP-L-01"

# LA VARA. Cada fila es (clave, que produce la mesa, campo, indice, cita literal).
# LA CITA SE COMPRUEBA CONTRA LA FICHA: si no aparece verbatim, esto cae en ROJO.
PUNTOS = [
    ("V.1",
     "UN DOCUMENTO `LECTURAS_DIRIGIDAS.md` CON LAS ONCE LECTURAS Y, EN CADA UNA, "
     "SU RAZON",
     "evidencia", 0,
     "LECTURAS_DIRIGIDAS.md, las once con su razon"),
    ("V.2",
     "UNA SECCION 52 EN `INTRA_DOMINIO_INFORME.md` CON LAS PAREJAS QUE EL "
     "EJERCICIO NO PUEDE CERRAR",
     "evidencia", 1,
     "INTRA_DOMINIO_INFORME.md seccion 52, las parejas que el ejercicio no puede cerrar"),
    ("V.3",
     "UNA `TABLA VIVA DE LOS PUROS` EN `BANCO_DE_TEXTOS.md`",
     "evidencia", 2,
     "BANCO_DE_TEXTOS.md, TABLA VIVA DE LOS PUROS"),
    ("V.4",
     "LA CIFRA MEDIDA DEL 11 AGO 2026: 205 PARES INTERNOS FUERA DE COLA SOBRE "
     "221 COMPONENTES",
     "evidencia", 3,
     "MEDIDO el 11 ago 2026: 205 pares internos fuera de cola sobre 221 componentes"),
    ("V.5",
     "LA TANDA DE ONCE LECTURAS DIRIGIDAS, HECHAS EL 11 AGO 2026",
     "adjudicacion", None,
     "TANDA DE ONCE LECTURAS DIRIGIDAS, hechas el 11 ago 2026."),
    ("V.6",
     "LAS ONCE CON LA MISMA VARA Y EL MISMO FORMATO DE VEREDICTO QUE EL CRIBADO, "
     "Y MARCADAS COMO LECTURA DIRIGIDA",
     "adjudicacion", None,
     "Misma vara y mismo formato de veredicto que el cribado, MARCADAS COMO LECTURA DIRIGIDA"),
    ("V.7",
     "EL SALDO DE LA TANDA: 2 `A` Y 9 `D`",
     "adjudicacion", None,
     "SALDO: 2 A y 9 D."),
    ("V.8",
     "LAS ONCE NOMBRADAS UNA A UNA, DE `LD-01` A `LD-11`, CADA UNA CON SU "
     "VEREDICTO",
     "nota", None,
     "LAS ONCE: LD-01 junta asesora D (cierra 6 de 6); LD-02 canal fisico contra digital D (ROMPE el sub-puro)"),
    ("V.9",
     "UNA CLASE NUEVA, `A DE BLOQUE`, NACIDA EN `LD-06`, CON SU DEFINICION",
     "nota", None,
     "CLASE NUEVA: A DE BLOQUE (LD-06). La A no es entre los nodos: es entre el BLOQUE INJERTADO de uno y el otro nodo entero."),
    ("V.10",
     "EL ARREGLO DE `LD-06` DICHO POR SU NOMBRE: NO ES FUSION DE NODOS, ES "
     "DESTEJIDO MAS FUSION PARCIAL",
     "nota", None,
     "El arreglo no es fusion de nodos: es DESTEJIDO mas fusion parcial."),
    ("V.11",
     "LA LECCION DEL SALDO: 9 DE 11 SALIERON SANAS, Y POR QUE ESOS PARES NO "
     "ESTABAN EN LA COLA",
     "nota", None,
     "LA LECCION DEL SALDO: 9 de 11 salieron SANAS."),
    ("V.12",
     "LA CLAUSULA 1 DE VERIFICACION: NINGUNA DE LAS ONCE VIVE EN "
     "`INTRA_DOMINIO_VEREDICTOS.jsonl`",
     "verificacion", 0,
     "ninguna de las once aparece en INTRA_DOMINIO_VEREDICTOS.jsonl: viven solo aqui"),
    ("V.13",
     "LA CLAUSULA 2 DE VERIFICACION: EL MARCADOR DEL CRIBADO NO SE MUEVE",
     "verificacion", 1,
     "el marcador del cribado no se mueve: sigue en 2.117"),
    ("V.14",
     "LA CLAUSULA 3 DE VERIFICACION: CADA NOMINA AFECTADA SE RE-MIDE CON SU "
     "COBERTURA AL LADO",
     "verificacion", 2,
     "cada nomina afectada se re-mide con su cobertura al lado (banco 9.26)"),
]

# QUE PUNTOS SE COTEJAN CONTRA DOCUMENTO, Y CUALES NO, DICHO AQUI Y NO DESPUES.
# EL COTEJO DEL 2.b ES CONTRA LOS TRES DOCUMENTOS QUE LA EVIDENCIA NOMBRA. Los
# puntos que NO son documentales se marcan aqui, ANTES de mirar nada, para que no
# se pueda decidir despues cual se exime.
NO_DOCUMENTALES = {
    "V.4": ("es una CIFRA MEDIDA, no un documento: su sede seria una salida de "
            "instrumento del 11 ago 2026, no ninguno de los tres"),
    "V.12": ("es una CLAUSULA DE VERIFICACION contra "
             "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, que NO es ninguno de los "
             "tres documentos de la evidencia"),
    "V.13": ("es una CLAUSULA DE VERIFICACION contra el marcador del cribado, "
             "que NO vive en ninguno de los tres"),
    "V.14": ("es una CLAUSULA DE VERIFICACION contra las nominas del "
             "inventario, que NO viven en ninguno de los tres"),
}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 207, TAREA 2.a: LA VARA DE LA MESA OP-L-01, SACADA DE SU FICHA")
    w("Y SELLADA ANTES DE ABRIR NINGUNO DE LOS TRES DOCUMENTOS")
    w("=" * 78)
    w("")

    crudo = io.open(OPS, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    w("A) LA SEDE DE LA FICHA, POR LAS DOS CONVENCIONES")
    w("   docs/plan/OPERACIONES.jsonl: %d bytes en disco y %d normalizado a LF"
      % (len(crudo), len(lf)))
    w("   sha256 disco %s | sha256 LF %s"
      % (hashlib.sha256(crudo).hexdigest()[:16],
         hashlib.sha256(lf).hexdigest()[:16]))
    w("")

    linea_n, ficha, linea_txt = None, None, None
    for i, l in enumerate(lf.decode("utf-8").split("\n"), 1):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get("id_op") == FICHA:
            linea_n, ficha, linea_txt = i, d, l
            break
    if ficha is None:
        w("   ROJO: no se encontro la ficha %s. NO SE ESCRIBE NADA." % FICHA)
        print(NL.join(L))
        return 1

    w("B) LA FICHA, LOCALIZADA Y SELLADA")
    w("   id_op: %s | linea del fichero: %d" % (FICHA, linea_n))
    w("   CIFRA campos de la ficha: %d" % len(ficha))
    w("   CIFRA bytes de la linea de la ficha: %d"
      % len(linea_txt.encode("utf-8")))
    w("   sha256 de la linea de la ficha: %s"
      % hashlib.sha256(linea_txt.encode("utf-8")).hexdigest())
    w("   tipo: %s | fase: %s | orden: %s"
      % (ficha.get("tipo"), ficha.get("fase"), ficha.get("orden")))
    w("   depende_de: %s (CIFRA: %d)"
      % (ficha.get("depende_de"), len(ficha.get("depende_de") or [])))
    w("   bloquea_a: %s (CIFRA: %d)"
      % (ficha.get("bloquea_a"), len(ficha.get("bloquea_a") or [])))
    w("   fecha_corte: %s" % ficha.get("fecha_corte"))
    w("   estado: %s   <- SE LEE COMO DATO Y NO SE TOCA (AUDITOR.md 0)"
      % ficha.get("estado"))
    w("   CIFRA elementos de `evidencia`: %d" % len(ficha.get("evidencia") or []))
    w("   CIFRA elementos de `verificacion`: %d"
      % len(ficha.get("verificacion") or []))
    w("   de esos, CORRECCIONES DECLARADAS: %d"
      % sum(1 for x in (ficha.get("verificacion") or [])
            if x.startswith("CORRECCION DECLARADA")))
    w("")

    w("C) LA VARA. CADA PUNTO CON SU CITA COMPROBADA CONTRA LA FICHA")
    w("   (si una cita no aparece VERBATIM en el elemento que dice, esto cae en")
    w("    ROJO y no escribe nada: una vara con citas sin comprobar no es vara)")
    w("")
    rojos = []
    for clave, produce, campo, idx, cita in PUNTOS:
        valor = ficha.get(campo)
        if idx is None:
            texto = valor if isinstance(valor, str) else NL.join(valor or [])
            sede = "%s" % campo
        else:
            if not isinstance(valor, list) or idx >= len(valor):
                rojos.append("%s: el campo %r no tiene elemento %s"
                             % (clave, campo, idx))
                continue
            texto = valor[idx]
            sede = "%s[%d]" % (campo, idx)
        ok = cita in texto
        w("   %-5s %s" % (clave, produce))
        w("         sede: `%s`, linea %d del fichero" % (sede, linea_n))
        w("         cita: %r" % cita[:150])
        w("         la cita aparece VERBATIM en esa sede: %s"
          % ("SI" if ok else "NO"))
        if not ok:
            rojos.append("%s: la cita NO aparece en %s" % (clave, sede))
        w("")
    w("   CIFRA puntos de la vara: %d" % len(PUNTOS))
    w("   CIFRA citas que NO aparecen verbatim: %d" % len(rojos))
    for r in rojos:
        w("      " + r)
    if rojos:
        w("   ROJO. NO SE SELLA NADA.")
        print(NL.join(L))
        return 1
    w("")

    w("D) EL REPARTO DE LA VARA, DECLARADO ANTES DE MIRAR NINGUN DOCUMENTO")
    doc = [c for c, _p, _ca, _i, _ci in PUNTOS if c not in NO_DOCUMENTALES]
    w("   CIFRA puntos que SE COTEJAN contra los tres documentos: %d" % len(doc))
    w("      %s" % ", ".join(doc))
    w("   CIFRA puntos que NO son documentales: %d" % len(NO_DOCUMENTALES))
    for c, motivo in NO_DOCUMENTALES.items():
        w("      %-5s %s" % (c, motivo))
    w("   ESTE REPARTO SE SELLA AQUI. Si el cotejo quisiera mover un punto de un")
    w("   lado al otro despues de mirar, eso seria acomodar la vara a lo visto, y")
    w("   el sello lo delataria.")
    w("")

    w("E) LOS TRES DOCUMENTOS QUE LA FICHA NOMBRA COMO SU EVIDENCIA")
    for i, e in enumerate(ficha.get("evidencia") or []):
        w("   evidencia[%d] %s" % (i, e[:120]))
    w("   ESTE COMPUTO NO LOS ABRE Y NO LOS MIDE. Eso es el 2.b.")
    w("")
    w("FIN DE LA VARA")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(RAIZ, "docs", "loop", "SALIDA_V207_T2_VARA.txt"),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
