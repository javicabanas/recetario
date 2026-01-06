.PHONY: help install sync serve deploy clean init-git

help: ## Mostrar esta ayuda
	@echo "======================================================"
	@echo "RECETARIO ESPAÑOL - Comandos Disponibles"
	@echo "======================================================"
	@echo ""
	@echo "  make install   - Instalar dependencias (solo primera vez)"
	@echo "  make sync      - Sincronizar recetas automáticamente"
	@echo "  make serve     - Ver sitio localmente (http://localhost:8000)"
	@echo "  make deploy    - PUBLICAR cambios al sitio web"
	@echo "  make init-git  - Configurar Git (solo primera vez)"
	@echo "  make clean     - Limpiar archivos temporales"
	@echo ""
	@echo "======================================================"

install: ## Instalar MkDocs y dependencias
	@echo "📦 Instalando MkDocs Material + PyYAML..."
	@if ! command -v pipx &> /dev/null; then \
		echo "🔧 Instalando pipx..."; \
		brew install pipx; \
		pipx ensurepath; \
	fi
	@echo "📦 Instalando mkdocs (comando base)..."
	@pipx install mkdocs --force || pipx upgrade mkdocs
	@echo "📦 Instalando tema Material y plugins..."
	@pipx inject mkdocs mkdocs-material mkdocs-print-site-plugin pyyaml
	@echo "✅ Instalación completada"
	@echo ""
	@echo "💡 Verifica la instalación con: mkdocs --version"

sync: ## Sincronizar recetas automáticamente
	@python3 auto_sync.py

serve: sync ## Servidor local para previsualizar
	@echo "🌐 Iniciando servidor local en http://localhost:8000"
	@echo "   Presiona Ctrl+C para detener"
	@mkdocs serve

deploy: sync ## Publicar al sitio web
	@echo "🚀 Preparando deployment..."
	@if [ ! -d .git ]; then \
		echo ""; \
		echo "❌ ERROR: Git no está configurado"; \
		echo ""; \
		echo "Ejecuta primero:"; \
		echo "  make init-git"; \
		echo ""; \
		exit 1; \
	fi
	@echo "📝 Guardando cambios..."
	@git add .
	@printf "Mensaje del commit [Actualización automática]: "; \
	read msg; \
	git commit -m "$${msg:-Actualización automática del recetario}" || true
	@echo "📤 Subiendo a GitHub..."
	@git push origin main
	@echo ""
	@echo "======================================================"
	@echo "✅ DEPLOYMENT COMPLETADO"
	@echo "======================================================"
	@echo "El sitio se actualizará en 2-3 minutos"
	@echo ""
	@repo=$$(git config --get remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/'); \
	echo "🌐 URL: https://$${repo%.*}.github.io/$${repo##*/}"
	@echo "======================================================"

init-git: ## Inicializar repositorio Git
	@echo "======================================================"
	@echo "CONFIGURACIÓN INICIAL DE GIT"
	@echo "======================================================"
	@echo ""
	@if [ -d .git ]; then \
		echo "✅ Git ya está configurado"; \
		git remote -v; \
		exit 0; \
	fi
	@echo "1️⃣  Inicializando repositorio Git..."
	@git init
	@git branch -M main
	@echo ""
	@echo "2️⃣  Crea tu repositorio en GitHub:"
	@echo "   https://github.com/new"
	@echo ""
	@echo "   - Nombre: recetario"
	@echo "   - Visibilidad: Public"
	@echo "   - NO inicialices con README"
	@echo ""
	@printf "3️⃣  Pega la URL de tu repositorio: "; \
	read repo; \
	git remote add origin $$repo; \
	echo ""; \
	echo "✅ Git configurado correctamente"
	@echo ""
	@echo "======================================================"
	@echo "SIGUIENTE PASO: Actualizar mkdocs.yml"
	@echo "======================================================"
	@repo=$$(git config --get remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/'); \
	usuario=$${repo%%/*}; \
	echo ""; \
	echo "Abre mkdocs.yml y reemplaza 'TU_USUARIO' con: $$usuario"; \
	echo ""; \
	echo "Luego ejecuta: make deploy"
	@echo "======================================================"

clean: ## Limpiar archivos temporales
	@echo "🧹 Limpiando archivos temporales..."
	@rm -rf site/
	@find . -name ".DS_Store" -delete
	@find . -name "__pycache__" -delete
	@find . -name "*.pyc" -delete
	@echo "✅ Limpieza completada"
