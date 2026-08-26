# -*- coding: utf-8 -*-
"""vuelta68_registrar_acta67.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DE LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 67, CON LA GUARDA DE CITAS
ENSANCHADA.

NO REESCRIBE NI UNA LINEA DE LAS SECCIONES DE ARRIBA: abre el fichero en modo
adosar y escribe detras. Es la via que esta pagina ya uso OCHO veces (acta 52 en
la linea 1250, acta 57 sobre el acto 25 en la 2475, acta 61 en la 2689, acta 62
en la 2933, acta 63 en la 3307, acta 64 en la 3613, acta 65 en la 3962 y acta 66
en la 4478).

EL ENSANCHE DE LA GUARDA DE CITAS (26 ago 2026, TAREA 1.c del encargo de la
vuelta 68; motivo: la caida de cifra publicada de la vuelta 67, acta 67 seccion
3). EL TEXTO VIEJO DE LA GUARDA, VERBATIM Y SIN TACHAR, tal como lo llevaba
scripts/loop/vuelta67_registrar_acta66.py:

    LA GUARDA DE CITAS, heredada del registrador de la vuelta 66: ANTES de
    escribir, cada cita de linea se coteja contra su fichero imprimiendo la
    linea citada; si una sola no calza con la aguja que la tabla dice de ella,
    el instrumento cae en ROJO y NO escribe nada. Aqui se cotejan citas de DOS
    ficheros, el acta y la propia pagina de fusiones.

POR QUE NO ALCANZABA, medido: esa guarda cotejaba las citas de UNA LISTA, no
las citas del TEXTO. La vuelta 67 tenia la linea 4055 en su lista con la aguja
LOS PENDIENTES 2 Y 4 (y ahi esta, la guarda dijo OK), pero su PROSA uso ese
mismo numero para una afirmacion distinta (que ahi vivia la frase envejecida
cuya linea base sigue en 2, que vive en las lineas 4073 a 4075). Una guarda que
no mira el texto deja pasar exactamente esa especie.

LAS DOS CONDICIONES QUE ESTE ENSANCHE ANADE, ENUMERADAS (acta 61, D2 y pregunta
2; van ademas MARCADAS DISCUTIBLES en el reporte de la vuelta 68):

  1. LAS CITAS DE LINEA DEL TEXTO SE DERIVAN POR AGUJA, NO SE TECLEAN. El texto
     no lleva ningun numero de linea escrito a mano: lleva marcas [[CLAVE]], y
     cada CLAVE es un par (fichero, aguja). El instrumento BUSCA la aguja en el
     fichero, exige que aparezca EXACTAMENTE UNA VEZ (si no, ROJO y cero
     escrituras) y sustituye la marca por el numero que la busqueda devuelve.
     Asi la cita queda atada al CONTENIDO que afirma, y no a un numero suelto.
  2. TODA CITA DE LA FORMA linea NNNN PRESENTE EN EL TEXTO NUEVO SE COTEJA
     CONTRA EL CONTENIDO DE ESA LINEA ANTES DE ESCRIBIR. Ya sustituidas las
     marcas, el instrumento vuelve a barrer el texto FINAL buscando la forma
     canonica (linea con el numero en negrita, y lineas NNNN a MMMM) y exige
     que CADA numero hallado salga de una CLAVE derivada; un numero que no
     salga de una aguja es ROJO y cero escrituras. Se exige tambien que toda
     CLAVE derivada se use al menos una vez, para que la lista no crie citas
     muertas.

Y UNA TERCERA COMPROBACION, LAS AGUJAS NEGATIVAS, que es la que prueba la
correccion de esta vuelta: una lista de pares (CLAVE, aguja que esa linea NO
debe contener). La correccion declarada afirma que la frase envejecida NO vive
en la linea de la cabecera del apartado e); esa afirmacion se MIDE aqui en vez
de creerse.

EL TEXTO VIEJO QUE SE CORRIGE NO SE TECLEA TAMPOCO: la marca
[[VERBATIM:CLAVE:N]] copia N lineas del fichero a partir de la linea derivada,
prefijadas como cita en bloque. Asi la correccion declarada del banco 9.10 cita
el texto viejo AL BYTE y no de memoria.

EL BLOQUE VERBATIM DUPLICA UNA AGUJA A PROPOSITO, y por eso el re-cotejo de
despues se corre SOBRE LAS LINEAS DE ARRIBA SOLAS: al copiar el texto viejo
dentro de la seccion nueva, la aguja de ese texto pasa a aparecer dos veces en
la pagina. Eso no es una sede movida, es la cita; medir el re-cotejo sobre la
pagina entera lo leeria como fallo.

LA GUARDA DE IDEMPOTENCIA: si la seccion ya esta en la pagina, no se escribe
nada. Una pagina con la adjudicacion duplicada no falla, dice que si.

Uso:
  python scripts/loop/vuelta68_registrar_acta67.py [--simular]
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:67 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 67 DEL AUDITOR" corte=2026-08-26 motivo="el titulo nombra el ACTA que este registro transcribe, que es de la vuelta 67; el fichero es de la vuelta 68 y por eso el numero no calza con su propia vuelta a proposito"
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
NL = chr(10)

# CLAVE -> (fichero, aguja). La aguja es el CONTENIDO que la cita afirma; el
# numero de linea sale de buscarla, nunca de teclearla.
AGUJAS = {
    # --- docs/loop/ACTA_AUDITOR.md, acta de la vuelta 67 ---
    "A67_ABRE": (ACTA, "# ACTA DE LA VUELTA 67 DEL AUDITOR (26 ago 2026, Fable 5)"),
    "A67_VERIF": (ACTA, "## 1. VERIFICACION POR CORRIDA PROPIA: TODO AL DIGITO SALVO UNA CITA,"),
    "A67_CIEGA": (ACTA, "## 2. RELECTURA CIEGA"),
    "A67_NOTA1030": (ACTA, "- UNA NOTA DE DICTADO SIN CAIDA: el reporte dice que el puesto 1030"),
    "A67_CAIDAS": (ACTA, "## 3. CAIDAS DE ESTA TANDA: UNA DE CIFRA PUBLICADA DEL EJECUTOR, FUERA"),
    "A67_CAIDA_MEDICION": (ACTA, "- LA CAIDA, CON SU MEDICION: el registro del acta 66 en"),
    "A67_GUARDA_NO_CAZO": (ACTA, "- POR QUE LA GUARDA NO LA CAZO: la guarda de citas del registrador"),
    "A67_SUSTANCIA": (ACTA, "- LA SUSTANCIA NO CAE: la declaracion de ENVEJECIDA es correcta (la"),
    "A67_EFECTO_CREDITO": (ACTA, "- EFECTO EN EL CREDITO: la relectura al doble se ejecuto (seccion 2,"),
    "A67_REPORTE_CERO": (ACTA, "- REPORTE: CERO caidas de la especie reporte (la afirmacion equivocada"),
    "A67_QUINCE": (ACTA, "## 4. ADJUDICACION DE LOS QUINCE DISCUTIBLES"),
    "A67_D1": (ACTA, "- D1, DECLARAR EL ACTO 12 POR UN D DIRECTO SIN TRIANGULO, CON MOTIVO"),
    "A67_D2": (ACTA, "- D2, DECLARAR EL ACTO 14 POR P.5 CUANDO EL QUINTO TIENE UNA A CON UN"),
    "A67_D3": (ACTA, "- D3, ESTRENAR LA GUARDA 1B COMO MOTIVO UNICO EN DOS ACTOS EL MISMO DIA:"),
    "A67_D4": (ACTA, "- D4, EN EL ACTO 15 LAS TRES VARAS APUNTAN A UNA PUERTA Y AUN ASI"),
    "A67_D5": (ACTA, "- D5, UNA SOLA FUSION SOBRE SEIS ACTOS: A FAVOR. El contrato es prefijo"),
    "A67_D6": (ACTA, "- D6, DECLARAR SEIS TENIENDO CINCO DECLARADOS BARATOS: A FAVOR. El lote"),
    "A67_D7": (ACTA, "- D7, EL SUPERVIVIENTE DEL ACTO 16 CONTRA EL CABLEADO 8 A 3: A FAVOR."),
    "A67_D8": (ACTA, "- D8, CINCO APPEND Y EL NODO DUPLICA SU TAMANO: A FAVOR, carril del D9"),
    "A67_D9": (ACTA, "- D9, LOS DOS APPEND QUE SE SOLAPAN (BRUJULA Y TITULAR): A FAVOR. El"),
    "A67_D10": (ACTA, "- D10, UNA PERDIDA CON DOS SITIOS EN UN SOLO CAMPO donde: A FAVOR, y el"),
    "A67_D11": (ACTA, "- D11, TRES PERDIDAS CON ATENUANTE DECLARADO: A FAVOR, carril del D8 del"),
    "A67_D12": (ACTA, "- D12, CORREGIR EL DEFECTO DE --base SIN ENCARGO: A FAVOR. Un"),
    "A67_D13": (ACTA, "- D13, RE-CODIFICAR DOS SALIDAS EN VEZ DE RE-CORRER: A FAVOR. Verificado"),
    "A67_D14": (ACTA, "- D14, NO CONTESTAR LA PREGUNTA DE P.5 EN EL ACTO 15: A FAVOR con la"),
    "A67_D15": (ACTA, "- D15, ENSANCHAR LA AGUJA DEL COMPROBADOR Y CORREGIR SU ROTULO SIN"),
    "A67_PEND": (ACTA, "## 5. LOS PENDIENTES DE DOCTRINA, ADJUDICADOS O NOMBRADOS"),
    "A67_P1": (ACTA, "1. QUE HACE UN ACTO CON UN VEREDICTO D DIRECTO INTERNO Y SIN TRIANGULO:"),
    "A67_P1_LISTA_NO_CERRADA": (ACTA, "   del ejecutor se contesta primero: LA LISTA DE TRES MOTIVOS SELLABLES"),
    "A67_P1_PRIMERA": (ACTA, "   DESMENTIRIA. Las letras: PRIMERA, P.12 parte 2 manda que con el acto"),
    "A67_P1_SEGUNDA": (ACTA, "   entre si, que es lo que esa lectura niega. SEGUNDA, la ultima linea"),
    "A67_P1_TERCERA": (ACTA, "   TERCERA, las tres salidas de P.10 estan cerradas por letra vigente:"),
    "A67_P1_CUARTA": (ACTA, "   ademas la fusion parcial la prohibe el encargo. CUARTA, el precedente"),
    "A67_P1_CATALOGO": (ACTA, "   sellado, y el catalogo de motivos queda en CUATRO: el triangulo de"),
    "A67_P2": (ACTA, "2. QUE DESTINO TIENE UN ACTO CUYA FORMA ES EMPATE SIN VARA: ADJUDICADO,"),
    "A67_P2_NI_NI": (ACTA, "   estado mientras tanto, y queda asi: EL ACTO NI SE DECLARA NI DETIENE"),
    "A67_P2_CASO": (ACTA, "   superviviente: escribe el caso entero en el reporte (la respuesta de"),
    "A67_P2_TRANSITO": (ACTA, "   acto queda ABIERTO EN TRANSITO dentro del tramo, fuera de la cuenta"),
    "A67_P2_RESERVADO": (ACTA, "   adjudicada como su primera operacion. DECLARADO Y NO FUNDIDO queda"),
    "A67_P3": (ACTA, "3. EL SUBCONJUNTO CERRADO DE UN ACTO CON PUENTE (heredado): sigue"),
    "A67_P4": (ACTA, "4. LA MARCA PARA YA LO DICE EL APPEND DE UN HERMANO (heredado): sigue"),
    "A67_P5": (ACTA, "5. EL INCISO DE CONDICIONES (heredado): sigue en su carril, cinco piezas"),
    "A67_P6": (ACTA, "6. EL ESQUEMA DE OPERACIONES.jsonl (heredado): sigue pendiente; esta"),
    "A67_METRICA": (ACTA, "## 6. METRICA DE CREDITO ACUMULADA"),
    "A67_ACUMULADO": (ACTA, "Acumulado: 463 relecturas, 786 puestos (mas unos 539 nodos de forma y"),
    "A67_RACHAS": (ACTA, "Rachas: REPORTE EN CERO (tercera tanda seguida). CLASE O CIFRA: ROTA en"),
    "A67_PARADAS": (ACTA, "## 7. CONDICIONES DE PARADA, RECORRIDAS: NINGUNA SE CUMPLE"),
    # --- docs/plan/03_FUSIONES.md, sedes de esta misma pagina ---
    "PAG_FICHA_ENVEJECIDA": (PAGINA, "### b) **LA REGLA DE LA FICHA ENVEJECIDA**"),
    "PAG_CARRIL_COLISIONES": (PAGINA, "### b) **EL CARRIL DE LAS DOS COLISIONES DE CLASE VIGENTES"),
    "PAG_ACTO1_P10": (PAGINA, "### a) **EL ACTO 1: `DECLARADO Y NO FUNDIDO` POR `P.10`"),
    "PAG_GUARDA_1B": (PAGINA, "### c) **UN ACTO CON DOS O MAS PUERTAS CIERRA `DECLARADO Y NO FUNDIDO`"),
    "PAG_ACTA65": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 65, REGISTRADAS AQUI"),
    "PAG_E_ACTA65": (PAGINA, "### e) **LOS PENDIENTES 2 Y 4, NOMBRADOS CON SU DESTINO: EL CIERRE DE LA FASE 03**"),
    "PAG_FRASE_1": (PAGINA, "**NO toca ni una cifra publicada arriba, NO elige ningun superviviente, NO funde nada, NO deshace"),
    "PAG_FRASE_2": (PAGINA, "ninguna fusion y NO re-lee ni un veredicto de las dos colisiones vigentes**, cuya **linea base sigue"),
    "PAG_FRASE_3": (PAGINA, "en `2`** y cuya duena sigue siendo la mesa `OP-M-03`. Registra adjudicaciones."),
    "PAG_ACTA66": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 66, REGISTRADAS AQUI"),
    "PAG_P5_MOTIVO": (PAGINA, "### b) **UN ACTO CUYO `P.5` CONTESTA QUE NO ES UNA FAMILIA CIERRA"),
    "PAG_CITA_MALA": (PAGINA, "no predicho es PARADA de guarda**. La frase de la linea"),
    "PAG_LOTE_C": (PAGINA, "## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE C`"),
    "PAG_ACTO12": (PAGINA, "### b) **EL `ACTO 12`: `DECLARADO Y NO FUNDIDO` POR ALGO QUE NINGUNA LETRA CUBRE"),
    "PAG_ACTO13_15": (PAGINA, "### c) **LOS `ACTOS 13` Y `15`: LAS DOS PRIMERAS VECES DE LA CAMPANA"),
    "PAG_ACTO14": (PAGINA, "### d) **EL `ACTO 14`: `DECLARADO Y NO FUNDIDO` POR `P.5`, Y ES EL SEGUNDO USO"),
    "PAG_ACTO17": (PAGINA, "### e) **EL `ACTO 17`: `DECLARADO Y NO FUNDIDO` POR `P.10`, CON SU TRIANGULO MEDIDO"),
}

# ANCLAS: hay agujas que NO son unicas en todo el fichero porque el acta y la
# pagina repiten cabeceras de seccion vuelta tras vuelta (RELECTURA CIEGA,
# METRICA DE CREDITO ACUMULADA, LO QUE ESTA SECCION NO HACE). Para esas, la
# busqueda se restringe a una VENTANA que arranca en otra clave ya derivada, y
# se sigue exigiendo UNA sola ocurrencia DENTRO de la ventana.
# CLAVE -> (clave ancla, ventana en lineas).
ANCLAS = dict(
    [(c, ("A67_ABRE", 600)) for c in
     ("A67_VERIF", "A67_CIEGA", "A67_NOTA1030", "A67_CAIDAS", "A67_CAIDA_MEDICION",
      "A67_GUARDA_NO_CAZO", "A67_SUSTANCIA", "A67_EFECTO_CREDITO", "A67_REPORTE_CERO",
      "A67_QUINCE", "A67_D1", "A67_D2", "A67_D3", "A67_D4", "A67_D5", "A67_D6",
      "A67_D7", "A67_D8", "A67_D9", "A67_D10", "A67_D11", "A67_D12", "A67_D13",
      "A67_D14", "A67_D15", "A67_PEND", "A67_P1", "A67_P1_LISTA_NO_CERRADA",
      "A67_P1_PRIMERA", "A67_P1_SEGUNDA", "A67_P1_TERCERA", "A67_P1_CUARTA",
      "A67_P1_CATALOGO", "A67_P2", "A67_P2_NI_NI", "A67_P2_CASO", "A67_P2_TRANSITO",
      "A67_P2_RESERVADO", "A67_P3", "A67_P4", "A67_P5", "A67_P6", "A67_METRICA",
      "A67_ACUMULADO", "A67_RACHAS", "A67_PARADAS")]
    + [("PAG_FRASE_1", ("PAG_E_ACTA65", 40))]
)

# NUMEROS QUE EL TEXTO ESCRIBE EN NEGRITA Y NO SON CITAS DE LINEA, declarados
# uno a uno con su motivo. Todo lo demas que aparezca en negrita con 3 a 5
# digitos tiene que salir de una aguja, o es ROJO.
NUMEROS_DECLARADOS = {
    "1374": "el puesto del veredicto D directo del acto 12",
    "1030": "el puesto del puro de cuatro del acto 14",
    "1319": "el puesto que llama al titular su unico gesto propio",
}

# (CLAVE, aguja que esa linea NO debe contener). La afirmacion negativa de la
# correccion declarada se MIDE, no se cree.
NEGATIVAS = [
    ("PAG_E_ACTA65", "linea base sigue"),
    ("PAG_E_ACTA65", "cuya **linea base sigue en `2`**"),
]

RE_MARCA = re.compile(r"\[\[([A-Z0-9_]+)\]\]")
RE_VERBATIM = re.compile(r"\[\[VERBATIM:([A-Z0-9_]+):(\d+)\]\]")
# LA FORMA CANONICA DE UNA CITA DE LINEA EN EL TEXTO. Todo numero que aparezca
# asi tiene que salir de una aguja.
RE_CITA = re.compile(r"l[ií]neas?\s+\*\*(\d+)\*\*(?:\s+a\s+\*\*(\d+)\*\*)?")
# Y LA RED MAS ANCHA: TODO numero de 3 a 5 digitos que el texto ponga en
# negrita. En las tablas la cita de linea va sola en su celda, sin la palabra
# linea delante, y sin esta segunda red esas celdas quedarian fuera del cotejo.
RE_NEGRITA = re.compile(r"\*\*(\d{3,5})\*\*")

_CACHE = {}


def lineas_de(ruta):
    if ruta not in _CACHE:
        _CACHE[ruta] = io.open(ruta, encoding="utf-8").read().split(NL)
    return _CACHE[ruta]


def derivar(fallos, callado=False):
    """CONDICION 1: cada cita sale de buscar su aguja, y la aguja tiene que ser
    UNICA en su fichero. Devuelve {CLAVE: (numero, ruta, aguja)}."""
    if not callado:
        print()
        print("  --- GUARDA DE CITAS, CONDICION 1: LAS CITAS SE DERIVAN POR AGUJA ---")
    derivadas = {}
    # las claves sin ancla primero: una clave anclada necesita su ancla derivada.
    orden = ([c for c in sorted(AGUJAS) if c not in ANCLAS]
             + [c for c in sorted(AGUJAS) if c in ANCLAS])
    for clave in orden:
        ruta, aguja = AGUJAS[clave]
        lineas = lineas_de(ruta)
        desde, hasta, etq_ventana = 0, len(lineas), "todo el fichero"
        if clave in ANCLAS:
            ancla, ventana = ANCLAS[clave]
            if ancla not in derivadas:
                fallos.append("la clave %s se ancla en %s y %s no se pudo derivar"
                              % (clave, ancla, ancla))
                continue
            desde = derivadas[ancla][0] - 1
            hasta = min(len(lineas), desde + ventana)
            etq_ventana = "ventana %d..%d" % (desde + 1, hasta)
        hallazgos = [i + 1 for i in range(desde, hasta) if aguja in lineas[i]]
        if len(hallazgos) != 1:
            fallos.append("la aguja de %s aparece %d veces en %s (%s; tiene que aparecer 1)"
                          % (clave, len(hallazgos), os.path.basename(ruta), etq_ventana))
            if not callado:
                print("     %-24s ROJO  %d hallazgos en %s" % (clave, len(hallazgos), etq_ventana))
            continue
        n = hallazgos[0]
        derivadas[clave] = (n, ruta, aguja)
        if not callado:
            print("     %-24s %-6d %s" % (clave, n, lineas[n - 1].strip()[:78]))
    return derivadas


def negativas(derivadas, fallos):
    """LAS AGUJAS NEGATIVAS: lo que una linea NO debe decir, medido."""
    print()
    print("  --- GUARDA DE CITAS, AGUJAS NEGATIVAS ---")
    for clave, aguja in NEGATIVAS:
        if clave not in derivadas:
            continue
        n, ruta, _ = derivadas[clave]
        real = lineas_de(ruta)[n - 1]
        if aguja in real:
            fallos.append("la linea %d (%s) SI contiene %r y no deberia" % (n, clave, aguja))
            print("     %-22s ROJO  la linea %d contiene %r" % (clave, n, aguja))
        else:
            print("     %-22s OK    la linea %d NO contiene %r" % (clave, n, aguja[:44]))


def sustituir(texto, derivadas, fallos, usos):
    """Sustituye [[VERBATIM:CLAVE:N]] y [[CLAVE]] por lo medido, contando cuantas
    veces se usa cada clave (una clave con cero usos es una cita muerta)."""
    def rep_verbatim(m):
        clave, cuantas = m.group(1), int(m.group(2))
        if clave not in derivadas:
            fallos.append("VERBATIM sobre clave no derivada: %s" % clave)
            return m.group(0)
        n, ruta, _ = derivadas[clave]
        usos[clave] = usos.get(clave, 0) + 1
        crudas = lineas_de(ruta)[n - 1:n - 1 + cuantas]
        return NL.join("> " + c for c in crudas)

    texto = RE_VERBATIM.sub(rep_verbatim, texto)

    def rep(m):
        clave = m.group(1)
        if clave not in derivadas:
            fallos.append("marca sin aguja derivada: %s" % clave)
            return m.group(0)
        usos[clave] = usos.get(clave, 0) + 1
        return str(derivadas[clave][0])

    return RE_MARCA.sub(rep, texto)


def cotejar_texto(texto, derivadas, fallos, usos):
    """CONDICION 2: toda cita de la forma linea NNNN del texto FINAL sale de una
    aguja derivada, y toda aguja derivada se usa al menos una vez."""
    print()
    print("  --- GUARDA DE CITAS, CONDICION 2: EL TEXTO NUEVO, COTEJADO ---")
    numeros = {}
    for clave, (n, ruta, aguja) in derivadas.items():
        numeros.setdefault(n, []).append((clave, ruta, aguja))
    halladas = []
    for m in RE_CITA.finditer(texto):
        for g in m.groups():
            if g:
                halladas.append(int(g))
    usadas = set()
    malas = 0
    for n in sorted(set(halladas)):
        if n not in numeros:
            fallos.append("el texto cita la linea %d y ese numero NO sale de ninguna aguja" % n)
            print("     linea %-6d ROJO  no sale de ninguna aguja" % n)
            malas += 1
            continue
        usadas.add(n)
        clave, ruta, aguja = numeros[n][0]
        real = lineas_de(ruta)[n - 1]
        ok = aguja in real
        if not ok:
            fallos.append("el texto cita la linea %d y su contenido no calza con la aguja" % n)
            malas += 1
        print("     linea %-6d %-4s %-24s %s"
              % (n, "OK" if ok else "MAL", clave, real.strip()[:58]))
    print()
    print("     citas de linea en forma canonica: %d distintas | MALAS: %d"
          % (len(set(halladas)), malas))

    # LA RED ANCHA: todo numero en negrita de 3 a 5 digitos.
    negritas = sorted(set(int(m.group(1)) for m in RE_NEGRITA.finditer(texto)))
    fuera = []
    for n in negritas:
        if n in numeros:
            usadas.add(n)
            continue
        if str(n) in NUMEROS_DECLARADOS:
            continue
        fuera.append(n)
    if fuera:
        for n in fuera:
            fallos.append("el texto escribe **%d** en negrita y ni sale de una aguja "
                          "ni esta en NUMEROS_DECLARADOS" % n)
        print("     ROJO: numeros en negrita sin aguja ni declaracion: %s"
              % ", ".join(str(n) for n in fuera))
    else:
        print("     numeros en negrita de 3 a 5 digitos: %d, TODOS con aguja o declarados "
              "(%s)" % (len(negritas), ", ".join(sorted(NUMEROS_DECLARADOS))))

    # NINGUNA CITA MUERTA: toda clave derivada se usa al menos una vez.
    sin_usar = sorted(c for c in derivadas if usos.get(c, 0) == 0)
    if sin_usar:
        fallos.append("hay %d aguja(s) derivada(s) que el texto no usa: %s"
                      % (len(sin_usar), ", ".join(sin_usar)))
        print("     ROJO: agujas derivadas sin usar: %s" % ", ".join(sin_usar))
    else:
        print("     todas las %d agujas derivadas se usan al menos una vez: OK"
              % len(derivadas))


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v68_texto_acta67 import TEXTO  # noqa: E402

MARCA_IDEMPOTENCIA = "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 67"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 67 AL FINAL DE 03_FUSIONES.md")
    print("Con la guarda de citas ENSANCHADA (las dos condiciones del acta 61).")
    print("=" * 78)

    # LA IDEMPOTENCIA SE MIRA PRIMERO, y no despues de derivar: el bloque
    # VERBATIM copia texto de arriba, asi que en una SEGUNDA corrida la aguja de
    # ese texto ya aparece dos veces y la derivacion caeria en ROJO antes de
    # llegar a decir YA ADOSADA. Rojo tambien es seguro (no escribe), pero la
    # respuesta correcta a una pagina ya registrada es decirlo, no fallar.
    crudo = io.open(PAGINA, encoding="utf-8").read()
    if MARCA_IDEMPOTENCIA in crudo:
        print()
        print("YA ADOSADA: la seccion del acta 67 ya esta en la pagina. No se escribe nada.")
        return 0

    fallos = []
    derivadas = derivar(fallos)
    negativas(derivadas, fallos)
    usos = {}
    texto = sustituir(TEXTO, derivadas, fallos, usos)
    cotejar_texto(texto, derivadas, fallos, usos)

    for mal, nombre in ((chr(8212), "guion largo"), (chr(8211), "guion medio")):
        if mal in texto:
            fallos.append("el texto trae un %s" % nombre)
    if RE_MARCA.search(texto) or RE_VERBATIM.search(texto):
        fallos.append("quedan marcas sin sustituir en el texto final")

    print()
    print("  agujas derivadas: %d | FALLOS: %d" % (len(derivadas), len(fallos)))
    if fallos:
        print()
        print("ROJO: %d fallo(s) y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    antes = len(crudo.split(NL))
    print()
    print("  la pagina tiene %d lineas y el texto anade %d" % (antes, texto.count(NL)))
    if a.simular:
        print()
        print("  SIMULACION: no se escribe nada. El texto empieza asi:")
        for l in texto.split(NL)[:8]:
            print("     %s" % l[:100])
        print()
        print("FIN")
        return 0

    with io.open(PAGINA, "a", encoding="utf-8", newline=NL) as fh:
        fh.write(texto)
    despues = len(io.open(PAGINA, encoding="utf-8").read().split(NL))
    print()
    print("GUARDAS TRAS ESCRIBIR")
    print("  lineas antes %d, despues %d (delta %d)" % (antes, despues, despues - antes))
    txt = io.open(PAGINA, encoding="utf-8").read()
    print("  guiones largos %d, guiones medios %d"
          % (txt.count(chr(8212)), txt.count(chr(8211))))
    # RE-COTEJO TRAS ADOSAR: las sedes de arriba no se movieron. Se mide sobre
    # LAS LINEAS DE ARRIBA SOLAS (las que habia antes de adosar), y no sobre la
    # pagina entera, porque el bloque VERBATIM copia texto de arriba y esa copia
    # haria que su aguja apareciera dos veces: la copia no es una sede nueva.
    _CACHE.clear()
    lineas_de(PAGINA)
    _CACHE[PAGINA] = _CACHE[PAGINA][:antes]
    re_fallos = []
    re_derivadas = derivar(re_fallos, callado=True)
    movidas = [c for c in derivadas
               if c in re_derivadas and re_derivadas[c][0] != derivadas[c][0]]
    print("  re-cotejo tras adosar: %d agujas re-derivadas" % len(re_derivadas))
    print("  las sedes de arriba siguen en su linea: %s"
          % ("OK (%d de %d)" % (len(derivadas), len(derivadas)) if not movidas
             else "ROJO, se movieron: %s" % ", ".join(movidas)))
    if movidas or re_fallos:
        return 1
    print()
    print("VERDE: registro adosado y nada de arriba reescrito.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
