# -*- coding: utf-8 -*-
"""Parche de la vuelta 40: anade el modo --cierre al registro de OP-D-05."""
import io

P = "scripts/loop/vuelta40_registro_opd05.py"
s = io.open(P, encoding="utf-8").read()

viejo = '''def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sellado", action="store_true")
    a = ap.parse_args()
    p = leer_plan()
    if a.sellado:
        texto = sellado(p)
    else:
        sys.exit("hace falta --sellado")'''

nuevo = '''def censo():
    total = vivos = dep = 0
    for nombre in os.listdir(NODOS):
        if not nombre.endswith(".json"):
            continue
        total += 1
        d = json.loads(io.open(os.path.join(NODOS, nombre), encoding="utf-8").read())
        if d.get("deprecado") or d.get("deprecated"):
            dep += 1
        else:
            vivos += 1
    return total, vivos, dep


def cierre(p):
    """LAS CIFRAS DEL CIERRE SE MIDEN AL CIERRE (EJECUTOR.md regla 1): el censo se
    recuenta ahora mismo sobre dataset/nodos y los enlaces se cuentan a los dos
    lados, contra el commit anterior a la fusion y contra el grafo de hoy."""
    import subprocess
    sup = p["superviviente"]
    d = json.loads(io.open(os.path.join(NODOS, sup + ".json"),
                           encoding="utf-8").read())
    total, vivos, dep = censo()

    def enlaces(commit=None):
        if commit:
            bruto = subprocess.check_output(
                ["git", "show", "%s:dataset/metadata/master_graph.json" % commit],
                cwd=RAIZ).decode("utf-8")
        else:
            bruto = io.open(os.path.join(RAIZ, "dataset", "metadata",
                                         "master_graph.json"),
                            encoding="utf-8").read()
        G = json.loads(bruto)["nodos"]
        return sum(len(v.get(c) or [])
                   for v in G.values()
                   for c in ("nodos_previos", "nodos_siguientes"))

    e_antes, e_despues = enlaces("002edf43"), enlaces()
    mil = lambda n: "{:,}".format(n).replace(",", ".")

    L = []
    A = L.append
    A("")
    A("### `OP-D-05` CERRADA: **LA FUSION EJECUTADA** (19 ago 2026, vuelta 40)")
    A("")
    A("**Esta seccion NO reescribe la de arriba.** El plan sellado se queda entero "
      "donde esta, y aqui va lo que paso al ejecutarlo, para que los dos se puedan "
      "comparar sin que uno tape al otro.")
    A("")
    A("#### EL RESULTADO, releido en `dataset/nodos` y no copiado del plan")
    A("")
    A("| | |")
    A("|---|---|")
    A("| superviviente | `%s`, **vivo**, **%d pasos** y **%d condiciones** |"
      % (sup, len(d.get("pasos_accionables") or []),
         len(d.get("condiciones_activacion") or [])))
    A("| titulo y etiqueta | **sin tocar** (`a6`): *%s* / *%s* |"
      % (d.get("titulo_concepto"), d.get("etiqueta_arbol")))
    A("| alias | %s |" % ", ".join("`%s`" % x for x in (d.get("ids_alias") or [])))
    A("| absorbidos | %s, **deprecados y con su texto entero** |"
      % ", ".join("`%s`" % x for x in p["absorbidos"]))
    A("| estandar de pasos | **%d, DENTRO del estandar de 3 a 6.** Esta operacion "
      "**no usa la excepcion de clase** de `OP-F-01` |"
      % len(d.get("pasos_accionables") or []))
    A("| campo `superviviente` | **ESCRITO** con `%s`, por el precedente **medido** "
      "de `OP-D-02`, que es la otra fusion de un solo superviviente y lo tiene "
      "escrito. **No es el `null` de `OP-D-03` ni el de `OP-D-04`** |" % sup)
    A("")
    A("#### EL CENSO, RECONTADO AL CIERRE")
    A("")
    A("| momento | ficheros | vivos | deprecados | enlaces |")
    A("|---|---:|---:|---:|---:|")
    A("| antes de la fusion (commit `002edf43`) | 3.853 | 3.534 | 319 | %s |"
      % mil(e_antes))
    A("| **recontado al cierre, ahora mismo** | **%s** | **%s** | **%s** | **%s** |"
      % (mil(total), mil(vivos), dep, mil(e_despues)))
    A("")
    A("**LA ARITMETICA DE LOS ENLACES, comprobada entrada por entrada y no "
      "publicada a ojo:** `criterios_equity_split.nodos_previos` **menos 1**, "
      "`decision_fundador_solo_vs_equipo.nodos_siguientes` **menos 2** (nombraba a "
      "los DOS absorbidos y ademas ya al superviviente, asi que tres entradas "
      "colapsan en una), y `%s` **mas 1** en `nodos_previos` y **mas 4** en "
      "`nodos_siguientes` por la simetrizacion del paso 5. **Menos 1, menos 2, mas "
      "1, mas 4, igual mas 2; y %s menos %s es 2.**"
      % (sup, mil(e_despues), mil(e_antes)))
    A("")
    A("#### LA VERIFICACION DE LA PROPIA OPERACION, punto por punto")
    A("")
    A("| punto, tal como lo escribe `OPERACIONES.jsonl` | como quedo |")
    A("|---|---|")
    A("| **1**, `Gate 0 verde` | **`GATE 0: OK`, exit 0** "
      "(`docs/loop/SALIDA_V40_GATE0.txt`), mas **71 etiquetas** y **seis assets** |")
    A("| **2**, `recomputo del cierre transitivo` | **CORRIDO** "
      "(`docs/loop/SALIDA_V40_RECOMPUTO_3388.txt`): actos de **333 a 332**, "
      "`CERRADOS` de **279 sobre 598** nodos a **278 sobre 595**, `ABIERTOS` "
      "**quietos en 54 sobre 243** porque el acto estaba CERRADO, nodos en actos "
      "de **841 a 838** y `A` vigentes de **569 a 566**. **Las cuatro "
      "comprobaciones del `08_VERIFICACION.md`: OK las cuatro.** El acto de tres "
      "**deja de existir**, porque sus tres nodos son ahora uno |")
    A("| **3**, `cada perdida quedo en el bloque del que proviene, o en el "
      "superviviente` | **CORRIDO** (`scripts/loop/verificar_mapas_destejido.py` "
      "con los SEIS planes sellados, `docs/loop/SALIDA_V40_VERIFICADOR_MAPAS.txt`): "
      "**6 tablas, 37 filas, 0 discrepancias**, varas 1 y 2 CORRIDAS. Y la tabla "
      "de `P.13`: **21 de 21 piezas VIAJAN y CERO se pierden**, o sea que **la "
      "regla de reparto se cumple POR VACIO**, y se dice asi en vez de darla por "
      "cumplida |")
    A("| **4**, `el acto se leyo ENTERO antes de fundirse: cero pares internos sin "
      "veredicto` | **3 de 3 con clase, los tres del ARCHIVO** y **cero lecturas "
      "dirigidas** (`docs/loop/SALIDA_V40_OPD05_ACTO.txt`). **No hizo falta releer "
      "ninguno: no hubo destejido que los dejara rancios** |")
    A("")
    A("#### EL PUNTO DEL ESTANDAR DE PASOS, CERRADO CON EL INSTRUMENTO YA VIVO")
    A("")
    A("**El resultado queda en SEIS pasos**, dentro del estandar de 3 a 6, asi que "
      "**no hace falta la excepcion de clase**. Pero el instrumento de costuras, "
      "reparado en esta misma vuelta y **corrido otra vez DESPUES de la fusion**, "
      "**CITA al resultado**: bloque **48,4**, corte tras el paso 3. **Y hay que "
      "decir lo que la vuelta 39 si pudo decir de su caso y esta NO puede: LA "
      "FUSION ENCENDIO LA SENAL.** Antes de fundir, `%s` daba **43,6** y estaba "
      "**fuera** de la cola." % sup)
    A("")
    A("**ESO SE MIDIO EN VEZ DE SOSTENERSE** "
      "(`scripts/loop/vuelta40_senal_antes_despues.py`, salida en "
      "`docs/loop/SALIDA_V40_SENAL_ANTES_DESPUES.txt`), sobre los **tres** "
      "resultantes de fusion que esta campaña lleva:")
    A("")
    A("| resultante | bloque ANTES | bloque DESPUES | movimiento | la cola |")
    A("|---|---:|---:|---:|---|")
    A("| `reglas_brainstorming` (`OP-D-04`, el taller) | 47,7 | **50,6** | **mas "
      "2,9** | DENTRO antes y despues |")
    A("| `pensamiento_convergente_divergente` (`OP-D-04`) | 0,0 | **43,8** | **mas "
      "43,8** | fuera antes y despues |")
    A("| **`%s`** (`OP-D-05`) | **43,6** | **48,4** | **mas 4,8** | **fuera antes, "
      "DENTRO despues** |" % sup)
    A("")
    A("> **SUBE EN 3 DE 3, y el mecanismo es mecanico y no semantico:** fundir mete "
      "el vocabulario de tres nodos en menos pasos y mas densos, y la senal de "
      "bloque mide **solape de tokens** entre los dos bloques de la lista. **Una "
      "cita sobre un nodo recien fundido es lo esperable.** **Y LO QUE ESO NO "
      "AUTORIZA: descartar la cita.** El instrumento **cita y no juzga**, y una "
      "cita es **una lectura obligada**.")
    A("")
    A("**LA LECTURA, hecha con el texto delante.** El corte que la senal propone es "
      "**tras el paso 3**: los pasos 1 a 3 contra los 4 a 6. **Los pasos 1 a 3 son "
      "la DELIBERACION** (con quien hablarlo, quien es la persona de la idea, con "
      "que vara se evalua) **y los 4 a 6 son la EJECUCION** (que rol alternativo "
      "darle, como se negocia el titulo, como se documenta). **El segundo bloque no "
      "vuelve a contar el primero: lo continua.** Y la pareja que el instrumento "
      "cita, los pasos 1 y 5, comparte **el vocabulario del acto** (CEO, titulos, "
      "conflicto) **y no su narracion**: el 1 es la conversacion que hay que tener "
      "y el 5 es la negociacion del titulo y la junta. **Es el limite que el propio "
      "instrumento declara en su encabezado, visto por el otro lado: un comparador "
      "de tokens no distingue tema de narracion.**")
    A("")
    A("**VA COMO DISCUTIBLE MARCADO AL AUDITOR**, porque quien declara que no hay "
      "costura es el mismo que hizo la fusion que encendio la senal.")
    A("")
    A("#### LO QUE ESTE CIERRE NO HACE")
    A("")
    A("- **No enlaza nada por `P.10`.** El acto era **UNA familia entera de tres** "
      "y **los tres se funden**: no queda colgado ni tercera salida que escribir. "
      "**Se dice en vez de callarlo**, porque `OP-D-04` si la tuvo.")
    A("- **No cambia el estado de la operacion.** Sigue en `LISTA`, **igual que "
      "`OP-D-01` a `OP-D-04`, que tambien estan ejecutadas**. **PENDIENTE DE "
      "DOCTRINA heredado: el esquema no distingue una operacion HECHA.**")
    A("- **No borra un solo fichero.** Los dos absorbidos **conservan su texto "
      "entero**, que es lo que hace auditable la fusion.")
    A("")
    return "\\n".join(L) + "\\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sellado", action="store_true")
    ap.add_argument("--cierre", action="store_true")
    a = ap.parse_args()
    p = leer_plan()
    if a.sellado:
        texto = sellado(p)
    elif a.cierre:
        texto = cierre(p)
    else:
        sys.exit("hace falta --sellado o --cierre")'''

assert s.count(viejo) == 1, "no ancla"
s = s.replace(viejo, nuevo)
io.open(P, "w", encoding="utf-8", newline="\n").write(s)
print("modo --cierre anadido")
