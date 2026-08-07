# -*- coding: utf-8 -*-
"""Poda de los dos indices, segun la auditoria fundador+auditor (2026-08-07).

Cada borrado se hace por TITULO EXACTO y con asercion: si un titulo no
aparece, el script se para. Una poda que borra "lo que se parezca" es una
poda que borra lo que no era.
"""
import io
import json
import sys
from pathlib import Path

BASE = Path(r"c:\Users\AlexDesk\Documents\I have an idea")
sys.path.insert(0, str(BASE / "scripts"))
from extraer_mundo import escribir_indice_md  # noqa: E402

# --- COMPRAS -------------------------------------------------------------
BORRAR_COMPRAS = {
    # Bloque 1: gestion de proyecto generica que duplica el nucleo del producto
    "Agrega un colchon de tiempo a tu cronograma, no a cada tarea": "pm_generico",
    "Calcula el tiempo real que tienes, no el que crees tener": "pm_generico",
    "Documenta los supuestos, hitos y avance de tu cronograma": "pm_generico",
    "Divide la compra en tareas pequenas y numeradas": "pm_generico",
    "Mapea las dependencias de tu cronograma con cajas y flechas": "pm_generico",
    "Estima cada tarea con tres escenarios, no a ciegas": "pm_generico",
    "Enfocate en el 20% de tareas que definen el exito del cronograma": "pm_generico",
    "Arma tu presupuesto en pasos y verificalo antes de defenderlo": "pm_generico",
    "Crea un plan de adquisicion y de comunicacion como linea base": "pm_generico",
    "Trata cada compra como un proceso de cinco fases": "pm_generico",
    "Prioriza tu tiempo con una matriz y aprende a decir no": "pm_generico",
    # Bloque 2: frontera con el pack de Riesgos (y "puntua" viola la anti-matriz)
    "Identifica y clasifica los riesgos de tu compra antes de que ocurran": "vive_en_riesgos",
    "Define de antemano que haras con cada riesgo": "vive_en_riesgos",
    "Puntua cada riesgo por probabilidad e impacto": "vive_en_riesgos",
    "Lleva un registro de riesgos con responsable asignado": "vive_en_riesgos",
    "Revisa tu registro de riesgos durante toda la ejecucion": "vive_en_riesgos",
    # Bloque 3: corporativo o mundo equivocado
    "Adopta un sistema de gestion por partes, no de golpe": "mundo_equivocado",
    "Entiende que resuelve un sistema integrado antes de comprarlo": "mundo_equivocado",
    "Calcula tu tarifa real y muestrasela al cliente como valor": "mundo_equivocado",
    "Fija y comunica un cronograma publico del proceso de compra": "mundo_equivocado",
    "Deja explicito que el contratista es independiente, no tu empleado": "mundo_equivocado",
    "Formaliza un periodo de silencio con tu proveedor actual al buscar otro": "mundo_equivocado",
    "Mapea a todos los interesados y que gana cada uno": "mundo_equivocado",
    "Usa los siete desperdicios como checklist de perdidas ocultas": "vive_en_calidad",
    # Bloque 4: baranda de relacion recurrente de Voss
    "Abre la negociacion con un ancla extrema": "ancla_extrema_vs_relacion",
}

# El nodo prometido en la omision del ABC: el puente de Kraljic.
ANADIR_COMPRAS = {
    "titulo": "Conoce tus insumos vitales",
    "aporta": ("Cuales de tus compras pesan de verdad: las de mas valor y las que te "
               "dejan parado si faltan. No es lo mismo lo caro que lo critico."),
    "fase": "planificacion",
    "ancla_de": "Clasifica tu inventario y define que meta persigues",
}

# --- ENTREGA -------------------------------------------------------------
BORRAR_ENTREGA = {
    "Agrupar productos en cargas unitarias": "escala_flota",
    "Asegurar pallets y cargas de freight": "escala_flota",
    "Optimizar rondas de reparto por densidad": "escala_flota",
    "Cumplir la normativa para envios con hielo seco": "mini_curso_dg",
    "Clasificar baterias antes de enviarlas": "mini_curso_dg",
    "Aplicar la excepcion para baterias de litio pequenas": "mini_curso_dg",
    "Marcar correctamente envios con mercancia regulada": "mini_curso_dg",
    "Cumplir con la declaracion y capacitacion para mercancias peligrosas": "mini_curso_dg",
    "Elegir el refrigerante segun la temperatura objetivo": "vertical_futura",
}

