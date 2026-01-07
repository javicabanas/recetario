#!/usr/bin/env python3
import shutil

source = "/Users/javierfernandezcabanas/Library/Mobile Documents/com~apple~CloudDocs/Recetario/bebidas/imagenes/negroni.jpg"
dest = "/Users/javierfernandezcabanas/Library/Mobile Documents/com~apple~CloudDocs/Recetario/docs/bebidas/imagenes/negroni.jpg"

shutil.copy2(source, dest)
print(f"Copiado: {source} -> {dest}")
