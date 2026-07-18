/**
 * calculadora.ts - Fase 3.0: port TypeScript de engine/calculadora.py
 * (Motor v2.1/v2.2). CERO llamadas a LLM: funciones puras sobre
 * numeros_proyecto. Cada formula conserva en su comentario el node_id
 * del grafo del que sale (o una nota explicita si aun no tiene nodo
 * dedicado), igual que el original en Python.
 *
 * PARIDAD NUMERICA OBLIGATORIA (prompt Fase 3.0): este archivo debe
 * calcular EXACTAMENTE lo mismo que engine/calculadora.py para los
 * mismos numeros_proyecto de entrada. Ver calculadora.test.ts para los
 * 3 casos canonicos (macetas, digital del fundador, SaaS sintetico) con
 * los mismos valores calculados a mano que engine/test_calculadora.py.
 *
 * Manejo de rangos: si el usuario dio un rango para un campo
 * (numeros_proyecto[campo].valor = {min, max}), el resultado tambien
 * sale como rango, calculado con el emparejamiento de intervalos
 * correcto por operacion (suma/resta cambian que lado es el "peor
 * caso"), no con un min-con-min ingenuo en todos los casos.
 *
 * Nota de redondeo: Python round() usa "banker's rounding" (redondeo al
 * par mas cercano) en el raro caso de un empate exacto en .5; esta
 * implementacion redondea la mitad lejos de cero (comportamiento
 * estandar de Math.round en JS). Ninguno de los 3 casos canonicos de
 * paridad cae en ese borde exacto -- si algun valor futuro lo hace, es
 * el unico punto de divergencia conocido entre las dos implementaciones.
 */

export type TipoOferta = "producto_fisico" | "servicio" | "digital" | "mixto" | null | undefined;

export type Rango = { min: number; max: number };
export type ValorNumerico = number | Rango;

export interface CampoNumero {
  valor: ValorNumerico | null;
  unidad?: string | null;
  texto_original?: string | null;
  session_id?: string | null;
  updated_at?: string | null;
}

export type NumerosProyecto = Record<string, CampoNumero>;

export const SEMANAS_POR_MES = 4; // aproximacion deliberada (no 4.33) para numeros redondos y verificables

function _valor(numeros: NumerosProyecto | undefined, campo: string): ValorNumerico | null {
  const entry = (numeros ?? {})[campo];
  if (!entry || entry.valor === null || entry.valor === undefined) return null;
  return entry.valor;
}

function _esRango(v: ValorNumerico | null | undefined): v is Rango {
  return typeof v === "object" && v !== null && "min" in v && "max" in v;
}

function _lado(v: ValorNumerico | null, lado: "min" | "max"): number {
  if (_esRango(v)) return v[lado];
  return v as number;
}

function _hayRango(...vals: (ValorNumerico | null)[]): boolean {
  return vals.some((v) => _esRango(v));
}

function _r(x: number | null, nd = 2): number | null {
  if (x === null) return null;
  const factor = 10 ** nd;
  return Math.round(x * factor) / factor;
}

export interface ResultadoValor {
  valor: ValorNumerico | null;
  insumos_usados: string[];
  insumos_faltantes: string[];
}

/**
 * Costo por unidad = costo_materiales_unidad + horas_por_unidad * valor_hora.
 * Fuente: nodo 'hoja_estimacion_costos' (metodo bottom-up: sumar mano de
 * obra + materiales) y 'margen_bruto' (estructura costo-precio) del grafo.
 *
 * Motor v2.2, rama 'digital': una oferta digital no tiene "horas por
 * unidad" de produccion (no se fabrica una unidad a la vez con trabajo
 * manual) -- el costo unitario es directamente el costo variable por
 * usuario/unidad declarado (costo_materiales_unidad, reusado como alias
 * de "costo variable"), sin exigir horas_por_unidad/valor_hora como
 * insumos faltantes (serian datos que no aplican a este tipo de oferta,
 * no datos que el usuario olvido dar).
 */
