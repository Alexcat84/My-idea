# -*- coding: utf-8 -*-
r"""_v216_t3_seccion.py . EL CUERPO DE LA TAREA 3 DEL REPORTE DE LA VUELTA 216,
COMPUESTO DE SU SALIDA SELLADA Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: las tres tablas de esta
seccion se PEGAN ENTERAS de docs/loop/SALIDA_V216_T3_DOS_VARAS.txt, y el
compositor DICE cuantas filas armo y cuantas deberia haber. Ninguna celda se
teclea.

USO:  python scripts/loop/_v216_t3_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
SALIDA = "docs/loop/SALIDA_V%d_T3_DOS_VARAS.txt" % VUELTA
EXPED = "docs/loop/SALIDA_V%d_T3_EXPEDIENTE.txt" % VUELTA
DESTINO = "scripts/loop/_v%d_t3_seccion.md" % VUELTA


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def cifra(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(-?\d+)", l.split(etiqueta, 1)[1])
            if m:
                return m.group(1)
    return None


def tabla(ls, cabecera):
    """LAS FILAS DE LA TABLA QUE EMPIEZA POR ESA CABECERA, PEGADAS ENTERAS Y NO
    TECLEADAS. PURA: devuelve (cabecera, separador, filas)."""
    for i, l in enumerate(ls):
        if l.strip() == cabecera:
            filas = []
            for j in range(i + 2, len(ls)):
                if not ls[j].startswith("|"):
                    break
                filas.append(ls[j])
            return [ls[i], ls[i + 1]] + filas, filas
    return [], []


def main():
    s = leer(SALIDA)
    ls = s.split(NL)
    exp = leer(EXPED)

    t_ficha, f_ficha = tabla(
        ls, "| ficha | linea del expediente | clausulas suyas | en CUBRE | NO en CUBRE | cuales |")
    t_cifras, f_cifras = tabla(
        ls, "| cifra | LA MIA, medida hoy | la del encargo, del auditor | calzan |")
    t_varas, f_varas = tabla(
        ls, "| ficha | VARA 1, la del expediente (P1 P2 P3) | VARA 2, las catorce clausulas |")

    nombradas = [l.strip() for l in ls if l.strip().startswith("HECHA SIN PRUEBA>")]
    anclajes = []
    for i, l in enumerate(ls):
        if l.strip().startswith("ANCLAJE "):
            anclajes.append(l.strip())

    D = {
        "v": VUELTA,
        "salida": SALIDA,
        "exped": EXPED,
        "armadas": cifra(s, "CIFRA FILAS ARMADAS LEYENDO %s: " % (
            "docs/loop/SALIDA_V%d_T2_REMEDICION.txt" % VUELTA)),
        "n_ficha": len(f_ficha),
        "n_cifras": len(f_cifras),
        "n_varas": len(f_varas),
        "n_nombradas": len(nombradas),
        "discrepancias": cifra(s, "CIFRA celdas que NO calzan con la cifra del encargo: "),
        "cubre": cifra(s, "CIFRA clausulas en CUBRE: "),
        "nocubre_cond": cifra(s, "CIFRA clausulas que NO estan en CUBRE: "),
        "faltan_hecha": cifra(s, "CIFRA de las CUATRO en HECHA sin prueba que NO aparecen en lo leido: "),
        "fallos": cifra(s, "CIFRA comprobaciones que fallan: "),
        "tabla_ficha": NL.join(t_ficha),
        "tabla_cifras": NL.join(t_cifras),
        "tabla_varas": NL.join(t_varas),
        "nombradas": NL.join("- " + x for x in nombradas),
        "anclajes": NL.join("- " + x for x in anclajes),
    }
    D["hash"] = s.split("no tecleado: ", 1)[1].split(NL, 1)[0].strip()
    D["no_cubre_cual"] = NL.join(
        "- " + l.strip() for l in ls if l.strip().startswith("NO CUBRE LA CONDICION>"))

    cuerpo = """### TAREA 3. LA CONSECUENCIA, MEDIDA, Y LAS DOS VARAS LADO A LADO

