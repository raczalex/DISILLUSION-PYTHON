import os
import platform
import wmi
import psutil
import winreg
import msvcrt
from utilities.print import _printg

class SystemInfo():
    def __init__(self):
        pass

    def get_windows_username(self):
        return os.environ.get('USERNAME')

    def get_desktop_name(self):
        return os.environ.get('COMPUTERNAME', 'Unknown')

    def get_os_version(self):
        if platform.system() == 'Windows':
            version_info = platform.win32_ver()
            return 'Windows', f"{version_info[0]} {version_info[1]}"
        else:
            return platform.system(), platform.version()

    def get_activation_state(self):
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", 0,
                                winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as key:
                value, _ = winreg.QueryValueEx(key, "DigitalProductId")
                return "Activated" if value else "Not Activated"
        except Exception as e:
            return "Not available"


    def get_cpu_info(self):
        c = wmi.WMI()
        cpu_info = c.Win32_Processor()[0]
        return cpu_info.Name

    def get_total_ram_size(self):
        return round(psutil.virtual_memory().total / (1024 ** 3))

    def get_motherboard_info(self):
        c = wmi.WMI()
        motherboard_info = c.Win32_BaseBoard()[0]
        return f"{motherboard_info.Manufacturer} {motherboard_info.Product}"

    def get_gpu_info(self):
        c = wmi.WMI()
        gpu_info = c.Win32_VideoController()
        return [(gpu.Caption, gpu.DriverVersion) for gpu in gpu_info]

    def get_tpm_state(self):
        try:
            tpm_objects = wmi.WMI(namespace="root/CIMv2/Security/MicrosoftTpm").Win32_Tpm()
            if tpm_objects:
                return "Enabled" if tpm_objects[0].IsEnabled_InitialValue else "Disabled"
            else:
                return "Not available"
        except Exception as e:
            return "Not available"


    def get_total_services(self):
        return len(list(psutil.win_service_iter()))
    
    def get_enabled_services_count(self):
        return sum(1 for service in psutil.win_service_iter() if service.status() == psutil.STATUS_RUNNING)

    def get_disabled_services_count(self):
        return sum(1 for service in psutil.win_service_iter() if service.status() == psutil.STATUS_STOPPED)

    def get_installed_apps_count(self):
        apps = [app for app in os.listdir(os.path.join(os.environ['PROGRAMFILES'])) if os.path.isdir(os.path.join(os.environ['PROGRAMFILES'], app))]
        return len(apps)

    def _start(self):
        _printg("Username", self.get_windows_username())
        _printg("Desktop Name",self.get_desktop_name())
        _printg("OS",f"{self.get_os_version()[0]} {self.get_os_version()[1]}")
        _printg("Activation State",self.get_activation_state())
        _printg("CPU",self.get_cpu_info())
        _printg("RAM Size", f"{self.get_total_ram_size()} GB")
        _printg("Motherboard",self.get_motherboard_info())
        for gpu in self.get_gpu_info():
            _printg(gpu[0],f"Driver Version: {gpu[1]}")
        _printg("TPM State",self.get_tpm_state())
        _printg("Total Services",self.get_total_services())
        _printg("Enabled Services",self.get_enabled_services_count())
        _printg("Disabled Services",self.get_disabled_services_count())
        _printg("Installed Apps",self.get_installed_apps_count())

        print('')
        _printg("SYSTEM INFO",'Press any key to exit.')

        while not msvcrt.kbhit():
            pass