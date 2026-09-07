# -*- coding: utf-8 -*-
r"""_v202_t2_op_l_02.py . `OP-L-02` CONTRA EL CRITERIO DE HECHO (TAREA 2 de la
vuelta 202).

PREFIJO DE GUION BAJO: computo de UNA vuelta, fuera del censo y fuera de la
nomina, que no vigila a nadie (adjudicacion `4.5` del acta 199). LA MORATORIA
(`AUDITOR.md` 6.3) NO SE TOCA: **no se clona ni se modifica ningun instrumento**.
Los dos que esta tarea necesita se **IMPORTAN Y SE CORREN TAL CUAL**, y sus
salidas se sellaron con nombre de esta vuelta ANTES de que este fichero corra:

  . `scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py`
  . `scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py`

LO QUE ESTE FICHERO HACE, Y ES SOLO LEER Y MEDIR:

  A) CITA EL CRITERIO DE HECHO POR LINEA, leyendolo de
     `docs/plan/08_VERIFICACION.md` y no de memoria.
  B) CITA LAS TRES CLAUSULAS POR LINEA MAS INDICE (linea 42 de
     `docs/plan/OPERACIONES.jsonl` mas el indice del elemento), separando la
     CORRECCION DECLARADA, que no es una clausula que cumplir.
  C) LEE LOS VEREDICTOS DE LAS SALIDAS SELLADAS de esta vuelta, sin teclearlos.
  D) REMIDE LA CLAUSULA 2 CONTRA EL HEAD DE APERTURA DE ESTA VUELTA, leido del
     sello propio `docs/loop/SALIDA_V202_HEAD_APERTURA.txt` y NO tecleado, y
     PUBLICA LAS DOS LECTURAS JUNTAS con la discrepancia declarada. El
     instrumento diffea contra `46208790`, que es un HEAD sellado en la vuelta
     170; el acta 201 ya lo declaro FALSO ROJO en su `4.2` y su reparacion es de
     codigo. AQUI NO SE ARREGLA.
  E) APLICA EL CRITERIO DE HECHO A CADA CLAUSULA: *una fase esta hecha cuando su
     verificacion SE CAERIA si el fallo volviera*. Se comprueba LEYENDO EL CODIGO
     DEL INSTRUMENTO, sin tocarlo, que cada veredicto sale de una VARIABLE
     COMPUTADA y no de un literal, que es la comprobacion barata que el propio
     criterio nombra: *correr la prueba antes del arreglo; si pasa, no prueba
     nada*.

Y NO CIERRA NADA: si de la lectura sale que la ficha esta cumplida, SE PROPONE
CON SU EVIDENCIA Y LO ADJUDICA EL AUDITOR. El campo `estado` no se mueve.

USO:
  python scripts/loop/_v202_t2_op_l_02.py
"""
import io
import json
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

OPERACIONES = "docs/plan/OPERACIONES.jsonl"
CRITERIO = "docs/plan/08_VERIFICACION.md"
VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
SELLO_PROPIO = "docs/loop/SALIDA_V202_HEAD_APERTURA.txt"
SELLO_DEL_170 = "docs/loop/SALIDA_V170_HEAD_APERTURA.txt"
INSTRUMENTOS = [
    "scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py",
    "scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py",
]
SELLADAS = [
    "docs/loop/SALIDA_V202_T2_COBERTURA_169.txt",
    "docs/loop/SALIDA_V202_T2_VEREDICTO_170.txt",
]
ID_OP = "OP-L-02"
LINEA_DE_LA_FICHA = None      # SE MIDE, NO SE TECLEA.
MARCA_CORRECCION = "CORRECCION DECLARADA"


def leer(rel):
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(ruta):
        return None
    crudo = io.open(ruta, "rb").read()
    return crudo.replace(b"\r\n", b"\n").decode("utf-8", errors="replace")


