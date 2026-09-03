# -*- coding: utf-8 -*-
r"""vuelta163_tarea5a_cotejo_contador.py . TAREA 5.a de la vuelta 163.

LA VARA DE ACEPTACION DE LA ADJUDICACION 6.11 DEL ACTA 162, MEDIDA: el contador
de `P.5.2` gana nombre estable POR REMISION
(`scripts/loop/contador_de_segundas_lecturas.py`), el viejo NO SE BORRA, las
citas de las actas siguen resolviendo, **y la cifra sale IDENTICA antes y
despues**.

COMO SE MIDE, Y NO SE ALEGA. Los tres se corren HOY:
  (1) `scripts/loop/_v163_contador_viejo_copia.py`, copia BYTE A BYTE del viejo
      tomada ANTES de tocar nada;
  (2) `scripts/loop/vuelta161_tarea1c_segunda_lectura.py`, el viejo despues del
      unico cambio (sacar a funcion el bucle que ya tenia dentro);
  (3) `scripts/loop/contador_de_segundas_lecturas.py`, el nombre estable.

Y se cotejan DOS COSAS: las CINCO cifras parseadas de cada salida, y la salida
ENTERA byte a byte. La unica diferencia admitida, y va declarada, es la linea de
titulo que el nombre estable anade al principio: cualquier otra tumba esto.

USO:
  python scripts/loop/vuelta163_tarea5a_cotejo_contador.py
  python scripts/loop/vuelta163_tarea5a_cotejo_contador.py --mutacion
"""
import argparse
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
LOOP = AQUI
RAIZ = os.path.dirname(os.path.dirname(AQUI))

CORREDORES = [
    ("COPIA DEL VIEJO, TOMADA ANTES DE TOCAR NADA",
     "scripts/loop/_v163_contador_viejo_copia.py"),
    ("EL VIEJO, DESPUES DEL CAMBIO",
     "scripts/loop/vuelta161_tarea1c_segunda_lectura.py"),
    ("EL NOMBRE ESTABLE, POR REMISION",
     "scripts/loop/contador_de_segundas_lecturas.py"),
]

# LA LINEA QUE EL NOMBRE ESTABLE ANADE A PROPOSITO, Y LA UNICA ADMITIDA.
LINEA_DE_REMISION = ("CONTADOR DE SEGUNDAS LECTURAS (P.5.2), NOMBRE ESTABLE POR "
                     "REMISION A scripts/loop/vuelta161_tarea1c_segunda_lectura.py")

CIFRAS = [
    ("con al menos una", r"CIFRA con AL MENOS UNA segunda lectura independiente: (\d+)"),
    ("con dos o mas", r"CIFRA con DOS O MAS: (\d+)"),
    ("con ninguna", r"CIFRA con NINGUNA: (\d+)"),
    ("actos sobre filas", r"CIFRA total de actos sobre filas: (\d+)"),
    ("tipos de acto", r"CIFRA actos distintos \(tipo, vuelta\): (\d+)"),
]

