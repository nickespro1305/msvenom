import subprocess
import os

def install():
    os.mkdir("msvenom")
    os.chdir("msvenom")
    
    os.mkdir("apps")
    os.mkdir("keys")
    os.mkdir("lib")

    subprocess.run("curl -O https://raw.githubusercontent.com/nickespro1305/msvenom/refs/heads/main/main.py", shell=True, check=True)

    os.chdir("keys")
    subprocess.run("curl -o sources.json https://raw.githubusercontent.com/nickespro1305/msvenom/refs/heads/main/SERVER/default_sources.json", shell=True, check=True)
    os.chdir("..")

    os.chdir("lib")
    os.mkdir("make")
    os.chdir("make")
    subprocess.run("curl -o make.zip https://raw.githubusercontent.com/nickespro1305/msvenom/refs/heads/main/SERVER/DEPENDENCES/make-3.81-bin.zip", shell=True, check=True)
    subprocess.run("curl -o makeD.zip https://raw.githubusercontent.com/nickespro1305/msvenom/refs/heads/main/SERVER/DEPENDENCES/make-3.81-dep.zip", shell=True, check=True)
    subprocess.run("tar -xf make.zip")
    subprocess.run("tar -xf makeD.zip")
    os.chdir("..")
    os.chdir("..")

    subprocess.run("pip install rich requests pywin32", shell=True, check=True)

    print("instalacion completada")
    return

print(f"estas seguro de proceder con la instalacion? msvenom creará una carpeta y se instalara en este directorio")
confirmation = input("[Y/n]")

if confirmation == "Y":
    install()
else: 
    print("instalacion cancelada correctamente")