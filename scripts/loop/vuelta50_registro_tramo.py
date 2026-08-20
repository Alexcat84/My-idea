# -*- coding: utf-8 -*-
"""vuelta50_registro_tramo.py . ESCRIBE EL REGISTRO DEL TRAMO DE LA VUELTA 50 AL
FINAL DE docs/plan/03_FUSIONES.md.

SUCESOR DECLARADO de scripts/loop/vuelta49_registro_tramo.py, del que hereda el
contrato entero: el veredicto de CADA lectura `P.12` se registra en el REGISTRO
DEL TRAMO de esta pagina, en tabla propia, y los `CONTINUA` declaran AHI su
arista a la fase 04, con id RESUELTO (`P.9`) y SIN ejecutarla. Es el carril
adjudicado por el auditor (acta de la vuelta 48, seccion 6, punto 2).

LO QUE CAMBIA: el registro se escribe POR BLOQUES y no de una sola vez, porque
esta vuelta tiene un encargo largo y la regla 6 del EJECUTOR.md manda commitear
por tramo para que nada dependa de que la sesion aguante. Cada bloque trae su
propia ANCLA y su propia GUARDA DE IDEMPOTENCIA.

GUARDA DE ANCLA: el texto se pega DETRAS de la ultima linea que se le indique,
comprobada literal. Si esa linea no esta o no es la ultima del fichero, aborta.
GUARDA DE IDEMPOTENCIA: si la cabecera del bloque ya esta dentro, no escribe.

Uso: python scripts/loop/vuelta50_registro_tramo.py --bloque apertura [--ejecutar]
"""
import argparse
import io
import sys

DESTINO = "docs/plan/03_FUSIONES.md"

BLOQUES = {}

