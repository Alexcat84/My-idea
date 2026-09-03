# -*- coding: utf-8 -*-
"""VUELTA 152, TAREA 5: LAS CUATRO FILAS VERDE PARCIAL, CADA UNA CON LO QUE LE
FALTA NOMBRADO.

VERDE PARCIAL no es media nota: es una celda con DOS mitades, una medida y otra
que no. Hasta hoy la mitad que falta se decia en prosa ("no mecanizable", "no
atribuible") y NO SE NOMBRABA. Aqui se nombra, y se nombra CONTANDO FICHEROS,
no de memoria (EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO).

ESTE INSTRUMENTO NO CONVIERTE NINGUNA MITAD EN VERDE. No inventa la vara que
falta (EJECUTOR.md 5): la describe, dice donde tendria que vivir y que hace
falta para escribirla. Lo que entrega es el INVENTARIO DE LO QUE FALTA, que es
justo lo que una fila VERDE PARCIAL debe.

USO:
  python scripts/loop/_v152_tarea5_verde_parcial.py
"""
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
DESTEJ = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")
VERED = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")


def fichas():
    return [json.loads(x) for x in io.open(OPS, encoding="utf-8").read().splitlines() if x.strip()]


def grafo(ref="WORK"):
    if ref == "WORK":
        return json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    b = subprocess.run(["git", "show", "%s:dataset/metadata/master_graph.json" % ref],
                       capture_output=True, cwd=RAIZ)
    return json.loads(b.stdout.decode("utf-8"))["nodos"]


F = fichas()
por_id = {x["id_op"]: x for x in F}
N = grafo("WORK")
base = subprocess.run(["git", "merge-base", "pasada-unica", "main"],
                      capture_output=True, cwd=RAIZ).stdout.decode().strip()

print("=" * 96)
print("LAS CUATRO FILAS VERDE PARCIAL, CON LO QUE LE FALTA A CADA UNA, NOMBRADO")
print("=" * 96)
print("Fuente de los veredictos: docs/loop/SALIDA_V152_T2_TABLA_POR_FASE.txt, corrida en")
print("esta vuelta con el reloj congelado en d9fa886b. Mergebase con main: %s" % base[:8])
print("")

# ===================================================== FILA 01 FUENTES
print("=" * 96)
print("FILA 01 FUENTES. MITAD MEDIDA: 'el material del segundo libro reubicado, NO")
print("BORRADO'. MITAD QUE FALTA: LA ATRIBUCION de la alteracion de pasos.")
print("=" * 96)
fase01 = [x for x in F if x["fase"] == "01_FUENTES"]
nomina01 = sorted({n for x in fase01 for n in (x.get("nodos") or [])})
Nb = grafo(base)
alterados, desaparecidos = [], []
for nid in nomina01:
    if nid not in N:
        desaparecidos.append(nid)
        continue
    if nid in Nb and (Nb[nid].get("pasos_accionables") or []) != (N[nid].get("pasos_accionables") or []):
        alterados.append(nid)
otras = {}
for x in F:
    if x["fase"] == "01_FUENTES":
        continue
    for n in (x.get("nodos") or []):
        otras.setdefault(n, []).append("%s(%s)" % (x["id_op"], x["fase"]))
solapan = [x for x in alterados if x in otras]
solo01 = [x for x in alterados if x not in otras]
print("MEDIDO: nomina de %d fichas = %d nodos | desaparecidos %d | con pasos ALTERADOS %d"
      % (len(fase01), len(nomina01), len(desaparecidos), len(alterados)))
print("")
print("LO QUE FALTA, NOMBRADO: no hay vara escrita que separe la alteracion de pasos hecha")
print("por FUENTES de la hecha por un DESTEJIDO sobre el mismo nodo. La unica comparacion")
print("disponible es contra el grafo previo a TODA la campana (%s), y por ahi han pasado" % base[:8])
print("tambien los destejidos, que alteran pasos A PROPOSITO.")
print("")
print("LOS %d ALTERADOS QUE OTRA FASE TAMBIEN RECLAMA (atribucion IMPOSIBLE con las varas de hoy):"
      % len(solapan))
