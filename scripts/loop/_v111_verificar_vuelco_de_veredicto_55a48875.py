# -*- coding: utf-8 -*-
r"""verificar_vuelco_de_veredicto.py . LA GUARDA DEL VUELCO DE VEREDICTO
(TAREA 2 de la vuelta 109, acta de la vuelta 108, seccion "EL BARRIDO DEL
TRAMO 2 VUELCA DOS VEREDICTOS REGISTRADOS Y NO DECLARA NINGUNO"). Nombre
estable, SIN numero de vuelta (como verificar_cobertura_bolsa_tres_vias.py
y contar_cierre_efectivo.py): no se clona cada vuelta.

POR QUE NACE. El acta de la vuelta 108 cruzo a mano los seis ficheros de
veredicto puesto a puesto y hallo que el 87 y el 91 cambiaron de SATELITE
(vuelta 105, docs/loop/SALIDA_V105_TAREA4_3_RE_BARRIDO.txt) a OBJETO
(vuelta 108, docs/loop/SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md) sin que
ninguna fila lo dijera, ni siquiera marcada DISCUTIBLE. Los otros tres
vuelcos de la historia (109, 123, 145) SI se declararon, dos de ellos por
el propio ejecutor, dentro de la fila o de la linea de resumen del fichero
que los revierte. La caida fue de HABITO, no de instrumento: nadie habia
escrito la guarda que lo exige. Esta es esa guarda (adjudicacion por
extension de EJECUTOR.md, "LA TABLA SE CUENTA DE SU FICHERO": si el habito
de declarar el vuelco se puede caer, la declaracion la tiene que exigir un
instrumento, no la memoria del que escribe la fila).

QUE HACE. (1) Recorre los MISMOS seis ficheros que
verificar_cobertura_bolsa_tres_vias.FICHEROS_VEREDICTO (se IMPORTA esa
constante, no se vuelve a teclear: una lista que se copia es una lista que
se desincroniza). (2) De cada fichero extrae, para CADA puesto, el
veredicto (OBJETO / SATELITE / NO_OBJETO) Y el texto de su fila o bloque
(para buscar la declaracion despues). (3) Para cada puesto que aparece en
DOS O MAS ficheros, si el veredicto no es el mismo en todos, es un VUELCO:
se reporta el fichero y veredicto del lado MAS VIEJO contra el lado MAS
NUEVO (orden cronologico = el orden de FICHEROS_VEREDICTO, que ya va de
la vuelta 105 a la 108). (4) Por cada vuelco, comprueba si el fichero MAS
NUEVO lo DECLARA.

COMO SE RECONOCE LA DECLARACION (leido de los tres vuelcos reales que SI
la traen, antes de decidir el patron, como pide el encargo):
  - 123 (docs/loop/SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md, fila 24):
    "OBJETO (ya barrido SATELITE en la vuelta 106 y SOSTENIDO tras lectura
    entera, ...)" -- el veredicto VIEJO (SATELITE) Y la vuelta vieja (106)
    viven DENTRO de la propia fila del puesto.
  - 145 (mismo fichero, fila 31): "OBJETO (...; revertido a RESUELTA por
    TAREA 3 de esta vuelta, correccion_v107)" -- no repite la palabra
    SATELITE, pero "revertido" y "correccion_v107" son la marca de que
    el puesto tenia una direccion o veredicto previo que esta fila cambia.
  - 109 (mismo fichero, fila 19): la fila SOLO dice "va a lectura entera,
    docs/loop/SALIDA_V107_TAREA4_1_2_LECTURA_ENTERA_109.md", sin nombrar
    ni el veredicto viejo (OBJETO) ni la vuelta (106). La declaracion vive
    DOS LINEAS MAS ABAJO, en el resumen del mismo fichero (linea 36):
    "SATELITE: 1 (109, nuevo hallazgo de esta vuelta)". Restringir la
    busqueda a la fila exacta del puesto habria dejado al 109 en ROJO
    pese a estar declarado: por eso la busqueda cubre TODA LINEA DEL
    FICHERO que mencione el puesto como palabra suelta (\b<puesto>\b), no
    solo su fila de tabla o bloque.

EL PATRON ACEPTADO, por tanto: el vuelco esta DECLARADO si, entre TODAS las
lineas del fichero mas nuevo que mencionan el puesto como palabra suelta,
alguna contiene (a) el veredicto VIEJO como palabra suelta, o (b) "vuelta
<N>" con N la vuelta del fichero mas viejo, o (c) una de las frases de
declaracion que los tres casos reales ya usan: "nuevo hallazgo", "ya
barrido", "sostenido", "revertido", "correccion_v". Ninguna de estas frases
aparece en ningun lugar del fichero de la vuelta 108 (TRAMO2) que mencione
el 87 o el 91 (comprobado a mano antes de escribir esta lista): las dos
filas son SOLO su propia razon gramatical, sin rastro de que el puesto ya
tuviera otro veredicto. Vuelco declarado: pasa. Vuelco mudo: ROJO EXIT 1
nombrando el puesto.

USO:
  python scripts/loop/verificar_vuelco_de_veredicto.py

CASO POSITIVO (vuelta 109, docs/loop/SALIDA_V109_TAREA2_3_CASO_POSITIVO.txt):
CINCO vuelcos (87, 91, 109, 123, 145); 109, 123 y 145 DECLARADOS; ROJO EXIT 1
nombrando 87 y 91.

CASO ROJO POR MUTACION (vuelta 109,
docs/loop/SALIDA_V109_TAREA2_4_CASO_ROJO_MUTACION.txt): sobre una COPIA de
docs/loop/SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md con la frase "ya barrido
SATELITE en la vuelta 106 y SOSTENIDO tras lectura entera" borrada de la
fila del 123 (dejando solo la razon gramatical), puesta EN EL LUGAR del
fichero real vía `verificar(overrides=...)`: el 123 tiene que pasar de
DECLARADO a MUDO. Si sigue DECLARADO con la frase quitada, el instrumento
no esta leyendo la declaracion de verdad, esta adivinando.
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
from verificar_cobertura_bolsa_tres_vias import FICHEROS_VEREDICTO  # noqa: E402

RE_BLOQUE_CABECERA = re.compile(r"^--- PUESTO (\d+) ---")
RE_BLOQUE_VEREDICTO = re.compile(r"VEREDICTO:\s*(OBJETO|SATELITE|NO_OBJETO)\b")
RE_TABLA_FILA = re.compile(r"^(\d+)\s*\|.*\|\s*(OBJETO|SATELITE|NO_OBJETO)\b")
RE_NOMBRE_VUELTA = re.compile(r"_V(\d+)_")

FRASES_DECLARACION = ["nuevo hallazgo", "ya barrido", "sostenido", "revertido", "correccion_v"]


def vuelta_de(nombre, fallos):
    m = RE_NOMBRE_VUELTA.search(nombre)
    if not m:
        fallos.append("%s: no se pudo leer el numero de vuelta de su nombre" % nombre)
        return None
    return int(m.group(1))


def extraer_bloque(texto):
    """puesto -> veredicto, para el formato 'bloque' (--- PUESTO N ---)."""
    out = {}
    puesto_actual = None
    for linea in texto.splitlines():
        m = RE_BLOQUE_CABECERA.match(linea)
        if m:
            puesto_actual = int(m.group(1))
            continue
        if linea.strip() == "":
            puesto_actual = None
            continue
        if puesto_actual is not None:
            mv = RE_BLOQUE_VEREDICTO.search(linea)
            if mv:
                out[puesto_actual] = mv.group(1)
                puesto_actual = None
    return out


def extraer_tabla(texto):
    """puesto -> veredicto, para el formato 'tabla' (N | ... | PALABRA)."""
    out = {}
    for linea in texto.splitlines():
        m = RE_TABLA_FILA.match(linea)
        if m:
            out[int(m.group(1))] = m.group(2)
    return out


def leer_ficheros(ficheros, overrides, fallos):
    """Devuelve lista de (nombre, vuelta, texto, {puesto: veredicto}), en el
    MISMO orden que `ficheros` (que ya va de la vuelta mas vieja a la mas
    nueva). `overrides` (nombre -> ruta alterna) es SOLO para la prueba de
    mutacion: nunca se usa en una corrida real."""
    salida = []
    for nombre, formato in ficheros:
        ruta = (overrides or {}).get(nombre) or os.path.join(LOOP, nombre)
        if not os.path.exists(ruta):
            fallos.append("no existe %s (declarado en FICHEROS_VEREDICTO)" % nombre)
            continue
        texto = io.open(ruta, encoding="utf-8").read()
        if formato == "bloque":
            veredictos = extraer_bloque(texto)
        elif formato == "tabla":
            veredictos = extraer_tabla(texto)
        else:
            fallos.append("%s: formato %r desconocido" % (nombre, formato))
            continue
        v = vuelta_de(nombre, fallos)
        salida.append((nombre, v, texto, veredictos))
    return salida


def lineas_que_mencionan(texto, puesto):
    patron = re.compile(r"\b%d\b" % puesto)
    return [linea for linea in texto.splitlines() if patron.search(linea)]


def esta_declarado(contexto, veredicto_viejo, vuelta_vieja):
    if re.search(r"\b%s\b" % veredicto_viejo, contexto):
        return True
    if vuelta_vieja is not None and re.search(r"vuelta\s+%d\b" % vuelta_vieja, contexto, re.IGNORECASE):
        return True
    bajo = contexto.lower()
    return any(frase in bajo for frase in FRASES_DECLARACION)


def verificar(overrides=None):
    fallos = []
    lados = leer_ficheros(FICHEROS_VEREDICTO, overrides, fallos)
    if fallos:
        return fallos, None

    # historia[puesto] = [(nombre, vuelta, veredicto), ...] en orden cronologico
    historia = {}
    for nombre, vuelta, _texto, veredictos in lados:
        for puesto, veredicto in veredictos.items():
            historia.setdefault(puesto, []).append((nombre, vuelta, veredicto))

    vuelcos = []
    for puesto in sorted(historia):
        apariciones = historia[puesto]
        if len(apariciones) < 2:
            continue
        vs = set(v for _, _, v in apariciones)
        if len(vs) < 2:
            continue
        nombre_viejo, vuelta_vieja, veredicto_viejo = apariciones[0]
        nombre_nuevo, vuelta_nueva, veredicto_nuevo = apariciones[-1]
        if veredicto_viejo == veredicto_nuevo:
            # el primero y el ultimo coinciden pero algo intermedio distinto:
            # no deberia ocurrir con los datos de hoy, pero no se calla.
            continue
        texto_nuevo = next(t for n, _v, t, _vs in lados if n == nombre_nuevo)
        contexto = "\n".join(lineas_que_mencionan(texto_nuevo, puesto))
        declarado = esta_declarado(contexto, veredicto_viejo, vuelta_vieja)
        vuelcos.append({
            "puesto": puesto,
            "nombre_viejo": nombre_viejo, "vuelta_vieja": vuelta_vieja, "veredicto_viejo": veredicto_viejo,
            "nombre_nuevo": nombre_nuevo, "vuelta_nueva": vuelta_nueva, "veredicto_nuevo": veredicto_nuevo,
            "declarado": declarado,
        })
    return fallos, vuelcos


def main():
    fallos, vuelcos = verificar()
    if fallos:
        print("ROJO, %d cosa(s) no cuadran, NO SE CUENTA NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("FICHEROS DE ENTRADA (declarados en FICHEROS_VEREDICTO, %d, reusada de "
          "verificar_cobertura_bolsa_tres_vias.py):" % len(FICHEROS_VEREDICTO))
    for nombre, formato in FICHEROS_VEREDICTO:
        print("   %s (%s)" % (nombre, formato))
    print()
    print("VUELCOS DE VEREDICTO HALLADOS: %d" % len(vuelcos))
    mudos = []
    for v in vuelcos:
        estado = "DECLARADO" if v["declarado"] else "MUDO"
        print("   %d: %s (%s, vuelta %s) -> %s (%s, vuelta %s) -- %s"
              % (v["puesto"], v["veredicto_viejo"], v["nombre_viejo"], v["vuelta_vieja"],
                 v["veredicto_nuevo"], v["nombre_nuevo"], v["vuelta_nueva"], estado))
        if not v["declarado"]:
            mudos.append(v["puesto"])

    if mudos:
        print("\nROJO: %d vuelco(s) MUDO(s), nombrados: %s"
              % (len(mudos), ", ".join(str(p) for p in mudos)))
        return 1

    print("\nVERDE: todos los vuelcos hallados estan declarados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
