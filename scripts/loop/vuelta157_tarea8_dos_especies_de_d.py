# -*- coding: utf-8 -*-
"""vuelta157_tarea8_dos_especies_de_d.py . TAREA 8 DE LA VUELTA 157.

LA CUENTA DE LAS DOS ESPECIES DE D (adjudicacion 6.6 del acta 157).

ESTA TAREA MIDE. NO RECLASIFICA NADA Y NO TOCA UNA CLASE. Lo dice el encargo y
este instrumento no escribe una sola linea en ningun registro: solo lee y cuenta.

QUE SE MIDE, Y POR QUE. La etiqueta D se lee en el archivo como SANO Y DISTINTO,
pero hay pares en D cuyo motivo real es MADRE E HIJO, EL PAR CONTINUA (tercer
caso del 9.22). El acta concede la objecion y ADJUDICA QUE, ANTES DE QUE NADIE
PROPONGA UNA LETRA NUEVA (que seria doctrina nueva y seria PARADA), SE MIDA
CUANTAS D SON DE CADA ESPECIE.

LOS DOS REGISTROS, PORQUE "EL REGISTRO" ES AMBIGUO Y NO SE ADIVINA. El acta 157
nombra como ejemplares los PUESTOS 316, 478, 1424, 1494 y 2066, que son puestos
del CRIBADO (`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, 3.388 filas); pero la
discusion nace en el REGISTRO DE CITAS de OP-C-05
(`docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl`, 154 filas). SE MIDEN LOS DOS Y SE
PUBLICAN LOS DOS, cada uno con su nombre. Medir las dos lecturas cuesta lo mismo
que elegir una a ciegas y no deja la pregunta abierta.

LA VARA, DECLARADA CON SUS LIMITES ANTES DE APLICARLA, que es la mitad del
encargo:

  QUE ES. Una vara LEXICA sobre el campo `razon`: busca marcas literales de cada
  especie y reparte. No lee los nodos, no aplica el 9.22 y no juzga si la clase
  esta bien puesta. Cuenta COMO ESTA ESCRITA la razon, que es exactamente lo que
  la adjudicacion pide antes de discutir una letra.

  LIMITE 1, Y ES EL GRANDE: LAS RAZONES LAS ESCRIBIERON MUCHAS MANOS A LO LARGO
  DE CIENTO CINCUENTA VUELTAS, con vocabulario que cambio por el camino. Una
  razon vieja puede describir madre e hijo sin usar ninguna de estas palabras.
  POR ESO LA CIFRA DE "MADRE E HIJO" ES UNA COTA INFERIOR, NUNCA UN TOTAL.

  LIMITE 2: EL RESIDUO SE PUBLICA, NO SE REPARTE. Las que no traen marca de
  ninguna especie salen en su propio saco, SIN MARCA, y las que traen marcas de
  las dos salen en AMBIGUA. Forzar un binario sobre prosa seria inventarse la
  cifra que esta tarea existe para medir.

  LIMITE 3: LAS MARCAS SE ELIGIERON MIRANDO EL VOCABULARIO DEL ARCHIVO, o sea
  que la vara esta ajustada a lo que ya hay. Sobre razones futuras puede quedarse
  corta.

  CALIBRACION, Y ES LO QUE HACE QUE LA VARA NO SEA UNA OPINION: los CINCO
  puestos que el acta nombra como madre e hijo se buscan uno a uno y se dice
  DONDE CAEN bajo esta vara. Si alguno no cae en MADRE E HIJO, SE DECLARA LA
  DISCREPANCIA en vez de retocar las marcas hasta que salga.

USO:  python scripts/loop/vuelta157_tarea8_dos_especies_de_d.py

--- ADJUDICACION 6.11 DEL ACTA 158 (3 sep 2026): LA CUENTA DE LAS DOS ESPECIES
DE D SE CIERRA AQUI, Y SIN LETRA NUEVA. ESTE INSTRUMENTO NO SE VUELVE A CORRER
COMO ENCARGO ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

QUE MIDIO ESTE INSTRUMENTO Y COMO LO JUZGA EL ACTA: su vara lexica cazo UNO de
los CINCO puestos que el acta nombro, y dejo el 71,9 por ciento del registro y
el 96,6 por ciento del archivo en SIN MARCA. EL EJECUTOR PUBLICO ESO EN VEZ DE
RETOCAR LAS MARCAS HASTA QUE SALIERA, y el acta lo dice con todas sus letras:
ES EXACTAMENTE LO QUE SE LE PIDIO.

LO ADJUDICADO: LA CUENTA CUMPLIO SU ENCARGO Y NO SE REPITE. Lo que dejo medido
es util y se escribe con su limite: LA ESPECIE EXISTE EN LOS DOS REGISTROS, ES
UNA COTA INFERIOR, Y UNA VARA LEXICA NO LA PUEDE MEDIR; SOLO UNA LECTURA.

LO QUE QUEDA PROHIBIDO Y POR QUE: NO SE ABRE LETRA NUEVA (seria doctrina nueva y
seria parada) y NO SE ENCARGA UNA SEGUNDA PASADA LEXICA, que solo repetiria el
mismo residuo. HILO CERRADO.
"""
import io
import json
import os
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
VERED = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

