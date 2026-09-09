# -*- coding: utf-8 -*-
r"""_v214_t1c_evidencia.py . LA PRUEBA DEL CIERRE DE OP-I-01, ESCRITA EN LA SEDE
DE LA PROPIA FICHA POR CORRECCION DECLARADA.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO: fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3).

EL CARRIL ES EL QUE LA PROPIA FICHA YA USO, Y NO SE INVENTA NINGUNO: la
correccion se escribe como UN ELEMENTO MAS de la lista evidencia, que es la via
que esta misma ficha uso en la vuelta 201 y la ficha gemela OP-L-01 en la 166.
Banco 9.10, con el texto viejo entero y sin tachar.

LO QUE ESTE INSTRUMENTO NO HACE, Y ES LA MITAD QUE IMPORTA: NO ESCRIBE EL CAMPO
estado. La vara del trabajo pendiente es el instrumento y nunca el campo estado
(recuadro de AUDITOR.md 0, decision del fundador del 4 sep 2026). La ficha
recibe SU PRUEBA, no un veredicto tecleado.

CERO CIFRAS TECLEADAS: todas las cifras del texto nuevo se LEEN de las salidas
selladas de esta misma vuelta, y si una de esas rutas no existe o mide cero
bytes, el instrumento no escribe (EJECUTOR.md 1, LA RUTA QUE PROMETE PRUEBA ES
CIFRA).

USO:
  python scripts/loop/_v214_t1c_evidencia.py --simular
  python scripts/loop/_v214_t1c_evidencia.py --mutantes
  python scripts/loop/_v214_t1c_evidencia.py --escribir
"""
import io
import json
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_",
                       os.path.basename(os.path.abspath(__file__))).group(1))

OPS = "docs/plan/OPERACIONES.jsonl"
FICHA = "OP-I-01"
RUTA_DECISION = "docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md"
FECHA = "2026-09-09"

# LAS RUTAS QUE ESTE TEXTO VA A PROMETER COMO PRUEBA. SE COMPRUEBAN ANTES.
PRUEBAS = [
    "docs/loop/SALIDA_V214_T1_SIMULACION.txt",
    "docs/loop/SALIDA_V214_T1_MUTANTES.txt",
    "docs/loop/SALIDA_V214_T1_MARCAR_95.txt",
    "docs/loop/SALIDA_V214_T1C_OP_I_01.txt",
    "docs/loop/SALIDA_V214_T1_VARA.txt",
]

CONVENCIONES = ((", ", ": "), (",", ":"))


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8", newline="").read()


def convencion_de(linea, d):
    for sep in CONVENCIONES:
        if json.dumps(d, ensure_ascii=False, separators=sep) == linea:
            return sep
    return None


def cifra_de(texto, etiqueta):
    """UNA CIFRA LEIDA DE UNA SALIDA SELLADA, NO TECLEADA. Devuelve None si la
    etiqueta no esta, y eso es ROJO en el juicio. PURA."""
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(\d+)", l.split(etiqueta, 1)[1])
            if m:
                return m.group(1)
    return None


def sha_de(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"sha256 ([0-9a-f]{16})", l)
            if m:
                return m.group(1)
    return None


def datos_medidos():
    """TODAS LAS CIFRAS DEL TEXTO NUEVO, LEIDAS DE LAS SALIDAS SELLADAS."""
    marcar = leer("docs/loop/SALIDA_V214_T1_MARCAR_95.txt")
    puntos = leer("docs/loop/SALIDA_V214_T1C_OP_I_01.txt")
    mut = leer("docs/loop/SALIDA_V214_T1_MUTANTES.txt")
    partes = marcar.split("EL CONTEO DESPUES")
    antes, despues = partes[0], partes[1]
    d = {
        "entradas": cifra_de(despues, "CIFRA entradas del inventario:"),
        "con_forma": cifra_de(despues, "'N de M pares leidos': "),
        "incompletas": cifra_de(despues, "INCOMPLETAS (N menor que M): "),
        "marcadas_antes": cifra_de(antes, "incompletas con PROVISIONAL en su campo forma: "),
        "marcadas_despues": cifra_de(despues, "incompletas con PROVISIONAL en su campo forma: "),
        "sha_antes": sha_de(antes, "CIFRA bytes:"),
        "sha_despues": sha_de(despues, "CIFRA bytes:"),
        "bytes_antes": cifra_de(antes, "CIFRA bytes: "),
        "bytes_despues": cifra_de(despues, "CIFRA bytes: "),
        "mutantes": cifra_de(mut, "CIFRA mutantes "),
        "caen": cifra_de(mut, "CIFRA que caen "),
        "cubre": cifra_de(puntos, "   CUBRE      "),
        "amedias": cifra_de(puntos, "   A MEDIAS   "),
        "nocubre": cifra_de(puntos, "CIFRA puntos en NO CUBRE: "),
    }
    return d