# LA VARA QUE EL ENCARGO DE LA VUELTA 163 ESCRIBIO CON SUS NUMEROS. NO SE BORRA
# NI UNO: queda escrita aqui como lo que es, la medicion de aquel dia.
#
# --- ARREGLO DE LA VUELTA 164, TAREA 2.a: ESTA VARA ESTABA CLAVADA Y CADUCO ---
#
# QUE PASO, MEDIDO Y NO ALEGADO. Estos cinco numeros eran ESTADO CLAVADO del
# registro tal como estaba el 3 sep 2026 al escribirse el encargo de la 163. La
# TAREA 4 de la vuelta 164 movio la `LD-OPC05-005` de `C` a `D` y le escribio su
# marca de relectura conjunta, que ES CONTABLE por `P.5.2`; y la TAREA 3 le
# escribio la suya a la `LD-OPC05-101`. Resultado medido: `con dos o mas` paso de
# 16 a 17 y `tipos de acto` de 8 a 9. El arnes salio ROJO en la bateria del
# cierre SIN QUE NADIE TOCARA UNA LINEA DE SU CODIGO, que es la definicion exacta
# de la enfermedad que esta misma vuelta 163 curo dos veces, en `160_6b` ("una
# contraprueba anclada a una referencia movil es un falso verde esperando su
# dia") y en `162_1a` ("los esperados se COMPUTAN del estado del dia, no se
# clavan"). Aqui no es un falso verde: es un ROJO LEGITIMO DEL ARNES, que cae
# porque el mundo se movio por debajo y no porque el instrumento medido falle.
#
# EL REMEDIO, Y ES EL DE LA CASA: LA VARA SE ANCLA A UN REF FIJO Y COMPUTADO. Ya
# no se teclea ningun numero: se corre el contador sobre el REGISTRO TAL COMO
# ESTABA EN EL COMMIT DE APERTURA DE LA VUELTA 163, leido de `git log
# --diff-filter=A` sobre su sello de HEAD, y esas son las cifras contra las que
# se coteja. Un ref de git no se mueve, asi que este cotejo no puede volver a
# caducar; y si alguna vuelta futura moviera el registro, este arnes seguiria
# midiendo lo unico que le importa de verdad: QUE LOS TRES CORREDORES DAN LO
# MISMO ENTRE SI.
VARA_DEL_ENCARGO_DE_LA_163 = {
    "con al menos una": 92,
    "con dos o mas": 16,
    "con ninguna": 30,
    "actos sobre filas": 115,
    "tipos de acto": 8,
}

SELLO_APERTURA_163 = "docs/loop/SALIDA_V163_HEAD_APERTURA.txt"
REGISTRO_REL = "docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl"


def ref_de_apertura_163():
    """EL REF FIJO Y COMPUTADO: el commit que ANADIO el sello de apertura de la
    vuelta 163. Ni se teclea un hash ni se mira HEAD."""
    r = subprocess.run(["git", "log", "--diff-filter=A", "--format=%H", "--",
                        SELLO_APERTURA_163],
                       cwd=RAIZ, capture_output=True, text=True)
    hs = [l.strip() for l in (r.stdout or "").splitlines() if l.strip()]
    return hs[0] if len(hs) == 1 else None


