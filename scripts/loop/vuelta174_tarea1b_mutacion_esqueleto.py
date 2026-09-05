# -*- coding: utf-8 -*-
r"""vuelta174_tarea1b_mutacion_esqueleto.py . EL CASO POSITIVO POR MUTACION DEL
UNICO CAMBIO DE MAQUINA QUE TRAE `vuelta174_esqueleto_reporte.py`: QUE EL PASO 0
PREGUNTE POR EL REPORTE QUE VA A PISAR Y NO POR `VUELTA - 1`.

POR QUE EXISTE. `EJECUTOR.md` 1, clausula del 29 ago 2026: **NINGUN assert,
GUARDA O CASO ROJO SE PUBLICA COMO PRUEBA SIN HABER CORRIDO ANTES SU PRUEBA DE
MUTACION**. El esqueleto de la 174 endurece el sujeto del paso 0; un
endurecimiento que nadie puede tumbar no es una guarda, es una afirmacion.

DOS FAMILIAS DE CASOS, Y LAS DOS SOBRE FUNCIONES QUE NO ESCRIBEN NADA:

  (A) `vuelta_del_reporte_del_arbol()`, que es PURA: se le dan cabeceras de
      mentira y se comprueba que devuelve el numero cuando lo hay y **None**
      cuando no, en vez de adivinar uno.
  (B) `paso0_archivar_anterior.exigir_archivado()`, corrida en modo SOLO
      COMPROBACION y **apuntada a un directorio de trabajo temporal**, nunca al
      repo. Se le quita una pieza a la vez y se comprueba que cae por SU
      clausula nombrada: (b) el archivo no existe, (c) el archivo lleva otra
      vuelta, (d) el texto que se va a pisar no esta guardado. **La (d) es la
      que importa**, porque es la unica que mira lo que se destruiria, y es
      exactamente la que se caeria sola si alguien volviera a teclear el numero.

LO QUE ESTE ARNES NO TOCA: el repo. Los ficheros de mentira viven en un
directorio temporal que se crea y se borra aqui dentro; `docs/loop/REPORTE.md` y
`docs/loop/reportes/` no se leen ni se escriben en ningun caso.

SUJETO CONGELADO (vuelta 180, TAREA 2.b), Y AQUI HAY QUE DECIR ALGO MAS QUE EN
LOS OTROS TRES, PORQUE LA MEDICION NO DIO LO QUE EL ENCARGO SUPONIA. El encargo
de la 180 pone este arnes entre "LOS CUATRO QUE SI ABREN" un fichero vivo,
nombrando `REPORTE.md`. MEDIDO, NO ABRE NINGUNO: la unica lectura que la 179
registro es su propia evidencia, `vivo -> os.path.join(tmp, "REPORTE.md") |
io.open(vivo).read()`, y `tmp` es el `tempfile.mkdtemp(prefix="v174_mut_")` que
este mismo fichero crea y borra. O sea que el fichero que abre lo FABRICA EL, se
llama igual que el vivo y vive en un temporal. `docs/loop/REPORTE.md` y
`docs/loop/reportes/` no se leen ni se escriben en ninguna rama de este arnes, y
esa frase ya estaba escrita arriba antes de esta vuelta.

POR ESO AQUI NO HAY NADA QUE CONGELAR, Y LO QUE FALTABA ERA DECLARARLO: la
guarda del sujeto congelado buscaba la huella `REPORTE.md` en la maquina, la
encontraba en el nombre del fichero fabricado y no podia distinguir un sujeto
fabricado de uno vivo. La prueba de que su resultado no se mueve es que corre
DOS VECES y da lo mismo, y eso se mide en
`scripts/loop/vuelta180_tarea2b_prueba_de_congelacion.py`.

USO:
  python scripts/loop/vuelta174_tarea1b_mutacion_esqueleto.py
"""
import io
import os
import shutil
import sys
import tempfile

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import paso0_archivar_anterior as PASO0    # noqa: E402
import vuelta174_esqueleto_reporte as ESQ  # noqa: E402

CUERPO = (NL + NL + "lo que sea, el cuerpo del reporte de mentira." + NL)


def cabecera(n):
    return "# REPORTE DE LA VUELTA %d (ejecutor). FASE III." % n


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline=NL) as f:
        f.write(texto)


