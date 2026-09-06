### TAREA 3. EL INSTRUMENTO DEL DIFERENCIADOR MOVIDO

Instrumento `scripts/loop/vuelta182_tarea3_diferenciador_movido.py`, salida
`docs/loop/SALIDA_V182_T3_DIFERENCIADOR.txt` (**8.313 bytes**) y la lista en crudo
en `docs/loop/SALIDA_V182_T3_COLA.json` (**1.074 bytes**). Decision del fundador
del 5 sep 2026, PREGUNTA 1, opcion `b`.

**LA CRIBA, CONTADA DE ESE FICHERO Y NO TECLEADA:**

| condicion | cuantas `D` la pasan |
|---|---:|
| todas las `D` del archivo | **2.760** |
| 1. su razon **declara** un diferenciador | **99** |
| 2. y hoy el otro nodo **si lo tiene** | **6** |
| 3. y el paso **entra despues** del veredicto | **1** |

**EL CASO POSITIVO OBLIGATORIO SALE NOMBRADO: EL PUESTO 2.464.** Carece
`cero_defectos`; su **paso 7** de hoy cubre **3 palabras** del diferenciador
declarado con **cobertura 0.50**; veredicto del **2026-08-12** y el paso entra el
**2026-08-20**. **El acta 181 lo fecha a mano en `02384c6a`, 20 ago 2026, y
calzan**, sin que este instrumento le copie ninguna cifra.

**LAS VARAS NO SE ELIGEN A OJO.** El instrumento imprime el barrido entero de las
dos (`abs` 2 a 5 por cobertura 0.30 a 0.70) con cuantas `D` selecciona cada celda,
y la elegida (**abs 3, cobertura 0.45**) es **la celda mas estrecha que sigue
nombrando el 2.464**. La tabla va dentro de la salida para que la eleccion se
pueda discutir.

**DOS CORRECCIONES MIAS, LAS DOS CON SU SALIDA VIEJA GUARDADA:**

1. El contenido declarado se juzgaba **en bloque** y el 2.464 daba cobertura
   **0.19** y no salia. La razon enumera **dos cosas** separadas por punto y coma:
   **un diferenciador enumerado en dos se ha movido si se mueve uno.** Con el corte
   por punto y coma la primera da **0.50**.
2. El fechado buscaba el texto del paso **en el blob entero** del grafo y fechaba
   el paso del AQL el **2026-07-10**, contra el 20 ago que el acta 181 fecha a
   mano. **Ese texto vivia en otro nodo antes de la fusion.** Ahora se busca
   **dentro de su nodo**, parseando cada uno de los **165 commits** del grafo una
   sola vez para los seis pares. La salida equivocada queda entera en
   `docs/loop/SALIDA_V182_T3_DIFERENCIADOR_FECHADO_MALO.txt` (**7.894 bytes**).

**EL CENSO POR ESTADO DE LAS `A`, en el mismo instrumento:** **551** `A`, de ellas
**0 ejecutadas**, **551 pendientes** y **0 no decidibles**; la suma calza con 551.
De las pendientes, **8** tienen hoy su diferenciador declarado en el otro nodo y
quedan **marcadas RANCIAS por `P.5`**: **978, 2230, 2255, 2272, 2414, 2420, 2498 y
2509**. **No se encolan**, por la PREGUNTA 2 de la misma decision.

Caso positivo por mutacion **VERDE** con material fabricado
(`docs/loop/SALIDA_V182_T3_MUTACION.txt`, **1.607 bytes**): **5 casos, 5 calzan**,
el esperado mutado **CAE** y con la vara imposible la lesion **desaparece**. Ni el
archivo ni `dataset/` se leen en la mutacion.

> **ESTE INSTRUMENTO NO CAMBIA NINGUN VEREDICTO, no toca el marcador y no toca
> `docs/plan/`.** Solo mide y nombra. Encolar es la TAREA 4.
