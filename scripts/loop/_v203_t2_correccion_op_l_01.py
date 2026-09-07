# -*- coding: utf-8 -*-
r"""_v203_t2_correccion_op_l_01.py . TAREA 2 DE LA VUELTA 203: LA CORRECCION
DECLARADA DE LA `verificacion` DE `OP-L-01`, EN SU SEDE Y POR ADICION.

ADJUDICADA POR EL ACTA 202 EN SU `4.4`. El ejecutor de la 202 hizo bien en
medirla y preguntar (`P.2`); ahora esta adjudicada y se escribe.

EL CARRIL, IDENTICO AL DE `OP-L-03` DE LA 202: banco `9.10`, POR ADICION, **un
elemento mas de la misma lista `verificacion`**, sin clave nueva de esquema y
sin tocar ni tachar el texto viejo. La ficha vive en la LINEA 41 y se cita por
LINEA MAS INDICE, con las DOS numeraciones del indice publicadas (base 0 de
Python y base 1 del encargo) para que ninguna cita quede ambigua.

NINGUN INSTRUMENTO SE CLONA Y NINGUNO SE TOCA: `vuelta166_tarea2_correccion_op_
l_01.py` se IMPORTA, y ANTES de llamarlo se lee su codigo para comprobar que en
modo medicion no escribe. **Se comprueba de verdad**, que es la caida `C.2` del
auditor de la 202.

LAS TRES COSAS QUE LA CORRECCION TIENE QUE DECIR, LAS TRES OBLIGATORIAS Y LAS
TRES MEDIDAS HOY:

  1. que `las_once()` NO devuelve once: devuelve toda cabecera `LD` que haya hoy
     en `docs/plan/LECTURAS_DIRIGIDAS.md`. La cifra de HOY y la del corte
     2026-09-04, **las dos leidas y ninguna tecleada**: la vieja sale de
     `git show` del fichero en el commit de ese corte, contada con LA MISMA
     expresion regular.
  2. la comparacion RESUELTA de hoy contra la congelada, y los puestos
     implicados, cada cifra con su corte.
  3. LA QUE NO PUEDE FALTAR: que en comparacion LITERAL siguen apareciendo 0, o
     sea que LA CLAUSULA 1 NO SE CAE. Sin esa linea la correccion se leeria como
     que la clausula se rompio, y es falso.

USO:
  python scripts/loop/_v203_t2_correccion_op_l_01.py
  python scripts/loop/_v203_t2_correccion_op_l_01.py --escribir
  python scripts/loop/_v203_t2_correccion_op_l_01.py --escribir --salida NOMBRE
"""
import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

sys.path.insert(0, AQUI)
import vuelta166_tarea2_correccion_op_l_01 as I166           # noqa: E402

OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
INSTRUMENTO = "scripts/loop/vuelta166_tarea2_correccion_op_l_01.py"
LECTURAS_REL = "docs/plan/LECTURAS_DIRIGIDAS.md"
ID_OP = "OP-L-01"
LINEA_ESPERADA = 41
CORTE_VIEJO = "2026-09-04"
CORTE = "2026-09-07"
VUELTA_QUE_ESCRIBE = 203
MARCA = ("CORRECCION DECLARADA (2026-09-07, vuelta 203, TAREA 2 del encargo), "
         "POR EL CARRIL DEL BANCO 9.10")

# LA MARCA DE ESCRITURA EN DISCO. No es una guarda nueva que se quede vigilando:
# es una expresion regular de este mismo computo de una vuelta, que muere con
# el y no entra en el censo ni en la nomina.
PATRON_ESCRITURA = re.compile(
    r"open\s*\([^)]*[" + chr(34) + chr(39) + r"](w|wb|a|ab|w\+|r\+)["
    + chr(34) + chr(39) + r"]|\.write\s*\(|os\.remove|shutil\.|os\.rename"
    r"|os\.makedirs|json\.dump\s*\(")


