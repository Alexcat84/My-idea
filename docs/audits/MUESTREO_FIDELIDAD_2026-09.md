NECESITO AL FUNDADOR: 10 de los 23 libros de la muestra pasan el umbral del encargo. Nueve lo pasan por INFERIDOS por encima del 10 por ciento: Assembling Tomorrow (4 de 4), Voss, Rompe la barrera del no (2 de 4), Braungart, Cradle to Cradle (2 de 7), Juran's Quality Handbook (2 de 8), Blank, The Startup Owner's Manual (1 de 4), Edwards et al., Managing Project Risks (1 de 4), Hubbard, The Failure of Risk Management (1 de 4), Requisitos de empaque de los couriers (1 de 4) y Wasserman, The Founder's Dilemmas (1 de 8). El decimo, Reason, Managing the Risks of Organizational Accidents, tiene 4 INFERIDOS de 8 y el unico CONTRARIO de la muestra (nodo `prevalencia_omisiones`, paso 2).

# MUESTREO DE FIDELIDAD, septiembre 2026: REPORTE

**Tasa global de INFERIDOS: 21 de 138 pasos, 15,2 por ciento (Wilson 95: 10,2 a 22,1).** Tasa global de CONTRARIOS: 1 de 138 pasos, 0,7 por ciento (Wilson 95: 0,1 a 4,0). FIELES: 116 de 138 (84,1 por ciento). Por nodo: 14 de los 30 nodos tienen al menos un paso INFERIDO (46,7 por ciento, Wilson 95: 30,2 a 63,9) y 1 de 30 tiene un CONTRARIO (3,3 por ciento, Wilson 95: 0,6 a 16,7). La tasa de INFERIDOS ponderada por los vivos de cada mundo (estimacion puntual) es 16,7 por ciento.

**Como leer el umbral.** Casi todos los libros de la muestra aportan 4 a 8 pasos. Con 4 pasos, un solo INFERIDO ya es un 25 por ciento, y el intervalo de ese libro va de 4,6 a 69,9. Ocho de los diez libros senalados pasan el umbral por uno o dos pasos. La senal fuerte esta en tres sitios: Assembling Tomorrow (el nodo `diseno_etico_de_privacidad` convierte en instrucciones un texto que solo describe), Reason (4 INFERIDOS y el CONTRARIO en dos nodos) y el CONTRARIO en si. Lo demas es ruido de muestras pequenas hasta que se lea mas.

**Hashes.**
- Pre-registro (semilla, metodo y criterios, sin resultados, antes de sortear): `c038586dc3e64e2b998c78b64a517b55905785c5` (2026-09-23 22:48:45 -0400).
- Primer resultado, sin fuente accesible: `835e92d6331ae62cd3c398e459bfa6741d24071d`. Esta version lo sustituye.
- Esta version (lectura con las rutas del fundador) es el commit que anade este bloque. Un fichero no puede citar el hash del commit que lo contiene: el hash va en el mensaje de cierre de la sesion.
- Las secciones 0 a 5 del pre-registro no cambian (`git diff c038586d -- docs/audits/MUESTREO_FIDELIDAD_2026-09.md`). La seccion 2 sigue tal cual. La seccion 7, nueva, recoge las rutas que el fundador indico despues de la semilla.
- La muestra no cambio: son los mismos 30 nodos y 138 pasos del sorteo de la seccion 6.1, y no se volvio a sortear.

## R1. Tablas por mundo y por libro

Por mundo (Wilson al 95 por ciento, por paso y por nodo):

| mundo | nodos | pasos | INFERIDO por paso | CONTRARIO por paso | nodos con algun INFERIDO | nodos con algun CONTRARIO |
|---|---:|---:|---|---|---|---|
| compras | 2 | 9 | 2/9 = 22,2% [6,3, 54,7] | 0/9 = 0% [0, 29,9] | 1/2 [9,5, 90,5] | 0/2 [0, 65,8] |
| core | 7 | 30 | 6/30 = 20,0% [9,5, 37,3] | 0/30 = 0% [0, 11,4] | 3/7 [15,8, 75,0] | 0/7 [0, 35,4] |
| entrega | 2 | 9 | 1/9 = 11,1% [2,0, 43,5] | 0/9 = 0% [0, 29,9] | 1/2 [9,5, 90,5] | 0/2 [0, 65,8] |
| environmental | 3 | 11 | 2/11 = 18,2% [5,1, 47,7] | 0/11 = 0% [0, 25,9] | 2/3 [20,8, 93,9] | 0/3 [0, 56,1] |
| exportacion | 2 | 12 | 1/12 = 8,3% [1,5, 35,4] | 0/12 = 0% [0, 24,2] | 1/2 [9,5, 90,5] | 0/2 [0, 65,8] |
| franquicias | 3 | 14 | 1/14 = 7,1% [1,3, 31,5] | 0/14 = 0% [0, 21,5] | 1/3 [6,1, 79,2] | 0/3 [0, 56,1] |
| health_safety | 3 | 14 | 4/14 = 28,6% [11,7, 54,6] | 1/14 = 7,1% [1,3, 31,5] | 2/3 [20,8, 93,9] | 1/3 [6,1, 79,2] |
| quality | 4 | 21 | 2/21 = 9,5% [2,7, 28,9] | 0/21 = 0% [0, 15,5] | 1/4 [4,6, 69,9] | 0/4 [0, 49,0] |
| risk_management | 2 | 8 | 2/8 = 25,0% [7,1, 59,1] | 0/8 = 0% [0, 32,4] | 2/2 [34,2, 100] | 0/2 [0, 65,8] |
| seguridad_digital | 2 | 10 | 0/10 = 0% [0, 27,8] | 0/10 = 0% [0, 27,8] | 0/2 [0, 65,8] | 0/2 [0, 65,8] |
| **total** | **30** | **138** | **21/138 = 15,2% [10,2, 22,1]** | **1/138 = 0,7% [0,1, 4,0]** | **14/30 [30,2, 63,9]** | **1/30 [0,6, 16,7]** |

Todos los mundos tienen fuente y al menos dos nodos leidos: se cumple el minimo de dos por mundo en los diez.

Por libro (primer libro del campo `fuente`; ninguno de los 30 nodos tiene fuente multiple). La marca "UMBRAL" senala los libros con mas del 10 por ciento de INFERIDOS o con algun CONTRARIO:

| libro | mundo | nodos | pasos | INFERIDO por paso | CONTRARIO por paso | umbral |
|---|---|---:|---:|---|---|---|
| Assembling Tomorrow (Doorley et al.) | core | 1 | 4 | 4/4 = 100% [51,0, 100] | 0/4 [0, 49,0] | UMBRAL |
| Reason, Managing the Risks of Organizational Accidents | health_safety | 2 | 8 | 4/8 = 50,0% [21,5, 78,5] | 1/8 = 12,5% [2,2, 47,1] | UMBRAL (y CONTRARIO) |
| Voss, Rompe la barrera del no | compras | 1 | 4 | 2/4 = 50,0% [15,0, 85,0] | 0/4 [0, 49,0] | UMBRAL |
| Braungart, Cradle to Cradle | environmental | 2 | 7 | 2/7 = 28,6% [8,2, 64,1] | 0/7 [0, 35,4] | UMBRAL |
| Juran's Quality Handbook | quality | 2 | 8 | 2/8 = 25,0% [7,1, 59,1] | 0/8 [0, 32,4] | UMBRAL |
| Blank, The Startup Owner's Manual | core | 1 | 4 | 1/4 = 25,0% [4,6, 69,9] | 0/4 [0, 49,0] | UMBRAL |
| Edwards et al., Managing Project Risks | risk_management | 1 | 4 | 1/4 = 25,0% [4,6, 69,9] | 0/4 [0, 49,0] | UMBRAL |
| Hubbard, The Failure of Risk Management | risk_management | 1 | 4 | 1/4 = 25,0% [4,6, 69,9] | 0/4 [0, 49,0] | UMBRAL |
| Requisitos de empaque de los couriers | entrega | 1 | 4 | 1/4 = 25,0% [4,6, 69,9] | 0/4 [0, 49,0] | UMBRAL |
| Wasserman, The Founder's Dilemmas | core | 2 | 8 | 1/8 = 12,5% [2,2, 47,1] | 0/8 [0, 32,4] | UMBRAL |
| A Basic Guide to Exporting | exportacion | 2 | 12 | 1/12 = 8,3% [1,5, 35,4] | 0/12 [0, 24,2] | |
| Siebert, Franchise Your Business | franquicias | 3 | 14 | 1/14 = 7,1% [1,3, 31,5] | 0/14 [0, 21,5] | |
| Crosby, Quality is Free | quality | 1 | 9 | 0/9 [0, 29,9] | 0/9 [0, 29,9] | |
| OSHA 3885 | health_safety | 1 | 6 | 0/6 [0, 39,0] | 0/6 [0, 39,0] | |
| Lindstrom, Procurement Project Management Success | compras | 1 | 5 | 0/5 [0, 43,4] | 0/5 [0, 43,4] | |
| Value Proposition Design | core | 1 | 5 | 0/5 [0, 43,4] | 0/5 [0, 43,4] | |
| Feld, Venture Deals | core | 1 | 5 | 0/5 [0, 43,4] | 0/5 [0, 43,4] | |
| Rushton et al., Handbook of Logistics and Distribution Management | entrega | 1 | 5 | 0/5 [0, 43,4] | 0/5 [0, 43,4] | |
| NIST SP 1318 | seguridad_digital | 1 | 5 | 0/5 [0, 43,4] | 0/5 [0, 43,4] | |
| FTC, Cybersecurity for Small Business (NIST CSF) | seguridad_digital | 1 | 5 | 0/5 [0, 43,4] | 0/5 [0, 43,4] | |
| Cooper, Winning at New Products | core | 1 | 4 | 0/4 [0, 49,0] | 0/4 [0, 49,0] | |
| Esty, The Green to Gold Business Playbook | environmental | 1 | 4 | 0/4 [0, 49,0] | 0/4 [0, 49,0] | |
| Deming, Out of the Crisis | quality | 1 | 4 | 0/4 [0, 49,0] | 0/4 [0, 49,0] | |

## R2. Nodos con algun CONTRARIO

| nodo | paso | texto del paso (tag) | cita del libro que lo contradice |
|---|---:|---|---|
| `prevalencia_omisiones` (health_safety; Reason, Managing the Risks of Organizational Accidents, cap. 5, "Maintenance can Seriously Damage your System") | 2 | Identificar en qué nivel cognitivo (planificación, almacenamiento, ejecución, monitoreo) ocurren las omisiones más frecuentes | L2170: "The former route [identificar los mecanismos cognitivos] is made difficult by the fact that an omission can arise within a number of cognitive processes concerned with planning and executing an action, as summarized in Table 5.3. Even when the omission is one's own, the underlying mechanisms are not easy to establish, but when the omission is made by another person at some time in the past, the underlying reasons may be impossible to discover. The task analysis route, on the other hand, is more promising." Y L1943: "Such a causal taxonomy is helpful in locating the underlying mental processes, but it is difficult for non-specialists to apply." El libro desaconseja la via cognitiva para omisiones pasadas y para no especialistas, y recomienda la de los rasgos de la tarea (L2250). Se busco en todo el libro apoyo a clasificar omisiones historicas por nivel cognitivo: no lo hay. |

