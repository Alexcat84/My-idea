#!/usr/bin/env bash
# Bucle autonomo de la campaña My Idea: ejecutor (Opus 4.8) + auditor (Fable 5).
# Se corre UNA vez, idealmente dentro de tmux:  bash orquestador.sh
# Se detiene solo si: existe docs/loop/PARA_ALEXIS.md, no hay prompt siguiente,
# se alcanza MAX_VUELTAS, o una invocacion falla 7 veces seguidas por una de las
# dos especies que el orquestador vigila: instantanea (probable limite de uso
# agotado) o auditor mudo (el turno corrio y cobro, pero no escribio su acta).
# El estado vive en el repo; cada vuelta sobrevive a caidas porque todo se
# commitea y pushea.
set -uo pipefail
cd "$(dirname "$0")"

MAX_VUELTAS="${MAX_VUELTAS:-20}"
MODELO_EJECUTOR="${MODELO_EJECUTOR:-claude-opus-4-8}"
MODELO_AUDITOR="${MODELO_AUDITOR:-claude-fable-5}"
# El bucle vive en su propia rama. El merge a staging o a produccion es
# SIEMPRE decision del fundador, nunca del bucle.
RAMA="${RAMA:-bucle}"
LOOP="docs/loop"
mkdir -p "$LOOP"

# Deteccion de fallo instantaneo (probable limite de uso agotado). Una
# invocacion que dura menos del umbral, o que no reporta costo positivo, no
# hizo trabajo real: se espera y se reintenta la MISMA invocacion, sin
# avanzar de rol. MAX_INTENTOS cuenta el intento original mas los reintentos:
# 7 intentos totales equivalen a 6 reintentos seguidos.
UMBRAL_SEGUNDOS=120
ESPERA_SEGUNDOS=1800
MAX_INTENTOS=7

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOOP/loop.log"; }

costo() { # extrae total_cost_usd del json de salida de claude
  local archivo="$1" valor=""
  if command -v jq >/dev/null 2>&1; then
    valor="$(jq -r '.total_cost_usd // empty' "$archivo" 2>/dev/null)"
  fi
  if [ -z "$valor" ]; then
    # respaldo sin jq: extrae el numero directo del json de salida
    valor="$(grep -oE '"total_cost_usd"[[:space:]]*:[[:space:]]*[0-9.]+' "$archivo" 2>/dev/null \
      | grep -oE '[0-9.]+$' | head -1)"
  fi
  printf '%s' "$valor"
}

costo_mayor_que_cero() { # $1 = valor de costo, puede venir vacio
  [ -n "$1" ] && awk -v v="$1" 'BEGIN{exit !(v+0>0)}'
}

hash_fichero() { # $1 = ruta. Vacio si no existe: asi un fichero que NACE cuenta como cambio.
  local archivo="$1"
  [ -f "$archivo" ] || { printf ''; return 0; }
  git hash-object "$archivo" 2>/dev/null || printf 'sin-hash'
}

para_alexis_por_fallo_instantaneo() { # rol modelo vuelta duracion costo motivo
  local rol="$1" modelo="$2" vuelta="$3" duracion="$4" c="$5" motivo="${6:-instantaneo}"
  cat > "$LOOP/PARA_ALEXIS.md" <<EOF
# PARA_ALEXIS: el bucle se detuvo por fallo repetido del $rol

Motivo: la invocacion del $rol ($modelo) fallo $MAX_INTENTOS veces seguidas en
la vuelta $vuelta del bucle, por la especie "$motivo".

Las DOS especies que el orquestador trata igual (esperar 30 minutos y
reintentar el MISMO turno, sin avanzar de rol):

- instantaneo: la invocacion duro menos de $UMBRAL_SEGUNDOS segundos, o el
  json de salida no trae total_cost_usd mayor que 0. Es el patron esperable
  de un limite de uso agotado: el rol no llego a trabajar.
- auditor mudo: el turno corrio y cobro, pero docs/loop/ACTA_AUDITOR.md
  quedo IDENTICO al de antes del turno. Es lo que paso de verdad en la
  vuelta 34 (15 ago 2026): el auditor corrio dieciocho minutos y termino sin
  escribir acta, y la vuelta 35 arranco con el encargo de la 34 ya
  ejecutado y sin nadie que lo hubiera verificado.

Ultimo intento: duracion ${duracion}s, costo reportado "${c:-vacio}".

Estado: rama $RAMA, hash $(git rev-parse --short HEAD 2>/dev/null || echo desconocido).

Lo que se necesita de Alexis: confirmar si el limite de uso ya se libero.

Como retomar: borra este fichero cuando el motivo ya no aplique y vuelve a
correr bash orquestador.sh. El bucle sigue leyendo docs/loop/PROMPT_SIGUIENTE.md
desde donde quedo; no hace falta rehacer nada.
EOF
  git add "$LOOP/PARA_ALEXIS.md"
  git commit -m "Bucle detenido: fallo instantaneo repetido del $rol" >>"$LOOP/loop.log" 2>&1
  git push origin "$RAMA" >>"$LOOP/loop.log" 2>&1
}

