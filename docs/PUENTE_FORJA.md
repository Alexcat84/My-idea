# EL PUENTE DE LA FORJA A LA APP, PROBADO EN SECO (22 sep 2026)

**Rama `puente-forja`, nacida de `main` (`1b128323`).** La forja es el repo hermano
`Alexcat84/forja-nodos`, rama `extraccion-mundo-11`, leida en SOLO LECTURA desde la
carpeta `../forja-nodos` (commit `5aef9f2`, 346 nodos en `dataset/nodos.jsonl`). Nada de
esta tarea escribe en `dataset/` de My-idea, llama a una API ni lee el `.env`.

**Las dos varas que se cotejan:**

- la forja: `esquema/nodo.schema.json` (draft 07, `additionalProperties: false`);
- My-idea: la lista blanca `CAMPOS_PERMITIDOS` y los `OBLIGATORIOS_NO_VACIOS` de
  `scripts/expansion/validar_esquema.py`, que es la misma lista que Gate 0 importa
  (`scripts/run_phase1.py`, comprobacion *Ninguna clave de nodo fuera de la lista
  blanca del esquema*), mas tres comprobaciones de Gate 0 que miran valores:
  `DOMINIOS_PERMITIDOS`, el campo `fuente` contra la lista canonica
  (`scripts/loop/verificar_fuente_canonico.py`, tabla de
  `docs/plan/OP_S_11_MAPEO_PROPUESTO.md`) y `fase_proyecto` en
  `{ideacion, validacion, planificacion, ejecucion}`.

## 1. EL MAPEO, CAMPO POR CAMPO

### Coinciden (mismo nombre, misma forma)

| forja | My-idea | nota |
|---|---|---|
| `resumen_teorico` (texto) | `resumen_teorico` | igual |
| `pasos_accionables` (lista de textos) | `pasos_accionables` | igual |
| `entregable_esperado` (texto) | `entregable_esperado` | igual |
| `ids_alias` (lista de ids) | `ids_alias` | igual; hoy la forja no trae ninguno |
| `nodos_previos` (lista de ids) | `nodos_previos` | igual; la forja las declara dirigidas de madre a hijo, y el seco mide que las 344 estan reciprocadas |
| `nodos_siguientes` (lista de ids) | `nodos_siguientes` | igual |
| `dominio` (texto) | `dominio` | mismo campo, pero **los valores no existen en My-idea** (ver 4) |

### Se renombran o cambian de forma

| forja | My-idea | transformacion |
|---|---|---|
| `id` | `node_id` | renombre; ademas es el nombre del fichero del nodo, como exige `validar_esquema.py` |
| `titulo` | `titulo_concepto` | renombre |
| `condiciones_activacion` (un texto) | `condiciones_activacion` (lista) | el texto pasa a lista de un elemento |
| `fuentes` (lista de `{clave, fecha}`) | `fuente` (un texto) | cada `clave` se resuelve en `fuentes/FUENTES_CANONICAS.json` de la forja a `"Titulo completo - Autor"`, que es la forma mayoritaria de la lista canonica de My-idea; el orden se conserva (el orden es significativo en las dos casas) y se une con `" \| "`, el separador que Gate 0 parte |
| `estado: "deprecado"` | `deprecado: true` | `vivo` no escribe nada; hoy los 346 son `vivo` |

### Faltan en la forja (My-idea los tiene)

| My-idea | obligatorio | que pasa en el pack |
|---|---|---|
| `fase_proyecto` | **SI**, y Gate 0 lo valida contra cuatro valores | queda vacio en los 344; el importador acepta `--fases fases.json` (`{node_id: fase}`) para rellenarlo cuando exista la clasificacion |
| `etiqueta_arbol` | no | queda ausente; la UI cae al titulo por la regla de `AGENTS.md` y el helper `etiquetaArbol()`. Se genera en la integracion, como en todos los packs |
| `merged_originals` | no | no aplica: ningun nodo de la forja es producto de una fusion con procedencia a registrar |

### Sobran en la forja (no tienen destino en el esquema de My-idea)

| forja | nodos que lo traen | que es |
|---|---:|---|
| `denominaciones` (`nombre_largo`, `sigla`, `otros_idiomas`) | 344 | las puertas de busqueda del lector: nombre largo, sigla y termino en otro idioma |
| `escala_minima` | 131 | quien conserva la version ejecutable a escala minima |
| `atribuciones` (`cifra`, `autor`, `fuente`, `fecha_corte`) | 130 | las cifras del autor con su fuente y fecha de corte |
| `marco_pais` | 2 | el marco legal de un pais (`evitar_preguntas_ilegales_entrevista` y `respetar_cautelas_legales_contratacion`: las listas de preguntas prohibidas son de Estados Unidos) |
| `vigencia` | 0 | norma con version o fecha de corte |
| `fuentes[].fecha` | 344 | la fecha de entrada de cada fuente al nodo |

