# -*- coding: utf-8 -*-
r"""vuelta98_tarea4_prueba_mutacion.py . VUELTA 98, TAREA 4: PRUEBA DE MUTACION
DE LAS GUARDAS DEL ESCRITOR DE VEREDICTOS.

POR QUE ES OBLIGATORIA (EJECUTOR.md regla 1, EL CASO ROJO SE PRUEBA POR
MUTACION). El escritor publica seis guardas como prueba de que ningun id, clase
ni razon puede colarse mal. Ninguna se publica sin comprobar que CAE cuando se
le cambia el valor esperado.

  C1  control: los juicios reales                          espera VERDE (0 fallos)
  M1  una clase que no es A, B, C ni D                     espera ROJO
  M2  una razon vacia                                      espera ROJO
  M3  una razon sin ninguna cita del banco                 espera ROJO
  M4  una direccion que nombra un id ajeno al par          espera ROJO
  M5  una direccion sin la forma 'a -> b'                  espera ROJO
  M6  un puesto juzgado que el material no trae            espera ROJO
  M7  una direccion que apunta a si misma                  espera ROJO

LA M4 ES LA IMPORTANTE, y es la que hace imposible la especie de caida que esta
campana ya cazo tres veces: un id tecleado a mano que no corresponde al par.

LO QUE NO TIENE CASO ROJO AUTOMATICO, Y SE DECLARA EN VEZ DE FABRICARLO: LA
CLASE Y LA DIRECCION DE CADA PAR. Son lectura a mano contra el grafo y no hay en
el repo una segunda fuente independiente contra la que contrastarlas. Su control
es la relectura ciega del auditor. Estas mutaciones prueban EL ESCRITOR, no las
lecturas.

USO:
  python scripts/loop/vuelta98_tarea4_prueba_mutacion.py
"""
import copy
import importlib.util
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
sys.path.insert(0, LOOP)


def cargar(nombre):
    ruta = os.path.join(LOOP, nombre + ".py")
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = mod
    spec.loader.exec_module(mod)
    return mod


RESULTADOS = []


def caso(nombre, desc, esperado, fallos):
    obtenido = "ROJO" if fallos else "VERDE"
    ok = (esperado == obtenido)
    RESULTADOS.append((nombre, desc, esperado, obtenido, ok, fallos))
    print("  %-4s %-52s espera %-6s obtiene %-6s (%d fallo/s) %s"
          % (nombre, desc, esperado, obtenido, len(fallos), "OK" if ok else "FALLA"))


def main():
    esc = cargar("vuelta98_tarea4_escribir_tramo3")
    jui = cargar("vuelta98_tarea4_juicios")
    material = esc.leer_material()
    base = jui.JUICIOS
    p = min(base)                       # el primer puesto juzgado
    otro = sorted(base)[1]

    print("=" * 112)
    print("PRUEBA DE MUTACION, VUELTA 98 TAREA 4 (guardas del escritor de veredictos)")
    print("=" * 112)
    print("MATERIAL: %d pares parseados. JUICIOS: %d. Puesto que se muta: %d."
          % (len(material), len(base), p))
    print("NADA SE ESCRIBE EN NINGUN CASO: las mutaciones van sobre copias en memoria.")
    print()

    _, fallos, _ = esc.construir(base, material)
    caso("C1", "control: los juicios reales", "VERDE", fallos)

    m = copy.deepcopy(base); m[p]["clase"] = "Z"
    _, fallos, _ = esc.construir(m, material)
    caso("M1", "clase 'Z', que no es A, B, C ni D", "ROJO", fallos)

    m = copy.deepcopy(base); m[p]["razon"] = ""
    _, fallos, _ = esc.construir(m, material)
    caso("M2", "razon vacia", "ROJO", fallos)

    m = copy.deepcopy(base)
    m[p]["razon"] = ("Una razon larga y sin una sola cita de ninguna regla del banco, "
                     "que es exactamente lo que la guarda tiene que cazar.")
    _, fallos, _ = esc.construir(m, material)
    caso("M3", "razon sin ninguna cita del banco", "ROJO", fallos)

    m = copy.deepcopy(base)
    ajeno = material[otro]["hijo_de_la_bolsa"]
    m[p]["direccion"] = "%s -> %s" % (material[p]["madre_de_la_bolsa"], ajeno)
    _, fallos, _ = esc.construir(m, material)
    caso("M4", "direccion con un id ajeno al par (la guarda clave)", "ROJO", fallos)

    m = copy.deepcopy(base)
    m[p]["direccion"] = material[p]["madre_de_la_bolsa"]
    _, fallos, _ = esc.construir(m, material)
    caso("M5", "direccion sin la forma 'a -> b'", "ROJO", fallos)

    m = copy.deepcopy(base)
    m[9999] = {"clase": "D", "direccion": None,
               "razon": "Un puesto que el material no trae, con su cita del 9.6.2 puesta."}
    _, fallos, _ = esc.construir(m, material)
    caso("M6", "un puesto juzgado que el material no trae", "ROJO", fallos)

    m = copy.deepcopy(base)
    idm = material[p]["madre_de_la_bolsa"]
    m[p]["direccion"] = "%s -> %s" % (idm, idm)
    _, fallos, _ = esc.construir(m, material)
    caso("M7", "direccion que apunta a si misma", "ROJO", fallos)

    print()
    fallan = [r for r in RESULTADOS if not r[4]]
    mut = [r for r in RESULTADOS if r[0].startswith("M")]
    con = [r for r in RESULTADOS if r[0].startswith("C")]
    print("RECUENTO, contado de los propios casos corridos:")
    print("   casos totales     %d" % len(RESULTADOS))
    print("   controles         %d, verdes %d" % (len(con), sum(1 for r in con if r[4])))
    print("   mutaciones        %d, caen %d" % (len(mut), sum(1 for r in mut if r[4])))
    print("   casos que FALLAN  %d" % len(fallan))
    print()
    print("DECLARADO Y NO FABRICADO: la CLASE y la DIRECCION de cada par son lectura a mano")
    print("contra el grafo y NO TIENEN CASO ROJO AUTOMATICO. Su control es la relectura")
    print("ciega del auditor. Estas mutaciones prueban EL ESCRITOR, no las lecturas.")
    print()
    if fallan:
        print("ROJO: %d caso(s) no se comportan como se espera." % len(fallan))
        for r in fallan:
            print("   %s %s: esperaba %s y obtuvo %s" % (r[0], r[1], r[2], r[3]))
        return 1
    print("VERDE: el control pasa y las %d mutaciones caen. Ninguna guarda del escritor "
          "es una constante que se apruebe sola." % len(mut))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
