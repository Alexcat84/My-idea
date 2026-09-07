# -*- coding: utf-8 -*-
r"""_v203_t3_op_i_01.py . TAREA 3 DE LA VUELTA 203: `OP-I-01` CONTRA EL CRITERIO
DE HECHO, LA CUARTA FICHA REAL.

ES LA UNICA DE LAS CUATRO QUE LA VARA DEL PLAN DA COMO TRABAJO REAL Y QUE NADIE
HA MEDIDO CONTRA EL CRITERIO DE HECHO. La 201 le corrigio la `evidencia`; nadie
le ha mirado la `verificacion`.

EL CRITERIO SE CITA POR LINEA Y NO DE MEMORIA, y se aplica como el acta 202 lo
aplico en su `4.3`: **no basta con que las clausulas salgan cumplidas hoy**. Se
pregunta, clausula por clausula, **si SE CAERIA SI EL FALLO VOLVIERA**, y si
alguna solo pasa porque alguien la remide a mano, **se dice**: esa ficha no se
cierra.

LOS INSTRUMENTOS SE IMPORTAN Y SE CORREN TAL CUAL, COMPROBANDO ANTES QUE NO
ESCRIBEN. Y SE COMPRUEBA DE VERDAD, que es la caida `C.2` del auditor de la 202.
Aqui la comprobacion SALE POSITIVA: `vuelta169_tarea3_op_i_01.py` **SI escribe**,
y ademas escribe **sobre un fichero sellado y commiteado en la vuelta 169**. Por
eso se corre con el mismo protocolo que el sello de apertura de esta vuelta uso
con el instrumento de la racha: **se mide antes, se corre, se lee, se RESTAURA
con `git checkout --` y se REMIDE**.

PROPONE, NO CIERRA.

USO:
  python scripts/loop/_v203_t3_op_i_01.py
"""
import argparse
import collections
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
PY = sys.executable

sys.path.insert(0, AQUI)

OPS_REL = "docs/plan/OPERACIONES.jsonl"
CRITERIO_REL = "docs/plan/08_VERIFICACION.md"
INVENTARIO_REL = "docs/plan/INVENTARIO.jsonl"
INSTRUMENTO_REL = "scripts/loop/vuelta169_tarea3_op_i_01.py"
SELLADO_REL = "docs/loop/RECOMPUTO_V169.jsonl"
ID_OP = "OP-I-01"
LINEA_ESPERADA = 44
VUELTA = 203
CORTE = "2026-09-07"

PATRON_ESCRITURA = re.compile(
    r"open\s*\([^)]*[" + chr(34) + chr(39) + r"](w|wb|a|ab|w\+|r\+)["
    + chr(34) + chr(39) + r"]|\.write\s*\(|os\.remove|shutil\.|os\.rename"
    r"|os\.makedirs|json\.dump\s*\(|--salida")

L = []


def w(s=""):
    L.append(s)


