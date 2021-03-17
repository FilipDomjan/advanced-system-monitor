from json import load
from string import digits
import sys
import tkinter as tk
from tkinter import PhotoImage, Toplevel
import time
from tkinter.constants import E, SUNKEN
from cpuinfo.cpuinfo import main
import psutil
import platform
import datetime
from datetime import date
from datetime import datetime
import GPUtil
from win32com.client.gencache import usage
import wmi
import speedtest
from time import sleep, time_ns
import cpuinfo
import multiprocessing
import os
import subprocess
from tkinter import filedialog, Text
import ctypes
import locale
from win32api import GetSystemMetrics
import win32api
import os.path
from os import path, times
from InfoBox import CreateToolTip
import random
from tqdm import tqdm


# Basic function for size conversion

try:
    def get_size(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()


# Pop-Up message box

try:
    def MessageBox(title, text, style):
        ctypes.windll.user32.MessageBoxW(0, text, title, style)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("MessageBox error: {}".format(e))
    f.close()

# Home page which holds various settings and options

try:
    def home():
        global ref
        global home_frame
        # Remove other active windows and change button background

        try:
            homeButton.configure(bg=button_bg)
        except Exception as e:
            print(e)

        try:
            combined_test_frame.place_forget()
            root.after_cancel(rct)
        except Exception as e:
            print(e)

        try:
            root.after_cancel(ref)
            cpu_frame.place_forget()
            cpuButton.configure(bg=sidemenu_bg)
        except Exception as e:
            print(e)

        try:
            root.after_cancel(gpu_update)
            gpu_frame.place_forget()
            gpuButton.configure(bg=sidemenu_bg)
        except Exception as e:
            print(e)

        try:
            main_frame.place_forget()
            motherboardButton.configure(bg=sidemenu_bg)
        except Exception as e:
            print(e)

        try:
            root.after_cancel(ram_ref)
            ram_frame.place_forget()
            ramButton.configure(bg=sidemenu_bg)
        except Exception as e:
            print(e)

        try:
            root.after_cancel(drive_ref)
            drive_frame.place_forget()
            hddButton.configure(bg=sidemenu_bg)
        except Exception as e:
            print(e)

        try:
            root.after_cancel(net_ref)
            network_frame.place_forget()
            netButton.configure(bg=sidemenu_bg)
        except Exception as e:
            print(e)

        try:
            root.after_cancel(fan_ref)
            fans_frame.place_forget()
            fanButton.configure(bg=sidemenu_bg)
        except Exception as e:
            print(e)

        # Setup main frame

        home_frame = tk.Frame(root, bg=canvas_bg)
        home_frame.place(relwidth=0.872, relheight=0.96,
                         relx=0.117, rely=0.021)

        loading = tk.Label(home_frame, bg=canvas_bg, fg=fg, font=(
            loading_font), width=100, height=50, text="Loading...")
        loading.pack()

        def declare_home():
            global s
            global h
            global m
            global h_accurate_time
            global m_accurate_time
            global s_accurate_time
            global denim_photo
            global bluegreen_photo
            global bluepink_photo
            global metallic_photo
            global redblack_photo
            global orangepink_photo
            global blackwhite_photo
            global info_symbol_photo
            global refresh_rate_entry
            global on_button
            global off_button
            global record_cpu_button
            global record_gpu_button
            global record_ram_button
            global record_fan_button
            global mobo_info_button
            global max_cpu_usg
            global cpu_max_usage_during_test
            global gpu_max_usage_during_test
            global max_gpu_usg
            global gpu_max_temp_during_test
            global ram_max_usage_during_test
            global swap_max_usage_during_test
            global fun_fact
            global rand_num_list
            global cpu_max_power_during_test
            global cpu_max_temp_during_test
            global cpu_max_core_usage_during_test
            global cpu_max_clock_during_test
            root.after_cancel(dec_home)
            with tqdm(total=100) as bar:

                system_monitor = tk.Frame(home_frame, bg=bg)
                system_monitor.place(
                    relwidth=1, relheight=0.08, relx=0, rely=0)

                system_monitor_label = tk.Label(system_monitor, bg=bg, fg=fg, font=font,
                                                anchor=tk.CENTER, width=100, height=100, text="ADVANCED SYSTEM MONITOR")
                system_monitor_label.pack()

                # Themes frame

                themes = tk.Frame(home_frame, bg=bg)
                themes.place(relwidth=0.40, relheight=0.58, relx=0, rely=0.1)

                themes_text_frame = tk.Frame(themes, bg=bg)
                themes_text_frame.place(
                    relwidth=0.3, relheight=0.05, relx=0.01, rely=0.03)

                themes_label = tk.Label(themes_text_frame, bg=bg, fg=fg, font=font,
                                        width=10, height=1, anchor=tk.W, text="THEMES")
                themes_label.pack()

                themes_container = tk.Frame(themes, bg=bg)
                themes_container.place(
                    relwidth=1, relheight=0.85, relx=0, rely=0.1)

                # Theme profiles

                metallic_photo = PhotoImage(
                    file=f"{themes_image_path}\pmetallic.png")

                metallic = tk.Button(themes_container, bg=bg, fg="white", image=metallic_photo, bd=0,
                                     width=70, height=70, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=metallic_theme)
                metallic.grid(row=0, column=0, padx=27, pady=(15, 5))

                denim_photo = PhotoImage(
                    file=f"{themes_image_path}\pdenim.png")

                denim_theme = tk.Button(
                    themes_container, bg=bg, fg="white", bd=0, image=denim_photo, width=70, height=70, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=denim)
                denim_theme.grid(row=0, column=1, padx=(0, 27), pady=(15, 5))

                redblack_photo = PhotoImage(
                    file=f"{themes_image_path}\predblack.png")

                redblack = tk.Button(
                    themes_container, bg=bg, fg="white", image=redblack_photo, bd=0, width=70, height=70, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=redblack_theme)
                redblack.grid(row=0, column=2, padx=(0, 27), pady=(15, 5))

                blackwhite_photo = PhotoImage(
                    file=f"{themes_image_path}\pblackwhite.png")

                blackwhite = tk.Button(themes_container, bg=bg, fg="white", image=blackwhite_photo, bd=0,
                                       width=70, height=70, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=blackwhite_theme)
                blackwhite.grid(row=0, column=3, padx=(0, 27), pady=(15, 5))

                with open("Code\Config\config.txt", "r") as config:
                    for line in config:
                        if "theme_selected" in line:
                            split = line.split()

                            if split[2] == "metallic":
                                metallic.configure(
                                    borderwidth=2, relief="solid")
                            elif split[2] == "denim":
                                denim_theme.configure(
                                    borderwidth=2, relief="solid")
                            elif split[2] == "redblack":
                                redblack.configure(
                                    borderwidth=2, relief="solid")
                            elif split[2] == "blackwhite":
                                blackwhite.configure(
                                    borderwidth=2, relief="solid")

                bar.update(10)

                # Clock frame

                time_frame = tk.Frame(home_frame, bg=bg)
                time_frame.place(
                    relwidth=0.40, relheight=0.30, relx=0, rely=0.7)

                lines = tk.Frame(time_frame, bg=bg)
                lines.place(relwidth=1, relheight=1, relx=0.05, rely=-0.05)

                hours = tk.Frame(lines, bg=bg)
                hours.place(relwidth=1, relheight=0.3, relx=0, rely=0.13)

                hours_label = tk.Label(hours, bg=bg, fg=asm_yellow, font=time_font,
                                       anchor=tk.W, width=100, height=0, text="Hours")
                hours_label.pack()

                h = tk.Label(hours, bg=bg, fg=asm_yellow, font=font,
                             anchor=tk.W, width=100, height=0, text="")
                h.pack()

                h_accurate = tk.Frame(lines, bg=bg)
                h_accurate.place(relwidth=0.1, relheight=0.1,
                                 relx=0.8, rely=0.13)

                h_accurate_time = tk.Label(h_accurate, bg=bg, fg=asm_yellow, font=time_font,
                                           anchor=tk.CENTER, width=5, height=5, text="H")
                h_accurate_time.pack()

                minutes = tk.Frame(lines, bg=bg)
                minutes.place(relwidth=1, relheight=0.4, relx=0, rely=0.42)

                minutes_label = tk.Label(minutes, bg=bg, fg="#10b1eb", font=time_font,
                                         anchor=tk.W, width=100, height=0, text="Minutes")
                minutes_label.pack()

                m_accurate = tk.Frame(lines, bg=bg)
                m_accurate.place(relwidth=0.1, relheight=0.1,
                                 relx=0.8, rely=0.42)

                m_accurate_time = tk.Label(m_accurate, bg=bg, fg="#10b1eb", font=time_font,
                                           anchor=tk.CENTER, width=5, height=5, text="M")
                m_accurate_time.pack()

                m = tk.Label(minutes, bg=bg, fg="#10b1eb", font=font,
                             anchor=tk.W, width=100, height=0, text="")
                m.pack()

                seconds = tk.Frame(lines, bg=bg)
                seconds.place(relwidth=1, relheight=0.3, relx=0, rely=0.72)

                s_accurate = tk.Frame(lines, bg=bg)
                s_accurate.place(relwidth=0.1, relheight=0.1,
                                 relx=0.8, rely=0.72)

                s_accurate_time = tk.Label(s_accurate, bg=bg, fg=asm_red, font=time_font,
                                           anchor=tk.CENTER, width=5, height=5, text="S")
                s_accurate_time.pack()

                seconds_label = tk.Label(seconds, bg=bg, fg=asm_red, font=time_font,
                                         anchor=tk.W, width=100, height=0, text="Seconds")
                seconds_label.pack()

                s = tk.Label(seconds, bg=bg, fg=asm_red, font=font,
                             anchor=tk.W, width=100, height=0, text="")
                s.pack()

                bar.update(10)

                # Combined test frame holds settings for a combined test which will exchange current "home" profile with different system monitors (cpu usage, gpu usage etc.)
                # Its purpose is to show important information in one place so one doesn't have to travel between tabs constantly

                combined_test = tk.Frame(home_frame, bg=bg)
                combined_test.place(relwidth=0.59, relheight=0.58,
                                    relx=0.415, rely=0.1)

                refresh_rate = []

                with open(
                        "Code\Config\switches.txt", "r") as file:
                    for line in file:
                        for word in line.split():
                            refresh_rate.append(word)

                combined_test_text_frame = tk.Frame(combined_test, bg=bg)
                combined_test_text_frame.place(
                    relwidth=0.5, relheight=0.15, relx=0.015, rely=0.018)

                combined_test_text = tk.Label(combined_test_text_frame, bg=bg, fg=fg,
                                              font=font, anchor=tk.W, width=14, height=1, text="COMBINED TEST")
                combined_test_text.grid(row=0, column=0, padx=0, pady=0)

                info_symbol_photo = PhotoImage(
                    file=f"{image_path}\info_19px_white.png")

                info_symbol = tk.Label(combined_test_text_frame, bg=bg,
                                       fg=fg, width=19, height=19, image=info_symbol_photo)
                info_symbol.grid(row=0, column=1, padx=10, pady=(2, 0))

                CreateToolTip(info_symbol, text="What is combined test?\nIts a tool that shows you only the most important data\nthat you need when benchmarking.\n\nWhat do the switches do?\nSwitches represent what is written into a text file\nduring the test, you can use all of them,\nbut beware, more information means higher performance impact,\nmeaning that the ASM will run slower. We recommend\nkeeping everything on except Mobo Data during the test,\nas it is the most demanding one.\n\nWhere is the text file?\nText file will be created on your desktop and\nwill contain only the data you choose to write\nin the combined test settings.\n\nWhat is 'WRITE ONLY' button?\nOnce clicked it will only do one run of performance check\nand write it into a file.\n\nWhat is the 'FULL TEST' button?\nOnce clicked the home layout will be replaced with\na new layout containing the combined test information.\nYou can return to home at any time by pressing the home\nbutton given in the bottom-right corner of the combined\ntest or by pressing the home button in the sidemenu.\n\nWhat is Refresh Rate field?\nThere you can choose how fast does the app refresh.\nYou can choose from 500 to 10000ms.\nNote: 1000ms = 1s", backg=bg, foreg=fg)

                settings_container = tk.Frame(combined_test, bg=bg)
                settings_container.place(
                    relwidth=1, relheight=0.70, relx=0, rely=0.15)

                # Adjust refresh rate (how fast it refresh statistics)

                refresh_rate = tk.Label(settings_container, bg=bg, fg=fg, font=font,
                                        anchor=tk.W, width=15, height=1, text="Refresh Rate")
                refresh_rate.grid(row=0, column=0, padx=(10, 0), pady=(0, 20))

                with open("Code\Config\switches.txt", "r") as file:
                    for line in file:
                        if "refresh_rate" in line:
                            split = line.split()

                refresh_rate_entry = tk.Entry(
                    settings_container, bg=canvas_bg, fg=fg, bd=0, width=10, textvariable=1, font=font, justify='center')
                refresh_rate_entry.delete(0, 'end')
                refresh_rate_entry.insert(0, f'{split[2]}')
                refresh_rate_entry.bind("<Return>", write_to_file)
                refresh_rate_entry.grid(
                    row=0, column=1, padx=(298, 0), pady=(0, 20))

                # Choose what you want to record and put into a text file during a test | note: more options > bigger the performance impact #
                with open("Code\Config\switches.txt", "r") as file:
                    for line in file:
                        if "record_cpu" in line:
                            rec_cpu = line.split()
                        if "record_gpu" in line:
                            rec_gpu = line.split()
                        if "record_ram" in line:
                            rec_ram = line.split()
                        if "record_fans" in line:
                            rec_fan = line.split()
                        if "mobo_info" in line:
                            base_inf = line.split()

                on_button = PhotoImage(
                    file=f"{image_path}\switch-on_small.png")
                off_button = PhotoImage(
                    file=f"{image_path}\switch-off_small.png")

                # BASE INFO

                if base_inf[2] == "True":
                    mobo_info_label = tk.Label(
                        settings_container, bg=bg, fg=fg, font=font, width=15, height=1, anchor=tk.W, text="Report Mobo Data")
                    mobo_info_label.grid(
                        row=1, column=0, padx=(10, 0), pady=(0, 20))
                    mobo_info_button = tk.Button(
                        settings_container, width=50, height=23, bg=bg, fg=fg, bd=0, activebackground=bg, image=on_button, relief=SUNKEN, command=mobo_info_status)
                    mobo_info_button.grid(
                        row=1, column=1, padx=(298, 0), pady=(0, 20))
                else:
                    mobo_info_label = tk.Label(
                        settings_container, bg=bg, fg=fg, font=font, width=15, height=1, anchor=tk.W, text="Report Mobo Data")
                    mobo_info_label.grid(
                        row=1, column=0, padx=(10, 0), pady=(0, 20))
                    mobo_info_button = tk.Button(
                        settings_container, width=50, height=23, bg=bg, fg=fg, bd=0, activebackground=bg, image=off_button, relief=SUNKEN, command=mobo_info_status)
                    mobo_info_button.grid(
                        row=1, column=1, padx=(298, 0), pady=(0, 20))

                # CPU RECORDING
                if rec_cpu[2] == "True":
                    record_cpu_label = tk.Label(
                        settings_container, bg=bg, fg=fg, font=font, width=15, height=1, anchor=tk.W, text="Report CPU Data")
                    record_cpu_label.grid(
                        row=2, column=0, padx=(10, 0), pady=(0, 20))
                    record_cpu_button = tk.Button(
                        settings_container, width=50, height=23, bg=bg, fg=fg, bd=0, activebackground=bg, image=on_button, relief=SUNKEN, command=cpu_button_state)
                    record_cpu_button.grid(
                        row=2, column=1, padx=(298, 0), pady=(0, 20))
                else:
                    record_cpu_label = tk.Label(
                        settings_container, bg=bg, fg=fg, font=font, width=15, height=1, anchor=tk.W, text="Report CPU Data")
                    record_cpu_label.grid(
                        row=2, column=0, padx=(10, 0), pady=(0, 20))
                    record_cpu_button = tk.Button(
                        settings_container, width=50, height=23, bg=bg, fg=fg, bd=0, activebackground=bg, image=off_button, relief=SUNKEN, command=cpu_button_state)
                    record_cpu_button.grid(
                        row=2, column=1, padx=(298, 0), pady=(0, 20))

                # GPU RECORDING
                if rec_gpu[2] == "True":
                    record_gpu_label = tk.Label(
                        settings_container, bg=bg, fg=fg, font=font, width=15, height=1, anchor=tk.W, text="Report GPU Data")
                    record_gpu_label.grid(
                        row=3, column=0, padx=(10, 0), pady=(0, 20))
                    record_gpu_button = tk.Button(
                        settings_container, width=50, height=23, bg=bg, fg=fg, bd=0, activebackground=bg, image=on_button, relief=SUNKEN, command=gpu_button_state)
                    record_gpu_button.grid(
                        row=3, column=1, padx=(298, 0), pady=(0, 20))
                else:
                    record_gpu_label = tk.Label(
                        settings_container, bg=bg, fg=fg, font=font, width=15, height=1, anchor=tk.W, text="Report GPU Data")
                    record_gpu_label.grid(
                        row=3, column=0, padx=(10, 0), pady=(0, 20))
                    record_gpu_button = tk.Button(
                        settings_container, width=50, height=23, bg=bg, fg=fg, bd=0, activebackground=bg, image=off_button, relief=SUNKEN, command=gpu_button_state)
                    record_gpu_button.grid(
                        row=3, column=1, padx=(298, 0), pady=(0, 20))

                # RAM RECORDING
                if rec_ram[2] == "True":
                    record_ram_label = tk.Label(
                        settings_container, bg=bg, fg=fg, font=font, width=15, height=1, anchor=tk.W, text="Report RAM Data")
                    record_ram_label.grid(
                        row=4, column=0, padx=(10, 0), pady=(0, 20))
                    record_ram_button = tk.Button(
                        settings_container, width=50, height=23, bg=bg, fg=fg, bd=0, activebackground=bg, image=on_button, relief=SUNKEN, command=ram_button_state)
                    record_ram_button.grid(
                        row=4, column=1, padx=(298, 0), pady=(0, 20))
                else:
                    record_ram_label = tk.Label(
                        settings_container, bg=bg, fg=fg, font=font, width=15, height=1, anchor=tk.W, text="Report RAM Data")
                    record_ram_label.grid(
                        row=4, column=0, padx=(10, 0), pady=(0, 20))
                    record_ram_button = tk.Button(
                        settings_container, width=50, height=23, bg=bg, fg=fg, bd=0, activebackground=bg, image=off_button, relief=SUNKEN, command=ram_button_state)
                    record_ram_button.grid(
                        row=4, column=1, padx=(298, 0), pady=(0, 20))

                # FAN RECORDING
                if rec_fan[2] == "True":
                    record_fan_label = tk.Label(
                        settings_container, bg=bg, fg=fg, font=font, width=15, height=1, anchor=tk.W, text="Report Fans Data")
                    record_fan_label.grid(
                        row=5, column=0, padx=(10, 0), pady=(0, 20))
                    record_fan_button = tk.Button(
                        settings_container, width=50, height=23, bg=bg, fg=fg, bd=0, activebackground=bg, image=on_button, relief=SUNKEN, command=fan_button_state)
                    record_fan_button.grid(
                        row=5, column=1, padx=(298, 0), pady=(0, 20))
                else:
                    record_fan_label = tk.Label(
                        settings_container, bg=bg, fg=fg, font=font, width=15, height=1, anchor=tk.W, text="Report Fans Data")
                    record_fan_label.grid(
                        row=5, column=0, padx=(10, 0), pady=(0, 20))
                    record_fan_button = tk.Button(
                        settings_container, width=50, height=23, bg=bg, fg=fg, bd=0, activebackground=bg, image=off_button, relief=SUNKEN, command=fan_button_state)
                    record_fan_button.grid(
                        row=5, column=1, padx=(298, 0), pady=(0, 20))

                bar.update(10)

                # Start test

                start_button_frame = tk.Frame(combined_test, bg=bg)
                start_button_frame.place(
                    relwidth=1, relheight=0.10, relx=0, rely=0.87)

                start_test = tk.Button(start_button_frame, bg="#b50000", fg="#d0d0d0", activebackground="#a10000", activeforeground="#d0d0d0",
                                       width=12, height=1, bd=0, anchor=tk.CENTER, font=font, text="FULL TEST", relief=SUNKEN, command=combined_test_function)
                start_test.grid(row=0, column=0, padx=(150, 10), pady=0)

                write_only = tk.Button(start_button_frame, bg="#16395b", fg="#d0d0d0", activebackground="#11314f", relief=SUNKEN, activeforeground="#d0d0d0",
                                       width=12, height=1, bd=0, anchor=tk.CENTER, font=font, text="WRITE ONLY", command=save_write_only)
                write_only.grid(row=0, column=1, padx=10, pady=0)

                bar.update(10)

                # Presets for a text file which will be written

                cpu_max_usage_during_test = []
                cpu_max_power_during_test = []
                cpu_max_temp_during_test = []
                cpu_max_clock_during_test = []
                cpu_max_core_usage_during_test = {}
                gpu_max_usage_during_test = []
                gpu_max_temp_during_test = []
                ram_max_usage_during_test = []
                swap_max_usage_during_test = []

                cpu_max_usage_during_test.clear()
                cpu_max_power_during_test.clear()
                cpu_max_temp_during_test.clear()
                cpu_max_core_usage_during_test.clear()
                gpu_max_usage_during_test.clear()
                gpu_max_temp_during_test.clear()
                ram_max_usage_during_test.clear()
                swap_max_usage_during_test.clear()

                max_cpu_usg = 0
                max_gpu_usg = 0

                bar.update(10)

                # Fun facts about the app

                fun_facts_frame = tk.Frame(home_frame, bg=bg)
                fun_facts_frame.place(
                    relwidth=0.59, relheight=0.30, relx=0.415, rely=0.7)

                fun_facts_text_frame = tk.Frame(fun_facts_frame, bg=bg)
                fun_facts_text_frame.place(
                    relwidth=0.4, relheight=0.1, relx=0.015, rely=0.05)

                fun_facts_text = tk.Label(fun_facts_text_frame, bg=bg, fg=fg,
                                          font=font, anchor=tk.W, width=100, height=1, text="FUN FACTS")
                fun_facts_text.pack()

                ff_container = tk.Frame(fun_facts_frame, bg=bg)
                ff_container.place(
                    relwidth=1, relheight=0.7, relx=0, rely=0.20)

                fun_fact = tk.Label(ff_container, bg=bg, fg=fg, font=("Oxygen", 20), anchor=tk.CENTER, width=100,
                                    height=10, text="")
                fun_fact.pack()

                rand_num_list = []

                bar.update(10)

                get_time()
                fun_facts()

                bar.update(40)

                loading.pack_forget()
        dec_home = root.after(15, declare_home)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# Following functions change the theme of the app #

try:
    def write_to_file(self):
        refrate = refresh_rate_entry.get()
        x = refrate.isnumeric()

        if x == False:
            MessageBox(
                'Warning!', f'Value must be a number! - Your pick: {refresh_rate_entry.get()}', 0)

        elif int(refresh_rate_entry.get()) < 500 or int(refresh_rate_entry.get()) >= 10000:
            MessageBox(
                'Warning!', f'Please choose values between 500 and 10000 - Your pick: {refresh_rate_entry.get()}', 0)
        else:
            with open("Code\Config\switches.txt") as f:
                a = f.read()

            with open("Code\Config\switches.txt") as f:
                s = f.readlines()

            with open("Code\Config\switches.txt", "w") as f:
                for line in s:
                    if "refresh_rate " in line:
                        split = line.split()

                        a = a.replace(
                            f"{split[2]}", f"{refresh_rate_entry.get()}")
                f.write(a)
                print(
                    f"Refresh Rate saved! - New Value: {refresh_rate_entry.get()}")
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()


# Metallic theme
try:
    def metallic_theme():
        conf = open(
            'Code\Config\config.txt', 'w')
        conf.write("canvas_color = #121212\nbg_color = #202020\nfg_color = #d0d0d0\nsidemenu_color = #2a2a2a\nbutton_bg_color = #16395b\ntheme_selected = metallic")
        conf.close()
        print("Metallic theme applied!")

        MessageBox('Theme Applied!',
                   'Theme has been successfully applied.\n\nRestart is required for changes to take effect.', 0)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()

# Denim theme
try:
    def denim():
        conf = open(
            'Code\Config\config.txt', 'w')
        conf.write("canvas_color = #242f41\nbg_color = #1b2331\nfg_color = #ffffff\nsidemenu_color = #1b2331\nbutton_bg_color = #303e55\ntheme_selected = denim")
        conf.close()
        print("Denim theme applied!")

        MessageBox('Theme Applied!',
                   'Theme has been successfully applied.\n\nRestart is required for changes to take effect.', 0)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()


# Red/Black theme
try:
    def redblack_theme():
        conf = open(
            'Code\Config\config.txt', 'w')
        conf.write("canvas_color = #1f1f1f\nbg_color = #1a1a1a\nfg_color = #ff3d3d\nsidemenu_color = #1a1a1a\nbutton_bg_color = #ff3d3d\ntheme_selected = redblack")
        conf.close()
        print("Red/Black theme applied!")

        MessageBox('Theme Applied!',
                   'Theme has been successfully applied.\n\nRestart is required for changes to take effect.', 0)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()

# Black/White theme
try:
    def blackwhite_theme():
        conf = open(
            'Code\Config\config.txt', 'w')
        conf.write("canvas_color = #ededed\nbg_color = #fafafa\nfg_color = #1c1c1c\nsidemenu_color = #fafafa\nbutton_bg_color = #d6d6d6\ntheme_selected = blackwhite")
        conf.close()
        print("Black/White theme applied!")

        MessageBox('Theme Applied!',
                   'Theme has been successfully applied.\n\nRestart is required for changes to take effect.', 0)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()


# Function for the clock located on the home page

try:
    def get_time():
        global time
        day = date.today()

        currentDate = day.strftime("%B %d, %Y")

        currentTime = datetime.now()

        currentTime = currentTime.strftime("%H:%M:%S")

        dt_time = datetime.now()

        h_accurate_time.configure(text=f"{dt_time.hour}")
        m_accurate_time.configure(text=f"{dt_time.minute}")
        s_accurate_time.configure(text=f"{dt_time.second}")

        s_quotient = dt_time.second / 60

        s_percentage = (s_quotient * 100) / 2.13

        s.configure(text="|"*(int(s_percentage)+1))

        m_quotient = dt_time.minute / 60

        m_percentage = (m_quotient * 100) / 2.13

        m.configure(text="|"*(int(m_percentage)+1))

        h_quotient = dt_time.hour / 24

        h_percentage = (h_quotient * 100) / 2.13

        h.configure(text="|"*(int(h_percentage)+1))

        time = root.after(1000, get_time)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()

# RECORD_CPU - BUTTON STATE #

try:
    def cpu_button_state():
        with open("Code\Config\switches.txt", "r") as file:
            for line in file:
                if "record_cpu" in line:
                    rec_cpu = line.split()

        try:
            if rec_cpu[2] == "True":
                record_cpu_button.configure(image=off_button)
                with open("Code\Config\switches.txt") as f:
                    a = f.read()

                with open("Code\Config\switches.txt") as f:
                    s = f.readlines()

                with open("Code\Config\switches.txt", "w") as f:
                    for line in s:
                        if "record_cpu" in line:
                            cpu_split = line.split()
                            a = a.replace(
                                f"record_cpu = {cpu_split[2]}", "record_cpu = False")
                            break
                    f.write(a)
            else:
                record_cpu_button.configure(image=on_button)
                with open("Code\Config\switches.txt") as f:
                    a = f.read()

                with open("Code\Config\switches.txt") as f:
                    s = f.readlines()

                with open("Code\Config\switches.txt", "w") as f:
                    for line in s:
                        if "record_cpu" in line:
                            cpu_split = line.split()
                            a = a.replace(
                                f"record_cpu = {cpu_split[2]}", "record_cpu = True")
                            break
                    f.write(a)
        except Exception as e:
            print(e)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# RECORD_GPU - BUTTON STATE #

try:
    def gpu_button_state():
        with open("Code\Config\switches.txt", "r") as file:
            for line in file:
                if "record_gpu" in line:
                    rec_gpu = line.split()

        try:
            if rec_gpu[2] == "True":
                record_gpu_button.configure(image=off_button)
                with open("Code\Config\switches.txt") as f:
                    a = f.read()

                with open("Code\Config\switches.txt") as f:
                    s = f.readlines()

                with open("Code\Config\switches.txt", "w") as f:
                    for line in s:
                        if "record_gpu" in line:
                            gpu_split = line.split()
                            a = a.replace(
                                f"record_gpu = {gpu_split[2]}", "record_gpu = False")
                            break
                    f.write(a)
            else:
                record_gpu_button.configure(image=on_button)
                with open("Code\Config\switches.txt") as f:
                    a = f.read()

                with open("Code\Config\switches.txt") as f:
                    s = f.readlines()

                with open("Code\Config\switches.txt", "w") as f:
                    for line in s:
                        if "record_gpu" in line:
                            gpu_split = line.split()
                            a = a.replace(
                                f"record_gpu = {gpu_split[2]}", "record_gpu = True")
                            break
                    f.write(a)
        except Exception as e:
            print(e)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# RECORD_RAM - BUTTON STATE #

try:
    def ram_button_state():
        with open("Code\Config\switches.txt", "r") as file:
            for line in file:
                if "record_ram" in line:
                    rec_ram = line.split()

        try:
            if rec_ram[2] == "True":
                record_ram_button.configure(image=off_button)
                with open("Code\Config\switches.txt") as f:
                    a = f.read()

                with open("Code\Config\switches.txt") as f:
                    s = f.readlines()

                with open("Code\Config\switches.txt", "w") as f:
                    for line in s:
                        if "record_ram" in line:
                            ram_split = line.split()
                            a = a.replace(
                                f"record_ram = {ram_split[2]}", "record_ram = False")
                            break
                    f.write(a)
            else:
                record_ram_button.configure(image=on_button)
                with open("Code\Config\switches.txt") as f:
                    a = f.read()

                with open("Code\Config\switches.txt") as f:
                    s = f.readlines()

                with open("Code\Config\switches.txt", "w") as f:
                    for line in s:
                        if "record_ram" in line:
                            ram_split = line.split()
                            a = a.replace(
                                f"record_ram = {ram_split[2]}", "record_ram = True")
                            break
                    f.write(a)
        except Exception as e:
            print(e)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# RECORD_FANS - BUTTON STATE #

try:
    def fan_button_state():
        with open("Code\Config\switches.txt", "r") as file:
            for line in file:
                if "record_fans" in line:
                    rec_fans = line.split()

        try:
            if rec_fans[2] == "True":
                record_fan_button.configure(image=off_button)
                with open("Code\Config\switches.txt") as f:
                    a = f.read()

                with open("Code\Config\switches.txt") as f:
                    s = f.readlines()

                with open("Code\Config\switches.txt", "w") as f:
                    for line in s:
                        if "record_fans" in line:
                            fans_split = line.split()
                            a = a.replace(
                                f"record_fans = {fans_split[2]}", "record_fans = False")
                            break
                    f.write(a)
            else:
                record_fan_button.configure(image=on_button)
                with open("Code\Config\switches.txt") as f:
                    a = f.read()

                with open("Code\Config\switches.txt") as f:
                    s = f.readlines()

                with open("Code\Config\switches.txt", "w") as f:
                    for line in s:
                        if "record_fans" in line:
                            fans_split = line.split()
                            a = a.replace(
                                f"record_fans = {fans_split[2]}", "record_fans = True")
                            break
                    f.write(a)
        except Exception as e:
            print(e)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# mobo_info - BUTTON STATE #

try:
    def mobo_info_status():
        with open("Code\Config\switches.txt", "r") as file:
            for line in file:
                if "mobo_info" in line:
                    base_inf = line.split()

        try:
            if base_inf[2] == "True":
                mobo_info_button.configure(image=off_button)
                with open("Code\Config\switches.txt") as f:
                    a = f.read()

                with open("Code\Config\switches.txt") as f:
                    s = f.readlines()

                with open("Code\Config\switches.txt", "w") as f:
                    for line in s:
                        if "mobo_info" in line:
                            mobo_info = line.split()
                            a = a.replace(
                                f"mobo_info = {mobo_info[2]}", "mobo_info = False")
                            break
                    f.write(a)
            else:
                mobo_info_button.configure(image=on_button)
                with open("Code\Config\switches.txt") as f:
                    a = f.read()

                with open("Code\Config\switches.txt") as f:
                    s = f.readlines()

                with open("Code\Config\switches.txt", "w") as f:
                    for line in s:
                        if "mobo_info" in line:
                            mobo_info = line.split()
                            a = a.replace(
                                f"mobo_info = {mobo_info[2]}", "mobo_info = True")
                            break
                    f.write(a)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)
