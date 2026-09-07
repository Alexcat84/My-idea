# -*- coding: utf-8 -*-
r"""_v196_t2_mis_clases.py . MIS CLASES SOBRE LOS 120 PARES, ESCRITAS ANTES DE
ABRIR EL DESTAPE, Y EL COTEJO CONTRA EL ARCHIVO.

EL ORDEN ES LO UNICO QUE HACE QUE EL COTEJO VALGA: la tabla `CLASES` de abajo se
escribio leyendo SOLO `docs/loop/SALIDA_V196_T2_CIEGA.txt`, y este fichero se
COMMITEA con las clases dentro ANTES de que nadie corra el cotejo. El destape se
abre despues, y desde el codigo, no con los ojos.

LOS DISCUTIBLES VAN MARCADOS AQUI, ANTES DE SABER SI SE ACIERTA, que es lo que
`EJECUTOR.md` 7 exige con esas palabras.

LOS QUEMADOS TAMBIEN VAN MARCADOS AQUI, y no se eligieron despues de cotejar: la
lista vive sellada en `scripts/loop/vuelta196_tarea2_relectura_al_doble.py` y este
fichero la IMPORTA en vez de volver a teclearla.

LA CONTAMINACION MAYOR SE DECLARA Y SE MIDE, y no es la de los seis quemados: la
seccion 2 del acta 196, que la TAREA 1 de esta misma vuelta obliga a leer entera,
PUBLICA EL REPARTO DEL ARCHIVO SOBRE LOS 60 PUESTOS DEL TRAMO (`A 8, B 1, C 0,
D 51`). Eso no es la clase de un puesto: es la distribucion de la mitad del
sujeto. Por eso el cotejo se publica TRES veces, y la unica lectura que puede
llamarse ciega de verdad es la del DOBLE.

USO:
  python scripts/loop/_v196_t2_mis_clases.py            (solo escribe mis clases)
  python scripts/loop/_v196_t2_mis_clases.py --cotejar  (abre el destape y coteja)
"""
import argparse
import hashlib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta196_tarea2_relectura_al_doble import QUEMADOS   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
ARCHIVO = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
CIEGA = "docs/loop/SALIDA_V196_T2_CIEGA.txt"
DESTAPE = "docs/loop/SALIDA_V196_T2_DESTAPE.txt"
SELLADA_DEL_DOBLE = "docs/loop/_auditor_v196_doble_para_la_197.txt"

# LA CONTAMINACION DE LA MITAD DEL SUJETO, DECLARADA CON SU SEDE Y SU CIFRA.
REPARTO_FILTRADO = {"A": 8, "B": 1, "C": 0, "D": 51}
SEDE_DEL_FILTRADO = ("acta 196, seccion 2: MI REPARTO CONTRA EL DEL ARCHIVO. "
                     "Publica el reparto del archivo sobre los 60 del tramo")

