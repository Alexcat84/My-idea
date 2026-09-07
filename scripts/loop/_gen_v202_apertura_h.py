# -*- coding: utf-8 -*-
w("=== H. EL SUJETO DE LA TAREA 1: LA FICHA OP-L-03, SU EVIDENCIA Y LOS DOS ===")
w("    FICHEROS DEL REPARTO POR ACTO, MEDIDOS ANTES DE TOCAR NADA")
w("LA COORDENADA DE UNA FICHA JSONL ES LINEA MAS INDICE (acta 201, 4.4). AQUI SE")
w("   PUBLICAN LAS DOS NUMERACIONES DEL INDICE, la de base 0 de Python y la de")
w("   base 1 que el encargo usa, para que ninguna cita quede ambigua.")
mops = sha_de(OPERACIONES)
lin_ops = []
if mops is None:
    w("   ROJO: NO EXISTE %s" % OPERACIONES)
else:
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (OPERACIONES, mops[2], mops[3], mops[1][:16]))
    ruta_ops = os.path.join(RAIZ, OPERACIONES.replace("/", os.sep))
    lin_ops = io.open(ruta_ops, encoding="utf-8", errors="replace").read().split(NL)
    w("   CIFRA lineas NO VACIAS de OPERACIONES.jsonl: %d"
      % len([l for l in lin_ops if l.strip()]))
    aguja = chr(34) + "id_op" + chr(34) + ": " + chr(34) + FICHA_T1 + chr(34)
    hits = [i + 1 for i, l in enumerate(lin_ops) if l.strip() and aguja in l]
    w("   CIFRA lineas donde vive %s: %d | linea(s): %s"
      % (FICHA_T1, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
    if len(hits) == 1:
        d = json.loads(lin_ops[hits[0] - 1])
        w("   la ficha %s vive en la LINEA %d" % (FICHA_T1, hits[0]))
        w("   estado=%r  tipo=%r  fase=%r  fecha_corte=%r"
          % (d.get("estado"), d.get("tipo"), d.get("fase"), d.get("fecha_corte")))
        w("   CIFRA claves de la ficha: %d" % len(d))
        w("      %s" % ", ".join(sorted(d)))
        ev = d.get("evidencia", [])
        w("   CIFRA elementos de `evidencia`: %d" % len(ev))
        for i, e in enumerate(ev):
            w("      evidencia indice %d (elemento %d): %s" % (i, i + 1, repr(e)))
        ver = d.get("verificacion", [])
        w("   CIFRA elementos de `verificacion`: %d" % len(ver))
        for i, e in enumerate(ver):
            w("      verificacion indice %d (elemento %d), %d caracteres: %s"
              % (i, i + 1, len(str(e)), repr(e)[:200]))
        w("   CIFRA elementos de `evidencia` que NOMBRAN un fichero: %d"
          % len([x for x in ev
                 if re.search(r"[A-Za-z0-9_/.-]+\.(md|jsonl|py|json|txt)", str(x))]))
        w("   CIFRA elementos de `evidencia` que traen el literal %r: %d"
          % (LITERAL_REPARTO,
             len([x for x in ev if LITERAL_REPARTO in str(x)])))
    else:
        w("   ROJO: la ficha %s no aparece exactamente una vez. NO SE ACOTA A OJO."
          % FICHA_T1)
w("")
w("LAS DOS CIFRAS QUE EL ENCARGO MANDA MEDIR SOBRE EL DOCUMENTO QUE LA EVIDENCIA")
w("   NOMBRA. NO SE COPIAN DEL ENCARGO: SE CUENTAN AQUI.")
mdoc = sha_de(DOC_DE_LA_EVIDENCIA)
if mdoc is None:
    w("   ROJO: NO EXISTE %s" % DOC_DE_LA_EVIDENCIA)
else:
    ruta_doc = os.path.join(RAIZ, DOC_DE_LA_EVIDENCIA.replace("/", os.sep))
    t_doc = io.open(ruta_doc, encoding="utf-8", errors="replace").read()
    l_doc = t_doc.split(NL)
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (DOC_DE_LA_EVIDENCIA, mdoc[2], mdoc[3], mdoc[1][:16]))
    w("   CIFRA lineas por split(NL): %d | por count(NL): %d"
      % (len(l_doc), t_doc.count(NL)))
    w("   CIFRA apariciones del literal %r: %d"
      % (LITERAL_REPARTO, t_doc.count(LITERAL_REPARTO)))
    w("   CIFRA lineas que traen el literal %r: %d"
      % (LITERAL_REPARTO,
         len([l for l in l_doc if LITERAL_REPARTO in l])))
    w("   CIFRA apariciones de %r: %d" % (FICHA_T1, t_doc.count(FICHA_T1)))
    w("   CIFRA lineas que mencionan %r: %d"
      % (FICHA_T1, len([l for l in l_doc if FICHA_T1 in l])))
    w("   LA BUSQUEDA POSITIVA, PORQUE UNA BUSQUEDA NEGATIVA NO SE PUEDE CITAR")
    w("      (EJECUTOR.md 9). Variantes buscadas y su cuenta:")
    for var in ("reparto por acto", "reparto por", "por acto", "OP-L-03",
                "OP_L_03", "OP L 03"):
        w("      %-20s %d aparicion(es)" % (var, t_doc.count(var)))
w("")
w("LOS DOS FICHEROS QUE SI TRAEN EL REPARTO POR ACTO, MEDIDOS EN BYTES EXACTOS")
w("   (P.2: bytes exactos, nunca redondeados, KB solo entre parentesis y detras")
w("   del byte). SE MIDE TAMBIEN SU CONTENIDO: filas, actos distintos y lineas")
w("   que no son JSON.")
for fr in FICHEROS_DEL_REPARTO:
    mfr = sha_de(fr)
    if mfr is None:
        w("   %-38s NO EXISTE EN DISCO" % fr)
        continue
    ruta_fr = os.path.join(RAIZ, fr.replace("/", os.sep))
    t_fr = io.open(ruta_fr, encoding="utf-8", errors="replace").read()
    filas_fr = [l for l in t_fr.split(NL) if l.strip()]
    actos = []
    malas_fr = 0
    for l in filas_fr:
        try:
            dd = json.loads(l)
        except Exception:                                # noqa: BLE001
            malas_fr += 1
            continue
        if "acto" in dd:
            actos.append(dd["acto"])
    w("   %s" % fr)
    w("      disco %d bytes (%.1f KB) | LF %d bytes | sha256 LF %s"
      % (mfr[2], mfr[2] / 1024.0, mfr[3], mfr[1][:16]))
    w("      CIFRA filas no vacias: %d" % len(filas_fr))
    w("      CIFRA lineas que NO son JSON valido: %d" % malas_fr)
    w("      CIFRA filas con campo `acto`: %d" % len(actos))
    w("      CIFRA actos DISTINTOS: %d" % len(set(actos)))
    w("      los actos distintos, ordenados: %s"
      % ", ".join(sorted(set(actos))))
w("")
w("LA CIFRA QUE LA EVIDENCIA PROMETE, LEIDA DE LA PROPIA FICHA Y NO TECLEADA:")
if lin_ops:
    aguja = chr(34) + "id_op" + chr(34) + ": " + chr(34) + FICHA_T1 + chr(34)
    hh = [i + 1 for i, l in enumerate(lin_ops) if l.strip() and aguja in l]
    if len(hh) == 1:
        d = json.loads(lin_ops[hh[0] - 1])
        for i, e in enumerate(d.get("evidencia", [])):
            mm = re.search(r"(\d+)\s+pares?\s+en\s+(\d+)\s+actos?", str(e))
            if mm:
                w("   evidencia indice %d (elemento %d) promete %s pares en %s actos"
                  % (i, i + 1, mm.group(1), mm.group(2)))
                w("      su literal entero: %s" % repr(e))
w("")

w("=== H.1 EL SUJETO DE LAS TAREAS 2 Y 3: LOS DOS INSTRUMENTOS DE OP-L-02, ===")
w("    EL CRITERIO DE HECHO Y LA TABLA VIVA DE LOS PUROS")
w("LOS DOS INSTRUMENTOS SE IMPORTAN Y NO SE CLONAN (encargo de esta vuelta). AQUI")
w("   SE MIDEN Y SE LEEN PARA COMPROBAR SI ESCRIBEN FICHEROS, que es lo que el")
w("   encargo manda comprobar ANTES de correrlos.")
for ins in INSTRUMENTOS_OP_L_02:
    mi = sha_de(ins)
    if mi is None or mi[2] == 0:
        w("   ROJO: %s NO EXISTE o mide CERO BYTES." % ins)
        continue
    ruta_i = os.path.join(RAIZ, ins.replace("/", os.sep))
    t_i = io.open(ruta_i, encoding="utf-8", errors="replace").read()
    l_i = t_i.split(NL)
    aciertos = [(j + 1, l.strip()) for j, l in enumerate(l_i)
                if PATRON_ESCRITURA.search(l)]
    w("   %s" % ins)
    w("      disco %d bytes | LF %d bytes | sha256 LF %s"
      % (mi[2], mi[3], mi[1][:16]))
    w("      CIFRA lineas por count(NL): %d" % t_i.count(NL))
    w("      CIFRA lineas con marca de ESCRITURA en disco: %d" % len(aciertos))
    for j, l in aciertos[:12]:
        w("         linea %d: %s" % (j, l[:110]))
    if not aciertos:
        w("         (ninguna: el instrumento SOLO MIDE, no escribe ficheros)")
    w("      CIFRA apariciones del literal 46208790 (el HEAD sellado en la 170): %d"
      % t_i.count("46208790"))
    for j, l in enumerate(l_i):
        if "46208790" in l:
            w("         linea %d: %s" % (j + 1, l.strip()[:120]))
w("")
w("EL CRITERIO DE HECHO, LOCALIZADO POR LINEA Y NO CITADO DE MEMORIA:")
mcri = sha_de(CRITERIO_DE_HECHO)
if mcri is None:
    w("   ROJO: NO EXISTE %s" % CRITERIO_DE_HECHO)
else:
    ruta_c = os.path.join(RAIZ, CRITERIO_DE_HECHO.replace("/", os.sep))
    t_c = io.open(ruta_c, encoding="utf-8", errors="replace").read()
    l_c = t_c.split(NL)
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (CRITERIO_DE_HECHO, mcri[2], mcri[3], mcri[1][:16]))
    w("   CIFRA lineas por count(NL): %d" % t_c.count(NL))
    for aguja in ("CRITERIO DE HECHO", "criterio de hecho", "OP-L-01",
                  "OP-L-02", "OP-L-03"):
        hits = [j + 1 for j, l in enumerate(l_c) if aguja in l]
        w("   %-20s %d linea(s): %s"
          % (aguja, len(hits),
             ", ".join(str(x) for x in hits[:16]) or "(ninguna)"))
