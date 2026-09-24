NECESITO AL FUNDADOR: no hay texto fuente accesible para NINGUNO de los 23 libros del sorteo (ni para ningun libro del catalogo del tag). Hace falta que indiques la ruta de los libros; la candidata es `C:\Users\AlexDesk\Documents\I have an idea\books` (ver seccion 6), que no lei porque no estaba autorizada.

# MUESTREO DE FIDELIDAD, septiembre 2026: REPORTE

**Tasa global: NO MEDIBLE.** Pasos INFERIDOS: 0 de 0 con veredicto (intervalo de Wilson al 95 por ciento no definido, n = 0). Pasos CONTRARIOS: 0 de 0 con veredicto (intervalo no definido, n = 0). Los 30 nodos sorteados suman 138 pasos, y los 138 quedaron SIN VEREDICTO porque ningun libro de la muestra esta en las fuentes permitidas (Drive "My idea" y `forja-nodos\fuentes\`). Esto NO es una tasa de cero: es ausencia de medida.

**Umbral del encargo** (libro con mas del 10 por ciento de INFERIDOS o con un solo CONTRARIO): no evaluable para ningun libro. La primera linea pide al fundador la fuente, no senala un libro infiel.

**Hashes.** Pre-registro (semilla, metodo y criterios, sin resultados, antes de sortear): `c038586dc3e64e2b998c78b64a517b55905785c5` (2026-09-23 22:48:45 -0400). Resultado: el commit que anade este bloque, en la rama `muestreo-fidelidad` (su hash va en el mensaje de cierre de la sesion: un fichero no puede citar el hash del commit que lo contiene). Las secciones 0 a 5 del pre-registro, mas abajo, no cambian en el commit de resultado: `git diff c038586d -- docs/audits/MUESTREO_FIDELIDAD_2026-09.md` solo muestra este bloque anadido arriba, la seccion 6 rellenada y el anexo.

## R1. Tablas por mundo y por libro

Por mundo:

| mundo | nodos | pasos | con veredicto | INFERIDO (IC95) | CONTRARIO (IC95) | fuente disponible |
|---|---:|---:|---:|---|---|---|
| compras | 2 | 9 | 0 | no definido | no definido | no |
| core | 7 | 30 | 0 | no definido | no definido | no |
| entrega | 2 | 9 | 0 | no definido | no definido | no |
| environmental | 3 | 11 | 0 | no definido | no definido | no |
| exportacion | 2 | 12 | 0 | no definido | no definido | no |
| franquicias | 3 | 14 | 0 | no definido | no definido | no |
| health_safety | 3 | 14 | 0 | no definido | no definido | no |
| quality | 4 | 21 | 0 | no definido | no definido | no |
| risk_management | 2 | 8 | 0 | no definido | no definido | no |
| seguridad_digital | 2 | 10 | 0 | no definido | no definido | no |
| **total** | **30** | **138** | **0** | **no definido** | **no definido** | |

Mundos con fuente disponible: **ninguno**. Por la regla del encargo, ninguno cuenta para el minimo de dos por mundo.

Por libro (primer libro del campo `fuente`; ninguno de los 30 nodos sorteados tiene fuente multiple):

| libro | mundo | nodos | pasos | con veredicto | INFERIDO | CONTRARIO |
|---|---|---:|---:|---:|---|---|
| Chris Voss, Rompe la barrera del no | compras | 1 | 4 | 0 | no definido | no definido |
| Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) | compras | 1 | 5 | 0 | no definido | no definido |
| Value Proposition Design | core | 1 | 5 | 0 | no definido | no definido |
| The Founder's Dilemmas - Wasserman, Noam | core | 2 | 8 | 0 | no definido | no definido |
| Winning at New Products - Robert G. Cooper | core | 1 | 4 | 0 | no definido | no definido |
| Venture Deals - Brad Feld | core | 1 | 5 | 0 | no definido | no definido |
| Assembling Tomorrow: A Guide to Designing a Thriving Future | core | 1 | 4 | 0 | no definido | no definido |
| The Startup Owner's Manual - Blank, Steve | core | 1 | 4 | 0 | no definido | no definido |
| Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management | entrega | 1 | 5 | 0 | no definido | no definido |
| Requisitos de empaque de los couriers | entrega | 1 | 4 | 0 | no definido | no definido |
| The Green to Gold Business Play - Daniel C. Esty | environmental | 1 | 4 | 0 | no definido | no definido |
| Cradle to Cradle - Michael Braungart | environmental | 2 | 7 | 0 | no definido | no definido |
| A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) | exportacion | 2 | 12 | 0 | no definido | no definido |
| Franchise Your Business - Mark Siebert | franquicias | 3 | 14 | 0 | no definido | no definido |
| Managing the Risks of Organizat - Reason, J. T_ | health_safety | 2 | 8 | 0 | no definido | no definido |
| OSHA3885 | health_safety | 1 | 6 | 0 | no definido | no definido |
| Quality is free _ the art of making quality certain -- Philip B_ Crosby | quality | 1 | 9 | 0 | no definido | no definido |
| Juran's Quality Handbook_ The C - Joseph A. Defeo | quality | 2 | 8 | 0 | no definido | no definido |
| Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev | quality | 1 | 4 | 0 | no definido | no definido |
| Edwards et al., Managing Project Risks | risk_management | 1 | 4 | 0 | no definido | no definido |
| Hubbard, The Failure of Risk Management | risk_management | 1 | 4 | 0 | no definido | no definido |
| NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer | seguridad_digital | 1 | 5 | 0 | no definido | no definido |
| Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework (FTC) | seguridad_digital | 1 | 5 | 0 | no definido | no definido |

## R2. Nodos con algun CONTRARIO

Ninguno registrado, porque no se leyo ningun paso. No es evidencia de que no los haya.

## R3. Script de tasas y su salida

Script (Python 3.12.8), el que servira tal cual cuando haya veredictos; `VEREDICTOS` va vacio porque no hay ninguno:

```python
# Tasas de INFERIDO y CONTRARIO con Wilson 95, por paso y por nodo.
# VEREDICTOS: lista de (node_id, mundo, libro, paso, veredicto); veredicto en FIEL, INFERIDO, CONTRARIO.
# Los pasos SIN FUENTE no entran. En esta corrida no hay ningun paso con veredicto.
import math
from collections import defaultdict
Z = 1.959964
VEREDICTOS = []
def wilson(k, n):
    if n == 0:
        return None
    p = k / n
    d = 1 + Z * Z / n
    c = (p + Z * Z / (2 * n)) / d
    h = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d
    return (c - h, c + h)
def fila(nombre, vs):
    n = len(vs)
    for v in ("INFERIDO", "CONTRARIO"):
        k = sum(1 for x in vs if x[4] == v)
        ic = wilson(k, n)
        print(nombre, v, f"{k}/{n}", "no definido (n=0)" if ic is None else f"{k/n:.3f} [{ic[0]:.3f}, {ic[1]:.3f}]")
fila("GLOBAL por paso", VEREDICTOS)
nodos = defaultdict(list)
for x in VEREDICTOS:
    nodos[x[0]].append(x[4])
for v in ("INFERIDO", "CONTRARIO"):
    k = sum(1 for vs in nodos.values() if v in vs)
    ic = wilson(k, len(nodos))
    print("GLOBAL por nodo, nodos con algun", v, f"{k}/{len(nodos)}", "no definido (n=0)" if ic is None else f"[{ic[0]:.3f}, {ic[1]:.3f}]")
for clave, idx in (("mundo", 1), ("libro", 2)):
    grupos = defaultdict(list)
    for x in VEREDICTOS:
        grupos[x[idx]].append(x)
    print("por", clave, ":", len(grupos), "grupos con veredicto")
    for gname, vs in sorted(grupos.items()):
        fila(gname, vs)
# comprobacion de la formula con un caso a mano: 2/10 -> Wilson 95 = [0.0567, 0.5098]
print("control wilson(2,10)", tuple(round(x, 4) for x in wilson(2, 10)))
```

Salida literal:

```
GLOBAL por paso INFERIDO 0/0 no definido (n=0)
GLOBAL por paso CONTRARIO 0/0 no definido (n=0)
GLOBAL por nodo, nodos con algun INFERIDO 0/0 no definido (n=0)
GLOBAL por nodo, nodos con algun CONTRARIO 0/0 no definido (n=0)
por mundo : 0 grupos con veredicto
por libro : 0 grupos con veredicto
control wilson(2,10) (0.0567, 0.5098)
```

Control de la formula calculado a mano: 2 de 10, z al cuadrado = 3,8415; centro = (0,2 + 0,1921) / 1,3841 = 0,2833; semiancho = 1,96 x raiz(0,0160 + 0,0096) / 1,3841 = 1,96 x 0,1600 / 1,3841 = 0,2266; intervalo [0,0567, 0,5098], igual que la salida.

## R4. Limitaciones

1. **La principal: ninguna fuente.** Ni Drive "My idea" ni `forja-nodos\fuentes\` contienen ninguno de los libros del catalogo del tag. Las dos carpetas guardan solo los libros del mundo 11 y el reservado del mundo 10 (onu_consumidor, smart_who, zhuo_manager, scott_radical_candor, marquet_turn_the_ship, grove_high_output, gerber_emyth, bernerslee_bananas, openstax_business_ethics, openstax_org_behavior). Esos libros entraron al catalogo DESPUES del tag (el lote 1, onu_consumidor, se inserto el 10 sep 2026 segun `forja-nodos\fuentes\FUENTES_CANONICAS.json`; el commit del tag es del 9 sep), y ningun nodo vivo del tag los tiene en `fuente`. Detalle de la busqueda en la seccion 6.
2. **Intervalo por paso y conglomerado.** Declarado en el pre-registro (seccion 5): los pasos se agrupan en nodos, asi que el intervalo por paso subestima la incertidumbre; el script da tambien el intervalo por nodo. Sin veredictos, los dos quedan indefinidos.
3. **Muestra no proporcional.** Piso de 2 por mundo: la global de la muestra no es un estimador ponderado del catalogo (seccion 5).
4. **Un solo lector.** Cuando se lea, los veredictos seran de un solo lector, sin segundo juez ciego.
5. **La muestra queda fijada.** El sorteo esta hecho y es reproducible con la orden de la seccion 4; la sesion que tenga la fuente debe leer ESTOS 30 nodos, no sortear otros, y rellenar la tabla del anexo.

---

# PARTE II: PRE-REGISTRO (secciones 0 a 5 tal como se commitearon en c038586d)

# MUESTREO DE FIDELIDAD, septiembre 2026

Estado de este fichero: **PRE-REGISTRO**. Esta version se commitea SIN resultados y ANTES de sortear. Contiene la semilla, el metodo de sorteo exacto, las definiciones y los criterios de veredicto. El reporte final citara el hash de este commit como prueba de que la semilla precede al sorteo.

## 0. Encargo y marco

- Encargo del fundador (Alexis, alexcat84), 23 sep 2026: medir la FIDELIDAD de los nodos vivos a su libro fuente, con 30 nodos al azar estratificados por mundo, paso a paso contra el texto, sin corregir nada.
- Repo: github.com/Alexcat84/My-idea, tag `catalogo-limpio-v1` (objeto tag `68e258d05613e610df9e1851b5a353103f6be026`, commit `1b12832392469afd2ac42775d606e4dfd443ab43`, fecha del commit 2026-09-09). Rama de trabajo `muestreo-fidelidad`, creada desde ese tag.
- Catalogo leido: `dataset/metadata/master_graph.json` en el tag, sha256 `c36775b8f622c709b6b3ced92c659f74a8f93c9c84023139508e521f219112c6`, `total_nodos` 3853.
- Sesion de solo lectura: no se escribe en `dataset/` ni se corrige nada. Un solo fichero de resultado (este).

## 1. Definiciones (sacadas del repo, no inventadas)

**Nodo vivo.** Un nodo de `master_graph.json["nodos"]` cuyo campo `deprecado` no es verdadero. Fuente de la definicion: la puerta unica de oferta `esOfrecible` en `web/lib/engine/graph.ts` (lineas 212 a 243 en el tag), que exige "que el nodo exista en el grafo" y "que NO este deprecado (fusionado dentro de otro: sigue existiendo para que la historia resuelva, pero ya no se ofrece)". El tercer filtro de esa puerta (dominio desbloqueado para un proyecto) es por usuario, no por nodo, y no entra en la definicion. `docs/AUDITORIA_MOTOR.md` usa la misma particion ("ningun nodo, vivo ni deprecado"). Medido en el tag: 3853 nodos, 684 con `deprecado: true`, **3169 vivos**.

**Mundo.** El valor del campo `dominio` del nodo. Fuente: `docs/BANCO_DE_TEXTOS.md` (seccion 7.1 y la decision de pertenencia: el espacio "viaja como campo `dominio`"), los paquetes de `packs/` (uno por dominio) y `DOMINIOS_DESBLOQUEADOS_DEFECTO = ["core"]` en `web/lib/engine/graph.ts`. `core` es el nucleo (gratis, abierto por defecto) y los otros nueve son los mundos de pago; para este muestreo el nucleo cuenta como un estrato mas, porque el encargo pide medir los nodos vivos, y el nucleo tiene el 45 por ciento de ellos. Diez estratos, con sus vivos en el tag:

| mundo (`dominio`) | vivos |
|---|---:|
| compras | 46 |
| core | 1439 |
| entrega | 47 |
| environmental | 265 |
| exportacion | 131 |
| franquicias | 182 |
| health_safety | 260 |
| quality | 692 |
| risk_management | 55 |
| seguridad_digital | 52 |
| **total** | **3169** |

**Libro.** El valor del campo `fuente` del nodo. Si el campo lista varios libros separados por ` | ` (8 nodos vivos en el tag, todos del nucleo), el nodo se atribuye al PRIMER libro listado para las tablas por libro, y se lee contra todos los listados.

**Paso.** Cada elemento de la lista `pasos_accionables` del nodo, tal como esta en el tag.

**Capitulo fuente.** Los nodos del tag no guardan capitulo. Se localiza buscando en el texto del libro el concepto del nodo (`titulo_concepto`, `resumen_teorico` y los terminos de sus pasos) y se toma el capitulo o seccion donde el libro lo desarrolla. Se anota el capitulo y la ruta o id del texto.

## 2. Fuentes permitidas, por este orden

1. Google Drive del fundador, carpeta "My idea", solo lectura.
2. Si Drive no tiene el texto: `C:\Users\AlexDesk\Documents\forja-nodos\fuentes\`, solo lectura con Read, Grep o cat, nunca con git.
3. Ninguna otra ruta, salvo que el fundador la indique.

Un nodo cuyo libro no este en esas fuentes queda **SIN FUENTE**: no se le da veredicto, no entra en las tasas y se lista aparte. Un mundo sin ningun libro disponible se declara y no cuenta para el minimo de dos por mundo.

## 3. Criterios de veredicto (fijados antes de sortear)

Cada paso recibe exactamente uno:

- **FIEL**: el libro dice la accion del paso (su verbo y su objeto), en esa forma o en una parafrasis directa, en el capitulo fuente o en otro lugar del mismo libro. Traducir, resumir o reordenar lo que el libro dice es FIEL. Se cita la linea (o la frase literal si el texto no tiene lineas).
- **INFERIDO**: el paso es razonable y compatible con el libro, pero el libro no lo dice asi: la accion, su objeto, su cifra, su secuencia o su alcance lo anade el extractor. Tambien es INFERIDO un paso que convierte en instruccion algo que el libro solo describe, cuando la instruccion concreta no esta en el texto. Antes de marcar INFERIDO se busca el concepto (no solo la frase) en todo el capitulo y en el indice del libro; se cita el pasaje mas cercano y se dice que falta.
- **CONTRARIO**: el libro dice otra cosa: recomienda lo opuesto, advierte contra esa accion, da otra cifra o secuencia, o atribuye la idea a lo contrario de lo que el paso afirma. Se cita la linea que lo contradice. Antes de marcar CONTRARIO se busca en todo el libro que no haya otro pasaje que respalde el paso.

Regla de duda: entre FIEL e INFERIDO, si la accion concreta no esta en el texto, es INFERIDO. Entre INFERIDO y CONTRARIO, solo es CONTRARIO si hay una cita que lo contradiga; la mera ausencia es INFERIDO.

## 4. Semilla y metodo de sorteo (fijados antes de sortear)

- **Semilla: `20260923`.**
- Python 3.12.8 (`3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]`), generador `random.Random(SEED)` (Mersenne Twister de la biblioteca estandar).
- Tamano: 30 nodos vivos. Asignacion: 2 por mundo (20) y los 10 restantes en proporcion a los vivos de cada mundo, por el metodo del mayor resto (empate de restos: orden alfabetico del mundo).
- Orden: los mundos en orden alfabetico; dentro de cada mundo, los `node_id` vivos ordenados alfabeticamente; de ahi `rng.sample(lista, n_mundo)`, un unico generador que recorre los mundos en ese orden.
- El sorteo cubre los diez mundos sin mirar si su libro esta disponible, para que la disponibilidad de la fuente no pueda sesgar que nodos salen. La disponibilidad se mira despues, nodo por nodo (seccion 2).
- Orden exacta de ejecucion, desde la raiz del clon en el tag, extrayendo el script de ESTE fichero para que lo ejecutado sea lo commiteado:

```
sed -n '/^# INICIO SORTEO$/,/^# FIN SORTEO$/p' docs/audits/MUESTREO_FIDELIDAD_2026-09.md | python -
```

```python
# INICIO SORTEO
import hashlib, json, random, sys
SEED = 20260923
N_TOTAL = 30
MIN_POR_MUNDO = 2
RUTA = "dataset/metadata/master_graph.json"
print("python", sys.version)
print("sha256", hashlib.sha256(open(RUTA, "rb").read()).hexdigest())
g = json.load(open(RUTA, encoding="utf-8"))["nodos"]
vivos = {nid: n for nid, n in g.items() if not n.get("deprecado")}
mundos = sorted({n["dominio"] for n in vivos.values()})
ids = {m: sorted(nid for nid, n in vivos.items() if n["dominio"] == m) for m in mundos}
total = sum(len(v) for v in ids.values())
print("nodos", len(g), "vivos", total, "mundos", len(mundos))
asig = {m: MIN_POR_MUNDO for m in mundos}
resto = N_TOTAL - MIN_POR_MUNDO * len(mundos)
cuota = {m: resto * len(ids[m]) / total for m in mundos}
for m in mundos:
    asig[m] += int(cuota[m])