**No se pierden:** el importador los deja, nodo por nodo, en
`<dominio>/metadata/forja_campos_sin_destino.json`, que `integrar_packs.py` no lee. Que
tengan o no un destino en My-idea (un campo nuevo en la lista blanca, o un volcado a un
texto existente) es una decision del fundador, y queda subida en la seccion 4.

## 2. EL IMPORTADOR: `scripts/importar_forja.py`

- **Seco por defecto:** sin banderas escribe el pack en una carpeta temporal del sistema
  (`tempfile.mkdtemp`, prefijo `puente_forja_`) y imprime el informe. Con `--salida DIR`
  escribe donde se diga y **se niega a escribir dentro de `dataset/`**.
- **El pack** tiene la forma que `integrar_packs.py` descubre: `<dominio>/nodos/<node_id>.json`
  (JSON con sangria 2 y acentos, como los packs de la casa) y `<dominio>/metadata/`.
- **Lo que mide:** volumen por dominio y dominios que Gate 0 no admite; ids que colisionan
  con el catalogo de My-idea (id vivo, id deprecado o alias, en los dos sentidos: el id del
  nodo y sus alias); aristas a ids inexistentes, a nodos de la forja que quedan fuera del
  pack, al catalogo de My-idea y sin reciproca; campos obligatorios vacios; el campo `fuente`
  contra la lista canonica; los campos sin destino; y **corre la propia lista blanca de
  My-idea** (`validar_carpeta` de `validar_esquema.py`) sobre el pack recien escrito.
- **Fuera del pack por defecto:** el dominio `forja` (dos nodos del manual interno de la
  casa, `registrar_fuente_canonica` y `elegir_grafia_clave`), que describen como se
  construye la forja y no son contenido del producto. `--incluir-forja` los mete.
- **Su caso rojo, probado:** sobre una copia temporal de la forja con un id cambiado a
  `customer_validation` (vivo en My-idea) y una arista a un id inventado, el informe sale
  con `COLISION> customer_validation: id VIVO en dataset/nodos` y
  `ROTA> informar_efectos_ambientales_productos.nodos_siguientes -> nodo_que_no_existe_mutante`.
  Los ceros de abajo son ceros medidos, no ceros de un instrumento ciego.

## 3. EL INFORME DEL SECO, ENTERO (346 nodos de la forja)

Corrido con `python scripts/importar_forja.py`, sin banderas. La ruta temporal cambia en
cada corrida.

```
INFORME DEL PUENTE DE LA FORJA A LA APP, MODO SECO
forja leida: C:\Users\AlexDesk\Documents\forja-nodos
pack escrito en: <carpeta temporal del sistema, prefijo puente_forja_> (fuera de dataset/)

1. VOLUMEN
   nodos en la forja: 346
   nodos en el pack: 344
   fuera del pack por dominio interno de la forja: 2 ['registrar_fuente_canonica', 'elegir_grafia_clave']
   dominio carrera_profesional      1 nodos
   dominio contratacion            59 nodos
   dominio gestion_equipos        278 nodos
   dominio proteccion_consumidor    6 nodos
   dominios del pack que Gate 0 de My-idea NO admite hoy: ['carrera_profesional', 'contratacion', 'gestion_equipos', 'proteccion_consumidor']

2. IDS QUE COLISIONAN CON EL CATALOGO DE MY-IDEA (id vivo, id deprecado o alias): 0

3. ARISTAS
   aristas a ids INEXISTENTES (ni en la forja ni en My-idea): 0
   aristas a ids de la forja que quedaron FUERA del pack: 0
   aristas a ids del catalogo de My-idea: 0
   aristas dentro del pack SIN su reciproca: 0

4. CAMPOS OBLIGATORIOS DE MY-IDEA VACIOS EN EL PACK
   fase_proyecto                  344 nodos, p. ej. ['formular_codigo_comercializacion_empresarial', 'verificar_afirmaciones_ambientales_publicidad', 'detectar_abusos_contractuales_consumo']
   node_id que no son ascii minuscula: 0 []

5. EL CAMPO fuente CONTRA LA LISTA CANONICA DE MY-IDEA (la que valida Gate 0)
   142 nodos | Radical Candor: Fully Revised and Updated Edition - Kim Scott | canonica en My-idea: NO
   136 nodos | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo | canonica en My-idea: NO
    59 nodos | Who: The A Method for Hiring - Geoff Smart y Randy Street | canonica en My-idea: NO
     6 nodos | Directrices de las Naciones Unidas para la Proteccion del Consumidor - Naciones Unidas, UNCTAD | canonica en My-idea: NO
     1 nodos | High Output Management - Andrew S. Grove | canonica en My-idea: NO
   grafias que Gate 0 rechazaria hoy: 5

6. CAMPOS DE LA FORJA SIN DESTINO EN EL ESQUEMA DE MY-IDEA (viajan en metadata/forja_campos_sin_destino.json)
   atribuciones       130 nodos
   denominaciones     344 nodos
   escala_minima      131 nodos
   fuentes[].fecha    344 nodos
   marco_pais           2 nodos

7. LA LISTA BLANCA DE MY-IDEA (scripts/expansion/validar_esquema.py) SOBRE EL PACK
   carrera_profesional      1 nodos,   2 falla(s)
        1 x obligatorio vacío o ausente: fase_proyecto
        1 x fase_proyecto inválida: 
   contratacion            59 nodos, 118 falla(s)
       59 x obligatorio vacío o ausente: fase_proyecto
       59 x fase_proyecto inválida: 
   gestion_equipos        278 nodos, 556 falla(s)
      278 x obligatorio vacío o ausente: fase_proyecto
      278 x fase_proyecto inválida: 
   proteccion_consumidor    6 nodos,  12 falla(s)
        6 x obligatorio vacío o ausente: fase_proyecto
        6 x fase_proyecto inválida: 

8. LO QUE EL PACK NO TRAE Y integrar_packs.py EXIGE
   metadata/bridges_aprobados.json: NO (prerequisito humano: 10 a 15 puentes por dominio anclados en el nucleo)
   metadata/entry_seeds.json: NO (se hornea a mano por pack)
   problemas de conversion: 0
```

