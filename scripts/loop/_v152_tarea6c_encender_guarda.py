# -*- coding: utf-8 -*-
"""VUELTA 152, TAREA 6.c: ENCENDER LA MITAD DE BIDIRECCIONALES DE `OP-C-05` EN
GATE 0, COMO REGISTRO DE CITAS.

Parchea scripts/run_phase1.py por sustitucion exacta, ANADIENDO el check nuevo
detras del de duplicadas y SIN borrar una linea del comentario viejo: el bloque
que decia "LO QUE ESTA GUARDA NO CUBRE" se queda entero y debajo se escribe la
correccion declarada que dice que ya lo cubre y por que decision.

USO:
  python scripts/loop/_v152_tarea6c_encender_guarda.py
"""
import io
import os
import py_compile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUARDA = os.path.join(RAIZ, "scripts", "run_phase1.py")

ANCLA = """    # ── FIN OP-C-05 ────────────────────────────────────────────
"""

NUEVO = '''    # ── OP-C-05, SEGUNDA MITAD: EL REGISTRO DE CITAS ───────────────────
    # CORRECCION DECLARADA (2026-09-02, vuelta 152, TAREA 6.c). EL COMENTARIO
    # DE ARRIBA QUE DICE "LO QUE ESTA GUARDA NO CUBRE" NO SE BORRA: describia
    # con exactitud el estado hasta el 2 sep 2026, y taparlo impediria auditar
    # por que la mitad estuvo apagada setenta vueltas. Lo que sigue es lo que
    # cambio.
    #
    # LA DECISION DEL FUNDADOR (2 sep 2026, PREGUNTA 1, opcion c con atajo de
    # registro, en docs/loop/paradas/2026-09-02-opc05-bidireccionales-DECISION.md):
    # LA LISTA BLANCA DEJA DE SER UNA LISTA A MANO Y PASA A SER UN REGISTRO DE
    # CITAS. La guarda ya no pregunta "esta en la lista?", pregunta "tiene este
    # par un VEREDICTO DE LECTURA REGISTRADO CON CITA?". UN PAR SIN CITA ES
    # ROJO. Asi las tres letras de la ficha dejan de chocar: L1 se reescribe
    # como registro, y L2 (el grafo saneado pasa en verde) y L3 (cada entrada
    # cita su lectura) quedan intactas y se cumplen las dos a la vez.
    #
    # DE DONDE SALEN LAS CITAS, y son solo dos vias mas la lectura:
    #   CRIBADO           el par existe en docs/INTRA_DOMINIO_VEREDICTOS.jsonl
    #                     con clase D, B o C. La C es el enlace mutuo legitimo
    #                     del banco 9.22. La cita es el puesto.
    #   P.10              declaracion sellada de nodo puente, declarado y NO
    #                     fundido.
    #   LECTURA_DIRIGIDA  lo que no cubran las dos, leido por P.5 y escrito en
    #                     docs/plan/LECTURAS_DIRIGIDAS.md.
    # El registro se construye con scripts/loop/vuelta152_registro_de_citas_opc05.py
    # y vive en docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl. ESTA GUARDA NO LO
    # CONSTRUYE: LO EXIGE. Si el registro no existe, es ROJO, no verde por
    # omision (banco 9, fallar ruidoso).
    #
    # P.1 NO ES OPCIONAL Y LA DIFERENCIA ESTA MEDIDA: resolviendo alias salen
    # 153 pares, sin resolver 147, y esas SEIS solo aparecen tras resolver. Una
    # guarda que no resolviera daria verde creyendo el registro completo.
    _registro_ruta = BASE / "docs" / "plan" / "REGISTRO_DE_CITAS_OPC05.jsonl"
    _citados = set()
    _registro_existe = _registro_ruta.exists()
    if _registro_existe:
        with _registro_ruta.open(encoding="utf-8") as _fh:
            for _linea in _fh:
                if not _linea.strip():
                    continue
                _e = json.loads(_linea)
                _p = _e.get("par") or []
                if len(_p) == 2:
                    _citados.add(tuple(sorted(_p)))
    _dirigidas = set()
    for _nid in sorted(activos):
        for _dest in activos[_nid].get("nodos_siguientes") or []:
            if _dest not in nodos_todos:
                continue
            _a, _b = _resolver(_nid), _resolver(_dest)
            if (_a and _b and _a != _b
                    and _a in activos and _b in activos):
                _dirigidas.add((_a, _b))
    _bidireccionales = sorted({tuple(sorted(_p)) for _p in _dirigidas
                               if (_p[1], _p[0]) in _dirigidas})
    _sin_cita = [f"{_a} <-> {_b}" for _a, _b in _bidireccionales
                 if (_a, _b) not in _citados]
    checks.append((
        "OP-C-05: todo par bidireccional entre nodos VIVOS tiene su veredicto de lectura REGISTRADO CON CITA",
        _registro_existe and not _sin_cita,
        (f"{len(_bidireccionales)} par(es) bidireccional(es) tras resolver, "
         f"{len(_bidireccionales) - len(_sin_cita)} con cita, {len(_sin_cita)} SIN CITA"
         + ("" if _registro_existe else " (Y EL REGISTRO NO EXISTE: docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl)")
         + (f": {_sin_cita[:5]}" if _sin_cita else "")),
    ))
    # ── FIN OP-C-05 ────────────────────────────────────────────
'''

t = io.open(GUARDA, encoding="utf-8").read()
assert t.count(ANCLA) == 1, "el ancla aparece %d veces" % t.count(ANCLA)
io.open(GUARDA, "w", encoding="utf-8", newline="\n").write(t.replace(ANCLA, NUEVO))
py_compile.compile(GUARDA, doraise=True)
print("  [OK] scripts/run_phase1.py parcheado y compila: la mitad de bidireccionales")
print("       de OP-C-05 queda ENCENDIDA en Gate 0 como REGISTRO DE CITAS.")
