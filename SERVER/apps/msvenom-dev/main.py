from rich import print
import subprocess
import argparse
import os

parser = argparse.ArgumentParser(description="msvenom developer toolset for plugins")
    parser.add_argument("setup", action="store_true", help="setup a new msvenom plugin project")

def setup():
    print("welcome to the project setup tool, in what directory you want to start a project? (use . for create a project in the current directory)")
    project_path = input("[+]")

    print("and what will be the plugin name?")
    project_name = input("[+]")

    print("creating your project, please wait...")
    os.chdir(project_path)
    os.mkdir(project_name)

    os.chdir(project_name)

    # copia del directorio donde esta instalado el plugin hacia el projecto los archivos de ejemplo de properties.json y de Makefile
    # subprocess.run("", shell=True, check=True)
