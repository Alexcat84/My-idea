# -*- coding: utf-8 -*-
r"""_v213_t2_cierre_fase_iii.py . LA TAREA 2 DE LA VUELTA 213: EL INVENTARIO DE
CIERRE DE LA FASE III, DE LAS 71 FICHAS, LEIDO DEL REPO Y NO DEL CAMPO `estado`.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). Muere con la vuelta.

LA FUENTE ES LA VARA, NUNCA EL CAMPO (recuadro 0 de AUDITOR.md). Esta tarea NO
reimplementa la vara: IMPORTA `vuelta150_3_relectura_expediente.py` y llama a sus
propias funciones con el MISMO `--corte` con el que la vara se corrio en esta
vuelta. IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5).

POR QUE HAY QUE IMPORTARLA EN VEZ DE LEER SU SALIDA: la vara imprime SOLO las
filas que NO CALZAN (40 de 71) y dice expresamente que las que calzan no se
imprimen. El encargo pide UNA FILA POR FICHA, LAS 71 Y SIN CORTAR, y esas 31
filas no existen en ningun fichero de salida. Se computan con la vara misma.

Y LA GUARDA QUE LO SOSTIENE: para las 40 filas que la vara SI imprime, este
instrumento COTEJA su celda de pruebas contra la que el fichero sellado publica,
fila a fila, y cae en ROJO si una sola difiere. Si mi computo se desviara de la
vara, la guarda lo dice.

ESTA TAREA MIDE Y NO ESCRIBE EN EL PLAN: publica el `sha256` de
`docs/plan/OPERACIONES.jsonl` al entrar y al salir para probarlo.

USO:  python scripts/loop/_v213_t2_cierre_fase_iii.py --corte <REF>
"""
import hashlib
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))

import vuelta150_3_relectura_expediente as V  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
OPS = "docs/plan/OPERACIONES.jsonl"
INV = "docs/plan/INVENTARIO.jsonl"
SALIDA_VARA = "docs/loop/SALIDA_V%d_T2_VARA.txt" % VUELTA
DESTINO = os.path.join(RAIZ, "docs", "loop",
                       "SALIDA_V%d_T2_CIERRE_FASE_III.txt" % VUELTA)

OUT = []
ROJOS = []


def w(s=""):
    OUT.append(s)


def sha(ruta):
    b = io.open(os.path.join(RAIZ, ruta.replace("/", os.sep)), "rb").read()
    return (hashlib.sha256(b).hexdigest()[:16],
            hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16],
            len(b))


def celdas_de_la_vara(texto):
    """LAS FILAS DE LA TABLA QUE LA VARA SI IMPRIME, leidas de su salida sellada.
    PURA: recibe el texto y devuelve {id_op: (estado, pruebas)}.

    SE ACOTA A LA TABLA DE LAS QUE NO CALZAN Y NO AL FICHERO ENTERO: la salida
    de la vara trae DOS tablas mas cuyas filas tambien empiezan por `| \x60OP-`
    (la de las desbloqueadas de la TAREA 3.c y la de la vara documental), y
    leerlas todas metia tres filas ajenas con las columnas cambiadas de sitio.
    Lo cazo la propia guarda en su primera corrida."""
    ini = texto.find("TABLA DE LAS QUE NO CALZAN")
    fin = texto.find("DESGLOSE, con la evidencia", ini if ini >= 0 else 0)
    if ini < 0 or fin < 0:
        return {}
    texto = texto[ini:fin]
    out = {}
    for l in texto.split(NL):
        l = l.strip()
        if not l.startswith("| `OP-"):
            continue
        c = [x.strip().strip("`") for x in l.strip("|").split("|")]
        if len(c) < 5:
            continue
        out[c[0]] = (c[2], c[3])
    return out


