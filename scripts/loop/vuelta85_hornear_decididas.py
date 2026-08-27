# -*- coding: utf-8 -*-
"""vuelta85_hornear_decididas.py . TAREA 3.a de la vuelta 85.

SUCESOR de scripts/loop/vuelta84_hornear_decididas.py, MISMO MECANISMO (el
descubrimiento por patron no cambia): lo que cambia es CUANDO CORRE, escrito
aqui para que no dependa de que el encargo se acuerde (adjudicacion 6.3 del
acta de la vuelta 84, que pone el CUANDO a la adjudicacion 6.6 del acta 83,
"el registro crece con el tramo").

EL REGISTRO SE HORNEA DOS VECES POR VUELTA:
  1. ANTES DEL FILTRO de esta misma vuelta, para que el tramo que la vuelta
     ANTERIOR acabo de leer (y lo que la relectura conjunta de esta vuelta
     haya escrito) ya este dentro cuando el filtro P.9.1 calcule la cabeza
     de la bolsa fresca.
  2. AL CIERRE de la vuelta, DESPUES de escribir todo lo que esta vuelta
     escriba (incluida la lectura del tramo nuevo), para que el tramo recien
     leido entre tambien. La guarda del registro (vuelta83_guarda_decididas.py)
     se corre DESPUES de este segundo horneado: verde significa que la
     primera unidad sin decidir es la cabeza del tramo SIGUIENTE, no la del
     que se acaba de leer.

EL RESTO ES IDENTICO al horneador de la vuelta 84: descubre los ficheros por
PATRON, sin nombres tecleados dentro.

  ESCRIBIR (tramos ya escritos): docs/loop/SALIDA_V*_TRAMO*_ESCRIBIR.txt
  LECTURA CRUDA (tramos 1 y 2, sin marca de decision):
      docs/loop/SALIDA_V*_OPE01_TRAMO*_LECTURA.txt

Cada tramo ESCRIBIR se cruza por NOMBRE del par contra sus ficheros de paso
propios, si existen, DESCUBIERTOS TAMBIEN POR PATRON (no tecleados):
  docs/loop/SALIDA_V<vuelta>_TRAMO<tramo>_DOSSIER30.txt (formato "[N] madre ->
  hijo (dominio X, paso senalado P)"), PRIMERO
  docs/loop/SALIDA_V<vuelta>_TRAMO<tramo>_FILTRO_P91_GUARDA_CADENA.txt
  (formato "N: madre -> hijo (paso P, dominio X) | ..."), SEGUNDO, para
  llenar los pares que el DOSSIER30 no traiga (los tramos 6 y 8 tienen los
  dos ficheros a la vez; el tramo 7 solo el segundo; los tramos 4 y 5 solo
  el primero). El tramo 3 no tiene ninguno de los dos: su paso se declara
  NO RECONSTRUIBLE, igual que antes.

EL RESTO DE LA MAQUINA ES IDENTICO al horneador de la vuelta 83 (mismo
partido de bloques por cabecera, misma verificacion contra el grafo de HOY
con ascenso/degradacion declarados, mismo formato de salida): lo unico que
cambia es COMO SE ENCUENTRAN LOS FICHEROS.

SALIDA: docs/plan/OP_E_01_DECIDIDAS.jsonl (una fila JSON por par decidido:
madre, hijo, paso, tramo, decision, fichero_origen, nota) y un resumen por
stdout con las cuentas de cada bloque, los ficheros descubiertos por tramo,
las filas no reconstruidas y las filas verificadas contra el grafo.
"""
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PLAN = os.path.join(RAIZ, "docs", "plan")

RE_HEADER = re.compile(r"^(?!\s)(.+?):\s*(\d+)\s*$")
# El tramo 8 en adelante (scripts/loop/vuelta83_medir_tramo8.py y sucesores)
# antepone el indice de la bolsa filtrada a cada par ("  34: madre -> hijo"),
# a diferencia de los tramos 3 a 7 ("  madre -> hijo"); el indice es opcional.
RE_PAR = re.compile(r"^\s{2}(?:\d+:\s*)?([A-Za-z0-9_]+)\s*->\s*([A-Za-z0-9_]+)")