export function costoUnitarioTotal(numeros: NumerosProyecto, tipoOferta?: TipoOferta): ResultadoValor {
  const materiales = _valor(numeros, "costo_materiales_unidad");
  if (tipoOferta === "digital") {
    if (materiales === null) {
      return { valor: null, insumos_usados: [], insumos_faltantes: ["costo_materiales_unidad"] };
    }
    return { valor: materiales, insumos_usados: ["costo_materiales_unidad"], insumos_faltantes: [] };
  }
  const horas = _valor(numeros, "horas_por_unidad");
  const valorHora = _valor(numeros, "valor_hora");
  const faltantes = (
    [
      ["costo_materiales_unidad", materiales],
      ["horas_por_unidad", horas],
      ["valor_hora", valorHora],
    ] as const
  )
    .filter(([, v]) => v === null)
    .map(([c]) => c);
  if (faltantes.length) {
    return { valor: null, insumos_usados: [], insumos_faltantes: faltantes };
  }
  let valor: ValorNumerico;
  if (_hayRango(materiales, horas, valorHora)) {
    const lo = _lado(materiales, "min") + _lado(horas, "min") * _lado(valorHora, "min");
    const hi = _lado(materiales, "max") + _lado(horas, "max") * _lado(valorHora, "max");
    valor = { min: _r(lo)!, max: _r(hi)! };
  } else {
    valor = _r((materiales as number) + (horas as number) * (valorHora as number))!;
  }
  return {
    valor,
    insumos_usados: ["costo_materiales_unidad", "horas_por_unidad", "valor_hora"],
    insumos_faltantes: [],
  };
}

export interface ResultadoMargen {
  valor: ValorNumerico | null;
  porcentaje: ValorNumerico | null;
  insumos_usados: string[];
  insumos_faltantes: string[];
}

/**
 * Margen por unidad = precio_tentativo - costo_unitario_total; porcentaje
 * = margen / precio. Fuente: nodo 'margen_bruto' (Gross Profit Margin).
 * Para ofertas digitales, esto es el "margen por usuario" (Motor v2.2) --
 * misma formula, el nombre cambia solo en la narracion, no en el calculo.
 */
export function margenUnitario(numeros: NumerosProyecto, tipoOferta?: TipoOferta): ResultadoMargen {
  const costo = costoUnitarioTotal(numeros, tipoOferta);
  const precio = _valor(numeros, "precio_tentativo");
  const faltantes = [...costo.insumos_faltantes];
  if (precio === null) faltantes.push("precio_tentativo");
  if (faltantes.length) {
    return { valor: null, porcentaje: null, insumos_usados: [], insumos_faltantes: faltantes };
  }
  const costoV = costo.valor as ValorNumerico;
  let margen: ValorNumerico;
  let porcentaje: ValorNumerico | null;
  if (_hayRango(costoV, precio)) {
    // peor caso: precio bajo y costo alto; mejor caso: precio alto y costo bajo
    const lo = _lado(precio, "min") - _lado(costoV, "max");
    const hi = _lado(precio, "max") - _lado(costoV, "min");
    margen = { min: _r(lo)!, max: _r(hi)! };
    const pLo = _lado(precio, "min");
    const pHi = _lado(precio, "max");
    porcentaje = {
      min: pLo ? _r((lo / pLo) * 100, 1)! : (null as unknown as number),
      max: pHi ? _r((hi / pHi) * 100, 1)! : (null as unknown as number),
    };
  } else {
    const precioN = precio as number;
    margen = _r(precioN - (costoV as number))!;
    porcentaje = precioN ? _r((margen / precioN) * 100, 1) : null;
  }
  return {
    valor: margen,
    porcentaje,
    insumos_usados: [...costo.insumos_usados, "precio_tentativo"],
    insumos_faltantes: [],
  };
}

export interface ResultadoEquilibrio {
  valor: number | Rango | null;
  insumos_usados: string[];
  insumos_faltantes: string[];
  nota?: string;
}

/**
 * Unidades/mes para cubrir costos fijos = costos_fijos_mensuales / margen_unitario.
 * Formula de margen de contribucion. Fuente: nodo 'punto_equilibrio_unidades'
 * (dataset v1.2 - antes de esa version, esta formula no tenia nodo propio).
 *
 * Motor v2.2: redondeado hacia ARRIBA (Math.ceil), no al decimal mas
 * cercano -- no se pueden vender fracciones de unidad, y quedarse corto
 * en la unidad de redondeo (ej. 15 en vez de 16 cuando el calculo exacto
 * da 15.38) significa no cubrir los costos fijos ese mes. Verificado
 * contra el caso real que motivo este cambio: $200 fijos / $13 margen =
 * 15.38 -> se necesitan 16 packs, no 15.4.
 */
