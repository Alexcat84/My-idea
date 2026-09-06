set -e
cd "C:/Users/AlexDesk/Documents/I have an idea"
echo "=== 1. run_phase1 --reaplico-curaduria"; python scripts/run_phase1.py --reaplico-curaduria 2>&1 | tail -25
echo "EXITCODE=$?"
echo "=== 2. etiquetas_de_cara --aplicar"; python scripts/etiquetas_de_cara.py --aplicar 2>&1 | tail -6
echo "=== 3. sync_assets_web"; python scripts/sync_assets_web.py 2>&1 | tail -6
echo "=== 4. numstat dataset/ web/ engine/"; git diff HEAD --numstat -- dataset/ web/ engine/ | wc -l
echo "=== 5. engine/run_all_tests.py"; python engine/run_all_tests.py 2>&1 | tail -8
echo "=== 6. tsc"; cd web && npx tsc --noEmit -p tsconfig.json 2>&1 | tail -5; echo "TSC_EXIT=$?"
echo "=== 7. pnpm test"; pnpm test 2>&1 | tail -12
