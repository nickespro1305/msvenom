from rich import print
import subprocess
import argparse
import os
import sys


def setup():
    print("[bold green]Welcome to the project setup tool[/bold green]")
    print("In what directory do you want to start a project? (use `.` for the current directory)")
    project_path = input("[+] ")

    print("And what will be the plugin name?")
    project_name = input("[+] ")

    print("Creating your project, please wait...")
    try:
        # Calculamos ruta absoluta del directorio destino
        target_dir = os.path.abspath(os.path.join(project_path, project_name))
        os.makedirs(target_dir, exist_ok=True)

        # Obtenemos la ruta absoluta del script que se está ejecutando
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Ruta absoluta a la carpeta example dentro del plugin (relativa al script)
        plugin_example_dir = os.path.join(script_dir, "example")

        if not os.path.isdir(plugin_example_dir):
            print(f"[red]❌ No se encontró la carpeta 'example' en {plugin_example_dir}[/red]")
            return

        # Copiar archivos Makefile y properties.json desde example al proyecto nuevo
        for filename in ["Makefile", "properties.json"]:
            src = os.path.join(plugin_example_dir, filename)
            dst = os.path.join(target_dir, filename)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
                print(f"[green]✅ Copiado {filename} a {target_dir}[/green]")
            else:
                print(f"[yellow]⚠️ No se encontró {filename} en {plugin_example_dir}[/yellow]")

        print(f"[green]✅ Project '{project_name}' created successfully in '{target_dir}'[/green]")
    except Exception as e:
        print(f"[red]❌ Error creating project:[/red] {e}")

def main():
    parser = argparse.ArgumentParser(description="msvenom developer toolset for plugins")
    parser.add_argument("mode", choices=["setup"], help="Mode to run: 'setup' for project creation")

    args = parser.parse_args()

    if args.mode == "setup":
        setup()

if __name__ == "__main__":
    main()
