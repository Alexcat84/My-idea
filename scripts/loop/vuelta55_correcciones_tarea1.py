# -*- coding: utf-8 -*-
"""vuelta55_correcciones_tarea1.py . LOS DOS REGISTROS DE LAS ADJUDICACIONES DEL
ACTA 54 (TAREAS 1.2 y 1.3 del encargo de la vuelta 55).

MISMA MAQUINA que scripts/loop/vuelta54_correcciones_tarea1.py: cada sitio se
localiza por un ANCLA literal, el texto viejo NO se borra ni se reescribe (se le
ADOSA lo nuevo detras), y el instrumento es IDEMPOTENTE, o sea que re-correrlo
no vuelve a escribir nada. Si un ancla no aparece, o aparece mas de una vez, cae
en rojo y no escribe NADA: un ancla ambigua no es un ancla.

LO QUE ESCRIBE, y nada mas:

  1.2  LA NOTA DE LA ADJUDICACION DE LAS PUERTAS, adosada al registro del tramo
       2 en docs/plan/03_FUSIONES.md, con sus piezas citadas; y la RESPUESTA
       adosada al rotulo del instrumento de las puertas
       (scripts/loop/vuelta48_puertas_en_el_lote.py, el print que dice que
       ninguna regla escrita lo resuelve hoy), CON EL TEXTO VIEJO DELANTE
       ENTERO. LA LOGICA DEL INSTRUMENTO NO SE TOCA: se anaden lineas de print
       y comentario, y el diff por git tiene que enseñarlo.

  1.3  LA NOTA DEL CHOQUE SIN PIEZA, adosada al registro del tramo 2: los actos
       4, 20 y 42 quedan DECLARADOS Y ACUMULAN PARA LA MESA por el carril ya
       escrito. NINGUNO DE LOS TRES SE TOCA.

Uso: python scripts/loop/vuelta55_correcciones_tarea1.py [--simular]
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

FUSIONES = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
PUERTAS = os.path.join(RAIZ, "scripts", "loop", "vuelta48_puertas_en_el_lote.py")

# --------------------------------------------------------------------------
# 1.2.a y 1.3: las dos notas del registro del tramo 2. El ancla es la cabecera
# de la seccion del tramo 2 que la vuelta 54 escribio, y las notas van DETRAS
# de ella, antes de su primer parrafo, para que se lean al abrir la seccion.
# --------------------------------------------------------------------------
ANCLA_TRAMO2 = ("## `OP-U-01`, TRAMO 2: **ABIERTO Y CON VEINTIUN ACTOS FUNDIDOS. "
                "LOS CINCUENTA SON DE FUSION PURA Y NINGUNO PIDE `P.12`** "
                "(20 ago 2026, vuelta 54)\n")

NOTA_PUERTAS = """
> ### ADJUDICACION REGISTRADA: **LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO** (20 ago 2026, vuelta 55, TAREA 1.2 del encargo; adjudicada por el acta de la vuelta 54, pregunta 1)
>
> **La pregunta que esta nota cierra:** cuando el CONTENIDO elige al miembro que **no** es puerta,
> quien manda, `P.8` o la guarda `1B`. **El instrumento de las puertas la traia sin resolver desde
> la vuelta 48** y el tramo 2 la hizo caer dos veces (actos **1** y **15**).
>
> **LA RESPUESTA, POR EXTENSION CITABLE Y SIN DOCTRINA NUEVA: LA GUARDA RESTRINGE Y EL CONTENIDO
> ELIGE ENTRE LO PERMITIDO.** Sus piezas, cada una con su sede:
>
> | la pieza | que aporta | donde vive |
> |---|---|---|
> | **la receta ratificada** | ya tiene esa arquitectura: primero se computan los **VIABLES** por estructura, y entre los viables **elige el contenido** | banco `9.3.1`, ratificada en el acta de la vuelta 50 |
> | **la vara del acta 51, pregunta 3** | la guarda `1B` es obligatoria y define al candidato **LIMPIO**: imposible por puerta es **solo** el acto donde NINGUNA fusion la respeta | acta de la vuelta 51 |
> | **la PRECISION DE LA ESTRELLA** | dice la figura entera: **el preferido que no es viable muere absorbido por el viable** | banco `9.3.1`, adosada en la vuelta 54 |
> | **el acta 50, adjudicacion 3** | en el choque entre la letra y la aritmetica **MANDA LA ARITMETICA**, y el choque **se registra con sus puestos** | acta de la vuelta 50 |
>
> **LA CONSECUENCIA, ESCRITA PARA QUE NO HAYA QUE DEDUCIRLA:** en un acto de dos donde el unico
> candidato limpio es la puerta, **el contenido no tiene entre quien elegir**. **LA PUERTA
> SOBREVIVE**, el choque de conteos **se registra en el motivo** con las cifras impresas, y **las
> piezas propias del absorbido viajan enteras por el reparto**, que es lo que protege el contenido
> que el conteo prefirio. **EJECUTADA EN LA VUELTA 55** sobre los actos **1** y **15**, los dos con
> sus conteos escritos en el motivo del plan sellado.
>
> **LO QUE ESTA ADJUDICACION NO DICE, y se dice para que no se estire:** no toca los **IMPOSIBLES
> POR ESTRUCTURA**, que no son un choque sino un cierre y se siguen DECLARANDO.

