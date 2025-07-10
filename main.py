import json
import requests
import subprocess
import os
from rich import print
from rich.table import Table
from rich.progress import Progress
from rich.console import Console

KEY_FILE = "keys/sources.json"
console = Console()

def load_key():
    if not os.path.exists(KEY_FILE):
        console.print(f"[red]No se encontró {KEY_FILE}[/red]")
        return None
    with open(KEY_FILE, "r") as f:
        try:
            data = json.load(f)
            return data.get("url")
        except json.JSONDecodeError:
            console.print(f"[red]Error al leer {KEY_FILE}[/red]")
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
    table = Table(title="📦 Tienda de Scripts", header_style="bold magenta")

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

def install_program(program_url):
    try:
        r = requests.get(program_url)
        data = r.json()
        name = data.get("name", "Programa sin nombre")
        install_commands = data.get("install", [])

        console.print(f"\n[bold green]Instalando {name}...[/bold green]\n")

        with Progress() as progress:
            task = progress.add_task(f"[cyan]Ejecutando comandos", total=len(install_commands))

            for cmd in install_commands:
                progress.console.print(f"[blue]>[/blue] {cmd}")
                subprocess.run(cmd, shell=True, check=True)
                progress.advance(task)

        console.print(f"\n[bold green]✅ Instalación completada[/bold green]")

    except Exception as e:
        console.print(f"[red]Error al instalar:[/red] {e}")

def main():
    base_url = load_key()
    if not base_url:
        return

    programs = get_programs(base_url)
    if not programs:
        return

    show_programs(programs)

    program_ids = list(programs.keys())
    selected = console.input("\n[bold yellow]Introduce el número del programa que quieres instalar[/bold yellow]: ").strip()

    if selected.isdigit() and 0 < int(selected) <= len(program_ids):
        selected_id = program_ids[int(selected) - 1]
        install_program(programs[selected_id])
    else:
        console.print("[red]Selección inválida[/red]")

if __name__ == "__main__":
    main()
