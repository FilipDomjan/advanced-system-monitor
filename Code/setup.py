from cx_Freeze import setup, Executable
import sys
from tkinter import font

base = None

executables = [Executable("advanced-system-monitor.py",
                          base=base, icon="Visual\images\ASM_Logo_ICO.ico", target_name="Advanced System Monitor")]

includefiles = ["Visual\images\ASM_Logo_ICO.ico"]

packages = ["idna", "tkinter", "tkinter.font"]

include = ["tkinter", "tkinter.font"]

options = {
    'build_exe': {
        'packages': packages,
        'include_files': includefiles,
        'includes': include
    },
}

setup(
    name="Advanced System Monitor",
    options=options,
    version="1.0.0",
    description='Collects vast amount of hardware information.',
    executables=executables
)