> ### ADJUDICACION REGISTRADA: **EL `entregable_esperado` NO ES RAZON, Y LOS ACTOS 4, 20 Y 42 QUEDAN DECLARADOS Y ACUMULAN PARA LA MESA** (20 ago 2026, vuelta 55, TAREA 1.3 del encargo; adjudicada por el acta de la vuelta 54, pregunta 2)
>
> **La pregunta que esta nota cierra:** en un acto de UN SOLO PAR cuyos conteos de contenido chocan,
> el `entregable_esperado` de los nodos vale como PIEZA DECLARADA (alcance del rol), o solo valen
> las razones.
>
> **LA RESPUESTA ES NO, Y POR LA LETRA:** la receta dice *pasos y condiciones, material propio y
> padre declarado **EN LAS RAZONES***, y el `entregable_esperado` es **campo del nodo, no razon**.
> Leerlo como pieza declarada seria **doctrina nueva**, y el bucle no escribe doctrina nueva: la
> decide el fundador si quiere.
>
> **EL CARRIL QUE SI APLICA, Y YA ESTABA ESCRITO:** con conteos que chocan y **CERO** piezas
> declaradas, el acto se **DECLARA** y **ACUMULA PARA LA MESA**, que es el mismo carril del acto que
> las reglas vigentes no pueden fundir (la politica del `703` y la del `604`, el empate sin vara del
> CEO, los imposibles por puerta). **Se declara, se acumula, el bucle sigue.**
>
> | el acto | sus miembros | el choque medido |
> |---|---|---|
> | **4** | `hr_calidad_gestion`, `hr_como_control_de_calidad_gerencial` | pasos **6 contra 4** a un lado, condiciones **1 contra 2** al otro |
> | **20** | `fases_de_retencion_de_clientes`, `ocho_fases_experiencia_cliente` | pasos **3 contra 4** a un lado, condiciones **2 contra 1** al otro |
> | **42** | `fase_acclimate_experiencia_cliente`, `fase_acclimate_mapa_de_proceso` | pasos **5 contra 8** a un lado, condiciones **2 contra 1** al otro |
>
> **NINGUNO DE LOS TRES SE TOCA**, y los tres siguen vivos al cerrar la vuelta 55.
>
> **EL PENDIENTE DE DOCTRINA QUEDA ABIERTO PARA LA MESA, CON NOMBRE PROPIO:** o una **prelacion
> entre conteos de contenido** (que vara manda cuando los pasos y las condiciones apuntan a lados
> distintos), o una **ampliacion de donde vive la pieza declarada** (que campos del nodo, ademas de
> la razon, pueden declarar padre, contencion o alcance del rol). **Las dos son decision de
> fundador.**

