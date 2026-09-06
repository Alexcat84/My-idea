# -*- coding: utf-8 -*-
r"""guarda_de_entrada_a_la_nomina.py . LA GUARDA QUE CAE EN ROJO SI UN ARNES CON
SUJETO VIVO SE CUELA HACIA LA NOMINA DE LA BATERIA SIN DECLARARSE.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como `aislador_de_ciega.py`,
`apertura_del_auditor.py` y `cotejo_de_ciega.py`: esta guarda vale en TODA vuelta
y NO SE CLONA.

Y VIVE EN SU PROPIO FICHERO A PROPOSITO, NO DENTRO DE
`verificar_mutaciones_viejas.py`. **La razon esta medida y no supuesta: 42
entradas de la nomina nombran ese fichero**, y la `4.7` del acta 192 acaba de
adjudicar que mover un fichero que la nomina nombra **antes** de una corrida de
bateria pone en riesgo la corrida por algo que no es un fallo. Si eso vale para
`tallar_cabecera_reporte.py` con CUATRO entradas, vale mas con CUARENTA Y DOS.
**Aqui se importa lo de alla y no se toca ni un byte de alla.**

--- DE DONDE SALE, Y CUAL ES EL AGUJERO QUE TAPA ---

Es la pieza `e` de la TAREA 3 de la vuelta 192, sobre el hallazgo `5.1` del acta
192. La bateria compara salidas selladas byte a byte, y **una salida que no
reproduce por sujeto vivo convierte una corrida legitima en un rojo que nadie
sabra leer**. Hasta hoy habia dos guardas y ninguna hacia esta pregunta:

  . `guarda_del_sujeto_congelado_separada()` mira **la nomina de HOY**, o sea los
    que YA entraron. Cuando muerde, ya es tarde.
  . `arneses_que_faltan()` mira **quien va a entrar**, pero **no mira su
    anclaje**: le da igual que el que reclama tenga el sujeto vivo.

**LA PREGUNTA QUE NADIE HACIA ES EL CRUCE DE LAS DOS: de los que el censo
RECLAMA, cual tiene el sujeto vivo.** Eso es lo que esta guarda computa, y por
eso cae ANTES y no DENTRO de la bateria.

--- LO QUE ES ROJO Y LO QUE ES DEUDA, SEPARADO Y NO MEZCLADO ---

  ROJO   . un arnes que el censo RECLAMA y que sale `SUJETO VIVO`. La `4.4` del
           acta 191 adjudico que `SUJETO VIVO` es **FALLO y no deuda**, y este es
           el unico caso que hace caer la guarda.
  DEUDA  . un arnes reclamado que sale `NO DECIDIBLE` **sin motivo escrito**. Se
           NOMBRA y se publica, **y NO hace caer la guarda**, porque la `4.4` y
           la `4.6` del acta 190 lo dejaron como deuda y no como fallo. Callarlo
           seria lo contrario de declararlo.
  LIMPIO . `CONGELADO`, `CASO DECLARADO`, y `NO DECIDIBLE` CON motivo escrito.

--- LO QUE ESTA GUARDA NO PUEDE HACER, DICHO EN VEZ DE CALLARLO ---

**No decide si el sujeto esta vivo de verdad: decide si el TEXTO lo parece.** Las
huellas son literales, y un literal puede aparecer dentro de una cadena que el
arnes nunca abre. Eso NO es hipotetico: la vuelta 192 midio que
`vuelta191_tarea3_arreglar_lineas.py` salia `SUJETO VIVO` por seis apariciones de
`REPORTE.md` **dentro de patrones de parcheo**, y ese fichero **no abre
`REPORTE.md` en ninguna linea**. Por eso el remedio de un falso positivo es
DECLARARLO en el propio arnes, con su evidencia, y no ensanchar la huella.

**Y no mira la nomina para cambiarla.** Esta guarda LEE. No poda, no adelanta y
no anade: la opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue rechazada.

USO:
  python scripts/loop/guarda_de_entrada_a_la_nomina.py
  python scripts/loop/guarda_de_entrada_a_la_nomina.py --mutacion
"""
import argparse
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as VMV   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

