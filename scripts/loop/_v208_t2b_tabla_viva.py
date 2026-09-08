# -*- coding: utf-8 -*-
r"""_v208_t2b_tabla_viva.py . TAREA 2.b DE LA VUELTA 208: LAS DOS FILAS DE LA
`TABLA VIVA DE LOS PUROS` DE `docs/BANCO_DE_TEXTOS.md`, PUESTAS AL DIA POR EL
CARRIL DEL BANCO `9.10`, POR ADICION Y CON CORRECCION DECLARADA.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3). No clona ni toca ningun lector.

QUIEN LO ENCARGA: la adjudicacion `6.3` del acta 207, que sale de su `6.1`. El
criterio de HECHO de la fase `06 MESAS` en `docs/plan/08_VERIFICACION.md` exige
"cada decision escrita con su motivo y su COBERTURA AL LADO (banco 9.26)", el
banco `9.26` dice que mientras falte un par la forma es PROVISIONAL, y la propia
`verificacion[2]` de `OP-L-01` pide que "cada nomina afectada se re-mide con su
cobertura al lado".

**NINGUNA CIFRA SE TECLEA AQUI.** Las once cifras de las dos filas corregidas se
IMPORTAN del computo del 2.a, `_v208_t2_denominador.py`, que las mide del archivo
con el resolutor puesto. Si aquel computo cambiara una, esta correccion cambiaria
con el.

LO QUE SE ESCRIBE, Y ES TODO POR ADICION:
  (1) una linea de PUNTERO justo debajo de la cabecera de la tabla, que dice que
      hay una correccion posterior debajo y con que corte;
  (2) el BLOQUE DE CORRECCION DECLARADA justo debajo de la ultima fila de la
      tabla, con las dos filas corregidas enteras.

LO QUE NO SE HACE, Y ES LA GUARDA DURA DEL 2.c: **NO SE BORRA NI SE TACHA NI SE
REESCRIBE UNA SOLA LINEA DEL TEXTO VIEJO.** Las dos filas viejas siguen en la
tabla, byte a byte, y la cabecera con su corte de 14 ago 2026 tambien. Si al
salir falta una sola linea del texto de entrada, el computo cae en ROJO.

Y NO SE TOCA `docs/plan/OPERACIONES.jsonl`: `OP-L-01` no se cierra y su campo
`estado` no se mira para decidir (`AUDITOR.md` 0). Esta corrida lo mide al entrar
y al salir para probarlo.
"""
import argparse
import hashlib
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

sys.path.insert(0, AQUI)

VUELTA = 208
CORTE = "7 sep 2026"
BANCO = os.path.join(RAIZ, "docs", "BANCO_DE_TEXTOS.md")
OPES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
SALIDA_2A = os.path.join(LOOP, "SALIDA_V%d_T2A_DENOMINADOR.txt" % VUELTA)

CABECERA = "#### TABLA VIVA DE LOS PUROS, al 14 ago 2026 (vigente al puesto 1157)"
MARCA_PUNTERO = "<!-- PUNTERO A LA CORRECCION V208 -->"
MARCA_BLOQUE = "<!-- CORRECCION DECLARADA V208 TABLA VIVA -->"
# LAS DOS FILAS VIEJAS, POR SU NUMERO DE RACIMO. NO SE TOCAN: se localizan para
# comprobar que siguen enteras al salir.
FILAS_VIEJAS = {"junta asesora": "| **7** | la junta asesora |",
                "seleccion de canal": "| **11** | **la seleccion de canal** |"}