## 4. LO QUE SUBE AL FUNDADOR

**Ids del mundo 11 que colisionan con el catalogo limpio: NINGUNO.** Cero colisiones de id,
vivo, deprecado o alias. El parecido de contenido con nodos ya existentes (por ejemplo, de
contratacion en el nucleo) no es una colision de id: lo mide la aduana semantica A2.6 en la
integracion, con credencial, y ahi se escriben los veredictos continua o repite.

**Campos de la forja sin destino posible en My-idea, y valores que no caben:**

1. **Cinco campos sin destino:** `denominaciones`, `escala_minima`, `atribuciones`,
   `marco_pais` y la fecha de cada fuente. Tres salidas posibles, y la eleccion no es
   tecnica: (a) se quedan en la forja y el pack los aparca en su metadata, como hoy;
   (b) My-idea gana campos nuevos en la lista blanca (tocaria `validar_esquema.py`, Gate 0,
   el sync a la web y el contrato de la web); (c) se vuelcan a un texto existente (por
   ejemplo `marco_pais` al resumen), que cambia el contenido del nodo.
2. **Cuatro dominios que Gate 0 no admite:** `gestion_equipos` (278), `contratacion` (59),
   `proteccion_consumidor` (6) y `carrera_profesional` (1). En My-idea un mundo es un
   dominio. Hay que decidir si el mundo 11 entra como **un** dominio (los cuatro colapsados,
   por ejemplo el futuro mundo *Primer Equipo* que ya tiene ficha en `docs/PENDIENTES.md`) o
   como varios; y en los dos casos el dominio nuevo se registra en `DOMINIOS_PERMITIDOS`,
   en la web y en sus desbloqueos, que es trabajo de producto y no de este puente.
   `proteccion_consumidor` (ONU) y `carrera_profesional` (Grove) no parecen del mismo
   mundo que la gente y la contratacion: se preguntan por separado.

**Lo que falta antes de integrar, y NO es decision del fundador (trabajo del proximo paso):**

- **`fase_proyecto` en los 344 nodos.** Sin el, la lista blanca de My-idea rechaza el pack
  entero (688 fallas, dos por nodo, todas de esta especie). Es una clasificacion por nodo
  que la forja no trae; el importador ya la acepta con `--fases`.
- **Los cinco libros en la lista canonica de My-idea** (`docs/plan/OP_S_11_MAPEO_PROPUESTO.md`),
  o Gate 0 rechaza el campo `fuente` de los 344 nodos.
- **`bridges_aprobados.json` y `entry_seeds.json` por dominio**, que son el prerequisito
  humano de `integrar_packs.py` (10 a 15 puentes anclados en el nucleo) y se hornean a mano.

## 5. GATE 0 Y LAS SUITES, SIN MOVERSE

Corridos en `puente-forja` con el importador y la documentacion ya escritos, y sin tocar
`dataset/`:

| comando | resultado |
|---|---|
| `python scripts/run_phase1.py --reaplico-curaduria` | exitcode 0, **27 comprobaciones OK, 0 FALLO** |
| `python scripts/etiquetas_de_cara.py --aplicar` | exitcode 0 |
| `python scripts/sync_assets_web.py` | exitcode 0 |
| `git diff HEAD --numstat -- dataset/ web/ engine/` | **0 filas**: el grafo y los assets salen identicos a `main` |
| `python engine/run_all_tests.py` | exitcode 0, **25 de 25** |
| `npx tsc --noEmit` (en `web/`) | exitcode 0, limpio |
| `pnpm vitest run` (en `web/`) | exitcode 0, **82 ficheros, 1040 pruebas** |
