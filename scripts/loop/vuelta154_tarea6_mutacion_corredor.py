# -*- coding: utf-8 -*-
"""vuelta154_tarea6_mutacion_corredor.py . TAREA 6 DE LA VUELTA 154.

EL CASO POR MUTACION DEL CORREDOR AMPLIADO, Y MUERDE POR LOS DOS LADOS.

LO QUE EL ENCARGO PIDE, LITERAL: "Con caso por mutacion por los dos lados: con
solo el commit del fundador en el corredor, VERDE; con un commit del ejecutor
dentro, ROJO nombrandolo."

SOBRE VARIABLE COMPUTADA (EJECUTOR.md 1, y la caida 2 de la vuelta 89): el
corredor NO se teclea. Se lee de git el CORREDOR REAL de la vuelta 152 (del acta
151 `bf514465` al commit de nacimiento de su bloque de apertura), que trae
exactamente los dos commits que el caso necesita:

  d9fa886b  "Decision del fundador: la lista blanca es un registro de citas..."
  6f419952  "VUELTA 152, TAREA 1: EL RELOJ DE GIT CONGELADO..."

y los dos tocan rutas que NO son papel de parada, o sea que la guarda vieja
falla por los dos por igual. Los hashes de arriba se imprimen para el lector,
pero el arnes los OBTIENE de git y los localiza por su asunto, no por un
literal comparandose consigo mismo. El conjunto de admitidos se computa con
`git rev-parse` sobre el commit del fundador leido de ese mismo corredor.

LOS CUATRO CASOS:

  (A) corredor real entero, admitidos VACIO
      -> 2 intrusos. Es el estado ANTES de la adjudicacion 6.7, y reproduce el
         rojo doble que la vuelta 152 declaro.
  (B) SOLO el commit del fundador, admitido por hash citado
      -> 0 intrusos, 1 admitido nombrado aparte. VERDE.
  (C) SOLO el commit del fundador, admitidos VACIO
      -> 1 intruso. Prueba que el verde del caso B lo produce LA ADMISION y no
         una laxitud nueva: sin el hash citado, el mismo commit sigue en rojo.
  (D) los DOS, con el del fundador admitido
      -> 1 intruso, y es EL DEL EJECUTOR, nombrado. ROJO. Es la mitad que el
         encargo manda dejar intacta.

--- LO QUE MIDO Y NO ME GUSTA, Y LO DIGO EN VEZ DE CALLARLO ---

LA REGLA, TAL COMO EL ACTA LA ESCRIBE, NO HABRIA SALVADO A LA VUELTA 152. La
adjudicacion 6.7 admite "el commit de la decision del fundador QUE
`PROMPT_SIGUIENTE.md` CITA POR SU HASH". Fui a mirar el
`docs/loop/PROMPT_SIGUIENTE.md` que la vuelta 152 tenia delante
(`git show 6f419952:docs/loop/PROMPT_SIGUIENTE.md`) y el UNICO hash que cita es
`36b57d78`, el mergebase con `main`: NO cita `d9fa886b`. Con la regla aplicada
al pie de la letra, la guarda de la vuelta 152 habria seguido en rojo por el
commit del fundador.

NO CAMBIO LA REGLA POR ESO, y el motivo es que la alternativa es peor: admitir
por asunto ("Decision del fundador") o por autor seria una puerta que cualquiera
puede abrir escribiendo un asunto, y la propia adjudicacion dice "por HASH
CITADO EN EL ENCARGO". La regla queda como esta escrita, es PROSPECTIVA, y lo
que hace falta para que sirva es que el encargo CITE el hash de la decision
cuando la haya. Va al reporte como discutible marcado.

USO:  python scripts/loop/vuelta154_tarea6_mutacion_corredor.py
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

from verificar_apertura_sellada import (  # noqa: E402
    corredor_desde_git, intrusos_del_corredor, hashes_citados_por_el_encargo)

ACTA_151 = "bf514465"
FICHERO_DE_APERTURA_152 = "docs/loop/SALIDA_V152_GATE0_CMD1_APERTURA.txt"


def main():
    print("=" * 96)
    print("VUELTA 154, TAREA 6: EL CASO POR MUTACION DEL CORREDOR, POR LOS DOS LADOS")
    print("=" * 96)

    fallos = []
    nac = subprocess.run(["git", "log", "--diff-filter=A", "--format=%H", "--",
                          FICHERO_DE_APERTURA_152], cwd=RAIZ, capture_output=True)
    nacido_en = nac.stdout.decode().split()[0]
    acta = subprocess.run(["git", "rev-parse", ACTA_151], cwd=RAIZ,
                          capture_output=True).stdout.decode().strip()
    corredor = corredor_desde_git(acta, nacido_en, fallos)
    assert corredor and not fallos, "no se pudo leer el corredor real: %s" % fallos

    print("EL CORREDOR REAL, LEIDO DE GIT (acta %s .. apertura %s):"
          % (acta[:8], nacido_en[:8]))
    for h, asunto, rutas in corredor:
        print("  %s '%s' -- %d ruta(s)" % (h[:8], asunto[:66], len(rutas)))
    print("")

    del_fundador = [c for c in corredor if c[1].lower().startswith("decision del fundador")]
    del_ejecutor = [c for c in corredor if c not in del_fundador]
    assert len(del_fundador) == 1, "el corredor real no trae UN commit de decision del fundador"
    assert del_ejecutor, "el corredor real no trae ningun commit del ejecutor"
    h_fundador = del_fundador[0][0]
    admitidos = {subprocess.run(["git", "rev-parse", "--verify", "%s^{commit}" % h_fundador],
                                cwd=RAIZ, capture_output=True).stdout.decode().strip()}
    print("COMPUTADO, no tecleado: el commit de decision del fundador dentro del corredor es")
    print("%s, y es el que se pasa como admitido. Los del ejecutor son %d: %s."
          % (h_fundador[:8], len(del_ejecutor), ", ".join(c[0][:8] for c in del_ejecutor)))
    print("")

    casos = [
        ("A", "corredor real entero, admitidos VACIO (el estado ANTES de la 6.7)",
         corredor, set(), 2, 0),
        ("B", "SOLO el del fundador, ADMITIDO por hash citado",
         del_fundador, admitidos, 0, 1),
        ("C", "SOLO el del fundador, admitidos VACIO (que el verde lo da la admision)",
         del_fundador, set(), 1, 0),
        # CORRECCION DECLARADA (vuelta 154, en la propia corrida): esta fila la
        # escribi esperando 1 intruso y 0 admitidos, y el arnes la tumbo. Tenia
        # razon el arnes: con LOS DOS commits dentro y el del fundador admitido,
        # lo correcto es 1 INTRUSO (el del ejecutor) Y 1 ADMITIDO (el del
        # fundador), porque el admitido se sigue NOMBRANDO APARTE aunque la
        # guarda caiga por otro. La expectativa estaba mal, no la guarda.
        ("D", "los DOS, con el del fundador admitido (la mitad que NO se afloja)",
         corredor, admitidos, 1, 1),
    ]

    print("| caso | que se prueba | intrusos esperados | intrusos medidos | admitidos medidos | veredicto | cuadra |")
    print("|---|---|---:|---:|---:|---|---|")
    filas = []
    for c, que, corr, adm, esp_i, esp_a in casos:
        intr, admv = intrusos_del_corredor(corr, adm)
        ok = (len(intr) == esp_i and len(admv) == esp_a)
        ver = "ROJO" if intr else "VERDE"
        filas.append((c, que, esp_i, intr, admv, ver, ok))
        print("| %s | %s | %d | %d | %d | %s | %s |"
              % (c, que, esp_i, len(intr), len(admv), ver, "SI" if ok else "NO"))
    print("")

    for c, que, esp_i, intr, admv, ver, ok in filas:
        print("CASO %s (%s): %s" % (c, que, ver))
        for h, asunto, ajenas in intr:
            print("   INTRUSO NOMBRADO: %s '%s' toca %d ruta(s) ajenas, la primera %s"
                  % (h[:8], asunto[:60], len(ajenas), ajenas[0]))
        for h, asunto, ajenas in admv:
            print("   ADMITIDO Y NOMBRADO APARTE: %s '%s' toca %d ruta(s) ajenas, la primera %s"
                  % (h[:8], asunto[:60], len(ajenas), ajenas[0]))
        print("")

    print("=" * 96)
    print("LO QUE LA REGLA NO SALVA, MEDIDO Y NO SUPUESTO")
    print("=" * 96)
    prompt_152 = subprocess.run(["git", "show", "6f419952:docs/loop/PROMPT_SIGUIENTE.md"],
                                cwd=RAIZ, capture_output=True).stdout.decode("utf-8", "replace")
    cita = h_fundador[:8] in prompt_152 or h_fundador in prompt_152
    print("El PROMPT_SIGUIENTE.md que la vuelta 152 tenia delante CITA el hash del commit")
    print("de la decision del fundador (%s): %s" % (h_fundador[:8], "SI" if cita else "NO"))
    print("Luego la regla del acta 153, 6.7, APLICADA AL PIE DE LA LETRA, no habria salvado")
    print("a la vuelta 152. Es PROSPECTIVA. No se afloja por eso: admitir por asunto o por")
    print("autor seria una puerta que abre cualquiera. Va al reporte como discutible.")
    print("")

    hoy, literales = hashes_citados_por_el_encargo()
    print("Y EL ENCARGO DE HOY: cita %d hash(es) que git resuelve (%s)."
          % (len(literales), ", ".join(literales) or "ninguno"))
    print("El corredor de ESTA vuelta esta VACIO (el bloque de apertura es hijo directo del")
    print("acta 153), asi que la admision no se usa hoy: se prueba, no se ejerce.")
    print("")

    print("CIFRA casos de mutacion del corredor corridos: %d comprobaciones" % len(filas))
    print("CIFRA casos que salen como se esperaba: %d comprobaciones"
          % sum(1 for f in filas if f[6]))
    for c, que, esp_i, intr, admv, ver, ok in filas:
        assert ok, "el caso %s no sale como se esperaba" % c
    print("")
    print("LOS CUATRO CASOS SALEN COMO SE ESPERABA, Y LA GUARDA MUERDE POR LOS DOS LADOS.")


main()