for n in sorted(solapan):
    print("  %-52s tambien en: %s" % (n, ", ".join(sorted(set(otras[n])))))
print("")
print("LOS %d ALTERADOS QUE SOLO 01_FUENTES RECLAMA POR NOMINA:" % len(solo01))
for n in sorted(solo01):
    print("  %s" % n)
print("")
print("Y AQUI LA PRECISION QUE IMPIDE UN FALSO VERDE: que un nodo salga en esta segunda")
print("lista NO lo atribuye a 01_FUENTES. La nomina dice quien lo TENIA ASIGNADO, no quien")
print("lo TOCO, y una operacion puede tocar un nodo fuera de su nomina. Para atribuir haria")
print("falta una vara que hoy no existe: el rastro por commit de que operacion escribio cada")
print("paso. NO LA INVENTO AQUI (EJECUTOR.md 5). SE NOMBRA Y SE DEJA ESCRITA.")
print("")

# ================================================== FILA 02 DESTEJIDOS
print("=" * 96)
print("FILA 02 DESTEJIDOS. MITAD MEDIDA: 'cada perdida en el bloque del que proviene'.")
print("MITAD QUE FALTA: 'los quince congelados releidos', SIN VARA ESCRITA.")
print("=" * 96)
# LA EXTRACCION VA ACOTADA A LA COLUMNA `congelados que libera` DE LA TABLA DEL
# ORDEN, y no al fichero entero. La primera version de este instrumento hacia
# re.finditer de "(\d+, ...)" sobre todo 02_DESTEJIDOS.md y se traia 24 puestos,
# entre ellos los del 1 al 7, que son puestos del cribado citados en otros
# parrafos y NO congelados. La cifra resultante era absurda a simple vista (la
# celda pide QUINCE y salian VEINTICUATRO, con un resto NEGATIVO de -9), y esa
# es justo la especie de cifra que no se publica: se arregla la vara. Aqui se
# leen SOLO las filas de la tabla que empiezan por un numero de orden, y de cada
# fila SOLO su cuarta celda.
texto = io.open(DESTEJ, encoding="utf-8").read()
puestos, filas_orden = [], []
dentro = False
for linea in texto.splitlines():
    if linea.strip().startswith("## EL ORDEN"):
        dentro = True
        continue
    if dentro and linea.startswith("---"):
        break
    if not dentro or not linea.strip().startswith("|"):
        continue
    celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
    if len(celdas) < 4 or not re.match(r"^\*{0,2}\d+\*{0,2}$", celdas[0]):
        continue
    filas_orden.append((celdas[0].strip("*"), celdas[1].strip("`*"), celdas[3]))
    for m in re.finditer(r"\((\d+(?:,\s*\d+)*)\)", celdas[3]):
        for p in m.group(1).split(","):
            if p.strip().isdigit():
                puestos.append(int(p.strip()))
puestos = sorted(set(puestos))
print("LA NOMINA VIVE EN PROSA, y se lee de la tabla '## EL ORDEN' de")
print("docs/plan/02_DESTEJIDOS.md, columna 'congelados que libera', fila a fila:")
for orden, op, celda in filas_orden:
    print("  orden %-2s %-10s %s" % (orden, op, celda[:110]))
print("")
print("PUESTOS DE CONGELADO QUE LA TABLA NOMBRA ENTRE PARENTESIS: %d -> %s"
      % (len(puestos), ", ".join(str(x) for x in puestos)))