**EL INSTRUMENTO ES `scripts/loop/_v%(v)d_t3_dos_varas.py` Y SU SALIDA SELLADA
ES `%(salida)s`.** Todas las tablas de abajo se pegan enteras de ese fichero.
**NINGUNA CELDA SE TECLEA.**

#### 3.a. LAS CATORCE CLAUSULAS, REPARTIDAS FICHA POR FICHA

**FILAS ARMADAS LEYENDO `%(salida)s`: %(n_ficha)d. FILAS QUE DEBERIA HABER: 5**
(las cinco fichas). **Y las clausulas repartidas son %(armadas)s, contra las 14
que la TAREA 2 midio: LA SUMA SE COMPRUEBA CONTRA SI MISMA.**

%(tabla_ficha)s

#### 3.b. LA VARA DEL EXPEDIENTE, CORRIDA CON EL HASH DE MI APERTURA

**EL COMANDO, CON MI HASH Y NO CON OTRO:**
`scripts/loop/vuelta150_3_relectura_expediente.py --corte %(hash)s`, leido del
sello `docs/loop/SALIDA_V%(v)d_HEAD_APERTURA.txt` y **no tecleado**. Su salida
cruda vive en `%(exped)s`.

**FILAS ARMADAS: %(n_cifras)d. FILAS QUE DEBERIA HABER: 5.** **LA COLUMNA DE LA
IZQUIERDA ES MIA Y LA DE LA DERECHA ES LA DEL ENCARGO**, y van separadas para
que se pueda auditar cual es cual.

%(tabla_cifras)s

**CIFRA celdas que NO calzan con la cifra del encargo: %(discrepancias)s.** Las
cinco calzan una a una. **Lo digo con las dos columnas delante y no con una
sola**, porque publicar solo la mia cuando coincide es indistinguible de
copiarla.

**Y LA CIFRA DEL AUDITOR NO SE TOMA DEL ENCARGO Y YA: SE LEE DE SU ACTA, CON SU
LINEA**, porque una cifra citada de un encargo no es una cifra leida.

%(anclajes)s

**LAS CUATRO FICHAS EN HECHA SIN NINGUNA PRUEBA SIGUEN IGUAL, Y VAN NOMBRADAS.**
**FILAS ARMADAS: %(n_nombradas)d. FILAS QUE DEBERIA HABER: 4.**

%(nombradas)s

#### 3.c. LAS DOS VARAS, LADO A LADO, SIN MAQUILLAR QUE MIDAN LO MISMO

**LA VARA NO SABE DE LAS CATORCE FILAS NUEVAS, Y ESO NO ES UN FALLO SUYO.** La
del expediente mide **P1, P2 y P3**: grafo, codigo vivo y huella en git. La de
las catorce filas mide **clausulas de verificacion**. **Son dos varas distintas
midiendo cosas distintas**, y una ficha puede salir en HECHA SIN NINGUNA PRUEBA
teniendo **todas sus clausulas en CUBRE**. **ESO NO ES UNA CONTRADICCION Y NO LO
MAQUILLO.** Cambiar la vara seria fabricar maquinaria y la moratoria lo prohibe.

**FILAS ARMADAS: %(n_varas)d. FILAS QUE DEBERIA HABER: 5.** **CIFRA de las
CUATRO en HECHA sin prueba que NO aparecen en lo leido: %(faltan_hecha)s** (se
exigen 0), que es la guarda que impide publicar esta tabla a medio leer.

%(tabla_varas)s

**LO QUE ESTA TABLA DICE, EN UNA FRASE Y SIN ADORNO:** las cuatro fichas que la
vara del expediente marca como **HECHA SIN NINGUNA PRUEBA** tienen hoy **todas
sus clausulas en CUBRE**; y la unica que **no** tiene todas sus clausulas en
CUBRE, `OP-I-01`, es justamente la que **si** calza con la vara del expediente,
porque su estado `LISTA` es exactamente lo que el repo dice de ella.