def medir(rel):
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(ruta):
        return None
    crudo = io.open(ruta, "rb").read()
    return len(crudo), len(crudo.replace(b"\r\n", b"\n"))


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 202, TAREA 2 . OP-L-02 CONTRA EL CRITERIO DE HECHO")
    w("LECTURA MEDIDA. NO SE CIERRA NADA Y NINGUN estado SE MUEVE.")
    w("=" * 78)
    w("")

    w("A) LOS DOS INSTRUMENTOS: IMPORTADOS Y CORRIDOS TAL CUAL, NO CLONADOS")
    w("   La moratoria (AUDITOR.md 6.3) prohibe fabricar y prohibe tocar. Aqui")
    w("   se comprueba que NINGUNO ESCRIBE FICHEROS, como hizo el auditor, y")
    w("   que sus selladas de ESTA vuelta existen y no estan vacias.")
    for ins, sell in zip(INSTRUMENTOS, SELLADAS):
        mi, ms = medir(ins), medir(sell)
        t_i = leer(ins) or ""
        # LA MARCA DE ESCRITURA: las mismas familias que el sello de apertura.
        escrituras = [j + 1 for j, l in enumerate(t_i.split(NL))
                      if re.search(r"\.write\s*\(|json\.dump\s*\(|os\.remove|"
                                   r"shutil\.|os\.rename|os\.makedirs", l)]
        w("   %s" % ins)
        w("      %d bytes en disco | %d bytes normalizados a LF"
          % (mi[0], mi[1]) if mi else "      NO EXISTE")
        w("      CIFRA lineas con marca de escritura en disco: %d %s"
          % (len(escrituras), escrituras or ""))
        if ms is None:
            w("      ROJO: la sellada %s NO EXISTE." % sell)
        elif ms[0] == 0:
            w("      ROJO: la sellada %s mide CERO BYTES." % sell)
        else:
            w("      sellada: %s, %d bytes en disco | %d bytes en LF"
              % (sell, ms[0], ms[1]))
    c, est = git(["status", "--porcelain"])
    sucios = [l for l in est.splitlines()
              if l.strip() and "SALIDA_V202_T2" not in l and "_v202_t2" not in l]
    w("   CIFRA lineas de git status que NO son salidas de esta tarea: %d"
      % len(sucios))
    for l in sucios[:10]:
        w("      " + l)
    if not sucios:
        w("      (ninguna: correrlos NO ensucio el arbol)")
    w("")

    w("B) EL CRITERIO DE HECHO, CITADO POR LINEA Y NO DE MEMORIA")
    t_cri = leer(CRITERIO)
    m_cri = medir(CRITERIO)
    l_cri = t_cri.split(NL)
    w("   %s: %d bytes en disco | %d bytes normalizados a LF | %d lineas"
      % (CRITERIO, m_cri[0], m_cri[1], t_cri.count(NL)))
    cab = [i + 1 for i, l in enumerate(l_cri)
           if l.startswith("## EL CRITERIO DE HECHO")]
    w("   cabecera del criterio: %d acierto(s), linea(s) %s"
      % (len(cab), ", ".join(str(x) for x in cab) or "(ninguna)"))
    for i in range(cab[0] - 1, min(cab[0] + 9, len(l_cri))):
        if l_cri[i].strip():
            w("      linea %d: %s" % (i + 1, l_cri[i].strip()))
    hits_op = [i + 1 for i, l in enumerate(l_cri) if ID_OP in l]
    w("   lineas de %s que NOMBRAN %s: %d, linea(s) %s"
      % (CRITERIO, ID_OP, len(hits_op),
         ", ".join(str(x) for x in hits_op) or "(ninguna)"))
    for x in hits_op:
        w("      linea %d: %s" % (x, l_cri[x - 1].strip()[:190]))
    w("")

    w("C) LAS TRES CLAUSULAS, CITADAS POR LINEA MAS INDICE (acta 201, 4.4)")
    t_ops = leer(OPERACIONES)
    lin_ops = t_ops.split(NL)
    aguja = chr(34) + "id_op" + chr(34) + ": " + chr(34) + ID_OP + chr(34)
    hits = [i + 1 for i, l in enumerate(lin_ops) if l.strip() and aguja in l]
    w("   CIFRA lineas donde vive %s: %d | linea(s): %s"
      % (ID_OP, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
    if len(hits) != 1:
        w("   ROJO: la ficha no aparece exactamente una vez. NO SE MIDE A OJO.")
        print(NL.join(L))
        return 1
    ln = hits[0]
    d = json.loads(lin_ops[ln - 1])
    ver = d.get("verificacion", [])
    ev = d.get("evidencia", [])
    w("   la ficha %s vive en la LINEA %d" % (ID_OP, ln))
    w("   estado (SE LEE, NO SE MUEVE): %r | tipo: %r | fecha_corte: %r"
      % (d.get("estado"), d.get("tipo"), d.get("fecha_corte")))
    w("   CIFRA elementos de `verificacion`: %d" % len(ver))
    w("   CIFRA elementos de `evidencia`: %d" % len(ev))
    clausulas, correcciones = [], []
    for i, x in enumerate(ver):
        (correcciones if MARCA_CORRECCION in str(x) else clausulas).append((i, x))
    w("   CIFRA clausulas propiamente dichas: %d" % len(clausulas))
    w("   CIFRA correcciones declaradas (no son clausulas que cumplir): %d"
      % len(correcciones))
    for i, x in clausulas:
        w("      linea %d + indice %d (elemento %d), %d caracteres:"
          % (ln, i, i + 1, len(str(x))))
        w("         %r" % x)
    for i, x in correcciones:
        w("      CORRECCION DECLARADA en linea %d + indice %d (elemento %d), "
          "%d caracteres" % (ln, i, i + 1, len(str(x))))
    w("")

    w("D) LOS VEREDICTOS DEL INSTRUMENTO, LEIDOS DE SU SELLADA DE ESTA VUELTA")
    t_ver = leer(SELLADAS[1]) or ""
    leidos = dict(re.findall(r"VEREDICTO CLAUSULA (\d+): (CUMPLIDA|NO CUMPLIDA)",
                             t_ver))
    for k in sorted(leidos):
        w("   clausula %s: %s" % (k, leidos[k]))
    m_cnt = re.search(r"CIFRA clausulas cumplidas: (\d+) de (\d+)", t_ver)
    w("   CIFRA clausulas cumplidas segun el instrumento: %s de %s"
      % (m_cnt.group(1), m_cnt.group(2)) if m_cnt else "   (no impresa)")
    m_sin = re.search(r"CIFRA pares SIN veredicto en las SEIS nominas: (\d+)",
                      t_ver)
    w("   CIFRA pares SIN veredicto en las seis nominas: %s"
      % (m_sin.group(1) if m_sin else "(no impresa)"))
    m_gr = re.search(r"CIFRA grupos SIN motivo escrito: (\d+)", t_ver)
    w("   CIFRA grupos del backlog SIN motivo escrito: %s"
      % (m_gr.group(1) if m_gr else "(no impresa)"))
    w("")

    w("E) LA CLAUSULA 2, REMEDIDA CONTRA EL HEAD DE APERTURA DE ESTA VUELTA.")
    w("   LAS DOS LECTURAS SE PUBLICAN JUNTAS Y LA DISCREPANCIA SE DECLARA.")
    head_170 = (leer(SELLO_DEL_170) or "").strip()
    head_202 = (leer(SELLO_PROPIO) or "").strip()
    w("   HEAD que el instrumento usa, leido de %s: %s"
      % (SELLO_DEL_170, head_170[:8] or "(no hay sello)"))
    w("   HEAD de apertura de ESTA vuelta, leido de %s: %s"
      % (SELLO_PROPIO, head_202[:8] or "(no hay sello)"))
    w("   LOS DOS SELLOS SE LEEN DE DISCO. NINGUNO SE TECLEA.")
    if len(head_202) != 40:
        w("   ROJO: el sello propio no trae un hash de 40 caracteres.")
        print(NL.join(L))
        return 1
    lecturas = []
    for etiqueta, h in (("la del instrumento (HEAD de la vuelta 170)", head_170),
                        ("la de esta vuelta (HEAD de apertura de la 202)",
                         head_202)):
        if not h:
            w("   %-48s SIN SELLO, no se mide" % etiqueta)
            continue
        c, dif = git(["diff", h, "HEAD", "--numstat", "--", VEREDICTOS])
        filas = [l for l in dif.splitlines() if l.strip()]
        c2, dif2 = git(["diff", "--numstat", "--", VEREDICTOS])
        filas2 = [l for l in dif2.splitlines() if l.strip()]
        w("   %s" % etiqueta)
        w("      comando: git diff %s HEAD --numstat -- %s" % (h[:8], VEREDICTOS))
        w("      CIFRA filas del numstat: %d" % len(filas))
        for l in filas:
            w("         " + l)
        w("      y sin commitear (arbol de trabajo): %d filas" % len(filas2))
        veredicto = (len(filas) == 0 and len(filas2) == 0)
        w("      LECTURA DE LA CLAUSULA 2: %s"
          % ("CUMPLIDA" if veredicto else "NO CUMPLIDA"))
        lecturas.append((etiqueta, len(filas), veredicto))
    if len(lecturas) == 2 and lecturas[0][2] != lecturas[1][2]:
        w("   LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO:")
        w("      contra %s salen %d filas y la clausula sale %s"
          % (head_170[:8], lecturas[0][1],
             "CUMPLIDA" if lecturas[0][2] else "NO CUMPLIDA"))
        w("      contra %s salen %d filas y la clausula sale %s"
          % (head_202[:8], lecturas[1][1],
             "CUMPLIDA" if lecturas[1][2] else "NO CUMPLIDA"))
        w("      EL ACTA 201 YA LO ADJUDICO EN SU 4.2: es FALSO ROJO, porque el")
        w("      instrumento diffea contra un HEAD sellado en la vuelta 170 y")
        w("      desde entonces han pasado vueltas que SI movieron el fichero.")
        w("      SU REPARACION ES DE CODIGO Y LA MORATORIA LA PROHIBE HOY.")
    else:
        w("   LAS DOS LECTURAS COINCIDEN. No hay discrepancia que declarar.")
    w("")
    w("   EL MARCADOR, RECONTADO AQUI Y NO COPIADO. P.1 manda pasar por el")
    w("   resolutor todo conteo que TOQUE IDS; contar filas y clases del")
    w("   archivo NO toca ningun id, asi que NO pasa por el resolutor, y eso")
    w("   se dice en vez de callarlo.")
    t_v = leer(VEREDICTOS)
    m_v = medir(VEREDICTOS)
    filas_v = [l for l in t_v.split(NL) if l.strip()]
    clases, malas_v, puestos = {}, 0, []
    for l in filas_v:
        try:
            r = json.loads(l)
        except Exception:                                    # noqa: BLE001
            malas_v += 1
            continue
        clases[r.get("clase")] = clases.get(r.get("clase"), 0) + 1
        # EL NOMBRE DE LA CLAVE SE MIDE, NO SE SUPONE. La clave del puesto en
        # este archivo es `puesto_intra` y no `puesto`; la primera version de
        # este computo miro `puesto`, publico 0 puestos distintos y era una
        # cifra falsa por buscar una clave que no existe. CORRECCION DECLARADA
        # de este mismo fichero, escrita aqui y no tapada.
        for clave_puesto in ("puesto_intra", "puesto"):
            if clave_puesto in r:
                puestos.append(int(r[clave_puesto]))
                break
    w("      %s: %d bytes en disco | %d bytes normalizados a LF"
      % (VEREDICTOS, m_v[0], m_v[1]))
    w("      CIFRA filas no vacias: %d" % len(filas_v))
    w("      CIFRA lineas que NO son JSON valido: %d" % malas_v)
    w("      EL REPARTO POR CLASE: %s"
      % ", ".join("%s %d" % (k, clases[k]) for k in sorted(clases, key=str)))
    w("      SUMA DEL REPARTO: %d" % sum(clases.values()))
    w("      CIFRA puestos distintos: %d | maximo: %s | huecos: %s"
      % (len(set(puestos)), max(puestos) if puestos else "(ninguno)",
         (max(puestos) - len(set(puestos))) if puestos else "(no medibles)"))
    w("      CORRECCION DECLARADA de este mismo fichero: la primera version")
    w("      buscaba la clave `puesto` y publicaba 0 puestos distintos. La")
    w("      clave de este archivo se llama `puesto_intra`, y el 0 no era una")
    w("      medicion sino el sintoma de mirar donde no hay nada.")
    w("      LA CLAUSULA PIDE QUE LA OPERACION NO LO MUEVA, no que valga 2.117")
    w("      hoy, y su propia CORRECCION DECLARADA lo dice: el 2.117 es el")
    w("      valor en la fecha_corte de la ficha, TESTIGO Y NO CONDICION.")
    w("")

    w("F) EL CRITERIO DE HECHO APLICADO A LAS TRES CLAUSULAS")
    w("   EL CRITERIO PIDE QUE LA VERIFICACION SE CAERIA SI EL FALLO VOLVIERA,")
    w("   y trae su propia comprobacion barata: correr la prueba antes del")
    w("   arreglo, y si pasa, no prueba nada. AQUI SE COMPRUEBA LEYENDO EL")
    w("   CODIGO DEL INSTRUMENTO, SIN TOCARLO, que cada veredicto sale de una")
    w("   VARIABLE COMPUTADA y no de un literal, que es lo que EJECUTOR.md 1")
    w("   llama un caso rojo que no puede fallar.")
    t_ins = leer(INSTRUMENTOS[1])
    l_ins = t_ins.split(NL)
    for k in ("1", "2", "3"):
        asig = [(j + 1, l.strip()) for j, l in enumerate(l_ins)
                if re.match(r"\s*cumple%s\s*=" % k, l)]
        w("   clausula %s:" % k)
        for j, l in asig:
            w("      %s linea %d: %s" % (INSTRUMENTOS[1], j, l[:150]))
            literal = re.match(r"cumple%s\s*=\s*[\"']" % k, l) is not None
            w("      el veredicto sale de un LITERAL: %s"
              % ("SI, y entonces no prueba nada" if literal
                 else "NO, sale de una expresion computada"))
        if not asig:
            w("      ROJO: no se encontro la asignacion del veredicto.")
    w("")

    w("G) LA PROPUESTA, QUE NO CIERRA NADA")
    cumplidas_inst = [k for k in sorted(leidos) if leidos[k] == "CUMPLIDA"]
    w("   SEGUN EL INSTRUMENTO, TAL CUAL SE CORRIO: %d de %d clausulas cumplidas"
      % (len(cumplidas_inst), len(leidos)))
    con_remedida = set(cumplidas_inst)
    if len(lecturas) == 2 and lecturas[1][2]:
        con_remedida.add("2")
    w("   CON LA CLAUSULA 2 REMEDIDA CONTRA EL HEAD DE ESTA VUELTA: %d de %d"
      % (len(con_remedida), len(leidos)))
    w("   LAS TRES QUEDAN CUMPLIDAS: %s"
      % ("SI" if len(con_remedida) == len(leidos) else "NO"))
    w("   Y AUN ASI NO SE CIERRA: el encargo dice PROPONLO Y NO LO CIERRES, y")
    w("   AUDITOR.md 0 dice que el campo estado no es la vara. El estado de")
    w("   %s entra y sale en %r." % (ID_OP, d.get("estado")))
    t_ops_fin = leer(OPERACIONES)
    w("   CIFRA lineas de %s que este fichero cambia: %d"
      % (OPERACIONES, 0 if t_ops_fin == t_ops else 1))
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V202_T2_OP_L_02.txt"), "w",
            encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
