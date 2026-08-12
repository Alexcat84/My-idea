#!/usr/bin/env bash
# Bucle autonomo de la campaña My Idea: ejecutor (Opus 4.8) + auditor (Fable 5).
# Se corre UNA vez, idealmente dentro de tmux:  bash orquestador.sh
# Se detiene solo si: existe docs/loop/PARA_ALEXIS.md, no hay prompt siguiente,
# o se alcanza MAX_VUELTAS. El estado vive en el repo; cada vuelta sobrevive
# a caidas porque todo se commitea y pushea.
set -uo pipefail
cd "$(dirname "$0")"

MAX_VUELTAS="${MAX_VUELTAS:-80}"
MODELO_EJECUTOR="${MODELO_EJECUTOR:-claude-opus-4-8}"
MODELO_AUDITOR="${MODELO_AUDITOR:-claude-fable-5}"
RAMA="${RAMA:-staging}"
LOOP="docs/loop"
mkdir -p "$LOOP"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOOP/loop.log"; }

costo() { # extrae total_cost_usd del json si jq existe
  command -v jq >/dev/null 2>&1 && jq -r '.total_cost_usd // empty' "$1" 2>/dev/null || true
}

for i in $(seq 1 "$MAX_VUELTAS"); do
  git pull --rebase origin "$RAMA" >/dev/null 2>&1 || true

  if [ -f "$LOOP/PARA_ALEXIS.md" ]; then
    log "DETENIDO en la vuelta $i: existe $LOOP/PARA_ALEXIS.md. Leelo."
    break
  fi
  if [ ! -s "$LOOP/PROMPT_SIGUIENTE.md" ]; then
    log "DETENIDO en la vuelta $i: no hay PROMPT_SIGUIENTE.md con contenido."
    break
  fi

  log "VUELTA $i : EJECUTOR ($MODELO_EJECUTOR)"
  claude -p --model "$MODELO_EJECUTOR" --dangerously-skip-permissions \
    --output-format json \
    "Estas en el repo de la campaña. Lee docs/loop/EJECUTOR.md (tus reglas permanentes) y despues docs/loop/PROMPT_SIGUIENTE.md (tu encargo). Ejecuta el encargo al pie de la letra. Escribe tu reporte completo en docs/loop/REPORTE.md sobrescribiendo el anterior, con los discutibles marcados. Commitea y pushea TODO a la rama activa antes de terminar." \
    > "$LOOP/ultimo_ejecutor.json" 2>>"$LOOP/loop.log"
  c1="$(costo "$LOOP/ultimo_ejecutor.json")"; log "ejecutor listo${c1:+ (USD $c1)}"

  git pull --rebase origin "$RAMA" >/dev/null 2>&1 || true

  log "VUELTA $i : AUDITOR ($MODELO_AUDITOR)"
  claude -p --model "$MODELO_AUDITOR" --dangerously-skip-permissions \
    --output-format json \
    "Estas en el repo de la campaña. Lee docs/loop/AUDITOR.md entero y actua como el auditor: verifica docs/loop/REPORTE.md contra el repo con tus propios comandos, haz la relectura ciega empezando por los discutibles marcados, adjudica lo adjudicable, registra tu acta en docs/loop/ACTA_AUDITOR.md (apendiendo), y escribe el encargo siguiente completo en docs/loop/PROMPT_SIGUIENTE.md. Si se cumple una condicion de parada de AUDITOR.md, escribe docs/loop/PARA_ALEXIS.md con el motivo y el estado, y deja PROMPT_SIGUIENTE.md vacio. Commitea y pushea docs/loop/ antes de terminar." \
    > "$LOOP/ultimo_auditor.json" 2>>"$LOOP/loop.log"
  c2="$(costo "$LOOP/ultimo_auditor.json")"; log "auditor listo${c2:+ (USD $c2)}"

  git pull --rebase origin "$RAMA" >/dev/null 2>&1 || true
done

log "Bucle terminado. Revisa $LOOP/PARA_ALEXIS.md si existe, y $LOOP/ACTA_AUDITOR.md."
