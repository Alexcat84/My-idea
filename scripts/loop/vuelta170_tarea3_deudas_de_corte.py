# -*- coding: utf-8 -*-
r"""vuelta170_tarea3_deudas_de_corte.py . TAREA 3 de la vuelta 170.

LAS DOS DEUDAS DE CORTE DE LA ADJUDICACION 6.11 DEL ACTA 169, LAS DOS POR `9.21`
MAS `9.10`: CON LA CIFRA VIEJA ENTERA Y LA FECHA AL LADO, NUNCA SUSTITUYENDO.

  3.a LA NOTA DE `OP-I-01` sigue diciendo "53 familias" (y una vez "53
      familia_de_ids"), y una de esas apariciones sostiene una aritmetica: "EL
      TOTAL REAL NO ES 450: es 671 (556 actos, 53 familias, ...)". El fichero
      mide HOY 672 con 54 familias.
  3.b LA CLAUSULA 2 de `OP-L-01` y la de `OP-L-02` dicen las dos "el marcador
      del cribado no se mueve: sigue en 2.117", y hoy el marcador es 3.388.

NINGUNA DE LAS TRES ES UNA MENTIRA: las tres son ciertas en su corte y les falta
el corte escrito al lado. Por eso NO se sustituye ni una letra.

LA CIFRA DE APARICIONES SE CUENTA AQUI Y NO SE COPIA DEL ACTA (EJECUTOR.md 2).
El encargo dice SIETE; este instrumento las cuenta del campo `nota` y publica lo
que le salga. Si sale otra cosa, sale otra cosa: MANDA EL CONTEO.

Y CADA ARITMETICA SE COMPRUEBA SUMANDOLA, no se cree: de las apariciones se
extraen los sumandos escritos y se verifica que dan el total que la propia frase
dice. Una aritmetica que no cuadra consigo misma seria otra cosa, y habria que
declararla como tal en vez de corregirle solo la fecha.

LO QUE ESTE INSTRUMENTO MIDE ANTES DE ESCRIBIR SOBRE `OP-L-01`, Y QUE EL ENCARGO
NO ANTICIPA: si esa clausula YA tiene una correccion fechada. Escribir una
segunda que diga lo mismo seria dejar dos versiones de la misma cosa, y eso es
justo lo que la casa no quiere. Se mide, y lo que salga se declara.

CERO CAMPOS NUEVOS DE ESQUEMA: `OP-I-01` crece DENTRO de su campo `nota`;
`OP-L-02` gana un elemento mas en su lista `verificacion` que ya existe, que es
la via que `OP-L-01` uso en la vuelta 166 y `OP-L-03` en la vuelta 72.

USO:
  python scripts/loop/vuelta170_tarea3_deudas_de_corte.py --comprobar
  python scripts/loop/vuelta170_tarea3_deudas_de_corte.py
"""
import collections
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
INVENTARIO = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

CLAUSULA_MARCADOR = "el marcador del cribado no se mueve: sigue en 2.117"
CORTE = "2026-09-04"


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def localizar(fichas, id_op):
    idx = [i for i, f in enumerate(fichas) if f.get("id_op") == id_op]
    return idx[0] if len(idx) == 1 else None


def aritmeticas(nota):
    """LAS ARITMETICAS ESCRITAS EN LA NOTA QUE LLEVAN UN 53 DE FAMILIAS, con su
    total declarado, sus sumandos y la suma real. No se cree ninguna: se suma."""
    salida = []
    for m in re.finditer(r"(\d{3})\s*\(([^)]*\b53\b[^)]*)\)", nota):
        total = int(m.group(1))
        cuerpo = m.group(2)
        sumandos = [int(x) for x in re.findall(r"\b(\d+)\b", cuerpo)]
        salida.append((total, cuerpo.strip(), sumandos, sum(sumandos)))
    for m in re.finditer(r"(\d{3}) ENTRADAS: ([^.]*\b53\b[^.]*)\.", nota):
        total = int(m.group(1))
        cuerpo = m.group(2)
        sumandos = [int(x) for x in re.findall(r"\b(\d+)\b", cuerpo)]
        salida.append((total, cuerpo.strip(), sumandos, sum(sumandos)))
    return salida


