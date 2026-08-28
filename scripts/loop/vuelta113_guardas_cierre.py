# -*- coding: utf-8 -*-
r"""vuelta113_guardas_cierre.py . Re-corre, EN ESTA VUELTA, la nomina fija de
las VEINTITRES mutaciones heredadas de la vuelta 112 (A-M, Q, R, S, T, U,
TAREA2.4-v109, N, O, P) y confirma que cada una sigue dando el resultado que
NO PUEDE CAMBIAR, MAS las TRES que nacen en la TAREA 2 de esta vuelta (V, el
tsc con solo el marcador, celda LIMPIA; W, el tsc con una linea de error
real, celda DISTINTA; X, el reporte 112 por git show 87397be1, que despues
del arreglo MARCA las dos oraciones con "sigue"), mas los NUEVE instrumentos
(los mismos ocho de la vuelta 112 con su --vuelta actualizado a 113, mas
tallar_cifras_de_antes.py sobre el propio reporte, YA CON LA LISTA DE MARCAS
CONVERTIDA EN REGLA).

USO:
  python scripts/loop/vuelta113_guardas_cierre.py
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
    # T CAMBIA DE ESPERADO EN ESTA VUELTA (0 -> 1), DECLARADO Y NO CALLADO:
    # el reporte 111 tiene, linea 30, "`verificar_cobertura_bolsa_tres_vias.py`
    # sigue 74/74/0." SIN NINGUNA CITA: la MISMA especie de caida que motivo
    # la TAREA 2.4 de esta vuelta (el "sigue" del reporte 112), solo que mas
    # vieja y nunca vista porque "sigue" no estaba en MARCAS hasta ahora. El
    # esperado de T se fijo en la vuelta 112 ANTES de que la TAREA 2.4 de la
    # 113 extendiera MARCAS: extenderla es el mandato explicito de esta
    # vuelta, y encontrar un hallazgo real y nuevo en un reporte historico no
    # es una caida de esta guarda, es la guarda funcionando mejor. Hallazgo
    # nombrado en el reporte de esta vuelta, TAREA 2.4.
    ("T (reporte 111 real, git show 9aea9f43)", ["scripts/loop/tallar_cifras_de_antes.py", "--fichero", "docs/loop/_v112_tarea2_mut/reporte_111_9aea9f43.md"], 1),
    ("U (censo por las dos reglas, 72/2 vs 70/4)", ["scripts/loop/vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py"], 0),
    # LAS TRES QUE NACEN EN LA TAREA 2 DE ESTA VUELTA (113)
    ("V (tsc solo EXIT=0, celda LIMPIA)", ["scripts/loop/vuelta113_tarea2_mutacion_tsc.py", "--solo", "V"], 0),
    ("W (tsc con una linea de error real, celda DISTINTA)", ["scripts/loop/vuelta113_tarea2_mutacion_tsc.py", "--solo", "W"], 0),
]

CASO_TAREA24_109 = ("TAREA2.4-v109 (123 sin declaracion)",
                     "docs/loop/_v109_mut/TRAMO3_SIN_DECLARACION_123.md")

CASOS_OVERRIDE = [
    ("N", "docs/loop/_auditor_v109_mut/tramo2_sin_decl_87.md", "SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md", 87, "en_sitio"),
    ("O", "docs/loop/_auditor_v109_mut/tramo2_sin_decl_91.md", "SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md", 91, "cruce"),
    ("P", "docs/loop/_auditor_v110_mut/v106_sin_decl_154.txt", "SALIDA_V106_TAREA4_3_TRES_VIAS.txt", 154, "en_sitio"),
]

# LOS NUEVE INSTRUMENTOS DEL ENCARGO, --vuelta actualizado a 113. El
# INSTRUMENTO #1 (tallar_veredictos_reporte.py sobre el propio reporte) NO se
# embebe aqui: se muerde la cola. Corre APARTE, al final, sobre
# SALIDA_V113_GUARDAS_CIERRE.txt.
INSTRUMENTOS = [
    ("2. tallar_nombre_de_operacion.py OP-E-03",
     ["scripts/loop/tallar_nombre_de_operacion.py", "OP-E-03"], 0),
    ("3. verificar_apertura_sellada.py --vuelta 113",
     ["scripts/loop/verificar_apertura_sellada.py", "--vuelta", "113"], 0),
    ("4. verificar_cabecera_pegada_o_condensada.py --vuelta 113",
     ["scripts/loop/verificar_cabecera_pegada_o_condensada.py", "--vuelta", "113"], 0),
    ("5. verificar_cobertura_bolsa_tres_vias.py",
     ["scripts/loop/verificar_cobertura_bolsa_tres_vias.py"], 0),
    ("6. contar_cierre_efectivo.py",
     ["scripts/loop/contar_cierre_efectivo.py"], 0),
    ("7. verificar_vuelco_de_veredicto.py",
     ["scripts/loop/verificar_vuelco_de_veredicto.py"], 0),
    ("8. tallar_cabecera_reporte.py --fase04 --vuelta 113 --comparar REPORTE.md",
     ["scripts/loop/tallar_cabecera_reporte.py", "--fase04", "--vuelta", "113",
      "--comparar", "docs/loop/REPORTE.md"], 0),
    ("9. tallar_cifras_de_antes.py (sobre el propio REPORTE.md, lista de marcas ya regla)",
     ["scripts/loop/tallar_cifras_de_antes.py"], 0),
]


def caso_x():
    """MUTACION X (TAREA 2.5): el reporte 112 real (git show 87397be1) tiene
    que MARCAR las dos oraciones con "sigue" (una con vara VERDE, otra ROJO
    por falta de cita: se declara tal cual sale, EXIT 1 en total). El caso
    calza si el EXIT es 1 (no 0, que seria el ANTES vacuo) Y las dos
    oraciones aparecen nombradas en la salida."""
    ruta = os.path.join(RAIZ, "docs", "loop", "_v113_mut_x", "reporte_112.md")
    codigo, out = correr(["scripts/loop/tallar_cifras_de_antes.py", "--fichero",
                          "docs/loop/_v113_mut_x/reporte_112.md"])
    dos_marcadas = out.count("sigue") >= 2
    ok = (codigo == 1) and dos_marcadas
    return ok, codigo, out


def main():
    print("GUARDAS DEL CIERRE, VUELTA 113: NUEVE INSTRUMENTOS Y VEINTISEIS CASOS DE MUTACION.")
    print("=" * 100)
    fallos = []

    for nombre, args, esperado in CASOS:
        codigo, _out = correr(args)
        calza = codigo == esperado
        print("%s -- EXIT %d (esperado %d) [%s]" % (nombre, codigo, esperado, "CALZA" if calza else "NO CALZA"))
        if not calza:
            fallos.append(nombre)

    ok_x, codigo_x, _out_x = caso_x()
    print("X (reporte 112 por git show 87397be1, marca las dos con \"sigue\") -- EXIT %d [%s]"
          % (codigo_x, "CALZA" if ok_x else "NO CALZA"))
    if not ok_x:
        fallos.append("X")

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

    total_casos = len(CASOS) + 1 + 1 + len(CASOS_OVERRIDE)  # CASOS(incl. V,W) + X + TAREA2.4-v109 + N,O,P
    print()
    print("%d mutaciones en CASOS (A-M,Q,R,S,T,U,V,W) + X + TAREA2.4-v109 + N,O,P = %d."
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
    print("VERDE: los VEINTISEIS casos de mutacion y los NUEVE instrumentos calzan.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
