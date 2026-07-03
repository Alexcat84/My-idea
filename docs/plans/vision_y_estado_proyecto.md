# Visión del Proyecto y Estado Actual: "La Telaraña del Emprendedor"

## 1. El Origen de la Idea
La idea de esta aplicación nace de una premisa simple pero inmensamente potente: **Cualquier persona puede tener una gran idea en un instante, pero la inmensa mayoría fracasa porque no conoce el camino correcto a seguir.** 

La visión consiste en democratizar el conocimiento de las metodologías empresariales, de diseño y de gestión de proyectos más avanzadas del mundo, pero escondiendo su complejidad académica detrás de una interfaz conversacional extremadamente simple. El resultado final debe ser un plan de acción paso a paso, entregado en lenguaje natural, tan fácil de entender como un "algoritmo para hacer café".

## 2. Objetivo Claro de la Aplicación
**Objetivo Principal:** Convertir cualquier idea cruda y genérica en un proyecto hiper-estructurado y accionable. 

Para lograr esto, el sistema actúa como un mentor invisible que:
1. **Evalúa el estado mental del creador:** Pasa la idea por un filtro cognitivo inicial para saber en qué etapa del proceso de pensamiento se encuentra.
2. **Navega por una telaraña de decisiones:** Hace preguntas clave al usuario, donde cada respuesta sirve como una "llave" que abre puertas hacia nuevos nodos de conocimiento en un grafo interactivo.
3. **Ensambla un plan infalible:** Recopila todos los pasos accionables de los nodos visitados y los traduce a un plan de ejecución simple, secuencial y en lenguaje natural.

## 3. Lo que ya se ha construido (El Trabajo de Claude 3.5 Sonnet)
En las fases iniciales del proyecto, la API de Claude (versión 3.5 Sonnet) realizó el trabajo pesado de **Ingeniería del Conocimiento**. 

### 3.1. Extracción y Fragmentación
Claude analizó una biblioteca de libros de texto densos y extrajo los conceptos clave para convertirlos en **nodos de datos** individuales. 
- Se crearon cientos de archivos JSON en el directorio `dataset/nodos/`.
- Cada nodo cuenta con un resumen, una lista de pasos accionables, criterios de activación, y enlaces teóricos hacia nodos previos y siguientes.

### 3.2. Scripts de Procesamiento
Se dejaron listos los motores de fragmentación y estructuración en la carpeta `scripts/` (ej. `chunker.py`, `generate_index.py`, `pipeline.py`). Estos scripts permitieron que la IA procesara la literatura y generara la telaraña en crudo.

## 4. Referencias Bibliográficas (Base de Conocimiento)
El corpus de conocimiento que alimenta la telaraña está construido sobre los siguientes textos, listados en formato APA 7:

Brown, T. (2009). *Change by design: How design thinking transforms organizations and inspires innovation*. Harper Business.

Carter, C., & Doorley, S. (2024). *Assembling tomorrow: A guide to designing a thriving future*. Ten Speed Press.

Osterwalder, A., & Pigneur, Y. (2010). *Business model generation: A handbook for visionaries, game changers, and challengers*. John Wiley & Sons.

Project Management Institute. (2017). *A project manager's book of forms* (3rd ed.). Project Management Institute.

Ries, E. (2011). *The lean startup: How today's entrepreneurs use continuous innovation to create radically successful businesses*. Crown Business.

Wallas, G. (1926). *The art of thought*. Harcourt, Brace and Company.

---

## 5. Próximos Pasos
La base de datos (el cerebro) ya existe, pero aún debe ser saneada, y la interfaz (el cuerpo) debe ser construida.

El siguiente paso inmediato es ejecutar la **Fase 1**, detallada en nuestro [Plan de Implementación](file:///C:/Users/AlexDesk/Documents/I%20have%20an%20idea/docs/plans/implementation_plan.md). Esto implica crear el script `fix_spiderweb.py` para curar la base de datos de nodos, eliminar enlaces rotos y generar el grafo maestro que permitirá a la aplicación navegar de puerta en puerta de forma fluida.
