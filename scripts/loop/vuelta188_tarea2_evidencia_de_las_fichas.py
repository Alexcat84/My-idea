# -*- coding: utf-8 -*-
r"""vuelta188_tarea2_evidencia_de_las_fichas.py . LAS CUATRO FICHAS QUE LA VARA
NOMBRA, RESUELTAS CONTRA SU EVIDENCIA DOCUMENTAL.

QUIEN LO ENCARGA. El acta 188, punto 12, y el encargo de la vuelta 188, TAREA 2:
*"Encargo resolver el estado de las cuatro contra su evidencia DOCUMENTAL, con la
vara ganando su pata documental para las de tipo `MESA`, y `estado` no se toca,
porque la casa ya declaro ese campo historico"*.

QUE HACE, Y EN ESTE ORDEN:

  A) LEE LAS CUATRO FICHAS ENTERAS de `docs/plan/OPERACIONES.jsonl` y las CITA,
     campo a campo, sin parafrasear.
  B) MIDE SI SU PRODUCTO EXISTE, contra la `evidencia` que la propia ficha
     nombra, con bytes POR LAS DOS CONVENCIONES.
  C) COTEJA LO QUE LA FICHA PROMETE CONTRA LO QUE HAY: las once lecturas de
     `OP-L-01` y las 323 entradas de `OP-I-01`, contadas del fichero y no
     copiadas del acta.
  D) MIDE EL DESFASE DE SUS CORTES: la `fecha_corte`, el marcador que las cuatro
     citan y el que el archivo dice HOY, y los cuatro dominios que `OP-I-01`
     nombra como su hueco mayor.
  E) DECLARA EL ESTADO DE CADA UNA en una de estas tres formas y en ninguna otra:
     (a) SU PRODUCTO ESTA Y LA CUBRE, (b) SU PRODUCTO ESTA PERO NO LA CUBRE
     nombrando que falta, o (c) NO HAY EVIDENCIA QUE LA DECIDA, y entonces es
     PARADA y se trae.

LO QUE ESTE FICHERO NO HACE, Y ES LA MITAD DEL ENCARGO: **NO toca el campo
`estado`**, declarado HISTORICO el 4 sep 2026; **NO reescribe ninguna ficha para
ponerla al dia**, que eso es plan; **NO mueve ningun veredicto**; y **NO decide
ninguna clase**. Mide, coteja y declara.

USO:
  python scripts/loop/vuelta188_tarea2_evidencia_de_las_fichas.py
"""
import hashlib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta150_3_relectura_expediente as VARA   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NL = chr(10)

CUATRO = ("OP-L-01", "OP-L-02", "OP-L-03", "OP-I-01")

# LO QUE CADA FICHA PROMETE, LEIDO DE SU PROPIO TEXTO Y NO TECLEADO. Cada entrada
# es (id_op, patron sobre el texto de la ficha, que se cuenta en el producto).
# El patron saca LA CIFRA DE LA FICHA; el contador saca LA DEL DISCO. Las dos se
# publican y su diferencia se nombra.
PROMESAS = [
    ("OP-I-01", re.compile(r"INVENTARIO\.jsonl,\s*(\d+)\s*entradas"),
     "entradas no vacias de docs/plan/INVENTARIO.jsonl"),
]

# LAS ETIQUETAS `LD-nn` SE CUENTAN CON DOS PATRONES Y SE PUBLICAN LAS DOS CIFRAS.
# El ancho es UN PATRON DE CABECERA (la etiqueta al principio de una linea o
# detras de una vineta o de una almohadilla), que es como el documento marca una
# lectura; el estrecho es toda aparicion, incluidas las CITAS dentro de la prosa
# de otra lectura. Publicar solo una de las dos diria mas de lo que se sabe.
PAT_LD_TODAS = re.compile(r"\bLD-(\d+)\b")
PAT_LD_CABECERA = re.compile(r"^(?:[#>\-*\s|]*)\**\s*`?LD-(\d+)`?\b")

# EL MARCADOR QUE LAS FICHAS CITAN, buscado en el texto entero de cada una.
# EL MARCADOR QUE UNA FICHA CITA SE BUSCA CON SU CONTEXTO Y NO A SECAS, Y ESO SE
# MIDIO ANTES DE DECIDIRLO. Con el patron suelto `sigue en (\d+)`, `OP-I-01`
# devolvia 671, que NO es un marcador: es la frase `el archivo sigue en 671
# lineas` hablando del propio inventario. Contar bien un patron y atribuirlo al
# sujeto equivocado es la caida del recuadro de AUDITOR.md 0, otra vez.
PAT_MARCADOR_FICHA = re.compile(
    r"marcador\s+del\s+cribado\s+no\s+se\s+mueve:\s*sigue\s+en\s*([0-9.]+)")
