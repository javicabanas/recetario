#!/usr/bin/env python3
"""
Script de sincronización automática para MkDocs
Copia recetas e imágenes de categorías a docs/
"""

import os
import shutil
from pathlib import Path

# Configuración
BASE_DIR = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Recetario"
DOCS_DIR = BASE_DIR / "docs"
CATEGORIAS = ["entrantes", "principales", "arroces", "tapas", "guarniciones_y_salsas", "postres"]

def sync_recetas():
    """Sincroniza recetas e imágenes a estructura docs/"""
    print("🔄 Iniciando sincronización...\n")
    
    recetas_copiadas = 0
    imagenes_copiadas = 0
    
    for categoria in CATEGORIAS:
        cat_origen = BASE_DIR / categoria
        cat_destino = DOCS_DIR / categoria
        
        # Crear directorio destino
        cat_destino.mkdir(parents=True, exist_ok=True)
        
        # Copiar archivos .md
        if cat_origen.exists():
            for archivo_md in cat_origen.glob("*.md"):
                destino = cat_destino / archivo_md.name
                shutil.copy2(archivo_md, destino)
                recetas_copiadas += 1
                print(f"  ✓ {categoria}/{archivo_md.name}")
            
            # Copiar carpeta de imágenes
            img_origen = cat_origen / "imagenes"
            img_destino = cat_destino / "imagenes"
            
            if img_origen.exists():
                # Eliminar carpeta destino si existe
                if img_destino.exists():
                    shutil.rmtree(img_destino)
                
                # Copiar carpeta completa
                shutil.copytree(img_origen, img_destino)
                imagenes = list(img_origen.glob("*.[jp][pn]g"))
                imagenes_copiadas += len(imagenes)
                print(f"  🖼️  {len(imagenes)} imágenes de {categoria}")
        
        print()
    
    print(f"✅ Sincronización completada:")
    print(f"   📝 {recetas_copiadas} recetas copiadas")
    print(f"   🖼️  {imagenes_copiadas} imágenes copiadas")

if __name__ == "__main__":
    os.chdir(BASE_DIR)
    sync_recetas()