def dos_convenciones(rel):
    ruta = os.path.join(RAIZ, rel)
    d = io.open(ruta, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return len(d), len(lf), hashlib.sha256(lf).hexdigest()[:16], lf.decode("utf-8")


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def fichas():
    """(linea, dict) DE CADA FICHA, leidas del disco AHORA."""
    salida = []
    for i, l in enumerate(io.open(OPS, encoding="utf-8").read()
                          .replace(chr(13) + NL, NL).split(NL), 1):
        if l.strip():
            salida.append((i, json.loads(l)))
    return salida


def ya_corregida(d):
    """LA GUARDA DE IDEMPOTENCIA. PURA: recibe la ficha ya parseada."""
    return any(MARCA in e for e in (d.get("verificacion") or []))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    ap.add_argument("--salida", default="T2_CORRECCION_OP_L_01")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2: LA CORRECCION DECLARADA DE LA verificacion DE"
      % VUELTA_QUE_ESCRIBE)
    w("OP-L-01, EN SU SEDE, POR ADICION Y POR EL CARRIL DEL BANCO 9.10")
    w("=" * 78)
    w("")

    w("A) EL INSTRUMENTO SE IMPORTA, NO SE CLONA, Y ANTES SE COMPRUEBA QUE NO")
    w("   ESCRIBE. SE COMPRUEBA DE VERDAD (caida C.2 del auditor de la 202).")
    di, lfi, shai, txti = dos_convenciones(INSTRUMENTO)
    w("   %s" % INSTRUMENTO)
    w("      disco %d bytes | LF %d bytes | sha256 LF %s" % (di, lfi, shai))
    lineas_i = txti.split(NL)
    w("      CIFRA lineas por count(NL): %d" % txti.count(NL))
    escrituras = [(i, l.strip()) for i, l in enumerate(lineas_i, 1)
                  if PATRON_ESCRITURA.search(l)]
    w("      CIFRA lineas con marca de ESCRITURA en disco: %d" % len(escrituras))
    for i, l in escrituras:
        w("         linea %4d | %s" % (i, l[:110]))
    w("      LO QUE SE LLAMA DE EL, Y NADA MAS: las_once(), mapa_de_alias(),")
    w("      veredictos(), medir_clausula_1() y su CABECERA_LD. Su main() NO se")
    w("      llama, que es donde vive lo que escribe con --aplicar.")
    _c, st_antes = git(["status", "--porcelain"])
    w("   CIFRA lineas de git status ANTES de importarlo y llamarlo: %d"
      % len([x for x in st_antes.split(NL) if x.strip()]))
    w("")

    w("B) EL RESOLUTOR DELANTE DE TODO CONTEO (P.1), Y LAS TRES LECTURAS DE HOY")
    mapa, n_nodos = I166.mapa_de_alias()
    once = I166.las_once()
    V = I166.veredictos()
    w("   CIFRA ficheros de nodo leidos: %d" % n_nodos)
    w("   CIFRA alias en el mapa del resolutor: %d" % len(mapa))
    w("   CIFRA cabeceras LD que las_once() devuelve HOY: %d" % len(once))
    w("   CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d" % len(V))
    n_lit, n_res, n_pl, n_pr, hallazgos = I166.medir_clausula_1(mapa, once, V)
    w("   CIFRA pares distintos, comparacion LITERAL: %d" % n_pl)
    w("   CIFRA pares distintos, comparacion RESUELTA: %d" % n_pr)
    w("   CIFRA de las LD que aparecen, LITERAL: %d" % n_lit)
    w("   CIFRA de las LD que aparecen, RESUELTA: %d" % n_res)
    puestos_hoy = sum(len(p) for _l, _a, _b, _c, p in hallazgos)
    w("   CIFRA puestos implicados en total: %d" % puestos_hoy)
    for ld, x, y, clase, puestos in hallazgos:
        w("      %-8s %s contra %s (lectura dirigida: %s), %d puesto(s)"
          % (ld, x, y, clase, len(puestos)))
    w("")

    w("C) EL UNIVERSO DE las_once() AL CORTE %s, LEIDO DE GIT Y NO TECLEADO"
      % CORTE_VIEJO)
    _c, rev = git(["rev-list", "-1", "--before=%s 23:59:59" % CORTE_VIEJO, "HEAD",
                   "--", LECTURAS_REL])
    rev = rev.strip()
    w("   comando: git rev-list -1 --before='%s 23:59:59' HEAD -- %s"
      % (CORTE_VIEJO, LECTURAS_REL))
    w("   commit que ese comando devuelve: %s" % (rev[:8] or "(ninguno)"))
    n_viejas = None
    if rev:
        _c, fecha = git(["log", "-1", "--format=%ad", "--date=short", rev])
        _c, asunto = git(["log", "-1", "--format=%s", rev])
        w("   su fecha: %s" % fecha.strip())
        w("   su asunto: %s" % asunto.strip()[:110])
        _c, viejo = git(["show", "%s:%s" % (rev, LECTURAS_REL)])
        n_viejas = len(I166.CABECERA_LD.findall(viejo))
        w("   CIFRA bytes de ese %s en aquel commit: %d"
          % (LECTURAS_REL, len(viejo.encode("utf-8"))))
        w("   CIFRA cabeceras LD ahi, contadas CON LA MISMA CABECERA_LD: %d"
          % n_viejas)
    else:
        w("   ROJO SUAVE: git no devuelve commit para ese corte, asi que LA")
        w("   CIFRA VIEJA NO SE PUBLICA COMO MEDICION. Se dice que no se pudo")
        w("   medir en vez de teclear un once.")
    dl, lfl, shal, _t = dos_convenciones(LECTURAS_REL)
    w("   %s HOY: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (LECTURAS_REL, dl, lfl, shal))
    w("")

    w("D) LO QUE LA FICHA TIENE CONGELADO, LEIDO DE ELLA Y NO DE UN ACTA")
    todas = fichas()
    w("   CIFRA lineas NO VACIAS de docs/plan/OPERACIONES.jsonl: %d" % len(todas))
    sitio = [(i, d) for i, d in todas if d.get("id_op") == ID_OP]
    w("   CIFRA lineas donde vive %s: %d | linea(s): %s"
      % (ID_OP, len(sitio), ", ".join(str(i) for i, _d in sitio)))
    if len(sitio) != 1:
        w("   ROJO: la ficha no vive en exactamente 1 linea. NO SE ESCRIBE.")
        print(NL.join(L))
        return 1
    n_linea, ficha_d = sitio[0]
    w("   LA COORDENADA ES LINEA MAS INDICE (acta 201, 4.4). La ficha esta en la")
    w("   LINEA %d, y el encargo dice %d: CALZA %s"
      % (n_linea, LINEA_ESPERADA, "SI" if n_linea == LINEA_ESPERADA else "NO"))
    estado_antes = ficha_d.get("estado")
    ver_antes = list(ficha_d.get("verificacion") or [])
    w("   estado=%r  tipo=%r  fase=%r  fecha_corte=%r"
      % (estado_antes, ficha_d.get("tipo"), ficha_d.get("fase"),
         ficha_d.get("fecha_corte")))
    w("   CIFRA claves de la ficha: %d" % len(ficha_d))
    w("   CIFRA elementos de `verificacion` ANTES: %d" % len(ver_antes))
    for k, e in enumerate(ver_antes):
        w("      verificacion indice %d (elemento %d), %d caracteres: %s"
          % (k, k + 1, len(e), repr(e)[:120]))
    congelado = ver_antes[3] if len(ver_antes) > 3 else ""
    def leer_congelada(pat, etiqueta):
        m = re.search(pat, congelado)
        v = m.group(1) if m else None
        w("   CONGELADO en el elemento 4, %-32s %s"
          % (etiqueta, v if v is not None else "(no legible)"))
        return v
    c_lit = leer_congelada(r"EN COMPARACION LITERAL[^.]*?(\d+) de las once", "literal:")
    c_res = leer_congelada(r"EN COMPARACION RESUELTA APARECEN (\d+)", "resuelta:")
    c_pl = leer_congelada(r"(\d+) pares literales distintos", "pares literales:")
    c_pr = leer_congelada(r"(\d+) pares RESUELTOS distintos", "pares resueltos:")
    c_alias = leer_congelada(r"mapa de (\d+) alias", "alias:")
    c_filas = leer_congelada(r"(\d+) filas en docs/INTRA_DOMINIO", "filas:")
    c_puestos = sum(int(x) for x in re.findall(r"cae sobre (\d+) puesto", congelado))
    w("   CONGELADO en el elemento 4, %-32s %d"
      % ("puestos implicados:", c_puestos))
    adj = ficha_d.get("adjudicacion") or ""
    m_once = re.search(r"TANDA DE (\w+) LECTURAS DIRIGIDAS", adj)
    w("   LA PALABRA `once` NO SALE DEL NOMBRE DE LA FUNCION: sale del campo")
    w("   `adjudicacion` de esta misma ficha, que dice %r"
      % (m_once.group(0) if m_once else "(no legible)"))
    w("")

    w("E) EL COTEJO, CIFRA A CIFRA, CON SUS DOS CORTES")
    filas_cotejo = [
        ("cabeceras LD que las_once() devuelve",
         (str(n_viejas) if n_viejas is not None else "(no medible)"),
         str(len(once))),
        ("filas de INTRA_DOMINIO_VEREDICTOS.jsonl", c_filas, str(len(V))),
        ("alias del resolutor", c_alias, str(len(mapa))),
        ("pares distintos, LITERAL", c_pl, str(n_pl)),
        ("pares distintos, RESUELTOS", c_pr, str(n_pr)),
        ("de las LD que aparecen, LITERAL", c_lit, str(n_lit)),
        ("de las LD que aparecen, RESUELTA", c_res, str(n_res)),
        ("puestos implicados", str(c_puestos), str(puestos_hoy)),
    ]
    discrepan = 0
    for etiqueta, viejo, nuevo in filas_cotejo:
        calza = (viejo == nuevo)
        if not calza:
            discrepan += 1
        w("   %-42s corte %s: %-8s | corte %s: %-8s  %s"
          % (etiqueta, CORTE_VIEJO, viejo if viejo is not None else "(no legible)",
             CORTE, nuevo, "CALZA" if calza else "DISCREPA"))
    w("   CIFRA cifras cotejadas: %d | CIFRA que DISCREPAN: %d"
      % (len(filas_cotejo), discrepan))
    w("")
    w("   LA LINEA QUE NO PUEDE FALTAR, Y VA AQUI Y NO AL FINAL: EN COMPARACION")
    w("   LITERAL SIGUEN APARECIENDO %d. La clausula 1 pregunta si alguna de las"
      % n_lit)
    w("   lecturas dirigidas VIVE en el archivo de veredictos, y en literal la")
    w("   respuesta sigue siendo NINGUNA. LA CLAUSULA 1 NO SE CAE: lo que")
    w("   envejecio es LA CIFRA DE LA EXCEPCION, no la clausula.")
    w("")

    if n_lit != 0:
        w("   ROJO: la comparacion literal NO da 0, y entonces esta correccion no")
        w("   se puede escribir como esta redactada. NO SE ESCRIBE NADA.")
        print(NL.join(L))
        return 1

    # ------------------------------------------------------------------ EL TEXTO
    detalle = []
    for ld, x, y, clase, puestos in hallazgos:
        detalle.append("%s (%s contra %s, cuya lectura dirigida es %s) cae sobre "
                       "%d puesto(s): %s"
                       % (ld, x, y, clase, len(puestos),
                          ", ".join("el puesto %s en %s (%s contra %s, dominio %s)"
                                    % (p, c, xx, yy, dom)
                                    for p, c, xx, yy, dom in puestos)))
    nuevo_elemento = (
        "%s, POR ADICION, CON EL TEXTO VIEJO ENTERO ARRIBA, SIN TACHARLO Y SIN "
        "CLAVE NUEVA DE ESQUEMA (es un elemento mas de esta misma lista "
        "verificacion, la via que esta ficha ya uso en las vueltas 166 y 169 y "
        "que el acta 71, seccion 6, adjudicacion 3, adjudico CON LAS PALABRAS NO "
        "ES PARADA). ADJUDICADA POR EL ACTA 202 EN SU 4.4: el ejecutor de la 202 "
        "midio la discrepancia y pregunto en su P.2 en vez de escribirla por su "
        "cuenta, y ahora esta adjudicada. "
        "LO QUE SE CORRIGE NO ES UNA CLAUSULA: ES LA CIFRA DE LA EXCEPCION que el "
        "elemento 4 de esta misma lista dejo congelada el %s. "
        "LO PRIMERO Y ANTES QUE NADA, PORQUE SIN ESTA LINEA LA CORRECCION SE "
        "LEERIA AL REVES: EN COMPARACION LITERAL SIGUEN APARECIENDO %d, o sea que "
        "LA CLAUSULA 1 NO SE CAE. Lo que la clausula pregunta es si alguna de las "
        "lecturas dirigidas vive en INTRA_DOMINIO_VEREDICTOS.jsonl, y medido hoy "
        "con el resolutor puesto (P.1) la respuesta sigue siendo NINGUNA. "
        "LO QUE ENVEJECIO ES EL UNIVERSO QUE PRODUCE LA CIFRA, Y ESTO ES LO "
        "PRIMERO QUE HAY QUE SABER PARA LEER EL RESTO: la funcion que el "
        "instrumento llama las_once() NO DEVUELVE ONCE. Devuelve toda cabecera LD "
        "que haya HOY en docs/plan/LECTURAS_DIRIGIDAS.md, con la expresion regular "
        "CABECERA_LD. La palabra `once` no sale de la funcion: sale del campo "
        "adjudicacion de esta misma ficha, que dice 'TANDA DE ONCE LECTURAS "
        "DIRIGIDAS'. MEDIDO EN LA VUELTA 203 Y NO TECLEADO: al corte %s ese "
        "documento traia %s cabeceras LD, contadas sobre el fichero tal como "
        "estaba en el commit %s con `git show` y con LA MISMA CABECERA_LD; y al "
        "corte %s trae %d. "
        "LA COMPARACION RESUELTA, CON SUS DOS CORTES: la ficha tiene congelado "
        "que en comparacion RESUELTA aparecen %s con %d puestos implicados, corte "
        "%s; medido hoy aparecen %d con %d puestos implicados, corte %s. Los pares "
        "distintos pasan de %s a %d en literal y de %s a %d en resuelto, sobre %s "
        "filas del archivo al corte viejo y %d hoy, con un mapa de %s alias al "
        "corte viejo y %d hoy. "
        "LAS QUE HOY CAEN, UNA POR UNA Y CON SU PUESTO, SU CLASE Y SUS IDS "
        "CRUDOS: %s. "
        "LA CIFRA VIEJA NO ES UNA MENTIRA Y NO SE RETIRA: viajaba con su corte "
        "%s y con ese corte era cierta. Lo que cambio no es la medicion sino el "
        "universo medido, y por eso esta correccion NO borra ni tacha el elemento "
        "4, que sigue entero arriba con su corte al lado. "
        "LO QUE ESTA CORRECCION NO HACE: no cierra esta ficha (el acta 202 dice "
        "en su 4.4 que OP-L-01 NO SE CIERRA), no toca su estado, que entra y sale "
        "en %s, no mueve ni un veredicto, no adjudica clase a ningun puesto, no "
        "toca ni un nodo y no autoriza ninguna lectura nueva. "
        "Ver docs/loop/SALIDA_V%d_%s.txt."
        % (MARCA, CORTE_VIEJO, n_lit, CORTE_VIEJO,
           (n_viejas if n_viejas is not None else "(no medible)"),
           (rev[:8] if rev else "(ninguno)"), CORTE, len(once),
           c_res, c_puestos, CORTE_VIEJO, n_res, puestos_hoy, CORTE,
           c_pl, n_pl, c_pr, n_pr, c_filas, len(V), c_alias, len(mapa),
           "; ".join(detalle) or "(ninguna)",
           CORTE_VIEJO, estado_antes, VUELTA_QUE_ESCRIBE,
           # LA RUTA CITADA ES LA CANONICA Y NO `a.salida`, Y SE DICE POR QUE:
           # si el texto del elemento llevara dentro el nombre de la salida de
           # cada corrida, la SEGUNDA corrida compondria un texto distinto por
           # cinco caracteres y la idempotencia se leeria como inestabilidad.
           # Cazado en la primera corrida de prueba de esta vuelta.
           "T2_CORRECCION_OP_L_01"))

    w("F) EL ELEMENTO NUEVO, COMPUESTO Y MEDIDO ANTES DE ESCRIBIRSE")
    w("   CIFRA caracteres del elemento nuevo: %d" % len(nuevo_elemento))
    w("   CIFRA bytes utf-8 del elemento nuevo: %d"
      % len(nuevo_elemento.encode("utf-8")))
    ya = ya_corregida(ficha_d)
    w("   la correccion de esta vuelta YA esta en la ficha: %s"
      % ("SI" if ya else "NO"))
    w("")

    d0, lf0, sha0, texto0 = dos_convenciones("docs/plan/OPERACIONES.jsonl")
    w("G) LA SEDE AL ENTRAR, POR LAS DOS CONVENCIONES")
    w("   docs/plan/OPERACIONES.jsonl: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (d0, lf0, sha0))
    estados_antes = {}
    for _i, d in todas:
        estados_antes[d.get("id_op")] = d.get("estado")
    w("   CIFRA fichas leidas para la guarda de estado: %d" % len(estados_antes))
    w("")

    if a.escribir and not ya:
        lineas = texto0.split(NL)
        d = json.loads(lineas[n_linea - 1])
        d["verificacion"] = list(d.get("verificacion") or []) + [nuevo_elemento]
        lineas[n_linea - 1] = json.dumps(d, ensure_ascii=False)
        io.open(OPS, "w", encoding="utf-8", newline=NL).write(NL.join(lineas))
        w("   ESCRITO: un elemento mas en `verificacion` de %s, linea %d."
          % (ID_OP, n_linea))
    elif a.escribir:
        w("   NO SE ESCRIBE: la correccion ya estaba. IDEMPOTENTE.")
    else:
        w("   MODO MEDICION: no se escribe nada.")
    w("")

    w("=" * 78)
    w("H) LA GUARDA, RELEIDA DEL DISCO Y CONTRA HEAD")
    w("=" * 78)
    d1, lf1, sha1, texto1 = dos_convenciones("docs/plan/OPERACIONES.jsonl")
    w("   docs/plan/OPERACIONES.jsonl al salir: disco %d bytes | LF %d bytes | "
      "sha256 LF %s" % (d1, lf1, sha1))
    w("   CIFRA crecimiento en bytes de disco: %d" % (d1 - d0))
    w("   CIFRA crecimiento en bytes LF: %d" % (lf1 - lf0))
    _c, num = git(["diff", "--numstat", "--", "docs/plan/OPERACIONES.jsonl"])
    filas_num = [x for x in num.split(NL) if x.strip()]
    w("   git diff --numstat -- docs/plan/OPERACIONES.jsonl: %d fila(s)"
      % len(filas_num))
    for x in filas_num:
        w("      %s" % x.strip())
    _c, head_txt = git(["show", "HEAD:docs/plan/OPERACIONES.jsonl"])
    viejas = [l for l in head_txt.replace(chr(13) + NL, NL).split(NL)]
    nuevas = texto1.split(NL)
    distintas = [i for i in range(max(len(viejas), len(nuevas)))
                 if (viejas[i] if i < len(viejas) else None)
                 != (nuevas[i] if i < len(nuevas) else None)]
    w("   CIFRA lineas DISTINTAS contra HEAD: %d | linea(s): %s"
      % (len(distintas), ", ".join(str(i + 1) for i in distintas) or "(ninguna)"))
    if len(distintas) == 1 and distintas[0] + 1 == n_linea:
        dv = json.loads(viejas[distintas[0]])
        dn = json.loads(nuevas[distintas[0]])
        claves_dist = sorted(k for k in set(dv) | set(dn) if dv.get(k) != dn.get(k))
        w("   CIFRA claves de esa ficha que CAMBIAN: %d | cuales: %s"
          % (len(claves_dist), ", ".join(claves_dist) or "(ninguna)"))
        vv = dv.get("verificacion") or []
        vn = dn.get("verificacion") or []
        w("   CIFRA elementos de `verificacion` ANTES: %d | DESPUES: %d"
          % (len(vv), len(vn)))
        iguales = sum(1 for k in range(min(len(vv), len(vn))) if vv[k] == vn[k])
        w("   CIFRA elementos viejos IDENTICOS Y EN SU ORDEN: %d de %d"
          % (iguales, len(vv)))
        w("   el `estado` entra %r y sale %r: %s"
          % (dv.get("estado"), dn.get("estado"),
             "IGUAL" if dv.get("estado") == dn.get("estado") else "CAMBIA, ROJO"))
    # LA GUARDA DE `estado` SE MIDE CONTRA HEAD Y NO CONTRA UNA COPIA EN
    # MEMORIA, que es lo unico que prueba que el fichero commiteado no se movio.
    en_head = {}
    for l in viejas:
        if l.strip():
            dd = json.loads(l)
            en_head[dd.get("id_op")] = dd.get("estado")
    ahora = {}
    for l in nuevas:
        if l.strip():
            dd = json.loads(l)
            ahora[dd.get("id_op")] = dd.get("estado")
    movidas = [k for k in en_head if en_head[k] != ahora.get(k)]
    faltan = [k for k in en_head if k not in ahora]
    sobran = [k for k in ahora if k not in en_head]
    w("   CIFRA fichas en HEAD: %d | CIFRA fichas en el disco al salir: %d"
      % (len(en_head), len(ahora)))
    w("   CIFRA fichas que aparecen o desaparecen: %d y %d"
      % (len(faltan), len(sobran)))
    w("   CIFRA de las %d fichas que MUEVEN su campo `estado` contra HEAD: %d"
      % (len(en_head), len(movidas)))
    w("   cuales: %s" % (", ".join(sorted(movidas)) or "(ninguna)"))
    w("   y la de esta tarea en concreto: %s entra %r en HEAD y sale %r en disco"
      % (ID_OP, en_head.get(ID_OP), ahora.get(ID_OP)))
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt"
                         % (VUELTA_QUE_ESCRIBE, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
