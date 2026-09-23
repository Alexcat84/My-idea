"use client";

/**
 * Landing pública — port fiel del diseño canónico del fundador
 * ("My Idea_ Diseño UI/index.html", commit 1b686ec).
 *
 * El JSX del return viene convertido 1:1 de la plantilla del diseño
 * (estilos inline incluidos: este archivo ES el diseño, no un tema de
 * la app — tokens.css sigue siendo la fuente de color de las pantallas
 * de trabajo). La lógica de este archivo transplanta el script interno
 * del diseño: scroll-spy del nav, tipeo simulado del mockup y reveals al
 * hacer scroll. Con prefers-reduced-motion todo queda quieto.
 *
 * HERO (portada-particula, decisión del fundador): la masa líquida que se
 * transforma, con su misma materia, en las cinco figuras (ui/portada/HeroMasa).
 * El lema y su animación desaparecen; el título queda como texto oculto a
 * la vista (lectores de pantalla y buscadores) y "Comenzar gratis" se
 * mantiene, discreto, en el borde inferior.
 */
import { useEffect, useState } from "react";
import { createClient } from "@/lib/supabase/client";
import { HeroMasa } from "./portada/HeroMasa";
import "./landing.css";

type SeccionId = "inicio" | "acerca" | "como-funciona" | "descargar";
const FRASE_DEMO = "Primero la temperatura: si el café llega frío, el empaque ya no importa.";
const SECCIONES: readonly SeccionId[] = ["inicio", "acerca", "como-funciona", "descargar"];

/**
 * Tipeo simulado del mockup, aislado en su propio componente: su estado
 * cambia cada 55 ms y antes re-renderizaba la landing entera (cientos de
 * nodos con estilos inline), lo que en un movil se comia el hilo principal
 * que necesita la masa del hero.
 */
function TipeoDemo() {
  const [typed, setTyped] = useState("");
  useEffect(() => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      // Sin animación: la frase completa, fuera del render síncrono del
      // efecto (regla de hooks; el timeout 0 la pinta en el siguiente tick).
      const inmediato = setTimeout(() => setTyped(FRASE_DEMO), 0);
      return () => clearTimeout(inmediato);
    }
    let ti = 0;
    let typedLocal = "";
    const tipeo = setInterval(() => {
      ti = (ti + 1) % (FRASE_DEMO.length + 46);
      const sig = FRASE_DEMO.slice(0, Math.min(ti, FRASE_DEMO.length));
      if (sig !== typedLocal) {
        typedLocal = sig;
        setTyped(sig);
      }
    }, 55);
    return () => clearInterval(tipeo);
  }, []);
  return <>{typed}</>;
}

