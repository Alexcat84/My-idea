# -*- coding: utf-8 -*-
r"""_v185_parche_relectura.py . EL PARCHE QUE CONVIERTE EL CLON DE LA RELECTURA AL
DOBLE DE LA 184 EN LA DE LA 185.

Se guarda con nombre y no se tira, para que el clon sea auditable, y ademas
scripts/loop/cotejar_clon_declarado.py lo mide por su cuenta. NO SE AFIRMA QUE
NINGUN DIFF SALGA VACIO: se publica lo que salga.

LO QUE CAMBIA, DECLARADO, Y LA PRIMERA ES LA QUE EL ACTA 185 NOMBRA COMO REMEDIO
DE SU PROPIA CAIDA `A.1`:

  1. LAS RUTAS DEL SELLO Y DE LA CIEGA. El fichero de origen lleva
     `SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_V185.json")` CLAVADO EN
     UNA CONSTANTE, y la ciega en la linea siguiente. El auditor de la 185 nombro
     su sello `V185b` cuando la casa lo nombra `V186`, lo declaro como caida
     propia `A.1`, y el encargo da las TRES rutas exactas. AQUI SE PONEN ESAS, NO
     LAS QUE EL NUMERO DE VUELTA SUGERIRIA. Es una diferencia mas que declarar en
     el cotejo de clones.
  2. LA CABECERA DEL ACTA que se cita de contraste, de la 184 a la 185.
  3. LA CIEGA ANTERIOR contra la que se mide el solape, que es la del turno de
     auditor 185 que sello y murio sin escribir acta.
  4. LA LISTA DE DISCREPANCIAS, de TRES a SIETE.
  5. EL NOMBRE DE LA SALIDA.
  6. EL DOCSTRING.

LA MAQUINA NO SE TOCA: `vecinos()` se sigue IMPORTANDO de
`vuelta182_tarea1c_relectura_al_doble.py` y la vara de
`vuelta182_tarea3_diferenciador_movido.py`.

USO:
  python scripts/loop/_v185_parche_relectura.py
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ORIGEN = os.path.join(RAIZ, "scripts", "loop",
                      "vuelta184_tarea1d_relectura_al_doble.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop",
                       "vuelta185_tarea1e_relectura_al_doble.py")
NL = chr(10)

DOCSTRING = '''# -*- coding: utf-8 -*-
r"""vuelta185_tarea1e_relectura_al_doble.py . LA RELECTURA AL DOBLE DEL TRAMO DE
LA CIEGA DEL ACTA 185 (la que el auditor sello como V185b).

QUIEN LA ENCARGA Y CON QUE PALABRAS. `AUDITOR.md` 1.2, leida hoy: *"si una
discrepancia aparece FUERA de los discutibles marcados, baja el credito de toda la
tanda: ese tramo se relee al doble y lo dices en el acta"*. Y el acta 185, seccion
4: *"EL CREDITO DE LA TANDA BAJA, Y NO POR FORMULA SINO POR LA LETRA: las siete
discrepancias caen FUERA de los discutibles marcados, porque el reporte no marco
ninguno"*. Las discrepancias son SIETE, los puestos 1208, 1459, 2363, 2386, 2505,
2636 y 2854, y el auditor LAS PIERDE LAS SIETE: las adjudica a favor del archivo
sin regatear. Lo que llega al ejecutor es la relectura, no la clase.

EL NOMBRE DEL SELLO NO SE DEDUCE DEL NUMERO DE VUELTA, Y ESTE ES EL PUNTO. El
auditor de la 185 nombro su sello `V185b` cuando la casa lo nombra `V186`, y lo
declaro como su caida propia `A.1`. El fichero del que este clona lleva la ruta
`SELLO_APERTURA_AUDITOR_V185.json` CLAVADA EN UNA CONSTANTE, y un clon que copiara
esa linea leeria el sello equivocado. **El encargo da las tres rutas exactas y son
las que estan aqui.** Aqui no se copia el `sha256` del encargo: se computa y se
compara con el del sello.

