# 🚀 INICIO RÁPIDO - Sabores de Familia

### Recetario Familiar Espíndola-Serrano-Fernández Cabanas

## ⏱️ Configuración en 5 Minutos

### 📋 Requisitos Previos
```bash
# Verificar que tienes Python 3
python3 --version

# Si NO tienes Python, instálalo:
brew install python3
```

---

## 🎯 CONFIGURACIÓN INICIAL (Una sola vez)

### **PASO 1:** Instalar Dependencias
```bash
cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/Recetario
make install
```

### **PASO 2:** Crear Repositorio en GitHub
1. Ve a: https://github.com/new
2. Configura:
   - **Nombre:** `recetario`
   - **Visibilidad:** Public
   - ❌ **NO** marcar "Add a README file"
3. Clic en **"Create repository"**
4. **Copia la URL** que aparece (ej: `https://github.com/TU_USUARIO/recetario.git`)

### **PASO 3:** Conectar Git
```bash
make init-git
# Pega la URL cuando te la pida
```

### **PASO 4:** Activar GitHub Pages
1. Ve a tu repositorio en GitHub
2. **Settings** → **Pages** (menú izquierdo)
3. En **Source**, selecciona: **GitHub Actions**
4. Guarda

### **PASO 5:** Actualizar mkdocs.yml
```bash
# Abre el archivo
open mkdocs.yml

# Busca esta línea:
repo_url: https://github.com/TU_USUARIO/recetario

# Reemplaza TU_USUARIO con tu usuario real de GitHub
# Guarda el archivo
```

### **PASO 6:** Primera Publicación
```bash
make deploy
# Escribe un mensaje: "feat: configuración inicial"
```

✅ **¡LISTO!** Tu sitio estará en: `https://TU_USUARIO.github.io/recetario`

---

## 📝 USO DIARIO

### Workflow Completo con Claude

```
1. Tú dices: "Claude, crea receta Gazpacho Andaluz"
   ↓
2. Claude ejecuta automáticamente:
   ✓ Crea /entrantes/gazpacho_andaluz.md
   ✓ Genera imagen en /entrantes/imagenes/gazpacho_andaluz.jpg
   ✓ Actualiza INDICE.md
   ↓
3. Tú ejecutas en Terminal:
   $ make deploy
   Mensaje: feat(entrantes): añadir gazpacho andaluz
   ↓
4. ✅ Receta publicada automáticamente en 2-3 minutos
```

### Comandos Esenciales

```bash
# Ver recetas localmente antes de publicar
make serve
# → http://localhost:8000

# Publicar cambios
make deploy

# Limpiar archivos temporales
make clean
```

---

## 🔍 Verificar que Todo Funciona

### Test Local
```bash
make serve
```
- Abre http://localhost:8000
- Navega por las categorías
- Presiona Ctrl+C para detener

### Test de Publicación
```bash
make deploy
```
- Espera 2-3 minutos
- Visita: `https://TU_USUARIO.github.io/recetario`

---

## 🎨 Personalización (Opcional)

### Cambiar Colores
Edita `mkdocs.yml`:
```yaml
theme:
  palette:
    primary: red      # Color principal
    accent: amber     # Color de acento
```

### Añadir Logo
1. Guarda tu logo en `docs/assets/logo.png`
2. En `mkdocs.yml`:
```yaml
theme:
  logo: assets/logo.png
```

---

## 🆘 Solución de Problemas

### "pip3: command not found"
```bash
brew install python3
```

### "make: command not found"
```bash
xcode-select --install
```

### "Permission denied" al hacer push
```bash
# Configurar credenciales de GitHub
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### Las imágenes no se ven
- Verifica ruta: `![Imagen](./imagenes/nombre.jpg)`
- Ejecuta: `make sync` → `make deploy`

---

## 📱 Compartir con Amigos

**Envía este enlace:**
```
https://TU_USUARIO.github.io/recetario
```

**Instrucciones para ellos:**
1. Abrir enlace en cualquier navegador
2. Navegar por categorías o buscar
3. Imprimir: Ctrl+P (Windows/Android) o Cmd+P (Mac/iOS)

---

## 💡 Tips Profesionales

### Previsualizar Antes de Publicar
```bash
make serve      # Ver cambios localmente
# Ctrl+C para detener
make deploy     # Publicar si todo se ve bien
```

### Commits Descriptivos
```bash
# Al hacer make deploy, usa mensajes claros:
feat(entrantes): añadir gazpacho andaluz
fix(arroces): corregir tiempo paella
docs: actualizar índice
```

### Backup Automático
iCloud Drive ya hace backup. Para seguridad extra:
```bash
# Clonar en otro lugar
cd ~/Desktop
git clone https://github.com/TU_USUARIO/recetario.git recetario-backup
```

---

## 📊 Estado del Sistema

```bash
# Ver recetas sincronizadas
make sync

# Ver estadísticas de Git
cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/Recetario
git log --oneline -5
```

---

## 🔗 Enlaces Útiles

- **GitHub Pages:** https://pages.github.com
- **MkDocs Material:** https://squidfunk.github.io/mkdocs-material
- **Markdown Guide:** https://www.markdownguide.org

---

*Configurado el 6 de enero de 2026*
