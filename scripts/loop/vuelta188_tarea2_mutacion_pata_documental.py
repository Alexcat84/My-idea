# -*- coding: utf-8 -*-
r"""vuelta188_tarea2_mutacion_pata_documental.py . EL CASO POSITIVO POR MUTACION
DE LA CUARTA PRUEBA DE LA VARA DEL EXPEDIENTE, LA DOCUMENTAL.

QUIEN LA ENCARGA. El acta 188, punto 12, con estas palabras: *"SUS TRES PRUEBAS
SON DE GRAFO, Y UNA `MESA` NO DEJA HUELLA EN EL GRAFO: PRODUCE DOCUMENTOS.
Preguntarle al grafo si una mesa se hizo es preguntarle a la fuente equivocada"*.
Y el encargo de la vuelta 188, TAREA 2, punto 3: *"para las que no son `MESA`
sigue exactamente igual, sin aflojar nada; para las `MESA` anade una cuarta
prueba, DOCUMENTAL"*.

QUE PRUEBA, CASO A CASO, Y TODOS TIENEN QUE CAER AL MUTAR SU ESPERADO:

  (A) LA P4 NO EXISTE PARA UNA FICHA QUE NO ES `MESA`. Ni con lista vacia: la
      ficha NO APARECE en el diccionario. Es la prueba mas fuerte de que la
      cuarta prueba no puede aflojar nada fuera de su tipo, y es de FORMA, no de
      cifra.

  (B) UNA `MESA` CUYA EVIDENCIA NOMBRA UN FICHERO QUE EXISTE SALE CON SU
      MEDICION, y la medicion es la del disco de verdad, por LAS DOS
      CONVENCIONES.

  (C) UNA `MESA` CUYA EVIDENCIA NOMBRA UN FICHERO QUE NO EXISTE SALE VACIA.
      **La P4 no inventa un documento que no esta**, que es justo lo contrario
      del afloje que se le podria acusar.

  (D) UNA `MESA` CUYA EVIDENCIA ES PROSA ENTERA (ningun nombre de fichero) SALE
      VACIA Y SE DISTINGUE DE LA ANTERIOR: son dos cosas distintas y las dos se
      dicen. `rutas_de_la_evidencia()` es PURA y devuelve las menciones, asi que
      la diferencia entre "no nombra ninguno" y "nombra uno que no esta" es
      medible sin tocar disco.

  (E) EL EXTRACTOR DE NOMBRES NO TRAGA CUALQUIER COSA: coge `.md`, `.jsonl`,
      `.json`, `.txt` y `.py`, y NO coge prosa con puntos ni versiones.

LO QUE ESTE ARNES NO HACE: no corre la vara entera como proceso, no toca
`docs/plan/OPERACIONES.jsonl` y no escribe ningun veredicto. Llama a las
funciones PURAS del fichero vivo con fichas fabricadas en memoria y, para el
unico caso que toca disco, con un directorio temporal propio que limpia al
salir (`P.16`, quien fabrica limpia).

Y PUBLICA EL `sha256` DE SU SUJETO AL LADO DE TODO NUMERO DE LINEA (vuelta 188,
TAREA 3.b; respuesta del acta 188 a la `P.2`): una salida que publica numeros de
linea de un fichero vivo envejece sola, y con el `sha256` del sujeto al lado un
diff futuro dice SI SE MOVIO EL SUJETO O SE MOVIO EL ARNES.

USO:
  python scripts/loop/vuelta188_tarea2_mutacion_pata_documental.py
"""
import hashlib
import io
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta150_3_relectura_expediente as VARA   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
SUJETO = "scripts/loop/vuelta150_3_relectura_expediente.py"


def sello_del_sujeto(rel):
    """EL `sha256` Y LOS BYTES DEL FICHERO QUE ESTE ARNES JUZGA. Sin el, un
    numero de linea publicado aqui envejece solo y nadie puede saber si se movio
    el sujeto o se movio el arnes."""
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    datos = io.open(p, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest())


def ficha(id_op, tipo, evidencia):
    """UNA FICHA DE MENTIRA. PURA: un diccionario y nada mas."""
    return {"id_op": id_op, "tipo": tipo, "fase": "09_LECTURAS_DIRIGIDAS",
            "estado": "LISTA", "evidencia": list(evidencia)}


