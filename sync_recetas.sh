#!/bin/bash
# Script de sincronización de recetas a estructura MkDocs

RECETARIO_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Recetario"
cd "$RECETARIO_DIR" || exit 1

echo "🔄 Sincronizando recetas a estructura docs/..."

# Crear directorios de categorías en docs/
for categoria in entrantes principales arroces tapas guarniciones_y_salsas postres; do
  mkdir -p "docs/$categoria"
  echo "  ✓ Carpeta docs/$categoria creada"
done

# Copiar archivos .md (excepto INDICE.md y README.md)
echo ""
echo "📝 Copiando archivos de recetas..."
for categoria in entrantes principales arroces tapas guarniciones_y_salsas postres; do
  if [ -d "$categoria" ]; then
    cp "$categoria"/*.md "docs/$categoria/" 2>/dev/null && \
      echo "  ✓ Recetas de $categoria copiadas" || \
      echo "  ⚠ No hay recetas en $categoria"
  fi
done

# Copiar carpetas de imágenes
echo ""
echo "🖼️  Copiando carpetas de imágenes..."
for categoria in entrantes principales arroces tapas guarniciones_y_salsas postres; do
  if [ -d "$categoria/imagenes" ]; then
    cp -r "$categoria/imagenes" "docs/$categoria/" && \
      echo "  ✓ Imágenes de $categoria copiadas" || \
      echo "  ⚠ No hay imágenes en $categoria"
  fi
done

echo ""
echo "✅ Sincronización completada"
echo ""
echo "📊 Resumen:"
find docs -name "*.md" ! -name "index.md" | wc -l | xargs echo "  Recetas copiadas:"
find docs -name "*.jpg" -o -name "*.png" | wc -l | xargs echo "  Imágenes copiadas:"