export function Landing({ sesionActiva = false }: { sesionActiva?: boolean } = {}) {
  // Logout desde la landing (lógica común: el botón de auth es "Iniciar
  // sesión" cuando estás fuera y "Salir" cuando estás dentro). Recarga a "/"
  // para que el servidor recalcule la sesión y el nav vuelva a su estado.
  async function cerrarSesion() {
    try {
      await createClient().auth.signOut();
    } catch {
      /* aunque falle el signOut remoto, la recarga limpia la sesión local */
    }
    window.location.assign("/");
  }
  const [activa, setActiva] = useState<SeccionId>("inicio");

  const colorNav = (id: SeccionId) => (activa === id ? "#F5F6F8" : "#A6A7AD");
  const subrayadoNav = (id: SeccionId) => (activa === id ? "scaleX(1)" : "scaleX(0)");
  const marcarActiva = (id: SeccionId) => setActiva(id);

  useEffect(() => {
    const reducirMovimiento = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    // ===== Reveals al hacer scroll (data-reveal / data-reveal-delay) =====
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            const el = e.target as HTMLElement;
            el.style.opacity = "1";
            el.style.transform = "translateY(0px)";
            io.unobserve(el);
          }
        });
      },
      { threshold: 0.12 }
    );
    document.querySelectorAll<HTMLElement>("[data-reveal]").forEach((el) => {
      if (reducirMovimiento) return; // quietos: se quedan visibles
      el.style.opacity = "0";
      el.style.transform = "translateY(28px)";
      const d = el.getAttribute("data-reveal-delay") ?? "0";
      el.style.transition = `opacity 700ms ease-out ${d}ms, transform 700ms ease-out ${d}ms, border-color 180ms ease-out, box-shadow 180ms ease-out`;
      io.observe(el);
    });

    // ===== Scroll-spy del nav =====
    let activaLocal: SeccionId = "inicio";
    const onSpy = () => {
      let cur: SeccionId = "inicio";
      for (const id of SECCIONES) {
        const el = document.getElementById(id);
        if (el && el.getBoundingClientRect().top <= 150) cur = id;
      }
      if (cur !== activaLocal) {
        activaLocal = cur;
        setActiva(cur);
      }
    };
    window.addEventListener("scroll", onSpy, { passive: true });
    onSpy();

    return () => {
      io.disconnect();
      window.removeEventListener("scroll", onSpy);
    };
  }, []);

  return (
    <div className="landing" style={{ background: "#000000", color: "#F5F6F8", minHeight: "100vh" }}>

      {/* ============ NAV ============ */}
      <nav style={{ position: "sticky", top: "0", zIndex: "50", background: "rgba(0,0,0,0.72)", backdropFilter: "blur(14px)", WebkitBackdropFilter: "blur(14px)", borderBottom: "1px solid rgba(255,255,255,0.08)" }}>
        <div style={{ maxWidth: "1160px", margin: "0 auto", padding: "0 24px", height: "64px", display: "flex", alignItems: "center", gap: "28px" }}>
          <div data-nav-links="true" style={{ display: "flex", alignItems: "center", gap: "6px", fontSize: "15px", fontWeight: "500" }}>
            <a href="#inicio" onClick={() => marcarActiva("inicio")} style={{ position: "relative", color: colorNav("inicio"), padding: "8px 12px", borderRadius: "8px", transition: "color 180ms ease-out,background 180ms ease-out" }} className="lh0">Inicio<span style={{ position: "absolute", left: "12px", right: "12px", bottom: "2px", height: "2px", borderRadius: "2px", background: "#4D7CFE", transform: subrayadoNav("inicio"), transformOrigin: "left center", transition: "transform 220ms ease-out" }}></span></a>
            <a href="#acerca" onClick={() => marcarActiva("acerca")} style={{ position: "relative", color: colorNav("acerca"), padding: "8px 12px", borderRadius: "8px", transition: "color 180ms ease-out,background 180ms ease-out" }} className="lh0">Acerca de<span style={{ position: "absolute", left: "12px", right: "12px", bottom: "2px", height: "2px", borderRadius: "2px", background: "#4D7CFE", transform: subrayadoNav("acerca"), transformOrigin: "left center", transition: "transform 220ms ease-out" }}></span></a>
            <a href="#como-funciona" onClick={() => marcarActiva("como-funciona")} style={{ position: "relative", color: colorNav("como-funciona"), padding: "8px 12px", borderRadius: "8px", transition: "color 180ms ease-out,background 180ms ease-out" }} className="lh0">Cómo funciona<span style={{ position: "absolute", left: "12px", right: "12px", bottom: "2px", height: "2px", borderRadius: "2px", background: "#4D7CFE", transform: subrayadoNav("como-funciona"), transformOrigin: "left center", transition: "transform 220ms ease-out" }}></span></a>
            <a href="#descargar" onClick={() => marcarActiva("descargar")} style={{ position: "relative", color: colorNav("descargar"), padding: "8px 12px", borderRadius: "8px", transition: "color 180ms ease-out,background 180ms ease-out" }} className="lh0">App<span style={{ position: "absolute", left: "12px", right: "12px", bottom: "2px", height: "2px", borderRadius: "2px", background: "#4D7CFE", transform: subrayadoNav("descargar"), transformOrigin: "left center", transition: "transform 220ms ease-out" }}></span></a>
          </div>
          <span style={{ flex: "1" }}></span>
          {sesionActiva ? (
            <button type="button" onClick={cerrarSesion} style={{ fontSize: "14.5px", fontWeight: "600", color: "#F5F6F8", background: "transparent", cursor: "pointer", fontFamily: "inherit", padding: "9px 20px", border: "1px solid rgba(255,255,255,0.18)", borderRadius: "10px", transition: "border-color 180ms ease-out,background 180ms ease-out,box-shadow 180ms ease-out" }} className="lh1">Salir</button>
          ) : (
            <a href="/login" style={{ fontSize: "14.5px", fontWeight: "600", color: "#F5F6F8", padding: "9px 20px", border: "1px solid rgba(255,255,255,0.18)", borderRadius: "10px", transition: "border-color 180ms ease-out,background 180ms ease-out,box-shadow 180ms ease-out" }} className="lh1">Iniciar sesión</a>
          )}
          <a href={sesionActiva ? "/ideas" : "/nueva"} style={{ background: "#4D7CFE", color: "#FFFFFF", border: "none", borderRadius: "10px", padding: "10px 20px", fontFamily: "inherit", fontSize: "14.5px", fontWeight: "600", cursor: "pointer", transition: "background 180ms ease-out" }} className="lh2">{sesionActiva ? "Mis ideas" : "Comenzar"}</a>
        </div>
      </nav>

      {/* ============ HERO ============ */}
      <header id="inicio" className="portada-hero">
        <h1 className="solo-lectores">My Idea: transforma tu creatividad en acción</h1>
        <HeroMasa />
        <a href="/nueva" className="portada-cta">Comenzar gratis</a>
      </header>

      {/* ============ MARQUEE DE TEMAS ============ */}

        <div style={{ borderTop: "1px solid rgba(255,255,255,0.08)", borderBottom: "1px solid rgba(255,255,255,0.08)", overflow: "hidden", padding: "18px 0", background: "#050507" }}>
          <div style={{ display: "flex", gap: "0", width: "max-content", animation: "marquee 36s linear infinite" }}>
            <div style={{ display: "flex", alignItems: "center", gap: "64px", paddingRight: "64px" }}>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>La Chispa</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>Claridad</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>La Exploración</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>Tu Plan</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>Manos a la Obra</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>Recorrido de la idea</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>Una acción para esta semana</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>Tu proyecto vivo</span>
            </div>
            <div style={{ display: "flex", alignItems: "center", gap: "64px", paddingRight: "64px" }}>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>La Chispa</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>Claridad</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>La Exploración</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>Tu Plan</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>Manos a la Obra</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>Recorrido de la idea</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>Una acción para esta semana</span>
              <span style={{ fontSize: "15px", color: "#A6A7AD", whiteSpace: "nowrap" }}>Tu proyecto vivo</span>
            </div>
          </div>
        </div>


      {/* ============ ACERCA DE ============ */}
      <section id="acerca" style={{ scrollMarginTop: "80px", maxWidth: "1160px", margin: "0 auto", padding: "clamp(80px,10vw,140px) 24px" }}>
        <div style={{ display: "flex", gap: "64px", alignItems: "flex-start" }} data-stack="true">
          <div data-reveal="true" style={{ flex: "1" }}>
            <div style={{ fontSize: "16px", fontWeight: "600", letterSpacing: "1.8px", textTransform: "uppercase", color: "#4D7CFE" }}>Acerca de</div>
            <h2 style={{ fontSize: "clamp(28px,4vw,44px)", lineHeight: "1.15", letterSpacing: "-0.02em", fontWeight: "700", margin: "16px 0 0", textWrap: "balance" }}>A los emprendedores no les faltan ideas. Les falta un interlocutor serio</h2>
          </div>
          <div data-reveal="true" data-reveal-delay="150" style={{ flex: "1", display: "flex", flexDirection: "column", gap: "18px", paddingTop: "8px" }}>
            <p style={{ fontSize: "18px", lineHeight: "1.75", color: "#A6A7AD", margin: "0", textAlign: "justify", textWrap: "pretty" }}>My Idea nace de esa convicción. Construimos un motor de conocimiento que pregunta como un buen mentor y estructura como un buen consultor: escucha tu contexto, no repite plantillas, y sabe cuándo una etapa ya quedó cubierta por lo que contaste.</p>
            <p style={{ fontSize: "18px", lineHeight: "1.75", color: "#A6A7AD", margin: "0", textAlign: "justify", textWrap: "pretty" }}>El resultado no es una conversación que se pierde: es un proyecto vivo. Pausa, ejecuta en el mundo real y regresa cuando quieras. My Idea recalcula dónde estás parado y te muestra los siguientes pasos exactos, hasta el cierre definitivo. Y si el proyecto lo exige, se expande con módulos especializados.</p>
          </div>
        </div>
      </section>

      {/* ============ CÓMO FUNCIONA ============ */}
      <section id="como-funciona" style={{ scrollMarginTop: "80px", maxWidth: "1160px", margin: "0 auto", padding: "clamp(80px,10vw,140px) 24px" }}>
        <div data-reveal="true" style={{ maxWidth: "640px" }}>
          <div style={{ fontSize: "16px", fontWeight: "600", letterSpacing: "1.8px", textTransform: "uppercase", color: "#4D7CFE" }}>Cómo funciona</div>
          <h2 style={{ fontSize: "clamp(30px,4.4vw,48px)", lineHeight: "1.1", letterSpacing: "-0.02em", fontWeight: "700", margin: "16px 0 0", textWrap: "balance" }}>De la idea al mundo real</h2>
        </div>
        <div data-grid-stack="true" style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "20px", marginTop: "56px" }}>
          <div data-reveal="true" data-reveal-delay="0" style={{ flex: "1", background: "#101013", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "16px", padding: "28px", display: "flex", flexDirection: "column", gap: "20px" }} className="lh6">
            <div style={{ fontSize: "15px", fontWeight: "600", color: "#A6A7AD" }}>01</div>
            <div style={{ background: "#17171B", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "12px", padding: "16px", display: "flex", alignItems: "center", gap: "12px" }}>
              <span style={{ fontSize: "13px", color: "#6B6C73", flex: "1", lineHeight: "1.5" }}>Cuéntame tu idea, o en qué punto estás con ella</span>
              <span style={{ width: "38px", height: "38px", borderRadius: "50%", background: "#4D7CFE", display: "flex", alignItems: "center", justifyContent: "center", flex: "none" }}>
                <svg width="15" height="15" viewBox="0 0 16 16" fill="none"><rect x="6" y="1.5" width="4" height="7.5" rx="2" fill="#FFFFFF"></rect><path d="M3.5 8a4.5 4.5 0 0 0 9 0" stroke="#FFFFFF" strokeWidth="1.4" fill="none"></path><line x1="8" y1="12.6" x2="8" y2="14.5" stroke="#FFFFFF" strokeWidth="1.4"></line></svg>
              </span>
            </div>
            <div>
              <div style={{ fontSize: "21px", fontWeight: "600" }}>Describe tu idea</div>
              <p style={{ fontSize: "16px", lineHeight: "1.65", color: "#A6A7AD", margin: "10px 0 0", textWrap: "pretty" }}>Escríbela o díctala tal como la tienes en mente. Ese es todo el requisito.</p>
            </div>
          </div>
          <div data-reveal="true" data-reveal-delay="120" style={{ flex: "1", background: "#101013", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "16px", padding: "28px", display: "flex", flexDirection: "column", gap: "20px" }} className="lh6">
            <div style={{ fontSize: "15px", fontWeight: "600", color: "#A6A7AD" }}>02</div>
            <div style={{ background: "#17171B", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "12px", padding: "16px 18px" }}>
              <div style={{ position: "relative", display: "flex", flexDirection: "column", gap: "14px" }}>
                <div style={{ position: "absolute", left: "5px", top: "7px", bottom: "7px", borderLeft: "1px dashed rgba(255,255,255,0.18)" }}></div>
                <div style={{ display: "flex", gap: "10px", alignItems: "center", position: "relative" }}><span style={{ width: "11px", height: "11px", borderRadius: "50%", background: "#17171B", display: "flex", alignItems: "center", justifyContent: "center", flex: "none" }}><span style={{ width: "7px", height: "7px", borderRadius: "50%", background: "#4D7CFE" }}></span></span><span style={{ width: "64%", height: "6px", borderRadius: "3px", background: "rgba(255,255,255,0.10)" }}></span></div>
                <div style={{ display: "flex", gap: "10px", alignItems: "center", position: "relative", opacity: "0.45" }}><span style={{ width: "11px", height: "11px", borderRadius: "50%", background: "#17171B", display: "flex", alignItems: "center", justifyContent: "center", flex: "none" }}><span style={{ width: "7px", height: "7px", borderRadius: "50%", border: "1.5px solid #A6A7AD", boxSizing: "border-box" }}></span></span><span style={{ width: "44%", height: "6px", borderRadius: "3px", background: "rgba(255,255,255,0.10)" }}></span></div>
                <div style={{ display: "flex", gap: "10px", alignItems: "center", position: "relative" }}><span style={{ width: "11px", height: "11px", borderRadius: "50%", background: "#17171B", display: "flex", alignItems: "center", justifyContent: "center", flex: "none" }}><span style={{ width: "7px", height: "7px", borderRadius: "50%", background: "#4D7CFE", animation: "ideaPulse 1.6s ease-out infinite" }}></span></span><span style={{ fontSize: "11px", color: "#4D7CFE", fontWeight: "500" }}>generando…</span></div>
              </div>
            </div>
            <div>
              <div style={{ fontSize: "21px", fontWeight: "600" }}>Aporta más detalles</div>
              <p style={{ fontSize: "16px", lineHeight: "1.65", color: "#A6A7AD", margin: "10px 0 0", textWrap: "pretty" }}>Nada de plantillas: una entrevista específica evoluciona en tiempo real con la naturaleza de tu idea y te habla en tu propio lenguaje, sin barreras técnicas.</p>
            </div>
          </div>
          <div data-reveal="true" data-reveal-delay="240" style={{ flex: "1", background: "#101013", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "16px", padding: "28px", display: "flex", flexDirection: "column", gap: "20px" }} className="lh6">
            <div style={{ fontSize: "15px", fontWeight: "600", color: "#A6A7AD" }}>03</div>
            <div style={{ background: "#17171B", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "12px", padding: "16px 18px", display: "flex", flexDirection: "column", gap: "9px" }}>
              <span style={{ width: "52%", height: "8px", borderRadius: "4px", background: "rgba(255,255,255,0.18)" }}></span>
              <span style={{ width: "88%", height: "6px", borderRadius: "3px", background: "rgba(255,255,255,0.08)" }}></span>
              <span style={{ width: "80%", height: "6px", borderRadius: "3px", background: "rgba(255,255,255,0.08)" }}></span>
              <span style={{ display: "flex", alignItems: "center", gap: "8px", background: "rgba(77,124,254,0.10)", border: "1px solid rgba(77,124,254,0.30)", borderRadius: "8px", padding: "8px 10px", marginTop: "4px" }}><span style={{ fontSize: "10.5px", color: "#8FA9FF", fontWeight: "600" }}>Esta semana</span></span>
            </div>
            <div>
              <div style={{ fontSize: "21px", fontWeight: "600" }}>Recibe tu plan</div>
              <p style={{ fontSize: "16px", lineHeight: "1.65", color: "#A6A7AD", margin: "10px 0 0", textWrap: "pretty" }}>Un plan detallado con etapas, experimentos y acciones concretas para ejecutarlo. Aquí se genera tu hoja de ruta.</p>
            </div>
          </div>
          <div data-reveal="true" data-reveal-delay="360" style={{ flex: "1", background: "#101013", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "16px", padding: "28px", display: "flex", flexDirection: "column", gap: "20px" }} className="lh6">
            <div style={{ fontSize: "15px", fontWeight: "600", color: "#A6A7AD" }}>04</div>
            <div style={{ background: "#17171B", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "12px", padding: "16px 18px", display: "flex", flexDirection: "column", gap: "13px" }}>
              <div style={{ display: "flex", alignItems: "center", gap: "10px" }}><span style={{ width: "7px", height: "7px", borderRadius: "50%", background: "#3FB950", flex: "none" }}></span><span style={{ width: "70%", height: "6px", borderRadius: "3px", background: "rgba(255,255,255,0.10)" }}></span></div>
              <div style={{ display: "flex", alignItems: "center", gap: "10px" }}><span style={{ width: "7px", height: "7px", borderRadius: "50%", background: "#3FB950", flex: "none" }}></span><span style={{ width: "54%", height: "6px", borderRadius: "3px", background: "rgba(255,255,255,0.10)" }}></span></div>
              <div style={{ display: "flex", alignItems: "center", gap: "10px" }}><span style={{ width: "7px", height: "7px", borderRadius: "50%", background: "#4D7CFE", animation: "ideaPulse 1.6s ease-out infinite", flex: "none" }}></span><span style={{ fontSize: "11px", color: "#8FA9FF", fontWeight: "600" }}>siguiente paso exacto</span></div>
            </div>
            <div>
              <div style={{ fontSize: "21px", fontWeight: "600" }}>Ejecuta y regresa</div>
              <p style={{ fontSize: "16px", lineHeight: "1.65", color: "#A6A7AD", margin: "10px 0 0", textWrap: "pretty" }}>Pausa, actúa en el mundo real y vuelve: el plan recalcula dónde estás y te muestra los pasos exactos hasta el cierre.</p>
            </div>
          </div>
        </div>

        <div data-reveal="true" style={{ position: "relative", marginTop: "72px" }}>
          <div style={{ textAlign: "center", marginBottom: "40px", fontSize: "clamp(20px,2.6vw,26px)", fontWeight: "700", letterSpacing: "-0.02em", textWrap: "balance" }}>No es un chatbot, es tu espacio de trabajo</div>

            <div style={{ position: "absolute", left: "50%", top: "40%", transform: "translate(-50%,-50%)", width: "80%", height: "70%", background: "radial-gradient(ellipse at center, rgba(77,124,254,0.17), transparent 66%)", pointerEvents: "none", animation: "glowDrift 9s ease-in-out infinite" }}></div>

          <div style={{ animation: "fadeUp 0.9s ease-out 0.45s both", position: "relative", background: "#101013", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "16px", overflow: "hidden", maxWidth: "980px", margin: "0 auto", boxShadow: "0 0 100px rgba(77,124,254,0.16),0 40px 90px rgba(0,0,0,0.5)" }}>
            <div style={{ height: "44px", borderBottom: "1px solid rgba(255,255,255,0.08)", display: "flex", alignItems: "center", gap: "8px", padding: "0 18px" }}>
              <span style={{ width: "9px", height: "9px", borderRadius: "50%", background: "#2A2A2F" }}></span>
              <span style={{ width: "9px", height: "9px", borderRadius: "50%", background: "#2A2A2F" }}></span>
              <span style={{ width: "9px", height: "9px", borderRadius: "50%", background: "#2A2A2F" }}></span>
              <span style={{ flex: "1" }}></span>
              <span style={{ fontSize: "12px", color: "#A6A7AD" }}>Cafetería de especialidad a domicilio · Entrevista</span>
              <span style={{ flex: "1" }}></span>
            </div>
            <div style={{ display: "flex", background: "#000000" }} data-stack="true">
              <div data-hide-mobile="true" style={{ width: "264px", flex: "none", borderRight: "1px solid rgba(255,255,255,0.08)", padding: "26px 22px" }}>
                <div style={{ fontSize: "10.5px", letterSpacing: "1.2px", textTransform: "uppercase", color: "#A6A7AD", fontWeight: "600", marginBottom: "22px" }}>Recorrido de la idea</div>
                <div style={{ position: "relative", display: "flex", flexDirection: "column", gap: "24px" }}>
                  <div style={{ position: "absolute", left: "6px", top: "10px", bottom: "10px", borderLeft: "1px dashed rgba(255,255,255,0.16)" }}></div>
                  <div style={{ display: "flex", gap: "11px", alignItems: "flex-start", position: "relative", animation: "nodeIn 0.5s ease-out 0.7s both" }}>
                    <span style={{ width: "13px", height: "13px", borderRadius: "50%", background: "#000000", display: "flex", alignItems: "center", justifyContent: "center", flex: "none" }}><span style={{ width: "8px", height: "8px", borderRadius: "50%", background: "#4D7CFE" }}></span></span>
                    <span style={{ fontSize: "12.5px", fontWeight: "500", lineHeight: "1.4", color: "#F5F6F8" }}>La Chispa</span>
                  </div>
                  <div style={{ display: "flex", gap: "11px", alignItems: "flex-start", position: "relative", animation: "nodeIn 0.5s ease-out 0.9s both" }}>
                    <span style={{ width: "13px", height: "13px", borderRadius: "50%", background: "#000000", display: "flex", alignItems: "center", justifyContent: "center", flex: "none" }}><span style={{ width: "8px", height: "8px", borderRadius: "50%", background: "#4D7CFE" }}></span></span>
                    <span style={{ fontSize: "12.5px", fontWeight: "500", lineHeight: "1.4", color: "#F5F6F8" }}>Claridad</span>
                  </div>
                  <div style={{ display: "flex", gap: "11px", alignItems: "center", position: "relative", animation: "nodeIn 0.5s ease-out 1.1s both" }}>
                    <span style={{ width: "13px", height: "13px", borderRadius: "50%", background: "#000000", display: "flex", alignItems: "center", justifyContent: "center", flex: "none" }}><span style={{ width: "8px", height: "8px", borderRadius: "50%", background: "#4D7CFE", animation: "ideaPulse 1.6s ease-out infinite" }}></span></span>
                    <span style={{ minWidth: "0" }}><span style={{ display: "block", fontSize: "12.5px", fontWeight: "500", lineHeight: "1.4", color: "#4D7CFE" }}>La Exploración</span><span style={{ display: "block", fontSize: "10.5px", color: "#A6A7AD", marginTop: "2px" }}>en curso…</span></span>
                  </div>
                  <div style={{ display: "flex", gap: "11px", alignItems: "flex-start", position: "relative", opacity: "0.4", animation: "nodeIn 0.5s ease-out 1.3s both" }}>
                    <span style={{ width: "13px", height: "13px", borderRadius: "50%", background: "#000000", display: "flex", alignItems: "center", justifyContent: "center", flex: "none" }}><span style={{ width: "8px", height: "8px", borderRadius: "50%", border: "1.5px solid #A6A7AD", boxSizing: "border-box" }}></span></span>
                    <span style={{ fontSize: "12.5px", fontWeight: "500", lineHeight: "1.4", color: "#F5F6F8" }}>Tu Plan</span>
                  </div>
                  <div style={{ display: "flex", gap: "11px", alignItems: "flex-start", position: "relative", opacity: "0.4", animation: "nodeIn 0.5s ease-out 1.5s both" }}>
                    <span style={{ width: "13px", height: "13px", borderRadius: "50%", background: "#000000", display: "flex", alignItems: "center", justifyContent: "center", flex: "none" }}><span style={{ width: "8px", height: "8px", borderRadius: "50%", border: "1.5px solid #A6A7AD", boxSizing: "border-box" }}></span></span>
                    <span style={{ fontSize: "12.5px", fontWeight: "500", lineHeight: "1.4", color: "#F5F6F8" }}>Manos a la Obra</span>
                  </div>
                </div>
              </div>
              <div style={{ flex: "1", padding: "clamp(24px,4vw,44px)", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center" }}>
                <div style={{ background: "#101013", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "16px", padding: "24px", maxWidth: "560px", width: "100%", boxSizing: "border-box" }}>
                  <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "14px" }}>
                    <span style={{ width: "6px", height: "6px", borderRadius: "50%", background: "#4D7CFE" }}></span>
                    <span style={{ fontSize: "10.5px", letterSpacing: "1.2px", textTransform: "uppercase", color: "#A6A7AD", fontWeight: "600" }}>Calidad y Diseño en el MVP</span>
                  </div>
                  <div style={{ fontSize: "clamp(15px,1.6vw,17px)", fontWeight: "500", lineHeight: "1.55", color: "#F5F6F8", textWrap: "pretty" }}>De estos dos riesgos, el café que llega frío y el costo del empaque térmico, ¿cuál necesitas resolver PRIMERO para confiar en que el negocio funciona como sistema?</div>
                  <div style={{ background: "#17171B", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "12px", padding: "14px", marginTop: "20px" }}>
                    <div style={{ fontSize: "13.5px", lineHeight: "1.55", color: "#F5F6F8", minHeight: "44px" }}><TipeoDemo /><span style={{ display: "inline-block", width: "1.5px", height: "14px", background: "#4D7CFE", animation: "caretBlink 1s steps(1) infinite", verticalAlign: "-2px", marginLeft: "1px" }}></span></div>
                    <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginTop: "10px" }}>
                      <span style={{ width: "32px", height: "32px", borderRadius: "50%", border: "1px solid rgba(255,255,255,0.14)", display: "flex", alignItems: "center", justifyContent: "center" }}>
                        <svg width="13" height="13" viewBox="0 0 16 16" fill="none"><rect x="6" y="1.5" width="4" height="7.5" rx="2" fill="#A6A7AD"></rect><path d="M3.5 8a4.5 4.5 0 0 0 9 0" stroke="#A6A7AD" strokeWidth="1.4" fill="none"></path><line x1="8" y1="12.6" x2="8" y2="14.5" stroke="#A6A7AD" strokeWidth="1.4"></line></svg>
                      </span>
                      <span style={{ background: "#4D7CFE", color: "#FFFFFF", borderRadius: "10px", padding: "8px 18px", fontSize: "12.5px", fontWeight: "600" }}>Enviar</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ============ BANDA ÁRBOL ============ */}
      <section style={{ position: "relative", overflow: "hidden", borderTop: "1px solid rgba(255,255,255,0.08)", borderBottom: "1px solid rgba(255,255,255,0.08)", background: "#050507" }}>
        <div style={{ position: "absolute", left: "50%", top: "0", transform: "translateX(-50%)", width: "min(640px,70%)", height: "1px", background: "linear-gradient(90deg,transparent,rgba(77,124,254,0.65),transparent)" }}></div>
        <div style={{ position: "absolute", left: "50%", top: "0", transform: "translateX(-50%)", width: "min(820px,88%)", height: "260px", background: "radial-gradient(ellipse at center top, rgba(77,124,254,0.12), transparent 65%)", pointerEvents: "none" }}></div>
        <div style={{ maxWidth: "1160px", margin: "0 auto", padding: "clamp(72px,9vw,120px) 24px" }}>
          <div data-reveal="true" style={{ textAlign: "center", maxWidth: "680px", margin: "0 auto" }}>
            <h2 style={{ fontSize: "clamp(28px,4vw,44px)", lineHeight: "1.15", letterSpacing: "-0.02em", fontWeight: "700", margin: "0", textWrap: "balance" }}>De la chispa a la realidad</h2>
            <p style={{ fontSize: "18px", lineHeight: "1.65", color: "#A6A7AD", margin: "18px 0 0", textWrap: "pretty" }}>Cinco etapas acompañan tu idea desde el primer destello hasta verla funcionando en el mundo real. En cada una sabes dónde estás y cuál es el siguiente paso.</p>
          </div>
          <div data-hide-mobile="true" data-reveal="true" data-reveal-delay="150" style={{ position: "relative", maxWidth: "920px", margin: "64px auto 0", height: "140px" }}>
            <div style={{ position: "absolute", left: "85px", right: "85px", top: "16px", borderTop: "3px dashed rgba(255,255,255,0.18)" }}></div>
            <div style={{ position: "absolute", left: "85px", right: "85px", top: "14px", height: "7px" }}><div style={{ height: "7px", borderRadius: "4px", background: "linear-gradient(90deg,rgba(77,124,254,0.35),#4D7CFE),#050507", animation: "treeLine 11s linear infinite" }}></div></div>
            <div style={{ position: "absolute", left: "0", right: "0", top: "0", display: "flex", justifyContent: "space-between" }}>
              <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: "16px", width: "170px" }}>
                <span style={{ width: "36px", height: "36px", borderRadius: "50%", background: "#050507", display: "flex", alignItems: "center", justifyContent: "center" }}><span style={{ width: "21px", height: "21px", borderRadius: "50%", background: "#4D7CFE", animation: "treeStep1 11s ease-out infinite" }}></span></span>
                <span style={{ fontSize: "17px", color: "#F5F6F8", fontWeight: "600", textAlign: "center", lineHeight: "1.45", animation: "treeStep1 11s ease-out infinite" }}>La Chispa</span>
              </div>
              <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: "16px", width: "170px" }}>
                <span style={{ width: "36px", height: "36px", borderRadius: "50%", background: "#050507", display: "flex", alignItems: "center", justifyContent: "center" }}><span style={{ width: "21px", height: "21px", borderRadius: "50%", background: "#4D7CFE", animation: "treeStep2 11s ease-out infinite" }}></span></span>
                <span style={{ fontSize: "17px", color: "#F5F6F8", fontWeight: "600", textAlign: "center", lineHeight: "1.45", animation: "treeStep2 11s ease-out infinite" }}>Claridad</span>
              </div>
              <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: "16px", width: "170px" }}>
                <span style={{ width: "36px", height: "36px", borderRadius: "50%", background: "#050507", display: "flex", alignItems: "center", justifyContent: "center" }}><span style={{ width: "21px", height: "21px", borderRadius: "50%", background: "#4D7CFE", animation: "treeStep3 11s ease-out infinite" }}></span></span>
                <span style={{ fontSize: "17px", color: "#F5F6F8", fontWeight: "600", textAlign: "center", lineHeight: "1.45", animation: "treeStep3 11s ease-out infinite" }}>La Exploración</span>
              </div>
              <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: "16px", width: "170px" }}>
                <span style={{ width: "36px", height: "36px", borderRadius: "50%", background: "#050507", display: "flex", alignItems: "center", justifyContent: "center" }}><span style={{ width: "21px", height: "21px", borderRadius: "50%", background: "#4D7CFE", animation: "treeStep4 11s ease-out infinite" }}></span></span>
                <span style={{ fontSize: "17px", color: "#F5F6F8", fontWeight: "600", textAlign: "center", lineHeight: "1.45", animation: "treeStep4 11s ease-out infinite" }}>Tu Plan</span>
              </div>
              <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: "16px", width: "170px" }}>
                <span style={{ width: "36px", height: "36px", borderRadius: "50%", background: "#050507", display: "flex", alignItems: "center", justifyContent: "center" }}><span style={{ width: "21px", height: "21px", borderRadius: "50%", background: "#3FB950", animation: "ideaPulseGreen 1.6s ease-out infinite, treeStep5 11s ease-out infinite" }}></span></span>
                <span style={{ fontSize: "17px", color: "#3FB950", fontWeight: "600", textAlign: "center", lineHeight: "1.45", animation: "treeStep5 11s ease-out infinite" }}>Manos a la Obra</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ============ DESCARGAR APP ============ */}
      <section id="descargar" style={{ scrollMarginTop: "80px", borderTop: "1px solid rgba(255,255,255,0.08)", background: "#050507" }}>
        <div style={{ maxWidth: "1160px", margin: "0 auto", padding: "clamp(80px,10vw,132px) 24px", display: "flex", gap: "64px", alignItems: "center" }} data-stack="true">
          <div data-reveal="true" style={{ flex: "1.2" }}>
            <div style={{ fontSize: "16px", fontWeight: "600", letterSpacing: "1.8px", textTransform: "uppercase", color: "#4D7CFE" }}>La app</div>
            <h2 style={{ fontSize: "clamp(28px,4vw,44px)", lineHeight: "1.15", letterSpacing: "-0.02em", fontWeight: "700", margin: "16px 0 0", textWrap: "balance" }}>Llévala en el bolsillo</h2>
            <p style={{ fontSize: "18px", lineHeight: "1.7", color: "#A6A7AD", margin: "20px 0 0", maxWidth: "500px", textWrap: "pretty" }}>Las mejores respuestas llegan lejos del escritorio.</p>
            <div style={{ display: "flex", alignItems: "center", gap: "14px", marginTop: "32px", flexWrap: "wrap" }}>
              <button style={{ display: "flex", alignItems: "center", gap: "12px", background: "#F5F6F8", color: "#000000", border: "none", borderRadius: "12px", padding: "13px 22px", fontFamily: "inherit", fontSize: "15.5px", fontWeight: "600", cursor: "pointer", transition: "background 180ms ease-out" }} className="lh7">
                <svg width="16" height="16" viewBox="0 0 16 16"><path d="M3 2l10 6-10 6z" fill="#000000"></path></svg>
                Descargar en Google Play
              </button>
            </div>
          </div>
          <div data-reveal="true" data-reveal-delay="150" style={{ flex: "1", display: "flex", justifyContent: "center", position: "relative" }}>
            <div style={{ position: "absolute", left: "50%", top: "50%", transform: "translate(-50%,-50%)", width: "440px", height: "440px", background: "radial-gradient(circle, rgba(77,124,254,0.15), transparent 65%)", pointerEvents: "none", animation: "glowDrift 11s ease-in-out infinite" }}></div>
            <div style={{ position: "relative", width: "300px", background: "#000000", border: "1px solid rgba(255,255,255,0.10)", borderRadius: "36px", padding: "10px", boxSizing: "border-box", boxShadow: "0 0 80px rgba(77,124,254,0.15)" }}>
              <div style={{ background: "#000000", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "28px", overflow: "hidden", display: "flex", flexDirection: "column", height: "560px" }}>
                <div style={{ height: "34px", display: "flex", alignItems: "center", justifyContent: "center" }}><span style={{ width: "74px", height: "16px", borderRadius: "999px", background: "#101013" }}></span></div>
                <div style={{ flex: "1", display: "flex", flexDirection: "column", justifyContent: "center", padding: "0 24px", textAlign: "center" }}>
                  <div style={{ display: "flex", justifyContent: "center", marginBottom: "22px" }}><span style={{ width: "12px", height: "12px", borderRadius: "50%", background: "#4D7CFE", animation: "ideaPulse 2.4s ease-out infinite" }}></span></div>
                  <div style={{ fontSize: "19px", fontWeight: "600", lineHeight: "1.4", letterSpacing: "-0.01em", textWrap: "balance" }}>Cuéntame tu idea, o en qué punto estás con ella</div>
                  <div style={{ background: "#101013", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "14px", marginTop: "26px", padding: "16px", display: "flex", flexDirection: "column", gap: "16px", alignItems: "center" }}>
                    <span style={{ width: "100%", height: "6px", borderRadius: "3px", background: "rgba(255,255,255,0.07)" }}></span>
                    <span style={{ width: "72%", height: "6px", borderRadius: "3px", background: "rgba(255,255,255,0.07)" }}></span>
                    <span style={{ width: "52px", height: "52px", borderRadius: "50%", background: "#4D7CFE", display: "flex", alignItems: "center", justifyContent: "center", marginTop: "4px" }}>
                      <svg width="20" height="20" viewBox="0 0 16 16" fill="none"><rect x="6" y="1.5" width="4" height="7.5" rx="2" fill="#FFFFFF"></rect><path d="M3.5 8a4.5 4.5 0 0 0 9 0" stroke="#FFFFFF" strokeWidth="1.4" fill="none"></path><line x1="8" y1="12.6" x2="8" y2="14.5" stroke="#FFFFFF" strokeWidth="1.4"></line></svg>
                    </span>
                    <span style={{ fontSize: "11px", color: "#A6A7AD" }}>también puedes dictarla</span>
                  </div>
                  <a href="/nueva" style={{ background: "#4D7CFE", color: "#FFFFFF", border: "none", borderRadius: "12px", padding: "13px", fontFamily: "inherit", fontSize: "14px", fontWeight: "600", cursor: "pointer", marginTop: "20px" }}>Comenzar</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ============ CTA FINAL ============ */}
      <section style={{ position: "relative", overflow: "hidden", borderTop: "1px solid rgba(255,255,255,0.08)" }}>
        <div style={{ position: "absolute", left: "50%", top: "0", transform: "translateX(-50%)", width: "min(720px,80%)", height: "1px", background: "linear-gradient(90deg,transparent,rgba(77,124,254,0.7),transparent)" }}></div>
        <div style={{ position: "absolute", left: "50%", bottom: "-170px", transform: "translateX(-50%)", width: "min(920px,92%)", height: "380px", background: "radial-gradient(ellipse at center bottom, rgba(77,124,254,0.13), transparent 65%)", pointerEvents: "none" }}></div>
        <div style={{ position: "relative", maxWidth: "1160px", margin: "0 auto", padding: "clamp(88px,11vw,150px) 24px", textAlign: "center" }}>
          <h2 data-reveal="true" style={{ fontSize: "clamp(34px,5.4vw,64px)", lineHeight: "1.08", letterSpacing: "-0.03em", fontWeight: "800", margin: "0", textWrap: "balance" }}>Aquí acaba tu idea y nace tu proyecto</h2>
          <div data-reveal="true" data-reveal-delay="120" style={{ display: "flex", justifyContent: "center", gap: "14px", marginTop: "36px", flexWrap: "wrap" }}>
            <a href={sesionActiva ? "/ideas" : "/nueva"} style={{ background: "#4D7CFE", color: "#FFFFFF", border: "none", borderRadius: "12px", padding: "14px 30px", fontFamily: "inherit", fontSize: "15px", fontWeight: "600", cursor: "pointer", boxShadow: "0 0 26px rgba(77,124,254,0.32)", transition: "background 180ms ease-out,box-shadow 180ms ease-out" }} className="lh8">{sesionActiva ? "Mis ideas" : "Comenzar gratis"}</a>
            {sesionActiva ? (
              <button type="button" onClick={cerrarSesion} style={{ display: "inline-flex", alignItems: "center", background: "transparent", cursor: "pointer", fontFamily: "inherit", border: "1px solid rgba(255,255,255,0.14)", color: "#F5F6F8", borderRadius: "12px", padding: "13px 26px", fontSize: "15px", fontWeight: "500", transition: "border-color 180ms ease-out" }} className="lh9">Salir</button>
            ) : (
              <a href="/login" style={{ display: "inline-flex", alignItems: "center", background: "transparent", border: "1px solid rgba(255,255,255,0.14)", color: "#F5F6F8", borderRadius: "12px", padding: "13px 26px", fontSize: "15px", fontWeight: "500", transition: "border-color 180ms ease-out" }} className="lh9">Iniciar sesión</a>
            )}
          </div>
        </div>
      </section>

      {/* ============ FOOTER ============ */}
      <footer style={{ borderTop: "1px solid rgba(255,255,255,0.08)" }}>
        <div style={{ maxWidth: "1160px", margin: "0 auto", padding: "32px 24px", display: "flex", alignItems: "center", gap: "24px", flexWrap: "wrap" }}>
          <span style={{ display: "flex", alignItems: "center", gap: "8px" }}><span style={{ width: "8px", height: "8px", borderRadius: "50%", background: "#4D7CFE" }}></span><span style={{ fontSize: "13.5px", fontWeight: "700" }}>My Idea</span></span>
          <span style={{ flex: "1" }}></span>
          <div style={{ display: "flex", alignItems: "center", gap: "22px", fontSize: "14.5px", flexWrap: "wrap" }}>
            <a href="#acerca" style={{ color: "#A6A7AD" }} className="lh5">Acerca de</a>
            <a href="#como-funciona" style={{ color: "#A6A7AD" }} className="lh5">Cómo funciona</a>
            <a href="#descargar" style={{ color: "#A6A7AD" }} className="lh5">App</a>
            <a href="#" style={{ color: "#A6A7AD" }} className="lh5">Privacidad</a>
            <a href="#" style={{ color: "#A6A7AD" }} className="lh5">Términos</a>
          </div>
          <span style={{ fontSize: "14.5px", color: "#A6A7AD" }}>© 2026 My Idea</span>
        </div>
      </footer>
    </div>
  );
}
