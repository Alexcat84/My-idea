# PARADA: LA COLA DE RELECTURA POST FUSION NO ADMITE LAS `D` (5 sep 2026, vuelta 181)

**Quien la levanta:** el auditor de la vuelta 181 (Opus 5).
**Donde vive el caso completo:** `docs/loop/PARA_ALEXIS.md` y el acta 181
(`docs/loop/ACTA_AUDITOR.md:62907`, seccion 6).
**Condicion de `AUDITOR.md` 4 que se cumple:** doctrina NUEVA necesaria, y cambio de
alcance de la campana, que es de lo que la casa reserva.

## EL CASO MEDIDO

Puesto **2.464**, `cero_defectos` contra `zero_defects_concepto`, quality, clase `D`.
Su razon sostiene la `D` en que uno de los dos *"trae dos cosas que el otro no tiene"*,
y la primera es **eliminar explicitamente el uso de niveles de calidad aceptables**.

**Hoy el otro nodo si lo tiene** (paso 7 de `cero_defectos`, *"Eliminar el lenguaje
que normaliza niveles aceptables de error (AQL)"*).

**Fechado en git, y por eso no es caida de nadie:**

| | |
|---|---|
| veredicto escrito en | `de20c078`, **12 ago 2026** |
| `cero_defectos` ese dia | **6 pasos, sin el del AQL** |
| paso del AQL anadido por | `02384c6a`, **20 ago 2026**, *"VUELTA 60, LOTE B DEL TRAMO 5: QUINCE ACTOS FUNDIDOS"* |
| `cero_defectos` hoy | **7 pasos, con el del AQL** |

## LA REGLA QUE NO ALCANZA

`docs/plan/08_VERIFICACION.md:485`. Su disparador incluye **"o cambia de texto"**; su
filtro de la linea **494** admite solo `B` y `C`, y **razona sobre el nodo que MUERE**:
*"un `D` dice que los dos nodos son sanos, y fundir uno de ellos con un tercero no lo
vuelve gemelo del otro"*.

**Cierto para la muerte. No alcanza al caso en que el otro nodo ABSORBE el paso que era
el diferenciador declarado.**

## EL TAMANO, CONTADO PAR POR PAR CON FECHAS

Salida en `docs/loop/_auditor_v182_alcance_exacto.txt`. Metodo: **194 commits** del
archivo de veredictos para fechar los 3.388 puestos, **119 commits** del grafo desde
el 12 ago para fechar el ultimo cambio de pasos de cada nodo, y **un par cuenta solo si
el cambio es POSTERIOR a su veredicto**.

| clase | total | texto movido despues de su veredicto | la cola los admite |
|---|---:|---:|---|
| A | 551 | **329** | NO |
| B | 72 | **26** | SI |
| C | 5 | **1** | SI |
| **D** | **2.760** | **543** | **NO** |

La cola escrita tiene **siete filas, barridas una vez el 12 ago 2026**. La fusion que
rompio el 2.464 es del 20 ago. **No hubo barrido posterior.** Nodos muertos entre el
12 ago y hoy: **cero**.

## POR QUE NO SE ADJUDICA POR EXTENSION

Precedente de extension citada: **14 ago 2026, vuelta 28**, que metio en esta cola las
costuras que crea un reparto, *"POR EXTENSION CITADA y sin doctrina nueva"*. **Entro
con once filas nombradas.** Esta entraria con **543 mas 329**. Eso es alcance de fase,
no extension.

## LAS PREGUNTAS

1. **Que hace la cola con las `D` cuyo texto se movio**: (a) nada y se escribe por que,
   (b) solo las que tienen el diferenciador declarado hoy en el otro nodo
   **[recomendada]**, (c) las 543 enteras, (d) la (b) ahora y la (c) al cierre.
2. **Que pasa con las 329 `A`** que el filtro tambien excluye. Sin caso medido todavia.
3. **Que precio tiene que el auditor rompa el remedio de su propia caida** (cuarta
   seguida de la `C.1`): (a) que acumule, (b) que el remedio pase a ser codigo
   **[recomendada]**, (c) las dos.
4. **Como corre la bateria**, que lleva cinco vueltas sin correr: (a) por tramos
   obligatorios, con el precedente de los nueve tramos de la 176 **[recomendada]**,
   (b) primero y sola, antes de los registros, lo que requiere tu palabra porque choca
   con `AUDITOR.md` 1.4, (c) podar la nomina, **ya rechazada el 5 sep y no reabierta**.
