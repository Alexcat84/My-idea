# -*- coding: utf-8 -*-
r"""_v212_t1c_op_f_04_hor.py . LA `P.2`: LA CORRECCION DECLARADA DEL CAMPO
`adjudicacion` DE `OP-F-04-HOR`. VUELTA 212.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo y fuera de la
nomina (congelada en 135). Moratoria de AUDITOR.md 6.3.

QUE CORRIGE: el campo `nodos` mide 14 y la propia `adjudicacion` dice *LEIDOS
LOS 13*. Es la especie que el acta 209 resolvio con los dos `estado`: un campo
que contradice a su vecino engana a quien venga. El carril es el banco `9.10` y
la regla 8 de `EJECUTOR.md`, y el motivo vive en `docs/plan/01_FUENTES.md`
lineas 1168 y 1453, QUE ESTE FICHERO LEE DEL DISCO Y NO RECUERDA.

LO QUE NO SE TOCA, Y LA GUARDA LO EXIGE: el campo `nodos` y el campo `estado`.

LAS TRES GUARDAS SON LAS DE LA `1.b` DE LA 211: sede por las dos convenciones al
entrar y al salir, cuentas por `estado` antes y despues mas `git diff --numstat`
sobre `docs/plan/`, y la recarga del `jsonl` linea a linea. Y EL ROJO PROBADO
POR MUTACION, CORRIDO ANTES DE ESCRIBIR NADA.
"""
import io
import json
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))

from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402
from _v211_apertura import shas, git                    # noqa: E402

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
ARCHIVO = "docs/plan/OPERACIONES.jsonl"
RUTA = os.path.join(RAIZ, ARCHIVO.replace("/", os.sep))
FUENTES = "docs/plan/01_FUENTES.md"
FICHA = "OP-F-04-HOR"
LINEAS_DEL_MOTIVO = [1168, 1453]

OUT = []


def di(s=""):
    OUT.append(s)


def sede(ruta, cuando):
    m = medir_en_disco(RAIZ, ruta)
    sd, sl = shas(ruta)
    igual = "COINCIDEN" if m[0] == m[1] else "NO COINCIDEN"
    di("CIFRA sede %s %s: %d bytes en disco y %d normalizado a LF (%s), "
       "sha256 disco %s y sha256 LF %s" % (ruta, cuando, m[0], m[1], igual, sd, sl))
    return sd, sl


def cuentas_por_estado(filas):
    c = {}
    for f in filas:
        c[f.get("estado")] = c.get(f.get("estado"), 0) + 1
    return c


def numstat(sede_git):
    _, ns = git(["diff", "--numstat", "--", sede_git])
    return [l for l in ns.split(NL) if l.strip()]


