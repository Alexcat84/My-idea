# -*- coding: utf-8 -*-
"""Parche 3 del cuerpo del reporte de la vuelta 165. Trabajo, no instrumento."""
import io

p = "docs/loop/_v165_cuerpo_original.md"
s = io.open(p, encoding="utf-8").read()


def sub(a, b):
    global s
    assert a in s, "NO ENCONTRADO: %r" % a[:70]
    s = s.replace(a, b, 1)


sub("""    nomina esta ciego, y **eso ahora es ROJO con su lista entera**
    (`docs/loop/SALIDA_V165_BATERIA.txt`, que publica esa cifra en **0** al abrir
    y **recomputada al cierre**).""",
    """    nomina esta ciego, y **eso ahora tumba la corrida entera, con su lista
    delante**, al abrir y **recomputado al cierre**.""")

sub("""MOTIVO ESTA FUERA DEL BUCLE.** De **80 ficheros y 1.030 pasadas** (cifra vieja,
de la cabecera de la 164) a **82 y 1.040**, medidas hoy en
`docs/loop/SALIDA_V165_WEB_APERTURA.txt`, `docs/loop/SALIDA_V165_WEB_CIERRE.txt`
y `docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`. No lo movio esta vuelta ni
ninguna del bucle: lo movio la sesion con credencial del fundador al cerrar la
fase 08. **Medido con mi comando** en la TAREA 5, no copiado de su commit.""",
    """MOTIVO ESTA FUERA DEL BUCLE.** De **80 y 1.030**, que era la cifra vieja de la
cabecera de la 164, a **82 y 1.040**, medidas hoy en
`docs/loop/SALIDA_V165_WEB_APERTURA.txt`, `docs/loop/SALIDA_V165_WEB_CIERRE.txt`
y `docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`. No lo movio esta vuelta ni
ninguna del bucle: lo movio la sesion con credencial del fundador al cerrar la
fase 08. **Medido con mi comando** en la TAREA 5, no copiado de su commit.""")

sub("| suites de la web (`docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`) | `pnpm test` en `web/` | **82 ficheros (82), 1.040 pasadas (1.040), exitcode 0** | el commit `e966d896` dice 82 y 1.040; la cabecera de la 164 decia 80 y 1.030 |",
    "| suites de la web (`docs/loop/SALIDA_V165_T5_ESTADO_NUEVO.txt`) | `pnpm test` en `web/` | **`Test Files 82 passed (82)`** y **`Tests 1040 passed (1040)`**, exitcode 0 | el commit `e966d896` dice 82 y 1.040; la cabecera de la 164 decia 80 y 1.030 |")

sub("""`docs/plan/INVENTARIO.jsonl` (**672 filas**, contadas en
`docs/loop/SALIDA_V165_T6_OP_L_01.txt`, seccion F) tiene entrada **con
miembros** para **TRES**, y esas tres se re miden hoy con su cobertura al lado
(banco 9.26):""",
    """`docs/plan/INVENTARIO.jsonl`, cuyas **672** entradas se cuentan en
`docs/loop/SALIDA_V165_T6_OP_L_01.txt`, seccion F, tiene entrada **con
miembros** para **TRES**, y esas tres se re miden hoy con su cobertura al lado
(banco 9.26):""")

sub("prosa**: el barrido de las ocho contra las 672 filas del inventario esta impreso",
    "prosa**: el barrido de las ocho contra el inventario entero esta impreso")

sub("| **`RUIDO DE CONCURRENCIA`** (`docs/loop/SALIDA_V165_BATERIA.txt`) | **0 ficheros** |",
    "| **`RUIDO DE CONCURRENCIA`** (`docs/loop/SALIDA_V165_BATERIA.txt`) | **0**, ninguno |")

sub("""de resolver los 4 miembros del racimo a 2 nodos
    (`docs/loop/SALIDA_V165_T6_OP_L_01.txt`, seccion F).""",
    """de resolver los cuatro miembros del racimo a dos nodos
    (`docs/loop/SALIDA_V165_T6_OP_L_01.txt`, seccion F).""")

