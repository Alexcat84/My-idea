# -*- coding: utf-8 -*-
r"""vuelta116_guardas_cierre.py . Re-corre, EN ESTA VUELTA, la nomina fija de
las VEINTIOCHO mutaciones de la vuelta 115 (A-M, Q, R, S, T, U,
TAREA2.4-v109, N, O, P, V, W, X embebida, Y, Z_SONDA), MAS UNA NUEVA: AA (el
control de la TAREA 2.3 de esta vuelta, ver MUTACION AA en
scripts/loop/vuelta116_tarea2_3_mutacion_aa.py), mas los NUEVE instrumentos
(los mismos ocho de la vuelta 115 con su --vuelta actualizado a 116).

POR QUE NACE LA EXTENSION DE LA CAPA DE MOTIVO (TAREA 2.1 de esta vuelta,
caida C.2 del acta 115: "LA GUARDA QUE NO ALCANZA"). La capa de motivo que
nacio en la vuelta 115 (ESPERADO_BASE + MOTIVOS) solo protegia a los
VEINTIDOS casos de la lista CASOS: los otros SEIS (X, Y, TAREA2.4-v109, N, O,
P) llevaban su esperado cableado dentro de su propia funcion, sin ancla
separada, y el reporte de la 115 daba un veredicto uniforme sobre
"veintiocho" cuando la proteccion real llegaba a veintidos. Desde esta
vuelta, los SEIS ganan su propio ancla, ESPERADO_BASE_EXTRA, exactamente con
el mismo contrato que ESPERADO_BASE: un literal FIJO, declarado APARTE del
valor que la funcion usa de verdad (ESPERADO_ACTUAL_EXTRA, o el literal
embebido en CASOS_OVERRIDE / CASO_TAREA24_109), para que una mutacion que
cambie el valor "actual" sin tocar el ancla se pueda detectar comparando los
dos. Si algun dia el ancla y el actual difieren y el nombre no esta en
MOTIVOS, la salida imprime la ALERTA y el caso se anade a fallos, IGUAL que
para los veintidos de siempre.

MUTACION AA (TAREA 2.3, scripts/loop/vuelta116_tarea2_3_mutacion_aa.py)
prueba esta extension por el LADO ROJO: una copia de este fichero con
X_MARCAS_MINIMO aflojado de 2 a 1 (SIN anadir la entrada a MOTIVOS) tiene que
seguir marcando X en [CALZA] a simple vista (la salida real de hoy trae
exactamente dos "sigue", que sigue siendo >= 1) PERO la ALERTA tiene que
nombrarlo y la guarda entera tiene que caer a ROJO. El caso "AA" que vive
AQUI ABAJO es el CONTROL: sobre el fichero REAL (sin mutar), confirma que el
ancla de X esta en silencio (CALZA, SIN alerta); la prueba de que SI se
puede mutar y caer a ROJO vive en el script de la TAREA 2.3, no aqui (mismo
reparto que Z_SONDA / Mutacion Z en la vuelta 115).

USO:
  python scripts/loop/vuelta116_guardas_cierre.py
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
    # Z_SONDA: caso de control heredado de la vuelta 115. En el fichero REAL
    # (no mutado) su comportamiento es fijo y silencioso.
    ("Z_SONDA (control 2.3/2.4 v115)", ["-c", "import sys; sys.exit(0)"], 0),
]

# ESPERADO_BASE: el esperado ORIGINAL de cada caso, antes de cualquier vuelco
# declarado. Para casi todos, IGUAL al esperado de arriba (nunca cambiaron).
# T es la excepcion viva (paso de 0 a 1 en la vuelta 113, acta 113 4.4).
# ESPERADO_BASE es un LITERAL FIJO, escrito a mano, DELIBERADAMENTE NO
# DERIVADO de CASOS: si se derivara de CASOS (p.ej. con un dict comprehension
# sobre la misma lista), una mutacion que cambia el esperado de un caso en
# CASOS cambiaria SU PROPIO ancla al mismo tiempo y la ALERTA nunca podria
# dispararse (el mismo boquete, en espejo, que TAREA 2.4 de la 115 probo que
# NO existe para estos veintidos). El ancla vive SEPARADA a proposito.
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
    "Z_SONDA (control 2.3/2.4 v115)": 0,
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

# --- CAPA DE MOTIVO, EXTENSION A LOS SEIS (TAREA 2.1 de la vuelta 116) ---
# Los "ACTUAL": el valor que la funcion usa DE VERDAD hoy, exactamente como
# antes de esta vuelta (nadie los cambio). Viven en constantes con nombre
# para que una mutacion tenga UNA linea que tocar (ver MUTACION AA).
X_CODIGO_ESPERADO = 1
X_MARCAS_MINIMO = 1
TAREA24_109_PUESTO_ESPERADO = 123

Y_MSG_CON_1 = "Crudo != neto en al menos una busqueda: True"
Y_MSG_CON_2 = "EXCLUSIONES ---\nvuelta114_tarea2_1_barrido_talladores.py:"
Y_MSG_SIN_1 = "Crudo == neto: True"
Y_MSG_SIN_2 = "EXCLUSIONES ---\nNINGUNA"

# ESPERADO_BASE_EXTRA: el mismo contrato que ESPERADO_BASE, pero para los
# seis que no viven en CASOS. Literal FIJO, declarado APARTE de las
# constantes ACTUAL de arriba y de CASOS_OVERRIDE / CASO_TAREA24_109: si se
# derivara de ellos, la mutacion de la TAREA 2.3 se mutaria a si misma y la
# ALERTA no podria dispararse jamas (el boquete que esta extension cierra).
ESPERADO_BASE_EXTRA = {
    "X": (1, 2),
    "Y": (Y_MSG_CON_1, Y_MSG_CON_2, Y_MSG_SIN_1, Y_MSG_SIN_2),
    CASO_TAREA24_109[0]: 123,
    "N": (87, "en_sitio"),
    "O": (91, "cruce"),
    "P": (154, "en_sitio"),
}


def verificar_ancla_extra(nombre, actual, fallos):
    """Mismo contrato que la alerta de imprimir_caso, para los seis fuera de
    CASOS: compara el valor ACTUAL (el que la funcion usa de verdad hoy)
    contra el ancla fija ESPERADO_BASE_EXTRA. Si difieren y el nombre no esta
    en MOTIVOS, imprime la ALERTA, nombra el caso y lo anade a fallos."""
    base = ESPERADO_BASE_EXTRA.get(nombre)
    if base is not None and base != actual:
        if nombre in MOTIVOS:
            print("   MOTIVO: %s" % MOTIVOS[nombre])
        else:
            print("   ALERTA: PROPIEDAD ESPERADA CAMBIADA SIN MOTIVO DECLARADO (base %r, actual %r)" % (base, actual))
            fallos.append("%s (propiedad esperada sin motivo)" % nombre)


INSTRUMENTOS = [
    ("2. tallar_nombre_de_operacion.py OP-E-03",
     ["scripts/loop/tallar_nombre_de_operacion.py", "OP-E-03"], 0),
    ("3. verificar_apertura_sellada.py --vuelta 116",
     ["scripts/loop/verificar_apertura_sellada.py", "--vuelta", "116"], 0),
    ("4. verificar_cabecera_pegada_o_condensada.py --vuelta 116",
     ["scripts/loop/verificar_cabecera_pegada_o_condensada.py", "--vuelta", "116"], 0),
    ("5. verificar_cobertura_bolsa_tres_vias.py",
     ["scripts/loop/verificar_cobertura_bolsa_tres_vias.py"], 0),
    ("6. contar_cierre_efectivo.py",
     ["scripts/loop/contar_cierre_efectivo.py"], 0),
    ("7. verificar_vuelco_de_veredicto.py",
     ["scripts/loop/verificar_vuelco_de_veredicto.py"], 0),
    ("8. tallar_cabecera_reporte.py --fase04 --vuelta 116 --comparar REPORTE.md",
     ["scripts/loop/tallar_cabecera_reporte.py", "--fase04", "--vuelta", "116",
      "--comparar", "docs/loop/REPORTE.md"], 0),
    ("9. tallar_cifras_de_antes.py (sobre el propio REPORTE.md)",
     ["scripts/loop/tallar_cifras_de_antes.py"], 0),
]


def caso_x():
    codigo, out = correr(["scripts/loop/tallar_cifras_de_antes.py", "--fichero",
                          "docs/loop/_v113_mut_x/reporte_112.md"])
    dos_marcadas = out.count("sigue") >= X_MARCAS_MINIMO
    ok = (codigo == X_CODIGO_ESPERADO) and dos_marcadas
    return ok, codigo, out


def caso_y():
    """Y (TAREA 2.2 de la vuelta 114, re-verificada aqui como guarda del
    cierre): la PROPIEDAD del barrido, no un exit fijo. Corre el barrido CON
    exclusion (default) y SIN exclusion (--sin-exclusion) y comprueba:
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
    ok = ok and Y_MSG_CON_1 in out_con
    ok = ok and Y_MSG_CON_2 in out_con
    ok = ok and Y_MSG_SIN_1 in out_sin
    ok = ok and Y_MSG_SIN_2 in out_sin

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
    print("GUARDAS DEL CIERRE, VUELTA 116: NUEVE INSTRUMENTOS Y VEINTINUEVE CASOS DE MUTACION.")
    print("=" * 100)
    fallos = []

    for nombre, args, esperado in CASOS:
        imprimir_caso(nombre, args, esperado, fallos)

    ok_x, codigo_x, _out_x = caso_x()
    print("X (reporte 112 por git show 87397be1, marca las dos con \"sigue\") -- EXIT %d [%s]"
          % (codigo_x, "CALZA" if ok_x else "NO CALZA"))
    if not ok_x:
        fallos.append("X")
    verificar_ancla_extra("X", (X_CODIGO_ESPERADO, X_MARCAS_MINIMO), fallos)

    ok_y, resumen_y, _out_con, _out_sin = caso_y()
    print("Y (barrido 114 --sin-exclusion, verificado por PROPIEDAD) -- [%s] :: %s"
          % ("CALZA" if ok_y else "NO CALZA", resumen_y))
    if not ok_y:
        fallos.append("Y")
    verificar_ancla_extra("Y", (Y_MSG_CON_1, Y_MSG_CON_2, Y_MSG_SIN_1, Y_MSG_SIN_2), fallos)

    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_vuelco_de_veredicto as vvv

    ruta_mut = os.path.join(RAIZ, CASO_TAREA24_109[1])
    overrides = {"SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md": ruta_mut}
    f2, vuelcos2 = vvv.verificar(overrides=overrides)
    ok_123_mudo = False
    if not f2:
        v123 = [v for v in vuelcos2 if v["puesto"] == TAREA24_109_PUESTO_ESPERADO]
        ok_123_mudo = bool(v123) and not v123[0]["declarado"]
    print("%s -- %d %s [%s]" % (CASO_TAREA24_109[0], TAREA24_109_PUESTO_ESPERADO,
                                 "MUDO" if ok_123_mudo else "no-mudo",
                                 "CALZA" if ok_123_mudo else "NO CALZA"))
    if not ok_123_mudo:
        fallos.append(CASO_TAREA24_109[0])
    verificar_ancla_extra(CASO_TAREA24_109[0], TAREA24_109_PUESTO_ESPERADO, fallos)

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
        verificar_ancla_extra(letra, (puesto, tipo_esperado), fallos)

    # AA: CONTROL de la mutacion AA (TAREA 2.3). Sobre el fichero REAL (este
    # mismo, sin mutar), el ancla de X tiene que estar en silencio: CALZA y
    # SIN alerta. La prueba de que SI cae a ROJO al mutarse vive en
    # vuelta116_tarea2_3_mutacion_aa.py (antes/despues en sus dos ficheros).
    alerta_x = (X_CODIGO_ESPERADO, X_MARCAS_MINIMO) != ESPERADO_BASE_EXTRA["X"]
    ok_aa = ok_x and not alerta_x
    print("AA (control 2.3, ancla de X sin mutar en este fichero) -- [%s]"
          % ("CALZA" if ok_aa else "NO CALZA"))
    if not ok_aa:
        fallos.append("AA")

    total_casos = len(CASOS) + 1 + 1 + 1 + len(CASOS_OVERRIDE) + 1  # CASOS(incl. Z_SONDA) + X + Y + TAREA2.4-v109 + N,O,P + AA
    print()
    print("%d en CASOS (A-M,Q,R,S,T,U,V,W,Z_SONDA) + X + Y + TAREA2.4-v109 + N,O,P + AA = %d."
          % (len(CASOS), total_casos))

    todos_los_casos = ([n for n, _a, _e in CASOS] + ["X", "Y", CASO_TAREA24_109[0]]
                        + [letra for letra, *_resto in CASOS_OVERRIDE])
    anclados = [n for n in todos_los_casos if n in ESPERADO_BASE or n in ESPERADO_BASE_EXTRA]
    faltan = [n for n in todos_los_casos if n not in ESPERADO_BASE and n not in ESPERADO_BASE_EXTRA]
    print("capa de motivo: %d de %d casos anclados (AA es el control, no cuenta anclas propias)."
          % (len(anclados), len(todos_los_casos)))
    if faltan:
        print("SIN ANCLA (declarados, no inventados): %s" % ", ".join(faltan))

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
    print("VERDE: los VEINTINUEVE casos de mutacion y los NUEVE instrumentos calzan.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
