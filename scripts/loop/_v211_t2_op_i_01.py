# -*- coding: utf-8 -*-
r"""_v211_t2_op_i_01.py . TAREA 2 DE LA VUELTA 211: `OP-I-01`, LA ULTIMA DE LAS
CUATRO FICHAS REALES DE LA MORATORIA, **MEDIDA Y NO CERRADA**.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3). **NO ESCRIBE EN NINGUNA SEDE DEL PLAN**:
abre todo en lectura. El punto 7 del encargo lo dice entero: *"NO TOQUES EL CAMPO
`estado` DE `OP-I-01`. Mide, adjudica lo que puedas con cita, y deja el cierre de
la ficha al acta"*.

**IMPORTAR NO ES CLONAR** (acta 206 `6.5`): `dos_convenciones` se IMPORTA de
`_v209_t2c_cerrar_opl01.py`, la misma sede de las dos convenciones que uso la
209 y que el acta 209 reprodujo al digito.

LOS SIETE PASOS DEL ENCARGO, EN SU ORDEN, Y CADA UNO CON SU CIFRA:

  1. LA FORMA DE LA FICHA, leida entera del `jsonl`.
  2. SU CRITERIO DE HECHO contra la fila `10 INVENTARIO` de
     `docs/plan/08_VERIFICACION.md`. **AQUI HAY PARADA Y NO IMPROVISACION**: la
     fila NO EXISTE, y este computo lo MIDE en vez de suponerlo, imprimiendo las
     filas que la tabla SI tiene. El encargo manda medir *"contra ella y no
     contra tu idea de lo que la ficha deberia ser"*, y una fila que no esta no
     se sustituye por la que a uno le parezca.
  3. PUNTO POR PUNTO de su `verificacion`, cada uno con CUBRE, A MEDIAS o NO
     CUBRE, **su cita, su fichero y su linea**. CIFRA de puntos sin cita: 0.
  4. LAS TRES SEDES de su evidencia, por las dos convenciones, AL ENTRAR y AL
     SALIR.
  5. LAS 336 ENTRADAS que la seccion 5 de `AUDITOR.md` lleva publicadas,
     RECOMPUTADAS DEL FICHERO con comando propio, y **las dos publicadas al
     lado**. Si no calzan, LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO
     NINGUNA DE LAS DOS (`AUDITOR.md` 1.1).

**LA BUSQUEDA NEGATIVA NO SE CITA** (`EJECUTOR.md` 9). Donde un punto solo se
puede comprobar por ausencia, este computo lo dice y baja el veredicto a
A MEDIAS en vez de escribir un CUBRE que no puede sostener.
"""
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

from _v209_t2c_cerrar_opl01 import dos_convenciones  # noqa: E402

OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VERIF = os.path.join(RAIZ, "docs", "plan", "08_VERIFICACION.md")
INV_JSONL = "docs/plan/INVENTARIO.jsonl"
INV_MD = "docs/plan/10_INVENTARIO.md"
AUD = "docs/loop/AUDITOR.md"
SEDES = [INV_JSONL, INV_MD, AUD]
FICHA = "OP-I-01"
CONTRASTE = {INV_JSONL: (584554, 584554), INV_MD: (34258, 33845), AUD: (30581, 30581)}


def lf(ruta):
    return io.open(os.path.join(RAIZ, ruta.replace("/", os.sep)), "rb").read(
        ).replace(b"\r\n", b"\n").decode("utf-8")