RE_ESCRIBIR_NOMBRE = re.compile(r"^SALIDA_V(\d+)_TRAMO(\d+)_ESCRIBIR\.txt$")
RE_LECTURA_NOMBRE = re.compile(r"^SALIDA_V(\d+)_OPE01_TRAMO(\d+)_LECTURA\.txt$")


def clasificar_header(nombre):
    if nombre.startswith("ARISTAS ESCRITAS"):
        return "ESCRITA"
    if nombre.startswith("DESCARTADOS"):
        return "NO SE ENLAZA"
    if nombre.startswith("NO ESCRITOS ESTA LECTURA FRESCA"):
        return "NO SE ENLAZA"
    if nombre.startswith("DISCUTIBLE, NO ESCRITO POR CAUTELA"):
        return "NO SE ENLAZA"
    # Formato propio de scripts/loop/vuelta83_medir_tramo8.py (y sucesores),
    # que mide la decision leyendo el grafo en vez de declararla a mano:
    # "NO SE ENLAZAN (verificadas ausentes en las DOS vistas): N".
    if nombre.startswith("NO SE ENLAZAN"):
        return "NO SE ENLAZA"
    if nombre.startswith("YA DECIDIDOS EN VUELTAS ANTERIORES"):
        return "CITA"
    # "UNIDADES YA DECIDIDAS, SALTADAS (leidas de ...): N" (tramo 8 en
    # adelante): son citas de decisiones YA registradas por un tramo previo
    # (los indices 0..K-1 de la bolsa filtrada que el propio filtro salto por
    # tener ya decision). No generan fila nueva ni cita nueva: la fila ya
    # existe con su fichero_origen original.
    if nombre.startswith("UNIDADES YA DECIDIDAS, SALTADAS"):
        return None
    return None  # ESCALERA ROTA, YA ESTABAN, TOTAL DE LA CABEZA LEIDA, DISCUTIBLES marcados...


def leer(nombre):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        return None
    return open(ruta, encoding="utf-8", errors="replace").read()


def descubrir_ficheros():
    """POR PATRON, no tecleados. Devuelve (escribir, lectura, discrepancias)
    donde escribir es una lista [(nombre, vuelta, tramo)] ordenada por tramo,
    lectura idem, y discrepancias es una lista de avisos (mas de un fichero
    para el mismo tramo)."""
    discrepancias = []

    candidatos_escribir = {}
    for ruta in glob.glob(os.path.join(LOOP, "SALIDA_V*_TRAMO*_ESCRIBIR.txt")):
        nombre = os.path.basename(ruta)
        m = RE_ESCRIBIR_NOMBRE.match(nombre)
        if not m:
            continue
        vuelta, tramo = int(m.group(1)), int(m.group(2))
        candidatos_escribir.setdefault(tramo, []).append((nombre, vuelta))

    escribir = []
    for tramo in sorted(candidatos_escribir):
        opciones = candidatos_escribir[tramo]
        if len(opciones) > 1:
            discrepancias.append(
                "tramo %d tiene %d ficheros ESCRIBIR candidatos (%s): se usa el de vuelta "
                "mas alta y se declara la ambiguedad" % (tramo, len(opciones),
                                                          ", ".join(n for n, _ in opciones)))
            opciones = sorted(opciones, key=lambda x: x[1])
        nombre, vuelta = opciones[-1]
        escribir.append((nombre, vuelta, tramo))

    candidatos_lectura = {}
    for ruta in glob.glob(os.path.join(LOOP, "SALIDA_V*_OPE01_TRAMO*_LECTURA.txt")):
        nombre = os.path.basename(ruta)
        m = RE_LECTURA_NOMBRE.match(nombre)
        if not m:
            continue
        vuelta, tramo = int(m.group(1)), int(m.group(2))
        candidatos_lectura.setdefault(tramo, []).append((nombre, vuelta))

    lectura = []
    for tramo in sorted(candidatos_lectura):
        opciones = candidatos_lectura[tramo]
        if len(opciones) > 1:
            discrepancias.append(
                "tramo %d tiene %d ficheros LECTURA candidatos (%s)" % (tramo, len(opciones),
                                                                         ", ".join(n for n, _ in opciones)))
            opciones = sorted(opciones, key=lambda x: x[1])
        nombre, vuelta = opciones[-1]
        lectura.append((nombre, vuelta, tramo))

    # Un tramo no puede estar en las dos listas a la vez (ESCRIBIR y LECTURA
    # cruda son mecanicas distintas). Se declara si pasa, no se decide solo.
    tramos_escribir = set(t for _, _, t in escribir)
    tramos_lectura = set(t for _, _, t in lectura)
    solapados = tramos_escribir & tramos_lectura
    if solapados:
        discrepancias.append("tramos con fichero ESCRIBIR Y LECTURA a la vez (revisar a mano): %s"
                              % sorted(solapados))

    return escribir, lectura, discrepancias


