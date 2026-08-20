# -*- coding: utf-8 -*-
"""vuelta56_correcciones_tarea1.py . LOS TRES REGISTROS DEL ACTA 55 (TAREA 1 del
encargo de la vuelta 56).

MISMA MAQUINA que scripts/loop/vuelta55_correcciones_tarea1.py: cada sitio se
localiza por un ANCLA literal, el texto viejo NO se borra ni se reescribe (se le
ADOSA lo nuevo detras), y el instrumento es IDEMPOTENTE, o sea que re-correrlo
no vuelve a escribir nada. Si un ancla no aparece, o aparece mas de una vez, cae
en rojo y no escribe NADA: un ancla ambigua no es un ancla.

LO QUE ESCRIBE, y nada mas:

  1.1  LA ADJUDICACION DEL FILO, adosada al carril: junto a la tabla de las
       cinco relecturas del filo del tramo 2, la adjudicacion del acta 55,
       pregunta 1, con sus DOS sedes citadas (acta 51 pregunta 2, de la que es
       extension citable; acta 55 pregunta 1, que fija la marca operativa).

  1.2  LA CORRECCION DE LA CUENTA DE PERDIDAS, adosada a la fila de suma de la
       tabla tallada del tramo 2, que es EXACTAMENTE la celda donde la cifra se
       podria heredar mal. LA TABLA DE LAS CUATRO PERDIDAS NO ESTA TECLEADA:
       se pega ENTERA de la salida de
       `python scripts/loop/vuelta56_tallar_perdidas_v55.py`, que la talla de
       los PLAN_V55_*.json SELLADOS y clasifica la especie leyendo el propio
       plan, sin rama por defecto (regla 1 del EJECUTOR).

  1.3  EL PENDIENTE DE DOCTRINA DEL `INCISO` DE CONDICIONES, con su cuenta
       corregida, en el mismo sitio. SE DECLARA UNA MEDICION QUE EL ENCARGO NO
       DABA POR HECHA Y QUE HAY QUE DECIR: el encargo pide dejar la cuenta
       "donde ese pendiente este nombrado en el registro", y MEDIDO HOY POR
       GREP SOBRE docs/plan/ EL PENDIENTE NO ESTABA NOMBRADO EN NINGUNA PAGINA
       DEL PLAN: vivia solo en docs/loop/REPORTE.md y en
       docs/loop/ACTA_AUDITOR.md. Asi que aqui se NOMBRA por primera vez en el
       registro, junto a la cuenta que lo mide, y la medicion va escrita en la
       propia nota en vez de callarse.

EL REPORTE VIEJO NO SE EDITA. Una correccion que tapa lo que corrige no se
puede auditar (banco 9.10): la correccion vive donde la cifra podria heredarse,
y el texto de la vuelta 55 se queda donde esta.

Uso: python scripts/loop/vuelta56_correcciones_tarea1.py [--simular]
"""
import argparse
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FUSIONES = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
TALLADOR = os.path.join(RAIZ, "scripts", "loop", "vuelta56_tallar_perdidas_v55.py")

# --------------------------------------------------------------------------
# 1.1 . EL ANCLA es la ultima linea del bloque de citas que cierra la tabla de
# las cinco relecturas del filo del tramo 2, para que la adjudicacion quede
# DETRAS de la tabla que interpreta y con el texto viejo delante entero.
# --------------------------------------------------------------------------
ANCLA_FILO = ("> ([`../loop/SALIDA_V55_COLISIONES_ESPERADAS_TRAS_FILO.txt`]"
              "(../loop/SALIDA_V55_COLISIONES_ESPERADAS_TRAS_FILO.txt)).\n")

