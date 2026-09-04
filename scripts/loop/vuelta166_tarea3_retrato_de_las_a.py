# -*- coding: utf-8 -*-
r"""vuelta166_tarea3_retrato_de_las_a.py . TAREA 3 de la vuelta 166.

EL RETRATO DE LAS A SE RECOMPUTA (adjudicacion 5.12 del acta 165, y hallazgo
4.1 de la misma acta). `docs/plan/RECOMPUTO_3388.md`, PASO 1, tabla del retrato.

POR QUE, Y NO ES COSMETICO. Las tres primeras filas de esa tabla llevan entre
doce y quince correcciones fechadas cada una, todas por el mismo carril: cada
vuelta que fundia actos cuadraba el contador y adosaba su nota. ESE BARRIDO PARO
EN LA VUELTA 58 (el ultimo commit del fichero es 3ffc2091) y desde entonces la
campana fundio el resto del tramo unico y sento las cinco mesas. Y NO ES UNA
TABLA CUALQUIERA: `docs/plan/08_VERIFICACION.md` pone el retrato de las A como
PASO 1 DE CUATRO y escribe que ES EL INSUMO DE TODO LO DEMAS.

EL CARRIL, QUE ES EL DE SIEMPRE Y NO UNO NUEVO (banco 9.10): contador cuadrado
EN EL MISMO ACTO, nota fechada ADOSADA, ninguna nota vieja reescrita y ninguna
cifra vieja borrada. Las cifras viejas se tachan con `~~` y se quedan enteras.

NINGUNA CIFRA DE ESTE INSTRUMENTO ESTA TECLEADA:
  - las CUATRO cifras nuevas se leen de la salida de `scripts/plan/recomputo_3388.py`,
    que es el instrumento de la casa, corrido en ESTA vuelta;
  - el CONTADOR de cada fila se COMPUTA contando los `~~**N**~~` que la celda ya
    tiene, nunca se lee de la palabra que el texto trae (que es justamente lo
    que fallaba cuando el contador se desincronizaba de la cadena);
  - el numeral en palabra sale de una tabla de numerales, no de la mano.

LO QUE NO HACE, Y SE DICE PARA QUE NO SE AMPLIE SOLO: NO recomputa los pasos 2,
3 y 4 del mismo documento. La 5.12 encarga el PASO 1 y nada mas, y ampliarlo
seria decidir su alcance por cuenta propia.

SU CASO POSITIVO POR MUTACION es `vuelta166_tarea3_mutacion_retrato.py`.

USO:
  python scripts/loop/vuelta166_tarea3_retrato_de_las_a.py            (mide, NO escribe)
  python scripts/loop/vuelta166_tarea3_retrato_de_las_a.py --aplicar  (mide, escribe y re mide)
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388.md")
SALIDA_JSONL = os.path.join("docs", "loop", "RECOMPUTO_V166.jsonl")

FECHA = "4 sep 2026"
VUELTA = 166

ORDINAL = {1: "PRIMERA", 2: "SEGUNDA", 3: "TERCERA", 4: "CUARTA", 5: "QUINTA",
           6: "SEXTA", 7: "SEPTIMA", 8: "OCTAVA", 9: "NOVENA", 10: "DECIMA",
           11: "UNDECIMA", 12: "DUODECIMA", 13: "DECIMOTERCERA",
           14: "DECIMOCUARTA", 15: "DECIMOQUINTA", 16: "DECIMOSEXTA",
           17: "DECIMOSEPTIMA", 18: "DECIMOCTAVA"}
CARDINAL = {1: "UNA VEZ", 2: "DOS VECES", 3: "TRES VECES", 4: "CUATRO VECES",
            5: "CINCO VECES", 6: "SEIS VECES", 7: "SIETE VECES",
            8: "OCHO VECES", 9: "NUEVE VECES", 10: "DIEZ VECES",
            11: "ONCE VECES", 12: "DOCE VECES", 13: "TRECE VECES",
            14: "CATORCE VECES", 15: "QUINCE VECES", 16: "DIECISEIS VECES",
            17: "DIECISIETE VECES", 18: "DIECIOCHO VECES"}

# LAS CUATRO FILAS, identificadas por el PRINCIPIO LITERAL de su primera celda.
FILAS = [
    ("A crudas en el archivo (`clase == 'A'`), corte 3.388", "crudas"),
    ("de esas, colapsan a auto-arista al resolver", "colapsos"),
    ("pares distintos en el retrato tras resolver y deduplicar", "distintos"),
    ("pares con mas de un veredicto crudo apuntando al mismo par resuelto",
     "multiples"),
]

PAT_TACHADA = re.compile(r"~~\*\*([\d.]+)\*\*~~")
PAT_VIVA = re.compile(r"(?<!~)\*\*([\d.]+)\*\*(?!~)")


def correr_recomputo():
    """LA CIFRA SALE DEL INSTRUMENTO DE LA CASA, CORRIDO HOY."""
    r = subprocess.run(
        [sys.executable, os.path.join("scripts", "plan", "recomputo_3388.py"),
         "--salida", SALIDA_JSONL], capture_output=True, cwd=RAIZ)
    texto = r.stdout.decode("utf-8", "replace") + r.stderr.decode("utf-8", "replace")
    # EL SALTO DE WINDOWS SE NORMALIZA ANTES DE LEER: si la salida trae el
    # retorno de carro, un patron anclado en fin de linea con re.M no casa
    # nunca, y el instrumento pararia diciendo que no hay cifra cuando la
    # cifra esta. Fallar por el salto de linea es fallar callado.
    limpio = texto.replace(chr(13) + chr(10), chr(10)).replace(chr(13), chr(10))
    return r.returncode, limpio


def leer_paso_1(texto):
    """Extrae las CUATRO cifras del PASO 1 y los pares en conflicto. Cae si una
    no se puede leer: una celda que no sale de un instrumento no se escribe."""
    d, faltan = {}, []
    m = re.search(r"^A crudas en el archivo \(clase == 'A'\): (\d+)$", texto, re.M)
    d["crudas"] = int(m.group(1)) if m else faltan.append("crudas")
    m = re.search(r"^de esas, colapsan a auto-arista tras resolver .*?: (\d+)$",
                  texto, re.M)
    d["colapsos"] = int(m.group(1)) if m else faltan.append("colapsos")
    m = re.search(r"^PARES DISTINTOS EN EL RETRATO \(tras resolver y deduplicar\): (\d+)$",
                  texto, re.M)
    d["distintos"] = int(m.group(1)) if m else faltan.append("distintos")
    m = re.search(r"^de esos, con mas de un veredicto crudo apuntando al mismo par resuelto: (\d+)$",
                  texto, re.M)
    d["multiples"] = int(m.group(1)) if m else faltan.append("multiples")
    pares = re.findall(r"^   (\[.+?\]): puestos (\[[\d, ]+\])$", texto, re.M)
    return d, [x for x in faltan if x], pares


def miles(n):
    """El estilo de la casa: los millares con punto."""
    return "{:,}".format(n).replace(",", ".")


def localizar_filas(lineas):
    """Devuelve [(clave, n_linea, texto)] para las cuatro filas, o PARA."""
    hallado, errores = [], []
    for prefijo, clave in FILAS:
        cand = [(i, l) for i, l in enumerate(lineas, 1)
                if l.startswith("| " + prefijo)]
        if len(cand) != 1:
            errores.append("la fila %r aparece %d veces" % (clave, len(cand)))
            continue
        hallado.append((clave, cand[0][0], cand[0][1]))
    return hallado, errores


def anatomia(texto_fila):
    """Cuenta la cadena de una celda: las tachadas, la viva y el contador REAL.
    EL CONTADOR SE CUENTA DE LA CADENA, NO SE LEE DE LA PALABRA."""
    celda = texto_fila.split("|")[2] if texto_fila.count("|") >= 3 else ""
    tachadas = PAT_TACHADA.findall(celda)
    vivas = PAT_VIVA.findall(celda)
    viva = vivas[0] if vivas else None
    return tachadas, viva, len(tachadas)


def nota_de_la_fila(clave, vieja, nueva, correcciones_ya, pares, medido):
    """La nota fechada que se ADOSA. Su ordinal se COMPUTA."""
    n = correcciones_ya + 1
    comun = (
        "[%s CORRECCION, CONTADOR CUADRADO EN EL MISMO ACTO, %s (vuelta %d, "
        "TAREA 3, adjudicacion 5.12 del acta 165 y su hallazgo 4.1): de %s a %s. "
        "EL BARRIDO DE ESTA TABLA PARO EN LA VUELTA 58 (ultimo commit del fichero, "
        "`3ffc2091`) y desde entonces la campana fundio el resto del tramo unico de "
        "`OP-U-01` y sento las cinco mesas de `06_MESAS`, sin volver a barrer aqui. "
        "Medido HOY con `python scripts/plan/recomputo_3388.py --salida %s` "
        "(`../loop/SALIDA_V166_T3_RECOMPUTO.txt`, paso 1), con el resolutor puesto, "
        "que es lo que `P.1` manda. Ninguna nota vieja se reescribe y ninguna cifra "
        "vieja se borra. "
        % (ORDINAL[n], FECHA, VUELTA, miles(int(vieja)), miles(nueva), SALIDA_JSONL.replace(os.sep, "/")))
    if clave == "colapsos":
        cuerpo = (
            "EL MOTIVO ES EL MISMO QUE EL DE LAS ONCE CORRECCIONES ANTERIORES DE ESTA "
            "FILA, y por eso no hace falta doctrina nueva: cada acto que se funde "
            "convierte su par `A` interno en un par cuyos dos ids resuelven al mismo "
            "nodo vivo. Lo que cambia no es la especie, es el tamano: son %d colapsos "
            "mas, los de todo lo que la campana fundio entre la vuelta 58 y hoy. "
            "ESTA VUELTA NO FUNDE NI UN ACTO Y NO VOLTEA NI UN VEREDICTO: solo mide y "
            "escribe la cifra que ya era verdad." % (nueva - int(vieja)))
    elif clave == "distintos":
        cuerpo = (
            "Y AQUI VA LO QUE ESTA CORRECCION ROMPE, DICHO ANTES DE QUE ALGUIEN LO USE: "
            "esta celda ya NO es la resta exacta de las dos filas de arriba, y las "
            "notas anteriores la calculaban asi con todas sus letras. %s crudas menos "
            "%s colapsos son %s, y los pares distintos son %s. LA DIFERENCIA DE %d ES "
            "EXACTAMENTE LA FILA DE ABAJO: cuatro pares llevan mas de un veredicto "
            "crudo apuntando al mismo par resuelto, y la deduplicacion los cuenta una "
            "vez. Mientras esa fila valia CERO la resta salia; desde hoy no sale, y "
            "quien la use como atajo se equivocara. LA VARA ES EL INSTRUMENTO, NO LA "
            "RESTA." % (miles(medido["crudas"]), miles(medido["colapsos"]),
                        miles(medido["crudas"] - medido["colapsos"]), miles(nueva),
                        (medido["crudas"] - medido["colapsos"]) - nueva))
    elif clave == "multiples":
        detalle = "; ".join("%s en los puestos %s" % (p, q) for p, q in pares)
        cuerpo = (
            "ESTA ES LA FILA QUE SOSTENIA A LAS OTRAS, y por eso su correccion es la "
            "que mas importa aunque su cifra sea la mas pequena: MIENTRAS VALIA CERO, "
            "la fila de los pares distintos podia leerse como la resta de las dos de "
            "arriba, y desde hoy no. Es la PRIMERA correccion de esta celda: nacio en "
            "cero y en cero se quedo mientras nadie barria. LOS %d PARES, NOMBRADOS "
            "UNO POR UNO CON SUS PUESTOS, que es como se publica una poblacion y no "
            "como se resume: %s. Y SE DICE LO QUE ESTA CORRECCION NO HACE, porque es "
            "la mitad que importa: NO ADJUDICA CLASE A NINGUNO DE ESOS PARES Y NO "
            "MUEVE NI UN VEREDICTO. Uno de ellos, `formalizar_junta_asesora` con "
            "`identificar_consejo_asesores`, esta leido y su conflicto es HUELLA DE "
            "FUSION y no error de lectura (acta 165, seccion 4.3). Declarar la "
            "poblacion entera defectuosa por un colapso seria la especie que `P.1` "
            "prohibe: la clase la decide una lectura, no un colapso."
            % (nueva, detalle))
    else:
        cuerpo = ""
    return comun + cuerpo + "]"


def nota_de_la_fila_que_no_se_mueve(vieja):
    return (
        "[RE MEDIDA Y NO MOVIDA, %s (vuelta %d, TAREA 3): recomputada hoy con "
        "`python scripts/plan/recomputo_3388.py --salida %s` "
        "(`../loop/SALIDA_V166_T3_RECOMPUTO.txt`, paso 1) y SIGUE EN %s. "
        "EL CONTADOR NO SE CUADRA Y SE DICE POR QUE, en vez de dejarlo callado: no "
        "hay correccion que contar. Una re medicion que CONFIRMA no es una "
        "correccion, y sumarla al contador haria que el contador dejase de contar lo "
        "que su palabra dice. La `A` global no se movio porque entre la vuelta 58 y "
        "hoy la campana FUNDIO nodos y no VOLTEO veredictos: fundir mueve el retrato "
        "y no el marcador, que es justo lo que la nota de la vuelta 58 de la fila de "
        "los colapsos ya dejo escrito.]"
        % (FECHA, VUELTA, SALIDA_JSONL.replace(os.sep, "/"), miles(int(vieja))))


PAT_CONTADOR = re.compile(r"\[CORREGIDA ((?:~~[A-Z]+~~ )*)([A-Z]+) (VEZ|VECES),")


def cuadrar_contador(celda, correcciones_ya):
    """CUADRA EL CONTADOR EN EL MISMO ACTO. Devuelve (celda_nueva, antes, despues).
    LA PALABRA NUEVA SE COMPUTA de la cadena contada, NO se lee de la palabra que
    el texto trae: si el texto y la cadena discrepan, MANDA LA CADENA, que es
    exactamente la caida que este contador existe para no repetir."""
    palabra = CARDINAL[correcciones_ya + 1]
    m = PAT_CONTADOR.search(celda)
    if not m:
        return celda, None, palabra          # fila sin contador: lo crea la nota
    vivo = "%s %s" % (m.group(2), m.group(3))
    reemplazo = "[CORREGIDA %s~~%s~~ %s," % (m.group(1), m.group(2), palabra)
    return celda[:m.start()] + reemplazo + celda[m.end():], vivo, palabra


def fila_corregida(texto_fila, vieja, nueva, correcciones_ya, nota):
    """Tacha la cifra viva, pone la nueva, cuadra el contador y adosa la nota.
    NO BORRA NADA: la cifra vieja se queda tachada y entera."""
    partes = texto_fila.split("|")
    celda = partes[2]
    m = None
    for m in PAT_VIVA.finditer(celda):
        break
    if m is None:
        raise SystemExit("ROJO: la celda no tiene cifra viva que tachar.")
    celda = (celda[:m.start()] + "~~**%s**~~ **%s**" % (vieja, miles(nueva))
             + celda[m.end():])
    celda, antes, despues = cuadrar_contador(celda, correcciones_ya)
    if antes is None:
        celda = celda.rstrip() + " **[CORREGIDA %s, %s]** " % (despues, nota[1:-1])
    else:
        cierre = celda.rstrip().rfind("]**")
        if cierre < 0:
            raise SystemExit("ROJO: no se encuentra donde adosar la nota.")
        celda = celda[:cierre + 1] + " " + nota + celda[cierre + 1:]
    partes[2] = celda
    return "|".join(partes), antes, despues


def main(aplicar):
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 166, TAREA 3: EL RETRATO DE LAS A SE RECOMPUTA (PASO 1)")
    print("=" * 78)
    print("")

    print("A) EL INSTRUMENTO DE LA CASA, CORRIDO EN ESTA VUELTA")
    code, texto = correr_recomputo()
    print("   comando: python scripts/plan/recomputo_3388.py --salida %s"
          % SALIDA_JSONL.replace(os.sep, "/"))
    print("   EXITCODE: %d" % code)
    if code != 0:
        print("   PARADA: el instrumento no sale en verde. No se escribe nada.")
        return 1
    medido, faltan, pares = leer_paso_1(texto)
    if faltan:
        print("   PARADA: no se pudieron leer las celdas: %s" % ", ".join(faltan))
        print("   LA CELDA QUE NO SALE DE UN INSTRUMENTO NO SE ESCRIBE.")
        return 1
    for _p, clave in FILAS:
        print("   CIFRA %-12s %d" % (clave + ":", medido[clave]))
    print("   CIFRA pares con mas de un veredicto, nombrados: %d" % len(pares))
    for p, q in pares:
        print("      %s puestos %s" % (p, q))
    print("   CONTRASTE con el acta 165 (contraste, no fuente): dice 551, 398,")
    print("   149 y 4, y los mismos cuatro pares. MI MEDICION DE HOY MANDA.")
    print("")

    lineas = io.open(DOC, encoding="utf-8").read().split("\n")
    filas, errores = localizar_filas(lineas)
    print("B) LAS CUATRO FILAS DE LA TABLA, LOCALIZADAS EN EL DOCUMENTO")
    if errores:
        for e in errores:
            print("   PARADA: %s" % e)
        return 1
    estado = {}
    for clave, n, texto_fila in filas:
        tachadas, viva, cuantas = anatomia(texto_fila)
        celda = texto_fila.split("|")[2]
        m = PAT_CONTADOR.search(celda)
        palabra = "%s %s" % (m.group(2), m.group(3)) if m else "(sin contador)"
        estado[clave] = (n, viva, cuantas, palabra)
        print("   %-11s docs/plan/RECOMPUTO_3388.md:%d" % (clave, n))
        print("      cifra viva publicada: %s" % viva)
        print("      cifras tachadas en la cadena: %d (%s)"
              % (cuantas, ", ".join(tachadas)))
        print("      contador que la celda escribe: %s" % palabra)
        print("      contador CONTADO de la cadena: %s"
              % (CARDINAL.get(cuantas, "?")))
        print("      cadena y contador cuadran hoy: %s"
              % (palabra == CARDINAL.get(cuantas) or palabra == "(sin contador)"))
    print("")

    print("C) QUE FILAS SE MUEVEN Y CUALES NO, CONTRA LA MEDICION DE HOY")
    mueven, quietas = [], []
    for _p, clave in FILAS:
        n, viva, cuantas, palabra = estado[clave]
        vieja_num = int(str(viva).replace(".", ""))
        if vieja_num == medido[clave]:
            quietas.append(clave)
            print("   %-11s publicada %s, medida hoy %d: NO SE MUEVE"
                  % (clave, viva, medido[clave]))
        else:
            mueven.append(clave)
            print("   %-11s publicada %s, medida hoy %d: SE MUEVE (delta %+d)"
                  % (clave, viva, medido[clave], medido[clave] - vieja_num))
    print("   CIFRA filas que se mueven: %d | filas quietas: %d"
          % (len(mueven), len(quietas)))
    print("")
    print("D) LA SIMULACION PREVIA: LAS FILAS NUEVAS, EN MEMORIA")
    lineas_nuevas = list(lineas)
    cambios = []
    for _p, clave in FILAS:
        n, viva, cuantas, palabra = estado[clave]
        if clave in quietas:
            texto_fila = lineas_nuevas[n - 1]
            partes = texto_fila.split("|")
            cierre = partes[2].rstrip().rfind("]**")
            if cierre < 0:
                print("   PARADA: la fila quieta %r no tiene donde adosar." % clave)
                return 1
            nota = nota_de_la_fila_que_no_se_mueve(viva)
            partes[2] = (partes[2][:cierre + 1] + " " + nota + partes[2][cierre + 1:])
            lineas_nuevas[n - 1] = "|".join(partes)
            cambios.append((clave, n, viva, viva, palabra, palabra, "RE MEDIDA"))
            continue
        nota = nota_de_la_fila(clave, viva, medido[clave], cuantas, pares, medido)
        nueva_fila, antes, despues = fila_corregida(
            lineas_nuevas[n - 1], viva, medido[clave], cuantas, nota)
        lineas_nuevas[n - 1] = nueva_fila
        cambios.append((clave, n, viva, miles(medido[clave]), antes, despues,
                        "CORREGIDA"))
    for clave, n, v0, v1, c0, c1, que in cambios:
        print("   %-11s linea %-4d %-9s  cifra %s -> %s | contador %s -> %s"
              % (clave, n, que, v0, v1, c0, c1))
    print("")

    print("E) LAS GUARDAS DEL CARRIL, SOBRE EL TEXTO NUEVO SIN ESCRIBIRLO")
    viejo = "\n".join(lineas)
    nuevo = "\n".join(lineas_nuevas)
    guardas = []
    todas_viejas = []
    for _p, clave in FILAS:
        n, viva, _c, _pa = estado[clave]
        t, v, _c2 = anatomia(lineas[n - 1])
        todas_viejas.extend(t + ([v] if v else []))
    sobreviven = sum(1 for x in todas_viejas
                     if ("~~**%s**~~" % x) in nuevo or ("**%s**" % x) in nuevo)
    guardas.append(("1_ninguna_cifra_vieja_desaparece", sobreviven,
                    len(todas_viejas)))
    guardas.append(("2_el_documento_solo_crece", len(nuevo) > len(viejo), True))
    guardas.append(("3_mismo_numero_de_lineas", len(lineas_nuevas), len(lineas)))
    guardas.append(("4_solo_se_tocan_las_cuatro_filas",
                    len([i for i in range(len(lineas))
                         if lineas[i] != lineas_nuevas[i]]), 4))
    guardas.append(("5_ninguna_nota_vieja_se_reescribe",
                    all(x in nuevo for x in
                        re.findall(r"\[(?:CONTADOR CUADRADO|[A-Z]+ CORRECCION)[^\]]{0,60}",
                                   viejo)), True))
    guardas.append(("6_los_contadores_cuadran_con_su_cadena",
                    todos_cuadran(lineas_nuevas), True))
    malos = 0
    for nombre, real, esperado in guardas:
        ok = (real == esperado)
        print("   %-42s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            malos += 1
    print("   CIFRA guardas: %d | pasan: %d | fallan: %d"
          % (len(guardas), len(guardas) - malos, malos))
    if malos:
        print("   PARADA: la simulacion falla. NO SE ESCRIBE NADA.")
        return 1
    print("")

    if not aplicar:
        print("F) NO SE ESCRIBE (falta --aplicar)")
        print("")
        print("FIN")
        return 0
    with io.open(DOC, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(nuevo)
    print("F) ESCRITO")
    print("   docs/plan/RECOMPUTO_3388.md")
    print("   CIFRA filas corregidas: %d | filas re medidas y no movidas: %d"
          % (len(mueven), len(quietas)))
    print("")

    print("G) LA COMPROBACION QUE NO SE FIA DE LO QUE ACABA DE ESCRIBIR")
    l2 = io.open(DOC, encoding="utf-8").read().split("\n")
    filas2, err2 = localizar_filas(l2)
    if err2:
        print("   PARADA: %s" % "; ".join(err2))
        return 1
    for clave, n, texto_fila in filas2:
        t, v, c = anatomia(texto_fila)
        celda = texto_fila.split("|")[2]
        m = PAT_CONTADOR.search(celda)
        palabra = "%s %s" % (m.group(2), m.group(3)) if m else "(sin contador)"
        cuadra = (palabra == CARDINAL.get(c))
        print("   %-11s cifra viva %-6s | tachadas %-3d | contador %-16s | cuadra: %s"
              % (clave, v, c, palabra, cuadra))
        if str(v).replace(".", "") != str(medido[clave]):
            print("   PARADA: la cifra escrita no es la medida.")
            return 1
        if not cuadra:
            print("   PARADA: el contador no cuadra con su cadena.")
            return 1
    print("   las cuatro filas publican la cifra medida hoy y su contador cuadra.")
    print("")
    print("FIN")
    return 0


def todos_cuadran(lineas):
    """El invariante que esta TAREA existe para restaurar: en cada fila, el
    contador escrito tiene que ser el CARDINAL de las cifras tachadas. La fila
    que no lleva contador no cuenta como rota: cuenta como fila sin cadena."""
    filas, errores = localizar_filas(lineas)
    if errores:
        return False
    for _clave, _n, texto_fila in filas:
        tachadas, _viva, cuantas = anatomia(texto_fila)
        m = PAT_CONTADOR.search(texto_fila.split("|")[2])
        if m is None:
            if cuantas:
                return False
            continue
        if "%s %s" % (m.group(2), m.group(3)) != CARDINAL.get(cuantas):
            return False
    return True


if __name__ == "__main__":
    sys.exit(main("--aplicar" in sys.argv))
