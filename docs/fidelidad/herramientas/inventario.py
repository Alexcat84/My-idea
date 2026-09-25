# -*- coding: utf-8 -*-
"""FASE 0 de la campania de fidelidad total: inventario de nodos vivos,
su libro fuente y si el texto del libro esta disponible para verificar.

SOLO LECTURA sobre dataset/ y sobre las carpetas de textos del fundador.
Escribe en docs/fidelidad/:
  INVENTARIO_NODOS.jsonl   un registro por nodo vivo
  INVENTARIO_LIBROS.json   la tabla de cobertura por libro, en orden de riesgo

Nodo vivo: la puerta esOfrecible de web/lib/engine/graph.ts (existe y
`deprecado` no es verdadero; el dominio depende del proyecto, no del nodo).
Un paso es VERIFICABLE si el texto de su libro existe en .txt o .md.
Un libro con texto solo en .epub o .pdf es NO VERIFICABLE hoy (convertible).
"""
import json, os, collections

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
IDEA = r"C:\Users\AlexDesk\Documents\I have an idea"
B = os.path.join(IDEA, "books")
T = os.path.join(IDEA, "txt")
OCR = r"C:\Users\AlexDesk\Documents\OCR"
DL = r"C:\Users\AlexDesk\Downloads"

# Libro del catalogo -> (texto verificable, copias epub/pdf, tramo de riesgo, nota)
# Tramo 1: seguridad y salud. Tramo 2: legal y dinero. Tramo 3: el resto.
LIBROS = {
 "Managing the Risks of Organizat - Reason, J. T_": (os.path.join(B, r"Especificos\Health and Safety\Managing the Risks of Organizat - Reason, J. T_.txt"), 1, ""),
 "The Field Guide to Understandin - Dekker, Sidney": (os.path.join(B, r"Especificos\Health and Safety\The Field Guide to Understandin - Dekker, Sidney;.txt"), 1, ""),
 "OSHA3885": (os.path.join(B, r"Especificos\Health and Safety\OSHA3885.md"), 1, ""),
 "OSHA3886": (os.path.join(B, r"Especificos\Health and Safety\OSHA3886.md"), 1, ""),
 "SMALL_BUSINESS": (os.path.join(B, r"Especificos\Health and Safety\SMALL_BUSINESS.md"), 1, "manual OSHA para pequena empresa"),
 "Guia de empaque para envios (FedEx)": (os.path.join(T, r"Supply chain\HowToPack_fxcom.txt"), 1, "incluye mercancia peligrosa (baterias, UN 3373, muestras clinicas)"),
 "Venture Deals - Brad Feld": (os.path.join(T, "Venture Deals - Brad Feld.txt"), 2, ""),
 "The Founder's Dilemmas - Wasserman, Noam": (os.path.join(T, "The Founder's Dilemmas - Wasserman, Noam.txt"), 2, ""),
 "Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe": (os.path.join(T, "Financial Intelligence for Entr - Berman, Karen; Knight, Joe;.txt"), 2, ""),
 "Franchise Your Business - Mark Siebert": (os.path.join(B, r"franquicias\Franchise Your Business - Mark Siebert.txt"), 2, ""),
 "A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition)": (os.path.join(B, r"exportacion\basic-guide-to-exporting_Latest_eg_main_086196.txt"), 2, "el txt es la edicion 'Latest' del gobierno; comprobar que coincide con la 11.a"),
 "Businessperson's Guide to Federal Warranty Law": (os.path.join(B, r"General\clientes_y_postventa\Businessperson's Guide to Federal Warranty Law.txt"), 2, ""),
 "NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer": (os.path.join(B, r"seguridad_digital\NIST.SP.1318.txt"), 2, ""),
 "NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide": (os.path.join(B, r"seguridad_digital\NIST.SP.1314.txt"), 2, ""),
 "NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start Guide": (os.path.join(B, r"seguridad_digital\NIST.SP.1300.txt"), 2, ""),
 "Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Businesses": (os.path.join(B, r"seguridad_digital\Getting-Started-NIST-Privacy-Framework-Guide.txt"), 2, ""),
 "Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework (FTC)": (os.path.join(B, r"seguridad_digital\cybersecurity_sb_nist-cyber-framework.txt"), 2, ""),
 "Hubbard, The Failure of Risk Management": (os.path.join(B, r"Risk Management\The Failure of Risk Management_ - Douglas W. Hubbard.txt"), 2, ""),
 "Edwards et al., Managing Project Risks": (os.path.join(B, r"Risk Management\Managing Project Risks - Peter J. Edwards.txt"), 2, ""),
 "DeMarco y Lister, Waltzing with Bears": (os.path.join(B, r"Risk Management\Waltzing with bears _ managing risk on software projects.txt"), 2, ""),
 "Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014)": (os.path.join(T, r"Procurenment\Diana L. Lindstrom - Procurement Project Management Success_ Achieving a Higher Level of Effectiveness-J. Ross Publishing (2014).txt"), 2, "contratos de compra"),
 "Chris Voss, Rompe la barrera del no": (os.path.join(T, r"Procurenment\Rompe la barrera del no_ 9 prin - Chris Voss.txt"), 2, "negociacion"),
 "Juran's Quality Handbook_ The C - Joseph A. Defeo": (os.path.join(B, r"Especificos\Quality\Juran's Quality Handbook_ The C - Joseph A. Defeo.txt"), 3, ""),
 "The Green to Gold Business Play - Daniel C. Esty": (os.path.join(B, r"Especificos\Environmental\The Green to Gold Business Play - Daniel C. Esty.txt"), 3, ""),
 "The Startup Owner's Manual - Blank, Steve": (os.path.join(T, "The Startup Owner's Manual_ The - Blank, Steve.txt"), 3, ""),
 "Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev": (os.path.join(B, r"Especificos\Quality\Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev.txt"), 3, ""),
 "Winning at New Products - Robert G. Cooper": (os.path.join(T, "Winning at New Products_ Creati - Robert G. Cooper.txt"), 3, ""),
 "Essentials of Supply Chain Management - Michael H. Hugos": (os.path.join(B, r"General\operaciones_y_logistica\Essentials of Supply Chain Mana - Michael H. Hugos.txt"), 3, ""),
 "The Hard Thing About Hard Things - Ben Horowitz": (os.path.join(B, r"General\liderazgo_y_crisis\The Hard Thing About Hard Thing - Ben Horowitz.txt"), 3, ""),
 "Quality is free _ the art of making quality certain -- Philip B_ Crosby": (os.path.join(B, r"Especificos\Quality\Quality is free _ the art of making quality certain -- Philip B_ Crosby.md"), 3, ""),
 "Change by Design, Revised and U - Tim Brown": (os.path.join(T, "Change by Design, Revised and U - Tim Brown.txt"), 3, ""),
 "The Lean Startup - Eric Ries": (os.path.join(T, "The Lean Startup_ How Today's E - Eric Ries.txt"), 3, ""),
 "Assembling Tomorrow: A Guide to Designing a Thriving Future": (os.path.join(T, "Assembling Tomorrow_ A Guide to - Scott Doorley.txt"), 3, ""),
 "A Project Manager's Book of Forms - Cynthia Stackpole Snyder": (os.path.join(T, "A Project Manager's Book of For - Cynthia Stackpole Snyder.txt"), 3, ""),
 "Never Lose a Customer Again - Joey Coleman": (os.path.join(B, r"General\clientes_y_postventa\Never Lose a Customer Again_ Tu - Joey Coleman.txt"), 3, ""),
 "Traction - Gabriel Weinberg": (os.path.join(B, r"General\marketing_y_crecimiento\Traction - Gabriel Weinberg.txt"), 3, ""),
 "Cradle to Cradle - Michael Braungart": (os.path.join(B, r"Especificos\Environmental\Cradle to Cradle - Michael Braungart.txt"), 3, ""),
 "Business Model Generation - Osterwalder, Alexander": (os.path.join(T, "Business Model Generation_ A Ha - Osterwalder, Alexander.txt"), 3, ""),
 "Value Proposition Design": (os.path.join(T, "Value Proposition Design - Smith, Alan, Osterwalder, Alexa.txt"), 3, ""),
 "Co-Intelligence_ Living and Wor - Ethan Mollick": (os.path.join(B, r"General\ia_para_negocios\Co-Intelligence_ Living and Wor - Ethan Mollick.txt"), 3, ""),
 "The Art of Thought - Wallas, Graham": (os.path.join(T, "The Art of Thought - Wallas, Graham.txt"), 3, ""),
 "SPIN Selling - Neil Rackham": (os.path.join(B, r"General\ventas\SPIN Selling - Neil Rackham.txt"), 3, ""),
 "The field guide to human-centered design": (os.path.join(T, "The field guide to human-center - Unknown.txt"), 3, ""),
 "Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management": (os.path.join(DL, r"Supply chain\The Handbook of Logistics and D - Alan Rushton;Phil Croucher;Pete.txt"), 3, "texto completo solo en Descargas; en txt/ hay un extracto"),
 "Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment)": (os.path.join(T, r"Supply chain\E-logistics_Cap8_B2C_ecommerce_y_fulfilment.md"), 3, "libro entero tambien en OCR/20260806"),
 "Max Muller, Essentials of Inventory Management": (os.path.join(OCR, "Essentials of Inventory Managem - Max Muller.txt"), 3, ""),
 "ISTA 3P, Protocolo de ensayo de empaque para paqueteria": (os.path.join(T, r"Supply chain\ISTA_3P_26-26_Overview.txt"), 3, ""),
 "Guia visual de empaque": (os.path.join(T, r"Supply chain\packaging_guide_infographic.txt"), 3, ""),
 "Guia de empaque para transporte": (os.path.join(T, r"Supply chain\Packaging_Guidelines.txt"), 3, "guia de UPS"),
 "DHL Express, Guia de empaque": (os.path.join(T, r"Supply chain\dhl_express_packing_guide_en.txt"), 3, ""),
 "Requisitos de empaque de los couriers": (os.path.join(T, r"Supply chain\EXTRACCION_EMPAQUE_COURIERS.md"), 3, "extraccion de la casa sobre las guias de UPS, FedEx y DHL; las tres primarias estan en txt"),
}
# Nombres del campo `fuente` que son el mismo libro con otra grafia.
ALIAS = {
 "The Art of Thought - Graham Wallas": "The Art of Thought - Wallas, Graham",
}
SINTESIS_WALTZING = "DeMarco y Lister, Waltzing with Bears"

