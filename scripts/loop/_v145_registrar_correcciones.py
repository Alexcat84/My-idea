# -*- coding: utf-8 -*-
"""_v145_registrar_correcciones.py . Escribe por ADICION las CORRECCIONES 21 y
22 al final de docs/plan/CORRECCIONES_A_APLICAR.md (vuelta 145, TAREA 1.b y
1.c). Instrumento de un solo uso, como los _v1xx_ anteriores: la adicion se
hace con una guarda que se niega si las correcciones ya estan."""
import io

TEXTO = u"""

---

## CORRECCION 21. **LA ANCLA UNICA NO ERA SOLO DE LA FORMULA DE LA EXCEPCION**

**Adjudicacion 4.3 del acta de la vuelta 144** (caida de la casa). Registrada por
adicion en la vuelta 145, TAREA 1.b; implementada en la TAREA 2.a. Corte de todas
las cifras de esta entrada: **2 sep 2026**. **TODO LO QUE SIGUE ESTA MEDIDO POR EL
EJECUTOR CON INSTRUMENTO PROPIO**, `scripts/loop/vuelta145_1b_censo_de_marcas.py`,
salida en [`loop/SALIDA_V145_1B_CENSO_DE_MARCAS.txt`](../loop/SALIDA_V145_1B_CENSO_DE_MARCAS.txt);
no se copia ninguna cifra del acta.

### 21.a. EL DEFECTO

`quitar_bloques_cubiertos()` de `scripts/loop/verificar_cifras_del_reporte.py`
resolvia cada uno de sus **TRES** pares de marcas con `texto.find(MARCA)`, y `find`
**devuelve la PRIMERA ocurrencia**. Con la marca repetida, el recorte iba **de la
primera apertura al primer cierre** y el segundo bloque **se parseaba entero, en
silencio y con VERDE EXIT 0**.

### 21.b. CUANTAS VECES APARECE CADA MARCA, MEDIDO

**Sujeto: el `docs/loop/REPORTE.md` de la vuelta 144 YA COMMITEADO**, leido por ref
de git (`b7f07648:docs/loop/REPORTE.md`), nunca del arbol vivo. **40.541 caracteres,
639 lineas.**

| marca | veces | posiciones (linea, offset) |
|---|---:|---|
| apertura de CABECERA TALLADA | 1 | 22 (1038) |
| cierre de CABECERA TALLADA | 1 | 34 (3630) |
| apertura de COMMITS TALLADOS | 1 | 43 (3849) |
| cierre de COMMITS TALLADOS | 1 | 66 (5739) |
| apertura de COBERTURA DE LA GUARDA | **2** | **274 (17651), 632 (40326)** |
| cierre de COBERTURA DE LA GUARDA | **2** | **278 (18315), 638 (40505)** |

### 21.c. QUE RECORTA HOY Y QUE SE QUEDA FUERA

| par | recorta | queda fuera |
|---|---|---|
| COBERTURA | lineas **274 a 278**, 699 caracteres | **lineas 632 a 638, 214 caracteres, QUE SI SE PARSEAN** |
| COMMITS | lineas 43 a 66, 1.919 caracteres | nada |
| CABECERA | lineas 22 a 34, 2.621 caracteres | nada |

**El bloque que la guarda protege es el que el ORDEN DEL FICHERO elige; el que el
reporte designa** (*"pegada abajo tras la segunda corrida"*, dicho en su seccion 8)
**es el segundo, y ese no se protegia.**

### 21.d. QUE PASA CON LA CIFRA CUANDO LA LINEA REAL SE PEGA EN EL SEGUNDO BLOQUE

Pegada la linea real de cobertura que la propia guarda produce sobre ese sujeto,
**dentro del SEGUNDO bloque**: la guarda pasa de **VERDE EXIT 0** a **ROJO EXIT 1**,
y las unidades vistas fuera del vocabulario suben de **29 a 34**. Las cinco que
entran son las del propio bloque pegado: `cifras`, `cotejadas`, `exentas`,
`palabra`, `viven`.

### 21.e. CERO DISCREPANCIAS CON EL AUDITOR

Mi medicion coincide con la del acta 144 en los seis numeros que el acta publica:
lineas **274 y 278**, lineas **632 y 638**, y **29 a 34**. **No hay nada que
declarar como discrepante en esta correccion.**

### 21.f. LA REGLA QUE QUEDA

**SI CUALQUIERA DE LAS SEIS MARCAS DE BLOQUE APARECE MAS DE UNA VEZ, ES ROJO POR
AMBIGUA**, nombrando la marca y **todas** sus posiciones. **No se toma la primera.**
Es la misma regla `(iii)` que la TAREA 2.a de la vuelta 144 escribio para la formula
canonica de la excepcion, **el ancla unica**, que la 2.d de esa misma vuelta no
heredo. Vale para **las tres parejas** porque el defecto es de `find` y no de un
bloque. Las otras tres reglas de delimitador **no cambian**.

**Y LA REGLA DE ESCRITURA QUE LA ACOMPANA:** la pareja de marcas aparece
**exactamente una vez** en el reporte; quien necesite citar el mecanismo en la
prosa lo cita **con otro literal**, no con la marca de verdad.

**MUTACION:** `scripts/loop/vuelta145_2a_mutacion_ancla_unica.py`,
[`loop/SALIDA_V145_2A_MUTACION_ANCLA_UNICA.txt`](../loop/SALIDA_V145_2A_MUTACION_ANCLA_UNICA.txt),
**4 de 4**.

---

## CORRECCION 22. **UNA MUTACION DE LA BATERIA LLEVA SUJETO CONGELADO O NO ENTRA**

**Adjudicaciones 4.4 a 4.6 del acta de la vuelta 144** (las tres de la casa, **UNA
SOLA ENFERMEDAD: EL SUJETO VIVO**). Registrada por adicion en la vuelta 145, TAREA
1.c; implementada en la TAREA 2.b. Corte: **2 sep 2026**. Medido por el ejecutor
corriendo cada arnes **sobre el HEAD de apertura y con el arbol limpio**.

### 22.a. CUALES ARNESES VIVOS TOMAN SUJETO VIVO, Y SU VEREDICTO DE HOY

| arnes | de que toma su sujeto | veredicto HOY, arbol limpio | por que |
|---|---|---|---|
| `vuelta144_2d_mutacion_cobertura.py` | `docs/loop/REPORTE.md` **VIVO**, y le agrega SUS PROPIOS delimitadores | **ROJO, 1 de 3** | en cuanto el reporte trae ya un par de marcas, el par que el arnes agrega deja de ser el unico: **(B)** mide sobre el bloque equivocado y **(D)** no puede levantar `ValueError` |
| `vuelta144_3b_mutacion_negativa.py` | el **grafo de hoy**, o sea el mundo DESPUES de su propia fusion | **ROJO, 1 de 3** | su contraprueba **(C)** pide que el sellador salga VERDE y el sellador contesta *"el nodo `formalize_advisory_board` YA esta deprecado"*: **la fusion que sella ya corrio y ese mundo no existe** |
| `vuelta144_2a_guarda_semantica.py` | **WORK contra UN solo ref** (`REF = sys.argv[1] ... else "HEAD"`) | **ROJO** | *"cambian 0 fichas, se esperaba 1"* |
| `vuelta144_3b_guarda_semantica.py` | **WORK contra UN solo ref**, igual | **ROJO** | *"cambian 0 fichas, se esperaba 1"* |

**Y AQUI VA MI UNICA DISCREPANCIA CON EL ACTA 144, DECLARADA EN VEZ DE COPIADA.**
El acta dice que `vuelta144_3b_guarda_semantica.py` *"sigue verde SOLO POR HABER
SIDO LA ULTIMA"*. **Medido hoy sobre el arbol limpio de la apertura, las DOS salen
ROJO, y con el mismo fallo.** La causa es la misma que el acta diagnostica y el
diagnostico **no cambia**: con el arbol limpio `WORK` **es** `HEAD`, asi que no
cambia ninguna ficha y las dos caen. La de la 3.b solo puede salir verde con el
cambio **sin commitear**, que es exactamente lo que esta correccion viene a quitar.

### 22.b. LA BATERIA ENTERA, ANTES

`python scripts/loop/verificar_mutaciones_viejas.py` sobre el HEAD de apertura,
[`loop/SALIDA_V145_1C_VIEJAS_ANTES.txt`](../loop/SALIDA_V145_1C_VIEJAS_ANTES.txt):
**13 mutaciones, ANCLA PERDIDA 0, NO REPRODUCIBLE 0, NO MORDIO 1**
(`vuelta144_2d_mutacion_cobertura.py`), **CASO DECLARADO 2**. **ROJO EXIT 1.**

### 22.c. EL PATRON DE LA CASA QUE YA RESUELVE ESTO

`docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md` (**banco 9.10**), nacido en la vuelta
138 por la misma enfermedad: tres mutaciones ancladas a un literal de
`docs/loop/REPORTE.md`, que se sobreescribe cada vuelta. El sujeto se **congela**, se
**commitea** y las mutaciones lo **cotejan contra el blob de su acta en cada
corrida**. Medido hoy: ese fichero trae **0** ocurrencias de las seis marcas de
bloque, que es justo lo que un sujeto de este caso necesita.

**LA VARIANTE QUE LA VUELTA 145 ANADE, Y SE DECLARA:** cuando el sujeto es un nodo
del catalogo o `docs/plan/OPERACIONES.jsonl`, **no se copia al repositorio: se lee
de un ref de git**. Una copia commiteada de un nodo seria un **segundo nodo con el
mismo id**, que es la clase de duplicado que esta campana persigue. **Git ya es el
congelador y el commit citado es el ancla**
(`scripts/loop/vuelta145_2b_prestado_congelado.py`).

### 22.d. LA REGLA QUE QUEDA, Y CORRIGE LA QUE EL ACTA 144 ESCRIBIO CORTA

El texto viejo, **que no se borra**, decia: *"UNA MUTACION ENTRA EN ESTA BATERIA EN
LA VUELTA SIGUIENTE A LA QUE NACE, NO MAS TARDE."* Le faltaba la mitad:

**UNA MUTACION ENTRA EN `VIEJAS` EN LA VUELTA SIGUIENTE A LA QUE NACE, Y SOLO SI SU
SUJETO ESTA CONGELADO.** La que no pueda tenerlo entra como **CASO DECLARADO**, con
su **exit esperado** y su **motivo escrito en el propio fichero**, como ya hacen
`vuelta135_2e_mutacion_3.py` y `vuelta140_2a_mutaciones.py`.

**POR QUE LA MITAD QUE FALTABA IMPORTA:** sin ella la regla mete en una bateria
permanente arneses que **no pueden ser permanentes**, y el verde de una vuelta **no
sobrevive a la vuelta**. Es lo contrario de fallar ruidoso: es envejecer callado.

### 22.e. QUE SE HIZO CON CADA UNO, Y LA ELECCION JUSTIFICADA MEDIDA

| arnes | salida elegida | medido |
|---|---|---|
| `vuelta144_2d_mutacion_cobertura.py` | **sujeto congelado commiteado**, elegido por computo entre candidatos con la condicion *cero marcas de COBERTURA y como mucho una de cada otra* | vuelve a **3 de 3** |
| `vuelta144_3b_mutacion_negativa.py` | **pre-estado congelado por ref**, con el ref COMPUTADO (`5fff85f7`, padre del `c72ce2c0` que deprecio a los dos absorbidos) | vuelve a **3 de 3** |
| `vuelta144_2a_guarda_semantica.py` | **dos refs**, invocacion canonica `c5a389dd^ c5a389dd` escrita en el docstring | **VERDE** |
| `vuelta144_3b_guarda_semantica.py` | **dos refs**, invocacion canonica `c72ce2c0^ c72ce2c0` escrita en el docstring | **VERDE** |

**SE ELIGIO CONGELAR Y NO DECLARAR EN LOS DOS PRIMEROS, Y EL MOTIVO ES MEDIDO:** un
CASO DECLARADO deja el arnes **excusado y sin morder**; congelado vuelve a **3 de 3**
en los dos. Un arnes congelado que ya no muerde seria peor que uno rojo, asi que
**se comprobo que siguen mordiendo** relajando la guarda que cada uno prueba:
`scripts/loop/vuelta145_2b_mutacion_arneses.py`,
[`loop/SALIDA_V145_2B_MUTACION_ARNESES.txt`](../loop/SALIDA_V145_2B_MUTACION_ARNESES.txt),
**2 de 2**: cada uno **cae** con la guarda relajada y **vuelve a verde** con la
guarda entera.

**LA BATERIA, DESPUES:** de **13 a 19** entradas, **ANCLA PERDIDA 0, NO MORDIO 0, NO
REPRODUCIBLE 0**, **VERDE EXIT 0**
([`loop/SALIDA_V145_2_VIEJAS_TRAS_TAREA2.txt`](../loop/SALIDA_V145_2_VIEJAS_TRAS_TAREA2.txt)).
"""

RUTA = "docs/plan/CORRECCIONES_A_APLICAR.md"


def main():
    t = io.open(RUTA, encoding="utf-8").read()
    if "CORRECCION 21." in t or "CORRECCION 22." in t:
        print("ROJO: ya estan escritas, no se duplica")
        return 1
    io.open(RUTA, "a", encoding="utf-8", newline="\n").write(TEXTO)
    print("anadido por adicion. Lineas ahora: %d"
          % len(io.open(RUTA, encoding="utf-8").read().split("\n")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
