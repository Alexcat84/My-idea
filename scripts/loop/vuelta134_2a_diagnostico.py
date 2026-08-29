# -*- coding: utf-8 -*-
"""vuelta134_2a_diagnostico.py . Diagnostico de TAREA 2.a de la vuelta 134,
ANTES de tocar una linea de verificar_cifras_del_reporte.py.

Para cada una de las cifras que verificar_cifras_del_reporte.py clasifica hoy
como "sin fichero que contar" contra el REPORTE.md de la vuelta 133, dice si
el motivo es:
  (A) NO SE ENCONTRO NINGUN docs/loop/SALIDA_V133_*.txt en su ventana de tres
      frases, o
  (B) SI se encontro un fichero SALIDA_V133_*.txt en la ventana, pero la
      cifra no se pudo CONTAR en el (contar_por_familia devolvio None).

No modifica verificar_cifras_del_reporte.py: reusa sus funciones internas
para no reimplementar la logica de ventana ni de conteo (EJECUTOR.md 2, "el
instrumento manda").

USO:
  python scripts/loop/vuelta134_2a_diagnostico.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_cifras_del_reporte as v  # noqa: E402


def diagnosticar(ruta_reporte):
    texto_completo = v.leer(ruta_reporte)
    texto = v.quitar_bloques_cubiertos(texto_completo)
    frases = v.dividir_frases(texto)
    existentes = v.ficheros_salida_existentes()

    resultado = []
    for i, frase in enumerate(frases):
        for m in v.PATRON_NUMERO_UNIDAD.finditer(frase):
            numero_txt = m.group(1)
            unidad = m.group(2).lower()
            if "," in numero_txt or "." in numero_txt:
                numero_txt_norm = numero_txt.replace(".", "").replace(",", "")
            else:
                numero_txt_norm = numero_txt
            if not numero_txt_norm.isdigit():
                continue
            numero = int(numero_txt_norm)
            ventana = frases[i:i + 3]
            ventana_txt = " ".join(ventana)
            citas = sorted(set(v.PATRON_CITA_SALIDA.findall(ventana_txt)))
            citas = [c for c in citas if c in existentes]
            if not citas:
                resultado.append((numero, unidad, "A", None))
                continue
            fichero_cita = citas[0]
            ruta_cita = os.path.join(v.LOOP, fichero_cita)
            contenido_cita = v.leer(ruta_cita)
            familia = v.UNIDAD_A_FAMILIA[unidad]
            contado = v.contar_por_familia(familia, contenido_cita)
            if contado is None:
                resultado.append((numero, unidad, "B", fichero_cita))
                continue
            if contado != numero:
                continue  # esto seria ROJO en la guarda real, no "sin fichero"
            # cotejada: no entra en el diagnostico de "sin fichero"
    return resultado


def main():
    ruta = v.RUTA_REPORTE
    resultado = diagnosticar(ruta)
    print("DIAGNOSTICO 2.a, %d cifra(s) 'sin fichero que contar' contra %s:" %
          (len(resultado), ruta))
    for numero, unidad, motivo, fichero in resultado:
        if motivo == "A":
            print("  %d %s: (A) NO SE ENCONTRO NINGUN SALIDA_V133_*.txt en su ventana" %
                  (numero, unidad))
        else:
            print("  %d %s: (B) SI se encontro `%s`, pero la cifra no se pudo CONTAR en el" %
                  (numero, unidad, fichero))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