# Combined test function

try:
    def combined_test_function():
        global combined_test_frame
        global max_record

        try:
            home_frame.place_forget()
            root.after_cancel(time)
            root.after_cancel(ff)
        except Exception as e:
            print(e)

        combined_test_frame = tk.Frame(root, bg=canvas_bg)
        combined_test_frame.place(
            relwidth=0.875, relheight=0.96, relx=0.117, rely=0.021)

        loading = tk.Label(combined_test_frame, bg=canvas_bg, fg=fg, font=(
            loading_font), width=100, height=50, text="Loading...")
        loading.pack()

        def declare_test():
            global home_image
            global total_usage_bar
            global total_usage_num
            global package_temp_bar
            global package_temp_value_label
            global frequency_bar
            global frequency_value_label
            global total_gpu_usage_bar
            global total_gpu_usage_num
            global current_temp_bar
            global current_temp_num_label
            global vram_bar
            global vram_value_label
            global ram_usage_bar
            global ram_usage_value_label
            global ram_free_bar
            global ram_free_value_label
            global max_cpu_usage
            global max_cpu_temp
            global max_gpu_usage
            global max_gpu_temp
            global max_ram_usage
            global max_ram_free
            global power_usage_bar
            global power_value_label
            global max_cpu_pwr

            root.after_cancel(dec_test)
            with tqdm(total=100) as bar:
                # CPU USAGE

                usage_frame = tk.Frame(combined_test_frame, bg=bg)
                usage_frame.place(
                    relwidth=0.49, relheight=0.19, relx=0, rely=0)

                usage_label_frame = tk.Frame(usage_frame, bg=bg)
                usage_label_frame.place(
                    relwidth=0.45, relheight=0.15, relx=0.02, rely=0.08)

                usage_label = tk.Label(usage_label_frame, bg=bg, fg=fg, width=100,
                                       height=1, anchor=tk.W, font=font, text="CPU USAGE")
                usage_label.pack()

                total_usage_frame = tk.Frame(usage_frame, bg=bg)
                total_usage_frame.place(
                    relwidth=1, relheight=0.90, relx=0.02, rely=0.426)

                total_usage = tk.Label(total_usage_frame, bg=bg, fg=fg, anchor=tk.W,
                                       font=font, width=100, height=1, text="Total usage")
                total_usage.pack()

                total_usage_bar = tk.Label(total_usage_frame, bg=bg, fg=fg, anchor=tk.W,
                                           font=font, width=100, height=1, text="|")
                total_usage_bar.pack()

                total_usage_num_frame = tk.Frame(usage_frame, bg=bg)
                total_usage_num_frame.place(
                    relwidth=0.25, relheight=0.15, relx=0.72, rely=0.465)

                total_usage_num = tk.Label(total_usage_num_frame, bg=bg, fg=fg,
                                           font=font, anchor=tk.E, width=15, height=15, text="0%")
                total_usage_num.pack()

                bar.update(10)

                # CPU TEMPERATURE

                temp_frame = tk.Frame(combined_test_frame, bg=bg)
                temp_frame.place(
                    relwidth=0.49, relheight=0.19, relx=0, rely=0.21)

                temperature_frame = tk.Frame(temp_frame, bg=bg)
                temperature_frame.place(
                    relwidth=0.40, relheight=0.15, relx=0.02, rely=0.08)

                temp_label = tk.Label(temperature_frame, bg=bg, fg=fg, width=100,
                                      height=100, anchor=tk.W, font=font, text="CPU TEMPERATURE")
                temp_label.pack()

                package_temp = tk.Frame(temp_frame, bg=bg)
                package_temp.place(relwidth=0.963, relheight=0.50,
                                   relx=0.018, rely=0.426)

                package_temp_label = tk.Label(package_temp, bg=bg, fg=fg, font=font,
                                              anchor=tk.W, width=100, height=1, text="Package Temperature")
                package_temp_label.pack()

                package_temp_bar = tk.Label(
                    package_temp, bg=bg, fg=fg, font=font, anchor=tk.W, width=200, height=1, text="|")
                package_temp_bar.pack()

                package_temp_value = tk.Frame(temp_frame, bg="white")
                package_temp_value.place(
                    relwidth=0.15, relheight=0.25, relx=0.83, rely=0.40)

                package_temp_value_label = tk.Label(
                    package_temp_value, bg=bg, fg=fg, font=font, anchor=tk.E, width=15, height=15, text="0°C")
                package_temp_value_label.pack()

                bar.update(10)

                # CPU FREQUENCY

                cpu_frequency = tk.Frame(combined_test_frame, bg=bg)
                cpu_frequency.place(
                    relwidth=0.49, relheight=0.19, relx=0, rely=0.42)

                frequency_frame = tk.Frame(cpu_frequency, bg=bg)
                frequency_frame.place(
                    relwidth=0.4, relheight=0.15, relx=0.02, rely=0.08)

                frequency_frame_label = tk.Label(
                    frequency_frame, bg=bg, fg=fg, font=font, anchor=tk.W, width=100, height=10, text="CPU FREQUENCY")
                frequency_frame_label.pack()

                frequency = tk.Frame(cpu_frequency, bg=bg)
                frequency.place(relwidth=0.963, relheight=0.50,
                                relx=0.021, rely=0.426)

                frequency_label = tk.Label(frequency, bg=bg, fg=fg, font=font,
                                           anchor=tk.W, width=100, height=1, text="Current Frequency")
                frequency_label.pack()

                frequency_bar = tk.Label(
                    frequency, bg=bg, fg=asm_cyan, font=font, anchor=tk.W, width=100, height=1, text="|")
                frequency_bar.pack()

                frequency_value = tk.Frame(cpu_frequency, bg=bg)
                frequency_value.place(relwidth=0.3, relheight=0.2,
                                      relx=0.72, rely=0.426)

                frequency_value_label = tk.Label(
                    frequency_value, bg=bg, fg=fg, font=font, anchor=tk.E, width=10, height=10, text="0 MHz")
                frequency_value_label.pack()

                bar.update(10)

                # CPU POWER

                cpu_power = tk.Frame(combined_test_frame, bg=bg)
                cpu_power.place(relwidth=0.49, relheight=0.19,
                                relx=0, rely=0.63)

                cpu_power_frame = tk.Frame(cpu_power, bg=bg)
                cpu_power_frame.place(
                    relwidth=0.40, relheight=0.15, relx=0.02, rely=0.08)

                cpu_power_label = tk.Label(cpu_power_frame, bg=bg, fg=fg, font=font,
                                           anchor=tk.W, width=100, height=10, text="CPU POWER")
                cpu_power_label.pack()

                power_consumption = tk.Frame(cpu_power, bg=bg)
                power_consumption.place(
                    relwidth=0.963, relheight=0.50, relx=0.021, rely=0.426)

                power_consumption_label = tk.Label(
                    power_consumption, bg=bg, fg=fg, font=font, anchor=tk.W, width=100, height=1, text="Power Usage")
                power_consumption_label.pack()

                power_usage_bar = tk.Label(power_consumption, bg=bg, fg=fg,
                                           font=font, anchor=tk.W, width=100, height=1, text="|")
                power_usage_bar.pack()

                power_value = tk.Frame(cpu_power, bg=bg)
                power_value.place(relwidth=0.2, relheight=0.2,
                                  relx=0.78, rely=0.426)

                power_value_label = tk.Label(
                    power_value, bg=bg, fg=fg, font=font, anchor=tk.E, width=10, height=10, text="0 W")
                power_value_label.pack()

                bar.update(10)

                # GPU USAGE

                gpu_usage = tk.Frame(combined_test_frame, bg=bg)
                gpu_usage.place(relwidth=0.49, relheight=0.19,
                                relx=0.505, rely=0)

                usage_frame = tk.Frame(gpu_usage, bg=bg)
                usage_frame.place(relwidth=0.4, relheight=0.15,
                                  relx=0.02, rely=0.08)

                usage_label = tk.Label(usage_frame, bg=bg, fg=fg, width=100,
                                       height=1, anchor=tk.W, font=font, text="GPU USAGE")
                usage_label.pack()

                total_gpu_usage = tk.Frame(gpu_usage, bg=bg)
                total_gpu_usage.place(relwidth=1, relheight=0.90,
                                      relx=0.02, rely=0.426)

                total_gpu_usage_label = tk.Label(total_gpu_usage, bg=bg, fg=fg, width=100,
                                                 height=1, anchor=tk.W, font=font, text="Total usage")
                total_gpu_usage_label.pack()

                total_gpu_usage_bar = tk.Label(total_gpu_usage, bg=bg, fg=fg, width=100,
                                               height=1, anchor=tk.W, font=font, text="|")
                total_gpu_usage_bar.pack()

                total_gpu_usage_num_frame = tk.Frame(gpu_usage, bg=bg)
                total_gpu_usage_num_frame.place(
                    relwidth=0.25, relheight=0.15, relx=0.72, rely=0.465)

                total_gpu_usage_num = tk.Label(total_gpu_usage_num_frame, bg=bg,
                                               fg=fg, font=font, anchor=tk.E, width=15, height=15, text="0%")
                total_gpu_usage_num.pack()

                bar.update(10)

                # GPU TEMPERATURE

                gpu_temp = tk.Frame(combined_test_frame, bg=bg)
                gpu_temp.place(relwidth=0.49, relheight=0.19,
                               relx=0.505, rely=0.21)

                gpu_temp_frame = tk.Frame(gpu_temp, bg=bg)
                gpu_temp_frame.place(relwidth=0.40, relheight=0.15,
                                     relx=0.02, rely=0.08)

                gpu_temp_label = tk.Label(gpu_temp_frame, bg=bg, fg=fg, width=100,
                                          height=100, anchor=tk.W, font=font, text="GPU TEMPERATURE")
                gpu_temp_label.pack()

                temp_container = tk.Frame(gpu_temp, bg=bg)
                temp_container.place(relwidth=0.963, relheight=0.50,
                                     relx=0.018, rely=0.426)

                current_temp = tk.Label(temp_container, bg=bg, fg=fg, width=100,
                                        height=1, anchor=tk.W, font=font, text="Package Temperature")
                current_temp.pack()

                current_temp_bar = tk.Label(temp_container, bg=bg, fg=fg, width=100,
                                            height=1, anchor=tk.W, font=font, text="|")
                current_temp_bar.pack()

                current_temp_num = tk.Frame(gpu_temp, bg=bg)
                current_temp_num.place(
                    relwidth=0.15, relheight=0.25, relx=0.83, rely=0.40)

                current_temp_num_label = tk.Label(current_temp_num, bg=bg, fg=fg, width=15,
                                                  height=15, anchor=tk.E, font=font, text="0°C")
                current_temp_num_label.pack()

                bar.update(10)

                # GPU VRAM
                gpu_vram_usage = tk.Frame(combined_test_frame, bg=bg)
                gpu_vram_usage.place(relwidth=0.49, relheight=0.19,
                                     relx=0.505, rely=0.42)

                vram_frame = tk.Frame(gpu_vram_usage, bg=bg)
                vram_frame.place(relwidth=0.4, relheight=0.15,
                                 relx=0.02, rely=0.08)

                vram_label = tk.Label(vram_frame, bg=bg, fg=fg, font=font,
                                      anchor=tk.W, width=100, height=10, text="VRAM USAGE")
                vram_label.pack()

                vram = tk.Frame(gpu_vram_usage, bg=bg)
                vram.place(relwidth=0.963, relheight=0.50,
                           relx=0.021, rely=0.426)

                vram_label = tk.Label(vram, bg=bg, fg=fg, font=font,
                                      anchor=tk.W, width=100, height=1, text="VRAM")
                vram_label.pack()

                vram_bar = tk.Label(vram, bg=bg, fg=fg, font=font,
                                    anchor=tk.W, width=100, height=1, text="|")
                vram_bar.pack()

                vram_value = tk.Frame(gpu_vram_usage, bg=bg)
                vram_value.place(relwidth=0.3, relheight=0.2,
                                 relx=0.684, rely=0.426)

                vram_value_label = tk.Label(
                    vram_value, bg=bg, fg=fg, anchor=tk.E, font=font, width=40, height=15, text="0GB/0GB")
                vram_value_label.pack()

                bar.update(10)

                # RAM USAGE

                ram_usage_frame = tk.Frame(combined_test_frame, bg=bg)
                ram_usage_frame.place(
                    relwidth=0.49, relheight=0.19, relx=0.505, rely=0.63)

                ram_usage_label_frame = tk.Frame(ram_usage_frame, bg=bg)
                ram_usage_label_frame.place(
                    relwidth=0.30, relheight=0.15, relx=0.02, rely=0.08)

                ram_usage_label = tk.Label(ram_usage_label_frame, bg=bg, fg=fg,
                                           font=font, anchor=tk.W, width=100, height=10, text="RAM USAGE")
                ram_usage_label.pack()

                ram_usage_container = tk.Frame(ram_usage_frame, bg=bg)
                ram_usage_container.place(
                    relwidth=0.963, relheight=0.5, relx=0.018, rely=0.426)

                ram_usage = tk.Label(ram_usage_container, bg=bg, fg=fg, font=font,
                                     anchor=tk.W, width=100, height=1, text="Total Usage")
                ram_usage.pack()

                ram_usage_bar = tk.Label(ram_usage_container, bg=bg, fg=fg,
                                         font=font, anchor=tk.W, width=100, height=1, text="|")
                ram_usage_bar.pack()

                ram_usage_value_frame = tk.Frame(ram_usage_frame, bg=bg)
                ram_usage_value_frame.place(
                    relwidth=0.30, relheight=0.2, relx=0.684, rely=0.426)

                ram_usage_value_label = tk.Label(
                    ram_usage_value_frame, bg=bg, fg=fg, font=font, anchor=tk.E, width=40, height=15, text="0GB/0GB")
                ram_usage_value_label.pack()

                bar.update(10)

                # CPU/GPU MAX

                cpu_gpu_max = tk.Frame(combined_test_frame, bg=bg)
                cpu_gpu_max.place(
                    relwidth=0.49, relheight=0.17, relx=0, rely=0.84)

                cpu_gpu_max_text_frame = tk.Frame(cpu_gpu_max, bg=bg)
                cpu_gpu_max_text_frame.place(
                    relwidth=0.4, relheight=0.12, relx=0.02, rely=0.10)

                cpu_gpu_max_text = tk.Label(cpu_gpu_max_text_frame, bg=bg, fg=fg,
                                            font=font, anchor=tk.W, width=100, height=10, text="CPU/GPU MAX")
                cpu_gpu_max_text.pack()

                # MAX CPU USAGE
                max_cpu_usage_text = tk.Label(cpu_gpu_max, bg=bg, fg=fg, font=font,
                                              anchor=tk.CENTER, width=10, height=1, text="CPU Usage")
                max_cpu_usage_text.grid(
                    row=0, column=0, padx=(7), pady=(50, 0))

                max_cpu_usage = tk.Label(cpu_gpu_max, bg=bg, fg=fg, font=font,
                                         anchor=tk.CENTER, width=10, height=1, text="0%")
                max_cpu_usage.grid(row=1, column=0, padx=(7), pady=(0))

                # MAX CPU TEMPERATURE
                max_cpu_temp_text = tk.Label(cpu_gpu_max, bg=bg, fg=fg, font=font,
                                             anchor=tk.CENTER, width=10, height=1, text="CPU Temp")
                max_cpu_temp_text.grid(row=0, column=1, padx=(7), pady=(50, 0))

                max_cpu_temp = tk.Label(cpu_gpu_max, bg=bg, fg=fg, font=font,
                                        anchor=tk.CENTER, width=10, height=1, text="0°C")
                max_cpu_temp.grid(row=1, column=1, padx=(7), pady=(0))

                # MAX GPU USAGE
                max_gpu_usage_text = tk.Label(cpu_gpu_max, bg=bg, fg=fg, font=font,
                                              anchor=tk.CENTER, width=10, height=1, text="GPU Usage")
                max_gpu_usage_text.grid(
                    row=0, column=2, padx=(7), pady=(50, 0))

                max_gpu_usage = tk.Label(cpu_gpu_max, bg=bg, fg=fg, font=font,
                                         anchor=tk.CENTER, width=10, height=1, text="0%")
                max_gpu_usage.grid(row=1, column=2, padx=(7), pady=(0))

                # MAX GPU TEMPERATURE
                max_gpu_temp_text = tk.Label(cpu_gpu_max, bg=bg, fg=fg, font=font,
                                             anchor=tk.CENTER, width=10, height=1, text="GPU Temp")
                max_gpu_temp_text.grid(row=0, column=3, padx=(7), pady=(50, 0))

                max_gpu_temp = tk.Label(cpu_gpu_max, bg=bg, fg=fg, font=font,
                                        anchor=tk.CENTER, width=10, height=1, text="0°C")
                max_gpu_temp.grid(row=1, column=3, padx=(7), pady=(0))

                bar.update(10)

                # RAM MAX

                ram_max = tk.Frame(combined_test_frame, bg=bg)
                ram_max.place(relwidth=0.37, relheight=0.17,
                              relx=0.505, rely=0.84)

                ram_max_text_frame = tk.Frame(ram_max, bg=bg)
                ram_max_text_frame.place(
                    relwidth=0.4, relheight=0.12, relx=0.02, rely=0.10)

                ram_max_text = tk.Label(ram_max_text_frame, bg=bg, fg=fg,
                                        font=font, anchor=tk.W, width=100, height=10, text="RAM/CPU MAX")
                ram_max_text.pack()

                # MAX RAM USAGE
                max_ram_usage_text = tk.Label(ram_max, bg=bg, fg=fg, font=font,
                                              anchor=tk.CENTER, width=10, height=1, text="RAM USED")
                max_ram_usage_text.grid(
                    row=0, column=0, padx=(50, 50), pady=(50, 0))

                max_ram_usage = tk.Label(ram_max, bg=bg, fg=fg, font=font,
                                         anchor=tk.CENTER, width=10, height=1, text="0%")
                max_ram_usage.grid(row=1, column=0, padx=(50, 50), pady=(0))

                # MAX FREE
                max_cpu_pwr_text = tk.Label(ram_max, bg=bg, fg=fg, font=font,
                                            anchor=tk.CENTER, width=10, height=1, text="CPU POWER")
                max_cpu_pwr_text.grid(row=0, column=1, padx=(0), pady=(50, 0))

                max_cpu_pwr = tk.Label(ram_max, bg=bg, fg=fg, font=font,
                                       anchor=tk.CENTER, width=10, height=1, text="0 W")
                max_cpu_pwr.grid(row=1, column=1, padx=(0), pady=(0))

                # HOME BUTTON
                home_btn_frame = tk.Frame(combined_test_frame, bg=bg)
                home_btn_frame.place(
                    relwidth=0.105, relheight=0.17, relx=0.89, rely=0.84)

                home_image = PhotoImage(file=f"{image_path}\homeCrop.png")

                home_btn = tk.Button(home_btn_frame, bg="#b50000", fg="#ffffff", activebackground="#a10000",
                                     width=110, height=122, bd=0, image=home_image, command=home)
                home_btn.pack()

                bar.update(10)

                loading.pack_forget()
                refresh_combined_test()

        max_record = 0

        dec_test = root.after(15, declare_test)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# Refresh combined test set amount of miliseconds

