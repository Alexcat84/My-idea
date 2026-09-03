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
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
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

# LA VARA QUE EL ENCARGO ESCRIBE CON SUS NUMEROS. Va aqui para que el cotejo
# pueda CAER, y su prueba de mutacion la muta para comprobar que cae.
VARA_DEL_ENCARGO = {
    "con al menos una": 92,
    "con dos o mas": 16,
    "con ninguna": 30,
    "actos sobre filas": 115,
    "tipos de acto": 8,
}


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

    print("C) LAS CINCO CIFRAS, COTEJADAS CONTRA LA VARA DEL ENCARGO Y ENTRE SI")
    fallos = []
    for nombre, _p in CIFRAS:
        valores = [cif[nombre] for _e, _r, _c, _s, cif in resultados]
        iguales = len(set(valores)) == 1
        contra_vara = valores[0] == VARA_DEL_ENCARGO[nombre]
        print("   %-20s %s  | iguales en los tres: %-5s | vara del encargo %d: %s"
              % (nombre, valores, iguales, VARA_DEL_ENCARGO[nombre],
                 "CALZA" if contra_vara else "NO CALZA"))
        if not iguales or not contra_vara:
            fallos.append(nombre)
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
    casos = []
    for nombre, _p in CIFRAS:
        valores = [cif[nombre] for _e, _r, _c, _s, cif in resultados]
        casos.append(("los_tres_dan_lo_mismo_en_%s" % nombre.replace(" ", "_"),
                      len(set(valores)), 1))
        casos.append(("la_vara_del_encargo_en_%s" % nombre.replace(" ", "_"),
                      valores[0], VARA_DEL_ENCARGO[nombre]))
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