def main():
    corte = sys.argv[sys.argv.index("--corte") + 1] if "--corte" in sys.argv else None
    if not corte:
        print("ROJO: --corte es obligatorio, igual que en la vara.")
        return 1

    sd0, sl0, by0 = sha(OPS)
    w("=" * 78)
    w("VUELTA %d, TAREA 2. INVENTARIO DE CIERRE DE LA FASE III, DE LAS 71 FICHAS"
      % VUELTA)
    w("LEIDO DEL REPO Y NO DEL CAMPO estado (recuadro 0 de AUDITOR.md)")
    w("=" * 78)
    w("")
    w("CIFRA sede %s AL ENTRAR: %d bytes, sha256 disco %s, sha256 LF %s"
      % (OPS, by0, sd0, sl0))
    w("CIFRA corte con el que corre la vara EN ESTA VUELTA: %s" % corte)
    w("")

    F = V.fichas()
    ids = [f["id_op"] for f in F]
    w("CIFRA fichas contadas de %s: %d" % (OPS, len(F)))
    w("CIFRA id_op distintos: %d" % len(set(ids)))
    if len(set(ids)) != len(ids):
        ROJOS.append("hay id_op duplicados")
    w("")

    w("LAS CUATRO VARAS, INVOCADAS DE SU PROPIO INSTRUMENTO Y NO REESCRITAS AQUI")
    v1 = V.p1_vara_de_grafo()
    v2 = V.p2_vara_de_codigo(ids)
    v3 = V.p3_huella_en_git(ids, corte)
    v3b = V.p3b_caso_positivo(F, corte)
    v4 = V.p4_vara_documental(F)
    mapa = V.mapa_de_alias()
    vivos = V.vivos_del_grafo()
    w("   CIFRA P1 con DESTINO CUMPLIDO: %d" % sum(1 for k in v1 if v1[k][0]))
    w("   CIFRA P2 con el id_op en codigo vivo: %d" % sum(1 for i in ids if v2[i]))
    w("   CIFRA P3a con huella en git: %d" % sum(1 for i in ids if v3[i][1]))
    w("   CIFRA P3b con caso positivo citado y presente: %d"
      % sum(1 for i in ids if v3b.get(i)))
    w("   CIFRA fichas de tipo MESA con vara documental computable: %d" % len(v4))
    w("   CIFRA de esas con al menos un documento hallado: %d"
      % sum(1 for k in v4 if v4[k]))
    w("")

    filas = []
    for f in F:
        i = f["id_op"]
        pruebas = []
        if v1.get(i, (False,))[0]:
            pruebas.append("P1")
        if v2[i]:
            pruebas.append("P2")
        if v3[i][1]:
            pruebas.append("P3a")
        if v3b.get(i):
            pruebas.append("P3b")
        ejecutada = bool(pruebas)
        doc = bool(v4.get(i))
        pruebas_pub = list(pruebas)
        if doc:
            pruebas_pub.append("documental")
        consumida, nombrados, destino = V.consumida_por(f, mapa, vivos)
        if ejecutada:
            veredicto = "EJECUTADA"
        elif consumida:
            veredicto = ("CONSUMIDA por %s" % ", ".join(nombrados)) if nombrados \
                else "CONSUMIDA (sin quien nombrado en la ficha)"
        else:
            veredicto = "SIN EJECUTAR"
        estado = f["estado"]
        calza = "SI" if ((estado == "HECHA" and ejecutada)
                         or (estado == "LISTA" and not ejecutada)) else "NO"
        filas.append({
            "id": i, "fase": f["fase"], "tipo": f.get("tipo") or "(sin tipo)",
            "estado": estado, "pruebas": "+".join(pruebas) or "ninguna",
            "pruebas_pub": "+".join(pruebas_pub) or "ninguna",
            "veredicto": veredicto, "calza": calza,
            "ejecutada": ejecutada, "consumida": consumida,
            "nombrados": nombrados,
        })

    w("=" * 78)
    w("LA GUARDA: MI CELDA DE PRUEBAS CONTRA LA QUE LA VARA PUBLICA EN SU SALIDA")
    w("=" * 78)
    texto_vara = io.open(os.path.join(RAIZ, SALIDA_VARA.replace("/", os.sep)),
                         encoding="utf-8").read()
    de_la_vara = celdas_de_la_vara(texto_vara)
    w("CIFRA filas que la vara IMPRIME en su tabla (%s): %d"
      % (SALIDA_VARA, len(de_la_vara)))
    mias = {f["id"]: f for f in filas}
    difieren = []
    for i, (est, pr) in sorted(de_la_vara.items()):
        m = mias.get(i)
        if m is None:
            difieren.append("%s: la vara la imprime y yo no la tengo" % i)
            continue
        if m["estado"] != est or m["pruebas"] != pr:
            difieren.append("%s: vara dice (%s, %s) y yo digo (%s, %s)"
                            % (i, est, pr, m["estado"], m["pruebas"]))
    w("CIFRA filas cotejadas: %d | CIFRA que DIFIEREN: %d (se exigen 0)"
      % (len(de_la_vara), len(difieren)))
    for d in difieren:
        w("   DIFIERE> " + d)
        ROJOS.append(d)
    w("")

    w("=" * 78)
    w("LA TABLA, UNA FILA POR FICHA, LAS 71 Y SIN CORTAR")
    w("=" * 78)
    w("La columna `estado` es HISTORICA y se publica como CONTRASTE, nunca como")
    w("fuente: el recuadro 0 de AUDITOR.md lo dice y esta tarea lo obedece.")
    w("")
    w("| id_op | fase | tipo | estado HISTORICO (contraste) | pruebas que dan "
      "positivo, de la vara de esta vuelta | veredicto del repo | calza el campo "
      "con el repo |")
    w("|---|---|---|---|---|---|---|")
    for f in filas:
        w("| `%s` | %s | %s | %s | %s | %s | %s |"
          % (f["id"], f["fase"], f["tipo"], f["estado"], f["pruebas_pub"],
             f["veredicto"], f["calza"]))
    w("")
    w("CIFRA filas de la tabla: %d | CIFRA fichas que deberia haber: %d"
      % (len(filas), len(F)))
    if len(filas) != len(F):
        ROJOS.append("la tabla no tiene una fila por ficha")
    w("")

    w("=" * 78)
    w("LAS CUATRO CIFRAS QUE CIERRAN LA SECCION, CADA UNA CONTADA DE LA TABLA")
    w("=" * 78)
    con_prueba = [f for f in filas if f["ejecutada"]]
    consumidas = [f for f in filas if not f["ejecutada"] and f["consumida"]]
    sin_ejecutar = [f for f in filas if f["veredicto"] == "SIN EJECUTAR"]
    hecha_sin = [f for f in filas if f["estado"] == "HECHA" and not f["ejecutada"]]
    lista_con = [f for f in filas if f["estado"] == "LISTA" and f["ejecutada"]]
    w("")
    w("1. CIFRA de las %d que tienen PRUEBA DE EJECUCION en el repo: %d"
      % (len(filas), len(con_prueba)))
    w("2. CIFRA CONSUMIDAS (sin prueba propia, con sus nodos resueltos a un vivo "
      "unico): %d" % len(consumidas))
    for f in consumidas:
        w("      CONSUMIDA: %-22s por %s" % (f["id"], ", ".join(f["nombrados"]) or "(sin nombrar)"))
    w("3. CIFRA SIN EJECUTAR: %d, y va su lista entera" % len(sin_ejecutar))
    for f in sin_ejecutar:
        w("      SIN EJECUTAR: %-22s fase %s, tipo %s, estado historico %s"
          % (f["id"], f["fase"], f["tipo"], f["estado"]))
    w("4. CIFRA con el campo estado EN DESACUERDO con el repo: %d, y van las dos "
      "direcciones con sus dos listas enteras" % (len(hecha_sin) + len(lista_con)))
    w("   4.a HECHA SIN PRUEBA (el campo afirma mas que el repo): %d" % len(hecha_sin))
    for f in hecha_sin:
        w("      HECHA sin prueba: %-22s fase %s" % (f["id"], f["fase"]))
    w("   4.b LISTA CON PRUEBA (el repo dice mas que el campo): %d" % len(lista_con))
    for f in lista_con:
        w("      LISTA con prueba: %-22s pruebas %s" % (f["id"], f["pruebas"]))
    w("")
    w("   LA CAUTELA DE LA CIFRA 4, PEGADA A ELLA Y NO SUELTA (adjudicacion 6.8")
    w("   del acta 211): si cada ficha va poniendo su campo al dia, la vara del")
    w("   desacuerdo tiende a cero SIN QUE SE HAYA EJECUTADO NADA MAS. La cifra")
    w("   mide cuanto miente el campo, no cuanto trabajo queda. El trabajo que")
    w("   queda es la cifra 3.")
    w("")
    suma = len(con_prueba) + len(consumidas) + len(sin_ejecutar)
    w("   LA SUMA SE COMPRUEBA: %d con prueba + %d consumidas + %d sin ejecutar "
      "= %d, y las fichas son %d" % (len(con_prueba), len(consumidas),
                                     len(sin_ejecutar), suma, len(filas)))
    if suma != len(filas):
        ROJOS.append("los tres veredictos no suman las fichas")
    w("")

    # ------------------------------------------------------------------ 2.b
    w("=" * 78)
    w("2.b LA UNICA QUE QUEDA ABIERTA: OP-I-01")
    w("=" * 78)
    ficha = [f for f in F if f["id_op"] == "OP-I-01"][0]
    puntos = ficha["verificacion"]
    w("CIFRA puntos de `verificacion` de OP-I-01, contados de la ficha: %d"
      % len(puntos))
    w("")
    w("LO QUE LA FICHA SI ESCRIBE Y LO QUE NO, DICHO ANTES DE LA TABLA: la ficha")
    w("escribe LOS PUNTOS y NO escribe su estado. CUBRE, A MEDIAS y NO CUBRE son")
    w("veredictos MEDIDOS, no campos: salen de docs/loop/SALIDA_V211_T2_OP_I_01.txt")
    w("y los ratifico el acta 211 en su 6.3 (linea 74595). No los invento aqui y no")
    w("los atribuyo a la ficha.")
    w("")
    ESTADOS = {}
    tv = io.open(os.path.join(RAIZ, "docs", "loop", "SALIDA_V211_T2_OP_I_01.txt"),
                 encoding="utf-8").read().split(NL)
    actual = None
    for l in tv:
        m = re.match(r"^\s*PUNTO (\d)\.", l)
        if m:
            actual = int(m.group(1))
        m2 = re.match(r"^\s*VEREDICTO: \*\*(.+?)\*\*", l)
        if m2 and actual:
            ESTADOS[actual] = m2.group(1)
    w("CIFRA veredictos leidos de SALIDA_V211_T2_OP_I_01.txt: %d (se esperan %d)"
      % (len(ESTADOS), len(puntos)))
    if len(ESTADOS) != len(puntos):
        ROJOS.append("no se leyeron los cuatro veredictos del fichero de la 211")
    w("")
    for n, p in enumerate(puntos, 1):
        w("   PUNTO %d, PEGADO ENTERO DE LA FICHA:" % n)
        w("      %s" % p)
        w("      ESTADO MEDIDO: %s" % ESTADOS.get(n, "(ROJO: no leido)"))
        w("")

    w("EL PUNTO QUE ESTA EN NO CUBRE, APARTE Y ENTERO:")
    nc = [n for n in ESTADOS if ESTADOS[n] == "NO CUBRE"]
    w("   CIFRA puntos en NO CUBRE: %d" % len(nc))
    for n in nc:
        w("   PUNTO %d: %s" % (n, puntos[n - 1]))
    w("")
    w("QUE HARIA FALTA EXACTAMENTE PARA QUE DEJARA DE ESTARLO, CITANDO LA")
    w("ADJUDICACION 6.4 DEL ACTA 211 CON SU LINEA:")
    acta = io.open(os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md"),
                   encoding="utf-8").read().split(NL)
    for n in (74601, 74606, 74607):
        w("   linea %d de docs/loop/ACTA_AUDITOR.md, leida hoy:" % n)
        w("      %s" % acta[n - 1].strip())
    w("")
    w("   EN UNA FRASE, Y SALE DE ESAS LINEAS: haria falta que las entradas con")
    w("   cobertura incompleta LO DIGAN, o sea que lleven escrita la palabra")
    w("   PROVISIONAL (o su equivalente declarado) en algun campo. El banco 9.26")
    w("   admite una cobertura incompleta como cumplimiento SI SE DICE ASI, y hoy")
    w("   ninguna lo dice. No hace falta completar la cobertura: hace falta")
    w("   MARCARLA.")
    w("")

    w("EL RECUENTO DE LAS ENTRADAS DEL INVENTARIO CON COBERTURA INCOMPLETA,")
    w("HECHO POR MI EN ESTA VUELTA Y NO COPIADO:")
    E = [json.loads(l) for l in
         io.open(os.path.join(RAIZ, INV.replace("/", os.sep)),
                 encoding="utf-8").read().split(NL) if l.strip()]
    pat = re.compile(r"^(\d+) de (\d+) pares leidos")
    con_forma = 0
    incompletas = []
    for d in E:
        m = pat.match(str(d.get("cobertura") or ""))
        if m:
            con_forma += 1
            if int(m.group(1)) < int(m.group(2)):
                incompletas.append(d)
    marcadas = [d for d in incompletas
                if "PROVISIONAL" in json.dumps(d, ensure_ascii=False).upper()]
    con_prov = [d for d in E if "PROVISIONAL" in json.dumps(d, ensure_ascii=False).upper()]
    w("   EL COMANDO QUE LA CUENTA, escrito para que se pueda repetir a mano:")
    w("      python -c \"import io,json,re;E=[json.loads(l) for l in "
      "io.open('docs/plan/INVENTARIO.jsonl',encoding='utf-8') if l.strip()];"
      "p=re.compile(r'^(\\d+) de (\\d+) pares leidos');"
      "m=[p.match(str(d.get('cobertura') or '')) for d in E];"
      "print(sum(1 for x in m if x), sum(1 for x in m if x and int(x.group(1))"
      "<int(x.group(2))))\"")
    w("   CIFRA entradas del inventario: %d" % len(E))
    w("   CIFRA entradas con cobertura de la forma 'N de M pares leidos': %d" % con_forma)
    w("   CIFRA de esas que estan INCOMPLETAS (N menor que M): %d" % len(incompletas))
    w("   CIFRA de esas incompletas que llevan PROVISIONAL en algun campo: %d"
      % len(marcadas))
    w("   CIFRA entradas del inventario entero que llevan PROVISIONAL: %d" % len(con_prov))
    w("   CONTRASTE CON LA CIFRA VIEJA: el acta 211 publica 95 en su 6.4 (linea")
    w("   74606). Mi conteo de hoy da %d, o sea que %s."
      % (len(incompletas),
         "REPRODUCE al digito" if len(incompletas) == 95
         else "NO REPRODUCE, y lo digo en vez de copiar la vieja"))
    w("")
    w("LO QUE DECIDE EL FUNDADOR Y LO QUE NO, EN UNA LINEA: marcar esas %d entradas"
      % len(incompletas))
    w("es EDICION DE DATOS de docs/plan que ninguna regla ordena hoy, y las filas que")
    w("faltan en docs/plan/08_VERIFICACION.md para las fases 09 y 10 CAMBIAN LA FORMA")
    w("DEL PLAN: las dos son suyas y ninguna es del bucle.")
    w("")

    sd1, sl1, by1 = sha(OPS)
    w("=" * 78)
    w("LA PROHIBICION 1, PROBADA CON EL sha256 Y NO PROMETIDA")
    w("=" * 78)
    w("CIFRA sede %s AL SALIR: %d bytes, sha256 disco %s, sha256 LF %s"
      % (OPS, by1, sd1, sl1))
    w("CIFRA el sha256 LF de %s es el mismo al entrar y al salir: %s"
      % (OPS, "SI, QUIETO como se exige" if sl0 == sl1 else "NO, ROJO"))
    if sl0 != sl1:
        ROJOS.append("OPERACIONES.jsonl se movio")
    w("")
    w("CIFRA rojos de esta tarea: %d" % len(ROJOS))
    for r in ROJOS:
        w("   ROJO> %s" % r)
    w("VEREDICTO: %s" % ("VERDE" if not ROJOS else "ROJO"))

    texto = NL.join(OUT) + NL
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    return 1 if ROJOS else 0


if __name__ == "__main__":
    sys.exit(main())