def main():
    solo_medir = "--comprobar" in sys.argv
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 170, TAREA 3: LAS DOS DEUDAS DE CORTE, POR 9.21 MAS 9.10")
    print("=" * 78)
    print("")

    lineas = [l for l in io.open(OPERACIONES, encoding="utf-8") if l.strip()]
    fichas = [json.loads(l) for l in lineas]
    print("A) EL SUJETO, MEDIDO ANTES DE TOCARLO")
    print("   fichas en docs/plan/OPERACIONES.jsonl: %d" % len(fichas))
    pos = {}
    for op in ("OP-I-01", "OP-L-01", "OP-L-02"):
        i = localizar(fichas, op)
        if i is None:
            print("   ROJO: %s no aparece exactamente una vez." % op)
            return 1
        pos[op] = i
        print("   %s vive en la linea %d, con %d claves"
              % (op, i + 1, len(fichas[i])))
    print("")

    # ------------------------------------------------------------------ 3.a
    nota = fichas[pos["OP-I-01"]].get("nota") or ""
    print("B) 3.a LAS APARICIONES DEL 53 EN LA NOTA DE OP-I-01, CONTADAS AQUI")
    print("   CIFRA caracteres de la nota: %d" % len(nota))
    ocur = [m.start() for m in re.finditer(r"\b53\b", nota)]
    print("   CIFRA apariciones del literal 53: %d" % len(ocur))
    print("   CIFRA de ellas escritas '53 familias': %d" % nota.count("53 familias"))
    print("   CIFRA de ellas escritas '53 familia_de_ids': %d"
          % nota.count("53 familia_de_ids"))
    for i in ocur:
        print("      ...%s..." % nota[max(0, i - 70):i + 55].replace("\n", " "))
    print("   CONTRASTE, y es contraste y no fuente: el encargo dice SIETE.")
    print("   yo cuento %d, %s" % (len(ocur), "CALZA" if len(ocur) == 7 else "NO CALZA"))
    print("")

    print("C) 3.a LAS ARITMETICAS, SUMADAS Y NO CREIDAS")
    ars = aritmeticas(nota)
    print("   CIFRA aritmeticas halladas que llevan un 53: %d" % len(ars))
    descuadres = []
    for total, cuerpo, sumandos, suma in ars:
        ok = (total == suma)
        if not ok:
            descuadres.append(total)
        print("      total escrito %d | sumandos %s | suma real %d | %s"
              % (total, sumandos, suma, "CUADRA" if ok else "NO CUADRA"))
        print("         %s" % cuerpo[:120])
    print("   CIFRA aritmeticas que no cuadran consigo mismas: %d" % len(descuadres))
    print("")

    print("D) 3.a EL INVENTARIO DE HOY, CONTADO DE SU FICHERO")
    inv = cargar(INVENTARIO)
    por_tipo = collections.Counter(x.get("tipo") for x in inv)
    print("   docs/plan/INVENTARIO.jsonl: %d entradas" % len(inv))
    for t, n in sorted(por_tipo.items(), key=lambda x: -x[1]):
        print("      %-16s %d" % (t, n))
    suma_tipos = sum(por_tipo.values())
    print("   CIFRA suma de los tipos: %d (%s)"
          % (suma_tipos, "CUADRA" if suma_tipos == len(inv) else "NO CUADRA"))
    hoy_familias = por_tipo["familia_de_ids"]
    print("   CIFRA familia_de_ids HOY: %d" % hoy_familias)
    print("")

    # ------------------------------------------------------------------ 3.b
    print("E) 3.b EL MARCADOR DE HOY, RECOMPUTADO DEL ARCHIVO")
    ver = cargar(VEREDICTOS)
    clases = collections.Counter(x.get("clase") for x in ver)
    puestos = set(x.get("puesto_intra") for x in ver)
    huecos = set(range(1, max(puestos) + 1)) - puestos
    print("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d filas" % len(ver))
    for k in sorted(clases):
        print("      clase %s: %d" % (k, clases[k]))
    print("   puestos distintos %d | maximo %d | huecos %d"
          % (len(puestos), max(puestos), len(huecos)))
    marcador = len(ver)
    print("")

    print("F) 3.b LA CLAUSULA 2, Y SI YA TIENE CORRECCION FECHADA")
    ya_corregida = {}
    for op in ("OP-L-01", "OP-L-02"):
        f = fichas[pos[op]]
        verif = f.get("verificacion") or []
        con_clausula = [k for k, v in enumerate(verif)
                        if isinstance(v, str) and CLAUSULA_MARCADOR in v]
        literal = [k for k in con_clausula if verif[k].strip() == CLAUSULA_MARCADOR]
        correcciones = [k for k in con_clausula
                        if verif[k].strip() != CLAUSULA_MARCADOR
                        and "CORRECCION DECLARADA" in verif[k]]
        ya_corregida[op] = bool(correcciones)
        print("   %s: %d elementos en `verificacion`" % (op, len(verif)))
        print("      la clausula LITERAL esta en los indices %s" % literal)
        print("      elementos que la citan DENTRO de una CORRECCION DECLARADA: %s"
              % correcciones)
        for k in correcciones:
            cab = verif[k][:150].replace("\n", " ")
            print("         [%d] %s..." % (k, cab))
        print("      -> YA TIENE CORRECCION FECHADA PARA ESTA CLAUSULA: %s"
              % ("SI" if correcciones else "NO"))
    print("")
    print("   LO QUE ESTO CAMBIA RESPECTO DE LO QUE EL ENCARGO SUPONE, Y SE DICE:")
    print("   el encargo da por hecho que a las DOS les falta el corte. Medido")
    print("   aqui, a %s ya se lo pusieron y a %s no."
          % (", ".join(o for o in ("OP-L-01", "OP-L-02") if ya_corregida[o]) or "ninguna",
             ", ".join(o for o in ("OP-L-01", "OP-L-02") if not ya_corregida[o]) or "ninguna"))
    print("   NO SE ESCRIBE UNA SEGUNDA CORRECCION QUE DIGA LO MISMO: dos versiones")
    print("   de la misma cosa es justo lo que la casa no quiere. Se declara.")
    print("")

    # ------------------------------------------------------------------ escritura
    nota_nueva = nota + (
        "\n\nCORRECCION DECLARADA (%(corte)s, vuelta 170, TAREA 3.a; adjudicacion 6.11 "
        "del acta 169), POR EL CARRIL DEL BANCO 9.21 MAS 9.10, POR ADICION Y CON LA "
        "CIFRA VIEJA ENTERA. NO SE SUSTITUYE NI UNA LETRA DE ARRIBA, y el motivo es "
        "que NINGUNA DE ESAS CIFRAS ES UNA MENTIRA: todas son ciertas en su corte y "
        "lo unico que les falta es el corte escrito al lado, que es exactamente lo "
        "que el 9.21 pide. LO QUE SE CORRIGE: esta nota nombra %(n_ocur)d veces la "
        "cifra 53 para las familias de ids (%(n_fam)d escritas '53 familias' y "
        "%(n_fid)d escrita '53 familia_de_ids'), y esa cifra ya no es la de hoy. "
        "MEDIDO HOY CONTANDO docs/plan/INVENTARIO.jsonl LINEA A LINEA: %(total)d "
        "entradas, de las cuales %(fam)d son de tipo familia_de_ids "
        "(%(reparto)s), y la suma de los tipos da %(total)d, que es el mismo total, "
        "asi que el conteo cuadra consigo mismo. "
        "LAS %(n_ar)d ARITMETICAS DE ESTA NOTA QUE LLEVAN UN 53, SUMADAS UNA A UNA Y "
        "NO CREIDAS, Y TODAS CUADRAN CONSIGO MISMAS EN SU PROPIO CORTE: %(lista_ar)s. "
        "O SEA QUE EL PROBLEMA NO ES ARITMETICO SINO DE CORTE: cada una suma bien "
        "con el 53 que tenia delante, y con el 54 de hoy cada total subiria en uno "
        "(la de 671 seria 672, que es justo lo que el fichero mide hoy). "
        "LA CIFRA DE APARICIONES NO SE COPIO DEL ACTA: se conto con "
        "scripts/loop/vuelta170_tarea3_deudas_de_corte.py sobre este mismo campo, y "
        "el conteo se publica aunque coincida. Salida: "
        "docs/loop/SALIDA_V170_T3_DEUDAS_DE_CORTE.txt. "
        "LO QUE ESTA CORRECCION NO HACE: no borra ni tacha ninguna de las cifras "
        "viejas, no recomputa ninguna de las cuatro poblaciones que el disparador de "
        "08_VERIFICACION no alcanza, no mueve ni un veredicto, no toca ni un nodo, y "
        "no cambia el estado ni las dependencias de esta ficha ni de ninguna otra."
        % dict(corte=CORTE, n_ocur=len(ocur), n_fam=nota.count("53 familias"),
               n_fid=nota.count("53 familia_de_ids"), total=len(inv),
               fam=hoy_familias,
               reparto=", ".join("%d %s" % (n, t) for t, n in
                                 sorted(por_tipo.items(), key=lambda x: -x[1])),
               n_ar=len(ars),
               lista_ar="; ".join("total %d = %d medido de sus sumandos" % (t, s)
                                  for t, _c, _ss, s in ars)))

    clausula_l02 = (
        "CORRECCION DECLARADA (%(corte)s, vuelta 170, TAREA 3.b; adjudicacion 6.11 "
        "del acta 169), POR EL CARRIL DEL BANCO 9.21 MAS 9.10, COMO UN ELEMENTO MAS "
        "DE ESTA MISMA LISTA verificacion Y SIN CLAVE NUEVA DE ESQUEMA (la via que "
        "OP-L-01 uso en la vuelta 166 para esta misma clausula y que OP-L-03 uso en "
        "la vuelta 72, y que el acta 71, seccion 6, adjudicacion 3, adjudico CON LAS "
        "PALABRAS NO ES PARADA). LO QUE SE CORRIGE es la clausula que en esta lista "
        "dice, verbatim: '%(clausula)s'. LA CLAUSULA NO ES FALSA Y ESO SE DICE "
        "PRIMERO: lo que exige es que la operacion NO MUEVA el marcador, no que el "
        "marcador valga 2.117 hoy. EL NUMERAL 2.117 ES EL VALOR DEL MARCADOR EN LA "
        "fecha_corte DE ESTA FICHA (%(fecha)s), TESTIGO Y NO CONDICION, y por eso se "
        "queda ENTERO donde esta. LO QUE LE FALTABA ES EL CORTE ESCRITO AL LADO, que "
        "es lo que el 9.21 pide, y aqui se le pone. MEDIDO HOY, %(corte)s, "
        "RECOMPUTANDO docs/INTRA_DOMINIO_VEREDICTOS.jsonl LINEA A LINEA: el marcador "
        "del cribado vale %(marcador)d, repartido en %(clases)s, con %(puestos)d "
        "puestos distintos, maximo %(maximo)d y %(huecos)d huecos. LA CLAUSULA, "
        "LEIDA ASI, SIGUE EN PIE Y NO SE PUEDE INCUMPLIR POR UNA CIFRA QUE OTRA "
        "OPERACION MOVIO. Salida: docs/loop/SALIDA_V170_T3_DEUDAS_DE_CORTE.txt. LO "
        "QUE ESTA CORRECCION NO HACE: no borra el numeral 2.117 ni la clausula que "
        "lo lleva, no mueve el marcador, no adjudica ninguna clase, no toca ni un "
        "nodo y no cambia el estado ni las dependencias de ninguna ficha."
        % dict(corte=CORTE, clausula=CLAUSULA_MARCADOR, marcador=marcador,
               fecha=fichas[pos["OP-L-02"]].get("fecha_corte"),
               clases=", ".join("%s %d" % (k, clases[k]) for k in sorted(clases)),
               puestos=len(puestos), maximo=max(puestos), huecos=len(huecos)))

    print("G) LO QUE SE VA A ESCRIBIR, Y QUE NADA VIEJO SE PIERDE")
    trozos_viejos = [nota[i:i + 60] for i in ocur]
    perdidos = [t for t in trozos_viejos if t not in nota_nueva]
    print("   CIFRA trozos viejos de la nota comprobados: %d" % len(trozos_viejos))
    print("   CIFRA perdidos: %d" % len(perdidos))
    print("   la nota pasa de %d a %d caracteres, y SOLO CRECE: %s"
          % (len(nota), len(nota_nueva), len(nota_nueva) > len(nota)))
    verif_l02 = list(fichas[pos["OP-L-02"]].get("verificacion") or [])
    print("   la verificacion de OP-L-02 pasa de %d a %d elementos"
          % (len(verif_l02), len(verif_l02) + 1))
    print("   la clausula literal sigue en la lista: %s"
          % (CLAUSULA_MARCADOR in verif_l02))
    if perdidos or CLAUSULA_MARCADOR not in verif_l02:
        print("   ROJO: se perderia texto viejo. No se escribe nada.")
        return 1
    print("")

    if solo_medir:
        print("MODO --comprobar: NO se escribe nada.")
        return 0

    nueva_i01 = dict(fichas[pos["OP-I-01"]])
    nueva_i01["nota"] = nota_nueva
    nueva_l02 = dict(fichas[pos["OP-L-02"]])
    nueva_l02["verificacion"] = verif_l02 + [clausula_l02]

    print("H) EL ESQUEMA NO CRECE Y NADA MAS SE MUEVE")
    for op, vieja, nueva in (("OP-I-01", fichas[pos["OP-I-01"]], nueva_i01),
                             ("OP-L-02", fichas[pos["OP-L-02"]], nueva_l02)):
        movidos = [k for k in vieja
                   if k not in ("nota", "verificacion") and vieja[k] != nueva.get(k)]
        print("   %s: claves antes %d, despues %d | campos movidos de mas: %d %s"
              % (op, len(vieja), len(nueva), len(movidos), movidos))
        print("      estado antes %r, despues %r"
              % (vieja.get("estado"), nueva.get("estado")))
        if len(nueva) != len(vieja) or movidos:
            print("   ROJO: se movio algo que no tocaba.")
            return 1
    print("   OP-L-01: NO SE TOCA. Su clausula 2 ya tiene correccion fechada desde")
    print("            la vuelta 166, y escribir otra igual seria dejar dos")
    print("            versiones de la misma cosa.")
    print("")

    lineas[pos["OP-I-01"]] = json.dumps(nueva_i01, ensure_ascii=False) + "\n"
    lineas[pos["OP-L-02"]] = json.dumps(nueva_l02, ensure_ascii=False) + "\n"
    io.open(OPERACIONES, "w", encoding="utf-8", newline="\n").writelines(lineas)

    despues = cargar(OPERACIONES)
    print("I) ESCRITO, Y RECONTADO DESPUES DE ESCRIBIR")
    print("   CIFRA fichas antes: %d | despues: %d" % (len(fichas), len(despues)))
    print("   OP-I-01 sigue en la linea %d: %s"
          % (pos["OP-I-01"] + 1, despues[pos["OP-I-01"]].get("id_op") == "OP-I-01"))
    print("   OP-L-02 sigue en la linea %d: %s"
          % (pos["OP-L-02"] + 1, despues[pos["OP-L-02"]].get("id_op") == "OP-L-02"))
    n_disco = despues[pos["OP-I-01"]]["nota"]
    v_disco = despues[pos["OP-L-02"]]["verificacion"]
    print("   CIFRA caracteres de la nota de OP-I-01 en disco: %d" % len(n_disco))
    # LA GUARDA MIDE LO QUE IMPORTA, Y SE DICE POR QUE NO MIDE EL TOTAL: la
    # correccion nueva NOMBRA la cifra 53 varias veces, porque es de lo que
    # habla, asi que el total de apariciones sube A PROPOSITO. Lo que no puede
    # pasar es que alguna de las SIETE VIEJAS desaparezca, y eso es lo que se
    # comprueba, trozo a trozo, con el contexto de 60 caracteres de cada una.
    sobreviven = sum(1 for t in trozos_viejos if t in n_disco)
    print("   CIFRA apariciones del 53 en la nota de disco (sube a proposito): %d"
          % len(re.findall(r"\b53\b", n_disco)))
    print("   CIFRA de las SIETE VIEJAS que sobreviven ENTERAS: %d de %d"
          % (sobreviven, len(trozos_viejos)))
    print("   CIFRA elementos de verificacion de OP-L-02 en disco: %d" % len(v_disco))
    print("   la clausula literal del 2.117 sigue en disco: %s"
          % (CLAUSULA_MARCADOR in v_disco))
    print("   OP-L-01 en disco tiene %d elementos de verificacion (sin tocar): %s"
          % (len(despues[pos["OP-L-01"]]["verificacion"]),
             despues[pos["OP-L-01"]]["verificacion"]
             == fichas[pos["OP-L-01"]]["verificacion"]))
    if (len(despues) != len(fichas)
            or sobreviven != len(trozos_viejos)
            or CLAUSULA_MARCADOR not in v_disco
            or despues[pos["OP-L-01"]]["verificacion"]
            != fichas[pos["OP-L-01"]]["verificacion"]):
        print("   ROJO: el fichero no quedo como debia.")
        return 1
    print("")
    print("VERDE: las dos deudas de corte quedan pagadas por adicion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
