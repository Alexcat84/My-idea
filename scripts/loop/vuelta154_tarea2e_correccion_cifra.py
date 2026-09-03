# -*- coding: utf-8 -*-
"""vuelta154_tarea2e_correccion_cifra.py . TAREA 2.e DE LA VUELTA 154.

LA CORRECCION DECLARADA DE LA CIFRA DE `OP-C-05` EN SUS DOS SEDES, POR ADICION Y
SIN BORRAR EL TEXTO VIEJO.

LA CIFRA CORREGIDA: donde se publico "153 pares bidireccionales entre vivos tras
resolver, 153 con cita, 0 sin cita", lo cierto es 154 PARES Y UNO ESTABA SIN
CITA. El "0 sin cita" era FALSO.

LAS DOS SEDES, y las dos son SEDE DE CIFRA PUBLICADA:
  1. `scripts/run_phase1.py`, los comentarios de la guarda. Es la CUARTA SEDE,
     creada por la decision del fundador del 2 sep 2026 (PREGUNTA 2), y el texto
     corregido esta escrito HOY, asi que la falta de retroactividad NO lo salva.
     SE CORRIGE EN LA PROPIA TAREA 2.d, dentro del bloque de la guarda
     ensanchada, y por eso este instrumento NO la vuelve a tocar: solo la
     COMPRUEBA y lo dice.
  2. `docs/plan/OPERACIONES.jsonl`, la `nota` de `OP-C-05`. Es la que este
     instrumento escribe, por adicion.

ES IDEMPOTENTE: busca su marca literal y no duplica.

USO:  python scripts/loop/vuelta154_tarea2e_correccion_cifra.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
GUARDA = os.path.join(RAIZ, "scripts", "run_phase1.py")

MARCA = "CORRECCION DECLARADA (2026-09-02, vuelta 154, TAREA 2"

TEXTO = (
    "CORRECCION DECLARADA (2026-09-02, vuelta 154, TAREA 2; hallazgo del acta 153, seccion "
    "4, FUERA de lo marcado. NADA DEL TEXTO ANTERIOR SE BORRA, esta linea se anade). LA "
    "CIFRA DE ESTA FICHA ERA FALSA EN SU MITAD MAS IMPORTANTE: donde arriba dice ~~153 "
    "pares bidireccionales entre vivos tras resolver, 153 con cita, 0 sin cita~~, lo cierto "
    "es 154 PARES, Y UNO ESTABA SIN CITA. EL MOTIVO, MEDIDO Y NO SUPUESTO: la guarda "
    "recorria los nodos ACTIVOS y de cada uno leia SOLO su lista nodos_siguientes, y NUNCA "
    "leia nodos_previos, asi que una arista declarada solo por ese lado era invisible. LA "
    "VARA DECLARADA DE ESTA CAMPANA SON LOS DOS CAMPOS, y esta escrita en tres sitios re "
    "leidos en la vuelta 154: la cabecera cuenta nodos_previos (8.740) y su union de 9.914 "
    "sale de los dos; aristas_a_simetrizar, dentro de la propia scripts/run_phase1.py, "
    "admite una arista si LA DECLARA UN NODO VIVO EN CUALQUIERA DE SUS DOS VISTAS, y la "
    "comprobacion de simetria de Gate 0 ya la usa; y web/lib/engine/planRedactor.ts linea "
    "96 recorre los dos campos juntos como vecinos. Mas P.1, que manda resolver antes de "
    "contar. LAS CUATRO VARAS, MEDIDAS CON INSTRUMENTO PROPIO ESCRITO HOY "
    "(scripts/loop/vuelta154_tarea2a_universo_bidireccionales.py, salida "
    "SALIDA_V154_T2A_UNIVERSO.txt): fuentes vivas y solo nodos_siguientes 153 pares y 0 sin "
    "cita; fuentes vivas y los dos campos 154 y 1; todas las fuentes y solo "
    "nodos_siguientes 155 y 2; todas las fuentes y los dos campos 157 y 4. Las cuatro "
    "reproducen la tabla del acta 153 al digito. EL PAR QUE FALTABA: "
    "error_proofing_servicio contra metodologia_6s, los dos VIVOS, con las dos direcciones "
    "declaradas por el propio metodologia_6s dentro de sus dos listas. Leido por P.5 en la "
    "vuelta 154 y registrado como LD-OPC05-122, clase C por el banco 9.22. LO QUE LA VARA "
    "DEJA FUERA SE NOMBRA EN VEZ DE CALLARSE: con fuentes deprecadas admitidas saldrian 157 "
    "pares y 4 sin cita, o sea TRES pares mas (asignacion_recursos_en_gates contra "
    "sistema_gates_go_kill, formalizar_junta_asesora contra identificar_consejo_asesores y "
    "revision_portafolio_periodica contra sistema_gates_go_kill); quedan fuera por el "
    "criterio ya adjudicado el 14 ago 2026 de que un nodo deprecado es registro historico y "
    "no superficie del producto. LA CIFRA DE HOY, con Gate 0 en verde: 154 pares "
    "bidireccionales entre vivos tras resolver, 154 con cita, 0 SIN CITA. La guarda "
    "ensanchada MUERDE por el lado que era ciego, probado por mutacion sobre variable "
    "computada con su CONTRAPRUEBA (la guarda vieja sale VERDE sobre la misma mutacion) y "
    "con dataset/ identico antes y despues por sha256: ver SALIDA_V154_T2D_MUTACION.txt."
)


def fichas():
    return [json.loads(x) for x in io.open(OPS, encoding="utf-8").read().splitlines()
            if x.strip()]


def main():
    print("=" * 92)
    print("VUELTA 154, TAREA 2.e: LA CORRECCION DECLARADA DE LA CIFRA, EN SUS DOS SEDES")
    print("=" * 92)
    print("")

    print("SEDE 1, scripts/run_phase1.py (la CUARTA sede, creada el 2 sep 2026):")
    texto_guarda = io.open(GUARDA, encoding="utf-8").read()
    tiene = MARCA in texto_guarda
    print("  la correccion declarada esta escrita en el fichero: %s" % ("SI" if tiene else "NO"))
    print("  el texto viejo sigue entero (la frase que se corrige): %s"
          % ("SI" if "153 pares" in texto_guarda else "NO"))
    print("  se escribio en la TAREA 2.d, dentro del bloque de la guarda ensanchada.")
    assert tiene, "la sede 1 no trae su correccion declarada"
    print("")

    print("SEDE 2, docs/plan/OPERACIONES.jsonl, nota de OP-C-05:")
    F = fichas()
    antes_n = len(F)
    claves_antes = sorted({k for f in F for k in f})
    tocada = 0
    for f in F:
        if f["id_op"] != "OP-C-05":
            continue
        nota = f.get("nota") or ""
        print("  nota ANTES: %d caracteres" % len(nota))
        if MARCA in nota:
            print("  YA ESTABA: no se duplica.")
        else:
            f["nota"] = (nota + " " + TEXTO).strip()
            tocada = 1
            print("  nota DESPUES: %d caracteres (+%d)" % (len(f["nota"]), len(f["nota"]) - len(nota)))
            print("  el texto viejo entero es prefijo del nuevo: %s"
                  % f["nota"].startswith(nota))
            assert f["nota"].startswith(nota), "la nota vieja no quedo entera"
    if tocada:
        with io.open(OPS, "w", encoding="utf-8", newline="\n") as fh:
            for f in F:
                fh.write(json.dumps(f, ensure_ascii=False) + "\n")

    G = fichas()
    claves_despues = sorted({k for f in G for k in f})
    print("")
    print("GUARDAS DEL ACTO:")
    print("  fichas antes %d, despues %d, IGUAL: %s" % (antes_n, len(G), antes_n == len(G)))
    print("  claves antes %d, despues %d, IGUALES: %s"
          % (len(claves_antes), len(claves_despues), claves_antes == claves_despues))
    print("  estados: ninguno se mueve en esta tarea (el de OP-C-05 se revisa al CIERRE,")
    print("           por la TAREA 2.f, no aqui).")
    assert antes_n == len(G) == 71
    assert claves_antes == claves_despues
    print("")
    print("CIFRA sedes de cifra publicada corregidas: %d ficheros" % 2)
    print("CIFRA fichas del expediente: %d operaciones" % len(G))


main()