PUESTOS_DEL_ACTA = [316, 478, 1424, 1494, 2066]

# LAS MARCAS DE CADA ESPECIE, escritas aqui para que se puedan discutir una a
# una. Van SIN ACENTOS y en minusculas porque el texto se normaliza igual.
MADRE_E_HIJO = [
    "madre e hijo",
    "el par continua",
    "un solo sentido",
    "un unico sentido",
    "casa propia",
    "9.6.2",
    "cabe entero",
    "el hijo que lo ejecuta",
    "es la madre",
    "tiene hijo",
    "hijo vivo",
    "despliega el paso",
    "despliegan el paso",
    "consume la salida",
]
SANO_Y_DISTINTO = [
    "sano y distinto",
    "sanos y distintos",
    "materias distintas",
    "cada uno expande lo suyo",
    "cada nodo expande lo suyo",
    "puesto 2091",
    "sujeto distinto",
    "sujetos distintos",
    "distinta decision",
    "son distintos",
    "9.6.3",
]
# LAS QUE HAY QUE DESCARTAR ANTES DE BUSCAR, porque contienen una marca DENTRO
# de una frase que dice LO CONTRARIO. Es una guarda contra la propia vara.
NEGACIONES = [
    "ninguno es la madre",
    "no es la madre",
    "no tiene hijo",
    "sin hijo",
]


def limpiar(texto):
    t = unicodedata.normalize("NFKD", texto or "")
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    for n in NEGACIONES:
        t = t.replace(n, " (negado) ")
    return t


def especie(razon):
    t = limpiar(razon)
    mh = [m for m in MADRE_E_HIJO if m in t]
    sd = [m for m in SANO_Y_DISTINTO if m in t]
    if mh and sd:
        return "AMBIGUA", mh, sd
    if mh:
        return "MADRE E HIJO", mh, sd
    if sd:
        return "SANO Y DISTINTO", mh, sd
    return "SIN MARCA", mh, sd


def repartir(filas, clave_id, clave_razon):
    sacos = {"MADRE E HIJO": [], "SANO Y DISTINTO": [], "AMBIGUA": [], "SIN MARCA": []}
    detalle = {}
    for f in filas:
        e, mh, sd = especie(f.get(clave_razon) or "")
        ident = f.get(clave_id)
        sacos[e].append(ident)
        detalle[ident] = (e, mh, sd)
    return sacos, detalle


def publicar(titulo, sacos, total, nomina_completa):
    print("")
    print("-" * 78)
    print(titulo)
    print("-" * 78)
    print("  CIFRA filas en clase D: %d" % total)
    for k in ("MADRE E HIJO", "SANO Y DISTINTO", "AMBIGUA", "SIN MARCA"):
        pct = (100.0 * len(sacos[k]) / total) if total else 0.0
        print("  CIFRA %-16s: %5d  (%.1f por ciento)" % (k, len(sacos[k]), pct))
    suma = sum(len(v) for v in sacos.values())
    print("  suma de los cuatro sacos: %d (tiene que ser %d)" % (suma, total))
    assert suma == total, "los sacos no suman el total: la particion esta rota"
    for k in ("MADRE E HIJO", "AMBIGUA"):
        v = sacos[k]
        print("")
        print("  NOMINA DE %s (%d):" % (k, len(v)))
        muestra = v if nomina_completa else v[:40]
        for i in range(0, len(muestra), 8):
            print("     " + "  ".join(str(x) for x in muestra[i:i + 8]))
        if not nomina_completa and len(v) > len(muestra):
            print("     ... y %d mas (la nomina entera vive en este mismo saco)"
                  % (len(v) - len(muestra)))


