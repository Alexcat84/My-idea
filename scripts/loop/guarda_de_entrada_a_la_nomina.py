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

--- LA HUELLA DE TEXTO NO PRUEBA REPRODUCCION (vuelta 193, TAREA 2.c) ---

**ESTA GUARDA DIO `CONGELADO` A DOS ARNESES CUYA SALIDA CAMBIABA EN CADA
CORRIDA, Y LA CAUSA ESTA MEDIDA.** `tempfile` y `mkdtemp` estan en
`HUELLAS_DE_CONGELADO`, asi que un arnes que fabrica un temporal para UN bloque
salia `CONGELADO` aunque OTRO de sus bloques leyera el arbol vivo. El acta 193 lo
midio en `docs/loop/_auditor_v193_reproducibilidad.txt`:
`vuelta191_tarea3_mutacion_lineas.py` pasaba de 5836 a 6559 bytes y
`vuelta191_tarea6_mutacion_bloque_tallado.py` de 4173 a 4998, **los dos con
veredicto `CONGELADO` de esta misma guarda**.

**LA UNICA VARA QUE PRUEBA REPRODUCCION ES CORRER EL ARNES DOS VECES Y COMPARAR
SUS BYTES.** Eso es lo que hace `reproduce_de_verdad()`, y por eso el veredicto
de esta puerta deja de ser una sola palabra: ahora son DOS COLUMNAS, la huella y
la reproduccion, **y la que manda es la segunda**.

**Y ES CARO, Y SE DICE EN VEZ DE ESCONDERLO.** Correr cada arnes reclamado DOS
veces cuesta tiempo real, y algunos escriben en `docs/loop/`. Por eso el carril
caro **no corre por defecto**: va en `--reproduccion`, y la corrida sin bandera
**declara en su propia salida que su columna de huella es UN INDICIO Y NO UN
VEREDICTO DE REPRODUCCION**. Un instrumento que no puede medir algo lo dice; no
publica un verde que no midio.

**LO QUE `--reproduccion` HACE CON LAS SALIDAS SELLADAS AJENAS:** las mide antes,
corre, mide, **y las RESTAURA con `git checkout --` remidiendolas** antes de
darlas por restauradas. Si alguna no se puede restaurar, **CAE EN ROJO** y lo
dice con su nombre.

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
  python scripts/loop/guarda_de_entrada_a_la_nomina.py --reproduccion
  python scripts/loop/guarda_de_entrada_a_la_nomina.py --mutacion
