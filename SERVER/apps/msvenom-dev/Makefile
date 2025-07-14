APP_NAME ?= msvenom-dev
ZIP_NAME := $(APP_NAME).zip
EXPORTED := ../../exported/$(APP_NAME)
SOURCE_ZIP := Source.zip

all: prepare unzip install rename

prepare:
	@echo "🔧 Iniciando instalación de $(APP_NAME)..."

unzip:
	@echo "📦 Descomprimiendo $(SOURCE_ZIP)..."
	@unzip $(SOURCE_ZIP) -d .

install:
	@echo "📥 Instalando dependencias..."
	@pip install -r requirements.txt

rename:
	@echo "🔄 Renombrando main.py a $(APP_NAME)..."
	@mv main.py $(APP_NAME).py
	@echo "✅ Instalación completada: ejecuta './$(APP_NAME)' para iniciar"

#  -- build --

build:
	@echo "🧱 Compilando $(APP_NAME).py a ejecutable..."
	@python3 -m nuitka --standalone --onefile \
		--output-dir=$(EXPORTED) \
		--output-filename=$(APP_NAME).bin $(APP_NAME).py

package: build
	@echo "📦 Comprimiendo en '$(ZIP_NAME)'..."
	@cd ../../exported && zip -r $(ZIP_NAME) $(APP_NAME)
	@echo "✅ Exportado: exported/$(ZIP_NAME)"