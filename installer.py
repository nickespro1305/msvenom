import subprocess
import os

def install():
    os.mkdir("msvenom")
    os.chdir("msvenom")
    
    os.mkdir("apps")
    os.mkdir("keys")

    subprocess.run("curl -O https://raw.githubusercontent.com/nickespro1305/msvenom/refs/heads/main/main.py", shell=True, check=True)

    os.chdir("keys")
    subprocess.run("curl -O sources.json https://raw.githubusercontent.com/nickespro1305/msvenom/refs/heads/main/SERVER/default_sources.json", shell=True, check=True)
    os.chdir("..")

    subprocess.run("pip install rich requests", shell=True, check=True)

    print("instalacion completada")
    return

print(f"estas seguro de proceder con la instalacion? msvenom creará una carpeta y se instalara en este directorio")
confirmation = input("[Y/n]")

if confirmation == "Y":
    install()
else: 
    print("instalacion cancelada correctamente")