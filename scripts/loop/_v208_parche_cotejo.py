# -*- coding: utf-8 -*-
r"""_v208_parche_cotejo.py . ARREGLA DOS SONDAS DE `_v208_t3_cotejo.py` QUE ERAN
MAS ESTRECHAS QUE LA AFIRMACION QUE VERIFICABAN.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3). Se guarda en vez de aplicarse a mano para
que el cambio quede auditable.

**NO TOCA LA VARA SELLADA.** `scripts/loop/_v208_t3_vara.py` no se abre aqui: lo
que se corrige es COMO busca el cotejo, no QUE se coteja ni contra que documento.
El reparto sellado sigue intacto y ningun punto cambia de lado.

LAS DOS CAIDAS, LAS DOS MIAS Y LAS DOS CAZADAS ANTES DE PUBLICARLAS. Son la misma
especie que la `C.3` del ejecutor de la 207 y la `9.3` del auditor: un cero de mi
patron a punto de publicarse como un hecho del mundo.

  (1) LA `V.8` AFIRMA UNA AUSENCIA, Y YO LA BUSCABA COMO PRESENCIA. Su cita dice
      que `LECTURAS_DIRIGIDAS.md` *"trae 0 apariciones del literal 'reparto por
      acto' y 0 menciones de OP-L-03"*. Buscar que ESE literal APAREZCA y
      declarar `NO CUBRE` cuando no aparece es exigirle al documento justo lo
      contrario de lo que el punto afirma: **encontrar 0 es lo que lo CONFIRMA.**
      Se invierte, y se le pone un CONTROL POSITIVO al lado, porque una busqueda
      negativa no se puede citar sola (`EJECUTOR.md` 9), que es ademas lo que la
      `V.14` de esta misma vara dice.

  (2) LA `V.13` SI ESTA Y MI SONDA NO LA VEIA POR LAS MAYUSCULAS.
      `docs/loop/AUDITOR.md` lo escribe en su linea 17 como **LA VARA DEL TRABAJO
      PENDIENTE ES EL INSTRUMENTO, NUNCA EL CAMPO `estado`**, en versales, y mi
      sonda buscaba minusculas. **Mi patron era mas estrecho que la afirmacion
      que verificaba.** Se busca sin distinguir mayusculas.

LO QUE ESTE PARCHE NO HACE: no ensancha ningun lector heredado (los dos ficheros
que toca son computo de esta vuelta con prefijo de guion bajo), no mueve ningun
punto de lado y no cambia ningun veredicto a mano: los recomputa el cotejo.
"""
import io
import sys

RUTA = "scripts/loop/_v208_t3_cotejo.py"

PARCHES = []

# (1) LA ESTRUCTURA DE LA SONDA SE ENSANCHA: ahora una sonda puede pedir
#     PRESENCIA, AUSENCIA, o las dos, y puede pedirlo sin distinguir mayusculas.
PARCHES.append(('''SONDAS = {
    "V.1": ["P.5"],
    "V.2": ['"id_op": "OP-L-03"'],
    "V.3": ["reparto por acto"],
    "V.4": ['"acto":'],
    "V.5": ['"terna":'],
    "V.6": ['"leido": true', '"leido": false', '"cifra_pares_leidos"'],
    "V.7": ['"leido": false'],
    "V.8": ["reparto por acto"],
    "V.9": ["P.5", "P.10"],
    "V.10": ["LECTURA DIRIGIDA"],
    "V.11": ['"cobertura"'],
    "V.12": ['"el_lado_de_fuera_es_el_D"'],
    "V.13": ["la vara del trabajo pendiente"],
    "V.14": ["una busqueda negativa no se puede citar"],
    "V.15": ["P.5"],
    "V.17": ["OP-U-01"],
}''', '''# CADA SONDA ES UN DICCIONARIO: `presentes` son literales que TIENEN que
# aparecer; `ausentes` son literales que TIENEN que dar CERO, y entonces la sonda
# exige ademas un `control` que SI aparezca, porque una busqueda negativa no se
# puede citar sola (`EJECUTOR.md` 9); `ci` busca sin distinguir mayusculas.
SONDAS = {
    "V.1": {"presentes": ["P.5"]},
    "V.2": {"presentes": ['"id_op": "OP-L-03"']},
    "V.3": {"presentes": ["reparto por acto"]},
    "V.4": {"presentes": ['"acto":']},
    "V.5": {"presentes": ['"terna":']},
    "V.6": {"presentes": ['"leido": true', '"leido": false',
                          '"cifra_pares_leidos"']},
    "V.7": {"presentes": ['"leido": false']},
    # LA `V.8` AFIRMA UNA AUSENCIA: encontrar 0 es lo que la CONFIRMA.
    "V.8": {"ausentes": ["reparto por acto", "OP-L-03"],
            "control": ["LD-01", "LECTURA DIRIGIDA"]},
    "V.9": {"presentes": ["P.5", "P.10"]},
    "V.10": {"presentes": ["LECTURA DIRIGIDA"]},
    "V.11": {"presentes": ['"cobertura"']},
    "V.12": {"presentes": ['"el_lado_de_fuera_es_el_D"']},
    # LA `V.13` VIVE EN VERSALES EN SU SEDE: se busca sin distinguir mayusculas.
    "V.13": {"presentes": ["la vara del trabajo pendiente es el instrumento"],
             "ci": True},
    "V.14": {"presentes": ["una busqueda negativa no se puede citar"]},
    "V.15": {"presentes": ["P.5"]},
    "V.17": {"presentes": ["OP-U-01"]},
}'''))

