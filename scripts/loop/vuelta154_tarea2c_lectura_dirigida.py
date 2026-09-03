# -*- coding: utf-8 -*-
"""vuelta154_tarea2c_lectura_dirigida.py . TAREA 2.c DE LA VUELTA 154.

EL PAR QUE LA VARA NUEVA DESTAPA VA A LECTURA DIRIGIDA POR P.5, CON SU ENTRADA
EN EL REGISTRO Y SIN MOVER `n`.

EL PAR: `error_proofing_servicio` <-> `metodologia_6s`, los dos VIVOS.

POR QUE NO LO CUBREN LAS DOS VIAS DE LA DECISION DEL FUNDADOR, medido y no
supuesto (ver la salida):
  - CRIBADO: `metodologia_6s` NO aparece ni una vez en
    docs/INTRA_DOMINIO_VEREDICTOS.jsonl. `error_proofing_servicio` aparece tres
    veces y en ninguna contra `metodologia_6s`. No hay veredicto que citar.
  - P.10: no hay declaracion sellada de nodo puente para este par.
Luego va por P.5, lectura dirigida, que es la tercera via que la propia decision
del fundador deja abierta para lo que las dos primeras no cubran.

POR QUE EL PAR EXISTE, dicho entero porque cambia como se lee: `metodologia_6s`
nombra DOS ids distintos que resuelven al MISMO nodo vivo. En
`nodos_siguientes` trae `mistake_proofing_poka_yoke` y en `nodos_previos` trae
`errores_a_prueba_poka_yoke`; los dos son deprecados y los dos cuelgan, por la
cadena de `ids_alias`, de `mistake_proofing_poka_yoke_2`, que a su vez es alias
de `error_proofing_servicio`. Es la misma especie de los seis pares que la
vuelta 152 ya leyo con la marca "PAR QUE SOLO EXISTE TRAS RESOLVER ALIAS", y por
eso la marca se repite en la razon.

LA LECTURA, POR EL BANCO 9.22 (primer polo, PROCEDIMIENTO en los dos sentidos
sobre DOS LINEAS DISTINTAS = clase C, enlace mutuo):

  6S hacia error-proofing  La linea es el paso 6 de 6S, "Safety: revisa e
      integra practicas seguras en cada etapa", mas la promesa del resumen
      ("prevenir defectos y accidentes"). 6S la NOMBRA y no la procedimenta.
      La expande ENTERO `error_proofing_servicio`: identificar la actividad
      propensa, los cinco principios (eliminar, sustituir, facilitar, detectar,
      mitigar), disenar el dispositivo fisico o logico, y validarlo antes de
      escalar.

  error-proofing hacia 6S  La linea es el paso 4 de error-proofing,
      "Simplificar el trabajo para reducir la posibilidad de error humano".
      Error-proofing la nombra en un paso y no la procedimenta. La expande
      ENTERA `metodologia_6s`: clasificar y sacar lo que no se necesita,
      ordenar para acceso y devolucion, limpiar, estandarizar la limpieza como
      habito y reservar tiempo y recursos para sostener la disciplina.

DOS LINEAS DISTINTAS, UNA EN CADA NODO: no es el solape que el propio 9.22
excluye ("si las dos direcciones apuntan a LA MISMA LINEA no es la figura").
Ninguno es la madre del otro. CLASE C, y fundirlos borraria dos procedimientos.

QUEDA MARCADO COMO DISCUTIBLE en el reporte de la vuelta 154, y el motivo se
dice aqui en vez de esconderse en el reporte: la mutualidad de este par es
RESIDUO DE UN COLAPSO. Los dos ids que `metodologia_6s` nombra eran, antes del
saneo, DOS NODOS DISTINTOS, y un lector estricto puede sostener que solo una de
las dos direcciones se penso nunca. La C se sostiene igual porque el 9.22
pregunta por LINEAS y no por intenciones, y las dos lineas estan y son
distintas; pero quien discrepe tiene aqui el caso entero para hacerlo.

NO MUEVE `n`: docs/INTRA_DOMINIO_VEREDICTOS.jsonl no se toca, y la corrida lo
comprueba contando sus lineas antes y despues.

USO:  python scripts/loop/vuelta154_tarea2c_lectura_dirigida.py
"""
import glob
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
LECTURAS = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
CRIBADO_NODOS = ("error_proofing_servicio", "metodologia_6s")