def juzgar(viejas, nuevas, exigir_texto_viejo=True):
    """LA GUARDA. PURA: recibe las dos listas de lineas y devuelve (fallos, informe)."""
    inf = []
    fallos = 0
    v = [l for l in viejas if l.strip()]
    n = [l for l in nuevas if l.strip()]
    inf.append("   filas antes %d, filas despues %d (se exige que sean iguales)"
               % (len(v), len(n)))
    if len(v) != len(n):
        fallos += 1
    distintas = [i for i in range(min(len(v), len(n))) if v[i] != n[i]]
    inf.append("   lineas distintas: %d (se exige 1)" % len(distintas))
    if len(distintas) != 1:
        return fallos + 1, inf
    i = distintas[0]
    a = json.loads(v[i])
    b = json.loads(n[i])
    inf.append("   la linea distinta es la ficha %r (se exige %r)"
               % (b.get("id_op"), FICHA))
    if b.get("id_op") != FICHA or a.get("id_op") != FICHA:
        fallos += 1
    cambiados = sorted(k for k in set(list(a) + list(b)) if a.get(k) != b.get(k))
    inf.append("   campos que cambian: %s (se exige exactamente adjudicacion)"
               % (", ".join(cambiados) or "ninguno"))
    if cambiados != ["adjudicacion"]:
        fallos += 1
    inf.append("   el campo nodos NO se movio: %s (mide %d antes y %d despues)"
               % ("SI" if a.get("nodos") == b.get("nodos") else "NO",
                  len(a.get("nodos") or []), len(b.get("nodos") or [])))
    if a.get("nodos") != b.get("nodos"):
        fallos += 1
    inf.append("   el campo estado NO se movio: %s (%r antes y %r despues)"
               % ("SI" if a.get("estado") == b.get("estado") else "NO",
                  a.get("estado"), b.get("estado")))
    if a.get("estado") != b.get("estado"):
        fallos += 1
    entero = (b.get("adjudicacion") or "").startswith(a.get("adjudicacion") or "")
    inf.append("   el texto viejo esta ENTERO Y ENCIMA (la adjudicacion nueva empieza "
               "por la vieja, byte a byte): %s" % ("SI" if entero else "NO"))
    if exigir_texto_viejo and not entero:
        fallos += 1
    largos = (b.get("adjudicacion") or "").count(chr(8212))
    medios = (b.get("adjudicacion") or "").count(chr(8211))
    inf.append("   guiones largos %d, guiones medios %d (se exige 0 y 0)"
               % (largos, medios))
    if largos or medios:
        fallos += 1
    return fallos, inf


