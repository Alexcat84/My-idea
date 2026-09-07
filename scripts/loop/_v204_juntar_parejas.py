# -*- coding: utf-8 -*-
r"""_v204_juntar_parejas.py . JUNTA CADA CIFRA CON SU PAREJA EN EL MISMO
RENGLON, EN LAS SECCIONES YA ANEXADAS Y EN SUS FUENTES A LA VEZ.

PREFIJO DE GUION BAJO: computo de una vuelta, fuera del censo y de la nomina.

POR QUE EXISTE, Y ES LA LETRA (b) QUE EL ENCARGO ESCRIBIO ANTES DE QUE ME
PASARA: *el markdown parte la frase donde le cabe el ancho, junta cada cifra con
su pareja en el MISMO renglon*. La guarda de `cerrar_reporte.py` me tumbo el
cierre con **9 cifras publicadas sin su pareja** y **2 parejas atribuidas a la
ruta equivocada**, y las once son de lo mismo: la pareja existia y el salto de
linea la partia.

NO SE CAMBIA NI UNA CIFRA. Lo unico que se mueve es DONDE CORTA EL RENGLON, y la
unica cifra que se ANADE es la que ya estaba medida y no escrita (el crecimiento
por las dos convenciones, que en un fichero sin CRLF es el mismo numero).

Y SE APLICA A LOS DOS SITIOS A LA VEZ, `docs/loop/REPORTE.md` y el `.md` fuente
de cada seccion, para que sigan siendo el mismo texto: si una sustitucion no
aparece exactamente una vez en cada sitio, CAE EN ROJO y no escribe nada.

USO: python scripts/loop/_v204_juntar_parejas.py
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")

CAMBIOS = [
    ("scripts/loop/_v204_t1_seccion.md",
     "- **PRIMERA CORRIDA:** `docs/PENDIENTES.md` entra con **1131953 bytes en disco y" + NL
     + "  1131953 normalizado a LF**, `sha256` LF **725b85e12050a0ae**, y sale con" + NL
     + "  **1145356 bytes en disco y 1145356 normalizado a LF**, `sha256` LF" + NL
     + "  **de3311c2a8d5aa8c**. Crecimiento **13403 bytes** y **209 lineas**.",
     "- **PRIMERA CORRIDA.** `docs/PENDIENTES.md` entra con **1131953 bytes en disco y 1131953 normalizado a LF**," + NL
     + "  y su `sha256` de entrada es **725b85e12050a0ae** en disco y **725b85e12050a0ae** normalizado a LF." + NL
     + "  Sale con **1145356 bytes en disco y 1145356 normalizado a LF**," + NL
     + "  y su `sha256` de salida es **de3311c2a8d5aa8c** en disco y **de3311c2a8d5aa8c** normalizado a LF." + NL
     + "  Crecimiento **13403 bytes en disco y 13403 normalizado a LF**, y **209** lineas mas."),

    ("scripts/loop/_v204_t1_seccion.md",
     "  (`docs/loop/SALIDA_V204_T1_REGISTROS_SEGUNDA.txt`): **crecimiento 0 bytes y 0" + NL
     + "  lineas, 0 entradas escritas**, porque la guarda de idempotencia mira **el",
     "  (`docs/loop/SALIDA_V204_T1_REGISTROS_SEGUNDA.txt`): **crecimiento 0 bytes en disco y 0 normalizado a LF**," + NL
     + "  **0 lineas y 0 entradas escritas**, porque la guarda de idempotencia mira **el"),

    ("scripts/loop/_v204_t2_seccion.md",
     "**LA SEDE, RECONTADA HOY:** `docs/plan/INVENTARIO.jsonl` mide **584554 bytes en" + NL
     + "disco y 584554 normalizado a LF**, `sha256` LF **69666b73339f2afe**, con **672",
     "**LA SEDE, RECONTADA HOY:** `docs/plan/INVENTARIO.jsonl` mide **584554 bytes en disco y 584554 normalizado a LF**," + NL
     + "con `sha256` **69666b73339f2afe** en disco y **69666b73339f2afe** normalizado a LF, y con **672"),

    ("scripts/loop/_v204_t2_seccion.md",
     "`OP-I-01` vive en la **linea 44** de `docs/plan/OPERACIONES.jsonl`, que mide" + NL
     + "**513043 bytes en disco y 513043 normalizado a LF**, `sha256` LF" + NL
     + "**829c583eb779cab6**. Su `verificacion` trae 4 elementos:",
     "`OP-I-01` vive en la **linea 44** de `docs/plan/OPERACIONES.jsonl`," + NL
     + "que mide **513043 bytes en disco y 513043 normalizado a LF**," + NL
     + "con `sha256` **829c583eb779cab6** en disco y **829c583eb779cab6** normalizado a LF." + NL
     + "Su `verificacion` trae 4 elementos:"),

    ("scripts/loop/_v204_t3_seccion.md",
     "`docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` mide **96361 bytes en disco y 96029" + NL
     + "normalizado a LF**, `sha256` LF **95dca64dbce48d52**, y **332 lineas no vacias**.",
     "`docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` mide **96361 bytes en disco y 96029 normalizado a LF**, `sha256` LF **95dca64dbce48d52**," + NL
     + "y **332 lineas no vacias**."),

    ("scripts/loop/_v204_t3_seccion.md",
     "`docs/loop/RECOMPUTO_V169.jsonl` mide **15369 bytes en disco y 15322 normalizado" + NL
     + "a LF**, `sha256` LF **e8a10f174df3c5fa**, **antes y despues de correr**, y",
     "`docs/loop/RECOMPUTO_V169.jsonl` mide **15369 bytes en disco y 15322 normalizado a LF**, `sha256` LF **e8a10f174df3c5fa**," + NL
     + "**antes y despues de correr**, y"),

    ("scripts/loop/_v204_t4_seccion.md",
     "**LA PRIMERA, EL CAMPO `estado`, QUE ES LA QUE `AUDITOR.md` 0 PROHIBE COMO VARA**" + NL
     + "y que va aqui porque el encargo pide las dos: `docs/plan/OPERACIONES.jsonl` mide" + NL
     + "**513043 bytes en disco y 513043 normalizado a LF**, `sha256` LF" + NL
     + "**829c583eb779cab6**, con **71 lineas no vacias, 42 en `LISTA` y 29 en `HECHA`**.",
     "**LA PRIMERA, EL CAMPO `estado`, QUE ES LA QUE `AUDITOR.md` 0 PROHIBE COMO VARA**" + NL
     + "y que va aqui porque el encargo pide las dos." + NL
     + "`docs/plan/OPERACIONES.jsonl` mide **513043 bytes en disco y 513043 normalizado a LF**," + NL
     + "con `sha256` **829c583eb779cab6** en disco y **829c583eb779cab6** normalizado a LF." + NL
     + "Trae **71 lineas no vacias, 42 en `LISTA` y 29 en `HECHA`**."),

    ("scripts/loop/_v204_t4_seccion.md",
     "`docs/loop/SALIDA_V204_HEAD_APERTURA.txt` y no tecleado**. Su salida mide" + NL
     + "**18759 bytes en disco y 18468 normalizado a LF**, `sha256` LF" + NL
     + "**26aceea650da798e**.",
     "`docs/loop/SALIDA_V204_HEAD_APERTURA.txt` y no tecleado**." + NL
     + "`docs/loop/SALIDA_V204_T4_VARA.txt` mide **18759 bytes en disco y 18468 normalizado a LF**, `sha256` LF **26aceea650da798e**."),

    ("scripts/loop/_v204_t4_seccion.md",
     "`docs/plan/OPERACIONES.jsonl` sale con **513043 bytes en disco y 513043" + NL
     + "normalizado a LF**, `sha256` LF **829c583eb779cab6**, **identico al de entrada**,",
     "`docs/plan/OPERACIONES.jsonl` sale con **513043 bytes en disco y 513043 normalizado a LF**, `sha256` LF **829c583eb779cab6**," + NL
     + "**identico al de entrada**,"),
]

# LOS DEL CUERPO DE CIERRE NO ESTAN TODAVIA EN EL REPORTE: SOLO EN SU FUENTE.
SOLO_FUENTE = [
    ("scripts/loop/_v204_cierre_texto.md",
     "  abre y cierra en `sha256` **`0a77b5a35a962621`** por las dos convenciones.",
     "  abre y cierra en `sha256` **`0a77b5a35a962621`** en disco y **`0a77b5a35a962621`** normalizado a LF."),
    ("scripts/loop/_v204_cierre_texto.md",
     "  `sha256` LF **`829c583eb779cab6`** con el que entro, y **0 de las 71 fichas**",
     "  `sha256` **`829c583eb779cab6`** en disco y **`829c583eb779cab6`** normalizado a LF, y **0 de las 71 fichas**"),
]

texto_rep = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
fuentes = {}
for rel, viejo, nuevo in CAMBIOS + SOLO_FUENTE:
    if rel not in fuentes:
        fuentes[rel] = io.open(os.path.join(RAIZ, rel),
                               encoding="utf-8").read().replace(chr(13) + NL, NL)

fallos = []
print("LAS SUSTITUCIONES, CADA UNA CONTADA EN SUS DOS SITIOS:")
for rel, viejo, nuevo in CAMBIOS:
    en_fuente = fuentes[rel].count(viejo)
    en_rep = texto_rep.count(viejo)
    print("   %-38s fuente %d | reporte %d" % (os.path.basename(rel), en_fuente, en_rep))
    if en_fuente != 1 or en_rep != 1:
        fallos.append("%s: fuente %d, reporte %d, y se necesita 1 y 1"
                      % (os.path.basename(rel), en_fuente, en_rep))
        continue
    fuentes[rel] = fuentes[rel].replace(viejo, nuevo)
    texto_rep = texto_rep.replace(viejo, nuevo)

print("")
print("LAS DEL CUERPO DE CIERRE, QUE TODAVIA NO ESTAN EN EL REPORTE:")
for rel, viejo, nuevo in SOLO_FUENTE:
    en_fuente = fuentes[rel].count(viejo)
    en_rep = texto_rep.count(viejo)
    print("   %-38s fuente %d | reporte %d (se espera 0)"
          % (os.path.basename(rel), en_fuente, en_rep))
    if en_fuente != 1 or en_rep != 0:
        fallos.append("%s: fuente %d, reporte %d, y se necesita 1 y 0"
                      % (os.path.basename(rel), en_fuente, en_rep))
        continue
    fuentes[rel] = fuentes[rel].replace(viejo, nuevo)

print("")
if fallos:
    print("ROJO, %d motivo(s), y NO se escribe nada:" % len(fallos))
    for f in fallos:
        print("   " + f)
    raise SystemExit(1)

for rel, t in fuentes.items():
    io.open(os.path.join(RAIZ, rel), "w", encoding="utf-8", newline=NL).write(t)
io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(texto_rep)

print("VERDE. ESCRITOS:")
for rel in sorted(fuentes):
    print("   %s" % rel)
print("   docs/loop/REPORTE.md (%d bytes, %d saltos de linea)"
      % (len(texto_rep.encode("utf-8")), texto_rep.count(NL)))
print("")
print("LA COMPROBACION QUE CONVIERTE 'siguen siendo el mismo texto' EN MEDICION:")
for rel in sorted(fuentes):
    if rel.endswith("_cierre_texto.md"):
        continue
    cuerpo = fuentes[rel]
    dentro = cuerpo.rstrip(NL) in texto_rep
    print("   %-40s esta byte a byte dentro del reporte: %s"
          % (os.path.basename(rel), "SI" if dentro else "NO"))
