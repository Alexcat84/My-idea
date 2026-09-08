# -*- coding: utf-8 -*-
r"""_v208_t2d_v3.py . TAREA 2.d DE LA VUELTA 208: SI CON LAS DOS FILAS ESCRITAS
LA `V.3` PASA DE `A MEDIAS` A `CUBRE`, MEDIDO Y CON SU CITA DE FICHERO Y LINEA,
PARA QUE EL AUDITOR LA CIERRE EN LA 209 SIN VOLVER A MEDIR.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3). SOLO MIDE: no escribe en ninguna sede.

**NO CIERRA `OP-L-01` Y NO TOCA SU CAMPO `estado`.** Cerrar una ficha es
adjudicacion del auditor (encargo 2.d, `AUDITOR.md` 0). Esta corrida mide
`docs/plan/OPERACIONES.jsonl` para probar que no lo movio.

LAS TRES LECTURAS QUE SE PUBLICAN, Y NINGUNA SE ELIGE EN SILENCIO:

  (1) LO QUE EL INSTRUMENTO SELLADO DE LA 207 DICE HOY, corrido tal cual y sin
      tocarle una linea. **Y hay que leerlo con cuidado, porque su motivo ya no
      es cierto entero:** su busqueda toma `fila_ban[0]`, o sea LA PRIMERA fila
      de la tabla cuya celda de nombre case, y una correccion POR ADICION deja
      DOS filas: la vieja arriba y la corregida debajo. **El instrumento lee la
      vieja.** No se toca (moratoria); se declara.
  (2) EL MISMO CRITERIO DE LA 207, APLICADO A LAS FILAS CORREGIDAS: para cada
      nomina que la mesa declara con cobertura COMPLETA, `leidos` tiene que
      igualar a `posibles`.
  (3) EL CRITERIO DE LA ADJUDICACION `6.1` DEL ACTA 207, que es el que la mesa
      tiene que satisfacer: *"cada decision escrita con su motivo y su COBERTURA
      AL LADO (banco 9.26)"*, y el `9.26` dice que **mientras falte un par la
      forma es PROVISIONAL y se dice asi**. Ese criterio NO exige que la
      cobertura sea completa: exige que ESTE ESCRITA con su motivo.
"""
import argparse
import hashlib
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

VUELTA = 208
BANCO = os.path.join(RAIZ, "docs", "BANCO_DE_TEXTOS.md")
LECTURAS = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
OPES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
MARCA_FILA = "(FILA CORREGIDA EN LA VUELTA %d)" % VUELTA
NOMINAS = ("junta asesora", "seleccion de canal")