w("")
w("LA TABLA VIVA DE LOS PUROS Y SU LITERAL DE VIGENCIA, MEDIDOS AL ENTRAR:")
mban = sha_de(BANCO)
if mban is None:
    w("   ROJO: NO EXISTE %s" % BANCO)
else:
    ruta_b = os.path.join(RAIZ, BANCO.replace("/", os.sep))
    t_b = io.open(ruta_b, encoding="utf-8", errors="replace").read()
    l_b = t_b.split(NL)
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (BANCO, mban[2], mban[3], mban[1][:16]))
    w("   CIFRA lineas por split(NL): %d | por count(NL): %d"
      % (len(l_b), t_b.count(NL)))
    w("   EL ENCARGO NOMBRA LA LINEA %d. Su contenido, leido y no supuesto:"
      % LINEA_TABLA_VIVA)
    if len(l_b) >= LINEA_TABLA_VIVA:
        w("      linea %d: %s" % (LINEA_TABLA_VIVA, l_b[LINEA_TABLA_VIVA - 1][:200]))
    else:
        w("      ROJO: el fichero tiene menos de %d lineas" % LINEA_TABLA_VIVA)
    hits = [j + 1 for j, l in enumerate(l_b) if LITERAL_VIGENCIA in l]
    w("   CIFRA lineas con el literal %r: %d | linea(s): %s"
      % (LITERAL_VIGENCIA, len(hits),
         ", ".join(str(x) for x in hits[:16]) or "(ninguna)"))
    for x in hits[:8]:
        w("      linea %d: %s" % (x, l_b[x - 1].strip()[:180]))
    hits2 = [j + 1 for j, l in enumerate(l_b) if "TABLA VIVA" in l]
    w("   CIFRA lineas con el literal TABLA VIVA: %d | linea(s): %s"
      % (len(hits2), ", ".join(str(x) for x in hits2[:16]) or "(ninguna)"))