export function puntoEquilibrioUnidadesMes(numeros: NumerosProyecto, tipoOferta?: TipoOferta): ResultadoEquilibrio {
  const margen = margenUnitario(numeros, tipoOferta);
  const costosFijos = _valor(numeros, "costos_fijos_mensuales");
  const faltantes = [...margen.insumos_faltantes];
  if (costosFijos === null) faltantes.push("costos_fijos_mensuales");
  if (faltantes.length) {
    return { valor: null, insumos_usados: [], insumos_faltantes: faltantes };
  }
  const margenV = margen.valor as ValorNumerico;
  let valor: number | Rango;
  if (_hayRango(margenV, costosFijos)) {
    const mLo = _lado(margenV, "min");
    const mHi = _lado(margenV, "max");
    const cfLo = _lado(costosFijos, "min");
    const cfHi = _lado(costosFijos, "max");
    if (mLo <= 0 || mHi <= 0) {
      return {
        valor: null,
        insumos_usados: [],
        insumos_faltantes: [],
        nota: "el margen por unidad no es positivo en todo el rango; no hay punto de equilibrio posible asi",
      };
    }
    valor = { min: Math.ceil(cfLo / mHi), max: Math.ceil(cfHi / mLo) };
  } else {
    const margenN = margenV as number;
    if (margenN <= 0) {
      return {
        valor: null,
        insumos_usados: [],
        insumos_faltantes: [],
        nota: "el margen por unidad no es positivo; no hay punto de equilibrio posible con estos numeros",
      };
    }
    valor = Math.ceil((costosFijos as number) / margenN);
  }
  return { valor, insumos_usados: [...margen.insumos_usados, "costos_fijos_mensuales"], insumos_faltantes: [] };
}

export interface ResultadoCapacidad {
  unidades_mes: ValorNumerico | null;
  ingreso: ValorNumerico | null;
  margen_mensual: ValorNumerico | null;
  insumos_usados: string[];
  insumos_faltantes: string[];
}

/**
 * Techo de ingreso mensual segun capacidad declarada:
 * unidades_mes = capacidad_semanal * SEMANAS_POR_MES; ingreso = unidades_mes * precio;
 * margen_mensual = unidades_mes * margen_unitario. Sin nodo dedicado (aritmetica
 * directa sobre capacidad_semanal y precio_tentativo, ambos ya declarados por el usuario).
 */
export function techoIngresoCapacidad(numeros: NumerosProyecto): ResultadoCapacidad {
  const capacidad = _valor(numeros, "capacidad_semanal");
  const precio = _valor(numeros, "precio_tentativo");
  const faltantes = (
    [
      ["capacidad_semanal", capacidad],
      ["precio_tentativo", precio],
    ] as const
  )
    .filter(([, v]) => v === null)
    .map(([c]) => c);
  if (faltantes.length) {
    return { unidades_mes: null, ingreso: null, margen_mensual: null, insumos_usados: [], insumos_faltantes: faltantes };
  }
  const margen = margenUnitario(numeros);
  let unidadesMes: ValorNumerico;
  let ingreso: ValorNumerico;
  let margenMensual: ValorNumerico | null;
  if (_hayRango(capacidad, precio) || _esRango(margen.valor)) {
    const capLo = _lado(capacidad, "min");
    const capHi = _lado(capacidad, "max");
    const precioLo = _lado(precio, "min");
    const precioHi = _lado(precio, "max");
    const uLo = _r(capLo * SEMANAS_POR_MES, 1)!;
    const uHi = _r(capHi * SEMANAS_POR_MES, 1)!;
    unidadesMes = { min: uLo, max: uHi };
    ingreso = { min: _r(uLo * precioLo)!, max: _r(uHi * precioHi)! };
    margenMensual = null;
    if (margen.valor !== null) {
      const mLo = _lado(margen.valor, "min");
      const mHi = _lado(margen.valor, "max");
      margenMensual = { min: _r(uLo * mLo)!, max: _r(uHi * mHi)! };
    }
  } else {
    unidadesMes = _r((capacidad as number) * SEMANAS_POR_MES, 1)!;
    ingreso = _r((unidadesMes as number) * (precio as number))!;
    margenMensual = margen.valor !== null ? _r((unidadesMes as number) * (margen.valor as number)) : null;
  }
  return {
    unidades_mes: unidadesMes,
    ingreso,
    margen_mensual: margenMensual,
    insumos_usados: ["capacidad_semanal", "precio_tentativo", ...margen.insumos_usados],
    insumos_faltantes: margen.insumos_faltantes,
  };
}

export interface EscenarioCapacidad {
  unidades_mes: number;
  ingreso: number;
  margen_mensual: number | null;
}

export interface SobredemandaCapacidad {
  demanda_estimada: number;
  unidades_producibles: number;
  unidades_no_atendidas: number;
  ingreso_perdido_estimado: number;
  margen_perdido_estimado: number | null;
}

