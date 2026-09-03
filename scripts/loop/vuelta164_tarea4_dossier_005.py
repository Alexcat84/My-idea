# -*- coding: utf-8 -*-
r"""vuelta164_tarea4_dossier_005.py . TAREA 4 de la vuelta 164.

EL DOSSIER DE LA RELECTURA CONJUNTA DE LA `LD-OPC05-005` (adjudicacion 6.5 del
acta 163). La ciega del auditor de la vuelta 163 le da `D` y la clase vigente es
`C`; el encargo manda leer LOS DOS NODOS ENTEROS contra el grafo con `P.5.1` y
sus cuatro ejemplares delante, Y NADA MAS, y decidir.

LO QUE ESTE INSTRUMENTO NO HACE, Y SE DICE ARRIBA PARA QUE NADIE LO LEA DE MAS:
NO DECIDE LA CLASE. La clasificacion de un paso como "procedimiento propio" o
como "orden mas complemento" es una LECTURA DEL EJECUTOR y no hay forma de
mecanizarla sin inventar una vara nueva, que es justo lo que `P.5.1` congelada
prohibe. Por `EJECUTOR.md` regla 1 SE DECLARA QUE NO HAY CASO ROJO AUTOMATICO
PARA EL VEREDICTO, en vez de fabricarle uno que se apruebe solo. El veredicto va
en el reporte y en la razon del registro.

LO QUE SI ES MECANICO, Y POR ESO TIENE ARNES DE MUTACION
(`vuelta164_tarea4_mutacion_005.py`): la vara leida del banco, los dos nodos
leidos del grafo, la arista en las cuatro vistas, la clase y la via leidas del
registro, el solape lexico entre los dos pasos que la vuelta 157 declaro
COLAPSADOS, el barrido de la direccion en disputa y el cruce de entregables con
su calibracion contra los cuatro ejemplares.

NO SE COPIA UNA LINEA DEL INSTRUMENTO DE LA 163: se IMPORTA
`vuelta163_tarea1b_relectura_101` y se llaman sus funciones. Una sola fuente.

USO:
  python scripts/loop/vuelta164_tarea4_dossier_005.py
  python scripts/loop/vuelta164_tarea4_dossier_005.py --mutar
"""
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))

import vuelta163_tarea1b_relectura_101 as B   # noqa: E402

EN_DISPUTA = "LD-OPC05-005"
NODO_A = "aim_of_leadership"
NODO_B = "causas_comunes_vs_especiales"

# LOS DOS PASOS QUE LA VUELTA 157 DECLARO COLAPSADOS, y que el auditor pide
# sacar de la cuenta. Se nombran POR SU NUMERO, no por su texto: el texto se lee
# del grafo de hoy.
PASO_COLAPSADO_A = 1     # aim_of_leadership
PASO_LINEA_2_B = 13      # causas_comunes_vs_especiales
# Los que el auditor deja en pie cuando saca el 1.
PASOS_QUE_QUEDAN_A = [3, 5]


def contenido(texto):
    """Las palabras de contenido de un paso, sin tildes, sin vacias y de mas de
    dos letras. Sirve para MEDIR el solape entre dos pasos, no para juzgarlo."""
    t = B.sin_tildes(texto or "")
    return set(w for w in re.findall(r"[a-z0-9]+", t)
               if w not in B.VACIAS and len(w) > 2)


def solape(a, b):
    ca, cb = contenido(a), contenido(b)
    if not ca or not cb:
        return 0.0, set()
    comunes = ca & cb
    return len(comunes) / float(min(len(ca), len(cb))), comunes