def parsear_escribir(texto, nombre_fichero, tramo):
    filas = []
    citas = []
    header_actual = None
    cuenta_esperada = {}
    cuenta_leida = {}
    for linea in texto.splitlines():
        m = RE_HEADER.match(linea)
        if m:
            header_actual = m.group(1)
            cuenta_esperada[header_actual] = int(m.group(2))
            cuenta_leida[header_actual] = 0
            continue
        if not linea.strip():
            header_actual = None
            continue
        mp = RE_PAR.match(linea)
        if mp and header_actual is not None:
            tipo = clasificar_header(header_actual)
            if tipo is None:
                continue
            madre, hijo = mp.group(1), mp.group(2)
            cuenta_leida[header_actual] += 1
            if tipo == "CITA":
                citas.append((madre, hijo))
            else:
                filas.append({"madre": madre, "hijo": hijo, "decision": tipo,
                              "fichero_origen": nombre_fichero, "tramo": tramo})
    discrepancias = []
    for h, esperado in cuenta_esperada.items():
        leido = cuenta_leida.get(h, 0)
        if clasificar_header(h) is not None and leido != esperado:
            discrepancias.append((nombre_fichero, h, esperado, leido))
    return filas, citas, discrepancias


def cargar_paso_dossier30(nombre_fichero):
    texto = leer(nombre_fichero)
    if not texto:
        return {}
    patron = re.compile(
        r"^\[\d+\]\s*([A-Za-z0-9_]+)\s*->\s*([A-Za-z0-9_]+)\s*\(dominio\s+(\S+?),"
        r"\s*paso senalado\s+(\S+?)\)\s*$"
    )
    out = {}
    for linea in texto.splitlines():
        m = patron.match(linea.strip())
        if m:
            madre, hijo, dominio, paso = m.groups()
            out[(madre, hijo)] = paso
    return out


def cargar_paso_filtro_cadena(nombre_fichero):
    texto = leer(nombre_fichero)
    if not texto:
        return {}
    patron = re.compile(
        r"^\s*\d+:\s*([A-Za-z0-9_]+)\s*->\s*([A-Za-z0-9_]+)\s*\(paso\s+(\S+?),"
        r"\s*dominio\s+\S+?\)"
    )
    out = {}
    for linea in texto.splitlines():
        m = patron.match(linea)
        if m:
            madre, hijo, paso = m.groups()
            out[(madre, hijo)] = paso
    return out


def cargar_paso(vuelta, tramo):
    """Cruce de paso por NOMBRE, descubriendo los ficheros companeros POR
    PATRON: DOSSIER30 primero, FILTRO_P91_GUARDA_CADENA despues para llenar
    los pares que el primero no traiga. Devuelve (dict par->paso, lista de
    nombres de fichero usados)."""
    out = {}
    usados = []
    nombre_dossier = "SALIDA_V%d_TRAMO%d_DOSSIER30.txt" % (vuelta, tramo)
    if os.path.exists(os.path.join(LOOP, nombre_dossier)):
        out.update(cargar_paso_dossier30(nombre_dossier))
        usados.append(nombre_dossier)
    nombre_cadena = "SALIDA_V%d_TRAMO%d_FILTRO_P91_GUARDA_CADENA.txt" % (vuelta, tramo)
    if os.path.exists(os.path.join(LOOP, nombre_cadena)):
        pasos_cadena = cargar_paso_filtro_cadena(nombre_cadena)
        nuevos = 0
        for clave, paso in pasos_cadena.items():
            if clave not in out:
                out[clave] = paso
                nuevos += 1
        if nuevos or nombre_cadena not in usados:
            usados.append(nombre_cadena)
    return out, usados