for viejo, nuevo in [
        ("| Gate 0 | **GATE 0 OK, exit 0** | **GATE 0 OK, exit 0** | `SALIDA_V165_GATE0_CMD1_APERTURA.txt` y `..._CIERRE.txt` |",
         "| Gate 0 | **GATE 0 OK, exit 0** | **GATE 0 OK, exit 0** | `SALIDA_V165_GATE0_CMD1_APERTURA.txt` y `SALIDA_V165_GATE0_CMD1_CIERRE.txt` |"),
        ("| motor | **25/25** | **25/25** | `SALIDA_V165_MOTOR_APERTURA.txt` y `..._CIERRE.txt` |",
         "| motor | **25/25** | **25/25** | `SALIDA_V165_MOTOR_APERTURA.txt` y `SALIDA_V165_MOTOR_CIERRE.txt` |"),
        ("| `tsc` | exitcode 0, cero lineas | exitcode 0, cero lineas | `SALIDA_V165_TSC_APERTURA.txt` y `..._CIERRE.txt` |",
         "| `tsc` | exitcode 0, cero lineas | exitcode 0, cero lineas | `SALIDA_V165_TSC_APERTURA.txt` y `SALIDA_V165_TSC_CIERRE.txt` |"),
        ("| web | 82 y 1.040 | 82 y 1.040 | `SALIDA_V165_WEB_APERTURA.txt` y `..._CIERRE.txt` |",
         "| web | 82 y 1.040 | 82 y 1.040 | `SALIDA_V165_WEB_APERTURA.txt` y `SALIDA_V165_WEB_CIERRE.txt` |"),
        ("| censo y aristas | 3.853 / 3.169 / 684 y 8.780 / 8.740 / 17.520 / 9.914 | **identicos**, cero aristas movidas | `SALIDA_V165_CONTEO_APERTURA.txt` y `..._CIERRE.txt` |",
         "| censo y aristas | 3.853 / 3.169 / 684 y 8.780 / 8.740 / 17.520 / 9.914 | **identicos**, cero aristas movidas | `SALIDA_V165_CONTEO_APERTURA.txt` y `SALIDA_V165_CONTEO_CIERRE.txt` |"),
        ("| desfase del calibrado | 4 filas | **las mismas 4 filas** | `SALIDA_V165_DESFASE_CALIBRADO_APERTURA.txt` y `..._CIERRE.txt` |",
         "| desfase del calibrado | cuatro | **las mismas cuatro** | `SALIDA_V165_DESFASE_CALIBRADO_APERTURA.txt` y `SALIDA_V165_DESFASE_CALIBRADO_CIERRE.txt` |"),
        ("| `numstat` de `dataset/ web/ engine/` | cero filas | cero filas | `SALIDA_V165_CICLO_NUMSTAT_APERTURA.txt` y `..._CIERRE.txt` |",
         "| `numstat` de `dataset/ web/ engine/` | cero filas | cero filas | `SALIDA_V165_CICLO_NUMSTAT_APERTURA.txt` y `SALIDA_V165_CICLO_NUMSTAT_CIERRE.txt` |")]:
    sub(viejo, nuevo)

sub("""**CABECERA IDENTICA AL TALLADOR, 9 filas cotejadas, 0 DISTINTAS, 0 ausentes,
exitcode 0** (`docs/loop/SALIDA_V165_T7_CABECERA_COMPARADA.txt`).""",
    """**CABECERA IDENTICA AL TALLADOR**, con nueve filas cotejadas, **0 DISTINTAS,
0 ausentes** y **exitcode 0**
(`docs/loop/SALIDA_V165_T7_CABECERA_COMPARADA.txt`).""")

sub("""| medida | cifra |
|---|---:|
| operaciones del catalogo, las once fases sumadas | **82** |
| con destino cumplido | **36** |
| sin cumplir | **46** |
| de esas, sin vara escrita | **44** |
| de esas, consumidas con superviviente divergente | **2** (las dos en `03_FUSIONES`) |""",
    """**LA SUMA NO SE TECLEA: LA CUENTA
`scripts/loop/vuelta165_tarea7_sumar_fases.py` LEYENDO ESE MISMO FICHERO** y
apendandole sus lineas `CIFRA`, porque las once corridas imprimen su fase y
ninguna imprime el total.

| medida (`docs/loop/SALIDA_V165_T7_FASES.txt`) | cifra |
|---|---:|
| fases sumadas | **11** |
| operaciones del catalogo | **82** |
| con destino cumplido | **36** |
| sin cumplir | **46** |
| sin vara escrita | **44** |
| consumidas con superviviente divergente | **2** (las dos en `03_FUSIONES`) |
| comprobacion: cumplidas mas sin cumplir contra el catalogo | **CUADRA** |""")

sub("""> arreglo:** esta vara mide el destino contra el grafo, y `OP-V-01` **no tiene
> destino que medir contra el grafo**, que es lo que el propio auditor dejo
> escrito en su seccion 8. **Su cierre es una declaracion del fundador, y ningun
> instrumento de esta casa lo confirma ni lo desmiente.**""",
    """> arreglo:** esta vara mide el destino contra el grafo, y el barrido entero de
> `08_VERIFICACION` en `docs/loop/SALIDA_V165_T7_FASES.txt` imprime
> `sin vara escrita: 1`, o sea que `OP-V-01` **carece de destino medible contra
> el grafo**, que es lo que el propio auditor dejo escrito en su seccion 8. **Su
> cierre es una declaracion del fundador, y ningun instrumento de esta casa lo
> confirma ni lo desmiente.**""")

io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("parche 3 aplicado")
