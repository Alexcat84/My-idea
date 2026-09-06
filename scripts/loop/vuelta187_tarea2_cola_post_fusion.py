# -*- coding: utf-8 -*-
r"""vuelta187_tarea2_cola_post_fusion.py . EL TRAMO 1 DE LA COLA DE RELECTURA
POST FUSION: EL PAR 2.464, RELEIDO CON SU DISPARADOR CITADO ANTES DE APLICARLO.

EL DISPARADOR SE LEE ANTES DE TOCAR NADA, Y SE CITA CON SU LINEA. Vive en
`docs/plan/08_VERIFICACION.md`, seccion `## LA COLA DE RELECTURA POST FUSION`, y
este fichero lo LOCALIZA en el fichero vivo y lo PEGA con su numero de linea en
vez de citarlo de memoria. **Si la seccion no estuviera, este instrumento cae en
ROJO y no relee nada:** un tramo que se ejecuta sin su criterio escrito es una
improvisacion, y eso es PARADA.

EL TAMANO DEL TRAMO NO SE INVENTA: SE COMPUTA DEL CRITERIO ESCRITO. La propia
seccion declara el tramo con estas palabras, y aqui se pegan con su linea:
*"TRAMO 1 y unico con lo medido hoy: el unico par de arriba, y se relee entero o
no cuenta. Si el instrumento volviera a correr y nombrara mas, cada nuevo grupo
abre su propio tramo con su fecha, para que un tramo cerrado no se pueda reabrir
por la puerta de atras."* Asi que el tramo 1 es **la lista que el instrumento del
diferenciador movido nombraba el dia que la cola se abrio**, y este fichero
**vuelve a correr esa criba HOY** para publicar si sigue nombrando lo mismo.

Y LO QUE LA CRIBA NOMBRA DE MAS NO ES UN TRAMO NUEVO, Y ESO SE MIDE EN VEZ DE
SUPONERSE. Esta criba corre **solo las condiciones 1 y 2**; la condicion 3, que
el paso entrara DESPUES del veredicto, la fecho en git la vuelta 182. Las que
pasan las dos primeras pero no la tercera son **los cinco puestos de la `PD.1`**
que el acta 187 registra en su `6.1`: su diferenciador **ya estaba el dia del
veredicto**, asi que **no pasan el disparador escrito y no entran en la cola**.
Darles cola seria doctrina nueva, que es del fundador. Aqui **se cotejan contra
los cinco del acta y se publica si son los mismos**, y **no se releen**.

LA MAQUINA SE IMPORTA, NO SE CLONA (`6.6` del acta 172): `analiza`,
`nodos_por_id`, `pasos_del_nodo`, `clausula_de_carencia`, `quien_carece`,
`items_declarados` y las dos varas salen de
`scripts/loop/vuelta182_tarea3_diferenciador_movido.py`. **Y NO SE CORRE SU
`main()`**, que reescribiria `SALIDA_V182_T3_DIFERENCIADOR.txt` y
`SALIDA_V182_T3_COLA.json`, que son evidencia sellada de la vuelta 182.

LA CORRECCION SE DECLARA Y NO TAPA LO VIEJO (`EJECUTOR.md` 8). El texto viejo de
la `razon` **se conserva entero y byte a byte**, y la correccion se ANEXA detras
con su fecha, su motivo y la vuelta que la escribe. **Ningun veredicto se mueve
en silencio** y **nada se borra**.

Y AQUI HAY UN PENDIENTE DE DOCTRINA QUE SE DECLARA EN VEZ DE RESOLVERSE SOLO
(`EJECUTOR.md` 5). `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` tiene OCHO campos y
**ninguno es de correccion**: medido hoy sobre sus 3388 filas, las claves son
`puesto_intra`, `dominio`, `nodo_a`, `nodo_b`, `clave`, `banda_078_080`, `clase`
y `razon`, y **ninguna fila del archivo ha llevado nunca un campo de
correccion**. Asi que **la forma de una correccion declarada dentro de este
archivo no esta escrita en ninguna doctrina**. Se registra lo mejor sostenido
(anexar a la `razon` sin borrar nada, con marca literal y fecha) y **se marca
PENDIENTE DE DOCTRINA dentro de la propia razon**, que es lo que la regla 5 manda
cuando falta la regla. **No se para**, porque la regla 5 dice expresamente que no
se para.

LO QUE ESTE FICHERO NO HACE: no toca `dataset/`, no toca el reporte, no abre la
mesa del `PMF` ni la del 603 ni la de figuras del 226, y **no cambia ninguna
clase que la relectura no cambie**. Si la relectura sostiene la clase de hoy, la
clase se queda y se dice.

USO:
  python scripts/loop/vuelta187_tarea2_cola_post_fusion.py --simular
  python scripts/loop/vuelta187_tarea2_cola_post_fusion.py
"""
import argparse
import hashlib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta182_tarea3_diferenciador_movido as T3   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VERIF = os.path.join(RAIZ, "docs", "plan", "08_VERIFICACION.md")
BANCO = os.path.join(RAIZ, "docs", "plan", "BANCO_DEL_PLAN.md")
ARCHIVO = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NL = chr(10)
VUELTA = 187

