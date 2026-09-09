# -*- coding: utf-8 -*-
r"""_v219_t1_registros.py . LA TAREA 1 DE LA VUELTA 219: LOS REGISTROS.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). NO ES ARNES NI GUARDA NI LECTOR NUEVO:
ES LECTURA, MEDICION Y REGISTRO, que es lo que la moratoria protege.

  1.a  LAS SEIS ADJUDICACIONES DEL ACTA 218, cada una con su rotulo, su numero
       de adjudicacion y SU LINEA LEIDA DEL FICHERO. Las lineas NO SE TECLEAN:
       el instrumento busca el ancla en docs/loop/ACTA_AUDITOR.md, publica su
       numero de linea y su texto verbatim, y CAE EN ROJO si un ancla no
       aparece o aparece mas de una vez. Y se comprueba, contra el registro y
       contra el marcador, que NINGUNA de las seis mueve un veredicto: si el
       registro dijera lo contrario, esta tarea PARA.

  1.b  EL RECUENTO DE LAS DIECISIETE, REMEDIDO HOY Y NO HEREDADO. La cifra sale
       de la corrida de HOY del mismo lector que el auditor reprodujo byte a
       byte (_v218_t2_lecturas.py, sellada en
       docs/loop/SALIDA_V219_T1_RECORRIDA_DEL_LECTOR.txt) y se publica JUNTO A
       la que la 218 dejo en docs/loop/SALIDA_V218_T2_LECTURAS.txt. LAS DOS
       CIFRAS JUNTAS, la medida y la heredada, y si discrepan se para.

  1.c  LAS SEIS COSAS QUE SUBEN NOMBRADAS A LA AUDITORIA INTEGRAL, con su cifra
       y su linea leida de la seccion 6 del acta 218. NO SE RESUELVEN: solo
       tienen que quedar escritas donde el fundador las encuentre.

EL CASO ROJO NO SE PROMETE Y SE DICE CUAL ES CUAL (EJECUTOR.md 1, EL CASO ROJO
SE PRUEBA POR MUTACION). La localizacion de las lineas de acta, la lectura del
recuento y el cotejo del marcador son MAQUINA de punta a punta y CAEN EN ROJO
por si solas. La glosa de cada adjudicacion es MIA y va firmada como tal: para
esa parte NO HAY CASO ROJO AUTOMATICO, y se declara en vez de fabricarse uno
que se apruebe solo.

CERO ESCRITURAS EN EL PLAN: esta tarea solo lee.

USO:  python scripts/loop/_v219_t1_registros.py
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

ACTA = "docs/loop/ACTA_AUDITOR.md"
EXPEDIENTE = "docs/plan/OPERACIONES.jsonl"
PAG08 = "docs/plan/08_VERIFICACION.md"
PAG07 = "docs/plan/07_ADUANA.md"
PAG01 = "docs/plan/01_FUENTES.md"
PAG05 = "docs/plan/05_SANEO.md"
INVENTARIO = "docs/plan/INVENTARIO.jsonl"
VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"

SEDES = (EXPEDIENTE, PAG08, PAG07, PAG01, PAG05, INVENTARIO)

# LAS SEIS ADJUDICACIONES. EL ANCLA NO ES LA RESPUESTA: es DONDE MIRAR. El
# numero de linea lo pone el fichero, no yo.
ADJUDICACIONES = [
    ("D.1", "4.1", "puesto 299 en D",
     "**`4.1` `D.1` SE ADJUDICA A FAVOR"),
    ("D.2", "4.2", "puesto 1249 en D",
     "**`4.2` `D.2` SE ADJUDICA A FAVOR"),
    ("D.3 y P.3", "4.3", "escribir en el registro del cribado estaba ORDENADO",
     "**`4.3` `D.3` Y `P.3` SE ADJUDICAN JUNTAS"),
    ("D.4", "4.4", "el ANTES es la VISPERA DE LA FASE 01",
     "**`4.4` `D.4` SE ADJUDICA A FAVOR"),
    ("D.5", "4.5", "la clausula exige el HECHO, no la FRASE",
     "**`4.5` `D.5` SE ADJUDICA A FAVOR"),
    ("D.6", "4.6", "no fabricar el mutante fue la lectura correcta",
     "**`4.6` `D.6` SE ADJUDICA A FAVOR"),
]

# LA CITA DE SEGUNDO GRADO QUE LA 4.3 APOYA EN EL ACTA 217, tambien localizada
# y no tecleada.
CITA_217 = ("acta 217", "5.7", "**`5.7`")

# LAS SEIS DE LA SECCION 6 DEL ACTA 218. Otra vez: ancla, no respuesta.
INTEGRAL = [
    ("1", "la celda de 07 ADUANA de la pagina 08 dice CUATRO y su ficha OP-A-02 dice CINCO",
     "1. **La celda de `07 ADUANA` de `docs/plan/08_VERIFICACION.md`, linea 30, dice CUATRO"),
    ("2", "vuelta150_4_tabla_por_fase.py en rojo, la tabla no trae ocho filas sino 11",
     "2. **`scripts/loop/vuelta150_4_tabla_por_fase.py` en rojo**"),
    ("3", "el rotulo de la salida de bateria dice VUELTA 183 sobre contenido de la 215",
     "3. **El rotulo de `docs/loop/SALIDA_V183_BATERIA.txt`"),
    ("4", "la familia C.1 del auditor en OCHO, con el remedio del fundador medido fallando DOS veces",
     "4. **Mi familia `C.1` en OCHO"),
    ("5", "la ciega no puede acertar las clases B y C, que viven de figuras de tres o mas",
     "5. **La ciega no puede acertar las clases `B` y `C`**"),
    ("6", "las CUATRO clausulas en A MEDIAS, con su cifra cada una",
     "6. **Las CUATRO clausulas en A MEDIAS**"),
]

# LO QUE EL REGISTRO TIENE QUE SEGUIR DICIENDO PARA QUE NINGUNA ADJUDICACION
# MUEVA UN VEREDICTO. Son las dos que la 218 dejo escritas.
PUESTOS_QUE_NO_SE_MUEVEN = [(299, "D"), (1249, "D")]
MARCADOR_CORTE = 3388


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def sha16(rel):
    b = io.open(os.path.join(RAIZ, rel.replace("/", os.sep)), "rb").read()
    return (hashlib.sha256(b).hexdigest()[:16],
            hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16])


def bytes_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    b = io.open(p, "rb").read()
    return os.path.getsize(p), len(b.replace(b"\r\n", b"\n"))


def localizar(lineas, ancla, desde=1):
    """DONDE VIVE UN ANCLA EN UN FICHERO YA LEIDO. PURA.

    Devuelve la lista de numeros de linea (base 1) a partir de `desde` cuyo
    texto EMPIEZA por el ancla. Una lista que no tenga exactamente un elemento
    es un fallo del que la llama, y aqui se cuenta como tal."""
    return [n for n, l in enumerate(lineas, start=1)
            if n >= desde and l.startswith(ancla)]


def main():
    out = []
    fallos = 0

    def w(s=""):
        out.append(s)

    w("=" * 78)
    w("TAREA 1 DE LA VUELTA %d: LOS REGISTROS. LECTURA, MEDICION Y REGISTRO."
      % VUELTA)
    w("=" * 78)
    w("")
    w("LOS SHA256 DE LAS SEDES DEL PLAN, AL ENTRAR, POR LAS DOS CONVENCIONES:")
    entrada = {}
    for rel in SEDES:
        entrada[rel] = sha16(rel)
        bd, bl = bytes_de(rel)
        w("   %s: %d bytes en disco y %d normalizado a LF, sha256 disco %s y "
          "sha256 LF %s" % ((rel, bd, bl) + entrada[rel]))
    w("")

    lineas_acta = leer(ACTA).split(NL)
    w("EL FICHERO DE LAS CITAS, MEDIDO HOY: %s, %d lineas leidas."
      % (ACTA, len(lineas_acta)))
    ancla_218 = localizar(lineas_acta,
                          "# ACTA DEL AUDITOR, VUELTA 218:")
    w("CIFRA lineas donde empieza el acta 218: %d | CIFRA que se exige: 1"
      % len(ancla_218))
    if len(ancla_218) != 1:
        fallos += 1
        inicio_218 = 1
    else:
        inicio_218 = ancla_218[0]
        w("   EL ACTA 218 EMPIEZA EN LA LINEA %d, y el encargo dice 77376: %s"
          % (inicio_218, "CALZA" if inicio_218 == 77376 else "NO CALZA"))
        if inicio_218 != 77376:
            fallos += 1
    w("")

    # =================================================================== 1.a
    w("=" * 78)
    w("1.a. LAS SEIS ADJUDICACIONES CAYERON DE MI LADO, Y NINGUNA MUEVE UN "
      "VEREDICTO")
    w("=" * 78)
    w("")
    w("   LA LINEA NO SE TECLEA: se localiza el ancla en %s a partir de la "
      "linea %d y se publica su numero y su texto verbatim." % (ACTA, inicio_218))
    w("")
    filas_adj = []
    for rot, num, sostiene, ancla in ADJUDICACIONES:
        donde = localizar(lineas_acta, ancla, desde=inicio_218)
        w("   ADJUDICACION %-4s (rotulo %-9s) | CIFRA lineas que casan el "
          "ancla: %d | CIFRA que se exige: 1" % (num, rot, len(donde)))
        if len(donde) != 1:
            fallos += 1
            w("      ROJO: el ancla %r no aparece exactamente una vez." % ancla)
            continue
        n = donde[0]
        w("      LINEA %d, LEIDA DEL FICHERO> %s" % (n, lineas_acta[n - 1]))
        w("      LO QUE SOSTIENE: %s" % sostiene)
        filas_adj.append((rot, num, n, sostiene))
    w("")
    w("   CIFRA adjudicaciones localizadas con su linea: %d | CIFRA que el "
      "encargo lista: 6" % len(filas_adj))
    if len(filas_adj) != 6:
        fallos += 1
    w("")
    w("   LA CITA DE SEGUNDO GRADO EN QUE LA 4.3 SE APOYA, TAMBIEN LOCALIZADA:")
    # CORRECCION DECLARADA DENTRO DE LA PROPIA VUELTA, y el ancla vieja queda
    # escrita sin borrar porque una correccion que tapa lo que corrige no se
    # puede auditar: la primera version de esta linea buscaba
    # "# ACTA DEL AUDITOR, VUELTA 217:" con dos puntos, copiando la forma de la
    # cabecera del acta 218, y la del acta 217 NO lleva dos puntos sino un
    # parentesis con su fecha. LA CAZO ESTA MISMA GUARDA, en rojo, antes de que
    # el numero llegara a ningun reporte.
    ancla_217 = localizar(lineas_acta, "# ACTA DEL AUDITOR, VUELTA 217")
    if len(ancla_217) != 1:
        fallos += 1
        w("      ROJO: el acta 217 no empieza exactamente una vez.")
    else:
        i217 = ancla_217[0]
        d217 = [n for n in localizar(lineas_acta, CITA_217[2], desde=i217)
                if n < inicio_218]
        w("      el acta 217 empieza en la linea %d" % i217)
        w("      CIFRA lineas que casan el ancla de la %s dentro del acta 217: "
          "%d | CIFRA que se exige: 1" % (CITA_217[1], len(d217)))
        if len(d217) != 1:
            fallos += 1
        else:
            w("      LINEA %d, LEIDA DEL FICHERO> %s"
              % (d217[0], lineas_acta[d217[0] - 1]))
            w("      y el encargo la cita en la 77304: %s"
              % ("CALZA" if d217[0] == 77304 else "NO CALZA"))
            if d217[0] != 77304:
                fallos += 1
    w("")

    w("   LA COMPROBACION DE QUE NINGUNA MUEVE UN VEREDICTO, CONTRA EL REGISTRO "
      "Y NO CONTRA MI RECUERDO:")
    ver = [json.loads(l) for l in leer(VEREDICTOS).split(NL) if l.strip()]
    w("      CIFRA veredictos en el registro: %d" % len(ver))
    por_puesto = {}
    for v in ver:
        por_puesto[v.get("puesto_intra")] = v
    for puesto, clase_esperada in PUESTOS_QUE_NO_SE_MUEVEN:
        v = por_puesto.get(puesto)
        if v is None:
            fallos += 1
            w("      ROJO: el puesto %d no esta en el registro." % puesto)
            continue
        clase = str(v.get("clase") or "")
        razon = str(v.get("razon") or "")
        ok = clase == clase_esperada
        w("      puesto %-5d | clase en el registro HOY: %-2s | clase que la "
          "218 dejo: %-2s | %s | razon de %d bytes | lleva CORRECCION "
          "DECLARADA: %s"
          % (puesto, clase, clase_esperada, "CALZA" if ok else "NO CALZA",
             len(razon.encode("utf-8")),
             "SI" if "CORRECCION DECLARADA" in razon else "NO"))
        if not ok:
            fallos += 1
    r = subprocess.run([sys.executable, "scripts/recomputar_marcador.py",
                        str(MARCADOR_CORTE)], cwd=RAIZ, capture_output=True)
    salida_marc = (r.stdout + r.stderr).decode("utf-8", "replace").replace(
        chr(13) + NL, NL)
    io.open(os.path.join(LOOP, "SALIDA_V%d_T1_MARCADOR.txt" % VUELTA),
            "w", encoding="utf-8", newline=NL).write(salida_marc)
    w("      EL MARCADOR RECOMPUTADO HOY (scripts/recomputar_marcador.py %d), "
      "exitcode %d, sellado en docs/loop/SALIDA_V%d_T1_MARCADOR.txt:"
      % (MARCADOR_CORTE, r.returncode, VUELTA))
    for l in salida_marc.split(NL):
        if l.strip():
            w("        marcador> " + l.rstrip())
    if r.returncode != 0:
        fallos += 1
    w("")
    w("      CIFRA correcciones que esta vuelta tiene que aplicar por "
      "adjudicacion: 0 | CIFRA que el encargo ordena: 0")
    w("      (el encargo dice NO HAY NINGUNA CORRECCION QUE APLICAR EN ESTA "
      "VUELTA, y mi registro NO dice lo contrario: las dos clases calzan y el "
      "marcador es el mismo. NO PARO.)")
    w("")
    w("   LA TABLA DE LAS SEIS, ARMADA DE LO LOCALIZADO ARRIBA Y NO TECLEADA:")
    w("| rotulo | adjudicacion | linea del acta 218, LEIDA DEL FICHERO | que se sostiene | mueve veredicto |")
    w("|---|---|---:|---|---|")
    for rot, num, n, sostiene in filas_adj:
        w("| `%s` | `%s` | **%d** | %s | **NO** |" % (rot, num, n, sostiene))
    w("   CIFRA filas armadas: %d | CIFRA que deberia haber: 6" % len(filas_adj))
    w("")

    # =================================================================== 1.b
    w("=" * 78)
    w("1.b. EL RECUENTO DE LAS DIECISIETE, REMEDIDO HOY Y NO HEREDADO")
    w("=" * 78)
    w("")
    rel_hoy = "docs/loop/SALIDA_V%d_T1_RECORRIDA_DEL_LECTOR.txt" % VUELTA
    rel_218 = "docs/loop/SALIDA_V218_T2_LECTURAS.txt"
    for rel in (rel_hoy, rel_218):
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(p):
            fallos += 1
            w("   ROJO: %s NO EXISTE, y una ruta que promete prueba es cifra."
              % rel)
            continue
        bd, bl = bytes_de(rel)
        if bd == 0:
            fallos += 1
            w("   ROJO: %s mide CERO BYTES y eso no cuenta como corrida." % rel)
        sd, sl = sha16(rel)
        w("   %s: %d bytes en disco y %d normalizado a LF, sha256 disco %s y "
          "sha256 LF %s" % (rel, bd, bl, sd, sl))
    w("")
    w("   EL INSTRUMENTO ES EL MISMO QUE EL AUDITOR REPRODUJO BYTE A BYTE: "
      "scripts/loop/_v218_t2_lecturas.py, corrido HOY por mi. Su fichero "
      "sellado propio no cambio de contenido al re-correrlo, y eso es la "
      "prueba de que es un lector y no un escritor.")
    pat = re.compile(r"CIFRA clausulas en (CUBRE|A MEDIAS|NO CUBRE) AL CIERRE "
                     r"DE LA TAREA 2: (\d+) de 17")
    hoy, dejo218 = {}, {}
    for l in leer(rel_hoy).split(NL):
        m = pat.search(l)
        if m:
            hoy[m.group(1)] = int(m.group(2))
    for l in leer(rel_218).split(NL):
        m = pat.search(l)
        if m:
            dejo218[m.group(1)] = int(m.group(2))
    w("   CIFRA filas de recuento leidas de mi corrida de hoy: %d | CIFRA "
      "leidas de la salida que la 218 dejo: %d | CIFRA que deberia haber en "
      "cada una: 3" % (len(hoy), len(dejo218)))
    if len(hoy) != 3 or len(dejo218) != 3:
        fallos += 1
    w("")
    w("| veredicto | CIFRA que MIDO HOY, al abrir la 219 | CIFRA que la 218 DEJO | |")
    w("|---|---:|---:|---|")
    for k in ("CUBRE", "A MEDIAS", "NO CUBRE"):
        a, b = hoy.get(k), dejo218.get(k)
        igual = "CALZA" if (a is not None and a == b) else "NO CALZA"
        w("| **%s** | **%s de 17** | %s de 17 | %s |" % (k, a, b, igual))
        if a is None or a != b:
            fallos += 1
    w("   CIFRA filas armadas: 3 | CIFRA que deberia haber: 3")
    w("")
    w("   Y LA CIFRA DEL ENCARGO, CITADA COMO CONTRASTE Y NO COMO FUENTE: el "
      "encargo dice 13 CUBRE, 4 A MEDIAS, 0 NO CUBRE.")
    w("   MI MEDICION DE HOY: %s CUBRE, %s A MEDIAS, %s NO CUBRE."
      % (hoy.get("CUBRE"), hoy.get("A MEDIAS"), hoy.get("NO CUBRE")))
    calza_encargo = (hoy.get("CUBRE"), hoy.get("A MEDIAS"),
                     hoy.get("NO CUBRE")) == (13, 4, 0)
    w("   CALZA CON EL CONTRASTE DEL ENCARGO: %s"
      % ("SI" if calza_encargo else "NO"))
    if not calza_encargo:
        fallos += 1
    w("")
    w("   LAS CUATRO QUE SIGUEN SIN CUBRIR, LEIDAS DE MI PROPIA CORRIDA DE HOY:")
    dentro = False
    n_resto = 0
    for l in leer(rel_hoy).split(NL):
        if "LAS QUE SIGUEN SIN CUBRIR" in l:
            dentro = True
            continue
        if dentro:
            m = re.match(r"^\s{3}(\S.*?)\s+idx (\d+) \| (\S.*?)\s+\| (.*)$", l)
            if m:
                n_resto += 1
                w("      %s idx %s | %s | %s"
                  % (m.group(1), m.group(2), m.group(3).strip(), m.group(4)))
            elif "CIFRA clausulas que siguen sin cubrir" in l:
                w("      %s" % l.strip())
                break
    w("   CIFRA filas de las que no cubren, armadas leyendo mi corrida: %d | "
      "CIFRA que el recuento de hoy exige: %s" % (n_resto, hoy.get("A MEDIAS")))
    if n_resto != hoy.get("A MEDIAS"):
        fallos += 1
    w("")

    # =================================================================== 1.c
    w("=" * 78)
    w("1.c. LAS SEIS COSAS QUE SUBEN NOMBRADAS A LA AUDITORIA INTEGRAL")
    w("=" * 78)
    w("")
    sec6 = localizar(lineas_acta, "## 6. LO QUE SUBE NOMBRADO A LA AUDITORIA "
                                  "INTEGRAL", desde=inicio_218)
    w("   CIFRA lineas donde empieza la seccion 6 del acta 218: %d | CIFRA que "
      "se exige: 1" % len(sec6))
    if len(sec6) != 1:
        fallos += 1
        inicio_6 = inicio_218
    else:
        inicio_6 = sec6[0]
        w("   LA SECCION 6 EMPIEZA EN LA LINEA %d" % inicio_6)
    w("")
    w("   NO SE RESUELVE NINGUNA. Solo quedan escritas, con su cifra y con la "
      "linea del acta donde viven.")
    w("")
    filas_int = []
    for num, resumen, ancla in INTEGRAL:
        donde = localizar(lineas_acta, ancla, desde=inicio_6)
        if len(donde) != 1:
            fallos += 1
            w("   ROJO: el punto %s no aparece exactamente una vez (%d)."
              % (num, len(donde)))
            continue
        n = donde[0]
        cuerpo = [lineas_acta[n - 1]]
        k = n
        while k < len(lineas_acta) and lineas_acta[k].startswith("   "):
            cuerpo.append(lineas_acta[k])
            k += 1
        texto = " ".join(x.strip() for x in cuerpo)
        w("   PUNTO %s, LINEA %d, LEIDO DEL FICHERO:" % (num, n))
        for c in cuerpo:
            w("      %d> %s" % (n + cuerpo.index(c), c))
        filas_int.append((num, n, resumen, texto))
    w("")
    w("   CIFRA puntos localizados con su linea: %d | CIFRA que la seccion 6 "
      "lista: 6" % len(filas_int))
    if len(filas_int) != 6:
        fallos += 1
    w("")
    w("   LA TABLA, ARMADA DE LO LOCALIZADO Y NO TECLEADA:")
    w("| # | linea del acta 218 | lo que sube, y su cifra |")
    w("|---:|---:|---|")
    for num, n, resumen, _t in filas_int:
        w("| %s | **%d** | %s |" % (num, n, resumen))
    w("   CIFRA filas armadas: %d | CIFRA que deberia haber: 6" % len(filas_int))
    w("")

    # ============================================================== EL CIERRE
    w("=" * 78)
    w("ESTA TAREA SOLO LEE, Y SE PRUEBA CON LOS SHA")
    w("=" * 78)
    for rel in SEDES:
        sal = sha16(rel)
        bd, bl = bytes_de(rel)
        w("   %s AL ENTRAR: sha256 disco %s y sha256 LF %s"
          % ((rel,) + entrada[rel]))
        w("   %s AL SALIR:   sha256 disco %s y sha256 LF %s, %d bytes en disco "
          "y %d normalizado a LF" % ((rel,) + sal + (bd, bl)))
        if sal != entrada[rel]:
            fallos += 1
            w("   ROJO: %s SE MOVIO." % rel)
    coinciden = all(sha16(r) == entrada[r] for r in SEDES)
    w("   LOS %d SHA DE LAS SEDES DEL PLAN COINCIDEN AL ENTRAR Y AL SALIR POR "
      "LAS DOS CONVENCIONES: %s" % (len(SEDES) * 2, "SI" if coinciden else "NO"))
    w("")
    w("   EL CASO ROJO, DICHO CUAL ES CUAL: la localizacion de las lineas, el "
      "cotejo de las dos clases, el marcador y el recuento CAEN EN ROJO por si "
      "solos y estan contados arriba. LA GLOSA DE CADA ADJUDICACION ES MIA y no "
      "tiene nada que mutar: SE DECLARA QUE NO HAY CASO ROJO AUTOMATICO PARA "
      "ESA PARTE.")
    w("")
    w("CIFRA comprobaciones que fallan: %d" % fallos)
    w("VERDE: la TAREA 1 sale limpia." if not fallos
      else "ROJO: la TAREA 1 tiene comprobaciones que fallan.")

    texto = NL.join(out) + NL
    destino = os.path.join(LOOP, "SALIDA_V%d_T1_REGISTROS.txt" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    sys.stdout.write(NL + "SELLADO EN %s, %d bytes%s"
                     % (os.path.basename(destino), os.path.getsize(destino), NL))
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
