# -*- coding: utf-8 -*-
"""vuelta56_tallar_perdidas_v55.py . TALLA LA TABLA DE LAS PERDIDAS NOMBRADAS DE
LA VUELTA 55 DESDE LOS PLANES SELLADOS, CON SU ESPECIE, PARA QUE NINGUNA CELDA
SE TECLEE.

POR QUE EXISTE, y el motivo esta medido y no supuesto: el acta de la vuelta 55,
seccion 3, nombra como CAIDA DE REPORTE que el `D8` del reporte de aquella
vuelta llamo DE CONDICIONES a las CUATRO perdidas, cuando la del acto 45 es de
un PARAMETRO DE PASO. La TAREA 1.2 del encargo de la vuelta 56 manda registrar
la correccion donde la cifra podria heredarse. Y la regla 1 del EJECUTOR dice
que toda tabla cuyo contenido exista en un plan sellado SE GENERA DESDE EL PLAN
y se pega entera, con el comando citado al lado: por eso la especie de cada
perdida NO se teclea aqui, SE LEE del plan.

COMO SE LEE LA ESPECIE, mecanicamente y sin categoria por defecto: dentro del
trozo de `nota_del_reparto` que empieza en PERDIDA NOMBRADA se busca cual de
las dos formas nombra la pieza perdida.

    dice "su condicion"      -> LA PERDIDA ES DE CONDICIONES
    dice "el paso"           -> LA PERDIDA ES DE PARAMETRO DE PASO

SI LAS DOS APARECEN, O NINGUNA, SALE ROJO CON EL ACTO NOMBRADO y no se emite la
tabla. Una clasificacion silenciosa es exactamente la especie de caida que este
instrumento existe para no repetir, y por eso no hay rama por defecto.

Y LA FRASE SELLADA VIAJA CON LA CELDA: la tabla lleva, en su ultima columna, el
trozo VERBATIM del plan que sostiene la clasificacion, recortado por maquina.
Quien audite no tiene que creerle a la etiqueta: tiene la frase al lado.

DE SOLO LECTURA. No escribe ningun fichero: imprime.

AMPLIADO EL MISMO DIA, ANTES DE QUE NINGUNA PAGINA CITARA SUS CIFRAS: sirve
para CUALQUIER vuelta y CUALQUIER lista de lotes, porque la vuelta 56 tiene sus
propias perdidas que contar y duplicar el instrumento para cambiar dos cadenas
seria fabricar un hermano gemelo sin motivo. La ampliacion NO toca la
aritmetica: solo saca a la linea de comandos el numero de vuelta y los lotes.

Uso:
  python scripts/loop/vuelta56_tallar_perdidas_v55.py --vuelta 55 --lotes T1,A,B
  python scripts/loop/vuelta56_tallar_perdidas_v55.py --vuelta 56 --lotes A,B,C
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
MARCA = "PERDIDA NOMBRADA"

# MISMA CORRECCION QUE LA DE scripts/loop/tallar_planes_del_tramo.py, aplicada
# aqui el mismo dia y por la misma medicion (vuelta 60, lotes B y C del tramo
# 5): de las SEIS apariciones del token, CINCO viven en frases que dicen que la
# perdida que la RAZON nombro esta REPUESTA por esta fusion, o sea lo contrario
# de una perdida. Una aparicion NO cuenta si en su misma frase el plan dice SE
# REPONE, SE REPONEN o NO SE PIERDE. El plan sellado no se toca.
# LO QUE SIGUE SIN ARREGLARSE, dicho y no callado: este instrumento solo ve las
# perdidas que llevan el token, asi que sigue contando de menos las que el plan
# nombra con otras palabras. No se arregla a ojo.
NO_ES_PERDIDA = ("SE REPONE", "SE REPONEN", "NO SE PIERDE")


def es_perdida_real(trozo):
    fin = trozo.find(".")
    frase = trozo[:fin if fin > 0 else len(trozo)]
    return not any(x in frase for x in NO_ES_PERDIDA)


def especie(trozo):
    """Devuelve (etiqueta, causa) o (None, motivo del rojo). Sin rama por defecto."""
    cond = "su condicion" in trozo
    paso = "el paso" in trozo
    if cond and paso:
        return None, "el trozo nombra condicion Y paso: ambiguo"
    if cond:
        return ("DE CONDICIONES",
                "el `INCISO` de condiciones no existe en el instrumento"), None
    if paso:
        return ("DE PARAMETRO DE PASO",
                "el inciso MENTIRIA contra la unica restriccion del paso que protege"), None
    return None, "el trozo no nombra ni condicion ni paso"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", default="55")
    ap.add_argument("--lotes", default="T1,A,B")
    a = ap.parse_args()
    V, LOTES = a.vuelta, [x.strip() for x in a.lotes.split(",") if x.strip()]
    PLAN = "PLAN_V%s_OPU01_LOTE_%%s.json" % V
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("LAS PERDIDAS NOMBRADAS DE LA VUELTA %s, TALLADAS DE LOS PLANES SELLADOS" % V)
    print("=" * 78)
    print()

    filas, rojo, saltados = [], [], []
    for L in LOTES:
        p = os.path.join(LOOP, PLAN % L)
        plan = json.load(io.open(p, encoding="utf-8"))
        for act in plan["actos"]:
            nota = act["nota_del_reparto"]
            if MARCA not in nota:
                continue
            # SEGUNDA CORRECCION DE LA VUELTA 60, Y VA CON LA MEDICION QUE LA
            # SOSTIENE PORQUE EL PRIMER INTENTO DE JUSTIFICARLA FUE MIO Y ESTABA
            # MAL, y un razonamiento equivocado descartado tambien es registro.
            # LO QUE HABIA: el trozo que se clasificaba era LA COLA ENTERA de la
            # nota desde el token, asi que arrastraba frases de OTROS asuntos.
            # Medido en el lote B acto 19 del tramo 5: la cola llegaba hasta
            # "es su condicion 2", una frase que habla de la cobertura de
            # condiciones y no de la perdida, y el instrumento salia AMBIGUO por
            # culpa de eso. El propio docstring de arriba dice que la especie se
            # lee de la FRASE, asi que se acota a la frase, que es ademas la
            # misma que ya se publica en la ultima columna.
            # LO QUE CREI Y NO ERA: llegue a revertir esta cota pensando que
            # rompia la clasificacion del lote A de la vuelta 59. LO COMPROBE
            # CORRIENDO EL INSTRUMENTO SIN NINGUN CAMBIO MIO (git stash) y es
            # FALSO: los actos 1, 4 y 7 de aquel lote YA SALIAN ROJO ANTES, con
            # otro motivo (el trozo no nombra ni condicion ni paso), y la vuelta
            # 59 nunca llego a correr este tallador, comprobado porque no existe
            # docs/loop/SALIDA_V59_TALLAR_PERDIDAS.txt. La cota NO cambia nada
            # para el lote A y SI arregla el lote B, asi que se queda. Aquel
            # ROJO del lote A es anterior, es de otra especie y queda declarado.
            cola = nota[nota.index(MARCA):]
            corte = cola.find(".")
            trozo = cola[:corte if corte > 0 else len(cola)]
            if not es_perdida_real(trozo):
                saltados.append((L, act["orden"], trozo.split(".")[0].strip()[:150]))
                continue
            esp, mal = especie(trozo)
            if esp is None:
                rojo.append((L, act["orden"], mal))
                continue
            # la frase sellada que sostiene la clasificacion, recortada por maquina
            frase = trozo.split(".")[0].strip()
            if len(frase) > 320:
                frase = frase[:317] + "..."
            filas.append({"lote": L, "orden": act["orden"], "muere": act["absorbidos"][0],
                          "especie": esp[0], "causa": esp[1], "frase": frase})

    print("  planes leidos       : %s" % ", ".join(PLAN % L for L in LOTES))
    print("  perdidas encontradas: %d" % (len(filas) + len(rojo)))
    if saltados:
        print("  APARICIONES DEL TOKEN QUE NO SON PERDIDA (la frase dice que se repone): %d"
              % len(saltados))
        for L, n_, fr in saltados:
            print("     lote %s acto %d: %s" % (L, n_, fr))
    if rojo:
        print()
        for L, n, mal in rojo:
            print("  [ROJO] lote %s acto %d: %s" % (L, n, mal))
        print("  NO SE EMITE LA TABLA.")
        return 1
    cuenta = {}
    for f in filas:
        cuenta[f["especie"]] = cuenta.get(f["especie"], 0) + 1
    print("  por especie         : %s" % dict(sorted(cuenta.items())))
    print()

    print("--- TABLA: LAS PERDIDAS NOMBRADAS DE LA VUELTA %s, CON SU ESPECIE ---" % V)
    print()
    print("| acto | lote | el nodo que muere | **ESPECIE** | por que se perdio | la frase del plan sellado que lo dice |")
    print("|---:|:---:|---|---|---|---|")
    for f in sorted(filas, key=lambda x: x["orden"]):
        print("| **%d** | %s | `%s` | **%s** | %s | *%s* |"
              % (f["orden"], f["lote"], f["muere"], f["especie"], f["causa"], f["frase"]))
    print("| **suma** | | | **%s** | | |"
          % ", ".join("%d %s" % (v, k) for k, v in sorted(cuenta.items())))
    print()
    print("  actos con perdida: %d | de condiciones: %d | de parametro de paso: %d"
          % (len(filas), cuenta.get("DE CONDICIONES", 0),
             cuenta.get("DE PARAMETRO DE PASO", 0)))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