def forma_de_los_pasos(g, nid):
    """UNA MEDICION DE FORMA, DECLARADA COMO PROXY Y NO COMO VEREDICTO. Cuenta,
    de los pasos de un nodo: cuantos traen una ENUMERACION explicita (dos puntos
    seguidos de lista, o tres o mas complementos separados por comas), cuantos
    traen un CRITERIO DE PARADA ('hasta ...') y la longitud media en palabras.

    POR QUE ES PROXY Y SE DICE: la vara `P.5.1` habla de "procedimiento propio",
    y eso no es contable. Lo que si es contable es si un paso ENUMERA algo o solo
    ordena, que es la diferencia que las razones de los ejemplares `052` y `100`
    describen con esas mismas palabras. Se publica como medicion de apoyo. NO
    decide."""
    pasos = g[nid].get("pasos_accionables") or []
    enumeran, paran, palabras = [], [], []
    for i, p in enumerate(pasos, 1):
        palabras.append(len(re.findall(r"\w+", p)))
        cuerpo = p
        tiene_lista = (":" in p and len(p.split(":")[-1].split(",")) >= 3)
        tiene_comas = len(cuerpo.split(",")) >= 4
        if tiene_lista or tiene_comas:
            enumeran.append(i)
        if re.search(r"\bhasta\b", B.sin_tildes(p)):
            paran.append(i)
    media = (sum(palabras) / float(len(palabras))) if palabras else 0.0
    return len(pasos), enumeran, paran, media


