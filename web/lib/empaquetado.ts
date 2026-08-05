/**
 * empaquetado.ts — Scheduler Inteligente, Fase 2: EL CORAZÓN.
 *
 * PURO y determinístico (cero LLM, cero red, cero reloj): dadas las tareas con
 * su banda de esfuerzo (F1) y la capacidad semanal REAL del usuario para ese
 * espacio, reparte las semanas y devuelve una fecha por tarea.
 *
 * Por qué existe: el sugeridor viejo (fechasBase.ts) reparte por ETAPA sin mirar
 * el trabajo que hay dentro — etapa N cae a la semana N, tenga esa etapa una
 * tarea de una hora o cinco de dos días. Prometía calendarios que nadie podía
 * cumplir. Este módulo llena semanas contra la capacidad declarada; el sugeridor
 * viejo NO muere: es el fallback cuando no hay bandas (ver `hayBandas`).
 *
 * LAS REGLAS (las del fundador, sin adornos):
 *  - Las ETAPAS son PUERTAS: la etapa N+1 arranca en la semana SIGUIENTE a la
 *    última que ocupó la N. No se solapan y no comparten semana de entrega: una
 *    etapa es un compromiso cerrado antes de abrir el siguiente.
 *  - Dentro de una etapa, las semanas se LLENAN contra la capacidad: la tarea
 *    que no cabe en lo que queda de la semana termina en la siguiente (desborde).
 *  - La entrega de cada tarea cae en el día dominante (viernes por defecto, o el
 *    día en que el usuario suele cerrar) de SU semana empaquetada.
 *  - La DESTACADA ("Esta semana") es el arranque de su etapa: se empaqueta
 *    primero y entrega el LUNES de la primera semana de la etapa.
 *  - La tarea con ESPERA EXTERNA (F3) se dispara temprano y entrega tarde: su
 *    inicio se fija en el lunes de la primera semana de su etapa y su entrega
 *    lleva el colchón de LEAD_ESPERA_SEMANAS. La espera NO consume capacidad:
 *    el tiempo de terceros no es tiempo del usuario, así que no empuja a las
 *    tareas hermanas; solo corre su propio reloj de entrega.
 */
import { fechaInputLocal } from "./fechas";
import type { Banda, CapacidadSemanal } from "./dbContract";
import type { FechaSugerida } from "./fechasBase";

/**
 * Horas de trabajo que representa cada banda. Son las MEDIAS de los rangos que
 * el modelo estima y que el usuario ve en el detalle (S ≈ una sentada de una
 * hora; M = 2-4 h; L = una jornada; XL = varios días). Se usan SOLO para
 * repartir semanas: nunca se le muestran al usuario como "tu tarea son 3 horas".
 */
export const HORAS_MEDIA: Record<Banda, number> = {
  S: 1, // una sentada de una hora o menos
  M: 3, // el centro de "dos a cuatro horas"
  L: 8, // una jornada completa de trabajo
  XL: 16, // varios días (dos jornadas de trabajo efectivo)
};

/**
 * Horas por semana con las que se PLANIFICA cada chip de capacidad: el PISO del
 * rango que el usuario eligió, no su centro. Es deliberado y es el mismo criterio
 * conservador de la mayoría-de-3 (el empate sube de banda): planificar con el
 * piso hace que a quien le sobre tiempo vaya adelantado, en vez de prometerle un
 * calendario que su semana floja no aguanta. Se le puede decir en una frase:
 * "planeo con las 5 horas que me diste; si te sobran, ganas tiempo".
 */
export const HORAS_POR_SEMANA: Record<CapacidadSemanal, number> = {
  "2-5": 2,
  "5-10": 5,
  "10-20": 10,
  "20+": 20,
};

/** El chip por defecto del ritual cuando el usuario aún no ha declarado nada. */
export const CAPACIDAD_DEFAULT: CapacidadSemanal = "5-10";

