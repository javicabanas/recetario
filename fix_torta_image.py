#!/usr/bin/env python3
"""
Script para copiar correctamente la imagen de torta de milanesa
"""
import shutil
from pathlib import Path

# Rutas
src = Path("/Users/javierfernandezcabanas/nanobanana-images/gen_20260106_190932_1_1_30179a91.png")
dst1 = Path("/Users/javierfernandezcabanas/Library/Mobile Documents/com~apple~CloudDocs/Recetario/principales/imagenes/torta_de_milanesa.jpg")
dst2 = Path("/Users/javierfernandezcabanas/Library/Mobile Documents/com~apple~CloudDocs/Recetario/docs/principales/imagenes/torta_de_milanesa.jpg")

def main():
    if not src.exists():
        print(f"❌ Error: Archivo fuente no encontrado: {src}")
        return 1
    
    print(f"📁 Fuente: {src}")
    print(f"   Tamaño: {src.stat().st_size:,} bytes")
    
    # Crear directorios si no existen
    dst1.parent.mkdir(parents=True, exist_ok=True)
    dst2.parent.mkdir(parents=True, exist_ok=True)
    
    # Eliminar archivos corruptos si existen
    if dst1.exists():
        dst1.unlink()
        print(f"🗑️  Eliminado archivo corrupto: {dst1}")
    
    if dst2.exists():
        dst2.unlink()
        print(f"🗑️  Eliminado archivo corrupto: {dst2}")
    
    # Copiar archivos
    shutil.copy2(src, dst1)
    print(f"✅ Copiado a: {dst1}")
    print(f"   Tamaño: {dst1.stat().st_size:,} bytes")
    
    shutil.copy2(src, dst2)
    print(f"✅ Copiado a: {dst2}")
    print(f"   Tamaño: {dst2.stat().st_size:,} bytes")
    
    print("\n✅ ¡Imagen copiada correctamente!")
    return 0

if __name__ == "__main__":
    exit(main())
