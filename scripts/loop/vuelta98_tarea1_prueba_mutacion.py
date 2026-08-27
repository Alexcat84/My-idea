# -*- coding: utf-8 -*-
r"""vuelta98_tarea1_prueba_mutacion.py . VUELTA 98, TAREA 1: PRUEBA DE MUTACION
DE LAS GUARDAS QUE ESTA VUELTA PUBLICA COMO PRUEBA.

POR QUE ES OBLIGATORIA (EJECUTOR.md regla 1, EL CASO ROJO SE PRUEBA POR
MUTACION, escrita el 29 ago 2026 a raiz de la caida 2 de la vuelta 89: alli se
publico como prueba un caso rojo que no podia fallar nunca, porque la variable
del veredicto era una constante literal y el assert comparaba "ENTRA" con
"ENTRA"). Ninguna guarda de esta vuelta se publica sin haber comprobado que CAE
cuando se le cambia el valor esperado.

QUE MUTA, y cada mutacion toca UNA sola cosa para que el veredicto no pueda
salir bien por casualidad:

  GUARDA DE FECHA (scripts/loop/vuelta97_tarea2_addendum_opE03.py:guarda_de_fecha)
    C1  control, estado real del repo                  espera VERDE CON DESFASE DECLARADO
    M1  se quita la correccion declarada de la nota    espera ROJO
    M2  la marca historica pasa a llevar la fecha
        que git devuelve hoy                           espera VERDE por igualdad
    M3  igual que M2 y ademas sin correccion en la
        nota                                           espera VERDE (no hay desfase que declarar)
    M4  git no devuelve ni un commit de la vuelta      espera ROJO
    M5  git devuelve otra fecha y no hay correccion    espera ROJO

  GUARDA DE IDEMPOTENCIA ANCLADA EN EL PARENTESIS (ancla_de)
    C2  control, la nota real de OP-E-03               espera DISPARA
    M6  nota sin el ancla del addendum                 espera NO DISPARA

  CENSO DE FECHAS (scripts/loop/vuelta98_tarea1_fechas_addenda.py)
    C3  control, el fichero real                       espera 6 IMPOSIBLE, 1 CALZA, 1 SIN FECHA
    M7  una fecha declarada mala se cambia por la
        que git devuelve                               espera esa fila en CALZA y 5 IMPOSIBLE
    M8  una fecha declarada buena se cambia por una
        posterior al techo del reloj                   espera esa fila en IMPOSIBLE y 7 IMPOSIBLE

USO:
  python scripts/loop/vuelta98_tarea1_prueba_mutacion.py

SALIDA: exit 0 si TODOS los casos salen como se espera; exit 1 si alguno no.
"""
import importlib.util
import io
import json
import os
import re
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")


def cargar(nombre):
    ruta = os.path.join(LOOP, nombre + ".py")
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = mod
    spec.loader.exec_module(mod)
    return mod


RESULTADOS = []


def caso(nombre, descripcion, esperado, obtenido):
    ok = (esperado == obtenido)
    RESULTADOS.append((nombre, descripcion, esperado, obtenido, ok))
    print("  %-4s %-58s espera %-28s obtiene %-28s %s"
          % (nombre, descripcion, esperado, obtenido, "OK" if ok else "FALLA"))
    return ok


def clasificar(fallos, diagnostico):
    if fallos:
        return "ROJO"
    if "VERDE CON DESFASE DECLARADO" in diagnostico:
        return "VERDE CON DESFASE"
    return "VERDE"


