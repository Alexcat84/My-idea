# -*- coding: utf-8 -*-
"""vuelta66_registrar_acta65.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DE LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 65.

NO REESCRIBE NI UNA LINEA DE LAS SECCIONES DE ARRIBA: abre el fichero en modo
adosar y escribe detras. Es la via que esta pagina ya uso SEIS veces (acta 52 en
la linea 1250, acta 57 sobre el acto 25 en la 2475, acta 61 en la 2689, acta 62
en la 2933, acta 63 en la 3307 y acta 64 en la 3613).

LA GUARDA DE CITAS, heredada del registrador de la vuelta 65: ANTES de escribir,
cada cita de linea se coteja contra su fichero imprimiendo la linea citada; si
una sola no calza con la aguja que la tabla dice de ella, el instrumento cae en
ROJO y NO escribe nada. Aqui se cotejan citas de DOS ficheros, el acta y la
propia pagina de fusiones.

LA GUARDA DE IDEMPOTENCIA: si la seccion ya esta en la pagina, no se escribe
nada. Una pagina con la adjudicacion duplicada no falla, dice que si.

Uso:
  python scripts/loop/vuelta66_registrar_acta65.py [--simular]
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:65 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 65 DEL AUDITOR" corte=2026-08-20 motivo="el titulo nombra el ACTA que este registro transcribe, que es de la vuelta 65; el fichero es de la vuelta 66 y por eso el numero no calza con su propia vuelta a proposito"
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
NL = chr(10)

# (linea, aguja que esa linea TIENE que contener).
CITAS_ACTA = [
    (17018, "ACTA DE LA VUELTA 65 DEL AUDITOR"),
    (17036, "VERIFICACION POR CORRIDA PROPIA"),
    (17130, "RELECTURA CIEGA"),
    (17160, "CAIDAS DE ESTA TANDA"),
    (17163, "EJECUTOR: CERO de clase, CERO de cifra publicada y CERO de reporte"),
    (17171, "AUDITOR, UNA CAIDA DE ACTA CON NOMBRE"),
    (17185, "ADJUDICACION DE LOS DOCE DISCUTIBLES"),
    (17187, "D1, REGISTRAR OCHO A FAVOR Y NO NUEVE"),
    (17193, "D2, CORREGIR LOS DOS INSTRUMENTOS DE NOMBRE ESTABLE EN EL SITIO"),
    (17200, "D3, LA GUARDA N-ARIA QUE CRECE Y SE ESTRENA EL MISMO DIA"),
    (17206, "D3.b, LA PRIMERA FUSION N-ARIA"),
    (17213, "D4, UN TRAMO SIN NUMERO NO SE NUMERA"),
    (17215, "D5, DECLARAR EL ACTO 1 POR P.10"),
    (17224, "D6, VEREDICTO AUSENTE COMO NO CANDIDATO"),
    (17226, "D7, LOTE DE DOS ACTOS"),
    (17229, "D8, LAS CUATRO ADVERTENCIAS A CUBIERTO CON PERDIDA"),
    (17233, "D9, DIECISEIS APPEND Y EL NODO MAS LARGO DE LA CAMPANA"),
    (17238, "D10, TRES PERDIDAS CON ATENUANTE DECLARADO"),
    (17242, "D11, EL INCISO AL PASO 6"),
    (17246, "D12, ENSANCHAR EL DOSSIER SIN ENCARGO"),
    (17253, "LOS PENDIENTES DE DOCTRINA, ADJUDICADOS O NOMBRADOS"),
    (17255, "UN VEREDICTO AUSENTE NO ES UN PAR SIN LEER A EFECTOS DE P.10"),
    (17257, "extension de cuatro letras vigentes. PRIMERA"),
    (17260, "SEGUNDA"),
    (17265, "TERCERA"),
    (17269, "CUARTA"),
    (17273, "UNA LETRA EN DIVERGENCIA Y NO SE DEJA CALLADA"),
    (17284, "EL SUBCONJUNTO CERRADO DE UN ACTO CON PUENTE"),
    (17293, "UN ACTO CON DOS PUERTAS Y SIN PUENTE"),
    (17299, "LA MARCA PARA YA LO DICE EL APPEND DE UN HERMANO"),
    (17305, "EL INCISO DE CONDICIONES (heredado)"),
    (17307, "EL ESQUEMA DE OPERACIONES.jsonl (heredado)"),
    (17311, "METRICA DE CREDITO ACUMULADA"),
    (17338, "Rachas: REPORTE EN CERO"),
    (17342, "CONDICIONES DE PARADA"),
]
CITAS_PAGINA = [
    (62, "EL ORDEN DE ESTA FASE"),
    (1250, "LAS TRES ADJUDICACIONES DEL ACTA DE LA VUELTA 52"),
    (1377, "EL CARRIL GENERAL DE COLISIONES"),
    (2475, "LA ADJUDICACION DEL ACTA 57 SOBRE EL **ACTO 25**"),
    (2689, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 61"),
    (2933, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 62"),
    (3307, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 63"),
    (3486, "`OP-M-03-II`: EL REGISTRO DE LA FUSION"),
    (3613, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 64"),
    (3732, "EL REGISTRO DEL LOTE A"),
    (3744, "EL ACTO 1: `DECLARADO Y NO FUNDIDO` POR `P.10`"),
    (3792, "EL ACTO 3: LA PRIMERA FUSION DE MAS DE DOS MIEMBROS DE LA CAMPANA"),
]


def cotejar(ruta, citas, etq, callado=False):
    lineas = io.open(ruta, encoding="utf-8").read().split(NL)
    if not callado:
        print()
        print("  --- GUARDA DE CITAS: %s (%d lineas) ---" % (etq, len(lineas)))
    malas = []
    for n, aguja in citas:
        real = lineas[n - 1] if 0 < n <= len(lineas) else "(FUERA DE RANGO)"
        ok = aguja in real
        if not ok:
            malas.append((n, aguja, real))
        if not callado:
            print("     %-6d %-4s %s" % (n, "OK" if ok else "MAL", real.strip()[:104]))
    return malas


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v66_texto_acta65 import TEXTO  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 65 AL FINAL DE 03_FUSIONES.md")
    print("=" * 78)

    malas = cotejar(ACTA, CITAS_ACTA, "docs/loop/ACTA_AUDITOR.md")
    malas += cotejar(PAGINA, CITAS_PAGINA, "docs/plan/03_FUSIONES.md")
    print()
    print("  citas cotejadas: %d | MALAS: %d"
          % (len(CITAS_ACTA) + len(CITAS_PAGINA), len(malas)))
    if malas:
        print()
        print("ROJO: %d cita(s) no calzan y NO se escribe nada:" % len(malas))
        for n, aguja, real in malas:
            print("   linea %d deberia contener %r y contiene: %s" % (n, aguja, real[:90]))
        return 1

    t = TEXTO
    for mal, nombre in ((chr(8212), "guion largo"), (chr(8211), "guion medio")):
        if mal in t:
            print()
            print("ROJO: el texto trae un %s. PARADA." % nombre)
            return 1

    crudo = io.open(PAGINA, encoding="utf-8").read()
    if "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 65" in crudo:
        print()
        print("YA ADOSADA: la seccion del acta 65 ya esta en la pagina. No se escribe nada.")
        return 0

    antes = len(crudo.split(NL))
    print()
    print("  la pagina tiene %d lineas y el texto anade %d" % (antes, t.count(NL)))
    if a.simular:
        print()
        print("  SIMULACION: no se escribe nada. El texto empieza asi:")
        for l in t.split(NL)[:8]:
            print("     %s" % l[:100])
        print()
        print("FIN")
        return 0

    with io.open(PAGINA, "a", encoding="utf-8", newline=NL) as fh:
        fh.write(t)
    despues = len(io.open(PAGINA, encoding="utf-8").read().split(NL))
    print()
    print("GUARDAS TRAS ESCRIBIR")
    print("  lineas antes %d, despues %d (delta %d)" % (antes, despues, despues - antes))
    txt = io.open(PAGINA, encoding="utf-8").read()
    print("  guiones largos %d, guiones medios %d"
          % (txt.count(chr(8212)), txt.count(chr(8211))))
    re_malas = cotejar(PAGINA, CITAS_PAGINA, "re-cotejo tras adosar", callado=True)
    print("  las sedes de arriba siguen en su linea: %s"
          % ("OK (%d de %d)" % (len(CITAS_PAGINA) - len(re_malas), len(CITAS_PAGINA))
             if not re_malas else "ROJO"))
    print()
    print("VERDE: registro adosado y nada de arriba reescrito.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
