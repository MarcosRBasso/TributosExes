from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("menu_windows.py", base=base)]

packages = ["configparser", "requests"]
options = {
    'build_exe': {

        'packages': packages,
    },

}

setup(
    name = "Tributos",
    options = options,
    version = "1.0",
    description = 'Sistema de envio de dados para o sistema Tributos Cloud',
    executables = executables
)