# ---------------------------------------------------------------------------
BLOQUES["apertura"] = {
    "ancla": "| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |",
    "cabecera": "## `OP-U-01`, TRAMO 1, LA VUELTA 50:",
    "texto": """
---

## `OP-U-01`, TRAMO 1, LA VUELTA 50: **EL BARRIDO QUE LA VUELTA 49 NO CORRIO AL CERRAR, Y UN ALIAS QUE NO SE IZO** (19 ago 2026, vuelta 50)

### LO PRIMERO DE LA VUELTA, PORQUE ES UNA CAIDA DE CIFRA PUBLICADA Y NO UN TRAMITE

**La vuelta 49 movio el marcador y el retrato DESPUES de correr su barrido `9.10`** (el volteo
del puesto **305** por `P.16` y las tres fusiones de su TAREA 2) **y no volvio a barrer al
cerrar.** El acta de la vuelta 49, seccion 3, lo nombra como caida de cifra publicada del
ejecutor, FUERA de sus discutibles marcados. **Las cinco celdas quedan corregidas hoy con
tachado, fecha y motivo**, y las cifras salen de dos instrumentos corridos EN ESTA VUELTA y de
ningun acta:

| la celda | decia | **hoy, medido en esta vuelta** | el instrumento |
|---|---:|---:|---|
| [`../INTRA_DOMINIO_INFORME.md`](../INTRA_DOMINIO_INFORME.md) apendice **100.1**, fila `A` | 574 | **573** | `scripts/recomputar_marcador.py 3388` |
| el mismo apendice, fila `D` | 2.729 | **2.730** | el mismo |
| [`RECOMPUTO_3388.md`](RECOMPUTO_3388.md) fila **246**, `A` crudas | 574 | **573** | `scripts/plan/recomputo_3388.py` |
| la fila **247**, colapsos a auto-arista | 41 | **48** | el mismo |
| la fila **248**, pares distintos del retrato | 533 | **525** | el mismo |
| la fila **1079**, total de `A` de la tabla por dominio | 574 | **573** | `recomputar_marcador.py` |
| el checkpoint **ii** de la fila **528** | 533 igual a 533 | **525 igual a 525, sigue OK** | `recomputo_3388.py`, seccion final |

**Y LA CIFRA 41 NO ERA UN ERROR DE LECTURA, QUE ES LO QUE LA HACE INTERESANTE:** era el corte de
la TAREA 1.3 de la vuelta 49, tomado ANTES de las tres fusiones de su propia TAREA 2. **Los
siete que faltaban son la huella de esas tres fusiones**, que es exactamente lo que la propia
fila ya explicaba de las 41. Una fila puede explicar bien su cifra y traer la cifra vieja.

> **LA REGLA QUE ESTO DEJA, y ya esta adjudicada** (acta de la vuelta 49, seccion 5, pregunta 5,
> por extension del banco `9.10`): **quien mueve una clase o funde un acto corre el barrido ANTES
> DE CERRAR LA VUELTA**, sobre toda tabla vigente que cite la clase, el marcador o el retrato.
> Barrer al destapar y barrer al mover son la misma regla vista de los dos lados.

### EL INSTRUMENTO DEL BARRIDO TENIA LA MISMA AVERIA QUE PERSEGUIA, Y SE DICE

**Medido antes de escribir una linea del sucesor:** `scripts/loop/vuelta49_barrido_910.py` acepta
`--viejo` **pero no lo usa para buscar**. Sus dos expresiones regulares estan clavadas a `583` y
`2709`, las cifras del marcador de la vuelta 14, y `--viejo` solo cambia la cabecera que imprime.
Corrido hoy con `--viejo 574,77,8,2729` devuelve 22 candidatos, **y los devuelve porque esas
celdas arrastran el 583 en su cadena de tachados, no porque sepa buscar el 574**
([`../loop/SALIDA_V50_BARRIDO_910_INSTRUMENTO_VIEJO.txt`](../loop/SALIDA_V50_BARRIDO_910_INSTRUMENTO_VIEJO.txt)).
**Una celda nueva escrita hoy con la cifra vigente y sin cadena de tachados le seria invisible.**
El sucesor `scripts/loop/vuelta50_barrido_910.py` busca de verdad lo que se le pide, conserva la
familia legado del 583 y anade la familia del RETRATO, que ningun barrido anterior miraba: **con
el, las siete celdas de arriba salen solas**
([`../loop/SALIDA_V50_BARRIDO_910_A.txt`](../loop/SALIDA_V50_BARRIDO_910_A.txt)).

### EL ALIAS QUE NO SE IZO AL SUPERVIVIENTE (`modelo_spin_2`)

**Una linea de registro y ningun dato tocado**, que es lo que el encargo manda. Al fundir la
parte A del acto 1 en la vuelta 49, el absorbido `modelo_spin` cargaba a su vez el alias
`modelo_spin_2` y **ese alias NO se izo a `modelo_spin_preguntas`**. Medido hoy con
`scripts/loop/vuelta50_alias_durmiente.py`
([`../loop/SALIDA_V50_ALIAS_DURMIENTE.txt`](../loop/SALIDA_V50_ALIAS_DURMIENTE.txt)), y con un
filo mas que la observacion del acta: **por el resolutor de la casa (`P.1`, que construye el mapa
de alias SOLO con nodos vivos) `modelo_spin_2` NO RESUELVE EN ABSOLUTO**; solo llega por la
cadena ancha `modelo_spin_2` a `modelo_spin` **[DEPRECADO]** a `modelo_spin_preguntas`. **CERO
referencias en aristas y CERO en veredictos**: nadie lo pisa hoy. **Es pasivo de la especie
`OP-S-12` y queda nombrado para esa operacion**, no se repara aqui.
""",
}

