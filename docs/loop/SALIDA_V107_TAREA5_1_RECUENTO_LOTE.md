# TAREA 5.1, vuelta 107. Recuento propio del lote antes de correrlo.

Contado hoy contra `docs/loop/CENSO_RELECTURAS_OP_E_03.jsonl` y los cuatro
ficheros de tramo (no copiado del encargo). El encargo cita, del acta de la
vuelta 106 (`docs/loop/_auditor_v106_bolsa.txt`): de las 73 RESUELTA vivas,
ONCE nunca pasaron por la pregunta de tres vias: 3, 5, 7, 10, 13, 16, 19, 27,
30, 33 (tramo1) y 148 (tramo3). De esos once: 3 y 16 con `veces_releido: 0`
(nunca por nada); 5, 7, 10, 13, 19, 27, 30, 33 con `veces_releido: 1` via
relectura ciega entera (vueltas 101 a 103, instrumento mas fuerte pero no la
pregunta de tres vias); 148 resuelto por `correccion_v99`.

Confirmado hoy, puesto por puesto contra el censo:
- 3: veces_releido 0, sin eventos. CONFIRMADO nunca releido.
- 16: veces_releido 0, sin eventos. CONFIRMADO nunca releido.
- 5, 7, 10, 13, 19, 27, 30, 33: veces_releido 1, evento de relectura ciega en
  vueltas 101 a 103 (vuelta102_tarea3_relectura_ciega_tramo1.py o
  vuelta103_tarea4_relectura_ciega_centro.py), NINGUNO trae la pregunta de
  tres vias. CONFIRMADO.
- 148: correccion_v99 (cita), confirmada a ciegas por el acta 98. CONFIRMADO.

**DISCREPANCIA DECLARADA CONTRA EL ENCARGO, DE PROCEDIMIENTO Y NO DE CIFRA:**
el 148 ya recibio la pregunta de tres vias HOY, dentro de la TAREA 4.3 de esta
misma vuelta (el encargo pide el tramo 3 al doble, y 148 es tramo3), antes de
que esta TAREA 5 empezara. Se cuenta como YA HECHO y no se repite.

**EL LOTE VIGENTE DE ESTA TAREA 5, RECONTADO: DIEZ puestos, no once.** Los
mismos diez del tramo1 que el encargo cita (3, 5, 7, 10, 13, 16, 19, 27, 30,
33). Los diez caben bajo el doble del austero (160 pares de tope; diez es una
fraccion minima).