QUE ES "AL DOBLE", DICHO ANTES DE HACERLO PARA QUE NO SE PUEDA ELEGIR DESPUES. Se
relee **el doble de puestos**: los 30 del tramo **mas 30 vecinos deterministas**.
La funcion `vecinos()` **SE IMPORTA** de
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`, no se copia, que es la
`6.6` del acta 172 al pie de la letra; y la maquina de la vara se importa de
`scripts/loop/vuelta182_tarea3_diferenciador_movido.py` por el mismo motivo.

CLON DECLARADO de `scripts/loop/vuelta184_tarea1d_relectura_al_doble.py`. Cambian
el sello, la ciega, la ciega anterior, la cabecera del acta que se cita de
contraste, la lista de discrepancias (de tres a siete) y el nombre de la salida.
El cotejo lo hace `scripts/loop/cotejar_clon_declarado.py` y su salida se pega en
el reporte con lo que salga.

LO QUE ESTA RELECTURA NO ES, Y SE DICE PARA NO VENDERLA DE MAS: **NO es una
relectura de juicio.** No vuelve a decidir la clase de ningun par. **Es la
relectura MECANICA del tramo con la vara**, que es la unica que se puede correr
sobre 60 pares sin inventarse nada. Lo que encuentre se nombra; **lo que la vara
no vea, esta salida NO lo afirma.**

USO:
  python scripts/loop/vuelta185_tarea1e_relectura_al_doble.py
"""
'''

CAMBIOS = [
    # (viejo, nuevo, cuantas se esperan)
    ('SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_V185.json")',
     'SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_V185b.json")', 1),
    ('CIEGA = os.path.join(LOOP, "_auditor_v185_ciega_blind.txt")',
     'CIEGA = os.path.join(LOOP, "_auditor_v185b_ciega_blind.txt")', 1),
    ('CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 184"',
     'CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 185"', 1),
    ('VUELTA 184, TAREA 1.d: LA RELECTURA AL DOBLE DEL',
     'VUELTA 185, TAREA 1.e: LA RELECTURA AL DOBLE DEL', 1),
    ('TRAMO DE LA CIEGA DEL ACTA 184, encargada por AUDITOR.md 1.2 porque las',
     'TRAMO DE LA CIEGA DEL ACTA 185, encargada por AUDITOR.md 1.2 porque las', 1),
    ('w("TRES discrepancias del auditor salieron FUERA del marcado")',
     'w("SIETE discrepancias del auditor salieron FUERA del marcado")', 1),
    ('docs/loop/SELLO_APERTURA_AUDITOR_V185.json',
     'docs/loop/SELLO_APERTURA_AUDITOR_V185b.json', 1),
    ('ANTERIOR = os.path.join(LOOP, "_auditor_v184_ciega_blind.txt")',
     'ANTERIOR = os.path.join(LOOP, "_auditor_v185_ciega_blind.txt")', 1),
    ('w("   ciega anterior: docs/loop/_auditor_v184_ciega_blind.txt -> %d puestos"',
     'w("   ciega anterior: docs/loop/_auditor_v185_ciega_blind.txt -> %d puestos"', 1),
    ("for p in (641, 2493, 2594):",
     "for p in (1208, 1459, 2363, 2386, 2505, 2636, 2854):", 1),
    ('ruta = os.path.join(LOOP, "SALIDA_V184_T1D_RELECTURA_AL_DOBLE.txt")',
     'ruta = os.path.join(LOOP, "SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt")', 1),
]

BLOQUE_A_VIEJO = '''    ini9, fin9, cuerpo9 = seccion_del_acta(t_acta, CABECERA_ACTA, 4)
    if ini9 is None:
        w("   el acta 184 NO tiene seccion 4. Se dice y no se inventa.")
        puestos_sec9 = []
    else:
        w("   seccion 4 del acta 184: lineas %d a %d (%d lineas)"
          % (ini9, fin9, len(cuerpo9)))
        w("   su cabecera: %s" % cuerpo9[0].strip()[:100])
        puestos_sec9 = [int(x) for x in
                        re.findall(r"puesto_intra:\\s*(\\d+)", NL.join(cuerpo9))]
    w("   CIFRA puestos que la seccion 4 del acta 184 lista: %d" % len(puestos_sec9))
    w("   (la seccion 4 es la de la ciega, y publica el reparto y LAS TRES")
    w("    discrepancias, no los 30 puestos. Por eso el tramo se lee de la ciega")
    w("    sellada del auditor, que es donde estan, y no del acta)")'''

BLOQUE_A_NUEVO = '''    ini9, fin9, cuerpo9 = seccion_del_acta(t_acta, CABECERA_ACTA, 4)
    if ini9 is None:
        w("   el acta 185 NO tiene seccion 4. Se dice y no se inventa.")
        puestos_sec9 = []
    else:
        w("   seccion 4 del acta 185: lineas %d a %d (%d lineas)"
          % (ini9, fin9, len(cuerpo9)))
        w("   su cabecera: %s" % cuerpo9[0].strip()[:100])
        puestos_sec9 = [int(x) for x in
                        re.findall(r"puesto_intra:\\s*(\\d+)", NL.join(cuerpo9))]
    w("   CIFRA puestos que la seccion 4 del acta 185 lista: %d" % len(puestos_sec9))
    w("   (la seccion 4 es la de la ciega, y publica el reparto y LAS SIETE")
    w("    discrepancias, no los 30 puestos. Por eso el tramo se lee de la ciega")
    w("    sellada del auditor, que es donde estan, y no del acta)")'''

BLOQUE_I_VIEJO = '''    w("I) LAS TRES DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA VARA")
    w("   (el acta 184 las nombra en su seccion 4: los puestos 641, 2493 y 2594,")
    w("    que el auditor pierde LOS TRES a favor del archivo. Aqui NO se re-decide")
    w("    ninguna clase: solo se dice si estan en el universo releido y que ve la")
    w("    vara en ellas)")'''

BLOQUE_I_NUEVO = '''    w("I) LAS SIETE DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA VARA")
    w("   (el acta 185 las nombra en su seccion 4: los puestos 1208, 1459, 2363,")
    w("    2386, 2505, 2636 y 2854, que el auditor pierde LOS SIETE a favor del")
    w("    archivo. Aqui NO se re-decide ninguna clase: solo se dice si estan en el")
    w("    universo releido y que ve la vara en ellas. LO QUE LA VARA NO VEA, NO SE")
    w("    AFIRMA)")'''

BLOQUE_F_VIEJO = '''    w("   (el criterio del sello dice que la muestra excluye los 89 puestos de")
    w("    las ciegas de las actas 180, 181 y 182; aqui se comprueba contra la")
    w("    ciega inmediatamente anterior, la que el acta 183 releyo en su continuacion)")'''

BLOQUE_F_NUEVO = '''    w("   (el criterio del sello dice que la muestra excluye los 90 puestos de")
    w("    las ciegas de las actas 183, 184 y del turno de auditor 185 que sello y")
    w("    murio sin escribir acta; aqui se comprueba contra esa ultima, que es la")
    w("    ciega inmediatamente anterior en disco)")'''

BLOQUE_J_VIEJO = '''    w("   1. El tramo se leyo de la ciega SELLADA del auditor, cotejada por")
    w("      sha256 contra su propio sello, y NO del acta, que no lo lista.")'''

BLOQUE_J_NUEVO = '''    w("   1. El tramo se leyo de la ciega SELLADA del auditor, cotejada por")
    w("      sha256 contra su propio sello, y NO del acta, que no lo lista. El")
    w("      sello se llama V185b y no V186 porque el auditor lo nombro asi y lo")
    w("      declaro como su caida propia A.1: la ruta viene del encargo, no de")
    w("      deducirla del numero de vuelta.")'''


def main():
    src = io.open(ORIGEN, encoding="utf-8").read().replace(chr(13) + NL, NL)
    fin_doc = src.index('"""', src.index('r"""') + 4) + 3 + 1
    cuerpo = src[fin_doc:]
    for viejo, nuevo, cuantas in CAMBIOS:
        hay = cuerpo.count(viejo)
        if hay != cuantas:
            raise SystemExit("ROJO: %r aparece %d veces y se esperaban %d."
                             % (viejo[:60], hay, cuantas))
        cuerpo = cuerpo.replace(viejo, nuevo)
    for viejo, nuevo in ((BLOQUE_A_VIEJO, BLOQUE_A_NUEVO),
                         (BLOQUE_F_VIEJO, BLOQUE_F_NUEVO),
                         (BLOQUE_I_VIEJO, BLOQUE_I_NUEVO),
                         (BLOQUE_J_VIEJO, BLOQUE_J_NUEVO)):
        if viejo not in cuerpo:
            raise SystemExit("ROJO: no encuentro el bloque %r." % viejo[:60])
        cuerpo = cuerpo.replace(viejo, nuevo, 1)
    texto = DOCSTRING + cuerpo
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITO: %s" % DESTINO)
    print("CIFRA bytes: %d | CIFRA lineas: %d"
          % (len(texto.encode("utf-8")), texto.count(NL)))
    print("CIFRA apariciones de 'V185b': %d" % texto.count("V185b"))
    print("CIFRA apariciones de 'V185.json': %d" % texto.count("V185.json"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
