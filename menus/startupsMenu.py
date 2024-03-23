
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.startups import Startups
from utilities.print import _printy

class StartupsMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [STARTUPS]')

    def _displayMenu(self):
        
        options = [
            "Show & Delete Startup Apps From Registry",
            "Show & Delete Startup Apps From Startup Folders",
            "Show & Delete Startup Apps From Task Scheduler"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [STARTUPS]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    startup_apps_registry = Startups()._getStartupAppsFromRegistry()
                    startup_apps_registry_names = []
                    if startup_apps_registry:
                        for index, app in enumerate(startup_apps_registry, start=1):
                            startup_apps_registry_names.append(app[1])
                        _printThreeColumnsWithNumbersColored(startup_apps_registry_names)
                        print('')
                        selected_index = int(input(f"   {Colors.white}[STARTUPS]{Colors.light_green} Enter the number of your choice:{Colors.white} ")) - 1
                        print('')
                        Startups()._delItem(selected_index,startup_apps_registry)
                    else:
                        _printy('STARTUPS','It is empty nothing to do')
                    sleep(2)
                elif choice == 2:
                    print('')
                    startup_apps_folders = Startups()._getStartupAppsFromFolders()
                    startup_apps_folders_names = []
                    if startup_apps_folders:
                        for index, app in enumerate(startup_apps_folders, start=1):
                            startup_apps_folders_names.append(app[1])
                        _printThreeColumnsWithNumbersColored(startup_apps_folders_names)
                        print('')
                        selected_index = int(input(f"   {Colors.white}[STARTUPS]{Colors.light_green} Enter the number of your choice:{Colors.white} ")) - 1
                        print('')
                        Startups()._delItem(selected_index,startup_apps_folders)
                    else:
                        _printy('STARTUPS','It is empty nothing to do')
                    sleep(2)
                elif choice == 3:
                    print('')
                    startup_apps_scheduled_tasks = Startups()._getStartupScheduledTasks()
                    startup_apps_scheduled_tasks_names = []
                    if startup_apps_scheduled_tasks:
                        for index, app in enumerate(startup_apps_scheduled_tasks, start=1):
                            startup_apps_scheduled_tasks_names.append(app.split('\\')[-1])
                        _printThreeColumnsWithNumbersColored(startup_apps_scheduled_tasks_names)
                        print('')
                        selected_index = int(input(f"   {Colors.white}[STARTUPS]{Colors.light_green} Enter the number of your choice:{Colors.white} ")) - 1
                        print('')
                        Startups()._delItem(selected_index,startup_apps_scheduled_tasks)
                    else:
                        _printy('STARTUPS','It is empty nothing to do')
                    sleep(2)
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")