def _caso_a(w):
    """A: la P4 no existe para una ficha que no es MESA."""
    fallos = casos = caen = 0
    w("CASO A. LA P4 NO EXISTE PARA UNA FICHA QUE NO ES `MESA`, Y ES DE FORMA")
    w("   (no sale con lista vacia: NO APARECE en el diccionario, que es la forma")
    w("    mas barata de que nadie la use por descuido en una ficha que no le toca)")
    F = [ficha("OP-X-01", "FUSION", ["LECTURAS_DIRIGIDAS.md, las once"]),
         ficha("OP-X-02", "DESTEJIDO", ["INVENTARIO.jsonl, 323 entradas"]),
         ficha("OP-X-03", "MESA", ["LECTURAS_DIRIGIDAS.md, las once"])]
    v4 = VARA.p4_vara_documental(F)
    casos += 1
    w("   fichas dadas: %s" % ", ".join("%s(%s)" % (f["id_op"], f["tipo"]) for f in F))
    w("   claves que devuelve p4_vara_documental(): %s" % sorted(v4))
    ok = (sorted(v4) == ["OP-X-03"])
    w("   ESPERADO solo la MESA -> %s" % ("CALZA" if ok else "NO CALZA"))
    if not ok:
        fallos += 1
    w("   MUTACION del esperado (exigir que la FUSION tambien este): %s"
      % ("PASA" if "OP-X-01" in v4 else "CAE"))
    if "OP-X-01" in v4:
        fallos += 1
    else:
        caen += 1
    w("   Y CON CERO MESAS, PARA QUE SE VEA QUE NO ESTA CLAVADO:")
    v4b = VARA.p4_vara_documental([f for f in F if f["tipo"] != "MESA"])
    casos += 1
    w("      claves: %s | ESPERADO ninguna -> %s"
      % (sorted(v4b), "CALZA" if not v4b else "NO CALZA"))
    if v4b:
        fallos += 1
    w("      MUTACION del esperado (exigir una clave): %s"
      % ("PASA" if len(v4b) == 1 else "CAE"))
    if len(v4b) == 1:
        fallos += 1
    else:
        caen += 1
    w("")
    return fallos, casos, caen