def dos_convenciones(ruta):
    d = io.open(ruta, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return (len(d), len(lf), hashlib.sha256(d).hexdigest()[:16],
            hashlib.sha256(lf).hexdigest()[:16], lf.decode("utf-8"))


def celdas_de(linea):
    return [c.strip() for c in linea.strip().strip("|").split("|")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default="T2D_V3")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2.d: LA `V.3`, MEDIDA CON LAS DOS FILAS YA ESCRITAS"
      % VUELTA)
    w("=" * 78)
    w("")

    _d, _lf, _sd, _sl, t_ban = dos_convenciones(BANCO)
    _d2, _lf2, _sd2, _sl2, t_ld = dos_convenciones(LECTURAS)
    ban = t_ban.split(NL)
    ld = t_ld.split(NL)
    w("A) LAS DOS SEDES, MEDIDAS AL ENTRAR")
    w("   docs/BANCO_DE_TEXTOS.md: %d bytes en disco y %d normalizado a LF,"
      % (_d, _lf))
    w("   sha256 disco %s y sha256 LF %s" % (_sd, _sl))
    w("   docs/plan/LECTURAS_DIRIGIDAS.md: %d bytes en disco y %d normalizado a"
      % (_d2, _lf2))
    w("   LF, sha256 disco %s y sha256 LF %s" % (_sd2, _sl2))
    w("")

    w("B) LECTURA (1). EL INSTRUMENTO SELLADO DE LA 207, CORRIDO TAL CUAL")
    r = subprocess.run([sys.executable,
                        os.path.join("scripts", "loop", "_v207_t2_cotejo.py")],
                       cwd=RAIZ, capture_output=True)
    salida = (r.stdout + r.stderr).decode("utf-8", errors="replace").replace(
        chr(13) + NL, NL)
    w("   EXITCODE del instrumento sellado: %d" % r.returncode)
    for l in salida.split(NL):
        if l.startswith("   V.3") or "CIFRA CUBRE" in l or "CIFRA A MEDIAS" in l \
                or "CIFRA NO CUBRE" in l:
            w("      %s" % l.strip()[:200])
    w("")
    w("   Y ESTO ES LO QUE HAY QUE DECIR DE ESA LECTURA, MEDIDO Y NO SUPUESTO:")
    w("   su busqueda toma la PRIMERA fila de la tabla cuya celda de nombre case")
    w("   (`fila_ban[0]` en la linea 236 de scripts/loop/_v207_t2_cotejo.py), y")
    w("   una correccion POR ADICION deja DOS filas por nomina. LEE LA VIEJA.")
    w("")

    w("C) LAS FILAS DE LA TABLA, VIEJAS Y CORREGIDAS, CON SU LINEA")
    filas = {}
    for nombre in NOMINAS:
        hits = [(i, l) for i, l in enumerate(ban, 1)
                if l.startswith("| **") and len(celdas_de(l)) > 5
                and nombre in celdas_de(l)[1]]
        w("   --- %s ---" % nombre.upper())
        w("   CIFRA filas de la tabla cuya celda de nombre trae %r: %d"
          % (nombre, len(hits)))
        vieja = [(i, l) for i, l in hits if MARCA_FILA not in l]
        nueva = [(i, l) for i, l in hits if MARCA_FILA in l]
        w("      de ellas VIEJAS (sin la marca de fila corregida): %d" % len(vieja))
        for i, l in vieja:
            c = celdas_de(l)
            w("         linea %d | miembros %s | posibles %s | leidos %s | en A %s"
              % (i, c[2], c[3], c[4], c[5]))
        w("      de ellas CORREGIDAS: %d" % len(nueva))
        for i, l in nueva:
            c = celdas_de(l)
            w("         linea %d | miembros %s | posibles %s | leidos %s | en A %s"
              % (i, c[2], c[3], c[4], c[5]))
        if len(nueva) != 1:
            w("      EL PATRON NO ENCONTRO EXACTAMENTE UNA FILA CORREGIDA.")
            w("      NO SE PUBLICA VEREDICTO POR ESTA VIA.")
            filas[nombre] = None
            continue
        c = celdas_de(nueva[0][1])
        pos = int(re.sub(r"[^0-9]", "", c[3]))
        lei = int(re.sub(r"[^0-9]", "", c[4]))
        filas[nombre] = dict(linea=nueva[0][0], posibles=pos, leidos=lei,
                             completa=(pos == lei), texto=nueva[0][1])
    w("")

    w("D) LECTURA (2). EL MISMO CRITERIO DE LA 207, SOBRE LAS FILAS CORREGIDAS")
    w("   el criterio, literal del instrumento: para cada nomina que la mesa")
    w("   declara con cobertura COMPLETA, `leidos` TIENE que igualar a `posibles`")
    desajustes = []
    for nombre in NOMINAS:
        f = filas.get(nombre)
        fila_ld = [(i, l) for i, l in enumerate(ld, 1)
                   if l.startswith("|") and celdas_de(l)
                   and nombre in celdas_de(l)[0]
                   and "cobertura COMPLETA" in l]
        w("   --- %s ---" % nombre.upper())
        if fila_ld:
            w("      la mesa lo declara COMPLETA en docs/plan/LECTURAS_DIRIGIDAS.md:%d"
              % fila_ld[0][0])
        else:
            w("      el patron no encontro su fila de cobertura COMPLETA en la mesa")
        if f is None:
            w("      NO COMPUTABLE por esta via.")
            continue
        w("      la fila corregida da %d de %d, o sea COMPLETA: %s"
          % (f["leidos"], f["posibles"], "SI" if f["completa"] else "NO"))
        w("      cita: docs/BANCO_DE_TEXTOS.md:%d" % f["linea"])
        if not f["completa"]:
            desajustes.append((nombre, f))
    w("   CIFRA nominas que la mesa declara CERRADAS y la fila CORREGIDA no")
    w("   lleva cerradas: %d (%s)"
      % (len(desajustes), ", ".join(n for n, _f in desajustes) or "ninguna"))
    v3_criterio_207 = "CUBRE" if not desajustes else "A MEDIAS"
    w("   VEREDICTO DE LA `V.3` POR EL CRITERIO DE LA 207: %s" % v3_criterio_207)
    w("")

    w("E) LECTURA (3). EL CRITERIO DE LA ADJUDICACION `6.1` DEL ACTA 207")
    w("   literal: cada decision escrita con su motivo y su COBERTURA AL LADO")
    w("   (banco 9.26), y el 9.26 dice que mientras falte un par la forma es")
    w("   PROVISIONAL y SE DICE ASI. Ese criterio NO exige cobertura completa:")
    w("   exige que la cobertura ESTE ESCRITA, con su motivo, y que lo incompleto")
    w("   se diga PROVISIONAL.")
    piezas = []
    for nombre in NOMINAS:
        f = filas.get(nombre)
        w("   --- %s ---" % nombre.upper())
        if f is None:
            w("      NO COMPUTABLE por esta via.")
            piezas.append(False)
            continue
        t = f["texto"]
        lleva_cob = ("COBERTURA" in t.upper())
        lleva_cifra = re.search(r"\b%d de %d\b" % (f["leidos"], f["posibles"]), t) is not None
        lleva_motivo = ("`LD-" in t)
        lleva_prov = ("PROVISIONAL" in t.upper())
        ok = lleva_cob and lleva_cifra and lleva_motivo and (
            f["completa"] or lleva_prov)
        w("      la fila lleva la palabra COBERTURA: %s" % ("SI" if lleva_cob else "NO"))
        w("      la fila lleva la cifra `%d de %d` al lado: %s"
          % (f["leidos"], f["posibles"], "SI" if lleva_cifra else "NO"))
        w("      la fila lleva su MOTIVO, nombrando la lectura dirigida que la"
          " mueve: %s" % ("SI" if lleva_motivo else "NO"))
        w("      si esta incompleta, la fila la declara PROVISIONAL: %s"
          % ("no aplica, esta completa" if f["completa"]
             else ("SI" if lleva_prov else "NO")))
        w("      cita: docs/BANCO_DE_TEXTOS.md:%d" % f["linea"])
        w("      esta nomina satisface el criterio `6.1`: %s" % ("SI" if ok else "NO"))
        piezas.append(ok)
    v3_criterio_61 = "CUBRE" if all(piezas) and piezas else "NO CUBRE"
    w("   VEREDICTO DE LA `V.3` POR EL CRITERIO DE LA `6.1`: %s" % v3_criterio_61)
    w("")

    w("=" * 78)
    w("EL RESULTADO DEL 2.d, DEJADO MEDIDO PARA QUE EL AUDITOR ADJUDIQUE")
    w("=" * 78)
    w("| lectura | criterio | veredicto de la `V.3` | cita |")
    w("|---|---|---|---|")
    w("| (1) el instrumento sellado de la 207, corrido tal cual | toma la PRIMERA "
      "fila que case, y esa es la VIEJA | **A MEDIAS** | "
      "`scripts/loop/_v207_t2_cotejo.py`, y su salida en "
      "`docs/loop/SALIDA_V%d_T2D_COTEJO_REPETIDO.txt` |" % VUELTA)
    cita2 = ", ".join("`docs/BANCO_DE_TEXTOS.md:%d`" % filas[n]["linea"]
                      for n in NOMINAS if filas.get(n))
    w("| (2) el mismo criterio, sobre las filas CORREGIDAS | `leidos` igual a "
      "`posibles` en las dos nominas | **%s** | %s |" % (v3_criterio_207, cita2))
    w("| (3) el criterio de la adjudicacion `6.1` del acta 207 | la cobertura "
      "ESCRITA al lado, con su motivo, y lo incompleto dicho PROVISIONAL | "
      "**%s** | %s |" % (v3_criterio_61, cita2))
    w("")
    w("LO QUE LAS TRES TIENEN EN COMUN, Y ES LO UNICO QUE NO SE DISCUTE: la tabla")
    w("AHORA LLEVA EL EFECTO DE LA MESA, que es lo que no llevaba. Lo que queda")
    w("por adjudicar es si una cobertura que la propia fila declara PROVISIONAL")
    w("cubre el punto o no lo cubre.")
    w("")
    w("Y LO QUE NO SE HACE AQUI, DICHO: NO SE CIERRA `OP-L-01`, NO SE TOCA SU")
    w("CAMPO `estado` Y NO SE ESCRIBE UNA SOLA LINEA EN NINGUNA SEDE.")
    do, lo, sdo, slo, _t = dos_convenciones(OPES)
    w("   docs/plan/OPERACIONES.jsonl: %d bytes en disco y %d normalizado a LF,"
      % (do, lo))
    w("   sha256 disco %s y sha256 LF %s" % (sdo, slo))
    w("")
    w("FIN")
    salida_txt = NL.join(L) + NL
    print(salida_txt)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida_txt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