def texto_nuevo(d):
    return (
        "CORRECCION DECLARADA (%s, vuelta %d, TAREA 1 del encargo), POR EL CARRIL "
        "DEL BANCO 9.10 Y CON EL TEXTO VIEJO ENTERO ARRIBA, SIN TACHARLO Y SIN "
        "CLAVE NUEVA DE ESQUEMA (es un elemento mas de esta misma lista evidencia, "
        "que es la via que esta ficha ya uso en la vuelta 201 y la ficha gemela "
        "OP-L-01 en la vuelta 166). "
        "QUIEN LO ORDENA, POR SU RUTA Y NO DE MEMORIA: %s, DECISION 1 del fundador. "
        "LO QUE SE ANADE ES LA PRUEBA DEL CIERRE DEL PUNTO 2 DE verificacion, que "
        "decia verbatim 'toda forma con cobertura incompleta va marcada "
        "PROVISIONAL' y que la vuelta 211 midio en NO CUBRE. "
        "LO EJECUTADO, MEDIDO Y NO PROMETIDO: las %s entradas de "
        "docs/plan/INVENTARIO.jsonl con cobertura de la forma N de M INCOMPLETA "
        "quedan marcadas PROVISIONAL en su campo forma, por instrumento "
        "(scripts/loop/_v214_t1_marcar_95.py) y nunca a mano. El conteo va ANTES y "
        "DESPUES sobre el mismo fichero: incompletas marcadas %s al entrar y %s al "
        "salir, sobre %s entradas totales y %s con forma N de M. El fichero pasa de "
        "%s a %s bytes y su sha256 de %s a %s. LA MARCA SE ANEXA Y NO SUSTITUYE: el "
        "texto viejo del campo forma queda entero y delante en las %s, y el campo "
        "cobertura NO se toca, porque la marca DICE la cobertura incompleta y no la "
        "COMPLETA (banco 9.26). "
        "LA GUARDA DEL ENCARGO SE CUMPLIO SIN AJUSTAR NADA: si el instrumento "
        "hubiera marcado un numero distinto de %s, la vuelta paraba. "
        "EL CASO ROJO NO SE PROMETE, SE PRUEBA POR MUTACION: %s mutantes y los %s "
        "caen, con el texto bueno pasando el mismo juicio en 0 fallos "
        "(docs/loop/SALIDA_V214_T1_MUTANTES.txt). "
        "LOS CUATRO PUNTOS RE-MEDIDOS HOY, en docs/loop/SALIDA_V214_T1C_OP_I_01.txt: "
        "%s en CUBRE, %s en A MEDIAS y %s en NO CUBRE; el punto 2 se mueve de NO "
        "CUBRE a CUBRE y es el unico que se mueve. "
        "Y LA DISCREPANCIA SE DECLARA EN VEZ DE TAPARSE: los puntos 3 y 4 SIGUEN EN "
        "A MEDIAS y esta vuelta no los mueve. El 3 porque su mitad pendiente es una "
        "NEGATIVA ('nunca rellenado') y una busqueda negativa no se puede citar; el "
        "4 porque su mitad pendiente es regenerar la vista humana, y "
        "docs/plan/10_INVENTARIO.md declara en su linea 19 que NO se regenera ahi A "
        "PROPOSITO. Ninguno de los dos es NO CUBRE y ninguno lo levanta el bucle por "
        "su cuenta: suben NOMBRADOS a la auditoria integral. "
        "NINGUN CAMPO estado SE MUEVE CON ESTA CORRECCION, ni en esta ficha ni en "
        "ninguna otra: la vara del trabajo pendiente es el instrumento y nunca el "
        "campo estado (recuadro de AUDITOR.md 0, decision del fundador del 4 sep "
        "2026). LO QUE ESTA CORRECCION NO HACE: no borra ni tacha ninguna cifra "
        "vieja, no toca ni un nodo, no mueve ni un veredicto, no regenera el "
        "inventario y no cambia las dependencias de ninguna ficha."
        % (FECHA, VUELTA, RUTA_DECISION,
           d["incompletas"], d["marcadas_antes"], d["marcadas_despues"],
           d["entradas"], d["con_forma"],
           d["bytes_antes"], d["bytes_despues"], d["sha_antes"], d["sha_despues"],
           d["incompletas"], d["incompletas"],
           d["mutantes"], d["caen"],
           d["cubre"], d["amedias"], d["nocubre"]))


def componer(crudo, d):
    partes = crudo.split(NL)
    nuevas = list(partes)
    tocada = None
    for i, linea in enumerate(partes):
        if not linea.strip():
            continue
        f = json.loads(linea)
        if f.get("id_op") != FICHA:
            continue
        sep = convencion_de(linea, f)
        if sep is None:
            return None, None
        f["evidencia"] = list(f["evidencia"]) + [texto_nuevo(d)]
        nuevas[i] = json.dumps(f, ensure_ascii=False, separators=sep)
        tocada = i + 1
    return NL.join(nuevas), tocada