/**
 * El colchón, en semanas, que se le da a una tarea que depende de terceros.
 *
 * Por qué UNA y no dos ni media: es el ciclo de respuesta más común de lo que el
 * plan pide de fuera (un correo a un proveedor, una cotización, una cita, un
 * permiso que alguien tiene que mirar). Una semana es el mínimo honesto que
 * cambia el calendario sin inflarlo: dos empujarían un plan entero por tareas
 * que muchas veces se resuelven en tres días, y media semana no sobrevive a un
 * fin de semana. Si la beta muestra que el colchón se queda corto, esta
 * constante es la palanca, y se mueve con datos (los completed_at reales de las
 * tareas con espera), no por intuición.
 */
export const LEAD_ESPERA_SEMANAS = 1;

const VIERNES = 5;
const LUNES = 1;

export interface ItemEmpaquetable {
  id: string;
  etapa: number;
  destacado: boolean;
  banda: Banda | null;
  /** F3 usará esto para el colchón de espera; F2 lo recibe y no lo aplica. */
  espera_externa?: boolean | null;
}

/** ¿Se puede empaquetar? Solo si TODAS las tareas traen banda. Con una sola sin
 * estimar, el plan entero cae al sugeridor viejo: media planificación repartida
 * por capacidad y media por etapa sería un calendario mentiroso. */
export function hayBandas(items: ItemEmpaquetable[]): boolean {
  return items.length > 0 && items.every((i) => i.banda !== null && i.banda !== undefined);
}

/** La fecha del `weekday` (0=Dom..6=Sáb) dentro de la semana ISO que cae
 * `semanas` después de `base`. Copia deliberada de fechasBase.objetivoEnSemana:
 * los dos módulos tienen que caer en el MISMO día para que el fallback y el
 * empaquetado sean intercambiables sin saltos de un día. */
function diaDeSemana(base: Date, semanas: number, weekday: number): Date {
  const anchor = new Date(base.getFullYear(), base.getMonth(), base.getDate() + semanas * 7, 12);
  const desdeLunes = (anchor.getDay() + 6) % 7;
  const lunes = new Date(anchor.getFullYear(), anchor.getMonth(), anchor.getDate() - desdeLunes, 12);
  const offset = (weekday + 6) % 7;
  return new Date(lunes.getFullYear(), lunes.getMonth(), lunes.getDate() + offset, 12);
}

export interface ItemEmpaquetado extends FechaSugerida {
  /** Semana (0 = la del ancla) en la que esta tarea TERMINA. Para el Gantt y
   * para poder asertar el reparto sin leer fechas. */
  semana: number;
  etapa: number;
  /** F3: SOLO en las tareas con espera externa — el día en que conviene
   * dispararla (el lunes de la primera semana de su etapa). No se persiste: es
   * un dato derivable que la pantalla usa para decir "empiézala temprano". En
   * las demás tareas no existe, porque inventarles un inicio sería precisión
   * fabricada: su fecha ya es su compromiso. */
  inicioTemprano?: string;
}

export interface ResultadoEmpaquetado {
  fechas: ItemEmpaquetado[];
  /** Cuántas semanas ocupa el plan completo (la última semana usada + 1). */
  semanasTotales: number;
}

/**
 * Empaqueta las tareas contra la capacidad y devuelve una fecha por tarea.
 *
 * El reparto dentro de una etapa se hace por HORAS ACUMULADAS: una tarea termina
 * en la semana donde su hora final cae. Así una tarea más grande que una semana
 * entera (una XL de 16 h con capacidad de 5 h) simplemente ocupa las semanas que
 * necesita y entrega en la última, sin ningún caso especial.
 */
