# -*- coding: utf-8 -*-
"""_v199_parche_t1.py . PARCHE DE UN SOLO USO sobre el arnes de la TAREA 1 de la
vuelta 199, para aislar cada mutacion donde de verdad se ve. Se declara como
parche y no como instrumento: no entra en ninguna nomina y no lo cita nadie."""
import io
import os

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
p = os.path.join(RAIZ, "scripts", "loop",
                 "vuelta199_tarea1_mutacion_guardas_revividas.py")
s = io.open(p, encoding="utf-8").read()


def sub(v, n):
    global s
    assert s.count(v) == 1, (s.count(v), v[:80])
    s = s.replace(v, n)


sub("""LAS TRES MUTACIONES, UNA POR REMEDIO:
  A) `_cargar_turno()` deja de reabrir el turno consumido  -> muere la `1.a` de carga
  B) `sellar()` deja de reabrir el turno                   -> muere la `1.a` de sello
  C) `sello_mas_reciente_en_disco()` devuelve vacio        -> muere la `1.b`
""",
    """LAS TRES MUTACIONES, UNA POR REMEDIO:
  A) `_cargar_turno()` deja de reabrir el turno consumido  -> muere la `1.a` de carga
  B) `_apuntar_sello()` deja de reabrir el turno           -> muere la `1.a` de sello
  C) `sello_mas_reciente_en_disco()` devuelve vacio        -> muere la `1.b`

Y CADA MUTACION SE MIDE DONDE DE VERDAD SE VE, QUE ES UNA COSA QUE ESTE ARNES
APRENDIO EN ROJO Y VA ESCRITA PORQUE ES LA MITAD QUE LO HACE VALER:

  . LA `B` NO SE VE SOLA. Con la `A` puesta, `_cargar_turno()` ya reabre el turno
    antes de que `_apuntar_sello()` llegue, asi que quitarle a la cola del sello
    su linea NO CAMBIA NADA MEDIBLE. Se mide contra la `A` YA QUITADA: `mut_A`
    (solo A) contra `mut_AB` (A y B). Un remedio que solo se ve cuando el otro
    falta SIGUE SIENDO un remedio, pero decir que se prueba solo seria falso.
  . LA `C` NO SE VE EN EL ESCENARIO LARGO, y por el motivo simetrico: con la `A`
    puesta el sello SOBREVIVE EN MEMORIA, y `puede_leer_reporte()` cae en rojo por
    la memoria antes de llegar a mirar el disco. Se mide en su ESCENARIO PROPIO,
    que es ademas el estado exacto que el auditor de la 198 se encontro: turno
    CERRADO, memoria en blanco, y EL SELLO EN EL DISCO, AL LADO.
""")