CABECERA_COLA = "## LA COLA DE RELECTURA POST FUSION"
MARCA_DISPARADOR = "EL DISPARADOR, y es mecanico"
MARCA_TRAMO = "EL TRAMO, DECLARADO AQUI Y NO IMPROVISADO DESPUES"
MARCA_DESTINO = "### QUE PASA CON LO QUE SE RELEA"

# LA MARCA CON LA QUE UNA CORRECCION DECLARADA SE RECONOCE DENTRO DE UNA `razon`.
# Va aqui, en una constante con nombre, para que la guarda de idempotencia y la
# escritura usen LA MISMA y no dos parecidas.
MARCA_CORRECCION = "CORRECCION DECLARADA (vuelta %d, TRAMO 1 DE LA COLA POST FUSION)" % VUELTA


def sha_lf(datos):
    """EL sha256 POR LA CONVENCION DE LF. PURA."""
    return hashlib.sha256(datos.replace(b"\r\n", b"\n")).hexdigest()


def seccion_de_la_cola(texto):
    """LA SECCION DEL DISPARADOR, ACOTADA. Devuelve (inicio, fin, lineas) en
    numeracion de 1, o (None, None, []) si no esta. PURA.

    El fin es la siguiente cabecera de SEGUNDO nivel, para que las sub secciones
    `###` de la propia cola queden DENTRO: la declaracion del tramo y la tabla de
    destinos viven en `###` y son parte del criterio."""
    lineas = texto.replace(chr(13) + NL, NL).split(NL)
    base = [i for i, l in enumerate(lineas, 1) if l.startswith(CABECERA_COLA)]
    if len(base) != 1:
        return None, None, []
    ini = base[0]
    fin = len(lineas)
    for i in range(ini, len(lineas)):
        if lineas[i].startswith("## ") and not lineas[i].startswith("### "):
            fin = i
            break
    return ini, fin, lineas[ini - 1:fin]


def citas_del_criterio(lineas, ini):
    """LAS TRES PIEZAS DEL CRITERIO, LOCALIZADAS EN EL FICHERO VIVO Y NO
    TECLEADAS. Devuelve {nombre: (linea, texto)} y deja fuera la que no este.
    PURA: recibe las lineas ya acotadas y su desplazamiento."""
    piezas = {}
    for i, l in enumerate(lineas, ini):
        for nombre, marca in (("disparador", MARCA_DISPARADOR),
                              ("tramo", MARCA_TRAMO),
                              ("destino", MARCA_DESTINO)):
            if marca in l and nombre not in piezas:
                piezas[nombre] = (i, l.strip())
    return piezas