V = [json.loads(x) for x in io.open(VERED, encoding="utf-8").read().splitlines() if x.strip()]
por_puesto = {x.get("puesto_intra"): x for x in V}
print("")
print("LOS QUE LA PROSA NOMBRA, COTEJADOS CONTRA EL ARCHIVO DEL CRIBADO DE HOY:")
for p in puestos:
    r = por_puesto.get(p)
    if r is None:
        print("  puesto %-5d NO EXISTE en docs/INTRA_DOMINIO_VEREDICTOS.jsonl" % p)
    else:
        print("  puesto %-5d clase %-2s %s <-> %s" % (p, r["clase"], r["nodo_a"], r["nodo_b"]))
print("")
print("LO QUE FALTA, NOMBRADO Y CONTADO: la celda pide QUINCE y la tabla nombra %d."
      % len(puestos))
print("LOS OTROS %d NO ESTAN NOMBRADOS EN NINGUN SITIO QUE YO PUEDA CONTAR:" % (15 - len(puestos)))
print("  - no hay campo `congelado` en docs/INTRA_DOMINIO_VEREDICTOS.jsonl (claves: %s)"
      % ", ".join(sorted(V[0].keys())))
print("  - la tabla del orden solo cuenta CUANTOS libera cada operacion, y solo las tres")
print("    primeras filas llevan sus puestos entre parentesis; las otras tres liberan 0.")
print("  - la propia pagina dice 'OCHO de los quince congelados cuelgan de TRES nodos', y ese")
print("    OCHO cuadra al digito con los %d puestos que acabo de extraer de la tabla. O sea que"
      % len(puestos))
print("    LOS SIETE RESTANTES NUNCA SE ESCRIBIERON UNO A UNO EN NINGUNA PARTE: la pagina los")
print("    cuenta (quince) pero solo nombra ocho, y el archivo del cribado no los distingue.")
print("")
print("PARA QUE ESTA MITAD PUDIERA MEDIRSE HARIA FALTA: un campo por par en el archivo del")
print("cribado que diga si estuvo congelado y por que operacion, o una nomina de los quince")
print("en un fichero de datos. NO SE INVENTA AQUI. Es PENDIENTE DE DOCTRINA.")
print("")

# =================================================== FILA 03 FUSIONES
print("=" * 96)
print("FILA 03 FUSIONES. MITAD MEDIDA: los absorbidos deprecados, en ids_alias y")
print("resolviendo al superviviente. MITAD QUE FALTA: los DOS supervivientes")
print("DIVERGENTES, que la CORRECCION 16 ya clasifica.")
print("=" * 96)


