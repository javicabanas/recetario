#!/bin/bash
# Script para copiar la imagen del Bloody Mary generada por nano-banana

SRC="/Users/javierfernandezcabanas/nanobanana-images/gen_20260106_231412_1_1_fd28a11c.png"
DST="/Users/javierfernandezcabanas/Library/Mobile Documents/com~apple~CloudDocs/Recetario/bebidas/imagenes/bloody_mary.jpg"

if [ -f "$SRC" ]; then
    cp "$SRC" "$DST"
    echo "✅ Imagen copiada exitosamente a $DST"
else
    echo "❌ Error: No se encontró la imagen fuente en $SRC"
    echo "Por favor, verifica la ruta o copia manualmente la imagen."
fi
