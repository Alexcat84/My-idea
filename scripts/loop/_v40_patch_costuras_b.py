# -*- coding: utf-8 -*-
"""Segundo parche de la vuelta 40 sobre scripts/costuras_internas.py: las
funciones de medida, el diagnostico y la salida. Se corre UNA vez."""
import io

P = "scripts/costuras_internas.py"
s = io.open(P, encoding="utf-8").read()
n_orig = len(s)

# ---------------------------------------------------------------- EDIT 3
viejo = '''def medir_calibracion(ratio=None):
    """Mide los nodos de calibracion con las senales CRUDAS y dice quien entra.

    Devuelve (faltan, detalle): `faltan` son los ids que NO entran en la cola con
    los umbrales por defecto, y `detalle` trae la medicion de cada uno para que
    quien la imprima no tenga que volver a medir.
    """
    if ratio is None:
        from rapidfuzz.fuzz import token_sort_ratio as ratio
    nodos = json.loads(GRAFO.read_text(encoding="utf-8"))["nodos"]
    faltan, detalle = [], {}
    for nid in CALIBRACION:
        pasos = (nodos.get(nid) or {}).get("pasos_accionables") or []
        sp = _peor_pareja(ratio, pasos)
        sb = _mejor_bloque(ratio, pasos)
        entra = sp[0] >= UMBRAL_PAREJA
        if not isinstance(sb[0], NoAplica):
            entra = entra or (bool(sb[1]) and sb[0] >= UMBRAL_BLOQUE)
        detalle[nid] = {"pasos": len(pasos), "pareja": sp, "bloque": sb, "entra": entra}
        if not entra:
            faltan.append(nid)
    return faltan, detalle
'''
nuevo = '''def _ficha(ratio, nodos, nid):
    """La medicion de UN nodo con las senales CRUDAS, con su margen al lado.

    El margen es lo que le sobra a la senal de bloque por encima de su umbral, y
    existe para que un fixture al borde se pueda AVISAR antes de que caiga, en
    vez de descubrirse por un exit 1 a destiempo (la averia de la vuelta 34)."""
    pasos = (nodos.get(nid) or {}).get("pasos_accionables") or []
    sp = _peor_pareja(ratio, pasos)
    sb = _mejor_bloque(ratio, pasos)
    aplica = not isinstance(sb[0], NoAplica)
    entra = sp[0] >= UMBRAL_PAREJA
    if aplica:
        entra = entra or (bool(sb[1]) and sb[0] >= UMBRAL_BLOQUE)
    return {"pasos": len(pasos), "pareja": sp, "bloque": sb, "entra": entra,
            "existe": bool(nodos.get(nid)),
            "margen": (sb[0] - UMBRAL_BLOQUE) if aplica else None}


def medir_calibracion(ratio=None):
    """Mide los nodos de calibracion con las senales CRUDAS y dice quien entra.

    Devuelve (faltan, detalle): `faltan` son los ids que NO entran en la cola con
    los umbrales por defecto, y `detalle` trae la medicion de cada uno para que
    quien la imprima no tenga que volver a medir.
    """
    if ratio is None:
        from rapidfuzz.fuzz import token_sort_ratio as ratio
    nodos = json.loads(GRAFO.read_text(encoding="utf-8"))["nodos"]
    faltan, detalle = [], {}
    for nid in CALIBRACION:
        detalle[nid] = _ficha(ratio, nodos, nid)
        if not detalle[nid]["entra"]:
            faltan.append(nid)
    return faltan, detalle


def medir_retiradas(ratio=None):
    """Mide los fixtures RETIRADOS, que no gobiernan la puerta pero se siguen
    publicando. Un fixture retirado en silencio es una calibracion que nadie
    puede auditar, y si alguno vuelve a disparar hay que enterarse."""
    if ratio is None:
        from rapidfuzz.fuzz import token_sort_ratio as ratio
    nodos = json.loads(GRAFO.read_text(encoding="utf-8"))["nodos"]
    salida = []
    for r in CALIBRACION_RETIRADA:
        f = _ficha(ratio, nodos, r["node_id"])
        d = dict(r)
        d["medicion_de_hoy"] = f
        salida.append(d)
    return salida


def _texto_bloque(sb):
    """El bloque en texto, y NO APLICA nunca se maquilla como un cero."""
    if isinstance(sb[0], NoAplica):
        return "NO APLICA"
    return "%.1f (corte tras %d)" % (sb[0], sb[1])


def fixtures_al_borde(detalle, margen=MARGEN_DE_AVISO):
    """Los fixtures que SI entran pero por menos de `margen` puntos. El aviso que
    la puerta vieja no tenia: aviso, no fallo."""
    return [nid for nid, d in sorted(detalle.items())
            if d["entra"] and d["margen"] is not None and d["margen"] < margen]
'''
assert s.count(viejo) == 1, "EDIT 3 no ancla"
s = s.replace(viejo, nuevo)