# Regla de datos locales: ninguna cifra que cambie por courier o pais va cableada.
EDITAR_ENTREGA = {
    "Calcular el peso dimensional antes de cotizar": {
        "aporta": ("Multiplica largo por ancho por alto y divide entre el divisor que "
                   "use tu courier: eso da el peso facturable, que suele ser mayor que "
                   "el peso real. Pregunta cual es tu divisor, porque cambia entre "
                   "couriers y entre paises."),
    },
    "Probar tu empaque gratis antes de escalar envios": {
        "titulo": "Prueba tu empaque antes de escalar envios",
        "aporta": ("Valida que el empaque resiste el transporte antes de comprometerte "
                   "a volumen. Algunos couriers ofrecen esa prueba sin costo: pregunta "
                   "al tuyo que ofrece."),
    },
}


def sin_acentos(t):
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", t)
                   if unicodedata.category(c) != "Mn")


def indice_por_titulo(lista):
    return {sin_acentos(c["titulo"]): i for i, c in enumerate(lista)}


def podar(mundo, borrar, editar=None, anadir=None):
    ruta = BASE / "packs" / mundo / "indice" / "_indice_propuesto.json"
    lista = json.loads(ruta.read_text(encoding="utf-8"))
    antes = len(lista)
    porTitulo = indice_por_titulo(lista)

    faltan = [t for t in borrar if t not in porTitulo]
    if faltan:
        print(f"ERROR en {mundo}: estos titulos a borrar NO existen:")
        for t in faltan:
            print(f"   - {t}")
        sys.exit(1)

    fuera = {porTitulo[t] for t in borrar}
    borrados = [{"titulo": lista[i]["titulo"], "motivo": borrar[sin_acentos(lista[i]["titulo"])]}
                for i in sorted(fuera)]
    lista = [c for i, c in enumerate(lista) if i not in fuera]

    editados = []
    if editar:
        porTitulo = indice_por_titulo(lista)
        for t, cambios in editar.items():
            if t not in porTitulo:
                print(f"ERROR en {mundo}: el titulo a editar NO existe: {t}")
                sys.exit(1)
            c = lista[porTitulo[t]]
            editados.append({"antes": c["titulo"], **cambios})
            c.update(cambios)

    if anadir:
        porTitulo = indice_por_titulo(lista)
        ancla = sin_acentos(anadir["ancla_de"])
        if ancla not in porTitulo:
            print(f"ERROR en {mundo}: no existe el ancla {anadir['ancla_de']}")
            sys.exit(1)
        hermano = lista[porTitulo[ancla]]
        lista.append({
            "titulo": anadir["titulo"],
            "aporta": anadir["aporta"],
            "fase": anadir["fase"],
            "fuentes": hermano["fuentes"],
            "fuente_label": hermano["fuente_label"],
            # Se ancla al mismo fragmento que su hermano del ABC: es de donde
            # nace la omision que este nodo viene a tapar.
            "chunks": hermano["chunks"],
            "fundidos_de": [anadir["titulo"]],
            "anadido_a_mano": True,
        })

    ruta.write_text(json.dumps(lista, ensure_ascii=False, indent=2), encoding="utf-8")
    cab = (f"{len(lista)} conceptos, tras la poda de la auditoria "
           f"(de {antes}: {len(borrados)} borrados"
           + (f", {len(editados)} editados" if editados else "")
           + (", 1 anadido" if anadir else "") + ").")
    escribir_indice_md(mundo, lista, ruta.parent, cab)

    (ruta.parent / "_poda_auditoria.json").write_text(
        json.dumps({"borrados": borrados, "editados": editados,
                    "anadidos": [anadir["titulo"]] if anadir else []},
                   ensure_ascii=False, indent=2), encoding="utf-8")

    from collections import Counter
    fases = Counter(c["fase"] for c in lista)
    print(f"\n== {mundo}: {antes} -> {len(lista)}")
    for f in ("ideacion", "validacion", "planificacion", "ejecucion"):
        print(f"     {f:<14} {fases.get(f, 0)}")
    return len(borrados)


n1 = podar("compras", BORRAR_COMPRAS, anadir=ANADIR_COMPRAS)
n2 = podar("entrega", BORRAR_ENTREGA, editar=EDITAR_ENTREGA)
print(f"\nborrados: compras {n1}, entrega {n2}")
