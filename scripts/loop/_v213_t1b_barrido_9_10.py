# -*- coding: utf-8 -*-
r"""_v213_t1b_barrido_9_10.py . LA TAREA 1.b DE LA VUELTA 213: EL BARRIDO DEL
`9.10` QUE EL ACTA 212 ADJUDICA EN SU `6.1`, Y ES UNA SOLA LINEA.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). Muere con la vuelta.

QUE HACE, Y NADA MAS: corrige por el carril del banco `9.10` la ultima clausula
de la frase de `docs/plan/03_FUSIONES.md` que arranca en la linea 5424, que decia
que el puesto 730 "lo deja anotado en vez de elegir" y hoy es falsa, porque la
fila eligio en la vuelta 212. LA CORRECCION ES DECLARADA Y ADITIVA: el texto
viejo se queda ENTERO Y SIN TACHAR, y el bloque nuevo va detras.

LO QUE NO TOCA: `docs/INTRA_DOMINIO_INFORME.md` linea 6941 (hecho historico que
sigue siendo verdadero), ningun reporte archivado, y ninguna clase ni razon de
ninguna fila del archivo de veredictos.

EL ORDEN ES EL DE LA CASA: (1) sede al entrar por las dos convenciones, (2) se
lee del disco lo que se va a corregir, (3) se compone en memoria, (4) SE JUZGA la
composicion, (5) EL CASO ROJO POR MUTACION corre ANTES de escribir y todos los
mutantes tienen que caer, (6) solo entonces se escribe, (7) sede al salir y
numstat.

USO:  python scripts/loop/_v213_t1b_barrido_9_10.py            (simula y no escribe)
      python scripts/loop/_v213_t1b_barrido_9_10.py --escribir
"""
import difflib
import hashlib
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = "docs/plan/03_FUSIONES.md"
RUTA_VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
RUTA_INFORME = "docs/INTRA_DOMINIO_INFORME.md"
LINEA_ANCLA = 5424          # la que el acta 212 cita en su 6.1
LINEA_CLAUSULA = 5425       # donde vive de verdad la clausula que envejecio
LINEA_INTOCABLE_INFORME = 6941
CLAUSULA_FALSA = "lo deja anotado en vez de elegir"
PUESTO = 730


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def sha_de(ruta):
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    b = io.open(p, "rb").read()
    return (hashlib.sha256(b).hexdigest()[:16],
            hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16])


def sede(ruta, cuando):
    m = medir_en_disco(RAIZ, ruta)
    sd, sl = sha_de(ruta)
    return ("CIFRA SEDE %s %s: %d bytes en disco y %d bytes normalizado a LF (%s), "
            "sha256 disco %s y sha256 LF %s"
            % (ruta, cuando, m[0], m[1],
               "COINCIDEN" if m[0] == m[1] else "NO COINCIDEN", sd, sl))


def clase_del_puesto(texto_jsonl, puesto):
    """PURA: recibe el texto del archivo y devuelve la clase de ese puesto."""
    import json
    for l in texto_jsonl.split(NL):
        l = l.strip()
        if not l:
            continue
        d = json.loads(l)
        if d.get("puesto_intra") == puesto:
            return d.get("clase"), d.get("nodo_a"), d.get("nodo_b")
    return None, None, None


