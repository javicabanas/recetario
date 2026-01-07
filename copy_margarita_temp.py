#!/usr/bin/env python3
import shutil
from pathlib import Path

source = Path("/Users/javierfernandezcabanas/Library/Mobile Documents/com~apple~CloudDocs/Recetario/bebidas/imagenes/margarita.jpg")
dest = Path("/Users/javierfernandezcabanas/Library/Mobile Documents/com~apple~CloudDocs/Recetario/docs/bebidas/imagenes/margarita.jpg")

if source.exists():
    shutil.copy2(source, dest)
    print(f"✅ Imagen copiada: {dest}")
else:
    print(f"❌ Fuente no existe: {source}")
