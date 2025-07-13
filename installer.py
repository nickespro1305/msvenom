import subprocess
import os

def archinstall():
    subprocess.run("sudo pacman -Syu --noconfirm", shell=True, check=True)
    subprocess.run("sudo pacman -S python3 python-pip make patchelf --noconfirm", shell=True, check=True)

    os.mkdir("msvenom")
    os.chdir("msvenom")
    
    os.mkdir("apps")
    os.mkdir("keys")
    os.mkdir("lib")

    subprocess.run("curl -o main.py https://raw.githubusercontent.com/nickespro1305/msvenom/refs/heads/main/ports/main-arch.py", shell=True, check=True)

    subprocess.run("curl -o run.sh https://raw.githubusercontent.com/nickespro1305/msvenom/refs/heads/main/ports/run-arch.sh", shell=True, check=True)

    subprocess.run("chmod +x main.py", shell=True, check=True)
    subprocess.run("chmod +x run.sh", shell=True, check=True)

    os.chdir("keys")
    subprocess.run("curl -o sources.json https://raw.githubusercontent.com/nickespro1305/msvenom/refs/heads/main/SERVER/default_sources.json", shell=True, check=True)
    os.chdir("..")

    subprocess.run("python3 -m venv venv && source venv/bin/activate && pip install rich requests nuitka", shell=True, check=True)

    print("instalacion completada")
    return


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

    subprocess.run("pip install rich requests pywin32 nuitka", shell=True, check=True)

    print("instalacion completada")
    return

print("indique la version que esta buscando de msvenom")
print("msvenom-arch, msvenom-windows")
version = input("[+]")

print(f"estas seguro de proceder con la instalacion? msvenom creará una carpeta y se instalara en este directorio")
confirmation = input("[Y/n]")

if confirmation == "Y":
    if version == "msvenom-arch":
        archinstall()
    if version == "msvenom-windows":
        install()
else: 
    print("instalacion cancelada correctamente")