PARCHES.append(('''def buscar(lineas, literal):
    return [(i, lineas[i - 1]) for i in range(1, len(lineas) + 1)
            if literal in lineas[i - 1]]''', '''def buscar(lineas, literal, ci=False):
    """LAS LINEAS QUE CONTIENEN EL LITERAL. Devuelve [(linea, texto)]. Si sale
    vacia, quien llama DICE que el patron no encontro nada, NUNCA que la cosa no
    existe (`EJECUTOR.md` 9). Con `ci`, no distingue mayusculas."""
    if ci:
        lit = literal.lower()
        return [(i, lineas[i - 1]) for i in range(1, len(lineas) + 1)
                if lit in lineas[i - 1].lower()]
    return [(i, lineas[i - 1]) for i in range(1, len(lineas) + 1)
            if literal in lineas[i - 1]]'''))

PARCHES.append(('''        rel = DOCS[doc][0]
        ls = textos[doc]
        sondas = SONDAS.get(clave, [])
        hits_por_sonda = []
        for s in sondas:
            h = buscar(ls, s)
            hits_por_sonda.append((s, h))
        todas = all(h for _s, h in hits_por_sonda)
        primera = None
        for _s, h in hits_por_sonda:
            if h:
                primera = h[0]
                break
        if not sondas:
            ver, glosa, linea = ("NO CUBRE",
                                 "NO HAY SONDA DEFINIDA PARA ESTE PUNTO, y eso "
                                 "es un hueco de mi computo, no del documento",
                                 None)
        elif not todas:
            faltan = [s for s, h in hits_por_sonda if not h]
            ver = "NO CUBRE"
            glosa = ("EL PATRON NO ENCONTRO %s en %s. NO DIGO QUE NO EXISTA: "
                     "DIGO QUE NO LO HALLE" % (", ".join(repr(x) for x in faltan), rel))
            linea = primera[0] if primera else None
        else:
            ver = "CUBRE"
            linea = primera[0]
            glosa = ("las %d sonda(s) aparecen: %s"
                     % (len(sondas),
                        "; ".join("%r en %d linea(s), la primera la %d"
                                  % (s, len(h), h[0][0])
                                  for s, h in hits_por_sonda)))''', '''        rel = DOCS[doc][0]
        ls = textos[doc]
        sonda = SONDAS.get(clave) or {}
        ci = bool(sonda.get("ci"))
        presentes = [(s, buscar(ls, s, ci)) for s in sonda.get("presentes", [])]
        ausentes = [(s, buscar(ls, s, ci)) for s in sonda.get("ausentes", [])]
        control = [(s, buscar(ls, s, ci)) for s in sonda.get("control", [])]
        primera = None
        for _s, h in presentes + control:
            if h:
                primera = h[0]
                break
        faltan_pres = [s for s, h in presentes if not h]
        sobran_aus = [s for s, h in ausentes if h]
        faltan_ctrl = [s for s, h in control if not h]
        if not sonda:
            ver, glosa, linea = ("NO CUBRE",
                                 "NO HAY SONDA DEFINIDA PARA ESTE PUNTO, y eso "
                                 "es un hueco de mi computo, no del documento",
                                 None)
        elif faltan_ctrl:
            ver = "NO CUBRE"
            linea = None
            glosa = ("EL CONTROL POSITIVO NO APARECE (%s), asi que la busqueda "
                     "negativa de este punto NO VALE y no publico su cero"
                     % ", ".join(repr(x) for x in faltan_ctrl))
        elif faltan_pres or sobran_aus:
            ver = "NO CUBRE"
            linea = primera[0] if primera else None
            trozos = []
            if faltan_pres:
                trozos.append("EL PATRON NO ENCONTRO %s en %s. NO DIGO QUE NO "
                              "EXISTA: DIGO QUE NO LO HALLE"
                              % (", ".join(repr(x) for x in faltan_pres), rel))
            if sobran_aus:
                trozos.append("EL PUNTO AFIRMA QUE %s NO APARECE, y SI aparece "
                              "en %s"
                              % (", ".join(repr(x) for x in sobran_aus), rel))
            glosa = ". ".join(trozos)
        else:
            ver = "CUBRE"
            linea = primera[0] if primera else None
            trozos = []
            if presentes:
                trozos.append("las %d sonda(s) de PRESENCIA aparecen: %s"
                              % (len(presentes),
                                 "; ".join("%r en %d linea(s), la primera la %d"
                                           % (s, len(h), h[0][0])
                                           for s, h in presentes)))
            if ausentes:
                trozos.append("las %d sonda(s) de AUSENCIA dan CERO, que es lo "
                              "que este punto AFIRMA: %s"
                              % (len(ausentes),
                                 "; ".join("%r en 0 lineas" % s
                                           for s, _h in ausentes)))
            if control:
                trozos.append("y el CONTROL POSITIVO aparece, asi que el cero de "
                              "arriba es del mundo y no de mi patron: %s"
                              % "; ".join("%r en %d linea(s), la primera la %d"
                                          % (s, len(h), h[0][0])
                                          for s, h in control))
            if ci:
                trozos.append("BUSCADO SIN DISTINGUIR MAYUSCULAS, y se dice: la "
                              "sede lo escribe en versales")
            glosa = ". ".join(trozos)'''))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    t = io.open(RUTA, encoding="utf-8").read()
    for i, (viejo, nuevo) in enumerate(PARCHES, 1):
        n = t.count(viejo)
        print("   parche %d: el trozo viejo aparece %d vez(ces) (se exige 1)"
              % (i, n))
        if n != 1:
            print("ROJO: no se escribe nada.")
            return 1
        t = t.replace(viejo, nuevo)
    io.open(RUTA, "w", encoding="utf-8", newline=chr(10)).write(t)
    print("VERDE: %s queda parcheado, %d bytes." % (RUTA, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