NOTA_FILO = """
> ### ADJUDICACION REGISTRADA: **UNA RAZON QUE REMITE A UNA MESA, O QUE SE ABSTIENE, ES PREGUNTA DE POLITICA Y BLOQUEA EL ACTO** (20 ago 2026, vuelta 56, TAREA 1.1 del encargo; adjudicada por el acta de la vuelta 55, pregunta 1)
>
> **La pregunta que esta nota cierra**, y que la tabla de arriba hizo caer cinco veces: cuando una
> razon del filo dice *esto lo decide la mesa* o *no lo decido*, eso cuenta como **PREGUNTA DE
> POLITICA que BLOQUEA el acto**, o como **MATIZ que no lo bloquea**. De ella dependian los actos
> **6** y **49**, que la vuelta 55 declaro en vez de fundir.
>
> **LA RESPUESTA, POR EXTENSION CITABLE Y SIN DOCTRINA NUEVA: ES PREGUNTA DE POLITICA, Y BLOQUEA.**
> Y con ella va **LA MARCA OPERATIVA**, para que la lectura no dependa del gusto de quien lee:
>
> | la forma de la razon | que es | que se hace con el acto |
> |---|---|---|
> | **REMITE** la decision a una **INSTANCIA NOMBRADA** (una mesa, un criterio por adoptar) | **PREGUNTA DE POLITICA** | **NO se funde**: se **DECLARA** y acumula para esa mesa |
> | **SE ABSTIENE** con sus palabras (*no lo decido*) | **PREGUNTA DE POLITICA** | **NO se funde**: se **DECLARA** y acumula |
> | **RESERVA que la propia razon resuelve, o que una VARA ESCRITA resuelve** | **MATIZ** | **se resuelve y el acto SE FUNDE** |
>
> **LAS DOS SEDES, citadas y no resumidas:** el **acta de la vuelta 51, pregunta 2**, que fija el
> carril del filo (*si la relectura encuentra que lo congelado es una pregunta de POLITICA de
> catalogo, el acto NO se funde*) y de la que esta adjudicacion es **extension citable**; y el
> **acta de la vuelta 55, pregunta 1**, que fija la **marca operativa** de arriba.
>
> **LAS FIGURAS ESTAN EN ESTA MISMA TABLA, y por eso la nota va aqui y no en otra pagina:** los
> cuatro pares de los actos **6** y **49** (**668**, **968**, **338** y **297**) escriben la
> remision o la abstencion **con sus palabras**, y los dos actos quedan **DECLARADOS**; el **218**
> del acto **44** era una **RESERVA que una vara escrita resuelve**, la del banco `9.6.1` (la linea
> contra el procedimiento), **y por eso ese acto SI se fundio**. **Cuatro y uno, en la misma
> tanda**: es el contraste el que hace legible la marca.
>
> **LO QUE ESTA ADJUDICACION NO DICE, para que no se estire:** **no contesta ninguna** de las
> preguntas de politica que las cuatro razones destapan. **Quien las contesta sigue siendo la mesa**
> del `PARA_ALEXIS` del cierre, y ese pendiente de doctrina **sigue abierto y engordado** con los
> actos 6 y 49.

"""

# --------------------------------------------------------------------------
# 1.2 y 1.3 . EL ANCLA es la fila de suma de la tabla tallada del tramo 2, que
# es la celda que publica el "4" de las perdidas nombradas: es ahi, y no en
# otro sitio, donde la cifra se podria heredar con la especie equivocada.
# --------------------------------------------------------------------------
ANCLA_SUMA = ("| **los tres** | | **25** | **25** | **156** | **53** | **75** | "
              "**28** | **4** |\n")

NOTA_PERDIDAS_CAB = """
> ### CORRECCION DECLARADA: **LAS CUATRO PERDIDAS NO SON TODAS DE CONDICIONES. SON TRES Y UNA** (20 ago 2026, vuelta 56, TAREA 1.2 del encargo; caida de reporte nombrada por el acta de la vuelta 55, seccion 3)
>
> **LA CELDA DE ARRIBA DICE `4` PERDIDAS NOMBRADAS Y ESA CIFRA ES CORRECTA: son cuatro.** Lo que
> estaba mal era **SU ESPECIE**, y la correccion se escribe **aqui** porque esta es la celda desde
> la que la cifra se podria heredar.
>
> **ESTA TABLA NO ESTA TECLEADA: sale entera de
> `python scripts/loop/vuelta56_tallar_perdidas_v55.py`**
> ([`../loop/SALIDA_V56_TALLAR_PERDIDAS_V55.txt`](../loop/SALIDA_V56_TALLAR_PERDIDAS_V55.txt)),
> **que la talla de los `PLAN_V55_*.json` SELLADOS y lee la especie del propio plan**, sin rama por
> defecto: si el trozo sellado no nombra ni condicion ni paso, o nombra los dos, el tallador sale
> **ROJO con el acto nombrado** y no emite tabla. **La ultima columna trae la frase sellada
> VERBATIM**, recortada por maquina, para que la etiqueta no haya que creersela.
>
"""