"""
import argparse
import hashlib
import io
import os
import re
import subprocess
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


def salida_sellada_de(nombre, directorio=None, base_salida=None):
    """LA SALIDA QUE UN ARNES SELLA, LEIDA DE SU PROPIO CODIGO. Devuelve la ruta
    relativa al repo, o cadena vacia si el arnes no nombra ninguna. PURA salvo
    por leer el fichero del arnes.

    LA VARA VA ESCRITA ANTES DE MEDIR, Y VA EN DOS PASADAS PORQUE LA PRIMERA SE
    MIDIO Y NO ALCANZA. **Pasada 1, LA QUE MANDA:** la asignacion de modulo
    `SALIDA = os.path.join(LOOP, "...")`, que es como los arneses de esta casa
    declaran su salida sellada; tiene que aparecer EXACTAMENTE UNA VEZ.
    **Pasada 2, solo si la primera no encuentra nada:** el literal
    `SALIDA_..._.txt` suelto, y entonces tiene que ser UNO SOLO en todo el
    fichero.

    **POR QUE DOS Y NO UNA, Y LA CAUSA ESTA MEDIDA (vuelta 193):** con la pasada
    2 sola, los CUATRO arneses que el censo reclama hoy salian `NO MEDIBLE`,
    porque sus docstrings NOMBRAN otras salidas de las que hablan. Una vara que
    declara no medible todo lo que hay no mide nada. **La pasada 1 mira LA
    MAQUINA, no la prosa**, que es la misma leccion que
    `sin_docstring_de_modulo()` ya habia aprendido en `verificar_mutaciones_viejas.py`.

    **Y SI NINGUNA DE LAS DOS RESUELVE, SE DEVUELVE CADENA VACIA** y quien llama
    lo declara NO MEDIBLE, en vez de elegir una a ojo."""
    texto = VMV.texto_del_arnes(nombre, directorio)
    por_constante = sorted(set(re.findall(
        r"^SALIDA\s*=\s*os\.path\.join\(LOOP,\s*[\"']([A-Za-z0-9_]+\.txt)[\"']\)",
        texto, re.M)))
    if len(por_constante) == 1:
        hallados = por_constante
    else:
        hallados = sorted(set(re.findall(r"SALIDA_[A-Z0-9_]+\.txt", texto)))
    if len(hallados) != 1:
        return ""
    if base_salida is not None:
        return os.path.join(base_salida, hallados[0])
    return "docs/loop/" + hallados[0]


def reproduce_de_verdad(nombre, directorio=None, base_salida=None,
                        restaurar=True):
    """CORRE UN ARNES DOS VECES Y COMPARA SU SALIDA SELLADA BYTE A BYTE.

    Devuelve un dict con `medible`, `reproduce`, `contra_sellada`, los bytes y
    los `sha256` LF de las tres mediciones, y `restaurada`.

    NO ES PURA Y NO PUEDE SERLO: es justo lo que la huella de texto no puede
    hacer. Toca disco, lanza procesos y RESTAURA lo que pisa con
    `git checkout --`, REMIDIENDO antes de darlo por restaurado. Si el arnes no
    nombra una sola salida, sale `medible: False` y NO se inventa un veredicto."""
    salida = {"medible": False, "reproduce": None, "contra_sellada": None,
              "ruta": "", "sellada": (None, ""), "c1": (None, ""),
              "c2": (None, ""), "restaurada": None, "exit1": None, "exit2": None}
    ruta_rel = salida_sellada_de(nombre, directorio, base_salida)
    if not ruta_rel:
        return salida
    salida["ruta"] = ruta_rel
    ruta_abs = (ruta_rel if base_salida is not None
                else os.path.join(RAIZ, ruta_rel.replace("/", os.sep)))
    arnes_abs = os.path.join(directorio or LOOP, nombre)
    if not os.path.isfile(arnes_abs) or not os.path.isfile(ruta_abs):
        return salida

    def medir():
        datos = io.open(ruta_abs, "rb").read().replace(b"\r\n", b"\n")
        return len(datos), hashlib.sha256(datos).hexdigest()[:16]

    def correr():
        env = dict(os.environ)
        env["PYTHONIOENCODING"] = "utf-8"
        r = subprocess.run([sys.executable, arnes_abs], cwd=RAIZ,
                           capture_output=True, env=env)
        return r.returncode

    salida["medible"] = True
    salida["sellada"] = medir()
    salida["exit1"] = correr()
    salida["c1"] = medir()
    salida["exit2"] = correr()
    salida["c2"] = medir()
    salida["reproduce"] = salida["c1"] == salida["c2"]
    salida["contra_sellada"] = salida["c1"] == salida["sellada"]
    if salida["contra_sellada"]:
        salida["restaurada"] = True
    elif restaurar:
        subprocess.run(["git", "checkout", "--", ruta_rel], cwd=RAIZ,
                       capture_output=True)
        salida["restaurada"] = medir() == salida["sellada"]
    else:
        salida["restaurada"] = None
    return salida


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
    w("")
    w("LO QUE ESTA COLUMNA NO ES, Y SE DICE EN VEZ DE CALLARLO (vuelta 193,")
    w("TAREA 2.c): EL VEREDICTO DE ARRIBA SALE DE UNA HUELLA DE TEXTO, Y UNA")
    w("HUELLA DE TEXTO NO PRUEBA REPRODUCCION. `tempfile` y `mkdtemp` cuentan")
    w("como huella de CONGELADO, y por eso esta misma guarda dio CONGELADO a dos")
    w("arneses cuya salida cambiaba en cada corrida (acta 193, hallazgo 5.3 y")
    w("adjudicacion 4.10, medido en docs/loop/_auditor_v193_reproducibilidad.txt).")
    w("LA UNICA VARA QUE LA PRUEBA es correr el arnes dos veces y comparar sus")
    w("bytes, y eso vive en el carril --reproduccion de este mismo fichero.")
    w("SIN ESA BANDERA, LO DE ARRIBA ES UN INDICIO DECLARADO Y NO UN VEREDICTO")
    w("DE REPRODUCCION.")
    w("")
    w("VEREDICTO DE LA PUERTA (por huella de texto): %s"
      % ("ROJO" if v["rojo"] else "VERDE"))
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
        # EL NOMBRE DEL TEMPORAL NO SE IMPRIME (vuelta 193, TAREA 2.b; hallazgo
        # 5.3 del acta 193). `mkdtemp` da un nombre ALEATORIO POR CONSTRUCCION,
        # y esta salida se sella y se compara: imprimirlo hacia que cambiara
        # EXACTAMENTE UNA LINEA en cada corrida. El directorio se sigue
        # fabricando y se sigue retirando; lo unico que se calla es su nombre,
        # que no prueba nada. Lo que SI prueba algo es que ya no exista, y eso
        # se sigue comprobando abajo.
        w("   (el nombre del temporal NO se imprime: `mkdtemp` lo fabrica")
        w("    aleatorio y esta salida se sella y se compara byte a byte)")
        w("   el prefijo con el que se fabrico: %r" % "guarda_entrada_")
        ok &= _caso(w, "el temporal quedo retirado", os.path.exists(tmp), False)
        w("")

    w("G) LA HUELLA DE TEXTO NO PRUEBA REPRODUCCION, Y ESTE ES EL CASO QUE CAE")
    w("   (vuelta 193, TAREA 2.d. Se fabrican DOS arneses que la huella de texto")
    w("    ve EXACTAMENTE IGUAL, porque los dos nombran `mkdtemp`, y que se")
    w("    comportan al reves: uno escribe siempre lo mismo y el otro escribe una")
    w("    linea distinta en cada corrida. Si el veredicto de esta guarda")
    w("    bastara, los dos pasarian)")
    tmp2 = tempfile.mkdtemp(prefix="guarda_reproduccion_")
    try:
        ESTABLE = ("vuelta199_tarea5_mutacion_estable.py",
                   "# -*- coding: utf-8 -*-\n"
                   '"""un arnes que reproduce."""\n'
                   "import io, os, sys, tempfile\n"
                   "d = tempfile.mkdtemp(prefix='x_')\n"
                   "os.rmdir(d)\n"
                   "r = os.path.join(os.path.dirname(os.path.abspath(__file__)),\n"
                   "                 'SALIDA_V199_ESTABLE.txt')\n"
                   "io.open(r, 'w', encoding='utf-8', newline=chr(10)).write(\n"
                   "    'siempre lo mismo' + chr(10))\n")
        MOVEDIZO = ("vuelta199_tarea6_mutacion_movedizo.py",
                    "# -*- coding: utf-8 -*-\n"
                    '"""un arnes que NO reproduce, y su huella dice lo contrario."""\n'
                    "import io, os, sys, tempfile\n"
                    "d = tempfile.mkdtemp(prefix='x_')\n"
                    "r = os.path.join(os.path.dirname(os.path.abspath(__file__)),\n"
                    "                 'SALIDA_V199_MOVEDIZO.txt')\n"
                    "io.open(r, 'w', encoding='utf-8', newline=chr(10)).write(\n"
                    "    'el temporal fue ' + d + chr(10))\n"
                    "os.rmdir(d)\n")
        _fabricar(tmp2, dict([ESTABLE, MOVEDIZO]))
        for _n, _c in (ESTABLE, MOVEDIZO):
            io.open(os.path.join(tmp2, "SALIDA_V199_%s.txt"
                                 % ("ESTABLE" if _n == ESTABLE[0] else "MOVEDIZO")),
                    "w", encoding="utf-8", newline=NL).write("sellada de mentira" + NL)

        w("   LA HUELLA DE TEXTO, QUE ES LA QUE HOY DECIDE:")
        vh = veredicto_de_entrada(nomina=[], directorio=tmp2, vara=198)
        por_nombre = dict((f[0], f[1]) for f in vh["reclamados"])
        for n in sorted(por_nombre):
            w("      %-46s %s" % (n, por_nombre[n]))
        ok &= _caso(w, "los DOS salen CONGELADO por su huella",
                    sorted(set(por_nombre.values())), ["CONGELADO"])
        ok &= _caso(w, "y por eso esta guarda NO cae por ninguno", vh["rojo"], False)
        w("")
        w("   LA VARA QUE SI LOS SEPARA: CORRERLOS DOS VECES Y COMPARAR BYTES")
        r_est = reproduce_de_verdad(ESTABLE[0], directorio=tmp2,
                                    base_salida=tmp2, restaurar=False)
        r_mov = reproduce_de_verdad(MOVEDIZO[0], directorio=tmp2,
                                    base_salida=tmp2, restaurar=False)
        w("      estable  -> medible %s | reproduce %s | c1 %s bytes | c2 %s bytes"
          % (r_est["medible"], r_est["reproduce"], r_est["c1"][0], r_est["c2"][0]))
        # LOS `sha256` DEL MOVEDIZO NO SE IMPRIMEN, Y ES LA MISMA LECCION DE LA
        # PIEZA 2.b: son distintos EN CADA CORRIDA por construccion, y esta
        # salida se sella y se compara byte a byte. Lo que prueba algo es que
        # sean DISTINTOS ENTRE SI, y eso si se imprime.
        w("      movedizo -> medible %s | reproduce %s | sus dos sha son "
          "distintos entre si: %s"
          % (r_mov["medible"], r_mov["reproduce"],
             r_mov["c1"][1] != r_mov["c2"][1]))
        ok &= _caso(w, "los dos son MEDIBLES",
                    (r_est["medible"], r_mov["medible"]), (True, True))
        ok &= _caso(w, "EL ESTABLE REPRODUCE", r_est["reproduce"], True)
        ok &= _caso(w, "EL MOVEDIZO NO REPRODUCE, Y ESTE ES EL CASO QUE CAE",
                    r_mov["reproduce"], False)
        w("   LA MUTACION: si la huella de texto bastara, los dos veredictos")
        w("   serian iguales y no habria nada que arreglar")
        if por_nombre.get(ESTABLE[0]) != por_nombre.get(MOVEDIZO[0]):
            w("      LA MUTACION NO CAYO: la huella ya los separaba.")
            ok = False
        elif r_est["reproduce"] == r_mov["reproduce"]:
            w("      LA MUTACION NO CAYO: la corrida doble tampoco los separa.")
            ok = False
        else:
            w("      LA MUTACION CAE: la huella dice %r de LOS DOS, y la corrida"
              % por_nombre.get(ESTABLE[0]))
            w("      doble dice reproduce=%s y reproduce=%s. UNA HUELLA DE TEXTO"
              % (r_est["reproduce"], r_mov["reproduce"]))
            w("      NO PRUEBA REPRODUCCION.")
        w("   LA MUTACION 2: un arnes que NO nombre una sola salida sellada tiene")
        w("   que salir NO MEDIBLE, y no colarse como reproducido")
        MUDO = ("vuelta199_tarea7_mutacion_mudo.py",
                "# -*- coding: utf-8 -*-\n"
                '"""un arnes que no sella nada."""\n'
                "import tempfile\n"
                "d = tempfile.mkdtemp()\n")
        _fabricar(tmp2, dict([MUDO]))
        r_mudo = reproduce_de_verdad(MUDO[0], directorio=tmp2,
                                     base_salida=tmp2, restaurar=False)
        ok &= _caso(w, "el mudo sale NO MEDIBLE", r_mudo["medible"], False)
        ok &= _caso(w, "y su veredicto de reproduccion NO es True",
                    r_mudo["reproduce"], None)
    finally:
        shutil.rmtree(tmp2, ignore_errors=True)
        w("   (el segundo temporal tambien se retira, P.16, y su nombre tampoco")
        w("    se imprime)")
        ok &= _caso(w, "el segundo temporal quedo retirado",
                    os.path.exists(tmp2), False)
    w("")

    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0 if ok else 1


def informe_de_reproduccion(filas):
    """LAS LINEAS DEL CARRIL CARO. PURA sobre la lista de (nombre, dict)."""
    L = []
    w = L.append
    w("=" * 78)
    w("LA REPRODUCCION, CORRIDA Y NO DEDUCIDA DE UNA HUELLA (vuelta 193, 2.c)")
    w("=" * 78)
    w("")
    w("LA VARA: cada arnes reclamado se corre DOS VECES y su salida sellada se")
    w("compara BYTE A BYTE. `reproduce` es entre las dos corridas de hoy;")
    w("`contra_sellada` es contra lo que el repo lleva commiteado. Las dos se")
    w("publican y ninguna se resuelve copiando.")
    w("")
    rotos, no_medibles, sin_restaurar = [], [], []
    for nombre, r in filas:
        if not r["medible"]:
            w("   %-46s NO MEDIBLE (no nombra una sola salida sellada)" % nombre)
            no_medibles.append(nombre)
            continue
        w("   %s" % nombre)
        w("      salida: %s" % r["ruta"])
        w("      sellada    -> LF %s bytes | sha256 %s" % r["sellada"])
        w("      corrida 1  -> exit %s | LF %s bytes | sha256 %s"
          % (r["exit1"], r["c1"][0], r["c1"][1]))
        w("      corrida 2  -> exit %s | LF %s bytes | sha256 %s"
          % (r["exit2"], r["c2"][0], r["c2"][1]))
        w("      REPRODUCE ENTRE SUS DOS CORRIDAS: %s" % r["reproduce"])
        w("      REPRODUCE CONTRA SU SELLADA:      %s" % r["contra_sellada"])
        w("      restaurada tras la corrida:       %s" % r["restaurada"])
        if not (r["reproduce"] and r["contra_sellada"]):
            rotos.append(nombre)
        if r["restaurada"] is False:
            sin_restaurar.append(nombre)
    w("")
    w("CIFRA arneses medidos: %d" % len([1 for _n, r in filas if r["medible"]]))
    w("CIFRA NO MEDIBLES (declarados, no supuestos): %d (%s)"
      % (len(no_medibles), ", ".join(no_medibles) or "ninguno"))
    w("CIFRA QUE NO REPRODUCEN: %d (%s)"
      % (len(rotos), ", ".join(rotos) or "ninguno"))
    w("CIFRA SIN RESTAURAR: %d (%s)"
      % (len(sin_restaurar), ", ".join(sin_restaurar) or "ninguno"))
    w("")
    w("VEREDICTO DE REPRODUCCION: %s"
      % ("ROJO" if (rotos or sin_restaurar) else "VERDE"))
    return L, bool(rotos or sin_restaurar)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutacion", action="store_true")
    ap.add_argument("--reproduccion", action="store_true",
                    help="corre cada arnes reclamado DOS veces y compara sus "
                         "bytes. Es el carril caro, y es el unico que prueba "
                         "reproduccion de verdad")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if a.mutacion:
        return prueba_de_mutacion()
    print("=" * 78)
    print("GUARDA DE ENTRADA A LA NOMINA. Corre ANTES de la bateria, no dentro.")
    print("=" * 78)
    v = veredicto_de_entrada()
    lineas = informe(v)
    rojo_repro = False
    if a.reproduccion:
        filas = [(f[0], reproduce_de_verdad(f[0])) for f in v["reclamados"]]
        extra, rojo_repro = informe_de_reproduccion(filas)
        lineas = lineas + [""] + extra
    for l in lineas:
        print(l)
    ruta = os.path.join(LOOP, "SALIDA_V193_T2C_GUARDA_REPRODUCCION.txt")
    if a.reproduccion:
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(
            NL.join(lineas) + NL)
        print("")
        print("ESCRITO: docs/loop/SALIDA_V193_T2C_GUARDA_REPRODUCCION.txt (%d bytes)"
              % len((NL.join(lineas) + NL).encode("utf-8")))
    return 1 if (v["rojo"] or rojo_repro) else 0


if __name__ == "__main__":
    sys.exit(main())