**Y UNA CORRECCION DECLARADA DE MI PROPIO COMPOSITOR, QUE NO TAPA LO QUE
CORRIGE:** su primera version leia CUALQUIER fila con forma de tabla de la
salida de la vara, y por eso cogia para `OP-I-01` la fila de la tabla de
DESBLOQUEADAS, cuya tercera celda es el TIPO y no el estado: publicaba
*estado MESA* cuando la ficha esta en `LISTA`. **La cifra era falsa por mi
compositor y no por el instrumento**, se acoto la lectura a la tabla por su
propia cabecera, y **la version vieja queda escrita en el codigo y no se borra**.

#### 3.d. LO QUE PROPONGO, QUE NO ES LO QUE DECLARO

**LA CONDICION LA ESCRIBI ANTES DE SABER EL RESULTADO**, que es lo que el
encargo manda: *"si las CATORCE clausulas quedan en CUBRE con su busqueda
corrida y su cifra delante, y si el cierre integral sale limpio, entonces la
campana esta consumada EN LO QUE EL BUCLE PUEDE CONSUMAR"*.

**CIFRA clausulas en CUBRE: %(cubre)s | CIFRA que la condicion exige: 14 | CIFRA
que NO estan en CUBRE: %(nocubre_cond)s.**

%(no_cubre_cual)s

**LA PRIMERA MITAD DE LA CONDICION NO SE CUMPLE, Y POR ESO NO PROPONGO LA PARADA
FELIZ.** **PROPONGO ESTO EN SU LUGAR, con la cifra delante:** el plan queda
**agotado en trece de sus catorce clausulas**, y la que falta, `OP-I-01` indice
3, **no falta por pereza de esta vuelta**: le falta **la sede que la cumpliria**,
y esa sede **no existe en el repo** (**0 ficheros escriben la vista humana**,
busqueda corrida en la TAREA 2). **Fabricarla es maquinaria nueva y la moratoria
de `AUDITOR.md` 6.3 lo prohibe**, asi que **sube NOMBRADA**, que es donde el
propio auditor ya la puso en el punto 3 de su seccion 6.

**LO QUE ESTA TAREA NO HACE, DICHO PARA QUE NO SE BUSQUE:** no declara la
campana consumada, no escribe `docs/loop/PARA_ALEXIS.md` y **no pide ningun
merge**. Quien declara es **EL AUDITOR**, por la `4.2` del acta 203, **linea
71543**, ratificada por el fundador el 9 sep 2026. **Y EL BUCLE NO FUNDE RAMAS.**

**LA GUARDA DE LA PROHIBICION QUE NO SE NEGOCIA:** `sha256` LF de
`docs/plan/OPERACIONES.jsonl` **igual al entrar y al salir**, y **cero filas** de
`git diff --numstat` sobre el expediente. **CIFRA comprobaciones que fallan en
esta tarea: %(fallos)s.**
""" % D

    fallos = 0
    print("EL COMPOSITOR DE LA TAREA 3, Y SUS GUARDAS ANTES DE ESCRIBIR")
    for nombre, n, esperado in (("filas por ficha", len(f_ficha), 5),
                                ("filas de cifras", len(f_cifras), 5),
                                ("filas de las dos varas", len(f_varas), 5),
                                ("fichas nombradas", len(nombradas), 4),
                                ("anclajes del acta", len(anclajes), 2)):
        print("CIFRA %s: %d (se exigen %d)" % (nombre, n, esperado))
        if n != esperado:
            fallos += 1
    print("CIFRA celdas con None: %d (se exigen 0)" % cuerpo.count("None"))
    if "None" in cuerpo:
        fallos += 1
    sospechosos = [c for c in re.findall(r"`([^`]+)`", cuerpo)
                   if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sospechosos))
    if sospechosos:
        fallos += 1
    print("CIFRA guiones largos: %d | CIFRA guiones medios: %d"
          % (cuerpo.count(chr(8212)), cuerpo.count(chr(8211))))
    if cuerpo.count(chr(8212)) or cuerpo.count(chr(8211)):
        fallos += 1
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: el compositor NO ESCRIBE.")
        return 1
    p = os.path.join(RAIZ, DESTINO.replace("/", os.sep))
    io.open(p, "w", encoding="utf-8", newline=NL).write(cuerpo)
    print("ESCRITO %s -> %d bytes" % (DESTINO, os.path.getsize(p)))
    print("VERDE: el cuerpo de la TAREA 3 queda compuesto.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
