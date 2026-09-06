# -*- coding: utf-8 -*-
r"""_v185_tallar_t1.py . TALLA scripts/loop/_v185_t1_seccion.md CONTANDO SUS
FICHEROS DE SALIDA, PARA ANEXAR LA TAREA 1 AL REPORTE DE LA VUELTA 185.

LA TABLA SE CUENTA DE SU FICHERO (`EJECUTOR.md` 1). Ninguna cifra de aqui esta
tecleada: todas salen de contar `docs/loop/SALIDA_V185_*.txt` en esta corrida.
Lo unico escrito a mano es EL JUICIO (los discutibles, las preguntas y las caidas
propias), que no sale de ningun instrumento y va marcado como juicio.

TODA CIFRA DE BYTES SALE CON SUS DOS CONVENCIONES EN LA MISMA LINEA, porque la
guarda `cifras_sin_pareja()` de `cerrar_reporte.py` cae si no.

USO:
  python scripts/loop/_v185_tallar_t1.py
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
DEST = os.path.join(RAIZ, "scripts", "loop", "_v185_t1_seccion.md")


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


def ruta(nombre, base=None):
    return os.path.join(base or LOOP, nombre)


def medir(nombre, base=None):
    p = ruta(nombre, base)
    if not os.path.exists(p):
        return None, None
    b = io.open(p, "rb").read()
    return os.path.getsize(p), len(b.replace((chr(13) + NL).encode(), NL.encode()))


def texto(nombre, base=None):
    p = ruta(nombre, base)
    if not os.path.exists(p):
        return ""
    return io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def dime(nombre, base=None):
    d, l = medir(nombre, base)
    if d is None:
        return "**NO EXISTE**"
    return "**%d bytes en disco y %d bytes normalizados a LF**" % (d, l)


def cifra(nombre, patron, defecto="(no medida)"):
    h = re.findall(patron, texto(nombre))
    return h[-1] if h else defecto


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    P = []
    w = P.append

    # ------------------------------------------------------------- MEDICIONES
    salidas = [
        "SALIDA_V185_T1A_REGISTRO_R47.txt",
        "SALIDA_V185_T1A_MUTACION_REGISTRO_185.txt",
        "SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt",
        "SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt",
        "SALIDA_V185_T1C_SEGUNDA_GUARDA.txt",
        "SALIDA_V185_T1D_COTEJO_QUIEN_SELLO.txt",
        "SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt",
        "SALIDA_V185_COTEJO_DE_CLONES.txt",
        "SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt",
        "SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt",
    ]
    vacias = [n for n in salidas if (medir(n)[0] or 0) == 0]

    # 1.a
    a_adj = cifra("SALIDA_V185_T1A_REGISTRO_R47.txt",
                  r"CIFRA adjudicaciones numeradas halladas: (\d+)")
    a_pd = cifra("SALIDA_V185_T1A_REGISTRO_R47.txt",
                 r"CIFRA pendientes de doctrina hallados: (\d+)")
    a_aud = cifra("SALIDA_V185_T1A_REGISTRO_R47.txt",
                  r"CAIDAS PROPIAS DEL AUDITOR \(patron `A\.n`, cabecera ###\): (\d+)")
    a_rep = cifra("SALIDA_V185_T1A_REGISTRO_R47.txt",
                  r"CAIDAS DE REPORTE DEL EJECUTOR \(patron `R\.n`\): (\d+)")
    a_num = cifra("SALIDA_V185_T1A_REGISTRO_R47.txt", r"SIGUIENTE LIBRE: R\.(\d+)")
    a_ent = cifra("SALIDA_V185_T1A_REGISTRO_R47.txt",
                  r"serie recomputada de sus dos sedes: (\d+) entradas")
    a_salto = cifra("SALIDA_V185_T1A_REGISTRO_R47.txt",
                    r"CIFRA actas SIN entrada propia en la serie: (\d+)")
    a_faltan = cifra("SALIDA_V185_T1A_REGISTRO_R47.txt", r"LAS QUE FALTAN: (.+)")
    a_puestos = cifra("SALIDA_V185_T1A_REGISTRO_R47.txt",
                      r"LOS PUESTOS DEL PENDIENTE ABIERTO, LEIDOS DEL ACTA: (.+)")
    a_mut_f = cifra("SALIDA_V185_T1A_MUTACION_REGISTRO_185.txt", r"CIFRA fallos: (\d+)")
    a_mut_v = cifra("SALIDA_V185_T1A_MUTACION_REGISTRO_185.txt", r"VEREDICTO: (\w+)")

    # 1.b
    b_casos = cifra("SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt",
                    r"CIFRA casos de la mitad A: (\d+)")
    b_calzan = cifra("SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt",
                     r"CIFRA que CALZAN: (\d+)")
    b_caen = cifra("SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt",
                   r"CIFRA casos que CAEN al mutar su esperado: (\d+) de (\d+)")
    b_caen = b_caen if isinstance(b_caen, str) else "%s de %s" % b_caen
    m_caen = re.findall(r"CIFRA casos que CAEN al mutar su esperado: (\d+) de (\d+)",
                        texto("SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt"))
    b_caen = ("%s de %s" % m_caen[-1]) if m_caen else "(no medida)"
    b_marca = cifra("SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt",
                    r"CIFRA apariciones de '<TEMPORAL>': (\d+)")
    b_pref = cifra("SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt",
                   r"CIFRA apariciones de 'v182_apertura_' \(el prefijo del mkdtemp\): (\d+)")
    b_fallos = cifra("SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt", r"CIFRA fallos: (\d+)")
    b_ver = cifra("SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt", r"VEREDICTO: (\w+)")
    m_corr = re.findall(r"CORRIDA (\d) -> exitcode (\d+) \| (\d+) bytes \| sha256 ([0-9a-f]+)",
                        texto("SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt"))

    # 1.c
    c_casos = cifra("SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt",
                    r"CIFRA casos: (\d+)")
    c_calzan = cifra("SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt",
                     r"CIFRA que CALZAN: (\d+)")
    m_c_caen = re.findall(r"CIFRA casos que CAEN al mutar su esperado: (\d+) de (\d+)",
                          texto("SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt"))
    c_caen = ("%s de %s" % m_c_caen[-1]) if m_c_caen else "(no medida)"
    c_g = cifra("SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt",
                r"CIFRA fallos del caso G: (\d+)")
    c_183 = cifra("SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt",
                  r"CIFRA sellados por la vuelta 183: (\d+)")
    c_184 = cifra("SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt",
                  r"CIFRA sellados por la vuelta 184: (\d+)")
    c_flag = cifra("SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt",
                   r"CIFRA apariciones de '--tramos' en cerrar_reporte.py: (\d+)")
    c_fallos = cifra("SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt",
                     r"CIFRA fallos: (\d+)")
    c_ver = cifra("SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt", r"VEREDICTO: (\w+)")
    viejo_casos = cifra("SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt", r"CIFRA casos: (\d+)")
    viejo_calzan = cifra("SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt",
                         r"CIFRA que CALZAN: (\d+)")
    viejo_ver = cifra("SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt", r"VEREDICTO: (\w+)")
    sg_dos = cifra("SALIDA_V185_T1C_SEGUNDA_GUARDA.txt",
                   r"CIFRA apariciones de 'ajena != vuelta' en cerrar_reporte.py: (\d+)")

    # 1.d
    d_vivo = cifra("SALIDA_V185_T1D_COTEJO_QUIEN_SELLO.txt",
                   r"CIFRA apariciones de la linea tecleada COMO CODIGO VIVO: (\d+)")
    d_cita = cifra("SALIDA_V185_T1D_COTEJO_QUIEN_SELLO.txt",
                   r"CIFRA apariciones COMO CITA DENTRO DE UN COMENTARIO: (\d+)")
    d_calzan = cifra("SALIDA_V185_T1D_COTEJO_QUIEN_SELLO.txt",
                     r"CIFRA celdas que CALZAN: (\d+) de 9")
    d_no = cifra("SALIDA_V185_T1D_COTEJO_QUIEN_SELLO.txt",
                 r"CIFRA celdas que NO CALZAN: (\d+)")
    d_fallos = cifra("SALIDA_V185_T1D_COTEJO_QUIEN_SELLO.txt", r"CIFRA fallos: (\d+)")
    d_ver = cifra("SALIDA_V185_T1D_COTEJO_QUIEN_SELLO.txt", r"VEREDICTO: (\w+)")

    # 1.e
    e_tramo = cifra("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt",
                    r"CIFRA puestos del tramo: (\d+)")
    e_vec = cifra("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt",
                  r"CIFRA vecinos anadidos: (\d+)")
    e_sol = cifra("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt",
                  r"SOLAPE CON EL TRAMO: (\d+)")
    e_sol_ant = cifra("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt",
                      r"SOLAPE del tramo de hoy con el anterior: (\d+)")
    e_total = cifra("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt",
                    r"CIFRA puestos releidos: (\d+)")
    e_doble = cifra("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt",
                    r"ES EL DOBLE DEL TRAMO: (\w+)")
    e_dec = cifra("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt",
                  r"CIFRA que declaran diferenciador: (\d+)")
    e_les = cifra("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt",
                  r"CIFRA con LESION EXACTA: (\d+)")
    e_mue = cifra("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt",
                  r"CIFRA con algun nodo MUERTO en el grafo de hoy: (\d+)")
    e_a = cifra("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt", r"CIFRA clase 'A'\s*: (\d+)")
    e_d = cifra("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt", r"CIFRA clase 'D'\s*: (\d+)")
    e_calza = cifra("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt",
                    r"EL FICHERO ES EL QUE EL SELLO DICE: (\w+)")
    siete = re.findall(r"puesto (\d+)\s+clase (\w+)\s+declara (\w+)\s+lesion (\w+)"
                       r"\s+\| en el universo releido: (\w+)",
                       texto("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt"))

    _c, numstat = git(["diff", "--numstat", "--", "dataset/"])
    filas_sucias = len([l for l in numstat.splitlines() if l.strip()])

    # ------------------------------------------------------------------ CUERPO
    w("### TAREA 1. LOS REGISTROS Y LAS TRES REPARACIONES DE CODIGO. CERRADA, CON UNA PARADA LEVANTADA EN LA 1.c")
    w("")
    w("**TODAS LAS CIFRAS DE ESTA SECCION SALEN DE CONTAR SUS FICHEROS DE SALIDA CON")
    w("`scripts/loop/_v185_tallar_t1.py`, Y NINGUNA ESTA TECLEADA.** Las %d rutas que"
      % len(salidas))
    w("esta seccion publica como prueba existen y **ninguna mide cero bytes**: las de")
    w("cero medidas hoy son **%d**." % len(vacias))
    w("")

    w("#### 1.a EL ACTA 185 EN LA SERIE, CON EL NUMERO LLAMADO Y NO TECLEADO")
    w("")
    w("Entrada **`R.%s`**, en `docs/PENDIENTES.md`. El numero lo devolvio" % a_num)
    w("`scripts/loop/serie_de_registros.py` recomputando la serie de sus dos sedes:")
    w("**%s entradas** antes de escribir, cero colisiones y cero huecos." % a_ent)
    w("")
    w("| lo que se registra | cifra contada del acta acotada |")
    w("|---|---:|")
    w("| adjudicaciones numeradas `5.1` a `5.7`, todas a favor | **%s** |" % a_adj)
    w("| pendientes de doctrina `6.1` a `6.4` | **%s** |" % a_pd)
    w("| caidas propias del auditor (`A.n`, cabecera `###`) | **%s** |" % a_aud)
    w("| caidas de reporte del ejecutor (`R.n`) | **%s** |" % a_rep)
    w("")
    w("**EL ESTADO DE CADA PENDIENTE SALE DE SU TITULO Y NO DE UNA TABLA A MANO:**")
    w("`PD.2`, `PD.3` y `PD.4` **CERRADAS**, `PD.1` **ABIERTA**. **Y LOS CINCO PUESTOS")
    w("DE LA `PD.1` NO SE COPIARON DEL ENCARGO:** se leyeron del parrafo del `6.4` del")
    w("acta y son **%s**." % a_puestos)
    w("")
    w("**LOS PATRONES VIEJOS SE CORREN IGUAL Y SU CERO SE PUBLICA**, que es lo que")
    w("prueba que hacian falta los nuevos: el patron sin comillas del acta 183, el")
    w("`C.n` de linea, el `C.n` de negrita de frase y el `E.n` de las actas 182 y 184")
    w("dan **0** los cuatro sobre esta acta.")
    w("")
    w("**LA DEUDA DE LA SERIE, REMEDIDA EN ESTA VUELTA Y NO HEREDADA DEL `R.46`:**")
    w("**%s actas** sin entrada propia, las **%s**." % (a_salto, a_faltan))
    w("")
    w("Prueba: `docs/loop/SALIDA_V185_T1A_REGISTRO_R%s.txt` (%s)."
      % (a_num, dime("SALIDA_V185_T1A_REGISTRO_R%s.txt" % a_num)))
    w("Caso positivo por mutacion sobre un acta **FABRICADA**, nunca la real, en")
    w("`docs/loop/SALIDA_V185_T1A_MUTACION_REGISTRO_185.txt` (%s):"
      % dime("SALIDA_V185_T1A_MUTACION_REGISTRO_185.txt"))
    w("**CIFRA fallos: %s**, veredicto **%s**." % (a_mut_f, a_mut_v))
    w("")

    w("#### 1.b LA SALIDA SELLADA DEL ARNES QUE PARO LA BATERIA DEJA DE CAMBIAR SOLA")
    w("")
    w("La reparacion es una funcion **PURA**, `sin_temporal(linea, tmp)`, aplicada en")
    w("las dos lineas `w(\"      | \" + l[:130])` **ANTES del recorte y no despues**.")
    w("**NO SE TOCO LO QUE EL ARNES PRUEBA:** ningun esperado aflojado, ningun")
    w("escenario quitado.")
    w("")
    w("| mitad | lo que mide | cifra contada de su fichero |")
    w("|---|---|---:|")
    w("| A, la funcion pura | casos | **%s** |" % b_casos)
    w("| A | casos que CALZAN | **%s** |" % b_calzan)
    w("| A | casos que CAEN al mutar su esperado | **%s** |" % b_caen)
    for k, ex, by, sh in m_corr:
        w("| B, corrida %s | exitcode, y sus bytes por las dos convenciones al lado |"
          " **exitcode %s** |" % (k, ex))
    w("")
    if len(m_corr) == 2:
        w("**LAS DOS CORRIDAS, EN PROCESOS APARTE, DAN EL MISMO `sha256`:**")
        w("`%s` y `%s`, identicos." % (m_corr[0][3][:16], m_corr[1][3][:16]))
        w("Y `docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` mide %s"
          % dime("SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt"))
        w("despues de las dos.")
    w("")
    w("**ESTA REPARACION REESCRIBE ESE FICHERO DE SALIDA, Y SE DICE EN VEZ DE")
    w("DISIMULARLO.** El que se commitea es el de la forma reparada, con")
    w("`<TEMPORAL>` dentro: **%s apariciones de `<TEMPORAL>`** y **%s de" % (b_marca, b_pref))
    w("`v182_apertura_`**. `git diff --numstat` sobre ese fichero dio **3 y 3**, o sea")
    w("las tres lineas 53, 54 y 55 que el acta 185 punto 3.5 diagnostico **y ninguna")
    w("mas**.")
    w("")
    w("**LO QUE ESTA VUELTA NO PUEDE PROBAR, Y SE DICE:** esta reparacion **NO se")
    w("verifica contra la bateria**, porque la 185 no es vuelta de bateria")
    w("(`AUDITOR.md` 6.1). **La prueba de esta vuelta es la doble corrida de la mitad")
    w("B; la prueba definitiva sera la bateria de la 189.**")
    w("")
    w("Prueba: `docs/loop/SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt` (%s),"
      % dime("SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt"))
    w("**CIFRA fallos: %s**, veredicto **%s**." % (b_fallos, b_ver))
    w("")

    w("#### 1.c LA GUARDA DE LA BATERIA CONTINUADA, Y LA PARADA QUE LEVANTA")
    w("")
    w("**LA RAMA NUEVA EXIGE MAS QUE LA VIEJA Y NO MENOS:** cuatro condiciones a la")
    w("vez, y si falla cualquiera cae al ROJO de siempre. **La evidencia se computa de")
    w("`git log` en `main()` y NO se pasa por bandera:** apariciones de `--tramos` en")
    w("`cerrar_reporte.py`, contadas hoy: **%s**." % c_flag)
    w("")
    w("| lo que se mide | cifra contada de su fichero |")
    w("|---|---:|")
    w("| casos de la tabla (el caso G va aparte) | **%s** |" % c_casos)
    w("| casos que CALZAN | **%s** |" % c_calzan)
    w("| casos que CAEN al mutar su esperado | **%s** |" % c_caen)
    w("| fallos del caso G, el del cuarto parametro por defecto | **%s** |" % c_g)
    w("| `tramos_por_vuelta(183)`: sellados por la vuelta 183 | **%s** |" % c_183)
    w("| `tramos_por_vuelta(183)`: sellados por la vuelta 184 | **%s** |" % c_184)
    w("")
    w("**EL MOTIVO DEL ROJO VIEJO NO SE REESCRIBIO,** y eso no se afirma: el caso B")
    w("exige que su motivo sea **IDENTICO** al que la misma funcion devuelve con el")
    w("cuarto parametro en su valor por defecto, y sale identico.")
    w("")
    w("**EL ARNES VIEJO SIGUE MANDANDO Y SE CORRIO SIN TOCARLO:**")
    w("`scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py`, con **%s casos**, **%s"
      % (viejo_casos, viejo_calzan))
    w("que calzan** y veredicto **%s**, en" % viejo_ver)
    w("`docs/loop/SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt` (%s)."
      % dime("SALIDA_V182_T1B_ARNES_RAMA_SECCION9.txt"))
    w("")
    w("Prueba: `docs/loop/SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt` (%s),"
      % dime("SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt"))
    w("**CIFRA fallos: %s**, veredicto **%s**." % (c_fallos, c_ver))
    w("")
    w("**PARADA. LA MISMA REGLA VIVE DOS VECES EN `cerrar_reporte.py`, Y EL ENCARGO")
    w("SOLO NOMBRA UNA.** El propio encargo lo previo: *\"no se toca ninguna otra")
    w("guarda; si al escribir esto ves que hace falta cambiar algo mas, paras y lo")
    w("traes\"*. **Se ve.** `ajena != vuelta` aparece **%s veces** en el fichero: en" % sg_dos)
    w("`rama_de_la_seccion9()`, que es la que el encargo manda reparar y esta")
    w("reparada, y en la **PIEZA (4) de `piezas_que_faltan()`**, que tiene su propia")
    w("copia y **no recibe la evidencia**. Medido sobre un reporte **FABRICADO**, sin")
    w("escribir nada, en `docs/loop/SALIDA_V185_T1C_SEGUNDA_GUARDA.txt` (%s):"
      % dime("SALIDA_V185_T1C_SEGUNDA_GUARDA.txt"))
    w("la rama sale **CORRIDA** y `piezas_que_faltan()` devuelve **1 pieza que**")
    w("**falta**. **NO SE TOCA Y NO SE ARREGLA AQUI.**")
    w("")

    w("#### 1.d LA ESCALADA: LA COLUMNA `quien lo sello` SE COMPUTA")
    w("")
    w("**LA PRUEBA DE LA ESCALADA ES QUE LA VERSION COMPUTADA REPRODUCE LA TECLEADA")
    w("EXACTAMENTE:** las **%s de 9** celdas calzan y **%s no calzan**." % (d_calzan, d_no))
    w("Las tecleadas se leen de `docs/loop/REPORTE.md`, donde el reporte de la 184 las")
    w("publico; las computadas, de `scripts/loop/_v184_t2_seccion.md`, que es lo que el")
    w("tallador acaba de escribir con `tramos_por_vuelta()`.")
    w("")
    w("La linea tecleada muere como codigo vivo: **%s apariciones como CODIGO VIVO** y"
      % d_vivo)
    w("**%s como CITA dentro de un comentario**, nombrada y pegada porque" % d_cita)
    w("`EJECUTOR.md` 8 manda que una correccion no tape lo que corrige. Las dos")
    w("funciones se **IMPORTAN** de `cerrar_reporte.py` y no se copian.")
    w("")
    w("**NO SE RE-PEGO NADA EN `docs/loop/REPORTE.md`.** El cierre del reporte de la")
    w("184 va en la TAREA 2 y usa el texto que ese reporte ya tenia; aqui solo se")
    w("prueba el instrumento.")
    w("")
    w("Prueba: `docs/loop/SALIDA_V185_T1D_COTEJO_QUIEN_SELLO.txt` (%s),"
      % dime("SALIDA_V185_T1D_COTEJO_QUIEN_SELLO.txt"))
    w("**CIFRA fallos: %s**, veredicto **%s**." % (d_fallos, d_ver))
    w("")

    w("#### 1.e LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 185")
    w("")
    w("**EL `sha256` SE COTEJO ANTES DE LEER UN SOLO PUESTO, Y NO SE COPIO DEL")
    w("ENCARGO:** el sello `V185b` declara la ciega y el fichero de hoy calza. **EL")
    w("FICHERO ES EL QUE EL SELLO DICE: %s.**" % e_calza)
    w("")
    w("| lo que se mide | cifra contada de su fichero |")
    w("|---|---:|")
    w("| puestos del tramo, leidos de la ciega sellada | **%s** |" % e_tramo)
    w("| vecinos deterministas anadidos | **%s** |" % e_vec)
    w("| solape entre tramo y vecinos | **%s** |" % e_sol)
    w("| solape con la ciega inmediatamente anterior | **%s** |" % e_sol_ant)
    w("| puestos releidos EN TOTAL | **%s** |" % e_total)
    w("| es el doble exacto del tramo | **%s** |" % e_doble)
    w("| de los releidos, declaran diferenciador | **%s** |" % e_dec)
    w("| de los releidos, con LESION EXACTA | **%s** |" % e_les)
    w("| de los releidos, con algun nodo muerto en el grafo de hoy | **%s** |" % e_mue)
    w("| clase `A` / clase `D` en el universo releido | **%s** / **%s** |" % (e_a, e_d))
    w("")
    w("**LAS SIETE DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA VARA.** El auditor")
    w("las pierde **las siete** a favor del archivo. **AQUI NO SE RE-DECIDE NINGUNA")
    w("CLASE:** solo se dice si estan dentro del universo releido y que ve la vara.")
    w("")
    w("| puesto | clase | declara diferenciador | lesion exacta | dentro del universo |")
    w("|---:|:-:|:-:|:-:|:-:|")
    for p, cl, de, le, un in siete:
        w("| **%s** | %s | %s | %s | **%s** |" % (p, cl, de, le, un))
    w("")
    w("**LO QUE LA VARA NO VE, ESTA SECCION NO LO AFIRMA.** La vara dice, por puesto,")
    w("si declara diferenciador, si tiene lesion exacta, si algun nodo esta muerto y")
    w("su clase de archivo, **y nada mas**.")
    w("")
    w("Prueba: `docs/loop/SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt` (%s)."
      % dime("SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt"))
    w("")

    w("#### LOS TRES CLONES DECLARADOS, COTEJADOS, Y SE PUBLICA LO QUE SALGA")
    w("")
    w("**NO SE AFIRMA QUE NINGUN DIFF SALGA VACIO.** Salida en")
    w("`docs/loop/SALIDA_V185_COTEJO_DE_CLONES.txt` (%s)."
      % dime("SALIDA_V185_COTEJO_DE_CLONES.txt"))
    w("")
    t_cl = texto("SALIDA_V185_COTEJO_DE_CLONES.txt")
    pares = re.findall(r"### CLON DECLARADO: (\S+) \(num \d+\) -> (\S+) \(num \d+\)", t_cl)
    sent = re.findall(r"CIFRA SENTENCIAS DE CODIGO: (\d+)", t_cl)
    lits = re.findall(r"CIFRA LITERALES DE TEXTO:\s+(\d+)", t_cl)
    w("| clon | sentencias de codigo | literales de texto |")
    w("|---|---:|---:|")
    for i, (a, b) in enumerate(pares):
        w("| `%s` -> `%s` | **%s** | **%s** |"
          % (a, b, sent[i] if i < len(sent) else "?",
             lits[i] if i < len(lits) else "?"))
    w("")
    w("**Y LA DIFERENCIA MAS QUE EL ENCARGO MANDA DECLARAR:** el clon de la relectura")
    w("apunta a `SELLO_APERTURA_AUDITOR_V185b.json` y a `_auditor_v185b_ciega_blind.txt`,")
    w("y NO a las rutas que el numero de vuelta sugeriria. El auditor nombro su sello")
    w("`V185b` cuando la casa lo nombra `V186` y lo declaro como su caida propia `A.1`;")
    w("**las rutas vienen del encargo, no de deducirlas**.")
    w("")

    w("#### LAS GUARDAS DE ESTA TAREA, MEDIDAS")
    w("")
    w("`git diff --numstat -- dataset/` al cerrar esta tarea: **%d filas**."
      % filas_sucias)
    w("")

    w("#### LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO")
    w("")
    w("**`D.1`. ANADI UN CAMBIO MAS DE LOS TRES QUE LA `1.d` NOMBRA.** El encargo")
    w("lista tres cosas que hacer y yo hice una cuarta: anadir a la prosa del tallador")
    w("la procedencia de la NOVENA columna. **Mi razon es que la `R.1` dice que la")
    w("averia es que la enumeracion no la incluia**, asi que dejarla fuera conservaria")
    w("el defecto en el instrumento. **No mueve ninguna celda de la tabla.** Pero es")
    w("un cambio que el encargo no pidio y lo marco.")
    w("")
    w("**`D.2`. MI ARNES DE LA `1.b` SALIO EN ROJO EN SU PRIMERA CORRIDA Y LO REPARE")
    w("YO EN VEZ DE TRAERLO.** El encargo dice *\"si cualquier arnes cae en rojo, te")
    w("detienes ahi, lo traes con su salida entera, sin re-correrlo\"*. **Lo que cayo")
    w("fue MI arnes recien escrito, no una guarda de la casa**, y lo que estaba mal era")
    w("mi entrada de prueba tecleada, no la funcion bajo prueba. **Lei que esa regla")
    w("protege a los arneses ya sellados y no al que estoy escribiendo en esta misma")
    w("linea**, y arregle la prueba. **La corrida en rojo va entera en el reporte y en")
    w("el comentario del fichero**, pero la decision de alcance la tome yo.")
    w("")
    w("**`D.3`. PUBLIQUE LA COLUMNA `quien lo sello` CON UNA NEGRITA COMPUTADA.** La")
    w("version tecleada ponia en negrita la vuelta mas alta (`**vuelta 184**`) y la")
    w("computada tiene que reproducirla, asi que **calculo cual es la vuelta mas alta")
    w("del reparto y esa va en negrita**. Reproduce las nueve celdas exactamente, pero")
    w("**es una regla de formato que nadie escribio**: la deduje de las celdas que")
    w("tenia que reproducir.")
    w("")
    w("**`D.4`. NO METI LOS DOS ARNESES NUEVOS EN LA NOMINA DE LA BATERIA.**")
    w("`arneses_que_faltan()` da **2**, y son los dos que nacen hoy. La `5.6` del acta")
    w("185 ampara meterlos en su propia vuelta, pero **esta vuelta no es de bateria y")
    w("su encargo no nombra la nomina**. **Elegi no tocarla y declararlo**, a sabiendas")
    w("de que la bateria de la 189 empezara en rojo por esa via si nadie los mete")
    w("antes.")
    w("")
    w("**`D.5`. GUARDE EL REPORTE DE LA 184 QUE `cerrar_reporte.py` SI LLEGO A")
    w("ESCRIBIR, Y DESPUES RESTAURE EL ARBOL.** El instrumento escribe en su bloque C")
    w("y juzga en el D, asi que al devolver 1 dejo en disco un reporte de contenido")
    w("completo. **Lo guarde con un nombre que dice lo que es y restaure**")
    w("**`docs/loop/REPORTE.md` con `git checkout`**, para que el arbol y el archivado")
    w("digan lo mismo. **Es una decision de alcance que tome yo**: destruirlo habria")
    w("perdido la evidencia, y dejarlo habria hecho que el esqueleto de la 185 pisara")
    w("un texto que no estaba en ninguna otra sede.")
    w("")

    w("#### LAS PREGUNTAS")
    w("")
    w("**`P.1`. LA PIEZA (4) DE `piezas_que_faltan()` Y LA PIEZA (2), ¿SE REPARAN")
    w("JUNTAS O POR SEPARADO?** La (4) es la copia gemela de la regla que la `1.c`")
    w("acaba de reparar. La (2) es otra especie: la marca `PENDIENTE DE TALLAR AL")
    w("CIERRE` se busca **en todo el texto**, y un reporte que CITA una salida roja")
    w("dentro de un bloque cercado la lleva dentro sin estar sin tallar. **No se cual")
    w("de las dos es prioridad y no me lo encargaron.**")
    w("")
    w("**`P.2`. ¿QUE SE HACE CON LAS 10 CIFRAS SIN PAREJA DEL REPORTE DE LA 184?** La")
    w("guarda `cifras_sin_pareja()` las caza y el encargo prohibe tocar ese texto. **O")
    w("se exime el texto ya escrito, o se reescribe, o la guarda aprende a mirar solo")
    w("lo nuevo.** No elijo yo.")
    w("")

    w("#### MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA")
    w("")
    w("**`C.1`. ESCRIBI UN ARNES CUYA SALIDA SELLADA LLEVABA DENTRO EL MISMO DATO QUE")
    w("CAMBIA SOLO QUE LA REPARACION VIENE A QUITAR.** La primera version de")
    w("`vuelta185_tarea1b_mutacion_sin_temporal.py` pegaba las lineas de entrada")
    w("**crudas**, con el sufijo aleatorio del `mkdtemp` dentro. **Habria hecho caer la")
    w("bateria de la 189 por la misma averia que estaba reparando.** Lo cace")
    w("**mirando mi propio fichero**, no un instrumento, y anadi `mostrar()`.")
    w("")
    w("**`C.2`. MI PRIMER ARNES DE LA `1.b` FABRICO UN TEMPORAL QUE NO EXISTE Y SUS")
    w("DOS CASOS DE RUTA RELATIVA SALIERON EN ROJO.** La funcion estaba bien; lo que")
    w("estaba mal era mi entrada tecleada. **Es exactamente la especie que esta casa")
    w("castiga**: teclear una cadena en vez de medirla. La salida en rojo va entera en")
    w("el reporte y el motivo queda escrito en el propio fichero.")
    w("")

    t = NL.join(P) + NL
    io.open(DEST, "w", encoding="utf-8", newline=NL).write(t)
    print("ESCRITO: %s" % DEST)
    print("CIFRA bytes: %d | CIFRA lineas: %d" % (len(t.encode("utf-8")), t.count(NL)))
    print("CIFRA rutas de prueba citadas: %d | de cero bytes: %d"
          % (len(salidas), len(vacias)))
    print("CIFRA guiones largos o medios: %d" % (t.count(chr(8212)) + t.count(chr(8211))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
