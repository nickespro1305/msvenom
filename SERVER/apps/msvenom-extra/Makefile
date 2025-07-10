APP_NAME ?= msvenom-extra

all: prepare unzip install rename

prepare:
	@echo "🔧 Iniciando instalación de $(APP_NAME)..."

unzip:
	@echo "📦 Descomprimiendo Source.zip..."
	@tar -xf Source.zip

install:
	@echo "📥 Instalando dependencias..."
	@pip install -r extracted/requirements.txt

rename:
	@echo "🔄 Renombrando main.py a $(APP_NAME)..."
	@mv extracted/main.py $(APP_NAME).py
	@echo "✅ Instalación completada: ejecuta './$(APP_NAME)' para iniciar"
