# -*- coding: utf-8 -*-
r"""_v208_t1d_correccion.py . TAREA 1.d DE LA VUELTA 208: LA CAIDA `4.1` DEL ACTA
207 CONTRA MI, CORREGIDA EN EL REPORTE ARCHIVADO DE LA 207 POR CORRECCION
DECLARADA Y CON EL TEXTO VIEJO ENTERO ENCIMA.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3). No escribe ni clona ningun lector.

LA CAIDA, LITERAL DEL ACTA 207 (linea 72794 de `docs/loop/ACTA_AUDITOR.md`):
*"EL REPORTE DICE `6` ELEMENTOS DE `verificacion` Y SON `7`, Y LO PRUEBA SU
PROPIO INSTRUMENTO"*.

Y NO SE CORRIGE COPIANDO AL AUDITOR (`EJECUTOR.md` 2, EL INSTRUMENTO MANDA). La
cifra se REMIDE aqui, en esta vuelta, sobre la linea 41 de
`docs/plan/OPERACIONES.jsonl`, y ADEMAS se lee de la linea 21 de mi propia salida
sellada de la 207, `docs/loop/SALIDA_V207_T2_VARA.txt`, que ya imprimia
`CIFRA elementos de verificacion: 7`. **El instrumento midio bien; lo que perdio
uno fue la transcripcion al reporte.**

LO QUE SE ESCRIBE Y LO QUE NO:
  . SE ANADE un bloque de CORRECCION DECLARADA DEBAJO del parrafo que falla.
  . NO SE BORRA NI SE TACHA UNA SOLA LINEA DEL TEXTO VIEJO (`EJECUTOR.md` 8:
    una correccion que tapa lo que corrige no se puede auditar).
  . NO SE TOCA `docs/plan/OPERACIONES.jsonl`, que solo se LEE.

LAS GUARDAS, Y SON LAS QUE PUEDEN CAER:
  (a) el parrafo ancla aparece EXACTAMENTE UNA VEZ en el reporte archivado;
  (b) la cifra remedida por mi y la de mi salida sellada COINCIDEN en 7; si no,
      no se escribe nada y se declara la discrepancia;
  (c) `V.12`, `V.13` y `V.14` salen de `verificacion[0]`, `[1]` y `[2]`, y los
      cuatro elementos que faltaban de contar son CORRECCIONES DECLARADAS: se
      comprueba leyendo los siete elementos, no afirmandolo;
  (d) al salir, CERO lineas del texto de entrada faltan del de salida;
  (e) segunda corrida IDEMPOTENTE, cero bytes de crecimiento.
"""
import argparse
import hashlib
import io
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

VUELTA = 208
SUJETO = 207
LINEA_FICHA = 41
REPORTE = os.path.join(LOOP, "reportes", "REPORTE_V%d.md" % SUJETO)
OPES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VARA = os.path.join(LOOP, "SALIDA_V%d_T2_VARA.txt" % SUJETO)
LINEA_VARA = 21

ANCLA = ("**LA FICHA, MEDIDA:** **18** campos, **4** elementos de `evidencia`, "
         "**6** de" + NL + "`verificacion` de los cuales **4** son CORRECCIONES "
         "DECLARADAS, `fecha_corte`")
MARCA = "<!-- CORRECCION DECLARADA V208 T1D -->"