Casos cercanos que NO se marcaron CONTRARIO (tension sin contradiccion directa, quedan INFERIDO): `autonomia_dependencia_regulatoria` paso 4, frente a la cita de Vaughan en L4265 ("To interpret the consequences of this negotiation and bargaining... as regulatory 'failures' is to miss the point"); `escepticismo_sano_ante_el_riesgo` paso 4, frente a la preferencia del libro por modelos cuantitativos simples (L946); `muestra_puntos_en_comun_antes_de_negociar` paso 4, frente al reflejo como "arte de insinuar que existe una similitud" (L688).

## R3. Script de tasas y su salida

Python 3.12.8. Las cadenas de veredictos (F, I, C por paso, en orden) salen del anexo 6.4.

```python
# Tasas de INFERIDO y CONTRARIO con Wilson 95, por paso y por nodo, global, por mundo y por libro.
# Una fila por nodo del sorteo de c038586: (n, node_id, mundo, libro, veredictos paso a paso)
# F = FIEL, I = INFERIDO, C = CONTRARIO. Sale del anexo 6.4 de este fichero.
import math
from collections import defaultdict
Z = 1.959964
NODOS = [
(1, 'muestra_puntos_en_comun_antes_de_negociar', 'compras', 'Voss, Rompe la barrera del no', 'IFFI'),
(2, 'domina_lo_que_compras', 'compras', 'Lindstrom, Procurement Project Management Success', 'FFFFF'),
(3, 'extraer_priorizar_hipotesis', 'core', 'Value Proposition Design', 'FFFFF'),
(4, 'identificacion_necesidad_sucesion_ceo', 'core', "Wasserman, The Founder's Dilemmas", 'FFFF'),
(5, 'equipo_dedicado_continuo', 'core', 'Cooper, Winning at New Products', 'FFFF'),
(6, 'mejorar_deal_despues_del_hecho', 'core', 'Feld, Venture Deals', 'FFFFF'),
(7, 'playing_with_fire_gap', 'core', "Wasserman, The Founder's Dilemmas", 'FFIF'),
(8, 'diseno_etico_de_privacidad', 'core', 'Assembling Tomorrow', 'IIII'),
(9, 'analisis_trafico_competitivo', 'core', "Blank, The Startup Owner's Manual", 'IFFF'),
(10, 'saber_hasta_donde_mejorar_servicio', 'entrega', 'Rushton et al., Handbook of Logistics and Distribution Management', 'FFFFF'),
(11, 'aplicar_regla_fija_de_colchon_de_relleno', 'entrega', 'Requisitos de empaque de los couriers', 'FFFI'),
(12, 'estrategia_proactiva_ambiental', 'environmental', 'Esty, The Green to Gold Business Playbook', 'FFFF'),
(13, 'volverse_nativo_del_lugar', 'environmental', 'Braungart, Cradle to Cradle', 'IFF'),
(14, 'cinco_principios_guia_transformacion', 'environmental', 'Braungart, Cradle to Cradle', 'FIFF'),
(15, 'tipos_sitio_web_exportacion', 'exportacion', 'A Basic Guide to Exporting', 'FFFI'),
(16, 'clausula_escape_contrato_representante', 'exportacion', 'A Basic Guide to Exporting', 'FFFFFFFF'),
(17, 'brokers_lead_referral_networks', 'franquicias', 'Siebert, Franchise Your Business', 'FFFFF'),
(18, 'folleto_franquicia', 'franquicias', 'Siebert, Franchise Your Business', 'FFIF'),
(19, 'embudo_ventas_franquicia', 'franquicias', 'Siebert, Franchise Your Business', 'FFFFF'),
(20, 'autonomia_dependencia_regulatoria', 'health_safety', 'Reason, Managing the Risks of Organizational Accidents', 'FFII'),
(21, 'prevalencia_omisiones', 'health_safety', 'Reason, Managing the Risks of Organizational Accidents', 'FCII'),
(22, 'participacion_trabajadores', 'health_safety', 'OSHA 3885', 'FFFFFF'),
(23, 'accion_correctiva_sistematica', 'quality', 'Crosby, Quality is Free', 'FFFFFFFFF'),
(24, 'decision_conformidad_producto', 'quality', "Juran's Quality Handbook", 'FFFF'),
(25, 'pruebas_inadecuadas_prototipos', 'quality', 'Deming, Out of the Crisis', 'FFFF'),
(26, 'sistema_de_alarma_de_defectos', 'quality', "Juran's Quality Handbook", 'FIFI'),
(27, 'plan_de_desastre_y_recuperacion', 'risk_management', 'Edwards et al., Managing Project Risks', 'FFFI'),
(28, 'escepticismo_sano_ante_el_riesgo', 'risk_management', 'Hubbard, The Failure of Risk Management', 'FFFI'),
(29, 'getting_started_system_information_integrity', 'seguridad_digital', 'NIST SP 1318', 'FFFFF'),
(30, 'funcion_respond_plan_incidentes', 'seguridad_digital', 'FTC, Cybersecurity for Small Business (NIST CSF)', 'FFFFF'),
]
VIVOS = {'compras': 46, 'core': 1439, 'entrega': 47, 'environmental': 265, 'exportacion': 131,
         'franquicias': 182, 'health_safety': 260, 'quality': 692, 'risk_management': 55, 'seguridad_digital': 52}
def wilson(k, n):
    if n == 0:
        return None
    p = k / n
    d = 1 + Z * Z / n
    c = (p + Z * Z / (2 * n)) / d
    h = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))
def pct(k, n):
    ic = wilson(k, n)
    return f"{k}/{n} = {100*k/n:.1f}% [{100*ic[0]:.1f}, {100*ic[1]:.1f}]"
def bloque(nombre, filas):
    pasos = "".join(f[4] for f in filas)
    n = len(pasos)
    ki, kc = pasos.count("I"), pasos.count("C")
    ni = sum(1 for f in filas if "I" in f[4]); nc = sum(1 for f in filas if "C" in f[4])
    print(f"{nombre} | pasos {n} | INF {pct(ki, n)} | CON {pct(kc, n)} | nodos {len(filas)} | nodos con INF {pct(ni, len(filas))} | nodos con CON {pct(nc, len(filas))}")
    return ki, n
print("== GLOBAL")
bloque("global", NODOS)
tasas = {}
print("== POR MUNDO")
for m in sorted({f[2] for f in NODOS}):
    tasas[m] = bloque(m, [f for f in NODOS if f[2] == m])
w = sum(VIVOS[m] * k / n for m, (k, n) in tasas.items()) / sum(VIVOS.values())
print(f"global INF ponderada por vivos de cada mundo (estimacion puntual, sin intervalo): {100*w:.1f}%")
print("== POR LIBRO")
for b in sorted({f[3] for f in NODOS}):
    bloque(b, [f for f in NODOS if f[3] == b])
print("== UMBRAL DEL ENCARGO (INF > 10% o algun CON)")
for b in sorted({f[3] for f in NODOS}):
    p = "".join(f[4] for f in NODOS if f[3] == b)
    if p.count("I") / len(p) > 0.10 or "C" in p:
        print(f"{b}: INF {p.count('I')}/{len(p)}, CON {p.count('C')}")
print("control wilson(2,10)", tuple(round(x, 4) for x in wilson(2, 10)))
```

Salida literal:

```
== GLOBAL
global | pasos 138 | INF 21/138 = 15.2% [10.2, 22.1] | CON 1/138 = 0.7% [0.1, 4.0] | nodos 30 | nodos con INF 14/30 = 46.7% [30.2, 63.9] | nodos con CON 1/30 = 3.3% [0.6, 16.7]
== POR MUNDO
compras | pasos 9 | INF 2/9 = 22.2% [6.3, 54.7] | CON 0/9 = 0.0% [0.0, 29.9] | nodos 2 | nodos con INF 1/2 = 50.0% [9.5, 90.5] | nodos con CON 0/2 = 0.0% [0.0, 65.8]
core | pasos 30 | INF 6/30 = 20.0% [9.5, 37.3] | CON 0/30 = 0.0% [0.0, 11.4] | nodos 7 | nodos con INF 3/7 = 42.9% [15.8, 75.0] | nodos con CON 0/7 = 0.0% [0.0, 35.4]
entrega | pasos 9 | INF 1/9 = 11.1% [2.0, 43.5] | CON 0/9 = 0.0% [0.0, 29.9] | nodos 2 | nodos con INF 1/2 = 50.0% [9.5, 90.5] | nodos con CON 0/2 = 0.0% [0.0, 65.8]
environmental | pasos 11 | INF 2/11 = 18.2% [5.1, 47.7] | CON 0/11 = 0.0% [0.0, 25.9] | nodos 3 | nodos con INF 2/3 = 66.7% [20.8, 93.9] | nodos con CON 0/3 = 0.0% [0.0, 56.1]
exportacion | pasos 12 | INF 1/12 = 8.3% [1.5, 35.4] | CON 0/12 = 0.0% [0.0, 24.2] | nodos 2 | nodos con INF 1/2 = 50.0% [9.5, 90.5] | nodos con CON 0/2 = 0.0% [0.0, 65.8]
franquicias | pasos 14 | INF 1/14 = 7.1% [1.3, 31.5] | CON 0/14 = 0.0% [0.0, 21.5] | nodos 3 | nodos con INF 1/3 = 33.3% [6.1, 79.2] | nodos con CON 0/3 = 0.0% [0.0, 56.1]
health_safety | pasos 14 | INF 4/14 = 28.6% [11.7, 54.6] | CON 1/14 = 7.1% [1.3, 31.5] | nodos 3 | nodos con INF 2/3 = 66.7% [20.8, 93.9] | nodos con CON 1/3 = 33.3% [6.1, 79.2]
quality | pasos 21 | INF 2/21 = 9.5% [2.7, 28.9] | CON 0/21 = 0.0% [0.0, 15.5] | nodos 4 | nodos con INF 1/4 = 25.0% [4.6, 69.9] | nodos con CON 0/4 = 0.0% [0.0, 49.0]
risk_management | pasos 8 | INF 2/8 = 25.0% [7.1, 59.1] | CON 0/8 = 0.0% [0.0, 32.4] | nodos 2 | nodos con INF 2/2 = 100.0% [34.2, 100.0] | nodos con CON 0/2 = 0.0% [0.0, 65.8]
seguridad_digital | pasos 10 | INF 0/10 = 0.0% [0.0, 27.8] | CON 0/10 = 0.0% [0.0, 27.8] | nodos 2 | nodos con INF 0/2 = 0.0% [0.0, 65.8] | nodos con CON 0/2 = 0.0% [0.0, 65.8]
global INF ponderada por vivos de cada mundo (estimacion puntual, sin intervalo): 16.7%
== POR LIBRO
A Basic Guide to Exporting | pasos 12 | INF 1/12 = 8.3% [1.5, 35.4] | CON 0/12 = 0.0% [0.0, 24.2] | nodos 2 | nodos con INF 1/2 = 50.0% [9.5, 90.5] | nodos con CON 0/2 = 0.0% [0.0, 65.8]
Assembling Tomorrow | pasos 4 | INF 4/4 = 100.0% [51.0, 100.0] | CON 0/4 = 0.0% [0.0, 49.0] | nodos 1 | nodos con INF 1/1 = 100.0% [20.7, 100.0] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Blank, The Startup Owner's Manual | pasos 4 | INF 1/4 = 25.0% [4.6, 69.9] | CON 0/4 = 0.0% [0.0, 49.0] | nodos 1 | nodos con INF 1/1 = 100.0% [20.7, 100.0] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Braungart, Cradle to Cradle | pasos 7 | INF 2/7 = 28.6% [8.2, 64.1] | CON 0/7 = 0.0% [0.0, 35.4] | nodos 2 | nodos con INF 2/2 = 100.0% [34.2, 100.0] | nodos con CON 0/2 = 0.0% [0.0, 65.8]
Cooper, Winning at New Products | pasos 4 | INF 0/4 = 0.0% [0.0, 49.0] | CON 0/4 = 0.0% [0.0, 49.0] | nodos 1 | nodos con INF 0/1 = 0.0% [0.0, 79.3] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Crosby, Quality is Free | pasos 9 | INF 0/9 = 0.0% [0.0, 29.9] | CON 0/9 = 0.0% [0.0, 29.9] | nodos 1 | nodos con INF 0/1 = 0.0% [0.0, 79.3] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Deming, Out of the Crisis | pasos 4 | INF 0/4 = 0.0% [0.0, 49.0] | CON 0/4 = 0.0% [0.0, 49.0] | nodos 1 | nodos con INF 0/1 = 0.0% [0.0, 79.3] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Edwards et al., Managing Project Risks | pasos 4 | INF 1/4 = 25.0% [4.6, 69.9] | CON 0/4 = 0.0% [0.0, 49.0] | nodos 1 | nodos con INF 1/1 = 100.0% [20.7, 100.0] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Esty, The Green to Gold Business Playbook | pasos 4 | INF 0/4 = 0.0% [0.0, 49.0] | CON 0/4 = 0.0% [0.0, 49.0] | nodos 1 | nodos con INF 0/1 = 0.0% [0.0, 79.3] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
FTC, Cybersecurity for Small Business (NIST CSF) | pasos 5 | INF 0/5 = 0.0% [0.0, 43.4] | CON 0/5 = 0.0% [0.0, 43.4] | nodos 1 | nodos con INF 0/1 = 0.0% [0.0, 79.3] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Feld, Venture Deals | pasos 5 | INF 0/5 = 0.0% [0.0, 43.4] | CON 0/5 = 0.0% [0.0, 43.4] | nodos 1 | nodos con INF 0/1 = 0.0% [0.0, 79.3] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Hubbard, The Failure of Risk Management | pasos 4 | INF 1/4 = 25.0% [4.6, 69.9] | CON 0/4 = 0.0% [0.0, 49.0] | nodos 1 | nodos con INF 1/1 = 100.0% [20.7, 100.0] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Juran's Quality Handbook | pasos 8 | INF 2/8 = 25.0% [7.1, 59.1] | CON 0/8 = 0.0% [0.0, 32.4] | nodos 2 | nodos con INF 1/2 = 50.0% [9.5, 90.5] | nodos con CON 0/2 = 0.0% [0.0, 65.8]
Lindstrom, Procurement Project Management Success | pasos 5 | INF 0/5 = 0.0% [0.0, 43.4] | CON 0/5 = 0.0% [0.0, 43.4] | nodos 1 | nodos con INF 0/1 = 0.0% [0.0, 79.3] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
NIST SP 1318 | pasos 5 | INF 0/5 = 0.0% [0.0, 43.4] | CON 0/5 = 0.0% [0.0, 43.4] | nodos 1 | nodos con INF 0/1 = 0.0% [0.0, 79.3] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
OSHA 3885 | pasos 6 | INF 0/6 = 0.0% [0.0, 39.0] | CON 0/6 = 0.0% [0.0, 39.0] | nodos 1 | nodos con INF 0/1 = 0.0% [0.0, 79.3] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Reason, Managing the Risks of Organizational Accidents | pasos 8 | INF 4/8 = 50.0% [21.5, 78.5] | CON 1/8 = 12.5% [2.2, 47.1] | nodos 2 | nodos con INF 2/2 = 100.0% [34.2, 100.0] | nodos con CON 1/2 = 50.0% [9.5, 90.5]
Requisitos de empaque de los couriers | pasos 4 | INF 1/4 = 25.0% [4.6, 69.9] | CON 0/4 = 0.0% [0.0, 49.0] | nodos 1 | nodos con INF 1/1 = 100.0% [20.7, 100.0] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Rushton et al., Handbook of Logistics and Distribution Management | pasos 5 | INF 0/5 = 0.0% [0.0, 43.4] | CON 0/5 = 0.0% [0.0, 43.4] | nodos 1 | nodos con INF 0/1 = 0.0% [0.0, 79.3] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Siebert, Franchise Your Business | pasos 14 | INF 1/14 = 7.1% [1.3, 31.5] | CON 0/14 = 0.0% [0.0, 21.5] | nodos 3 | nodos con INF 1/3 = 33.3% [6.1, 79.2] | nodos con CON 0/3 = 0.0% [0.0, 56.1]
Value Proposition Design | pasos 5 | INF 0/5 = 0.0% [0.0, 43.4] | CON 0/5 = 0.0% [0.0, 43.4] | nodos 1 | nodos con INF 0/1 = 0.0% [0.0, 79.3] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Voss, Rompe la barrera del no | pasos 4 | INF 2/4 = 50.0% [15.0, 85.0] | CON 0/4 = 0.0% [0.0, 49.0] | nodos 1 | nodos con INF 1/1 = 100.0% [20.7, 100.0] | nodos con CON 0/1 = 0.0% [0.0, 79.3]
Wasserman, The Founder's Dilemmas | pasos 8 | INF 1/8 = 12.5% [2.2, 47.1] | CON 0/8 = 0.0% [0.0, 32.4] | nodos 2 | nodos con INF 1/2 = 50.0% [9.5, 90.5] | nodos con CON 0/2 = 0.0% [0.0, 65.8]
== UMBRAL DEL ENCARGO (INF > 10% o algun CON)
Assembling Tomorrow: INF 4/4, CON 0
Blank, The Startup Owner's Manual: INF 1/4, CON 0
Braungart, Cradle to Cradle: INF 2/7, CON 0
Edwards et al., Managing Project Risks: INF 1/4, CON 0
Hubbard, The Failure of Risk Management: INF 1/4, CON 0
Juran's Quality Handbook: INF 2/8, CON 0
Reason, Managing the Risks of Organizational Accidents: INF 4/8, CON 1
Requisitos de empaque de los couriers: INF 1/4, CON 0
Voss, Rompe la barrera del no: INF 2/4, CON 0
Wasserman, The Founder's Dilemmas: INF 1/8, CON 0
control wilson(2,10) (0.0567, 0.5098)
```

Control de la formula, calculado a mano: 2 de 10, z al cuadrado = 3,8415; centro = (0,2 + 0,1921) / 1,3841 = 0,2833; semiancho = 1,96 x raiz(0,0160 + 0,0096) / 1,3841 = 0,2266; intervalo [0,0567, 0,5098], igual que la salida.

## R4. Limitaciones

1. **Intervalo por paso y conglomerado.** Los pasos de un mismo nodo no son independientes: salen del mismo extractor, del mismo pasaje y del mismo lector. El intervalo por paso (10,2 a 22,1) es demasiado estrecho. El intervalo por nodo (14 de 30 nodos con algun INFERIDO, 30,2 a 63,9) es la lectura prudente. Por libro, con 4 a 8 pasos, los intervalos van casi de 0 a 50 o mas: el umbral del 10 por ciento no se puede afirmar ni descartar libro a libro con esta muestra.
2. **Un solo lector, criterio estricto.** Todos los veredictos son de una sola sesion, sin segundo juez ciego. Se aplico la regla de duda del pre-registro: si la accion concreta no esta en el texto, INFERIDO. Hubo casos limite, y se decidieron asi:
   - **FIEL:** un medio de verificacion obvio de un criterio que el libro si da (`aplicar_regla_fija_de_colchon_de_relleno`, pasos 1 y 3: medir con regla y agitar la caja; `funcion_respond_plan_incidentes`, paso 5: "mediante simulacros").
   - **INFERIDO:** un medio nuevo que cambia la accion (`muestra_puntos_en_comun_antes_de_negociar`, paso 1: "preguntas personales").
   - Otro lector podria mover 3 o 4 pasos en cualquiera de los dos sentidos.
3. **Muestra no proporcional.** Hay un piso de 2 nodos por mundo. La global de la muestra (15,2) no es un estimador ponderado del catalogo; la ponderada por vivos es 16,7, como estimacion puntual y sin intervalo.
4. **Fuente de `aplicar_regla_fija_de_colchon_de_relleno`.** No es el texto original: es `EXTRACCION_EMPAQUE_COURIERS.md`, una extraccion ya hecha de las paginas de UPS, FedEx y DHL. Se complemento con `HowToPack_fxcom.txt` (FedEx). La fidelidad medida en ese nodo es a la extraccion, no a los originales de UPS y DHL.
5. **Numeros de linea.** Son del fichero .txt o .md de cada libro, no de la pagina impresa. Algunas conversiones cortan palabras ("commod ity", "presen tation", "con tract"), y las citas las reproducen tal cual.
6. **Rayas del original.** Por la regla de estilo de la casa, la raya (U+2014) y el guion medio (U+2013) de los textos citados se transcriben como dos guiones (`--`) y como guion (`-`). Es el unico cambio sobre la letra de las citas.
7. **Solo se juzgan los pasos.** El titulo, el resumen y el entregable no se juzgan. Nota al margen: el resumen de `identificacion_necesidad_sucesion_ceo` usa las metaforas "speedboat" y "oil tanker", que no aparecen en el libro de Wasserman.
8. **Ediciones.** Se leyo la edicion que hay en los ficheros indicados. El nodo `analisis_trafico_competitivo` nombra AdRoll y Adbeat; el texto leido nombra Alexa y Compete. Si el extractor uso otra edicion, ese INFERIDO podria no serlo.
9. **Comprobacion mecanica de las citas.** Un script de control busco cada fragmento citado entre comillas en la linea indicada, con dos lineas de margen: 203 de 204 fragmentos casaron. El que no casa es un falso negativo del propio control (una cita seguida de coma), y la frase esta en L7422 del Value Proposition Design.

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

### 6.3 Donde probablemente estan los textos (no leido en la primera pasada; ver seccion 7)

El repo dice donde vivian los textos que se usaron para extraer el catalogo: `scripts/pipeline_libros.py` linea 63, `BOOKS_DIR = BASE / "books"` (carpeta `books/` en la raiz de una copia de trabajo del repo, fuera de git), y `scripts/_run_dominio_full2.log` lista ficheros como `Juran's Quality Handbook_ The C - Joseph A. Defeo.txt` y `The Green to Gold Business Play - Daniel C. Esty.txt`. En este equipo existe el directorio `C:\Users\AlexDesk\Documents\I have an idea\books` (comprobado solo que existe, con `ls -d`; no se listo ni se leyo su contenido, porque esa ruta no esta entre las fuentes autorizadas). Si el fundador la autoriza, la lectura puede hacerse sobre los 30 nodos ya sorteados.

