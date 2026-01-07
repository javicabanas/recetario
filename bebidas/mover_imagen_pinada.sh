#!/bin/bash
# Script para copiar la imagen de la Piñada generada por nano-banana

SRC="/Users/javierfernandezcabanas/nanobanana-images/gen_20260106_234136_1_1_24953105.png"
DST="/Users/javierfernandezcabanas/Library/Mobile Documents/com~apple~CloudDocs/Recetario/bebidas/imagenes/pinada.jpg"

if [ -f "$SRC" ]; then
    cp "$SRC" "$DST"
    echo "✅ Imagen de Piñada copiada exitosamente a $DST"
else
    echo "❌ Error: No se encontró la imagen fuente en $SRC"
    echo "Por favor, verifica la ruta o copia manualmente la imagen."
fi
