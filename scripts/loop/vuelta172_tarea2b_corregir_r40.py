# -*- coding: utf-8 -*-
r"""vuelta172_tarea2b_corregir_r40.py . TAREA 2.b DE LA VUELTA 172.

CORRIGE LA AFIRMACION FALSA DEL `R.40` POR EL CARRIL DEL BANCO `9.10`
(adjudicacion 6.3 del acta 171).

EL HECHO, Y NO SE CREE: la entrada `R.40` de `docs/PENDIENTES.md`, escrita en la
TAREA 1.a de la vuelta 171, publica de la adjudicacion 6.1 la via **EJECUTADA** y
la glosa *"EJECUTADA, TAREA 3 de esta vuelta ... las 16 filas de la segunda tanda
ganan `LD-139` a `LD-154` por ADICION PURA"*. **LA TAREA 3 DE LA VUELTA 171 NO SE
CORRIO**, y el propio reporte de la 171 lo dice. La causa era de orden: la
entrada se escribio la primera de la vuelta y nadie volvio a ella.

EL CARRIL, TAL COMO EL BANCO `9.10` LO ESCRIBE Y COMO LA VUELTA 171 LO USO PARA
EL `R.38`:
  . LA FRASE VIEJA SE QUEDA ENTERA Y SE TACHA. No se borra ni se reescribe.
  . LA CORRECCION VA FECHADA DEBAJO, CON LA MEDICION PEGADA.
  . NADA MAS SE TOCA.

Y EL CRITERIO DEL `D.3` DE LA VUELTA 171, QUE LA `6.9` DEL ACTA 171 DIO POR
CORRECTO, SE APLICA AQUI: **se tacha lo falso, no la oracion entera por
vecindad**. En la glosa de la 6.1 hay una parte CIERTA (que la regla estaba
escrita en `serie_de_registros.py`, con su cita de codigo) y esa parte se queda
en pie; lo falso es el tiempo verbal de la ejecucion.

EL REPARTO POR VIA SE RECOMPUTA POR INSTRUMENTO Y NO SE TECLEA: el
`EJECUTADA: 8` de la entrada cuenta la 6.1 entre las ocho, asi que la cifra
tambien es falsa. Se lee la entrada, se cuentan sus `VIA:`, se reclasifica la
6.1 y se imprimen las dos cifras al lado.

LO QUE NO SE TOCA, Y VA DICHO PARA QUE NADIE LO SUPONGA: **la glosa de la 6.2
del `R.40` no se toca**, por letra de la adjudicacion 6.3 del acta 171, que dice
que describe bien lo que paso, parada incluida. Su `VIA: EJECUTADA` tampoco.

CERO REPARACIONES DE NODOS: este fichero solo toca docs/PENDIENTES.md.

USO:
  python scripts/loop/vuelta172_tarea2b_corregir_r40.py
"""
import io
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
REPORTE_171 = os.path.join(RAIZ, "docs", "loop", "reportes", "REPORTE_V171.md")

CAB_R40 = "## R.40. Registro de las doce adjudicaciones"
FECHA = "5 sep 2026"

CLAUSULA_FALSA = ("EJECUTADA, TAREA 3 de esta vuelta. La 'parada' de la numeracion "
                  "`LD` queda cerrada por donde el acta dice:")
FRASE_FALSA_2 = ("EL SIGUIENTE LIBRE ES EL MAYOR MAS UNO, y las 16 filas de la segunda "
                 "tanda ganan `LD-139` a `LD-154` por ADICION PURA, con los numeros "
                 "COMPUTADOS POR INSTRUMENTO y sin tocar una palabra de su texto.")
VIA_FALSA = "  - **6.1 (`docs/loop/ACTA_AUDITOR.md:57628`, leida hoy). VIA: EJECUTADA.** Titulo"


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def acotar(lineas, cabecera):
    """La entrada, acotada por su cabecera y la siguiente `## R.n.`."""
    inicios = [i for i, l in enumerate(lineas, 1) if l.startswith(cabecera)]
    if len(inicios) != 1:
        return None, None, "la cabecera %r aparece %d veces" % (cabecera, len(inicios))
    ini = inicios[0]
    sig = [i for i, l in enumerate(lineas, 1)
           if i > ini and re.match(r"^##\s+R\.\d+\.", l)]
    return ini, (min(sig) - 1 if sig else len(lineas)), None