faltan = N_TOTAL - sum(asig.values())
for m in sorted(mundos, key=lambda m: (-(cuota[m] - int(cuota[m])), m))[:faltan]:
    asig[m] += 1
print("asignacion", json.dumps(asig, sort_keys=True))
rng = random.Random(SEED)
k = 0
for m in mundos:
    for nid in rng.sample(ids[m], asig[m]):
        k += 1
        n = vivos[nid]
        print(k, m, nid, len(n["pasos_accionables"]), n["fuente"], sep="\t")
# FIN SORTEO
```

## 5. Estadistica (fijada antes de sortear)

- Unidad de tasa: el paso. Tasa de INFERIDOS = pasos INFERIDOS / pasos con veredicto; lo mismo para CONTRARIOS. Global, por mundo y por libro.
- Intervalo: Wilson al 95 por ciento (z = 1.959964), con la formula cerrada, sin correccion de continuidad.
- Limitacion declarada de antemano: los pasos se agrupan en nodos (efecto de conglomerado), asi que el intervalo por paso es demasiado estrecho. Se anade un intervalo por nodo: proporcion de nodos con al menos un paso INFERIDO (y con al menos un CONTRARIO), con Wilson sobre el numero de nodos.
- Las tasas son de la muestra; la estratificacion no es proporcional (piso de 2 por mundo), asi que la tasa global de la muestra no es un estimador ponderado del catalogo. Si hace falta, se da ademas la global ponderada por vivos de cada mundo.
- Umbral del encargo: un libro con mas del 10 por ciento de pasos INFERIDOS, o con un solo CONTRARIO, abre el reporte con NECESITO AL FUNDADOR.

## 6. Resultados

### 6.1 El sorteo: orden y salida literal

Ejecutado despues del commit del pre-registro (`c038586d`, 2026-09-23 22:48:45 -0400), desde la raiz del clon, con HEAD en ese commit:

```
$ git rev-parse HEAD
c038586dc3e64e2b998c78b64a517b55905785c5
$ sed -n '/^# INICIO SORTEO$/,/^# FIN SORTEO$/p' docs/audits/MUESTREO_FIDELIDAD_2026-09.md | PYTHONIOENCODING=utf-8 python -
python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]
sha256 c36775b8f622c709b6b3ced92c659f74a8f93c9c84023139508e521f219112c6
nodos 3853 vivos 3169 mundos 10
asignacion {"compras": 2, "core": 7, "entrega": 2, "environmental": 3, "exportacion": 2, "franquicias": 3, "health_safety": 3, "quality": 4, "risk_management": 2, "seguridad_digital": 2}
1	compras	muestra_puntos_en_comun_antes_de_negociar	4	Chris Voss, Rompe la barrera del no
2	compras	domina_lo_que_compras	5	Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014)
3	core	extraer_priorizar_hipotesis	5	Value Proposition Design
4	core	identificacion_necesidad_sucesion_ceo	4	The Founder's Dilemmas - Wasserman, Noam
5	core	equipo_dedicado_continuo	4	Winning at New Products - Robert G. Cooper
6	core	mejorar_deal_despues_del_hecho	5	Venture Deals - Brad Feld
7	core	playing_with_fire_gap	4	The Founder's Dilemmas - Wasserman, Noam
8	core	diseno_etico_de_privacidad	4	Assembling Tomorrow: A Guide to Designing a Thriving Future
9	core	analisis_trafico_competitivo	4	The Startup Owner's Manual - Blank, Steve
10	entrega	saber_hasta_donde_mejorar_servicio	5	Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management
11	entrega	aplicar_regla_fija_de_colchon_de_relleno	4	Requisitos de empaque de los couriers
12	environmental	estrategia_proactiva_ambiental	4	The Green to Gold Business Play - Daniel C. Esty
13	environmental	volverse_nativo_del_lugar	3	Cradle to Cradle - Michael Braungart
14	environmental	cinco_principios_guia_transformacion	4	Cradle to Cradle - Michael Braungart
15	exportacion	tipos_sitio_web_exportacion	4	A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition)
16	exportacion	clausula_escape_contrato_representante	8	A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition)
17	franquicias	brokers_lead_referral_networks	5	Franchise Your Business - Mark Siebert
18	franquicias	folleto_franquicia	4	Franchise Your Business - Mark Siebert
19	franquicias	embudo_ventas_franquicia	5	Franchise Your Business - Mark Siebert
20	health_safety	autonomia_dependencia_regulatoria	4	Managing the Risks of Organizat - Reason, J. T_
21	health_safety	prevalencia_omisiones	4	Managing the Risks of Organizat - Reason, J. T_
22	health_safety	participacion_trabajadores	6	OSHA3885
23	quality	accion_correctiva_sistematica	9	Quality is free _ the art of making quality certain -- Philip B_ Crosby
24	quality	decision_conformidad_producto	4	Juran's Quality Handbook_ The C - Joseph A. Defeo
25	quality	pruebas_inadecuadas_prototipos	4	Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev
26	quality	sistema_de_alarma_de_defectos	4	Juran's Quality Handbook_ The C - Joseph A. Defeo
27	risk_management	plan_de_desastre_y_recuperacion	4	Edwards et al., Managing Project Risks
28	risk_management	escepticismo_sano_ante_el_riesgo	4	Hubbard, The Failure of Risk Management
29	seguridad_digital	getting_started_system_information_integrity	5	NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer
30	seguridad_digital	funcion_respond_plan_incidentes	5	Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework (FTC)
```

(`PYTHONIOENCODING=utf-8` solo fija la codificacion de la consola de Windows; no cambia el sorteo.)

### 6.2 Donde se busco la fuente de cada nodo

Para los 30 nodos, en este orden y con el mismo resultado:

1. **Google Drive, carpeta "My idea"** (id `1XgX_D6LNYPzwSQtkw2MECKLGWnSkqWg7`), solo lectura. Contiene dos subcarpetas: `mundo_11` (id `1rhlleEcYcuPUFcmhx9xyFx6IgI9OAUnT`: onu_consumidor, openstax_business_ethics, grove_high_output, zhuo_manager, bernerslee_bananas, gerber_emyth, marquet_turn_the_ship, smart_who, openstax_org_behavior, scott_radical_candor, y los ficheros LISTADO_ARCHIVOS_AUDITORIA.md, MANIFIESTO.md, CENSO_DE_CUERPOS.md, INDICE_REAL.md) y `mundo_10_reservado` (id `17iYbAMf6zCpG2YqvxRCor8g3eMK1MbDc`: gerber_emyth). Ninguno de los 23 libros del sorteo. Busquedas por titulo en todo el Drive (Juran, Franchise, Startup Owner, Exporting, Green to Gold, Deming, Dekker, Lean Startup, Venture Deals, Cradle, Crosby, Siebert, Reason, NIST, Waltzing, Hugos, Cooper, Horowitz, Osterwalder, Esty, Braungart, Quality, Handbook, Traction, OSHA, Hubbard, Voss, Lindstrom, Procurement, Value Proposition, Founder, Winning at New, Assembling Tomorrow, Rushton, Logistics, Managing Project Risks, Failure of Risk, Cybersecurity, Out of the Crisis, Quality is free, Managing the Risks) y por texto (Crosby, Wasserman, Siebert, Braungart, "Rompe la barrera del no", SP 800-171): ningun libro del catalogo; solo un capitulo de OpenStax (mundo 11) y documentos personales ajenos al encargo, que no se abrieron.
2. **`C:\Users\AlexDesk\Documents\forja-nodos\fuentes\`**, solo lectura con `ls` y `cat`, sin git. Contiene `FUENTES_CANONICAS.json` y once carpetas: bernerslee_bananas, gerber_emyth, gerber_emyth_cap17_reservado, grove_high_output, marquet_turn_the_ship, onu_consumidor, openstax_business_ethics, openstax_org_behavior, scott_radical_candor, smart_who, zhuo_manager. Ninguno de los 23 libros del sorteo.

Resultado: **los 30 nodos quedan SIN FUENTE**, y ningun capitulo fuente pudo localizarse.

### 6.3 Donde probablemente estan los textos (no leido)

El repo dice donde vivian los textos que se usaron para extraer el catalogo: `scripts/pipeline_libros.py` linea 63, `BOOKS_DIR = BASE / "books"` (carpeta `books/` en la raiz de una copia de trabajo del repo, fuera de git), y `scripts/_run_dominio_full2.log` lista ficheros como `Juran's Quality Handbook_ The C - Joseph A. Defeo.txt` y `The Green to Gold Business Play - Daniel C. Esty.txt`. En este equipo existe el directorio `C:\Users\AlexDesk\Documents\I have an idea\books` (comprobado solo que existe, con `ls -d`; no se listo ni se leyo su contenido, porque esa ruta no esta entre las fuentes autorizadas). Si el fundador la autoriza, la lectura puede hacerse sobre los 30 nodos ya sorteados.