def libro_de(fuente):
    if fuente in LIBROS: return [fuente]
    if fuente in ALIAS: return [ALIAS[fuente]]
    if "Waltzing with Bears" in fuente: return [SINTESIS_WALTZING]
    if " | " in fuente: return [libro_de(p)[0] for p in fuente.split(" | ")]
    return [None]

def main():
    g = json.load(open(os.path.join(REPO, "web", "lib", "assets", "master_graph.json"), encoding="utf-8"))["nodos"]
    d = json.load(open(os.path.join(REPO, "dataset", "metadata", "master_graph.json"), encoding="utf-8"))["nodos"]
    assert set(g) == set(d), "el grafo de web y el de dataset difieren"
    vivos = {k: v for k, v in g.items() if not v.get("deprecado")}
    filas = []
    por_libro = collections.OrderedDict()
    for nid, n in sorted(vivos.items()):
        libros = libro_de(n.get("fuente", ""))
        disp = all(l and os.path.exists(LIBROS[l][0]) for l in libros)
        npasos = len(n.get("pasos_accionables") or [])
        filas.append({"nodo": nid, "fuente": n.get("fuente"), "libros": libros,
                      "texto_disponible": disp, "pasos": npasos,
                      "compuesta": len(libros) > 1})
        clave = libros[0] if len(libros) == 1 else " | ".join(libros)
        e = por_libro.setdefault(clave, {"nodos": 0, "pasos": 0, "verificables": 0, "no_verificables": 0})
        e["nodos"] += 1; e["pasos"] += npasos
        e["verificables" if disp else "no_verificables"] += npasos
    out = os.path.join(REPO, "docs", "fidelidad")
    with open(os.path.join(out, "INVENTARIO_NODOS.jsonl"), "w", encoding="utf-8") as f:
        for r in filas: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    tabla = []
    for clave, e in por_libro.items():
        partes = clave.split(" | ")
        tramo = min(LIBROS[p][1] for p in partes if p in LIBROS) if all(p in LIBROS for p in partes) else 9
        texto = [LIBROS[p][0] for p in partes if p in LIBROS]
        nota = "; ".join(LIBROS[p][2] for p in partes if p in LIBROS and LIBROS[p][2])
        tabla.append(dict(libro=clave, tramo=tramo, texto=texto, nota=nota, **e))
    tabla.sort(key=lambda r: (r["tramo"], -r["pasos"]))
    json.dump(tabla, open(os.path.join(out, "INVENTARIO_LIBROS.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tv = sum(r["verificables"] for r in tabla); tn = sum(r["no_verificables"] for r in tabla)
    print("nodos vivos", len(vivos), "pasos", tv + tn, "verificables", tv, "no verificables", tn)
    for r in tabla:
        print(r["tramo"], r["nodos"], r["pasos"], r["verificables"], r["no_verificables"], r["libro"][:70])

if __name__ == "__main__":
    main()
