# -*- coding: utf-8 -*-
r"""_v214_t2_vara_tres_fases.py . LA TAREA 2.a DE LA VUELTA 214: LA TABLA DEL
CRITERIO DE HECHO DE docs/plan/08_VERIFICACION.md GANA SUS FILAS PARA LAS FASES
08, 09 Y 10.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO: fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3).

QUIEN LO ORDENA: docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md,
DECISION 2 del fundador.

LAS FILAS NO SE INVENTAN: SE DERIVAN. Cada celda se COMPONE de los textos
VERBATIM de las clausulas de verificacion que las propias fichas traen, leidas
hoy de docs/plan/OPERACIONES.jsonl, y cada fila lleva su cita (ficha, indice de
la clausula y linea del fichero). Si una celda contuviera una palabra que no
salga de una clausula, el juicio cae.

LAS CORRECCIONES DECLARADAS NO SON PUNTOS DE LA VARA, y eso no lo decide este
instrumento: lo adjudico el acta 208 en su registro R.72, que separo las tres
clausulas de los indices 0 a 2 de las CUATRO CORRECCIONES DECLARADAS de los
indices 3 a 6, que NUNCA FUERON PUNTOS DE LA VARA. Aqui se detectan por su
propio encabezado y se dicen aparte, con la clausula que cada una corrige
EXTRAIDA de su propio texto y no supuesta.

LA ESCRITURA ES ADITIVA Y NO TOCA UNA LETRA DE LA TABLA VIEJA: las tres filas se
anaden detras de la ultima, y el bloque de derivacion va detras del bloque de
correccion que la vuelta 122 ya dejo ahi. Banco 9.10.

USO:
  python scripts/loop/_v214_t2_vara_tres_fases.py --simular
  python scripts/loop/_v214_t2_vara_tres_fases.py --mutantes
  python scripts/loop/_v214_t2_vara_tres_fases.py --escribir
"""
import hashlib
import io
import json
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_",
                       os.path.basename(os.path.abspath(__file__))).group(1))

VER = "docs/plan/08_VERIFICACION.md"
OPS = "docs/plan/OPERACIONES.jsonl"
RUTA_DECISION = "docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md"
FECHA = "2026-09-09"

ANCLA_ULTIMA_FILA = "| **07 ADUANA** |"
ANCLA_FIN_BLOQUE = "## LA VERIFICACION TRANSVERSAL, y su orden importa"

# LAS TRES FASES QUE HOY NO TIENEN FILA, CON LA FICHA DE CADA UNA. El nombre de
# la fase se lee del campo `fase` de la propia ficha, no se teclea.
FASES = [
    ("08", ["OP-V-01"]),
    ("09", ["OP-L-01", "OP-L-02", "OP-L-03"]),
    ("10", ["OP-I-01"]),
]


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read()


