# -*- coding: utf-8 -*-
r"""_v214_t1_marcar_95.py . LA TAREA 1.a Y 1.b DE LA VUELTA 214: LAS 95 ENTRADAS
DEL INVENTARIO CON COBERTURA INCOMPLETA SE MARCAN PROVISIONAL, POR INSTRUMENTO Y
NUNCA A MANO.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO: fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3, que ademas protege justo este trabajo,
porque esto es PLAN y no maquinaria de vigilancia).

QUIEN LO ORDENA, POR SU RUTA Y NO DE MEMORIA:
docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md, DECISION 1.

LA DOCTRINA: banco 9.26, "mientras falte un par, la forma es PROVISIONAL y se
dice asi". No hace falta COMPLETAR la cobertura: hace falta MARCARLA.

LA SEDE ES EL CAMPO forma, Y NO SE ELIGE POR GUSTO: el instrumento que la
vuelta 203 uso para medir esta misma clausula (scripts/loop/_v203_t3_op_i_01.py,
su linea 258) mide con "PROVISIONAL" in (r.get("forma") or ""), o sea que la
clausula 2 de OP-I-01 se lee sobre el campo forma. Ademas ese campo YA lleva
marcas en mayusculas (FUNDIDA), segun el censo de la vuelta 171.

EL TEXTO VIEJO NO SE TAPA (banco 9.10 y EJECUTOR.md 8): la marca se ANEXA
detras del texto viejo del campo, entero y sin tachar.

CERO CIFRAS TECLEADAS: la N y la M de cada entrada se leen de su propio campo
cobertura; el numero de vuelta sale del nombre de este fichero.

USO:
  python scripts/loop/_v214_t1_marcar_95.py --simular
  python scripts/loop/_v214_t1_marcar_95.py --mutantes
  python scripts/loop/_v214_t1_marcar_95.py --escribir
"""
import hashlib
import io
import json
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INV = "docs/plan/INVENTARIO.jsonl"
VUELTA = int(re.search(r"_v(\d+)_",
                       os.path.basename(os.path.abspath(__file__))).group(1))

PAT = re.compile(r"^(\d+) de (\d+) pares leidos")
RUTA_DECISION = "docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md"
FECHA = "2026-09-09"


def leer_lineas():
    """EL FICHERO ENTERO, LINEA A LINEA Y SIN NORMALIZAR NADA."""
    p = os.path.join(RAIZ, INV.replace("/", os.sep))
    crudo = io.open(p, encoding="utf-8", newline="").read()
    return crudo


