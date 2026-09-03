# -*- coding: utf-8 -*-
r"""vuelta164_tarea4_unificar_cita.py . TAREA 4 de la vuelta 164, SEGUNDA MITAD.

LA CITA DE LA `LD-OPC05-005` SE REESCRIBE A LA FORMA UNICA DE LA ADJUDICACION
6.6 DEL ACTA 158, PORQUE SU CLASE SE MOVIO EN ESTA MISMA VUELTA.

Y LA GUARDA DEL MOTOR HIZO SU TRABAJO, QUE ES LO QUE HAY QUE DECIR PRIMERO. La
TAREA 4 movio la clase de `C` a `D` con `vuelta159_motor_veredictos.aplicar`, y
ese motor escribe `clase`, `razon` y la celda del `.md` pero NO el campo `cita`.
En la vuelta 160 esa misma combinacion dejo CUATRO citas mintiendo y no la vio
nadie hasta el cierre; desde entonces el motor lleva dentro la guarda `C.7`, que
nacio de aquella caida. HOY LA GUARDA SALIO ROJA EN EL SITIO, con `exit 1` y
nombrando la fila: *"LA CITA MIENTE SOBRE SU PROPIA CLASE en 1 fila(s):
LD-OPC05-005"*. No llego al cierre, no la cazo el marcador y no hubo que
contarla a mano. Esto es una guarda vieja mordiendo, y se publica como tal.

QUE HACE ESTE INSTRUMENTO, Y SOLO ESTO:
  (a) recomputa LAS FILAS cuya clase escrita en `cita` no es la vigente, sin
      teclear ninguna;
  (b) reescribe su `cita` a la forma unica de la 6.6;
  (c) deja constancia EN LA RAZON, por adicion y con el texto viejo entero como
      prefijo, de que la cita cambio y de que LA CLASE NO SE MUEVE AQUI;
  (d) comprueba por assert que al terminar no queda ninguna descuadrada, que
      ninguna clase se movio y que el prefijo de las 154 razones esta intacto.

NO CLONA AL DE LA VUELTA 160: importa sus funciones puras
(`entradas`, `guardar`, `ld_de`, `clase_escrita`, `numstat`) y escribe su propia
prosa, porque la del 160 dice literalmente "la TAREA 2 de esta misma vuelta" y
aqui la mano es la TAREA 4. Una razon con la tarea equivocada dentro seria una
cifra falsa en el registro.

USO:  python scripts/loop/vuelta164_tarea4_unificar_cita.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta160_tarea7b_unificar_cita as U   # noqa: E402

VUELTA = 164
MARCA = "UNIFICACION DEL CAMPO cita (VUELTA 164"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 164, TAREA 4: LA CITA DE LA FILA CUYA CLASE SE MOVIO HOY")
    print("=" * 78)
    print("")

    E = U.entradas()
    antes_razon = {U.ld_de(e): e["razon"] for e in E}
    antes_clase = {U.ld_de(e): e["clase"] for e in E}

    print("A) LAS FILAS DESCUADRADAS, RECOMPUTADAS Y NO TECLEADAS")
    descuadradas = [e for e in E if U.clase_escrita(e["cita"]) != e["clase"]]
    print("   CIFRA filas del registro: %d" % len(E))
    print("   CIFRA citas cuya clase escrita NO es la vigente: %d" % len(descuadradas))
    for e in descuadradas:
        print("      %-16s la cita dice %s | la clase vigente es %s"
              % (U.ld_de(e), U.clase_escrita(e["cita"]), e["clase"]))
    print("   LA CAZO LA GUARDA C.7 DEL MOTOR, EN EL SITIO Y CON exit 1, y no el")
    print("   marcador del cierre como en la vuelta 160. Esa guarda nacio de")
    print("   aquella caida y hoy mordio.")
    print("")

    print("B) LAS CITAS, REESCRITAS A LA FORMA UNICA DE LA 6.6 DEL ACTA 158")
    tocadas = 0
    for e in descuadradas:
        ld = U.ld_de(e)
        vieja = e["cita"]
        ant = U.clase_escrita(vieja)
        nueva = ("%s, clase %s [ANTES %s, RECLASIFICADA EN LA VUELTA %d: "
                 "ver la razon]" % (ld, e["clase"], ant, VUELTA))
        if MARCA in e["razon"]:
            print("   %-16s YA ESTABA" % ld)
            continue
        e["cita"] = nueva
        e["razon"] = e["razon"] + (
            "  [%s), ANADIDA SIN BORRAR NADA DE LO ANTERIOR: el campo `cita` de "
            "esta fila decia %r y desde hoy dice %r. LA CLASE NO SE MUEVE AQUI: "
            "la reclasificacion de C a D la hizo la TAREA 4 de esta misma "
            "vuelta, la relectura conjunta que la adjudicacion 6.5 del acta 163 "
            "encarga, y su caso entero esta escrito arriba en esta misma razon. "
            "Lo que cambia en esta linea es solo que la cita deja de leer "
            "`clase C` en una fila que es `D`, que es lo que la adjudicacion 6.6 "
            "del acta 158 vino a cerrar. LA CAZO LA GUARDA C.7 DEL MOTOR "
            "`vuelta159_motor_veredictos.py`, en el sitio y con exit 1, no el "
            "marcador del cierre: esa guarda nacio en la vuelta 160 de una caida "
            "de esta misma especie y hoy es la primera vez que muerde.]"
            % (MARCA, vieja, nueva))
        tocadas += 1
        print("   %-16s %r" % (ld, nueva))
    U.guardar(E)
    print("")
    print("   CIFRA citas reescritas: %d" % tocadas)
    print("")

    print("C) LAS GUARDAS, MEDIDAS Y NO PROMETIDAS")
    D = U.entradas()
    assert len(D) == len(E) == 154, "el numero de lineas del registro se movio"
    print("   C.1 CIFRA filas: %d, las mismas antes y despues" % len(D))

    rotos = [U.ld_de(d) for d in D if not d["razon"].startswith(antes_razon[U.ld_de(d)])]
    print("   C.2 CIFRA razones cuyo texto viejo YA NO ES PREFIJO: %d" % len(rotos))
    assert not rotos, "PREFIJO ROTO en: %s" % ", ".join(rotos)
    print("       PREFIJO INTACTO en las %d." % len(D))

    movidas = [U.ld_de(d) for d in D if d["clase"] != antes_clase[U.ld_de(d)]]
    print("   C.3 CIFRA clases movidas por esta tarea: %d" % len(movidas))
    assert not movidas, "esta tarea NO mueve ninguna clase"
    print("       NINGUNA. Solo se reescribe el campo cita.")

    quedan = [U.ld_de(d) for d in D if U.clase_escrita(d["cita"]) != d["clase"]]
    print("   C.4 CIFRA citas cuya clase escrita NO es la vigente, AL TERMINAR: %d"
          % len(quedan))
    assert not quedan, "siguen descuadradas: %s" % ", ".join(quedan)
    print("       NINGUNA. UNA SOLA FORMA Y NINGUNA TAPA SU CORRECCION.")

    con_rastro = sum(1 for d in D if "[ANTES " in d["cita"])
    print("   C.5 CIFRA citas con rastro de correccion: %d" % con_rastro)
    print("       (el acta 163 midio 110 al abrir esta vuelta; esta fila YA")
    print("       llevaba rastro, asi que la cifra NO se mueve por reescribirla)")

    mas, menos = U.numstat("docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl")
    print("   C.6 numstat del registro: mas %d, menos %d" % (mas, menos))
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