try:
    def refresh_combined_test():
        global rct
        global max_record
        global cpuPerc
        global temp_last
        global clock_last
        global clock_max
        global power_last
        global gpu_load
        global gpu_total_memory_test
        global gpu_temperature
        global gpu_used_memory
        global vmem_used
        global vmem_total
        global vmem_free
        global sv_used
        global sv_total
        global sv_free
        # READ CONFIG FILE
        with open("Code\Config\switches.txt", "r") as file:
            s = file.readlines()
            for line in s:
                if "refresh_rate" in line:
                    split = line.split()

        # UPDATING CPU #

        # USAGE
        try:
            cpuPerc = psutil.cpu_percent()
        except Exception as e:
            print(e)

        # MAX USAGE
        try:
            if cpuPerc not in cpu_max_usage_list:
                if cpuPerc > max_record:
                    cpu_max_usage_during_test.append(cpuPerc)
                    max_record = cpuPerc
                else:
                    max_cpu_usage.configure(
                        text=f"{max(cpu_max_usage_during_test)}%")
        except Exception as e:
            print(e)

        try:
            total_usage_num.configure(text=f"{cpuPerc}%")

            usage_perc = ((cpuPerc / 100) * 100) / 1.65

            total_usage_bar.configure(text=f"|"*int(usage_perc))
        except Exception as e:
            print(e)

        try:
            if cpuPerc < 40:
                total_usage_bar.configure(fg=asm_cyan)
            if cpuPerc > 40 and cpuPerc < 60:
                total_usage_bar.configure(fg=asm_yellow)
            if cpuPerc > 60 and cpuPerc < 80:
                total_usage_bar.configure(fg=asm_orange)
            if cpuPerc > 80:
                total_usage_bar.configure(fg=asm_red)
        except Exception as e:
            print(e)

        try:
            if max(cpu_max_usage_during_test) <= 40:
                max_cpu_usage.configure(fg=asm_cyan)
            elif max(cpu_max_usage_during_test) > 40 and max(cpu_max_usage_during_test) <= 60:
                max_cpu_usage.configure(fg=asm_yellow)
            elif max(cpu_max_usage_during_test) > 60 and max(cpu_max_usage_during_test) <= 80:
                max_cpu_usage.configure(fg=asm_orange)
            elif max(cpu_max_usage_during_test) > 80:
                max_cpu_usage.configure(fg=asm_red)
        except Exception as e:
            print(e)

        # TEMPERATURE

        try:
            w = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            temperature_info = w.Sensor()
            for sensor in temperature_info:
                if sensor.SensorType == u"Temperature":
                    if sensor.Name == u"CPU Package":
                        temp_last = sensor.Value

                        temp_quotient = sensor.Value / 100

                        temp_perc = temp_quotient * 100 / 1.8

                        package_temp_bar.configure(
                            text=f"|"*int(temp_perc))

                        package_temp_value_label.configure(
                            text=f"{sensor.Value:.2f}°C")

                        if sensor.Value < 50:
                            package_temp_bar.configure(fg=asm_cyan)
                        if sensor.Value > 50 and sensor.Value < 70:
                            package_temp_bar.configure(fg=asm_yellow)
                        if sensor.Value > 70 and sensor.Value < 90:
                            package_temp_bar.configure(fg=asm_orange)
                        if sensor.Value > 90:
                            package_temp_bar.configure(fg=asm_red)

                        # Max temperature

                        if sensor.Value not in cpu_max_temp_during_test:
                            cpu_max_temp_during_test.append(sensor.Value)
                        else:
                            pass

                        max_cpu_temp.configure(
                            text=f"{max(cpu_max_temp_during_test):.2f}°C")

                        if max(cpu_max_temp_during_test) <= 50:
                            max_cpu_temp.configure(fg=asm_cyan)
                        elif max(cpu_max_temp_during_test) > 50 and max(cpu_max_temp_during_test) <= 70:
                            max_cpu_temp.configure(fg=asm_yellow)
                        elif max(cpu_max_temp_during_test) > 70 and max(cpu_max_temp_during_test) <= 90:
                            max_cpu_temp.configure(fg=asm_orange)
                        elif max(cpu_max_temp_during_test) > 90:
                            max_cpu_temp.configure(fg=asm_red)
                        break
        except Exception as e:
            print(e)

        # FREQUENCY
        try:
            c = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            clocks = c.Sensor()
            for sensor in clocks:
                if sensor.SensorType == u"Clock":
                    if sensor.Name == u"CPU Core #1":
                        clock_last = sensor.Value

                        if clock_last not in cpu_max_clock_during_test:
                            cpu_max_clock_during_test.append(clock_last)

                        clock_max = max(cpu_max_clock_during_test)

                        freq_quotient = (
                            (clock_last / clock_max) * 100) / 1.65

                        frequency_bar.configure(
                            text=f"|"*int(freq_quotient))
                        frequency_value_label.configure(
                            text=f"{clock_last:.1f} MHz")

        except Exception as e:
            print(e)

        # POWER

        try:
            pwr = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            pwr_info = pwr.Sensor()
            for sensor in pwr_info:
                if sensor.SensorType == u"Power":
                    if sensor.Name == u"CPU Package":
                        power_last = sensor.Value

                        power_value_label.configure(
                            text=f"{sensor.Value:.2f} W")
                        power_perc = ((sensor.Value / sensor.Max) * 100) / 1.65
                        power_usage_bar.configure(text="|"*int(power_perc))

                        if sensor.Value not in cpu_max_power_during_test:
                            cpu_max_power_during_test.append(sensor.Value)
                        else:
                            pass

                        # Max power

                        max_cpu_pwr.configure(
                            text=f"{max(cpu_max_power_during_test):.2f} W")

                        if sensor.Value <= sensor.Max * 0.5:
                            power_usage_bar.configure(fg=asm_cyan)
                        if sensor.Value > sensor.Max * 0.5 and sensor.Value <= sensor.Max * 0.7:
                            power_usage_bar.configure(fg=asm_yellow)
                        if sensor.Value > sensor.Max * 0.7 and sensor.Value <= sensor.Max * 0.9:
                            power_usage_bar.configure(fg=asm_orange)
                        if sensor.Value > sensor.Max * 0.9:
                            power_usage_bar.configure(fg=asm_red)

                         # Adjust color for max values
                        if max(cpu_max_power_during_test) < max(cpu_max_power_during_test) * 0.5:
                            max_cpu_pwr.configure(fg=asm_cyan)
                        elif max(cpu_max_power_during_test) > max(cpu_max_power_during_test) * 0.5 and max(cpu_max_power_during_test) <= max(cpu_max_power_during_test) * 0.7:
                            max_cpu_pwr.configure(fg=asm_yellow)
                        elif max(cpu_max_power_during_test) > max(cpu_max_power_during_test) * 0.7 and max(cpu_max_power_during_test) <= max(cpu_max_power_during_test) * 0.9:
                            max_cpu_pwr.configure(fg=asm_orange)
                        elif max(cpu_max_power_during_test) > max(cpu_max_power_during_test) * 0.9:
                            max_cpu_pwr.configure(fg=asm_red)
        except Exception as e:
            print(e)
        # UPDATING GPU #

        # USAGE

        # Find gpus
        try:
            devices = GPUtil.getGPUs()

            for gpu in devices:
                gpu_load = f"{gpu.load*100}"
                gpu_total_memory_test = f"{gpu.memoryTotal / 1000}"
                gpu_temperature = f"{gpu.temperature}"
                gpu_used_memory = f"{gpu.memoryUsed / 1000}"

            # A little math to optimize the percentage to bar length
            load_perc = float(gpu_load) / 1.65
            mem_perc = ((float(gpu_used_memory) /
                         float(gpu_total_memory_test)) * 100) / 1.65
            temp_perc = ((float(gpu_temperature) / 120) * 100) / 1.65
        except Exception as e:
            print(e)

        try:
            # Update usage
            if int(load_perc) < 1:
                total_gpu_usage_bar.configure(text="|")
            else:
                total_gpu_usage_bar.configure(text="|"*int(load_perc))
                total_gpu_usage_num.configure(text=f"{float(gpu_load):.1f}%")
        except Exception as e:
            print(e)

        try:
            # Adjust colors for usage
            if float(gpu_load) <= 30:
                total_gpu_usage_bar.configure(fg=asm_cyan)
            elif float(gpu_load) > 30 and float(gpu_load) <= 60:
                total_gpu_usage_bar.configure(fg=asm_yellow)
            elif float(gpu_load) > 60 and float(gpu_load) <= 80:
                total_gpu_usage_bar.configure(fg=asm_orange)
            elif float(gpu_load) > 80:
                total_gpu_usage_bar.configure(fg=asm_red)
        except Exception as e:
            print(e)

        # MAX USAGE
        try:
            if gpu_load not in gpu_max_usage_during_test:
                gpu_max_usage_during_test.append(gpu_load)
            else:
                if float(max(gpu_max_usage_during_test)) < 30:
                    max_gpu_usage.configure(fg=asm_cyan)
                elif float(max(gpu_max_usage_during_test)) > 30 and float(max(gpu_max_usage_during_test)) <= 60:
                    max_gpu_usage.configure(fg=asm_yellow)
                elif float(max(gpu_max_usage_during_test)) > 60 and float(max(gpu_max_usage_during_test)) <= 80:
                    max_gpu_usage.configure(fg=asm_orange)
                elif float(max(gpu_max_usage_during_test)) > 80:
                    max_gpu_usage.configure(fg=asm_red)

                max_gpu_usage.configure(
                    text=f"{max(gpu_max_usage_during_test)}%")
        except Exception as e:
            print(e)

        # TEMPERATURE
        try:
            current_temp_bar.configure(text="|"*int(temp_perc))
            current_temp_num_label.configure(text=f"{gpu_temperature}°C")
        except Exception as e:
            print(e)

        try:
            # Adjust colors for temperature
            if float(gpu_temperature) < 50:
                current_temp_bar.configure(fg=asm_cyan)
            elif float(gpu_temperature) > 50 and float(gpu_temperature) <= 60:
                current_temp_bar.configure(fg=asm_yellow)
            elif float(gpu_temperature) > 60 and float(gpu_temperature) <= 75:
                current_temp_bar.configure(fg=asm_orange)
            elif float(gpu_temperature) > 75:
                current_temp_bar.configure(fg=asm_red)
        except Exception as e:
            print(e)
        # MAX TEMPERATURE
        try:
            if gpu_temperature not in gpu_max_temp_during_test:
                gpu_max_temp_during_test.append(gpu_temperature)
            else:
                if float(max(gpu_max_temp_during_test)) < 50:
                    max_gpu_temp.configure(fg=asm_cyan)
                elif float(max(gpu_max_temp_during_test)) > 50 and float(max(gpu_max_temp_during_test)) <= 60:
                    max_gpu_temp.configure(fg=asm_yellow)
                elif float(max(gpu_max_temp_during_test)) > 60 and float(max(gpu_max_temp_during_test)) <= 75:
                    max_gpu_temp.configure(fg=asm_orange)
                elif float(max(gpu_max_temp_during_test)) > 75:
                    max_gpu_temp.configure(fg=asm_red)

                max_gpu_temp.configure(
                    text=f"{max(gpu_max_temp_during_test)}°C")
        except Exception as e:
            print(e)

        # VRAM
        try:
            vram_bar.configure(text="|"*int(mem_perc))
            vram_value_label.configure(
                text=f"{float(gpu_used_memory):.2f}GB/{float(gpu_total_memory_test):.2f}GB")

            mem_perc_unop = (
                (float(gpu_used_memory) / float(gpu_total_memory_test)) * 100)
        except Exception as e:
            print(e)

        try:
            if mem_perc_unop < 10:
                vram_bar.configure(fg=asm_cyan)
            elif mem_perc_unop > 10 and mem_perc_unop <= 30:
                vram_bar.configure(fg=asm_green)
            elif mem_perc_unop > 30 and mem_perc_unop <= 60:
                vram_bar.configure(fg=asm_yellow)
            elif mem_perc_unop > 60 and mem_perc_unop <= 80:
                vram_bar.configure(fg=asm_orange)
            elif mem_perc_unop > 80:
                vram_bar.configure(fg=asm_red)
        except Exception as e:
            print(e)
        # UPDATING RAM #
        vmem = psutil.virtual_memory()
        vmem_used = vmem.used
        vmem_total = vmem.total
        vmem_free = vmem.free

        svmem = psutil.swap_memory()
        sv_used = svmem.used
        sv_total = svmem.total
        sv_free = svmem.free

        # USAGE

        try:
            ram_usage_value_label.configure(
                text=f"{get_size(vmem_used)}/{get_size(vmem_total)}")
            usg_perc = (vmem_used / vmem_total) * 100
            usg_perc_optimized = usg_perc / 1.65
            ram_usage_bar.configure(text="|"*int(usg_perc_optimized))
            if vmem_used not in ram_max_usage_during_test:
                ram_max_usage_during_test.append(vmem_used)
            else:
                pass

            if sv_used not in swap_max_usage_during_test:
                swap_max_usage_during_test.append(sv_used)
            else:
                pass
        except Exception as e:
            print(e)

        try:
            # Adjusting colors for RAM usages
            if usg_perc < 50:
                ram_usage_bar.configure(fg=asm_cyan)
            if usg_perc > 50 and usg_perc < 70:
                ram_usage_bar.configure(fg=asm_yellow)
            if usg_perc > 70 and usg_perc < 90:
                ram_usage_bar.configure(fg=asm_orange)
            if usg_perc > 90:
                ram_usage_bar.configure(fg=asm_red)
        except Exception as e:
            print(e)

        # MAX USAGE
        try:
            max_ram_usage.configure(
                text=f"{get_size(max(ram_max_usage_during_test))}")
            max_perc = (max(ram_max_usage_during_test) / vmem.total) * 100
        except Exception as e:
            print(e)

        try:
            # Adjusting colors for MAX RAM usage
            if max_perc < 50:
                max_ram_usage.configure(fg=asm_cyan)
            if max_perc > 50 and max_perc < 70:
                max_ram_usage.configure(fg=asm_yellow)
            if max_perc > 70 and max_perc < 90:
                max_ram_usage.configure(fg=asm_orange)
            if max_perc > 90:
                max_ram_usage.configure(fg=asm_red)

        except Exception as e:
            print(e)

        full_test()

        # Update test
        rct = root.after(split[2], refresh_combined_test)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()

# WRITING STATISTICS TO A FILE - FULL TEST #
try:
    def full_test():
        global max_cpu_usg
        global max_gpu_usg

        main_line_separator = "-"*80
        line_separator = "-"*5

        with open("Code\Config\switches.txt", "r") as file:
            for line in file:
                if "mobo_info" in line:
                    mobo_info = line.split()
                if "record_cpu" in line:
                    rec_cpu = line.split()
                if "record_gpu" in line:
                    rec_gpu = line.split()
                if "record_ram" in line:
                    rec_ram = line.split()
                if "record_fans" in line:
                    rec_fans = line.split()

        f = open(
            f"C:\\Users\\{os.getlogin()}\\Desktop\\Report_Full_Test.txt", "w")
        try:
            day = date.today()

            currentDate = day.strftime("%B %d, %Y")

            currentTime = datetime.now()

            currentTime = currentTime.strftime("%H:%M:%S")
        except Exception as e:
            print(e)

        f.write(main_line_separator)

        f.write("\n\nAdvanced System Monitor Report\n\n")

        f.write(main_line_separator)

        f.write(f"\n\nTime: {currentDate} | {currentTime}\n\n")

        f.write(main_line_separator)

        f.write("\n\nVersion: 1.0.0.0\n\n")

        f.write(main_line_separator)

        # Write base info if selected
        if mobo_info[2] == "True":
            f.write(f"\n\nMOTHERBOARD\n\n")
            f.write(f"{main_line_separator}\n\n")
            uname = platform.uname()
            w = wmi.WMI()
            sysinf = w.Win32_ComputerSystem()[0]
            windll = ctypes.windll.kernel32
            cpu_name_raw = cpuinfo.get_cpu_info()['brand_raw']
            gpus = GPUtil.getGPUs()
            for gpu in gpus:
                gpu_id = gpu.id
                gpu_name = gpu.name
                gpu_total_memory = f"{gpu.memoryTotal}MB"
                gpu_uuid = gpu.uuid
            device = win32api.EnumDisplayDevices()
            settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
            rammem = psutil.virtual_memory()
            swapmemory = psutil.swap_memory()
            disk = wmi.WMI()
            counter = []
            i = 0

            if not counter:
                for item in disk.Win32_PhysicalMedia():
                    counter.append(i)
                    i += 1
            else:
                pass

            partition = psutil.disk_partitions()
            total_space = 0
            free_space = 0
            used_space = 0
            windows_path = ""
            mounts = ""
            partitions_with_storage_list = []

            for part in partition:
                mounts += f"{part.mountpoint}, "
                try:
                    partition_usage = psutil.disk_usage(part.mountpoint)
                except Exception as e:
                    print(e)

                if path.exists(f'{part.mountpoint}Windows'):
                    windows_path += part.mountpoint

                mount = part.mountpoint
                sp = partition_usage.total

                partitions_with_storage_list.append((mount, sp))

                total_space += partition_usage.total
                free_space += partition_usage.free
                used_space += partition_usage.used

            total_space_in_gb = get_size(total_space)
            total_free_in_gb = get_size(free_space)
            total_used_in_gb = get_size(used_space)

            f.write(f"{line_separator} OS {line_separator}\n\n")
            f.write(f"System: {uname.system}\n")
            f.write(f"Node name: {uname.node}\n")
            f.write(f"Release: {uname.release}\n")
            f.write(f"Version: {uname.version}\n")
            f.write(f"Machine: {uname.machine}\n")
            f.write(f"Processor: {uname.processor}\n")
            f.write(f"Manufacturer: {sysinf.Manufacturer}\n")
            f.write(f"Model: {sysinf.Model}\n")
            f.write(
                f"Language Pack: {locale.windows_locale[ windll.GetUserDefaultUILanguage() ]}\n\n")

            f.write(f"{line_separator} CPU {line_separator}\n\n")
            f.write(f"CPU Name: {cpu_name_raw}\n")
            f.write(f"Physical Cores: {psutil.cpu_count(logical=False)}\n")
            f.write(f"Total Cores: {psutil.cpu_count(logical=True)}\n\n")

            f.write(f"{line_separator} GPU {line_separator}\n\n")
            f.write(f"ID: {gpu_id}\n")
            f.write(f"Name: {gpu_name}\n")
            f.write(f"Total Memory: {gpu_total_memory}")
            f.write(
                f"Active Resolution: {GetSystemMetrics(0)}x{GetSystemMetrics(1)}\n")

            for varName in ['DisplayFrequency']:
                f.write(f"Refresh Rate: {getattr(settings, varName)}Hz\n")

            f.write(f"UUID: {gpu_uuid}\n\n")

            f.write(f"{line_separator} MEMORY {line_separator}\n\n")
            f.write(f"-- RAM --\n")
            f.write(f"Total Size: {get_size(rammem.total)}\n\n")
            f.write("-- SWAP --\n")
            f.write(f"Total Size: {get_size(swapmemory.total)}\n\n")

            f.write(f"{line_separator} DISK {line_separator}\n\n")
            f.write(f"Number of drives: {len(counter)}\n")
            f.write(f"Mountpoints: {mounts}\n")
            f.write(f"Windows installed on partition: {windows_path}\n")
            f.write(f"Total Space (Combined): {total_space_in_gb}\n")
            f.write(
                f"Used Space (Combined): {total_used_in_gb} ({((used_space / total_space)*100):.2f}%)\n")
            f.write(
                f"Free Space (Combined): {total_free_in_gb} ({((free_space / total_space)*100):.2f}%)\n\n")

            f.write(main_line_separator)
        else:
            pass

        # Write cpu if selected

        if rec_cpu[2] == "True":
            f.write(f"\n\nCPU INFO\n\n")
            f.write(f"{main_line_separator}\n\n")
            f.write(f"{line_separator} Usage {line_separator}\n\n")
            try:
                f.write(f"Usage (last): {cpuPerc}%\n")
                f.write(f"Max Usage: {max(cpu_max_usage_during_test)}%\n\n")
            except Exception as e:
                print(e)
            f.write("PER CORE\n")
            # Usage per core
            try:
                for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
                    f.write(
                        f"Core #{i+1} (last): {percentage}%\n")

            except Exception as e:
                print(e)
            # Temperature
            f.write(f"\n{line_separator} Temperature {line_separator}\n\n")
            try:
                f.write(
                    f"Temperature (last): {temp_last:.3f}°C\n")
                f.write(
                    f"Max Temperature: {max(cpu_max_temp_during_test):.3f}°C\n")
            except Exception as e:
                print(e)
            # Voltage
            f.write(f"\n{line_separator} Voltage {line_separator}\n\n")
            try:
                w = wmi.WMI(namespace=r"root/OpenHardwareMonitor")
                volt_info = w.Sensor()
                for sensor in volt_info:
                    if sensor.SensorType == u"Voltage":
                        if sensor.Name == u"Voltage #1":
                            f.write(f"Voltage (last): {sensor.Value:.3f}V\n")
                            break
            except Exception as e:
                print(e)
            # Frequency
            f.write(f"\n{line_separator} Frequency {line_separator}\n\n")
            try:
                f.write(f"Frequency (last): {clock_last:.2f}Mhz\n")
                f.write(f"Max Frequency: {clock_max:.2f}Mhz\n")
            except Exception as e:
                print(e)
            # Power
            f.write(f"\n{line_separator} Power Usage {line_separator}\n\n")
            try:
                f.write(f"Power Usage (last): {power_last:.3f} W\n")
                f.write(
                    f"Max Power Usage: {max(cpu_max_power_during_test):.3f} W\n\n")
            except Exception as e:
                print(e)
            f.write(main_line_separator)
        else:
            pass

        # Write gpu if selected

        if rec_gpu[2] == "True":
            f.write(f"\n\nGPU INFO\n\n")
            f.write(f"{main_line_separator}\n\n")
            try:
                gf = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
                gpu_fans = gf.Sensor()
                for sensor in gpu_fans:
                    if sensor.SensorType == u"Fan":
                        if sensor.Name == u"GPU":
                            fan_value = sensor.Value
                            fan_value_max = sensor.Max
                    if sensor.SensorType == u"Control":
                        if sensor.Name == u"GPU Fan":
                            fan_perc = sensor.Value
                            fan_perc_max = sensor.Max
            except Exception as e:
                print(e)

            try:
                m = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
                memory_clock = m.Sensor()
                for sensor in memory_clock:
                    if sensor.SensorType == u"Clock":
                        if sensor.Name == u"GPU Memory":
                            memory_clk = sensor.Value
                            memory_clk_max = sensor.Max
                        if sensor.Name == u"GPU Shader":
                            shader_clk = sensor.Value
                            shader_clk_max = sensor.Max
                        if sensor.Name == u"GPU Core":
                            core_clk = sensor.Value
                            core_clk_max = sensor.Max
            except Exception as e:
                print(e)

            # Usage
            f.write(f"{line_separator} Usage {line_separator}\n\n")
            try:
                f.write(f"Usage (last): {float(gpu_load):.2f}%\n")
                f.write(
                    f"Max Usage: {float(max(gpu_max_usage_during_test)):.2f}%\n")
            except Exception as e:
                print(e)

            # Memory
            f.write(f"\n{line_separator} VRAM {line_separator}\n\n")
            try:
                f.write(
                    f"Total Memory: {float(gpu_total_memory_test):.2f}GB\n")
                f.write(f"Used Memory: {float(gpu_used_memory):.2f}GB\n")
                f.write(
                    f"Percentage used: {((float(gpu_used_memory) / float(gpu_total_memory_test)) * 100):.2f}%\n")
            except Exception as e:
                print(e)
            # Temperature
            f.write(f"\n{line_separator} Temperature {line_separator}\n\n")
            try:
                f.write(f"Temperature (last): {gpu_temperature}°C\n")
                f.write(
                    f"Max Temperature: {max(gpu_max_temp_during_test)}°C\n")
            except Exception as e:
                print(e)
            # Fans
            f.write(f"\n{line_separator} Fans {line_separator}\n\n")
            try:
                f.write(f"Fan speed (last): {fan_value}RPM | {fan_perc}%\n")
                f.write(
                    f"Max Fan Speed: {fan_value_max}RPM | {fan_perc_max}%\n")
            except Exception as e:
                print(e)
            # Clocks
            f.write(f"\n{line_separator} Clocks {line_separator}\n\n")
            try:
                f.write(f"Core Clock: {core_clk:.2f}Mhz\n")
                f.write(f"Max Core Clock: {core_clk_max:.2f}Mhz\n\n")
                f.write(f"Shader Clock: {shader_clk:.2f}Mhz\n")
                f.write(f"Max Shader Clock: {shader_clk_max:.2f}Mhz\n\n")
                f.write(f"Memory Clock: {memory_clk:.2f}Mhz\n")
                f.write(f"Max Memory Clock: {memory_clk_max:.2f}Mhz\n\n")
            except Exception as e:
                print(e)
            f.write(main_line_separator)
        else:
            pass

        # Write ram if selected
        if rec_ram[2] == "True":
            f.write(f"\n\nRAM INFO\n\n")
            f.write(f"{main_line_separator}\n\n")
            f.write(f"{line_separator} RAM Usage {line_separator}\n\n")

            try:
                f.write(f"Total Memory: {get_size(vmem_total)}\n")
                f.write(
                    f"Used Memory (last): {get_size(vmem_used)} ({((vmem_used / vmem_total)*100):.2f}%)\n")
                f.write(f"Free Memory (last): {get_size(vmem_free)}\n")
                f.write(
                    f"Max RAM Usage: {get_size(max(ram_max_usage_during_test))} ({((max(ram_max_usage_during_test) / vmem_total)*100):.2f}%)\n")
            except Exception as e:
                print(e)

            f.write(
                f"\n{line_separator} SWAP Memory Usage {line_separator}\n\n")

            try:
                f.write(f"Total SWAP Memory: {get_size(sv_total)}\n")
                f.write(
                    f"Used SWAP Memory (last): {get_size(sv_used)} ({((sv_used / sv_total)*100):.2f}%)\n")
                f.write(f"Free SWAP Memory (last): {get_size(sv_free)}\n")
                f.write(
                    f"Max SWAP Usage: {get_size(max(swap_max_usage_during_test))} ({((max(swap_max_usage_during_test) / sv_total)*100):.2f}%)\n\n")
            except Exception as e:
                print(e)

            f.write(main_line_separator)
        else:
            pass

        # Write fans if selected
        if rec_fans[2] == "True":
            f.write(f"\n\nFANS INFO\n\n")
            f.write(f"{main_line_separator}\n\n")
            try:
                fan = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
                fan_info = fan.Sensor()
                for sensor in fan_info:
                    if sensor.SensorType == u"Fan":
                        f.write(
                            f"{sensor.Name} (last): {sensor.Value:.2f} RPM\n")
                        f.write(
                            f"{sensor.Name} (Max): {sensor.Max:.2f} RPM\n\n")
                    else:
                        pass
            except Exception as e:
                print(e)

        f.close()
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()


