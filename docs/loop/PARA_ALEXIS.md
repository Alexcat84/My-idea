# PARA ALEXIS. Parada del bucle, 14 ago 2026

**El bucle esta DETENIDO.** `docs/loop/PROMPT_SIGUIENTE.md` esta vacio a proposito.

---

## 1. EL MOTIVO, en una linea

**Credito de tanda roto: dos tandas seguidas con una caida de cifra publicada del ejecutor.** Es la
regla que afinaste el 13 ago 2026 y que el acta de la vuelta 15 ya dejo escrita por adelantado.

| vuelta | la caida | donde vivia |
|---|---|---|
| 15 | la cobertura del racimo de la mesa unida no era 49 de 136 sino **54 de 136** | `INVENTARIO.jsonl`, `10_INVENTARIO.md` |
| **16** | el acto que crecio entre el corte 2.117 y el 3.388 **no es `construccion_de_leverage`**, es **`gestion_terminacion_franquiciado`, de 2 a 3** | `docs/plan/RECOMPUTO_3388.md` linea 1042 |

**La caida de la vuelta 16, con detalle.** El reporte y el recomputo dicen *"de los 221, 220 son
identicos en tamano y 1 crecio (`construccion_de_leverage`, la competencia entre inversores, de 4 a
5 miembros)"*. Lo medi con tres metodos independientes (superset contra el archivo de componentes,
superset contra las 335 entradas nuevas, e histograma de tamanos) y los tres dan el mismo resultado:
**el unico que crecio es `gestion_terminacion_franquiciado`, de 2 a 3 miembros, ganando
`perdida_control_operativo`**. `construccion_de_leverage` tiene cinco miembros en los dos cortes y
nunca tuvo cuatro.

**Lo que hace que cuente y no sea ruido: el nombre correcto ya estaba escrito en el propio plan.**
La nota de `OP-U-02` dice, con esas palabras, *"UNO crecio (gestion_terminacion_franquiciado con
terminacion_franquiciado_causas, de 2 a 3)"*. El instrumento del ejecutor conto bien ("220 identicos
y 1 crecio") y despues el nombre se copio de una nota vieja de otro objeto y de otra epoca en vez de
leerse de la salida que acababa de producirse. **Es la misma especie de fallo que la vuelta 15: el
instrumento corriendo y la afirmacion saliendo de otro sitio.** Por eso paro: no por el tamano del
error, sino porque el modo de fallo es estable.

---

## 2. LO QUE HAY QUE DECIR A FAVOR, porque tambien esta medido

**Salvo esa linea, la vuelta 16 es la mas verificada de la campaña.** Todo lo siguiente lo medi yo
en esta vuelta con instrumento propio, sin reusar ni uno de los cinco scripts del ejecutor, y todo
sale **exacto**:

- **La tabla de los trece racimos, remedida entera: las trece filas calzan celda por celda**,
  incluida la mesa unida en 54 de 136 con 23 A, 2 B, 2 C y 27 D.
- **El bloque humano de la supervision de la IA: 10 de 10, cinco A y cinco D**, par por par.
- **Las 335 entradas nuevas de tipo `acto`: correspondencia uno a uno exacta** con
  `RECOMPUTO_3388_COMPONENTES.jsonl`, convencion de nombre 556 de 556, 114 huecos nombrados que son
  exactamente las 114 sin antecesor, y la unica nota escrita a mano trasladada con su corte viejo.
- **El campo `operaciones` de las 335, reproducido entero con metodo propio: identico**, con
  `OP-L-03` en 40 y solo en 40, que es el backlog adjudicado.
- **Las tres cubetas de las 53 familias: 23, 14 y 16.**
- **El barrido de citas, 81 de 221: correcto**, y lo prueba su corte (mi barrido daba 84 sobre
  `HEAD` porque el propio reporte cita tres nombres mas; sobre el hash del ejecutor da 81 exacto).
- **Marcador, dominios, integridad de las 69 operaciones, siete sedes de tachado, cero guiones:
  todo exacto.**

---

## 3. ESTADO EXACTO DEL REPO

| | |
|---|---|
| **rama** | `bucle`, arbol limpio, `HEAD` igual a `origin/bucle` |
| **hash** | `7bec35eb` (mas el commit de esta acta) |
| **fase** | **FASE II, RECOMPUTO, abierta.** La FASE III **no** se abrio y `pasada-unica` **no** se creo |
| **marcador** | **A 583 (17,2 %), B 89 (2,6 %), C 7 (0,2 %), D 2.709 (80,0 %); n 3.388, cero huecos, cero duplicados** |
| **cribado** | **CERRADO en 3.388 de 3.388** desde la vuelta 10 |
| **`dataset/`** | **intacto**, ni un byte tocado en toda la FASE II |
| **`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`** | **intacto**, 3.388 lineas |
| **operaciones** | 69, ids unicos, cero dependencias rotas, las 69 en LISTA. **Cero ejecutadas, cero creadas** |
| **inventario** | `docs/plan/INVENTARIO.jsonl` en **671 lineas** (556 acto, 53 familia, 20 figura, 19 defecto, 13 racimo, 10 dominio) |
| **credito acumulado** | 31 relecturas, 382 puestos, 7 caidas de clase, mas 2 caidas de reporte y 2 de cifra publicada del ejecutor, mas 2 de cifra publicada del auditor |

