APP_NAME ?= msvenom-extra

all: prepare unzip install rename

prepare:
	@echo "🔧 Iniciando instalación de $(APP_NAME)..."

unzip:
	@echo "📦 Descomprimiendo Source.zip..."
	@powershell -Command "Expand-Archive -Force Source.zip -DestinationPath '.'"

install:
	@echo "📥 Instalando dependencias..."
	@pip install -r requirements.txt

rename:
	@echo "🔄 Renombrando main.py a $(APP_NAME)..."
	@cmd /c move /Y extracted\main.py $(APP_NAME).py
	@echo "✅ Instalación completada: ejecuta './$(APP_NAME)' para iniciar"