# WRITING STATISTICS TO A FILE - WRITE ONLY #
try:
    def save_write_only():
        global max_cpu_usg
        global max_gpu_usg

        main_line_separator = "-"*80
        line_separator = "-"*10

        with open("Code\Config\switches.txt", "r") as file:
            for line in file:
                if "mobo_info" in line:
                    mobo_info = line.split()
                if "record_cpu" in line:
                    rec_cpu = line.split()
                if "record_gpu" in line:
                    rec_gpu = line.split()
                if "record_ram" in line:
                    rec_ram = line.split()
                if "record_fans" in line:
                    rec_fans = line.split()

        f = open(
            f"C:\\Users\\{os.getlogin()}\\Desktop\\Report_Write_Only.txt", "w")

        try:
            day = date.today()

            currentDate = day.strftime("%B %d, %Y")

            currentTime = datetime.now()

            currentTime = currentTime.strftime("%H:%M:%S")
        except Exception as e:
            print(e)

        f.write(main_line_separator)

        f.write("\n\nAdvanced System Monitor Report\n\n")

        f.write(main_line_separator)

        f.write(f"\n\nTime: {currentDate} | {currentTime}\n\n")

        f.write(main_line_separator)

        f.write("\n\nVersion: 1.0.0.0\n\n")

        f.write(main_line_separator)

        # Write base info if selected
        if mobo_info[2] == "True":
            f.write(f"\n\nMOTHERBOARD\n\n")
            f.write(f"{main_line_separator}\n\n")
            uname = platform.uname()
            w = wmi.WMI()
            sysinf = w.Win32_ComputerSystem()[0]
            windll = ctypes.windll.kernel32
            cpu_name_raw = cpuinfo.get_cpu_info()['brand_raw']
            gpus = GPUtil.getGPUs()
            for gpu in gpus:
                gpu_id = gpu.id
                gpu_name = gpu.name
                gpu_total_memory = f"{gpu.memoryTotal}MB"
                gpu_uuid = gpu.uuid
            device = win32api.EnumDisplayDevices()
            settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
            rammem = psutil.virtual_memory()
            swapmemory = psutil.swap_memory()
            disk = wmi.WMI()
            counter = []
            i = 0

            if not counter:
                for item in disk.Win32_PhysicalMedia():
                    counter.append(i)
                    i += 1
            else:
                pass

            partition = psutil.disk_partitions()
            total_space = 0
            free_space = 0
            used_space = 0
            windows_path = ""
            mounts = ""
            partitions_with_storage_list = []

            for part in partition:
                mounts += f"{part.mountpoint}, "
                try:
                    partition_usage = psutil.disk_usage(part.mountpoint)
                except Exception as e:
                    print(e)

                if path.exists(f'{part.mountpoint}Windows'):
                    windows_path += part.mountpoint

                mount = part.mountpoint
                sp = partition_usage.total

                partitions_with_storage_list.append((mount, sp))

                total_space += partition_usage.total
                free_space += partition_usage.free
                used_space += partition_usage.used

            total_space_in_gb = get_size(total_space)
            total_free_in_gb = get_size(free_space)
            total_used_in_gb = get_size(used_space)

            f.write(f"{line_separator} OS {line_separator}\n\n")
            f.write(f"System: {uname.system}\n")
            f.write(f"Node name: {uname.node}\n")
            f.write(f"Release: {uname.release}\n")
            f.write(f"Version: {uname.version}\n")
            f.write(f"Machine: {uname.machine}\n")
            f.write(f"Processor: {uname.processor}\n")
            f.write(f"Manufacturer: {sysinf.Manufacturer}\n")
            f.write(f"Model: {sysinf.Model}\n")
            f.write(
                f"Language Pack: {locale.windows_locale[ windll.GetUserDefaultUILanguage() ]}\n\n")

            f.write(f"{line_separator} CPU {line_separator}\n\n")
            f.write(f"CPU Name: {cpu_name_raw}\n")
            f.write(f"Physical Cores: {psutil.cpu_count(logical=False)}\n")
            f.write(f"Total Cores: {psutil.cpu_count(logical=True)}\n\n")

            f.write(f"{line_separator} GPU {line_separator}\n\n")
            f.write(f"ID: {gpu_id}\n")
            f.write(f"Name: {gpu_name}\n")
            f.write(f"Total Memory: {gpu_total_memory}")
            f.write(
                f"Active Resolution: {GetSystemMetrics(0)}x{GetSystemMetrics(1)}\n")

            for varName in ['DisplayFrequency']:
                f.write(f"Refresh Rate: {getattr(settings, varName)}Hz\n")

            f.write(f"UUID: {gpu_uuid}\n\n")

            f.write(f"{line_separator} MEMORY {line_separator}\n\n")
            f.write(f"-- RAM --\n")
            f.write(f"Total Size: {get_size(rammem.total)}\n\n")
            f.write("-- SWAP --\n")
            f.write(f"Total Size: {get_size(swapmemory.total)}\n\n")

            f.write(f"{line_separator} DISK {line_separator}\n\n")
            f.write(f"Number of drives: {len(counter)}\n")
            f.write(f"Mountpoints: {mounts}\n")
            f.write(f"Windows installed on partition: {windows_path}\n")
            f.write(f"Total Space (Combined): {total_space_in_gb}\n")
            f.write(
                f"Used Space (Combined): {total_used_in_gb} ({((used_space / total_space)*100):.2f}%)\n")
            f.write(
                f"Free Space (Combined): {total_free_in_gb} ({((free_space / total_space)*100):.2f}%)\n\n")

            f.write(main_line_separator)
        else:
            pass

        # Write cpu if selected

        if rec_cpu[2] == "True":
            f.write(f"\n\nCPU INFO\n\n")
            f.write(f"{main_line_separator}\n\n")
            cpu_perc = psutil.cpu_percent()
            # Usage

            if cpu_perc not in cpu_max_usage_during_test:
                if cpu_perc > max_cpu_usg:
                    cpu_max_usage_during_test.append(cpu_perc)
                    max_cpu_usg = cpu_perc

            f.write(f"{line_separator} Usage {line_separator}\n\n")
            try:
                f.write(f"Usage (last): {cpu_perc}%\n")
                f.write(f"Max Usage: {max(cpu_max_usage_during_test)}%\n\n")
            except Exception as e:
                print(e)
            f.write("PER CORE\n")
            # Usage per core
            try:
                for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
                    f.write(
                        f"Core #{i+1} (last): {percentage}%\n")

            except Exception as e:
                print(e)
            # Temperature
            f.write(f"\n{line_separator} Temperature {line_separator}\n\n")
            try:
                w = wmi.WMI(namespace=r"root/OpenHardwareMonitor")
                temp_info = w.Sensor()
                for sensor in temp_info:
                    if sensor.SensorType == u"Temperature":
                        if sensor.Name == u"CPU Package":
                            if sensor.Value not in cpu_max_temp_during_test:
                                cpu_max_temp_during_test.append(sensor.Value)
                            else:
                                pass

                            f.write(
                                f"Temperature (last): {sensor.Value:.3f}°C\n")
                            f.write(
                                f"Max Temperature: {max(cpu_max_temp_during_test):.3f}°C\n")
            except Exception as e:
                print(e)

            # Voltage
            f.write(f"\n{line_separator} Voltage {line_separator}\n\n")
            try:
                w = wmi.WMI(namespace=r"root/OpenHardwareMonitor")
                volt_info = w.Sensor()
                for sensor in volt_info:
                    if sensor.SensorType == u"Voltage":
                        if sensor.Name == u"Voltage #1":
                            f.write(f"Voltage (last): {sensor.Value:.3f}V\n")
                            break
            except Exception as e:
                print(e)
            # Frequency
            f.write(f"\n{line_separator} Frequency {line_separator}\n\n")
            try:
                w = wmi.WMI(namespace=r"root/OpenHardwareMonitor")
                freq_info = w.Sensor()
                for sensor in freq_info:
                    if sensor.SensorType == u"Clock":
                        if sensor.Name == u"CPU Core #1":
                            f.write(
                                f"Frequency (last): {sensor.Value:.2f}Mhz\n")
                            f.write(f"Max Frequency: {sensor.Max:.2f}Mhz\n")
            except Exception as e:
                print(e)

            # Power
            f.write(f"\n{line_separator} Power Usage {line_separator}\n\n")
            try:
                w = wmi.WMI(namespace=r"root/OpenHardwareMonitor")
                pwr_info = w.Sensor()
                for sensor in pwr_info:
                    if sensor.SensorType == u"Power":
                        if sensor.Name == u"CPU Package":
                            if sensor.Value not in cpu_max_power_during_test:
                                cpu_max_power_during_test.append(sensor.Value)
                            else:
                                pass
                            f.write(
                                f"Power Usage (last): {sensor.Value:.3f} W\n")
                            f.write(
                                f"Max Power Usage: {max(cpu_max_power_during_test):.3f} W\n\n")
            except Exception as e:
                print(e)
            f.write(main_line_separator)
        else:
            pass

        # Write gpu if selected

        if rec_gpu[2] == "True":
            f.write(f"\n\nGPU INFO\n\n")
            f.write(f"{main_line_separator}\n\n")
            devices = GPUtil.getGPUs()

            for gpu in devices:
                gpu_load = f"{gpu.load*100}"
                gpu_total_memory = f"{gpu.memoryTotal / 1000}"
                gpu_temperature = f"{gpu.temperature}"
                gpu_used_memory = f"{gpu.memoryUsed / 1000}"

            if gpu_load not in gpu_max_usage_during_test:
                gpu_max_usage_during_test.append(gpu_load)
            else:
                pass

            if gpu_temperature not in gpu_max_temp_during_test:
                gpu_max_temp_during_test.append(gpu_temperature)
            else:
                pass

            try:
                gf = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
                gpu_fans = gf.Sensor()
                for sensor in gpu_fans:
                    if sensor.SensorType == u"Fan":
                        if sensor.Name == u"GPU":
                            fan_value = sensor.Value
                            fan_value_max = sensor.Max
                    if sensor.SensorType == u"Control":
                        if sensor.Name == u"GPU Fan":
                            fan_perc = sensor.Value
                            fan_perc_max = sensor.Max
            except Exception as e:
                print(e)

            try:
                m = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
                memory_clock = m.Sensor()
                for sensor in memory_clock:
                    if sensor.SensorType == u"Clock":
                        if sensor.Name == u"GPU Memory":
                            memory_clk = sensor.Value
                            memory_clk_max = sensor.Max
                        if sensor.Name == u"GPU Shader":
                            shader_clk = sensor.Value
                            shader_clk_max = sensor.Max
                        if sensor.Name == u"GPU Core":
                            core_clk = sensor.Value
                            core_clk_max = sensor.Max
            except Exception as e:
                print(e)

            # Usage
            try:
                f.write(f"{line_separator} Usage {line_separator}\n\n")
                f.write(f"Usage (last): {float(gpu_load):.2f}%\n")
                f.write(
                    f"Max Usage: {float(max(gpu_max_usage_during_test)):.2f}%\n")
            except Exception as e:
                print(e)

            # Memory
            try:
                f.write(f"\n{line_separator} VRAM {line_separator}\n\n")
                f.write(f"Total Memory: {float(gpu_total_memory):.2f}GB\n")
                f.write(f"Used Memory: {float(gpu_used_memory):.2f}GB\n")
                f.write(
                    f"Percentage used: {((float(gpu_used_memory) / float(gpu_total_memory)) * 100):.2f}%\n")
            except Exception as e:
                print(e)
            # Temperature
            try:
                f.write(f"\n{line_separator} Temperature {line_separator}\n\n")
                f.write(f"Temperature (last): {gpu_temperature}°C\n")
                f.write(
                    f"Max Temperature: {max(gpu_max_temp_during_test)}°C\n")
            except Exception as e:
                print(e)
            # Fans
            try:
                f.write(f"\n{line_separator} Fans {line_separator}\n\n")
                f.write(f"Fan speed (last): {fan_value}RPM | {fan_perc}%\n")
                f.write(
                    f"Max Fan Speed: {fan_value_max}RPM | {fan_perc_max}%\n")
            except Exception as e:
                print(e)
            # Clocks
            try:
                f.write(f"\n{line_separator} Clocks {line_separator}\n\n")
                f.write(f"Core Clock: {core_clk:.2f}Mhz\n")
                f.write(f"Max Core Clock: {core_clk_max:.2f}Mhz\n\n")
                f.write(f"Shader Clock: {shader_clk:.2f}Mhz\n")
                f.write(f"Max Shader Clock: {shader_clk_max:.2f}Mhz\n\n")
                f.write(f"Memory Clock: {memory_clk:.2f}Mhz\n")
                f.write(f"Max Memory Clock: {memory_clk_max:.2f}Mhz\n\n")
            except Exception as e:
                print(e)
            f.write(main_line_separator)
        else:
            pass

        # Write ram if selected
        if rec_ram[2] == "True":
            f.write(f"\n\nRAM INFO\n\n")
            f.write(f"{main_line_separator}\n\n")
            vmem = psutil.virtual_memory()
            swapmem = psutil.swap_memory()

            if vmem.used not in ram_max_usage_during_test:
                ram_max_usage_during_test.append(vmem.used)
            else:
                pass

            if swapmem.used not in swap_max_usage_during_test:
                swap_max_usage_during_test.append(swapmem.used)
            else:
                pass

            f.write(f"{line_separator} RAM Usage {line_separator}\n\n")

            try:
                f.write(f"Total Memory: {get_size(vmem.total)}\n")
                f.write(
                    f"Used Memory (last): {get_size(vmem.used)} ({((vmem.used / vmem.total)*100):.2f}%)\n")
                f.write(f"Free Memory (last): {get_size(vmem.free)}\n")
                f.write(
                    f"Max RAM Usage: {get_size(max(ram_max_usage_during_test))} ({((max(ram_max_usage_during_test) / vmem.total)*100):.2f}%)\n")
            except Exception as e:
                print(e)

            f.write(
                f"\n{line_separator} SWAP Memory Usage {line_separator}\n\n")

            try:
                f.write(f"Total SWAP Memory: {get_size(swapmem.total)}\n")
                f.write(
                    f"Used SWAP Memory (last): {get_size(swapmem.used)} ({((swapmem.used / swapmem.total)*100):.2f}%)\n")
                f.write(f"Free SWAP Memory (last): {get_size(swapmem.free)}\n")
                f.write(
                    f"Max SWAP Usage: {get_size(max(swap_max_usage_during_test))} ({((max(swap_max_usage_during_test) / swapmem.total)*100):.2f}%)\n\n")
            except Exception as e:
                print(e)

            f.write(main_line_separator)
        else:
            pass

        # Write fans if selected
        if rec_fans[2] == "True":
            f.write(f"\n\nFANS INFO\n\n")
            f.write(f"{main_line_separator}\n\n")
            try:
                fan = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
                fan_info = fan.Sensor()
                for sensor in fan_info:
                    if sensor.SensorType == u"Fan":
                        f.write(
                            f"{sensor.Name} (last): {sensor.Value:.2f} RPM\n")
                    else:
                        pass
            except Exception as e:
                print(e)

        f.close()
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# Function to generate random fun facts about Advanced System Monitor

try:
    def fun_facts():
        global ff
        random_number = random.randint(1, 10)

        if random_number == 1:
            fun_fact.configure(
                text="This app has 5.2k lines of code and\n15k+ words in total.")
        elif random_number == 2:
            fun_fact.configure(
                text="Advanced System Monitor was written\nby only one developer.")
        elif random_number == 3:
            fun_fact.configure(
                text="Development of this app took 2 months,\nand its still being worked on.")
        elif random_number == 4:
            fun_fact.configure(
                text="Most of the app is improvised\nand unplanned.")
        elif random_number == 5:
            fun_fact.configure(
                text="Developer studied Python for a month\nbefore starting this project.")
        elif random_number == 6:
            fun_fact.configure(
                text="This app is developers first big project.")
        elif random_number == 7:
            fun_fact.configure(
                text="Point of this app is to be unlike any other\napp of this kind on the market.")
        elif random_number == 8:
            fun_fact.configure(
                text="AVS is open source and its code can be viewed\nby anybody if they are interested.")
        elif random_number == 9:
            fun_fact.configure(text="There are 20 fun facts in total.")
        elif random_number == 10:
            fun_fact.configure(
                text="There is a secret fun fact that appears\nonly in special conditions.")

        ff = root.after(7000, fun_facts)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# Mobo function grabs and displays wide range of data related to the system