export interface ResultadoEscenariosCapacidad {
  pesimista: EscenarioCapacidad | null;
  base: EscenarioCapacidad | null;
  sobredemanda: SobredemandaCapacidad | null;
  insumos_usados: string[];
  insumos_faltantes: string[];
}

/**
 * Tres escenarios relativos a la capacidad declarada: pesimista (50% de
 * la capacidad), base (100%, el techo real), y sobredemanda (150% de
 * demanda estimada, mostrando cuanta venta se pierde porque la capacidad
 * de produccion no alcanza). Sin nodo dedicado (deriva de techo_ingreso_capacidad).
 */
export function escenariosCapacidad(numeros: NumerosProyecto): ResultadoEscenariosCapacidad {
  const techo = techoIngresoCapacidad(numeros);
  if (techo.insumos_faltantes.length || techo.unidades_mes === null) {
    return { pesimista: null, base: null, sobredemanda: null, insumos_usados: [], insumos_faltantes: techo.insumos_faltantes };
  }
  let unidadesBase: number;
  let precio: number;
  let margenU: number | null;
  if (_esRango(techo.unidades_mes)) {
    // Con rangos, los escenarios de capacidad se simplifican al punto medio
    // para no explotar en un arbol de combinaciones dificil de leer en el reporte.
    unidadesBase = _r((techo.unidades_mes.min + techo.unidades_mes.max) / 2, 1)!;
    const precioRaw = _valor(numeros, "precio_tentativo");
    precio = _r((_lado(precioRaw, "min") + _lado(precioRaw, "max")) / 2)!;
    let mu = margenUnitario(numeros).valor;
    if (_esRango(mu)) mu = _r((mu.min + mu.max) / 2);
    margenU = mu as number | null;
  } else {
    unidadesBase = techo.unidades_mes as number;
    precio = _valor(numeros, "precio_tentativo") as number;
    margenU = margenUnitario(numeros).valor as number | null;
  }

  const escenario = (factor: number): EscenarioCapacidad => {
    const unidades = _r(unidadesBase * factor, 1)!;
    return {
      unidades_mes: unidades,
      ingreso: _r(unidades * precio)!,
      margen_mensual: margenU !== null ? _r(unidades * margenU) : null,
    };
  };

  const pesimista = escenario(0.5);
  const base = escenario(1.0);
  const demandaEstimada = _r(unidadesBase * 1.5, 1)!;
  const unidadesNoAtendidas = _r(demandaEstimada - unidadesBase, 1)!;
  const sobredemanda: SobredemandaCapacidad = {
    demanda_estimada: demandaEstimada,
    unidades_producibles: unidadesBase,
    unidades_no_atendidas: unidadesNoAtendidas,
    // Hotfix v2.1.1: dos campos con semantica distinta, no uno solo.
    // ingreso_perdido_estimado = ventas que no se facturan (unidades x
    // PRECIO); margen_perdido_estimado = ganancia que no llega (unidades
    // x MARGEN). Antes, "ingreso_perdido_estimado" calculaba con margen
    // por error, subestimando 5x el costo de oportunidad real.
    ingreso_perdido_estimado: _r(unidadesNoAtendidas * precio)!,
    margen_perdido_estimado: margenU !== null ? _r(unidadesNoAtendidas * margenU) : null,
  };
  return { pesimista, base, sobredemanda, insumos_usados: techo.insumos_usados, insumos_faltantes: [] };
}

export interface EscenarioAdopcion {
  unidades: number;
  ingreso: number;
  margen_total: number | null;
}

export interface ResultadoEscenariosAdopcion {
  "50%": EscenarioAdopcion | null;
  "100%": EscenarioAdopcion | null;
  "200%": EscenarioAdopcion | null;
  insumos_usados: string[];
  insumos_faltantes: string[];
}

/**
 * Motor v2.2, rama 'digital': un producto digital no tiene un techo de
 * capacidad semanal como un producto fisico (no se "produce" una unidad a
 * la vez) -- en su lugar, los tres escenarios son niveles de ADOPCION de
 * una meta declarada (unidades_vendidas, reusado aqui como "meta mensual
 * realista de usuarios o ventas"): 50%, 100%, 200% de esa meta. Sin nodo
 * dedicado todavia (aritmetica directa sobre unidades_vendidas y
 * precio_tentativo, igual que techo_ingreso_capacidad hace con
 * capacidad_semanal).
 */