def juzgar(lineas_viejas, lineas_nuevas, commit_citado, commit_real,
           clase_hoy, clase_antes):
    """EL JUICIO. PURA: no lee ni escribe nada, recibe todo y devuelve la lista
    de fallos. Es la que los mutantes tienen que tumbar."""
    fallos = []
    sm = difflib.SequenceMatcher(None, lineas_viejas, lineas_nuevas, autojunk=False)
    ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
    inserciones = [o for o in ops if o[0] == "insert"]
    otros = [o for o in ops if o[0] != "insert"]
    if otros:
        fallos.append("(1) EL TEXTO VIEJO NO ESTA ENTERO: hay %d bloque(s) que no "
                      "son insercion (%s). Una correccion que tapa lo que corrige "
                      "no se puede auditar." % (len(otros), [o[0] for o in otros]))
    if len(inserciones) != 1:
        fallos.append("(2) SE TOCA MAS DE UNA REGION DEL FICHERO: %d bloque(s) de "
                      "insercion, y esta tarea es UNA sola." % len(inserciones))
    else:
        i1, i2, j1, j2 = inserciones[0][1], inserciones[0][2], inserciones[0][3], inserciones[0][4]
        if i1 != LINEA_CLAUSULA:
            fallos.append("(3) LA INSERCION NO VA PEGADA A LA CLAUSULA QUE ENVEJECIO: "
                          "entra tras la linea %d y tenia que entrar tras la %d."
                          % (i1, LINEA_CLAUSULA))
        bloque = "".join(lineas_nuevas[j1:j2])
        if CLAUSULA_FALSA not in bloque:
            fallos.append("(4) LA CORRECCION NO CITA LA CLAUSULA VIEJA VERBATIM: no "
                          "aparece %r en el bloque nuevo." % CLAUSULA_FALSA)
        if commit_citado not in bloque:
            fallos.append("(5) LA CORRECCION NO CITA EL COMMIT DEL VOLTEO dentro de "
                          "su propio bloque.")
        if "vuelta 212" not in bloque.lower():
            fallos.append("(6) LA CORRECCION NO CITA LA VUELTA DEL VOLTEO dentro de "
                          "su propio bloque.")
        if chr(8212) in bloque or chr(8211) in bloque:
            fallos.append("(7) HAY GUION LARGO O GUION MEDIO en el bloque nuevo "
                          "(EJECUTOR.md 10).")
    if commit_citado != commit_real:
        fallos.append("(8) LA CITA NO CALZA: se cita el commit %s y git dice que el "
                      "que volteo el puesto %d es %s."
                      % (commit_citado, PUESTO, commit_real))
    if clase_hoy != "D" or clase_antes != "A":
        fallos.append("(9) LA CITA NO CALZA CONTRA EL ARCHIVO: se afirma un paso de "
                      "A a D y el archivo dice %s antes y %s hoy."
                      % (clase_antes, clase_hoy))
    return fallos


