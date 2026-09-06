# -*- coding: utf-8 -*-
r"""_v182_parche_apertura.py . EL PARCHE QUE CONVIERTE EL CLON DEL BLOQUE DE
APERTURA DE LA 181 EN EL DE LA 182.

Se guarda con nombre y no se tira, para que el clon sea auditable: quien quiera
saber que cambio entre vuelta181_apertura.py y vuelta182_apertura.py tiene aqui
el trozo exacto que se sustituyo, y ademas
scripts/loop/cotejar_clon_declarado.py lo mide por su cuenta.

USO:
  python scripts/loop/_v182_parche_apertura.py
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(RAIZ, "scripts", "loop", "vuelta182_apertura.py")
NL = chr(10)

NUEVO_BLOQUE_H = r'''w("=== H.5 TAREA 1.a: LA SERIE DE REGISTROS Y EL ACTA 181, LOCALIZADAS ===")
w("(no se teclea ningun numero de registro: se llama a serie_de_registros.py y")
w(" se imprime lo que devuelva. La cabecera del acta se busca en su fichero)")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
t_acta = io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_acta = t_acta.split(NL)
w("docs/loop/ACTA_AUDITOR.md -> %d lineas | disco %d bytes | LF %d bytes"
  % (len(l_acta), os.path.getsize(ACTA), len(t_acta.encode("utf-8"))))
for i, l in enumerate(l_acta, 1):
    if l.startswith("# ACTA DEL AUDITOR, VUELTA 18"):
        w("   CABECERA en la LINEA %d: %s" % (i, l.strip()[:120]))
CAB181 = [i for i, l in enumerate(l_acta, 1)
          if l.startswith("# ACTA DEL AUDITOR, VUELTA 181")]
w("CIFRA cabeceras del acta 181 encontradas: %d" % len(CAB181))
if CAB181:
    base = CAB181[0]
    w("   lineas del acta 181, de su cabecera al final del fichero: %d"
      % (len(l_acta) - base + 1))
    for aguja in ("## 1. ", "## 2. ", "## 3. ", "## 4. ", "## 5. ", "## 6. ",
                  "## 7. ", "## 8. ", "## 9. ", "## 10. ", "## 11. ",
                  "**7.1 ", "**7.2 ", "**7.3 ", "**7.4 ", "**7.5 "):
        hits = [i for i, l in enumerate(l_acta, 1)
                if l.startswith(aguja) and i >= base]
        w("   %-10s -> lineas %s"
          % (repr(aguja), ", ".join(str(x) for x in hits) or "(ninguna)"))
try:
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import serie_de_registros as SER   # noqa: E402
    serie, sedes = SER.serie_entera()
    w("serie_de_registros.serie_entera() -> %d registros" % len(serie))
    for s in sedes:
        w("   SEDE: %s" % s)
    w("SIGUIENTE LIBRE, LLAMADO Y NO TECLEADO: R.%s" % SER.siguiente_libre())
    for n in sorted(serie)[-6:]:
        w("   ULTIMOS: R.%s -> %s" % (n, str(serie[n])[:110]))
except Exception as e:
    w("NO SE PUDO RECOMPUTAR LA SERIE: %r" % (e,))
w("")

w("=== H.6 TAREA 1.b: LOS DOS PENDIENTES DEL ACTA 180, MEDIDOS EN EL CODIGO ===")
w("(el E.1 sobre cerrar_reporte.py y la P.1 del censo. NO SE COPIA NADA DEL ACTA:")
w(" se busca en el fichero y se imprime la linea con su numero)")
CER = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
t_cer = io.open(CER, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_cer = t_cer.split(NL)
w("scripts/loop/cerrar_reporte.py -> %d lineas | disco %d bytes | LF %d bytes"
  % (len(l_cer), os.path.getsize(CER), len(t_cer.encode("utf-8"))))
for aguja in ("CAB_9 =", "CAB_9_HUECO =", "PATRON_FICHERO_BATERIA =",
              "def vuelta_de_fichero", "def hueco_declarado_que_falta",
              "if lineas_bat:", "hueco_declarado_que_falta(seccion9",
              "vuelta que lleva dentro el nombre del fichero"):
    hits = [(i, l) for i, l in enumerate(l_cer, 1) if aguja in l]
    w("   %-46s -> %d aparicion(es)" % (repr(aguja), len(hits)))
    for i, l in hits:
        w("      LINEA %d: %s" % (i, l.strip()[:150]))
w("EL PATRON APLICADO, CON vuelta_de_fichero() DE VERDAD Y NO PARAFRASEADA:")
try:
    import cerrar_reporte as CR   # noqa: E402
    for nombre in ("docs/loop/SALIDA_V177_BATERIA.txt",
                   "docs/loop/SALIDA_V180_HUECO_BATERIA.txt",
                   "docs/loop/SALIDA_V181_BATERIA.txt",
                   "docs/loop/SALIDA_V182_HUECO_BATERIA.txt",
                   "docs/loop/SALIDA_V183_BATERIA.txt"):
        pth = os.path.join(RAIZ, nombre.replace("/", os.sep))
        w("   %-46s vuelta_de_fichero -> %-5s | existe: %-2s | disco: %s"
          % (nombre, CR.vuelta_de_fichero(nombre),
             "SI" if os.path.exists(pth) else "NO",
             (os.path.getsize(pth) if os.path.exists(pth) else "n/a")))
except Exception as e:
    w("   NO SE PUDO IMPORTAR cerrar_reporte: %r" % (e,))
w("LA P.1, EL ARNES EN ROJO, MEDIDO Y NO RECORDADO:")
RP1 = "scripts/loop/vuelta172_tarea1c_guarda_que_mordio.py"
P1 = os.path.join(RAIZ, RP1.replace("/", os.sep))
w("   %s existe: %s" % (RP1, "SI" if os.path.exists(P1) else "NO"))
if os.path.exists(P1):
    g1 = bytes_de_git(RP1)
    w("   -> disco %d bytes | git %s"
      % (os.path.getsize(P1), ("%d bytes" % g1) if g1 is not None else "NO ESTA EN HEAD"))
    c_p1, o_p1 = correr([PY, RP1])
    w("   CORRIDO HOY -> EXITCODE %d, %d bytes de salida"
      % (c_p1, len(o_p1.encode("utf-8"))))
    for l in o_p1.replace(chr(13), "").split(NL):
        if l.strip():
            w("      | " + l.strip()[:140])
    c_nac, o_nac = git(["log", "--diff-filter=A", "--format=%h%x09%ad%x09%s",
                        "--date=short", "--", RP1])
    w("   COMMIT DE NACIMIENTO (git log --diff-filter=A): %s"
      % (o_nac.strip()[:160] or "(no localizado)"))
VMV = None
try:
    import verificar_mutaciones_viejas as VMV   # noqa: E402
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _a in VMV.VIEJAS]
    w("   esta en el censo arneses_del_directorio(): %s"
      % ("SI" if os.path.basename(P1) in censo else "NO"))
    w("   esta en la nomina VIEJAS: %s"
      % ("SI" if os.path.basename(P1) in nomina else "NO"))
    w("   CIFRA censo: %d | CIFRA nomina: %d | VARA_DEL_CENSO: %d"
      % (len(censo), len(nomina), VMV.VARA_DEL_CENSO))
    w("   FAMILIAS_DE_ARNES: %s" % ", ".join(VMV.FAMILIAS_DE_ARNES))
except Exception as e:
    w("   NO SE PUDO RECOMPUTAR EL CENSO: %r" % (e,))
w("")

w("=== H.7 TAREA 1.c: EL TRAMO DE LA CIEGA DE LA 181, LEIDO DEL ACTA ===")
w("(los 30 puestos NO se teclean: se sacan de la linea del acta que los lista y")
w(" se parsean. Si el acta no los trae, se dice y no se inventa ninguno)")
puestos_ciega = []
if CAB181:
    base = CAB181[0]
    for i in range(base, len(l_acta)):
        if "LOS 30 PUESTOS SON" in l_acta[i]:
            bloque = NL.join(l_acta[i:i + 4])
            w("   LINEA %d del acta, y sus tres siguientes:" % (i + 1))
            for l in bloque.split(NL):
                w("      | " + l.strip()[:150])
            crudo = bloque.split(":", 1)[1] if ":" in bloque else ""
            puestos_ciega = [int(x) for x in re.findall(r"\d+", crudo.replace(".", ""))]
            break
w("   CIFRA puestos parseados de esa linea: %d" % len(puestos_ciega))
w("   LOS PUESTOS, ORDENADOS: %s" % ", ".join(str(x) for x in sorted(puestos_ciega)))
w("   MIN %s | MAX %s | REPETIDOS %d"
  % (min(puestos_ciega) if puestos_ciega else "n/a",
     max(puestos_ciega) if puestos_ciega else "n/a",
     len(puestos_ciega) - len(set(puestos_ciega))))
w("")

w("=== H.8 TAREA 2: EL AISLADOR Y LA APERTURA DEL AUDITOR, ANTES DE ESCRIBIRLA ===")
for r in ("scripts/loop/aislador_de_ciega.py",
          "scripts/loop/verificar_apertura_sellada.py",
          "scripts/loop/apertura_del_auditor.py",
          "scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py"):
    pth = os.path.join(RAIZ, r.replace("/", os.sep))
    g = bytes_de_git(r)
    w("   %-58s -> disco %s | git %s"
      % (r, ("%d bytes" % os.path.getsize(pth)) if os.path.exists(pth) else "NO EXISTE",
         ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("   (los dos ultimos NO EXISTEN al abrir, y eso es lo correcto: los escribe")
w("    esta vuelta. Si existieran al abrir, seria que la vuelta ya se corrio)")
AIS = os.path.join(RAIZ, "scripts", "loop", "aislador_de_ciega.py")
t_ais = io.open(AIS, encoding="utf-8", errors="replace").read().replace(chr(13) + NL, NL)
w("   aislador_de_ciega.py -> %d lineas" % len(t_ais.split(NL)))
for aguja in ("def guarda_de_fuga", "def elegir_pares", "def escribir_ciega",
              "--criterio", "--puestos", "--semilla", "CAMPOS_CIEGOS"):
    hits = [i for i, l in enumerate(t_ais.split(NL), 1) if aguja in l]
    w("   %-22s -> lineas %s"
      % (repr(aguja), ", ".join(str(x) for x in hits[:6]) or "(ninguna)"))
w("   LAS TRES COSAS QUE EL REMEDIO PROHIBE ANTES DEL SELLO, nombradas aqui para")
w("   que el gemelo no las pueda elegir despues: git log, git status, REPORTE.md")
w("")

w("=== H.9 TAREA 3: EL ARCHIVO DE VEREDICTOS Y EL 2.464, RECONTADOS ===")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
filas = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
w("docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> %d filas | disco %d bytes"
  % (len(filas), os.path.getsize(VER)))
por_clase = {}
for f in filas:
    por_clase[f.get("clase")] = por_clase.get(f.get("clase"), 0) + 1
for k in sorted(por_clase, key=lambda x: (x is None, x)):
    w("   CIFRA clase %-6s: %d" % (repr(k), por_clase[k]))
w("   SUMA de las clases: %d | filas: %d | CALZAN: %s"
  % (sum(por_clase.values()), len(filas),
     "SI" if sum(por_clase.values()) == len(filas) else "NO"))
puestos = [f.get("puesto_intra") for f in filas]
w("   MIN puesto %s | MAX puesto %s | HUECOS %d | DUPLICADOS %d"
  % (min(puestos), max(puestos),
     len(set(range(min(puestos), max(puestos) + 1)) - set(puestos)),
     len(puestos) - len(set(puestos))))
EL_2464 = [f for f in filas if f.get("puesto_intra") == 2464]
w("   EL PUESTO 2464, LOCALIZADO Y NO RECORDADO: %d fila(s)" % len(EL_2464))
for f in EL_2464:
    w("      nodo_a: %s" % f.get("nodo_a"))
    w("      nodo_b: %s" % f.get("nodo_b"))
    w("      clase : %s | dominio: %s" % (f.get("clase"), f.get("dominio")))
    w("      razon : %s" % str(f.get("razon"))[:400])
w("   LOS CAMPOS DE UNA FILA, LISTADOS PARA QUE EL INSTRUMENTO NO INVENTE NINGUNO:")
w("      %s" % ", ".join(sorted(filas[0].keys())))
w("EL GRAFO DE HOY, ABIERTO PARA VER SI EL DIFERENCIADOR SIGUE AHI:")
GR = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
w("   dataset/metadata/master_graph.json -> disco %d bytes" % os.path.getsize(GR))
try:
    G = json.load(io.open(GR, encoding="utf-8"))
    nodos = G.get("nodes", G if isinstance(G, list) else [])
    w("   CIFRA nodos del grafo: %d" % len(nodos))
    porid = {}
    for n in nodos:
        if isinstance(n, dict) and n.get("id"):
            porid[n["id"]] = n
    w("   LAS CLAVES DE UN NODO: %s"
      % ", ".join(sorted(nodos[0].keys())) if nodos else "(sin nodos)")
    for nid in ("cero_defectos", "zero_defects_concepto"):
        n = porid.get(nid)
        if n is None:
            w("   %s -> NO ESTA EN EL GRAFO DE HOY" % nid)
            continue
        pasos = n.get("pasos") or n.get("steps") or []
        w("   %s -> %d pasos" % (nid, len(pasos)))
        for k, ps in enumerate(pasos, 1):
            w("      paso %d: %s" % (k, str(ps)[:150]))
except Exception as e:
    w("   NO SE PUDO ABRIR EL GRAFO: %r" % (e,))
w("")

w("=== H.10 TAREA 5: LAS BATERIAS Y SUS TRAMOS, CONTADAS DE SU DIRECTORIO ===")
PAT_BAT = re.compile(r"^SALIDA_V(\d+)_BATERIA.*\.txt$")
vivas = sorted(n for n in os.listdir(LOOP) if PAT_BAT.match(n))
n_cero = 0
for n in vivas:
    pth = os.path.join(LOOP, n)
    tam = os.path.getsize(pth)
    if tam == 0:
        n_cero += 1
    w("   %-50s disco %8d bytes" % (n, tam))
w("CIFRA ficheros SALIDA_V<N>_BATERIA*.txt en docs/loop/: %d" % len(vivas))
w("CIFRA de ellos que miden CERO BYTES: %d" % n_cero)
w("EL LANZADOR POR TRAMOS DE LA 176, QUE ES EL PRECEDENTE QUE LA DECISION CITA:")
RBT = "scripts/loop/vuelta176_bateria_por_tramos.py"
BT = os.path.join(RAIZ, RBT.replace("/", os.sep))
w("   %s existe: %s | disco %s bytes"
  % (RBT, "SI" if os.path.exists(BT) else "NO",
     os.path.getsize(BT) if os.path.exists(BT) else "n/a"))
if os.path.exists(BT):
    t_bt = io.open(BT, encoding="utf-8", errors="replace").read().replace(chr(13) + NL, NL)
    for i, l in enumerate(t_bt.split(NL), 1):
        if "TRAMOS" in l and "=" in l and not l.strip().startswith("#"):
            w("      LINEA %d: %s" % (i, l.strip()[:150]))
w("EL RELOJ DE LAS CORRIDAS VIEJAS, LEIDO CON reloj_de_la_corrida():")
if VMV is None:
    w("   NO SE PUDO LEER EL RELOJ: el modulo de la bateria no se importo")
else:
    for n in vivas:
        pth = os.path.join(LOOP, n)
        if os.path.getsize(pth) == 0:
            w("   %-50s CERO BYTES: no hay reloj que leer" % n)
            continue
        tt = io.open(pth, encoding="utf-8", errors="replace").read()
        rl = VMV.reloj_de_la_corrida(tt)
        cost = VMV.minutos_por_entrada(rl)
        w("   %-50s tramos con reloj: %2d | minutos por entrada (MAXIMO): %s"
          % (n, len(rl), ("%.4f" % cost) if cost is not None else "(sin reloj)"))
    w("   TOPE_DE_MINUTOS_POR_TRAMO = %s" % VMV.TOPE_DE_MINUTOS_POR_TRAMO)
    ultima, faltan = VMV.arneses_que_faltan()
    w("   arneses_que_faltan() HOY: ultima vuelta %s, faltan %d" % (ultima, len(faltan)))
    for n in faltan:
        w("      FALTA: %s" % n)
    invis = VMV.nomina_invisible_al_censo()
    w("   nomina_invisible_al_censo(): %d" % len(invis))
    malas = VMV.guarda_del_sujeto_congelado()
    w("   guarda_del_sujeto_congelado(): %d entradas sin congelar" % len(malas))
    for nombre, veredicto, vive in malas:
        w("      SUJETO SIN CONGELAR: %-46s %s" % (nombre, veredicto))
w("EL REGISTRO DEL SUJETO CONGELADO, CONTADO DE SU FICHERO:")
if os.path.exists(REGISTRO_SC):
    filas_sc = [json.loads(l) for l in io.open(REGISTRO_SC, encoding="utf-8") if l.strip()]
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> %d filas, disco %d bytes"
      % (len(filas_sc), os.path.getsize(REGISTRO_SC)))
else:
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> NO EXISTE")
w("")

'''


def main():
    t = io.open(P, encoding="utf-8").read()
    ini = t.index('w("=== H.5')
    fin = t.index('w("FIN DEL SELLO DE APERTURA")')
    t = t[:ini] + NUEVO_BLOQUE_H + t[fin:]
    io.open(P, "w", encoding="utf-8", newline=NL).write(t)
    print("PARCHE APLICADO sobre %s" % P)
    print("bytes ahora: %d | lineas: %d" % (len(t.encode("utf-8")), t.count(NL)))


if __name__ == "__main__":
    main()