### 6.4 Anexo: tabla completa paso a paso

Numero de nodo segun el sorteo (6.1). Fuente y capitulo de cada nodo en la seccion 7. `L` = numero de linea del fichero fuente. En las citas, la raya del original va como `--` (limitacion 6).

| # | node_id | mundo | paso | texto del paso (tag) | veredicto | cita del libro |
|---:|---|---|---:|---|---|---|
| 1 | `muestra_puntos_en_comun_antes_de_negociar` | compras | 1 | En la primera conversación, dedica unos minutos a preguntas personales antes de entrar en cifras. | **INFERIDO** | L4789: "en muchas culturas los negociadores invierten mucho tiempo en construir estos puntos de compenetración antes de empezar a pensar siquiera en la oferta". El libro pide construir compenetración antes de la oferta; las "preguntas personales" como medio las pone el extractor. |
| 1 | `muestra_puntos_en_comun_antes_de_negociar` | compras | 2 | Escucha qué palabras o valores repite la otra parte y usa ese mismo lenguaje al responder. | **FIEL** | L4793: "Mi interlocutor hacía constantes referencias que yo identifiqué como típicas de un converso al cristianismo" y L4797: "Todo esto supone una verdadera «mayordomía» para usted" (usar su propio lenguaje); ver también el reflejo, L930. |
| 1 | `muestra_puntos_en_comun_antes_de_negociar` | compras | 3 | Menciona con sinceridad algo que tengan en común: forma de trabajar, sector o experiencia previa. | **FIEL** | L5136: "Explota el principio de similitud... busca lo que les hace tilín y déjales ver que tenéis cosas en común". |
| 1 | `muestra_puntos_en_comun_antes_de_negociar` | compras | 4 | Evita fingir similitud que no existe, porque se nota y rompe la confianza. | **INFERIDO** | El libro no advierte contra fingir similitud. Lo más cercano es L1713: "ser «amable» como forma de simpatía fingida es a menudo igual de infructuoso" (sobre amabilidad, no similitud); y el reflejo es, L688, "el arte de insinuar que existe una similitud con la otra persona". |
| 2 | `domina_lo_que_compras` | compras | 1 | Investiga precios de referencia y variantes del insumo o servicio antes de hablar con el proveedor. | **FIEL** | L5871: "you need to know and understand the commod ity (or commodities) that you buy... If you do not know your commodity, sales people can easily take advantage of you. You will not get the best value because you do not know what that is." |
| 2 | `domina_lo_que_compras` | compras | 2 | Pregunta a otras personas de tu rubro que condiciones de compra consideran normales. | **FIEL** | L5885: "Go to professional soci ety meetings... Finding out how other people are procuring the same, or similar, goods and services is enlightening." |
| 2 | `domina_lo_que_compras` | compras | 3 | Usa tu propio formato para pedir cotizaciones en vez del que te entrega el proveedor. | **FIEL** | L5873: "Do not use a supplier's RFX template... a supplier's RFX is directed at getting the supplier everything that the supplier wants." |
| 2 | `domina_lo_que_compras` | compras | 4 | Identifica quienes son los competidores de tu proveedor y que ofrecen. | **FIEL** | L1581 a L1583 (registro de riesgos): "No competitors in market ... Find and research competitors in this industry and market". Nota: el pasaje de L5883 que parece inspirar el resumen habla de los competidores de TU empresa, no del proveedor. |
| 2 | `domina_lo_que_compras` | compras | 5 | Anota las preguntas que aun no puedes responder antes de sentarte a negociar. | **FIEL** | L4927: "ask questions either during the supplier's oral presen tation or before you begin negotiations"; y L879: "Jot down questions as you read the con tract". |
| 3 | `extraer_priorizar_hipotesis` | core | 1 | Lista todo lo que tiene que ser cierto sobre tu modelo de negocio, tu propuesta de valor y tu cliente | **FIEL** | L7422 a L7429: "To succeed, ask yourself what needs to be true about", seguido de "your business model?", "your value proposition?" y "your customer?" |
| 3 | `extraer_priorizar_hipotesis` | core | 2 | Escribe cada hipótesis por separado, una por nota | **FIEL** | L7514 (ejemplo de la priorizacion, en notas adhesivas): "duplicate hypothesis-- eliminate one sticky note": el ejercicio pone una hipotesis por nota. |
| 3 | `extraer_priorizar_hipotesis` | core | 3 | Elimina las que estén repetidas | **FIEL** | L7514: "duplicate hypothesis-- eliminate one sticky note". |
| 3 | `extraer_priorizar_hipotesis` | core | 4 | Identifica cuáles son capaces de acabar con tu proyecto si fallan | **FIEL** | L7444: "Identify the business killers. These are the hypotheses that are critical to the survival of your idea. Test them first!" |
| 3 | `extraer_priorizar_hipotesis` | core | 5 | Ordena todas tus hipótesis según qué tan crítica es cada una para que tu proyecto funcione | **FIEL** | L7447: "Rank all your hypotheses in order of how critical they are for your idea to survive and thrive". |
| 4 | `identificacion_necesidad_sucesion_ceo` | core | 1 | Desde tu primera ronda de inversión, habla abierto sobre las condiciones que podrían llevar a un cambio de liderazgo en el futuro | **FIEL** | L3337: "the process begins even before investors participate in their first round of financing... the investors should openly discuss the possibility of succession and the conditions that might trigger it"; y L3361: founders "should... raise the issue before accepting the capital". |
| 4 | `identificacion_necesidad_sucesion_ceo` | core | 2 | Vigila si los retos de tu negocio, como pasar del arranque inicial a conquistar el mercado masivo, piden nuevas capacidades de liderazgo | **FIEL** | L3138: "once the product or service has been developed and is ready to be sold, the startup becomes much more complex and the CEO faces dramatically different challenges". (Las metaforas speedboat y oil tanker del resumen no aparecen en el libro; no afectan a los pasos.) |
| 4 | `identificacion_necesidad_sucesion_ceo` | core | 3 | Sigue el proceso: deja que quien dirige opere, identifica los problemas y trabaja junto a esa persona para resolverlos, y si no hay mejora, decide el reemplazo | **FIEL** | L3337: "(a) Let the CEO run the company; (b) when a problem occurs, the board should identify it and try to work with the CEO to solve it; (c) if that doesn't work, "fire him." ... "coach, then replace."" |
| 4 | `identificacion_necesidad_sucesion_ceo` | core | 4 | Comunica de forma clara y repetida qué esperas sobre un posible cambio de liderazgo, porque quienes fundan suelen ignorar o minimizar estas señales | **FIEL** | L3339: "confident, passionate founder-CEOs often fail to receive that message... Even when directors think they have sent the message about succession, they must realize that, most likely, the message was not understood clearly, not taken as seriously as it was meant, or tuned out altogether." |
| 5 | `equipo_dedicado_continuo` | core | 1 | Definir un equipo central que permanezca en el proyecto de inicio a fin | **FIEL** | L4709: "in Agile-Stage-Gate, the core team remains intact from beginning to end of the project". |
| 5 | `equipo_dedicado_continuo` | core | 2 | Incorporar nuevos miembros especializados (manufactura, ventas) según avance el proyecto sin reemplazar al núcleo | **FIEL** | L4711: "new people may join the project as needed, for example, manufacturing and sales people may be added towards the commercialization phases". |
| 5 | `equipo_dedicado_continuo` | core | 3 | Buscar perfiles de equipo con expertise específico pero capacidades generalistas | **FIEL** | L4713: "They are experts in their functional area but also have a broad set of general capabilities". |
| 5 | `equipo_dedicado_continuo` | core | 4 | Mantener la responsabilidad y ownership del equipo hasta la revisión post-lanzamiento | **FIEL** | L4711: "the team members remain "on the team" throughout the project and up to the post-launch review"; y L4709: "one loses momentum, knowledge, accountability, and ownership". |
| 6 | `mejorar_deal_despues_del_hecho` | core | 1 | No des por definitivas las condiciones actuales hasta que llegue la salida (exit) | **FIEL** | L3720: "until an exit occurs--either an acquisition or an IPO--many of the terms don't matter much"; y L3718: "There are plenty of ways to fix things after the fact". |
| 6 | `mejorar_deal_despues_del_hecho` | core | 2 | Cuando busques tu siguiente ronda, cuéntale abiertamente al nuevo inversionista qué condiciones te están pesando | **FIEL** | L3720: "If you talk to your new potential financing partner about issues that are troubling you, in many cases the new VC will concentrate on trying to bring this back into balance". |
| 6 | `mejorar_deal_despues_del_hecho` | core | 3 | Después de un periodo de buen desempeño, abre una conversación honesta con tus inversionistas actuales | **FIEL** | L3722: "you still have the option of sitting down with your current VCs after you've had some run time together (again, assuming success)". |
| 6 | `mejorar_deal_despues_del_hecho` | core | 4 | Si llega una adquisición, negocia que parte del dinero de la venta se destine a retener a tu equipo | **FIEL** | L3724: "Most acquisition negotiations include a heavy focus on retention dynamics for the management team going forward, and there are often cases of reallocating some of the proceeds from the investors to management." |
| 6 | `mejorar_deal_despues_del_hecho` | core | 5 | Mantén siempre transparencia y trato justo con tus inversionistas para no dañar la relación | **FIEL** | L3726: "So, be thoughtful, fair, and open with your investors around the incentives and dynamics." |
| 7 | `playing_with_fire_gap` | core | 1 | Evaluar el daño potencial a la relación social si el negocio genera tensión | **FIEL** | L1094 a L1096: "Damage If the Social Relationship Blows Up"; "The closer the prior relationship, the greater the damage if tension from the business spills over into the relationship." Es uno de los dos factores del marco (L1133). |
| 7 | `playing_with_fire_gap` | core | 2 | Evaluar la probabilidad real de que el equipo discuta temas incómodos abiertamente | **FIEL** | L1111 y L1113: "Avoiding the "Elephant in the Room"... cofounders with prior social relationships are often the least likely to deal with the elephants in the room." Segundo factor del marco (L1133). |
| 7 | `playing_with_fire_gap` | core | 3 | Calcular la brecha entre ambos factores para cada relación de cofundador | **INFERIDO** | L1133: "For each type of relationship, the greater the distance between the two factors, the more the cofounders are "playing with fire."" El libro compara tipos de relacion en una figura cualitativa; no pide calcular la brecha para cada par de cofundadores. |
| 7 | `playing_with_fire_gap` | core | 4 | Identificar 'elefantes en la habitación' no discutidos (roles, equity, compromiso, visión) | **FIEL** | L1122: "Wozniak and Jobs failed to discuss crucial issues about roles and rewards that were too uncomfortable for best friends to broach"; y L1179: "Force sensitive discussions". |
| 8 | `diseno_etico_de_privacidad` | core | 1 | Enumera qué datos sensibles recolecta tu sistema (ubicación, salud, comportamiento, emociones). | **INFERIDO** | L1086: "Data is like garbage. You'd better know what you are going to do with it before you collect it." El libro describe los tipos de datos (L1001, "Data Parts Include People") pero no pide inventariar los datos sensibles de un sistema propio. |
| 8 | `diseno_etico_de_privacidad` | core | 2 | Diseña mecanismos de opt-out reales y accesibles, no ocultos en términos legales. | **INFERIDO** | L985: "it takes work to opt out. It's rarely (make that never) the default." El libro constata el problema; no prescribe disenar mecanismos de opt-out. |
| 8 | `diseno_etico_de_privacidad` | core | 3 | Evalúa el trade-off: ¿qué conveniencia pierde el usuario al optar por no compartir datos? | **INFERIDO** | L1009: "Maybe you want less agency. If the board game you need to buy... can be searched for and purchased in minutes... you've made time for something else." El libro describe el trade-off desde el usuario; no lo convierte en evaluacion de diseno. |
| 8 | `diseno_etico_de_privacidad` | core | 4 | Comunica de forma transparente cómo se usan y quién se beneficia de los datos recolectados. | **INFERIDO** | L1005: "The owner of the data has significantly more power than the generator"; L1007: "Where data pools lies power." No hay instruccion de comunicar como se usan los datos ni quien se beneficia. |
| 9 | `analisis_trafico_competitivo` | core | 1 | Buscar y comparar tráfico de competidores con herramientas como AdRoll o Adbeat | **INFERIDO** | L8522: "Use free traffic-measurement tools like Alexa and Compete to compare and understand the traffic generated by each competitive product or website". La accion es del libro, pero los ejemplos AdRoll y Adbeat no aparecen en el texto (grep sin resultados); los pone el extractor. |
| 9 | `analisis_trafico_competitivo` | core | 2 | Revisar rankings y reseñas en tiendas de apps | **FIEL** | L8524: "Mobile startups should visit every app store... Where do the competitors rank within the category... And read the product reviews". |
| 9 | `analisis_trafico_competitivo` | core | 3 | Visitar foros y sitios de preguntas (como Quora) para obtener información de mercado | **FIEL** | L8522: "Visit "answer" sites like Quora.com and start asking questions. This will cause more market information to surface". |
| 9 | `analisis_trafico_competitivo` | core | 4 | Organizar hallazgos en una grilla competitiva y mapa de mercado | **FIEL** | L8526: "Organize the competitive findings themselves into a competitive grid and a market map". |
| 10 | `saber_hasta_donde_mejorar_servicio` | entrega | 1 | Anota tu nivel actual de servicio: por ejemplo, que porcentaje de pedidos llega a tiempo y completo. | **FIEL** | L2937: "The first task, then, is to identify the factors that need to be measured... The second task is to produce a measure or series of measures." |
| 10 | `saber_hasta_donde_mejorar_servicio` | entrega | 2 | Pregunta a tus clientes si notarian la diferencia si mejoraras ese numero unos puntos mas. | **FIEL** | L2701: "The most common approach for the major element of a study is likely to be a detailed questionnaire-based customer survey"; y L2952: a 95 a 97 "may well have little, if any, noticeable impact on the customer's perception". |
| 10 | `saber_hasta_donde_mejorar_servicio` | entrega | 3 | Calcula cuanto te costaria en tiempo o dinero subir ese numero antes de intentarlo. | **FIEL** | L2948: "there is a need to balance the level of customer service with the cost of providing that service"; y L2952: "an increase of 2 per cent in service levels will cost far more between 95 and 97 per cent than between 70 and 72 per cent". |
| 10 | `saber_hasta_donde_mejorar_servicio` | entrega | 4 | Detente en el punto donde el costo de mejorar supera lo que el cliente valora. | **FIEL** | L2948: "the point where the additional revenue for each increment of service is equal to the extra cost of providing that increment". |
| 10 | `saber_hasta_donde_mejorar_servicio` | entrega | 5 | Revisa esta decision cada varios meses, porque las expectativas del cliente cambian. | **FIEL** | L2939: "any service measures are periodically reviewed. Businesses change fairly rapidly". |
| 11 | `aplicar_regla_fija_de_colchon_de_relleno` | entrega | 1 | Mide con una regla la distancia entre el producto y cada pared de la caja antes de cerrarla. | **FIEL** | Extraccion L26 a L30: "El contenido va CENTRADO con colchón en TODOS los lados... FedEx 2-3 pulgadas (5-7.5 cm)... UPS mínimo 2 pulgadas (5 cm)... DHL mínimo 6 cm de separación de las paredes". Medir la distancia es la forma directa de aplicar el umbral (medio operativo, no contenido nuevo). |
| 11 | `aplicar_regla_fija_de_colchon_de_relleno` | entrega | 2 | Ajusta el tamaño de caja si la distancia es menor a cinco centímetros en algún lado. | **FIEL** | Extraccion L15 a L16: "El tamaño correcto importa en las dos direcciones: muy justa no deja espacio para acolchado". |
| 11 | `aplicar_regla_fija_de_colchon_de_relleno` | entrega | 3 | Rellena cualquier espacio vacío hasta que el producto no se mueva al agitar la caja con cuidado. | **FIEL** | Extraccion L26 a L27: "todo vacío se rellena para que nada se mueva en tránsito"; FedEx HowToPack L123: "fill void spaces and prevent movement of goods inside the box". La prueba de agitar la caja no aparece (medio de verificacion del mismo criterio). |
| 11 | `aplicar_regla_fija_de_colchon_de_relleno` | entrega | 4 | Anota esta regla en un lugar visible de tu zona de empaque para no improvisar cada vez. | **INFERIDO** | Ni la extraccion ni HowToPack piden anotar la regla en un lugar visible. Lo mas cercano, extraccion L30: "Nodo: "regla de los ~5 cm de colchón por todos lados"". |
| 12 | `estrategia_proactiva_ambiental` | environmental | 1 | Revisa si tu estrategia ambiental actual es reactiva (solo cumplimiento) o proactiva | **FIEL** | L247 a L249: "Reactive or Proactive?... such a "compliance" approach to environmental protection dominated corporate attitudes for decades"; y L267: "we'll provide you with a practical guide to identify where your company lies on the "going green" spectrum". |
| 12 | `estrategia_proactiva_ambiental` | environmental | 2 | Define la sostenibilidad como algo estratégico para tu negocio, no solo como una tarea operativa | **FIEL** | L251: "Environmental issues and concerns about sustainability have become core concerns of society--and must become central elements of business strategy." |
| 12 | `estrategia_proactiva_ambiental` | environmental | 3 | Establece objetivos ambientales que anticipen regulaciones futuras y expectativas de tu mercado | **FIEL** | L2175: "To anticipate future standards of excellence, you will need to track emerging regulatory requirements, technology developments, and evolving public attitudes." |
| 12 | `estrategia_proactiva_ambiental` | environmental | 4 | Aplica la lente ambiental en todas las áreas de tu negocio, no solo en las operaciones | **FIEL** | L251: "Companies that want to stay ahead of the pack have to view all aspects of their business through an environmental lens." |
| 13 | `volverse_nativo_del_lugar` | environmental | 1 | Estudiar prácticas tradicionales o indígenas de manejo de recursos aplicables a la región del proyecto | **INFERIDO** | L537: el libro da el ejemplo de los Menominee, y advierte: "this particular form of forestry is not necessarily universal in its potential applications". No pide estudiar practicas indigenas de la region del proyecto. |
| 13 | `volverse_nativo_del_lugar` | environmental | 2 | Diseñar sistemas de extracción de recursos que mantengan o incrementen el capital natural a largo plazo | **FIEL** | L537: "The Menominee... use a logging method that lets them profit from nature while allowing it to thrive... today they have 1.7 billion standing feet--a slight increase"; y L471: "design them to get bigger and better in a way that replenishes, restores, and nourishes the rest of the world". |
| 13 | `volverse_nativo_del_lugar` | environmental | 3 | Evaluar la posibilidad de integrar industria y comunidad en lugar de separarlas mediante zonificación estricta | **FIEL** | L535: "industry can be so safe... that it need not be fenced off from other human activity. (This could stand the concept of zoning on its head; when manufacturing is no longer dangerous, commercial and residential sites can exist alongside factories". |
| 14 | `cinco_principios_guia_transformacion` | environmental | 1 | Comunicar públicamente el compromiso de la organización con un cambio de paradigma (no solo mejora incremental). | **FIEL** | L1032: "Signal your intention. Commit to a new paradigm, rather than to an incremental improvement of the old." |
| 14 | `cinco_principios_guia_transformacion` | environmental | 2 | Definir métricas de 'buen crecimiento' que incluyan impacto restaurador social y ambiental, no solo financiero. | **INFERIDO** | L1038: "Restore. Strive for "good growth," not just economic growth." El libro no habla de definir metricas de buen crecimiento. |
| 14 | `cinco_principios_guia_transformacion` | environmental | 3 | Destinar recursos y tiempo a proyectos de innovación paralelos, aceptando una tasa de éxito baja (10-15%). | **FIEL** | L1028: "in medium- and high-tech industries innovation typically has a success rate of 10 to 15 percent"; y L1046: "an automobile manufacturer might also be designing another car on the side". |
| 14 | `cinco_principios_guia_transformacion` | environmental | 4 | Establecer criterios de decisión que consideren el impacto en generaciones futuras y otras especies. | **FIEL** | L1048 a L1050: "Exert intergenerational responsibility... Ask: How can we support and perpetuate the rights of all living things to share in a world of abundance?" |
| 15 | `tipos_sitio_web_exportacion` | exportacion | 1 | Evaluar si el producto puede venderse completamente en línea (transaccional) o requiere solo información (informacional) | **FIEL** | L3203: transactional "allowing customers to search for, order, and pay for products online"; L3209: "An informational website is ideal for companies that market products and services that cannot be provided online or goods that cannot be sold online." |
| 15 | `tipos_sitio_web_exportacion` | exportacion | 2 | Investigar e-marketplaces relevantes para el sector y mercado objetivo (Amazon, Alibaba, eBay, etc.) | **FIEL** | L3213: "There is a profusion of marketplaces including eBay, Amazon, and China-based Alibaba." |
| 15 | `tipos_sitio_web_exportacion` | exportacion | 3 | Decidir el tipo de sitio web o combinación de modelos más adecuada para la empresa | **FIEL** | L3199: "Many U.S. companies have a website that fulfills one or more marketing functions tailored to their business specialties", seguido de los tres tipos (L3201 a L3213). |
| 15 | `tipos_sitio_web_exportacion` | exportacion | 4 | Definir presupuesto de diseño y mantenimiento según el tipo de sitio elegido | **INFERIDO** | L3209: "design and maintenance are less expensive than for a transactional website". El libro compara el coste de los tipos; no pide definir un presupuesto de diseno y mantenimiento. |
| 16 | `clausula_escape_contrato_representante` | exportacion | 1 | Definir el plazo de notificación previa para terminar el contrato (ej. 90 días) | **FIEL** | L1981: "either party may terminate the agreement with written advance notice of 30, 60, or 90 days"; L1985: "How far in advance must the representative be notified". |
| 16 | `clausula_escape_contrato_representante` | exportacion | 2 | Especificar por escrito qué constituye 'causa justa' de terminación | **FIEL** | L1987: "What is "just cause" for terminating a representative? Specifying causes for termination in the written contract usually strengthens your position." |
| 16 | `clausula_escape_contrato_representante` | exportacion | 3 | Determinar qué ley o convención internacional regirá disputas contractuales | **FIEL** | L1989: "Which country's laws (or which international conventions) govern a contract dispute?" |
| 16 | `clausula_escape_contrato_representante` | exportacion | 4 | Establecer qué compensación corresponde al representante en caso de despido | **FIEL** | L1991: "What compensation is due to the representative on dismissal?" |
| 16 | `clausula_escape_contrato_representante` | exportacion | 5 | Especificar la devolución de propiedad (patentes, marcas, registros, datos de clientes) | **FIEL** | L1993: "The contract should specify the return of property, including patents, trademarks, name registrations, and customer records." |
| 16 | `clausula_escape_contrato_representante` | exportacion | 6 | Aclarar si el representante tiene poder de 'agente' con implicaciones legales | **FIEL** | L1995: "The contract needs to specify whether the representative is a legal agent with power of attorney." |
| 16 | `clausula_escape_contrato_representante` | exportacion | 7 | Redactar el contrato en inglés y en el idioma oficial del país extranjero | **FIEL** | L1997: "the contract should be in both English and the official language of the foreign country". |
| 16 | `clausula_escape_contrato_representante` | exportacion | 8 | Obtener asesoría legal calificada sobre requisitos del país del representante | **FIEL** | L1983: "you should learn as much as you can about the legal requirements of the representative's country and obtain qualified legal counsel in preparing the contract". |
| 17 | `brokers_lead_referral_networks` | franquicias | 1 | Evalúa tu presupuesto de marketing y tus metas de crecimiento para decidir si te conviene usar brokers | **FIEL** | L4006: "In deciding whether to use brokers, factors to be considered include the aggressiveness of your franchise sales goals, the size of your marketing budget". |
| 17 | `brokers_lead_referral_networks` | franquicias | 2 | Elige las redes de brokers con el mismo cuidado con el que contratarías a alguien para vender por ti | **FIEL** | L4006: "Select your brokerage network (or networks) with the same care you would use in selecting an in-house franchise sales force." |
| 17 | `brokers_lead_referral_networks` | franquicias | 3 | Evita brokers que te pidan un porcentaje de regalías o cualquier pago continuo, más allá de la comisión por cierre | **FIEL** | L3982: "we strongly advise our clients to avoid any brokerage company that asks for a piece of the royalty or any other ongoing compensation". |
| 17 | `brokers_lead_referral_networks` | franquicias | 4 | Vigila de cerca cómo los brokers hablan de tu marca frente a los prospectos | **FIEL** | L3996: "prudent franchisors will make it their responsibility to monitor how the brokerage network is representing them". |
| 17 | `brokers_lead_referral_networks` | franquicias | 5 | Asiste a convenciones y mantén comunicación constante para que tu marca esté siempre presente en la mente de esa red | **FIEL** | L3998: "Franchisors who rely heavily on brokers will often spend money to attend or sponsor conventions for each brokerage network and develop formal communications plans to keep their concepts "top of mind"". |
| 18 | `folleto_franquicia` | franquicias | 1 | Contratar un consultor o agencia con experiencia específica en marketing de franquicias | **FIEL** | L3346: "use an experienced consultant or ad agency that really knows franchise marketing". |
| 18 | `folleto_franquicia` | franquicias | 2 | Diseñar en formato a cuatro colores con fotografía profesional de alta calidad | **FIEL** | L3346: "Go four-color with quality copy and design... Use excellent photography and paper stock." |
| 18 | `folleto_franquicia` | franquicias | 3 | Revisar el copy con el abogado de franquicias (regulado en ocho estados) | **INFERIDO** | L3346: "(Remember, ad copy for this brochure needs to be reviewed by regulators in eight states.)" El libro dice que lo revisan los reguladores de ocho estados; la revision con el abogado de franquicias la pone el extractor. |
| 18 | `folleto_franquicia` | franquicias | 4 | Decidir entre impresión offset (mayor calidad, mayor costo por tirada grande) o digital (menor tirada) | **FIEL** | L3346: "Good brochures can cost $4-$5 apiece if you use an offset print process... consider a print shop with digital printing capabilities... digital will provide you with high quality even with a lower print run (offset would be too expensive for a short run)". Nota: el libro atribuye alta calidad tambien a lo digital. |
| 19 | `embudo_ventas_franquicia` | franquicias | 1 | Mapea todas las vías por las que hoy te llegan contactos y cuánto te cuesta cada una | **FIEL** | L3547: "From left to right (highest cost-per-lead to lowest), you will generate franchise sales leads from public relations, print media, trade shows, direct mail, the internet, brokers..., and referrals." |
| 19 | `embudo_ventas_franquicia` | franquicias | 2 | Mide la tasa de conversión de cada vía en cada etapa del embudo (contacto, formulario, reunión, venta) | **FIEL** | L3553: "each will have their own associated close rates"; L3577: "About 13.5 percent of those filling out your confidential information request form (CIRF) to convert to a sale"; L3589: "You need to track everything". |
| 19 | `embudo_ventas_franquicia` | franquicias | 3 | Compara el costo por contacto y el costo por venta entre tus distintos canales | **FIEL** | L3565: "Each of the lead sources has its own anticipated cost-per-lead"; L3780: "cost per thousand (CPM), cost per lead, and cost per sale". |
| 19 | `embudo_ventas_franquicia` | franquicias | 4 | Mueve tu inversión de marketing hacia los canales que mejor resultado te dan según el tipo de franquiciado que buscas | **FIEL** | L3569: "the media mix that is best for some franchisors will be the absolute worst choice for others. If, for example, you are trying to sell a restaurant franchise to an experienced area development franchisee, the internet would be an extremely ineffective tool". |
| 19 | `embudo_ventas_franquicia` | franquicias | 5 | Arma un sistema para seguir todo el embudo de forma continua | **FIEL** | L3589: "You need to track everything if you want to optimize your franchise marketing and sales efforts." |
| 20 | `autonomia_dependencia_regulatoria` | health_safety | 1 | Identificar los límites estructurales que impiden al regulador conocer completamente las operaciones internas de la organización | **FIEL** | L4259: "Size, complexity, the peculiarities of organizational jargon..., the rapid development of technology and, on occasions, deliberate obfuscation all combine to make it difficult for the regulator to gain a comprehensive and in-depth view". |
| 20 | `autonomia_dependencia_regulatoria` | health_safety | 2 | Reconocer los riesgos de relaciones personales excesivamente cercanas entre inspectores y personal de la empresa regulada | **FIEL** | L4261: "Regulators, being human beings, tend to establish personal relationships with the regulated... and this sometimes compromises their ability to identify, report or sanction violations." |
| 20 | `autonomia_dependencia_regulatoria` | health_safety | 3 | Establecer mecanismos de verificación independientes que no dependan únicamente de la información proporcionada por el regulado | **INFERIDO** | L4261: "regulators tend to become dependent upon the regulated organizations to help them acquire and interpret information". El libro describe la dependencia; no propone mecanismos de verificacion independientes (la seccion siguiente, L4271, pasa a la autorregulacion). |
| 20 | `autonomia_dependencia_regulatoria` | health_safety | 4 | Evaluar si las sanciones actuales reflejan compromiso/negociación en lugar de cumplimiento real de la normativa | **INFERIDO** | L4265 (cita de Vaughan): "To interpret the consequences of this negotiation and bargaining (e.g., the 'slap-on-the-wrist' sanction or no sanction at all) as regulatory 'failures' is to miss the point." El libro no pide auditar las sanciones; hay tension con el paso, que trata el compromiso como algo a detectar frente al "cumplimiento real", pero no una contradiccion directa. |
| 21 | `prevalencia_omisiones` | health_safety | 1 | Clasificar los errores de mantenimiento históricos según tipo (omisión, instalación incorrecta, parte equivocada, otro) | **FIEL** | L2111: "I analysed the reports of 122 maintenance lapses occurring within a major airline over a three-year period", y la lista de L2113 a L2122: "Omissions (56%)", "Incorrect installations (30%)", "Wrong parts (8%)", "Other (6%)". |
| 21 | `prevalencia_omisiones` | health_safety | 2 | Identificar en qué nivel cognitivo (planificación, almacenamiento, ejecución, monitoreo) ocurren las omisiones más frecuentes | **CONTRARIO** | L2170 (la "former route" es la de los mecanismos cognitivos): "The former route is made difficult by the fact that an omission can arise within a number of cognitive processes... when the omission is made by another person at some time in the past, the underlying reasons may be impossible to discover. The task analysis route, on the other hand, is more promising." Y L1943: "Such a causal taxonomy is helpful in locating the underlying mental processes, but it is difficult for non-specialists to apply." El paso pide justo la via que el libro descarta para omisiones historicas y para no especialistas. |
| 21 | `prevalencia_omisiones` | health_safety | 3 | Enfocar las intervenciones de mejora en los pasos con mayor tasa de omisión histórica | **INFERIDO** | L2250: "it is therefore possible, in principle, to identify in advance those steps most vulnerable to omissions by establishing the number of omission-provoking features that each discrete step possesses". El libro elige los pasos por sus rasgos, por adelantado; la "tasa de omision historica" como criterio la pone el extractor. |
| 21 | `prevalencia_omisiones` | health_safety | 4 | Establecer métricas de seguimiento de omisiones por tipo de tarea | **INFERIDO** | L2089 a L2097 (Rasmussen: actividades asociadas a omisiones, "Repair and modification (41%)", etc.). El libro no propone metricas de seguimiento de omisiones por tipo de tarea. |
| 22 | `participacion_trabajadores` | health_safety | 1 | Crea un proceso simple para que te reporten peligros, incidentes y casi accidentes, incluyendo la opción de hacerlo de forma anónima | **FIEL** | L355: "Establish a process for workers to report injuries, illnesses, close calls/near misses, hazards... Include an option for anonymous reporting to reduce fear of reprisal." |
| 22 | `participacion_trabajadores` | health_safety | 2 | Da retroalimentación frecuente sobre lo que haces con cada reporte que recibes | **FIEL** | L429: "Provide frequent and regular feedback to show employees that their safety and health concerns are being heard and addressed." |
| 22 | `participacion_trabajadores` | health_safety | 3 | Comparte con tus trabajadores la información de seguridad, como las hojas de datos de seguridad (SDS), los datos de lesiones y las inspecciones | **FIEL** | L369 a L386: "Give workers the information they need... Safety Data Sheets (SDSs)... Injury and illness data... Workplace inspection reports". |
| 22 | `participacion_trabajadores` | health_safety | 4 | Involucra a tus trabajadores en el diseño de metas, análisis de peligros, inspecciones, capacitación y desarrollo de soluciones | **FIEL** | L391 a L414: "Provide opportunities for workers to participate in all aspects of the program... Develop the program and set goals... Analyze hazards... Conduct site inspections... Train current coworkers... develop solutions". |
| 22 | `participacion_trabajadores` | health_safety | 5 | Elimina barreras de idioma, habilidad, educación o miedo a represalias | **FIEL** | L427: "Ensure that workers from all levels of the organization can participate regardless of their skill level, education, or language."; L433: retaliation. |
| 22 | `participacion_trabajadores` | health_safety | 6 | Comunica con claridad las protecciones contra represalias que existen en tu país y revisa que tus incentivos no desalienten el reporte | **FIEL** | L435: "Post the 11(c) fact sheet... in the workplace"; L437: "Incentive programs... should be designed in a manner that does not discourage injury and illness reporting". |
| 23 | `accion_correctiva_sistematica` | quality | 1 | Documenta cada problema detectado en una ficha simple: qué pasó, qué tan grave es, por qué pasó, quién se encarga y para cuándo | **FIEL** | L2869: "These meetings should be documented on an item-by-item action chart that states the problem, the seriousness of the problem, and its cause, as well as who is going to do what when." |
| 23 | `accion_correctiva_sistematica` | quality | 2 | Revisa a diario los problemas nuevos junto con la persona que te ayuda con calidad o producción, si la tienes | **FIEL** | L2869: "Hold daily meetings between the area supervisor and a quality engineer or supervisor to examine the problems detected." |
| 23 | `accion_correctiva_sistematica` | quality | 3 | Si un problema no se resuelve en la revisión diaria, pásalo a una revisión semanal más a fondo | **FIEL** | L2871: "Hold weekly meetings between the production general supervision and senior quality management to attack problems that cannot be, or were not, solved at the lower level." |
| 23 | `accion_correctiva_sistematica` | quality | 4 | Revisa una vez al mes lo que sigue sin resolverse y decide si necesita un esfuerzo dedicado aparte | **FIEL** | L2873: "Monthly or special meetings should be held by the general manager and staff to review the unresolved problems... those requiring complex or long-range action should be assigned to a task team". |
| 23 | `accion_correctiva_sistematica` | quality | 5 | Para los problemas más complejos, junta puntualmente a las personas involucradas en un grupo de trabajo con un responsable claro, y disuélvelo en cuanto el problema quede resuelto | **FIEL** | L2873: "Task teams should consist of responsible members of each affected organization with one person appointed as chairperson... At the time the problem is judged to be eliminated, the team should be dissolved." |
| 23 | `accion_correctiva_sistematica` | quality | 6 | Ordena los problemas por gravedad y ataca primero los más grandes | **FIEL** | L2875: "Corrective action is most successful when it operates on the well known Pareto principle, which states that the biggest and most important problems should be attacked first". |
| 23 | `accion_correctiva_sistematica` | quality | 7 | Define acciones que corrijan la causa raíz y prevengan la recurrencia, no solo alivien la presión del momento | **FIEL** | L2869: "Determine methods of cor- the present situations while preventing their recurrence in the future"; L2875: "fix a problem once and for all so it will never come back". |
| 23 | `accion_correctiva_sistematica` | quality | 8 | Escala los problemas más sutiles o de largo plazo a un nivel de decisión superior con frecuencia regular, para que no se acepten como normales | **FIEL** | L1629: "also less obvious problems--as seen by the working people themselves--that require attention... Those that cannot be resolved are formally passed up to the next level of supervision for review at their regular meeting." |
| 23 | `accion_correctiva_sistematica` | quality | 9 | Dar seguimiento y verificar que la acción implementada haya eliminado el problema | **FIEL** | L2873: "At the time the problem is judged to be eliminated, the team should be dissolved"; L2899: "Corrective action has been taken. The problem won't happen again." |
| 24 | `decision_conformidad_producto` | quality | 1 | Entrenar a inspectores y operadores en el conocimiento de productos, estándares e instrumentos. | **FIEL** | L24389: "they are trained to understand the products, the standards, and the instruments." |
| 24 | `decision_conformidad_producto` | quality | 2 | Delegar la autoridad de juicio de conformidad a inspectores o sistemas automatizados. | **FIEL** | L24389: "the work is organized so that inspectors or production workers can make these decisions themselves... (In many cases, the delegation is to automated instruments.)" |
| 24 | `decision_conformidad_producto` | quality | 3 | Establecer procedimientos de identificación ('stamp') para productos conformes. | **FIEL** | L24391: "The inspector is authorized to identify the product ("stamp it up") as acceptable product." |
| 24 | `decision_conformidad_producto` | quality | 4 | Definir políticas de gestión sobre el envío de productos conformes. | **FIEL** | L24391: "company procedures (which are established by the managers) provide that conforming products should be shipped as a regular practice." |
| 25 | `pruebas_inadecuadas_prototipos` | quality | 1 | Realizar pruebas con muestras que reflejen la variación real esperada en producción, no solo valores nominales | **FIEL** | L3037: "put together a prototype of an assembly with every part very close to the nominal... when the assembly goes into production, all characteristics will vary"; L3055: Monte Carlo "equally helpful in tests of actual hardware, although the number of combinations of departures from nominal values must be drastically reduced". |
| 25 | `pruebas_inadecuadas_prototipos` | quality | 2 | Aplicar métodos Monte Carlo para simular variaciones de dimensión, presión, temperatura, etc. en diseño asistido por computadora | **FIEL** | L3055: "Monte Carlo methods can be of help in testing, especially in the stage of computer-assisted design, by varying dimensions, pressure, temperature, torque". |
| 25 | `pruebas_inadecuadas_prototipos` | quality | 3 | Verificar el estado de control estadístico del proceso antes de confiar en resultados de prototipos | **FIEL** | L3037: "In practice, there may be no predictable distribution of many of the parts, the state of statistical control being still far in the future. The fact is that volume production may turn out only one part in 100,000 that will perform like the prototype." |
| 25 | `pruebas_inadecuadas_prototipos` | quality | 4 | Formular preguntas clave sobre a qué se refieren los resultados de prueba: ¿predicen la corrida de mañana o el resultado de próximo año? | **FIEL** | L3041 a L3045: "1. What will the results refer to? 2. Will they refer to tomorrow's run or to next year's crop?" |
| 26 | `sistema_de_alarma_de_defectos` | quality | 1 | Definir indicadores clave que disparen alarmas de calidad | **FIEL** | L23867: "upper management properly looks to the people associated with the quality function to set up alarm signals to detect quality failures". |
| 26 | `sistema_de_alarma_de_defectos` | quality | 2 | Establecer un cronograma común entre comprador y proveedor | **INFERIDO** | L23867: "Under many contracts, the buyer and supplier are yoked to a common timetable for completion of the final product. Usually, a separate department (e.g., materials management) presides over major aspects of scheduling." El libro da el cronograma comun por existente y lo pone en otro departamento; establecerlo como paso del sistema de alarmas lo pone el extractor. |
| 26 | `sistema_de_alarma_de_defectos` | quality | 3 | Asignar responsables de actuar sobre las alarmas | **FIEL** | L23867: "the people associated with the quality function... to act positively on these signals to avoid deterioration, whether in quality, cost, or delivery." |
| 26 | `sistema_de_alarma_de_defectos` | quality | 4 | Documentar tiempos de respuesta esperados | **INFERIDO** | L23867: "Establishment of a system of timely response to alarm signals". El libro pide respuesta oportuna; no pide documentar tiempos de respuesta esperados. |
| 27 | `plan_de_desastre_y_recuperacion` | risk_management | 1 | Identifica los pocos desastres que te dejarían fuera del juego: pérdida de datos, salud, un local. | **FIEL** | L6139: "project stakeholder organisations need to prepare and maintain plans to deal with the more severe risks they face, especially those where the consequences could be considered critical or disastrous." (Los ejemplos del paso, datos, salud, local, son adaptacion al emprendedor.) |
| 27 | `plan_de_desastre_y_recuperacion` | risk_management | 2 | Para cada uno, escribe los pasos concretos que te devolverían a operar, en orden. | **FIEL** | L8852: "we can also rationalise an affiliation with project risks if we projectify the response and recovery planning processes"; L6075: "Emergency response and recovery plans and procedures should be pre-planned". |
| 27 | `plan_de_desastre_y_recuperacion` | risk_management | 3 | Prepara de antemano lo que esa recuperación necesita: respaldos, contactos, un fondo. | **FIEL** | L5766: "precautionary measures such as backup resources and recovery planning, contingency allocations, reserve funds". |
| 27 | `plan_de_desastre_y_recuperacion` | risk_management | 4 | Guarda el plan donde puedas acceder a él aunque hayas perdido lo demás. | **INFERIDO** | El libro no dice donde guardar el plan. Lo mas cercano, L6139 a L6160 (lista de 10.7: comunicaciones, rutas de acceso, recursos) y L6075 (planes "formalised, rehearsed"); nada sobre acceso al plan tras perderlo todo. |
| 28 | `escepticismo_sano_ante_el_riesgo` | risk_management | 1 | De cualquier método de riesgo que uses, pregúntate cómo sabrías si de verdad te está ayudando. | **FIEL** | L549: "A harder question to answer is, "What is the evidence for the belief that it works?""; L596: "we must ask, again, "How do we know it works?"" |
| 28 | `escepticismo_sano_ante_el_riesgo` | risk_management | 2 | Desconfía de la calma: que te sientas seguro no es prueba de que estás seguro. | **FIEL** | L607: "An analysis placebo produces the feeling that some analytical method has improved decisions and estimates even when it has not." |
| 28 | `escepticismo_sano_ante_el_riesgo` | risk_management | 3 | Antes de adoptar una plantilla ajena, busca evidencia de que a alguien le funcionó de verdad. | **FIEL** | L549 ("What is the evidence for the belief that it works?") y L676: "the mere fact that other organizations bought it... is proof that it worked. I call this the testimonial proof... the testimonial is not evidence of effectiveness." El paso pide evidencia de que funciono "de verdad", no testimonio. |
| 28 | `escepticismo_sano_ante_el_riesgo` | risk_management | 4 | Prefiere una nota simple y honesta a un tablero vistoso que no puedas comprobar. | **INFERIDO** | L607: "the mere appearance of structure and formality in risk management is pleasing to some". El libro condena la apariencia sin prueba, pero su alternativa son modelos cuantitativos simples (L946: "a simple Monte Carlo simulation done in a spreadsheet"; L2808), no "una nota simple". |
| 29 | `getting_started_system_information_integrity` | seguridad_digital | 1 | Suscribirse a fuentes de alertas de seguridad (CISA, NSA, FBI, ISACs, proveedores). | **FIEL** | L697 a L705: "Staying up to date on system security alerts, advisories, and directives is essential... (CISA)... (NSA)... (FBI)... industry Information Sharing and Analysis Centers (ISACs)". |
| 29 | `getting_started_system_information_integrity` | seguridad_digital | 2 | Establecer una estrategia de monitoreo del sistema con procedimientos y herramientas definidas. | **FIEL** | L707: "Establish a System Monitoring Strategy, Including"; L709: "Procedures for system monitoring tools and techniques." |
| 29 | `getting_started_system_information_integrity` | seguridad_digital | 3 | Detectar ataques, conexiones no autorizadas y actividades inusuales en tráfico entrante/saliente. | **FIEL** | L709: "Monitoring the system to detect attacks, indicators of potential attacks, and unauthorized connections... Unusual or unauthorized activities or conditions for inbound communications traffic... outbound". |
| 29 | `getting_started_system_information_integrity` | seguridad_digital | 4 | Establecer políticas de gestión y retención de CUI conforme a leyes y regulaciones. | **FIEL** | L717: "Establish policies and procedures for managing and retaining CUI in accordance with applicable laws". |
| 29 | `getting_started_system_information_integrity` | seguridad_digital | 5 | Eliminar CUI de sistemas no federales una vez concluidos los contratos para reducir la superficie de ataque. | **FIEL** | L717: "Retaining CUI on nonfederal systems after contracts or agreements have concluded increases the attack surface for those systems". |
| 30 | `funcion_respond_plan_incidentes` | seguridad_digital | 1 | Definir protocolo de notificación a clientes, empleados y terceros afectados | **FIEL** | L51: "Have a plan for"; L53: "Notifying customers, employees, and others whose data may be at risk." |
| 30 | `funcion_respond_plan_incidentes` | seguridad_digital | 2 | Establecer procedimientos para mantener operaciones durante un incidente | **FIEL** | L55: "Keeping business operations up and running." |
| 30 | `funcion_respond_plan_incidentes` | seguridad_digital | 3 | Crear proceso de reporte a autoridades y fuerzas del orden | **FIEL** | L57: "Reporting the attack to law enforcement and other authorities." |
| 30 | `funcion_respond_plan_incidentes` | seguridad_digital | 4 | Documentar pasos de investigación y contención de ataques | **FIEL** | L75: "Investigating and containing an attack." |
| 30 | `funcion_respond_plan_incidentes` | seguridad_digital | 5 | Probar el plan de respuesta regularmente mediante simulacros | **FIEL** | L59: "Test your plan regularly." (El medio, simulacros, no se nombra.) |