invocar_claude() { # rol modelo prompt salida vuelta [testigo]
  # TESTIGO (opcional, 15 ago 2026): fichero que el turno TIENE que haber
  # cambiado para contar como trabajo hecho. Nace de la vuelta 34, donde el
  # auditor corrio dieciocho minutos, cobro, y termino sin escribir acta: el
  # turno parecia bueno por duracion y por costo, y no lo era. Un turno que no
  # movio su testigo se trata IGUAL que el fallo instantaneo: se espera y se
  # reintenta el MISMO turno, sin avanzar de rol y con el mismo tope.
  local rol="$1" modelo="$2" prompt="$3" salida="$4" vuelta="$5" testigo="${6:-}"
  local intento inicio duracion c hash_antes hash_despues motivo
  for intento in $(seq 1 "$MAX_INTENTOS"); do
    hash_antes="$(hash_fichero "$testigo")"
    inicio=$SECONDS
    claude -p --model "$modelo" --dangerously-skip-permissions \
      --output-format json \
      "$prompt" \
      > "$salida" 2>>"$LOOP/loop.log"
    duracion=$((SECONDS - inicio))
    c="$(costo "$salida")"
    hash_despues="$(hash_fichero "$testigo")"

    motivo=""
    if [ "$duracion" -lt "$UMBRAL_SEGUNDOS" ] || ! costo_mayor_que_cero "$c"; then
      motivo="instantaneo"
    elif [ -n "$testigo" ] && [ "$hash_antes" = "$hash_despues" ]; then
      motivo="auditor mudo"
    fi

    if [ -z "$motivo" ]; then
      log "$rol listo${c:+ (USD $c)}, ${duracion}s, intento $intento de $MAX_INTENTOS"
      return 0
    fi

    if [ "$motivo" = "auditor mudo" ]; then
      log "$rol: AUDITOR MUDO, el turno corrio ${duracion}s y cobro \"${c:-vacio}\" pero $testigo quedo identico, intento $intento de $MAX_INTENTOS"
    else
      log "$rol: fallo instantaneo (probable limite de uso), ${duracion}s, costo \"${c:-vacio}\", intento $intento de $MAX_INTENTOS"
    fi
    if [ "$intento" -eq "$MAX_INTENTOS" ]; then
      para_alexis_por_fallo_instantaneo "$rol" "$modelo" "$vuelta" "$duracion" "$c" "$motivo"
      log "DETENIDO en la vuelta $vuelta: $rol fallo por \"$motivo\" $MAX_INTENTOS veces seguidas. Ver $LOOP/PARA_ALEXIS.md"
      exit 1
    fi
    log "fallo \"$motivo\"; espero 30 minutos y reintento"
    sleep "$ESPERA_SEGUNDOS"
  done
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
  invocar_claude "ejecutor" "$MODELO_EJECUTOR" \
    "Estas en el repo de la campaña. Lee docs/loop/EJECUTOR.md (tus reglas permanentes) y despues docs/loop/PROMPT_SIGUIENTE.md (tu encargo). Ejecuta el encargo al pie de la letra. Escribe tu reporte completo en docs/loop/REPORTE.md sobrescribiendo el anterior, con los discutibles marcados. Commitea y pushea TODO a la rama activa antes de terminar." \
    "$LOOP/ultimo_ejecutor.json" "$i"

  git pull --rebase origin "$RAMA" >/dev/null 2>&1 || true

  log "VUELTA $i : AUDITOR ($MODELO_AUDITOR)"
  invocar_claude "auditor" "$MODELO_AUDITOR" \
    "Estas en el repo de la campaña. Lee docs/loop/AUDITOR.md entero y actua como el auditor: verifica docs/loop/REPORTE.md contra el repo con tus propios comandos, haz la relectura ciega empezando por los discutibles marcados, adjudica lo adjudicable, registra tu acta en docs/loop/ACTA_AUDITOR.md (apendiendo), y escribe el encargo siguiente completo en docs/loop/PROMPT_SIGUIENTE.md. Si se cumple una condicion de parada de AUDITOR.md, escribe docs/loop/PARA_ALEXIS.md con el motivo y el estado, y deja PROMPT_SIGUIENTE.md vacio. Commitea y pushea docs/loop/ antes de terminar." \
    "$LOOP/ultimo_auditor.json" "$i" "$LOOP/ACTA_AUDITOR.md"

  git pull --rebase origin "$RAMA" >/dev/null 2>&1 || true
done

log "Bucle terminado. Revisa $LOOP/PARA_ALEXIS.md si existe, y $LOOP/ACTA_AUDITOR.md."
