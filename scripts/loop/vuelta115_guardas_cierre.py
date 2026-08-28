# -*- coding: utf-8 -*-
r"""vuelta115_guardas_cierre.py . Re-corre, EN ESTA VUELTA, la nomina fija de
las VEINTISEIS mutaciones heredadas de la vuelta 113 (A-M, Q, R, S, T, U,
TAREA2.4-v109, N, O, P, V, W, mas X embebida), MAS DOS NUEVAS: Y (el barrido
de la TAREA 2.1 de la vuelta 114 corrido con --sin-exclusion, verificado por
su PROPIEDAD y no por un exit fijo) y Z_SONDA (el caso de control de la
TAREA 2.3/2.4 de esta vuelta, ver MUTACION Z en
scripts/loop/vuelta115_tarea2_4_mutacion_z.py), mas los NUEVE instrumentos
(los mismos ocho de la vuelta 113 con su --vuelta actualizado a 115).

POR QUE NACE LA CAPA DE MOTIVO (TAREA 2.3, encargo de la vuelta 115, que
remedia la caida A.2 del acta 113: "LA CITA QUE PROMETE DETALLE Y NO LO
TIENE"). El reporte 113 afirmo que el vuelco del caso T estaba "declarado con
el detalle completo" en la salida de guardas, y esa salida solo traia el
EXIT y la palabra CALZA: el motivo real vivia en un comentario del codigo y
en el mensaje de commit, dos sitios que la cita no nombraba. Desde esta
vuelta, cada caso lleva, ademas de su `esperado` de siempre, un
`ESPERADO_BASE` (el esperado ORIGINAL, antes de cualquier vuelco declarado) y
un `MOTIVOS` opcional: si `esperado` de hoy es DISTINTO de `ESPERADO_BASE`, la
SALIDA imprime una linea "MOTIVO: ..." cuando el vuelco esta en `MOTIVOS`, o
una linea "ALERTA: ESPERADO CAMBIADO SIN MOTIVO DECLARADO" (que ROMPE la
guarda, aunque el caso individual calce) cuando no lo esta. EMPIEZA POR T,
que arrastra su motivo desde la vuelta 113 (acta 113, seccion 4.4: el
esperado paso de 0 a 1 porque el reporte 111, linea 30, trae una afirmacion
de permanencia sin cita, hallazgo real destapado por la extension de MARCAS
con "sigue" en la TAREA 2.4 de la 113).

MUTACION Z (TAREA 2.4, scripts/loop/vuelta115_tarea2_4_mutacion_z.py) prueba
esta capa por el LADO ROJO: una copia de este fichero con el esperado del
caso Z_SONDA cambiado (y su comportamiento real mutado para que SIGA
CALZANDO a simple vista) pero SIN anadir su vuelco a MOTIVOS tiene que dar
ROJO con la ALERTA nombrando el caso, no "CALZA" en silencio.

USO:
  python scripts/loop/vuelta115_guardas_cierre.py
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PY = sys.executable


def correr(args):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([PY] + args, cwd=RAIZ, capture_output=True, env=env)
    out = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    return r.returncode, out


CASOS = [
    ("A", ["scripts/loop/tallar_veredictos_reporte.py", "--reporte", "docs/loop/_auditor_v104_mut_A.md"], 1),
    ("B", ["scripts/loop/tallar_veredictos_reporte.py", "--reporte", "docs/loop/_auditor_v104_mut_B.md"], 1),
    ("C", ["scripts/loop/tallar_veredictos_reporte.py", "--reporte", "docs/loop/_auditor_v104_mut_C.md"], 1),
    ("D", ["scripts/loop/tallar_veredictos_reporte.py", "--reporte", "docs/loop/_auditor_v105_mut_D.md"], 0),
    ("E", ["scripts/loop/tallar_veredictos_reporte.py", "--reporte", "docs/loop/_auditor_v105_mut_E.md"], 1),
    ("F", ["scripts/loop/tallar_veredictos_reporte.py", "--reporte", "docs/loop/_auditor_v105_mut_F.md"], 1),
    ("G", ["scripts/loop/tallar_veredictos_reporte.py", "--reporte", "docs/loop/_auditor_v106_mut_G.md"], 1),
    ("H", ["scripts/loop/tallar_veredictos_reporte.py", "--reporte", "docs/loop/_auditor_v106_mut_H.md"], 0),
    ("griton (reporte 102, f253842b)", ["scripts/loop/tallar_veredictos_reporte.py", "--reporte", "docs/loop/REPORTE.md", "--commit", "f253842b"], 0),
    ("I (mI.md, cabecera pegada/condensada v107)", ["scripts/loop/verificar_cabecera_pegada_o_condensada.py", "--vuelta", "107", "--reporte", "docs/loop/_auditor_v107_mut/mI.md"], 1),
    ("J (mJ.md, tallar_cabecera --comparar v107)", ["scripts/loop/tallar_cabecera_reporte.py", "--fase04", "--vuelta", "107", "--comparar", "docs/loop/_auditor_v107_mut/mJ.md"], 1),
    ("K (mK.md, mismo tallador v107)", ["scripts/loop/tallar_cabecera_reporte.py", "--fase04", "--vuelta", "107", "--comparar", "docs/loop/_auditor_v107_mut/mK.md"], 1),
    ("L (mL.md, mismo tallador v107)", ["scripts/loop/tallar_cabecera_reporte.py", "--fase04", "--vuelta", "107", "--comparar", "docs/loop/_auditor_v107_mut/mL.md"], 1),
    ("M (mM.md, cabecera pegada/condensada v108)", ["scripts/loop/verificar_cabecera_pegada_o_condensada.py", "--vuelta", "108", "--reporte", "docs/loop/_auditor_v108_mut/mM.md"], 1),
    ("Q (reporte 110 real, git show 27ecfe43)", ["scripts/loop/tallar_cifras_de_antes.py", "--fichero", "docs/loop/_v111_mut/reporte_110.md"], 1),
    ("R (reporte 110, cita quitada al caso N)", ["scripts/loop/tallar_cifras_de_antes.py", "--fichero", "docs/loop/_v111_mut/reporte_110_mut_casoN.md"], 1),
    ("S (sonda de backticks, DESPUES del arreglo)", ["scripts/loop/tallar_cifras_de_antes.py", "--fichero", "docs/loop/_auditor_v111_mut/sonda_backticks.md"], 0),
    ("T (reporte 111 real, git show 9aea9f43)", ["scripts/loop/tallar_cifras_de_antes.py", "--fichero", "docs/loop/_v112_tarea2_mut/reporte_111_9aea9f43.md"], 1),
    ("U (censo por las dos reglas, 72/2 vs 70/4)", ["scripts/loop/vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py"], 0),
    ("V (tsc solo EXIT=0, celda LIMPIA)", ["scripts/loop/vuelta113_tarea2_mutacion_tsc.py", "--solo", "V"], 0),
    ("W (tsc con una linea de error real, celda DISTINTA)", ["scripts/loop/vuelta113_tarea2_mutacion_tsc.py", "--solo", "W"], 0),
    # Z_SONDA: caso de control, ver docstring "MUTACION Z" arriba. En el
    # fichero REAL (no mutado) su comportamiento es fijo y silencioso.
    ("Z_SONDA (control 2.3/2.4)", ["-c", "import sys; sys.exit(0)"], 0),
]

# ESPERADO_BASE: el esperado ORIGINAL de cada caso, antes de cualquier vuelco
# declarado. Para casi todos, IGUAL al esperado de arriba (nunca cambiaron).
# T es la excepcion viva (paso de 0 a 1 en la vuelta 113, acta 113 4.4).
# ESPERADO_BASE es un LITERAL FIJO, escrito a mano, DELIBERADAMENTE NO
# DERIVADO de CASOS: si se derivara de CASOS (p.ej. con un dict comprehension
# sobre la misma lista), una mutacion que cambia el esperado de un caso en
# CASOS cambiaria SU PROPIO ancla al mismo tiempo y la ALERTA nunca podria
# dispararse (el mismo boquete, en espejo, que TAREA 2.4 viene a probar que
# NO existe). El ancla vive SEPARADA a proposito.
NOMBRE_T = "T (reporte 111 real, git show 9aea9f43)"
ESPERADO_BASE = {
    "A": 1, "B": 1, "C": 1, "D": 0, "E": 1, "F": 1, "G": 1, "H": 0,
    "griton (reporte 102, f253842b)": 0,
    "I (mI.md, cabecera pegada/condensada v107)": 1,
    "J (mJ.md, tallar_cabecera --comparar v107)": 1,
    "K (mK.md, mismo tallador v107)": 1,
    "L (mL.md, mismo tallador v107)": 1,
    "M (mM.md, cabecera pegada/condensada v108)": 1,
    "Q (reporte 110 real, git show 27ecfe43)": 1,
    "R (reporte 110, cita quitada al caso N)": 1,
    "S (sonda de backticks, DESPUES del arreglo)": 0,
    NOMBRE_T: 0,  # arrastra el motivo desde la vuelta 113 (paso de 0 a 1)
    "U (censo por las dos reglas, 72/2 vs 70/4)": 0,
    "V (tsc solo EXIT=0, celda LIMPIA)": 0,
    "W (tsc con una linea de error real, celda DISTINTA)": 0,
    "Z_SONDA (control 2.3/2.4)": 0,
}

MOTIVOS = {
    NOMBRE_T: ("esperado paso de 0 a 1 en la vuelta 113 (acta 113 seccion 4.4): el "
          "reporte 111, linea 30, trae \"verificar_cobertura_bolsa_tres_vias.py "
          "sigue 74/74/0\" SIN NINGUNA CITA, hallazgo real y mas viejo que la "
          "vuelta, destapado por la extension de MARCAS con el verbo \"sigue\" "
          "en la TAREA 2.4 de la propia vuelta 113."),
}

CASO_TAREA24_109 = ("TAREA2.4-v109 (123 sin declaracion)",
                     "docs/loop/_v109_mut/TRAMO3_SIN_DECLARACION_123.md")

CASOS_OVERRIDE = [
    ("N", "docs/loop/_auditor_v109_mut/tramo2_sin_decl_87.md", "SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md", 87, "en_sitio"),
    ("O", "docs/loop/_auditor_v109_mut/tramo2_sin_decl_91.md", "SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md", 91, "cruce"),
    ("P", "docs/loop/_auditor_v110_mut/v106_sin_decl_154.txt", "SALIDA_V106_TAREA4_3_TRES_VIAS.txt", 154, "en_sitio"),
]

INSTRUMENTOS = [
    ("2. tallar_nombre_de_operacion.py OP-E-03",
     ["scripts/loop/tallar_nombre_de_operacion.py", "OP-E-03"], 0),
    ("3. verificar_apertura_sellada.py --vuelta 115",
     ["scripts/loop/verificar_apertura_sellada.py", "--vuelta", "115"], 0),
    ("4. verificar_cabecera_pegada_o_condensada.py --vuelta 115",
     ["scripts/loop/verificar_cabecera_pegada_o_condensada.py", "--vuelta", "115"], 0),
    ("5. verificar_cobertura_bolsa_tres_vias.py",
     ["scripts/loop/verificar_cobertura_bolsa_tres_vias.py"], 0),
    ("6. contar_cierre_efectivo.py",
     ["scripts/loop/contar_cierre_efectivo.py"], 0),
    ("7. verificar_vuelco_de_veredicto.py",
     ["scripts/loop/verificar_vuelco_de_veredicto.py"], 0),
    ("8. tallar_cabecera_reporte.py --fase04 --vuelta 115 --comparar REPORTE.md",
     ["scripts/loop/tallar_cabecera_reporte.py", "--fase04", "--vuelta", "115",
      "--comparar", "docs/loop/REPORTE.md"], 0),
    ("9. tallar_cifras_de_antes.py (sobre el propio REPORTE.md)",
     ["scripts/loop/tallar_cifras_de_antes.py"], 0),
]


def caso_x():
    codigo, out = correr(["scripts/loop/tallar_cifras_de_antes.py", "--fichero",
                          "docs/loop/_v113_mut_x/reporte_112.md"])
    dos_marcadas = out.count("sigue") >= 2
    ok = (codigo == 1) and dos_marcadas
    return ok, codigo, out


def caso_y():
    """Y (TAREA 2.2 de la vuelta 114, re-verificada aqui como guarda del
    cierre): la PROPIEDAD del barrido, no un exit fijo (letra del encargo de
    la 115, seccion GUARDAS). Corre el barrido CON exclusion (default) y SIN
    exclusion (--sin-exclusion) y comprueba:
      con exclusion: crudo != neto en al menos una busqueda, y la seccion
        EXCLUSIONES nombra el fichero excluido con su motivo (no dice
        NINGUNA).
      sin exclusion: crudo == neto en las tres busquedas, y la seccion
        EXCLUSIONES dice NINGUNA (el fichero antes excluido permanece).
    Devuelve (ok, texto_absolutos_para_el_reporte)."""
    script = "scripts/loop/vuelta114_tarea2_1_barrido_talladores.py"
    cod_con, out_con = correr([script])
    cod_sin, out_sin = correr([script, "--sin-exclusion"])
    out_con = out_con.replace("\r\n", "\n")
    out_sin = out_sin.replace("\r\n", "\n")

    ok = cod_con == 0 and cod_sin == 0
    ok = ok and "Crudo != neto en al menos una busqueda: True" in out_con
    ok = ok and "EXCLUSIONES ---\nvuelta114_tarea2_1_barrido_talladores.py:" in out_con
    ok = ok and "Crudo == neto: True" in out_sin
    ok = ok and "EXCLUSIONES ---\nNINGUNA" in out_sin

    def _absolutos(out):
        vals = []
        for linea in out.splitlines():
            l = linea.strip()
            if l.startswith("RECUENTO NETO"):
                vals.append(int(l.rsplit(":", 1)[1].strip()))
        union = None
        for linea in out.splitlines():
            if linea.startswith("UNION crudo"):
                union = linea.strip()
        return vals, union

    netos_con, union_con = _absolutos(out_con)
    resumen = ("con exclusion: netos %s, %s | sin exclusion (=crudo): netos %s"
               % (netos_con, union_con, _absolutos(out_sin)[0]))
    return ok, resumen, out_con, out_sin


def imprimir_caso(nombre, args, esperado, fallos):
    codigo, _out = correr(args)
    calza = codigo == esperado
    print("%s -- EXIT %d (esperado %d) [%s]" % (nombre, codigo, esperado, "CALZA" if calza else "NO CALZA"))
    if not calza:
        fallos.append(nombre)
    base = ESPERADO_BASE.get(nombre)
    if base is not None and base != esperado:
        if nombre in MOTIVOS:
            print("   MOTIVO: %s" % MOTIVOS[nombre])
        else:
            print("   ALERTA: ESPERADO CAMBIADO SIN MOTIVO DECLARADO (base %d, actual %d)" % (base, esperado))
            fallos.append("%s (esperado sin motivo)" % nombre)


def main():
    print("GUARDAS DEL CIERRE, VUELTA 115: NUEVE INSTRUMENTOS Y VEINTIOCHO CASOS DE MUTACION.")
    print("=" * 100)
    fallos = []

    for nombre, args, esperado in CASOS:
        imprimir_caso(nombre, args, esperado, fallos)

    ok_x, codigo_x, _out_x = caso_x()
    print("X (reporte 112 por git show 87397be1, marca las dos con \"sigue\") -- EXIT %d [%s]"
          % (codigo_x, "CALZA" if ok_x else "NO CALZA"))
    if not ok_x:
        fallos.append("X")

    ok_y, resumen_y, _out_con, _out_sin = caso_y()
    print("Y (barrido 114 --sin-exclusion, verificado por PROPIEDAD) -- [%s] :: %s"
          % ("CALZA" if ok_y else "NO CALZA", resumen_y))
    if not ok_y:
        fallos.append("Y")

    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_vuelco_de_veredicto as vvv

    ruta_mut = os.path.join(RAIZ, CASO_TAREA24_109[1])
    overrides = {"SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md": ruta_mut}
    f2, vuelcos2 = vvv.verificar(overrides=overrides)
    ok_123_mudo = False
    if not f2:
        v123 = [v for v in vuelcos2 if v["puesto"] == 123]
        ok_123_mudo = bool(v123) and not v123[0]["declarado"]
    print("%s -- 123 %s [%s]" % (CASO_TAREA24_109[0], "MUDO" if ok_123_mudo else "no-mudo",
                                  "CALZA" if ok_123_mudo else "NO CALZA"))
    if not ok_123_mudo:
        fallos.append(CASO_TAREA24_109[0])

    for letra, archivo, fichero_real, puesto, tipo_esperado in CASOS_OVERRIDE:
        ruta = os.path.join(RAIZ, archivo)
        f3, vuelcos3 = vvv.verificar(overrides={fichero_real: ruta})
        ok = False
        if not f3:
            vs = [v for v in vuelcos3 if v["puesto"] == puesto and v["tipo"] == tipo_esperado]
            ok = bool(vs) and not vs[0]["declarado"]
        print("%s (%s) -- %d %s MUDO [%s]" % (letra, os.path.basename(archivo), puesto, tipo_esperado,
                                               "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos.append(letra)

    total_casos = len(CASOS) + 1 + 1 + 1 + len(CASOS_OVERRIDE)  # CASOS(incl. Z_SONDA) + X + Y + TAREA2.4-v109 + N,O,P
    print()
    print("%d en CASOS (A-M,Q,R,S,T,U,V,W,Z_SONDA) + X + Y + TAREA2.4-v109 + N,O,P = %d."
          % (len(CASOS), total_casos))
    print()
    print("LOS NUEVE INSTRUMENTOS:")
    for nombre, args, esperado in INSTRUMENTOS:
        codigo, out = correr(args)
        calza = codigo == esperado
        primera = next((l for l in out.splitlines() if l.strip()), "")
        print("%s -- EXIT %d (esperado %d) [%s] :: %s" % (nombre, codigo, esperado,
                                                            "CALZA" if calza else "NO CALZA", primera[:120]))
        if not calza:
            fallos.append(nombre)

    print()
    if fallos:
        print("ROJO: %d caso(s) NO CALZAN: %s" % (len(fallos), ", ".join(fallos)))
        return 1
    print("VERDE: los VEINTIOCHO casos de mutacion y los NUEVE instrumentos calzan.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