def correr():
    print("=" * 78)
    print("CASO POSITIVO POR MUTACION DEL PASO 0 DEL ESQUELETO DE LA 174")
    print("=" * 78)
    print("Los ficheros de mentira viven en un temporal. El repo NO se toca.")
    print("")
    verdes = 0
    rojos = 0

    def marcar(etiqueta, ok):
        nonlocal verdes, rojos
        print("   %-62s %s" % (etiqueta, "SI" if ok else "NO"))
        if ok:
            verdes += 1
        else:
            rojos += 1

    print("-" * 78)
    print("(A) vuelta_del_reporte_del_arbol(), PURA: ni lee ni escribe")
    print("-" * 78)
    casos_a = [
        ("una cabecera normal devuelve su numero",
         cabecera(172) + CUERPO, 172),
        ("otra cabecera devuelve OTRO numero (no hay constante escondida)",
         cabecera(168) + CUERPO, 168),
        ("un numero de tres cifras se lee entero",
         "# REPORTE DE LA VUELTA 1740" + CUERPO, 1740),
        ("sin almohadilla NO es cabecera",
         "REPORTE DE LA VUELTA 172" + CUERPO, None),
        ("si la cabecera no esta en la PRIMERA linea, no vale",
         "lo que sea" + NL + cabecera(172) + CUERPO, None),
        ("otro titulo cualquiera devuelve None",
         "# ACTA DEL AUDITOR, VUELTA 172" + CUERPO, None),
        ("sin numero devuelve None",
         "# REPORTE DE LA VUELTA (ejecutor)" + CUERPO, None),
        ("el texto vacio devuelve None", "", None),
    ]
    for etiqueta, texto, esperado in casos_a:
        dado = ESQ.vuelta_del_reporte_del_arbol(texto)
        marcar("%s -> %s" % (etiqueta, dado), dado == esperado)
    print("")

    tmp = tempfile.mkdtemp(prefix="v174_mut_")
    try:
        dir_arch = os.path.join(tmp, "reportes")
        os.makedirs(dir_arch)
        vivo = os.path.join(tmp, "REPORTE.md")

        print("-" * 78)
        print("(B) exigir_archivado(), SOLO COMPROBACION, sobre el temporal")
        print("-" * 78)

        # EL CASO VERDE PRIMERO, que es el que prueba que los rojos no son
        # rojos siempre.
        escribir(vivo, cabecera(172) + CUERPO)
        escribir(os.path.join(dir_arch, "REPORTE_V172.md"), cabecera(172) + CUERPO)
        ok, inf = PASO0.exigir_archivado(172, ruta_reporte=vivo,
                                         dir_archivo=dir_arch,
                                         ejecutar_archivador=False)
        marcar("VERDE cuando el archivado calza byte a byte con el que se pisa", ok)

        # (b) EL ARCHIVO NO EXISTE. Es EXACTAMENTE lo que pasaria tecleando 173.
        ok, inf = PASO0.exigir_archivado(173, ruta_reporte=vivo,
                                         dir_archivo=dir_arch,
                                         ejecutar_archivador=False)
        texto_inf = NL.join(inf)
        marcar("(b) cae si se pregunta por una vuelta SIN reporte archivado",
               (not ok) and "(b) no existe" in texto_inf)
        marcar("    y nombra su clausula (b), no otra",
               "(b) no existe" in texto_inf and "(d) EL TEXTO" not in texto_inf)

        # (c) EL ARCHIVO LLEVA OTRA VUELTA.
        escribir(os.path.join(dir_arch, "REPORTE_V171.md"), cabecera(999) + CUERPO)
        ok, inf = PASO0.exigir_archivado(171, ruta_reporte=vivo,
                                         dir_archivo=dir_arch,
                                         ejecutar_archivador=False)
        texto_inf = NL.join(inf)
        marcar("(c) cae si el fichero archivado lleva el reporte de OTRA vuelta",
               (not ok) and "(c) el archivo" in texto_inf)

        # (c bis) EL ARCHIVO NO EMPIEZA POR UNA CABECERA.
        escribir(os.path.join(dir_arch, "REPORTE_V170.md"), "lo que sea" + CUERPO)
        ok, inf = PASO0.exigir_archivado(170, ruta_reporte=vivo,
                                         dir_archivo=dir_arch,
                                         ejecutar_archivador=False)
        marcar("(c) cae si la primera linea del archivado no es cabecera",
               (not ok) and "(c) la primera linea" in NL.join(inf))

        # (d) LA QUE IMPORTA: el texto que se va a pisar NO esta guardado.
        escribir(vivo, cabecera(172) + CUERPO + "una linea mas que el archivo no tiene" + NL)
        ok, inf = PASO0.exigir_archivado(172, ruta_reporte=vivo,
                                         dir_archivo=dir_arch,
                                         ejecutar_archivador=False)
        texto_inf = NL.join(inf)
        marcar("(d) cae si el REPORTE.md del arbol NO esta guardado byte a byte",
               (not ok) and "(d) EL TEXTO QUE SE VA A PISAR NO ESTA GUARDADO" in texto_inf)
        marcar("    y publica los DOS sha256 para que se puedan cotejar",
               texto_inf.count("sha256") >= 2)

        # (d) NO SE ENGANA CON UN BYTE DE DIFERENCIA.
        escribir(vivo, cabecera(172) + CUERPO + " ")
        ok, inf = PASO0.exigir_archivado(172, ruta_reporte=vivo,
                                         dir_archivo=dir_arch,
                                         ejecutar_archivador=False)
        marcar("(d) cae tambien por UN SOLO byte de diferencia",
               (not ok) and "(d) EL TEXTO" in NL.join(inf))

        # LA VUELTA AL VERDE: se restaura y tiene que volver a pasar. Sin esto,
        # los rojos de arriba podrian ser un rojo permanente.
        escribir(vivo, cabecera(172) + CUERPO)
        ok, inf = PASO0.exigir_archivado(172, ruta_reporte=vivo,
                                         dir_archivo=dir_arch,
                                         ejecutar_archivador=False)
        marcar("y VUELVE al verde al restaurar el texto: no es un rojo permanente", ok)
        print("")

        print("-" * 78)
        print("(C) LA MUTACION QUE PRUEBA EL CAMBIO DE ESTA VUELTA")
        print("-" * 78)
        print("   El arbol tiene el reporte de la 172 y la vuelta anterior es la 173.")
        print("   Se corre la guarda con LOS DOS SUJETOS y se comparan:")
        escribir(vivo, cabecera(172) + CUERPO)
        ok_tecleado, _i = PASO0.exigir_archivado(173, ruta_reporte=vivo,
                                                 dir_archivo=dir_arch,
                                                 ejecutar_archivador=False)
        n_leido = ESQ.vuelta_del_reporte_del_arbol(
            io.open(vivo, encoding="utf-8").read())
        ok_leido, _i = PASO0.exigir_archivado(n_leido, ruta_reporte=vivo,
                                              dir_archivo=dir_arch,
                                              ejecutar_archivador=False)
        print("      sujeto TECLEADO (VUELTA - 1 = 173) -> %s"
              % ("VERDE" if ok_tecleado else "ROJO"))
        print("      sujeto LEIDO del fichero      (= %s) -> %s"
              % (n_leido, "VERDE" if ok_leido else "ROJO"))
        marcar("el sujeto tecleado da ROJO y el leido da VERDE: el cambio hace algo",
               (not ok_tecleado) and ok_leido)
        marcar("y el leido NO es un numero tecleado aqui: sale de la cabecera",
               n_leido == 172)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print("")
        print("   temporal borrado: %s -> existe: %s"
              % (tmp, "SI" if os.path.exists(tmp) else "NO"))

    print("")
    total = verdes + rojos
    print("=" * 78)
    print("CIFRA casos: %d | verdes: %d | rojos: %d" % (total, verdes, rojos))
    print("=" * 78)
    if rojos:
        print("ROJO: %d comprobacion(es) no se comportan." % rojos)
        return 1
    print("VERDE: las %d comprobaciones se comportan. La guarda del paso 0 cae por"
          % total)
    print("       cada una de sus clausulas cuando se le quita su pieza, y el sujeto")
    print("       leido del fichero pasa donde el tecleado se caeria.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(correr())
