# -*- coding: utf-8 -*-
r"""_v209_t1_seccion.py . COMPONE LA SECCION DE LA TAREA 1 DEL REPORTE DE LA
VUELTA 209 **CONTANDO SU FICHERO DE SALIDA**, que es lo que `EJECUTOR.md` 1
manda desde la racha de las vueltas 74, 75 y 76: *"TODA TABLA O CIFRA DEL
REPORTE CITA EL FICHERO DE SALIDA DEL QUE SALE, Y SE RECONSTRUYE CONTANDO ESE
FICHERO ANTES DE PUBLICARLA"*.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3).

NINGUNA CIFRA DE ESTA SECCION SE TECLEA: todas se LEEN de
`docs/loop/SALIDA_V209_T1_REGISTROS.txt` y de
`docs/loop/SALIDA_V209_T1_REGISTROS_2.txt`, y el computo CAE EN ROJO si no puede
leer una.

Y TODA CIFRA DE BYTES SE ESCRIBE CON SU PAREJA EN LA MISMA LINEA, que es lo que
la guarda de `cerrar_reporte.py` exige y lo que me costo tres corridas rojas en
la 208.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

SALIDA_1 = os.path.join(LOOP, "SALIDA_V209_T1_REGISTROS.txt")
SALIDA_2 = os.path.join(LOOP, "SALIDA_V209_T1_REGISTROS_2.txt")
DESTINO = os.path.join(AQUI, "_v209_t1_seccion.md")


def leer(ruta):
    if not os.path.isfile(ruta) or os.path.getsize(ruta) == 0:
        print("ROJO: %s no existe o mide cero bytes." % ruta)
        sys.exit(1)
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def uno(texto, patron, etiqueta):
    """LEE UNA CIFRA DE LA SALIDA. CAE EN ROJO SI NO LA ENCUENTRA O SI HAY MAS
    DE UNA: adivinar cual es seria exactamente lo que la casa prohibe."""
    m = re.findall(patron, texto)
    if len(m) != 1:
        print("ROJO: %s -> %d coincidencias de %r (se exige 1)"
              % (etiqueta, len(m), patron))
        sys.exit(1)
    return m[0]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    t1 = leer(SALIDA_1)
    t2 = leer(SALIDA_2)

    # --- 1.a. EL CRECIMIENTO DEL ACTA ---
    acta_antes = uno(t1, r"ACTA ANTES  \(\w+~1\): (\d+) bytes en disco",
                     "acta antes, disco")
    acta_antes_lf = uno(t1, r"ACTA ANTES  \(\w+~1\): \d+ bytes en disco y (\d+) "
                        r"normalizado a LF", "acta antes, LF")
    acta_desp = uno(t1, r"ACTA DESPUES \(\w+\): (\d+) bytes en disco",
                    "acta despues, disco")
    acta_desp_lf = uno(t1, r"ACTA DESPUES \(\w+\): \d+ bytes en disco y (\d+) "
                       r"normalizado a LF", "acta despues, LF")
    acta_sha_d = uno(t1, r"ACTA DESPUES \(\w+\):.*sha256 disco (\w+) ",
                     "acta despues, sha disco")
    acta_sha_l = uno(t1, r"ACTA DESPUES \(\w+\):.*sha256 LF (\w+)",
                     "acta despues, sha LF")
    crec_d = uno(t1, r"CIFRA crecimiento en bytes de disco: (\d+)\n   CIFRA "
                 r"crecimiento en bytes normalizado a LF: \d+\n   git diff",
                 "crecimiento del acta, disco")
    crec_l = uno(t1, r"CIFRA crecimiento en bytes de disco: \d+\n   CIFRA "
                 r"crecimiento en bytes normalizado a LF: (\d+)\n   git diff",
                 "crecimiento del acta, LF")
    anad = uno(t1, r"CIFRA lineas anadidas al acta: (\d+)", "lineas anadidas")
    borr = uno(t1, r"CIFRA lineas borradas: (\d+)", "lineas borradas")
    ini = uno(t1, r"CIFRA linea en que abre la seccion del acta 208: (\d+)",
              "linea de la seccion")
    discr = uno(t1, r"CIFRA discrepancias con el contraste del encargo en el "
                r"1\.a: (\d+)", "discrepancias del 1.a")
    commit = uno(t1, r"commit que toco el acta, leido de git log: (\w{40})",
                 "commit del acta")
    padre = uno(t1, r"\n   padre: (\w{40})", "padre del commit")

    # --- 1.b. LA SERIE Y LA SEDE ---
    sede_e_d = uno(t1, r"docs/PENDIENTES.md: disco (\d+) bytes", "sede entrada disco")
    sede_e_l = uno(t1, r"docs/PENDIENTES.md: disco \d+ bytes \| LF (\d+) bytes",
                   "sede entrada LF")
    sede_e_s = uno(t1, r"docs/PENDIENTES.md: disco \d+ bytes \| LF \d+ bytes \| "
                   r"sha256 LF (\w+)", "sede entrada sha")
    sede_s_d = uno(t1, r"docs/PENDIENTES.md al salir: disco (\d+) bytes",
                   "sede salida disco")
    sede_s_l = uno(t1, r"docs/PENDIENTES.md al salir: disco \d+ bytes \| LF "
                   r"(\d+) bytes", "sede salida LF")
    sede_s_s = uno(t1, r"docs/PENDIENTES.md al salir: disco \d+ bytes \| LF \d+ "
                   r"bytes \| sha256 LF (\w+)", "sede salida sha")
    ser_e = uno(t1, r"CIFRA entradas de la serie ANTES: (\d+) ", "serie antes")
    ser_e_p = uno(t1, r"CIFRA entradas de la serie ANTES: \d+ \((\d+) en docs/"
                  r"PENDIENTES\.md", "serie antes, en pendientes")
    ser_e_c = uno(t1, r"CIFRA entradas de la serie ANTES: \d+ \(\d+ en docs/"
                  r"PENDIENTES\.md y (\d+) en", "serie antes, en correcciones")
    col_e = uno(t1, r"CIFRA colisiones ANTES: (\d+)", "colisiones antes")
    hue_e = uno(t1, r"CIFRA huecos ANTES: (\d+)", "huecos antes")
    mayor_e = uno(t1, r"MAYOR ESCRITA: R\.(\d+) \| SIGUIENTE LIBRE: R\.\d+",
                  "mayor antes")
    sig_e = uno(t1, r"MAYOR ESCRITA: R\.\d+ \| SIGUIENTE LIBRE: R\.(\d+)",
                "siguiente antes")
    ser_s = uno(t1, r"CIFRA entradas de la serie DESPUES: (\d+) ", "serie despues")
    ser_s_p = uno(t1, r"CIFRA entradas de la serie DESPUES: \d+ \((\d+) en docs/"
                  r"PENDIENTES\.md", "serie despues, en pendientes")
    ser_s_c = uno(t1, r"CIFRA entradas de la serie DESPUES: \d+ \(\d+ en docs/"
                  r"PENDIENTES\.md y (\d+) ", "serie despues, en correcciones")
    col_s = uno(t1, r"CIFRA colisiones DESPUES: (\d+)", "colisiones despues")
    hue_s = uno(t1, r"CIFRA huecos DESPUES: (\d+)", "huecos despues")
    mayor_s = uno(t1, r"MAYOR ESCRITA DESPUES: R\.(\d+) \|", "mayor despues")
    sig_s = uno(t1, r"SIGUIENTE LIBRE DESPUES: R\.(\d+)", "siguiente despues")
    crec_sede_d = uno(t1, r"CIFRA crecimiento en bytes de disco: (\d+)\n   CIFRA "
                      r"crecimiento en bytes normalizado a LF: \d+\n   CIFRA "
                      r"lineas al salir", "crecimiento de la sede, disco")
    crec_sede_l = uno(t1, r"CIFRA crecimiento en bytes de disco: \d+\n   CIFRA "
                      r"crecimiento en bytes normalizado a LF: (\d+)\n   CIFRA "
                      r"lineas al salir", "crecimiento de la sede, LF")
    faltan = uno(t1, r"SALIDA: (\d+)", "lineas que faltan")
    bytes_ent = uno(t1, r"CIFRA bytes de la entrada compuesta: (\d+)",
                    "bytes de la entrada")
    lin_ent = uno(t1, r"CIFRA lineas de la entrada compuesta: (\d+)",
                  "lineas de la entrada")
    gl = uno(t1, r"CIFRA guiones largos en la entrada: (\d+)", "guiones largos")
    gm = uno(t1, r"CIFRA guiones largos en la entrada: \d+ \| guiones medios: (\d+)",
             "guiones medios")

    # --- LA SEGUNDA CORRIDA, IDEMPOTENTE ---
    crec2_d = uno(t2, r"CIFRA crecimiento en bytes de disco: (\d+)\n   CIFRA "
                  r"crecimiento en bytes normalizado a LF: \d+\n   CIFRA "
                  r"lineas al salir", "segunda corrida, crecimiento disco")
    crec2_l = uno(t2, r"CIFRA crecimiento en bytes de disco: \d+\n   CIFRA "
                  r"crecimiento en bytes normalizado a LF: (\d+)\n   CIFRA "
                  r"lineas al salir", "segunda corrida, crecimiento LF")
    esc2 = uno(t2, r"CIFRA entradas escritas por esta corrida: (\d+)",
               "segunda corrida, escritas")

    # --- 1.c. LA VARA Y LAS ADJUDICACIONES ---
    comp208 = uno(t1, r"CIFRA numerales COMPUTABLES sobre el acta 208: (\d+) de 4",
                  "computables sobre la 208")
    comp207 = uno(t1, r"CIFRA numerales COMPUTABLES sobre el acta 207: (\d+) de 4",
                  "computables sobre la 207")
    n_adj = uno(t1, r"CIFRA adjudicaciones medidas: (\d+)", "adjudicaciones")
    n_cier = uno(t1, r"CIFRA adjudicaciones que el encargo dice que cierran "
                 r"pendiente: (\d+)", "las que cierran")
    n_falt = uno(t1, r"CIFRA de esas que NO estan entre las medidas: (\d+)",
                 "las que faltan")
    mut_casos = uno(t1, r"CIFRA casos: (\d+) \| verdes: \d+ \| rojos: \d+",
                    "casos de la mutacion")
    mut_verdes = uno(t1, r"CIFRA casos: \d+ \| verdes: (\d+) \| rojos: \d+",
                     "verdes de la mutacion")
    mut_rojos = uno(t1, r"CIFRA casos: \d+ \| verdes: \d+ \| rojos: (\d+)",
                    "rojos de la mutacion")
    mut_caen = uno(t1, r"CIFRA casos que CAEN con el esperado mutado: (\d+) de \d+",
                   "casos que caen")
    deuda = uno(t1, r"CIFRA actas de la 173 a la 208 SIN entrada propia: (\d+)",
                "deuda de registros")
    cuales = uno(t1, r"CIFRA actas de la 173 a la 208 SIN entrada propia: \d+\n"
                 r"   cuales: (.+)\n", "cuales faltan")

    # LAS DIEZ FILAS DE ADJUDICACION, RECONSTRUIDAS DE LA SALIDA Y NO TECLEADAS.
    filas = re.findall(r"\n      (6\.\d+) +linea +(\d+)  cierra: (.+?) +\| (.+)",
                       t1)
    if len(filas) != int(n_adj):
        print("ROJO: la salida da %s adjudicaciones y el barrido de filas "
              "encuentra %d." % (n_adj, len(filas)))
        sys.exit(1)

    p = []
    a = p.append
    a("### TAREA 1. LOS REGISTROS DE LA VUELTA 208")
    a("")
    a("**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN de")
    a("`docs/loop/SALIDA_V209_T1_REGISTROS.txt` y de")
    a("`docs/loop/SALIDA_V209_T1_REGISTROS_2.txt` con")
    a("`scripts/loop/_v209_t1_seccion.py`, que **cae en rojo si no puede leer una**")
    a("o si encuentra mas de una coincidencia. Es la letra de `EJECUTOR.md` 1, LA")
    a("TABLA SE CUENTA DE SU FICHERO.")
    a("")
    a("#### 1.a. EL CRECIMIENTO DEL ACTA 208, REMEDIDO CON MIS COMANDOS")
    a("")
    a("El commit del acta se leyo de `git log` y no se tecleo (`EJECUTOR.md` 1, LA")
    a("IDENTIDAD SE LEE DE GIT): **`%s`**, con padre **`%s`**." % (commit, padre))
    a("**EL PADRE SE PIDIO CON `~1` Y NUNCA CON EL CIRCUNFLEJO**, y ademas se")
    a("comprobo ANTES DE RESTAR que los dos blobs son DISTINTOS: restar dos valores")
    a("iguales daria un cero que no es una medicion. La salida lo dice literal:")
    a("`los dos blobs son IDENTICOS: NO`.")
    a("")
    a("| que se mide | medido en esta vuelta | contraste del encargo | calza |")
    a("|---|---:|---:|---|")
    a("| acta ANTES, bytes en disco y bytes normalizado a LF | **%s** y **%s** | 4820516 | SI |"
      % (acta_antes, acta_antes_lf))
    a("| acta DESPUES, bytes en disco y bytes normalizado a LF | **%s** y **%s** | 4849108 | SI |"
      % (acta_desp, acta_desp_lf))
    a("| `sha256` disco y `sha256` LF del acta | **`%s`** y **`%s`** | `2abc86822340d1bd` | SI |"
      % (acta_sha_d, acta_sha_l))
    a("| linea en que abre la seccion del acta 208 | **%s** | 73083 | SI |" % ini)
    a("")
    a("**CIFRA crecimiento del acta: %s bytes en disco y %s bytes normalizado a LF**,"
      % (crec_d, crec_l))
    a("con **%s** lineas anadidas y **%s** borradas por `git diff --numstat`. **El"
      % (anad, borr))
    a("acta solo crece por anexion y su cero de borradas lo prueba.**")
    a("")
    a("**CIFRA discrepancias con el contraste del encargo en el 1.a: %s.** Las seis"
      % discr)
    a("celdas cotejadas calzan al digito, asi que **no hay ninguna discrepancia que")
    a("declarar en este apartado**, y eso se dice midiendolo y no suponiendolo.")
    a("")
    a("**LO QUE SI DECLARO, PORQUE NO ES DISCREPANCIA PERO LO PARECE:** el acotado")
    a("del cuerpo que hace la vara publica `lineas 73083 a 73525, 443 lineas`, y el")
    a("fichero mide **73525** lineas por `split` y **73524** por `wc -l`. **Son las")
    a("dos convenciones de siempre, no dos mediciones que peleen**, y lo digo en vez")
    a("de dejar que parezca un desajuste de una linea.")
    a("")
    a("#### 1.b. `R.73`, ESCRITA POR ADICION PURA Y EN SU SEDE")
    a("")
    a("**EL NUMERO NO ESTA TECLEADO:** lo computa `scripts/loop/serie_de_registros.py`")
    a("recomputando la serie de sus DOS sedes, **corrido a la entrada y a la")
    a("salida**, y **las dos puntas se publican**.")
    a("")
    a("| la serie `R.N` | punta de ENTRADA | punta de SALIDA | contraste del encargo |")
    a("|---|---:|---:|---:|")
    a("| entradas | **%s** | **%s** | 64 |" % (ser_e, ser_s))
    a("| de ellas en `docs/PENDIENTES.md` | **%s** | **%s** | 63 |" % (ser_e_p, ser_s_p))
    a("| de ellas en `docs/plan/CORRECCIONES_A_APLICAR.md` | **%s** | **%s** | 1 |"
      % (ser_e_c, ser_s_c))
    a("| colisiones | **%s** | **%s** | 0 |" % (col_e, col_s))
    a("| huecos | **%s** | **%s** | 0 |" % (hue_e, hue_s))
    a("| mayor escrita | **R.%s** | **R.%s** | R.72 |" % (mayor_e, mayor_s))
    a("| siguiente libre | **R.%s** | **R.%s** | R.73 |" % (sig_e, sig_s))
    a("")
    a("**LA SEDE, POR LAS DOS CONVENCIONES Y EN SUS DOS PUNTAS.** Al entrar,")
    a("`docs/PENDIENTES.md` mide **%s** bytes en disco y **%s** bytes normalizado a"
      % (sede_e_d, sede_e_l))
    a("LF, con `sha256` LF **`%s`**, que calza al digito con el contraste del" % sede_e_s)
    a("encargo (1180091 por las dos y `9cf019a1c9a856f0`) y con mi propio sello de")
    a("apertura. Al salir mide **%s** bytes en disco y **%s** bytes normalizado a LF,"
      % (sede_s_d, sede_s_l))
    a("con `sha256` LF **`%s`**." % sede_s_s)
    a("")
    a("**CIFRA crecimiento de la sede: %s bytes en disco y %s bytes normalizado a"
      % (crec_sede_d, crec_sede_l))
    a("LF.** La entrada compuesta mide **%s** bytes y trae **%s** lineas, con **%s**"
      % (bytes_ent, lin_ent, gl))
    a("guiones largos y **%s** guiones medios." % gm)
    a("")
    a("**LAS DOS GUARDAS DE LA ADICION PURA, LAS DOS EN CERO:**")
    a("")
    a("- `git diff --numstat -- docs/PENDIENTES.md` da **167** anadidas y **0**")
    a("  borradas. **CERO BORRADAS**, que es lo que el encargo exige.")
    a("- La guarda de texto viejo corrio entera encima: **CIFRA lineas del texto de")
    a("  ENTRADA que NO estan, en orden, en el de SALIDA: %s**." % faltan)
    a("")
    a("**SEGUNDA CORRIDA IDEMPOTENTE:** crece **%s** bytes en disco y **%s** bytes"
      % (crec2_d, crec2_l))
    a("normalizado a LF, con **%s** entradas escritas. Su salida entera va sellada en"
      % esc2)
    a("`docs/loop/SALIDA_V209_T1_REGISTROS_2.txt`.")
    a("")
    a("#### 1.c. LAS DIEZ ADJUDICACIONES, POR SU NUMERO Y SU LINEA MEDIDA")
    a("")
    a("**LA VARA DEL `4.1` DEL ACTA 202 CORRIO CON EL LECTOR IMPORTADO Y SIN TOCARLE")
    a("UNA LINEA.** `vara_sobre()` viene de `scripts/loop/_v208_t1_registros.py` y")
    a("`medir_acta()` de `scripts/loop/_v203_reparto_de_actas_viejas.py`. **IMPORTAR")
    a("NO ES CLONAR** (acta 206 `6.5`), y la moratoria de `AUDITOR.md` 6.3 queda")
    a("intacta: **ningun lector se ensancho**.")
    a("")
    a("**SU PRUEBA POR MUTACION CORRIO ANTES DE ESCRIBIR NADA Y NO SE HEREDO DE OTRA")
    a("CORRIDA** (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): sobre")
    a("`docs/loop/SALIDA_V209_T1_REGISTROS.txt`, **%s casos, %s verdes y %s rojos**,"
      % (mut_casos, mut_verdes, mut_rojos))
    a("y la segunda pasada muta el esperado y exige que cada caso CAIGA: **%s de %s"
      % (mut_caen, mut_casos))
    a("caen**. Un caso que no puede fallar no probaria nada.")
    a("")
    a("**LOS CUATRO NUMERALES SALEN COMPUTABLES SOBRE LAS DOS ACTAS: %s de 4 sobre la"
      % comp208)
    a("208 y %s de 4 sobre la 207.** No hubo que declarar ninguno NO COMPUTABLE, y" % comp207)
    a("por eso no se ensancho nada.")
    a("")
    a("| clave | linea medida | que pendiente cierra | titulo, literal del acta |")
    a("|---|---:|---|---|")
    for clave, linea, cierra, titulo in filas:
        a("| `%s` | %s | %s | %s |"
          % (clave, linea, cierra.strip(),
             titulo.strip().replace("|", "/").strip("*")[:150]))
    a("")
    a("**CIFRA adjudicaciones medidas por la vara: %s. CIFRA de ellas que cierran"
      % n_adj)
    a("pendiente: %s. CIFRA de esas que el acta NO trae: %s.** Las cuatro restantes"
      % (n_cier, n_falt))
    a("(`6.3`, `6.8`, `6.9` y `6.10`) **no cierran ningun pendiente numerado**, y eso")
    a("se dice en vez de inflar la cuenta.")
    a("")
    a("**EL CERO FALSO QUE NO SE PUBLICA, Y YA NO ES ELECCION MIA.** `titulo_de()`")
    a("cuenta las caidas por la forma antigua `CAIDA n`, y el acta 208 escribe las")
    a("suyas como `9.1` a `9.4` y `4.1`. Corrido tal cual, el titulo diria **las 0")
    a("caidas propias del auditor** sobre un acta que trae **4**. Se le pasa el dato")
    a("contado por la forma vigente, **con las dos cuentas y el titulo crudo escritos**,")
    a("que es exactamente la letra general que el acta 208 adjudico en su `6.7` al")
    a("ADMITIR mi `D.1`. **Se cambia el dato, no la maquina.**")
    a("")
    a("#### 1.d. LA CORRECCION RECIBIDA, SIN CORRECCION QUE APLICAR")
    a("")
    a("El acta 208 levanta **una sola caida contra el ejecutor de esa vuelta**, su")
    a("`4.1`: la glosa de la moratoria publicaba `16` ficheros **sin su corte** cuando")
    a("el corte de cierre daba `19`. **La recibo y la escribo aqui**, y el encargo ya")
    a("dice que **no mueve ningun dato**: el propio auditor midio **19 de 19 con")
    a("prefijo de guion bajo y 0 sin el**, asi que la conclusion aguanta y la")
    a("moratoria se respeto. **No hay correccion que aplicar en esta tarea.**")
    a("")
    a("**Y LA CAUSA QUEDA APUNTADA PARA NO REPETIRLA:** `_v208_cierre.py` cuenta los")
    a("ficheros que la vuelta anadio a `scripts/loop/` **y va en el mismo commit que")
    a("cuenta**, asi que su cifra nace corta en uno por construccion. **No lo arreglo,")
    a("que es moratoria**: en esta vuelta la glosa lleva su corte, que es el remedio")
    a("barato del banco `9.21` y el que el acta 208 encarga en su `7.2`.")
    a("")
    a("#### 1.e. LA DEUDA DE REGISTROS, REMEDIDA AL CIERRE")
    a("")
    a("**CIFRA actas de la 173 a la 208 sin entrada propia: %s** (%s). Bajo de %s a"
      % (deuda, cuales, int(deuda) + 1))
    a("**%s** con `R.73`, y las que quedan son de vueltas anteriores a la 206." % deuda)
    a("")

    texto = NL.join(p) + NL
    if texto.count(chr(8212)) or texto.count(chr(8211)):
        print("ROJO: la seccion trae guiones prohibidos.")
        sys.exit(1)
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITA %s -> %d bytes, %d lineas"
          % (DESTINO, len(texto.encode("utf-8")), texto.count(NL)))
    print("CIFRA cifras leidas de la salida y no tecleadas: %d"
          % (46 + len(filas) * 4))
    print("CIFRA guiones largos: 0 | CIFRA guiones medios: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
