# -*- coding: utf-8 -*-
"""vuelta49_registro_tramo.py . ESCRIBE EL REGISTRO DEL TRAMO DE LA VUELTA 49 AL
FINAL DE docs/plan/03_FUSIONES.md.

Es el carril adjudicado por el auditor (acta de la vuelta 48, seccion 6, punto 2):
el veredicto de CADA lectura P.12 se registra en el REGISTRO DEL TRAMO de esta
pagina, en tabla propia, y los CONTINUA declaran AHI su arista a la fase 04, con
id RESUELTO (P.9) y SIN ejecutarla.

GUARDA DE ANCLA: el texto se pega DETRAS de la ultima linea del registro de la
vuelta 48, comprobada literal. Si esa linea no esta o no es la ultima, aborta.
GUARDA DE IDEMPOTENCIA: si el encabezado de esta seccion ya esta dentro, no
escribe. Correr dos veces no duplica el registro.

Uso: python scripts/loop/vuelta49_registro_tramo.py [--ejecutar]
"""
import argparse
import io
import sys

DESTINO = "docs/plan/03_FUSIONES.md"
ANCLA = ("| auto-aristas | **CERO** nuevas; **3** que la fusion habria creado, "
         "retiradas en el acto |")
CABECERA = "## `OP-U-01`, TRAMO 1, CIERRE PARCIAL:"