VEREDICTO_FALLO = "SUJETO VIVO"
VEREDICTO_DEUDA = "NO DECIDIBLE"


def reclamados_por_el_censo(nomina=None, directorio=None, vara=None):
    """LOS ARNESES QUE EL CENSO RECLAMA PARA LA NOMINA. Devuelve la lista de
    nombres. Semi-pura: delega entera en `arneses_que_faltan()` de
    `verificar_mutaciones_viejas.py`, **importada y no copiada**, para que la
    regla de entrada siga teniendo UNA sola fuente de verdad."""
    _ultima, faltan = VMV.arneses_que_faltan(nomina, directorio, vara)
    return list(faltan)


def veredicto_de_entrada(nomina=None, directorio=None, vara=None,
                         declarados=None, marcas=None, ventana=None):
    """EL VEREDICTO DE LA PUERTA. Devuelve un dict con las cuatro listas y el
    booleano `rojo`. Semi-pura: lo unico que toca disco es leer los ficheros de
    los arneses, y los cuatro parametros van por parametro para que el caso
    positivo por mutacion la corra sobre un directorio y una nomina fabricados.

    `rojo` es True **si y solo si** algun reclamado sale `SUJETO VIVO`. La deuda
    se publica y no hace caer: la separacion es de la `4.4` y la `4.6` del acta
    190 y aqui no se re decide."""
    dec = VMV.CASOS_DECLARADOS if declarados is None else declarados
    salida = {"reclamados": [], "fallo": [], "deuda": [], "limpios": []}
    for nombre in reclamados_por_el_censo(nomina, directorio, vara):
        texto = VMV.texto_del_arnes(nombre, directorio)
        veredicto, congela, vive = VMV.anclaje_de(texto, declarado=(nombre in dec))
        tiene, evidencia = VMV.motivo_del_sujeto_vivo(texto, marcas, ventana)
        fila = (nombre, veredicto, tiene, vive, congela, evidencia)
        salida["reclamados"].append(fila)
        if veredicto == VEREDICTO_FALLO:
            salida["fallo"].append(fila)
        elif veredicto == VEREDICTO_DEUDA and not tiene:
            salida["deuda"].append(fila)
        else:
            salida["limpios"].append(fila)
    salida["rojo"] = bool(salida["fallo"])
    return salida


def informe(v):
    """LAS LINEAS DEL INFORME. PURA sobre el dict que devuelve
    `veredicto_de_entrada()`."""
    L = []
    w = L.append
    w("LOS QUE EL CENSO RECLAMA PARA LA NOMINA: %d" % len(v["reclamados"]))
    for nombre, veredicto, tiene, vive, congela, _ev in v["reclamados"]:
        w("   %-46s %-14s motivo escrito: %-3s"
          % (nombre, veredicto, "SI" if tiene else "no"))
        w("      huellas de vivo:      %s" % (", ".join(vive) or "(ninguna)"))
        w("      huellas de congelado: %s" % (", ".join(congela) or "(ninguna)"))
    w("")
    w("FALLO (SUJETO VIVO y reclamado, y esto SI hace caer): %d" % len(v["fallo"]))
    for f in v["fallo"]:
        w("   %s" % f[0])
    w("DEUDA (NO DECIDIBLE sin motivo escrito, y esto NO hace caer): %d"
      % len(v["deuda"]))
    for f in v["deuda"]:
        w("   %s   huellas de vivo: %s" % (f[0], ", ".join(f[3]) or "(ninguna)"))
    w("LIMPIOS (congelado, caso declarado, o no decidible CON motivo): %d"
      % len(v["limpios"]))
    for f in v["limpios"]:
        w("   %s   %s" % (f[0], f[1]))
    w("")
    w("VEREDICTO DE LA PUERTA: %s" % ("ROJO" if v["rojo"] else "VERDE"))
    if not v["rojo"] and v["deuda"]:
        w("   VERDE CON DEUDA DECLARADA, que no es lo mismo que verde a secas: %d"
          % len(v["deuda"]))
        w("   arnes(es) reclamado(s) nombran un sujeto vivo y no escriben por que.")
    return L


