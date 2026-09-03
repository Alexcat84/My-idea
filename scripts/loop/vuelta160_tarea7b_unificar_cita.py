# -*- coding: utf-8 -*-
"""vuelta160_tarea7b_unificar_cita.py . TAREA 7.b DE LA VUELTA 160, Y NACE DE
UNA CAIDA MIA CAZADA EN EL CIERRE, ANTES DE PUBLICAR.

QUE PASO. Las TAREAS 2.a y 2.b de esta vuelta movieron CUATRO clases de C a D
(`LD-OPC05-100`, `094`, `101` y `118`) con todas las guardas de la 2.d en verde.
Pero el motor comun `vuelta159_motor_veredictos.py` escribe `clase` y `razon` y
la celda del `.md`, y NO TOCA EL CAMPO `cita`. Resultado: cuatro filas cuyo
campo `cita` sigue diciendo `clase C` sobre una fila que hoy es `D`.

ESO ES EXACTAMENTE LO QUE LA ADJUDICACION 6.6 DEL ACTA 158 VINO A CERRAR, con
esta letra: *las 3 de la vuelta 156 dejan de leer "clase C" en una fila que es
D*. La vuelta 159 lo arreglo para 65 filas con
`vuelta159_tarea4_unificar_cita.py`, y su guarda de cierre publico entonces
CERO citas cuya clase escrita no fuera la vigente. HOY VOLVERIA A SER CUATRO SI
NO SE ARREGLA: es una regresion de una adjudicacion ya cerrada, causada por mis
propias TAREAS 2.a y 2.b.

COMO LA CACE, y se dice porque importa para la proxima: NO la vi al escribir. La
delato el marcador del cierre, que publica `CIFRA citas con rastro de correccion`
y la dejo clavada en 106 cuando esta vuelta habia movido cuatro clases mas. Al
preguntarme por que no subia, conte las citas contra las clases vigentes y
salieron las cuatro.

QUE HACE ESTE INSTRUMENTO, Y SOLO ESTO:
  (a) recomputa LAS FILAS CUYA CLASE ESCRITA EN `cita` NO ES LA VIGENTE, sin
      teclear ninguna;
  (b) reescribe su `cita` a LA FORMA UNICA de la 6.6, la misma literal que uso
      la vuelta 159:
          LD-OPC05-NNN, clase <VIGENTE> [ANTES <ANTERIOR>, RECLASIFICADA EN LA
          VUELTA <N>: ver la razon]
  (c) deja constancia EN LA RAZON, por adicion y con el texto viejo entero como
      prefijo, de que la cita cambio y de que LA CLASE NO SE MUEVE;
  (d) y comprueba por assert que, al terminar, NINGUNA cita del registro tiene
      una clase escrita distinta de la vigente.

Y EL REMEDIO DE FONDO NO VIVE AQUI: vive en el motor. En la misma corrida se
anade a `vuelta159_motor_veredictos.py` la guarda que faltaba, para que un
cambio de clase que deje la cita mintiendo SALGA ROJO en el sitio en vez de
llegar al cierre. Un arreglo sin guarda solo aplaza la proxima.

USO:  python scripts/loop/vuelta160_tarea7b_unificar_cita.py
"""
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")

VUELTA = 160
MARCA = "UNIFICACION DEL CAMPO cita (VUELTA 160"


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def entradas():
    return [json.loads(x) for x in leer(REGISTRO).splitlines() if x.strip()]


def guardar(E):
    with io.open(REGISTRO, "w", encoding="utf-8", newline="\n") as fh:
        for e in E:
            fh.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")


def ld_de(e):
    return e["cita"].split(",")[0].strip()


def clase_escrita(cita):
    """La clase que el campo `cita` DICE, o None si no dice ninguna."""
    resto = cita.split(",", 1)[1] if "," in cita else ""
    m = re.search(r"clase ([A-D])", resto)
    return m.group(1) if m else None


def numstat(ruta_rel):
    r = subprocess.run(["git", "diff", "--numstat", "--", ruta_rel],
                       cwd=RAIZ, capture_output=True)
    linea = r.stdout.decode("utf-8", "replace").strip()
    if not linea:
        return 0, 0
    campos = linea.split("\t")
    return int(campos[0]), int(campos[1])