def sha(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()[:16]


def fichas():
    """LAS FICHAS Y LA LINEA EN QUE VIVE CADA UNA. PURA salvo la lectura."""
    out = {}
    for i, l in enumerate(leer(OPS).split(NL), 1):
        if not l.strip():
            continue
        d = json.loads(l)
        out[d["id_op"]] = (d, i)
    return out


def es_correccion(c):
    return c.strip().upper().startswith("CORRECCION DECLARADA")


def corrige_a(c):
    """QUE CLAUSULA CORRIGE UNA CORRECCION DECLARADA, EXTRAIDO DE SU PROPIO
    TEXTO Y NO SUPUESTO. Devuelve el verbatim o None. PURA."""
    m = re.search(r"LO QUE SE CORRIGE es la clausula que en esta lista dice, "
                  r"verbatim: '(.+?)'", c)
    return m.group(1) if m else None


def partir(ficha):
    """(clausulas de vara, correcciones declaradas). PURA."""
    v = ficha["verificacion"]
    return ([c.strip() for c in v if not es_correccion(c)],
            [c for c in v if es_correccion(c)])


CABECERA_TABLA = "| fase | que tiene que dar verde |"


def filas_de_la_tabla(texto):
    """LAS FILAS DE LA TABLA DEL CRITERIO DE HECHO, Y SOLO DE ESA. PURA.

    ACOTAR IMPORTA Y SE MIDIO EN ESTA MISMA VUELTA: este fichero tiene muchas
    tablas, y un barrido por todo el texto se tragaba numeros de otras (707,
    1096, 2464 y mas) como si fueran fases. No cambiaba el resultado, porque el
    8, el 9 y el 10 no estaban entre ellos, pero una vara que acierta por suerte
    no es una vara. El corte va de la cabecera de la tabla a la primera linea
    que ya no empieza por tuberia."""
    lineas = texto.split(NL)
    ini = [i for i, l in enumerate(lineas) if l.strip() == CABECERA_TABLA]
    if len(ini) != 1:
        return None
    i = ini[0] + 2
    filas = []
    while i < len(lineas) and lineas[i].startswith("|"):
        filas.append(lineas[i])
        i += 1
    return filas


def numeros_con_fila(texto):
    """LOS NUMEROS DE FASE QUE LA TABLA DEL CRITERIO YA TIENE. PURA."""
    filas = filas_de_la_tabla(texto)
    if filas is None:
        return None
    ns = []
    for l in filas:
        m = re.match(r"^\| \*\*(\d+)\b", l)
        if m:
            ns.append(int(m.group(1)))
    return ns


def numero_de_clausula(c):
    """EL NUMERO DE FASE CON QUE ABRE UNA CLAUSULA, O None SI NO ABRE CON UNO.
    PURA. Reconoce las dos formas que las fichas usan de verdad: 'FASE 0:' y
    '01 FUENTES:'. Una clausula sin numero (TRANSVERSAL, o las de las fichas de
    lectura y de inventario) devuelve None y NO se excluye."""
    m = re.match(r"^(?:FASE\s+)?(\d+)\s+[A-Za-z]|^FASE\s+(\d+)\s*:", c.strip())
    if not m:
        return None
    return int(m.group(1) or m.group(2))


def derivar():
    """LAS TRES FILAS, DERIVADAS DE LAS CLAUSULAS. Devuelve (filas, derivacion,
    informe). Ninguna palabra de una celda se teclea aqui."""
    F = fichas()
    ya_tienen = numeros_con_fila(leer(VER))
    if ya_tienen is None:
        raise SystemExit("ROJO: la cabecera de la tabla del criterio no aparece "
                         "exactamente una vez. NO SE ADIVINA donde esta la tabla.")
    filas = []
    derivacion = []
    informe = []
    informe.append("   NUMEROS DE FASE QUE LA TABLA VIEJA YA TIENE, LEIDOS DE ELLA: "
                   "%s" % ya_tienen)
    informe.append("   LA REGLA DE EXCLUSION, MECANICA Y SIN OJO: una clausula que")
    informe.append("   ABRE CON EL NUMERO DE UNA FASE QUE YA TIENE FILA no es la vara")
    informe.append("   de SU fase: es la ficha repitiendo una fila que ya existe. Se")
    informe.append("   excluye y se dice. Una clausula SIN numero no se excluye.")
    for num, ids in FASES:
        nombre = None
        piezas = []
        origen = []
        for fid in ids:
            d, linea = F[fid]
            nombre = d["fase"]
            vara, corr = partir(d)
            usadas = 0
            excluidas = 0
            for idx, c in enumerate(d["verificacion"]):
                cs = c.strip()
                if es_correccion(c):
                    continue
                n_cl = numero_de_clausula(cs)
                if n_cl is not None and n_cl in ya_tienen:
                    excluidas += 1
                    informe.append("      %s indice %d EXCLUIDA: abre con la fase %d, "
                                   "que ya tiene fila" % (fid, idx, n_cl))
                    continue
                usadas += 1
                corregida_por = [j for j, x in enumerate(d["verificacion"])
                                 if es_correccion(x) and corrige_a(x) == cs]
                origen.append((fid, idx, linea, cs, corregida_por))
                if cs not in piezas:
                    piezas.append(cs)
            informe.append("   %s (%s): %d clausula(s) de vara, %d correccion(es) "
                           "declarada(s), %d EXCLUIDA(s) por tener fila ya, %d "
                           "USADA(s), linea %d"
                           % (fid, d["fase"], len(vara), len(corr), excluidas,
                              usadas, linea))
        etiqueta = "%s %s" % (num, nombre.split("_", 1)[1].replace("_", " "))
        filas.append((etiqueta, "; ".join(piezas), piezas))
        derivacion.append((etiqueta, origen))
    return filas, derivacion, informe


def bloque_nuevo(filas, derivacion):
    """EL TEXTO QUE SE ANADE DEBAJO DE LA TABLA. Las citas salen de derivar()."""
    L = []
    L.append("")
    L.append("**CORRECCION DECLARADA (vuelta %d, %s, ADITIVA: LA TABLA VIEJA NO SE "
             "TOCA NI EN UNA LETRA). LAS TRES FILAS QUE FALTABAN, PARA LAS FASES "
             "08, 09 y 10.**" % (VUELTA, FECHA))
    L.append("")
    L.append("**QUIEN LO ORDENA, POR SU RUTA Y NO DE MEMORIA:** `%s`, **DECISION 2** "
             "del fundador. **El acta 211 ya habia reservado estas filas al fundador "
             "en su `6.4`, y el acta 213 midio en su `7.2` que la ausencia era TOTAL "
             "y no parcial: la tabla llevaba SIETE filas, de `01 FUENTES` a `07 "
             "ADUANA`, y CERO para estas tres.**" % RUTA_DECISION)
    L.append("")
    L.append("**LAS FILAS NO SE INVENTAN, SE DERIVAN, Y CADA UNA VA CON SU CITA.** "
             "Cada celda se compone de los textos **VERBATIM** de las clausulas de "
             "`verificacion` que las propias fichas traen, leidas hoy de "
             "`%s`. **Ninguna palabra de esas celdas la escribio esta vuelta:** las "
             "compuso `scripts/loop/_v%d_t2_vara_tres_fases.py` concatenando "
             "clausulas, y su juicio cae si una celda trae texto que no salga de "
             "una." % (OPS, VUELTA))
    L.append("")
    L.append("**Y LAS CORRECCIONES DECLARADAS NO ENTRAN, PORQUE NUNCA FUERON PUNTOS "
             "DE LA VARA:** lo adjudico el registro `R.72` del acta 208, que separo "
             "las tres clausulas de los indices 0 a 2 de las cuatro correcciones "
             "declaradas de los indices 3 a 6. **Aqui se detectan por su propio "
             "encabezado y se listan aparte**, con la clausula que cada una corrige "
             "**extraida de su propio texto** y no supuesta.")
    L.append("")
    L.append("| fase | de que ficha sale | indice de la clausula | linea de `%s` | la clausula, VERBATIM | corregida por |"
             % OPS)
    L.append("|---|---|---:|---:|---|---|")
    n = 0
    for etiqueta, origen in derivacion:
        for fid, idx, linea, cs, corregida in origen:
            n += 1
            L.append("| **%s** | `%s` | %d | %d | %s | %s |"
                     % (etiqueta, fid, idx, linea, cs,
                        ("indice %s" % ", ".join(str(x) for x in corregida))
                        if corregida else "no"))
    L.append("")
    L.append("**FILAS DE DERIVACION ARMADAS: %d.** Cada una es una clausula de vara "
             "de una de las cinco fichas, y las celdas de arriba son su "
             "concatenacion." % n)
    L.append("")
    L.append("**LO QUE ESTA CORRECCION NO HACE:** no borra ni tacha ninguna fila "
             "vieja, no toca el campo `estado` de ninguna ficha, no mueve ni un "
             "veredicto, no toca ni un nodo y no cambia el disparador del recomputo.")
    L.append("")
    return NL.join(L)


def componer():
    txt = leer(VER)
    filas, derivacion, informe = derivar()
    lineas = txt.split(NL)
    idx_ultima = [i for i, l in enumerate(lineas) if l.startswith(ANCLA_ULTIMA_FILA)]
    if len(idx_ultima) != 1:
        return None, None, None, None, informe + [
            "ROJO: el ancla de la ultima fila aparece %d veces" % len(idx_ultima)]
    i = idx_ultima[0]
    nuevas_filas = ["| **%s** | %s |" % (e, celda) for e, celda, _ in filas]
    idx_fin = [j for j, l in enumerate(lineas) if l.startswith(ANCLA_FIN_BLOQUE)]
    if len(idx_fin) != 1:
        return None, None, None, None, informe + [
            "ROJO: el ancla de fin de bloque aparece %d veces" % len(idx_fin)]
    j = idx_fin[0]
    # el bloque nuevo va DETRAS de la correccion de la vuelta 122 y DELANTE del
    # separador que precede a la seccion siguiente
    corte = j
    while corte > 0 and lineas[corte - 1].strip() in ("", "---"):
        corte -= 1
    salida = (lineas[:i + 1] + nuevas_filas + lineas[i + 1:corte]
              + bloque_nuevo(filas, derivacion).split(NL) + lineas[corte:])
    return NL.join(salida), filas, derivacion, nuevas_filas, informe


def juzgar(antes, despues, filas, nuevas_filas):
    L = []
    fallos = 0

    def chequeo(nombre, ok, glosa):
        nonlocal fallos
        L.append("   %-64s %s" % (nombre, "VERDE" if ok else "ROJO"))
        L.append("      %s" % glosa)
        if not ok:
            fallos += 1

    la, lb = antes.split(NL), despues.split(NL)

    viejas = [l for l in (filas_de_la_tabla(antes) or [])
              if re.match(r"^\| \*\*\d", l)]
    siguen = [l for l in viejas if l in lb]
    chequeo("las filas viejas de la tabla siguen ENTERAS y sin tocar",
            len(siguen) == len(viejas),
            "CIFRA filas viejas %d, de ellas intactas %d" % (len(viejas), len(siguen)))

    chequeo("no se borra NI UNA linea del fichero",
            all(l in lb for l in la) or len([l for l in la if l not in lb]) == 0,
            "CIFRA lineas viejas que ya no estan: %d"
            % len([l for l in la if l not in lb]))

    nuevas_en = [f for f in nuevas_filas if f in lb]
    chequeo("las TRES filas nuevas estan escritas",
            len(nuevas_en) == 3 and len(nuevas_filas) == 3,
            "CIFRA filas nuevas compuestas %d, presentes en el texto %d"
            % (len(nuevas_filas), len(nuevas_en)))

    # LA GUARDA QUE IMPORTA: NINGUNA CELDA TRAE TEXTO QUE NO SALGA DE UNA CLAUSULA
    inventado = []
    for etiqueta, celda, piezas in filas:
        resto = celda
        for p in piezas:
            resto = resto.replace(p, "", 1)
        resto = resto.replace(";", "").strip()
        if resto:
            inventado.append((etiqueta, resto[:80]))
    chequeo("ninguna celda nueva trae UNA PALABRA que no salga de una clausula",
            not inventado,
            "CIFRA celdas con texto inventado: %d %s" % (len(inventado), inventado))

    tuberias = [e for e, c, _ in filas if "|" in c]
    chequeo("ninguna clausula trae una tuberia que rompa la tabla",
            not tuberias, "CIFRA celdas con tuberia: %d" % len(tuberias))

    etiquetas = [e for e, _, _ in filas]
    chequeo("las tres filas son de las fases 08, 09 y 10",
            [e.split()[0] for e in etiquetas] == ["08", "09", "10"],
            "etiquetas compuestas: %s" % etiquetas)

    ya_habia = [e for e in etiquetas
                if any(l.startswith("| **%s" % e.split()[0]) for l in viejas)]
    chequeo("ninguna de las tres fases tenia fila ya",
            not ya_habia, "CIFRA fases que ya tenian fila: %d %s"
            % (len(ya_habia), ya_habia))

    chequeo("el bloque nuevo cita la decision POR SU RUTA",
            RUTA_DECISION in despues and RUTA_DECISION not in antes,
            "la ruta aparece en el texto nuevo y no estaba antes")

    chequeo("el fichero crece y no encoge",
            len(despues) > len(antes),
            "CIFRA caracteres antes %d, despues %d" % (len(antes), len(despues)))

    largos = despues.count(chr(8212)) + despues.count(chr(8211))
    chequeo("cero guiones largos y cero guiones medios", largos == 0,
            "CIFRA guiones largos mas medios: %d" % largos)
    return fallos, L


def main():
    modo = sys.argv[1] if len(sys.argv) > 1 else "--simular"
    out = []

    def w(s=""):
        out.append(s)

    w("=" * 78)
    w("VUELTA %d, TAREA 2.a. LA VARA DE LAS TRES FASES. MODO %s" % (VUELTA, modo))
    w("=" * 78)
    w("QUIEN LO ORDENA: %s, DECISION 2" % RUTA_DECISION)
    w("LAS FILAS SE DERIVAN DE LAS CLAUSULAS DE LAS FICHAS, NO SE INVENTAN.")
    w("")

    antes = leer(VER)
    sha_ops_0 = sha(leer(OPS))
    w("CIFRA %s AL ENTRAR: %d bytes, sha256 %s"
      % (VER, len(antes.encode("utf-8")), sha(antes)))
    w("CIFRA %s AL ENTRAR: sha256 %s (este fichero NO se toca en la 2.a)"
      % (OPS, sha_ops_0))
    w("")

    despues, filas, derivacion, nuevas_filas, informe = componer()
    w("LAS CINCO FICHAS, CON SUS CLAUSULAS SEPARADAS DE SUS CORRECCIONES:")
    for l in informe:
        w(l)
    w("")
    if despues is None:
        w("ROJO: no se pudo componer.")
        sys.stdout.write(NL.join(out) + NL)
        return 1

    w("LA TABLA VIEJA, CONTADA DEL FICHERO ANTES DE TOCARLO:")
    viejas = [l for l in (filas_de_la_tabla(antes) or [])
              if re.match(r"^\| \*\*\d", l)]
    w("   CIFRA filas de fase que ya tenia: %d" % len(viejas))
    for l in viejas:
        w("      %s" % l[:96])
    w("")

    w("LAS TRES FILAS NUEVAS, ENTERAS:")
    for f in nuevas_filas:
        w("   %s" % f)
    w("")

    w("EL JUICIO ENTERO:")
    fallos, L = juzgar(antes, despues, filas, nuevas_filas)
    out.extend(L)
    w("   CIFRA comprobaciones que fallan: %d" % fallos)
    w("")

    if modo == "--mutantes":
        w("=" * 78)
        w("LA PRUEBA DE MUTACION DEL JUICIO. CADA MUTANTE TIENE QUE CAER.")
        w("=" * 78)
        mutantes = []

        m1 = despues.replace(viejas[0], "| **01 FUENTES** | reescrita |", 1)
        mutantes.append(("A. una fila vieja se reescribe", m1, filas, nuevas_filas))

        m2 = despues.replace(nuevas_filas[2], "", 1)
        mutantes.append(("B. falta una de las tres filas nuevas", m2, filas,
                         nuevas_filas))

        f3 = [(e, c + "; y ademas todo lo que a uno le parezca", p)
              for e, c, p in filas]
        m3 = despues.replace(nuevas_filas[0],
                             "| **%s** | %s |" % (f3[0][0], f3[0][1]), 1)
        mutantes.append(("C. una celda trae texto que no sale de ninguna clausula",
                         m3, f3, nuevas_filas))

        m4 = despues.replace(RUTA_DECISION, "una ruta cualquiera")
        mutantes.append(("D. el bloque nuevo no cita la decision por su ruta",
                         m4, filas, nuevas_filas))

        m5 = NL.join(l for l in despues.split(NL) if l != viejas[3])
        mutantes.append(("E. se borra una linea vieja del fichero", m5, filas,
                         nuevas_filas))

        caen = 0
        for nombre, texto, ff, nf in mutantes:
            f, ll = juzgar(antes, texto, ff, nf)
            rotas = [x.strip() for x in ll if x.strip().endswith("ROJO")]
            w("   MUTANTE %-58s fallos %d -> %s"
              % (nombre, f, "CAE, como debe" if f > 0 else "PASA, Y ESO ES ROJO"))
            for r in rotas:
                w("      cae por> %s" % r)
            if f > 0:
                caen += 1
        w("   CIFRA mutantes %d | CIFRA que caen %d | se exigen %d"
          % (len(mutantes), caen, len(mutantes)))
        w("   EL CASO POSITIVO: el texto bueno sin mutar da %d fallos." % fallos)
        w("")
        sys.stdout.write(NL.join(out) + NL)
        return 0 if (caen == len(mutantes) and fallos == 0) else 1

    if modo == "--escribir":
        if fallos:
            w("ROJO: el juicio no da cero. NO SE ESCRIBE.")
            sys.stdout.write(NL.join(out) + NL)
            return 1
        io.open(os.path.join(RAIZ, VER.replace("/", os.sep)), "w",
                encoding="utf-8", newline=NL).write(despues)
        de_nuevo = leer(VER)
        w("ESCRITO %s -> %d bytes, sha256 %s"
          % (VER, len(de_nuevo.encode("utf-8")), sha(de_nuevo)))
        w("   RELECTURA DEL DISCO identica a lo juzgado: %s"
          % ("SI" if de_nuevo == despues else "NO"))
        w("CIFRA %s AL SALIR: sha256 %s | QUIETO: %s"
          % (OPS, sha(leer(OPS)),
             "SI" if sha(leer(OPS)) == sha_ops_0 else "NO, ROJO"))
        f2, l2 = juzgar(antes, de_nuevo, filas, nuevas_filas)
        w("EL JUICIO OTRA VEZ, YA CONTRA EL DISCO:")
        out.extend(l2)
        w("   CIFRA comprobaciones que fallan sobre el disco: %d" % f2)
        w("")
        ok = (f2 == 0 and de_nuevo == despues and sha(leer(OPS)) == sha_ops_0)
        w("VERDE: la vara de las tres fases esta escrita." if ok else "ROJO.")
        sys.stdout.write(NL.join(out) + NL)
        return 0 if ok else 1

    w("SIMULACION: NO SE ESCRIBE NADA.")
    sys.stdout.write(NL.join(out) + NL)
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
