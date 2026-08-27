# -*- coding: utf-8 -*-
"""vuelta83_hornear_decididas.py . TAREA 2.a de la vuelta 83.

HORNEA docs/plan/OP_E_01_DECIDIDAS.jsonl leyendo, con expresiones regulares
(NINGUNA FILA TECLEADA), los ficheros de salida de los tramos de `OP-E-01`
ya corridos:

  tramo 3 (vuelta 77): docs/loop/SALIDA_V77_TRAMO3_ESCRIBIR.txt
  tramo 4 (vuelta 78): docs/loop/SALIDA_V78_TRAMO4_ESCRIBIR.txt
  tramo 5 (vuelta 79): docs/loop/SALIDA_V79_TRAMO5_ESCRIBIR.txt
  tramo 6 (vuelta 80): docs/loop/SALIDA_V80_TRAMO6_ESCRIBIR.txt
  tramo 7 (vuelta 82): docs/loop/SALIDA_V82_TRAMO7_ESCRIBIR.txt
  tramo 1 (vuelta 75): docs/loop/SALIDA_V75_OPE01_TRAMO1_LECTURA.txt
  tramo 2 (vuelta 76): docs/loop/SALIDA_V76_OPE01_TRAMO2_LECTURA.txt

CADA FICHERO _ESCRIBIR.txt SE PARTE EN BLOQUES POR SUS PROPIAS CABECERAS
("ARISTAS ESCRITAS: N", "DESCARTADOS: N", "NO ESCRITOS ESTA LECTURA FRESCA,
con razon: N", "DISCUTIBLE, NO ESCRITO POR CAUTELA (...): N", "YA DECIDIDOS
EN VUELTAS ANTERIORES (citados, no re-derivados): N"), sin tocar el resto
("ESCALERA ROTA...", "YA ESTABAN...", "TOTAL DE LA CABEZA LEIDA...",
"DISCUTIBLES marcados..."). Los bloques "YA DECIDIDOS EN VUELTAS ANTERIORES"
son CITAS de decisiones de tramos previos, no decisiones nuevas: se cuentan
para declarar si su nomina calza, pero NUNCA generan una fila nueva (la fila
ya existe, del tramo que decidio primero).

EL PASO se cruza por NOMBRE del par (no por indice, que difiere entre
lectura y escritura) contra el fichero de la propia vuelta que SI trae paso:
DOSSIER30 para los tramos 4, 5 y 6 (formato "[N] madre -> hijo (dominio X,
paso senalado P)"), la CABEZA de FILTRO_P91_GUARDA_CADENA para el tramo 7
(formato "N: madre -> hijo (paso P, dominio X) | ..."). El tramo 3 NO TIENE
fichero de pasos: su paso se declara NO RECONSTRUIBLE, tal como manda el
encargo ("si un fichero viejo no se deja leer con un patron... NO se rellena
a mano"). Los tramos 1 y 2 (LECTURA, no ESCRIBIR) son el volcado crudo de
los candidatos SIN ninguna marca de decision: CERO filas se reconstruyen de
ahi, y se declara cuantos candidatos volcaba cada uno.

VERIFICACION CONTRA EL GRAFO DE HOY (EJECUTOR.md regla 2, "el instrumento
manda"; regla 9, "toda perdida se re-verifica contra el grafo"): cada fila
ESCRITA se comprueba contra dataset/metadata/master_graph.json de HOY, en
las DOS vistas. Si la arista YA NO ESTA (revertida despues por una
correccion declarada fuera de estos 7 ficheros), la fila se DEGRADA a NO SE
ENLAZA con una nota; si una fila NO SE ENLAZA SI tiene la arista hoy
(escrita despues por una correccion fuera de estos 7 ficheros, como
`descubrir_necesidades_del_cliente -> traduccion_necesidades_cliente` en la
TAREA 3 de la vuelta 82), se ASCIENDE a ESCRITA con una nota. Ninguna
degradacion o ascenso se teclea: los dos salen de leer dataset/ hoy.

SALIDA: docs/plan/OP_E_01_DECIDIDAS.jsonl (una fila JSON por par decidido:
madre, hijo, paso, tramo, decision, fichero_origen, nota) y un resumen por
stdout con las cuentas de cada bloque, las filas no reconstruidas y las
filas verificadas contra el grafo.
"""
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PLAN = os.path.join(RAIZ, "docs", "plan")

# Un HEADER nunca lleva sangria (empieza en columna 0); una fila de par
# SIEMPRE la lleva (dos espacios). Es la unica distincion fiable: el texto
# del header mezcla mayusculas y minusculas ("ARISTAS ESCRITAS
# (nodos_siguientes Y nodos_previos): 12"), asi que separar por mayuscula
# fallaria.
RE_HEADER = re.compile(r"^(?!\s)(.+?):\s*(\d+)\s*$")
RE_PAR = re.compile(r"^\s{2}([A-Za-z0-9_]+)\s*->\s*([A-Za-z0-9_]+)")

TIPO_HEADER = {
    "ARISTAS ESCRITAS": "ESCRITA",
    "DESCARTADOS": "NO SE ENLAZA",
    "NO ESCRITOS ESTA LECTURA FRESCA, con razon": "NO SE ENLAZA",
    "YA DECIDIDOS EN VUELTAS ANTERIORES (citados, no re-derivados)": "CITA",
}


def clasificar_header(nombre):
    if nombre.startswith("ARISTAS ESCRITAS"):
        return "ESCRITA"
    if nombre.startswith("DESCARTADOS"):
        return "NO SE ENLAZA"
    if nombre.startswith("NO ESCRITOS ESTA LECTURA FRESCA"):
        return "NO SE ENLAZA"
    if nombre.startswith("DISCUTIBLE, NO ESCRITO POR CAUTELA"):
        return "NO SE ENLAZA"
    if nombre.startswith("YA DECIDIDOS EN VUELTAS ANTERIORES"):
        return "CITA"
    return None  # ESCALERA ROTA, YA ESTABAN, TOTAL DE LA CABEZA LEIDA, DISCUTIBLES marcados...


