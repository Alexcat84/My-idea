# -*- coding: utf-8 -*-
r"""vuelta174_tarea2a_registrar_acta172.py . TAREA 2.a de la vuelta 174.

REGISTRA EN LA FORMA DE LA CASA (`R.N`) EL ACTA 172 ENTERA: SUS ADJUDICACIONES
`6.n` Y LAS CAIDAS PROPIAS DEL AUDITOR de su seccion 3. Es la sub-tarea que la
vuelta 172 encargo, la 173 no ejecuto y el encargo de la 174 vuelve a pedir.

NO ES UN CLON: LA MAQUINA SE IMPORTA. Los clones anteriores
(`vuelta171_tarea1_registrar_acta170.py`, `vuelta172_tarea1_registrar_acta171.py`)
copiaban el mecanismo entero cada vuelta, y una maquina copiada tres veces son
tres sitios donde arreglar el mismo fallo. Aqui `PAT_CAIDA`, `PALABRA`,
`titulo_de_la_negrita`, `claves_de_adjudicacion` y `_cuenta_caidas` **se importan
de `vuelta172_tarea1_registrar_acta171.py`**, que es su ultima sede y la que la
bateria ya vigila con su arnes `vuelta172_tarea1b_mutacion_registro.py`. Es la
regla de la casa sobre fuentes unicas, la misma que la `6.6` del acta 172
adjudica como correcta y obligatoria. Lo unico propio de este fichero es **el
acote de SU acta y sus tablas de glosas**.

Y HAY UNA DIFERENCIA DE FONDO CON EL `R.41`, QUE ES LA QUE CIERRA EL CIRCULO QUE
LA `6.4` DEL ACTA 172 ABRIO. El `R.41` se escribio **la primera** de su vuelta,
cuando ninguna tarea habia corrido, y por eso sus glosas dicen *"VA A EJECUTARSE
... Y TODAVIA NO HA CORRIDO"* y el campo se llama **VIA PREVISTA**. **Esta
entrada se escribe la penultima**, con la TAREA 1 entera ya cerrada y medida, asi
que sus glosas **SI afirman en pasado, y cada una lleva al lado la linea o la
salida que la mide**, que es exactamente lo que `EJECUTOR.md` 1 pide. El campo se
llama **VIA** a secas, sin la palabra PREVISTA, y **por eso esta entrada no
necesita ningun fichero de confirmacion posterior**: no hay nada que confirmar
despues, porque nada se afirmo antes de tiempo.

NINGUNA CIFRA SE TECLEA: el numero de la entrada lo computa
`serie_de_registros.py` recomputando la serie de sus DOS sedes; las
adjudicaciones se barren del acta parando en el primer hueco; las caidas se
cuentan de las negritas `CAIDA n` del cuerpo acotado; y los numerales en palabra
del titulo salen de esos dos conteos.

UNA VIA QUE NO EXISTE, DECLARADA COMO PENDIENTE DE DOCTRINA EN VEZ DE
INVENTADA (`EJECUTOR.md` 5). La adjudicacion `6.3` del acta 172 (mover la
bateria al principio de la vuelta) **quedo superada por una decision del
fundador posterior**, la del 5 sep 2026 que la saca del ciclo por vuelta. Las
tres etiquetas de VIA que existen escritas son `EJECUTADA`, `SIN TOCAR NADA` y
`NO SE CORRIO`, y **ninguna dice "superada por decision del fundador"**. No se
estrena ninguna: se usa `NO SE CORRIO`, que es la mas cercana y la que no
afirma de mas, y la glosa dice el motivo entero con su cita. **Queda como
PENDIENTE DE DOCTRINA en el reporte.**

USO:  python scripts/loop/vuelta174_tarea2a_registrar_acta172.py
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE                      # noqa: E402
import vuelta172_tarea1_registrar_acta171 as MAQUINA    # noqa: E402

RAIZ = SERIE.RAIZ
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 172"
VUELTA_DEL_ACTA = 172
VUELTA_QUE_ESCRIBE = 174
NL = chr(10)

FRASE_DE_LA_SEDE = "la sede por defecto es `docs/PENDIENTES.md`"

PAT_CAIDA = MAQUINA.PAT_CAIDA
PALABRA = MAQUINA.PALABRA


def titulo_de_la_entrada(n_adj, n_cai):
    """El titulo, con sus dos numerales COMPUTADOS y no tecleados."""
    cola = ("la caida propia" if n_cai == 1
            else "las %s caidas propias" % PALABRA[n_cai])
    return ("Registro de las %s adjudicaciones y %s del acta de la vuelta %d"
            % (PALABRA[n_adj], cola, VUELTA_DEL_ACTA))


VIA = {
    "6.1": "SIN TOCAR NADA",
    "6.2": "EJECUTADA",
    "6.3": "NO SE CORRIO",
    "6.4": "EJECUTADA",
    "6.5": "SIN TOCAR NADA",
    "6.6": "SIN TOCAR NADA",
    "6.7": "SIN TOCAR NADA",
    "6.8": "SIN TOCAR NADA",
    "6.9": "SIN TOCAR NADA",
    "6.10": "SIN TOCAR NADA",
    "6.11": "NO SE CORRIO",
}

QUE_HACE_ESTA_VUELTA = {
    "6.1": ("SE ACATA SIN TOCAR NADA. La adjudicacion da por correcto el `D.2` de la "
            "vuelta 172 y aclara que las dos lecturas de la guarda eran ciertas y de "
            "preguntas distintas. Y ESTA VUELTA HA IDO UN PASO MAS ALLA POR SU CUENTA, "
            "cosa que la `6.1` no encarga y que por eso sube como discutible: el paso 0 "
            "del esqueleto de la 174 deja de preguntar por `VUELTA - 1` y pregunta por "
            "el reporte que de verdad va a pisar, con el numero LEIDO de la cabecera de "
            "ese fichero. La vuelta 173 no escribio ningun reporte, asi que el sujeto "
            "tecleado ya no servia. MEDIDO HOY en "
            "`docs/loop/SALIDA_V174_T1B_ESQUELETO.txt`: sobre la 173 la guarda da ROJO "
            "por su clausula (b) y se publica igual; sobre la 172 da VERDE con los dos "
            "sha256 calzando en `d29e45527ea302a0`."),
    "6.2": ("EJECUTADA, Y NO POR ESTA VUELTA: la construyo la vuelta 173 en su TAREA "
            "1.b, commit `c5b69ad9`, con los 17 casos viejos intactos y un arnes nuevo "
            "de 24. LO QUE ESTA VUELTA APORTA ES SU ESTRENO, que es la unica forma de "
            "saber si sirve: el reporte de la vuelta 172 se cerro con ella en la TAREA "
            "1.a de hoy, con la seccion 9 en HUECO DECLARADO Y MEDIDO y sus tres piezas "
            "juntas (nombre del fichero, bytes medidos y atribucion). MEDIDO en "
            "`docs/loop/SALIDA_V174_T1A_CERRAR_REPORTE_172.txt`: `CIFRA piezas que "
            "faltan: 0`. Sin este carril, el reporte de la 172 no se podia cerrar."),
    "6.3": ("NO SE CORRIO, Y EL MOTIVO NO ES DESCUIDO SINO QUE UNA DECISION POSTERIOR "
            "LA DEJO SIN OBJETO. La adjudicacion movia la bateria al PRINCIPIO de la "
            "vuelta. La vuelta 173 aplico ese remedio entero y su bateria siguio "
            "saliendo en CERO BYTES, y sobre esa medicion el fundador decidio el 5 sep "
            "2026 que la bateria SALE del ciclo por vuelta y corre CADA CINCO, en una "
            "vuelta propia que no lleva nada mas (`docs/loop/AUDITOR.md` seccion 6.1, "
            "citada en `EJECUTOR.md` 1, y la parada entera en "
            "`docs/loop/paradas/2026-09-05-la-bateria-sin-techo-DECISION.md`). Mover al "
            "principio algo que ya no corre cada vuelta no significa nada. NINGUNA DE "
            "LAS TRES ETIQUETAS DE VIA ESCRITAS DICE 'SUPERADA POR DECISION DEL "
            "FUNDADOR', asi que se usa la mas cercana y el hueco de doctrina se declara "
            "en el reporte en vez de rellenarse con una etiqueta inventada."),
    "6.4": ("EJECUTADA EN LA TAREA 2.b DE ESTA VUELTA, Y LA MEDICION VA AL LADO. La "
            "adjudicacion da por correcto el `D.1` (que las glosas del `R.41` no "
            "afirmen en pasado) y dice que lo unico que falta es el fichero que la "
            "entrada nombra. Ese fichero, `scripts/loop/vuelta172_tarea1b_confirmar_r41.py`, "
            "NACE HOY: llevaba dos vueltas prometido y sin existir, y por la regla del "
            "5 sep 2026 (LA RUTA QUE PROMETE PRUEBA ES CIFRA) el `R.41` estaba "
            "publicando una ruta sobre un vacio. Su corrida vive en "
            "`docs/loop/SALIDA_V174_T2B_CONFIRMAR_R41.txt`."),
    "6.5": ("SE ACATA SIN TOCAR NADA. El `D.3` (que naciera "
            "`scripts/loop/anexar_tarea_al_reporte.py`, de nombre estable y sin numero "
            "de vuelta) queda adjudicado como correcto. Esta vuelta no lo reabre: LO "
            "USA, y es la primera que lo usa para las dos filas de su propio reporte."),
    "6.6": ("SE ACATA SIN TOCAR NADA. El `D.4` (sacar el criterio de exclusion a una "
            "funcion pura llamable) queda adjudicado como correcto y obligatorio, con "
            "la frase que esta vuelta se lleva entera: UNA GUARDA QUE NO SE PUEDE "
            "LLAMAR NO SE PUEDE PROBAR. Los dos instrumentos nuevos de hoy nacen con "
            "esa forma: `corregir()` en la TAREA 1.a y "
            "`vuelta_del_reporte_del_arbol()` en la 1.b son puras y sus arneses las "
            "tumban sin tocar el repo."),
    "6.7": ("SE ACATA SIN TOCAR NADA. La etiqueta de VIA `NO SE CORRIO` queda "
            "adjudicada como correcta y se queda. Esta entrada la usa dos veces, en la "
            "`6.3` y en la `6.11`, que es la unica forma de acatarla que significa "
            "algo, y declara aparte que la etiqueta no alcanza para el caso de la "
            "`6.3`."),
    "6.8": ("SE ACATA SIN TOCAR NADA. El `D.6` (que el corte de una guarda pase a "
            "parametro en vez de quedar clavado) queda adjudicado como correcto. Esta "
            "vuelta no toca esa guarda y no reabre nada."),
    "6.9": ("SE ACATA SIN TOCAR NADA. El `D.7` (la segunda fila del `00_INDICE`) queda "
            "adjudicado como correcto y necesario. Esta vuelta no toca "
            "`docs/plan/00_INDICE.md` en ninguna linea."),
    "6.10": ("SE ACATA SIN TOCAR NADA. Las tres caidas propias del ejecutor de la "
             "vuelta 172 quedan adjudicadas como bien declaradas y sin mover ninguna "
             "cifra. Estan escritas con su nombre en la seccion 8 del reporte de la "
             "172, que esta vuelta acaba de cerrar y archivar en "
             "`docs/loop/reportes/REPORTE_V172.md`, y no se reabren ni se suavizan."),
    "6.11": ("NO SE CORRIO, Y SE DICE CON SU MOTIVO. La adjudicacion dice que a la "
             "TAREA 4 de la vuelta 172 solo le falta la `4.c`, que es la bateria "
             "corrida entera y sola. ESTA VUELTA NO LA CORRE, y no por descuido: el "
             "regimen del fundador del 5 sep 2026 la manda a una VUELTA DE BATERIA "
             "propia, y el encargo de hoy dice con esas palabras que la proxima es la "
             "175. La 4.a y la 4.b siguen pagadas y verificadas por el auditor (4.6 de "
             "su acta), y la nomina, RECOMPUTADA HOY por su funcion pura en el bloque "
             "H.5 de la apertura, da 82 entradas con ultima vuelta 172."),
}

QUE_HACE_CON_LA_CAIDA = {
    "CAIDA 1": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. El auditor aislo la ciega DESPUES de "
                "correr Gate 0, la vara, los cinco arneses y las verificaciones de las "
                "cuatro tareas, cuando la regla escrita en `aislador_de_ciega.py` dice "
                "que el sujeto se aisla ANTES del primer comando de verificacion, y el "
                "propio acta dice que van DOS SEGUIDAS con esta misma caida. El auditor "
                "da la consecuencia entera y acotada: ninguno de sus comandos imprimio "
                "la clase ni la razon de ningun par, y ninguno de los 17 pares que si "
                "asomaron toca ninguno de sus ocho nodos. LO QUE ESTA VUELTA SE LLEVA: "
                "una regla de ORDEN no se cumple midiendo despues si te quemaste, y por "
                "eso el bloque de apertura de hoy corrio ENTERO antes de la primera "
                "operacion en vez de despues."),
    "CAIDA 2": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. El auditor tecleo de memoria una ruta que "
                "en esta maquina no es la que python entiende y su conteo de la nomina "
                "murio a medias; rehizo por otra ruta y de ahi salio el 75 que publico, "
                "y ninguna cifra salio de la corrida rota. El propio acta dice que van "
                "TRES ACTAS SEGUIDAS con el mismo vicio de teclear en vez de mirar. ES "
                "EL VICIO QUE ESTA CAMPANA PERSIGUE, mire quien mire, y es literalmente "
                "el mismo del que sale la regla nueva del 5 sep 2026, LA RUTA QUE "
                "PROMETE PRUEBA ES CIFRA."),
}


def cuerpo_del_acta():
    """El texto del acta 172, acotado por su cabecera y por la cabecera del acta
    siguiente. NO se hereda de la maquina porque cada instrumento acota SU acta:
    lo unico propio de este fichero, con las tablas de glosas."""
    texto = io.open(ACTA, encoding="utf-8").read()
    lineas = texto.split(NL)
    inicios = [i for i, l in enumerate(lineas, 1) if l.startswith(CABECERA_ACTA)]
    if len(inicios) != 1:
        raise SystemExit("ROJO: la cabecera del acta %d aparece %d veces."
                         % (VUELTA_DEL_ACTA, len(inicios)))
    inicio = inicios[0]
    siguientes = [i for i, l in enumerate(lineas, 1)
                  if i > inicio and re.match(r"^# ACTA (DE LA VUELTA|DEL AUDITOR)", l)]
    fin = min(siguientes) - 1 if siguientes else len(lineas)
    return lineas, inicio, fin


def main():
    print("=" * 78)
    print("VUELTA %d, TAREA 2.a: EL ACTA %d ENTERA, REGISTRADA EN LA FORMA DE LA CASA"
          % (VUELTA_QUE_ESCRIBE, VUELTA_DEL_ACTA))
    print("=" * 78)
    print("")

    lineas, inicio, fin = cuerpo_del_acta()
    print("A) EL CUERPO DEL ACTA, ACOTADO ANTES DE CONTAR NADA")
    print("   acta %d: docs/loop/ACTA_AUDITOR.md, lineas %d a %d"
          % (VUELTA_DEL_ACTA, inicio, fin))
    print("   LA MAQUINA SE IMPORTA, NO SE CLONA: PAT_CAIDA, PALABRA,")
    print("   titulo_de_la_negrita, claves_de_adjudicacion y _cuenta_caidas salen de")
    print("   scripts/loop/vuelta172_tarea1_registrar_acta171.py")
    print("")

    print("B) LAS ADJUDICACIONES, CONTADAS DEL ACTA Y NO TECLEADAS")
    claves = MAQUINA.claves_de_adjudicacion(lineas, inicio, fin)
    for clave, cuantas in claves:
        if cuantas != 1:
            print("   PARADA: %s aparece %d veces." % (clave, cuantas))
            return 1
    print("   CIFRA adjudicaciones halladas: %d (%s)"
          % (len(claves), ", ".join(c for c, _ in claves)))
    if not claves:
        print("   PARADA: el acta %d no trae ninguna adjudicacion 6.n." % VUELTA_DEL_ACTA)
        return 1
    sin_glosa = [c for c, _ in claves if c not in QUE_HACE_ESTA_VUELTA or c not in VIA]
    if sin_glosa:
        print("   PARADA: sin glosa escrita en este instrumento: %s"
              % ", ".join(sin_glosa))
        return 1
    sobran = [c for c in QUE_HACE_ESTA_VUELTA if c not in [k for k, _ in claves]]
    if sobran:
        print("   PARADA: este instrumento trae glosa para adjudicaciones que el acta "
              "no tiene: %s" % ", ".join(sorted(sobran)))
        return 1
    print("   todas tienen VIA y glosa escritas: SI")
    print("   y ninguna glosa sobra: SI")
    print("")

    print("C) LAS CAIDAS PROPIAS DEL AUDITOR, CONTADAS DEL ACTA Y NO TECLEADAS")
    viejo = re.compile(r"^\s*\*\*CAIDA \d[,.]")
    n_viejo = len([i for i in range(inicio, fin + 1) if viejo.match(lineas[i - 1])])
    encontradas = [i for i in range(inicio, fin + 1) if PAT_CAIDA.match(lineas[i - 1])]
    print("   CIFRA con el patron VIEJO (el del acta 169): %d" % n_viejo)
    print("   CIFRA con el patron NUEVO (las dos formas):  %d" % len(encontradas))
    print("   (el acta 172 escribe sus caidas como vineta y con comillas inversas,")
    print("    igual que la 170 y la 171, asi que el patron heredado las ve y el")
    print("    viejo no ve ninguna. EL PATRON NO SE ENSANCHA NI UNA LETRA.)")
    if not encontradas:
        print("   PARADA: no hay ninguna caida propia que registrar.")
        return 1
    print("")

    n_adj, n_cai = len(claves), len(encontradas)
    titulo_entrada = titulo_de_la_entrada(n_adj, n_cai)
    print("D) EL TITULO DE LA ENTRADA, COMPUESTO CON LOS DOS CONTEOS")
    print("   %s" % titulo_entrada)
    print("   CIFRA adjudicaciones contadas: %d | CIFRA caidas contadas: %d"
          % (n_adj, n_cai))
    print("   CONTRASTE, Y ES CONTRASTE Y NO FUENTE: el `R.41` registro DOCE y TRES.")
    print("")

    serie = SERIE.entradas()
    print("E) LA SERIE, RECOMPUTADA DE SUS DOS SEDES ANTES DE ESCRIBIR")
    for numero, rel, linea, titulo in serie:
        print("   R.%-3d %s:%-6d %s" % (numero, rel, linea, titulo[:88]))
    cols = SERIE.colisiones(serie)
    print("   CIFRA entradas: %d" % len(serie))
    print("   CIFRA colisiones: %d" % len(cols))
    print("   CIFRA huecos: %d" % len(SERIE.huecos(serie)))
    if cols:
        print("   PARADA: la serie trae colisiones. No se escribe encima de eso.")
        return 1
    ya = [(n, rel, ln) for n, rel, ln, t in serie if titulo_entrada in t]
    if ya:
        n, rel, ln = ya[0]
        print("YA ESTABA: la entrada vive como R.%d en %s:%d. No se toca." % (n, rel, ln))
        print("CIFRA entradas escritas: 0")
        return 0
    for rel in ("docs/PENDIENTES.md", "docs/plan/CORRECCIONES_A_APLICAR.md"):
        ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.exists(ruta):
            continue
        if titulo_entrada in io.open(ruta, encoding="utf-8").read():
            print("   PARADA: el titulo YA ESTA ESCRITO en %s pero la serie no lo ve."
                  % rel)
            return 1
    numero = SERIE.siguiente_libre(serie)
    print("   SIGUIENTE LIBRE, computado y no tecleado: R.%d" % numero)
    print("")

    print("F) LA SEDE, LEIDA DE LA REGLA ESCRITA Y NO SUPUESTA")
    todas = [i for i, l in enumerate(lineas, 1) if FRASE_DE_LA_SEDE in l]
    print("   CIFRA veces que la frase de la sede aparece en el fichero entero: %d"
          % len(todas))
    if len(todas) != 1:
        print("   PARADA: la frase de la sede no aparece exactamente una vez.")
        return 1
    print("   docs/loop/ACTA_AUDITOR.md:%d dice hoy: %s"
          % (todas[0], lineas[todas[0] - 1].strip()))
    sede_rel = "docs/PENDIENTES.md"
    por_sede = {}
    for n, rel, _l, _t in serie:
        por_sede.setdefault(rel, []).append(n)
    for rel in sorted(por_sede):
        print("   CIFRA entradas en %s: %d" % (rel, len(por_sede[rel])))
    if sede_rel not in por_sede:
        print("   PARADA: la sede que manda la 6.3 no tiene ninguna entrada de la serie.")
        return 1
    print("   SEDE: %s (la que la 6.3 del acta 162 fija por defecto)" % sede_rel)
    sede = os.path.join(RAIZ, sede_rel.replace("/", os.sep))
    print("")

    print("G) LAS ADJUDICACIONES, LEIDAS HOY DE SU LINEA EN EL ACTA %d" % VUELTA_DEL_ACTA)
    adjudicaciones = []
    for clave, _c in claves:
        patron = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        hallado, error = MAQUINA.titulo_de_la_negrita(
            lineas, inicio, fin, patron, "la adjudicacion %s" % clave)
        if error:
            print("   " + error)
            return 1
        ln, titulo = hallado
        titulo = re.sub(r"^%s " % re.escape(clave), "", titulo).strip()
        adjudicaciones.append((clave, ln, titulo))
        print("   %-5s docs/loop/ACTA_AUDITOR.md:%d" % (clave, ln))
        print("      %s" % titulo[:150])
    print("   CIFRA adjudicaciones leidas: %d" % len(adjudicaciones))
    if len(adjudicaciones) != n_adj:
        print("   PARADA: se leyeron menos de las que se contaron.")
        return 1
    print("")

    print("H) LAS CAIDAS, LEIDAS HOY DE LA SECCION 3")
    caidas = []
    for ln0 in encontradas:
        m = PAT_CAIDA.match(lineas[ln0 - 1])
        clave = "CAIDA %s" % m.group(1)
        patron = re.compile(r"^\s*(?:-\s+)?\*\*`?%s`?[,.]" % re.escape(clave))
        hallado, error = MAQUINA.titulo_de_la_negrita(
            lineas, inicio, fin, patron, "la %s" % clave)
        if error:
            print("   " + error)
            return 1
        ln, titulo = hallado
        if clave not in QUE_HACE_CON_LA_CAIDA:
            print("   PARADA: %s no tiene glosa escrita en este instrumento." % clave)
            return 1
        caidas.append((clave, ln, titulo))
        print("   %-8s docs/loop/ACTA_AUDITOR.md:%d" % (clave, ln))
        print("      %s" % titulo[:150])
    print("   CIFRA caidas leidas: %d" % len(caidas))
    print("")

    print("I) EL REPARTO POR VIA, CONTADO Y NO TECLEADO")
    reparto = {}
    for clave, _ln, _t in adjudicaciones:
        reparto.setdefault(VIA[clave], []).append(clave)
    for via in sorted(reparto):
        print("   CIFRA %s: %d (%s)" % (via, len(reparto[via]), ", ".join(reparto[via])))
    print("")

    bloques = []
    for clave, ln, titulo in adjudicaciones:
        bloques.append(
            "  - **%s (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). VIA: %s.** Titulo\n"
            "    literal del acta: *\"%s\"*\n"
            "    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s\n"
            % (clave, ln, VIA[clave], titulo, QUE_HACE_ESTA_VUELTA[clave]))

    bloques_caidas = []
    for clave, ln, titulo in caidas:
        bloques_caidas.append(
            "  - **%s (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy).** Titulo literal del\n"
            "    acta: *\"%s\"*\n"
            "    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s\n"
            % (clave, ln, titulo, QUE_HACE_CON_LA_CAIDA[clave]))

    linea_reparto = "; ".join(
        "%s: %d (%s)" % (via, len(reparto[via]), ", ".join(reparto[via]))
        for via in sorted(reparto))

    palabra_caidas = ("LA CAIDA PROPIA DEL AUDITOR, REGISTRADA"
                      if n_cai == 1 else
                      "LAS %s CAIDAS PROPIAS DEL AUDITOR, REGISTRADAS"
                      % PALABRA[n_cai].upper())

    trozos = []
    trozos.append(
        "\n---\n\n## R.%d. %s\n\n"
        "(Acta del auditor, vuelta %d, secciones 3 y 6; escrito en la vuelta %d,\n"
        "TAREA 2.a.)\n\n"
        "Por adicion, como `R.21` a `R.41`. **Corte de todas las cifras de esta entrada:\n"
        "5 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa\n"
        "`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.\n"
        "La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, leida hoy\n"
        "en `docs/loop/ACTA_AUDITOR.md:%d`. Salida:\n"
        "`docs/loop/SALIDA_V%d_T2A_REGISTRO_ACTA_%d.txt`.\n\n"
        % (numero, titulo_entrada, VUELTA_DEL_ACTA, VUELTA_QUE_ESCRIBE,
           todas[0], VUELTA_QUE_ESCRIBE, VUELTA_DEL_ACTA))
    trozos.append(
        "> **ESTA ENTRADA SE ESCRIBE LA PENULTIMA DE LA VUELTA, CON LA TAREA 1 ENTERA YA\n"
        "> CERRADA Y MEDIDA, Y POR ESO SUS GLOSAS SI AFIRMAN EN PASADO.** Es la\n"
        "> diferencia de fondo con el `R.41`, y no es un capricho de forma: el `R.41` se\n"
        "> escribio **la primera** de su vuelta, cuando ninguna tarea habia corrido, asi\n"
        "> que su campo se llamaba **VIA PREVISTA** y sus glosas decian *\"VA A\n"
        "> EJECUTARSE ... Y TODAVIA NO HA CORRIDO\"*. La `6.4` del acta 172 adjudico esa\n"
        "> forma como correcta y **probada por la realidad**, porque la vuelta 172 se\n"
        "> corto de verdad antes de su anexion y la entrada siguio siendo cierta.\n"
        "> \n"
        "> **AQUI EL CAMPO SE LLAMA `VIA` A SECAS Y CADA GLOSA LLEVA AL LADO LA LINEA O\n"
        "> LA SALIDA QUE LA MIDE**, que es `EJECUTOR.md` 1 al pie de la letra: *\"toda\n"
        "> afirmacion sobre el estado del registro se escribe CON LA MEDICION DEL DIA AL\n"
        "> LADO; si no hay linea que citar, la afirmacion no se escribe\"*. **Y por eso\n"
        "> esta entrada NO necesita ningun fichero de confirmacion posterior**: no hay\n"
        "> nada que confirmar despues, porque nada se afirmo antes de tiempo. **La que\n"
        "> si lo necesitaba era el `R.41`, y ese fichero nace en la TAREA 2.b de esta\n"
        "> misma vuelta.**\n\n")
    trozos.append(
        "**Y LAS DOS CIFRAS DEL TITULO TAMPOCO ESTAN TECLEADAS:** se cuentan del acta\n"
        "(%d adjudicaciones `6.n` y %d negritas `CAIDA n` dentro del cuerpo acotado,\n"
        "lineas %d a %d) y de ahi sale el numeral en palabra, **incluida la\n"
        "concordancia**. **EL `R.41` REGISTRO DOCE Y TRES; ESTE REGISTRA %d Y %d.**\n\n"
        "**Y EL PATRON DE CAIDA TAMPOCO SE TOCA ESTA VEZ.** El acta 172 usa la MISMA\n"
        "forma de vineta con comillas inversas que la 170 y la 171, asi que el patron se\n"
        "hereda TAL CUAL, sin ensancharlo ni una letra, y ademas **se importa** de\n"
        "`scripts/loop/vuelta172_tarea1_registrar_acta171.py` en vez de copiarse. Las dos\n"
        "cifras se siguen publicando al lado para que se vea que no se afloja: el patron\n"
        "VIEJO, el de la vuelta 170, corrido sobre el acta 172, cuenta **%d**; el\n"
        "heredado cuenta **%d**.\n\n"
        % (n_adj, n_cai, inicio, fin, n_adj, n_cai, n_viejo, n_cai))
    trozos.append(
        "**LA MAQUINA NO SE CLONA, SE IMPORTA, Y ESO ES LO UNICO NUEVO DE ESTE\n"
        "INSTRUMENTO.** Los dos registradores anteriores copiaban el mecanismo entero\n"
        "cada vuelta. `PAT_CAIDA`, `PALABRA`, `titulo_de_la_negrita`,\n"
        "`claves_de_adjudicacion` y `_cuenta_caidas` se importan aqui de su ultima sede,\n"
        "que es la que la bateria ya vigila con `vuelta172_tarea1b_mutacion_registro.py`.\n"
        "**Lo unico propio de este fichero es el acote de SU acta y sus tablas de\n"
        "glosas.** Es la regla de la casa sobre fuentes unicas, la misma que la `6.6` de\n"
        "esta acta adjudica como correcta y obligatoria.\n\n")
    trozos.append(
        "**LAS %s ADJUDICACIONES, CON SU LINEA EN EL ACTA LEIDA HOY.** El titulo de\n"
        "cada una es LITERAL del fichero (localizado dentro del cuerpo del acta %d, no\n"
        "de cualquier acta); la glosa que sigue es prosa del ejecutor y va marcada como\n"
        "tal.\n\n%s\n"
        % (PALABRA[n_adj].upper(), VUELTA_DEL_ACTA, "".join(bloques)))
    trozos.append(
        "**EL REPARTO POR VIA, CONTADO Y NO TECLEADO:** %s.\n"
        "**Ninguna de las %s sube al fundador.**\n\n"
        "**Y UNA ETIQUETA QUE NO ALCANZA, DECLARADA EN VEZ DE INVENTADA.** La `6.3` no\n"
        "es un descuido: **una decision posterior del fundador la dejo sin objeto**, y\n"
        "ninguna de las tres etiquetas escritas (`EJECUTADA`, `SIN TOCAR NADA`,\n"
        "`NO SE CORRIO`) dice *\"superada por decision del fundador\"*. Se usa la mas\n"
        "cercana, `NO SE CORRIO`, la glosa dice el motivo entero con su cita, y **el\n"
        "hueco queda como PENDIENTE DE DOCTRINA en el reporte de la vuelta 174 en vez de\n"
        "rellenarse con una etiqueta estrenada por la mano del ejecutor** (`EJECUTOR.md`\n"
        "5).\n\n"
        % (linea_reparto, PALABRA[n_adj]))
    trozos.append(
        "**%s IGUAL QUE LAS DEL EJECUTOR**\n"
        "(precedente del `R.36`, escrito en la vuelta 167 por letra de su encargo, y\n"
        "heredado aqui sin reabrirlo). No son del ejecutor y no acumulan para sus\n"
        "rachas; se escriben aqui porque el registro de la casa no distingue de quien es\n"
        "la mano que cae. En el acta %d viven en la **seccion 3**.\n\n%s\n"
        % (palabra_caidas, VUELTA_DEL_ACTA, "".join(bloques_caidas)))
    trozos.append(
        "**LO QUE ESTE REGISTRO NO CIERRA, Y SE DICE ANTES DE QUE NADIE LO SUPONGA.**\n"
        "La vara `P.5.1` sigue CONGELADA y ninguna de estas %s la estrecha ni la\n"
        "ensancha. **Ninguna clase del cribado se mueve por esta entrada** y\n"
        "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no se toca. **Ningun `estado` de\n"
        "`docs/plan/OPERACIONES.jsonl` se mueve por esta entrada**: el campo sigue\n"
        "jubilado como historico y la vara del trabajo pendiente sigue siendo\n"
        "`scripts/loop/vuelta150_3_relectura_expediente.py`. **Y las dos `OP-M-02`\n"
        "siguen sin ejecutarse**, por la `6.6` del acta 168. **`OP-L-03` queda abierta y\n"
        "leida y NO se ejecuta en esta vuelta**, y esta vez no por ningun tope sino\n"
        "porque el encargo de la 174 la aplaza EXPRESAMENTE a la 175, detras de la\n"
        "recuperacion del cierre del reporte. **Y la bateria tampoco corre aqui**: por\n"
        "el regimen del fundador del 5 sep 2026 corre cada cinco vueltas, en vuelta\n"
        "propia, y la proxima es la 175.\n"
        % PALABRA[n_adj])
    texto = "".join(trozos)

    for malo, nombre in ((chr(8212), "guion largo"), (chr(8211), "guion medio")):
        if malo in texto:
            print("   PARADA: el texto que se iba a escribir trae un %s." % nombre)
            return 1

    with io.open(sede, "a", encoding="utf-8", newline=NL) as fh:
        fh.write(texto)
    print("J) ESCRITO")
    print("   R.%d en %s" % (numero, sede_rel))
    print("   CIFRA adjudicaciones escritas: %d" % len(adjudicaciones))
    print("   CIFRA caidas escritas: %d" % len(caidas))
    print("   CIFRA entradas escritas: 1")
    print("   CIFRA bytes anexados: %d" % len(texto.encode("utf-8")))
    print("")

    serie2 = SERIE.entradas()
    ve = [(n, rel, ln) for n, rel, ln, t in serie2 if titulo_entrada in t]
    print("K) LA SERIE, RECOMPUTADA DESPUES DE ESCRIBIR")
    print("   CIFRA entradas: %d" % len(serie2))
    print("   CIFRA colisiones: %d" % len(SERIE.colisiones(serie2)))
    print("   CIFRA huecos: %d" % len(SERIE.huecos(serie2)))
    print("   la serie VE la entrada nueva: %s"
          % ("SI, R.%d en %s:%d" % ve[0] if ve else "NO"))
    if not ve:
        print("   PARADA: escrita pero invisible para la serie. Revisar la cabecera.")
        return 1
    print("")
    print("VERDE: el acta %d queda registrada como R.%d." % (VUELTA_DEL_ACTA, numero))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