def main():
    print("=" * 78)
    print("VUELTA 160, TAREA 7.b: LAS CITAS QUE MI PROPIA TAREA 2 DEJO MINTIENDO")
    print("=" * 78)
    print("")

    E = entradas()
    antes_razon = {ld_de(e): e["razon"] for e in E}
    antes_clase = {ld_de(e): e["clase"] for e in E}

    print("A) LAS FILAS DESCUADRADAS, RECOMPUTADAS Y NO TECLEADAS")
    descuadradas = [e for e in E if clase_escrita(e["cita"]) != e["clase"]]
    print("   CIFRA filas del registro: %d" % len(E))
    print("   CIFRA citas cuya clase escrita NO es la vigente: %d" % len(descuadradas))
    for e in descuadradas:
        print("      %-16s la cita dice %s | la clase vigente es %s"
              % (ld_de(e), clase_escrita(e["cita"]), e["clase"]))
    print("   CIFRA que la guarda del cierre de la vuelta 159 publico: 0")
    print("   O SEA QUE ES UNA REGRESION DE ESTA VUELTA, Y ES MIA.")
    print("")

    print("B) LAS CITAS, REESCRITAS A LA FORMA UNICA DE LA 6.6 DEL ACTA 158")
    tocadas = 0
    for e in descuadradas:
        ld = ld_de(e)
        vieja = e["cita"]
        ant = clase_escrita(vieja)
        nueva = ("%s, clase %s [ANTES %s, RECLASIFICADA EN LA VUELTA %d: "
                 "ver la razon]" % (ld, e["clase"], ant, VUELTA))
        if MARCA in e["razon"]:
            print("   %-16s YA ESTABA" % ld)
            continue
        e["cita"] = nueva
        e["razon"] = e["razon"] + (
            "  [%s), ANADIDA SIN BORRAR NADA DE LO ANTERIOR: el campo `cita` de "
            "esta fila decia %r y desde hoy dice %r. LA CLASE NO SE MUEVE: la "
            "reclasificacion de C a D la hizo la TAREA 2 de esta misma vuelta y "
            "su caso esta escrito arriba; lo que cambia aqui es que la cita "
            "deja de leer `clase C` en una fila que es `D`, que es literalmente "
            "lo que la adjudicacion 6.6 del acta 158 vino a cerrar. La cazo el "
            "marcador del cierre, no mi mano.]" % (MARCA, vieja, nueva))
        tocadas += 1
        print("   %-16s %r" % (ld, nueva))
    guardar(E)
    print("")
    print("   CIFRA citas reescritas: %d" % tocadas)
    print("")

    print("C) LAS GUARDAS, MEDIDAS Y NO PROMETIDAS")
    D = entradas()
    assert len(D) == len(E) == 154, "el numero de lineas del registro se movio"
    print("   C.1 CIFRA filas: %d, las mismas antes y despues" % len(D))

    rotos = [ld_de(d) for d in D if not d["razon"].startswith(antes_razon[ld_de(d)])]
    print("   C.2 CIFRA razones cuyo texto viejo YA NO ES PREFIJO: %d" % len(rotos))
    assert not rotos, "PREFIJO ROTO en: %s" % ", ".join(rotos)
    print("       PREFIJO INTACTO en las %d." % len(D))

    movidas = [ld_de(d) for d in D if d["clase"] != antes_clase[ld_de(d)]]
    print("   C.3 CIFRA clases movidas por esta tarea: %d" % len(movidas))
    assert not movidas, "esta tarea NO mueve ninguna clase"
    print("       NINGUNA. Solo se reescribe el campo cita.")

    quedan = [ld_de(d) for d in D if clase_escrita(d["cita"]) != d["clase"]]
    print("   C.4 CIFRA citas cuya clase escrita NO es la vigente, AL TERMINAR: %d"
          % len(quedan))
    assert not quedan, "siguen descuadradas: %s" % ", ".join(quedan)
    print("       NINGUNA. UNA SOLA FORMA Y NINGUNA TAPA SU CORRECCION.")

    con_rastro = sum(1 for d in D if "[ANTES " in d["cita"])
    print("   C.5 CIFRA citas con rastro de correccion: %d" % con_rastro)
    print("       (la vuelta 159 cerro con 106; esta vuelta suma las %d de arriba)"
          % tocadas)

    mas, menos = numstat("docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl")
    print("   C.6 numstat del registro: mas %d, menos %d" % (mas, menos))
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
