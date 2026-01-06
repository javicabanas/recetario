# 📚 Recetario Familiar Espíndola-Serrano-Fernández Cabanas - Guía de Configuración

Sistema de publicación automatizada de recetas usando MkDocs Material + GitHub Pages.

---

## 🎯 Resultado Final

Tu recetario estará disponible en: `https://TU_USUARIO.github.io/recetario`

**Características:**
- ✅ Accesible desde cualquier dispositivo (Android, iOS, PC)
- ✅ Navegación por categorías + búsqueda
- ✅ Impresión profesional con Ctrl+P
- ✅ Actualización automática al hacer `make deploy`
- ✅ Solo lectura para visitantes

---

## 📦 Instalación Inicial (Una sola vez)

### Paso 1: Instalar Herramientas Básicas

```bash
# Instalar Homebrew (si no lo tienes)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python y Git
brew install python3 git

# Instalar MkDocs Material
pip3 install mkdocs-material mkdocs-print-site-plugin
```

### Paso 2: Crear Repositorio en GitHub

1. Ve a https://github.com/new
2. Configura:
   - **Nombre:** `recetario`
   - **Visibilidad:** Public (necesario para GitHub Pages gratuito)
   - **NO inicialices con README** (ya tienes archivos)
3. Copia la URL del repositorio (ej: `https://github.com/TU_USUARIO/recetario.git`)

### Paso 3: Conectar Repositorio Local

```bash
cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/Recetario

# Inicializar Git
git init
git branch -M main

# Conectar con GitHub (reemplaza con TU URL)
git remote add origin https://github.com/TU_USUARIO/recetario.git

# Primer commit
git add .
git commit -m "chore: configuración inicial del recetario"
git push -u origin main
```

### Paso 4: Activar GitHub Pages

1. Ve a tu repositorio en GitHub
2. **Settings** → **Pages** (menú lateral izquierdo)
3. En **Source**, selecciona: **GitHub Actions**
4. Guarda los cambios

### Paso 5: Actualizar mkdocs.yml

Abre `mkdocs.yml` y reemplaza `TU_USUARIO` con tu usuario real de GitHub:

```yaml
repo_url: https://github.com/TU_USUARIO/recetario
```

---

## 🚀 Uso Diario

### Flujo de Trabajo Completo

```
1. Tú: "Claude, crea receta Gazpacho Andaluz"
   ↓
2. Claude: Crea receta + imagen + actualiza índice
   ↓
3. Tú ejecutas en Terminal:
   make deploy
   ↓
4. ✅ Receta publicada automáticamente en 2-3 minutos
```

### Comandos Disponibles

```bash
# Ver recetario localmente antes de publicar
make serve
# Abre http://localhost:8000 en tu navegador

# Publicar cambios al sitio web
make deploy

# Limpiar archivos temporales
make clean

# Ver ayuda de comandos
make help
```

---

## 📝 Workflow de Nueva Receta

### Ejemplo Real

```
Usuario: "Crea receta Gazpacho Andaluz"

Claude ejecuta automáticamente:
1. Escribir /entrantes/gazpacho_andaluz.md
2. Generar /entrantes/imagenes/gazpacho_andaluz.jpg
3. Actualizar /INDICE.md
4. Actualizar mkdocs.yml (añadir a navegación)
5. ✅ Confirma: "Receta creada en categoría ENTRANTES"

Usuario ejecuta en Terminal:
$ cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/Recetario
$ make deploy
Mensaje del commit [Actualización automática]: feat(entrantes): añadir gazpacho andaluz
✅ Deployment iniciado

GitHub Actions:
- Detecta cambios
- Regenera sitio web
- Publica automáticamente

Resultado:
https://TU_USUARIO.github.io/recetario/entrantes/gazpacho_andaluz
```

---

## 🔧 Mantenimiento

### Actualizar Estructura de Navegación

Si añades/eliminas recetas manualmente, actualiza `mkdocs.yml`:

```yaml
nav:
  - Entrantes:
    - entrantes/nueva_receta.md  # Añadir aquí
```

Luego ejecuta `make deploy`.

### Cambiar Tema o Colores

Edita `mkdocs.yml`:

```yaml
theme:
  palette:
    primary: red      # Color principal (actual: rojo español)
    accent: amber     # Color de acento (actual: amarillo español)
```

### Problemas Comunes

**Error: "no changes to commit"**
- Normal si no hay cambios. El sitio ya está actualizado.

**Error: "failed to push"**
- Solución: `git pull origin main` → Luego `make deploy`

**Las imágenes no se ven en el sitio**
- Verifica que estén en `/categoría/imagenes/nombre.jpg`
- El enlace en el .md debe ser: `![Imagen](./imagenes/nombre.jpg)`

---

## 📂 Estructura de Archivos

```
Recetario/
├── mkdocs.yml              # Configuración del sitio
├── Makefile                # Comandos simplificados
├── README.md               # Este archivo
├── .gitignore              # Archivos a ignorar en Git
├── .github/
│   └── workflows/
│       └── deploy.yml      # Automatización de publicación
├── docs/
│   ├── index.md            # Página de inicio
│   └── stylesheets/
│       ├── print.css       # Estilos de impresión
│       └── extra.css       # Estilos adicionales
├── entrantes/
│   ├── *.md                # Recetas de entrantes
│   └── imagenes/           # Imágenes de entrantes
├── principales/
├── arroces/
├── tapas/
├── guarniciones_y_salsas/
└── postres/
```

---

## 🌐 Compartir con Amigos

### Enlace Único

Envía a tus amigos:
```
https://TU_USUARIO.github.io/recetario
```

### Instrucciones para Ellos

1. Abrir enlace en cualquier navegador
2. Navegar por categorías o usar búsqueda
3. Para imprimir: Ctrl+P (Windows/Android) o Cmd+P (Mac/iOS)
4. Marcar como favorito para acceso rápido

**Nota:** El sitio se actualiza automáticamente cuando tú publicas cambios.

---

## 🔒 Privacidad

- **Repositorio público:** Necesario para GitHub Pages gratuito
- **Alternativa privada:** Upgrade a GitHub Pro ($4/mes) permite repos privados con Pages

---

## 💡 Tips Profesionales

### Previsualizar Antes de Publicar

```bash
make serve
# Abre http://localhost:8000
# Verifica que todo se vea bien
# Presiona Ctrl+C para detener
make deploy
```

### Commits Descriptivos

Al hacer `make deploy`, escribe mensajes claros:
```
feat(entrantes): añadir gazpacho andaluz
fix(arroces): corregir tiempo de cocción en paella
docs: actualizar índice con nuevas recetas
```

### Backup Manual

iCloud Drive ya hace backup automático. Para seguridad extra:
```bash
# Exportar todas las recetas a PDF
for file in */*.md; do
  pandoc "$file" -o "${file%.md}.pdf"
done
```

---

## 📞 Soporte

**Problema técnico con GitHub:**
- Consulta: https://docs.github.com/pages

**Problema con MkDocs:**
- Documentación: https://squidfunk.github.io/mkdocs-material/

**Problema con Claude:**
- "Claude, ayúdame a resolver [problema específico]"

---

*Sistema configurado por Claude el 6 de enero de 2026*
