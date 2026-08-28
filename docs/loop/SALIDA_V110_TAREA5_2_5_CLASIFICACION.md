# TAREA 5, vuelta 110: la especie de la construccion de dos argumentos, AL DOBLE

## 5.1 EL LOTE (cifra tallada de codigo, docs/loop/SALIDA_V110_TAREA5_1_LOTE_PREPOSICIONAL.txt)

`python scripts/loop/vuelta110_tarea5_lote_preposicional.py`: **74 RESUELTA vivas**, **63 con
preposicion** (con/por/a/de/en/hacia/contra) en el `paso_casado` LITERAL (resuelto por id contra
`master_graph.json`, no el texto de la razon), **11 SIN preposicion** (2, 3, 14, 46, 53, 57, 59,
99, 111, 169, 179). 63 cabe entero bajo el doble del austero (160): no se parte por tramo.

## 5.2 LA PARTICION, por la unica pregunta que importa

**Grupo 2 (EXIGE el segundo termino, no puede ser SATELITE):** el verbo, POR SI SOLO, no completa
su sentido sin el termino regido por la preposicion (no es un adjunto de instrumento, criterio,
tiempo o lugar, ni un complemento anidado DENTRO del objeto o de un sustantivo relacional como
"relaciones con", "gates con criterios"). Leidos los 63 uno a uno, la especie EXACTA de "combinar
A con B / reemplazar X por Y / vincular A a B / diferenciar X de Y" solo aparece en:

- **13** `waterfall_vs_agile_development` p3: "Alinear el proceso de desarrollo de producto CON el
  proceso de Customer Development" -- alinear A con B.
- **49** `terminologia_clave_breakthrough` p2: "Diferenciar sintomas DE causas" -- diferenciar X de Y.
- **97** `principios_alineacion_empresarial` p3: "Alinear estrategias... CON el proposito central"
  -- alinear A con B.
- **123** `eliminacion_inspeccion_masiva_por_control_estadistico` p3: "Reemplazar inspeccion 100%
  POR muestreo estadistico" -- reemplazar X por Y.
- **145** `poder_a_traves_de_la_accion` p4: "Vincular... el trabajo intelectual cotidiano A un
  proposito o impacto mayor" -- vincular A a B.
- **154** `desarrollo_de_clientes_customer_development` p4: "Combinar el aprendizaje del cliente
  CON ingenieria agil" -- combinar A con B.

**Grupo 1 (el verbo SE COMPLETA con su objeto directo solo, el complemento PUEDE ser satelite):**
los 57 restantes de los 63. Verbos dominantes: evaluar (10, 30, 87, 102, 132, 148), definir/
identificar (27, 33, 45, 47, 58, 83, 84, 101, 114, 158, 177), medir (18, 77, 134), clasificar (48,
64), establecer (91, 127, 156), y el resto de la misma especie (transitivo, objeto completo sin
el termino preposicional). Caso limite anotado, NO forzado a grupo 2: **4**
`consejo_de_calidad_y_rol_del_director` p3 "Integra las metas de calidad EN tus planes de
negocio" -- "integrar X en Y" tiene aire de dos argumentos, pero la propia fila ya registrada
(SALIDA_V105_TAREA4_3_RE_BARRIDO.txt) lo trata como Grupo 1 desde la vuelta 105 ("'en tus
planes...' es complemento ADICIONAL, no el unico lugar donde vive el hijo"), y "integrar" no esta
en la lista cerrada de cuatro verbos que trajo el encargo: se deja en Grupo 1, judgment call
declarado, y de todos modos NO CAMBIA NADA (Grupo 1 admite cualquier veredicto).

## 5.3 LA VARA: el veredicto registrado, CONTRA el grupo

Por definicion el Grupo 1 admite cualquier veredicto (el complemento PUEDE ser satelite, no tiene
que serlo): ningun par de ese grupo puede producir una contradiccion con esta prueba. La cosecha
solo puede salir del Grupo 2 (donde SATELITE es estructuralmente imposible). Los seis del Grupo 2,
veredicto registrado HOY (tras la correccion_v110 del 154 en la TAREA 3 de esta misma vuelta):

| puesto | veredicto registrado | calza |
|---|---|---|
| 13  | OBJETO | SI |
| 49  | OBJETO | SI |
| 97  | OBJETO | SI |
| 123 | OBJETO | SI |
| 145 | OBJETO | SI |
| 154 | OBJETO | SI |

**COSECHA: 0.** Los seis ya estaban OBJETO (123 y 145 corregidos en la vuelta 107/109, 13 y 97
clasificados asi desde su primera lectura en la vuelta 107 con la MISMA razon de dos argumentos,
154 corregido en la TAREA 3 de esta vuelta). Ninguno contradice su grupo.

## 5.4 Cobertura

63 de 63 leidos esta vuelta. No hace falta partir por tramo (cabe bajo el doble del austero).

## 5.5 Veredicto de la tarea

**Ninguno se mueve.** No hay hallazgo que forzar: el barrido de la vuelta 106 fallaba
especificamente en la especie "verbo de dos argumentos + complemento con preposicion" (109, 123,
145, y ahora 154), y las CUATRO instancias reales de esa especie exacta en todo el lote de 74
RESUELTA vivas (13, 97, 123, 145; mas 49 y 154 que no vinieron del barrido 106 sino de otras
lecturas) ya estan corregidas. No queda ninguna mas por corregir en esta pasada.