export function escenariosAdopcion(numeros: NumerosProyecto, tipoOferta?: TipoOferta): ResultadoEscenariosAdopcion {
  const meta = _valor(numeros, "unidades_vendidas");
  const precio = _valor(numeros, "precio_tentativo");
  const faltantes = (
    [
      ["unidades_vendidas", meta],
      ["precio_tentativo", precio],
    ] as const
  )
    .filter(([, v]) => v === null)
    .map(([c]) => c);
  if (faltantes.length) {
    return { "50%": null, "100%": null, "200%": null, insumos_usados: [], insumos_faltantes: faltantes };
  }
  const margen = margenUnitario(numeros, tipoOferta);
  const margenU = margen.valor;

  let metaV: number;
  let precioV: number;
  let margenV: number | null;
  if (_hayRango(meta, precio) || _esRango(margenU)) {
    // Mismo criterio de simplificacion que escenariosCapacidad: los
    // rangos colapsan al punto medio para no explotar en un arbol de
    // combinaciones dificil de leer en el reporte.
    metaV = _esRango(meta) ? _r((meta.min + meta.max) / 2, 1)! : (meta as number);
    precioV = _esRango(precio) ? _r((precio.min + precio.max) / 2)! : (precio as number);
    margenV = _esRango(margenU) ? _r((margenU.min + margenU.max) / 2) : (margenU as number | null);
  } else {
    metaV = meta as number;
    precioV = precio as number;
    margenV = margenU as number | null;
  }

  const escenario = (factor: number): EscenarioAdopcion => {
    const unidades = _r(metaV * factor, 1)!;
    return {
      unidades,
      ingreso: _r(unidades * precioV)!,
      margen_total: margenV !== null ? _r(unidades * margenV) : null,
    };
  };

  return {
    "50%": escenario(0.5),
    "100%": escenario(1.0),
    "200%": escenario(2.0),
    insumos_usados: ["unidades_vendidas", "precio_tentativo", ...margen.insumos_usados],
    insumos_faltantes: [],
  };
}

export const UMBRAL_MARGEN_PCT_INCONSISTENTE = -100; // margen mas negativo que -100% del precio
export const UMBRAL_PRECIO_MINIMO_FRACCION_COSTO = 0.05; // precio < 5% del costo unitario

export interface ResultadoGigo {
  inconsistente: boolean;
  motivo: string | null;
}

/**
 * Guardian GIGO (Motor v2.2): antes de narrar cualquier conclusion
 * financiera, verifica que los numeros capturados no sean matematicamente
 * absurdos al punto de sugerir que una cifra quedo en la unidad
 * equivocada (ej. un presupuesto MENSUAL leido como costo POR UNIDAD).
 * Caso real que motiva esta funcion: costo_materiales_unidad=200 (era en
 * realidad presupuesto mensual), horas_por_unidad=4 (eran meses de
 * desarrollo), precio_tentativo=13 (precio real del pack) -> costo total
 * 400, margen -387, margen_pct = -387/13*100 = -2976.9%. El reporte
 * narro con confianza 'no existe punto de equilibrio posible' sobre un
 * modelo cuyo equilibrio real (una vez corregida la unidad) es de solo
 * 16 packs/mes. Esta funcion existe para que ese calculo NUNCA se narre
 * como si fuera confiable.
 */
export function detectarInconsistenciaGigo(numeros: NumerosProyecto, tipoOferta?: TipoOferta): ResultadoGigo {
  const costo = costoUnitarioTotal(numeros, tipoOferta);
  const precio = _valor(numeros, "precio_tentativo");
  if (costo.valor === null || precio === null) {
    return { inconsistente: false, motivo: null };
  }
  let costoV = costo.valor as number;
  let precioV = precio as number;
  if (_esRango(costo.valor)) costoV = (costo.valor.min + costo.valor.max) / 2;
  if (_esRango(precio)) precioV = (precio.min + precio.max) / 2;
  if (costoV <= 0 || precioV <= 0) {
    return { inconsistente: false, motivo: null };
  }
  const margenPct = ((precioV - costoV) / precioV) * 100;
  if (margenPct < UMBRAL_MARGEN_PCT_INCONSISTENTE) {
    return {
      inconsistente: true,
      motivo:
        `con estos numeros el margen por unidad es ${_r(margenPct, 1)}%, muy por debajo ` +
        "de -100% -- es mas probable que alguna cifra este en la unidad equivocada (por " +
        "ejemplo, un presupuesto mensual leido como costo por unidad, o un plazo en meses " +
        "leido como horas) que que cada venta pierda esa cantidad de dinero",
    };
  }
  if (precioV < costoV * UMBRAL_PRECIO_MINIMO_FRACCION_COSTO) {
    return {
      inconsistente: true,
      motivo:
        "el precio declarado es menos del 5% del costo unitario calculado -- revisa si el " +
        "precio y el costo estan expresados en la misma unidad (por pieza, por mes, etc.)",
    };
  }
  return { inconsistente: false, motivo: null };
}