try:
    def mobo():
        global main_frame

        try:
            motherboardButton.configure(bg=button_bg)
        except Exception as e:
            print(e)

        try:
            combined_test_frame.place_forget()
            root.after_cancel(rct)
        except Exception as e:
            print(e)

        try:
            homeButton.configure(bg=sidemenu_bg)
            root.after_cancel(time)
            root.after_cancel(ff)
            home_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            cpuButton.configure(bg=sidemenu_bg)
            root.after_cancel(ref)
            combined_test_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            gpuButton.configure(bg=sidemenu_bg)
            root.after_cancel(gpu_update)
            gpu_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            ramButton.configure(bg=sidemenu_bg)
            root.after_cancel(ram_ref)
            ram_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            hddButton.configure(bg=sidemenu_bg)
            root.after_cancel(drive_ref)
            drive_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            netButton.configure(bg=sidemenu_bg)
            root.after_cancel(net_ref)
            network_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            fanButton.configure(bg=sidemenu_bg)
            root.after_cancel(fan_ref)
            fans_frame.place_forget()
        except Exception as e:
            print(e)

        main_frame = tk.Frame(root, bg=canvas_bg)
        main_frame.place(relwidth=0.875, relheight=0.96,
                         relx=0.117, rely=0.021)

        loading = tk.Label(main_frame, bg=canvas_bg, fg=fg, font=(
            loading_font), width=100, height=50, text="Loading...")
        loading.pack()

        def declare_mobo():
            global sys_name
            root.after_cancel(dec_mobo)
            with tqdm(total=100) as bar:
                uname = platform.uname()

                os_info = tk.Frame(main_frame, bg=bg)
                os_info.place(relwidth=0.49, relheight=0.51, relx=0, rely=0)

                os_frame = tk.Frame(os_info, bg=bg)
                os_frame.place(relwidth=1, relheight=0.90, relx=0, rely=0.15)

                os_info_frame = tk.Frame(os_info, bg=bg)
                os_info_frame.place(relwidth=0.60, relheight=0.15,
                                    relx=0.02, rely=-0.01)

                os_info_label = tk.Label(os_info_frame, bg=bg, fg=fg, font=font,
                                         anchor=tk.W, width=100, height=100, text="SYSTEM INFORMATION")
                os_info_label.pack()

                uname = platform.uname()

                boot_time_timestamp = psutil.boot_time()
                bt = datetime.fromtimestamp(boot_time_timestamp)

                system = tk.Label(os_frame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                  width=100, height=1, pady=(1), text=f"System: {uname.system}")
                system.grid(row=0, column=0, padx=(10), pady=(5, 0))

                node = tk.Label(os_frame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                width=100, height=1, text=f"Node name: {uname.node}")
                node.grid(row=1, column=0, padx=(10))

                release = tk.Label(os_frame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                   width=100, height=1, text=f"Release: {uname.release}")
                release.grid(row=2, column=0, padx=(10))

                version = tk.Label(os_frame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                   width=100, height=1, text=f"Version: {uname.version}")
                version.grid(row=3, column=0, padx=(10))

                machine = tk.Label(os_frame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                   width=100, height=1, text=f"Machine: {uname.machine}")
                machine.grid(row=4, column=0, padx=(10))

                boot_time = tk.Label(os_frame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                     width=100, height=1, text=f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
                boot_time.grid(row=5, column=0, padx=(10))

                processor = tk.Label(os_frame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                     width=100, height=1, text=f"Processor: {uname.processor}")
                processor.grid(row=6, column=0, padx=(10))

                w = wmi.WMI()
                sysinf = w.Win32_ComputerSystem()[0]

                man = sysinf.Manufacturer
                model = sysinf.Model

                manufacturer = tk.Label(os_frame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                        width=100, height=1, text=f"Manufacturer: {man}")
                manufacturer.grid(row=7, column=0, padx=(10))

                model_name = tk.Label(os_frame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                      width=100, height=1, text=f"Model: {model}")
                model_name.grid(row=8, column=0, padx=(10))

                windll = ctypes.windll.kernel32

                language = tk.Label(os_frame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                    width=100, height=1, text=f"Language pack: {locale.windows_locale[ windll.GetUserDefaultUILanguage() ]}")
                language.grid(row=9, column=0, padx=(10))

                bar.update(20)

                cpuInfo = tk.Frame(main_frame, bg=bg)
                cpuInfo.place(relwidth=0.49, relheight=0.26,
                              relx=0.505, rely=0)

                procFrame = tk.Frame(cpuInfo, bg=bg)
                procFrame.place(relwidth=1, relheight=0.90, relx=0, rely=0.29)

                cpu_info_frame = tk.Frame(cpuInfo, bg=bg)
                cpu_info_frame.place(relwidth=0.50, relheight=0.15,
                                     relx=0.02, rely=0.04)

                cpu_info_label = tk.Label(cpu_info_frame, bg=bg, fg=fg, font=font,
                                          anchor=tk.W, width=100, height=10, text="CPU INFORMATION")
                cpu_info_label.pack()

                cpu_name_raw = cpuinfo.get_cpu_info()['brand_raw']

                cpu_name = tk.Label(procFrame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                    width=100, height=1, text=f"Name: {cpu_name_raw}")
                cpu_name.grid(row=0, column=0, padx=(10), pady=(5, 0))

                physical_cores = tk.Label(procFrame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                          width=100, height=1, text=f"No. Cores: {psutil.cpu_count(logical=False)}")
                physical_cores.grid(row=1, column=0, padx=(10))

                total_cores = tk.Label(procFrame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                       width=100, height=1, text=f"No. Threads: {psutil.cpu_count(logical=True)}")
                total_cores.grid(row=2, column=0, padx=(10))

                cpufreq = psutil.cpu_freq()

                base_freq = tk.Label(procFrame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                     width=100, height=1, text=f"Base Frequency: {cpufreq.current:.2f}Mhz")
                base_freq.grid(row=3, column=0, padx=(10))

                displayInfo = tk.Frame(main_frame, bg=bg)
                displayInfo.place(relwidth=0.49, relheight=0.355,
                                  relx=0.505, rely=0.28)

                displayFrame = tk.Frame(displayInfo, bg=bg)
                displayFrame.place(
                    relwidth=1, relheight=0.90, relx=0, rely=0.24)

                display_info_frame = tk.Frame(displayInfo, bg=bg)
                display_info_frame.place(
                    relwidth=0.80, relheight=0.15, relx=0.02, rely=0.03)

                bar.update(20)

                display_info_label = tk.Label(display_info_frame, bg=bg, fg=fg, font=font,
                                              anchor=tk.W, width=100, height=10, text="DISPLAY ADAPTER INFORMATION")
                display_info_label.pack()

                gpus = GPUtil.getGPUs()
                for gpu in gpus:
                    gpu_id = gpu.id
                    gpu_name = gpu.name
                    gpu_total_memory = f"{gpu.memoryTotal}MB"
                    gpu_uuid = gpu.uuid

                gpu_number = tk.Label(displayFrame, bg=bg, fg=fg, font=font,
                                      anchor=lbl_anchor, width=100, height=1, text=f"ID: {gpu_id}")
                gpu_number.grid(row=0, column=0, padx=(10), pady=(5, 0))

                gpu_nam = tk.Label(displayFrame, bg=bg, fg=fg, font=font,
                                   anchor=lbl_anchor, width=100, height=1, text=f"Name: {gpu_name}")
                gpu_nam.grid(row=1, column=0, padx=(10))

                gpu_total_mem = tk.Label(displayFrame, bg=bg, fg=fg, font=font, anchor=lbl_anchor,
                                         width=100, height=1, text=f"Total Memory: {gpu_total_memory}")
                gpu_total_mem.grid(row=2, column=0, padx=(10))

                resolution = tk.Label(displayFrame, bg=bg, fg=fg, font=font,
                                      anchor=lbl_anchor, width=100, height=1, text=f"Active Resolution: {GetSystemMetrics(0)}x{GetSystemMetrics(1)}")
                resolution.grid(row=3, column=0, padx=(10))

                device = win32api.EnumDisplayDevices()
                settings = win32api.EnumDisplaySettings(device.DeviceName, -1)

                for varName in ['DisplayFrequency']:
                    refreshRate = tk.Label(displayFrame, bg=bg, fg=fg, font=font,
                                           anchor=lbl_anchor, width=100, height=1, text=f"Refresh Rate: {getattr(settings, varName)}Hz")
                    refreshRate.grid(row=4, column=0, padx=(10))
                gpu_uid = tk.Label(displayFrame, bg=bg, fg=fg, font=font,
                                   anchor=lbl_anchor, width=100, height=1, text=f"UUID: {gpu_uuid}")
                gpu_uid.grid(row=5, column=0, padx=(10))

                bar.update(20)

                # Memory information

                memory_info = tk.Frame(main_frame, bg=bg)
                memory_info.place(relwidth=0.49, relheight=0.35,
                                  relx=0.505, rely=0.655)

                memory_info_frame = tk.Frame(memory_info, bg=bg)
                memory_info_frame.place(
                    relwidth=0.45, relheight=0.15, relx=0.025, rely=0.03)

                memory_info_label = tk.Label(memory_info_frame, bg=bg, fg=fg, font=font,
                                             anchor=tk.CENTER, width=100, height=100, text="MEMORY INFORMATION")
                memory_info_label.pack()

                memory = tk.Frame(memory_info, bg=bg)
                memory.place(relwidth=0.5, relheight=0.75, relx=0, rely=0.27)

                svmem = psutil.virtual_memory()

                memory_label = tk.Label(memory, bg=bg, fg=fg, font=font,
                                        anchor=tk.W, width=100, height=1, text=f"PHYSICAL MEMORY")
                memory_label.grid(row=0, column=0, padx=(12), pady=(2))

                total_memory = tk.Label(memory, bg=bg, fg=fg, font=font,
                                        anchor=tk.W, width=100, height=1, text=f"Total size: {get_size(svmem.total)}")
                total_memory.grid(row=1, column=0, padx=(12))

                used_memory = tk.Label(memory, bg=bg, fg=fg, font=font,
                                       anchor=tk.W, width=100, height=1, text=f"Used: {get_size(svmem.used)}")
                used_memory.grid(row=2, column=0, padx=(12))

                free_memory = tk.Label(memory, bg=bg, fg=fg, font=font,
                                       anchor=tk.W, width=100, height=1, text=f"Free: {get_size(svmem.free)}")
                free_memory.grid(row=3, column=0, padx=(12))

                memory_perc = tk.Label(memory, bg=bg, fg=fg, font=font,
                                       anchor=tk.W, width=100, height=1, text=f"Percentage: {svmem.percent}%")
                memory_perc.grid(row=4, column=0, padx=(12))

                separator = tk.Frame(memory_info, bg="white")
                separator.place(relwidth=0.004, relheight=0.61,
                                relx=0.5, rely=0.27)

                swap_mem = tk.Frame(memory_info, bg=bg)
                swap_mem.place(relwidth=0.5, relheight=0.75,
                               relx=0.58, rely=0.27)

                swap = psutil.swap_memory()

                swap_label = tk.Label(swap_mem, bg=bg, fg=fg, font=font,
                                      anchor=tk.W, width=100, height=1, text=f"SWAP MEMORY")
                swap_label.grid(row=0, column=0, padx=(12), pady=(2))

                swap_total = tk.Label(swap_mem, bg=bg, fg=fg, font=font,
                                      anchor=tk.W, width=100, height=1, text=f"Total size: {get_size(swap.total)}")
                swap_total.grid(row=1, column=0, padx=(12))

                swap_used = tk.Label(swap_mem, bg=bg, fg=fg, font=font,
                                     anchor=tk.W, width=100, height=1, text=f"Used: {get_size(swap.used)}")
                swap_used.grid(row=2, column=0, padx=(12))

                swap_free = tk.Label(swap_mem, bg=bg, fg=fg, font=font,
                                     anchor=tk.W, width=100, height=1, text=f"Free: {get_size(swap.free)}")
                swap_free.grid(row=3, column=0, padx=(12))

                swap_perc = tk.Label(swap_mem, bg=bg, fg=fg, font=font,
                                     anchor=tk.W, width=100, height=1, text=f"Percentage: {swap.percent}%")
                swap_perc.grid(row=4, column=0, padx=(12))

                bar.update(20)

                # Disk information

                disk_info = tk.Frame(main_frame, bg=bg)
                disk_info.place(relwidth=0.49, relheight=0.47,
                                relx=0, rely=0.53)

                disk_info_frame = tk.Frame(disk_info, bg=bg)
                disk_info_frame.place(
                    relwidth=0.37, relheight=0.15, relx=0.02, rely=0)

                disk_info_label = tk.Label(disk_info_frame, bg=bg, fg=fg, font=font,
                                           anchor=tk.CENTER, width=100, height=10, text="DISK INFORMATION")
                disk_info_label.pack()

                partitions = tk.Frame(disk_info, bg=bg)
                partitions.place(relwidth=1, relheight=0.80, relx=0, rely=0.17)

                d = wmi.WMI()
                counter = 0

                for item in d.Win32_PhysicalMedia():
                    counter += 1

                partition = psutil.disk_partitions()
                total_space = 0
                free_space = 0
                used_space = 0
                windows_path = ""
                mounts = ""
                list_of_parititons_with_storage = []

                for part in partition:
                    mounts += f"{part.mountpoint}, "
                    try:
                        partition_usage = psutil.disk_usage(part.mountpoint)
                    except Exception as e:
                        print(e)

                    if path.exists(f'{part.mountpoint}Windows'):
                        windows_path += part.mountpoint

                    mount = part.mountpoint
                    sp = partition_usage.total

                    list_of_parititons_with_storage.append((mount, sp))

                    total_space += partition_usage.total
                    free_space += partition_usage.free
                    used_space += partition_usage.used

                total_space_in_gb = get_size(total_space)
                total_free_in_gb = get_size(free_space)
                total_used_in_gb = get_size(used_space)

                number_of_drives = tk.Label(partitions, bg=bg, fg=fg, font=font,
                                            anchor=tk.W, width=100, height=1, text=f"Number of drives: {counter}")
                number_of_drives.grid(row=0, column=0, padx=(9), pady=(2, 0))

                mount_points = tk.Label(partitions, bg=bg, fg=fg, font=font,
                                        anchor=tk.W, width=100, height=1, text=f"Mountpoints: {mounts}")
                mount_points.grid(row=1, column=0, padx=(9))

                windows_installed_on = tk.Label(partitions, bg=bg, fg=fg, font=font,
                                                anchor=tk.W, width=100, height=1, text=f"Windows installed on partition: {windows_path}")
                windows_installed_on.grid(row=2, column=0, padx=(9))

                total_drive_space = tk.Label(partitions, bg=bg, fg=fg, font=font,
                                             anchor=tk.W, width=100, height=1, text=f"Total Space (Combined): {total_space_in_gb}")
                total_drive_space.grid(row=3, column=0, padx=(9))

                total_free_space = tk.Label(partitions, bg=bg, fg=fg, font=font,
                                            anchor=tk.W, width=100, height=1, text=f"Free Space (Combined): {total_free_in_gb}")
                total_free_space.grid(row=4, column=0, padx=(9))

                free_perc = (free_space / total_space) * 100

                total_free_percentage = tk.Label(partitions, bg=bg, fg=fg, font=font,
                                                 anchor=tk.W, width=100, height=1, text=f"Free Space (Percentage): {free_perc:.2f}%")
                total_free_percentage.grid(row=5, column=0, padx=(9))

                total_used_space = tk.Label(partitions, bg=bg, fg=fg, font=font,
                                            anchor=tk.W, width=100, height=1, text=f"Used Space (Combined): {total_used_in_gb}")
                total_used_space.grid(row=6, column=0, padx=(9))

                used_perc = (used_space / total_space) * 100

                total_used_percentage = tk.Label(partitions, bg=bg, fg=fg, font=font,
                                                 anchor=tk.W, width=100, height=1, text=f"Used Space (Percentage): {used_perc:.2f}%")
                total_used_percentage.grid(row=7, column=0, padx=(9))

                bar.update(20)

                loading.pack_forget()

        dec_mobo = root.after(15, declare_mobo)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# CPU function grabs various information about your CPU and displays it

try:
    def cpu():
        global cpu_frame
        global max_record
        # Hide existing frames from other functions

        try:
            cpuButton.configure(bg=button_bg)
        except Exception as e:
            print(e)

        try:
            combined_test_frame.place_forget()
            root.after_cancel(rct)
        except Exception as e:
            print(e)

        try:
            homeButton.configure(bg=sidemenu_bg)
            root.after_cancel(time)
            root.after_cancel(ff)
            home_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            motherboardButton.configure(bg=sidemenu_bg)
            main_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            gpuButton.configure(bg=sidemenu_bg)
            gpu_frame.place_forget()
            root.after_cancel(gpu_update)
        except Exception as e:
            print(e)

        try:
            ramButton.configure(bg=sidemenu_bg)
            root.after_cancel(ram_ref)
            ram_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            hddButton.configure(bg=sidemenu_bg)
            root.after_cancel(drive_ref)
            drive_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            netButton.configure(bg=sidemenu_bg)
            root.after_cancel(net_ref)
            network_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            fanButton.configure(bg=sidemenu_bg)
            root.after_cancel(fan_ref)
            fans_frame.place_forget()
        except Exception as e:
            print(e)

        # Setup frames and lables

        cpu_frame = tk.Frame(root, bg=canvas_bg)
        cpu_frame.place(relwidth=0.875, relheight=0.96, relx=0.117, rely=0.021)

        loading = tk.Label(cpu_frame, bg=canvas_bg, fg=fg, font=(
            loading_font), width=100, height=50, text="Loading...")
        loading.pack()

        def declare_cpu():
            global totalUsageMeasure
            global coreUsage
            global helpFrame
            global pos
            global total_usage_bar
            global total_usage_num
            global usage_frame
            global package_temp_bar
            global package_temp_value_label
            global voltage_value_label
            global voltage_bar
            global frequency_bar
            global frequency_value_label
            global power_value_label
            global power_usage_bar
            global cores
            global max_temp
            global max_freq
            global max_usage
            global max_power
            global sheet

            root.after_cancel(dec_cpu)

            with tqdm(total=100) as bar:

                # Measure usage

                usage_frame = tk.Frame(cpu_frame, bg=bg)
                usage_frame.place(
                    relwidth=0.49, relheight=0.19, relx=0, rely=0)

                usage_label_frame = tk.Frame(usage_frame, bg=bg)
                usage_label_frame.place(
                    relwidth=0.15, relheight=0.15, relx=0.01, rely=0.08)

                usage_label = tk.Label(usage_label_frame, bg=bg, fg=fg, width=100,
                                       height=1, anchor=tk.CENTER, font=font, text="USAGE")
                usage_label.pack()

                total_usage_frame = tk.Frame(usage_frame, bg=bg)
                total_usage_frame.place(
                    relwidth=1, relheight=0.90, relx=0.02, rely=0.426)

                total_usage = tk.Label(total_usage_frame, bg=bg, fg=fg, anchor=tk.W,
                                       font=font, width=100, height=1, text="Total usage")
                total_usage.pack()

                total_usage_bar = tk.Label(total_usage_frame, bg=bg, fg=fg, anchor=tk.W,
                                           font=font, width=100, height=1, text="|")
                total_usage_bar.pack()

                total_usage_num_frame = tk.Frame(usage_frame, bg=bg)
                total_usage_num_frame.place(
                    relwidth=0.25, relheight=0.15, relx=0.72, rely=0.465)

                total_usage_num = tk.Label(total_usage_num_frame, bg=bg, fg=fg,
                                           font=font, anchor=tk.E, width=15, height=15, text="0%")
                total_usage_num.pack()

                bar.update(12.5)

                # Measure usage per core

                usage_per_core = tk.Frame(cpu_frame, bg=bg)
                usage_per_core.place(
                    relwidth=0.49, relheight=0.61, relx=0, rely=0.21)

                per_core_usage = tk.Frame(usage_per_core, bg=bg)
                per_core_usage.place(relwidth=0.35, relheight=0.07,
                                     relx=0.02, rely=0.02)

                per_core_usage_label = tk.Label(
                    per_core_usage, bg=bg, fg=fg, font=font, anchor=tk.W, width=100, height=10, text="USAGE PER CORE")
                per_core_usage_label.pack()

                cores = tk.Frame(usage_per_core, bg=bg)
                cores.place(relwidth=1, relheight=0.83, relx=0, rely=0.13)

                bar.update(12.5)

                # Measure temperature

                temp_frame = tk.Frame(cpu_frame, bg=bg)
                temp_frame.place(relwidth=0.49, relheight=0.19,
                                 relx=0.505, rely=0)

                temperature_frame = tk.Frame(temp_frame, bg=bg)
                temperature_frame.place(
                    relwidth=0.40, relheight=0.15, relx=-0.04, rely=0.09)

                temp_label = tk.Label(temperature_frame, bg=bg, fg=fg, width=100,
                                      height=100, anchor=tk.CENTER, font=font, text="TEMPERATURE")
                temp_label.pack()

                package_temp = tk.Frame(temp_frame, bg=bg)
                package_temp.place(relwidth=0.963, relheight=0.50,
                                   relx=0.018, rely=0.426)

                package_temp_label = tk.Label(package_temp, bg=bg, fg=fg, font=font,
                                              anchor=tk.W, width=100, height=1, text="Package Temperature")
                package_temp_label.pack()

                package_temp_bar = tk.Label(
                    package_temp, bg=bg, fg=fg, font=font, anchor=tk.W, width=200, height=1, text="|")
                package_temp_bar.pack()

                package_temp_value = tk.Frame(temp_frame, bg="white")
                package_temp_value.place(
                    relwidth=0.15, relheight=0.25, relx=0.83, rely=0.40)

                package_temp_value_label = tk.Label(
                    package_temp_value, bg=bg, fg=fg, font=font, anchor=tk.E, width=15, height=15, text="0°C")
                package_temp_value_label.pack()

                bar.update(12.5)

                # Measure voltage

                cpu_voltage = tk.Frame(cpu_frame, bg=bg)
                cpu_voltage.place(relwidth=0.49, relheight=0.19,
                                  relx=0.505, rely=0.21)

                voltage_frame = tk.Frame(cpu_voltage, bg="white")
                voltage_frame.place(
                    relwidth=0.20, relheight=0.15, relx=0.012, rely=0.09)

                voltage_frame_label = tk.Label(voltage_frame, bg=bg, fg=fg, width=100,
                                               height=100, anchor=tk.CENTER, font=font, text="VOLTAGE")
                voltage_frame_label.pack()

                voltage = tk.Frame(cpu_voltage, bg=bg)
                voltage.place(relwidth=0.963, relheight=0.50,
                              relx=0.021, rely=0.426)

                voltage_label = tk.Label(voltage, bg=bg, fg=fg, font=font,
                                         anchor=tk.W, width=100, height=1, text="Voltage")
                voltage_label.pack()

                voltage_bar = tk.Label(voltage, bg=bg, fg=asm_cyan, font=font,
                                       anchor=tk.W, width=100, height=1, text="|")
                voltage_bar.pack()

                voltage_value = tk.Frame(cpu_voltage, bg=bg)
                voltage_value.place(relwidth=0.2, relheight=0.2,
                                    relx=0.78, rely=0.426)

                voltage_value_label = tk.Label(
                    voltage_value, bg=bg, fg=fg, anchor=tk.E, font=font, width=15, height=15, text="0V")
                voltage_value_label.pack()

                bar.update(12.5)

                # Measure frequency

                cpu_frequency = tk.Frame(cpu_frame, bg=bg)
                cpu_frequency.place(relwidth=0.49, relheight=0.19,
                                    relx=0.505, rely=0.42)

                frequency_frame = tk.Frame(cpu_frequency, bg=bg)
                frequency_frame.place(
                    relwidth=0.25, relheight=0.15, relx=0.012, rely=0.09)

                frequency_frame_label = tk.Label(
                    frequency_frame, bg=bg, fg=fg, font=font, anchor=tk.CENTER, width=100, height=100, text="FREQUENCY")
                frequency_frame_label.pack()

                frequency = tk.Frame(cpu_frequency, bg=bg)
                frequency.place(relwidth=0.963, relheight=0.50,
                                relx=0.021, rely=0.426)

                frequency_label = tk.Label(frequency, bg=bg, fg=fg, font=font,
                                           anchor=tk.W, width=100, height=1, text="Current Frequency")
                frequency_label.pack()

                frequency_bar = tk.Label(
                    frequency, bg=bg, fg=asm_cyan, font=font, anchor=tk.W, width=100, height=1, text="|")
                frequency_bar.pack()

                frequency_value = tk.Frame(cpu_frequency, bg=bg)
                frequency_value.place(relwidth=0.3, relheight=0.2,
                                      relx=0.72, rely=0.426)

                frequency_value_label = tk.Label(
                    frequency_value, bg=bg, fg=fg, font=font, anchor=tk.E, width=10, height=10, text="0 MHz")
                frequency_value_label.pack()

                bar.update(12.5)

                # Measure power consumption

                cpu_power = tk.Frame(cpu_frame, bg=bg)
                cpu_power.place(relwidth=0.49, relheight=0.19,
                                relx=0.505, rely=0.63)

                cpu_power_frame = tk.Frame(cpu_power, bg=bg)
                cpu_power_frame.place(
                    relwidth=0.45, relheight=0.15, relx=0.018, rely=0.09)

                cpu_power_label = tk.Label(cpu_power_frame, bg=bg, fg=fg, font=font,
                                           anchor=tk.CENTER, width=100, height=100, text="POWER CONSUMPTION")
                cpu_power_label.pack()

                power_consumption = tk.Frame(cpu_power, bg=bg)
                power_consumption.place(
                    relwidth=0.963, relheight=0.50, relx=0.021, rely=0.426)

                power_consumption_label = tk.Label(
                    power_consumption, bg=bg, fg=fg, font=font, anchor=tk.W, width=100, height=1, text="Power Usage")
                power_consumption_label.pack()

                power_usage_bar = tk.Label(power_consumption, bg=bg, fg=fg,
                                           font=font, anchor=tk.W, width=100, height=1, text="|")
                power_usage_bar.pack()

                power_value = tk.Frame(cpu_power, bg=bg)
                power_value.place(relwidth=0.2, relheight=0.2,
                                  relx=0.78, rely=0.426)

                power_value_label = tk.Label(
                    power_value, bg=bg, fg=fg, font=font, anchor=tk.E, width=10, height=10, text="0 W")
                power_value_label.pack()

                bar.update(12.5)

                # Max values

                max_values = tk.Frame(cpu_frame, bg=bg)
                max_values.place(relwidth=0.49, relheight=0.17,
                                 relx=0.505, rely=0.84)

                # TEMPERATURE
                max_temp_text = tk.Label(max_values, bg=bg, fg=fg, font=font,
                                         anchor=tk.CENTER, width=10, height=1, text="Temp (Max)")
                max_temp_text.grid(row=0, column=0, padx=(7), pady=(30, 0))

                max_temp = tk.Label(max_values, bg=bg, fg=fg, font=font,
                                    anchor=tk.CENTER, width=10, height=1, text="0C")
                max_temp.grid(row=1, column=0, padx=(7), pady=(0))

                # POWER
                max_power_text = tk.Label(max_values, bg=bg, fg=fg, font=font,
                                          anchor=tk.CENTER, width=10, height=1, text="Power (Max)")
                max_power_text.grid(row=0, column=1, padx=(7), pady=(30, 0))

                max_power = tk.Label(max_values, bg=bg, fg=fg, font=font,
                                     anchor=tk.CENTER, width=10, height=1, text="0 W")
                max_power.grid(row=1, column=1, padx=(7), pady=(0))

                # USAGE
                max_usage_text = tk.Label(max_values, bg=bg, fg=fg, font=font,
                                          anchor=tk.CENTER, width=10, height=1, text="Usage (Max)")
                max_usage_text.grid(row=0, column=2, padx=(7), pady=(30, 0))

                max_usage = tk.Label(max_values, bg=bg, fg=fg, font=font,
                                     anchor=tk.CENTER, width=10, height=1, text="0%")
                max_usage.grid(row=1, column=2, padx=(7), pady=(0))

                # FREQUENCY
                max_freq_text = tk.Label(max_values, bg=bg, fg=fg, font=font,
                                         anchor=tk.CENTER, width=10, height=1, text="Freq (Max)")
                max_freq_text.grid(row=0, column=3, padx=(7), pady=(30, 0))

                max_freq = tk.Label(max_values, bg=bg, fg=asm_cyan, font=font,
                                    anchor=tk.CENTER, width=10, height=1, text="0 MHz")
                max_freq.grid(row=1, column=3, padx=(7), pady=(0))

                bar.update(12.5)

                # Notes
                def MessageBox(title, text, style):
                    ctypes.windll.user32.MessageBoxW(0, text, title, style)

                notes = tk.Frame(cpu_frame, bg=bg)
                notes.place(relwidth=0.49, relheight=0.17, relx=0, rely=0.84)

                notes_frame = tk.Frame(notes, bg=bg)
                notes_frame.place(relwidth=0.94, relheight=0.80,
                                  relx=0.01, rely=0.07)

                sheet = PhotoImage(file=f"{image_path}\psheet.png")

                note1 = tk.Button(notes_frame, bg=bg, fg=fg, image=sheet, width=70, height=70,
                                  bd=0, activebackground=button_bg, activeforeground="white", command=lambda: MessageBox(
                                      'Note #1', 'Some metrics require OpenHardwareMonitor to be running in order to display information, If its not running they will show "0" as a value. \n\nCPU Usage does not require OHM as its pulling information directly from the sensors using a module which, well, measures Usage.', 0))
                note1.grid(row=0, column=0, padx=(5), pady=0)

                note1_label = tk.Label(notes_frame, bg=bg, fg=fg, font=font,
                                       anchor=tk.CENTER, width=10, height=1, text="Note #1")
                note1_label.grid(row=1, column=0, padx=(5))

                note2 = tk.Button(notes_frame, bg=bg, fg=fg, image=sheet, width=70, height=70,
                                  bd=0, activebackground=button_bg, activeforeground="white", command=lambda: MessageBox(
                                      'Note #2', 'It is possible that the program will lag when moving it while its refreshing. Lag intensity will depend on your system but it is nothing to worry about as its only refreshing and loading new data and Python apparently does not like to be moved while doing so.', 0))
                note2.grid(row=0, column=1, padx=(5), pady=0)

                note2_label = tk.Label(notes_frame, bg=bg, fg=fg, font=font,
                                       anchor=tk.CENTER, width=10, height=1, text="Note #2")
                note2_label.grid(row=1, column=1, padx=(5))

                note3 = tk.Button(notes_frame, bg=bg, fg=fg, image=sheet, width=70, height=70,
                                  bd=0, activebackground=button_bg, activeforeground="white", command=lambda: MessageBox(
                                      'Note #3', 'If the OpenHardwareMonitor does not launch with this app you can launch it manually and the information will start updating automatically. OHM comes standard with this app so please do not remove it from its own folder. \n\nAlso, some live information is based on maximum values it measured like Power and Frequency, Python cannot determine the TDP or Base frequency so when you load the CPU it will use its Max TDP and Frequency then those values will be used for measurements.', 0))
                note3.grid(row=0, column=2, padx=(5), pady=0)

                note3_label = tk.Label(notes_frame, bg=bg, fg=fg, font=font,
                                       anchor=tk.CENTER, width=10, height=1, text="Note #3")
                note3_label.grid(row=1, column=2, padx=(5))

                note4 = tk.Button(notes_frame, bg=bg, fg=fg, image=sheet, width=70, height=70,
                                  bd=0, activebackground=button_bg, activeforeground="white", command=lambda: MessageBox(
                                      'Note #4', 'Per-Core Usage only supports updating up to 24 cores, meaning it will not show usage Per-Core if you have more than 24 non-logical cores (32, 64 etc.). This feature will be added later when we figure out how to fit them all in that small window. \n\nHowever if you have 12C/24T or less it will show all of the cores including logical ones and if you have more than 12C/24T it will show only non-logical cores up to 24 cores.', 0))
                note4.grid(row=0, column=3, padx=(5), pady=0)

                note4_label = tk.Label(notes_frame, bg=bg, fg=fg, font=font,
                                       anchor=tk.CENTER, width=10, height=1, text="Note #4")
                note4_label.grid(row=1, column=3, padx=(5))

                bar.update(12.5)

                loading.pack_forget()

                refresh_cpu()

        max_record = 0

        dec_cpu = root.after(15, declare_cpu)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# refresh_cpu function updates cpu information every x amount of miliseconds

try:
    def refresh_cpu():
        global ref
        global max_record

        cpuPerc = psutil.cpu_percent()
        cpuCores = psutil.cpu_count(logical=True)
        ind = 1
        row = 0
        column = 0
        pady = (20)
        padx = (5)

        if cpuPerc not in cpu_max_usage_list:
            if cpuPerc > max_record:
                cpu_max_usage_list.append(cpuPerc)
                max_record = cpuPerc
            else:
                max_usage.configure(
                    text=f"{max(cpu_max_usage_list)}%")

        # Update usage per core
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):

            if cpuCores > 16 and cpuCores <= 24:
                pady = (10)
            if cpuCores > 24:
                pady = (10)
                if ind == cpuCores / 2:
                    break
            if cpuCores / 2 > 24:
                break

            core_usage_num = tk.Label(cores, bg=bg, fg=fg,
                                      font=font, anchor=tk.CENTER, width=10, height=2, text=f"Core #{i+1}\n{percentage}%")
            core_usage_num.grid(row=row, column=column, padx=padx, pady=pady)

            if percentage < 30:
                core_usage_num.configure(fg=fg)
            if percentage > 30 and percentage <= 50:
                core_usage_num.configure(fg=asm_yellow)
            if percentage > 50 and percentage <= 90:
                core_usage_num.configure(fg=asm_orange)
            if percentage > 90:
                core_usage_num.configure(fg=asm_red)

            column += 1

            if column > 3:
                column = 0
                row += 1
        # Update total usage

        usage_quotient = cpuPerc / 100

        usage_perc = usage_quotient * 100 / 1.65

        total_usage_bar.configure(text=f"|"*int(usage_perc))

        total_usage_num.configure(text=f"{cpuPerc}%")

        if cpuPerc < 40:
            total_usage_bar.configure(fg=asm_cyan)
        if cpuPerc > 40 and cpuPerc < 60:
            total_usage_bar.configure(fg=asm_yellow)
        if cpuPerc > 60 and cpuPerc < 80:
            total_usage_bar.configure(fg=asm_orange)
        if cpuPerc > 80:
            total_usage_bar.configure(fg=asm_red)

        # Update temperature
        try:
            w = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            temperature_info = w.Sensor()
            for sensor in temperature_info:
                if sensor.SensorType == u"Temperature":
                    if sensor.Name == u"CPU Package":
                        temp_quotient = sensor.Value / 100

                        temp_perc = temp_quotient * 100 / 1.8

                        package_temp_bar.configure(
                            text=f"|"*int(temp_perc))

                        max_temp.configure(text=f"{sensor.Max:.2f}°C")

                        max_temp_sensor = sensor.Max

                        package_temp_value_label.configure(
                            text=f"{sensor.Value:.2f}°C")
                        if sensor.Value < 50:
                            package_temp_bar.configure(fg=asm_cyan)
                        if sensor.Value > 50 and sensor.Value < 70:
                            package_temp_bar.configure(fg=asm_yellow)
                        if sensor.Value > 70 and sensor.Value < 90:
                            package_temp_bar.configure(fg=asm_orange)
                        if sensor.Value > 90:
                            package_temp_bar.configure(fg=asm_red)
                        break
        except Exception as e:
            print(e)

        # Update voltage
        try:
            w = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            voltage_info = w.Sensor()
            for sensor in voltage_info:
                if sensor.SensorType == u"Voltage":
                    if sensor.Name == u"Voltage #1":
                        voltage_quotient = sensor.Value * 100 / 3
                        voltage_bar.configure(
                            text=f"|"*int(voltage_quotient))
                        voltage_value_label.configure(
                            text=f"{sensor.Value:.2f}V")
                        break
        except Exception as e:
            print(e)

        # Update CPU Power

        try:
            w = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            power_info = w.Sensor()
            for sensor in power_info:
                if sensor.Name == u"CPU Package":
                    power_quotient = (sensor.Value / sensor.Max) * 100 / 1.65
                    power_usage_bar.configure(
                        text=f"|"*int(power_quotient))
                    power_value_label.configure(text=f"{sensor.Value:.2f} W")

                    max_power.configure(text=f"{sensor.Max:.2f} W")

                    if sensor.Value <= sensor.Max * 0.5:
                        power_usage_bar.configure(fg=asm_cyan)
                    if sensor.Value > sensor.Max * 0.5 and sensor.Value <= sensor.Max * 0.7:
                        power_usage_bar.configure(fg=asm_yellow)
                    if sensor.Value > sensor.Max * 0.7 and sensor.Value <= sensor.Max * 0.9:
                        power_usage_bar.configure(fg=asm_orange)
                    if sensor.Value > sensor.Max * 0.9:
                        power_usage_bar.configure(fg=asm_red)

                    # Adjust color for max values
                    if sensor.Max < sensor.Max * 0.5:
                        max_power.configure(fg=asm_cyan)
                    elif sensor.Max > sensor.Max * 0.5 and sensor.Max <= sensor.Max * 0.7:
                        max_power.configure(fg=asm_yellow)
                    elif sensor.Max > sensor.Max * 0.7 and sensor.Max <= sensor.Max * 0.9:
                        max_power.configure(fg=asm_orange)
                    elif sensor.Max > sensor.Max * 0.9:
                        max_power.configure(fg=asm_red)

                    break
        except Exception as e:
            print(e)

        # Update frequency
        try:
            w = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            freq_info = w.Sensor()
            for sensor in freq_info:
                if sensor.SensorType == u"Clock":
                    if sensor.Name == u"CPU Core #1":
                        freq_quotient = (
                            (sensor.Value / sensor.Max) * 100) / 1.8

                        frequency_bar.configure(
                            text=f"|"*int(freq_quotient))
                        frequency_value_label.configure(
                            text=f"{sensor.Value:.1f} MHz")
                        max_freq.configure(text=f"{sensor.Max:.1f} MHz")
                        break
        except Exception as e:
            print(e)

        try:
            if max(cpu_max_usage_list) <= 40:
                max_usage.configure(fg=asm_cyan)
            elif max(cpu_max_usage_list) > 40 and max(cpu_max_usage_list) <= 60:
                max_usage.configure(fg=asm_yellow)
            elif max(cpu_max_usage_list) > 60 and max(cpu_max_usage_list) <= 80:
                max_usage.configure(fg=asm_orange)
            elif max(cpu_max_usage_list) > 80:
                max_usage.configure(fg=asm_red)
        except Exception as e:
            print(e)

        try:
            if max_temp_sensor <= 50:
                max_temp.configure(fg=asm_cyan)
            elif max_temp_sensor > 50 and max_temp_sensor <= 70:
                max_temp.configure(fg=asm_yellow)
            elif max_temp_sensor > 70 and max_temp_sensor <= 90:
                max_temp.configure(fg=asm_orange)
            elif max_temp_sensor > 90:
                max_temp.configure(fg=asm_red)
        except Exception as e:
            print(e)

        ref = root.after(1500, refresh_cpu)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# GPU function gets all the information available for the GPU

