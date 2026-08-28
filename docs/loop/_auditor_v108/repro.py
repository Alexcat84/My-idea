import sys, os
sys.path.insert(0, os.path.join('scripts','loop'))
import verificar_cobertura_bolsa_tres_vias as m
def corre(lista, etiqueta):
    fallos=[]
    vivas=m.vivas_de_hoy(fallos)
    con=m.puestos_con_pregunta(lista, fallos)
    if fallos: print(etiqueta,'FALLOS',fallos); return
    sin=sorted(vivas-con)
    print(etiqueta, 'vivas=%d con=%d sin=%d' % (len(vivas), len(vivas&con), len(sin)), 'faltan:', sin)
cuatro = m.FICHEROS_VEREDICTO[:4]
corre(cuatro, 'CASO POSITIVO (4 ficheros, estado pre TAREA3):')
corre(m.FICHEROS_VEREDICTO[:5], 'CINCO (pre TAREA5):')
corre(m.FICHEROS_VEREDICTO, 'SEIS (cierre):')
mut = cuatro[:3] + [("_v108_mut/SALIDA_V107_TAREA5_3_TRAMO1_TRES_VIAS_MUTADO.md","tabla")]
corre(mut, 'MUTACION (falta la fila del 3):')
inex = m.FICHEROS_VEREDICTO + [("NO_EXISTE_ESTE.txt","tabla")]
fallos=[]; m.puestos_con_pregunta(inex, fallos); print('FICHERO INEXISTENTE ->', fallos)
