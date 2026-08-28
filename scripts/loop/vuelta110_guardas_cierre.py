# -*- coding: utf-8 -*-
r"""vuelta110_guardas_cierre.py . Re-corre, EN ESTA VUELTA, la nomina fija
de las diecisiete mutaciones del cierre (EJECUTOR.md/encargo de la vuelta
110: "LAS GUARDAS DEL CIERRE") y confirma que cada una sigue dando el
resultado que NO PUEDE CAMBIAR. No inventa comandos: cada caso usa el
MISMO instrumento y el MISMO --vuelta (historico, cuando aplica) con el
que se establecio la primera vez.

USO:
  python scripts/loop/vuelta110_guardas_cierre.py
"""
import io
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
]

# TAREA2.4 de la vuelta 109 (123 DECLARADO -> MUDO al borrar su declaracion,
# via overrides, sobre el script de HOY que ya trae la TAREA 2/4 de la 110)
CASO_TAREA24_109 = ("TAREA2.4-v109 (123 sin declaracion)",
                     "docs/loop/_v109_mut/TRAMO3_SIN_DECLARACION_123.md")

INSTRUMENTOS_ADICIONALES = [
    ("tallar_nombre_de_operacion.py OP-E-03", ["scripts/loop/tallar_nombre_de_operacion.py", "OP-E-03"], 0),
    ("verificar_cobertura_bolsa_tres_vias.py", ["scripts/loop/verificar_cobertura_bolsa_tres_vias.py"], 0),
    ("contar_cierre_efectivo.py", ["scripts/loop/contar_cierre_efectivo.py"], 0),
    ("verificar_apertura_sellada.py --vuelta 110", ["scripts/loop/verificar_apertura_sellada.py", "--vuelta", "110"], 0),
    ("verificar_vuelco_de_veredicto.py", ["scripts/loop/verificar_vuelco_de_veredicto.py"], 0),
]


def main():
    print("GUARDAS DEL CIERRE, VUELTA 110: OCHO INSTRUMENTOS Y DIECISIETE CASOS DE MUTACION.")
    print("=" * 100)
    fallos = []

    for nombre, args, esperado in CASOS:
        codigo, _out = correr(args)
        calza = codigo == esperado
        print("%s -- EXIT %d (esperado %d) [%s]" % (nombre, codigo, esperado, "CALZA" if calza else "NO CALZA"))
        if not calza:
            fallos.append(nombre)

    # TAREA2.4 de la vuelta 109, sobre el script de HOY (via harness de overrides)
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

    # N y O (nuevas desde la vuelta 110, TAREA 2.4/2.5): re-verificadas aqui tambien
    for letra, archivo, puesto, tipo_esperado in [
        ("N", "docs/loop/_auditor_v109_mut/tramo2_sin_decl_87.md", 87, "en_sitio"),
        ("O", "docs/loop/_auditor_v109_mut/tramo2_sin_decl_91.md", 91, "cruce"),
    ]:
        ruta = os.path.join(RAIZ, archivo)
        f3, vuelcos3 = vvv.verificar(overrides={"SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md": ruta})
        ok = False
        if not f3:
            vs = [v for v in vuelcos3 if v["puesto"] == puesto and v["tipo"] == tipo_esperado]
            ok = bool(vs) and not vs[0]["declarado"]
        print("%s (%s) -- %d %s MUDO [%s]" % (letra, os.path.basename(archivo), puesto, tipo_esperado,
                                               "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos.append(letra)

    total_casos = len(CASOS) + 1 + 2  # CASOS (A..M) + TAREA2.4-v109 + N + O
    print()
    print("%d mutaciones heredadas (A-M) + TAREA2.4-v109 + N + O = %d." % (len(CASOS), total_casos))
    print()
    print("INSTRUMENTOS ADICIONALES (fuera de la tabla de mutacion):")
    for nombre, args, esperado in INSTRUMENTOS_ADICIONALES:
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
    print("VERDE: los DIECISIETE casos de mutacion y los CINCO instrumentos adicionales calzan.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