try:
    def gpu():
        global gpu_frame

        # Remove any previously opened windows and change button background

        try:
            gpuButton.configure(bg=button_bg)
        except Exception as e:
            print(e)

        try:
            combined_test_frame.place_forget()
            root.after_cancel(rct)
        except Exception as e:
            print(e)

        try:
            homeButton.configure(bg=sidemenu_bg)
            root.after_cancel(time)
            root.after_cancel(ff)
            home_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            cpuButton.configure(bg=sidemenu_bg)
            root.after_cancel(ref)
            cpu_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            motherboardButton.configure(bg=sidemenu_bg)
            main_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            ramButton.configure(bg=sidemenu_bg)
            root.after_cancel(ram_ref)
            ram_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            hddButton.configure(bg=sidemenu_bg)
            root.after_cancel(drive_ref)
            drive_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            netButton.configure(bg=sidemenu_bg)
            root.after_cancel(net_ref)
            network_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            fanButton.configure(bg=sidemenu_bg)
            root.after_cancel(fan_ref)
            fans_frame.place_forget()
        except Exception as e:
            print(e)

        # Set up frames and labels
        gpu_frame = tk.Frame(root, bg=canvas_bg)
        gpu_frame.place(relwidth=0.875, relheight=0.96, relx=0.117, rely=0.021)

        loading = tk.Label(gpu_frame, bg=canvas_bg, fg=fg, font=(
            loading_font), width=100, height=50, text="Loading...")
        loading.pack()

        def declare_gpu():
            global total_gpu_usage_bar
            global total_gpu_usage_num
            global current_temp_bar
            global current_temp_num_label
            global vram_bar
            global vram_value_label
            global core_clock_value
            global core_clock_bar
            global memory_clock_bar
            global memory_clock_value
            global shader_clock_bar
            global shader_clock_value
            global core_load
            global frame_buffer
            global video_engine
            global bus_interface
            global memory_load
            global rpm_value
            global fan_rpm_bar
            global video_engine_usage_bar
            global video_engine_value_label
            global gpu_max_temp
            global gpu_max_usage
            global gpu_max_vram
            global gpu_max_rpm
            global note_image

            root.after_cancel(dec_gpu)

            with tqdm(total=100) as bar:
                # Set frames, labels and bar for usage
                gpu_usage = tk.Frame(gpu_frame, bg=bg)
                gpu_usage.place(relwidth=0.49, relheight=0.19, relx=0, rely=0)

                usage_frame = tk.Frame(gpu_usage, bg=bg)
                usage_frame.place(
                    relwidth=0.15, relheight=0.15, relx=0.01, rely=0.08)

                usage_label = tk.Label(usage_frame, bg=bg, fg=fg, width=100,
                                       height=1, anchor=tk.CENTER, font=font, text="USAGE")
                usage_label.pack()

                total_gpu_usage = tk.Frame(gpu_usage, bg=bg)
                total_gpu_usage.place(relwidth=1, relheight=0.90,
                                      relx=0.02, rely=0.426)

                total_gpu_usage_label = tk.Label(total_gpu_usage, bg=bg, fg=fg, width=100,
                                                 height=1, anchor=tk.W, font=font, text="Total usage")
                total_gpu_usage_label.pack()

                total_gpu_usage_bar = tk.Label(total_gpu_usage, bg=bg, fg=fg, width=100,
                                               height=1, anchor=tk.W, font=font, text="|")
                total_gpu_usage_bar.pack()

                total_gpu_usage_num_frame = tk.Frame(gpu_usage, bg=bg)
                total_gpu_usage_num_frame.place(
                    relwidth=0.25, relheight=0.15, relx=0.72, rely=0.465)

                total_gpu_usage_num = tk.Label(total_gpu_usage_num_frame, bg=bg,
                                               fg=fg, font=font, anchor=tk.E, width=15, height=15, text="0%")
                total_gpu_usage_num.pack()

                bar.update(10)

                # Set frames, labels and bar for temperature
                gpu_temp = tk.Frame(gpu_frame, bg=bg)
                gpu_temp.place(relwidth=0.49, relheight=0.19,
                               relx=0.505, rely=0)

                gpu_temp_frame = tk.Frame(gpu_temp, bg=bg)
                gpu_temp_frame.place(relwidth=0.40, relheight=0.15,
                                     relx=-0.04, rely=0.09)

                gpu_temp_label = tk.Label(gpu_temp_frame, bg=bg, fg=fg, width=100,
                                          height=100, anchor=tk.CENTER, font=font, text="TEMPERATURE")
                gpu_temp_label.pack()

                temp_container = tk.Frame(gpu_temp, bg=bg)
                temp_container.place(relwidth=0.963, relheight=0.50,
                                     relx=0.018, rely=0.426)

                current_temp = tk.Label(temp_container, bg=bg, fg=fg, width=100,
                                        height=1, anchor=tk.W, font=font, text="Current Temperature")
                current_temp.pack()

                current_temp_bar = tk.Label(temp_container, bg=bg, fg=fg, width=100,
                                            height=1, anchor=tk.W, font=font, text="|")
                current_temp_bar.pack()

                current_temp_num = tk.Frame(gpu_temp, bg=bg)
                current_temp_num.place(
                    relwidth=0.15, relheight=0.25, relx=0.83, rely=0.40)

                current_temp_num_label = tk.Label(current_temp_num, bg=bg, fg=fg, width=15,
                                                  height=15, anchor=tk.E, font=font, text="0°C")
                current_temp_num_label.pack()

                bar.update(10)

                # Set frames, labels and bar for VRAM usage
                gpu_vram_usage = tk.Frame(gpu_frame, bg=bg)
                gpu_vram_usage.place(relwidth=0.49, relheight=0.19,
                                     relx=0.505, rely=0.21)

                vram_frame = tk.Frame(gpu_vram_usage, bg=bg)
                vram_frame.place(relwidth=0.28, relheight=0.15,
                                 relx=0.012, rely=0.09)

                vram_label = tk.Label(vram_frame, bg=bg, fg=fg, font=font,
                                      anchor=tk.CENTER, width=100, height=10, text="VRAM USAGE")
                vram_label.pack()

                vram = tk.Frame(gpu_vram_usage, bg=bg)
                vram.place(relwidth=0.963, relheight=0.50,
                           relx=0.021, rely=0.426)

                vram_label = tk.Label(vram, bg=bg, fg=fg, font=font,
                                      anchor=tk.W, width=100, height=1, text="VRAM")
                vram_label.pack()

                vram_bar = tk.Label(vram, bg=bg, fg=fg, font=font,
                                    anchor=tk.W, width=100, height=1, text="|")
                vram_bar.pack()

                vram_value = tk.Frame(gpu_vram_usage, bg=bg)
                vram_value.place(relwidth=0.3, relheight=0.2,
                                 relx=0.684, rely=0.426)

                vram_value_label = tk.Label(
                    vram_value, bg=bg, fg=fg, anchor=tk.E, font=font, width=40, height=15, text="0GB/0GB")
                vram_value_label.pack()

                bar.update(10)

                # Set frame, labels and bars for various gpu clock speeds
                gpu_clocks = tk.Frame(gpu_frame, bg=bg)
                gpu_clocks.place(
                    relwidth=0.49, relheight=0.35, relx=0, rely=0.21)

                clocks_frame = tk.Frame(gpu_clocks, bg=bg)
                clocks_frame.place(relwidth=0.15, relheight=0.15,
                                   relx=0.023, rely=0.03)

                clocks_label = tk.Label(clocks_frame, bg=bg, fg=fg, font=font,
                                        anchor=tk.CENTER, width=100, height=1, text="CLOCKS")
                clocks_label.pack()

                # Container which holds all the clocks
                clock_container = tk.Frame(gpu_clocks, bg=bg)
                clock_container.place(
                    relwidth=1, relheight=0.76, relx=0, rely=0.217)

                # Core clock
                core_clock = tk.Label(clock_container, bg=bg, fg=fg, font=font,
                                      anchor=tk.W, width=100, height=1, text="Core Clock")
                core_clock.grid(row=0, column=0, padx=(10), pady=(5, 0))

                core_clock_bar = tk.Label(clock_container, bg=bg, fg=asm_cyan,
                                          font=font, anchor=tk.W, width=100, height=1, text="|")
                core_clock_bar.grid(row=1, column=0, padx=(10))

                core_clock_value_frame = tk.Frame(gpu_clocks, bg=bg)
                core_clock_value_frame.place(
                    relwidth=0.30, relheight=0.10, relx=0.675, rely=0.245)

                core_clock_value = tk.Label(core_clock_value_frame, bg=bg, fg=fg, font=font,
                                            anchor=tk.E, width=100, height=1, text="0 MHz")
                core_clock_value.pack()

                # Memory clock
                memory_clock = tk.Label(clock_container, bg=bg, fg=fg, font=font,
                                        anchor=tk.W, width=100, height=1, text="Memory Clock")
                memory_clock.grid(row=2, column=0, padx=(10))

                memory_clock_bar = tk.Label(clock_container, bg=bg, fg=asm_cyan,
                                            font=font, anchor=tk.W, width=100, height=1, text="|")
                memory_clock_bar.grid(row=3, column=0, padx=(10))

                memory_clock_value_frame = tk.Frame(gpu_clocks, bg=bg)
                memory_clock_value_frame.place(
                    relwidth=0.30, relheight=0.10, relx=0.675, rely=0.48)

                memory_clock_value = tk.Label(memory_clock_value_frame, bg=bg, fg=fg, font=font,
                                              anchor=tk.E, width=100, height=1, text="0 MHz")
                memory_clock_value.pack()

                # Shader clock
                shader_clock = tk.Label(clock_container, bg=bg, fg=fg, font=font,
                                        anchor=tk.W, width=100, height=1, text="Shader Clock")
                shader_clock.grid(row=4, column=0, padx=(10))

                shader_clock_bar = tk.Label(clock_container, bg=bg, fg=asm_cyan,
                                            font=font, anchor=tk.W, width=100, height=1, text="|")
                shader_clock_bar.grid(row=5, column=0, padx=(10))

                shader_clock_value_frame = tk.Frame(gpu_clocks, bg=bg)
                shader_clock_value_frame.place(
                    relwidth=0.30, relheight=0.10, relx=0.675, rely=0.715)

                shader_clock_value = tk.Label(shader_clock_value_frame, bg=bg, fg=fg, font=font,
                                              anchor=tk.E, width=100, height=1, text="0 MHz")
                shader_clock_value.pack()

                bar.update(10)

                # Set frames and labels for various gpu loads

                gpu_loads = tk.Frame(gpu_frame, bg=bg)
                gpu_loads.place(relwidth=0.49, relheight=0.24,
                                relx=0, rely=0.58)

                gpu_loads_label_frame = tk.Frame(gpu_loads, bg=bg)
                gpu_loads_label_frame.place(
                    relwidth=0.15, relheight=0.15, relx=0.02, rely=0.04)

                gpu_loads_label = tk.Label(gpu_loads_label_frame, bg=bg, fg=fg,
                                           font=font, anchor=tk.CENTER, width=100, height=10, text="LOADS")
                gpu_loads_label.pack()

                load_container = tk.Frame(gpu_loads, bg=bg)
                load_container.place(
                    relwidth=1, relheight=0.70, relx=0, rely=0.30)

                core_load = tk.Label(load_container, bg=bg, fg=fg, font=font,
                                     anchor=tk.CENTER, width=10, height=2, text="Core Load\n0%")
                core_load.grid(row=0, column=0, padx=(25), pady=(5))

                frame_buffer = tk.Label(load_container, bg=bg, fg=fg, font=font,
                                        anchor=tk.CENTER, width=10, height=2, text="Frame Buffer\n0%")
                frame_buffer.grid(row=0, column=1, padx=(25), pady=(5))

                bus_interface = tk.Label(load_container, bg=bg, fg=fg, font=font,
                                         anchor=tk.CENTER, width=10, height=2, text="Bus Interface\n0%")
                bus_interface.grid(row=0, column=2, padx=(25), pady=(20))

                bar.update(10)

                # GPU Fans

                gpu_fans = tk.Frame(gpu_frame, bg=bg)
                gpu_fans.place(relwidth=0.49, relheight=0.19,
                               relx=0.505, rely=0.42)

                gpu_fans_label_frame = tk.Frame(gpu_fans, bg=bg)
                gpu_fans_label_frame.place(
                    relwidth=0.10, relheight=0.15, relx=0.027, rely=0.085)

                gpu_fans_label = tk.Label(gpu_fans_label_frame, bg=bg, fg=fg,
                                          font=font, anchor=tk.CENTER, width=100, height=10, text="FANS")
                gpu_fans_label.pack()

                fans_container = tk.Frame(gpu_fans, bg=bg)
                fans_container.place(relwidth=0.963, relheight=0.50,
                                     relx=0.021, rely=0.426)

                fan_rpm = tk.Label(fans_container, bg=bg, fg=fg, font=font,
                                   anchor=tk.W, width=100, height=1, text="Fan RPM")
                fan_rpm.pack()

                fan_rpm_bar = tk.Label(fans_container, bg=bg, fg=fg,
                                       font=font, anchor=tk.W, width=100, height=1, text="|")
                fan_rpm_bar.pack()

                rpm_value_frame = tk.Frame(gpu_fans, bg=bg)
                rpm_value_frame.place(relwidth=0.3, relheight=0.2,
                                      relx=0.684, rely=0.426)

                rpm_value = tk.Label(rpm_value_frame, bg=bg, fg=fg, font=font,
                                     anchor=tk.E, width=40, height=15, text="0 RPM")
                rpm_value.pack()

                bar.update(10)

                # Video engine

                gpu_video_engine = tk.Frame(gpu_frame, bg=bg)
                gpu_video_engine.place(relwidth=0.49, relheight=0.19,
                                       relx=0.505, rely=0.63)

                gpu_video_engine_frame = tk.Frame(gpu_video_engine, bg=bg)
                gpu_video_engine_frame.place(
                    relwidth=0.30, relheight=0.15, relx=0.01, rely=0.085)

                gpu_video_engine_label = tk.Label(gpu_video_engine_frame, bg=bg, fg=fg,
                                                  font=font, anchor=tk.CENTER, width=100, height=10, text="VIDEO ENGINE")
                gpu_video_engine_label.pack()

                video_engine_container = tk.Frame(gpu_video_engine, bg=bg)
                video_engine_container.place(
                    relwidth=0.963, relheight=0.50, relx=0.021, rely=0.426)

                video_engine_usage = tk.Label(video_engine_container, bg=bg, fg=fg,
                                              font=font, anchor=tk.W, width=100, height=1, text="Usage")
                video_engine_usage.pack()

                video_engine_usage_bar = tk.Label(
                    video_engine_container, bg=bg, fg=fg, font=font, anchor=tk.W, width=100, height=1, text="|")
                video_engine_usage_bar.pack()

                video_engine_value_frame = tk.Frame(gpu_video_engine, bg=bg)
                video_engine_value_frame.place(
                    relwidth=0.3, relheight=0.2, relx=0.684, rely=0.426)

                video_engine_value_label = tk.Label(
                    video_engine_value_frame, bg=bg, fg=fg, font=font, anchor=tk.E, width=40, height=15, text="0%")
                video_engine_value_label.pack()

                bar.update(10)

                # Max recorded values

                gpu_max_values = tk.Frame(gpu_frame, bg=bg)
                gpu_max_values.place(relwidth=0.49, relheight=0.17,
                                     relx=0.505, rely=0.84)

                gpu_max_temp_text = tk.Label(gpu_max_values, bg=bg, fg=fg, font=font,
                                             anchor=tk.CENTER, width=10, height=1, text="Temp (Max)")
                gpu_max_temp_text.grid(row=0, column=0, padx=(7), pady=(30, 0))

                gpu_max_temp = tk.Label(gpu_max_values, bg=bg, fg=fg, font=font,
                                        anchor=tk.CENTER, width=10, height=1, text="0C")
                gpu_max_temp.grid(row=1, column=0, padx=(7), pady=0)

                gpu_max_usage_text = tk.Label(gpu_max_values, bg=bg, fg=fg, font=font,
                                              anchor=tk.CENTER, width=10, height=1, text="Usage (Max)")
                gpu_max_usage_text.grid(
                    row=0, column=1, padx=(7), pady=(30, 0))

                gpu_max_usage = tk.Label(gpu_max_values, bg=bg, fg=fg, font=font,
                                         anchor=tk.CENTER, width=10, height=1, text="0%")
                gpu_max_usage.grid(row=1, column=1, padx=(7), pady=0)

                gpu_max_vram_text = tk.Label(gpu_max_values, bg=bg, fg=fg, font=font,
                                             anchor=tk.CENTER, width=10, height=1, text="VRAM (Max)")
                gpu_max_vram_text.grid(row=0, column=2, padx=(7), pady=(30, 0))

                gpu_max_vram = tk.Label(gpu_max_values, bg=bg, fg=fg, font=font,
                                        anchor=tk.CENTER, width=10, height=1, text="0GB")
                gpu_max_vram.grid(row=1, column=2, padx=(7), pady=0)

                gpu_max_rpm_text = tk.Label(gpu_max_values, bg=bg, fg=fg, font=font,
                                            anchor=tk.CENTER, width=10, height=1, text="RPM (Max)")
                gpu_max_rpm_text.grid(row=0, column=3, padx=(7), pady=(30, 0))

                gpu_max_rpm = tk.Label(gpu_max_values, bg=bg, fg=fg, font=font,
                                       anchor=tk.CENTER, width=10, height=1, text="0 RPM")
                gpu_max_rpm.grid(row=1, column=3, padx=(7), pady=0)

                bar.update(10)

                # Notes
                def MessageBox(title, text, style):
                    ctypes.windll.user32.MessageBoxW(0, text, title, style)

                note_image = PhotoImage(file=f"{image_path}\psheet.png")

                gpu_section_notes = tk.Frame(gpu_frame, bg=bg)
                gpu_section_notes.place(
                    relwidth=0.49, relheight=0.17, relx=0, rely=0.84)

                gpu_section_notes_frame = tk.Frame(gpu_section_notes, bg=bg)
                gpu_section_notes_frame.place(
                    relwidth=0.94, relheight=0.80, relx=0.01, rely=0.07)

                gpu_note_1 = tk.Button(gpu_section_notes_frame, bg=bg, fg=fg, image=note_image, width=70, height=70, bd=0,
                                       activebackground=button_bg, activeforeground="white", command=lambda: MessageBox('Note #1', 'This is a test!', 0))
                gpu_note_1.grid(row=0, column=0, padx=(5), pady=0)

                gpu_note_1_label = tk.Label(gpu_section_notes_frame, bg=bg, fg=fg,
                                            font=font, anchor=tk.CENTER, width=10, height=1, text="Note #1")
                gpu_note_1_label.grid(row=1, column=0, padx=(5))

                gpu_note_2 = tk.Button(gpu_section_notes_frame, bg=bg, fg=fg, image=note_image, width=70, height=70, bd=0,
                                       activebackground=button_bg, activeforeground="white", command=lambda: MessageBox('Note #2', 'This is a test!', 0))
                gpu_note_2.grid(row=0, column=1, padx=(5), pady=0)

                gpu_note_2_label = tk.Label(gpu_section_notes_frame, bg=bg, fg=fg,
                                            font=font, anchor=tk.CENTER, width=10, height=1, text="Note #2")
                gpu_note_2_label.grid(row=1, column=1, padx=(5))

                gpu_note_3 = tk.Button(gpu_section_notes_frame, bg=bg, fg=fg, image=note_image, width=70, height=70, bd=0,
                                       activebackground=button_bg, activeforeground="white", command=lambda: MessageBox('Note #3', 'This is a test!', 0))
                gpu_note_3.grid(row=0, column=2, padx=(5), pady=0)

                gpu_note_3_label = tk.Label(gpu_section_notes_frame, bg=bg, fg=fg,
                                            font=font, anchor=tk.CENTER, width=10, height=1, text="Note #3")
                gpu_note_3_label.grid(row=1, column=2, padx=(5))

                gpu_note_4 = tk.Button(gpu_section_notes_frame, bg=bg, fg=fg, image=note_image, width=70, height=70, bd=0,
                                       activebackground=button_bg, activeforeground="white", command=lambda: MessageBox('Note #4', 'This is a test!', 0))
                gpu_note_4.grid(row=0, column=3, padx=(5), pady=0)

                gpu_note_4_label = tk.Label(gpu_section_notes_frame, bg=bg, fg=fg,
                                            font=font, anchor=tk.CENTER, width=10, height=1, text="Note #4")
                gpu_note_4_label.grid(row=1, column=3, padx=(5))

                bar.update(20)

                loading.pack_forget()

                refresh_gpu()
        dec_gpu = root.after(15, declare_gpu)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# This function refreshes GPU information every x amount of miliseconds

try:
    def refresh_gpu():

        global gpu_update

        # Find gpus
        devices = GPUtil.getGPUs()

        for gpu in devices:
            gpu_load = f"{gpu.load*100}"
            gpu_total_memory = f"{gpu.memoryTotal / 1000}"
            gpu_temperature = f"{gpu.temperature}"
            gpu_used_memory = f"{gpu.memoryUsed / 1000}"

        # A little math to optimize the percentage to bar length
        load_perc = float(gpu_load) / 1.65
        mem_perc = ((float(gpu_used_memory) /
                     float(gpu_total_memory)) * 100) / 1.65
        temp_perc = ((float(gpu_temperature) / 120) * 100) / 1.65

        # Adjust colors for usage
        if float(gpu_load) <= 30:
            total_gpu_usage_bar.configure(fg=asm_cyan)
        elif float(gpu_load) > 30 and float(gpu_load) <= 60:
            total_gpu_usage_bar.configure(fg=asm_yellow)
        elif float(gpu_load) > 60 and float(gpu_load) <= 80:
            total_gpu_usage_bar.configure(fg=asm_orange)
        elif float(gpu_load) > 80:
            total_gpu_usage_bar.configure(fg=asm_red)

        # Adjust colors for temperature
        if float(gpu_temperature) <= 50:
            current_temp_bar.configure(fg=asm_cyan)
        elif float(gpu_temperature) > 50 and float(gpu_temperature) <= 60:
            current_temp_bar.configure(fg=asm_yellow)
        elif float(gpu_temperature) > 60 and float(gpu_temperature) <= 75:
            current_temp_bar.configure(fg=asm_orange)
        elif float(gpu_temperature) > 75:
            current_temp_bar.configure(fg=asm_red)

        # Adjust colors for VRAM
        mem_perc_unop = (
            (float(gpu_used_memory) / float(gpu_total_memory)) * 100)

        if mem_perc_unop not in gpu_max_vram_perc:
            gpu_max_vram_perc.append(mem_perc_unop)

        if mem_perc_unop < 10:
            vram_bar.configure(fg=asm_cyan)
        elif mem_perc_unop > 10 and mem_perc_unop <= 30:
            vram_bar.configure(fg=asm_green)
        elif mem_perc_unop > 30 and mem_perc_unop <= 60:
            vram_bar.configure(fg=asm_yellow)
        elif mem_perc_unop > 60 and mem_perc_unop <= 80:
            vram_bar.configure(fg=asm_orange)
        elif mem_perc_unop > 80:
            vram_bar.configure(fg=asm_red)

        # Update usage
        if int(load_perc) < 1:
            total_gpu_usage_bar.configure(text="|")
        else:
            total_gpu_usage_bar.configure(text="|"*int(load_perc))
            total_gpu_usage_num.configure(text=f"{float(gpu_load):.1f}%")

        # Update temperature
        current_temp_bar.configure(text="|"*int(temp_perc))
        current_temp_num_label.configure(text=f"{gpu_temperature}°C")

        # Update VRAM
        vram_bar.configure(text="|"*int(mem_perc))
        vram_value_label.configure(
            text=f"{float(gpu_used_memory):.2f}GB/{float(gpu_total_memory):.2f}GB")

        # Update core clock
        try:
            c = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            core_clock = c.Sensor()
            clock_bar_percentage = 0
            for sensor in core_clock:
                if sensor.SensorType == u"Clock":
                    if sensor.Name == u"GPU Core":
                        clock_bar_percentage = (
                            (sensor.Value / sensor.Max) * 100) / 1.62
                        core_clock_value.configure(
                            text=f"{sensor.Value:.2f} MHz")
                        core_clock_bar.configure(
                            text="|"*int(clock_bar_percentage))
        except Exception as e:
            print(e)

        # Update memory clock
        try:
            m = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            memory_clock = m.Sensor()
            for sensor in memory_clock:
                if sensor.SensorType == u"Clock":
                    if sensor.Name == u"GPU Memory":
                        clock_bar_percentage = (
                            (sensor.Value / sensor.Max) * 100) / 1.62
                        memory_clock_value.configure(
                            text=f"{sensor.Value:.2f} MHz")
                        memory_clock_bar.configure(
                            text=f"|"*int(clock_bar_percentage))
        except Exception as e:
            print(e)

        # Update shader clock
        try:
            s = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            shader_clock = s.Sensor()
            shader_bar_percentage = 0
            for sensor in shader_clock:
                if sensor.SensorType == u"Clock":
                    if sensor.Name == u"GPU Shader":
                        shader_bar_percentage = (
                            (sensor.Value / sensor.Max) * 100) / 1.62
                        shader_clock_value.configure(
                            text=f"{sensor.Value:.2f} MHz")
                        shader_clock_bar.configure(
                            text="|"*int(shader_bar_percentage))
        except Exception as e:
            print(e)

        # Update loads

        try:
            l = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            loads = s.Sensor()
            for sensor in loads:
                if sensor.SensorType == u"Load":
                    if sensor.Name == u"GPU Core":
                        core_load.configure(text=f"Core Load\n{sensor.Value}%")
                    if sensor.Name == u"GPU Frame Buffer":
                        frame_buffer.configure(
                            text=f"Frame Buffer\n{sensor.Value:.1f}%")
                    if sensor.Name == u"GPU Bus Interface":
                        bus_interface.configure(
                            text=f"Bus Interface\n{sensor.Value:.1f}%")
        except Exception as e:
            print(e)

        # Update fan RPM

        try:
            f = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            fans = f.Sensor()
            for sensor in fans:
                if sensor.SensorType == u"Fan":
                    if sensor.Name == u"GPU":
                        rpm_value.configure(text=f"{sensor.Value} RPM")
                        if sensor.Value not in gpu_max_fan_list:
                            gpu_max_fan_list.append(sensor.Value)
                        else:
                            gpu_max_rpm.configure(
                                text=f"{max(gpu_max_fan_list)} RPM")
                if sensor.SensorType == u"Control":
                    if sensor.Name == u"GPU Fan":
                        # Adjust colors for GPU Fans

                        if sensor.Value < 30:
                            fan_rpm_bar.configure(fg=asm_cyan)
                        elif sensor.Value > 30 and sensor.Value <= 60:
                            fan_rpm_bar.configure(fg=asm_yellow)
                        elif sensor.Value > 60 and sensor.Value <= 80:
                            fan_rpm_bar.configure(fg=asm_orange)
                        elif sensor.Value > 80:
                            fan_rpm_bar.configure(fg=asm_red)

                        quotient = sensor.Value / 1.65
                        fan_rpm_bar.configure(text=f"|"*int(quotient))

                        if sensor.Value not in gpu_max_fan_perc:
                            gpu_max_fan_perc.append(sensor.Value)
                        else:
                            if float(max(gpu_max_fan_perc)) <= 30:
                                gpu_max_rpm.configure(fg=asm_cyan)
                            elif float(max(gpu_max_fan_perc)) > 30 and float(max(gpu_max_fan_perc)) <= 60:
                                gpu_max_rpm.configure(fg=asm_yellow)
                            elif float(max(gpu_max_fan_perc)) > 60 and float(max(gpu_max_fan_perc)) <= 80:
                                gpu_max_rpm.configure(fg=asm_orange)
                            elif float(max(gpu_max_fan_perc)) > 80:
                                gpu_max_rpm.configure(fg=asm_red)

        except Exception as e:
            print(e)

        # Update video engine usage

        try:
            ve = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            v_engine = s.Sensor()
            for sensor in v_engine:
                if sensor.SensorType == u"Load":
                    if sensor.Name == u"GPU Video Engine":
                        ve_quotient = sensor.Value / 1.65

                        # Adjusts colors for video engine usage

                        if sensor.Value < 40:
                            video_engine_usage_bar.configure(fg=asm_cyan)
                        elif sensor.Value > 40 and sensor.Value <= 60:
                            video_engine_usage_bar.configure(fg=asm_yellow)
                        elif sensor.Value > 60 and sensor.Value <= 80:
                            video_engine_usage_bar.configure(fg=asm_orange)
                        elif sensor.Value > 80:
                            video_engine_usage_bar.configure(fg=asm_red)
                        video_engine_value_label.configure(
                            text=f"{sensor.Value}%")
                        if ve_quotient < 1:
                            video_engine_usage_bar.configure(text="|")
                        else:
                            video_engine_usage_bar.configure(
                                text="|"*int(ve_quotient))
        except Exception as e:
            print(e)

        # Update maximum values

        try:
            if gpu_load not in gpu_max_load_list:
                gpu_max_load_list.append(gpu_load)
            else:
                if float(max(gpu_max_load_list)) < 30:
                    gpu_max_usage.configure(fg=asm_cyan)
                elif float(max(gpu_max_load_list)) > 30 and float(max(gpu_max_load_list)) <= 60:
                    gpu_max_usage.configure(fg=asm_yellow)
                elif float(max(gpu_max_load_list)) > 60 and float(max(gpu_max_load_list)) <= 80:
                    gpu_max_usage.configure(fg=asm_orange)
                elif float(max(gpu_max_load_list)) > 80:
                    gpu_max_usage.configure(fg=asm_red)

                gpu_max_usage.configure(
                    text=f"{max(gpu_max_load_list)}%")
        except Exception as e:
            print(e)

        try:
            if gpu_temperature not in gpu_max_temp_list:
                gpu_max_temp_list.append(gpu_temperature)
            else:
                if float(max(gpu_max_temp_list)) < 50:
                    gpu_max_temp.configure(fg=asm_cyan)
                elif float(max(gpu_max_temp_list)) > 50 and float(max(gpu_max_temp_list)) <= 60:
                    gpu_max_temp.configure(fg=asm_yellow)
                elif float(max(gpu_max_temp_list)) > 60 and float(max(gpu_max_temp_list)) <= 75:
                    gpu_max_temp.configure(fg=asm_orange)
                elif float(max(gpu_max_temp_list)) > 75:
                    gpu_max_temp.configure(fg=asm_red)

                gpu_max_temp.configure(
                    text=f"{max(gpu_max_temp_list)}°C")
        except Exception as e:
            print(e)

        try:
            if gpu_used_memory not in gpu_max_vram_list:
                gpu_max_vram_list.append(gpu_used_memory)
            else:
                if float(max(gpu_max_vram_perc)) < 10:
                    gpu_max_vram.configure(fg=asm_cyan)
                elif float(max(gpu_max_vram_perc)) > 10 and float(max(gpu_max_vram_perc)) <= 30:
                    gpu_max_vram.configure(fg=asm_green)
                elif float(max(gpu_max_vram_perc)) > 30 and float(max(gpu_max_vram_perc)) <= 60:
                    gpu_max_vram.configure(fg=asm_yellow)
                elif float(max(gpu_max_vram_perc)) > 60 and float(max(gpu_max_vram_perc)) <= 80:
                    gpu_max_vram.configure(fg=asm_orange)
                elif float(max(gpu_max_vram_perc)) > 80:
                    gpu_max_vram.configure(fg=asm_red)

                gpu_max_vram.configure(
                    text=f"{max(gpu_max_vram_list)}GB")
        except Exception as e:
            print(e)

        gpu_update = root.after(1000, refresh_gpu)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# RAM function gets all available information for RAM and SWAP memory