# ---------------------------------------------------------------- LA MUTACION
def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    w("   %-62s %s" % (nombre, "VERDE" if ok else "ROJO"))
    if not ok:
        w("      esperado: %r" % (esperado,))
        w("      obtenido: %r" % (obtenido,))
    return ok


def _fabricar(directorio, ficheros):
    for nombre, cuerpo in ficheros.items():
        io.open(os.path.join(directorio, nombre), "w", encoding="utf-8",
                newline=NL).write(cuerpo)


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION. **CAE si un arnes con sujeto vivo se cuela
    hacia la nomina sin declararse.** No toca el repo: fabrica un directorio
    temporal con sus arneses, y lo retira (`P.16`, quien fabrica limpia)."""
    import shutil
    import tempfile
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DE LA GUARDA DE ENTRADA A LA NOMINA")
    w("=" * 78)
    w("")
    w("LO QUE SE PRUEBA, Y POR QUE PUEDE CAER: los arneses se FABRICAN en un")
    w("directorio temporal con su anclaje sabido por construccion, y la nomina se")
    w("le pasa por parametro. El valor esperado de cada caso sale de como se")
    w("fabrico el fichero, no de una constante igual a la obtenida.")
    w("")

    tmp = tempfile.mkdtemp(prefix="guarda_entrada_")
    try:
        VIVO = ("vuelta199_tarea1_mutacion_vivo.py",
                '# -*- coding: utf-8 -*-\n"""un arnes cualquiera."""\n'
                'import io\nt = io.open("docs/loop/REPORTE.md").read()\n')
        VIVO_DECLARADO = ("vuelta199_tarea2_mutacion_declarado.py",
                          '# -*- coding: utf-8 -*-\n"""un arnes cualquiera."""\n'
                          '# SUJETO CONGELADO: lo que sigue es un patron de texto y no una\n'
                          '# apertura de fichero.\n'
                          'PATRON = "docs/loop/REPORTE.md"\n')
        DEUDA = ("vuelta199_tarea3_mutacion_deuda.py",
                 '# -*- coding: utf-8 -*-\n"""un arnes cualquiera."""\n'
                 'import tempfile\nd = tempfile.mkdtemp()\n'
                 'P = "docs/loop/REPORTE.md"\n')
        DEUDA_CON_MOTIVO = ("vuelta199_tarea4_mutacion_motivo.py",
                            '# -*- coding: utf-8 -*-\n"""un arnes cualquiera."""\n'
                            'import tempfile\nd = tempfile.mkdtemp()\n'
                            '# NO SE TOCA: es solo el nombre del fichero, no se abre.\n'
                            'P = "docs/loop/REPORTE.md"\n')
        _fabricar(tmp, dict([VIVO, VIVO_DECLARADO, DEUDA, DEUDA_CON_MOTIVO]))
        vacia = []

        w("A) EL CASO QUE TIENE QUE CAER: UN ARNES CON SUJETO VIVO, RECLAMADO POR")
        w("   EL CENSO Y SIN DECLARARSE")
        v = veredicto_de_entrada(nomina=vacia, directorio=tmp, vara=148)
        nombres = sorted(f[0] for f in v["reclamados"])
        ok &= _caso(w, "el censo reclama los cuatro fabricados", len(nombres), 4)
        ok &= _caso(w, "LA GUARDA CAE EN ROJO", v["rojo"], True)
        ok &= _caso(w, "y el que la tumba es el de sujeto vivo",
                    sorted(f[0] for f in v["fallo"]), [VIVO[0]])
        w("")

        w("B) LA MUTACION QUE LA LEVANTA: EL MISMO ARNES, DECLARADO EN SU PROPIO")
        w("   FICHERO POR EL CARRIL DE LA CASA. La guarda TIENE que dejar de caer.")
        os.remove(os.path.join(tmp, VIVO[0]))
        v2 = veredicto_de_entrada(nomina=vacia, directorio=tmp, vara=148)
        ok &= _caso(w, "sin el de sujeto vivo, la guarda NO cae", v2["rojo"], False)
        ok &= _caso(w, "el declarado en su fichero sale limpio",
                    VIVO_DECLARADO[0] in [f[0] for f in v2["limpios"]], True)
        w("")

        w("C) LA DEUDA SE PUBLICA Y NO HACE CAER, QUE ES LA SEPARACION DE LA 4.4")
        w("   Y LA 4.6 DEL ACTA 190 Y AQUI NO SE RE DECIDE")
        ok &= _caso(w, "el NO DECIDIBLE sin motivo entra en DEUDA",
                    sorted(f[0] for f in v2["deuda"]), [DEUDA[0]])
        ok &= _caso(w, "y la deuda NO pone la guarda en rojo", v2["rojo"], False)
        ok &= _caso(w, "el NO DECIDIBLE CON motivo escrito sale limpio",
                    DEUDA_CON_MOTIVO[0] in [f[0] for f in v2["limpios"]], True)
        w("")

        w("D) LA MUTACION QUE PRUEBA QUE MIRA AL QUE ENTRA Y NO AL QUE YA ESTA:")
        w("   SI EL DE SUJETO VIVO YA ESTUVIERA EN LA NOMINA, EL CENSO NO LO")
        w("   RECLAMA Y ESTA GUARDA NO LO VE. Es su ceguera, y va escrita.")
        _fabricar(tmp, dict([VIVO]))
        v3 = veredicto_de_entrada(nomina=[(VIVO[0], True)], directorio=tmp, vara=148)
        ok &= _caso(w, "ya en la nomina: el censo NO lo reclama",
                    VIVO[0] in [f[0] for f in v3["reclamados"]], False)
        ok &= _caso(w, "y por eso esta guarda NO cae por el", v3["rojo"], False)
        w("   (para ese caso ya existe `guarda_del_sujeto_congelado_separada()`,")
        w("    que mira la nomina de hoy. Las dos hacen falta y ninguna sobra)")
        w("")

        w("E) LA MUTACION DE LA VARA: SUBIENDOLA POR ENCIMA DE LA VUELTA")
        w("   FABRICADA, EL CENSO DEJA DE RECLAMAR Y LA GUARDA DEJA DE VER")
        v4 = veredicto_de_entrada(nomina=vacia, directorio=tmp, vara=999)
        ok &= _caso(w, "con la vara en 999 no se reclama a nadie",
                    len(v4["reclamados"]), 0)
        ok &= _caso(w, "y la guarda sale VERDE por vacio, no por limpio",
                    (v4["rojo"], len(v4["fallo"])), (False, 0))
        w("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        w("F) EL DIRECTORIO FABRICADO SE RETIRA (P.16, quien fabrica limpia)")
        w("   %s existe todavia: %s" % (tmp, os.path.exists(tmp)))
        ok &= _caso(w, "el temporal quedo retirado", os.path.exists(tmp), False)
        w("")

    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutacion", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if a.mutacion:
        return prueba_de_mutacion()
    print("=" * 78)
    print("GUARDA DE ENTRADA A LA NOMINA. Corre ANTES de la bateria, no dentro.")
    print("=" * 78)
    v = veredicto_de_entrada()
    for l in informe(v):
        print(l)
    return 1 if v["rojo"] else 0


if __name__ == "__main__":
    sys.exit(main())
