# -*- coding: utf-8 -*-
"""RELECTURA AL DOBLE DEL TRAMO (regla del credito, AUDITOR.md seccion 1.2).
La caida de la vuelta 91 cayo FUERA de los discutibles marcados, asi que el
tramo entero de las 80 direcciones automaticas se relee con una vara nueva:

NO basta con que la razon tenga una marca de HIJO ("trae"). El banco 9.6.2
exige que la razon NOMBRE LA LINEA DE LA MADRE que el hijo despliega ("dice
en su paso N, en UNA LINEA", "ES EL INDICE", "ENUMERA", "es UNA LINEA y X
trae su procedimiento", "MONTA EL MARCO", ...). Un par con marca de hijo y
SIN marca de madre es un par cuya jerarquia nadie escribio: candidato a
SALIR por la propia `verificacion` de OP-E-07.
"""
import io, json, re, os
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V = {}
for l in io.open(os.path.join(RAIZ,'docs','INTRA_DOMINIO_VEREDICTOS.jsonl'), encoding='utf-8'):
    l = l.strip()
    if l:
        d = json.loads(l); V[int(d['puesto_intra'])] = d
EJ = [json.loads(l) for l in io.open(os.path.join(RAIZ,'docs','plan','OP_E_07_DIRECCION_V91.jsonl'), encoding='utf-8')]
MANUALES = {1163,1191,1388,1500,1778,1847,1886,1992}

MARCA_MADRE = re.compile(
    r"dice en su paso|dicen en su paso|en UNA LINEA|en DOS LINEAS|es UNA LINEA|"
    r"ES EL INDICE|es el indice|ENUMERA|enumera|MONTA EL MARCO|"
    r"en su paso \d|Ese (?:tercer|primer|segundo|cuarto|quinto|sexto|septimo|octavo|noveno) paso|"
    r"lo compartido es una linea|Lo compartido es UNA linea|una sola linea|UNA SOLA LINEA|"
    r"es el catalogo|es un repertorio|es un habito|despacha en|nombra en|"
    r"lo dice en un paso|en un solo paso de|cabe entero dentro", re.IGNORECASE)
NIEGA = re.compile(r"no crea jerarquia|ninguno la expande|no hay jerarquia|sin jerarquia|ninguno de los dos", re.IGNORECASE)

sin_madre, niegan, ok = [], [], 0
for e in EJ:
    p = int(e['puesto'])
    if p in MANUALES:
        continue
    r = V[p]['razon']
    if NIEGA.search(r):
        niegan.append(p)
    if not MARCA_MADRE.search(r):
        sin_madre.append(p)
    else:
        ok += 1

print('AUTOMATICAS RELEIDAS (80):', len(EJ) - len(MANUALES))
print('con MARCA DE MADRE explicita en la razon:', ok)
print('SIN marca de madre (la jerarquia descansa solo en un "trae" suelto):', len(sin_madre))
print('  puestos:', sin_madre)
print('con formula que NIEGA la jerarquia:', len(niegan), niegan)