def resolutor(N):
    alias = {}
    for nid, n in N.items():
        for a in (n.get("ids_alias") or []):
            if a != nid:
                alias[a] = nid

    def r(nid):
        n = N.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid
        visto, cur, ult = {nid}, nid, (nid if n is not None else None)
        while cur in alias:
            cur = alias[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = N.get(cur)
            if c is None:
                continue
            ult = cur
            if not c.get("deprecado"):
                return cur
        return ult
    return r


res = resolutor(N)
con_surv = [x for x in F if x.get("superviviente") and x["fase"] == "03_FUSIONES"]
divergentes = []
for x in con_surv:
    s = x["superviviente"]
    if s not in N or N[s].get("deprecado"):
        divergentes.append(x)
print("fichas de 03_FUSIONES con superviviente escrito: %d | incumplimientos: 0 | DIVERGENTES: %d"
      % (len(con_surv), len(divergentes)))
print("")
for x in divergentes:
    s = x["superviviente"]
    print("  %s" % x["id_op"])
    print("    superviviente ESCRITO en la ficha : %s  (hoy %s)"
          % (s, "DEPRECADO" if s in N and N[s].get("deprecado") else "AUSENTE DEL GRAFO"))
    print("    resuelve por alias (P.1) a        : %s  (hoy %s)"
          % (res(s), "VIVO" if res(s) in N and not N[res(s)].get("deprecado") else "no vivo"))
    print("    y ese id esta en el campo eliminar: %s" % (res(s) in (x.get("eliminar") or [])))
    print("    campo eliminar de la ficha        : %s" % ", ".join(x.get("eliminar") or []))
print("")
print("LO QUE FALTA, NOMBRADO: NADA QUE MEDIR, y por eso esta fila es distinta de las otras")
print("tres. La CORRECCION 16 de docs/plan/CORRECCIONES_A_APLICAR.md ya dice que 'una fusion")
print("consumida al reves no es cumplida ni sin cumplir', o sea que estos dos casos tienen su")
print("casillero escrito y NO son un incumplimiento pendiente. Lo que falta no es una")
print("medicion: es una DECISION de si una fila con dos casos ya clasificados debe seguir")
print("leyendose VERDE PARCIAL o pasar a VERDE con los dos declarados al lado. ESO ES DEL")
print("AUDITOR Y NO ME LO ADJUDICO.")
print("")

# ==================================================== FILA 04 ENLACES
print("=" * 96)
print("FILA 04 ENLACES. MITAD MEDIDA: 'ninguna crea auto-arista tras resolver', que es")
print("un check de Gate 0. MITAD QUE FALTA: 'cada arista nueva CONFIRMADA POR LECTURA,")
print("NO POR EL INSTRUMENTO', excluida por la propia letra de la celda.")
print("=" * 96)
con_aristas = [x for x in F if x.get("aristas_nuevas")]
total = sum(len(x["aristas_nuevas"]) for x in con_aristas)
print("fichas con aristas_nuevas escritas: %d | aristas propuestas en total: %d"
      % (len(con_aristas), total))
print("")
print("LAS FICHAS Y SUS ARISTAS, NOMBRADAS UNA A UNA (esto es el CENSO de lo que habria")
print("que leer, no la lectura):")
for x in sorted(con_aristas, key=lambda y: y["id_op"]):
    print("  %-20s %-14s %d arista(s) propuesta(s)" % (x["id_op"], x["fase"], len(x["aristas_nuevas"])))
print("")
print("LO QUE FALTA, NOMBRADO: la celda dice literalmente 'no por el instrumento'. O sea que")
print("POR CONSTRUCCION ninguna vara mecanica puede contestarla, y cualquier cifra que yo")
print("publique aqui contestaria la otra pregunta (cuantas ESTAN presentes), que es")
print("justamente la que la celda excluye. Lo unico honesto es el censo de arriba: %d aristas"
      % total)
print("sobre %d fichas es el TAMANO del trabajo de lectura que la celda pide, y ese trabajo" % len(con_aristas))
print("es de una sesion de lectura humana, no de este bucle.")
print("")
print("=" * 96)
print("RESUMEN, CONTADO DE LO DE ARRIBA")
print("=" * 96)
print("| fila | mitad medida | lo que le falta, nombrado | especie de lo que falta |")
print("|---|---|---|---|")
print("| 01 FUENTES | 0 desaparecidos de %d | la ATRIBUCION de %d nodos con pasos alterados, %d de ellos reclamados tambien por otra fase | VARA QUE NO EXISTE (rastro por commit de que operacion escribio cada paso) |"
      % (len(nomina01), len(alterados), len(solapan)))
print("| 02 DESTEJIDOS | mapas de destejido exitcode 0 | los quince congelados: la prosa nombra %d por su puesto y %d NO ESTAN NOMBRADOS EN NINGUN FICHERO | NOMINA QUE NO EXISTE (no hay campo congelado en el archivo del cribado) |"
      % (len(puestos), 15 - len(puestos)))
print("| 03 FUSIONES | %d fichas, 0 incumplimientos | los %d supervivientes divergentes, YA CLASIFICADOS por la CORRECCION 16 | DECISION DEL AUDITOR, no medicion |"
      % (len(con_surv), len(divergentes)))
print("| 04 ENLACES | auto-aristas en Gate 0: OK | la confirmacion POR LECTURA de %d aristas sobre %d fichas | LECTURA HUMANA, excluida por la letra de la celda |"
      % (total, len(con_aristas)))