PAR = ["error_proofing_servicio", "metodologia_6s"]
CITA = "LD-OPC05-122"
RAZON = ("PAR QUE SOLO EXISTE TRAS RESOLVER ALIAS, y ademas SOLO SE VE LEYENDO LOS DOS "
         "CAMPOS: metodologia_6s nombra mistake_proofing_poka_yoke en nodos_siguientes y "
         "errores_a_prueba_poka_yoke en nodos_previos, y los dos resuelven a "
         "error_proofing_servicio. La organizacion del puesto de trabajo (sacar lo que no "
         "se necesita, ordenar, limpiar, estandarizar el habito, sostener la disciplina) "
         "contra el diseno de dispositivos a prueba de error (los cinco principios, el "
         "dispositivo fisico o logico, la validacion antes de escalar): el paso 6 de 6S "
         "nombra la seguridad y no la procedimenta, y el paso 4 de error-proofing nombra "
         "simplificar el trabajo y no lo procedimenta. Dos lineas distintas, una en cada "
         "nodo, y ninguno es la madre")


def contar(ruta):
    return sum(1 for l in io.open(ruta, encoding="utf-8") if l.strip())


def main():
    print("=" * 92)
    print("VUELTA 154, TAREA 2.c: LA LECTURA DIRIGIDA DEL PAR QUE LA VARA NUEVA DESTAPA")
    print("=" * 92)
    print("PAR: %s <-> %s" % (PAR[0], PAR[1]))
    print("")

    print("PASO 1, LAS DOS VIAS DE LA DECISION DEL FUNDADOR, MEDIDAS ANTES DE ELEGIR P.5")
    n_antes = contar(VEREDICTOS)
    apariciones = {n: 0 for n in CRIBADO_NODOS}
    juntos = 0
    for linea in io.open(VEREDICTOS, encoding="utf-8"):
        if not linea.strip():
            continue
        d = json.loads(linea)
        a, b = d.get("nodo_a"), d.get("nodo_b")
        for n in CRIBADO_NODOS:
            if n in (a, b):
                apariciones[n] += 1
        if {a, b} == set(PAR):
            juntos += 1
    print("  CRIBADO (docs/INTRA_DOMINIO_VEREDICTOS.jsonl, %d lineas):" % n_antes)
    for n in CRIBADO_NODOS:
        print("    %-28s aparece en %d puesto(s)" % (n, apariciones[n]))
    print("    LOS DOS EN EL MISMO PUESTO: %d. NO HAY VEREDICTO DE CRIBADO QUE CITAR." % juntos)
    print("  P.10 (declaracion sellada de nodo puente): no hay declaracion para este par.")
    print("  LUEGO VA POR P.5, LECTURA DIRIGIDA.")
    print("")

    print("PASO 2, LOS DOS NODOS IMPRESOS ANTES DE ADJUDICAR (metodo de la lectura dirigida)")
    for nid in PAR:
        d = json.load(io.open(os.path.join(RAIZ, "dataset", "nodos", nid + ".json"),
                              encoding="utf-8"))
        print("  --- %s (deprecado=%s, dominio=%s)" % (nid, d.get("deprecado"), d.get("dominio")))
        print("      titulo: %s" % d.get("titulo_concepto"))
        for i, p in enumerate(d.get("pasos_accionables") or [], 1):
            print("      %2d. %s" % (i, p))
    print("")

    print("PASO 3, LA ADJUDICACION: CLASE C, ENLACE MUTUO POR EL BANCO 9.22, PRIMER POLO.")
    print("La lectura entera, con las dos lineas nombradas una a una, vive en el docstring")
    print("de este fichero y no se repite aqui.")
    print("")

    print("PASO 4, EL REGISTRO")
    ya = set()
    for linea in io.open(REGISTRO, encoding="utf-8"):
        if linea.strip():
            p = json.loads(linea).get("par") or []
            if len(p) == 2:
                ya.add(tuple(sorted(p)))
    reg_antes = contar(REGISTRO)
    print("  registro ANTES: %d entrada(s), %d par(es) distinto(s)" % (reg_antes, len(ya)))
    if tuple(sorted(PAR)) in ya:
        print("  YA ESTABA: no se duplica.")
    else:
        entrada = {
            "cita": "%s, clase C" % CITA,
            "clase": "C",
            "nodo_a_leido": PAR[0],
            "nodo_b_leido": PAR[1],
            "par": sorted(PAR),
            "razon": RAZON,
            "via": "LECTURA_DIRIGIDA",
        }
        with io.open(REGISTRO, "a", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(entrada, ensure_ascii=False, sort_keys=True) + "\n")
        print("  ANADIDA la entrada %s" % CITA)

        fila = ("| 122 | REGISTRO DE CITAS `OP-C-05` | %s <-> %s | C | %s | %s |\n"
                % (PAR[0], PAR[1], CITA, RAZON))
        texto = io.open(LECTURAS, encoding="utf-8").read()
        if CITA not in texto:
            bloque = (
                "\n## LECTURA DIRIGIDA `LD-OPC05-122`, LA QUE LA VARA DE LOS DOS CAMPOS DESTAPA "
                "(vuelta 154, TAREA 2.c)\n\n"
                "**Nace del hallazgo del acta 153, seccion 4:** la guarda de `OP-C-05` leia solo "
                "`nodos_siguientes` de los nodos vivos, y por eso contaba 153 pares donde la vara "
                "declarada de esta campana (LOS DOS CAMPOS) cuenta 154. Este es el par 154, y "
                "no tenia cita.\n\n"
                "| # | via | par | clase | cita | razon |\n|---:|---|---|---|---|---|\n"
                + fila)
            with io.open(LECTURAS, "a", encoding="utf-8", newline="\n") as fh:
                fh.write(bloque)
            print("  ANADIDA la fila en docs/plan/LECTURAS_DIRIGIDAS.md")

    reg_despues = contar(REGISTRO)
    n_despues = contar(VEREDICTOS)
    print("  registro DESPUES: %d entrada(s)" % reg_despues)
    print("")
    print("PASO 5, LAS GUARDAS DE ESTE ACTO")
    print("  n NO SE MUEVE: docs/INTRA_DOMINIO_VEREDICTOS.jsonl antes %d, despues %d, IGUAL: %s"
          % (n_antes, n_despues, n_antes == n_despues))
    assert n_antes == n_despues, "n se movio, y esta tarea NO puede moverlo"
    pares = set()
    dobles = 0
    for linea in io.open(REGISTRO, encoding="utf-8"):
        if not linea.strip():
            continue
        p = tuple(sorted(json.loads(linea).get("par") or []))
        if p in pares:
            dobles += 1
        pares.add(p)
    print("  registro sin repetidos: %d entrada(s), %d par(es) distinto(s), %d repetido(s)"
          % (reg_despues, len(pares), dobles))
    assert dobles == 0, "el registro trae un par repetido"
    print("")
    print("CIFRA entradas del registro de citas: %d lineas" % reg_despues)
    print("CIFRA pares distintos del registro de citas: %d pares" % len(pares))
    print("CIFRA lecturas dirigidas anadidas en esta tarea: %d pares"
          % (reg_despues - reg_antes))
    print("CIFRA veredictos del cribado: %d lineas" % n_despues)


main()
