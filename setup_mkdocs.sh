#!/bin/bash
# EJECUTAR ESTE SCRIPT PARA COMPLETAR LA CONFIGURACIÓN
# chmod +x setup_mkdocs.sh && ./setup_mkdocs.sh

cd "$HOME/Library/Mobile Documents/com~apple~CloudDocs/Recetario" || exit 1

echo "🔧 Configurando MkDocs Material para tu recetario..."
echo ""

# Paso 1: Copiar recetas a docs/
echo "📝 Copiando recetas..."
for cat in entrantes principales arroces tapas guarniciones_y_salsas postres; do
  mkdir -p "docs/$cat"
  if [ -d "$cat" ]; then
    cp "$cat"/*.md "docs/$cat/" 2>/dev/null && echo "  ✓ $cat"
  fi
done

# Paso 2: Copiar imágenes a docs/
echo ""
echo "🖼️  Copiando imágenes..."
for cat in entrantes principales arroces tapas guarniciones_y_salsas postres; do
  if [ -d "$cat/imagenes" ]; then
    cp -r "$cat/imagenes" "docs/$cat/" && echo "  ✓ $cat/imagenes"
  fi
done

echo ""
echo "✅ Estructura MkDocs lista!"
echo ""
echo "📋 Siguiente paso:"
echo "   1. Instala MkDocs: make install"
echo "   2. Visualiza local: make serve"
echo "   3. Configura GitHub: sigue README.md"
echo ""
