#!/usr/bin/env python3
"""
Script de sincronización automática simplificado
- Sincroniza recetas e imágenes a docs/
- Actualiza estadísticas en index.md
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict

# Configuración
BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "docs"
CATEGORIAS = {
    "entrantes": "🥗 Entrantes",
    "principales": "🍖 Principales", 
    "arroces": "🍚 Arroces",
    "tapas": "🍷 Tapas",
    "guarniciones_y_salsas": "🥫 Guarniciones y Salsas",
    "bebidas": "🍹 Bebidas",
    "postres": "🍰 Postres"
}

def get_recipe_title(md_path):
    """Extrae el título de la receta desde el archivo .md"""
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('# '):
                    return line[2:].strip()
    except:
        pass
    # Fallback: usar nombre de archivo
    return md_path.stem.replace('_', ' ').replace('-', ' ').title()

def sync_recetas():
    """Sincroniza recetas e imágenes a estructura docs/"""
    print("🔄 Iniciando sincronización completa...\n")
    
    recetas_por_categoria = defaultdict(list)
    total_recetas = 0
    total_imagenes = 0
    
    for cat_id, cat_nombre in CATEGORIAS.items():
        cat_origen = BASE_DIR / cat_id
        cat_destino = DOCS_DIR / cat_id
        
        # Crear directorio destino
        cat_destino.mkdir(parents=True, exist_ok=True)
        
        # Copiar archivos .md
        if cat_origen.exists():
            for archivo_md in sorted(cat_origen.glob("*.md")):
                destino = cat_destino / archivo_md.name
                shutil.copy2(archivo_md, destino)
                
                # Guardar info de receta
                titulo = get_recipe_title(archivo_md)
                recetas_por_categoria[cat_id].append({
                    'path': f"{cat_id}/{archivo_md.name}",
                    'title': titulo
                })
                total_recetas += 1
                print(f"  ✓ {cat_id}/{archivo_md.name}")
            
            # Copiar carpeta de imágenes
            img_origen = cat_origen / "imagenes"
            img_destino = cat_destino / "imagenes"
            
            if img_origen.exists():
                if img_destino.exists():
                    shutil.rmtree(img_destino)
                shutil.copytree(img_origen, img_destino)
                imagenes = list(img_origen.glob("*.jpg")) + list(img_origen.glob("*.png"))
                total_imagenes += len(imagenes)
                print(f"  🖼️  {len(imagenes)} imágenes de {cat_id}")
        
        print()
    
    return recetas_por_categoria, total_recetas, total_imagenes

def update_index_stats(recetas_por_categoria, total_recetas):
    """Actualiza estadísticas en index.md"""
    index_path = DOCS_DIR / "index.md"
    
    if not index_path.exists():
        print("⚠️  index.md no encontrado, saltando actualización de estadísticas")
        return
    
    # Leer contenido actual
    with open(index_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Actualizar líneas
    new_lines = []
    for line in lines:
        if line.startswith("Este recetario digital es una compilación de"):
            new_lines.append(f"Este recetario digital es una compilación de **{total_recetas} recetas** cuidadosamente documentadas, diseñadas para preservar la autenticidad de la gastronomía española y facilitar su reproducción en cualquier cocina.\n")
        elif "| **Total** |" in line:
            new_lines.append(f"| **Total** | **{total_recetas}** |\n")
        elif any(f"### {CATEGORIAS[cat]}" in line for cat in CATEGORIAS):
            # Actualizar contadores de categorías
            for cat_id, cat_nombre in CATEGORIAS.items():
                if f"### {cat_nombre}" in line:
                    count = len(recetas_por_categoria.get(cat_id, []))
                    # Reemplazar el número entre paréntesis
                    import re
                    new_line = re.sub(r'\(\d+ recetas?\)', f'({count} receta{"s" if count != 1 else ""})', line)
                    new_lines.append(new_line)
                    break
            else:
                new_lines.append(line)
        elif any(f"| {CATEGORIAS[cat]}" in line for cat in CATEGORIAS):
            # Actualizar tabla de estadísticas
            for cat_id, cat_nombre in CATEGORIAS.items():
                if f"| {cat_nombre}" in line:
                    count = len(recetas_por_categoria.get(cat_id, []))
                    parts = line.split('|')
                    new_lines.append(f"{parts[0]}| {parts[1]}| {count} |\n")
                    break
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    
    # Guardar index.md actualizado
    with open(index_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("📊 Estadísticas actualizadas en index.md")

def main():
    print("=" * 60)
    print("SINCRONIZACIÓN AUTOMÁTICA DEL RECETARIO")
    print("=" * 60 + "\n")
    
    # Paso 1: Sincronizar archivos
    recetas, total_recetas, total_imagenes = sync_recetas()
    
    # Paso 2: Actualizar estadísticas
    update_index_stats(recetas, total_recetas)
    
    print("\n" + "=" * 60)
    print("✅ SINCRONIZACIÓN COMPLETADA")
    print("=" * 60)
    print(f"📝 {total_recetas} recetas sincronizadas")
    print(f"🖼️  {total_imagenes} imágenes copiadas")
    print(f"📂 {len([r for r in recetas.values() if r])} categorías activas")
    print("\n💡 Navegación en mkdocs.yml lista para usar")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
