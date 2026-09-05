# -*- coding: utf-8 -*-
r"""vuelta172_tarea3_mutacion_numeracion.py . CASO POSITIVO POR MUTACION DE LAS
DOS GUARDAS DE LA NUMERACION `LD` (TAREA 3 de la vuelta 172), CON NOMBRE DE
ARNES.

POR QUE EXISTE ESTE FICHERO Y NO UN FLAG: la bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS.

LAS DOS GUARDAS QUE EL ENCARGO EXIGE, Y LAS DOS TIENEN QUE CAER:

  (i)  QUE EL NUMERO SE COMPUTE Y NO SE TECLEE. Se le dan a `siguiente_libre`
       mapas de hechas FABRICADOS y se comprueba que el resultado los SIGUE. Si
       alguien sustituyera la funcion por la constante 139, estos casos caen.
  (ii) QUE NINGUN NUMERO POR ENCIMA DEL CORTE TENGA SECCION PROPIA. Se le dan a
       `asignacion_ajena` mapas con y sin intrusos y se comprueba que los ve.

Y ADEMAS, PORQUE UNA GUARDA QUE NO MIRA SU SUJETO NO SIRVE: que el lector de
filas (`filas_de_la_segunda_tanda`) cuenta las filas de par de una pagina
FABRICADA, que NO se traga las filas de cabecera ni las de otras tablas, y que
lee la clase LITERAL en vez de suponerla.

SUJETO CONGELADO (condicion de la vuelta 148): todas las paginas son cadenas
literales de este proceso y todos los mapas de hechas son diccionarios en
memoria. NO se lee el disco y NO se escribe nada, asi que el resultado no
depende de que haya en `docs/plan/` hoy ni dentro de diez vueltas.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: los reales salen de llamar a las
funciones, y la pasada 2 muta cada esperado y exige que el caso CAIGA.

USO:  python scripts/loop/vuelta172_tarea3_mutacion_numeracion.py
"""
import os
import sys

NL = chr(10)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta172_tarea3_numerar_ld as T3   # noqa: E402


def pagina_fabricada(filas, con_tercera=True):
    """Una segunda tanda DE MENTIRA, en memoria. `filas` es
    {etiqueta_de_bloque: [(a, b, clase)]}."""
    L = ["# SEGUNDA TANDA: LA SELECCION DE `OP-L-02`", "",
         "| ruido | de otra tabla |", "|---|---|",
         "| `no_es_un_par` contra `tampoco` | **Z** |", ""]
    for titulo, etiqueta in T3.BLOQUES:
        L.append(titulo)
        L.append("")
        L.append("| par | clase |")
        L.append("|---|:---:|")
        for a, b, c in filas.get(etiqueta, []):
            L.append("| `%s` contra `%s` | **%s** |" % (a, b, c))
        L.append("")
        L.append("| oficio | nodos |")
        L.append("|---|---|")
        L.append("| **diagnosticar** | `x`, `y` |")
        L.append("")
    if con_tercera:
        L.append("# TERCERA TANDA: LO QUE VIENE DESPUES")
        L.append("")
        L.append("| `fuera_de_la_segunda` contra `tanda` | **A** |")
    return NL.join(L)


TRES = {
    "cuadrantes de mercado": [("a1", "b1", "D"), ("a2", "b2", "D"), ("a3", "b3", "A")],
    "ecuacion de valor": [("c1", "d1", "D"), ("c2", "d2", "A")],
    "supervision de la IA, bloque humano": [("e1", "f1", "D")],
}