"""

# --------------------------------------------------------------------------
# 1.2.b: el rotulo del instrumento de las puertas. TEXTO VIEJO DELANTE ENTERO.
# LA LOGICA NO SE TOCA: solo se anaden lineas de print y un comentario.
# --------------------------------------------------------------------------
ANCLA_PUERTAS = '''    print("ninguna regla escrita hoy. Va como pregunta al auditor, no como decision.")
'''

ADOSADO_PUERTAS = '''    # ROTULO ADOSADO EL 20 ago 2026 (vuelta 55, TAREA 1.2 del encargo). EL TEXTO
    # VIEJO QUEDA DELANTE ENTERO Y NO SE TOCA, porque fue verdad desde la vuelta
    # 48 hasta la 54 y una correccion que tapa lo que corrige no se puede
    # auditar (banco 9.10). LA LOGICA DE ESTE INSTRUMENTO TAMPOCO SE TOCA: aqui
    # solo se anaden lineas de print, y el diff por git lo enseña.
    print("ADOSADO EL 20 ago 2026 (vuelta 55): LA PREGUNTA DE ARRIBA YA ESTA")
    print("CONTESTADA Y ESTE ROTULO QUEDA VIEJO. El acta de la vuelta 54,")
    print("pregunta 1, la adjudico SIN DOCTRINA NUEVA y el registro del tramo 2")
    print("de docs/plan/03_FUSIONES.md la deja escrita: LA GUARDA RESTRINGE Y EL")
    print("CONTENIDO ELIGE ENTRE LO PERMITIDO. Las piezas: la receta ratificada")
    print("elige entre VIABLES; la vara del acta 51 pregunta 3 define al")
    print("candidato limpio; la precision de la estrella del banco 9.3.1 dice la")
    print("figura entera; y el acta 50 adjudicacion 3 manda la aritmetica y")
    print("obliga a registrar el choque. EN UN ACTO DE DOS DONDE EL UNICO")
    print("CANDIDATO LIMPIO ES LA PUERTA, LA PUERTA SOBREVIVE, el choque de")
    print("conteos se registra en el motivo y las piezas propias del absorbido")
    print("viajan enteras por el reparto. Ejecutado en la vuelta 55 sobre los")
    print("actos 1 y 15 del tramo 2. LO QUE NO CAMBIA: los IMPOSIBLES POR")
    print("ESTRUCTURA siguen siendo un cierre y se siguen DECLARANDO.")
'''


def aplicar(ruta, ancla, adosado, etiqueta, simular):
    """Devuelve (estado, detalle). Idempotente: si el adosado ya esta, no toca."""
    with io.open(ruta, encoding="utf-8", newline="") as fh:
        texto = fh.read()
    marca = adosado.strip().splitlines()[0]
    if marca in texto:
        return "YA ESTABA", "idempotente, no se escribe"
    veces = texto.count(ancla)
    if veces == 0:
        return "ROJO", "el ancla NO aparece"
    if veces > 1:
        return "ROJO", "el ancla aparece %d veces: ambigua" % veces
    nuevo = texto.replace(ancla, ancla + adosado)
    if not simular:
        with io.open(ruta, "w", encoding="utf-8", newline="") as fh:
            fh.write(nuevo)
    return "ESCRITO", "%d caracteres adosados detras del ancla" % len(adosado)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("LOS DOS REGISTROS DE LAS ADJUDICACIONES DEL ACTA 54 (vuelta 55)")
    print("MODO %s" % ("SIMULAR" if a.simular else "ESCRIBIR"))
    print("=" * 78)
    print()

    trabajos = [
        ("1.2.a y 1.3, las dos notas del registro del tramo 2",
         FUSIONES, ANCLA_TRAMO2, NOTA_PUERTAS),
        ("1.2.b, la respuesta adosada al rotulo del instrumento de las puertas",
         PUERTAS, ANCLA_PUERTAS, ADOSADO_PUERTAS),
    ]

    rojo = 0
    for etiqueta, ruta, ancla, adosado in trabajos:
        estado, detalle = aplicar(ruta, ancla, adosado, etiqueta, a.simular)
        print("  %-70s %s" % (etiqueta, estado))
        print("      fichero: %s" % os.path.relpath(ruta, RAIZ))
        print("      %s" % detalle)
        print()
        if estado == "ROJO":
            rojo += 1

    if rojo:
        print("  ROJO en %d de %d: NO se escribio nada de lo que fallo." % (rojo, len(trabajos)))
        return 1
    print("  LOS DOS SITIOS EN VERDE. El texto viejo queda entero en los dos: en el")
    print("  registro las notas van DETRAS de la cabecera de la seccion, y en el")
    print("  instrumento el print viejo queda delante y solo se anaden lineas nuevas.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
