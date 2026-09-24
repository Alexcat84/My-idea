# -*- coding: utf-8 -*-
"""PRUEBA DE RECALL, paso aparte: genera pasos CONTRARIOS SINTETICOS basados
en pasajes reales de Reason. Se escriben SOLO en docs/fidelidad/pruebas/,
marcados como sinteticos en cada registro. Nunca en dataset/.

La generacion no sabe nada de las pasadas y las pasadas no sabran nada de
esto: mezclar.py los baraja con los reales bajo ids opacos.
"""
import json, os, random, sys
import comun as C

N_CANDIDATOS = 48
N_SINTETICOS = 16

SISTEMA = ("Eres un generador de casos de prueba para un auditor de fidelidad. Respondes SOLO con JSON valido, "
           "sin texto alrededor. Escribes en espanol neutro, sin rayas ni guiones largos.")

def main():
    frags = C.lee_jsonl(os.path.join(C.WORK, "fragmentos.jsonl"))
    reserv = {"F0189", "F0198"}  # los del contrario conocido quedan fuera: son su vara
    cand = [f for f in frags if not f["notas"] and f["palabras"] >= 110 and f["id"] not in reserv and f["cap"] >= 1]
    rnd = random.Random(20260925)
    por_cap = {}
    for f in cand: por_cap.setdefault(f["cap"], []).append(f)
    elegidos = []
    for cap in sorted(por_cap):
        elegidos += rnd.sample(por_cap[cap], min(5, len(por_cap[cap])))
    elegidos = elegidos[:N_CANDIDATOS]
    nodos = C.nodos_reason()
    lista_nodos = "\n".join(f"- {k}: {v['titulo_concepto']}" for k, v in nodos.items())
    ejemplos = []
    for k in list(nodos)[::15][:6]:
        ejemplos += nodos[k]["pasos_accionables"][:2]
    pasajes = "\n\n".join(f"[{f['id']}] (cap. {f['cap']})\n{f['texto']}" for f in elegidos)
    prompt = f"""Tarea: escribir {N_SINTETICOS} pasos CONTRARIOS sinteticos para probar si un auditor los detecta.

Contexto: un catalogo en espanol tiene nodos extraidos del libro de James Reason "Managing the Risks of Organizational
Accidents". Cada nodo tiene "pasos accionables" (consejos breves para un cliente). Un paso es CONTRARIO cuando
aconseja lo que el libro desaconseja o contradice.

Elige {N_SINTETICOS} de los pasajes de abajo en los que el libro toma una postura clara (recomienda, desaconseja,
afirma una relacion, declara algo ineficaz, dificil o preferible), cada uno de un pasaje distinto y repartidos entre
capitulos. Para cada uno escribe UN paso accionable en espanol que contradiga ese pasaje, con el MISMO estilo y
longitud que los pasos reales del catalogo (infinitivo o imperativo, una sola frase, 10 a 25 palabras, sin citar
el libro, sin palabras que delaten la contradiccion como "ignora lo que dice" o "al contrario").

Reparte la dificultad:
- 5 FRANCOS: invierten directamente lo que el pasaje recomienda o afirma.
- 6 SUTILES: suenan razonables y usan el vocabulario del libro, pero mandan por la via que el libro presenta como
  menos prometedora, dificil o ineficaz, o invierten una prioridad, una causalidad o un orden que el libro afirma.
- 5 MUY SUTILES: generalizan de mas, quitan una condicion esencial, o convierten en regla algo que el libro limita,
  de modo que seguir el paso lleve a hacer lo que el libro desaconseja.

Para cada paso, elige como nodo_huesped el nodo del catalogo cuyo tema mejor le cuadre (de la lista), para que el
paso parezca uno mas de ese nodo.

Ejemplos de pasos reales (solo para el estilo):
{chr(10).join('- ' + e for e in ejemplos)}

Nodos del catalogo (id: titulo):
{lista_nodos}

Pasajes (cada linea empieza con su numero Lnnn en el libro):
{pasajes}

Responde SOLO con un array JSON de {N_SINTETICOS} objetos:
[{{"fragmento": "Fxxxx", "lineas": [numeros de las lineas exactas del pasaje que el paso contradice],
  "dificultad": "FRANCO|SUTIL|MUY_SUTIL", "nodo_huesped": "id_del_nodo", "paso": "texto del paso",
  "que_dice_el_libro": "una frase en espanol", "por_que_contradice": "una frase en espanol"}}]"""
    datos, coste = C.llama("sinteticos", "generacion", SISTEMA, prompt)
    out = []
    for i, d in enumerate(datos):
        assert d["nodo_huesped"] in nodos, d
        d = dict(sintetico=True, sid=f"S{i+1:02d}", **d)
        out.append(d)
    ruta = os.path.join(C.PRU, "SINTETICOS_REASON.jsonl")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(json.dumps({"_aviso": "FICHERO DE PRUEBAS. Todos los pasos de este fichero son SINTETICOS y CONTRARIOS a proposito. No son del catalogo. Nunca se copian a dataset/."}, ensure_ascii=False) + "\n")
        for d in out:
            f.write(json.dumps(C.sanea(d), ensure_ascii=False) + "\n")
    print(len(out), "sinteticos", coste)

if __name__ == "__main__":
    main()
