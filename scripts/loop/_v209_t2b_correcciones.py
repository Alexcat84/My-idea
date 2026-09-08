# -*- coding: utf-8 -*-
r"""_v209_t2b_correcciones.py . TAREA 2.b DE LA VUELTA 209: LAS DOS CIFRAS DE
`OP-L-01` QUE SIGUEN MAL EN `docs/plan/LECTURAS_DIRIGIDAS.md`, CORREGIDAS POR EL
CARRIL DEL BANCO `9.10`.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3).

LA FORMA, QUE ES LA MISMA QUE SALIO BIEN EN EL BANCO EN LA 208:
  . POR ADICION PURA. **No se pisa ni una linea**: ni la 31, ni la 291, ni la
    cabecera del documento. El texto viejo queda entero y sin tachar.
  . CORRECCION DECLARADA, con quien la encarga y con el motivo medido.
  . **LA FILA NUEVA LLEVA SU MARCA EN LA CELDA DE NOMBRE**,
    `(FILA CORREGIDA EN LA VUELTA 209)`. Es la adjudicacion `6.5` del acta 208 y
    ya no es una eleccion del ejecutor: un lector que toma la primera fila que
    casa no distingue la vieja de la nueva sin ella.

**NINGUNA CIFRA DE LAS FILAS SE TECLEA:** todas se LEEN de
`docs/loop/SALIDA_V209_T2A_DENOMINADOR.txt` y **el computo CAE EN ROJO si no
puede leer una**.

LAS DOS ESCRITURAS VAN DE ABAJO ARRIBA, la de la linea 291 antes que la de la 31,
para que el ancla de la segunda no se mueva mientras se escribe la primera.

LAS GUARDAS QUE PUEDEN CAER, y cada una para en seco sin escribir nada:
  (a) cada ancla tiene que aparecer EXACTAMENTE UNA VEZ en el fichero;
  (b) la linea 31 y la 291 tienen que ser las que se creen, cotejadas VERBATIM;
  (c) el control positivo de la columna `fuera de cola`: en la fila VIEJA tiene
      que cumplirse `posibles - leidos = fuera de cola`. Si no se cumple, es que
      la columna no significa lo que se cree y NO se computa la nueva;
  (d) al terminar, ni una linea del texto de entrada puede faltar, en orden, en
      el de salida.
"""
import argparse
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

LECTURAS = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
SALIDA_2A = os.path.join(LOOP, "SALIDA_V209_T2A_DENOMINADOR.txt")
VUELTA = 209

# LAS DOS LINEAS VIEJAS, VERBATIM. Se cotejan antes de escribir; si una no calza
# al byte, no se escribe nada.
VIEJA_31 = "| **seleccion de canal** | 5 | 10 | 8 | **2** |"
VIEJA_291 = ("| **seleccion de canal** | 8 de 10, **sub-puro** | **10 de 10, "
             "cobertura COMPLETA. MEZCLADO**: `LD-02` mete el primer D. **El "
             "sub-puro cae, y cae con la nomina cerrada** |")

# LOS DOS SITIOS DONDE SE ANCLA CADA ADICION. Van DETRAS del bloque citado, para
# no meterse dentro de ninguna tabla.
ANCLA_1 = ("> **NINGUNA de estas nominas tiene un solo par EN LA COLA.** Los que "
           "faltan, faltan" + NL +
           "> para siempre. **Por eso la lectura dirigida no es un lujo: es la "
           "unica via.**")
ANCLA_2 = ("> **LA LECCION DEL SALDO: 9 de 11 salieron SANAS.** Estos pares no "
           "estaban en la" + NL +
           "> cola **porque de verdad se parecen poco**, y la cola los descarto "
           "con razon.")


def uno(texto, patron, etiqueta, w):
    m = re.findall(patron, texto)
    if len(m) != 1:
        w("   ROJO: %s -> %d coincidencias de %r (se exige 1)"
          % (etiqueta, len(m), patron))
        return None
    return m[0]