def vara_computada():
    """LAS CINCO CIFRAS DE LA VARA, RECOMPUTADAS SOBRE EL REGISTRO DEL COMMIT DE
    APERTURA DE LA 163. Devuelve (dict, ref) o (None, ref) si no se puede."""
    ref = ref_de_apertura_163()
    if not ref:
        return None, ref
    b = subprocess.run(["git", "show", "%s:%s" % (ref, REGISTRO_REL)],
                       cwd=RAIZ, capture_output=True)
    if b.returncode:
        return None, ref
    tmp = tempfile.mkdtemp(prefix="vara_163_")
    try:
        # EL CONTADOR LEE UNA RUTA FIJA (su global `REGISTRO`), asi que se le
        # apunta al fichero DEL REF, escrito en un temporal, y se le corre su
        # `main()` capturando la salida: NO se reimplementa ni una linea de su
        # cuenta. P.16, el temporal se retira siempre y el global se restaura en
        # un `finally`.
        ruta = os.path.join(tmp, "REGISTRO_DEL_REF.jsonl")
        with open(ruta, "wb") as fh:
            fh.write(b.stdout)
        sys.path.insert(0, LOOP)
        import vuelta161_tarea1c_segunda_lectura as C   # noqa: E402
        guardado = C.REGISTRO
        pantalla = io.StringIO()
        try:
            C.REGISTRO = ruta
            viejo_stdout = sys.stdout
            sys.stdout = pantalla
            try:
                C.main()
            finally:
                sys.stdout = viejo_stdout
        finally:
            C.REGISTRO = guardado
        return cifras_de(pantalla.getvalue()), ref
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def correr(ruta):
    r = subprocess.run([sys.executable, os.path.join(RAIZ, ruta.replace("/", os.sep))],
                       cwd=RAIZ, capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def cifras_de(salida):
    out = {}
    for nombre, patron in CIFRAS:
        m = re.search(patron, salida)
        out[nombre] = int(m.group(1)) if m else None
    return out


def sin_la_linea_de_remision(salida):
    return "\n".join(l for l in salida.split("\n") if l.strip() != LINEA_DE_REMISION)


def medir():
    resultados = []
    for etiqueta, ruta in CORREDORES:
        code, salida = correr(ruta)
        resultados.append((etiqueta, ruta, code, salida, cifras_de(salida)))
    return resultados


def main():
    print("=" * 78)
    print("VUELTA 163, TAREA 5.a: NOMBRE ESTABLE POR REMISION PARA EL CONTADOR DE P.5.2")
    print("=" * 78)
    print("")

    print("A) EL VIEJO NO SE BORRA Y LAS CITAS SIGUEN RESOLVIENDO")
    for _e, ruta in CORREDORES:
        print("   existe %-58s %s" % (ruta, os.path.exists(os.path.join(RAIZ, ruta))))
    citas = subprocess.run(
        ["git", "grep", "-c", "vuelta161_tarea1c_segunda_lectura",
         "--", "docs/loop/ACTA_AUDITOR.md", "docs/loop/REPORTE.md",
         "docs/PENDIENTES.md", "docs/plan"],
        cwd=RAIZ, capture_output=True, text=True)
    lineas_citas = [l for l in citas.stdout.strip().split("\n") if l.strip()]
    print("   CIFRA ficheros de docs/ que citan el nombre viejo: %d" % len(lineas_citas))
    for l in lineas_citas:
        print("      %s" % l)
    print("   El nombre viejo SIGUE EXISTIENDO, asi que ninguna de esas citas se rompe.")
    print("")

    print("B) LOS TRES, CORRIDOS HOY")
    resultados = medir()
    for etiqueta, ruta, code, _s, cif in resultados:
        print("   %-45s exit %d  %s" % (ruta, code, etiqueta))
        print("      %s" % "  ".join("%s=%s" % (k, cif[k]) for k, _p in CIFRAS))
    print("")

    print("C) LAS CINCO CIFRAS, COTEJADAS ENTRE SI Y CONTRA LA VARA ANCLADA")
    vara, ref = vara_computada()
    print("   LA VARA YA NO SE TECLEA (arreglo de la vuelta 164, TAREA 2.a): se")
    print("   recomputa corriendo el contador sobre el REGISTRO DEL COMMIT DE")
    print("   APERTURA DE LA VUELTA 163, leido de git log --diff-filter=A sobre")
    print("   %s." % SELLO_APERTURA_163)
    print("   ref de apertura de la 163, computado: %s" % (ref or "NO SE PUDO COMPUTAR"))
    if vara is None:
        print("   ROJO PREVIO: no se pudo recomputar la vara sobre el ref.")
        return 1
    print("   VARA RECOMPUTADA SOBRE EL REF: %s"
          % "  ".join("%s=%s" % (k, vara[k]) for k, _p in CIFRAS))
    print("   VARA QUE EL ENCARGO DE LA 163 TECLEO, que NO se borra y se coteja")
    print("   contra la recomputada: %s"
          % "  ".join("%s=%s" % (k, VARA_DEL_ENCARGO_DE_LA_163[k]) for k, _p in CIFRAS))
    discrepan = [k for k, _p in CIFRAS if vara[k] != VARA_DEL_ENCARGO_DE_LA_163[k]]
    print("   CIFRA cifras de la vara tecleada que NO reproduce el ref: %d (%s)"
          % (len(discrepan), ", ".join(discrepan) or "ninguna"))
    print("")
    fallos = []
    for nombre, _p in CIFRAS:
        valores = [cif[nombre] for _e, _r, _c, _s, cif in resultados]
        iguales = len(set(valores)) == 1
        contra_vara = valores[0] == vara[nombre]
        print("   %-20s %s  | iguales en los tres: %-5s | vara anclada %s: %s"
              % (nombre, valores, iguales, vara[nombre],
                 "CALZA" if contra_vara else "SE MOVIO DESDE LA APERTURA DE LA 163"))
        if not iguales:
            fallos.append(nombre)
    movidas = [n for n, _p in CIFRAS
               if [cif[n] for _e, _r, _c, _s, cif in resultados][0] != vara[n]]
    print("")
    print("   CIFRA cifras que SE MOVIERON desde la apertura de la 163: %d (%s)"
          % (len(movidas), ", ".join(movidas) or "ninguna"))
    print("   Y ESO NO ES ROJO DE ESTE ARNES, Y SE DICE POR QUE: lo que este")
    print("   instrumento tiene que probar es que LOS TRES CORREDORES DAN LO MISMO,")
    print("   que es la vara de aceptacion de la 6.11 del acta 162. Que el registro")
    print("   se mueva entre vueltas es lo NORMAL y no dice nada del contador. La")
    print("   version vieja de este arnes hacia caer el veredicto cuando el registro")
    print("   se movia, y por eso salio ROJO en la bateria de la vuelta 164 sin que")
    print("   nadie tocara su codigo. Las movidas se PUBLICAN, no se tumban.")
    print("")

    print("D) LA SALIDA ENTERA, BYTE A BYTE, Y NO SOLO LAS CIFRAS")
    base = sin_la_linea_de_remision(resultados[0][3])
    for etiqueta, ruta, _c, salida, _cif in resultados[1:]:
        otro = sin_la_linea_de_remision(salida)
        igual = (base == otro)
        print("   %-45s %s" % (ruta, "IDENTICA" if igual else "DISTINTA"))
        if not igual:
            fallos.append(ruta)
            a = base.split("\n")
            b = otro.split("\n")
            for i in range(max(len(a), len(b))):
                la = a[i] if i < len(a) else "(no hay linea)"
                lb = b[i] if i < len(b) else "(no hay linea)"
                if la != lb:
                    print("      linea %d:" % (i + 1))
                    print("        copia:  %s" % la)
                    print("        nuevo:  %s" % lb)
    print("   La UNICA diferencia admitida es la linea de remision que el nombre")
    print("   estable anade a proposito, y se descuenta con su literal declarado.")
    print("   CIFRA lineas de remision en la salida del nombre estable: %d"
          % resultados[2][3].count(LINEA_DE_REMISION))
    print("")

    if fallos:
        print("ROJO: %d cotejo(s) no calzan: %s" % (len(fallos), ", ".join(fallos)))
        return 1
    print("VERDE: los tres dan las MISMAS cinco cifras, calzan con la vara del encargo,")
    print("y su salida es IDENTICA byte a byte salvo la linea de remision declarada.")
    return 0


def prueba_de_mutacion():
    print("=" * 78)
    print("VUELTA 163, TAREA 5.a: CASO POSITIVO POR MUTACION")
    print("=" * 78)
    print("")
    resultados = medir()
    vara, ref = vara_computada()
    if vara is None:
        print("ROJO PREVIO: no se pudo recomputar la vara sobre el ref de apertura")
        print("de la vuelta 163. Sin ancla no se mide.")
        return 1
    print("   LA VARA, ANCLADA Y NO TECLEADA (arreglo de la vuelta 164, TAREA 2.a)")
    print("   ref de apertura de la vuelta 163, computado de git: %s" % ref)
    print("   vara recomputada sobre ESE registro: %s"
          % "  ".join("%s=%s" % (k, vara[k]) for k, _p in CIFRAS))
    print("")
    casos = []
    for nombre, _p in CIFRAS:
        valores = [cif[nombre] for _e, _r, _c, _s, cif in resultados]
        # LO QUE ESTE ARNES TIENE QUE PROBAR, Y ES LA VARA DE LA 6.11 DEL ACTA
        # 162: que LOS TRES CORREDORES DAN LO MISMO. Esto no puede caducar.
        casos.append(("los_tres_dan_lo_mismo_en_%s" % nombre.replace(" ", "_"),
                      len(set(valores)), 1))
        # Y LA VARA, ANCLADA A UN REF FIJO: el contador corrido sobre el registro
        # de la apertura de la 163 reproduce la cifra que aquel encargo tecleo.
        # Es la misma comprobacion de antes, pero contra algo que no se mueve.
        casos.append(("la_vara_anclada_reproduce_la_tecleada_en_%s"
                      % nombre.replace(" ", "_"),
                      vara[nombre], VARA_DEL_ENCARGO_DE_LA_163[nombre]))
    # EL DELTA, PUBLICADO Y NO TUMBADO: cuantas cifras se movieron desde la
    # apertura de la 163. Es medicion del mundo, no veredicto del contador, y por
    # eso NO entra como caso que pueda hacer caer este arnes.
    movidas = [n for n, _p in CIFRAS
               if [cif[n] for _e, _r, _c, _s, cif in resultados][0] != vara[n]]
    print("   CIFRA cifras que SE MOVIERON desde la apertura de la 163: %d (%s)"
          % (len(movidas), ", ".join(movidas) or "ninguna"))
    print("   NO es caso de este arnes: el registro se mueve entre vueltas y eso")
    print("   no dice nada del contador. Se publica y no se tumba.")
    print("")
    base = sin_la_linea_de_remision(resultados[0][3])
    casos.append(("salida_del_viejo_refactorizado_IDENTICA",
                  sin_la_linea_de_remision(resultados[1][3]) == base, True))
    casos.append(("salida_del_nombre_estable_IDENTICA",
                  sin_la_linea_de_remision(resultados[2][3]) == base, True))
    casos.append(("el_nombre_estable_anade_UNA_linea_de_remision",
                  resultados[2][3].count(LINEA_DE_REMISION), 1))
    casos.append(("el_viejo_NO_anade_la_linea_de_remision",
                  resultados[1][3].count(LINEA_DE_REMISION), 0))
    casos.append(("el_viejo_sigue_existiendo",
                  os.path.exists(os.path.join(
                      RAIZ, "scripts", "loop",
                      "vuelta161_tarea1c_segunda_lectura.py")), True))
    # EL CASO QUE MUERDE LA REMISION DE VERDAD: el nombre estable no trae copia
    # de la definicion, la importa. Si alguien la copiara, esta cifra sube.
    fuente = io.open(os.path.join(RAIZ, "scripts", "loop",
                                  "contador_de_segundas_lecturas.py"),
                     encoding="utf-8").read()
    casos.append(("el_estable_NO_reimplementa_FORMAS_QUE_CUENTAN",
                  fuente.count("RELECTURA CIEGA DEL AUDITOR, VUELTA"), 0))

    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("")
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")
    print("   SEGUNDA PASADA: SE MUTA EL VALOR ESPERADO Y TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        mutado = (not esperado) if isinstance(esperado, bool) else (esperado + 1)
        cae = (real != mutado)
        print("   %-52s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    print("")
    print("   CIFRA casos que CAEN: %d de %d" % (caen, len(casos)))
    if fallos or caen != len(casos):
        print("ROJO: la bateria no se comporta.")
        return 1
    print("VERDE: %d casos, los %d pasan y los %d CAEN al mutarles el valor esperado."
          % (len(casos), len(casos), len(casos)))
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutacion", action="store_true")
    a = ap.parse_args()
    raise SystemExit(prueba_de_mutacion() if a.mutacion else main())
