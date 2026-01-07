#!/usr/bin/env python3
import shutil
from pathlib import Path

source = Path("/Users/javierfernandezcabanas/Library/Mobile Documents/com~apple~CloudDocs/Recetario/bebidas/imagenes/margarita.jpg")
dest = Path("/Users/javierfernandezcabanas/Library/Mobile Documents/com~apple~CloudDocs/Recetario/docs/bebidas/imagenes/margarita.jpg")

try:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, dest)
    print(f"✅ Imagen copiada exitosamente")
    print(f"   Origen: {source}")
    print(f"   Destino: {dest}")
except Exception as e:
    print(f"❌ Error al copiar imagen: {e}")