# (puesto, clase, marca, razon). Escritas leyendo SOLO la ciega.
CLASES = [
    (10, "D", "", "Criterios propios antes de contactar contra investigar el mercado. Cada lado conserva su procedimiento."),
    (11, "D", "", "Reconocer la urgencia artificial contra estructurar la visita como solo evaluacion. Procedimiento a los dos lados."),
    (12, "D", "", "Gestionar el contrato firmado contra investigar antes de renovar. Momentos y entregables distintos."),
    (13, "D", "", "Intereses no posiciones contra preparar el punto de retirada. Comparten una linea, problema no persona, y nada mas."),
    (24, "D", "", "Dos tacticas distintas: el permiso para decir no contra el silencio y no partir la diferencia."),
    (25, "D", "", "La aritmetica del lote contra el costo del stock muerto. Uno termina en cantidad de pedido y el otro en fecha de liquidacion."),
    (26, "D", "", "El no del proveedor contra verificar que el si es real. B trae un procedimiento entero que A nombra en una linea."),
    (27, "D", "", "Preguntas calibradas contra el permiso para decir no. Tacticas hermanas y distintas."),
    (71, "D", "", "Preparacion y agenda contra la tactica del no."),
    (72, "D", "", "Intereses no posiciones contra el silencio."),
    (73, "D", "", "Valor no economico contra preparacion y agenda."),
    (74, "D", "", "Preparacion y agenda contra punto unico de contacto."),
    (133, "D", "", "Documentar lo que queda fuera del alcance contra el registro de lecciones. Artefactos y momentos distintos."),
    (134, "D", "", "Puntos en comun antes de negociar contra prepararse para marcharse."),
    (135, "D", "", "Intereses no posiciones contra verificar quien decide o veta."),
    (139, "D", "", "Prepararse para marcharse contra avisar a los proveedores no elegidos."),
    (159, "D", "", "Clasificar Full contra Limited es la decision; Magnuson Moss son los tres requisitos y el abogado."),
    (160, "A", "", "Ids sinonimos, y TRES de los cuatro pasos de B son pasos de A. Lo que queda fuera son lineas: party round y desacuerdos al lider."),
    (161, "A", "", "Los pasos 2, 3 y 4 de B son los pasos 1, 5 y 6 de A, dos de ellos palabra por palabra. B esta entero dentro de A."),
    (162, "D", "", "Magnuson Moss nombra los terminos enganosos en una linea y B los despliega en procedimiento propio."),
    (204, "D", "", "Terminos economicos del venture debt contra el pricing del warrant: el hijo despliega dos pasos de la madre en siete, y la madre conserva tasa, comisiones y la comparacion banco contra fondo."),
    (205, "D", "", "Inside out contra outside in: dos patrones opuestos de innovacion abierta."),
    (206, "A", "", "Los cuatro pasos de B son literalmente las cuatro fases que A ya escribe en sus pasos 6 a 9. B no anade nada que no sea una linea."),
    (207, "B", "DISCUTIBLE", "Los dos seleccionan arenas cruzando atractivo de mercado con fortaleza propia, y se cruzan justo en el medio. Se distinguen en el encuadre: uno termina en roadmap y el otro en filtro de gate."),
    (397, "D", "", "Capital humano, social y financiero del fundador contra la critica desapasionada de la idea."),
    (398, "D", "", "Orden de comunicacion tras un despido ejecutivo contra el proceso de despidos responsables."),
    (399, "D", "", "Terminos enganosos de la garantia contra la clausula de venta atada."),
    (400, "A", "DISCUTIBLE", "Tres de los cinco pasos de B son pasos de A, uno casi palabra por palabra. Fuera del solape quedan lineas a los dos lados: fisico o digital contra habitos de compra."),
    (613, "D", "", "Construir la matriz probabilidad por impacto contra el plan de gestion de riesgos entero."),
    (614, "A", "", "Los CUATRO pasos de A estan dentro de los nueve de B, dos de ellos palabra por palabra. A no anade procedimiento."),
    (615, "D", "", "Las cuatro etapas del customer development contra la introduccion al discovery."),
    (616, "D", "", "Gates go kill con seis criterios contra la revision formal con strategic buckets."),
    (654, "B", "QUEMADO", "Dos listas de tacticas de activacion cruzadas en el medio por la prueba gratuita, sin que ninguna nombre a la otra. QUEMADO: el acta 196 declara que su clase se publico."),
    (655, "A", "DISCUTIBLE", "Ids casi identicos, y por 9.6.3 eso NO decide. Lo que decide: fuera del solape A conserva la preparacion del MVP y las tres preguntas de escala, y B solo dos lineas de filosofia."),
    (656, "D", "", "El analisis de ratios nombra el ROA en una linea y B lo despliega con formula y verificacion del balance."),
    (657, "D", "", "Conexion personal y emocional contra la investigacion de datos: rituales y nombre propio contra CRM y fuentes."),
    (719, "D", "QUEMADO", "Bienvenida tras la compra contra celebracion de un logro: dos FASES distintas de la misma serie, y por la regla de familia dos fases distintas son sanas. QUEMADO."),
    (720, "D", "", "Papel del fundador en la busqueda del CEO contra la planificacion de la sucesion."),
    (721, "D", "", "La etapa de iluminacion nombra la intimacion en una linea y B la despliega en procedimiento."),
    (722, "D", "", "Equipos de visita a cliente contra etnografia: guia de entrevista e hipotesis contra observar sin interferir."),
    (880, "D", "DISCUTIBLE", "La tribu de marca nombra el marcador visual en una linea y B lo despliega, pero dos de los cinco pasos de B repiten a A palabra por palabra."),
    (881, "D", "", "El diccionario de la WBS contra construir la WBS: dos artefactos distintos."),
    (882, "D", "", "La busqueda del CEO externo nombra el involucramiento del fundador en una linea y B lo despliega."),
    (883, "A", "", "Los cuatro pasos de B son cuatro de los seis de A, dos de ellos palabra por palabra. B no anade nada."),
    (908, "A", "DISCUTIBLE", "Mismo procedimiento de cuatro pasos uno a uno: mercado, dolores, capacidades propias, solucion integrada. Lo unico que cambia es el encuadre del mercado, y eso es una linea."),
    (910, "D", "", "La evaluacion de industria nombra el VoC en una linea y B lo despliega en procedimiento."),
    (911, "D", "", "Obtener el compromiso contra el riesgo de las tecnicas de cierre. B despliega una linea de A."),
    (912, "D", "", "La revision de pivotar o seguir contra el modelo entero de customer development."),
    (973, "D", "", "Investigar datos nombra en su ultimo paso el uso personalizado, y B lo despliega."),
    (974, "D", "", "DSO y DPO contra la gestion de cuentas por cobrar: reserva de incobrables y cobranza contra la aritmetica de los dos ratios."),
    (975, "D", "", "Filosofia de validacion de clientes contra el ajuste problema solucion."),
    (976, "A", "QUEMADO", "Familia de la junta asesora con REGLA PROPIA ya fijada, que manda sobre la vara general. QUEMADO: el acta 196 publica su clase y su razon."),
    (979, "D", "", "Fundamentos del design thinking contra identificar pensadores de diseno internos."),
    (980, "D", "", "Fase admit contra fase assess: dos FASES distintas de la misma serie, y por la regla de familia eso es sano."),
    (981, "D", "", "Catalogo de tecnicas de MVP contra las posibilidades de prototipado."),
    (982, "D", "", "Arquetipos de cliente contra el perfil de jobs, pains y gains."),
    (1070, "D", "", "Hipotesis de segmentos de cliente contra el ajuste producto mercado."),
    (1071, "D", "", "Duos contra trios frente a la relacion previa del equipo fundador."),
    (1072, "D", "", "La busqueda del CEO externo nombra el rol futuro del fundador en una linea y B despliega la transicion."),
    (1073, "D", "", "Salir del edificio contra preparar la lista y la agenda de contactos."),
    (1206, "D", "", "Relacion continua con el cliente contra el riesgo de las tecnicas de cierre. Comparten una linea."),
    (1207, "D", "", "Abandonar el plan de negocio contra romper la vision en experimentos concretos."),
    (1212, "D", "", "Compromiso con linea de tiempo contra la obtencion del compromiso dentro de la reunion."),
    (1213, "D", "", "Autofinanciarse o no contra las fuentes de financiamiento: runway y control contra estructura fiscal y terminos."),
    (1372, "D", "", "Garantias implicitas contra expresas frente a la prohibicion de venta atada."),
    (1373, "D", "", "Cuentas por cobrar contra tipos de pasivos."),
    (1374, "D", "", "Calculo del cash burn contra la validacion de la hipotesis de ingresos con LTV."),
    (1379, "D", "", "Actitud de experimentacion contra transformacion organizacional por diseno."),
    (1807, "D", "", "Ids casi sinonimos y por 9.6.3 no deciden: A conserva broker, tarifa fija y venta de excedente, y B conserva mix, instalacion en sitio y RECs."),
    (1808, "D", "DISCUTIBLE", "Ids sinonimos. Fuera del solape del reconocimiento, A conserva programas por nivel y canales de ideas, y B conserva el ejemplo propio, las competencias internas y la senaletica."),
    (1809, "D", "DISCUTIBLE", "Critica a la ecoeficiencia contra menos malo frente a bueno: A conserva toxinas, incineracion y rediseno regenerativo, y B conserva el lenguaje y la presentacion a stakeholders."),
    (1810, "D", "DISCUTIBLE", "Capacidad de empleados contra inversion en capacitacion: A conserva treasure hunts e induccion, B conserva roles de material toxico y Eco Advantage."),
    (1818, "A", "", "El paso 5 de A y el paso 3 de B son la misma frase. Los tres pasos de B estan dentro de los cinco de A y B no anade procedimiento."),
    (1819, "D", "", "Empaque ecoeficiente contra transporte de bajas emisiones."),
    (1820, "D", "", "Benchmarking de practicas contra evaluacion de materialidad con los nueve factores."),
    (1821, "D", "DISCUTIBLE", "El concepto cradle to cradle produce una decision escrita en una frase; la ecoefectividad produce el rediseno entero. Procedimiento corto pero propio a los dos lados."),
    (2031, "D", "", "El certificado de origen es UN documento; B es la documentacion de exportacion entera y lo nombra en una linea."),
    (2032, "D", "", "El metodo paso a paso de investigacion de mercado contra la lista de fuentes."),
    (2033, "D", "", "Convenio de Paris contra PCT: dos tratados distintos."),
    (2034, "D", "", "Carta de credito contra letra de cambio: dos instrumentos distintos."),
    (2158, "D", "", "Leyes estatales de franquicia contra revision legal del marketing."),
    (2159, "D", "", "Crecimiento desde franquiciados actuales contra velocidad de expansion."),
    (2160, "D", "", "Mercados secundarios contra rentabilidad del franquiciante."),
    (2161, "D", "DISCUTIBLE", "B nombra en su paso 3 el capital necesario sin depender de los fees, y A lo despliega con fuente de capital y validacion experta. Madre e hijo con direccion."),
    (2427, "D", "", "Ids casi identicos y por 9.6.3 no deciden: A conserva capex contra opex, muestreo y prueba de robustez, y B conserva la cadena entera de estimacion y los benchmarks."),
    (2428, "D", "QUEMADO", "Uno genera caracteristicas y el otro las elige y prioriza: arista que falta, con direccion. QUEMADO: el acta 196 publica su clase y su razon."),
    (2429, "A", "DISCUTIBLE", "Los dos primeros pasos son los mismos y el ultimo tambien. Fuera del solape A solo conserva comparar las dos listas, que es una linea, y B conserva las categorias de seriedad y el piloto."),
    (2430, "A", "DISCUTIBLE", "Mapear, eliminar lo que no agrega valor y el sistema pull estan a los dos lados. Fuera quedan lineas: las ocho categorias e involucrar gente contra definir valor, takt time y controles."),
    (2661, "D", "", "Calificar al comprador contra calificar al proveedor: sujetos distintos."),
    (2662, "A", "QUEMADO E INALCANZABLE", "A ciegas los dos son la misma constitucion del consejo de calidad. INALCANZABLE por el hallazgo 5.3 del acta 196: la clase se apoya en una fusion planeada y NO aplicada, y la ciega ensena los pasos del nodo viejo."),
    (2663, "A", "", "Los seis pasos de A estan dentro de los once de B, tres de ellos palabra por palabra."),
    (2664, "A", "", "Los seis pasos de B son seis de los siete de A, casi frase por frase. A solo conserva el equipo con project owner."),
    (2837, "D", "", "Reuniones de accion correctiva contra el formulario de eliminacion de causas de error."),
    (2838, "A", "", "Los cinco pasos de A estan dentro de los ocho de B, tres de ellos como parentesis literales. A no anade procedimiento."),
    (2839, "D", "", "Benchmarking de mejores practicas contra el monitoreo continuo ano contra ano."),
    (2840, "D", "", "Aprobacion de la alta direccion contra los inhibidores del breakthrough."),
    (2914, "D", "", "Auditoria de calidad contra auditoria de negocio: alcances y procedimientos distintos."),
    (2915, "D", "", "La escalera diaria, semanal y mensual contra la clasificacion esporadico frente a cronico."),
    (2916, "D", "DISCUTIBLE", "El consejo de once pasos contra el de cuatro. B conserva institucionalizarlo como estructura permanente y coordinar la repeticion del ciclo."),
    (2917, "D", "DISCUTIBLE", "Dos pasos de B citan a A palabra por palabra, pero A conserva puntos de consumo y niveles de reposicion, y B conserva push contra pull, cuellos de botella y tiempo de entrega."),
    (3071, "D", "", "Auditorias de vigilancia de la certificacion contra el concepto de auditoria de calidad."),
    (3072, "D", "DISCUTIBLE", "El consejo de calidad contra el papel de la alta direccion. A conserva Pareto, proyectos, carta y vinculo de consejos; B conserva estrategias, participacion personal en cronicos y reconocimiento."),
    (3073, "D", "", "El consejo de calidad contra el equipo de mejora: dos cuerpos distintos."),
    (3074, "D", "", "Metas SMART de proyecto contra metas de calidad validadas con benchmarks."),
    (3090, "D", "", "Definir la calidad como aptitud de uso contra contrastarla con la conformidad interna."),
    (3091, "D", "", "Las quejas llegan tarde contra el sistema de manejo de quejas."),
    (3092, "D", "", "Boxplot contra histograma: dos graficos distintos."),
    (3093, "D", "", "Diagnostico antes del remedio contra responsabilidad personal en la gestion."),
    (3172, "D", "", "A establece la mejora como politica en una linea y B despliega como se redacta, se publica y se sigue."),
    (3173, "D", "QUEMADO", "Los dos enumeran la triada del autocontrol, y cada lado conserva su especializacion propia. QUEMADO: el acta 196 publica su clase."),
    (3174, "D", "", "Eliminar lemas contra remover barreras: dos puntos distintos de la misma serie, y comparten una sola linea."),
    (3180, "D", "", "Auditoria del producto propio contra encuesta de calidad al proveedor."),
    (3186, "D", "", "El proceso de benchmarking nombra la brecha en una linea y B despliega bruta, neta y vital few."),
    (3187, "D", "", "Concepto de auditoria contra la separacion entre aseguramiento y control."),
    (3188, "D", "", "La escalera de accion correctiva contra el ciclo PDCA de control."),
    (3189, "D", "", "Costo de calidad contra medicion de calidad con graficos de tendencia."),
    (3330, "D", "", "El riesgo cambia con el tiempo contra el riesgo se administra siempre."),
    (3331, "D", "", "Revisar la lista de riesgos contra nombrar las suposiciones fragiles."),
    (3332, "D", "", "El colchon de reserva contra el plan B preparado de antemano."),
    (3333, "D", "", "El riesgo del entorno que no controlas contra que hacer con un riesgo nuevo."),
]


