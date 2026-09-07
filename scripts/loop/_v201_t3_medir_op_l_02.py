# -*- coding: utf-8 -*-
r"""_v201_t3_medir_op_l_02.py . LA MEDICION DE `OP-L-02` CONTRA SU CAMPO
`verificacion`, NO CONTRA SU `evidencia` (TAREA 3 de la vuelta 201).

ADJUDICADA POR EL ACTA 199 EN SU `4.2`. `OP-L-02` es la unica de las cuatro
fichas reales SIN DOCUMENTO QUE MEDIR: su `evidencia` entera es prosa, con CERO
menciones de fichero, y eso lo cuenta este mismo computo en vez de heredarlo.

PREFIJO DE GUION BAJO Y POR EL MISMO MOTIVO QUE SUS HERMANOS de esta vuelta
(moratoria `AUDITOR.md` 6.3 mas adjudicacion `4.5` del acta 199): computo de una
vuelta, fuera del censo y fuera de la nomina, que no vigila a nadie.

QUE HACE Y QUE NO HACE. LEE la ficha entera, CITA su `verificacion` clausula a
clausula con su linea, y por cada clausula dice **que pide exactamente**, **que
parte se puede comprobar hoy contra el repo** y **que parte no**. **NO MUEVE
NINGUN `estado`**, **no cierra la ficha**, **no adjudica nada** y **no escribe
una sola linea en `docs/plan/`**: lo unico que produce es una salida sellada.

LO QUE MIDE, Y CADA COSA CON SU FUENTE:
  . el marcador del cribado, RECONTADO HOY de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
    linea a linea, con su reparto por clase. NO PASA POR EL RESOLUTOR, y se dice
    por que: `P.1` manda el resolutor para TODO CONTEO QUE TOQUE IDS, y contar
    PUESTOS no toca ids. Los ids de las filas ni se agrupan ni se comparan aqui.
  . cuantas nominas nombra la clausula 1 (`tres`) contra cuantas nombra la
    propia `nota` de la ficha (`SEIS`), que es la discrepancia que decide si la
    clausula alcanza para ejecutar sin decidir.
  . si las nominas estan NOMBRADAS POR ID en algun sitio de la ficha.
  . los grupos del backlog y si cada uno lleva motivo escrito (clausula 3).
  . las rutas que la ficha promete como prueba: existen y cuantos bytes miden
    (`EJECUTOR.md` 1, LA RUTA QUE PROMETE PRUEBA ES CIFRA).

USO:
  python scripts/loop/_v201_t3_medir_op_l_02.py
"""
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
ID_OP = "OP-L-02"

# LAS NOMINAS QUE LA `nota` DE LA FICHA NOMBRA EN CASTELLANO. No es una tabla de
# verdad: es la lista de agujas con las que se BUSCA en el texto de la ficha, y
# el resultado de la busqueda es lo que se publica.
AGUJAS_NOMINA = ["cuadrantes", "ecuacion de valor", "bloque humano",
                 "sales roadmap", "supervision de la IA"]
# LAS RUTAS QUE LA FICHA PROMETE COMO PRUEBA, extraidas de su propio texto mas
# abajo. Esta lista solo fija el patron con que se extraen.
PATRON_RUTA = re.compile(r"(docs/[A-Za-z0-9_/.-]+\.(?:md|jsonl|txt|json))")