def main():
    print("=" * 78)
    print("VUELTA 172, TAREA 2.b: EL `R.40` TRAE UNA AFIRMACION FALSA Y SE CORRIGE")
    print("=" * 78)
    print("")
    rojos = []

    texto = leer(SEDE)
    lineas = texto.split(NL)

    print("A) LA ENTRADA, ACOTADA ANTES DE TOCAR NADA")
    ini, fin, err = acotar(lineas, CAB_R40)
    if err:
        print("   PARADA: " + err)
        return 1
    print("   `R.40` en docs/PENDIENTES.md, lineas %d a %d" % (ini, fin))
    cuerpo = NL.join(lineas[ini - 1:fin])
    print("   CIFRA bytes de la entrada: %d" % len(cuerpo.encode("utf-8")))
    print("")

    print("B) LA AFIRMACION FALSA, LOCALIZADA Y CONTADA")
    for etiqueta, aguja in (("la via EJECUTADA de la 6.1", VIA_FALSA),
                            ("la clausula 'EJECUTADA, TAREA 3 de esta vuelta'", CLAUSULA_FALSA),
                            ("la frase de las 16 filas en pasado", FRASE_FALSA_2)):
        dentro = cuerpo.count(aguja)
        entero = texto.count(aguja)
        print("   %-48s dentro del R.40: %d | en el fichero entero: %d"
              % (etiqueta, dentro, entero))
        if dentro != 1 or entero != 1:
            rojos.append("%s no aparece exactamente una vez dentro y una en el fichero"
                         % etiqueta)
    print("")

    print("C) LA PRUEBA DE QUE ES FALSA, CONTADA DEL REPORTE ARCHIVADO DE LA 171")
    rep = leer(REPORTE_171)
    veces = rep.count("NO SE CORRE")
    print("   docs/loop/reportes/REPORTE_V171.md -> %d bytes" % len(rep.encode("utf-8")))
    print("   CIFRA veces que dice 'NO SE CORRE': %d" % veces)
    filas_no_corre = [l.strip()[:96] for l in rep.split(NL) if "NO SE CORRE" in l]
    for l in filas_no_corre:
        print("      %s" % l)
    if veces < 1:
        rojos.append("el reporte archivado de la 171 no dice NO SE CORRE ni una vez")
    c, log = git(["log", "--format=%h", "0caca89f..cae2731d", "--",
                  "docs/plan/LECTURAS_DIRIGIDAS.md"])
    tocaron = [l for l in log.split(NL) if l.strip()]
    print("   CIFRA commits de la vuelta 171 que tocan docs/plan/LECTURAS_DIRIGIDAS.md: %d"
          % len(tocaron))
    if tocaron:
        rojos.append("la vuelta 171 SI toco LECTURAS_DIRIGIDAS.md; revisar el hecho")
    print("   (cero commits tocandolo es la prueba dura de que la TAREA 3 no corrio)")
    print("")

    print("D) EL REPARTO POR VIA, RECOMPUTADO DE LA PROPIA ENTRADA Y NO TECLEADO")
    vias = re.findall(r"^  - \*\*(6\.\d+) \(`[^`]+`, leida hoy\)\. VIA: ([A-Z ]+)\.\*\*",
                      cuerpo, re.M)
    print("   CIFRA lineas de VIA halladas en el R.40: %d" % len(vias))
    if len(vias) != 12:
        rojos.append("el R.40 no trae doce lineas de VIA sino %d" % len(vias))
    viejo = {}
    for clave, via in vias:
        viejo.setdefault(via.strip(), []).append(clave)
    for via in sorted(viejo):
        print("   VIEJO  %-16s %d (%s)" % (via, len(viejo[via]), ", ".join(viejo[via])))
    nuevo = {}
    for clave, via in vias:
        etiqueta = "NO SE CORRIO" if clave == "6.1" else via.strip()
        nuevo.setdefault(etiqueta, []).append(clave)
    for via in sorted(nuevo):
        print("   NUEVO  %-16s %d (%s)" % (via, len(nuevo[via]), ", ".join(nuevo[via])))
    linea_vieja = "; ".join("%s: %d (%s)" % (v, len(viejo[v]), ", ".join(viejo[v]))
                            for v in sorted(viejo))
    linea_nueva = "; ".join("%s: %d (%s)" % (v, len(nuevo[v]), ", ".join(nuevo[v]))
                            for v in sorted(nuevo))
    print("")

    print("E) LO QUE NO SE TOCA, COMPROBADO ANTES DE ESCRIBIR")
    aguja_62 = "  - **6.2 (`docs/loop/ACTA_AUDITOR.md:57649`, leida hoy). VIA: EJECUTADA.** Titulo"
    print("   la linea de la 6.2 esta en la entrada: %s"
          % ("SI" if aguja_62 in cuerpo else "NO"))
    if aguja_62 not in cuerpo:
        rojos.append("no se encuentra la linea de la 6.2 que hay que NO tocar")
    print("   (la 6.3 del acta 171 dice que su glosa describe bien lo que paso)")
    print("")

    if rojos:
        print("ROJO, %d motivo(s), y NO se escribe nada:" % len(rojos))
        for r in rojos:
            print("   " + r)
        return 1

    print("F) SE ESCRIBE, POR EL CARRIL DEL `9.10`")
    largos_antes = texto.count(chr(8212))
    medios_antes = texto.count(chr(8211))
    print("   guiones largos y medios que YA HABIA en el fichero: %d y %d"
          % (largos_antes, medios_antes))
    print("   (el fichero es historico y trae 54 de antiguo; la guarda mira el DELTA,")
    print("    no el total, o una guarda buena se caeria por culpa de texto de 2026)")

    via_corregida = (
        "  - **6.1 (`docs/loop/ACTA_AUDITOR.md:57628`, leida hoy). "
        "~~VIA: EJECUTADA.~~ VIA CORREGIDA (%s): NO SE CORRIO.** Titulo" % FECHA)
    texto = texto.replace(VIA_FALSA, via_corregida)

    tachada_1 = "~~%s~~" % CLAUSULA_FALSA
    texto = texto.replace(CLAUSULA_FALSA, tachada_1)
    tachada_2 = "~~%s~~" % FRASE_FALSA_2
    texto = texto.replace(FRASE_FALSA_2, tachada_2)

    correccion = (
        NL + NL +
        "    **CORRECCION DECLARADA (%s, vuelta 172, TAREA 2.b; adjudicacion 6.3 del" % FECHA + NL +
        "    acta 171). LO TACHADO DE ARRIBA ES FALSO Y SE QUEDA ENTERO Y TACHADO, QUE" + NL +
        "    ES EL CARRIL DEL BANCO `9.10`: UNA CORRECCION QUE TAPA LO QUE CORRIGE NO SE" + NL +
        "    PUEDE AUDITAR.** La TAREA 3 de la vuelta 171 **no se corrio**. La guarda de" + NL +
        "    su TAREA 2 cayo (las dos varas del contador no convergian) y la 3 quedo sin" + NL +
        "    correr; esta glosa se escribio ANTES, en la TAREA 1.a de aquella vuelta, y" + NL +
        "    nadie volvio a ella." + NL + NL +
        "    **LA MEDICION, PEGADA Y CORRIDA HOY POR `scripts/loop/vuelta172_tarea2b_correg" + NL +
        "    ir_r40.py`:** el reporte archivado de la 171" + NL +
        "    (`docs/loop/reportes/REPORTE_V171.md`) dice **%d veces** *\"NO SE CORRE\"*, y" % veces + NL +
        "    `git log 0caca89f..cae2731d -- docs/plan/LECTURAS_DIRIGIDAS.md` devuelve" + NL +
        "    **%d commits**: la vuelta 171 no toco el fichero donde esas 16 filas viven." % len(tocaron) + NL + NL +
        "    **QUE SE TACHA Y QUE NO, PORQUE ES UNA DECISION.** La glosa abria diciendo" + NL +
        "    que la regla estaba escrita en el codigo de `serie_de_registros.py`, con su" + NL +
        "    cita de lineas, **y eso es CIERTO y se queda en pie**. Lo falso es el tiempo" + NL +
        "    verbal de la ejecucion, y es lo unico tachado. Es el criterio del `D.3` de la" + NL +
        "    vuelta 171, que la `6.9` del acta 171 dio por correcto: enterrar una" + NL +
        "    afirmacion buena para tapar una mala no es corregir." + NL + NL +
        "    **Y LA VIA TAMBIEN ERA FALSA, ASI QUE EL REPARTO DE ABAJO TAMBIEN LO ES.** El" + NL +
        "    reparto se ha RECOMPUTADO POR INSTRUMENTO leyendo las doce lineas `VIA:` de" + NL +
        "    esta misma entrada, no tecleando:" + NL + NL +
        "    - reparto VIEJO, contado de la entrada: **%s**" % linea_vieja + NL +
        "    - reparto CORREGIDO, con la 6.1 reclasificada: **%s**" % linea_nueva + NL + NL +
        "    **LA ETIQUETA `NO SE CORRIO` NO ESTABA EN EL VOCABULARIO DE VIAS DE LA CASA**" + NL +
        "    (que trae `EJECUTADA`, `SIN TOCAR NADA` y `AL FUNDADOR`) y **se declara como" + NL +
        "    estreno**, no se cuela: describe un hecho medido y ninguna regla escrita la" + NL +
        "    prohibe, pero estrenar una palabra es lo que el `D.5` de la vuelta 170 hizo y" + NL +
        "    se le pidio cuenta. Va como discutible en el reporte de la vuelta 172." + NL + NL +
        "    **LO QUE ESTA CORRECCION NO TOCA:** la glosa de la `6.2` ni su via, por letra" + NL +
        "    de la adjudicacion 6.3 del acta 171, que dice que describe bien lo que paso," + NL +
        "    parada incluida. Y no toca ninguna otra entrada de la serie." + NL)

    ancla_fin_glosa_61 = tachada_2 + (" El `D.6` (la adyacencia del tramo `LD-12` a `LD-27`) "
                                      "se publica como CONTRASTE MEDIDO y no como fundamento: "
                                      "una adyacencia no es una asignacion.")
    if texto.count(ancla_fin_glosa_61) != 1:
        print("   ROJO: no se localiza el final de la glosa de la 6.1 para adosar debajo.")
        return 1
    texto = texto.replace(ancla_fin_glosa_61, ancla_fin_glosa_61 + correccion)

    io.open(SEDE, "w", encoding="utf-8", newline=NL).write(texto)
    print("   ESCRITO: docs/PENDIENTES.md (%d bytes)" % len(texto.encode("utf-8")))
    print("")

    print("G) LA RELECTURA DEL DISCO")
    de_nuevo = leer(SEDE)
    lineas2 = de_nuevo.split(NL)
    ini2, fin2, err2 = acotar(lineas2, CAB_R40)
    cuerpo2 = NL.join(lineas2[ini2 - 1:fin2]) if not err2 else ""
    fallos = 0
    for etiqueta, cond in (
            ("la clausula falsa sigue ENTERA en el fichero",
             CLAUSULA_FALSA in de_nuevo),
            ("y ahora esta TACHADA", tachada_1 in de_nuevo),
            ("la frase de las 16 filas sigue ENTERA", FRASE_FALSA_2 in de_nuevo),
            ("y ahora esta TACHADA", tachada_2 in de_nuevo),
            ("la via vieja de la 6.1 sigue escrita y tachada",
             "~~VIA: EJECUTADA.~~ VIA CORREGIDA" in de_nuevo),
            ("la parte CIERTA de la glosa sigue en pie y sin tachar",
             "`serie_de_registros.py:97-102`" in de_nuevo),
            ("la correccion esta dentro del R.40", "CORRECCION DECLARADA (%s" % FECHA in cuerpo2),
            ("el reparto corregido esta escrito", linea_nueva in de_nuevo),
            ("el reparto viejo tambien, sin borrarlo", linea_vieja in de_nuevo),
            ("la linea de la 6.2 sigue INTACTA", aguja_62 in de_nuevo),
            ("no se toco ninguna otra entrada de la serie",
             de_nuevo.count("CORRECCION DECLARADA (%s, vuelta 172, TAREA 2.b" % FECHA) == 1),
            ("no anado ni un guion largo ni uno medio (delta cero)",
             de_nuevo.count(chr(8212)) == largos_antes
             and de_nuevo.count(chr(8211)) == medios_antes),
            ("y mi propio bloque de correccion no trae ninguno",
             chr(8212) not in correccion and chr(8211) not in correccion)):
        print("   %-58s %s" % (etiqueta, "SI" if cond else "NO"))
        if not cond:
            fallos += 1
    print("   CIFRA comprobaciones: 13 | fallan: %d" % fallos)
    print("")
    if fallos:
        print("ROJO: el fichero escrito no cumple %d de sus propias guardas." % fallos)
        return 1
    print("VERDE: el `R.40` queda corregido por el carril del `9.10`.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
