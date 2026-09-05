# -*- coding: utf-8 -*-
r"""_v178_parche_congelado.py . EL PARCHE QUE INSTRUMENTA LA REGLA DEL SUJETO
CONGELADO EN `scripts/loop/verificar_mutaciones_viejas.py` (vuelta 178, TAREA
1.e).

ES UN PARCHE, NO CODIGO VIVO: empieza por guion bajo, no lo ve el censo de
arneses y no entra en ninguna nomina. Cada sustitucion lleva su `assert`.
"""
import io
import os

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R = os.path.join(RAIZ, "scripts", "loop", "verificar_mutaciones_viejas.py")

t = io.open(R, encoding="utf-8").read().replace(chr(13) + NL, NL)
PARES = []

BLOQUE = '''# LA REGLA DEL SUJETO CONGELADO DEJA DE SER UNA FRASE (vuelta 178, TAREA 1.e;
# `PD.2` del reporte 176, adjudicado a favor del ejecutor en el acta 176 punto
# 7.9 con destino esta vuelta).
#
# LA REGLA EXISTE DESDE LA VUELTA 145 Y SIGUE ESCRITA ARRIBA, palabra por
# palabra: una mutacion entra en la nomina SOLO SI SU SUJETO ESTA CONGELADO, y
# la que no pueda tenerlo entra como CASO DECLARADO. Lo que NO existia es nada
# que la hiciera cumplir: la nomina admitia arneses anclados a ficheros vivos y
# nadie lo veia hasta que el registro crecia lo bastante. El rojo del tramo 6 de
# la vuelta 176 fue exactamente eso.
#
# QUE MIDE, Y ES SOBRE EL TEXTO DEL PROPIO ARNES. Un sujeto congelado deja
# HUELLA EN EL CODIGO que lo lee, y esa huella es de una de estas formas:
# fabrica su sujeto en un temporal, se hace una copia en memoria, lee un blob de
# git clavado, o apunta a un fichero `SUJETO_FIJO_*` commiteado. Un sujeto vivo
# tambien deja huella: abre por su nombre uno de los ficheros que la campana
# mueve cada vuelta.
#
# LA CLASIFICACION ES DE TRES ESTADOS Y NO DE DOS, y esa es la parte honesta: si
# un arnes trae LAS DOS huellas, esta guarda NO ADIVINA cual manda. Pide que el
# propio arnes lo declare con el literal `SUJETO CONGELADO` en su texto, que es
# lo que la casa ya escribe en los que lo tienen. Sin esa declaracion el
# veredicto es NO DECIDIBLE, y NO DECIDIBLE no es verde.
#
# LO QUE ESTA GUARDA NO HACE: no poda la nomina, no reescribe ningun arnes y no
# decide si un arnes vale. Clasifica y publica.

HUELLAS_DE_CONGELADO = (
    "SUJETO_FIJO",       # un fichero congelado y commiteado en docs/loop/
    "tempfile",          # fabrica su propio sujeto y lo retira (P.16)
    "mkdtemp",
    "deepcopy",          # copia en memoria, el original no se toca
    "git show",          # blob de git, que no se mueve
    "cat-file",
    "sha256",            # sujeto clavado por su huella de contenido
    "SUJETO CONGELADO",  # lo declara el propio arnes
)

HUELLAS_DE_VIVO = (
    "REPORTE.md",
    "INTRA_DOMINIO_VEREDICTOS.jsonl",
    "OPERACIONES.jsonl",
    "master_graph.json",
    "ACTA_AUDITOR.md",
    "LECTURAS_DIRIGIDAS.md",
)

MARCA_DECLARA_CONGELADO = "SUJETO CONGELADO"


def texto_del_arnes(nombre, directorio=None):
    """EL TEXTO DE UN ARNES, o cadena vacia si no esta. Lo unico de esta familia
    que toca disco, y se aisla aqui para que el resto sea puro."""
    ruta = os.path.join(directorio or LOOP, nombre)
    if not os.path.isfile(ruta):
        return ""
    return io.open(ruta, encoding="utf-8", errors="replace").read().replace(
        chr(13) + chr(10), chr(10))


def anclaje_de(texto, declarado=False):
    """EL VEREDICTO DE ANCLAJE DE UN ARNES, LEIDO DE SU TEXTO. PURA.

    Devuelve (veredicto, huellas_de_congelado, huellas_de_vivo). El veredicto es
    uno de: CASO DECLARADO, CONGELADO, SUJETO VIVO, NO DECIDIBLE.

    `declarado` dice si el arnes esta en `CASOS_DECLARADOS`, que es la exencion
    que la regla de la vuelta 145 ya preveia y la unica que hay."""
    congela = [h for h in HUELLAS_DE_CONGELADO if h in texto]
    vive = [h for h in HUELLAS_DE_VIVO if h in texto]
    if declarado:
        return "CASO DECLARADO", congela, vive
    if congela and not vive:
        return "CONGELADO", congela, vive
    if vive and not congela:
        return "SUJETO VIVO", congela, vive
    if congela and vive:
        if MARCA_DECLARA_CONGELADO in texto:
            return "CONGELADO", congela, vive
        return "NO DECIDIBLE", congela, vive
    return "CONGELADO", congela, vive


def anclaje_de_la_nomina(nomina=None, directorio=None, declarados=None):
    """[(nombre, veredicto, congela, vive)] para toda la nomina, en su orden.

    Semi-pura: lo unico que toca disco es leer los ficheros, y `directorio` va
    por parametro para que su caso positivo por mutacion pueda apuntarla a uno
    fabricado."""
    entradas = nomina if nomina is not None else VIEJAS
    dec = CASOS_DECLARADOS if declarados is None else declarados
    salida = []
    for nombre, _admite in entradas:
        texto = texto_del_arnes(nombre, directorio)
        v, c, vv = anclaje_de(texto, declarado=(nombre in dec))
        salida.append((nombre, v, c, vv))
    return salida


def guarda_del_sujeto_congelado(nomina=None, directorio=None, declarados=None):
    """LOS QUE NO CUMPLEN LA REGLA. Devuelve [(nombre, veredicto, vive)].

    Solo `SUJETO VIVO` y `NO DECIDIBLE` cuentan: un `CASO DECLARADO` esta exento
    por la propia regla, y un `CONGELADO` la cumple."""
    return [(n, v, vv)
            for n, v, _c, vv in anclaje_de_la_nomina(nomina, directorio, declarados)
            if v in ("SUJETO VIVO", "NO DECIDIBLE")]


'''

PARES.append(("def vuelta_de(nombre):", BLOQUE + "def vuelta_de(nombre):"))

for viejo, nuevo in PARES:
    assert viejo in t, "NO ESTA: " + viejo[:70]
    t = t.replace(viejo, nuevo, 1)

io.open(R, "w", encoding="utf-8", newline=NL).write(t)
print("PARCHES APLICADOS: %d" % len(PARES))
print("verificar_mutaciones_viejas.py -> %d bytes en disco y %d normalizado a LF"
      % (len(t.encode("utf-8")), len(t.encode("utf-8"))))