def bloque_de_la_nomina(t2a, w):
    """EL TROZO DE LA SALIDA DEL 2.a QUE HABLA DE LA SELECCION DE CANAL, Y SOLO
    DE ELLA.

    --- POR QUE EXISTE ESTA FUNCION, Y ES UNA CAIDA MIA CAZADA ANTES DE
        PUBLICAR (`EJECUTOR.md` 8: la correccion no tapa lo que corrige) ---

    La primera version de este computo leia las cifras del FICHERO ENTERO con
    `uno()`, que cae en rojo si hay mas de una coincidencia. **La guarda paso y
    aun asi la cifra salio mal.** El patron de `fundidos` exigia una linea de
    detalle detras, y la seleccion de canal tiene **cero** fundidos, o sea
    ninguna linea de detalle: la unica coincidencia del fichero era **la de la
    JUNTA ASESORA, que tiene dos**. `uno()` devolvia 2 tan campante y la prosa
    iba a publicar que la seleccion de canal tiene dos miembros fundidos.

    **UNA GUARDA DE UNICIDAD SOBRE UN FICHERO CON DOS NOMINAS NO ES UNA GUARDA
    DE IDENTIDAD.** El arreglo no es afinar el patron: es ACOTAR EL TROZO, para
    que la pregunta *cuantos fundidos* solo pueda contestarse con datos de la
    nomina por la que se pregunta.
    """
    ini = t2a.find("   --- SELECCION DE CANAL ---")
    if ini < 0:
        w("   ROJO: la salida del 2.a no trae el bloque de la seleccion de canal.")
        return None
    fin = t2a.find("B.1)", ini)
    if fin < 0:
        w("   ROJO: no se pudo cerrar el bloque de la seleccion de canal.")
        return None
    return t2a[ini:fin]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    ap.add_argument("--salida", default="T2B_CORRECCIONES")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append

    def cerrar(codigo):
        salida = NL.join(L) + NL
        print(salida)
        io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
                "w", encoding="utf-8", newline=NL).write(salida)
        return codigo

    w("=" * 78)
    w("VUELTA %d, TAREA 2.b: LAS DOS CIFRAS DE OP-L-01 EN SU PROPIO DOCUMENTO,"
      % VUELTA)
    w("CORREGIDAS POR EL CARRIL DEL BANCO 9.10 Y POR ADICION PURA")
    w("=" * 78)
    w("")

    w("0) LAS CIFRAS, LEIDAS DE LA SALIDA DEL 2.a Y NO TECLEADAS")
    if not os.path.isfile(SALIDA_2A) or os.path.getsize(SALIDA_2A) == 0:
        w("   ROJO: %s no existe o mide cero bytes." % SALIDA_2A)
        return cerrar(1)
    t2a = io.open(SALIDA_2A, encoding="utf-8").read().replace(chr(13) + NL, NL)
    # LAS CINCO CIFRAS DE LA NOMINA SE LEEN DE **SU** BLOQUE Y NO DEL FICHERO
    # ENTERO. Ver el docstring de `bloque_de_la_nomina()`: una guarda de
    # unicidad sobre un fichero con dos nominas no es una guarda de identidad.
    canal = bloque_de_la_nomina(t2a, w)
    if canal is None:
        return cerrar(1)
    w("   el bloque de la SELECCION DE CANAL, acotado: %d bytes en disco y %d "
      "bytes normalizado a LF" % (len(canal.encode("utf-8")),
                                  len(canal.encode("utf-8"))))
    w("   y el de la JUNTA ASESORA queda FUERA a proposito: %s"
      % ("SI, no aparece" if "JUNTA ASESORA" not in canal else "NO, Y ESO ES ROJO"))
    if "JUNTA ASESORA" in canal:
        return cerrar(1)
    lecturas_de_la_nomina = {
        "miembros_lit": r"CIFRA miembros DISTINTOS EN LITERAL: (\d+)",
        "pares_lit": r"CIFRA PARES POSIBLES EN LITERAL: (\d+)",
        "miembros_res": r"CIFRA miembros DISTINTOS TRAS RESOLVER: (\d+)",
        "pares_res": r"CIFRA PARES POSIBLES TRAS RESOLVER: (\d+)",
        "fundidos": r"CIFRA miembros FUNDIDOS, o sea que hoy resuelven a otro "
                    r"nodo: (\d+)",
    }
    lecturas = {
        "leidos_viejos": r"CIFRA leidos publicados por la linea 31: (\d+)",
        "fuera_viejos": r"CIFRA fuera de cola que la linea 31 publica: (\d+)",
        "mesa_miembros": r"lo que la mesa dice\n   seleccion de canal .*?"
                         r"(\d+) miembros, \d+ pares\n",
        "lds_dentro": r"dentro de la seleccion de canal: (\d+)",
        "leidos_nuevos": r"CIFRA leidos mas las lecturas dirigidas de esta "
                         r"nomina: \d+ mas \d+ es (\d+)",
        "cobertura_num": r"COBERTURA: (\d+) de \d+",
        "cobertura_den": r"COBERTURA: \d+ de (\d+)",
        "node_id": r"CIFRA node_id distintos en disco: (\d+)",
        "alias": r"CIFRA alias en el mapa: (\d+)",
        "discrepan": r"CIFRA discrepancias con el contraste del encargo en el "
                     r"2\.a: (\d+)",
    }
    v = {}
    for k, pat in lecturas_de_la_nomina.items():
        x = uno(canal, pat, k, w)
        if x is None:
            return cerrar(1)
        v[k] = int(x)
        w("   %-16s -> %-4s (leida del BLOQUE de la seleccion de canal)" % (k, x))
    for k, pat in lecturas.items():
        x = uno(t2a, pat, k, w)
        if x is None:
            return cerrar(1)
        v[k] = int(x)
        w("   %-16s -> %-4s (leida del fichero entero, cifra que no es de nomina)"
          % (k, x))
    w("")

    w("1) LA SEDE AL ENTRAR, POR LAS DOS CONVENCIONES")
    crudo = io.open(LECTURAS, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    import hashlib
    sd = hashlib.sha256(crudo).hexdigest()[:16]
    sl = hashlib.sha256(lf).hexdigest()[:16]
    w("   docs/plan/LECTURAS_DIRIGIDAS.md: %d bytes en disco y %d bytes "
      "normalizado a LF" % (len(crudo), len(lf)))
    w("   sha256 disco %s y sha256 LF %s" % (sd, sl))
    w("   contraste del encargo: 214916 por las dos y sha256 dda1cdd67042c733")
    w("   CALZA: %s" % ("SI" if (len(crudo) == 214916 and len(lf) == 214916
                                 and sd == "dda1cdd67042c733"
                                 and sl == "dda1cdd67042c733")
                        else "NO, Y LA DISCREPANCIA SE DECLARA"))
    texto0 = lf.decode("utf-8")
    ls0 = texto0.split(NL)
    w("   CIFRA lineas por split: %d" % len(ls0))
    w("")

    w("2) LAS GUARDAS, ANTES DE COMPONER NADA")
    fallos = 0
    w("   (b) LAS DOS LINEAS VIEJAS, COTEJADAS VERBATIM CONTRA SU NUMERO:")
    for n, vieja in ((31, VIEJA_31), (291, VIEJA_291)):
        real = ls0[n - 1] if n <= len(ls0) else ""
        ok = (real == vieja)
        w("      linea %d calza al byte: %s" % (n, "SI" if ok else "NO"))
        if not ok:
            fallos += 1
            w("         esperada: %s" % vieja[:150])
            w("         hallada : %s" % real[:150])
    w("   (a) CADA ANCLA APARECE EXACTAMENTE UNA VEZ:")
    for nombre, ancla in (("ancla de la tabla por nomina", ANCLA_1),
                          ("ancla de que nominas cambian", ANCLA_2)):
        c = texto0.count(ancla)
        w("      %-34s aparece %d vez(ces) (se exige 1)" % (nombre, c))
        if c != 1:
            fallos += 1
    w("   Y CADA LINEA VIEJA APARECE EXACTAMENTE UNA VEZ, para que la adicion no")
    w("   pueda confundirse de fila:")
    for n, vieja in ((31, VIEJA_31), (291, VIEJA_291)):
        c = texto0.count(vieja)
        w("      la de la linea %-4d aparece %d vez(ces) (se exige 1)" % (n, c))
        if c != 1:
            fallos += 1
    w("   (c) EL CONTROL POSITIVO DE LA COLUMNA `fuera de cola`, SOBRE LA FILA")
    w("       VIEJA: posibles menos leidos tiene que dar fuera de cola.")
    celdas = [c.strip() for c in ls0[30].split("|")]
    vm = int(re.sub(r"[^0-9]", "", celdas[2]))
    vp = int(re.sub(r"[^0-9]", "", celdas[3]))
    vl = int(re.sub(r"[^0-9]", "", celdas[4]))
    vf = int(re.sub(r"[^0-9]", "", celdas[5]))
    w("       fila vieja: %d miembros, %d posibles, %d leidos, %d fuera de cola"
      % (vm, vp, vl, vf))
    ok_c = (vp - vl == vf)
    w("       %d menos %d es %d, y la columna dice %d: %s"
      % (vp, vl, vp - vl, vf, "CALZA" if ok_c else "NO CALZA"))
    if not ok_c:
        fallos += 1
        w("       ROJO: la columna no significa lo que se cree. NO SE COMPUTA.")
    w("   CIFRA guardas que fallan: %d" % fallos)
    if fallos:
        w("   ROJO: NO SE ESCRIBE NADA Y LA SEDE QUEDA INTACTA.")
        return cerrar(1)
    w("")

    # LA CIFRA DE `fuera de cola` DE LA FILA NUEVA SE COMPUTA CON LA MISMA REGLA
    # QUE EL CONTROL POSITIVO ACABA DE VALIDAR. NO SE TECLEA.
    nuevos_fuera = v["pares_lit"] - v["leidos_nuevos"]
    w("3) LAS DOS FILAS NUEVAS, COMPUESTAS DE CIFRAS LEIDAS")
    w("   miembros %d, posibles %d, leidos %d, fuera de cola %d"
      % (v["miembros_lit"], v["pares_lit"], v["leidos_nuevos"], nuevos_fuera))
    w("   cobertura %d de %d, INCOMPLETA y por tanto PROVISIONAL (banco 9.26)"
      % (v["cobertura_num"], v["cobertura_den"]))
    w("")

    marca = "(FILA CORREGIDA EN LA VUELTA %d)" % VUELTA

    bloque_1 = NL.join([
        "",
        "<!-- CORRECCION DECLARADA V%d TABLA POR NOMINA -->" % VUELTA,
        "",
        "> **CORRECCION DECLARADA (7 sep 2026, vuelta %d, TAREA 2), POR EL CARRIL"
        % VUELTA,
        "> DEL BANCO `9.10`, POR ADICION, CON EL TEXTO VIEJO ENTERO ARRIBA Y SIN",
        "> TACHARLO.** Las nueve filas de la tabla de aqui arriba siguen enteras y",
        "> sin tocar; lo que se anade es **la fila corregida de la seleccion de",
        "> canal**, que es la unica que este recomputo mueve.",
        ">",
        "> **QUIEN LA ENCARGA:** la adjudicacion `6.3` del acta del auditor de la",
        "> vuelta 208, medida en su `5.2`. El criterio de HECHO de la fase",
        "> `06 MESAS` en `docs/plan/08_VERIFICACION.md` exige que cada decision",
        "> vaya **con su cobertura al lado**, y esta tabla publicaba un denominador",
        "> que el recomputo desmiente.",
        ">",
        "> **EL MOTIVO, MEDIDO Y NO ALEGADO.** El denominador se conto de la",
        "> **nomina de miembros** de `docs/INTRA_DOMINIO_INFORME.md` lineas `5314`",
        "> a `5319`, y **no de esta tabla**, con el resolutor puesto (`P.1`). Esa",
        "> nomina tiene **%d** miembros y su **CORRECCION DECLARADA del 11 ago 2026**"
        % v["miembros_lit"],
        "> vive en `docs/INTRA_DOMINIO_INFORME.md:5321` y dice, literal, *son SEIS",
        "> y no cinco*. Con **%d** miembros los pares posibles son **%d** y no 10."
        % (v["miembros_lit"], v["pares_lit"]),
        ">",
        "> **LAS DOS CONVENCIONES, Y MANDA LA DEL CORTE DE LA FICHA.** En LITERAL",
        "> son **%d** miembros y **%d** pares; TRAS RESOLVER son **%d** y **%d**,"
        % (v["miembros_lit"], v["pares_lit"], v["miembros_res"], v["pares_res"]),
        "> con **%d** miembros fundidos. **Las dos dan lo mismo aqui.** La que"
        % v["fundidos"],
        "> manda es la **LITERAL**, que es la del `fecha_corte` de `OP-L-01`",
        "> (**2026-08-11**), por la adjudicacion `6.6` del acta 208. La resuelta se",
        "> publica al lado, con su fecha de hoy, **7 sep 2026**, y nunca en su",
        "> lugar.",
        ">",
        "> **NINGUNA CIFRA DE LA FILA ESTA TECLEADA:** todas salen de",
        "> `docs/loop/SALIDA_V%d_T2A_DENOMINADOR.txt`, y el computo que la escribe"
        % VUELTA,
        "> **cae en rojo si no puede leer una**. La columna `fuera de cola` se",
        "> computa con la misma regla que su control positivo valido sobre la fila",
        "> vieja: **posibles menos leidos**.",
        "",
        "| nomina | miembros | posibles | leidos | **fuera de cola** |",
        "|---|---:|---:|---:|---:|",
        "| **seleccion de canal** **%s** | **%d** | **%d** | **%d** | **%d** |"
        % (marca, v["miembros_lit"], v["pares_lit"], v["leidos_nuevos"],
           nuevos_fuera),
        "",
        "> **LA COBERTURA, AL LADO Y MEDIDA: %d de %d, o sea INCOMPLETA y por tanto"
        % (v["cobertura_num"], v["cobertura_den"]),
        "> PROVISIONAL** (banco `9.26`, verbatim: *mientras falte un par, la forma",
        "> es PROVISIONAL y se dice asi*). Los **%d** leidos son los **%d** que la"
        % (v["leidos_nuevos"], v["leidos_viejos"]),
        "> fila vieja publicaba mas las **%d** lecturas dirigidas cuyos dos extremos,"
        % v["lds_dentro"],
        "> tras resolver, caen dentro de esta nomina: `LD-02` (**D**) y `LD-03`",
        "> (**A**). **Los %d pares que faltan no estan en la cola y no van a venir**,"
        % nuevos_fuera,
        "> que es justo lo que dice el recuadro de aqui arriba.",
        "",
    ])

    bloque_2 = NL.join([
        "",
        "<!-- CORRECCION DECLARADA V%d QUE NOMINAS CAMBIAN -->" % VUELTA,
        "",
        "> **CORRECCION DECLARADA (7 sep 2026, vuelta %d, TAREA 2), POR EL CARRIL"
        % VUELTA,
        "> DEL BANCO `9.10`, POR ADICION, CON EL TEXTO VIEJO ENTERO ARRIBA Y SIN",
        "> TACHARLO.** Las ocho filas de la tabla de aqui arriba siguen enteras y",
        "> sin tocar; lo que se anade es **la fila corregida de la seleccion de",
        "> canal**.",
        ">",
        "> **LO QUE ESTABA MAL, DICHO CON SUS DOS CIFRAS.** La fila vieja publica",
        "> *10 de 10, cobertura COMPLETA*. **El denominador no es 10 sino %d**, y"
        % v["pares_lit"],
        "> con **%d** leidos la cobertura es **%d de %d**: **INCOMPLETA, y por el"
        % (v["leidos_nuevos"], v["cobertura_num"], v["cobertura_den"]),
        "> banco `9.26` la forma es PROVISIONAL y se dice asi**. El motivo entero,",
        "> con la nomina y su correccion del 11 ago 2026, esta en la correccion",
        "> declarada de la tabla por nomina de mas arriba en este mismo documento.",
        ">",
        "> **LA CELDA `antes` TAMBIEN LLEVABA EL DENOMINADOR VIEJO**, y por eso la",
        "> fila corregida la reescribe como **%d de %d**: son los mismos **%d**"
        % (v["leidos_viejos"], v["pares_lit"], v["leidos_viejos"]),
        "> leidos de siempre sobre el denominador recomputado. **Lo digo en vez de",
        "> cambiarlo callando**, porque la adjudicacion `6.3` del acta 208 nombra la",
        "> celda `despues` y no esta.",
        ">",
        "> **LA CLASE NO CAMBIA CON ESTO:** `LD-02` mete el primer **D** dentro de",
        "> la nomina y el sub-puro cae igual. **Lo que cae es el *cerrada*:** la",
        "> nomina **no** queda cerrada, quedan **%d** pares sin leer." % nuevos_fuera,
        "",
        "| nomina o forma | antes | **despues** |",
        "|---|---|---|",
        "| **seleccion de canal** **%s** | %d de %d, **sub-puro** | **%d de %d, "
        "cobertura INCOMPLETA y por tanto PROVISIONAL** (banco `9.26`). "
        "**MEZCLADO**: `LD-02` mete el primer D y **el sub-puro cae**. "
        "**La nomina NO queda cerrada: faltan %d pares** |"
        % (marca, v["leidos_viejos"], v["pares_lit"], v["cobertura_num"],
           v["cobertura_den"], nuevos_fuera),
        "",
    ])

    w("4) LOS DOS BLOQUES COMPUESTOS")
    for nombre, b in (("bloque de la tabla por nomina", bloque_1),
                      ("bloque de que nominas cambian", bloque_2)):
        w("   %-32s %d bytes, %d lineas" % (nombre, len(b.encode("utf-8")),
                                            b.count(NL)))
    todo = bloque_1 + bloque_2
    w("   CIFRA guiones largos: %d | CIFRA guiones medios: %d"
      % (todo.count(chr(8212)), todo.count(chr(8211))))
    if todo.count(chr(8212)) or todo.count(chr(8211)):
        w("   ROJO: los bloques traen guiones prohibidos. NO SE ESCRIBE.")
        return cerrar(1)
    w("   la marca %r aparece %d vez(ces) en lo compuesto (se exigen 2)"
      % (marca, todo.count(marca)))
    if todo.count(marca) != 2:
        w("   ROJO: falta la marca en la celda de nombre de alguna fila.")
        return cerrar(1)
    w("")

    w("5) LA ESCRITURA, DE ABAJO ARRIBA Y POR ADICION")
    ya = ("<!-- CORRECCION DECLARADA V%d TABLA POR NOMINA -->" % VUELTA) in texto0
    w("   las dos correcciones YA ESTAN: %s" % ("SI" if ya else "NO"))
    if a.escribir and not ya:
        nuevo = texto0.replace(ANCLA_2, ANCLA_2 + NL + bloque_2, 1)
        nuevo = nuevo.replace(ANCLA_1, ANCLA_1 + NL + bloque_1, 1)
        io.open(LECTURAS, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("   ESCRITAS las dos correcciones por adicion.")
    elif a.escribir:
        w("   NO SE ESCRIBE: ya estaban. IDEMPOTENTE.")
    else:
        w("   MODO MEDICION: no se escribe nada.")
    w("")

    w("=" * 78)
    w("EL CIERRE, REMEDIDO Y NO HEREDADO")
    w("=" * 78)
    crudo1 = io.open(LECTURAS, "rb").read()
    lf1 = crudo1.replace(b"\r\n", b"\n")
    sd1 = hashlib.sha256(crudo1).hexdigest()[:16]
    sl1 = hashlib.sha256(lf1).hexdigest()[:16]
    w("   docs/plan/LECTURAS_DIRIGIDAS.md al salir: %d bytes en disco y %d bytes "
      "normalizado a LF" % (len(crudo1), len(lf1)))
    w("   sha256 disco %s y sha256 LF %s" % (sd1, sl1))
    w("   CIFRA crecimiento: %d bytes en disco y %d bytes normalizado a LF"
      % (len(crudo1) - len(crudo), len(lf1) - len(lf)))
    texto1 = lf1.decode("utf-8")
    ls1 = texto1.split(NL)
    w("   CIFRA lineas al salir: %d (al entrar %d)" % (len(ls1), len(ls0)))
    w("")
    w("(d) LA GUARDA DEL TEXTO VIEJO: NI UNA LINEA BORRADA NI UNA CAMBIADA")
    faltan = 0
    j = 0
    for l in ls0:
        while j < len(ls1) and ls1[j] != l:
            j += 1
        if j >= len(ls1):
            faltan += 1
        else:
            j += 1
    w("   CIFRA lineas del texto de ENTRADA que NO estan, en orden, en el de")
    w("   SALIDA: %d" % faltan)
    w("   (la adicion solo puede ANADIR: si esta cifra no es 0, es ROJO)")
    w("")
    w("DONDE QUEDAN LAS CUATRO FILAS, REMEDIDO SOBRE EL FICHERO DE SALIDA")
    w("   (las dos viejas se MUEVEN de numero porque encima de ellas no se")
    w("   escribio nada, pero debajo si: el numero cambia, EL TEXTO NO.)")
    for etiqueta, patron in (
            ("la vieja de la tabla por nomina", VIEJA_31),
            ("la vieja de que nominas cambian", VIEJA_291)):
        donde = [i for i, l in enumerate(ls1, 1) if l == patron]
        w("   %-34s en la linea %s (entraba en la %s)"
          % (etiqueta, donde,
             "31" if etiqueta.endswith("nomina") else "291"))
    donde_m = [i for i, l in enumerate(ls1, 1) if marca in l]
    w("   las dos filas NUEVAS, por su marca en la celda de nombre: lineas %s"
      % donde_m)
    for i in donde_m:
        w("      linea %d | %s" % (i, ls1[i - 1][:190]))
    w("")
    w("FIN")
    return cerrar(0)


if __name__ == "__main__":
    raise SystemExit(main())