def juzgar(antes, despues, d):
    L = []
    fallos = 0

    def chequeo(nombre, ok, glosa):
        nonlocal fallos
        L.append("   %-62s %s" % (nombre, "VERDE" if ok else "ROJO"))
        L.append("      %s" % glosa)
        if not ok:
            fallos += 1

    la, lb = antes.split(NL), despues.split(NL)
    A = [json.loads(l) for l in la if l.strip()]
    B = [json.loads(l) for l in lb if l.strip()]

    chequeo("el numero de fichas no se mueve", len(A) == len(B),
            "CIFRA fichas antes %d, despues %d" % (len(A), len(B)))
    if len(A) != len(B):
        return fallos, L

    dif = [i for i in range(len(la)) if la[i] != lb[i]]
    chequeo("cambia EXACTAMENTE una linea del expediente", len(dif) == 1,
            "CIFRA lineas que cambian: %d" % len(dif))
    if len(dif) != 1:
        return fallos, L

    j = sum(1 for l in la[:dif[0]] if l.strip())
    a, b = A[j], B[j]
    chequeo("la linea que cambia es la de %s" % FICHA,
            a.get("id_op") == FICHA and b.get("id_op") == FICHA,
            "id_op antes %r, despues %r" % (a.get("id_op"), b.get("id_op")))

    solo_ev = all(json.dumps(a[k], ensure_ascii=False)
                  == json.dumps(b.get(k), ensure_ascii=False)
                  for k in a if k != "evidencia") and set(a) == set(b)
    chequeo("de esa ficha, SOLO se mueve la lista evidencia", solo_ev,
            "ningun otro campo cambia, y no nace ninguna clave de esquema")

    chequeo("el campo estado NO se mueve en NINGUNA ficha del fichero",
            all(A[i].get("estado") == B[i].get("estado") for i in range(len(A))),
            "CIFRA fichas cuyo estado cambia: %d"
            % sum(1 for i in range(len(A)) if A[i].get("estado") != B[i].get("estado")))

    ev_a, ev_b = a["evidencia"], b["evidencia"]
    chequeo("la lista evidencia crece en EXACTAMENTE un elemento",
            len(ev_b) == len(ev_a) + 1,
            "CIFRA elementos antes %d, despues %d" % (len(ev_a), len(ev_b)))
    chequeo("los elementos viejos quedan ENTEROS y en su orden, sin tachar",
            ev_b[:len(ev_a)] == ev_a,
            "CIFRA elementos viejos identicos %d de %d"
            % (sum(1 for x, y in zip(ev_a, ev_b) if x == y), len(ev_a)))

    nuevo = ev_b[-1] if len(ev_b) > len(ev_a) else ""
    chequeo("el elemento nuevo cita el carril 9.10 y la decision POR SU RUTA",
            "9.10" in nuevo and RUTA_DECISION in nuevo,
            "las dos citas presentes: %s"
            % ("SI" if ("9.10" in nuevo and RUTA_DECISION in nuevo) else "NO"))
    chequeo("el elemento nuevo dice que NINGUN campo estado se mueve",
            "NINGUN CAMPO estado SE MUEVE" in nuevo,
            "la clausula esta escrita: %s"
            % ("SI" if "NINGUN CAMPO estado SE MUEVE" in nuevo else "NO"))

    faltan = [k for k, v in d.items() if v is None]
    chequeo("TODAS las cifras del texto salen de una salida sellada",
            not faltan,
            "CIFRA cifras que no se pudieron leer de su fichero: %d %s"
            % (len(faltan), faltan if faltan else ""))

    huecos = re.findall(r"\bNone\b", nuevo)
    chequeo("el texto nuevo no publica ningun None", not huecos,
            "CIFRA apariciones de None en el texto nuevo: %d" % len(huecos))

    malas = []
    for r in PRUEBAS:
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        if not os.path.isfile(p) or os.path.getsize(p) == 0:
            malas.append(r)
    chequeo("las rutas que el texto promete como prueba EXISTEN y no son de 0 bytes",
            not malas,
            "CIFRA rutas inexistentes o vacias: %d %s" % (len(malas), malas))

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
    w("VUELTA %d, TAREA 1.c. LA PRUEBA DEL CIERRE DE %s, EN SU PROPIA SEDE. MODO %s"
      % (VUELTA, FICHA, modo))
    w("=" * 78)
    w("EL CARRIL: banco 9.10, un elemento mas de la lista evidencia, como ya hizo")
    w("esta misma ficha en la vuelta 201. NO SE ESCRIBE EL CAMPO estado.")
    w("")

    w("LAS RUTAS QUE EL TEXTO VA A PROMETER COMO PRUEBA, COMPROBADAS ANTES:")
    for r in PRUEBAS:
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        w("   %-52s existe %s | %s bytes"
          % (r, "SI" if os.path.isfile(p) else "NO",
             os.path.getsize(p) if os.path.isfile(p) else 0))
    w("")

    d = datos_medidos()
    w("LAS CIFRAS DEL TEXTO NUEVO, LEIDAS DE SUS SALIDAS Y NO TECLEADAS:")
    for k in sorted(d):
        w("   %-18s %s" % (k, d[k]))
    w("")

    crudo = leer(OPS)
    nuevo, linea = componer(crudo, d)
    if nuevo is None:
        w("ROJO: la linea de la ficha no vuelve a su propio texto al re-volcarla.")
        sys.stdout.write(NL.join(out) + NL)
        return 1
    w("LA FICHA VIVE EN LA LINEA %d de %s" % (linea, OPS))
    w("")
    w("EL TEXTO NUEVO, ENTERO, PARA QUE SE PUEDA LEER SIN ABRIR EL JSONL:")
    for trozo in re.findall(r".{1,76}(?:\s|$)", texto_nuevo(d)):
        w("   " + trozo.rstrip())
    w("")

    w("EL JUICIO ENTERO:")
    fallos, L = juzgar(crudo, nuevo, d)
    out.extend(L)
    w("   CIFRA comprobaciones que fallan: %d" % fallos)
    w("")

    if modo == "--mutantes":
        w("=" * 78)
        w("LA PRUEBA DE MUTACION DEL JUICIO. CADA MUTANTE ES EL TEXTO BUENO CON UN")
        w("DANO Y EL JUICIO TIENE QUE CAER EN TODOS.")
        w("=" * 78)
        lineas_b = nuevo.split(NL)
        idx = linea - 1

        def mutar(cambio, otra=None):
            copia = list(lineas_b)
            i = otra if otra is not None else idx
            f = json.loads(copia[i])
            sep = convencion_de(copia[i], f)
            cambio(f)
            copia[i] = json.dumps(f, ensure_ascii=False, separators=sep)
            return NL.join(copia)

        def mueve_estado(f):
            f["estado"] = "HECHA"

        def tapa_viejo(f):
            f["evidencia"] = [f["evidencia"][-1]]

        def sin_cita(f):
            f["evidencia"][-1] = f["evidencia"][-1].replace(RUTA_DECISION, "por ahi")

        def sin_clausula(f):
            f["evidencia"][-1] = f["evidencia"][-1].replace(
                "NINGUN CAMPO estado SE MUEVE", "el estado se movio")

        def otro_campo(f):
            f["nota"] = (f.get("nota") or "") + " tocado"

        otra_linea = None
        for i, l in enumerate(lineas_b):
            if l.strip() and json.loads(l).get("id_op") != FICHA:
                otra_linea = i
                break

        mutantes = [
            ("A. el campo estado se mueve a HECHA", mueve_estado, None),
            ("B. la evidencia vieja se tapa en vez de conservarse", tapa_viejo, None),
            ("C. el texto nuevo no cita la decision por su ruta", sin_cita, None),
            ("D. el texto nuevo deja de decir que el estado no se mueve",
             sin_clausula, None),
            ("E. se mueve un campo que no es evidencia", otro_campo, None),
            ("F. se toca ademas una ficha que no es la suya", otro_campo, otra_linea),
        ]
        caen = 0
        for nombre, cambio, otra in mutantes:
            f, ll = juzgar(crudo, mutar(cambio, otra), d)
            rotas = [x.strip() for x in ll if x.strip().endswith("ROJO")]
            w("   MUTANTE %-56s fallos %d -> %s"
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
        io.open(os.path.join(RAIZ, OPS.replace("/", os.sep)), "w",
                encoding="utf-8", newline="").write(nuevo)
        de_nuevo = leer(OPS)
        w("ESCRITO %s" % OPS)
        w("   RELECTURA DEL DISCO identica a lo juzgado: %s"
          % ("SI" if de_nuevo == nuevo else "NO"))
        f2, l2 = juzgar(crudo, de_nuevo, d)
        w("EL JUICIO OTRA VEZ, YA CONTRA EL DISCO:")
        out.extend(l2)
        w("   CIFRA comprobaciones que fallan sobre el disco: %d" % f2)
        w("")
        w("VERDE: la ficha tiene su prueba." if (f2 == 0 and de_nuevo == nuevo)
          else "ROJO: lo escrito no es lo juzgado.")
        sys.stdout.write(NL.join(out) + NL)
        return 0 if (f2 == 0 and de_nuevo == nuevo) else 1

    w("SIMULACION: NO SE ESCRIBE NADA.")
    sys.stdout.write(NL.join(out) + NL)
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