def main():
    escribir = "--escribir" in sys.argv
    print("=" * 78)
    print("VUELTA 213, TAREA 1.b. EL BARRIDO DEL 9.10, Y ES UNA SOLA LINEA")
    print("adjudicacion 6.1 del acta 212 (linea 75082 de docs/loop/ACTA_AUDITOR.md)")
    print("modo: %s" % ("ESCRIBIR" if escribir else "SIMULACION, no toca el disco"))
    print("=" * 78)
    print("")

    print("PASO 1. LAS SEDES AL ENTRAR, POR LAS DOS CONVENCIONES")
    print("   " + sede(RUTA, "AL ENTRAR"))
    print("   " + sede(RUTA_VEREDICTOS, "AL ENTRAR"))
    print("   " + sede(RUTA_INFORME, "AL ENTRAR"))
    sha_ver_entrar = sha_de(RUTA_VEREDICTOS)
    sha_inf_entrar = sha_de(RUTA_INFORME)
    sha_fus_entrar = sha_de(RUTA)
    print("")

    print("PASO 2. LO QUE SE VA A CORREGIR, LEIDO DEL DISCO EN ESTA VUELTA")
    p = os.path.join(RAIZ, RUTA.replace("/", os.sep))
    raw = io.open(p, encoding="utf-8", newline="").read()
    lineas = raw.splitlines(keepends=True)
    print("   CIFRA lineas del fichero: %d" % len(lineas))
    for n in (LINEA_ANCLA, LINEA_CLAUSULA):
        print("   linea %d LEIDA DEL DISCO: %s" % (n, lineas[n - 1].rstrip()))
    esta = CLAUSULA_FALSA in lineas[LINEA_CLAUSULA - 1]
    print("   la clausula que envejecio vive en la linea %d: %s"
          % (LINEA_CLAUSULA, "SI" if esta else "NO"))
    if not esta:
        print("ROJO: la clausula no esta donde se dice. No se escribe nada.")
        return 1
    print("")

    print("PASO 3. LA LINEA 6941 DEL INFORME, LEIDA Y NO TOCADA (prohibicion expresa)")
    pi = os.path.join(RAIZ, RUTA_INFORME.replace("/", os.sep))
    li = io.open(pi, encoding="utf-8", newline="").read().splitlines()
    print("   linea %d: %s" % (LINEA_INTOCABLE_INFORME,
                               li[LINEA_INTOCABLE_INFORME - 1].strip()[:150]))
    print("   ESTE FICHERO NO SE ABRE PARA ESCRITURA EN NINGUN CAMINO DE ESTE SCRIPT.")
    print("")

    print("PASO 4. EL VOLTEO DEL 730, LEIDO DE GIT Y DEL ARCHIVO EN ESTA VUELTA")
    c, sal = git(["log", "-1", "--format=%H", "--", RUTA_VEREDICTOS])
    commit_real = sal.strip()[:8]
    c, fecha = git(["log", "-1", "--format=%ci", commit_real])
    hoy_txt = io.open(os.path.join(RAIZ, RUTA_VEREDICTOS.replace("/", os.sep)),
                      encoding="utf-8").read()
    clase_hoy, nodo_a, nodo_b = clase_del_puesto(hoy_txt, PUESTO)
    c, antes_txt = git(["show", "%s^:%s" % (commit_real, RUTA_VEREDICTOS)])
    clase_antes, _, _ = clase_del_puesto(antes_txt, PUESTO)
    print("   CIFRA commit que toco el archivo por ultima vez: %s (%s)"
          % (commit_real, fecha.strip()))
    print("   CIFRA clase del puesto %d en %s^: %s" % (PUESTO, commit_real, clase_antes))
    print("   CIFRA clase del puesto %d en el disco de hoy: %s" % (PUESTO, clase_hoy))
    print("   los dos nodos del puesto: %s -> %s" % (nodo_a, nodo_b))
    print("")

    fin = lineas[LINEA_CLAUSULA - 1][len(lineas[LINEA_CLAUSULA - 1].rstrip(chr(13) + NL)):]
    if not fin:
        fin = NL
    bloque_txt = [
        ">",
        "> **CORRECCION DECLARADA (8 sep 2026, vuelta 213, TAREA `1.b` del encargo, por el",
        "> carril del banco `9.10`; adjudicacion `6.1` del acta 212, linea 75082 de",
        "> `docs/loop/ACTA_AUDITOR.md`, leida hoy). EL TEXTO DE ARRIBA SE QUEDA ENTERO Y SIN",
        "> TACHAR, Y LO QUE SE CORRIGE ES SU ULTIMA CLAUSULA.** La frase de arriba cierra con",
        "> *\"y lo deja anotado en vez de elegir\"*, **y eso YA ES FALSO: la fila eligio.** El",
        "> puesto **730** (`colaboracion_cadena_suministro` a `efecto_bullwhip`) **paso de `A` a",
        "> `D` en la VUELTA 212**, con la vara del banco `9.6.1` aplicada en la direccion del",
        "> `9.6.2`, y el volteo vive en el commit **`9140d524`** (2026-09-08). **NO LO RECUERDO,",
        "> LO MEDI EN ESTA VUELTA:** `git log -1 --format=%H -- docs/INTRA_DOMINIO_VEREDICTOS.jsonl`",
        "> devuelve ese commit, la clase del puesto es **`A`** en `9140d524^` y es **`D`** en el",
        "> disco de hoy.",
        ">",
        "> **LO QUE SIGUE SIENDO VERDADERO Y NO SE CORRIGE, PORQUE LA CORRECCION ES ESTRECHA A",
        "> PROPOSITO:** la primera mitad de la frase, o sea que el puesto **declaraba de si",
        "> mismo** que la clase quedaba en `A` por la lectura vieja del cero-enlazados y que si",
        "> mandara el contenido seria `D`. **Eso es lo que paso, y es exactamente lo que hizo que",
        "> la fila se releyera.**",
        ">",
        "> **Y LO QUE NO SE TOCA, DICHO AQUI PARA QUE NADIE LO BARRA DESPUES:**",
        "> `docs/INTRA_DOMINIO_INFORME.md` linea **6941** *(\"El puesto 730 es el primer veredicto",
        "> nuevo emitido despues de que el choque de la seccion 19 quedara escrito\")* **NO se",
        "> corrige**: es un hecho historico y sigue siendo verdadero.",
    ]
    bloque = [t + fin for t in bloque_txt]
    nuevas = lineas[:LINEA_CLAUSULA] + bloque + lineas[LINEA_CLAUSULA:]

    print("PASO 5. EL JUICIO SOBRE LA COMPOSICION EN MEMORIA, ANTES DE TOCAR EL DISCO")
    fallos = juzgar(lineas, nuevas, "9140d524", commit_real, clase_hoy, clase_antes)
    print("   CIFRA lineas anadidas: %d | CIFRA lineas quitadas: %d"
          % (len(nuevas) - len(lineas), 0))
    print("   CIFRA fallos de la simulacion: %d" % len(fallos))
    for f in fallos:
        print("      FALLO " + f)
    print("")

    print("PASO 6. EL CASO ROJO POR MUTACION, CORRIDO ANTES DE ESCRIBIR")
    print("   (EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION: se cambia el")
    print("    valor esperado y se comprueba que el caso CAE)")
    mut_tapa = lineas[:LINEA_CLAUSULA - 3] + bloque + lineas[LINEA_CLAUSULA:]
    mut_segunda = list(nuevas)
    idx_segunda = LINEA_CLAUSULA + len(bloque) + 2
    mut_segunda[idx_segunda] = mut_segunda[idx_segunda].rstrip(chr(13) + NL) + " (tocada)" + fin
    mutantes = [
        ("A: TAPA EL TEXTO VIEJO (se come tres lineas de la frase)",
         lambda: juzgar(lineas, mut_tapa, "9140d524", commit_real, clase_hoy, clase_antes)),
        ("B: TOCA UNA SEGUNDA LINEA DEL FICHERO ademas de insertar",
         lambda: juzgar(lineas, mut_segunda, "9140d524", commit_real, clase_hoy, clase_antes)),
        ("C: ESCRIBE UNA CITA QUE NO CALZA (commit inventado)",
         lambda: juzgar(lineas, [l.replace("9140d524", "0000dead") for l in nuevas],
                        "0000dead", commit_real, clase_hoy, clase_antes)),
        ("D: AFIRMA UN PASO QUE EL ARCHIVO NO SOSTIENE (clase de hoy fingida en A)",
         lambda: juzgar(lineas, nuevas, "9140d524", commit_real, "A", clase_antes)),
    ]
    caen = 0
    for nombre, fn in mutantes:
        fs = fn()
        cae = len(fs) > 0
        caen += 1 if cae else 0
        print("   MUTANTE %-62s -> %s (%d fallo(s))"
              % (nombre, "CAE" if cae else "NO CAE, ROJO", len(fs)))
        for f in fs:
            print("        " + f)
    print("   CIFRA mutantes: %d | CIFRA mutantes que caen: %d (se exigen todos)"
          % (len(mutantes), caen))
    print("")

    if fallos or caen != len(mutantes):
        print("ROJO: no se escribe nada. docs/plan/03_FUSIONES.md queda intacto.")
        return 1
    if not escribir:
        print("SIMULACION VERDE. No se ha tocado el disco. Vuelve con --escribir.")
        return 0

    io.open(p, "w", encoding="utf-8", newline="").write("".join(nuevas))
    print("PASO 7. ESCRITO. LAS SEDES AL SALIR, POR LAS DOS CONVENCIONES")
    print("   " + sede(RUTA, "AL SALIR"))
    print("   " + sede(RUTA_VEREDICTOS, "AL SALIR"))
    print("   " + sede(RUTA_INFORME, "AL SALIR"))
    sha_fus_salir = sha_de(RUTA)
    sha_ver_salir = sha_de(RUTA_VEREDICTOS)
    sha_inf_salir = sha_de(RUTA_INFORME)
    print("")
    print("   el sha256 LF de %s SE MUEVE: %s -> %s (%s)"
          % (RUTA, sha_fus_entrar[1], sha_fus_salir[1],
             "SI, como se exige" if sha_fus_entrar[1] != sha_fus_salir[1] else "NO, ROJO"))
    print("   el sha256 LF de %s NO se mueve: %s -> %s (%s)"
          % (RUTA_VEREDICTOS, sha_ver_entrar[1], sha_ver_salir[1],
             "QUIETO, como se exige" if sha_ver_entrar[1] == sha_ver_salir[1] else "SE MOVIO, ROJO"))
    print("   el sha256 LF de %s NO se mueve: %s -> %s (%s)"
          % (RUTA_INFORME, sha_inf_entrar[1], sha_inf_salir[1],
             "QUIETO, como se exige" if sha_inf_entrar[1] == sha_inf_salir[1] else "SE MOVIO, ROJO"))
    print("")
    print("PASO 8. EL NUMSTAT, ACOTADO Y CONTADO")
    for sede_ns, ruta_ns in (("ese fichero", RUTA), ("docs/plan entero", "docs/plan"),
                             ("dataset, web y engine", None)):
        if ruta_ns is None:
            c, ns = git(["diff", "HEAD", "--numstat", "--", "dataset/", "web/", "engine/"])
        else:
            c, ns = git(["diff", "HEAD", "--numstat", "--", ruta_ns])
        filas = [l for l in ns.split(NL) if l.strip()]
        print("   CIFRA filas de numstat de %-22s: %d" % (sede_ns, len(filas)))
        for f in filas:
            print("      FILA: %s" % f)
    relectura = io.open(p, encoding="utf-8", newline="").read()
    print("")
    print("   RELECTURA DEL DISCO identica a lo juzgado: %s"
          % ("SI" if relectura == "".join(nuevas) else "NO"))
    print("VERDE: la 1.b queda ejecutada." if relectura == "".join(nuevas)
          else "ROJO: lo escrito no es lo juzgado.")
    return 0 if relectura == "".join(nuevas) else 1


if __name__ == "__main__":
    sys.exit(main())
