import os
import glob

files = glob.glob(r"C:\Users\AlexDesk\Documents\I have an idea\dataset\nodos\*.json")
names = [os.path.basename(f).replace('.json', '') for f in files]

print("--- MVP ---")
for n in names:
    if 'mvp' in n or 'minimo_viable' in n or 'minimum_viable' in n:
        print(n)

print("\n--- CANVAS ---")
for n in names:
    if 'canvas' in n or 'lienzo' in n:
        print(n)