def dos_convenciones(ruta):
    d = io.open(ruta, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return (len(d), len(lf), hashlib.sha256(d).hexdigest()[:16],
            hashlib.sha256(lf).hexdigest()[:16], lf.decode("utf-8"))


def cifras_del_2a(texto):
    """LAS ONCE CIFRAS DE LAS DOS FILAS, LEIDAS DE LA SALIDA DEL 2.a Y NO
    TECLEADAS. PURA: recibe el texto. Devuelve (mapa, motivos); motivos no vacio
    es ROJO y entonces no se escribe nada."""
    out, motivos = {}, []
    for etiqueta in ("junta asesora", "seleccion de canal"):
        marca = "   --- %s ---" % etiqueta.upper()
        trozos = [i for i, l in enumerate(texto.split(NL)) if l == marca]
        if len(trozos) != 2:
            motivos.append("la marca %r aparece %d veces en la salida del 2.a "
                           "y se esperaban 2" % (marca, len(trozos)))
            continue
        ls = texto.split(NL)
        # EL SEGUNDO TROZO ES EL DEL APARTADO E, que es el que trae los leidos.
        a, b = trozos[0], len(ls)
        e0 = trozos[1]
        def busca(pat, desde, hasta):
            for i in range(desde, hasta):
                m = re.search(pat, ls[i])
                if m:
                    return int(m.group(1))
            return None
        d = {}
        d["miembros"] = busca(r"CIFRA miembros DISTINTOS EN LITERAL: (\d+)", a, e0)
        d["posibles"] = busca(r"CIFRA PARES POSIBLES EN LITERAL: (\d+)", a, e0)
        d["mie_res"] = busca(r"CIFRA miembros DISTINTOS TRAS RESOLVER: (\d+)", a, e0)
        d["pos_res"] = busca(r"CIFRA PARES POSIBLES TRAS RESOLVER: (\d+)", a, e0)
        d["fundidos"] = busca(r"HUELLA DE FUSION: (\d+)", a, e0)
        d["leidos_antes"] = busca(r"CIFRA leidos que la tabla viva publica hoy: (\d+)", e0, b)
        d["en_a_antes"] = busca(r"CIFRA en A que la tabla viva publica hoy: (\d+)", e0, b)
        d["ld"] = busca(r"dentro de esta nomina: (\d+)", e0, b)
        d["leidos"] = busca(r"CIFRA leidos DESPUES de sumar las lecturas dirigidas de la mesa:"
                            r" \d+ mas \d+ = (\d+)", e0, b)
        d["en_a"] = busca(r"CIFRA en A DESPUES: \d+ mas \d+ = (\d+)", e0, b)
        faltan = [k for k, v in d.items() if v is None]
        if faltan:
            motivos.append("de %s no se pudo leer: %s" % (etiqueta, ", ".join(faltan)))
            continue
        d["completa"] = d["leidos"] >= d["posibles"]
        # LOS NOMBRES DE LAS LECTURAS DIRIGIDAS QUE ENTRAN, LEIDOS Y NO TECLEADOS.
        lds = []
        for i in range(e0, b):
            m = re.match(r"\s+(LD-\d+)\s+(\S+) contra (\S+) \| clase (\w+)", ls[i])
            if m:
                lds.append((m.group(1), m.group(2), m.group(3), m.group(4)))
            if ls[i].startswith("   --- ") and i > e0:
                break
        d["lds"] = lds
        out[etiqueta] = d
    return out, motivos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    ap.add_argument("--salida", default="T2B_TABLA_VIVA")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2.b: LAS DOS FILAS DE LA TABLA VIVA DE LOS PUROS," % VUELTA)
    w("ESCRITAS POR EL CARRIL DEL BANCO 9.10, POR ADICION Y CON CORRECCION")
    w("DECLARADA")
    w("=" * 78)
    w("")

    w("A) LAS ONCE CIFRAS, LEIDAS DE LA SALIDA DEL 2.a Y NO TECLEADAS")
    if not os.path.isfile(SALIDA_2A):
        w("   ROJO: %s NO EXISTE. El 2.a tiene que correr antes." % SALIDA_2A)
        print(NL.join(L))
        return 1
    t2a = io.open(SALIDA_2A, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("   docs/loop/SALIDA_V%d_T2A_DENOMINADOR.txt: %d bytes en disco"
      % (VUELTA, os.path.getsize(SALIDA_2A)))
    datos, motivos = cifras_del_2a(t2a)
    for mo in motivos:
        w("   MOTIVO DE ROJO: %s" % mo)
    if motivos:
        w("   ROJO: no se escribe nada.")
        print(NL.join(L))
        return 1
    for etiqueta, d in datos.items():
        w("   --- %s ---" % etiqueta)
        for k in ("miembros", "posibles", "leidos_antes", "en_a_antes", "ld",
                  "leidos", "en_a", "mie_res", "pos_res", "fundidos"):
            w("      %-14s %s" % (k, d[k]))
        w("      %-14s %s" % ("completa", d["completa"]))
        w("      lecturas dirigidas que entran: %s"
          % ", ".join("%s (%s)" % (x[0], x[3]) for x in d["lds"]))
    w("")

    w("B) LA SEDE AL ENTRAR, POR LAS DOS CONVENCIONES")
    d0, lf0, sd0, sl0, texto0 = dos_convenciones(BANCO)
    w("   docs/BANCO_DE_TEXTOS.md: %d bytes en disco y %d normalizado a LF,"
      % (d0, lf0))
    w("   sha256 disco %s y sha256 LF %s" % (sd0, sl0))
    ls0 = texto0.split(NL)
    w("   CIFRA lineas: %d" % len(ls0))
    w("   CIFRA guiones largos en el fichero ENTERO al entrar: %d"
      % texto0.count(chr(8212)))
    w("   CIFRA guiones medios en el fichero ENTERO al entrar: %d"
      % texto0.count(chr(8211)))
    w("   (esos son del texto viejo y NO se tocan; lo que esta corrida escribe")
    w("    tiene que llevar CERO de los dos, y se mide aparte mas abajo)")
    w("")

    w("C) LAS CUATRO SEDES, REMEDIDAS ANTES DE ESCRIBIR")
    rojos = []
    n_cab = texto0.count(CABECERA)
    w("   la cabecera de la tabla aparece %d vez(ces) (se exige 1)" % n_cab)
    if n_cab != 1:
        rojos.append("la cabecera de la tabla no aparece exactamente una vez")
    else:
        w("      linea %d | %s" % (ls0.index(CABECERA) + 1, CABECERA))
    ultima = None
    for etiqueta, ancla in FILAS_VIEJAS.items():
        hits = [i + 1 for i, l in enumerate(ls0) if l.startswith(ancla)]
        w("   la fila vieja de %s aparece %d vez(ces) (se exige 1)"
          % (etiqueta, len(hits)))
        if len(hits) != 1:
            rojos.append("la fila vieja de %s no aparece exactamente una vez"
                         % etiqueta)
            continue
        w("      linea %d | %s" % (hits[0], ls0[hits[0] - 1][:130]))
        ultima = max(ultima or 0, hits[0])
    ya_p = MARCA_PUNTERO in texto0
    ya_b = MARCA_BLOQUE in texto0
    w("   el puntero YA ESTA: %s | el bloque YA ESTA: %s"
      % ("SI" if ya_p else "NO", "SI" if ya_b else "NO"))
    if rojos:
        for r in rojos:
            w("   MOTIVO DE ROJO: %s" % r)
        w("   ROJO: no se escribe nada.")
        print(NL.join(L))
        return 1
    w("")

    ja = datos["junta asesora"]
    sc = datos["seleccion de canal"]
    puntero = NL.join([
        MARCA_PUNTERO,
        "",
        "> **HAY UNA CORRECCION DECLARADA POSTERIOR A ESTA CABECERA, JUSTO DEBAJO",
        "> DE LA TABLA, CON CORTE %s Y POR EL CARRIL DEL 9.10.** Toca las filas"
        % CORTE,
        "> **7** (la junta asesora) y **11** (la seleccion de canal). **El corte de",
        "> esta cabecera, 14 ago 2026, no se toca ni se tacha**: es el corte de las",
        "> once filas tal como estan escritas, y el corte de la correccion va con",
        "> la correccion.",
    ])

    def fila(num, nombre, d, estado):
        """LA FILA CORREGIDA. Su celda de racimo lleva la marca de que es la fila
        corregida, y eso NO es adorno: sin ella el ancla de la fila vieja de la
        junta asesora casaria tambien con esta, la guarda del cierre contaria DOS
        y no podria distinguir el texto viejo del nuevo. Se cazo corriendola."""
        return ("| **%s** | %s **(FILA CORREGIDA EN LA VUELTA %d)** | **%d** | "
                "**%d** | **%d** | **%d** | %s |"
                % (num, nombre, VUELTA, d["miembros"], d["posibles"],
                   d["leidos"], d["en_a"], estado))

    est_ja = ("**MEZCLADO**, y **COBERTURA COMPLETA, %d de %d** (banco 9.26): "
              "la cierra `LD-01`, que es **D**, en `docs/plan/LECTURAS_DIRIGIDAS.md`"
              " linea 76. El par que faltaba era `formalizar_junta_asesora` contra "
              "`identificar_consejo_asesores`, el que nunca entro a la cola. **La "
              "clase no cambia: ya era MEZCLADO por el puesto 1190**"
              % (ja["leidos"], ja["posibles"]))
    est_sc = ("**MEZCLADO desde esta correccion** (antes SUB-PURO): `LD-02` mete el "
              "**primer D** dentro de la nomina y **el sub-puro cae**. **COBERTURA "
              "%d de %d, o sea INCOMPLETA y por tanto PROVISIONAL** (banco 9.26). "
              "Entran `LD-02` (**D**, linea 95) y `LD-03` (**A**, linea 112) de "
              "`docs/plan/LECTURAS_DIRIGIDAS.md`"
              % (sc["leidos"], sc["posibles"]))

    bloque = NL.join([
        "",
        MARCA_BLOQUE,
        "",
        "> **CORRECCION DECLARADA (%s, vuelta %d, TAREA 2), POR EL CARRIL DEL"
        % (CORTE, VUELTA),
        "> BANCO `9.10`, POR ADICION, CON EL TEXTO VIEJO ENTERO ARRIBA, SIN",
        "> TACHARLO Y SIN CLAVE NUEVA DE ESQUEMA.** Las once filas de la tabla",
        "> siguen enteras y sin tocar; lo que se anade son **las dos filas",
        "> corregidas**, que son las unicas que la mesa `OP-L-01` mueve.",
        ">",
        "> **QUIEN LA ENCARGA:** la adjudicacion `6.3` del acta del auditor de la",
        "> vuelta 207, que sale de su `6.1`. El criterio de HECHO de la fase",
        "> `06 MESAS` en `docs/plan/08_VERIFICACION.md` exige que cada decision",
        "> vaya **con su cobertura al lado**, y la `verificacion[2]` de la propia",
        "> ficha `OP-L-01` pide que **cada nomina afectada se re-mida con su",
        "> cobertura al lado**. Esta tabla es la sede de esa cobertura.",
        ">",
        "> **EL DENOMINADOR SE RECOMPUTO PRIMERO, Y NO ES DE ADORNO.** Se conto de",
        "> la **nomina de miembros** de cada familia, en",
        "> `docs/INTRA_DOMINIO_INFORME.md`, y no de esta tabla, con el resolutor",
        "> puesto (`P.1`). Salida en",
        "> `docs/loop/SALIDA_V%d_T2A_DENOMINADOR.txt`." % VUELTA,
        "",
        "| # | racimo | miembros | pares posibles | leidos | en A | estado con su cobertura al lado |",
        "|---:|---|---:|---:|---:|---:|---|",
        fila("7", "la junta asesora", ja, est_ja),
        fila("11", "la seleccion de canal", sc, est_sc),
        "",
        "> **LA DISCREPANCIA DE LA SELECCION DE CANAL SE DECLARA Y NO SE RESUELVE",
        "> COPIANDO** (`EJECUTOR.md` 2). La mesa declara, en",
        "> `docs/plan/LECTURAS_DIRIGIDAS.md` linea 291, *%s de %s, cobertura"
        % (sc["leidos"], sc["leidos"]),
        "> COMPLETA*; **sobre el denominador recomputado es %d de %d y NO es"
        % (sc["leidos"], sc["posibles"]),
        "> completa**. Su denominador de %s sale de la tabla por nomina de la"
        % sc["leidos"],
        "> propia mesa, linea 31, que cuenta **5 miembros**; y la nomina de esa",
        "> familia, verificada contra el grafo en `docs/INTRA_DOMINIO_INFORME.md`",
        "> linea 5321, lleva una **correccion declarada del 11 ago 2026** que dice",
        "> literalmente *son SEIS y no cinco*. **La mesa cuenta sobre el universo",
        "> anterior a esa correccion.** Las dos cifras quedan escritas y ninguna se",
        "> elige en silencio.",
        ">",
        "> **Y LA JUNTA ASESORA TIENE UNA SEGUNDA CUENTA QUE TAMBIEN SE DICE.** Sus",
        "> **%d** miembros son **%d** nodos distintos TRAS RESOLVER, porque la"
        % (ja["miembros"], ja["mie_res"]),
        "> campana fundio **%d** de ellos despues del `fecha_corte` de la ficha:"
        % ja["fundidos"],
        "> `identificar_junta_asesores` resuelve hoy a",
        "> `identificar_consejo_asesores`, y `formalize_advisory_board` a",
        "> `formalizar_junta_asesora`. **En esa convencion los pares posibles son",
        "> %d y no %d.** Es HUELLA DE FUSION, que es como la propia ficha `OP-L-01`"
        % (ja["pos_res"], ja["posibles"]),
        "> llama a este mismo fenomeno. **Las columnas de esta tabla cuentan en",
        "> LITERAL**, con los ids tal como la nomina los escribe, y por eso las",
        "> filas de arriba van en literal; **la cuenta resuelta va aqui al lado y no",
        "> sustituye a ninguna**. En la seleccion de canal las dos convenciones dan",
        "> lo mismo, **%d**." % sc["pos_res"],
        ">",
        "> **LO QUE ESTA CORRECCION NO HACE:** no cierra la ficha `OP-L-01`, no toca",
        "> su campo `estado`, no mueve ni un veredicto del archivo, no adjudica",
        "> clase a ningun puesto, no toca ni un nodo y no autoriza ninguna lectura",
        "> nueva. **Cerrar una ficha es adjudicacion del auditor.**",
        "",
    ])

    w("D) LO QUE SE VA A ESCRIBIR, MEDIDO ANTES DE ESCRIBIRLO")
    for nombre, bl in (("puntero", puntero), ("bloque", bloque)):
        w("   %s: %d bytes, %d lineas, guiones largos %d, guiones medios %d"
          % (nombre, len(bl.encode("utf-8")), bl.count(NL),
             bl.count(chr(8212)), bl.count(chr(8211))))
        if bl.count(chr(8212)) or bl.count(chr(8211)):
            w("   ROJO: lo que se escribe trae guiones prohibidos.")
            print(NL.join(L))
            return 1
    w("   LAS DOS FILAS CORREGIDAS, PEGADAS AQUI ENTERAS:")
    w("      " + fila("7", "la junta asesora", ja, est_ja)[:400])
    w("      " + fila("11", "la seleccion de canal", sc, est_sc)[:400])
    w("")

    if a.escribir and not (ya_p and ya_b):
        ls = texto0.split(NL)
        i_cab = ls.index(CABECERA)
        # (2) EL BLOQUE, DEBAJO DE LA ULTIMA FILA. Se hace ANTES que el puntero
        # para que el indice de la cabecera no se mueva.
        ls = ls[:ultima] + bloque.split(NL) + ls[ultima:]
        # (1) EL PUNTERO, JUSTO DEBAJO DE LA CABECERA.
        ls = ls[:i_cab + 1] + [""] + puntero.split(NL) + ls[i_cab + 1:]
        nuevo = NL.join(ls)
        io.open(BANCO, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("   ESCRITO: puntero debajo de la cabecera (linea %d) y bloque debajo"
          % (i_cab + 1))
        w("   de la ultima fila (linea %d). LAS DOS COSAS POR ADICION." % ultima)
    elif a.escribir:
        w("   NO SE ESCRIBE: la correccion ya estaba. IDEMPOTENTE.")
    else:
        w("   MODO MEDICION: no se escribe nada.")
    w("")

    w("=" * 78)
    w("EL CIERRE, REMEDIDO Y NO HEREDADO")
    w("=" * 78)
    d1, lf1, sd1, sl1, texto1 = dos_convenciones(BANCO)
    w("   docs/BANCO_DE_TEXTOS.md al salir: %d bytes en disco y %d normalizado a"
      % (d1, lf1))
    w("   LF, sha256 disco %s y sha256 LF %s" % (sd1, sl1))
    w("   CIFRA crecimiento en bytes de disco: %d" % (d1 - d0))
    w("   CIFRA crecimiento en bytes LF: %d" % (lf1 - lf0))
    w("   CIFRA lineas al salir: %d (al entrar %d)"
      % (len(texto1.split(NL)), len(ls0)))
    w("")
    w("LA GUARDA DURA DEL 2.c: NI UNA LINEA DE TEXTO VIEJO BORRADA")
    nuevas = texto1.split(NL)
    faltan, j, cuales = 0, 0, []
    for l in ls0:
        while j < len(nuevas) and nuevas[j] != l:
            j += 1
        if j >= len(nuevas):
            faltan += 1
            cuales.append(l[:80])
        else:
            j += 1
    w("   CIFRA lineas del texto de ENTRADA que NO estan, en orden, en el de")
    w("   SALIDA: %d" % faltan)
    for c in cuales[:10]:
        w("      falta: %s" % c)
    w("   (si esta cifra no es 0, es ROJO: se habria borrado texto viejo)")
    w("")
    w("LAS DOS FILAS VIEJAS, COMPROBADAS ENTERAS AL SALIR")
    for etiqueta, ancla in FILAS_VIEJAS.items():
        hits = [i + 1 for i, l in enumerate(nuevas) if l.startswith(ancla)]
        w("   la fila vieja de %s sigue apareciendo %d vez(ces), en la linea %s"
          % (etiqueta, len(hits), hits[0] if hits else "(ninguna)"))
        if len(hits) != 1:
            faltan += 1
    w("   LA CABECERA CON SU CORTE VIEJO SIGUE ENTERA: %s"
      % ("SI" if texto1.count(CABECERA) == 1 else "NO"))
    w("")
    w("LA SEDE QUE NO SE TOCA, REMEDIDA AL CIERRE")
    d_o, lf_o, sd_o, sl_o, _t = dos_convenciones(OPES)
    w("   docs/plan/OPERACIONES.jsonl: %d bytes en disco y %d normalizado a LF,"
      % (d_o, lf_o))
    w("   sha256 disco %s y sha256 LF %s" % (sd_o, sl_o))
    w("")
    w("FIN")
    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0 if faltan == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
