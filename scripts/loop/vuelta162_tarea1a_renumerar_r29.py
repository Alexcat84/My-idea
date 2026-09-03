# -*- coding: utf-8 -*-
r"""vuelta162_tarea1a_renumerar_r29.py . TAREA 1.a de la vuelta 162.

LA ENTRADA QUE LA VUELTA 161 ESCRIBIO COMO `R.29` PASA A `R.30` POR CORRECCION
DECLARADA, SIN BORRAR UNA SOLA LINEA: el titulo viejo queda TACHADO Y LEGIBLE
con su motivo delante (acta 161, seccion 5.1 y adjudicacion 6.8).

NINGUNA CELDA SE TECLEA:
  - el numero nuevo lo da `scripts/loop/serie_de_registros.py`, recomputando la
    serie de LOS DOS ficheros (`siguiente_libre`), no la cabeza de este script;
  - la sede y la linea de la `R.29` legitima se LEEN hoy de la propia serie;
  - la linea de la remision de la vuelta 150 se LOCALIZA hoy por su texto en
    `docs/PENDIENTES.md`, y si no se halla, este script PARA sin escribir.

ES IDEMPOTENTE Y LO COMPRUEBA MIRANDO LOS DOS FICHEROS, que es justo la
comprobacion que la vuelta 161 no hizo.

USO:  python scripts/loop/vuelta162_tarea1a_renumerar_r29.py
"""
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402

RAIZ = SERIE.RAIZ
PENDIENTES = os.path.join(RAIZ, "docs", "PENDIENTES.md")

TITULO_VIEJO_1 = "## R.29. Registro de las caidas de clase de las dos tandas y de la parada de la"
TITULO_VIEJO_2 = "vuelta 160, con su resolucion (escrito en la vuelta 161, TAREA 1.0)"
ANCLA_REMISION = "REMISION (vuelta 150, TAREA 1.a): `R.29`, el registro del acta de la vuelta"
MARCA_YA_HECHO = "## R.30. Registro de las caidas de clase de las dos tandas"


