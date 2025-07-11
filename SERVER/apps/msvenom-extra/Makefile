APP_NAME ?= msvenom-extra
ZIP_NAME := $(APP_NAME).zip
EXPORTED := ../../exported/$(APP_NAME)
SOURCE_ZIP := Source.zip

all: prepare unzip install rename

prepare:
	@echo "🔧 Iniciando instalación de $(APP_NAME)..."

unzip:
	@echo "📦 Descomprimiendo $(SOURCE_ZIP)..."
	@powershell -Command "Expand-Archive -Force $(SOURCE_ZIP) extracted"

install:
	@echo "📥 Instalando dependencias..."
	@pip install -r extracted/requirements.txt

rename:
	@echo "🔄 Renombrando main.py a $(APP_NAME)..."
	@cmd /c move /Y main.py $(APP_NAME).py
	@echo "✅ Instalación completada: ejecuta './$(APP_NAME)' para iniciar"

#  -- build --

build:
	@echo "🧱 Compilando $(APP_NAME).py a ejecutable..."
	@python -m nuitka --standalone --onefile --windows-disable-console ^
		--output-dir=$(EXPORTED) ^
		--output-filename=$(APP_NAME).exe $(APP_NAME).py

package: build
	@echo "📦 Comprimendo en '$(ZIP_NAME)'..."
	@cd $(EXPORTED) && powershell -Command "Compress-Archive -Path * -DestinationPath ../$(ZIP_NAME) -Force"
	@echo "✅ Exportado en exported/$(ZIP_NAME)"