def main():
    di("=" * 78)
    di("TAREA 1.c DE LA VUELTA %d. LA `P.2`: LA ADJUDICACION DE %s." % (VUELTA, FICHA))
    di("=" * 78)
    di("")

    di("## 0. EL MOTIVO, LEIDO DEL DISCO Y NO RECORDADO")
    lineas_f = io.open(os.path.join(RAIZ, FUENTES.replace("/", os.sep)),
                       encoding="utf-8").read().split(NL)
    di("CIFRA lineas de %s: %d" % (FUENTES, len(lineas_f)))
    di("LA TABLA DE LAS LINEAS DEL MOTIVO: %d fila(s) armada(s) sobre %d lineas "
       "que el encargo nombra" % (len(LINEAS_DEL_MOTIVO), len(LINEAS_DEL_MOTIVO)))
    citas = {}
    for n in LINEAS_DEL_MOTIVO:
        citas[n] = lineas_f[n - 1]
        di("   motivo> %s linea %d :: %s" % (FUENTES, n, lineas_f[n - 1]))
    di("")

    di("## 1. LA ENTRADA")
    raw = io.open(RUTA, encoding="utf-8", newline="").read()
    lineas = raw.split(NL)
    filas = [json.loads(l) for l in lineas if l.strip()]
    di("CIFRA fichas de %s AL ENTRAR: %d" % (ARCHIVO, len(filas)))
    sd0, _ = sede(ARCHIVO, "AL ENTRAR")
    c0 = cuentas_por_estado(filas)
    di("LA TABLA DE CUENTAS POR estado AL ENTRAR: %d fila(s) armada(s), y suman %d, "
       "que es el total de fichas" % (len(c0), sum(c0.values())))
    for k in sorted(c0, key=lambda x: (x is None, x)):
        di("   estado> %-8s %d" % (k, c0[k]))
    ns0 = numstat("docs/plan/")
    di("CIFRA filas de git diff --numstat -- docs/plan/ AL ENTRAR: %d" % len(ns0))
    di("")

    idx = [i for i, l in enumerate(lineas)
           if l.strip() and json.loads(l).get("id_op") == FICHA]
    di("CIFRA lineas con la ficha %s: %d (se exige 1) -> %s" % (FICHA, len(idx), idx))
    if len(idx) != 1:
        di("ROJO: la ficha no es unica.")
        return 1
    i = idx[0]
    ficha = json.loads(lineas[i])
    di("CIFRA round-trip de json.dumps sobre la ficha vieja identico a su linea: %s"
       % ("SI" if json.dumps(ficha, ensure_ascii=False) == lineas[i] else "NO"))
    if json.dumps(ficha, ensure_ascii=False) != lineas[i]:
        di("ROJO: la serializacion de la casa no reproduce la linea. No se escribe.")
        return 1
    nodos = ficha.get("nodos") or []
    di("CIFRA el campo nodos de %s mide: %d (contado del campo, no tecleado)"
       % (FICHA, len(nodos)))
    di("CIFRA el campo estado de %s AL ENTRAR: %r" % (FICHA, ficha.get("estado")))
    di("CIFRA bytes de la adjudicacion AL ENTRAR: %d"
       % len((ficha.get("adjudicacion") or "").encode("utf-8")))
    di("   adjudicacion vieja> %s" % ficha.get("adjudicacion"))
    dice_13 = "LEIDOS LOS 13" in (ficha.get("adjudicacion") or "")
    di("CIFRA la adjudicacion contiene la frase LEIDOS LOS 13: %s"
       % ("SI" if dice_13 else "NO"))
    if not dice_13:
        di("ROJO: la contradiccion que este fichero viene a declarar no esta ahi. "
           "No se escribe.")
        return 1
    nombrado = [x for x in nodos if x in citas[1168] or x in citas[1453]]
    di("LA TABLA DE NODOS DEL CAMPO QUE LAS DOS LINEAS DEL MOTIVO NOMBRAN: %d "
       "fila(s) armada(s) sobre los %d del campo" % (len(nombrado), len(nodos)))
    for x in nombrado:
        di("   nombrado> %s (posicion %d de %d en el campo nodos)"
           % (x, nodos.index(x) + 1, len(nodos)))
    di("")

    correccion = (
        " CORRECCION DECLARADA, vuelta 212 (8 sep 2026), por el carril del banco "
        "9.10 y la regla 8 de EJECUTOR.md: EL TEXTO VIEJO QUEDA ENTERO ENCIMA Y SIN "
        "TACHAR, porque una correccion que tapa lo que corrige no se puede auditar. "
        "ESTA ADJUDICACION DICE LEIDOS LOS 13 Y EL CAMPO nodos DE ESTA MISMA FICHA "
        "MIDE %d, contado hoy sobre el propio campo. Los dos son ciertos en su fecha "
        "y por eso ninguno se borra: el 13 es la nomina del 11 ago 2026, que es la "
        "fecha_corte de esta ficha, y el %d es la nomina de hoy. LO QUE CAMBIO NO FUE "
        "LA LECTURA SINO LA NOMINA. EL MOTIVO VIVE EN docs/plan/01_FUENTES.md y sus "
        "dos lineas se leyeron hoy del disco: la linea 1168 dice 'devolvio "
        "principio_calidad_mvp a la operacion y la nomina volvio a CATORCE', por la "
        "decision del fundador del 15 ago 2026 archivada en "
        "docs/loop/paradas/2026-08-15-el-14vo-de-horowitz.md, al quedar rota la "
        "premisa de la exclusion de la vuelta 21; y la linea 1453 dice 'El que sobra "
        "es principio_calidad_mvp', que es esa exclusion vieja, la que aquella "
        "decision revirtio. EL 14.o ES principio_calidad_mvp, y esta hoy en la "
        "posicion %d de %d del campo nodos, leida por el instrumento. NO SE TOCA EL "
        "CAMPO nodos NI EL CAMPO estado: esta correccion es solo sobre la prosa que "
        "contradice a su vecina, que es lo que engana a quien venga. La medicion "
        "entera, con su caso rojo por mutacion corrido antes de escribir, en "
        "docs/loop/SALIDA_V212_T1C_OP_F_04_HOR.txt."
        % (len(nodos), len(nodos),
           nodos.index("principio_calidad_mvp") + 1 if "principio_calidad_mvp" in nodos else 0,
           len(nodos)))

    di("## 2. LA SIMULACION SOBRE COPIA EN MEMORIA, ANTES DE TOCAR EL DISCO")
    nueva = dict(ficha)
    nueva["adjudicacion"] = ficha["adjudicacion"] + correccion
    lineas_sim = list(lineas)
    lineas_sim[i] = json.dumps(nueva, ensure_ascii=False)
    di("CIFRA bytes de la adjudicacion vieja %d, de la nueva %d, de lo anadido %d"
       % (len(ficha["adjudicacion"].encode("utf-8")),
          len(nueva["adjudicacion"].encode("utf-8")),
          len(correccion.encode("utf-8"))))
    fallos, inf = juzgar(lineas, lineas_sim)
    for l in inf:
        di(l)
    di("CIFRA fallos de la simulacion: %d (se exige 0)" % fallos)
    c_sim = cuentas_por_estado([json.loads(l) for l in lineas_sim if l.strip()])
    di("CIFRA las cuentas por estado NO se mueven en la simulacion: %s"
       % ("SI" if c_sim == c0 else "NO"))
    di("")

    di("## 3. EL CASO ROJO POR MUTACION, CORRIDO ANTES DE ESCRIBIR NADA")
    rojos = []

    m1 = list(lineas)
    f1 = dict(ficha)
    f1["adjudicacion"] = correccion.strip()
    m1[i] = json.dumps(f1, ensure_ascii=False)
    n1, i1 = juzgar(lineas, m1)
    di("MUTANTE 1, la correccion TAPA el texto viejo: fallos %d (se exige >0)" % n1)
    for l in i1:
        di("  " + l)
    rojos.append(n1 > 0)
    di("")

    m2 = list(lineas)
    f2 = dict(ficha)
    f2["adjudicacion"] = ficha["adjudicacion"] + correccion
    f2["nodos"] = list(nodos)[:-1]
    m2[i] = json.dumps(f2, ensure_ascii=False)
    n2, i2 = juzgar(lineas, m2)
    di("MUTANTE 2, se toca ademas el campo nodos (se le quita el 14.o): fallos %d "
       "(se exige >0)" % n2)
    for l in i2:
        di("  " + l)
    rojos.append(n2 > 0)
    di("")

    m3 = list(lineas)
    f3 = dict(ficha)
    f3["adjudicacion"] = ficha["adjudicacion"] + correccion
    f3["estado"] = "HECHA"
    m3[i] = json.dumps(f3, ensure_ascii=False)
    n3, i3 = juzgar(lineas, m3)
    di("MUTANTE 3, se toca ademas el campo estado (la prohibicion expresa del "
       "encargo): fallos %d (se exige >0)" % n3)
    for l in i3:
        di("  " + l)
    rojos.append(n3 > 0)
    di("")

    m4 = list(lineas_sim)
    otra = [k for k, l in enumerate(lineas)
            if l.strip() and json.loads(l).get("id_op") == "OP-F-01"][0]
    f4 = json.loads(m4[otra])
    f4["nota"] = (f4.get("nota") or "") + " (toque de mentira del mutante 4)"
    m4[otra] = json.dumps(f4, ensure_ascii=False)
    n4, i4 = juzgar(lineas, m4)
    di("MUTANTE 4, se toca ademas otra ficha (OP-F-01): fallos %d (se exige >0)" % n4)
    for l in i4:
        di("  " + l)
    rojos.append(n4 > 0)
    di("")

    di("CIFRA mutantes corridos: %d. CIFRA mutantes que CAEN en rojo: %d "
       "(se exige que caigan todos)" % (len(rojos), len([x for x in rojos if x])))
    di("EL CASO ROJO %s"
       % ("SE COMPORTA: la guarda dice VERDE sobre lo correcto y ROJO sobre las "
          "cuatro escrituras equivocadas." if all(rojos) else
          "NO SE COMPORTA, Y ESO INVALIDA LA GUARDA. NO SE ESCRIBE."))
    di("")
    if fallos or not all(rojos):
        di("ROJO: NO SE ESCRIBE NADA. El fichero del disco queda intacto.")
        return 1

    di("## 4. LA ESCRITURA")
    texto_nuevo = NL.join(lineas_sim)
    io.open(RUTA, "w", encoding="utf-8", newline="").write(texto_nuevo)
    di("ESCRITO %s" % ARCHIVO)
    di("")

    di("## 5. LA SALIDA, CON LA RECARGA DEL jsonl LINEA A LINEA")
    raw2 = io.open(RUTA, encoding="utf-8", newline="").read()
    lineas2 = raw2.split(NL)
    malas = []
    filas2 = []
    for k, l in enumerate(lineas2, 1):
        if not l.strip():
            continue
        try:
            filas2.append(json.loads(l))
        except Exception as e:                       # noqa: BLE001
            malas.append((k, str(e)[:80]))
    di("CIFRA lineas del fichero recargadas una a una: %d; lineas que NO parsean: %d "
       "(se exige 0)" % (len(filas2), len(malas)))
    for k, e in malas:
        di("   mala> linea %d :: %s" % (k, e))
    di("CIFRA fichas AL SALIR: %d (se exige %d)" % (len(filas2), len(filas)))
    di("CIFRA lo escrito es identico a lo juzgado: %s"
       % ("SI" if raw2 == texto_nuevo else "NO"))
    fallos2, inf2 = juzgar(lineas, lineas2)
    for l in inf2:
        di(l)
    di("CIFRA fallos de la guarda SOBRE EL DISCO: %d (se exige 0)" % fallos2)
    c1 = cuentas_por_estado(filas2)
    di("LA TABLA DE CUENTAS POR estado AL SALIR: %d fila(s) armada(s), y suman %d"
       % (len(c1), sum(c1.values())))
    for k in sorted(c1, key=lambda x: (x is None, x)):
        di("   estado> %-8s %d" % (k, c1[k]))
    di("CIFRA las cuentas por estado son IDENTICAS a las de la entrada: %s"
       % ("SI" if c1 == c0 else "NO"))
    sd1, _ = sede(ARCHIVO, "AL SALIR")
    di("CIFRA el sha256 cambia entre entrada y salida: %s (se exige SI)"
       % ("SI" if sd1 != sd0 else "NO"))
    ns1 = numstat("docs/plan/")
    di("CIFRA filas de git diff --numstat -- docs/plan/ AL SALIR: %d (se exige 1, y "
       "es %s)" % (len(ns1), ARCHIVO))
    for l in ns1:
        di("   numstat> %s" % l)
    f2f = [f for f in filas2 if f["id_op"] == FICHA][0]
    di("CIFRA el campo nodos de %s AL SALIR: %d (se exige %d)"
       % (FICHA, len(f2f.get("nodos") or []), len(nodos)))
    di("CIFRA el campo estado de %s AL SALIR: %r (se exige %r)"
       % (FICHA, f2f.get("estado"), ficha.get("estado")))
    di("CIFRA bytes de la adjudicacion AL SALIR: %d"
       % len((f2f.get("adjudicacion") or "").encode("utf-8")))
    ok = (fallos2 == 0 and not malas and raw2 == texto_nuevo and sd1 != sd0
          and c1 == c0 and len(ns1) == 1
          and len(f2f.get("nodos") or []) == len(nodos)
          and f2f.get("estado") == ficha.get("estado"))
    di("")
    di("VERDE: la `P.2` queda declarada sobre el campo adjudicacion, con el texto "
       "viejo entero encima, y ni nodos ni estado se movieron."
       if ok else "ROJO: la salida no calza con lo juzgado.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    codigo = main()
    texto = NL.join(OUT) + NL
    io.open(os.path.join(RAIZ, "docs", "loop",
                         "SALIDA_V%d_T1C_OP_F_04_HOR.txt" % VUELTA),
            "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    sys.stdout.write("EXITCODE: %d%s" % (codigo, NL))
    sys.exit(codigo)