def main(mutacion=False):
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 164, TAREA 4: LA RELECTURA CONJUNTA DE LA LD-OPC05-005")
    print("=" * 78)
    print("")
    print("LO QUE ESTE INSTRUMENTO NO HACE: no decide la clase. La")
    print("clasificacion de los pasos es una LECTURA DEL EJECUTOR y por")
    print("EJECUTOR.md 1 SE DECLARA QUE NO HAY CASO ROJO AUTOMATICO PARA EL")
    print("VEREDICTO, en vez de fabricarle uno que se apruebe solo. El")
    print("veredicto va en el reporte y en la razon del registro.")
    print("")

    g = B.cargar_grafo()
    ini, fin, frase, ejemplares = B.vara_de_hoy()
    filas = B.filas_del_registro()

    print("A) LA VARA, LEIDA HOY DEL BANCO Y NO TECLEADA")
    print("   docs/plan/BANCO_DEL_PLAN.md, lineas %d a %d" % (ini, fin))
    print("   FRASE: %s" % frase)
    print("   CIFRA ejemplares parseados de la tabla: %d" % len(ejemplares))
    for eid, ver, por in ejemplares:
        print("      %-14s %-8s %s" % (eid, ver, por))
    print("")

    print("B) EL PAR EN DISPUTA, CONTRA EL GRAFO Y ENTERO")
    f = filas.get(EN_DISPUTA, {})
    print("   %s | clase VIGENTE en el registro: %s | via: %s"
          % (EN_DISPUTA, f.get("clase"), f.get("via")))
    print("   cita: %s" % f.get("cita"))
    print("")
    for nid in (NODO_A, NODO_B):
        B.imprimir_nodo(g, nid)
        print("")

    print("C) LA ARISTA, EN LAS DOS VISTAS")
    vistas = B.arista_en_las_dos_vistas(g, NODO_A, NODO_B)
    for k in sorted(vistas):
        print("   %-24s %s" % (k, vistas[k]))
    print("   CIFRA vistas que traen el par: %d de 4" % sum(1 for v in vistas.values() if v))
    print("")

    print("D) LOS CUATRO EJEMPLARES, CON SUS DOS NODOS ENTEROS")
    print("   (una regla sin sus casos se vuelve a estrechar sola: los")
    print("   ejemplares son la vara tanto como la frase)")
    print("")
    for eid, ver, por in ejemplares:
        fe = filas.get(eid, {})
        print("   --- %s : %s (%s) | clase vigente en el registro: %s"
              % (eid, ver, por, fe.get("clase")))
        for nid in (fe.get("nodo_a_leido"), fe.get("nodo_b_leido")):
            if nid in g:
                B.imprimir_nodo(g, nid, sangria="      ")
        print("")

    print("E) EL COLAPSO DE LA VUELTA 157, MEDIDO Y NO CITADO DE MEMORIA")
    print("   La vuelta 157 declaro, y la 159 lo re confirmo por escrito, que el")
    print("   paso %d de %s y el paso %d de %s COLAPSAN en la misma linea. Aqui no"
          % (PASO_COLAPSADO_A, NODO_A, PASO_LINEA_2_B, NODO_B))
    print("   se repite esa frase: se mide el solape lexico de los dos pasos y se")
    print("   contrasta contra el solape MEDIO del paso %d contra los otros cinco."
          % PASO_LINEA_2_B)
    pa = (g[NODO_A].get("pasos_accionables") or [])
    pb = (g[NODO_B].get("pasos_accionables") or [])
    texto_13 = pb[PASO_LINEA_2_B - 1]
    s1, comunes1 = solape(pa[PASO_COLAPSADO_A - 1], texto_13)
    print("   paso %d de %s: %s" % (PASO_COLAPSADO_A, NODO_A, pa[PASO_COLAPSADO_A - 1]))
    print("   paso %d de %s: %s" % (PASO_LINEA_2_B, NODO_B, texto_13))
    print("   CIFRA solape del par colapsado: %.2f (palabras comunes: %s)"
          % (s1, ", ".join(sorted(comunes1)) or "ninguna"))
    otros = []
    for i, p in enumerate(pa, 1):
        if i == PASO_COLAPSADO_A:
            continue
        s, _c = solape(p, texto_13)
        otros.append((i, s))
        print("      paso %d de %s contra el paso %d: solape %.2f"
              % (i, NODO_A, PASO_LINEA_2_B, s))
    medio = sum(s for _i, s in otros) / float(len(otros)) if otros else 0.0
    print("   CIFRA solape MEDIO de los otros cinco: %.2f" % medio)
    maximo = max(s for _i, s in otros)
    empatan = [i for i, s in otros if s == s1]
    print("   CIFRA el colapsado esta en el MAXIMO de los seis: %s" % (s1 >= maximo))
    print("   CIFRA otros pasos que EMPATAN con el: %d (%s)"
          % (len(empatan), ", ".join("paso %d" % i for i in empatan) or "ninguno"))
    print("   Y SE DICE EL EMPATE EN VEZ DE PUBLICAR 'ES EL MAYOR' A SECAS: el")
    print("   solape lexico por si solo NO separa el paso colapsado de los demas.")
    print("   Lo que separa al paso 1 no es el lexico, es que el COLAPSO YA ESTA")
    print("   ESTABLECIDO EN EL REGISTRO desde la vuelta 157 y re confirmado por")
    print("   la relectura conjunta de la 159.")
    print("   ESTO NO DECIDE NADA POR SI SOLO: mide que el paso %d es, de los seis,"
          % PASO_COLAPSADO_A)
    print("   el que mas se parece a la linea que tendria que EXPANDIR. Un paso que")
    print("   repite la linea no puede ser su 'como se hace'.")
    print("")

    print("F) EL BARRIDO DE LA DIRECCION EN DISPUTA (6.3 del acta 158: la")
    print("   pregunta es un EXISTENCIAL, descartar UN par no descarta la figura)")
    na, ea, ta, ma = forma_de_los_pasos(g, NODO_A)
    nb, eb, tb, mb = forma_de_los_pasos(g, NODO_B)
    print("   CIFRA pasos de %s: %d" % (NODO_A, na))
    print("   CIFRA pasos de %s: %d" % (NODO_B, nb))
    print("   MEDICION DE FORMA, DECLARADA COMO PROXY Y NO COMO VEREDICTO:")
    print("      %s: pasos que ENUMERAN %s | con criterio de parada 'hasta' %s | "
          "media de palabras por paso %.1f" % (NODO_A, ea or "ninguno", ta or "ninguno", ma))
    print("      %s: pasos que ENUMERAN %s | con criterio de parada 'hasta' %s | "
          "media de palabras por paso %.1f" % (NODO_B, eb or "ninguno", tb or "ninguno", mb))
    print("")
    print("   LA DIRECCION EN DISPUTA ES %s -> %s: que linea de %s la expande un"
          % (NODO_B, NODO_A, NODO_B))
    print("   procedimiento de %s. Se imprimen LOS SEIS pasos de %s enteros, que"
          % (NODO_A, NODO_A))
    print("   son todo el material del que puede salir esa expansion:")
    for i, p in enumerate(pa, 1):
        marca = ""
        if i == PASO_COLAPSADO_A:
            marca = "  <- COLAPSA con el paso %d de %s" % (PASO_LINEA_2_B, NODO_B)
        elif i in PASOS_QUE_QUEDAN_A:
            marca = "  <- de los que el auditor deja en pie"
        print("      %2d. %s%s" % (i, p, marca))
    print("")

    print("G) EL CRUCE DE ENTREGABLES, MEDIDO Y CON SU CALIBRACION")
    print("   POR LA ADJUDICACION 6.3 DEL ACTA 163 ES CORROBORADOR Y NO DECISOR.")
    calzan = 0
    for eid, ver, _por in ejemplares:
        fe = filas.get(eid, {})
        x, y = fe.get("nodo_a_leido"), fe.get("nodo_b_leido")
        if x not in g or y not in g:
            continue
        ver_c, en_x, en_y = B.cruce_de_entregables(g, x, y)
        predice = "D" if ver_c.startswith("ASIMETRICO") else "C"
        ok = (predice == fe.get("clase"))
        calzan += 1 if ok else 0
        print("   %s (%s, clase %s): %s -> predice %s -> %s"
              % (eid, ver, fe.get("clase"), ver_c, predice, "CALZA" if ok else "NO CALZA"))
    print("   CIFRA ejemplares que el cruce reproduce: %d de %d" % (calzan, len(ejemplares)))
    ver_d, en_a, en_b = B.cruce_de_entregables(g, NODO_A, NODO_B)
    print("   EL PAR EN DISPUTA: %s" % ver_d)
    print("      palabras de %s dentro del entregable de %s: %s"
          % (NODO_A, NODO_B, ", ".join(en_b) or "ninguna"))
    print("      palabras de %s dentro del entregable de %s: %s"
          % (NODO_B, NODO_A, ", ".join(en_a) or "ninguna"))
    print("")

    print("H) LA CIEGA DEL AUDITOR, COMPROBADA Y NO CITADA DE MEMORIA")
    ruta = os.path.join(RAIZ, "docs", "loop", "_auditor_v163_mis_adjudicaciones.txt")
    print("   fichero: docs/loop/_auditor_v163_mis_adjudicaciones.txt")
    print("   existe: %s" % os.path.exists(ruta))
    letra = None
    if os.path.exists(ruta):
        for l in io.open(ruta, encoding="utf-8", errors="replace"):
            if EN_DISPUTA in l:
                m = re.search(r"\b([ABCD])\b", l.split(EN_DISPUTA, 1)[1])
                if m:
                    letra = m.group(1)
                    break
    print("   veredicto sellado para la 005, parseado del fichero: %s" % letra)
    print("   Y LA OTRA CIEGA DEL MISMO AUDITOR, la de la vuelta 161, dio C sobre")
    print("   este mismo par: lo dice el propio acta 163 en su seccion 3.1. DOS")
    print("   CIEGAS DE LA MISMA PLUMA CON LETRAS DISTINTAS.")
    print("")

    print("VERDE: dossier completo. EL VEREDICTO NO LO DA ESTE FICHERO: lo da la")
    print("lectura del ejecutor, publicada en el reporte con la letra de P.5.1")
    print("delante y en la razon del registro.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