def main():
    add = cargar("vuelta97_tarea2_addendum_opE03")
    cen = cargar("vuelta98_tarea1_fechas_addenda")

    ops = [json.loads(l) for l in io.open(add.OPERACIONES, encoding="utf-8") if l.strip()]
    nota_real = [o for o in ops if o.get("id_op") == "OP-E-03"][0]["nota"]
    fecha_git = add.fecha_de_git()

    print("=" * 118)
    print("PRUEBA DE MUTACION, VUELTA 98 TAREA 1")
    print("=" * 118)
    print("DATO DE PARTIDA, leido y no supuesto:")
    print("   fecha_de_git() de la vuelta 97 = %r" % fecha_git)
    print("   fecha dentro de MARCA_APLICADA = %r"
          % add.RE_FECHA.search(add.MARCA_APLICADA).group(0))
    print("   la correccion declarada esta en la nota de OP-E-03: %s"
          % ("SI" if add.MARCA_DE_LA_CORRECCION in nota_real else "NO"))
    print()

    print("GUARDA DE FECHA")
    guardado_marca = add.MARCA_APLICADA
    guardado_fecha = add.fecha_de_git

    # C1: control, estado real
    f, d = add.guarda_de_fecha(nota_real)
    caso("C1", "control: estado real del repo", "VERDE CON DESFASE", clasificar(f, d))

    # M1: se quita la correccion declarada de la nota
    nota_sin = nota_real.replace(add.MARCA_DE_LA_CORRECCION, "XXX")
    f, d = add.guarda_de_fecha(nota_sin)
    caso("M1", "mutada la nota: sin la correccion declarada", "ROJO", clasificar(f, d))

    # M2: la marca historica pasa a llevar la fecha que git devuelve
    add.MARCA_APLICADA = add.marca_con(fecha_git)
    f, d = add.guarda_de_fecha(nota_real)
    caso("M2", "mutada la marca historica: lleva la fecha de git", "VERDE", clasificar(f, d))

    # M3: igual que M2 y ademas sin correccion en la nota
    f, d = add.guarda_de_fecha(nota_sin)
    caso("M3", "mutada la marca a la de git y la nota sin correccion", "VERDE",
         clasificar(f, d))
    add.MARCA_APLICADA = guardado_marca

    # M4: git no devuelve ni un commit de la vuelta
    add.fecha_de_git = lambda: None
    f, d = add.guarda_de_fecha(nota_real)
    caso("M4", "mutado git: no devuelve ni un commit de la vuelta 97", "ROJO",
         clasificar(f, d))

    # M5: git devuelve OTRA fecha y la nota no trae correccion
    add.fecha_de_git = lambda: "1 ene 2020"
    f, d = add.guarda_de_fecha(nota_sin)
    caso("M5", "mutada la fecha esperada de git y la nota sin correccion", "ROJO",
         clasificar(f, d))
    add.fecha_de_git = guardado_fecha

    print()
    print("GUARDA DE IDEMPOTENCIA ANCLADA EN EL PARENTESIS")
    ancla = add.ancla_de(add.MARCA_APLICADA)
    caso("C2", "control: la nota real de OP-E-03", "DISPARA",
         "DISPARA" if ancla in nota_real else "NO DISPARA")
    nota_pelada = nota_real.replace(ancla, "YYY")
    caso("M6", "mutada la nota: sin el ancla del addendum", "NO DISPARA",
         "DISPARA" if ancla in nota_pelada else "NO DISPARA")

    print()
    print("CENSO DE FECHAS")
    guardado_ops = cen.OPERACIONES

    def censar_con(texto):
        fd, tmp = tempfile.mkstemp(suffix=".jsonl")
        os.close(fd)
        io.open(tmp, "w", encoding="utf-8", newline="\n").write(texto)
        cen.OPERACIONES = tmp
        try:
            _, _, _, _, filas = cen.censar()
        finally:
            cen.OPERACIONES = guardado_ops
            os.unlink(tmp)
        c = {}
        for x in filas:
            c[x["veredicto"]] = c.get(x["veredicto"], 0) + 1
        return c, filas

    crudo = io.open(guardado_ops, encoding="utf-8").read()
    c, _ = censar_con(crudo)
    caso("C3", "control: el fichero real", "6 IMPOSIBLE / 1 CALZA / 1 SIN FECHA",
         "%d IMPOSIBLE / %d CALZA / %d SIN FECHA"
         % (c.get("IMPOSIBLE", 0), c.get("CALZA", 0), c.get("SIN FECHA", 0)))

    # M7: la fecha mala de la vuelta 97 pasa a ser la que git devuelve
    mut = crudo.replace("ADDENDUM DE EJECUCION (30 ago 2026, vuelta 97, TAREA 2)",
                        "ADDENDUM DE EJECUCION (%s, vuelta 97, TAREA 2)" % fecha_git)
    c, _ = censar_con(mut)
    caso("M7", "mutada la fecha de la vuelta 97 a la de git", "5 IMPOSIBLE / 2 CALZA",
         "%d IMPOSIBLE / %d CALZA" % (c.get("IMPOSIBLE", 0), c.get("CALZA", 0)))

    # M8: la fecha BUENA de la vuelta 96 pasa a ser posterior al techo del reloj
    mut = crudo.replace("ADDENDUM DE EJECUCION (27 ago 2026, vuelta 96, TAREA 3)",
                        "ADDENDUM DE EJECUCION (14 sep 2026, vuelta 96, TAREA 3)")
    c, _ = censar_con(mut)
    caso("M8", "mutada la fecha BUENA de la vuelta 96 a una imposible",
         "7 IMPOSIBLE / 0 CALZA",
         "%d IMPOSIBLE / %d CALZA" % (c.get("IMPOSIBLE", 0), c.get("CALZA", 0)))

    print()
    fallan = [r for r in RESULTADOS if not r[4]]
    mutaciones = [r for r in RESULTADOS if r[0].startswith("M")]
    controles = [r for r in RESULTADOS if r[0].startswith("C")]
    print("RECUENTO, contado de los propios casos corridos:")
    print("   casos totales      %d" % len(RESULTADOS))
    print("   controles          %d, verdes %d" % (len(controles),
                                                   sum(1 for r in controles if r[4])))
    print("   mutaciones         %d, se comportan como se esperaba %d"
          % (len(mutaciones), sum(1 for r in mutaciones if r[4])))
    print("   casos que FALLAN   %d" % len(fallan))
    print()
    if fallan:
        print("ROJO: %d caso(s) no se comportan como se espera." % len(fallan))
        for r in fallan:
            print("   %s %s: esperaba %r y obtuvo %r" % (r[0], r[1], r[2], r[3]))
        return 1
    print("VERDE: los %d controles pasan y las %d mutaciones mueven el veredicto. "
          "NINGUNA guarda de esta tarea es una constante que se apruebe sola."
          % (len(controles), len(mutaciones)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