def sha_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    datos = io.open(p, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest())


def puestos_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    t = io.open(p, encoding="utf-8", errors="replace").read()
    return sorted(set(int(x) for x in
                      re.findall(r"puesto_intra[^0-9]{0,12}(\d+)", t)))


def doble_de_la_sellada():
    p = os.path.join(RAIZ, SELLADA_DEL_DOBLE.replace("/", os.sep))
    for l in io.open(p, encoding="utf-8", errors="replace"):
        if l.strip().startswith("EL DOBLE"):
            return sorted(int(x) for x in re.findall(r"\d+", l.split(":", 1)[1]))
    return []


def reparto(clases):
    """EL REPARTO POR CLASE DE UNA LISTA DE PARES (puesto, clase). PURA."""
    r = {"A": 0, "B": 0, "C": 0, "D": 0}
    for _p, c in clases:
        r[c] = r.get(c, 0) + 1
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cotejar", action="store_true",
                    help="ABRE EL DESTAPE y publica el cotejo")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append

    mias = dict((p, (c, m, r)) for p, c, m, r in CLASES)
    universo = puestos_de(CIEGA)
    doble = doble_de_la_sellada()
    tramo = [p for p in universo if p not in set(doble)]

    w("=" * 78)
    w("VUELTA 196, TAREA 2: MIS CLASES SOBRE LOS 120, Y SU COTEJO")
    w("=" * 78)
    w("")
    w("A) EL SUJETO Y LA COBERTURA, CONTADOS Y NO TECLEADOS")
    m = sha_de(CIEGA)
    w("   %s -> disco %d bytes | LF %d | sha256 LF %s" % (CIEGA, m[0], m[1], m[2][:16]))
    w("   CIFRA puestos de la ciega: %d" % len(universo))
    w("   CIFRA puestos del DOBLE, leidos de la sellada del auditor: %d" % len(doble))
    w("   CIFRA puestos del TRAMO, por diferencia: %d" % len(tramo))
    w("   CIFRA clases que yo escribi: %d" % len(mias))
    faltan = [p for p in universo if p not in mias]
    sobran = [p for p in mias if p not in set(universo)]
    w("   CIFRA puestos SIN clase mia: %d %s"
      % (len(faltan), ", ".join(str(x) for x in faltan)))
    w("   CIFRA clases mias que no estan en el sujeto: %d %s"
      % (len(sobran), ", ".join(str(x) for x in sobran)))
    if faltan or sobran:
        w("   PARADA: la cobertura no es exacta. No se coteja una lista coja.")
        print(NL.join(L))
        return 1
    w("")

    w("B) MI REPARTO, ANTES DE ABRIR NADA")
    r_todos = reparto([(p, mias[p][0]) for p in universo])
    r_tramo = reparto([(p, mias[p][0]) for p in tramo])
    r_doble = reparto([(p, mias[p][0]) for p in doble])
    w("   sobre los 120: A %d, B %d, C %d, D %d"
      % (r_todos["A"], r_todos["B"], r_todos["C"], r_todos["D"]))
    w("   sobre el TRAMO (60): A %d, B %d, C %d, D %d"
      % (r_tramo["A"], r_tramo["B"], r_tramo["C"], r_tramo["D"]))
    w("   sobre el DOBLE (60): A %d, B %d, C %d, D %d"
      % (r_doble["A"], r_doble["B"], r_doble["C"], r_doble["D"]))
    w("   LA `B` NI SE SALTA NI SE SOBRE EMITE: emito %d sobre 120, y el archivo"
      % r_todos["B"])
    w("   entero lleva 72 sobre 3388, que es el 2,1 por ciento. Sobre 120 eso son")
    w("   2,5 esperadas.")
    w("")

    w("C) LA CONTAMINACION, DECLARADA Y MEDIDA ANTES DEL COTEJO")
    w("   LOS SEIS QUEMADOS, importados de la sellada del sujeto y no retecleados:")
    for k in sorted(QUEMADOS):
        w("      %-5d %s" % (k, QUEMADOS[k][:96]))
    w("   Y LA GRANDE, QUE NO ES LA DE LOS SEIS: %s" % SEDE_DEL_FILTRADO)
    w("   `A %d, B %d, C %d, D %d` sobre los 60 del TRAMO."
      % (REPARTO_FILTRADO["A"], REPARTO_FILTRADO["B"], REPARTO_FILTRADO["C"],
         REPARTO_FILTRADO["D"]))
    w("   MI REPARTO SOBRE EL TRAMO ES `A %d, B %d, C %d, D %d`."
      % (r_tramo["A"], r_tramo["B"], r_tramo["C"], r_tramo["D"]))
    calza = (r_tramo["A"] == REPARTO_FILTRADO["A"]
             and r_tramo["B"] == REPARTO_FILTRADO["B"]
             and r_tramo["C"] == REPARTO_FILTRADO["C"]
             and r_tramo["D"] == REPARTO_FILTRADO["D"])
    w("   COINCIDE CON EL FILTRADO: %s" % ("SI" if calza else "NO"))
    w("   NO RECLAMO CEGUERA SOBRE EL TRAMO, Y ESA ES LA DECLARACION: ese reparto lo")
    w("   LEI en la TAREA 1 de esta misma vuelta, que es BLOQUEANTE y obliga a")
    w("   leer el acta entera. La unica mitad que se puede llamar ciega de verdad")
    w("   es el DOBLE, y por eso su cotejo se publica aparte.")
    w("")

    if not a.cotejar:
        w("D) MIS CLASES, UNA POR UNA (el destape NO se ha abierto)")
        for p in universo:
            c, mk, rz = mias[p]
            w("   %-5d %s %-24s %s" % (p, c, mk, rz[:150]))
        w("")
        w("FIN. El cotejo se corre despues, con --cotejar.")
        texto = NL.join(L) + NL
        ruta = os.path.join(LOOP, "SALIDA_V196_T2_MIS_CLASES.txt")
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
        print(texto)
        print("ESCRITO: %s (%d bytes)" % (ruta, len(texto.encode("utf-8"))))
        return 0

    w("D) EL DESTAPE, ABIERTO AHORA Y NO ANTES")
    d = sha_de(DESTAPE)
    w("   %s -> disco %d bytes | LF %d | sha256 LF %s"
      % (DESTAPE, d[0], d[1], d[2][:16]))
    filas = [json.loads(l) for l in
             io.open(os.path.join(RAIZ, ARCHIVO.replace("/", os.sep)),
                     encoding="utf-8") if l.strip()]
    del_archivo = dict((int(f["puesto_intra"]), f) for f in filas)
    w("   CIFRA filas del archivo: %d" % len(filas))
    w("")

    w("E) EL COTEJO, PUESTO POR PUESTO")
    coinciden, discrepan = [], []
    for p in universo:
        c, mk, rz = mias[p]
        real = del_archivo[p]["clase"]
        ok = c == real
        (coinciden if ok else discrepan).append(p)
        w("   %-5d mia %s | archivo %s | %-9s %-24s"
          % (p, c, real, "CALZA" if ok else "DISCREPA", mk))
        if not ok:
            w("         mi razon:      %s" % rz[:140])
            w("         razon del archivo: %s"
              % del_archivo[p].get("razon", "")[:190])
    w("")

    w("F) LAS CIFRAS DEL COTEJO, POR LAS TRES VARAS")
    quemados = sorted(set(QUEMADOS) & set(universo))
    limpios = [p for p in universo if p not in set(quemados)]
    marcados = set(p for p, _c, mk, _r in CLASES if "DISCUTIBLE" in mk)
    for etiqueta, grupo in (("los 120 enteros", universo),
                            ("los %d sin quemados" % len(limpios), limpios),
                            ("el DOBLE, la unica mitad ciega de verdad", doble),
                            ("el TRAMO, con el reparto filtrado", tramo)):
        g = set(grupo)
        ok = len([p for p in coinciden if p in g])
        no = len([p for p in discrepan if p in g])
        w("   %-46s %3d de %3d coinciden, %2d discrepan"
          % (etiqueta, ok, len(g), no))
    w("")
    dentro = [p for p in discrepan if p in marcados]
    fuera = [p for p in discrepan if p not in marcados]
    w("   CIFRA discutibles que marque ANTES de saber: %d" % len(marcados))
    w("   CIFRA discrepancias DENTRO de mi marcado: %d -> %s"
      % (len(dentro), ", ".join(str(x) for x in dentro) or "(ninguna)"))
    w("   CIFRA discrepancias FUERA de mi marcado: %d -> %s"
      % (len(fuera), ", ".join(str(x) for x in fuera) or "(ninguna)"))
    fuera_limpios = [p for p in fuera if p not in set(quemados)]
    w("   CIFRA discrepancias FUERA del marcado Y NO QUEMADAS: %d -> %s"
      % (len(fuera_limpios), ", ".join(str(x) for x in fuera_limpios) or "(ninguna)"))
    w("   ESA ES LA QUE DISPARA AUDITOR.md 1.2 sobre mi propia tanda.")
    w("")

    w("G) EL REPARTO REAL DEL ARCHIVO, CONTADO Y NO SUPUESTO")
    r_arch_todos = reparto([(p, del_archivo[p]["clase"]) for p in universo])
    r_arch_tramo = reparto([(p, del_archivo[p]["clase"]) for p in tramo])
    r_arch_doble = reparto([(p, del_archivo[p]["clase"]) for p in doble])
    w("   sobre los 120: A %d, B %d, C %d, D %d"
      % (r_arch_todos["A"], r_arch_todos["B"], r_arch_todos["C"], r_arch_todos["D"]))
    w("   sobre el TRAMO: A %d, B %d, C %d, D %d"
      % (r_arch_tramo["A"], r_arch_tramo["B"], r_arch_tramo["C"], r_arch_tramo["D"]))
    w("   sobre el DOBLE: A %d, B %d, C %d, D %d"
      % (r_arch_doble["A"], r_arch_doble["B"], r_arch_doble["C"], r_arch_doble["D"]))
    w("   EL FILTRADO DEL ACTA DECIA `A %d, B %d, C %d, D %d` sobre el tramo, y el"
      % (REPARTO_FILTRADO["A"], REPARTO_FILTRADO["B"], REPARTO_FILTRADO["C"],
         REPARTO_FILTRADO["D"]))
    w("   archivo contado hoy da lo de arriba.")
    w("")

    w("H) EL ARCHIVO NO SE MOVIO")
    ar = sha_de(ARCHIVO)
    w("   %s -> disco %d bytes | LF %d | sha256 LF %s"
      % (ARCHIVO, ar[0], ar[1], ar[2][:16]))
    w("")
    w("FIN DEL COTEJO")

    texto = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V196_T2_COTEJO.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(texto.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
