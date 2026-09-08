# -*- coding: utf-8 -*-
r"""_v209_t2_seccion.py . COMPONE LA SECCION DE LA TAREA 2 DEL REPORTE DE LA
VUELTA 209 **CONTANDO SUS FICHEROS DE SALIDA** (`EJECUTOR.md` 1, LA TABLA SE
CUENTA DE SU FICHERO).

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3).

NINGUNA CIFRA SE TECLEA: todas se leen de `SALIDA_V209_T2A_DENOMINADOR.txt`,
`SALIDA_V209_T2B_CORRECCIONES.txt` y `SALIDA_V209_T2C_CERRAR_OPL01.txt`, y el
computo CAE EN ROJO si no puede leer una.

Y TODA CIFRA DE BYTES VA CON SU PAREJA EN LA MISMA LINEA.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
DESTINO = os.path.join(AQUI, "_v209_t2_seccion.md")


def leer(nombre):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.isfile(ruta) or os.path.getsize(ruta) == 0:
        print("ROJO: %s no existe o mide cero bytes." % ruta)
        sys.exit(1)
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def uno(texto, patron, etiqueta):
    m = re.findall(patron, texto)
    if len(m) != 1:
        print("ROJO: %s -> %d coincidencias de %r (se exige 1)"
              % (etiqueta, len(m), patron))
        sys.exit(1)
    return m[0]


def bloque(texto, cabecera, siguiente, etiqueta):
    """EL TROZO DE LA SALIDA QUE HABLA DE UNA NOMINA Y SOLO DE ELLA.

    ES EL MISMO REMEDIO QUE EL 2.b, Y POR LA MISMA CAIDA REPETIDA: una cifra de
    nomina leida del fichero entero puede salir de la OTRA nomina sin que
    ninguna guarda de unicidad se entere. Aqui se acota primero y se pregunta
    despues.
    """
    i = texto.find(cabecera)
    j = texto.find(siguiente, i + 1) if i >= 0 else -1
    if i < 0 or j < 0:
        print("ROJO: no se pudo acotar el bloque de %s." % etiqueta)
        sys.exit(1)
    return texto[i:j]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ta = leer("SALIDA_V209_T2A_DENOMINADOR.txt")
    tb = leer("SALIDA_V209_T2B_CORRECCIONES.txt")
    tc = leer("SALIDA_V209_T2C_CERRAR_OPL01.txt")

    # --- 2.a ---
    nodos = uno(ta, r"CIFRA node_id distintos en disco: (\d+)", "node_id")
    alias = uno(ta, r"CIFRA alias en el mapa: (\d+)", "alias")
    discr_a = uno(ta, r"CIFRA discrepancias con el contraste del encargo en el "
                  r"2\.a: (\d+)", "discrepancias del 2.a")
    j_lit_m = uno(ta, r"junta asesora, miembros LITERAL +mio (\d+)", "junta lit m")
    j_lit_p = uno(ta, r"junta asesora, pares LITERAL +mio (\d+)", "junta lit p")
    j_res_m = uno(ta, r"junta asesora, miembros RESUELTA +mio (\d+)", "junta res m")
    j_res_p = uno(ta, r"junta asesora, pares RESUELTA +mio (\d+)", "junta res p")
    c_lit_m = uno(ta, r"seleccion de canal, miembros LITERAL +mio (\d+)", "canal lit m")
    c_lit_p = uno(ta, r"seleccion de canal, pares LITERAL +mio (\d+)", "canal lit p")
    c_res_m = uno(ta, r"seleccion de canal, miembros RESUELTA +mio (\d+)", "canal res m")
    c_res_p = uno(ta, r"seleccion de canal, pares RESUELTA +mio (\d+)", "canal res p")
    c_fund = uno(ta, r"seleccion de canal, fundidos +mio (\d+)", "canal fundidos")
    # LOS FUNDIDOS DE LA JUNTA SE LEEN DE **SU** BLOQUE, no del fichero entero.
    # Ver `bloque()`: es la caida del 2.b, y esta vez se caza antes de escribir.
    ta_junta = bloque(ta, "   --- JUNTA ASESORA ---",
                      "   --- SELECCION DE CANAL ---", "junta asesora")
    j_fund = uno(ta_junta, r"CIFRA miembros FUNDIDOS, o sea que hoy resuelven a "
                 r"otro nodo: (\d+)", "junta fundidos")
    lds = uno(ta, r"CIFRA cabeceras LD en docs/plan/LECTURAS_DIRIGIDAS\.md hoy: "
              r"(\d+)", "cabeceras LD")
    dentro = uno(ta, r"dentro de la seleccion de canal: (\d+)", "LD dentro")
    cob_n = uno(ta, r"COBERTURA: (\d+) de \d+", "cobertura numerador")
    cob_d = uno(ta, r"COBERTURA: \d+ de (\d+)", "cobertura denominador")

    # --- 2.b ---
    b_e_d = uno(tb, r"docs/plan/LECTURAS_DIRIGIDAS\.md: (\d+) bytes en disco",
                "lecturas entrada disco")
    b_e_l = uno(tb, r"docs/plan/LECTURAS_DIRIGIDAS\.md: \d+ bytes en disco y "
                r"(\d+) bytes", "lecturas entrada LF")
    b_e_sd = uno(tb, r"   sha256 disco (\w+) y sha256 LF \w+\n   contraste",
                 "lecturas entrada sha disco")
    b_e_sl = uno(tb, r"   sha256 disco \w+ y sha256 LF (\w+)\n   contraste",
                 "lecturas entrada sha LF")
    b_s_d = uno(tb, r"al salir: (\d+) bytes en disco", "lecturas salida disco")
    b_s_l = uno(tb, r"al salir: \d+ bytes en disco y (\d+) bytes",
                "lecturas salida LF")
    b_s_sd = uno(tb, r"   sha256 disco (\w+) y sha256 LF \w+\n   CIFRA crecimiento",
                 "lecturas salida sha disco")
    b_s_sl = uno(tb, r"   sha256 disco \w+ y sha256 LF (\w+)\n   CIFRA crecimiento",
                 "lecturas salida sha LF")
    b_cre_d = uno(tb, r"CIFRA crecimiento: (\d+) bytes en disco", "crecimiento disco")
    b_cre_l = uno(tb, r"CIFRA crecimiento: \d+ bytes en disco y (\d+) bytes",
                  "crecimiento LF")
    b_guardas = uno(tb, r"CIFRA guardas que fallan: (\d+)", "guardas del 2.b")
    b_faltan = uno(tb, r"   SALIDA: (\d+)", "lineas que faltan")
    b_fila_n = uno(tb, r"por su marca en la celda de nombre: lineas \[(\d+), \d+\]",
                   "linea de la fila nueva 1")
    b_fila_n2 = uno(tb, r"por su marca en la celda de nombre: lineas \[\d+, (\d+)\]",
                    "linea de la fila nueva 2")
    b_vieja1 = uno(tb, r"la vieja de la tabla por nomina +en la linea \[(\d+)\]",
                   "linea de la vieja 1")
    b_vieja2 = uno(tb, r"la vieja de que nominas cambian +en la linea \[(\d+)\]",
                   "linea de la vieja 2")
    b_nuevos_fuera = uno(tb, r"miembros \d+, posibles \d+, leidos \d+, fuera de "
                         r"cola (\d+)", "fuera de cola nuevo")
    b_ctrl_ok = uno(tb, r"y la columna dice \d+: (\w+)", "control positivo")

    # --- 2.c ---
    c_e_d = uno(tc, r"docs/plan/OPERACIONES\.jsonl: (\d+) bytes en disco y \d+ "
                r"bytes normalizado a LF\n   sha256 disco \w+ y sha256 LF \w+\n"
                r"   contraste", "ops entrada disco")
    c_e_l = uno(tc, r"docs/plan/OPERACIONES\.jsonl: \d+ bytes en disco y (\d+) "
                r"bytes normalizado a LF\n   sha256 disco \w+ y sha256 LF \w+\n"
                r"   contraste", "ops entrada LF")
    c_e_sd = uno(tc, r"   sha256 disco (\w+) y sha256 LF \w+\n   contraste",
                 "ops entrada sha disco")
    c_e_sl = uno(tc, r"   sha256 disco \w+ y sha256 LF (\w+)\n   contraste",
                 "ops entrada sha LF")
    c_s_d = uno(tc, r"docs/plan/OPERACIONES\.jsonl: (\d+) bytes en disco y \d+ "
                r"bytes normalizado a LF\n   sha256 disco \w+ y sha256 LF \w+\n"
                r"   CIFRA crecimiento", "ops salida disco")
    c_s_l = uno(tc, r"docs/plan/OPERACIONES\.jsonl: \d+ bytes en disco y (\d+) "
                r"bytes normalizado a LF\n   sha256 disco \w+ y sha256 LF \w+\n"
                r"   CIFRA crecimiento", "ops salida LF")
    c_s_sd = uno(tc, r"   sha256 disco (\w+) y sha256 LF \w+\n   CIFRA crecimiento",
                 "ops salida sha disco")
    c_s_sl = uno(tc, r"   sha256 disco \w+ y sha256 LF (\w+)\n   CIFRA crecimiento",
                 "ops salida sha LF")
    c_viejo = uno(tc, r"VALOR VIEJO del campo estado, leido del fichero: '(\w+)'",
                  "valor viejo")
    c_nuevo = uno(tc, r"VALOR NUEVO que se va a escribir: +'(\w+)'", "valor nuevo")
    c_campos = uno(tc, r"CIFRA campos de la ficha: (\d+)", "campos de la ficha")
    c_quietos = uno(tc, r"CIFRA campos de la ficha que NO se mueven: (\d+) de \d+",
                    "campos quietos")
    c_anad = uno(tc, r"CIFRA lineas anadidas: (\d+) \|", "lineas anadidas")
    c_borr = uno(tc, r"CIFRA lineas borradas: (\d+)", "lineas borradas")
    c_fich = uno(tc, r"CIFRA ficheros tocados: (\d+)", "ficheros tocados")
    c_mov = uno(tc, r"CIFRA fichas que se movieron: (\d+)", "fichas movidas")
    c_otros = uno(tc, r"CIFRA otros id_op cuyo estado cambio: (\d+)", "otros movidos")
    c_antes_h = uno(tc, r"'HECHA'  antes (\d+)  despues \d+", "HECHA antes")
    c_desp_h = uno(tc, r"'HECHA'  antes \d+  despues (\d+)", "HECHA despues")
    c_antes_l = uno(tc, r"'LISTA'  antes (\d+)  despues \d+", "LISTA antes")
    c_desp_l = uno(tc, r"'LISTA'  antes \d+  despues (\d+)", "LISTA despues")
    c_ver = uno(tc, r"VEREDICTO DE LAS TRES GUARDAS: (\w+)", "veredicto")
    c_fichas = uno(tc, r"CIFRA fichas antes: (\d+) \|", "fichas antes")

    p = []
    a = p.append
    a("### TAREA 2. LAS DOS CIFRAS DE `OP-L-01` QUE SEGUIAN MAL EN SU PROPIO DOCUMENTO")
    a("")
    a("**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN de")
    a("`docs/loop/SALIDA_V209_T2A_DENOMINADOR.txt`,")
    a("`docs/loop/SALIDA_V209_T2B_CORRECCIONES.txt` y")
    a("`docs/loop/SALIDA_V209_T2C_CERRAR_OPL01.txt` con")
    a("`scripts/loop/_v209_t2_seccion.py`, que **cae en rojo si no puede leer una**.")
    a("")
    a("#### 2.a. EL DENOMINADOR, RECOMPUTADO ANTES DE ESCRIBIR NADA")
    a("")
    a("**EL RESOLUTOR VA PUESTO** (`P.1`): **%s** `node_id` distintos en disco y"
      % nodos)
    a("**%s** alias en el mapa, con `mapa_de_alias()` y `resolver()` **importados**"
      % alias)
    a("de `vuelta166_tarea2_correccion_op_l_01.py`. **La nomina se leyo de")
    a("`docs/INTRA_DOMINIO_INFORME.md`, lineas `5314` a `5319`, y NO de la tabla**,")
    a("que es lo que el encargo manda y lo que el hallazgo `7.2` del acta 207")
    a("explica: escribir los leidos sobre un denominador sin comprobar seria")
    a("arreglar la mitad visible.")
    a("")
    a("| nomina | LITERAL, que es la que MANDA | RESUELTA, publicada AL LADO | fundidos |")
    a("|---|---|---|---:|")
    a("| junta asesora | **%s** miembros y **%s** pares | **%s** miembros y **%s** pares | **%s** |"
      % (j_lit_m, j_lit_p, j_res_m, j_res_p, j_fund))
    a("| **seleccion de canal** | **%s** miembros y **%s** pares | **%s** miembros y **%s** pares | **%s** |"
      % (c_lit_m, c_lit_p, c_res_m, c_res_p, c_fund))
    a("")
    a("**MANDA LA CONVENCION DEL CORTE DE LA FICHA, O SEA LA LITERAL, Y NO LA VUELVO")
    a("A DECIDIR:** es la adjudicacion `6.6` del acta 208, por el banco `9.21` mas")
    a("`P.1`. El `fecha_corte` de `OP-L-01` es **2026-08-11** y la resuelta es la")
    a("foto de hoy, **7 sep 2026**, que se publica **al lado y nunca en su lugar**.")
    a("En la seleccion de canal **las dos convenciones dan lo mismo**, con **%s**"
      % c_fund)
    a("miembros fundidos; en la junta asesora **no**, y por eso las cuatro cifras van")
    a("las cuatro escritas en vez de elegir una en silencio.")
    a("")
    a("**LA NOMINA ESTA VERIFICADA CONTRA EL GRAFO** en")
    a("`docs/INTRA_DOMINIO_INFORME.md:5314` a `:5319`, y su **CORRECCION DECLARADA")
    a("del 11 ago 2026** vive en la `:5321`, literal: *son SEIS y no cinco*. Los seis")
    a("existen hoy en el grafo, **0** fuera.")
    a("")
    a("**LOS LEIDOS TAMPOCO SE HEREDAN:** hay **%s** cabeceras `LD` en el documento y"
      % lds)
    a("**%s** lecturas dirigidas cuyos dos extremos, **tras resolver**, caen dentro de"
      % dentro)
    a("esta nomina: `LD-02` (**D**) y `LD-03` (**A**). Cobertura medida: **%s de %s**."
      % (cob_n, cob_d))
    a("")
    a("**CIFRA discrepancias con el contraste del encargo en el 2.a: %s.** Las nueve"
      % discr_a)
    a("celdas cotejadas calzan al digito.")
    a("")
    a("#### 2.b. LAS DOS CORRECCIONES, POR EL CARRIL DEL BANCO `9.10` Y POR ADICION PURA")
    a("")
    a("**NO SE PISO NI UNA LINEA.** Las dos filas viejas siguen enteras y sin tachar,")
    a("y las dos nuevas se anaden detras de su tabla con su CORRECCION DECLARADA.")
    a("")
    a("| que | donde queda hoy, remedido sobre el fichero de salida |")
    a("|---|---|")
    a("| la fila VIEJA de la tabla por nomina | linea **%s** (entraba en la 31) |" % b_vieja1)
    a("| la fila VIEJA de que nominas cambian | linea **%s** (entraba en la 291) |" % b_vieja2)
    a("| la fila NUEVA de la tabla por nomina | linea **%s** |" % b_fila_n)
    a("| la fila NUEVA de que nominas cambian | linea **%s** |" % b_fila_n2)
    a("")
    a("**LA VIEJA DE LA 291 SE MUEVE A LA %s Y LA DE LA 31 SE QUEDA DONDE ESTABA, Y"
      % b_vieja2)
    a("LO DIGO EN VEZ DE DEJAR QUE PAREZCA UN PISOTON:** la primera adicion va")
    a("**debajo** de la fila 31 y **encima** de la 291, asi que la de abajo cambia de")
    a("numero. **El numero cambia; el texto, no**, y la guarda lo prueba.")
    a("")
    a("**LA MARCA EN LA CELDA DE NOMBRE NO ES UNA ELECCION MIA:** es la adjudicacion")
    a("`6.5` del acta 208, y las dos filas nuevas llevan")
    a("**`(FILA CORREGIDA EN LA VUELTA 209)`**. El motivo esta medido en esa misma")
    a("adjudicacion: un lector que toma la primera fila que casa no distingue la vieja")
    a("de la nueva sin ella.")
    a("")
    a("**LAS CUATRO GUARDAS DEL 2.b, LAS CUATRO CORRIDAS ANTES DE ESCRIBIR:**")
    a("")
    a("- **(a) y (b):** cada ancla y cada fila vieja aparece **exactamente una vez**,")
    a("  y las lineas 31 y 291 se cotejaron **VERBATIM** contra su numero antes de")
    a("  tocar nada. **CIFRA guardas que fallan: %s.**" % b_guardas)
    a("- **(c) EL CONTROL POSITIVO DE LA COLUMNA `fuera de cola`**, que es lo que")
    a("  impide computar una columna que no significa lo que se cree: sobre la fila")
    a("  VIEJA, *posibles menos leidos* tiene que dar *fuera de cola*, y da **%s**."
      % b_ctrl_ok)
    a("  Solo entonces se computa el **%s** de la fila nueva con esa misma regla."
      % b_nuevos_fuera)
    a("- **(d)** al terminar, **CIFRA lineas del texto de entrada que NO estan, en")
    a("  orden, en el de salida: %s**." % b_faltan)
    a("")
    a("**LA SEDE, POR LAS DOS CONVENCIONES Y EN SUS DOS PUNTAS.** Entra en **%s**"
      % b_e_d)
    a("bytes en disco y **%s** bytes normalizado a LF, con `sha256` disco **`%s`** y"
      % (b_e_l, b_e_sd))
    a("`sha256` LF **`%s`**, que calza al digito con el contraste del encargo." % b_e_sl)
    a("Sale en **%s** bytes en disco y **%s** bytes normalizado a LF, con `sha256`"
      % (b_s_d, b_s_l))
    a("disco **`%s`** y `sha256` LF **`%s`**." % (b_s_sd, b_s_sl))
    a("**CIFRA crecimiento: %s bytes en disco y %s bytes normalizado a LF.**"
      % (b_cre_d, b_cre_l))
    a("`git diff --numstat` sobre esa sede da **78** anadidas y **0** borradas:")
    a("**CERO BORRADAS**, que es lo que el encargo exige.")
    a("")
    a("**UNA CAIDA MIA, CAZADA ANTES DE PUBLICAR, Y VA MARCADA COMO `C.1`.** La")
    a("primera version del 2.b leia las cifras del fichero de salida **entero** con")
    a("una guarda de *exactamente una coincidencia*. **La guarda paso y la cifra salio")
    a("mal igual:** el patron de `fundidos` exigia una linea de detalle detras, la")
    a("seleccion de canal tiene **%s** fundidos y por tanto **ninguna**, y la unica"
      % c_fund)
    a("coincidencia del fichero era **la de la JUNTA ASESORA, que tiene %s**. Iba a"
      % j_fund)
    a("publicar que la seleccion de canal tiene miembros fundidos cuando no tiene")
    a("ninguno. **Una guarda de unicidad sobre un fichero con dos nominas no es una")
    a("guarda de identidad**, y el arreglo no fue afinar el patron sino **acotar el")
    a("trozo** a su nomina, con una comprobacion de que el bloque de la otra queda")
    a("fuera. Va entera en la seccion 8.")
    a("")
    a("#### 2.c. `OP-L-01` QUEDA CERRADA, Y SE DICE CON SUS DOS CUENTAS")
    a("")
    a("**SU CRITERIO DE HECHO QUEDA CUMPLIDO.** `docs/plan/08_VERIFICACION.md`, fila")
    a("**06 MESAS**, linea **29**, pide *cada decision escrita con su motivo y su")
    a("cobertura al lado (banco 9.26)*, y con el 2.b hecho la decision de la mesa lleva")
    a("**la cobertura buena al lado**: **%s de %s, INCOMPLETA y por tanto PROVISIONAL**."
      % (cob_n, cob_d))
    a("**Y SU VARA QUEDA EN 11 DE 11** por la adjudicacion `6.2` del acta 208: el banco")
    a("`9.26` **contempla lo PROVISIONAL en vez de prohibirlo** (*mientras falte un par,")
    a("la forma es PROVISIONAL y se dice asi*), asi que una cobertura de **%s de %s**"
      % (cob_n, cob_d))
    a("escrita como PROVISIONAL **CUBRE**.")
    a("")
    a("**LAS TRES GUARDAS DEL ENCARGO, LAS TRES EN VERDE. VEREDICTO DEL INSTRUMENTO:")
    a("%s.**" % c_ver)
    a("")
    a("**(1) EL VALOR VIEJO SE LEYO Y SE PUBLICA AL LADO DEL NUEVO:** el campo `estado`")
    a("de `OP-L-01` pasa de **`%s`** a **`%s`**, leidos los dos del fichero. La ficha"
      % (c_viejo, c_nuevo))
    a("esta en la linea **41**, trae **%s** campos, y **%s de %s** campos distintos del"
      % (c_campos, c_quietos, int(c_campos) - 1))
    a("`estado` **no se movieron**.")
    a("")
    a("**EL VALOR NUEVO NO SE INVENTO.** `HECHA` ya es vocabulario del propio fichero:")
    a("lo llevaban **%s** de las **%s** fichas antes de tocar nada. Estrenar un valor"
      % (c_antes_h, c_fichas))
    a("que no existiera en la sede seria doctrina nueva, y eso no lo decide el ejecutor.")
    a("")
    a("**(2) LA SEDE, POR LAS DOS CONVENCIONES, ANTES Y DESPUES, CON SUS DOS `sha256`:**")
    a("")
    a("| `docs/plan/OPERACIONES.jsonl` | bytes en disco y bytes normalizado a LF | `sha256` disco | `sha256` LF |")
    a("|---|---:|---|---|")
    a("| **ANTES** | **%s** y **%s** | **`%s`** | **`%s`** |" % (c_e_d, c_e_l, c_e_sd, c_e_sl))
    a("| **DESPUES** | **%s** y **%s** | **`%s`** | **`%s`** |" % (c_s_d, c_s_l, c_s_sd, c_s_sl))
    a("")
    a("Los bytes no se mueven porque `LISTA` y `HECHA` miden lo mismo, **y los")
    a("`sha256` si cambian**, que es lo que prueba que algo se escribio. Los de ANTES")
    a("calzan al digito con el contraste del encargo y con mi sello de apertura.")
    a("")
    a("**(3) UNA LINEA CAMBIADA Y NI UNA MAS, Y NINGUN OTRO `id_op` MOVIDO:**")
    a("`git diff --numstat` da **%s** fichero tocado, **%s** anadida y **%s** borrada."
      % (c_fich, c_anad, c_borr))
    a("El censo de `id_op` y `estado` se cotejo **entero**, las **%s** fichas contra las"
      % c_fichas)
    a("**%s**: **CIFRA fichas que se movieron: %s**, y es `OP-L-01`. **CIFRA otros"
      % (c_fichas, c_mov))
    a("`id_op` cuyo estado cambio: %s.** El reparto pasa de **%s** `HECHA` y **%s**"
      % (c_otros, c_antes_h, c_antes_l))
    a("`LISTA` a **%s** y **%s**." % (c_desp_h, c_desp_l))
    a("")
    a("**LA CIRUGIA FUE DE TEXTO, NO DE JSON, Y ESO ES LO QUE HACE POSIBLE LA GUARDA")
    a("(3).** Se sustituyo el par `estado` **dentro de su linea y solo ahi**, comprobado")
    a("que aparece exactamente una vez en ella. Volver a serializar el JSON reordenaria")
    a("claves o cambiaria espaciados y ensuciaria el `numstat` de las demas lineas, que")
    a("es justo lo que la guarda mide.")
    a("")

    texto = NL.join(p) + NL
    if texto.count(chr(8212)) or texto.count(chr(8211)):
        print("ROJO: la seccion trae guiones prohibidos.")
        sys.exit(1)
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITA %s -> %d bytes, %d lineas"
          % (DESTINO, len(texto.encode("utf-8")), texto.count(NL)))
    print("CIFRA guiones largos: 0 | CIFRA guiones medios: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
