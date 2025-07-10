import json
import requests
import subprocess
import os
import argparse
import zipfile
from rich import print
from rich.table import Table
from rich.progress import Progress
from rich.console import Console

KEY_FILE = "keys/main.json"
SOURCES_FILE = "keys/sources.json"
console = Console()

def show_program_info(data):
    table = Table(title="📄 Información del programa", header_style="bold green")
    table.add_column("Campo", style="cyan", justify="right")
    table.add_column("Valor", style="white")

    table.add_row("Nombre", data.get("name", "Desconocido"))
    table.add_row("Descripción", data.get("description", "Sin descripción"))
    table.add_row("Makefile URL", data.get("makefile_url", "No especificado"))
    table.add_row("ZIP URL", data.get("zip_url", "No especificado"))

    console.print(table)

def load_sources():
    if not os.path.exists(SOURCES_FILE):
        console.print(f"[red]No se encontró {SOURCES_FILE}[/red]")
        return []
    try:
        with open(SOURCES_FILE, "r") as f:
            data = json.load(f)
            return data.get("sources", [])
    except Exception as e:
        console.print(f"[red]Error al leer {SOURCES_FILE}:[/red] {e}")
        return []

def save_key(url):
    try:
        data = {"url": url}
        with open(KEY_FILE, "w") as f:
            json.dump(data, f, indent=4)
        console.print(f"[green]✅ key.json actualizado correctamente[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error guardando key.json:[/red] {e}")
        return False

def load_key():
    if not os.path.exists(KEY_FILE):
        console.print("[red]No se encontró key.json[/red]")
        return None
    with open(KEY_FILE, "r") as f:
        try:
            data = json.load(f)
            return data.get("url")
        except json.JSONDecodeError:
            console.print("[red]Error al leer key.json[/red]")
            return None

def get_programs(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        console.print(f"[red]Error al descargar index.json:[/red] {e}")
        return {}

def show_programs(programs):
    table = Table(title="📦 Scripts disponibles", header_style="bold magenta")
    table.add_column("#", justify="right")
    table.add_column("ID", style="cyan")
    table.add_column("Nombre", style="green")
    table.add_column("Descripción", style="white")

    for i, (key, value) in enumerate(programs.items(), 1):
        try:
            r = requests.get(value)
            data = r.json()
            table.add_row(str(i), key, data.get("name", "Sin nombre"), data.get("description", "Sin descripción"))
        except:
            table.add_row(str(i), key, "[red]Error[/red]", "[red]No se pudo cargar properties.json[/red]")

    console.print(table)

def install_program_by_name(name, programs):
    if name not in programs:
        console.print(f"[red]❌ No se encontró el programa '{name}'[/red]")
        return

    program_url = programs[name]
    if not program_url.startswith("http"):
        console.print(f"[red]❌ URL inválida:[/red] '{program_url}'")
        return

    try:
        # Descargar properties.json
        r = requests.get(program_url)
        r.raise_for_status()
        data = r.json()

        show_program_info(data)

        app_name = data.get("name", name)
        makefile_url = data.get("makefile_url")
        zip_url = data.get("zip_url")

        if not makefile_url or not zip_url:
            console.print(f"[red]❌ Faltan campos en properties.json[/red]")
            return

        # Crear directorio apps/<app_name>
        app_dir = os.path.join("apps", app_name)
        os.makedirs(app_dir, exist_ok=True)

        # Descargar Makefile
        makefile_path = os.path.join(app_dir, "Makefile")
        with requests.get(makefile_url, stream=True) as r:
            r.raise_for_status()
            with open(makefile_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        # Descargar .zip
        zip_path = os.path.join(app_dir, "archive.zip")
        with requests.get(zip_url, stream=True) as r:
            r.raise_for_status()
            with open(zip_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        # Extraer .zip
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(app_dir)

        # Ejecutar Makefile usando el binario de make en lib/
        console.print(f"[cyan]🔧 Ejecutando Makefile para {app_name}...[/cyan]")
        make_binary = os.path.abspath("lib/make/bin/make")
        subprocess.run([make_binary, "-C", app_dir], check=True)

        console.print(f"\n[bold green]✅ {app_name} instalado correctamente[/bold green]")

    except Exception as e:
        console.print(f"[red]Error durante la instalación:[/red] {e}")
def main():
    parser = argparse.ArgumentParser(description="Tienda de scripts en Python")
    parser.add_argument("--update", action="store_true", help="Actualizar key.json desde sources.json")
    parser.add_argument("--install", type=str, help="Instalar un paquete por nombre")

    args = parser.parse_args()

    if args.update:
        sources = load_sources()
        if not sources:
            return

        main_url = sources[0]
        if save_key(main_url):
            programs = get_programs(main_url)
            if programs:
                show_programs(programs)
        return

    if args.install:
        base_url = load_key()
        if not base_url:
            return
        programs = get_programs(base_url)
        if not programs:
            return
        install_program_by_name(args.install, programs)
        return

    # Si no se pasa ningún argumento
    parser.print_help()

if __name__ == "__main__":
    main()
