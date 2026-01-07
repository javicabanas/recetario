#!/bin/bash
# Script para copiar la imagen de torta de milanesa al directorio correcto

SRC="/Users/javierfernandezcabanas/nanobanana-images/gen_20260106_190932_1_1_30179a91.png"
DST="/Users/javierfernandezcabanas/Library/Mobile Documents/com~apple~CloudDocs/Recetario/principales/imagenes/torta_de_milanesa.jpg"

if [ -f "$SRC" ]; then
    cp "$SRC" "$DST"
    echo "✓ Imagen copiada exitosamente a: $DST"
    # Copiar también al directorio docs para el sitio web
    cp "$SRC" "/Users/javierfernandezcabanas/Library/Mobile Documents/com~apple~CloudDocs/Recetario/docs/principales/imagenes/torta_de_milanesa.jpg"
    echo "✓ Imagen copiada también a docs/"
else
    echo "✗ Error: No se encontró el archivo fuente: $SRC"
    exit 1
fi
