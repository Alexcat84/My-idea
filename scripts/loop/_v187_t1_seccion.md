### TAREA 1. LOS REGISTROS. **CERRADA.**

**EL NUMERO NO SE TECLEO.** `scripts/loop/serie_de_registros.py`, corrido en esta
vuelta, recomputo la serie de sus **dos sedes** (`docs/PENDIENTES.md` y
`docs/plan/CORRECCIONES_A_APLICAR.md`), hallo **40 entradas**, **0 colisiones**,
**0 huecos**, y devolvio **`R.49`**. El encargo tambien decia `R.49`, y las dos
cifras se publican al lado: **la que manda es la del instrumento**.

**LA ENTRADA ESCRITA:** `## R.49. Registro de las seis adjudicaciones numeradas,
los dos numerales de la seccion 6, las tres preguntas contestadas, las cero
caidas propias del auditor y la caida de reporte del ejecutor del acta de la
vuelta 187`. **Los cinco numerales del titulo estan CONTADOS del acta acotada**
(`docs/loop/ACTA_AUDITOR.md`, lineas **65441 a 66070**, 630 lineas) **y no
tecleados**, incluida la concordancia en palabra.

| que se conto | cifra | de donde sale |
|---|---:|---|
| adjudicaciones `5.1` a `5.6` | **6** | patron entrecomillado sobre el acta acotada |
| el mismo patron SIN comillas, el del acta 183 | **0** | se conserva intacto y su cero se publica |
| numerales de la seccion 6 | **2** | `6.1` y `6.2` |
| preguntas de la seccion 7 | **3** | `7.1`, `7.2` y `7.3`, las tres CONTESTADAS |
| caidas propias del auditor, patron `A.n` | **0** | y **declaradas**: la frase `CERO CAIDAS PROPIAS` esta en la linea **65460** |
| caidas del ejecutor | **1** | la `C.1`, en la linea **65857** |

**LAS SEIS ADJUDICACIONES SON A FAVOR, LAS SEIS.** El acta no regatea ninguna.

**EL ESTADO NUEVO, QUE ES LA PRIMERA DE LAS DOS COSAS QUE ESTE REGISTRADOR
ESTRENA.** El `6.2` del acta 187 no cierra un pendiente, no lo deja abierto y no
es la anotacion de un trabajo ajeno: es una **CORRECCION POR DECLARACION**. El
registrador de la 186 sabia leer `ABIERTA`, `CERRADA` y `ANOTACION`, y con este
titulo habria sacado `SIN DECIR` y habria hecho **PARADA**. El cuarto estado se
lee del titulo con la marca literal `NO ES UN PENDIENTE DE DOCTRINA`, y **la
PARADA se conserva entera**: un estado que el registrador no sabe leer sigue
siendo PARADA y **no se mete en el saco de los abiertos ni en el de los
cerrados**. El reparto medido: **CERRADAS 0, ABIERTAS 1, ANOTACIONES 0,
CORRECCIONES POR DECLARACION 1**.

> **Y LA CONSECUENCIA SE REGISTRA CON TODAS LAS LETRAS: LA `PD.7` DEL REPORTE DE
> LA 186 NO ES UN PENDIENTE DE DOCTRINA, Y EL NUMERO `PD.7` QUEDA LIBRE.**

**LA ATRIBUCION DE LA CAIDA, QUE ES LA SEGUNDA, Y ES LA QUE HABRIA PUBLICADO UNA
CIFRA FALSA.** El patron `C.n` nombraba **las caidas propias del AUDITOR** en las
actas 178 a 184, y el acta 187 usa `C.1` para **la caida del EJECUTOR**. Corrido
a secas sobre esta acta, ese patron da **1**, que es exactamente **una caida
propia del auditor donde el acta declara CERO**. Aqui la atribucion **no la hace
el patron: la hace LA SECCION en que la caida vive**, leyendo su cabecera:

```
   EL PATRON `C.n` A SECAS, SIN MIRAR LA SECCION: 1
   Y REPARTIDO POR LA CABECERA DE SU SECCION, QUE ES LA ATRIBUCION BUENA:
      DEL EJECUTOR: 1
         LINEA 65857: C.1 bajo '## 8. LA CAIDA PROPIA DEL EJECUTOR, Y LE CORRIJO LA ESPECIE'
      DEL AUDITOR: 0
      HUERFANAS (sin dueno declarado en su cabecera): 0
```

**Una `C.n` bajo una cabecera que no dice de quien es sale HUERFANA y hace
PARADA.** Una caida sin dueno no se reparte a ojo.

**LOS CINCO PUESTOS DE LA `PD.1`, LEIDOS DEL ACTA Y NO COPIADOS DEL ENCARGO:**
**1778, 2530, 2540, 3141, 3232**. Sexta vuelta abierta.

**LA DEUDA DE LA SERIE, REMEDIDA HOY Y NO HEREDADA DEL `R.48`:** tramo mirado
actas **173 a 186**, **8 actas sin entrada propia** (**173 a 180**), extremo bajo
**`R.42` cubre el acta 172** y extremo alto **`R.43` cubre el acta 181**. **No se
rellenan aqui.**

**EL CASO POSITIVO POR MUTACION, SOBRE UN ACTA FABRICADA Y NUNCA SOBRE LA REAL**,
que es lo que el encargo manda con esas palabras. **Doce mutaciones, `CIFRA
fallos: 0`, `VEREDICTO: VERDE`.** Las dos que importan hoy:

| mutacion | que prueba | con el esperado mutado |
|---|---|---|
| la **cuarta** | el cuarto estado sale `CORRECCION POR DECLARACION` sobre un acta fabricada, y **no aparece donde no lo hay** | **CAE** |
| la **quinta** | un `6.n` cuyo titulo no dice ninguna de las cuatro marcas sale **`SIN DECIR`**, que es la PARADA | **CAE** |
| la **sexta** | la misma `C.1` bajo cabecera del EJECUTOR es del ejecutor; bajo una sin dueno sale **HUERFANA** | **CAE** |
| la **octava** | los patrones `R.n` y `E.n` dan **0** sobre una caida escrita como `C.n`, y ese cero es la medicion que prueba que hacia falta la atribucion por seccion | |

**IDEMPOTENCIA COMPROBADA ANTES DE ESCRIBIR:** la marca `## R.49.` no estaba en
la sede. Escrita, `docs/PENDIENTES.md` pasa de **909780 a 924954 bytes**, la
entrada se releyo del disco byte a byte, **0 guiones largos o medios**, y la
serie recomputada DESPUES da **41 entradas**, siguiente libre `R.50`, **0
colisiones y 0 huecos**.
