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
        os.chdir(project_path)
        os.mkdir(project_name)
        os.chdir(project_name)

        # Aquí podrías copiar los archivos base:
        # subprocess.run("cp /ruta/origen/Makefile .", shell=True)
        # subprocess.run("cp /ruta/origen/properties.json .", shell=True)

        print(f"[green]✅ Project '{project_name}' created successfully in '{os.getcwd()}'[/green]")
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
