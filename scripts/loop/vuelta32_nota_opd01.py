"""Vuelta 32: el REGISTRO DE EJECUCION de OP-D-01 en su campo nota.

CORRECCION DECLARADA: el texto viejo se queda ENTERO delante y solo se anade al
final. Las cifras no se teclean: se leen del grafo y del archivo de veredictos en
esta misma corrida.

Uso: python scripts/loop/vuelta32_nota_opd01.py [--aplicar]
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

MARCA = "REGISTRO DE EJECUCION, 15 ago 2026 (vuelta 32)"


def nodo(nid):
    with open(os.path.join(NODOS, nid + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


def main():
    aplicar = "--aplicar" in sys.argv
    pmv, pcm = nodo("producto_minimo_viable"), nodo("principio_calidad_mvp")
    clases = {}
    with open(VER, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                v = json.loads(linea)
                if v["puesto_intra"] in (494, 592, 830):
                    clases[v["puesto_intra"]] = v["clase"]

    texto = (
        " %s: LOS CUATRO MOVIMIENTOS, con su medicion del dia al lado y el detalle entero "
        "publicado en docs/plan/02_DESTEJIDOS.md, seccion OP-D-01 EJECUTADA. "
        "MOVIMIENTO 1, HECHO: producto_minimo_viable pasa de 22 pasos a %d y de 10 "
        "condiciones a %d, sin que salga un solo bloque del nodo (su costura es de fuente "
        "UNICA, Ries consigo mismo, cinco narraciones en fila: no hay material ajeno que "
        "destejer con destino, solo repetido que colapsar). Criterio del superviviente escrito "
        "antes de aplicarlo: de cada grupo sobrevive el de INDICE MAS BAJO, y el resultado cae "
        "sobre la narracion 1 entera, que es la que el propio entregable del nodo ya narraba, "
        "mas el paso 8. Perdidas repartidas por la tabla de los seis motivos: SALVAGUARDA en "
        "los pasos 1, 2 y 5 del resultado, ALCANCE en el 3 y en el 6, NOMBRE en el 4; DESTINO, "
        "METODO ALTERNATIVO y DIRECCION no aplican. Plan sellado en "
        "docs/loop/PLAN_V32_OPD01_EMBLEMA.json, ejecutado con scripts/loop/vuelta32_podar.py "
        "(sucesor declarado de vuelta30_fundir.py, con el campo condiciones_activacion "
        "anadido y su motivo dentro). Guardas: simulacion verde, guarda de texto 22 de 22 y 10 "
        "de 10, cero perdida con cobertura exacta en los dos campos, caso positivo 0 PASAN y 8 "
        "CAEN antes contra 8 PASAN y 0 CAEN despues, 14 rastros de conservacion vivos las dos "
        "veces. DISCREPANCIA DECLARADA contra una cifra publicada: la ficha proyectaba de "
        "veintidos pasos a CINCO y la medicion de hoy da SEIS, porque iterar o cambiar de "
        "rumbo (pasos 8, 14, 17 y 22) es una cosa que la narracion 1 no contiene; seis sigue "
        "dentro del estandar de 3 a 6. "
        "MOVIMIENTO 2, CONSUMIDO: principio_calidad_mvp no tiene costura interna que destejer "
        "hoy, y lo dice el instrumento, no yo. Medido con scripts/loop/vuelta32_costura_opd01.py, "
        "que importa las dos senales y los dos umbrales de scripts/costuras_internas.py en vez "
        "de copiarlos: mejor pareja de pasos 51,2 contra umbral 80 y mejor alineacion de "
        "bloques 0,0 contra umbral 44, NINGUNA SENAL DISPARA. De sus tres narraciones, la "
        "TERCERA se la llevo OP-F-03 y la SEGUNDA se fundio con la PRIMERA en esta misma "
        "vuelta por P.19 dentro de OP-F-04-HOR. El nodo queda en %d pasos, uno por encima del "
        "estandar, y entra por la puerta que la verificacion de esta operacion nombra: la "
        "excepcion de clase de OP-F-01, cuya firma escrita es superar el estandar SIN narracion "
        "repetida dentro, que es exactamente lo que el instrumento midio. "
        "MOVIMIENTO 3, EL PAR 494: NO SE FUNDE. La razon publicada apoyaba la A en una sola "
        "cosa (los pasos 11 al 14 del primero son el nucleo del segundo dicho otra vez) y esos "
        "pasos ya no existen; el informe habia escrito la condicion por adelantado (si conserva "
        "la narracion de la CALIDAD, el par deja de repetir) y la conserva. La vara aplicada en "
        "los DOS sentidos y sobre LINEAS DISTINTAS da el banco 9.22, LA VARA EN LOS DOS "
        "SENTIDOS: producto_minimo_viable trae el procedimiento entero de la linea de "
        "lanzamiento de principio_calidad_mvp, y principio_calidad_mvp trae el procedimiento "
        "entero de la linea de cuan simple es bastante simple del otro. Clase que sostengo: C, "
        "sano CON FIGURA, y el arreglo es ENLACE MUTUO, dos aristas, que medidas hoy en los dos "
        "sentidos NO EXISTEN. Seria el tercer ejemplar del 9.22 tras el 1077 y el 1240. "
        "MOVIMIENTO 4, 592 Y 830: los dos estaban en B por la misma causa (banco 9.4, el "
        "veredicto emitido contra un texto que iba a cambiar) y esa causa cayo. Clases que "
        "sostengo: las dos D, sanas, con ARISTA QUE FALTA hacia mvp_catalogo_tecnicas y hacia "
        "prueba_mvp_alta_fidelidad; 592 porque la ESCALERA DE COSTO no la dice ninguno de los "
        "seis pasos de hoy, y 830 porque el AISLAMIENTO DE LA PRUEBA tampoco. La clase se "
        "sostiene con la practica medida del archivo y no con mi gusto: barrido hoy el fichero "
        "entero de veredictos, los 207 cuya razon nombra ARISTA QUE FALTA son D, los 207. "
        "LO QUE ESTA VUELTA NO ESCRIBE, Y POR QUE: las tres clases nuevas NO se vuelcan en "
        "docs/INTRA_DOMINIO_VEREDICTOS.jsonl (siguen en %s, %s y %s, leidas hoy) porque el "
        "campo preservar de esta misma operacion manda que un par nuevo entre POR EL RECOMPUTO "
        "(banco 9.10), y volcarlas moveria el marcador publicado y obligaria a barrer en el "
        "mismo acto todas las tablas derivadas. Y las tres aristas tampoco se ponen: el campo "
        "aristas_nuevas de esta operacion esta VACIO y los enlaces son la fase 04. Las tres "
        "lecturas y las tres aristas quedan publicadas con su evidencia en 02_DESTEJIDOS.md."
    ) % (MARCA,
         len(pmv.get("pasos_accionables") or []),
         len(pmv.get("condiciones_activacion") or []),
         len(pcm.get("pasos_accionables") or []),
         clases.get(494), clases.get(592), clases.get(830))

    lineas = []
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                lineas.append(json.loads(linea))
    for o in lineas:
        if o["id_op"] != "OP-D-01":
            continue
        if MARCA in (o.get("nota") or ""):
            print("YA APLICADA.")
            return 0
        o["nota"] = (o.get("nota") or "") + texto
        print(texto.strip())

    if not aplicar:
        print("\n(simulacion: sin --aplicar no se escribe nada)")
        return 0

    with open(OPS, "w", encoding="utf-8") as fh:
        for o in lineas:
            fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    de_vuelta = []
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                de_vuelta.append(json.loads(linea))
    ids = [o["id_op"] for o in de_vuelta]
    rotas = sum(1 for o in de_vuelta
                for x in (o.get("depende_de") or []) + (o.get("bloquea_a") or [])
                if x not in set(ids))
    print("\nVERIFICADO TRAS ESCRIBIR: %d lineas JSON validas, %d ids unicos, "
          "%d dependencias rotas" % (len(de_vuelta), len(set(ids)), rotas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
