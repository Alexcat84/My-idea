# -*- coding: utf-8 -*-
r"""_v183_tallar_apertura_h.py . ANEXA A scripts/loop/vuelta183_apertura.py LOS
BLOQUES H.5 A H.10 DE ESTE ENCARGO Y LA COLA DE MEDICIONES.

La cola (el bloque B de mediciones, con el ciclo de Gate 0 entero) se copia BYTE
A BYTE de scripts/loop/vuelta182_apertura.py: es maquina y no se reescribe. Lo
que se talla aqui son los bloques H, que son los que miden lo que ESTE encargo
promete y por eso no pueden ser un clon.
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)
ORIG = os.path.join(RAIZ, "scripts", "loop", "vuelta182_apertura.py")
DEST = os.path.join(RAIZ, "scripts", "loop", "vuelta183_apertura.py")

t = io.open(ORIG, encoding="utf-8").read().replace(chr(13) + NL, NL)
cola = t[t.index('w("FIN DEL SELLO DE APERTURA")'):]
cola = cola.replace("VUELTA 176", "VUELTA 183")

H = r'''w("=== H.5 TAREA 1.a y 1.b: LA SERIE DE REGISTROS, EL ACTA 182 Y EL SALTO ===")
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
CAB182 = [i for i, l in enumerate(l_acta, 1)
          if l.startswith("# ACTA DEL AUDITOR, VUELTA 182")]
w("CIFRA cabeceras del acta 182 encontradas: %d" % len(CAB182))
if CAB182:
    base = CAB182[0]
    w("   lineas del acta 182, de su cabecera al final del fichero: %d"
      % (len(l_acta) - base + 1))
    for aguja in ("## 1. ", "## 2. ", "## 3. ", "## 4. ", "## 5. ", "## 6. ",
                  "## 7. ", "## 8. ", "## 9. ", "## 10. ", "## 11. ",
                  "**5.D.", "**7.1 ", "**7.2 ", "**7.3 ", "**7.4 ", "**7.5 "):
        hits = [i for i, l in enumerate(l_acta, 1)
                if l.startswith(aguja) and i >= base]
        w("   %-10s -> lineas %s"
          % (repr(aguja), ", ".join(str(x) for x in hits) or "(ninguna)"))
try:
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import serie_de_registros as SER   # noqa: E402
    halladas = SER.entradas()
    w("serie_de_registros.entradas() -> %d entradas en %d sedes"
      % (len(halladas), len(SER.SEDES)))
    for s in SER.SEDES:
        w("   SEDE: %s" % os.path.relpath(s, RAIZ).replace(os.sep, "/"))
    w("CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SER.colisiones(halladas)), len(SER.huecos(halladas))))
    w("SIGUIENTE LIBRE, LLAMADO Y NO TECLEADO: R.%s"
      % SER.siguiente_libre(halladas))
    for numero, rel, linea, titulo in halladas[-6:]:
        w("   ULTIMOS: R.%s en %s:%d -> %s" % (numero, rel, linea, titulo[:100]))
except Exception as e:
    w("NO SE PUDO RECOMPUTAR LA SERIE: %r" % (e,))
w("EL SALTO DE LA 1.b, CONTADO Y NO TECLEADO: que actas tienen cabecera en el")
w("fichero del acta, para saber cuantas quedan sin entrada propia en la serie.")
cabeceras = []
for i, l in enumerate(l_acta, 1):
    if l.startswith("# ACTA DEL AUDITOR, VUELTA ") or l.startswith("# ACTA DE LA VUELTA "):
        m = re.search(r"VUELTA (\d+)", l)
        if m:
            cabeceras.append((int(m.group(1)), i))
w("   CIFRA cabeceras de acta en ACTA_AUDITOR.md: %d" % len(cabeceras))
w("   LAS ULTIMAS DOCE, POR NUMERO DE VUELTA Y LINEA:")
for n_v, li in sorted(cabeceras)[-12:]:
    w("      acta %3d -> linea %d" % (n_v, li))
w("")

w("=== H.6 TAREA 1.c: LA ESCALADA, Y LA CAIDA QUE LA TRAE, MEDIDA ===")
w("(el veredicto de una linea del reporte de la 182 contra su propia seccion 8.")
w(" NI EL VEREDICTO NI LAS CABECERAS SE TECLEAN: se leen del reporte archivado)")
R182 = os.path.join(LOOP, "reportes", "REPORTE_V182.md")
l182 = []
if not os.path.exists(R182):
    w("   docs/loop/reportes/REPORTE_V182.md -> NO EXISTE. Sin el no hay caida que")
    w("   medir, y eso se declara en vez de suponerla.")
else:
    t182 = io.open(R182, encoding="utf-8").read().replace(chr(13) + NL, NL)
    l182 = t182.split(NL)
    g182 = bytes_de_git("docs/loop/reportes/REPORTE_V182.md")
    w("   docs/loop/reportes/REPORTE_V182.md -> %d lineas | disco %d bytes | git %s"
      % (len(l182), os.path.getsize(R182),
         ("%d bytes" % g182) if g182 is not None else "NO ESTA EN HEAD"))
    for i, l in enumerate(l182, 1):
        if "EL VEREDICTO DE UNA LINEA" in l:
            w("   VEREDICTO en la LINEA %d:" % i)
            for k in range(i - 1, min(i + 6, len(l182))):
                w("      | " + l182[k].strip()[:150])
    w("   LAS CABECERAS C.n DE LA SECCION 8, CONTADAS Y NO RECORDADAS:")
    cs = [(i, l) for i, l in enumerate(l182, 1)
          if re.match(r"^\*{0,2}C\.\d+", l.strip())]
    for i, l in cs:
        w("      LINEA %d: %s" % (i, l.strip()[:130]))
    w("   CIFRA cabeceras C.n localizadas: %d" % len(cs))
    w("   CIFRA numerales distintos de C.n: %d"
      % len({re.search(r"C\.(\d+)", l).group(1) for _i, l in cs}))
    w("   LAS FILAS DE LA TABLA DE TAREAS, CONTADAS DE SU TABLA:")
    filas_t = [(i, l) for i, l in enumerate(l182, 1)
               if re.match(r"^\|\s*\*{0,2}\d+\*{0,2}\s*\|", l)]
    for i, l in filas_t:
        w("      LINEA %d: %s" % (i, l.strip()[:130]))
    w("   CIFRA filas de tabla que empiezan por un numero: %d" % len(filas_t))
    w("   LOS NUMERALES ESCRITOS CON LETRA QUE APARECEN EN EL VEREDICTO:")
    for l in [x for x in l182 if "EL VEREDICTO DE UNA LINEA" in x]:
        for pal in ("una", "dos", "tres", "cuatro", "cinco", "seis", "siete",
                    "ocho", "nueve", "diez"):
            if re.search(r"\b%s\b" % pal, l.lower()):
                w("      %s -> SI aparece" % pal)
w("EL SUJETO DE LA OPERACION, MEDIDO ANTES DE TOCARLO:")
CER = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
t_cer = io.open(CER, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_cer = t_cer.split(NL)
g_cer = bytes_de_git("scripts/loop/cerrar_reporte.py")
w("   scripts/loop/cerrar_reporte.py -> %d lineas | disco %d bytes | git %s"
  % (len(l_cer), os.path.getsize(CER),
     ("%d bytes" % g_cer) if g_cer is not None else "NO ESTA EN HEAD"))
for aguja in ("def piezas_que_faltan", "def hueco_declarado_que_falta",
              "def citas_de_arnes_que_no_calzan", "def rama_de_la_seccion9",
              "def cifras_sin_pareja", "os.path.getsize(ruta_bat)",
              "max(tam, 0)", "def main"):
    hits = [(i, l) for i, l in enumerate(l_cer, 1) if aguja in l]
    w("   %-42s -> %d aparicion(es)" % (repr(aguja), len(hits)))
    for i, l in hits:
        w("      LINEA %d: %s" % (i, l.strip()[:150]))
w("")

w("=== H.7 TAREA 1.d: EL HUECO DE LA SECCION 9, EN SU CODIGO DE HOY ===")
w("(no se copia la linea que el encargo nombra: se busca en el fichero y se")
w(" imprime con su numero, tal como esta hoy)")
for i, l in enumerate(l_cer, 1):
    if "ruta_bat" in l or "NO EXISTE" in l:
        w("   LINEA %d: %s" % (i, l.rstrip()[:160]))
w("LAS TRES PIEZAS QUE EL HUECO YA EXIGE, LOCALIZADAS EN EL CODIGO:")
for aguja in ("MARCA_HUECO", "MARCA_ATRIBUCION", "PATRON_BYTES"):
    hits = [(i, l) for i, l in enumerate(l_cer, 1) if aguja in l]
    w("   %-20s -> %d aparicion(es), lineas %s"
      % (aguja, len(hits), ", ".join(str(i) for i, _l in hits[:12])))
w("")

w("=== H.8 TAREA 1.e: EL TRAMO DE LA CIEGA DE LA 182, LEIDO DEL ACTA ===")
w("(los 30 puestos NO se teclean: se sacan de la seccion 9 del acta 182 y se")
w(" parsean. Si el acta no los trae, se dice y no se inventa ninguno)")
puestos_ciega = []
if CAB182:
    base = CAB182[0]
    ini9 = None
    fin9 = len(l_acta)
    for i in range(base, len(l_acta)):
        if l_acta[i].startswith("## 9. "):
            ini9 = i
            break
    if ini9 is None:
        w("   EL ACTA 182 NO TIENE SECCION 9. No se inventa ninguna.")
    else:
        for i in range(ini9 + 1, len(l_acta)):
            if l_acta[i].startswith("## "):
                fin9 = i
                break
        w("   SECCION 9 del acta 182: lineas %d a %d (%d lineas)"
          % (ini9 + 1, fin9, fin9 - ini9))
        for i in range(ini9, min(ini9 + 12, fin9)):
            w("      | " + l_acta[i].strip()[:150])
        for i in range(ini9, fin9):
            if "PUESTOS SON" in l_acta[i].upper():
                bloque = NL.join(l_acta[i:i + 4])
                w("   LA LINEA QUE LOS LISTA es la %d, y sus tres siguientes:" % (i + 1))
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
w("LA MAQUINA DE LA 182 QUE SE IMPORTA Y NO SE COPIA:")
RREL = "scripts/loop/vuelta182_tarea1c_relectura_al_doble.py"
PREL = os.path.join(RAIZ, RREL.replace("/", os.sep))
w("   %s existe: %s | disco %s bytes"
  % (RREL, "SI" if os.path.exists(PREL) else "NO",
     os.path.getsize(PREL) if os.path.exists(PREL) else "n/a"))
if os.path.exists(PREL):
    t_rel = io.open(PREL, encoding="utf-8", errors="replace").read().replace(chr(13) + NL, NL)
    for i, l in enumerate(t_rel.split(NL), 1):
        if l.startswith("def ") or l.startswith("VARA") or l.startswith("PUESTOS"):
            w("      LINEA %d: %s" % (i, l.strip()[:130]))
w("")

w("=== H.9 TAREA 2: LA BATERIA, SU LANZADOR Y SUS TRAMOS, CONTADOS ===")
RBT = "scripts/loop/vuelta183_bateria_por_tramos.py"
BT = os.path.join(RAIZ, RBT.replace("/", os.sep))
g_bt = bytes_de_git(RBT)
w("   %s existe: %s | disco %s bytes | git %s"
  % (RBT, "SI" if os.path.exists(BT) else "NO",
     os.path.getsize(BT) if os.path.exists(BT) else "n/a",
     ("%d bytes" % g_bt) if g_bt is not None else "NO ESTA EN HEAD"))
w("EL REPARTO, CORRIDO HOY CON --plan Y NO COPIADO DEL ENCARGO:")
c_pl, o_pl = correr([PY, RBT, "--plan"])
w("   EXITCODE de --plan: %d" % c_pl)
for l in o_pl.replace(chr(13), "").split(NL):
    if l.strip():
        w("      | " + l.rstrip()[:150])
w("QUE TRAMO TOCA, CORRIDO HOY CON --siguiente:")
c_sg, o_sg = correr([PY, RBT, "--siguiente"])
w("   EXITCODE de --siguiente: %d" % c_sg)
for l in o_sg.replace(chr(13), "").split(NL):
    if l.strip():
        w("      | " + l.rstrip()[:150])
w("LAS BATERIAS VIVAS EN docs/loop/, CONTADAS DE SU DIRECTORIO:")
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
try:
    import verificar_mutaciones_viejas as VMV   # noqa: E402
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _a in VMV.VIEJAS]
    w("   CIFRA censo: %d | CIFRA nomina: %d | VARA_DEL_CENSO: %d"
      % (len(censo), len(nomina), VMV.VARA_DEL_CENSO))
    w("   FAMILIAS_DE_ARNES: %s" % ", ".join(VMV.FAMILIAS_DE_ARNES))
    w("   TOPE_DE_MINUTOS_POR_TRAMO = %s" % VMV.TOPE_DE_MINUTOS_POR_TRAMO)
    ultima, faltan = VMV.arneses_que_faltan()
    w("   arneses_que_faltan() HOY: ultima vuelta %s, faltan %d" % (ultima, len(faltan)))
    for n in faltan:
        w("      FALTA: %s" % n)
    invis = VMV.nomina_invisible_al_censo()
    w("   nomina_invisible_al_censo(): %d" % len(invis))
    for n in invis:
        w("      INVISIBLE: %s" % n)
    malas = VMV.guarda_del_sujeto_congelado()
    w("   guarda_del_sujeto_congelado(): %d entradas sin congelar" % len(malas))
    for nombre, veredicto, vive in malas:
        w("      SUJETO SIN CONGELAR: %-46s %s" % (nombre, veredicto))
except Exception as e:
    w("   NO SE PUDO RECOMPUTAR EL CENSO: %r" % (e,))
w("EL REGISTRO DEL SUJETO CONGELADO, CONTADO DE SU FICHERO:")
if os.path.exists(REGISTRO_SC):
    filas_sc = [json.loads(l) for l in io.open(REGISTRO_SC, encoding="utf-8") if l.strip()]
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> %d filas, disco %d bytes"
      % (len(filas_sc), os.path.getsize(REGISTRO_SC)))
else:
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> NO EXISTE")
w("")

w("=== H.10 EL ARCHIVO DE VEREDICTOS, QUE ESTA VUELTA NO PUEDE MOVER ===")
w("(el encargo dice que su sha256 tiene que seguir siendo el mismo al cerrar.")
w(" AQUI NO SE COPIA EL DEL ENCARGO: se computa y se imprime lo que salga)")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
datos_ver = io.open(VER, "rb").read()
w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> disco %d bytes | LF %d bytes"
  % (os.path.getsize(VER), len(datos_ver.replace(chr(13).encode(), b""))))
w("   sha256 (disco): %s" % hashlib.sha256(datos_ver).hexdigest())
w("   sha256 (LF)   : %s"
  % hashlib.sha256(datos_ver.replace((chr(13) + NL).encode(), NL.encode())).hexdigest())
filas = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
w("   CIFRA filas: %d" % len(filas))
por_clase = {}
for f in filas:
    por_clase[f.get("clase")] = por_clase.get(f.get("clase"), 0) + 1
for k in sorted(por_clase, key=lambda x: (x is None, x)):
    w("   CIFRA clase %-6s: %d" % (repr(k), por_clase[k]))
puestos = [f.get("puesto_intra") for f in filas]
w("   MIN puesto %s | MAX puesto %s | HUECOS %d | DUPLICADOS %d"
  % (min(puestos), max(puestos),
     len(set(range(min(puestos), max(puestos) + 1)) - set(puestos)),
     len(puestos) - len(set(puestos))))
w("")

'''

with io.open(DEST, "a", encoding="utf-8", newline=NL) as f:
    f.write(H)
    f.write(cola)

n = io.open(DEST, encoding="utf-8").read()
print("ESCRITO %s" % DEST)
print("CIFRA bytes: %d | CIFRA lineas: %d" % (len(n.encode("utf-8")), n.count(NL)))
