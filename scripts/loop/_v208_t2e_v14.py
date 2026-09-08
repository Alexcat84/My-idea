# -*- coding: utf-8 -*-
r"""_v208_t2e_v14.py . TAREA 2.e DE LA VUELTA 208: LA `V.14`, CORREGIDA POR
ADICION Y NO REHECHA, CON LAS DOS CUENTAS PUBLICADAS JUNTAS.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3). SOLO MIDE: no escribe en ninguna sede y NO
TOCA EL SELLO.

QUIEN LO ENCARGA: la adjudicacion `6.4` del acta 207. La `V.14` se sello como NO
DOCUMENTAL *"porque las nominas del inventario no viven en ninguno de los tres"*,
y la cobertura de esas nominas vive en la `TABLA VIVA DE LOS PUROS`, que esta en
`BANCO_DE_TEXTOS.md`, **que es uno de los tres**. Es la misma especie que la `D.2`
de la 207 con la `V.4`.

LA REGLA QUE SE APLICA, LITERAL DE LA `6.4`: *"un punto de una vara sellada que
aparece del otro lado se corrige POR ADICION DECLARADA, NUNCA REESCRIBIENDO EL
SELLO, Y LAS DOS CUENTAS SE PUBLICAN JUNTAS"*.

EL SELLO SE LEE, NO SE ESCRIBE: `PUNTOS` y `NO_DOCUMENTALES` se IMPORTAN de
`scripts/loop/_v207_t2_vara.py`, committeado en `d7ab4545` ANTES de que la 207
abriera ningun documento. Este computo NO puede cambiarlo, y lo comprueba
midiendo su `sha256` al entrar y al salir.
"""
import argparse
import hashlib
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

sys.path.insert(0, AQUI)
from _v207_t2_vara import PUNTOS, NO_DOCUMENTALES  # noqa: E402

VUELTA = 208
BANCO = os.path.join(RAIZ, "docs", "BANCO_DE_TEXTOS.md")
SELLO = os.path.join(AQUI, "_v207_t2_vara.py")
COTEJO_207 = os.path.join(LOOP, "SALIDA_V207_T2_COTEJO.txt")
COTEJO_HOY = os.path.join(LOOP, "SALIDA_V%d_T2D_COTEJO_REPETIDO.txt" % VUELTA)
MARCA_FILA = "(FILA CORREGIDA EN LA VUELTA %d)" % VUELTA