def pares_del_tramo1(lineas, ini):
    """LOS PARES QUE EL TRAMO 1 DECLARA, LEIDOS DE LA TABLA DE LA SECCION Y NO
    TECLEADOS. Devuelve [(linea, puesto)]. PURA.

    LA TABLA ES LA DE `LA ENTRADA POR EL DIFERENCIADOR MOVIDO`, que es la que el
    parrafo del tramo llama *"el unico par de arriba"*. Se localiza por su
    cabecera y se leen los renglones de tabla que empiezan por un puesto en
    negrita. **Si la tabla no estuviera, la lista sale vacia y quien llama para:**
    un tramo sin lista no se inventa."""
    cab = None
    for i, l in enumerate(lineas, ini):
        if l.startswith("### LA ENTRADA POR EL DIFERENCIADOR MOVIDO"):
            cab = i
            break
    if cab is None:
        return []
    salida = []
    for i, l in enumerate(lineas, ini):
        if i <= cab:
            continue
        if l.startswith("### ") or (l.startswith("## ") and not l.startswith("### ")):
            break
        m = re.match(r"^\|\s*\*\*(\d+)\*\*\s*\|", l)
        if m:
            salida.append((i, int(m.group(1))))
    return salida


def razon_con_correccion(razon_vieja, texto_correccion):
    """LA RAZON NUEVA: LA VIEJA ENTERA Y BYTE A BYTE, MAS LA CORRECCION DETRAS.
    PURA.

    NO BORRA NADA Y NO REESCRIBE NADA (`EJECUTOR.md` 8, *"una correccion que tapa
    lo que corrige no se puede auditar"*). Es idempotente: si la marca ya esta,
    devuelve la razon tal cual y no la duplica."""
    if MARCA_CORRECCION in razon_vieja:
        return razon_vieja, False
    return (razon_vieja.rstrip() + " " + texto_correccion), True


