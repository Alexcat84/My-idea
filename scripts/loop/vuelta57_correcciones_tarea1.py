# -*- coding: utf-8 -*-
"""vuelta57_correcciones_tarea1.py . LAS TRES CITAS DE PUESTO CON CLASE QUE LA
VUELTA 56 DEJO ENVEJECIDAS, CORREGIDAS CON TACHADO, CUENTA CUADRADA Y NOTA
FECHADA.

LA REGLA QUE LO MANDA: banco `9.10`, todo volteo barre sus tablas derivadas EN
EL MISMO ACTO. La vuelta 56 volteo el puesto 203 de `C` a `D` (relectura del
filo del acto 15 del tramo 3 de `OP-U-01`) y NO barrio las tres tablas que lo
citan con clase. El precedente contrario esta escrito: la vuelta 49 volteo el
844 y SI tacho su cita en el mismo acto.

Y LA LISTA DE LAS SIETE SANAS CON FIGURA ESTABA ENVEJECIDA POR LOS DOS LADOS, no
solo por el 203, y las dos direcciones se dicen porque son especies distintas:

  SALEN TRES. El `203` lo volteo la vuelta 56. El `246` y el `360` dejaron de
  ser `C` cuando sus actos se fundieron en las vueltas 52 y 53 y sus dos lados
  pasaron a resolver al mismo nodo vivo: nadie los tecleo mal, envejecieron
  solos.

  ENTRA UNO, y este NADIE lo habia notado. El `494` es `C` desde el 15 ago 2026,
  medido con `git` sobre las 194 versiones del archivo de veredictos: el commit
  `7cec9ecc` lo volteo de `A` a `C` por el tercer ejemplar del banco `9.22`, y
  las dos listas no lo recogieron nunca. Una lista publicada puede envejecer por
  no soltar y tambien por no tomar.

LA `C` VIGENTE, RECOMPUTADA HOY del archivo y no heredada de ningun texto:
201, 215, 494, 1077 y 1240, CINCO.

Y UNA CELDA VECINA QUE VA EN EL MISMO ACTO Y SE DECLARA: la fila hermana de esa
misma tabla publica `B, dudosas` en **89**, que es la `B` de una medicion vieja.
La `B` de hoy es **72**. Corregir el `7` y dejar el `89` en la fila de arriba
seria la caida de medir una celda y publicar la de al lado sin mirarla, que es
justo la especie que la regla 1 castiga. Va corregida con su nota, y va MARCADA
COMO DISCUTIBLE en el reporte porque el encargo no la nombraba.

DONDE VA CADA NOTA, y el motivo es de instrumento: las CELDAS quedan limpias
(solo el tachado y la cifra nueva) y las notas fechadas van en un BLOQUE DE CITA
debajo de su tabla. Asi `scripts/loop/vuelta57_puestos_volteados.py` puede leer
la celda sin tropezar con las letras de clase que la propia nota nombra. Ninguna
nota vieja se reescribe y ningun texto viejo se borra.

IDEMPOTENTE: cada sustitucion comprueba primero si su resultado ya esta escrito,
y el ancla literal tiene que aparecer EXACTAMENTE UNA VEZ. Si no aparece, o
aparece de mas, es ROJO y no se escribe nada.

Uso: python scripts/loop/vuelta57_correcciones_tarea1.py [--simular]
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INFORME = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_INFORME.md")
FUSIONES = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
ENLACES = os.path.join(RAIZ, "docs", "plan", "04_ENLACES.md")

# El enlace a las salidas se escribe RELATIVO A SU FICHERO. Desde docs/ la
# carpeta es `loop/`; desde docs/plan/ es `../loop/`. La nota de la vuelta 56 en
# el informe usa `../loop/`, que desde docs/ no resuelve: se deja como esta (no
# es una cifra y no es el encargo de hoy) y se declara en el reporte.
MED_DOCS = ("Medido HOY sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` con "
            "`python scripts/loop/vuelta57_puestos_volteados.py --base c0e8041a "
            "--tambien 203,246,360`: "
            "[`loop/SALIDA_V57_PUESTOS_VOLTEADOS_ANTES.txt`](loop/SALIDA_V57_PUESTOS_VOLTEADOS_ANTES.txt) "
            "da esta celda ROJA y "
            "[`loop/SALIDA_V57_PUESTOS_VOLTEADOS_DESPUES.txt`](loop/SALIDA_V57_PUESTOS_VOLTEADOS_DESPUES.txt) "
            "la da VERDE.")

MED_PLAN = ("Medido HOY sobre `../INTRA_DOMINIO_VEREDICTOS.jsonl` con "
            "`python scripts/loop/vuelta57_puestos_volteados.py --base c0e8041a "
            "--tambien 203,246,360` y con `python scripts/recomputar_marcador.py 3388`: "
            "[`../loop/SALIDA_V57_PUESTOS_VOLTEADOS_ANTES.txt`](../loop/SALIDA_V57_PUESTOS_VOLTEADOS_ANTES.txt) "
            "da estas celdas ROJAS, "
            "[`../loop/SALIDA_V57_PUESTOS_VOLTEADOS_DESPUES.txt`](../loop/SALIDA_V57_PUESTOS_VOLTEADOS_DESPUES.txt) "
            "las da VERDES, y "
            "[`../loop/SALIDA_V57_MARCADOR_APERTURA.txt`](../loop/SALIDA_V57_MARCADOR_APERTURA.txt) "
            "es la corrida del marcador de la que salen el 5 y el 72.")

NOTA_INFORME = (
    "\n> **CORRECCION DECLARADA (20 ago 2026, vuelta 57, TAREA 1.1, por el carril del banco "
    "`9.10`). LA CELDA DEL 203 EN ESTA TABLA ESTABA ENVEJECIDA UNA VUELTA ENTERA.** La vuelta "
    "56 volteo ese puesto en la relectura del filo del acto 15 del tramo 3 de `OP-U-01`, y **no "
    "barrio esta tabla derivada en el mismo acto**, que es lo que el `9.10` manda y lo que el "
    "precedente del **844** (vuelta 49) si hizo. **Lo que la remedicion del 653 dice NO cambia "
    "y por eso no se reescribe**: los tres nodos de la figura no repiten entre si y la unica "
    "`A` sigue siendo la del ciclo. Lo unico que se mueve es el veredicto de esa fila. " +
    MED_DOCS + "\n")

NOTA_FUSIONES = (
    "\n> **CORRECCION DECLARADA (20 ago 2026, vuelta 57, TAREA 1.2, por el carril del banco "
    "`9.10`). LA LISTA DE LAS SANAS CON FIGURA ESTABA ENVEJECIDA POR LOS DOS LADOS, y las dos "
    "direcciones se dicen porque son especies distintas.**\n>\n"
    "> **SALEN TRES.** El **`203`** lo volteo la vuelta 56 en la relectura del filo del acto 15 "
    "del tramo 3 de `OP-U-01`. El **`246`** y el **`360`** dejaron de serlo cuando sus actos se "
    "fundieron en las vueltas 52 y 53 y sus dos lados pasaron a resolver al mismo nodo vivo: "
    "**nadie los tecleo mal, envejecieron solos**, y por eso ningun barrido que dependa de que "
    "alguien NOMBRE el puesto los iba a cazar.\n>\n"
    "> **ENTRA UNO, y este no lo habia notado nadie.** El **`494`** lo es desde el **15 ago "
    "2026**, medido con `git` sobre las versiones del archivo de veredictos: el commit "
    "`7cec9ecc` lo volteo desde `A` por el **tercer ejemplar del banco `9.22`**, y esta lista "
    "no lo recogio nunca. **Una lista publicada envejece por no soltar y tambien por no "
    "tomar.**\n>\n"
    "> **LA CUENTA VIGENTE, RECOMPUTADA HOY del archivo y no heredada de ningun texto: 201, "
    "215, 494, 1077 y 1240, CINCO.** " + MED_PLAN + "\n>\n"
    "> **Y LA FILA DE ARRIBA VA EN EL MISMO ACTO, aunque el encargo no la nombraba:** publicaba "
    "**89** dudosas, que es la cifra de una medicion vieja; la de hoy es **72**. Corregir una "
    "celda y publicar la de al lado sin mirarla es la caida que la regla 1 castiga, asi que se "
    "corrige aqui y **se marca como discutible en el reporte de la vuelta**.\n")

NOTA_ENLACES = (
    "\n> **CORRECCION DECLARADA (20 ago 2026, vuelta 57, TAREA 1.2, por el carril del banco "
    "`9.10`). ESTA LISTA ES HERMANA DE LA DE `03_FUSIONES.md` Y ESTABA ENVEJECIDA IGUAL.** "
    "Salen el **`203`** (volteado por la vuelta 56, relectura del filo del acto 15 del tramo 3 "
    "de `OP-U-01`), el **`246`** y el **`360`** (sus actos se fundieron en las vueltas 52 y 53 "
    "y sus dos lados pasaron a resolver al mismo nodo vivo). Entra el **`494`**, que lo es "
    "desde el 15 ago 2026 por el commit `7cec9ecc` y que esta lista no recogio nunca. **La "
    "cuenta vigente, recomputada hoy del archivo: 201, 215, 494, 1077 y 1240, CINCO**, y por "
    "eso el titulo de la seccion tambien se tacha. **El texto de la regla no cambia**: siguen "
    "siendo enlace mutuo del banco `9.22` y siguen sin fundirse. " + MED_PLAN + "\n")

# (fichero, ancla literal unica, texto nuevo, etiqueta)
CAMBIOS = [
    (INFORME,
     "| el conjunto contra la mitad del pago | 203 | **C** |",
     "| el conjunto contra la mitad del pago | 203 | ~~**C**~~ **D** |",
     "1.1 informe 4169, la celda del 203"),
    (FUSIONES,
     "| **B, dudosas** | **89** |",
     "| **B, dudosas** | ~~**89**~~ **72** |",
     "1.2 03_FUSIONES 166, la cuenta de las dudosas (celda vecina, declarada)"),
    (FUSIONES,
     "| **C, sanas con figura** | **7** | **no se funden NUNCA**: son **ENLACE MUTUO**, "
     "o sea **dos aristas**. Puestos 201, 203, 215, 246, 360, 1077 y 1240 |",
     "| **C, sanas con figura** | ~~**7**~~ **5** | **no se funden NUNCA**: son "
     "**ENLACE MUTUO**, o sea **dos aristas**. Puestos 201, ~~203~~, 215, ~~246~~, ~~360~~, "
     "**494**, 1077 y 1240 |",
     "1.2 03_FUSIONES 167, la lista de las sanas con figura"),
    (ENLACES,
     "## LAS SIETE C TAMBIEN SON DE ESTA FASE",
     "## ~~LAS SIETE C~~ LAS CINCO C TAMBIEN SON DE ESTA FASE",
     "1.2 04_ENLACES 310, el titulo de la seccion"),
    (ENLACES,
     "una fusion. Puestos **201, 203, 215, 246, 360, 1077 y 1240**.",
     "una fusion. Puestos **201, ~~203~~, 215, ~~246~~, ~~360~~, 494, 1077 y 1240**.",
     "1.2 04_ENLACES 313, la lista de las sanas con figura"),
]

# (fichero, ancla literal unica del final del bloque, nota, etiqueta)
ADOSADOS = [
    (INFORME,
     "> el nodo del ciclo. **Los dos forman una PAREJA CERRADA**: ninguno de los dos\n"
     "> tiene otra A.\n",
     NOTA_INFORME, "1.1 informe, la nota fechada debajo del bloque"),
    (FUSIONES,
     "> **Fundir una C seria el error caro que el banco 9.22 nombra**: borraria los dos\n"
     "> procedimientos para dejar un nodo con dos lineas sueltas. **Van a la fase 04, no\n"
     "> a esta.**\n",
     NOTA_FUSIONES, "1.2 03_FUSIONES, la nota fechada debajo del bloque"),
    (ENLACES,
     "> **Es el ENLACE MUTUO del banco 9.22**: cada nodo expande una linea distinta del\n"
     "> otro, ninguno es la madre, **y fundirlos borraria los dos procedimientos.**\n",
     NOTA_ENLACES, "1.2 04_ENLACES, la nota fechada debajo del bloque"),
]


def sustituir(ruta, viejo, nuevo, etiqueta, simular, estado):
    with io.open(ruta, encoding="utf-8", newline="") as fh:
        t = fh.read()
    # CADA FICHERO CON SU FINAL DE LINEA, y se mide en vez de suponerse: medido
    # hoy, `04_ENLACES.md` viene con CRLF y el informe y `03_FUSIONES.md` con LF.
    # Un ancla de varias lineas escrita con LF no aparece en el fichero de CRLF y
    # el instrumento cae en ROJO diciendo que aparece 0 veces, que fue lo que
    # paso en la primera corrida de hoy.
    if "\r\n" in t:
        viejo = viejo.replace("\r\n", "\n").replace("\n", "\r\n")
        nuevo = nuevo.replace("\r\n", "\n").replace("\n", "\r\n")
    if nuevo in t:
        estado.append((etiqueta, "YA ESTABA"))
        return 0
    veces = t.count(viejo)
    if veces != 1:
        estado.append((etiqueta, "ROJO: el ancla literal aparece %d veces" % veces))
        return 1
    if not simular:
        with io.open(ruta, "w", encoding="utf-8", newline="") as fh:
            fh.write(t.replace(viejo, nuevo))
    estado.append((etiqueta, "CORREGIDA"))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("TAREA 1 DE LA VUELTA 57: LAS CITAS DE PUESTO CON CLASE QUE ENVEJECIERON")
    print("MODO %s" % ("SIMULAR" if a.simular else "ESCRIBIR"))
    print("=" * 78)
    print()

    estado, rojo = [], 0
    for ruta, viejo, nuevo, etq in CAMBIOS:
        rojo += sustituir(ruta, viejo, nuevo, etq, a.simular, estado)
    for ruta, ancla, nota, etq in ADOSADOS:
        rojo += sustituir(ruta, ancla, ancla + nota, etq, a.simular, estado)

    for etq, res in estado:
        print("  %-64s %s" % (etq, res))
    print()
    if rojo:
        print("  ROJO en %d sitios. No se escribio nada de ese sitio." % rojo)
        return 1
    print("  LAS CELDAS QUEDAN LIMPIAS Y LAS NOTAS VAN DEBAJO, a proposito: asi la")
    print("  celda la puede leer por maquina scripts/loop/vuelta57_puestos_volteados.py")
    print("  sin tropezar con las letras de clase que la propia nota nombra.")
    print("  NINGUN TEXTO VIEJO SE BORRA: todo va tachado y con su fecha al lado.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