try:
    def ram():
        global ram_frame

        # Remove and previously running windows and change button background

        try:
            ramButton.configure(bg=button_bg)
        except Exception as e:
            print(e)

        try:
            combined_test_frame.place_forget()
            root.after_cancel(rct)
        except Exception as e:
            print(e)

        try:
            homeButton.configure(bg=sidemenu_bg)
            root.after_cancel(time)
            root.after_cancel(ff)
            home_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            cpuButton.configure(bg=sidemenu_bg)
            root.after_cancel(ref)
            cpu_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            motherboardButton.configure(bg=sidemenu_bg)
            main_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            gpuButton.configure(bg=sidemenu_bg)
            root.after_cancel(gpu_update)
            gpu_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            hddButton.configure(bg=sidemenu_bg)
            root.after_cancel(drive_ref)
            drive_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            netButton.configure(bg=sidemenu_bg)
            root.after_cancel(net_ref)
            network_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            fanButton.configure(bg=sidemenu_bg)
            root.after_cancel(fan_ref)
            fans_frame.place_forget()
        except Exception as e:
            print(e)

        # Setup main container

        ram_frame = tk.Frame(root, bg=canvas_bg)
        ram_frame.place(relwidth=0.875, relheight=0.96, relx=0.117, rely=0.021)

        loading = tk.Label(ram_frame, bg=canvas_bg, fg=fg, font=(
            loading_font), width=100, height=50, text="Loading...")
        loading.pack()

        def declare_ram():
            global ram_usage_bar
            global ram_usage_value_label
            global ram_free_bar
            global ram_free_value_label
            global ram_max_usage_bar
            global ram_max_usage_value_label
            global swap_usage_bar
            global swap_usage_value
            global swap_free_bar
            global swap_free_value
            global swap_max_usage_bar
            global swap_max_usage_value
            root.after_cancel(dec_ram)
            with tqdm(total=100) as bar:
                # Ram usage

                ram_usage_frame = tk.Frame(ram_frame, bg=bg)
                ram_usage_frame.place(
                    relwidth=0.49, relheight=0.19, relx=0, rely=0)

                ram_usage_label_frame = tk.Frame(ram_usage_frame, bg=bg)
                ram_usage_label_frame.place(
                    relwidth=0.30, relheight=0.15, relx=0.02, rely=0.08)

                ram_usage_label = tk.Label(ram_usage_label_frame, bg=bg, fg=fg,
                                           font=font, anchor=tk.W, width=100, height=10, text="RAM USAGE")
                ram_usage_label.pack()

                ram_usage_container = tk.Frame(ram_usage_frame, bg=bg)
                ram_usage_container.place(
                    relwidth=0.963, relheight=0.5, relx=0.018, rely=0.426)

                ram_usage = tk.Label(ram_usage_container, bg=bg, fg=fg, font=font,
                                     anchor=tk.W, width=100, height=1, text="Total Usage")
                ram_usage.pack()

                ram_usage_bar = tk.Label(ram_usage_container, bg=bg, fg=fg,
                                         font=font, anchor=tk.W, width=100, height=1, text="|")
                ram_usage_bar.pack()

                ram_usage_value_frame = tk.Frame(ram_usage_frame, bg=bg)
                ram_usage_value_frame.place(
                    relwidth=0.30, relheight=0.2, relx=0.684, rely=0.426)

                ram_usage_value_label = tk.Label(
                    ram_usage_value_frame, bg=bg, fg=fg, font=font, anchor=tk.E, width=40, height=15, text="0GB/0GB")
                ram_usage_value_label.pack()

                bar.update(10)

                # RAM Free memory

                ram_free_frame = tk.Frame(ram_frame, bg=bg)
                ram_free_frame.place(
                    relwidth=0.49, relheight=0.19, relx=0, rely=0.21)

                ram_free_label_frame = tk.Frame(ram_free_frame, bg=bg)
                ram_free_label_frame.place(
                    relwidth=0.30, relheight=0.15, relx=0.02, rely=0.08)

                ram_free_label = tk.Label(ram_free_label_frame, bg=bg, fg=fg,
                                          font=font, anchor=tk.W, width=100, height=10, text="RAM (FREE)")
                ram_free_label.pack()

                ram_free_container = tk.Frame(ram_free_frame, bg=bg)
                ram_free_container.place(
                    relwidth=0.963, relheight=0.5, relx=0.018, rely=0.426)

                ram_free = tk.Label(ram_free_container, bg=bg, fg=fg, font=font,
                                    anchor=tk.W, width=100, height=1, text="Total Free")
                ram_free.pack()

                ram_free_bar = tk.Label(ram_free_container, bg=bg, fg=fg,
                                        font=font, anchor=tk.W, width=100, height=1, text="|")
                ram_free_bar.pack()

                ram_free_value_frame = tk.Frame(ram_free_frame, bg=bg)
                ram_free_value_frame.place(
                    relwidth=0.30, relheight=0.2, relx=0.684, rely=0.426)

                ram_free_value_label = tk.Label(
                    ram_free_value_frame, bg=bg, fg=fg, font=font, anchor=tk.E, width=40, height=15, text="0GB")
                ram_free_value_label.pack()

                bar.update(10)

                # RAM Max usage

                ram_max_usage_frame = tk.Frame(ram_frame, bg=bg)
                ram_max_usage_frame.place(
                    relwidth=0.49, relheight=0.19, relx=0, rely=0.42)

                ram_max_usage_label_frame = tk.Frame(
                    ram_max_usage_frame, bg=bg)
                ram_max_usage_label_frame.place(
                    relwidth=0.30, relheight=0.15, relx=0.02, rely=0.08)

                ram_max_usage_label = tk.Label(ram_max_usage_label_frame, bg=bg, fg=fg,
                                               font=font, anchor=tk.W, width=100, height=10, text="RAM (MAX)")
                ram_max_usage_label.pack()

                ram_max_usage_container = tk.Frame(ram_max_usage_frame, bg=bg)
                ram_max_usage_container.place(
                    relwidth=0.963, relheight=0.5, relx=0.018, rely=0.426)

                ram_max_usage = tk.Label(ram_max_usage_container, bg=bg, fg=fg, font=font,
                                         anchor=tk.W, width=100, height=1, text="Max Usage")
                ram_max_usage.pack()

                ram_max_usage_bar = tk.Label(ram_max_usage_container, bg=bg, fg=fg,
                                             font=font, anchor=tk.W, width=100, height=1, text="|")
                ram_max_usage_bar.pack()

                ram_max_usage_value_frame = tk.Frame(
                    ram_max_usage_frame, bg=bg)
                ram_max_usage_value_frame.place(
                    relwidth=0.30, relheight=0.2, relx=0.684, rely=0.426)

                ram_max_usage_value_label = tk.Label(
                    ram_max_usage_value_frame, bg=bg, fg=fg, font=font, anchor=tk.E, width=40, height=15, text="0GB")
                ram_max_usage_value_label.pack()

                bar.update(10)

                # SWAP Memory usage (if it exists)

                swap_memory_usage_frame = tk.Frame(ram_frame, bg=bg)
                swap_memory_usage_frame.place(
                    relwidth=0.49, relheight=0.19, relx=0.505, rely=0)

                swap_usage_label_frame = tk.Frame(
                    swap_memory_usage_frame, bg=bg)
                swap_usage_label_frame.place(
                    relwidth=0.45, relheight=0.15, relx=0.02, rely=0.08)

                swap_usage_label = tk.Label(swap_usage_label_frame, bg=bg, fg=fg, font=font,
                                            anchor=tk.W, width=100, height=10, text="SWAP MEMORY USAGE")
                swap_usage_label.pack()

                swap_usage_container = tk.Frame(swap_memory_usage_frame, bg=bg)
                swap_usage_container.place(
                    relwidth=0.963, relheight=0.5, relx=0.018, rely=0.426)

                swap_usage = tk.Label(swap_usage_container, bg=bg, fg=fg, font=font,
                                      anchor=tk.W, width=100, height=1, text="Total Usage")
                swap_usage.pack()

                swap_usage_bar = tk.Label(swap_usage_container, bg=bg, fg=fg,
                                          font=font, anchor=tk.W, width=100, height=1, text="|")
                swap_usage_bar.pack()

                swap_usage_value_frame = tk.Frame(
                    swap_memory_usage_frame, bg=bg)
                swap_usage_value_frame.place(
                    relwidth=0.3, relheight=0.2, relx=0.684, rely=0.426)

                swap_usage_value = tk.Label(swap_usage_value_frame, bg=bg, fg=fg,
                                            font=font, anchor=tk.E, width=40, height=15, text="0GB/0GB")
                swap_usage_value.pack()

                bar.update(10)

                # SWAP free memory

                swap_memory_free_frame = tk.Frame(ram_frame, bg=bg)
                swap_memory_free_frame.place(
                    relwidth=0.49, relheight=0.19, relx=0.505, rely=0.21)

                swap_free_label_frame = tk.Frame(swap_memory_free_frame, bg=bg)
                swap_free_label_frame.place(
                    relwidth=0.45, relheight=0.15, relx=0.02, rely=0.08)

                swap_free_label = tk.Label(swap_free_label_frame, bg=bg, fg=fg, font=font,
                                           anchor=tk.W, width=100, height=10, text="SWAP (FREE)")
                swap_free_label.pack()

                swap_free_container = tk.Frame(swap_memory_free_frame, bg=bg)
                swap_free_container.place(
                    relwidth=0.963, relheight=0.5, relx=0.018, rely=0.426)

                swap_free = tk.Label(swap_free_container, bg=bg, fg=fg, font=font,
                                     anchor=tk.W, width=100, height=1, text="Total Free")
                swap_free.pack()

                swap_free_bar = tk.Label(swap_free_container, bg=bg, fg=fg,
                                         font=font, anchor=tk.W, width=100, height=1, text="|")
                swap_free_bar.pack()

                swap_free_value_frame = tk.Frame(swap_memory_free_frame, bg=bg)
                swap_free_value_frame.place(
                    relwidth=0.3, relheight=0.2, relx=0.684, rely=0.426)

                swap_free_value = tk.Label(swap_free_value_frame, bg=bg, fg=fg,
                                           font=font, anchor=tk.E, width=40, height=15, text="0GB")
                swap_free_value.pack()

                bar.update(10)

                # SWAP Max usage

                swap_memory_max_frame = tk.Frame(ram_frame, bg=bg)
                swap_memory_max_frame.place(
                    relwidth=0.49, relheight=0.19, relx=0.505, rely=0.42)

                swap_max_usage_label_frame = tk.Frame(
                    swap_memory_max_frame, bg=bg)
                swap_max_usage_label_frame.place(
                    relwidth=0.45, relheight=0.15, relx=0.02, rely=0.08)

                swap_max_usage_label = tk.Label(swap_max_usage_label_frame, bg=bg, fg=fg, font=font,
                                                anchor=tk.W, width=100, height=10, text="SWAP (MAX)")
                swap_max_usage_label.pack()

                swap_max_usage_container = tk.Frame(
                    swap_memory_max_frame, bg=bg)
                swap_max_usage_container.place(
                    relwidth=0.963, relheight=0.5, relx=0.018, rely=0.426)

                swap_max_usage = tk.Label(swap_max_usage_container, bg=bg, fg=fg, font=font,
                                          anchor=tk.W, width=100, height=1, text="Max Usage")
                swap_max_usage.pack()

                swap_max_usage_bar = tk.Label(swap_max_usage_container, bg=bg, fg=fg,
                                              font=font, anchor=tk.W, width=100, height=1, text="|")
                swap_max_usage_bar.pack()

                swap_max_usage_value_frame = tk.Frame(
                    swap_memory_max_frame, bg=bg)
                swap_max_usage_value_frame.place(
                    relwidth=0.3, relheight=0.2, relx=0.684, rely=0.426)

                swap_max_usage_value = tk.Label(swap_max_usage_value_frame, bg=bg, fg=fg,
                                                font=font, anchor=tk.E, width=40, height=15, text="0GB")
                swap_max_usage_value.pack()

                bar.update(50)

                loading.pack_forget()

                refresh_ram()
        dec_ram = root.after(5, declare_ram)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# refresh_ram function refreshes ram and swap memory information every x amount of miliseconds

try:
    def refresh_ram():
        global ram_ref
        vmem = psutil.virtual_memory()
        swapmem = psutil.swap_memory()

        # Update ram usage

        try:
            ram_usage_value_label.configure(
                text=f"{get_size(vmem.used)}/{get_size(vmem.total)}")
            usg_perc = (vmem.used / vmem.total) * 100
            usg_perc_optimized = usg_perc / 1.65
            ram_usage_bar.configure(text="|"*int(usg_perc_optimized))
            if vmem.used not in ram_max_usage_list:
                if not ram_max_usage_list:
                    ram_max_usage_list.append(vmem.used)
                if vmem.used > max(ram_max_usage_list):
                    ram_max_usage_list.append(vmem.used)
                else:
                    pass
            else:
                pass
        except Exception as e:
            print(e)

        # Update free memory

        try:
            ram_free_value_label.configure(text=f"{get_size(vmem.free)}")
            free_perc = (vmem.free / vmem.total) * 100
            free_perc_optimized = free_perc / 1.65
            ram_free_bar.configure(text="|"*int(free_perc_optimized))
        except Exception as e:
            print(e)

        # Update max usage

        try:
            ram_max_usage_value_label.configure(
                text=f"{get_size(max(ram_max_usage_list))}")
            max_perc = (max(ram_max_usage_list) / vmem.total) * 100
            max_perc_optimized = max_perc / 1.65
            ram_max_usage_bar.configure(text="|"*int(max_perc_optimized))
        except Exception as e:
            print(e)

        # Update swap usage

        try:
            swap_usage_value.configure(
                text=f"{get_size(swapmem.used)}/{get_size(swapmem.total)}")
            sw_usg_perc = (swapmem.used / swapmem.total) * 100
            sw_usg_perc_optimized = sw_usg_perc / 1.65
            swap_usage_bar.configure(text="|"*int(sw_usg_perc_optimized))
            if swapmem.used not in swap_max_usage_list:
                if not swap_max_usage_list:
                    swap_max_usage_list.append(swapmem.used)
                if swapmem.used > max(swap_max_usage_list):
                    swap_max_usage_list.append(swapmem.used)
                else:
                    pass
            else:
                pass
        except Exception as e:
            print(e)

        # Update swap free

        try:
            swap_free_value.configure(text=f"{get_size(swapmem.free)}")
            sw_free_perc = (swapmem.free / swapmem.total) * 100
            sw_free_perc_optimized = sw_free_perc / 1.65
            swap_free_bar.configure(text="|"*int(sw_free_perc_optimized))
        except Exception as e:
            print(e)

        # Update swap maximum usage

        try:
            swap_max_usage_value.configure(
                text=f"{get_size(max(swap_max_usage_list))}")
            sw_max_perc = (max(swap_max_usage_list) / swapmem.total) * 100
            sw_max_perc_optimized = sw_max_perc / 1.65
            swap_max_usage_bar.configure(text="|"*int(sw_max_perc_optimized))
        except Exception as e:
            print(e)

        # Adjust colors

        try:
            # Adjusting colors for RAM usages
            if usg_perc < 50:
                ram_usage_bar.configure(fg=asm_cyan)
            if usg_perc > 50 and usg_perc < 70:
                ram_usage_bar.configure(fg=asm_yellow)
            if usg_perc > 70 and usg_perc < 90:
                ram_usage_bar.configure(fg=asm_orange)
            if usg_perc > 90:
                ram_usage_bar.configure(fg=asm_red)

            # Adjusting colors for MAX RAM usage
            if max_perc < 50:
                ram_max_usage_bar.configure(fg=asm_cyan)
            if max_perc > 50 and max_perc < 70:
                ram_max_usage_bar.configure(fg=asm_yellow)
            if max_perc > 70 and max_perc < 90:
                ram_max_usage_bar.configure(fg=asm_orange)
            if max_perc > 90:
                ram_max_usage_bar.configure(fg=asm_red)

            # Adjust colors for free memory
            if free_perc >= 50:
                ram_free_bar.configure(fg=asm_cyan)
            if free_perc < 50 and free_perc > 30:
                ram_free_bar.configure(fg=asm_yellow)
            if free_perc < 30 and free_perc > 10:
                ram_free_bar.configure(fg=asm_orange)
            if free_perc < 10:
                ram_free_bar.configure(fg=asm_red)

        except Exception as e:
            print(e)

        try:
            # Adjusting colors for SWAP memory
            if sw_usg_perc < 50:
                swap_usage_bar.configure(fg=asm_cyan)
            if sw_usg_perc > 50 and sw_usg_perc < 70:
                swap_usage_bar.configure(fg=asm_yellow)
            if sw_usg_perc > 70 and sw_usg_perc < 90:
                swap_usage_bar.configure(fg=asm_orange)
            if sw_usg_perc > 90:
                swap_usage_bar.configure(fg=asm_red)

            # Adjusting colors for MAX SWAP memory usage
            if sw_max_perc < 50:
                swap_max_usage_bar.configure(fg=asm_cyan)
            if sw_max_perc > 50 and sw_max_perc < 70:
                swap_max_usage_bar.configure(fg=asm_yellow)
            if sw_max_perc > 70 and sw_max_perc < 90:
                swap_max_usage_bar.configure(fg=asm_orange)
            if sw_max_perc > 90:
                swap_max_usage_bar.configure(fg=asm_red)

            # Adjust colors for free swap memory

            if free_perc >= 50:
                swap_free_bar.configure(fg=asm_cyan)
            if free_perc < 50 and free_perc > 30:
                swap_free_bar.configure(fg=asm_yellow)
            if free_perc < 30 and free_perc > 10:
                swap_free_bar.configure(fg=asm_orange)
            if free_perc < 10:
                swap_free_bar.configure(fg=asm_red)

        except Exception as e:
            print(e)

        ram_ref = root.after(1000, refresh_ram)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# Drives function gets all available partitions and shows their usage and free space

try:
    def drives():
        global drive_frame
        # Remove any previous opened windows and change button background
        try:
            hddButton.configure(bg=button_bg)
        except Exception as e:
            print(e)

        try:
            combined_test_frame.place_forget()
            root.after_cancel(rct)
        except Exception as e:
            print(e)

        try:
            homeButton.configure(bg=sidemenu_bg)
            root.after_cancel(time)
            root.after_cancel(ff)
            home_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            cpuButton.configure(bg=sidemenu_bg)
            root.after_cancel(ref)
            cpu_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            motherboardButton.configure(bg=sidemenu_bg)
            main_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            ramButton.configure(bg=sidemenu_bg)
            root.after_cancel(ram_ref)
            ram_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            gpuButton.configure(bg=sidemenu_bg)
            root.after_cancel(gpu_update)
            gpu_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            netButton.configure(bg=sidemenu_bg)
            root.after_cancel(net_ref)
            network_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            fanButton.configure(bg=sidemenu_bg)
            root.after_cancel(fan_ref)
            fans_frame.place_forget()
        except Exception as e:
            print(e)

        drive_frame = tk.Frame(root, bg=canvas_bg)
        drive_frame.place(relwidth=0.875, relheight=0.96,
                          relx=0.117, rely=0.021)

        refresh_drives()
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# refresh_drives function refreshes partition data every x amount of seconds

try:
    def refresh_drives():
        global drive_ref
        partitions = psutil.disk_partitions()
        x = 0
        y = 0
        total_space = 0
        used_space = 0

        for part in partitions:
            try:
                partition_usage = psutil.disk_usage(part.mountpoint)
            except Exception as e:
                print(e)

            usage_perc = (partition_usage.used / partition_usage.total) * 100

            usage_perc_optimized = usage_perc / 1.65

            disk = tk.Frame(drive_frame, bg=bg)
            disk.place(relwidth=0.49, relheight=0.19, relx=x, rely=y)

            partition_name_frame = tk.Frame(disk, bg=bg)
            partition_name_frame.place(
                relwidth=0.45, relheight=0.15, relx=0.02, rely=0.08)

            partition_name = tk.Label(partition_name_frame, bg=bg, fg=fg, font=font,
                                      anchor=tk.W, width=100, height=10, text=f"Paritition: {part.mountpoint}")
            partition_name.pack()

            space_usage_container = tk.Frame(disk, bg=bg)
            space_usage_container.place(
                relwidth=0.963, relheight=0.5, relx=0.018, rely=0.426)

            space_usage = tk.Label(space_usage_container, bg=bg, fg=fg,
                                   font=font, anchor=tk.W, width=100, height=1, text="Usage")
            space_usage.pack()

            space_usage_bar = tk.Label(space_usage_container, bg=bg, fg=fg,
                                       font=font, anchor=tk.W, width=100, height=1, text="|"*int(usage_perc_optimized))
            space_usage_bar.pack()

            space_usage_value_frame = tk.Frame(disk, bg=bg)
            space_usage_value_frame.place(
                relwidth=0.40, relheight=0.2, relx=0.59, rely=0.426)

            space_usage_value = tk.Label(space_usage_value_frame, bg=bg, fg=fg,
                                         font=font, anchor=tk.E, width=40, height=15, text=f"{get_size(partition_usage.used)}/{get_size(partition_usage.total)}")
            space_usage_value.pack()

            if usage_perc < 50:
                space_usage_bar.configure(fg=asm_cyan)
            elif usage_perc > 50 and usage_perc < 70:
                space_usage_bar.configure(fg=asm_yellow)
            elif usage_perc > 70 and usage_perc < 90:
                space_usage_bar.configure(fg=asm_orange)
            elif usage_perc > 90:
                space_usage_bar.configure(fg=asm_red)

            if x == 0:
                x = 0.505
            elif x == 0.505:
                x = 0
                y += 0.21

            total_space += partition_usage.total
            used_space += partition_usage.used

        total_size_frame = tk.Frame(drive_frame, bg=bg)
        total_size_frame.place(relwidth=0.49, relheight=0.19, relx=x, rely=y)

        total_size_label_frame = tk.Frame(total_size_frame, bg=bg)
        total_size_label_frame.place(
            relwidth=0.45, relheight=0.15, relx=0.02, rely=0.08)

        total_size_label = tk.Label(total_size_label_frame, bg=bg, fg=fg,
                                    font=font, anchor=tk.W, width=100, height=10, text="TOTAL SIZE")
        total_size_label.pack()

        total_size_container = tk.Frame(total_size_frame, bg=bg)
        total_size_container.place(
            relwidth=0.963, relheight=0.5, relx=0.018, rely=0.426)

        total_size = tk.Label(total_size_container, bg=bg, fg=fg, font=font,
                              anchor=tk.W, width=100, height=1, text="Total Size")
        total_size.pack()

        sp_per = (used_space / total_space) * 100
        sp_per_optimized = sp_per / 1.65

        total_size_bar = tk.Label(total_size_container, bg=bg, fg=fg,
                                  font=font, anchor=tk.W, width=100, height=1, text="|"*int(sp_per_optimized))
        total_size_bar.pack()

        total_size_value_frame = tk.Frame(total_size_frame, bg=bg)
        total_size_value_frame.place(
            relwidth=0.4, relheight=0.2, relx=0.59, rely=0.426)

        total_size_value = tk.Label(total_size_value_frame, bg=bg, fg=fg,
                                    font=font, anchor=tk.E, width=40, height=15, text=f"{get_size(used_space)}/{get_size(total_space)}")
        total_size_value.pack()

        if sp_per < 50:
            total_size_bar.configure(fg=asm_cyan)
        if sp_per > 50 and sp_per < 70:
            total_size_bar.configure(fg=asm_yellow)
        if sp_per > 80 and sp_per < 90:
            total_size_bar.configure(fg=asm_orange)
        if sp_per > 90:
            total_size_bar.configure(fg=asm_red)

        drive_ref = root.after(10000, refresh_drives)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# fans function sets up basic frame and closes all previous processes

try:
    def fans():
        global fans_frame

        # Remove any previously opened windows and change button background

        try:
            fanButton.configure(bg=button_bg)
        except Exception as e:
            print(e)

        try:
            combined_test_frame.place_forget()
            root.after_cancel(rct)
        except Exception as e:
            print(e)

        try:
            homeButton.configure(bg=sidemenu_bg)
            root.after_cancel(time)
            root.after_cancel(ff)
            home_frame.place_forget()
        except Exception as e:
            print(e)
        try:
            cpuButton.configure(bg=sidemenu_bg)
            root.after_cancel(ref)
            cpu_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            gpuButton.configure(bg=sidemenu_bg)
            root.after_cancel(gpu_update)
            gpu_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            motherboardButton.configure(bg=sidemenu_bg)
            main_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            ramButton.configure(bg=sidemenu_bg)
            root.after_cancel(ram_ref)
            ram_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            hddButton.configure(bg=sidemenu_bg)
            root.after_cancel(drive_ref)
            drive_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            netButton.configure(bg=sidemenu_bg)
            root.after_cancel(net_ref)
            network_frame.place_forget()
        except Exception as e:
            print(e)

        fans_frame = tk.Frame(root, bg=canvas_bg)
        fans_frame.place(relwidth=0.875, relheight=0.96,
                         relx=0.117, rely=0.021)

        refresh_fans()
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# refresh_fans finds all the fans connected to the system, displays and refreshes them every x amount of miliseconds

try:
    def refresh_fans():
        global fan_ref
        x = 0
        y = 0

        try:
            f = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
            fan_info = f.Sensor()
            for sensor in fan_info:
                if sensor.SensorType == u"Fan":
                    fan_frame = tk.Frame(fans_frame, bg=bg)
                    fan_frame.place(
                        relwidth=0.49, relheight=0.19, relx=x, rely=y)

                    fan_label_frame = tk.Frame(fan_frame, bg=bg)
                    fan_label_frame.place(
                        relwidth=0.45, relheight=0.15, relx=0.02, rely=0.08)

                    fan_label = tk.Label(fan_label_frame, bg=bg, fg=fg, font=font,
                                         anchor=tk.W, width=100, height=10, text=f"{sensor.Name}")
                    fan_label.pack()

                    fan_speed_container = tk.Frame(fan_frame, bg=bg)
                    fan_speed_container.place(
                        relwidth=0.963, relheight=0.5, relx=0.018, rely=0.426)

                    fan_speed = tk.Label(fan_speed_container, bg=bg, fg=fg,
                                         font=font, anchor=tk.W, width=100, height=1, text="Fan RPM")
                    fan_speed.pack()

                    # Program has no way of determining the maximum fan speed therefore it assumes that the maximum is 5000 RPM

                    speed_perc = (sensor.Value / 5000) * 100
                    speed_perc_optimized = speed_perc / 1.65

                    fan_speed_bar = tk.Label(fan_speed_container, bg=bg, fg=fg, font=font,
                                             anchor=tk.W, width=100, height=1, text="|"*int(speed_perc_optimized))
                    fan_speed_bar.pack()

                    fan_speed_value_frame = tk.Frame(fan_frame, bg=bg)
                    fan_speed_value_frame.place(
                        relwidth=0.40, relheight=0.2, relx=0.59, rely=0.426)

                    fan_speed_value = tk.Label(fan_speed_value_frame, bg=bg, fg=fg, font=font,
                                               anchor=tk.E, width=40, height=15, text=f"{sensor.Value:.0f} RPM")
                    fan_speed_value.pack()

                    if x == 0:
                        x = 0.505
                    elif x == 0.505:
                        y += 0.21
                        x = 0

                    if speed_perc < 50:
                        fan_speed_bar.configure(fg=asm_cyan)
                    elif speed_perc > 50 and speed_perc < 70:
                        fan_speed_bar.configure(fg=asm_yellow)
                    elif speed_perc > 70 and speed_perc < 90:
                        fan_speed_bar.configure(fg=asm_orange)
                    elif speed_perc > 90:
                        fan_speed_bar.configure(fg=asm_red)

        except Exception as e:
            print(e)

        fan_ref = root.after(1000, refresh_fans)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# network function sets up frames and labels for various network information and removes previously active services

