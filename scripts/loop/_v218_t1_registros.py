# -*- coding: utf-8 -*-
r"""_v218_t1_registros.py . LA TAREA 1 DE LA VUELTA 218: LOS REGISTROS.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). NO ES ARNES NI GUARDA NI LECTOR NUEVO:
lee, mide y registra, que es lo que la moratoria protege.

QUE HACE, EN EL ORDEN DEL ENCARGO:

  1.a  EL RECUENTO CORREGIDO DE LAS DIECISIETE. La tabla NO se teclea: se
       CUENTA del fichero sellado docs/loop/SALIDA_V217_T1_DIECISIETE.txt, y
       encima se aplica LA CORRECCION DECLARADA que adjudica el auditor en su
       5.5 del acta 217: la clausula de 07 ADUANA idx 0 baja de CUBRE a
       A MEDIAS. Las dos cifras enfrentadas se LEEN de sus tres fuentes, la
       celda de la pagina 08, la clausula de indice 3 de OP-A-02 en el
       expediente, y el titulo de la tabla de la pagina 07.

  1.b  LAS CUATRO ADJUDICACIONES A FAVOR DE MI LECTURA, con su numero de
       adjudicacion Y SU LINEA de docs/loop/ACTA_AUDITOR.md, LEIDA DEL FICHERO
       y no recordada (obligacion 6.6 del acta 210, linea 74203).

  1.c  LAS DOS DISCREPANCIAS DE LA CIEGA, MEDIDAS CONTRA EL GRAFO. Los dos
       pares se leen del grafo vivo con el resolutor delante (P.1), y de cada
       uno se publican pasos, entregables y aristas. El veredicto es MIO.
       Si la lectura confirma un cambio de clase, la correccion se ESCRIBE en
       el registro JSONL, declarada y sin borrar el texto viejo, y el marcador
       se RECOMPUTA con su comando.

  1.d  LA PRUEBA DE QUE EL PLAN NO SE TOCA: sha256 del expediente y de la
       pagina 08 al entrar y al salir.

DONDE VA CADA COSA, Y NO SE MEZCLAN. El plan (expediente, pagina 08, pagina 07,
inventario) NO SE TOCA: el encargo lo prohibe con todas sus letras. Lo que SI se
escribe es el REGISTRO DEL CRIBADO, docs/INTRA_DOMINIO_VEREDICTOS.jsonl, que es
donde el modo austero manda que vivan las decisiones de lectura (EJECUTOR.md,
MODO AUSTERO 2: "las decisiones de lectura en el registro JSONL, no narradas en
prosa"), y que es el carril que el auditor nombra en su 5.7: correccion
declarada y recomputo del marcador si el ejecutor confirma contra el grafo.

EL CASO ROJO NO SE PROMETE. Lo que este instrumento mide a maquina son cifras
duras: cuantos pasos trae cada nodo, si estan deprecados, que resuelve el
resolutor, que aristas hay, y si el texto viejo de la razon sobrevive entero
dentro de la nueva. EL MAPEO PASO A PASO ES UNA LECTURA MIA, UNA TABLA A MANO,
Y POR ESO SE DECLARA QUE NO HAY CASO ROJO AUTOMATICO PARA EL en vez de fabricar
uno que se apruebe solo (EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION).

USO:  python scripts/loop/_v218_t1_registros.py
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402
from _v217_t1_diecisiete import V150  # noqa: E402
# IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5, linea 72517 de
# docs/loop/ACTA_AUDITOR.md, leida en esta vuelta). Los lectores grafo() y
# resolutor() viven en scripts/loop/vuelta150_4_tabla_por_fase.py, que HOY NO
# ARRANCA por su propio assert de ocho filas y que la moratoria prohibe
# reparar. El cargador que lo esquiva SIN TOCAR EL FICHERO EN DISCO ya existe
# en _v217_t1_diecisiete.py, asi que se importa de alli en vez de escribirlo
# otra vez. Aqui no se copia ni una linea de ninguno de los dos.

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

ACTA = "docs/loop/ACTA_AUDITOR.md"
EXPEDIENTE = "docs/plan/OPERACIONES.jsonl"
PAG08 = "docs/plan/08_VERIFICACION.md"
PAG07 = "docs/plan/07_ADUANA.md"
VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
T1_217 = "docs/loop/SALIDA_V217_T1_DIECISIETE.txt"

FECHA = "9 sep 2026"


def ruta(rel):
    return os.path.join(RAIZ, rel.replace("/", os.sep))


def leer(rel):
    return io.open(ruta(rel), encoding="utf-8").read().replace(chr(13) + NL, NL)


def lineas(rel):
    return leer(rel).split(NL)


def sha16(rel):
    b = io.open(ruta(rel), "rb").read()
    return (hashlib.sha256(b).hexdigest()[:16],
            hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16])


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def linea_de(texto_lineas, marca):
    """EL NUMERO DE LINEA DONDE VIVE UNA MARCA, LEIDO DEL FICHERO Y NO
    RECORDADO. Devuelve None si no aparece, y ese None se publica."""
    for n, l in enumerate(texto_lineas, start=1):
        if marca in l:
            return n
    return None


def main():
    out = []
    w = out.append
    fallos = 0

    w("=" * 78)
    w("VUELTA %d, TAREA 1. LOS REGISTROS" % VUELTA)
    w("=" * 78)
    w("")

    # ---------------------------------------------------------------- sha ENTRADA
    sha_exp_e = sha16(EXPEDIENTE)
    sha_p08_e = sha16(PAG08)
    sha_p07_e = sha16(PAG07)
    sha_ver_e = sha16(VEREDICTOS)

    # ================================================================== 1.a
    w("1.a. EL RECUENTO CORREGIDO DE LAS DIECISIETE, CON SUS TRES FUENTES LEIDAS")
    w("")
    l08 = lineas(PAG08)
    l07 = lineas(PAG07)
    n_celda = linea_de(l08, "| **07 ADUANA** |")
    n_p07 = linea_de(l07, "CONTROLES MECANICOS QUE LA ACOMPANAN")
    w("   FUENTE 1, LA CELDA: %s, linea %s, LEIDA DEL FICHERO" % (PAG08, n_celda))
    w("      %s" % (l08[n_celda - 1].strip() if n_celda else "(no aparece)"))
    exp = [json.loads(x) for x in lineas(EXPEDIENTE) if x.strip()]
    n_ficha, ficha = None, None
    for n, x in enumerate(lineas(EXPEDIENTE), start=1):
        if x.strip() and json.loads(x)["id_op"] == "OP-A-02":
            n_ficha, ficha = n, json.loads(x)
            break
    ver_ficha = ficha.get("verificacion") or []
    w("   FUENTE 2, LA FICHA: %s, linea %s, id_op %s, fase %s"
      % (EXPEDIENTE, n_ficha, ficha["id_op"], ficha.get("fase")))
    w("      CIFRA clausulas de verificacion de esa ficha: %d | CIFRA indice de "
      "la que decide: 3" % len(ver_ficha))
    w("      VERBATIM idx 3: %s" % ver_ficha[3])
    w("   FUENTE 3, LA PAGINA DE LA FASE: %s, linea %s" % (PAG07, n_p07))
    w("      %s" % (l07[n_p07 - 1].strip() if n_p07 else "(no aparece)"))
    quinto = [l.strip() for l in l07 if "revision de toda nomina por el DOMINIO" in l]
    w("      EL QUINTO, CON SU ORIGEN: %s"
      % (quinto[0] if quinto else "(no aparece)"))
    w("")
    dice_cuatro = "cuatro controles mecanicos" in (l08[n_celda - 1] if n_celda else "")
    dice_cinco = "CINCO controles mecanicos" in ver_ficha[3]
    w("   LAS DOS CIFRAS ENFRENTADAS, CADA UNA CONTADA DE SU FICHERO:")
    w("   CIFRA que la celda de la pagina 08 pide: 4 | CIFRA que la clausula de "
      "la ficha pide: 5")
    w("   la celda dice literalmente 'cuatro controles mecanicos': %s"
      % ("SI" if dice_cuatro else "NO"))
    w("   la ficha dice literalmente 'CINCO controles mecanicos': %s"
      % ("SI" if dice_cinco else "NO"))
    if not dice_cuatro or not dice_cinco:
        fallos += 1
    w("   QUIEN MANDA, Y NO LO INVENTO YO: la correccion declarada de la vuelta "
      "214 escrita en %s dice que las filas no se inventan, se derivan, y que "
      "cada celda se compone de las clausulas de verificacion que las propias "
      "fichas traen. MANDA LA FICHA." % PAG08)
    n_corr = linea_de(l08, "LAS FILAS NO SE INVENTAN")
    w("   esa correccion declarada vive en la linea %s de %s, leida del fichero"
      % (n_corr, PAG08))
    w("")

    w("   LA TABLA DE LAS DIECISIETE, CONTADA DEL FICHERO SELLADO DE LA 217 Y "
      "NO TECLEADA, Y CON LA CORRECCION ENCIMA:")
    filas = []
    for l in lineas(T1_217):
        m = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*"
                     r"(CUBRE|A MEDIAS|NO CUBRE|SIN SONDA)\s*\|\s*(.*?)\s*\|$", l)
        if m:
            filas.append([int(m.group(1)), m.group(2), int(m.group(3)),
                          m.group(4), m.group(5)])
    w("   CIFRA filas armadas leyendo %s: %d | CIFRA que deberia haber: 17"
      % (T1_217, len(filas)))
    if len(filas) != 17:
        fallos += 1
    antes = {}
    for f in filas:
        antes[f[3]] = antes.get(f[3], 0) + 1
    w("   EL REPARTO ANTES DE LA CORRECCION, CONTADO DE ESAS FILAS: CUBRE %d | "
      "A MEDIAS %d | NO CUBRE %d"
      % (antes.get("CUBRE", 0), antes.get("A MEDIAS", 0), antes.get("NO CUBRE", 0)))
    tocadas = 0
    for f in filas:
        if f[1] == "07 ADUANA" and f[2] == 0:
            w("   CORRECCION DECLARADA SOBRE LA FILA %d, %s idx %d: el veredicto "
              "viejo era %s y el nuevo es A MEDIAS. EL VIEJO NO SE BORRA, SE "
              "ESCRIBE AL LADO." % (f[0], f[1], f[2], f[3]))
            f.append(f[3])
            f[3] = "A MEDIAS"
            tocadas += 1
    w("   CIFRA filas tocadas por la correccion: %d | CIFRA que deberia haber: 1"
      % tocadas)
    if tocadas != 1:
        fallos += 1
    ahora = {}
    for f in filas:
        ahora[f[3]] = ahora.get(f[3], 0) + 1
    n_cubre = ahora.get("CUBRE", 0)
    n_medias = ahora.get("A MEDIAS", 0)
    n_no = ahora.get("NO CUBRE", 0)
    w("")
    w("   CIFRA clausulas en CUBRE, RECOMPUTADAS: %d de 17 | CIFRA que la 217 "
      "publico: %d" % (n_cubre, antes.get("CUBRE", 0)))
    w("   CIFRA clausulas en A MEDIAS, RECOMPUTADAS: %d de 17 | CIFRA que la 217 "
      "publico: %d" % (n_medias, antes.get("A MEDIAS", 0)))
    w("   CIFRA clausulas en NO CUBRE, RECOMPUTADAS: %d de 17 | CIFRA que la 217 "
      "publico: %d" % (n_no, antes.get("NO CUBRE", 0)))
    if (n_cubre, n_medias, n_no) != (11, 6, 0):
        fallos += 1
        w("   ROJO: el recomputo no da 11, 6 y 0.")
    w("")
    w("   LA TABLA ENTERA, TRAS LA CORRECCION:")
    w("| # | fila | idx | veredicto | la clausula, VERBATIM |")
    w("|---:|---|---:|---|---|")
    for f in filas:
        nota = (" (CORREGIDA: la 217 publico %s)" % f[5]) if len(f) > 5 else ""
        w("| %d | %s | %d | %s%s | %s |" % (f[0], f[1], f[2], f[3], nota, f[4]))
    w("")
    w("   LAS SEIS QUE NO DAN CUBRE, CON SU FILA Y SU INDICE:")
    seis = [f for f in filas if f[3] != "CUBRE"]
    for f in seis:
        w("   %-14s idx %d | %-9s | %s" % (f[1], f[2], f[3], f[4]))
    w("   CIFRA filas que no dan CUBRE, contadas de esa lista: %d | CIFRA que "
      "deberia haber: 6" % len(seis))
    if len(seis) != 6:
        fallos += 1
    w("")

    # ================================================================== 1.b
    w("=" * 78)
    w("1.b. LAS CUATRO ADJUDICACIONES A FAVOR DE MI LECTURA, CON SU LINEA LEIDA")
    w("=" * 78)
    w("")
    la = lineas(ACTA)
    n_acta217 = linea_de(la, "# ACTA DEL AUDITOR, VUELTA 217")
    w("   EL ACTA 217 EMPIEZA EN LA LINEA %s de %s, LEIDA DEL FICHERO"
      % (n_acta217, ACTA))
    ADJ = [
        ("D.a", "`5.1` `D.a` SE ADJUDICA",
         "01 FUENTES idx 0", "A MEDIAS",
         "la clausula dice pasos ALTERADOS y alterar es cambiar, no contar"),
        ("D.b", "`5.2` `D.b` SE ADJUDICA",
         "01 FUENTES idx 1", "A MEDIAS",
         "un nodo que sigue declarando dos o mas fuentes no ha reubicado nada"),
        ("D.c", "`5.3` `D.c` SE ADJUDICA EN LA LECTURA",
         "02 DESTEJIDOS idx 1", "A MEDIAS",
         "la LECTURA se adjudica al detector ANCHO, nombrar el bloque cumple la "
         "clausula y la formula literal no es la vara, pero el veredicto no sube "
         "con un detector mas ancho"),
        ("D.d", "`5.4` `D.d` SE ADJUDICA",
         "03 FUSIONES idx 0", "A MEDIAS",
         "se sostiene bajo LAS DOS lecturas del universo, la ancha con 71 actos "
         "sin fundir y la estrecha con las SEIS fusiones de 19 nodos que la "
         "remision de la fase 03 dejo enrutadas"),
    ]
    w("   CIFRA adjudicaciones a registrar: %d | CIFRA que deberia haber: 4"
      % len(ADJ))
    if len(ADJ) != 4:
        fallos += 1
    w("")
    w("| rotulo | adjudicacion del acta 217 | su linea, LEIDA | clausula | veredicto que se sostiene | por que |")
    w("|---|---|---:|---|---|---|")
    for rot, marca, clausula, veredicto, porque in ADJ:
        n = linea_de(la, marca)
        if n is None or not (n_acta217 <= n):
            fallos += 1
        w("| **%s** | %s | %s | %s | **%s, SIN CAMBIO** | %s |"
          % (rot, marca.split(" ")[0].strip("`"), n, clausula, veredicto, porque))
    w("")
    n55 = linea_de(la, "`5.5` `D.e` Y `P.1` SE ADJUDICAN JUNTAS")
    w("   Y LA QUINTA, LA QUE SI CAMBIA UNA CIFRA: `D.e` se adjudica en la %s "
      "del acta 217, linea %s, y baja la clausula de 07 ADUANA idx 0 de CUBRE a "
      "A MEDIAS. Es la correccion de la 1.a." % ("5.5", n55))
    if n55 is None:
        fallos += 1
    w("")

    # ================================================================== 1.c
    w("=" * 78)
    w("1.c. LAS DOS DISCREPANCIAS DE LA CIEGA, MEDIDAS CONTRA EL GRAFO")
    w("=" * 78)
    w("")
    N = V150.grafo("WORK")
    res = V150.resolutor(N)
    w("   EL GRAFO ES EL VIVO Y TODO ID PASA POR EL RESOLUTOR ANTES DE CONTAR "
      "(P.1 del banco del plan).")
    w("   CIFRA nodos del grafo vivo: %d" % len(N))
    w("")
    ver = [json.loads(x) for x in lineas(VEREDICTOS) if x.strip()]
    por_puesto = {}
    for d in ver:
        por_puesto.setdefault(d["puesto_intra"], []).append(d)
    w("   CIFRA veredictos en el registro: %d" % len(ver))
    w("")

    def retrato(nid):
        r = res(nid)
        n = N.get(r) or {}
        return {
            "id": nid, "resuelto": r,
            "deprecado": bool(n.get("deprecado")),
            "pasos": list(n.get("pasos_accionables") or []),
            "entregable": n.get("entregable_esperado"),
            "fuente": n.get("fuente"),
            "sig": list(n.get("nodos_siguientes") or []),
            "prev": list(n.get("nodos_previos") or []),
        }

    def publicar(rr):
        w("      NODO %s | resuelve a %s | deprecado: %s | CIFRA pasos: %d"
          % (rr["id"], rr["resuelto"], "SI" if rr["deprecado"] else "NO",
             len(rr["pasos"])))
        w("         entregable: %s" % rr["entregable"])
        for i, p in enumerate(rr["pasos"], start=1):
            w("         paso %2d) %s" % (i, p))

    def arista_entre(a, b):
        ra, rb = res(a), res(b)
        na, nb = N.get(ra) or {}, N.get(rb) or {}
        ida = any(res(x) == rb for x in (na.get("nodos_siguientes") or []))
        vue = any(res(x) == ra for x in (nb.get("nodos_siguientes") or []))
        return ida, vue

    cambios = []

    # ---- PUESTO 299
    w("   PUESTO 299. entrenamiento_de_gerentes_para_despidos contra "
      "proceso_despidos_responsables")
    d299 = por_puesto[299][0]
    w("      CIFRA registros con ese puesto: %d | CIFRA que deberia haber: 1"
      % len(por_puesto[299]))
    if len(por_puesto[299]) != 1:
        fallos += 1
    w("      CLASE EN EL ARCHIVO AL ENTRAR: %s" % d299["clase"])
    hijo = retrato("entrenamiento_de_gerentes_para_despidos")
    madre = retrato("proceso_despidos_responsables")
    publicar(madre)
    publicar(hijo)
    ida, vue = arista_entre(madre["id"], hijo["id"])
    w("      ARISTA, DATO DEL GRAFO Y NO ARGUMENTO (no acusa cuando falta ni "
      "exculpa cuando esta): de la madre al hijo %s | del hijo a la madre %s"
      % ("SI" if ida else "NO", "SI" if vue else "NO"))
    w("      LA VARA ES EL BANCO 9.6.2, COMO SE RECONOCE UN PAR MADRE E HIJO: el "
      "hijo cabe entero dentro de UN paso de la madre, y la madre conserva "
      "materia propia que el hijo no toca en ningun paso.")
    w("      CONDICION 1, LEIDA Y NO CONTADA: los CUATRO pasos del hijo caen "
      "dentro del paso 4 de la madre. EL MAPEO ES LECTURA MIA, UNA TABLA A "
      "MANO, Y SE DECLARA QUE NO HAY CASO ROJO AUTOMATICO PARA EL.")
    w("         hijo 1 -> madre 4, 'despida personalmente a su propio equipo'")
    w("         hijo 2 -> madre 4, 'explicando la situacion' y 'la decision es "
      "innegociable'")
    w("         hijo 3 -> madre 4, 'detallando los beneficios y apoyo disponibles'")
    w("         hijo 4 -> los simulacros son el DESPLIEGUE de ese paso, que la "
      "madre nombra y no ejecuta")
    propios = [1, 2, 5]
    w("      CONDICION 2: la madre conserva %d pasos que el hijo no toca, los "
      "numeros %s." % (len(propios), propios))
    for i in propios:
        w("         madre %d) %s" % (i, madre["pasos"][i - 1]))
    w("      LA SENAL DE VERIFICACION DEL 9.6.2, LOS ENTREGABLES: la madre "
      "entrega tres productos y el hijo entrega el primero de los tres. Es el "
      "perfil del 2.215.")
    w("      MI VEREDICTO CONTRA EL GRAFO: LAS DOS CONDICIONES SE CUMPLEN, Y LA "
      "REGLA NO ADMITE EL EMPATE. LA CLASE PASA DE B A D.")
    cambios.append((299, "D", d299))

    w("")
    # ---- PUESTO 1249
    w("   PUESTO 1249. cierre_segun_complejidad_venta contra "
      "relacion_continua_con_cliente")
    d1249 = por_puesto[1249][0]
    w("      CIFRA registros con ese puesto: %d | CIFRA que deberia haber: 1"
      % len(por_puesto[1249]))
    if len(por_puesto[1249]) != 1:
        fallos += 1
    w("      CLASE EN EL ARCHIVO AL ENTRAR: %s" % d1249["clase"])
    grande = retrato("cierre_segun_complejidad_venta")
    chico = retrato("relacion_continua_con_cliente")
    publicar(grande)
    publicar(chico)
    ida2, vue2 = arista_entre(grande["id"], chico["id"])
    w("      ARISTA, DATO DEL GRAFO Y NO ARGUMENTO: del grande al chico %s | del "
      "chico al grande %s" % ("SI" if ida2 else "NO", "SI" if vue2 else "NO"))
    w("      LA CIFRA QUE LA RAZON VIEJA PUBLICA, CITADA VERBATIM DEL ARCHIVO: "
      "'Lo compartido es una linea, no uses estilos agresivos, y esta en un paso "
      "de cada uno'.")
    tiene = ("Lo compartido es una linea, no uses estilos agresivos, y esta en "
             "un paso de cada uno") in d1249["razon"]
    w("      esa frase esta en la razon del archivo: %s" % ("SI" if tiene else "NO"))
    if not tiene:
        fallos += 1
    w("      MEDIDO HOY CONTRA EL GRAFO, ESA CIFRA ES FALSA POR DOS LADOS:")
    w("      CIFRA pasos que la razon vieja enumera de cierre_segun_complejidad_venta: 5 | "
      "CIFRA pasos que el nodo trae hoy: %d" % len(grande["pasos"]))
    if len(grande["pasos"]) != 12:
        fallos += 1
    w("      CIFRA pasos de relacion_continua_con_cliente con contraparte: 3 | "
      "CIFRA pasos que trae: %d" % len(chico["pasos"]))
    w("         chico 1 -> grande 7, construir la relacion en base a confianza")
    w("         chico 4 -> grande 8, la estrategia de seguimiento entre llamadas")
    w("         chico 3 -> grande 3 y grande 12, minimizar tecnicas y medir si "
      "danan la relacion")
    w("         chico 2 -> SIN contraparte: anticipar y comunicar el soporte "
      "post-venta disponible")
    w("      EL MAPEO ES LECTURA MIA, TABLA A MANO, Y NO LLEVA CASO ROJO "
      "AUTOMATICO. Lo que si es maquina son las dos cifras de pasos de arriba.")
    w("      LA REGLA QUE DECIDE NO ES LA DEL SOLAPE. El 9.6.2 no aplica en modo "
      "madre e hijo, porque su prueba de reconocimiento pide que el chico quepa "
      "entero dentro de UN paso del grande y aqui toca CUATRO pasos distintos, "
      "el 3, el 7, el 8 y el 12. Manda el 9.6.3: la vara no cuenta cuantos pasos "
      "se comparten, pregunta que queda FUERA del solape y en que lado.")
    w("      FUERA DEL SOLAPE, EL GRANDE CONSERVA 8 de sus %d pasos, y son "
      "procedimiento y son la tesis del racimo: 1, 2, 4, 5, 6, 9, 10 y 11."
      % len(grande["pasos"]))
    w("      FUERA DEL SOLAPE, EL CHICO CONSERVA su paso 2 y su entregable, un "
      "plan con puntos de contacto DURANTE Y DESPUES de la venta, donde el paso "
      "8 del grande solo cubre el seguimiento ENTRE LLAMADAS, o sea durante.")
    w("      Y LA CUENTA DEL RACIMO NO CAMBIA: cuatro lecturas, 520, 1206, 1217 y "
      "esta, dejan a relacion_continua_con_cliente ADYACENTE al racimo del cierre "
      "y no miembro. El 520 ademas lo declara HIJO CON CASA PROPIA de otra madre.")
    for p in (520, 1206, 1217):
        w("         PUESTO %-5d clase en el archivo: %s"
          % (p, por_puesto[p][0]["clase"]))
    w("      MI VEREDICTO CONTRA EL GRAFO: LA CLASE NO CAMBIA, SIGUE SIENDO D. "
      "LA RAZON SI SE CORRIGE, Y LO DIGO SIN MAQUILLAJE: con la cifra corregida "
      "el margen de esta D es MUCHO MAS ESTRECHO que el que la razon vieja "
      "pintaba, y por eso sube marcada como DISCUTIBLE.")
    cambios.append((1249, "D", d1249))
    w("")

    # ================================================================== 1.d
    w("=" * 78)
    w("1.d. LO QUE SE ESCRIBE EN EL REGISTRO DEL CRIBADO, DECLARADO Y SIN TAPAR")
    w("=" * 78)
    w("")
    w("   DONDE SE ESCRIBE, Y DONDE NO. Se escribe en %s, que es el registro del "
      "cribado. NO se escribe en el plan: ni el expediente, ni la pagina 08, ni "
      "la pagina 07, ni el inventario." % VEREDICTOS)
    w("")

    n217_57 = linea_de(la, "`5.7` LA DISCREPANCIA `299` SE ADJUDICA") \
        or linea_de(la, "`5.7` LA DISCREPANCIA `299`")
    n217_58 = linea_de(la, "`5.8` LA DISCREPANCIA `1249`")
    w("   la adjudicacion 5.7 del acta 217 vive en la linea %s de %s, leida del "
      "fichero" % (n217_57, ACTA))
    w("   la adjudicacion 5.8 del acta 217 vive en la linea %s de %s, leida del "
      "fichero" % (n217_58, ACTA))
    if n217_57 is None or n217_58 is None:
        fallos += 1
    w("")

    razon_vieja_299 = d299["razon"]
    razon_vieja_1249 = d1249["razon"]

    nueva_299 = (
        "CORRECCION DECLARADA EL %(f)s (vuelta %(v)d, TAREA 1.c). LA CLASE CAMBIA: DE B A D. "
        "EL CASO LO ESCRIBE EL AUDITOR EN SU ADJUDICACION 5.7 DEL ACTA 217, linea %(l57)s de "
        "docs/loop/ACTA_AUDITOR.md leida hoy del fichero, y LO VERIFICA Y LO DECIDE EL EJECUTOR "
        "CONTRA EL GRAFO, que es el carril de relectura conjunta que esa misma adjudicacion fija. "
        "LA VARA ES EL BANCO 9.6.2, COMO SE RECONOCE UN PAR MADRE E HIJO: el hijo cabe entero "
        "dentro de UN paso de la madre, y la madre conserva materia propia que el hijo no toca en "
        "ningun paso; si eso se cumple, la pregunta ya solo puede hacerse en un sentido. "
        "MEDIDO CONTRA EL GRAFO VIVO CON EL RESOLUTOR DELANTE, los dos nodos vivos y sin deprecar: "
        "proceso_despidos_responsables trae %(nm)d pasos y entrenamiento_de_gerentes_para_despidos "
        "trae %(nh)d. PRIMERA CONDICION: los cuatro pasos del hijo caen dentro del paso 4 de la "
        "madre, entrenar a cada gerente para que despida personalmente a su propio equipo "
        "explicando la situacion, dejando claro que la decision es innegociable y detallando los "
        "beneficios y apoyo disponibles. El 1 con despida personalmente a su propio equipo, el 2 "
        "con explicando la situacion y la decision es innegociable, el 3 con detallando los "
        "beneficios y apoyo disponibles, y el 4, los simulacros o ensayos de la conversacion, es "
        "el DESPLIEGUE que ese paso nombra y no ejecuta. SEGUNDA CONDICION: la madre conserva TRES "
        "pasos que el hijo no toca en ninguno de los suyos, aceptar mentalmente la responsabilidad "
        "de la decision antes de actuar, minimizar el tiempo entre la decision y la ejecucion para "
        "evitar filtraciones, y comunicar a toda la empresa lo sucedido despues de ejecutado el "
        "despido. LA SENAL DE VERIFICACION DEL 9.6.2, LOS ENTREGABLES, APUNTA IGUAL Y ES EL PERFIL "
        "DEL 2.215: la madre entrega protocolo escrito con guion, cronograma de ejecucion y plan de "
        "comunicacion interna, tres productos, y el hijo entrega el guion estandarizado y la sesion "
        "de capacitacion, que es el primero de los tres. QUE ANADE EL HIJO A LA MADRE, que es la "
        "unica direccion en que la pregunta se puede hacer: el guion como producto estandarizado, la "
        "entrega de toda la informacion de paquetes de beneficios ANTES de la conversacion, y los "
        "simulacros. Eso es procedimiento, no linea: el paso 4 de la madre es una linea que tarda "
        "cuatro pasos en ejecutarse, y la prueba de que es un procedimiento es que existe el hijo "
        "que lo ejecuta. POR QUE LA B NO SE SOSTIENE: la razon vieja acreditaba LAS DOS CONDICIONES "
        "y luego declaraba el empate con un no lo decido. La regla no admite el empate, y el "
        "desprendimiento que la razon vieja ofrecia como segunda lectura es exactamente lo que el "
        "9.6.2 llama madre e hijo. ARISTA: DATO DEL GRAFO Y NO ARGUMENTO, no acusa cuando falta ni "
        "exculpa cuando esta. Medida hoy resolviendo por alias, NO HAY ARISTA en ninguno de los dos "
        "sentidos entre los dos nodos. EL MARCADOR SE RECOMPUTA EN LA MISMA VUELTA, con "
        "python scripts/recomputar_marcador.py 3388, y las cifras de antes y de despues se publican "
        "juntas en el reporte de la vuelta %(v)d. LO QUE DECIA LA RAZON VIEJA, y se deja escrita "
        "ENTERA para que la correccion se pueda auditar, copiada del archivo por maquina y no "
        "transcrita: %(vieja)s FIN DE LA RAZON VIEJA."
    ) % {"f": FECHA, "v": VUELTA, "l57": n217_57,
         "nm": len(madre["pasos"]), "nh": len(hijo["pasos"]),
         "vieja": razon_vieja_299}

    nueva_1249 = (
        "CORRECCION DECLARADA EL %(f)s (vuelta %(v)d, TAREA 1.c). LA CLASE NO CAMBIA, SIGUE SIENDO "
        "D. LO QUE SE CORRIGE ES LA CIFRA CON QUE LA RAZON VIEJA LA SOSTENIA, y la trae el auditor "
        "en su adjudicacion 5.8 del acta 217, linea %(l58)s de docs/loop/ACTA_AUDITOR.md leida hoy "
        "del fichero. LA CIFRA VIEJA DECIA que lo compartido era una linea, no uses estilos "
        "agresivos, y que estaba en un paso de cada uno. MEDIDO HOY CONTRA EL GRAFO ESO ES FALSO "
        "POR DOS LADOS. PRIMERO: cierre_segun_complejidad_venta trae %(ng)d pasos y la razon vieja "
        "enumeraba cinco, o sea que leyo menos de la mitad del nodo. SEGUNDO: TRES de los %(nc)d "
        "pasos de relacion_continua_con_cliente tienen contraparte en el otro nodo, el 1 con el 7, "
        "el 4 con el 8, y el 3 con el 3 y el 12; el unico sin contraparte es el 2, anticipar y "
        "comunicar claramente el soporte post-venta disponible. LA CLASE SE SOSTIENE, Y NO POR LA "
        "CIFRA SINO POR LAS DOS REGLAS QUE DECIDEN. UNA: el 9.6.2 no aplica en modo madre e hijo, "
        "porque su prueba de reconocimiento pide que el nodo pequeno quepa entero dentro de UN paso "
        "del grande, y aqui toca CUATRO pasos distintos, el 3, el 7, el 8 y el 12. DOS: manda el "
        "9.6.3, que es el simetrico, la vara no cuenta cuantos pasos comparten dos nodos, pregunta "
        "que queda FUERA del solape y en que lado. Fuera del solape cierre_segun_complejidad_venta "
        "conserva OCHO de sus doce pasos, y son procedimiento y son la tesis del racimo: clasificar "
        "la venta por valor, sofisticacion, relacion posventa, ciclo, monto y visibilidad; aplicar "
        "tecnicas tradicionales sin restriccion si es pequena; revisar el proceso completo y no solo "
        "el cierre; capacitar al equipo diferenciando por tipo de venta; medir tiempo de transaccion "
        "y tasa de exito antes y despues; anticipar que el cliente evaluara la relacion en "
        "decisiones grandes; auditar el uso de tecnicas de cierre por observacion de llamadas "
        "reales; y comparar tasas de exito entre vendedores que usan muchas tecnicas y pocos. Fuera "
        "del solape relacion_continua_con_cliente conserva su paso 2 y su entregable, un plan de "
        "relacion con puntos de contacto DURANTE Y DESPUES de cerrada la venta, donde el paso 8 del "
        "otro solo cubre el seguimiento ENTRE LLAMADAS, o sea durante. Y LA CUENTA DEL RACIMO NO "
        "CAMBIA: cuatro lecturas, los puestos 520, 1206, 1217 y esta, dejan a "
        "relacion_continua_con_cliente ADYACENTE al racimo del cierre y no miembro, y el 520 ademas "
        "lo declara HIJO CON CASA PROPIA de otra madre, diferencias_venta_pequena_venta_grande, de "
        "modo que fundirlo aqui borraria esa lectura. ARISTA: DATO DEL GRAFO Y NO ARGUMENTO. Medida "
        "hoy resolviendo por alias, HAY ARISTA de cierre_segun_complejidad_venta a "
        "relacion_continua_con_cliente y no en el otro sentido; no acusa ni exculpa y por eso no "
        "entra en el razonamiento. Y SE DICE SIN MAQUILLAJE, PORQUE LA CORRECCION APRIETA LA VARA: "
        "con la cifra corregida el margen de esta D es MUCHO MAS ESTRECHO que el que la razon vieja "
        "pintaba, lo que el nodo pequeno conserva fuera del solape es UN paso y su entregable, y por "
        "eso la vuelta %(v)d la sube marcada como DISCUTIBLE para que el auditor la pueda voltear. "
        "LO QUE DECIA LA RAZON VIEJA, y se deja escrita ENTERA para que la correccion se pueda "
        "auditar, copiada del archivo por maquina y no transcrita: %(vieja)s FIN DE LA RAZON VIEJA."
    ) % {"f": FECHA, "v": VUELTA, "l58": n217_58,
         "ng": len(grande["pasos"]), "nc": len(chico["pasos"]),
         "vieja": razon_vieja_1249}

    NUEVAS = {299: ("D", nueva_299), 1249: ("D", nueva_1249)}

    w("   EL MARCADOR ANTES DE ESCRIBIR, RECOMPUTADO CON SU COMANDO:")
    cod, mar_antes = git(["--version"])  # placeholder para no dejar cod suelto
    r = subprocess.run([sys.executable, "scripts/recomputar_marcador.py", "3388"],
                       cwd=RAIZ, capture_output=True,
                       env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    mar_antes = r.stdout.decode("utf-8", "replace")
    for l in mar_antes.split(NL)[:12]:
        if l.strip():
            w("      | " + l.rstrip())

    crudo = io.open(ruta(VEREDICTOS), encoding="utf-8", newline="").read()
    if chr(13) in crudo:
        w("   ROJO: el registro trae retornos de carro y este instrumento no los "
          "conserva. NO SE ESCRIBE.")
        fallos += 1
    filas_jsonl = crudo.split(NL)
    tocadas_jsonl, roundtrip_ok = 0, 0
    salida = []
    for l in filas_jsonl:
        if not l.strip():
            salida.append(l)
            continue
        d = json.loads(l)
        p = d["puesto_intra"]
        if p in NUEVAS and json.dumps(d, ensure_ascii=False) == l:
            roundtrip_ok += 1
            vieja_clase = d["clase"]
            d["clase"], d["razon"] = NUEVAS[p]
            nueva_l = json.dumps(d, ensure_ascii=False)
            salida.append(nueva_l)
            tocadas_jsonl += 1
            w("   TOCADO puesto %-5d | clase %s -> %s | razon vieja dentro de la "
              "nueva: %s | bytes de razon %d -> %d"
              % (p, vieja_clase, d["clase"],
                 "SI" if (razon_vieja_299 if p == 299 else razon_vieja_1249)
                 in d["razon"] else "NO",
                 len((razon_vieja_299 if p == 299 else razon_vieja_1249)
                     .encode("utf-8")),
                 len(d["razon"].encode("utf-8"))))
            if (razon_vieja_299 if p == 299 else razon_vieja_1249) not in d["razon"]:
                fallos += 1
        elif p in NUEVAS:
            w("   ROJO: la linea del puesto %d no vuelve identica al serializarla, "
              "asi que NO se toca." % p)
            fallos += 1
            salida.append(l)
        else:
            salida.append(l)
    w("   CIFRA lineas tocadas: %d | CIFRA que deberia haber: 2" % tocadas_jsonl)
    w("   CIFRA lineas cuyo serializado vuelve identico antes de tocarlas: %d | "
      "CIFRA que deberia haber: 2" % roundtrip_ok)
    if tocadas_jsonl != 2 or roundtrip_ok != 2:
        fallos += 1

    texto_nuevo = NL.join(salida)
    dif = sum(1 for a, b in zip(filas_jsonl, salida) if a != b)
    w("   CIFRA lineas del registro que difieren del original: %d | CIFRA que "
      "deberia haber: 2" % dif)
    w("   CIFRA lineas del registro antes: %d | CIFRA despues: %d"
      % (len(filas_jsonl), len(salida)))
    if dif != 2 or len(filas_jsonl) != len(salida):
        fallos += 1

    if fallos:
        w("")
        w("   ROJO: NO SE ESCRIBE NADA EN EL REGISTRO. Fallos: %d" % fallos)
    else:
        io.open(ruta(VEREDICTOS), "w", encoding="utf-8", newline="").write(texto_nuevo)
        w("   ESCRITO %s" % VEREDICTOS)
        de_nuevo = io.open(ruta(VEREDICTOS), encoding="utf-8", newline="").read()
        w("   RELECTURA DEL DISCO: identico a lo juzgado: %s"
          % ("SI" if de_nuevo == texto_nuevo else "NO"))
        if de_nuevo != texto_nuevo:
            fallos += 1
        comp = [json.loads(x) for x in de_nuevo.split(NL) if x.strip()]
        w("   CIFRA veredictos releidos del disco: %d | CIFRA que habia: %d"
          % (len(comp), len(ver)))
        if len(comp) != len(ver):
            fallos += 1
        w("")
        w("   EL MARCADOR DESPUES DE ESCRIBIR, RECOMPUTADO CON EL MISMO COMANDO:")
        r2 = subprocess.run([sys.executable, "scripts/recomputar_marcador.py", "3388"],
                            cwd=RAIZ, capture_output=True,
                            env=dict(os.environ, PYTHONIOENCODING="utf-8"))
        mar_desp = r2.stdout.decode("utf-8", "replace")
        for l in mar_desp.split(NL)[:12]:
            if l.strip():
                w("      | " + l.rstrip())

        def clases_de(t):
            c, dentro = {}, False
            for l in t.split(NL):
                if l.strip() == "MARCADOR GLOBAL":
                    dentro = True
                    continue
                if dentro:
                    m = re.match(r"^\s+([ABCD])\s+(\d+)\s", l)
                    if m:
                        c[m.group(1)] = int(m.group(2))
                    elif not l.strip():
                        dentro = False
            return c
        ca, cd = clases_de(mar_antes), clases_de(mar_desp)
        w("")
        w("   EL MARCADOR, LAS DOS CIFRAS JUNTAS Y NINGUNA TECLEADA:")
        for k in ("A", "B", "C", "D"):
            w("      clase %s | ANTES %d | DESPUES %d | movimiento %+d"
              % (k, ca.get(k, 0), cd.get(k, 0), cd.get(k, 0) - ca.get(k, 0)))
        esperado = (ca.get("B", 0) - 1 == cd.get("B", 0)
                    and ca.get("D", 0) + 1 == cd.get("D", 0)
                    and ca.get("A", 0) == cd.get("A", 0)
                    and ca.get("C", 0) == cd.get("C", 0))
        w("   EL MOVIMIENTO ES EL QUE LA CORRECCION PREDICE, una B menos y una D "
          "mas, y nada mas se mueve: %s" % ("SI" if esperado else "NO"))
        if not esperado:
            fallos += 1
        io.open(os.path.join(LOOP, "SALIDA_V%d_T1_MARCADOR_ANTES.txt" % VUELTA),
                "w", encoding="utf-8", newline=NL).write(mar_antes)
        io.open(os.path.join(LOOP, "SALIDA_V%d_T1_MARCADOR_DESPUES.txt" % VUELTA),
                "w", encoding="utf-8", newline=NL).write(mar_desp)
        w("   los dos recomputos quedan sellados en "
          "docs/loop/SALIDA_V%d_T1_MARCADOR_ANTES.txt y en "
          "docs/loop/SALIDA_V%d_T1_MARCADOR_DESPUES.txt" % (VUELTA, VUELTA))
    w("")

    # ================================================================== 1.e
    w("=" * 78)
    w("1.e. EL PLAN NO SE TOCA, Y SE PRUEBA CON LOS SHA DE ENTRADA Y DE SALIDA")
    w("=" * 78)
    sha_exp_s = sha16(EXPEDIENTE)
    sha_p08_s = sha16(PAG08)
    sha_p07_s = sha16(PAG07)
    sha_ver_s = sha16(VEREDICTOS)
    w("SHA256 DE %s AL ENTRAR: %s disco y %s LF" % ((EXPEDIENTE,) + sha_exp_e))
    w("SHA256 DE %s AL SALIR: %s disco y %s LF" % ((EXPEDIENTE,) + sha_exp_s))
    w("SHA256 DE %s AL ENTRAR: %s disco y %s LF" % ((PAG08,) + sha_p08_e))
    w("SHA256 DE %s AL SALIR: %s disco y %s LF" % ((PAG08,) + sha_p08_s))
    w("SHA256 DE %s AL ENTRAR: %s disco y %s LF" % ((PAG07,) + sha_p07_e))
    w("SHA256 DE %s AL SALIR: %s disco y %s LF" % ((PAG07,) + sha_p07_s))
    coinciden = (sha_exp_e == sha_exp_s and sha_p08_e == sha_p08_s
                 and sha_p07_e == sha_p07_s)
    w("LOS SEIS SHA DEL PLAN COINCIDEN CON LOS DE LA ENTRADA: %s"
      % ("SI" if coinciden else "NO"))
    if not coinciden:
        fallos += 1
    w("")
    w("Y LA SEDE QUE SI SE MUEVE, DICHA EN VOZ ALTA Y NO ESCONDIDA:")
    w("SHA256 DE %s AL ENTRAR: %s disco y %s LF" % ((VEREDICTOS,) + sha_ver_e))
    w("SHA256 DE %s AL SALIR: %s disco y %s LF" % ((VEREDICTOS,) + sha_ver_s))
    w("ESA SEDE SE MOVIO A PROPOSITO: %s"
      % ("SI" if sha_ver_e != sha_ver_s else "NO"))
    m = medir_en_disco(RAIZ, VEREDICTOS)
    w("CIFRA bytes de %s al salir: %d en disco y %d normalizado a LF"
      % (VEREDICTOS, m[0], m[1]))
    w("")
    w("CIFRA comprobaciones que fallan: %d" % fallos)
    w("VERDE: la TAREA 1 sale limpia." if not fallos
      else "ROJO: la TAREA 1 tiene comprobaciones que fallan.")

    texto = NL.join(out) + NL
    destino = os.path.join(LOOP, "SALIDA_V%d_T1_REGISTROS.txt" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    sys.stdout.write(NL + "SELLADO EN %s, %d bytes%s"
                     % (os.path.basename(destino), os.path.getsize(destino), NL))
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