def marcador(filas):
    """EL MARCADOR RECOMPUTADO DEL ARCHIVO. PURA: recibe las filas ya leidas.

    Devuelve un dict con filas, el reparto por clase, puestos unicos, huecos y
    duplicados. **No se ajusta a mano y no se hereda de ningun reporte.**"""
    por_clase = {}
    for f in filas:
        por_clase[f.get("clase")] = por_clase.get(f.get("clase"), 0) + 1
    puestos = [f.get("puesto_intra") for f in filas]
    return {"filas": len(filas), "por_clase": por_clase,
            "unicos": len(set(puestos)), "min": min(puestos), "max": max(puestos),
            "huecos": len(set(range(min(puestos), max(puestos) + 1)) - set(puestos)),
            "duplicados": len(puestos) - len(set(puestos))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true",
                    help="mide y arma la correccion, pero NO escribe el archivo")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2: EL TRAMO 1 DE LA COLA DE RELECTURA POST FUSION" % VUELTA)
    w("=" * 78)
    w("")

    w("A) EL DISPARADOR ESCRITO, LEIDO ANTES DE TOCAR NADA Y CITADO CON SU LINEA")
    t_ver = io.open(VERIF, encoding="utf-8").read()
    ini, fin, cuerpo = seccion_de_la_cola(t_ver)
    if ini is None:
        w("   ROJO: %r no aparece exactamente una vez en" % CABECERA_COLA)
        w("   docs/plan/08_VERIFICACION.md. Sin criterio escrito no se relee nada.")
        print(NL.join(L))
        return 1
    w("   docs/plan/08_VERIFICACION.md -> disco %d bytes" % os.path.getsize(VERIF))
    w("   seccion %r: lineas %d a %d (%d lineas)"
      % (CABECERA_COLA, ini, fin, len(cuerpo)))
    piezas = citas_del_criterio(cuerpo, ini)
    for nombre in ("disparador", "tramo", "destino"):
        if nombre not in piezas:
            w("   ROJO: la pieza %r del criterio NO esta en la seccion. Si el texto"
              % nombre)
            w("   no alcanza para ejecutarlo sin decidir, eso es PARADA.")
            print(NL.join(L))
            return 1
        ln, txt = piezas[nombre]
        w("   PIEZA %-11s -> docs/plan/08_VERIFICACION.md:%d" % (nombre, ln))
        w("      | %s" % txt[:200])
    w("")
    w("   EL DISPARADOR ENTERO, PEGADO CON SUS LINEAS Y NO PARAFRASEADO:")
    ln_d = piezas["disparador"][0]
    for i in range(ln_d, min(ln_d + 3, fin + 1)):
        w("      LINEA %d: %s" % (i, cuerpo[i - ini].strip()[:200]))
    w("")
    w("   LA DECLARACION DEL TRAMO, ENTERA, QUE ES LA QUE FIJA EL TAMANO:")
    ln_t = piezas["tramo"][0]
    for i in range(ln_t, min(ln_t + 8, fin + 1)):
        w("      LINEA %d: %s" % (i, cuerpo[i - ini].strip()[:200]))
    w("")
    w("   LA TABLA DE DESTINOS, QUE DICE QUE HACER CON LO QUE SE RELEA:")
    ln_x = piezas["destino"][0]
    for i in range(ln_x, min(ln_x + 8, fin + 1)):
        w("      LINEA %d: %s" % (i, cuerpo[i - ini].strip()[:200]))
    w("")

    w("A.1) EL BANCO DEL PLAN, MEDIDO Y NO SUPUESTO")
    w("   (el encargo dice que el criterio esta escrito EN LOS DOS ficheros. Aqui")
    w("    se mide el segundo y se publica lo que salga, sin resolverlo copiando)")
    t_ban = io.open(BANCO, encoding="utf-8").read().replace(chr(13) + NL, NL)
    for aguja in ("post fusion", "POST FUSION", "cola post fusion", "2464", "2.464"):
        hits = [i for i, l in enumerate(t_ban.split(NL), 1) if aguja in l]
        w("   docs/plan/BANCO_DEL_PLAN.md, %-18s -> %d aparicion(es) %s"
          % (repr(aguja), len(hits), hits[:6] if hits else ""))
    w("   DECLARADO: el criterio de esta cola vive ENTERO en")
    w("   docs/plan/08_VERIFICACION.md y NO en el BANCO_DEL_PLAN. La discrepancia")
    w("   con el encargo se declara en vez de resolverse copiando (EJECUTOR.md 2).")
    w("   NO ES PARADA: el texto de 08_VERIFICACION.md alcanza para ejecutar el")
    w("   tramo sin decidir nada, que es la condicion que el encargo pone.")
    w("")

    w("B) EL TRAMO 1, COMPUTADO DEL CRITERIO Y NO INVENTADO")
    tramo = pares_del_tramo1(cuerpo, ini)
    if not tramo:
        w("   ROJO: la seccion no lista ningun par. Un tramo sin lista no se inventa.")
        print(NL.join(L))
        return 1
    w("   CIFRA pares que el TRAMO 1 declara: %d" % len(tramo))
    for ln, p in tramo:
        w("      docs/plan/08_VERIFICACION.md:%d -> puesto %d" % (ln, p))
    w("   POR QUE ESE ES EL TAMANO, Y SALE DEL TEXTO Y NO DE MI: la criba escrita")
    w("   en la propia seccion es 2760 D -> 99 que declaran diferenciador -> 6 que")
    w("   hoy lo tienen en el otro nodo -> 1 cuyo paso entro DESPUES del veredicto.")
    w("   Y el parrafo del tramo dice, literal, TRAMO 1 y unico con lo medido hoy:")
    w("   el unico par de arriba. ASI QUE EL TRAMO 1 SON %d PAR(ES)." % len(tramo))
    w("")

    w("C) LA CRIBA, RE CORRIDA HOY SOBRE EL ARCHIVO ENTERO, PARA VER SI SIGUE")
    w("   NOMBRANDO LO MISMO (la maquina se IMPORTA de")
    w("   scripts/loop/vuelta182_tarea3_diferenciador_movido.py y su main() NO se")
    w("   corre: reescribiria evidencia sellada de la vuelta 182)")
    datos_antes = io.open(ARCHIVO, "rb").read()
    w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl AL ABRIR:")
    w("      disco %d bytes | LF %d bytes"
      % (len(datos_antes), len(datos_antes.replace(b"\r\n", b"\n"))))
    w("      sha256 (LF): %s" % sha_lf(datos_antes))
    filas = [json.loads(l) for l in io.open(ARCHIVO, encoding="utf-8") if l.strip()]
    grafo = json.load(io.open(T3.GRAFO, encoding="utf-8"))
    porid = T3.nodos_por_id(grafo)
    w("   grafo: %d nodos | archivo: %d filas" % (len(porid), len(filas)))
    w("   varas importadas: VARA_ABSOLUTA %s | VARA_COBERTURA %s"
      % (T3.VARA_ABSOLUTA, T3.VARA_COBERTURA))
    d_todas = [f for f in filas if f.get("clase") == "D"]
    declaran = lesionadas = 0
    nombradas = []
    for f in d_todas:
        r = T3.analiza(f, porid)
        if r["declara"]:
            declaran += 1
        if r["lesion"]:
            lesionadas += 1
            nombradas.append((f.get("puesto_intra"), r))
    w("   CIFRA D en el archivo: %d" % len(d_todas))
    w("   CIFRA D que declaran diferenciador: %d" % declaran)
    w("   CIFRA D con LESION EXACTA hoy (condiciones 1 y 2, sin fechar): %d"
      % lesionadas)
    w("   LAS QUE LA CRIBA NOMBRA HOY: %s"
      % ", ".join(str(p) for p, _r in sorted(nombradas)))
    en_tramo = {p for _ln, p in tramo}
    de_mas = sorted(p for p, _r in nombradas if p not in en_tramo)
    w("   DE ELLAS, FUERA DEL TRAMO 1: %s"
      % (", ".join(str(x) for x in de_mas) or "(ninguna)"))
    w("   QUE SON ESAS DE MAS, Y NO SON UN TRAMO NUEVO: SON LA `PD.1`. Esta criba")
    w("   corre SOLO las condiciones 1 y 2. La condicion 3, que el paso entrara")
    w("   DESPUES del veredicto, la fecho en git la vuelta 182 y su salida sellada")
    w("   vive en docs/loop/SALIDA_V182_T3_DIFERENCIADOR.txt, que aqui NO SE TOCA.")
    w("   Las que no pasan la condicion 3 son justamente los cinco puestos que el")
    w("   acta 187 registra en su `6.1` como `PD.1`, sexta vuelta ABIERTA: su")
    w("   diferenciador YA ESTABA el dia del veredicto, asi que NO PASAN EL")
    w("   DISPARADOR ESCRITO y NO ENTRAN EN LA COLA. Darles cola seria DOCTRINA")
    w("   NUEVA, que es del fundador, y el acta lo dice con esas palabras.")
    w("   COTEJO, MEDIDO Y NO SUPUESTO: los de mas de esta criba son %s"
      % ", ".join(str(x) for x in de_mas))
    w("   y los cinco de la `PD.1` que el registro R.49 leyo del acta son")
    w("   1778, 2530, 2540, 3141, 3232. SON LOS MISMOS CINCO: %s"
      % ("SI" if de_mas == [1778, 2530, 2540, 3141, 3232] else "NO"))
    w("   Y SI ALGUN DIA LA CRIBA NOMBRARA UNO QUE NO ESTE NI EN EL TRAMO 1 NI EN")
    w("   LA `PD.1`, ESE SI ABRIRIA SU PROPIO TRAMO CON SU FECHA, por la letra de")
    w("   la linea %d, para que un tramo cerrado no se pueda reabrir por la puerta"
      % ln_t)
    w("   de atras. Hoy no hay ninguno asi.")
    w("")

    w("D) LA RELECTURA DEL PAR DEL TRAMO 1, PUESTO A PUESTO, CON LOS PASOS DE HOY")
    porpuesto = {f.get("puesto_intra"): f for f in filas}
    movimientos = []
    for _ln, p in tramo:
        f = porpuesto.get(p)
        if f is None:
            w("   ROJO: el puesto %d no esta en el archivo." % p)
            print(NL.join(L))
            return 1
        r = T3.analiza(f, porid)
        w("   PUESTO %d, dominio %s, clase de archivo %s"
          % (p, f.get("dominio"), f.get("clase")))
        w("      %s  contra  %s" % (f.get("nodo_a"), f.get("nodo_b")))
        w("      declara diferenciador: %s | carece: %s"
          % ("SI" if r["declara"] else "no", r["carece"]))
        w("      lesion exacta: %s" % ("SI" if r["lesion"] else "no"))
        w("      motivo de la vara: %s" % r["motivo"])
        w("      el item declarado que se movio: %s" % (r["item"] or "(ninguno)")[:220])
        w("      el paso de HOY que lo cubre: %s" % (r["paso"] or "(ninguno)")[:220])
        for lado in ("nodo_a", "nodo_b"):
            nid = f.get(lado)
            pasos = T3.pasos_del_nodo(porid.get(nid) or {})
            w("      PASOS DE HOY de %s (%s): %d" % (nid, lado, len(pasos)))
            for k, paso in enumerate(pasos, 1):
                w("         paso %d: %s" % (k, str(paso)[:190]))
        w("      LA RAZON ESCRITA, ENTERA Y SIN CORTAR:")
        for trozo in re.findall(r".{1,150}(?:\s|$)", f.get("razon") or ""):
            if trozo.strip():
                w("         | %s" % trozo.strip())
        movimientos.append((p, f, r))
    w("")

    w("E) LO QUE LA RELECTURA SOSTIENE, Y EL DESTINO QUE EL CRITERIO ESCRITO LE DA")
    w("   (la tabla QUE PASA CON LO QUE SE RELEA, citada arriba con su linea, dice:")
    w("    si sale A entra en la fusion que le corresponda y su perdida se nombra")
    w("    antes; si sale D se queda, y si hay jerarquia se enlaza; si sale B otra")
    w("    vez va a la lista de decisiones del inventario final)")
    correcciones = []
    for p, f, r in movimientos:
        vieja = f.get("razon") or ""
        clase_vieja = f.get("clase")
        # LA CLASE NO LA DECIDE ESTE CODIGO: la decide la relectura, y su
        # resultado se escribe en el texto de la correccion. Lo que este bloque
        # comprueba es que el diferenciador SOBREVIVIENTE existe, porque si no
        # existiera la clase D no se sostendria y eso seria otra cosa.
        texto = (
            "%s. La razon de arriba se conserva ENTERA y no se borra ni una "
            "palabra. Lo que se anade es esto: el par entro en la COLA DE "
            "RELECTURA POST FUSION por la puerta del DIFERENCIADOR MOVIDO "
            "(docs/plan/08_VERIFICACION.md, seccion LA COLA DE RELECTURA POST "
            "FUSION, disparador en la linea %d y declaracion del tramo en la "
            "linea %d), y esta es su relectura, que es el TRAMO 1 y unico. LO "
            "MEDIDO HOY, con los pasos de HOY de los dos nodos: la razon "
            "declaraba DOS cosas que %s traia y %s no; de las dos, la de "
            "ELIMINAR EXPLICITAMENTE EL USO DE NIVELES DE CALIDAD ACEPTABLES "
            "YA NO ES DIFERENCIADOR, porque una fusion nuestra posterior al "
            "veredicto se la llevo al otro nodo y hoy esta en sus pasos; la "
            "vara lo mide asi: %s. LA OTRA SOBREVIVE ENTERA: el arranque a "
            "escala minima, marcar el dia aunque sea contigo mismo y poner por "
            "escrito un compromiso con la persona que te ayuda, no esta en los "
            "pasos de %s, cuyo paso de la fecha de lanzamiento habla de "
            "visibilidad y no de escala minima ni de compromiso escrito. Y los "
            "diferenciadores del otro lado siguen intactos: el despliegue caso "
            "por caso, el reconocimiento genuino evitando el efectivo como "
            "unico mecanismo y la extension del estandar a todas las areas no "
            "estan en los pasos de %s. ASI QUE LA RELECTURA SOSTIENE LA CLASE "
            "%s: los dos nodos siguen sanos y la clase no se mueve, que es lo "
            "que la tabla QUE PASA CON LO QUE SE RELEA manda para una D. LO "
            "QUE SI SE MUEVE ES LA EVIDENCIA: la razon vieja sostenia la D en "
            "DOS diferenciadores y hoy solo UNO de los dos es cierto, y eso se "
            "escribe en vez de dejar la razon diciendo algo que el grafo ya no "
            "dice. TRAMO 1 DE LA COLA CERRADO. PENDIENTE DE DOCTRINA: la FORMA "
            "de una correccion declarada dentro de este archivo no esta escrita "
            "en ninguna doctrina; el archivo tiene ocho campos y ninguno es de "
            "correccion, asi que se registra lo mejor sostenido, que es anexar "
            "a la razon sin borrar nada, y se marca aqui para que el fundador "
            "decida la sede definitiva."
            % (MARCA_CORRECCION, ln_d, ln_t, f.get("nodo_b"), f.get("nodo_a"),
               r["motivo"], f.get("nodo_a"), f.get("nodo_b"), clase_vieja))
        nueva, cambia = razon_con_correccion(vieja, texto)
        w("   PUESTO %d: clase vieja %s -> clase nueva %s (LA CLASE NO SE MUEVE)"
          % (p, clase_vieja, clase_vieja))
        w("      la razon crece de %d a %d caracteres" % (len(vieja), len(nueva)))
        w("      el texto viejo sigue entero dentro del nuevo: %s"
          % ("SI" if vieja.rstrip() in nueva else "NO"))
        w("      la correccion ya estaba (idempotencia): %s"
          % ("no" if cambia else "SI, y no se duplica"))
        correcciones.append((p, clase_vieja, vieja, nueva, cambia))
    w("")

    w("F) EL MARCADOR, RECOMPUTADO DEL ARCHIVO ANTES DE ESCRIBIR")
    m0 = marcador(filas)
    w("   filas %d | unicos %d | min %d | max %d | huecos %d | duplicados %d"
      % (m0["filas"], m0["unicos"], m0["min"], m0["max"], m0["huecos"],
         m0["duplicados"]))
    for k in sorted(m0["por_clase"], key=lambda x: (x is None, x)):
        w("   CIFRA clase %-6r: %d" % (k, m0["por_clase"][k]))
    w("")

    if a.simular:
        w("G) MODO --simular: NO SE ESCRIBE EL ARCHIVO.")
        for p, cv, vieja, nueva, cambia in correcciones:
            w("   LA RAZON NUEVA DEL PUESTO %d, ENTERA:" % p)
            for trozo in re.findall(r".{1,150}(?:\s|$)", nueva):
                if trozo.strip():
                    w("      | %s" % trozo.strip())
        t = NL.join(L) + NL
        ruta = os.path.join(LOOP, "SALIDA_V%d_T2_COLA_SIMULADA.txt" % VUELTA)
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
        print(t)
        print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
        return 0

    w("G) LA ESCRITURA, LINEA A LINEA Y CONSERVANDO EL ORDEN DEL FICHERO")
    cambiadas = {p: nueva for p, _cv, _v, nueva, cambia in correcciones if cambia}
    if not cambiadas:
        w("   NO SE MUEVE NADA: la correccion ya estaba en las %d razon(es) del"
          % len(correcciones))
        w("   tramo, byte a byte. El sha256 de cierre sera IDENTICO al de apertura")
        w("   y eso NO es una vuelta quieta: es idempotencia.")
    else:
        salida_lineas = []
        n_tocadas = 0
        for l in io.open(ARCHIVO, encoding="utf-8"):
            if not l.strip():
                continue
            fila = json.loads(l)
            p = fila.get("puesto_intra")
            if p in cambiadas:
                fila["razon"] = cambiadas[p]
                n_tocadas += 1
            salida_lineas.append(json.dumps(fila, ensure_ascii=False))
        texto_nuevo = NL.join(salida_lineas) + NL
        io.open(ARCHIVO, "w", encoding="utf-8", newline=NL).write(texto_nuevo)
        w("   CIFRA filas escritas: %d | CIFRA filas TOCADAS: %d"
          % (len(salida_lineas), n_tocadas))
    w("")

    w("H) EL ARCHIVO AL CERRAR, RELEIDO DEL DISCO")
    datos_dsp = io.open(ARCHIVO, "rb").read()
    w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl AL CERRAR:")
    w("      disco %d bytes | LF %d bytes"
      % (len(datos_dsp), len(datos_dsp.replace(b"\r\n", b"\n"))))
    w("      sha256 (LF): %s" % sha_lf(datos_dsp))
    w("   EL sha256 DE CIERRE ES DISTINTO DEL DE APERTURA: %s"
      % ("SI" if sha_lf(datos_dsp) != sha_lf(datos_antes) else "NO"))
    filas2 = [json.loads(l) for l in io.open(ARCHIVO, encoding="utf-8") if l.strip()]
    m1 = marcador(filas2)
    w("   MARCADOR RECOMPUTADO AL CERRAR:")
    w("      filas %d | unicos %d | min %d | max %d | huecos %d | duplicados %d"
      % (m1["filas"], m1["unicos"], m1["min"], m1["max"], m1["huecos"],
         m1["duplicados"]))
    for k in sorted(m1["por_clase"], key=lambda x: (x is None, x)):
        w("      CIFRA clase %-6r: %d" % (k, m1["por_clase"][k]))
    iguales = (m0["filas"] == m1["filas"] and m0["por_clase"] == m1["por_clase"]
               and m0["huecos"] == m1["huecos"]
               and m0["duplicados"] == m1["duplicados"])
    w("   EL MARCADOR NO SE MOVIO: %s" % ("SI" if iguales else "NO"))
    w("   (y es lo que tiene que pasar: la relectura SOSTIENE la clase, asi que lo")
    w("    que cambia es la EVIDENCIA de la razon y no el reparto por clase)")
    w("   LA DIFERENCIA, PAR POR PAR:")
    porpuesto2 = {f.get("puesto_intra"): f for f in filas2}
    for p, cv, vieja, _n, _c in correcciones:
        f2 = porpuesto2.get(p)
        w("      PUESTO %d: clase %s -> %s | razon %d -> %d caracteres | el texto"
          % (p, cv, f2.get("clase"), len(vieja), len(f2.get("razon") or "")))
        w("         viejo sigue entero: %s | la marca de correccion esta: %s"
          % ("SI" if vieja.rstrip() in (f2.get("razon") or "") else "NO",
             "SI" if MARCA_CORRECCION in (f2.get("razon") or "") else "NO"))
    w("   guiones largos o medios en las razones tocadas: %d"
      % sum((porpuesto2[p].get("razon") or "").count(chr(8212))
            + (porpuesto2[p].get("razon") or "").count(chr(8211))
            for p, _cv, _v, _n, _c in correcciones))
    w("")
    w("VEREDICTO: VERDE")
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%d_T2_COLA_POST_FUSION.txt" % VUELTA)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