sub('''    esperados_por_mutacion = {
        "A": [("1.a la bitacora ya NO acumula",
               lambda x: x.get("bitacora") != esperado_bit),
              ("1.a `sellar()` ya NO ve ningun prohibido",
               lambda x: x.get("toques_prohibidos") == []),
              ("1.a un toque anterior al sello ya NO cierra `puede_sellar()`",
               lambda x, p=None: True)],
        "B": [("1.a el sello ya NO sobrevive al proceso siguiente",
               lambda x: x.get("sellado_en_memoria") is False)],
        "C": [("1.b `leer_reporte()` SIN vuelta ya DEJA PASAR",
               lambda x: (x.get("puede_leer_sin_vuelta") or [None])[0] is True)],
    }
    for nombre, d_mut in dirs_mutados:
        letra = nombre[:1]
        pre_m, dm, _b, _t = escenario(d_mut, "mut_%s" % letra)
        w("   MUTACION %s" % nombre)
        w("      bitacora: %s | sellado: %s | prohibidos: %s"
          % (dm.get("bitacora"), dm.get("sellado_en_memoria"),
             dm.get("toques_prohibidos")))
        w("      puede_leer SIN vuelta: %s"
          % ((dm.get("puede_leer_sin_vuelta") or [None])[0],))
        if letra == "A":
            caso("MUTACION A: la bitacora ya NO acumula entre procesos",
                 dm.get("bitacora") != esperado_bit,
                 "bitacora con la mutacion: %s" % dm.get("bitacora"))
            caso("MUTACION A: un toque anterior al sello ya NO cierra el sello",
                 (pre_m.get("puede_sellar") or [None])[0] is True,
                 "puede_sellar con la mutacion: %s"
                 % ((pre_m.get("puede_sellar") or [None])[0],))
        if letra == "B":
            caso("MUTACION B: el sello ya NO sobrevive al proceso siguiente",
                 dm.get("sellado_en_memoria") is False,
                 "sellado con la mutacion: %s" % dm.get("sellado_en_memoria"))
        if letra == "C":
            caso("MUTACION C: `leer_reporte()` SIN vuelta ya DEJA PASAR",
                 (dm.get("puede_leer_sin_vuelta") or [None])[0] is True,
                 "motivo con la mutacion: %s"
                 % (dm.get("puede_leer_sin_vuelta") or [None, ""])[1][:88])''',
    '''    por_letra = dict((n[:1], d) for n, d in dirs_mutados)

    # MUTACION A, EN EL ESCENARIO LARGO: es la que se ve sola y entera.
    pre_a, da, _b, _t = escenario(por_letra["A"], "mut_A")
    w("   MUTACION A (solo A)")
    w("      bitacora: %s | sellado: %s | prohibidos: %s"
      % (da.get("bitacora"), da.get("sellado_en_memoria"),
         da.get("toques_prohibidos")))
    caso("MUTACION A: la bitacora ya NO acumula entre procesos",
         da.get("bitacora") != esperado_bit,
         "bitacora con la mutacion: %s" % da.get("bitacora"))
    caso("MUTACION A: un toque anterior al sello ya NO cierra el sello",
         (pre_a.get("puede_sellar") or [None])[0] is True,
         "puede_sellar con la mutacion: %s"
         % ((pre_a.get("puede_sellar") or [None])[0],))
    w("")

    # MUTACION B, CONTRA LA `A` YA QUITADA, que es donde de verdad se ve.
    dir_ab = os.path.join(carpeta, "mut_AB")
    os.makedirs(dir_ab)
    texto_ab = original
    for _n, viejo, nuevo in MUTACIONES[:2]:
        texto_ab = texto_ab.replace(viejo, nuevo, 1)
    io.open(os.path.join(dir_ab, "apertura_del_auditor.py"), "w",
            encoding="utf-8", newline=NL).write(texto_ab)
    _pre_ab, dab, _b, _t = escenario(dir_ab, "mut_AB")
    w("   MUTACION B, MEDIDA CONTRA LA `A` YA QUITADA (mut_A contra mut_AB)")
    w("      con A quitada y B PUESTA:   sellado %s" % da.get("sellado_en_memoria"))
    w("      con A y B quitadas:         sellado %s" % dab.get("sellado_en_memoria"))
    caso("MUTACION B: con la A fuera, la B PUESTA salva el sello",
         da.get("sellado_en_memoria") is True)
    caso("MUTACION B: con la A fuera, quitar la B TIRA el sello",
         dab.get("sellado_en_memoria") is False,
         "sellado con A y B quitadas: %s" % dab.get("sellado_en_memoria"))
    w("")

    # MUTACION C, EN SU ESCENARIO PROPIO: turno CERRADO, memoria en blanco, y el
    # sello EN DISCO al lado. Es el estado exacto del auditor de la 198.
    w("   MUTACION C, EN SU ESCENARIO PROPIO (el del auditor de la 198):")
    w("      turno CERRADO, memoria en blanco, y el sello V199 EN EL DISCO.")
    base_c = os.path.join(carpeta, "base_solo_disco")
    os.makedirs(base_c)
    io.open(os.path.join(base_c, "SELLO_APERTURA_AUDITOR_V199.json"), "w",
            encoding="utf-8", newline=NL).write("{}" + NL)
    turno_solo = os.path.join(carpeta, "turno_solo_disco.json")
    escribir_turno(turno_solo, False)
    d_sano_c = estado(dir_sano, turno_solo, base_c)
    escribir_turno(turno_solo, False)
    d_mut_c = estado(por_letra["C"], turno_solo, base_c)
    w("      con el remedio:   sellado en memoria %s | puede_leer SIN vuelta %s"
      % (d_sano_c.get("sellado_en_memoria"),
         (d_sano_c.get("puede_leer_sin_vuelta") or [None])[0]))
    w("      con la mutacion:  sellado en memoria %s | puede_leer SIN vuelta %s"
      % (d_mut_c.get("sellado_en_memoria"),
         (d_mut_c.get("puede_leer_sin_vuelta") or [None])[0]))
    caso("1.b EL ESCENARIO ES EL BUENO: la memoria NO tiene sello, solo el disco",
         d_sano_c.get("sellado_en_memoria") is False)
    caso("1.b CON EL REMEDIO, `leer_reporte()` SIN vuelta CAE EN ROJO",
         (d_sano_c.get("puede_leer_sin_vuelta") or [None])[0] is False,
         "motivo: %s" % (d_sano_c.get("puede_leer_sin_vuelta") or [None, ""])[1][:88])
    caso("MUTACION C: sin el remedio, SIN vuelta DEJA PASAR (el agujero de la 198)",
         (d_mut_c.get("puede_leer_sin_vuelta") or [None])[0] is True,
         "motivo con la mutacion: %s"
         % (d_mut_c.get("puede_leer_sin_vuelta") or [None, ""])[1][:88])''')

io.open(p, "w", encoding="utf-8", newline=NL).write(s)
print("PARCHEADO: %s" % p)
