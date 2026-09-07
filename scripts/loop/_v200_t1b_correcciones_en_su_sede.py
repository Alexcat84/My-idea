# -*- coding: utf-8 -*-
r"""_v200_t1b_correcciones_en_su_sede.py . LAS TRES CORRECCIONES DE CIFRA DEL
ACTA 199, ESCRITAS EN SU SEDE Y SIN TAPAR LO QUE CORRIGEN.

PREFIJO DE GUION BAJO, por lo mismo que su hermano `_v200_t1_registrar_acta199`:
la moratoria de maquinaria (`AUDITOR.md` 6.3) prohibe fabricar arneses, guardas y
lectores nuevos, y la adjudicacion `4.5` del acta 199 declara que un computo de
una vuelta, con prefijo de guion bajo, fuera del censo y fuera de la nomina, y
que no vigila a nadie, NO ES MAQUINARIA.

LA SEDE ES `docs/loop/reportes/REPORTE_V199.md`, que es DONDE VIVEN LAS TRES
CIFRAS FALSAS. Al abrir esta vuelta ese texto todavia estaba en
`docs/loop/REPORTE.md`; el esqueleto de la 200 lo archivo byte a byte antes de
pisarlo, con los dos `sha256` cotejados, y a partir de ahi el archivo ES la sede.

COMO SE ESCRIBEN, Y ES EL CARRIL DEL BANCO `9.10` MAS `EJECUTOR.md` 8:
  . EL TEXTO VIEJO NO SE TOCA NI SE TACHA. Ni un caracter.
  . Detras del parrafo que trae la cifra falsa se INSERTA UN AVISO de una linea
    que dice que hay correccion y donde esta.
  . Al final del fichero se anade UN BLOQUE con las tres correcciones, cada una
    con la cifra vieja, la cifra de hoy, el instrumento que la remidio y su
    corte.
  . LA CIFRA DE LA `C.1` NO SE TECLEA: se pega la salida de
    `V.arneses_que_faltan()` corrida EN ESTA VUELTA.

IDEMPOTENTE: si la marca ya esta en la sede, no se escribe nada, y eso se prueba
re corriendolo con los bytes y el `sha256` medidos antes y despues.

USO:
  python scripts/loop/_v200_t1b_correcciones_en_su_sede.py
  python scripts/loop/_v200_t1b_correcciones_en_su_sede.py --escribir
"""
import argparse
import hashlib
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

sys.path.insert(0, AQUI)
import verificar_mutaciones_viejas as V   # noqa: E402

SEDE = os.path.join(LOOP, "reportes", "REPORTE_V199.md")
INVENTARIO = os.path.join(RAIZ, "docs", "plan", "10_INVENTARIO.md")
MARCA = "CORRECCIONES DECLARADAS, ESCRITAS EN LA VUELTA 200"
AVISO = ("> **CORRECCION DECLARADA (vuelta 200, TAREA 1): la cifra %s de este "
         "parrafo es falsa. El texto viejo se queda entero y sin tachar; la "
         "correccion va al final de este fichero, bajo `%s`.**")

# LOS TRES ANCLAJES SON LITERALES DEL PROPIO FICHERO, y la linea se BUSCA, no se
# teclea: un numero de linea tecleado caduca en cuanto alguien inserta algo
# encima, que es justo lo que este fichero va a hacer.
ANCLAJES = [
    ("C.1", "**1 arnes del censo queda fuera de la nomina con la vara 148**, y es"),
    ("C.1 (seccion 9)", "CON ESA VARA hay 1 arnes del censo fuera de la nomina"),
    ("C.2 y C.3", "literal `PROVISIONAL` **2** veces y `HUECO` **4**"),
]


def medir(ruta):
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (len(datos), len(lf), hashlib.sha256(datos).hexdigest(),
            hashlib.sha256(lf).hexdigest())