# ---------------------------------------------------------------- EDIT 4
viejo = '''    print("INSTRUMENTO MAL CALIBRADO. No entrega nada.")
    print("  La calibracion conocida no aparece en la cola: %s" % err.faltan)
    for nid, d in sorted(err.detalle.items()):
        sp, sb = d["pareja"], d["bloque"]
        print("    %s: %d pasos, mejor pareja %.1f (pasos %d y %d), mejor bloque %s"
              % (nid, d["pasos"], sp[0], sp[1], sp[2],
                 ("NO APLICA" if isinstance(sb[0], NoAplica)
                  else "%.1f (corte tras %d)" % (sb[0], sb[1]))))
    print("  Umbrales usados: pareja %s, bloque %s" % (umbral_pareja, umbral_bloque))
'''
nuevo = '''    print("INSTRUMENTO MAL CALIBRADO. No entrega nada.")
    print("  La calibracion conocida no aparece en la cola: %s" % err.faltan)
    for nid, d in sorted(err.detalle.items()):
        sp, sb = d["pareja"], d["bloque"]
        print("    %s: %d pasos, mejor pareja %.1f (pasos %d y %d), mejor bloque %s"
              % (nid, d["pasos"], sp[0], sp[1], sp[2], _texto_bloque(sb)))
    print("  Umbrales usados: pareja %s, bloque %s" % (umbral_pareja, umbral_bloque))
    # EL CAMINO ESCRITO, ANADIDO EN LA VUELTA 40. La averia de la vuelta 34
    # vivio cinco vueltas en parte porque el diagnostico decia QUE fallaba y no
    # QUE HACER, y lo unico a mano era aflojar el umbral. Se dice aqui.
    print("")
    print("  QUE HACER, y que NO:")
    print("    NO se afloja el umbral para que el fixture entre: eso arregla la")
    print("    vara en vez de la pieza. Si la campana recorto el nodo por una")
    print("    operacion legitima, EL FIXTURE QUEDO RANCIO y se RETIRA DECLARADO")
    print("    en CALIBRACION_RETIRADA, con su motivo y su commit de origen, y")
    print("    se elige otro por el criterio escrito arriba de CALIBRACION.")
'''
assert s.count(viejo) == 1, "EDIT 4 no ancla"
s = s.replace(viejo, nuevo)

