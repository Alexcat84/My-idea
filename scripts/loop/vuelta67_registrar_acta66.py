# -*- coding: utf-8 -*-
"""vuelta67_registrar_acta66.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DE LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 66.

NO REESCRIBE NI UNA LINEA DE LAS SECCIONES DE ARRIBA: abre el fichero en modo
adosar y escribe detras. Es la via que esta pagina ya uso SIETE veces (acta 52
en la linea 1250, acta 57 sobre el acto 25 en la 2475, acta 61 en la 2689, acta
62 en la 2933, acta 63 en la 3307, acta 64 en la 3613 y acta 65 en la 3962).

LA GUARDA DE CITAS, heredada del registrador de la vuelta 66: ANTES de escribir,
cada cita de linea se coteja contra su fichero imprimiendo la linea citada; si
una sola no calza con la aguja que la tabla dice de ella, el instrumento cae en
ROJO y NO escribe nada. Aqui se cotejan citas de DOS ficheros, el acta y la
propia pagina de fusiones.

LA GUARDA DE IDEMPOTENCIA: si la seccion ya esta en la pagina, no se escribe
nada. Una pagina con la adjudicacion duplicada no falla, dice que si.

Uso:
  python scripts/loop/vuelta67_registrar_acta66.py [--simular]
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:66 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 66 DEL AUDITOR" corte=2026-08-25 motivo="el titulo nombra el ACTA que este registro transcribe, que es de la vuelta 66; el fichero es de la vuelta 67 y por eso el numero no calza con su propia vuelta a proposito"
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
    (17368, "ACTA DE LA VUELTA 66 DEL AUDITOR"),
    (17396, "VERIFICACION POR CORRIDA PROPIA"),
    (17496, "RELECTURA CIEGA"),
    (17544, "CAIDAS DE ESTA TANDA"),
    (17547, "EJECUTOR: CERO de clase, CERO de cifra publicada y CERO de reporte"),
    (17555, "AUDITOR, UNA CAIDA DE PROCEDIMIENTO DEL ROL"),
    (17568, "ADJUDICACION DE LOS DOCE DISCUTIBLES"),
    (17570, "D1, DECLARAR EL ACTO 5 POR LA PREGUNTA DE P.5"),
    (17579, "D2, FUNDIR EL ACTO 9 CON EL SUPERVIVIENTE MAS CORTO"),
    (17584, "D3, LOS PASOS 7 A 10 DE cuatro_categorias"),
    (17590, "D4, LA LINEA BASE DEL CENSO DE 2 A 4 CON OP-U-02 DE DUENA"),
    (17592, "D5, CERO INCISO EN EL ACTO 7 POR LA PUNTUACION"),
    (17596, "D6, SEIS APPEND DE LA SECUENCIA UNIVERSAL AL DMAIC"),
    (17602, "D7, VEINTIUN APPEND EN EL ACTO 9"),
    (17604, "D8, LAS SIETE PERDIDAS CON ATENUANTE DECLARADO"),
    (17607, "D9, LOS DOS CAMBIOS DEL CUADRO DE VARAS"),
    (17615, "D10, CORREGIR EL CASO POSITIVO DEL CONTRATO DE PERDIDAS SIN ENCARGO"),
    (17621, "D11, LA CITA 3959 POR 3962 CORREGIDA CON GREP"),
    (17626, "D12, EL FICHERO DE APERTURA CON TITULO SIN ETIQUETA"),
    (17632, "LOS PENDIENTES DE DOCTRINA, ADJUDICADOS O NOMBRADOS"),
    (17634, "QUE HACE UN ACTO CUANDO P.5 CONTESTA DOS FAMILIAS"),
    (17637, "PRIMERA: P.5 con su correccion de alcance"),
    (17641, "SEGUNDA: P.12"),
    (17645, "TERCERA: el carril del DECLARADO Y NO FUNDIDO CON MOTIVO"),
    (17648, "CUARTA: las"),
    (17653, "NO ES PARADA"),
    (17657, "UNA COLISION QUE FABRICA UNA FUSION DE OP-U-02, QUIEN LA HEREDA"),
    (17658, "LA DUENA ES QUIEN LA FABRICA"),
    (17660, "la colision nace de"),
    (17663, "LA LINEA BASE"),
    (17665, "Que hace la campana con"),
    (17669, "EL SUBCONJUNTO CERRADO DE UN ACTO CON PUENTE"),
    (17674, "LA MARCA PARA YA LO DICE EL APPEND DE UN HERMANO"),
    (17679, "EL INCISO DE CONDICIONES (heredado)"),
    (17681, "EL ESQUEMA DE OPERACIONES.jsonl (heredado)"),
    (17685, "METRICA DE CREDITO ACUMULADA"),
    (17712, "Rachas: REPORTE EN CERO"),
    (17715, "CONDICIONES DE PARADA"),
    (17731, "CIERRE DE LA FASE 03"),
]
CITAS_PAGINA = [
    (62, "EL ORDEN DE ESTA FASE"),
    (1250, "LAS TRES ADJUDICACIONES DEL ACTA DE LA VUELTA 52"),
    (1377, "EL CARRIL GENERAL DE COLISIONES"),
    (2475, "LA ADJUDICACION DEL ACTA 57 SOBRE EL **ACTO 25**"),
    (2689, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 61"),
    (2933, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 62"),
    (3307, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 63"),
    (3613, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 64"),
    (3653, "EL CARRIL DE LAS DOS COLISIONES DE CLASE VIGENTES"),
    (3732, "EL REGISTRO DEL LOTE A"),
    (3744, "EL ACTO 1: `DECLARADO Y NO FUNDIDO` POR `P.10`"),
    (3962, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 65"),
    (4023, "CON LA GUARDA `1B` COMO MOTIVO SELLADO"),
    (4055, "LOS PENDIENTES 2 Y 4, NOMBRADOS CON SU DESTINO"),
    (4080, "EL REGISTRO DEL LOTE B"),
    (4365, "EL `ACTO 5`: `DECLARADO Y NO FUNDIDO` POR `P.5`"),
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
from _v67_texto_acta66 import TEXTO  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 66 AL FINAL DE 03_FUSIONES.md")
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
    if "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 66" in crudo:
        print()
        print("YA ADOSADA: la seccion del acta 66 ya esta en la pagina. No se escribe nada.")
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
