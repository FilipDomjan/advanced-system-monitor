from cx_Freeze import setup, Executable

base = None

executables = [Executable("advanced-system-monitor.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="Advanced System Monitor",
    options=options,
    version="1.0.0",
    description='Collects vast amount of hardware information.',
    executables=executables
)