def sha(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()[:16]


def clasificar(d):
    """DEVUELVE (con_forma, incompleta, n, m) LEYENDO SOLO EL CAMPO cobertura.
    PURA: no lee ni escribe nada."""
    m = PAT.match(str(d.get("cobertura") or ""))
    if not m:
        return (False, False, None, None)
    n, mm = int(m.group(1)), int(m.group(2))
    return (True, n < mm, n, mm)


def marca_de(d):
    """EL TEXTO DE LA MARCA, COMPUESTO DE LOS PROPIOS DATOS DE LA ENTRADA.
    PURA. Las dos cifras salen del campo cobertura y no se teclean."""
    _, _, n, mm = clasificar(d)
    return (" FORMA PROVISIONAL (banco 9.26): la cobertura de esta entrada es "
            "INCOMPLETA, %d de %d pares leidos, y mientras falte un par la forma "
            "es PROVISIONAL y se dice asi. MARCADA EN LA VUELTA %d (%s) POR "
            "DECISION DEL FUNDADOR, %s, DECISION 1, y por el carril del banco "
            "9.10: el texto viejo de este campo va entero y sin tachar delante "
            "de esta marca, que se ANEXA y no sustituye. La marca NO completa la "
            "cobertura: la DICE." % (n, mm, VUELTA, FECHA, RUTA_DECISION))


def ya_marcada(d):
    return "PROVISIONAL" in (d.get("forma") or "")


# LAS DOS CONVENCIONES DE VOLCADO QUE ESTE FICHERO TIENE DENTRO, Y NO ES UN
# DETALLE: la simulacion de esta misma vuelta midio que 335 de sus 672 lineas se
# volcaron con separadores COMPACTOS y las otras 337 con los de por defecto. Un
# re-volcado ciego reformatearia 335 lineas que nadie mando tocar. Por eso cada
# linea se vuelve a volcar CON SU PROPIA CONVENCION, elegida probando cual
# reproduce la linea original BYTE A BYTE antes de tocarle nada.
CONVENCIONES = ((", ", ": "), (",", ":"))


def convencion_de(linea, d):
    """LA CONVENCION CON LA QUE ESTA LINEA SE ESCRIBIO, MEDIDA Y NO SUPUESTA:
    la que reproduce la linea original tal cual. Devuelve None si ninguna lo
    hace, que es caso ROJO. PURA."""
    for sep in CONVENCIONES:
        if json.dumps(d, ensure_ascii=False, separators=sep) == linea:
            return sep
    return None


def componer(crudo):
    """COMPONE EL FICHERO NUEVO EN MEMORIA. Devuelve (texto_nuevo, informe).
    Las lineas que no se tocan salen BYTE A BYTE como entraron, porque no se
    re-vuelcan: se copian."""
    partes = crudo.split(NL)
    nuevas = list(partes)
    tocadas = []
    no_round = []
    convs = {}
    con_forma = 0
    incompletas = 0
    for i, linea in enumerate(partes):
        if not linea.strip():
            continue
        d = json.loads(linea)
        sep = convencion_de(linea, d)
        # LA FIDELIDAD SE COMPRUEBA EN TODAS, NO SOLO EN LAS QUE SE TOCAN
        if sep is None:
            no_round.append(i + 1)
        else:
            convs[sep] = convs.get(sep, 0) + 1
        cf, inc, _n, _m = clasificar(d)
        if cf:
            con_forma += 1
        if not (cf and inc):
            continue
        incompletas += 1
        if ya_marcada(d) or sep is None:
            continue
        viejo = d.get("forma") or ""
        d["forma"] = viejo + "." + marca_de(d)
        nuevas[i] = json.dumps(d, ensure_ascii=False, separators=sep)
        tocadas.append((i + 1, d.get("nombre"), viejo, d["forma"], sep))
    return NL.join(nuevas), {
        "lineas": len(partes),
        "entradas": sum(1 for l in partes if l.strip()),
        "con_forma": con_forma,
        "incompletas": incompletas,
        "tocadas": tocadas,
        "no_round": no_round,
        "convs": convs,
    }


def juzgar(crudo_antes, texto_despues, esperado=95):
    """EL JUICIO ENTERO SOBRE LOS DOS TEXTOS. Devuelve (fallos, lineas).
    PURA: recibe los dos textos y no lee ni escribe nada. Es lo que se muta."""
    L = []
    fallos = 0

    def w(s):
        L.append(s)

    la = crudo_antes.split(NL)
    lb = texto_despues.split(NL)
    A = [json.loads(l) for l in la if l.strip()]
    B = [json.loads(l) for l in lb if l.strip()]

    def chequeo(nombre, ok, glosa):
        nonlocal fallos
        w("   %-62s %s" % (nombre, "VERDE" if ok else "ROJO"))
        w("      %s" % glosa)
        if not ok:
            fallos += 1

    chequeo("el numero de entradas no se mueve",
            len(A) == len(B),
            "CIFRA entradas antes %d, despues %d" % (len(A), len(B)))
    if len(A) != len(B):
        return fallos, L

    inc_a = [i for i, d in enumerate(A) if clasificar(d)[0] and clasificar(d)[1]]
    inc_b = [i for i, d in enumerate(B) if clasificar(d)[0] and clasificar(d)[1]]
    chequeo("las mismas entradas siguen siendo las INCOMPLETAS",
            inc_a == inc_b,
            "CIFRA incompletas antes %d, despues %d, en los mismos indices: %s"
            % (len(inc_a), len(inc_b), "SI" if inc_a == inc_b else "NO"))
    chequeo("las INCOMPLETAS son EXACTAMENTE las que el encargo nombra",
            len(inc_b) == esperado,
            "CIFRA incompletas medidas %d, esperadas por el encargo %d"
            % (len(inc_b), esperado))

    marcadas_b = [i for i, d in enumerate(B) if ya_marcada(d)]
    marcadas_inc = [i for i in marcadas_b if i in set(inc_b)]
    marcadas_fuera = [i for i in marcadas_b if i not in set(inc_b)]
    marcadas_a_fuera = [i for i, d in enumerate(A)
                        if ya_marcada(d) and i not in set(inc_a)]
    chequeo("TODAS las incompletas quedan marcadas PROVISIONAL en su forma",
            len(marcadas_inc) == len(inc_b),
            "CIFRA incompletas %d, de ellas marcadas %d"
            % (len(inc_b), len(marcadas_inc)))
    chequeo("NINGUNA entrada COMPLETA gana la marca en esta vuelta",
            marcadas_fuera == marcadas_a_fuera,
            "CIFRA marcadas fuera de las incompletas antes %d, despues %d "
            "(las de antes NO son mias y no se tocan)"
            % (len(marcadas_a_fuera), len(marcadas_fuera)))

    cambiadas = [i for i in range(len(A))
                 if json.dumps(A[i], ensure_ascii=False)
                 != json.dumps(B[i], ensure_ascii=False)]
    chequeo("se mueven EXACTAMENTE las incompletas y ninguna mas",
            sorted(cambiadas) == sorted(inc_b),
            "CIFRA entradas cuyo JSON cambia %d, incompletas %d, son las mismas: %s"
            % (len(cambiadas), len(inc_b),
               "SI" if sorted(cambiadas) == sorted(inc_b) else "NO"))

    solo_forma = True
    prefijo_intacto = True
    cobertura_quieta = True
    for i in cambiadas:
        a, b = A[i], B[i]
        if set(a.keys()) != set(b.keys()):
            solo_forma = False
            continue
        for k in a:
            if k == "forma":
                continue
            if json.dumps(a[k], ensure_ascii=False) != json.dumps(b[k], ensure_ascii=False):
                solo_forma = False
        if not (b.get("forma") or "").startswith(a.get("forma") or ""):
            prefijo_intacto = False
        if (a.get("cobertura") or "") != (b.get("cobertura") or ""):
            cobertura_quieta = False
    chequeo("de las que se mueven, SOLO se mueve el campo forma",
            solo_forma,
            "ningun otro campo cambia en ninguna de las %d" % len(cambiadas))
    chequeo("el texto viejo de forma queda ENTERO Y DELANTE, sin tapar",
            prefijo_intacto,
            "la forma nueva EMPIEZA por la vieja en las %d" % len(cambiadas))
    chequeo("el campo cobertura no se toca (la marca DICE, no COMPLETA)",
            cobertura_quieta,
            "CIFRA coberturas movidas: 0 de %d" % len(cambiadas))

    cita = [i for i in cambiadas if RUTA_DECISION in (B[i].get("forma") or "")
            and "9.26" in (B[i].get("forma") or "")]
    chequeo("cada marca cita el banco 9.26 y la decision POR SU RUTA",
            len(cita) == len(cambiadas),
            "CIFRA marcas con las dos citas %d de %d" % (len(cita), len(cambiadas)))

    cifras_ok = 0
    for i in cambiadas:
        _, _, n, mm = clasificar(B[i])
        if ("%d de %d pares leidos" % (n, mm)) in (B[i].get("forma") or ""):
            cifras_ok += 1
    chequeo("la N y la M de cada marca salen de SU PROPIA cobertura",
            cifras_ok == len(cambiadas),
            "CIFRA marcas cuya pareja de cifras calza con su cobertura %d de %d"
            % (cifras_ok, len(cambiadas)))

    # LA GUARDA DE BYTES, QUE ES LA QUE LA SIMULACION DE ESTA VUELTA GANO:
    # las lineas que no son de las 95 tienen que salir IGUALES BYTE A BYTE, no
    # solo equivalentes en JSON. Un re-volcado con la otra convencion pasaria el
    # cotejo semantico y reformatearia 335 lineas que nadie mando tocar.
    mismas = len(la) == len(lb)
    iguales = 0
    reformateadas = []
    if mismas:
        inc_set = set()
        j = -1
        for i, l in enumerate(la):
            if not l.strip():
                continue
            j += 1
            if j in set(inc_b):
                inc_set.add(i)
        for i in range(len(la)):
            if i in inc_set:
                continue
            if la[i] == lb[i]:
                iguales += 1
            else:
                reformateadas.append(i + 1)
    chequeo("las lineas que NO son de las 95 salen IGUALES BYTE A BYTE",
            mismas and not reformateadas,
            "CIFRA lineas identicas %d, CIFRA lineas reformateadas sin mandato %d"
            % (iguales, len(reformateadas)))

    largos = texto_despues.count(chr(8212)) + texto_despues.count(chr(8211))
    chequeo("cero guiones largos y cero guiones medios",
            largos == 0,
            "CIFRA guiones largos mas medios: %d" % largos)
    return fallos, L


def informe_conteo(titulo, crudo):
    E = [json.loads(l) for l in crudo.split(NL) if l.strip()]
    con_forma = sum(1 for d in E if clasificar(d)[0])
    inc = [d for d in E if clasificar(d)[0] and clasificar(d)[1]]
    inc_marc = sum(1 for d in inc if ya_marcada(d))
    todo_prov = sum(1 for d in E
                    if "PROVISIONAL" in json.dumps(d, ensure_ascii=False).upper())
    forma_prov = sum(1 for d in E if ya_marcada(d))
    L = [titulo,
         "   CIFRA entradas del inventario: %d" % len(E),
         "   CIFRA entradas con cobertura de la forma 'N de M pares leidos': %d"
         % con_forma,
         "   CIFRA de esas que estan INCOMPLETAS (N menor que M): %d" % len(inc),
         "   CIFRA de esas incompletas con PROVISIONAL en su campo forma: %d"
         % inc_marc,
         "   CIFRA entradas del fichero entero con PROVISIONAL en su campo forma: %d"
         % forma_prov,
         "   CIFRA entradas del fichero entero con PROVISIONAL en CUALQUIER campo: %d"
         % todo_prov,
         "   CIFRA bytes: %d | sha256 %s" % (len(crudo.encode("utf-8")), sha(crudo))]
    return L


def main():
    modo = sys.argv[1] if len(sys.argv) > 1 else "--simular"
    out = []

    def w(s=""):
        out.append(s)

    w("=" * 78)
    w("VUELTA %d, TAREA 1.a Y 1.b. LAS 95 SE DICEN. MODO %s" % (VUELTA, modo))
    w("=" * 78)
    w("QUIEN LO ORDENA: %s, DECISION 1" % RUTA_DECISION)
    w("LA DOCTRINA: banco 9.26. LA SEDE: el campo forma, por el precedente de")
    w("scripts/loop/_v203_t3_op_i_01.py linea 258, que mide esta misma clausula")
    w("sobre ese campo.")
    w("")

    crudo = leer_lineas()
    for l in informe_conteo("EL CONTEO ANTES, SOBRE EL FICHERO EN DISCO:", crudo):
        w(l)
    w("")

    nuevo, inf = componer(crudo)
    w("LO QUE EL COMPOSITOR HIZO, EN MEMORIA:")
    w("   CIFRA lineas del fichero (incluida la ultima vacia): %d" % inf["lineas"])
    w("   CIFRA entradas no vacias: %d" % inf["entradas"])
    w("   CIFRA con forma N de M: %d" % inf["con_forma"])
    w("   CIFRA INCOMPLETAS: %d" % inf["incompletas"])
    w("   CIFRA entradas que el compositor MARCA en esta corrida: %d"
      % len(inf["tocadas"]))
    w("   LAS DOS CONVENCIONES DE VOLCADO QUE ESTE FICHERO TIENE DENTRO, MEDIDAS:")
    for sep, n in sorted(inf["convs"].items()):
        w("      separadores %-12r -> %d linea(s)" % (sep, n))
    w("   CIFRA lineas que NO vuelven a su propio texto con NINGUNA de las dos: %d"
      % len(inf["no_round"]))
    if inf["no_round"]:
        w("   ROJO: el volcado no es fiel y una linea sin tocar cambiaria sola.")
        for n in inf["no_round"][:10]:
            w("      linea %d" % n)
    w("")

    w("LA GUARDA DEL ENCARGO: SI EL INSTRUMENTO MARCA UN NUMERO DISTINTO DE 95,")
    w("SE PARA Y SE TRAE, EN VEZ DE AJUSTAR LA CIFRA.")
    w("   CIFRA que el encargo nombra: 95")
    w("   CIFRA que este instrumento mide: %d" % inf["incompletas"])
    w("   CALZAN: %s" % ("SI" if inf["incompletas"] == 95 else "NO, Y ESTO ES PARADA"))
    w("")
    if inf["incompletas"] != 95 or inf["no_round"]:
        w("ROJO: no se escribe nada.")
        sys.stdout.write(NL.join(out) + NL)
        return 1

    w("LAS TRES PRIMERAS MARCAS, ENTERAS, PARA QUE SE VEA LA FORMA DEL TEXTO:")
    for ln, nombre, viejo, nuevo_f, sep in inf["tocadas"][:3]:
        w("   linea %d | %s | convencion de volcado %r" % (ln, nombre, sep))
        w("      VIEJO: %s" % viejo)
        w("      NUEVO: %s" % nuevo_f)
    w("")

    w("EL JUICIO ENTERO, SOBRE LOS DOS TEXTOS:")
    fallos, lineas = juzgar(crudo, nuevo)
    out.extend(lineas)
    w("   CIFRA comprobaciones que fallan: %d" % fallos)
    w("")

    if modo == "--mutantes":
        w("=" * 78)
        w("LA PRUEBA DE MUTACION DEL JUICIO (EJECUTOR.md 1, EL CASO ROJO SE PRUEBA")
        w("POR MUTACION). CADA MUTANTE ES EL TEXTO BUENO CON UN DANO, Y EL JUICIO")
        w("TIENE QUE CAER EN LOS CINCO. Si alguno pasa, el juicio no vale.")
        w("=" * 78)
        # EL MUTANTE SE HACE POR SUSTITUCION DE UNA SOLA LINEA DEL TEXTO BUENO,
        # NO RE-VOLCANDO EL FICHERO ENTERO. Si se re-volcara entero, los cinco
        # mutantes caerian por la guarda de bytes y no por su propio dano, y una
        # prueba de mutacion que cae siempre por el mismo sitio no prueba nada.
        lineas_b = nuevo.split(NL)
        idx_lin = [i for i, l in enumerate(lineas_b) if l.strip()]

        def mutar(pos_entrada, cambio):
            """Devuelve el texto bueno con UNA linea cambiada, volcada con SU
            PROPIA convencion. PURA."""
            i = idx_lin[pos_entrada]
            d = json.loads(lineas_b[i])
            sep = convencion_de(lineas_b[i], d)
            cambio(d)
            copia = list(lineas_b)
            copia[i] = json.dumps(d, ensure_ascii=False, separators=sep)
            return NL.join(copia)

        base = [json.loads(l) for l in nuevo.split(NL) if l.strip()]
        inc_pos = [i for i, d in enumerate(base)
                   if clasificar(d)[0] and clasificar(d)[1]]
        com_pos = [i for i, d in enumerate(base)
                   if clasificar(d)[0] and not clasificar(d)[1]]

        def sin_marca(d):
            # TODAS las apariciones, no la primera: el texto de la marca dice
            # PROVISIONAL DOS veces, y quitar solo una deja la entrada MARCADA
            # igualmente. La primera version de este mutante quitaba una sola y
            # PASABA el juicio; el defectuoso era el mutante y no el juicio, y
            # eso es exactamente lo que la prueba de mutacion existe para cazar.
            d["forma"] = d["forma"].replace("PROVISIONAL", "x")

        def con_marca(d):
            d["forma"] = (d.get("forma") or "") + " PROVISIONAL"

        def tapando(d):
            d["forma"] = marca_de(d).strip()

        def otro_campo(d):
            d["nota"] = (d.get("nota") or "") + " tocado"

        def cifras_falsas(d):
            d["forma"] = re.sub(r"\d+ de \d+ pares leidos",
                                "999 de 999 pares leidos", d["forma"], count=1)

        def sin_cita(d):
            d["forma"] = d["forma"].replace(RUTA_DECISION, "una ruta cualquiera")

        mutantes = [
            ("A. una de las 95 se queda SIN marcar", inc_pos[0], sin_marca),
            ("B. una entrada COMPLETA gana la marca", com_pos[0], con_marca),
            ("C. la marca TAPA el texto viejo en vez de anexarse", inc_pos[1], tapando),
            ("D. se mueve un campo que no es forma", inc_pos[2], otro_campo),
            ("E. las cifras de la marca no calzan con su cobertura", inc_pos[3],
             cifras_falsas),
            ("F. la marca no cita la decision por su ruta", inc_pos[4], sin_cita),
        ]

        caen = 0
        for nombre, pos, cambio in mutantes:
            f, ll = juzgar(crudo, mutar(pos, cambio))
            rotas = [x.strip() for x in ll if x.strip().endswith("ROJO")]
            w("   MUTANTE %-52s fallos %d -> %s"
              % (nombre, f, "CAE, como debe" if f > 0 else "PASA, Y ESO ES ROJO"))
            for r in rotas:
                w("      cae por> %s" % r)
            if f > 0:
                caen += 1
        w("   CIFRA mutantes %d | CIFRA que caen %d | se exigen %d"
          % (len(mutantes), caen, len(mutantes)))
        w("   Y EL CASO POSITIVO, para que la prueba no sea trivial: el texto")
        w("   bueno SIN mutar pasa por el MISMO juicio y da %d fallos." % fallos)
        w("")
        sys.stdout.write(NL.join(out) + NL)
        return 0 if (caen == len(mutantes) and fallos == 0) else 1

    if modo == "--escribir":
        if fallos:
            w("ROJO: el juicio no da cero. NO SE ESCRIBE. El fichero queda intacto.")
            sys.stdout.write(NL.join(out) + NL)
            return 1
        p = os.path.join(RAIZ, INV.replace("/", os.sep))
        io.open(p, "w", encoding="utf-8", newline="").write(nuevo)
        de_nuevo = leer_lineas()
        w("ESCRITO %s" % INV)
        w("   RELECTURA DEL DISCO: identica a lo juzgado: %s"
          % ("SI" if de_nuevo == nuevo else "NO"))
        w("")
        for l in informe_conteo("EL CONTEO DESPUES, RELEYENDO EL DISCO:", de_nuevo):
            w(l)
        w("")
        f2, l2 = juzgar(crudo, de_nuevo)
        w("EL JUICIO OTRA VEZ, YA CONTRA EL DISCO:")
        out.extend(l2)
        w("   CIFRA comprobaciones que fallan sobre el disco: %d" % f2)
        w("")
        w("VERDE: las 95 estan dichas." if (f2 == 0 and de_nuevo == nuevo)
          else "ROJO: lo escrito no es lo juzgado.")
        sys.stdout.write(NL.join(out) + NL)
        return 0 if (f2 == 0 and de_nuevo == nuevo) else 1

    w("SIMULACION: NO SE ESCRIBE NADA. El fichero en disco queda como estaba.")
    sys.stdout.write(NL.join(out) + NL)
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