def _casos_bcd(w):
    """B, C y D: existe, no existe, y prosa entera. El unico que toca disco va
    contra un directorio temporal propio."""
    fallos = casos = caen = 0
    tmp = tempfile.mkdtemp(prefix="v188_pata_")
    try:
        os.makedirs(os.path.join(tmp, "docs", "plan"))
        contenido = b"una linea\r\notra linea\r\n"
        io.open(os.path.join(tmp, "docs", "plan", "EXISTE.md"), "wb").write(contenido)
        esperado_disco = len(contenido)
        esperado_lf = len(contenido.replace(b"\r\n", b"\n"))

        w("CASO B. UNA `MESA` CUYA EVIDENCIA NOMBRA UN FICHERO QUE EXISTE")
        w("   (el fichero se fabrica en un temporal propio, con CRLF a proposito para")
        w("    que las dos convenciones NO sean el mismo numero, y se limpia al salir)")
        F = [ficha("OP-M-01", "MESA", ["EXISTE.md, con su razon"])]
        v4 = VARA.p4_vara_documental(F, raiz=tmp)
        casos += 1
        w("   p4_vara_documental() -> %s" % (v4,))
        halladas = v4.get("OP-M-01") or []
        ok = (len(halladas) == 1
              and halladas[0][1] == "EXISTE.md"
              and halladas[0][2] == "docs/plan/EXISTE.md"
              and halladas[0][3] == esperado_disco
              and halladas[0][4] == esperado_lf)
        w("   ESPERADO 1 hallazgo en docs/plan/EXISTE.md con disco %d y LF %d -> %s"
          % (esperado_disco, esperado_lf, "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos += 1
        w("   LAS DOS CONVENCIONES SON DISTINTAS Y SE MIDEN LAS DOS: disco %s | LF %s"
          % (halladas[0][3] if halladas else "?", halladas[0][4] if halladas else "?"))
        w("   MUTACION del esperado (exigir disco %d): %s"
          % (esperado_disco + 1,
             "PASA" if halladas and halladas[0][3] == esperado_disco + 1 else "CAE"))
        if halladas and halladas[0][3] == esperado_disco + 1:
            fallos += 1
        else:
            caen += 1
        w("")

        w("CASO C. UNA `MESA` CUYA EVIDENCIA NOMBRA UN FICHERO QUE NO EXISTE")
        w("   LA P4 NO INVENTA UN DOCUMENTO QUE NO ESTA, que es lo contrario del")
        w("   afloje que se le podria acusar.")
        G = [ficha("OP-M-02", "MESA", ["NO_ESTA.md, con su razon"])]
        v4c = VARA.p4_vara_documental(G, raiz=tmp)
        casos += 1
        halladas_c = v4c.get("OP-M-02")
        menciones_c = VARA.rutas_de_la_evidencia(G[0])
        w("   p4_vara_documental() -> %s" % (v4c,))
        w("   menciones de fichero que su evidencia SI nombra: %d (%s)"
          % (len(menciones_c), ", ".join(n for _m, n in menciones_c)))
        ok_c = (halladas_c == [] and len(menciones_c) == 1)
        w("   ESPERADO lista vacia PERO con 1 mencion -> %s"
          % ("CALZA" if ok_c else "NO CALZA"))
        if not ok_c:
            fallos += 1
        w("   MUTACION del esperado (exigir 1 hallazgo): %s"
          % ("PASA" if halladas_c else "CAE"))
        if halladas_c:
            fallos += 1
        else:
            caen += 1
        w("")

        w("CASO D. UNA `MESA` CUYA EVIDENCIA ES PROSA ENTERA")
        w("   Sale vacia IGUAL QUE LA ANTERIOR, y aun asi son dos cosas distintas: una")
        w("   nombra un fichero que falta y la otra no nombra ninguno. Las dos se dicen.")
        H = [ficha("OP-M-03", "MESA",
                   ["MEDIDO el 11 ago 2026: 205 pares fuera de cola, 11 leidos"])]
        v4d = VARA.p4_vara_documental(H, raiz=tmp)
        casos += 1
        halladas_d = v4d.get("OP-M-03")
        menciones_d = VARA.rutas_de_la_evidencia(H[0])
        w("   p4_vara_documental() -> %s" % (v4d,))
        w("   menciones de fichero: %d" % len(menciones_d))
        ok_d = (halladas_d == [] and len(menciones_d) == 0)
        w("   ESPERADO lista vacia Y 0 menciones -> %s"
          % ("CALZA" if ok_d else "NO CALZA"))
        if not ok_d:
            fallos += 1
        w("   LA DIFERENCIA CON EL CASO C ES MEDIBLE SIN TOCAR DISCO: %d mencion(es)"
          % len(menciones_c))
        w("   contra %d, y `rutas_de_la_evidencia()` es PURA." % len(menciones_d))
        w("   MUTACION del esperado (exigir 1 mencion en la de prosa): %s"
          % ("PASA" if len(menciones_d) == 1 else "CAE"))
        if len(menciones_d) == 1:
            fallos += 1
        else:
            caen += 1
        w("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        w("   TEMPORAL LIMPIADO (P.16, quien fabrica limpia): %s -> existe: %s"
          % (tmp, "SI" if os.path.exists(tmp) else "NO"))
        w("")
    return fallos, casos, caen


def _caso_e(w):
    """E: el extractor de nombres no traga cualquier cosa."""
    fallos = casos = caen = 0
    w("CASO E. EL EXTRACTOR DE NOMBRES NO TRAGA CUALQUIER COSA")
    escenarios = [
        ("un .md con ruta corta", "LECTURAS_DIRIGIDAS.md, las once", ["LECTURAS_DIRIGIDAS.md"]),
        ("un .jsonl", "INVENTARIO.jsonl, 323 entradas", ["INVENTARIO.jsonl"]),
        ("dos en la misma mencion", "A.md y B.jsonl juntos", ["A.md", "B.jsonl"]),
        ("prosa con puntos", "MEDIDO el 11 ago 2026: 205 pares. 11 leidos.", []),
        ("una version, que no es un fichero", "el pack v1.3 salio", []),
        ("una extension que no esta en la lista", "la hoja tabla.xlsx", []),
    ]
    for etiqueta, mencion, esperado in escenarios:
        f = ficha("OP-M-09", "MESA", [mencion])
        leidos = [n for _m, n in VARA.rutas_de_la_evidencia(f)]
        casos += 1
        ok = (leidos == esperado)
        w("   %-40s %-46r -> %s | esperado %s | %s"
          % (etiqueta, mencion[:44], leidos, esperado,
             "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos += 1
        w("      MUTACION del esperado (exigir %d nombres): %s"
          % (len(esperado) + 1,
             "PASA" if len(leidos) == len(esperado) + 1 else "CAE"))
        if len(leidos) == len(esperado) + 1:
            fallos += 1
        else:
            caen += 1
    w("")
    return fallos, casos, caen


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    disco, lf, sha = sello_del_sujeto(SUJETO)
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DE LA CUARTA PRUEBA, LA DOCUMENTAL")
    w("(vuelta 188, TAREA 2; encargada por el punto 12 del acta 188)")
    w("=" * 78)
    w("")
    w("EL SUJETO ES EL FICHERO VIVO %s, IMPORTADO." % SUJETO)
    w("SELLO DEL SUJETO (vuelta 188, TAREA 3.b): disco %d bytes | LF %d bytes |"
      % (disco, lf))
    w("sha256 LF %s" % sha)
    w("Con ese sello al lado, un diff futuro de esta salida dice SI SE MOVIO EL")
    w("SUJETO O SE MOVIO EL ARNES, en vez de dejarlo a que alguien lo deduzca.")
    w("")
    w("LINEAS DEL SUJETO QUE ESTE ARNES JUZGA, LEIDAS HOY Y CON EL SELLO DE ARRIBA:")
    fuente = io.open(os.path.join(RAIZ, SUJETO.replace("/", os.sep)),
                     encoding="utf-8").read().replace(chr(13) + NL, NL)
    for aguja in ("def rutas_de_la_evidencia", "def localizar_evidencia",
                  "def p4_vara_documental", "TIPO_DOCUMENTAL ="):
        hits = [i for i, l in enumerate(fuente.split(NL), 1) if l.startswith(aguja)]
        w("   %-32s -> lineas %s"
          % (aguja, ", ".join(str(x) for x in hits) or "(ninguna)"))
    w("")
    fallos = casos = caen = 0
    for parte in (_caso_a, _casos_bcd, _caso_e):
        f, c, k = parte(w)
        fallos += f
        casos += c
        caen += k
    w("CIFRA casos: %d | pasan: %d" % (casos, casos - fallos))
    w("CIFRA casos que CAEN al mutar su esperado: %d de %d" % (caen, caen))
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V188_T2_MUTACION_PATA_DOCUMENTAL.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
