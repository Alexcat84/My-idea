"use client";

/**
 * Landing pública — port fiel del diseño canónico del fundador
 * ("My Idea_ Diseño UI/index.html", commit 1b686ec).
 *
 * El JSX del return viene convertido 1:1 de la plantilla del diseño
 * (estilos inline incluidos: este archivo ES el diseño, no un tema de
 * la app — tokens.css sigue siendo la fuente de color de las pantallas
 * de trabajo). La lógica de este archivo transplanta el script interno
 * del diseño: campo de estrellas con fugaces, wordmark "My idea" + foco
 * en ~3400 partículas con ciclo ensamblado → pausa → desintegración →
 * reensamblado con cometa que barre y revela el eslogan letra a letra,
 * repulsión al mouse y onda al click, scroll-spy del nav, tipeo simulado
 * del mockup y reveals al hacer scroll. Con prefers-reduced-motion todo
 * queda quieto: una sola pasada estática del wordmark, sin bucles.
 */
import { useEffect, useState } from "react";
import "./landing.css";

type SeccionId = "inicio" | "acerca" | "como-funciona" | "descargar";
type ModoEslogan = "shown" | "destroy" | "hidden" | "reveal";

const ESLOGAN = "Transforma tu creatividad en acción";
const FRASE_DEMO = "Primero la temperatura: si el café llega frío, el empaque ya no importa.";
const SECCIONES: readonly SeccionId[] = ["inicio", "acerca", "como-funciona", "descargar"];

interface Dispersion {
  dx: number;
  dy: number;
  rot: number;
  delay: number;
}

interface EstadoEslogan {
  mode: ModoEslogan;
  reveal: number;
  scatter: Dispersion[];
}