def dos_convenciones(ruta):
    d = io.open(ruta, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return (len(d), len(lf), hashlib.sha256(d).hexdigest()[:16],
            hashlib.sha256(lf).hexdigest()[:16], lf.decode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    ap.add_argument("--salida", default="T1D_CORRECCION")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 1.d: LA CAIDA `4.1` DEL ACTA %d, CORREGIDA POR"
      % (VUELTA, SUJETO))
    w("CORRECCION DECLARADA EN EL REPORTE ARCHIVADO DE LA %d" % SUJETO)
    w("=" * 78)
    w("")

    w("A) LA CIFRA, REMEDIDA POR MI SOBRE LA LINEA %d DE docs/plan/OPERACIONES.jsonl"
      % LINEA_FICHA)
    d_o, lf_o, sd_o, sl_o, texto_o = dos_convenciones(OPES)
    w("   docs/plan/OPERACIONES.jsonl: %d bytes en disco y %d normalizado a LF,"
      % (d_o, lf_o))
    w("   sha256 disco %s y sha256 LF %s" % (sd_o, sl_o))
    filas = texto_o.split(NL)
    w("   CIFRA lineas del fichero: %d" % len([x for x in filas if x.strip()]))
    ficha = json.loads(filas[LINEA_FICHA - 1])
    n_campos = len(ficha)
    n_evi = len(ficha.get("evidencia", []))
    ver = ficha.get("verificacion", [])
    n_ver = len(ver)
    correcciones = [i for i, v in enumerate(ver)
                    if v.strip().startswith("CORRECCION DECLARADA")]
    clausulas = [i for i in range(n_ver) if i not in correcciones]
    w("   CIFRA campos de la ficha: %d" % n_campos)
    w("   CIFRA elementos de `evidencia`: %d" % n_evi)
    w("   CIFRA elementos de `verificacion`: %d" % n_ver)
    w("   CIFRA de esos que son CORRECCION DECLARADA: %d (indices %s)"
      % (len(correcciones), ", ".join(str(i) for i in correcciones)))
    w("   CIFRA clausulas de verificacion que NO son correccion: %d (indices %s)"
      % (len(clausulas), ", ".join(str(i) for i in clausulas)))
    for i in clausulas:
        w("      verificacion[%d]: %s" % (i, ver[i][:120]))
    w("")

    w("B) LA MISMA CIFRA, LEIDA DE MI PROPIA SALIDA SELLADA DE LA %d" % SUJETO)
    if not os.path.isfile(VARA):
        w("   ROJO: %s NO EXISTE." % VARA)
        print(NL.join(L))
        return 1
    lineas_vara = io.open(VARA, encoding="utf-8").read().replace(
        chr(13) + NL, NL).split(NL)
    linea21 = lineas_vara[LINEA_VARA - 1]
    w("   docs/loop/SALIDA_V%d_T2_VARA.txt: %d bytes en disco"
      % (SUJETO, os.path.getsize(VARA)))
    w("   su linea %d, pegada entera y no parafraseada:" % LINEA_VARA)
    w("      %s" % linea21)
    de_la_vara = None
    if "elementos de" in linea21 and "verificacion" in linea21:
        de_la_vara = int(linea21.rsplit(":", 1)[1].strip())
    w("   CIFRA leida de esa linea: %s" % de_la_vara)
    w("")

    w("C) LAS DOS MEDICIONES, JUNTAS")
    w("   remedida por mi sobre la ficha:      %s" % n_ver)
    w("   leida de mi salida sellada de la 207: %s" % de_la_vara)
    w("   el reporte de la 207 publica:        6")
    calzan = (n_ver == de_la_vara == 7)
    w("   LAS DOS MIAS CALZAN EN 7: %s" % ("SI" if calzan else "NO"))
    if not calzan:
        w("   ROJO: mis dos mediciones no calzan. NO SE ESCRIBE NADA y la")
        w("   discrepancia se declara en el reporte en vez de resolverse copiando.")
        print(NL.join(L))
        return 1
    w("")

    w("D) LA COBERTURA NO CAMBIA, Y SE COMPRUEBA EN VEZ DE AFIRMARSE")
    w("   `V.12`, `V.13` y `V.14` salen de verificacion[0], [1] y [2].")
    ok_cob = (clausulas == [0, 1, 2] and len(correcciones) == 4)
    w("   los tres indices de los que salen son clausulas y no correcciones: %s"
      % ("SI" if clausulas == [0, 1, 2] else "NO"))
    w("   los cuatro elementos que faltaban de contar son CORRECCIONES")
    w("   DECLARADAS, que nunca fueron puntos de la vara: %s"
      % ("SI" if len(correcciones) == 4 else "NO"))
    w("   CIFRA puntos de la vara que se mueven por esta correccion: 0")
    if not ok_cob:
        w("   ROJO: el reparto de los siete elementos no es el que la correccion")
        w("   afirma. NO SE ESCRIBE NADA.")
        print(NL.join(L))
        return 1
    w("")

    w("E) EL REPORTE ARCHIVADO, Y LA GUARDA DEL ANCLA")
    d0, lf0, sd0, sl0, texto0 = dos_convenciones(REPORTE)
    w("   docs/loop/reportes/REPORTE_V%d.md: %d bytes en disco y %d normalizado a"
      % (SUJETO, d0, lf0))
    w("   LF, sha256 disco %s y sha256 LF %s" % (sd0, sl0))
    w("   CIFRA lineas: %d" % len(texto0.split(NL)))
    n_ancla = texto0.count(ANCLA)
    w("   CIFRA veces que el parrafo ancla aparece: %d (se exige 1)" % n_ancla)
    if n_ancla != 1:
        w("   ROJO: el ancla no aparece exactamente una vez. NO SE ESCRIBE NADA.")
        print(NL.join(L))
        return 1
    ya = MARCA in texto0
    w("   la correccion YA ESTA escrita: %s" % ("SI" if ya else "NO"))
    w("")

    bloque = NL.join([
        "",
        MARCA,
        "",
        "> **CORRECCION DECLARADA (7 sep 2026, vuelta %d, TAREA 1.d), POR ADICION,"
        % VUELTA,
        "> CON EL TEXTO VIEJO ENTERO ARRIBA, SIN TACHARLO Y SIN CLAVE NUEVA DE",
        "> ESQUEMA.** El parrafo de aqui arriba publica **6** elementos de",
        "> `verificacion` y son **SIETE**. La caida la levanto el auditor en la",
        "> `4.1` de su acta de la vuelta %d, y **no la corrijo copiandole**"
        % SUJETO,
        "> (`EJECUTOR.md` 2, EL INSTRUMENTO MANDA): la remedi yo en la vuelta %d"
        % VUELTA,
        "> sobre la linea **%d** de `docs/plan/OPERACIONES.jsonl`, que da"
        % LINEA_FICHA,
        "> **%d** campos, **%d** elementos de `evidencia` y **%d** de"
        % (n_campos, n_evi, n_ver),
        "> `verificacion`, de los cuales **%d** son CORRECCIONES DECLARADAS."
        % len(correcciones),
        ">",
        "> **Y NO HACIA FALTA IR A LA FICHA: MI PROPIA SALIDA SELLADA YA LO DECIA.**",
        "> `docs/loop/SALIDA_V%d_T2_VARA.txt`, en su linea **%d**, imprime"
        % (SUJETO, LINEA_VARA),
        "> literalmente `%s`. **El instrumento midio bien y la transcripcion al"
        % linea21.strip(),
        "> reporte perdio uno.**",
        ">",
        "> **LA COBERTURA NO CAMBIA NI EN UN PUNTO, Y ESO TAMBIEN VA MEDIDO.**",
        "> `V.12`, `V.13` y `V.14` salen de `verificacion[0]`, `[1]` y `[2]`, que",
        "> son las **%d** clausulas que no son correcciones; los **%d** elementos"
        % (len(clausulas), len(correcciones)),
        "> que faltaban de contar son las CORRECCIONES DECLARADAS, **que nunca",
        "> fueron puntos de la vara**. **Puntos de la vara que se mueven por esta",
        "> correccion: 0.** El cotejo de la `2.b` y la cobertura de la `2.c` se",
        "> quedan exactamente como estan.",
        "",
    ])

    w("F) EL BLOQUE COMPUESTO")
    w("   CIFRA bytes del bloque: %d" % len(bloque.encode("utf-8")))
    w("   CIFRA lineas del bloque: %d" % bloque.count(NL))
    w("   CIFRA guiones largos: %d | guiones medios: %d"
      % (bloque.count(chr(8212)), bloque.count(chr(8211))))
    if bloque.count(chr(8212)) or bloque.count(chr(8211)):
        w("   ROJO: el bloque trae guiones prohibidos. NO SE ESCRIBE.")
        print(NL.join(L))
        return 1
    w("")

    if a.escribir and not ya:
        # SE INSERTA JUSTO DESPUES DEL PARRAFO ANCLA, o sea CON EL TEXTO VIEJO
        # ENTERO ENCIMA. El ancla se corta en su punto final, que es el fin de la
        # frase del `bloquea_a`, para no partir el parrafo por la mitad.
        i = texto0.index(ANCLA)
        fin = texto0.index(NL + NL, i)
        nuevo = texto0[:fin] + NL + bloque + texto0[fin:]
        io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("   ESCRITO: la correccion queda anadida DEBAJO del parrafo viejo.")
    elif a.escribir:
        w("   NO SE ESCRIBE: la correccion ya estaba. IDEMPOTENTE.")
    else:
        w("   MODO MEDICION: no se escribe nada.")
    w("")

    w("=" * 78)
    w("EL CIERRE, REMEDIDO Y NO HEREDADO")
    w("=" * 78)
    d1, lf1, sd1, sl1, texto1 = dos_convenciones(REPORTE)
    w("   docs/loop/reportes/REPORTE_V%d.md al salir: %d bytes en disco y %d"
      % (SUJETO, d1, lf1))
    w("   normalizado a LF, sha256 disco %s y sha256 LF %s" % (sd1, sl1))
    w("   CIFRA crecimiento en bytes de disco: %d" % (d1 - d0))
    w("   CIFRA crecimiento en bytes LF: %d" % (lf1 - lf0))
    w("   CIFRA lineas al salir: %d (al entrar %d)"
      % (len(texto1.split(NL)), len(texto0.split(NL))))
    w("")
    w("LA GUARDA DEL TEXTO VIEJO: NI UNA LINEA BORRADA NI UNA CAMBIADA")
    viejas, nuevas = texto0.split(NL), texto1.split(NL)
    faltan, j = 0, 0
    for l in viejas:
        while j < len(nuevas) and nuevas[j] != l:
            j += 1
        if j >= len(nuevas):
            faltan += 1
        else:
            j += 1
    w("   CIFRA lineas del texto de ENTRADA que NO estan, en orden, en el de")
    w("   SALIDA: %d" % faltan)
    w("   (si esta cifra no es 0, es ROJO)")
    w("")
    w("LA SEDE QUE SOLO SE LEYO, REMEDIDA AL CIERRE")
    d_o2, lf_o2, sd_o2, sl_o2, _t = dos_convenciones(OPES)
    w("   docs/plan/OPERACIONES.jsonl: %d bytes en disco y %d normalizado a LF,"
      % (d_o2, lf_o2))
    w("   sha256 disco %s y sha256 LF %s" % (sd_o2, sl_o2))
    w("   IDENTICO AL DE LA APERTURA DE ESTA CORRIDA: %s"
      % ("SI" if (d_o, lf_o, sd_o, sl_o) == (d_o2, lf_o2, sd_o2, sl_o2) else "NO"))
    w("")
    w("FIN")
    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0 if faltan == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
