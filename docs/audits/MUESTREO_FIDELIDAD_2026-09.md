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

Pendiente: se escriben despues del sorteo, en un segundo commit.