**Nada de lo reservado a ti se toco:** cero merges, cero borrados que ninguna regla ordene, nada
fuera del repo, produccion sin tocar.

---

## 4. LO QUE NECESITO DE TI

**Una sola decision, y son tres opciones:**

1. **RELANZAR EL BUCLE CON EL MISMO EJECUTOR**, aceptando que el credito se reinicia y que el
   encargo de la vuelta 17 empieza por corregir la caida. Es lo mas barato y el trabajo de fondo lo
   respalda.
2. **RELANZAR CAMBIANDO EL MODELO DEL EJECUTOR.** Ya tenias previsto un cambio de modelo antes de
   que se tocara el primer nodo de la FASE III; esta parada cae justo antes de ese punto y es la
   ocasion natural para adelantarlo.
3. **PARAR AQUI Y REVISAR TU LA FASE II** antes de seguir. La FASE II sigue abierta y le faltan
   bloques nombrados (ver punto 6).

**No necesito nada mas: ni credenciales, ni accesos, ni decisiones de alcance.**

---

## 5. COMO RETOMAR

El encargo de la vuelta 17 esta listo para escribirse y son cinco puntos, en este orden. **Los tres
primeros son adjudicaciones ya cerradas de mi acta de la vuelta 16, seccion 3; no hay nada que
decidir en ellos.**

1. **CORREGIR LA CAIDA con tachado y sin borrar**, en `docs/plan/RECOMPUTO_3388.md` linea 1042 y en
   `docs/loop/REPORTE.md`: el que crecio es **`gestion_terminacion_franquiciado`, de 2 a 3**, y el
   ejecutor lo **remide con instrumento propio**, no copia mi cifra. En el tachado queda escrito que
   la caida es del ejecutor y que la fuente correcta ya estaba en la nota de `OP-U-02`.
2. **MARCAR LAS 221 LINEAS VIEJAS COMO SUPERADAS** por el corte 3.388, cada una con el puntero a su
   sucesora (adjudicacion del discutible 1). La lectura aditiva del ejecutor queda, pero **hoy esta
   a medias**: `10_INVENTARIO.md` linea 311 manda al lector a esas entradas como LA fuente para
   contestar "si un nodo repite", y hoy contesta dos veces con dos nominas y dos cortes.
3. **PONER EL AVISO CON TACHADO EN `docs/plan/10_INVENTARIO.md`** (adjudicacion del discutible 3):
   sigue declarando acto 221, TOTAL 336 y corte 2.117, y su linea 313 dice "todo el inventario es
   del 11 ago 2026", que ya es falso para el archivo al que ella misma manda. **No se regenera la
   tabla entera** (eso es el disparador de `08_VERIFICACION`); se le pone el aviso.
4. **REGISTRAR EL HUECO NOMBRADO DEL DISCUTIBLE 2** en la entrada de `OP-I-01`: el campo
   `operaciones` de las 335 hereda lo que el campo `nodos` de las operaciones viejas tenga
   incompleto, y auditarlo operacion por operacion es trabajo de la FASE III.
5. **SEGUIR LA FASE II** por donde estaba: los ejemplares de las veinte figuras, el lote de cinco
   del sales roadmap, la cola de relectura post fusion, el criterio del forastero y las lecturas de
   acto entero de P.5.

---

## 6. LO QUE LE FALTA A LA FASE II PARA CERRAR

Para que lo tengas de un vistazo si eliges la opcion 3:

- **Los ejemplares de las veinte figuras.** Es el bloque grande que queda. El grep quedo descartado
  como instrumento en la vuelta 15 (doce de las veinte dan cero menciones teniendo ejemplares
  declarados), asi que **es trabajo de lectura**, y es el que decide cuando cierra la FASE II.
- El **lote de cinco del sales roadmap**, la **cola de relectura post fusion**, el **criterio del
  forastero** y las **lecturas de acto entero de P.5**.

---

## 7. UNA COSA MIA, para que la peses al decidir

**Mis dos discrepancias de la relectura ciega de esta vuelta fueron mias, no del archivo, y las dos
en la misma direccion: inflar la diferencia.** Es la cuarta vuelta seguida con ese sesgo mio (13,
14, 15 y 16). No cambia la parada, que es del ejecutor y esta medida tres veces, pero **si eliges
cambiar de modelo, considera cambiar tambien el del auditor**: mi patron ya no es casualidad y esta
declarado con nombre en el acta de cada vuelta.