export function empaquetarFechas(opts: {
  /** El ancla: normalmente plan.created_at (la semana 0 es la suya). */
  ancla: string;
  items: ItemEmpaquetable[];
  capacidad: CapacidadSemanal;
  /** Día en que el usuario suele cerrar (0=Dom..6=Sáb). null → viernes. */
  diaPreferido?: number | null;
}): ResultadoEmpaquetado {
  const base = new Date(opts.ancla);
  const capacidad = HORAS_POR_SEMANA[opts.capacidad];
  const diaEntrega = opts.diaPreferido ?? VIERNES;

  // Etapas en orden; dentro de cada una, la destacada primero (es el arranque).
  const porEtapa = new Map<number, ItemEmpaquetable[]>();
  for (const it of opts.items) {
    if (!porEtapa.has(it.etapa)) porEtapa.set(it.etapa, []);
    porEtapa.get(it.etapa)!.push(it);
  }
  const etapas = [...porEtapa.keys()].sort((a, b) => a - b);

  const fechas: ItemEmpaquetado[] = [];
  // La primera etapa arranca en la semana SIGUIENTE a la del ancla, igual que el
  // sugeridor viejo. No es adorno: si arrancara en la semana 0, el lunes de la
  // destacada caería en el PASADO cada vez que un plan nace a media semana, y
  // ninguna fecha del ritual puede nacer vencida.
  let semanaInicioEtapa = 1;

  for (const etapa of etapas) {
    const items = porEtapa.get(etapa)!;
    // Orden estable: las destacadas al frente, el resto como venían del plan.
    const ordenados = [...items.filter((i) => i.destacado), ...items.filter((i) => !i.destacado)];

    let horasAcumuladas = 0;
    let ultimaSemanaEtapa = 0; // relativa al inicio de la etapa

    for (const it of ordenados) {
      const espera = it.espera_externa === true;
      // La semana (dentro de la etapa) donde caería la hora final de esta tarea
      // con la capacidad gastada hasta aquí.
      const semanaTrabajo = Math.ceil((horasAcumuladas + HORAS_MEDIA[it.banda as Banda]) / capacidad) - 1;
      // F3: la espera NO consume la capacidad del usuario. Su trabajo propio es
      // disparar y esperar; cargar esas horas contra la semana empujaría a las
      // tareas hermanas por tiempo que el usuario no está gastando.
      if (!espera) horasAcumuladas += HORAS_MEDIA[it.banda as Banda];

      // La destacada entrega el LUNES de la primera semana de su etapa; el resto,
      // el día de cierre de la semana en que terminan. La espera suma su colchón
      // a la semana de entrega, sin cambiar el día.
      const semanaBase = it.destacado ? 0 : semanaTrabajo;
      const semanaEntrega = semanaBase + (espera ? LEAD_ESPERA_SEMANAS : 0);
      const semana = semanaInicioEtapa + semanaEntrega;
      const weekday = it.destacado ? LUNES : diaEntrega;

      // La etapa cierra cuando cierra su tarea más tardía DE VERDAD: cuenta la
      // entrega con colchón, no solo el reparto de horas. Así la puerta de la
      // etapa siguiente respeta la espera en vez de abrir sobre ella.
      if (semanaTrabajo > ultimaSemanaEtapa) ultimaSemanaEtapa = semanaTrabajo;
      if (semanaEntrega > ultimaSemanaEtapa) ultimaSemanaEtapa = semanaEntrega;

      fechas.push({
        id: it.id,
        fecha: fechaInputLocal(diaDeSemana(base, semana, weekday)),
        semana,
        etapa,
        // Dispararla pronto es lo único que el usuario controla de una espera.
        ...(espera
          ? { inicioTemprano: fechaInputLocal(diaDeSemana(base, semanaInicioEtapa, LUNES)) }
          : {}),
      });
    }

    // Puerta: la etapa siguiente arranca en la semana DESPUÉS de la última que
    // ocupó esta. Ninguna tarea de la N+1 entrega la misma semana que la última
    // de la N.
    semanaInicioEtapa = semanaInicioEtapa + ultimaSemanaEtapa + 1;
  }

  // Se devuelve en el orden de entrada (el del plan), no en el de empaquetado:
  // el llamador indexa por id, pero un orden estable evita sorpresas al pintar.
  const porId = new Map(fechas.map((f) => [f.id, f]));
  const enOrden = opts.items.map((i) => porId.get(i.id)!).filter(Boolean);
  const semanasTotales = fechas.reduce((max, f) => Math.max(max, f.semana), 0) + 1;
  return { fechas: enOrden, semanasTotales };
}
