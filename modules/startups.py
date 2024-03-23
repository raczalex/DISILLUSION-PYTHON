import subprocess
import platform
import winreg
import os
from utilities.print import _printg,_printr
from pystyle import Colors

class Startups():
    def __init__(self) -> None:
        pass

    def _getStartupAppsFromRegistry(self):
        startup_apps = []

        try:
            key_current_user = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
            i = 0
            while True:
                try:
                    app_name, _, _ = winreg.EnumValue(key_current_user, i)
                    key_path = r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run"
                    startup_apps.append((key_path, app_name))
                    i += 1
                except OSError:
                    break

            key_local_machine = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run")
            i = 0
            while True:
                try:
                    app_name, _, _ = winreg.EnumValue(key_local_machine, i)
                    key_path = r"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run"
                    startup_apps.append((key_path, app_name))
                    i += 1
                except OSError:
                    break

        except Exception as e:
            _printr('STARTUPS',f"Error accessing registry: {e}")

        finally:
            winreg.CloseKey(key_current_user)
            winreg.CloseKey(key_local_machine)

        return startup_apps

    def _getStartupAppsFromFolders(self):
        startup_apps = []

        try:
            all_users_startup_folder = os.path.join(os.environ['ALLUSERSPROFILE'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
            startup_apps.extend(self._getAppsFromFolder(all_users_startup_folder))

            current_user_startup_folder = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
            startup_apps.extend(self._getAppsFromFolder(current_user_startup_folder))

        except Exception as e:
            _printr('STARTUPS',f"Error accessing startup folders: {e}")

        return startup_apps

    def _getAppsFromFolder(self,folder_path):
        apps = []
        try:
            for file_name in os.listdir(folder_path):
                if file_name.lower() == 'desktop.ini':
                    continue
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    apps.append((file_name, file_path))
        except Exception as e:
            _printr('STARTUPS',f"Error accessing folder {folder_path}: {e}")

        return apps

    def _getStartupScheduledTasks(self):
        startup_scheduled_apps = []

        try:
            result = subprocess.run(['schtasks', '/query', '/FO', 'LIST'], capture_output=True, text=True)
            output_lines = result.stdout.split('\n')

            for line in output_lines:
                if line.startswith("TaskName:"):
                    app_name = line.split("TaskName:")[1].strip()
                    startup_scheduled_apps.append(app_name)

        except Exception as e:
            _printr('STARTUPS',f"ERROR retrieving scheduled tasks from Task Scheduler: {e}")

        return startup_scheduled_apps

    def _deleteSelectedItemFromStartup(self,selected_item):
        try:
            if isinstance(selected_item, tuple):
                key_path = selected_item[0]
                app_name = selected_item[1]
                if key_path.startswith("HKEY_CURRENT_USER"):
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", access=winreg.KEY_SET_VALUE)
                    winreg.DeleteValue(key, app_name)
                    winreg.CloseKey(key)
                    _printg('STARTUPS',f"Deleted from registry (HKEY_CURRENT_USER): {app_name}")
                elif key_path.startswith("HKEY_LOCAL_MACHINE"):
                    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run", access=winreg.KEY_SET_VALUE)
                    winreg.DeleteValue(key, app_name)
                    winreg.CloseKey(key)
                    _printg('STARTUPS',f"Deleted from registry (HKEY_LOCAL_MACHINE): {app_name}")
                else:
                    folder_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
                    file_path = os.path.join(folder_path, app_name)
                    os.remove(file_path)
                    _printg('STARTUPS',f"Deleted from folder: {app_name}")
            elif isinstance(selected_item, str):
                subprocess.run(['schtasks', '/delete', '/TN', selected_item, '/F'])
                _printg('STARTUPS',f"Deleted scheduled task: {selected_item}")
            else:
                print(f"   {Colors.white}[STARTUPS] {Colors.white}{Colors.light_red}Exiting the menu.")
        except Exception as e:
            _printr('STARTUPS',f"Error deleting item: {e}")
                

    def _delItem(self,selected_index,apps_list):
        if 0 <= selected_index < len(apps_list):
            selected_item = apps_list[selected_index]
            self._deleteSelectedItemFromStartup(selected_item)
        else:
           print(f"   {Colors.white}[STARTUPS] {Colors.white}{Colors.light_red}Exiting the menu.")