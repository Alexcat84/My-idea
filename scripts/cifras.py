#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cifras.py - LA baranda anti invencion de cifras, en un solo sitio.

POR QUE EXISTE ESTE ARCHIVO. `RE_CIFRA` vivia DUPLICADA en revoz_pack.py y
consolidar_pack.py. Al ampliarla habria quedado la misma regla escrita dos
veces, y esta casa ya adjudico que una regla repartida en varios sitios no falla
de golpe: falla en el que alguien olvido actualizar. Se saca a un solo sitio.

QUE CAZA, y por que solo esto (adjudicacion de ago 2026, en
docs/CIFRAS_EN_PALABRAS_CASOS_GRISES.md):

  1. DIGITOS, como siempre: 15, 3.5, 1,200.
  2. EL COMPUESTO EXACTO `<numeral> por ciento`.
  3. DECENAS, CENTENAS Y MIL como palabra, incluidos compuestos con "y".

ALCANCE ESTRECHO A PROPOSITO. Fracciones, frecuencias, ordinales y numerales
chicos quedan FUERA: la medicion sobre los 3.521 nodos activos demostro que casi
todos viven con DOS sentidos y solo uno es una cifra. Un detector de numerales
sueltos marcaria 2.488 nodos, el 70,7 por ciento del catalogo, y una baranda que
caza lo correcto no es estricta, esta rota. Lo que queda fuera lo cubre la
lectura del lote, que es justo como se cazo el primer caso.

LA REGLA DE TOKENIZACION, que resuelve MIL-STD-105D sin lista de exenciones: se
matchean PALABRAS COMPLETAS EN MINUSCULA, jamas subcadenas de tokens con
mayusculas, guiones o digitos pegados. Por eso no hay `re.I` y por eso los
limites excluyen el guion.

LA SEMANTICA DE DIFF SE CONSERVA INTACTA: solo la aparicion NUEVA respecto del
original rechaza. Lo que ya estaba en el nodo jamas dispara.

VALVULA DE DEGRADACION, fijada por adelantado y no discutible en caliente: si en
operacion se adjudican DOS falsos positivos de la extension de palabras en
dataset/metadata/falsos_positivos_adjudicados.json, esta se degrada a aviso y
vuelve a adjudicacion.
"""
import re

# Los digitos, exactamente como estaban.
RE_CIFRA = re.compile(r"\d+(?:[.,]\d+)?")

_UNIDADES = ("uno", "una", "dos", "tres", "cuatro", "cinco", "seis", "siete",
             "ocho", "nueve", "diez")
_DECENAS = ("veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta",
            "ochenta", "noventa")
_CENTENAS = ("cien", "ciento", "doscientos", "doscientas", "trescientos", "trescientas",
             "cuatrocientos", "cuatrocientas", "quinientos", "quinientas",
             "seiscientos", "seiscientas", "setecientos", "setecientas",
             "ochocientos", "ochocientas", "novecientos", "novecientas")
_MIL = ("mil",)

# Lo que puede ir DELANTE de "por ciento": cualquier numeral, chico incluido.
# Ahi el compuesto es lo que lo hace seguro: "diez por ciento" es una cifra y
# "diez tipos" no.
_ANTES_DE_POR_CIENTO = _UNIDADES + _DECENAS + _CENTENAS + _MIL
# Lo que dispara POR SI SOLO: solo lo grande. "cien pedidos" es una cifra,
# "tres tipos" no.
#
# `ciento` NO entra aqui aunque este en las centenas: suelto es arcaico, y su
# uso real es siempre dentro de "por ciento", que ya cubre la clase del
# compuesto. Dejarlo duplicaba la unidad detectada sin cazar nada nuevo.
_SOLAS = _DECENAS + tuple(c for c in _CENTENAS if c != "ciento") + _MIL

# Un caracter de token es letra, digito o guion. Los limites los excluyen todos,
# asi que `MIL-STD-105D` no puede casar ni aunque estuviera en minuscula, y
# `cien` dentro de `ciencia` tampoco.
_B = r"(?<![0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ\-])"
_F = r"(?![0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ\-])"

# El compuesto con "y": "cuarenta y cinco", "doscientos y uno".
_COLA = r"(?:\s+y\s+(?:" + "|".join(_UNIDADES + _DECENAS) + r"))?"

RE_POR_CIENTO = re.compile(
    _B + r"(?:" + "|".join(_ANTES_DE_POR_CIENTO) + r")" + _COLA + r"\s+por\s+ciento" + _F)
RE_NUMERAL_GRANDE = re.compile(
    _B + r"(?:" + "|".join(_SOLAS) + r")" + _COLA + _F)


def _normalizar(s):
    """Un espacio entre palabras, para que 'cuarenta  y cinco' y 'cuarenta y
    cinco' sean la MISMA cifra y el diff no las vea distintas."""
    return " ".join(s.split())


def cifras_de(texto):
    """Todas las cifras del texto: digitos, porcentajes escritos y numerales
    grandes. Devuelve un conjunto normalizado, listo para restar."""
    texto = texto or ""
    out = set(RE_CIFRA.findall(texto))
    out |= {_normalizar(m.group(0)) for m in RE_POR_CIENTO.finditer(texto)}
    out |= {_normalizar(m.group(0)) for m in RE_NUMERAL_GRANDE.finditer(texto)}
    return out


def cifras_nuevas(texto_nuevo, textos_originales):
    """Las cifras que aparecen en el texto nuevo y en NINGUNO de los originales.

    Es toda la baranda: lo que ya estaba jamas dispara, y por eso un nodo que
    conserva sus propias cifras pasa siempre.
    """
    if isinstance(textos_originales, str):
        textos_originales = [textos_originales]
    antes = set()
    for t in textos_originales:
        antes |= cifras_de(t)
    return sorted(cifras_de(texto_nuevo) - antes)