export const CAMPOS_CICLO_CONVERSION_EFECTIVO = ["dias_inventario", "dias_cobro_clientes", "dias_pago_proveedores"] as const;

export interface ResultadoCCE {
  valor: number | null;
  insumos_usados: string[];
  insumos_faltantes: string[];
}

/**
 * Cash Conversion Cycle = dias_inventario + dias_cobro_clientes - dias_pago_proveedores.
 * Fuente: nodo 'ciclo_de_conversion_de_efectivo'. Los 8 campos nucleares de
 * numeros_proyecto (Motor v2.1) no incluyen datos de cobro/pago todavia, asi
 * que esta funcion casi siempre reportara insumos_faltantes hasta que una
 * fase futura capture esos campos; existe para completar la formula del nodo
 * y para no fingir un calculo que no se puede hacer con lo disponible.
 */
export function cicloConversionEfectivo(numeros: NumerosProyecto): ResultadoCCE {
  const valores = Object.fromEntries(CAMPOS_CICLO_CONVERSION_EFECTIVO.map((c) => [c, _valor(numeros, c)]));
  const faltantes = CAMPOS_CICLO_CONVERSION_EFECTIVO.filter((c) => valores[c] === null);
  if (faltantes.length) {
    return { valor: null, insumos_usados: [], insumos_faltantes: [...faltantes] };
  }
  const valor =
    (valores.dias_inventario as number) + (valores.dias_cobro_clientes as number) - (valores.dias_pago_proveedores as number);
  return { valor: _r(valor, 1), insumos_usados: [...CAMPOS_CICLO_CONVERSION_EFECTIVO], insumos_faltantes: [] };
}

export interface ReporteCalculado {
  costo_unitario: ResultadoValor;
  margen: ResultadoMargen;
  punto_equilibrio: ResultadoEquilibrio;
  ciclo_conversion_efectivo: ResultadoCCE;
  capacidad: ResultadoCapacidad;
  escenarios: ResultadoEscenariosCapacidad | ResultadoEscenariosAdopcion;
}

/**
 * Corre todos los calculos disponibles sobre numeros_proyecto y devuelve
 * un objeto agregado. No lanza excepciones ante datos faltantes: cada
 * sub-resultado reporta sus propios insumos_faltantes.
 *
 * Motor v2.2: tipoOferta=undefined/null o 'producto_fisico'/'servicio' usa
 * 'capacidad'/'escenarios' basados en capacidad semanal (retrocompatible,
 * formulas sin cambios). tipoOferta='digital' usa 'escenarios' basados
 * en adopcion de una meta declarada en su lugar (escenariosAdopcion);
 * 'capacidad' queda en null porque el techo de produccion semanal no
 * aplica a una oferta digital. El guardian GIGO (detectarInconsistenciaGigo)
 * NO vive aqui adentro a proposito: el llamador (route de --reporte) lo
 * llama por separado antes de decidir si narra o no.
 */
// =====================================================================
// Palancas inversas (canon 14, "Tus Numeros"): dado un OBJETIVO, que
// precio, que costo o que volumen lo logra. Son el corazon de las tres
// palancas de la pantalla. NO inventan el objetivo -- la politica de a
// que apunta cada palanca (que margen es "sano", que meta de ganancia)
// vive en la capa que arma la pantalla, no aqui; aqui solo esta la
// aritmetica inversa, espejo exacta de margenUnitario/puntoEquilibrio.
// Paridad con engine/calculadora.py. CERO LLM, rangos soportados, y el
// objetivo escalar (precioNuevo, margenPct, ganancia) nunca es rango.
// =====================================================================

export interface ResultadoObjetivo {
  valor: ValorNumerico | null;
  insumos_usados: string[];
  insumos_faltantes: string[];
  nota?: string;
}

/**
 * Margen por unidad si el precio fuera `precioNuevo` en vez del
 * precio_tentativo declarado (el costo unitario no cambia). Espejo de
 * margenUnitario con el precio sustituido: sirve para narrar "a $58 tu
 * margen pasa a +$16" sin tocar numeros_proyecto.
 */