def sha(ruta):
    d = io.open(ruta, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return (len(d), len(lf), hashlib.sha256(d).hexdigest()[:16],
            hashlib.sha256(lf).hexdigest()[:16])


def veredictos_de(ruta):
    """LOS VEREDICTOS DEL COTEJO, LEIDOS DE SU FICHERO DE SALIDA Y NO TECLEADOS.
    Devuelve {clave: (documento, veredicto)}."""
    out = {}
    if not os.path.isfile(ruta):
        return out
    for l in io.open(ruta, encoding="utf-8").read().replace(
            chr(13) + NL, NL).split(NL):
        m = re.match(r"^   (V\.\d+)\s+(\S+)\s+(NO DOCUMENTAL|A MEDIAS|NO CUBRE|CUBRE)\b", l)
        if m:
            out[m.group(1)] = (m.group(2), m.group(3))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default="T2E_V14")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2.e: LA `V.14`, CORREGIDA POR ADICION Y NO REHECHA"
      % VUELTA)
    w("=" * 78)
    w("")

    w("A) EL SELLO, MEDIDO AL ENTRAR")
    d0, lf0, sd0, sl0 = sha(SELLO)
    w("   scripts/loop/_v207_t2_vara.py: %d bytes en disco y %d normalizado a LF,"
      % (d0, lf0))
    w("   sha256 disco %s y sha256 LF %s" % (sd0, sl0))
    w("   CIFRA puntos de la vara sellada: %d" % len(PUNTOS))
    w("   CIFRA puntos sellados como NO DOCUMENTALES: %d" % len(NO_DOCUMENTALES))
    w("   CIFRA puntos sellados como DOCUMENTALES: %d"
      % (len(PUNTOS) - len(NO_DOCUMENTALES)))
    w("")

    w("B) LO QUE EL SELLO DICE DE LA `V.14`, VERBATIM Y SIN PARAFRASEAR")
    motivo = NO_DOCUMENTALES.get("V.14")
    w("   `NO_DOCUMENTALES['V.14']` = %r" % motivo)
    p14 = [p for p in PUNTOS if p[0] == "V.14"]
    if p14:
        w("   su enunciado en la vara: %s" % str(p14[0][1])[:180])
        w("   su sede en la ficha:     %s" % str(p14[0][2])[:180])
        w("   su cita literal:         %s" % str(p14[0][3])[:180])
    w("")

    w("C) LA SEDE QUE EL SELLO DECIA QUE NO EXISTIA, MEDIDA HOY")
    w("   el sello dice que las nominas del inventario NO viven en ninguno de los")
    w("   tres documentos. LA COBERTURA DE ESAS NOMINAS VIVE EN LA `TABLA VIVA DE")
    w("   LOS PUROS`, QUE ESTA EN `docs/BANCO_DE_TEXTOS.md`, UNO DE LOS TRES.")
    ban = io.open(BANCO, encoding="utf-8").read().replace(
        chr(13) + NL, NL).split(NL)
    cab = [i for i, l in enumerate(ban, 1)
           if l.startswith("#### TABLA VIVA DE LOS PUROS")]
    w("   la tabla abre en docs/BANCO_DE_TEXTOS.md:%s"
      % (cab[0] if cab else "(el patron no la encontro)"))
    filas = [(i, l) for i, l in enumerate(ban, 1) if MARCA_FILA in l]
    w("   CIFRA filas CORREGIDAS por esta vuelta dentro de esa tabla: %d" % len(filas))
    if not filas:
        w("   EL PATRON NO ENCONTRO NINGUNA FILA CORREGIDA. No se publica cifra.")
    for i, l in filas:
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        w("      docs/BANCO_DE_TEXTOS.md:%d | %s | cobertura %s de %s"
          % (i, c[1][:44], c[4], c[3]))
    w("   CIFRA de esas filas que llevan la palabra COBERTURA escrita: %d"
      % len([1 for _i, l in filas if "COBERTURA" in l.upper()]))
    w("")

    w("D) LAS DOS CUENTAS, PUBLICADAS JUNTAS, QUE ES LO QUE LA `6.4` PIDE")
    v207 = veredictos_de(COTEJO_207)
    vhoy = veredictos_de(COTEJO_HOY)
    w("   CIFRA veredictos leidos de docs/loop/SALIDA_V207_T2_COTEJO.txt: %d"
      % len(v207))
    w("   CIFRA veredictos leidos de docs/loop/SALIDA_V%d_T2D_COTEJO_REPETIDO.txt:"
      " %d" % (VUELTA, len(vhoy)))
    doc_sellados = [p[0] for p in PUNTOS if p[0] not in NO_DOCUMENTALES]
    con_veredicto_doc = sorted(
        [k for k, (_d, ver) in vhoy.items() if ver != "NO DOCUMENTAL"],
        key=lambda x: int(x.split(".")[1]))
    w("   CUENTA 1, LA DEL SELLO (no se reescribe): %d puntos documentales"
      % len(doc_sellados))
    w("      %s" % ", ".join(doc_sellados))
    w("   CUENTA 2, LA DE LOS VEREDICTOS DE HOY: %d puntos con veredicto"
      " documental" % len(con_veredicto_doc))
    w("      %s" % ", ".join(con_veredicto_doc))
    fuera = [k for k in con_veredicto_doc if k not in doc_sellados]
    w("   CIFRA puntos con veredicto documental que el sello NO sello como tales:"
      " %d (%s)" % (len(fuera), ", ".join(fuera) or "ninguno"))
    for k in fuera:
        w("      %-6s sellado como NO DOCUMENTAL con este motivo: %s"
          % (k, str(NO_DOCUMENTALES.get(k))[:150]))
    w("")
    w("   LA ASIMETRIA SE DECLARA Y NO SE ARREGLA MOVIENDO EL SELLO. Mover un")
    w("   punto de lado despues de mirar es exactamente lo que sellar el reparto")
    w("   viene a impedir, y la `6.4` lo adjudico asi con todas las letras.")
    w("")

    w("E) LO QUE LA `V.14` DEBERIA LLEVAR, DECLARADO AL LADO Y NO SUSTITUYENDO AL")
    w("   SELLO")
    v14 = vhoy.get("V.14")
    w("   veredicto que el cotejo le da hoy, corrido tal cual: %s"
      % (v14[1] if v14 else "(no leido)"))
    tiene_sede = bool(filas)
    w("   la `V.14` TIENE sede en uno de los tres documentos: %s"
      % ("SI, docs/BANCO_DE_TEXTOS.md" if tiene_sede else "NO"))
    w("   y esa sede LLEVA la cobertura de las dos nominas que la mesa mueve: %s"
      % ("SI" if len(filas) == 2 else "NO, lleva %d de 2" % len(filas)))
    w("   POR TANTO, DECLARADO Y NO ESCRITO EN EL SELLO: la `V.14` es DOCUMENTAL")
    w("   y su sede es `docs/BANCO_DE_TEXTOS.md`, filas %s."
      % ", ".join(str(i) for i, _l in filas))
    w("   EL SELLO NO SE REESCRIBE, y sigue diciendo NO DOCUMENTAL con su motivo.")
    w("")

    w("=" * 78)
    w("EL CIERRE: EL SELLO, REMEDIDO PARA PROBAR QUE NO SE TOCO")
    w("=" * 78)
    d1, lf1, sd1, sl1 = sha(SELLO)
    w("   scripts/loop/_v207_t2_vara.py: %d bytes en disco y %d normalizado a LF,"
      % (d1, lf1))
    w("   sha256 disco %s y sha256 LF %s" % (sd1, sl1))
    igual = (d0, lf0, sd0, sl0) == (d1, lf1, sd1, sl1)
    w("   IDENTICO AL DE LA APERTURA DE ESTA CORRIDA: %s" % ("SI" if igual else "NO"))
    w("")
    w("FIN")
    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0 if igual else 1


if __name__ == "__main__":
    raise SystemExit(main())
