import os

# Obtener la variable PATH del sistema
system_path = os.environ.get('PATH')

for i in system_path.split(';'):
    print(i)





# import subprocess
# import os


# ENV_NAME = ".venv"
# ENV_PATH = os.path.abspath(os.path.dirname(__file__))

# # Ruta actual del PATH
# current_path = os.environ.get('PATH', '')

# # Construir la nueva ruta del PATH
# new_path = f'{current_path};{ENV_PATH}'

# # Ejecutar el comando setx para agregar la nueva ruta al PATH del sistema
# subprocess.check_call([r'C:\Windows\System32\setx.exe', 'PATH', new_path], shell=True)


exit()

# Crear entorno virtual
subprocess.check_call(["virtualenv", env_name])

# Activar entorno virtual
activate_script = "{}\\Scripts\\activate.bat".format(env_name)
subprocess.check_call(activate_script, shell=True)

# Instalar los módulos requeridos
subprocess.check_call(["pip", "install", "modulo1", "modulo2", ...])

# Desactivar el entorno virtual
subprocess.check_call("deactivate", shell=True)



# C:\Users\leonel\.cargo\bin;
# C:\Program Files\Git\cmd;
# C:\Users\leonel\AppData\Local\Programs\Python\Python312\Scripts\;
# C:\Users\leonel\AppData\Local\Programs\Python\Python312\;
# C:\Users\leonel\AppData\Local\Programs\Python\Launcher\;
# C:\Program Files\MySQL\MySQL Shell 8.0\bin\;
# C:\Users\leonel\.console-ninja\.bin;
# C:\Users\leonel\AppData\Local\Microsoft\WindowsApps;
# C:\Users\leonel\AppData\Local\Programs\Microsoft VS Code\bin;
# C:\Users\leonel\AppData\Local\Programs\oh-my-posh\bin;
# L:\files\programs\sqlite3;
# \\wsl.localhost\Ubuntu\home\leo\.cargo\bin;
# C:\Users\leonel\AppData\Roaming\fnm\aliases\default;
# L:\endev\scripts\bin;C:\Program Files (x86)\cloudflared.exe;
# C:\Program Files\PostgreSQL\16\bin;