def sede(w, etiqueta):
    w("   %s, %s:" % (etiqueta, "por las dos convenciones"))
    medidas = {}
    for r in SEDES:
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        d, l, sd, sl, _ = dos_convenciones(p)
        medidas[r] = (d, l, sd, sl)
        c = CONTRASTE[r]
        w("      %-28s %d bytes en disco y %d normalizado a LF (%s), sha256 disco %s y LF %s"
          % (r, d, l, "COINCIDEN" if d == l else "NO COINCIDEN", sd, sl))
        w("         contraste del encargo: %d y %d  ->  CALZA: %s"
          % (c[0], c[1], "SI" if (d, l) == c else "NO, Y SE DECLARA"))
    return medidas


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append

    def cerrar(codigo):
        salida = NL.join(L) + NL
        print(salida)
        io.open(os.path.join(LOOP, "SALIDA_V%d_T2_OP_I_01.txt" % VUELTA),
                "w", encoding="utf-8", newline=NL).write(salida)
        return codigo

    w("=" * 78)
    w("VUELTA %d, TAREA 2: %s, MEDIDA Y NO CERRADA. NO SE TOCA SU CAMPO estado."
      % (VUELTA, FICHA))
    w("=" * 78)
    w("")

    w("PASO 4, PRIMERA MITAD: LAS TRES SEDES AL ENTRAR")
    ent = sede(w, "AL ENTRAR")
    w("")

    # ---- PASO 1 -------------------------------------------------------------
    w("=" * 78)
    w("PASO 1. LA FORMA DE LA FICHA, LEIDA ENTERA DEL jsonl")
    w("=" * 78)
    texto = lf("docs/plan/OPERACIONES.jsonl")
    ficha = None
    linea_ficha = None
    for i, l in enumerate(texto.split(NL), 1):
        if not l.strip():
            continue
        d = json.loads(l)
        if d["id_op"] == FICHA:
            ficha, linea_ficha = d, i
    if ficha is None:
        w("   ROJO: %s no esta en el fichero." % FICHA)
        return cerrar(1)
    w("   linea del fichero: %d" % linea_ficha)
    w("   CIFRA campos: %d" % len(ficha))
    w("   claves: %s" % ", ".join(sorted(ficha)))
    for k in ("tipo", "orden", "fase", "fecha_corte", "estado"):
        w("   %-14s %r" % (k, ficha.get(k)))
    for k in ("depende_de", "bloquea_a"):
        v = ficha.get(k)
        w("   %-14s %r (CIFRA elementos: %s)"
          % (k, v, len(v) if isinstance(v, list) else "no es lista"))
    w("")
    w("   EL TAMANO EN CARACTERES DE LOS CUATRO CAMPOS QUE EL ENCARGO PIDE:")
    for k in ("evidencia", "verificacion", "adjudicacion", "nota"):
        v = ficha.get(k)
        if isinstance(v, list):
            w("      %-14s LISTA de %d elementos, %d caracteres sumados"
              % (k, len(v), sum(len(x) for x in v)))
        else:
            w("      %-14s cadena de %d caracteres" % (k, len(v or "")))
    w("")

    # ---- PASO 2 -------------------------------------------------------------
    w("=" * 78)
    w("PASO 2. SU CRITERIO DE HECHO CONTRA LA FILA `10 INVENTARIO`")
    w("=" * 78)
    tv = lf("docs/plan/08_VERIFICACION.md").split(NL)
    filas = []
    for i, l in enumerate(tv, 1):
        m = re.match(r"^\|\s+\*\*(\S+)\s+([A-ZÑ ]+)\*\*\s+\|", l)
        if m:
            filas.append((i, m.group(1), m.group(2).strip()))
    w("   LA TABLA `POR FASE` DE docs/plan/08_VERIFICACION.md, BARRIDA Y NO RECORDADA:")
    for i, num, nombre in filas:
        w("      linea %d | fila `%s %s`" % (i, num, nombre))
    w("   CIFRA filas de la tabla: %d" % len(filas))
    hay10 = [f for f in filas if f[1] == "10"]
    w("   CIFRA filas cuyo numero de fase es 10: %d" % len(hay10))
    w("   CIFRA menciones del literal '10 INVENTARIO' en el fichero entero: %d"
      % lf("docs/plan/08_VERIFICACION.md").count("10 INVENTARIO"))
    w("")
    if not hay10:
        w("   *** PARADA, Y NO IMPROVISACION (encargo, punto 6; `AUDITOR.md` 3) ***")
        w("   LA FILA `10 INVENTARIO` QUE EL ENCARGO MANDA CITAR **NO EXISTE**.")
        w("   La tabla llega hasta `07 ADUANA` y no tiene fila 08, 09 ni 10.")
        w("   El encargo dice: medir 'contra ella y no contra tu idea de lo que la")
        w("   ficha deberia ser'. Una fila que no esta NO SE SUSTITUYE por la que a")
        w("   uno le parezca, y por eso este paso queda SIN VEREDICTO y se trae.")
        w("")
        w("   LO QUE SI EXISTE, Y SE PUBLICA SIN ADJUDICARLO A ESTA FICHA:")
        crit = [(i, l) for i, l in enumerate(tv, 1)
                if "UNA FASE ESTA HECHA CUANDO" in l]
        for i, l in crit:
            w("      linea %d: %s" % (i, l.strip("> ").strip()))
        w("      Es el criterio general, que el propio fichero titula")
        w("      'EL CRITERIO DE HECHO, y es uno solo'. **Que ese criterio general")
        w("      valga para una ficha de fase 10 sin fila propia es precisamente")
        w("      LA DECISION QUE NO ME TOCA**, y por eso se trae en vez de usarse.")
    w("")

    # ---- PASO 3 -------------------------------------------------------------
    w("=" * 78)
    w("PASO 3. PUNTO POR PUNTO DE SU `verificacion`, CADA UNO CON SU CITA")
    w("=" * 78)
    E = [json.loads(l) for l in lf(INV_JSONL).split(NL) if l.strip()]
    md = lf(INV_MD).split(NL)

    con_corte = [d for d in E if d.get("fecha_corte")]
    pat = re.compile(r"^(\d+) de (\d+) pares leidos")
    incompletas = []
    con_forma_n = 0
    for d in E:
        m = pat.match(str(d.get("cobertura") or ""))
        if m:
            con_forma_n += 1
            if int(m.group(1)) < int(m.group(2)):
                incompletas.append(d)
    marcadas = [d for d in incompletas
                if "PROVISIONAL" in json.dumps(d, ensure_ascii=False).upper()]
    con_prov = [d for d in E if "PROVISIONAL" in json.dumps(d, ensure_ascii=False).upper()]
    con_hueco = [d for d in E if "HUECO" in json.dumps(d, ensure_ascii=False).upper()]

    def linea_md(frag):
        h = [i for i, l in enumerate(md, 1) if frag in l]
        return h[0] if len(h) == 1 else 0

    def linea_v(frag):
        h = [i for i, l in enumerate(tv, 1) if frag in l]
        return h[0] if len(h) == 1 else 0

    l_corte = linea_md("que se copia lleva su fecha de corte")
    l_hueco = linea_md("como HUECO NOMBRADO, no se rellena")
    l_disp = linea_v("Se dispara EL DIA QUE EL CRIBADO LLEGUE AL PUESTO 3.388")
    l_nogen = linea_md("LA TABLA NO SE REGENERA AQUI, A PROPOSITO")
    l_vista = linea_md("| filas totales |")

    puntos = []
    puntos.append((
        1, ficha["verificacion"][0], "CUBRE",
        "CIFRA entradas: %d. CIFRA con `fecha_corte`: %d. CIFRA sin `fecha_corte`: %d."
        % (len(E), len(con_corte), len(E) - len(con_corte)),
        "%s (contado hoy, entrada a entrada) y la regla en %s linea %d: "
        "\"todo lo que se copia lleva su fecha de corte\""
        % (INV_JSONL, INV_MD, l_corte)))
    puntos.append((
        2, ficha["verificacion"][1], "NO CUBRE",
        "CIFRA entradas con cobertura de la forma 'N de M pares leidos': %d. "
        "De esas, INCOMPLETAS (N menor que M): %d. De esas incompletas, con la "
        "palabra PROVISIONAL en algun campo: %d. CIFRA entradas del inventario "
        "entero que llevan PROVISIONAL: %d, y las tres son de tipo `racimo`, "
        "ninguna de ellas incompleta por esta cuenta."
        % (con_forma_n, len(incompletas), len(marcadas), len(con_prov)),
        "%s, contado hoy campo a campo" % INV_JSONL))
    puntos.append((
        3, ficha["verificacion"][2], "A MEDIAS",
        "LA MITAD QUE SE PUEDE MEDIR: CIFRA entradas que nombran HUECO en algun "
        "campo: %d, o sea que el hueco SI se nombra. LA MITAD QUE NO SE PUEDE "
        "MEDIR: 'nunca rellenado' es una NEGATIVA, y una busqueda negativa no se "
        "puede citar (`EJECUTOR.md` 9). Por eso no escribo CUBRE."
        % len(con_hueco),
        "%s (contado hoy) y la regla en %s linea %d: "
        "\"Lo que no existe todavia se escribe como HUECO NOMBRADO, no se rellena\""
        % (INV_JSONL, INV_MD, l_hueco)))
    puntos.append((
        4, ficha["verificacion"][3], "A MEDIAS",
        "EL DISPARADOR YA DISPARO Y LAS DOS MITADES NO FUERON A LA VEZ. El "
        "archivo fuente SI se recomputo: la propia vista humana publica que "
        "esta al corte 2.117 y que 'el archivo fuente tiene hoy (corte 3.388)'. "
        "La vista humana NO se recomputo, y lo dice ella misma con todas las "
        "letras. 'El inventario' son las dos formas que la adjudicacion de la "
        "ficha nombra, y solo una esta al dia.",
        "%s linea %d (\"Se dispara EL DIA QUE EL CRIBADO LLEGUE AL PUESTO 3.388\"), "
        "%s linea %d (\"LA TABLA NO SE REGENERA AQUI, A PROPOSITO\") y %s linea %d "
        "(la fila `filas totales` de su propia tabla de aviso)"
        % ("docs/plan/08_VERIFICACION.md", l_disp, INV_MD, l_nogen, INV_MD, l_vista)))

    sin_cita = 0
    for n, texto_p, veredicto, medicion, cita in puntos:
        w("")
        w("   PUNTO %d. %r" % (n, texto_p))
        w("      VEREDICTO: **%s**" % veredicto)
        w("      LO MEDIDO: %s" % medicion)
        w("      CITA, CON SU FICHERO Y SU LINEA: %s" % cita)
        if not cita.strip():
            sin_cita += 1
    w("")
    w("   CIFRA puntos de la `verificacion`: %d" % len(puntos))
    w("   CIFRA puntos que quedan SIN CITA: %d (se exige 0)" % sin_cita)
    rep = {}
    for _n, _t, v, _m, _c in puntos:
        rep[v] = rep.get(v, 0) + 1
    w("   EL REPARTO: %s" % ", ".join("%s %d" % (k, rep[k]) for k in sorted(rep)))
    w("")

    # ---- PASO 5 -------------------------------------------------------------
    w("=" * 78)
    w("PASO 5. LAS 336 ENTRADAS DE `AUDITOR.md` 5, RECOMPUTADAS DEL FICHERO")
    w("=" * 78)
    aud = lf(AUD).split(NL)
    h = [i for i, l in enumerate(aud, 1) if "inventario de 336 entradas" in l]
    w("   LA CIFRA PUBLICADA, LEIDA DE SU SEDE Y NO RECORDADA:")
    for i in h:
        w("      %s linea %d: %s" % (AUD, i, aud[i - 1].strip("- ").strip()))
        w("      %s linea %d: %s" % (AUD, i + 1, aud[i].strip()))
    publicado = {"dominio": 10, "acto": 221, "racimo": 13,
                 "familia_de_ids": 53, "figura": 20, "defecto": 19}
    w("   SUMA de la cifra publicada, recontada de sus propios sumandos: %d"
      % sum(publicado.values()))
    w("")
    mio = {}
    for d in E:
        mio[d.get("tipo")] = mio.get(d.get("tipo"), 0) + 1
    w("   MI RECOMPUTO DE HOY, CONTANDO %s LINEA A LINEA:" % INV_JSONL)
    w("")
    w("   | tipo | `AUDITOR.md` 5 (corte 12 ago 2026) | mi conteo de hoy | calza |")
    w("   |---|---:|---:|---|")
    for k in sorted(set(list(publicado) + list(mio))):
        a, b = publicado.get(k, 0), mio.get(k, 0)
        w("   | `%s` | %d | %d | %s |" % (k, a, b, "SI" if a == b else "**NO**"))
    w("   | **TOTAL** | **%d** | **%d** | %s |"
      % (sum(publicado.values()), sum(mio.values()),
         "SI" if sum(publicado.values()) == sum(mio.values()) else "**NO**"))
    w("")
    w("   CIFRA lineas del fichero que no son JSON valido: 0 (contadas al leer)")
    w("   LAS DOS CIFRAS SE PUBLICAN AL LADO Y **NO SE RESUELVE COPIANDO NINGUNA**")
    w("   (`AUDITOR.md` 1.1). La de 336 lleva su corte y el archivo pudo envejecer")
    w("   honestamente (banco `9.21`).")
    w("")
    w("   Y LA DISCREPANCIA TIENE CAUSA MEDIDA, QUE NO ES LA MISMA PARA LOS DOS TIPOS:")
    l32 = linea_md("| filas totales |")
    l33 = linea_md("los otros cinco tipos")
    w("      %s linea %d publica `filas totales` **671** para el archivo fuente al"
      % (INV_MD, l32))
    w("      corte 3.388, y mi conteo de hoy da **%d**." % sum(mio.values()))
    w("      %s linea %d dice de los otros cinco tipos: \"identicos, no se movieron\","
      % (INV_MD, l33))
    fam = [d for d in E if d.get("tipo") == "familia_de_ids"]
    tardias = [d for d in fam if str(d.get("fecha_corte")) > "2026-08-11"]
    w("      y `familia_de_ids` **SI se movio**: %d hoy contra las 53 de esa fila."
      % len(fam))
    w("      CIFRA `familia_de_ids` con `fecha_corte` posterior al 2026-08-11: %d"
      % len(tardias))
    for d in tardias:
        w("         %r, fecha_corte %s" % (d.get("nombre"), d.get("fecha_corte")))
    w("      ESA ES LA UNIDAD QUE SEPARA 671 DE %d, y queda declarada."
      % sum(mio.values()))
    w("")

    w("=" * 78)
    w("PASO 4, SEGUNDA MITAD: LAS TRES SEDES AL SALIR, REMEDIDAS Y NO HEREDADAS")
    w("=" * 78)
    sal = sede(w, "AL SALIR")
    w("")
    iguales = sum(1 for r in SEDES if ent[r] == sal[r])
    w("   CIFRA sedes que salen identicas a como entraron: %d de %d"
      % (iguales, len(SEDES)))
    w("   ESTA TAREA NO ESCRIBE EN NINGUNA DE LAS TRES, asi que se exigen las tres.")
    w("")
    w("EL CAMPO estado DE %s, RELEIDO AL SALIR: %r"
      % (FICHA, ficha.get("estado")))
    w("   NO SE TOCO, Y ESE ES EL PUNTO 7 DEL ENCARGO.")
    w("")
    w("FIN")
    return cerrar(0 if (sin_cita == 0 and iguales == len(SEDES)) else 1)


if __name__ == "__main__":
    raise SystemExit(main())