def fin_del_parrafo(lineas, i):
    """LA ULTIMA LINEA DEL PARRAFO QUE CONTIENE LA LINEA `i` (1-indexada). PURA.
    El parrafo acaba en la primera linea en blanco o en el fin del fichero."""
    j = i
    while j < len(lineas) and lineas[j].strip():
        j += 1
    return j


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    L = []
    w = L.append
    w("=" * 78)
    w("LAS TRES CORRECCIONES DE CIFRA DEL ACTA 199, EN SU SEDE")
    w("=" * 78)
    w("")

    if not os.path.isfile(SEDE):
        w("ROJO: no existe la sede %s" % SEDE)
        print(NL.join(L))
        return 1

    d, lf, sd, slf = medir(SEDE)
    w("A) LA SEDE, MEDIDA AL ENTRAR")
    w("   docs/loop/reportes/REPORTE_V199.md")
    w("   disco %d bytes | LF %d bytes" % (d, lf))
    w("   sha256 disco %s | sha256 LF %s" % (sd[:16], slf[:16]))
    texto = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    lineas = texto.split(NL)
    w("   CIFRA lineas por split(NL): %d | por count(NL): %d"
      % (len(lineas), texto.count(NL)))
    w("   la marca %r ya esta: %s" % (MARCA, "SI" if MARCA in texto else "NO"))
    w("")

    w("B) LOS TRES ANCLAJES, BUSCADOS Y NO TECLEADOS")
    ya = MARCA in texto
    if ya:
        w("   LA CORRECCION YA ESTA ESCRITA, ASI QUE EL ANCLAJE APARECE DOS VECES:")
        w("   la original y la que el bloque CITA. La exigencia de UNA SOLA vale")
        w("   para el fichero SIN corregir, y aqui se dice en vez de aflojarse.")
    hallados = []
    for etiqueta, aguja in ANCLAJES:
        hits = [i for i, l in enumerate(lineas, 1) if aguja in l]
        w("   %-16s %d acierto(s), linea(s) %s"
          % (etiqueta, len(hits), ", ".join(str(x) for x in hits) or "(ninguna)"))
        exigido = (len(hits) >= 1) if ya else (len(hits) == 1)
        if not exigido:
            w("   ROJO: el anclaje no aparece las veces que se exige. NO SE ESCRIBE.")
            print(NL.join(L))
            return 1
        hallados.append((etiqueta, hits[0]))
    w("")

    w("C) LA CIFRA DE LA C.1, RECOMPUTADA Y NO TECLEADA")
    w("   comando: V.arneses_que_faltan(vara=148) y V.arneses_que_faltan(vara=0)")
    w("   sobre scripts/loop/verificar_mutaciones_viejas.py")
    ultima, con_vara = V.arneses_que_faltan(vara=148)
    _u, sin_vara = V.arneses_que_faltan(vara=0)
    censo = V.arneses_del_directorio()
    w("   CIFRA entradas de la nomina: %d" % len(V.VIEJAS))
    w("   CIFRA arneses que el censo reconoce: %d" % len(censo))
    w("   LA VARA DEL CENSO, leida del modulo: %d" % V.VARA_DEL_CENSO)
    w("   CIFRA ultima vuelta representada en la nomina (INFORMATIVA): %s" % ultima)
    w("   CIFRA arneses del censo FUERA de la nomina CON LA VARA 148: %d"
      % len(con_vara))
    for n in con_vara:
        w("      %s" % n)
    w("   CIFRA arneses del censo FUERA de la nomina SIN VARA (vara=0): %d"
      % len(sin_vara))
    w("")

    w("D) LAS CIFRAS DE LA C.2 Y LA C.3, RECONTADAS DE SU FICHERO")
    t_inv = io.open(INVENTARIO, encoding="utf-8").read().replace(chr(13) + NL, NL)
    l_inv = t_inv.split(NL)
    sens = [i for i, l in enumerate(l_inv, 1) if "HUECO" in l]
    insens = [i for i, l in enumerate(l_inv, 1) if "hueco" in l.lower()]
    prov = [i for i, l in enumerate(l_inv, 1) if "PROVISIONAL" in l]
    d_i, lf_i, sd_i, slf_i = medir(INVENTARIO)
    w("   docs/plan/10_INVENTARIO.md: disco %d bytes | LF %d bytes" % (d_i, lf_i))
    w("   sha256 disco %s | sha256 LF %s" % (sd_i[:16], slf_i[:16]))
    w("   CIFRA lineas por split(NL): %d  (el camino del 414)" % len(l_inv))
    w("   CIFRA lineas por count(NL): %d  (el camino del 413)" % t_inv.count(NL))
    w("   CIFRA el fichero acaba en salto de linea: %s"
      % ("SI" if t_inv.endswith(NL) else "NO"))
    w("   CIFRA lineas con el literal HUECO (sensible): %d, lineas %s"
      % (len(sens), ", ".join(str(x) for x in sens)))
    w("   CIFRA apariciones del literal HUECO: %d" % t_inv.count("HUECO"))
    w("   CIFRA lineas con hueco (insensible): %d, lineas %s"
      % (len(insens), ", ".join(str(x) for x in insens)))
    w("   CIFRA lineas con PROVISIONAL: %d, lineas %s"
      % (len(prov), ", ".join(str(x) for x in prov)))
    w("")

    bloque = armar_bloque(con_vara, sin_vara, censo, len(V.VIEJAS),
                          l_inv, t_inv, sens, insens, prov, d_i, lf_i, slf_i)

    w("E) LO QUE SE ESCRIBE")
    if MARCA in texto:
        w("   NO SE ESCRIBE: la marca ya esta en la sede. IDEMPOTENTE.")
    elif not a.escribir:
        w("   MODO MEDICION: no se escribe nada.")
        w("   CIFRA lineas del bloque que se anadiria: %d"
          % (bloque.count(NL) + 1))
    else:
        nuevas = list(lineas)
        for etiqueta, ln in sorted(hallados, key=lambda x: -x[1]):
            fin = fin_del_parrafo(nuevas, ln)
            nuevas.insert(fin, "")
            nuevas.insert(fin + 1, AVISO % (etiqueta, MARCA))
            w("   AVISO insertado tras la linea %d (fin del parrafo de %s)"
              % (fin, etiqueta))
        salida_txt = NL.join(nuevas)
        if not salida_txt.endswith(NL):
            salida_txt += NL
        salida_txt += NL + bloque
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(salida_txt)
        w("   BLOQUE anadido al final, %d lineas" % (bloque.count(NL) + 1))

    d2, lf2, sd2, slf2 = medir(SEDE)
    w("")
    w("F) LA SEDE, REMEDIDA AL SALIR")
    w("   disco %d bytes | LF %d bytes" % (d2, lf2))
    w("   sha256 disco %s | sha256 LF %s" % (sd2[:16], slf2[:16]))
    w("   crecimiento en bytes LF: %d" % (lf2 - lf))
    w("   la marca %r esta ahora: %s"
      % (MARCA, "SI" if MARCA in io.open(SEDE, encoding="utf-8").read() else "NO"))
    w("")
    w("G) EL TEXTO VIEJO SIGUE ENTERO, Y SE COMPRUEBA EN VEZ DE PROMETERSE")
    w("   LA VARA CORRECTA NO ES 'APARECE UNA VEZ', Y SE DICE POR QUE: el bloque")
    w("   de correcciones CITA el texto viejo, asi que despues de escribir hay DOS")
    w("   apariciones de cada literal, la original y la citada. Exigir una sola")
    w("   seria exigir que la correccion no citara lo que corrige, que es justo lo")
    w("   contrario de lo que EJECUTOR.md 8 manda. LA VARA ES: sigue estando, y")
    w("   NO SE BORRO NI UNA LINEA.")
    t2 = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    intactos = 0
    for etiqueta, aguja in ANCLAJES:
        esta = t2.count(aguja)
        w("   %-16s el literal viejo sigue %d vez(ces) en la sede" % (etiqueta, esta))
        intactos += 1 if esta >= 1 else 0
    w("   CIFRA anclajes viejos que siguen en la sede: %d de %d"
      % (intactos, len(ANCLAJES)))
    lineas_viejas = texto.split(NL)
    lineas_nuevas = t2.split(NL)
    perdidas = [l for l in lineas_viejas if l not in set(lineas_nuevas)]
    w("   CIFRA lineas del fichero viejo que YA NO ESTAN en el nuevo: %d"
      % len(perdidas))
    for l in perdidas[:10]:
        w("      PERDIDA: %s" % l[:100])
    w("   CIFRA lineas del fichero viejo: %d | del nuevo: %d | anadidas: %d"
      % (len(lineas_viejas), len(lineas_nuevas),
         len(lineas_nuevas) - len(lineas_viejas)))
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V200_T1B_CORRECCIONES_EN_SU_SEDE.txt"),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