try:
    def network():
        global network_frame
        global total_sent_bar
        global total_sent_value
        global total_rec_bar
        global total_rec_value
        global ping_value
        global download_value
        global upload_value
        global best_ping_value
        global best_download_value
        global best_upload_value

        # Remove any previously opened windows and change button background

        try:
            netButton.configure(bg=button_bg)
        except Exception as e:
            print(e)

        try:
            combined_test_frame.place_forget()
            root.after_cancel(rct)
        except Exception as e:
            print(e)

        try:
            homeButton.configure(bg=sidemenu_bg)
            root.after_cancel(time)
            root.after_cancel(ff)
            home_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            cpuButton.configure(bg=sidemenu_bg)
            root.after_cancel(ref)
            cpu_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            gpuButton.configure(bg=sidemenu_bg)
            root.after_cancel(gpu_update)
            gpu_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            motherboardButton.configure(bg=sidemenu_bg)
            main_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            ramButton.configure(bg=sidemenu_bg)
            root.after_cancel(ram_ref)
            ram_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            hddButton.configure(bg=sidemenu_bg)
            root.after_cancel(drive_ref)
            drive_frame.place_forget()
        except Exception as e:
            print(e)

        try:
            fanButton.configure(bg=sidemenu_bg)
            root.after_cancel(fan_ref)
            fans_frame.place_forget()
        except Exception as e:
            print(e)

        # Main network frame containing all elements

        network_frame = tk.Frame(root, bg=canvas_bg)
        network_frame.place(relwidth=0.875, relheight=0.96,
                            relx=0.117, rely=0.021)

        # Ping information

        ping_frame = tk.Frame(network_frame, bg=bg)
        ping_frame.place(relwidth=0.32, relheight=0.32, relx=0, rely=0)

        if not ping_list:
            ping_label = tk.Label(ping_frame, bg=bg, fg=fg, font=net_font,
                                  anchor=tk.CENTER, width=17, height=1, text=f"PING")
            ping_label.grid(row=0, column=0, padx=0, pady=(57, 0))

            ping_value = tk.Label(ping_frame, bg=bg, fg=fg, font=net_font,
                                  anchor=tk.CENTER, width=17, height=1, text=f"0ms")
            ping_value.grid(row=1, column=0, padx=0, pady=(35, 0))
        else:
            ping_label = tk.Label(ping_frame, bg=bg, fg=fg, font=net_font,
                                  anchor=tk.CENTER, width=17, height=1, text=f"PING")
            ping_label.grid(row=0, column=0, padx=0, pady=(57, 0))

            ping_value = tk.Label(ping_frame, bg=bg, fg=ping_color, font=net_font,
                                  anchor=tk.CENTER, width=17, height=1, text=f"{max(ping_list)}ms")
            ping_value.grid(row=1, column=0, padx=0, pady=(35, 0))

        # Download speed

        download_frame = tk.Frame(network_frame, bg=bg)
        download_frame.place(
            relwidth=0.32, relheight=0.32, relx=0.3375, rely=0)

        if not download_list:
            download_label = tk.Label(download_frame, bg=bg, fg=fg, font=net_font,
                                      anchor=tk.CENTER, width=17, height=1, text=f"DOWNLOAD")
            download_label.grid(row=0, column=0, padx=0, pady=(57, 0))

            download_value = tk.Label(download_frame, bg=bg, fg=fg, font=net_font,
                                      anchor=tk.CENTER, width=17, height=1, text=f"0Mbps")
            download_value.grid(row=1, column=0, padx=0, pady=(35, 0))
        else:
            download_label = tk.Label(download_frame, bg=bg, fg=fg, font=net_font,
                                      anchor=tk.CENTER, width=17, height=1, text=f"DOWNLOAD")
            download_label.grid(row=0, column=0, padx=0, pady=(57, 0))

            download_value = tk.Label(download_frame, bg=bg, fg=download_color, font=net_font,
                                      anchor=tk.CENTER, width=17, height=1, text=f"{max(download_list)}Mbps")
            download_value.grid(row=1, column=0, padx=0, pady=(35, 0))

        # Upload speed

        upload_frame = tk.Frame(network_frame, bg=bg)
        upload_frame.place(relwidth=0.32, relheight=0.32, relx=0.675, rely=0)

        if not upload_list:
            upload_label = tk.Label(upload_frame, bg=bg, fg=fg, font=net_font,
                                    anchor=tk.CENTER, width=17, height=1, text=f"UPLOAD")
            upload_label.grid(row=0, column=0, padx=0, pady=(57, 0))

            upload_value = tk.Label(upload_frame, bg=bg, fg=fg, font=net_font,
                                    anchor=tk.CENTER, width=17, height=1, text=f"0Mbps")
            upload_value.grid(row=1, column=0, padx=0, pady=(35, 0))
        else:
            upload_label = tk.Label(upload_frame, bg=bg, fg=fg, font=net_font,
                                    anchor=tk.CENTER, width=17, height=1, text=f"UPLOAD")
            upload_label.grid(row=0, column=0, padx=0, pady=(57, 0))

            upload_value = tk.Label(upload_frame, bg=bg, fg=upload_color, font=net_font,
                                    anchor=tk.CENTER, width=17, height=1, text=f"{max(upload_list)}Mbps")
            upload_value.grid(row=1, column=0, padx=0, pady=(35, 0))

        # Network interfaces

        interfaces_frame = tk.Frame(network_frame, bg=bg)
        interfaces_frame.place(
            relwidth=0.49, relheight=0.66, relx=0, rely=0.34)

        interface_label_frame = tk.Frame(interfaces_frame, bg=bg)
        interface_label_frame.place(
            relwidth=0.45, relheight=0.05, relx=0.02, rely=0.02)

        interface_label = tk.Label(interface_label_frame, bg=bg, fg=fg,
                                   font=font, anchor=tk.W, width=100, height=1, text="INTERFACES")
        interface_label.pack()

        interface_container = tk.Frame(interfaces_frame, bg=bg)
        interface_container.place(relwidth=1, relheight=0.9, relx=0, rely=0.1)

        if_addrs = psutil.net_if_addrs()

        column = 0
        row = 0
        padx = 10
        pady = 5

        for interface_name, interface_addresses, in if_addrs.items():
            for address in interface_addresses:
                intfc_name = tk.Label(interface_container, bg=bg, fg=fg, font=font, anchor=tk.W,
                                      width=100, height=1, text=f"Interface Name: {interface_name}")
                intfc_name.grid(row=row, column=column, padx=padx, pady=pady)
                row += 1
                if str(address.family) == 'AddressFamily.AF_INET':
                    ip_addrs = tk.Label(interface_container, bg=bg, fg=fg, font=font, anchor=tk.W,
                                        width=100, height=1, text=f"IP Address: {address.address}")
                    ip_addrs.grid(row=row, column=column, padx=padx, pady=pady)
                    row += 1

                    net_mask = tk.Label(interface_container, bg=bg, fg=fg, font=font,
                                        anchor=tk.W, width=100, height=1, text=f"Netmask: {address.netmask}")
                    net_mask.grid(row=row, column=column, padx=padx, pady=pady)
                    row += 1

                    brdcast_ip = tk.Label(interface_container, bg=bg, fg=fg, font=font, anchor=tk.W,
                                          width=100, height=1, text=f"Broadcast IP: {address.broadcast}")
                    brdcast_ip.grid(row=row, column=column,
                                    padx=padx, pady=pady)
                    row += 1
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    mac_addrs = tk.Label(interface_container, bg=bg, fg=fg, font=font, anchor=tk.W,
                                         width=100, height=1, text=f"MAC Address: {address.address}")
                    mac_addrs.grid(row=row, column=column,
                                   padx=padx, pady=pady)
                    row += 1

                    net_mask = tk.Label(interface_container, bg=bg, fg=fg, font=font,
                                        anchor=tk.W, width=100, height=1, text=f"Netmask: {address.netmask}")
                    net_mask.grid(row=row, column=column, padx=padx, pady=pady)
                    row += 1

                    brdcast_mac = tk.Label(interface_container, bg=bg, fg=fg, font=font, anchor=tk.W,
                                           width=100, height=1, text=f"Broadcast MAC: {address.broadcast}")
                    brdcast_mac.grid(row=row, column=column,
                                     padx=padx, pady=pady)
                    row += 1

        # IO statistics since boot
        net_io = psutil.net_io_counters

        # SENT

        bytes_sent = tk.Frame(network_frame, bg=bg)
        bytes_sent.place(relwidth=0.49, relheight=0.20667,
                         relx=0.505, rely=0.34)

        bytes_sent_label_frame = tk.Frame(bytes_sent, bg=bg)
        bytes_sent_label_frame.place(
            relwidth=0.45, relheight=0.15, relx=0.02, rely=0.07)

        bytes_sent_label = tk.Label(
            bytes_sent_label_frame, bg=bg, fg=fg, font=font, anchor=tk.W, width=100, height=10, text="SENT")
        bytes_sent_label.pack()

        bytes_sent_container = tk.Frame(bytes_sent, bg=bg)
        bytes_sent_container.place(
            relwidth=0.963, relheight=0.5, relx=0.018, rely=0.46)

        total_sent = tk.Label(bytes_sent_container, bg=bg, fg=fg, font=font,
                              anchor=tk.W, width=100, height=1, text="Total Bytes Sent")
        total_sent.pack()

        total_sent_bar = tk.Label(bytes_sent_container, bg=bg, fg=fg,
                                  font=font, anchor=tk.W, width=100, height=1, text="|")
        total_sent_bar.pack()

        total_sent_value_frame = tk.Frame(bytes_sent, bg=bg)
        total_sent_value_frame.place(
            relwidth=0.40, relheight=0.2, relx=0.59, rely=0.46)

        total_sent_value = tk.Label(total_sent_value_frame, bg=bg, fg=fg,
                                    font=font, anchor=tk.E, width=40, height=15, text="0 MB")
        total_sent_value.pack()

        # RECEIVED

        bytes_received = tk.Frame(network_frame, bg=bg)
        bytes_received.place(relwidth=0.49, relheight=0.20667,
                             relx=0.505, rely=0.56667)

        bytes_rec_label_frame = tk.Frame(bytes_received, bg=bg)
        bytes_rec_label_frame.place(
            relwidth=0.45, relheight=0.15, relx=0.02, rely=0.07)

        bytes_rec_label = tk.Label(
            bytes_rec_label_frame, bg=bg, fg=fg, font=font, anchor=tk.W, width=100, height=10, text="RECEIVED")
        bytes_rec_label.pack()

        bytes_rec_container = tk.Frame(bytes_received, bg=bg)
        bytes_rec_container.place(
            relwidth=0.963, relheight=0.5, relx=0.018, rely=0.46)

        total_rec = tk.Label(bytes_rec_container, bg=bg, fg=fg, font=font,
                             anchor=tk.W, width=100, height=1, text="Total Bytes Received")
        total_rec.pack()

        total_rec_bar = tk.Label(bytes_rec_container, bg=bg, fg=fg,
                                 font=font, anchor=tk.W, width=100, height=1, text="|")
        total_rec_bar.pack()

        total_rec_value_frame = tk.Frame(bytes_received, bg=bg)
        total_rec_value_frame.place(
            relwidth=0.40, relheight=0.2, relx=0.59, rely=0.46)

        total_rec_value = tk.Label(total_rec_value_frame, bg=bg, fg=fg,
                                   font=font, anchor=tk.E, width=40, height=15, text="0 MB")
        total_rec_value.pack()

        # SPEEDTEST button

        speedtest_frame = tk.Frame(network_frame, bg=bg)
        speedtest_frame.place(relwidth=0.12, relheight=0.20667,
                              relx=0.505, rely=0.79334)

        speedtest_button = tk.Button(speedtest_frame, bg=bg, fg=fg, font=font, width=30, height=7, text="SPEEDTEST",
                                     bd=0, activebackground=button_bg, activeforeground="white", command=get_speed)
        speedtest_button.pack()
        # Maximum speedtest results

        speed_test_max = tk.Frame(network_frame, bg=bg)
        speed_test_max.place(relwidth=0.355, relheight=0.20667,
                             relx=0.64, rely=0.79334)

        speed_test_max_text_frame = tk.Frame(speed_test_max, bg=bg)
        speed_test_max_text_frame.place(
            relwidth=0.5, relheight=0.15, relx=0.02, rely=0.06)

        speed_test_max_text = tk.Label(speed_test_max_text_frame, bg=bg, fg=fg,
                                       font=font, anchor=tk.W, width=100, height=1, text="BEST RESULTS")
        speed_test_max_text.pack()

        speed_test_results_container = tk.Frame(speed_test_max, bg=bg)
        speed_test_results_container.place(
            relwidth=1, relheight=0.5, relx=0, rely=0.35)

        if not ping_list:
            best_ping = tk.Label(speed_test_results_container, bg=bg, fg=fg,
                                 font=font, anchor=tk.CENTER, width=8, height=1, text="PING")
            best_ping.grid(row=0, column=0, padx=(5), pady=(5, 0))
            best_ping_value = tk.Label(speed_test_results_container, bg=bg, fg=fg,
                                       font=font, anchor=tk.CENTER, width=8, height=1, text="0ms")
            best_ping_value.grid(row=1, column=0, padx=(5), pady=(0))
        else:
            best_ping = tk.Label(speed_test_results_container, bg=bg, fg=fg,
                                 font=font, anchor=tk.CENTER, width=10, height=1, text="PING")
            best_ping.grid(row=0, column=0, padx=(5), pady=(5, 0))
            best_ping_value = tk.Label(speed_test_results_container, bg=bg, fg=fg,
                                       font=font, anchor=tk.CENTER, width=10, height=1, text=f"{min(ping_list)}ms")
            best_ping_value.grid(row=1, column=0, padx=(5), pady=(0))

        if not download_list:
            best_download = tk.Label(speed_test_results_container, bg=bg, fg=fg,
                                     font=font, anchor=tk.CENTER, width=11, height=1, text="DOWNLOAD")
            best_download.grid(row=0, column=1, padx=(5), pady=(5, 0))
            best_download_value = tk.Label(speed_test_results_container, bg=bg,
                                           fg=fg, font=font, anchor=tk.CENTER, width=11, height=1, text="0Mbps")
            best_download_value.grid(row=1, column=1, padx=(5), pady=(0))
        else:
            best_download = tk.Label(speed_test_results_container, bg=bg, fg=fg,
                                     font=font, anchor=tk.CENTER, width=10, height=1, text="DOWNLOAD")
            best_download.grid(row=0, column=1, padx=(5), pady=(5, 0))
            best_download_value = tk.Label(speed_test_results_container, bg=bg,
                                           fg=fg, font=font, anchor=tk.CENTER, width=10, height=1, text=f"{max(download_list)}Mbps")
            best_download_value.grid(row=1, column=1, padx=(5), pady=(0))

        if not upload_list:
            best_upload = tk.Label(speed_test_results_container, bg=bg, fg=fg,
                                   font=font, anchor=tk.CENTER, width=10, height=1, text="UPLOAD")
            best_upload.grid(row=0, column=2, padx=(5), pady=(5, 0))
            best_upload_value = tk.Label(speed_test_results_container, bg=bg, fg=fg,
                                         font=font, anchor=tk.CENTER, width=10, height=1, text="0Mbps")
            best_upload_value.grid(row=1, column=2, padx=(5), pady=(0))
        else:
            best_upload = tk.Label(speed_test_results_container, bg=bg, fg=fg,
                                   font=font, anchor=tk.CENTER, width=10, height=1, text="UPLOAD")
            best_upload.grid(row=0, column=2, padx=(5), pady=(5, 0))
            best_upload_value = tk.Label(speed_test_results_container, bg=bg, fg=fg,
                                         font=font, anchor=tk.CENTER, width=10, height=1, text=f"{max(upload_list)}Mbps")
            best_upload_value.grid(row=1, column=2, padx=(5), pady=(0))

        refresh_net()
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# refresh_net function refreshes network information every x amount of miliseconds

try:
    def refresh_net():
        global net_ref
        net_io = psutil.net_io_counters()

        sent_perc = (
            ((net_io.bytes_sent / 1024 / 1024 / 1024) / 50) * 100) / 1.65

        recv_perc = (
            ((net_io.bytes_recv / 1024 / 1024 / 1024) / 50) * 100) / 1.65

        if sent_perc < 10:
            total_sent_bar.configure(fg=asm_cyan)
        elif sent_perc > 10 and sent_perc < 20:
            total_sent_bar.configure(fg=asm_green)
        elif sent_perc > 20 and sent_perc < 30:
            total_sent_bar.configure(fg=asm_yellow)
        elif sent_perc > 30 and sent_perc < 50:
            total_sent_bar.configure(fg=asm_orange)
        elif sent_perc > 50:
            total_sent_bar.configure(fg=asm_red)

        if recv_perc < 10:
            total_rec_bar.configure(fg=asm_cyan)
        elif recv_perc > 10 and recv_perc < 20:
            total_rec_bar.configure(fg=asm_green)
        elif recv_perc > 20 and recv_perc < 30:
            total_rec_bar.configure(fg=asm_yellow)
        elif recv_perc > 30 and recv_perc < 50:
            total_rec_bar.configure(fg=asm_orange)
        elif recv_perc > 50:
            total_rec_bar.configure(fg=asm_red)

        # Update sent net bytes since boot

        total_sent_value.configure(text=f"{get_size(net_io.bytes_sent)}")

        # Assumes that the maximum sent bytes is 50GB daily and adjusts the bar accordingly

        if sent_perc < 1:
            total_sent_bar.configure(text="|")
        else:
            total_sent_bar.configure(text="|"*int(sent_perc))

        # Update recieved net bytes since boot

        total_rec_value.configure(text=f"{get_size(net_io.bytes_recv)}")

        # Assumes that the maximum received bytes is 50GB daily and adjusts the bar accordingly

        if recv_perc < 1:
            total_rec_bar.configure(text="|")
        else:
            total_rec_bar.configure(text="|"*int(recv_perc))

        net_ref = root.after(1000, refresh_net)
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
# get_speed function handles the speedtesting

try:
    def get_speed():

        def start_test():
            global download
            global upload
            global ping
            root.after_cancel(start_speedtest)

            with tqdm(total=3) as bar:
                st = speedtest.Speedtest()

                download = st.download() / 1000000
                download_list.append(f"{download:.2f}")

                if download < 5:
                    download_color.clear()
                    download_color.append(asm_red)
                    download_value.configure(fg=download_color)
                elif download > 5 and download < 10:
                    download_color.clear()
                    download_color.append(asm_orange)
                    download_value.configure(fg=download_color)
                elif download > 10 and download < 20:
                    download_color.clear()
                    download_color.append(asm_yellow)
                    download_value.configure(fg=download_color)
                elif download > 20 and download < 40:
                    download_color.clear()
                    download_color.append(asm_green)
                    download_value.configure(fg=download_color)
                elif download > 40:
                    download_color.clear()
                    download_color.append(asm_cyan)
                    download_value.configure(fg=download_color)

                try:
                    download_value.configure(
                        text=f"{download:.2f}Mbps")
                except Exception as e:
                    print(e)
                try:
                    best_download_value.configure(
                        text=f"{max(download_list)}Mbps")
                except Exception as e:
                    print(e)

                bar.update(1)

                upload = st.upload() / 1000000
                upload_list.append(f"{upload:.2f}")

                if upload < 3:
                    upload_color.clear()
                    upload_color.append(asm_red)
                    upload_value.configure(fg=upload_color)
                elif upload > 3 and upload < 6:
                    upload_color.clear()
                    upload_color.append(asm_orange)
                    upload_value.configure(fg=upload_color)
                elif upload > 6 and upload < 10:
                    upload_color.clear()
                    upload_color.append(asm_yellow)
                    upload_value.configure(fg=upload_color)
                elif upload > 10 and upload < 20:
                    upload_color.clear()
                    upload_color.append(asm_green)
                    upload_value.configure(fg=upload_color)
                elif upload > 20:
                    upload_color.clear()
                    upload_color.append(asm_cyan)
                    upload_value.configure(fg=upload_color)

                try:
                    upload_value.configure(text=f"{upload:.2f}Mbps")
                except Exception as e:
                    print(e)

                try:
                    best_upload_value.configure(
                        text=f"{max(upload_list)}Mbps")
                except Exception as e:
                    print(e)

                bar.update(1)

                ping = st.results.ping
                ping_list.append(f"{ping:.2f}")

                if ping < 10:
                    ping_color.clear()
                    ping_color.append(asm_cyan)
                    ping_value.configure(fg=ping_color)
                elif ping > 10 and ping < 20:
                    ping_color.clear()
                    ping_color.append(asm_green)
                    ping_value.configure(fg=ping_color)
                elif ping > 20 and ping < 30:
                    ping_color.clear()
                    ping_color.append(asm_yellow)
                    ping_value.configure(fg=ping_color)
                elif ping > 30 and ping < 50:
                    ping_color.clear()
                    ping_color.append(asm_orange)
                    ping_value.configure(fg=ping_color)
                elif ping > 50:
                    ping_color.clear()
                    ping_color.append(asm_red)
                    ping_value.configure(fg=ping_color)

                try:
                    ping_value.configure(text=f"{ping:.2f}ms")
                except Exception as e:
                    print(e)

                try:
                    best_ping_value.configure(
                        text=f"{min(ping_list)}ms")
                except Exception as e:
                    print(e)
                bar.update(1)

        ping_value.configure(text="...", fg=fg)
        download_value.configure(text="...", fg=fg)
        upload_value.configure(text="...", fg=fg)

        start_speedtest = root.after(10, start_test)


# all the basic stuff is setup in this section
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()

try:
    if __name__ == '__main__':
        multiprocessing.freeze_support()

        # Basic root options
        root = tk.Tk()
        root.title("Advanced System Monitor (BETA)")
        root.resizable(False, False)

        # Read color and theme from file
        color_list = []
        theme_selected = ""

        with open("Code\Config\config.txt", "r") as config:
            for line in config:
                for word in line.split():
                    if word.startswith("#"):
                        color_list.append(word)
                    elif "blackwhite" in word:
                        theme_selected = "blackwhite"
                    else:
                        pass

        # Presets
        # Color
        canvas_bg = color_list[0]
        bg = color_list[1]
        fg = color_list[2]
        sidemenu_bg = color_list[3]
        button_bg = color_list[4]

        # Color names
        asm_cyan = "#00a6ff"
        asm_green = "#00de2c"
        asm_yellow = "#ebca10"
        asm_orange = "#ff9100"
        asm_red = "#ba4545"

        # Fonts
        font = ("Oxygen", 15)
        time_font = ("Oxygen", 10)
        usage_font = ("Oxygen", 15, 'bold')
        net_font = ("Oxygen", 25)
        loading_font = ("Oxygen", 30)
        # Anchors
        anchor = tk.SW
        lbl_anchor = tk.W
        # Paths
        image_path = "Code\Visual\images"
        themes_image_path = "Code\Visual\images\Themes"

        # Other colors needed for certain tests
        download_color = []
        upload_color = []
        ping_color = []

        # Values are stored in these lists during tests
        cpu_max_usage_list = []
        cpu_max_usage_list.clear()

        gpu_max_load_list = []
        gpu_max_load_list.clear()

        gpu_max_temp_list = []
        gpu_max_temp_list.clear()

        gpu_max_vram_list = []
        gpu_max_vram_list.clear()

        gpu_max_vram_perc = []
        gpu_max_vram_perc.clear()

        gpu_max_fan_list = []
        gpu_max_fan_list.clear()

        gpu_max_fan_perc = []
        gpu_max_fan_perc.clear()

        ram_max_usage_list = []
        ram_max_usage_list.clear()

        swap_max_usage_list = []
        swap_max_usage_list.clear()

        ping_list = []
        ping_list.clear()

        download_list = []
        download_list.clear()

        upload_list = []
        upload_list.clear()

        # Set canvas
        canvas = tk.Canvas(root, width=1200, height=800,
                           bg=canvas_bg, highlightthickness=0)
        canvas.pack()

        # Set sidebar
        sidebar = tk.Frame(root, bg=sidemenu_bg)
        sidebar.place(relwidth=0.104, relheight=1, relx=0, rely=0)

        # Set home screen
        home()

        # Set all the sidebar icons and buttons
        # Different color icons will be used if certain themes are selected
        if theme_selected == "blackwhite":
            home_photo = PhotoImage(
                file=f"{image_path}\Black_Icons\homeCrop_black.png")

            homeButton = tk.Button(
                sidebar, bg=button_bg, fg="white", image=home_photo, width=124, height=105, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=home)
            homeButton.place(relx=0, rely=0)

            motherboard_photo = PhotoImage(
                file=f"{image_path}\Black_Icons\motherboardCrop_black.png")

            motherboardButton = tk.Button(
                sidebar, bg=sidemenu_bg, fg="white", image=motherboard_photo, width=124, height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=mobo)
            motherboardButton.place(relx=0, rely=0.127)

            cpu_photo = PhotoImage(
                file=f"{image_path}\Black_Icons\cpuCrop_black.png")

            cpuButton = tk.Button(sidebar, bg=sidemenu_bg, fg="white", width=124, image=cpu_photo,
                                  height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=cpu)
            cpuButton.place(relx=0, rely=0.252)

            gpu_photo = PhotoImage(
                file=f"{image_path}\Black_Icons\gpuCrop_black.png")

            gpuButton = tk.Button(sidebar, bg=sidemenu_bg, fg="white", width=124, image=gpu_photo,
                                  height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=gpu)
            gpuButton.place(relx=0, rely=0.377)

            ram_photo = PhotoImage(
                file=f"{image_path}\Black_Icons\pramCrop_black.png")

            ramButton = tk.Button(sidebar, bg=sidemenu_bg, fg="white", width=124, image=ram_photo,
                                  height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=ram)
            ramButton.place(relx=0, rely=0.502)

            hdd_photo = PhotoImage(
                file=f"{image_path}\Black_Icons\hddCrop_black.png")

            hddButton = tk.Button(sidebar, bg=sidemenu_bg, fg="white", width=124, image=hdd_photo,
                                  height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=drives)
            hddButton.place(relx=0, rely=0.627)

            fan_photo = PhotoImage(
                file=f"{image_path}\Black_Icons\pfanCrop_black.png")

            fanButton = tk.Button(sidebar, bg=sidemenu_bg, fg="white", width=124, image=fan_photo,
                                  height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=fans)
            fanButton.place(relx=0, rely=0.752)

            net_photo = PhotoImage(
                file=f"{image_path}\Black_Icons\pnetworkCrop_black.png")

            netButton = tk.Button(sidebar, bg=sidemenu_bg, fg="white", width=124, image=net_photo,
                                  height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=network)
            netButton.place(relx=0, rely=0.877)

        else:

            home_photo = PhotoImage(
                file=f"{image_path}\homeCrop.png")

            homeButton = tk.Button(
                sidebar, bg=button_bg, fg="white", image=home_photo, width=124, height=105, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=home)
            homeButton.place(relx=0, rely=0)

            motherboard_photo = PhotoImage(
                file=f"{image_path}\motherboardCrop.png")

            motherboardButton = tk.Button(
                sidebar, bg=sidemenu_bg, fg="white", image=motherboard_photo, width=124, height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=mobo)
            motherboardButton.place(relx=0, rely=0.127)

            cpu_photo = PhotoImage(
                file=f"{image_path}\cpuCrop.png")

            cpuButton = tk.Button(sidebar, bg=sidemenu_bg, fg="white", width=124, image=cpu_photo,
                                  height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=cpu)
            cpuButton.place(relx=0, rely=0.252)

            gpu_photo = PhotoImage(
                file=f"{image_path}\gpuCrop.png")

            gpuButton = tk.Button(sidebar, bg=sidemenu_bg, fg="white", width=124, image=gpu_photo,
                                  height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=gpu)
            gpuButton.place(relx=0, rely=0.377)

            ram_photo = PhotoImage(
                file=f"{image_path}\pramCrop.png")

            ramButton = tk.Button(sidebar, bg=sidemenu_bg, fg="white", width=124, image=ram_photo,
                                  height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=ram)
            ramButton.place(relx=0, rely=0.502)

            hdd_photo = PhotoImage(
                file=f"{image_path}\hddCrop.png")

            hddButton = tk.Button(sidebar, bg=sidemenu_bg, fg="white", width=124, image=hdd_photo,
                                  height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=drives)
            hddButton.place(relx=0, rely=0.627)

            fan_photo = PhotoImage(
                file=f"{image_path}\pfanCrop.png")

            fanButton = tk.Button(sidebar, bg=sidemenu_bg, fg="white", width=124, image=fan_photo,
                                  height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=fans)
            fanButton.place(relx=0, rely=0.752)

            net_photo = PhotoImage(
                file=f"{image_path}\pnetworkCrop.png")

            netButton = tk.Button(sidebar, bg=sidemenu_bg, fg="white", width=124, image=net_photo,
                                  height=98, bd=0, activebackground=button_bg, activeforeground="white", relief=SUNKEN, command=network)
            netButton.place(relx=0, rely=0.877)

        root.mainloop()
except Exception as e:
    f = open("errorFile.txt", "a")
    f.write("Get size function error: {}".format(e))
    f.close()