w("")

w("=== H.2 EL SUJETO DE LA TAREA 4: LAS ACTAS 173 Y 174, ACOTADAS AQUI, Y ===")
w("    SUS REPORTES ARCHIVADOS, MEDIDOS CON os.path.isfile Y os.path.getsize")
ma = sha_de(ACTA)
if ma is None:
    w("   ROJO: no existe %s" % ACTA)
else:
    w("   %s: %d bytes disco | %d bytes LF | sha256 LF %s"
      % (ACTA, ma[2], ma[3], ma[1][:16]))
    ruta_acta = os.path.join(RAIZ, ACTA.replace("/", os.sep))
    lineas_acta = io.open(ruta_acta, encoding="utf-8",
                          errors="replace").read().split(NL)
    w("   CIFRA lineas del acta por split(NL): %d" % len(lineas_acta))
    for v in ACTAS_DE_LA_DEUDA + [201, 202]:
        hits = [i + 1 for i, l in enumerate(lineas_acta)
                if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA %d\b" % v, l)
                or re.match(r"^#\s*ACTA DE LA VUELTA %d DEL AUDITOR\b" % v, l)]
        w("   cabecera de la VUELTA %d: %d acierto(s), linea(s) %s"
          % (v, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
    for v in ACTAS_DE_LA_DEUDA:
        ini = [i for i, l in enumerate(lineas_acta)
               if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA %d\b" % v, l)
               or re.match(r"^#\s*ACTA DE LA VUELTA %d DEL AUDITOR\b" % v, l)]
        if len(ini) != 1:
            w("   ROJO: la cabecera del acta %d no aparece exactamente una vez." % v)
            continue
        i0 = ini[0]
        sig = [i for i in range(i0 + 1, len(lineas_acta))
               if re.match(r"^#\s+ACTA\b", lineas_acta[i])]
        i1 = sig[0] if sig else len(lineas_acta)
        w("   CUERPO ACOTADO del acta %d: lineas %d a %d (1-indexadas), %d lineas"
          % (v, i0 + 1, i1, i1 - i0))
        cuerpo = lineas_acta[i0:i1]
        secc = {}
        for j, l in enumerate(cuerpo):
            mm = re.match(r"^#{2,4}\s*(\d+)(?:\.(\d+))?\b", l)
            if mm:
                secc.setdefault(mm.group(1), []).append(i0 + j + 1)
        for k in sorted(secc, key=lambda x: int(x)):
            w("      seccion %s: %d cabecera(s) en linea(s) %s"
              % (k, len(secc[k]), ", ".join(str(x) for x in secc[k][:20])))
        claves_p = sorted(set(re.findall(r"P\.(\d+)", NL.join(cuerpo))), key=int)
        w("      CIFRA claves P.n distintas nombradas en el cuerpo: %d (%s)"
          % (len(claves_p), ", ".join("P." + x for x in claves_p) or "(ninguna)"))
w("")
w("LOS REPORTES ARCHIVADOS DE LA DEUDA, MEDIDOS Y NO RECORDADOS:")
dir_rep = os.path.join(LOOP, "reportes")
for v in ACTAS_DE_LA_DEUDA:
    rel_rep = "docs/loop/reportes/REPORTE_V%d.md" % v
    ruta_rep = os.path.join(RAIZ, rel_rep.replace("/", os.sep))
    existe = os.path.isfile(ruta_rep)
    w("   %-40s os.path.isfile: %s | os.path.getsize: %s"
      % (rel_rep, "SI" if existe else "NO",
         (str(os.path.getsize(ruta_rep)) + " bytes") if existe
         else "NO MEDIBLE, no hay fichero"))
archivados = sorted(n for n in os.listdir(dir_rep)
                    if re.match(r"^REPORTE_V\d+\.md$", n))
nums_rep = sorted(int(re.match(r"^REPORTE_V(\d+)\.md$", n).group(1))
                  for n in archivados)
w("   CIFRA reportes archivados en docs/loop/reportes/: %d" % len(archivados))
w("   rango %d a %d" % (min(nums_rep), max(nums_rep)))
faltan_rep = [n for n in range(min(nums_rep), max(nums_rep) + 1)
              if n not in nums_rep]
w("   CIFRA vueltas del rango SIN reporte archivado: %d" % len(faltan_rep))
w("      cuales: %s" % (", ".join(str(n) for n in faltan_rep) or "(ninguna)"))
faltan_168_199 = [n for n in range(168, 200) if n not in nums_rep]
w("   CIFRA vueltas del rango 168 a 199 SIN reporte archivado: %d"
  % len(faltan_168_199))
w("      cuales: %s" % (", ".join(str(n) for n in faltan_168_199) or "(ninguna)"))
mpen = sha_de(PENDIENTES)
if mpen is None:
    w("   ROJO: NO EXISTE %s" % PENDIENTES)
else:
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (PENDIENTES, mpen[2], mpen[3], mpen[1][:16]))
w("")

w("=== H.3 EL INVENTARIO Y LAS CUATRO FICHAS REALES, MEDIDOS ANTES DE TOCAR ===")
w("    NADA, Y LA VARA DEL TRABAJO PENDIENTE CORRIDA CON EL HEAD DE APERTURA")
minv = sha_de(INVENTARIO_JSONL)
if minv is None:
    w("   ROJO: NO EXISTE %s" % INVENTARIO_JSONL)
else:
    ruta_inv = os.path.join(RAIZ, INVENTARIO_JSONL.replace("/", os.sep))
    t_inv = io.open(ruta_inv, encoding="utf-8", errors="replace").read()
    l_inv = [l for l in t_inv.split(NL) if l.strip()]
    w("   %s: %d bytes disco | %d LF | sha256 LF %s"
      % (INVENTARIO_JSONL, minv[2], minv[3], minv[1][:16]))
    w("   CIFRA lineas NO VACIAS (las entradas): %d" % len(l_inv))
w("   LAS CUATRO FICHAS REALES, LOCALIZADAS POR LINEA EN %s:" % OPERACIONES)
if lin_ops:
    for idop in FICHAS_REALES:
        aguja = chr(34) + "id_op" + chr(34) + ": " + chr(34) + idop + chr(34)
        hits = [i + 1 for i, l in enumerate(lin_ops) if l.strip() and aguja in l]
        w("      %-9s %d linea(s): %s"
          % (idop, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
        if len(hits) == 1:
            d = json.loads(lin_ops[hits[0] - 1])
            w("         estado=%r  tipo=%r  fase=%r"
              % (d.get("estado"), d.get("tipo"), d.get("fase")))
            w("         CIFRA elementos de `verificacion`: %d"
              % len(d.get("verificacion", [])))
            w("         CIFRA elementos de `evidencia`: %d"
              % len(d.get("evidencia", [])))
w("   LOS CUATRO DOCUMENTOS QUE LA VARA NOMBRA, EN BYTES EXACTOS (P.2):")
for doc in DOCUMENTOS_DE_LA_VARA:
    md = sha_de(doc)
    if md is None:
        w("      %-38s NO EXISTE EN DISCO" % doc)
        continue
    ruta_d = os.path.join(RAIZ, doc.replace("/", os.sep))
    td = io.open(ruta_d, encoding="utf-8", errors="replace").read()
    w("      %-38s disco %8d bytes | LF %8d bytes | sha256 LF %s | %d lineas "
      "por count(NL)" % (doc, md[2], md[3], md[1][:16], td.count(NL)))
w("")
w("   LA VARA DEL TRABAJO PENDIENTE, CORRIDA AQUI CON EL HEAD DE APERTURA COMO")
w("   CORTE. LA VARA NO SE CLONA Y NO SE TOCA: SE INVOCA.")
mv = sha_de(VARA_DEL_PLAN)
if mv is None or mv[2] == 0:
    w("   ROJO: la vara %s NO EXISTE o mide CERO BYTES." % VARA_DEL_PLAN)
else:
    w("   vara: %s" % VARA_DEL_PLAN)
    w("      %d bytes disco | %d LF | sha256 LF %s" % (mv[2], mv[3], mv[1][:16]))
    w("   comando: python %s --corte %s" % (VARA_DEL_PLAN, head[:8]))
    c_v, sal_vara = correr([PY, VARA_DEL_PLAN, "--corte", head])
    io.open(os.path.join(LOOP, "SALIDA_V%d_VARA_DEL_PLAN.txt" % VUELTA), "w",
            encoding="utf-8", newline=NL).write(sal_vara)
    w("   exitcode: %d" % c_v)
    w("   sellada en docs/loop/SALIDA_V%d_VARA_DEL_PLAN.txt (%d bytes)"
      % (VUELTA, len(sal_vara.encode("utf-8"))))
    for l in sal_vara.split(NL):
        if l.strip().startswith("CIFRA"):
            w("   | " + l.strip()[:150])
w("")