def dos_convenciones(rel):
    ruta = os.path.join(RAIZ, rel)
    if not os.path.isfile(ruta):
        return None
    d = io.open(ruta, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return dict(disco=len(d), lf=len(lf),
                sha_lf=hashlib.sha256(lf).hexdigest()[:16],
                texto=lf.decode("utf-8", errors="replace"))


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default="T3_OP_I_01")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    w("=" * 78)
    w("VUELTA %d, TAREA 3: OP-I-01 CONTRA EL CRITERIO DE HECHO" % VUELTA)
    w("LA CUARTA FICHA REAL. SE PROPONE, NO SE CIERRA.")
    w("=" * 78)
    w("")

    # ---------------------------------------------------------------- A
    w("A) EL CRITERIO DE HECHO, CITADO POR LINEA Y NO DE MEMORIA")
    mc = dos_convenciones(CRITERIO_REL)
    lc = mc["texto"].split(NL)
    w("   %s: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (CRITERIO_REL, mc["disco"], mc["lf"], mc["sha_lf"]))
    w("   CIFRA lineas por split(NL): %d" % len(lc))
    cab = [i for i, l in enumerate(lc, 1) if "EL CRITERIO DE HECHO" in l]
    w("   CIFRA lineas con la cabecera 'EL CRITERIO DE HECHO': %d | linea(s): %s"
      % (len(cab), ", ".join(str(x) for x in cab) or "(ninguna)"))
    for i in cab:
        w("      linea %4d | %s" % (i, lc[i - 1].strip()))
    lit = [i for i, l in enumerate(lc, 1) if "SE CAERIA SI EL FALLO VOLVIERA" in l]
    w("   CIFRA lineas con el literal 'SE CAERIA SI EL FALLO VOLVIERA': %d | "
      "linea(s): %s" % (len(lit), ", ".join(str(x) for x in lit) or "(ninguna)"))
    for i in lit:
        w("      linea %4d | %s" % (i, lc[i - 1].strip()))
    barata = [i for i, l in enumerate(lc, 1) if "comprobacion barata" in l]
    w("   CIFRA lineas con 'comprobacion barata': %d | linea(s): %s"
      % (len(barata), ", ".join(str(x) for x in barata) or "(ninguna)"))
    for i in barata:
        for j in range(i, min(i + 3, len(lc)) + 1):
            w("      linea %4d | %s" % (j, lc[j - 1].strip()))
    nombrada = [i for i, l in enumerate(lc, 1) if ID_OP in l]
    w("   CIFRA lineas de ese documento que nombran %s: %d" % (ID_OP, len(nombrada)))
    w("   ESO SE DICE Y NO SE CALLA: el criterio que se le aplica a esta ficha es")
    w("   EL GENERAL, porque el documento NO la nombra ni una vez.")
    disp = [i for i, l in enumerate(lc, 1)
            if l.startswith("## EL DISPARADOR DEL RECOMPUTO")]
    w("   CIFRA cabeceras 'EL DISPARADOR DEL RECOMPUTO': %d | linea(s): %s"
      % (len(disp), ", ".join(str(x) for x in disp) or "(ninguna)"))
    paso4 = [i for i, l in enumerate(lc, 1)
             if l.startswith("| **4** |") or "LAS NOMINAS Y LOS ACTOS" in l]
    w("   CIFRA lineas del PASO 4 del disparador: %d | linea(s): %s"
      % (len(paso4), ", ".join(str(x) for x in paso4) or "(ninguna)"))
    for i in paso4:
        w("      linea %4d | %s" % (i, lc[i - 1].strip()[:150]))
    w("")

    # ---------------------------------------------------------------- B
    w("B) LA FICHA, CITADA POR LINEA MAS INDICE, Y LA LINEA SE COMPRUEBA")
    mo = dos_convenciones(OPS_REL)
    filas = [(i, l) for i, l in enumerate(mo["texto"].split(NL), 1) if l.strip()]
    w("   %s: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (OPS_REL, mo["disco"], mo["lf"], mo["sha_lf"]))
    w("   CIFRA lineas NO VACIAS: %d" % len(filas))
    sitio = [(i, json.loads(l)) for i, l in filas
             if json.loads(l).get("id_op") == ID_OP]
    w("   CIFRA lineas donde vive %s: %d | linea(s): %s"
      % (ID_OP, len(sitio), ", ".join(str(i) for i, _d in sitio)))
    if len(sitio) != 1:
        w("   ROJO: la ficha no vive en exactamente 1 linea. SE PARA.")
        return 1
    n_linea, ficha = sitio[0]
    w("   EL ENCARGO DICE LINEA %d. COMPROBADO, NO SUPUESTO: la ficha vive en la"
      % LINEA_ESPERADA)
    w("   LINEA %d. CALZA: %s"
      % (n_linea, "SI" if n_linea == LINEA_ESPERADA else "NO, y se declara"))
    w("   estado=%r  tipo=%r  fase=%r  fecha_corte=%r"
      % (ficha.get("estado"), ficha.get("tipo"), ficha.get("fase"),
         ficha.get("fecha_corte")))
    ver = list(ficha.get("verificacion") or [])
    evi = list(ficha.get("evidencia") or [])
    w("   CIFRA elementos de `evidencia`: %d" % len(evi))
    w("   CIFRA elementos de `verificacion`: %d" % len(ver))
    for k, e in enumerate(ver):
        w("      verificacion indice %d (elemento %d), %d caracteres:" % (k, k + 1, len(e)))
        w("         %s" % (e[:300] + (" [...]" if len(e) > 300 else "")))
    correcciones = [k for k, e in enumerate(ver)
                    if e.startswith("CORRECCION DECLARADA")]
    clausulas = [k for k in range(len(ver)) if k not in correcciones]
    w("   CIFRA elementos que son CORRECCION DECLARADA y NO clausula que cumplir:"
      " %d | indice(s): %s"
      % (len(correcciones), ", ".join(str(x) for x in correcciones) or "(ninguno)"))
    w("   CIFRA CLAUSULAS QUE HAY QUE CUMPLIR: %d | indice(s): %s"
      % (len(clausulas), ", ".join(str(x) for x in clausulas)))
    w("   Y LO MISMO EN LA EVIDENCIA, PARA NO CONFUNDIR LAS DOS LISTAS:")
    corr_evi = [k for k, e in enumerate(evi) if e.startswith("CORRECCION DECLARADA")]
    w("   CIFRA elementos de `evidencia` que son CORRECCION DECLARADA: %d "
      "| indice(s): %s"
      % (len(corr_evi), ", ".join(str(x) for x in corr_evi) or "(ninguno)"))
    w("")

    # ---------------------------------------------------------------- C
    w("C) EL SUJETO DE LAS CLAUSULAS: docs/plan/INVENTARIO.jsonl, MEDIDO HOY")
    mi = dos_convenciones(INVENTARIO_REL)
    inv = []
    no_json = 0
    for l in mi["texto"].split(NL):
        if not l.strip():
            continue
        try:
            inv.append(json.loads(l))
        except Exception:
            no_json += 1
    w("   %s: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (INVENTARIO_REL, mi["disco"], mi["lf"], mi["sha_lf"]))
    w("   CIFRA filas no vacias: %d | CIFRA lineas que NO son JSON valido: %d"
      % (len(inv), no_json))
    tipos = collections.Counter(r.get("tipo") for r in inv)
    for t, n in sorted(tipos.items()):
        w("      tipo %-16s %d" % (t, n))
    w("   LO QUE LA `evidencia` PROMETE, LEIDO DE LA PROPIA FICHA:")
    for k, e in enumerate(evi):
        m = re.search(r"INVENTARIO\.jsonl,\s*(\d+)\s+entradas", e)
        if m:
            w("      evidencia indice %d (elemento %d) nombra %s entradas | "
              "medidas hoy: %d | %s"
              % (k, k + 1, m.group(1), len(inv),
                 "CALZA" if int(m.group(1)) == len(inv) else "DISCREPA"))
    w("   Y ESA DISCREPANCIA NO ES UN HALLAZGO NUEVO: EL ACTA 201 YA LA CORRIGIO")
    w("   EN SU TAREA 2, y su correccion vive en el elemento 4 de la `evidencia`.")
    m201 = re.search(r"tiene (\d+) entradas \(lineas no vacias\), (\d+) lineas "
                     r"que no sean JSON valido, (\d+) bytes en disco y (\d+) "
                     r"normalizados a LF", evi[3] if len(evi) > 3 else "")
    if m201:
        w("   LO QUE ESA CORRECCION PUBLICA, LEIDO DE ELLA: %s entradas, %s lineas"
          % (m201.group(1), m201.group(2)))
        w("   no JSON, %s bytes en disco y %s normalizados a LF."
          % (m201.group(3), m201.group(4)))
        calza = (int(m201.group(1)) == len(inv) and int(m201.group(2)) == no_json
                 and int(m201.group(3)) == mi["disco"]
                 and int(m201.group(4)) == mi["lf"])
        w("   REPRODUCIDO HOY POR MI, CON OTRO INSTRUMENTO: %d entradas, %d no"
          % (len(inv), no_json))
        w("   JSON, %d bytes en disco y %d normalizados a LF. CALZA AL DIGITO: %s"
          % (mi["disco"], mi["lf"], "SI" if calza else "NO, y se declara"))
    w("")

    # ---------------------------------------------------------------- D
    w("D) LAS CLAUSULAS, UNA POR UNA, MEDIDAS Y DESPUES PASADAS POR EL CRITERIO")
    w("   DE HECHO. EL VEREDICTO DE CADA UNA SALE DE UNA EXPRESION COMPUTADA")
    w("   SOBRE EL FICHERO, NUNCA DE UN LITERAL.")
    w("")
    veredictos = []

    # CLAUSULA 1
    w("   D.1 CLAUSULA 1 (indice 0): %r" % ver[0])
    sin_corte = [r for r in inv if not (r.get("fecha_corte") or "").strip()]
    con_corte = len(inv) - len(sin_corte)
    w("       CIFRA entradas CON `fecha_corte` no vacia: %d de %d"
      % (con_corte, len(inv)))
    w("       CIFRA entradas SIN `fecha_corte`: %d" % len(sin_corte))
    for r in sin_corte[:10]:
        w("          %s | %s" % (r.get("tipo"), r.get("nombre")))
    cortes = collections.Counter(r.get("fecha_corte") for r in inv)
    w("       CIFRA cortes distintos: %d" % len(cortes))
    for c, n in sorted(cortes.items()):
        w("          %-12s %d" % (c, n))
    v1 = (len(sin_corte) == 0)
    w("       VEREDICTO CLAUSULA 1: %s" % ("CUMPLIDA" if v1 else "NO CUMPLIDA"))
    w("       EL CRITERIO DE HECHO: SE CAERIA SI EL FALLO VOLVIERA? SI. El")
    w("       veredicto es `len(sin_corte) == 0` sobre el fichero entero: basta")
    w("       UNA entrada sin `fecha_corte` para que caiga, y la lista de las")
    w("       que faltasen se imprimiria con su nombre. NO se remide a mano.")
    veredictos.append(("clausula 1", ver[0], v1, "SI"))
    w("")

    # CLAUSULA 2
    w("   D.2 CLAUSULA 2 (indice 1): %r" % ver[1])
    w("       LA CLAUSULA TIENE DOS MITADES Y SE MIDEN LAS DOS: que se sepa QUE")
    w("       FORMA tiene cobertura incompleta, y que ESA vaya marcada PROVISIONAL.")
    marca_prov = [r for r in inv if "PROVISIONAL" in (r.get("forma") or "")]
    w("       CIFRA entradas cuya `forma` trae el literal PROVISIONAL: %d"
      % len(marca_prov))
    for r in marca_prov:
        w("          %s | %s | forma: %s" % (r.get("tipo"), r.get("nombre"),
                                             (r.get("forma") or "")[:80]))
    w("       Y AHORA LA MITAD QUE NO SE PUEDE MEDIR SIN DECIDIR, Y SE DICE:")
    w("       la clave `cobertura` de este fichero es TEXTO LIBRE, no un campo")
    w("       con valores cerrados. Medido hoy:")
    w("       CIFRA entradas con `cobertura` vacia: %d"
      % sum(1 for r in inv if not (r.get("cobertura") or "").strip()))
    marcas_incompleta = ("incompleta", "INCOMPLETA", "parcial", "PARCIAL",
                         "sin cerrar", "pendiente", "falta")
    hits = {}
    for m in marcas_incompleta:
        hits[m] = sum(1 for r in inv if m in (r.get("cobertura") or ""))
    w("       LA BUSQUEDA POSITIVA, porque una busqueda negativa no se puede")
    w("       citar (EJECUTOR.md 9). Variantes buscadas en `cobertura` y su cuenta:")
    for m in marcas_incompleta:
        w("          %-14s %d aparicion(es)" % (m, hits[m]))
    total_marcadas = sum(hits.values())
    v2 = (total_marcadas == 0 or len(marca_prov) > 0)
    w("       VEREDICTO CLAUSULA 2, TAL COMO SE PUEDE MEDIR HOY: %s"
      % ("SIN CONTRAEJEMPLO" if v2 else "CON CONTRAEJEMPLO"))
    w("       EL CRITERIO DE HECHO: SE CAERIA SI EL FALLO VOLVIERA? NO, Y ESTO ES")
    w("       LO QUE ESTA TAREA TRAE. Para que esta clausula se cayera haria falta")
    w("       saber, POR UNA VARA ESCRITA, que entradas tienen cobertura")
    w("       INCOMPLETA; y `cobertura` es texto libre. Un dia que alguien deje de")
    w("       marcar PROVISIONAL una forma incompleta, ESTA COMPROBACION SEGUIRIA")
    w("       DANDO LO MISMO, porque no hay campo que la delate. Lo que hoy la")
    w("       sostiene es que ALGUIEN LA MIRA, no una expresion que caiga.")
    veredictos.append(("clausula 2", ver[1], v2, "NO"))
    w("")

    # CLAUSULA 3
    w("   D.3 CLAUSULA 3 (indice 2): %r" % ver[2])
    marcas_hueco = ("NO MEDIBLE", "no medible", "sin componente", "HUECO",
                    "hueco", "no se rellena", "NOMBRADO")
    hh = {}
    for m in marcas_hueco:
        hh[m] = sum(1 for r in inv
                    if m in ((r.get("nota") or "") + " " + (r.get("cobertura") or "")))
    w("       LA BUSQUEDA POSITIVA sobre `nota` mas `cobertura`:")
    for m in marcas_hueco:
        w("          %-16s %d fila(s)" % (m, hh[m]))
    vacios = [r for r in inv
              if not (r.get("nota") or "").strip()
              and not (r.get("cobertura") or "").strip()]
    w("       CIFRA filas con `nota` Y `cobertura` las dos vacias: %d" % len(vacios))
    v3 = (len(vacios) == 0)
    w("       VEREDICTO CLAUSULA 3, TAL COMO SE PUEDE MEDIR HOY: %s"
      % ("SIN CONTRAEJEMPLO" if v3 else "CON CONTRAEJEMPLO"))
    w("       EL CRITERIO DE HECHO: SE CAERIA SI EL FALLO VOLVIERA? NO. Lo que")
    w("       esta comprobacion sabe medir es que ninguna fila esta MUDA del todo,")
    w("       y eso NO es lo que la clausula pide. `todo hueco va NOMBRADO, nunca")
    w("       rellenado` exige saber DONDE hay hueco, y para eso hace falta la")
    w("       misma vara escrita que le falta a la clausula 2. Un hueco RELLENADO")
    w("       en silencio no deja sintoma en ningun campo, que es exactamente la")
    w("       enfermedad que el banco 9 llama degradacion silenciosa.")
    veredictos.append(("clausula 3", ver[2], v3, "NO"))
    w("")

    # CLAUSULA 4
    w("   D.4 CLAUSULA 4 (indice 3): %r" % ver[3])
    w("       ESTA SI TIENE INSTRUMENTO, Y LO PRIMERO ES MIRAR SI ESCRIBE.")
    mins = dos_convenciones(INSTRUMENTO_REL)
    w("       %s: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (INSTRUMENTO_REL, mins["disco"], mins["lf"], mins["sha_lf"]))
    escrituras = [(i, l.strip()) for i, l in enumerate(mins["texto"].split(NL), 1)
                  if PATRON_ESCRITURA.search(l)]
    w("       CIFRA lineas con marca de ESCRITURA en disco: %d" % len(escrituras))
    for i, l in escrituras:
        w("          linea %4d | %s" % (i, l[:100]))
    w("       LA COMPROBACION SALE POSITIVA Y NO SE IGNORA: ESTE INSTRUMENTO SI")
    w("       ESCRIBE, y ademas escribe sobre %s, que esta SELLADO Y COMMITEADO"
      % SELLADO_REL)
    _c, cm = git(["log", "-1", "--format=%h %ad %s", "--date=short", "--",
                  SELLADO_REL])
    w("       en la vuelta 169: %s" % cm.strip()[:110])
    w("       POR ESO SE CORRE CON EL PROTOCOLO DEL SELLO: se mide antes, se")
    w("       corre, se lee, se RESTAURA con git checkout -- y se REMIDE.")
    antes = dos_convenciones(SELLADO_REL)
    w("       SELLADO ANTES: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (antes["disco"], antes["lf"], antes["sha_lf"]))
    _c, st_antes = git(["status", "--porcelain"])
    n_st_antes = len([x for x in st_antes.split(NL) if x.strip()])
    w("       CIFRA lineas de git status ANTES de correrlo: %d" % n_st_antes)
    r = subprocess.run([PY, INSTRUMENTO_REL], cwd=RAIZ, capture_output=True)
    sal = (r.stdout.decode("utf-8", "replace")
           + r.stderr.decode("utf-8", "replace")).replace(chr(13) + NL, NL)
    io.open(os.path.join(LOOP, "SALIDA_V%d_T3_INSTRUMENTO_169.txt" % VUELTA),
            "w", encoding="utf-8", newline=NL).write(sal + NL + "EXITCODE: %d" % r.returncode + NL)
    w("       exitcode del instrumento: %d" % r.returncode)
    w("       su salida cruda queda sellada aparte en")
    w("       docs/loop/SALIDA_V%d_T3_INSTRUMENTO_169.txt" % VUELTA)
    # LAS ETIQUETAS NO SE ADIVINAN: SE LEYERON DE LA SALIDA DEL PROPIO
    # INSTRUMENTO. Mi primera tanda de patrones sacaba `(no legible)` en tres de
    # cuatro porque yo habia tecleado las etiquetas de memoria; cazado antes de
    # publicar nada y arreglado leyendo el fichero.
    for pat, et in (
            (r"CIFRA entradas del inventario:\s*(\d+)", "entradas inventario"),
            (r"CIFRA DENTRO del disparador \(acto mas racimo\):\s*(\d+)",
             "dentro disparador"),
            (r"CIFRA FUERA del disparador:\s*(\d+)", "fuera disparador"),
            (r"CIFRA entradas VIGENTES \(sin marca SUPERADA\):\s*(\d+)",
             "vigentes"),
            (r"CIFRA entradas marcadas SUPERADA[^:]*:\s*(\d+)", "superadas"),
            (r"CIFRA lineas del fichero:\s*(\d+)", "componentes sellado"),
            (r"CIFRA lineas de la corrida de HOY:\s*(\d+)", "componentes hoy"),
            (r"CIFRA entradas vigentes re medidas:\s*(\d+)", "re medidas"),
            (r"CIFRA cuyas CIFRAS de cobertura calzan[^:]*:\s*(\d+)", "calzan"),
            (r"CIFRA cuyas CIFRAS de cobertura DIFIEREN[^:]*:\s*(\d+)",
             "difieren"),
            (r"CIFRA sin componente en el fichero sellado:\s*(\d+)",
             "sin componente"),
            (r"exit de scripts/plan/recomputo_3388\.py:\s*(\d+)",
             "exit recomputo")):
        mm = re.search(pat, sal)
        w("       %-22s %s" % (et, mm.group(1) if mm else "(no legible)"))
    mm = re.search(r"la corrida de hoy REPRODUCE el fichero sellado en linea y "
                   r"estado:\s*(\w+)", sal)
    w("       %-22s %s" % ("reproduce el sellado", mm.group(1) if mm else "(no legible)"))
    w("       LA DISCREPANCIA QUE EL PROPIO INSTRUMENTO DECLARA, PEGADA ENTERA:")
    for i, l in enumerate(sal.split(NL)):
        if "DISCREPANCIA DECLARADA" in l:
            for j in range(i, min(i + 3, len(sal.split(NL)))):
                w("          %s" % sal.split(NL)[j].strip()[:150])
    despues = dos_convenciones(SELLADO_REL)
    w("       SELLADO TRAS CORRER: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (despues["disco"], despues["lf"], despues["sha_lf"]))
    w("       LO PISO: %s"
      % ("SI, y por eso se restaura" if despues["sha_lf"] != antes["sha_lf"]
         else "NO, la corrida lo deja identico"))
    git(["checkout", "--", SELLADO_REL])
    rest = dos_convenciones(SELLADO_REL)
    w("       SELLADO RESTAURADO: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (rest["disco"], rest["lf"], rest["sha_lf"]))
    w("       RESTAURADO IDENTICO AL DE ENTRADA: %s"
      % ("SI" if rest["sha_lf"] == antes["sha_lf"] else "NO, Y ESO ES ROJO"))
    _c, st_desp = git(["status", "--porcelain"])
    nuevas_st = [x.strip() for x in st_desp.split(NL) if x.strip()
                 and x.strip() not in [y.strip() for y in st_antes.split(NL)]]
    w("       CIFRA lineas de git status DESPUES de correr y restaurar: %d"
      % len([x for x in st_desp.split(NL) if x.strip()]))
    w("       CIFRA lineas de status NUEVAS respecto de antes: %d" % len(nuevas_st))
    for x in nuevas_st:
        w("          %s" % x)
    v4 = (r.returncode == 0)
    w("       VEREDICTO CLAUSULA 4, TAL COMO EL INSTRUMENTO LA DEJA: %s"
      % ("el instrumento corre en verde" if v4 else "el instrumento cae"))
    w("       EL CRITERIO DE HECHO: SE CAERIA SI EL FALLO VOLVIERA? EN PARTE, Y")
    w("       LA PARTE QUE NO SE DICE. El instrumento SI computa y SI cotejaria")
    w("       una discrepancia de componentes, pero su alcance esta acotado por la")
    w("       adjudicacion 6.4 del acta 168 a los tipos `acto` y `racimo`: los")
    w("       otros cuatro tipos del inventario quedan FUERA del disparador y el")
    w("       propio instrumento lo declara. O sea que la clausula dice `el")
    w("       inventario se recomputa ENTERO` y lo que se recomputa es una parte")
    w("       nombrada. La parte que se recomputa SI se caeria; el resto NO tiene")
    w("       quien lo tumbe.")
    veredictos.append(("clausula 4", ver[3], v4, "EN PARTE"))
    w("")

    # ---------------------------------------------------------------- E
    w("=" * 78)
    w("E) EL RESUMEN, Y NO ES UN CIERRE")
    w("=" * 78)
    w("| clausula | medida hoy | se caeria si el fallo volviera |")
    w("|---|---|---|")
    for nombre, texto, ok, cae in veredictos:
        w("| %s | %s | %s |" % (nombre, "SIN CONTRAEJEMPLO" if ok else "CON CONTRAEJEMPLO", cae))
    caen = sum(1 for _n, _t, _o, c in veredictos if c == "SI")
    w("   CIFRA clausulas medidas: %d" % len(veredictos))
    w("   CIFRA clausulas SIN CONTRAEJEMPLO hoy: %d"
      % sum(1 for _n, _t, o, _c in veredictos if o))
    w("   CIFRA clausulas que SE CAERIAN si el fallo volviera: %d" % caen)
    w("   CIFRA clausulas que NO se caerian: %d"
      % sum(1 for _n, _t, _o, c in veredictos if c == "NO"))
    w("   CIFRA clausulas que se caerian EN PARTE: %d"
      % sum(1 for _n, _t, _o, c in veredictos if c == "EN PARTE"))
    w("")
    w("   LO QUE SE PROPONE, Y LO ADJUDICA EL AUDITOR: OP-I-01 NO SE CIERRA. No")
    w("   porque una clausula salga en rojo hoy, que no sale, sino porque DOS de")
    w("   sus CUATRO no se caerian si el fallo volviera y UNA se caeria solo en")
    w("   parte, que es lo que el criterio de HECHO de la linea %s pregunta."
      % (", ".join(str(x) for x in lit) or "(no localizada)"))
    w("   EL ESTADO NO SE TOCA: entra %r y sale %r." % (ficha.get("estado"),
                                                        ficha.get("estado")))
    w("")

    # ---------------------------------------------------------------- F
    w("F) LA GUARDA DE QUE ESTA TAREA NO ESCRIBE EN EL PLAN")
    for rel in (OPS_REL, INVENTARIO_REL, CRITERIO_REL, SELLADO_REL):
        _c, num = git(["diff", "--numstat", "--", rel])
        f = [x for x in num.split(NL) if x.strip()]
        w("   git diff --numstat -- %-34s %d fila(s)" % (rel, len(f)))
        for x in f:
            w("      %s" % x.strip())
    m2 = dos_convenciones(OPS_REL)
    w("   %s al salir: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (OPS_REL, m2["disco"], m2["lf"], m2["sha_lf"]))
    w("   IDENTICO AL DE LA ENTRADA DE ESTA TAREA: %s"
      % ("SI" if m2["sha_lf"] == mo["sha_lf"] else "NO"))
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
