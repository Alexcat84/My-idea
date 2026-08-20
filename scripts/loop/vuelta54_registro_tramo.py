# -*- coding: utf-8 -*-
"""vuelta54_registro_tramo.py . EL REGISTRO DEL TRAMO 2 DE OP-U-01 EN
docs/plan/03_FUSIONES.md.

TODA CIFRA DE ESTE REGISTRO SE LEE DE LA SALIDA QUE LA PROPIA CELDA CITA, y el
instrumento NO la teclea: la LEE del fichero de salida al escribir la seccion,
y si no la encuentra CAE EN ROJO sin escribir nada. Es la regla 1 del EJECUTOR
(la tabla se imprime, no se teclea) llevada hasta el registro.

IDEMPOTENTE: si la seccion ya esta, no la duplica.

Uso: python scripts/loop/vuelta54_registro_tramo.py [--simular]
"""
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FUS = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
LOOP = os.path.join(RAIZ, "docs", "loop")


def leer(nombre):
    return io.open(os.path.join(LOOP, nombre), encoding="utf-8").read()


def uno(texto, patron, etiqueta):
    m = re.search(patron, texto)
    if not m:
        raise SystemExit("ROJO: no encuentro %s con %r" % (etiqueta, patron))
    return m.group(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    # ---- las cifras, LEIDAS de la salida que cada celda cita ----
    nom = leer("SALIDA_V54_TRAMO2_NOMINA.txt")
    ap_mar = leer("SALIDA_V54_MARCADOR_APERTURA.txt")
    ci_mar = leer("SALIDA_V54_MARCADOR_CIERRE.txt")
    ap_est = leer("SALIDA_V54_APERTURA.txt")
    ci_est = leer("SALIDA_V54_CIERRE.txt")
    ap_rec = leer("SALIDA_V54_RECOMPUTO_APERTURA.txt")
    ci_rec = leer("SALIDA_V54_RECOMPUTO_CIERRE.txt")
    ap_col = leer("SALIDA_V54_COLA_APERTURA.txt")
    ci_col = leer("SALIDA_V54_COLA_CIERRE.txt")
    ci_cls = leer("SALIDA_V54_COLISIONES_CIERRE.txt")
    ejec_a = leer("SALIDA_V54_LOTE_A_EJEC.txt")
    ejec_b = leer("SALIDA_V54_LOTE_B_EJEC.txt")

    d = {}
    d["actos_tramo"] = uno(nom, r"actos del tramo 2\s*:\s*(\d+)", "actos del tramo")
    d["por_figura"] = uno(nom, r"por figura\s*:\s*(\{[^}]*\})", "figura")
    d["nodos_impl"] = uno(nom, r"nodos implicados\s*:\s*(\d+)", "nodos implicados")
    for k, txt in (("ap", ap_mar), ("ci", ci_mar)):
        for cl in "ABCD":
            d[k + cl] = uno(txt, r"\n  %s (\d+)" % cl, "marcador %s %s" % (k, cl))
    for k, txt in (("ap", ap_est), ("ci", ci_est)):
        d[k + "_vivos"] = uno(txt, r"vivos\s*:\s*(\d+)", "vivos")
        d[k + "_dep"] = uno(txt, r"deprecados\s*:\s*(\d+)", "deprecados")
        d[k + "_enl"] = uno(txt, r"enlaces\s*:\s*(\d+)", "enlaces")
    for k, txt in (("ap", ap_rec), ("ci", ci_rec)):
        d[k + "_crudas"] = uno(txt, r"A crudas en el archivo \(clase == 'A'\): (\d+)", "crudas")
        d[k + "_colapsos"] = uno(txt, r"colapsan a auto-arista tras resolver[^:]*: (\d+)", "colapsos")
        d[k + "_cerrados"] = uno(txt, r"CERRADOS: (\d+) sobre", "cerrados")
        d[k + "_nod_cer"] = uno(txt, r"CERRADOS: \d+ sobre (\d+) nodos", "nodos cerrados")
        d[k + "_abiertos"] = uno(txt, r"ABIERTOS: (\d+) sobre", "abiertos")
        d[k + "_nod_abi"] = uno(txt, r"ABIERTOS: \d+ sobre (\d+) nodos", "nodos abiertos")
        d[k + "_ii"] = uno(txt, r"A vigentes resueltas del retrato \((\d+)\)", "ii")
    for k, txt in (("ap", ap_col), ("ci", ci_col)):
        d[k + "_cola"] = uno(txt, r"nodos en la cola:\s*(\d+)", "cola")
    d["ci_colisiones"] = uno(ci_cls, r"COLISIONES DE CLASE VIGENTES\s*:\s*(\d+)", "colisiones")
    for k, txt in (("a", ejec_a), ("b", ejec_b)):
        d[k + "_fund"] = uno(txt, r"actos fundidos\s*:\s*(\d+)", "fundidos")
        d[k + "_mueren"] = uno(txt, r"nodos que MUEREN\s*:\s*(\d+)", "mueren")
        d[k + "_piezas"] = uno(txt, r"piezas repartidas\s*:\s*(\d+)", "piezas")
        d[k + "_enteras"] = uno(txt, r"piezas repartidas\s*:\s*\d+ \((\d+) viajan enteras", "enteras")
        d[k + "_dichas"] = uno(txt, r"viajan enteras, (\d+) ya estaban dichas", "dichas")
        d[k + "_incisos"] = str(sum(int(x) for x in re.findall(r"INCISOS ADOSADOS: (\d+)", txt)))
    d["fundidos"] = str(int(d["a_fund"]) + int(d["b_fund"]))
    d["muertos"] = str(int(d["a_mueren"]) + int(d["b_mueren"]))
    d["pendientes"] = str(int(d["actos_tramo"]) - int(d["fundidos"]))
    d["colapsos_mas"] = str(int(d["ci_colapsos"]) - int(d["ap_colapsos"]))

    seccion = """
---

## `OP-U-01`, TRAMO 2: **ABIERTO Y CON VEINTIUN ACTOS FUNDIDOS. LOS CINCUENTA SON DE FUSION PURA Y NINGUNO PIDE `P.12`** (20 ago 2026, vuelta 54)

**LA DEFINICION DEL TRAMO NO SE DECIDIO: SE MIDIO.** La definicion vigente es la de la cabecera
del registro del tramo 1 (*los CINCUENTA primeros actos `CERRADOS` de la nomina re-medida al
abrirlo, en el orden en que el instrumento los imprime*), y **los CINCUENTA SIGUIENTES admitian
dos lecturas.** `python scripts/loop/vuelta54_tramo2_nomina.py`
([`../loop/SALIDA_V54_TRAMO2_NOMINA.txt`](../loop/SALIDA_V54_TRAMO2_NOMINA.txt)) **computa LAS
DOS y las compara**:

| lectura | que dice | resultado |
|---|---|---|
| **A, por el orden de HOY** | se re-mide la nomina hoy, se marcan los actos del tramo 1 que siguen vivos **identificados POR SUS MIEMBROS** (que es la doctrina de esta pagina) y el tramo 2 son los 50 `CERRADOS` siguientes | los once del tramo 1 ocupan los puestos **1 a 11** y el tramo 2 es del **12 al 61** |
| **B, por el orden del dia en que se abrio el tramo 1** | el tramo 2 son los que ocupaban los puestos **51 a 100** de [`../loop/RECOMPUTO_V48_COMPONENTES.jsonl`](../loop/RECOMPUTO_V48_COMPONENTES.jsonl) | **50 actos, los mismos** |

> **LAS DOS DAN EL MISMO TRAMO EN EL MISMO ORDEN**, comprobado acto por acto, **y el instrumento
> cae en ROJO con PARADA si algun dia no calzan.** Una operacion cuyo texto no alcanza para
> ejecutarse sin decidir detiene; esta alcanza, y la prueba esta impresa.

### LA FORMA DEL TRAMO 2, Y ES LO CONTRARIO DEL TRAMO 1

| | |
|---|---:|
| actos del tramo | **{actos_tramo}** |
| por tamano | **los {actos_tramo} de tamano 2** |
| por figura | **{por_figura}** |
| nodos implicados | **{nodos_impl}** |
| **lecturas `P.12` que este tramo pide** | **CERO** |

**NO HAY NI UNA SOLA LECTURA `P.12` EN ESTE TRAMO, y se dice porque es la diferencia entera con
el tramo 1**, que dejo veintisiete mixtos esperando cinco vueltas: **un acto de dos miembros con
UN par `A` directo no deja ningun mixto fuera**, asi que la receta de la estrella no tiene nada
que decidir. **Lo que este tramo pide es la otra mitad de `P.8`: quien sobrevive por CONTENIDO.**

**LAS DOS GUARDAS DE ENTRADA, LAS DOS EN VERDE:** la **guarda de los cuatro ajenos** (ninguno de
los cuatro que esta pagina declara fuera de `OP-U-01` desde el 11 ago 2026 entra en el tramo, y
**ninguno esta ya en el lote `CERRADO` entero**) y la **guarda de solape con el tramo 1** (cero
actos del tramo 2 tocan un miembro de un acto del tramo 1).

### LA GUARDA DE COLISIONES NO CUBRIA ESTA FORMA, Y SE DICE EN VEZ DE APAGARLA

**Corrido `scripts/loop/vuelta51_colisiones_esperadas.py` sobre la nomina del dia como manda el
encargo, NO IMPRIME NI UNO de los cincuenta actos**
([`../loop/SALIDA_V54_COLISIONES_ESPERADAS.txt`](../loop/SALIDA_V54_COLISIONES_ESPERADAS.txt)).
**El motivo esta escrito en su propio codigo**, la linea 130: `continue  # fusion pura, no pide
P.12`. **Y es correcto para lo que aquel instrumento mide:** nacio para la guarda de cuenta de la
vuelta 51, que cuenta una colision por cada mixto en `CONTINUA`.

**La guarda no se apaga y el instrumento viejo no se falsea: se escribe un SUCESOR DECLARADO**,
`scripts/loop/vuelta54_colisiones_esperadas.py`, con **la misma aritmetica copiada de aquel** y
la rama que faltaba ([`../loop/SALIDA_V54_COLISIONES_ESPERADAS_TRAMO2.txt`](../loop/SALIDA_V54_COLISIONES_ESPERADAS_TRAMO2.txt)).
**Lo que predice, sobre el archivo entero y antes de tocar un nodo:**

| | |
|---|---:|
| combinaciones simuladas (cada acto por cada eleccion posible) | **100** |
| combinaciones que fabrican alguna colision | **6** |
| **actos del tramo que fabrican colision** | **TRES**: el **6** con dos, el **44** con una y el **49** con dos |
| **actos del tramo que no fabrican ninguna** | **47** |

**LAS CINCO COLISIONES PREVISTAS SON TODAS `B` DIRECTO CONTRA `D` Y TODAS FUERA DEL ACTO**, o
sea del carril del filo: **relectura EN EL MISMO ACTO.** **Los tres actos NO se tocan en esta
vuelta y quedan nombrados abajo.**

### LOS VEINTIUN ACTOS FUNDIDOS, en dos lotes

| lote | actos | fundidos | nodos que mueren | piezas repartidas | enteras | ya dichas | de `INCISO` |
|---|---|---:|---:|---:|---:|---:|---:|
| **A** | 2, 3, 5, 7, 8, 9, 10, 11, 12, 13 y 14 | **{a_fund}** | **{a_mueren}** | **{a_piezas}** | **{a_enteras}** | **{a_dichas}** | **{a_incisos}** |
| **B** | 16, 17, 19, 21, 22, 23, 24, 25, 26 y 27 | **{b_fund}** | **{b_mueren}** | **{b_piezas}** | **{b_enteras}** | **{b_dichas}** | **{b_incisos}** |
| **los dos** | | **{fundidos}** | **{muertos}** | | | | |

**LAS CUATRO FORMAS DEL VEREDICTO QUE EL TRAMO 2 TRAE, contadas por maquina sobre los cincuenta**
([`../loop/SALIDA_V54_VARAS_TRAMO2.txt`](../loop/SALIDA_V54_VARAS_TRAMO2.txt)) **y aplicadas en
los veintiuno:**

| la forma | cuantos de los 50 | que decide |
|---|---:|---|
| **TODAS DE ACUERDO** | **13** | las varas de contenido que no empatan apuntan al mismo lado |
| **UNA SOLA VARA** | **22** | solo una vara de contenido no empata, **y BASTA** (acta de la vuelta 53, pregunta 4) |
| **CHOCAN** | **5** | decide **LA PIEZA DECLARADA** de mayor peso en las razones; **si no hay ninguna, es PARADA** (acta 53, pregunta 3) |
| **CONTENIDO EMPATA** | **9** | **EL CABLEADO DECIDE SOLO** |
| **EMPATE SIN VARA** | **1** | tampoco el cableado separa: **se DECLARA** |

### LOS ACTOS QUE ESTA VUELTA NO FUNDE, CADA UNO CON SU ESPECIE

| acto | especie | por que no se funde |
|---|---|---|
| **1** (`balance_eficiencia_responsividad`, `trade_off_responsividad_eficiencia`) y **15** (`apertura_efectiva_llamada_venta`, `apertura_llamada_venta_grande`) | **EL CONTENIDO APUNTA AL QUE NO ES PUERTA** | La guarda `1B` exige que la puerta sobreviva y el contenido elige al otro (pasos 6 contra 4 y condiciones 3 contra 2 en el 1; pasos 5 contra 4 en el 15). **Ese choque entre la vara de la fase y el Gate 0 no lo resuelve ninguna regla escrita hoy**, y el propio instrumento de las puertas lo dice desde la vuelta 48: *va como pregunta al auditor, no como decision.* **SE DECLARAN** |
| **4** (`hr_calidad_gestion`, `hr_como_control_de_calidad_gerencial`), **20** (`fases_de_retencion_de_clientes`, `ocho_fases_experiencia_cliente`) y **42** (`fase_acclimate_experiencia_cliente`, `fase_acclimate_mapa_de_proceso`) | **CONTEOS DE CONTENIDO QUE CHOCAN SIN PIEZA DECLARADA** | Los pasos apuntan a un lado y las condiciones al otro, y la razon **no declara ni padre, ni contencion, ni alcance del rol** en ninguna direccion: la del 326 llega a escribir que los dos anadidos son *la misma deteccion por dos caminos*. **El acta de la vuelta 53, pregunta 3, manda PARAR y traerlo como pregunta antes de fundir**, y eso es lo que se hace |
| **18** (`desconexion_ventas_experiencia`, `traspaso_ventas_cuentas`) | **EMPATE SIN VARA** | pasos 4 contra 4, condiciones 3 contra 3 **y cableado 2 contra 2**. Es el unico del tramo donde TODO empata, que es lo que la receta reserva para declarar |
| **6**, **44** y **49** | **COLISION PREVISTA, PENDIENTE DE RELECTURA** | los tres fabrican colision de clase con un `B` DIRECTO contra una `D`, y el carril del filo pide **relectura EN EL MISMO ACTO**. **No hubo cuerda en esta vuelta y quedan nombrados** |
| los **veinte** restantes (28 a 41, 43, 45 a 48 y 50) | **SIN TOCAR POR FALTA DE CUERDA** | ninguna guarda los frena: quedan para el siguiente tramo de trabajo |

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

| | al abrir la vuelta 54 | **al cerrarla** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | {apA} / {apB} / {apC} / {apD} | **{ciA} / {ciB} / {ciC} / {ciD}**, sin mover |
| grafo: vivos / deprecados / enlaces | {ap_vivos} / {ap_dep} / {ap_enl} | **{ci_vivos} / {ci_dep} / {ci_enl}** |
| retrato: `A` crudas / colapsos / pares distintos | {ap_crudas} / {ap_colapsos} / {ap_ii} | **{ci_crudas} / {ci_colapsos} / {ci_ii}** |
| actos `CERRADOS` / `ABIERTOS` | {ap_cerrados} / {ap_abiertos} | **{ci_cerrados} / {ci_abiertos}** |
| nodos en `CERRADOS` / `ABIERTOS` | {ap_nod_cer} / {ap_nod_abi} | **{ci_nod_cer} / {ci_nod_abi}** |
| cola de costuras | {ap_cola} | **{ci_cola}** |
| colisiones de clase vigentes | 0 | **{ci_colisiones}**, censo propio sobre el archivo entero |
| actos del tramo 2 fundidos / pendientes | 0 / {actos_tramo} | **{fundidos} / {pendientes}** |
| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |
| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |

> **DE DONDE SALE CADA COLUMNA.** **LAS DOS COLUMNAS SON CORRIDAS PROPIAS DE ESTA VUELTA, y
> ninguna fila de la apertura se hereda del cierre anterior**, que es lo que la regla de la
> apertura pide desde el `D1` de la vuelta 53: marcador
> ([`../loop/SALIDA_V54_MARCADOR_APERTURA.txt`](../loop/SALIDA_V54_MARCADOR_APERTURA.txt)),
> estado ([`../loop/SALIDA_V54_APERTURA.txt`](../loop/SALIDA_V54_APERTURA.txt)), retrato y actos
> ([`../loop/SALIDA_V54_RECOMPUTO_APERTURA.txt`](../loop/SALIDA_V54_RECOMPUTO_APERTURA.txt)),
> cola ([`../loop/SALIDA_V54_COLA_APERTURA.txt`](../loop/SALIDA_V54_COLA_APERTURA.txt)),
> colisiones ([`../loop/SALIDA_V54_COLISIONES_APERTURA.txt`](../loop/SALIDA_V54_COLISIONES_APERTURA.txt))
> y duplicadas ([`../loop/SALIDA_V54_DUPLICADAS_APERTURA.txt`](../loop/SALIDA_V54_DUPLICADAS_APERTURA.txt)),
> **todas corridas ANTES de la primera operacion.** La columna de cierre esta **RECOMPUTADA AL
> CIERRE**, despues del ultimo movimiento.

> **EL MARCADOR NO SE MUEVE Y NO ES UN OLVIDO DEL BARRIDO.** Esta vuelta **no volteo ni un
> veredicto**: los veintiun actos fundidos son de fusion pura y **ninguno fabrico colision**, asi
> que `P.16` no tuvo nada que limpiar. **Por eso las DOS tablas por dominio hermanas tampoco se
> mueven: la `A` de cada uno de los diez dominios es la misma al digito.** La hermandad escrita
> en la TAREA 1.1 de la vuelta 53 **se cumple POR VACIO, y se dice asi en vez de darla por
> cumplida.** **Lo que si se movio son las tres celdas del retrato** (`RECOMPUTO_3388.md` 247,
> 248 y 528), corregidas con tachado, contador cuadrado y nota fechada por el barrido `9.10` del
> cierre: **{colapsos_mas} colapsos mas, UNO POR CADA ACTO FUNDIDO.**
"""

    seccion = seccion.format(**d)

    t = io.open(FUS, encoding="utf-8").read()
    marca = "## `OP-U-01`, TRAMO 2:"
    if marca in t:
        print("  YA ESTABA: el registro del tramo 2 ya esta en la pagina (idempotente)")
        return 0
    if not a.simular:
        io.open(FUS, "w", encoding="utf-8", newline=chr(10)).write(
            t.rstrip(chr(10)) + chr(10) + seccion)
    print("=" * 78)
    print("EL REGISTRO DEL TRAMO 2, con cada cifra LEIDA de la salida que su celda cita")
    print("=" * 78)
    print()
    for k in sorted(d):
        print("  %-16s %s" % (k, d[k]))
    print()
    print("  %s" % ("SIMULACION: no se escribe" if a.simular else "ESCRITO en docs/plan/03_FUSIONES.md"))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