def armar_bloque(con_vara, sin_vara, censo, nomina, l_inv, t_inv, sens, insens,
                 prov, d_i, lf_i, slf_i):
    p = []
    p.append("---")
    p.append("")
    p.append("## %s" % MARCA)
    p.append("")
    p.append("**ESTE BLOQUE LO ESCRIBE LA VUELTA 200, NO LA 199.** Sale de la seccion 3 del")
    p.append("acta del auditor de la vuelta 199, que levanta **tres caidas de reporte** sobre")
    p.append("este fichero, y del encargo de la 200, que manda escribirlas **cada una en su")
    p.append("sede, por el carril del banco `9.10` mas `EJECUTOR.md` 8, con el texto viejo")
    p.append("entero y sin tachar**. **Arriba no se ha borrado ni un caracter**: cada parrafo")
    p.append("afectado lleva detras un aviso de una linea que apunta aqui.")
    p.append("")
    p.append("**Corte de todas las cifras de este bloque: 7 sep 2026.**")
    p.append("")
    p.append("### `C.1`, LA QUE ACUMULA: ERA UNO Y SON DOS, Y NO SE CORRIGE TECLEANDO EL DOS")
    p.append("")
    p.append("**LO QUE ESTE FICHERO DICE Y SE QUEDA DONDE ESTA:** su seccion 8 publica")
    p.append("*\"**1 arnes del censo queda fuera de la nomina con la vara 148**, y es")
    p.append("`vuelta197_tarea2_mutacion_orden_del_turno.py`\"*, y su seccion 9 repite el **1**")
    p.append("con vara y el **61** sin vara, sobre un censo de **196**.")
    p.append("")
    p.append("**LA CIFRA NO SE CORRIGE TECLEANDO EL DOS: SE PEGA LA SALIDA DEL INSTRUMENTO,")
    p.append("CORRIDO EN LA VUELTA 200** con `V.arneses_que_faltan()` sobre")
    p.append("`scripts/loop/verificar_mutaciones_viejas.py`:")
    p.append("")
    p.append("```")
    p.append("CIFRA entradas de la nomina: %d" % nomina)
    p.append("CIFRA arneses que el censo reconoce en scripts/loop/: %d" % len(censo))
    p.append("LA VARA DEL CENSO, leida del modulo: %d" % V.VARA_DEL_CENSO)
    p.append("CIFRA arneses del censo FUERA de la nomina CON LA VARA 148: %d"
             % len(con_vara))
    for n in con_vara:
        p.append("      %s" % n)
    p.append("CIFRA arneses del censo FUERA de la nomina SIN VARA (vara=0): %d"
             % len(sin_vara))
    p.append("```")
    p.append("")
    p.append("| que dice este fichero | que mide la 200 | de donde sale la de hoy |")
    p.append("|---|---|---|")
    p.append("| fuera de la nomina con vara 148: **1** | **%d** | `V.arneses_que_faltan(vara=148)` |"
             % len(con_vara))
    p.append("| fuera de la nomina sin vara: **61** | **%d** | `V.arneses_que_faltan(vara=0)` |"
             % len(sin_vara))
    p.append("| arneses que el censo reconoce: **196** | **%d** | `V.arneses_del_directorio()` |"
             % len(censo))
    p.append("")
    p.append("**EL SEGUNDO ES `vuelta199_tarea1_mutacion_guardas_revividas.py`, Y LO ESCRIBIO")
    p.append("ESTA MISMA VUELTA 199.** El **1** no era falso cuando se midio: sale del bloque")
    p.append("`F` del sello de apertura de la 199, tomado **antes** de que la vuelta escribiera")
    p.append("nada. **Lo que fallo es que se publico sin su corte en la seccion que traspasa")
    p.append("el estado a la vuelta siguiente**, y la 200 es vuelta de bateria con la nomina")
    p.append("congelada en 135, o sea que ese segundo arnes **no lo va a correr nadie**.")
    p.append("**Esto no se arregla metiendolo en la nomina**: la moratoria `AUDITOR.md` 6.3 la")
    p.append("congela, y meterlo seria saltarse una decision del fundador. **Se dice, y por")
    p.append("eso la seccion 9 del reporte de la 200 nombra LOS DOS.**")
    p.append("")
    p.append("### `C.2`: EL LITERAL `HUECO` SALE 3, NO 4. **SE CORRIGE LA CIFRA**")
    p.append("")
    p.append("**LO QUE ESTE FICHERO DICE Y SE QUEDA DONDE ESTA:** su seccion `4.d` publica")
    p.append("*\"con el literal `PROVISIONAL` **2** veces y `HUECO` **4**\"* sobre")
    p.append("`docs/plan/10_INVENTARIO.md`.")
    p.append("")
    p.append("**EL ENCARGO DE LA 200 PIDE ELEGIR ENTRE CORREGIR LA CIFRA O CORREGIR LA")
    p.append("ETIQUETA, Y SE DICE CUAL SE ELIGE: SE CORRIGE LA CIFRA.** El motivo es que la")
    p.append("etiqueta que el parrafo escribe es **el literal**, en singular y con la palabra")
    p.append("en mayusculas, y esa etiqueta describe bien la clausula de la `verificacion` que")
    p.append("se estaba midiendo. **La cifra que no calzaba con ella era la del patron")
    p.append("insensible a mayusculas.** Las dos se publican, cada una con su etiqueta:")
    p.append("")
    p.append("| etiqueta | patron | cifra de hoy | lineas |")
    p.append("|---|---|---:|---|")
    p.append("| lineas con el literal `HUECO` | sensible a mayusculas | **%d** | %s |"
             % (len(sens), ", ".join(str(x) for x in sens)))
    p.append("| apariciones del literal `HUECO` | sensible, contando repeticiones | **%d** | (no aplica) |"
             % t_inv.count("HUECO"))
    p.append("| lineas que nombran un hueco | insensible a mayusculas | **%d** | %s |"
             % (len(insens), ", ".join(str(x) for x in insens)))
    p.append("| lineas con `PROVISIONAL` | sensible a mayusculas | **%d** | %s |"
             % (len(prov), ", ".join(str(x) for x in prov)))
    p.append("")
    p.append("**LA CUARTA LINEA, LA QUE SOBRABA, ES LA %d**, y dice *hueco* en minusculas."
             % (sorted(set(insens) - set(sens))[0] if set(insens) - set(sens) else 0))
    p.append("**El `PROVISIONAL` **%d** si calzaba y no se toca.**" % len(prov))
    p.append("")
    p.append("**ES LA MISMA ESPECIE QUE LA ERRATA DEL `pares?` QUE ESTA MISMA VUELTA CAZO EN")
    p.append("SU TAREA 3:** la etiqueta nombra un sujeto y la cifra sale de otro patron.")
    p.append("")
    p.append("### `C.3`: EL FICHERO TIENE 413 LINEAS, NO 414. **SE CORRIGE LA CIFRA**")
    p.append("")
    p.append("**LO QUE ESTE FICHERO DICE Y SE QUEDA DONDE ESTA:** el mismo parrafo publica")
    p.append("**414 lineas** de `docs/plan/10_INVENTARIO.md`.")
    p.append("")
    p.append("**LAS DOS CONVENCIONES, MEDIDAS HOY Y PUBLICADAS LAS DOS**, que es lo que esta")
    p.append("casa hace mientras la convencion no este fijada:")
    p.append("")
    p.append("| camino | cifra de hoy |")
    p.append("|---|---:|")
    p.append("| `texto.split(chr(10))`, el camino del 414 | **%d** |" % len(l_inv))
    p.append("| `texto.count(chr(10))`, el camino del 413 | **%d** |" % t_inv.count(NL))
    p.append("| el fichero acaba en salto de linea | **%s** |"
             % ("SI" if t_inv.endswith(NL) else "NO"))
    p.append("| bytes en disco / bytes normalizados a LF | **%d** / **%d** |" % (d_i, lf_i))
    p.append("| `sha256` LF | `%s` |" % slf_i[:16])
    p.append("")
    p.append("**SE CORRIGE LA CIFRA A %d.** `split()` sobre un texto que termina en salto"
             % t_inv.count(NL))
    p.append("devuelve una ultima cadena vacia que no es una linea del fichero, y por eso el")
    p.append("**414** contaba una de mas. **El texto viejo se queda arriba entero**, que es la")
    p.append("unica forma de que esta correccion se pueda auditar.")
    p.append("")
    return NL.join(p) + NL


if __name__ == "__main__":
    raise SystemExit(main())
