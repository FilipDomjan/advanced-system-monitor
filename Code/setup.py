from cx_Freeze import setup, Executable
import sys

base = None

# if (sys.platform == "win32"):
#base = "Win32GUI"

executables = [Executable("advanced-system-monitor.py",
                          base=base, icon="Visual\images\ASM_Logo_ICO.ico", target_name="Advanced System Monitor")]

includefiles = ["Visual\images\ASM_Logo_ICO.ico"]

packages = ["idna"]
options = {
    'build_exe': {
        'packages': packages,
        'include_files': includefiles
    },
}

setup(
    name="Advanced System Monitor",
    options=options,
    version="1.0.0",
    description='Collects vast amount of hardware information.',
    executables=executables
)