def main():
    print("=" * 78)
    print("VUELTA 172, TAREA 3: CASO POSITIVO POR MUTACION DE LAS DOS GUARDAS DE LA")
    print("NUMERACION LD")
    print("=" * 78)
    print("")
    casos = []

    print("A) GUARDA (i): EL NUMERO SE COMPUTA Y SIGUE AL MAPA DE HECHAS")
    for hechas, esperado in (({1: ["x"], 2: ["x"], 138: ["x"]}, 139),
                             ({1: ["x"], 138: ["x"], 200: ["x"]}, 201),
                             ({7: ["x"]}, 8),
                             ({1: ["x"], 2: ["x"], 3: ["x"]}, 4),
                             ({}, 1)):
        real = T3.siguiente_libre(hechas)
        print("   hechas con mayor %-4s -> siguiente libre %d"
              % (max(hechas) if hechas else "(vacio)", real))
        casos.append(("A_siguiente_de_%s_es_%d"
                      % (max(hechas) if hechas else "vacio", esperado), real, esperado))
    print("")

    print("B) GUARDA (i), EL LADO QUE IMPORTA: UNA CONSTANTE NO PASARIA ESTO")
    distintos = len(set(T3.siguiente_libre(h) for h in
                        ({138: ["x"]}, {200: ["x"]}, {7: ["x"]}, {3: ["x"]})))
    print("   valores distintos que devuelve para cuatro mapas distintos: %d" % distintos)
    casos.append(("B_devuelve_cuatro_valores_distintos", distintos, 4))
    casos.append(("B_no_es_la_constante_139",
                  T3.siguiente_libre({200: ["x"]}) == 139, False))
    casos.append(("B_no_rellena_huecos",
                  T3.siguiente_libre({1: ["x"], 5: ["x"]}), 6))
    print("   (no rellena huecos: con {1, 5} devuelve 6 y no 2, que es la misma")
    print("    regla que serie_de_registros.siguiente_libre)")
    print("")

    print("C) GUARDA (ii): LA ASIGNACION AJENA SE VE, Y SU AUSENCIA TAMBIEN")
    limpio = {1: ["x"], 138: ["x"]}
    sucio = {1: ["x"], 138: ["x"], 145: ["ajeno.md:9"]}
    dos_sucios = {1: ["x"], 138: ["x"], 145: ["a"], 154: ["b"]}
    print("   sobre un mapa limpio, con corte 138: %s" % T3.asignacion_ajena(limpio, 138))
    print("   sobre uno con un intruso:            %s" % T3.asignacion_ajena(sucio, 138))
    print("   sobre uno con dos:                   %s" % T3.asignacion_ajena(dos_sucios, 138))
    casos.append(("C_el_limpio_no_da_ninguno", len(T3.asignacion_ajena(limpio, 138)), 0))
    casos.append(("C_el_de_un_intruso_da_uno", len(T3.asignacion_ajena(sucio, 138)), 1))
    casos.append(("C_y_lo_nombra", T3.asignacion_ajena(sucio, 138), [145]))
    casos.append(("C_el_de_dos_da_dos", len(T3.asignacion_ajena(dos_sucios, 138)), 2))
    casos.append(("C_sin_corte_usa_el_mayor_y_da_cero",
                  len(T3.asignacion_ajena(sucio)), 0))
    print("   (sin corte explicito usa el mayor del propio mapa, y entonces por")
    print("    definicion no hay nadie por encima: por eso main() le pasa el corte)")
    print("")

    print("D) EL LECTOR DE FILAS CUENTA LO QUE HAY Y NO LO QUE ESPERA")
    p3 = pagina_fabricada(TRES)
    leidas = T3.filas_de_la_segunda_tanda(p3)
    print("   pagina fabricada con 3+2+1 filas de par -> el lector ve %d" % len(leidas))
    casos.append(("D_ve_las_seis", len(leidas), 6))
    casos.append(("D_no_se_traga_el_ruido_de_otra_tabla",
                  any(a == "no_es_un_par" for _e, _i, a, _b, _c in leidas), False))
    casos.append(("D_no_cruza_a_la_tercera_tanda",
                  any(a == "fuera_de_la_segunda" for _e, _i, a, _b, _c in leidas), False))
    casos.append(("D_no_se_traga_la_tabla_de_oficios",
                  any(c == "" for _e, _i, _a, _b, c in leidas), False))
    clases = "".join(c for _e, _i, _a, _b, c in leidas)
    print("   clases leidas, en orden: %s" % clases)
    casos.append(("D_las_clases_se_leen_literales", clases, "DDADAD"))
    bloques = [e for e, _i, _a, _b, _c in leidas]
    casos.append(("D_el_reparto_por_bloque_es_3_2_1",
                  [bloques.count(e) for _t, e in T3.BLOQUES], [3, 2, 1]))
    vacia = T3.filas_de_la_segunda_tanda(pagina_fabricada({}))
    print("   pagina fabricada SIN filas de par -> el lector ve %d" % len(vacia))
    casos.append(("D_una_pagina_sin_pares_da_cero", len(vacia), 0))
    dieciseis = {"cuadrantes de mercado": [("a%d" % k, "b%d" % k, "D") for k in range(8)],
                 "ecuacion de valor": [("c%d" % k, "d%d" % k, "D") for k in range(5)],
                 "supervision de la IA, bloque humano":
                     [("e%d" % k, "f%d" % k, "D") for k in range(3)]}
    casos.append(("D_con_16_fabricadas_ve_16",
                  len(T3.filas_de_la_segunda_tanda(pagina_fabricada(dieciseis))), 16))
    print("")

    print("E) LOS NUMEROS QUE SALDRIAN, ENCADENANDO LAS DOS COSAS")
    hechas_fab = {1: ["x"], 138: ["x"]}
    n0 = T3.siguiente_libre(hechas_fab)
    rango = list(range(n0, n0 + 16))
    print("   con mayor 138 y 16 filas: LD-%d a LD-%d" % (rango[0], rango[-1]))
    casos.append(("E_el_rango_empieza_en_139", rango[0], 139))
    casos.append(("E_y_termina_en_154", rango[-1], 154))
    hechas_otro = {1: ["x"], 90: ["x"]}
    n1 = T3.siguiente_libre(hechas_otro)
    otro = list(range(n1, n1 + 16))
    print("   con mayor 90 y 16 filas:  LD-%d a LD-%d" % (otro[0], otro[-1]))
    casos.append(("E_con_otro_mayor_el_rango_se_mueve", otro[0], 91))
    print("   (si el rango 139 a 154 estuviera tecleado, esta ultima no se moveria)")
    print("")

    print("F) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("G) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, list):
            mutado = esperado + [999]
        else:
            mutado = str(esperado) + "_mutado"
        cae = (real != mutado)
        print("   %-52s %s   (esperado mutado=%r)"
              % (nombre, "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