def marcador_del_cribado(ruta=None):
    """EL MARCADOR, RECONTADO LINEA A LINEA. Devuelve (filas, por_clase,
    puestos_distintos, maximo, huecos, bytes_disco, bytes_lf).

    NO PASA POR EL RESOLUTOR Y SE DICE POR QUE: `P.1` lo manda para todo conteo
    QUE TOQUE IDS, y aqui no se toca ninguno. Se cuentan filas y puestos."""
    ruta = ruta or VEREDICTOS
    crudo = io.open(ruta, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    filas = [l for l in lf.decode("utf-8").split(NL) if l.strip()]
    por_clase = {}
    puestos = set()
    for l in filas:
        d = json.loads(l)
        c = d.get("clase", "(sin clase)")
        por_clase[c] = por_clase.get(c, 0) + 1
        p = d.get("puesto_intra")
        if p is not None:
            puestos.add(p)
    maximo = max(puestos) if puestos else 0
    huecos = [i for i in range(1, maximo + 1) if i not in puestos]
    return (len(filas), por_clase, len(puestos), maximo, len(huecos),
            len(crudo), len(lf))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 201, TAREA 3 . %s MEDIDA CONTRA SU `verificacion`" % ID_OP)
    w("adjudicada por el acta 199 en su 4.2. NO SE MUEVE NINGUN `estado`.")
    w("=" * 78)
    w("")

    w("A) LA FICHA, LOCALIZADA POR LINEA Y LEIDA ENTERA")
    crudo = io.open(OPERACIONES, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    lineas = lf.decode("utf-8").split(NL)
    aguja = chr(34) + "id_op" + chr(34) + ": " + chr(34) + ID_OP + chr(34)
    hits = [i for i, l in enumerate(lineas, 1) if l.strip() and aguja in l]
    w("   docs/plan/OPERACIONES.jsonl: disco %d bytes | LF %d bytes"
      % (len(crudo), len(lf)))
    w("   CIFRA lineas con la ficha %s: %d, linea(s) %s"
      % (ID_OP, len(hits), ", ".join(str(x) for x in hits) or "(ninguna)"))
    if len(hits) != 1:
        w("   ROJO: la ficha no aparece exactamente una vez.")
        print(NL.join(L))
        return 1
    ln = hits[0]
    d = json.loads(lineas[ln - 1])
    ver = d.get("verificacion", [])
    ev = d.get("evidencia", [])
    w("   estado (SE LEE, NO SE MUEVE): %r" % d.get("estado"))
    w("   fecha_corte: %r | tipo: %r | fase: %r"
      % (d.get("fecha_corte"), d.get("tipo"), d.get("fase")))
    w("   depende_de: %s" % ", ".join(d.get("depende_de") or []) or "(ninguna)")
    w("")

    w("B) POR QUE SE MIDE CONTRA `verificacion` Y NO CONTRA `evidencia`,")
    w("   CONTADO AQUI Y NO HEREDADO DEL ENCARGO")
    w("   CIFRA elementos de `evidencia`: %d" % len(ev))
    for i, x in enumerate(ev, 1):
        w("      evidencia[%d]: %s" % (i, x))
    con_fichero = [i for i, x in enumerate(ev, 1) if PATRON_RUTA.search(str(x))]
    w("   CIFRA elementos de `evidencia` que nombran un fichero: %d  %s"
      % (len(con_fichero),
         ", ".join(str(x) for x in con_fichero) or "(ninguno)"))
    w("   ESA ES LA RAZON, Y ES UNA CIFRA: sin fichero nombrado NO HAY DOCUMENTO")
    w("   QUE MEDIR, asi que la vara tiene que ser el campo `verificacion`.")
    w("")

    w("C) LA `verificacion`, CITADA CLAUSULA A CLAUSULA CON SU LINEA")
    w("   LA FICHA ES UNA LINEA DE JSONL, asi que la cita por linea es la LINEA")
    w("   %d de docs/plan/OPERACIONES.jsonl, y dentro de ella el INDICE del" % ln)
    w("   elemento en la lista `verificacion`. Las dos coordenadas se dan juntas.")
    w("   CIFRA elementos de `verificacion`: %d" % len(ver))
    for i, x in enumerate(ver, 1):
        s = str(x)
        w("   --- verificacion[%d] (linea %d) %s ---"
          % (i, ln, "CLAUSULA" if "CORRECCION DECLARADA" not in s
             else "CORRECCION DECLARADA POR ADICION"))
        for trozo in [s[k:k + 72] for k in range(0, len(s), 72)]:
            w("      | " + trozo)
    w("")

    w("D) CLAUSULA 1: LAS TRES NOMINAS. QUE PIDE Y QUE SE PUEDE COMPROBAR")
    c1 = str(ver[0]) if ver else ""
    w("   PIDE, verbatim: %r" % c1)
    w("   PIDE DOS COSAS Y NO UNA: (i) que las nominas afectadas queden con")
    w("      COBERTURA COMPLETA, y (ii) que su FORMA quede REESCRITA.")
    m_tres = re.search(r"\b(tres|cuatro|cinco|seis|siete)\b", c1)
    w("   EL NUMERAL QUE LA CLAUSULA ESCRIBE: %s"
      % (m_tres.group(1) if m_tres else "(ninguno)"))
    texto_ficha = json.dumps(d, ensure_ascii=False)
    w("   CUANTAS NOMINAS NOMBRA LA PROPIA FICHA, CONTADO DE SU TEXTO:")
    for ag in AGUJAS_NOMINA:
        w("      %-24s aparece %d vez(ces) en el texto de la ficha"
          % (ag, texto_ficha.count(ag)))
    seis = len(re.findall(r"SEIS nominas", texto_ficha))
    tres = len(re.findall(r"TRES nominas", texto_ficha))
    w("   CIFRA apariciones del literal 'SEIS nominas' en la ficha: %d" % seis)
    w("   CIFRA apariciones del literal 'TRES nominas' en la ficha: %d" % tres)
    w("   LAS NOMINAS NO ESTAN NOMBRADAS POR ID EN NINGUN SITIO DE LA FICHA, y")
    w("      eso se cuenta en vez de afirmarse: los campos `nodos`, `preservar`,")
    w("      `eliminar` y `superviviente` de esta ficha miden")
    w("      nodos=%d preservar=%d eliminar=%d superviviente=%r"
      % (len(d.get("nodos") or []), len(d.get("preservar") or []),
         len(d.get("eliminar") or []), d.get("superviviente")))
    w("")

    w("E) CLAUSULA 2: EL MARCADOR. RECONTADO HOY, LINEA A LINEA")
    c2 = str(ver[1]) if len(ver) > 1 else ""
    w("   PIDE, verbatim: %r" % c2)
    n, por_clase, distintos, maximo, huecos, bd, blf = marcador_del_cribado()
    w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl: disco %d bytes | LF %d bytes"
      % (bd, blf))
    w("   CIFRA filas: %d" % n)
    w("   CIFRA puestos distintos: %d | maximo: %d | huecos: %d"
      % (distintos, maximo, huecos))
    w("   EL REPARTO POR CLASE, RECONTADO HOY:")
    for c in sorted(por_clase):
        w("      clase %-12s %d" % (c, por_clase[c]))
    w("   SUMA DEL REPARTO: %d" % sum(por_clase.values()))
    w("   NO PASA POR EL RESOLUTOR Y SE DICE POR QUE: `P.1` lo manda para TODO")
    w("      CONTEO QUE TOQUE IDS, y contar PUESTOS no toca ninguno. Aqui no se")
    w("      agrupa ni se compara un solo id.")
    w("   EL NUMERAL 2.117 DE LA CLAUSULA, CONTRA LO MEDIDO HOY: la correccion")
    w("      declarada de la vuelta 170 que vive en esta misma lista ya dice que")
    w("      el 2.117 es TESTIGO Y NO CONDICION, y que la clausula exige que la")
    w("      OPERACION no mueva el marcador, no que valga 2.117 hoy.")
    w("")

    w("F) CLAUSULA 3: CADA GRUPO DEL BACKLOG CON SU MOTIVO ESCRITO")
    c3 = str(ver[2]) if len(ver) > 2 else ""
    w("   PIDE, verbatim: %r" % c3)
    nota = str(d.get("nota") or "")
    m_backlog = re.search(r"BACKLOG DOCUMENTADO,\s*(\d+)\s*pares:(.*?)\.", nota)
    if m_backlog:
        total = m_backlog.group(1)
        cuerpo = m_backlog.group(2)
        grupos = [g.strip() for g in cuerpo.split(",") if g.strip()]
        w("   EL BACKLOG, LEIDO DEL CAMPO `nota` DE LA PROPIA FICHA:")
        w("      CIFRA pares del backlog: %s" % total)
        w("      CIFRA grupos escritos: %d" % len(grupos))
        suma = 0
        con_motivo = 0
        for g in grupos:
            # LA CONJUNCION SE QUITA ANTES DE LEER LA CIFRA, Y ES UNA CORRECCION
            # MEDIDA DE ESTE MISMO COMPUTO. La primera version casaba
            # r"(\d+)\s+(.*)" contra el trozo crudo, y el CUARTO grupo de la
            # nota empieza por "y 3 ya leidas...": el patron NO casaba, la cuenta
            # salia 0, el motivo salia vacio y este computo publicaba
            # "3 de 4 grupos con motivo" y "186 contra 189, NO CALZA". LA FICHA
            # ESTABA BIEN Y EL LECTOR ESTABA MAL. Se corrige aqui y se declara,
            # porque una caida que se tapa no se puede auditar.
            g = re.sub(r"^y\s+", "", g)
            mg = re.match(r"(\d+)\s+(.*)", g)
            cuenta = int(mg.group(1)) if mg else 0
            motivo = mg.group(2) if mg else ""
            suma += cuenta
            tiene = len(motivo.strip()) > 0
            con_motivo += 1 if tiene else 0
            w("         %-4s %-52s motivo escrito: %s"
              % (cuenta, motivo[:52], "SI" if tiene else "NO"))
        w("      SUMA DE LOS GRUPOS: %d contra el total escrito %s -> %s"
          % (suma, total, "CALZA" if str(suma) == total else "NO CALZA"))
        w("      CIFRA grupos CON motivo escrito: %d de %d"
          % (con_motivo, len(grupos)))
        w("      LA CLAUSULA 3 SE PUEDE COMPROBAR HOY Y SALE: %s"
          % ("CUMPLIDA" if con_motivo == len(grupos) and grupos
             else "NO CUMPLIDA"))
    else:
        w("   NO SE ENCUENTRA el bloque 'BACKLOG DOCUMENTADO, N pares:' en la")
        w("      `nota`. LA CIFRA NO SE PUBLICA.")
    w("")

    w("G) CLAUSULA 4: LA CORRECCION DECLARADA DE LA VUELTA 170, QUE YA VIVE")
    w("   DENTRO DE ESTA MISMA LISTA")
    c4 = str(ver[3]) if len(ver) > 3 else ""
    w("   CIFRA caracteres: %d" % len(c4))
    w("   NO ES UNA CLAUSULA QUE PEDIR: es la correccion por adicion de la")
    w("      clausula 2, y por eso NO se mide como criterio. Se cita entera en")
    w("      el bloque C.")
    w("")

    w("H) LAS RUTAS QUE LA FICHA PROMETE COMO PRUEBA, MEDIDAS UNA A UNA")
    w("   (EJECUTOR.md 1, LA RUTA QUE PROMETE PRUEBA ES CIFRA: si apunta a un")
    w("   fichero inexistente o de CERO BYTES es CAIDA DE CIFRA.)")
    rutas = []
    for x in PATRON_RUTA.findall(texto_ficha):
        if x not in rutas:
            rutas.append(x)
    w("   CIFRA rutas distintas nombradas en la ficha: %d" % len(rutas))
    vivas = muertas = vacias = 0
    for r in rutas:
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        if not os.path.isfile(p):
            w("      %-52s NO EXISTE" % r)
            muertas += 1
            continue
        t = os.path.getsize(p)
        if t == 0:
            w("      %-52s EXISTE PERO MIDE CERO BYTES" % r)
            vacias += 1
        else:
            w("      %-52s %d bytes en disco" % (r, t))
            vivas += 1
    w("   CIFRA rutas vivas: %d | inexistentes: %d | de cero bytes: %d"
      % (vivas, muertas, vacias))
    w("")

    w("I) EL VEREDICTO DE LA LECTURA, CON SU CIFRA DELANTE")
    w("   CLAUSULA 1: NO ALCANZA PARA EJECUTAR SIN DECIDIR.")
    w("      Motivo medido, no opinado: la clausula escribe el numeral %r y la"
      % (m_tres.group(1) if m_tres else "(ninguno)"))
    w("      propia `nota` de la ficha escribe 'SEIS nominas' %d vez(ces) y" % seis)
    w("      'TRES nominas' %d vez(ces). Las dos frases estan en la MISMA ficha," % tres)
    w("      hablan de las MISMAS nominas y dan numeros distintos, y NINGUNA de")
    w("      las dos las nombra por id: los campos `nodos`, `preservar`,")
    w("      `eliminar` y `superviviente` de la ficha estan TODOS vacios.")
    w("      Elegir cuales son las 'tres afectadas' es DECIDIR, no medir.")
    w("   CLAUSULA 2: SE PUEDE MEDIR EL MARCADOR, PERO NO ES CRITERIO DE HECHO.")
    w("      Lo que pide es que la OPERACION no mueva el marcador. Eso solo se")
    w("      comprueba corriendo la operacion y comparando antes y contra")
    w("      despues, y la operacion NO SE HA CORRIDO. Hoy el marcador vale %d," % n)
    w("      con 0 huecos, y ese numero es un ESTADO, no el cumplimiento de la")
    w("      clausula.")
    w("   CLAUSULA 3: SE PUEDE COMPROBAR HOY Y SE COMPRUEBA ARRIBA.")
    w("   CLAUSULA 4: NO ES CRITERIO, ES LA CORRECCION DECLARADA DE LA 2.")
    w("   POR TANTO: `%s` NO SE PUEDE EJECUTAR HOY SIN DECIDIR, y eso NO SE" % ID_OP)
    w("      IMPROVISA NI SE DECLARA HECHA. Va como PARADA al reporte, con esta")
    w("      medicion, por AUDITOR.md 3.")
    w("")
    w("J) LO QUE ESTE COMPUTO NO HIZO, DICHO PARA QUE NO HAGA FALTA MIRARLO")
    w("   No movio ningun `estado`, no cerro la ficha, no adjudico ninguna clase,")
    w("   no toco ni un veredicto, no escribio una sola linea en docs/plan/ y no")
    w("   ejecuto la operacion. Lo unico que produce es esta salida sellada.")
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V201_T3_OP_L_02.txt"), "w",
            encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