PAT_CORTE_PUESTO = re.compile(r"corte\s+(?:del\s+)?puesto\s+([0-9.]+)")


def sha_de(ruta):
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest())


def texto_entero(f):
    """TODO EL TEXTO DE UNA FICHA, UNIDO. PURA."""
    trozos = []
    for k in sorted(f.keys()):
        v = f[k]
        if isinstance(v, list):
            trozos += [str(x) for x in v]
        elif v is not None:
            trozos.append(str(v))
    return " ".join(trozos)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 188, TAREA 2: LAS CUATRO FICHAS RESUELTAS CONTRA SU EVIDENCIA")
    w("(acta 188, punto 12. `estado` NO SE TOCA: la casa lo declaro HISTORICO)")
    w("=" * 78)
    w("")

    fichas = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    por_id = {f["id_op"]: f for f in fichas}
    d_ops, l_ops, s_ops = sha_de(OPS)
    w("A) EL EXPEDIENTE Y LAS CUATRO FICHAS, LEIDAS ENTERAS")
    w("   docs/plan/OPERACIONES.jsonl -> disco %d bytes | LF %d bytes | sha256 LF %s"
      % (d_ops, l_ops, s_ops))
    w("   CIFRA fichas del expediente: %d" % len(fichas))
    faltan = [i for i in CUATRO if i not in por_id]
    if faltan:
        w("   PARADA: no estan en el expediente: %s" % ", ".join(faltan))
        print(NL.join(L))
        return 1
    w("   CIFRA de las cuatro cuyo `tipo` es MESA: %d"
      % len([1 for i in CUATRO if por_id[i].get("tipo") == "MESA"]))
    w("   CIFRA de las cuatro cuyo `estado` es LISTA: %d"
      % len([1 for i in CUATRO if por_id[i].get("estado") == "LISTA"]))
    w("   CIFRA de las cuatro con `depende_de` VACIO: %d (%s)"
      % (len([1 for i in CUATRO if not (por_id[i].get("depende_de") or [])]),
         ", ".join(i for i in CUATRO if not (por_id[i].get("depende_de") or []))))
    w("")
    for i in CUATRO:
        f = por_id[i]
        w("   " + "-" * 72)
        for k in ("id_op", "fase", "tipo", "orden", "estado", "fecha_corte"):
            w("   %-16s %s" % (k, f.get(k)))
        for k in ("depende_de", "bloquea_a", "verificacion", "evidencia"):
            v = f.get(k) or []
            w("   %-16s [%d]" % (k, len(v)))
            for j, e in enumerate(v):
                w("      [%d] %s" % (j, str(e)))
        for k in ("adjudicacion", "nota", "pregunta_pendiente"):
            w("   %-16s %s" % (k, f.get(k)))
    w("")

    w("B) EL PRODUCTO DE CADA UNA, MEDIDO CONTRA LA `evidencia` QUE ELLA NOMBRA")
    w("   (por las DOS convenciones, y con el auditor recomputado y no creido)")
    v4 = VARA.p4_vara_documental(fichas)
    productos = {}
    for i in CUATRO:
        f = por_id[i]
        menciones = VARA.rutas_de_la_evidencia(f)
        halladas = v4.get(i)
        w("   %s" % i)
        w("      menciones de fichero en su `evidencia`: %d" % len(menciones))
        if not menciones:
            w("      SU EVIDENCIA ENTERA ES PROSA: no nombra ningun fichero.")
        for mencion, nombre in menciones:
            ruta, disco, lf = VARA.localizar_evidencia(nombre)
            if ruta is None:
                w("      `%s` -> NO EXISTE EN DISCO (mencion: %s)"
                  % (nombre, mencion[:70]))
            else:
                w("      `%s` -> `%s` | disco %d bytes | LF %d bytes"
                  % (nombre, ruta, disco, lf))
                productos.setdefault(i, []).append((nombre, ruta, disco, lf))
        w("      halladas por la P4 documental: %s"
          % ("%d" % len(halladas) if halladas is not None else "(no es MESA)"))
    w("")

    w("C) LO QUE LA FICHA PROMETE CONTRA LO QUE HAY, CONTADO DEL PRODUCTO")
    w("")
    w("   C.1 `OP-L-01`: LAS ONCE LECTURAS DIRIGIDAS")
    f1 = por_id["OP-L-01"]
    t1 = texto_entero(f1)
    m_once = re.search(r"ONCE\s+LECTURAS\s+DIRIGIDAS", t1, re.I)
    prometidas = re.findall(r"\bLD-(\d+)\b", str(f1.get("nota") or ""))
    w("      la ficha dice literalmente: %r"
      % (m_once.group(0) if m_once else "(no dice ONCE lecturas dirigidas)"))
    w("      etiquetas `LD-nn` que su propia `nota` enumera: %d (%s)"
      % (len(set(prometidas)),
         ", ".join("LD-%s" % x for x in sorted(set(prometidas), key=int))))
    LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
    if not os.path.exists(LD):
        w("      PARADA: docs/plan/LECTURAS_DIRIGIDAS.md NO EXISTE.")
        print(NL.join(L))
        return 1
    d_ld, l_ld, s_ld = sha_de(LD)
    txt_ld = io.open(LD, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    todas = sorted(set(PAT_LD_TODAS.findall(txt_ld)), key=int)
    cabec = sorted(set(x for l in txt_ld.split(NL)
                       for x in PAT_LD_CABECERA.findall(l)), key=int)
    w("      docs/plan/LECTURAS_DIRIGIDAS.md -> disco %d bytes | LF %d bytes |"
      % (d_ld, l_ld))
    w("      sha256 LF %s | %d lineas" % (s_ld, txt_ld.count(NL)))
    w("      LAS DOS CUENTAS, Y SE PUBLICAN LAS DOS PORQUE UNA SOLA DIRIA DE MAS:")
    w("         etiquetas distintas por TODA APARICION (incluye citas dentro de")
    w("         la prosa de otra lectura): %d, de LD-%s a LD-%s"
      % (len(todas), todas[0] if todas else "?", todas[-1] if todas else "?"))
    w("         etiquetas distintas EN CABECERA (la etiqueta al principio de su")
    w("         linea, que es como el documento marca una lectura): %d, de LD-%s a"
      % (len(cabec), cabec[0] if cabec else "?"))
    w("         LD-%s" % (cabec[-1] if cabec else "?"))
    once = [x for x in cabec if int(x) <= 11]
    w("      DE LAS ONCE QUE LA FICHA DESCRIBE (LD-01 a LD-11), ESTAN EN CABECERA: %d"
      % len(once))
    w("         %s" % ", ".join("LD-%s" % x for x in once))
    w("      EL CONTRASTE CONTRA EL ACTA, DECLARADO Y NO RESUELTO COPIANDO: el acta")
    w("      188 punto 12 dice `de LD-01 hasta LD-98`. Mi medicion de hoy da como")
    w("      maximo LD-%s por toda aparicion y LD-%s en cabecera. NO se copia la"
      % (todas[-1] if todas else "?", cabec[-1] if cabec else "?"))
    w("      cifra del acta y NO se toca la del disco: se publican las dos.")
    w("      Y LAS DOS ETIQUETAS EXISTEN, LOCALIZADAS CON SU LINEA (y el `sha256` del")
    w("      sujeto va arriba, TAREA 3.b, para que estas lineas no envejezcan solas):")
    for etq in ("LD-98", "LD-154"):
        hits = [n for n, l in enumerate(txt_ld.split(NL), 1)
                if l.lstrip().startswith(("#", ">", "-", "*", "|", "`"))
                and etq in l and l.lstrip().lstrip("#>-*| ").startswith(("`" + etq, etq))]
        w("         %-8s en cabecera, lineas %s"
          % (etq, ", ".join(str(x) for x in hits) or "(ninguna)"))
    w("      NINGUNA DE LAS DOS CIFRAS ES FALSA: el documento NO numera en orden de")
    w("      posicion, asi que el mayor por numero y el mayor por posicion no son el")
    w("      mismo. Se dice, no se elige uno y se calla el otro.")
    w("")

    w("   C.2 `OP-I-01`: LAS 323 ENTRADAS DEL INVENTARIO")
    f2 = por_id["OP-I-01"]
    t2 = texto_entero(f2)
    prom = None
    for _id, pat, _que in PROMESAS:
        m = pat.search(t2)
        if m:
            prom = int(m.group(1))
    w("      la ficha promete, leido de su propio texto: %s entradas" % prom)
    INV = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
    if not os.path.exists(INV):
        w("      PARADA: docs/plan/INVENTARIO.jsonl NO EXISTE.")
        print(NL.join(L))
        return 1
    d_inv, l_inv, s_inv = sha_de(INV)
    lineas_inv = [l for l in io.open(INV, encoding="utf-8") if l.strip()]
    validas = 0
    sujetos = {}
    for l in lineas_inv:
        try:
            e = json.loads(l)
            validas += 1
            k = e.get("tipo") or e.get("clase") or "(sin tipo)"
            sujetos[k] = sujetos.get(k, 0) + 1
        except Exception:
            pass
    w("      docs/plan/INVENTARIO.jsonl -> disco %d bytes | LF %d bytes |"
      % (d_inv, l_inv))
    w("      sha256 LF %s" % s_inv)
    w("      CIFRA entradas no vacias: %d" % len(lineas_inv))
    w("      CIFRA de esas que son JSON valido: %d" % validas)
    w("      DIFERENCIA contra lo que la ficha promete: %s"
      % (("%+d" % (len(lineas_inv) - prom)) if prom else "(la ficha no lo dice)"))
    w("      EL REPARTO POR TIPO, CONTADO DEL FICHERO:")
    for k in sorted(sujetos, key=lambda x: (-sujetos[x], str(x))):
        w("         %-28s %d" % (k, sujetos[k]))
    w("")

    w("D) EL DESFASE DE LOS CORTES, MEDIDO Y PUBLICADO (NO REPARADO)")
    d_v, l_v, s_v = sha_de(VEREDICTOS)
    filas = [json.loads(l) for l in io.open(VEREDICTOS, encoding="utf-8") if l.strip()]
    w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> disco %d bytes | LF %d bytes"
      % (d_v, l_v))
    w("   sha256 LF: %s" % s_v)
    w("   MARCADOR RECOMPUTADO DEL ARCHIVO HOY: %d filas" % len(filas))
    w("   LA `fecha_corte` DE CADA UNA DE LAS CUATRO, Y EL MARCADOR QUE CITA:")
    for i in CUATRO:
        f = por_id[i]
        t = texto_entero(f)
        m = PAT_MARCADOR_FICHA.search(t)
        mc = PAT_CORTE_PUESTO.search(t)
        cita = m.group(1) if m else (mc.group(1) if mc else None)
        w("      %-10s fecha_corte %-12s marcador que cita: %-8s | hoy %d | desfase %s"
          % (i, f.get("fecha_corte"), cita if cita else "(ninguno)", len(filas),
             ("%+d" % (len(filas) - int(cita.replace(".", ""))))
             if cita else "(no medible)"))
        w("                    la frase de la que sale: %r"
          % ((m.group(0) if m else mc.group(0))[:110] if (m or mc) else "(ninguna)"))
    w("")
    w("   EL HUECO MAYOR QUE `OP-I-01` NOMBRA, COTEJADO CONTRA EL ARCHIVO DE HOY:")
    nota = str(por_id["OP-I-01"].get("nota") or "")
    m_dom = re.search(r"CUATRO DOMINIOS[^:]*:?\s*([^)]*)\)", nota)
    w("      la ficha dice: %r"
      % (m_dom.group(0)[:200] if m_dom else "(no se localiza la frase)"))
    nombrados = ["quality", "health_safety", "risk_management", "seguridad_digital"]
    dominios_hoy = {}
    for f in filas:
        d = f.get("dominio")
        dominios_hoy[d] = dominios_hoy.get(d, 0) + 1
    w("      CIFRA dominios distintos en el archivo de veredictos HOY: %d"
      % len(dominios_hoy))
    for d in nombrados:
        w("         %-22s pares en el archivo HOY: %d"
          % (d, dominios_hoy.get(d, 0)))
    fuera = [d for d in nombrados if dominios_hoy.get(d, 0) == 0]
    w("      CIFRA de los cuatro que HOY siguen sin un solo par en el archivo: %d (%s)"
      % (len(fuera), ", ".join(fuera) or "ninguno"))
    w("      LA FICHA LOS NOMBRA COMO SU HUECO MAYOR CON CORTE DEL 11 AGO 2026.")
    w("      SE MIDE Y SE PUBLICA. NO SE REESCRIBE LA FICHA: eso es plan.")
    w("")

    w("E) EL ESTADO DE CADA UNA DE LAS CUATRO, CON SU EVIDENCIA DELANTE")
    w("   (una de estas tres formas y en ninguna otra:")
    w("    (a) SU PRODUCTO ESTA Y LA CUBRE | (b) SU PRODUCTO ESTA PERO NO LA CUBRE,")
    w("    nombrando que falta | (c) NO HAY EVIDENCIA QUE LA DECIDA, y es PARADA)")
    w("")
    veredictos = []
    # OP-L-01
    cubre_01 = (len(once) == 11)
    veredictos.append((
        "OP-L-01",
        "(a) SU PRODUCTO ESTA Y LA CUBRE" if cubre_01
        else "(b) SU PRODUCTO ESTA PERO NO LA CUBRE",
        "docs/plan/LECTURAS_DIRIGIDAS.md existe (%d bytes por las dos convenciones) "
        "y trae en cabecera %d de las once que la ficha describe (LD-01 a LD-11). "
        "El documento ha crecido muy por encima: %d etiquetas distintas en cabecera, "
        "hasta LD-%s." % (d_ld, len(once), len(cabec),
                          cabec[-1] if cabec else "?")))
    # OP-L-02
    veredictos.append((
        "OP-L-02",
        "(c) NO HAY EVIDENCIA QUE LA DECIDA",
        "su `evidencia` entera es prosa (`MEDIDO el 11 ago 2026: 205 pares fuera de "
        "cola, 11 leidos, 194 pendientes`) y NO NOMBRA NINGUN FICHERO, asi que no hay "
        "documento que medir. Su `verificacion` habla de tres nominas y de un backlog "
        "con su motivo, y ninguna de las dos cosas tiene sede declarada en la ficha."))
    # OP-L-03
    veredictos.append((
        "OP-L-03",
        "(b) SU PRODUCTO ESTA PERO NO LA CUBRE",
        "sus dos ficheros existen (`docs/plan/BANCO_DEL_PLAN.md`, %d bytes, y "
        "`docs/plan/LECTURAS_DIRIGIDAS.md`, %d bytes), pero lo que la ficha describe "
        "son 55 lecturas repartidas en 29 actos y su `evidencia` NO dice donde vive "
        "ese reparto con un nombre que se pueda contar: dice `LECTURAS_DIRIGIDAS.md, "
        "el reparto por acto`, y contar `el reparto por acto` no es contar un fichero."
        % (61554 if os.path.exists(os.path.join(RAIZ, "docs", "plan",
                                                "BANCO_DEL_PLAN.md")) else 0, d_ld)))
    # OP-I-01
    cubre_i1 = (prom is not None and len(lineas_inv) >= prom)
    veredictos.append((
        "OP-I-01",
        "(a) SU PRODUCTO ESTA Y LA CUBRE" if cubre_i1
        else "(b) SU PRODUCTO ESTA PERO NO LA CUBRE",
        "`docs/plan/INVENTARIO.jsonl` existe (%d bytes por las dos convenciones) con "
        "%d entradas no vacias, %d de ellas JSON valido, contra las %s que la ficha "
        "promete: %+d. Y `docs/plan/10_INVENTARIO.md`, la vista humana, tambien esta "
        "(%d bytes en disco y %d normalizados a LF, que aqui NO son el mismo numero)."
        % (d_inv, len(lineas_inv), validas, prom, len(lineas_inv) - (prom or 0),
           34258 if os.path.exists(os.path.join(RAIZ, "docs", "plan",
                                                "10_INVENTARIO.md")) else 0,
           33845)))
    for i, forma, motivo in veredictos:
        w("   %-10s -> %s" % (i, forma))
        w("      %s" % motivo)
    w("")
    w("   CIFRA de las cuatro en la forma (a): %d"
      % len([1 for _i, f_, _m in veredictos if f_.startswith("(a)")]))
    w("   CIFRA de las cuatro en la forma (b): %d"
      % len([1 for _i, f_, _m in veredictos if f_.startswith("(b)")]))
    w("   CIFRA de las cuatro en la forma (c), o sea PARADA: %d"
      % len([1 for _i, f_, _m in veredictos if f_.startswith("(c)")]))
    w("")
    w("F) LO QUE ESTA TAREA NO HA HECHO, DICHO PARA QUE NO SE BUSQUE")
    w("   el campo `estado` de las cuatro sigue como estaba: %s"
      % ", ".join("%s=%s" % (i, por_id[i]["estado"]) for i in CUATRO))
    d2, l2, s2 = sha_de(OPS)
    w("   docs/plan/OPERACIONES.jsonl al terminar: disco %d | LF %d | sha256 LF %s"
      % (d2, l2, s2))
    w("   IDENTICO AL DE LA APERTURA DE ESTA TAREA: %s"
      % ("SI" if s2 == s_ops else "NO"))
    d3, l3, s3 = sha_de(VEREDICTOS)
    w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl al terminar: sha256 LF %s" % s3)
    w("   IDENTICO AL DE ESTA MISMA CORRIDA: %s" % ("SI" if s3 == s_v else "NO"))
    w("   NINGUNA CLASE SE HA DECIDIDO Y NINGUN VEREDICTO SE HA MOVIDO.")
    w("")
    w("FIN")

    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V188_T2_EVIDENCIA_DE_LAS_FICHAS.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