NOTA_PERDIDAS_PIE = """>
> **TRES DE CONDICIONES Y UNA DE PARAMETRO DE PASO.** **El `D8` del reporte de la vuelta 55 las
> llamo a las CUATRO de condiciones, y esa es la caida de reporte que el acta de la vuelta 55
> nombra en su seccion 3.** **EL REPORTE VIEJO NO SE EDITA** (una correccion que tapa lo que
> corrige no se puede auditar, banco `9.10`): **la correccion vive aqui**. Y se deja dicho que
> **aquel mismo reporte describia BIEN el caso del 45 en su `D5` y lo generalizaba MAL en su
> `D8`**: la caida no fue de medicion, fue de dictado.

> ### EL PENDIENTE DE DOCTRINA DEL `INCISO` DE CONDICIONES, NOMBRADO EN EL REGISTRO CON SU CUENTA MEDIDA (20 ago 2026, vuelta 56, TAREA 1.3 del encargo)
>
> **UNA MEDICION DEL DIA QUE SE DECLARA EN VEZ DE CALLARSE, porque cambia donde va esta nota:** la
> TAREA 1.3 pedia dejar la cuenta *donde ese pendiente este nombrado en el registro*, y **medido hoy
> por `grep` sobre `docs/plan/`, EL PENDIENTE NO ESTABA NOMBRADO EN NINGUNA PAGINA DEL PLAN**.
> Vivia solo en `docs/loop/REPORTE.md` y en `docs/loop/ACTA_AUDITOR.md`. **Asi que se nombra aqui
> por primera vez, pegado a la cuenta que lo mide**, que es el unico sitio del registro donde tiene
> con que sostenerse.
>
> **EL PENDIENTE, dicho entero:** el instrumento de fundir conoce el destino `INCISO` para los
> **PASOS** y **no para las CONDICIONES**. Mientras no exista, una condicion del que muere que dice
> **casi** lo mismo que una del superviviente solo tiene dos destinos: **`APPEND`**, que fabrica
> condiciones casi gemelas, o **`CUBIERTO` con perdida nombrada**.
>
> **SU COSTO, MEDIDO Y NO ESTIMADO: TRES perdidas de condicion en UNA SOLA VUELTA** (los actos
> **18**, **31** y **33** de la vuelta 55, contados por el tallador de arriba) **son el costo de
> que el `INCISO` de condiciones no exista.**
>
> **LA RAMA DE MANDARLAS DE `APPEND` QUEDO CONTESTADA** (acta de la vuelta 55, pregunta 5): **NO
> por defecto.** Fabricar condiciones casi gemelas para no nombrar una perdida **esconde el sintoma
> que mantiene visible este pendiente**, y **la perdida NOMBRADA es el carril mientras siga
> abierto**.
>
> **LA DECISION DE CREAR EL `INCISO` DE CONDICIONES SIGUE SIENDO DE LA MESA.** Este registro no la
> toma: la nombra, la mide y la deja acumulada.

"""


def tabla_tallada():
    """Recorta la tabla del tallador de su propia salida, por maquina."""
    p = subprocess.run([sys.executable, TALLADOR], capture_output=True, cwd=RAIZ)
    salida = p.stdout.decode("utf-8", "replace") + p.stderr.decode("utf-8", "replace")
    if p.returncode != 0:
        return None, "el tallador salio en ROJO (exit %d)" % p.returncode
    lineas = [l.rstrip() for l in salida.splitlines() if l.startswith("|")]
    if len(lineas) < 4:
        return None, "el tallador no emitio tabla (%d lineas)" % len(lineas)
    return "\n".join("> " + l for l in lineas) + "\n", None


def aplicar(ruta, ancla, adosado, simular):
    """Devuelve (estado, detalle). Idempotente: si el adosado ya esta, no toca."""
    with io.open(ruta, encoding="utf-8", newline="") as fh:
        texto = fh.read()
    marca = adosado.strip().splitlines()[0]
    if marca in texto:
        return "YA ESTABA", "idempotente, no se escribe"
    veces = texto.count(ancla)
    if veces == 0:
        return "ROJO", "el ancla NO aparece"
    if veces > 1:
        return "ROJO", "el ancla aparece %d veces: ambigua" % veces
    nuevo = texto.replace(ancla, ancla + adosado)
    if not simular:
        with io.open(ruta, "w", encoding="utf-8", newline="") as fh:
            fh.write(nuevo)
    return "ESCRITO", "%d caracteres adosados detras del ancla" % len(adosado)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("LOS TRES REGISTROS DEL ACTA 55 (vuelta 56, TAREA 1)")
    print("MODO %s" % ("SIMULAR" if a.simular else "ESCRIBIR"))
    print("=" * 78)
    print()

    tabla, mal = tabla_tallada()
    if tabla is None:
        print("  ROJO: no se pudo tallar la tabla de las perdidas: %s" % mal)
        print("  NO SE ESCRIBE NADA.")
        return 1
    print("  tabla de las perdidas TALLADA del plan sellado: %d lineas, %d caracteres"
          % (len(tabla.splitlines()), len(tabla)))
    print("  comando: python scripts/loop/vuelta56_tallar_perdidas_v55.py")
    print()

    nota_perdidas = NOTA_PERDIDAS_CAB + tabla + NOTA_PERDIDAS_PIE

    trabajos = [
        ("1.1, la adjudicacion del filo adosada a su tabla", FUSIONES,
         ANCLA_FILO, NOTA_FILO),
        ("1.2 y 1.3, la cuenta de perdidas y el pendiente del INCISO", FUSIONES,
         ANCLA_SUMA, nota_perdidas),
    ]

    rojo = 0
    for etiqueta, ruta, ancla, adosado in trabajos:
        estado, detalle = aplicar(ruta, ancla, adosado, a.simular)
        print("  %-62s %s" % (etiqueta, estado))
        print("      fichero: %s" % os.path.relpath(ruta, RAIZ))
        print("      ancla  : %s" % ancla.strip()[:90])
        print("      %s" % detalle)
        print()
        if estado == "ROJO":
            rojo += 1

    if rojo:
        print("  ROJO en %d de %d: NO se escribio nada de lo que fallo." % (rojo, len(trabajos)))
        return 1
    print("  LOS DOS SITIOS EN VERDE, y el texto viejo queda ENTERO en los dos: las")
    print("  notas van DETRAS de lo que interpretan (la tabla del filo y la fila de")
    print("  suma de la tabla tallada), no encima.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