## 7. Fuentes indicadas por el fundador despues de la semilla

**Cuando y como.** El 23 sep 2026, despues del commit de la semilla (`c038586d`) y del primer resultado sin fuente (`835e92d6`), el fundador indico, a traves de la sesion que lanzo este muestreo, una lista cerrada de ficheros de solo lectura con los textos de los 23 libros. La seccion 2 del pre-registro no se reescribe: esta seccion la completa. **La muestra no cambio:** se leyeron los mismos 30 nodos y 138 pasos del sorteo de la seccion 6.1, y no se volvio a sortear. Solo se abrieron los ficheros de la lista (y, para el nodo de couriers, el complemento autorizado `HowToPack_fxcom.txt`). No se listo ni se abrio nada mas de esas carpetas. Los 24 ficheros existian con el nombre exacto; ninguno resulto ser otro libro ni estar roto, asi que ningun paso quedo SIN FUENTE.

**Fuente y capitulo de cada nodo** (rutas completas; `IHAI` = `C:\Users\AlexDesk\Documents\I have an idea`):

| # | node_id | fuente leida | capitulo o seccion |
|---:|---|---|---|
| 1 | `muestra_puntos_en_comun_antes_de_negociar` | `IHAI\txt\Procurenment\Rompe la barrera del no_ 9 prin - Chris Voss.txt` | cap. 10 "Encuentra el cisne negro", seccion "El principio de similitud" (L4778); apoyo en cap. 2 (reflejo, L688 y L930) y cap. 4 (L1713) |
| 2 | `domina_lo_que_compras` | `IHAI\txt\Procurenment\Diana L. Lindstrom - Procurement Project Management Success_ ... (2014).txt` | cap. 11 "Final Words", "Know Your Commodity" y "Know Your Business and Industry" (L5869 a L5885); registro de riesgos (L1581); cap. 8 "Negotiations", "Information" (L4927) |
| 3 | `extraer_priorizar_hipotesis` | `IHAI\txt\Value Proposition Design - Smith, Alan, Osterwalder, Alexa.txt` | parte "Test": "Extract Your Hypotheses" y "Prioritize Your Hypotheses" (L7392 a L7514) |
| 4 | `identificacion_necesidad_sucesion_ceo` | `IHAI\txt\The Founder's Dilemmas - Wasserman, Noam.txt` | cap. 10 "Failure, Success, and Founder-CEO Succession" (L3053) |
| 5 | `equipo_dedicado_continuo` | `IHAI\txt\Winning at New Products_ Creati - Robert G. Cooper.txt` | cap. 6 "The Agile-Stage-Gate Hybrid Model" (L4217; pasaje L4709 a L4713) |
| 6 | `mejorar_deal_despues_del_hecho` | `IHAI\txt\Venture Deals - Brad Feld.txt` | cap. 13 "Negotiation Tactics", "Can You Make a Bad Deal Better?" (L3715) |
| 7 | `playing_with_fire_gap` | `IHAI\txt\The Founder's Dilemmas - Wasserman, Noam.txt` | cap. 4 "Relationship Dilemmas: Flocking Together and Playing with Fire" (L941; pasaje L1085 a L1179) |
| 8 | `diseno_etico_de_privacidad` | `IHAI\txt\Assembling Tomorrow_ A Guide to - Scott Doorley.txt` | cap. 2 "Flow": "Data Zero Top Ten!", "Data Floods", "Data Parts Include People" (L933 a L1090) |
| 9 | `analisis_trafico_competitivo` | `IHAI\txt\The Startup Owner's Manual_ The - Blank, Steve.txt` | cap. 4 "Customer Discovery, Phase Two", "Traffic/Competitive Analysis (Web/Mobile)" (L8505) |
| 10 | `saber_hasta_donde_mejorar_servicio` | `C:\Users\AlexDesk\Downloads\Supply chain\The Handbook of Logistics and D - Alan Rushton;Phil Croucher;Pete.txt` | cap. 3 "Customer service and logistics", "Levels of customer service" (L2945 a L2952) |
| 11 | `aplicar_regla_fija_de_colchon_de_relleno` | `IHAI\txt\Supply chain\EXTRACCION_EMPAQUE_COURIERS.md` y `C:\Users\AlexDesk\Downloads\Supply chain\HowToPack_fxcom.txt` | extraccion, "TEMA 2: EL ACOLCHADO" (L25 a L38); FedEx How to Pack (L123) |
| 12 | `estrategia_proactiva_ambiental` | `IHAI\books\Especificos\Environmental\The Green to Gold Business Play - Daniel C. Esty.txt` | cap. 1 "Why Every Business Needs an Eco-Strategy", "Reactive or Proactive?" (L247); L2175 |
| 13 | `volverse_nativo_del_lugar` | `IHAI\books\Especificos\Environmental\Cradle to Cradle - Michael Braungart.txt` | cap. 3 "Eco-Effectiveness", "Becoming a Native" (L529 a L539) |
| 14 | `cinco_principios_guia_transformacion` | `IHAI\books\Especificos\Environmental\Cradle to Cradle - Michael Braungart.txt` | cap. 6 "Putting Eco-Effectiveness into Practice" (L889; pasaje L1028 a L1050) |
| 15 | `tipos_sitio_web_exportacion` | `IHAI\books\exportacion\basic-guide-to-exporting_Latest_eg_main_086196.txt` | cap. 11 "Going Online: E-Exporting Tools for Small Businesses" (L3199 a L3213) |
| 16 | `clausula_escape_contrato_representante` | `IHAI\books\exportacion\basic-guide-to-exporting_Latest_eg_main_086196.txt` | cap. 5 "Methods and Channels", acuerdo con el representante extranjero (L1979 a L1997) |
| 17 | `brokers_lead_referral_networks` | `IHAI\books\franquicias\Franchise Your Business - Mark Siebert.txt` | cap. 10 "Franchise Lead Generation", "Brokers" (L3976 a L4008) |
| 18 | `folleto_franquicia` | `IHAI\books\franquicias\Franchise Your Business - Mark Siebert.txt` | cap. 9 "Franchise Marketing: Your Unique Message", "The Franchise Brochure" (L3340 a L3346) |
| 19 | `embudo_ventas_franquicia` | `IHAI\books\franquicias\Franchise Your Business - Mark Siebert.txt` | cap. 10 "Franchise Lead Generation", "Franchise Sales Funnel" (L3543 a L3589) |
| 20 | `autonomia_dependencia_regulatoria` | `IHAI\books\Especificos\Health and Safety\Managing the Risks of Organizat - Reason, J. T_.txt` | cap. 8 "The Regulator's Unhappy Lot", "Autonomy and Dependence as Constraints on the Regulatory Process" (L4252) |
| 21 | `prevalencia_omisiones` | `IHAI\books\Especificos\Health and Safety\Managing the Risks of Organizat - Reason, J. T_.txt` | cap. 5 "Maintenance can Seriously Damage your System", "The Prevalence of Omissions" y "Omission-prone Task Features" (L2066 a L2259); L1943 |
| 22 | `participacion_trabajadores` | `IHAI\books\Especificos\Health and Safety\OSHA3885.md` | "Worker Participation", action items 1 a 5 (L313 a L437) |
| 23 | `accion_correctiva_sistematica` | `IHAI\books\Especificos\Quality\Quality is free _ the art of making quality certain -- Philip B_ Crosby.md` | "Step Six: Corrective Action" (L1627, resumen de los catorce pasos; L2861, desarrollo del paso) |
| 24 | `decision_conformidad_producto` | `IHAI\books\Especificos\Quality\Juran's Quality Handbook_ The C - Joseph A. Defeo.txt` | cap. 24 "Inspection, Test, and Measurement", "The Conformance Decision" (L24386) |
| 25 | `pruebas_inadecuadas_prototipos` | `IHAI\books\Especificos\Quality\Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev.txt` | cap. 3 "Diseases and Obstacles", "Inadequate testing of prototypes" (L3034) |
| 26 | `sistema_de_alarma_de_defectos` | `IHAI\books\Especificos\Quality\Juran's Quality Handbook_ The C - Joseph A. Defeo.txt` | cap. 23 "Managing Quality in the Supply Chain", punto 12 (L23867) |
| 27 | `plan_de_desastre_y_recuperacion` | `IHAI\books\Risk Management\Managing Project Risks - Peter J. Edwards.txt` | 10.7 "Disaster Planning and Recovery" (L6137); cap. 15 "Planning for Crisis Response and Disaster Recovery" (L8817) |
| 28 | `escepticismo_sano_ante_el_riesgo` | `IHAI\books\Risk Management\The Failure of Risk Management_ - Douglas W. Hubbard.txt` | cap. 3 "How Do We Know What Works?" (L528 a L676); L946 y L2808 |
| 29 | `getting_started_system_information_integrity` | `IHAI\books\seguridad_digital\NIST.SP.1318.txt` | "Getting Started with System and Information Integrity" (L687 a L717) |
| 30 | `funcion_respond_plan_incidentes` | `IHAI\books\seguridad_digital\cybersecurity_sb_nist-cyber-framework.txt` (FTC) | "4. RESPOND" (L49 a L75) |

El nombre del fichero 2 esta abreviado en la tabla; el completo es `Diana L. Lindstrom - Procurement Project Management Success_ Achieving a Higher Level of Effectiveness-J. Ross Publishing (2014).txt`.