# ---------------------------------------------------------------------------
BLOQUES["tramo2"] = {
    "ancla": "`OP-S-12` y queda nombrado para esa operacion**, no se repara aqui.",
    "cabecera": "### LA RECETA DE `P.12` NO ESTABA DEFINIDA",
    "texto": """
### LA RECETA DE `P.12` NO ESTABA DEFINIDA PARA LA FORMA QUE TIENEN 24 DE LOS 26 MIXTOS, Y ESO ES LO PRIMERO QUE HUBO QUE MEDIR

**El encargo manda, por cada acto mixto, elegir el superviviente de la PARTE A y leer el MIXTO
contra el.** Esa receta presupone una forma concreta, que es la del UNICO acto ya resuelto (el
del SPIN, vuelta 49): **una clique de pares `A` mas UN nodo colgando** que entra a la componente
por una sola arista `A` y tiene `D` con el resto. **El primer acto que se abrio en esta vuelta no
tiene esa forma**, y por eso antes de fundir nada se midio la de los veintiseis
([`../loop/SALIDA_V50_FORMA_MIXTOS.txt`](../loop/SALIDA_V50_FORMA_MIXTOS.txt)):

| forma del subgrafo `A` | actos |
|---|---:|
| **CLIQUE MAS COLGANTE**, la del SPIN, donde la receta se aplica sola | **2** |
| **ESTRELLA**, un centro que repite contra cada punta y puntas que no se parecen entre si | **24** |

**La ESTRELLA no es una rareza: es la figura `9.23` del banco**, escrita con su ejemplar y su
tabla de costes, y **el propio archivo la nombra** (el puesto **1201** dice, con esa palabra,
*este par cierra una ESTRELLA*). Lo que el banco `9.23` NO dice es quien sobrevive cuando el
centro repite contra varios nodos que son `D` entre si.

### LA DEFINICION OPERATIVA, SACADA DEL ACTO YA RESUELTO Y NO INVENTADA

**En el acto del SPIN la parte A fueron los nodos con arista `A` CONTRA EL SUPERVIVIENTE, y el
mixto fue el unico miembro SIN arista `A` contra el.** Generalizado, y es lo unico que esta
vuelta anade:

> **dado un superviviente `S`: PARTE A = `S` mas los miembros con arista `A` contra `S`;
> MIXTOS = los miembros SIN arista `A` contra `S`.**

**Y de ahi sale una comprobacion que no es criterio sino aritmetica**, corrida sobre los 26
([`../loop/SALIDA_V50_SUPERVIVIENTES_VIABLES.txt`](../loop/SALIDA_V50_SUPERVIVIENTES_VIABLES.txt)):
un superviviente es **VIABLE** si su parte A es una clique `A` (si no, fundirla juntaria dos nodos
que el archivo declaro `D`, que es lo que `P.12` prohibe) y si deja al menos un mixto fuera.

| resultado | actos |
|---|---:|
| **VARIOS VIABLES**, y el CONTENIDO decide, que es la regla de esta pagina | **26 de 26** |
| NINGUNO VIABLE, que habria sido parada | **CERO** |

> **NINGUN ACTO SE QUEDA SIN SUPERVIVIENTE POSIBLE, asi que no hay condicion de parada.** Lo que
> hay es que **en la estrella el CENTRO casi nunca es viable**: absorberlo todo juntaria las
> puntas, que son `D` entre si.

**Y UN CHOQUE MEDIDO QUE SE DEJA NOMBRADO: CINCO veredictos en CUATRO actos** (los de hoy **3**,
que trae dos, **27**, **28** y **29**): **un veredicto `A` cierra con la formula *Sobrevive X* y
ese `X` NO es viable** por la estructura del acto. La letra del veredicto y la aritmetica del acto
apuntan a sitios distintos. **No se resuelve aqui**: se mide, se nombra y se trae.

### EL ACTO 1 DE LA NOMINA DE HOY, EJECUTADO ENTERO: EL RACIMO DE LA DERIVA

| | |
|---|---|
| miembros | `deriva_hacia_el_fallo`, `drift_hacia_el_fallo`, `drift_hacia_el_fallo_2`, `normalizacion_de_la_desviacion` |
| forma | **ESTRELLA**, centro `drift_hacia_el_fallo_2`, que repite contra los otros tres (puestos **2222**, **2226**, **2237**) |
| supervivientes viables | **TRES**; el centro **NO** es viable |
| **superviviente elegido** | **`normalizacion_de_la_desviacion`**, por **CONTENIDO** y sin empate: **SEIS** pasos contra cuatro, **CUATRO** condiciones contra dos, y el resumen mas largo de los cuatro (**711** caracteres contra 574, 466 y 458). Es el mismo margen y el mismo criterio con que la vuelta 49 eligio a `modelo_spin_preguntas`. **Y lo escribe el propio veredicto `A` del par**: el **2237** cierra con *Sobrevive normalizacion_de_la_desviacion* |
| parte A fundida | `normalizacion_de_la_desviacion` absorbe `drift_hacia_el_fallo_2` |
| **vara de las puertas** | medida hoy sobre la nomina de hoy ([`../loop/SALIDA_V50_PUERTAS_EN_EL_LOTE.txt`](../loop/SALIDA_V50_PUERTAS_EN_EL_LOTE.txt)): el acto **no** esta entre los **30 SALVABLES** ni entre los **2 IMPOSIBLES**, ningun miembro es semilla ni extremo de puente. **La guarda `1B` pasa por vacio y se dice asi en vez de darla por buena** |

**NOTA DE FUENTE, que no decide pero se dice**, igual que en el acto del SPIN: los otros tres
miembros son de **Dekker** y el superviviente es de **Reason**; el que muere es de Dekker. **La
regla de la pagina pesa CONTENIDO, no procedencia**, y las piezas de Dekker viajan enteras o
adosadas: **ninguna se pierde.**

#### LAS DOS LECTURAS `P.12`, con sus citas

| el mixto | contra | veredicto | lo que lo decide |
|---|---|---|---|
| `deriva_hacia_el_fallo` | `normalizacion_de_la_desviacion` | **`CONTINUA`** | El puesto **2275**: *LA ESTRUCTURA CONTRA EL CALENDARIO*. Uno explica **por que pasa** (acoplamiento fuerte de Perrow, exploracion organizacional contra los limites de seguridad) y el otro dice **como se para**. Lo propio del mixto es **un marco analitico entero** que el superviviente no menciona, no un paso de su procedimiento |
| `drift_hacia_el_fallo` | `normalizacion_de_la_desviacion` | **`CONTINUA`** | El puesto **2394** reparte los dos con dos verbos y esas palabras: **drift VIGILA** (monitorear la brecha entre procedimiento escrito y practica real de forma sistematica, y cuestionar si el exito reciente es seguridad real) y **normalizacion FRENA**. Dos procedimientos distintos sobre la misma idea |

**LAS DOS ARISTAS QUEDAN DECLARADAS AQUI CON ID RESUELTO (`P.9`) Y SIN EJECUTARSE**, que es la
figura de [`02_DESTEJIDOS.md`](02_DESTEJIDOS.md) linea 3521, y **la poda del solape queda anotada
como pendiente de la fase 04**:

| de | a | sentido | el solape a podar |
|---|---|---|---|
| `deriva_hacia_el_fallo` | `normalizacion_de_la_desviacion` | del que explica al que remedia | la auditoria del historial, **declarada como solape por el propio 2275** |
| `drift_hacia_el_fallo` | `normalizacion_de_la_desviacion` | del que vigila al que frena | la auditoria del historial y la relajacion de criterios, **declaradas por el propio 2394** |

#### EL REPARTO DE LAS SEIS PIEZAS, impreso por el instrumento

**Ninguna se teclea: el plan trae INDICES y el instrumento lee cada pieza verbatim del fichero**
([`../loop/PLAN_V50_OPU01_ACTO1.json`](../loop/PLAN_V50_OPU01_ACTO1.json),
[`../loop/SALIDA_V50_ACTO1_EJEC.txt`](../loop/SALIDA_V50_ACTO1_EJEC.txt), exit 0).

| pieza de `drift_hacia_el_fallo_2` | destino |
|---|---|
| paso **1**, el historial de pequenos cambios acumulados | **ya lo dice el paso 1** del superviviente, **y lo escribe el 2237** |
| paso **2**, las senales descartadas o no reportadas como *malas noticias* | **viaja entero**, paso **7** |
| paso **3**, la puntualidad vuelta norma a costa de los margenes | **INCISO ADOSADO al paso 3** |
| paso **4**, la cultura donde las desviaciones son visibles | **viaja entero**, paso **8** |
| condiciones **1** y **2** | **viajan enteras**, condiciones **5** y **6** |

> **POR QUE EL PASO 3 VA DE INCISO Y NO DE `APPEND` NI DE `CUBIERTO`, que es la unica pieza fina
> del reparto:** el **2237** dice que ese paso es **un EJEMPLO** del paso 3 del superviviente.
> **`APPEND` dejaria dos pasos mandando revisar lo mismo; `CUBIERTO` perderia el ejemplar
> concreto**, que es lo unico que vuelve palpable la relajacion de criterios. Es la forma exacta
> para la que la vuelta 49 incorporo el INCISO al instrumento. **El nexo, lo unico de cosecha
> propia, va impreso aparte**: `, por ejemplo si `.

#### LAS DOS COLISIONES QUE LA FUSION FABRICO, LIMPIADAS EN EL MISMO ACTO (`P.16`)

**LA CUENTA CALZA CON LA QUE EL ENCARGO EXIGE: una colision por cada `CONTINUA`, cero por cada
`ENTRA`. Dos `CONTINUA`, DOS colisiones**, medidas con resolutor propio
([`../loop/SALIDA_V50_CENSO_COLISIONES_ACTO1.txt`](../loop/SALIDA_V50_CENSO_COLISIONES_ACTO1.txt)).

| el par resuelto | los dos veredictos | el volteo |
|---|---|---|
| `deriva_hacia_el_fallo` contra `normalizacion_de_la_desviacion` | **2222** `A` (emitido contra `drift_hacia_el_fallo_2`) y **2275** `D` | **2222: `A` a `D`** |
| `drift_hacia_el_fallo` contra `normalizacion_de_la_desviacion` | **2226** `A` (emitido contra `drift_hacia_el_fallo_2`) y **2394** `D` | **2226: `A` a `D`** |

**Las dos correcciones llevan la razon vieja ENTERA dentro, pegada POR MAQUINA y no transcrita**
([`../loop/SALIDA_V50_CORREGIR_ACTO1.txt`](../loop/SALIDA_V50_CORREGIR_ACTO1.txt)), con el carril
adjudicado en el acta de la vuelta 49, pregunta 1: **la lectura `P.12` ES la relectura conjunta
de ese `A`**, porque ese `A` se emitio contra un nodo que hoy no existe solo. **Censo tras la
limpieza: CERO colisiones vigentes.**

### LO QUE ESTA VUELTA NO HIZO DEL TRAMO 1, CON SU CIFRA

| | |
|---|---:|
| lecturas `P.12` **hechas y ejecutadas** en esta vuelta | **2** (las dos del acto 1) |
| actos **fundidos** | **1** |
| actos **MIXTOS que siguen pendientes** de `P.12`, re-medidos al cierre | **25** |
| **tramo 2** de 50 actos | **NO ABIERTO** |

> **Y LA CIFRA DEL ENCARGO NO CUADRA CON LA MEDICION, ASI QUE SE DECLARA EN VEZ DE COPIARSE**
> (regla 2 del `EJECUTOR.md`): **el encargo pide *las veinticinco lecturas `P.12` pendientes*, y
> al abrir esta vuelta eran VEINTISEIS**, medidas por miembros sobre la nomina re-corrida
> ([`../loop/SALIDA_V50_TRAMO1_POR_MIEMBROS.txt`](../loop/SALIDA_V50_TRAMO1_POR_MIEMBROS.txt)).
> **El 25 viene de la fila *lecturas `P.12` encargadas y NO hechas* del registro de la vuelta 49**,
> que en la misma pagina convive con un **26 de 26** en su medicion de la forma. **La cuenta buena
> es 26**: la vuelta 48 dejo **27** mixtos y la 49 resolvio **uno**. Con el acto 1 de esta vuelta
> hecho, **quedan 25**, que ahora si es la cifra medida y no la heredada.

### LOS DECLARADOS, IDENTIFICADOS POR SUS MIEMBROS Y NO POR SU NUMERO

**El numero baila con cada fusion y por eso no se usa** (lo manda el encargo). Los cinco del tramo
1 siguen declarados y **ninguno se toca**:

| los miembros | por que sigue declarado | numero en la vuelta 48 / **hoy** |
|---|---|---|
| `obtencion_compromiso`, `obtencion_compromiso_venta`, `obtencion_de_compromiso` | **colision de clase medida**: fundirlo fabrica una colision **aunque se funda solo el nucleo `A`**, medido hoy | 8 / **7** |
| `mejora_del_sistema_responsabilidad_gerencial`, `sistema_estable_causas_comunes`, `sistema_estable_responsabilidad_gerencial` | el puesto **2572** llama **PROVISIONAL** a su propio ganador | 29 / **24** |
| `dia_cero_defectos`, `dia_cero_defectos_2`, `dia_cero_defectos_3` | el puesto **2525** deja aviso expreso: las cadenas de firma son **incompatibles** y hay que **decidirlo, no apilarlo** | 32 / **26** |
| `domina_lo_que_compras`, `investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor` | **IMPOSIBLE POR PUERTA**: los dos miembros son puerta, alguien tendria que morir | 36 / **30** |
| `cultura_climatica_innovacion`, `cultura_de_innovacion` | **colision de clase medida**, igual que el primero | 40 / **31** |

**Los dos IMPOSIBLES por puerta re-medidos hoy sobre la nomina de hoy son el `domina_lo_que_compras`
y `licenciamiento_tecnologico` contra `proteccion_propiedad_intelectual_internacional`** (hoy el
acto **156**), **y el segundo cae FUERA del tramo 1**, que es exactamente lo que decia el registro
de la vuelta 48 con la numeracion de aquel dia.

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

| | al abrir la vuelta 50 | **al cerrarla** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 573 / 77 / 8 / 2.730 | **571 / 77 / 8 / 2.732** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.499 / 354 / 16.984 | **3.853 / 3.498 / 355 / 16.986** |
| retrato: `A` crudas / colapsos / pares distintos | 573 / 48 / 525 | **571 / 49 / 522** |
| actos `CERRADOS` / `ABIERTOS` | 252 / 53 | **251 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 536 / 240 | **532 / 240** |
| cola de costuras | 1.491 | **1.491**, sin cambio |
| colisiones de clase vigentes | 0 | **0** |
| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |
| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |
| **el barrido `9.10` DEL CIERRE**, la regla del aviso | | **CORRIDO despues del ultimo movimiento**, con **diez** celdas corregidas |
""",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bloque", required=True, choices=sorted(BLOQUES))
    ap.add_argument("--ejecutar", action="store_true")
    args = ap.parse_args()
    b = BLOQUES[args.bloque]

    texto = io.open(DESTINO, encoding="utf-8").read()

    print("=" * 78)
    print("REGISTRO DEL TRAMO, vuelta 50, bloque: %s" % args.bloque)
    print("destino: %s" % DESTINO)
    print("=" * 78)

    if b["cabecera"] in texto:
        print("YA ESCRITO (idempotencia): la cabecera del bloque ya esta dentro.")
        return 0

    ancla = b["ancla"]
    if texto.count(ancla) != 1:
        print("ROJO: el ancla aparece %d veces, tiene que aparecer UNA." % texto.count(ancla))
        return 1
    if not texto.rstrip("\n").endswith(ancla):
        print("ROJO: el ancla no es la ULTIMA linea del fichero. No se escribe nada.")
        print("      ultima linea: %r" % texto.rstrip("\n").splitlines()[-1][:120])
        return 1

    nuevo = texto.rstrip("\n") + "\n" + b["texto"]
    print("ancla OK y es la ultima linea. Se anaden %d caracteres."
          % (len(nuevo) - len(texto)))
    # Los dos caracteres van por ESCAPE y no literales, para que este fichero
    # cumpla el mismo cero guiones que comprueba. Un guardian que lleva dentro
    # lo que prohibe es un guardian que no se puede barrer con su propia vara.
    for mal, nombre in ((chr(0x2014), "guion largo"), (chr(0x2013), "guion medio")):
        if mal in b["texto"]:
            print("ROJO: el bloque trae un %s." % nombre)
            return 1
    print("guiones largos y medios en el bloque: CERO")

    if not args.ejecutar:
        print("SIMULACION: nada escrito.")
        return 0
    io.open(DESTINO, "w", encoding="utf-8", newline="").write(nuevo)
    print("ESCRITO.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