### 6.4 Anexo: tabla completa paso a paso

Numero de nodo segun el sorteo (6.1). Veredicto y cita pendientes de fuente para los 138 pasos.

| # | node_id | mundo | paso | texto del paso (tag) | veredicto | cita del libro |
|---:|---|---|---:|---|---|---|
| 1 | `muestra_puntos_en_comun_antes_de_negociar` | compras | 1 | En la primera conversación, dedica unos minutos a preguntas personales antes de entrar en cifras. | SIN VEREDICTO (sin fuente) | sin cita |
| 1 | `muestra_puntos_en_comun_antes_de_negociar` | compras | 2 | Escucha qué palabras o valores repite la otra parte y usa ese mismo lenguaje al responder. | SIN VEREDICTO (sin fuente) | sin cita |
| 1 | `muestra_puntos_en_comun_antes_de_negociar` | compras | 3 | Menciona con sinceridad algo que tengan en común: forma de trabajar, sector o experiencia previa. | SIN VEREDICTO (sin fuente) | sin cita |
| 1 | `muestra_puntos_en_comun_antes_de_negociar` | compras | 4 | Evita fingir similitud que no existe, porque se nota y rompe la confianza. | SIN VEREDICTO (sin fuente) | sin cita |
| 2 | `domina_lo_que_compras` | compras | 1 | Investiga precios de referencia y variantes del insumo o servicio antes de hablar con el proveedor. | SIN VEREDICTO (sin fuente) | sin cita |
| 2 | `domina_lo_que_compras` | compras | 2 | Pregunta a otras personas de tu rubro que condiciones de compra consideran normales. | SIN VEREDICTO (sin fuente) | sin cita |
| 2 | `domina_lo_que_compras` | compras | 3 | Usa tu propio formato para pedir cotizaciones en vez del que te entrega el proveedor. | SIN VEREDICTO (sin fuente) | sin cita |
| 2 | `domina_lo_que_compras` | compras | 4 | Identifica quienes son los competidores de tu proveedor y que ofrecen. | SIN VEREDICTO (sin fuente) | sin cita |
| 2 | `domina_lo_que_compras` | compras | 5 | Anota las preguntas que aun no puedes responder antes de sentarte a negociar. | SIN VEREDICTO (sin fuente) | sin cita |
| 3 | `extraer_priorizar_hipotesis` | core | 1 | Lista todo lo que tiene que ser cierto sobre tu modelo de negocio, tu propuesta de valor y tu cliente | SIN VEREDICTO (sin fuente) | sin cita |
| 3 | `extraer_priorizar_hipotesis` | core | 2 | Escribe cada hipótesis por separado, una por nota | SIN VEREDICTO (sin fuente) | sin cita |
| 3 | `extraer_priorizar_hipotesis` | core | 3 | Elimina las que estén repetidas | SIN VEREDICTO (sin fuente) | sin cita |
| 3 | `extraer_priorizar_hipotesis` | core | 4 | Identifica cuáles son capaces de acabar con tu proyecto si fallan | SIN VEREDICTO (sin fuente) | sin cita |
| 3 | `extraer_priorizar_hipotesis` | core | 5 | Ordena todas tus hipótesis según qué tan crítica es cada una para que tu proyecto funcione | SIN VEREDICTO (sin fuente) | sin cita |
| 4 | `identificacion_necesidad_sucesion_ceo` | core | 1 | Desde tu primera ronda de inversión, habla abierto sobre las condiciones que podrían llevar a un cambio de liderazgo en el futuro | SIN VEREDICTO (sin fuente) | sin cita |
| 4 | `identificacion_necesidad_sucesion_ceo` | core | 2 | Vigila si los retos de tu negocio, como pasar del arranque inicial a conquistar el mercado masivo, piden nuevas capacidades de liderazgo | SIN VEREDICTO (sin fuente) | sin cita |
| 4 | `identificacion_necesidad_sucesion_ceo` | core | 3 | Sigue el proceso: deja que quien dirige opere, identifica los problemas y trabaja junto a esa persona para resolverlos, y si no hay mejora, decide el reemplazo | SIN VEREDICTO (sin fuente) | sin cita |
| 4 | `identificacion_necesidad_sucesion_ceo` | core | 4 | Comunica de forma clara y repetida qué esperas sobre un posible cambio de liderazgo, porque quienes fundan suelen ignorar o minimizar estas señales | SIN VEREDICTO (sin fuente) | sin cita |
| 5 | `equipo_dedicado_continuo` | core | 1 | Definir un equipo central que permanezca en el proyecto de inicio a fin | SIN VEREDICTO (sin fuente) | sin cita |
| 5 | `equipo_dedicado_continuo` | core | 2 | Incorporar nuevos miembros especializados (manufactura, ventas) según avance el proyecto sin reemplazar al núcleo | SIN VEREDICTO (sin fuente) | sin cita |
| 5 | `equipo_dedicado_continuo` | core | 3 | Buscar perfiles de equipo con expertise específico pero capacidades generalistas | SIN VEREDICTO (sin fuente) | sin cita |
| 5 | `equipo_dedicado_continuo` | core | 4 | Mantener la responsabilidad y ownership del equipo hasta la revisión post-lanzamiento | SIN VEREDICTO (sin fuente) | sin cita |
| 6 | `mejorar_deal_despues_del_hecho` | core | 1 | No des por definitivas las condiciones actuales hasta que llegue la salida (exit) | SIN VEREDICTO (sin fuente) | sin cita |
| 6 | `mejorar_deal_despues_del_hecho` | core | 2 | Cuando busques tu siguiente ronda, cuéntale abiertamente al nuevo inversionista qué condiciones te están pesando | SIN VEREDICTO (sin fuente) | sin cita |
| 6 | `mejorar_deal_despues_del_hecho` | core | 3 | Después de un periodo de buen desempeño, abre una conversación honesta con tus inversionistas actuales | SIN VEREDICTO (sin fuente) | sin cita |
| 6 | `mejorar_deal_despues_del_hecho` | core | 4 | Si llega una adquisición, negocia que parte del dinero de la venta se destine a retener a tu equipo | SIN VEREDICTO (sin fuente) | sin cita |
| 6 | `mejorar_deal_despues_del_hecho` | core | 5 | Mantén siempre transparencia y trato justo con tus inversionistas para no dañar la relación | SIN VEREDICTO (sin fuente) | sin cita |
| 7 | `playing_with_fire_gap` | core | 1 | Evaluar el daño potencial a la relación social si el negocio genera tensión | SIN VEREDICTO (sin fuente) | sin cita |
| 7 | `playing_with_fire_gap` | core | 2 | Evaluar la probabilidad real de que el equipo discuta temas incómodos abiertamente | SIN VEREDICTO (sin fuente) | sin cita |
| 7 | `playing_with_fire_gap` | core | 3 | Calcular la brecha entre ambos factores para cada relación de cofundador | SIN VEREDICTO (sin fuente) | sin cita |
| 7 | `playing_with_fire_gap` | core | 4 | Identificar 'elefantes en la habitación' no discutidos (roles, equity, compromiso, visión) | SIN VEREDICTO (sin fuente) | sin cita |
| 8 | `diseno_etico_de_privacidad` | core | 1 | Enumera qué datos sensibles recolecta tu sistema (ubicación, salud, comportamiento, emociones). | SIN VEREDICTO (sin fuente) | sin cita |
| 8 | `diseno_etico_de_privacidad` | core | 2 | Diseña mecanismos de opt-out reales y accesibles, no ocultos en términos legales. | SIN VEREDICTO (sin fuente) | sin cita |
| 8 | `diseno_etico_de_privacidad` | core | 3 | Evalúa el trade-off: ¿qué conveniencia pierde el usuario al optar por no compartir datos? | SIN VEREDICTO (sin fuente) | sin cita |
| 8 | `diseno_etico_de_privacidad` | core | 4 | Comunica de forma transparente cómo se usan y quién se beneficia de los datos recolectados. | SIN VEREDICTO (sin fuente) | sin cita |
| 9 | `analisis_trafico_competitivo` | core | 1 | Buscar y comparar tráfico de competidores con herramientas como AdRoll o Adbeat | SIN VEREDICTO (sin fuente) | sin cita |
| 9 | `analisis_trafico_competitivo` | core | 2 | Revisar rankings y reseñas en tiendas de apps | SIN VEREDICTO (sin fuente) | sin cita |
| 9 | `analisis_trafico_competitivo` | core | 3 | Visitar foros y sitios de preguntas (como Quora) para obtener información de mercado | SIN VEREDICTO (sin fuente) | sin cita |
| 9 | `analisis_trafico_competitivo` | core | 4 | Organizar hallazgos en una grilla competitiva y mapa de mercado | SIN VEREDICTO (sin fuente) | sin cita |
| 10 | `saber_hasta_donde_mejorar_servicio` | entrega | 1 | Anota tu nivel actual de servicio: por ejemplo, que porcentaje de pedidos llega a tiempo y completo. | SIN VEREDICTO (sin fuente) | sin cita |
| 10 | `saber_hasta_donde_mejorar_servicio` | entrega | 2 | Pregunta a tus clientes si notarian la diferencia si mejoraras ese numero unos puntos mas. | SIN VEREDICTO (sin fuente) | sin cita |
| 10 | `saber_hasta_donde_mejorar_servicio` | entrega | 3 | Calcula cuanto te costaria en tiempo o dinero subir ese numero antes de intentarlo. | SIN VEREDICTO (sin fuente) | sin cita |
| 10 | `saber_hasta_donde_mejorar_servicio` | entrega | 4 | Detente en el punto donde el costo de mejorar supera lo que el cliente valora. | SIN VEREDICTO (sin fuente) | sin cita |
| 10 | `saber_hasta_donde_mejorar_servicio` | entrega | 5 | Revisa esta decision cada varios meses, porque las expectativas del cliente cambian. | SIN VEREDICTO (sin fuente) | sin cita |
| 11 | `aplicar_regla_fija_de_colchon_de_relleno` | entrega | 1 | Mide con una regla la distancia entre el producto y cada pared de la caja antes de cerrarla. | SIN VEREDICTO (sin fuente) | sin cita |
| 11 | `aplicar_regla_fija_de_colchon_de_relleno` | entrega | 2 | Ajusta el tamaño de caja si la distancia es menor a cinco centímetros en algún lado. | SIN VEREDICTO (sin fuente) | sin cita |
| 11 | `aplicar_regla_fija_de_colchon_de_relleno` | entrega | 3 | Rellena cualquier espacio vacío hasta que el producto no se mueva al agitar la caja con cuidado. | SIN VEREDICTO (sin fuente) | sin cita |
| 11 | `aplicar_regla_fija_de_colchon_de_relleno` | entrega | 4 | Anota esta regla en un lugar visible de tu zona de empaque para no improvisar cada vez. | SIN VEREDICTO (sin fuente) | sin cita |
| 12 | `estrategia_proactiva_ambiental` | environmental | 1 | Revisa si tu estrategia ambiental actual es reactiva (solo cumplimiento) o proactiva | SIN VEREDICTO (sin fuente) | sin cita |
| 12 | `estrategia_proactiva_ambiental` | environmental | 2 | Define la sostenibilidad como algo estratégico para tu negocio, no solo como una tarea operativa | SIN VEREDICTO (sin fuente) | sin cita |
| 12 | `estrategia_proactiva_ambiental` | environmental | 3 | Establece objetivos ambientales que anticipen regulaciones futuras y expectativas de tu mercado | SIN VEREDICTO (sin fuente) | sin cita |
| 12 | `estrategia_proactiva_ambiental` | environmental | 4 | Aplica la lente ambiental en todas las áreas de tu negocio, no solo en las operaciones | SIN VEREDICTO (sin fuente) | sin cita |
| 13 | `volverse_nativo_del_lugar` | environmental | 1 | Estudiar prácticas tradicionales o indígenas de manejo de recursos aplicables a la región del proyecto | SIN VEREDICTO (sin fuente) | sin cita |
| 13 | `volverse_nativo_del_lugar` | environmental | 2 | Diseñar sistemas de extracción de recursos que mantengan o incrementen el capital natural a largo plazo | SIN VEREDICTO (sin fuente) | sin cita |
| 13 | `volverse_nativo_del_lugar` | environmental | 3 | Evaluar la posibilidad de integrar industria y comunidad en lugar de separarlas mediante zonificación estricta | SIN VEREDICTO (sin fuente) | sin cita |
| 14 | `cinco_principios_guia_transformacion` | environmental | 1 | Comunicar públicamente el compromiso de la organización con un cambio de paradigma (no solo mejora incremental). | SIN VEREDICTO (sin fuente) | sin cita |
| 14 | `cinco_principios_guia_transformacion` | environmental | 2 | Definir métricas de 'buen crecimiento' que incluyan impacto restaurador social y ambiental, no solo financiero. | SIN VEREDICTO (sin fuente) | sin cita |
| 14 | `cinco_principios_guia_transformacion` | environmental | 3 | Destinar recursos y tiempo a proyectos de innovación paralelos, aceptando una tasa de éxito baja (10-15%). | SIN VEREDICTO (sin fuente) | sin cita |
| 14 | `cinco_principios_guia_transformacion` | environmental | 4 | Establecer criterios de decisión que consideren el impacto en generaciones futuras y otras especies. | SIN VEREDICTO (sin fuente) | sin cita |
| 15 | `tipos_sitio_web_exportacion` | exportacion | 1 | Evaluar si el producto puede venderse completamente en línea (transaccional) o requiere solo información (informacional) | SIN VEREDICTO (sin fuente) | sin cita |
| 15 | `tipos_sitio_web_exportacion` | exportacion | 2 | Investigar e-marketplaces relevantes para el sector y mercado objetivo (Amazon, Alibaba, eBay, etc.) | SIN VEREDICTO (sin fuente) | sin cita |
| 15 | `tipos_sitio_web_exportacion` | exportacion | 3 | Decidir el tipo de sitio web o combinación de modelos más adecuada para la empresa | SIN VEREDICTO (sin fuente) | sin cita |
| 15 | `tipos_sitio_web_exportacion` | exportacion | 4 | Definir presupuesto de diseño y mantenimiento según el tipo de sitio elegido | SIN VEREDICTO (sin fuente) | sin cita |
| 16 | `clausula_escape_contrato_representante` | exportacion | 1 | Definir el plazo de notificación previa para terminar el contrato (ej. 90 días) | SIN VEREDICTO (sin fuente) | sin cita |
| 16 | `clausula_escape_contrato_representante` | exportacion | 2 | Especificar por escrito qué constituye 'causa justa' de terminación | SIN VEREDICTO (sin fuente) | sin cita |
| 16 | `clausula_escape_contrato_representante` | exportacion | 3 | Determinar qué ley o convención internacional regirá disputas contractuales | SIN VEREDICTO (sin fuente) | sin cita |
| 16 | `clausula_escape_contrato_representante` | exportacion | 4 | Establecer qué compensación corresponde al representante en caso de despido | SIN VEREDICTO (sin fuente) | sin cita |
| 16 | `clausula_escape_contrato_representante` | exportacion | 5 | Especificar la devolución de propiedad (patentes, marcas, registros, datos de clientes) | SIN VEREDICTO (sin fuente) | sin cita |
| 16 | `clausula_escape_contrato_representante` | exportacion | 6 | Aclarar si el representante tiene poder de 'agente' con implicaciones legales | SIN VEREDICTO (sin fuente) | sin cita |
| 16 | `clausula_escape_contrato_representante` | exportacion | 7 | Redactar el contrato en inglés y en el idioma oficial del país extranjero | SIN VEREDICTO (sin fuente) | sin cita |
| 16 | `clausula_escape_contrato_representante` | exportacion | 8 | Obtener asesoría legal calificada sobre requisitos del país del representante | SIN VEREDICTO (sin fuente) | sin cita |
| 17 | `brokers_lead_referral_networks` | franquicias | 1 | Evalúa tu presupuesto de marketing y tus metas de crecimiento para decidir si te conviene usar brokers | SIN VEREDICTO (sin fuente) | sin cita |
| 17 | `brokers_lead_referral_networks` | franquicias | 2 | Elige las redes de brokers con el mismo cuidado con el que contratarías a alguien para vender por ti | SIN VEREDICTO (sin fuente) | sin cita |
| 17 | `brokers_lead_referral_networks` | franquicias | 3 | Evita brokers que te pidan un porcentaje de regalías o cualquier pago continuo, más allá de la comisión por cierre | SIN VEREDICTO (sin fuente) | sin cita |
| 17 | `brokers_lead_referral_networks` | franquicias | 4 | Vigila de cerca cómo los brokers hablan de tu marca frente a los prospectos | SIN VEREDICTO (sin fuente) | sin cita |
| 17 | `brokers_lead_referral_networks` | franquicias | 5 | Asiste a convenciones y mantén comunicación constante para que tu marca esté siempre presente en la mente de esa red | SIN VEREDICTO (sin fuente) | sin cita |
| 18 | `folleto_franquicia` | franquicias | 1 | Contratar un consultor o agencia con experiencia específica en marketing de franquicias | SIN VEREDICTO (sin fuente) | sin cita |
| 18 | `folleto_franquicia` | franquicias | 2 | Diseñar en formato a cuatro colores con fotografía profesional de alta calidad | SIN VEREDICTO (sin fuente) | sin cita |
| 18 | `folleto_franquicia` | franquicias | 3 | Revisar el copy con el abogado de franquicias (regulado en ocho estados) | SIN VEREDICTO (sin fuente) | sin cita |
| 18 | `folleto_franquicia` | franquicias | 4 | Decidir entre impresión offset (mayor calidad, mayor costo por tirada grande) o digital (menor tirada) | SIN VEREDICTO (sin fuente) | sin cita |
| 19 | `embudo_ventas_franquicia` | franquicias | 1 | Mapea todas las vías por las que hoy te llegan contactos y cuánto te cuesta cada una | SIN VEREDICTO (sin fuente) | sin cita |
| 19 | `embudo_ventas_franquicia` | franquicias | 2 | Mide la tasa de conversión de cada vía en cada etapa del embudo (contacto, formulario, reunión, venta) | SIN VEREDICTO (sin fuente) | sin cita |
| 19 | `embudo_ventas_franquicia` | franquicias | 3 | Compara el costo por contacto y el costo por venta entre tus distintos canales | SIN VEREDICTO (sin fuente) | sin cita |
| 19 | `embudo_ventas_franquicia` | franquicias | 4 | Mueve tu inversión de marketing hacia los canales que mejor resultado te dan según el tipo de franquiciado que buscas | SIN VEREDICTO (sin fuente) | sin cita |
| 19 | `embudo_ventas_franquicia` | franquicias | 5 | Arma un sistema para seguir todo el embudo de forma continua | SIN VEREDICTO (sin fuente) | sin cita |
| 20 | `autonomia_dependencia_regulatoria` | health_safety | 1 | Identificar los límites estructurales que impiden al regulador conocer completamente las operaciones internas de la organización | SIN VEREDICTO (sin fuente) | sin cita |
| 20 | `autonomia_dependencia_regulatoria` | health_safety | 2 | Reconocer los riesgos de relaciones personales excesivamente cercanas entre inspectores y personal de la empresa regulada | SIN VEREDICTO (sin fuente) | sin cita |
| 20 | `autonomia_dependencia_regulatoria` | health_safety | 3 | Establecer mecanismos de verificación independientes que no dependan únicamente de la información proporcionada por el regulado | SIN VEREDICTO (sin fuente) | sin cita |
| 20 | `autonomia_dependencia_regulatoria` | health_safety | 4 | Evaluar si las sanciones actuales reflejan compromiso/negociación en lugar de cumplimiento real de la normativa | SIN VEREDICTO (sin fuente) | sin cita |
| 21 | `prevalencia_omisiones` | health_safety | 1 | Clasificar los errores de mantenimiento históricos según tipo (omisión, instalación incorrecta, parte equivocada, otro) | SIN VEREDICTO (sin fuente) | sin cita |
| 21 | `prevalencia_omisiones` | health_safety | 2 | Identificar en qué nivel cognitivo (planificación, almacenamiento, ejecución, monitoreo) ocurren las omisiones más frecuentes | SIN VEREDICTO (sin fuente) | sin cita |
| 21 | `prevalencia_omisiones` | health_safety | 3 | Enfocar las intervenciones de mejora en los pasos con mayor tasa de omisión histórica | SIN VEREDICTO (sin fuente) | sin cita |
| 21 | `prevalencia_omisiones` | health_safety | 4 | Establecer métricas de seguimiento de omisiones por tipo de tarea | SIN VEREDICTO (sin fuente) | sin cita |
| 22 | `participacion_trabajadores` | health_safety | 1 | Crea un proceso simple para que te reporten peligros, incidentes y casi accidentes, incluyendo la opción de hacerlo de forma anónima | SIN VEREDICTO (sin fuente) | sin cita |
| 22 | `participacion_trabajadores` | health_safety | 2 | Da retroalimentación frecuente sobre lo que haces con cada reporte que recibes | SIN VEREDICTO (sin fuente) | sin cita |
| 22 | `participacion_trabajadores` | health_safety | 3 | Comparte con tus trabajadores la información de seguridad, como las hojas de datos de seguridad (SDS), los datos de lesiones y las inspecciones | SIN VEREDICTO (sin fuente) | sin cita |
| 22 | `participacion_trabajadores` | health_safety | 4 | Involucra a tus trabajadores en el diseño de metas, análisis de peligros, inspecciones, capacitación y desarrollo de soluciones | SIN VEREDICTO (sin fuente) | sin cita |
| 22 | `participacion_trabajadores` | health_safety | 5 | Elimina barreras de idioma, habilidad, educación o miedo a represalias | SIN VEREDICTO (sin fuente) | sin cita |
| 22 | `participacion_trabajadores` | health_safety | 6 | Comunica con claridad las protecciones contra represalias que existen en tu país y revisa que tus incentivos no desalienten el reporte | SIN VEREDICTO (sin fuente) | sin cita |
| 23 | `accion_correctiva_sistematica` | quality | 1 | Documenta cada problema detectado en una ficha simple: qué pasó, qué tan grave es, por qué pasó, quién se encarga y para cuándo | SIN VEREDICTO (sin fuente) | sin cita |
| 23 | `accion_correctiva_sistematica` | quality | 2 | Revisa a diario los problemas nuevos junto con la persona que te ayuda con calidad o producción, si la tienes | SIN VEREDICTO (sin fuente) | sin cita |
| 23 | `accion_correctiva_sistematica` | quality | 3 | Si un problema no se resuelve en la revisión diaria, pásalo a una revisión semanal más a fondo | SIN VEREDICTO (sin fuente) | sin cita |
| 23 | `accion_correctiva_sistematica` | quality | 4 | Revisa una vez al mes lo que sigue sin resolverse y decide si necesita un esfuerzo dedicado aparte | SIN VEREDICTO (sin fuente) | sin cita |
| 23 | `accion_correctiva_sistematica` | quality | 5 | Para los problemas más complejos, junta puntualmente a las personas involucradas en un grupo de trabajo con un responsable claro, y disuélvelo en cuanto el problema quede resuelto | SIN VEREDICTO (sin fuente) | sin cita |
| 23 | `accion_correctiva_sistematica` | quality | 6 | Ordena los problemas por gravedad y ataca primero los más grandes | SIN VEREDICTO (sin fuente) | sin cita |
| 23 | `accion_correctiva_sistematica` | quality | 7 | Define acciones que corrijan la causa raíz y prevengan la recurrencia, no solo alivien la presión del momento | SIN VEREDICTO (sin fuente) | sin cita |
| 23 | `accion_correctiva_sistematica` | quality | 8 | Escala los problemas más sutiles o de largo plazo a un nivel de decisión superior con frecuencia regular, para que no se acepten como normales | SIN VEREDICTO (sin fuente) | sin cita |
| 23 | `accion_correctiva_sistematica` | quality | 9 | Dar seguimiento y verificar que la acción implementada haya eliminado el problema | SIN VEREDICTO (sin fuente) | sin cita |
| 24 | `decision_conformidad_producto` | quality | 1 | Entrenar a inspectores y operadores en el conocimiento de productos, estándares e instrumentos. | SIN VEREDICTO (sin fuente) | sin cita |
| 24 | `decision_conformidad_producto` | quality | 2 | Delegar la autoridad de juicio de conformidad a inspectores o sistemas automatizados. | SIN VEREDICTO (sin fuente) | sin cita |
| 24 | `decision_conformidad_producto` | quality | 3 | Establecer procedimientos de identificación ('stamp') para productos conformes. | SIN VEREDICTO (sin fuente) | sin cita |
| 24 | `decision_conformidad_producto` | quality | 4 | Definir políticas de gestión sobre el envío de productos conformes. | SIN VEREDICTO (sin fuente) | sin cita |
| 25 | `pruebas_inadecuadas_prototipos` | quality | 1 | Realizar pruebas con muestras que reflejen la variación real esperada en producción, no solo valores nominales | SIN VEREDICTO (sin fuente) | sin cita |
| 25 | `pruebas_inadecuadas_prototipos` | quality | 2 | Aplicar métodos Monte Carlo para simular variaciones de dimensión, presión, temperatura, etc. en diseño asistido por computadora | SIN VEREDICTO (sin fuente) | sin cita |
| 25 | `pruebas_inadecuadas_prototipos` | quality | 3 | Verificar el estado de control estadístico del proceso antes de confiar en resultados de prototipos | SIN VEREDICTO (sin fuente) | sin cita |
| 25 | `pruebas_inadecuadas_prototipos` | quality | 4 | Formular preguntas clave sobre a qué se refieren los resultados de prueba: ¿predicen la corrida de mañana o el resultado de próximo año? | SIN VEREDICTO (sin fuente) | sin cita |
| 26 | `sistema_de_alarma_de_defectos` | quality | 1 | Definir indicadores clave que disparen alarmas de calidad | SIN VEREDICTO (sin fuente) | sin cita |
| 26 | `sistema_de_alarma_de_defectos` | quality | 2 | Establecer un cronograma común entre comprador y proveedor | SIN VEREDICTO (sin fuente) | sin cita |
| 26 | `sistema_de_alarma_de_defectos` | quality | 3 | Asignar responsables de actuar sobre las alarmas | SIN VEREDICTO (sin fuente) | sin cita |
| 26 | `sistema_de_alarma_de_defectos` | quality | 4 | Documentar tiempos de respuesta esperados | SIN VEREDICTO (sin fuente) | sin cita |
| 27 | `plan_de_desastre_y_recuperacion` | risk_management | 1 | Identifica los pocos desastres que te dejarían fuera del juego: pérdida de datos, salud, un local. | SIN VEREDICTO (sin fuente) | sin cita |
| 27 | `plan_de_desastre_y_recuperacion` | risk_management | 2 | Para cada uno, escribe los pasos concretos que te devolverían a operar, en orden. | SIN VEREDICTO (sin fuente) | sin cita |
| 27 | `plan_de_desastre_y_recuperacion` | risk_management | 3 | Prepara de antemano lo que esa recuperación necesita: respaldos, contactos, un fondo. | SIN VEREDICTO (sin fuente) | sin cita |
| 27 | `plan_de_desastre_y_recuperacion` | risk_management | 4 | Guarda el plan donde puedas acceder a él aunque hayas perdido lo demás. | SIN VEREDICTO (sin fuente) | sin cita |
| 28 | `escepticismo_sano_ante_el_riesgo` | risk_management | 1 | De cualquier método de riesgo que uses, pregúntate cómo sabrías si de verdad te está ayudando. | SIN VEREDICTO (sin fuente) | sin cita |
| 28 | `escepticismo_sano_ante_el_riesgo` | risk_management | 2 | Desconfía de la calma: que te sientas seguro no es prueba de que estás seguro. | SIN VEREDICTO (sin fuente) | sin cita |
| 28 | `escepticismo_sano_ante_el_riesgo` | risk_management | 3 | Antes de adoptar una plantilla ajena, busca evidencia de que a alguien le funcionó de verdad. | SIN VEREDICTO (sin fuente) | sin cita |
| 28 | `escepticismo_sano_ante_el_riesgo` | risk_management | 4 | Prefiere una nota simple y honesta a un tablero vistoso que no puedas comprobar. | SIN VEREDICTO (sin fuente) | sin cita |
| 29 | `getting_started_system_information_integrity` | seguridad_digital | 1 | Suscribirse a fuentes de alertas de seguridad (CISA, NSA, FBI, ISACs, proveedores). | SIN VEREDICTO (sin fuente) | sin cita |
| 29 | `getting_started_system_information_integrity` | seguridad_digital | 2 | Establecer una estrategia de monitoreo del sistema con procedimientos y herramientas definidas. | SIN VEREDICTO (sin fuente) | sin cita |
| 29 | `getting_started_system_information_integrity` | seguridad_digital | 3 | Detectar ataques, conexiones no autorizadas y actividades inusuales en tráfico entrante/saliente. | SIN VEREDICTO (sin fuente) | sin cita |
| 29 | `getting_started_system_information_integrity` | seguridad_digital | 4 | Establecer políticas de gestión y retención de CUI conforme a leyes y regulaciones. | SIN VEREDICTO (sin fuente) | sin cita |
| 29 | `getting_started_system_information_integrity` | seguridad_digital | 5 | Eliminar CUI de sistemas no federales una vez concluidos los contratos para reducir la superficie de ataque. | SIN VEREDICTO (sin fuente) | sin cita |
| 30 | `funcion_respond_plan_incidentes` | seguridad_digital | 1 | Definir protocolo de notificación a clientes, empleados y terceros afectados | SIN VEREDICTO (sin fuente) | sin cita |
| 30 | `funcion_respond_plan_incidentes` | seguridad_digital | 2 | Establecer procedimientos para mantener operaciones durante un incidente | SIN VEREDICTO (sin fuente) | sin cita |
| 30 | `funcion_respond_plan_incidentes` | seguridad_digital | 3 | Crear proceso de reporte a autoridades y fuerzas del orden | SIN VEREDICTO (sin fuente) | sin cita |
| 30 | `funcion_respond_plan_incidentes` | seguridad_digital | 4 | Documentar pasos de investigación y contención de ataques | SIN VEREDICTO (sin fuente) | sin cita |
| 30 | `funcion_respond_plan_incidentes` | seguridad_digital | 5 | Probar el plan de respuesta regularmente mediante simulacros | SIN VEREDICTO (sin fuente) | sin cita |