TEXTO = """
---

## `OP-U-01`, TRAMO 1, CIERRE PARCIAL: **LOS DOS EMPATES ADJUDICADOS, LA PRIMERA LECTURA `P.12` EJECUTADA, Y UNA COLISION QUE FABRICO ESTA MISMA VUELTA** (19 ago 2026, vuelta 49)

**Esta seccion NO cierra el tramo 1: cierra TRES de sus treinta y cuatro actos pendientes.** Lo
que queda sin hacer va escrito abajo con su cifra, en vez de callado.

### LOS DOS EMPATES DE `P.8` FILA TRES, ADJUDICADOS Y EJECUTADOS

**Los dos venian declarados en el registro del tramo de la vuelta 48 con la frase `SE TRAE AL
AUDITOR`.** El auditor los re-midio, verifico el empate en los dos y escribio el caso del
superviviente ([`../loop/ACTA_AUDITOR.md`](../loop/ACTA_AUDITOR.md), acta de la vuelta 48,
seccion 5). **El ejecutor verifico cada caso CONTRA EL GRAFO antes de fundir**, con los
veredictos reproducidos verbatim en el dossier de hoy
([`../loop/SALIDA_V49_DOSSIER_20.txt`](../loop/SALIDA_V49_DOSSIER_20.txt) y
[`../loop/SALIDA_V49_DOSSIER_34.txt`](../loop/SALIDA_V49_DOSSIER_34.txt)), **y las tres patas de
cada caso calzan.**

| era el acto | hoy | sobrevive | absorbe | las tres patas del caso, VERIFICADAS hoy |
|---:|---:|---|---|---|
| **22** | **20** | `respeto_a_la_diversidad` | `diversidad_como_fortaleza_ecosistemica`, `respetar_la_diversidad` | **(a)** el puesto **1792** lo escribe **DE CENTRO** de la familia con esas palabras; **(b)** el puesto **1779** llama a su *evaluar la resiliencia* **la unica que pone una PRUEBA al diseno en vez de una regla**; **(c)** el nombre es el principio **sin calificar**, contra *Diversidad como Fortaleza (Fitting)*, que es el angulo del encaje, y contra *Respetar la Diversidad (Biologica, Cultural y de Lugar)*, que es el principio con tres calificativos |
| **42** | **34** | `storyboard` | `storyboard_prototipado` | **(a)** el nombre del concepto **sin calificar**, y el propio veredicto **179** dice que el otro es *el base mas un sufijo tematico*; **(b)** su **mecanica de sesion** es lo que hace ejecutable la practica (el time-box de 30 a 45 minutos, no preocuparse por la calidad del dibujo, actuar o presentar al equipo) y **ninguna de las tres esta en el otro**; **(c)** la anatomia del otro **viaja limpia** |

**EL EMPATE, RE-MEDIDO HOY Y NO HEREDADO:** el acto 20 da **cuatro pasos y dos condiciones cada
uno** y **cableado 3 a 3** entre los dos punteros; el acto 34 da **cuatro pasos cada uno**,
**cableado 4 a 4** y **cero aristas internas**. **El empate era real y sigue siendolo**, que es
lo que hace que la eleccion la decidan las tres patas y no el conteo.

**LA VARA DE LAS PUERTAS, APLICADA ANTES DE TOCAR** (adjudicacion del acta 48, seccion 6, punto
1): medida hoy sobre la nomina de hoy
([`../loop/SALIDA_V49_PUERTAS_EN_EL_LOTE.txt`](../loop/SALIDA_V49_PUERTAS_EN_EL_LOTE.txt)),
**ninguno de los cinco miembros de los dos actos es semilla de entrada ni extremo de puente
aprobado**, y ni el 20 ni el 34 estan entre los **30 SALVABLES** ni entre los **2 IMPOSIBLES**.
**La vara no muerde aqui y la guarda `1B` pasa por vacio: se dice en vez de darla por buena.**

### EL TERCER DESTINO QUE LE FALTABA AL INSTRUMENTO DE FUNDIR: `INCISO`

> **Nace de la correccion que el auditor encargo sobre el acto 49, dos secciones mas arriba, y
> no de un capricho.** El instrumento de la vuelta 48 solo sabia **DOS** destinos para una pieza
> del que muere: `APPEND` (viaja entera) y `CUBIERTO:n` (ya lo dice el paso n). **El caso de en
> medio no tenia marca**, y esa carencia es exactamente lo que produjo la pieza mal marcada del
> acto 49.

**`scripts/loop/vuelta49_fundir_tramo.py`**, sucesor declarado del de la vuelta 48, anade la
marca **`INCISO:n|<inciso VERBATIM>|<nexo>`** con sus dos guardas propias: **el inciso tiene que
ser trozo LITERAL** del paso del absorbido, y **si ya esta dentro no se apila**.

**El acto 34 lo estrena, y es LA MISMA FORMA del acto 49.** El paso 4 de `storyboard_prototipado`
(*Compartir el storyboard con usuarios o el equipo para retroalimentacion*) contra el paso 4 del
superviviente (*Actuar o presentar el storyboard al equipo para recibir feedback*): **`APPEND`
entero habria dejado dos pasos mandando lo mismo, y `CUBIERTO` habria perdido la palabra
`usuarios`, que es lo unico que el otro anade.**

| | el paso 4 del superviviente |
|---|---|
| **antes** | `Actuar o presentar el storyboard al equipo para recibir feedback` |
| **HOY** | `Actuar o presentar el storyboard al equipo para recibir feedback, y compartirlo con usuarios o el equipo para retroalimentacion` |

> **SE MARCA COMO DISCUTIBLE, y va tambien al reporte de la vuelta:** el auditor escribio que esa
> pieza *viaja limpia como pieza*, y **el ejecutor la hace viajar como INCISO**. No se pierde ni
> una palabra de lo que el auditor mando viajar, pero **no es literalmente lo que dijo**.

### LA PRIMERA LECTURA `P.12`, REGISTRADA EN TABLA PROPIA (el carril adjudicado)

**El carril lo adjudico el auditor** (acta de la vuelta 48, seccion 6, punto 2): el veredicto de
cada lectura `P.12` se registra **AQUI**, en tabla propia, y **los `CONTINUA` declaran AHI su
arista a la fase 04**, con id **RESUELTO** (`P.9`) y **SIN ejecutarla**, que es la figura de
[`02_DESTEJIDOS.md`](02_DESTEJIDOS.md) **linea 3521**.

| el mixto | leido CONTRA | veredicto | las citas |
|---|---|---|---|
| `metodologia_spin_selling` | `modelo_spin_preguntas` | **`CONTINUA`** | **Los DOS veredictos `D` del acto lo dicen con esa palabra.** El puesto **764**: *el paso 3 de la madre es UNA LINEA QUE ADEMAS REMITE FUERA* (*prepararse para usar las preguntas de Situacion, Problema, Implicacion y Necesidad-Beneficio, que se detallan en capitulos posteriores*) y `modelo_spin_preguntas` *trae el PROCEDIMIENTO entero*; **No cabe en una linea: CONTINUA**. El puesto **625** dice lo mismo con el otro miembro de la parte A: *CONTINUA, no repite* |

**LA ARISTA QUE FALTA, DECLARADA AQUI Y NO EJECUTADA:**

| de | a | sentido | medida hoy | quien la ejecuta | la poda del solape |
|---|---|---|---|---|---|
| `metodologia_spin_selling` | `modelo_spin_preguntas` | de la **madre** al **hijo**: la madre nombra en su paso 3 lo que el hijo desarrolla | **CERO arista en los dos sentidos**, buscada hoy resolviendo por alias | **la fase 04**. Los dos ids van **RESUELTOS** (`P.9`): `modelo_spin_preguntas` es el superviviente de la parte A de este mismo acto | **PENDIENTE de la fase que ejecute el enlace.** Esta operacion **NO la tiene autorizada**. El solape a podar es **el paso 3 de `metodologia_spin_selling`**, que es la linea que remite fuera |

### LA PARTE A DEL ACTO 1, FUNDIDA

| sobrevive | absorbe | por que, y no esta empatado |
|---|---|---|
| `modelo_spin_preguntas` | `framework_spin_selling`, `modelo_spin` | **CONTENIDO, y el cableado no habla porque no hay empate (`P.8`).** SEIS pasos contra CUATRO y CUATRO, TRES condiciones contra UNA y DOS, y el resumen mas largo del acto. **Es el unico que trae las dos piezas que cierran el metodo**: ajustar la secuencia al flujo natural **sin forzar el orden rigido**, y **NO presentar la solucion hasta que el cliente haya articulado la Necesidad Explicita**. **Y lo escribe el veredicto 401**: *el segundo detalla que hace cada tipo de pregunta*. Cableado **15** contra 9 y 7 |

**Pasos 6 a 9, condiciones 3 a 5. Once piezas repartidas: CINCO viajan enteras y SEIS ya las
decia.** Plan sellado en
[`../loop/PLAN_V49_OPU01_ACTO1.json`](../loop/PLAN_V49_OPU01_ACTO1.json).

### **LA COLISION DE CLASE QUE FABRICO ESTA MISMA VUELTA**, y se cuenta con nombre

> **Se dice asi, y no como hallazgo, porque la fabrico mi propia operacion.** Es el canon 9: un
> fallo que no deja sintoma es la especie que hay que contar.

**Al deprecar `modelo_spin` con alias a `modelo_spin_preguntas`, el puesto 305**
(`metodologia_spin_selling` contra `modelo_spin`, clase **`A`**) **paso a RESOLVER sobre el mismo
par que el 764** (clase **`D`**) **y que el 625** (clase **`D`**). **Tres veredictos, un solo par
resuelto, dos clases.**

**`P.16` DEL BANCO DEL PLAN, QUIEN FABRICA LIMPIA**, y el carril es el que el auditor adjudico
para las tres colisiones preexistentes: **relectura conjunta con los textos vivos delante,
correccion declarada, y marcador recomputado.** **El 305 pasa de `A` a `D`**, y la relectura no
necesita doctrina nueva porque **la lectura `P.12` de arriba YA ES esa relectura**: el `305` leyo
`modelo_spin`, un nodo cuyo cuerpo eran **tres gestos de entrenamiento** mas el orden enunciado;
**el nodo vivo de hoy tiene NUEVE pasos** y trae el procedimiento entero. **Contra ese, el paso 3
de `metodologia_spin_selling` sigue siendo una linea.**

### **LA MEDICION QUE ESTO OBLIGA A HACER, Y ES LO MAS GRANDE QUE DEJA ESTA VUELTA**

**No es un caso suelto.** Medido hoy sobre **todos** los mixtos pendientes
([`../loop/SALIDA_V49_MIXTOS_FORMA.txt`](../loop/SALIDA_V49_MIXTOS_FORMA.txt)):

| | |
|---|---:|
| mixtos pendientes con **la forma** (algun miembro carga a la vez un par `A` y un par NO-`A` dentro del acto) | **26** |
| mixtos pendientes **sin** la forma | **1** |

> **QUE SIGNIFICA, dicho con su limite:** la forma **solo fabrica colision cuando el veredicto es
> `CONTINUA`**. Si el mixto `ENTRA`, el acto se funde entero y todos sus pares colapsan a
> auto-par sin chocar. **Asi que la cifra de 26 es el TECHO, no la prediccion**: cuantas
> colisiones nazcan de verdad depende de cuantas lecturas digan `CONTINUA`, y eso no se sabe
> hasta leerlas.
>
> **Y LA BUENA NOTICIA VA CON ELLA:** cuando nace, **la colision se resuelve con la MISMA lectura
> que la produjo**, sin doctrina nueva, porque `CONTINUA` es precisamente el hallazgo de que el
> mixto **no repite** al superviviente. **El `A` viejo se emitio contra un nodo que hoy no existe
> solo.**

### LO QUE ESTA SECCION **NO** HIZO

| | |
|---|---:|
| lecturas `P.12` **hechas y registradas** | **1** (el acto 1, que ya la tenia hecha) |
| lecturas `P.12` **encargadas y NO hechas** | **25** |
| actos **fundidos** en esta seccion | **3** (los dos empates y la parte A del acto 1) |
| **tramo 2** de 50 actos | **NO ABIERTO**: no hubo cuerda |
| los declarados **29**, **32** y **36** (hoy **26**, **28** y **32**) | **siguen declarados**, ninguno se toca |
| los dos actos que la vuelta 48 dejo fuera **por colision de clase medida** (hoy los **8** y **33**) | **siguen fuera**, y esta vuelta no los mira |

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

| | al abrir la vuelta 49 | **al cerrarla** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 575 / 79 / 8 / 2.726 | **573 / 77 / 8 / 2.730** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.504 / 349 / 16.962 | **3.853 / 3.499 / 354 / 16.984** |
| actos `CERRADOS` / `ABIERTOS` | 254 / 54 | **252 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 543 / 243 | **536 / 240** |
| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |
| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    t = io.open(DESTINO, encoding="utf-8", newline="").read()
    print("destino: %s (%d lineas)" % (DESTINO, t.count("\n") + 1))

    if CABECERA in t:
        print("YA ESCRITO: la cabecera de esta seccion ya esta dentro. Cero escrituras.")
        return 0
    if not t.rstrip().endswith(ANCLA):
        print("[ROJO] el ancla no es la ultima linea del fichero. Se aborta sin escribir.")
        print("  ancla esperada: %s" % ANCLA)
        print("  ultima linea  : %s" % t.rstrip().splitlines()[-1])
        return 1

    nuevo = t.rstrip("\n") + "\n" + TEXTO
    print("lineas nuevas: %d" % (TEXTO.count("\n")))
    if not a.ejecutar:
        print("SIMULACION: cero escrituras.")
        return 0
    io.open(DESTINO, "w", encoding="utf-8", newline="").write(nuevo)
    print("ESCRITO. total ahora: %d lineas" % (nuevo.count("\n") + 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