export function Landing() {
  const [typed, setTyped] = useState("");
  const [activa, setActiva] = useState<SeccionId>("inicio");
  const [eslogan, setEslogan] = useState<EstadoEslogan>({ mode: "shown", reveal: 1, scatter: [] });

  const colorNav = (id: SeccionId) => (activa === id ? "#F5F6F8" : "#A6A7AD");
  const subrayadoNav = (id: SeccionId) => (activa === id ? "scaleX(1)" : "scaleX(0)");
  const marcarActiva = (id: SeccionId) => setActiva(id);

  // Mismo cálculo que renderVals() en el script del diseño: cada letra
  // del eslogan con su transform/opacity/filter/transition según el modo.
  const n = ESLOGAN.length;
  const sloganChars = Array.from(ESLOGAN, (ch, i) => {
    let tf = "none";
    let op = 1;
    let fl = "none";
    let tr = "none";
    if (eslogan.mode === "destroy") {
      const s = eslogan.scatter[i] ?? { dx: 0, dy: 0, rot: 0, delay: 0 };
      tf = `translate(${s.dx}px,${s.dy}px) rotate(${s.rot}deg) scale(0.4)`;
      op = 0;
      tr = `transform 1.2s cubic-bezier(0.5,0,0.85,0.45) ${s.delay}s, opacity 1.05s ease-in ${s.delay}s`;
    } else if (eslogan.mode === "hidden") {
      op = 0;
    } else if (eslogan.mode === "reveal") {
      const f = n <= 1 ? 0 : i / (n - 1);
      if (eslogan.reveal > 0.001 && f <= eslogan.reveal) {
        const brillando = eslogan.reveal - f < 0.045 && eslogan.reveal < 1;
        fl = brillando
          ? "brightness(3.4) saturate(0.55) drop-shadow(0 0 13px rgba(230,240,255,0.95))"
          : "none";
        tr = brillando
          ? "opacity 0.08s ease-out, filter 0.04s linear"
          : "opacity 0.08s ease-out, filter 0.9s ease-out";
      } else {
        op = 0;
      }
    }
    return { ch, tf, op, fl, tr };
  });

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

    // ===== Tipeo simulado del mockup del hero =====
    let ti = 0;
    let typedLocal = "";
    const tipeo = reducirMovimiento
      ? null
      : setInterval(() => {
          ti = (ti + 1) % (FRASE_DEMO.length + 46);
          const sig = FRASE_DEMO.slice(0, Math.min(ti, FRASE_DEMO.length));
          if (sig !== typedLocal) {
            typedLocal = sig;
            setTyped(sig);
          }
        }, 55);
    if (reducirMovimiento) setTyped(FRASE_DEMO);

    // ===== Canvas 1: estrellas del hero (idea-canvas) =====
    let rafEstrellas = 0;
    let limpiarEstrellas: (() => void) | null = null;
    {
      const c = document.getElementById("idea-canvas") as HTMLCanvasElement | null;
      const ctx = c?.getContext("2d");
      if (c && ctx) {
        let w = 0;
        let h = 0;
        const ajustar = () => {
          const dpr = window.devicePixelRatio || 1;
          w = c.clientWidth;
          h = c.clientHeight;
          c.width = Math.max(1, w * dpr);
          c.height = Math.max(1, h * dpr);
          ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        };
        ajustar();
        window.addEventListener("resize", ajustar);

        interface Estrella {
          x: number; y: number; vx: number; vy: number; r: number;
          big: boolean; sp: number; ci: number; ph: number;
        }
        const N = 220;
        const pts: Estrella[] = [];
        for (let i = 0; i < N; i++) {
          const big = Math.random() < 0.07;
          pts.push({
            x: Math.random() * (w || 1200),
            y: Math.random() * (h || 700),
            vx: (Math.random() - 0.5) * 0.05,
            vy: (Math.random() - 0.5) * 0.05,
            r: big ? 1.4 + Math.random() * 1.1 : 0.4 + Math.random() * 0.9,
            big,
            sp: 0.5 + Math.random() * 1.6,
            ci: Math.random(),
            ph: Math.random() * Math.PI * 2,
          });
        }

        interface Fugaz { x: number; y: number; vx: number; vy: number; a: number }
        const fugaces: Fugaz[] = [];
        let t = 0;
        let siguienteFugaz = 3 + Math.random() * 4;

        const pintarEstrellas = () => {
          ctx.clearRect(0, 0, w, h);
          for (const p of pts) {
            p.x += p.vx;
            p.y += p.vy;
            if (p.x < -5) p.x = w + 5;
            else if (p.x > w + 5) p.x = -5;
            if (p.y < -5) p.y = h + 5;
            else if (p.y > h + 5) p.y = -5;
            const tw = 0.22 + 0.55 * (0.5 + 0.5 * Math.sin(t * p.sp + p.ph));
            const col = p.ci < 0.7 ? "rgba(205,218,255," : p.ci < 0.9 ? "rgba(150,178,255," : "rgba(255,232,205,";
            ctx.fillStyle = col + tw + ")";
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
            ctx.fill();
            if (p.big) {
              const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * 7);
              g.addColorStop(0, "rgba(160,190,255," + tw * 0.3 + ")");
              g.addColorStop(1, "rgba(160,190,255,0)");
              ctx.fillStyle = g;
              ctx.fillRect(p.x - p.r * 7, p.y - p.r * 7, p.r * 14, p.r * 14);
            }
          }
        };

        const paso = () => {
          t += 0.016;
          pintarEstrellas();
          if (t > siguienteFugaz) {
            siguienteFugaz = t + 5 + Math.random() * 6;
            const dir = Math.random() < 0.5 ? 1 : -1;
            fugaces.push({
              x: w * 0.1 + Math.random() * w * 0.8,
              y: Math.random() * h * 0.35,
              vx: dir * (7 + Math.random() * 4),
              vy: 3 + Math.random() * 2,
              a: 0,
            });
          }
          for (let i = fugaces.length - 1; i >= 0; i--) {
            const s = fugaces[i];
            s.a += 0.02;
            s.x += s.vx;
            s.y += s.vy;
            if (s.a >= 1 || s.x < -90 || s.x > w + 90 || s.y > h + 60) {
              fugaces.splice(i, 1);
              continue;
            }
            const fade = Math.sin(Math.min(1, s.a) * Math.PI);
            const tx = s.x - s.vx * 9;
            const ty = s.y - s.vy * 9;
            const g = ctx.createLinearGradient(s.x, s.y, tx, ty);
            g.addColorStop(0, "rgba(222,233,255," + 0.85 * fade + ")");
            g.addColorStop(1, "rgba(222,233,255,0)");
            ctx.strokeStyle = g;
            ctx.lineWidth = 1.6;
            ctx.beginPath();
            ctx.moveTo(s.x, s.y);
            ctx.lineTo(tx, ty);
            ctx.stroke();
            ctx.fillStyle = "rgba(240,246,255," + 0.9 * fade + ")";
            ctx.beginPath();
            ctx.arc(s.x, s.y, 1.4, 0, Math.PI * 2);
            ctx.fill();
          }
          rafEstrellas = requestAnimationFrame(paso);
        };
        if (reducirMovimiento) {
          pintarEstrellas(); // una sola pasada quieta
        } else {
          rafEstrellas = requestAnimationFrame(paso);
        }
        limpiarEstrellas = () => window.removeEventListener("resize", ajustar);
      }
    }

    // ===== Canvas 2: wordmark de partículas + cometa (wordmark-canvas) =====
    let rafWord = 0;
    let limpiarWord: (() => void) | null = null;
    {
      const c = document.getElementById("wordmark-canvas") as HTMLCanvasElement | null;
      const ctx = c?.getContext("2d");
      if (c && ctx) {
        // next/font hashea el nombre de Inter: usar la familia real del body
        // para que el sampleo del texto use la misma tipografía que la página.
        const familia = getComputedStyle(document.body).fontFamily || "Inter, sans-serif";

        interface PtWord {
          tx: number; ty: number; sx: number; sy: number; d: number; ph: number;
          r: number; ci: number; ox: number; oy: number; d2: number; fx: number; fy: number;
        }
        interface Tri { x: number; y: number; s: number; rot: number; vr: number }

        let w = 0;
        let h = 0;
        let pts: PtWord[] = [];
        let tris: Tri[] = [];
        let links: Array<[number, number]> = [];
        let mx = -99999;
        let my = -99999;
        let t = 0;
        let fase: "in" | "out" = "in";
        let pt = 0;
        let ciclado = false;
        let cometa: { u: number; trail: Array<{ x: number; y: number }> } | null = null;
        let bcx = 0;
        let bcy = 0;
        let bR = 0;
        const anillos: Array<{ a: number }> = [];
        let ultimoAnillo = 0;
        // espejos locales del estado del eslogan (el bucle rAF no puede
        // depender de re-renders para leer el valor vigente)
        let modoLocal: ModoEslogan = "shown";
        let revealLocal = 1;
        let timerEslogan: ReturnType<typeof setTimeout> | undefined;

        const dispersarEslogan = () => {
          clearTimeout(timerEslogan);
          const scatter: Dispersion[] = [];
          for (let i = 0; i < ESLOGAN.length; i++) {
            scatter.push({
              dx: (Math.random() - 0.5) * 320,
              dy: (Math.random() - 0.5) * 220 - 50,
              rot: (Math.random() - 0.5) * 160,
              delay: Math.random() * 0.3,
            });
          }
          modoLocal = "destroy";
          setEslogan((e) => ({ ...e, mode: "destroy", scatter }));
          timerEslogan = setTimeout(() => {
            modoLocal = "hidden";
            revealLocal = 0;
            setEslogan((e) => ({ ...e, mode: "hidden", reveal: 0 }));
          }, 1600);
        };

        const empezarReveal = () => {
          clearTimeout(timerEslogan);
          modoLocal = "reveal";
          revealLocal = 0;
          setEslogan((e) => ({ ...e, mode: "reveal", reveal: 0 }));
        };

        const muestrear = (gap: number): Array<{ x: number; y: number }> => {
          const off = document.createElement("canvas");
          off.width = w;
          off.height = h;
          const o = off.getContext("2d")!;
          o.fillStyle = "#fff";
          o.textAlign = "center";
          // El texto se dibuja dentro del área del ancla (layout), aunque
          // el canvas cubre todo el hero.
          const ancla = document.getElementById("wordmark-anchor");
          const cr = c.getBoundingClientRect();
          const ar = ancla ? ancla.getBoundingClientRect() : cr;
          const rx = ar.left - cr.left;
          const ry = ar.top - cr.top;
          const rw = ar.width;
          const rh = ar.height;
          let fs = Math.round(rh * 0.42);
          o.font = `800 ${fs}px ${familia}`;
          let tw = Math.max(o.measureText("My").width, o.measureText("idea").width);
          let R = (rh * 0.45 + fs * 0.74) / 2.62;
          let gp2 = fs * 0.3;
          let comp = tw + gp2 + R * 2.3;
          if (comp > rw * 0.97) {
            const s = Math.max(0.45, (rw * 0.97 - gp2 - R * 2.3) / tw);
            fs = Math.round(fs * s);
            o.font = `800 ${fs}px ${familia}`;
            tw = Math.max(o.measureText("My").width, o.measureText("idea").width);
            gp2 = fs * 0.3;
            R = (rh * 0.45 + fs * 0.74) / 2.62;
            comp = tw + gp2 + R * 2.3;
          }
          const startX = rx + (rw - comp) / 2;
          const textCx = startX + tw / 2;
          bcx = startX + tw + gp2 + R * 1.05;
          bcy = ry + rh * 0.47 - fs * 0.74 + R;
          bR = R;
          o.fillText("My", textCx, ry + rh * 0.47);
          o.fillText("idea", textCx, ry + rh * 0.92);
          // Foco (bombilla) en trazos simples
          o.strokeStyle = "#fff";
          o.lineCap = "round";
          o.lineWidth = Math.max(3, R * 0.075);
          o.beginPath();
          o.arc(bcx, bcy, R, 0.75 * Math.PI, 2.25 * Math.PI, false);
          o.stroke();
          o.beginPath();
          o.moveTo(bcx - R * 0.707, bcy + R * 0.707);
          o.lineTo(bcx - R * 0.3, bcy + R * 1.18);
          o.stroke();
          o.beginPath();
          o.moveTo(bcx + R * 0.707, bcy + R * 0.707);
          o.lineTo(bcx + R * 0.3, bcy + R * 1.18);
          o.stroke();
          o.beginPath();
          o.moveTo(bcx - R * 0.32, bcy + R * 1.34);
          o.lineTo(bcx + R * 0.32, bcy + R * 1.34);
          o.stroke();
          o.beginPath();
          o.moveTo(bcx - R * 0.24, bcy + R * 1.56);
          o.lineTo(bcx + R * 0.24, bcy + R * 1.56);
          o.stroke();
          o.beginPath();
          o.moveTo(bcx - R * 0.32, bcy + R * 0.6);
          o.lineTo(bcx - R * 0.16, bcy + R * 0.05);
          o.lineTo(bcx, bcy + R * 0.5);
          o.lineTo(bcx + R * 0.16, bcy + R * 0.05);
          o.lineTo(bcx + R * 0.32, bcy + R * 0.6);
          o.stroke();
          const d = o.getImageData(0, 0, w, h).data;
          const out: Array<{ x: number; y: number }> = [];
          for (let y = 0; y < h; y += gap) {
            for (let x = 0; x < w; x += gap) {
              if (d[(y * w + x) * 4 + 3] > 128) out.push({ x, y });
            }
          }
          return out;
        };

        const construir = () => {
          w = c.clientWidth;
          h = c.clientHeight;
          if (!w || !h) return;
          const dpr = window.devicePixelRatio || 1;
          c.width = w * dpr;
          c.height = h * dpr;
          ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
          let gap = Math.max(4, Math.round(w / 180));
          let objetivo = muestrear(gap);
          while (objetivo.length > 3400 && gap < 16) {
            gap += 1;
            objetivo = muestrear(gap);
          }
          pts = objetivo.map((p) => ({
            tx: p.x,
            ty: p.y,
            sx: w / 2 + (Math.random() - 0.5) * w * 1.7,
            sy: h / 2 + (Math.random() - 0.5) * h * 2.0,
            d: (p.x / w) * 1.4 + Math.random() * 0.8,
            ph: Math.random() * 6.283,
            r: Math.random() < 0.06 ? 2.0 + Math.random() * 1.4 : 1.1 + Math.random() * 1.0,
            ci: (Math.random() * 5) | 0,
            ox: 0,
            oy: 0,
            d2: 0,
            fx: 0,
            fy: 0,
          }));
          tris = [];
          for (let i = 0; i < pts.length; i += 26) {
            const p = pts[i];
            tris.push({ x: p.tx, y: p.ty, s: 3 + Math.random() * 6, rot: Math.random() * 6.283, vr: (Math.random() - 0.5) * 0.012 });
          }
          links = [];
          for (let i = 0; i < tris.length; i++) {
            let b1 = -1;
            let b2 = -1;
            let d1 = 1e9;
            let d2 = 1e9;
            for (let j = 0; j < tris.length; j++) {
              if (i === j) continue;
              const dx = tris[i].x - tris[j].x;
              const dy = tris[i].y - tris[j].y;
              const dd = dx * dx + dy * dy;
              if (dd < d1) {
                d2 = d1;
                b2 = b1;
                d1 = dd;
                b1 = j;
              } else if (dd < d2) {
                d2 = dd;
                b2 = j;
              }
            }
            if (b1 >= 0) links.push([i, b1]);
            if (b2 >= 0 && Math.random() < 0.5) links.push([i, b2]);
          }
          t = 0;
          pt = 0;
          fase = "in";
          cometa = null;
          if (modoLocal !== "shown") {
            modoLocal = "shown";
            revealLocal = 1;
            setEslogan((e) => ({ ...e, mode: "shown", reveal: 1 }));
          }
        };

        const onResize = () => construir();
        window.addEventListener("resize", onResize);
        const host = c.parentElement ?? c;
        const onMove = (e: MouseEvent) => {
          const r = c.getBoundingClientRect();
          mx = e.clientX - r.left;
          my = e.clientY - r.top;
        };
        const onLeave = () => {
          mx = -99999;
          my = -99999;
        };
        const onClick = (e: MouseEvent) => {
          const r = c.getBoundingClientRect();
          const cx = e.clientX - r.left;
          const cy = e.clientY - r.top;
          for (const p of pts) {
            const dx = p.tx - cx;
            const dy = p.ty - cy;
            const dist = Math.sqrt(dx * dx + dy * dy) || 1;
            const f = Math.max(0, 1 - dist / (w * 0.45));
            p.ox += (dx / dist) * f * 46;
            p.oy += (dy / dist) * f * 46;
          }
        };
        host.addEventListener("mousemove", onMove);
        host.addEventListener("mouseleave", onLeave);
        host.addEventListener("click", onClick);

        const easeOut = (k: number) => 1 - Math.pow(1 - k, 3);

        const paso = () => {
          t += 0.0166;
          pt += 0.0166;
          // Ciclo: ensamblado (lento) -> pausa -> desintegración -> reensamblado
          if (fase === "in" && pt > 2.2 + 2.0 + 9.0) {
            fase = "out";
            pt = 0;
            ciclado = true;
            dispersarEslogan();
            for (const p of pts) {
              p.d2 = Math.random() * 0.7;
              p.fx = Math.random() * w;
              p.fy = Math.random() * h;
            }
          } else if (fase === "out" && pt > 0.7 + 1.8 + 4.2) {
            for (const p of pts) {
              p.sx = p.fx;
              p.sy = p.fy;
            }
            fase = "in";
            pt = 0;
            cometa = { u: 0, trail: [] };
            empezarReveal();
          }
          ctx.clearRect(0, 0, w, h);
          const pal = ["rgba(150,178,255,", "rgba(122,156,255,", "rgba(77,124,254,", "rgba(214,228,255,", "rgba(111,207,255,"];
          const gp = fase === "in" ? Math.max(0, Math.min(1, (pt - 2.6) / 1.4)) : Math.max(0, 1 - pt / 0.7);
          // Resplandor pulsante del foco + anillos de "idea encendida"
          if (gp > 0 && bR > 0) {
            const ga = (0.10 + 0.07 * Math.sin(t * 1.3)) * gp;
            const g = ctx.createRadialGradient(bcx, bcy, 0, bcx, bcy, bR * 1.8);
            g.addColorStop(0, "rgba(120,160,255," + ga + ")");
            g.addColorStop(1, "rgba(120,160,255,0)");
            ctx.fillStyle = g;
            ctx.fillRect(bcx - bR * 2, bcy - bR * 2, bR * 4, bR * 4);
            if (gp >= 1 && t - ultimoAnillo > 3.6) {
              ultimoAnillo = t;
              anillos.push({ a: 0 });
            }
            for (let i = anillos.length - 1; i >= 0; i--) {
              const rg = anillos[i];
              rg.a += 0.011;
              if (rg.a >= 1) {
                anillos.splice(i, 1);
                continue;
              }
              ctx.strokeStyle = "rgba(120,160,255," + 0.32 * (1 - rg.a) + ")";
              ctx.lineWidth = 1;
              ctx.beginPath();
              ctx.arc(bcx, bcy, bR * 0.3 + rg.a * bR * 1.5, 0, 6.283);
              ctx.stroke();
            }
          }

          for (const p of pts) {
            let e2: number;
            if (fase === "in") {
              const k = Math.max(0, Math.min(1, (pt - p.d) / 2.0));
              if (k <= 0 && !ciclado) continue;
              e2 = k <= 0 ? 0 : easeOut(k);
            } else {
              const k = Math.max(0, Math.min(1, (pt - p.d2) / 1.8));
              e2 = 1 - easeOut(k);
            }
            const bx = fase === "in" ? p.sx : p.fx;
            const by = fase === "in" ? p.sy : p.fy;
            let hx = 0;
            let hy = 0;
            const dxm = p.tx - mx;
            const dym = p.ty - my;
            const dm2 = dxm * dxm + dym * dym;
            if (dm2 < 4900) {
              const dm = Math.sqrt(dm2) || 1;
              const f = (1 - dm / 70) * 14;
              hx = (dxm / dm) * f;
              hy = (dym / dm) * f;
            }
            p.ox *= 0.9;
            p.oy *= 0.9;
            const wob = e2 * 1.6 + (ciclado ? (1 - e2) * 9 : 0);
            const x = bx + (p.tx - bx) * e2 + Math.sin(t * 1.3 + p.ph) * wob + p.ox + hx;
            const y = by + (p.ty - by) * e2 + Math.cos(t * 1.1 + p.ph) * wob + p.oy + hy;
            const al = (0.35 + 0.45 * (0.5 + 0.5 * Math.sin(t * 2.2 + p.ph))) * (ciclado ? 0.55 + 0.45 * e2 : 0.25 + 0.75 * e2);
            ctx.fillStyle = pal[p.ci] + al + ")";
            ctx.beginPath();
            ctx.arc(x, y, p.r, 0, 6.283);
            ctx.fill();
          }

          // Cometa: órbita en semicírculo y pasada horizontal que revela el eslogan
          if (cometa) {
            cometa.u += 0.0166 / 4.6;
            const u = cometa.u;
            const crect = c.getBoundingClientRect();
            const sEl = document.getElementById("slogan-line");
            let sx0 = w * 0.36;
            let sx1 = w * 0.64;
            let syl = h * 0.8;
            if (sEl) {
              const sr = sEl.getBoundingClientRect();
              sx0 = sr.left - crect.left;
              sx1 = sr.right - crect.left;
              syl = sr.top - crect.top + sr.height * 0.5;
            }
            const Cx = w * 0.5;
            const xEnd = Math.max(w * 0.05, sx0 - w * 0.18);
            const Rx = Cx - xEnd;
            const Ry = Math.max(60, syl * 0.85);
            const arcPos = (uu: number) => {
              const th = Math.PI * Math.min(1, uu / 0.6);
              return { x: Cx + Math.cos(th) * Rx, y: syl - Math.sin(th) * Ry };
            };
            const lineK = Math.max(0, (u - 0.5) / 0.5);
            const lineX = xEnd + lineK * lineK * (w + 90 - xEnd);
            let cx2: number;
            let cy2: number;
            let sc2: number;
            if (u < 0.5) {
              const a2 = arcPos(u);
              cx2 = a2.x;
              cy2 = a2.y;
              sc2 = 0.35 + 0.65 * (u / 0.5);
            } else if (u < 0.6) {
              const s = (u - 0.5) / 0.1;
              const ss = s * s * (3 - 2 * s);
              const a2 = arcPos(u);
              cx2 = a2.x + (lineX - a2.x) * ss;
              cy2 = a2.y + (syl - a2.y) * ss;
              sc2 = 1;
            } else {
              cx2 = lineX;
              cy2 = syl;
              sc2 = 1;
            }
            if (u >= 0.6) {
              const p2 = Math.max(revealLocal, Math.max(0, Math.min(1, (cx2 - sx0) / Math.max(1, sx1 - sx0))));
              if (p2 - revealLocal > 0.004 || (p2 >= 1 && revealLocal < 1)) {
                revealLocal = p2;
                setEslogan((e) => ({ ...e, reveal: p2 }));
              }
            }
            cometa.trail.push({ x: cx2, y: cy2 });
            if (cometa.trail.length > 34) cometa.trail.shift();
            for (let i = 1; i < cometa.trail.length; i++) {
              const a2 = cometa.trail[i - 1];
              const b2 = cometa.trail[i];
              const fa = (i / cometa.trail.length) * 0.8 * sc2;
              ctx.strokeStyle = "rgba(170,200,255," + fa + ")";
              ctx.lineWidth = 1.2 + (i / cometa.trail.length) * 4 * sc2;
              ctx.beginPath();
              ctx.moveTo(a2.x, a2.y);
              ctx.lineTo(b2.x, b2.y);
              ctx.stroke();
            }
            const gg = ctx.createRadialGradient(cx2, cy2, 0, cx2, cy2, 34 * sc2);
            gg.addColorStop(0, "rgba(235,243,255," + 0.95 * sc2 + ")");
            gg.addColorStop(0.3, "rgba(160,195,255," + 0.55 * sc2 + ")");
            gg.addColorStop(1, "rgba(160,195,255,0)");
            ctx.fillStyle = gg;
            ctx.beginPath();
            ctx.arc(cx2, cy2, 34 * sc2, 0, 6.283);
            ctx.fill();
            ctx.fillStyle = "rgba(255,255,255," + 0.95 * sc2 + ")";
            ctx.beginPath();
            ctx.arc(cx2, cy2, 4 * sc2 + 0.8, 0, 6.283);
            ctx.fill();
            if (u >= 1) {
              cometa = null;
              modoLocal = "shown";
              revealLocal = 1;
              setEslogan((e) => ({ ...e, mode: "shown", reveal: 1 }));
            }
          }
          rafWord = requestAnimationFrame(paso);
        };

        const pintarEstatico = () => {
          // prefers-reduced-motion: wordmark ensamblado, un solo frame
          ctx.clearRect(0, 0, w, h);
          const pal = ["rgba(150,178,255,", "rgba(122,156,255,", "rgba(77,124,254,", "rgba(214,228,255,", "rgba(111,207,255,"];
          for (const p of pts) {
            ctx.fillStyle = pal[p.ci] + "0.8)";
            ctx.beginPath();
            ctx.arc(p.tx, p.ty, p.r, 0, 6.283);
            ctx.fill();
          }
        };

        const arrancar = () => {
          construir();
          if (reducirMovimiento) {
            pintarEstatico();
          } else {
            rafWord = requestAnimationFrame(paso);
          }
        };
        if (document.fonts?.load) {
          document.fonts.load(`800 100px ${familia}`).then(arrancar, arrancar);
        } else {
          arrancar();
        }

        limpiarWord = () => {
          window.removeEventListener("resize", onResize);
          host.removeEventListener("mousemove", onMove);
          host.removeEventListener("mouseleave", onLeave);
          host.removeEventListener("click", onClick);
          clearTimeout(timerEslogan);
        };
      }
    }

    return () => {
      io.disconnect();
      window.removeEventListener("scroll", onSpy);
      if (tipeo) clearInterval(tipeo);
      cancelAnimationFrame(rafEstrellas);
      cancelAnimationFrame(rafWord);
      limpiarEstrellas?.();
      limpiarWord?.();
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
          <a href="/login" style={{ fontSize: "14.5px", fontWeight: "600", color: "#F5F6F8", padding: "9px 20px", border: "1px solid rgba(255,255,255,0.18)", borderRadius: "10px", transition: "border-color 180ms ease-out,background 180ms ease-out,box-shadow 180ms ease-out" }} className="lh1">Iniciar sesión</a>
          <a href="/nueva" style={{ background: "#4D7CFE", color: "#FFFFFF", border: "none", borderRadius: "10px", padding: "10px 20px", fontFamily: "inherit", fontSize: "14.5px", fontWeight: "600", cursor: "pointer", transition: "background 180ms ease-out" }} className="lh2">Comenzar</a>
        </div>
      </nav>

      {/* ============ HERO ============ */}
      <header id="inicio" style={{ position: "relative", overflow: "hidden", height: "calc(100vh - 64px)", minHeight: "600px", background: "radial-gradient(ellipse 70% 55% at 18% 20%, rgba(52,66,140,0.20), transparent 62%), radial-gradient(ellipse 60% 50% at 82% 70%, rgba(96,70,180,0.14), transparent 62%), radial-gradient(ellipse 90% 70% at 50% 45%, #090B16 0%, #030308 78%)" }}>
        <canvas id="idea-canvas" style={{ position: "absolute", inset: "0", width: "100%", height: "100%", pointerEvents: "none" }}></canvas>
        <canvas id="wordmark-canvas" aria-label="My Idea" style={{ animation: "fadeUp 0.9s ease-out 0.15s both", position: "absolute", inset: "0", width: "100%", height: "100%", pointerEvents: "none" }}></canvas>
        <div style={{ position: "absolute", left: "50%", top: "0", transform: "translateX(-50%)", width: "min(720px,80%)", height: "1px", background: "linear-gradient(90deg,transparent,rgba(77,124,254,0.7),transparent)" }}></div>
        <div style={{ position: "relative", height: "100%", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "flex-end", textAlign: "center", padding: "0 24px 68px", boxSizing: "border-box" }}>
          <div id="wordmark-anchor" style={{ width: "min(97vw,1560px)", aspectRatio: "900/560", maxHeight: "calc(100vh - 250px)", cursor: "pointer" }}></div>
          <p id="slogan-line" style={{ animation: "fadeUp 0.9s ease-out 0.3s both", fontFamily: "var(--font-serif), Georgia, serif", fontStyle: "italic", fontSize: "clamp(20px,2.6vw,30px)", fontWeight: "400", margin: "14px 0 0", letterSpacing: "0.01em", color: "#4E71D8", cursor: "default", minHeight: "1.3em" }} className="lh3">{sloganChars.map((sc, i) => <span key={i} style={{ display: "inline-block", whiteSpace: "pre", transform: sc.tf, opacity: sc.op, filter: sc.fl, transition: sc.tr }}>{sc.ch}</span>)}</p>
          <a href="/nueva" style={{ animation: "fadeUp 0.9s ease-out 0.45s both", background: "#4D7CFE", color: "#FFFFFF", border: "none", borderRadius: "12px", padding: "15px 34px", fontFamily: "inherit", fontSize: "15.5px", fontWeight: "600", cursor: "pointer", marginTop: "26px", boxShadow: "0 0 32px rgba(77,124,254,0.35)", transition: "background 180ms ease-out,box-shadow 180ms ease-out" }} className="lh4">Comenzar gratis</a>
        </div>
        <a href="#acerca" style={{ position: "absolute", left: "50%", bottom: "24px", transform: "translateX(-50%)", color: "#A6A7AD", display: "flex", flexDirection: "column", alignItems: "center", padding: "10px" }} className="lh5">
          <svg width="18" height="18" viewBox="0 0 12 12"><path d="M2 4l4 4 4-4" stroke="currentColor" strokeWidth="1.4" fill="none"></path></svg>
        </a>
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
                    <div style={{ fontSize: "13.5px", lineHeight: "1.55", color: "#F5F6F8", minHeight: "44px" }}>{typed}<span style={{ display: "inline-block", width: "1.5px", height: "14px", background: "#4D7CFE", animation: "caretBlink 1s steps(1) infinite", verticalAlign: "-2px", marginLeft: "1px" }}></span></div>
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
            <a href="/nueva" style={{ background: "#4D7CFE", color: "#FFFFFF", border: "none", borderRadius: "12px", padding: "14px 30px", fontFamily: "inherit", fontSize: "15px", fontWeight: "600", cursor: "pointer", boxShadow: "0 0 26px rgba(77,124,254,0.32)", transition: "background 180ms ease-out,box-shadow 180ms ease-out" }} className="lh8">Comenzar gratis</a>
            <a href="/login" style={{ display: "inline-flex", alignItems: "center", background: "transparent", border: "1px solid rgba(255,255,255,0.14)", color: "#F5F6F8", borderRadius: "12px", padding: "13px 26px", fontSize: "15px", fontWeight: "500", transition: "border-color 180ms ease-out" }} className="lh9">Iniciar sesión</a>
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