def contar_pares_lectura_cruda(nombre_fichero):
    texto = leer(nombre_fichero)
    if not texto:
        return None
    return len(re.findall(r"^PAR \d+", texto, re.MULTILINE))


def cargar_grafo():
    ruta = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
    g = json.load(open(ruta, encoding="utf-8"))
    return g["nodos"]


def arista_presente_hoy(nodos, madre, hijo):
    n_madre = nodos.get(madre, {})
    n_hijo = nodos.get(hijo, {})
    en_sig = hijo in (n_madre.get("nodos_siguientes") or [])
    en_prev = madre in (n_hijo.get("nodos_previos") or [])
    return en_sig, en_prev


def main():
    ficheros_escribir, ficheros_lectura, discrepancias_descubrimiento = descubrir_ficheros()

    todas_filas = []
    todas_citas = []
    todas_discrepancias = []
    resumen_por_tramo = []

    for nombre, vuelta, tramo in ficheros_escribir:
        texto = leer(nombre)
        if texto is None:
            print("ROJO: no existe %s, tramo %d no se puede hornear" % (nombre, tramo))
            return 1
        filas, citas, discrepancias = parsear_escribir(texto, nombre, tramo)
        pasos, ficheros_paso = cargar_paso(vuelta, tramo)
        sin_paso = 0
        for f in filas:
            clave = (f["madre"], f["hijo"])
            if clave in pasos:
                f["paso"] = pasos[clave]
            else:
                f["paso"] = "NO RECONSTRUIBLE"
                sin_paso += 1
        todas_filas.extend(filas)
        todas_citas.extend(citas)
        todas_discrepancias.extend(discrepancias)
        resumen_por_tramo.append((tramo, nombre, len(filas), len(citas), sin_paso, ficheros_paso))

    por_par = {}
    repetidas = []
    for f in todas_filas:
        clave = (f["madre"], f["hijo"])
        if clave in por_par:
            repetidas.append((clave, por_par[clave]["tramo"], f["tramo"]))
            if f["tramo"] < por_par[clave]["tramo"]:
                por_par[clave] = f
        else:
            por_par[clave] = f

    nodos = cargar_grafo()
    ascendidas = []
    degradadas = []
    for f in por_par.values():
        en_sig, en_prev = arista_presente_hoy(nodos, f["madre"], f["hijo"])
        hoy_escrita = en_sig and en_prev
        if f["decision"] == "ESCRITA" and not hoy_escrita:
            f["decision"] = "NO SE ENLAZA"
            f["nota"] = ("degradada: %s la marcaba ESCRITA pero la arista NO esta "
                         "hoy en las dos vistas del grafo (en_sig=%s en_prev=%s); "
                         "verificado contra dataset/ de hoy"
                         % (f["fichero_origen"], en_sig, en_prev))
            degradadas.append(f)
        elif f["decision"] == "NO SE ENLAZA" and hoy_escrita:
            f["decision"] = "ESCRITA"
            f["nota"] = ("ascendida: %s la marcaba NO SE ENLAZA pero la arista SI "
                         "esta hoy en las dos vistas del grafo; verificado contra "
                         "dataset/ de hoy" % f["fichero_origen"])
            ascendidas.append(f)
        else:
            f["nota"] = None

    filas_final = sorted(por_par.values(), key=lambda f: (f["tramo"], f["madre"], f["hijo"]))

    ruta_salida = os.path.join(PLAN, "OP_E_01_DECIDIDAS.jsonl")
    with open(ruta_salida, "w", encoding="utf-8", newline="\n") as fh:
        for f in filas_final:
            fh.write(json.dumps({
                "madre": f["madre"], "hijo": f["hijo"], "paso": f["paso"],
                "tramo": f["tramo"], "decision": f["decision"],
                "fichero_origen": f["fichero_origen"], "nota": f.get("nota"),
            }, ensure_ascii=False) + "\n")

    print("=" * 78)
    print("HORNEADO docs/plan/OP_E_01_DECIDIDAS.jsonl, TAREA 2.a vuelta 84 (POR PATRON)")
    print("=" * 78)
    print()
    print("--- FICHEROS ESCRIBIR DESCUBIERTOS POR PATRON (SALIDA_V*_TRAMO*_ESCRIBIR.txt) ---")
    for tramo, nombre, n_filas, n_citas, sin_paso, ficheros_paso in resumen_por_tramo:
        print("  tramo %d: %s | %d filas nuevas, %d citadas, %d sin paso | pasos de: %s"
              % (tramo, nombre, n_filas, n_citas, sin_paso, ", ".join(ficheros_paso) or "(ninguno)"))
    print()
    print("--- FICHEROS LECTURA CRUDA DESCUBIERTOS POR PATRON (SALIDA_V*_OPE01_TRAMO*_LECTURA.txt) ---")
    total_no_reconstruibles = 0
    for nombre, vuelta, tramo in ficheros_lectura:
        n = contar_pares_lectura_cruda(nombre)
        if n is None:
            print("  ROJO: no existe %s" % nombre)
            return 1
        print("  tramo %d (%s): %d candidatos volcados, 0 filas reconstruibles" % (tramo, nombre, n))
        total_no_reconstruibles += n
    print()
    print("--- DISCREPANCIAS DE DESCUBRIMIENTO (mas de un fichero para el mismo tramo) ---")
    if discrepancias_descubrimiento:
        for d in discrepancias_descubrimiento:
            print("  %s" % d)
    else:
        print("  NINGUNA")
    print()
    print("--- DISCREPANCIAS DE CUENTA (cabecera del fichero vs lineas leidas) ---")
    if todas_discrepancias:
        for nombre, header, esperado, leido in todas_discrepancias:
            print("  %s | %s | cabecera dice %d | leidas %d" % (nombre, header, esperado, leido))
    else:
        print("  NINGUNA")
    print()
    print("--- PARES REPETIDOS ENTRE TRAMOS (declarados, no corregidos a mano) ---")
    if repetidas:
        for clave, t1, t2 in repetidas:
            print("  %s -> %s | primero en tramo %d, repetido en tramo %d" % (clave[0], clave[1], t1, t2))
    else:
        print("  NINGUNO")
    print()
    print("--- VERIFICACION CONTRA EL GRAFO DE HOY (dataset/metadata/master_graph.json) ---")
    print("  filas ASCENDIDAS (NO SE ENLAZA -> ESCRITA, arista SI presente hoy): %d" % len(ascendidas))
    for f in ascendidas:
        print("     %s -> %s (tramo %d, %s)" % (f["madre"], f["hijo"], f["tramo"], f["fichero_origen"]))
    print("  filas DEGRADADAS (ESCRITA -> NO SE ENLAZA, arista NO presente hoy): %d" % len(degradadas))
    for f in degradadas:
        print("     %s -> %s (tramo %d, %s)" % (f["madre"], f["hijo"], f["tramo"], f["fichero_origen"]))
    print()
    total_escrita = sum(1 for f in filas_final if f["decision"] == "ESCRITA")
    total_no_enlaza = sum(1 for f in filas_final if f["decision"] == "NO SE ENLAZA")
    print("--- TOTALES ---")
    print("  filas en el registro: %d (%d ESCRITA, %d NO SE ENLAZA)"
          % (len(filas_final), total_escrita, total_no_enlaza))
    print("  candidatos de tramos 1 y 2 sin fila reconstruible: %d" % total_no_reconstruibles)
    print("  escrito: docs/plan/OP_E_01_DECIDIDAS.jsonl (%d filas)" % len(filas_final))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
