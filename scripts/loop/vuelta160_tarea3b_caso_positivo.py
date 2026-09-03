# -*- coding: utf-8 -*-
"""vuelta160_tarea3b_caso_positivo.py . TAREA 3.b DE LA VUELTA 160.

EL CASO POSITIVO POR MUTACION DEL REMEDIO DEL CHECK DE P.16. El encargo lo pide
con esta letra: SI UNA MUTACION ESCRIBE DE VERDAD EN `dataset/` O `docs/plan/`,
EL CHECK SIGUE SALIENDO ROJO.

Y SE PRUEBAN LAS DOS MITADES, PORQUE UNA SOLA NO SIRVE. Un remedio que solo
demuestre que sigue mordiendo no prueba que haya remediado nada (la version
vieja tambien mordia); y uno que solo demuestre que dejo de dar falsos rojos no
prueba que siga siendo una guarda. Van los CUATRO casos:

  CASO 1, DE UNIDAD, sobre `huella_de_contenido.py`. Una escritura REAL bajo
  `dataset/` cambia la huella, y `comparar` devuelve False Y NOMBRA que cambio
  el numero de ficheros. Borrado el fichero, la huella VUELVE al valor original,
  lo que prueba que la huella es funcion del contenido y de nada mas.

  CASO 2, DE EXTREMO A EXTREMO, EL ROJO QUE TIENE QUE SEGUIR CAYENDO. Se corre
  `vuelta89_tarea4_guarda_op_c05.py --caso-rojo` EN PROCESO con su funcion
  `contar` envuelta para que ESCRIBA DE VERDAD un fichero bajo `dataset/` entre
  las dos tomas de la huella. TIENE QUE SALIR ROJO, con su `SystemExit`.

  CASO 3, EL REMEDIO PROPIAMENTE DICHO, Y ES EL QUE PRUEBA QUE LA GUARDA DEJO DE
  MENTIR. Se ensucia `dataset/` ANTES de arrancar y el script NO escribe nada.
  El codigo viejo abortaba aqui (ancla 2 de la 6.7: se negaba a correr por
  suciedad que no era suya) y el remediado PASA. Y no se afirma que el viejo
  abortaba: se EVALUA su condicion literal sobre el mismo estado y se publica.

  CASO 4, LA CONTRAPRUEBA. Con `dataset/` limpio y sin escrituras inyectadas, el
  caso rojo sale VERDE. Sin esta, los tres de arriba no distinguirian un remedio
  de una guarda rota.

POR QUE SOBRE `vuelta89_tarea4_guarda_op_c05.py` Y NO SOBRE OTRO DE LOS DOCE: es
el DUODECIMO, el que el acta 159 tuvo que adjudicar dentro del alcance leyendo su
fuente, y el unico de los doce que llevaba las DOS anclas de la 6.7 con la
segunda en su forma mas pura (una parada por suciedad ajena). Probar el remedio
donde el defecto era mas grave vale mas que probarlo donde era mas comodo.

LA LIMPIEZA NO SE PROMETE, SE MIDE: el fichero sucio se borra en un `finally` y
al final se comprueba que la huella de `dataset/` es IDENTICA a la de la apertura
de este instrumento. Si no lo fuera, este script sale ROJO por su propia mano.

USO:  python scripts/loop/vuelta160_tarea3b_caso_positivo.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import huella_de_contenido as HC  # noqa: E402
import vuelta89_tarea4_guarda_op_c05 as G  # noqa: E402

RUTAS = ("dataset/",)
SUCIO = os.path.join(RAIZ, "dataset", "_V160_ESCRITURA_DE_PRUEBA.txt")
CONTENIDO = ("fichero de prueba de la TAREA 3.b de la vuelta 160. Si esto queda "
             "en el arbol, el instrumento que lo escribio fallo su limpieza y su "
             "propia guarda final lo dice.\n")


class Capturada(object):
    def __init__(self):
        self.trozos = []

    def write(self, s):
        self.trozos.append(s)
        return len(s)

    def flush(self):
        pass

    def valor(self):
        return "".join(self.trozos)


def ensuciar():
    with io.open(SUCIO, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(CONTENIDO)


def limpiar():
    if os.path.exists(SUCIO):
        os.remove(SUCIO)


def porcelain():
    r = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                       cwd=RAIZ, capture_output=True, text=True)
    return r.stdout


def correr_caso_rojo(envolver_contar=False):
    """Corre G.cmd_caso_rojo() en proceso. Devuelve (codigo, salida). Con
    envolver_contar, la funcion `contar` del script ESCRIBE DE VERDAD un fichero
    bajo dataset/ la primera vez que se la llama, que es entre las dos tomas de
    la huella."""
    real_contar = G.contar
    real_out = sys.stdout
    buf = Capturada()

    def contar_que_escribe(ruta_grafo, ruta_salida_jsonl):
        r = real_contar(ruta_grafo, ruta_salida_jsonl)
        ensuciar()
        return r

    if envolver_contar:
        G.contar = contar_que_escribe
    sys.stdout = buf
    codigo = 0
    try:
        codigo = G.cmd_caso_rojo() or 0
    except SystemExit as e:
        codigo = e.code if isinstance(e.code, int) else 1
        if isinstance(e.code, str):
            buf.write("\nSystemExit: %s\n" % e.code)
    finally:
        G.contar = real_contar
        sys.stdout = real_out
    return codigo, buf.valor()


def main():
    print("=" * 78)
    print("VUELTA 160, TAREA 3.b: EL CASO POSITIVO POR MUTACION DEL CHECK DE P.16")
    print("=" * 78)
    print("")

    limpiar()
    h_apertura = HC.huella(*RUTAS)
    print("HUELLA DE APERTURA DE ESTE INSTRUMENTO: sha256 %s sobre %d fichero(s)"
          % (h_apertura[0][:16], h_apertura[1]))
    print("")

    resultados = []
    try:
        # ------------------------------------------------------------------
        print("CASO 1, DE UNIDAD: una escritura REAL cambia la huella")
        print("-" * 78)
        a1 = HC.huella(*RUTAS)
        ensuciar()
        b1 = HC.huella(*RUTAS)
        ok1a, linea1a = HC.comparar(a1, b1, *RUTAS)
        limpiar()
        c1 = HC.huella(*RUTAS)
        ok1b, linea1b = HC.comparar(a1, c1, *RUTAS)
        print("   con el fichero escrito : %s" % linea1a)
        print("   tras borrarlo          : %s" % linea1b)
        ok1 = (not ok1a) and ok1b and ("numero de ficheros" in linea1a)
        print("   la huella CAE con la escritura: %s" % (not ok1a))
        print("   y VUELVE al valor original al borrarla: %s" % ok1b)
        print("   y el rojo NOMBRA que cambio el numero de ficheros: %s"
              % ("numero de ficheros" in linea1a))
        print("   VEREDICTO: %s" % ("OK" if ok1 else "ROJO"))
        resultados.append(("CASO 1, la huella cae con una escritura real y vuelve", ok1))
        print("")

        # ------------------------------------------------------------------
        print("CASO 2, DE EXTREMO A EXTREMO: con una escritura REAL inyectada,")
        print("el caso rojo de vuelta89_tarea4_guarda_op_c05.py SIGUE SALIENDO ROJO")
        print("-" * 78)
        limpiar()
        codigo2, salida2 = correr_caso_rojo(envolver_contar=True)
        limpiar()
        nombra2 = "quedo con cambios tras el caso rojo" in salida2
        huella_roja = "P.16 ROJO" in salida2
        ok2 = codigo2 != 0 and nombra2 and huella_roja
        print("   codigo de salida: %r (distinto de cero: %s)" % (codigo2, codigo2 != 0))
        print("   la salida trae la linea de rojo de la huella: %s" % huella_roja)
        print("   y nombra el motivo correcto: %s" % nombra2)
        for ln in salida2.splitlines():
            if "P.16" in ln or "SystemExit" in ln:
                print("      | %s" % ln[:150])
        print("   VEREDICTO: %s" % ("OK" if ok2 else "ROJO"))
        resultados.append(("CASO 2, una escritura real SIGUE cayendo en rojo", ok2))
        print("")

        # ------------------------------------------------------------------
        print("CASO 3, EL REMEDIO: con dataset/ SUCIO DE ANTES y sin escrituras")
        print("del script, el caso rojo PASA (el codigo viejo abortaba aqui)")
        print("-" * 78)
        limpiar()
        ensuciar()
        sucio_visto = porcelain()
        # LA CONDICION LITERAL DEL CODIGO VIEJO, EVALUADA Y NO AFIRMADA. Era:
        #     if r_antes.stdout.strip(): raise SystemExit("ROJO: dataset/ ya tenia
        #     cambios antes del caso rojo: no se corre sobre un arbol sucio")
        viejo_habria_abortado = bool(sucio_visto.strip())
        codigo3, salida3 = correr_caso_rojo(envolver_contar=False)
        limpiar()
        ok3 = (codigo3 == 0) and viejo_habria_abortado
        print("   git status -- dataset/ antes de arrancar: %r" % sucio_visto.strip()[:120])
        print("   LA CONDICION DEL CODIGO VIEJO, EVALUADA sobre ese mismo estado")
        print("   (bool(r_antes.stdout.strip())): %s" % viejo_habria_abortado)
        print("   o sea que el codigo viejo HABRIA ABORTADO sin correr nada.")
        print("   codigo de salida del remediado: %r" % codigo3)
        for ln in salida3.splitlines():
            if "P.16" in ln:
                print("      | %s" % ln[:150])
        print("   VEREDICTO: %s" % ("OK" if ok3 else "ROJO"))
        resultados.append(("CASO 3, la suciedad ajena YA NO tumba la guarda", ok3))
        print("")

        # ------------------------------------------------------------------
        print("CASO 4, LA CONTRAPRUEBA: limpio y sin escrituras, sale VERDE")
        print("-" * 78)
        limpiar()
        codigo4, salida4 = correr_caso_rojo(envolver_contar=False)
        verde4 = "IDENTICA antes y despues" in salida4
        ok4 = (codigo4 == 0) and verde4
        print("   codigo de salida: %r" % codigo4)
        print("   la huella sale IDENTICA antes y despues: %s" % verde4)
        for ln in salida4.splitlines():
            if "P.16" in ln:
                print("      | %s" % ln[:150])
        print("   VEREDICTO: %s" % ("OK" if ok4 else "ROJO"))
        resultados.append(("CASO 4, contraprueba en limpio, sale verde", ok4))
        print("")
    finally:
        limpiar()

    # ----------------------------------------------------------------------
    print("=" * 78)
    h_cierre = HC.huella(*RUTAS)
    limpio, linea_limpieza = HC.comparar(h_apertura, h_cierre, *RUTAS)
    print("LA LIMPIEZA, MEDIDA Y NO PROMETIDA:")
    print("   %s" % linea_limpieza)
    resultados.append(("LA LIMPIEZA: dataset/ vuelve identico a la apertura", limpio))
    print("")
    buenas = sum(1 for _, ok in resultados if ok)
    for nombre, ok in resultados:
        print("  %-5s %s" % ("OK" if ok else "ROJO", nombre))
    print("")
    print("CIFRA casos del arnes: %d" % len(resultados))
    print("CIFRA casos que se comportan: %d" % buenas)
    print("=" * 78)
    if buenas != len(resultados):
        print("ROJO: %d de %d no se comportan." % (len(resultados) - buenas, len(resultados)))
        return 1
    # CORRECCION DECLARADA (vuelta 160, TAREA 3.b, cazada por mi al releer la
    # salida): la linea vieja imprimia el literal "%d" porque le faltaba su
    # operando. Queda tachada y legible:
    #     ~~print("VERDE: los %d se comportan. EL CHECK SIGUE MORDIENDO UNA ESCRITURA REAL Y")~~
    print("VERDE: los %d se comportan. EL CHECK SIGUE MORDIENDO UNA ESCRITURA REAL Y"
          % buenas)
    print("YA NO MUERDE A QUIEN NO ESCRIBIO.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