def main():
    print("=" * 78)
    print("VUELTA 157, TAREA 8: LAS DOS ESPECIES DE D, CONTADAS")
    print("=" * 78)
    print("")
    print("ESTA TAREA MIDE. NO RECLASIFICA NADA Y NO TOCA UNA CLASE.")
    print("")
    print("LA VARA, EN UNA LINEA: lexica sobre el campo `razon`, con %d marcas de"
          % len(MADRE_E_HIJO))
    print("MADRE E HIJO, %d marcas de SANO Y DISTINTO y %d negaciones que se descartan"
          % (len(SANO_Y_DISTINTO), len(NEGACIONES)))
    print("antes de buscar. NO lee los nodos. La cifra de MADRE E HIJO es una COTA")
    print("INFERIOR, porque las razones viejas describen la especie sin usar estas")
    print("palabras. El residuo se publica en SIN MARCA en vez de repartirse.")

    # --- A) EL REGISTRO DE CITAS DE OP-C-05 ---
    E = [json.loads(x) for x in io.open(REGISTRO, encoding="utf-8") if x.strip()]
    for e in E:
        e["_id"] = e["cita"].split(",")[0].strip()
    D_reg = [e for e in E if e["clase"] == "D"]
    sacos_reg, _det = repartir(D_reg, "_id", "razon")
    print("")
    print("CIFRA filas del registro de citas de OP-C-05: %d" % len(E))
    publicar("A) LAS D DEL REGISTRO DE CITAS DE OP-C-05 (docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl)",
             sacos_reg, len(D_reg), nomina_completa=True)

    # --- B) EL ARCHIVO DEL CRIBADO ---
    V = [json.loads(x) for x in io.open(VERED, encoding="utf-8") if x.strip()]
    D_cri = [v for v in V if v.get("clase") == "D"]
    sacos_cri, det_cri = repartir(D_cri, "puesto_intra", "razon")
    print("")
    print("CIFRA filas del archivo del cribado: %d" % len(V))
    publicar("B) LAS D DEL ARCHIVO DEL CRIBADO (docs/INTRA_DOMINIO_VEREDICTOS.jsonl)",
             sacos_cri, len(D_cri), nomina_completa=False)

    # --- C) LA CALIBRACION CONTRA LOS CINCO PUESTOS QUE EL ACTA NOMBRA ---
    print("")
    print("-" * 78)
    print("C) CALIBRACION: LOS CINCO PUESTOS QUE EL ACTA 157 NOMBRA COMO MADRE E HIJO")
    print("-" * 78)
    aciertos = 0
    for p in PUESTOS_DEL_ACTA:
        if p not in det_cri:
            print("  puesto %-6d NO ESTA ENTRE LAS D DEL CRIBADO" % p)
            continue
        e, mh, sd = det_cri[p]
        if e == "MADRE E HIJO":
            aciertos += 1
        print("  puesto %-6d %-16s marcas MH: %s | marcas SD: %s"
              % (p, e, ", ".join(mh) or "ninguna", ", ".join(sd) or "ninguna"))
    print("  CIFRA de los cinco puestos del acta que esta vara clasifica como MADRE E HIJO: %d de %d"
          % (aciertos, len(PUESTOS_DEL_ACTA)))
    if aciertos < len(PUESTOS_DEL_ACTA):
        print("")
        print("  DISCREPANCIA DECLARADA, Y NO SE ARREGLA RETOCANDO LAS MARCAS: el acta los")
        print("  nombra como madre e hijo leyendolos, y esta vara es lexica. Donde no")
        print("  coinciden, la razon MADRE E HIJO existe pero no esta ESCRITA con estas")
        print("  palabras, que es justo el LIMITE 1 declarado arriba y la prueba de que la")
        print("  cifra es una cota inferior.")

    print("")
    print("-" * 78)
    print("D) LO QUE ESTA CUENTA HABILITA Y LO QUE NO")
    print("-" * 78)
    print("  HABILITA: discutir con cifras si hace falta una letra para 'madre e hijo, el")
    print("  par continua'. La cuenta esta delante, que es lo que la 6.6 exigia ANTES de")
    print("  que nadie proponga nada.")
    print("  NO HABILITA: proponer la letra. Una letra nueva es DOCTRINA NUEVA y eso seria")
    print("  PARADA. Esta tarea no la propone y no la escribe.")
    print("  Y NO SE MOVIO NINGUNA CLASE: este instrumento no abre un fichero para")
    print("  escribir. Solo lee.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