def leer(nombre):
    """Algunos ficheros viejos traen bytes latin-1 sueltos en la prosa
    (mojibake historico); los identificadores que este script necesita son
    siempre ASCII, asi que se lee tolerando el resto con errors='replace'
    en vez de caer entero por un byte de una linea que no se usa."""
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        return None
    return open(ruta, encoding="utf-8", errors="replace").read()


def parsear_escribir(texto, nombre_fichero, tramo):
    """Devuelve (filas_nuevas, citas) de un fichero *_ESCRIBIR.txt.
    filas_nuevas: lista de dict {madre,hijo,decision,fichero_origen,tramo}.
    citas: lista de (madre,hijo) SOLO citadas, no nuevas."""
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
    """Cruce de paso por NOMBRE para tramos 4, 5, 6: formato
    '[N] madre -> hijo  (dominio X, paso senalado P)'."""
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
    """Cruce de paso por NOMBRE para el tramo 7: CABEZA de
    FILTRO_P91_GUARDA_CADENA, formato 'N: madre -> hijo (paso P, dominio X) | ...'."""
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


def contar_pares_lectura_cruda(nombre_fichero):
    """Tramos 1 y 2: cuenta los PAR N volcados, sin decision reconstruible."""
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
    FICHEROS_ESCRIBIR = [
        ("SALIDA_V77_TRAMO3_ESCRIBIR.txt", 3, None, None),
        ("SALIDA_V78_TRAMO4_ESCRIBIR.txt", 4, "dossier30", "SALIDA_V78_TRAMO4_DOSSIER30.txt"),
        ("SALIDA_V79_TRAMO5_ESCRIBIR.txt", 5, "dossier30", "SALIDA_V79_TRAMO5_DOSSIER30.txt"),
        ("SALIDA_V80_TRAMO6_ESCRIBIR.txt", 6, "dossier30", "SALIDA_V80_TRAMO6_DOSSIER30.txt"),
        ("SALIDA_V82_TRAMO7_ESCRIBIR.txt", 7, "filtro_cadena", "SALIDA_V82_TRAMO7_FILTRO_P91_GUARDA_CADENA.txt"),
    ]
    FICHEROS_LECTURA_CRUDA = [
        ("SALIDA_V75_OPE01_TRAMO1_LECTURA.txt", 1),
        ("SALIDA_V76_OPE01_TRAMO2_LECTURA.txt", 2),
    ]

    todas_filas = []
    todas_citas = []
    todas_discrepancias = []
    resumen_por_tramo = []

    for nombre, tramo, modo_paso, fichero_paso in FICHEROS_ESCRIBIR:
        texto = leer(nombre)
        if texto is None:
            print("ROJO: no existe %s, tramo %d no se puede hornear" % (nombre, tramo))
            return 1
        filas, citas, discrepancias = parsear_escribir(texto, nombre, tramo)
        if modo_paso == "dossier30":
            pasos = cargar_paso_dossier30(fichero_paso)
        elif modo_paso == "filtro_cadena":
            pasos = cargar_paso_filtro_cadena(fichero_paso)
        else:
            pasos = {}
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
        resumen_por_tramo.append((tramo, nombre, len(filas), len(citas), sin_paso))

    # Dedupe: si un par aparece como fila nueva en mas de un tramo (no deberia,
    # pero se declara si pasa), se queda con la del tramo MAS BAJO (la decision
    # original), y se cuenta cuantas veces se repitio.
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

    # VERIFICACION CONTRA EL GRAFO DE HOY: EJECUTOR.md regla 2 y regla 9.
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
                         "revertida por una correccion fuera de los 7 ficheros "
                         "hornados, verificado contra dataset/ de hoy"
                         % (f["fichero_origen"], en_sig, en_prev))
            degradadas.append(f)
        elif f["decision"] == "NO SE ENLAZA" and hoy_escrita:
            f["decision"] = "ESCRITA"
            f["nota"] = ("ascendida: %s la marcaba NO SE ENLAZA pero la arista SI "
                         "esta hoy en las dos vistas del grafo; escrita despues por "
                         "una correccion fuera de los 7 ficheros hornados, "
                         "verificado contra dataset/ de hoy" % f["fichero_origen"])
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
    print("HORNEADO docs/plan/OP_E_01_DECIDIDAS.jsonl, TAREA 2.a vuelta 83")
    print("=" * 78)
    print()
    print("--- FILAS NUEVAS POR TRAMO (ESCRIBIR), leidas con patron ---")
    for tramo, nombre, n_filas, n_citas, sin_paso in resumen_por_tramo:
        print("  tramo %d (%s): %d filas nuevas, %d citadas (ya cubiertas), "
              "%d sin paso reconstruible" % (tramo, nombre, n_filas, n_citas, sin_paso))
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
    print("--- TRAMOS 1 Y 2 (LECTURA CRUDA, sin marca de decision) ---")
    total_no_reconstruibles = 0
    for nombre, tramo in FICHEROS_LECTURA_CRUDA:
        n = contar_pares_lectura_cruda(nombre)
        if n is None:
            print("  ROJO: no existe %s" % nombre)
            return 1
        print("  tramo %d (%s): %d candidatos volcados, 0 filas reconstruibles "
              "(el fichero es el volcado crudo de la lectura, sin marca ESCRITA/NO "
              "SE ENLAZA por patron)" % (tramo, nombre, n))
        total_no_reconstruibles += n
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