# ---------------------------------------------------------------- EDIT 5
viejo = '''    A("## La calibracion conocida")
    A("")
    for c in CALIBRACION:
        f = next(x for x in filas if x["node_id"] == c)
        A(f"**CAZADO** `{c}`: pareja **{f['sim_pareja']}**, bloque "
          f"**{f['sim_bloque_texto']}** con el corte **tras el paso {f['corte']}**.")
        A("")
'''
nuevo = '''    A("## La calibracion conocida")
    A("")
    A("**Los nodos contra los que se comprueba que el instrumento sigue cazando "
      "la clase para la que se construyo. Tienen que entrar TODOS**, y si falta "
      "uno el instrumento no entrega nada. **El criterio de eleccion esta escrito "
      "arriba de la lista en `scripts/costuras_internas.py`.**")
    A("")
    A("| fixture | pasos | pareja | bloque | corte | margen sobre el umbral |")
    A("|---|---:|---:|---:|---:|---:|")
    for c in CALIBRACION:
        f = next(x for x in filas if x["node_id"] == c)
        d = detalle_calib.get(c) or {}
        m = d.get("margen")
        A(f"| **CAZADO** `{c}` | {f['pasos']} | {f['sim_pareja']} | "
          f"{f['sim_bloque_texto']} | {f['corte']} | "
          f"{('%+.1f' % m) if m is not None else 'NO APLICA'} |")
    A("")
    borde = fixtures_al_borde(detalle_calib)
    if borde:
        A(f"> **AVISO DE BORDE: {len(borde)} fixture o mas esta a menos de "
          f"{MARGEN_DE_AVISO:.1f} puntos del umbral** ({', '.join('`%s`' % b for b in borde)}). "
          "**No es un fallo y no cambia nada hoy**, pero es el mismo sitio del que "
          "vino la averia de la vuelta 34: un fixture al borde cae con cualquier "
          "recorte legitimo del nodo. **Se dice para que la proxima se vea venir.**")
        A("")
    if CALIBRACION_RETIRADA:
        A("### Los fixtures RETIRADOS, que no se borran")
        A("")
        A("**No gobiernan la puerta, pero se siguen midiendo y publicando en cada "
          "corrida**: un fixture retirado en silencio es una calibracion que nadie "
          "puede auditar.")
        A("")
        A("| fixture retirado | cuando | por que | commit de origen | como quedo hoy |")
        A("|---|---|---|---|---|")
        for r in retiradas:
            f = r["medicion_de_hoy"]
            hoy = ("**VUELVE A DISPARAR**" if f["entra"] else "sigue sin disparar")
            A(f"| `{r['node_id']}` | {r['retirado']} | {r['motivo']} | "
              f"`{r['commit_de_origen']}` ({r['operacion']}) | {hoy}: "
              f"{f['pasos']} pasos, pareja {f['pareja'][0]:.1f}, bloque "
              f"{_texto_bloque(f['bloque'])} |")
        A("")
'''
assert s.count(viejo) == 1, "EDIT 5 no ancla"
s = s.replace(viejo, nuevo)

# ---------------------------------------------------------------- EDIT 6
viejo = '''    try:
        _asegurar_calibracion()
    except CalibracionRota as err:
        imprimir_calibracion_rota(err, args.umbral_pareja, args.umbral_bloque)
        return 1
'''
nuevo = '''    try:
        _asegurar_calibracion()
    except CalibracionRota as err:
        imprimir_calibracion_rota(err, args.umbral_pareja, args.umbral_bloque)
        return 1
    _faltan, detalle_calib = _CALIBRACION
    retiradas = medir_retiradas(ratio)
'''
assert s.count(viejo) == 1, "EDIT 6 no ancla"
s = s.replace(viejo, nuevo)

# ---------------------------------------------------------------- EDIT 7
viejo = '''    print(f"  nodos en la cola: {len(filas)} | escrito {SALIDA.name} y {RESUMEN.name}")
    print(f"  calibracion: los {len(CALIBRACION)} nodos conocidos, CAZADOS")
    return 0
'''
nuevo = '''    print(f"  nodos en la cola: {len(filas)} | escrito {SALIDA.name} y {RESUMEN.name}")
    print(f"  calibracion: los {len(CALIBRACION)} nodos conocidos, CAZADOS")
    for c in CALIBRACION:
        d = detalle_calib[c]
        m = d["margen"]
        print("    %-44s %d pasos | pareja %5.1f | bloque %-22s | margen %s"
              % (c, d["pasos"], d["pareja"][0], _texto_bloque(d["bloque"]),
                 ("%+.1f" % m) if m is not None else "NO APLICA"))
    for b in fixtures_al_borde(detalle_calib):
        print("  AVISO DE BORDE: el fixture %s entra por menos de %.1f puntos "
              "(margen %+.1f). No es un fallo; es el sitio del que vino la averia "
              "de la vuelta 34." % (b, MARGEN_DE_AVISO, detalle_calib[b]["margen"]))
    for r in retiradas:
        f = r["medicion_de_hoy"]
        print("  RETIRADO y NO borrado: %s (%s, commit %s) | hoy: bloque %s, %s"
              % (r["node_id"], r["retirado"], r["commit_de_origen"],
                 _texto_bloque(f["bloque"]),
                 "VUELVE A DISPARAR" if f["entra"] else "sigue sin disparar"))
    return 0
'''
assert s.count(viejo) == 1, "EDIT 7 no ancla"
s = s.replace(viejo, nuevo)

io.open(P, "w", encoding="utf-8", newline="\n").write(s)
print("EDITS 3 a 7 aplicados. %d -> %d caracteres" % (n_orig, len(s)))