export function margenConPrecio(numeros: NumerosProyecto, precioNuevo: number, tipoOferta?: TipoOferta): ResultadoMargen {
  const costo = costoUnitarioTotal(numeros, tipoOferta);
  if (costo.valor === null) {
    return { valor: null, porcentaje: null, insumos_usados: [], insumos_faltantes: costo.insumos_faltantes };
  }
  const costoV = costo.valor;
  let margen: ValorNumerico;
  let porcentaje: ValorNumerico | null;
  if (_esRango(costoV)) {
    const lo = precioNuevo - _lado(costoV, "max");
    const hi = precioNuevo - _lado(costoV, "min");
    margen = { min: _r(lo)!, max: _r(hi)! };
    porcentaje = precioNuevo
      ? { min: _r((lo / precioNuevo) * 100, 1)!, max: _r((hi / precioNuevo) * 100, 1)! }
      : null;
  } else {
    margen = _r(precioNuevo - (costoV as number))!;
    porcentaje = precioNuevo ? _r(((margen as number) / precioNuevo) * 100, 1) : null;
  }
  return { valor: margen, porcentaje, insumos_usados: costo.insumos_usados, insumos_faltantes: [] };
}

/**
 * Margen por unidad si el costo unitario fuera `costoNuevo` (el
 * precio_tentativo declarado no cambia). Espejo de margenUnitario con el
 * costo sustituido: la palanca "baja el costo a $24 -> +$14".
 */
export function margenConCosto(numeros: NumerosProyecto, costoNuevo: number): ResultadoMargen {
  const precio = _valor(numeros, "precio_tentativo");
  if (precio === null) {
    return { valor: null, porcentaje: null, insumos_usados: [], insumos_faltantes: ["precio_tentativo"] };
  }
  let margen: ValorNumerico;
  let porcentaje: ValorNumerico | null;
  if (_esRango(precio)) {
    const lo = _lado(precio, "min") - costoNuevo;
    const hi = _lado(precio, "max") - costoNuevo;
    margen = { min: _r(lo)!, max: _r(hi)! };
    const pLo = _lado(precio, "min");
    const pHi = _lado(precio, "max");
    porcentaje = {
      min: pLo ? _r((lo / pLo) * 100, 1)! : (null as unknown as number),
      max: pHi ? _r((hi / pHi) * 100, 1)! : (null as unknown as number),
    };
  } else {
    const precioN = precio as number;
    margen = _r(precioN - costoNuevo)!;
    porcentaje = precioN ? _r(((margen as number) / precioN) * 100, 1) : null;
  }
  return { valor: margen, porcentaje, insumos_usados: ["precio_tentativo"], insumos_faltantes: [] };
}

/**
 * Precio al que habria que vender para que el margen porcentual fuera
 * `margenPctObjetivo` (fraccion, ej. 0.25 = 25%): precio = costo / (1 - m).
 * La palanca "sube el precio a X". margenPctObjetivo en [0, 1); 100% o
 * mas es inalcanzable (precio infinito o negativo).
 */
export function precioParaMargenObjetivo(
  numeros: NumerosProyecto,
  margenPctObjetivo: number,
  tipoOferta?: TipoOferta
): ResultadoObjetivo {
  const costo = costoUnitarioTotal(numeros, tipoOferta);
  if (costo.valor === null) {
    return { valor: null, insumos_usados: [], insumos_faltantes: costo.insumos_faltantes };
  }
  if (margenPctObjetivo === null || margenPctObjetivo === undefined || margenPctObjetivo < 0 || margenPctObjetivo >= 1) {
    return {
      valor: null,
      insumos_usados: [],
      insumos_faltantes: [],
      nota: "un margen objetivo fuera de [0, 100%) no da un precio valido: 100% o mas implicaria precio infinito",
    };
  }
  const factor = 1 - margenPctObjetivo;
  const costoV = costo.valor;
  const valor: ValorNumerico = _esRango(costoV)
    ? { min: _r(_lado(costoV, "min") / factor)!, max: _r(_lado(costoV, "max") / factor)! }
    : _r((costoV as number) / factor)!;
  return { valor, insumos_usados: costo.insumos_usados, insumos_faltantes: [] };
}

/**
 * Costo unitario maximo para que, al precio_tentativo declarado, el
 * margen porcentual llegue a `margenPctObjetivo`: costo = precio * (1 - m).
 * La palanca "baja el costo a Y". margenPctObjetivo en [0, 1).
 */