def main():
    print("=" * 78)
    print("VUELTA 162, TAREA 1.a: LA ENTRADA DE LA VUELTA 161 PASA DE R.29 A R.30")
    print("=" * 78)
    print("")

    pend = io.open(PENDIENTES, encoding="utf-8").read()
    if MARCA_YA_HECHO in pend:
        print("YA ESTABA: la entrada ya se llama R.30. No se toca.")
        print("CIFRA renumeradas: 0")
        return 0

    print("A) LA SERIE, RECOMPUTADA DE SUS DOS SEDES ANTES DE ESCRIBIR NADA")
    halladas = SERIE.entradas()
    cols = SERIE.colisiones(halladas)
    print("   CIFRA entradas: %d" % len(halladas))
    print("   CIFRA colisiones: %d" % len(cols))
    if 29 not in cols:
        print("   PARADA: la serie ya no trae la colision de R.29 que esta correccion")
        print("   viene a resolver. No se escribe nada.")
        return 1
    sitios = cols[29]
    legitima = [(rel, ln, t) for rel, ln, t in sitios if "CORRECCIONES_A_APLICAR" in rel]
    intrusa = [(rel, ln, t) for rel, ln, t in sitios if "PENDIENTES" in rel]
    if len(legitima) != 1 or len(intrusa) != 1:
        print("   PARADA: la colision de R.29 no tiene la forma esperada (una en cada sede).")
        return 1
    rel_leg, ln_leg, tit_leg = legitima[0]
    rel_int, ln_int, tit_int = intrusa[0]
    print("   R.29 LEGITIMA, asignada desde la vuelta 150: %s:%d" % (rel_leg, ln_leg))
    print("      %s" % tit_leg[:110])
    print("   R.29 ESCRITA POR LA VUELTA 161, la que se renumera: %s:%d" % (rel_int, ln_int))
    print("      %s" % tit_int[:110])
    nuevo = SERIE.siguiente_libre(halladas)
    print("   SIGUIENTE LIBRE, computado y NO tecleado: R.%d" % nuevo)
    if nuevo != 30:
        print("   PARADA: el siguiente libre no es 30 y este script escribe R.30.")
        return 1
    print("")

    print("B) LA PRUEBA QUE YA ESTABA EN EL MISMO FICHERO, LOCALIZADA HOY POR SU TEXTO")
    lineas = pend.split("\n")
    remision = [i for i, l in enumerate(lineas, 1) if ANCLA_REMISION in l]
    if len(remision) != 1:
        print("   PARADA: la remision de la vuelta 150 aparece %d veces." % len(remision))
        return 1
    ln_rem = remision[0]
    print("   docs/PENDIENTES.md:%d" % ln_rem)
    print("      %s" % lineas[ln_rem - 1].strip()[:110])
    print("   distancia entre la remision y la entrada mal numerada: %d lineas"
          % (ln_int - ln_rem))
    print("")

    if TITULO_VIEJO_1 not in pend or TITULO_VIEJO_2 not in pend:
        print("   PARADA: el titulo viejo no esta literal en el fichero.")
        return 1

    nuevo_bloque = (
        "## R.30. Registro de las caidas de clase de las dos tandas y de la parada de la\n"
        "vuelta 160, con su resolucion (escrito en la vuelta 161, TAREA 1.0; RENUMERADA de\n"
        "`R.29` a `R.30` en la vuelta 162, TAREA 1.a)\n"
        "\n"
        "**CORRECCION DECLARADA, Y NO SE BORRA UNA SOLA LINEA** (vuelta 162, TAREA 1.a;\n"
        "acta del auditor de la vuelta 161, seccion 5.1 y adjudicacion 6.8).\n"
        "\n"
        "**EL MOTIVO, MEDIDO HOY Y NO ALEGADO.** La `R.29` **ya estaba asignada** desde la\n"
        "vuelta 150 y vive en `%s:%d`\n"
        "(*\"%s\"*). La entrada de la vuelta 161 se numero `R.29` porque su instrumento\n"
        "llevaba el ultimo numero **TECLEADO** (*\"con la ultima escrita siendo `R.28`\"*) y\n"
        "su idempotencia miraba **un solo fichero**. **La serie `R.N` es GLOBAL a los dos**,\n"
        "y lo prueba la propia remision de la vuelta 150, que estaba en esta misma pagina,\n"
        "en `docs/PENDIENTES.md:%d`, a **%d lineas** de la entrada mal numerada: *\"%s\"*.\n"
        "**Corte de esta medicion: 3 sep 2026**, instrumento\n"
        "`scripts/loop/serie_de_registros.py`, salida\n"
        "`docs/loop/SALIDA_V162_T1A_SERIE_ANTES.txt`.\n"
        "\n"
        "**EL TITULO VIEJO, TACHADO Y LEGIBLE:**\n"
        "\n"
        "~~## R.29. Registro de las caidas de clase de las dos tandas y de la parada de la\n"
        "vuelta 160, con su resolucion (escrito en la vuelta 161, TAREA 1.0)~~\n"
        "\n"
        "**LO QUE NO CAMBIA:** el cuerpo entero de la entrada, sus cifras y su corte siguen\n"
        "tal cual se escribieron en la vuelta 161. Lo unico que se corrige es el numero.\n"
        % (rel_leg, ln_leg, tit_leg.lstrip("# ").strip(), ln_rem, ln_int - ln_rem,
           lineas[ln_rem - 1].strip())
    )

    viejo_bloque = TITULO_VIEJO_1 + "\n" + TITULO_VIEJO_2 + "\n"
    if pend.count(viejo_bloque) != 1:
        print("   PARADA: el bloque del titulo viejo aparece %d veces."
              % pend.count(viejo_bloque))
        return 1
    pend = pend.replace(viejo_bloque, nuevo_bloque, 1)
    io.open(PENDIENTES, "w", encoding="utf-8", newline="\n").write(pend)

    print("C) LA ESCRITURA")
    r = subprocess.run(["git", "diff", "--numstat", "--", "docs/PENDIENTES.md"],
                       cwd=RAIZ, capture_output=True, text=True)
    print("   git diff --numstat: %s" % r.stdout.strip())
    partes = r.stdout.strip().split("\t")
    anadidas, borradas = int(partes[0]), int(partes[1])
    print("   CIFRA lineas anadidas: %d" % anadidas)
    print("   CIFRA lineas borradas: %d" % borradas)
    if borradas != 2:
        print("   ROJO: se esperaban EXACTAMENTE 2 lineas borradas (las dos del titulo")
        print("   viejo, que vuelven tachadas justo debajo).")
        return 1
    print("   Las 2 borradas son las 2 del titulo viejo, y vuelven TACHADAS Y LEGIBLES")
    print("   dentro del bloque nuevo. Se comprueba:")
    texto_nuevo = io.open(PENDIENTES, encoding="utf-8").read()
    tachado_ok = ("~~" + TITULO_VIEJO_1) in texto_nuevo and (TITULO_VIEJO_2 + "~~") in texto_nuevo
    print("      titulo viejo presente y tachado: %s" % ("SI" if tachado_ok else "NO"))
    if not tachado_ok:
        print("   ROJO: el titulo viejo no quedo legible.")
        return 1
    print("")

    print("D) LA SERIE, RECOMPUTADA DESPUES")
    despues = SERIE.entradas()
    cols2 = SERIE.colisiones(despues)
    print("   CIFRA entradas: %d" % len(despues))
    print("   CIFRA colisiones: %d" % len(cols2))
    print("   CIFRA huecos: %d" % len(SERIE.huecos(despues)))
    print("   SIGUIENTE LIBRE: R.%d" % SERIE.siguiente_libre(despues))
    if cols2:
        print("   ROJO: sigue habiendo colisiones.")
        return 1
    print("")
    print("VERDE: la entrada de la vuelta 161 se llama R.30, la R.29 legitima se queda")
    print("donde estaba, la serie no tiene colisiones y el titulo viejo sigue legible.")
    print("CIFRA renumeradas: 1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