export function costoMaximoParaMargenObjetivo(numeros: NumerosProyecto, margenPctObjetivo: number): ResultadoObjetivo {
  const precio = _valor(numeros, "precio_tentativo");
  if (precio === null) {
    return { valor: null, insumos_usados: [], insumos_faltantes: ["precio_tentativo"] };
  }
  if (margenPctObjetivo === null || margenPctObjetivo === undefined || margenPctObjetivo < 0 || margenPctObjetivo >= 1) {
    return { valor: null, insumos_usados: [], insumos_faltantes: [], nota: "un margen objetivo fuera de [0, 100%) no da un costo valido" };
  }
  const factor = 1 - margenPctObjetivo;
  const valor: ValorNumerico = _esRango(precio)
    ? { min: _r(_lado(precio, "min") * factor)!, max: _r(_lado(precio, "max") * factor)! }
    : _r((precio as number) * factor)!;
  return { valor, insumos_usados: ["precio_tentativo"], insumos_faltantes: [] };
}

/**
 * Unidades/mes para que, despues de cubrir los costos fijos, quede una
 * ganancia mensual de `gananciaObjetivo`: ceil((fijos + ganancia) / margen).
 * gananciaObjetivo=0 es exactamente el punto de equilibrio (cubrir fijos).
 * Redondeo hacia ARRIBA por la misma razon que puntoEquilibrioUnidadesMes.
 * Requiere margen positivo: con margen <= 0 no hay volumen que llegue
 * (vender mas agranda la perdida).
 */
export function unidadesParaGananciaObjetivo(
  numeros: NumerosProyecto,
  gananciaObjetivo = 0,
  tipoOferta?: TipoOferta
): ResultadoEquilibrio {
  const margen = margenUnitario(numeros, tipoOferta);
  const costosFijos = _valor(numeros, "costos_fijos_mensuales");
  const faltantes = [...margen.insumos_faltantes];
  if (costosFijos === null) faltantes.push("costos_fijos_mensuales");
  if (faltantes.length) {
    return { valor: null, insumos_usados: [], insumos_faltantes: faltantes };
  }
  const margenV = margen.valor as ValorNumerico;
  if (_hayRango(margenV, costosFijos)) {
    const mLo = _lado(margenV, "min");
    const mHi = _lado(margenV, "max");
    const cfLo = _lado(costosFijos, "min");
    const cfHi = _lado(costosFijos, "max");
    if (mLo <= 0 || mHi <= 0) {
      return {
        valor: null,
        insumos_usados: [],
        insumos_faltantes: [],
        nota: "el margen por unidad no es positivo en todo el rango; ningun volumen alcanza la meta",
      };
    }
    return {
      valor: { min: Math.ceil((cfLo + gananciaObjetivo) / mHi), max: Math.ceil((cfHi + gananciaObjetivo) / mLo) },
      insumos_usados: [...margen.insumos_usados, "costos_fijos_mensuales"],
      insumos_faltantes: [],
    };
  }
  const margenN = margenV as number;
  if (margenN <= 0) {
    return {
      valor: null,
      insumos_usados: [],
      insumos_faltantes: [],
      nota: "el margen por unidad no es positivo; ningun volumen alcanza la meta (vender mas agranda la perdida)",
    };
  }
  return {
    valor: Math.ceil(((costosFijos as number) + gananciaObjetivo) / margenN),
    insumos_usados: [...margen.insumos_usados, "costos_fijos_mensuales"],
    insumos_faltantes: [],
  };
}

export function calcularReporte(numerosProyecto: NumerosProyecto, tipoOferta?: TipoOferta): ReporteCalculado {
  const resultado: ReporteCalculado = {
    costo_unitario: costoUnitarioTotal(numerosProyecto, tipoOferta),
    margen: margenUnitario(numerosProyecto, tipoOferta),
    punto_equilibrio: puntoEquilibrioUnidadesMes(numerosProyecto, tipoOferta),
    ciclo_conversion_efectivo: cicloConversionEfectivo(numerosProyecto),
    capacidad: { unidades_mes: null, ingreso: null, margen_mensual: null, insumos_usados: [], insumos_faltantes: [] },
    escenarios: { pesimista: null, base: null, sobredemanda: null, insumos_usados: [], insumos_faltantes: [] },
  };
  if (tipoOferta === "digital") {
    resultado.escenarios = escenariosAdopcion(numerosProyecto, tipoOferta);
  } else {
    resultado.capacidad = techoIngresoCapacidad(numerosProyecto);
    resultado.escenarios = escenariosCapacidad(numerosProyecto);
  }
  return resultado;
}
